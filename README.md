## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-10-27](docs/good-messages/2022/2022-10-27.md)


2,381,942 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,381,942 were push events containing 3,545,436 commit messages that amount to 262,808,631 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 34 messages:


## [phoenixjin8/dsci100-group-project](https://github.com/phoenixjin8/dsci100-group-project)@[bfa4193c61...](https://github.com/phoenixjin8/dsci100-group-project/commit/bfa4193c61e331f567790e19bd5c99b22ba68760)
#### Thursday 2022-10-27 00:07:03 by amyw143

expected outcomes and intro

Life expectancy is a crucial metric in assessing the wellbeing of populations, and as such, is of pertinence in both medical and socioeconomic research. Essentially, life expectancy provides the average age of death in a population, revealing general insight into human mortality (Roser, Ortiz-Ospina & Ritchie, 2013). Life expectancy has risen drastically in industrialized communities since the 19th century due to the advent of new technology and more advanced healthcare. Indeed, life expectancy has globally increased from 2000 to 2019, from 66.8 years in 2000 to 73.4 years in 2019 (World Health Organization, 2019). However, this increase is not truly equal - countries with lower human development have consistently reported lower life expectancies, leading to a large discrepancy in health worldwide (Roser et al., 2013). As human societies develop new structures and technologies, the factors influencing life expectancy grow. In this project, we will analyze the effects of carbon dioxide emissions per capita (production), mean years of schooling, gross national income (GNI) per capita, and poverty headcount ratio at $6.85 a day (2017 PPP). Under the assumption that higher life expectancy leads to positive contributions to the economy, as well as general human development, it is important to determine what impedes or enhances the life expectancy of the population.

The use of fossil fuels has increased dramatically over the years following the industrial revolution, and remains popular today. As a result, its byproduct, carbon dioxide, has also increased in concentration in the atmosphere. Several decades of research over the years have indicated that rising air pollution caused by fossil fuel emissions threatens local ecosystems and accelerates global warming (Balakrishnan et al., 2018). As such, air pollution poses a large threat to the population's health, and therefore life expectancy. 

Education is an important part of societal structure, as such, it will be considered as a factor on life expectancy. Past research has indicated that higher levels of schooling are linked to higher life expectancies; in part due to more informed decisions and healthier lifestyles (Blackburn and Cipriani, 2002). In addition, the ability to attend school in some countries is linked with socioeconomic status. 

The gross national income is the total amount of money earned by a country's people and businesses, calculated from their income (citation). At a national level, a higher GNI allows more expense for health promoting public systems, such as improved healthcare and sanitation. Therefore, a higher GNI should be linked to an increase in life expectancy. 

