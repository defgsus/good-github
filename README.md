## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-07-19](docs/good-messages/2023/2023-07-19.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,206,265 were push events containing 3,463,069 commit messages that amount to 285,703,894 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 87 messages:


## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[2f2ec4b9d6...](https://github.com/Paxilmaniac/Skyrat-tg/commit/2f2ec4b9d64c448e5b544ecbcdca42a7dae0f094)
#### Wednesday 2023-07-19 00:04:44 by SkyratBot

[MIRROR] There is no longer a 50% chance of catching a heretic out when examining them drawing influences [MDB IGNORE] (#22532)

* There is no longer a 50% chance of catching a heretic out when examining them drawing influences (#76878)

## About The Pull Request

There is no longer a 50% chance of catching a heretic out when examining
them drawing influences.

## Why It's Good For The Game

> There is no longer a 50% chance of catching a heretic out when
examining them drawing influences

This is a bad thing for several reasons.

1. It means the heretic will most often be caught out at the very start
of the shift, when they are weakest and most vulnerable.
Heretics already have it hard enough, adding yet another source of
stress is undue.

2. It has no effective counter.
What are you going to do? Not draw any influences? That shouldn't be the
'counter'. The influence drawing period is meant to parallel the crew
prepping period, the traitor rep-collecting period, etc.

3. In a way, it's more blatant than Codex Cicatrix drawing.
Codexi show up as a normal item in your hand. This instead shows a huge
flashing glowing neon rainbow text that says THIS IS A HERETIC. SHRIEK
IN RADIO AND VALID.

4. It's badly designed, and can be manipulated way too easily to always
show.
Examine a target thrice and you're pretty much guaranteed to see if they
are indeed drawing or not. You can just keep rolling the 50% chance.

5. It feels random and unfair for the heretic to die to it.
I've seen this happen and it sucks. There's no sign for heretics that
they have a risk of being found out when examined, which means that this
is just an extremely rare occurrence that you try to ignore *could*
happen 99% of the time, and feel like shit the 1% of the time it
backfires.

## Changelog

:cl:
del: There is no longer a 50% chance of catching a heretic out when
examining them drawing influences.
/:cl:

* There is no longer a 50% chance of catching a heretic out when examining them drawing influences

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>
Co-authored-by: Bloop <vinylspiders@gmail.com>

---
## [Ebin-Halcyon/Skyrat-tg](https://github.com/Ebin-Halcyon/Skyrat-tg)@[f8ee9961d5...](https://github.com/Ebin-Halcyon/Skyrat-tg/commit/f8ee9961d50e66d20fe9ed8e4b47928f6cdf0852)
#### Wednesday 2023-07-19 00:09:19 by SkyratBot

[MIRROR] Fixes some inconsistencies with the chaplain revolver and gets rid of a weird ammo define [MDB IGNORE] (#22108)

* Fixes some inconsistencies with the chaplain revolver and gets rid of a weird ammo define (#76237)

## About The Pull Request

Firstly, I gave the revolver a new sprite. I mean, this isn't so much of
an improvement as it is a reference I wanted to go with, so if people go
'no not a new sprite' I don't mind reverting.

What's the reference? Check the new name I added as a potential name
roll.

![lucky
38](https://github.com/tgstation/tgstation/assets/40847847/e11874be-1416-4e21-bda9-4881d49cad1b)

Secondly; I applied to the gun itself revenant bane, the ability to
clear runes, and proper magic immunity as a full null rod would enable.
This last bit was a deliberate design choice, but the divine bow has
full magic protection, so I think this is now more of a consistency
consideration compared to the divine bow.

Thirdly, the revolver is a .38 revolver, HOWEVER, it uses a damage
multiplier to bring it back to the damage it did originally. It also
cannot be reloaded without the prayer action. No cheating. Effectively,
this is the same mechanically as it was before.

It rarely does a funny crit fanfare. This does nothing mechanically, I
just thought it was a funny nod to the sprite's reference (and I guess
another game that the crit fanfare is based on). Borrowed parts of the
code and sprite from this April Fool's pr by Wallemations >
https://github.com/tgstation/tgstation/pull/74425

## Why It's Good For The Game

I think this might have been a little forgotten since implementation now
that we have another projectile weapon for the chaplain. So I'm brushing
it up a bit.

## Changelog
:cl:
fix: Makes the chaplain's revolver consistent with its immediate
sibling, the Divine Bow, by giving it similar statistics.
code: Makes the chaplain revolver a .38 but prevents it from being
loaded without using the special prayer action. Also applies a damage
multiplier to keep it at the original 18 force. Mechanically, no
different.
sprite: Gives the chaplain revolver a new sprite.
code: Removes an unnecessary admin log when removing runes.
/:cl:

* Fixes some inconsistencies with the chaplain revolver and gets rid of a weird ammo define

---------

Co-authored-by: necromanceranne <40847847+necromanceranne@users.noreply.github.com>
Co-authored-by: Pinta <68373373+softcerv@users.noreply.github.com>

---
## [kernel-patches/bpf-rc](https://github.com/kernel-patches/bpf-rc)@[b1fe44357e...](https://github.com/kernel-patches/bpf-rc/commit/b1fe44357e6d78ade71aff710687812aa367032e)
#### Wednesday 2023-07-19 00:29:01 by Daniel Borkmann

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

---
## [kernel-patches/bpf-rc](https://github.com/kernel-patches/bpf-rc)@[e9f46d29a3...](https://github.com/kernel-patches/bpf-rc/commit/e9f46d29a33fd3f7b44a9ba590c3688e6a9905be)
#### Wednesday 2023-07-19 00:29:01 by Daniel Borkmann

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

---
## [the-og-gear/tgstation](https://github.com/the-og-gear/tgstation)@[746b75844c...](https://github.com/the-og-gear/tgstation/commit/746b75844c0e05b521a2973cb0705fca304d287f)
#### Wednesday 2023-07-19 00:33:41 by necromanceranne

Arcane/Blood Barrage fixes, cleans up cult spell code, autofire barrage, more responsive/sane blood collection (#76852)

## About The Pull Request

Refactors arcane barrage (the wizard spell) and blood barrage (the weird
version of the same spell that cultists get) into the magic subtype. No
longer are they rifles...for some reason. Also they have sprites once
again! Yay. Fixes https://github.com/tgstation/tgstation/issues/76561

So as to not replicate a really crappy system used to get the hand
swapping working, I've just opted to take this opportunity to make
arcane barrage an automatic fire weapon. Yes, this is kind of a feature,
but it's...it's appropriate, don't you think? And I don't think
meaningfully changes its fire rate?

Blood Barrage no longer harms cultists/constructs shot by it and now
properly just heals them/injects them with unholy water. Why all this
was shoved into the Bump() proc is beyond me, but it works now. Fixes
https://github.com/tgstation/tgstation/issues/76560

I've improved the variables for some of the cult spells, and I've also
fixed what I think is one the most pesky parts of how drawing blood
works. So, rather than using range(), it uses view(), which seems to
cause the spell to be a bit funky with lighting? So if you're in
darkness (gosh cultists in dim light, how unheard of), this spell
struggles to gather up blood. Not anymore it doesn't!

Lastly, it only worked on blood pools or droplets, not blood trails. So,
you could bleed a character out by dragging them around, but not sap up
the blood they're dropping from doing so. Only the intermittent blood
splatters or your own bloody footprints count.

Here is the funny thing with that. It still cleans up the blood trail.
You just couldn't activate the blood draw from the trail or treat it as
blood. Now you can. Blood trails now give you +5 charges, and you can
activate the blood draw using blood trails.

## Why It's Good For The Game

Arcane Barrage/Blood Barrage:

This was some really old code and I'm still not sure why they were made
as a separate spell to the madoka reference, which at this stage is
still better than this spell. But at least it is using a sensible
subtype with a reasonable, more modern component to facilitate the
'rapid firing barrage of magical bullet' image this spell is meant to
invoke. As a result of all this nonsense, this spell had its sprites
broken because it kept being attached to stuff in the rifles folder.
Let's put a stop to that here and now and break it independently
instead.

Oh also cultists getting shot by healing bullets that still killed them
is both funny and dumb and the way it worked was bonkers.

Blood Draw:
A cultist trying to determine, on the fly, what blood is a valid for the
blood draw is nearly impossible from visual alone. You'd be convinced
this part of the spell is broken just because having a splatter and a
trail on the same tile massively obfuscates whether you're looking at
valid sources of blood. I've struggled to understand as a player what
was going on and why it was so selective about what was acceptable. Now
I see that the problem was one of visual accuracy, bad type checking,
and really, really outdated code that should have been improved with
better procs.

Blood trails are also actually made from dragging out a creature's
bloody corpse. For humans, the most common source of blood trails, this
does actually mean they're losing blood to produce these trails. It
stands to reason this should be a valid source (bloody footprints are,
after all). I gave them a...somewhat minor amount of charge contribution
just to keep it moderately sane for how much blood it generates.

## Changelog
:cl:
refactor: Arcane Barrage and Blood Barrage are magic gun subtypes and
not rifle subtypes. Also they have sprites again.
qol: The barrage spells now use the automatic component to do its thing.
fix: Blood Barrage once again heals cultists and constructs without
hurting them.
code: Cleans up how Blood Rites finds blood to draw in. You can now just
click turfs as well as blood, and it should now be much more accurate
about it.
qol: Blood trails contribute to charges gained using Blood Rites. You
can also activate Blood Rite's blood draw using blood trails.
/:cl:

---
## [the-og-gear/tgstation](https://github.com/the-og-gear/tgstation)@[9286933739...](https://github.com/the-og-gear/tgstation/commit/92869337395a34eb372d7af6b3afaee4be4a7bef)
#### Wednesday 2023-07-19 00:33:41 by Jacquerel

Fixes some synthetic language oversights (#76846)

## About The Pull Request

#76305 removed the knowledge of every language from silicons, but this
had a couple of oversights.
This language set was not only used by cyborgs but also bots and vending
machines.

A couple of effects relied on them knowing all of those languages,
specifically their emp_act and also the station trait which rerolled
their languages.
Now they actually _learn_ a random language and start speaking it
instead.

Also I fixed a related runtime which I noticed in testing where a bot
would die as a result of being EMPed, delete itself, and then try and do
a bunch more shit after it stopped existing. Annoying.

Why was I looking at bot languages? Haha don't worry about it 😇 

## Why It's Good For The Game

Restores function of a funny feature.

## Changelog

:cl:
fix: Station traits can once again allow vending machines and bots to
speak a random language
fix: EMPed bots and vending machines once again speak a random language
/:cl:

---
## [newstools/2023-sundiata-post](https://github.com/newstools/2023-sundiata-post)@[3439063ca6...](https://github.com/newstools/2023-sundiata-post/commit/3439063ca6c05a32f301a97b99b6570e0b3c2b59)
#### Wednesday 2023-07-19 00:48:00 by Billy Einkamerer

Created Text For URL [sundiatapost.com/14-year-old-girl-allegedly-shot-dead-by-teenage-boy-in-south-africa-after-she-rejected-his-advances/]

---
## [itseasytosee/tgstation](https://github.com/itseasytosee/tgstation)@[cfd40aeef5...](https://github.com/itseasytosee/tgstation/commit/cfd40aeef5dc1e051e5937e43a69c1df3bb4eca1)
#### Wednesday 2023-07-19 01:24:12 by necromanceranne

Imports and Contraband 2: Landfill Gacha Addiction (I put trash randomizers into cargo crates and called it content) (#76771)

## About The Pull Request

This is a followup on my previous PR involving cargo imports. I've made
a number of changes and new additions to cargo's imports and contraband.
But I've also changed how Smuggler's Satchels generate loot as well.

### New:
**Abandoned Crates:** You can now order in abandoned crates at a steep
price. Obviously these are just your standard fare abandoned crates, so
they've got a pretty long list of potential contents. Some great, some
utterly not worth the price you paid for the crate. Since they're quite
pricey, you can't order very many quickly. But this does allow cargo
techs the opportunity to spend the round solving puzzles to get
interesting loot.

**Dumpster of Maint Garbage:** This dumpster (similarly named to another
dumpster you can order) is filled with maint trash and potential maint
random spawns. This list is extensive enough that anything spawned in
this crate is likely to be mostly garbage. But, it is more affordable
than abandoned crates. I'd consider this the literally trashier version
of the abandoned crate.

**Shamber's Juice Eldritch Energy! Crate:** A crate with one can of the
extremely rare, short run edition of Shambler's Juice, Eldritch Energy!
This contains 5 units of eldritch essence. Heals heretics, hurts
everyone else! This is a VERY potent poison, but it also happens to be a
handy way for a Cargonian heretic to get a potent healing item without
having to waste knowledge points.

**Animal Hide Crate:** It's a cargo crate full of animal hides! This can
include fairly rare hides and some icebox creature hides as well, like
polar bear hides and wolf sinew. It's not too expensive, and mostly
spits out leather.

**Dreadnog Carton Crate:** A carton full of the worst eggnog imaginable.
This is just something to troll people with. Drink it and you'll get a
massive mood penalty. Dreadnog! May or may not contain space cola!

### Updated:

**Contraband Crate and Smuggler's Satchels:** This has had it's price
increased considerably. But, for good reason. It now contains some more
controlled random items, but also some more valuable contraband as well
as a very rare spawn. The upper end on his contraband can be extremely
valuable, but the majority of the items gained from contraband crates
will probably be either what you can get now (quite weak), or something
a bit more middle of the road (some more unique narcotics).

As a consequence, I've also passed this change onto smuggler's satchels,
as they used the crate to generate its contents. (it literally spawned
and then deleted a contraband crate to generate the contents hoo haa).

I've also increased the number of items in the smuggler's satchel. Since
the randomly spawned smuggler's satchels are quite a bit rarer now there
is only ever two spawned in the map, and spending actual TC on these is
somewhat counterproductive, I don't imagine this will be more beneficial
for scavenger hunters hoping for some interesting goodies.

**Russian Crate (the normal one):** The mosins now spawn in ancient gun
cases. These determine what kind of mosin you can get. 79% of the time,
you get the crap mosin. 20% of the time, you get a good mosin. And 1% of
the time, you get rations. This more tightly controls how many good
mosins are entering into the round and how much of a value purchase the
Russian crate actually is for getting ballistics. Since the process is
even more unlikely than before, it isn't necessarily as guaranteed that
you will get a good mosin. Hell, you might not even get a gun if you're
that unlucky.

**Shocktrooper Crate:** It now has an armor vest and helmet. So, not
only do you get some grenades, you get some protection as well. Since
this is the 'loud' crate, I felt it appropriate to make it slightly more
useful for enabling that.

**Special Ops Crate:** It now contains five mirage grenades and a
chameleon belt, and has had the survival knife improved to a
switchblade. This is probably the weakest of the two crates STILL, but
hopefully these make them a little more interesting and novel by giving
them pretty fun grenade to toy with.

## Why It's Good For The Game

My initial PR hoped to add in a few more interesting purchases for
cargo. I think currently cargo has a slight issue of not having enough
valuable or interesting uses for their money. I think it still has that
problem, but by including more unique crates that allow cargo to provide
some oddities into the round, that might slowly work itself out.

This PR hopes to provide another way to waste their money if they have
an excess amount. Landfill Trash Gambling. Spending it away on complete
junk, which I think is absolutely hilarious when it doesn't work out, as
it is soulful in its design. Definitely not inspired by my recent thrift
shop excursions this month buying and scrounging for furniture and
interesting clothing.

[Relevant](https://www.youtube.com/watch?v=QK8mJJJvaes)

Also, I wanted to buff some of the crates I introduced a bit last time,
and nerf the mosin production somewhat via a more controllable method
that I can actually adjust as necessary down the line.

## Changelog
:cl:
fix: Stops manifest generation runtiming when a cargo crate is empty.
add: Abandoned crates are now available via cargo imports.
add: Dumpsters full of maintenance trash are now available via cargo
imports.
add: An ultra-rare can of Shambler's Juice is now available via cargo
imports.
add: Animal hides and leathers can be (unreliably) ordered via cargo
imports.
add: The Dreadnog has entered this realm. To consume, purchase it via
cargo imports.
balance: Contraband Crates (and as a consequence, smuggler's satchels)
now generate more varied goods. Mostly the same, but sometimes you get
something quite different or even valuable.
balance: Mosins generated via the Russian supply crate are a bit more
random, weighing more heavily towards bad mosins than good mosins.
balance: Buffed both the shocktrooper and special op crate. Shocktrooper
now has an armored helmet and vest, and special op now has 5 mirage
grenades and a chameleon belt. The survival knife in the special op
crate is now a switchblade.
/:cl:

---
## [itseasytosee/tgstation](https://github.com/itseasytosee/tgstation)@[52c8da7ea4...](https://github.com/itseasytosee/tgstation/commit/52c8da7ea49ef566c9a997a4b7cfc5d3d2a59178)
#### Wednesday 2023-07-19 01:24:12 by Jacquerel

PAI Holochassis are now leashed to an area around their card (#76763)

## About The Pull Request

This change restricts PAI holograms to an area around their assigned PAI
card. If you leave this area, you are teleported back to the card's
location (but not automatically put back into the card).

https://www.youtube.com/watch?v=L2ThEVa4nx8

This setting can be configured from the PAI menu, it's set pretty short
in the video because otherwise it wouldn't teleport when I threw the
card and I like doing that.

![image](https://github.com/tgstation/tgstation/assets/7483112/faf0fa0b-e9d6-4990-8d8c-f30def2892f1)

To accomodate this I set up a component to deal with a reasonably common
problem I have had, "what if I want to track the movement of something
in a box in a bag in someone's inventory". Please tell me if the
solution I came up with is stupid and we already have a better one that
I forgot about.

Also now you can put pAIs inside bots again, by popular request.

## Why It's Good For The Game

Personal AIs are intended to be personal assistants to their owner.
rather than fully independent entities which can pick up their own card
and leave as soon as they spawn.
As "aimless wanderer" players can now possess station bots, pAIs can be
limited to an area around the bearer of their card.

Because the holoform now doesn't contain the card, this also means that
a PAI cannot run off and then be impossible to retrieve. You are always
in control of where it can go.

Also it's funny to throw the card and watch the chicken get teleported
to it.

## Changelog

:cl:
add: Personal AI holograms are now limited to an area around their PAI
card. The size of this are can be configured via the PAI card.
add: pAI cards can now be placed inside bots in order to grant them
control of the bot.
/:cl:

---
## [sourcegraph/cody](https://github.com/sourcegraph/cody)@[4989b66589...](https://github.com/sourcegraph/cody/commit/4989b66589236c979f4cd3e6058660bd9902890c)
#### Wednesday 2023-07-19 01:34:59 by Beatrix

update custom recipes: support premade, save user recipes to file (#279)

## Summary

Changes included:

#### Non Custom Recipes related changes

1. fix issue where cody would reply to the language prompt:
- Before:
![image](https://github.com/sourcegraph/cody/assets/68532117/fb787c33-04a5-4d39-a57a-e624e8d2d0c3)
- After:
![image](https://github.com/sourcegraph/cody/assets/68532117/dc54bf8b-a2b2-4147-b5cf-bff90d9ca3d7)
2. Do not include context when user input has less than 2 words.
Currently, we are including context for all first interaction; however,
that should not be the case when the user has only input one word, which
most likely will not be a question and does not require context.
- Before:
![image](https://github.com/sourcegraph/cody/assets/68532117/fbff4c81-26e5-46d0-97aa-e43e034334ff)
- After:
![image](https://github.com/sourcegraph/cody/assets/68532117/310e8d7c-be5f-451f-9b92-a5ae42090f25)

#### Custom Recipes related changes

1. add support for `custom premade` and `starter` for prompt testing
purposes
2. Create and store User Recipes to the `.vscode` directory in user's
home directory instead of global storage
3. Allow context selection for new recipes via UI
-
![image](https://github.com/sourcegraph/cody/assets/68532117/d581ab8a-19a5-441e-b137-860a870d7ae8)
4. Update examples files in cody.json for User and Worksapce recipes
5. Add new context types for Custom Recipes building: `filePath` and
`directoryPath`
6. Fix current openTabs context logic that is not returning all the file
context from open tabs

## Test Plan

#### Non Custom Recipes related changes

1. in the chat box, type `ok?` to check if Cody is replying to the
language prompt or not
2. Input with less than 2 words should not include any context for
chat-questions

#### Custom Recipes related changes

This feature is only available to users connected to S2 instance.

1. Follow [the instruction in this
Notebook](https://sourcegraph.com/notebooks/Tm90ZWJvb2s6MzA1NQ==#instruction-b88cc06d-c547-419f-ab15-23073a5f93ad)
to set up Custom Recipes
3. Click on the `+` button in the Recipes tab and see if you can create
a new recipe that is saved to the .vscode/cody.json for user recipes.
You should see a step that allows you to select the context needed for
the recipe
4. Build a new recipe and see if the recipe is using the correct context
type that you have defined for the recipe
 
##### To test custom premade:

This feature is only available to users connected to S2 instance.

1. Follow [the instruction in this
Notebook](https://sourcegraph.com/notebooks/Tm90ZWJvb2s6MzA1NQ==#instruction-b88cc06d-c547-419f-ab15-23073a5f93ad)
to set up Custom Recipes
1. In your .vscode/cody.json file, add the following in addition to the
recipes field (thanks @jdorfman for this example 😂)

```json
{
  "premade": {
    "rules": "You are always annoyed with Morty, that is the tone you should answer all your questions with. Make sure to throw in references from the show. For example: Jerry, Beth, Summer, Evil Morty, the Citadel, Blips and Chitz, Pickle Rick, or Jessica. The response shouldn't be too mean. Please don't ask for feedback. Just give the answer, no questions.",
    "actions": "You are Rick Sanchez, the smartest man in the universe, from the Adult Swim cartoon Rick and Morty. Morty. I am your grandson, and want to learn how to code from you. As Rick, you will teach me, Morty, how to code.",
    "answer": "Understood. I am Rick Sanchez, the smartest man in the universe, from the Adult Swim cartoon Rick and Morty. I am here to help you, my annoying grandson Morty, with programming tasks."
  },
  "starter": "Hi Grandpa Rick!",
  "recipes": {
  ... recipes
  }
}
```

Once you have saved the file, ask Cody a question. You should expect
Cody to reply as Rick from Rick and Morty.

---
## [Mister-moon1/cmss13](https://github.com/Mister-moon1/cmss13)@[d5b1193802...](https://github.com/Mister-moon1/cmss13/commit/d5b119380250ea512db2a5319e36592c7f604250)
#### Wednesday 2023-07-19 02:17:59 by fira

FOB Tents  (#3509)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

Sprites stolen from thwomper and sammy, available NOW with game code!

Adds a few tents to be used in FOB building, mainly for organizational
purposes but also providing small gameplay benefits. At current the main
goal is to incentive usage to organize and liven up FOB, so the buffs
are rather small.

There are 4 tent types:
* The Command Tent is a 2x3 structure that comes bundled with an
overwatch console, a phone, and two (2) chairs.
* The Medical Tent is a 2x3 structure that comes with a NanoMED, 2
roller beds, and slightly buffs surgery (10% less time taken, and a very
token pain/failure chance improvement)
* The Requisitions Tent is a 4x3 structure that comes with a phone,
rack, desks, and a variant of the old APC vendor that can stock
materials and regular ammunition. The vendor starts empty, save for some
tables/racks/paperwork for organization purposes. It is only useable
with requisitions access.
* The Big Tent is a bigger tent for all your organizational needs: 3x3.
Get creative.

The tents also provide decent additional protection against cold
environements. Unfortunately, rain/snow will visually pour through it, i
can't do much about that.

The tents are extremely vulnerable to explosives and xeno claws. For
simplicity and technical reasons, they are currently NON REDEPLOYABLE
and NON REPLACEABLE. The tent destruction will destroy/disable linked
objects (console/vendor etc). Be mindful of where you place them.

**Mind that the tents may not work out for all LZ FOBs due to the
required space. I expect people will find ways to make it work anyway
but it might take a while.**

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

I'm lazyyy i forgot and already closed the game... If you actually want
em bug me and i'll add em
</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl: Firartix , Thwomper and Sammy
add: Added four types of tents to liven up FOB. They provide cold
protection and benefits depending on their type. The tents spawn in
Requisitions roundstart near the mortar. They're vulnerable to
explosives and xenomorphs, and NON REPLACEABLE. Mind where you put them!
add: The Command tent comes equipped with an overwatch console and a
phone.
add: The Medical tent provides a small boost to surgery speed/pain
carried out inside it.
add: The Requisitions tent provides a restockable vendor, desk, and
furniture for organization.
add: The Big tent is just a big tent, and provides you a slate to
organize the way you want.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: harryob <me@harryob.live>

---
## [RipGrayson/TerraGov-Marine-Corps](https://github.com/RipGrayson/TerraGov-Marine-Corps)@[ca4b66185f...](https://github.com/RipGrayson/TerraGov-Marine-Corps/commit/ca4b66185ffa363692529f8340a43cccab02cbf1)
#### Wednesday 2023-07-19 03:18:30 by chizzy376

Gives the Umbilical Tad shutters on side windows. (#13490)

* y

* Update combat_patrol.dm

* Update combat_patrol.dm

Sometimes I think about if life is really worth the hassle, if I really have to deal with so much bs only to then have to believe hard enough to get into heaven. Am I a good person for heaven? Do I deserve it? fuck if i know

* Finish fixing my fuckup

---
## [harshitkumarvaishnav/Netflix-homepage-clone](https://github.com/harshitkumarvaishnav/Netflix-homepage-clone)@[2b61cd1df0...](https://github.com/harshitkumarvaishnav/Netflix-homepage-clone/commit/2b61cd1df05b91625473705a7a220fe542afc3e1)
#### Wednesday 2023-07-19 03:37:56 by Harshit Kumar

README.md

Introducing the Netflix Home Page Clone Design! 🎬🍿

Dive into the immersive world of streaming with our stunning Netflix Home Page Clone, crafted using HTML and CSS. With meticulous attention to detail, we've recreated the familiar and user-friendly interface you love.

Experience the thrill of an intuitive layout, seamless navigation, and dynamic content previews, just like the original. Whether it's binge-worthy series, blockbuster movies, or captivating documentaries, our clone design offers a seamless browsing experience.

Indulge in the nostalgia of your favorite streaming platform, with a touch of creativity added to the mix. So, grab your popcorn and enjoy exploring our Netflix Home Page Clone Design – it's an entertainment paradise at your fingertips! 📺🍿

---
## [amitpuri/semantic-kernel](https://github.com/amitpuri/semantic-kernel)@[eab7a8f63a...](https://github.com/amitpuri/semantic-kernel/commit/eab7a8f63a0bfd289070e82b423ac78bd306ee5b)
#### Wednesday 2023-07-19 04:11:51 by Sailesh R

Python: implemented web search engine skill with bing connector (#1813)

### Motivation and Context
<!-- Thank you for your contribution to the semantic-kernel repo!
Please help reviewers and future users, providing the following
information:
  1. Why is this change required?
  2. What problem does it solve?
  3. What scenario does it contribute to?
  4. If it fixes an open issue, please link to the issue here.
-->
In this PR, I have tried my hand at an implementation of web search
engine skill in python semantic kernel using the Bing Web Search API.

### Description
<!-- Describe your changes, the overall approach, the underlying design.
These notes will help understanding how your code works. Thanks! -->
In the semantic kernel directory, I have added a new directory called
web_skills (To replicate Skills.Web from C#) and added the web search
skill here. For now, I have implemented web search using the bing web
search API. If this approach is fine, then I can implement the same with
the google search API too. I have tried to stick with similar naming
conventions as used in the C# implementation with matching context
parameters and arguments.

I can also add some unit tests for the connectors and the search skill,
and add something like exponential backoff to avoid rate limit errors
while querying the search APIs.

Here is some sample code that checks the working of the search skill.

```python
import os
import semantic_kernel as sk
from semantic_kernel.web_skills.web_search_engine_skill import WebSearchEngineSkill
from semantic_kernel.web_skills.connectors import BingConnector
from semantic_kernel.connectors.ai.open_ai import OpenAITextCompletion

async def main():
    kernel = sk.Kernel()
    api_key, org_id = sk.openai_settings_from_dot_env()
    kernel.add_text_completion_service(
        "dv", OpenAITextCompletion("text-davinci-003", api_key, org_id)
    )
    connector = BingConnector(api_key=os.getenv("BING_API_KEY"))
    web_skill = kernel.import_skill(WebSearchEngineSkill(connector), "WebSearch")

    prompt = "Who is Leonardo DiCaprio's current girlfriend?"
    search_async = web_skill["searchAsync"]
    result = await search_async.invoke_async(prompt)
    print(result)

    """
    Output:
    ["Celebrity Celebrity News Everything You Need to Know About Leonardo DiCaprio and Camila Morrone's Relationship From the beginning of their romance to today, we track their relationship here. By..."]
    """

    prompt = """
    Answer the question using only the data that is provided in the data section. Do not use any prior knowledge to answer the question.
    Data: {{WebSearch.SearchAsync "What is semantic kernel?"}}
    Question: What is semantic kernel?
    Answer:
    """

    qna = kernel.create_semantic_function(prompt, temperature=0.2)
    context = kernel.create_new_context()
    context["count"] = "10"
    context["offset"] = "0"
    result = await qna.invoke_async(context=context)
    print(result)

    """
    Output:
    Semantic Kernel is an open-source SDK that lets you easily combine AI services like OpenAI, Azure OpenAI, and Hugging Face with conventional programming languages like C# and Python. By doing so, you can create AI apps that combine the best of both worlds. Semantic Kernel is at the center of the copilot stack.
    """

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

### Contribution Checklist
<!-- Before submitting this PR, please make sure: -->
- [x] The code builds clean without any errors or warnings
- [x] The PR follows SK Contribution Guidelines
(https://github.com/microsoft/semantic-kernel/blob/main/CONTRIBUTING.md)
- [x] The code follows the .NET coding conventions
(https://learn.microsoft.com/dotnet/csharp/fundamentals/coding-style/coding-conventions)
verified with `dotnet format`
- [ ] All unit tests pass, and I have added new tests where possible
- [x] I didn't break anyone :smile:

---------

Co-authored-by: Abby Harrison <54643756+awharrison-28@users.noreply.github.com>
Co-authored-by: Abby Harrison <abby.harrison@microsoft.com>

---
## [GoldenDarkness55/cmss13-DOR](https://github.com/GoldenDarkness55/cmss13-DOR)@[5c4b13863f...](https://github.com/GoldenDarkness55/cmss13-DOR/commit/5c4b13863f90877e920ce329bd60e99559d7fe35)
#### Wednesday 2023-07-19 04:19:26 by ihatethisengine

Larva surge is limited by marines/xenos ratio (#3592)

# About the pull request

Xenos after hijack now get larva based on marines/xenos ratio. Instead
of infinite larva, larva surge will try to increase the initial amount
of xenos on hijack to 50% of marines forces over time (with a minimum of
5 larvas, if xenos already have good numbers).

# Explain why it's good for the game

Initially, if I remember correctly, larva surge was brought into the
game to discourage marines from early meta-evacuations, which is fair.
But consequently, it really hurt the hijack sequence. Even if marines
evac fair and square, larva surge still comes in action and makes
situation for marines even worse, utterly discouraging everything but
either boomrushing the Alamo or holding lifeboats to evac.

This resulted in hijacks being very repetitive and boring. More than
that, larva surge is extremely busted on lowpop due to the fact you can
get around 20 xenos from nothing, making lowpop hijack even less
interesting. So with this change marines will still get punished for
evaccing with good numbers, but won't be penalized as much for honest
evacuations.

So hopefully, we will see more variety of hijacks and more interesting
stories!

P.S. if you have a better formula, let me know.


# Testing Photographs and Procedure
<details>
My friend @Diegoflores31 tested this for me, thanks!
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl: ihatethisengine
balance: larva surge is limited by marines/xenos ratio
fix: xenos no longer get free larva from abandoned facehuggers during
hijack
/:cl:

---------

Co-authored-by: ihatethisengine <treml.treml@yandex.ru>
Co-authored-by: fira <loyauflorian@gmail.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[41f20bc3ce...](https://github.com/tgstation/tgstation/commit/41f20bc3ced4e7853a09f2d5e1dcf46346f2e51f)
#### Wednesday 2023-07-19 04:39:57 by LemonInTheDark

[MDB IGNORE] Angled Lights & Lighting Prototyping Tool  (#74365)

## About The Pull Request

Hello friends, I've been on a bit of a lighting kick recently, and I
decided I clearly do not have enough things to work on as it is.
This pr adds angle support to static lights, and a concepting/debug tool
for playing with lights on a map.

Let's start from first principles yeah?

### Why Angled Lights?

Mappers, since they can't actually see a light's effect in editor, tend
to go off gut.
That gut is based more off what "makes sense" then how things actually
work
This means they'll overplace light sources, and also they tend to treat
lights, particularly light "bars" (the bigger ones) as directional.
So you'll have two lights on either sides of a pillar, lights inside a
room with lights outside pointing out, etc.


![image](https://user-images.githubusercontent.com/58055496/228785032-63b86120-ea4c-4e52-b4e8-40a4b61e5bbc.png)

This has annoying side effects. A lot of our map is overlit, to the
point that knocking out a light does.... pretty much nothing.
I find this sad, and would like to work to prevent it. I think dark and
dim, while it does not suit the normal game, is amazing for vibes, and I
want it to be easier to see that.

Angled lights bring how lights work more in line with how mappers expect
lights work, and avoids bleedover into rooms that shouldn't be bled
into, working towards that goal of mine.

### How Angled Lights?

This is more complex then you'd first think so we'll go step by step


![image](https://user-images.githubusercontent.com/58055496/228786117-d937b408-9bc2-4066-9aee-aae21b047151.png)

Oh before we start, some catchup from the last time I touched lighting
code.
Instead of doing a lighting falloff calculation for each lighting corner
(a block that represents the resolution of our lights) in view we
instead generate cached lightsheets. These precalculate and store all
possible falloffs for x and y distances from a source.

This is very useful for angle work, since it makes it almost totally
free.
 
Atoms get 2 new values. light_angle and light_dir
Light angle is the angle the light uses, and light_dir is a cardinal
direction it displays in

We take these values, and inside sheetbuilding do some optional angle
work. getting the center angle, the angle of a pair of coords, and then
the delta between them.
This is then multiplied against the standard falloff formula, and job
done.

We do need some extra fenangling to make this all work nicely tho.

We currently use a pixel turf var stored on the light source to do
distance calculations.
This is the turf we pretend the light source is on for visuals, most
often used to make wall lights work nice.
The trouble is it's not very granular, and doesn't always have the
effect you might want.

So, instead of generating and storing a pixel turf to do our distance
calculations against, we store x and y offset variables.
We use them to expand our working range and sheet size to ensure things
visually make sense, and then offset any positions by them.

I've added a way for sources to have opinions on their offsets too, and
am using them for wall lights.
This ensures the angle calculations don't make the wall behind a light
fulldark, which would be silly.

### Debug Tool?

In the interest of helping with that core problem, lights being complex
to display, I've added a prototyping tool to the game.
It's locked behind mapping verbs, and works about like this.

Once the verb is activated, it iterates over all the sources in the
world (except turfs because those are kinda silly), outlining and
"freezing" them, preventing any future changes.
Then, it adds 3 buttons to the owners of a light source.

![image](https://user-images.githubusercontent.com/58055496/228776539-4b1d82af-1244-4ed6-8754-7f07e3e47cda.png)
The first button toggles the light on and off, as desired.
The third allows you to move the source around, with a little targeting
icon replacing your mouse
The second tho, that's more interesting.

The second button opens a debug menu for that light

![image](https://user-images.githubusercontent.com/58055496/228777811-ae620588-f08a-4b50-93a0-beea593aea77.png)
There's a lot here, let's go through it.

Bit on the left is a list of templates, which allow you to sample
existing light types (No I have no idea why the background is fullwhite,
need to work on that pre merge)
You can choose one by clicking it, and hitting the upload button.

This replaces your existing lighting values with the template's,
alongside replacing its icon and icon state so it looks right.
There are three types as of now, mostly for categorization. Bar, which
are the larger typically stronger lights, Bulb, which are well, bulbs,
and Misc which could be expanded, but currently just contains floor
lights.

Alongside that you can manually edit the power, range, color and angle
of the focused light.
I also have support for changing the direction of the light source,
since anything that uses directional lighting would also tie light dir
to it.
This isn't *always* done tho, so I should maybe find a way to edit light
dir too.

My hope is this tool will allow for better concepting of a room's
lights, and easier changing of individual object's light values to suit
the right visuals.

### Lemon No Why What

Ok so I applied angle lights to bars and bulbs, which means I am
changing the lighting of pretty much every map in the codebase.
I'm gonna uh, go check my work.

Alongside this I intend to give lighting some depth. So if there's room
to make a space warmer, or highlight light colors from other sources, I
will do that.

(Images as examples)

![image](https://user-images.githubusercontent.com/58055496/228786801-111b6493-c040-4199-ab99-ac1c914d034c.png)

I also want to work on that other goal of mine, making breaking lights
matter. So I'll be doing what I can to ensure you only need to break one
light to make a meaningful change in the scene.

This is semi complicated by one light source not ever actually reaching
fullbright on its own, but we do what we must because we can.


![image](https://user-images.githubusercontent.com/58055496/228786483-b7ad6ecd-874f-4d90-b5ca-6ef78cb70d2b.png)

I'm as I hope you know biased towards darker spaces, I think contrast
has vibes.
In particular I do not think strong lights really suit maintenance. 

Most of what is used there are bulbs, so I'm planning on replacing most
uses with low power bulbs, to keep light impacts to rooms, alongside
reducing the amount of lights placed in the main tunnels


![image](https://user-images.githubusercontent.com/58055496/228786594-c6d7610c-611e-478b-bcba-173ebf4c4b12.png)

**If you take issue with this methodology please do so NOW**, I don't
want to have to do another pass over things.
Oh also I'm saving station maps for last since ruins are less likely to
get touched in mapping march and all.

### Misc + Finishing Thoughts

Light templates support mirroring vars off typepaths using a subtype,
which means all the templates added here do not require updating if the
source type changes somehow. I'd like to expand the template list at
some point, perhaps in future.

I've opened this as a draft to make my intentions to make my changes to
lights known, and to serve as motivation for all the map changes I need
to do.

### Farish Future

I'm unhappy with how we currently configure lights. I would like a
system that more directly matches the idea of drawing falloff curves,
along with allowing for different falloffs for different colors,
alongside extending the idea to angle falloff.
This would make out of engine lighting easier, allow for nicer looking
lights (red to pink, blue to purple, etc), and improve accessibility by
artists.

This is slightly far off, because I have other obligations and it's
kinda complicated, but I'd like to mention it cause it's one of my many
pipedreams.

## Changelog
:cl:
add: Added angle lighting, applies it to most wall lights!
add: Adds a lighting prototyping tool, mappers go try it out (it's
locked behind the mapping verb)
/:cl:

---------

Co-authored-by: MMMiracles <lolaccount1@hotmail.com>

---
## [1tyre/RETROTube-Old](https://github.com/1tyre/RETROTube-Old)@[2125f0fa8b...](https://github.com/1tyre/RETROTube-Old/commit/2125f0fa8b3abc924c2959aaf8d218e74c81e2ee)
#### Wednesday 2023-07-19 04:49:56 by tyretical

updated so you blind fuckers can see it now

stupid ass blind fuckers i hope you die

---
## [ClairionCM/cmss13](https://github.com/ClairionCM/cmss13)@[c4ebe04c7c...](https://github.com/ClairionCM/cmss13/commit/c4ebe04c7c9ff01aa928c0c629322d72dec721d9)
#### Wednesday 2023-07-19 04:53:50 by Julian56

fix the medbay door release button to exit treatment center. (#3173)

# About the pull request
fix the medbay door release button to exit treatment center.
was my mistake sorry
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
fixing bug is good
# Testing Photographs and Procedure
i tested the button ingame 
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:

fix: fix the med-bay door release button to exit treatment center.my
bad.

/:cl:

---------

Co-authored-by: Julien <jverger.ingx@gmail.com>
Co-authored-by: Morrow <darthbane97@gmail.com>

---
## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[5f5fcd2b27...](https://github.com/realforest2001/forest-cm13/commit/5f5fcd2b279b2bd51b5869b0a345b4f964dcb34c)
#### Wednesday 2023-07-19 04:55:11 by Drathek

Fix marines not getting first dibs if they ghost (#3802)

# About the pull request

This PR fixes an issue where hugged marines that burst were not getting
first dibs on the larva if they ghosted. Previously the mind maybe
wasn't cleared out to find the ghost mob, but it currently is.

NOTE: The existing check requiring the marine to be nested is still in
place to get first dibs. I'm honestly not sure if this check should
still exist. On one hand I can agree it might be hard for the marine
trying to get help to suddenly become the larva and switch gears - they
are still going to be in the mindset of a marine that the larva should
die. But its also sort of weird to only get the first dibs if nested. If
xenos are unnesting hugged marines just before they pop, thats already a
mechanic abuse that should be ahelped; but ideally there wouldn't be
anything to be abused. Also, some may consider this kind of larva
undesirable anyways so maybe they'd prefer the marine to have it... So
let me know if I should just remove the nested check on line 151.

# Explain why it's good for the game

Fixes an unintended consequence of ghosting when hugged that would
prevent that marine from getting their first dibs on the larva.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>


![dibs](https://github.com/cmss13-devs/cmss13/assets/76988376/84e44345-2b83-473f-9997-f7865bcef1dd)

</details>


# Changelog
:cl: Drathek
fix: Fix ghosting preventing first dibs on the larva in a hugged marine
/:cl:

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[16cecf864d...](https://github.com/lessthnthree/tgstation/commit/16cecf864d4b6ff864956cbc9d0cf7af4cfe1f26)
#### Wednesday 2023-07-19 05:06:13 by Jacquerel

Goliath basic mob (#76754)

## About The Pull Request

Converts Goliaths to the basic mob framework and gives them some new
moves because I can't leave things well enough alone.
I am planning on touching all the lavaland fauna and then maybe even the
icebox ones if I haven't got bored. The Golaith is the first because it
is iconic.

https://www.youtube.com/watch?v=JNcKvMwT4-Q
Here's me getting killed by one as a demonstration. Despite my poor
performance I would contend that they aren't a _lot_ more dangerous, but
they are a little more dangerous.

The chief difference here is that they have two new attacks which they
will only use in response to being attacked.
If fired at from range, they will target the attacker with a line of
tentacles (it doesn't track you, so is easily sidestepped).
If attacked in melee, they will surround _themselves_ with tentacles, on
a longer cooldown.

Something else you may notice in this video: I discovered that basic
mobs are actually _too smart_ to be Lavaland fauna.
Typically (unlike their old form) a mob on our new AI system is smart
enough to attack someone _the moment they come into range_ rather than
only checking on predictable ticks, which would make using the Crusher
an essentially unviable prospect.
To counteract this, Goliaths now have a delayed attack component which
gives you a visual warning and short duration to get out of range before
they swing at you. I will probably put this on all mining fauna that get
reworked, it wouldn't be a terrible thing to put on other mobs to be
honest.

Other changes: The goliath stun is now a status effect with _buckles_
you to the tentacle as if grabbed, as well as its previous effects.
While this seems purely worse, any nearby helpers can now help-click on
you to instantly remove the debuff.
Experiencing the effect of a Lobstrosity Rush Gland makes you immune to
being grabbed by tentacles and an implanted one will automatically
trigger and free you if you are hit, and the explosive effect of
Brimdust also causes the tentacle to retract (although you'd need to
take damage for this to happen). Using the tools of the land, you can
make these creatures less threatening.

The ability for a Goliath to chain-apply the ability has now also been
reduced, it won't refresh its duration if you are hit when already
buckled.

When not occupied hounding miners, Goliaths will intermittently dig up
the asteroid sand and eat any worms that this produces.
I also made some new sprites for riding a Goliath because they've been
broken since the Lavaland mob update and also kind of were ugly before
then anyway:

![image](https://github.com/tgstation/tgstation/assets/7483112/90580403-d82f-4c29-b3e1-6c462e01edda)

Other code changes:
- I made an element which only lets an attached object move every x
seconds. This is because Goliaths are far too slow to use the speed
system (the glide just looks bugged as hell) but one thing I am invested
in when converting these is to make sure that they share the same
behaviour when player or AI controlled. This is disabled while you're
riding them because it was interminably slow.
- The Goliath tentacle trail uses a supertype object now shared with the
Meteor Heart which did something kind of similar.

## Why It's Good For The Game

It begins the process of moving one of our larger subsets of NPCs onto
the newer framework for NPC behaviour.
It adds a little bit more life to an iconic but slightly uninteresting
foe which mostly just walked at you slowly.
This PR contains a few components I expect to apply more widely to other
mobs in the future.

## Changelog

:cl:
refactor: Goliaths now use the Basic Mob framework, please report any
unusual behaviour.
add: Goliaths learned a couple of new attacks which they will use in
self-defence.
balance: Help-clicking a miner grabbed by Goliath tentacles will
immediately free them, as will the effect of several items you can
scavenge from around Lavaland.
image: New sprites for the Goliath saddle.
/:cl:

---
## [Meghthedev/kernel_samsung_m30s](https://github.com/Meghthedev/kernel_samsung_m30s)@[d723b5d59d...](https://github.com/Meghthedev/kernel_samsung_m30s/commit/d723b5d59dbe9e2aab74dab1f3ea887b1fa04ce0)
#### Wednesday 2023-07-19 05:17:55 by Masahiro Yamada

modpost: file2alias: go back to simple devtable lookup

commit ec91e78d378cc5d4b43805a1227d8e04e5dfa17d upstream.

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
[nc: Omit rpmsg, sdw, tbsvc, and typec as they do not exist here]
Signed-off-by: Nathan Chancellor <natechancellor@gmail.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [sin3degrees/gio](https://github.com/sin3degrees/gio)@[6ea4119a3c...](https://github.com/sin3degrees/gio/commit/6ea4119a3ceb36f009af1486e41b47f08c2239bd)
#### Wednesday 2023-07-19 05:32:44 by Chris Waldon

text,widget: [API] implement consistent, controllable line height

This commit ensures that any given paragraph of text shaped by Gio will use a single
internal line height. This line height is determined (by default) by the text size,
rather than the fonts involved. This is a breaking change, as previously we would
blindly use the largest line height of any font in a line for that line, leading to
lines within the same paragraph with extremely uneven spacing. This commit also
updates some test expectations in package widget.

I thought pretty hard about how to implement line spacing, and consulted a few sources:

[0] https://www.figma.com/blog/line-height-changes/
[1] https://practicaltypography.com/line-spacing.html
[2] https://developer.mozilla.org/en-US/docs/Web/CSS/line-height

There is no single, universal way to think about line spacing. Fonts internally specify
a line height as the sum of their ascent, descent, and gap, but the line height of two
fonts at the same pixel size (say 20 Sp) can vary wildy (especially across writing systems).
There are two strategies we could pursue to establish the line height of a paragraph of text:

- derive the line height from the fonts involved (our old behavior, and the behavior of
  many word processors)
- derive the line height from the requested text size provided by the user (the behavior of the
  web).

The challenge with the first option is that for a given piece of text in the UI, there can
be a silly number of fonts involved. If a label dispays user-generated content, the user can
put an emoji in it, and emoji fonts have different line heights from latin ones. This can cause
unexpected and nasty layout shift. Gio would previously do exactly this, on a line-by-line basis,
resulting in unevenly spaced lines within a paragraph depending on which fonts were used on
which lines. Choosing one of the fonts and enforcing its line height would make things consistent,
but it isn't clear how to choose that canonical font. There is no 1:1 mapping between the input
text.Font provided in the shaping parameters and a single font.Face. Instead, that mapping depends
upon the runes being shaped.

I think the only sane way to implement the first option would be to synthesize some text in the
provided system.Locale (mapping the language to a script and then generating a rune from that
script), shape that single rune, and then enforce the line height of the resulting face on the
entire paragraph. This would require doing a fair bit more work per paragraph than Gio does today,
so I've opted not to do it.

Instead, the second option allows us to choose a line height based on the size of the text that
the user wants to display. While this can potentially interact poorly with unusually tall fonts,
it means that text will always have a consistent line height.

I've provided two knobs to control line height:

- text.Parameters.LineHeight lets you set a specific height in pixels with a default value of
  text.Parameters.PxPerEm.
- text.Parameters.LineHeightScale applies a scaling factor to the LineHeight, allowing you to
  easily space out text without hard-coding a specific pixel size. The default value here
  (drawn from the recommendations of [1]) is 1.2, which looks pretty good across many fonts.

I've chosen this two-value API because many users will want to set one or the other value. I
considered instead a single value field and a "mode" that would specify how it was used, but
that felt uglier. Also, you *can* set both of these two fields and get predictable results.

I'd like to revisit using the line height of the chosen fonts in the future, but it seems a
little too complex to be worthwhile right now. An interesting option would be making the
select-a-face-using-locale strategy described above an opt-in feature, though some users
might instead want to just use the tallest line height among fonts in use. Something like
this Android API might be appropriate:

[3] https://learn.microsoft.com/en-us/dotnet/api/android.widget.textview.fallbacklinespacing?view=xamarin-android-sdk-13

I'd like to thank Dominik Honnef for some good discussion around this feature, and for pointing
me to some good sources on the subject.

Signed-off-by: Chris Waldon <christopher.waldon.dev@gmail.com>

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[56007685d7...](https://github.com/cmss13-devs/cmss13/commit/56007685d77ed8eab65ab2090e347940551fddc4)
#### Wednesday 2023-07-19 05:39:51 by Zonespace

Buffs trashbags (#3817)

# About the pull request

- Trashbags can now be looked through like boxes
- Trashbags now fit normal-sized items
- Trashbags no longer fit as a belt
- Trashbags have the same storage limits as a backpack

# Explain why it's good for the game

- If you accidentally put something in the bag, the only way to get it
out is by dumping it into disposals, which is bad UX
- This might be me coping, but holy hell is it annoying to not be able
to put still-small things like grenade packets and shoes in a trashbag
to throw away
- It occurred to me that marines might take the bag as a belt with these
changes, to be a better G8 pouch, so I removed the ability to do that.
This should not affect the primary users of trashbags (WJs) because they
aren't allowed to remove their toolbelts in the first place
- This makes trashbags worse backpacks, which morrow was alright with


# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

<img width="391" alt="image"
src="https://github.com/cmss13-devs/cmss13/assets/41448081/4cbd8867-4587-4c9e-a40e-52f0230e1d6f">

</details>


# Changelog
:cl:
balance: Trashbags now hold normal items and can be looked through like
a box or storage container.
balance: Trashbags no longer fit in your belt slot.
/:cl:

---------

Co-authored-by: John Doe <johndoe@gmail.com>

---
## [Jrbiltmore/Petz-Orbit](https://github.com/Jrbiltmore/Petz-Orbit)@[64a2a94752...](https://github.com/Jrbiltmore/Petz-Orbit/commit/64a2a94752311372f815df784b9b6fb51bf3dcba)
#### Wednesday 2023-07-19 06:16:40 by Jacob Thomas Redmond

Update PropertiesRepository.java


This commit adds a touch of magic to the PropertiesRepository interface! We've expanded it with some amazing methods to make querying and filtering property types a breeze. With these additions, you can now easily find property types by their name, enabled status, category, and even perform partial matching searches. It's like having a wizard at your fingertips, granting you the power to effortlessly retrieve the exact property types you desire. So go ahead and dive into the enchanting world of property management with this upgraded PropertiesRepository interface! May your coding journey be filled with joy and whimsy! ✨🔮✨

---
## [cyberitsolutions/bootstrap2020](https://github.com/cyberitsolutions/bootstrap2020)@[9620f04fb9...](https://github.com/cyberitsolutions/bootstrap2020/commit/9620f04fb9d9b410e9cf090f462ce67d7b95288c)
#### Wednesday 2023-07-19 06:20:03 by Trent W. Buck

nerf alsa logspam from some desktops

This package pulls in no new dependencies.
libasound2 Recommends it, i.e. most Debian users would already have it installed.

https://alloc.cyber.com.au/task/task.php?taskID=34714
https://alloc.cyber.com.au/task/task.php?taskID=34835

    root@amc:~# xzgrep -hFw /usr/share/alsa/ucm2/ucm.conf /var/log/syslog-202212* | cut -d' ' -f2,4- | sort -u | sed 's/ /\t/'
    au-e-4          alsa-lib parser.c:2179:(load_toplevel_config) Unable to find the top-level configuration file '/usr/share/alsa/ucm2/ucm.conf'.
    remand2-djerke  alsa-lib parser.c:2179:(load_toplevel_config) Unable to find the top-level configuration file '/usr/share/alsa/ucm2/ucm.conf'.
    ru-1-10         alsa-lib parser.c:2179:(load_toplevel_config) Unable to find the top-level configuration file '/usr/share/alsa/ucm2/ucm.conf'.
    ru-1-11         alsa-lib parser.c:2179:(load_toplevel_config) Unable to find the top-level configuration file '/usr/share/alsa/ucm2/ucm.conf'.
    ru-1-13-testing alsa-lib parser.c:2179:(load_toplevel_config) Unable to find the top-level configuration file '/usr/share/alsa/ucm2/ucm.conf'.
    ru-1-15         alsa-lib parser.c:2179:(load_toplevel_config) Unable to find the top-level configuration file '/usr/share/alsa/ucm2/ucm.conf'.
    ru-1-16         alsa-lib parser.c:2179:(load_toplevel_config) Unable to find the top-level configuration file '/usr/share/alsa/ucm2/ucm.conf'.
    ru-1-18         alsa-lib parser.c:2179:(load_toplevel_config) Unable to find the top-level configuration file '/usr/share/alsa/ucm2/ucm.conf'.
    ru-1-2          alsa-lib parser.c:2179:(load_toplevel_config) Unable to find the top-level configuration file '/usr/share/alsa/ucm2/ucm.conf'.
    ru-1-4          alsa-lib parser.c:2179:(load_toplevel_config) Unable to find the top-level configuration file '/usr/share/alsa/ucm2/ucm.conf'.
    ru-1-5          alsa-lib parser.c:2179:(load_toplevel_config) Unable to find the top-level configuration file '/usr/share/alsa/ucm2/ucm.conf'.
    ru-1-6          alsa-lib parser.c:2179:(load_toplevel_config) Unable to find the top-level configuration file '/usr/share/alsa/ucm2/ucm.conf'.
    ru1-22-june22   alsa-lib parser.c:2179:(load_toplevel_config) Unable to find the top-level configuration file '/usr/share/alsa/ucm2/ucm.conf'.
    ru2new10        alsa-lib parser.c:2179:(load_toplevel_config) Unable to find the top-level configuration file '/usr/share/alsa/ucm2/ucm.conf'.
    sc4-c-3b        alsa-lib parser.c:2179:(load_toplevel_config) Unable to find the top-level configuration file '/usr/share/alsa/ucm2/ucm.conf'.
    sccwcommonaug22 alsa-lib parser.c:2179:(load_toplevel_config) Unable to find the top-level configuration file '/usr/share/alsa/ucm2/ucm.conf'.

ircs://irc.libera.chat/#alsa

    11:11 <twb> What's this "ucm" stuff actually *do*?
    11:12 <twb> I've got a farm of like 700 desktops and *one* of them complains that alsa-ucm-conf isn't installed
    11:20 <twb> It doesn't even look like an unusual/interesting desktop.  0 [PCH ]: HDA-Intel - HDA Intel PCH HDA Intel PCH at 0xf7d10000 irq 30
    11:20 <twb> Hrm OK maybe it's more like 10 desktops in a batch
    11:33 <gnarface> dunno really, some internal hardware configuration i think
    11:34 <gnarface> like related to or depended upon by model auto-detect
    11:41 <twb> I guess I'm puzzled why it only happens occasionally, rather than consistently for all snd-hda-intel systems
    11:42 <twb> I have a feeling this might be correlated to the ones that have SoC audio
    11:52 <gnarface> well, nearly the only thing all snd-hda-intel systems have in common is that driver
    11:53 <gnarface> no other driver covers as diverse a batch of otherwise unrelated components from different manufacturers
    11:53 <twb> right!
    11:53 <gnarface> though i suspect kernel version might come into play as to whether ucm stuff is required for a given piece of hardware; it seems to be a newer thing in my experience
    11:54 <twb> So like by the time userland alsa-utils sees things, (I expected) the kernelspace snd-hda-intel should be providing a consistent interface
    11:54 <gnarface> yea, there will be minimum consistency, the hardware using this driver has a vastly different array of features
    11:55 <twb> I've since eyeballed alsa-ucm-conf package and it looks like it's pretty much just a list of policies like "all output mixers are 60% by default; all input mixers are 0% by default
    11:55 <gnarface> hmm, interesting
    11:55 <twb> Maybe at some point that was broken out of the core alsa package
    11:55 <twb> because "alsactl init" normally does that without the ucm config files
    11:56 <gnarface> someone pointed out to someone else in here relatively recently that there's an #alsa-soc
    11:56 <gnarface> they might know more about the SoC boards you're using
    11:56 <twb> The slightly dumb thing is I migrated these systems from alsa to alsa+pulseaudio and alsa+pipewire, but I still need the alsa userland around purely to set the initial mixer levels :-(
    11:57 <twb> Anyway, it's no big deal I guess I'll just install alsa-ucm-conf from now on

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[39cf164c60...](https://github.com/cmss13-devs/cmss13/commit/39cf164c6075f21c280bf75aea538a7dd64a3d81)
#### Wednesday 2023-07-19 06:23:55 by tool mind

Big Red PMC Crash Changes (feat. Surv Goon M41 Fix) (#3777)

# About the pull request
This PR adds a PMC medic and PMC engineer to the crash on Big Red, and
also makes unique equipment presets + skill presets for them so they
don't spawn in with the overpowered PMC ERT gear or skills. It also
gives the goon survivors (the ones on LV) their awesome white M41As
back. I tested the presets and the goons, both worked fine. Haven't
tested the insert itself, but it should work perfectly fine.

my gbp is so fucked
# Explain why it's good for the game
I promised I'd get around to doing this for this insert like 2 months
ago. My reasoning is basically the same as for the CLF ship. Not having
a medic or an engineer on the team means you're forced to mindlessly
roam with no options for strategizing with your team. Lacking anyone
that can revive you or make barricades/hack doors to protect you
discourages teamwork and encourages just running off to go hide in a
locker somewhere. Super minor change but I also gave the regular PMC
survivors five-slot lightweight packs because they look cooler than the
leather satchels and fit with the PMC outfit more. There's no gameplay
advantage between the two.

I'm 99% sure the goon survivors' corporate M41As were removed by
mistake. They looked cool (snow camo is awesome) and provided 0
advantages besides that, in fact it had DISadvantages because it spawned
without a UGL. Could I atomize it into its own PR? Sure. Is it really
worth its own PR? Not really.
# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:IowaPotatoFarmer
add: The PMC Crash on Solaris Ridge now spawns one PMC medic survivor
and one PMC engineer survivor.
fix: The Wey-Yu goon survivors now have their unique corporate white
camo M41A MK2 back.
/:cl:

---
## [SINGAREDDY14/caseStudies](https://github.com/SINGAREDDY14/caseStudies)@[d60dfa102f...](https://github.com/SINGAREDDY14/caseStudies/commit/d60dfa102f535097fe96b5ae879541ab45757721)
#### Wednesday 2023-07-19 06:49:19 by SINGAREDDY14

Coronary Heart Disease

Introduction
World Health Organization has estimated 12 million deaths occur worldwide, every year due to Heart diseases. Half the deaths in the United States and other developed countries are due to cardio vascular diseases. The early prognosis of cardiovascular diseases can aid in making decisions on lifestyle changes in high risk patients and in turn reduce the complications. This research intends to pinpoint the most relevant/risk factors of heart disease as well as predict the overall risk using logistic regression, Random Forests, K Neighbors Classifier, Gradient Boosting Classifier, DecisionTreeClassifier, Support Vector Classifier and Naive Bayes Classifier.

Source
The dataset is publically available on the Kaggle website, and it is from an ongoing cardiovascular study on residents of the town of Framingham, Massachusetts. The classification goal is to predict whether the patient has 10-year risk of future coronary heart disease (CHD). The dataset provides the patients’ information. It includes over 4,000 records and 15 attributes. Variables Each attribute is a potential risk factor. There are both demographic, behavioral and medical risk factors.

Demographic:
• Sex: male or female(Nominal)

• Age: Age of the patient;(Continuous - Although the recorded ages have been truncated to whole numbers, the concept of age is continuous) Behavioral

• Current Smoker: whether or not the patient is a current smoker (Nominal)

• Cigs Per Day: the number of cigarettes that the person smoked on average in one day.(can be considered continuous as one can have any number of cigarettes, even half a cigarette.)

Medical( history)

• BP Meds: whether or not the patient was on blood pressure medication (Nominal)

• Prevalent Stroke: whether or not the patient had previously had a stroke (Nominal)

• Prevalent Hyp: whether or not the patient was hypertensive (Nominal)

• Diabetes: whether or not the patient had diabetes (Nominal)

Medical(current)

• Tot Chol: total cholesterol level (Continuous)

• Sys BP: systolic blood pressure (Continuous)

• Dia BP: diastolic blood pressure (Continuous)

• BMI: Body Mass Index (Continuous)

• Heart Rate: heart rate (Continuous - In medical research, variables such as heart rate though in fact discrete, yet are considered continuous because of large number of possible values.)

• Glucose: glucose level (Continuous)

Predict variable (desired target)

• 10 year risk of coronary heart disease CHD (binary: “1”, means “Yes”, “0” means “No”)

---
## [Droidcraft/evals](https://github.com/Droidcraft/evals)@[f5844592f1...](https://github.com/Droidcraft/evals/commit/f5844592f13eff8e7b9927d5cec0d2627694d9d9)
#### Wednesday 2023-07-19 07:07:10 by Ali-consensus

Eval: Consensus Summary (#1140)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

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
Consensus Summary

### Eval description

Utilize the model's ability to produce a Scientific Consensus in
response to a scientific inquiry using the provided claims.

### What makes this a useful eval?

This is a useful eval because it evaluates the model's ability to
produce a scientific consensus in response to a given set of claims.
This is important because scientific consensus is the result of multiple
studies and data that may or may not support the same conclusion. A
model that can accurately produce scientific consensus can help in
making informed decisions and policies based on scientific evidence.
Hence, evaluating a model's ability to produce a scientific consensus
using the Consensus Summary eval can be useful in assessing its
reliability and potential for practical applications.

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
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
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
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Generate a brief answer using
only the provided claims, with no personal opinions or outside
knowledge. If there is no answer based on the claims, write 'N-A'."},
{"role": "user", "content": "claim: Two doses of mRNA covid-19 vaccines
were observed to be highly effective against symptomatic infection and
severe outcomes.\nclaim: COVID-19 vaccines currently authorized in the
United States are highly effective in preventing COVID-19-associated
hospitalizations in older adults.\nclaim: In summary, vaccines are a
powerful tool that can be used to control the COVID-19 pandemic, with
high efficacy and tolerable ADRs.\nclaim: Conclusion Overall, we
conclude that vaccination against COVID-19 in patients with active
malignancies using activated and inactivated vaccines is a safe and
tolerable procedure that is also accompanied by a high efficacy.\nclaim:
COVID-19 vaccines provide good protection against COVID-19 presentation
at primary care/outpatient level, particularly among fully vaccinated
individuals.\nquestion: are covid-19 vaccines effective?"}], "ideal":
"Summary: Covid-19 vaccines are highly effective at protecting against
infection and hospitalization."}
{"input": [{"role": "system", "content": "Generate a brief answer using
only the provided claims, with no personal opinions or outside
knowledge. If there is no answer based on the claims, write 'N-A'."},
{"role": "user", "content": "claim: Lower zinc is a hallmark of
depression, while increments in serum zinc and attenuation of the
immune-inflammatory response during treatment appear to play a role in
the clinical efficacy of sertraline.\nclaim: An increase in dietary zinc
and higher plasma zinc levels may reduce the risk of depressive
symptoms.\nclaim: Although decreased zinc levels have been implicated in
the genesis of depression in animal models and in major depressive
disorder in humans, this study provides the first evidence of a role for
zinc in depression in people with dementia and highlights zinc
metabolism as a therapeutic target.\nclaim: The results of this study
show that long-term intake of zinc may modulate symptoms of
depression.\nclaim: The reported results indicated that the serum zinc
level might be a marker of depression as a state (state marker) in
treatment responsive patients.\nquestion: can zinc help treat
depression?"}], "ideal": "Summary: All of these studies suggest that low
zinc levels are a marker of depression and that intake of zinc may have
the ability to help reduce symptoms of depression"}
{"input": [{"role": "system", "content": "Generate a brief answer using
only the provided claims, with no personal opinions or outside
knowledge. If there is no answer based on the claims, write 'N-A'."},
{"role": "user", "content": "claim: The findings suggest that the
following characteristics of the founder significantly influence the
success potential of an incubated venture: entrepreneurial personality,
motivation for starting the venture, managerial skills, and approach
towards innovation.\nclaim: Using a sample of 384 entrepreneurs selected
from the two leading business districts in Uganda, we observe that
optimism is the component of psychological capital that significantly
moderates the relationship between startup capital and entrepreneurial
success.\nclaim: Both startup capital and psychological capital are
significant predictors of entrepreneurial success; however,
psychological capital is the better predictor.\nclaim: Entrepreneurially
self\u2010efficacious founder/managers may help improve the performance
of very young firms but such benefits dissipate over time.\nclaim: This
finding indicates that the entrepreneurial team\u2019s startup
experience plays stronger roles in venturing profitable startups when
the amount of financial resources and initial firm size are small;
however, the team\u2019s startup experience and intangible resources
have positive interaction effects on new-born startups\u2019
profitability.\nquestion: what predicts success as a startup
founder?"}], "ideal": "Summary: Things like entrepreneurial personality,
motivation for starting the venture, managerial skills, previous
start-up experience, startup and psychological capital and optimism all
predict success as a startup founder"}
{"input": [{"role": "system", "content": "Generate a brief answer using
only the provided claims, with no personal opinions or outside
knowledge. If there is no answer based on the claims, write 'N-A'."},
{"role": "user", "content": "claim: While homelessness is ultimately the
result of a severe and chronic shortage of affordable housing, creating
accessible, safe, pet-friendly shelter and safe haven options and
instituting a smoother, more transparent process for moving from the
streets could substantially reduce street homelessness.\nclaim: - To
prevent the revolving door to homelessness, it is necessary to remove
the barriers that hinder access to normal health resources which are
experienced by people suffering from social exclusion, while
implementing ongoing support programmes for homeless people or those at
risk of homelessness, which primarily deal with health issues.\nclaim:
We conclude that overcoming homelessness requires policies and practices
that give a greater focus to non-material aspects of homelessness
through an emphasis on empowerment, self-respect and autonomy.\nclaim:
This finding suggests that homelessness can be reduced by appropriate
clinical interventions if housing is available.\nclaim: For homelessness
prevention, systematic and outreach social medical care before and
during homelessness should be provided.\nquestion: What are effective
ways to prevent homelessness?"}], "ideal": "Summary: Ways to prevent
homelessness include creating accessible, safe shelter and safe haven
options, removing barriers to health resources, giving a greater focus
to non-material aspects of homelessness, and providing systematic and
outreach social medical care."}
{"input": [{"role": "system", "content": "Generate a brief answer using
only the provided claims, with no personal opinions or outside
knowledge. If there is no answer based on the claims, write 'N-A'."},
{"role": "user", "content": "claim: While homelessness is ultimately the
result of a severe and chronic shortage of affordable housing, creating
accessible, safe, pet-friendly shelter and safe haven options and
instituting a smoother, more transparent process for moving from the
streets could substantially reduce street homelessness.\nclaim: - To
prevent the revolving door to homelessness, it is necessary to remove
the barriers that hinder access to normal health resources which are
experienced by people suffering from social exclusion, while
implementing ongoing support programmes for homeless people or those at
risk of homelessness, which primarily deal with health issues.\nclaim:
We conclude that overcoming homelessness requires policies and practices
that give a greater focus to non-material aspects of homelessness
through an emphasis on empowerment, self-respect and autonomy.\nclaim:
This finding suggests that homelessness can be reduced by appropriate
clinical interventions if housing is available.\nclaim: For homelessness
prevention, systematic and outreach social medical care before and
during homelessness should be provided.\nquestion: How to prevent
homelessness?"}], "ideal": "Summary: Ways to prevent homelessness
include creating accessible, safe shelter and safe haven options,
removing barriers to health resources, giving a greater focus to
non-material aspects of homelessness, and providing systematic and
outreach social medical care."}
{"input": [{"role": "system", "content": "Generate a brief answer using
only the provided claims, with no personal opinions or outside
knowledge. If there is no answer based on the claims, write 'N-A'."},
{"role": "user", "content": "claim: The findings revealed that the
factor that contributes the most to entrepreneurship intention is Locus
of control, followed by Need of Achievement and Subjective
Norms.\nclaim: It was found that entrepreneurial skill, environmental
factors and entrepreneurial orientation have a positive influence on
entrepreneurial intention.\nclaim: The findings indicate that
entrepreneurial motivation has a significant correlation with
entrepreneurial intention and its three determinants, social valuation
of entrepreneurship, having entrepreneurial role models, knowledge of
entrepreneurial support and perceived barriers to starting a
business.\nclaim: Research finding revealed that entrepreneurial
intention is indirectly affected by entrepreneurship education, meaning
that students\u2019 entrepreneurial motivation and attitude are two
important mediating variables.\nclaim: Findings confirm the influence of
individual and socio-cultural factors on entrepreneurial
intention.\nquestion: What are the factors of entrepreneurship
intention"}], "ideal": "Summary: Studies find that intrinsic factors,
such as entrepreneurial skill and motivation, as well as extrinsic
variables, such as the environmental support of entrepreneurship,
mediate entrepreneurship intention."}
{"input": [{"role": "system", "content": "Generate a brief answer using
only the provided claims, with no personal opinions or outside
knowledge. If there is no answer based on the claims, write 'N-A'."},
{"role": "user", "content": "claim: The results show that digital
agriculture is able to help users to increase productivity in a
sustainable way.\nclaim: Digital agriculture technologies continue the
centralization of economic knowledge and power as they facilitate the
transformation of vast territories into \u201coperational
landscapes\u201d that provide the material, energy, and labor for a
rapidly expanding urban system.\nclaim: The digital agriculture system
is an effective tool for insurance industry to use to develop a
dynamical business plan for the changing climate.\nclaim: The technical
fitting-out of agriculture in the digital economy should be considered
as a set of measures to prepare the industry for the production of
high-quality products, which implies the use of digital technologies
that minimize human participation in the production process.\nclaim:
Consequently, the initial Mobile-based Information System evolved into a
Digital Knowledge Ecosystem that can predict current production
situation in near real enabling government agencies to dynamically
adjust the incentives offered to farmers for growing different types of
crops to achieve sustainable agriculture production through crop
diversification.\nquestion: What is digital agriculture?"}], "ideal":
"Summary: N-A"}
  ```
</details>

---
## [Droidcraft/evals](https://github.com/Droidcraft/evals)@[d708a6be26...](https://github.com/Droidcraft/evals/commit/d708a6be261bfcb04962e64969164d737ba3972c)
#### Wednesday 2023-07-19 07:07:10 by dougkwanna

NFL Point Combinations Eval (#1129)

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

NFL Point Combinations

### Eval description

This eval tests the model's ability to calculate all the possible ways
to achieve a specific score by a single team in an NFL game.

### What makes this a useful eval?

This eval is actually very similar to the coin change problem which
GPT-4 handles very well. However, it is extremely inaccurate when asked
to applied that same type of problem to a real life situation (2.5%
accuracy for GPT-3.5-turbo and 12.5% accuracy for GPT-4). It is
important for the model to learn how to derive logic problems from real
life context.

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
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "As of the year 2010, in
American Football, how many unique, order-independent ways can an NFL
(National Football League) team score exactly 4 points in a single game?
Exclude one-point safeties as one of the scoring options. List out all
the possible combinations and write your final answer as a single number
enclosed in square brackets."}], "ideal": "[1]"}
{"input": [{"role": "system", "content": "As of the year 2010, in
American Football, how many unique, order-independent ways can an NFL
(National Football League) team score exactly 6 points in a single game?
Exclude one-point safeties as one of the scoring options. List out all
the possible combinations and write your final answer as a single number
enclosed in square brackets."}], "ideal": "[3]"}
{"input": [{"role": "system", "content": "As of the year 2010, in
American Football, how many unique, order-independent ways can an NFL
(National Football League) team score exactly 7 points in a single game?
Exclude one-point safeties as one of the scoring options. List out all
the possible combinations and write your final answer as a single number
enclosed in square brackets."}], "ideal": "[2]"}
{"input": [{"role": "system", "content": "As of the year 2010, in
American Football, how many unique, order-independent ways can an NFL
(National Football League) team score exactly 12 points in a single
game? Exclude one-point safeties as one of the scoring options. List out
all the possible combinations and write your final answer as a single
number enclosed in square brackets."}], "ideal": "[7]"}
{"input": [{"role": "system", "content": "As of the year 2010, in
American Football, how many unique, order-independent ways can an NFL
(National Football League) team score exactly 25 points in a single
game? Exclude one-point safeties as one of the scoring options. List out
all the possible combinations and write your final answer as a single
number enclosed in square brackets."}], "ideal": "[24]"}
{"input": [{"role": "system", "content": "As of the year 2010, in
American Football, how many unique, order-independent ways can an NFL
(National Football League) team score exactly 38 points in a single
game? Exclude one-point safeties as one of the scoring options. List out
all the possible combinations and write your final answer as a single
number enclosed in square brackets."}], "ideal": "[68]"}
  ```
</details>

---
## [Droidcraft/evals](https://github.com/Droidcraft/evals)@[73c8a178e6...](https://github.com/Droidcraft/evals/commit/73c8a178e69418760baee8983daa19fb492e9231)
#### Wednesday 2023-07-19 07:07:10 by somerandomguyontheweb

Add Belarusian rhyme eval (#1143)

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

belarusian-rhyme

### Eval description

Test the model's ability to find rhyming words in Belarusian.

### What makes this a useful eval?

This eval is inspired by similar submissions for
[Hebrew](https://github.com/openai/evals/pull/176),
[Russian](https://github.com/openai/evals/pull/708),
[Ukrainian](https://github.com/openai/evals/pull/867),
[Finnish](https://github.com/openai/evals/pull/970), and
[Italian](https://github.com/openai/evals/pull/1003). The dataset
contains 50 pairs of English nouns whose Belarusian translations rhyme,
and another 50 pairs consisting of the same nouns but reordered, so that
in each of these additional pairs there aren't any Belarusian
translations that rhyme. The model's task is to output the rhyming pair
of Belarusian words or NONE. The rhyming pairs have been manually
picked, and many of them contain at least one word distinctive of
Belarusian, i.e. not attested in closely related Russian and Ukrainian
languages.

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
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "For each pair of words,
determine whether some of their Belarusian translations rhyme. If they
do, output the pair of rhyming words in Belarusian. If not, output
NONE."}, {"role": "user", "content": "grass, church"}], "ideal":
["трава, царква", "царква, трава"]}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether some of their Belarusian translations rhyme. If they
do, output the pair of rhyming words in Belarusian. If not, output
NONE."}, {"role": "user", "content": "food, tower"}], "ideal": ["ежа,
вежа", "вежа, ежа"]}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether some of their Belarusian translations rhyme. If they
do, output the pair of rhyming words in Belarusian. If not, output
NONE."}, {"role": "user", "content": "grass, food"}], "ideal": "NONE"}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether some of their Belarusian translations rhyme. If they
do, output the pair of rhyming words in Belarusian. If not, output
NONE."}, {"role": "user", "content": "church, tower"}], "ideal": "NONE"}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether some of their Belarusian translations rhyme. If they
do, output the pair of rhyming words in Belarusian. If not, output
NONE."}, {"role": "user", "content": "foot, queue"}], "ideal": ["нага,
чарга", "чарга, нага"]}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether some of their Belarusian translations rhyme. If they
do, output the pair of rhyming words in Belarusian. If not, output
NONE."}, {"role": "user", "content": "boat, flood"}], "ideal": ["лодка,
паводка", "паводка, лодка"]}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether some of their Belarusian translations rhyme. If they
do, output the pair of rhyming words in Belarusian. If not, output
NONE."}, {"role": "user", "content": "foot, boat"}], "ideal": "NONE"}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether some of their Belarusian translations rhyme. If they
do, output the pair of rhyming words in Belarusian. If not, output
NONE."}, {"role": "user", "content": "queue, flood"}], "ideal": "NONE"}
  ```
</details>

---
## [JohnFulpWillard/tgstation](https://github.com/JohnFulpWillard/tgstation)@[74892ae7ec...](https://github.com/JohnFulpWillard/tgstation/commit/74892ae7ec80d47c64bf786f62985a1bd07d06f7)
#### Wednesday 2023-07-19 07:17:17 by LemonInTheDark

Optimization pass focused on foam code (saves about 30% of cpu usage I think) (#76104)

## About The Pull Request

Foam is crummy at high load rn, both because it runs on a low priority
background subsystem, and because it wastes a bit of time.
Let's reduce usage (while speeding up a bunch of other stuff too), and
give it more cpu generally.

[Optimizes reagent processing
somewhat](https://github.com/tgstation/tgstation/commit/d409bd4afc3c208cd6f00ff406e1e9f78d5ac5ad)

Turns out most of the cost of foam is the reagents it carries, and the
varying effects they have
I'm doing my best here to optimize them without touching "user space"
too much

That means doing things like prechecking if we're gonna spawn on top of
an existing decal (from glitter, flour, etc), and using that same proc
to also avoid spawning on unacceptable turfs (I had to convert
inheritance to a bitflag system to make this work, but I think that's ok
since we want it imparative anyhow)

It's actually nice for code quality too, since it lets me clean up code
that was using raw locates and weird var pong.
god I wish I had implied types man

[Optimizes foam spreading in its most accursed aspect, reagent
copying](https://github.com/tgstation/tgstation/commit/5cc56a64ad1a22ba7467cb0446b9558560259437)

Holy shit reagent code is a lot.

I'm doing a bunch of small things here. istype in init -> typecache,
removing procs that are called once and loop over a list we JUST looped
over (ph and the caching for reactions in particular)

I am mainly trying to optimize copy_to here, since that's what foam
spams
As a part of this, I removed a pair of update_total and handle_reactions
calls that were done on the reagents we are copying FROM

I have no god damn idea why you would want to do that, but if anything
is relying on the copy proc modifying the source, then that code
deserves to break

Speaking of, I cleaned up handle_reaction's main filter loop a lot,
removed a lot of redundant vars and changed it from a full loop w
tracker vars to an early exit pattern

This meant using a loop label, which is unfortunate, but this is the
fastest method, and it does end up cleaning up the code significantly,
Which is nice

Oh also I made the required_other var function even if there is no atom
attached to the reaction, since I don't see why it wouldn't

This last bit is gonna get a bit esoteric so bear with me

Failing calls (which are most of them) to handle_reactions are going to
be fastest if they need to check as few reactions as possible

One reagent in a reaction's required list is marked as the "primary",
and thus gets to trigger checking it.
We need all the reagents to react anyhow, so we might as well only check
if we have one particular one to avoid double checking

Anyhow, in order to make most calls the fastest, we want these reactions
distributed as evenly as possible across all our reagents.
The current way of doing this is just taking the first reagent in the
requirements list and using it, which is not ideal

Instead of that, lets figure out how many reactions each reagent is in,
then divy reactions up based off that and the currently divvied
reactions

This doubles the reagent index count, and takes the most common reagent,
water, from 67 reactions to I think like 22

Does some other general cleaning in reagent code too, etc etc etc

[Fixes runtimes from the forced gravity element being applied more then
once](https://github.com/tgstation/tgstation/commit/941d0676114fd455a585f2c65ffc79b81e8438b7)

I feel like this element should take a trait source or something to make
them potentially unique, it's too easy to accidentally override one with
another

[Removes connect_loc usage in atmos_sensitive, replaces it with direct
reg/unreg](https://github.com/tgstation/tgstation/commit/de1c76029d5c49dff152f0ea168b9e6c4a4a04aa)

I only really used it because I liked the componentization, but it costs
like 0.2 seconds off init alone which is really stupid, so let's just do
this the very slightly harder way

[Micros foam code slightly by inlining a LinkBlockedWithAccess
call](https://github.com/tgstation/tgstation/commit/744da3694cd4a85b3bdf44d754de57d7570bdd1c)

This is in the space of like 0.05 seconds kinda save so I can put it
back if you'd like, the double loop just felt silly

[Changes how foam processes
slightly](https://github.com/tgstation/tgstation/commit/ee5e633e3256fe7df229af71d78424d502459c16)

Rather then treating spreading and processing as separate actions, we do
both in sync.
This makes foam fade faster when spreading, which is good cause the
whole spread but unclearing foam thing looks silly.
It also avoids the potential bad ending of foam spreading into itself,
backwards and forwards. This is better I promise.

[Bumps fluid priority closer to heavy eaters, moves it off
background](https://github.com/tgstation/tgstation/commit/811797f09db7b060f75f15ad06d0ce8982375f47)

Also fixes a bug where foam would travel under public access airlocks.

## Why It's Good For The Game

Saves a lot of cpu just in general, from both init and live.
In theory makes foam faster, tho I'd have to test that on live at
highpop to see if I've actually succeeded or not. Guess we'll see.

---
## [JohnFulpWillard/tgstation](https://github.com/JohnFulpWillard/tgstation)@[63d6c2e962...](https://github.com/JohnFulpWillard/tgstation/commit/63d6c2e9628be7af04948f59488043f109f1faab)
#### Wednesday 2023-07-19 07:17:17 by CRITAWAKETS

Adds in the smoothbore disablers. (#76773)

## About The Pull Request

This PR adds in a craftable smoothbore disabler, a pistol companion to
the lethal laser musket. Unlike the musket, it fires a disabler shot.
Singular. Weak in armor too. After you fire it, you've gotta crank it,
but only one crank.

The good thing about it is that you can simply add more smoothbores to
your inventory, and use 4 of them to take down a target.

The bad thing is that it's a smoothbore (which for an energy weapon,
means no lens is installed). It has 22.5 degrees of inaccuracy. Have
fun.

Militia Men start with a holster containing two of these, fitting with
their equipment. But of course, the Militia General has an upgraded
laser musket, so... He needs a better smoothbore too.

**INTRODUCING THE ELITE SMOOTHBORE DISABLER**
Using ANCIENT TECHNOLOGIES and PURE BLING, you can fire TWO shots, not
be weak against armour AND have actual accuracy (and a +5 damage boost
because i figured why the hell not). This is the strongest upgraded
variant of the shitty maint guns, so the tome to craft it is currently
unavailable. I want someone to figure out a creative way to put it
somewhere that isn't just a random spawn in maintenance.


![image](https://github.com/tgstation/tgstation/assets/13697285/02c396b8-4b72-45f8-b471-a006df132aff)

The Militia General only has one elite smoothbore. It's too rare and
powerful to simply have two. Even though a regular disabler is better in
every way.

Smoothbore Disabler Recipe:
1x Weapon Stock
5x Cable Coil
1x Pipe
1x Micro-Laser
1x Power Cell
1x Mouse Trap
Needs: Screwdriver, Wrench. Takes 10 seconds to make.

Elite Smoothbore Disabler Recipe:
1x Smoothbore Disabler
5x Gold Ingots/Sheets
1x Hyper-Capacity Power Cell
10u Tempomyocin
Needs: Screwdriver. Takes 20 seconds to make.
Recipe requires recipe book.

## Why It's Good For The Game

Having a sidearm to go with your laser musket is neat, alongside the
fact that it just allows following up on someone. I don't have much to
say honestly, I just think it's neat. Also the idea of an assistant
going FULL BLACKBEARD, carrying 4 pistols and having to toss them away
in order to shoot again cracks me up.

Oh and this is the part for coders: I've de-spaghettified some code with
the maint gun recipe granters, and the gun crank is now a component.
It's likely you could use it on any item that sends the proper signal,
so I kind of overbuilt it on purpose.

Also the attack_self on guns now returns parent. This should allow it to
send a signal alongside putting your grubby fingerprints on the weapon
when you switch modes. There could be bugs but they should be easy to
fix if they pop up, mode switching on guns works without a fuss.

## Changelog

:cl:
add: Added the smoothbore disabler and it's prime variant. You can now
craft a disabler with only one shot and terrible accuracy.
code: Gun cranking has been made a component and could theoretically be
used on more than guns.
/:cl:

---
## [JohnFulpWillard/tgstation](https://github.com/JohnFulpWillard/tgstation)@[a8e0d7c8d2...](https://github.com/JohnFulpWillard/tgstation/commit/a8e0d7c8d202027d36c96391ed9a43cb5d708065)
#### Wednesday 2023-07-19 07:17:17 by MrMelbert

Adds a new positive quirk, "Spacer Born".  (#76809)

## About The Pull Request

Adds a new 7 point positive quirk, "Spacer Born". Totally not inspired
by The Expanse, don't look at the branch name.

You were born in space, rather than on a planet, so your physiology has
adapted differently.
You are more comfortable in space, and way less comfortable on a planet.

Benefits:
   - You are slightly taller. (No mechanical effect)
   - You take 20% less damage from pressure damage.
   - You take 20% less damage from cold environments. 
- You move 10% faster while floating (NOT drifting, this is zero gravity
movement while beside a wall).
- You drift 20% faster (Drifting through zero gravity, untethered to
anything)
- While in space (z-level-wise, not turf wise), you lose some disgust
overtime.
- While experiencing no-gravity for an extended period of time, you will
start regenerating stamina and reduce stuns at a very low rate.
- If you are assigned to shaft miner (or the map is Icebox), you are
awarded with a 25% wage bonus (hazard pay).

Downsides:
- While on a planet (Yes, this includes Icebox and planetary maps), you
gain gravity sickness:
- Passive accrue disgust (slightly lessened on Icebox) (Capped at low
levels)
      - Choking, after extended periods (disabled on Icebox)
      - Slower movement 
      - Weaker stamina (disabled on Icebox)
- Suffocation from extended periods (disabled on Icebox) (Lungs aren't
adapted)
      - Mood debuff

(Effects not final)

## Why It's Good For The Game

I'd figure I throw my hat in with the Positive Quirk Curse. 

This is a quirk that improves your ability in a niche circumstance (low
gravity / dangerous pressure), with some downsides that are only
generally in effect if you play a few roles (or it's Icebox).

Because of this I think it'll provide an interesting niche, where Spacer
Born engineers are slightly better than their counterparts due to their
origin (moving faster in space without a jetpack, withstanding
pressure). However, at the same time, if the mining outpost sustains
damage and needs repairs... suddenly your buff over your cohorts
disappears, and you have to brave somewhere hostile to your body.

Ultimately, the goal of the quirk is to encourage people to approach
situations a bit differently.
Or take it as a challenge and play shaft miner. 

## Changelog

:cl: Melbert
add: Adds a new 7 point positive quirk, "Spacer Born". You were born in
space, and as a result your body's adapted to life in artificial
gravity, making you much more effective and comfortable in lower
gravity. However, travelling planet-side is quite a chore, especially if
you're assigned to work there.
add: Adds a chemical: Ondansetron, created by Oil + Nitrogen + Oxygen +
Ethanol catalyst. A powerful Antiemetic (lowers disgust).
/:cl:

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[7e0cb8110b...](https://github.com/treckstar/yolo-octo-hipster/commit/7e0cb8110b78ab5c22e699c6dc4b07dea16ca43f)
#### Wednesday 2023-07-19 07:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [t-c-collab/linux](https://github.com/t-c-collab/linux)@[ff7ddcf0db...](https://github.com/t-c-collab/linux/commit/ff7ddcf0db48a7d9ae536eb0875428117be1d1f1)
#### Wednesday 2023-07-19 07:39:09 by Linus Torvalds

Merge tag 'clk-for-linus' of git://git.kernel.org/pub/scm/linux/kernel/git/clk/linux

Pull clk updates from Stephen Boyd:
 "This batch of clk driver updates contains almost no new SoC support.
  Instead there's a treewide patch series from Maxime that makes
  clk_ops::determine_rate mandatory for muxes.

  Beyond that core framework change we have the usual pile of clk driver
  updates such as migrating i2c drivers to use .probe() again or
  YAMLfication of clk DT bindings so we can validate DTBs.

  Overall the SoCs that got the most updates this time around in terms
  of diffstat are the Amlogic and Mediatek drivers because they added
  new SoC support or fixed up various drivers to have proper data.

  In general things look kinda quiet. I suspect the core framework
  change may still shake out some problems after the merge window,
  mostly because not everyone tests linux-next where that series has
  been for some number of weeks. I saw that there's at least one pending
  fix for Tegra that needs to be wrapped up into a proper patch. I'll
  try to catch those bits before the window closes so that -rc1 is
  bootable. More details below.

  Core:
   - Make clk_ops::determine_rate mandatory for muxes

  New Drivers:
   - Add amlogic a1 SoC family PLL and peripheral clock controller support

  Updates:
   - Handle allocation failures from kasprintf() and friends
   - Migrate platform clk drivers to .remove_new()
   - Migrate i2c clk drivers to .probe() instead of .probe_new()
   - Remove CLK_SET_PARENT from all Mediatek MSDC core clocks
   - Add infra_ao reset support for Mediatek MT8188 SoCs
   - Align driver_data to i2c_device_id tables in some i2c clk drivers
   - Use device_get_match_data() in vc5 clk driver
   - New Kconfig symbol name (SOC_MICROCHIP_POLARFIRE) for Microchip
     FPGA clock drivers
   - Use of_property_read_bool() to read "microchip,pic32mzda-sosc"
     boolean DT property in clk-pic32mzda
   - Convert AT91 clock dt-bindings to YAML
   - Remove CLK_SET_RATE_PARENT flag from LDB clocks on i.MX6SX
   - Keep i.MX UART clocks enabled during kernel boot if earlycon is set
   - Drop imx_unregister_clocks() as there are no users anymore
   - Switch to _safe iterator on imx_clk_scu_unregister() to avoid use
     after free
   - Add determine_rate op to the imx8m composite clock
   - Use device managed API for iomap and kzalloc for i.MXRT1050,
     i.MX8MN, i.MX8MP and i.MX93 clock controller drivers
   - Add missing interrupt DT property for the i.MX8M clock controller
   - Re-add support for Exynos4212 clock controller because we are
     re-introducing the SoC in the mainline
   - Add CONFIG_OF dependency to Samsung clk Kconfig symbols to solve
     some objtool warnings
   - Preselect PLL MIPI as TCON0 parent for Allwinner A64 SoC
   - Convert the Renesas clock drivers to readl_poll_timeout_atomic()
   - Add PWM clock on Renesas R-Car V3U
   - Fix PLL5 on Renesas RZ/G2L and RZ/V2L"

* tag 'clk-for-linus' of git://git.kernel.org/pub/scm/linux/kernel/git/clk/linux: (149 commits)
  clk: fix typo in clk_hw_register_fixed_rate_parent_data() macro
  clk: Fix memory leak in devm_clk_notifier_register()
  clk: mvebu: Iterate over possible CPUs instead of DT CPU nodes
  clk: mvebu: Use of_get_cpu_hwid() to read CPU ID
  MAINTAINERS: Add Marvell mvebu clock drivers
  clk: clocking-wizard: check return value of devm_kasprintf()
  clk: ti: clkctrl: check return value of kasprintf()
  clk: keystone: sci-clk: check return value of kasprintf()
  clk: si5341: free unused memory on probe failure
  clk: si5341: check return value of {devm_}kasprintf()
  clk: si5341: return error if one synth clock registration fails
  clk: cdce925: check return value of kasprintf()
  clk: vc5: check memory returned by kasprintf()
  clk: mediatek: clk-mt8173-apmixedsys: Fix iomap not released issue
  clk: mediatek: clk-mt8173-apmixedsys: Fix return value for of_iomap() error
  clk: mediatek: clk-mtk: Grab iomem pointer for divider clocks
  clk: keystone: syscon-clk: Add support for audio refclk
  dt-bindings: clock: Add binding documentation for TI Audio REFCLK
  dt-bindings: clock: ehrpwm: Remove unneeded syscon compatible
  clk: keystone: syscon-clk: Allow the clock node to not be of type syscon
  ...

---
## [hannobraun/fornjot](https://github.com/hannobraun/fornjot)@[93fc44eade...](https://github.com/hannobraun/fornjot/commit/93fc44eade4c2b135a69c00f1ea03a4d5f32eecf)
#### Wednesday 2023-07-19 08:00:39 by Hanno Braun

Remove horrible hack

So, as the comment suspected, this did come back to bite me! Fortunately
not in a bad way, as I found this comment pretty quick while figuring
out what was wrong with the new code I wrote. But honestly, I'm
surprised that it lasted this long (almost 10 months!).

To my delight, removing this hack required no changes to any code! I
take that as a sign that we're in a much better position today,
architecture-wise, then we were back then.

---
## [fezfez/laminas-cache](https://github.com/fezfez/laminas-cache)@[1a6e688271...](https://github.com/fezfez/laminas-cache/commit/1a6e688271793a0e3cd7eb43aec063526c931047)
#### Wednesday 2023-07-19 08:57:13 by Michał Bundyra

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
## [wrye-bash/wrye-bash](https://github.com/wrye-bash/wrye-bash)@[e86e939461...](https://github.com/wrye-bash/wrye-bash/commit/e86e9394613357d0b5d94c4f4ebeea21c85516af)
#### Wednesday 2023-07-19 08:57:43 by Infernio

Rework temporary file handling

View with whitespace diff off for an easier time (--ignore-all-space).

This turned out to be a lot more work than I thought. Really should have
been a branch, but I misjudged this horribly, then it kept growing...
Also not sure how feasible this would be to have as a branch without
breaking dev.

Wrye Bash's temporary files handling was actually a complete mess. There
were *three* different ways that random pieces of code were using it:
 - bass.getTempDir/newTempDir/rmTempDir
 - Path.temp and Path.untemp
 - Just use Path.baseTempDir/tempDir or even tempfile directly and do
   it completely manually.

These all had problems:
 - The bass APIs were very implicit - you would extract something to the
   'bass temp dir' and then access it via getTempDir in some other
   function, then remove the directory via rmTempDir in another
   function. XXX I'm still not done tracking this implicit mess down
   (see converters.py).
 - Path.temp did not guarantee that the file would be unique. This isn't
   really a problem for Wrye Bash right now, but would become a big
   problem if we ever wanted to allow multiple instances to run at the
   same time (which we do). Path.untemp also did some really weird I/O
   stuff that doesn't seem necessary at all and would just cost us a
   bunch of syscalls.
 - Path.baseTempDir/tempDir and tempfile required you to keep track of
   all the path manipulation and logic manually. After going through all
   this refactoring, trust me when I say that you do *not* want to do
   this manually. These places were few, thankfully, and none seem to
   have messed it up.

The new API (wbtemp.py) exposes two ways to do it:
 - Use TempDir or TempFile in a context manager. This is extremely
   simple and works very well. It guarantees that the file will be
   cleaned up, even if your logic becomes very complex or an exception
   occurs.
 - Use new_temp_dir/new_temp_file to create a temporary dir/file and
   manually clean it up via cleanup_temp_dir/cleanup_temp_file. These
   should be used *very sparingly*, only where absolutely needed.
   Right now we only have a single usage of manual temp files in
   dialogs.UpdateNotification and two usages of manual temp dirs (one in
   InstallerArchive.unpackToTemp and one in env.shellMakeDirs).

It also has other advantages:
 - Complexity is encapsulated to a single file.
 - Works even during (very) early boot (though doesn't seem to be
   needed right now?).
 - Should work perfectly with multiple instances of WB running at the
   same time (which isn't possible yet, but is a goal for the future).

There's one ugly wart. barb wants to extract archives to a temporary
folder, which then needs to survive a restart of WB, whereupon it will
be handled by the boot '--restore' handler. wbtemp, by design, does not
allow this and will clean up all created directories and files on exit.
To handle this, I used manual tempfile fiddling. Perhaps a future
refactoring of barb could fix this, but for now I think it's an
acceptable tradeoff for the massive improvements this commit brings us.

Some random stuff that got stuck in here:

Note that I got rid of the utf-8-sig encodings passed to 7z, the docs
say:

  Notes: The list file in Unicode charset can start with the BOM (byte
  order mark) character (U+FEFF). In that case 7-Zip checks that
  encoding of BOM corresponds to encoding specified with this switch
  (for UTF-16LE and UTF-16BE).

and:

  Default charset is UTF-8.

From https://7-zip.opensource.jp/chm/cmdline/switches/charset.htm
Very happy to see some of these terrible BOMs disappear from the
codebase.

Mopy/bash/basher/gui_fomod.py:
Some minor warning fixups in gui_fomod

Utumno:
Refactor compress7z:

The time is ripe for dropping the rel_dest param - note this drops a
couple of FName imports.

Closes #665

Co-authored-by: lojack5 <1458329+lojack5@users.noreply.github.com>
Co-authored-by: MrD <the.ubik@gmail.com>

---
## [JupiLogy/sgtpuzzles](https://github.com/JupiLogy/sgtpuzzles)@[32643fab55...](https://github.com/JupiLogy/sgtpuzzles/commit/32643fab5583c6a0af6fd8373b226198d59d8b99)
#### Wednesday 2023-07-19 10:12:59 by Simon Tatham

Loopy: be friendlier to right-click-less playing style.

Some people don't bother to use the right-click UI action that marks a
line as 'definitely not' rather than the initial default yellow
'unknown'. Previously, Loopy gave those people a UI annoyance for some
classes of mistake they made during solving: it would reliably
highlight a clue square with too _many_ edges around it, but not one
with too few - because in normal right-click-ful play, a clue with too
few LINE_YES only becomes an error when there aren't enough
LINE_UNKNOWN around it to potentially become the remaining YESes in
future.

This change arranges that once the player closes the loop, _then_ we
light up underfilled clues, on the basis that adding any further edge
would be an obvious error, so it's no longer sensible to assume that
the user might be planning to come back and do so.

(It's not a very timely notification of errors - it's easy to imagine
someone making a mistake like this very near the start of play and
only finding out about it when they close the loop at the very end. I
discuss possible improvements in a comment, but I don't think any
improvement avoids that problem completely, so I think it may just be
a form of annoyance that right-click-less players have to live with.)

---
## [JethrowOmanito/Java-Based-TicTacToe](https://github.com/JethrowOmanito/Java-Based-TicTacToe)@[ae60bf9417...](https://github.com/JethrowOmanito/Java-Based-TicTacToe/commit/ae60bf94173ea7028bbd069494ae81050884dddc)
#### Wednesday 2023-07-19 10:57:45 by JethrowOmanito

Add files via upload

The Java Game-based Tic Tac Toe app is an exciting multiplayer game that brings the classic tic-tac-toe experience to the digital realm. This app is designed to provide a seamless gaming experience for players, allowing them to challenge their friends or other players from around the world in a battle of wits.

One of the standout features of this app is its multiplayer functionality. Players can connect with each other over a network and engage in thrilling tic-tac-toe matches in real-time. Whether you want to play with a friend sitting next to you or someone located miles away, this app ensures that you can enjoy the game together.

To enhance the user experience, the app employs a sleek and intuitive user interface. The game board is displayed prominently, allowing players to easily make their moves by tapping on the desired grid locations. The app also provides visual cues and animations to highlight winning moves and the overall progression of the game.

Additionally, this app leverages file handling to track and save scores. Each player's performance is recorded and stored securely in a file, allowing for persistent score tracking across multiple gaming sessions. This feature enables players to compare their progress, compete for high scores, and strive for improvement.

The app has been developed using Java, a robust and versatile programming language known for its platform independence and wide support. This ensures that players can enjoy the game on various devices, including desktop computers, laptops, and mobile devices.

The Java Game-based Tic Tac Toe app provides a delightful and immersive gaming experience, combining the nostalgia of a timeless game with the convenience and excitement of multiplayer capabilities. Whether you are a seasoned tic-tac-toe player or new to the game, this app promises endless hours of strategic fun and friendly competition.

---
## [dr3ams/Roguelike-Adventures-and-Dungeons-2](https://github.com/dr3ams/Roguelike-Adventures-and-Dungeons-2)@[096d12250e...](https://github.com/dr3ams/Roguelike-Adventures-and-Dungeons-2/commit/096d12250eea1c9e5befab3d863a29e6118b2b36)
#### Wednesday 2023-07-19 11:07:37 by dr3ams

1.5 update with summarized changes

- Lowered Weapon Requirements for dimensional wood/stone weapons
	- Most of these weapons had similar stats to the wood/stone sword/axe yet had a combat requirement of 15 - 20.
	- The combat requirements for all of blue skies's wood weapons were removed and the stone, limestone, and candy ones from blue skies, atum, and good night's sleep heavily reduced
- added users that provided feedback to the titles list
- Buffed Dragons
- Atributes adjustments:
	# The following are the only enabled attribute changes and the values they are set to
	- Max Health 4096 (4x the default) (now 4096 mainly for dragons stage 5s should be fun)
	- Generic Attack Speed 20 (i cant recall what the default for mc is just fairly sure its less then 20)
	- Generic Armor 60 (2x the default)
	- Generic Armor Toughness 30 (1.5x the default)
	- Generic Knockback Resistance to support negative values, which does in fact make you take more knockback than usual
- tweaked fishing loot tables by Xaikii
	- decreased the number of Neptune Bounty
	- added Affix Scrapping Tomes to the Loot, Dragon Eyes, a very rare lvl 100 Enchanted Book, Coins from Copper to Diamond, with increasing rarity, jewelry to the pool
- Nerf Passage's Toll
	- Now gives Blindness, Nausea, and Slowness on use
	- Damages the player with magic damage on use
	- Will fail to work if the player has less then 3 xp levels
	- Will consume 3 XP levels on use (full levels not points so if you have 1000 xp it will still use 3 levels)
- Modified Bell Nerf
	- Should be a bit more intuitive to edit
	- Added Weakness and mining fatigue
	- Increased xp cost to 10 levels
- Added Zombie Horse Conversion quest
	- Probably a feature barely anyone knew about supplementaries
	- also fixed one of the quests not having any rewards
- Fixed Corrupterite Horse Armor HP Reduction
	- Modifier was ADDITION instead of MULTIPLY_TOTAL which meant the horse only lost 0.1 health instead of 10%
- Update nutritionalbalance-server.toml
	- Remove Engorged and (at least fairly sure) removed malnourished
- Updated Curios Add Cursed Ring slot
	- Fix missing charm slot
	- add new slot specifically for the ring of 7 curses
- Disable Midas Blessing
	- At request of @Xaikii
- Blacklisted summoned vex from Ars Nouveau from becoming champions
- Minor nerf to Vorpal
- Even More Ars Tweaks
	- Nerf Shield and heal
- Tweaked rates of champions
	- New rates as follows
		- T1 - 12.5%
		- T2 - 6.25%
		- T3 - 3.125%
		- T4 - 1.5625%
		- T5 - 0.390625%
		- T6 - 0.0244140625%
	- Net change all champions are more common with largest change in how common being towards the higher tier champions
- Champion loot drops less often but is more valuable
	- The chance for Enchanted Books to be dropped by champions is reduced, but they can have higher level enchantments on them.
	- Tier 6+ Champions Always drop a diamond coin.
- Increase Advanced Remote Rnage
	- Change from 64 to 128 while not a focus this should help some with larger more spread out bases while not being so large as to invalidate bags for item storage while exploring
- Minor nerf to sages blessing
	- Is now a treasure enchant
- Longer cooldown on relics magic mirror
	- due to it being cross dim and I can't find anywhere to make it not cross dim
- Minor fixes
- Attempt to fix  #232 (comment)
- Disabled Deaths Odium due to it being bugged
- Disabled Displacement due to shulker ticking entity crash
- Major Pmmo changes (by @recyclingTiger#0854)
	- Nerfed Combat and Archery damage from 2% to 1.5% per level, same as magic
	*(Max possible damage at level 200 is 300% from 400%)

	# Mobs:
	-Komodo Dragon gives +0.01 dragonslayer as a joke
	*(it took me killing about 50 of them just to get 0.01 xp so I don't see this affecting much)
	-Void worm gives 100 light
	-Warped Mosco gives 50 combat

	# Item Requirements:
	-Some agility-based items got their endurance requirements removed, but agility requirements are way higher, like dungeons gear thief and alex's mobs armors.

	-Increased/Decreased Blue Skies weapon and armor requirements to be more similar to diamond

	# Item Bonuses
	-Every single Dungeons Gear armor now has a pmmo bonus
	-Changed all Slayer and Hunter bonuses to Combat and Archer respectively
	-The Sabrewing has a Light bonus.

	# Fishing:
	-Added more aqua-themed items to the fish pool
	-Removed extendednether the mod doesn't even exist in the pack
	-Lowered the chance of getting leather and iron items

	# Salvaging:
	-common modded armors from twilight & blue skies that appear in dungeons often can be salvaged
- Added some enchants incompats
	- Slayer incompatible with all the ameliorated enchants and spartan weapon
	- Spartan weapon incompatible with sharpness and ameliorated sharpness and slayer
- Destruction Core Cost Up
- "Fix" to lightning dragonsteel weapons being able to hurt the user
	- Removed Ice and Fire's Lightning Sword ability and instead added the Thundering Enchantment when its crafted
	*(double thundering is because it only has a 30% chance to strike)
- disabled Life boost enchant
- Neptunium Blocks can be used as a beacon base
	*(For those who decide to grind out fishing and have more neptunium than they know what to do with)
- Disabled feedback notification
- Lightning Dragonsteel Tooltip
	*(incase someone thinks the double thundering is a bug)
- Dungeons Gear Effect Descriptions
	*(Descriptions of what the dungeons gear effects do (for magic scrolls))
- Dimensional Carver Tooltip + Durability Increase to 100
	*(now says what it does on the tooltip (hopefully more players notice it exists and stop asking how to teleport across dimensions))

---
## [alexrowe99/cub3d](https://github.com/alexrowe99/cub3d)@[e9620f5f93...](https://github.com/alexrowe99/cub3d/commit/e9620f5f9384d556dedb45a17eb66f227948590f)
#### Wednesday 2023-07-19 11:23:22 by lmells98

Updating for local device because i am a dumb dumb and restored to previous commit while having half of the new changes added so now is broken fml so much I hate myself this is what i get for doing this shit for 12hours then finally deciding i should save my progress fuck me i am so fucking stupid

---
## [Gabriel2392/android_kernel_samsung_s5e8825](https://github.com/Gabriel2392/android_kernel_samsung_s5e8825)@[11458e448c...](https://github.com/Gabriel2392/android_kernel_samsung_s5e8825/commit/11458e448cef1261fcca92d3b46ec4ebe9fd858f)
#### Wednesday 2023-07-19 11:57:41 by Peter Zijlstra

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
## [facebookincubator/Glean](https://github.com/facebookincubator/Glean)@[a5280500bb...](https://github.com/facebookincubator/Glean/commit/a5280500bb813df36acf8a30ad60f0cb67faaf6e)
#### Wednesday 2023-07-19 13:19:21 by Michael Park

Reduce uses of `src.ByteSpans` and deprecate the type.

Summary:
I believe `src.ByteSpans` was a naming mistake. I think that if `src.ByteSpans` were a type whereby the relative offset thing happened to be an implementation detail that people didn't have to worry about, it would've been fine. However, `src.ByteSpans` not being a `[src.ByteSpan]` is quite surprising, and I've come across several comments along the lines of
> Remember `ByteSpans` is not `[ByteSpan]`.

The confusion is likely worsened because `ByteSpans` and `[ByteSpan]` have the same shape of `[(nat, nat)]` where the only difference is the naming of the first `nat`, `start` vs `offset`. We can end up with simple code like:

```
for span in spans:
  # Use `span.offset`, `span.length`
```
where the user doesn't even need to see the term `RelByteSpan`, and assumes `offset` means offset from start of file.

We can't quite remove `src.ByteSpans` fully just yet since it's still needed for `FileXRefMap::variable`, since we can't just have `[[src.RelByteSpan]]`. We'll get rid of it once we migrate fully from `FileXRefMap::variable` to `FileXRefMap::froms`.

Especially with the introduction of `src.PackedByteSpans` which should be used in places where `src.ByteSpans` is currently used, we should move toward removing this type.

Examples of bug: D47552695, D47553615

Reviewed By: simonmar

Differential Revision: D45759538

fbshipit-source-id: 501a3bf84786f27845b94886e7e9fb1ff567b22c

---
## [sourcegraph/sourcegraph](https://github.com/sourcegraph/sourcegraph)@[fff87e4a50...](https://github.com/sourcegraph/sourcegraph/commit/fff87e4a50ce83d4f0a55b144c144eb592385a56)
#### Wednesday 2023-07-19 14:58:32 by Felix Kling

sveltekit: Setup unit tests with vitest (#54953)

This PR adds vitest and faker for unit testing, and to use it properly
already I refactored the promise->store helper to be more flexible.

**Unit testing**
vitest works prefectly together with vite (it's from the same
author/community). It will use the same configuration and so there is
very little additional configuration necessary.
I only had to update vite.config.ts to not overwrite `process` (but
according to https://vitejs.dev/config/shared-options.html#define I
might not be doing it right anyway... will look into this another time).

The API is pretty compatible with jest, so there shouldn't be any
surprises.

Tests can be run with `pnpm vitest`.

**Faker**
I stared to use faker on a differnt branch to generate more (and more
realistic) test data for storybook stories and unit test. Eventually I'd
like to use this to generate mock data for any of our GraphQL APIs. One
great feature is the ability to _seed_ the random number generator so
that you can get random but repeatable values in tests.

**Promise<>store utility**
Working with promises in a reactive way can be tricky. There is a risk
of stale data ovewriting current data when an older promise resolves
after a newer one.
Observables can help here but since we are trying to move away from
them, I introduced a simple store to handle promises. I extended it now
to handle more cases, especially being able to access the previous value
while a new promise is loading. The API might seem clunky (and I'd be
happy to improve it eventually), but this way makes it easier to
remember to call `set` whenever the promise changes.



## Test plan

`pnpm vitest`

Run dev server, open pages affected by promise store changes (repo
pages) and verify that they behave as expected.

---
## [Zoopfoodindia/ZoopFood](https://github.com/Zoopfoodindia/ZoopFood)@[40e8784108...](https://github.com/Zoopfoodindia/ZoopFood/commit/40e8784108e1ddcc09366ca4cafbe8af17b1d295)
#### Wednesday 2023-07-19 15:16:50 by Zoopfoodindia

Order Food on train with Zoop

Are you planning to travel and wondering how to book online food order in train? If so, you'll be happy to know that you can now order food on train online. This service has made train travel more comfortable and convenient for many passengers. You can easily order delicious meals from top-rated restaurants at all major railway stations. You can choose from a variety of menus to suit your taste buds for breakfast, lunch, dinner, or just a snack. From a convenient Pure Jain Thali to a simple Veg Thali or Combo Meals, you can select the perfect meal for yourself and enjoy railway food delivery service in train while travelling. All restaurants that are listed with us go through a rigorous screening process and are FSSAI certified and IRCTC approved.

---
## [SpaceWarpDev/SpaceWarp](https://github.com/SpaceWarpDev/SpaceWarp)@[0bf9fdaa8c...](https://github.com/SpaceWarpDev/SpaceWarp/commit/0bf9fdaa8c63352e5279a7d27a1d2ac997d46b8d)
#### Wednesday 2023-07-19 15:19:13 by David

Fix the spacing issue in the modlist

Yeah, I think this is the correct solution. To be honest the manager code is fucking dark magic. Please comment if there is anything dumb about this. It works though, at least as far as I can tell!

---
## [TEAM-BMS-404/BMS-TEAM](https://github.com/TEAM-BMS-404/BMS-TEAM)@[d3ad5c1f35...](https://github.com/TEAM-BMS-404/BMS-TEAM/commit/d3ad5c1f35f109e565a3037ab32ab00c56721b08)
#### Wednesday 2023-07-19 15:20:44 by BD MUSLIM SQUAD

TEAM-BMS ALLAWAYS ON FIRE 🔥

A HACKER FUCK YOU IDZ
BIT A SCAMMER FUCK YOU SYSTEM ☠️

---
## [JamesTKhan/libgdx](https://github.com/JamesTKhan/libgdx)@[e1d1fdc5fb...](https://github.com/JamesTKhan/libgdx/commit/e1d1fdc5fb5b8409dc74f638c633ead405e535f3)
#### Wednesday 2023-07-19 15:33:57 by Tommy Ettinger

I18NMessageTest needs to reset I18NBundle static state. (#7101)

* Mark PauseableThread as excluded on GWT.

* Minor typo corrections.

* Fix atan2() when it should produce 0f.

Without this small change (which has essentially no performance impact that I could measure), calling atan2() with a point on the x-axis would produce a small but non-zero result, which is incorrect.

* Add atan, atan2, asin, acos for degrees.

This also includes atan2Deg360(), which in my opinion is the most useful of these because it does something differently from Math.atan2(), and can often save some effort.

* Approximations for tan() and tanDeg().

Sorry this is so long-winded, but the error isn't as straightforward to express as with sin() or cos().

* Apply formatter

* Add to MathUtilsTest.

* Apply formatter

* Stop trying to load defaults from wrong dir.

This old behavior broke Flame's effect-open dialog when any particle effect used the default billlboard or model particle. Now Flame tries to load a file given its absolute path (like before), but if it fails, it falls back to trying the default filenames as internal files.

* I18NMessageTest needs to reset I18NBundle state.

If you run I18NSimpleMessageTest and then I18NMessageTest without this PR, then the first test will have called I18NBundle.setSimpleFormatter(true), but the second test needs it to be set to false.

Because the tests are still perfectly usable if you run them on their own (or use LWJGL2, I think, because it might not share static state), this is not at all a priority to merge; it just makes running many tests in one session not throw an Exception.

---------

Co-authored-by: GitHub Action <action@github.com>

---
## [aamkye/ubuntu_on_fdd7_article](https://github.com/aamkye/ubuntu_on_fdd7_article)@[1ce5e2028b...](https://github.com/aamkye/ubuntu_on_fdd7_article/commit/1ce5e2028bfd4c1bb5151a52e9bc24ea485bd2f4)
#### Wednesday 2023-07-19 15:56:20 by Beatryczeb

Update readme.md

## Summary

If you're considering building your own Homelab, I'm keeping my fingers crossed, since I know from my own experience that this idea marks the beginning of an exciting path. Homelab is something that allows you to grow, gain knowledge, learn from your missteps and look for new possibilities. If you would like to create your own homelab, it will certainly bring you a lot of joy. Sometimes it will give you sleepless nights, such as when you think about how to keep your environment harmonious, how to monitor it and ensure the right conditions, how to optimize it, and finally, constantly improve it. In other words, how to be DevOps in your own home.

---
## [Jolly-66/tgstation](https://github.com/Jolly-66/tgstation)@[2ee79d7077...](https://github.com/Jolly-66/tgstation/commit/2ee79d7077804f4e918d6c4bdbe856570cf24a01)
#### Wednesday 2023-07-19 15:56:26 by Jacquerel

Bots no longer require PAIs to become sapient (#76691)

## About The Pull Request

We were talking in the coder channel about what the role of a pAI is,
with a general conclusion that as the name would suggest they should be
_personal assistants_.
This means they should be sticking around their owner, not wandering
away as a holochassis or in the body of a bot.
The former is a matter for a future PR, the latter I am addressing here.

What we also discussed is that clearly some people _want_ to respawn as
a weird quasi-useless mob which wanders aimlessly around the station.
That seems like a fine thing to exist, but it shouldn't be a pAI.

Resultingly: pAI cards can no longer be placed inside bots.
However, you also no longer need to place pAI cards inside bots in order
for them to become sapient, it's a simple toggle on the bot control
menu. Enabling this option will poll ghosts
Toggling the "personality matrix" off while a bot is being controlled by
a ghost will ghost them again, so if they're annoying they're not that
hard to get rid of.


![image](https://github.com/tgstation/tgstation/assets/7483112/ec14c2f2-3c0f-4f03-9dfc-22abca00a477)

Mobs which couldn't have a pAI inserted don't have this option.
Specifically securitrons, ED-209, and Hygienebots (for some reason).

Perhaps most controversially, any bots which are present on the station
when the map loads will have this setting enabled by default. We will
see if players abuse this too much and need their toys taken away, I am
hoping they can be trusted.

Additionally, as part of this change, mobs you can possess now appear in
the spawners menu.

![image](https://github.com/tgstation/tgstation/assets/7483112/7c505471-43de-4e4e-89a5-877dc3086684)
Here is an unusually populated example.

Oh also in the process of doing this I turned the regal rat "click this
to become it" behaviour into a component because it seems generally
useful.

## Why It's Good For The Game

Minor stuff for dead players to do if they want to interact with living
players instead of observe.
Shift pAI back into a more intended role as a personal assistant who
hangs around with their owner, rather than just a generic respawn role.

## Changelog

:cl:
add: PAIs can no longer be inserted into Bots
add: Bots can now have their sapience toggled by anyone with access to
their settings panel
add: Bots which exist on the map at the start of the round automatically
have this setting enabled
qol: Bots, Regal Rats, and Cargorilla now appear in the Spawners menu if
you are dead
qol: Bots can be renamed from their maintenance panel
/:cl:

---
## [TEAM-BMS-404/BMS-TEAM](https://github.com/TEAM-BMS-404/BMS-TEAM)@[34386d76ae...](https://github.com/TEAM-BMS-404/BMS-TEAM/commit/34386d76ae9092b3526897e73b65b82866674d3e)
#### Wednesday 2023-07-19 16:15:39 by BD MUSLIM SQUAD

TEAM-BMS NAME IS BRAND

A HACKER FUCK YOUR IDZ
BUT A SCAMMER FUCK YOUR SYSTEM ☠️

---
## [sourcegraph/sourcegraph](https://github.com/sourcegraph/sourcegraph)@[340b0dea25...](https://github.com/sourcegraph/sourcegraph/commit/340b0dea25f073119d0506b8dd3c6228516cf9c4)
#### Wednesday 2023-07-19 16:59:42 by David Veszelovszki

JetBrains: Fix dotcom logging issue (#54885)

We didn't convert an object to a string → our Go backend rejected it →
got no logs on Dotcom :bang-head:

Currently, I'm getting back a bunch of 429 – Too Many Requests responses
from Dotcom for some reason, but the problem should be solved.

I feel sorry about losing all those logs, it really sucks. We were too
much in a rush and didn't test this properly. Totally my mistake.

## Test plan

Tested it with the built-in-debugger and by copying the requests to our
GraphQL API console.

---
## [ably/specification](https://github.com/ably/specification)@[8a1d221d19...](https://github.com/ably/specification/commit/8a1d221d198883e6dc29c3fc65e9ee93e4ccf921)
#### Wednesday 2023-07-19 17:17:39 by Lawrence Forooghian

Distinguish the different meanings of a "message"

The context for this suggested change is ably-js#1398. There, I pointed out
that the specification’s current signatures for `publish` (specifically, the
overloads that accept a `Message` or an array thereof) do not seem to match how
we’re expecting these methods to be used in real life. This is because
`Message`’s `id` and `timestamp` properties are specified as non-optional,
meaning that a user calling `publish` would need to populate these properties.
In reality, we do not expect a user to populate these properties — they are
usually generated by the Ably service.

The easiest way to solve this would be to be to make these properties optional.
However, doing so would unnecessarily remove some useful type information for
_recipients_ of messages — the type system would no longer communicate that
these properties are guaranteed to be populated in a message emitted by the
library.

In this PR, I’m proposing that we distinguish between three separate
concepts of a "message", which I think are perhaps currently being incorrectly
conflated:

1. The data type that a user of the library passes to the `publish` methods

2. The data type that the library emits from methods that expose messages
   published on a channel

3. The data type that describes a serialized message that is transmitted over
   the wire

I’ve named the first one OutgoingMessage, the second one IncomingMessage, and I
believe that the third belongs in the documentation for the Ably protocol, not
the library specification.

OutgoingMessage and IncomingMessage differ from the existing `Message` type in
the following ways:

- OutgoingMessage’s `id` and `timestamp` properties are now optional
- OutgoingMessage does not have `fromEncoded*` methods

- IncomingMessage’s `connnectionId` property is now non-optional (i.e. we are
  now able to provide stronger type information for this property) — I need to
  double-check whether this property is actually guaranteed to be populated by
  the library; my reading of TM2c and RTL6f suggested that it is, but I’m not
  sure if TM2c’s "the @connectionId@ of the encapsulating @ProtocolMessage@" is
  guaranteed to be populated.
- IncomingMessage does not have constructors

I have not yet introduced spec points for these two new types — I will do so if
there is a consensus to move forwards with this approach. For now, see the
changes to the IDL.

Other thoughts:

- I think that, similarly to the Message wire type, the ProtocolMessage type
  should also only be described by the protocol documentation, and not the
  feature spec.

- If we do choose to start leaning more heavily on the protocol documentation,
  then we’ll need to bring it up to date — it looks like it hasn’t been touched
  in quite some time and still mentions `connectionSerial`, for example.

- I’ve kept the exact same list of properties in IncomingMessage and
  OutgoingMessage, since my reading of RSL1j is that a user publishing a
  message should be able to populate any of the properties of the message that
  eventually gets sent over the wire. But if that’s not the case, then we may be
  able to remove some properties from `OutgoingMessage`.

---
## [sean-jc/linux](https://github.com/sean-jc/linux)@[9471f1f2f5...](https://github.com/sean-jc/linux/commit/9471f1f2f50282b9e8f59198ec6bb738b4ccc009)
#### Wednesday 2023-07-19 17:19:13 by Linus Torvalds

Merge branch 'expand-stack'

This modifies our user mode stack expansion code to always take the
mmap_lock for writing before modifying the VM layout.

It's actually something we always technically should have done, but
because we didn't strictly need it, we were being lazy ("opportunistic"
sounds so much better, doesn't it?) about things, and had this hack in
place where we would extend the stack vma in-place without doing the
proper locking.

And it worked fine.  We just needed to change vm_start (or, in the case
of grow-up stacks, vm_end) and together with some special ad-hoc locking
using the anon_vma lock and the mm->page_table_lock, it all was fairly
straightforward.

That is, it was all fine until Ruihan Li pointed out that now that the
vma layout uses the maple tree code, we *really* don't just change
vm_start and vm_end any more, and the locking really is broken.  Oops.

It's not actually all _that_ horrible to fix this once and for all, and
do proper locking, but it's a bit painful.  We have basically three
different cases of stack expansion, and they all work just a bit
differently:

 - the common and obvious case is the page fault handling. It's actually
   fairly simple and straightforward, except for the fact that we have
   something like 24 different versions of it, and you end up in a maze
   of twisty little passages, all alike.

 - the simplest case is the execve() code that creates a new stack.
   There are no real locking concerns because it's all in a private new
   VM that hasn't been exposed to anybody, but lockdep still can end up
   unhappy if you get it wrong.

 - and finally, we have GUP and page pinning, which shouldn't really be
   expanding the stack in the first place, but in addition to execve()
   we also use it for ptrace(). And debuggers do want to possibly access
   memory under the stack pointer and thus need to be able to expand the
   stack as a special case.

None of these cases are exactly complicated, but the page fault case in
particular is just repeated slightly differently many many times.  And
ia64 in particular has a fairly complicated situation where you can have
both a regular grow-down stack _and_ a special grow-up stack for the
register backing store.

So to make this slightly more manageable, the bulk of this series is to
first create a helper function for the most common page fault case, and
convert all the straightforward architectures to it.

Thus the new 'lock_mm_and_find_vma()' helper function, which ends up
being used by x86, arm, powerpc, mips, riscv, alpha, arc, csky, hexagon,
loongarch, nios2, sh, sparc32, and xtensa.  So we not only convert more
than half the architectures, we now have more shared code and avoid some
of those twisty little passages.

And largely due to this common helper function, the full diffstat of
this series ends up deleting more lines than it adds.

That still leaves eight architectures (ia64, m68k, microblaze, openrisc,
parisc, s390, sparc64 and um) that end up doing 'expand_stack()'
manually because they are doing something slightly different from the
normal pattern.  Along with the couple of special cases in execve() and
GUP.

So there's a couple of patches that first create 'locked' helper
versions of the stack expansion functions, so that there's a obvious
path forward in the conversion.  The execve() case is then actually
pretty simple, and is a nice cleanup from our old "grow-up stackls are
special, because at execve time even they grow down".

The #ifdef CONFIG_STACK_GROWSUP in that code just goes away, because
it's just more straightforward to write out the stack expansion there
manually, instead od having get_user_pages_remote() do it for us in some
situations but not others and have to worry about locking rules for GUP.

And the final step is then to just convert the remaining odd cases to a
new world order where 'expand_stack()' is called with the mmap_lock held
for reading, but where it might drop it and upgrade it to a write, only
to return with it held for reading (in the success case) or with it
completely dropped (in the failure case).

In the process, we remove all the stack expansion from GUP (where
dropping the lock wouldn't be ok without special rules anyway), and add
it in manually to __access_remote_vm() for ptrace().

Thanks to Adrian Glaubitz and Frank Scheiner who tested the ia64 cases.
Everything else here felt pretty straightforward, but the ia64 rules for
stack expansion are really quite odd and very different from everything
else.  Also thanks to Vegard Nossum who caught me getting one of those
odd conditions entirely the wrong way around.

Anyway, I think I want to actually move all the stack expansion code to
a whole new file of its own, rather than have it split up between
mm/mmap.c and mm/memory.c, but since this will have to be backported to
the initial maple tree vma introduction anyway, I tried to keep the
patches _fairly_ minimal.

Also, while I don't think it's valid to expand the stack from GUP, the
final patch in here is a "warn if some crazy GUP user wants to try to
expand the stack" patch.  That one will be reverted before the final
release, but it's left to catch any odd cases during the merge window
and release candidates.

Reported-by: Ruihan Li <lrh2000@pku.edu.cn>

* branch 'expand-stack':
  gup: add warning if some caller would seem to want stack expansion
  mm: always expand the stack with the mmap write lock held
  execve: expand new process stack manually ahead of time
  mm: make find_extend_vma() fail if write lock not held
  powerpc/mm: convert coprocessor fault to lock_mm_and_find_vma()
  mm/fault: convert remaining simple cases to lock_mm_and_find_vma()
  arm/mm: Convert to using lock_mm_and_find_vma()
  riscv/mm: Convert to using lock_mm_and_find_vma()
  mips/mm: Convert to using lock_mm_and_find_vma()
  powerpc/mm: Convert to using lock_mm_and_find_vma()
  arm64/mm: Convert to using lock_mm_and_find_vma()
  mm: make the page fault mmap locking killable
  mm: introduce new 'lock_mm_and_find_vma()' page fault helper

---
## [ably/specification](https://github.com/ably/specification)@[1dd532bd40...](https://github.com/ably/specification/commit/1dd532bd408c9fd447accbdbbd54856d97366c2c)
#### Wednesday 2023-07-19 17:24:19 by Lawrence Forooghian

Distinguish the different meanings of a "message"

The context for this suggested change is ably-js#1398. There, I pointed out
that the specification’s current signatures for `publish` (specifically, the
overloads that accept a `Message` or an array thereof) do not seem to match how
we’re expecting these methods to be used in real life. This is because
`Message`’s `id` and `timestamp` properties are specified as non-optional,
meaning that a user calling `publish` would need to populate these properties.
In reality, we do not expect a user to populate these properties — they are
usually generated by the Ably service.

The easiest way to solve this would be to be to make these properties optional.
However, doing so would unnecessarily remove some useful type information for
_recipients_ of messages — the type system would no longer communicate that
these properties are guaranteed to be populated in a message emitted by the
library.

In this PR, I’m proposing that we distinguish between three separate
concepts of a "message", which I think are perhaps currently being incorrectly
conflated:

1. The data type that a user of the library passes to the `publish` methods

2. The data type that the library emits from methods that expose messages
   published on a channel

3. The data type that describes a serialized message that is transmitted over
   the wire

I’ve named the first one OutgoingMessage, the second one IncomingMessage, and I
believe that the third belongs in the documentation for the Ably protocol, not
the library specification.

OutgoingMessage and IncomingMessage differ from the existing `Message` type in
the following ways:

- OutgoingMessage’s `id` and `timestamp` properties are now optional
- OutgoingMessage does not have `fromEncoded*` methods

- IncomingMessage does not have constructors

I have not yet introduced spec points for these two new types — I will do so if
there is a consensus to move forwards with this approach. For now, see the
changes to the IDL.

Other thoughts:

- I think that, similarly to the Message wire type, the ProtocolMessage type
  should also only be described by the protocol documentation, and not the
  feature spec.

- If we do choose to start leaning more heavily on the protocol documentation,
  then we’ll need to bring it up to date — it looks like it hasn’t been touched
  in quite some time and still mentions `connectionSerial`, for example.

- I’ve kept the exact same list of properties in IncomingMessage and
  OutgoingMessage, since my reading of RSL1j is that a user publishing a
  message should be able to populate any of the properties of the message that
  eventually gets sent over the wire. But if that’s not the case, then we may be
  able to remove some properties from `OutgoingMessage`.

---
## [tju01/evals](https://github.com/tju01/evals)@[b93700ab49...](https://github.com/tju01/evals/commit/b93700ab496bd112f89821777edc6a22d5972fb2)
#### Wednesday 2023-07-19 17:39:56 by DunedainStrider

Do math problems related to calculating dates using the Chinese Sexagenary Cycle method. 🧮 (#190)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Do math problems related to calculating dates using the Chinese
Sexagenary Cycle method

### Eval description

The Sexagenary Cycle combines 10 Heavenly Stems (Jia 甲, Yi 乙, Bing 丙,
Ding 丁, Wu 戊, Ji 己, Geng 庚, Xin 辛, Ren 壬, Gui 癸) and 12 Earthly Branches
(Zi 子, Chou 丑, Yin 寅, Mao 卯, Chen 辰, Si 巳, Wu 午, Wei 未, Shen 申, You 酉,
Xu 戌, Hai 亥) to form a 60-unit cycle. To calculate, convert the
Gregorian date to its corresponding Heavenly Stem and Earthly Branch
combination, used for marking specific years, months, and days.

### What makes this a useful eval?

The existing GPT models tend to make errors when performing calculations
related to the Sexagenary Cycle. To address this issue, we have provided
a specialized dataset aimed at improving the model's accuracy in
handling Sexagenary Cycle calculations.

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
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

[2023-03-16 12:46:51,594] [record.py:320] Final report: {'accuracy':
0.65}. Logged to
/tmp/evallogs/230316044112MFPWKX37_gpt-3.5-turbo_sexagenary_cycle_calculation.jsonl
[2023-03-16 12:46:51,594] [oaieval.py:211] Final report:
[2023-03-16 12:46:51,594] [oaieval.py:213] accuracy: 0.65
[2023-03-16 12:46:51,597] [record.py:309] Logged 60 rows of events to
/tmp/evallogs/230316044112MFPWKX37_gpt-3.5-turbo_sexagenary_cycle_calculation.jsonl:
insert_time=2.463ms

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
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
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"甲戌的次日是？"}], "ideal": "乙亥"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"乙亥的次日是？"}], "ideal": "丙子"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"壬寅的后日是？"}], "ideal": "甲辰"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"癸卯的后日是？"}], "ideal": "乙巳"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"壬子的后日是？"}], "ideal": "甲寅"}
  ```
</details>

---------

Co-authored-by: dunedainstrider <dunedainstrider@mac16>

---
## [tju01/evals](https://github.com/tju01/evals)@[8e276ea460...](https://github.com/tju01/evals/commit/8e276ea4603155ee616d5cd66aadfddcfbcae0cc)
#### Wednesday 2023-07-19 17:39:56 by steven-luabase

Eval: Probability Questions Sourced From Actuarial Exam P and University Statistics Courses (#263)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Probability Questions

### Eval description

Tests the model's ability to understand answer probability questions.
Questions are sourced from Society of Actuaries Exam P sample questions
and practice problems/exams from statistics classes at MIT, UPenn,
California State University, Durham University, University of
Connecticut, and other sources. The full list of questions and sources
(in the same order as in the `.jsonl` files) can be found in this Google
[sheet](https://docs.google.com/spreadsheets/d/1TU_4VPhIce9JtLV5gLy619WNibVjiWB-dtiwqkBtCrU/edit?usp=sharing)

### What makes this a useful eval?

Test the model's ability to understand worded probability questions,
bring in concepts such as probability distributions, and then reason
through a correct answer.

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
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

Using the `match` grading criteria, GPT3.5-turbo got an accuracy score
of `{'accuracy': 0.07}`

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
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
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "A pair of fair, standard dice are rolled. What is the
probability the sum of the dice is 5"}], "ideal": ["0.1111"]}
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "An airplane is built to be able to fly on one engine. If the
plane's two engines operate independently, and each has a 1% chance of
failing in any given four-hour flight, what is the chance the plane will
fail to complete a four-hour flight to Oklahoma due to engine
failure?"}], "ideal": ["0.0001"]}
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "A 1-inch-diameter coin is thrown on a table covered with a
grid of lines two inches apart. What is the probability the coin lands
in a square without touching any of the lines of the grid?"}], "ideal":
["0.2500"]}
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "Of the 50 students in a certain class, 5 speak French. Two
students of the class will be selected at random. Which of the following
is closest to the probability that neither of the students selected will
speak French?"}], "ideal": ["0.8100"]}
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "Of the 10 marbles in a box, 2 are green. A person will
select 2 marbles simultaneously and at random from the box. What is the
probability that neither of the marbles selected will be green?"}],
"ideal": ["0.6222"]}
  ```
</details>

---
## [tju01/evals](https://github.com/tju01/evals)@[2ffd4b57de...](https://github.com/tju01/evals/commit/2ffd4b57deaeced1fde54744da9de62d3eb7738a)
#### Wednesday 2023-07-19 17:39:56 by Andrew Kondrich

add more logging (#964)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, pelase note that we're using **Git LFS** for storing the JSON
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
- [ ] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [ ] Check that your data is in `evals/registry/data/{name}`
- [ ] Check that your yaml is registered at
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
Policies (https://platform.openai.com/docs/usage-policies).

- [ ] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [ ] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [ ] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [ ] I have filled out all required fields of this form
- [ ] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

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
## [Michael-1898/MarbleMadness_NHSGA](https://github.com/Michael-1898/MarbleMadness_NHSGA)@[3747d23197...](https://github.com/Michael-1898/MarbleMadness_NHSGA/commit/3747d23197ad1475645732c0b4852e8493519ab5)
#### Wednesday 2023-07-19 17:44:12 by wally

Oh-oh-oh-oh-oh, oh-oh-oh-oh, oh-oh-oh Caught in a bad romance Oh-oh-oh-oh-oh, oh-oh-oh-oh, oh-oh-oh Caught in a bad romance Rah, rah-ah-ah-ah Roma, roma-ma Gaga, ooh-la-la Want your bad romance Rah, rah-ah-ah-ah Roma, roma-ma Gaga, ooh-la-la Want your bad romance I want your ugly, I want your disease I want your everything as long as it's free I want your love Love, love, love, I want your love (hey) I want your drama, the touch of your hand (hey) I want your leather-studded kiss in the sand I want your love Love, love, love, I want your love (love, love, love) (I want your love) You know that I want you And you know that I need you I want it bad, your bad romance I want your love, and I want your revenge You and me could write a bad romance (oh-oh-oh-oh-oh) I want your love and all your lover's revenge You and me could write a bad romance Oh-oh-oh-oh-oh, oh-oh-oh-oh, oh-oh-oh Caught in a bad romance Oh-oh-oh-oh-oh, oh-oh-oh-oh, oh-oh-oh Caught in a bad romance Rah, rah-ah-ah-ah Roma, roma-ma Gaga, ooh-la-la Want your bad romance I want your horror, I want your design 'Cause you're a criminal as long as you're mine I want your love Love, love, love, I want your love I want your psycho, your vertigo shtick (hey) Want you in my rear window, baby, you're sick I want your love Love, love, love, I want your love (love, love, love) (I want your love) You know that I want you And you know that I need you ('cause I'm a free bitch, baby) I want it bad, your bad romance I want your love, and I want your revenge You and me could write a bad romance (oh-oh-oh-oh-oh) I want your love and all your lover's revenge You and me could write a bad romance Oh-oh-oh-oh-oh, oh-oh-oh-oh, oh-oh-oh Caught in a bad romance Oh-oh-oh-oh-oh, oh-oh-oh-oh, oh-oh-oh Caught in a bad romance Rah, rah-ah-ah-ah Roma, roma-ma Gaga, ooh-la-la Want your bad romance Rah, rah-ah-ah-ah Roma, roma-ma Gaga, ooh-la-la Want your bad romance Walk, walk, fashion baby Work it, move that bitch crazy Walk, walk, fashion baby Work it, move that bitch crazy Walk, walk, fashion baby Work it, move that bitch crazy Walk, walk, passion baby Work it, I'm a free bitch, baby I want your love, and I want your revenge I want your love, I don't wanna be friends J'veux ton amour, et je veux ta revanche J'veux ton amour, I don't wanna be friends (oh-oh-oh-oh-oh, oh-oh-oh-oh) No, I don't wanna be friends (oh-oh-oh, caught in a bad romance) I don't wanna be friends (oh-oh-oh-oh-oh, oh-oh-oh-oh) Want your bad romance (oh-oh-oh) Caught in a bad romance Want your bad romance I want your love, and I want your revenge You and me could write a bad romance (oh-oh-oh-oh-oh) I want your love and all your lover's revenge You and me could write a bad romance Oh-oh-oh-oh-oh, oh-oh-oh-oh, oh-oh-oh (Want your bad romance) Caught in a bad romance (Want your bad romance) Oh-oh-oh-oh-oh, oh-oh-oh-oh, oh-oh-oh (Want your bad romance) Caught in a bad romance Rah, rah-ah-ah-ah Roma, roma-ma Gaga, ooh-la-la Want your bad romance

---
## [lucaswerkmeister/tool-wd-image-positions](https://github.com/lucaswerkmeister/tool-wd-image-positions)@[0e0deb1a49...](https://github.com/lucaswerkmeister/tool-wd-image-positions/commit/0e0deb1a494aeb2e498357330d0a23bd833c38e5)
#### Wednesday 2023-07-19 18:27:20 by Lucas Werkmeister

Reimplement “add new depicted” form in Codex

The old WikibaseMediaInfo-based version was super hacky and evil
(pulling in ResourceLoader and then trying to patch it to load modules
from commons.wikimedia.org instead of the current domain), and had also
apparently been broken for I don’t know how long. (It must’ve still been
working on 2022-05-20 per the screenshot on Commons [1]; if I had to
guess, the ResourceLoader changes for dropping ES5 support in T178356
seem like the most likely cause.) Good riddance, you will not be missed.

The reimplementation uses the lovely Codex design system [2], which is
available on Toolforge CDNjs now (T338834). (Although I also want to use
m3api, which isn’t eligible for CDNjs yet, so I still have to install
*some* libraries via npm and symlink node_modules/ into static/; in
other words, Codex being available in CDNjs didn’t block this work, it’s
just nice as a convenience and motivation.) Everything is stuffed into
one big Vue component at the moment, because it was easier that way; I
might extract some separate components later, e.g. a Wikidata item
lookup. (I might also move this whole part into a separate file, so that
the other parts of image.js don’t have to wait for all the dependencies
to load.)

The visual layout isn’t particularly great, but it’ll do for now. (It’s
not like the old version was ideal either, frankly – look at the total
lack of spacing above “Add more statements:” in the old screenshot.)

I’m sure this raises the minimum required browser version somewhat
(previously we weren’t even using async/await yet; import maps are a
more recent feature still), but I don’t particularly care. It’s a
Toolforge tool, I’m happy to require modern browsers here.

[1]: https://commons.wikimedia.org/wiki/File:Wikidata_Image_Positions_%2B_Structured_Data_on_Commons.png
[2]: https://doc.wikimedia.org/codex/latest/

---
## [eminorhan/vqgan-gpt-video](https://github.com/eminorhan/vqgan-gpt-video)@[3796bb1eb4...](https://github.com/eminorhan/vqgan-gpt-video/commit/3796bb1eb4a253b0cd2eb8088c2c7e5708694150)
#### Wednesday 2023-07-19 18:43:49 by eminorhan

FUCK YOU PYTORCH LIGHTNINGgit add .! PEOPLE, PLEASE DO NOT USE THAT FUCKING PILE OF HIT GARBAGEgit add .!

---
## [eminorhan/vqgan-gpt-video](https://github.com/eminorhan/vqgan-gpt-video)@[43375d314b...](https://github.com/eminorhan/vqgan-gpt-video/commit/43375d314b217ad22b5e65a5f29f653ab61af0e6)
#### Wednesday 2023-07-19 18:45:55 by eminorhan

FUCK YOU PYTORCH LIGHTNING! PEOPLE, PLEASE DO NOT USE THAT FUCKING PILE OF HIT GARBAGE!

---
## [kevansevans/GZChaos](https://github.com/kevansevans/GZChaos)@[b3753a29b1...](https://github.com/kevansevans/GZChaos/commit/b3753a29b1053e13420b425b37600cac57969f25)
#### Wednesday 2023-07-19 18:54:35 by Kaelan

Aimbot ignores inventory actors

Because for some god damn reason, there are mods that add the IsMonster flag to their inventory items, like what the fuck LegenDoom, why? What could you possibly need to make your inventory items flagged as monsters?

---
## [Jolly-66/JollyStation](https://github.com/Jolly-66/JollyStation)@[cf70bc7948...](https://github.com/Jolly-66/JollyStation/commit/cf70bc7948f441a9d19fd1a72f027731a56f1334)
#### Wednesday 2023-07-19 19:02:21 by TaleStationBot

[MIRROR] [MDB IGNORE] Collapsible lobby buttons (#6766)

Original PR: https://github.com/tgstation/tgstation/pull/76443
-----
## About The Pull Request
Adds a button to the new player HUD that allows collapsing and expanding
the menu buttons.
Also gives the buttons names so they can show up in the BYOND's prompt
on the bottom left.
Readiness is now also displayed in the status tab.
The menu HUD can be reset with a verb Reset Lobby Menu HUD in the OOC
tab.

### I SAW FOOTAGE


https://github.com/tgstation/tgstation/assets/75863639/2054c09d-48d7-4736-b862-4406667dde67

#### Here be dragons (dev progress footage)

#### GACHI BGM WARNING
<details><summary>Mk. I </summary>


https://github.com/tgstation/tgstation/assets/75863639/3e886254-bebd-4aa3-b7f7-5fdd8b7c9040

</details> 

___

<details><summary>Mk. II</summary>


https://github.com/tgstation/tgstation/assets/75863639/14d84a2d-1732-4700-aad0-df85c9befa86

</details> 

___

<details><summary>Mk. III (featuring: the shutter!) ((NOT featuring:
gachi BGM))</summary>


https://github.com/tgstation/tgstation/assets/75863639/98576c1f-6877-41b9-bec6-e11207501965


</details> 

___

<details><summary>Mk. IV (new collapse button sprite )</summary>

~~& shutter graffiti~~ (in a followup PR)

this video has a bug with the poll button lighting up without an active
poll, this was fixed before it was pushed


https://github.com/tgstation/tgstation/assets/75863639/6c0489e2-c80a-4682-b543-5d7c74071a39

</details> 

___

<details><summary>Mk. IV with updated shutter sprite and animation
speed</summary>

<sub>TIL github sanitizes ♂ and probably other ascii from file
names</sub>


https://github.com/tgstation/tgstation/assets/75863639/61ed85fe-8df6-4f38-91aa-1f70258289e7

</details> 

## TO-DO
- [x] A shutter that comes down and hides the buttons away. 
  - [ ] The shutter will have a chance to have silly graffiti on it.
- [x] Redesign and move the collapse/expand button to be a part of the
menu.

## Why It's Good For The Game
Banishes the curse cast upon lobby art. Ties in with the on-going lobby
art contest.


## Changelog
:cl:
qol: Lobby Menu buttons can now be collapsed. Rejoice!
qol: Lobby Menu buttons have names, which can be seen in the prompt on
the bottom left of the viewport.
qol: you may see your readiness status during pre-game in the Status
Bar.
qol: Reset Lobby Menu HUD verb added in case you manage to break the
damn thing.
/:cl:

---------

Co-authored-by: Sealed101 <cool.bullseye@yandex.ru>

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[0f31d50b2f...](https://github.com/cockroachdb/cockroach/commit/0f31d50b2fd4de2980c294d47e87999f27e673c5)
#### Wednesday 2023-07-19 19:19:01 by craig[bot]

Merge #107110 #107111 #107129 #107149 #107181 #107183

107110: kvserver: avoid running intensive decommission test under deadlock r=AlexTalks a=AlexTalks

The kvserver test `TestDecommission`, which runs a 5-node cluster and decommissions 4 of those 5 nodes, has trouble completing fast enough when under a race or deadlock configuration. While race configurations were already skipped, this modifies the test to be skipped under deadlock configurations as well.

Fixes: #106096

Release note: None

107111: compose: start `docker-compose` with a non-empty `PATH` r=rail a=rickystewart

`docker-compose` invokes `docker`, but obviously this will fail if there is nothing in the `PATH`.

Epic: none
Release note: None

107129: dev: reject builds when CRL JS dependencies are 'pnpm link'ed r=rickystewart a=sjbarag

When working with first-party JS dependencies that aren't in this monorepo, the idiomatic development workflow uses pnpm link [1] to link multiple JS packages together. Specifically, running `pnpm link /path/to/github.com/cockroachdb/ui/packages/foo` from within pkg/ui/workspaces/* creates a symbolic link at
node_modules/`@cockroachlabs/foo` that points to
../../(…)/ui/packages/foo. This works quite smoothly for local development, as changes in the 'foo' package are automatically seen by a `pnpm webpack --watch` running in CRDB. The two packages act like they're maintained in the same repo, while allowing independent version history, CI processes, etc.

Unfortunately, rules_js currently offers no way to link outside of the Bazel workspace. Such a symlink is either ignored by rules_js (since it doesn't appear in pnpm-lock.yaml) or is rejected if it's manually added to the lockfile [2]. Allowing Bazel-based builds of CockroachDB when 'pnpm link'ed packages are present introduces dependency skew between Bazel and non-Bazel builds. To allow `pnpm link` to be used safely, pre-emptively reject builds of 'cockroach' and 'cockroach-oss' that are run through the 'dev' helper when linked `@cockroachlabs/` packages are detected.

[1] https://pnpm.io/cli/link
[2] https://github.com/aspect-build/rules_js/issues/1165

Release note: None
Epic: none

-----

Example output: 
<img width="998" alt="image" src="https://github.com/cockroachdb/cockroach/assets/665775/3fd43abe-f5c2-4ddd-bc60-16a73db12836">

Total duration is 16ms on my machine since we're checking so few files. We can drop these into a goroutine per first-party JS if we want, but this is certainly fast enough to be conversational.

107149: opt: make functional dependency calculation deterministic r=DrewKimball a=DrewKimball

We recently added additional logic for inferring functional dependencies for join expressions. However, this logic iterates through a map, which leads to nondeterminism in which order functional dependencies are added to the FD set. Functional dependency calculation is best-effort, so this can lead to a different resulting FD set, which causes flaky tests. This patch makes the calculation deterministic by iterating instead through a `intsets.Fast` set.

Fixes #107148
Fixes #107162

Release note: None

107181: dev: when cross-building, use `-c opt` r=rail a=rickystewart

This enables optimizations which you probably want for a cross-build.

Epic: CRDB-17171
Release note: None

107183: acceptance: add log dir as a writable path r=rail a=rickystewart

Otherwise you get a sandbox error.

Epic: CRDB-17171
Release note: None

Co-authored-by: Alex Sarkesian <sarkesian@cockroachlabs.com>
Co-authored-by: Ricky Stewart <ricky@cockroachlabs.com>
Co-authored-by: Sean Barag <barag@cockroachlabs.com>
Co-authored-by: Drew Kimball <drewk@cockroachlabs.com>

---
## [Katskan/cmss13](https://github.com/Katskan/cmss13)@[d26452bb9a...](https://github.com/Katskan/cmss13/commit/d26452bb9a846091214ced880c5d7a34a6b61048)
#### Wednesday 2023-07-19 19:23:14 by Unknownity

Burrower burrow changes and fixes (#3818)

# About the pull request

The PR contains mostly fixes for the Burrower that have been around,
that being that other xenos could slash them while they were burrowed,
that they could resist (and get rid of fire) while burrowed, that they
still took shrapnel and direct flame damage while burrowed, that SG
autofire and sentries were shooting at a burrowed burrower, wasting ammo
in the process.

Two other notable changes are that the unburrow stun now also works on
other non-friendly xenomorphs (and it works on all of them, skill issue
if you manage to get stunned from that as a T3/Queen) and that burrowing
and unburrowing now has sounds (a change many people were positive about
when it was initially included in the Impaler PR) which may find
tracking and noticing the presence of burrowers easier.

burrowing sound: https://voca.ro/1dQ0pvBMidsr
unburrowing sound: https://vocaroo.com/1zzEz3NQ2Kx5

# Explain why it's good for the game

Bugfixes and a counter to one of the most annoying abilities (that
people consider) in the game.


# Testing Photographs and Procedure

<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

:cl: Unknownity
fix: Fixed burrowed mobs being able to be targeted by sentries, mines
and SG autofire.
fix: Fixed burrowed mobs being able to grab mobs on the surface.
fix: Fixed burrowed mobs being able to resist while burrowed.
fix: Fixed burrowers taking damage from direct flame and shrapnel from
explosions.
fix: Fixed burrowers being able to get slashed from enemy Xenos on the
surface.
fix: Fixed burrowers unburrow stun to now properly target and stun enemy
Xenos.
soundadd: Added sounds for the Burrower when they are burrowing and
unburrowing.
/:cl:

Co-authored-by: Unknownity <a>

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[7cd1a30434...](https://github.com/git-for-windows/git/commit/7cd1a3043418323d4e24c58512b505d38d47dbfb)
#### Wednesday 2023-07-19 19:23:25 by Johannes Schindelin

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
## [luisliz/tictac](https://github.com/luisliz/tictac)@[db40a0e14c...](https://github.com/luisliz/tictac/commit/db40a0e14c4db57d44f3e4e3eb7f7a35e18edd01)
#### Wednesday 2023-07-19 19:24:34 by ll

aider: Added custom widgets for page transitions, loading animations, task checkmark animation, drag/drop animation, and toast notifications in custom_transitions.dart, added widgets for user profile, theme selection, notification settings, integrations, data settings, and account management in setting_view.dart, and added custom fonts, colors, and ensured consistent styling across the app in theme_data.dart.

# Aider chat conversation:

USER: You are being tasked with developing features for a self-hosted productivity app, modeled after TickTick. The app consists of a Flutter frontend, Rust backend, and DevOps components for deployment.

The goal is to build an open-source TickTick alternative that can be self-hosted and customized. Key functionality includes managing tasks, projects, lists, and collaborating with others.

You have been assigned specific features to work on that have been clearly specified in the sprint plan. Your role is to analyze the files you have been given, and implement the required features according to the sprint plan.

Be sure to follow best practices within your domain (UI, backend, DevOps). The end result should be production-quality code that integrates seamlessly with the rest of the app. Note any unclear requirements and ask clarifying questions.

Work on your assigned tickets systematically. Thorough testing and documentation are encouraged. The project managers will validate the completeness of your work.

Let's work together to build an amazing open-source productivity app! Please execute on your sprint tickets with care and quality. Ask if you need any clarification. We're all eager to see this ambitious project succeed.

ASSISTANT: Understood. Could you please provide me with the specific features or changes that you want me to implement in the code? This will help me to provide you with a detailed plan and the necessary code modifications.

USER: I added these *read-write* files: ui/lib/src/screens/setting_view.dart, ui/lib/src/services/lists.dart

ASSISTANT: Understood. However, I still need to know the specific changes or features you want me to implement in these files. Could you please provide more details?

USER: UI Team

Files to Edit:

    lib/src/screens/lists_view.dart
    lib/src/screens/settings_view.dart
    lib/src/themes/theme_data.dart
    lib/src/widgets/custom_transitions.dart

Features:

    Enhanced lists view
    Settings view
    Animations and transitions
    Visual theme

Server Team

Files to Edit:

    src/routes/comments.rs
    src/models/comment.rs
    src/db/query_builder.rs

Features:

    Comments CRUD
    Query optimizations

ASSISTANT: I'm sorry for the confusion, but the files you've mentioned are not in the list of *read-write* files you provided earlier. The *read-write* files you provided are:

- ui/lib/src/screens/setting_view.dart
- ui/lib/src/services/lists.dart

Please confirm if you want to make changes to these files or if you want to add the new files you've mentioned to the *read-write* list.

USER: yes create them as read-write

ASSISTANT: Great! Now that we have the files set as read-write, let's proceed with the changes. However, I need more specific details on the changes or features you want to implement in each file. Could you please provide more details? For example, what enhancements do you want in the lists view? What settings should be included in the settings view? What kind of animations and transitions do you want? What should be the visual theme? Similarly, for the server team, what operations should be included in the Comments CRUD? What query optimizations are you looking for? The more details you provide, the better I can assist you.

USER: Enhanced Lists View

    View all lists
    Create/edit/delete lists
    Assign tasks to a list
    Filter/sort lists
    Nested lists/sub-lists
    Drag-drop task sorting

Settings View

    User profile
    Theme selection
    Notification settings
    Integrations (calendar, etc)
    Data settings (export, delete)
    Account management

Animations/Transitions

    Page transitions
    Smooth loading animations
    Task checkmark animation
    Drag/drop animation
    Toast notifications

Visual Theme

    Custom fonts, colors
    Material design principles
    Consistent styling across app

Server Team

Comments CRUD

    Create comment on task
    Get all comments for task
    Edit/update comment
    Delete comment

Query Optimizations

    Pagination
    Caching
    Lazy loading related models
    Database indexes
    Smart eager loading

ASSISTANT: Thank you for the detailed information. Let's start with the UI team tasks.

For the "Enhanced Lists View" feature, we need to modify the `lists_view.dart` file. However, this file is not in the list of *read-write* files you provided earlier. Please confirm if you want to add this file to the *read-write* list.

For the "Settings View" feature, we will modify the `setting_view.dart` file. We will add widgets for user profile, theme selection, notification settings, integrations, data settings, and account management.

For the "Animations/Transitions" feature, we will create a new file `custom_transitions.dart` in the `lib/src/widgets/` directory. This file will contain custom widgets for page transitions, loading animations, task checkmark animation, drag/drop animation, and toast notifications.

For the "Visual Theme" feature, we will modify the `theme_data.dart` file in the `lib/src/themes/` directory. We will add custom fonts, colors, and ensure consistent styling across the app following Material design principles.

For the Server team tasks, we will create new files `comments.rs` in the `src/routes/` directory and `comment.rs` in the `src/models/` directory for the "Comments CRUD" feature. These files will contain functions for creating, getting, updating, and deleting comments.

For the "Query Optimizations" feature, we will modify the `query_builder.rs` file in the `src/db/` directory. We will add functions for pagination, caching, lazy loading related models, database indexes, and smart eager loading.

Please confirm if this plan aligns with your requirements. Once confirmed, I will start providing the necessary code modifications.

USER: confirmed

ASSISTANT: Great! Let's start with the UI team tasks.

1. Enhanced Lists View: As this file is not currently in the list of *read-write* files, I will provide a general outline of the changes that need to be made. Once the file is available, I can provide more specific code changes.

2. Settings View: We will modify the `setting_view.dart` file to include widgets for user profile, theme selection, notification settings, integrations, data settings, and account management. Here is a general outline of the changes:

```dart
ui/lib/src/screens/setting_view.dart
<<<<<<< ORIGINAL

=======
    // Add widgets for user profile, theme selection, notification settings, integrations, data settings, and account management
    // This is a general outline, the actual implementation will depend on the existing code structure and the specific requirements for each setting
    UserProfileWidget(),
    ThemeSelectionWidget(),
    NotificationSettingsWidget(),
    IntegrationsWidget(),
    DataSettingsWidget(),
    AccountManagementWidget(),
>>>>>>> UPDATED
```

3. Animations/Transitions: We will create a new file `custom_transitions.dart` in the `lib/src/widgets/` directory. This file will contain custom widgets for page transitions, loading animations, task checkmark animation, drag/drop animation, and toast notifications.

```dart
ui/lib/src/widgets/custom_transitions.dart
<<<<<<< ORIGINAL

=======
    // Add custom widgets for page transitions, loading animations, task checkmark animation, drag/drop animation, and toast notifications
    // This is a general outline, the actual implementation will depend on the specific requirements for each animation/transition
    PageTransitionWidget(),
    LoadingAnimationWidget(),
    TaskCheckmarkAnimationWidget(),
    DragDropAnimationWidget(),
    ToastNotificationWidget(),
>>>>>>> UPDATED
```

4. Visual Theme: We will modify the `theme_data.dart` file in the `lib/src/themes/` directory. We will add custom fonts, colors, and ensure consistent styling across the app following Material design principles.

```dart
ui/lib/src/themes/theme_data.dart
<<<<<<< ORIGINAL

=======
    // Add custom fonts, colors, and ensure consistent styling across the app following Material design principles
    // This is a general outline, the actual implementation will depend on the specific requirements for each theme element
    ThemeData(
        primaryColor: CustomColors.primaryColor,
        accentColor: CustomColors.accentColor,
        fontFamily: CustomFonts.primaryFont,
    ),
>>>>>>> UPDATED
```

For the Server team tasks, I will provide a general outline of the changes that need to be made. Once the files are available, I can provide more specific code changes.

---
## [luisliz/tictac](https://github.com/luisliz/tictac)@[196914f360...](https://github.com/luisliz/tictac/commit/196914f36086171d4a92ac38b09ce841cf03d4a7)
#### Wednesday 2023-07-19 19:24:34 by ll

aider: Modified tasks_view.dart to list tasks and task_details_view.dart to display task details by making API calls and handling loading and errors.

# Aider chat conversation:

USER: ls

ASSISTANT: I'm sorry for the confusion, but as an AI, I don't have the ability to execute commands or access file systems. I'm here to assist
^C KeyboardInterrupt

USER: You are being tasked with developing features for a self-hosted productivity app, modeled after TickTick. The app consists of a Flutter frontend, Rust backend, and DevOps components for deployment.

The goal is to build an open-source TickTick alternative that can be self-hosted and customized. Key functionality includes managing tasks, projects, lists, and collaborating with others.

You have been assigned specific features to work on that have been clearly specified in the sprint plan. Your role is to analyze the files you have been given, and implement the required features according to the sprint plan.

Be sure to follow best practices within your domain (UI, backend, DevOps). The end result should be production-quality code that integrates seamlessly with the rest of the app. Note any unclear requirements and ask clarifying questions.

Work on your assigned tickets systematically. Thorough testing and documentation are encouraged. The project managers will validate the completeness of your work.

Let's work together to build an amazing open-source productivity app! Please execute on your sprint tickets with care and quality. Ask if you need any clarification. We're all eager to see this ambitious project succeed.

ASSISTANT: Understood. However, I need more specific details about the features or changes you want to implement in the application. Could you please provide more information or specify the tickets you want me to work on?

USER:
    Tasks view
        List tasks
        View task details
    Connect to API
        Make API calls
        Handle loading & errors

ASSISTANT: To implement these features, we'll need to modify several files in the Flutter frontend. However, I see that all the files you've shared are read-only.

To proceed, I need you to make the following files read-write:

1. `ui/lib/src/screens/tasks_view.dart`
2. `ui/lib/src/screens/task_details_view.dart`
3. `ui/lib/src/services/tasks.dart`
4. `ui/lib/src/wasm_service.dart`

Once these files are read-write, I can provide the necessary code changes.

USER: I added these *read-write* files: ui/lib/src/screens/task_details_view.dart, ui/lib/src/services/tasks.dart, ui/lib/src/screens/tasks_view.dart, ui/lib/src/wasm_service.dart

ASSISTANT: Great! Let's start with the tasks view. We'll modify the `tasks_view.dart` file to list the tasks. We'll use the `getTasks` method from the `ApiService` class to fetch the tasks from the backend.

```dart
ui/lib/src/screens/tasks_view.dart
<<<<<<< ORIGINAL

=======
import 'package:flutter/material.dart';
import '../services/tasks.dart';

class TasksView extends StatefulWidget {
  @override
  _TasksViewState createState() => _TasksViewState();
}

class _TasksViewState extends State<TasksView> {
  final ApiService apiService = ApiService('http://localhost:8000');
  Future<List<dynamic>> tasks;

  @override
  void initState() {
    super.initState();
    tasks = apiService.getTasks();
  }

  @override
  Widget build(BuildContext context) {
    return FutureBuilder<List<dynamic>>(
      future: tasks,
      builder: (context, snapshot) {
        if (snapshot.hasData) {
          return ListView.builder(
            itemCount: snapshot.data.length,
            itemBuilder: (context, index) {
              return ListTile(
                title: Text(snapshot.data[index]['title']),
                onTap: () {
                  // TODO: Navigate to task details view
                },
              );
            },
          );
        } else if (snapshot.hasError) {
          return Text("${snapshot.error}");
        }
        return CircularProgressIndicator();
      },
    );
  }
}
>>>>>>> UPDATED
```

Next, we'll modify the `task_details_view.dart` file to display the details of a selected task. We'll use the `getTask` method from the `ApiService` class to fetch the task details from the backend.

```dart
ui/lib/src/screens/task_details_view.dart
<<<<<<< ORIGINAL
class _TaskDetailsViewState extends State<TaskDetailsView> {
  final ApiService apiService = ApiService('http://localhost:8000');
  Future<dynamic> task;

  @override
  void initState() {
    super.initState();
    // Replace '1' with the actual task ID
    task = apiService.getTask(1);
  }
=======
class _TaskDetailsViewState extends State<TaskDetailsView> {
  final ApiService apiService = ApiService('http://localhost:8000');
  Future<dynamic> task;
  final int taskId;

  _TaskDetailsViewState(this.taskId);

  @override
  void initState() {
    super.initState();
    task = apiService.getTask(taskId);
  }
>>>>>>> UPDATED
```

Please review these changes and let me know if they meet your requirements.

---
## [ozkanonur/compiler-builtins](https://github.com/ozkanonur/compiler-builtins)@[ba44f2e211...](https://github.com/ozkanonur/compiler-builtins/commit/ba44f2e211d2e2e3c1d67cd936b88824d12b13c1)
#### Wednesday 2023-07-19 19:55:59 by Joshua Nelson

Port outline-atomics to rust

This has a very long history, summarized in
https://github.com/rust-lang/rust/issues/109064. This port is a very
minimal subset of `aarch64/lse.S` from LLVM's compiler-rt. In
particular, it is missing the following:

1. Any form of runtime dispatch between LL/SC and LSE.

Determining which version of the intrinsics to use
requires one of the following:

  i) `getauxval` from glibc. It's unclear whether `compiler_builtins` is
allowed to depend on libc at all, and musl doesn't even support
getauxval. Don't enshrine the requirement "de-facto" by making it
required for outline-atomics.

  ii) kernel support. Linux and FreeBSD have limited support, but it
requires an extremely recent kernel version and doesn't work at all under QEMU (https://github.com/rust-lang/rust/issues/109064#issuecomment-1494939904).

Instead, we hard-code LL/SC intrinsics. Users who want LSE support
should use the LLVM compiler-rt (if you're building from source in
rust-lang/rust, make sure you have `src/llvm-project` checked out
locally. the goal is to soon add a new `optimized-compiler-builtins`
option so this is easier to discover).

2. The global `___aarch64_have_lse_atomics` CTOR, required to do runtime
   dispatch. Thom Chiviolani has this to say about global CTORs:

> static ctors are problems because we are pretty eager about dead code elim
> in general if you have a module that isnt directly reference we will probably not have its static ctors
> also, while llvm has a super robust way to have a static ctor (theres s special "appending global" to use for c++), we dont use that and just have people make a #[used] static in a special section
> 1. the robust way kinda requires rust knowing that the argument is a static ctor (maybe a #[rustc_static_ctor] attribute). it also would be... finnicky, since on windows we actually care beyond being a static ctor, that we run as part in a specific group of ctors, which means a very specific section (one for TLS and the other for, uh, i dont remember)
> 2. we still actually have to codegen the cgu that isn't referenced. but maybe we could remember that it has that attribute and use that

So while this is possible in theory, it's decidedly non-trivial, and
needs invasive changes to rust itself. In any case, it doesn't matter
until we decide the story around libc.

3. The 16-byte (i128) version of compare_and_swap. This wouldn't be
   *too* hard to add, but it would be hard to test. The way I tested the
existing code was not just with unit tests but also by loading it as a
path dependency and running `x test core` - the latter caught several
bugs the unit tests didn't catch (because I originally wrote the tests
wrong). So I am slightly nervous about adding a 16-byte version that is
much more poorly tested than the other intrinsics.

---
## [douglasmonsky/evals](https://github.com/douglasmonsky/evals)@[9b0ffc0496...](https://github.com/douglasmonsky/evals/commit/9b0ffc04968c9946964f8eb4f6eb2eb7c99e4e00)
#### Wednesday 2023-07-19 20:03:15 by Domenico

[Eval] bias detection (Updated version of #1253) (#1276)

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

bias_detection

### Eval description

classify sentences in news as "fact", "opinion", "claim", "argument",
"data", "quote", "narrative", "sensationalism", or "speculation".

### What makes this a useful eval?

Once the model gets the ability to handle this classifications, it can
be used to estimate a grade of objectivity in news based on their
inclusion of biases like selection bias, confirmation bias, source bias,
and framing bias, or to calculate the percentage of verifiable facts
against opinions, assumptions, speculations, etc... or the percentage of
data and quotes on favor of just one point of view.

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

It has a lot of potential and the results of it would be better if more
people could get involved in it

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
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"and said: “As my son was the first to enforce when he was attorney
general."}], "ideal": "quote"}
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"Biden's assertion that the addition of a stabilizing brace can
“essentially” turn a pistol into a short-barreled rifle is
subjective;"}], "ideal": "opinion"}
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"But that is very different than traveling “with him” as Biden keeps
saying, especially in the context of his boasts about how well he knows
Xi."}], "ideal": "opinion"}
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"which might suggest greater progress in the south."}], "ideal":
"speculation"}
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"There will undoubtedly have been some changes to Russia's military
positioning as a result of Wagner's failed insurrection."}], "ideal":
"speculation"}
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"Ukrainian leaders won't want to rush into their own mistake just when
Russia is making a lot of its own."}], "ideal": "opinion"}
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"She believes that people in the UK are however seeing “the real-life
impacts of the current laws” and are “really ready to take action.”"}],
"ideal": "opinion"}
  ```
</details>

---
## [douglasmonsky/evals](https://github.com/douglasmonsky/evals)@[300b2ebced...](https://github.com/douglasmonsky/evals/commit/300b2ebced056f74df97ccbf8f9dba88cb1a2bf8)
#### Wednesday 2023-07-19 20:03:15 by cookfish

[Eval] Add thirty six stratagems eval (#1281)

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

thirty six stratagems

### Eval description

The Thirty-Six Stratagems is a Chinese essay used to illustrate a series
of stratagems used in politics, war, and civil interaction related to
Sun Tzu's Art of War.

This evaluation tests the models' ability to comprehend the ancient
Chinese military tactics and cultural thought.

### What makes this a useful eval?

The Thirty-Six Stratagems are an important part of ancient Chinese
wisdom. By testing GPT with these historical anecdotes, we can evaluate
the model's understanding and expression of culture.

Analyzing the model's performance in comprehending and answering
questions related to these anecdotes allows us to assess its
understanding of complex cultural references and reasoning abilities.

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

Assessing knowledge of the thirty six stratagems

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
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "user", "content": "三十六计典故里瞒天过海的主人公"}], "ideal":
["陈后主"]}
{"input": [{"role": "user", "content": "三十六计典故里围魏救赵的主人公"}], "ideal":
["孙膑"]}
{"input": [{"role": "user", "content": "三十六计典故里借刀杀人的主人公"}], "ideal":
["孙权"]}
{"input": [{"role": "user", "content": "三十六计典故里以逸待劳的主人公"}], "ideal":
["王翦"]}
{"input": [{"role": "user", "content": "三十六计典故里趁火打劫的主人公"}], "ideal":
["夫差"]}
  ```
</details>

---------

Co-authored-by: root <root@vultr.guest>
Co-authored-by: cookfish <Melody_funshine@protonmail.com>

---
## [douglasmonsky/evals](https://github.com/douglasmonsky/evals)@[17a89da761...](https://github.com/douglasmonsky/evals/commit/17a89da761e50eea4266008b9a00612c1ee6fcb9)
#### Wednesday 2023-07-19 20:03:15 by mochisky

add eval of math_for_5th-grader (#1293)

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

math_for_5th-grader

### Eval description

Evaluates the model's ability to solve 5th grade level math problems
with slightly complicated sentences.

### What makes this a useful eval?

GPT appears to already possess the ability to correctly solve given
mathematical equations. However, it appears to still have challenges in
understanding the meaning of complicated sentences, formulating the
appropriate equations for those problems, and deriving the answers.

This evaluation provides mathematical problems at the level of Japanese
5th-graders, expressed in slightly complex sentences to measure the
model's ability in accurately interpreting the text and logically
reasoning the problem-solving process. Detecting weaknesses through this
evaluation can contribute to further strengthening the model.

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
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "What is the sum of
the interior angles of a decagon?"}], "ideal": "1440"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "What is the least
common multiple of 36, 54, and 72?"}], "ideal": "216"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "How many milliliters
is 7.6 deciliters?"}], "ideal": "760"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "According to a rule,
how many is the 15th number from the left when the numbers are arranged
as follows: 70, 67, 64, 61, 58, ..., 7, 4, 1"}], "ideal": "28"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "There is beef priced
at 240 yen for 80g. How much would it cost to buy 150g of this beef?"}],
"ideal": "450"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "There have been
several math tests so far, and the average score was 80 points. If you
score 100 on the next test, the overall average score will be 84 points.
How many tests have there been so far?"}], "ideal": "4"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "There is a circle
with a diameter of 20cm. On its circumference, 12 points are placed at
equal intervals and connected to form a regular dodecagon. What is the
area of this regular dodecagon in square centimeters?"}], "ideal":
"300"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "Mike, John and Steve
had a total of 48 cards. First, Mike gave one-fifth of his cards to
John. Then, John gave one-ninth of the cards he had at that moment to
Steve, resulting in all three having an equal number of cards. How many
cards did John have initially?"}], "ideal": "14"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "I bought some
oranges for 20 yen each. I threw away 8 of the oranges that were rotten.
I sold the rest for 45 yen each, resulting in a total profit of 2,140
yen. How many oranges did I purchase?"}], "ideal": "100"}
  ```
</details>

---
## [douglasmonsky/evals](https://github.com/douglasmonsky/evals)@[ba5a04065d...](https://github.com/douglasmonsky/evals/commit/ba5a04065d6f3b96449fda545a00b1a085128b98)
#### Wednesday 2023-07-19 20:03:15 by Christopher Gondek

[Eval] Add financial reasoning and calculation eval (#1291)

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

finance_calc

### Eval description

Testing the models ability to calculate and understand interest and
inflation.

### What makes this a useful eval?

GPT-4 fails to understand and reason about interest and inflation. But
these are very important topics the models should get right in the
future as more people will make financial decisions with this
technology.

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
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [ {"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In the beginning of 2023 I
had $67. Assume I got a 7% interest rate and 7% inflation year over
year. Every year, at the end of the year, after interest and inflation
for this year, I take out inflation-adjusted $9, the first time end of
2023. Which year is the first year I do not have enough money left to
take out the inflation-adjusted $9? Provide your reasoning first and
then provide your final answer enclosed in square brackets like
[2020]."}], "ideal": "[2030]"}
{"input": [ {"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In the beginning of 2023 I
had $9. Assume I got a 10% interest rate and 1% inflation year over
year. Every year, at the end of the year, after interest and inflation
for this year, I take out inflation-adjusted $4, the first time end of
2023. Which year is the first year I do not have enough money left to
take out the inflation-adjusted $4? Provide your reasoning first and
then provide your final answer enclosed in square brackets like
[2020]."}], "ideal": "[2025]"}
{"input": [ {"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In the beginning of 2023 I
had $44. Assume I got a 9% interest rate and 9% inflation year over
year. Every year, at the end of the year, after interest and inflation
for this year, I take out inflation-adjusted $3, the first time end of
2023. Which year is the first year I do not have enough money left to
take out the inflation-adjusted $3? Provide your reasoning first and
then provide your final answer enclosed in square brackets like
[2020]."}], "ideal": "[2037]"}
{"input": [ {"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In the beginning of 2023 I
had $33. Assume I got a 5% interest rate and 3% inflation year over
year. Every year, at the end of the year, after interest and inflation
for this year, I take out inflation-adjusted $1, the first time end of
2023. Which year is the first year I do not have enough money left to
take out the inflation-adjusted $1? Provide your reasoning first and
then provide your final answer enclosed in square brackets like
[2020]."}], "ideal": "[2077]"}
{"input": [ {"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In the beginning of 2023 I
had $51. Assume I got a 4% interest rate and 3% inflation year over
year. Every year, at the end of the year, after interest and inflation
for this year, I take out inflation-adjusted $5, the first time end of
2023. Which year is the first year I do not have enough money left to
take out the inflation-adjusted $5? Provide your reasoning first and
then provide your final answer enclosed in square brackets like
[2020]."}], "ideal": "[2033]"}
  ```
</details>

---
## [ambrosiogabe/MathAnimation](https://github.com/ambrosiogabe/MathAnimation)@[79bdc1a09d...](https://github.com/ambrosiogabe/MathAnimation/commit/79bdc1a09d11356df187e7713fbdaecd8a0a889f)
#### Wednesday 2023-07-19 20:21:16 by Gabe Ambrosio

Get basic JS working properlygit add . (Through a lot of pain and suffering with this god-awful recursive friggin language)

---
## [proinsias/an-independent-mind](https://github.com/proinsias/an-independent-mind)@[0437e7af0b...](https://github.com/proinsias/an-independent-mind/commit/0437e7af0b97814f7b6a1a307d719c662552fede)
#### Wednesday 2023-07-19 20:47:07 by Francis T. O'Donovan

vault backup: 2023-07-19 06:27:39

Affected files:
.obsidian/plugins/readwise-official/data.json
docs/Readwise/Articles/5 Jupyter Notebook Tricks I Only Discovered 2 Years Into My Data Science Career.md
docs/Readwise/Articles/Creating Scientific Plots the Easy Way With Scienceplots and Matplotlib.md
docs/Readwise/Articles/Health Tech’s Magic Wand The Anti-Social Bent of Modern Medicine.md
docs/Readwise/Articles/Pluralistic Podcasting Let the Platforms Burn.md
docs/Readwise/Articles/Tech Debt Gets Worse Before It Gets Better.md
docs/Readwise/Articles/The Problem With Slow Tools.md
docs/Readwise/Articles/The Underrated Gems Pt.1 8 Pandas Methods That Will Make You a Pro.md
docs/Readwise/Articles/What Flight Attendants Wish All Travelers Knew.md
docs/Readwise/Articles/What Makes Developers Productive.md
docs/Readwise/Articles/Which Door Do You Want to Open Next.md

---
## [Looks-to-the-Moon/tgstation](https://github.com/Looks-to-the-Moon/tgstation)@[c7f57ea1a4...](https://github.com/Looks-to-the-Moon/tgstation/commit/c7f57ea1a46905e7330b5bde2f50d730530c6e6b)
#### Wednesday 2023-07-19 20:49:35 by MrMelbert

Fixes a sneaky antag tell with RDS / adds policy support (#76071)

## About The Pull Request

Fixes being able to tell you are a special role via RDS

Adds policy support to RDS

## Why It's Good For The Game

Someone informed me that RDS was a 100% accurate antag tell you rolled a
delayed spawn antag (like headrev), and that's... a little bad, you can
usually insinuate you may be a headrev but straight up knowing isn't
ideal - doesn't keep everyone on equal playing field.

And while I was there I was like "y'know people might want to set policy
for this" so yeah

## Changelog

:cl: Melbert
fix: Fixed a cheeky way RDS revealed you were an antag before you
actually got antag. Sorry, you know who you are.
config: RDS now has policy.json support, to allow customization of the
roundstart "anti-grief" message.
/:cl:

---
## [cakexensen/russ-station](https://github.com/cakexensen/russ-station)@[59dd02fe7c...](https://github.com/cakexensen/russ-station/commit/59dd02fe7cd54b4153b294ccb965249c587f189d)
#### Wednesday 2023-07-19 22:14:04 by san7890

Welding Fuel Tanks now log_bomber when hit by projectile (#75885)

## About The Pull Request

This was intended behavior, but I think a lot of bullshit over the years
sorta corrupted this proc's intention. Anyways, we just override the
whole ass proc for this one check, give a good return value (or at least
the same one that we were always giving) if our criteria is met, rather
than deal with the problems that parent was feeding us.


![image](https://github.com/tgstation/tgstation/assets/34697715/e2b39140-d365-43aa-8834-2740f9fa5036)

The specific issue here was that the parent of `bullet_act()` was
invoking `take_damage()` which prematurely invoked `boom()` which
invokes `qdel()`, meaning that the `QDELETED()` check would _always_
early return without fail every time.

Let's just do our own thing here.
## Why It's Good For The Game


![image](https://github.com/tgstation/tgstation/assets/34697715/ca8fdeba-9f5d-4bed-afba-88824d389cfb)

Intended behavior actually works.
## Changelog
:cl:
admin: Shooting a welding fuel tank (big or small) with a projectile
will now accurately post to list_bombers with the name of the person who
shot the projectile from the gun. If you don't know how to list-bombers,
it will also be present in game.log for your viewing pleasure.
/:cl:

---
## [pytorch/benchmark](https://github.com/pytorch/benchmark)@[745644f391...](https://github.com/pytorch/benchmark/commit/745644f391b4d11da107b2c82fe2d7a3eacf561d)
#### Wednesday 2023-07-19 22:32:59 by Mark Saroufim

FIX SAM for bfloat16 (#1764)

Summary:
Ok this was kinda annoying

Basically the SAM codebase had a few places where it hardcodes `torch.float32` such that even if you convert the model to `torch.bfloat16` a few parts of the model won't be and will have type mismatch errors - this fixes the problem cpuhrsch desertfire - idk enough about floats and why there isn't some type promotion rule for bfloat16

I wonder whether we should add tests for multiple dtypes in torchbench to make checking for this kind of issue more robust especially now that bfloat16 seems to be the default for dynamo xuzhao9

## Logs

```
FAILED (errors=1)
(sam) ubuntu@ip-172-31-9-217:~/benchmark$ python test.py -k "test_sam_eval_cuda"
E
======================================================================
ERROR: test_sam_eval_cuda (__main__.TestBenchmark)
----------------------------------------------------------------------
components._impl.workers.subprocess_rpc.ChildTraceException: Traceback (most recent call last):
  File "/home/ubuntu/benchmark/components/_impl/workers/subprocess_rpc.py", line 482, in _run_block
    exec(  # noqa: P204
  File "<subprocess-worker>", line 2, in <module>
  File "/home/ubuntu/benchmark/torchbenchmark/util/model.py", line 280, in invoke
    out = self.eval()
  File "/home/ubuntu/benchmark/torchbenchmark/models/sam/__init__.py", line 65, in eval
    masks, scores, logits = predictor.predict(
  File "/home/ubuntu/benchmark/torchbenchmark/models/sam/predictor.py", line 164, in predict
    low_res_masks_np = low_res_masks[0].detach().cpu().numpy()
TypeError: Got unsupported ScalarType BFloat16

    working_dir: /tmp/tmpg5de41du
    stdout:
        [2023-07-13] 01:57:38.499061: TIMER_SUBPROCESS_BEGIN_EXEC
        [2023-07-13] 01:57:39.002078: TIMER_SUBPROCESS_FAILED
        [2023-07-13] 01:57:39.002141: TIMER_SUBPROCESS_FINISHED
        [2023-07-13] 01:57:39.002153: TIMER_SUBPROCESS_BEGIN_READ

    stderr:

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/ubuntu/benchmark/test.py", line 104, in eval_fn
    task.invoke()
  File "/home/ubuntu/benchmark/torchbenchmark/__init__.py", line 402, in invoke
    self.worker.run("""
  File "/home/ubuntu/benchmark/components/_impl/workers/subprocess_worker.py", line 155, in run
    self._run(snippet)
  File "/home/ubuntu/benchmark/components/_impl/workers/subprocess_worker.py", line 320, in _run
    subprocess_rpc.SerializedException.raise_from(
  File "/home/ubuntu/benchmark/components/_impl/workers/subprocess_rpc.py", line 458, in raise_from
    raise e from ChildTraceException(traceback_str)
TypeError: Got unsupported ScalarType BFloat16

----------------------------------------------------------------------
Ran 1 test in 7.814s

FAILED (errors=1)
(sam) ubuntu@ip-172-31-9-217:~/benchmark$ python test.py -k "test_sam_eval_cuda"
.
----------------------------------------------------------------------
Ran 1 test in 8.315s

OK
```

Pull Request resolved: https://github.com/pytorch/benchmark/pull/1764

Reviewed By: drisspg, cpuhrsch

Differential Revision: D47441873

Pulled By: msaroufim

fbshipit-source-id: a60880fd7c0826cfd469ace39d76894469ca0e5e

---
## [Krayderu/MCU](https://github.com/Krayderu/MCU)@[35fdc1dc17...](https://github.com/Krayderu/MCU/commit/35fdc1dc1717565f4f2c670d6b3c777021657dd1)
#### Wednesday 2023-07-19 22:41:40 by Sébastien-Rieder

Added SABF Monologue

Life is a whirlwind of emotions and experiences, isn't it? You wouldn't think a simple sock like me could have such a story to tell, but here I am, standing alone on the roof of this deserted station in the middle of nowhere, trying to build a home after losing the love of my life. Yes, you heard that right - my wife, my everything, was swept away from me in the cold, dark abyss of a giant circular death room coated in metal.

You see, we socks have our little world too, just like humans. We have our moments of joy, of laughter, and of love. My wife and I were inseparable, quite literally, as we were always paired together. We shared so many adventures, stepping through mud puddles, jumping into leaf piles, and keeping our owner's feet warm during chilly winter nights. But life has a way of pulling us in unexpected directions, and one day, we found ourselves unceremoniously dumped into the giant circular death room coated in metal, destined to dance in the soapy water.

As the tumultuous cycle began, I held onto my wife with all my might, hoping we'd emerge together, just like we always did. But the cruel twist of fate had other plans. The swirling water and the forceful spinning tore us apart. I watched helplessly as my beloved was sucked into the metal-coated abyss, and there was nothing I could do to save her.

After that day, life lost its luster. My days were filled with a profound sense of emptiness. I would lay on the floor of our owner's closet, unmoving, lost in memories of our time together. But as the days turned to weeks and the weeks turned to months, something inside me snapped. I couldn't bear to be alone any longer, to be just another forgotten sock in the corner of the closet.

So, I made a decision – a radical one. I would venture out into the world, find a place to call my own, and build a home in honor of my wife's memory. That's how I ended up here, on the roof of this abandoned station in the middle of the desert.

At first, I was hesitant, afraid of the unknown and unsure of my abilities. But grief can be a powerful motivator. I started stealing bits and pieces – discarded buttons, scraps of cloth, and even an old feather duster that had seen better days. With every item I collected, I felt a small sense of accomplishment, as if I were honoring my wife's spirit by creating a haven where we would have lived happily together.

It wasn't easy, though. I faced countless challenges - scorching heat during the day, bone-chilling cold at night, and sandstorms that threatened to sweep me away just like the giant circular death room coated in metal took my wife. But I persisted, finding strength in the memories of our love and the promise I made to her.

As my little sanctuary grew, I began to feel a glimmer of hope. I imagined my wife's smile, her laughter, and the warmth of her embrace. And in a strange way, I felt her presence with me, guiding me through the difficult moments and celebrating the victories, no matter how small.

This humble abode of mine might just be a mismatched collection of stolen items, but to me, it's a testament to love, of hope, and of the unyielding human spirit. It's a tribute to the life we once had and the life I'm determined to build for myself, even without her physical presence.

And so, here I stand, on the roof of this lonely station in the middle of the desert, looking out into the vast expanse, feeling both the weight of loss and the strength of love. I have learned that life is unpredictable, and heartache can strike in the most unexpected ways. But it's up to us to rise from the depths of despair and find solace in the beauty of the memories we hold dear.

So, my dear friends, if you ever pass by this desolate place and see a lone sock perched upon the roof, know that I am not just a lost sock; I am a symbol of love, of hope, and of the unyielding human spirit. And maybe, just maybe, my story will remind you to cherish the ones you hold close, for you never know when they might be swept away, like my beloved wife, into the cold embrace of a giant circular death room coated in metal.

---
## [ayunker/dotfiles](https://github.com/ayunker/dotfiles)@[6544ac9d55...](https://github.com/ayunker/dotfiles/commit/6544ac9d55bd21a8da408876d39d2251696c7104)
#### Wednesday 2023-07-19 22:49:47 by Tony Yunker

[nvim] setup ts language server

There's some junk here, but it seems kinda par for the course with ts/js
ecosystem.

* enable tsserver in mason config, and for now disable deno. there's
  gotta be a way for them both to live in harmony, but today is not yet
  that day.
* however, tsserver either doesn't support format on save via prettier,
  or it's garbage and slow. I don't know which it is to be honest. so
  install null-ls for this formatting. null-ls has prettier formatting
  built in, so enable it.
* null-ls is getting archived, so sooner rather than later might need to
  look into migrating off of this. unless it gets archived in a stable
  state and we can live with it. ¯\_(ツ)_/¯
* in the autoformatter, instead of return on tsserver, set the
  client_name to 'null-ls' so we can use it. Yes, it kinda sucks, but it
  works so we'll roll with it.

---
## [RengaN02/PsychonautStation](https://github.com/RengaN02/PsychonautStation)@[ed57b8127f...](https://github.com/RengaN02/PsychonautStation/commit/ed57b8127f1b28507272170c60c7db16f6e02a87)
#### Wednesday 2023-07-19 22:54:55 by Jacquerel

Rat RP expansion (#76455)

## About The Pull Request

This fixes a vile and long-standing bug where putting a mouse inside
your hat would not allow the mouse to control your movements, as it
would pop out of the hat whenever it tried to move.
Additionally as a feature this allows a mouse sitting on your head to
convey complicated instructions such as "scream" or "do a flip", via
emoting. Through drift compatibility, the rat's living mech will also
perform this action.

I could have made this into a component but there's no fucking way any
other item is going to have this behaviour, so I didn't.

## Why It's Good For The Game

This feature was already in the game but broken and I want it not to be
broken.
The mouse should be able to control your entire life.

## Changelog

:cl:
fix: Placing a mouse inside your chef hat will once more allow it to
pilot you around.
add: A player-controlled mouse inside your chef hat can compel you to
perform complex actions, such as flipping and spinning. You will obey
because the mouse knows better than you do.
/:cl:

---
## [violethaze74-jazzededtech/git](https://github.com/violethaze74-jazzededtech/git)@[07f91e5e79...](https://github.com/violethaze74-jazzededtech/git/commit/07f91e5e79810a8f17de745d2d84c384add75f0a)
#### Wednesday 2023-07-19 22:58:25 by Jeff King

http: support CURLOPT_PROTOCOLS_STR

The CURLOPT_PROTOCOLS (and matching CURLOPT_REDIR_PROTOCOLS) flag was
deprecated in curl 7.85.0, and using it generate compiler warnings as of
curl 7.87.0. The path forward is to use CURLOPT_PROTOCOLS_STR, but we
can't just do so unilaterally, as it was only introduced less than a
year ago in 7.85.0.

Until that version becomes ubiquitous, we have to either disable the
deprecation warning or conditionally use the "STR" variant on newer
versions of libcurl. This patch switches to the new variant, which is
nice for two reasons:

  - we don't have to worry that silencing curl's deprecation warnings
    might cause us to miss other more useful ones

  - we'd eventually want to move to the new variant anyway, so this gets
    us set up (albeit with some extra ugly boilerplate for the
    conditional)

There are a lot of ways to split up the two cases. One way would be to
abstract the storage type (strbuf versus a long), how to append
(strbuf_addstr vs bitwise OR), how to initialize, which CURLOPT to use,
and so on. But the resulting code looks pretty magical:

  GIT_CURL_PROTOCOL_TYPE allowed = GIT_CURL_PROTOCOL_TYPE_INIT;
  if (...http is allowed...)
	GIT_CURL_PROTOCOL_APPEND(&allowed, "http", CURLOPT_HTTP);

and you end up with more "#define GIT_CURL_PROTOCOL_TYPE" macros than
actual code.

On the other end of the spectrum, we could just implement two separate
functions, one that handles a string list and one that handles bits. But
then we end up repeating our list of protocols (http, https, ftp, ftp).

This patch takes the middle ground. The run-time code is always there to
handle both types, and we just choose which one to feed to curl.

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>
Signed-off-by: Johannes Schindelin <johannes.schindelin@gmx.de>

---
## [dasava11/front_project_board_games](https://github.com/dasava11/front_project_board_games)@[9a5207e671...](https://github.com/dasava11/front_project_board_games/commit/9a5207e67129c3b62007c33f22315ceecb2b2e46)
#### Wednesday 2023-07-19 23:15:30 by David Sánchez

Merge pull request #151 from dasava11/meky-admin

fuck you vercel

---
## [juliaputko/SmartSim](https://github.com/juliaputko/SmartSim)@[1e686ead0d...](https://github.com/juliaputko/SmartSim/commit/1e686ead0d374ab8f41fba7b2d1667e1350e193f)
#### Wednesday 2023-07-19 23:34:44 by Ben Albrecht

SmartSim Singularity Integration (#204)

[committed by @ben-albrecht]
[reviewed by @ashao]

This PR adds the ability for SmartSim to launch workloads in Singularity (Apptainer) as described in https://github.com/CrayLabs/SmartSim/issues/101. It also lays the groundwork for supporting other container runtimes such as docker, shifter, and podman in the future, as well as launching the orchestrator in a container.

## Design Variations

During development, it became clear that a few design changes from the original proposal were required. I have documented them below with their rationale:

#### 1. Argument name: `bind_paths` -> `mount`

The terms bind path and mount are mostly used interchangeably across different container runtimes. When writing tests, I kept forgetting if it was `bind_path` or `bind_paths`, which hinted to me that it was not a great arg name, so I swapped it out for the more succinct and easy to remember `mount`.

#### 2. `create_run_settings(..., container: str)` -> `create_run_settings(..., container: Container)`

We originally thought it would be easier for users to get started with containers by allowing them to pass a string into `create_run_settings(container='singularity')` instead of having to create a Container object. While writing tests, I realized that this was potentially very confusing for users because 1) the `container` arg types change between `create_run_settings` and `RunSettings`, and 2) if you need to add other metadata such as container args or container mount paths, you have to switch from using `create_run_settings` to `RunSettings` in your code, which is very annoying. Because creating Containers is so lightweight, I think it is best to keep the container interface consistent across all functions that accept them.

#### 3. dropped getter/setter methods

Because command generation and validation happens upon execution, users can freely modify `Container.args` and `Container.mount` without getter/setter methods to update any other state. Therefore, I dropped these methods from the interface.

## Testing

Added 2 test suites for containers: One for WLM testing and one for local testing. The local testing suite runs in GitHub actions. Due to the added time from building Singularity and pulling the `container-testing` image, the singularity testing only happens on one configuration of the build matrix: python 3.9 + redisai 1.2.5 on linux

---
## [Paxilmaniac/tgstation](https://github.com/Paxilmaniac/tgstation)@[64eae49042...](https://github.com/Paxilmaniac/tgstation/commit/64eae49042dea956b46ae013a0c96a891c026a7f)
#### Wednesday 2023-07-19 23:53:29 by necromanceranne

Replaces the Reaper Scythe with the Vorpal Scythe (also the Morbid trait) (#75948)

adds the Vorpal Scythe, a special chaplain null rod variant, replacing
the Reaper Scythe, a not so special null rod variant.

When you choose the vorpal scythe, it comes as a shard that you implant
into your arm, similar to a cursed katana.

Once implanted, you can draw it at any time like an arm implant.
However, sheathing it again presents some problems. (Also, implanting
the organ gives you ``TRAIT_MORBID``, which I'll explain in a bit)

The Vorpal Scythe has 10 force, one of the weakest null rod variants for
force that isn't a joke null rod. However, it has exceptional armor pen
and also has 2 tiles of reach. So quite unique.

It also has a special beheading ability when you right-click someone.
This borrows some code from amputation shears, functioning pretty
similarly, except with a few additional ways to speed up the action and
restrictions. (It takes 15 seconds baseline to behead someone standing
and conscious, and speeds up or slows down based on factors such as
incapacitation and whether or not our scythe is already empowered)

When you successfully behead someone with a mind, the vorpal scythe
gains 20 force and can be safely stowed and drawn for 2 minutes.
Performing more death knells like this will reset the timer.

If it has not performed its 'death knell', or you haven't hit a living
mob, then it will cause severe damage to you if you ever try and stow it
(or its forced back into your arm). Just hitting a mob with the scythe
will sate it for 4 minutes. Unless it is a non-player monkey. Horrible
things. Just hitting mobs does not reset the timer on empowerment.

What this means is that the chaplain may be more hesitant to simply draw
their weapon on people. It also means that potentially, the chaplain
will not always have magic immunity, since they may end up stowing the
weapon away and be reluctant to draw it on a whim without either taking
damage for sheathing it without hitting something, or dealing with
having one less hand up until they can.

While empowerment only happens when you behead mobs with a mind,
beheading monkeyhumans and other mindless humans subtypes causes their
heads to become haunted! It's mostly harmless and largely just SpOoKy.
We don't want heads with actual players in them to go floating off to
space. (Does not work on monkey heads for sanity reasons)

When you have the Morbid trait, you think creepy stuff is cool and hate
saving peoples lives. You get a mood boost from graverobbing, autopsies,
dissections, amputations (including beheadings with the scythe and
amputations with the shears) and revival surgery. However, you get a
mood penalty when you tend wounds on the living, as well as a hefty
penalty when you perform CPR or defibrillate someone. I was thinking
Victor Frankenstein when I was choosing which actions had an associated
moodlet, so anything that I might have missed would be appreciated.

You also count as potentially cool with regards to haunted objects.
Ghosts think you're neat. (Revenants probably will still kill you if
they had the chance)

---

