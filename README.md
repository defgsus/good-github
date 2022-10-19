## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-10-18](docs/good-messages/2022/2022-10-18.md)


2,329,198 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,329,198 were push events containing 3,497,271 commit messages that amount to 278,735,918 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 27 messages:


## [postgresql-cfbot/postgresql](https://github.com/postgresql-cfbot/postgresql)@[8272749e8c...](https://github.com/postgresql-cfbot/postgresql/commit/8272749e8ca1dbbcb5f8cf5632ec26a573ac3111)
#### Tuesday 2022-10-18 00:00:06 by Tom Lane

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
## [dhanesh-kapadiya/cadence](https://github.com/dhanesh-kapadiya/cadence)@[add4b390ad...](https://github.com/dhanesh-kapadiya/cadence/commit/add4b390ada43fdd8167f06e209ae6ece0d11aaa)
#### Tuesday 2022-10-18 00:40:27 by Steven L

Standardizing cancellation behavior: a canceled workflow never starts a new run (#4898)

# Summary for busy people

Workflow cancellation was kinda weird and confusing, and left some awful, unrecoverable, and un-*preventable* edge cases (particularly with child workflows).  It also left users with no way to reliably stop work, aside from termination.  Termination is inherently "unclean" and risky, so it should not be required to achieve something outside exceptional circumstances where recovery is not possible.

This commit changes that: cancellation is now "sticky", and a canceled workflow does not ever trigger a new run after it completes, regardless of how it completes, so it can be used as a reliable "stop processing after cleanup" tool.  The final state of a canceled workflow's run is now *always* a successful completion with a value, canceled, or timed out. (termination remains always "terminated")  
A canceled workflow can still start and abandon child workflows, so all current behavior with retries / continue as new / etc can be replicated with child workflows if desired.

A fair bit of (not very complex) additional work here and in nearly all other repos is required to truly complete this, but it is *functional* and non-optional with this commit alone.  
In particular, adding a dynamic config to (temporarily!) restore old behavior should be fairly easy if it proves to be needed.

# More details and motivation

Part 1 of [many, tbd, in multiple repos] involved in changing workflow cancellation to reliably end workflows.
Tests will be coming soon, for now I'm using a fairly simple set of workflows and checking the resulting histories exhaustively by hand.

The primary motivation for these changes is to address some impossible-to-recover-from scenarios when canceling child workflows.  After further exploration and discussion we've realized that, without these changes, there is *no reliable way* to stop a sequence of workflows without relying on termination, which we consistently treat as a fallback / impure-but-necessary ultimate hammer.

Workflows should not *need* to rely on termination to achieve a desired behavior.  With these changes, cancellation becomes capable of *guaranteeing* that workflows end within some finite time, which is a unique ability and makes it much more consistent and reliable.  
Turning this into a "complete" change will require quite a few tests, documentation changes, client-side changes (to allow recording more info, and likely changing test suites), and some smallish database and maybe RPC changes (to hold/return more data in cancellation errors).

We are also not currently planning on making this configurable.  It's seen as a correction of an under-specified and somewhat flawed chunk of behavior, more than "a change".  
Existing workflows will not experience replay errors, but it is still a substantial *semantic* change, though from what we have seen cancellation is relatively rarely used (partly due to its complex behavior).  If issues are encountered / if users end up needing it, it should be fairly easy to add a per-domain/tasklist/workflow type configuration value, but it will be opt-*out*, not opt-*in*.

# What was happening

Previously, workflow behavior on cancellation was pretty frequently surprising to our users, arguably inconsistent, and not very well documented:

| **PREVIOUS**  | **simple**               | **retry**                                 | **cron**                                | **retry+cron**                                    |
|--------------:|--------------------------|-------------------------------------------|-----------------------------------------|---------------------------------------------------|
| **success**   | success                  | success                                   | success<br>continue cron<br>cron        | success<br>continue cron<br>cron<br>retry         |
| **cancel**    | canceled                 | canceled                                  | canceled                                | canceled                                          |
| **retryable** | (n/a, fatal)             | continue retry<br>retry<br>recorded error | (n/a, fatal)                            | continue retry<br>cron<br>retry<br>recorded error |
| **fatal**     | failed<br>recorded error | failed<br>recorded error                  | continue cron<br>cron<br>recorded error | continue cron<br>cron<br>retry<br>recorded error  |
| **continue**  | continue immediately     | continue immediately<br>retry             | continue immediately                    | continue immediately<br>retry                     |
| **timeout**   | timeout                  | continue retry<br>retry<br>recorded error | continue cron<br>cron<br>recorded error | continue retry<br>cron<br>retry<br>recorded error |

A legend is:
- success / etc shows the final state of the canceled run (success = completed with a value that can be retrieved)
- "continue X" covers what source is used to compute the next run's starting delay (cron, retry, or no delay)
- "cron" / "retry" shows whether or not cron/retry configuration is carried over to the new run
  - note that cron is lost by default with continue-as-new
- and "recorded error" is whether or not the returned error is saved in its entirety (type + reason + details)

This largely summarizes as "cancellation works when you end with the canceled-context error", say from `ctx.Err()`, otherwise it behaves like normal (or nearly) and many scenarios will start a new run.
That's somewhat reasonable, but it's fairly "fragile" (it depends on what you return, and there are *many* ways for code to return some other error), and most importantly it means *there is no reliable way to stop a workflow* except to terminate it.

That has severe consequences in at least two scenarios:
1. When termination is *unsafe*
2. When a parent workflow cancels a child by canceling its context

For 1, for manual cancellations it's potentially reasonable to just terminate a run that begins after a successful cancel... but in principle if you're using cancellation it implies that termination is *not* desired, and potentially not safe to do.  Canceling may result in a brand new run that immediately starts new behavior, leaving you with no safe window to terminate and not leave bad state lingering.  
So users wanting a safe way to stop a sequence of workflows have no reliable way to do so.

For 2, it puts parent+child workflows in an extremely awkward, and essentially unrecoverable scenario.  Cancellation is a *one time event*, and as far as the parent is concerned, if the child/its context is canceled, the child is canceled...  
...but if the child then starts a new run for *any* reason (retry, cron, reset, etc), that new run is no longer canceled.  The parent has no way to know this has happened, and has no way to *re*-cancel the new child, so it can easily lead to the collection of workflows getting into an impossible state that it never recovers from.

Both cases are able to lead to unreliable behavior which can only use termination to stop, and for which no "safe" option exists.

After reviewing some customer issues and desires and thinking about things, we've settled on "cancel should guarantee that things stop".  Not necessarily in a timely manner, but that's fine.  And if a workflow wants to run behavior longer or larger than its current run can achieve, it has a workaround: start a new (likely child) workflow to do the cleanup.

# What happens now

So that's what this PR does, in a minimal / to-be-polished way so we can start running it for our stuck users while we flesh out tests and change other behaviors.

Currently that means our cancellation behavior is now:

| **CURRENT**    | **simple**                                | **retry**                                 | **cron**                                  | **retry+cron**                            |
|--------------:|-------------------------------------------|-------------------------------------------|-------------------------------------------|-------------------------------------------|
| **success**   | success                                   | success                                   | success                                   | success                                   |
| **cancel**    | canceled                                  | canceled                                  | canceled                                  | canceled                                  |
| **retryable** | (n/a, fatal)                              | canceled<br>recorded error (details only) | (n/a, fatal)                              | canceled<br>recorded error (details only) |
| **fatal**     | canceled<br>recorded error (details only) | canceled<br>recorded error (details only) | canceled<br>recorded error (details only) | canceled<br>recorded error (details only) |
| **continue**  | canceled<br>(no details)                  | canceled<br>(no details)                  | canceled<br>(no details)                  | canceled<br>(no details)                  |
| **timeout**   | timeout                                   | timeout                                   | timeout                                   | timeout                                   |

And the new "details" entries cover whether or not an error's "details" (the custom encoded data, not reason or type) are saved.  Unfortunately the current cancellation event (and clients' API) does not allow recording all data, or any in some cases, so the original reason/message and error type are lost and are replaced with a canceled error.

