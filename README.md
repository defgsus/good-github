## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-01-27](docs/good-messages/2023/2023-01-27.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,100,909 were push events containing 3,261,374 commit messages that amount to 253,841,463 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 46 messages:


## [Metvertz/eths23](https://github.com/Metvertz/eths23)@[9b461456e9...](https://github.com/Metvertz/eths23/commit/9b461456e9f8168c833c0c36040638103a246b4e)
#### Friday 2023-01-27 00:24:40 by Mitchell Everetts

Addition of my url to the page

I thought I had done this twice already, but I was clearly having some kind of fever dream because not only was it not there, I checked my own fork and it wasn't updated, which has led me to the conclusion that I, in an out of body homework induced experienced, edited my repository in the spirit realm and thus the changes were not reflected in the material realm. 

Signed-off-by: Mitchell Everetts <77137408+Metvertz@users.noreply.github.com>

---
## [andro951/WeaponEnchantments](https://github.com/andro951/WeaponEnchantments)@[39e6093878...](https://github.com/andro951/WeaponEnchantments/commit/39e60938787af2e154ad25f2f7ee8d850f4ecca1)
#### Friday 2023-01-27 00:34:52 by andro951

1.0.2.0(26JAN23)
     -Added Armor Reduction per level on Armor and accessories.  (Similar to the crit chance per level on weapons)
          Damage Reduction values do not scale off the Global Enchantment Strength Multiplier.  Instead, they have setpoints in the config with the defaults below:

                                      Damage Reduction per level
                                    Armor                              Accessory
               Journey     0.625% (25% at 40)      0.3125% (12.5% at 40)
                Normal     0.25% (10% at 40)         0.125% (5% at 40)
                Expert      0.1875% (7.5% at 40)     0.09375% (3.75% at 40)
                Master     0.125% (5% at 40)          0.0625% (2.5% at 40)
           These values are based on the vote from 27SEP22 when I pitched the idea.  Sorry this took so long.  I took a break from modding because I got very burnt out.
     -Added config options to completely disable the damage reduction per level or customize the amount of damage reduction received.
     -Added tooltips for Damage Reduction per level and crit chance per level.
     -Items that consume mana, but aren't weapons are now considered tools. (@EARLE)
     -Fixed size enchantments on armor/accessories not increasing the size of held items.  They still worked on projectiles before.(@niknik98)
     -Fixed being able to change an armor's armor set bonus with infusion without pressing finalize.  (aka for free, but it would reset upon save/quit)
     -Added config option to disable armor infusion.  This will prevent you consuming armor for infusion and ignore infusions on existing armor, but still remembers the infusions.(@Yureii)
     -Updated Infusion Damage Multiplier config setting.  Setting it to 1000 (aka 1x which is no bonus damage) will now prevent you from consuming weapons for infusion.(@Yureii)
     -Added automatic checking of New and Changed wiki txt files and a change summary
     -Added ItemExperience wiki page

---
## [vulpineawoo/solanum](https://github.com/vulpineawoo/solanum)@[06c5309534...](https://github.com/vulpineawoo/solanum/commit/06c53095343c2756208f6398bb7e00fb2cbe46dd)
#### Friday 2023-01-27 00:55:09 by Ed Kellett

m_sasl: Remove implicit abort on registration

This doesn't make sense in a world where post-registration SASL is
allowed, and should fix one case of an annoying login desync that's seen
in the real world.

Specifically, when a client sends its final AUTHENTICATE and Atheme
receives it, it sends an SVSLOGIN for that client. If the client sends
us its CAP END *before* we see the SVSLOGIN, the implicit abort will try
to abort the SASL session that's already succeeded.

Atheme interprets this as an instruction to forget about the successful
SASL session; you'll connect unidentified. But it's already sent
SVSLOGIN, which will log the client in ircd-side, causing ircd and
services views to differ until the user authenticates again manually.

I think allowing a SASL session to be aborted when it has already
succeeded is an Atheme bug, and it can still be triggered without this
change. But our behaviour here seems silly anyway.

---
## [Offroaders123/NBTify](https://github.com/Offroaders123/NBTify)@[2fe23c07fe...](https://github.com/Offroaders123/NBTify/commit/2fe23c07fed3abcc9c05b52dccc2826b36c3c072)
#### Friday 2023-01-27 01:18:28 by Offroaders123

Deno-Minecraft Help + Wow, Noice!

Realized while looking at my progress from last night with new eyes, it would be a more efficient way to take a similar path with the SNBT implementation similar to how I started the library, with NBT.js. Once I have a working implementation with the reference library, which already works, I can rebuild my own code from that version, then further tweak everything until it becomes the code I wanted to make to start with.

This way works really well for making sure not to skip over things on the way though reimplementing the format with your own code. If I simply go though each part of the original code, and just rewrite it line by line, but my own way, I miss the big picture of how it all works together, as a whole. If you make little patches here and there to turn it into your own code, you can see how each of your ideas/misinterpretations will affect the result outcome of the program being able to run. So, rather than a key feature erroring out because you haven't just rewritten it yourself yet, you can see that it was actually an error in the logic of your new idea, which allows you to fix it while you know where the error happened. If you make a logic error that doesn't show up until later, you will have to try and figure out where the problem started later, and it will give you more curveballs along the way.

Glad I remembered about this technique, I need to remind myself to do this while working on STE's codebase too, rather than starting from scratch alltogether again, like I tend to want to do. I think I should try this out for Menu Drop and maybe Num Text too, as the current reworked versions are missing key features that the legacy ones have. So, now that I have the modern setup essentially nearly figured out, I should try to fit the legacy codebase in there, and modify it with the little patches like mentioned above, allowing me to ensure the features I already 'logically implemented' into the codebase can be kept inside of the modern versions too.

About the 'Wow, Noice!' part, I can't believe patching in part of Deno-Minecraft actually worked! I had to change some of the API logic with the NBT primitives, since Deno-Minecraft uses custom classes, unlike NBTify which uses direct JavaScript primitives (where possible).

It works so nice to the extent that I can read an NBT file of 'x' type, stringify it to SNBT, re-read it as a JavaScript object again, then serialize that object back down to an NBT buffer, and the resulting NBT buffer is byte-for-byte exactly the same! F-ing awesome, I love it :D

---
## [eun0115/kernel-ginkgo](https://github.com/eun0115/kernel-ginkgo)@[53354d843c...](https://github.com/eun0115/kernel-ginkgo/commit/53354d843c3ca08fef8ffeac8ccc6d56f3c16709)
#### Friday 2023-01-27 01:54:23 by Joonsoo Kim

mm/page_alloc: use ac->high_zoneidx for classzone_idx

Patch series "integrate classzone_idx and high_zoneidx", v5.

This patchset is followup of the problem reported and discussed two years
ago [1, 2].  The problem this patchset solves is related to the
classzone_idx on the NUMA system.  It causes a problem when the lowmem
reserve protection exists for some zones on a node that do not exist on
other nodes.

This problem was reported two years ago, and, at that time, the solution
got general agreements [2].  But it was not upstreamed.

[1]: http://lkml.kernel.org/r/20180102063528.GG30397@yexl-desktop
[2]: http://lkml.kernel.org/r/1525408246-14768-1-git-send-email-iamjoonsoo.kim@lge.com

This patch (of 2):

Currently, we use classzone_idx to calculate lowmem reserve proetection
for an allocation request.  This classzone_idx causes a problem on NUMA
systems when the lowmem reserve protection exists for some zones on a node
that do not exist on other nodes.

Before further explanation, I should first clarify how to compute the
classzone_idx and the high_zoneidx.

- ac->high_zoneidx is computed via the arcane gfp_zone(gfp_mask) and
  represents the index of the highest zone the allocation can use

- classzone_idx was supposed to be the index of the highest zone on the
  local node that the allocation can use, that is actually available in
  the system

Think about following example.  Node 0 has 4 populated zone,
DMA/DMA32/NORMAL/MOVABLE.  Node 1 has 1 populated zone, NORMAL.  Some
zones, such as MOVABLE, doesn't exist on node 1 and this makes following
difference.

Assume that there is an allocation request whose gfp_zone(gfp_mask) is the
zone, MOVABLE.  Then, it's high_zoneidx is 3.  If this allocation is
initiated on node 0, it's classzone_idx is 3 since actually
available/usable zone on local (node 0) is MOVABLE.  If this allocation is
initiated on node 1, it's classzone_idx is 2 since actually
available/usable zone on local (node 1) is NORMAL.

You can see that classzone_idx of the allocation request are different
according to their starting node, even if their high_zoneidx is the same.

Think more about these two allocation requests.  If they are processed on
local, there is no problem.  However, if allocation is initiated on node 1
are processed on remote, in this example, at the NORMAL zone on node 0,
due to memory shortage, problem occurs.  Their different classzone_idx
leads to different lowmem reserve and then different min watermark.  See
the following example.

root@ubuntu:/sys/devices/system/memory# cat /proc/zoneinfo
Node 0, zone      DMA
  per-node stats
...
  pages free     3965
        min      5
        low      8
        high     11
        spanned  4095
        present  3998
        managed  3977
        protection: (0, 2961, 4928, 5440)
...
Node 0, zone    DMA32
  pages free     757955
        min      1129
        low      1887
        high     2645
        spanned  1044480
        present  782303
        managed  758116
        protection: (0, 0, 1967, 2479)
...
Node 0, zone   Normal
  pages free     459806
        min      750
        low      1253
        high     1756
        spanned  524288
        present  524288
        managed  503620
        protection: (0, 0, 0, 4096)
...
Node 0, zone  Movable
  pages free     130759
        min      195
        low      326
        high     457
        spanned  1966079
        present  131072
        managed  131072
        protection: (0, 0, 0, 0)
...
Node 1, zone      DMA
  pages free     0
        min      0
        low      0
        high     0
        spanned  0
        present  0
        managed  0
        protection: (0, 0, 1006, 1006)
Node 1, zone    DMA32
  pages free     0
        min      0
        low      0
        high     0
        spanned  0
        present  0
        managed  0
        protection: (0, 0, 1006, 1006)
Node 1, zone   Normal
  per-node stats
...
  pages free     233277
        min      383
        low      640
        high     897
        spanned  262144
        present  262144
        managed  257744
        protection: (0, 0, 0, 0)
...
Node 1, zone  Movable
  pages free     0
        min      0
        low      0
        high     0
        spanned  262144
        present  0
        managed  0
        protection: (0, 0, 0, 0)

- static min watermark for the NORMAL zone on node 0 is 750.

- lowmem reserve for the request with classzone idx 3 at the NORMAL on
  node 0 is 4096.

- lowmem reserve for the request with classzone idx 2 at the NORMAL on
  node 0 is 0.

So, overall min watermark is:
allocation initiated on node 0 (classzone_idx 3): 750 + 4096 = 4846
allocation initiated on node 1 (classzone_idx 2): 750 + 0 = 750

Allocation initiated on node 1 will have some precedence than allocation
initiated on node 0 because min watermark of the former allocation is
lower than the other.  So, allocation initiated on node 1 could succeed on
node 0 when allocation initiated on node 0 could not, and, this could
cause too many numa_miss allocation.  Then, performance could be
downgraded.

Recently, there was a regression report about this problem on CMA patches
since CMA memory are placed in ZONE_MOVABLE by those patches.  I checked
that problem is disappeared with this fix that uses high_zoneidx for
classzone_idx.

http://lkml.kernel.org/r/20180102063528.GG30397@yexl-desktop

Using high_zoneidx for classzone_idx is more consistent way than previous
approach because system's memory layout doesn't affect anything to it.
With this patch, both classzone_idx on above example will be 3 so will
have the same min watermark.

allocation initiated on node 0: 750 + 4096 = 4846
allocation initiated on node 1: 750 + 4096 = 4846

One could wonder if there is a side effect that allocation initiated on
node 1 will use higher bar when allocation is handled on local since
classzone_idx could be higher than before.  It will not happen because the
zone without managed page doesn't contributes lowmem_reserve at all.

Reported-by: Ye Xiaolong <xiaolong.ye@intel.com>
Signed-off-by: Joonsoo Kim <iamjoonsoo.kim@lge.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Tested-by: Ye Xiaolong <xiaolong.ye@intel.com>
Reviewed-by: Baoquan He <bhe@redhat.com>
Acked-by: Vlastimil Babka <vbabka@suse.cz>
Acked-by: David Rientjes <rientjes@google.com>
Cc: Johannes Weiner <hannes@cmpxchg.org>
Cc: Michal Hocko <mhocko@kernel.org>
Cc: Minchan Kim <minchan@kernel.org>
Cc: Mel Gorman <mgorman@techsingularity.net>
Link: http://lkml.kernel.org/r/1587095923-7515-1-git-send-email-iamjoonsoo.kim@lge.com
Link: http://lkml.kernel.org/r/1587095923-7515-2-git-send-email-iamjoonsoo.kim@lge.com
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: celtare21 <celtare21@gmail.com>

---
## [vascorsd/dango](https://github.com/vascorsd/dango)@[d066b00d27...](https://github.com/vascorsd/dango/commit/d066b00d27553f1ef972341e980749356115cd2e)
#### Friday 2023-01-27 03:03:10 by Vasco Dias

updates: bumped a bunch of verisions. fix semanticdb weird fuck up of version by randomly updating sbt plugins

really, dafuq is - Error downloading org.scalameta:semanticdb-scalac_2.13.10:4.4.30 - ?? where is it coming from? who dafuq controls this 4.4.30 version? it.s not in any version of anything updated. god I hate not understanding how my tooling is working.

---
## [dahga/Little-Bits](https://github.com/dahga/Little-Bits)@[c6ea83a9d0...](https://github.com/dahga/Little-Bits/commit/c6ea83a9d0fd2d5a40f1484385825f9256138b76)
#### Friday 2023-01-27 04:25:59 by Robyn

Linda (Business Owner) - Robyn


Persona
Linda – Business Owner
Linda is 35 years old and lives in a small town in MN. She and her husband just started their own brewery. While her husband oversees making the beer and finding the right ingredients, she oversees everything else. Linda is comfortable with schedules and puts everything in her calendar on her cell phone as things come up. When Linda is at the computer, she uses the website to see how much time she has between tasks. Although she is not computer savvy, she uses what is most convenient to her. Linda is in charge of creating community events to bring people together at the brewery and ensuring all the servers are scheduled as needed. She is also in charge of the local bands that are able to play at the brewery at least once a week. She wants everyone to be happy and to establish a good relation in the community.


User Stories

User Story 1 (Linda, business owner)
Linda has a hectic day and realizes since the grand opening several bands have reached out and had reviews scheduled on Monday. She doesn’t know how much time she has between the reviews to complete the regular daily requirements of the brewery. Although the brewery opens at 11 am all her band reviews are 11 am and after. She just made it to the brewery at 9 am and viewed her calendar. She views the countdown clock and sees she has exactly 1.50 hours until her first review. Without eating breakfast or starting her cleaning she jumps on the jobs. She gets most of the cleaning done and her next review is at 1:30 pm and she has another every 30 min thereafter. The first review lasted 45 min, and an employee was called in sick. Linda agreed to help where needed to keep the flow of business. She realizes with the countdown clock she now has 1.1 hours until the next review and it’s always busier after lunch. With the limited time she has she is able to call the bands and ask that they do the review in front of the guests. This works out perfectly, the reviews are given a 1 – 10 score and all the customers are happy to put their vote in. Linda was able to get through the reviews and made progress with the local bands.

User Story 2 (Linda, business owner)
Linda decided she would work from home today for the brewery and be on call when needed. She logs into the website and reviews her calendar. She sees there is no countdown, but the business is in the summer parade in just 3 days! She forgot to put a countdown on the event. Now that she has added the countdown, she can see that she has 2 days and 12 hours left. She scrambles to the store to get things as needed and rushes her online delivery orders. The countdown helps, and when she doesn’t add it to her calendar events, she forgets about them.

---
## [Henderythmix/Terminal-Bible](https://github.com/Henderythmix/Terminal-Bible)@[43864d8ade...](https://github.com/Henderythmix/Terminal-Bible/commit/43864d8ade3e7b9fd5ba2e26e59c37c3656a6441)
#### Friday 2023-01-27 04:46:35 by Henderythmix

My friends won't shut up about this error lmao

