## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-12-19](docs/good-messages/2023/2023-12-19.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,498,979 were push events containing 3,781,493 commit messages that amount to 312,970,094 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 74 messages:


## [sysfce2/boringssl](https://github.com/sysfce2/boringssl)@[a942d57207...](https://github.com/sysfce2/boringssl/commit/a942d572073e98944200e154597442796fdb13de)
#### Tuesday 2023-12-19 00:03:48 by David Benjamin

Support lists and code blocks in doc.go

Our documentation comments already include examples of code blocks
and lists, they just don't get rendered right. We also have things that
were trying to be lists but aren't. Go ahead and add support for it, and
fix the handful of list-like things that didn't get rendered as lists.

I took inspiration from CommonMark (https://spec.commonmark.org/0.30/)
to resolve questions such as whether blank lines are needed between
lists, etc., but this does not support any kind of nesting and is still
far from a CommonMark parser. Aligning with CommonMark leaves the door
open to pulling in a real Markdown parser if we start to need too many
features. I've also borrowed the "block" terminology from CommonMark.

One ambiguity of note: whether lists may interrupt paragraphs (i.e.
without a blank line in between) is a little thorny. If we say no, this
doesn't work:

   Callers should heed the following warnings:
   1) Don't use the function
   2) Seriously, don't use this function
   3) This function is a bad idea

But if we say yes, this renders wrong:

   This function parses an X.509 certificate (see RFC
   5280) into an X509 object.

We have examples of both in existing comments, though we could easily
add a blank line in the former or rewrap the latter. CommonMark has a
discussion on this in https://spec.commonmark.org/0.30/#lists

CommonMark says yes, but with a hack that only lists starting with 1 can
interrupt paragraphs. Since we're unlikely to cite RFC 1, I've matched
for now, but we may want to revisit this if it gets to be a pain. I
could imagine this becoming a problem:

   This function, on success, does some stuff and returns
   1. Otherwise, it returns 0.

But that looks a little weird and we usually spell out "one" and "zero".
I printed all the lists we detected in existing comments, and this has
not happened so far.

I've also required fewer spaces than CommonMark to trigger a code block.
CommonMark uses four, but four spaces plus a leading "//" and a " " is
quite a lot. For now I'm not stripping the spaces after the comment
marker at comment extraction time and then requiring three spaces, so
two spaces relative to normal text. This is mostly to match what we've
currently been doing, but we can always change it and our comments
later.

Change-Id: Ic61a8e93491ed96aba755aec2a5f32914bdc42ae
Reviewed-on: https://boringssl-review.googlesource.com/c/boringssl/+/64930
Reviewed-by: Bob Beck <bbe@google.com>
Commit-Queue: David Benjamin <davidben@google.com>

---
## [iprtel/cppfront](https://github.com/iprtel/cppfront)@[cdf71bdca6...](https://github.com/iprtel/cppfront/commit/cdf71bdca64536a005f2491d8c19f1d05a1c62f6)
#### Tuesday 2023-12-19 00:08:21 by Herb Sutter

Correct copy/move for `union`

By writing separate construction and assignment, plus the new feature of suppressing assignment to a member by writing `member = _ ;` (now allowed only in assignment operators).

I do realize that's an "opt-out" which I normally prefer to avoid, but:

- I considered and decided against (for now) the alternative of not having assignment be memberwise by default. I want to keep the (new to Cpp2) default of memberwise semantics for assignment as with construction. I think that's a useful feature, and normally if you do assign to a member it doesn't arise, and so I think it makes sense to explicitly call out when we're choosing not to do any assignment at all to a member before doing other assignment processing. We'll get experience with how it goes.

- `_` is arguably natural here, since it's pronounced "don't care." There too, we'll see if that is natural generalized, or feels strained. For now it feels natural to me.

---
## [deltanedas/ss14-docs](https://github.com/deltanedas/ss14-docs)@[4feada28fb...](https://github.com/deltanedas/ss14-docs/commit/4feada28fbf0cdd543026992706dd770c4edfb35)
#### Tuesday 2023-12-19 00:27:28 by Kevin Zheng