Now, cancellation *always* ends workflows with the current run.  Returning a value will return that value, including in cron scenarios, timeouts are still timeouts (and they imply a possibly un-clean termination), and _all_ errors or attempts to continue-as-new will instead result in a canceled state.

# Future changes to make to finish this effort

With further changes to the clients and RPC/storage models, canceled errors will store more details about what was returned.  E.g. continue-as-new does not record what was *attempted* to be started, and other error types lose their "reason" (i.e. the message) and type but not details.  Pretty clearly this is sub-par, and we should be capable of reporting the actual return in full so it can be retrieved if needed.  This is also why returning a value now always ends in a completed state, so successful completions do not lose those values.

Prior to merging into master / a release, we may end up making this configurable (likely with a default of opt-out), to address both the sub-par information recording and the semantically-breaking behavior change.  Docs changes are also due, as well as some integration tests, client library changes (e.g. to make sure the test suite reflects the new behavior), etc.

Another gap to plug is that resetting a workflow does not "forward" the canceled state to the new run.  We should probably be treating cancellation like we do signals: cancel the new run if the current run is canceled.  This will ensure that you can reset a child and retain the parent's cancellation, so it'll very likely become the default behavior, but we'll allow overriding it.  Resets are manual actions, they can break the rules if desired.  And they can just manually cancel later if they decide they do want it.

And last and perhaps least: it's quite strange that continue-as-new does not retain cron config.  At least from the Go client.  I suspect it's just not adding to / pulling from the context correctly.

---
## [hexagon-geo-surv/linux-stable-rt](https://github.com/hexagon-geo-surv/linux-stable-rt)@[7112098b69...](https://github.com/hexagon-geo-surv/linux-stable-rt/commit/7112098b69d5922b7d34c1f6088dad4b0507214e)
#### Tuesday 2022-10-18 00:42:50 by Jason A. Donenfeld

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
## [drakomatic/drakomatic.github.io](https://github.com/drakomatic/drakomatic.github.io)@[8a3cf4b3db...](https://github.com/drakomatic/drakomatic.github.io/commit/8a3cf4b3db8ed7cd69e33373439d44be39ad805d)
#### Tuesday 2022-10-18 01:31:17 by drakomatic

added icon for the website

the thing is there now at the top bar
fuck you IE <= 10 users

---
## [dlee2008/mpv](https://github.com/dlee2008/mpv)@[6f7506b660...](https://github.com/dlee2008/mpv/commit/6f7506b660b83a44535eceb12a8b9c4de6c0eb36)
#### Tuesday 2022-10-18 03:15:35 by Philip Langdale

f_hwtransfer: get rid of the shit list

A few years ago, wm4 got sufficiently annoyed with how vaapi image
format support was being discovered that he flipped the table and
introduced the shit list (which just included vaapi) to hard-code the
set of supported formats.

While that might have been necessary at the time, I haven't been able
to find a situation where the true list of supported formats was unsafe
to use. We filter down the list based on what the vo reports - and the
vo is already doing a thorough testing of formats, and if a format
makes it through that gauntlet, it does actually work.

Interestingly, as far as I can tell, the hwdec_vaapi probing code was
already good enough at the time (also written by wm4), so perhaps the
key difference here is that the driver side of things has improved.

I dug into this because of the support for the 422/444 high bit depth
vaapi formats I added to ffmpeg. These are obviously not in the hard
coded list today, but they work fine.

Finally, although it's positioned as a vaapi thing, it's really just
Intel specific, as the AMD vaapi driver has never exposed support for
anything except the formats used by the decoder/encoder profiles.

---
## [dragid10/dnd-bot](https://github.com/dragid10/dnd-bot)@[2958246fbb...](https://github.com/dragid10/dnd-bot/commit/2958246fbb4f354ca4ec35e9a487a38fde75f063)
#### Tuesday 2022-10-18 04:31:52 by Alex Oladele

