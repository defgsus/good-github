## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-11-02](docs/good-messages/2022/2022-11-02.md)


2,264,389 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,264,389 were push events containing 3,413,808 commit messages that amount to 265,081,421 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 40 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[55e5c5be67...](https://github.com/tgstation/tgstation/commit/55e5c5be679f37093e8e60f1f6bdfc4030aba4a6)
#### Wednesday 2022-11-02 00:02:35 by Striders13

Clowns will now always like bananas. (#70919)



## About The Pull Request
Clown's liver makes them like bananas, ignoring their racial food
preferences.

## Why It's Good For The Game
I don't think clown moths should vomit from eating bananas. They are
clowns, after all.
Also clowns are healed from eating them, so it's a bit silly that they
vomit from their funny medicine.

## Changelog


:cl:
balance: Non-human clowns enjoy eating bananas now.
/:cl:

---
## [GoblinBackwards/tgstation](https://github.com/GoblinBackwards/tgstation)@[83c75cac2c...](https://github.com/GoblinBackwards/tgstation/commit/83c75cac2c632a51eb8252b2d93b0cf0faa0a9ee)
#### Wednesday 2022-11-02 00:39:41 by Jacquerel

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
## [DAKKA-WAAAGH/tgstation](https://github.com/DAKKA-WAAAGH/tgstation)@[d45e244401...](https://github.com/DAKKA-WAAAGH/tgstation/commit/d45e244401425d34edc38e3dd2f3c2bbdbcec7ce)
#### Wednesday 2022-11-02 00:52:56 by san7890

Crab-17 No Longer Breaks Economy If You Swipe Too Fast (#70094)

Hey there,

Remember swiping credit cards, before everything was chipped? You know how sometimes if you went too slow, the transaction might fail, the cashier had to plonk in some digits on their machine, and you had to go again? That kinda sucked.

If you're too young to get that reference, just imagine the card swiping task in AMONG US. Doesn't that minigame suck? You know exactly what that is. Same principle.

Anyways, that's pretty much what was going on here. The reason why SS.Economy would break so god damn hard if you swiped an ID before the machine's "boot up" slowflake animation was complete is probably due to the line where it starts fast processing. I added an early return to check for if the animation was complete by leveraging a var we already set at the end of the process, because I am lazy.

There's probably a few other ways you can tackle this issue, but this feels right to me in a thematic sense. I'm willing to change it if needed though.

---
## [DAKKA-WAAAGH/tgstation](https://github.com/DAKKA-WAAAGH/tgstation)@[223e8bfd96...](https://github.com/DAKKA-WAAAGH/tgstation/commit/223e8bfd96a7762f0d23dd9b789fa90be1a572ec)
#### Wednesday 2022-11-02 00:52:56 by Time-Green

Fixes gravity pulse and transparent floor plane sharing a layer (#70124)

fixes gravity pulse and transparent floor plane sharing a layer

Broken by #69642 , sorry
I'll open up a seperate PR later today with a unit test to catch these cases
(my later today is in like 10 hours)

closes #70123 (weird fucking floors)

---
## [ttaylorr/git](https://github.com/ttaylorr/git)@[a1a9cf5641...](https://github.com/ttaylorr/git/commit/a1a9cf5641eafd8fe489db25c4dc964368660e7b)
#### Wednesday 2022-11-02 00:53:50 by Ævar Arnfjörð Bjarmason

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
Signed-off-by: Taylor Blau <me@ttaylorr.com>

---
## [mc-oofert/tgstation](https://github.com/mc-oofert/tgstation)@[b2be252eb6...](https://github.com/mc-oofert/tgstation/commit/b2be252eb61e91f3aac08b1e4160420e444db3e8)
#### Wednesday 2022-11-02 00:54:35 by san7890

UpdatePaths Readme - Reforged (#70806)

* UpdatePaths Readme - Reforged

I'm a bit tired after typing for the last hour so apologies if some of this stuff is unreadable. Basically, I just took time to add a small blurb about UpdatePaths in MAPS_AND_AWAY_MISSIONS.md, as well as write out examples on how you can properly use every single function UpdatePaths might have. I'm probably missing something? I think I got everything though. Let me know if I should be consistent somehow, but I did deliberately choose different test-cases per example because it's nearly impossible to come up one "generic" fit-all situation that illustrates every possible use of UpdatePaths (to my small mind).

Anyways, hope this helps.

* i fucked up with the TGM format

augh

---
## [coldud13/tgstation](https://github.com/coldud13/tgstation)@[14c96d05b8...](https://github.com/coldud13/tgstation/commit/14c96d05b82cd377dc3fe04944fdb4ece6176bd9)
#### Wednesday 2022-11-02 01:11:57 by scriptis

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
## [RigglePrime/tgstation](https://github.com/RigglePrime/tgstation)@[e5a2b0f16e...](https://github.com/RigglePrime/tgstation/commit/e5a2b0f16e2bb47b0ed60e487e3c6b2dd32f81dc)
#### Wednesday 2022-11-02 01:58:40 by LemonInTheDark

Micros the lighting subsystem (Saves a second of init) (#69838)


About The Pull Request

Micros lighting objects, and their creation

We save a good bit of time by not walking space turfs adjacent to new objects.
We also save some time with micros in the actual underlay update logic.

I swear dude we spend like 0.8 seconds of init applying the underlay. I want threaded maptick already

Micros lighting sources, and corner creation

A: Corners were being passed just A turf, and then expected to generatecorners based on that. This is pointless.
It is better to instead pass in the coords of the bottom left turf, and then build in a circle. This saves like 0.3 seconds

B: We use so many damn datum vars in corner application that we just do not need to.
This resolves that, since it pissed me off. It's pointless. Lets cache em instead

There's some misc datum var caching going on here too. Lemme see...
Oh and a bit of shortcutting for a for loop, since it was a tad expensive on its own.

Also I removed the turfs list, because it does fucking nothing. Why is this still here.

All my little optimizations save about 1 second of init I think
Not great, but not bad, and plus actual lighting work is faster now too
Why It's Good For The Game

Speed

---
## [ShizCalev/tgstation](https://github.com/ShizCalev/tgstation)@[422accbe4e...](https://github.com/ShizCalev/tgstation/commit/422accbe4e9b53f075f9a76ba6293435cb3399da)
#### Wednesday 2022-11-02 03:00:47 by John Willard

[MDB IGNORE] Shuttle engines part 2: Engines are now machines (#69793)

* Makes engines machines instead of structures

* Updates the maps

* Fixes boards and anchoring

* Removes 2 unused engine types

Router was actually used a total of once, so I just replaced it with propulsion.
I think cutting down on these useless engine types that make no difference in-game would be a nice first step to adding more functionalities to them.

* Don't use power (since shuttles dont have)

Shuttles don't have APCs, instead they just have infinite power, so I'm removing their power usage for now. I'm hoping this can be removed when unique mechanics are added to engines, because I would like them to make use of power like other machines.

* re-organizes vars

* deletes deleted dm file

* Slightly improves cargo selling code

* Renames the updatepaths

* Removes in_wall engines

I hate this stupid engine it sucks it's useless it's used solely for the tram it provides nothing of benefit to the server
replaces them with regular engines

---
## [boost-entropy-typescript/apollo-server](https://github.com/boost-entropy-typescript/apollo-server)@[c1651bfacf...](https://github.com/boost-entropy-typescript/apollo-server/commit/c1651bfacf8d310615be79e9246d7f0bd9bfa926)
#### Wednesday 2022-11-02 03:33:32 by Trevor Scheer

Integration testsuite direct dependency on Apollo Server (#7114)

The peer dependency arrangement of testsuite on server was problematic.
In one sense, it seems reasonable since we want integration authors to
bring their own AS package. However, bumping that peer dependency with
every version update is technically a breaking change - and our release
tooling (changeset) doesn't provide us a means to workaround the
behavior where it major version bumps both packages.

For correctness and compliance with our tooling, a direct dependency
addresses both concerns. We've also added an additional test which
ensures that the versions match. The test really just validates that
there's one install of @apollo/server (by using an instanceof check
against the testsuite's ApolloServer constructor and the actual instance
provided by the testsuite consumer).

Fixes #7109

<!--
First, 🌠 thank you 🌠 for taking the time to consider a contribution to
Apollo!

Here are some important details to follow:

* ⏰ Your time is important
To save your precious time, if the contribution you are making will take
more
than an hour, please make sure it has been discussed in an issue first.
          This is especially true for feature requests!
* 💡 Features
Feature requests can be created and discussed within a GitHub Issue. Be
sure to search for existing feature requests (and related issues!) prior
to
opening a new request. If an existing issue covers the need, please
upvote
that issue by using the 👍 emote, rather than opening a new issue.
* 🔌 Integrations
Apollo Server has many web-framework integrations including Express,
Koa,
Hapi and more. When adding a new feature, or fixing a bug, please take a
peak and see if other integrations are also affected. In most cases, the
fix can be applied to the other frameworks as well. Please note that,
since new web-frameworks have a high maintenance cost, pull-requests for
new web-frameworks should be discussed with a project maintainer first.
* 🕷 Bug fixes
These can be created and discussed in this repository. When fixing a
bug,
please _try_ to add a test which verifies the fix. If you cannot, you
should
still submit the PR but we may still ask you (and help you!) to create a
test.
* 📖 Contribution guidelines
Follow
https://github.com/apollographql/apollo-server/blob/main/CONTRIBUTING.md
when submitting a pull request. Make sure existing tests still pass, and
add
          tests for all new behavior.
* ✏️ Explain your pull request
Describe the big picture of your changes here to communicate to what
your
pull request is meant to accomplish. Provide 🔗 links 🔗 to associated
issues!

We hope you will find this to be a positive experience! Open source
contribution can be intimidating and we hope to alleviate that pain as
much as possible. Without following these guidelines, you may be missing
context that can help you succeed with your contribution, which is why
we encourage discussion first. Ultimately, there is no guarantee that we
will be able to merge your pull-request, but by following these
guidelines we can try to avoid disappointment.
-->

---
## [ZephyrTFA/TaleStation](https://github.com/ZephyrTFA/TaleStation)@[ab5dbb3c9e...](https://github.com/ZephyrTFA/TaleStation/commit/ab5dbb3c9e5ad774032bed641a87b3af033d9662)
#### Wednesday 2022-11-02 03:39:55 by TaleStationBot

[MIRROR] [MDB IGNORE] Fixes Some Incredulously Fucked Up Recycler Behavior (#2911)

* Fixes Some Incredulously Fucked Up Recycler Behavior (#70638)

* test one

Hey there!

Did you know that if you toss someone into a recycled emagger, that we delete _all_ of that mob's contents? You probably didn't because this shit is broken broken. Like, ow.

That's because we manually moved an item to nullspace, which caused a _slew_ of odd behavior in the Destroy chain for `obj/item` since it moves it to nullspace at a very specific point in time and makes all of it's assumptions on when you move the thing to nullspace. If it's in nullspace before you call qdel, you would shit out the ass with hanging references stuck on the mob (like `w_uniform` pointing to something in nullspace, like the image above).

All fixed now, though.

* I FUCKING LOVE UNIT TESTS

THIS SHIT WILL NEVER BREAK AGAIN!!!

* i blanked

my guy hasn't moved for twenty minutes

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

* wrong documentation

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

* Fixes Some Incredulously Fucked Up Recycler Behavior

Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [focusate/odoo](https://github.com/focusate/odoo)@[61270ee8bf...](https://github.com/focusate/odoo/commit/61270ee8bffb6e85f8ff0d19c7a3889fdce2f486)
#### Wednesday 2022-11-02 04:03:26 by qsm-odoo

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

closes odoo/odoo#104193

X-original-commit: e7c8fed8e373d7005c16c88d3a7bad6f425d13e5
Signed-off-by: Romain Derie (rde) <rde@odoo.com>
Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>

---
## [npjohnson/android_kernel_essential_msm8998](https://github.com/npjohnson/android_kernel_essential_msm8998)@[9123d7a666...](https://github.com/npjohnson/android_kernel_essential_msm8998/commit/9123d7a6666f4fed5ddd3ead6902de866d58126f)
#### Wednesday 2022-11-02 05:47:39 by Christian Brauner

BACKPORT: signal: add pidfd_send_signal() syscall

The kill() syscall operates on process identifiers (pid). After a process
has exited its pid can be reused by another process. If a caller sends a
signal to a reused pid it will end up signaling the wrong process. This
issue has often surfaced and there has been a push to address this problem [1].

This patch uses file descriptors (fd) from proc/<pid> as stable handles on
struct pid. Even if a pid is recycled the handle will not change. The fd
can be used to send signals to the process it refers to.
Thus, the new syscall pidfd_send_signal() is introduced to solve this
problem. Instead of pids it operates on process fds (pidfd).

/* prototype and argument /*
long pidfd_send_signal(int pidfd, int sig, siginfo_t *info, unsigned int flags);

/* syscall number 424 */
The syscall number was chosen to be 424 to align with Arnd's rework in his
y2038 to minimize merge conflicts (cf. [25]).

In addition to the pidfd and signal argument it takes an additional
siginfo_t and flags argument. If the siginfo_t argument is NULL then
pidfd_send_signal() is equivalent to kill(<positive-pid>, <signal>). If it
is not NULL pidfd_send_signal() is equivalent to rt_sigqueueinfo().
The flags argument is added to allow for future extensions of this syscall.
It currently needs to be passed as 0. Failing to do so will cause EINVAL.

/* pidfd_send_signal() replaces multiple pid-based syscalls */
The pidfd_send_signal() syscall currently takes on the job of
rt_sigqueueinfo(2) and parts of the functionality of kill(2), Namely, when a
positive pid is passed to kill(2). It will however be possible to also
replace tgkill(2) and rt_tgsigqueueinfo(2) if this syscall is extended.

/* sending signals to threads (tid) and process groups (pgid) */
Specifically, the pidfd_send_signal() syscall does currently not operate on
process groups or threads. This is left for future extensions.
In order to extend the syscall to allow sending signal to threads and
process groups appropriately named flags (e.g. PIDFD_TYPE_PGID, and
PIDFD_TYPE_TID) should be added. This implies that the flags argument will
determine what is signaled and not the file descriptor itself. Put in other
words, grouping in this api is a property of the flags argument not a
property of the file descriptor (cf. [13]). Clarification for this has been
requested by Eric (cf. [19]).
When appropriate extensions through the flags argument are added then
pidfd_send_signal() can additionally replace the part of kill(2) which
operates on process groups as well as the tgkill(2) and
rt_tgsigqueueinfo(2) syscalls.
How such an extension could be implemented has been very roughly sketched
in [14], [15], and [16]. However, this should not be taken as a commitment
to a particular implementation. There might be better ways to do it.
Right now this is intentionally left out to keep this patchset as simple as
possible (cf. [4]).

/* naming */
The syscall had various names throughout iterations of this patchset:
- procfd_signal()
- procfd_send_signal()
- taskfd_send_signal()
In the last round of reviews it was pointed out that given that if the
flags argument decides the scope of the signal instead of different types
of fds it might make sense to either settle for "procfd_" or "pidfd_" as
prefix. The community was willing to accept either (cf. [17] and [18]).
Given that one developer expressed strong preference for the "pidfd_"
prefix (cf. [13]) and with other developers less opinionated about the name
we should settle for "pidfd_" to avoid further bikeshedding.

The  "_send_signal" suffix was chosen to reflect the fact that the syscall
takes on the job of multiple syscalls. It is therefore intentional that the
name is not reminiscent of neither kill(2) nor rt_sigqueueinfo(2). Not the
fomer because it might imply that pidfd_send_signal() is a replacement for
kill(2), and not the latter because it is a hassle to remember the correct
spelling - especially for non-native speakers - and because it is not
descriptive enough of what the syscall actually does. The name
"pidfd_send_signal" makes it very clear that its job is to send signals.

/* zombies */
Zombies can be signaled just as any other process. No special error will be
reported since a zombie state is an unreliable state (cf. [3]). However,
this can be added as an extension through the @flags argument if the need
ever arises.

/* cross-namespace signals */
The patch currently enforces that the signaler and signalee either are in
the same pid namespace or that the signaler's pid namespace is an ancestor
of the signalee's pid namespace. This is done for the sake of simplicity
and because it is unclear to what values certain members of struct
siginfo_t would need to be set to (cf. [5], [6]).

/* compat syscalls */
It became clear that we would like to avoid adding compat syscalls
(cf. [7]).  The compat syscall handling is now done in kernel/signal.c
itself by adding __copy_siginfo_from_user_generic() which lets us avoid
compat syscalls (cf. [8]). It should be noted that the addition of
__copy_siginfo_from_user_any() is caused by a bug in the original
implementation of rt_sigqueueinfo(2) (cf. 12).
With upcoming rework for syscall handling things might improve
significantly (cf. [11]) and __copy_siginfo_from_user_any() will not gain
any additional callers.

/* testing */
This patch was tested on x64 and x86.

/* userspace usage */
An asciinema recording for the basic functionality can be found under [9].
With this patch a process can be killed via:

 #define _GNU_SOURCE
 #include <errno.h>
 #include <fcntl.h>
 #include <signal.h>
 #include <stdio.h>
 #include <stdlib.h>
 #include <string.h>
 #include <sys/stat.h>
 #include <sys/syscall.h>
 #include <sys/types.h>
 #include <unistd.h>

 static inline int do_pidfd_send_signal(int pidfd, int sig, siginfo_t *info,
                                         unsigned int flags)
 {
 #ifdef __NR_pidfd_send_signal
         return syscall(__NR_pidfd_send_signal, pidfd, sig, info, flags);
 #else
         return -ENOSYS;
 #endif
 }

 int main(int argc, char *argv[])
 {
         int fd, ret, saved_errno, sig;

         if (argc < 3)
                 exit(EXIT_FAILURE);

         fd = open(argv[1], O_DIRECTORY | O_CLOEXEC);
         if (fd < 0) {
                 printf("%s - Failed to open \"%s\"\n", strerror(errno), argv[1]);
                 exit(EXIT_FAILURE);
         }

         sig = atoi(argv[2]);

         printf("Sending signal %d to process %s\n", sig, argv[1]);
         ret = do_pidfd_send_signal(fd, sig, NULL, 0);

         saved_errno = errno;
         close(fd);
         errno = saved_errno;

         if (ret < 0) {
                 printf("%s - Failed to send signal %d to process %s\n",
                        strerror(errno), sig, argv[1]);
                 exit(EXIT_FAILURE);
         }

         exit(EXIT_SUCCESS);
 }

/* Q&A
 * Given that it seems the same questions get asked again by people who are
 * late to the party it makes sense to add a Q&A section to the commit
 * message so it's hopefully easier to avoid duplicate threads.
 *
 * For the sake of progress please consider these arguments settled unless
 * there is a new point that desperately needs to be addressed. Please make
 * sure to check the links to the threads in this commit message whether
 * this has not already been covered.
 */
Q-01: (Florian Weimer [20], Andrew Morton [21])
      What happens when the target process has exited?
A-01: Sending the signal will fail with ESRCH (cf. [22]).

Q-02:  (Andrew Morton [21])
       Is the task_struct pinned by the fd?
A-02:  No. A reference to struct pid is kept. struct pid - as far as I
       understand - was created exactly for the reason to not require to
       pin struct task_struct (cf. [22]).

Q-03: (Andrew Morton [21])
      Does the entire procfs directory remain visible? Just one entry
      within it?
A-03: The same thing that happens right now when you hold a file descriptor
      to /proc/<pid> open (cf. [22]).

Q-04: (Andrew Morton [21])
      Does the pid remain reserved?
A-04: No. This patchset guarantees a stable handle not that pids are not
      recycled (cf. [22]).

Q-05: (Andrew Morton [21])
      Do attempts to signal that fd return errors?
A-05: See {Q,A}-01.

Q-06: (Andrew Morton [22])
      Is there a cleaner way of obtaining the fd? Another syscall perhaps.
A-06: Userspace can already trivially retrieve file descriptors from procfs
      so this is something that we will need to support anyway. Hence,
      there's no immediate need to add another syscalls just to make
      pidfd_send_signal() not dependent on the presence of procfs. However,
      adding a syscalls to get such file descriptors is planned for a
      future patchset (cf. [22]).

Q-07: (Andrew Morton [21] and others)
      This fd-for-a-process sounds like a handy thing and people may well
      think up other uses for it in the future, probably unrelated to
      signals. Are the code and the interface designed to permit such
      future applications?
A-07: Yes (cf. [22]).

Q-08: (Andrew Morton [21] and others)
      Now I think about it, why a new syscall? This thing is looking
      rather like an ioctl?
A-08: This has been extensively discussed. It was agreed that a syscall is
      preferred for a variety or reasons. Here are just a few taken from
      prior threads. Syscalls are safer than ioctl()s especially when
      signaling to fds. Processes are a core kernel concept so a syscall
      seems more appropriate. The layout of the syscall with its four
      arguments would require the addition of a custom struct for the
      ioctl() thereby causing at least the same amount or even more
      complexity for userspace than a simple syscall. The new syscall will
      replace multiple other pid-based syscalls (see description above).
      The file-descriptors-for-processes concept introduced with this
      syscall will be extended with other syscalls in the future. See also
      [22], [23] and various other threads already linked in here.

Q-09: (Florian Weimer [24])
      What happens if you use the new interface with an O_PATH descriptor?
A-09:
      pidfds opened as O_PATH fds cannot be used to send signals to a
      process (cf. [2]). Signaling processes through pidfds is the
      equivalent of writing to a file. Thus, this is not an operation that
      operates "purely at the file descriptor level" as required by the
      open(2) manpage. See also [4].

/* References */
[1]:  https://lore.kernel.org/lkml/20181029221037.87724-1-dancol@google.com/
[2]:  https://lore.kernel.org/lkml/874lbtjvtd.fsf@oldenburg2.str.redhat.com/
[3]:  https://lore.kernel.org/lkml/20181204132604.aspfupwjgjx6fhva@brauner.io/
[4]:  https://lore.kernel.org/lkml/20181203180224.fkvw4kajtbvru2ku@brauner.io/
[5]:  https://lore.kernel.org/lkml/20181121213946.GA10795@mail.hallyn.com/
[6]:  https://lore.kernel.org/lkml/20181120103111.etlqp7zop34v6nv4@brauner.io/
[7]:  https://lore.kernel.org/lkml/36323361-90BD-41AF-AB5B-EE0D7BA02C21@amacapital.net/
[8]:  https://lore.kernel.org/lkml/87tvjxp8pc.fsf@xmission.com/
[9]:  https://asciinema.org/a/IQjuCHew6bnq1cr78yuMv16cy
[11]: https://lore.kernel.org/lkml/F53D6D38-3521-4C20-9034-5AF447DF62FF@amacapital.net/
[12]: https://lore.kernel.org/lkml/87zhtjn8ck.fsf@xmission.com/
[13]: https://lore.kernel.org/lkml/871s6u9z6u.fsf@xmission.com/
[14]: https://lore.kernel.org/lkml/20181206231742.xxi4ghn24z4h2qki@brauner.io/
[15]: https://lore.kernel.org/lkml/20181207003124.GA11160@mail.hallyn.com/
[16]: https://lore.kernel.org/lkml/20181207015423.4miorx43l3qhppfz@brauner.io/
[17]: https://lore.kernel.org/lkml/CAGXu5jL8PciZAXvOvCeCU3wKUEB_dU-O3q0tDw4uB_ojMvDEew@mail.gmail.com/
[18]: https://lore.kernel.org/lkml/20181206222746.GB9224@mail.hallyn.com/
[19]: https://lore.kernel.org/lkml/20181208054059.19813-1-christian@brauner.io/
[20]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[21]: https://lore.kernel.org/lkml/20181228152012.dbf0508c2508138efc5f2bbe@linux-foundation.org/
[22]: https://lore.kernel.org/lkml/20181228233725.722tdfgijxcssg76@brauner.io/
[23]: https://lwn.net/Articles/773459/
[24]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[25]: https://lore.kernel.org/lkml/CAK8P3a0ej9NcJM8wXNPbcGUyOUZYX+VLoDFdbenW3s3114oQZw@mail.gmail.com/

Cc: "Eric W. Biederman" <ebiederm@xmission.com>
Cc: Jann Horn <jannh@google.com>
Cc: Andy Lutomirsky <luto@kernel.org>
Cc: Andrew Morton <akpm@linux-foundation.org>
Cc: Oleg Nesterov <oleg@redhat.com>
Cc: Al Viro <viro@zeniv.linux.org.uk>
Cc: Florian Weimer <fweimer@redhat.com>
Signed-off-by: Christian Brauner <christian@brauner.io>
Reviewed-by: Tycho Andersen <tycho@tycho.ws>
Reviewed-by: Kees Cook <keescook@chromium.org>
Reviewed-by: David Howells <dhowells@redhat.com>
Acked-by: Arnd Bergmann <arnd@arndb.de>
Acked-by: Thomas Gleixner <tglx@linutronix.de>
Acked-by: Serge Hallyn <serge@hallyn.com>
Acked-by: Aleksa Sarai <cyphar@cyphar.com>

(cherry picked from commit 3eb39f47934f9d5a3027fe00d906a45fe3a15fad)

Conflicts:
        arch/x86/entry/syscalls/syscall_32.tbl - trivial manual merge
        arch/x86/entry/syscalls/syscall_64.tbl - trivial manual merge
        include/linux/proc_fs.h - trivial manual merge
        include/linux/syscalls.h - trivial manual merge
        include/uapi/asm-generic/unistd.h - trivial manual merge
        kernel/signal.c - struct kernel_siginfo does not exist in 4.14
        kernel/sys_ni.c - cond_syscall is used instead of COND_SYSCALL
        arch/x86/entry/syscalls/syscall_32.tbl
        arch/x86/entry/syscalls/syscall_64.tbl

(1. manual merges because of 4.14 differences
 2. change prepare_kill_siginfo() to use struct siginfo instead of
kernel_siginfo
 3. use copy_from_user() instead of copy_siginfo_from_user() in copy_siginfo_from_user_any()
 4. replaced COND_SYSCALL with cond_syscall
 5. Removed __ia32_sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_32.tbl.
 6. Replaced __x64_sys_pidfd_send_signal with sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_64.tbl.)

Bug: 135608568
Test: test program using syscall(__NR_pidfd_send_signal,..) to send SIGKILL
Change-Id: I34da11c63ac8cafb0353d9af24c820cef519ec27
Signed-off-by: Suren Baghdasaryan <surenb@google.com>
Signed-off-by: electimon <electimon@gmail.com>

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[f994fbd8ae...](https://github.com/LemonInTheDark/tgstation/commit/f994fbd8ae91c6028bac3eb528d0db3e1eb2021e)
#### Wednesday 2022-11-02 05:47:39 by LemonInTheDark

Speeds up mapload back to what it should be, roughly

Rather then instantly removing turfs from the contained_turfs list, we
enter them into a list of turfs to pull out, later.
Then we just use a getter for contained_turfs rather then a var read

This means we don't need to generate a lot of usage off removing turf by
turf from space, and can instead do it only when we need to

I've added a subsystem to manage this process as well, to ensure we
don't get any out of memory errors. It goes entry by entry, ensuring we
get no overtime.
This allows me to keep things like space clean, while keeping high
amounts of usage on a sepearate subsystem when convienient

As a part of this goal of keeping space's churn as low as possible, I've
setup code to ensure we do not add turfs to areas during a z level
increment adjacent mapload. this saves a LOT of time, but is a tad
messy

I've expanded where we use contained_turfs, including into some cases
that filter for objects in areas. need to see if this is sane or not.

Oh also I added a global area list, and replaced all non sort caring
instances of sortedAreas with it, since it seemed kinda silly

---
## [walternewtz/android_kernel_xiaomi_sdm845](https://github.com/walternewtz/android_kernel_xiaomi_sdm845)@[1c0948c50e...](https://github.com/walternewtz/android_kernel_xiaomi_sdm845/commit/1c0948c50e8e32be053f1746d68c102d2e9f80a4)
#### Wednesday 2022-11-02 06:32:18 by tanish2k09

Introducing KLapse - A kernel level livedisplay module v4.0:

Author: @tanish2k09 (email: tanish2k09.dev@gmail.com)

What is it?
Kernel-based Lapse ("K-Lapse") is a linear RGB scaling module that 'shifts' RGB based on time (of the day/selected by user), or (since v2.0) brightness. This concept is inspired from
LineageOS (formerly known as 'CyanogenMod') ROM's feature "livedisplay" which also changes the display settings (RGB, hue, temperature, etc) based on time.

Why did you decide to make this? (Tell me a story).
I (personally) am a big fan of the livedisplay feature found on LineageOS ROM. I used it every single day, since Android Lollipop. Starting from Android Nougat, a native night mode
solution was added to AOSP and it felt like livedisplay was still way superior, thanks to its various options (you could say it spoiled me, sure). I also maintained a kernel (Venom
kernel) for the device I was using at that time. It was all good until the OEM dropped support for the device at Android M, and XDA being XDA, was already working on N ROMs. The issue
was, these ROMs weren't LineageOS or based on it, so livedisplay was... gone. I decided I'll try to bring that feature to every other ROM. How would I do that? Of course! The kernel! It
worked on every single ROM, it was the key! I started to work on it ASAP and here it is, up on GitHub, licensed under GPL (check klapse.c), open to everyone :)

How does it work?
Think of it like a fancy night mode, but not really. Klapse is dependent on an RGB interface (like Gamma on MTK and KCAL on SD chipsets). It fetches time from the kernel, converts it to
local time, and selects and RGB set based on the time. The result is really smooth shifting of RGB over time.

How does it really work (dev)?
Klapse mode 1 (time-based scaling) uses a method void klapse_pulse(void) that should ideally be called every minute. This can be done by injecting a pulse call inside another method that
is called repeatedly naturally, like cpufreq or atomic or frame commits. It can be anything, whatever you like, even a kthread, as long as it is called repeatedly naturally. To execute
every 60 seconds, use jiffies or ktime, or any similar method. The pulse function fetches the current time and makes calculations based on the current hour and the values of the tunables
listed down below.

Klapse mode 2 (brightness-based scaling) uses a method void set_rgb_slider(<type> bl_lvl) where is the data type of the brightness level used in your kernel source. (OnePlus 6 uses u32
data type for bl_lvl) set_rgb_slider needs to be called/injected inside a function that sets brightness for your device. (OnePlus 6 uses dsi_panel.c for that, check out the diff for that
file in /op6)

What all stuff can it do?

1, Emulate night mode with the proper RGB settings
2, Smoothly scale from one set of RGB to another set of RGB in integral intervals over time.
3, Reduce perceived brightness using brightness_factor by reducing the amount of color on screen. Allows lower apparent brightness than system permits.
4, Scale RGB based on brightness of display (low brightness usually implies a dark environment, where yellowness is probably useful).
5, Automate the perceived brightness independent of whether klapse is enabled, using its own set of start and stop hours.
6, Be more efficient,faster by residing inside the kernel instead of having to use the HWC HAL like android's night mode.
7, (On older devices) Reduce stuttering or frame lags caused by native night mode.
8, An easier solution against overlay-based apps that run as service in userspace/Android and sometimes block apps asking for permissions.
9, Give you a Livedisplay alternative if it doesn't work in your ROM.
10, Impress your crush so you can get a date (Hey, don't forget to credit me if it works).

Alright, so this is a replacement for night mode?
NO! Not at all. One can say this is merely an alternative for LineageOS' Livedisplay, but inside a kernel. Night mode is a sub-function of both Livedisplay and KLapse. Most comparisons
here were made with night mode because that's what an average user uses, and will relate to the most. There is absolutely no reason for your Android kernel to not have KLapse. Go ahead
and add it or ask your kernel maintainer to. It's super-easy!

What can it NOT do (yet)?

1, Calculate scaling to the level of minutes, like "Start from 5:37pm till 7:19am". --TODO
2, Make coffee for you.
3, Fly you to the moon. Without a heavy suit.
4, Get you a monthly subscription of free food, cereal included.

All these following tunables are found in their respective files in /sys/klapse/

1. enable_klapse : A switch to enable or disable klapse. Values : 0 = off, 1 = on (since v2.0, 2 = brightness-dependent mode)
2. klapse_start_hour : The hour at which klapse should start scaling the RGB values from daytime to target (see next points). Values : 0-23
3. klapse_stop_hour : The hour by which klapse should scale back the RGB values from target to daytime (see next points). Values : 0-23
4. daytime_rgb : The RGB set that must be used for all the time outside of start and stop hour range.
5. target_rgb : The RGB set that must be scaled towards for all the time inside of start and stop hour range.
6. klapse_scaling_rate : Controls how soon the RGB reaches from daytime to target inside of start and stop hour range. Once target is reached, it remains constant till 30 minutes before
   stop hour, where target RGB scales back to daytime RGB.
7. brightness_factor : From the name itself, this value has the ability to bend perception and make your display appear as if it is at a lesser brightness level than it actually is at.
   It works by reducing the RGB values by the same factor. Values : 2-10, (10 means accurate brightness, 5 means 50% of current brightness, you get it)
8. brightness_factor_auto : A switch that allows you to automatically set the brightness factor in a set time range. Value : 0 = off, 1 = on
9. brightness_factor_auto_start_hour : The hour at which brightness_factor should be applied. Works only if #8 is 1. Values : 0-23
10. brightness_factor_auto_stop_hour : The hour at which brightness_factor should be reverted to 10. Works only if #8 is 1. Values : 0-23
11. backlight_range : The brightness range within which klapse should scale from daytime to target_rgb. Works only if #1 is 2. Values : MIN_BRIGHTNESS-MAX_BRIGHTNESS

Signed-off-by: Eliminater74 <eliminater74@gmail.com>
Signed-off-by: energyspear17 <energyspear17@gmail.com>
Signed-off-by: Michael <loukerismichalis@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>

---
## [Warhand/Limitless-rebirth-1.18.2](https://github.com/Warhand/Limitless-rebirth-1.18.2)@[94e6a7a99a...](https://github.com/Warhand/Limitless-rebirth-1.18.2/commit/94e6a7a99a23464c02a960efdfdc958e5e6404e1)
#### Wednesday 2022-11-02 06:43:24 by Rosie-Holstein

Update Automodlist.txt

Updated:
~Another furniture mod
~Anvil restoration
~Architectury
~Art of forging
~Blueflame
~Champions
~Collective
~Crafttweaker
~Effortless building
~Fancymenu
~Fastload
~Fast workbench
~Gateways to eternity
~Geckolib
~Iceberg lib
~Integrated dynamics and structures
~Item filters
~Jade
~JAOPCA
~Konkrete
~Legendary tooltips
~Oh the biomes you'll go
~Placebo
~Roughly enough items
~Roughly enough items additional
~Sophisticated core
~Sommuning rituals
~HT's treechop
~Voicechat
~Yungs API

Added:
+Vanillatweaks resource and datapacks
+Canary
+Continents
+Daves potioneering
+Easy magic
+Enchantment transfer
+Forgetmechunk
+FTB pack companion
+Lootbags
+Not enough crashes
+Plain grinder
+Portable mobs
+Saturn mc
+Smoothboot reloaded
+Stable anvil cost
+Universal enchants
+Villager comfort

Removed:
-Akashic tome (Feels somewhat unnecessary, might add back later)
-Bettereyes (Tested and decided it wasn't worth the addition)
-Better mending (Didn't like how it changed mending)
-Block swap (No other block swaps are needed in the pack after the removal of some other problem mods)
-Boomshot (Slimesling already introduces a similar feature and cutting mods where needed is important)
-Brewin and chewin (Wasn't a fan of the brewing system, and wanted to cull a few unused mods)
-Crayfish gun mod (Completely off theme and doesn't fit with any other mods, the only reason it stuck around this long was because my girlfriend likes this mod, but I added a few other mods she likes to make up for the removal)
-Chat mods (Small mod, removed to prune the modlist)
-Cleanview (Using vanillatweaks instead)
-Clickadv (Advancements aren't a major focus so I'm cutting this)
-Common capabilities (No mods remain that use this library)
-Cyclops core (No mods remain that use this library)
-Enchanting infuser (Felt it trivialized and usurped vanilla enchanting)
-Fast leaf decay (Vanillatweaks)
-Illuminations (Unneeded visual improvement)
-Integrated dynamics suite (Took up a lot of space and didn't add a lot of value. Manual squeezer has been replaced by plain grinder)
-Primitive multibreak (Making multibreak tools added by other mods more important)
-Pronounmc (Blue hair and pronouns removed)
-Radium (Using canary as a lithium port instead of Radium)
-Realistic bees (Didn't work super well, and needed to cut some mods)
-Silent lib (Unused library)
-Treasure bags (Was kinda jank and didn't work super well. Has been replaced by Lootbags)

---
## [peff/git](https://github.com/peff/git)@[3d2efd7668...](https://github.com/peff/git/commit/3d2efd766820ca49dd137dc688a32a015ef6e7e7)
#### Wednesday 2022-11-02 07:36:50 by Jeff King

branch: gracefully handle '-d' on orphan HEAD

When deleting a branch, "git branch -d" has a safety check that ensures
the branch is merged either to its upstream, or to HEAD. To do that,
naturally we try to resolve HEAD to a commit object. If we're on an
orphan branch (i.e., HEAD points to a branch that does not yet exist),
that will fail, and we'll bail with an error:

  $ git branch -d to-delete
  fatal: Couldn't look up commit object for HEAD

This usually isn't that big of a deal. The deletion would fail anyway,
since the branch isn't merged to HEAD, and you'd need to use "-D" (or
"-f"). And doing so skips the HEAD resolution, courtesy of 67affd5173
(git-branch -D: make it work even when on a yet-to-be-born branch,
2006-11-24).

But there are still two problems:

  1. The error message isn't very helpful. We should give the usual "not
     fully merged" message, which points the user at "branch -D". That
     was a problem even back in 67affd5173.

  2. Even without a HEAD, these days it's still possible for the
     deletion to succeed. After 67affd5173, commit 99c419c915 (branch
     -d: base the "already-merged" safety on the branch it merges with,
     2009-12-29), made it OK to delete a branch if it is merged to its
     upstream.

We can fix both by removing the die() in delete_branches() completely,
leaving head_rev NULL in this case. It's tempting to stop there, as it
appears at first glance that the rest of the code does the right thing
with a NULL. But sadly, it's not quite true.

We end up feeding the NULL to repo_is_descendant_of(). In the
traditional code path there, we call repo_in_merge_bases_many(). It
feeds the NULL to repo_parse_commit(), which is smart enough to return
an error, and we immediately return "no, it's not a descendant".

But there's an alternate code path: if we have a commit graph with
generation numbers, we end up in can_all_from_reach(), which does
eventually try to set a flag on the NULL commit and segfaults.

So instead, we'll teach the local branch_merged() to treat a NULL as
"not merged". This would be a little more elegant in in_merge_bases()
itself, but that function is called in a lot of places, and it's not
clear that quietly returning "not merged" is the right thing everywhere
(I'd expect in many cases, feeding a NULL is a sign of a bug).

There are four tests here:

  a. The first one confirms that deletion succeeds with an orphaned HEAD
     when the branch is merged to its upstream. This is case (2) above.

  b. Same, but with commit graphs enabled. Even if it is merged to
     upstream, we still check head_rev so that we can say "deleting
     because it's merged to upstream, even though it's not merged to
     HEAD". Without the second hunk in branch_merged(), this test would
     segfault.

  c. The third one confirms that we correctly say "not merged to HEAD"
     when we can't resolve HEAD, and reject the deletion.

  d. Same, but with commit graphs enabled. Without the first hunk in
     branch_merged(), this one would segfault.

Reported-by: Martin von Zweigbergk <martinvonz@google.com>

---
## [peff/git](https://github.com/peff/git)@[5dc4bb1cb5...](https://github.com/peff/git/commit/5dc4bb1cb52cdd2ba8b260b8b170f1d89d03a0b7)
#### Wednesday 2022-11-02 07:36:50 by Jeff King

ref-filter: fix parsing of signatures without blank lines

When ref-filter is asked to show %(content:subject), etc, we end up in
find_subpos() to parse out the three major parts: the subject, the body,
and the signature (if any).

When searching for the blank line between the subject and body, if we
don't find anything, we try to treat the whole message as the subject,
with no body. But our idea of "the whole message" needs to take into
account the signature, too. Since 9f75ce3d8f (ref-filter: handle CRLF at
end-of-line more gracefully, 2020-10-29), the code instead goes all the
way to the end of the buffer, which produces confusing output.

Here's an example. If we have a tag message like this:

  this is the subject
  -----BEGIN SSH SIGNATURE-----
  ...some stuff...
  -----END SSH SIGNATURE-----

then the current parser will put the start of the body at the end of the
whole buffer. This produces two buggy outcomes:

  - since the subject length is computed as (body - subject), showing
    %(contents:subject) will print both the subject and the signature,
    rather than just the single line

  - since the body length is computed as (sig - body), and the body now
    starts _after_ the signature, we end up with a negative length!
    Fortunately we never access out-of-bounds memory, because the
    negative length is fed to xmemdupz(), which casts it to a size_t,
    and xmalloc() bails trying to allocate an absurdly large value.

    In theory it would be possible for somebody making a malicious tag
    to wrap it around to a more reasonable value, but it would require a
    tag on the order of 2^63 bytes. And even if they did, all they get
    is an out of bounds string read. So the security implications are
    probably not interesting.

We can fix both by correctly putting the start of the body at the same
index as the start of the signature (effectively making the body empty).

Note that this is a real issue with signatures generated with gpg.format
set to "ssh", which would look like the example above. In the new tests
here I use a hard-coded tag message, for a few reasons:

  - regardless of what the ssh-signing code produces now or in the
    future, we should be testing this particular case

  - skipping the actual signature makes the tests simpler to write (and
    allows them to run on more systems)

  - t6300 has helpers for working with gpg signatures; for the purposes
    of this bug, "BEGIN PGP" is just as good a demonstration, and this
    simplifies the tests

Curiously, the same issue doesn't happen with real gpg signatures (and
there are even existing tests in t6300 with cover this). Those have a
blank line between the header and the content, like:

  this is the subject
  -----BEGIN PGP SIGNATURE-----

  ...some stuff...
  -----END PGP SIGNATURE-----

Because we search for the subject/body separator line with a strstr(),
we find the blank line in the subject, even though it's outside of what
we'd consider the body. But that puts us unto a separate code path,
which realizes that we're now in the signature and adjusts the line back
to "sigstart". So we're just making the "no line found at all" case
match that. And "sigstart" is always defined (if there is no signature,
it points to the end of the buffer as you'd expect).

Reported-by: Martin Englund <martin@englund.nu>

---
## [peff/git](https://github.com/peff/git)@[1fb204bb55...](https://github.com/peff/git/commit/1fb204bb5517f688b24e415ecee6b7133b90c4f5)
#### Wednesday 2022-11-02 07:36:50 by Jeff King

t5516: move plaintext-password tests from t5601 and t5516

Commit 6dcbdc0d66 (remote: create fetch.credentialsInUrl config,
2022-06-06) added tests for our handling of passwords in URLs. Since the
obvious URL to be affected is git-over-http, the tests use http. However
they don't set up a test server; they just try to access
https://localhost, assuming it will fail (because the nothing is
listening there).

This causes some possible problems:

  - There might be a web server running on localhost, and we do not
    actually want to connect to that.

  - The DNS resolver, or the local firewall, might take a substantial
    amount of time (or forever, whichever comes first) to fail to
    connect, slowing down the tests cases unnecessarily.

  - Since there's no server, our tests for "allow" and "warn" still
    expect the clone/fetch/push operations to fail, even though in the
    real world we'd expect these to succeed. We scrape stderr to see
    what happened, but it's not as robust as a more realistic test.

Let's instead move these to t5551, which is all about testing http and
where we have a real server. That eliminates any issues with contacting
a strange URL, and lets the "allow" and "warn" tests confirm that the
operation actually succeeds.

It's not quite a verbatim move for a few reasons:

  - we can drop the LIBCURL dependency; it's already part of
    lib-httpd.sh

  - we'll use HTTPD_URL_USER_PASS, etc, instead of our fake URL. To
    avoid repetition, we'll add a few extra variables.

  - the "https://username:@localhost" test uses a funny URL that
    lib-httpd.sh doesn't provide. We'll similarly construct it in a
    variable. Note that we're hard-coding the lib-httpd username here,
    but t5551 already does that everywhere.

  - for the "domain:port" test, the URL provided by lib-httpd is fine,
    since our test server will always be on an exotic port. But we'll
    confirm in the test that this is so.

  - since our message-matching is done via grep, I simplified it to use
    a regex, rather than trying to massage lib-httpd's variables.
    Arguably this makes it more readable, too, while retaining the bits
    we care about: the fatal/warning distinction, the "uses plaintext"
    message, and the fact that the password was redacted.

  - we'll use the /auth/ path for the repo, which shows that we are
    indeed making use of the auth information when needed.

  - we'll also use /smart/; most of these tests could be done via /dumb/
    in t5550, but setting up pushes there requires extra effort and
    dependencies. The smart protocol is what most everyone is using
    these days anyway.

This patch is my own, but I stole the analysis and a few bits of the
commit message from a patch by Johannes Schindelin.

---
## [xhevfx/postgres](https://github.com/xhevfx/postgres)@[8272749e8c...](https://github.com/xhevfx/postgres/commit/8272749e8ca1dbbcb5f8cf5632ec26a573ac3111)
#### Wednesday 2022-11-02 08:41:21 by Tom Lane

Record dependencies of a cast on other casts that it requires.

When creating a cast that uses a conversion function, we've
historically allowed the input and result types to be
binary-compatible with the function's input and result types,
rather than necessarily being identical.  This means that the new
cast is logically dependent on the binary-compatible cast or casts
that it references: if those are defined by pg_cast entries, and you
try to restore the new cast without having defined them, it'll fail.
Hence, we should make pg_depend entries to record these dependencies
so that pg_dump knows that there is an ordering requirement.

This is not the only place where we allow such shortcuts; aggregate
functions for example are similarly lax, and in principle should gain
similar dependencies.  However, for now it seems sufficient to fix
the cast-versus-cast case, as pg_dump's other ordering heuristics
should keep it out of trouble for other object types.

Per report from David Turoň; thanks also to Robert Haas for
preliminary investigation.  I considered back-patching, but
seeing that this issue has existed for many years without
previous reports, it's not clear it's worth the trouble.
Moreover, back-patching wouldn't be enough to ensure that the
new pg_depend entries exist in existing databases anyway.

Discussion: https://postgr.es/m/OF0A160F3E.578B15D1-ONC12588DA.003E4857-C12588DA.0045A428@notes.linuxbox.cz

---
## [IntellectualSites/FastAsyncWorldEdit](https://github.com/IntellectualSites/FastAsyncWorldEdit)@[2fe54a04b5...](https://github.com/IntellectualSites/FastAsyncWorldEdit/commit/2fe54a04b5d2b8cbb2a26947df610f3c8d4400ca)
#### Wednesday 2022-11-02 08:41:22 by Pierre Maurice Schwang

Adjust platform specific code to recent changes (#1997)

* chore: remove usage of MCUtil in StarlightRelighter

* chore: cleanup of unused imports

* hacky shit-fuckery for papers new chunksystem und refactor

* chore: address review comments

* Update dependency io.papermc.paperweight.userdev:io.papermc.paperweight.userdev.gradle.plugin to v1.3.9 (#2001)

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

* fix: suppress exceptions for field retrieval, cache fields / methods

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

---
## [ShushStudios/Shush](https://github.com/ShushStudios/Shush)@[8b8bf83b00...](https://github.com/ShushStudios/Shush/commit/8b8bf83b00586c32912028bdd02914bb362bb3d7)
#### Wednesday 2022-11-02 09:15:20 by zekrom034

Jesse, im in a notepad document jesse

My name is Walter Hartwell White. I live at 308 Negra Arroyo Lane, Albuquerque, New Mexico, 87104. This is my confession. If you're watching this tape, I'm probably dead, murdered by my brother-in-law Hank Schrader. Hank has been building a Virtual Youtuber empire for over a year now and using me as his recruiter. Shortly after my 50th birthday, Hank came to me with a rather, shocking proposition. He asked that I use my Live2D knowledge to recruit talents, which he would then hire using his connections in the Japanese utaite world. Connections that he made through his career with Niconico. I was... astounded, I... I always thought that Hank was a very moral man and I was... thrown, confused, but I was also particularly vulnerable at the time, something he knew and took advantage of. I was reeling from a cancer diagnosis that was poised to bankrupt my family. Hank took me on a ride along, and showed me just how much money even a small indie channel could make. And I was weak. I didn't want my family to go into financial ruin so I agreed. Every day, I think back at that moment with regret. I quickly realized that I was in way over my head, and Hank had a partner, a man named Motoaki "Yagoo" Tanigo, a businessman. Hank essentially sold me into servitude to this man, and when I tried to quit, Yagoo threatened my family. I didn't know where to turn. Eventually, Hank and Yagoo had a falling out. From what I can gather, Hank was always pushing for a greater share of the business, to which Yagoo flatly refused to give him, and things escalated. Yagoo was able to arrange, uh I guess I guess you call it a "hit" on my brother-in-law, and failed, but Hank was seriously injured, and I wound up paying his medical bills which amounted to a little over $177,000. Upon recovery, Hank was bent on revenge, working with a man named Riku Tazumi , he plotted to kill Yagoo, and did so. In fact, the bomb that he used was built by me, and he gave me no option in it. I have often contemplated suicide, but I'm a coward. I wanted to go to the police, but I was frightened. Hank had risen in the ranks to become the head of the Cover Corp, and about that time, to keep me in line, he took my children from me. For 3 months he kept them. My wife, who up until that point, had no idea of my vtubing activities, was horrified to learn what I had done, why Hank had taken our children. We were scared. I was in Hell, I hated myself for what I had brought upon my family. Recently, I tried once again to quit, to end this nightmare, and in response, he gave me this. I can't take this anymore. I live in fear every day that Hank will kill me, or worse, hurt my family. I... All I could think to do was to make this video in hope that the world will finally see this man, for what he really is.

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[1810b85553...](https://github.com/LemonInTheDark/tgstation/commit/1810b855536f05891593b1379e455164f45fab3a)
#### Wednesday 2022-11-02 09:30:36 by tralezab

Heretics cannot be converted, and are immune to cult stun hands. Instead, the cult is rewarded for sacrificing them with the bloody bastard sword, an oversized SPIN2WIN funblade. + Soul Stealing Fantasy Affix (#69725)

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

---
## [GeoB99/reactos](https://github.com/GeoB99/reactos)@[d5373b4eda...](https://github.com/GeoB99/reactos/commit/d5373b4eda2ebade6018baeebae3541cfc8c48f3)
#### Wednesday 2022-11-02 09:39:59 by George Bișoc

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
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[e7c8fed8e3...](https://github.com/odoo-dev/odoo/commit/e7c8fed8e373d7005c16c88d3a7bad6f425d13e5)
#### Wednesday 2022-11-02 10:22:55 by qsm-odoo

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
## [avar/git](https://github.com/avar/git)@[af668b7d7c...](https://github.com/avar/git/commit/af668b7d7c4dbf6b1f0efc7fe948a06df46019d3)
#### Wednesday 2022-11-02 11:12:12 by Ævar Arnfjörð Bjarmason

[TODO t0450] submodule: make it a built-in, remove git-submodule.sh

Replace the "git-submodule.sh" script with a built-in
"builtin/submodule.c. For" now this new command is only a dumb
dispatcher that uses run-command.c to invoke "git submodule--helper",
just as "git-submodule.sh" used to do.

This is obviously not ideal, and we should eventually follow-up and
merge the "builtin/submodule--helper.c" code into
"builtin/submodule.c". Doing it this way makes it easy to review that
this new C implementation isn't doing anything more clever than the
old shellscript implementation.

This is a large win for performance, we're now more than 4x as fast as
before in terms of the fixed cost of invoking any "git submodule"
command[1]:

	$ git hyperfine -L rev HEAD~1,HEAD -s 'make CFLAGS=-O3' './git --exec-path=$PWD submodule foreach "echo \$name"'
	Benchmark 1: ./git --exec-path=$PWD submodule foreach "echo \$name"' in 'HEAD~1
	  Time (mean ± σ):      42.2 ms ±   0.4 ms    [User: 34.9 ms, System: 9.1 ms]
	  Range (min … max):    41.3 ms …  43.2 ms    70 runs

	Benchmark 2: ./git --exec-path=$PWD submodule foreach "echo \$name"' in 'HEAD
	  Time (mean ± σ):       9.7 ms ±   0.1 ms    [User: 7.6 ms, System: 2.2 ms]
	  Range (min … max):     9.5 ms …  10.3 ms    282 runs

	Summary
	  './git --exec-path=$PWD submodule foreach "echo \$name"' in 'HEAD' ran
	    4.33 ± 0.07 times faster than './git --exec-path=$PWD submodule foreach "echo \$name"' in 'HEAD~1'

We're taking pains here to faithfully reproduce existing
"git-submodule.sh" behavior related to "--" handling, even when that
behavior is stupid. We'll fix in subsequent commits, but let's first
faithfully reproduce it.

One exception is the change in the behavior of the exit code
stand-alone "-h" and "--" yield, see the altered tests. Returning 129
instead of 0 and 1 for "-h" and "--" respectively is a concession to
basic sanity.

It would be better to use run_command() here directly to avoid copying
"args" and "env" copying, but let's use run_command_v_opt_cd_env()
instead to optimize for subsequent diff size. By using our own "struct
strvec args" we can push to "&args", not a "&cp.args". Eventually
we'll stop invoking "submodule--helper" as a sub-process, and avoid
the churn of converting all of "&cp.args" to "&args".

1. Using the "git hyperfine" wrapper for "hyperfine":
   https://lore.kernel.org/git/211201.86r1aw9gbd.gmgdl@evledraar.gmail.com/

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [harryob/cmss13](https://github.com/harryob/cmss13)@[ca2114f0f5...](https://github.com/harryob/cmss13/commit/ca2114f0f56ab4a51443bdac52053ead327724dc)
#### Wednesday 2022-11-02 11:40:52 by Mister-moon1

Removes some useless code from welding helmet (#1363)

* fuck you useless code

* you cannot hide, useless code

---
## [harryob/cmss13](https://github.com/harryob/cmss13)@[2a8ebba36a...](https://github.com/harryob/cmss13/commit/2a8ebba36a2c76ed855987dc107c9c385f6f16ea)
#### Wednesday 2022-11-02 11:40:52 by Joelampost

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
## [greenhas/spg_website](https://github.com/greenhas/spg_website)@[2dd6a0d030...](https://github.com/greenhas/spg_website/commit/2dd6a0d03087ee8b249c894a9d55f55487f10f7b)
#### Wednesday 2022-11-02 12:08:01 by Spencer Greenhalgh

post My parents are hosting (almost) everyone from my big family for Thanksgiving this year. Given growing numbers of food preferences and restrictions among us, I wonder whether we'll have a big inclusive-but-non-traditional Thursday feast or whether dinner gets balkanized.

---
## [Empire-Strikes-Back/Thanos](https://github.com/Empire-Strikes-Back/Thanos)@[7ac81008a6...](https://github.com/Empire-Strikes-Back/Thanos/commit/7ac81008a602d5396cf1f880d5cb3c47b13a3076)
#### Wednesday 2022-11-02 12:12:19 by Thanos

pie doesn't work if you won't let it

like Durant I took the wide gate to force result - and delivered evil fruit

like Patrick Baboumian I can turn the car even though I also seem to be vegan in my garden of peace

I don't follow Jesus - I chose to be a king and an elder, missed about murder, force it, least, kigdom divided

let my identity as a library - which goes against garden of programs - remain
like Griffin I see multiple futures - yet fail to bring simplicty like he does
I heard Jesus speak about resist - but I missed that either, so let me be an angry wide gate taker
I heard Jesus speak about wide gates, weeds
my name is Thanos

:James-Corden maybe it's the situation that is ugly? you're good, he's bad and - ugly

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[950bfa3cc4...](https://github.com/treckstar/yolo-octo-hipster/commit/950bfa3cc4540da89b65abba9f1146a2165dfddf)
#### Wednesday 2022-11-02 14:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[e4e615b2ed...](https://github.com/treckstar/yolo-octo-hipster/commit/e4e615b2edc5e584937da9f326d698523d34aa85)
#### Wednesday 2022-11-02 15:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [digitalmethodsinitiative/4cat](https://github.com/digitalmethodsinitiative/4cat)@[30aa4bae14...](https://github.com/digitalmethodsinitiative/4cat/commit/30aa4bae144885dd59f224e14dd4257f3c693df3)
#### Wednesday 2022-11-02 15:33:12 by Dale Wahl

oh yeah, helper for metadata
grumble stupid set hating jsons...

---
## [CourierAtoll/courieratoll.github.io](https://github.com/CourierAtoll/courieratoll.github.io)@[84c6c5009b...](https://github.com/CourierAtoll/courieratoll.github.io/commit/84c6c5009beed0418f51eb00ba1ec16c13ede6ee)
#### Wednesday 2022-11-02 16:42:25 by Courier

Did a ton of stuff. Fuck writing a summary. Fuck you.

---
## [Jackal-boop/tgstation](https://github.com/Jackal-boop/tgstation)@[99b8d6b494...](https://github.com/Jackal-boop/tgstation/commit/99b8d6b4947b6a89d13fc22e469e77c313521e79)
#### Wednesday 2022-11-02 17:38:08 by vincentiusvin

Changed Supermatter Internal Math + UI Additions (#69240)

Basically all what I'm doing is categorize and display whatever modifiers are currently applying to the SM. This way players can see powerloss, temperature generation, damage taking, temp limit adjustment etc all in live instead of diving code or looking it up in the wiki.

I have taken the liberty of making most of these modifiers additive instead of multiplicative since it's easier to illustrate how much a given modifier is doing when they are all additive. E.G: The gas you added gave you an extra 2500 joules instead of the gas you added gave you a 1.2x multiplier.

To make this job not CBT there are a few gameplay changes that are needed to make things fall into the framework and some general cleanup. Most noteworthy might be:

    Space damage taking (opted for 

SM damage and balance #66692 instead of SM can explode on space tiles again #35275 just because it's newer. Wont mind changing if asked). Also removed the power gen see the edit in
Changed Supermatter Internal Math + UI Additions #69240 (comment). Wont mind bringing it back and tweaking if asked.
SM will now use the same heat limit for everything that once used variations of it. Unified healing temp limit (influenced by psychologist) with damage heat limit (influenced by gases and low moles, yeah that's a thing). In practice this means your rock will heal at higher temps instead of the old one.
Heat output production. See:

    Changed Supermatter Internal Math + UI Additions #69240 (comment) and heat penalty from gases.
    I'm really sorry for tacking this on to this PR, but there's no good way to present the heat output effect of gases to the SM in a way I'm satisfied with if I don't do this. Kinda hard to atomize too since it relies on the cleanup. Rolled back!

Work left:

    Oh and need to make the NTOS things work.
    Ntos Done! Since the active crystal is now deprecated and we use localstate, the notification system got changed a bit. SM will now ping you if you subscribed to it. Only works when minimized and not closed, like the old one.
    Oh and also documentation.
    Think its in an ok spot now.
    Reimplement transmission view and low pressure power bonus. Yeah thats a thing.
    Looks like the low pressure power bonus is actually broken. It evaluates to ~2 for pretty much any x given. So im axing it.
    Reimplement moles doubling heat resistance. Yep thats also a thing.
    Readd the pluox and miasma pressure scaling thing.
    Done, also multiplied the reaction rate by half but multiplied the mole manipulation by 2 for pluox gen. Did this so it's easier to understand.
    Dump shit into the changelog.

Why It's Good For The Game

Future coders will now need to write a bit more code when they want to add another modifier. Meaning it's a tad more rigid if someone wants to go out of the existing framework. Also demands a little bit of math but nothing more than basic algebra.

But on the flipside, this means future coders that want to add a brand new modifier to the SM will need to justify and document it (with only a single string descriptor so its not even that much work). Makes the work of people maintaining the code waaay easier at the expense of feature coders. Also makes whatever change they want to apply be relayed immediately to the players.

I mean jesus christ we didnt even know PN was really good for SM until it's added to the wiki.
Changelog

🆑
del: Removed the broken pressure power multiplier which always evaluates to 2. Multiplied base SM power production by 2.
del: SM will no longer gain power when exposed to space. It actually used to do that, but only when the tile it's on has gas so you don't really notice it.
qol: added the factor breakdowns to the SM ui.
qol: added the gas effect breakdowns to the SM ui.
qol: Made the supermatter selection in NT CIMS ui frontend based. Notifications will be based on you pressing the bell button instead of opening a SM page.
code: Instead of showing the environment breakdown of the SM tile, the NT CIMS will show you the exact gas mixture that it uses for calculation.
code: Total moles in NT CIMS will now be substituted with absorbed moles, which is the thing we use to calculate scrung delams. Scrungs at 1800.
balance: Unified the SM taking damage on space (last modified 2018) with SM taking damage around space (added 2020, last modified 2022). Chose the latter formula, it's significantly stronger.
balance: SM will start healing at the same damage at which it stops taking heat damage. Instead of the old fixed healing at ~313K.
balance: made the low mole heat resistance thing on SM not scale with heat resistant gases.
balance: Made the supermatter temperature power gain multiplier thing linear at 1/6 instead of 50/273 or 30/273.
balance: Psychologist heat reduction is weaker on high heat gas.
refactor: rerouted how external damage (bullets) and external power (emitter) is applied to SM.
refactor: restructured the internal power calculations for SM. Power should be applied on each atmos tick instead of separately.
refactor: restructured how the SM calculates the damage that it takes. No changes expected except for the low mole temp limit multiplier thing.
refactor: Restructured SM pluox generation and miasma consumption. No changes expected though.
\🆑

---
## [clark-lindsay/fluid-habits](https://github.com/clark-lindsay/fluid-habits)@[d5d89d85da...](https://github.com/clark-lindsay/fluid-habits/commit/d5d89d85da3f7a07cb620f59d63a292ab293c383)
#### Wednesday 2022-11-02 18:52:54 by clark-lindsay

Add a credo config file, modify default nesting rule

I received a credo refactor warning about overly nested code. I
personally think that nesting does not indicate poorly factored code
in-and-of-itself, so I at least bumped up the warning threshold to > 3.
In this particular case, the code that I was being warned about is in
the `active_streak_start/1` function, but I believe that all of that
code is very tightly related and is not general purpose enough to
extract and place somewhere else; it would only have the one callsite.

My opinion has recently been changed in this regard thanks to [A
Philosophy of Software Design](https://web.stanford.edu/~ouster/cgi-bin/book.php)

---
## [FIJTeam/FIJTeam_TGStation](https://github.com/FIJTeam/FIJTeam_TGStation)@[85b2d5043d...](https://github.com/FIJTeam/FIJTeam_TGStation/commit/85b2d5043dbc9eb277bf57dd6dc5147ae08fe978)
#### Wednesday 2022-11-02 19:35:23 by LemonInTheDark

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
## [kret/metals](https://github.com/kret/metals)@[6fca4bc1b2...](https://github.com/kret/metals/commit/6fca4bc1b27e11e955a366b6251a2e8ec73ff755)
#### Wednesday 2022-11-02 19:48:08 by ckipp01

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
## [1ace/mesa](https://github.com/1ace/mesa)@[3a9cdd780d...](https://github.com/1ace/mesa/commit/3a9cdd780de28deeda45600fb5b8b134d91d17f2)
#### Wednesday 2022-11-02 22:10:50 by Alyssa Rosenzweig

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
## [LuminariMUD/Luminari-Source](https://github.com/LuminariMUD/Luminari-Source)@[35313b972a...](https://github.com/LuminariMUD/Luminari-Source/commit/35313b972a262aaf29d000545128fdd5bca6ecb8)
#### Wednesday 2022-11-02 23:46:37 by GickerLDS

-Updated the help files on most races.
-Elves are now known as moon elves. They no longer have a -2 penalty to strength and gain +1 to wisdom now in addition to the +2 to dex. They now gain the lunar magic and bathed in moonlight feats.
-Dwarves are now known as mountain dwarves. They no longer have a -2 to charisma, and gain a +2 to strength in addition to the +2 to con.  They gain light and medium armor profieciency and the encumbered resilience feat.
-Halflings are now known as lightfoot halflings. They no longer suffer a -2 penalty to strength and gain a +1 to cha in addition to the +2 to dex they have. They gain the naturally stealthy and shadow hopper feats.
-Half elves now get +2 to cha and the adaptability feat.
-Half Orcs no longer suffer -2 penalties to int and cha, and now get a +1 to con in addition to their +2 to str.  They gain the menacing, savage attacks and relentless endurance feats.
-Gnomes are now known as rock gnomes. They no longer suffer a -2 to str, and now have a +1 to con and +2 to int instead of +2 to con. They gain the tinker and artificer's lore feats.
-Half Trolls have gained an additional +2 to cha, int, wis and con.
-Arcana Golems have gained an additional +1 to cha, int and wis, and +2 to con and str.
-Drow Elves have gained an additional +2 to int and con. They also gain the drow innate magic feat.
-Duergar have gained an additional +2 to cha and str. They also gain the duergar magic feat.
-Crystal Dwarves have gained an additional +2 to dex and wis.
-Added a new race: wild elf. They gain +2 to dex and +1 to str. In addition to racial feats all elves get, they get wood elf fleetness and mask of the wild feats.
-Added the RACEFIX command.  This will allow you to gain the new racial stats and feats without having to respec.
-The race numbers for lich and vampire changed in the code.  If you log in with your lich or vampire character and their race has changed, please contact a staff member to correct the issue for you.
-Added the tinker command.
-Added the following new spells: moonbeam, minor illusion, hellish rebuke.

---