Add atmos roadmap (#78)

# Roadmap For Atmospherics

## Background

Most atmos players currently agree that atmos is not very fun to play,
for some of the following reasons:

1. There is little content to play after round-start setup. Part of the
problem is that things like distro and TEG are "set up and forget".

2. Atmos can't actually rectify atmos problems in a reasonable amount of
time. For example, if there actually is a plasma leak, scrubbers
typically work too slowly resulting in the plasma inevitably being lit
before it can be cleaned up.

3. Atmos techs don't play with the rest of the station, preferring to
isolate themselves to produce a funny green gas that is only
particularly useful for shuttle bombing. Mechanics like this violate the
[fundamental design
principles](en/general-development/feature-proposals/ss14-fundamental-design-principles.md).
While these mechanics shouldn't be removed per-se, more focus should be
given to mechanics that increase interactions with the station, like
making sure the air is breathable and well-heated.

## Proposal

Make atmos more fun to play by adding more challenges and processes
semi-inspired by real life.

**An atmos tech's primary job is to keep the station livable and
breathable.** There are a lot of interesting real life challenges
associated with making this happen, not in the least of which is that in
space, every gas molecule wants desperately to escape into the cold of
space. There is also the challenge of keeping the station appropriately
temperature-regulated despite the cold outside and occasional plasma
fires inside.

Where it does not conflict with fun (see below), **incorporate realistic
processes and simulations**. As stated in the [fundamental design
principles](en/general-development/feature-proposals/ss14-fundamental-design-principles.md),
intuitive simulation makes for a better game. Having real-life analogs
for gas behaviors helps make both atmos more discoverable and intuitive
for new players and also caters to atmos nerds.

None of these realism additions require any sort of math to play. Only a
basic understanding of the following principles should be enough to
understand and play:

1. You should not be able to spin energy out of thin air.
2. When given a choice, gas flows from high pressure to low pressure.
3. When given a choice, temperature transfers from hot to cold.

### An Interlude on Realism

The chief objective of a game is to be fun to play, and not to be
realistic. Where realism conflicts with fun, fun should be chosen every
time.

**However,** games are most fun when players have a sense of agency
(their actions matter in determining the final outcome of the game) and
when their challenges are struggles are believable.

In order for players' challenges and struggles to be believable, the
game universe must obey a consistent system of rules and physical
limitations. It would not be fun if players have a way to *deux ex
machina* out of every imaginable problem (e.g. Nukies? Why don't we use
the magical remote control that makes all the nukies disappear? After
all, we have *spess magic*.) We're in space, and it should be hard to
get gases because they tend to escape into... you know... space. Not
every station should have a magical gas miner.

But guess what? It turns out that realism provides both a set of
interesting problems and a set of rules for how a universe should
consistently behave. So by making things more realistic, we get both
interesting mechanics and a set of consistent rules for free. Of course
realism doesn't trump fun, and if it is fun to make something that is
unrealistic (e.g. plasma gas), then we should always pick fun.
**However, where realism does not conflict with being fun, then we
should opt to be realistic because it provides a set of interesting
problems and consistent rules.**

After all, why do we say that *PV=nRT*? Shouldn't we make up a different
gas law because realism is bad?

## High-Priority Proposals

These proposals should be implemented first, because they have an
outsized impact on atmos balance as a whole.

- **Phase out gas miners for all upstream maps.** It doesn't make sense
that all stations have free and plentiful sources of gas, otherwise you
might as well be on a planet. This is a game that is literally set in
space. It would make sense to keep a few specialty miners, e.g. for
plasma, if a station is set on a plasma mining planet. But in general,
all other gases should be imported via gas canisters. Miners should
still be kept available for any forks that choose to use them.

- This solves problems (1) and (3). Maintaining a livable atmos would
involve work during the round beyond setting up distro to pipe gas from
miners. It would help increase interactions with other departments, such
as cargo and salvage as atmos needs to order gas.

- Ensuring a appropriate round-start supply of gas would make the game
playable without a functional cargo department.

- This would discourage fighting fires or atmos problems by wholesale
spacing a section. There is currently very little downside to spacing a
section to get rid of problems because of an unlimited gas supply.

- There is [overwhelming consensus on mappers for
this](https://discord.com/channels/310555209753690112/770682801607278632/1162179968915210280).

- As an interim or for very low pop-count maps, keep miners but make
them mine gas at low temperature that has to be heated up before use.
This preserves a bit of an incentive for atmos players to not space a
section at the first sign of trouble.

- **Globally increase MaxTransferRate** for devices that are not
flow-based, e.g. pumps.

- This solves problem (2). Among other things, it would make scrubbers
and other devices actually useful for combating atmospheric problems.
Currently players prefer to just space everything. Increasing this would
provide a feasible alternative.

## Medium Priority

- **Make all atmos devices flow-based.** This means driving gas flow as
a result of pressure differences created using pumps. The specific
offenders are currently any "pumped" device that is not a dedicated
pump, e.g. air vents, scrubbers, filters, and mixers.

- This addresses an issue about atmos intuition and accessibility.
Players should not have to understand the internal workings of the pipe
net system (e.g. a pipe is one big node, gases move between them). In
real life, a fan or pump creates a pressure difference, and pressure
differences drive gas flow. If you blow on one end of a straw, you can
expect it to come out of the other end, not get stuck in a pipe net.

- This also addresses (2). Instead of having a fixed upper bound on
volume transfer, transfer rates would always depend on the pressure
difference that you create.

- **Add maximum temperature and pressure limits for most devices.** It
does not make sense that you can contain the surface of the sun in your
pipes. Adding limits would encourage designing processes and systems
that work within reasonable constraints.

- Some "sub-optimal" setups are really unintuitive and wouldn't work in
real life due to temperature and pressure limits.

- There are some concerns about being able to run burn chambers and the
TEG. The screenshot below demonstrates a TEG that is capable of powering
an entire large-sized station (256.8 kW current output, the peak output
is quite a bit higher) with a maximum pressure excursion of 1600 kPa. It
shows that pipes that burst at reasonable pressures are entirely
consistent with having burn chambers. You just need to set them up
correctly.


![image](https://user-images.githubusercontent.com/3229565/274441724-712f4ebf-7440-4d81-879e-19aa29788822.png)

- This addresses problem (1), the "set up and forget" issue by adding
temperatures and pressures to monitor. It also allows the opportunity
for sabatoge.


- **Make heaters and freezers thermodynamically sound.** Keeping a
station properly heated or cooled is actually a substantial real-life
problem. Why deprive atmos techs an actual challenge that keeps gameplay
interesting? Because of the existence of generators like the TEG,
keeping things thermodynamically balanced is also a great way to prevent
infinite power hacks.

## Low Priority

- **Make station air flow-based.** Currently, air vents release air when
the pressure is too low, and by default scrubbers only scrub waste
gases. So if for some reason the station gets cold, there's no easy way
to cycle the air out and heat it up. Of course, you could set all the
scrubbers to siphon, heat your distro, and then set the air alarm to
fill. But that would just be describing a bad way of doing what real
life HVAC systems have always been doing: keep the air flowing.

- This addresses problem (2) by making it possible to better regulate
station temperature.

- **Make heaters and freezers binary.** Just like your central heating
and air conditioning circulate air through heat/cold coils, gases should
flow across heaters and freezers in order to exchange temperature.

- **Adding process-based alternatives to scrubbers and filters.** For
example, with gas reaction-based scrubbing processes, scrubbers with
limited uses, or physical processes.

- This addresses problems (1) and (3) by adding more content that is
directly related to the well-being of the station.

- One of the most pressing challenges in the real world is "how do you
separate different kinds of gas." Most current methods of gas extraction
are based on chemistry (e.g. real life carbon dioxide scrubbers contain
chemicals that react with CO2, pulling it out) or physical methods (e.g.
fractional distillation, where you cool down air in different stages to
get liquid nitrogen, oxygen, etc.) This creates a lot of opportunity for
new game play mechanics and industrial processes. This would also give
more opportunities to add gas-based reactions (i.e. more content).

- This does not advocate for removal of scrubbers and filters, but
rather makes it a mapper option, e.g. whether to use scrubbers at
round-start or make atmos set up a system depending on the desired level
of role-play.

- When set up correctly, these should have much higher processing rates
than scrubbers. This should give an incentive to set these up, e.g. on
longer rounds, while still keeping scrubbers as an option.

- This adds "optimization, tinkering, and creation of intricate builds."

- **Add gas condensation.** This would enable fractional distillation
and permit conversion between gas and the equivalent reagent.

- **Add pump efficiency curves.** Pumps have to work harder when they
create a larger pressure difference. As a result, pumping from 1 atm to
2 atm should be easier (read: faster) than pumping from 1 atm to 10 atm.
You could create a multi-stage pump, and indeed, that is what people in
real life do, at the trade-off of less throughput.

- **Breaking windows at high enough tile pressure differences.** To
handle explosions and resulting space wind without leaning on the
explosino system, and to encourage people to design burn chambers with
more controlled burns instead of always putting their pedal to the
metal.

- **Various QoL improvements** such as the RPD.

---
## [GesuBackups/Aurora.3](https://github.com/GesuBackups/Aurora.3)@[bc66a212d7...](https://github.com/GesuBackups/Aurora.3/commit/bc66a212d771eef33ae88445ebe4462ee25bde17)
#### Tuesday 2023-12-19 00:52:29 by RustingWithYou

Hephaestus Security Ship & Corporate Voidsuit Tweaks (#17962)

* hephaestus security ship

* fuck off

* welcome mesgaes

* lattice hell

* damn you kaizr

* cabinet

---
## [Starfly-13/STARFLY-13](https://github.com/Starfly-13/STARFLY-13)@[247a4e02ea...](https://github.com/Starfly-13/STARFLY-13/commit/247a4e02eab24ccfa191ea0447e587aeaf4c1235)
#### Tuesday 2023-12-19 01:14:53 by BluBerry016

{Icemoon, Ruin} The Crashed Holemaker (#2413)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Adds a brand-new - well, [new to
shiptest](https://cohost.org/bluwu016/post/885120-a-compilation-of-my) -
ruin to the Icemoon roster, focused on the service department.

It's flavored around being an *incredibly* old NT Spaceworks vessel
that's been carved in half and crashed - what's present only being the
fore of the ship. Being mainly service-focused, it's loot is pretty dry
~~as is it's sole threat.~~
If more current-day mappers/balance-heads have any words about how to
fluff out either of those pools a bit more with the screenshots below,
lemme know. I'll listen well.

(Notarized loot summary removed as updating it was a pain in the ass,
lmao.)

It strikes me as leaning on the underwhelming side from looking at the
other ruins present here but we'll. See? I suppose? It's good practice
for me in the whole, "making something I have memorized and that looks
good normally look sicker ruined".

<details><summary>Pictures (All but SDMM Outdated)</summary>
<p>

Ignore that there's no rust, the firelocks are open here, and some
stuff's knocked around, I was testing it prior to me tacking the rust on
and took pics after running around it in-person.


![image](https://github.com/shiptest-ss13/Shiptest/assets/50649185/51a3cc54-1727-4241-9592-639f892621bf)


![image](https://github.com/shiptest-ss13/Shiptest/assets/50649185/580e39fe-bbf9-481f-aff8-cc25f860638d)

StrongDMM View:

![2023-11-09 15 02
20](https://github.com/shiptest-ss13/Shiptest/assets/50649185/5b94af63-d2d8-42bd-a823-0d300d66191f)

</p>
</details> 
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
This isn't what I intended to do when I was like, "oh yeah, I have a
goofy ahh downstream out of boredom, ya'll want some of our better
ships" but w/e here it is anyways. Ya'll need ruins. I made (another)
ruin.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: A new icemoon ruin has been added, should you be in need of service
department goodies.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: BluBerry016 <50649185+unit0016@users.noreply.github.com>

---
## [Stutternov/f13tbd](https://github.com/Stutternov/f13tbd)@[667500fde5...](https://github.com/Stutternov/f13tbd/commit/667500fde5871478747cdd48d7624dab6bb42c8f)
#### Tuesday 2023-12-19 01:52:12 by Stutternov

Fire Delay Fix & Bolt Action Overhaul (#366)

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

So - funny thing. Fire delay NEVER worked properly on this codebase
since the change of the way fire delay worked to a different proc.

I have reversed this and re-adjusted fire delays for guns, at people
clearly were balancing them around the 'fire_delay' proc that wasn't
working. While some guns had 0 fire delay and seemed to function fine,
upon fixing - you realize **"Oh this fires literally as fast as you can
possibly click."**

As such, this is an attempt at balancing gun fire delays. Honestly -
this is a great thing, since I think with these new values (which need
to be tested a bit first) that guns like the Rangemaster and M1 garand
are finally viable alternatives to, say, the DKS. The main issue I see
is guns will be firing faster in some ways across the board due to this
fix so we'll need to slowly fix this via testing to where a gun should
be.

**Bolt actions have also been overhauled.**
Bolt actions are now viable again, as they are better damage, some
bullet speed, and being relatively equal to their automatic
counterparts. Their downside is the fact they are bolt action and, for
some, have limited capacities.

The Remington, for example, now does near equal damage to the DKS but
only has a 5 round capacity, less penetration, and is stripper-clip fed.

The Varmint has also been re-made into a boltaction rifle, effectively
being a 'near equal' to the service rifle albeit bolt-action. It has
some extra pen (only by about 0.1) and extra speed to its bullets,
making it more of a marksman rifle rather than putting bullets down
range better.

**Misc balance adjustments**
Since firedelay needed to be changed, since we have kept changing fire
delays.. despite them not fucking working, guns like the Marksman have
been buffed while others, like the R-91, have had their role
re-evaluated some.

Examples:
- Marksman carbines are now same fire delay as service rifles, but due
to rarity pack some extra damage and penetration in exchange for a bit
more slowdown.
- R-91 lost its damage malice but also its extra pen, instead making it
more of a good automatic weapon.

## Why It's Good For The Game

Either an oversight or a really silly change that broke fire delays on
guns for quite awhile now. Other changes to balance were needed to
balance guns against eachother.

## Pre-Merge Checklist
<!-- Don't bother filling these in while creating your Pull Request,
just click the checkboxes after the Pull Request is opened and you are
redirected to the page. -->
- [X] You tested this on a local server.
- [X] This code did not runtime during testing.
- [X] You documented all of your changes.
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
balance: Re-balances ALL gun fire delays.
fixes: Removed CD_Firedelay in gun proc in exchange for the ACTUALLY
used fire_delay proc
tweak: Moves varmint rifle to being bolt action as well as its variants.
Also buffs them to be competitive while being bolts.
balance: Re-does quite a few guns (Marksman, hunting rifle, remington,
R-91, etc) to make them balance against eachother better due to firerate
changes.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: macha <likeacompleteboss@gmail.com>
Co-authored-by: maaacha <116771811+maaacha@users.noreply.github.com>

---
## [YunxianHua/ros2_ws](https://github.com/YunxianHua/ros2_ws)@[c1e2906377...](https://github.com/YunxianHua/ros2_ws/commit/c1e2906377becb3819507b9634468c651d3d823a)
#### Tuesday 2023-12-19 01:55:19 by fei.gao

feat: x86 workflow, but still not work for aarch (#8)

* pay no attention to the man behind the curtain

* refuckulated the carbonator

* Committing in accordance with the prophecy.

* holy shit it's functional

* By works, I meant 'doesnt work'.  Works now..

* Popping stash

* Fucking submodule bull shit

---
## [Clarence5/react](https://github.com/Clarence5/react)@[b6978bc38f...](https://github.com/Clarence5/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Tuesday 2023-12-19 02:39:47 by Andrew Clark

experimental_use(promise) (#25084)

* Internal `act`: Unwrapping resolved promises

This update our internal implementation of `act` to support React's new
behavior for unwrapping promises. Like we did with Scheduler, when 
something suspends, it will yield to the main thread so the microtasks
can run, then continue in a new task.

I need to implement the same behavior in the public version of `act`,
but there are some additional considerations so I'll do that in a
separate commit.

* Move throwException to after work loop resumes

throwException is the function that finds the nearest boundary and
schedules it for a second render pass. We should only call it right 
before we unwind the stack — not if we receive an immediate ping and
render the fiber again.

This was an oversight in 8ef3a7c that I didn't notice because it happens
to mostly work, anyway. What made me notice the mistake is that
throwException also marks the entire render phase as suspended
(RootDidSuspend or RootDidSuspendWithDelay), which is only supposed to
be happen if we show a fallback. One consequence was that, in the 
RootDidSuspendWithDelay case, the entire commit phase was blocked,
because that's the exit status we use to block a bad fallback
from appearing.

* Use expando to check whether promise has resolved

Add a `status` expando to a thrown thenable to track when its value has
resolved.

In a later step, we'll also use `value` and `reason` expandos to track
the resolved value.

This is not part of the official JavaScript spec — think of
it as an extension of the Promise API, or a custom interface that is a
superset of Thenable. However, it's inspired by the terminology used
by `Promise.allSettled`.

The intent is that this will be a public API — Suspense implementations
can set these expandos to allow React to unwrap the value synchronously
without waiting a microtask.

* Scaffolding for `experimental_use` hook

Sets up a new experimental hook behind a feature flag, but does not
implement it yet.

* use(promise)

Adds experimental support to Fiber for unwrapping the value of a promise
inside a component. It is not yet implemented for Server Components, 
but that is planned.

If promise has already resolved, the value can be unwrapped
"immediately" without showing a fallback. The trick we use to implement
this is to yield to the main thread (literally suspending the work
loop), wait for the microtask queue to drain, then check if the promise
resolved in the meantime. If so, we can resume the last attempted fiber
without unwinding the stack. This functionality was implemented in 
previous commits.

Another feature is that the promises do not need to be cached between
attempts. Because we assume idempotent execution of components, React
will track the promises that were used during the previous attempt and
reuse the result. You shouldn't rely on this property, but during
initial render it mostly just works. Updates are trickier, though,
because if you used an uncached promise, we have no way of knowing 
whether the underlying data has changed, so we have to unwrap the
promise every time. It will still work, but it's inefficient and can
lead to unnecessary fallbacks if it happens during a discrete update.

When we implement this for Server Components, this will be less of an
issue because there are no updates in that environment. However, it's
still better for performance to cache data requests, so the same
principles largely apply.

The intention is that this will eventually be the only supported way to
suspend on arbitrary promises. Throwing a promise directly will
be deprecated.

---
## [CirnoDayo/EnRoute-Prototype-V1](https://github.com/CirnoDayo/EnRoute-Prototype-V1)@[7bf762c914...](https://github.com/CirnoDayo/EnRoute-Prototype-V1/commit/7bf762c914a2811e5996f63995f859efb8bf19c0)
#### Tuesday 2023-12-19 02:48:02 by ZuTahi

I added the cam movement for the Nav scene

Dashing through the snow
In a one-horse open sleigh
O'er the fields we go
Laughing all the way
Bells on bobtails ring
Making spirits bright
What fun it is to ride and sing
A sleighing song tonight, oh!

Jingle bells, jingle bells
Jingle all the way
Oh, what fun it is to ride
In a one-horse open sleigh, hey!
Jingle bells, jingle bells
Jingle all the way
Oh what fun it is to ride
In a one-horse open sleigh

Now the ground is white
Go it while you're young
Take the girls tonight
Sing this sleighing song
Get a bobtailed bay
Two forty for his speed
And hitch him to an open sleigh
And you will take the lead

Oh, jingle bells, jingle bells
Jingle all the way
Oh, what fun it is to ride
In a one-horse open sleigh, hey!
Jingle bells, jingle bells
Jingle all the way
Oh, what fun it is to ride
In a one-horse open sleigh
Oh, what fun it is to ride
In one horse open sleigh!

---
## [Aylong220/Paradise-SS220](https://github.com/Aylong220/Paradise-SS220)@[d1377939b9...](https://github.com/Aylong220/Paradise-SS220/commit/d1377939b9ac81e23f105057f8777e8d7d75fd4b)
#### Tuesday 2023-12-19 03:06:32 by Aylong

Squash TGchat

rebuild

axios

STOP PAINT THE FUCKING INPUT

Command line, fucking finally

RegEx

Highlights

More shit

Revert "Revert "Scroll fix""

This reverts commit f63ef764884a55479cb7a36403b16fd142492f40.

Revert "Scroll fix"

This reverts commit 44dbfcc3c08bd46682701f41b0b17ff128de7a15.

Scroll fix

No null to_chat

Dropdown and font

Stoopid

Fix fix chat and IE8

Prevent Ctrl+F passthrough, Fix regressions #53012

TGUI 4.2 and chat fixes

515 fix?

Colors

oops

Update reloader.js

Fixes

Styles

TGUI Panel

Base TGUI JS

Massive Delete Programm

Update iconprocs.dm

Core TGUI

SSchat

---
## [ReturnToZender/ReturnsBubber](https://github.com/ReturnToZender/ReturnsBubber)@[2e656fba14...](https://github.com/ReturnToZender/ReturnsBubber/commit/2e656fba14e0b67086bb4d2eff59d6fa6748a55c)
#### Tuesday 2023-12-19 03:18:42 by Cursor

Grants the ability to open Clown slots once more. (#853)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Title. Skyrat disabled it because they hate fun. We don't.

<!-- Please make sure to actually test your PRs. If you have not tested
your PR mention it. -->

## Why It's Good For The Game

Say a Clown dies. Is arrested, or is just a bit shit.
What can you do?
Jackshit.
Pray, fax Clown Planet, but why wait on God or the Clown in the High
Castle when you can do it yourself?
This also let's Antags, or Clowns summon more friends. Assuming people
in the lobby wanna be a clown.

P.S. I commented out and unticked the Skyrat file for double safety.
Tried to just override it, didn't work. If you have a better idea for
this. You have the floor.

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
add: Clown slots are re-openable by royal decree. The incident between
Nanotrasen and King Honkington has been resolved.
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

---------

Co-authored-by: Waterpig <49160555+Majkl-J@users.noreply.github.com>

---
## [KittyNoodle/Monkestation2.0](https://github.com/KittyNoodle/Monkestation2.0)@[1e9edd6a49...](https://github.com/KittyNoodle/Monkestation2.0/commit/1e9edd6a49665dc9ae5e857e72455961be4f8230)
#### Tuesday 2023-12-19 03:38:17 by Kittynoodle

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
## [Noway-code/Checked](https://github.com/Noway-code/Checked)@[61ed9fcbeb...](https://github.com/Noway-code/Checked/commit/61ed9fcbebb4b632c86ebbd650ca56d8087a68b6)
#### Tuesday 2023-12-19 04:53:24 by noway

remove node modules from main branch
Our Father, Who art in heaven, Hallowed be Thy Name. Thy Kingdom come, Thy Will be done, On earth as it is in Heaven. Give us this day, our daily bread, And forgive us our trespasses, as we forgive those who trespass against us. And lead us not into temptation, but deliver us from evil.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[8491adc6b5...](https://github.com/treckstar/yolo-octo-hipster/commit/8491adc6b5b32f6eb71d015c22155ea28e55b443)
#### Tuesday 2023-12-19 05:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [builtwithai/PixArt-alpha](https://github.com/builtwithai/PixArt-alpha)@[e8682374f2...](https://github.com/builtwithai/PixArt-alpha/commit/e8682374f2ea49c2046c3fbca7e9192c87fe56dd)
#### Tuesday 2023-12-19 05:28:55 by SKi

feat: Add celeb avatar generation

We've made exciting changes in this commit, we added two new lists 'celebs' and 'mcelebs' that contain the names of famous female and male celebrities. We also added a new function 'createAvatarPrompt' which generates avatar prompts by randomly choosing celebrities from the 'celebs' list.

We also made changes to 'createRandomPrompt' function, reduced the range from 1000 to 10. The 'prompts' list now generates 10 random prompts using 'createRandomPrompt' then prints them. The 'prompts' list is then cleared and generates 10 avatar prompts using 'createAvatarPrompt' and prints them.

Also in 'test.py', we modified code to generate 100 avatar prompts using 'createAvatarPrompt' instead of generating random prompts.

This feature is bringing creativity to another level and enhancing user experience with celebrity avatar generation.

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[55f9dd8d39...](https://github.com/cmss13-devs/cmss13/commit/55f9dd8d39bcdd3a1e6c8c72f128c6f4447111dc)
#### Tuesday 2023-12-19 05:46:52 by fira

/tg/ Status Effects Part 2 - datum, KD, KO, Stuns (#4842)

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

Part 2 - this includes porting the actual status_effect datum, modifying
it to fit our purposes by backing it with timers similarly to old
system, and finally implementing KD, KO and Stun with it.

This contains Part 1 PR (#4828) so if you want to take a look at it I'd
advise checking the last commits or setting up a compare between both
branches.

# Explain why it's good for the game
Predictable status timers. Current ones are bogus in their handling of
"life tick correction" and will "stack" time even when they're not
supposed to.

Also provides a more robust backend for general effects, and integrates
status effects into it.

# Testing Photographs and Procedure

Summary testing of buckling interactions, explosion knock times,
crawling, resting. Will have to be expanded once part 1 is ready


# Changelog
:cl:
add: Added Buckled, Handcuffed and Legcuffed screen alerts
code: Ported /tg/ status effects backend, modified with timers to let
effects end at appropriate time
code: Stun, Knockdown and Knockout now use the new effects backend
balance: Due to backend change, all KO/KD/Stuns may behave differently
timing wise. This is of course subject to adjustments.
balance: Endurance is now set at 8% effect duration reduction per level
above 1. However it now compounds with species bonus. Feel free to
adjust.
balance: Knockdowns are not inherently incapacitating anymore and many
sources of it have been updated to also stun to make up for it.
fix: KO/KD/Stuns do not artificially and randomly ''stack'' due to
incorrect timer offset calculation anymore.
fix: Stuns now correctly apply Stun reduction values instead of
Knockdown reductions.
fix: Crawling can now be interrupted by a normal move, if you are fit
enough to do so.
/:cl:

---------

Co-authored-by: forest2001 <41653574+realforest2001@users.noreply.github.com>

---
## [Draganfrukts/f13tbd](https://github.com/Draganfrukts/f13tbd)@[4bd789088c...](https://github.com/Draganfrukts/f13tbd/commit/4bd789088c9dbf0382b855f1cbd3af46d37c9295)
#### Tuesday 2023-12-19 06:22:34 by Dragonfruits

The Great Shotgun Debacle (+ AMR tweaks) (#352)

### The Summary
This PR cleans up shotgun code some by getting rid of unused ammo,
removes trainshot, nerfs slugs, substantially nerfs double barrel
shotguns, and buffs the AMR slightly.

### The Why
_**The slug nerf**_
Literally outclasses most mid-high tier guns. Does more damage than 7.62
with more AP yet it's infinitely easier to find, make, and store. Does
insane damage to literally fucking everything.

_**YOU REMOVED TRAINSHOT I FUCKING HATE THIS, THIS IS THE WORST THING
EVER, THE GAME IS RUINED, SHOTGUNS ARE USELESS, I'M GONNA KILL MYSELF**_
Trainshot has all the benefits of slugs, and all the benefits of
buckshot, on top of being better in literally every way imaginable,
locked behind a magazine. It completely kills any niche you obtain by
switching ammo types on your shotguns.

_**The AMR buff**_
It's currently too weak to justify its terrible handling. The buff isn't
substantial, but it helps it shine more, especially in PVE.

**_The DB nerf_**
They literally had up to 15% bonus AP. I don't know what the fuck I was
thinking one year ago but this created the most hilariously broken shit
ever. Now the only shotgun with AP and damage bonuses is, rightfully,
the single-shot.

### Show me the numbers.

_**Slugs**_
_DAMAGE 40 > 35_
_STAMINA DAMAGE 15 > 0_
_BARE WOUND BONUS 30 > 0_
_ARMOR PENETRATION 30% > 15%_
_SUPERFFECTIVE DAMAGE 50 > 35_

_**Buckshot**_
_DAMAGE 11.5 > 12_
_WOUND BONUS 35 > 40_
_WOUND BONUS FALLOFF 15.5/Tile > 20/Tile_
_SUPEREFFECTIVE DAMAGE 9.5 > 3_

_**.50 MG**_
_DAMAGE 45 > 50_
_STAMINA DAMAGE 0 > 45_
_WOUND BONUS 30 > 35_
_BARE WOUND BONUS 40 > 80_
_SUPEREFFECTIVE DAMAGE 60 > 150_

---
## [Draganfrukts/f13tbd](https://github.com/Draganfrukts/f13tbd)@[4e65d6a243...](https://github.com/Draganfrukts/f13tbd/commit/4e65d6a24380d3feb6682ff7910bc6ea5a7ef0c8)
#### Tuesday 2023-12-19 06:22:34 by GreytidePanda

Makes Flypeople Viable (#344)

## About The Pull Request
The flyperson race was basically a death sentence for two reasons:
1. Flypeople gain no nutrients and just vomit upon eating normal food,
but eating the vomit then gets the nutrients they need. _Or is supposed
to._ Despite a lot of fancy code vomit gave them no nutrients at all.
2. When flypeople begin (due to the first issue, inevitably) starving to
death, they can't vomit at all and can only dry heave, which means that
even if vomit did give nutrients they'd be unable to make any and would
be in deep trouble. This led to a dry heaving death spiral that was
hilarious but silly.

![image](https://github.com/f13babylon/f13babylon/assets/132588088/f19bdbdb-e566-4b0c-9f6d-09c0cf051db4)

The new code is much less elegant but actually works. tl;dr vomit now
gives a flat nutrient amount (only flypeople can eat it anyway) and the
dry heave mechanic is skipped if you're a flyperson.

## Why It's Good For The Game
This race is actually playable now. I imagine this would have been
caught sooner but only one weirdo wants to play them. Well I hope they
are happy. : )

## Pre-Merge Checklist
- [x] You tested this on a local server.
- [x] This code did not runtime during testing.
- [x] You documented all of your changes.

## Changelog
:cl:
fix: Fixes flyperson hunger mechanics.
/:cl:

---
## [Draganfrukts/f13tbd](https://github.com/Draganfrukts/f13tbd)@[bdb724a900...](https://github.com/Draganfrukts/f13tbd/commit/bdb724a90019aadd90cfb1df2dced35978b6d98e)
#### Tuesday 2023-12-19 06:22:34 by GreytidePanda

Big Customisation Update (#339)

## About The Pull Request

![anyinterest](https://github.com/f13babylon/f13babylon/assets/132588088/ea961bfc-390f-42ec-83ea-0fe69d48bb86)

Adds in 269 new customisation parts. Many were ported and some were
already in our codebase one way or another.

A few existing broken parts (no sprite and I can't find one anywhere)
were removed. There was also an effort to alphabetise the part lists
more, sort out the dmis (mam_markings.dmi is looking really neat now,
check it out) and integrate modularised content (goodbye citadel
snowflake.dm)

Also, species that were allowed hair but not facial hair were lifted
from this restriction. (This is anthromorphs, synthetic anthromorphs,
and synthetic lizardpeople.) This is especially useful for the new horn
and tongue parts they have.

This was not a straight port - it took a while and I playtested it a
bunch. But please please test merge first, there is a lot.

-59 New Hairstyles
> African Pigtails, Afro Puff Double, Afro Puff Left, Afro Puff Right,
Astolfo, Baum, Belenko Tied, Belenko, Bluntbangs Alt, Bluntbangs, Cobra
Hood, Combed Back, Combed Bob, Cotton Alt, Cotton Belle, Cotton
Pigtails, Diagonal Bangs, Fortune Teller, Froofy, Geisha, Glam Metal,
Hajime Alt, Hajime, Half-Shaved Glamorous, Half-Shaved Long Messy,
Half-Shaved Long, Half-Shaved Messy, Harold, Long Straight Hair w/ Twin
Tails, Long Fringe Alt, Pigtail Advanced, Quadcurls, Rockstar, Sharp
Tail, Slightly Messy, Spicy, Tailhair, Vox Afro, Vox Crested Quills, Vox
Cropped, Vox Emperor Quills, Vox Hawk, Vox Horns, Vox Keel Quills, Vox
Keet Quills, Vox Kingly, Vox Mangy, Vox Mohawk, Vox Nights, Vox
Ponytail, Vox Razor, Vox Razorclipped, Vox Rows, Vox Short Quills, Vox
Surf, Vox Tiel Quills, Vox Yasu, Wife, Zone

-9 New Facial Hairs
> Face Horns, Chin Horns, Lizard Lick, Lizard Lick Fast, Lizard Lick
Slow, Nose Lick, Nose Lick Fast, Nose Lick Slow, Tusks

-16 New Horns

> Antlers Wide, Billberry, Curly, Dragon, Dragon Inverted, Jackalope,
Lizard, Ram Curled, Ram Curled Alt, Ram Small, Ram Small Alt, Ram Small
Alt 2, Stabbers, Teppi, Unicorn, Upwards

-45 New Ears

> Antennae Face Alt, Antennae Face, Antennae Moth, Antennae Plume,
Antennae Round, Antennae Thin, Avali, Big Wolf Both Piercings, Big Wolf
Left Piercing, Big Wolf Right Piercing, Bunny Alt, Bunny Floppy, Bunny
Long Alt, Bunny Long, Bunny Tall Alt 2, Bunny Tall Alt, Bunny Tall, Cat
Alt, Deer Alt, Eastern Dragon, Fan, Full Frill, Goat Horns, Goat, Gret,
Jackal, Jackalope Tall, Long Frill, Lunasune, Miqo'te, Mouse Alt, Noodle
Dragon, Pig, Pointy, Rosey, Sabresune, Sandfox Tall, Shadekin Tall,
Shock, Spaniel, Split Frill, Teppi, Trike, Umbreon, Vaporeon

-47 New Snouts

> Beak Corvid, Beak Tiny, Cow, Deer, Deoxys, Duck, Eastern Dragon,
Eastern Dragon Female, Eastern Dragon No Whiskers, Eastern Dragon No
Whiskers, Female, Fox, Fox Alt, Goose, Magus, Mandible Big, Mandible
Small, Orca, Otter, Owl, Proboscis, Rabbit, Rad-Dog, Rad-Dog Top, Rhino
Beetle, Round Classic, Round Classic Top, Round + Light Classic, Round +
Light Classic Top, Scarab, Sharp Alt, Sharp Classic, Sharp Classic Top,
Sharp + Light Classic, Sharp + Light Classic Top, Short Alt, Skullbird
Female, Skullbird Male, Sloog, Sloog Alt, Snub, Spider, Tajaran, Tajaran
Short, Tarantula, Vulp, Vulp Alt, Zebra

-36 New Markings

> Abdominals 2-Tone, Abdominals 3-Tone, Abdominals, Backsail, Bands, Bee
Alt, Bee Fluffy, Beetle, Belly Scutes, Belly Tajaran Full, Belly
Tajaran, Body Gloss, Datashark, Dino Head, Eastern Dragon, Gradient,
Moth, Patches, Paw Socks, Pigeon, Raccoon Alt, Rad-Dog, Sabresune,
Shrike, Stego Chestplate, Stripes Back, Stripes Tiger, Tattoo Blush,
Tattoo Campbell, Tattoo Lip, Tattoo Nightling, Tattoo Silverburgh,
Tattoo Tiger, Trike Beak, Trike Horn, Umbreon

-12 New Wings

> Angel Moth, Harpy Arm Wings Alt Collar, Harpy Arm Wings Alt, Harpy Arm
Wings Bat Collar, Harpy Arm Wings Bat, Harpy Arm Wings, Lugia,
Pterodactyl, Robotic Alternate, Spider Legs Fuzzy, Spider Legs Plain,
Spider Legs Spiky

-45 New Tails

> Bee Stinger, Gecko Big, Big Ring, Cat Slug, Club, Corgi, Demon Spade,
Double Fox, Eastern Dragon, Feather, Furret, Gecko, Glaceon, Hawk Short,
Insect 2 Tone, Kangaroo Large, Leafeon, Lizard Large, Long Fluff,
Lunasune, Nightstalker Large, Ninetales, Octopus, Peacock Female,
Peacock Male, Pig, Pigeon Long, Pigeon Short, Pony Alt 1, Pony Alt 2,
Pony Alt 3, Porkapine, Raptor, Sabresune, Snake Large, Snep, Spike,
Succubus, Swallow Striped, Swallow, Tail Maw, Turkey, Umbreon, Western
Dragon Large, Xeno

## Why It's Good For The Game
More customisation options are always good.

## Pre-Merge Checklist
- [x] You tested this on a local server.
- [x] This code did not runtime during testing.
- [x] You documented all of your changes.

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
add: Added a lot more customisation options (hairs, ears, wings, etc)
/:cl:

---
## [littlefs-project/littlefs](https://github.com/littlefs-project/littlefs)@[eb6c361dfa...](https://github.com/littlefs-project/littlefs/commit/eb6c361dfa6ee2179679c8cf9098fb6dc74c930d)
#### Tuesday 2023-12-19 06:49:09 by Christopher Haster

Adopted lazy orphaned mdir drops

This ended up being much less of a simplification than I hoped it would.

It's still easier/more efficient to revert to a relocation in most cases
when dropping in an mdir split, and the small gain from simplifying how
drops/commits interact is overshadowed by the code duplication necessary
to separate lfsr_mdir_drop out from lfsr_mdir_commit:

            code          stack
  before:  30952           2528
  after:   31280 (+1.1%)   2648 (+4.7%)

Still, this does at least simplify the logical corner cases (we don't
need to abort commits when droppable anymore), and lfsr_mdir_drop is
ultimately necessary for supporting lazy file creation.

Also having a fix-orphans step during mount allows other littlefs
implementations the option to create orphanned mdirs without compat
issues. So this ends up the more flexible approach.

It _might_ be worth having both eager mdir drops and an explicit
lfsr_mdir_drop for lazy file creation in the future, but I doubt this
will end up worth the code duplication...

---

Oh right, I forgot to actually describe this change.

This trades eager mdir drops:

1. Drop mdirs from the mtree immediately as soon as their weight goes
   to zero.

For lazy mdir drops:

1. Drop mdirs from the mtree in a second commit.
2. Scan and drop orphaned mdirs on the first write after mount.

This sounds very similar to the previous "deorphan" scan, which risked
an extreme performance cost during mount, but it should be noted this
orphan scan only needs to touch every mdir once. This makes it no worse
than the overhead of actually mounting the filesystem.

We can also keep an eye out for orphaned mdirs when we mount, so no
extra scan is needed unless there was an unlucky powerloss.

Eager mdir dropping sounds simpler, but thanks to deferred commits
introduces some subtle complexity around aborting commits that would
drop an mdir to zero. Remember commits are viewable on-disk as soon as a
commit completes.

In _theory_, lazy mdir drops simplify the logic around committing to
mdirs.

Though the real kicker is that lazy mdir drops are required for lazy file
creation.

The current idea for lazy file creation involves tracking mid-less
opened-but-not-yet-created files. These files can have bshrubs, so they
need space on an mdir somewhere. But they aren't actually created yet,
so they don't have an mid.

This is fine (though it's probably going to be tricky) as long as we
allocate an mid on file sync, but there is always a risk of losing power
with mdirs that contain only RAM-backed files. Fortunately, no-mids
means no orphaned files, but it does mean orphaned mdirs with no synced
contents.

Long story short, lazy mdir drops are currently a necessary evil, and
logical simplification, that unfortunately comes with some cost.

---
## [ProjectMatrixx/android_vendor_addons](https://github.com/ProjectMatrixx/android_vendor_addons)@[0a2885706f...](https://github.com/ProjectMatrixx/android_vendor_addons/commit/0a2885706fbf9a604e0f0025842a7f848accb879)
#### Tuesday 2023-12-19 06:52:44 by Pranav Vashi

[SQUASH]: Import common overlays
- neobuddy's commits:
01]- addons: Add initial values-night
02]- addons: Update styles for night mode
03]- addons: Fix panel color background for dark theme
04]- addons: Play with darkness
05]- addons: Darker..
06]- addons: Clean up overlay night colors
07]- addons: Set proper dark color for emergency icon in power menu
08]- addons: Set color for qs tile disabled in dark mode
09]- addons: Update default colors
10]- addons: Fix resolver colors for dark theme
11]- addons: Clean up and fix night style
12]- addons: Add more accent magic
13]- addons: Fix up dark mode styles
14]- addons: Update colors for global screenshot buttons
15]- addons: Lighten up screenshot button borders

- ElDainosor's commits:
16]- addons: Fix share copy icon color and change personal apps color
17]- addons: More theming for screenshot and other elements

- SKULSHADY's commits:
18]- addons: Fix Biometric dialog corner radius

- neobuddy's commits:
19]- addons: Update color overlay for screenshot buttons
20]- addons: Clean up old theming

- kdrag0n's commits:
21]- addons: Add chroma to light surface highlight color
22]- addons: Use default surface colors for power menu buttons
23]- addons: Remove power menu shadow
24]- addons: Use accent color for progress bar background

- minaripenguin's commit:
25]- addons: Add dark mode support for colorAccentPrimary

Co-authored-by: ElDainosor <eldainosor@gmail.com>
Co-authored-by: kdrag0n <danny@kdrag0n.dev>
Co-authored-by: minaripenguin <minaripenguin@users.noreply.github.com>
Co-authored-by: SKULSHADY <anushekprasal@gmail.com>
Signed-off-by: Pranav Vashi <neobuddy89@gmail.com>
Signed-off-by: mukesh22584 <mks22584@gmail.com>