Don't mention `@everyone`  when polling for availability (#17)

<!--- Provide a general summary of your changes in the Title above -->

## Description
- Remove `@everyone` tag and instead get everyone who hasn't rsvp'd 
- If everyone hasn't rsvp'd then we just do `@here`
- Get rid of dreamers functionality

## Motivation and Context
Everyone kept telling me that doing `@everyone` was annoying and
disruptive. So I listened to the homies and made the relevant change

## How Has This Been Tested?
- Tested locally

## Screenshots (if appropriate):
![Screenshot from 2022-10-17
23-21-22](https://user-images.githubusercontent.com/4042877/196328090-24a25675-c3d3-4490-93d7-daa209188496.png)

## Types of changes
<!--- What types of changes does your code introduce? Put an `x` in all
the boxes that apply: -->
- [ ] Bug fix (non-breaking change which fixes an issue)
- [x] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing
functionality to change)

## Checklist:
<!--- Go over all the following points, and put an `x` in all the boxes
that apply. -->
<!--- If you're unsure about any of these, don't hesitate to ask. We're
here to help! -->
- [x] My code follows the code style of this project.
- [ ] My change requires a change to the documentation.
- [ ] I have updated the documentation accordingly.

---
## [Mantas22XYT/NewHorizonMC](https://github.com/Mantas22XYT/NewHorizonMC)@[25f096561b...](https://github.com/Mantas22XYT/NewHorizonMC/commit/25f096561b891b0e180065d565d2ebde776ee43e)
#### Tuesday 2022-10-18 07:26:43 by Mantas22XYT

read code of conduct

fuck you lexington

Signed-off-by: Mantas22XYT <75636222+Mantas22XYT@users.noreply.github.com>

---
## [rohankumardubey/spark](https://github.com/rohankumardubey/spark)@[c4c623a3a8...](https://github.com/rohankumardubey/spark/commit/c4c623a3a890267b2f9f8d472c8be30fc5db53e1)
#### Tuesday 2022-10-18 08:45:05 by Hyukjin Kwon

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
## [xuv8r/orbstation](https://github.com/xuv8r/orbstation)@[23bfdec8f4...](https://github.com/xuv8r/orbstation/commit/23bfdec8f43046f7b54906509e38ed1ad91f5096)
#### Tuesday 2022-10-18 08:52:54 by LemonInTheDark

