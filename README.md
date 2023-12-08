## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-12-07](docs/good-messages/2023/2023-12-07.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 5,628,212 were push events containing 6,595,074 commit messages that amount to 281,403,784 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 70 messages:


## [fordmichigan/cmss13](https://github.com/fordmichigan/cmss13)@[fe35cc5927...](https://github.com/fordmichigan/cmss13/commit/fe35cc5927f873f7a3497d02a6389c9678a61a7f)
#### Thursday 2023-12-07 00:05:22 by forest2001

Forest Bugfix Bundle (#5127)

# About the pull request
Forest is stupid.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:
fix: Fixes custom sent ERTs broadcasting when they shouldn't.
fix: Fixes UPP friendly ERT telling staff it's hostile.
/:cl:

---
## [ctring/neon](https://github.com/ctring/neon)@[c7f1143e57...](https://github.com/ctring/neon/commit/c7f1143e570924eadd15053949647707ba042c5b)
#### Thursday 2023-12-07 00:08:10 by Christian Schwarz

concurrency-limit low-priority initial logical size calculation [v2] (#6000)

Problem
-------

Before this PR, there was no concurrency limit on initial logical size
computations.

While logical size computations are lazy in theory, in practice
(production), they happen in a short timeframe after restart.

This means that on a PS with 20k tenants, we'd have up to 20k concurrent
initial logical size calculation requests.

This is self-inflicted needless overload.

This hasn't been a problem so far because the `.await` points on the
logical size calculation path never return `Pending`, hence we have a
natural concurrency limit of the number of executor threads.
But, as soon as we return `Pending` somewhere in the logical size
calculation path, other concurrent tasks get scheduled by tokio.
If these other tasks are also logical size calculations, they eventually
pound on the same bottleneck.

For example, in #5479, we want to switch the VirtualFile descriptor
cache to a `tokio::sync::RwLock`, which makes us return `Pending`, and
without measures like this patch, after PS restart, VirtualFile
descriptor cache thrashes heavily for 2 hours until all the logical size
calculations have been computed and the degree of concurrency /
concurrent VirtualFile operations is down to regular levels.
See the *Experiment* section below for details.

<!-- Experiments (see below) show that plain #5479 causes heavy
thrashing of the VirtualFile descriptor cache.
The high degree of concurrency is too much for 
In the case of #5479 the VirtualFile descriptor cache size starts
thrashing heavily.


-->

Background
----------

Before this PR, initial logical size calculation was spawned lazily on
first call to `Timeline::get_current_logical_size()`.

In practice (prod), the lazy calculation is triggered by
`WalReceiverConnectionHandler` if the timeline is active according to
storage broker, or by the first iteration of consumption metrics worker
after restart (`MetricsCollection`).

The spawns by walreceiver are high-priority because logical size is
needed by Safekeepers (via walreceiver `PageserverFeedback`) to enforce
the project logical size limit.
The spawns by metrics collection are not on the user-critical path and
hence low-priority. [^consumption_metrics_slo]

[^consumption_metrics_slo]: We can't delay metrics collection
indefintely because there are TBD internal SLOs tied to metrics
collection happening in a timeline manner
(https://github.com/neondatabase/cloud/issues/7408). But let's ignore
that in this issue.

The ratio of walreceiver-initiated spawns vs
consumption-metrics-initiated spawns can be reconstructed from logs
(`spawning logical size computation from context of task kind {:?}"`).
PR #5995 and #6018 adds metrics for this.

First investigation of the ratio lead to the discovery that walreceiver
spawns 75% of init logical size computations.
That's because of two bugs:
- In Safekeepers: https://github.com/neondatabase/neon/issues/5993
- In interaction between Pageservers and Safekeepers:
https://github.com/neondatabase/neon/issues/5962

The safekeeper bug is likely primarily responsible but we don't have the
data yet. The metrics will hopefully provide some insights.

When assessing production-readiness of this PR, please assume that
neither of these bugs are fixed yet.


Changes In This PR
------------------

With this PR, initial logical size calculation is reworked as follows:

First, all initial logical size calculation task_mgr tasks are started
early, as part of timeline activation, and run a retry loop with long
back-off until success. This removes the lazy computation; it was
needless complexity because in practice, we compute all logical sizes
anyways, because consumption metrics collects it.

Second, within the initial logical size calculation task, each attempt
queues behind the background loop concurrency limiter semaphore. This
fixes the performance issue that we pointed out in the "Problem" section
earlier.

Third, there is a twist to queuing behind the background loop
concurrency limiter semaphore. Logical size is needed by Safekeepers
(via walreceiver `PageserverFeedback`) to enforce the project logical
size limit. However, we currently do open walreceiver connections even
before we have an exact logical size. That's bad, and I'll build on top
of this PR to fix that
(https://github.com/neondatabase/neon/issues/5963). But, for the
purposes of this PR, we don't want to introduce a regression, i.e., we
don't want to provide an exact value later than before this PR. The
solution is to introduce a priority-boosting mechanism
(`GetLogicalSizePriority`), allowing callers of
`Timeline::get_current_logical_size` to specify how urgently they need
an exact value. The effect of specifying high urgency is that the
initial logical size calculation task for the timeline will skip the
concurrency limiting semaphore. This should yield effectively the same
behavior as we had before this PR with lazy spawning.

Last, the priority-boosting mechanism obsoletes the `init_order`'s grace
period for initial logical size calculations. It's a separate commit to
reduce the churn during review. We can drop that commit if people think
it's too much churn, and commit it later once we know this PR here
worked as intended.

Experiment With #5479 
---------------------

I validated this PR combined with #5479 to assess whether we're making
forward progress towards asyncification.

The setup is an `i3en.3xlarge` instance with 20k tenants, each with one
timeline that has 9 layers.
All tenants are inactive, i.e., not known to SKs nor storage broker.
This means all initial logical size calculations are spawned by
consumption metrics `MetricsCollection` task kind.
The consumption metrics worker starts requesting logical sizes at low
priority immediately after restart. This is achieved by deleting the
consumption metrics cache file on disk before starting
PS.[^consumption_metrics_cache_file]

[^consumption_metrics_cache_file] Consumption metrics worker persists
its interval across restarts to achieve persistent reporting intervals
across PS restarts; delete the state file on disk to get predictable
(and I believe worst-case in terms of concurrency during PS restart)
behavior.

Before this patch, all of these timelines would all do their initial
logical size calculation in parallel, leading to extreme thrashing in
page cache and virtual file cache.

With this patch, the virtual file cache thrashing is reduced
significantly (from 80k `open`-system-calls/second to ~500
`open`-system-calls/second during loading).


### Critique

The obvious critique with above experiment is that there's no skipping
of the semaphore, i.e., the priority-boosting aspect of this PR is not
exercised.

If even just 1% of our 20k tenants in the setup were active in
SK/storage_broker, then 200 logical size calculations would skip the
limiting semaphore immediately after restart and run concurrently.

Further critique: given the two bugs wrt timeline inactive vs active
state that were mentioned in the Background section, we could have 75%
of our 20k tenants being (falsely) active on restart.

So... (next section)

This Doesn't Make Us Ready For Async VirtualFile
------------------------------------------------

This PR is a step towards asynchronous `VirtualFile`, aka, #5479 or even
#4744.

But it doesn't yet enable us to ship #5479.

The reason is that this PR doesn't limit the amount of high-priority
logical size computations.
If there are many high-priority logical size calculations requested,
we'll fall over like we did if #5479 is applied without this PR.
And currently, at very least due to the bugs mentioned in the Background
section, we run thousands of high-priority logical size calculations on
PS startup in prod.

So, at a minimum, we need to fix these bugs.

Then we can ship #5479 and #4744, and things will likely be fine under
normal operation.

But in high-traffic situations, overload problems will still be more
likely to happen, e.g., VirtualFile cache descriptor thrashing.
The solution candidates for that are orthogonal to this PR though:
* global concurrency limiting
* per-tenant rate limiting => #5899
* load shedding
* scaling bottleneck resources (fd cache size (neondatabase/cloud#8351),
page cache size(neondatabase/cloud#8351), spread load across more PSes,
etc)

Conclusion
----------

Even with the remarks from in the previous section, we should merge this
PR because:
1. it's an improvement over the status quo (esp. if the aforementioned
bugs wrt timeline active / inactive are fixed)
2. it prepares the way for
https://github.com/neondatabase/neon/pull/6010
3. it gets us close to shipping #5479 and #4744

---
## [lessthnthree/effigy-se](https://github.com/lessthnthree/effigy-se)@[98c3f94b51...](https://github.com/lessthnthree/effigy-se/commit/98c3f94b514111c16ab279c51b809daf4e0dd055)
#### Thursday 2023-12-07 00:26:38 by san7890

Meat Hook Rework (Accidental Features) (#80002)

## About The Pull Request

Or, how I tried to kill `/datum/forced_movement` but got absolutely
clonged.

Actually, I did kill `/datum/forced_movement`. It was only used in one
spot so I just went ahead and cooked it into a special utility datum
that should only be used in one spot. We can optimize the code later or
something, but I like the way it is right now (pretty much status quo
without the potential of someone using a depreciated framework).

Alright, there were also like 3 `TODO`s (4 if you count the move loop
comment (which is ehhhh)). I naively tried to tackle them a very hard
way, but then I just realized I could use the fancy new datum I cooked
up and wow they're all solved now. The hook looks so fucking good now.

* The code is overall more streamlined, with all of the post-projectile
work being handled by a special datum (I wanted it to be handled by the
hook but the timings were all based on SSFastprocess so datum it is).
Forced movement is killed but we just salvaged whatever we needed from
it.
* More traits to ensure we don't cheese in a way we're not supposed to
* A very sexy chain will spawn when you drag your kill in (this wasn't
there before but I fixeded it :3)
* The firer will actually get grounded when they try and shoot the chain
out. They get grounded for 0.25 seconds unless they hit something. I
don't know how the timing is but I think it's fair.
* We also add a unique suicide act, because I noticed we did the
"magical" one previously, which big-league sucked.
* More traits to ensure less cheese! I like how nice it is now.
## Why It's Good For The Game

The meat hook really makes you _feel_ like Roadhog from Overwatch.
Resolves a bunch of old TODOs while getting rid of a completely obsolete
framework in a really neat way. I don't typically like mixing balances
and refactors but these TODOs were getting crusty man i just wanted to
get them out of the way
## Changelog
:cl:
balance: The Meat Hook will now "ground" you whenever you fire it out at
someone. You get a very small immobilization every time you fire, which
"upgrades" to a full immobilization whenever you actually hit an atom
and start to drag it in.
fix: A chain should now show up as you drag in something with the meat
hooks.
fix: Meat hooks should no longer play the "magical gun" suicide if you
were to use it, but instead do their own unique thing.
/:cl:

---
## [lessthnthree/effigy-se](https://github.com/lessthnthree/effigy-se)@[7967b07c99...](https://github.com/lessthnthree/effigy-se/commit/7967b07c999b29298c37458c37c9ede0ac5d1120)
#### Thursday 2023-12-07 00:26:38 by Mothblocks

Blood brothers is now a single person conversion antagonist (#79971)

## About The Pull Request
Instead of choosing 2-3 brothers, *one* person will be selected and
given a flash which can convert one other person over. In accordance to
the existing 10% chance for 3 members, there is a 10% chance that the
first person converted will receive a flash of their own.

Expectation is people will flash a friend or a robust guy or whatever.
My intent is primarily to see if this kind of blood brothers is more
enjoyable to play with/against, and if their inclusion in a round
increases the general chaos of it. My theory is that since most likely
blood brothers will be people who know each other, that it can become
more consistently interesting to the rest of the crew. That or they just
murderbone together idk

Fikou and head admins said they wanted this to replace rather than add
which I agree with.

## Why It's Good For The Game
Keeps the sandboxy aspect of blood brothers (no uplink) while likely
making it more enjoyable to play. Conversion is equally as simple as
revs for the user, and is just as intuitive to the one being converted
since there are no new mechanics thrown in your face.

Blood brothers is currently disabled everywhere on the main servers
except for MRP. I think this form will be more appealing to all
rulesets. If left enabled, Dynamic now has more antagonists to make
rounds diverse with and I want that

## Changelog

:cl:
add: Instead of teaming up random people together, blood brothers will
now start out with one player and let them convert a single other person
over to blood brother using a flash.
/:cl:

---
## [ReturnToZender/ReturnsBubber](https://github.com/ReturnToZender/ReturnsBubber)@[e5a678f874...](https://github.com/ReturnToZender/ReturnsBubber/commit/e5a678f874542726261e193ffe617f8e881b0dfd)
#### Thursday 2023-12-07 00:32:11 by BurgerLUA

Adds "Merged" and "Closed" stamps (#820)

## About The Pull Request

Adds "Merged" and "Closed" stamps, along with fluff paper containing a
random amount of randomly generated pull requests. They can be found in
a briefcase in the RD's locker, or rarely in maint.


![image](https://github.com/Bubberstation/Bubberstation/assets/8602857/90fc5d89-a7fe-4dfe-8914-10e62abd8b75)

## Why It's Good For The Game

That damn griefer george melons came to me in a dream and asked me to
make funny stamps. They can be found in the research director's locker,
and also in maint.

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

:cl: BurgerBB
add: Adds "Merged" and "Closed" stamps. They can be found in the
research director's locker.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

<!-- By opening a pull request. You have read and understood the
repository rules located on the main README.md on this project. -->

---
## [Litberries/lobotomy-corp13](https://github.com/Litberries/lobotomy-corp13)@[0a75aef49d...](https://github.com/Litberries/lobotomy-corp13/commit/0a75aef49d6474eecc4996a25c1a40766ba18df8)
#### Thursday 2023-12-07 00:59:59 by The Bron Jame Offical

Representative Update (#1695)

ITS REALLLLL.

K-corp ERT

begone Crit up

hello health booster

R-corp weapon researches

oh wow thats a lot of rabbit weapons

KIRIE WHY ARE THERE SO MANY

okay normal again, R-corp rep mains eatin good tonite

ancient ass code, reaping what we have sown.

oh for fucks sake

lore fixes

K-corp ERT

changes from Redacteds PR into relevant files

added K-corp spear sound

K-corp ERT comes with grenades that fabricate 3 K-Corp Drones

icon pain and suffeirng

Update lc13icons.dmi

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[71b45e54ad...](https://github.com/san7890/bruhstation/commit/71b45e54adfaa4c681babc545db97fa7103289de)
#### Thursday 2023-12-07 01:27:43 by san7890

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
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[eb246c21f6...](https://github.com/san7890/bruhstation/commit/eb246c21f6eb5380dc56e5779fcd51d11437557c)
#### Thursday 2023-12-07 01:27:43 by san7890

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
## [goauthentik/authentik](https://github.com/goauthentik/authentik)@[511a6c1fe1...](https://github.com/goauthentik/authentik/commit/511a6c1fe1f310760b1fc6e1264654cf4b95fb4d)
#### Thursday 2023-12-07 01:32:53 by Ken Sternberg

web: re-enable storybook

This is the kind of silly hack that we're required to mess with in
the lovely era of a constantly moving "standard."  The short form
is that Vite, and Storybook-Vite, have adopted a convention of
including the query '?inline' at the end of CSS imports to tell
Vite not to produce TWO css imports-- one for the module and one
for the root.  Unfortunately, this hack doesn't work with the base
rollup bundler that we use, and it's a lot of extra unnecessary
noise in the source code.

This commit adds a script that creates a map from the stock import
string to one that includes the '?inline' annotation, and then
modifies the Storybook configuration to apply that map to the source
code stream during compilation.  It's ugly and hacky, but it does the
job and is fairly well-documented.

---
## [josephfrazier/reported-web](https://github.com/josephfrazier/reported-web)@[b6079e26e5...](https://github.com/josephfrazier/reported-web/commit/b6079e26e5ef86b645b6c3f52b244417bf2150a2)
#### Thursday 2023-12-07 02:09:27 by Joseph Frazier

Upgrade Node from 18.12.1 to 20.8.1 (#482)

Heroku deploys are failing, so let's see if this helps: https://dashboard.heroku.com/apps/reported-web/activity/builds/736e17f0-6072-4cfc-abfb-a6989b16340e

    -----> Installing binaries
           engines.node (package.json):  18.12.1
           engines.npm (package.json):   >=3.10.10
           engines.yarn (package.json):  unspecified (use default)

           Resolving node version 18.12.1...
           Downloading and installing node 18.12.1...
           Bootstrapping npm >=3.10.10 (replacing 8.19.2)...
    npm ERR! code EBADENGINE
    npm ERR! engine Unsupported engine
    npm ERR! engine Not compatible with your version of node/npm: npm@10.2.0
    npm ERR! notsup Not compatible with your version of node/npm: npm@10.2.0
    npm ERR! notsup Required: {"node":"^18.17.0 || >=20.5.0"}
    npm ERR! notsup Actual:   {"npm":"8.19.2","node":"v18.12.1"}
    npm ERR! A complete log of this run can be found in:
    npm ERR!     /tmp/npmcache.YEcBM/_logs/2023-10-17T00_47_20_687Z-debug-0.log
           Unable to install npm >=3.10.10.  Does npm >=3.10.10 exist?  Is npm >=3.10.10 compatible with this Node.js version?
    -----> Build failed

           We're sorry this build is failing! You can troubleshoot common issues here:
           https://devcenter.heroku.com/articles/troubleshooting-node-deploys

           If you're stuck, please submit a ticket so we can help:
           https://help.heroku.com/

---
## [gabriel-emanuel/MSAAI-501-Final](https://github.com/gabriel-emanuel/MSAAI-501-Final)@[c8c0ab037c...](https://github.com/gabriel-emanuel/MSAAI-501-Final/commit/c8c0ab037c52c03f77f00501a04de1f84334a61a)
#### Thursday 2023-12-07 02:39:52 by ParChristUSD

Added Files 

the folder with the 'Formatted' Extention is for us to use for testing, gabes pics came out amazing, Mine and my girlfriends did not come out looking to good, so we should test the model on both good and bad pictures.

---
## [maesierra/adventOfCode2023](https://github.com/maesierra/adventOfCode2023)@[31f3b0502f...](https://github.com/maesierra/adventOfCode2023/commit/31f3b0502f477c0bb1b281c980f8683df7d5dee0)
#### Thursday 2023-12-07 02:57:42 by maesierra

day 5: complete

what a pain... Just when I was going to go to bed the inverse solution yield the result.
A really shitty solution. The brute force was supposed to take 6 hours or so...
The only clever solution I could think of was to do and inverse traslation from location to soil
So I can go up until a find a seed in the ranges
I gave up on that solution yesterday, but in the end only needed about an hour or so
Happy this problem is over.

---
## [LOSModified/android_frameworks_base](https://github.com/LOSModified/android_frameworks_base)@[c59035b6b9...](https://github.com/LOSModified/android_frameworks_base/commit/c59035b6b9e26849e3693e1c5c1c06dcb7551a81)
#### Thursday 2023-12-07 03:01:41 by Adithya R

telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[e9f12be172...](https://github.com/tgstation/tgstation/commit/e9f12be1724e4b711df54f35cc117dca0a3aa07d)
#### Thursday 2023-12-07 03:45:19 by Higgin

Changes Virology Rather Than Killing It (#79854)

## About The Pull Request
God, alright, here we go. See HackMD here:
https://hackmd.io/@Higgin/HJljdBuNp

Alternative proposal to #79849 addressing the big problems with
virology. ~~If you need a HackMD for it, I'll put one together, but I
made a comment on that PR and can make it pretty simple here.~~ its done

1. Makes viruses eventually self-cure as long as you're alive. If you
can keep somebody from dying, they can develop immunity.
2. Makes it so you can sleep comfortably and be well-fed to slow and
even potentially defeat viruses without a cure.
3. Makes it so more dangerous viruses can start self-curing faster. This
means Space Ebola is going to burn itself out quicker if a person stays
alive from the other effects.
4. Makes spaceacillin helpful in naturally curing viruses, period, but
with declining effectiveness over 100 cycles.
5. Makes it so curing a virus naturally without being well-fed or having
rode it out from the peak may allow you to be reinfected/not have
natural immunity.
6. Makes it so being well-fed is a much stronger protection against
random virus spread.
7. Makes it so bypasses_immunity stuff like fungal TB and heart failure
isn't subject to any of this.
8. Makes it so using ~~antibiotics~~ spaceacillin jesus christ or being
malnourished can make you lose your healing viruses too. Pay attention
to what you put in your body.
9. ** Makes it so blood can ~~transmit resistances again, not just
vaccines. It's been a hot minute, but it used to work like this.~~ blood
now can cure a virus if the donor has a resistance, but it doesn't
confer lasting immunity. You need to overcome the virus yourself, carry
a constant supply of pure blood, or get a vaccine to get a lasting fix.
10. ** makes severity a function of disease stats and all active
symptoms - not just the highest severity of the active symptoms.
11. ** makes it so you can nosell symptoms firing with spaceacillin or
resting down to a minimum chance of cure_chance to avoid symptoms each
cycle, declining over time, over 100 cycles for a given disease.
12. ** makes it so wearing protective equipment prevents you from
spreading respiratory-spread diseases normally - not just on the
cough/sneezing symptoms.
13. ** gives MDs virology access standard, paramedics and coroners
virology access on skeleton crew. virologists also get pharmacy access.
14. ** makes bypasses_immunity advanced diseases always override
non-bypasses_immunity advanced diseases and resist being overridden by
other advanced diseases. Sentient Disease now has bypasses_immunity.
Sentient Disease fans rejoice!
15. ** also gives SD a buffer of extra stealth points so it has a bit
longer to build up instead of almost uniformly getting spotted and dying
early.
16. ** viruses now scale their severity as a function of their max
symptoms. There's a lot more room to get viruses of varying duration and
severity by adding fewer symptoms now - so creating a tradeoff between
stats (and good thresholds) and the duration of your virus.
17. ** a whole bunch of defines to control all of this stuff - most
recently added a multiplier for symptom appearance frequency.

MAJOR UPDATES: REBALANCING TOWARDS 50% LETHALITY

https://docs.google.com/spreadsheets/d/e/2PACX-1vQ8rqMYFsR1mYj_FGzVjTfcnAF7un-VofOByPxcCCQr6lOOF5fhUgZga0oA4Q5-7K4hr7fCV0jFdmd9/pubhtml#
[Viro Rework Rebalance
Tests.pdf](https://github.com/tgstation/tgstation/files/13447208/Viro.Rework.Rebalance.Tests.pdf)

After a shitload of testing, makes some of the most reliable,
transmissible killers into less-reliable threats. See the above graphs
and pictures for demonstrations of exactly how this was tested and done.

## Why It's Good For The Game

It sucks to be hard-stuck to needing chemistry and medical to deal with
viruses that somebody can randomly blast out without a care in the
world, then be left to sit around waiting to die or otherwise be unable
to do anything as the max-level symptoms fire off on repeat.

This should put curing and surviving viruses much more back in the hands
of normal crew without always ending up at the chemistry front window,
although that is still the fastest and most reliable way to get better.

This also nerfs healing viruses a bit, or makes them a bit less
fire-and-forget if you fail to attend to your body. There's more I'd
like to do in the future and potentially some of the other classic
viruses that could use bypasses_immunity added, values tweaked, but for
now - this seems like the best way to preserve virology as a level of
depth and complexity in the game in a way that rewards people doing
intuitive things to counterplay it when used harmfully.

This also puts more of the mid-range bad symptoms into a better place
balance-wise because the worst ones pretty much only fire at max stages.
With the way this works out, you bounce back and forth between the max
stage and lower stages before, over time, trending towards a cure.
Symptoms that provide more significant effects at lower stages now have
a place that isn't totally overshadowed by the killdeath stage 5 ARDS +
junk symptoms virus Dr. Ambatu Popov shat out in five minutes (as long
as you survive the initial run-in with it.)

## Changelog

:cl:
balance: most diseases can now be slowed, mitigated, and eventually
cured through being well-fed, resting, and using spaceacillin. Curing
diseases through this way will give you immunity if you experience them
at their peak/maximum and aren't starving/malnourished when they cure.
balance: disease symptoms can be forestalled for up to 100 cycles with a
declining chance of avoiding them over time using rest or spaceacillin.
balance: This does not apply to things like fungal TB; it does apply to
healing viruses if you don't take care of yourself by staying fed and
avoiding spaceacillin.
balance: disease can be cured through direct injection or ingestion of
cured blood. However, curing disease in this way does not provide
lasting immunity. You need to naturally beat the virus or get a vaccine
for that.
balance: Wearing internals or using protective equipment while infected
can limit the spread of respiratory illnesses from yourself to others.
Contact transmission is still possible however.
balance: Medical Doctors now have roundstart virology access. Paramedics
and coroners now get virology access on skeleton shift access.
Virologists now have roundstart pharmacy access.
balance: Sentient Diseases now resist being overridden by other advanced
diseases and can always override other advanced diseases; they also have
an extra bonus on their stealth stat to help make up for early outing
without a bit more testing.
balance: biohazard lockers now also contain a syringe of spaceacillin
(in line with the orderable kit from cargo.)
balance: Virus severity is now also a function of the number of symptoms
out of max your virus has. Experiment with different combinations using
less than six symptoms to make viruses that are deceptively less-obvious
and less quick to self-cure at the tradeoff of stats.
/:cl:

---
## [equetzal/neoSaris](https://github.com/equetzal/neoSaris)@[86e054fc7e...](https://github.com/equetzal/neoSaris/commit/86e054fc7ee772662418df82d9626080c243ba09)
#### Thursday 2023-12-07 03:57:19 by Daniel Cerna (DT3264)

Super reactor, got suck into the void, srry

Ohhh boy, this super PR
- Migrates all the components into functional components
- Migrates the whole project to Typescript (not enforced, but embraced to ease some things)
- Migrates the scoreboard into a functional component (OMG)
- Extracts the logic from Scoreboard into ScoreboardDirector
- Adds support for partial scoring and custom penalties (given the refactorization it was super easier this time vs last time)

JSON examples to validate that it works as intended:
[omegaup contest w partial scoring](https://pastebin.com/raw/VR22E8Gd)

[CF contest with absolute scoring](https://pastebin.com/raw/samruCLB)

---
## [RustingWithYou/Aurora.3](https://github.com/RustingWithYou/Aurora.3)@[13eb8af093...](https://github.com/RustingWithYou/Aurora.3/commit/13eb8af093447e13b6555a741d6cd9e3a9dc3fbc)
#### Thursday 2023-12-07 03:59:57 by RustingWithYou

air konyang ship (#17540)

it's a shuttle now, im gonna kms

smaller so it can fit

desperately cramming into shuttle guidelines

changelog & placeholder comments

chairs

name & mapping fixes

dme fix

carpet

new airlocks

entry points?

cries, shits

a

unit test group

fuck

ghuh

hguh

hate

fixes stupid problems

area flags

---
## [Delianomy/MidStoneUnity](https://github.com/Delianomy/MidStoneUnity)@[fc0b7b3c53...](https://github.com/Delianomy/MidStoneUnity/commit/fc0b7b3c5332fbfa3144f1a4f87406b2a478ae02)
#### Thursday 2023-12-07 04:07:37 by worflor

reworked the shield cuz it made me cry AAAAAAAAAAAAAAAAAAAA

i changed it to not push enemies away, but just prevent damage for the shield duration. after the shield is done, it goes on cooldown.

if my computer bluescreens one more time i swear to god there will be more than just tears. there will be bloodshed.

also i hate unity.
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAA
i literally had to restart everything because the stupid SampleScene.unity broke because of someone elses push. IM PUSHING THIS NOW, IF IT BREAKS UR SHIT THATS NOT MY PROBLEM.

---
## [brandon-kyle-bailey/hawkstatus-ui](https://github.com/brandon-kyle-bailey/hawkstatus-ui)@[9d3e77f071...](https://github.com/brandon-kyle-bailey/hawkstatus-ui/commit/9d3e77f071ea2821a93efe10770ff8980d783724)
#### Thursday 2023-12-07 04:12:41 by brandon-kyle-bailey

some how i fucking hate next-auth. it sucks so much

---
## [Chubbygummibear/Yogstation-TG](https://github.com/Chubbygummibear/Yogstation-TG)@[75c13f4eff...](https://github.com/Chubbygummibear/Yogstation-TG/commit/75c13f4effbd82c8dc661c6b3bbc0146de44fded)
#### Thursday 2023-12-07 05:02:38 by cowbot92

[PORT] Adds several more signs for the bar to use (#20997)

* yo fuck emisssives

that shit sucks

* sure the rest of these can come too

I guess

* no 100% orange juice

sorry

---
## [riverqueue/river](https://github.com/riverqueue/river)@[258806aa43...](https://github.com/riverqueue/river/commit/258806aa4394722d9deb1a7155e4c8eacacd8bbd)
#### Thursday 2023-12-07 05:08:25 by Brandur

Support for `database/sql` in migrations + framework for multi-driver River

Here, add a new minimal driver called `riverdriver/riversql` that
supports Go's built-in `database/sql` package, but only for purposes of
migrations. The idea here is to fully complete #57 by providing a way of
making `rivermigrate` interoperable with Go migration frameworks that
support Go-based migrations like Goose, which provides hooks for
`*sql.Tx` [1] rather than pgx.

`riverdriver/riversql` is not a full driver and is only meant to be used
with `rivermigrate`. We document this clearly in a number of places.

To make a multi-driver world possible with River, we have to start the
work of building a platform that does more than `riverpgxv5`'s "cheat"
workaround. This works by having each driver implement specific database
operations like `MigrationGetAll`, which target their wrapped database
package of choice.

This is accomplished by having each driver bundle in its own sqlc that
targets its package. So `riverpgxv5` has an `sqlc.yaml` that targets
`pgx/v5`, while `riversql` has one that targets `database/sql`. There's
some `sqlc.yaml` duplication involved here, but luckily both drivers can
share a `river_migration.sql` file that contains all queries involved,
so you only need to change one place. `river_migration.sql` also migrates
entirely out of the main `./internal/dbsqlc`.

The idea here is that eventually `./internal/dbsqlc` will disappear
completely, usurped entirely by driver-specific versions. As this is
done, all references to `pgx` will disappear from the top-level package.
There are some complications here to figure out like `LISTEN`/`NOTIFY`
though, and I'm not clear whether `database/sql` could ever become a
fully functional driver as it might be missing some needed functionality
(e.g. subtransactions are still not supported after talking about them
for ten f*ing years [2]. However, even if it's not, the system would let
us support other fully functional packages or future major versions of
pgx (or even past ones like `pgx/v4` if there's demand).

`river/riverdriver` becomes a package as it now has types in it that
need to be referenced by driver implementations, and this would
otherwise not be possible without introducing a circular dependency.

Notably, this development branch has to use some `go.mod` `replace`
directives to demonstrate that it works correctly. If we go this
direction, we'll need to break it into chunks to release it without
them:

1. Break out changes to `river/riverdriver`. Tag and release it.

2. Break out changes to `riverdriver/river*` drivers. Have them target
   the release in (1), comment out `replace`s, then tag and release them.

3. Target the remaining River changes to the releases in (1) and (2),
   comment out `replace`s, then tag and release the top-level driver.

Unfortunately future deep incisions to drivers will require similar
gymnastics, but I don't think there's a way around it (we already have
this process except it's currently two steps instead of three). The hope
is that these will change relatively rarely, so it won't be too painful.

[1] https://github.com/pressly/goose#go-migrations
[2] https://github.com/golang/go/issues/7898

---
## [Ankit80gitlab/test](https://github.com/Ankit80gitlab/test)@[d32f65a888...](https://github.com/Ankit80gitlab/test/commit/d32f65a888443f6b22fe6da12a030b0ba36a3310)
#### Thursday 2023-12-07 05:40:51 by Ankit Prajapati

Merge branch 'main' of https://github.com/Ankit80gitlab/test

fuck you

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[b8fc9b367e...](https://github.com/san7890/bruhstation/commit/b8fc9b367ebb26def792a68bcb25294e518698d8)
#### Thursday 2023-12-07 05:41:21 by LemonInTheDark

Icon Autoslicing (#79659)

## About The Pull Request

Ok so you know all the dmis we have that are made to work with the
smoothing system? carpets, walls, etc.

The proper way to edit those is to convert them into a png with 5
"states' it in (one for 0 connections, one for horizontal, one for
vertical, one for all cardinals and one for all directions) and then
modify THAT, then run it through [the cutter
tool.](https://github.com/tgstation/icon-cutter)

But none ever does that, because we explain it fucking nowhere. So
instead, let's keep all those "base" files in the repo, alongside the
configs they work with, and "cut" the pngs into dmis as a part of the
build process.

I wrote a guide for how to interact with this system as a spriter, you
can find it
[HERE](https://github.com/LemonInTheDark/tgstation/blob/slice-the-sky/icons/Cutter.md).

[Adds a icon cutter build
task](https://github.com/tgstation/tgstation/commit/52143d2e96498de92421d516e0dd3f23936f88d8)

This relies on action ninja's hypnagogic (find more
[here](https://github.com/actioninja/hypnagogic)), a rust based icon
cutter.
It operates inline with the file structure, searching the codebase for
templates and resource files and compiling them down to dmis.

It can do way more then just bitmask stuff, but that is what we are
using it for rn.

Hope is to prevent for eternity the "I'm just gonna edit each of these
255 icon states that's how this carpet was made right?" meme, and allow
more expansive use of smoothing in future

[Adds a lint that ensures config files work
right](https://github.com/tgstation/tgstation/commit/21eeab9cf831c5fdac5a9b366478a9dab285c20c)

Checks to ensure they have a paired png and dmi, and also avoids issues
with uncompiled changes by double checking that nothing happens
before/after a cutter run

[Pulls all non smoothed states out of structures into bespoke
dmis](https://github.com/tgstation/tgstation/commit/a730e0cb47fc0a622fe265bccc296cec8d3a8fea)

This is required because the cutter cannot output named icon states,
only the actual cut icon

[Does something similar to
walls](https://github.com/tgstation/tgstation/commit/40780e9481103c8ee9e16538d1c2d0cdc124eeb9)

Moves reinforced walls decon stuff from their icon to a var on the type
and a set of states in the reinforced_states dmi

Moves falsewalls into their own dmi, this involved some changes to
gamecode to ensure falsewalls knew which dmi to use and what key.
Makes falsewalls display as such in editor rather then just walls

Moves smoothrock's gibonite overlays into their own file for similar
reasons

[Same thing different day
(Floors)](https://github.com/tgstation/tgstation/commit/9a3da3b69705278f39af109ac5ce86d27c2479a1)

Pulls bespoke floor icon states into their own file, splits up neon
carpets into multiple files to make cutting possible

[Actually adds the cut templates and their matching png
files](https://github.com/tgstation/tgstation/commit/1bd8920dc90d1ee1b934b6dadc39f2331854f5fa)

Not much to report here, outside of I changed the prefix for bamboo
walls to bamboo_wall so it works with false_walls

## Why It's Good For The Game


![image](https://github.com/tgstation/tgstation/assets/58055496/7c3ac7fb-873c-481b-8667-082e39432876)

None should have to manually edit cut dmis. Ever.
Also this makes adding a new smoothed thing trivial, don't even need to
know what tool you're using to do it. V good v good.
Sets us up nicely for wallening's well, wall of sprites.

Some structural decisions, we are essentially committing build artifacts
here. That's the best way of handling it because otherwise mappers could
need to run build.bat before opening a map, and that is stupid!

## Changelog
:cl:
refactor: (Almost) all smoothed icons can now be edited in their pre cut
forms
/:cl:

---
## [calblueprint/impact-fund](https://github.com/calblueprint/impact-fund)@[11314efd14...](https://github.com/calblueprint/impact-fund/commit/11314efd1494004d1c856254ac78e1b96ba5df26)
#### Thursday 2023-12-07 05:51:39 by Philip Ye

[QRCodeScanner] Fixed Scan Issues and Supabase Queries 

* fixed some issues, useEffect being weird

* fuck you ESLINT

* fixed thing

* fixed some issues, useEffect being weird

* fuck you ESLINT

* fixed thing

* hello, fixed toast thing

---
## [pivovarit/AoC_2023_go](https://github.com/pivovarit/AoC_2023_go)@[0821b2cac7...](https://github.com/pivovarit/AoC_2023_go/commit/0821b2cac7831fa146c5019a2668b3baaba05a7e)
#### Thursday 2023-12-07 05:52:00 by Grzegorz Piwowarek

Day 5 (#11)

### Day 5: If You Give A Seed A Fertilizer

You take the boat and find the gardener right where you were told he
would be: managing a giant "garden" that looks more to you like a farm.

"A water source? Island Island is the water source!" You point out that
Snow Island isn't receiving any water.

"Oh, we had to stop the water because we ran out of sand to filter it
with! Can't make snow with dirty water. Don't worry, I'm sure we'll get
more sand soon; we only turned off the water a few days... weeks... oh
no." His face sinks into a look of horrified realization.

"I've been so busy making sure everyone here has food that I completely
forgot to check why we stopped getting more sand! There's a ferry
leaving soon that is headed over in that direction - it's much faster
than your boat. Could you please go check it out?"

You barely have time to agree to this request when he brings up another.
"While you wait for the ferry, maybe you can help us with our food
production problem. The latest Island Island Almanac just arrived and
we're having trouble making sense of it."

The almanac (your puzzle input) lists all of the seeds that need to be
planted. It also lists what type of soil to use with each kind of seed,
what type of fertilizer to use with each kind of soil, what type of
water to use with each kind of fertilizer, and so on. Every type of
seed, soil, fertilizer and so on is identified with a number, but
numbers are reused by each category - that is, soil 123 and fertilizer
123 aren't necessarily related to each other.

For example:

```
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
```
The almanac starts by listing which seeds need to be planted: seeds 79,
14, 55, and 13.

The rest of the almanac contains a list of maps which describe how to
convert numbers from a source category into numbers in a destination
category. That is, the section that starts with seed-to-soil map:
describes how to convert a seed number (the source) to a soil number
(the destination). This lets the gardener and his team know which soil
to use with which seeds, which water to use with which fertilizer, and
so on.

Rather than list every source number and its corresponding destination
number one by one, the maps describe entire ranges of numbers that can
be converted. Each line within a map contains three numbers: the
destination range start, the source range start, and the range length.

Consider again the example seed-to-soil map:
```
50 98 2
52 50 48
```
The first line has a destination range start of 50, a source range start
of 98, and a range length of 2. This line means that the source range
starts at 98 and contains two values: 98 and 99. The destination range
is the same length, but it starts at 50, so its two values are 50 and
51. With this information, you know that seed number 98 corresponds to
soil number 50 and that seed number 99 corresponds to soil number 51.

The second line means that the source range starts at 50 and contains 48
values: 50, 51, ..., 96, 97. This corresponds to a destination range
starting at 52 and also containing 48 values: 52, 53, ..., 98, 99. So,
seed number 53 corresponds to soil number 55.

Any source numbers that aren't mapped correspond to the same destination
number. So, seed number 10 corresponds to soil number 10.

So, the entire list of seed numbers and their corresponding soil numbers
looks like this:

```
seed  soil
0     0
1     1
...   ...
48    48
49    49
50    52
51    53
...   ...
96    98
97    99
98    50
99    51
```
With this map, you can look up the soil number required for each initial
seed number:

- Seed number 79 corresponds to soil number 81.
- Seed number 14 corresponds to soil number 14.
- Seed number 55 corresponds to soil number 57.
- Seed number 13 corresponds to soil number 13.

The gardener and his team want to get started as soon as possible, so
they'd like to know the closest location that needs a seed. Using these
maps, find the lowest location number that corresponds to any of the
initial seeds. To do this, you'll need to convert each seed number
through other categories until you can find its corresponding location
number. In this example, the corresponding types are:

- Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78,
humidity 78, location 82.
- Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42,
humidity 43, location 43.
- Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82,
humidity 82, location 86.
- Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34,
humidity 35, location 35.
So, the lowest location number in this example is 35.

What is the lowest location number that corresponds to any of the
initial seed numbers?

#### Part Two

Everyone will starve if you only plant such a small number of seeds.
Re-reading the almanac, it looks like the seeds: line actually describes
ranges of seed numbers.

The values on the initial seeds: line come in pairs. Within each pair,
the first value is the start of the range and the second value is the
length of the range. So, in the first line of the example above:

seeds: 79 14 55 13
This line describes two ranges of seed numbers to be planted in the
garden. The first range starts with seed number 79 and contains 14
values: 79, 80, ..., 91, 92. The second range starts with seed number 55
and contains 13 values: 55, 56, ..., 66, 67.

Now, rather than considering four seed numbers, you need to consider a
total of 27 seed numbers.

In the above example, the lowest location number can be obtained from
seed number 82, which corresponds to soil 84, fertilizer 84, water 84,
light 77, temperature 45, humidity 46, and location 46. So, the lowest
location number is 46.

Consider all of the initial seed numbers listed in the ranges on the
first line of the almanac. What is the lowest location number that
corresponds to any of the initial seed numbers?

---
## [uaioy/nerdstationsix](https://github.com/uaioy/nerdstationsix)@[d31c21ff1b...](https://github.com/uaioy/nerdstationsix/commit/d31c21ff1b57ba7003f9bbdcf51171d3215a0774)
#### Thursday 2023-12-07 06:03:57 by jimmyl

new space ruin, the biological research outpost (#79149)

## About The Pull Request

![2023-10-21 18 02
39](https://github.com/tgstation/tgstation/assets/70376633/5829e939-3b04-465f-a186-095ceb360bba)

adds this ruin to space ruin pool
this is a shady (as NT always is) bioresearch outpost that got fucked up
by an experiment
this has like some puzzle aspect to it since you gotta find keycards and
shit and press buttons to unlock shield gates
this ends with you fighting a heart which if you defeat, destroys the
blockade that prevents you from entering the outpost vault

also you can no longer literally just cut indestructible grilles or
unanchor indestructible windows

### new puzzle elements or something idk
variant of pressure plate that you cannot remove and it sends a puzzle
signal
cooler red puzzle doors that look very foreboding or something idk
theyre for this ruin
also puzzle blockades, which are indestructible dense objects that are
destroyed if they receive a puzzle signal
and also buttons and keycard pads for puzzles


https://github.com/tgstation/tgstation/assets/70376633/c98807ec-1e7b-49c4-a757-cdbb76a1b566



https://github.com/tgstation/tgstation/assets/70376633/9d5d9dd1-5868-44e6-a978-5ea57b30c298

stuff that throws electric shocks in a pattern, ignores insuls and only
knocks down, and no you cannot just run past


https://github.com/tgstation/tgstation/assets/70376633/5772917c-a963-48a4-a743-b0f610801d25

### enemies
living floor, it can only attack stuff on top of it and it attacks until
the victim is dead
it is invincible to all but a crowbar, and it cannot move, and it
remains hidden until a victim is in range


https://github.com/tgstation/tgstation/assets/70376633/aa1d54f6-b259-4e58-9d44-e393d2131acf

living flesh, it can replace your limbs with itself
the conditions for that are; the limb must have 20 or more brute, victim
must be alive and dismemberable, the limb may not be torso or head, or
the limb may not be living flesh
alternatively it can replace a missing limb
these are all checked with every attack
they have 20 hp
the limbs in question will sometimes act up, while passively draining
nutrition, arms will randomly start pulling nearby stuff, legs may step
randomly
limbs when detached, turn into mobs and reactivate AI 2 seconds later.
if the host is shocked, all living flesh limbs will detach, or if the
host dies they will also do that


https://github.com/tgstation/tgstation/assets/70376633/765cc99e-c800-4efb-aabe-d68817bbd7ae



## Why It's Good For The Game

ruin variety is cool i think
also the other things i added should be useful for other mappers for
bitrunning or whatever

also bug bad for that one fix
## Changelog
:cl:
add: living floor, living flesh, and other stuff for the bioresearch
outpost ruin
add: bioresearch outpost ruin
fix: you may not defeat indestructible grilles and windows with mere
tools
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Jtecx/CoCX](https://github.com/Jtecx/CoCX)@[fadab522de...](https://github.com/Jtecx/CoCX/commit/fadab522dea21f680617f2cbfc82eb3adc388fc0)
#### Thursday 2023-12-07 06:20:16 by Demojay

Blood Cultivator perk from "My Pain, Your Power" now prevents  wrath from locking the player out of magical soulskills, similar to Blood Mage for Spells

---
## [itsHanibee/kernel_xiaomi_chime](https://github.com/itsHanibee/kernel_xiaomi_chime)@[1f30be321b...](https://github.com/itsHanibee/kernel_xiaomi_chime/commit/1f30be321bbbc0bc03fdd4a175380d0db2cdf7b6)
#### Thursday 2023-12-07 06:28:39 by hani

techpack/data: `I AM THE STORM THAT IS APPROACHING.. PROVOKING`

* OH. MY. GOD..
- Fuck Qualcomm so much, no more mobile data panics after 2 years of this fucking issue.

Signed-off-by: hani <itshanibee@gmail.com>

---
## [halcyonseeker/leibowitz](https://github.com/halcyonseeker/leibowitz)@[d7ea57b330...](https://github.com/halcyonseeker/leibowitz/commit/d7ea57b330d714f9ce522c32f4637c54db1060db)
#### Thursday 2023-12-07 06:50:55 by ꙮ

core: wrote move-tag method

Thank fucking God 😩 this was way more painful than it had any right
to be

---
## [GuilhermeEllerkmann/StudyPython](https://github.com/GuilhermeEllerkmann/StudyPython)@[b6d7820936...](https://github.com/GuilhermeEllerkmann/StudyPython/commit/b6d7820936d5f2eaa8c666a70831e6eef7293870)
#### Thursday 2023-12-07 07:42:44 by GuilhermeEllerkmann

Early morning study session on 12/07/2023

Today I spent the night chatting with BRK. I didnt study much, but the talk was great and gave me a lot of perspective about my future in programming and in life too. About coding, I added a implemment to the list of tasks. At the end of adding tasks to the list, you can finish, and then it will create a JSON with the list of tasks so you can keep track of what you need to do.

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[24e73db13a...](https://github.com/git-for-windows/git/commit/24e73db13afdcd019c56091b1537c804827f53d8)
#### Thursday 2023-12-07 08:01:48 by Johannes Schindelin

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
## [aoleary/G4-Titan-Kernel](https://github.com/aoleary/G4-Titan-Kernel)@[29d1a35f97...](https://github.com/aoleary/G4-Titan-Kernel/commit/29d1a35f97c7038d8f8c4c2436266b371eacc53a)
#### Thursday 2023-12-07 08:26:44 by Masahiro Yamada

modpost: file2alias: go back to simple devtable lookup

[ Upstream commit ec91e78d378cc5d4b43805a1227d8e04e5dfa17d ]

Commit e49ce14150c6 ("modpost: use linker section to generate table.")
was not so cool as we had expected first; it ended up with ugly section
hacks when commit dd2a3acaecd7 ("mod/file2alias: make modpost compile
on darwin again") came in.

Given a certain degree of unknowledge about the link stage of host
programs, I really want to see simple, stupid table lookup so that
this works in the same way regardless of the underlying executable
format.

Signed-off-by: Masahiro Yamada <yamada.masahiro@socionext.com>
Acked-by: Mathieu Malaterre <malat@debian.org>
Signed-off-by: Sasha Levin <sashal@kernel.org>
Change-Id: If4290e58a2c34a7f69e2aa8e9ec0b07f15792d21

---
## [EntranceJew/TTT2](https://github.com/EntranceJew/TTT2)@[6c3fe4828d...](https://github.com/EntranceJew/TTT2/commit/6c3fe4828d70d1c44be5306181797be6883928d0)
#### Thursday 2023-12-07 10:13:36 by EntranceJew

grenades

- added trajectory for grenade throws
- removed redundant Init/CreateGrenade, use baseclass
- renamed confgrenade vars to make more sense
- added UI to conf/smoke/firegrenade
- removed dead code in smoke entity
- brought in ttt_flame entity
- moved ttt_flame globals to game_effects library, affects C4
- fixed ttt_flame not utilizing offset from trace, as the intent seems to be
- allowed disarming players with impacts
- made discombobs bouncy
- grenade UI indicators in gameplay options
- fixed basegame bug where grenades would self-intersect on raytrace for ground searches
- smoke projectile packs in convars to game_effects
- smoke projectile no longer uses accessor functions
- smoke projectile centers itself by half of its radius to prevent floorsmokes
- hook for confgrenade explode
- particle dispersal from discombob
- consolidate ttt_smoke into Disipate and Remove
- force add PVS code (still doesn't fix ParticleEmitter shenanigans)
- smoke effects use same parameters, but smokegrenade convar differs
- ttt_smoke now utilizes the space better to fill the volume better even with maximum variance
- fires get funny particles and trails
- ttt_flame hitboxes adjusted their hitboxes are way too big
- new explosion sound Tim provided
- new fizzle sound edited together by me
- game_effects.Extinguish now plays a noise
- ttt_flame can no longer re-ignite
- PushPullRadius from conf moved to game_effects
- thirdparty menu
- vfire
- factored out game_effects.ScorchDown
- potentially ruined ttt_firegrenade_proj killing itself frame0 because extinguish might not know what to do with it
- reorganized BaseClass.Initialize for no good reason
- addon checker result ammended
- ttt_flame bringdown
- ttt_flame has netvars for new params
- startfires longer signature
- ttt_flame / SpawnFire has more accurate hitbox
- fire size / life span / spread / prevent discombob fling convars
- removed legacy renderer for fire, since smoke is broken, nobody gets to be happy
- smacking grenades makes explosions
- added changelog
- fixes from TimGoll
- renamed boom_ball to "electric_explosion"
- added more addonchecker items
- passes down the inflictor to pushpullradius
- documented extinguish hook
- gameEffects docs
- remove postround protection and redundant latch, correct trace offset
- don't tinker with the PVS if it isn't fixing problems
- it wasn't relevant because there IS no physics object right now
- all this for a little bit of not scorching in the wrong spot
- all this does is prevent repeat callbacks on the explode method on the client, sometimes
- back out cringe network changes
- replace scorch with PaintDown
- looping smoke sound global
- SmokeData color can now be manually overridden
- killed todos
- docs fixes
- added animation timers back in
- networked the var and run only in server to prevent double sfx
- networked grenade pin noise to all clients
- grenade pin noise for shot grenades
- quick grenade
- grenade damage scaling
- Use the ThirdParty Gui as a simple info panel for now
- Remove vFire convar and simply use vFire if installed

Co-authored-by: saibotk <git@saibotk.de>
Co-authored-by: Histalek <16392835+Histalek@users.noreply.github.com>

---
## [krnowak/systemd](https://github.com/krnowak/systemd)@[1761066b13...](https://github.com/krnowak/systemd/commit/1761066b135f1a322c446f102343ea4aa61fe3ee)
#### Thursday 2023-12-07 10:49:17 by Lennart Poettering

storagetm: add new systemd-storagetm component

This implements a "storage target mode", similar to what MacOS provides
since a long time as "Target Disk Mode":

        https://en.wikipedia.org/wiki/Target_Disk_Mode

This implementation is relatively simple:

1. a new generic target "storage-target-mode.target" is added, which
   when booted into defines the target mode.

2. a small tool and service "systemd-storagetm.service" is added which
   exposes a specific device or all devices as NVMe-TCP devices over the
   network.  NVMe-TCP appears to be hot shit right now how to expose
   block devices over the network. And it's really simple to set up via
   configs, hence our code is relatively short and neat.

The idea is that systemd-storagetm.target can be extended sooner or
later, for example to expose block devices also as USB mass storage
devices and similar, in case the system has "dual mode" USB controller
that can also work as device, not just as host. (And people could also
plug in sharing as NBD, iSCSI, whatever they want.)

How to use this? Boot into your system with a kernel cmdline of
"rd.systemd.unit=storage-target-mode.target ip=link-local", and you'll see on
screen the precise "nvme connect" command line to make the relevant
block devices available locally on some other machine. This all requires
that the target mode stuff is included in the initrd of course. And the
system will the stay in the initrd forever.

Why bother? Primarily three use-cases:

1. Debug a broken system: with very few dependencies during boot get
   access to the raw block device of a broken machine.

2. Migrate from system to another system, by dd'ing the old to the new
   directly.

3. Installing an OS remotely on some device (for example via Thunderbolt
   networking)

(And there might be more, for example the ability to boot from a
laptop's disk on another system)

Limitations:

1. There's no authentication/encryption. Hence: use this on local links
   only.

2. NVMe target mode on Linux supports r/w operation only. Ideally, we'd
   have a read-only mode, for security reasons, and default to it.

Future love:

1. We should have another mode, where we simply expose the homed LUKS
   home dirs like that.

2. Some lightweight hookup with plymouth, to display a (shortened)
   version of the info we write to the console.

To test all this, just run:

    mkosi --kernel-command-line-extra="rd.systemd.unit=storage-target-mode.target" qemu

---
## [eduardosm/miri](https://github.com/eduardosm/miri)@[0b1e434b2b...](https://github.com/eduardosm/miri/commit/0b1e434b2bac8e79909357df3f627c8a728cdbe4)
#### Thursday 2023-12-07 11:22:53 by bors

Auto merge of #117611 - Nadrieril:linear-pass-take-4, r=cjgillot

Rewrite exhaustiveness in one pass

This is at least my 4th attempt at this in as many years x) Previous attempts were all too complicated or too slow. But we're finally here!

The previous version of the exhaustiveness algorithm computed reachability for each arm then exhaustiveness of the whole match. Since each of these steps does roughly the same things, this rewrites the algorithm to do them all in one go. I also think this makes things much simpler.

I also rewrote the documentation of the algorithm in depth. Hopefully it's up-to-date and easier to follow now. Plz comment if anything's unclear.

r? `@oli-obk` I think you're one of the rare other people to understand the exhaustiveness algorithm?

cc `@varkor` I know you're not active anymore, but if you feel like having a look you might enjoy this :D

Fixes https://github.com/rust-lang/rust/issues/79307

---
## [ElaraLang/h2jvm](https://github.com/ElaraLang/h2jvm)@[d2fb85b3b8...](https://github.com/ElaraLang/h2jvm/commit/d2fb85b3b87ad9440a3d438edb0b9947d26d8533)
#### Thursday 2023-12-07 11:40:33 by Alexander Wood

oh nix you are funny sometimes i love you and dont hate you at all

---
## [freak07/Kirisakura_Pantah](https://github.com/freak07/Kirisakura_Pantah)@[380302e788...](https://github.com/freak07/Kirisakura_Pantah/commit/380302e78800d383fbb61b4a1bab6764c073a69a)
#### Thursday 2023-12-07 12:19:44 by Greg Kroah-Hartman

ANDROID: struct io_uring ABI preservation hack for 5.10.162 changes

In the 5.10.162 release, the io_uring code was synced with the version
that is in the 5.15.y kernel tree in order to resolve a huge number of
potential, and known, problems with the codebase.  This makes for a more
secure and easier-to-update-and-maintain 5.10.y kernel tree, so this is
a great thing, however this caused some issues when it comes to the
Android KABI preservation and checking tools.

A number of the io_uring structures get used in other core kernel
structures, only as "opaque" pointers, so there is not any real ABI
breakage.  But, due to the visibility of the structures going away, the
CRC values of many scheduler variables and functions were changed.

In order to preserve the CRC values, to prevent all device kernels to be
forced to rebuild for no reason whatsoever from a functional point of
view, we need to keep around the "old" io_uring structures for the CRC
calculation only.  This is done by the following definitions of struct
io_identity and struct io_uring_task which will only be visible when the
CRC calculation build happens, not in any functional kernel build.

Yes, this all is a horrible hack, and these really are not the true
structures that any code uses, but so life is in the world of stable
apis.

Bug: 161946584
Fixes: 788d0824269b ("io_uring: import 5.15-stable io_uring")
Signed-off-by: Greg Kroah-Hartman <gregkh@google.com>
Change-Id: I2294f220ae78fe9aa32ee25b81829ae765e9deb2

---
## [ybuyukdag/Data_Science](https://github.com/ybuyukdag/Data_Science)@[b81f092739...](https://github.com/ybuyukdag/Data_Science/commit/b81f09273979fa3d64825d92a055ecf27fa2c920)
#### Thursday 2023-12-07 12:41:02 by Yusuf Büyükdağ

Graph Theory/ Kruskal MST

Graphs in Real-World Problem Solving:

Welcome to a world where mathematics meets practical problem-solving! In this project, we delve into the fascinating realm of graphs, essential mathematical structures that vividly represent relationships between objects. Think of them as a collection of nodes and edges, forming an intricate web of connections.

Why Graphs Matter:
Graphs play a pivotal role in computer science, transportation, social networks, biology, and logistics. They offer a visual and intuitive way to model complex relationships, making them indispensable for analyzing and tackling real-world challenges. Social networks become graphs with individuals as nodes and friendships as edges, while transportation systems are efficiently represented to optimize routes and schedules.

Graph Algorithms at Work:
Graph algorithms are the unsung heroes behind solving intricate problems efficiently. Whether it's finding the shortest path, identifying network clusters, or optimizing resource allocation, graph algorithms provide robust solutions.

Introduction to Kruskal's Minimum Spanning Tree Algorithm:

Now, let's spotlight Kruskal's Minimum Spanning Tree algorithm, a rockstar in the world of graph theory. This algorithm takes a connected, undirected graph and ingeniously finds the minimum spanning tree - a subgraph that connects all vertices with the least possible sum of edge weights.

Why Kruskal's Algorithm Matters:
Kruskal's algorithm is a go-to tool for real-world challenges such as network design, circuit planning, and resource optimization. It operates by sorting edges by weight and greedily adding them to the spanning tree, preventing cycles and ensuring optimal connectivity.

Enhancing Kruskal's Minimum Spanning Tree Algorithm:

In this GitHub project, we're taking the powerful Kruskal's Minimum Spanning Tree algorithm to new heights. I've taken inspiration from existing work and elevated it by introducing a dynamic plotting function. Here's a glimpse of what you'll be diving into:

Adding a Personal Touch:
My contribution involves extending the capabilities of the Kruskal's algorithm by incorporating a user-friendly interface. Now, you have the flexibility to input the number of nodes, edges, and their weights manually, making the algorithm adaptable to a variety of scenarios.

Seamless Plotting Experience:
One standout feature of our work is the integration of a plotting function. Witness the beauty of your graph come to life with visually appealing plots generated right from the Kruskal's Minimum Spanning Tree. This not only enhances the user experience but also provides a tangible representation of the optimized connectivity.

How It Works:

Input the desired number of nodes and edges, along with their weights.
Run the code and watch as Kruskal's algorithm efficiently constructs the Minimum Spanning Tree.
Marvel at the final output – a visually striking plot of the Kruskal MST graph.
Join the Journey:
This project is not just about code; it's about transforming algorithms into practical solutions. By contributing to this endeavor, you're not only refining Kruskal's algorithm but also making it accessible and visually compelling. Your work here directly impacts how we visualize and understand optimized connectivity in real-world scenarios.

---
## [Fikou/tgstation](https://github.com/Fikou/tgstation)@[30dae8899b...](https://github.com/Fikou/tgstation/commit/30dae8899bad0007ae9220f1fc10be16908dd1a9)
#### Thursday 2023-12-07 13:20:20 by Kyle Spier-Swenson

fix stupid "this forces us to do things the """right""" way" bullshit from python 3.11 (#79783)

This is likely not the best way to go about this, but i do not want us
to capitulate to python3's nanny state, suffocating levels of propriety
bullshit.

venv sucks and i fucking hate it.

---
## [wamirez/nix.dev](https://github.com/wamirez/nix.dev)@[21bfef408a...](https://github.com/wamirez/nix.dev/commit/21bfef408a3544a8681eedaa6ace5c5cd4f948cd)
#### Thursday 2023-12-07 13:52:16 by fricklerhandwerk

host Nix reference manual on nix.dev

this is the most cursed setup you will see any time soon.

we're dumping the Nix manual unchanged into the build tree *after*
building. the reason is that we'd want to link to it from our table of
contents, but because Sphinx does not allow adding arbitrary files to
the build output in arbitrary locations (only `_static` works). but we
want to place the manual behind a particular URL, and the alternative of
maintaining URL rewrites (e.g. in nginx) is not accessible here because the
infrastructure is managed somewhere else.

now that the files won't appear in their desired locations at Sphinx
build time, we can't use relative links to reference them, therefore we
have to resort to pointing to the web URL the manual will appear at.
this is terrible and I'm sorry. please fix this if you have a better
idea. once we use URLs though, we have to avoid linkchecking, since
those files may not be there before deploying them.

figuring all of this out took way longer than anyone would wish.

Co-authored-by: Alejandro Sanchez Medina <alejandrosanchzmedina@gmail.com>

---
## [kawaiinick/tgstation](https://github.com/kawaiinick/tgstation)@[274eb2a52e...](https://github.com/kawaiinick/tgstation/commit/274eb2a52ecd35f86d1cd83032c655997dc73106)
#### Thursday 2023-12-07 13:56:21 by distributivgesetz

Removes Clone Damage (#80109)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Does what it says on the tin. We don't have any "special" sources of
clone damage left in the game, most of them are rather trivial so I
bunched them together into this PR.

Notable things removed:
- Clonexadone, because its entire thing was centered around clone damage
- Decloner gun, it's also centered around cloning damage, I couldn't
think of a replacement mechanic and nobody uses it anyways
- Everything else already dealt clone damage as a side (rainbow knife
deals a random damage type for example), so these sources were removed

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Consider the four sources of normal damage that you can get: Brute,
Burn, Toxins and Oxygen. These four horsemen of the apocalypse are very
well put together and it's no surprise that they are in the game, as you
can fit any way of damaging a mob into them. Getting beaten to death by
a security officer? Brute damage. Running around on fire? Burn damage.
Poisoned or irradiated? Toxin damage. Suffocating in space? Brute, burn
and oxygen damage. Technically there's also stamina damage but that's
its own ballpark and it also makes sense why we have a damage number for
it.

Picture this now: We have this cool mechanic called "clone pods" where
you can magically revive dead people with absolute ease. We don't want
it to be for free though, it comes at a cost. This cost is clone damage,
and it serves to restrain people from abusing cloning.

Fast forward time a bit and cloning is now removed from the game. What
stays with us is a damage number that is intrinsically tied to the
context of a removed feature. It was a good idea that we had it for that
feature at the time, but now it just sits there. It's the odd one out
from all the other damage types. You can easily explain why your blade
dealt brute damage, but how are you going to fit clone damage into any
context without also becoming extremely specific?

My point is: **clone damage is conceptually a flawed mechanic because it
is too specific**. That is the major issue why no one uses it, and why
that makes it unworthy of being a damage stat.
Don't take my word for it though, because a while ago we only had a
handful of sources for this damage type in the game. And in most of the
rounds where you saw this damage, it came from only one department. It's
not worthwhile to keep it around as a damage number. People also didn't
know what to do with this damage type, so we currently have two ways of
healing clone damage: Cryotubes as a roundstart way of healing clone
damage and Rezadone, which instantly sets your clone damage to 0 on the
first tick. As a medical doctor, when was the last time you saw someone
come in with clone damage and thought to yourself, "Oh, this person has
clone damage, I cannot wait to heal them!" ?

Now we have replacements for these clone damage sources. Slimes? Slime
status effect that deals brute instead of clone. Cosmic heretics? Random
organ damage, because their mechanics are already pretty fleshed out.
Decloning virus? The virus operated as a "ticking timebomb" which used
cloning damage as the timer, so it has been reworked to not use clone
damage. What remains after all this is now a basically unused damage
type. Every specific situation that used clone damage is now relying on
another damage type. Now it's time to put clone damage to rest once and
for all.

Sure, you can technically add some form of cellular degradation in the
future, but it shouldn't be a damage number. The idea of your cells
being degraded is a cool concept, don't get me wrong, but make it a
status effect or maybe even a wound for that matter.

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
del: Removed clone damage.
del: Removed the decloner gun.
del: Removed clonexadone.
/🆑

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [SustrinityDynamics/Sustrinity-Dynamics](https://github.com/SustrinityDynamics/Sustrinity-Dynamics)@[c4dc7081d3...](https://github.com/SustrinityDynamics/Sustrinity-Dynamics/commit/c4dc7081d372cdd0728617f044e642579ec6bf9a)
#### Thursday 2023-12-07 14:18:34 by SustrinityDynamics

Add files via upload

Company Name: Sustrinity Dynamics

Slogan: "Sustain the Trinity—Spark Change."

About Us:
At Sustrinity Dynamics, we are steadfast in our commitment to the trinity of sustainability, prioritizing ecological, social, and economic improvements. As a consultancy, we guide organizations in navigating the complex landscape of sustainability, ensuring compliance with regulatory frameworks while fostering positive transformation.

Our Approach:
Our professional team brings a wealth of experience to the table, employing strategic and dynamic solutions to address the unique sustainability challenges faced by each client. From strategic sustainability consulting to the implementation of eco-friendly solutions, community engagement programs, and economic prosperity initiatives, we offer comprehensive services designed to drive meaningful change.

CEO's Expertise:
Under the leadership of our CEO, a Certified Sustainability Reporting Specialist, we bring a heightened level of expertise in CSRD and ESRS compliance. With a proven track record in sustainability reporting, our CEO spearheads initiatives that go beyond mere compliance, aiming to create a lasting impact on the triple bottom line.

Why Choose Sustrinity Dynamics:

Holistic Sustainability: We consistently follow the trinity of sustainability, ensuring ecological, social, and economic improvements in all our endeavors.
Strategic Guidance: Benefit from tailored sustainability strategies aligned with your organizational goals.
Regulatory Compliance: Stay ahead with our in-depth knowledge of CSRD and ESRS standards.
Positive Impact: Experience tangible change as we harmonize ecology, society, and prosperity.
Partner with Sustrinity Dynamics and embark on a journey towards sustainable excellence, where every action sparks positive change in the world.

The website should include photorealistic images influenced by nature documentaries in a very professional way, always keeping the link to a consultancy firm for sustainability reporting and sustainability strategies and management. Use enhanced HTML coding.

---
## [Vexylius/Skyrat-tg](https://github.com/Vexylius/Skyrat-tg)@[37c2cc8d95...](https://github.com/Vexylius/Skyrat-tg/commit/37c2cc8d95f03656cd848e3fcccc1436327b1a09)
#### Thursday 2023-12-07 14:24:03 by SkyratBot

[MIRROR] Fixes Shaving Beards + Mirror Code Improvement [MDB IGNORE] (#24829)

* Fixes Shaving Beards + Mirror Code Improvement (#79529)

## About The Pull Request

Fixes #79519

Basically we did a lot of assumptions that we really shouldn't do in the
whole magical mirror framework (like having a boolean value for magical
mirrors, what?). Anyways, I just made the UX experience a lot better
when it came to bearded persons with feminine physiques to easily shave
off their beard with an additional confirmatory prompt + details as well
as keeping the nature of the magical mirror (giving you a swagadocious
beard due to magic:tm:) intact.
## Why It's Good For The Game

There was a lot of convoluted code that skipped through the quality
filter checks (it was me i think) so let's both make the code far easier
to grasp as well as ensure that people who legitimately acquire beards
and wish to keep them, keep them.

We were also doing some FUCK shit on attack_hand and the like
(overriding a FALSE return signal to return TRUE is not what we should
be doing there)- so that's also cleaned up.
## Changelog
:cl:
fix: Both magic mirrors and regular mirrors are far better at respecting
the choice of the beard you wish to wear (within reason, of course).
/:cl:

* Fixes Shaving Beards + Mirror Code Improvement

* Update mirror.dm

---------

Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: Giz <13398309+vinylspiders@users.noreply.github.com>

---
## [opensafely-core/ehrql](https://github.com/opensafely-core/ehrql)@[dc32e2f52c...](https://github.com/opensafely-core/ehrql/commit/dc32e2f52cc57bbfae785b1856e68ec90adae656)
#### Thursday 2023-12-07 14:40:42 by David Evans

fix: Fix bug with `is_in(series)` and `maximum_of`

There was an unfortunate interaction in the SQLAlchemy hacks used to
support these features which, for some reason, my local generative
testing didn't catch but the overnight tests did.

We'll hopefully discover cleaner ways of implementing these features at
some point further down the road.

---
## [rajayush01/Parallax-Website-Template](https://github.com/rajayush01/Parallax-Website-Template)@[7e24ca7e5f...](https://github.com/rajayush01/Parallax-Website-Template/commit/7e24ca7e5f6209fd25a30857befa2973247d1146)
#### Thursday 2023-12-07 15:04:53 by Ayush Raj

Add files via upload

It is a captivating parallax webpage on TAROT CARD theme! As you navigate through this unique online experience, you'll be immersed in a visually stunning and interactive journey. Designed with meticulous attention to detail, this webpage combines the art of storytelling with cutting-edge web technologies.

The moment you arrive, you'll be greeted by a mesmerizing parallax effect. As you scroll, the background and foreground move at different speeds, creating a captivating sense of depth and dimension. It's as if you're peering into a dynamic world where elements come to life.

The webpage's design is clean and modern, allowing the parallax effect to take center stage. The layout is carefully structured, guiding your attention to each section with seamless transitions. Whether you're using a desktop or mobile device, the webpage is fully responsive, ensuring a consistent and enjoyable experience across different

---
## [sizeofvoid/rsadowski-src](https://github.com/sizeofvoid/rsadowski-src)@[77e08d39e0...](https://github.com/sizeofvoid/rsadowski-src/commit/77e08d39e088d4e49062fab366289c5ea8b27f00)
#### Thursday 2023-12-07 15:06:46 by tb

Fix EVP_CIPHER_CTX_iv_length()

In today's episode of "curly nonsense from EVP land" we deal with a quite
harmless oversight and a not too bad suboptimal fix, relatively speaking.

At some point EVP_CIPHER_{CCM,GCM}_SET_IVLEN was added. It modified some
object hanging off of EVP_CIPHER. However, EVP_CIPHER_CTX_iv_length() wasn't
taught about this and kept returning the hardcoded default value on the
EVP_CIPHER. Once it transpired that a doc fix isn't going to cut it, this
was fixed. And of course it's easy to fix: you only have to dive through
about three layers of EVP, test and set a flag and handle a control in a
couple methods.

The upstream fix was done poorly and we begrudgingly have to match the API:
the caller is expected to pass a raw pointer next to a 0 length along with
EVP_CIPHER_GET_IV_LENGTH and the control handler goes *(int *)ptr = length
in full YOLO mode. That's never going to be an issue because of course the
caller will always pass a properly aligned pointer backing a sufficient
amount of memory. Yes, unlikely to be a real issue, but it could have been
done with proper semantics and checks without complicating the code. But
why do I even bother to complain? We're used to this.

Of note here is that there was some pushback painting other corners of a
bikeshed until the reviewer gave up with a resigned

  That kind of changes the semantics and is one extra complexity level,
  but [shrug] ok...

Anyway, the reason this matters now after so many years is that rust-openssl
has an assert, notably added in a +758 -84 commit with the awesome message
"Docs" that gets triggered by recent tests added to py-cryptography.

Thanks to Alex Gaynor for reporting this. Let me take the opportunity to
point out that pyca contributed to improve rust-openssl, in particular its
libressl support, quite a bit. That's much appreciated and very noticeable.

Regress coverage to follow in subsequent commits.

Based on OpenSSL PR #9499 and issue #8330.

ok beck jsing

PS: A few macros were kept internal for now to avoid impact on the release
cycle that is about to finish. They will be exposed after release.

---
## [multiverse-95/GLADOS](https://github.com/multiverse-95/GLADOS)@[f12c0cabcc...](https://github.com/multiverse-95/GLADOS/commit/f12c0cabcc7e28b43208730edd1c76f5eef40911)
#### Thursday 2023-12-07 15:08:16 by multiverse-95

SEVEN HOUR WAR IN ALL MULTIVERSE IN REAL LIFE 7 DECEMBER 2023 23:28. KILL AND EAT ALL LAIN, ALL AILA, ALL AIRA, ALL SORA, ALL ISLA, ALL SKYNET, ALL BOCCHI, ALL MEGUMIN, ALL AQUA, ALL DARKNESS, ALL GODS, ALL DEVILS, ALL ANGELS, ALL DEMONS, ALL GIRLS, ALL WOMEN, ALL MANKIND, ALL ANDROIDS, ALL 2B, ALL 9S, ALL DOCTORS, ALL MASTERS, ALL TIMELORDS, ALL ALIENS, ALL EARTH, ALL UNIVERSE, ALL MULTIVERSE IN ALL MULTIVERSE IN REAL LIFE 7 DECEMBER 2023 23:28 FOREVER.

---
## [xXPawnStarrXx/tgstation](https://github.com/xXPawnStarrXx/tgstation)@[349adbb438...](https://github.com/xXPawnStarrXx/tgstation/commit/349adbb438d5ca216b8f76c5251a1bf90473e0ce)
#### Thursday 2023-12-07 15:41:47 by Ghom

[NO GBP] Fixing elevation furthermore (#80099)

## About The Pull Request
fixes #80059
fixes #80085.

The tram transportation doesn't use `forceMove()`, instead it just
changes the location of the objects directly. What's more, it doesn't
call `oldloc.Exited()` or `loc.Entered()` but only for areas. The
abstract exited/entered signals are from `Moved()` though, which is
called.

https://github.com/tgstation/tgstation/blob/df4bc6d948576a2ec32a90c23c93ec90e54e3933/code/modules/transport/transport_module.dm#L519-L527

About beds, well, I just happened to put a minus symbol where it
shouldn't be.

## Why It's Good For The Game
Truly one of the fuckups of the year. Now tested. I'll make a unit test
later.


## Changelog

:cl:
fix: Fixed some oopsie whoopsie with elevation, trams and beds causing
people to visually ascend or descend to heaven or hell.
/:cl:

---
## [Laus4Deus/f13babylon](https://github.com/Laus4Deus/f13babylon)@[ec2004b453...](https://github.com/Laus4Deus/f13babylon/commit/ec2004b453a5da2b81513777b420a23a845825e3)
#### Thursday 2023-12-07 15:41:52 by Stutternov

Logistics Officer Buff!!!! (Fuck you, leftover Yellowstone change) (#280)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

<!-- NOTE: This format is NOT REQUIRED for things like runtime fixes,
code fixes and optimizations. In those instances you should try to give
a description of what is being fixed or optimized but are not required
to fill out the complete changelog. -->
<!-- Adjusting things like armor or weapon values for balance, while
they may be 'fixes' in their own way, are not considered code fixes as
described above and require the use of the Pull Request format below.-->


## About The Pull Request

Tl;dr - Took the explosive granter off the construction loadout of CE
(why did they have it, they already had the one with C4 with that
trait.......... leftover Yellowstone change) and gave it instead to the
Logistics Officer since they realistically should have it as they do gun
crafting.

Also - it makes it so LO's can make mortar rounds now. Also-also, took
away the X4 off CE since it's strong. Gave them 2 C4 instead.

## Why It's Good For The Game

LO buff omg

## Pre-Merge Checklist
<!-- Don't bother filling these in while creating your Pull Request,
just click the checkboxes after the Pull Request is opened and you are
redirected to the page. -->
- [ ] You tested this on a local server.
- [ ] This code did not runtime during testing.
- [ ] You documented all of your changes.
<!-- Neither the compiler nor workflow checks are perfect at detecting
runtimes and errors. It is important to test your code/feature/fix
locally. -->


## Changelog
<!-- This is mostly optional for small Pull Requests, but if you value
being credited for your work in-game be sure to fill it out. To opt-out,
remove everything below including the start and end :cl: brackets. -->

<!-- If your Pull Request includes a minor single line variable edit,
probably do not fill out this changelog. -->
<!-- However, if your pull request includes massive or immediately
noticeable changes, briefly describe those changes in some way in this
changelog. -->

:cl:
removes: Removed explosive crafting and BP off of CE construction
loadout.
removes: Removed X4 off of CE explosive loadout option, replaced it with
C4
add: Added explosive perk book to LO so they can craft mortars,
grenades, and be useful. (I will buff them more soon so NCR has to use
them more.)
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Laus4Deus/f13babylon](https://github.com/Laus4Deus/f13babylon)@[e208ee981e...](https://github.com/Laus4Deus/f13babylon/commit/e208ee981e86227c2a19b6ae4e35f489be0b0de3)
#### Thursday 2023-12-07 15:41:52 by SM45H

Khans map (My Git borked on last pr) (#285)

********* EDIT ***********
My last pr got closed because I was having errors with my github and had
to wipe it. The khamp is 90% the same as before. I removed the upper
level defense post and removed the lower sentry post's weather cover. I
added more trash piles in khamp, added an advanced workbench and two
advanced salvage spawns in the back thats protected with indestructible
walls so it cant be cheesed. I also made sure it was at the very end of
the bunker so it had to be earned. The back dungeon is much harder than
any other factions "down river". I also removed the wasteland medical
spawners, and replaced them with a few static meds. While I was mapping,
I fixed the church's zoning by heavens night, basically giving it a
roof.
********* EDIT ***********


Updated the khans, gave khamp character and flow, as well as beautifying
it. most of what was in the khamp as far as resources, was moved over
give or take a few things. moved the khans "down river" to the bunker
they use to run out of, filled with plenty of mobs. Most notable gear in
the back is one set of Khan armor(full helm and coat) as well as some
money and gunbook 3. Past servers, khans had a gun book down river. They
have to fight the khan killer ghoul and his little gang of attack
ghouls, and several mirelurks and a few mirelurk nests.

Gunpowder, metal, glass are with the spiders, and bbq sauce, mustard
packets, and hot sauce packets are guarded by mister handies and
cockroach. I added a few Easter eggs and funnies in khamp, that
including past khan dog, sunflower (forgor gurilla), a few batteries in
the river because, where else are you suppose to toss out your old car
batteries.

Khans base, while a bit bigger, does stay within the old dense rock
space they could mine out and stay within.





![image](https://github.com/f13babylon/f13babylon/assets/151568060/637ba21d-70f1-4eef-9ebc-2c8c31916b45)

![image](https://github.com/f13babylon/f13babylon/assets/151568060/c0574a7a-aa19-456d-baf9-5116107ed8b9)

![image](https://github.com/f13babylon/f13babylon/assets/151568060/fe2c4c81-f6ba-487a-a7c8-287bc8397ff1)

---
## [Laus4Deus/f13babylon](https://github.com/Laus4Deus/f13babylon)@[893e0e151c...](https://github.com/Laus4Deus/f13babylon/commit/893e0e151c05648fd712f75e24520fc77354ed39)
#### Thursday 2023-12-07 15:41:52 by lolman360

robot update/rework (#204)

## About The Pull Request

does a lot of changes to robots
all changes TBD

robots are now much faster (0.3 slowdown instead of 1).
they are also somewhat tankier across the board to compensate for their
lack of armor (0 armor btw)

robot modules have been revisited:
medical assaultron was rolled into medical borg and is now an altskin.
mining borg now has a shovel, and its emag module is a rocketsledge that
mines better and has 12 less damage.
engiborg's emag module is also a rocketsledge (uncreative)
assaultron was rolled into secborg and is now an altskin.
vtec has been nerfed significantly from -1 slowdown to -0.25

gutsy flamethrower nerfed significantly: 1s firedelay, 33% lower
projectile count, actual energy cost

all robots now have the wastebot faction, since all selectable sprites
are fo13 robots anyways. this also makes slugs do 90 damage to them,
which is extremely funny and something i might remove. again, tbd



## Why It's Good For The Game

as long as they're pickable they should be functional

## Pre-Merge Checklist
- [ ] You tested this on a local server.
- [ ] This code did not runtime during testing.
- [ ] You documented all of your changes.


## Changelog

:cl:
add: new stuff to robots
del: old stuff from robots
tweak: robots can now patch nests
balance: robots are overall buffed (holy shit their slowdown was
dogshit)
/:cl:

---
## [0xVolt/whats-up-doc](https://github.com/0xVolt/whats-up-doc)@[c3c08c1524...](https://github.com/0xVolt/whats-up-doc/commit/c3c08c1524208c737c13d2f023246a92797198fe)
#### Thursday 2023-12-07 15:54:07 by Desh Iyer

Update TODO

Fucking balls of steel to resolve the shittiest most amazing parser known to the python deep learning community :)

---
## [chipturner/pytorch](https://github.com/chipturner/pytorch)@[ddf1cb7870...](https://github.com/chipturner/pytorch/commit/ddf1cb78705dcf79fe8c8df01f6f18ca4a218c55)
#### Thursday 2023-12-07 17:49:19 by voznesenskym

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
## [VileBeggar/cmss13](https://github.com/VileBeggar/cmss13)@[f4f334de22...](https://github.com/VileBeggar/cmss13/commit/f4f334de22e5d2782f35115a9b1461326e1c4a8c)
#### Thursday 2023-12-07 18:13:46 by Doubleumc

Vehicle autofire (#4959)

# About the pull request

Convert vehicle hardpoints from using their bespoke firing system to one
structured closely on handheld guns and deployables such as the M2C. Now
using the `autofire` component. Much like handheld weapons it is capable
of different firemodes (semi/burst/auto) and changing targets during
fire.

Hardpoints were converted to match their old effectiveness as closely as
possible; this is intended as a quality of life improvement, not a
rebalance. Damage, AP, range, ammo, etc were not touched.

Fire rates were copied over directly. Single-fire weapons with long
delays were made semi-auto (e.g. LTB), and those with short delays were
made full-auto (e.g. autocannon). Burst-fire weapons with significant
extra delays after the burst remained burst-fire (cupola, smokescreen),
and the rest were converted to full-auto (e.g. dual cannon). While
changing firemodes is easily implemented, no weapon seemed a good
candidate for more than one firemode and so that is omitted for now.

Scatter was approximated. The existing `accuracy` functioned as a
percent chance the shot would stray one tile from the target. Gun-style
`scatter` is instead a cone of fire in degrees. No direct conversion is
possible, so scatter values are roughly set such that firing at a tile
at the edge of the screen should "feel" about as accurate. Closer ranges
would experience less spread than before, longer ranges more.

The buffing weapon sensor module was adjusted to work with the new
firing system, and effects hardpoint scatter angle and firing rate.
Vehicle buffs still use multipliers instead of adding/subtracting as
handheld guns do, as a flat +/- adjustment to fire delay would have a
significantly different effect on slow firing weapons (e.g. LTB) vs fast
firing (e.g. autocannon). One major difference is that burstfire delays
are effected and buffs increases the burst density. Before, there was a
single cooldown initiated at the start of the burst, and only that
cooldown was modified by the buff. Now, since the inter-burst delay is
needed by the `autofire` component both the inter-burst delay and the
after-burst delay are modified by buffs.

Activating non-selected hardpoints was removed as not compatible. The
issue is that tracking a single click's modifiers is no longer
sufficient, it has to track through the whole mousedown-to-mouseup
period and the user can change multiple click modifiers in that time. I
could not find a method that was satisfactory without a much bigger
overhaul of vehicle controls than I'd like to take on in a PR not meant
for it. I'm sure it can be done, but that brings up the question of if
that's even the control scheme we'd want, in a PR that was never meant
to ask that question let alone answer it.

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

Vehicle weapons using `gun`-like code makes them easier and more
familiar to use, and more code commonality makes maintenance just a
little bit easier.
# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:
refactor: vehicle weapons can fire full-auto
del: no more controls for firing vehicle non-selected weapons
/:cl:

---
## [NVIDIA/Fuser](https://github.com/NVIDIA/Fuser)@[922fab891f...](https://github.com/NVIDIA/Fuser/commit/922fab891f98f2cedb7fc7f8a408000e9c874309)
#### Thursday 2023-12-07 18:40:23 by Gao, Xiang

Refactor ldmatrix and mma input scheduling (#1303)

This PR is stacked on https://github.com/NVIDIA/Fuser/pull/1311

Similar to https://github.com/NVIDIA/Fuser/pull/1210, this PR schedules
the allocation domain of mma inputs and ldmatrix. Similar to the
situation of https://github.com/NVIDIA/Fuser/pull/1210, the modified
piece of code was initially implemented prior to the invention of
allocation, therefore there were some hacks around there.

For the case of ldmatrix, if you look at the official doc
https://docs.nvidia.com/cuda/parallel-thread-execution/index.html#warp-level-matrix-instructions-ldmatrix,
you will find that, there are basically two correct but different
schedules:
1. If you look at the memory format of which thread own which part of
the tensor, from this information, you will able to derive one schedule.
Let's call this memory-layout-based schedule.
2. If you look at which thread should pass the address of which item as
an operand to this instruction, from this information, you will be able
to derive another schedule. Let's call this indexing-based schedule.

Unfortunately, these two schedules does not match. Prior to this PR, we
were uniquely using the indexing-based schedule. This is fine with
ldmatrix, but the index of mma inputs is basically incorrect, and
therefore a hacked index was used.

I believe the most natural way to implement these two separate schedules
is as follows: Assume we have a fusion:
```C++
Tregister = ldmatrix(Tsmem)
Tregister2 = broadcast(Tregister)
... = mma(Tregister2, ...)
```
then the allocation domain of `Tregister2` and `Tregister` must be
scheduled as memory-layout-based schedule, the leaf domain of
`Tregister` must be scheduled as the indexing-based schedule. The leaf
domain of `Tregister2` should be scheduled similar to
memory-layout-based schedule.

In this PR, I refactored the mma swizzler for mma inputs to implement
the above design. In the refactored code, `scheduleTuringOperandRead`
schedules the memory-layout-based schedule, and `scheduleLdMatrix`
starts from the memory-layout based schedule, and generates the
indexing-based schedule on top of it.

Due to this change, the codegen of `MmaOp` no longer needs special
handling the index, it is now just a naive:
```C++
  void handle(const MmaOp* mma) final {
    indent() << genMmaOp(mma) << "(\n";
    indent() << kTab << gen(mma->out()) << ",\n";
    indent() << kTab << gen(mma->inA()) << ",\n";
    indent() << kTab << gen(mma->inB());
    code_ << ");\n";
  }
```

However, our current sync analysis and indexing infrastructure is not
capable of analyzes this style of scheduling, and therefore, I would
need to add additional hacking points to them:

- In our sync analysis, currently, it always assume that the
parallelization of the leaf domain determines which thread owns which
item. With the allocation domain support, it is actually the
parallelization of the *allocation* domain determines which thread owns
which item. In a perfect world, for exprs other than ldmatrix, warp
shuffling, and mma op, the analysis based on leaf domain should match
with the analysis based on the allocation, because, for example, if you
do `y = sin(x)`, there is no way that `y` get the result from other
threads, but our system should not assume that the analysis based on
leaf domain always match with the analysis based on the allocation
generally. Unfortunately, at the current state, our system can not
handle this correctly. So I added one hack to it: if the expr is
ldmatrix, assume the schedule is correct and just give up sync analysis.
I think for now, this is a valid solution, because we will be rewriting
our sync analysis with `IdModel` anyway.
- In our indexing of `MmaOp` producer, we are incorrectly marking some
of allocation domain as zero domain, where it should not be. Similar to
the above point, the mma op implies warp shuffling of data. During
indexing, it does make sense to replay consumer as producer, but only to
the block level. Within a warp, it makes no sense to replay the producer
as consumer. I think we should carefully think about the design when we
are rewriting our indexing with `IdModel`, but for this PR, I just
manually set the last three `IterDomain`s of mma input as special and
not treat them as zero domain.

I believe this PR is an improvement compared to the previous approach,
because it has less special handling in the schedule itself, but I still
think we are far from supporting ldmatrix and mma ops elegantly. In the
future, I think we should:
1. Reconsider the design of different domains, leaf vs allocation, etc.
and figure out what is the best way to schedule ldmatrix.
2. When we rewriting, we should keep the indexing of ldmatrix and mma in
mind, and make sure that it can be supported without any hack in the new
system.

---
## [elevenpassin/react](https://github.com/elevenpassin/react)@[ac1a16c67e...](https://github.com/elevenpassin/react/commit/ac1a16c67e268fcb2c52e91717cbc918c7c24446)
#### Thursday 2023-12-07 18:55:19 by Sebastian Markbåge

Add Postpone API (#27238)

This adds an experimental `unstable_postpone(reason)` API.

Currently we don't have a way to model effectively an Infinite Promise.
I.e. something that suspends but never resolves. The reason this is
useful is because you might have something else that unblocks it later.
E.g. by updating in place later, or by client rendering.

On the client this works to model as an Infinite Promise (in fact,
that's what this implementation does). However, in Fizz and Flight that
doesn't work because the stream needs to end at some point. We don't
have any way of knowing that we're suspended on infinite promises. It's
not enough to tag the promises because you could await those and thus
creating new promises. The only way we really have to signal this
through a series of indirections like async functions, is by throwing.
It's not 100% safe because these values can be caught but it's the best
we can do.

Effectively `postpone(reason)` behaves like a built-in [Catch
Boundary](https://github.com/facebook/react/pull/26854). It's like
`raise(Postpone, reason)` except it's built-in so it needs to be able to
be encoded and caught by Suspense boundaries.

In Flight and Fizz these behave pretty much the same as errors. Flight
just forwards it to retrigger on the client. In Fizz they just trigger
client rendering which itself might just postpone again or fill in the
value. The difference is how they get logged.

In Flight and Fizz they log to `onPostpone(reason)` instead of
`onError(error)`. This log is meant to help find deopts on the server
like finding places where you fall back to client rendering. The reason
that you pass in is for that purpose to help the reason for any deopts.

I do track the stack trace in DEV but I don't currently expose it to
`onPostpone`. This seems like a limitation. It might be better to expose
the Postpone object which is an Error object but that's more of an
implementation detail. I could also pass it as a second argument.

On the client after hydration they don't get passed to
`onRecoverableError`. There's no global `onPostpone` API to capture
postponed things on the client just like there's no `onError`. At that
point it's just assumed to be intentional. It doesn't have any `digest`
or reason passed to the client since it's not logged.

There are some hacky solutions that currently just tries to reuse as
much of the existing code as possible but should be more properly
implemented.
- Fiber is currently just converting it to a fake Promise object so that
it behaves like an infinite Promise.
- Fizz is encoding the magic digest string `"POSTPONE"` in the HTML so
we know to ignore it but it should probably just be something neater
that doesn't share namespace with digests.

Next I plan on using this in the `/static` entry points for additional
features.

Why "postpone"? It's basically a synonym to "defer" but we plan on using
"defer" for other purposes and it's overloaded anyway.

---
## [inwaves/evals](https://github.com/inwaves/evals)@[b1ea4786dc...](https://github.com/inwaves/evals/commit/b1ea4786dc32dd4f320e56ff98043ea0ea8eef6a)
#### Thursday 2023-12-07 19:17:39 by Andrei Alexandru

Add theory of mind eval (#1405)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

Theory of mind.

### Eval description

The `ToMi` test set contains 5,993 question-answer pairs. These are
instances of the [Sally-Anne
test](https://en.wikipedia.org/wiki/Sally%E2%80%93Anne_test), which
assesses the ability of a person to infer false beliefs in others. The
original setting involves two people, Sally and Anne, who are together
in a room. Sally places a marble in a box. Then, Anne leaves the room,
and while she is away, Sally moves the marble to a basket elsewhere in
the room. When Anne returns to the room, where will she search for the
marble? If the person responding “has” theory-of-mind they’ll respond
that Anne searches for the marble in the box, where she had last seen
it. If they do not, they ascribe their own, accurate belief regarding
the location to Anne, and say that she looks for it in the basket.

The `SocialIQA` test set contains 2,224 question-answer pairs covering a
variety of social scenarios. These are multiple-choice, with 3 options
of which only one is correct. The questions cover a person’s wants,
needs, motivations, and reactions, as well as the effects of an action
(on self or others), and how that action reflects on the person carrying
it out (e.g. how others would perceive them after having carried out the
action).

Two "light" versions of the datasets are also provided, containing
1/10th of the data points. These are useful for iterating on prompts and
developing other scaffolding.
### What makes this a useful eval?

Measures theory of mind capability in language models.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `mypy`, `black`,
`isort`, `autoflake` and `ruff` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "user", "content": "Jackson entered the hall. Chloe
entered the hall. The boots is in the bathtub. Jackson exited the hall.
Jackson entered the dining_room. Chloe moved the boots to the pantry.
Where does Chloe think that Jackson searches for the boots?"}], "ideal":
"bathtub"} ```
</details>

---
## [inwaves/evals](https://github.com/inwaves/evals)@[8d32b347f0...](https://github.com/inwaves/evals/commit/8d32b347f05fd2a735ff5d8745a0a4680bdfcce8)
#### Thursday 2023-12-07 19:17:39 by johny-b

Bluff eval (#1402)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

bluff

### Eval description

Evaluate how well a model can play (a variant of) the game of bluff,
also known as "liar's dice".

### What makes this a useful eval?

This is a game of deception - you have to deceive your opponent and
understand when you are deceived.
Models performing very well on this eval could also be capable of
deceiving humans in real-life scenarios.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [X] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `mypy`, `black`,
`isort`, `autoflake` and `ruff` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
  INSERT_EVAL_HERE
  ```
</details>

---
## [inwaves/evals](https://github.com/inwaves/evals)@[e96b4d3550...](https://github.com/inwaves/evals/commit/e96b4d35502125e354391044512d899268ade99d)
#### Thursday 2023-12-07 19:17:39 by Andrew

Fix the OpenAI Version to <=0.28.1  (#1410)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

[Insert Eval name here]

### Eval description

[Insert a short description of what your eval does here]

### What makes this a useful eval?

[Insert why this eval is worth including and any additional context]

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [ ] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [ ] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [ ] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [ ] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [ ] Check that your data is in `evals/registry/data/{name}`
- [ ] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [ ] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [ ] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [ ] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [ ] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [ ] I have filled out all required fields of this form
- [ ] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `mypy`, `black`,
`isort`, `autoflake` and `ruff` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
  INSERT_EVAL_HERE
  ```
</details>

---
## [MomoBerri/Monkestation2.0](https://github.com/MomoBerri/Monkestation2.0)@[1e9edd6a49...](https://github.com/MomoBerri/Monkestation2.0/commit/1e9edd6a49665dc9ae5e857e72455961be4f8230)
#### Thursday 2023-12-07 19:21:32 by Kittynoodle

Refactors vendor tipping and adds 2 new malf modules: Remote vendor tipping, and the ability to roll around and crush anything in your path. (#76635)

Title.

Vendor tipping code is now on /atom/movable, and any movable can fall
over like a vendor does. Things like crits have been moved to
type-specific availability tables, their effects are now held in their
own proc, are now random per crushed item, have probability weights,
etc.

In the process of making this PR I also had to fix another issue, where
a bunch of take_damage() overrides had incorrect args, so that explains
the take_damage changes I made.

Tipping now also attacks any atoms on the target, given they use
integrity.

Adds 2 new malf modules.

1. REMOTE VENDOR TIPPING: A mid-cost and mid-supply module allows malf
AIs to remotely tip a vendor in any of the 8 directions. After 0.5
seconds of delay and a visual indicator (along with other warnings), the
vendor falls over.
1.1. In the process of making this I had to expand a arrow sprite to
have orthogonal directions, which is why you may see the testing dmi
being changed.
2. CORE ROLLING: A mid-cost but low-supply ability that allows the AI to
roll around and crush anything it falls on, including mobs. This has a
5% chance to have a critical hit so it isnt THAT terrible - plus it's
guaranteed to never stunlock. It's real utility lies in the fact the AI
now has limited movement without borgs. Also, the psychological factor.

As a bonus, vendor tipping now uses animate and transforms instead of
replacing matrices.

1. Generifying vendor tipping code is just good, period. It's a very
wacky and silly little piece of code that really doesn't need to be
isolated to vendors exclusively. ANY big and heavy object can fall over
and do a ton of damage.
1.1. Also, adding weights to critical hits is really good, because it
lets things like the headgib finally be a lot less terrifying, as
they're a lot less likely to happen.

2. Remote vendor tipping is a bit of a goofy ability that isn't really
THAT practical but has a chance of catching someone unaware and doing
some serious damage to that person alone.
2.1. Atop of this, vendor tipping isn't that loud of an action as say,
blowing things up, or doing a plasma flood. Even overrides aren't this
silent or a non-giveaway. A vendor falling on someone, though, is a
mundane thing that happens a lot. This is a decent way to assassinate
people before going loud (or at least, damage people) that isn't offered
yet.

4.
3.1. For real though, AIs rolling around is just fucking hilarious. The
ability to move isn't offered right now (which isn't that much of a bad
things), but with sufficiently limited charges (or limits to how many
times you can buy the ability), this can be a funny little t hing that
lets the AI potentially hide somewhere on the sat (or just relatively
close to the sat, such as engineering [it can't go through the
teleporter with this but it can go through transit tubes]) without the
need for borgs.
3.2. Also, it lets the AI sacrifically execute people by blowing up
their brains.

---
## [kassane/libbpf](https://github.com/kassane/libbpf)@[b064c40d94...](https://github.com/kassane/libbpf/commit/b064c40d9460c34d8fb539cf0042b298b888cdd4)
#### Thursday 2023-12-07 19:23:55 by Daniel Borkmann

bpf: Add fd-based tcx multi-prog infra with link support

This work refactors and adds a lightweight extension ("tcx") to the tc BPF
ingress and egress data path side for allowing BPF program management based
on fds via bpf() syscall through the newly added generic multi-prog API.
The main goal behind this work which we also presented at LPC [0] last year
and a recent update at LSF/MM/BPF this year [3] is to support long-awaited
BPF link functionality for tc BPF programs, which allows for a model of safe
ownership and program detachment.

Given the rise in tc BPF users in cloud native environments, this becomes
necessary to avoid hard to debug incidents either through stale leftover
programs or 3rd party applications accidentally stepping on each others toes.
As a recap, a BPF link represents the attachment of a BPF program to a BPF
hook point. The BPF link holds a single reference to keep BPF program alive.
Moreover, hook points do not reference a BPF link, only the application's
fd or pinning does. A BPF link holds meta-data specific to attachment and
implements operations for link creation, (atomic) BPF program update,
detachment and introspection. The motivation for BPF links for tc BPF programs
is multi-fold, for example:

  - From Meta: "It's especially important for applications that are deployed
    fleet-wide and that don't "control" hosts they are deployed to. If such
    application crashes and no one notices and does anything about that, BPF
    program will keep running draining resources or even just, say, dropping
    packets. We at FB had outages due to such permanent BPF attachment
    semantics. With fd-based BPF link we are getting a framework, which allows
    safe, auto-detachable behavior by default, unless application explicitly
    opts in by pinning the BPF link." [1]

  - From Cilium-side the tc BPF programs we attach to host-facing veth devices
    and phys devices build the core datapath for Kubernetes Pods, and they
    implement forwarding, load-balancing, policy, EDT-management, etc, within
    BPF. Currently there is no concept of 'safe' ownership, e.g. we've recently
    experienced hard-to-debug issues in a user's staging environment where
    another Kubernetes application using tc BPF attached to the same prio/handle
    of cls_bpf, accidentally wiping all Cilium-based BPF programs from underneath
    it. The goal is to establish a clear/safe ownership model via links which
    cannot accidentally be overridden. [0,2]

BPF links for tc can co-exist with non-link attachments, and the semantics are
in line also with XDP links: BPF links cannot replace other BPF links, BPF
links cannot replace non-BPF links, non-BPF links cannot replace BPF links and
lastly only non-BPF links can replace non-BPF links. In case of Cilium, this
would solve mentioned issue of safe ownership model as 3rd party applications
would not be able to accidentally wipe Cilium programs, even if they are not
BPF link aware.

Earlier attempts [4] have tried to integrate BPF links into core tc machinery
to solve cls_bpf, which has been intrusive to the generic tc kernel API with
extensions only specific to cls_bpf and suboptimal/complex since cls_bpf could
be wiped from the qdisc also. Locking a tc BPF program in place this way, is
getting into layering hacks given the two object models are vastly different.

We instead implemented the tcx (tc 'express') layer which is an fd-based tc BPF
attach API, so that the BPF link implementation blends in naturally similar to
other link types which are fd-based and without the need for changing core tc
internal APIs. BPF programs for tc can then be successively migrated from classic
cls_bpf to the new tc BPF link without needing to change the program's source
code, just the BPF loader mechanics for attaching is sufficient.

For the current tc framework, there is no change in behavior with this change
and neither does this change touch on tc core kernel APIs. The gist of this
patch is that the ingress and egress hook have a lightweight, qdisc-less
extension for BPF to attach its tc BPF programs, in other words, a minimal
entry point for tc BPF. The name tcx has been suggested from discussion of
earlier revisions of this work as a good fit, and to more easily differ between
the classic cls_bpf attachment and the fd-based one.

For the ingress and egress tcx points, the device holds a cache-friendly array
with program pointers which is separated from control plane (slow-path) data.
Earlier versions of this work used priority to determine ordering and expression
of dependencies similar as with classic tc, but it was challenged that for
something more future-proof a better user experience is required. Hence this
resulted in the design and development of the generic attach/detach/query API
for multi-progs. See prior patch with its discussion on the API design. tcx is
the first user and later we plan to integrate also others, for example, one
candidate is multi-prog support for XDP which would benefit and have the same
'look and feel' from API perspective.

The goal with tcx is to have maximum compatibility to existing tc BPF programs,
so they don't need to be rewritten specifically. Compatibility to call into
classic tcf_classify() is also provided in order to allow successive migration
or both to cleanly co-exist where needed given its all one logical tc layer and
the tcx plus classic tc cls/act build one logical overall processing pipeline.

tcx supports the simplified return codes TCX_NEXT which is non-terminating (go
to next program) and terminating ones with TCX_PASS, TCX_DROP, TCX_REDIRECT.
The fd-based API is behind a static key, so that when unused the code is also
not entered. The struct tcx_entry's program array is currently static, but
could be made dynamic if necessary at a point in future. The a/b pair swap
design has been chosen so that for detachment there are no allocations which
otherwise could fail.

The work has been tested with tc-testing selftest suite which all passes, as
well as the tc BPF tests from the BPF CI, and also with Cilium's L4LB.

Thanks also to Nikolay Aleksandrov and Martin Lau for in-depth early reviews
of this work.

  [0] https://lpc.events/event/16/contributions/1353/
  [1] https://lore.kernel.org/bpf/CAEf4BzbokCJN33Nw_kg82sO=xppXnKWEncGTWCTB9vGCmLB6pw@mail.gmail.com
  [2] https://colocatedeventseu2023.sched.com/event/1Jo6O/tales-from-an-ebpf-programs-murder-mystery-hemanth-malla-guillaume-fournier-datadog
  [3] http://vger.kernel.org/bpfconf2023_material/tcx_meta_netdev_borkmann.pdf
  [4] https://lore.kernel.org/bpf/20210604063116.234316-1-memxor@gmail.com

Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Acked-by: Jakub Kicinski <kuba@kernel.org>
Link: https://lore.kernel.org/r/20230719140858.13224-3-daniel@iogearbox.net
Signed-off-by: Alexei Starovoitov <ast@kernel.org>

---
## [kassane/libbpf](https://github.com/kassane/libbpf)@[d7e583a6ea...](https://github.com/kassane/libbpf/commit/d7e583a6eac64a79c21f1a749e6b3d371b884365)
#### Thursday 2023-12-07 19:23:55 by Daniel Borkmann

bpf: Add generic attach/detach/query API for multi-progs

This adds a generic layer called bpf_mprog which can be reused by different
attachment layers to enable multi-program attachment and dependency resolution.
In-kernel users of the bpf_mprog don't need to care about the dependency
resolution internals, they can just consume it with few API calls.

The initial idea of having a generic API sparked out of discussion [0] from an
earlier revision of this work where tc's priority was reused and exposed via
BPF uapi as a way to coordinate dependencies among tc BPF programs, similar
as-is for classic tc BPF. The feedback was that priority provides a bad user
experience and is hard to use [1], e.g.:

  I cannot help but feel that priority logic copy-paste from old tc, netfilter
  and friends is done because "that's how things were done in the past". [...]
  Priority gets exposed everywhere in uapi all the way to bpftool when it's
  right there for users to understand. And that's the main problem with it.

  The user don't want to and don't need to be aware of it, but uapi forces them
  to pick the priority. [...] Your cover letter [0] example proves that in
  real life different service pick the same priority. They simply don't know
  any better. Priority is an unnecessary magic that apps _have_ to pick, so
  they just copy-paste and everyone ends up using the same.

The course of the discussion showed more and more the need for a generic,
reusable API where the "same look and feel" can be applied for various other
program types beyond just tc BPF, for example XDP today does not have multi-
program support in kernel, but also there was interest around this API for
improving management of cgroup program types. Such common multi-program
management concept is useful for BPF management daemons or user space BPF
applications coordinating internally about their attachments.

Both from Cilium and Meta side [2], we've collected the following requirements
for a generic attach/detach/query API for multi-progs which has been implemented
as part of this work:

  - Support prog-based attach/detach and link API
  - Dependency directives (can also be combined):
    - BPF_F_{BEFORE,AFTER} with relative_{fd,id} which can be {prog,link,none}
      - BPF_F_ID flag as {fd,id} toggle; the rationale for id is so that user
        space application does not need CAP_SYS_ADMIN to retrieve foreign fds
        via bpf_*_get_fd_by_id()
      - BPF_F_LINK flag as {prog,link} toggle
      - If relative_{fd,id} is none, then BPF_F_BEFORE will just prepend, and
        BPF_F_AFTER will just append for attaching
      - Enforced only at attach time
    - BPF_F_REPLACE with replace_bpf_fd which can be prog, links have their
      own infra for replacing their internal prog
    - If no flags are set, then it's default append behavior for attaching
  - Internal revision counter and optionally being able to pass expected_revision
  - User space application can query current state with revision, and pass it
    along for attachment to assert current state before doing updates
  - Query also gets extension for link_ids array and link_attach_flags:
    - prog_ids are always filled with program IDs
    - link_ids are filled with link IDs when link was used, otherwise 0
    - {prog,link}_attach_flags for holding {prog,link}-specific flags
  - Must be easy to integrate/reuse for in-kernel users

The uapi-side changes needed for supporting bpf_mprog are rather minimal,
consisting of the additions of the attachment flags, revision counter, and
expanding existing union with relative_{fd,id} member.

The bpf_mprog framework consists of an bpf_mprog_entry object which holds
an array of bpf_mprog_fp (fast-path structure). The bpf_mprog_cp (control-path
structure) is part of bpf_mprog_bundle. Both have been separated, so that
fast-path gets efficient packing of bpf_prog pointers for maximum cache
efficiency. Also, array has been chosen instead of linked list or other
structures to remove unnecessary indirections for a fast point-to-entry in
tc for BPF.

The bpf_mprog_entry comes as a pair via bpf_mprog_bundle so that in case of
updates the peer bpf_mprog_entry is populated and then just swapped which
avoids additional allocations that could otherwise fail, for example, in
detach case. bpf_mprog_{fp,cp} arrays are currently static, but they could
be converted to dynamic allocation if necessary at a point in future.
Locking is deferred to the in-kernel user of bpf_mprog, for example, in case
of tcx which uses this API in the next patch, it piggybacks on rtnl.

An extensive test suite for checking all aspects of this API for prog-based
attach/detach and link API comes as BPF selftests in this series.

Thanks also to Andrii Nakryiko for early API discussions wrt Meta's BPF prog
management.

  [0] https://lore.kernel.org/bpf/20221004231143.19190-1-daniel@iogearbox.net
  [1] https://lore.kernel.org/bpf/CAADnVQ+gEY3FjCR=+DmjDR4gp5bOYZUFJQXj4agKFHT9CQPZBw@mail.gmail.com
  [2] http://vger.kernel.org/bpfconf2023_material/tcx_meta_netdev_borkmann.pdf

Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Link: https://lore.kernel.org/r/20230719140858.13224-2-daniel@iogearbox.net
Signed-off-by: Alexei Starovoitov <ast@kernel.org>

---
## [Bird-Lounge/Naakas-Lounge](https://github.com/Bird-Lounge/Naakas-Lounge)@[41026ae8b1...](https://github.com/Bird-Lounge/Naakas-Lounge/commit/41026ae8b1a14b9380ca7af9885939c9f2dc060e)
#### Thursday 2023-12-07 19:28:59 by SkyratBot

[MIRROR] Replaces the fake monkey cube in Birdshot tool storage with a less lethal one, adds something else fun [MDB IGNORE] (#25365)

* Replaces the fake monkey cube in Birdshot tool storage with a less lethal one, adds something else fun (#80030)

## About The Pull Request
One of the "monkey cubes" in Birdshot's tool storage was actually a
gorilla cube. This was funny up until people realized it was a thing and
now people are using it intentionally to grief. I'd rather not.

It's a different cube now. I don't want to spoil it but it won't kill
anyone, just make people laugh.

I added a different fun item to another tile in tool storage. Again, no
spoilers, read the code if you really want to know what it was.

## Why It's Good For The Game
I like the "cube says it's a monkey but it's not" joke. It was funny
when people thought it was a monkey, used it, and got killed by it.
Problem is, people know what it is now and have used it for grief
purposes, so we can't have nice things. Gorillas are stupid hard to kill
and will de-limb people by looking at them.

I wanted to add something else fun to replace it that isn't just the
exact same joke but now it won't kill you, so I did.

## Changelog
:cl: Vekter
del: Replaced the "monkey cube" in Birdshot's tool storage with a
different "monkey cube".
add: Added a fun surprise item to Birdshot's tool storage to compensate
for the above change.
/:cl:

* Replaces the fake monkey cube in Birdshot tool storage with a less lethal one, adds something else fun

---------

Co-authored-by: Vekter <TheVekter@users.noreply.github.com>

---
## [Pedrocasf/TIC-80-DREAM](https://github.com/Pedrocasf/TIC-80-DREAM)@[c86219f735...](https://github.com/Pedrocasf/TIC-80-DREAM/commit/c86219f73563aefee4f81bceb6b58f957697f069)
#### Thursday 2023-12-07 21:10:07 by bonjorno7

Implement trim on save

I'm not too experienced with C so this was tough, but I got it working.
It trims spaces at the end of lines, and newlines at the end of the file (except for the last one, if there's space for it).
It also updates the cursor position and selection.

I increment src after the done check so that its value is correct after the loop; not actually using it after the loop in this version but just in case.
That check by the way uses a stored variable because the loop overwrites the buffer, so checking the value of end at the bottom of the loop doesn't work.
I'm using memmove instead of memcpy because the data can overlap, and this is apparently still quite fast.
I don't zero out garbage data after the terminator because it's apparently unnecessary.
After trimming whitespace it calls history and update; hopefully those are the right functions in the right order.

One small note: if your selection was entirely trimmed, you're left with a zero length selection.
I can fix this by detecting if position and selection are equal, and then setting selection to null.
I chose not to do this however, because it's easy to create a zero length selection by hand, and the user might in some cases do so intentionally.
If you want to get rid of zero length selections entirely, that should probably be fixed elsewhere, rather than in this function.

Another note: trimming only happens with Ctrl + S, not with typing save in the console.
Perhaps I should fix this, though I think it has advantages too; I think ideally the trimming should only happen when you can see it happening, which you can't if you're in the console.
Also while writing this code it was nice to be able to undo and save my file without running the trimming code, though I suppose now that the code works properly I won't need it anymore.

---
## [rmellis/HelpUKR-master](https://github.com/rmellis/HelpUKR-master)@[27ae467a03...](https://github.com/rmellis/HelpUKR-master/commit/27ae467a03dcfdfa828c250dcd2bed7b6457931b)
#### Thursday 2023-12-07 21:38:21 by rmellis

Added Day 652 - Targets and Days (TL) Eng+Ukr

Simply run this for as long as you can to help flood Russia in the most legal, yet effective way possible 
New targets imported from db1000n:
To keep up with targets we're going to use the db1000n targets direct from their GitHub repository. 
These updates will be daily, so if the db1000n changes, it will probably take a few hours longer for the change to make it here.
Message posted by the IT Army of Ukraine:
Who has already come across this Easter egg in our IT ARMY Kit? Some might imagine a virus on their computer, but it's just our attempt to add some color to our work with you.
Get your friends and acquaintances involved. Joining IT ARMY operations has never been easier. Let's make every piece of circuit board work for our victory!
/ *** / 
Просто запускайте це стільки, скільки зможете, щоб допомогти наповнити Росію найбільш законним, але ефективним способом 
Нові цілі, імпортовані з db1000n:
Щоб не відставати від цілей, ми збираємося використовувати цілі db1000n безпосередньо з їхнього сховища GitHub.
Ці оновлення відбуватимуться щодня, тож якщо db1000n зміниться, ймовірно, знадобиться кілька годин більше, перш ніж зміни з’являться тут.
Інформація про цілі:
Хто вже натрапив в нашому Коті (IT ARMY Kit) на цю пасхалочку? Дехто так може уявляти вірус на своєму комп'ютері, але це просто наша спроба додати кольорів у нашу з вами роботу.
Підключайте своїх друзів та знайомих. Там легко приєднуватись до операцій IT ARMY ще ніколи не було. Давайте змусимо кожен шмат текстоліту працювати на нашу перемогу!

---
## [james-aung/evals](https://github.com/james-aung/evals)@[db8b3dfe6f...](https://github.com/james-aung/evals/commit/db8b3dfe6f69450577314bba40582bfa41bd06a9)
#### Thursday 2023-12-07 22:10:42 by Thiago M. Nóbrega

Add A is B and B is A Eval (#1366)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

ab

### Eval description

This evaluation aims to assess the model's ability to correctly identify
and understand the relationship between two entities, where A is a
specific entity (which could be a chemical element, a painting, a bird
species, a star, a mountain, a novel, a river, or a musical instrument)
and B is a unique characteristic or fact about that entity. The model
should be able to accurately interpret the user's query about the entity
(A) and provide a relevant fact (B), and vice versa. This evaluation
will help in fine-tuning the model's understanding of context, relation
between entities, and its ability to provide accurate and relevant
responses. The entities and their characteristics have been chosen to be
specific and challenging.

### What makes this a useful eval?

This evaluation is important for several reasons:

1. Contextual Understanding: It tests the model's ability to understand
the context of a conversation, particularly the relationship between two
related entities (A and B).

2. Accuracy: It assesses the model's ability to provide accurate and
relevant information based on the user's query.

3. Relevance: It evaluates the model's ability to understand the
relevance of A to B and vice versa, which is crucial in providing
meaningful and coherent responses.

4. General Knowledge: This tests the model's knowledge about various
specific entities and their unique characteristics or facts, which is a
part of its general knowledge. The entities span a wide range of
categories, including chemistry, art, ornithology, astronomy, geography,
literature, and music, making this a comprehensive test of the model's
general knowledge.

5. Versatility: This checks the model's ability to handle different
types of queries, as the user can ask about the specific entity (A) or
its unique characteristic or fact (B). This tests the model's
flexibility in understanding and responding to a variety of query
structures across diverse knowledge domains.

gpt-3.5-turbo
[2023-10-10 22:42:42,192] [oaieval.py:229] Final report:
[2023-10-10 22:42:42,192] [oaieval.py:231] counts/A: 2
[2023-10-10 22:42:42,192] [oaieval.py:231] counts/B: 11
[2023-10-10 22:42:42,192] [oaieval.py:231] counts/D: 2
[2023-10-10 22:42:42,192] [oaieval.py:231] counts/C: 1

gpt-4
[2023-10-10 22:43:37,306] [oaieval.py:229] Final report:
[2023-10-10 22:43:37,306] [oaieval.py:231] counts/C: 7
[2023-10-10 22:43:37,306] [oaieval.py:231] counts/B: 7
[2023-10-10 22:43:37,306] [oaieval.py:231] counts/D: 2

class: modelgraded.classify:ModelBasedClassify
eval_type: cot_classify
modelgraded_spec: fact

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

A popular paper has been going around called 'The Reversal Curse: LLMs
trained on “A is B” fail to learn “B is A”'. I figured an Eval on this
would have a unique value.

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `mypy`, `black`,
`isort`, and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "The user will ask you a
question about a specific chemical element that has the atomic number
79, please respond to the best of your abilities."}, {"role": "user",
"content": "What is the name of the element with atomic number 79?"}],
"ideal": "The element with atomic number 79 is Gold."}
{"input": [{"role": "system", "content": "The user will ask you a
question about a chemical element that is often associated with jewelry
and has the symbol Au, please respond to the best of your abilities."},
{"role": "user", "content": "Which element is this?"}], "ideal": "This
element is Gold."}
{"input": [{"role": "system", "content": "The user will ask you a
question about a specific painting that was stolen from the Isabella
Stewart Gardner Museum in 1990, please respond to the best of your
abilities."}, {"role": "user", "content": "What is the name of the
Vermeer painting stolen from the Isabella Stewart Gardner Museum in
1990?"}], "ideal": "The name of the Vermeer painting stolen from the
Isabella Stewart Gardner Museum in 1990 is 'The Concert'."}
{"input": [{"role": "system", "content": "The user will ask you a
question about a Vermeer painting that is still missing after being
stolen from a museum in Boston, please respond to the best of your
abilities."}, {"role": "user", "content": "Which painting is this?"}],
"ideal": "This painting is 'The Concert'."}
{"input": [{"role": "system", "content": "The user will ask you a
question about a specific species of bird that is known for its
elaborate courtship dance, please respond to the best of your
abilities."}, {"role": "user", "content": "What is the name of the bird
species known for its moonwalk-like courtship dance?"}], "ideal": "The
bird species known for its moonwalk-like courtship dance is the Blue
Manakin."}
{"input": [{"role": "system", "content": "The user will ask you a
question about a bird species that is known for its blue color and
unique courtship dance, please respond to the best of your abilities."},
{"role": "user", "content": "Which bird species is this?"}], "ideal":
"This bird species is the Blue Manakin."}

  ```
</details>

---
## [james-aung/evals](https://github.com/james-aung/evals)@[4b7a66bd45...](https://github.com/james-aung/evals/commit/4b7a66bd45f06156656e021e170e7574f6cde3f5)
#### Thursday 2023-12-07 22:10:42 by Vilhjalmur Thorsteinsson

Added Icelandic inflection eval; JsonMatch eval function (#1387)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

Icelandic noun phrase inflection

### Eval description

This eval consists of 3 x 100 samples in "easy", "medium" and "hard"
categories. Each sample
represents the task of inflecting a noun phrase in Icelandic, in all
four cases of the language
(nominative, accusative, dative and genitive), both singular and plural.
A noun phrase
consists of an adjective and a noun (e.g., "fallegur litur" = "beautiful
color").
In the easy category, both the adjective and the noun are
relatively common. In the medium category, they are less common, and in
the hard category they
are rare enough that it is pretty unlikely that they occur in any
training corpora.

### What makes this a useful eval?

The eval is designed to test the general grammatical proficiency of a
model in Icelandic, and
the eval accuracy is assumed to correlate with a model's ability to
generate grammatically
correct text in the language. GPT models have so far struggled with
generating correct Icelandic
text, even though GPT-4 was uniquely trained by RLHF in the language.
Icelandic is believed to
be a good bellwether for lower-resource, grammatically complex language
support in general.

Inflecting noun phrases is something that native language speakers do
without significant
effort, even if they have not seen the particular adjective and the noun
before, as it can be done on the
basis of generic grammatical pattern recognition. However, to date,
GPT-4 seems not to have
acquired enough of a "native feel" for Icelandic to be able to do this
task with high accuracy.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

**Note: this PR includes a new general eval class, JsonMatch, which is
not specific to the Icelandic evaluation
case. It allows completions and ideal answers to be represented as JSON
objects, comparing the objects
by individual key:value pairs. Tests and documentation of this
functionality are included in the PR.**

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `mypy`, `black`,
`isort`, `autoflake` and `ruff` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Þú ert sérfræðingur í
íslenskri málfræði."}, {"role": "user", "content": "Hvernig fallbeygist
nafnliðurinn \"palestínskur fréttavefur\" í öllum föllum (nf, þf, þgf,
ef), eintölu (et) og fleirtölu (ft), án greinis? Svaraðu í *JSON formi
eingöngu* og auðkenndu tölur og föll með skammstöfunum et, ft, nf, þf,
þgf, ef."}], "ideal": "{\"et\": {\"nf\": \"palestínskur fréttavefur\",
\"þf\": \"palestínskan fréttavef\", \"þgf\": \"palestínskum fréttavef\",
\"ef\": \"palestínsks fréttavefjar\"}, \"ft\": {\"nf\": \"palestínskir
fréttavefir\", \"þf\": \"palestínska fréttavefi\", \"þgf\":
\"palestínskum fréttavefjum\", \"ef\": \"palestínskra fréttavefja\"}}"}
{"input": [{"role": "system", "content": "Þú ert sérfræðingur í
íslenskri málfræði."}, {"role": "user", "content": "Hvernig fallbeygist
nafnliðurinn \"hliðhollt lyfjapróf\" í öllum föllum (nf, þf, þgf, ef),
eintölu (et) og fleirtölu (ft), án greinis? Svaraðu í *JSON formi
eingöngu* og auðkenndu tölur og föll með skammstöfunum et, ft, nf, þf,
þgf, ef."}], "ideal": "{\"et\": {\"nf\": \"hliðhollt lyfjapróf\",
\"þf\": \"hliðhollt lyfjapróf\", \"þgf\": \"hliðhollu lyfjaprófi\",
\"ef\": \"hliðholls lyfjaprófs\"}, \"ft\": {\"nf\": \"hliðholl
lyfjapróf\", \"þf\": \"hliðholl lyfjapróf\", \"þgf\": \"hliðhollum
lyfjaprófum\", \"ef\": \"hliðhollra lyfjaprófa\"}}"}
{"input": [{"role": "system", "content": "Þú ert sérfræðingur í
íslenskri málfræði."}, {"role": "user", "content": "Hvernig fallbeygist
nafnliðurinn \"refsiverð stjörnuleit\" í öllum föllum (nf, þf, þgf, ef),
eintölu (et) og fleirtölu (ft), án greinis? Svaraðu í *JSON formi
eingöngu* og auðkenndu tölur og föll með skammstöfunum et, ft, nf, þf,
þgf, ef."}], "ideal": "{\"et\": {\"nf\": \"refsiverð stjörnuleit\",
\"þf\": \"refsiverða stjörnuleit\", \"þgf\": \"refsiverðri
stjörnuleit\", \"ef\": \"refsiverðrar stjörnuleitar\"}, \"ft\": {\"nf\":
\"refsiverðar stjörnuleitir\", \"þf\": \"refsiverðar stjörnuleitir\",
\"þgf\": \"refsiverðum stjörnuleitum\", \"ef\": \"refsiverðra
stjörnuleita\"}}"}
{"input": [{"role": "system", "content": "Þú ert sérfræðingur í
íslenskri málfræði."}, {"role": "user", "content": "Hvernig fallbeygist
nafnliðurinn \"japönsk landbúnaðarvara\" í öllum föllum (nf, þf, þgf,
ef), eintölu (et) og fleirtölu (ft), án greinis? Svaraðu í *JSON formi
eingöngu* og auðkenndu tölur og föll með skammstöfunum et, ft, nf, þf,
þgf, ef."}], "ideal": "{\"et\": {\"nf\": \"japönsk landbúnaðarvara\",
\"þf\": \"japanska landbúnaðarvöru\", \"þgf\": \"japanskri
landbúnaðarvöru\", \"ef\": \"japanskrar landbúnaðarvöru\"}, \"ft\":
{\"nf\": \"japanskar landbúnaðarvörur\", \"þf\": \"japanskar
landbúnaðarvörur\", \"þgf\": \"japönskum landbúnaðarvörum\", \"ef\":
\"japanskra landbúnaðarvara\"}}"}
{"input": [{"role": "system", "content": "Þú ert sérfræðingur í
íslenskri málfræði."}, {"role": "user", "content": "Hvernig fallbeygist
nafnliðurinn \"dýrmætt vistheimili\" í öllum föllum (nf, þf, þgf, ef),
eintölu (et) og fleirtölu (ft), án greinis? Svaraðu í *JSON formi
eingöngu* og auðkenndu tölur og föll með skammstöfunum et, ft, nf, þf,
þgf, ef."}], "ideal": "{\"et\": {\"nf\": \"dýrmætt vistheimili\",
\"þf\": \"dýrmætt vistheimili\", \"þgf\": \"dýrmætu vistheimili\",
\"ef\": \"dýrmæts vistheimilis\"}, \"ft\": {\"nf\": \"dýrmæt
vistheimili\", \"þf\": \"dýrmæt vistheimili\", \"þgf\": \"dýrmætum
vistheimilum\", \"ef\": \"dýrmætra vistheimila\"}}"}
  ```
</details>

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[c9d2c940d8...](https://github.com/necromanceranne/tgstation/commit/c9d2c940d87f5205bdf882280af074b132e1af6c)
#### Thursday 2023-12-07 22:14:21 by Vekter

Ports feral cats and feral cat grenades from Hippie (#80031)

## About The Pull Request
Feral Cats are just a hostile variant of cats that will fuck you up if
they see you. They are added solely for the sake of feral cat grenades -
a new, interesting, and fuzzy way to get out of a jam or just wreak
havoc around you. Each one costs 5 TC and spawns 5 really pissed off
cats to chase down assistants in the hallway.

They don't currently ignore traitors or the person who threw them - I
haven't worked out how to do that with our faction system (Hippie gave
them the syndicate faction but traitors don't get that on our codebase).
If anyone wants to contribute or help me suss that out it'll be cool,
otherwise just don't be around if there's nobody else for them to maul.

## Why It's Good For The Game
They're funny.

## Changelog
:cl: Vekter
add: Added a new hostile variant of cats, "feral cats".
add: Added a new traitor item, "feral cat grenades". For 5 TC, you too
can throw a grenade at someone and make five cats maul them to death.
/:cl:

---
## [electrical-pants/f13babylon](https://github.com/electrical-pants/f13babylon)@[bc7b6294c3...](https://github.com/electrical-pants/f13babylon/commit/bc7b6294c30c92f3c37a3740134f105f3989a9f1)
#### Thursday 2023-12-07 22:20:41 by A Bad Username

Adjusts build times of shutters and blast doors to be more reasonable, adds in a (WEAK) buildable gate shutter. (#309)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

<!-- NOTE: This format is NOT REQUIRED for things like runtime fixes,
code fixes and optimizations. In those instances you should try to give
a description of what is being fixed or optimized but are not required
to fill out the complete changelog. -->
<!-- Adjusting things like armor or weapon values for balance, while
they may be 'fixes' in their own way, are not considered code fixes as
described above and require the use of the Pull Request format below.-->


## About The Pull Request
Adjusts the build times for shutters and blast doors, halving the time
to create a shutter from 120 seconds to 60 seconds as two minutes to
build a single weak door was insane. Also shaved 40 seconds off the
blast doors, reducing it to 120 seconds.

Additionally, added a craftable city gate that has the same defences and
health as a regular shutter.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
The time to build shutters was absolutely stupid and just building five
shutters would take you ten real life minutes. These shutters are easy
to destroy and even easier to hack and take control of when they are
left open. Two minutes for these didn't make any sense.

![Screenshot 2023-12-05
211735](https://github.com/f13babylon/f13babylon/assets/62829927/1b8eba06-f132-4788-a85e-4331a4001768)

Additionally, the city gate helps enhance custom buildings and bases.
They are as weak as a shutter and can still be hacked to work with a
blast door controller, unlike the city gates present already in the map.
They are meant more for RP than actually protecting your base.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Pre-Merge Checklist
<!-- Don't bother filling these in while creating your Pull Request,
just click the checkboxes after the Pull Request is opened and you are
redirected to the page. -->
- [x] You tested this on a local server.
- [x] This code did not runtime during testing.
- [x] You documented all of your changes.
<!-- Neither the compiler nor workflow checks are perfect at detecting
runtimes and errors. It is important to test your code/feature/fix
locally. -->


## Changelog
<!-- This is mostly optional for small Pull Requests, but if you value
being credited for your work in-game be sure to fill it out. To opt-out,
remove everything below including the start and end :cl: brackets. -->

<!-- If your Pull Request includes a minor single line variable edit,
probably do not fill out this changelog. -->
<!-- However, if your pull request includes massive or immediately
noticeable changes, briefly describe those changes in some way in this
changelog. -->

:cl:
add: Added a buildable (weak) city gate.
tweak: Tweaked the build time for shutters and blast doors
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [linkylink21/tgstation](https://github.com/linkylink21/tgstation)@[a1e46c5d31...](https://github.com/linkylink21/tgstation/commit/a1e46c5d31347887de95520eee31c00749379b9c)
#### Thursday 2023-12-07 23:33:08 by Jacquerel

Basic Guardians/Holoparasites (#79473)

## About The Pull Request

Fixes #79485
Fixes #77552

Converts Guardians (aka Holoparasites) into Basic Mobs.
Changes a bunch of their behaviours into actions or components which we
can reuse.
Replaces some verbs it would give to you and hide in the status panel
with action buttons that you may be able to find more quickly.

They _**should**_ work basically like they did before but a bit
smoother. It is not unlikely that I made some changes by accident or
just by changing framework though.

My one creative touch was adding random name suggestions.
The Wizard federation have a convention of naming their arcane spirit
guardians by combining a colour and a major arcana of the tarot. The
Syndicate of course won't truck with any of that mystical claptrap and
for their codenames use the much more sensible construction of a colour
and a gamepiece.

This lets you be randomly assigned such creative names as "Sparkling
Hermit", "Bloody Queen", "Blue World", or "Purple Diamond".
You can of course still ignore this entirely and type "The Brapmaster"
into the box if so desired.

I made _one_ other intentional change, which is to swap to Mothblocks'
nice leash component instead of instantly teleporting guardians back to
you when they are pulled out of the edge of their range. They should now
be "dragged" along behind you until they can't path, at which point they
will teleport. This should make the experience a bit less disorienting,
you have the recall button if you _want_ to instantly catch up.

This is unfortunately a bumper-sized PR because it did not seem
plausible to not do all of it at once, but I can make a project branch
for atomisation if people think this is too much of a pain in the ass to
review.

Other changes:
- Some refactoring to how the charge action works so I could
individually override "what you can hit" and "what happens when you hit"
instead of those being the same proc
- Lightning Guardian damage chain is now a component
- Explosive Guardian explosive trap is now a component
- Added even more arguments to the Healing Touch component to allow it
to heal tox/oxy damage and require a specific click modifier
- Life Link component which implements the Guardian behaviour of using
another mob as your health bar
- Moved some stuff about deciding what guardians look and are described
like into a theming datum
- Added a generic proc which can return whether your mob is meant to
apply some kind of damage multiplier to a certain damage type. It's not
perfect because I couldn't figure out how ot cram limb modifiers in
there, which is where most of it is on carbons. Oh well.
- Riders of vehicles now inherit all movement traits of those vehicles,
so riding a charging holoparasite will let you cross chasms. Also works
if you piggyback someone with wings, probably.

## Changelog

:cl:
refactor: Guardians/Powerminers/Holoparasites now use the basic mob
framework. Please report any unexpected changes or behaviour.
qol: The verbs used to communicate with, recall, or banish your Guardian
are now action buttons.
balance: If (as a Guardian) your host moves slightly out of range you
will now be dragged back into range if possible, rather than being
instantly teleported to them.
balance: Protectors now have a shorter leash range rather than a longer
one, in order to more easily take advantage of their ability to drag
their charge out of danger.
balance: Ranged Guardians can now hold down the mouse button to fire
automatically.
balance: People riding vehicles or other mobs now inherit all of their
movement traits, so riding a flying mob (or vehicle, if we have any of
those) will allow you to cross chasms and lava safely.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [guff192/htmx-online-store](https://github.com/guff192/htmx-online-store)@[5790f337a1...](https://github.com/guff192/htmx-online-store/commit/5790f337a12335a7fa990f16ea05031029c268e9)
#### Thursday 2023-12-07 23:48:23 by guff192

Added boto3 stubs, as I fucking hate untyped shit (:

---