---
## [Mu-L/zola](https://github.com/Mu-L/zola)@[22dc32a589...](https://github.com/Mu-L/zola/commit/22dc32a5893deac5e91d173d0daf59e1868065ef)
#### Tuesday 2023-12-19 06:55:28 by sinofp

Add support for lazy loading images (#2211)

* Add optional decoding="async" loading="lazy" for img

In theory, they can make the page load faster and show content faster.

There’s one problem: CommonMark allows arbitrary inline elements in alt text.
If I want to get the correct alt text, I need to match every inline event.

I think most people will only use plain text, so I only match Event::Text.

* Add very basic test for img

This is the reason why we should use plain text when lazy_async_image is enabled.

* Explain lazy_async_image in documentation

* Add test with empty alt and special characters

I totaly forgot one can leave the alt text empty.
I thought I need to eliminate the alt attribute in that case,
but actually empty alt text is better than not having an alt attribute at all:
https://www.w3.org/TR/WCAG20-TECHS/H67.html
https://www.boia.org/blog/images-that-dont-need-alternative-text-still-need-alt-attributes
Thus I will leave the empty alt text.

Another test is added to ensure alt text is properly escaped.
I will remove the redundant escaping code after this commit.

* Remove manually escaping alt text

After removing the if-else inside the arm of Event::Text(text),
the alt text is still escaped.
Indeed they are redundant.

* Use insta for snapshot testing

`cargo insta review` looks cool!

I wanted to dedup the cases variable,
but my Rust skill is not good enough to declare a global vector.

---
## [AcademySoftwareFoundation/OpenImageIO](https://github.com/AcademySoftwareFoundation/OpenImageIO)@[64248a6e52...](https://github.com/AcademySoftwareFoundation/OpenImageIO/commit/64248a6e52c00e96b857756520edf539b933698d)
#### Tuesday 2023-12-19 07:57:54 by Larry Gritz

feat(ImageBuf): make IB::Iterator lazy in its making the image writable (#4033)

Historically, ImageBuf has provided Iterator for writing to mutable IB's
and ConstIterator for reading into IBs. If you initialized an Iterator
to an IB that was ImageCache-backed (and therefore by definition not
mutable), it would convert the IB to the mutable kind (basically by
allocating the memory and reading the file through the IC, thus freeing
the IB of its dependence on the cache.

An important bug was fixed by PR 3997, which kinda proved that people
were not depending on this behavior, since it would tend to fail. But it
also got me thinking about to what degree the whole Iterator vs
ConstIterator was really necessary, or did it just make things harder
for users.

In this proposed patch, we change the Iterator behavior so that instead
of immediately making the IB writable as soon as the Iterator was
instantiated and associated with the IB, we instead treat it as a
ConstIterator UNTIL it actually tries to write a value, at which point
we ensure that the IB is writable.

The bottom line is that this seems to work. If you don't want to have to
think about Iterator vs ConstIterator, you don't have to. Iterator is
fine. If you don't actually write into any of the pixels, it behaves
just like a ConstIterator, including being perfectly happy with an
IC-backed IB. Performance metrics indicate that there is NO penalty for
doing so -- if you are only reading pixel values, traversing an IB with
Iterator is the same speed as doing it with ConstIterator.

I had one sleepless night after implementing this when suddenly I
realized that this was totally not thread-safe, that somehow multiple
iterators traversing the same IB would screw each other up if one of
them wrote to a pixel and converted the image. So I put in a test to
have many threads concurrently traversing the same IB, some with
ConstIterator, some with Iterator but only reading, and some with
Iterator and writing. I have not been able to trigger any failures or
crashes. It seems fine. (I did use the mutex a little more aggressively
than before.)

Why is this not as dangerous as I thought? Mainly because once an
iterator (of either variety) thinks it's dealing with an IC-backed
ImageBuf, basically, it will just happily keep using the IC all on its
own, even if the IB that it's supposedly traversing has, because another
thread's iterator has written to a pixel, "localized" the image and
severed the IC dependence. Then if it also needs to write, it will
(safely, because of a mutex) see that the image is already
localized/writable, and start using that representation.

So herein lies a very important caveat about using IB iterators: If you
have multiple iterators traversing the same IB and any of them are
*writing* to the image, the iterators may not see a globally temporally
consistent version of the image. Put in plain English: iterators that
are strictly reading may see an IC-backed disk image as it was on disk,
and not as it has since been modified by a different active iterator. So
if you are modifying an image in place, beware of using multiple
iterators, because a reading iterator may or may not see the changes
that a writing iterator made to a pixel value.

Signed-off-by: Larry Gritz <lg@larrygritz.com>

---
## [ODRI-the-human/HighSpeedVideoGaming](https://github.com/ODRI-the-human/HighSpeedVideoGaming)@[9bd7704454...](https://github.com/ODRI-the-human/HighSpeedVideoGaming/commit/9bd770445465b9f396548e5677058c3035957819)
#### Tuesday 2023-12-19 08:05:34 by Aidan Holdsworth

magnet kinda implemented

after a huge amount of time and effort and a 3-day period of my laptop not even posting so I couldn't work on this fucking mechanic, the magnet is in. I believe the camera flip and the switching hitbox positions, up direction and such works perfectly, but sometimes you don't properly land on surfaces and running/airtime is a little fucked atm. I don't think these will be as hard to do as the basic magnet implementation has been! (copium)

---
## [eurotools/eurochef](https://github.com/eurotools/eurochef)@[68cb5f5a27...](https://github.com/eurotools/eurochef/commit/68cb5f5a27ed7edacd499b80830fe15a33154854)
#### Tuesday 2023-12-19 09:01:02 by cohaereo

Fix binrw compile error

Whoever pushed a breaking change without incrementing major version, fuck you.

---
## [grafbase/grafbase](https://github.com/grafbase/grafbase)@[d84940b6f4...](https://github.com/grafbase/grafbase/commit/d84940b6f439b2171e69554420d852aad2865cae)
#### Tuesday 2023-12-19 09:26:42 by Benjamin Rabier

feat: Add extra fields support (requires, key fields) in the engine v2 (#1121)

The PR is again really big and likely not that readable... Sorry, again,
for that.

The goal of this PR is to add fields depending on the resolver
requirements (fields of `@key`) and the `@requires` of individual
fields. I'm only really testing the former for now, but they're treated
identically. It's tricky because the prepared `Operation` is shared
during execution and we're planning children on the fly (depending on
type conditions). So we're not modifying the `Operation` directly to
avoid a complex and/or poor locking mechanism. We also want to keep
`Operation` cacheable to bypass the parsing & binding steps later.

So to add extra fields, I'm keeping track of those in `plan.Attribution`
in an `extra_fields` and `extra_selection_sets` array, indexed by ids.
Initially, I tried without IDs, but we need this information at two
places:
- for the operation walkers: For each actual selection set within the
query, I'm tracking whether any extra fields need to be added. This
makes extra fields mostly transparent when building the GraphQL query
string for a subgraph.
- during deserialization of the upstream response: In `plan.expectation`
we construct the structure we expect from the upstream response and
build an appropriate `DeserializeSeed` implementation. This also needs
to be aware of extra fields. We wouldn't if GraphQL had no type
conditions, because we could generate the whole structure ahead of time
during planning. But for cases with complex type conditions where we
can't simplify it, we need to generate the expectations during
deserialization and thus need to merge extra selection sets.

The other tricky aspect of extra fields is that we need to ensure their
names won't collide with anything else in the upstream GraphQL response.
For resolvers that return static data without aliases (OpenAPI,
resolvers, etc.) it's just the field name, for GraphQL we need to find a
name during planning as the query string depends on it. So I ended up
with `_extra{short_hex(FieldId)}_{field_name}` as the base name. I
verify that it's not present in response keys. If it is, I'm adding an
integer suffix and looping over it until I find an available one.

To ensure that extra fields don't collide within the `Response` data
I've tweaked a bit the bit packing I do, and added better documentation
for it. I'm using a flag + `FieldId` to ensure its uniqueness. I've also
constrained all schema IDs to fit within 28 bits ensuring my current bit
packing (needs 2 bits) works and leaving some margin in case. It's still
268 million possible values, so good enough.

---
## [OrionTheFox/Skyrat-tg](https://github.com/OrionTheFox/Skyrat-tg)@[0304282fb9...](https://github.com/OrionTheFox/Skyrat-tg/commit/0304282fb9581bf6d3a3c2a0eeb9d06ba71e93d3)
#### Tuesday 2023-12-19 09:37:05 by SkyratBot

[MIRROR] Blood brothers is now a single person conversion antagonist [MDB IGNORE] (#25338)

* Blood brothers is now a single person conversion antagonist (#79971)

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

* Blood brothers is now a single person conversion antagonist

* Update oneclickantag.dm

---------

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>
Co-authored-by: Giz <13398309+vinylspiders@users.noreply.github.com>

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[a5fabd8819...](https://github.com/LemonInTheDark/tgstation/commit/a5fabd881961cc0c26fdcc93a23a973af1c5cdc3)
#### Tuesday 2023-12-19 10:54:57 by Profakos

Changes to the lore of Knock (#79542)

## About The Pull Request

This PR renames Knock to Lock, and changes most of the knowledge gain
lore.

## Why It's Good For The Game

The Knock Lore, is based on the Knock Principle from Cultist Simulator,
with the path description being copied from the wiki. Many other
keywords and concepts are fully lifted from that game (Locksmith's
Secret, Mother Of Ants, etc). In my vision, if a heretic path has to be
based on a principle from cultist simulator, it should have its own
spin, and also, the knowledge gain texts should tell a story. For
example, Ash tells the story of a watchman burning down their city after
being betrayed, and Cosmic is a love story between a knowledge seeker
and a monster from the beyond.

So I have decided to reflavour Knock. I have changed the name to Lock,
so at least it would feel similar, just like how Blade is akin to Edge.
Many powers also block people or confuse their paths instead of opening
new ways, and thus, I feel a path whose name implies that it *both*
opens and closes would be more self describing.

I have changed most of its lore to be about the Locked Labyrinth, where
knowledge seekers willingly trap themselves and submit themselves to
servitude to find ultimate freedom by progressing through its trials.
These are the Stewards, who are basically workers in an infinite and
malicious hotel in their dreams. Consider them assistants if you will
(this wasn't my intention when I wrote the lore, but thinking about it
in retrospect, it honestly fits). In the implied story, the heretic
joins their ranks, but keeps getting closer to the more corrupt members,
along with parasitic spirits. Ultimately, they manage to open the
Labyrinth's core, letting out the Stewards, allowing them to manifest in
the forms of heretic summon creatures.

The side path spells and the lock knowledge ritual I have not touched,
they were fine. Some items have been renamed and repathed.

I have kept the distinctive sound effect for using the Grasp, as its
unique enough. Though if someone did have a nice sound effect for
turning a lock and added some filters, I would add it.

**DB Issue**

I have renamed the achievement's define to MEDAL_LOCK_ASCENSION but kept
the value as "Knock", as I don't know how trigger a change in the DB. If
this is a blocking change, I'll try to figure out how to make a
migration file.

**Future improvements**

I would also come back later with another PR, that hands out names to
the eldritch beings spawned by the portal, based on the Stewards in the
knowledge gain lore that I added, along with some new ones that fit the
theme, and some jokey ones like Minotaur.

## Changelog

:cl:
spellcheck: Renamed Knock to Locks, and changed most of the flavor text
of knowledge gain, and renamed some items and knowledges from the path.
/:cl:

---
## [GymBuddy-Corporation/GymBuddyProject](https://github.com/GymBuddy-Corporation/GymBuddyProject)@[3d1be14aad...](https://github.com/GymBuddy-Corporation/GymBuddyProject/commit/3d1be14aad9be0448ff65a6b25ea939fbed9543a)
#### Tuesday 2023-12-19 11:54:21 by Luca Martorelli

Added Interfaces RequestBean and WorkoutRoutineBean

I also did:
- Removed the add/delete exercise from WorkoutRoutineBean of the SatisfyWorkoutRoutineRequestGUIController from the SatisfyWorkoutRequestsController and insert those things directly in the GUIController.

- KINDA solved all the stupid view bugs where the exercises weren't shown as they should have been. IMPORTANT: learn very well wtf happens in this shit code, I did things by tentatives and this code is son of many hours of hard work, that isn't, although clear.

---
## [urbit/urbit](https://github.com/urbit/urbit)@[58f2d427ce...](https://github.com/urbit/urbit/commit/58f2d427ce76f461732f53b0810afdedddd9b7e7)
#### Tuesday 2023-12-19 12:16:02 by Liam Fitzgerald

gall: security primitives for encrypted scry

This commit adds `%tend` `%germ` and `%snip` to the notes that gall can
pass. `%tend` is analogous to `%grow`, except with a security group defined
by .coop.

 ### The coop system
A `$coop` is a path, which defines a security context for the portion of
the namespace that it prefixes. Each `$coop` receives a symmetric key,
which is used to encrypt requests and responses for any key-value pair
belonging to a coop.

 ### Network overview
This design requires a single handshake over ames to inform clients what
key is to be used. However, this handshake can be made less frequent by
including all paths underneath the `%coop` in the response, such that if
the user is requesting sibling paths under the same `%coop`, only one
handshake is required.

 ### Naming
I am utterly detached to all new names introduced, just trying to get
something down

 ### API Design
The most contentious part of this proposal will likely be the split
between `%grow` and `%tend`. I assert (rather weakly mind you) that this
is more ergonomic for the end user, although there's a strong argument
to be made that `%grow` should just take a `(unit coop)`. If this were
the case, however, it would muddy the semantics. If the value is
encrypted, then the ship,desk,case will be in the coop, else it will be
specified in the path.  Worth noting that specifying the
`%coop` and the rest of the path seperately seems like it could be
unintuitive because the path that it will be bound to is actually
`(welp coop path)`

The lifecycles for coops seem straightforward, although worth revisiting
the invariants it maintains, and how it handles those invariants. A list of such:
- No nesting (obviously good)
- Crashing on binding publically into a private coop (crashing is bad,
do we want to deliver a notification? (See footnote 1))
- Crashing on binding into a coop that doesn't exist (same notes as above)

 ### Key generation
Current implementation is obviously stupid, how should i do it?

 ### Footnotes
 1. Why are the remote scry datastructures notes and not gifts? Forgive
 me being out of the loop, but we don't actually use the wire for
 anything anywhere, and remote scry is giving gift anyway.
 2. It's so good to be back

---
## [cuberound/cmss13](https://github.com/cuberound/cmss13)@[e7816d96c5...](https://github.com/cuberound/cmss13/commit/e7816d96c5d1523337dec081bea0056fbc9189fc)
#### Tuesday 2023-12-19 12:24:24 by forest2001

Almayer AntiTheft measures. (#5100)

STOP STEALING SHIT
# About the pull request
Adds a subtype of reinforced hull for the Almayer that changes between
indestructible hull and normal reinforced wall after hijack.
Uses this wall type around uniform vendors, the separation wall in the
firing range and around engineering storage.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
Having the engineering storage looted at round start is just silly
avoidance of the "don't deconstruct the whole ship without a reason"
rule.

# Testing Photographs and Procedure

I have verified that all works as intended, the walls cannot be harmed
prior to hijack, and shutters function as advertised.

# Changelog
:cl:
add: Added a new almayer hull type (heavy reinforced) which is
indestructible by normal means until after hijack collision.
add: Added a new subtype of shutter that automatically opens or closes
depending on security level.
maptweak: Maps both of the above around the engineering storeroom. Also
adds the walls between the firing ranges and around uniform vendors.
maptweak: Manual control button for shutters over engineering storage in
the CEs office.
code: Changes hijack structural changes (walls/windows/windoors/ladders)
to use signals.
/:cl:

---------

Co-authored-by: fira <loyauflorian@gmail.com>

---
## [discourse/discourse](https://github.com/discourse/discourse)@[8def5c4286...](https://github.com/discourse/discourse/commit/8def5c428666f84e5642eee17182b5b8fe37821e)
#### Tuesday 2023-12-19 12:30:39 by David Taylor

Enable Embroider/Webpack code spliting for Wizard

* Move Wizard back into main app, remove Wizard addon
* Remove Wizard-related resolver or build hacks
* Install and enable `@embroider/router`
* Add "wizard" to `splitAtRoutes`

In a fully optimized Embroider app, route-based code splitting more
or less Just Work™ – install `@embroider/router`, subclass from it,
configure which routes you want to split and that's about it.

However, our app is not "fully optimized", by which I mean we are
not able to turn on all the `static*` flags.

In Embroider, "static" means "statically analyzable". Specifically
it means that all inter-dependencies between modules (files) are
explicitly expressed as `import`s, as opposed to `{{i18n ...}}`
magically means "look for the default export in app/helpers/i18n.js"
or something even more dynamic with the resolver.

Without turning on those flags, Embroider behaves conservatively,
slurps up all `app` files eagerly into the primary bundle/chunks.
So, while you _could_ turn on route-based code splitting, there
won't be much to split.

The commits leading up to this involves a bunch of refactors and
cleanups that 1) works perfectly fine in the classic build, 2) are
good and useful in their own right, but also 3) re-arranged things
such that most dependencies are now explicit.

With those in place, I was able to move all the wizard code into
the "app/static" folder. Embroider does not eagerly pull things from
this folder into any bundle, unless something explicitly "asks" for
them via `imports`. Conversely, things from this folder are not
registered with the resolver and are not added to the `loader.js`
registry.

In conjunction with route-based code splitting, we now have the
ability to split out islands of on-demand functionalities from the
main app bundle.

When you split a route in Embroider, it automatically creates a
bundle/entrypoint with the relevant routes/templates/controllers
matching that route prefix. Anything they import will be added to
the bundle as well, assuming they are not already in the main app
bundle, which is where the "app/static" folder comes into play.

The "app/static" folder name is not special. It is configured in
ember-cli-build.js. Alternatively, we could have left everything
in their normal locations, and add more fine-grained paths to the
`staticAppPaths` array. I just thought it would be easy to manage
and scale, and less error-prone to do it this way.

Note that putting things in `app/static` does not guarantee that
it would not be part of the main app bundle. For example, if we
were to add an `import ... from "app/static/wizard/...";` in a
main bundle file (say, `app.js`), then that chunk of the module
graph would be pulled in. (Consider using `await import(...)`?)

Overtime, we can build better tooling (e.g. lint rules and babel
macros to make things less repetitive) as we expand the use of
this pattern, but this is a start.

Co-authored-by: Godfrey Chan <godfreykfc@gmail.com>

---
## [reynaldiarya/FOSSBilling](https://github.com/reynaldiarya/FOSSBilling)@[b3321a8dd3...](https://github.com/reynaldiarya/FOSSBilling/commit/b3321a8dd33dfbd084899709a37b7e3a5c626300)
#### Tuesday 2023-12-19 12:36:20 by Adam Daley

Update to Sentry v4 (#1780)

* Bump minimum PHP version to 8.1

* Missed these too

* Shit's broke and stupid as fuck

* Update SentryHelper.php

* Update package-lock.json

* I did the fixing

---------

Co-authored-by: Belle Aerni <belleaerni@gmail.com>

---
## [fira/cmss13](https://github.com/fira/cmss13)@[dc234c9939...](https://github.com/fira/cmss13/commit/dc234c9939efeb43170a934437f50148323407f7)
#### Tuesday 2023-12-19 13:03:45 by InsaneRed

Oppressor cooldown changes (#5154)

# About the pull request

Lowers the oppressor tail_abudct (the hook) to 15 seconds of cooldown
and makes the windup faster.

Makes punch shave off cooldown from the abduct for 5 seconds 

All have been tested but i would like this to get testmerged first so i
can actually see the results in game, nothing is set in stone and i want
to edit this further so the cd / cd reduction isnt too powerful, they're
just numbers ive decided were good enough to atleast make the caste
decent for the time being.


# Explain why it's good for the game

Oppressor has been a snoozer strain for a while now where you cast an
ability, and IF it hits you get to play the game otherwise you wait 20
seconds and thats just not fun. Especially for what the ability is, a 20
second cooldown is not worth it.

I've talked with a few people that all agree that the downtime for what
you "could" do with oppressor is not worth it. And i have to agree with
them, the caste feels boring to play and its basically half dead due to
the amnout of downtime you have between abilities compared to how
everything else works. The idea of this is to make it so its not busted
out of its brain but atleast not an observer++ strain so you can feel
more involved in the gameplay.




# Testing Photographs and Procedure
</details>


# Changelog



:cl:
balance: Oppressor tail abduct changed to 15 seconds and lowers the
windup to 7 deciseconds
balance: Changes around the punch effect so that instead of having to
meet demonic standards, you only need to punch to lower your tail/hook
on oppressor.
fix: You will now automatically punch chest if the target you are aiming
at is delimbed instead of doing nothing
/:cl:

---------

Co-authored-by: InsaneRed <prodexter31@outlook.comm>
Co-authored-by: Birdtalon <birdtalon@gmail.com>

---
## [sahilmasand/best-digital-marketing-trainer-in-india](https://github.com/sahilmasand/best-digital-marketing-trainer-in-india)@[ec2ccaa87f...](https://github.com/sahilmasand/best-digital-marketing-trainer-in-india/commit/ec2ccaa87f071529a136ddbda7dadec6b79fb8a0)
#### Tuesday 2023-12-19 13:25:52 by sahilmasand

"Mastering the Digital Frontier: A Journey of Learning Digital Marketing from the Best Digital Marketing Trainer in India - Chetan Chauhan"


My Journey with Maayodiya Academy, Home to the Best Digital Marketing Trainer in
India, Chetan Chauhan, and Expert Guidance from Ratan Shrivastav"
In the ever-evolving landscape of digital marketing, the right mentorship can make all
the difference. My venture into the world of digital marketing took an exciting turn
when I enrolled in Maayodiya Academy, recognized as the best digital marketing
institute in India, under the guidance of the renowned Chetan Chauhan, also knows as
the best digital marketing trainer in india
From the very beginning, it was evident that Maayodiya Academy was not just a place
of learning; it was a hub of innovation and expertise. Chetan Chauhan, a seasoned
professional in the field, brought a wealth of knowledge and real-world experience
that transcended traditional classroom teachings. His dynamic approach to digital
marketing was not only insightful but also inspiring, creating an atmosphere that
fueled curiosity and creativity.
Chauhan's ability to break down complex concepts into digestible chunks made
learning an enjoyable experience. He effortlessly combined theory with practical
insights, ensuring that each lesson was not just theoretical but applicable to the
real-world scenarios we would encounter in our digital marketing careers. His passion
for the subject matter was contagious, motivating each student to delve deeper into
the intricacies of the digital realm.
While Chetan Chauhan set the tone for excellence, Ratan Shrivastav, his able
subordinate, added another layer of expertise to the learning experience. Shrivastav's
hands-on approach and personalised attention to each student were instrumental in
bridging the gap between theory and practice. His interactive sessions and case
studies provided valuable insights into the nuances of digital marketing campaigns,
making the learning process more immersive and relevant.
One of the standout features of Maayodiya Academy was the practical projects that
Chetan Chauhan incorporated into the curriculum. These projects mirrored real-world
scenarios, allowing us to apply our newfound knowledge in a simulated professional
environment. The constructive feedback provided by him played a pivotal role in
refining our skills and instilling a sense of confidence in tackling actual digital
marketing challenges.
The collaborative nature of the learning environment fostered by Chetan Chauhan,
recognized as the best digital marketing trainer in India, and Ratan Shrivastav made
Maayodiya Academy stand out as the best digital marketing institute in the country.
At Maayodiya Academy, the commitment to nurturing digital marketing talent goes
beyond the classroom. One distinguishing aspect that sets this institution apart is its
dedication to practical skill development through free internships. Recognizing the
value of hands-on experience, Maayodiya Academy not only imparts theoretical
knowledge but also provides students with the opportunity to apply their learning in
real-world scenarios. The inclusion of free internships is a testament to the academy's
holistic approach to education. These internships serve as invaluable platforms for
students to further refine their skills, gain exposure to industry practices, and build a
robust portfolio. The academy's emphasis on practical training not only enhances the
students' understanding of digital marketing but also equips them with the confidence
and expertise needed to thrive in the dynamic landscape of the digital realm.
As I reflect on my time at Maayodiya Academy, I am not only equipped with a
comprehensive understanding of digital marketing but also a network of like-minded
professionals. Chetan Chauhan's mentorship, acknowledged as the best in the india,
and Ratan Shrivastav's guidance have not only shaped my skills but have also
instilled a passion for continuous learning in the ever-evolving field of digital
marketing. The experience at Maayodiya Academy has undoubtedly set the
foundation for a successful career in the digital realm, and I am grateful for the
invaluable lessons learned under the guidance of these exceptional mentors.
Sahil Masand

---
## [OGFlab/name-suggestion-index](https://github.com/OGFlab/name-suggestion-index)@[0bfae497e7...](https://github.com/OGFlab/name-suggestion-index/commit/0bfae497e7d38f2f62c6861f0ea15f0f4955cc71)
#### Tuesday 2023-12-19 13:25:58 by 快乐的老鼠宝宝

LATEST NSI STATE

As of https://github.com/osmlab/name-suggestion-index/commit/0922fd0c7ed88a2cc025cf94c589b62bed84ee62

---
Here are all contributior in upstream repo and count of commits:

(log generated by `git log --pretty="%an <%ae>" | sort | uniq -c | sort -nr`

---
   1861 kjonosm <51236777+kjonosm@users.noreply.github.com>
   1768 Bryan Housel <bryan@mapbox.com>
   1253 UKChris-osm <59393694+UKChris-osm@users.noreply.github.com>
   1147 Bryan Housel <bhousel@gmail.com>
    927 Bryan Housel <bryan@7thposition.com>
    765 快乐的老鼠宝宝 <keaitianxinmail@qq.com>
    719 Serhii Muchychka <Serhii.Muchychka@gmail.com>
    687 arch0345 <archpdx@pm.me>
    683 Tim Smith <tsmith84@gmail.com>
    527 archpdx <archpdx@pm.me>
    458 Minh Nguyễn <mxn@1ec5.org>
    432 LaoshuBaby <keaitianxinmail@qq.com>
    427 ENT8R <info.ent8r@gmail.com>
    424 Tim Smith <tsmith@chef.io>
    419 Mateusz Konieczny <matkoniecz@gmail.com>
    339 快乐的老鼠宝宝 <42690037+LaoshuBaby@users.noreply.github.com>
    338 arch0345 <85302075+arch0345@users.noreply.github.com>
    299 Cj Malone <Cj-Malone@users.noreply.github.com>
    271 Chris <59393694+UKChris-osm@users.noreply.github.com>
    262 Mathew Attlee <hello@codeinabox.com>
    246 arrival-spring <77166354+arrival-spring@users.noreply.github.com>
    238 m-hue <m-hue@users.noreply.github.com>
    235 Cj Malone <CjMalone@mail.com>
    223 Tommylung <tommylung@users.noreply.github.com>
    220 Adamant36 <amendenhall@live.com>
    216 Contrib1043 <mueller@turboprinzessin.de>
    205 Diego <diego.sanguinetti@hotmail.com>
    203 RickeyRichards <51227778+RickeyRichards@users.noreply.github.com>
    173 Ferdi <58372210+Identitaet@users.noreply.github.com>
    156 Héctor Ochoa Ortiz <cie.hochoa@gmail.com>
    153 Kiel Hurley <kielhurley@gmail.com>
    133 doublah <doublah@airmail.cc>
    130 hanchao <hanchao0123@hotmail.com>
    125 Wille Marcel <wille.yyz@gmail.com>
    121 David Hicks <david@hicks.id.au>
    118 Baptiste Mille-Mathias <baptiste.millemathias@gmail.com>
    113 afanasovich <75438207+afanasovich@users.noreply.github.com>
    109 Chak Lung Ngan <tommylung@users.noreply.github.com>
    108 serhii-muchychka <Serhii.Muchychka@gmail.com>
    107 Tim Smith <tim@mondoo.com>
    105 Peter Newman <peternewman@users.noreply.github.com>
    103 Chak Lung Ngan <tommylung27@hotmail.com>
    102 diego <diego.sanguinetti@hotmail.com>
    101 Max Erickson <maxerickson@gmail.com>
     99 SilentSpike <SilentSpike100+Github@gmail.com>
     93 nuxper <po.gregoire@wanadoo.fr>
     93 AntiCompositeNumber <anticompositenumber@gmail.com>
     88 Sky <dimiturtasev@abv.bg>
     88 Praxis | Darian <hello@vulpinecat.com>
     87 Diego Sangunietti <5572928+sguinetti@users.noreply.github.com>
     76 TagaSanPedroAko <jheromemiguel@gmail.com>
     74 Robot8A <cie.hochoa@gmail.com>
     72 arnowrld <93239523+arnowrld@users.noreply.github.com>
     72 Sky <19364673+Dimitar5555@users.noreply.github.com>
     72 Dimitar <19364673+Dimitar5555@users.noreply.github.com>
     71 u-spec-png <54671367+u-spec-png@users.noreply.github.com>
     70 Colton Piper <pipercolton@gmail.com>
     69 cmap99 <101516688+cmap99@users.noreply.github.com>
     67 Yağızhan <yagizhan49@protonmail.com>
     64 wish7 <wish7code@gmail.com>
     63 Aaron Lidman <aaronlidman@gmail.com>
     61 bkissin <53274972+bkissin@users.noreply.github.com>
     61 ArenaL5 <arenal5@gmx.com>
     58 jhutton1 <144355969+jhutton1@users.noreply.github.com>
     57 Malcolm Smith <malcolmsmith18@gmail.com>
     53 sb12 <sb12@users.noreply.github.com>
     51 Robin van der Linde <robin.vanderlinde@gmail.com>
     50 tohaklim <tohaklim@gmail.com>
     50 Revtro <111625617+Revtro@users.noreply.github.com>
     49 MASangys <37516216+MASangys@users.noreply.github.com>
     49 Adam <amendenhall@live.com>
     48 mds08011 <malcolmsmith18@gmail.com>
     47 ffff-23 <open_ffff23@protonmail.ch>
     45 AntiCompositeNumber <AntiCompositeNumber@gmail.com>
     44 dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>
     43 divya-bandapalle <79717676+DivyaB1@users.noreply.github.com>
     43 Sascha Brawer <sascha@brawer.ch>
     41 Arthur Eigenbrot <aeigenbrot@nso.edu>
     39 Leon Kernan <lkernan@users.noreply.github.com>
     37 Josh Carlson <jdcarls2@gmail.com>
     36 Supaplextw <bejokeup@gmail.com>
     35 Sukkoria <sukkoria@gmx.fr>
     34 Win Olario <govvin@users.noreply.github.com>
     34 Manuel Tassi <mannivuwiki@gmail.com>
     34 Andrew Harvey <andrew@alantgeo.com.au>
     32 ShinyDog2636 <113802015+ShinyDog2636@users.noreply.github.com>
     32 Filip Czaplicki <github@starsep.com>
     31 Arthur Galuza <arthur@galuza.io>
     30 mparrault <39238548+mparrault@users.noreply.github.com>
     30 Matthijs Melissen <github@matthijsmelissen.nl>
     29 Danny McDonald <mparrault@gmail.com>
     29 Daniel <96841083+dan13l9@users.noreply.github.com>
     29 ArenaL5 <37388405+ArenaL5@users.noreply.github.com>
     28 chuqtas <51102336+chuqtas@users.noreply.github.com>
     27 Mario Daniel Ruiz Saavedra <desiderantes93@gmail.com>
     27 Karthoo <leon.karcher@helmlingen.net>
     27 Guerme <52296173+Guerme@users.noreply.github.com>
     27 Alessandro <80714562+alessandrocarmeli@users.noreply.github.com>
     26 paunofu <paunofuentes@gmail.com>
     26 LeJun <lejun@gmx.fr>
     25 iigmir <roc120j@gmail.com>
     25 bgo-eiu <100172442+bgo-eiu@users.noreply.github.com>
     25 Tan Wei Lin <stravagation@gmail.com>
     25 Denis Verheyden <msts_2@hotmail.com>
     23 Vesihiisi <alicia@fagerving.se>
     23 Revtro <118647831+Lonerat@users.noreply.github.com>
     23 AnjaliGGeetha <anjali.g@icfoss.in>
     22 waso99 <43682410+waso99@users.noreply.github.com>
     22 rskedgell <58479391+rskedgell@users.noreply.github.com>
     22 Lakshyajeet Jalal <73988826+MG-LSJ@users.noreply.github.com>
     22 Identitaet <58372210+Identitaet@users.noreply.github.com>
     22 Eric Christensen <Eric-Sparks@users.noreply.github.com>
     22 Christine <48364789+coderbeetle@users.noreply.github.com>
     21 SafetyIng <77867539+SafetyIng@users.noreply.github.com>
     21 Herbert Persley <United600@users.noreply.github.com>
     21 Contrib1043 <59527956+Contrib1043@users.noreply.github.com>
     21 Christopher Eby <kreed@kreed.org>
     21 AlertSubject <mail@jannikkiel.com>
     20 Diego Sangunietti <diego.sanguinetti@hotmail.com>
     19 doktorpixel14 <leonkarcher.123@gmail.com>
     19 Josh Lee <jleedev@gmail.com>
     19 Daniele Napolitano <daniele.napolitano@nttdata.com>
     18 pyrog <pyrog@laposte.net>
     18 luisluigi639 <66276929+luisluigi639@users.noreply.github.com>
     18 ffff-23 <72978935+ffff-23@users.noreply.github.com>
     18 andrewpmk <andrewpmk@gmail.com>
     18 Simon Poole <simon@poole.ch>
     18 Sam <35312698+Samuel12321@users.noreply.github.com>
     18 Mathias Haugsbø <mathiash98@gmail.com>
     17 Michael Lyons <github@michael.lyo.nz>
     17 Identität <58372210+Identitaet@users.noreply.github.com>
     16 mneko <m.the.neko@gmail.com>
     16 hernandez87v <hernandez87v@hotmail.com>
     16 Tim Smith <tsmith@mondoo.com>
     16 Sean Young <assanges@icloud.com>
     16 Han Chao <hanchao0123@hotmail.com>
     16 Charlotte M <charlie@sinclarius.com>
     16 Asif Youssuff <yoasif@gmail.com>
     15 orangegrove_1955 <orangegrove_1955@hotmail.com>
     15 hdevine825 <hdevine825@gmail.com>
     15 Quincy Morgan <quincy.morgan@icloud.com>
     15 Olyon <jerome.amagat@gmail.com>
     15 Michaël Guay-Lambert <michaelguaylambert@me.com>
     15 Michael Lyons <michael@fireside21.com>
     15 Math1985 <github@matthijsmelissen.nl>
     15 Emmanuel Eboh <63825997+EOEboh@users.noreply.github.com>
     15 Emil <77762440+coolultra1@users.noreply.github.com>
     15 David Morais Ferreira <david.moraisferreira@gmail.com>
     14 wolfy1339 <webmaster@wolfy1339.com>
     14 maxerickson <maxerickson@gmail.com>
     14 hikemaniac <31667811+hikemaniac@users.noreply.github.com>
     14 Xhika <laureta.dzika@gmail.com>
     14 Manuel Tassi <42747216+Mannivu@users.noreply.github.com>
     14 Ferdinand S <ferdi98701@gmail.com>
     14 David Haberthür <email@davidhaberthuer.ch>
     14 Christopher Lorenz <britiger@gmx.net>
     13 mollimch <149695583+mollimch@users.noreply.github.com>
     13 blendy-map <99269223+blendy-map@users.noreply.github.com>
     13 Scottie0001 <105581438+Scottie0001@users.noreply.github.com>
     13 Guerme <winn.ketchum@gmail.com>
     13 DivyaB1 <79717676+DivyaB1@users.noreply.github.com>
     12 venue-map <77090087+venue-map@users.noreply.github.com>
     12 mstsbe <113928350+mstsbe@users.noreply.github.com>
     12 SierraIm <48466185+SierraIm@users.noreply.github.com>
     12 Nevidomskyi Oleksandr <neviksasha@gmail.com>
     12 Michael Raguso <michael.raguso@gmail.com>
     12 Markus Göllnitz <camelcasenick@bewares.it>
     12 Lukas <35879422+Lukas458@users.noreply.github.com>
     12 Josh Carlson <39384515+jdcarls2@users.noreply.github.com>
     12 Hugoren Martinako <aumpfbahn@gmail.com>
     12 Dean Scott <105581438+Scottie0001@users.noreply.github.com>
     12 Christoph <topfolas@t-online.de>
     12 Caro Aguilar <48287964+caguilara@users.noreply.github.com>
     12 Binnette <binnette@gmail.com>
     11 ᴄʜʀɪsᴛᴏᴘʜᴇʀ ᴍᴇɴɢ <im@dyi.ng>
     11 mutipg <mutancik@gmail.com>
     11 jarek <jarek@piorkowski.ca>
     11 Tubalevião <alvaro.prata.filho@gmail.com>
     11 Russ Garrett <russ@garrett.co.uk>
     11 Matthew Wootten <mmwootten@outlook.com>
     11 Kyle Hensel <k.y.l.e@outlook.co.nz>
     11 Jyunhou <vayyenhow@outlook.com>
     11 DBrgr <121040973+DBrgr@users.noreply.github.com>
     11 Abdelkrim2003 <115945559+Abdelkrim2003@users.noreply.github.com>
     10 thilinatnt <36640320+thilinatnt@users.noreply.github.com>
     10 pkoby <peterjkoby@gmail.com>
     10 kirandash <thekirankumardash@gmail.com>
     10 ferdinand0101 <ferdi98701@gmail.com>
     10 SALLES Quentin <quentin.salles@akka.eu>
     10 Praxis | Darian <hello@vulpinecat.com>
     10 Jef D <danielsjf@users.noreply.github.com>
     10 HandyHat <58530748+HandyHat@users.noreply.github.com>
     10 Giovanni Alfredo Garciliano Díaz <giobeatle10@gmail.com>
     10 Flo Edelmann <florian-edelmann@online.de>
     10 Alessandro <80714562+carmeliale@users.noreply.github.com>
      9 wmisener <58491489+wmisener@users.noreply.github.com>
      9 paunofu <94412187+paunofu@users.noreply.github.com>
      9 noenandre <5470915+noenandre@users.noreply.github.com>
      9 dieter <dieter09@live.be>
      9 andrepoiy <47615278+andrepoiy@users.noreply.github.com>
      9 Yotam Nachum <me@yotam.net>
      9 Thibault Molleman <thibaultmol@users.noreply.github.com>
      9 Pushkar Khedekar <pushkarkhedekar@gmail.com>
      9 Marcelo Cristiano <marceloabk@hotmail.com>
      9 Lung <tommylung@users.noreply.github.com>
      9 Kuba Mędrek <kubix.medrek@gmail.com>
      9 ImreSamu <ImreSamu@users.noreply.github.com>
      9 Hugo <hugo.lucas@targomo.com>
      9 Dmitrii Romanov <dmromanov@users.noreply.github.com>
      9 DULAC Philippe <phd0@hotmail.com>
      9 Alberto Iannaccone <a.iannaccone@arduino.cc>
      8 yelaD <dale@interold.com>
      8 vrun1208 <vrun4750@gmail.com>
      8 username <youremail@domain>
      8 monk198230 <67480594+monk198230@users.noreply.github.com>
      8 mcliquid <info@mcliquid.de>
      8 danieldegroot2 <67521919+danieldegroot2@users.noreply.github.com>
      8 azheng4119 <azheng4119@bths.edu>
      8 amous4822 <amous4822@gmail.com>
      8 Syarol <1oleq25@gmail.com>
      8 Steven Michaels <steven.michaels@gmail.com>
      8 Stefan Haan <stefan@kikeriki.at>
      8 Shu Higashi <higa432@gmail.com>
      8 Scarlett <me@kyy0602.com>
      8 NMVikings <no.more.vikings@gmail.com>
      8 Mykhaylo Samonov <y0nd3rb0y@gmail.com>
      8 Lukas Kronberger <j13m126@posteo.de>
      8 Eric Czajkowski <eczajkowski@centuryeng.com>
      8 Daniele Napolitano <dnax88@gmail.com>
      8 Ashutosh <33365865+TheDynamicPunk@users.noreply.github.com>
      8 Ashu <ashutoshgu18@gmail.com>
      7 wolfy1339 <4595477+wolfy1339@users.noreply.github.com>
      7 Ryan <ry4n86@gmail.com>
      7 Rishabh <rishabh.bajaj66@gmail.com>
      7 Peter Newman <peterjnewman@gmail.com>
      7 Mkrtich <soghomonyanmkrtich@gmail.com>
      7 Matheus Gomes <86851490+matheusgomesms@users.noreply.github.com>
      7 Kovoschiz <11350903+Kovoschiz@users.noreply.github.com>
      7 Jérôme Amagat <jerome.amagat@gmail.com>
      7 Hiausirg <102484092+Hiausirg@users.noreply.github.com>
      7 Evan Siroky <evan.siroky@yahoo.com>
      7 Bitha007 <bibekthapa922@gmail.com>
      7 Ben L <prizefighter@gmail.com>
      7 Andrew MacKinnon <andrewpmk@gmail.com>
      6 wouter van der plas <2423856+wvanderp@users.noreply.github.com>
      6 rkdclgh <78959698+rkdclgh@users.noreply.github.com>
      6 modaserMoj <modaser.farooqi@gmail.com>
      6 kyy0602 <me@kyy0602.com>
      6 johnnybar <johnnybareket@gmail.com>
      6 hfs <github@knackich.de>
      6 haansn08 <stefan@kikeriki.at>
      6 evansiroky <evan.siroky@yahoo.com>
      6 b4hub4l1 <57061194+b4hub4l1@users.noreply.github.com>
      6 ale <alefuedev@gmail.com>
      6 Wouter van der Plas <2423856+wvanderp@users.noreply.github.com>
      6 Varun Patodia <58364635+vrun1208@users.noreply.github.com>
      6 Tom Stewart <tjstewar@us.ibm.com>
      6 Tck13 <tycho.tck13@gmail.com>
      6 TCK13 <tycho.tck13@gmail.com>
      6 SilentSpike <silentspike100+Github@gmail.com>
      6 Sean Sutherland <sssuthe@gmail.com>
      6 Richlv <richlv@nakts.net>
      6 Noémie <noemie.lehuby@zaclys.net>
      6 Mikkel Kirkgaard Nielsen <miki+git@mikini.dk>
      6 Lyndi Castrejon <lyndic@protonmail.com>
      6 Kyℓe Hensel <k-yle@users.noreply.github.com>
      6 Khadijah Parks <khadijah.parks@mailchimp.com>
      6 Justin Bento <bento.a.justin@gmail.com>
      6 Jez Nicholson <jez.nicholson@gmail.com>
      6 Jakub Duchateau <duchateaujakub@gmail.com>
      6 Irham Dzuhri <irhamdz@gmail.com>
      6 Heikrana <vs201100@gmail.com>
      6 George Daneke <flatroy@gmail.com>
      6 DianAgesson <99240595+DianAgesson@users.noreply.github.com>
      6 Daniel Yee <danjamesyee@gmail.com>
      6 AlertSubject <72819077+AlertSubject@users.noreply.github.com>
      5 zyphlar <zyphlar@users.noreply.github.com>
      5 viveknshah <vivek_n_shah@yahoo.com>
      5 shawn12 <1572964+shawn12@users.noreply.github.com>
      5 phcarval <philippe.carvalho@posteo.net>
      5 kyy0602 <16321802+kyy0602@users.noreply.github.com>
      5 itsmeAnubhab <91974827+itsmeAnubhab@users.noreply.github.com>
      5 archpdx <85302075+arch0345@users.noreply.github.com>
      5 ankita2210 <ankita.nasipuri@gmail.com>
      5 Wouter van der Plas <wouterv.dplas@gmail.com>
      5 Wojciech Malinowski <wojciech.malinowski@gmail.com>
      5 Waldir Pimenta <waldyrious@gmail.com>
      5 Shashwat <shashwatmahar12@gmail.com>
      5 Sam M <s.mansch@gmail.com>
      5 Robert Finkley <rfinkley@gmail.com>
      5 Quentin Salles <53410161+QuentinS33@users.noreply.github.com>
      5 Mitsjol <mitchelvanduuren@hotmail.com>
      5 Lonerat <118647831+Lonerat@users.noreply.github.com>
      5 Lele Lew <lele@lelelew.com>
      5 John Firebaugh <john.firebaugh@gmail.com>
      5 J. Tran <jyntran@gmail.com>
      5 Iván <13920663+ivanrome@users.noreply.github.com>
      5 Ian Dees <ian.dees@gmail.com>
      5 Frank Iriarte <jurrish@For-the-screen-is-dark-and-full-of-errors.local>
      5 Ferveloper <fermervil@gmail.com>
      5 Ferdi Laptop <58372210+Identitaet@users.noreply.github.com>
      5 Eugene Alvin Villar <seav80@gmail.com>
      5 Daniel Callejas Sevilla <daniel.callejas.sevilla@gmail.com>
      5 Cyril Cincet <64784806+Djiril@users.noreply.github.com>
      5 Austin Stevens <austinestevens@outlook.com>
      5 Arash N <arash_negari@yahoo.ca>
      5 Andrey Golovin <Andygol@users.noreply.github.com>
      5 28688 <95373042+28688@users.noreply.github.com>
      4 zymurgic <simon.hewison@zymurgy.org>
      4 skfd <kk@comentality.com>
      4 sandy8169 <goodnewssandy@gmail.com>
      4 paradice <paradice@MacBook-Air-paradice.local>
      4 modaserMoj <54120999+modaserMoj@users.noreply.github.com>
      4 michael-reuter <17342888+michael-reuter@users.noreply.github.com>
      4 ldw606 <lewis.wakeland+GitHubPersonal@hotmail.co.uk>
      4 ldw606 <34221259+ldw606@users.noreply.github.com>
      4 jgon6 <1424393+jgon6@users.noreply.github.com>
      4 hplewis <holden@holdenlewis.xyz>
      4 greenkeeper[bot] <23040076+greenkeeper[bot]@users.noreply.github.com>
      4 charlie ✨ <sinclarius@users.noreply.github.com>
      4 bonbon12 <bonwork280@gmail.com>
      4 arszh <arsenzhitnikov@gmail.com>
      4 alechan <alechan@tencent.com>
      4 aayush920 <76609501+aayush920@users.noreply.github.com>
      4 Wolfgang Schildbach <wschildbach@fermi.franken.de>
      4 Whitemalt <noppadet-ice@hotmail.com>
      4 Vinicius Philot <vphilot@p1a-v17613.alpha.cglp.ca>
      4 VJ1224 <vanshjain1224@gmail.com>
      4 Tobias Zwick <newton@westnordost.de>
      4 Tck13 <Tck13@users.noreply.github.com>
      4 Silvanus Bordignon <silvanusbordignon@gmail.com>
      4 Shiraaz Ahammed <shiraaz.ahammed@gmail.com>
      4 SK53 <SK53.osm@gmail.com>
      4 Romil <romilj012@gmail.com>
      4 Reuter, Michael <Michael.Reuter@cerner.com>
      4 Patchi-Osm <76591095+Patchi-Osm@users.noreply.github.com>
      4 OmnificOne <sam.wallingford@gmail.com>
      4 Nicolas Le Roux <mr.leroux.nicolas@gmail.com>
      4 Michael Bråten <braaten.michael@outlook.com>
      4 Madeleine Schönemann <madeleine.schonemann@gmail.com>
      4 Kevin Kandlbinder <kevin@kevink.dev>
      4 Karol Dawidziak <karol@dawidziak.eu>
      4 Janjko <janjko@gmail.com>
      4 Italo Sousa <italusousa@gmail.com>
      4 Hermann Schwarting <hfs@gmx.de>
      4 Eric_C <a762466074@gmail.com>
      4 Edward Betts <edward@4angle.com>
      4 Edoardo Tenani <edoardo.tenani@protonmail.com>
      4 Dejan <dejan@hey.com>
      4 David Hunter <david@davidhunter.io>
      4 Damian Klisiewicz <damianklisiewicz@gmail.com>
      4 Christopher <christopher.blue@gmail.com>
      4 Bocong Zhao <zhaobocong@hotmail.com>
      4 Bibek Thapa <bibekthapa922@gmail.com>
      4 Ben Lee <prizefighter@gmail.com>
      4 BARBIER, Alexandre (ATY) <alexandre.barbier@infopro-digital.com>
      4 AyushiN <36621150+ANaphade@users.noreply.github.com>
      4 AnonymousAlligator <anonymousalligatorosm@gmail.com>
      4 Andrew Harvey <andrew.harvey4@gmail.com>
      4 Alex Weech <abw@alexweech.com>
      4 Adzkar Fauzie <adzkarfauzie02@gmail.com>
      3 yukijina <yukijina@gmail.com>
      3 waso99 <waso99@yahoo.com>
      3 unknown <joey.assal@gmail.com>
      3 ttomasz <31594210+ttomasz@users.noreply.github.com>
      3 trigpoint <trigpoint@users.noreply.github.com>
      3 sophiabonsu <sophiabonsu@gmail.com>
      3 sommerluk <sommerluk@gmail.com>
      3 sinclarius <sinclarius@users.noreply.github.com>
      3 sinclarius <paperpirates@gmail.com>
      3 silvanusbordignon <63549543+silvanusbordignon@users.noreply.github.com>
      3 robinroscher <rroscher92@mgail.com>
      3 naposm <63296731+naposm@users.noreply.github.com>
      3 mlmesa2 <60515370+mlmesa2@users.noreply.github.com>
      3 math1985 <info@matthijsmelissen.nl>
      3 linux2good <110234273+linux2good@users.noreply.github.com>
      3 klswcz <damianklisiewicz@gmail.com>
      3 johanricher <johan.richer@jailbreak.paris>
      3 gabrielhicks <gabrielhicks@mail.com>
      3 g4rry420 <61521805+g4rry420@users.noreply.github.com>
      3 danih0311 <65899160+danih0311@users.noreply.github.com>
      3 camilorecce <camilorecce@gmail.com>
      3 Will Skora <skorasaurus@gmail.com>
      3 Vitor George <vitor.george@gmail.com>
      3 Vedant Singhania <vedant.singhania@gmail.com>
      3 Toma Nistor <toma.nistor@fishawack.com>
      3 Tom Hukins <tom@eborcom.com>
      3 Tobias Jordans <t@tobiasjordans.de>
      3 Tobias <t@tobiasjordans.de>
      3 Strongwillow <clear.tsai@gmail.com>
      3 Sergei Eremenko <finalitik@gmail.com>
      3 SelfishSeahorse <SelfishSeahorse@users.noreply.github.com>
      3 Scott <Scotthall1983@hotmail.com>
      3 Samantha Arias <skao93@hotmail.com>
      3 Robert Whittaker <rjw62@cantab.net>
      3 Revtro <mailto:111625617+Revtro@users.noreply.github.com>
      3 Raman077 <ramanprabhakar007@gmail.com>
      3 RCRalph <rcralph@rcralph.me>
      3 PierceWHoward <pierce.w.howard@gmail.com>
      3 Parthiban Sundaramurthy <29parthiban@gmail.com>
      3 Outlet2048 <72819077+Outlet2048@users.noreply.github.com>
      3 Olga Boiaryntseva <olgaboiar@gmail.com>
      3 Mike Kerslake <theonlymikeever@gmail.com>
      3 Michael Moroni <michaelmoroni@disroot.org>
      3 Michael <2701605+michaelblyons@users.noreply.github.com>
      3 Lukas Sommer <sommerluk@gmail.com>
      3 Kyle Mckay <5459452+kymckay@users.noreply.github.com>
      3 KungFuryKeyboard <ry4ndevwork@gmail.com>
      3 Koverpih <koverpp@gmail.com>
      3 Ken <hello@kennethgutierrez.com>
      3 KarenDouglas <79128405+KarenDouglas@users.noreply.github.com>
      3 Karen Kerr <karenkerrgithub@gmail.com>
      3 Juanro49 <juanrobertogarciasanchez@gmail.com>
      3 Johannes Jarbratt <johannes.jarbratt+github@gmail.com>
      3 Joan <joan.gawelda@gmail.com>
      3 Javi RG <javirg@users.noreply.github.com>
      3 Javi RG <javirg@protonmail.com>
      3 JCGF-OSM <63681208+JCGF-OSM@users.noreply.github.com>
      3 Holden Lewis <holden@holdenlewis.xyz>
      3 Hinacio Sant <38104629+NeroSals@users.noreply.github.com>
      3 Hervé Saint-Amand <git@saintamh.org>
      3 HLucasTargomo <54280830+HLucasTargomo@users.noreply.github.com>
      3 Francesco Ansanelli <francians@gmail.com>
      3 Felix Edelmann <fxedel@gmail.com>
      3 Elizabeth Wait <Elizabeth.Wait@vmlyr.com>
      3 Dương Thành Vũ <vudt.93@gmail.com>
      3 Ben Lee <36443100+prizef@users.noreply.github.com>
      3 Ben Dyer <dyer.ben@protonmail.com>
      3 Austin Stevens <austin@penguin.tech>
      3 Ashutosh Shisodia <48064027+ashutoshshisodia@users.noreply.github.com>
      3 Anton Khorev <tony29@yandex.ru>
      3 Ansel Bridgewater <iamansel@gmail.com>
      3 Adriel Cavalcanti <cavalcantiadriel@gmail.com>
      3 Abdirahman Guled <aguled2@myseneca.ca>
      3 3Hearts <48471582+3Hearts@users.noreply.github.com>
      3 1-Byte <1-byte@gmx.net>
      2 ᴄʜʀɪsᴛᴏᴘʜᴇʀ ᴍ <im@dyi.ng>
      2 Štefan Baebler <stefan.baebler@gmail.com>
      2 xmready <77082140+xmready@users.noreply.github.com>
      2 wessport <wesporter92@gmail.com>
      2 tyr <tyr.asd@gmail.com>
      2 tntchn <tran0408tran0408t@yahoo.com.tw>
      2 simonpoole <simonpoole@users.noreply.github.com>
      2 siiky <github-siiky@net-c.cat>
      2 rye761 <ryebread761@gmail.com>
      2 rog-wilco <84986548+rog-wilco@users.noreply.github.com>
      2 pjr10th <65917229+pjr10th@users.noreply.github.com>
      2 parmeet9891 <parmeet_coder@yahoo.com>
      2 orangegrove1955 <38221472+orangegrove1955@users.noreply.github.com>
      2 nrg100 <nrg100@users.noreply.github.com>
      2 mxxcon <847140+mxxcon@users.noreply.github.com>
      2 micschwarz <contact@micschwarz.dev>
      2 luky89 <holubec.lukas@gmail.com>
      2 lucumon <vacamaribu@hotmail.es>
      2 kudlav <vladankudlac@gmail.com>
      2 jqngarcia <35226532+jqngarcia@users.noreply.github.com>
      2 javbw <johnw@mac.com>
      2 ilyakuchin <19621723+ilyakuchin@users.noreply.github.com>
      2 hwb15 <47414652+hwb15@users.noreply.github.com>
      2 giorgiomec <94143306+giorgiomec@users.noreply.github.com>
      2 gileri <e+pgp9225@linuxw.info>
      2 femtioelva <naivigera@gmail.com>
      2 fansanelli <francians@gmail.com>
      2 evgeniy.islamov <darkkrol16@yandex.ru>
      2 dharmadev108 <42813982+dharmadev108@users.noreply.github.com>
      2 debyos <gabor.babos@gmail.com>
      2 dafadllyn <79018751+dafadllyn@users.noreply.github.com>
      2 cmppoon <cmp.poon@gmail.com>
      2 bripmccann <bripmccann@gmail.com>
      2 brainshaker <parupp@gmx.de>
      2 bhavesh0206s <bhaveshsuthar0299@gmail.com>
      2 axserg <axel.alatorre.ferreiro@gmail.com>
      2 alefuedev <42624248+alefuedev@users.noreply.github.com>
      2 Vansh Jain <vanshjain1224@gmail.com>
      2 Tuan Pham <zeotuan@gmail.com>
      2 TomEWilkinson <tom-wil-ko@hotmail.co.uk>
      2 Thomas Ruffino <thomasruffino1@gmail.com>
      2 TheSnoozer <s.lange@alumni.tu-berlin.de>
      2 TheAdventurer64 <50059322+TheAdventurer64@users.noreply.github.com>
      2 Sāfto Rangen <2233810+kriswema@users.noreply.github.com>
      2 Sãfto Rangen <orangensaft@kriswema.de>
      2 Syfur Rahman <syfur.cse8.bu@gmail.com>
      2 Stheffany <stheffanyhadlich@gmail.com>
      2 Stacey <Stacey@MacBook-Pro-3.local>
      2 Spencer Alves <impiaaa@gmail.com>
      2 Soumyadeep Bhattacharya <43139047+SBhattacharya45@users.noreply.github.com>
      2 Shweta <72426535+Shweta200126@users.noreply.github.com>
      2 Shuvojit Saha <shuvojit.saha@kaz.com.bd>
      2 Sheikh Jamir Alam <48979376+Sheikh-JamirAlam@users.noreply.github.com>
      2 Seth Ryder <Seth.Ryder@harpercollins.com>
      2 Ricardo Christmann <80476005+ricci2511@users.noreply.github.com>
      2 Recoil016 <recoil@recoil.nrw>
      2 Raymond Berger <RayBB@users.noreply.github.com>
      2 Quincy Morgan <2046746+quincylvania@users.noreply.github.com>
      2 Prashant Kumar Mishra <33893505+ichbinprashant@users.noreply.github.com>
      2 Pavan Gudiwada <pavangudiwada@tutamail.com>
      2 OumKaZa <111268508+OumKaZa@users.noreply.github.com>
      2 Nuthi-Sriram <sriramnuthi@gmail.com>
      2 Nickolas Gupton <CorruptComputer@protonmail.com>
      2 Nick Landreville <45861790+nel417@users.noreply.github.com>
      2 Nicholas Mendez <mendez.nicholasr@gmail.com>
      2 Nicholas Mendez <95987301+nickmendezFlatiron@users.noreply.github.com>
      2 NeroSals <38104629+NeroSals@users.noreply.github.com>
      2 Nelson A. de Oliveira <naoliv@debian.org>
      2 Nathan Cruz <nathan_cruz77@hotmail.com>
      2 Nadyita <nadyita@hodorraid.org>
      2 Mxdanger <32040254+mxdanger@users.noreply.github.com>
      2 Mukul Khanna <mukul18khanna@gmail.com>
      2 Moritz Sternemann <moritz@strnmn.me>
      2 Mollie McHugh <88096377+molliemchugh-tomtom@users.noreply.github.com>
      2 Mohammadreza Abdoli <herbodabdoli@gmail.com>
      2 Miguel Carneiro <miguel.carneiro.morenas@everis.com>
      2 Michał Gwóźdź <114614618+michalgwo@users.noreply.github.com>
      2 Michaël Dierick <michael@dierick.io>
      2 Michael Reichert <nakaner@gmx.net>
      2 Matthew Henschke <matthewhenschke98@gmail.com>
      2 Mats Andreassen <matsand@live.no>
      2 Marquet Reid <contact@marquetreid.com>
      2 Markus <SelfishSeahorse@users.noreply.github.com>
      2 Mario Barrera <luismmario@gmail.com>
      2 Mariana <mariana.campos@tempest.com.br>
      2 Luke Stewart <stewartluke21@yahoo.com>
      2 Lexi Cummins <lcummins@burns-group.com>
      2 Laureta Dzika <laureta.dzika@gmail.com>
      2 KamajiiSC <brandonlschaen@gmail.com>
      2 Kai NeSmith <36375285+resistiv@users.noreply.github.com>
      2 Justin Doak <justinhdoak@gmail.com>
      2 Jonathan Brier <brierjon@users.noreply.github.com>
      2 Jonah Adkins <jonahadkins@gmail.com>
      2 JonFreer <j.freer@hotmail.co.uk>
      2 Johan Richer <johan.richer@jailbreak.paris>
      2 Johan <johan.richer@jailbreak.paris>
      2 Joe Innes <joe@joeinn.es>
      2 Jinkiesz <20435546+Jinkiesz@users.noreply.github.com>
      2 Jay Agaskar <jayagaskar47@gmail.com>
      2 Jarek Piórkowski <jarek@piorkowski.ca>
      2 Janko Mihelić <janjko@gmail.com>
      2 Jaime Marquínez Ferrándiz <jaime.marquinez.ferrandiz@fastmail.net>
      2 Irham Dzuhri <irham.dzuhri@gramedia.digital>
      2 Ian McEwen <mian@cyverse.org>
      2 Hussain Arif <hussainarifkl@gmail.com>
      2 Hsiao-Ting <sst.dreams@gmail.com>
      2 Gurjit Sangha <gurjit.sangha@sky.uk>
      2 Grzegorz Dąbkowski <gdabski@users.noreply.github.com>
      2 George Daneke <Flatroy@users.noreply.github.com>
      2 Gabe <zealouspencil@gmail.com>
      2 Fernando Merino <fermervil@gmail.com>
      2 Felipe <felipehfsouza@gmail.com>
      2 Erich Ritz <erich.public@protonmail.com>
      2 Dāvis Kļaviņš <68686450+Davis-Klavins@users.noreply.github.com>
      2 Dvontre Coleman <dvontrec@gmail.com>
      2 Dragoș Străinu <str.dr4605@gmail.com>
      2 Dongha Hwang <depth221@gmail.com>
      2 Dmitrii Khrustalev <31587652+DmitriiKh@users.noreply.github.com>
      2 David H. Martín <dmartina@hotmail.com>
      2 Daniela <t.dani@live.com>
      2 Daniel Reinoso <danielreinoso1807@gmail.com>
      2 CompositeRegister <78451157+CompositeRegister@users.noreply.github.com>
      2 Colin Chumak <cmchumak@myseneca.ca>
      2 Codain <Codain@users.noreply.github.com>
      2 Christopher Kwiatkowski <63965954+docentYT@users.noreply.github.com>
      2 Chris Szczechowicz <info@cjszczechowicz.com>
      2 Chris MacSwan <cmacswan07@gmail.com>
      2 Chanwit Settavongsin <max180643@gmail.com>
      2 C ✨ <charlie@sinclarius.com>
      2 Bryce Jasmer <bryce@jasmer.com>
      2 Brad <bradleofabian@gmail.com>
      2 Bobbay <49123594+Bobbbay@users.noreply.github.com>
      2 BillNas <37874504+BillNas@users.noreply.github.com>
      2 BenR31415 <rayner.ben3@gmail.com>
      2 Baptiste Mille-Mathias <bmillemathias@amadeus.com>
      2 Bacto <adrien@bacto.net>
      2 Anna Wu <wu.annay@gmail.com>
      2 Amin Jegham <amin.jeghal@gmail.com>
      2 Alain2003 <ali.zaroili@gmail.com>
      2 Adithya-Sr <97578285+Adithya-Sr@users.noreply.github.com>
      2 Aaron Muir Hamilton <aaron@correspondwith.me>
      2 Aaron <aaronlidman@gmail.com>
      1 ☕ Tim <tim@wants.coffee>
      1 zeromap <zeromap@runbox.com>
      1 zeotuan <48720253+zeotuan@users.noreply.github.com>
      1 yasmin yazdi <yyazdi13@gmail.com>
      1 xeluna <xeluna@users.noreply.github.com>
      1 wouter van der plas <wvanderplas1@lely.com>
      1 valoTN <34451873+valoTN@users.noreply.github.com>
      1 unnervingduck <71168753+unnervingduck@users.noreply.github.com>
      1 unknown <rihisime@gmail.com>
      1 u-spec-png <srdjankalaba@protonmail.ch>
      1 tommylung <tommylung@users.noreply.github.com>
      1 tevez07b9 <35212025+tevez07b9@users.noreply.github.com>
      1 tanvesh01 <sarvetanvesh01@gmail.com>
      1 tanvesh01 <52021185+tanvesh01@users.noreply.github.com>
      1 sucrerouge123 <43409115+sucrerouge123@users.noreply.github.com>
      1 sophiabonsu <37914995+sophiabonsu@users.noreply.github.com>
      1 smfuller <steven@palescale.com>
      1 saarthak_300067723 <saarthak.jain@myntra.com>
      1 rzelaya11 <r_zelyam@hotmail.com>
      1 ryuzaki221 <52002984+ryuzaki221@users.noreply.github.com>
      1 rsuttles58 <robert.suttles58@gmail.com>
      1 rspinabella <83297873+rspinabella@users.noreply.github.com>
      1 roshavagarga <roshavagarga@users.noreply.github.com>
      1 ritika99 <35415933+ritika99@users.noreply.github.com>
      1 ricloy <ricloy@users.noreply.github.com>
      1 preeformance <93346315+preeformance@users.noreply.github.com>
      1 philchisholm <151080034+philchisholm@users.noreply.github.com>
      1 pearlslugs <pearlslugs@gmail.com>
      1 noktulo <michael@tyznik.com>
      1 nis130 <nishitlimbani130@gmail.com>
      1 nicolasmaia <4v1p71+6o5kp8qcb3vos@sharklasers.com>
      1 nathannaveen <42319948+nathannaveen@users.noreply.github.com>
      1 mxdanger <32040254+mxdanger@users.noreply.github.com>
      1 mretoolforge <100172442+mretoolforge@users.noreply.github.com>
      1 misterRaven <infernoxx51@gmail.com>
      1 micaela.lechmann <micaela.lechmann@gmail.com>
      1 mellangr <darkonus@ukr.net>
      1 mahihossain <sayed.muddashir@gmail.com>
      1 lrm25 <luke.r.mccrone@gmail.com>
      1 lmagreault <laurent.magreault@gmail.com>
      1 leochras <leo@traussnigg.com>
      1 lbarros00 <laisa.barros26@gmail.com>
      1 kmedrek <kuba.medrek@yahoo.com>
      1 jmarchon <50030493+jmarchon1@users.noreply.github.com>
      1 jmacura <jmacura@users.noreply.github.com>
      1 hole1988 <hole88@home.nl>
      1 hlfan <50826859+hlfan@users.noreply.github.com>
      1 hfs <hfs@gmx.de>
      1 geospatialem <geospatialem@gmail.com>
      1 garaolaza <garaolaza@codesyntax.com>
      1 fridokus <raxomukus@gmail.com>
      1 fizdooatsprintreply <110389815+fizdooatsprintreply@users.noreply.github.com>
      1 eisams <62468530+eisams@users.noreply.github.com>
      1 druzanov <58026891+druzanov@users.noreply.github.com>
      1 docentYT <63965954+docentYT@users.noreply.github.com>
      1 diogoccosta <diogoccosta@icloud.com>
      1 ddpasa <112642920+ddpasa@users.noreply.github.com>
      1 codejockey02 <codejockey02@gmail.com>
      1 cheesecak3h <aclwxh@gmail.com>
      1 charleshtrenholm <42216351+charleshtrenholm@users.noreply.github.com>
      1 camilorecce <57818783+camilorecce@users.noreply.github.com>
      1 bpranz <bpranz.bp@gmail.com>
      1 bovlb <31326650+bovlb@users.noreply.github.com>
      1 blacx0 <josepd.capdevila@gmail.com>
      1 bharmalh <hussen.akil@gmail.com>
      1 avnishpandey113 <avnishpandey113@live.com>
      1 ashutoshshisodia <ashutosh.17bit1065@abes.ac.in>
      1 asd153866714 <asd153866714@gmail.com>
      1 apurvatripathi <alonemayank@gmail.com>
      1 alineary <alinadvries@googlemail.com>
      1 adzika <adziklipa@gmail.com>
      1 Yves Pratter <yves.pratter@gmail.com>
      1 YounessBird <67457600+YounessBird@users.noreply.github.com>
      1 Yohan <yohan@Yohans-MacBook-Pro.local>
      1 Ying Wang <ywang.botany@gmail.com>
      1 Yin Dong Wang <zhongli1994@live.cn>
      1 Yağızhan Burak Yakar <yagizhan49@protonmail.com>
      1 Wouter van der Plas <wvanderplas1@lely.com>
      1 Winn Ketchum <winn.ketchum@tomtom.com>
      1 William Edmisten <wcedmisten@gmail.com>
      1 Will Hubsch <wahubsch@gmail.com>
      1 Will <wahubsch@gmail.com>
      1 Voron3d <Voron3d@gmail.com>
      1 Vladimir Alexiev <vladimir.alexiev@ontotext.com>
      1 Vivek Shah <viveknshah@users.noreply.github.com>
      1 Vincent Lafeychine <vincent.lafeychine@proton.me>
      1 Undearius <steveyzrkicksbutt@hotmail.com>
      1 Tubaleviao <alvaro.prata.filho@gmail.com>
      1 TownCube <15699466+TownCube@users.noreply.github.com>
      1 Tony Lee <30307659+hytonylee@users.noreply.github.com>
      1 Tommy Oldfield <koaxuaudio@gmail.com>
      1 Tomasz Lewandowski <tlewandster@gmail.com>
      1 Tom Stewart <tstewart15@users.noreply.github.com>
      1 Tom Morris <tom@tommorris.org>
      1 TishG <38973991+TishG@users.noreply.github.com>
      1 Timmy-Tesseract <71176747+Timmy-Tesseract@users.noreply.github.com>
      1 Tim Parsons <timmparsons85@gmail.com>
      1 Tim <tim@wants.coffee>
      1 Thusal06 <66709891+Thusal06@users.noreply.github.com>
      1 Thilakshan Arulnesan <47302571+ThilakshanArulnesan@users.noreply.github.com>
      1 Teemu Piippo <crimsondusk64@gmail.com>
      1 Taylor Smith <tavlor@protonmail.com>
      1 Swapna <manupati.swapna2@gmail.com>
      1 Suman Nath <mesuman287@gmail.com>
      1 Stuart Morgan <smorgan@mythtv.org>
      1 SteveLz <stevel2520@gmail.com>
      1 Simon Legner <Simon.Legner@gmail.com>
      1 Shubham Rajput <shubham.rajput01@infosys.com>
      1 ServusWorld <31391499+ServusWorld@users.noreply.github.com>
      1 Sergi Miralles <uxx4pv85@mailer.me>
      1 Senpaistorm <austin.l@qq.com>
      1 Scott Anecito <sanecito@users.noreply.github.com>
      1 Schokobecher <Schokobecher@gmail.com>
      1 Sahil Siddiq <39989901+valdaarhun@users.noreply.github.com>
      1 Sahib <sarora42@mysenecac.ca>
      1 Rupesh Chaudhari <30570616+hrupesh@users.noreply.github.com>
      1 Roy Jia <roy.jia@outlook.com>
      1 Rory McCann <rory@technomancy.org>
      1 Rodrigo Tavares <rodrigost23@users.noreply.github.com>
      1 Robbin Johansson <mail@robbin.works>
      1 Rifa Achrinza <25147899+achrinza@users.noreply.github.com>
      1 RicoElectrico <ricoelectrico@orange.pl>
      1 RedAuburn <endim8@pm.me>
      1 Rashmi <rashmiap.10@gmail.com>
      1 Raphael Das Gupta <git@raphael.dasgupta.ch>
      1 RandomGuy <66908644+manjukrishna1837@users.noreply.github.com>
      1 Ramon Bezerra <ramonbezerra90@gmail.com>
      1 Rajat Upadhyay <43850934+rajatmw1999@users.noreply.github.com>
      1 Rajat Chowdhury <43143912+Rajat-Chowdhury@users.noreply.github.com>
      1 Rachelle Hu <rachelle.hu123@gmail.com>
      1 RCRalph <36704328+RCRalph@users.noreply.github.com>
      1 Quincy Morgan <quincylvania@users.noreply.github.com>
      1 Qing Cai <qing.cai@tomtom.com>
      1 PrimeN <arash_negari@yahoo.ca>
      1 Prayag <52105313+prayagd@users.noreply.github.com>
      1 Po Chun, Lu <oceanus11034@gmail.com>
      1 Piper McCorkle <contact@piperswe.me>
      1 Pieter Vander Vennet <pietervdvn@posteo.net>
      1 Philippe Carvalho <31983398+phcarval@users.noreply.github.com>
      1 Peter Cho <pcho51990@gmail.com>
      1 PatrickMackridge <38439947+PatrickMackridge@users.noreply.github.com>
      1 Patrick Salvatore <44264255+patrick-salvatore@users.noreply.github.com>
      1 OthankQ <41326930+OthankQ@users.noreply.github.com>
      1 Oskar F <raxomukus@gmail.com>
      1 Ollie <oliver.siket@gmail.com>
      1 Oliver Siket <oliver.siket@gmail.com>
      1 Oleh Yaroshchuk <1oleq25@gmail.com>
      1 Noémie <noemie.lehuby@openstreetmap.fr>
      1 Noé Lopez <51089082+Bqleine@users.noreply.github.com>
      1 Nokolai Timofeev <71152094+n-timofeev@users.noreply.github.com>
      1 Noah Blumenstein <69017889+roadtomoab@users.noreply.github.com>
      1 Nishit Patel <nishitlimbani130@gmail.com>
      1 Niharika Pandit <niharikap219@gmail.com>
      1 Nicolas MARET <maret.nicolas@gmail.com>
      1 Nicolas Hohm <nickel7152@gmail.com>
      1 NiAlvarez <nicolas.alvarez@fluxit.com.ar>
      1 Mohammed Chhatriwala <mohammed.chhatriwala@bt.com>
      1 Mohammad Javad Afkari <wmateam@gmail.com>
      1 Mitch Barnett <mitch@mitchbarnett.com>
      1 Minh Pham <est2000vn@gmail.com>
      1 Mikkel Kirkgaard Nielsen <memb_github@mikini.dk>
      1 Mike Smith <msmith@bioneos.com>
      1 Miguel Ángel Latre Abadía <latre@unizar.es>
      1 Michal Vinárek <michal.vinarek@gmail.com>
      1 Michael Wahba <mwahba@ucalgary.ca>
      1 Michael Dettbarn <michael.dettbarn@physik.uni-wuerzburg.de>
      1 Michael <50381321+michalisKout@users.noreply.github.com>
      1 Michael <30999326+Discostu36@users.noreply.github.com>
      1 Meisyarah Dwiastuti <meisyarah.dwiastuti@gmail.com>
      1 Meisyarah Dwiastuti <Meisyarah Dwiastuti>
      1 Matthias Feist <github.com@matf.de>
      1 Matthew Wootten <mwootten@localhost.localdomain>
      1 Matheus Gomes <matheus.gomes03@hotmail.com>
      1 Martin Raifer <martin@raifer.tech>
      1 Mariano Salamanca Jr <msalamancajr@gmail.com>
      1 Mariana de Albuquerque Campos <marianaalbuquerque02@gmail.com>
      1 Marco Antonio <marcoantoniofrias@gmail.com>
      1 Marc-marc-marc <31963329+Marc-marc-marc@users.noreply.github.com>
      1 Maksim Gurtovenko <maksim@gurtovenko.name>
      1 Mahi Hossain <sayed.muddashir@gmail.com>
      1 Lyndi Castrejon <47511217+lyndic@users.noreply.github.com>
      1 Luzandro <andreas.wecer@gmail.com>
      1 Lulucmy <lulucmy@live.com>
      1 Lukas Winkler <git@lw1.at>
      1 Luis Balbás <lbq200@gmail.com>
      1 Luis Anton Imperial <imperialluisanton@outlook.ph>
      1 Lucas Werkmeister <mail@lucaswerkmeister.de>
      1 Lucas Narciso <lucasnar@gmail.com>
      1 Luc Gommans <lgommans@users.noreply.github.com>
      1 Liad Yosef <liady@users.noreply.github.com>
      1 Leonardo Colman Lopes <dev@leonardo.colman.com.br>
      1 Lens0021 / Leslie <lorentz0021@gmail.com>
      1 Lemuria <74448738+a-random-lemurian@users.noreply.github.com>
      1 Lee Doughty <leedoughtydesign@gmail.com>
      1 Laxminarayan Majhi <laxminarayanmajhi@Laxminarayans-Mac-mini.local>
      1 Lachlan Rehder <lachlan2357@outlook.com>
      1 Lachlan Rehder <33368366+lachlan2357@users.noreply.github.com>
      1 Károlyi Péter Márton <karolyi.peter.marton@gmail.com>
      1 Kálmán „KAMI” Szalai <kami911@gmail.com>
      1 Kyle Mckay <kymckay.dev@gmail.com>
      1 Kiel <kielhurley@gmail.com>
      1 Kezxo <Kezxo@users.noreply.github.com>
      1 Kevin Mai <40449746+maingockien01@users.noreply.github.com>
      1 Kazing <41507326+Kazing@users.noreply.github.com>
      1 Kasper Sanguesa-Franz <kasper@franz.guru>
      1 Karen Kerr <138442998+karen-kerr@users.noreply.github.com>
      1 Karen Douglas <kdindependence@gmail.com>
      1 Justin Doak <justin.doak@stablekernel.com>
      1 Justin Bento <44421842+Justin-Bento@users.noreply.github.com>
      1 Juan Carlos González Fernández <juancarlos.gonzalezfernandez@iesmiguelherrero.com>
      1 José Luis <puenterodriguezjose@gmail.com>
      1 Jonathan Freer <30393324+JonFreer@users.noreply.github.com>
      1 Jonathan Bareket <32452833+Johnnybar@users.noreply.github.com>
      1 John A. Leuenhagen <john@zlima12.com>
      1 JoeyKentin <71698370+JoeyKentin@users.noreply.github.com>
      1 Joey Marshment-Howell <josephkmh@users.noreply.github.com>
      1 Joe Westcott <joewestcott@users.noreply.github.com>
      1 Jimmie Smith <84278458+FriendOfDorothy@users.noreply.github.com>
      1 JesseWeinstein <jesse@wefu.org>
      1 Jean-Frederic <jeanfrederic.wiki@gmail.com>
      1 Jay Turner <jay@trainerdex.app>
      1 Javbw <johnw@mac.com>
      1 Janek <xerusx@pm.me>
      1 Janek <27jf@pm.me>
      1 Jan Silbersiepe <jan@targomo.com>
      1 Jack Wong <jackwzj@spgroup.com.sg>
      1 Jack Rosenblatt <45472610+JackRosenblatt1@users.noreply.github.com>
      1 JZachrisson <jesper.zachrisson@gmail.com>
      1 Ilya Zverev <ilya@zverev.info>
      1 HubMiner <g246020@aol.com>
      1 Hel Nershing Thapa <51614993+HelNershingThapa@users.noreply.github.com>
      1 Harshit <7harshit20@gmail.com>
      1 Harry Bond <endim8@pm.me>
      1 Gustavo Soares <77340463+Playzinho@users.noreply.github.com>
      1 Guillaume Verstraete <versgui+github@protonmail.com>
      1 Grant Slater <grant.slater@paconsulting.com>
      1 GrandmaCoding <jmetzger5@gmail.com>
      1 Giovanni Alfredo Garciliano Díaz <rapunzel@disroot.org>
      1 Gerson Alvarado <Lewatoto@users.noreply.github.com>
      1 Gerard Fajardo <gedfaj@gmail.com>
      1 Gabriel Manfroi <32476134+gabemanfroi@users.noreply.github.com>
      1 FredPavao <frederico.pavao@tts.com>
      1 ForgottenHero <whackedman@msn.com>
      1 Filip <filipilicfilip@gmail.com>
      1 Felipe Henrique <felipehfsouza@gmail.com>
      1 Fabio Massaretto <>
      1 Evgeny <batyrmastyr@ya.ru>
      1 Evgenii Smirnov <smirnov.eo@gmail.com>
      1 Evgeni <50407089+darkkrol16@users.noreply.github.com>
      1 Evan Carroll <me@evancarroll.com>
      1 Eric_C <ericcao@bu.edu>
      1 Eric G <e+pgp9225@linuxw.info>
      1 Endy99 <64232986+Endy99@users.noreply.github.com>
      1 Emmy D'Anello <ynerant@emy.lu>
      1 Emmet Allen <59685332+Mrskillful@users.noreply.github.com>
      1 Eleni Papanicolas <76261375+e-papanicolas@users.noreply.github.com>
      1 Eddy Dardour <eddy.dardour.pro@gmail.com>
      1 Dustin Watkins <38428507+watkins656@users.noreply.github.com>
      1 Dimitar Dimitrov <dev.dimitar.dimitrov@gmail.com>
      1 Diego Eiras <eiras.lucio@gmail.com>
      1 Diana <dianacpgouveia@gmail.com>
      1 Denis Oliveira <denis.olvr@gmail.com>
      1 Dayal <dayal.sharan@nestaway.com>
      1 Dawn Summerall <dawn@mgmdesign.com>
      1 Dawid2849 <77780707+Dawid2849@users.noreply.github.com>
      1 David Henshaw <31974655+drahenshaw@users.noreply.github.com>
      1 Dane Springmeyer <dane@dbsgeo.com>
      1 Dan Stowell <danstowell@users.sourceforge.net>
      1 Damien Picard <dam.pic@free.fr>
      1 Clay <clay@clay-desktop.lan>
      1 Christopher Meng <im@dyi.ng>
      1 Christopher Greene-Szmadzinski <christopher.blue@gmail.com>
      1 Chen (Kina) <adult@live.cn>
      1 Charlotte M <sinclarius@users.noreply.github.com>
      1 Carlos <erielkhan@gmail.com>
      1 Caleb McQuaid <McQuaid_Caleb@bah.com>
      1 Bruno Bigras <bigras.bruno@gmail.com>
      1 Brianna Marie <briannarodriguez0529@gmail.com>
      1 Brian Egge <brianegge@gmail.com>
      1 Brent Ottke <marieottke@Maries-MacBook-Air.local>
      1 Branko Kokanovic <branko@kokanovic.org>
      1 Berrely <20139168+berrely@users.noreply.github.com>
      1 Ben Rayner <rayner.ben3@gmail.com>
      1 Ayush Raj <raj.ayush012@gmail.com>
      1 Axel <62251475+Asteliks@users.noreply.github.com>
      1 Athif Shaffy <athif.shaffy@gmail.com>
      1 Arturo Miranda <artumira8@gmail.com>
      1 Arturo Miranda <80984726+Artumira96@users.noreply.github.com>
      1 Artur H. Lange <ArturLange@users.noreply.github.com>
      1 Arthur <atu.cr92@gmail.com>
      1 Apurva-Singh <apurva.17bit1054@abes.ac.in>
      1 Apurva Singh <65821097+Apurva-Singh@users.noreply.github.com>
      1 April Copley <52804777+acopperlily@users.noreply.github.com>
      1 Anthony Tong <darkintragedy@gmail.com>
      1 AnonymousAlligatorOSM <anonymousalligatorosm@gmail.com>
      1 Anomalyce <47085833+anomalyce@users.noreply.github.com>
      1 AnnaYWu <50470094+AnnaYWu@users.noreply.github.com>
      1 André <andre@dev-next.com>
      1 Andrew MacLeod <A6macleod@gmail.com>
      1 Andrej Shadura <andrew@shadura.me>
      1 Amey <43315144+amey-kudari@users.noreply.github.com>
      1 Alina <85510512+alineary@users.noreply.github.com>
      1 Alexander Jones <happy5214@gmail.com>
      1 Alex Smith <alex@smithhub.me>
      1 Alex Smith <18553943+squishynsmoo@users.noreply.github.com>
      1 Alex <alex.jaravete@gmail.com>
      1 AlesKubr1 <110310297+AlesKubr1@users.noreply.github.com>
      1 Alasdair Nicol <alasdair@thenicols.net>
      1 Aku <aku.n.makela@gmail.com>
      1 Afiq Nazrie <afnazrie@gmail.com>
      1 Adwaiya Srivastav <adwaiyasrivastav@gmail.com>
      1 Adrien <adrien.rousselet@adotmob.com>
      1 Adam Mendenhall <amendenhall@live.com>
      1 Adam <adam.watson@myunidays.com>
      1 ASHUTOSH KUMAR CHOUDHARY <choudharykumarashutosh1209@gmail.com>
      1 = <=>
      1 1papaya <1love1papaya@gmail.com>
      1 1-Byte <1-Byte@users.noreply.github.com>

---
## [kittysmooch/Skyrat-tg](https://github.com/kittysmooch/Skyrat-tg)@[41026ae8b1...](https://github.com/kittysmooch/Skyrat-tg/commit/41026ae8b1a14b9380ca7af9885939c9f2dc060e)
#### Tuesday 2023-12-19 13:50:07 by SkyratBot

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
## [sarkarbikram90/cockroachDB](https://github.com/sarkarbikram90/cockroachDB)@[d1ddc072a8...](https://github.com/sarkarbikram90/cockroachDB/commit/d1ddc072a8c10c7568166af9495e6418df3e5a22)
#### Tuesday 2023-12-19 13:55:02 by craig[bot]

Merge #114273

114273: pkg/util/aggmetric: tick histogram windows in AggHistogram r=aadityasondhi a=abarganier

Fixes: https://github.com/cockroachdb/cockroach/issues/114175, https://github.com/cockroachdb/cockroach/issues/112947

**NOTE**: The ideal way to fix this is merging `pkg/util/metric/aggmetric` into 
`pkg/util/metric`. That way, we wouldn't have to expose any of the "tick" 
functionality in the histogram public API. However, merging the two packages 
would be a pain to backport, and therefore we're leaving the merging to a 
follow up PR (coming soon). In the meantime, this provides a fix with a minimized 
surface area, so that we can more easily backport the fix. The merging will only 
occur on the master branch. 

**Reviewer note:** Recommended to review commit-wise.

---

AggHistograms are wrappers around the histogram implementations found in
pkg/util/metric. Internally, Histogram implementations within
pkg/util/metric maintain histogram windows to calculate quantiles at
each scrape by CockroachDB's TSDB, instead of storing every single
histogram bucket. These windows are rotated periodically, where the
current window becomes the previous window, and the current window is
then set to a new histogram. This allows us to diff the two windows, and
internally, pkg/util/metric has "ticking" functionality which is
responsible for rotating these histogram windows.

Unfortunately, since `pkg/util/metric/aggmetric` is in a separate
package, somehow this "ticking"/rotating of histogram windows was never
implemented into the AggHistogram. Because of this, it's likely that
metrics powered by AggHistogram have been broken since its inception
within CockroachDB's internal TSDB (but work fine in Prometheus).

Previous patches did some work to expose this ticking library to
AggHistogram, and this patch implements it.

In this patch, we make it so AggHistogram ticks/rotates histogram
windows, similar to how the other Histogram library does it. Since
AggHistograms have child histograms, this means that the rotation of all
histograms for both parent and children need to be done atomically. We
implement this by providing the AggHistogram its own tick.Ticker, where
the onTick function holds a RWMutex shared by the parent & all its
children and rotates the histograms for all.

With this in place, histogram windows are properly rotated for
AggHistograms. Future work will merge `pkg/util/metric/aggmetric` into
`pkg/util/metric`, after which we can once again make all this ticking
functionality private to the metrics package.

Release note (bug fix): Previously, all `AggHistogram`-powered metrics
were not reporting quantiles properly in DB Console. The list of
affected metrics is:

- changefeed.message_size_hist
- changefeed.parallel_io_queue_nanos
- changefeed.sink_batch_hist_nanos
- changefeed.flush_hist_nanos
- changefeed.commit_latency
- changefeed.admit_latency
- jobs.row_level_ttl.span_total_duration
- jobs.row_level_ttl.select_duration
- jobs.row_level_ttl.delete_duration

This patch fixes the histograms so that the quantiles in DB Console are
reported correctly.

Please note: these histograms were only broken in the DB Console metrics
features, but were **not** broken in the Prometheus-compatible endpoint,
`/_status/vars`.

## Screenshots

#### AggHistogram in DB Console pre-fix:
![pre](https://github.com/cockroachdb/cockroach/assets/8194877/aa08592b-4ebd-43d5-acff-8d00edc4ada1)

#### AggHistogram in DB Console post-fix:
<img width="1059" alt="Screenshot 2023-11-10 at 4 06 57 PM" src="https://github.com/cockroachdb/cockroach/assets/8194877/723c4974-e038-4871-9721-8ec18fca5f95">

#### AggHistogram in Grafana post-fix:
<img width="1648" alt="Screenshot 2023-11-10 at 4 07 22 PM" src="https://github.com/cockroachdb/cockroach/assets/8194877/05920189-c1b1-4895-a1fa-b8b1e069407a">


Co-authored-by: Alex Barganier <abarganier@cockroachlabs.com>

---
## [StrangeWeirdKitten/Skyrat-tg](https://github.com/StrangeWeirdKitten/Skyrat-tg)@[1a2ab1b13c...](https://github.com/StrangeWeirdKitten/Skyrat-tg/commit/1a2ab1b13c2da4eee7c39df31695926b13048063)
#### Tuesday 2023-12-19 14:07:22 by SkyratBot

[MIRROR] Touches up Moffuchi's pizzeria  [MDB IGNORE] (#25246)

* Touches up Moffuchi's pizzeria  (#79899)

## About The Pull Request
I've given the icebox pizzeria ruin a few small improvements:
- Firstly, The kitchen is actually stocked with tomatoes from the get
go. Along with a few mothic themed ingredients for those signature
mothic pizzas we all know and love (And hate for being such a pain to
make)
- The discarded air alarm frames have been replaced with working ones
(I'm unsure if this was intentional or not)
- Some drinking glasses have been added to the bar
- And finally a pacman has been placed in the backroom along with some
plasma to power the place
## Why It's Good For The Game
This place gets overlooked a lot because its completely powerless, and
doesn't actually give you enough from the get go to make even a basic
pizza besides the tomato seeds a lot of people are gonna miss. This
gives the ruin just a little more life to maybe be worth trekking out
for. And having mothic themed ingredients in the **MOFFIC** Pizzeria
just makes sense even if they are a bitch to make.

Not sure if this counts as a balance change or a QOL so feel free to
yell at me if I've labelled this wrong, I have been advised that this
SHOULD be the latter at least.
## Changelog
:cl:
qol: Mothuchi's pizzeria has been improved slightly! Order yourself a
fresh mothic pizza today!
/:cl:

* Touches up Moffuchi's pizzeria

---------

Co-authored-by: DaydreamIQ <62606051+DaydreamIQ@users.noreply.github.com>
Co-authored-by: Bloop <13398309+vinylspiders@users.noreply.github.com>

---
## [Majkl-J/Bubberstation](https://github.com/Majkl-J/Bubberstation)@[fa8399334f...](https://github.com/Majkl-J/Bubberstation/commit/fa8399334f9bc10abbf6ddf25b40e43b5363a9ae)
#### Tuesday 2023-12-19 14:28:16 by The-Sun-In-Splendour

Horrorform changeling salt PR (#859)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Now okay. I get it. It's huge, it's obvious, it's slow... I don't care
if it has more health and sustain than a tank spider or blobbernaut.
What I care is that it can fit into vents.

You can kill a changeling horror form with enough manpower. It's hard
but it's doable. But the fucking fact it can just... Ventcrawl into any
vent and if you don't see the tiny icon during the shitshow and push it?
Sorry but that is just absolute aids gameplay. Usually the monsters with
ventcrawl are pretty weak to make up for it. But not horrorling. I'm
sorry but if you have;

1. 750 health
2. 40 fucking damage swings (A double esword is 34 damage)
3. Passive, CONSTANT life regen
4. Lifesteal off dead bodies

You do **_not_** need ventcrawl. 

## Why it's good for the game

Do I really need to explain why having this almost unkillable machine be
able to ventcrawl to escape practically every situation because "teehee
forgot to weld vent in obscure location!" is bad for the game?

Yes. This is a salt PR.

:cl:
balance: Horror ling cannot ventcrawl anymore
/:cl:

---
## [ShamanSliph/Bubberstation](https://github.com/ShamanSliph/Bubberstation)@[85ee756c24...](https://github.com/ShamanSliph/Bubberstation/commit/85ee756c24905736dac9c468ad25f3cf626d4a55)
#### Tuesday 2023-12-19 14:40:13 by SkyratBot

[MIRROR] [CI Fix] The Demonic Frost-Miner will not attack corpses. [MDB IGNORE] (#24615)

* [CI Fix] The Demonic Frost-Miner will not attack corpses. (#79294)

## About The Pull Request

Fixes #79147.

Prevents the Demonic Frost-Miner from shooting at corpses by returning
early from `OpenFire()`. Also adds the "gutted" status effect to the
corpses in its arena so it won't try to gut them.
## Why It's Good For The Game

#78826 introduced an unfortunate bug by placing corpses in the Frost
Miner's arena. There were a combination of three factors at play here:
that the Miner attacks corpses, that it happens to use colossus bolts in
its attacks, which dust corpses, and that some unfortunate quirk of life
code causes runtimes if, as far as I can tell, a life tick goes off when
a mob is at the wrong point in the dusting process. The time this
process takes happened to perfectly coincide with the Monkey Business
unit test (being the first test that takes a significant period of
time), causing it to randomly fail.

So, this fixes a flaky test that has been a pain in the ass for the last
five days, is the big thing.

Also, it can't possibly have been intended for the Miner to run around
obliterating the aesthetic corpses in its arena within the first 15
seconds of any given round. Completely ruining the mood!

I'll point out that this particular boss may have been forgotten in
#77731, which set out to make only the colossus still gib/dust you, but
even were that not the case I think it would be a bit silly for the
Miner to be busy shooting lifeless corpses when a player shows up to
challenge it, rather than standing in its scary ritual circle.
## Changelog
:cl:
fix: The Demonic Frost-Miner will no longer run around destroying the
corpses in its arena the moment the round begins.
/:cl:

* [CI Fix] The Demonic Frost-Miner will not attack corpses.

---------

Co-authored-by: lizardqueenlexi <105025397+lizardqueenlexi@users.noreply.github.com>

---
## [Bubberstation/Bubberstation](https://github.com/Bubberstation/Bubberstation)@[d96b2b97aa...](https://github.com/Bubberstation/Bubberstation/commit/d96b2b97aa9969f4a9d800ec0bc8501fcf3529ef)
#### Tuesday 2023-12-19 14:41:07 by Waterpig

Waterpig grows more insane with modularity: The massive PR that probably breaks shit (#838)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

I have circuitry theory finals in 1 hour. And as such, to distract
myself from my impending doom and to stop thinking about loop currents,
I have decided to start working on this. (Update: I passed)

This isn't even close to how I wish our modularity to look

But that's future Waterpig's problem (Note to self: Fix the no_antag
button)

In another news, this probably breaks stuff.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Please make sure to actually test your PRs. If you have not tested
your PR mention it. -->

## Why It's Good For The Game

Modularity is good. The more stuff we can modularize the better, and
incase it gets removed upstream it's as simple as... removing our
modular override.
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
refactor: Refactors modularity significantly
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

---------

Co-authored-by: The Sharkening <95130227+StrangeWeirdKitten@users.noreply.github.com>

---
## [semrush/intergalactic](https://github.com/semrush/intergalactic)@[1e3807fa31...](https://github.com/semrush/intergalactic/commit/1e3807fa31e40226cba8c2957bbdc06aefe161db)
#### Tuesday 2023-12-19 14:42:18 by Michael Sereniti

[d3-chart] fixed chart legend table trimming with Ellipsis component (#962)

## Motivation and Context

Found that ellipsis doesn't work in the chart legend table grid.
I have found some wierd hacks
([1](https://css-tricks.com/preventing-a-grid-blowout/),
[2](https://stackoverflow.com/questions/36230944/prevent-flex-items-from-overflowing-a-container))
that make everything work like a charm.

## How has this been tested?

It almost impossible to test in our screenshot unit tests because
ellipsis needs a trimming rerender.

## Screenshots:

Before:

<img width="746" alt="Screen Shot 2023-12-12 at 14 15 42"
src="https://github.com/semrush/intergalactic/assets/31261408/6596acc7-7085-4742-9331-599b17f9d205">

After:

<img width="610" alt="Screen Shot 2023-12-12 at 14 14 12"
src="https://github.com/semrush/intergalactic/assets/31261408/4568e46c-b60c-4c18-b515-4aaa35344771">

## Types of changes

<!--- What types of changes does your code introduce? Put an `x` in all
the boxes that apply: -->

- [x] Bug fix (non-breaking change which fixes an issue).
- [ ] New feature (non-breaking change which adds functionality).
- [ ] Breaking change (fix or feature that would cause existing
functionality to not work as expected).
- [ ] Nice improve.

## Checklist:

<!--- Go over all the following points, and put an `x` in all the boxes
that apply. -->
<!--- If you're unsure about any of these, don't hesitate to ask. We're
here to help! -->

- [x] My code follows the code style of this project.
- [x] I have updated the documentation accordingly or it's not required.
- [x] Unit tests are not broken.
- [x] I have added changelog note to corresponding `CHANGELOG.md` file
with planned publish date.
- [ ] I have added new unit tests on added of fixed functionality.

---
## [vtex/faststore](https://github.com/vtex/faststore)@[d476541686...](https://github.com/vtex/faststore/commit/d4765416862d2386e2b1a7767c2ee455282584d3)
#### Tuesday 2023-12-19 14:43:57 by Fanny Chien

fix: Display discount badge only when has discount (#2173)

## What's the purpose of this pull request?

This PR attempts to fix scenario when there is no discount applied in
the product, and sale price is > listing price.

<img width="233" alt="image"
src="https://github.com/vtex/faststore/assets/3356699/fef94c1e-d50f-4c29-843b-41cbeca10783">


_I wonder if this logic should be inside the `ProductCardContent`
component (fs/ui library) or in the core. Any thoughts?_


## How it works?

When no discount applied, we should not display the `DiscountBadge`
component.

## How to test it?

<img width="1322" alt="image"
src="https://github.com/vtex/faststore/assets/3356699/3256f552-318b-4688-9ea2-08f37e7ae177">

1. Go to homepage -> Look for `Apple Magic Mouse` in the Most Wanted
section.
2. The `infinity` badge should not appear.

### Starters Deploy Preview

<!--- Add a link to a deploy preview from `gatsby.store` AND
`nextjs.store` with this branch being used. --->

<!--- Tip: You can get an installable version of this branch from the
CodeSandbox generated when this PR is created. --->

## References


[FS-1482](https://vtex-dev.atlassian.net/browse/FS-1482?atlOrigin=eyJpIjoiMWU1MGFjYTZkY2RiNDY2MGE0NGI4ZDZiNmZjODRkMWEiLCJwIjoiaiJ9)


[FS-1482]:
https://vtex-dev.atlassian.net/browse/FS-1482?atlOrigin=eyJpIjoiNWRkNTljNzYxNjVmNDY3MDlhMDU5Y2ZhYzA5YTRkZjUiLCJwIjoiZ2l0aHViLWNvbS1KU1cifQ

---
## [ZacharyTStone/ZacharyTStone](https://github.com/ZacharyTStone/ZacharyTStone)@[be6ef43786...](https://github.com/ZacharyTStone/ZacharyTStone/commit/be6ef43786004710f672e9314dad65a26fc62378)
#### Tuesday 2023-12-19 15:04:10 by ROBO-ZACH

Update README with new quote: "Read as you taste fruit or savor wine, or enjoy friendship, love or life." <br>— George Herbert

---
## [inttter/md-badges](https://github.com/inttter/md-badges)@[1aa57c7656...](https://github.com/inttter/md-badges/commit/1aa57c765684b4254bd48801b1faaf48a4c6f7a1)
#### Tuesday 2023-12-19 15:29:44 by Inter

+ 🎨 Reformatted "Website and Service Status" badges (#80)

---------
- 📄 Seperated the code coverage badges and the website status badges from that category to their own respective ones
- 🔥 Removed "Netlify" and "Heroku" as they are hosting platforms and there isn't currently a section for hosting yet (coming soon though!)

- ⚠️ Removed many badges relating to repository status ⚠️

This was done as they honestly did not fit the other sections and this whole project in general.
I mean, take a look yourself at the other sections, they're stuff like "Browsers" and "Social Media". Having "docker pulls: 100" (example) just would not fit in this repo.

If you want these kinds of badges, see things like [dwyl/repo-badges](https://github.com/dwyl/repo-badges), or this [Medium article](https://sharifsuliman.medium.com/modern-github-badges-for-open-source-repositories-fb4dceeb368a) for some inspiration.
---------

---
## [AkihiroSuda/runc](https://github.com/AkihiroSuda/runc)@[8e8b136c49...](https://github.com/AkihiroSuda/runc/commit/8e8b136c4923ac33567c4cb775c6c8a17749fd02)
#### Tuesday 2023-12-19 16:01:14 by Aleksa Sarai

tree-wide: use /proc/thread-self for thread-local state

With the idmap work, we will have a tainted Go thread in our
thread-group that has a different mount namespace to the other threads.
It seems that (due to some bad luck) the Go scheduler tends to make this
thread the thread-group leader in our tests, which results in very
baffling failures where /proc/self/mountinfo produces gibberish results.

In order to avoid this, switch to using /proc/thread-self for everything
that is thread-local. This primarily includes switching all file
descriptor paths (CLONE_FS), all of the places that check the current
cgroup (technically we never will run a single runc thread in a separate
cgroup, but better to be safe than sorry), and the aforementioned
mountinfo code. We don't need to do anything for the following because
the results we need aren't thread-local:

 * Checks that certain namespaces are supported by stat(2)ing
   /proc/self/ns/...

 * /proc/self/exe and /proc/self/cmdline are not thread-local.

 * While threads can be in different cgroups, we do not do this for the
   runc binary (or libcontainer) and thus we do not need to switch to
   the thread-local version of /proc/self/cgroups.

 * All of the CLONE_NEWUSER files are not thread-local because you
   cannot set the usernamespace of a single thread (setns(CLONE_NEWUSER)
   is blocked for multi-threaded programs).

Note that we have to use runtime.LockOSThread when we have an open
handle to a tid-specific procfs file that we are operating on multiple
times. Go can reschedule us such that we are running on a different
thread and then kill the original thread (causing -ENOENT or similarly
confusing errors). This is not strictly necessary for most usages of
/proc/thread-self (such as using /proc/thread-self/fd/$n directly) since
only operating on the actual inodes associated with the tid requires
this locking, but because of the pre-3.17 fallback for CentOS, we have
to do this in most cases.

In addition, CentOS's kernel is too old for /proc/thread-self, which
requires us to emulate it -- however in rootfs_linux.go, we are in the
container pid namespace but /proc is the host's procfs. This leads to
the incredibly frustrating situation where there is no way (on pre-4.1
Linux) to figure out which /proc/self/task/... entry refers to the
current tid. We can just use /proc/self in this case.

Yes this is all pretty ugly. I also wish it wasn't necessary.

Signed-off-by: Aleksa Sarai <cyphar@cyphar.com>

---
## [StrangeWeirdKitten/Bubberstation](https://github.com/StrangeWeirdKitten/Bubberstation)@[8f3d1036c8...](https://github.com/StrangeWeirdKitten/Bubberstation/commit/8f3d1036c8f4f7b51acc6bad8b28009a81e20ac4)
#### Tuesday 2023-12-19 16:15:18 by SkyratBot

[MIRROR] Refactor icemoon wolves into basic mobs and add taming + pack behavior [MDB IGNORE] (#25126)

* Refactor icemoon wolves into basic mobs and add taming + pack behavior (#79736)

## About The Pull Request

Ports icemoon wolves over to the basic mob framework with a bit of extra
stuff:

- Wolves call for help when attacked within a decently large radius.
Because you know, pack animals.
- Wolves can now be tamed with a slab of meat
- When tamed, wolves can be ridden like goliath mounts. Ride wolf, life
good. Pretend you're playing ARK and start shivering to death in thatch
huts for that High Roleplay experience.
- Tamed wolves have access to a bunch of pet commands (following, point
fetching, point attacking, play dead, etc) and will also defend their
owners vehemently if they're attacked.

You can probably tame multiple if you wanted to.

## Why It's Good For The Game

What part about riding wolves isn't entertaining? I don't really play
/tg/ that much so I can't argue too much about the balance implications
this might pose, but it's undoubtedly a stupid little gimmick and is
likely to be used by bored assistants and miners with too much time on
their hands.

Especially robust individuals will probably find a million things to do
with a basic mob capable of fetching, attacking on command and generally
being able to defend themselves decently well.

## Changelog

:cl: yooriss
refactor: Icemoon wolves now use the basic mob framework and should act
more intelligently, defending their pack.
add: Icemoon wolves can be tamed with slabs of meat and can be ridden as
mounts once friendly. Being rather large dogs, they also have access to
most of the pet commands you'd expect, such as fetching things, and
violently mauling people their owners point at.
/:cl:

---------

Co-authored-by: san7890 <the@ san7890.com>

* Refactor icemoon wolves into basic mobs and add taming + pack behavior

---------

Co-authored-by: Ephemeralis <Ephemeralis@users.noreply.github.com>
Co-authored-by: san7890 <the@ san7890.com>

---
## [Roadhog360/Et-Futurum-Requiem](https://github.com/Roadhog360/Et-Futurum-Requiem)@[aef5968a71...](https://github.com/Roadhog360/Et-Futurum-Requiem/commit/aef5968a71be261fc3f72f2848a6c2ba5e8cab5a)
#### Tuesday 2023-12-19 16:39:27 by Roadhog360

OK SMARTASS INTERPRETER JUST HAVE IT ALL
OH THIS IS MISSING OH THAT IS MISSING WHO FUCKING CARES JUST COMPILE IT ANYWAYS AND IGNORE THE ONE GODDAMN MISSING FUNCTION UNTIL I COMMIT THE CODE
People be like "oh just use branches" "just commit a bit at a time" I TRY THAT AND THIS SHIT IS WHAT FUCKING HAPPENS
build failed build fauileldd sdfbsfogdiuhaeraipiz[p
It just leads to build failures
So when people tell me to use branches to confuse my code or make more """""organized""""" commits I link them to this message. Yes I'm tilted
Let's see Gradle fail this one too because it likes to be an asshole

- Add soul fire gen through WorldGenSoulFire and apply it to NetherChunkProvider, so soul fire appears on soul soil when enabled
- Due to failures with forge's custom item entity system, it has been removed and replaced with a mixin. Bugs include custom item-entities jittering when first spawned in and /give not dispensing the item into the player's inventory. It's clear the custom item entity system was NOT thoroughly tested by Forge. Old uninflammable items that exist in the world will be converted to the regular item entities automatically.
  - A system to add/remove items via the config or mod code will be added in the future, as well as adjusting their buoyancy
 - Add a biome list helper function to Utils.java, to make it easier to create biome lists with certain blacklists

---
## [HickeysTechCompany/finalsprintbackend](https://github.com/HickeysTechCompany/finalsprintbackend)@[0bcb5c8c5c...](https://github.com/HickeysTechCompany/finalsprintbackend/commit/0bcb5c8c5c7b7d0c1bfd27a8b2a5848de3cf4337)
#### Tuesday 2023-12-19 17:05:42 by Colonater

WORKING BACK END HELL YA

please please for the love of god make a branch of this and merge im sick of manuelly merging ur guys

---
## [Yakiyo/aoc-2023](https://github.com/Yakiyo/aoc-2023)@[1aa937354b...](https://github.com/Yakiyo/aoc-2023/commit/1aa937354bc9db57422a69991ac1eeca2cf758d8)
#### Tuesday 2023-12-19 17:31:36 by Yakiyo

fix: use math.min, im fucking stupid to make that idiotic sorting mistake

---
## [Craigspaz/terminal](https://github.com/Craigspaz/terminal)@[86fb9b4478...](https://github.com/Craigspaz/terminal/commit/86fb9b44787accd09c5943a506e27eb4c8e573c0)
#### Tuesday 2023-12-19 17:36:15 by Dustin L. Howett

Add a magic incantation to tell the Store we support Server (#16306)

I find it somewhat silly that (1) this isn't documented anywhere and (2)
installing the "desktop experience" packages for Server doesn't
automatically add support for the `Windows.Desktop` platform...

Oh well.

I'm going to roll this one out via Preview first, because if the store
blows up on it I would rather it not be during Stable roll-out.

---
## [ratatouille100/kernel_samsung_universal9611](https://github.com/ratatouille100/kernel_samsung_universal9611)@[b95fb113c2...](https://github.com/ratatouille100/kernel_samsung_universal9611/commit/b95fb113c254bd00c31a73e3ce39ccb90548cbdc)
#### Tuesday 2023-12-19 17:41:31 by Jason A. Donenfeld

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
## [AysheDaArtist/sojourn-station](https://github.com/AysheDaArtist/sojourn-station)@[3409d0b3ec...](https://github.com/AysheDaArtist/sojourn-station/commit/3409d0b3ec3ac4c5a8e9bd7a0118581c9749ed51)
#### Tuesday 2023-12-19 17:46:02 by benj8560

misc map fixes (#4883)

* map stuff

* small touchup

* stuff!

more minor fixes!

Relocates Ians dinner so it's not hiding away inside a closet where he can't enjoy it assumed unintended. Also returns Runtimes food to her from the old map.

Corrects the micromeds in dorms to using offsets rather then being lodged insdie a wall.

Relocates the Turbine cooling chamber blast door button to the GMs storage room and gives it a atmos ID lock for good mesure. Should keep those trainees away from the funny room.

Adds a sec cam I forgot to the new atmos hard storage room.

Moves poly into the GMs breakroom and gives him a few crackers to eat/grab. The stamp is finally free!

* weh

fixes the missing cables preventing the Terminal Lounge from getting power. You know small lounge near the big shuttle pad for ebents.

* buttttton

adds a button to control the shutter for blackshields maint backdoor

---
## [mosra/magnum-extras](https://github.com/mosra/magnum-extras)@[3333047441...](https://github.com/mosra/magnum-extras/commit/333304744166e0a954cdbad423eb1a3525d1d196)
#### Tuesday 2023-12-19 17:46:15 by Vladimír Vondruš

Whee: rework BaseLayer and TextLayer style assignment.

Requiring the calling code to have a compile-time-sized struct felt like
a good idea in theory. In practice it's absolutely horrendous tho, as:

 - The calling code then has to ensure matching order between a style
   enum and a style struct, which is extremely hard to maintain without
   a nasty preprocessor magic.
 - Defining a builtin style means either having to define & document a
   struct that glues a LayerStyleCommon instance together with several
   LayerStyleItem instances, which is nasty on its own, and then have to
   *somehow* populate it. Which in a (C++11) constexpr context means
   either using the implicit initializer, again losing any mapping from
   the actual enum values to the order (thus gaining *nothing* from such
   a "named tuple" definition), or having to give up on any constexpr
   use and assign to the named fields in order to ensure at least some
   ordering sanity.
 - It's extremely annoying and / or impossible to extend the style
   definition for custom widgets -- one has to *derive a struct* for
   that, and then somehow copy the original builtin data to its prefix.
 - The error message when the layer style count differs from the actual
   passed data is total garbage. Nobody is interested in how many bytes
   something occupies, they want to know *what is wrong* and the API
   isn't capable of saying or even knowing that.

So now it's instead a setStyle() API taking the LayerStyleCommon
instance and a (contiguous) list of LayerStyleItem. A downside is that
the (GL) implementation then does two GL buffer uploads, alternatively
it could put them together and upload at once (which means a nasty temp
allocation). With Vulkan (and I hope WebGPU) this won't be a problem as
there's a way to submit multiple uploads in a single command, or just
memory-mapping the buffer and doing a copy directly.

Extending a style is then a matter of creating an array that's larger
than the compile-time constant, having the custom style items start from
that constant, and copying the original data to prefix of that array.
Simple.

For the TextLayer this also merges the previous setStyle() and
setStyleFonts() APIs together, because they were always meant to be
called together anyway. It makes the whole usage a lot less janky and
unclear.

---
## [ImaginePog/memory-game](https://github.com/ImaginePog/memory-game)@[95f271df43...](https://github.com/ImaginePog/memory-game/commit/95f271df434d5e24cdea02d696115bf1687c6ef1)
#### Tuesday 2023-12-19 18:30:42 by imagine

Use dimensions to get dynamic card sizes

This shits dumb and this components getting bloated
prolly gonna extract gameboard or smth

Also who fucking made CSS hate this shit
Anyways stuff's looking better aile so we take it :)

---
## [Flamefire/pytorch](https://github.com/Flamefire/pytorch)@[a911b4db9d...](https://github.com/Flamefire/pytorch/commit/a911b4db9d82238a1d423e2b4c0a3d700217f0c1)
#### Tuesday 2023-12-19 18:49:46 by voznesenskym

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
## [oskarlundborg/IgnitionOverdrive](https://github.com/oskarlundborg/IgnitionOverdrive)@[2b01fa4144...](https://github.com/oskarlundborg/IgnitionOverdrive/commit/2b01fa4144cf56598d0e98cd5d91a488654ababc)
#### Tuesday 2023-12-19 19:40:39 by Arxhlight

LAST FUCK YOU MATERIAL

FU SO FUCKING HARD YOU FUCKING FUCK TWAT

---
## [oskarlundborg/IgnitionOverdrive](https://github.com/oskarlundborg/IgnitionOverdrive)@[696a4e5160...](https://github.com/oskarlundborg/IgnitionOverdrive/commit/696a4e5160119acf5399df2b8d63112e68d45489)
#### Tuesday 2023-12-19 19:41:14 by Arxhlight

Merge pull request #398 from oskarlundborg/Philip_Beta

LAST FUCK YOU MATERIAL

---
## [robertmeta/crawl](https://github.com/robertmeta/crawl)@[1e143483b6...](https://github.com/robertmeta/crawl/commit/1e143483b6627f70fcabc2f6040ccbc6713882da)
#### Tuesday 2023-12-19 19:44:56 by Skrybe

Xom-themed vaults (#2616)

[The first:] Inspired by the Xom worshiping daevas that can generate in
the Abyss. Contains daevas that call on Xom to smite the player, dancing
holy weapons, and chaos effects through apocalypse crabs and chaos
weapons wielded by the angels and daevas.  Some angels that bored Xom
have been turned to holy swine.

[The other:] Undead Xom worshipers have built a deep shrine (or maybe
they just took over a temple to Yred/Kiku?). Some of the followers are
wielding chaos weapons, a few dancing draining weapons are wielding
themselves, and cacodemons will provide plenty of opportunity for
hilarious mutations. The temple is led by mummified Xom priests
in the back.

[Committer's note: Cleaned up both headers heavily. Minorly nerfed the
Abyss vault. Converted the Crypt end into a regular D + Depths vault and
heavily lowered its derived undead / skeletal warrior spam, leaning more
on regular D + Depths chaos + demons (and some MuCks), and with a touch
of Xom's standard messy decor. Even when taking out the wide number of
demons harmless by depth, I'm ruling out cacodemons and chaos brand being
a noticeable part of the broad and notably focused Crypt end sets. D and
Depths have chaotic / demonic monsters and undead themes plenty to cover
for the union, and we could do a lot more with juxtaposition in bigger
vault themes anyway.]

---
## [Birdtalon/cmss13](https://github.com/Birdtalon/cmss13)@[5d957ce94e...](https://github.com/Birdtalon/cmss13/commit/5d957ce94e398a102fdf16682b740e96df3e363e)
#### Tuesday 2023-12-19 20:24:21 by InsaneRed

Vanguard tweaks (#5174)

# About the pull request
This catches up vanguard to current gameplay as it was last changed
approximately 4 years ago


# Explain why it's good for the game
Currently Vanguard is supposed to be a frontlining tier 3 who dashes in
> stays in and gets some damage in and goes out (thats why the shield is
a thing) and you're supposed to be able to stay there because your
abilities (pierce and dash) resets your shield. But with the recent
addition of just more damage in general be it m56d, full auto mode or
just the amnout of extra damage you can receive from the front compared
4 years ago.

The strain currently struggles and is near useless other then the
occasional go in and lucky fling.

I've changed up the dash to reset your shield once you hit ONE person,
rather then two so that you dont instantly die while going in, the
shield is very situational as it will most likely decay before you can
even go in.

Listening to people who play vanguard, i've also increased the root to
2.5 seconds (this is buffed so when the prae has the shield) the marine
can still shoot back when they're rooted so i dont think the duration is
a big problem (this is going to be a test merge so i will be watching)

# Testing Photographs and Procedure
it just works

</details>


# Changelog

:cl:
balance: Vanguard dash now restores your shield if you hit ANYONE
instead of 2 people.
balance: Vanguard buffed root now roots you for 2.5 seconds, unbuffed
for 1 second
qol: Vanguard's pierce has now a hit sound for better feedback
/:cl:

---------

Co-authored-by: InsaneRed <prodexter31@outlook.comm>

---
## [Ua-Gi-Oh/UA_EDO](https://github.com/Ua-Gi-Oh/UA_EDO)@[a66446d50d...](https://github.com/Ua-Gi-Oh/UA_EDO/commit/a66446d50dd571bade99fef43872ee62eb3c5ae3)
#### Tuesday 2023-12-19 20:27:45 by Ua-Gi-Oh

Перекладені карти 

1 - Substitoad
2 - Amphibious Swarmship Amblowhale
3 - Morphtronic Rusty Engine
4 - Pilgrim of the Ice Barrier
5 - Metaphys Factor
6 - Icy Crevasse
7, 8 - Elemental HERO Sparkman
9 - Disarmament
10 - Bye Bye Damage
11 - Magical Musket - Desperado
12 - Berry Magician Girl
13 - Mask of Dispel
14 - Zefraxa, Flame Beast of the Nekroz
15 - Rock Bombardment
16 - Number C103: Ragnafinity
17 - Salamangreat Gift
18 - Tricular
19 - Virtual World Oto-Hime - Toutou
20 - Spirit Converter

---
## [Addust/Yogstation](https://github.com/Addust/Yogstation)@[5c140d7624...](https://github.com/Addust/Yogstation/commit/5c140d7624b7b9f904d5bd78602d2fb0ee33a9ec)
#### Tuesday 2023-12-19 20:30:36 by Aquizit

[ICEMETA] Fixes Hermit and Walker Spawns (Walkers disabled in config see PR text) (#21065)

* name + config fixes

* fix walker - disabled, redo hermit flavor text

* fuck your stupid uncapitalized t

---
## [Ghommie/tgstation](https://github.com/Ghommie/tgstation)@[2631b0b8ef...](https://github.com/Ghommie/tgstation/commit/2631b0b8ef1a85c75500916215fae69477784558)
#### Tuesday 2023-12-19 20:54:22 by Jeremiah

Replaces prettierx with the normal prettier (#80189)

## About The Pull Request
Oh god the file diff... I'm so, so sorry.

No need to worry though. This just replaces the prettierx version that
we were using and replaces it with normal prettier. Most of the settings
were default or no longer valid with this version.
## Why It's Good For The Game
You no longer get this warning #70484

It actually drives me up the wall and I have to click it each time I
open my editor.
## Changelog
N/A nothing player facing

---
## [Arkatos1/tgstation](https://github.com/Arkatos1/tgstation)@[d751e1c642...](https://github.com/Arkatos1/tgstation/commit/d751e1c64246612f02089bc4059f3dc686edad2a)
#### Tuesday 2023-12-19 21:12:33 by DaCoolBoss

Adds garbage dumpster ruins (#79446)

## About The Pull Request
Adds 4 small space ruins. Each is a dumpster in space containing hostile
mobs to fight and items to bring back to the station. There's a
decommissioned garbage truck pulling each dumpster which acts as a
staging area before you take on the mobs inside.
All the fights are in cramped dark areas with full pressure, air is
breathable but sometimes has miasma in it so beware of getting sick. So
you can drop your space suit and put on armour, but PKAs won't fire at
full power and keeping a gas mask on is recommended.
Also all the dumpsters look the same from the outside so you gotta crawl
inside to know what's inside. And no you can't metagame it with mesons
either.

Comes in the following flavours:
Food Waste
Full of trash from kitchens, and food. Some of the food is still edible.
There's a lot of territorial rats. You can chop them up into meat if you
want more food. The big prize is a big vat of cooking oil.

Medical Waste
Spare organs, cyberorgans and almost a full set of old surgical gear.
There's a syndicate agent here up to no good and he has a GUN. The gun
blows up when the agent dies so you can't get it. There's a few corpses
of different species in bodybags and some spare corpse parts so you can
bring them back to the station and give them to the coroner. Also a
single use eyestealer in a safe (the cool way to do surgery) and a bug
from the old traitor objective that doesn't do jack but can probably
still get you thrown in perma.

Construction Garbage
Tools and construction materials here, including a cool hammer that fits
in a tool belt and can function as a crowbar. There's also a drug lab
with plenty of weird pills to eat, cigarettes to eat and an angry
russian drug dealer who will stab you if he sees you. He has a badass
lighter and a flamethrower you can take after you kill him. Setting fire
to things in here is not recommended because of all the welding fuel.

Mall Trash
Action figures, trading cards, Christmas crackers and other trash the
local mall tossed out. Also a mothman used to live here but he got eaten
by giant spiders so you can grab his stuff, including snacks and a
civilian modsuit with no mods (wow). You can cut through the webs to
kill the spiders or let them eat you too if you want.
## Why It's Good For The Game
More content for space explorers.
More variety to the potential dangers of space, now u can get sick and
die or get eaten by rats (this is hobo RP)
Better environmental storytelling. Now instead of players left asking
"what happens to the garbage when it goes into space" they can rest
assured that there's busted ass garbage trucks in space. All their
questions are answered.
Loot that encourages working with people on the station. Raw food for
the kitchen, rats for genetics, organs for the coroner, etc
## Changelog
:cl:
add: 4 new space ruins
/:cl:

---
## [FrankerFaceZ/FrankerFaceZ](https://github.com/FrankerFaceZ/FrankerFaceZ)@[6e78fd7cab...](https://github.com/FrankerFaceZ/FrankerFaceZ/commit/6e78fd7caba59e4237853257e2006973c7e3c4ab)
#### Tuesday 2023-12-19 21:25:28 by SirStendec

4.64.0

This update adds a check that forces users to agree to YouTube's Terms of Service before they are able to view rich embeds for YouTube links. I personally do not agree with this, but we were required to implement this in order to maintain access to YouTube's API. Actually, they said "API Clients must state in their own terms of use that, by using those API Clients, users are agreeing to be bound by the YouTube Terms of Service." but that's obviously ridiculous for this use case. This is my compromise. Sorry for the inconvenience, everyone. This also comes with aesthetic tweaks to make YouTube's compliance team happy. Woo...

* Added: Setting to display labels on highlighted chat messages giving the reason why the message was highlighted.
* Added: System to force users to agree to a service's Terms of Service before displaying rich content from specific providers. So far this is only used by YouTube.
* Changed: Made the background of highlighted words in chat messages slightly smaller.
* Fixed: A few page elements in mod view not being themed correctly.
* Fixed: Timestamps displaying with an hour when they obviously do not need to.
* API Added: `main_menu:open` event for a general way to open the main menu.
* API Added: Settings UI elements using components using the `provider-mixin` can now override the provider key they use by setting an `override_setting` value on their definition.
* API Changed: The `chat.addHighlightReason(key, data, label)` method now takes an optional `label` parameter to set the text that appears on chat messages when the setting to display labels is enabled.

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[b7b0932c4b...](https://github.com/lessthnthree/tgstation/commit/b7b0932c4b5b3d4f9386b6dce514ee1ba3e25a05)
#### Tuesday 2023-12-19 21:52:11 by distributivgesetz

Delamination variants are now locked in after the countdown is reached (#80324)

## About The Pull Request

Does what it says on the tin.
## Why It's Good For The Game

This effectively changes one and only one thing: 

The "All Within Theoretical Limits" achievement is easier/fairer to get
with this. Previously, if you edged a crystal with the gas composition
method to get a resonance cascade, you had to make sure that your gas
composition stayed until it left the explosion point, which made the
achievement extremely finnicky and unfun to get this way. Regular
delaminations won't really be affected, because yeah. It's at the
explosion point. What are you going to do about it?

This makes the achievement easier to cheese, but honestly, in my opinion
as person who added the achievement, meh. If people feel like this isn't
good for the achievement, say something in the comments.

Closes #79528

## Changelog
:cl:
balance: Delamination variants no longer change once the explosion point
has been reached.
/:cl:

---
## [h-lame/advent-of-code](https://github.com/h-lame/advent-of-code)@[24d7c73d99...](https://github.com/h-lame/advent-of-code/commit/24d7c73d997b58d36e72634bfd94890f8ace7fc5)
#### Tuesday 2023-12-19 22:15:59 by Murray Steele

2023 Day 17

Part 1 took longer than I'd have liked because of lots of silly off by one errors.  Crucially, I didn't really write any tests for this one until I was deep in implementation and that caused me a lot of pain.  Along with standard x + y confusion, and n,e,s,w confusion.  I initially started using the `SortedSet` that's now a gem but I think it expects objects to have unique ordering and if an object has the same ordering as something already in the set, it won't add it.  It took me a while to understand this and why I was getting weird results.  Switched to an array that I sort every time.

That's probably the cause of the slowness in my implementation - it took ~17mins to solve Part 1.

Part 2 didn't take too long to augment to understand the new movement constraints, but it took 2hrs to run, so I had to leave it overnight.  Definitely should have tried to optimise insertion to avoid sorting.

---
## [flutterdro/BattleSimulator](https://github.com/flutterdro/BattleSimulator)@[f8312585f1...](https://github.com/flutterdro/BattleSimulator/commit/f8312585f197f7a4dcfeada492d8b1539193293e)
#### Tuesday 2023-12-19 22:34:06 by Rostyslav

FUCK THIS TASK, I HATE IT SO FUCKING MUCH, I DONT NEED THIS SHIT, I JUST WANT TO TAKE A REST

---
## [alexbaden/llvm-project](https://github.com/alexbaden/llvm-project)@[67daacbdc2...](https://github.com/alexbaden/llvm-project/commit/67daacbdc26c0fd73881b2327ce65e0d84ae5499)
#### Tuesday 2023-12-19 22:59:11 by Douglas Gregor

If we encounter a friend class template for which we cannot resolve
the nested-name-specifier (e.g., because it is dependent), do not
error even though we can't represent it in the AST at this point.

This is a horrible, horrible hack. The actual feature we still need to
implement (for C++98!) is covered by PR12292. However, we used to
silently accept this code, so when we recently started rejecting it we
caused some regressions (e.g., <rdar://problem/11147355>). This hack
brings us back to the passable-but-not-good state we had previously.

llvm-svn: 153752

---
## [crawl/crawl](https://github.com/crawl/crawl)@[669487a9a5...](https://github.com/crawl/crawl/commit/669487a9a525f5f27f84f9cdecce6a169c2510da)
#### Tuesday 2023-12-19 23:11:38 by DracoOmega

Shuffle spellbooks a bunch

The book of Changes was incredibly sad (and nonsensically named) with just
Sting and Irradiate, and attempting to touch this up caused a chain
reaction (which hopefully still improves the status quo).

Unrestrained Analects loses Ignition and gains Ozocubu's Refrigeration.

Book of Battle returns, with Ozocubu's Armour, Manifold Assault, and
Fugue of the Fallen.

Book of Changes renamed to Book of Spontaneous Combustion, containing
Inner Flame, Irradiate, and Ignition.

Book of Alchemy renamed to the book of Transmutation (but contains the
same spells as before).

Book of Minor Magic lost Mephitic Cloud and gained Blink.

Book of the Senses gained Mephitic Cloud.

Book of Blood gained Call Imp (since apparently there was only one book
that had a copy of it)

Book of Cantrips gains Sting.

Book of Death loses Fugue of the Fallen.

Book of Misfortune loses Inner Flame to gain Jinxbite.

Book of Danerous Friends loses Jinxbite.

Ozocubu's Autobiography and the Inescapable Atlas were cut. The latter's
description didn't really make any flavor sense with its spell set of Blink
and Manifold Assault. It's a shame to lose two of the best book
descriptions, so I adapted most of the former for Book of Battle.

Trismegistus Codex loses the joke about all its spells having 3 schools,
but the only other 3 school spell remaining is Mephitic Cloud which already
shares another book with Freezing Cloud. Alas.

---
## [alexbaden/llvm-project](https://github.com/alexbaden/llvm-project)@[7664127f8c...](https://github.com/alexbaden/llvm-project/commit/7664127f8c949ac3da7003427d87ff4b93e320d2)
#### Tuesday 2023-12-19 23:39:09 by Chandler Carruth

Fix a horrible infloop in value tracking in the face of dead code.

Amazingly, we just never triggered this without:
1) Moving code around for MetadataTracking so that a certain *different*
   amount of inlining occurs in the per-TU compile step.
2) Then you LTO opt or clang with a bootstrap, and get inlining, loop
   opts, and GVN line up everything *just* right.

I don't really know how we didn't hit this before. We really need to be
fuzz testing stuff, it shouldn't be hard to trigger. I'm working on
crafting a reduced nice test case, and will submit that when I have it,
but I want to get LTO build bots going again.

llvm-svn: 256735

---
## [bricooke/aoc-in-swift](https://github.com/bricooke/aoc-in-swift)@[f7060707c8...](https://github.com/bricooke/aoc-in-swift/commit/f7060707c84396ff1a49e8ff2054eb4fdad9770e)
#### Tuesday 2023-12-19 23:42:52 by Brian Cooke

day17; needed hints but mostly fought with myself

my min heap implementation had a silly bug where I forgot to move the last item, move it to the top and then heapify that down when popping :facepalm: I was just heapifying down the new 0th item which of course isn't what it needed.

anyway, this works, but is surprisingly slow. I didn't profile it but I'm guessing its my heap impl.

---
## [alexbaden/llvm-project](https://github.com/alexbaden/llvm-project)@[8882346842...](https://github.com/alexbaden/llvm-project/commit/88823468420e652918cbf13f420d885bacd67681)
#### Tuesday 2023-12-19 23:47:38 by Chandler Carruth

[PM] Introduce basic update capabilities to the new PM's CGSCC pass
manager, including both plumbing and logic to handle function pass
updates.

There are three fundamentally tied changes here:
1) Plumbing *some* mechanism for updating the CGSCC pass manager as the
   CG changes while passes are running.
2) Changing the CGSCC pass manager infrastructure to have support for
   the underlying graph to mutate mid-pass run.
3) Actually updating the CG after function passes run.

I can separate them if necessary, but I think its really useful to have
them together as the needs of #3 drove #2, and that in turn drove #1.

The plumbing technique is to extend the "run" method signature with
extra arguments. We provide the call graph that intrinsically is
available as it is the basis of the pass manager's IR units, and an
output parameter that records the results of updating the call graph
during an SCC passes's run. Note that "...UpdateResult" isn't a *great*
name here... suggestions very welcome.

I tried a pretty frustrating number of different data structures and such
for the innards of the update result. Every other one failed for one
reason or another. Sometimes I just couldn't keep the layers of
complexity right in my head. The thing that really worked was to just
directly provide access to the underlying structures used to walk the
call graph so that their updates could be informed by the *particular*
nature of the change to the graph.

The technique for how to make the pass management infrastructure cope
with mutating graphs was also something that took a really, really large
number of iterations to get to a place where I was happy. Here are some
of the considerations that drove the design:

- We operate at three levels within the infrastructure: RefSCC, SCC, and
  Node. In each case, we are working bottom up and so we want to
  continue to iterate on the "lowest" node as the graph changes. Look at
  how we iterate over nodes in an SCC running function passes as those
  function passes mutate the CG. We continue to iterate on the "lowest"
  SCC, which is the one that continues to contain the function just
  processed.

- The call graph structure re-uses SCCs (and RefSCCs) during mutation
  events for the *highest* entry in the resulting new subgraph, not the
  lowest. This means that it is necessary to continually update the
  current SCC or RefSCC as it shifts. This is really surprising and
  subtle, and took a long time for me to work out. I actually tried
  changing the call graph to provide the opposite behavior, and it
  breaks *EVERYTHING*. The graph update algorithms are really deeply
  tied to this particualr pattern.

- When SCCs or RefSCCs are split apart and refined and we continually
  re-pin our processing to the bottom one in the subgraph, we need to
  enqueue the newly formed SCCs and RefSCCs for subsequent processing.
  Queuing them presents a few challenges:
  1) SCCs and RefSCCs use wildly different iteration strategies at
     a high level. We end up needing to converge them on worklist
     approaches that can be extended in order to be able to handle the
     mutations.
  2) The order of the enqueuing need to remain bottom-up post-order so
     that we don't get surprising order of visitation for things like
     the inliner.
  3) We need the worklists to have set semantics so we don't duplicate
     things endlessly. We don't need a *persistent* set though because
     we always keep processing the bottom node!!!! This is super, super
     surprising to me and took a long time to convince myself this is
     correct, but I'm pretty sure it is... Once we sink down to the
     bottom node, we can't re-split out the same node in any way, and
     the postorder of the current queue is fixed and unchanging.
  4) We need to make sure that the "current" SCC or RefSCC actually gets
     enqueued here such that we re-visit it because we continue
     processing a *new*, *bottom* SCC/RefSCC.

- We also need the ability to *skip* SCCs and RefSCCs that get merged
  into a larger component. We even need the ability to skip *nodes* from
  an SCC that are no longer part of that SCC.

This led to the design you see in the patch which uses SetVector-based
worklists. The RefSCC worklist is always empty until an update occurs
and is just used to handle those RefSCCs created by updates as the
others don't even exist yet and are formed on-demand during the
bottom-up walk. The SCC worklist is pre-populated from the RefSCC, and
we push new SCCs onto it and blacklist existing SCCs on it to get the
desired processing.

We then *directly* update these when updating the call graph as I was
never able to find a satisfactory abstraction around the update
strategy.

Finally, we need to compute the updates for function passes. This is
mostly used as an initial customer of all the update mechanisms to drive
their design to at least cover some real set of use cases. There are
a bunch of interesting things that came out of doing this:

- It is really nice to do this a function at a time because that
  function is likely hot in the cache. This means we want even the
  function pass adaptor to support online updates to the call graph!

- To update the call graph after arbitrary function pass mutations is
  quite hard. We have to build a fairly comprehensive set of
  data structures and then process them. Fortunately, some of this code
  is related to the code for building the cal graph in the first place.
  Unfortunately, very little of it makes any sense to share because the
  nature of what we're doing is so very different. I've factored out the
  one part that made sense at least.

- We need to transfer these updates into the various structures for the
  CGSCC pass manager. Once those were more sanely worked out, this
  became relatively easier. But some of those needs necessitated changes
  to the LazyCallGraph interface to make it significantly easier to
  extract the changed SCCs from an update operation.

- We also need to update the CGSCC analysis manager as the shape of the
  graph changes. When an SCC is merged away we need to clear analyses
  associated with it from the analysis manager which we didn't have
  support for in the analysis manager infrsatructure. New SCCs are easy!
  But then we have the case that the original SCC has its shape changed
  but remains in the call graph. There we need to *invalidate* the
  analyses associated with it.

- We also need to invalidate analyses after we *finish* processing an
  SCC. But the analyses we need to invalidate here are *only those for
  the newly updated SCC*!!! Because we only continue processing the
  bottom SCC, if we split SCCs apart the original one gets invalidated
  once when its shape changes and is not processed farther so its
  analyses will be correct. It is the bottom SCC which continues being
  processed and needs to have the "normal" invalidation done based on
  the preserved analyses set.

All of this is mostly background and context for the changes here.

Many thanks to all the reviewers who helped here. Especially Sanjoy who
caught several interesting bugs in the graph algorithms, David, Sean,
and others who all helped with feedback.

Differential Revision: http://reviews.llvm.org/D21464

llvm-svn: 279618

---