Multiz Rework: Human Suffering Edition (Contains PLANE CUBE) (#69115)


About The Pull Request

I've reworked multiz. This was done because our current implementation of multiz flattens planes down into just the openspace plane. This breaks any effects we attach to plane masters (including lighting), but it also totally kills the SIDE_MAP map format, which we NEED for wallening (A major 3/4ths resprite of all wall and wall adjacent things, making them more then one tile high. Without sidemap we would be unable to display things both in from of and behind objects on map. Stupid.)

This required MASSIVE changes. Both to all uses of the plane var for reasons I'll discuss later, and to a ton of different systems that interact with rendering.

I'll do my best to keep this compact, but there's only so much I can do. Sorry brother.
Core idea

OK: first thing.
vis_contents as it works now squishes the planes of everything inside it down into the plane of the vis_loc.
This is bad. But how to do better?

It's trivially easy to make copies of our existing plane masters but offset, and relay them to the bottom of the plane above. Not a problem. The issue is how to get the actual atoms on the map to "land" on them properly.

We could use FLOAT_PLANE to offset planes based off how they're being seen, in theory this would allow us to create lens for how objects are viewed.
But that's not a stable thing to do, because properly "landing" a plane on a desired plane master would require taking into account every bit of how it's being seen, would inherently break this effect.

Ok so we need to manually edit planes based off "z layer" (IE: what layer of a z stack are you on).

That's the key conceit of this pr. Implementing the plane cube, and ensuring planes are always offset properly.
Everything else is just gravy.
About the Plane Cube

Each plane master (except ones that opt out) is copied down by some constant value equal to the max absolute change between the first and the last plane.
We do this based off the max z stack size detected by SSmapping. This is also where updates come from, and where all our updating logic will live.

As mentioned, plane masters can choose to opt out of being mirrored down. In this case, anything that interacts with them assuming that they'll be offset will instead just get back the valid plane value. This works for render targets too, since I had to work them into the system as well.

Plane masters can also be temporarily hidden from the client's screen. This is done as an attempt at optimization, and applies to anything used in niche cases, or planes only used if there's a z layer below you.
About Plane Master Groups

BYOND supports having different "maps" on screen at once (IE: groups of items/turfs/etc)
Plane masters cannot cover 2 maps at once, since their location is determined by their screen_loc.
So we need to maintain a mirror of each plane for every map we have open.

This was quite messy, so I've refactored it (and maps too) to be a bit more modular.

Rather then storing a list of plane masters, we store a list of plane master group datums.
Each datum is in charge of the plane masters for its particular map, both creating them, and managing them.

Like I mentioned, I also refactored map views. Adding a new mapview is now as simple as newing a /atom/movable/screen/map_view, calling generate_view with the appropriate map id, setting things you want to display in its vis_contents, and then calling display_to on it, passing in the mob to show ourselves to.

Much better then the hardcoded pattern we used to use. So much duplicated code man.

Oh and plane master controllers, that system we have that allows for applying filters to sets of plane masters? I've made it use lookups on plane master groups now, rather then hanging references to all impacted planes. This makes logic easier, and prevents the need to manage references and update the controllers.

image

In addition, I've added a debug ui for plane masters.
It allows you to view all of your own plane masters and short descriptions of what they do, alongside tools for editing them and their relays.

It ALSO supports editing someone elses plane masters, AND it supports (in a very fragile and incomplete manner) viewing literally through someone else's eyes, including their plane masters. This is very useful, because it means you can debug "hey my X is yorked" issues yourself, on live.

In order to accomplish this I have needed to add setters for an ungodly amount of visual impacting vars. Sight flags, eye, see_invis, see_in_dark, etc.

It also comes with an info dump about the ui, and plane masters/relays in general.

Sort of on that note. I've documented everything I know that's niche/useful about our visual effects and rendering system. My hope is this will serve to bring people up to speed on what can be done more quickly, alongside making my sin here less horrible.
See https://github.com/LemonInTheDark/tgstation/blob/multiz-hell/.github/guides/VISUALS.md.
"Landing" planes

Ok so I've explained the backend, but how do we actually land planes properly?
Most of the time this is really simple. When a plane var is set, we need to provide some spokesperson for the appearance's z level. We can use this to derive their z layer, and thus what offset to use.

This is just a lot of gruntwork, but it's occasionally more complex.
Sometimes we need to cache a list of z layer -> effect, and then use that.
Also a LOT of updating on z move. So much z move shit.

Oh. and in order to make byond darkness work properly, I needed to add SEE_BLACKNESS to all sight flags.
This draws darkness to plane 0, which means I'm able to relay it around and draw it on different z layers as is possible. fun darkness ripple effects incoming someday

I also need to update mob overlays on move.
I do this by realiizing their appearances, mutating their plane, and then readding the overlay in the correct order.

The cost of this is currently 3N. I'm convinced this could be improved, but I've not got to it yet.
It can also occasionally cause overlays to corrupt. This is fixed by laying a protective ward of overlays.Copy in the sand, but that spell makes the compiler confused, so I'll have to bully lummy about fixing it at some point.
Behavior changes

We've had to give up on the already broken gateway "see through" effect. Won't work without managing gateway plane masters or something stupid. Not worth it.
So instead we display the other side as a ui element. It's worse, but not that bad.

Because vis_contents no longer flattens planes (most of the time), some uses of it now have interesting behavior.
The main thing that comes to mind is alert popups that display mobs. They can impact the lighting plane.
I don't really care, but it should be fixable, I think, given elbow grease.

Ah and I've cleaned up layers and plane defines to make them a bit easier to read/reason about, at least I think.
Why It's Good For The Game
<visual candy>

Fixes #65800
Fixes #68461
Changelog

cl
refactor: Refactored... well a lot really. Map views, anything to do with planes, multiz, a shit ton of rendering stuff. Basically if you see anything off visually report it
admin: VV a mob, and hit View/Edit Planes in the dropdown to steal their view, and modify it as you like. You can do the same to yourself using the Edit/Debug Planes verb
/cl

---
## [xuv8r/orbstation](https://github.com/xuv8r/orbstation)@[1810b85553...](https://github.com/xuv8r/orbstation/commit/1810b855536f05891593b1379e455164f45fab3a)
#### Tuesday 2022-10-18 08:52:54 by tralezab

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
## [RikuTheKiller/tgstation](https://github.com/RikuTheKiller/tgstation)@[fc7c186957...](https://github.com/RikuTheKiller/tgstation/commit/fc7c186957088b6ffd0605f814bea754670c0212)
#### Tuesday 2022-10-18 13:05:20 by RikuTheKiller

Brains can now be healed with mannitol without being fully decayed among other quality of life tweaks (#70357)

Removed the minimum amount of mannitol required to pour it since limiting this made barely any sense in the first place. Why oh why must we coders implement useless restrictions? (Useless restrictions caused the decay bug anyways.)

Brains no longer care about whether or not they're fully decayed when checking if they can be healed by pouring mannitol on them. They instead check if they're damaged at all and if they are, they'll let you pour mannitol on them.

The amount of time it takes to pour mannitol onto a brain is now 3 seconds instead of 6 seconds as it was way too slow. (Especially since something like a surgery step takes less time than 6 seconds.)

The solution is now only partially consumed as well, meaning if you need 20u of mannitol to fix a brain and you have a mixture of 40u of mannitol and 40u of mercury for example, pouring it will consume 40u of the mixture since you can't magically separate out the mannitol. This is rounded up, by the way. (Before this it simply consumed all of the mannitol, somehow you apparently can't stop pouring even while slowly pouring, according to the text.)

I've also very slightly increased the consistency of the pouring messages.

Fixes #70355

---
## [prokrishpatel/Data-Structures-and-Algorithum-using-CPP](https://github.com/prokrishpatel/Data-Structures-and-Algorithum-using-CPP)@[b0453d2c27...](https://github.com/prokrishpatel/Data-Structures-and-Algorithum-using-CPP/commit/b0453d2c27694b8d1fca111c52fb4943ca4e2c8f)
#### Tuesday 2022-10-18 14:12:54 by Krish Patel

Create 23 Stack String Palindrome.cpp

Krishna has shown one magic to reverse the given string. He asked his friend that can you write a code to check the given string is palindrome or not.

Sample 1: Line 1: Enter the string : amma Line 2: Palindrome

Sample 1: Line 1 : Enter the expression : papa Line 2 : Not Palindrome

---
## [mediocr3/qatacombs](https://github.com/mediocr3/qatacombs)@[b409a71dc7...](https://github.com/mediocr3/qatacombs/commit/b409a71dc707c0000cb67ffd3601f270dfb8b783)
#### Tuesday 2022-10-18 16:04:48 by mediocr3

Added food, eating, player portrait.

finally getting back into development. so the player character already had the ticking hunger timer, but now they can finally sustain themselves with floor meat (mmmmm). the actual starvation mechanic is currently broken now, so nothing happens yet when the hunger timer reaches zero. the hunger timer will largely be an invisible mechanic (ie. no bars or numbers seen by the player) but once audio is added i do plan on adding audio queues for hunger (ideally once audio is fully implemented there will be enough sounds to do literal blind playthroughs of the game). And speaking of future mechanics, i noticed during playtesting that looking for food on each level is a major pain in the ass and more of a chore than something that adds real tension. so im going to do either:
a) have food spawn on set intervals of levels
b) have a "smelling" system where your character generates "particles" in the direction of the food.
these arent mutually exclusive. both are probably good ideas. ill think it over.