It's ok I forgive them :D

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[9e69e5d6ac...](https://github.com/san7890/bruhstation/commit/9e69e5d6acae10bf0941155c418ea3b9194668e5)
#### Friday 2023-01-27 05:03:13 by LemonInTheDark

Minor plane cube cleanup (#72038)

## About The Pull Request

[Fixes area lighting not working on turf change in multiz
cases](https://github.com/tgstation/tgstation/commit/7b92deffbca92a834cb0a361fd685de51a12ea53)

If you modify a area lit turf when using multiz, it'd end up using the
wrong plane for its light, because of stupid shit on my part.
Stupid shit resolved

[Fixes some uses of plane masters that only specified one rather then
all](https://github.com/tgstation/tgstation/commit/a59ec96d29710b967bf8b3ffe8210b230cb194b3)

We almost never only want to show SOME hidden planes. 
Should really make a helper for this someday

---
## [TurtleShroom/TSP_STORYTIME_RIDES_AGAIN](https://github.com/TurtleShroom/TSP_STORYTIME_RIDES_AGAIN)@[731b437cae...](https://github.com/TurtleShroom/TSP_STORYTIME_RIDES_AGAIN/commit/731b437cae22b225da6cab12dfc82d38721fd8fd)
#### Friday 2023-01-27 05:13:11 by TURTLESHROOM

Major

1. Imported Hard Lemonade. In tribute to Weebl's Amazing Horse... I guess I'd better not show you where the lemonade is made.

2. You can now find out where the lemonade is made if you look for the right animals.

3. Revised Toxic Resistance to its "Biotech" EP inverse in multiple files..

4. The Weezer Gene is a blessing from Randy, not an unnamed deity.

5. When speaking to each other, Pawns can now make fun of me or discuss how JEREMIAH WAS A BULLFROG! HE WAS A GOOD FRIEND OF MINE!

6. Certain Mods ow allow the Black Steel Tiles and the Hhhite Tiles to block Infestations.

7. Fixed grammar and punctuation where found.

8. Added missing entry for Pepsi and the Pepsi Frog. Pepsi sucks and I'll be adding a Coca-Cola Frog soon.

9. The Flying Frog, being an Archotech lifeform, can no longer get poisoned.

10. If you have the Lord of the Rim Elf Mod, you can make some Gnome Dishes with Elf Flour.

11. If you have the Mod, the Grim Reaper imitator Animal now has a proper skeletal body.

12. Imported code to allow Cyper Frogs to spawn with the Vanilla Factions Expanded Mechanoid's Faction.

---
## [boost-entropy-azure/prime-data-hub](https://github.com/boost-entropy-azure/prime-data-hub)@[8b92a1e515...](https://github.com/boost-entropy-azure/prime-data-hub/commit/8b92a1e515d1f0e0c68d9471fcb1163432dae487)
#### Friday 2023-01-27 05:55:23 by Stephen Kao

Experience-7891: Disable organization-specific fetches as admin (#7928)

This changeset disables a few Organization-specific requests to mitigate the number of 404s we're getting as admins try to fetch Organization resources:
- Organization settings
- Deliveries
- Submissions

There's not a one-size-fits-all solution here given the different fetch mechanisms we already have and how the data is rendered, so I tried to add minimal changes to prevent disrupting anything down the line.  I think going forward, we can make a generic `useOrganizationQuery` hook that'll automatically be disabled if the user is logged in as an admin without impersonating an Organization.  There are a lot of layers with our fetching that in my opinion should be untangled, but that's out of the scope of this pull request.

---
## [MostlyOperational18119/Mostly-Operational-Power-Play](https://github.com/MostlyOperational18119/Mostly-Operational-Power-Play)@[49625a3579...](https://github.com/MostlyOperational18119/Mostly-Operational-Power-Play/commit/49625a3579e11de0ef6bbd54ad44c6bb79a7c104)
#### Friday 2023-01-27 06:20:21 by TedArmenston

HOLY SHIT IT STACKED CONES. IT ACTUALLY DID IT (needs some fine tuning on the approach, and some obvious speed improvements, but god DAMN she's a beauty

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[5c6f5439b7...](https://github.com/pytorch/pytorch/commit/5c6f5439b7e6a5e63a68b36b4cf093a00d46e8be)
#### Friday 2023-01-27 06:25:12 by Edward Z. Yang

Implement SymBool (#92149)

We have known for a while that we should in principle support SymBool as a separate concept from SymInt and SymFloat ( in particular, every distinct numeric type should get its own API). However, recent work with unbacked SymInts in, e.g., https://github.com/pytorch/pytorch/pull/90985 have made this a priority to implement. The essential problem is that our logic for computing the contiguity of tensors performs branches on the passed in input sizes, and this causes us to require guards when constructing tensors from unbacked SymInts. Morally, this should not be a big deal because, we only really care about the regular (non-channels-last) contiguity of the tensor, which should be guaranteed since most people aren't calling `empty_strided` on the tensor, however, because we store a bool (not a SymBool, prior to this PR it doesn't exist) on TensorImpl, we are forced to *immediately* compute these values, even if the value ends up not being used at all. In particular, even when a user allocates a contiguous tensor, we still must compute channels-last contiguity (as some contiguous tensors are also channels-last contiguous, but others are not.)

This PR implements SymBool, and makes TensorImpl use SymBool to store the contiguity information in ExtraMeta. There are a number of knock on effects, which I now discuss below.

* I introduce a new C++ type SymBool, analogous to SymInt and SymFloat. This type supports logical and, logical or and logical negation. I support the bitwise operations on this class (but not the conventional logic operators) to make it clear that logical operations on SymBool are NOT short-circuiting. I also, for now, do NOT support implicit conversion of SymBool to bool (creating a guard in this case). This does matter too much in practice, as in this PR I did not modify the equality operations (e.g., `==` on SymInt) to return SymBool, so all preexisting implicit guards did not need to be changed. I also introduced symbolic comparison functions `sym_eq`, etc. on SymInt to make it possible to create SymBool. The current implementation of comparison functions makes it unfortunately easy to accidentally introduce guards when you do not mean to (as both `s0 == s1` and `s0.sym_eq(s1)` are valid spellings of equality operation); in the short term, I intend to prevent excess guarding in this situation by unit testing; in the long term making the equality operators return SymBool is probably the correct fix.
* ~~I modify TensorImpl to store SymBool for the `is_contiguous` fields and friends on `ExtraMeta`. In practice, this essentially meant reverting most of the changes from https://github.com/pytorch/pytorch/pull/85936 . In particular, the fields on ExtraMeta are no longer strongly typed; at the time I was particularly concerned about the giant lambda I was using as the setter getting a desynchronized argument order, but now that I have individual setters for each field the only "big list" of boolean arguments is in the constructor of ExtraMeta, which seems like an acceptable risk. The semantics of TensorImpl are now that we guard only when you actually attempt to access the contiguity of the tensor via, e.g., `is_contiguous`. By in large, the contiguity calculation in the implementations now needs to be duplicated (as the boolean version can short circuit, but the SymBool version cannot); you should carefully review the duplicate new implementations. I typically use the `identity` template to disambiguate which version of the function I need, and rely on overloading to allow for implementation sharing. The changes to the `compute_` functions are particularly interesting; for most of the functions, I preserved their original non-symbolic implementation, and then introduce a new symbolic implementation that is branch-less (making use of our new SymBool operations). However, `compute_non_overlapping_and_dense` is special, see next bullet.~~ This appears to cause performance problems, so I am leaving this to an update PR.
* (Update: the Python side pieces for this are still in this PR, but they are not wired up until later PRs.) While the contiguity calculations are relatively easy to write in a branch-free way, `compute_non_overlapping_and_dense` is not: it involves a sort on the strides. While in principle we can still make it go through by using a data oblivious sorting network, this seems like too much complication for a field that is likely never used (because typically, it will be obvious that a tensor is non overlapping and dense, because the tensor is contiguous.) So we take a different approach: instead of trying to trace through the logic computation of non-overlapping and dense, we instead introduce a new opaque operator IsNonOverlappingAndDenseIndicator which represents all of the compute that would have been done here. This function returns an integer 0 if `is_non_overlapping_and_dense` would have returned `False`, and an integer 1 otherwise, for technical reasons (Sympy does not easily allow defining custom functions that return booleans). The function itself only knows how to evaluate itself if all of its arguments are integers; otherwise it is left unevaluated. This means we can always guard on it (as `size_hint` will always be able to evaluate through it), but otherwise its insides are left a black box. We typically do NOT expect this custom function to show up in actual boolean expressions, because we will typically shortcut it due to the tensor being contiguous. It's possible we should apply this treatment to all of the other `compute_` operations, more investigation necessary. As a technical note, because this operator takes a pair of a list of SymInts, we need to support converting `ArrayRef<SymNode>` to Python, and I also unpack the pair of lists into a single list because I don't know if Sympy operations can actually validly take lists of Sympy expressions as inputs. See for example `_make_node_sizes_strides`
* On the Python side, we also introduce a SymBool class, and update SymNode to track bool as a valid pytype. There is some subtlety here: bool is a subclass of int, so one has to be careful about `isinstance` checks (in fact, in most cases I replaced `isinstance(x, int)` with `type(x) is int` for expressly this reason.) Additionally, unlike, C++, I do NOT define bitwise inverse on SymBool, because it does not do the correct thing when run on booleans, e.g., `~True` is `-2`. (For that matter, they don't do the right thing in C++ either, but at least in principle the compiler can warn you about it with `-Wbool-operation`, and so the rule is simple in C++; only use logical operations if the types are statically known to be SymBool). Alas, logical negation is not overrideable, so we have to introduce `sym_not` which must be used in place of `not` whenever a SymBool can turn up. To avoid confusion with `__not__` which may imply that `operators.__not__` might be acceptable to use (it isn't), our magic method is called `__sym_not__`. The other bitwise operators `&` and `|` do the right thing with booleans and are acceptable to use.
* There is some annoyance working with booleans in Sympy. Unlike int and float, booleans live in their own algebra and they support less operations than regular numbers. In particular, `sympy.expand` does not work on them. To get around this, I introduce `safe_expand` which only calls expand on operations which are known to be expandable.

TODO: this PR appears to greatly regress performance of symbolic reasoning. In particular, `python test/functorch/test_aotdispatch.py -k max_pool2d` performs really poorly with these changes. Need to investigate.

Signed-off-by: Edward Z. Yang <ezyang@meta.com>
Pull Request resolved: https://github.com/pytorch/pytorch/pull/92149
Approved by: https://github.com/albanD, https://github.com/Skylion007

---
## [Nyeriah/azerothcore-wotlk](https://github.com/Nyeriah/azerothcore-wotlk)@[ef949f9ff0...](https://github.com/Nyeriah/azerothcore-wotlk/commit/ef949f9ff0a89e837c67258d7e199da1706bc438)
#### Friday 2023-01-27 09:03:32 by ICXCNIKA

fix(DB/Locale): deDE fix request items texts #02 (#14615)

Process of translation: only original sources of deDE texts by
researching multiple sources, reverse translation by searching for
related quest items/NPCs and using these names to reconstruct a proper
translation.

This fixes the terms

Coldtooth-Mine (Eisbeißermine), Doomhammer (Schicksalshammer), Fizzle
(Zischel), Fizzledowser (Rutenwünschels), Fizzlebub (Zischelbub),
Burning Blade (Brennende Klinge), Ashenvale (Eschental),
Bloodscalp/s/stamm (Blutskalpe, Blutskalpstamm),
Darkspeartrolle/Darkspears/Darkspearstamm (Dunkelspeere,
Dunkelspeertrolle, -stamm), Moonglade (Mondlichtung), Starblaze
(Sternenschauer), Shadowglen (Laubschattental), Darrowshire (Darroheim),
Booty Bay (Beutebucht), Ratchet (Ratschet), Dizzywig (Flunkerblick),
Hearthglen (Herdweiler), Chillwindspitze (Zugwindspitze), Stormrage
(Sturmgrimm), Stormpike (Sturmlanze/n), Ironforge (Eisenschmiede),
Thunderhorn (Donnerhörner), Steamboil (Kesseldampf), Twilight-Hammer,
-klan (Schattenhammer/Schattenhammerklan), Fathom-Kern (Tiefenkern),
Blackfathom Deeps (Tiefschwarze Grotte), Blackrock-* (Schwarzfels-*),
Hawkwind (Falkenwind), Feathermoon (Mondfeder), Moonrage (Mondzorn),
Firemane (Feuermähne), Searingblade (Sengende Klinge), Ragefireabgrund
(Flammenschlund), Ironbands Areal (Eisenbands Lager), Zandalar
(Zandalari), Southshore (Süderstade)

for quest progress/request text entries for the deDE localisation with
proper casus/declension (these are not proper translated names of
locations/NPCs that have been left over by Blizzard since their language
localisations in TBC in 2006 and onward).

Added missing progress/request text entries for 308, 311, 417, 1644,
1787, 5059, 5060, 5721, 6004, 6023, 6025, 6187, 8042, 8043, 8044, 8046,
8047, 8048, 8050-8079, 8102, 8107, 8108, 8111, 8112, 8113, 8117, 8118,
8142, 8143, 8147, 8183-8195, 8238, 8239, 8240, 8243, 8246, 8860, 9594,
9692, 9707, 10414, 10415, 10919, 11451. (A lot of them are
Zandalari/Zul'Gurub related quests.)

Replaced post-Cataclysm progress/request text entries for 933, 935,
6387, 7383.

Fixed a wrong $R with plain text at progress/request text for 9147.

Added missing female gender equivalent to 6391.

(There are probably more changes in the file that aren't further
explained here as it was hard to keep track of everything. If you think
I made a mistake or have questions please contact me directly.)

<!-- First of all, THANK YOU for your contribution. -->

## Changes Proposed:
-  Fixing a lot in the quest_request_items_locale table.

## Issues Addressed:
<!-- If your fix has a relating issue, link it below -->
- Fixing some of the tasks in
https://github.com/azerothcore/azerothcore-wotlk/issues/14244
Referring to my other two bug reports from CC Github:
- https://github.com/chromiecraft/chromiecraft/issues/4697
- https://github.com/chromiecraft/chromiecraft/issues/4745

## SOURCE:
<!-- If you can, include a source that can strengthen your claim -->
- Read the text on top.

## Tests Performed:
<!-- Does it build without errors? Did you test in-game? What did you
test? On which OS did you test? Describe any other tests performed -->
- Not tested.


## How to Test the Changes:
<!-- Describe in a detailed step-by-step order how to test the changes
-->
All of the changes are to reward texts of quests, can be tested by
completing quests or simply reviewing the changed file.

## Known Issues and TODO List:
<!-- Is there anything else left to do after this PR? -->

- [ ]
- [ ]

<!-- If you intend to contribute repeatedly to our project, it is a good
idea to join our discord channel. We set ranks for our contributors and
give them access to special resources or knowledge:
https://discord.com/invite/DasJqPba)
Do not remove the instructions below about testing, they will help users
to test your PR -->
## How to Test AzerothCore PRs
 
When a PR is ready to be tested, it will be marked as **[WAITING TO BE
TESTED]**.

You can help by testing PRs and writing your feedback here on the PR's
page on GitHub. Follow the instructions here:

http://www.azerothcore.org/wiki/How-to-test-a-PR

**REMEMBER**: when testing a PR that changes something **generic** (i.e.
a part of code that handles more than one specific thing), the tester
should not only check that the PR does its job (e.g. fixing spell XXX)
but **especially** check that the PR does not cause any regression (i.e.
introducing new bugs).

**For example**: if a PR fixes spell X by changing a part of code that
handles spells X, Y, and Z, we should not only test X, but **we should
test Y and Z as well**.

---
## [Citadel-Station-13/Citadel-Station-13-RP](https://github.com/Citadel-Station-13/Citadel-Station-13-RP)@[287fb079d1...](https://github.com/Citadel-Station-13/Citadel-Station-13-RP/commit/287fb079d1d52c8f244c7f08b3efa18de567f1cd)
#### Friday 2023-01-27 09:17:36 by Felix

Whitelist backend changes (#4996)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Whitelist are run by name, so renaming a whitelisted species also needs
an update to the WL as well.
Removes a shitty gimmick of a mirror most people dont have access to
because its a fucking nightmare of conditions we partially removed
and a fix for both runtimes and uninteded stat cheating
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
del: Removed the code behind the raider mirror
fix: fixed the shadekin traits applying to non shadekin
config: changed WL using Species ID rather than name
refactor: changed character species to always have a superspecies_id
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Danda420/kernel_xiaomi_sm8250](https://github.com/Danda420/kernel_xiaomi_sm8250)@[81acbf1b37...](https://github.com/Danda420/kernel_xiaomi_sm8250/commit/81acbf1b37e41bf4f012f1a91ac71882b07f91f0)
#### Friday 2023-01-27 09:27:17 by Wang Han

power: Introduce OnePlus 3 fingerprintd thaw hack

Taken from Oneplus 3, this hack will make fingerprintd recover from suspend quickly.

Small fixes for newer kernels since we're coming from 3.10.108..

Change-Id: I0166e82d51a07439d15b41dbc03d7e751bfa783b
Co-authored-by: Cyber Knight <cyberknight755@gmail.com>
[cyberknight777: forwardport and adapt to 4.14]
Signed-off-by: Shreyansh Lodha <slodha96@gmail.com>
Signed-off-by: Pierre2324 <pdbbasketball@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>
Signed-off-by: Dhruv <dhruvgera61@gmail.com>
Signed-off-by: Cyber Knight <cyberknight755@gmail.com>

---
## [Holoo-1/tgstation](https://github.com/Holoo-1/tgstation)@[10a344bde0...](https://github.com/Holoo-1/tgstation/commit/10a344bde0d48fb250dcb7a9eb4a1e98b9bb6df5)
#### Friday 2023-01-27 10:26:56 by Time-Green

External Organ Rework: new bodypart_overlay system (#72734)

Bodypart overlays are now drawn by the new /datum/bodypart_overlay
datum.

External organs no longer draw anything and instead add a special
/datum/bodypart_overlay/mutant to the bodypart, which draws everything

Makes it way easier to add custom overlays to limbs, since the whole
system is now modularized and external organs are just one
implementation of it

I haven't moved anything but external organs to this new system, I'll
move eyes, bodymarkings, hair, lipstick etc to this later

New pipeline is as follows:
- External organ added to limb
- External organ adds /datum/bodypart_overlay/mutant to limb to
bodypart_overlays
- Limb updates its icon, looks for all /datum/bodypart_overlay in
bodypart_overlays
- Very cool new overlay on your limb!

closes #71820

:cl:
refactor: External organs have been near-completely refactored. 
admin: Admin-spawned external organs will load with a random icon and
color
fix: fixes angel wings not working for non-humans (it was so fucking
broken)
fix: fixes external organs being invisible if they werent initialized
with a human
/:cl:

### Why this is good for the game
External organs are cool but are pretty limited in some ways. Making
stuff like synthetic organs is kinda fucked. I tried and it was dogshit.
Now you can just give an icon state and icon and you're good (using
/datum/bodypart_accessory/simple)

Stuff like eyes, cat ears and hair seem like good choices for extorgans,
but don't quite work for it because their icons work a lot differently.
This solves for it completely since any organ (or object or whatever)
can add it's own icon to a bodypart.

Want to add an iron plate to someones head? Go ahead. Want a heart to
stick out of someones chest? No problem.

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [Holoo-1/tgstation](https://github.com/Holoo-1/tgstation)@[36090c1b20...](https://github.com/Holoo-1/tgstation/commit/36090c1b206dee8b643e83607e333c29906b6bc8)
#### Friday 2023-01-27 10:26:56 by san7890

Refactors Suicide Verb + Basic Mobs (actually all (most) living mobs) Can Now Suicide (#72919)

## About The Pull Request

On the tin. There was a lot of needless copy-paste and a lot of
single-letter vars and weird indentation and... well just all of it was
at least eight years old. So, I decided to "abstract" as much as I could
of it out instead of piling onto the big copypaste clusterfuck for
implementing basic mob suicide.
## Why It's Good For The Game

Fixes #72903

Having more procs that can be easily repeatably called to the same
results is much better than having to transplant the same exact three
lines everywhere. It's also a good first step to further in-depth
behavior by allowing sub-type overrides of certain procs (which is quite
nice). Just feels more extensible overall for the next guy who wants to
add funny suicide behavior whenever they might come around.

There's probably a few better ways to do what I did, but I wrote code
comments explaining why I did what I did. I think there's a few ways to
make it more agnostic, but I think that'll be another can of worms that
will bloat out an already quite large PR. Let's just get the framework
set.

(this refactor should also make it quite easy to unit test suicide
actions :eyes:)
## Changelog
:cl:
fix: All Mobs (including Basic mobs) are now able to suicide. (warning:
some exclusions remain)
/:cl:

---
## [zeeb92/tgstation](https://github.com/zeeb92/tgstation)@[5e80257423...](https://github.com/zeeb92/tgstation/commit/5e802574231c9c6fe835c40b55f2c8aa9f1c68b4)
#### Friday 2023-01-27 10:46:53 by Jeremiah

Refactors crew records (#72725)

## About The Pull Request
I have attempted or otherwise started this project at least 4 times. I
am sick of it being on my calendar. The code needs it. I need it.

- This makes crew records a proper datum rather than assigning
properties record.fields.
- General, medical, and security records are merged.
- Did some slight refactoring here and there for things that looked
obvious.
- Wanted states are now defined (and you can suspect someone through
sechud)
- pAI (unrelated but annoying) had some poorly named exported types that
i made more specific
- Job icons are moved back to the JS side (I wanted to get icons for
initial rank without passing trim)

<details>
<summary>previews</summary>

Editable fields & security console

![CM6d74brnC](https://user-images.githubusercontent.com/42397676/213950290-af6cfd76-eb8b-48e9-b792-925949311d9a.gif)

Medical records

![bFJErsvOaN](https://user-images.githubusercontent.com/42397676/214132534-59af1f8c-9920-4b51-8b27-297103649962.gif)

Look and feel of the more current version

![cxGruQsJpP](https://user-images.githubusercontent.com/42397676/214132611-0134eef0-e74c-4fad-9cde-328ff7c06165.gif)

</details>

## Why It's Good For The Game
TGUI'd some of the worst UIs in the game.
Creating new records is made much simpler. 
Manifest_inject is made readable.
Probably bug fixes

## Changelog

:cl:
refactor: Crew records have been refactored.
refactor: Medical records -> TGUI
refactor: Security records -> TGUI
refactor: Warrants console -> TGUI
qol: Players are now alerted when their fines are paid off.
qol: Cleaned up sec hud examination text.
qol: Adding and deleting crimes is easier.
qol: Writing crimes in the console sets players to arrest.
qol: You can now mark someone as a suspect through sec hud.
/:cl:

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[9a05786af1...](https://github.com/mrakgr/The-Spiral-Language/commit/9a05786af11b605c74f438e6e4868cefef135cc2)
#### Friday 2023-01-27 11:48:01 by Marko Grdinić

"10:10am. I could have gotten up earlier, but I did not want to be in an ice cube of a room. Any mails?

Surprisingly no. I guess this takes a while. At any rate, I've done all that I can, and I have some free time at the moment. Let me chill. Then I will focus on making videos. Just a few days of this and I will increase my skill significantly.

10:15am. I see on AngelList there are a bunch of rejects. Anyway, I am going to give it a couple of days to see how these applications play out. Maybe till the end of next week. Maybe I'll just apply to those mid exp C# jobs, and that is it.

Since I am at it, let me apply to them now.

10:20am. Ugh, the jobs at these companies really make it tedious to apply. I applied to CME group, but it likely that place requires residence. I am not going to apply to corpos that require so many hoops anymore.

10:25am. Now they are asking me about my educational experience, but I can't put anything in there. The web control is broken.

10:30am. Forget this shit. It is a waste of time. I have to fill in a zillion forms just to apply instead of sending a resume for these places. It is obviously not meant for people like me, but for those in the States.

I should focus on startups rather than these big companies.

Let this be a lesson. If absolutely nothing is working, I'll stick to the plan of making videos while I move to freelancing.

This world is some kind of a nightmare for me. In a sane world having talent and putting in effort would work, but in here you have to a mind reader to be successful.

Let me chill for a while.

I had wasted my time applying here, because at these kinds of places my resume will just get filtered via keywords.

11am. Done chilling. I want to apply a bit more, this time on YCombinator. Remember than ML framework job a couple of weeks ago?

...No, I'll never find it in this journal.

11:10am. YCombinator is really good.

///

How to stand out when applying to startups
Tired of applying to jobs and never hearing back? Want to get smarter about your outreach so you can stand out as a candidate?

Join Y Combinator's Work at a Startup team for a candid conversation about how to stand out when applying to startups. Come with questions about your job search and, if you're brave, a copy of your resume!

///

Right now I am filling out my data and saw this offer. Is it remote.

> Recommended pre-read: https://bit.ly/yc-resumes-and-standing-out

> Cold outreach: Highlight 2-3 things you’d be excited to work on at the company — and why.

This is super annoying. It is basically inviting me to do a lot of work for a particular company only to get rejected.

> Note: You can only apply to 10 companies per week.

Oh this is interesting. So there is that kind of limitation.

It seems these places want to me to write a note to them.

Ok, since there is a limit of 10 companies per week why don't I make use of that. Once I go through this round I'll really be set as far as applications go. After that I'll be able to focus on making videos.

Expertise or strong interest in the following areas: high performance computing, code optimization, concurrent programming, security, encryption, and certificates. · Flexibility and dedication to making exceptional products.

Let me do a little thing. Since these guys want concurrent programming, can I add Lithe POC back to my resume?

///

* A proof of concept functional reactive library for UIs
- Link: https://github.com/mrakgr/Lithe-POC
- In 2015 I made a poker game using WPF, and the UI code was a huge mess. After studying concurrency in 2020 I realized how to abstract UIs and here show how it is possible to emulate the Elm pattern using just reactive extensions. A 100 LOC is all it takes.
- Tech used: F#, Rx, WPF, Avalonia, GTK

///

Let me add this to the resume.

11:25am. Now I am a bit confused. Where should I be putting my YCombinator resume?

11:30am. I replaced my LinkedIn resume with a link. Come to think of it, let me also replace the AngelList one.

> I have great skills in compiler engineering and concurrency, as well as ML library engineering. If a functional programmer like me interests you, I'd love to work for you.

Let me go with this.

https://www.workatastartup.com/jobs/59245

>  Reinforcement Learning Scientist at Mayan (W21)

This 45-50k. Never thought I'd see a job like this. This is a pretty good fit.

https://www.workatastartup.com/jobs/56267

Let me apply here. What I am really shocked is how good this site is at giving me interesting jobs to apply to. Just what am I doing at AngelList.

https://www.workatastartup.com/jobs/59225

I'll go over these all in turn. Writing messages is taking my time compared to AngelList, but whereas AngelList positions are random the stuff I am getting here is interestin.

11:55am. https://www.workatastartup.com/jobs/57729

///

You have blockchain experience
You have understanding of smart contracts
Have written 10,000+ loc on distributed systems

///

This one is crypto. I guess I'll avoid this one.

https://www.workatastartup.com/jobs/54431

Let me go for these lower paying jobs as well.

https://www.workatastartup.com/jobs/54431

///

● Very strong Python skills, with deep expertise in at least one of: PyTorch, TensorFlow, JAX
● Very strong skills in recursive programming. Check out the Ivy Container class
● A passion for Machine Learning research, and for our vision to unify the ML frameworks!

///

> I have strong skills in compiler engineering, ML, concurrency and functional programming. I've put in 3 years of full time work into my own functional PL Spiral, so I am very confident in my ability to handle complexity. You don't have to worry about me having trouble with recursion!

> Despite my strong programming skills, I am a hobbyist programmer looking to go pro, so if you want somebody with pro experience I'd also be willing to take an intership position just to learn how to work on a team and within a company. I am willing to work hard!

12:05pm. I've applied to Ivy, Enso, Mayan and Rescale.

12:10pm. Apart from Rescale, these aren't highly paid, so I have a decent chance of getting a callback. The thing about jobs is that I need only a single one to make my way.

https://www.workatastartup.com/jobs/57619

Let me also apply here.

> Over the next 10 years, we plan to create a powerful AI render pipeline that allows us to edit, create, and understand pixels to accomplish challenging tasks ranging from instructing an AI to make subtle changes to images, creating entire 3D environments, and understanding context of a scene in a video. We plan to start by accomplishing difficult tasks with images first.

> Note: We are only accepting candidates from the U.S. or Canada at this time

Oh whops. Nevermind.

12:20pm. I am looking at the other jobs...

Let me go through the entire list quickly. There are only 127 anyway.

https://www.workatastartup.com/jobs/56536

///

I have strong programming skills and experience in 3d programs such as Blender and Houdini. I also have experience of implementing ML algorithms as well as libraries. I made my own programming language just for that explicit purpose.

When it comes to generative AI, my knowledge is a bit out of date - back when I was starting out in ML I implemented sparse autoencoders, as well as a F# ML library for them from scratch as an exercise, but I would be capable of getting up to speed with diffusion models quickly. For the past couple of months, I've been using Stable Diffusion to illustrate my webnovel, so I am familiar with their use.

///

Let me go with this.

https://www.workatastartup.com/jobs/42388

This one is meh. I'll leave it for later.

https://www.workatastartup.com/jobs/55300

This one too.

Now I have enough. I've apply to everything that interests me.

12:35pm. This is good enough. I'll let this run and won't apply to any more places for a week. During this time I need to focus on making Youtube screencasts and sharpening my personal skills.

Let me do the chores here. Then I will get started for real. If I could get my skills up, I should be able to get job offers consistently. I need to overcome this obstacle of mine. A week should be just enough to improve my skills notably.

12:40pm. I need to get started. Let me do the chores here and have breakfast. After that I'll get started on the Paperspace series. I am going to split my casts in various short subjects and stitch them together. I'll slowly gain skills that way."

---
## [sloisel/pyptex](https://github.com/sloisel/pyptex)@[50e36cf989...](https://github.com/sloisel/pyptex/commit/50e36cf989b12d1d88f3ad6c561b9da59791c2b2)
#### Friday 2023-01-27 11:50:14 by Sébastien Loisel

Restore stack filtering that had been accidentally removed

When there is a Python exception, the stack trace is supposed to
be filtered so that internal pyptex stack frames are deleted.
I had accidentally suppressed that behavior in the previous
version.

There are some slight changes elsewhere that are related to my
trying to track down some sort of race condition or python bug
or even possibly an OS bug. PypTeX uses streamcapture to
capture the output of spawned processes and log them. This
machinery is now also used to annote LaTeX error messages
with line numbers in the intermediary .pyptex file, with the
corresponding line numbers in the source .tex file, for easy
cross-referencing.

I'm not sure exactly what happened, but apparently the slightly
increased workload in the streamcapture "writer", which detects
those LaTeX error messages, triggered some sort of race condition
or underlying python or OS bug. It's hard to debug this because,
by its nature, streamcapture redirects stdout and stderr, so
as soon as streamcapture errors out, you often don't have stdout
and stderr anymore, so pdb is not so useful. Instead, I used
webpdb, which at least allows me to debug my program a bit. The
second problem is that streamcapture is inherently threaded, so
you have to launch webpdb in the right thread or else you won't
be able to debug your problem.

Long story short, from the master thread, it looks like sometimes,
when you os.close() the write end of a pipe, it doesn't actually
close it. The problem with this is that the streamcapture thread
that reads from the pipe, never gets an EOF, so that thread becomes
a zombie, preventing the whole process from terminating. One
workaround would be to daemonize the slave thread(s) but that is
also wrong, because the slave threads need to empty whatever
data is pending from the pipe and write it to whatever log file,
before finishing up, and daemonization would prevent that.

The weird thing is that, supposedly, the underlying OS should
signal an error when the underlying C library close() function
fails, and errno should be said, and according to python documentation,
this should trigger an exception. I never saw any of this.
It's not immediately obvious how to read libc's errno directly
from Python (I guess maybe ctypes or something).

Reading on the internet people struggling with pipes in C,
many people do a complicated song and dance to try and close
these pipes correctly, and often I feel like that code is wrong.
I also read reports of underlying OS bugs with the closing of
those pipes.

Since that seemed like a wild goose chase for now, I implemented
a kludge in streamcapture. When a streamcapture is closed,
it sends a magic byte string through the pipe before closing it.
The receiving thread will strip that magic byte string and cleanup
and shut down. Seems to work for now.

commit-msg approval for sebastienloisel on 2023.01.27-11:49:31

---
## [Offroaders123/NBTify](https://github.com/Offroaders123/NBTify)@[264f28b3ce...](https://github.com/Offroaders123/NBTify/commit/264f28b3ceea18ba2f79cb56ae5904dfac3f5fe5)
#### Friday 2023-01-27 12:12:58 by Offroaders123

SNBT Indentation

Wow! Been working on this for a few hours now. Had it almost working a few times along the way, so I would restart with what I had learned to make it right to get even closer to having everything indented correctly.

This looks great! There's only a little more formatting I want to add to non-structure-based tags, so primitive-based arrays will still have a little bit of spacing, but not be multi-lined.

This is a super huge benefit to having my own object parser! I would have loved to have these kinds of checks for my JSON formatting in STE back in the day. The ability to format arrays differently, depending on what is in each array, is super awesome. I want the TypedArray tags to be single-lined, since they tend to be really long, the primitive item arrays to be singled lined (string arrays may be one I might make multi-line though), and the arrays which *hold* either ListTag, CompoundTag, or the TypedArray tags will be multi-lined. So the only one left to implement from those, which isn't already added to match those are the possible string arrays, and pretty but single lined, primitive arrays. I think I will keep the TypedArray tags flattened to not have any whitespace. I can look into seeing if it looks nice though :)

Listened to Blackwater Park for the second time tonight. I love it a ton! It was musically easy to comprehend this time around. Gonna listen to that some more this week, and also gonna go further into Mike Keneally's catalog. Listened to Incubus Science today, did not expect that! It sounded very Keneally-ish, completely different from their sound on later albums. It was sick! Glad I mentioned that right now to myself, now I'm gonna make it a plan to listen to it again tomorrow! And Blackwater Park :8

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[354910566f...](https://github.com/treckstar/yolo-octo-hipster/commit/354910566fa186c4656ec5892722b400979a3057)
#### Friday 2023-01-27 14:22:05 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [watsbron/FlexFriday2023](https://github.com/watsbron/FlexFriday2023)@[3ae6df4c0b...](https://github.com/watsbron/FlexFriday2023/commit/3ae6df4c0ba2812e727f704d8da25321f722b5fa)
#### Friday 2023-01-27 14:36:11 by DefNotALemon

gamemaker update don't mind

why are you here get out leave me alone I'm a creep I'm a weirdo I don't belong here wait no you don't belong here fucking creep what the hell are you doing here

---
## [clamor-s/u-boot](https://github.com/clamor-s/u-boot)@[2deeeb90d0...](https://github.com/clamor-s/u-boot/commit/2deeeb90d07afae511c821e7b40419e594b71759)
#### Friday 2023-01-27 15:11:02 by Marcel Ziswiler

tegra: lcd: video: integrate display driver for t30

On popular request make the display driver from T20 work on T30 as
well. Turned out to be quite straight forward. However a few notes
about some things encountered during porting: Of course the T30 device
tree was completely missing host1x as well as PWM support but it turns
out this can simply be copied from T20. The only trouble compiling the
Tegra video driver for T30 had to do with some hard-coded PWM pin
muxing for T20 which is quite ugly anyway. On T30 this gets handled by
a board specific complete pin muxing table. The older Chromium U-Boot
2011.06 which to my knowledge was the only prior attempt at enabling a
display driver for T30 for whatever reason got some clocking stuff
mixed up. Turns out at least for a single display controller T20 and
T30 can be clocked quite similar. Enjoy.

Tested-by: Andreas Westman Dorcsak <hedmoo@yahoo.com> # ASUS TF600T T30
Tested-by: Jonas Schwöbel <jonasschwoebel@yahoo.de> # Surface RT T30
Tested-by: Svyatoslav Ryhel <clamor95@gmail.com> # LG P895 T30
Signed-off-by: Marcel Ziswiler <marcel.ziswiler@toradex.com>
Signed-off-by: Svyatoslav Ryhel <clamor95@gmail.com>

---
## [RalphHightower/RalphHightower](https://github.com/RalphHightower/RalphHightower)@[7da2bacfb9...](https://github.com/RalphHightower/RalphHightower/commit/7da2bacfb9f8541233537cd1d566c5bbdc6a9cb8)
#### Friday 2023-01-27 16:41:32 by Ralph Hightower

docs: 2023-01-25 FITSNews update (closes #604)

| **January 25, 2023** |
| [‘Murdaugh Murders’ Saga: Alex Murdaugh’s Clothes From Night Of Murder Are Missing](https://www.fitsnews.com/2023/01/25/murdaugh-murders-saga-alex-murdaughs-clothes-from-night-of-murder-are-missing/) |
More missing evidence?
|Accused killer Alex Murdaugh made multiple wardrobe changes on the evening of June 7, 2021 – the night prosecutors say he savagely murdered his wife and younger son on his family’s Lowcountry, South Carolina hunting property.<br>Why does this matter? Because the clothes he removed in at least one of these wardrobe changes have reportedly vanished without a trace, sources say … not unlike the weapons Murdaugh allegedly used to kill his wife, 52-year-old Maggie Murdaugh, and youngest son, 22-year-old Paul Murdaugh on the family’s 1,700-acre hunting property in Colleton County on June 7, 2021.<br>News of at least one of Murdaugh’s wardrobe changes on the night of the murders was reported Wednesday afternoon by Columbia, S.C. criminal defense attorney Lori Murray – whose TikTok page has been a big hit among those tracking the ‘Murdaugh Murders‘ crime and corruption saga.<br>Murray specifically discussed clothes Murdaugh was wearing in a Snapchat video sent from Paul Murdaugh at 7:56 p.m. EDT on the night of the murders.<br>*“I think I finally know what was on the Snapchat video Paul (Murdaugh) sent to his friends at 7:56 p.m. on the night he was killed,”* Murray said in her clip. *“Alex Murdaugh can be seen on that video wearing long pants and a dress shirt – not the clothes he was seen wearing when police arrived after he called 9-1-1.”*<br>*“He changed clothes a lot that day,”* one source familiar with the status of the case told me.<br>Lead prosecutor Creighton Waters did not reference them during his opening arguments on Wednesday afternoon – in which he laid out several new details of the case agains Murdaugh.<br>Curiously, the 7:56 p.m. EDT Snapchat video was referenced by lead defense attorney Dick Harpootlian in his opening statement – as purported evidence of the closeness between Alex Murdaugh and his son, whom he referred to as *“the apple of his (father’s) eye.”*<br>Harpootlian also seemed to invite scrutiny of the wardrobe changes during his opening argument when he asked jurors about the lack of physical evidence in the case.<br>*“Where are the bloody clothes?”* Harpootlian asked jurors.<br>That’s a very good question … but the fact we are having to ask it at all could wind up backfiring on Murdaugh’s attorneys in a big way if the clothes Murdaugh was wearing on the night of the murders have truly vanished.|

---
## [gadget-inc/mobx-quick-tree](https://github.com/gadget-inc/mobx-quick-tree)@[703989dac0...](https://github.com/gadget-inc/mobx-quick-tree/commit/703989dac0818c8973dcbb2d6b35ef160a89f297)
#### Friday 2023-01-27 17:04:32 by Harry Brundage

Add class models, a faster API for readonly instances

This introduces a new API for defining models that allows us to construct the read only instances much faster. Without any optimization yet, our primitive benchmark shows a 2.5x speedup for this new API over the existing readonly API:

```
claw ~/C/mobx-quick-tree (class-models) ➜  yarn x spec/bench/cross-framework.ts
yarn run v1.22.10
$ ts-node --transpile-only spec/bench/cross-framework.ts
mobx-state-tree x 4,618 ops/sec ±12.62% (80 runs sampled)
mobx-quick-tree types.model x 98,964 ops/sec ±3.50% (91 runs sampled)
mobx-quick-tree ClassModel x 261,246 ops/sec ±0.22% (92 runs sampled)
Fastest is mobx-quick-tree ClassModel
Slowest is mobx-state-tree
```

The central premise is that `mobx-state-tree`'s API for defining models collects functions that add views and actions in such a way that each view-adder function or action-adder function has to be run once *per* instance. If you have a model like:

```typescript
const Todo = types.model("Todo", {
  name: types.string,
  done: types.boolean
}).actions(self => {
  setDone(done: boolean) {
    self.done = done;
  }
});
```

each time you instantiate a `Todo` with `Todo.create` or `Todo.createReadOnly`, that `self => ({ setDone() {} })` block has to run once to create a new set of actions which close over a new value of self. There's no magic behind the scenes that only runs that function once and re-uses the output between instances -- it's instead re-executed on instantiation every time. NIce API, terrible for performance.

Instead, we should leverage JavaScripts existing mechanisms for defining what is the same about a bunch of objects once instead of over and over: the prototype chain! Classes (which in JS are just sugar over prototypes) allow us to define something like the `setDone` function once on a prototype, and then create an instance which has that as it's prototype, and not need to re-create `setDone` per instance. This whole PR is about defining a class-based API that leverages this built-in performant approach in JS to power read only instances, while still allowing us to generate the observable instances we need sometimes. It's an inversion from the previous approach to MQT: before, we adapted the MST API to give us readonly instances while conforming to the existing API, but now, we define a new API with a higher performance ceiling, and adapt that API to the slower thing under the hood.

The implementation of this is scary to be honest. `types.model` was clearly modelled after classes, so the grain of class definitions and MST type defintions match, but getting it to work at runtime and typetime requires lots of fancy stuff. The first tricky part is the types. I think it's key that a new, class based API for MQT is incrementally adoptable so that we can roll it out over time and build confidence, and that means that the existing `types.model` types and MQT class based types need to interoperate. After much fiddling, I think I accomplished this, but it was hard to get `IType` and `IClassModelType` working in harmony. See the note in `IClassModelType` for more info.

Also tricky is the runtime derivation of the observable class from the readonly class. The decorators give us enough structure to hang off of, but ES2020/TS decorators have two key limitations: they can't muck with properties until they are defined, and TS decorators can't change the type. This matters most for volatiles and async actions.

Let's review the requirements:

 - Async actions in MST and plain old mobx are really several chunks of sync action chained together, which some kind of hook system to ensure that each sync bit is wrapped in mobx action wrapper goodness, and that inbetween while awaiting something, the wrapper isn't active. mobx/MST need this hook point to enforce actions are actually the only ones changing data.
 - We want to define async actions on classes

And then the limitations:

 - The only hook system that the mobx or MST folks have come up with that is ergonomic is having userland code build async actions using generators instead of the normal async/await. This is so they have their hook point for every `yield`, where they can be like "oh, a promise!" and disable the action bits for the duration of the promise, and re-active them when it resolves and they pass the value back in to the caller. Generators allow userland to intercept each call to what would be `await` in both node and the browser.
 - *Inside* the async action you use `yield somePromise`, but calling the action still returns a promise, so you still do `await someNode.someAsyncAction()`. This is to stay as normal as possible outside of MST action bodies and not make the whole system use generators. So, to adapt the generator into a normally typed async function, users need to wrap their generator functions in `flow()`.
 - There's no way to automatically adapt an async function into a generator function for MST. If there was, MST would use it already and not require folks to write generators. This means the code on the MQT class model *has* to be in generator form.
 - TypeScript decorators can't change the type of the property they are decorating, so they can't automatically apply the `flow` expression to a prototype level generator function and get the type turned into a nice promise returning type. If you have a class body like this:

```typescript

class Foo {

  @flow
  *someAsyncAction() {
  }
```

the return type of that function is locked in as a generator, and `@flow` can't change it. It can do stuff to it at *runtime*, but it can't mutate the type time type. That means that `await someFoo.someAsyncAction()` won't typecheck, as TypeScript will be expecting it to return a generator regardless of what runtime trickery the decorator gets up to. Sad.

So, we need to do the adaptation of the generator function into a promise-returning function for nice caller types with some sort of expression. That's what the `flow()` helper from MST does.

 - To assign a `flow(function * () {})` expression to a property on a class, it becomes an "instance property" instead of a prototype property. That is:

```typescript
class Foo {

  someAsyncAction = flow(function * () {
    yield sleep(100)
  });

}
```

desugars into:

```javascript
class Foo {

  constructor() {
    this.someAsyncAction = flow(function * () {
      yield sleep(100)
    });
  }

}
```

It'd be far more performant in general to have this somehow do a `Foo.prototype.whatever = flow(...)`, but alas, thats not how ES6 expression assignments work. This is a major issue for us though, because this desugaring means that there is nothing to look at to get the flow definition at class definition time. For things defined on the prototype, we can get a handle on them easily at class definition time to send them into mobx land for making the observable instance, but, for these things which aren't set until the constructor, we can't see their value until the constructor runs! After much brain wracking I couldn't find a away around this -- I had to go with a major hack which is to actually construct an instance, let the constructor run, and then pull the resulting expression off of the constructed instance to get a handle on the flow implementation to pass into MST. Yikes.

---
## [azhar-ikhtiarudin/uav-rl-paper](https://github.com/azhar-ikhtiarudin/uav-rl-paper)@[3ff8b9a7ff...](https://github.com/azhar-ikhtiarudin/uav-rl-paper/commit/3ff8b9a7ffbfee1a3fbe5a43a3be7f93fa636484)
#### Friday 2023-01-27 17:06:56 by Raisal P

+fixed lotsa shits
+added Runs automation
+I hate my life

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[406b6870bd...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/406b6870bd28dd78e65e59787d8c54c776078019)
#### Friday 2023-01-27 17:15:20 by SkyratBot

[MIRROR] adds atmospheric gloves, small resprite of firefighter gear, repaths stupid glove paths [MDB IGNORE] (#18785)

* adds atmospheric gloves, small resprite of firefighter gear, repaths stupid glove paths (#72736)

repaths a lot of gloves off /color because they were incredibly stupid
firefighter gear has gotten an update (it doesnt cover hands anymore
though, you need something else)
firefighter helmets no longer hide your mask or glasses

![image](https://user-images.githubusercontent.com/23585223/212542599-c004d0e4-c141-40b4-a1bb-c838f9893c4b.png)
fixed engine goggles starting with darkness vision
to the atmos lockers adds atmospheric gloves, a pair of thick (chunky
fingers) gloves that are fireproof and fire protective, slightly shock
resistant and let you fireman carry people faster.
atmospheric firefighter helmets now are a subtype of welding hardhats,
you can enable a welding visor.
welding hardhats change mode with right click instead of altclick

im not a good spriter but i think this resprite makes them fit nicer
with other engi equipment
lets me firefighter rp

:cl:
add: Atmospheric Gloves, thick gloves that are fully fireproof and fire
protective and let you fireman carry people faster.
fix: fixes engine goggles starting with darkness vision
qol: firefighter helmets can now enable a welding visor
qol: welding hardhats change mode with right click instead of altclick
balance: firesuits no longer protect your hands
/:cl:

* Makes shit compile

* Updates the digi and snouted stuff to match the new sprites (thanks Halcyon!)

* Fixes a whole ton more issues that popped up

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>
Co-authored-by: GoldenAlpharex <jerego1234@hotmail.com>

---
## [RalphHightower/RalphHightower](https://github.com/RalphHightower/RalphHightower)@[6d0a1f3d94...](https://github.com/RalphHightower/RalphHightower/commit/6d0a1f3d946654ed2c963270e1e9e9e5ff446e4c)
#### Friday 2023-01-27 17:22:04 by Ralph Hightower

docs: 2023-01-25 P&C update (closes #6xx)

| [Alex Murdaugh trial begins with explosive opening statements, support from relatives](https://www.postandcourier.com/murdaugh-updates/alex-murdaugh-trial-begins-with-explosive-opening-statements-support-from-relatives/article_5b67bd1c-9cc8-11ed-8eeb-7f00639e747d.html)<br>*“You’re going to see what he did to Maggie and Paul,”* Waters said. *“It’s going to be gruesome. There’s no other way around it.”<br>The Columbia trial attorney and state senator countered that his client was a loving husband and father who was incapable of inflicting the shotgun blasts that killed Paul, the 22-year-old “apple of his eye,” or the rifle shots that took down Maggie, 52.<br>Harpootlian described the scene in great and gory detail. Shot at close range, Paul’s head exploded *“like a watermelon,”* he said, describing that brain matter was sprayed all over the walls and floor of the feed room he was standing in by the property’s dog kennels. Only the front of his face was left intact, Harpootlian said.<br>Maggie was shot next as she ran away from the scene, Harpootlian said. She had fallen and was lying prone when the killer fired the fatal shot into the back of her head, the defense attorney said.<br>Harpootlian repeatedly used words like “butchered,” “slaughtered” and “executed” to describe the slayings, contrasting the horrific violence against what he described as a lack of evidence of discord in the family.<br>*“He didn’t kill — butcher — his son and wife,”* Harpootlian said.<br> Yet state investigators spent some 13 months trying to prove it, rather than pursue an objective investigation to find the real killer, Harpootlian said.<br>*“They decided that night: He did it,”* Harpootlian said. *“They’ve been pounding that square peg in that round hole.”*<br>In a twist, Murdaugh’s surviving son, Buster; brothers Randy and John Marvin; sister Lynn Murdaugh Goette; and sister-in-law Liz Murdaugh appeared in court. They declined to speak with reporters outside the courthouse. But they sat in the second row behind the defendant and at times spoke with him as he turned around in his chair to face them.<br>Murdaugh’s relatives had skipped Alex Murdaugh’s prior court appearances, hoping to avoid the publicity that would surely follow.<br>Murdaugh’s lawyers have named each of them as potential witnesses in the trial. It is unclear what they might say. But their testimony would come later in the trial, if at all. |

---
## [zz912/linuxcnc](https://github.com/zz912/linuxcnc)@[cede6a0a5c...](https://github.com/zz912/linuxcnc/commit/cede6a0a5c0235309fb2875c8b3c7b6fa56fa937)
#### Friday 2023-01-27 19:13:53 by zz912

Adding function for carousel HAL component

Hello,

I tried use component carousel for encoder without trigger signal:
https://forum.linuxcnc.org/24-hal-components/47845-carousel-dont-work-w-o-trigger
It did not work. 

So we have a problem when moving from position 9 to 8 and from position 3 to 2.
Why is this so:
9 = 2^3+0+0+2^0
8 = 2^3+0+0+0

3 = 0+0+2^1+2^0
2 = 0+0+2^1+0

When I want the revolver, let it turn from position 9 to 8 or from position 3 to 2. Then the engine starts and immediately stops. A situation occurs when, due to manufacturing tolerances, bit ^0 (2^0=1) turns on one millisecond before the rest of the bit, and the program thinks it is already in the position where it should be (but physically it is not) and turns off the rotation relay.

I solved it. I made a modification to the carousel component. The original solution worked in such a way that moving from the first position to the second position was only about checking whether it is already in the correct position. I have several phases. 

The first phase (case 0 and case 1) is the same as it was. ATC is started and the direction of rotation is evaluated.

The second phase (case 102) to leave the first position. I check if the position is already 0 and I don't care how the read position changes. 

In the third phase (case 103), I just check that the position is zero. 

In the fourth phase (case 104), I check that the position has changed to anything else and i make decision, how to continue.
Than I am waiting user defined short time (several miliseconds). Than I read code position. 
If position is not correct I continue move. If position is correct I continue to next phase. 

In the fifth phase (case 105) I waiting user defined time. It is long time for stabilize mechanical oscilation of toolchanger. Than I check if the position is correct, than I make decision, how to continue.
If position is not correct I repeat cycle . If position is correct I continue to next phase.

I needed to make sure that the ATC motor still wouldn't spin when the encoder failed. The Brother TC-211 uses a motor that is not designed for continuous operation. That's why I made the "error_time" parameter. If the ATC cycle length is longer than this parameter, the ATC motor will shut down and the program will hang. The default value of this parameter is 3600s = 1 hour. I don't expect anyone to have a longer cycle ATC. I have this value set to 20 seconds myself.

I would like to ask for help.
1) I would need someone to test these changes on an ATC without an encoder with only indexing. I don't have such an ATC myself, so I can't verify if my changes messed something up.
2) I'm just an amateur programmer, so I need comments about the C language so I don't break any conventions.
3) I need advice on what else to do in the LinuxuCNC project so as not to break the rules. I guess I'll have to edit the manual? And what else?

---
## [RalphHightower/RalphHightower](https://github.com/RalphHightower/RalphHightower)@[09561a9330...](https://github.com/RalphHightower/RalphHightower/commit/09561a93301cb7c1f011951ed35493bd472228af)
#### Friday 2023-01-27 19:19:13 by Ralph Hightower

Interim check-in 

| **January 26, 2023** |
[‘Murdaugh Murders’ Saga: Prosecution Carries First Day Of Testimony](https://www.fitsnews.com/2023/01/26/murdaugh-murders-saga-prosecution-carries-first-day-of-testimony/)<br>
Another strong performance from prosecutor Creighton Waters as the state begins laying out its case …<br>
South Carolina’s ‘Trial of the Century’ – the double homicide case against accused killer Alex Murdaugh – was supposed to be a legal mismatch. And through its first day of witness testimony, it has been.

The surprise? The mismatch we have seen isn’t the one everyone was expecting …

Heading into this trial, the general consensus was that lead prosecutor Creighton Waters would be unlikely to match wits against Murdaugh’s lead defense attorney Dick Harpootlian. Sure, Waters had demonstrated the ability to do so in multiple pre-trail hearings, but could he sustain it over the course of a multi-week trial? One in which the burden of proof – a.k.a. the pressure – was squarely on him and his team of prosecutors?

Also, the defense entered these proceedings with significant momentum … poking what appeared to be major holes in the state’s case.

As the first day of testimony drew to a close, though, Waters has proven himself more than equal to the task … while Harpootlian has stumbled badly out of the gate. As a result, the murder case against Murdaugh is looking far better than it did forty-eight hours ago.


Alex Murdaugh’s defense attorney Dick Harpootlian in court on January 25, 2023 (Grace Beahm Alford/ Pool)
After delivering a thunderously effective opening statement yesterday, Waters pressed his advantage on the first day of testimony – introducing key initial evidence and eliciting compelling testimony from several first responders who arrived and discovered the initial carnage at the scene of this crime.

To recap: At approximately 8:49 p.m. EDT on June 7, 2021, state prosecutors say Murdaugh savagely dispatched his wife, 52-year-old Maggie Murdaugh, and their younger son, 22-year-old Paul Murdaugh, near the dog kennels on the family’s 1,700-acre hunting property – known locally as Moselle.

Paul Murdaugh was hit by a pair of shotgun blasts on that fateful evening – one to the head, the other to the arm and chest. Maggie Murdaugh was killed by multiple rounds from a semi-automatic rifle around the same time her son was killed. At least two of Maggie Murdaugh’s gunshot wounds were inflicted as she was lying wounded on the ground – consistent with initial reports we received of “execution-style” slayings.

Maggie Murdaugh’s body was found approximately thirty yards from the dog kennels where her son was murdered. Also found at the crime scene? Five spent .300 blackout cartridges and other ballistics evidence.

This evidence has become increasingly important to prosecutors in light of pre-trial problems that arose with regard to one of its blood spatter experts.
On Thursday, jurors saw body-worn camera footage from responding deputies along with crime scene photos from these shootings – and judging from the looks on their faces, what they saw was every bit as horrific as what was described to us in the weeks leading up to trial.

*“The majority of the head is gone,”* said Colleton County sheriff’s office captain Jason Chapman.

*“There is substantial damage to his head … and what appears to be his brain down around his ankles,”* noted Barry McCoy of Colleton County fire and rescue during his testimony.

As jurors absorbed all of this information, Waters also began laying the groundwork for several narratives key to the prosecution’s case – 1) That Murdaugh immediately sought to cast blame for the murders elsewhere and 2) That he immediately began laying the groundwork for a concocted alibi.

In his first comments to Colleton County sergeant Daniel Greene – the first law enforcement officer to arrive on the scene – Murdaugh said that his son was the victim of vigilante justice.

*“This is a long story my son was in a boat crash,”* Murdaugh told Greene. *“I know that’s what (this) is.”*

Murdaugh offered this same unsolicited theory in the full, unredacted 9-1-1 call that was played in court for the first time.

Murdaugh also encouraged Greene to check his cell phone to verify his recent movements.
Readers will recall Murdaugh’s attorneys boasted of him having an “ironclad alibi” for the night of these killings.

They will also recall how that alibi was shredded by the retrieval of a cell phone video taken by his son, Paul, just three minutes before he was killed. That clip placed Alex Murdaugh at the scene of the murders just moments before they took place.

The cell phone video also revealed Murdaugh lied to investigators about his whereabouts on the night of the murders.

Prosecutors have yet to introduce this video into evidence, but Waters did reference it in his opening arguments.
While Waters and his deputies – including Savanna Goude and David Fernandez – began laying the foundation for their case, Harpootlian also attempted to begin injecting his own narratives into the mix.

The veteran attorney – who has five decades of courtroom experience – is clearly hoping that allegations of contaminated evidence, shoddy police work and a so-called “rush to judgment” on the part of prosecutors will begin creating reasonable doubt in the minds of jurors.

*“You are taught to keep the crime scene pristine,”* Harpootlian told Greene during his testimony. *“What I’m getting at is one of the cardinal rules of a crime scene is to keep it pristine.”*

According to Harpootlian, responding officers failed to do so by walking in and around the immediate vicinity of the bodies after determining the two victims had expired – and by placing sheets over their bodies prior to crime scene technicians arriving to inspect them.

Harpootlian also chided Colleton County corporal Chad McDowell – the second officer who arrived on the scene – for marking evidence without being asked to do so.

*“Were y’all trying to solve the crime?”* he asked McDowell. *“What were y’all doing?”*

In addition to these narratives, Harpootlian is eager to advance the same “boat crash vigilante” theory his client tried to sell law enforcement on from the beginning.

If he is to be successful, he is going to have to improve on his performance in front of this jury.

Harpootlian struggled to build a rhythm all day – encountering technical difficulties with courtroom audio-visual equipment, objections from Waters and his own apparent lack of organization.

Jurors seemed miffed by Harpootlian from the beginning, and by the time he finally began scoring a few points late in the afternoon – many looked as though they had already formed a negative opinion of him.

Should Harpootlian be counted out? Absolutely not … as I noted frequently on social media posts throughout the day, I fully expect him to find his rhythm as proceedings progress. |
| [Alex Murdaugh prosecutors launch case with unredacted 911 tapes, body camera footage](https://www.postandcourier.com/murdaugh-updates/alex-murdaugh-prosecutors-launch-case-with-unredacted-911-tapes-body-camera-footage/article_3818e9d2-9d84-11ed-a44d-afa132da63de.html)
WALTERBORO — Alex Murdaugh was dry-eyed when officers arrived at his Colleton County hunting property the night his wife and son were shot to death, first responders testified Jan. 26 in his double-murder trial.

Murdaugh also didn’t appear to be covered in blood, though he told dispatchers he had touched Maggie and Paul Murdaugh’s bodies while checking for signs of life, those officers said.

Within minutes of dialing 911 to report the slayings, Murdaugh had developed a theory of why someone would brutally kill two of his closest relatives: retaliation for the fatal 2019 boat crash that first brought scrutiny to his prominent Lowcountry family.
In separate conversations shortly after reporting the slayings on June 7, 2021, the prominent Hampton attorney shared that theory with both an emergency dispatcher and the first officer on scene at the Murdaughs’ estate, audio and body camera recordings showed.

*“This is a long story,”* Murdaugh whimpered to the officer in a high-pitched voice. *“My son was in a boat wreck months back. He’s been getting threats. Most of it has been benign stuff we didn’t take serious. … I know that’s what it is.”*
*“My son has been threatened for months and months and months,”* Murdaugh told the dispatcher minutes earlier. *“He’s been hit several times.”*

Almost immediately after he told the deputy about the threats, Murdaugh offered to show the deputy his phone to prove he had just gotten home from his parents’ house.

State prosecutors believe the exchanges help prove their theory that the slayings of Maggie and Paul Murdaugh were an elaborate ruse Murdaugh concocted to portray himself as the victim of an “unspeakable tragedy” and cover up his decade-long financial crime spree.

Paul Murdaugh had been criminally charged with driving a family boat while intoxicated in 2019, when it crashed into a Beaufort County bridge piling. Mallory Beach, 19, died. State investigators quickly excluded Beach’s parents and the other boat crash survivors as suspects in the Murdaugh murders.
Tapes of Murdaugh’s conversations shortly after the slayings were among a series of records the S.C. Attorney General’s Office revealed for the first time Jan. 26 in their quest to convict Murdaugh on charges of murdering his wife and son.

In the dark
Throughout hours of testimony, the public was not allowed to see the new footage. At times, this made the proceedings difficult to follow.

Prosecutors and defense attorneys repeatedly asked witnesses questions about videos and photos presented to them, images that neither the courtroom audience nor the wider viewing public could see.

Prosecutors taped paper over one monitor that faced the audience, and Murdaugh’s defense propped the lid of a cardboard box another. Sometimes they did so even when they showed images that were not submitted under seal.

The jury watched on screens angled away from public seating. The Colleton County courthouse does not have monitors set up for public viewing.
In an order signed by Judge Clifton Newman Jan. 25, both sides agreed that graphic images from the crime scene and autopsies should be kept under seal. The deputies’ body camera footage was said to show their bodies.

Yet extensive portions of the videos appeared to be recorded away from the bodies, where officers said it showed new details that could prove key to the case.

For instance, deputies described how the camera footage showed multiple sets of unidentified tire tracks near the buildings where Maggie and Paul were shot. It showed Murdaugh’s behavior in the minutes after deputies arrived. And it showed the clothing he was wearing, which did not bear visible signs of blood.

Scene of the crime
Prosecutors began presenting their case Jan. 26 by calling six witnesses to testify about the night of the slayings. Two were dispatchers who took Murdaugh’s 911 call that evening.

The county fire chief and three deputies with the Colleton County Sheriff’s Office testified about responding to the family’s 1,770-acre hunting estate, which they called Moselle. They found the bodies of Maggie Murdaugh, 52, and her 22-year-old son near dog kennels on the property. <br>pResponders at the scene testified Murdaugh appeared distraught and nervous, though he wasn’t crying. Some said they didn’t view that as suspicious, as people process shock and grief differently.<br>On Sgt. Daniel Greene’s body camera video, Murdaugh could be heard repeatedly asking if deputies had checked Maggie and Paul’s bodies and if they were really dead. At one point, he asked if their deaths were *“official.”*<br>Greene and others testified it was obvious they were dead. A shotgun blast had blown Paul’s head apart, and his brain lay by his feet. Maggie had a hole in her head as well from a close-range, execution-style rifle shot. Both were lying facedown in large pools of blood and other matter, officers testified.<br>Paul’s injuries were *“incompatible with life,”* Colleton County Fire-Rescue Chief Barry McRoy said, explaining why he didn’t bother checking their pulses. He said Maggie’s wounds were *“not sustainable.”*<br>Murdaugh, 54, appeared emotional throughout the day. He rocked back and forth in his courtroom chair as witnesses recounted the grisly details of his wife and son’s deaths. Murdaugh’s face flushed red as tears flowed freely down his cheeks.<br>Murdaugh defense attorney Dick Harpootlian seemed focused on establishing that first responders made critical blunders while securing the crime scene and establishing evidence.<brìIn cross-examination, he repeatedly asked sheriff’s deputies why they walked about the scene that night, marking shell casings and at one point stepping into the feed room where Paul was shot.<br>Any bloody footprints found at the scene could have been left by the deputies, rather than the killer, Harpootlian asserted.<br>*“You do your best not to contaminate the crime scene,”* Greene told him at one point.<br>*“And this is your best?”* Harpootlian asked. *“To walk in an area where there is blood and brain matter?”*<br>He noted that deputies observed multiple sets of tire impressions in the wet grass around the crime scene, but they didn’t take photos to document them and weren’t able to prevent other responders and even civilians from driving onto the scene and mooting that potential evidence.<br>*“Whatever tire tracks were left were obliterated by your men, is that correct?”* Harpootlian asked Greene.<b4>*“That’s possible,”* the deputy responded.<br>State prosecutors countered by noting how much care first responders took to secure the scene and avoid damaging evidence. The deputies noted that at first, they had no clue whether they were walking into an active shooter situation, a murder-suicide or something else entirely.<br>*“At the time, we didn’t know what we had,”* testified Jason Chapman, a captain with the sheriff’s office.<br>Harpootlian defended his client’s behavior that evening, saying he was overcome with grief and concerned about his wife and son’s well-being.<br>He also noted that while Murdaugh didn’t appear to be covered in blood, there was blood on his shorts. Harpootlian objected when prosecutors seemed to imply that the lack of blood on Murdaugh indicated he hadn’t checked on Maggie and Paul’s pulses.<br>One piece of evidence that came through despite the restrictions on exhibits was Murdaugh’s 911 call. Jurors heard new audio that had been redacted in versions released to the media after the slayings<br>In one of the never-before-heard exchanges, Murdaugh told the dispatcher he was going up to the Moselle house to retrieve a shotgun for his own protection, not knowing whether the killer was still on the grounds<br>In another, the dispatcher asked Murdaugh if his relatives shot themselves.<br>
*“Oh no!”* Murdaugh cried. *“Hell no!”*|

---
## [SMERTONOS/tgstation](https://github.com/SMERTONOS/tgstation)@[bf73344399...](https://github.com/SMERTONOS/tgstation/commit/bf73344399f4b372c13d367cbbd8a40bec23916b)
#### Friday 2023-01-27 19:41:37 by Time-Green

[READY] DRAMATIC SHUTTLES!! You can now fly around the shuttle (#71906)

You can move around shuttles during transport now! Instead of them
teleporting you instantly into deepspace, you can move around somewhat
depending on your space-mobility and grip-strength.


![image](https://user-images.githubusercontent.com/7501474/206866132-3fae024c-a8a2-4f4a-b4b8-37c96a254498.png)

**Please watch the demonstration aswell, it should answer most
questions:**
https://www.youtube.com/watch?v=Os77qDOVSXE

Interactions:
- Being within armsreach of a wall or solid object means you 'cling',
where the shuttle pull is very weak and you can basically run around the
shutt;e (but dont fuck up or you're gone)
- Being in range of nothing gives you a very heavy pull, you can barely
resist if you have a decent jetpack
- Objects are instantly power-yeeted
- Being pulled or riding something excempts you from hyperspace pull
- Touching a space tile while being on hyperspace dumps you in
deepspace, you either go back to the shuttle or enjoy deepspace
- On shuttle hyperspace tiles are a lot less dangerous, and will instead
launch and freeze you instead of teleporting you into deepspace
- In-case it wasn't obvious, you can rest outside the shuttle as long as
something is blocking your path. I think it's funny but I might nerf it

:cl:
add: You can now fly around the shuttle during transit! Woohoo! You can
either cling to the side or grab a jetpack and try and keep up with the
shuttle! Carps can move around freely in hyperspace
qol: Increased shuttle hyperspace size from 8 tiles to 16
/:cl:

- [x] Find a way to detect when a shuttle arrives and do something with
the shit left in hyperspace

Things I will do in another PR: 
- Engines spit fire and hurt (almost finished but I want to keep this
small)
- Random shuttle events. You might run into dust meteors or migrating
carps OR A CHANGELING INFILTRATOR
- Hyperspace turfs on the shuttle pull you under the shuttle

### Why it's good for the game
It's so much more immersive than being instantly teleported into
deepspace. It gives you a chance to recover if you get spaced or for
daredevils to look cool

It's also just very cool idk

---
## [SMERTONOS/tgstation](https://github.com/SMERTONOS/tgstation)@[acb96fee1d...](https://github.com/SMERTONOS/tgstation/commit/acb96fee1d0f6605992280d751a7b9930e3a7211)
#### Friday 2023-01-27 19:41:37 by MrMelbert

Refactors memories to be less painful to add and apply, moves memory detail / text to memory subtypes. Adds some new memories to demonstrate.  (#72110)

## About The Pull Request

So, a huge issue with memories and - what I personally believe is the
reason why not many have been added since their inception is - they're
very annoying to add!

Normally, adding subtypes of stuff like traumas or hallucinations are as
easy as doing just that, adding a subtype.

But memories used this factory argument passing method combined with
holding all their strings in a JSON file which made it just frustrating
to add, debug, or just mess with.

It also made it much harder to organize new memories keep it clean for
stuff like downstreams.

So I refactored it. Memories are now handled on a subtype by subtype
basis, instead of all memories being a `/datum/memory`.

Any variety of arguments can be passed into memories like addcomponent
(KWARGS) so each subtype can have their own `new` parameters.

This makes it much much easier to add a new memory. All you need to do
is make your subtype and add it somewhere. Don't need to mess with jsons
or defines or anything.

To demonstrate this, I added a few memories. Some existing memories had
their story values tweak to compensate.

## Why It's Good For The Game

Makes it way simpler to add new memories. Maybe we'll get some more fun
ones now?

## Changelog

:cl: Melbert
add: Roundstart captains will now memorize the code to the spare ID
safe.
add: Traitors will now memorize the location and code to their uplink.
add: Heads of staff winning a revolution will now get a memory of their
success.
add: Heads of staff and head revolutionaries who lose their respective
sides of the revolution also get a memory of their failure.
add: Completing a ritual of knowledge as a heretic grants you a quality
memory.
add: Successfully defusing a bomb now grants you a cool memory. Failing
it will also grant you a memory, though you will likely not be alive to
see it.
add: Planting bombs now increase their memory quality depending on how
cool the bomb is.
refactor: Memories have been refactored to be much easier to add.
/:cl:

---
## [Neebe3289/kernel_xiaomi_mt6785](https://github.com/Neebe3289/kernel_xiaomi_mt6785)@[2eb095b1ec...](https://github.com/Neebe3289/kernel_xiaomi_mt6785/commit/2eb095b1ecc1f911dbe59cdca1c575c1446b0be7)
#### Friday 2023-01-27 20:05:38 by Peter Zijlstra

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
Signed-off-by: Neebe3289 <neebexd@gmail.com>

---
## [IndieanaJones/tgstation](https://github.com/IndieanaJones/tgstation)@[b174af7661...](https://github.com/IndieanaJones/tgstation/commit/b174af7661cbfaf564292caabfccca18619bda23)
#### Friday 2023-01-27 20:25:36 by Jacquerel

Basic Mob Carp Part VIII: Basic Mob Carp (#72073)

## About The Pull Request

Wow we're finally here. This turns carp into Basic Mobs instead of
Simple Animals.
They use a variety of behaviours added in previous PRs to act in a
marginally more interesting way than they used to.
But don't worry there's still 2 or 3 PRs to follow this one until I'm
done with space fish.

Changes in this PR:
Carp will try to run away if they get below 50% health, to make use of
their "regenerate if not attacked" component.
Magicarp have different targetting behaviour for spells depending on
their spell;
- Ressurecting Carp will try to ressurect allied mobs.
- Animating Carp will try to animate nearby objects.
- Door-creating Carp will try to turn nearby walls into doors.

You can order Magicarp to cast their spell on something if you happen to
manage to tame one.
The eating element now has support for "getting hurt" when you eat
something. Carp eating can rings and hating it was too soulful not to
continue supporting.

## Why It's Good For The Game

Carp are iconic beasts and I think they should be more interesting.
Also we just want to turn mobs into basic mobs anyway.

## Changelog

:cl:
add: Carp will now run away if their health gets low, meaning they may
have a chance to regenerate.
add: Lia will now fight back if attacked instead of letting herself get
killed, watch out!
balance: Magicarp will now aim their spells more intelligently.
add: Tame Magicarp can be ordered to use their spells on things.
refactor: Carp are now "Basic Mobs" instead of "Simple Mobs"
fix: Dehydrated carp no longer give you a bad feeling when they're your
friend and a good feeling when they're going to attack you.
balance: Tamed carp are now friendly only to their tamer rather than
their whole faction, which should make dehydrated carp more active.
Order them to stay or follow you if you want them to behave around your
friends.
/:cl:

---
## [IndieanaJones/tgstation](https://github.com/IndieanaJones/tgstation)@[125745d232...](https://github.com/IndieanaJones/tgstation/commit/125745d232163406c107d3947b87d6d406ac3a17)
#### Friday 2023-01-27 20:25:36 by Fikou

guardian death checks (#72251)

## About The Pull Request
if a guardian summoner is dead during the summoner setting process, we
(the guardian) now kill ourselves since itd mean a guardian that cant
die
to combat some fucked upness of it (if you inject a guardian and it only
spawns after you died and then dusts you), the process of spawning a
guardian from the playerside guardian creator stuff gets canceled if
youre dead or dont exist

## Why It's Good For The Game
yeah that seems good

## Changelog
:cl:
fix: guardian spirits check for death before they add themselves to you
/:cl:

---
## [Abyss-Services/abyss-browser-OLD](https://github.com/Abyss-Services/abyss-browser-OLD)@[9fa00e07fd...](https://github.com/Abyss-Services/abyss-browser-OLD/commit/9fa00e07fd2633bc16776653987abcc05673910f)
#### Friday 2023-01-27 20:33:39 by pxstaa

ur ugly as fuck go away bitchhhh

yeahhh uhhh anyway go die

---
## [filipporomani/Wafflebot](https://github.com/filipporomani/Wafflebot)@[da7c290583...](https://github.com/filipporomani/Wafflebot/commit/da7c290583a6780860dffc7da2063be1b8591987)
#### Friday 2023-01-27 20:35:28 by fire6945

suck my cock, dpy. you just got L'ed on. you thought you could fucking trip me up like that, huh? well, you were fucking wrong. suck it up, bitch.

---
## [tcharding/rust-bitcoin](https://github.com/tcharding/rust-bitcoin)@[f6d983b2ef...](https://github.com/tcharding/rust-bitcoin/commit/f6d983b2ef4dfacd53499fd9f1d77058c0f396ff)
#### Friday 2023-01-27 20:54:12 by Andrew Poelstra

Merge rust-bitcoin/rust-bitcoin#1532: Improve Psbt error handling

e7bbfd391353fd03d60550c768364e9de5d3e8c5 Improve Psbt error handling (DanGould)

Pull request description:

  ## Separate `encode::Error` and `psbt::Error` recursive dependency

  This initial work attempts to fix #837's first 2 points

  > - The current psbt::serialize::Deserialize has an error type of consensus::encode::Error. I think we should cleanly separate consensus encoding errors from application-level encoding errors like psbt.
  > - There is a recursive dependence between encode::Error and psbt::Error which would need to be cleanly dissected and separated so that there is no dependence or only one-way dependence.

  ## Better `ParseError(String)` types

  arturomf94 how compatible do your #1310 changes look to address #837's third point with this design?

  > - There are a lot ParseError(String) messages that could use a better type to downflow the information.

  I think your prior art would completely address this issue now.

  ## On handling `io::Error` with an associated error

  `encode::Error` has an `Io` variant. now that `Psbt::deserialize` returns `psbt::Error` and produces an `io::Error`, we need an `Io` variant on `psbt::Error`. Except that doing so breaks  `#[derive(Eq)]` and lots of tests for `psbt::Error`.

  Kixunil, I'm trying to understand your feedback regarding a solution to this problem.

  > I believe that the best error untangling would be to make decodable error associated.

  > I meant having associated `Error` type at `Decodable` trait. Encoding should only fail if the writer fails so we should have `io::Error` there (at least until we have something like `genio`).
  >
  > > [it] is a problem to instantiate consensus::encode::Error in [the psbt] module for `io::Error`?
  >
  > It certainly does look strange. Maybe we should have this shared type:
  >
  > ```rust
  > /// Error used when reading or decoding fails.
  > pub enum ReadError<Io, Decode> {
  >     /// Reading failed
  >     Io(Io),
  >     /// Decoding failed
  >     Decode(Decode), // consensus and PSBT error here
  > }
  > ```
  >
  > However this one will be annoying to use with `?` :( We could have `ResultExt` to provide `decode()` and `io()` methods to make it easier.
  >
  > If that's not acceptable then I think deduplicated IO error is better.

  Kixunil didn't we just get rid of Psbt as `Decodable`? Would this make more sense to have as an error associated with `Deserialize`? Or did we do the opposite of what we should have by making Psbt only `Serialize`/`Deserialize` because of #934, where only consensus objects are allowed to be `Decodable`? I wonder if we prioritized that strict categorization and are stuck with worth machinery because of it. My goal with #988 was to get to a point where we could address #837 and ultimately implement PSBTv2.

ACKs for top commit:
  tcharding:
    ACK e7bbfd391353fd03d60550c768364e9de5d3e8c5
  apoelstra:
    ACK e7bbfd391353fd03d60550c768364e9de5d3e8c5

Tree-SHA512: 32975594fde42727ea9030f46570a1403ae1a108570ab115519ebeddc28938f141e2134b04d6b29ce94817ed776c13815dea5647c463e4a13b47ba55f4e7858a

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[780523112c...](https://github.com/git-for-windows/git/commit/780523112cecca1b4426b4ac482b08f883312576)
#### Friday 2023-01-27 21:08:31 by Johannes Schindelin

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

---
## [Kepteyn/Skyrat-tg](https://github.com/Kepteyn/Skyrat-tg)@[67ca6389d0...](https://github.com/Kepteyn/Skyrat-tg/commit/67ca6389d031e7b12813af27fe89ced9ce633a3c)
#### Friday 2023-01-27 21:15:44 by SkyratBot

[MIRROR] Adds the Sandstorm random event, directional meteor functionality, space sand. [MDB IGNORE] (#18338)

* Adds the Sandstorm random event, directional meteor functionality, space sand. (#71802)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

![sandstorm](https://user-images.githubusercontent.com/28870487/206070641-80d37afc-a365-4f5e-ad48-e8cdf0153ac9.png)

Hey guys, it's your boy. Back at it again with another meteor-adjacent
event PR.

Adds the Sandstorm random event, inspired by the long-unused admin only
one. It picks a direction to approach from, alerts the crew of its
imminent arrival, and after a little over a minute of preparatory time,
sends waves of sand and dust to grind down everything in that direction.

To accomplish this, some minor adjustments had to be made to meteor
generation code. They can now be passed an optional arg for a direction
to be thrown from, and will pick a random one if no direction is given.

Also introduces the newest addition to our cast of meteors -- space
sand! It's even weaker than space dust, and shows up exclusively in this
event. Space sand is **ineffective against rwalls**, and will not damage
the arrivals area's high-tech sand-resistant glass. This is to prevent
this event from venting one of the most dust-vulnerable areas on the
station, and to make sure new players aren't shafted into firelock hell
when the right angle is picked.

I did a lot of testing and tweaking of numbers to get the damage to
average at about the level I'm comfortable with. This is meant to be a
high-impact event that isn't as destructive (or unavoidable) as a meteor
wave. Speaking of avoidance, let's talk about mitigation:

You get an early warning and a direction the sand will come from. You
have time to grab repair supplies, move to safety, get a MODsuit. You
can make worthwhile repairs as the sand comes in from inside (or
outside, if you're brave enough) with nothing more than a welder and
iron sheets. If you're feeling particularly spicy, you can leverage your
prep time setting up shield generators, which spawn in engineering and
have been added to the maintenance machines loot pool. Anyone can
contribute, so do your part as a good crewmate and help out!

All that being said, the event can't be prevented entirely. Shit's going
to get shredded, especially on the outside of the station. Damage will
vary heavily based on the station and direction, ranging from
inconsequential to threatening. It should happen late enough into the
round that, at the bare minimum, the crew shouldn't be caught
unprepared.

For those of you who are worried, the ORIGINAL sandstorm admin event is
still with us too. It's been moved from the space dust file into the
Sandstorm event file. This PR also makes a very minor change to the
naming of the space _dust_ events, for better menuing.

So, to sum it all up: Sand hits grinds down one side of the station, you
get a minute of warning, shield generators now spawn in maintenance. Be
a good crewmate and help where you can.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

More event variety is good, and events that give the players agency on
how bad the impact will be is even better.

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

:cl: Rhials
add: Sandstorm random event! A random side of the station is pummeled by
an onslaught of sand and dust. If you hear that one is approaching, grab
a welder and some iron to help with repairs!
add: Space sand! It's weak and doesn't hurt reinforced walls, but
shouldn't be underestimated in high quantities.
code: You can now pass a start direction to the
spawn_meteors/spawn_meteor global procs.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

* Adds the Sandstorm random event, directional meteor functionality, space sand.

Co-authored-by: Rhials <Datguy33456@gmail.com>

---
## [AAGaming00/According-to-all-known-laws-of-aviation-there-is-no-way-a-bee-should-be-able-to-fly.-Its-wings-are-](https://github.com/AAGaming00/According-to-all-known-laws-of-aviation-there-is-no-way-a-bee-should-be-able-to-fly.-Its-wings-are-)@[a964a17856...](https://github.com/AAGaming00/According-to-all-known-laws-of-aviation-there-is-no-way-a-bee-should-be-able-to-fly.-Its-wings-are-/commit/a964a17856e96fe8fe55e3f7f96f64c0c0940877)
#### Friday 2023-01-27 21:17:20 by AAGaming

According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible. Yellow, black. Yellow, black. Yellow, black. Yellow, black. Ooh, black and yellow! Let's shake it up a little. Barry! Breakfast is ready! Coming! Hang on a second. Hello? Barry? Adam? Can you believe this is happening? I can't. I'll pick you up. Looking sharp. Use the stairs, Your father paid good money for those. Sorry. I'm excited. Here's the graduate. We're very proud of you, son. A perfect report card, all B's. Very proud. Ma! I got a thing going here. You got lint on your fuzz. Ow! That's me! Wave to us! We'll be in row 118,000. Bye! Barry, I told you, stop flying in the house! Hey, Adam. Hey, Barry. Is that fuzz gel? A little. Special day, graduation. Never thought I'd make it. Three days grade school, three days high school. Those were awkward. Three days college. I'm glad I took a day and hitchhiked around The Hive. You did come back different. Hi, Barry. Artie, growing a mustache? Looks good. Hear about Frankie? Yeah. You going to the funeral? No, I'm not going. Everybody knows, sting someone, you die. Don't waste it on a squirrel. Such a hothead. I guess he could have just gotten out of the way. I love this incorporating an amusement park into our day. That's why we don't need vacations. Boy, quite a bit of pomp under the circumstances. Well, Adam, today we are men. We are! Bee-men. Amen! Hallelujah! Students, faculty, distinguished bees, please welcome Dean Buzzwell. Welcome, New Hive City graduating class of 9:15. That concludes our ceremonies And begins your career at Honex Industries! Will we pick our job today? I heard it's just orientation. Heads up! Here we go. Keep your hands and antennas inside the tram at all times. Wonder what it'll be like? A little scary. Welcome to Honex, a division of Honesco and a part of the Hexagon Group. This is it! Wow. Wow. We know that you, as a bee, have worked your whole life to get to the point where you can work for your whole life. Honey begins when our valiant Pollen Jocks bring the nectar to The Hive. Our top-secret formula is automatically color-corrected, scent-adjusted and bubble-contoured into this soothing sweet syrup with its distinctive golden glow you know as... Honey! That girl was hot. She's my cousin! She is? Yes, we're all cousins. Right. You're right. At Honex, we constantly strive to improve every aspect of bee existence. These bees are stress-testing a new helmet technology. What do you think he makes? Not enough. Here we have our latest advancement, the Krelman. What does that do? Catches that little strand of honey that hangs after you pour it. Saves us millions. Can anyone work on the Krelman? Of course. Most bee jobs are small ones. But bees know that every small job, if it's done well, means a lot. But choose carefully because you'll stay in the job you pick for the rest of your life. The same job the rest of your life? I didn't know that. What's the difference? You'll be happy to know that bees, as a species, haven't had one day off in 27 million years. So you'll just work us to death? We'll sure try. Wow! That blew my mind! "What's the difference?" How can you say that? One job forever? That's an insane choice to have to make. I'm relieved. Now we only have to make one decision in life. But, Adam, how could they never have told us that? Why would you question anything? We're bees. We're the most perfectly functioning society on Earth. You ever think maybe things work a little too well here? Like what? Give me one example. I don't know. But you know what I'm talking about. Please clear the gate. Royal Nectar Force on approach. Wait a second. Check it out. Hey, those are Pollen Jocks! Wow. I've never seen them this close. They know what it's like outside The Hive. Yeah, but some don't come back. Hey, Jocks! Hi, Jocks! You guys did great! You're monsters! You're sky freaks! I love it! I love it! I wonder where they were. I don't know. Their day's not planned. Outside The Hive, flying who knows where, doing who knows what. You can't just decide to be a Pollen Jock. You have to be bred for that. Right. Look. That's more pollen than you and I will see in a lifetime. It's just a status symbol. Bees make too much of it. Perhaps. Unless you're wearing it and the ladies see you wearing it. Those ladies? Aren't they our cousins too? Distant. Distant. Look at these two. Couple of Hive Harrys. Let's have fun with them. It must be dangerous being a Pollen Jock. Yeah. Once a bear pinned me against a mushroom! He had a paw on my throat, and with the other, he was slapping me! Oh, my! I never thought I'd knock him out. What were you doing during this? Trying to alert the authorities. I can autograph that. A little gusty out there today, wasn't it, comrades? Yeah. Gusty. We're hitting a sunflower patch six miles from here tomorrow. Six miles, huh? Barry! A puddle jump for us, but maybe you're not up for it. Maybe I am. You are not! We're going 0900 at J-Gate. What do you think, buzzy-boy? Are you bee enough? I might be. It all depends on what 0900 means. Hey, Honex! Dad, you surprised me. You decide what you're interested in? Well, there's a lot of choices. But you only get one. Do you ever get bored doing the same job every day? Son, let me tell you about stirring. You grab that stick, and you just move it around, and you stir it around. You get yourself into a rhythm. It's a beautiful thing. You know, Dad, the more I think about it, maybe the honey field just isn't right for me. You were thinking of what, making balloon animals? That's a bad job for a guy with a stinger. Janet, your son's not sure he wants to go into honey! Barry, you are so funny sometimes. I'm not trying to be funny. You're not funny! You're going into honey. Our son, the stirrer! You're gonna be a stirrer? No one's listening to me! Wait till you see the sticks I have. I could say anything right now. I'm gonna get an ant tattoo! Let's open some honey and celebrate! Maybe I'll pierce my thorax. Shave my antennae. Shack up with a grasshopper. Get a gold tooth and call everybody "dawg"! I'm so proud. We're starting work today! Today's the day. Come on! All the good jobs will be gone. Yeah, right. Pollen counting, stunt bee, pouring, stirrer, front desk, hair removal... Is it still available? Hang on. Two left! One of them's yours! Congratulations! Step to the side. What'd you get? Picking crud out. Stellar! Wow! Couple of newbies? Yes, sir! Our first day! We are ready! Make your choice. You want to go first? No, you go. Oh, my. What's available? Restroom attendant's open, not for the reason you think. Any chance of getting the Krelman? Sure, you're on. I'm sorry, the Krelman just closed out. Wax monkey's always open. The Krelman opened up again. What happened? A bee died. Makes an opening. See? He's dead. Another dead one. Deady. Deadified. Two more dead. Dead from the neck up. Dead from the neck down. That's life! Oh, this is so hard! Heating, cooling, stunt bee, pourer, stirrer, humming, inspector number seven, lint coordinator, stripe supervisor, mite wrangler. Barry, what do you think I should... Barry? Barry! All right, we've got the sunflower patch in quadrant nine... What happened to you? Where are you? I'm going out. Out? Out where? Out there. Oh, no! I have to, before I go to work for the rest of my life. You're gonna die! You're crazy! Hello? Another call coming in. If anyone's feeling brave, there's a Korean deli on 83rd that gets their roses today. Hey, guys. Look at that. Isn't that the kid we saw yesterday? Hold it, son, flight deck's restricted. It's OK, Lou. We're gonna take him up. Really? Feeling lucky, are you? Sign here, here. Just initial that. Thank you. OK. You got a rain advisory today, and as you all know, bees cannot fly in rain. So be careful. As always, watch your brooms, hockey sticks, dogs, birds, bears and bats. Also, I got a couple of reports of root beer being poured on us. Murphy's in a home because of it, babbling like a cicada! That's awful. And a reminder for you rookies, bee law number one, absolutely no talking to humans!  All right, launch positions! Buzz, buzz, buzz, buzz! Buzz, buzz, buzz, buzz! Buzz, buzz, buzz, buzz! Black and yellow! Hello! You ready for this, hot shot? Yeah. Yeah, bring it on. Wind, check. Antennae, check. Nectar pack, check. Wings, check. Stinger, check. Scared out of my shorts, check. OK, ladies, let's move it out! Pound those petunias, you striped stem-suckers! All of you, drain those flowers! Wow! I'm out! I can't believe I'm out! So blue. I feel so fast and free! Box kite! Wow! Flowers! This is Blue Leader, We have roses visual. Bring it around 30 degrees and hold. Roses! 30 degrees, roger. Bringing it around. Stand to the side, kid. It's got a bit of a kick. That is one nectar collector! Ever see pollination up close? No, sir. I pick up some pollen here, sprinkle it over here. Maybe a dash over there, a pinch on that one. See that? It's a little bit of magic. That's amazing. Why do we do that? That's pollen power. More pollen, more flowers, more nectar, more honey for us. Cool. I'm picking up a lot of bright yellow, Could be daisies, Don't we need those? Copy that visual. Wait. One of these flowers seems to be on the move. Say again? You're reporting a moving flower? Affirmative. That was on the line! This is the coolest. What is it? I don't know, but I'm loving this color. It smells good. Not like a flower, but I like it. Yeah, fuzzy. Chemical-y. Careful, guys. It's a little grabby. My sweet lord of bees! Candy-brain, get off there! Problem! Guys! This could be bad. Affirmative. Very close. Gonna hurt. Mama's little boy. You are way out of position, rookie! Coming in at you like a missile! Help me! I don't think these are flowers. Should we tell him? I think he knows. What is this?! Match point! You can start packing up, honey, because you're about to eat it! Yowser! Gross. There's a bee in the car! Do something! I'm driving! Hi, bee. He's back here! He's going to sting me! Nobody move. If you don't move, he won't sting you. Freeze! He blinked! Spray him, Granny! What are you doing?! Wow... the tension level out here is unbelievable. I gotta get home. Can't fly in rain. Can't fly in rain. Can't fly in rain. Mayday! Mayday! Bee going down! Ken, could you close the window please? Ken, could you close the window please? Check out my new resume. I made it into a fold-out brochure. You see? Folds out. Oh, no. More humans. I don't need this. What was that? Maybe this time. This time. This time. This time! This time! This... Drapes! That is diabolical. It's fantastic. It's got all my special skills, even my top-ten favorite movies. What's number one? Star Wars? Nah, I don't go for that... kind of stuff. No wonder we shouldn't talk to them. They're out of their minds. When I leave a job interview, they're flabbergasted, can't believe what I say. There's the sun. Maybe that's a way out. I don't remember the sun having a big 75 on it. I predicted global warming. I could feel it getting hotter. At first I thought it was just me. Wait! Stop! Bee! Stand back. These are winter boots. Wait! Don't kill him! You know I'm allergic to them! This thing could kill me! Why does his life have less value than yours? Why does his life have any less value than mine? Is that your statement? I'm just saying all life has value. You don't know what he's capable of feeling. My brochure! There you go, little guy. I'm not scared of him.It's an allergic thing.  Put that on your resume brochure. My whole face could puff up. Make it one of your special skills. Knocking someone out is also a special skill. Right. Bye, Vanessa. Thanks. Vanessa, next week? Yogurt night? Sure, Ken. You know, whatever. You could put carob chips on there. Bye. Supposed to be less calories. Bye. I gotta say something. She saved my life. I gotta say something. All right, here it goes. Nah. What would I say? I could really get in trouble. It's a bee law. You're not supposed to talk to a human. I can't believe I'm doing this. I've got to. Oh, I can't do it. Come on! No. Yes. No. Do it. I can't. How should I start it? "You like jazz?" No, that's no good. Here she comes! Speak, you fool! Hi! I'm sorry. You're talking. Yes, I know. You're talking! I'm so sorry. No, it's OK. It's fine. I know I'm dreaming. But I don't recall going to bed. Well, I'm sure this is very disconcerting. This is a bit of a surprise to me. I mean, you're a bee! I am. And I'm not supposed to be doing this, but they were all trying to kill me. And if it wasn't for you... I had to thank you. It's just how I was raised. That was a little weird. I'm talking with a bee. Yeah. I'm talking to a bee. And the bee is talking to me! I just want to say I'm grateful. I'll leave now. Wait! How did you learn to do that? What? The talking thing. Same way you did, I guess. "Mama, Dada, honey." You pick it up. That's very funny. Yeah. Bees are funny. If we didn't laugh, we'd cry with what we have to deal with. Anyway... Can I... get you something? Like what? I don't know. I mean... I don't know. Coffee? I don't want to put you out. It's no trouble. It takes two minutes. It's just coffee. I hate to impose. Don't be ridiculous! Actually, I would love a cup. Hey, you want rum cake? I shouldn't. Have some. No, I can't. Come on! I'm trying to lose a couple micrograms. Where? These stripes don't help. You look great! I don't know if you know anything about fashion. Are you all right? No. He's making the tie in the cab as they're flying up Madison. He finally gets there. He runs up the steps into the church. The wedding is on. And he says, "Watermelon? I thought you said Guatemalan. Why would I marry a watermelon?" Is that a bee joke? That's the kind of stuff we do. Yeah, different. So, what are you gonna do, Barry? About work? I don't know. I want to do my part for The Hive, but I can't do it the way they want. I know how you feel. You do? Sure. My parents wanted me to be a lawyer or a doctor, but I wanted to be a florist. Really? My only interest is flowers. Our new queen was just elected with that same campaign slogan. Anyway, if you look... There's my hive right there. See it? You're in Sheep Meadow! Yes! I'm right off the Turtle Pond! No way! I know that area. I lost a toe ring there once. Why do girls put rings on their toes? Why not? It's like putting a hat on your knee. Maybe I'll try that. You all right, ma'am? Oh, yeah. Fine. Just having two cups of coffee! Anyway, this has been great. Thanks for the coffee. Yeah, it's no trouble. Sorry I couldn't finish it. If I did, I'd be up the rest of my life. Are you...? Can I take a piece of this with me? Sure! Here, have a crumb. Thanks! Yeah. All right. Well, then... I guess I'll see you around. Or not. OK, Barry. And thank you so much again... for before. Oh, that? That was nothing. Well, not nothing, but... Anyway... This can't possibly work. He's all set to go. We may as well try it. OK, Dave, pull the chute. Sounds amazing. It was amazing! It was the scariest, happiest moment of my life. Humans! I can't believe you were with humans! Giant, scary humans! What were they like? Huge and crazy. They talk crazy. They eat crazy giant things. They drive crazy. Do they try and kill you, like on TV? Some of them. But some of them don't. How'd you get back? Poodle. You did it, and I'm glad. You saw whatever you wanted to see. You had your "experience." Now you can pick out yourjob and be normal. Well... Well? Well, I met someone. You did? Was she Bee-ish? A wasp?! Your parents will kill you! No, no, no, not a wasp. Spider? I'm not attracted to spiders. I know it's the hottest thing, with the eight legs and all. I can't get by that face. So who is she? She's... human. No, no. That's a bee law. You wouldn't break a bee law. Her name's Vanessa. Oh, boy. She's so nice. And she's a florist! Oh, no! You're dating a human florist! We're not dating. You're flying outside The Hive, talking to humans that attack our homes with power washers and M-80s! One-eighth a stick of dynamite! She saved my life! And she understands me. This is over! Eat this. This is not over! What was that? They call it a crumb. It was so stingin' stripey! And that's not what they eat. That's what falls off what they eat! You know what a Cinnabon is? No. It's bread and cinnamon and frosting. They heat it up... Sit down! ...really hot! Listen to me! We are not them! We're us. There's us and there's them! Yes, but who can deny the heart that is yearning? There's no yearning. Stop yearning. Listen to me! You have got to start thinking bee, my friend. Thinking bee! Thinking bee. Thinking bee. Thinking bee! Thinking bee! Thinking bee! Thinking bee! There he is. He's in the pool. You know what your problem is, Barry? I gotta start thinking bee? How much longer will this go on? It's been three days! Why aren't you working? I've got a lot of big life decisions to think about. What life? You have no life! You have no job. You're barely a bee! Would it kill you to make a little honey? Barry, come out. Your father's talking to you. Martin, would you talk to him? Barry, I'm talking to you! You coming? Got everything? All set! Go ahead. I'll catch up. Don't be too long. Watch this! Vanessa! We're still here. I told you not to yell at him. He doesn't respond to yelling! Then why yell at me? Because you don't listen! I'm not listening to this. Sorry, I've gotta go. Where are you going? I'm meeting a friend. A girl? Is this why you can't decide? Bye. I just hope she's Bee-ish. They have a huge parade of flowers every year in Pasadena? To be in the Tournament of Roses, that's every florist's dream! Up on a float, surrounded by flowers, crowds cheering. A tournament. Do the roses compete in athletic events? No. All right, I've got one. How come you don't fly everywhere? It's exhausting. Why don't you run everywhere? It's faster. Yeah, OK, I see, I see. All right, your turn. TiVo. You can just freeze live TV? That's insane! You don't have that? We have Hivo, but it's a disease. It's a horrible, horrible disease. Oh, my. Dumb bees! You must want to sting all those jerks. We try not to sting. It's usually fatal for us. So you have to watch your temper. Very carefully. You kick a wall, take a walk, write an angry letter and throw it out. Work through it like any emotion: Anger, jealousy, lust. Oh, my goodness! Are you OK? Yeah. What is wrong with you?! It's a bug. He's not bothering anybody. Get out of here, you creep! What was that? A Pic 'N' Save circular? Yeah, it was. How did you know? It felt like about 10 pages. Seventy-five is pretty much our limit. You've really got that down to a science. I lost a cousin to Italian Vogue. I'll bet. What in the name of Mighty Hercules is this? How did this get here? cute Bee, Golden Blossom, Ray Liotta Private Select? Is he that actor? I never heard of him. Why is this here? For people. We eat it. You don't have enough food of your own? Well, yes. How do you get it? Bees make it. I know who makes it! And it's hard to make it! There's heating, cooling, stirring. You need a whole Krelman thing! It's organic. It's our-ganic! It's just honey, Barry. Just what?! Bees don't know about this! This is stealing! A lot of stealing! You've taken our homes, schools,hospitals! This is all we have! And it's on sale?! I'm getting to the bottom of this. I'm getting to the bottom of all of this! Hey, Hector. You almost done? Almost. He is here. I sense it. Well, I guess I'll go home now and just leave this nice honey out, with no one around. You're busted, box boy! I knew I heard something. So you can talk! I can talk. And now you'll start talking! Where you getting the sweet stuff? Who's your supplier? I don't understand. I thought we were friends. The last thing we want to do is upset bees! You're too late! It's ours now! You, sir, have crossed the wrong sword! You, sir, will be lunch for my iguana, Ignacio! Where is the honey coming from? Tell me where! Honey Farms! It comes from Honey Farms! Crazy person! What horrible thing has happened here? These faces, they never knew what hit them. And now they're on the road to nowhere! Just keep still. What? You're not dead? Do I look dead? They will wipe anything that moves. Where you headed? To Honey Farms. I am onto something huge here. I'm going to Alaska. Moose blood, crazy stuff. Blows your head off! I'm going to Tacoma. And you? He really is dead. All right. Uh-oh! What is that?! Oh, no! A wiper! Triple blade! Triple blade? Jump on! It's your only chance, bee! Why does everything have to be so doggone clean?! How much do you people need to see?! Open your eyes! Stick your head out the window! From NPR News in Washington, I'm Carl Kasell. But don't kill no more bugs! Bee! Moose blood guy!! You hear something? Like what? Like tiny screaming. Turn off the radio. Whassup, bee boy? Hey, Blood. Just a row of honey jars, as far as the eye could see. Wow! I assume wherever this truck goes is where they're getting it. I mean, that honey's ours. Bees hang tight. We're all jammed in. It's a close community. Not us, man. We on our own. Every mosquito on his own. What if you get in trouble? You a mosquito, you in trouble. Nobody likes us. They just smack. See a mosquito, smack, smack! At least you're out in the world. You must meet girls. Mosquito girls try to trade up, get with a moth, dragonfly. Mosquito girl don't want no mosquito. You got to be kidding me! Mooseblood's about to leave the building! So long, bee! Hey, guys! Mooseblood! I knew I'd catch y'all down here. Did you bring your crazy straw? We throw it in jars, slap a label on it, and it's pretty much pure profit. What is this place? A bee's got a brain the size of a pinhead. They are pinheads! Pinhead. Check out the new smoker. Oh, sweet. That's the one you want. The Thomas 3000! Smoker? Ninety puffs a minute, semi-automatic. Twice the nicotine, all the tar. A couple breaths of this knocks them right out. They make the honey, and we make the money. "They make the honey, and we make the money"? Oh, my! What's going on? Are you OK? Yeah. It doesn't last too long. Do you know you're in a fake hive with fake walls? Our queen was moved here. We had no choice. This is your queen? That's a man in women's clothes! That's a drag queen! What is this? Oh, no! There's hundreds of them! Bee honey. Our honey is being brazenly stolen on a massive scale! This is worse than anything bears have done! I intend to do something. Oh, Barry, stop. Who told you humans are taking our honey? That's a rumor. Do these look like rumors? That's a conspiracy theory. These are obviously doctored photos. How did you get mixed up in this? He's been talking to humans. What? Talking to humans?! He has a human girlfriend. And they make out! Make out? Barry! We do not. You wish you could. Whose side are you on? The bees! I dated a cricket once in San Antonio. Those crazy legs kept me up all night. Barry, this is what you want to do with your life? I want to do it for all our lives. Nobody works harder than bees! Dad, I remember you coming home so overworked your hands were still stirring. You couldn't stop. I remember that. What right do they have to our honey? We live on two cups a year. They put it in lip balm for no reason whatsoever! Even if it's true, what can one bee do? Sting them where it really hurts. In the face! The eye! That would hurt. No. Up the nose? That's a killer. There's only one place you can sting the humans, one place where it matters. Hive at Five, The Hive's only full-hour action news source. No more bee beards! With Bob Bumble at the anchor desk. Weather with Storm Stinger. Sports with Buzz Larvi. And Jeanette Chung. Good evening. I'm Bob Bumble. And I'm Jeanette Ohung. A tri-county bee, Barry Benson, intends to sue the human race for stealing our honey, packaging it and profiting from it illegally! Tomorrow night on Bee Larry King, we'll have three former queens here in our studio, discussing their new book, classy Ladies, out this week on Hexagon. Tonight we're talking to Barry Benson. Did you ever think, "I'm a kid from The Hive. I can't do this"? Bees have never been afraid to change the world. What about Bee Oolumbus? Bee Gandhi? Bejesus? Where I'm from, we'd never sue humans. We were thinking of stickball or candy stores. How old are you? The bee community is supporting you in this case, which will be the trial of the bee century. You know, they have a Larry King in the human world too. It's a common name. Next week... He looks like you and has a show and suspenders and colored dots... Next week... Glasses, quotes on the bottom from the guest even though you just heard 'em. Bear Week next week! They're scary, hairy and here live. Always leans forward, pointy shoulders, squinty eyes, very Jewish. In tennis, you attack at the point of weakness! It was my grandmother, Ken. She's 81. Honey, her backhand's a joke! I'm not gonna take advantage of that? Quiet, please. Actual work going on here. Is that that same bee? Yes, it is! I'm helping him sue the human race. Hello. Hello, bee. This is Ken. Yeah, I remember you. Timberland, size ten and a half. Vibram sole, I believe. Why does he talk again? Listen, you better go 'cause we're really busy working. But it's our yogurt night! Bye-bye. Why is yogurt night so difficult?! You poor thing. You two have been at this for hours! Yes, and Adam here has been a huge help. Frosting... How many sugars? Just one. I try not to use the competition. So why are you helping me? Bees have good qualities. And it takes my mind off the shop. Instead of flowers, people are giving balloon bouquets now. Those are great, if you're three. And artificial flowers. Oh, those just get me psychotic! Yeah, me too. Bent stingers, pointless pollination. Bees must hate those fake things! Nothing worse than a daffodil that's had work done. Maybe this could make up for it a little bit. This lawsuit's a pretty big deal. I guess. You sure you want to go through with it? Am I sure? When I'm done with the humans, they won't be able to say, "Honey, I'm home," without paying a royalty! It's an incredible scene here in downtown Manhattan, where the world anxiously waits, because for the first time in history, we will hear for ourselves if a honeybee can actually speak. What have we gotten into here, Barry? It's pretty big, isn't it? I can't believe how many humans don't work during the day. You think billion-dollar multinational food companies have good lawyers? Everybody needs to stay behind the barricade. What's the matter? I don't know, I just got a chill. Well, if it isn't the bee team. You boys work on this? All rise! The Honorable Judge Bumbleton presiding. All right. Case number 4475, Superior Court of New York, Barry Bee Benson v. the Honey Industry is now in session. Mr. Montgomery, you're representing the five food companies collectively? A privilege. Mr. Benson... you're representing all the bees of the world? I'm kidding. Yes, Your Honor, we're ready to proceed. Mr. Montgomery, your opening statement, please. Ladies and gentlemen of the jury, my grandmother was a simple woman. Born on a farm, she believed it was man's divine right to benefit from the bounty of nature God put before us. If we lived in the topsy-turvy world Mr. Benson imagines, just think of what would it mean. I would have to negotiate with the silkworm for the elastic in my britches! Talking bee! How do we know this isn't some sort of holographic motion-picture-capture Hollywood wizardry? They could be using laser beams! Robotics! Ventriloquism! Cloning! For all we know, he could be on steroids! Mr. Benson? Ladies and gentlemen, there's no trickery here. I'm just an ordinary bee. Honey's pretty important to me. It's important to all bees. We invented it! We make it. And we protect it with our lives. Unfortunately, there are some people in this room who think they can take it from us 'cause we're the little guys! I'm hoping that, after this is all over, you'll see how, by taking our honey, you not only take everything we have but everything we are! I wish he'd dress like that all the time. So nice! Call your first witness. So, Mr. Klauss Vanderhayden of Honey Farms, big company you have. I suppose so. I see you also own Honeyburton and Honron! Yes, they provide beekeepers for our farms. Beekeeper. I find that to be a very disturbing term. I don't imagine you employ any bee-free-ers, do you? No. I couldn't hear you. No. No. Because you don't free bees. You keep bees. Not only that, it seems you thought a bear would be an appropriate image for a jar of honey. They're very lovable creatures. Yogi Bear, Fozzie Bear, Build-A-Bear. You mean like this? Bears kill bees! How'd you like his head crashing through your living room?! Biting into your couch! Spitting out your throw pillows! OK, that's enough. Take him away. So, Mr. Sting, thank you for being here. Your name intrigues me. Where have I heard it before? I was with a band called The Police. But you've never been a police officer, have you? No, I haven't. No, you haven't. And so here we have yet another example of bee culture casually stolen by a human for nothing more than a prance-about stage name. Oh, please. Have you ever been stung, Mr. Sting? Because I'm feeling a little stung, Sting. Or should I say... Mr. Gordon M. Sumner! That's not his real name?! You idiots! Mr. Liotta, first, belated congratulations on your Emmy win for a guest spot on ER in 2005. Thank you. Thank you. I see from your resume that you're devilishly handsome with a churning inner turmoil that's ready to blow. I enjoy what I do. Is that a crime? Not yet it isn't. But is this what it's come to for you? Exploiting tiny, helpless bees so you don't have to rehearse your part and learn your lines, sir? Watch it, Benson! I could blow right now! This isn't a goodfella. This is a badfella! Why doesn't someone just step on this creep, and we can all go home?! Order in this court! You're all thinking it! Order! Order, I say! Say it! Mr. Liotta, please sit down! I think it was awfully nice of that bear to pitch in like that. I think the jury's on our side. Are we doing everything right, legally? I'm a florist. Right. Well, here's to a great team. To a great team! Well, hello. Ken! Hello. I didn't think you were coming. No, I was just late I tried to call, but... the battery. I didn't want all this to go to waste, so I called Barry. Luckily, he was free. Oh, that was lucky. There's a little left. I could heat it up. Yeah, heat it up, sure, whatever. So I hear you're quite a tennis player. I'm not much for the game myself. The ball's a little grabby. That's where I usually sit. Right... there. Ken, Barry was looking at your resume, and he agreed with me that eating with chopsticks isn't really a special skill. You think I don't see what you're doing? I know how hard it is to find the right job. We have that in common. Do we? Bees have 100 percent employment, but we do jobs like taking the crud out. That's just what I was thinking about doing. Ken, I let Barry borrow your razor for his fuzz. I hope that was all right. I'm going to drain the old stinger. Yeah, you do that. Look at that. You know, I've just about had it with your little Mind Games. What's that? Italian Vogue. Mamma mia, that's a lot of pages. A lot of ads. Remember what Van said, why is your life more valuable than mine? Funny, I just can't seem to recall that! I think something stinks in here! I love the smell of flowers. How do you like the smell of flames?! Not as much. Water bug! Not taking sides! Ken, I'm wearing a Chapstick hat! This is pathetic! I've got issues! Well, well, well, a royal flush! You're bluffing. Am I? Surf's up, dude! Poo water! That bowl is gnarly. Except for those dirty yellow rings! Kenneth! What are you doing?! You know, I don't even like honey! I don't eat it! We need to talk! He's just a little bee! And he happens to be the nicest bee I've met in a long time! Long time? What are you talking about?! Are there other bugs in your life?  No, but there are other things bugging me in life. And you're one of them! Fine! Talking bees, no yogurt night... My nerves are fried from riding on this emotional roller coaster! Goodbye, Ken. And for your information, I prefer sugar-free, artificial sweeteners made by man! I'm sorry about all that. I know it's got an aftertaste! I like it! I always felt there was some kind of barrier between Ken and me. I couldn't overcome it. Oh, well. Are you OK for the trial? I believe Mr. Montgomery is about out of ideas. We would like to call Mr. Barry Benson Bee to the stand. Good idea! You can really see why he's considered one of the best lawyers... Yeah. Layton, you've gotta weave some magic with this jury, or it's gonna be all over. Don't worry. The only thing I have to do to turn this jury around is to remind them of what they don't like about bees. You got the tweezers? Are you allergic? Only to losing, son. Only to losing. Mr. Benson Bee, I'll ask you what I think we'd all like to know. What exactly is your relationship to that woman? We're friends. Good friends? Yes. How good? Do you live together? Wait a minute... Are you her little... bedbug? I've seen a bee documentary or two. From what I understand, doesn't your queen give birth to all the bee children? Yeah, but... So those aren't your real parents! Oh, Barry... Yes, they are! Hold me back! You're an illegitimate bee, aren't you, Benson? He's denouncing bees! Don't y'all date your cousins? Objection! I'm going to pincushion this guy! Adam, don't! It's what he wants! Oh, I'm hit!! Oh, lordy, I am hit! Order! Order! The venom! The venom is coursing through my veins! I have been felled by a winged beast of destruction! You see? You can't treat them like equals! They're striped savages! Stinging's the only thing they know! It's their way! Adam, stay with me. I can't feel my legs. What Angel of Mercy will come forward to suck the poison from my heaving buttocks? I will have order in this court. Order! Order, please! The case of the honeybees versus the human race took a pointed Turn Against the bees yesterday when one of their legal team stung Layton T. Montgomery. Hey, buddy. Hey. Is there much pain? Yeah. I... I blew the whole case, didn't I? It doesn't matter. What matters is you're alive. You could have died. I'd be better off dead. Look at me. They got it from the cafeteria downstairs, in a tuna sandwich. Look, there's a little celery still on it. What was it like to sting someone? I can't explain it. It was all... All adrenaline and then...and then ecstasy! All right. You think it was all a trap? Of course. I'm sorry. I flew us right into this. What were we thinking? Look at us. We're just a couple of bugs in this world. What will the humans do to us if they win? I don't know. I hear they put the roaches in motels. That doesn't sound so bad. Adam, they check in, but they don't check out! Oh, my. Could you get a nurse to close that window? Why? The smoke. Bees don't smoke. Right. Bees don't smoke. Bees don't smoke! But some bees are smoking. That's it! That's our case! It is? It's not over? Get dressed. I've gotta go somewhere. Get back to the court and stall. Stall any way you can. And assuming you've done step correctly, you're ready for the tub. Mr. Flayman. Yes? Yes, Your Honor! Where is the rest of your team? Well, Your Honor, it's interesting. Bees are trained to fly haphazardly, and as a result, we don't make very good time. I actually heard a funny story about... Your Honor, haven't these ridiculous bugs taken up enough of this court's valuable time? How much longer will we allow these absurd shenanigans to go on? They have presented no compelling evidence to support their charges against my clients, who run legitimate businesses. I move for a complete dismissal of this entire case! Mr. Flayman, I'm afraid I'm going to have to consider Mr. Montgomery's motion. But you can't! We have a terrific case. Where is your proof? Where is the evidence? Show me the smoking gun! Hold it, Your Honor! You want a smoking gun? Here is your smoking gun. What is that? It's a bee smoker! What, this? This harmless little contraption? This couldn't hurt a fly, let alone a bee. Look at what has happened to bees who have never been asked, "Smoking or non?" Is this what nature intended for us? To be forcibly addicted to smoke machines and man-made wooden slat work camps? Living out our lives as honey slaves to the white man? What are we gonna do? He's playing the species card. Ladies and gentlemen, please, free these bees! Free the bees! Free the bees! Free the bees! Free the bees! Free the bees! The court finds in favor of the bees! Vanessa, we won! I knew you could do it! High-five! Sorry. I'm OK! You know what this means? All the honey will finally belong to the bees. Now we won't have to work so hard all the time. This is an unholy perversion of the balance of nature, Benson. You'll regret this. Barry, how much honey is out there? All right. One at a time. Barry, who are you wearing? My sweater is Ralph Lauren, and I have no pants. What if Montgomery's right? What do you mean? We've been living the bee way a long time, 27 million years. Congratulations on your victory. What will you demand as a settlement? First, we'll demand a complete shutdown of all bee work camps. Then we want back the honey that was ours to begin with, every last drop. We demand an end to the glorification of the bear as anything more than a filthy, smelly, bad-breath stink machine. We're all aware of what they do in the woods. Wait for my signal. Take him out. He'll have nauseous for a few hours, then he'll be fine. And we will no longer tolerate bee-negative nicknames... But it's just a prance-about stage name! ...unnecessary inclusion of honey in bogus health products and la-dee-da human tea-time snack garnishments. Can't breathe. Bring it in, boys! Hold it right there! Good. Tap it. Mr. Buzzwell, we just passed three cups and there's gallons more coming! I think we need to shut down! Shut down? We've never shut down. Shut down honey production! Stop making honey! Turn your key, sir! What do we do now? Cannonball! We're shutting honey production! Mission abort. Aborting pollination and nectar detail. Returning to base. Adam, you wouldn't believe how much honey was out there. Oh, yeah? What's going on? Where is everybody? Are they out celebrating? They're home. They don't know what to do. Laying out, sleeping in. I heard your Uncle Carl was on his way to San Antonio with a cricket. At least we got our honey back. Sometimes I think, so what if humans liked our honey? Who wouldn't? It's the greatest thing in the world! I was excited to be part of making it. This was my new desk. This was my new job. I wanted to do it really well. And now... Now I can't. I don't understand why they're not happy. I thought their lives would be better! They're doing nothing. It's amazing. Honey really changes people. You don't have any idea what's going on, do you? What did you want to show me? This. What happened here? That is not the half of it. Oh, no. Oh, my. They're all wilting. Doesn't look very good, does it? No. And whose fault do you think that is? You know, I'm gonna guess bees. Bees? Specifically, me. I didn't think bees not needing to make honey would affect all these things. It's not just flowers. Fruits, vegetables, they all need bees. That's our whole SAT test right there. Take away produce, that affects the entire animal kingdom. And then, of course... The human species? So if there's no more pollination, it could all just go south here, couldn't it? I know this is also partly my fault. How about a suicide pact? How do we do it? I'll sting you, you step on me. That just kills you twice. Right, right. Listen, Barry... sorry, but I gotta get going. I had to open my mouth and talk. Vanessa? Vanessa? Why are you leaving? Where are you going? To the final Tournament of Roses parade in Pasadena. They've moved it to this weekend because all the flowers are dying. It's the Last Chance I'll ever have to see it. Vanessa, I just wanna say I'm sorry. I never meant it to turn out like this. I know. Me neither. Tournament of Roses. Roses can't do sports. Wait a minute. Roses. Roses? Roses! Vanessa! Roses?! Barry? Roses are flowers! Yes, they are. Flowers, bees, pollen! I know. That's why this is the last parade. Maybe not. Could you ask him to slow down? Could you slow down? Barry! OK, I made a huge mistake. This is a total disaster, all my fault. Yes, it kind of is. I've ruined the planet. I wanted to help you with the flower shop. I've made it worse. Actually, it's completely closed down. I thought maybe you were remodeling. But I have another idea, and it's greater than my previous ideas combined. I don't want to hear it! All right, they have the roses, the roses have the pollen. I know every bee, plant and flower bud in this park. All we gotta do is get what they've got back here with what we've got. Bees. Park. Pollen! Flowers. Repollination! Across the nation! Tournament of Roses, Pasadena, California. They've got nothing but flowers, floats and cotton candy. Security will be tight. I have an idea. Vanessa Bloome, FTD. Official floral business. It's real. Sorry, ma'am. Nice brooch. Thank you. It was a gift. Once inside, we just pick the right float. How about The Princess and the Pea? I could be the princess, and you could be the pea! Yes, I got it. Where should I sit? What are you? I believe I'm the pea. The pea? It goes under the mattresses. Not in this fairy tale, sweetheart. I'm getting the marshal. You do that! This whole parade is a fiasco! Let's see what this baby'll do. Hey, what are you doing?! Then all we do is blend in with traffic... without arousing suspicion. Once at the airport, there's no stopping us. Stop! Security. You and your insect pack your float? Yes. Has it been in your possession the entire time? Would you remove your shoes? Remove your stinger. It's part of me. I know. Just having some fun. Enjoy your flight. Then if we're lucky, we'll have just enough pollen to do the job. Can you believe how lucky we are? We have just enough pollen to do the job! I think this is gonna work. It's got to work. Attention, passengers, this is Captain Scott. We have a bit of bad weather in New York. It looks like we'll experience a couple hours delay. Barry, these are cut flowers with no water. They'll never make it. I gotta get up there and talk to them. Be careful. Can I get help with the Sky Mall magazine? I'd like to order the talking inflatable nose and ear hair trimmer. Captain, I'm in a real situation. What'd you say, Hal? Nothing. Bee! Don't freak out! My entire species... What are you doing? Wait a minute! I'm an attorney! Who's an attorney? Don't move. Oh, Barry. Good afternoon, passengers. This is your captain. Would a Miss Vanessa Bloome in 24B please report to the cockpit? And please hurry! What happened here? There was a DustBuster, a toupee, a life raft exploded. One's bald, one's in a boat, they're both unconscious! Is that another bee joke? No! No one's flying the plane! This is JFK control tower, Flight 356. What's your status? This is Vanessa Bloome. I'm a florist from New York. Where's the pilot? He's unconscious, and so is the copilot. Not good. Does anyone onboard have flight experience? As a matter of fact, there is. Who's that? Barry Benson. From the honey trial?! Oh, great. Vanessa, this is nothing more than a big metal bee. It's got giant wings, huge engines. I can't fly a plane. Why not? Isn't John Travolta a pilot? Yes. How hard could it be? Wait, Barry! We're headed into some lightning. This is Bob Bumble. We have some late-breaking news from JFK Airport, where a suspenseful scene is developing. Barry Benson, fresh from his legal victory... That's Barry! ...is attempting to land a plane, loaded with people, flowers and an incapacitated flight crew. Flowers?! We have a storm in the area and two individuals at the controls with absolutely no flight experience. Just a minute. There's a bee on that plane. I'm quite familiar with Mr. Benson and his no-account compadres. They've done enough damage. But isn't he your only hope? Technically, a bee shouldn't be able to fly at all. Their wings are too small... Haven't we heard this a million times? "The surface area of the wings and body mass make no sense." Get this on the air! Got it. Stand by. We're going live. The way we work may be a mystery to you. Making honey takes a lot of bees doing a lot of small jobs. But let me tell you about a small job. If you do it well, it makes a big difference. More than we realized. To us, to everyone. That's why I want to get bees back to working together. That's the bee way! We're not made of Jell-O. We get behind a fellow. Black and yellow! Hello! Left, right, down, hover. Hover? Forget hover. This isn't so hard. Beep-beep! Beep-beep! Barry, what happened?! Wait, I think we were on autopilot the whole time. That may have been helping me. And now we're not! So it turns out I cannot fly a plane. All of you, let's get behind this fellow! Move it out! Move out! Our only chance is if I do what I'd do, you copy me with the wings of the plane! Don't have to yell. I'm not yelling! We're in a lot of trouble. It's very hard to concentrate with that panicky tone in your voice! It's not a tone. I'm panicking! I can't do this! Vanessa, pull yourself together. You have to snap out of it! You snap out of it. You snap out of it. You snap out of it! You snap out of it! You snap out of it! You snap out of it! You snap out of it! You snap out of it! Hold it! Why? Come on, it's my turn. How is the plane flying? I don't know. Hello? Benson, got any flowers for a happy occasion in there? The Pollen Jocks! They do get behind a fellow. Black and yellow. Hello. All right, let's drop this tin can on the blacktop. Where? I can't see anything. Can you? No, nothing. It's all cloudy. Come on. You got to think bee, Barry. Thinking bee. Thinking bee. Thinking bee! Thinking bee! Thinking bee! Wait a minute. I think I'm feeling something. What? I don't know. It's strong, pulling me. Like a 27-million-year-old instinct. Bring the nose down. Thinking bee! Thinking bee! Thinking bee! What in the world is on the tarmac? Get some lights on that! Thinking bee! Thinking bee! Thinking bee! Vanessa, aim for the flower. OK. Cut the engines. We're going in on bee power. Ready, boys? Affirmative! Good. Good. Easy, now. That's it. Land on that flower! Ready? Full reverse! Spin it around! Not that flower! The other one! Which one? That flower. I'm aiming at the flower! That's a fat guy in a flowered shirt. I mean the giant pulsating flower made of millions of bees! Pull forward. Nose down. Tail up. Rotate around it. This is insane, Barry! This's the only way I know how to fly. Am I koo-koo-kachoo, or is this plane flying in an insect-like pattern? Get your nose in there. Don't be afraid. Smell it. Full reverse! Just drop it. Be a part of it. Aim for the center! Now drop it in! Drop it in, woman! Come on, already. Barry, we did it! You taught me how to fly! Yes. No high-five! Right. Barry, it worked! Did you see the giant flower? What giant flower? Where? Of course I saw the flower! That was genius! Thank you. But we're not done yet. Listen, everyone! This runway is covered with the last pollen from the last flowers available anywhere on Earth. That means this is our Last Chance. We're the only ones who make honey, pollinate flowers and dress like this. If we're gonna survive as a species, this is our moment! What do you say? Are we going to be bees, or just Museum of Natural History keychains? We're bees! Keychain! Then follow me! Except Keychain. Hold on, Barry. Here. You've earned this. Yeah! I'm a Pollen Jock! And it's a perfect fit. All I gotta do are the sleeves. Oh, yeah. That's our Barry. Mom! The bees are back! If anybody needs to make a call, now's the time. I got a feeling we'll be working late tonight! Here's your change. Have a great afternoon! Can I help who's next? Would you like some honey with that? It is bee-approved. Don't forget these. Milk, cream, cheese, it's all me.  And I don't see a nickel! Sometimes I just feel like a piece of meat! I had no idea. Barry, I'm sorry. Have you got a moment? Would you excuse me? My mosquito associate will help you. Sorry I'm late. He's a lawyer too? I was already a blood-sucking parasite. All I needed was a briefcase. Have a great afternoon! Barry, I just got this huge tulip order, and I can't get them anywhere. No problem, Vannie. Just leave it to me. You're a lifesaver, Barry. Can I help who's next? All right, scramble, jocks! It's time to fly. Thank you, Barry! That bee is living my life! Let it go, Kenny. When will this nightmare end?! Let it all go. Beautiful day to fly. Sure is. Between you and me, I was dying to get out of that office. You have got to start thinking bee, my friend. Thinking bee! Me? Hold it. Let's just stop for a second. Hold it. I'm sorry. I'm sorry, everyone. Can we stop here? I'm not making a major life decision during a production number! All right. Take ten, everybody. Wrap it up, guys. I had virtually no rehearsal for that.

According to all known laws of aviation, there is no way a bee should be able to fly.
Its wings are too small to get its fat little body off the ground.
The bee, of course, flies anyway because bees don't care what humans think is impossible.
Yellow, black. Yellow, black. Yellow, black. Yellow, black.
Ooh, black and yellow!
Let's shake it up a little.
Barry! Breakfast is ready!
Coming!
Hang on a second.
Hello?
Barry?
Adam?
Can you believe this is happening?
I can't.
I'll pick you up.
Looking sharp.
Use the stairs, Your father paid good money for those.
Sorry. I'm excited.
Here's the graduate.
We're very proud of you, son.
A perfect report card, all B's.
Very proud.
Ma! I got a thing going here.
You got lint on your fuzz.
Ow! That's me!
Wave to us! We'll be in row 118,000.
Bye!
Barry, I told you, stop flying in the house!
Hey, Adam.
Hey, Barry.
Is that fuzz gel?
A little. Special day, graduation.
Never thought I'd make it.
Three days grade school, three days high school.
Those were awkward.
Three days college. I'm glad I took a day and hitchhiked around The Hive.
You did come back different.
Hi, Barry. Artie, growing a mustache? Looks good.
Hear about Frankie?
Yeah.
You going to the funeral?
No, I'm not going.
Everybody knows, sting someone, you die.
Don't waste it on a squirrel.
Such a hothead.
I guess he could have just gotten out of the way.
I love this incorporating an amusement park into our day.
That's why we don't need vacations.
Boy, quite a bit of pomp under the circumstances.
Well, Adam, today we are men.
We are!
Bee-men.
Amen!
Hallelujah!
Students, faculty, distinguished bees,
please welcome Dean Buzzwell.
Welcome, New Hive City graduating class of 9:15.
That concludes our ceremonies And begins your career at Honex Industries!
Will we pick our job today?
I heard it's just orientation.
Heads up! Here we go.
Keep your hands and antennas inside the tram at all times.
Wonder what it'll be like?
A little scary.
Welcome to Honex, a division of Honesco and a part of the Hexagon Group.
This is it!
Wow.
Wow.
We know that you, as a bee, have worked your whole life to get to the point where you can work for your whole life.
Honey begins when our valiant Pollen Jocks bring the nectar to The Hive.
Our top-secret formula is automatically color-corrected, scent-adjusted and bubble-contoured into this soothing sweet syrup with its distinctive golden glow you know as... Honey!
That girl was hot.
She's my cousin!
She is?
Yes, we're all cousins.
Right. You're right.
At Honex, we constantly strive to improve every aspect of bee existence.
These bees are stress-testing a new helmet technology.
What do you think he makes?
Not enough.
Here we have our latest advancement, the Krelman.
What does that do?
Catches that little strand of honey that hangs after you pour it.
Saves us millions.
Can anyone work on the Krelman?
Of course. Most bee jobs are small ones.
But bees know that every small job, if it's done well, means a lot.
But choose carefully because you'll stay in the job you pick for the rest of your life.
The same job the rest of your life? I didn't know that.
What's the difference?
You'll be happy to know that bees, as a species, haven't had one day off in 27 million years.
So you'll just work us to death?
We'll sure try.
Wow! That blew my mind!
"What's the difference?"
How can you say that?
One job forever?
That's an insane choice to have to make.
I'm relieved. Now we only have to make one decision in life.
But, Adam, how could they never have told us that?
Why would you question anything? We're bees.
We're the most perfectly functioning society on Earth.
You ever think maybe things work a little too well here?
Like what? Give me one example.
I don't know. But you know what I'm talking about.
Please clear the gate. Royal Nectar Force on approach.
Wait a second. Check it out.
Hey, those are Pollen Jocks!
Wow.
I've never seen them this close.
They know what it's like outside The Hive.
Yeah, but some don't come back.
Hey, Jocks!
Hi, Jocks!
You guys did great!
You're monsters!
You're sky freaks! I love it! I love it!
I wonder where they were.
I don't know.
Their day's not planned.
Outside The Hive, flying who knows where, doing who knows what.
You can't just decide to be a Pollen Jock. You have to be bred for that.
Right.
Look. That's more pollen than you and I will see in a lifetime.
It's just a status symbol.
Bees make too much of it.
Perhaps. Unless you're wearing it and the ladies see you wearing it.
Those ladies?
Aren't they our cousins too?
Distant. Distant.
Look at these two.
Couple of Hive Harrys.
Let's have fun with them.
It must be dangerous being a Pollen Jock.
Yeah. Once a bear pinned me against a mushroom!
He had a paw on my throat, and with the other, he was slapping me!
Oh, my!
I never thought I'd knock him out.
What were you doing during this?
Trying to alert the authorities.
I can autograph that.
A little gusty out there today, wasn't it, comrades?
Yeah. Gusty.
We're hitting a sunflower patch six miles from here tomorrow.
Six miles, huh?
Barry!
A puddle jump for us, but maybe you're not up for it.
Maybe I am.
You are not!
We're going 0900 at J-Gate.
What do you think, buzzy-boy?
Are you bee enough?
I might be. It all depends on what 0900 means.
Hey, Honex!
Dad, you surprised me.
You decide what you're interested in?
Well, there's a lot of choices.
But you only get one.
Do you ever get bored doing the same job every day?
Son, let me tell you about stirring.
You grab that stick, and you just move it around, and you stir it around.
You get yourself into a rhythm.
It's a beautiful thing.
You know, Dad, the more I think about it,
maybe the honey field just isn't right for me.
You were thinking of what, making balloon animals?
That's a bad job for a guy with a stinger.
Janet, your son's not sure he wants to go into honey!
Barry, you are so funny sometimes.
I'm not trying to be funny.
You're not funny! You're going into honey. Our son, the stirrer!
You're gonna be a stirrer?
No one's listening to me!
Wait till you see the sticks I have.
I could say anything right now.
I'm gonna get an ant tattoo!
Let's open some honey and celebrate!
Maybe I'll pierce my thorax. Shave my antennae. Shack up with a grasshopper. Get a gold tooth and call everybody "dawg"!
I'm so proud.
We're starting work today!
Today's the day.
Come on! All the good jobs will be gone.
Yeah, right.
Pollen counting, stunt bee, pouring, stirrer, front desk, hair removal...
Is it still available?
Hang on. Two left!
One of them's yours! Congratulations!
Step to the side.
What'd you get?
Picking crud out. Stellar!
Wow!
Couple of newbies?
Yes, sir! Our first day! We are ready!
Make your choice.
You want to go first?
No, you go.
Oh, my. What's available?
Restroom attendant's open, not for the reason you think.
Any chance of getting the Krelman?
Sure, you're on.
I'm sorry, the Krelman just closed out.
Wax monkey's always open.
The Krelman opened up again.
What happened?
A bee died. Makes an opening. See? He's dead. Another dead one.
Deady. Deadified. Two more dead.
Dead from the neck up. Dead from the neck down. That's life!
Oh, this is so hard!
Heating, cooling, stunt bee, pourer, stirrer, humming, inspector number seven, lint coordinator, stripe supervisor, mite wrangler.
Barry, what do you think I should... Barry?
Barry!
All right, we've got the sunflower patch in quadrant nine...
What happened to you?
Where are you?
I'm going out.
Out? Out where?
Out there.
Oh, no!
I have to, before I go to work for the rest of my life.
You're gonna die! You're crazy! Hello?
Another call coming in.
If anyone's feeling brave, there's a Korean deli on 83rd that gets their roses today.
Hey, guys.
Look at that.
Isn't that the kid we saw yesterday?
Hold it, son, flight deck's restricted.
It's OK, Lou. We're gonna take him up.
Really? Feeling lucky, are you?
Sign here, here. Just initial that.
Thank you.
OK.
You got a rain advisory today, and as you all know, bees cannot fly in rain.
So be careful. As always, watch your brooms, hockey sticks, dogs, birds, bears and bats.
Also, I got a couple of reports of root beer being poured on us.
Murphy's in a home because of it, babbling like a cicada!
That's awful.
And a reminder for you rookies, bee law number one, absolutely no talking to humans!
 All right, launch positions!
Buzz, buzz, buzz, buzz! Buzz, buzz, buzz, buzz! Buzz, buzz, buzz, buzz!
Black and yellow!
Hello!
You ready for this, hot shot?
Yeah. Yeah, bring it on.
Wind, check.
Antennae, check.
Nectar pack, check.
Wings, check.
Stinger, check.
Scared out of my shorts, check.
OK, ladies,
let's move it out!
Pound those petunias, you striped stem-suckers!
All of you, drain those flowers!
Wow! I'm out!
I can't believe I'm out!
So blue.
I feel so fast and free!
Box kite!
Wow!
Flowers!
This is Blue Leader, We have roses visual.
Bring it around 30 degrees and hold.
Roses!
30 degrees, roger. Bringing it around.
Stand to the side, kid.
It's got a bit of a kick.
That is one nectar collector!
Ever see pollination up close?
No, sir.
I pick up some pollen here, sprinkle it over here. Maybe a dash over there, a pinch on that one.
See that? It's a little bit of magic.
That's amazing. Why do we do that?
That's pollen power. More pollen, more flowers, more nectar, more honey for us.
Cool.
I'm picking up a lot of bright yellow, Could be daisies, Don't we need those?
Copy that visual.
Wait. One of these flowers seems to be on the move.
Say again? You're reporting a moving flower?
Affirmative.
That was on the line!
This is the coolest. What is it?
I don't know, but I'm loving this color.
It smells good.
Not like a flower, but I like it.
Yeah, fuzzy.
Chemical-y.
Careful, guys. It's a little grabby.
My sweet lord of bees!
Candy-brain, get off there!
Problem!
Guys!
This could be bad.
Affirmative.
Very close.
Gonna hurt.
Mama's little boy.
You are way out of position, rookie!
Coming in at you like a missile!
Help me!
I don't think these are flowers.
Should we tell him?
I think he knows.
What is this?!
Match point!
You can start packing up, honey, because you're about to eat it!
Yowser!
Gross.
There's a bee in the car!
Do something!
I'm driving!
Hi, bee.
He's back here!
He's going to sting me!
Nobody move. If you don't move, he won't sting you. Freeze!
He blinked!
Spray him, Granny!
What are you doing?!
Wow... the tension level out here is unbelievable.
I gotta get home.
Can't fly in rain. Can't fly in rain. Can't fly in rain.
Mayday! Mayday! Bee going down!
Ken, could you close the window please?
Ken, could you close the window please?
Check out my new resume. I made it into a fold-out brochure. You see? Folds out.
Oh, no. More humans. I don't need this.
What was that?
Maybe this time. This time. This time. This time! This time! This... Drapes!
That is diabolical.
It's fantastic. It's got all my special skills, even my top-ten favorite movies.
What's number one? Star Wars?
Nah, I don't go for that... kind of stuff.
No wonder we shouldn't talk to them. They're out of their minds.
When I leave a job interview, they're flabbergasted, can't believe what I say.
There's the sun. Maybe that's a way out.
I don't remember the sun having a big 75 on it.
I predicted global warming. I could feel it getting hotter. At first I thought it was just me.
Wait! Stop! Bee!
Stand back. These are winter boots.
Wait!
Don't kill him!
You know I'm allergic to them! This thing could kill me!
Why does his life have less value than yours?
Why does his life have any less value than mine? Is that your statement?
I'm just saying all life has value. You don't know what he's capable of feeling.
My brochure!
There you go, little guy.
I'm not scared of him.It's an allergic thing.
 Put that on your resume brochure.
My whole face could puff up.
Make it one of your special skills.
Knocking someone out is also a special skill.
Right. Bye, Vanessa. Thanks.
Vanessa, next week? Yogurt night?
Sure, Ken. You know, whatever.
You could put carob chips on there.
Bye.
Supposed to be less calories.
Bye.
I gotta say something. She saved my life. I gotta say something.
All right, here it goes.
Nah.
What would I say?
I could really get in trouble. It's a bee law. You're not supposed to talk to a human.
I can't believe I'm doing this. I've got to.
Oh, I can't do it. Come on!
No. Yes. No. Do it. I can't.
How should I start it? "You like jazz?" No, that's no good.
Here she comes! Speak, you fool!
Hi!
I'm sorry. You're talking.
Yes, I know.
You're talking!
I'm so sorry.
No, it's OK. It's fine.
I know I'm dreaming. But I don't recall going to bed.
Well, I'm sure this is very disconcerting.
This is a bit of a surprise to me. I mean, you're a bee!
I am. And I'm not supposed to be doing this, but they were all trying to kill me.
And if it wasn't for you... I had to thank you. It's just how I was raised.
That was a little weird. I'm talking with a bee.
Yeah.
I'm talking to a bee. And the bee is talking to me!
I just want to say I'm grateful.
I'll leave now.
Wait! How did you learn to do that?
What?
The talking thing.
Same way you did, I guess. "Mama, Dada, honey." You pick it up.
That's very funny.
Yeah.
Bees are funny. If we didn't laugh, we'd cry with what we have to deal with.
Anyway... Can I... get you something?
Like what?
I don't know. I mean... I don't know. Coffee?
I don't want to put you out.
It's no trouble. It takes two minutes.
It's just coffee.
I hate to impose.
Don't be ridiculous!
Actually, I would love a cup.
Hey, you want rum cake?
I shouldn't.
Have some.
No, I can't.
Come on!
I'm trying to lose a couple micrograms.
Where?
These stripes don't help.
You look great!
I don't know if you know anything about fashion.
Are you all right?
No.
He's making the tie in the cab as they're flying up Madison.
He finally gets there.
He runs up the steps into the church.
The wedding is on.
And he says, "Watermelon?
I thought you said Guatemalan.
Why would I marry a watermelon?"
Is that a bee joke?
That's the kind of stuff we do.
Yeah, different.
So, what are you gonna do, Barry?
About work? I don't know.
I want to do my part for The Hive, but I can't do it the way they want.
I know how you feel.
You do?
Sure.
My parents wanted me to be a lawyer or a doctor, but I wanted to be a florist.
Really?
My only interest is flowers.
Our new queen was just elected with that same campaign slogan.
Anyway, if you look... There's my hive right there. See it?
You're in Sheep Meadow!
Yes! I'm right off the Turtle Pond!
No way! I know that area. I lost a toe ring there once.
Why do girls put rings on their toes?
Why not?
It's like putting a hat on your knee.
Maybe I'll try that.
You all right, ma'am?
Oh, yeah. Fine.
Just having two cups of coffee!
Anyway, this has been great.
Thanks for the coffee.
Yeah, it's no trouble.
Sorry I couldn't finish it. If I did, I'd be up the rest of my life.
Are you...?
Can I take a piece of this with me?
Sure! Here, have a crumb.
Thanks!
Yeah.
All right. Well, then... I guess I'll see you around. Or not.
OK, Barry.
And thank you so much again... for before.
Oh, that? That was nothing.
Well, not nothing, but... Anyway...
This can't possibly work.
He's all set to go.
We may as well try it.
OK, Dave, pull the chute.
Sounds amazing.
It was amazing!
It was the scariest, happiest moment of my life.
Humans! I can't believe you were with humans!
Giant, scary humans!
What were they like?
Huge and crazy. They talk crazy.
They eat crazy giant things.
They drive crazy.
Do they try and kill you, like on TV?
Some of them. But some of them don't.
How'd you get back?
Poodle.
You did it, and I'm glad. You saw whatever you wanted to s…

---
## [pavel-petrenko/terminal](https://github.com/pavel-petrenko/terminal)@[77215d9d77...](https://github.com/pavel-petrenko/terminal/commit/77215d9d77b99b48d1ee8302736178f2ec9f3a77)
#### Friday 2023-01-27 22:11:30 by Mike Griese

Fix `ShowWindow(GetConsoleWindow())` (#13118)

A bad merge, that actually revealed a horrible bug.

There was a secret conflict between the code in #12526 and #12515. 69b77ca was a bad merge that hid just how bad the issue was. Fixing the one line `nullptr`->`this` in `InteractivityFactory` resulted in a window that would flash uncontrollably, as it minimized and restored itself in a loop. Great. 

This can seemingly be fixed by making sure that the conpty window is initially created with the owner already set, rather than relying on a `SetParent` call in post. This does pose some complications for the #1256 future we're approaching. However, this is a blocking bug _now_, and we can figure out the tearout/`SetParent` thing in post. 

* fixes #13066.
* Tested with the script in that issue.
* Window doesn't flash uncontrollably.
* `gci | ogv` still works right
* I work here.
* Opening a new tab doesn't spontaneously cause the window to minimize
* Restoring from minimized doesn't yeet focus to an invisible window
* Opening a new tab doesn't yeet focus to an invisible window
* There _is_ a viable way to call `GetAncestor` s.t. it returns the Terminal's hwnd in Terminal, and the console's in Conhost


The `SW_SHOWNOACTIVATE` change is also quite load bearing. With just `SW_NORMAL`, the pseudo window (which is invisible!) gets activated whenever the terminal window is restored from minimized. That's BAD.


There's actually more to this as well. 


Calling `SetParent` on a window that is `WS_VISIBLE` will cause the OS to hide the window, make it a _child_ window, then call `SW_SHOW` on the window to re-show it. `SW_SHOW`, however, will cause the OS to also set that window as the _foreground_ window, which would result in the pty's hwnd stealing the foreground away from the owning terminal window. That's bad.

`SetWindowLongPtr` seems to do the job of changing who the window owner is, without all the other side effects of reparenting the window. 

Without `SetParent`, however, the pty HWND is no longer a descendant of the Terminal HWND, so that means `GA_ROOT` can no longer be used to find the owner's hwnd. For even more insanity, without `WS_POPUP`, none of the values of `GetAncestor` will actually get the terminal HWND. So, now we also need `WS_POPUP` on the pty hwnd. To get at the Terminal hwnd, you'll need

```c++
GetAncestor(GetConsoleWindow(), GA_ROOTOWNER)
```

---
## [pavel-petrenko/terminal](https://github.com/pavel-petrenko/terminal)@[9ccd6ecd74...](https://github.com/pavel-petrenko/terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Friday 2023-01-27 22:11:30 by Mike Griese

Manually copy trailing attributes on a resize (#12637)

## THE WHITE WHALE

This is a fairly naive fix for this bug. It's not terribly performant,
but neither is resize in the first place.

When the buffer gets resized, typically we only copy the text up to the
`MeasureRight` point, the last printable char in the row. Then we'd just
use the last char's attributes to fill the remainder of the row.

Instead, this PR changes how reflow behaves when it gets to the end of
the row. After we finish copying text, then manually walk through the
attributes at the end of the row, and copy them over. This ensures that
cells that just have a colored space in them get copied into the new
buffer as well, and we don't just blat the last character's attributes
into the rest of the row. We'll do a similar thing once we get to the
last printable char in the buffer, copying the remaining attributes.

This could DEFINITELY be more performant. I think this current
implementation walks the attrs _on every cell_, then appends the new
attrs to the new ATTR_ROW. That could be optimized by just using the
actual iterator. The copy after the last printable char bit is also
especially bad in this regard. That could likely be a blind copy - I
just wanted to get this into the world.

Finally, we now copy the final attributes to the correct buffer: the new
one.  We used to copy them to the _old_ buffer, which we were about to
destroy.

## Validation

I'll add more gifs in the morning, not enough time to finish spinning a
release Terminal build with this tonight.

Closes #32 🎉🎉🎉🎉🎉🎉🎉🎉🎉
Closes #12567

(cherry picked from commit 855e1360c0ff810decf862f1d90e15b5f49e7bbd)

---
## [measurement-factory/daft](https://github.com/measurement-factory/daft)@[51fee554f9...](https://github.com/measurement-factory/daft/commit/51fee554f9f22a52cbde519da072c59fac7cd038)
#### Friday 2023-01-27 22:36:12 by Alex Rousskov

Restart DUT for each test attempt; rework test concurrency

When starting tests, Runner.js applied all test attempts to the same DUT
instance. Also, each sequential attempt could have experienced a
significantly different test concurrency level as threads with fewer
necessary attempts would quit first.

    DUT start
    for_each thread in threads
        while more attempts are necessary
            test_object.run()
    DUT shutdown

To reduce unknown differences between test attempts (both in terms of
DUT state and in terms of concurrency levels), we now restart the DUT
for each attempt and apply concurrency at each attempt level:

    while more attempts are necessary
        DUT start
        for_each thread in threads
            test_object.run()
        DUT shutdown

Also established and polished related terminology (in src/test/Runner.js
preamble).

This change started with a failure to reproduce some old test results.
The failing test (proxy-collapsed-forwarding) was known to be unstable
and used 10 attempts by default to mitigate that flaw. I was thinking
that something in the test environment had changed, resulting in those
repeated attempts being less effective than before.

I increased the number of attempts to at least 100, but that did not
help. That outcome was puzzling -- an unstable but otherwise "working"
test should succeed if retried "enough" times. In retrospect, I should
have assumed that the old code being tested probably never passed this
test, but I realized something else instead: Keeping the DUT running
though multiple test attempts increases the difference between attempts
and might prevent the test from succeeding! While differences in random
"noise" may help an unstable test, non-random differences in DUT state
(due to artifacts of earlier attempts) may also doom these repeated
attempts (and complicate triage of individual attempts).

Reproducible results, even negative ones, are better than having a
chance of success: If a test reliably fails, it will be fixed or
removed. Either is a much better outcome than a test that suddenly
starts failing for no good reason. We should not make the DUT state more
complex in hope that some poorly understood state change helps a lucky
test attempt to succeed. CI tests should control as much as feasible,
reducing inter-test dependencies, so that even an unstable test can
"reliably" succeed when retried enough times.

---

