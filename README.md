## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-10-31](docs/good-messages/2022/2022-10-31.md)


2,193,818 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,193,818 were push events containing 3,340,748 commit messages that amount to 268,757,175 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 35 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[85b2d5043d...](https://github.com/tgstation/tgstation/commit/85b2d5043dbc9eb277bf57dd6dc5147ae08fe978)
#### Monday 2022-10-31 00:02:45 by LemonInTheDark

Optimizes qdel related things (slight init time savings) (#70729)

* Moves spawners and decals to a different init/delete scheme

Rather then fully creating and then immediately deleting these things,
we instead do the bare minimum.

This is faster, if in theory more fragile. We should be safe since any
errors should be caught in compile since this is very close to a
"static" action. It does mean these atoms cannot use signals, etc.

* Potentially saves init time, mostly cleans up a silly pattern

We use sleeps and INVOKE_ASYNC to ensure that handing back turfs doesn't
block a space reservation, but this by nature consumes up to the
threshold and a bit more of whatever working block we were in.

This is silly. Should just be a subsystem, so I made it one, with
support for awaiting its finish if you want to

* Optimizes garbage/proc/Queue slightly

Queue takes about 1.6 seconds to process 26k items right now.
The MASSIVE majority of this time is spent on using \ref
This is because \ref returns a string, and that string requires being
inserted into the global cache of strings we store

What I'm doing is caching the result of ANY \ref on the datum it's
applied to. This ensures previous uses will never decay from the string
tree.

This saves about 0.2 seconds of init

---
## [usnpeepoo/cmss13](https://github.com/usnpeepoo/cmss13)@[ca2114f0f5...](https://github.com/usnpeepoo/cmss13/commit/ca2114f0f56ab4a51443bdac52053ead327724dc)
#### Monday 2022-10-31 00:22:56 by Mister-moon1

Removes some useless code from welding helmet (#1363)

* fuck you useless code

* you cannot hide, useless code

---
## [usnpeepoo/cmss13](https://github.com/usnpeepoo/cmss13)@[2a8ebba36a...](https://github.com/usnpeepoo/cmss13/commit/2a8ebba36a2c76ed855987dc107c9c385f6f16ea)
#### Monday 2022-10-31 00:22:56 by Joelampost

Pred bug fix no.2 (#1287)

* a

a

* Update code/game/objects/structures/tables_racks.dm

Co-authored-by: harryob <me@harryob.live>

* Update yaut_procs.dm

* :>(

* fuck you

* return

* Update code/modules/cm_preds/yaut_procs.dm

Co-authored-by: Stan_Albatross <66756236+stanalbatross@users.noreply.github.com>

* Update code/game/objects/structures/tables_racks.dm

Co-authored-by: Stan_Albatross <66756236+stanalbatross@users.noreply.github.com>

Co-authored-by: harryob <me@harryob.live>
Co-authored-by: Stan_Albatross <66756236+stanalbatross@users.noreply.github.com>

---
## [OliOliOnsiPree/tgstation](https://github.com/OliOliOnsiPree/tgstation)@[14c96d05b8...](https://github.com/OliOliOnsiPree/tgstation/commit/14c96d05b82cd377dc3fe04944fdb4ece6176bd9)
#### Monday 2022-10-31 00:40:12 by scriptis

TGUI for Techfabs II: The Great Recategorizing (AND ICONS) (AND MECHFABS) (AND AUTOLATHES) (#69990)

    I recategorized EVERY /datum/design/ IN THE GAME to be more UX friendly and I HATE MYSELF FOR IT
    I refactored techfab UI to WORK ANYWHERE for ANY MACHINE THAT USES /datum/design as a SET OF MODULAR COMPONENTS
    I moved a lot of DESIGNS EXCLUSIVE TO THE AUTOLATHE to also work IN PROTOLATHES
    I made MATERIAL ICONS animate between ICON STATES for STACKS
    I PUT ICONS IN ALL OF YOUR FABRICATORS
    I SOMEHOW DID ALL OF THIS WITHOUT LOSING ANY PERFORMANCE
    ALSO SUPPORTS COMPONENT PRINTERS AND MODULE DUPLICATORS

Other garbage:

    Fixed numerous spelling and consistency issues in designs
    Removed Machine Design (<x>) and Computer Design (<x>) from all relevant designs
    All designs are now in title case
    Numerous designs that were formerly autolathe exclusives can now also be printed at a protolathe (but not all); this is mostly just service equipment like drinking glasses and plates and silverware
    Circuits components can no longer be printed at a circuit imprinter (fixes 

    Integrated circuit components printed in the component printer/module printer cost twice as much than from an un upgraded circuit printer #67758)
    Designs that are not sensible for a department to have are no longer accessible to that department (read: medbay printing turbine parts)

Why It's Good For The Game

Improved UX for techfabs, but also for mechfabs and autolathes, and oh look it's pretty!

also I spent like eight hours doing nothing but categorizing /datum/designs and I'll cry if some version of this doesn't get merged eventually
Changelog

cl
refactor: mechfabs, autolathes, component printers, and module duplicators now use techfab tgui components
refactor: every single design is now categorized and subcategorized
refactor: mechfabs and autolathes are now in typescript
qol: techfabs now have icons for what you're about to print
qol: techfab material icons are now animated
qol: techfab material icons now fade when no materials are available
qol: techfab searching no longer lags like hell
qol: techfab searching now searches all recipes instead of just the current category
qol: techfabs now have subcategorization (stock part users rejoice)
qol: techfabs now announce when new recipes are available
qol: numerous other techfab ui tweaks
balance: some designs that were formerly autolathe exclusive can now be printed at some departmental techfabs

---
## [Jolly-66/JollyStation](https://github.com/Jolly-66/JollyStation)@[0cd78be6a1...](https://github.com/Jolly-66/JollyStation/commit/0cd78be6a19a9a3d6907cdf84759c59717dd8cb4)
#### Monday 2022-10-31 00:41:32 by TaleStationBot

[MIRROR] [MDB IGNORE] Heretics cannot be converted, and are immune to cult stun hands. Instead, the cult is rewarded for sacrificing them with the bloody bastard sword, an oversized SPIN2WIN funblade. + Soul Stealing Fantasy Affix (#2617)

* Heretics cannot be converted, and are immune to cult stun hands. Instead, the cult is rewarded for sacrificing them with the bloody bastard sword, an oversized SPIN2WIN funblade. + Soul Stealing Fantasy Affix (#69725)

About The Pull Request

Heretics can no longer be converted to a cult, as they follow their own Forgotten Gods.
Instead, Nar'Sie will reward the cult for managing to sacrifice one, with the bastard sword.
The bloody bastard sword has been cleaned up codewise and all that. Because it is a free reward instead of a (removed) progression mechanic of cult, it swings just a bit slower during the spin and doesn't have a jaunt. It's still a !fun! swinging sword of hilarity and death.
BLOODY BASTARD https://www.youtube.com/watch?v=ukznXQ3MgN0
Fantasy weapons can now roll "soul-stealing" weapons. They, on killing something, capture its soul inside the item.

    Add fail conditions that instantly end a spin2win, ala how 

    Mimes can now hold a baguette like a sword by right clicking it #69592 works

Why It's Good For The Game

Bloody bastard sword was fun, it made no sense that heretics were valid converts when they're already worshipping a DIFFERENT evil god granting them powers. Should be in a good spot as a nice little antag to antag special interaction. I fucking love antag to antag special interactions, we should have more of 'em

Fantasy affixes are always a neat thing to throw a new component into
Changelog

cl
add: Heretics can no longer be converted to cult. But sacrificing them is very valuable to Nar'Sie, and she will grant special weapons if you manage to do so.
add: Fantasy affixes can also include soul-stealing items!
/cl

* Heretics cannot be converted, and are immune to cult stun hands. Instead, the cult is rewarded for sacrificing them with the bloody bastard sword, an oversized SPIN2WIN funblade. + Soul Stealing Fantasy Affix

Co-authored-by: tralezab <40974010+tralezab@users.noreply.github.com>

---
## [zjkk123/odoo](https://github.com/zjkk123/odoo)@[1636ba5ed2...](https://github.com/zjkk123/odoo/commit/1636ba5ed2f8a284bef0930313a85cc3dc7cf072)
#### Monday 2022-10-31 01:50:33 by qsm-odoo

[FIX] website, *: allow to re-edit company team snippet images

*: website_sale

Since [1], it was not possible to edit a company team snippet image
anymore as soon as the page was saved once. Indeed that commit added
o_not_editable/contenteditable="false" on the parent column to make sure
no text can be added in that column and contenteditable="true" on the
images so that they are still editable (even though HTML-specs-wise
adding contenteditable="true" on images probably does not mean much as
images are self-closing tags, our editor understand that as the ability
to edit the image anyway). That contenteditable="true" part is however
removed when leaving edit mode... and was not restored upon entering
edit mode again.

This fixes the problems with a specific JS patch, we'll review to see if
better can be done in master.

Funny enough, that bug was actually gone in 15.0... by mistake. A recent
bug fix actually reintroduced that isolated bug at [2] (by reintroducing
the fact that images in a non-editable environment are not possible to
edit). The 3 opened tickets this commit mentions were actually reported
for 15.0 immediately after that, while the 14.0 being broken about this
since the beginning apparently did not bother anyone.

Note: as a forward-ported fix, this also takes the opportunity to clean
a bit what was done at [3]. (calling `_super`, no duplicated code,
adding comments, ...).

[1]: https://github.com/odoo/odoo/commit/656cac1bf21c7c5a56aa569008aac58436c747fb
[2]: https://github.com/odoo/odoo/commit/e113bae04a64a8bd341a80736086ab7c25079dd3
[3]: https://github.com/odoo/odoo/commit/e2f7b8fad76dc816b2f6864340d3740446117cdb

opw-3031217
opw-3032482
opw-3035289

closes odoo/odoo#104335

X-original-commit: 61270ee8bffb6e85f8ff0d19c7a3889fdce2f486
Signed-off-by: Romain Derie (rde) <rde@odoo.com>
Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>

---
## [cheekybrdy/goonstation](https://github.com/cheekybrdy/goonstation)@[693f38836f...](https://github.com/cheekybrdy/goonstation/commit/693f38836f362b8083c1d0169c7e5c17196852f1)
#### Monday 2022-10-31 02:02:04 by aloe

why do you set vis_flags if you aren't going to use vis_contents fuck you

---
## [ruiznorlan/odoo](https://github.com/ruiznorlan/odoo)@[e7c8fed8e3...](https://github.com/ruiznorlan/odoo/commit/e7c8fed8e373d7005c16c88d3a7bad6f425d13e5)
#### Monday 2022-10-31 02:04:07 by qsm-odoo

[FIX] website, *: allow to re-edit company team snippet images

*: web_editor

Since [1], it was not possible to edit a company team snippet image
anymore as soon as the page was saved once. Indeed that commit added
o_not_editable/contenteditable="false" on the parent column to make sure
no text can be added in that column and contenteditable="true" on the
images so that they are still editable (even though HTML-specs-wise
adding contenteditable="true" on images probably does not mean much as
images are self-closing tags, our editor understand that as the ability
to edit the image anyway). That contenteditable="true" part is however
removed when leaving edit mode... and was not restored upon entering
edit mode again.

This fixes the problems with an ugly patch. We'll review what to do in
master.

Funny enough, that bug was actually gone in 15.0... by mistake. A recent
bug fix actually reintroduced that isolated bug at [2] (by reintroducing
the fact that images in a non-editable environment are not possible to
edit). The 3 opened tickets this commit mentions were actually reported
for 15.0 immediately after that, while the 14.0 being broken about this
since the beginning apparently did not bother anyone.

[1]: https://github.com/odoo/odoo/commit/656cac1bf21c7c5a56aa569008aac58436c747fb
[2]: https://github.com/odoo/odoo/commit/e113bae04a64a8bd341a80736086ab7c25079dd3

opw-3031217
opw-3032482
opw-3035289

closes odoo/odoo#104156

Signed-off-by: Romain Derie (rde) <rde@odoo.com>

---
## [Mooshimi/tgstation](https://github.com/Mooshimi/tgstation)@[b2be252eb6...](https://github.com/Mooshimi/tgstation/commit/b2be252eb61e91f3aac08b1e4160420e444db3e8)
#### Monday 2022-10-31 02:08:02 by san7890

UpdatePaths Readme - Reforged (#70806)

* UpdatePaths Readme - Reforged

I'm a bit tired after typing for the last hour so apologies if some of this stuff is unreadable. Basically, I just took time to add a small blurb about UpdatePaths in MAPS_AND_AWAY_MISSIONS.md, as well as write out examples on how you can properly use every single function UpdatePaths might have. I'm probably missing something? I think I got everything though. Let me know if I should be consistent somehow, but I did deliberately choose different test-cases per example because it's nearly impossible to come up one "generic" fit-all situation that illustrates every possible use of UpdatePaths (to my small mind).

Anyways, hope this helps.

* i fucked up with the TGM format

augh

---
## [DarkFire01/reactos](https://github.com/DarkFire01/reactos)@[73eedb1fbf...](https://github.com/DarkFire01/reactos/commit/73eedb1fbf30a5f0f3f50d5e13c27c78acd0a156)
#### Monday 2022-10-31 02:17:12 by George Bișoc

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
## [4812571/opa](https://github.com/4812571/opa)@[965301f90e...](https://github.com/4812571/opa/commit/965301f90e1c10900c2c134ee21e486993796a20)
#### Monday 2022-10-31 02:44:44 by Stephan Renatus

ast: support dotted heads (#4660)

This change allows rules to have string prefixes in their heads -- we've
come to call them "ref heads".

String prefixes means that where before, you had

    package a.b.c
    allow = true

you can now have

    package a
    b.c.allow = true

This allows for more concise policies, and different ways to structure
larger rule corpuses.

Backwards-compatibility:

- There are code paths that accept ast.Module structs that don't necessarily
  come from the parser -- so we're backfilling the rule's Head.Reference
  field from the Name when it's not present.
  This is exposed through (Head).Ref() which always returns a Ref.

  This also affects the `opa parse` "pretty" output:

  With x.rego as

    package x
    import future.keywords
    a.b.c.d if true
    e[x] if true

  we get

    $ opa parse x rego
    module
     package
      ref
       data
       "x"
     import
      ref
       future
       "keywords"

     rule
      head
       ref
        a
        "b"
        "c"
        "d"
       true
      body
       expr index=0
        true
     rule
      head
       ref
        e
        x
       true
      body
       expr index=0
        true

  Note that

    Name: e
    Key: x

  becomes

    Reference: e[x]

  in the output above (since that's how we're parsing it, back-compat edge cases aside)

- One special case for backcompat is `p[x] { ... }`:

    rule                    | ref   | key | value | name
    ------------------------+-------+-----+-------+-----
    p[x] { ... }            | p     | x   | nil   | "p"
    p contains x if { ... } | p     | x   | nil   | "p"
    p[x] if { ... }         | p[x]  | nil | true  | ""

  For interpreting a rule, we now have the following procedure:

  1. if it has a Key, it's a multi-value rule; and its Ref defines the set:

     Head{Key: x, Ref: p} ~> p is a set
     ^-- we'd get this from `p contains x if true`
         or `p[x] { true }` (back compat)

  2. if it has a Value, it's a single-value rule; its Ref may contain vars:

     Head{Ref: p.q.r[s], Value: 12} ~> body determines s, `p.q.r.[s]` is 12
     ^-- we'd get this from `p.q.r[s] = 12 { s := "whatever" }`

     Head{Key: x, Ref: p[x], Value: 3} ~> `p[x]` has value 3, `x` is determined
                                          by the rule body
     ^-- we'd get this from `p[x] = 3 if x := 2`
         or `p[x] = 3 { x := 2 }` (back compat)

     Here, the Key isn't used, it's present for backwards compatibility: for ref-
     less rule heads, `p[x] = 3` used to be a partial object: key x, value 3,
     name "p"

- The destinction between complete rules and partial object rules disappears.
  They're both single-value rules now.

- We're now outputting the refs of the rules completely in error messages, as
  it's hard to make sense of "rule r" when there's rule r in package a.b.c and
  rule b.c.r in package a.

Restrictions/next steps:

- Support for ref head rules in the REPL is pretty poor so far. Anything that
  works does so rather accidentally. You should be able to work with policies
  that contain ref heads, but you cannot interactively define them.
  
  This is because before, we'd looked at REPL input like

      p.foo.bar = true

  and noticed that it cannot be a rule, so it's got to be a query. This is no
  longer the case with ref heads.

- Currently vars in Refs are only allowed in the last position. This is expected
 to change in the future.

- Also, for multi-value rules, we can not have a var at all -- so the following
  isn't supported yet:

      p.q.r[s] contains t if { ... }

-----

Most of the work happens when the RuleTree is derived from the ModuleTree -- in
the RuleTree, it doesn't matter if a rule was `p` in `package a.b.c` or `b.c.p`
in `package a`.

As such, the planner and wasm compiler hasn't seen that many adaptations:

- We're putting rules into the ruletree _including_ the var parts, so

  p.q.a = 1
  p.q.[x] = 2 { x := "b" }

  end up in two different leaves:

  p
  `-> q
       `-> a = 1
       `-> [x] = 2`

- When planing a ref, we're checking if a rule tree node's children have
  var keys, and plan "one level higher" accordingly:

  Both sets of rules, p.q.a and p.q[x] will be planned into one function
  (same as before); and accordingly return an object {"a": 1, "b": 2}

- When we don't have vars in the last ref part, we'll end up planning
  the rules separately. This will have an effect on the IR.

  p.q = 1
  p.r = 2

  Before, these would have been one function; now, it's two. As a result,
  in Wasm, some "object insertion" conflicts can become "var assignment
  conflicts", but that's in line with the now-new view of "multi-value"
  and "single-value" rules, not partial {set/obj} vs complete.
* planner: only check ref.GroundPrefix() for optimizations

In a previous commit, we've only mapped

    p.q.r[7]

as p.q.r;  and as such, also need to lookup the ref

    p.q.r[__local0__]

via p.q.r

(I think. Full disclosure: there might be edge cases here that are unaccounted
for, but right now, I'm aiming for making the existing tests green...)


New compiler stage:

In the compiler, we're having a new early rewriting step to ensure that the
RuleTree's keys are comparible. They're ast.Value, but some of them cause us
grief:

- ast.Object cannot be compared structurally; so

      _, ok := map[ast.Value]bool{ast.NewObject([2]*ast.Term{ast.StringTerm("foo"), ast.StringTerm("bar")}): true}[ast.NewObject([2]*ast.Term{ast.StringTerm("foo"), ast.StringTerm("bar")})]

  `ok` will never be true here.

- ast.Ref is a slice type, not hashable, so adding that to the RuleTree would
  cause a runtime panic:

      p[y.z] { y := input }

  is now rewritten to

    p[__local0__] { y := input; __local0__ := y.z }

This required moving the InitLocalVarGen stage up the chain, but as it's still
below ResolveRefs, we should be OK.

As a consequence, we've had to adapt `oracle` to cope with that rewriting:

1. The compiler rewrites rule head refs early because the rule tree expects
   only simple vars, no refs, in rule head refs. So `p[x.y]` becomes
   `p[local] { local = x.y }`
2. The oracle circles in on the node it's finding the definition for based
   on source location, and the logic for doing that depends on unaltered
   modules.

So here, (2.) is relaxed: the logic for building the lookup node stack can
now cope with generated statements that have been appended to the rule bodies.


There is a peculiarity about ref rules and extents:

See the added tests: having a ref rule implies that we get an empty object
in the full extent:

    package p
    foo.bar if false

makes the extent of data.p: {"foo": {}}

This is somewhat odd, but also follows from the behaviour we have right now
with empty modules:

    package p.foo
    bar if false

this also gives data.p the extent {"foo": {}}.

This could be worked around by recording, in the rule tree, when a node was
added because it's an intermediary with no values, but only children.

Signed-off-by: Stephan Renatus <stephan.renatus@gmail.com>

---
## [TorchTheDragon/RiftJumpers-NewBuild](https://github.com/TorchTheDragon/RiftJumpers-NewBuild)@[e08d8fdd9a...](https://github.com/TorchTheDragon/RiftJumpers-NewBuild/commit/e08d8fdd9a374f6b88282e2bec76dc3ad5c87083)
#### Monday 2022-10-31 06:50:02 by TorchTheDragon

Umm... dis a lot

Ok, like holy shit, I didn't know I changed this much. I decided to look back at what I had changed compared to the new version and this is what I see... yeah... just look through it I guess

---
## [UltraFormula1/Platformer](https://github.com/UltraFormula1/Platformer)@[fba280cc91...](https://github.com/UltraFormula1/Platformer/commit/fba280cc91f5f02e040a401b3f5360ad89ab46d2)
#### Monday 2022-10-31 08:09:04 by UltraFormula1

Final Day (For real)

I am not crazy! I know he swapped those numbers! I knew it was 1216. One after Magna Carta. As if I could ever make such a mistake. Never. Never! I just – I just couldn't prove it. He – he covered his tracks, he got that idiot at the copy shop to lie for him. You think this is something? You think this is bad? This? This chicanery? He's done worse. That billboard! Are you telling me that a man just happens to fall like that? No! He orchestrated it! Jimmy! He defecated through a sunroof! And I saved him! And I shouldn't have. I took him into my own firm! What was I thinking? He'll never change. He'll never change! Ever since he was 9, always the same! Couldn't keep his hands out of the cash drawer! But not our Jimmy! Couldn't be precious Jimmy! Stealing them blind! And he gets to be a lawyer!? What a sick joke! I should've stopped him when I had the chance! And you – you have to stop him! You-

---
## [CivilizationVIBetterBalancedGame/BetterBalancedGame](https://github.com/CivilizationVIBetterBalancedGame/BetterBalancedGame)@[ef82550580...](https://github.com/CivilizationVIBetterBalancedGame/BetterBalancedGame/commit/ef825505806807506727df20edc5038981af35ee)
#### Monday 2022-10-31 09:13:37 by ZhenjaMax

English update (#62)

* 5.1.2 Beta English

New lines for 5.1.2 patch:
- Hungary UU (Huszar) - tag LOC_ABILITY_HUSZAIR_COMBAT_PREVIEW for combat stregth from City-states; in contains only one word (see file), you can write nothing there or change this word so it fits your language syntax and style! Now it looks like "+2 from Armagh", but you can change (for example) to "+2 from City-State Armagh");
- Sumerian UU - added new tag LOC_ABILITY_WAR_CART_COMBAT_STRENGTH_VS_BARBS_COMBAT_DESCRIPTION_BBG, requires for short correct combat preview (now that long desription about ignoring anti-cav for unit ability list only);
- Heavy cavalry promotion name - visual bug fix;
- Ibrahim T0, L1, R1 promotions - clarification from bug-report (some work for Ottoman only, some for friends too);
>
Edited lines for 5.1.2 patch:
- France UI - 2 => 1 base culture;
- Norway leader ability - HS gains adjacency from coast and lakes (not just coast);
- Spain UI - clarification for 1-7 tiles and 8+ tiles;
- Ibrahim R2 promotion - clarification from bug-report;
- Nan-Madol City-state bonus - for specialty districts only;

New other lines:
- Hungary civilization ability - district icon;
- Classical Republic legacy - district icon;
- Digital Democracy bonus - district icon;
>
Edited other lines:
- Australian UI - text strcture;
- Aztec civilization ability - district icon;
- Babylon leader ability - district icon;
- China UI - text strcture;
- Colombia UI - text strcture;
- Cree UI - text structure;
- Dutch UI - text strcture;
- Egypt UI - text structure;
- Ethiopia UI - text structure;
- France UI - text structure;
- Germany civilization ability - district icon;
- India UI - text structure;
- Indonesia UI - text structure;
- Japan civilization ability - district icon;
- Norway leader ability - re-formatted English text;
- Nubia leader ability - district icon;
- Nubia UI - text structure;
- Persia UI - text structure;
- Phoenicia leader ability - district icon;
- Portugal UU special UI (Feirotia) - text structure;
- Scotland UI - text strcture;
- Scythia UI - text structure;
- Spain civilization ability - district icon;
- Spain UI - text structure;
- Sumerian UI - text structure; clarification for faith from adjacency;
>
- Reyna L3 promotion - district icon;
- Liang R2 promotion - district icon;
- Moksha T0 promotion - simplify +15%;
- Moksha L2 promotion - district icon;
>
- Tupac Amaru Great General ability - district icon;
- Great Merchants ability - remove sentence for "+1 capacity" because game already shows that line from Great Merchant traits.

* update Arabia lines

- Arabia leader ability - religion icon;
- Arabia leader ability - adjacency lines for Campus and Holy Site districts.

* fix English syntax errors

- UI - from => for (except Tourism);
- UI - additional "the";
- China UI - Tourism note;
- many other changes ("built", "is reached", etc.);
- Nubia leader ability - "increasing";
- Spain UI - "more", "less";

- skipped: UI - "increasing to" instead of "up to".

* Egypt UI english text

- missed "the".

* English text UI descriptions fix

- UI - "up to" to "increasing to".

* English Armagh UI text

+1 Housing for XP2, additional +1 Housing with the Colonialism civic

* Hungary UI tooltip comment

- commentary line clarification

---
## [dreyfus92/docs](https://github.com/dreyfus92/docs)@[6b97aae394...](https://github.com/dreyfus92/docs/commit/6b97aae394f0cd6dff5b73809d0d1d248c62ee91)
#### Monday 2022-10-31 10:35:41 by Vinicius Victorino

Fix pronouns in Portuguese for Katie Sylor-Miller (#1955)

As you can see by her twitter account https://twitter.com/ksylor, she identifies as she/her. In Portuguese we have different names for male and female job descriptions, in this case arquitetO (male) and arquitetA (female).

Co-authored-by: Yan Thomas <61414485+Yan-Thomas@users.noreply.github.com>

---
## [Phytolizer/Obsidian](https://github.com/Phytolizer/Obsidian)@[9863d33d15...](https://github.com/Phytolizer/Obsidian/commit/9863d33d15eb399c20c6d086c45be24a7d4ad6bf)
#### Monday 2022-10-31 12:01:03 by Demiosis

Modified slightly the organ T hall

To help impatient kids, peoples who can't read a map and zoomers understand it better! Holy shit I laughed quite hard on this one..

---
## [reema-alsabt/reema-alsabt](https://github.com/reema-alsabt/reema-alsabt)@[46236d5cfc...](https://github.com/reema-alsabt/reema-alsabt/commit/46236d5cfc16d187e72872339e7e5a4a0742b70a)
#### Monday 2022-10-31 12:23:18 by reema-alsabt

Add files via upload

Twitter and other social networking sites are being used increasingly to spread hate speech. Several recent studies have also shown that the expression of hate speech leads to hate crimes such as Islamophobic attacks. Due to the increasing popularity of social media sites and the negative societal effects of hateful speech, it is crucial to develop automated tools for detecting hateful speech. Our goal in this research is to develop a natural language processing model for detecting hate speech on Twitter. Our review of previous studies indicates that the BERT model consistently results in effective measures. We will therefore be using the BERT base model as our NLP method to detect hateful speech from hugging face transformers along with the BERTokenizer to preprocess the data. This study will make use of the Kaggle dataset, which includes 25,296 tweets classified as offensive, hateful, or neither. We also utilized the Python language, TensorFlow, and NumPy. Therefore, our primary objective is to attain high levels of accuracy and reduce error rates. Meanwhile, the unbalanced data was rectified by obtaining the tweets that were strongly classified and categorized by CrowdFlower workers, resulting in 17,481 remaining tweets. Our analysis revealed that after filtering out the weakly classified tweets, our model achieved an overall accuracy of 98.09%, surpassing the BERT benchmark models and the unfiltered Kaggle dataset.

---
## [ehunt34/neochromium-ehunt34](https://github.com/ehunt34/neochromium-ehunt34)@[0c8bfe985c...](https://github.com/ehunt34/neochromium-ehunt34/commit/0c8bfe985cc6dcd8cc862989899753b2b52bbb8a)
#### Monday 2022-10-31 12:53:24 by ehunt34

store unenroll script

Also fuck you 3kh0 I still have your fucking script. Hope you're fucking happy.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[15bb688a33...](https://github.com/treckstar/yolo-octo-hipster/commit/15bb688a33ba84dcfff2e08192e46e8e51b75be4)
#### Monday 2022-10-31 14:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [xclaesse/wrapdb](https://github.com/xclaesse/wrapdb)@[7e69bfce97...](https://github.com/xclaesse/wrapdb/commit/7e69bfce97df6ef5d70e556ca4059e8f5f38af3f)
#### Monday 2022-10-31 15:05:09 by Eli Schwartz

openjp2: Use wrap fallbacks instead of thirdparty

The thirdparty directory provided by upstream contains (old) versions of
projects we already have in the wrapdb. There is zero value in
permitting or encouraging this usage.

Also, the actual dependency lookups suck. e.g. the zlib logic, even when
probing for system versions, tries to find a pkg-config dependency, then
probes for 3 different library names, falls back to subproject() on a
subproject that doesn't exist in the wrap itself, with incorrect usage
of found(), and finally subdirs into the custom copy.

Half of this doesn't work, and all of it is redundant since meson
includes its own robust finder logic that does library probing correctly
in a cross-platform manner under the name... "zlib", just like the
pkg-config dependency.

Furthermore, ***upstream agrees with us***. To quote their own README:

```
This directory contains 3rd party libs (PNG, ZLIB)...

They are convinient copy of code from people outside of the OpenJPEG community.
They are solely provided for ease of build of OpenJPEG on system where those
3rd party libs are not easily accessible (typically non-UNIX).

The OpenJPEG does not recommend using those 3rd party libs over your system
installed libs. The OpenJPEG does not even guarantee that those libraries will
work for you.
```

This is so un-recommended by literally everyone everywhere, that
continuing to provide broken versions here is an intolerable thing.

What upstream wanted, really, was a build system that supported meson wraps.
Then they could have never included a thirdparty directory, but provided
subprojects/*.wrap "solely for ease of build on systems where those libs
are not easily accessible". It's a match made in heaven!

...

Also while we are at it, ditch the commented out copy of astyle, which
was built as an executable because a manually run maintainer shellscript
would execute the forked "openjpstyle" for you. It's totally unneeded by
the wrap, and even if it was considered interesting, it must go through
the standard wrap review && release process.

Move the remaining simple dependency() calls to the subdir that needs
them, which is already guarded by a project option.

Co-authored-by: Xavier Claessens <xavier.claessens@collabora.com>

---
## [Hatterhat/tgstation](https://github.com/Hatterhat/tgstation)@[db83f6498d...](https://github.com/Hatterhat/tgstation/commit/db83f6498da37ecd25588ea3f7024409d2f3f117)
#### Monday 2022-10-31 17:00:41 by vincentiusvin

Simplifies SM damage calculation, tweaks the numbers. (#70347)


About The Pull Request

We apply the damage hardcap individually now, split off the old flat 1.8 into individual caps for heat, moles, and power.

Set it to 1.5 for heat, 1 for mole and 1 for power. This means for most delams it'll be a tad slower! But its possible to make SM delam nearly twice as fast if you combine all 3. (3.5). Be pretty hard tho.

Set the heat healing to -1 so you can counteract one factor at most (except heat since you'll never get both heat healing and heat damage at the same time anyway).

I'm not hell bent on any of the numbers, just picked round even ones and ones that i think will make sense. If you want them changed lmk.

Got rid of the cascade mole and power multipliers since there's probably like three people that are aware that it even exists. Ideally we just add another entry to the CIMS but its already pretty crowded. Figured nobody is gonna miss it anyway? Sorry ghil.

Got rid of the moles multiplier thing since its nicer to keep the temp damage fully based on temp damage instead of adding another multiplier. I just applied the .25 to the damage flatly, meaning it slows down delams again!

And some space exposure stuff: #70347 (comment)
Why It's Good For The Game

Hardcap: Discrete, less randomly interconnected factors are easier to present and remember. The calculation procs are also made to be additive so we had to hack a bit and do some rescaling to accomodate the old behavior in my original PR #69240. Can remove the hack if this pr goes through.

Cascade and mole multiplier: The rest are just getting rid of underutilized factors so we have a cleaner behavior to maintain, present, and understand. (In a perfect world modifiers that aren't visible to the players shouldn't have been merged in the first place smh smh)
Changelog

🆑
fix: Fixed sm space exposure damage going through walls
del: got rid of the molar multiplier for sm heating damage. It will now only impact molar damage and temp limit. We apply the lowest value directly so this slows down sm delams a tiny bit.
del: got rid of cascades making sm delam at 450 moles and 1250 mev. It delams normally now.
balance: Applied the sm damage hardcap of 1.8 individually to heat (1.5), moles (1), power (1). Meaning most sm delams are slower now, but the really bad ones can be faster.
balance: Halved sm temp healing across the board. Temp limits are still the same though so you shouldn't notice it that much.
balance: Halved SM power damage across the board.
balance: Changed sm space exposure damage to just check for the current tile and adjacent atmos connected tiles.
/🆑

---
## [avar/git](https://github.com/avar/git)@[ee9ad433ab...](https://github.com/avar/git/commit/ee9ad433ab5df6335525f366b9ddbf12da135361)
#### Monday 2022-10-31 17:39:13 by Ævar Arnfjörð Bjarmason

cocci: make "coccicheck" rule incremental

Optimize the very slow "coccicheck" target to take advantage of
incremental rebuilding, and fix outstanding dependency problems with
the existing rule.

The rule is now faster both on the initial run as we can make better
use of GNU make's parallelism than the old ad-hoc combination of
make's parallelism combined with $(SPATCH_BATCH_SIZE) and/or the
"--jobs" argument to "spatch(1)".

It also makes us *much* faster when incrementally building, it's now
viable to "make coccicheck" as topic branches are merged down.

The rule didn't use FORCE (or its equivalents) before, so a:

	make coccicheck
	make coccicheck

Would report nothing to do on the second iteration. But all of our
patch output depended on all $(COCCI_SOURCES) files, therefore e.g.:

    make -W grep.c coccicheck

Would do a full re-run, i.e. a a change in a single file would force
us to do a full re-run.

The reason for this (not the initial rationale, but my analysis) is:

* Since we create a single "*.cocci.patch+" we don't know where to
  pick up where we left off, or how to incrementally merge e.g. a
  "grep.c" change with an existing *.cocci.patch.

* We've been carrying forward the dependency on the *.c files since
  63f0a758a06 (add coccicheck make target, 2016-09-15) the rule was
  initially added as a sort of poor man's dependency discovery.

  As we don't include other *.c files depending on other *.c files
  has always been broken, as could be trivially demonstrated
  e.g. with:

       make coccicheck
       make -W strbuf.h coccicheck

  However, depending on the corresponding *.c files has been doing
  something, namely that *if* an API change modified both *.c and *.h
  files we'd catch the change to the *.h we care about via the *.c
  being changed.

  For API changes that happened only via *.h files we'd do the wrong
  thing before this change, but e.g. for function additions (not
  "static inline" ones) catch the *.h change by proxy.

Now we'll instead:

 * Create a <RULE>/<FILE> pair in the .build directory, E.g. for
   swap.cocci and grep.c we'll create
   .build/contrib/coccinelle/swap.cocci.patch/grep.c.

   That file is the diff we'll apply for that <RULE>-<FILE>
   combination, if there's no changes to me made (the common case)
   it'll be an empty file.

 * Our generated *.patch
   file (e.g. contrib/coccinelle/swap.cocci.patch) is now a simple "cat
   $^" of all of all of the <RULE>/<FILE> files for a given <RULE>.

   In the case discussed above of "grep.c" being changed we'll do the
   full "cat" every time, so they resulting *.cocci.patch will always
   be correct and up-to-date, even if it's "incrementally updated".

   See 1cc0425a27c (Makefile: have "make pot" not "reset --hard",
   2022-05-26) for another recent rule that used that technique.

As before we'll:

 * End up generating a contrib/coccinelle/swap.cocci.patch, if we
   "fail" by creating a non-empty patch we'll still exit with a zero
   exit code.

   Arguably we should move to a more Makefile-native way of doing
   this, i.e. fail early, and if we want all of the "failed" changes
   we can use "make -k", but as the current
   "ci/run-static-analysis.sh" expects us to behave this way let's
   keep the existing behavior of exhaustively discovering all cocci
   changes, and only failing if spatch itself errors out.

Further implementation details & notes:

 * Before this change running "make coccicheck" would by default end
   up pegging just one CPU at the very end for a while, usually as
   we'd finish whichever *.cocci rule was the most expensive.

   This could be mitigated by combining "make -jN" with
   SPATCH_BATCH_SIZE, see 960154b9c17 (coccicheck: optionally batch
   spatch invocations, 2019-05-06).

   There will be cases where getting rid of "SPATCH_BATCH_SIZE" makes
   things worse, but a from-scratch "make coccicheck" with the default
   of SPATCH_BATCH_SIZE=1 (and tweaking it doesn't make a difference)
   is faster (~3m36s v.s. ~3m56s) with this approach, as we can feed
   the CPU more work in a less staggered way.

 * Getting rid of "SPATCH_BATCH_SIZE" particularly helps in cases
   where the default of 1 yields parallelism under "make coccicheck",
   but then running e.g.:

       make -W contrib/coccinelle/swap.cocci coccicheck

   I.e. before that would use only one CPU core, until the user
   remembered to adjust "SPATCH_BATCH_SIZE" differently than the
   setting that makes sense when doing a non-incremental run of "make
   coccicheck".

 * Before the "make coccicheck" rule would have to clean
   "contrib/coccinelle/*.cocci.patch*", since we'd create "*+" and
   "*.log" files there. Now those are created in
   .build/contrib/coccinelle/, which is covered by the "cocciclean" rule
   already.

Outstanding issues & future work:

 * We could get rid of "--all-includes" in favor of manually
   specifying a list of includes to give to "spatch(1)".

   As noted upthread of [1] a naïve removal of "--all-includes" will
   result in broken *.cocci patches, but if we know the exhaustive
   list of includes via COMPUTE_HEADER_DEPENDENCIES we don't need to
   re-scan for them, we could grab the headers to include from the
   .depend.d/<file>.o.d and supply them with the "--include" option to
   spatch(1).q

1. https://lore.kernel.org/git/87ft18tcog.fsf@evledraar.gmail.com/

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [sorbet/sorbet](https://github.com/sorbet/sorbet)@[9d448f0735...](https://github.com/sorbet/sorbet/commit/9d448f07352030587f75c0fa09acecf663cc4772)
#### Monday 2022-10-31 18:24:33 by Jake Zimmerman

Remove call to `dealias` in namer

We don't allow constant aliases in class scopes anyways. Not sure why
we're trying to dealias here.

If I had to guess, this was a remant of some hacks we had way long ago
to support this pattern, which was common in Stripe's codebase:

    class Chalk::ODM::Model
    end

    M = Chalk::ODM::Model

    class M::A
    end

But this pattern is already rejected by Sorbet, and has been for as long
as I can remember, so likely when that change was finally made, someone
forgot to delete this `dealias` call.

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[d616f34b0b...](https://github.com/cockroachdb/cockroach/commit/d616f34b0bd7c488412827e754c08ea0cce92546)
#### Monday 2022-10-31 19:17:22 by craig[bot]

Merge #90875 #90953 #91008

90875: sqlliveness/slstorage: rework deletion loop to avoid contention r=ajwerner a=ajwerner

#### sqlliveness/slstorage: rework deletion loop to avoid contention

The periodic loop to delete abandoned records used to to a potentially
long-running transaction to discover and delete expired sessions. This
could lead to live-lock starvation in some scenarios. Consider a case
whereby there are live sessions which are heart-beating their records
successfully. In the meantime, local sessions heart-beat regularly and
stay alive. Those sessions are in the read set of the deletion loop but
not in the write set. Imagine now that the deletion loop gets pushed and
has to refresh. It will fail and need to restart, but it will hold its
locks. This livelock can persist forever if the rate of heartbeats of
live sessions has a period shorter than the latency of the deletion
loop's operations. In a cluster with 100 nodes and a heartbeat interval
of 5s, we'd expect a heartbeat every 50ms. If the latency between the
deletion loop and leaseholder is, say, 50ms, we're in big trouble because
just the scan phase will take at least that long.

This change avoids the large transaction altogether. It decouples candidate
discover from removal. The usual process by which rows are removed is able
to avoid intents altogether and use 1PC. In this way, starvation, or even
waiting on locks should be fully eliminated.

#### sqlliveness/slstorage: reduce the garbage collection loop frequency

Nothing ever scans the sqlliveness table. We don't expect it to grow very large
very rapidly. Also, we run this loop on every node. Running it every 20s never
made much sense. This commit changes it to run hourly.

#### sqlliveness/slstorage: use 1PC to avoid intents

There was no reason for these transactions to lay down intents. They can always
commit with 1PC. Use the API to achieve that.

Epic: None

Release note (bug fix): In large, multi-region clusters, it was possible for
the leasing mechanism used for jobs to get caught in a live-lock scenario
whereby jobs could not be adopted. This bug has been resolved.

90953: storage: fix point synthesis activation during reverse scans r=erikgrinaker a=erikgrinaker

This patch fixes a bug where `pointSynthesizingIter` could appear to have skipped a synthetic point tombstone in the reverse direction when enabled dynamically by `pebbleMVCCScanner`.

Consider the following case:

```
REAL DATASET          SYNTHETIC DATASET
3       [b3]          3      [b3]
2    a2               2   a2
1    [---)            1   x
     a   b                a   b
```

Recall that `pebbleMVCCScanner` only enables `pointSynthesizingIter` when it encounters a range key. In the case above, during a reverse scan, the `[a-b)`@1`` range key will first become visible to `pebbleMVCCScanner` when it lands on `a@2`, so it enabled point synthesis positioned at the `a@2` point key. Notice how the iterator has now skipped over the synthetic point tombstone `a@1`.

This is particularly problematic when combined with `pebbleMVCCScanner` peeking, which assumes that following a `iterPeekPrev()` call, an `iterNext()` call can step the parent iterator forward once to get back to the original position.  With the above bug, that is no longer true, as it instead lands on the synthetic point tombstone which was skipped during reverse iteration. During intent processing for `b@3`, such an `iterNext()` call is expected to land on the intent's provisional value at `b@3`, but it instead lands on the intent itself at `b@0`. This in turn caused a value checksum or decoding failure, where it was expecting the current key to be `b@3`, but the actual key was `b@0`.

This patch fixes the bug by keeping track of the direction of the previous positioning operation in `pebbleMVCCScanner`, and then repositioning the `pointSynthesizingIter` as appropriate during dynamic activation in the reverse direction. This doesn't have a significant effect on performance (in particular, the point get path is never in reverse).

Several alternative approaches were attempted but abandoned:

* Don't synthesize points at a range key's start bound. While compelling for a range of reasons (complexity, performance, etc) this has two flaws: on a bare range key, the iterator still needs to know which direction to skip in, and we also need to know the timestamps of bare range keys for `FailOnMoreRecent` handling.

* Only synthesize a single point at a range key's start bound. This would solve the problem at hand, but has rather strange semantics.

Longer-term, it may be better to merge range key logic into `pebbleMVCCScanner` itself -- `pointSynthesizingIter` was intended to reduce complexity, but it's not clear that the overall complexity is actually reduced.

Resolves #90642.

Release note: None

91008: colexecdisk: increase a test tolerance r=ajwerner a=ajwerner

Despite `16601 runs so far, 0 failures, over 8m45s` at the current 2.2, the test did fail once [here](https://teamcity.cockroachdb.com/buildConfiguration/Cockroach_UnitTests_BazelUnitTests/7237709?showRootCauses=false&expandBuildChangesSection=true&expandBuildProblemsSection=true&expandBuildDeploymentsSection=true&expandBuildTestsSection=true)


Epic: None

Release note: None

Co-authored-by: Andrew Werner <awerner32@gmail.com>
Co-authored-by: Erik Grinaker <grinaker@cockroachlabs.com>

---
## [opentensor/bittensor](https://github.com/opentensor/bittensor)@[1b7241f31f...](https://github.com/opentensor/bittensor/commit/1b7241f31f86e0ee244a407c9ba91075a9ec1535)
#### Monday 2022-10-31 19:37:32 by salvivona

holy shit that was fucked, finally can load alot of hashes per second without syncio shitting the bed

---
## [Zevotech/Shiptest](https://github.com/Zevotech/Shiptest)@[3efa9b5382...](https://github.com/Zevotech/Shiptest/commit/3efa9b538241ffef48ddf1fe102feb589e88dff0)
#### Monday 2022-10-31 19:57:20 by Zevotech

undoes a fuckup on a ruin (#1578)

* undoes a fuckup on a ruin
<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull request process. -->

## About The Pull Request
sets light range to 2 on the ruin areas of beach_colony.dmm
<!-- Describe The Pull Request. Please be sure every change is documented or this can delay review and even discourage maintainers from merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the brackets) if you have tested your changes and this is ready for review. Leave unticked if you have yet to test your changes and this is not ready for review. -->

- [ ] I affirm that I have tested all of my proposed changes and that any issues found during tested have been addressed.

## Why It's Good For The Game
the ruin is no longer pitch fucking dark in the middle of a daylit planet (hopefully)
<!-- Please add a short description of why you think these changes would benefit the game. If you can't justify it in words, it might not be worth adding. -->

## Changelog

:cl:
fix: changes light range to 2 on the areas of beach_colony
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put your name to the right of the first :cl: if you want to overwrite your GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the icon ingame) and delete the unneeded ones. Despite some of the tags, changelogs should generally represent how a player might be affected by the changes rather than a summary of the PR's contents. -->

* im stupid

---
## [youniversityupc/app](https://github.com/youniversityupc/app)@[0e99947eb8...](https://github.com/youniversityupc/app/commit/0e99947eb8b84b03d397891a93c2d04672a8d29f)
#### Monday 2022-10-31 20:10:34 by Diego Albitres

refactor: fixed AppBar tab rendering

OMG, this is finally working. I hate myself.

---
## [kenmays/mesa](https://github.com/kenmays/mesa)@[3a9cdd780d...](https://github.com/kenmays/mesa/commit/3a9cdd780de28deeda45600fb5b8b134d91d17f2)
#### Monday 2022-10-31 20:16:50 by Alyssa Rosenzweig

panfrost/ci: Disable trace-based testing

Trace-based testing has not worked for Panfrost. It was a neat
experiment, and I'm glad we tried it, but the results have been mostly
negative for the driver. Disable the trace-based tests.

For testing that specific API features work correctly, we run the
conformance tests (dEQP), which are thorough for OpenGL ES. For big GL
features, we run Piglit, and if there are big GL features that we are
not testing adequately, we should extend Piglit for these. For
fine-grained driver correctness, we are already covered.

Where trace-based testing can fit in is as a smoke test, ensuring that
the overall rendering of complex scenes does not regress. In principle,
that's a lovely idea, but the current implementation has not worked out
for Panfrost thus far. The crux of the issue is that the trace based
tests are based on checksums, not fuzzy-compared reference images. That
requires updating checksums any time rendering changes. However, a
rendering change to a trace is NOT a regression. The behaviour of OpenGL
is specified very loosely. For a given trace, there are many different
valid checksums. That means that correct changes to core code frequently
fail CI after running through the rest of CI, only because a checksum
changed in a still correct way. That's a pain to deal with, exacerbated
by rebase pains, and provides negative value to the project. Some recent
examples of this I've hit in the past two weeks alone:

   panfrost: Enable rendering to 16-bit and 32-bit
   4b49241f7d7 ("panfrost: Use proper formats for pntc varying")
   ac2964dfbd1 ("nir: Be smarter fusing ffma")

The last example were virgl traces, but were especially bad: due to a
rebase fail, I had to update traces /twice/, wasting two full runs of
pre-merge CI across *all* hardware. This was extremely wasteful.

The value of trace-based testing is as a smoke test to check that traces
still render correctly. That is useful, but it turns out that checksums
are the wrong way to go about it. A better implementation would be
storing only a single reference image from a software rasterizer per
trace. No driver-specific references would be stored. That reference
image must never change, provided the trace never changes. CI would then
check rendered results against that image with tolerant fuzzy
comparisons. That tolerance matches with the fuzzy comparison that the
human eye would do when investigating a checksum change anyway. Yes, the
image comparison JavaScript will now report that
0 pixels changed within the tolerance, but there's nothing a human eye
can do with that information other than an error prone copypaste of new
checksums back in the yaml file and kicking it back to CI, itself a
waste of time.

Finally, in the time we've had trace-based testing alongside the
conformance tests, I cannot remember a single actual regression in one
of my commits the trace jobs have identified that the conformance tests
have not also identified. By contrast, the conformance test coverage has
prevented the merge of a number of actual regressions, with very few
flakes or xfail changes, and I am grateful we have that coverage. That
means the value added from the trace jobs is close to zero, while the
above checksum issues means that the cost is tremendous, even ignoring
the physical cost of the extra CI jobs.

If you work on trace-based testing and would like to understand how it
could adapted to be useful for Panfrost, see my recommendations above.
If you work on CI in general and would like to improve Panfrost's CI
coverage, what we need right now is not trace-based testing, it's
GLES3.1 conformance runs on MediaTek MT8192 or MT8195. That hardware is
already in the Collabora LAVA lab, but it's not being used for Mesa CI
as the required kernel patches haven't made their way to mainline yet
and nobody has cherry-picked them to the gfx-ci kernel. If you are a
Collaboran and interested in improving Panfrost CI, please ping
AngeloGioacchino for information on which specific patches need to be
backported or cherry-picked to our gfx-ci kernel. Thank you.

Signed-off-by: Alyssa Rosenzweig <alyssa@collabora.com>
Acked-by: Jason Ekstrand <jason.ekstrand@collabora.com>
Part-of: <https://gitlab.freedesktop.org/mesa/mesa/-/merge_requests/19358>

---
## [Fikou/tgstation](https://github.com/Fikou/tgstation)@[3582aa77bb...](https://github.com/Fikou/tgstation/commit/3582aa77bb68d43c1ebbff9e06226bf3089cb07a)
#### Monday 2022-10-31 21:15:35 by LemonInTheDark

Slightly optimizes reagent splashing (#70709)

* Slightly optimizes reagent splashing

Ok so like, before, splashing a reagent performed a rudimentary
floodfill based off atmos connectivity.

This was really slow, because it did it using orange(), and repeated
orange()s to cut out JUST the rim, because we
needed to ensure things were ordered.

I've changed this to use floodfill. I've also moved some code that was
in a second loop into the first one, and replaced a repeated in check
with a single use of &

This is still not optimal for large ranges, because we filter by connectivity first
and THEN view, but it's faster for smaller ones.

BTW I'm also capping the max spread range at 40x40 tiles. If you want
more then 1600 you can rot in hell.

This takes the (uncapped range) cost of deconstructing a highcap tank
from 40 seconds to 0.16.

I hate this codebase

* god damn it

Co-authored-by: san7890 <the@san7890.com>

* whoops that's redundant

Co-authored-by: san7890 <the@san7890.com>

---
## [McLogicmaster69/Ciphers](https://github.com/McLogicmaster69/Ciphers)@[b32b778d6e...](https://github.com/McLogicmaster69/Ciphers/commit/b32b778d6e9914046dc6a44efe4c4f0bc49e839a)
#### Monday 2022-10-31 21:33:31 by Luftwaffle129

I luv bacon

Now baby come on (calling upon her baby, four words like beats in her heart)
Don't claim that love you never let me feel (Atmosphere and calls upons sensory imagery)
I shoulda known (She should of known)
'Cause you brought nothin' real (slang, shows how her english is broken just like her heart)
C'mon be a man about it you won't die (He is probably about to die and women being “femenist” are telling men to “be a man”)
I ain't got no more tears to cry and I can't take this no more (She has been crying for a while, sensory imagery)
You now I gotta let you go and you know (Sad atmosphere)
I'm outta love set me free and let me out this misery (She is outta love and needs to be set free)
Just show me the way to get my life again (i give up)
'Cause you can't handle me
Said I'm outta love can't you see
Baby that you gotta set me free, I'm outta love
Said how many times
Have I tried to turn this love around
But every time you just let me down
C'mon be a man about it you'll survive
I'm sure that you can work this out all right
Tell me yesterday did you know
I'd be the one to let you go and you know
I'm outta love set me free and let me out this misery
Show me the way to get my life again
'Cause you can't handle me
Said I'm outta love can't you see
Baby that you gotta set me free, I'm outta love
Let me get over you
The way you gotten over me too
Seems like my time has come and now I'm movin' on
I'll be stronger
I'm outta love set me free and let me out this misery
Show me the way to get my life again
'Cause you can't handle me
I'm outta love set me free and let me out this misery
Show me the way to get my life again
'Cause you can't handle me
Said I'm outta love can't you see
Baby that you gotta set me free, I'm outta love
I'm outta love set me free and let me out this misery
Show me the way to get my life again
'Cause you can't handle me
I'm outta love set me free

---
## [smxi/inxi](https://github.com/smxi/inxi)@[029a331a06...](https://github.com/smxi/inxi/commit/029a331a06d5ffc737d75a87315e50d6cb3d80e1)
#### Monday 2022-10-31 22:48:26 by Harald Hope

This release fixes another very long standing bug, which I was not sure was an
inxi or a Konversation bug, which made tracking it down very difficult. Special
thanks to argonel of Konversation for helping solve this problem, or at least,
for directing my attention towards the likely cause area, and away from wrong
ideas. The bug was that inxi simply did not run in Konversation, it would exit
with error when run with /cmd or /inxi via symbolic links.

This may not seem like a huge deal to many of you, but the actual history of
inxi was directly linked to user support in mainly Konversation, so this feature
not working I have alwyas found extremely annoying, but I could never figure out
why it wasn't workiing, and didn't really know where to start until Argonel
helped narrow it down to a specific Konversation function in inxi. At which
point tracking down the real bug was fairly easy. Since testing in IRC is always
a key test point for inxi features and releases, not working in my main GUI IRC
client forced me to use CLI clients like irssi, via /exec -o inxi.

There was a secondary cause of failure, which was missing a key qdbus package,
which made figuring this one out a two step process.

So inxi is once again working in all areas, with no known significant failure
areas beyond known issues that have no current solution, or which I don't feel
like doing.

But possibly more important, a goal I have had for a while now of doing long
needed code refactors, bug fixes, without huge new code blocks or features
adding new future fixes and bugs, has been slowly happening.

This was quite important, because inxi's codebase and logic is so complex and
large now that at some point, it required rest and cleanup and corrections,
without continuously adding new code and logic, which would then trigger new
fixes and bugs. In other words, the code is taking a long needed, and well
deserved, breather, to recover after huge increases in the overall LOC and
feature sets.

--------------------------------------------------------------------------------
KNOWN ISSUES:

1. No known way to detect that the system might be Wayland for the Graphics:..
API: fixes, unless Xwayland is installed if the wayland protocol detections
failed, which they often do in console. Not practical to look for all compositor
variants on system to determine if it could be Wayland if not X or Xvesa, so
that one will just be what it is, which is fine, definitely better than it was
before. Note this is only an issue if in Console, no Display. Note that if inxi
is run as root, Wayland data also usually fails, even in Display.

--------------------------------------------------------------------------------
BUGS:

1. Another corner case monitor position issue, applied fallback primary monitor
rule when a primary monitor had already been located. This is corrected via a
graphics global $b_primary which once set will disable this fallback feature.
Objectively, the fallback feature should just be removed. The test is if that
monitor is not primary, and if position is 0x0, then assume primary, without
verifying no primary had been located yet.

2. A super old bug, in current konversation, was failing to trip the konvi
detections, which then resulted in not stripping off the first two args in
@ARGV, which then resulted in bad args being passed to inxi on konvi start,
which then resulted in silent failing. Many thanks to argonel of #konversation
for the patience to help me figure out what was going on with this bug. He's
been a Konversation developer probably longer than I've been doing inxi.

Cause was very tricky and subtle, the ps aux path for konvi had changed
slightly, not the path, but the pattern, it used to be:

konversation -session [sessin id]
but it's changed to:
konversation -qwindowtitle Konversation
or just plain:
konversation as line ending.

This led to failure to find konvi running, which then made the konvi ids fail.

Also, this would not work if the qdbus-qt5 package was not installed, or other
distros might have that packaged differently. Because of these dual causes, I
was simply unable to figure out what was going on for many years. I suspect this
stopped working with KDE 5/QT 5, but I'm not sure.

3. Used wrong key names for some ZFS tests and fallbacks, those could have led
to failures though very difficult to test and verify this. Also see fix 5, which
of course also looks like a bug, acts like one, but was actually due to a new
use of /dev/disk/by-partuuid for ZFS components in Ubuntu which inxi had not
seen before.

--------------------------------------------------------------------------------
FIXES:

1. Alternate ps IDs for appimage detection (try appimagelauncher), alternate
paths for possible appimage storage locations (also try ~/.appimage/*). File
names might be *.appimage or *.AppImage, probably other variants too.

2. Going along with Change 1, made tests more granular for missing graphics API
type data. Also updated messages to be more correct and clear, in and out of
display. This corrects an issue I'd seen but never resolved, which was on
headless systems showing this message:

Message: GL data unavailable in console. Try -G --display

Now the tests are far more granular, and only show that if glxinfo is installed,
and also shows specific messages if glxinfo not installed, but X/Xorg present,
or, for Wayland, if Xwayland present. These all get their own specific messages
now, and generally will also show which API is being used, or API: N/A if
nothing is detected, as in the case of a headless system with no X, Wayland,
etc.

3. Github issue #275 on of all things Microsoft WSL environment, has a small
glitch with undefined display hz, but otherwise inxi seems to work in that
environment, albeit missing many data types!

4. Made tests for konversation more robust, including test for
$ENV{'PYTHONPATH'} containing konversation in path, which I believe will work
for all new Konversations (KDE 5 and newer), and be much faster. The previous
tests are now more robust and less prone to failure, and only activate when
PYTHONPATH is not present with konversation string present as well.

5. Fix for ZFS using /dev/disk/by-partuuid for partition id in zfs,
which can lead to wrong usable disk total size report, along with failure
to show components. Thanks delanym, issue #276 for reporting this problem, which
also exposed some harder to trigger bugs in ZFS (Bug 3).

6. Exposed by issue #276, case where line was wrapping value when value was too
short visually to value: used: 34.4 GiB (4.5%) due to the 3 or more words
trigger to enable wrapping of value, but noticed that if length of line was
exactly max-width, not > or <, it might vanish.

7. Case where no X or GPU drivers found, but dri driver detected, was not
showing, now does.

8. OpenRC is the init system in some cases, that is: readlink /sbin/init >
/sbin/openrc-init, where /proc/1/comm == init. Was showing only as OpenRC rc
type, which wasn't actually correct.

--------------------------------------------------------------------------------
ENHANCEMENTS:

1. New nvidia gpu product ids for Turing, Ampere, Lovelace, Hopper. New Intel
GPU ids.

2. Added Zinc to systembase/distro, needs slightly special handling to get both
names right. Also added Tuxedo, which could use existing methods.

3. Added dpkg tool nala, which is sort of a CLI front end for apt, zinc uses it,
but it's also in Debian main package pool. Also deb-get, which is another zinc
thing for package management.

4. Full support for dinit: version, dinitctl w/status in ServiceData

4. Added initial support for init systems: 31init (31 line C program, no
--version), Hummingbird (unknown if -v/--version).

5. A few new CPU arch ids (new Intels).

--------------------------------------------------------------------------------
CHANGES:

1. Going somewhat along with the change in Audio to call ALSA a Sound API
instead of a sound server, changed key name OpenGL: to API: OpenGL in Graphics.
Also for EGL wayland, calling that the api too.

https://en.wikipedia.org/wiki/OpenGL

This conforms more closely to how these things are defined. Note that once
again, a value had been used as a key name, which almost always indicates a
failure to understand something about the core tech.

2. Changed wrapping of values from 3 words or more to 3 or more words AND length
> 24 characters. Saw example of:
 .... used: 28.45 GiB
  (4.5%)

which isn't desirable.

3. Changed minimum wrap to 60 columns, the new wrapper features are working so
well that if users want output that short, it will usually work fine, except of
course for very long word strings like a kernel name or parameter.

Note that this does not truncate long 'words' that might be wrapped, or going
along with Change 2, long 'sentences' of 2 words, those will always appear on
the same line regardless. For 'sentences' of 3 or more words, however, it goes
word by word, so it could well wrap after the first word, and so on. Obviously,
a 24 or fewer character value will never be wrapped, which was the intended
correction of change 2.

4. Going with Fix 8, OpenRc is an init system when it owns /proc/1/comm, had not
realized that /proc/1/comm == init can map to dinit, openrc as init. Now will
only show OpenRc as rc: type if not init as well.

--------------------------------------------------------------------------------
DOCUMENTATION:

1. Updates in man for Change 1.

2. Added to docs/inxi-graphics.txt good quote re EGL/GBM, as well as VBE/GOP for
vesa. Trying to find docs where they actually say clearly it's an API is
remarkably difficult.

3. Man page, added note about Konversation requiring qdbus-qt5 (Debian+),
qt5-qttool (RHEL+/SUSE+), qt-tools (Arch+) for inxi to work inside it. Also
updated smxi.org/docs/inxi-usage.txt to note requirements for Konversation use
and setup.

4. Man, help, changed min width for -y/--width from 80 to 60.

5. docs/inxi-values.txt updated for --cygwin, --wsl fake OS type switches. Not
technically the OS, more the environment, but close enough.

6. docs/inxi-init.txt updated for new init types.

--------------------------------------------------------------------------------
CODE:

1. Refactored tools/gpu_ids.pl to correct and enhance some features.

2. Renamed functions and sections to better reflect that the display interface
is an API, this makes stuff less odd internally, and makes the function/variable
names correspond better to what the stuff really is.

3. Commented out kde konversation data source config collector, that logic looks
like it never worked, and couldn't work, since it never actually located
inxi.conf files, just paths to the data directories.

4. Expanded release.pl to handle acxi docs as well, makes it all consistent and
a lot easier to do long term.

5. Fake --wsl WSL switch, not really used, but in case.

6. Changed $b_cygwin to $windows{'cygwin'} and added $windows{'wsl'}.

7. Added -WSL to debugger string generator once WSL type is detected.

8. Refactored init, runlevel functions get_init_data() (now InitData::get()),
get_runlevel_data() (now InitData::get_runlevel()), get_runlevel_default() (now
InitData::get_runlevel_default()) into one package/class: InitData. This should
have been done a long time ago, to follow the general rule "if > 1 functions for
a tool refactor it into a class/package" for when to create a package/class
internally.

9. Completed gpu_ids.pl, now outputs the full hash set per item, so entire
blocks can be copied/pasted over. Something of a pain to get comments included,
which aren't strictly necessary in pinxi itself, but they do help read the
hashes for gpu data.

---
## [Zevotech/Shiptest](https://github.com/Zevotech/Shiptest)@[8c58ea2007...](https://github.com/Zevotech/Shiptest/commit/8c58ea20073fe006104d6400ce71cb1b2f5d9fca)
#### Monday 2022-10-31 22:48:43 by Zevotech

Adjusts necropolis chest loot pools and ports a rework of the berserkers hardsuit
<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull request process. -->

## About The Pull Request
fuck you im not writing this entire desc in github you can wait 5 minutes
<!-- Describe The Pull Request. Please be sure every change is documented or this can delay review and even discourage maintainers from merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the brackets) if you have tested your changes and this is ready for review. Leave unticked if you have yet to test your changes and this is not ready for review. -->

- [ ] I affirm that I have tested all of my proposed changes and that any issues found during tested have been addressed.

## Why It's Good For The Game

<!-- Please add a short description of why you think these changes would benefit the game. If you can't justify it in words, it might not be worth adding. -->

## Changelog

:cl:
add: Added new things
add: Added more things
del: Removed old things
tweak: tweaked a few things
balance: rebalanced something
fix: fixed a few things
soundadd: added a new sound thingy
sounddel: removed an old sound thingy
imageadd: added some icons and images
imagedel: deleted some icons and images
spellcheck: fixed a few typos
code: changed some code
refactor: refactored some code
config: changed some config setting
admin: messed with admin stuff
server: something server ops should know
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put your name to the right of the first :cl: if you want to overwrite your GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the icon ingame) and delete the unneeded ones. Despite some of the tags, changelogs should generally represent how a player might be affected by the changes rather than a summary of the PR's contents. -->

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[83c75cac2c...](https://github.com/tgstation/tgstation/commit/83c75cac2c632a51eb8252b2d93b0cf0faa0a9ee)
#### Monday 2022-10-31 23:28:20 by Jacquerel

Brimdemons & Lobstrosities drop (slightly) useful organs (#70546)



Goliaths, Legions, Watchers, and (as of recently) Bileworms all drop
something vaguely useful when they die.
Brimdemons and Lobstrosities do not. This PR aims to fix that, so that
there's at least some vague benefit to hunting them.

In this case it takes the form of organs you get when you butcher them,
similar to the regenerative core from Legions.
As they're similar to the regenerative core, I modified the regenerative
core to extend from a new common "monster core" typepath which these two
new organs also extend.
Like the regenerative core, both of these items do something when used
and something slightly different if you go to the effort of having
someone implant them into your body. They also decay over time, and you
can use stabilising serum to prevent this from happening.


https://user-images.githubusercontent.com/7483112/195967746-55a7d04d-224e-412d-aedc-3a0ec754db3d.mp4

The Rush Gland from the Lobstrosity lets you do a little impression of
their charging attack, making you run very fast for a handful of seconds
and ignoring slowdown effects. Unlike a lobstrosity you aren't actually
built to do this so if you run into a mob you will fall over, and if you
are doing this on the space station running into any dense object will
also make you fall over (it shouldn't make you _too_ much of a pain for
security to catch).
The idea here is that you use this to save time running back and forth
from the mining base.

The Brimdust Sac from the Brimdemon covers you in exploding dust. The
next three times you take Brute damage some of the dust will explode,
dealing damage equal to an unupgraded PKA shot to anything near you (but
not you).
If you do this in a space station not only is the damage proportionally
lower (still matching the PKA), but it _does_ effect you and also it
sets you on fire. You can remove the buff by showering it off.
The idea here is that you use this for minor revenge damage on enemies
whose attacks you don't manage to dodge.


https://user-images.githubusercontent.com/7483112/195967811-0b362ba9-2da0-42ac-bd55-3809473cbc74.mp4

If you implant the Rush Gland then you can use it once every 3 minutes
without consuming it, and the buff lasts very slightly longer. It will
automatically trigger itself if your health gets low, which might be
good (helps you escape a rough situation) or bad (didn't want to use it
yet).


https://user-images.githubusercontent.com/7483112/195967888-f63f7cbd-60cd-4309-8004-203afc5b2153.mp4

If you implant the Brimdust Sac then you can use it once every 3 minutes
to shake off cloud of dust which gives the buff to everyone nearby, if
you want to kit out your miner squad. The dust cloud also makes you
cough if you stand in it, and it's opaque. If you catch fire with this
organ inside you and aren't in mining atmosphere then it will explode
inside of your abdomen, which should probably be avoided, resultingly it
is very risky to use this on the space station.

---
## [Groxx/cadence-client](https://github.com/Groxx/cadence-client)@[f5e0fd25e4...](https://github.com/Groxx/cadence-client/commit/f5e0fd25e4347c85b28dac87f51b532700455d2c)
#### Monday 2022-10-31 23:51:39 by Steven L

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
## [i3roly/CMI8788](https://github.com/i3roly/CMI8788)@[1c23d16188...](https://github.com/i3roly/CMI8788/commit/1c23d161888c390ba79b9d8ee93f138fffd59173)
#### Monday 2022-10-31 23:59:24 by gagan sidhu

bring back the hardware filter functions and start converting. the best shit way i can think of atm is to clear the stream and re-add via arrays.

boy are OS containers fucking annoying on os x! you can't even find proper declarations or instantiations in "definitive sources" like:
- OS X and iOS Kernel Programming by Halvorsen and Clarke, which simply state "YOU CAN USE THESE BUT HEY WE'LL PRETEND WE TOLD YOU HOW!" (page 69 is all that covers OSArray, OSDictionary and OSSet. SAD AF)

---