oh yeah also i added a few more q's where there should be and some more middle english grammar, in line with the character's weird dialect. oh yeah, the rules for the q's are that they are there at the starts and ends of words, but there can be c's and k's in the middle (but ck's at the ends of words become qq's, like in "stiqq"). debating whether or not i should do "qey" or "key" because it might get a bit confusing.

---
## [justinpryzby/postgres](https://github.com/justinpryzby/postgres)@[6856e7ea04...](https://github.com/justinpryzby/postgres/commit/6856e7ea0403dd3f96573d2d01b1c44b50be0c4c)
#### Tuesday 2022-10-18 16:10:37 by Tomas Vondra

PATCH: AM-specific statistics, with an example implementation for BRIN (WIP)

Hi,

A couple days ago I posted a WIP patch [1] implementing "BRIN Sort",
i.e. a node producing sorted output for BRIN minmax indexes. One of the
challenges I mentioned in that thread is costing - that's actually not
specific to that patch, it's an issue affecting BRIN in general, not
just the proposed node, due to block-range indexes being very different
from regular indexes with explicit tuple pointers.

I mentioned I have some ideas how to improve this, and that I'll start a
separate thread to discuss this. So here we go ...

The traditional estimation problem is roughly this:

    Given a condition, how many rows will match it?

That is, given a table with X rows, we need to estimate how many rows
will match a WHERE condition, for example. And once we have the row
estimate, we can estimate the amount of I/O, cost for sorting, etc.

We have built fairly solid capability to calculate these estimates,
using per-column statistics, extended statistics, ... The calculated
estimates are not always perfect, but in general it works well.

This affects all path types etc. mostly equally - yes, some paths are
more sensitive to poor estimates (e.g. runtime may grow exponentially
with increasing rowcount).

BRIN indexes however add another layers to this - once we have estimated
the number of rows, we need to estimate the number of pages ranges this
maps to. You may estimate the WHERE condition to match 1000 rows, but
then you need to decide if that's 1 page range, 1000 page ranges or
possibly even all page ranges for the table.

It all depends on how "correlated" the data is with physical position in
the table. If you have perfectly correlated data, it may be enough to
scan a single page. If it's random, you may need to scan everything.

The existing costing uses the column correlation statistics, but sadly
that's rather insensitive to outlier values. If you have a sequential
table, and then set 1% of data to min/max (making the ranges very wide),
the correlation will remain very close to 1.0, but you'll have to scan
all the ranges (and the costing won't reflect that).

The "BRIN sort" patch needs to estimate a different thing - given a page
range, how many other page ranges overlap with it? This is roughly the
amount of stuff we'll need to scan and sort in order to produce the
first row.

These are all things we can't currently estimate - we have some rough
heuristics, but it's pretty easy to confuse those.

Therefore, I propose to calculate a couple new statistics for BRIN
indexes (assume minmax indexes, unless mentioned otherwise):

1) average number of overlapping ranges
---------------------------------------

Given a range, with how many ranges it overlaps? In a perfectly
sequential table this will be 0, so if you have a value you know it'll
match just one range. In random table, it'll be pretty close to the
number of page ranges.

This can be calculated by simply walking the ranges, sorted by minval
(see brin_minmax_count_overlaps).

2) average number of matching ranges for a value
------------------------------------------------

Given a value, how many ranges it matches? This can be calculated by
matching sampled rows to ranges (brin_minmax_match_tuples_to_ranges).

For minmax indexes this is somewhat complementary to the average number
of overlaps, the relationship is roughly this:

  avg(# of matching ranges) = 1 + avg(number of overlapping ranges)/2

The intuition is that if you assume a range randomly overlapped by other
ranges, you're likely to hit about 1/2 of them.

The reason why we want to calculate both (1) and (2) is that for other
opclasses the relationship is not that simple. For bloom opclasses we
probably can't calculate overlaps at all (or at least not that easily),
so the average number of matches is all we have. For minmax-multi, the
overlaps will probably use only the min/max values, ignoring the "gaps",
but the matches should use the gaps.

3) a bunch of other simple statistics
-------------------------------------

These are number of summarized / not-summarized ranges, all_nulls and
has_nulls ranges, which is useful to estimate IS NULL conditions etc.

The attached patch implements a PoC of this. There's a new GUC
(enable_indexam_stats) that can be used to enable/disable this (both the
ANALYZE and costing part). By default it's "off" so make sure to do

  SET enable_indexam_stats = true;

The statistics is stored in pg_statistics catalog, in a new staindexam
column (with bytea). The opclasses can implement a new support
procedure, similarly to what we do of opclass options. There's a couple
of wrinkles (should be explained in XXX comments), but in principle this
works.

The brin_minmax_stats procedure implements this for minmax opclasses,
calculating the stuff mentioned above. I've been experimenting with
different ways to calculate some of the stuff, and ANALYZE prints info
about the calculated values and timings (this can be disabled by
removing the STATS_CROSS_CHECK define).

Finally, brincostestimate() loads the statistics and uses it for
costing. At the moment it uses only the average number of overlaps.

Trivial example:

create table t (a int) with (fillfactor = 10);

  insert into t
  select (case when mod(i,22) = 0 then 100000000
               when mod(i,22) = 1 then 0
               else i end)
    from generate_series(1,300000) s(i);

  create index on t using brin (a) with (pages_per_range = 1);

The table fits 22 rows per page, and the data is mostly sequential,
except that every page has both 0 and 100000000. The correlation however
remains fairly high:

  # select correlation from pg_stats where tablename = 't';
   correlation
  -------------
     0.8303595
  (1 row)

Now, let's do a simple query:

# explain (analyze, buffers, timing off) select * from t where a = 500;

                              QUERY PLAN
