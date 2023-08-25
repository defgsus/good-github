## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-08-24](docs/good-messages/2023/2023-08-24.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,287,037 were push events containing 3,492,676 commit messages that amount to 254,213,347 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 49 messages:


## [andmeics/gcc](https://github.com/andmeics/gcc)@[6619b3d4c1...](https://github.com/andmeics/gcc/commit/6619b3d4c15cd754798b1048c67f3806bbcc2e6d)
#### Thursday 2023-08-24 00:31:47 by Jivan Hakobyan

Improve quality of code from LRA register elimination

This is primarily Jivan's work, I'm mostly responsible for the write-up and
coordinating with Vlad on a few questions.

On targets with limitations on immediates usable in arithmetic instructions,
LRA's register elimination phase can construct fairly poor code.

This example (from the GCC testsuite) illustrates the problem well.

int  consume (void *);
int foo (void) {
  int x[1000000];
  return consume (x + 1000);
}

If you compile on riscv64-linux-gnu with "-O2 -march=rv64gc -mabi=lp64d", then
you'll get this code (up to the call to consume()).

        .cfi_startproc
        li      t0,-4001792
        li      a0,-3997696
        li      a5,4001792
        addi    sp,sp,-16
        .cfi_def_cfa_offset 16
        addi    t0,t0,1792
        addi    a0,a0,1696
        addi    a5,a5,-1792
        sd      ra,8(sp)
        add     a5,a5,a0
        add     sp,sp,t0
        .cfi_def_cfa_offset 4000016
        .cfi_offset 1, -8
        add     a0,a5,sp
        call    consume

Of particular interest is the value in a0 when we call consume. We compute that
horribly inefficiently.   If we back-substitute from the final assignment to a0
we get...

a0 = a5 + sp
a0 = a5 + (sp + t0)
a0 = (a5 + a0) + (sp + t0)
a0 = ((a5 - 1792) + a0) + (sp + t0)
a0 = ((a5 - 1792) + (a0 + 1696)) + (sp + t0)
a0 = ((a5 - 1792) + (a0 + 1696)) + (sp + (t0 + 1792))
a0 = (a5 + (a0 + 1696)) + (sp + t0)  // removed offsetting terms
a0 = (a5 + (a0 + 1696)) + ((sp - 16) + t0)
a0 = (4001792 + (a0 + 1696)) + ((sp - 16) + t0)
a0 = (4001792 + (-3997696 + 1696)) + ((sp - 16) + t0)
a0 = (4001792 + (-3997696 + 1696)) + ((sp - 16) + -4001792)
a0 = (-3997696 + 1696) + (sp -16) // removed offsetting terms
a0 = sp - 3990616

That's a pretty convoluted way to compute sp - 3990616.

Something like this would be notably better (not great, but we need both the
stack adjustment and the address of the object to pass to consume):

   addi sp,sp,-16
   sd ra,8(sp)
   li t0,-4001792
   addi t0,t0,1792
   add sp,sp,t0
   li a0,4096
   addi a0,a0,-96
   add a0,sp,a0
   call consume