Lastly, the poverty headcount ratio shows the percentage of the country's population who has less than $6.85 to spend per day, in PPP.  Poverty and its encompassing characteristics such as poor living conditions, limited access to housing and healthcare

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[3efa9b5382...](https://github.com/shiptest-ss13/Shiptest/commit/3efa9b538241ffef48ddf1fe102feb589e88dff0)
#### Thursday 2022-10-27 00:15:10 by Zevotech

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
## [hexagon-geo-surv/linux-stable](https://github.com/hexagon-geo-surv/linux-stable)@[d21f4b7ffc...](https://github.com/hexagon-geo-surv/linux-stable/commit/d21f4b7ffc22c009da925046b69b15af08de9d75)
#### Thursday 2022-10-27 00:22:55 by Douglas Anderson

pinctrl: qcom: Avoid glitching lines when we first mux to output

Back in the description of commit e440e30e26dd ("arm64: dts: qcom:
sc7180: Avoid glitching SPI CS at bootup on trogdor") we described a
problem that we were seeing on trogdor devices. I'll re-summarize here
but you can also re-read the original commit.

On trogdor devices, the BIOS is setting up the SPI chip select as:
- mux special function (SPI chip select)
- output enable
- output low (unused because we've muxed as special function)

In the kernel, however, we've moved away from using the chip select
line as special function. Since the kernel wants to fully control the
chip select it's far more efficient to treat the line as a GPIO rather
than sending packet-like commands to the GENI firmware every time we
want the line to toggle.

When we transition from how the BIOS had the pin configured to how the
kernel has the pin configured we end up glitching the line. That's
because we _first_ change the mux of the line and then later set its
output. This glitch is bad and can confuse the device on the other end
of the line.

The old commit e440e30e26dd ("arm64: dts: qcom: sc7180: Avoid
glitching SPI CS at bootup on trogdor") fixed the glitch, though the
solution was far from elegant. It essentially did the thing that
everyone always hates: encoding a sequential program in device tree,
even if it's a simple one. It also, unfortunately, got broken by
commit b991f8c3622c ("pinctrl: core: Handling pinmux and pinconf
separately"). After that commit we did all the muxing _first_ even
though the config (set the pin to output high) was listed first. :(

I looked at ideas for how to solve this more properly. My first
thought was to use the "init" pinctrl state. In theory the "init"
pinctrl state is supposed to be exactly for achieving glitch-free
transitions. My dream would have been for the "init" pinctrl to do
nothing at all. That would let us delay the automatic pin muxing until
the driver could set things up and call pinctrl_init_done(). In other
words, my dream was:

  /* Request the GPIO; init it 1 (because DT says GPIO_ACTIVE_LOW) */
  devm_gpiod_get_index(dev, "cs", GPIOD_OUT_LOW);
  /* Output should be right, so we can remux, yay! */
  pinctrl_init_done(dev);

Unfortunately, it didn't work out. The primary reason is that the MSM
GPIO driver implements gpio_request_enable(). As documented in
pinmux.h, that function automatically remuxes a line as a GPIO. ...and
it does this remuxing _before_ specifying the output of the pin. You
can see in gpiod_get_index() that we call gpiod_request() before
gpiod_configure_flags(). gpiod_request() isn't passed any flags so it
has no idea what the eventual output will be.

We could have debates about whether or not the automatic remuxing to
GPIO for the MSM pinctrl was a good idea or not, but at this point I
think there is a plethora of code that's relying on it and I certainly
wouldn't suggest changing it.

Alternatively, we could try to come up with a way to pass the initial
output state to gpio_request_enable() and plumb all that through. That
seems like it would be doable, but we'd have to plumb it through
several layers in the stack.

This patch implements yet another alternative. Here, we specifically
avoid glitching the first time a pin is muxed to GPIO function if the
direction of the pin is output. The idea is that we can read the state
of the pin before we set the mux and make sure that the re-mux won't
change the state.

NOTES:
- We only do this the first time since later swaps between mux states
  might want to preserve the old output value. In other words, I
  wouldn't want to break a driver that did:
     gpiod_set_value(g, 1);
     pinctrl_select_state(pinctrl, special_state);
     pinctrl_select_default_state();
     /* We should be driving 1 even if "special_state" made the pin 0 */
- It's safe to do this the first time since the driver _couldn't_ have
  explicitly set a state. In order to even be able to control the GPIO
  (at least using gpiod) we have to have requested it which would have
  counted as the first mux.
- In theory, instead of keeping track of the first time a pin was set
  as a GPIO we could enable the glitch-free behavior only when
  msm_pinmux_request_gpio() is in the callchain. That works an enables
  my "dream" implementation above where we use an "init" state to
  solve this. However, it's nice not to have to do this. By handling
  just the first transition to GPIO we can simply let the normal
  "default" remuxing happen and we can be assured that there won't be
  a glitch.

Before this change I could see the glitch reported on the EC console
when booting. It would say this when booting the kernel:
  Unexpected state 1 in CSNRE ISR

After this change there is no error reported.

Note that I haven't reproduced the original problem described in
e440e30e26dd ("arm64: dts: qcom: sc7180: Avoid glitching SPI CS at
bootup on trogdor") but I could believe it might happen in certain
timing conditions.

Fixes: b991f8c3622c ("pinctrl: core: Handling pinmux and pinconf separately")
Signed-off-by: Douglas Anderson <dianders@chromium.org>
Reviewed-by: Stephen Boyd <swboyd@chromium.org>
Link: https://lore.kernel.org/r/20221014103217.1.I656bb2c976ed626e5d37294eb252c1cf3be769dc@changeid
Signed-off-by: Linus Walleij <linus.walleij@linaro.org>

---
## [swbs-co/odoo](https://github.com/swbs-co/odoo)@[e7c8fed8e3...](https://github.com/swbs-co/odoo/commit/e7c8fed8e373d7005c16c88d3a7bad6f425d13e5)
#### Thursday 2022-10-27 01:00:41 by qsm-odoo

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
## [bustedwallstudios/Softbody](https://github.com/bustedwallstudios/Softbody)@[a596122d44...](https://github.com/bustedwallstudios/Softbody/commit/a596122d443cd8aad89c1025a9e6d88291434d0d)
#### Thursday 2022-10-27 01:29:07 by Alexander McCarter

added shitty edge bulges with an idiotic workaround for the stupid fucking weird ass original rest length number

---
## [JasonGoemaat/bitburner-batcher](https://github.com/JasonGoemaat/bitburner-batcher)@[94776213fd...](https://github.com/JasonGoemaat/bitburner-batcher/commit/94776213fddc8fb13db6b580ec0e80e4df1b3d7f)
#### Thursday 2022-10-27 02:41:58 by Jason Goemaat

Lotta stuff

Most recent it `tools/infiltration.js` - Oh, yeah!  Easy billions of
money even on some restricted nodes.  166k rep for a faction by
taking on MegaCorp.  From a script found on Reddit, and I added an
'auto' option and 'faction' option to keep replaying and pick money
by default or a faction of your choice for reward.

Second, I added all my simple corp scripts and some in samples,
early-corp.js being very nice.

Also borrowed sample/contractor.js for auto finding and solving
contracts.

Also simple singularity and gang scripts.

Tweaks to start-hgw.js and some other scripts.  New mega-hack script
for when your hacking skill is just too high, like when I had the
weaken time on MegaCorp being just 33ms and 1 hack thread taking
almost 90%.   It uses zombies for each HGW and runs them at the same
time.  About 4ms extra time for each.

---
## [avar/git](https://github.com/avar/git)@[340ce52343...](https://github.com/avar/git/commit/340ce5234364ee04061901b3001e3ae7d3290741)
#### Thursday 2022-10-27 03:33:06 by Ævar Arnfjörð Bjarmason

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
## [Ashima1503/Endtermproject_Frontend](https://github.com/Ashima1503/Endtermproject_Frontend)@[cd4caf823b...](https://github.com/Ashima1503/Endtermproject_Frontend/commit/cd4caf823b69d0c499e3904707f9b879fd0e3c06)
#### Thursday 2022-10-27 05:01:29 by Ashima1503

This is a project on matrimonial website in react.

Me and my friend Dia have made our project in react. It includes 11 components namely Navbar, Register, Login, Subscription, Match, Cards, Boysprofile, Girlsprofile, Gateway, BProfile & GProfile. We have used routing, hooks etc. in our project.

---
## [mjungsbluth/opa](https://github.com/mjungsbluth/opa)@[965301f90e...](https://github.com/mjungsbluth/opa/commit/965301f90e1c10900c2c134ee21e486993796a20)
#### Thursday 2022-10-27 06:44:47 by Stephan Renatus

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
## [iamcosmin/Allo](https://github.com/iamcosmin/Allo)@[9dc24013e7...](https://github.com/iamcosmin/Allo/commit/9dc24013e75c1a3e6e492ecb27fc7eefa212d476)
#### Thursday 2022-10-27 07:54:37 by iamcosmin

1.3.5 (330)

RO:

De la ultima actualizare a canalelor beta și stabil (din luna martie), multe lucruri s-au petrecut în spatele scenei.

BREAKING:

Utilizatorii care nu au verificat emailul vor trebui să și-l verifice, în caz contrar nu vor mai avea acces la aplicație.
DESIGN

REBRANDING MAJOR: Allo a fost redesenat cu o culoare de accent mov.
Am adaptat majoritatea schimbărilor propuse de Google în Material 3.
Dispozitivele compatibile cu noile caracteristici ale Android 12+ au opțiunea de a activa tema aplicației în funcție de fundalul telefonului. Restul utilizatorilor pot personaliza aplicația cu ajutorul culorilor prestabilite.
Ecranele late au acum bara de navigare pe partea stângă, lăsând mai mult spațiu în partea de jos.
Experiența de utilizare cu o mână este îmbunătățită: bara de navigare este acum mai mare pentru ca utilizatorul să ajungă la conținutul dorit mai ușor. Pe măsură ce conținutul este derulat, bara scade în dimensiune, permițând conținutului să se întindă pe tot ecranul.
Pentru o performanță sporită, am adăugat abilitatea de a dezactiva majoritatea animațiilor. Această opțiune este activată implicit pe Web, dar poate fi dezactivată.
Toate versiunile de Android au acum un splash screen cât aplicația se încarcă. Cei care au Android 12 sau mai mare au parte de un log animat la pornirea aplicației. Utilizatorii web se pot bucura de faptul că nu vor mai fi orbiți de lumina albă atunci când au activat modul întunecat și pornesc în primă instanță aplicația.
Tranzițiile au fost îmbunătățite.
Font nou.
ÎMBUNĂTĂȚIRI MAJORE

Utilizatorii aplicației Web au parte acum de fotografii de profil.
La încărcarea conținutului media, animația indicatorului de progres a fost adăugată.
Lista de mesaje din conversații este mult mai fiabilă: nu mai există probleme majore la animații, mai ales cu privire la reanimarea întregii liste de mesaje atunci când utilizatorul revenea din altă aplicație.
Am îndepărtat abilitatea de a răspunde la mesaje direct din panoul de notificări. Sperăm că această funcție se va reîntoarce într-o versiune viitoare de Allo.
Mărirea imaginilor (pinch to zoom) a fost îmbunătățită substanțial.
Cea mai așteptată îmbunătățire: funcționează notificările! De asemenea, acum se pot dezactiva notificările în conversațiile nedorite.
Am adăugat pagina "Despre": informații despre aplicație, utile când o eroare își face de cap.
Am rezolvat eroarea care afișa un ecran gri, ca urmare a deconectării din aplicație.
Lista de conversații are animații îmbunătățite.
Am implementat o pagină mai prietenoasă pentru modificarea setărilor contului tău Allo.
Folosești o altă adresă de email? Schimbă-ți emailul direct din Allo, fără să-ți pierzi datele.
Aplicația este mai reactivă la schimbări de autentificare.
Ai derulat prea multe mesaje în conversație? Acum există un buton care să deruleze lista cu mesaje până la capăt.
Când răspunzi la un mesaj, experiența este mai rafinată.

EN:

Since the last update to the beta and stable channels (since March), a lot has been happening behind the scenes.

BREAKING:

Users who have not verified their email will have to verify it, otherwise they will no longer have access to the application.
DESIGN

MAJOR REBRANDING: Allo has been redesigned with a purple accent color.
We adapted most of the changes proposed by Google in Material 3.
Devices compatible with the new features of Android 12+ have the option to activate the theme of the application according to the background of the phone. The rest of the users can customize the application with the help of preset colors.
Wide screens now have the navigation bar on the left side, leaving more space at the bottom.
The one-handed user experience is improved: the navigation bar is now larger for the user to reach the desired content more easily. As the content is scrolled, the bar decreases in size, allowing the content to span the entire screen.
For increased performance, we added the ability to disable most animations. This option is enabled by default on the web, but can be disabled.
All Android versions now have a splash screen while the app is loading. Those with Android 12 or higher get an animated log when starting the app. Web users can enjoy the fact that they will no longer be blinded by white light when they have activated the dark mode and start the application in the first instance.
Transitions have been improved.
New font.
MAJOR IMPROVEMENTS

Web App users now have profile photos.
Added progress indicator animation when loading media.
The list of messages in conversations is much more reliable: there are no longer major problems with animations, especially regarding the reanimation of the entire list of messages when the user returns from another application.
Removed the ability to reply to messages directly from the notification panel. Hopefully this feature will return in a future version of Allo.
Pinch to zoom has been substantially improved.
Most awaited improvement: Notifications work! Notifications in unwanted conversations can also now be turned off.
Added "About" page: information about the app, useful when a bug rears its head.
Fixed the bug showing a gray screen after logging out of the app.
Chat list has improved animations.
Implemented a friendlier page for changing your Allo account settings.
Are you using a different email address? Change your email directly from Allo without losing your data.
The application is more reactive to authentication changes.
Did you scroll through too many messages in the conversation? Now there is a button to scroll the list of messages to the end.
When you reply to a message, the experience is more refined.

---
## [BubkisLord/modlinks](https://github.com/BubkisLord/modlinks)@[7ecdb977ed...](https://github.com/BubkisLord/modlinks/commit/7ecdb977ed51a1040282d4b6d29280f75937bf30)
#### Thursday 2022-10-27 08:27:54 by BubkisLord

Added Fyrenest v3

# Fyrenest v3 - Lore Update
This update re-works most of the Hollow Knight lore!
This is the first snapshot of what is to come in version 3!
So far, Fyrenest v3 remaps the Ancient Basin, The Hive, The Abyss, The Resting Grounds, and Crystal Peak!
It also rewrites dialogue for most of the NPCs like The Seer, The Last Stag, Elderbug, Cornifer (now called Conifer), Iselda (now called Pine), and more! Version 3 of Fyrenest also adds new charms, modifies some old ones, and changes the ways to get some!

Technically, this is a pre-release of the finished version 3 of Fyrenest,
But since this is already such a big update, I think it should have its own release.

## Major Changes
- Added lots of room transitions.
- Added various game objects to different rooms.
- Deleted various game objects in different rooms.
- Replaced the location of lots of items.
- Rewrote & revised all already replaced dialogue.
- Replaced tons more dialogue.
- Split the Hive area.
- Mirrored half of Ancient Basin.
- Mirrored half of The Hive.

## Minor Changes
These are minor changes from the last update that aren't already listed.
- Made some modifications to the language replacement system.
- Made all charms inherit the itemchanger charm class.
- Re-worked some code. (So minor it isn't all gonna be said)
- Added more comments and summaries so code is easier to understand.
- Starting on adding charms around the map. (Like with VoidSoul)
- Made all charms publicly accessible. (In terms of the code)
- Updated where the charm images are stored.
- Made tiny tweaks to some of the charm images.
- Started doing something for the README.md (Not that it effects the gameplay)
- Added SlowJump.
- Added QuickJump.
- Modified SlowFall.
- Modified QuickFall.
- Added image for SlowJump.
- Added image for QuickJump.
- Added new ways to get some of the charms.

## Bug Fixes:
- Fixed Elderstone charm, now gravity changing works.
- Fixed some menu bugs.
- Fixed some bugs with various charms.
- Fixed a bug with the abilities. (With object preloads and stuff)

## Known Bugs:
- SlowJump is broken. (Does nothing)
- SlowFall is broken. (Does nothing)
- QuickJump is broken. (Does nothing)
- QuickFall is broken. (Does nothing)
- Errors with some room transitions when continuing from past saves.
- A few bugs with the Aspid room in the Forgotten Crossroads.
- Some bugs with the hot springs in the Forgotten Crossroads.
- Sometimes the knight cannot move. (To fix this, use noclip from the DebugMod to enter a room transition. You can then move as normal.)
- <strong>SPOILER COMING UP:</strong> VoidSoul can still be obtained without getting to the area where Joni's Blessing is found.

---
## [youniversityupc/app](https://github.com/youniversityupc/app)@[0e99947eb8...](https://github.com/youniversityupc/app/commit/0e99947eb8b84b03d397891a93c2d04672a8d29f)
#### Thursday 2022-10-27 08:58:35 by Diego Albitres

refactor: fixed AppBar tab rendering

OMG, this is finally working. I hate myself.

---
## [neebe000/kernel_xiaomi_mt6785](https://github.com/neebe000/kernel_xiaomi_mt6785)@[7432cc678c...](https://github.com/neebe000/kernel_xiaomi_mt6785/commit/7432cc678c4a5d56bb449effc2ae34e92c92a13e)
#### Thursday 2022-10-27 09:42:44 by Peter Zijlstra

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
Signed-off-by: neebe000 <neebexd@gmail.com>

---
## [SeigaSeiga/tgstation-local](https://github.com/SeigaSeiga/tgstation-local)@[db83f6498d...](https://github.com/SeigaSeiga/tgstation-local/commit/db83f6498da37ecd25588ea3f7024409d2f3f117)
#### Thursday 2022-10-27 09:52:15 by vincentiusvin

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
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[57ec27c81b...](https://github.com/odoo-dev/odoo/commit/57ec27c81bd49192cce5523c3d7151890e75f00f)
#### Thursday 2022-10-27 09:59:56 by qsm-odoo

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

X-original-commit: e7c8fed8e373d7005c16c88d3a7bad6f425d13e5

---
## [reinpeter/ultimate-geography](https://github.com/reinpeter/ultimate-geography)@[90e1e3dfff...](https://github.com/reinpeter/ultimate-geography/commit/90e1e3dfff699da113346e4ae1522ff0c8f5479e)
#### Thursday 2022-10-27 10:24:07 by aplaice

Expand SADR country info mentioning alternative names (#570)

Fix #561.

As discussed in #561, saying that "Sahara Zachodnia" (Western Sahara)
is also known as SADR (in the Polish version), is ambiguous and
potentially misleading, since Western Sahara is both the name of the
geographic area (ignoring political associations) and one of the names
used for the partially recognised state.  However, AFAICT, we have the
exact same situation for Artsakh, in Polish, (Górski
Karabach (Nagorno-Karabakh) also known as Artsakh, where
Nagorno-Karabakh can refer both to the country and the geographical
area.).  Also, since we're generally dealing with countries, here, it
should be clear that we mean Western Sahara (the country) rather than
WS (the area), so I think my initial worry was overblown.

I'm not 100% sure if I have the correct gender for conosciuto in
Italian (should it agree with Repubblica.. or with stato?).

The same question holds for Czech — should známý agree with
..republika or with stát?

I've gone with agreement with stát for Czech (male) and with
republic (female) for Italian, because in the former the second clause
is separated only with a comma, while in the latter it's separated by
a semicolon.  The choice of separator was based on precedence in other
cases (Faroe islands and Taiwan).

---
## [boylie3d/reds-fit-v2](https://github.com/boylie3d/reds-fit-v2)@[b3e02f6606...](https://github.com/boylie3d/reds-fit-v2/commit/b3e02f6606fc50796d44e1419093d6c9fb11a7f9)
#### Thursday 2022-10-27 14:42:04 by Dave Boyle

Profile stats (#52)

closes #51 and closes #50 , though i need to hook the participation stats up properly

* activity stats working

holy shit i got it

* starting participation

removed hellof comments

* bit of finessing in the activity graph

feelin bored might close #50 i dunno

* Update activityGraph.tsx

typescript is a silly language sometimes.

* Update participationStats.tsx

* Update [id].tsx

---
## [GeoB99/reactos](https://github.com/GeoB99/reactos)@[3a3114de07...](https://github.com/GeoB99/reactos/commit/3a3114de07e3288c1523c2a2094d67bc06dffc8d)
#### Thursday 2022-10-27 15:37:28 by George Bișoc

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
## [lyz-code/blue-book](https://github.com/lyz-code/blue-book)@[56f423cc29...](https://github.com/lyz-code/blue-book/commit/56f423cc29d4f2624f7b453ae50d7b0c58eff0f2)
#### Thursday 2022-10-27 16:21:10 by Lyz

feat(cpu#market-analysis): Add the market analysis

feat(cpu#cpu-coolers): Analyze the cpu coolers

feat(cpu#cpu-thermal-paste): Analyze the use of cpu thermal paste

Thermal paste is designed to minimize microscopic air gaps and irregularities
between the surface of the cooler and the CPU's IHS (integrated heat spreader),
the piece of metal which is built into the top of the processor.

Good thermal paste can have a profound impact on your performance, because it
will allow your processor to transfer more of its waste heat to your cooler,
keeping your processor running cool.

Most pastes are comprised of ceramic or metallic materials suspended within
a proprietary binder which allows for easy application and spread as well as
simple cleanup.

These thermal pastes can be electrically conductive or non-conductive, depending
on their specific formula. Electrically conductive thermal pastes can carry
current between two points, meaning that if the paste squeezes out onto other
components, it can cause damage to motherboards and CPUs when you switch on the
power. A single drop out of place can lead to a dead PC, so extra care is
imperative.

Liquid metal compounds are almost always electrically conductive, so while these
compounds provide better performance than their paste counterparts, they require
more focus and attention during application. They are very hard to remove if you
get some in the wrong place, which would fry your system.

In contrast, traditional thermal paste compounds are relatively simple for every
experience level. Most, but not all, traditional pastes are electrically
non-conductive.

Most cpu coolers come with their own thermal paste, so check yours before buying
another one.

feat(drone): Introduce Drone

[Drone](https://www.drone.io/) is a modern Continuous Integration platform that
empowers busy teams to automate their build, test and release workflows using
a powerful, cloud native pipeline engine.

Check how to install it [here](drone.md#installation)

feat(kag#Builder guides): Builder guides

[Turtlebutt and Bunnie](https://deynarde.github.io/kag-builder-guide)
guide is awesome.

feat(nas): Choose the Power Supply Unit and CPU cooler

After doing some [basic research](cpu.md#cpu-coolers) I've chosen the [Dark Rock
4](https://www.bequiet.com/en/cpucooler/1376) but just because the [Enermax
ETS-T50 AXE Silent
Edition](https://www.enermaxeu.com/products/cpu-cooling/air-cooling/ets-t50-axe/)
doesn't fit my case :(.

Using [PCPartPicker](https://pcpartpicker.com/list/) I've seen that with 4 disks
it consumes approximately 264W, when I have the 8 disks, it will consume up to
344W, if I want to increase the ram then it will reach 373W. So in theory I can go with a 400W power supply unit.

You need to make sure that it has enough wires to connect to all the disks.
Although that usually is not a problem as there are adapters:

* [Molex to
    sata](https://www.amazon.com/CB-44SATA-Individually-Sleeved-Connector-Premium/dp/B0036ORCIA/ref=sr_1_13?ie=UTF8&qid=1409942557&sr=8-13&keywords=sleeved+molex+to+sata&tag=linus21-20)
* [Sata to sata](https://www.amazon.com/dp/B0086OGN9E/ref=wl_it_dp_o_pd_nS_ttl?_encoding=UTF8&colid=2IW6VX45YF9B0&coliid=I1QUIF5VMSN2SG&psc=1&tag=linus21-20)

After an [analysis on the different power supply units](psu.md), I've decided to
go with [Be Quiet! Straight Power 11 450W Gold](https://www.bequiet.com/en/powersupply/1251)

feat(psu): Introduce Power Supply Unit

[Power supply unit](https://linuxhint.com/pc-power-supply-unit/) is the component
of the computer that sources power from the primary source (the power coming
from your wall outlet) and delivers it to its motherboard and all its
components. Contrary to the common understanding, the PSU does not supply power
to the computer; it instead converts the AC (Alternating Current) power from the
source to the DC (Direct Current) power that the computer needs.

There are two types of PSU: Linear and Switch-mode. Linear power supplies have
a built-in transformer that steps down the voltage from the main to a usable one
for the individual parts of the computer. The transformer makes the Linear PSU
bulky, heavy, and expensive. Modern computers have switched to the switch-mode
power supply, using switches instead of a transformer for voltage regulation.
They’re also more practical and economical to use because they’re smaller,
lighter, and cheaper than linear power supplies.

PSU need to deliver at least the amount of power that each component requires,
if it needs to deliver more, it simply won't work.

Another puzzling question for most consumers is, “Does a PSU supply constant
wattage to the computer?” The answer is a flat No. The wattage you see on the
PSUs casing or labels only indicates the maximum power it can supply to the
system, theoretically. For example, by theory, a 500W PSU can supply a maximum
of 500W to the computer. In reality, the PSU will draw a small portion of the
power for itself and distributes power to each of the PC components according to
its need. The amount of power the components need varies from 3.3V to 12V. If
the total power of the components needs to add up to 250W, it would only use
250W of the 500W, giving you an overhead for additional components or future
upgrades.

Additionally, the amount of power the PSU supplies varies during peak periods
and idle times. When the components are pushed to their limits, say when a video
editor maximizes the GPU for graphics-intensive tasks, it would require more
power than when the computer is used for simple tasks like web-browsing. The
amount of power drawn from the PSU would depend on two things; the amount of
power each component requires and the tasks that each component performs.

I've also added the next sections:

* [Power supply efficiency](psu.md#power-supply-efficiency)
* [Power supply shopping tips](psu.md#power-supply-shopping-tips)
* [Market analysis](psu.md#market-analysis)

---
## [SpaceLoveSs13/Skyrat-tg](https://github.com/SpaceLoveSs13/Skyrat-tg)@[967de5fb00...](https://github.com/SpaceLoveSs13/Skyrat-tg/commit/967de5fb00613b8004ccfeea93a399799d99191e)
#### Thursday 2022-10-27 17:06:38 by SkyratBot

[MIRROR] Brains can now be healed with mannitol without being fully decayed among other quality of life tweaks [MDB IGNORE] (#16716)

* Brains can now be healed with mannitol without being fully decayed among other quality of life tweaks (#70357)

Removed the minimum amount of mannitol required to pour it since limiting this made barely any sense in the first place. Why oh why must we coders implement useless restrictions? (Useless restrictions caused the decay bug anyways.)

Brains no longer care about whether or not they're fully decayed when checking if they can be healed by pouring mannitol on them. They instead check if they're damaged at all and if they are, they'll let you pour mannitol on them.

The amount of time it takes to pour mannitol onto a brain is now 3 seconds instead of 6 seconds as it was way too slow. (Especially since something like a surgery step takes less time than 6 seconds.)

The solution is now only partially consumed as well, meaning if you need 20u of mannitol to fix a brain and you have a mixture of 40u of mannitol and 40u of mercury for example, pouring it will consume 40u of the mixture since you can't magically separate out the mannitol. This is rounded up, by the way. (Before this it simply consumed all of the mannitol, somehow you apparently can't stop pouring even while slowly pouring, according to the text.)

I've also very slightly increased the consistency of the pouring messages.

Fixes #70355

* Brains can now be healed with mannitol without being fully decayed among other quality of life tweaks

Co-authored-by: RikuTheKiller <88713943+RikuTheKiller@users.noreply.github.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[b2be252eb6...](https://github.com/tgstation/tgstation/commit/b2be252eb61e91f3aac08b1e4160420e444db3e8)
#### Thursday 2022-10-27 17:07:56 by san7890

UpdatePaths Readme - Reforged (#70806)

* UpdatePaths Readme - Reforged

I'm a bit tired after typing for the last hour so apologies if some of this stuff is unreadable. Basically, I just took time to add a small blurb about UpdatePaths in MAPS_AND_AWAY_MISSIONS.md, as well as write out examples on how you can properly use every single function UpdatePaths might have. I'm probably missing something? I think I got everything though. Let me know if I should be consistent somehow, but I did deliberately choose different test-cases per example because it's nearly impossible to come up one "generic" fit-all situation that illustrates every possible use of UpdatePaths (to my small mind).

Anyways, hope this helps.

* i fucked up with the TGM format

augh

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[937fb57d4b...](https://github.com/treckstar/yolo-octo-hipster/commit/937fb57d4b3e777d028f47b50ec6907082f81e25)
#### Thursday 2022-10-27 17:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [dashodanger/Obsidian](https://github.com/dashodanger/Obsidian)@[9863d33d15...](https://github.com/dashodanger/Obsidian/commit/9863d33d15eb399c20c6d086c45be24a7d4ad6bf)
#### Thursday 2022-10-27 18:36:26 by Demiosis

Modified slightly the organ T hall

To help impatient kids, peoples who can't read a map and zoomers understand it better! Holy shit I laughed quite hard on this one..

---
## [tgodzik/metals](https://github.com/tgodzik/metals)@[6fca4bc1b2...](https://github.com/tgodzik/metals/commit/6fca4bc1b27e11e955a366b6251a2e8ec73ff755)
#### Thursday 2022-10-27 19:23:21 by ckipp01

feat: capture and forward `diagnosticCode`

This relates to the grand plan of
https://github.com/lampepfl/dotty/issues/14904 and recently forwarding
the `diagnosticCode` has been merged in
https://github.com/lampepfl/dotty/pull/15565 and also backported so it
should show up in the 3.2.x series. While this pr isn't super exciting,
it's just making sure we capture the code and forward it, this should
unlock _much_ better ways to determine what code actions are available
for a given diagnostic. Meaning we don't have to do lovely things like
regex on the diagnostic message for Scala 3 diagnostics.

NOTE: that this does need some more changes in the build servers before
this is usable. So we can wait for those to be merged in if you'd like.

- [ ] sbt - https://github.com/sbt/sbt/pull/6998
- [ ] Bloop - https://github.com/scalacenter/bloop/pull/1750
- [ ] Mill - https://github.com/com-lihaoyi/mill/pull/1912

Now if you look at the trace file for a diagnostic you'll see the
addition of the code:

```
  "diagnostics": [
    {
      "range": {
        "start": {
          "line": 9,
          "character": 15
        },
        "end": {
          "line": 9,
          "character": 19
        }
      },
      "severity": 1,
      "code": "7",
      "source": "sbt",
      "message": "Found:    (\u001b[32m\"hi\"\u001b[0m : String)\nRequired: Int\n\nThe following import might make progress towards fixing the problem:\n\n  import sourcecode.Text.generate\n\n"
    }
  ],
```

Refs: https://github.com/lampepfl/dotty/issues/14904

---
## [Offroaders123/MCRegionJS](https://github.com/Offroaders123/MCRegionJS)@[ece936d5d7...](https://github.com/Offroaders123/MCRegionJS/commit/ece936d5d79331e017cba67e107602cb99abb2bf)
#### Thursday 2022-10-27 19:24:29 by Offroaders123

Aquatic Chunks! v0

With more thanks to UtterEvergreen1, they decompiled the source code for MCCToolChest, and have been working with the chunk parsing bits, and made it work for Aquatic+ versions! Since I'm not familiar with working in C++ (I can read it now, just no experience in writing it), I rewrote the source the best I could, over in TypeScript. This is more to try and reverse engineer how the format works, using the source, then to get a working parser the first time around. This version will definitely not be able to parse anything. Now that I rewrote it in something more familiar to me, I can start abstracting simple parts down so it is easier to understand. That's what I did with NBT.js, and it worked very well. Take something big, then tear it down, and put it back together to look more like you want it to. Eventually, things start to click, and you will understand the implementation enough to write your own program for the format, and then you can document the format using that! So, cheers to the last 5 hours or so of trying to understand the reverse-engineered MCCToolChest code, but in TypeScript! haha.

Oh yeah, one other note:
I didn't convert the functions that weren't used by `class AquaticParser` itself, like `method_3`, `method_9`, `method_11`, and a few others.

---
## [soynain/microservice-practice](https://github.com/soynain/microservice-practice)@[bf7edd0b42...](https://github.com/soynain/microservice-practice/commit/bf7edd0b423c91fd3407917398d373905a91cc37)
#### Thursday 2022-10-27 19:55:37 by Moises

Because I'm still not getting how da fuck spring security works yet (pretty complicated to me for god's sakes), I'm overtaking the other microservices for the better, this one is small too, practically every microservice's gonna be easy to code, the hard part is the security, the dockerization, orchestration? and the queue implementation for the sagas

---
## [Pingumask/townsquare](https://github.com/Pingumask/townsquare)@[974bbb1a0f...](https://github.com/Pingumask/townsquare/commit/974bbb1a0f35ab2a3333ba2a28955956e24fd900)
#### Thursday 2022-10-27 20:14:27 by Dae Lorant

Updated night order for all roles

Updated night order for all roles to match the order at https://script.bloodontheclocktower.com/data/nightsheet.json

Some noticeable changes:
- Legion was moved much earlier in the order of demons (relevant if a another demon is made in a legion game, you can keep it around and kill it with legion before it kills on a subsequent night)
- Amnesiac was moved much later in night order (a more reasonable place for the most common type of amni abilities)
- Magician was given a night order for N1
- Pixie was given a night order for other nights

---
## [weblate/HeroicGamesLauncher](https://github.com/weblate/HeroicGamesLauncher)@[3f6541c8a7...](https://github.com/weblate/HeroicGamesLauncher/commit/3f6541c8a700511cea9f0c9b572a5d2138ee76e3)
#### Thursday 2022-10-27 20:18:37 by Mathis Dröge

Improve README and developer experience (#1807)

* Update VSCode configuration

* Lots of README changes

- Update our bages; might've overdone it a little, but they're fun to add :^)
- Add badges for Web Technologies used
- Rewrite & bump up system requirements a bit
- Wrap the Language list, Development in a container, and Screenshots in
  <details>; this makes the page load faster and makes it seem less
  daunting
- Add a Flathub badge to the Flatpak section
- Unify Linux install instructions (as much as possible)
- Remove 3rd-party APT repository
  In my opinion, we have enough distribution formats already, and the
  install instructions are a little dodgy
- Add Beta AUR package to the list
- Clarify Windows install instructions by splitting up WinGet and manual
  install
- Make "Development environment" its own section
- Remove Beta and Alpha notes on Windows and macOS build instructions
- Explain what exactly is happening when you run `yarn dev` and in which
  scenarios you might want to use it
- Move the "Back to top" badge to the actual bottom of the page

* Add a Content Security Policy

This doesn't really do much in our situation:
- Just in case someone ever manages to load a website in Heroic's main
  window, no JS can run inside it
- Gets rid of the warning in the console when testing with `yarn dev`

I've tested the Webviews (unaffected) and links to ProtonDB and such
(also unaffected, not sure why though). Please test if this breaks
anything

---
## [BenGercuj/PizzaPain](https://github.com/BenGercuj/PizzaPain)@[1b16114bc0...](https://github.com/BenGercuj/PizzaPain/commit/1b16114bc0beee7b6c74fb79b37c47af2a15765d)
#### Thursday 2022-10-27 21:00:13 by Bence Gercuj

Finally fixed that fucking annoying little shit bug

---
## [rudra-sett/Jam-O-Lantern-2022](https://github.com/rudra-sett/Jam-O-Lantern-2022)@[561cd62acf...](https://github.com/rudra-sett/Jam-O-Lantern-2022/commit/561cd62acf563a9f5a3bcd4b7c8d837485ec809b)
#### Thursday 2022-10-27 21:56:00 by TroubledCalf

fixed fire rate issue, but new quirk

BUG/FEATURE: the speed at which the fireball is shot is dependent on how far away the player is from the candle, so the farther it is, the faster it travels and the closer it is, the slower it fires and ooh boy because of that additional speed variable it fucking GOES

---
## [Humonitarian/CEV-Eris](https://github.com/Humonitarian/CEV-Eris)@[29430253ff...](https://github.com/Humonitarian/CEV-Eris/commit/29430253ffa7c3394df438c922c3827bfbf79f51)
#### Thursday 2022-10-27 22:31:23 by maikilangiolo

Levergun re do (#7587)

* update timer (#7501)

* FUCK YOU FUCK YOUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU

* Update code/modules/projectiles/guns/projectile/battle_rifle/levergun.dm

Co-authored-by: hyperioo <64754494+hyperioo@users.noreply.github.com>

---
## [Moonstroke/SDLife](https://github.com/Moonstroke/SDLife)@[5ff08876d0...](https://github.com/Moonstroke/SDLife/commit/5ff08876d00939c34e5c536a5ea2073d5e983b5b)
#### Thursday 2022-10-27 22:41:25 by joH1

Add parens around expr to shut up paranoid gcc

GCC complains when parens are *not* used around a logical AND
expression within a logical OR expression. It also does not support
-Wno-logical-op-parentheses, so the only way to silence the warning is
to oblige and add parentheses around the && expression.

This is plain stupid, and it makes *me* look like a newbie programmer.
I know perfectly well that && has higher precedence than ||, and *not*
using them here shows that I trust my programming skills, and that
other programmers can rely on *my* programming skills as well! This is
a tacit contract between developers that I am forced to break because
the GCC guys cater for newbies more than experienced programmers.
Anyway. At least the line stays below 80 chars, and I don't have to
wrap it.

---
## [Daoma1/free-programming-books](https://github.com/Daoma1/free-programming-books)@[5fd70502a0...](https://github.com/Daoma1/free-programming-books/commit/5fd70502a063c46914fd444d2511c8233f81777f)
#### Thursday 2022-10-27 22:52:32 by Mathieu FONTAINE

Update free-programming-cheatsheets.md - React (#7095)

I suggested a React cheat sheet that I use very often. It is one of the most exhaustive and qualitative in my opinion.

---
## [embeddedTS/linux-lts](https://github.com/embeddedTS/linux-lts)@[adee8f3082...](https://github.com/embeddedTS/linux-lts/commit/adee8f3082b01e5dab620d651e3ec75f57c0c855)
#### Thursday 2022-10-27 22:52:57 by Peter Zijlstra

x86/nospec: Unwreck the RSB stuffing

commit 4e3aa9238277597c6c7624f302d81a7b568b6f2d upstream.

Commit 2b1299322016 ("x86/speculation: Add RSB VM Exit protections")
made a right mess of the RSB stuffing, rewrite the whole thing to not
suck.

Thanks to Andrew for the enlightening comment about Post-Barrier RSB
things so we can make this code less magical.

Cc: stable@vger.kernel.org
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Link: https://lkml.kernel.org/r/YvuNdDWoUZSBjYcm@worktop.programming.kicks-ass.net
[bwh: Backported to 5.10: adjust context]
Signed-off-by: Ben Hutchings <benh@debian.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---