------------------------------------------------------------------------
 Bitmap Heap Scan on t  (cost=154.00..254.92 rows=2 width=4)
                        (actual rows=1 loops=1)
   Recheck Cond: (a = 500)
   Rows Removed by Index Recheck: 299999
   Heap Blocks: lossy=13637
   Buffers: shared hit=13695
   ->  Bitmap Index Scan on t_a_idx  (cost=0.00..154.00 rows=26 width=0)
                                     (actual rows=136370 loops=1)
         Index Cond: (a = 500)
         Buffers: shared hit=58
 Planning:
   Buffers: shared hit=1
 Planning Time: 0.173 ms
 Execution Time: 101.972 ms
(12 rows)

That's pretty poor, because brincostestimate() still thinks it'll be
enough to read one or two page ranges (because 1/0.8 = ~1.2).

Now, with the extra statistics:

SET enable_indexam_stats = true;
ANALYZE t;

                               QUERY PLAN
----------------------------------------------------------------------
 Bitmap Heap Scan on t  (cost=157.41..17544.41 rows=2 width=4)
                        (actual rows=1 loops=1)
   Recheck Cond: (a = 500)
   Rows Removed by Index Recheck: 299999
   Heap Blocks: lossy=13637
   Buffers: shared hit=13695
   ->  Bitmap Index Scan on t_a_idx  (cost=0.00..157.41 rows=300000
                               width=0) (actual rows=136370 loops=1)
         Index Cond: (a = 500)
         Buffers: shared hit=58
 Planning:
   Buffers: shared hit=1
 Planning Time: 0.230 ms
 Execution Time: 104.603 ms
(12 rows)

So in this case we realize we actually have to scan the whole table, all
~13637 ranges, and the cost reflects that.

Feel free to experiment with other data sets.

regards

[1]
https://www.postgresql.org/message-id/e70fa091-e338-1598-9de4-6d0ef6b693e2%40enterprisedb.com

--
Tomas Vondra
EnterpriseDB: http://www.enterprisedb.com
The Enterprise PostgreSQL Company

---
## [GNOME/glib](https://github.com/GNOME/glib)@[b8e1ecdd6b...](https://github.com/GNOME/glib/commit/b8e1ecdd6bfd6ff00b7b70f6177549f3a8d3cba3)
#### Tuesday 2022-10-18 17:13:59 by Michael Catanzaro

Automatically disable cast checks when building with optimization

Cast checks are slow. We seem to have some rough consensus that they are
important for debug builds, but not for release builds. Problem is, very
few apps define G_DISABLE_CAST_CHECKS for release builds. Worse, it's
undocumented, so there's no way apps could even be expected to know
about it.

We can get the right default is almost all situations by making this
depend on the __OPTIMIZE__ preprocessor definition. This is a GCC-specific
thing, although Clang supports it too. If the compiler does not define
__OPTIMIZE__, then this commit does no harm: you can still use
G_DISABLE_CAST_CHECKS as before. When checking __OPTIMIZE__, we are
supposed to ensure our code has the same behavior as it would if we do
not, which will be true except in case the check fails (which is
programmer error).

Downside: this will not automatically do the right thing with -Og,
because __OPTIMIZE__ is always defined to 1. We don't want to disable
cast checks automatically if using -O0 or -Og. There's no way to
automatically fix this, but we can create an escape hatch by allowing
you to define G_DISABLE_CAST_CHECKS=0 to force-enable cast checks. In
practice, I don't think this matters much because -Og kinda failed:
GCC's man page says it should be a superior debugging experience to -O0,
but it optimizes variables away so it's definitely not.

Another downside: this is bad if you really *do* want cast checks in
release builds. The same solution applies: define
G_DISABLE_CAST_CHECKS=0 and you'll get your cast checks.

---
## [Axlefublr/lib-v2](https://github.com/Axlefublr/lib-v2)@[88e0a2b0a8...](https://github.com/Axlefublr/lib-v2/commit/88e0a2b0a8721e2fe60ed2e633b2e1bc9f5c7a17)
#### Tuesday 2022-10-18 18:23:21 by Axlefublr

Windows. You little fucker. You made a shit of piece with your *trash* tool. It is fucking bad this storage system. I will become back my money. I hope you will in your next time a cow on a trash farm, you sucker.

---
## [justinwritescode/deploy-to-docs](https://github.com/justinwritescode/deploy-to-docs)@[c6a547f4e3...](https://github.com/justinwritescode/deploy-to-docs/commit/c6a547f4e3ba94c6532acab295564cd1bef37723)
#### Tuesday 2022-10-18 18:48:18 by Justin

HOLY SHIT IT FINALLY FUCKING WORKS!

Initial commit

Create action.yml

Update action.yml

Update action.yml

Update action.yml

action.yml

Update action.yml

Update action.yml

Update action.yml

more changes

foo

added folder name to action inputs

added folder name to action inputs

update the damn workflow

bump action

bump action

bump the action

bump

bump

maybe i'm done?

grr

foo

foo

grr

maybe?!

fix folder_name

changes

shell:bash

remove setup-git

login

change back to using the checkout action

fixing syntax error

changing strategy

modified:   action.yml

commit

41

42

43

44

---
## [apollographql/apollo-server](https://github.com/apollographql/apollo-server)@[d0d8f4be70...](https://github.com/apollographql/apollo-server/commit/d0d8f4be705065745bd3767a62b8025abe774842)
#### Tuesday 2022-10-18 19:18:55 by Trevor Scheer