The problem is LRA's elimination code is not handling the case where we have
(plus (reg1) (reg2) where reg1 is an eliminable register and reg2 has a known
equivalency, particularly a constant.

If we can determine that reg2 is equivalent to a constant and treat (plus
(reg1) (reg2)) in the same way we'd treat (plus (reg1) (const_int)) then we can
get the desired code.

This eliminates about 19b instructions, or roughly 1% for deepsjeng on rv64.
There are improvements elsewhere, but they're relatively small.  This may
ultimately lessen the value of Manolis's fold-mem-offsets patch.  So we'll have
to evaluate that again once he posts a new version.

Bootstrapped and regression tested on x86_64 as well as bootstrapped on rv64.
Earlier versions have been tested against spec2017.  Pre-approved by Vlad in a
private email conversation (thanks Vlad!).

Committed to the trunk,

gcc/
	* lra-eliminations.cc (eliminate_regs_in_insn): Use equivalences to
	to help simplify code further.

---
## [vmware-tanzu/kubeapps](https://github.com/vmware-tanzu/kubeapps)@[4e5ac7a243...](https://github.com/vmware-tanzu/kubeapps/commit/4e5ac7a24310d30a0ab539560373cab1106277cd)
#### Thursday 2023-08-24 00:56:55 by Antonio Gámez, PhD

Use finalizers to spin up AppRepo clean-up jobs (#6647)

### Description of the change

Even if the sync jobs were added a security context (by means of each
AppRepo CRD), this information was not available for Cleanup jobs. This
is mainly due to the fact that those jobs are spun up once a NotFound
error is thrown when fetching an AppRepo.
However, Kubernetes does have a native approach for dealing with these
scenarios: finalizers.

In https://github.com/vmware-tanzu/kubeapps/pull/6605 we proposed a
simplistic workaround based on adding more params to the controller...
but as suggested in
https://github.com/vmware-tanzu/kubeapps/pull/6605#issuecomment-1678268807,
moving to finalizers is a better long-term solution.


### Benefits

Cleanup jobs are now handled within an existing AppRepo context...
meaning we have all the syncJobTemplate available to be used (ie,
securityPolicies and so on).

### Possible drawbacks

When dealing with finalizers in the past I often found it really
annoying when they get stuck and prevent the resource to get deleted. I
wonder if we should add some info in the FAQ on how to manually remove
the finalizers.

Additionally, and this might be something important: for the AppRepo
controller to be able to `update` AppRepos in other namespaces !=
kubeapps.... (to add the finalizer) it now needs extra RBAC. Before we
were just granting `...-appprepos-read`.. but now we would need to grant
`...-write` as well...and I'm not sure we really want to do so.
WDYT, @absoludity ?
Another idea is using an admission policy... but not sure again if we
want to deal with that...

~(I haven't modified the RBAC yet in this PR)~ Changes have been
performed finally

### Applicable issues

- fixes #6545

### Additional information

This PR is based on top of
https://github.com/vmware-tanzu/kubeapps/pull/6646, but the main change
to review is
https://github.com/vmware-tanzu/kubeapps/commit/6e7091015f9a6c3a289224d05dab5f60736489a0
The rest is just moving code into separate files, mostly.

Also, I have been taking a look at `kubebuilder` to create a new
controller, based on the `sigs.k8s.io/controller-runtime` rather than on
the workqueues we currently have. While it is pretty easy to start with
([see quickstart](https://book.kubebuilder.io/quick-start)), I think it
is adding too much complexity (using kustomize, adding rbac proxies,
prometheus metrics, etc...
I also quickly tried the k8s codegen scripts, but ran into some issues
with my setup... but perhaps it's the best option.

IMO, at some point we should start thinking about moving towards a new
state-of-the-art k8s controller boilerplate.

---------

Signed-off-by: Antonio Gamez Diaz <agamez@vmware.com>

---
## [GuillaumePrata/tgstation](https://github.com/GuillaumePrata/tgstation)@[0dd3e66aef...](https://github.com/GuillaumePrata/tgstation/commit/0dd3e66aefa2a61cb4e78482273958c1d09f8295)
#### Thursday 2023-08-24 01:02:33 by Vekter

Grilles take 0-1 damage when shocking something, power sinks are available at lower reputation (#77860)

## About The Pull Request
Ports BeeStation/BeeStation-Hornet#3590. As it is right now, it's
trivial to set up a contraption using a conveyor belt and a shocked
grille to continuously shock monkey bodies. While this is very funny, it
also serves as a ghetto powersink that's hard to locate, easy to
replicate, and lasts effectively forever, since you can just keep
shocking the same bodies over and over again.

This doesn't completely remove the ability to make these, but it makes
them require at least a little maintenance and provides a way for them
to stop working even if the crew isn't able to locate them.

In an attempt to finally get people using the _actual_ powersink,
they'll show up a bit earlier in progression now. I'm not convinced 20
minutes is enough, but I don't want to put them in early enough that it
fucks with Engineering's ability to set things up at round start. We can
turn this down further if need be.

I'm also up for turning the TC requirement down, but 11 feels about
right for what they're supposed to do, so I'd prefer we try this first
and see how that works.

## Why It's Good For The Game
I'm all for goofy weird shit players have found, but there's an issue
with being able to do what an antag item is supposed to do but just
plain better. This shouldn't make creating these impossible or make them
unusable, but it'll require players to actively monitor them if they
want it to run for an extended period.

Additionally, we don't really see powersinks much anymore, and while
that might be more because powernets are kind of buggy and unreliable, I
think making them easier to get will make them show up a little more.

## Changelog
:cl: Vekter
balance: Grilles will now take 0-1 damage every time they shock
something.
balance: Powersinks are now available earlier in traitor progression.
/:cl:

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [rgwood/nushell](https://github.com/rgwood/nushell)@[ad49c17eba...](https://github.com/rgwood/nushell/commit/ad49c17ebacd04585fb4355e079ec87d7fc63d8d)
#### Thursday 2023-08-24 01:23:43 by Kiryl Mialeshka

fix(nu-parser): do not update plugin.nu file on nu startup (#10007)

<!--
if this PR closes one or more issues, you can automatically link the PR
with
them by using one of the [*linking
keywords*](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword),
e.g.
- this PR should close #xxxx
- fixes #xxxx

you can also mention related issues, PRs or discussions!
-->

# Description

I've been investigating the [issue
mentioned](https://github.com/nushell/nushell/pull/9976#issuecomment-1673290467)
in my prev pr and I've found that plugin.nu file that is used to cache
plugins signatures gets overwritten on every nushell startup and that
may actually mess up with the file content if 2 or more instances of
nushell will run simultaneously.

To reproduce:
1. register at least 2 plugins in your local nushell
2. remember how many entries you have in plugin.nu with `open
$nu.plugin-path | find nu_plugin`
3. run 
    - either `cargo test` inside nushell repo
- or run smth like this `1..100 | par-each {|it| $"(random integer
1..100)ms" | into duration | sleep $in; nu -c "$nu.plugin-path"}` to
simulate parallel access. This approach is not so reliable to reproduce
as running test but still a good point that it may effect users actually
4. validate that your `plugin.nu` file was stripped

<!--
Thank you for improving Nushell. Please, check our [contributing
guide](../CONTRIBUTING.md) and talk to the core team before making major
changes.

Description of your pull request goes here. **Provide examples and/or
screenshots** if your changes affect the user experience.
-->

# Solution

In this pr I've refactored the code of handling the `register` command
to minimize code duplications and make sure that overwrite of
`plugin.nu` file is happen only when user calls the command and not on
nu startup

Another option would be to use temp `plugin.nu` when running tests, but
as the issue actually can affect users I've decided to prevent
unnecessary writing at all. Although having isolated `plugin.nu` still
worth of doing

# User-Facing Changes
<!-- List of all changes that impact the user experience here. This
helps us keep track of breaking changes. -->
It changes the behaviour actually as the call `register <plugin>
<signature>` now doesn't updates `plugin.nu` and just reads signatures
to the memory. But as I understand that kind of call with explicit
signature is meant to use only by nushell itself in the `plugin.nu` file
only. I've asked about it in
[discord](https://discordapp.com/channels/601130461678272522/615962413203718156/1140013448915325018)

<!--
Don't forget to add tests that cover your changes.

Make sure you've run and fixed any issues with these commands:

- `cargo fmt --all -- --check` to check standard code formatting (`cargo
fmt --all` applies these changes)
- `cargo clippy --workspace -- -D warnings -D clippy::unwrap_used -A
clippy::needless_collect -A clippy::result_large_err` to check that
you're using the standard code style
- `cargo test --workspace` to check that all tests pass
- `cargo run -- -c "use std testing; testing run-tests --path
crates/nu-std"` to run the tests for the standard library

> **Note**
> from `nushell` you can also use the `toolkit` as follows
> ```bash
> use toolkit.nu # or use an `env_change` hook to activate it
automatically
> toolkit check pr
> ```
-->

# After Submitting
<!-- If your PR had any user-facing changes, update [the
documentation](https://github.com/nushell/nushell.github.io) after the
PR is merged, if necessary. This will help us keep the docs up to date.
-->

Actually, I think the way plugins are stored might be reworked to
prevent or mitigate possible issues further:
- problem with writing to file may still arise if we try to register in
parallel as several instances will write to the same file so the lock
for the file might be required
- using additional parameters to command like `register` to implement
some internal logic could be misleading to the users
- `register` call actually affects global state of nushell that sounds a
little bit inconsistent with immutability and isolation of other parts
of the nu. See issues
[1](https://github.com/nushell/nushell/issues/8581),
[2](https://github.com/nushell/nushell/issues/8960)

---
## [NateElison18/RockBuddy](https://github.com/NateElison18/RockBuddy)@[5cc4a3566f...](https://github.com/NateElison18/RockBuddy/commit/5cc4a3566f486640b08b1aa5488a1c216dc3c6b9)
#### Thursday 2023-08-24 01:52:14 by 404kevnotfound

Everything is broken. Fuck you. I'll see you tomorrow.

---
## [julian0406/Evaluacion_U3](https://github.com/julian0406/Evaluacion_U3)@[5670128287...](https://github.com/julian0406/Evaluacion_U3/commit/5670128287e0eed2c443b3bc3d968bd25534ed28)
#### Thursday 2023-08-24 02:58:08 by julian0406

Commit

By
Walk on by
Walk on by
Walk on by
Walk on by
Yeah, bitch, I said what I said
I'd rather be famous instead
I let all that get to my head
I don't care, I paint the town red
Bitch, I said what I said
I'd rather be famous instead
I let all that get to my head
I don't care, I paint the town red
Mm, she the devil
She a bad lil' bitch, she a rebel
She put her foot to the pedal
It'll take a whole lot for me to settle
Mm, she the devil
She a bad lil' bitch, she a rebel
She put her foot to the pedal
It'll take a whole lot for me to settle (yeah, yeah)
Said, my happiness is all of your misery
I put good dick all in my kidneys
This Margiel' don't come with no jealousy
My illness don't come with no remedy
I am so much fun without Hennessy
They just want my love and my energy
You can't talk no shit without penalties
Bitch, I'm in yo' shit if you send for me
I'm going to glow up one more time
Trust me, I have magical foresight
You gon' see me sleepin' in courtside
You gon' see me eatin' ten more times
Ugh, you can't take that bitch nowhere
Ugh, I look better with no hair
Ugh, ain't no sign I can't smoke here
Ugh, gimme the chance and I'll go there (Yeah)
Yeah, bitch, I said what I said
I'd rather be famous instead
I let all that get to my head
I don't care, I paint the town red
Bitch, I said what I said
I'd rather be famous instead
I let all that get to my head
I don't care, I paint the town red
Mm, she the devil
She a bad lil' bitch, she a rebel
She put her foot to the pedal
It'll take a whole lot for me to settle
Mm, she the devil
She a bad lil' bitch, she a rebel
She put her foot to the pedal
It'll take a whole lot for me to settle (yeah, yeah)
Said pop make money, now you try, bitch
You could use a revamp with a new vibe, sis
I don't need a big feature or a new sidekick
I don't need a new fan 'cause my boo like it
I don't need to wear a wig to make you like it
I'm a two-time bitch, you ain't knew I'd win?
Throw a shot like you tryna have a food fight then
All my opps waitin' for me to be you, I bet
Said I got drive, I don't need a car
Money really all that we fiendin' for
I'm doin' things they ain't seen before
Fans ain't dumb, but extremists are
I'm a demon, Lord
Fall off what? I ain't seen the horse
Called your bluff, better cite the source
Fame ain't somethin' that I need no more
'Cause, bitch, I said what I said
I'd rather be famous instead
I let all that get to my head
I don't care, I paint the town red
Bitch, I said what I said
I'd rather be famous instead
I let all that get to my head
I don't care, I paint the town red
Mm, she the devil
She a bad lil' bitch, she a rebel
She put her foot to the pedal
It'll take a whole lot for me to settle
Mm, she the devil
She a bad lil' bitch, she a rebel
She put her foot to the pedal
It'll take a whole lot for me to settle
Walk on by
Walk on by
Walk on by
Walk on by
Walk on by

---
## [KateBiel/2023_PersonalProject_WebXR_KanaSmash](https://github.com/KateBiel/2023_PersonalProject_WebXR_KanaSmash)@[e0d7d5fc50...](https://github.com/KateBiel/2023_PersonalProject_WebXR_KanaSmash/commit/e0d7d5fc50bee049a1d8ce2a495e4e4b70d82533)
#### Thursday 2023-08-24 03:01:44 by KateBiel

Updated Night Mode and UI with functional Kana buttons

: Enhanced the night mode scene for a better user experience.
Refined the user interface for improved clarity and interaction.
Integrated new shaders for enhanced visuals.
Enabled kana buttons to correspond with the romaji displayed on the canvas, ensuring seamless interaction and learning.

ChatGPT
In this update, we've made several improvements to enhance the gameplay experience. Firstly, the night mode scene has been enhanced, offering a more user-friendly ambiance. We've also refined the user interface, emphasizing clarity and smoother interaction. To enrich the visuals, new shaders have been integrated. Furthermore, we've ensured that the kana buttons now correspond seamlessly with the romaji displayed on the canvas, optimizing both interaction and the learning process.

---
## [Ninlives/nix](https://github.com/Ninlives/nix)@[b13fc7101f...](https://github.com/Ninlives/nix/commit/b13fc7101fb06a65935d145081319145f7fef6f9)
#### Thursday 2023-08-24 03:19:24 by Robert Hensing

Add positive source filter

Source filtering is a really cool Nix feature that lets us avoid a
lot of rebuilds, which speeds up the iteration cycle a lot in cases
where the relevant source files aren't actually modified.

We used to have a source filter that marked a few files as irrelevant,
but this is the wrong approach, as we have many more files that are
irrelevant. We may call this negative filtering.

This commit switches the source filtering to positive filtering, which
is a lot more robust. Instead of marking which files we don't need
we marked the files that we do need.

It's a superior approach because it is fail safe. Instead of allowing
build performance problems to creep in over time, we require that all
source inputs are declared.

I shouldn't have to explain that declaring inputs is a good practice,
so I'll stop over-explaining here.

I do have to acknowledge that this will cause a build failure when the
filter is incomplete. This is *good*, because it's the only realistic
way we could be reminded of these problems. These events will be
infrequent, so the small cost of extending the filter is worth it,
compared to the hidden cost of longer dev cycles for things like tests,
docker image, etc, etc.

(Also rebuilding Nix for stupid unnecessary reasons makes my blood boil)

---
## [Citadel-Station-13/Citadel-Station-13-RP](https://github.com/Citadel-Station-13/Citadel-Station-13-RP)@[69d6d9d4e1...](https://github.com/Citadel-Station-13/Citadel-Station-13-RP/commit/69d6d9d4e1d72089acb1754bace58625d27c6571)
#### Thursday 2023-08-24 03:54:15 by CharlesWedge

Let Slip the Dogs of War (#5905)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## The Machines Rise
With the recent sector wide hack rogue synthetics have become a problem
in the sector. What's worse now corrupted fabricators are even building
more combat designs! With an increasingly dangerous galaxy, it seems
that mercenaries will not be the only threat brave explorers and
security teams may face today. All security forces are advised to stay
on the lookout for the latest threat to the galaxy, and those not
equipped to take them on are advised, stay well out range!

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
As we want to move away for humanoid threats for simple mobs, I feel it
necessary to shore up killer machines as more advanced type of enemy to
take the place of humans in terms of 'dangerous opponents'. The current
selection of machines mobs tend to be more niche in function (we can't
exactly use the nanite horror as common enemies). Also there is a bigger
maint drone now because the smaller ones weren't bad enough, least these
ones are easier to hit.

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
add: 4 New Hostile Drones, Three Dogs (including one sniper), and a
Maint Drone.
add: New News article elaborating on recent events.
tweak: drones are now part of the same faction as hivebots. This means
evil bots will now cooperate (Hivebots are being updated next).
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: BlueWildrose <57083662+BlueWildrose@users.noreply.github.com>

---
## [CliffracerX/Skyraptor-SS13](https://github.com/CliffracerX/Skyraptor-SS13)@[cd8a55f9d5...](https://github.com/CliffracerX/Skyraptor-SS13/commit/cd8a55f9d54bd82fca9605e88169c96d79558f5d)
#### Thursday 2023-08-24 04:43:39 by Rhials

Adds a handful of Ninja Hacking MODule interactions of varying usefulness (#77707)

## About The Pull Request

Adds a few new interactions with the Ninja's ~~right click multipurpose
trolling tool~~ Hacking MOD Module. These new effects are not tied to
objectives and are geared towards expanding the ninja's access,
disabling equipment, and giving them more ways to punk the crew.

### **Useful additions**
Ninjas can now hack open **windoors** and **elevator control panels**.
Both trigger emag_act() when hacked, opening in the case of the windoor,
and disabling the access restrictions _(and also maybe the safeties)_ in
the case of the elevator controls.

**Buttons** can also be emagged by the hacking modules, which removes
their access restrictions.

Hacking a **camera** will now EMP it, disabling it for about 90 seconds.
This can especially useful when trying to complete objectives, and works
better than smashing the cameras with your sword or lugging around
tools.

**Firelocks** can be right-click opened now too, thanks to the hacking
MODule.

**Energy guns** of all variety, useless to a ninja since they can't use
ranged weapons, can now be drained and used to charge your suit. This
takes a brief do_after to complete, so pulling it off mid-combat may be
as risky as it is stylish.

### **Being a nuisance**

**Vendors** can be hacked, expending some charge to trigger the "throw"
wire, making it launch inventory at anyone who passes by.

You can now hack **simplebots**, expending some charge from your suit to
overload and detonate them. It's faster than tipping, and far more
tragic. Sentient simplebots should take care when a ninja is around.

### **Sabotage opportunities**

The **recycler** can now be hacked. This takes 30 seconds and notifies
the AI, just like the communications console hack. Completing the hack
will emag it. That's it.

Hacking the **tram control console** will trigger an extended Tram
Malfunction event, and can be repeated after the event is done. This can
only be done to the "main" tram of the map, which I forsee will be an
absolute nightmare to complete on highpop tramstation.

Neither of these, presently, contribute towards any objectives. They can
be useful for diverting attention, but I see them more as ways for an
overachieving ninja to flex or continue the chaos after their objectives
are complete.

### **OH ALSO**

Hacking open doors costs energy. This really shouldn't be an issue just
remember to recharge sometimes.

The charge drains and do_after lengths for all of these were chosen on
vibes. In all honesty I think the drainage values don't _really_ matter,
due to how easy recharging is, but I had a hard time settling on how
long some of these hack do_afters should take (even if I know they
probably won't matter either).

## Why It's Good For The Game

Being able to hack open airlocks but not windoors always irked me. I
figured that they would be openable like any other door, and that losing
their status as a "-1 dash charge gate" wouldn't be a big enough balance
change to spark arguments. The same philosophy extends to buttons and
elevator controls.

Sapping power from eguns expands on the list of sources energy can be
siphoned from. You can also use it to disarm opponents (like the badass
ninja you are), take emergency charge from a recently-gored officer's
disabler, or dunk on security by draining their entire armory.

Hacking simplebots, vendors, and by extension elevator lifts (since that
also disables the safeties!) give opportunities for minor sabotage. Not
meant to be super disruptive, just a bit silly and annoying for the
crew.

The recycler/tram hacking in particular are meant to be bonus goals,
only sought out by the ballsiest (or more likely boredest) of ninjas.

I see all of these additions as expanding upon the current abilities of
the ninja (not really making them much more powerful, just expanding
their flexibility), or providing more interactions to have fun (and
antagonize the crew) with when not mainlining their objectives.
## Changelog
:cl: Rhials
add: Ninjas can now temporarily disable cameras with the Ninja MOD
right-click hacking ability.
add: Ninjas can emag windoors, elevator controls, and buttons with their
hacking ability.
add: Ninjas can drain the power from energy weaponry, adding the charge
to their MODsuit.
add: Ninjas can now hack simplebots, overloading and detonating them
after a brief delay.
add: Ninjas can now hack vendors, causing them to eject their inventory
at people.
add: Ninjas can now hack the recycler, which notifies the AI and emags
it once complete.
add: Ninjas can now trigger an extended tram malfunction by hacking the
tram control console.
add: Ninjas can now hack open firelocks (temporarily) with right-click.
balance: Hacking open doors with the Ninja Hacking MODule will subtract
a paltry amount of energy from your suit.
/:cl:

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[d9eefb4e3c...](https://github.com/git-for-windows/git/commit/d9eefb4e3c9edc24d38331ede2aebaaaf028179f)
#### Thursday 2023-08-24 05:22:38 by Johannes Schindelin

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
## [MarcusCaparini/Competative_Programming](https://github.com/MarcusCaparini/Competative_Programming)@[e29ed6fb3b...](https://github.com/MarcusCaparini/Competative_Programming/commit/e29ed6fb3bed90cc3ef1da9fdb444285e61a4b42)
#### Thursday 2023-08-24 06:04:59 by MarcusCaparini

Add Moderate difficulty problem. 4.5

Annoying thing about this code was that you'd expect the period about which the string returns to it's base form to be along the lines of "string.length()-1" or something. 
However, there's a notable case where string.length() returns a number of the form 2+3*n, where n is a positive integer. I eventually found a solution to these, but then realized that there were other, non-obvious exceptions.
In my rage, I have brute forced finding the period. Yes, I am ashamed.

---
## [mcx/koreader](https://github.com/mcx/koreader)@[4acf131071...](https://github.com/mcx/koreader/commit/4acf131071c704863d0d66f78f1b2314df9c3164)
#### Thursday 2023-08-24 06:20:47 by NiLuJe

ReaderActivityIndicator: Oh god, my eyes, they buuuuurn.

Make this a real boy, with a transient lipc handle.
And get rid of the insane 1s sleep on affected ReaderView paints,
because ouchy.

This is completely deprecated anyway, so this is entirely pointless,
and mainly to prevent implementation details from creeping into
reader.lua.

---
## [ModyQyW/naming-cheatsheet](https://github.com/ModyQyW/naming-cheatsheet)@[8bcb483976...](https://github.com/ModyQyW/naming-cheatsheet/commit/8bcb4839762053a095ee8cbbf3b4f5b471d01181)
#### Thursday 2023-08-24 06:46:29 by tebb

docs: improve a/hc/lc pattern order explanation (#40)

Thank you.  This cheatsheet is very useful.

If I understood the logic, my changes to README.md may be helpful.  If not, sorry :)

Also ... Could you add shouldUpdateComponent and shouldComponentUpdate into the table (or an extension to the table below Note:).  It isn't obvious to me which columns 'should', 'Update' and 'Component' are in because 'Update' is the verb (action?).

Thanks.

---
## [zNightlord/MCprep](https://github.com/zNightlord/MCprep)@[a34b01aa69...](https://github.com/zNightlord/MCprep/commit/a34b01aa69f7e215a0cd6ec46665e1c15a0a78ca)
#### Thursday 2023-08-24 07:27:50 by mahid

Added type annotations and use of Path
Replaced some instances of os.path with the Path object from pathlib for
readability. Also added type annotations to MCprepEnv as we're moving
towards that. This also means MCprep will not work at all in Blender
2.7x due to the use of new syntax.

This will be the first in a long process of modernizing MCprep's code
with 2.8 style code. Blender 2.7x users may not be happy, but it's for
the better. If anything, 6 years worth of 2.7x support was a mistake (in
my opinion), as it limited what we could do and opened MCprep to even
more bugs (like in Blender 2.93 with make_annotations, which ironically
now is deprecated).

---
## [korbal/compost-v3](https://github.com/korbal/compost-v3)@[8c82f18c2c...](https://github.com/korbal/compost-v3/commit/8c82f18c2c39a0ee5cccab9c11d0c18381f46454)
#### Thursday 2023-08-24 07:40:27 by Balint Korosi

added api_key but doesnt work with fucking env variables. fuck you

---
## [evverx/libbpf](https://github.com/evverx/libbpf)@[b064c40d94...](https://github.com/evverx/libbpf/commit/b064c40d9460c34d8fb539cf0042b298b888cdd4)
#### Thursday 2023-08-24 10:02:48 by Daniel Borkmann

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
## [evverx/libbpf](https://github.com/evverx/libbpf)@[d7e583a6ea...](https://github.com/evverx/libbpf/commit/d7e583a6eac64a79c21f1a749e6b3d371b884365)
#### Thursday 2023-08-24 10:02:48 by Daniel Borkmann

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
## [KathrinBailey/Bubberstation](https://github.com/KathrinBailey/Bubberstation)@[4537b1e980...](https://github.com/KathrinBailey/Bubberstation/commit/4537b1e980f226f2f6a18ef1c92d6ffc3e3b6ac4)
#### Thursday 2023-08-24 10:11:40 by Bloop

[MISSED MIRROR] New space ambient track (#76547) (#22449)

New space ambient track (#76547)

## About The Pull Request

Adds a new space ambient track made by me to the game, supposed to be a
bit scarier than the others that were recently added as I feel that
they're a bit too happy (not to diss I really like them), also cleaned
up a bit of ambience.dm as the medical portion of it didn't follow the
same rules as the other ones. also also this will only be used for
tgstation so license wise I think this is CC BY-SA 3.0 but I'm not sure
so correct me if I'm wrong, also this is my first PR so yeah. Here's a
link to listen to the track https://voca.ro/18WvrGORDDdR

## Why It's Good For The Game

Variety is the spice of life.

## Changelog

:cl:
sound: A new ambient track will now play in space
/:cl:

Co-authored-by: atlasle <132299254+atlasle@users.noreply.github.com>

---
## [klaoun/linux](https://github.com/klaoun/linux)@[4542057e18...](https://github.com/klaoun/linux/commit/4542057e18caebe5ebaee28f0438878098674504)
#### Thursday 2023-08-24 11:06:54 by Linus Torvalds

mm: avoid 'might_sleep()' in get_mmap_lock_carefully()

This might_sleep() goes back a long time: it was originally introduced
way back when by commit 010060741ad3 ("x86: add might_sleep() to
do_page_fault()"), and made it into the generic VM code when the x86
fault path got re-organized and generalized in commit c2508ec5a58d ("mm:
introduce new 'lock_mm_and_find_vma()' page fault helper").

However, it turns out that the placement of that might_sleep() has
always been rather questionable simply because it's not only a debug
statement to warn about sleeping in contexts that shouldn't sleep (which
was the original reason for adding it), but it also implies a voluntary
scheduling point.

That, in turn, is less than desirable for two reasons:

 (a) it ends up being done after we successfully got the mmap_lock, so
     just as we got the lock we will now eagerly schedule away and
     increase lock contention

and

 (b) this is all very possibly part of the "oops, things went horribly
     wrong" path and we just haven't figured that out yet

After all, the whole _reason_ for having that get_mmap_lock_carefully()
rather than just doing the obvious mmap_read_lock() is because this code
wants to deal somewhat gracefully with potential kernel wild pointer
bugs.

So then a voluntary scheduling point here is simply not a good idea.

We could certainly turn the 'might_sleep()' into a '__might_sleep()' and
make it be just the debug check that it was originally intended to be.

But even that seems questionable in the wild kernel pointer case - which
again is part of the whole point of this code.  The problem wouldn't be
about the _sleeping_ part of the page fault, but about a bad kernel
access.  The fact that that bad kernel access might happen in a section
that you shouldn't sleep in is secondary.

So it really ends up being the case that this is simply entirely the
wrong place to do this debug check and related scheduling point at all.

So let's just remove the check entirely.  It's been around for over a
decade, it has served its purpose.

The re-schedule will happen at return to user space anyway for the
normal case, and the warning - if we even need it - might be better off
done as a special case for "page fault from kernel mode" once we've
dealt with any potential kernel oopses where the oops is the relevant
thing, not some artificial "scheduling while atomic" test.

Reported-by: Mateusz Guzik <mjguzik@gmail.com>
Link: https://lore.kernel.org/lkml/20230820104303.2083444-1-mjguzik@gmail.com/
Cc: Matthew Wilcox <willy@infradead.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [Proxima-Project/Proxi-Eris](https://github.com/Proxima-Project/Proxi-Eris)@[013f53a9b1...](https://github.com/Proxima-Project/Proxi-Eris/commit/013f53a9b1bb6f0e8188f8e3e7c0aeaf10839f94)
#### Thursday 2023-08-24 12:34:15 by евиё

Titanium material (#8)

* adding titanium

may the god forgive me for editing base

* fixes my fuck ups

---
## [downthecrop/2009scape-mirror](https://github.com/downthecrop/2009scape-mirror)@[c52e02936d...](https://github.com/downthecrop/2009scape-mirror/commit/c52e02936d13d0ed6a260c6584ea49fd5528030a)
#### Thursday 2023-08-24 14:00:08 by Zerken

Audio refactor continued

Implemented admin audio command ::audio audioId loops[optional]
Implemented admin globalaudio command ::globalaudio audioId radius playername (plays from that players location) or can be used by coords ::globalaudio audioId radius x y z
Refactored the following sounds:
Tribal totem quest Cromperty teleport (fixed looping)
Vinesweeper tool leprechaun teleport sound (Corrected this sound so it does not loop 10 times)
Antifire and poision immunity 30 seconds remaining tick tock sounds and sound of the potions expiring (Fixed it so it plays the correct number of tick tocks)
Sound when summoning a familiar (All familiars were using the summon unicorn sound. It is now defaulted to the normal summoning sound instead of the unicorn summon sound. All familiars on first summon have a their own sounds that will need to be implemented later)
Door and gate sounds
Bank interface sounds
Unicorn stallion special move sound
Agility pyramid rolling block sounds
Prayer book sounds
Lunar stat spy
Hunter falconry
Picking items in a field like potatoes
Ectophial teleport and refill
Summoning pouch creation and renewing points
Runecrafting at altar sound
Making finished and unfinished potions
Cutting gems
Entering giant mole area
Praying at an altar
Warriors guild animator sounds
Chiseling limestone
Spirit wolf special move sound
Telegrab spell sound
Glassblowing sound
Strong of security opening reward chest creaking sound
Butterfly net sound
Desert rug travel rise and descend sound
Enchanting bolts
Woodcutting tree falling and chopping sound
Hunter setting up dismantling traps and pitfall sounds
Explorers ring run energy restore sound
Farming: Raking, adding compost to patch, picking from fruit trees, seed dibb, using plant cure on patch, opening/closing/adding to/from compost bin
Mage training arena alchemy spell sounds
Breaking bones to peaches/bananas tab sound
Casting silver sickle bloom
Entrana magic door teleport
Cabbage teleport
Teleother cast sound
Fairy ring teleport sound
Lunar vengeance spells
Running out of prayer sound
Lunar (non teleport) spells
Super heat and bones to bananas normal spell book sounds
Equip/unequip item sound
Revenant combat sounds
Herb cleaning sound
Emptying buckets/bowls/jugs of water
Making cannonballs at a furnace
Digging with a spade
Peer the seer fremmenik trials challenge: heating items on the range
Blessing a spirit shield at a POH altar
ContentAPI function stun sound
Picking up items off the ground
Eating food sound
Cooking and intentionally burning food
Drinking a potion
Warriors guild catapult
Pulling wilderness teleport levers
Offering bones on a POH altar
Slashing spider webs in Varrock sewers
Entering POH portal teleport sound
GE exchanging item set sound
Jumping wilderness ditch
Dragon axe special
Digging up a farming patch
Lunar heal spells
Chaos elemental projectile impact sounds
Mounted glory teleport
Lunar share and boost potion spell
Dwarf multi cannon setup, rotate, and firing sounds
NPC attacking sound
Enchanted bolt effect combat sound

---
## [norbert-acedanski/supernatural-guide](https://github.com/norbert-acedanski/supernatural-guide)@[d38f338d1b...](https://github.com/norbert-acedanski/supernatural-guide/commit/d38f338d1b1cc07aac78bd907cf58b0fa137c002)
#### Thursday 2023-08-24 14:15:36 by Norbert Acedanski

Add Vengeful spirit, Witch, Angel, Demon Crowley appearances.
Add Reaper clue.
Add GOD clue and kill method.
Add Darkness clues.
All episodes done.
S11E23

---
## [norbert-acedanski/supernatural-guide](https://github.com/norbert-acedanski/supernatural-guide)@[3c76f7531e...](https://github.com/norbert-acedanski/supernatural-guide/commit/3c76f7531ec8c73f78d680c388c99a37a006cb85)
#### Thursday 2023-08-24 14:18:48 by Norbert Acedanski

Add Demon-killing Knife, Angel Blade, Demonic handcuffs usages.
Add Human Soul, Word of GOD, Lucifer's Cage appearances.
S11E06

---
## [Danielkaas94/DTAP](https://github.com/Danielkaas94/DTAP)@[373d05c715...](https://github.com/Danielkaas94/DTAP/commit/373d05c7151f5f5ee565e05731ef675ff7e7aeeb)
#### Thursday 2023-08-24 14:35:01 by Daniel Kaas Bundgaard Jørgensen

🔥😈🔥 Evilized 🔥😈🔥

It seems like I'm trapped in my own dreams
It feels like the walls are caving in
When I close my eyes and start to fall asleep
Something's evil and dark, takes over me

I never feel safe to dream
I won't close my eyes and sleep
I fear that the dreams I dream are real

You need me so trust me - I make you feel free
You're under my spell now - So welcome to hell

It's getting hotter
Feel how the flames are growing
Surrounded by fire
You're inside my evil dream, my friend

Inside this dream all is painted black
Hundreds of doors but there's no way back
The road that I'm on never seems to end
A sinister feeling closing in

You need me so trust me - I make you feel free
You're under my spell now - So welcome to hell

It's getting hotter
Feel how the flames are growing
Surrounded by fire
You're inside my evil dream, my friend

So now you are trapped inside this dream
Only the walls can hear you scream
You can't close your eyes when you're falling down
Your heartbeat has stopped

It's getting hotter
Feel how the flames are growing
Surrounded by fire
You're inside my evil dream, my friend
It's getting hotter
Feel how the flames are growing
Surrounded by fire
You're inside my evil dream, my friend

---
## [Danielkaas94/DTAP](https://github.com/Danielkaas94/DTAP)@[d7a13058e2...](https://github.com/Danielkaas94/DTAP/commit/d7a13058e2e92a0eba650ab6c669bf672dc0e24a)
#### Thursday 2023-08-24 14:35:47 by Daniel Kaas Bundgaard Jørgensen

Calling Your Name 🗣️

Serious, is this just another dream
So delirious the way that you make me feel
I can't control myself when you are in my sight
Too dangerous haunting me through the night

You're the reason I can't sleep at night
I hear voices in my head...

The Gods must be insane
They keep calling, keep calling your name
My heart is burning in flames
They keep calling, keep calling your name...

I don't know... maybe you got another man?
So talk to me, I hope that we are more than friends
I would give you all I got just to have you by my side
Come on let me know, give me a sign

You're the reason I can't sleep at night
I hear voices in my head...

The Gods must be insane
They keep calling, keep calling your name
My heart is burning in flames
They keep calling, keep calling your name...
It echoes through the night
I wanna hold you tight
I haven't slept for weeks

'Thou I only know your name
In darkness you're my light
Make the shadows go to sleep

---
## [Danielkaas94/DTAP](https://github.com/Danielkaas94/DTAP)@[f3b6f6dadc...](https://github.com/Danielkaas94/DTAP/commit/f3b6f6dadcb369afb57455f4cb6fcd5e9deb026f)
#### Thursday 2023-08-24 14:37:32 by Daniel Kaas Bundgaard Jørgensen

😡😠 Vengeance 😠😡

I have worked for nothing, slaved in vain
All those years that I've been pushed around
They better watch their backs now, those who gave me pain
'Cause vengeance screams their names tonight

All of you sinners
You better run and try to hide
You've all been dreaming
So you better hide to stay alive

Marching out now, out to kill
The rain of blood has just begun
Blocked emotions now released
In darkness wou will fear my name
All of you sinners
You better run and try to hide
You've all been dreaming
So you better hide to stay alive
All of you sinners

Can you hear me?
I'm closing in on you
Can't you fell it...

I will show no mercy wou will not survive
'Cause vengeance screams your names tonight

All of you sinners
You better run and try to hide
You've all been dreaming
So you better hide to stay alive

---
## [Danielkaas94/DTAP](https://github.com/Danielkaas94/DTAP)@[7035ca1f5a...](https://github.com/Danielkaas94/DTAP/commit/7035ca1f5add7c865556b7f6a4fb11a1cd5a770e)
#### Thursday 2023-08-24 14:45:16 by Daniel Kaas Bundgaard Jørgensen

🔥💀🔥 In Flames You Burn 🔥💀🔥

Oh God forbid this bloody war
I see my knights falling one by one
So here I am, in this fight I'm alone
I'm stuck here in this hellhole on my own

Taste the blood, tears of pain
Memories from the past strike through my mind
My royal blood, begins to boil
Deadly wounds can't stop me now, I still stand strong
I just can't die

Surrender is no option for me now
Bless those souls I send to hell
If you dare just look into my eyes
My steel is warm my face is stained with blood

One by one I hit them to the ground
One by one I see their heads roll
Anyone against me taste my sword
Anyone who'll challenge me will die

You, killed my men, raped my land and you ruined our lives
Still I stand in command in flames you burn
You will die by my hand forever you're condemned
Cause I am in command in flames you burn

No it's no use for you to beg, I will send you down to hell
I can't die my faith is far too strong
In the flames of hell is where you belong

One by one I hit them to the ground
One by one I see their heads roll
Anyone against me taste my sword
Anyone who'll challenge me will die

You, killed my men, raped my land and you ruined our lives
Still I stand in command in flames you burn
You will die by my hand forever you're condemned
Cause I am in command in flames you burn

You, killed my men, raped my land and you ruined our lives
Still I stand in command in flames you burn
You will die by my hand forever you're condemned
Cause I am in command in flames you burn

---
## [SomeRandomOwl/Skyrat-tg](https://github.com/SomeRandomOwl/Skyrat-tg)@[2b80714afa...](https://github.com/SomeRandomOwl/Skyrat-tg/commit/2b80714afa150d6f9e335f8ae68ef84444d52506)
#### Thursday 2023-08-24 15:24:29 by SkyratBot

[MIRROR] Base Female sprite tweaks [MDB IGNORE] (#22924)

* Base Female sprite tweaks (#77407)

## About The Pull Request

ASS STUFF HAS BEEN REMOVED BUT I STILL HATE IT

This PR tones down the proportions of the female base sprites, as
currently they have about SIX extra pixels on the ass and a random pixel
missing from the neck, which breaks some hairstyles & makes the neck
look quite stupid.
It also adds a couple pixels to the male one because theirs was so
stupidly SMALL it looked like they had no tailbone (still does, kind
of).

Here is the current sprite

![image](https://github.com/tgstation/tgstation/assets/81964183/1bf22dd7-2b06-4632-8617-b89b3b1c8d2c)
& new sprite (only neck pixel removed)

![image](https://github.com/tgstation/tgstation/assets/81964183/b1228e01-23e0-4508-86a6-bc8e73b0fcd0)

## Why It's Good For The Game

Fixes some hairs

![image](https://github.com/tgstation/tgstation/assets/81964183/3b293cf9-2661-4358-a327-2882acb93067)

## Changelog

:cl:
image: fixes weird inconsistency on the neck and butt of the female base
sprite
/:cl:

* Base Female sprite tweaks

---------

Co-authored-by: Sheits <81964183+Sheits@users.noreply.github.com>

---
## [SomeRandomOwl/Skyrat-tg](https://github.com/SomeRandomOwl/Skyrat-tg)@[bd075740f4...](https://github.com/SomeRandomOwl/Skyrat-tg/commit/bd075740f45aaaafa41d388ed2120c0a0574121e)
#### Thursday 2023-08-24 15:24:29 by SkyratBot

[MIRROR] Chen And Garry's Ice Cream: Ice Cream DLC (LIZARD APPROVED!) [MDB IGNORE] (#22927)

* Chen And Garry's Ice Cream: Ice Cream DLC (LIZARD APPROVED!) (#77174)

## About The Pull Request

Authored with help and love from @ Thalpy

I scream for ice cream!!

![image](https://github.com/tgstation/tgstation/assets/10399117/db1e559b-7dab-499b-a076-8f12748ba2e8)

Introduces many new flavours of ice cream:
-Caramel
-Banana
-Lemon Sorbet
-Orange Creamsicle
-Peach (Limited Edition!)
-Cherry chip
-Korta Vanilla (made with lizard-friendly ingredients!)

![image](https://github.com/tgstation/tgstation/assets/10399117/99a87615-f55c-49be-8caf-2b1ac4c7f03f)

Korta Cones! Now too can Nanotrasen's sanitation staff enjoy the wonders
of ice cream!
You can also substitute custom ice cream flavours with korta milk!
Finally, the meaty ice cream lactose-intolerants asked for is in reach!

## Why It's Good For The Game

I always thought the ice cream vat could use more flavours. The custom
flavour besides, it isn't as intuitive to rename the cone and the added
variety is good. The lack of a banana flavour already was questionable.
All the ice cream flavours used a selection of five sprites, now it's
just one sprite and better supporting more additions.
Some of the flavours don't use milk! You can't do this with the custom
flavour, making it slightly more interesting.

## Changelog
:cl: YakumoChen, Thalpy
add: Chen And Garry's Ice Cream is proud to debut a wide selection of
cool new frozen treat flavours on a space station near you!
add: Chen And Garry's Ice Cream revolutionary Korta Cones allow our ice
cream vendors to profit off the lizard demographic like never before!
code: Ice cream flavours now are all greyscaled similarly to GAGs
/:cl:

* Chen And Garry's Ice Cream: Ice Cream DLC (LIZARD APPROVED!)

---------

Co-authored-by: YakumoChen <king_yoshi42@yahoo.com>

---
## [JuhTyg010/Zapoctovy_program_1](https://github.com/JuhTyg010/Zapoctovy_program_1)@[ac8e7d40e4...](https://github.com/JuhTyg010/Zapoctovy_program_1/commit/ac8e7d40e43d1b36cd3e296b0d9556d4066e7671)
#### Thursday 2023-08-24 15:35:50 by JuhTyg010

Added comments

I think I hate myself, this was more pain than the actual coding I hate this

---
## [cyphar/runc](https://github.com/cyphar/runc)@[be892f00e6...](https://github.com/cyphar/runc/commit/be892f00e61dd8ba54b372ecdfe0f16dd4400479)
#### Thursday 2023-08-24 15:52:07 by Aleksa Sarai

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
confusing errors). This is not necessary for most usages of
/proc/thread-self (such as using /proc/thread-self/fd/$n directly) but
operating on the actual inodes associated with the tid requires this
locking.

In addition, CentOS's kernel is too old for /proc/thread-self, which
requires us to emulate it -- however in rootfs_linux.go, we are in the
container pid namespace but /proc is the host's procfs. This leads to
the incredibly frustrating situation where there is no way (on pre-4.1
Linux) to figure out which /proc/self/task/... entry refers to the
current tid. We can just use /proc/self in this case.

Yes this is all pretty ugly. I also wish it wasn't necessary.

Signed-off-by: Aleksa Sarai <cyphar@cyphar.com>

---
## [JordiPallaresllorens/styles](https://github.com/JordiPallaresllorens/styles)@[3f6ede9d16...](https://github.com/JordiPallaresllorens/styles/commit/3f6ede9d168ad8471bf28cc44f3c90b5c7d7fe84)
#### Thursday 2023-08-24 17:02:56 by JordiPallaresllorens

Releasing acm-sig-proceedings-long-author-list.csl acm-sig-proceedings.csl acta-palaeontologica-polonica.csl al-jamiah-journal-of-islamic-studies.csl american-chemical-society.csl american-institute-of-physics.csl american-journal-of-botany.csl american-journal-of-respiratory-and-critical-care-medicine.csl american-medical-association-no-url-alphabetical.csl american-medical-association.csl american-society-for-horticultural-science.csl american-sociological-association.csl amsterdam-university-press-academic.csl angiology.csl apa-6th-edition-no-ampersand.csl apa-6th-edition.csl apa-annotated-bibliography.csl apa-cv.csl apa-eu.csl apa-no-ampersand.csl apa-no-doi-no-issue.csl apa-no-initials.csl apa-numeric-superscript-brackets.csl apa-numeric-superscript.csl apa-old-doi-prefix.csl apa-single-spaced.csl apa-with-abstract.csl apa.csl arachnologische-mitteilungen.csl arcadia-science.csl archives-of-medical-research.csl arkivoc.csl association-for-computational-linguistics.csl australasian-journal-of-philosophy.csl begell-house-apa.csl bern-university-of-applied-sciences-school-of-agricultural-forest-and-food-sciences-hafl.csl bibliothek-forschung-und-praxis.csl bio-protocol.csl biochemical-society-transactions.csl biologiceskie-membrany.csl biomolecular-concepts.csl biotechnology-and-bioprocess-engineering.csl bluebook-law-review.csl boletin-de-pediatria.csl bristol-university-press.csl business-and-human-rights-journal.csl cahiers-mondes-anciens.csl cambridge-university-press-author-date-cambridge-a.csl cambridge-university-press-author-date.csl cardiff-university-harvard.csl cell.csl chemistry-education-research-and-practice.csl chicago-annotated-bibliography.csl chicago-author-date.csl chicago-fullnote-bibliography-short-title-subsequent.csl chicago-fullnote-bibliography-with-ibid.csl chicago-fullnote-bibliography.csl chicago-library-list.csl chicago-note-bibliography-with-ibid.csl chicago-note-bibliography.csl citation-compass-apa-note.csl computer-supported-cooperative-work.csl constructivist-foundations.csl council-of-science-editors-author-date.csl czech-journal-of-international-relations.csl dependent/anaesthesia-and-intensive-care-medicine.csl dependent/cancer-cell.csl dependent/cell-chemical-biology.csl dependent/cell-genomics.csl dependent/cell-host-and-microbe.csl dependent/cell-metabolism.csl dependent/cell-reports-medicine.csl dependent/cell-reports-methods.csl dependent/cell-reports-physcial-science.csl dependent/cell-reports.csl dependent/cell-stem-cell.csl dependent/cell-systems.csl dependent/chem-catalysis.csl dependent/chem.csl dependent/conservation-science-and-practice.csl dependent/consumption-and-society.csl dependent/critical-and-radical-social-work.csl dependent/current-biology.csl dependent/development-growth-differentiation.csl dependent/developmental-cell.csl dependent/diagnostic-histopathology.csl dependent/emotions-and-society.csl dependent/european-journal-of-politics-and-gender.csl dependent/european-social-work-research.csl dependent/evidence-and-policy.csl dependent/families-relationships-and-societies.csl dependent/global-discourse.csl dependent/global-political-economy.csl dependent/global-social-challenges-journal.csl dependent/harvard-the-university-of-melbourne.csl dependent/hgg-advances.csl dependent/immunity.csl dependent/international-journal-of-care-and-caring.csl dependent/iscience.csl dependent/jci-insight.csl dependent/joule.csl dependent/journal-of-gender-based-violence.csl dependent/journal-of-poverty-and-social-justice.csl dependent/journal-of-psychosocial-studies.csl dependent/journal-of-public-finance-and-public-choice.csl dependent/journal-of-the-american-society-for-mass-spectrometry.csl dependent/justice-power-and-resistance.csl dependent/longitudinal-and-life-course-studies.csl dependent/magnetic-resonance-in-medicine.csl dependent/matter.csl dependent/med.csl dependent/medicine.csl dependent/molecular-cell.csl dependent/molecular-ecology.csl dependent/molecular-physics.csl dependent/molecular-therapy-methods-and-clinical-development.csl dependent/molecular-therapy-nucleic-acids.csl dependent/molecular-therapy-oncolytics.csl dependent/molecular-therapy.csl dependent/monash-university-harvard.csl dependent/negative-results.csl dependent/neuron.csl dependent/nursing-open.csl dependent/obstetrics-gynaecology-and-reproductive-medicine.csl dependent/one-earth.csl dependent/orthopaedics-and-trauma.csl dependent/paediatrics-and-child-health.csl dependent/patterns.csl dependent/policy-and-politics.csl dependent/star-protocols.csl dependent/structure.csl dependent/surgery-oxford.csl dependent/the-american-journal-of-human-genetics.csl dependent/the-american-journal-of-sports-medicine.csl dependent/turabian-fullnote-bibliography.csl dependent/voluntary-sector-review.csl dependent/work-in-the-global-economy.csl duale-hochschule-baden-wurttemberg-department-of-international-business.csl early-music-history.csl ecosistemas.csl elsevier-american-chemical-society.csl emerald-harvard.csl energy-research-and-social-science.csl engineering-technology-and-applied-science-research.csl environmental-and-engineering-geoscience.csl environmental-conservation.csl european-review-of-agricultural-economics.csl european-review-of-international-studies.csl exploration-of-targeted-anti-tumor-therapy.csl food-and-agriculture-organization-of-the-united-nations-numeric.csl frontiers.csl fundamental-and-applied-limnology.csl gaceta-sanitaria.csl gender-and-society.csl genetics-and-molecular-biology.csl geographical-analysis.csl geographie-et-cultures.csl geophysical-journal-international.csl german-council-of-economic-experts.csl gnosis-journal-of-gnostic-studies.csl guide-des-citations-references-et-abreviations-juridiques.csl harvard-anglia-ruskin-university.csl harvard-deakin-university.csl harvard-stellenbosch-university.csl harvard-university-of-abertay-dundee.csl harvard-university-of-the-west-of-england.csl harvard-xi-an-jiaotong-liverpool-university.csl haute-ecole-de-gestion-de-geneve-iso-690.csl historical-materialism.csl hochschule-fur-soziale-arbeit-fhnw.csl howard-hughes-medical-institute.csl iainutuban-tarbiyah.csl iawa-journal.csl ieee-with-url.csl ieee.csl indian-journal-of-orthopaedics.csl intellect-newgen-books.csl international-union-of-crystallography.csl internet-archaeology.csl interpreting.csl isara-iso-690.csl iso690-author-date-es.csl journal-fur-kulturpflanzen-journal-of-cultivated-plants.csl journal-of-dental-traumatology.csl journal-of-emerging-investigators.csl journal-of-endodontics.csl journal-of-experimental-botany.csl journal-of-human-nutrition-and-dietetics.csl journal-of-law-medicine-ethics.csl journal-of-medical-internet-research.csl journal-of-neolithic-archaeology.csl journal-of-paleontology.csl journal-of-prosthodontics.csl journal-of-the-american-college-of-cardiology.csl journal-of-the-american-philosophical-association.csl journal-of-the-marine-biological-association-of-the-united-kingdom.csl jurnal-teknik-mesin-indonesia.csl karstenia.csl knee-surgery-sports-traumatology-arthroscopy.csl la-nouvelle-revue-du-travail.csl law-citation-manual.csl les-mondes-du-travail.csl lethaia.csl life-science-alliance.csl lund-university-school-of-economics-and-management.csl masarykova-univerzita-pravnicka-fakulta.csl medizinische-hochschule-hannover.csl medizinische-universitat-innsbruck-vancouver.csl microbiome-research-reports.csl modern-humanities-research-association-author-date.csl modern-humanities-research-association.csl modern-language-association.csl molecular-oncology.csl mots.csl natur-und-landschaft.csl netherlands-journal-of-geosciences-geologie-en-mijnbouw.csl norsk-apa-manual-note.csl norsk-apa-manual.csl norsk-henvisningsstandard-for-rettsvitenskapelige-tekster.csl north-pacific-anadromous-fish-commission-bulletin.csl nys-nydanske-sprogstudier.csl offa.csl oil-shale.csl open-window.csl organization-studies.csl palaeontology.csl paleobiology.csl pallas.csl physiotherapy-theory-and-practice.csl polish-archives-of-internal-medicine.csl polygraphia.csl pravnik.csl presses-universitaires-de-rennes.csl publicatiewijzer-voor-de-archeologie.csl raptor-journal.csl rassegna-degli-archivi-di-stato-bibliografia-generale.csl retina.csl review-of-international-studies.csl royal-society-of-chemistry.csl san-francisco-estuary-and-watershed-science.csl sciences-po-ecole-doctorale-author-date.csl sciences-po-ecole-doctorale-note-french.csl scientific-online-letters-on-the-atmosphere.csl silva-fennica.csl slovensko-drustvo-za-medicinsko-informatiko.csl smithsonian-institution-scholarly-press-author-date.csl smithsonian-institution-scholarly-press-note.csl sn-computer-science.csl social-science-history.csl society-of-biblical-literature-fullnote-bibliography.csl sodertorns-hogskola-oxford.csl springer-vancouver-brackets.csl stanovnistvo.csl stem-cell-reports.csl studii-teologice.csl survey-of-ophthalmology.csl taylor-and-francis-aip.csl taylor-and-francis-ama.csl taylor-and-francis-chicago-b-author-date.csl technische-universitat-dresden-betriebswirtschaftslehre-rechnungswesen-controlling.csl the-accounting-review.csl the-journal-of-clinical-investigation.csl the-journal-of-pain.csl the-quarterly-journal-of-economics.csl the-university-of-winchester-harvard.csl theses-de-sorbonne-universite.csl trames.csl travail-et-emploi.csl triangle.csl turabian-fullnote-bibliography-8th-edition.csl turcica.csl ucl-university-college-apa.csl ucl-university-college-harvard.csl uni-fribourg-theologie.csl united-states-international-trade-commission.csl universitat-basel-iberoromanistik.csl universitat-bern-institut-fur-sozialanthropologie.csl universite-de-bordeaux-ecole-doctorale-de-droit.csl universite-de-sherbrooke-histoire.csl universite-du-quebec-a-montreal-etudes-litteraires-et-semiologie.csl universite-du-quebec-a-montreal.csl university-of-gothenburg-apa-7th-edition-swedish-legislations.csl university-of-pretoria-harvard-theology-religion.csl uppsala-university-library-harvard.csl van-yuzuncu-yil-universitesi-fen-bilimleri-enstitusu.csl vancouver-alphabetical.csl vancouver.csl veterinary-clinical-pathology.csl veterinary-record-open.csl vox-sanguinis.csl wiley-was.csl world-politics.csl zeitschrift-fur-deutsche-philologie.csl zeitschrift-fur-geschichtsdidaktik.csl zitierguide-leitfaden-zum-fachgerechten-zitieren-in-rechtswissenschaftlichen-arbeiten.csl zoological-journal-of-the-linnean-society.csl bursa-uludag-universitesi-fen-bilimleri-enstitusu.csl bursa-uludag-universitesi-sosyal-bilimler-enstitusu-metinici-atif.csl bursa-uludag-universitesi-sosyal-bilimler-enstitusu.csl cell-numeric-superscript.csl dependent/archives-of-medical-research.csl dependent/energy-research-and-social-science.csl dependent/retina.csl dependent/stem-cell-reports.csl dependent/survey-of-ophthalmology.csl dependent/veterinary-record-open.csl harvard-the-university-of-melbourne.csl jci-insight.csl magnetic-resonance-in-medicine.csl monash-university-harvard.csl the-american-journal-of-human-genetics.csl turabian-fullnote-bibliography.csl world-politcs.csl

---
## [Sitanshu0101/Data-Analytics---Project-4---YouTube-Analytics](https://github.com/Sitanshu0101/Data-Analytics---Project-4---YouTube-Analytics)@[85fdb60053...](https://github.com/Sitanshu0101/Data-Analytics---Project-4---YouTube-Analytics/commit/85fdb600537299915f53171de9ed9fd40f245f00)
#### Thursday 2023-08-24 19:36:57 by Sitanshu Pathak

Overview

📊 Welcome to the Zorro Oz YouTube Data Analytics Project! 🎥

Explore the world of data-driven insights as we dive into the analytics journey of my own YouTube channel, Zorro Oz. 🚀 This repository encapsulates a meticulous exploration of the channel's performance, audience demographics, and content dynamics.

📈 Leveraging the power of the YouTube Studio analytics option, I've meticulously collected and processed the dataset, ensuring that null values and extraneous columns are eradicated. This robust data processing phase forms the foundation of accurate and reliable analyses.

🧹 Data cleaning was a crucial step in this journey. I've employed advanced techniques to not only fix spellings but also perform essential operations that enhance the integrity of the dataset. This meticulous attention to detail guarantees that our insights are based on accurate and coherent data.

💡 The true magic happens with Power BI. By harnessing its capabilities, I've brought the data to life through visually captivating representations. Dive into comprehensive visualizations that shed light on content performance, audience age groups, subscription status, and geographic location segments. 🌍 The gender framework adds an additional layer of understanding to these insights, allowing us to tailor our content to the preferences of our diverse audience.

🎯 Whether you're interested in understanding which videos resonate the most, the age groups that engage the most, or the locations where our content has the highest impact, this project has got it all covered. It's not just about the numbers; it's about the stories they tell.

🚀 Join me in this journey of discovery and insights, where data paints a picture that guides our content strategy and enhances our connection with the audience. Your curiosity is the key to unlocking the potential of Zorro Oz on YouTube!

Stay tuned for more updates as we continue to refine our content and strategies based on these valuable data-driven revelations. 🎉 #YouTubeAnalytics #DataDrivenDecisions #PowerBIInsights #AudienceEngagement

---
## [arzam16/mt6577_kernel_Acer_B1_A71](https://github.com/arzam16/mt6577_kernel_Acer_B1_A71)@[a2ab2d5102...](https://github.com/arzam16/mt6577_kernel_Acer_B1_A71/commit/a2ab2d510239ca2f086dee0ddc47d2d967768cd9)
#### Thursday 2023-08-24 19:44:12 by arzamas-16

Lower the logging level of battery subsystem

This shit is annoying as fuck and was hindering reading logs

---
## [LC4492/CM-Space-Station-13](https://github.com/LC4492/CM-Space-Station-13)@[f5784dabc7...](https://github.com/LC4492/CM-Space-Station-13/commit/f5784dabc77752802da20f2d14787667161d61ac)
#### Thursday 2023-08-24 19:49:04 by ihatethisengine

More portable cades tweaks and buffs (#3967)

# About the pull request

Despite making a lot of tweaks and changes to portable cades I barely
touched them in the game until recently. Now I have more experience and
can tweak it again.

1) You can now stack damaged cades and stack stores health of each cade.
You can repair stacked cades but it will take longer time.

2) Miniengi pamphlet allows faster repairs but only when cade is folded.

3) You can quickly collapse portable cades with crowbar if you have at
least miniengi skills.

4) You no longer need to have folded portable cade in hand in order to
repair it, but if you do, you can move while repairing.

# Explain why it's good for the game

1) It's extremely annoying to repair each individual cade in order to
stack them just because it got hit by a stray bullet once. Now you can
just ignore damage and keep going.

2) Yeah it took 10 second for PFC to repair each single cade. Really
long. Now it's 5 seconds, but only when folded and if you have miniengi
skills. Makes miniengi pamphlet a bit more relevant.

3) It was intended, but turned out it was a bit inconvenient. It was
faster to collapse by hand because you didn't need to deal with tools.
Now it requires just a crowbar and slightly faster. Also requires
miniengi skill to use crowbar.

4) First was just a bit annoying, second allows more mobility which is
the point of portable barricades.


# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl: ihatethisengine
balance: you can stack scratched portable cades if their HP at least
75%. Doing so will reduce the health of all barricades in the stack to
the level of the most damaged.
balance: you can repair stacked portable cades but it will take longer
time depending on how many cades in stack.
balance: miniengi skill makes repairs of folded portable cades faster
(10 seconds to 5 seconds, same as engineer).
balance: with engineering skill at least of miniengi you can collapse
deployed portable barricade with a crowbar (wrench is no longer
required, slightly faster (2 sec to 1.5 sec)).
balance: you no longer need to have folded portable cade in hand in
order to repair it.
balance: if you have folded portable cade in hand, you can move while
repairing it.
/:cl:

---------

Co-authored-by: ihatethisengine <treml.treml@yandex.ru>

---
## [LC4492/CM-Space-Station-13](https://github.com/LC4492/CM-Space-Station-13)@[3e9d54628d...](https://github.com/LC4492/CM-Space-Station-13/commit/3e9d54628d68fe91319ae87ad7ebd7aef9500811)
#### Thursday 2023-08-24 19:49:04 by Ben

Can no longer bypass Lesser Drone Limit (#4034)

# About the pull request

Users can no longer keep menu open and bypass lesser drone slots

# Explain why it's good for the game

Honestly kinda wish I didn't make this one, infinite lesser drones
sounds really funny.

# Changelog
:cl:
fix: You can no longer circumvent the lesser drone limit by keeping the
prompt open.
/:cl:

---
## [transpapers/transpapers.github.io](https://github.com/transpapers/transpapers.github.io)@[80cee88d8a...](https://github.com/transpapers/transpapers.github.io/commit/80cee88d8ad8b7b0700b845c59933747cd8c1c50)
#### Thursday 2023-08-24 19:57:40 by Sasha Lišková

Flatten form fields

You may be wondering why this took me weeks. The short version is I'm a
moron. The long version is that PDF documents come with a bunch of
metadata. The persistent form-field issues stemmed from the bare fact
that you cannot nicely unify the metadata of many documents from
different sources.

Form field data is now flattened into the document, effectively turning
it into absolutely positioned data. This was in the documentation and I
didn't notice. Yeah. That's what a graduate degree gets you in 2023, I
suppose. Woof. Jesus fucking Christmas, I'm stupid.

---
## [rmader/mpv](https://github.com/rmader/mpv)@[3d459832a8...](https://github.com/rmader/mpv/commit/3d459832a88a9bd2835b339cf6ca98f84aad0115)
#### Thursday 2023-08-24 19:57:57 by Dudemanguy

x11: support xorg present extension

This builds off of present_sync which was introduced in a previous
commit to support xorg's present extension in all of the X11 backends
(sans vdpau) in mpv. It turns out there is an Xpresent library that
integrates the xorg present extention with Xlib (which barely anyone
seems to use), so this can be added without too much trouble. The
workflow is to first setup the event by telling Xorg we would like to
receive PresentCompleteNotify (there are others in the extension but
this is the only one we really care about). After that, just call
XPresentNotifyMSC after every buffer swap with a target_msc of 0. Xorg
then returns the last presentation through its usual event loop and we
go ahead and use that information to update mpv's values for vsync
timing purposes. One theoretical weakness of this approach is that the
present event is put on the same queue as the rest of the XEvents. It
would be nicer for it be placed somewhere else so we could just wait
on that queue without having to deal with other possible events in
there. In theory, xcb could do that with special events, but it doesn't
really matter in practice.

Unsurprisingly, this doesn't work on NVIDIA. Well NVIDIA does actually
receive presentation events, but for whatever the calculations used make
timings worse which defeats the purpose. This works perfectly fine on
Mesa however. Utilizing the previous commit that detects Xrandr
providers, we can enable this mechanism for users that have both Mesa
and not NVIDIA (to avoid messing up anyone that has a switchable
graphics system or such). Patches welcome if anyone figures out how to
fix this on NVIDIA.

Unlike the EGL/GLX sync extensions, the present extension works with any
graphics API (good for vulkan since its timing extension has been in
development hell). NVIDIA also happens to have zero support for the
EGL/GLX sync extensions, so we can just remove it with no loss. Only
Xorg ever used it and other backends already have their own present
methods. vo_vdpau VO is a special case that has its own fancying timing
code in its flip_page. This presumably works well, and I have no way of
testing it so just leave it as it is.

---
## [warptools/warpforge](https://github.com/warptools/warpforge)@[60edd30fd6...](https://github.com/warptools/warpforge/commit/60edd30fd653ecf83315cac6c1f30ab55e34ebca)
#### Thursday 2023-08-24 20:05:38 by Eric Myhre

tests which maintain CLI help docs in the website repo.

... if you have it checked out in the appropriate relative path.
(I'm not yet attempting to introduce any closer coupling of repos.
In the long run, this is probably a great case for submodules again,
or possibly some dogfooding of warpforge's own relationships for
modules in a workspace (if we dare put that level of complex
self-hosting in our own path, which... may not be wise).  But that
won't improve velocity today, so, it's a job for later.)

This uses testmark to maintain the data again.

A few deps are bumped... so that we can use the new testmark suite
system.  That makes it really easy to do a large batch of similar
tests across multiple files.
((Amend: you no longer see that in the go mod diff here because
I've rebased this branch after something else which also forced
that same bump!))

I haven't retrofitted any other existing tests to use the suite system,
but it's almost certainly going to make them simpler and more robust
too.

The CLI help generation is now *all* in markdown, including flags.
I cargo-culted a lot of the stringer there, and added a few very
minor opinionated tweaks of opportunity.  It's probably still all
nonfinal; and in particular I'm still utterly giving up on trying to
get the whitespace I want out of golang templates.

There's a few tweaks to the experimental goldmark code, because I
found... either an interesting edge case, or an outright bug.
Some of our text with parenthesis causes goldmark to produce paragraph
objects that point to themselves as siblings... in a loop.  Oof.
I don't know if that's intended behavior or not, but I doubt it,
because it sure surprised me.  Anyway, for now I work around it.
Our yak-shave depth is already entirely too high right now.

So what _becomes_ of the generated docs hunks?  Well, over in the
site repo, the static site rendering pipeline actually hoists those
hunks back out, and processes them as markdown again.
Isn't that neat?  (There's a "clidocs" tag on the code blocks
which engages that... though you can't see that in this diff; it's
entirely over in the site repo.)

Probably the most "oof" thing in this diff is... I had to disable
the automatic file-level parallelization in the testmark suite system,
because of the dang package scope shenanigans with the CLI lib.
The amount of pain that's producing is already staggeringly high.

---
## [warptools/warpforge](https://github.com/warptools/warpforge)@[3daf6d9fd0...](https://github.com/warptools/warpforge/commit/3daf6d9fd0bbeedac88e783183b1b9fd6066f77b)
#### Thursday 2023-08-24 20:05:38 by Eric Myhre

Research checkpoint: attempting to use lipgloss and goldmark.

... and I think, after playing with it for a good number of hours,
this ain't it either.

lipgloss is coming in at a really weird middle level of abstraction.
The features like margins and wrapping aren't really doing the right
things without an incredible amount of cajoling (and even then).
It seems to have kind of _half_ a component model, and doesn't seem
to compose very gracefully -- it looks like I'll just *keep* passing
width info down on the side, while I use it, which is confusing.
I'm not sure if I'm holding it wrong or if it just doesn't have the
same view as me on what's important.

And it seems to have the helpful opinion that it's gonna emit
CSI reset codes constantly... which absolutely does not compose
with how goldmark AST visitors (or any sane AST visit system) is
going to want to get things done.

Less importantly, but perturbing to me, is that lipgloss is also doing
just a staggering amount of map lookups and memory allocations for
every little thing.

All in all, I think I'm going to have to dive another level deeper,
because this just isn't doing the thing.

(I'm halfway tempted to pull up and go back to using glamour, because
that got an interesting MVP radically faster, but... it just plateaus
so dang hard.  I can't do variable indent; the tables were meh; the
options for doing anything transformative with links was ziltch...
No, I don't think I really wanna rest there either.)

I'm thinking just a few key functions for wrapping text with awareness
of ANSI codes and their (lack of) effect on render size will maybe
be entirely sufficient and do a simpler better job.
A much simpler library (or even just set of short functions; ANSI codes
are distinctly Not That Complicated) for the highlighting will also
totally suffice.  So: that'll be the approach to try up next.

---
## [warptools/warpforge](https://github.com/warptools/warpforge)@[a42537d29d...](https://github.com/warptools/warpforge/commit/a42537d29d3427fda51c037719571b0f00672a58)
#### Thursday 2023-08-24 20:05:38 by Eric Myhre

Research checkpoint commit: markdown processing.

This has... mixed success.

I've got three different irons in the fire here:
 1. The plain markdown text coming out (to sanity check my templates)
 2. A library called Glamour used to process it
 3. A brief prototype of going straight to Goldmark and using
  that system's renderers directly on the AST.

I've posted a bunch of notes on this in the dev chat on Matrix already,
as well as some screenshots, so I'll keep this commit note briefer.

In short, controlling the line spacing and indentation is turning out
remarkably hard with option 2.  In fact, I think it's outright
impossible without some invasive changes tantamount to forking.
So that's a bummer.  It got good rapid results and was very exciting!
But "indent the contents under an h4 deeper than under an h2" is just
not a feature I can get there.  And there are a few other weird cliffs
to customizability (links can only be handled one way, except for a
special case around fragment-only links?  tables or other attempts to
pack info densely are limited.  etc) that are unfortunate.

Getting isomorphic html output, if I wanted to include spacing and all,
and have it rendered in html identically to how it would be in plain
ANSI terminal text, is also looking pretty hard with Option 2.
I think we'd end up literally storing the ANSI and all in testmark
codeblocks, and then writing code in the site generator to re-render
that into html.  Possible, and well within the range of things I was
considering doing anyway at the begining of this exploration, but...
also maybe not totally ideal, considering how much control we _could_
have of this, by going with Option 3.

Now, Option 3... well, the big question there is simply "how much work
is that going to be?", and the answer is "I don't know".

But the prototype of using goldmark directly with my own renderer went
off pretty much without a hitch, and it seems like it reaches a very
maximal level of control.  And for reference, the size of goldmark's
own html renderer is about 1000 lines of (very understandable) code.
That's... about a 990 lines more than I'd _like_ to own, but on the
other hand, if it's self contained and doesn't need much tweaking
after the first pass, maybe it's acceptable.

In exchange for that code, we'd get utterly total control of rendering,
so we could fearlessly use all sorts of stuff (say, even codeblocks
within text within headings that describe flags, and get all of it
aligned correctly)... and it would become also totally in reach to
write branches for emitting html color annotations vs ANSI, with full
correctness as the action of both would be driven by the same AST walk.

Jury's still out a bit.  This checkpoint is just that: a checkpoint.
Some of this code will disappear again, for certain.  Which, exactly,
is not yet certain.

---
## [TheDarkElites/Foundation-19](https://github.com/TheDarkElites/Foundation-19)@[b4642dc835...](https://github.com/TheDarkElites/Foundation-19/commit/b4642dc835dc801d801fd543cfd34bd44ca23929)
#### Thursday 2023-08-24 20:15:10 by cheesePizza2

Armor improvements (#1251)

* the fixes

* FUCK YOU

* few more improvements

* bring em back

* fuck you

---
## [mothbeanie/VVVVVV](https://github.com/mothbeanie/VVVVVV)@[86d90a1296...](https://github.com/mothbeanie/VVVVVV/commit/86d90a1296739adef30b224f41e3a6ab55069a48)
#### Thursday 2023-08-24 20:23:07 by Misa

Add color support to Windows console output, properly

This adds color support to the output of the console on Windows. Now if
you're using Windows 10 build 1511 or later (I think it's build 1511
anyway; they added more VT sequence support in later versions), you will
see colors by default. This isn't due to Windows helping in any way;
this commit has to specifically enable it with SetConsoleMode() because
by default, Windows won't enable color support unless we enable it. (Or
if it's enabled in the registry, but having to go through the registry
to enable basic shit like that is completely fucking stupid.)

I tested this in my Windows 10 virtual machine and it's completely
working.

---
## [Rohail33/Realking_kernel_sm8250](https://github.com/Rohail33/Realking_kernel_sm8250)@[fda855f2fd...](https://github.com/Rohail33/Realking_kernel_sm8250/commit/fda855f2fd6ba584e867c04f1ef26ad5eec9bc08)
#### Thursday 2023-08-24 21:07:27 by Tashfin Shakeer Rhythm

Revert "thermal_core: Do not unload thermal core driver as a module"

thermal_unregister_governors() is not marked with __init annotation anymore
and my sorry ass didn't remember during rebase. Revert this broken patch.

This reverts commit e3036b0a6a61076444cf6b4e8dd83e52e581c939.

Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>
Signed-off-by: NotZeetaa <rodrigo2005contente@gmail.com>

---
## [W4rd3nn/Skyrat-tg](https://github.com/W4rd3nn/Skyrat-tg)@[a1609c4536...](https://github.com/W4rd3nn/Skyrat-tg/commit/a1609c4536fe05f95560bd1a1be4607b944ee5a5)
#### Thursday 2023-08-24 22:25:06 by SkyratBot

[MIRROR] [NO GBP] Fixes clown car + deer collision  [MDB IGNORE] (#22709)

* [NO GBP] Fixes clown car + deer collision  (#77076)

## About The Pull Request

A not-so-long time ago I drunkenly coded #71488 which did not work as
intended.

I return now, in a state of reflective sobriety, to rectify that.

The clown car will now not only crash like it should, but will also
cause (additional) head injuries to some occupants and kill the deer on
impact.

Content warnings: **Animal death, vehicle collision, blood, DUI.**

https://github.com/tgstation/tgstation/assets/28870487/4889f452-7e49-4512-8cdd-e4e2a4d6b394
## Why It's Good For The Game

Fixes the product of a silly PR that never actually worked. Also gives
it a bit more TLC in the event that this joke actually plays out on a
live server.
## Changelog
:cl:
fix: Clown cars now properly collide with deer.
sound: Violent, slightly glassy car impact sound.
/:cl:

* [NO GBP] Fixes clown car + deer collision

---------

Co-authored-by: Rhials <28870487+Rhials@users.noreply.github.com>

---
## [GamingasCZ/gdlists](https://github.com/GamingasCZ/gdlists)@[c56e754320...](https://github.com/GamingasCZ/gdlists/commit/c56e75432072b7458e5abe0d8497155a5425c878)
#### Thursday 2023-08-24 23:15:55 by GamingasCZ

 uhh... tiny updates lmao

- finished social media picker (almost)
- added member clipboard
- added recently used roles
- added more role presets
- added funny collab editor title names :D
- visual fixes
- many bugfixes
- code cleanup
- reduced animations (if prefers reduced motion)
- updated footer profile pfp (epiiiiiccccc)
- second time lmao (damn you, vsc)

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[35cb1556ad...](https://github.com/lessthnthree/tgstation/commit/35cb1556ad4bad7703b75c0edc472ed41a5fb34f)
#### Thursday 2023-08-24 23:33:30 by carlarctg

When Space Dragons devour people they get .extinguish()ed (#77248)

## About The Pull Request

When Space Dragons devour people they get extinguished, removing flames.
## Why It's Good For The Game

> When Space Dragons devour people they get extinguished, removing
flames.

I find it quite annoying that even after you die to a space dragon, the
jackass melts not just your jumpsuit, your suit, your hat, your mask, he
also melts your entire skin off, leaving your body husked with 400
million burn damage when and if the dragon finally dies. I don't think
there's any real reason for this to be necessary, it doesn't help the
dragon in any way - It's just kind of a middle finger to the dead guy,
or more accurately, an oversight.

Worse, because the flame sprite is stupidly noisy, when a dragon DOES
die the corpses are all thrown around randomly and they all look the
exact same, which makes it easier to ignore them.

If there's a concern about tracking sensors, I can make it disable them,
but honestly if you can do that with demons I don't see why this would
be a problem. Not even accounting for the fact that many jumpsuits
ingame are fireproof.
## Changelog
:cl:
qol: When Space Dragons devour people they get extinguished, removing
flames.
/:cl:

---
## [lizardqueenlexi/orbstation](https://github.com/lizardqueenlexi/orbstation)@[a2ee4ec813...](https://github.com/lizardqueenlexi/orbstation/commit/a2ee4ec813c38741d593e5e1731764458c77b811)
#### Thursday 2023-08-24 23:51:09 by Jacquerel

Polymorphic Inverter tweaks (#77675)

## About The Pull Request

Fixes #77649

You can no longer use the belt to turn into any kind of carbon mob,
sorry gamers it was a cool dream but it leads to too many problems.
Also I made space dragon "there's an alive guy in my stomach" code now
work on signals instead of on Life tick which is slightly more efficient
and also resolves an issue with the funny belt.

## Why It's Good For The Game

Too much room for weird edge cases as a result of doing this (messing
with monkey DNA, producing infinite xeno organs, blocking legit xeno
queens from being created) which had no graceful solution.
Moving stuff off Life if it can be event based is nice.

## Changelog

:cl:
fix: Turning into a space dragon with the polymorphic inverter will no
longer leave you existing in two places
balance: You can no longer use the belt to transform into monkeys or
xenomorphs, for technical reasons.
/:cl:

---