Distribute `@apollo/server-integration-testsuite` as CJS (correctly) (#7055)

Right now the integration testsuite package declares `"type": "module"`
but builds as CJS. This seems to be problematic for some integrations,
and we should resolve the misconfiguration.

This also moves the tsconfig/build "things" over to the CJS branch of
our build step. This also removes the ESM configuration options for how
we run jest/ts-jest in this repo.

Confirmed this doesn't cause a regression in our local dev in that a
change in test code is immediately reflected in a test run without
running an additional build.

Fixes #7042

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
## [InsightfulParasite/lobotomy-corp13](https://github.com/InsightfulParasite/lobotomy-corp13)@[0220bde488...](https://github.com/InsightfulParasite/lobotomy-corp13/commit/0220bde48808454df3754d7c71953f66553dcd47)
#### Tuesday 2022-10-18 19:56:55 by PotatoTomahto

pathfinding

revert

oops

oops 2

god fragment

fixes

fixes oopsie

forgot scorched girl

real scorched fix:

typo

better patrolling

final

forgot about dreaming

dreaming current name

fragment oopsies

violet oopsie

really the final one

final final one

---
## [peff/git](https://github.com/peff/git)@[88f6b5ee66...](https://github.com/peff/git/commit/88f6b5ee66b9dd0b217f917b5ac5f0c1a4b14592)
#### Tuesday 2022-10-18 20:55:24 by Jeff King

Makefile: force -O0 when compiling with SANITIZE=leak

Compiling with -O2 can interact badly with LSan's leak-checker, causing
false positives. Imagine a simplified example like:

  char *str = allocate_some_string();
  if (some_func(str) < 0)
          die("bad str");
  free(str);

The compiler may eliminate "str" as a stack variable, and just leave it
in a register. The register is preserved through most of the function,
including across the call to some_func(), since we'd eventually need to
free it. But because die() is marked with NORETURN, the compiler knows
that it doesn't need to save registers, and just clobbers it.

When die() eventually exits, the leak-checker runs. It looks in
registers and on the stack for any reference to the memory allocated by
str (which would indicate that it's not leaked), but can't find one.  So
it reports it as a leak.

Neither system is wrong, really. The C standard (mostly section 5.1.2.3)
defines an abstract machine, and compilers are allowed to modify the
program as long as the observable behavior of that abstract machine is
unchanged. Looking at random memory values on the stack is undefined
behavior, and not something that the optimizer needs to support. But
there really isn't any other way for a leak checker to work; it
inherently has to do undefined things like scouring memory for pointers.
So the two things are inherently at odds with each other. We can't fix
it by changing the code, because from the perspective of the program
running in an abstract machine, there is no leak.

This has caused real false positives in the past, like:

  - https://lore.kernel.org/git/patch-v3-5.6-9a44204c4c9-20211022T175227Z-avarab@gmail.com/

  - https://lore.kernel.org/git/Yy4eo6500C0ijhk+@coredump.intra.peff.net/

  - https://lore.kernel.org/git/Y07yeEQu+C7AH7oN@nand.local/

This patch makes those go away by forcing -O0 when compiling with LSan.
There are a few ways we could do this:

  - we could just teach the linux-leaks CI job to set -O0. That's the
    smallest change, and means we wouldn't get spurious CI failures. But
    it doesn't help people looking for leaks manually or in a specific
    test (and because the problem depends on the vagaries of the
    optimizer, investigating these can waste a lot of time in
    head-scratching as the problem comes and goes)

  - we default to -O2 in CFLAGS; we could pull this out to a separate
    variable ("-O$(O)" or something) and modify "O" when LSan is in use.
    This is the most flexible, in that you could still build with "make
    O=2 SANITIZE=leak" if you really wanted to (say, for experimenting).
    But it would also fail to kick in if the user defines their own
    CFLAGS variable, which again leads to head-scratching.

  - we can just stick -O0 into BASIC_CFLAGS when enabling LSan. Since
    this comes after the user-provided CFLAGS, it will override any
    previous -O setting found there. This is more foolproof, albeit less
    flexible. If you want to experiment with an optimized leak-checking
    build, you'll have to put "-O2 -fsanitize=leak" into CFLAGS
    manually, rather than using our SANITIZE=leak Makefile magic.

Since the final one is the least likely to break in normal use, this
patch uses that approach.

The resulting build is a little slower, of course, but since LSan is
already about 2x slower than a regular build, another 10% slowdown isn't
that big a deal.

---
## [entrez/NetHack](https://github.com/entrez/NetHack)@[4c98ba493b...](https://github.com/entrez/NetHack/commit/4c98ba493bb7eaa7c556c4b720a7b6df7ea74d0e)
#### Tuesday 2022-10-18 21:51:03 by Michael Meyer

Remove explicit 'none' opt from autounlock handler

The autounlock handler included an explicit 'none' option, a choice that
gave it a different UX from similar existing compound option handlers
(e.g. paranoid_confirm or pickup_types), which set 'none' simply by
deselecting all options.  It didn't make the menu any easier to use (at
least in my experience), since in order to go from some combination of
options to 'none', you'd have to deselect everything anyway (which on
its own was enough to set 'none', so there was no reason to explicitly
select it after doing so).

Make the autounlock handler work like other compound option handlers,
such that deselecting all options is the way to set 'none', and there is
no explicit 'none' option included in the list.

---
## [bearrrrrrrr/coyote-bayou](https://github.com/bearrrrrrrr/coyote-bayou)@[288f673652...](https://github.com/bearrrrrrrr/coyote-bayou/commit/288f6736526554c75abbcb09c92acb457be1c9b0)
#### Tuesday 2022-10-18 22:10:31 by Superlagg

Merge remote-tracking branch 'upstream/master' into that-stupid-fuckin-dumb-shitass-fuckin--fuck-fuckass-shitfuck-gun-thing-that-isnt-alll-that-bad-honestly

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[223e8bfd96...](https://github.com/LemonInTheDark/tgstation/commit/223e8bfd96a7762f0d23dd9b789fa90be1a572ec)
#### Tuesday 2022-10-18 22:45:03 by Time-Green

Fixes gravity pulse and transparent floor plane sharing a layer (#70124)

fixes gravity pulse and transparent floor plane sharing a layer

Broken by #69642 , sorry
I'll open up a seperate PR later today with a unit test to catch these cases
(my later today is in like 10 hours)

closes #70123 (weird fucking floors)

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[c745f4bf46...](https://github.com/san7890/bruhstation/commit/c745f4bf46036d8b5a0e5f0e077f17a798e88973)
#### Tuesday 2022-10-18 23:01:52 by san7890

I FUCKING LOVE UNIT TESTS

THIS SHIT WILL NEVER BREAK AGAIN!!!

---
## [david-rowley/postgres](https://github.com/david-rowley/postgres)@[1c27d16e6e...](https://github.com/david-rowley/postgres/commit/1c27d16e6e5c1f463bbe1e9ece88dda811235165)
#### Tuesday 2022-10-18 23:22:37 by Tom Lane

Revise tree-walk APIs to improve spec compliance & silence warnings.

expression_tree_walker and allied functions have traditionally
declared their callback functions as, say, "bool (*walker) ()"
to allow for variation in the declared types of the callback
functions' context argument.  This is apparently going to be
forbidden by the next version of the C standard, and the latest
version of clang warns about that.  In any case it's always
been pretty poor for error-detection purposes, so fixing it is
a good thing to do.

What we want to do is change the callback argument declarations to
be like "bool (*walker) (Node *node, void *context)", which is
correct so far as expression_tree_walker and friends are concerned,
but not change the actual callback functions.  Strict compliance with
the C standard would require changing them to declare their arguments
as "void *context" and then cast to the appropriate context struct
type internally.  That'd be very invasive and it would also introduce
a bunch of opportunities for future bugs, since we'd no longer have
any check that the correct sort of context object is passed by outside
callers or internal recursion cases.  Therefore, we're just going
to ignore the standard's position that "void *" isn't necessarily
compatible with struct pointers.  No machine built in the last forty
or so years actually behaves that way, so it's not worth introducing
bug hazards for compatibility with long-dead hardware.

Therefore, to silence these compiler warnings, introduce a layer of
macro wrappers that cast the supplied function name to the official
argument type.  Thanks to our use of -Wcast-function-type, this will
still produce a warning if the supplied function is seriously
incompatible with the required signature, without going as far as
the official spec restriction does.

This method fixes the problem without any need for source code changes
outside nodeFuncs.h/.c.  However, it is an ABI break because the
physically called functions now have names ending in "_impl".  Hence
we can only fix it this way in HEAD.  In the back branches, we'll have
to settle for disabling -Wdeprecated-non-prototype.

Discussion: https://postgr.es/m/CA+hUKGKpHPDTv67Y+s6yiC8KH5OXeDg6a-twWo_xznKTcG0kSA@mail.gmail.com

---
## [macladson/lighthouse](https://github.com/macladson/lighthouse)@[66eca1a882...](https://github.com/macladson/lighthouse/commit/66eca1a88218462235cb76a116dc3c6a1853444f)
#### Tuesday 2022-10-18 23:24:15 by Michael Sproul

Refactor op pool for speed and correctness (#3312)

## Proposed Changes

This PR has two aims: to speed up attestation packing in the op pool, and to fix bugs in the verification of attester slashings, proposer slashings and voluntary exits. The changes are bundled into a single database schema upgrade (v12).

Attestation packing is sped up by removing several inefficiencies: 

- No more recalculation of `attesting_indices` during packing.
- No (unnecessary) examination of the `ParticipationFlags`: a bitfield suffices. See `RewardCache`.
- No re-checking of attestation validity during packing: the `AttestationMap` provides attestations which are "correct by construction" (I have checked this using Hydra).
- No SSZ re-serialization for the clunky `AttestationId` type (it can be removed in a future release).

So far the speed-up seems to be roughly 2-10x, from 500ms down to 50-100ms.

Verification of attester slashings, proposer slashings and voluntary exits is fixed by:

- Tracking the `ForkVersion`s that were used to verify each message inside the `SigVerifiedOp`. This allows us to quickly re-verify that they match the head state's opinion of what the `ForkVersion` should be at the epoch(s) relevant to the message.
- Storing the `SigVerifiedOp` on disk rather than the raw operation. This allows us to continue track the fork versions after a reboot.

This is mostly contained in this commit 52bb1840ae5c4356a8fc3a51e5df23ed65ed2c7f.

## Additional Info

The schema upgrade uses the justified state to re-verify attestations and compute `attesting_indices` for them. It will drop any attestations that fail to verify, by the logic that attestations are most valuable in the few slots after they're observed, and are probably stale and useless by the time a node restarts. Exits and proposer slashings and similarly re-verified to obtain `SigVerifiedOp`s.

This PR contains a runtime killswitch `--paranoid-block-proposal` which opts out of all the optimisations in favour of closely verifying every included message. Although I'm quite sure that the optimisations are correct this flag could be useful in the event of an unforeseen emergency.

Finally, you might notice that the `RewardCache` appears quite useless in its current form because it is only updated on the hot-path immediately before proposal. My hope is that in future we can shift calls to `RewardCache::update` into the background, e.g. while performing the state advance. It is also forward-looking to `tree-states` compatibility, where iterating and indexing `state.{previous,current}_epoch_participation` is expensive and needs to be minimised.

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[1af2c12e05...](https://github.com/TaleStation/TaleStation/commit/1af2c12e0501c2cf5eb5946738360564fd78cea4)
#### Tuesday 2022-10-18 23:56:46 by TaleStationBot

[MIRROR] [MDB IGNORE] canUseTopic now uses TRUE/FALSE instead of defines that just say TRUE (#2676)

* canUseTopic now uses TRUE/FALSE instead of defines that just say TRUE (#69790)

* canUseTopic now uses TRUE/FALSE instead of defines that just say TRUE

The most idiotic thing I've seen is canUseTopic's defines, they literally just define TRUE, you can use it however you want, it doesn't matter, it just means TRUE. You can mix and match the args and it will set that arg to true, despite the name.

It's so idiotic I decided to remove it, so now I can reclaim a little bit of my sanity.

* canUseTopic now uses TRUE/FALSE instead of defines that just say TRUE

* fix

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>

---

