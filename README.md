## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-02-21](docs/good-messages/2022/2022-02-21.md)


1,856,887 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,856,887 were push events containing 2,918,353 commit messages that amount to 213,454,685 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 35 messages:


## [cyberitsolutions/bootstrap2020](https://github.com/cyberitsolutions/bootstrap2020)@[bc67a92c74...](https://github.com/cyberitsolutions/bootstrap2020/commit/bc67a92c74a75569405559b88f629f764e45ed55)
#### Monday 2022-02-21 00:13:03 by Trent W. Buck

openttd: fix music

Use timidity with Debian's default MIDI "sound font".
This is a little bigger (150MB vs freepats 30MB), but
avoids editing config file.

I tried using fluidsynth, and while "fluidsynth -a pulseaudio" works,
there is AFAICT no way to tell fluidsynth to read /etc/default/fluidsynth.
Nor is there any way to make openttd run "fluidsynth -a pulseaudio", because
OpenTTD is (I think) using libfluidsynth, not the actual binary?

Anyway, timidity works and I don't care anymore!

    13:38 <twb> I can hear plane sound effects in my VM, but not any music
    13:40 <twb> # timidity /usr/share/games/openttd/baseset/OpenMSX-0.4.0/*.mid ===> /etc/timidity/fluidr3_gm.cfg: No such file or directory
    13:40 <twb> That sounds like my fault somehow
    13:40 <twb> Looks like Debian changed the default from "freepats" to "fluid-soundfont"
    13:41 <twb> Aw yeah, phat tunes are back
    13:43 <glx> if you can, it's better to use fluidsynth than timidity
    13:47 <twb> If fluidsynth is installed, will openttd just use it?
    13:48 <twb> This is for 1.10
    13:48 <twb> If I have to edit config files in each user's $HOME that is a pain.
    13:49 <twb> Debian's definitely at least building against libfluidsynth-dev

    13:45 <twb> Sigh.  So freepats (30MB) is replaced by fluid-soundfont-gm (150MB).
    13:45 <twb> I can move it back, but that's slightly icky because switching back has to happen in a different place, so the "choose freepats" and "select freepats" changes won't be obviously connected
    13:45 <twb> So I'm intending to just use the fluid-soundfont-gm package instead

    ⋮

    14:00 <twb> Answer: no
    14:01 <twb> root@desktop-inmate:~# fluidsynth /usr/share/games/openttd/baseset/*/*.mid ===> exec of JACK server (command = "/usr/bin/jackd") failed: No such file or directory
    14:01 <twb> ugghhhhhh
    14:02 <twb> Why isn't it just playing music via alsa or even pulseaudio
    14:05 <twb> https://www.fluidsynth.org/api/fluidsettings.xml  says it SHOULD be defaulting to alsa
    14:06 <twb> "fluidsynth -a alsa *.mid" works but I don't see how to make openttd do that for all users
    14:26 <twb> OK I can't see how to make fluidsynth Just Work so I'm going to continue using timidity.
    14:28 <twb> Oh hrm that's weird
    14:28 <twb> Why is fluidsynth using /etc/default like it's a daemon
    14:36 <twb> "fluidsynth -a pulseaudio *.mid" works, but moving -a pulseaudio into /etc/defaults/fluidsynth doesn't
    14:36 <twb> i.e. (echo SOUND_FONT=/usr/share/sounds/sf3/default-GM.sf3; echo OTHER_OPTS='"-a pulseaudio"')  >/etc/default/fluidsynth
    14:37 <twb> AFAICT fluidsynth just ignores that file completely

---
## [Mu-L/crawl](https://github.com/Mu-L/crawl)@[a852ce8369...](https://github.com/Mu-L/crawl/commit/a852ce8369264a3a4759b99df0bbba7645a78c97)
#### Monday 2022-02-21 01:30:31 by Nicholas Feinberg

Play with ranged weapon stats more

Following some thinking about ranged weapons, here's a new set of
ammoless stats. Philosophy:

- Slings are high-skill 1-handers. Hunting slings are vaguely like
  war axes, and fustibaluses are no longer ultra-rare but are now
  more like broad axes.
- Bows are high-skill 2-handers.
- Crossbows are lower-skill - it takes fairly little to get the hand
  crossbow or the arbalest to mindelay. The triple crossbow is still
  high-skill, but it's quite rare, so doesn't define the 'feel' of
  the class, much as you can't rely on finding a triple sword as a
  lbl user or an exec axe as an axe user. (Unless a gifting god gets
  involved.)

If we're going to keep all these item classes, it would be great to
have some more obvious and pronounced gimmicks. I suspect we'll end
up merging or removing some of these at some point, but that's a
larger project than I'm ready for right now.

TODO: make fustibali spawn at a higher rate - right now they're about
1/5th as common as I'd like.

---
## [azerothcore/mod-anticheat](https://github.com/azerothcore/mod-anticheat)@[a354922e07...](https://github.com/azerothcore/mod-anticheat/commit/a354922e07020f5ba5c7c6aa43d95eaae10aa1b3)
#### Monday 2022-02-21 01:55:31 by MDIC

Update: Readjusted SQL, New Dectection , new Conf

Readjusted the Sql again, Removes the teleporthack_report collumns. It is pretty much worthless with its insane high count that would cause drag on the db and well not needed, it seems like a good idea at the time but it isnt, instead it will add a +1 to the total_reports collumn and the teleport and ignore control hacks will spam their own message once the reports hit default 70 or whatever the user has set. New detection type Ignore Control Hack, This is if a player is rooted or stunned, they are able to still move when effected.

---
## [DesmontTiney/tgstation](https://github.com/DesmontTiney/tgstation)@[2209c36036...](https://github.com/DesmontTiney/tgstation/commit/2209c36036c5c0c303443fd4a6304da9384e5107)
#### Monday 2022-02-21 02:51:06 by san7890

Fixes Weird Area Definition on DeltaStation (#64986)

So, there I was. Pondering the blobbosity of Auxiliary Base Construction. Deciphering and unclothing the issue in my mind in order to better comphrehend it. I was there for a few moments, until this ugly beast of a fucking area definition caught my eye:

Hideous. Repugnant. I was relishing the thought of dissecting Auxiliary Base Construction into fifteen million more areas (it _will_ lessen obtusities) when that scraggletooth of an utterly mortifying error forced me into a visceral rage: the likes of which have never been experienced on this planet Earth.

---
## [Unfunkable/CK3-Expanded-Empires](https://github.com/Unfunkable/CK3-Expanded-Empires)@[2e2eb2ec7f...](https://github.com/Unfunkable/CK3-Expanded-Empires/commit/2e2eb2ec7ff798372cdc003756a58df5d0e3d079)
#### Monday 2022-02-21 03:44:00 by Unfunkable

Fix excommunication detection and pretender opinion

Excommunication is now detected accurately, every single same-faith Emperor needs to be excommunicated to form a new Empire with the Church's blessing. All existing emperors will also have the pretender opinion malus even if the church crowned you.

---
## [harche/api](https://github.com/harche/api)@[5b82635ef1...](https://github.com/harche/api/commit/5b82635ef101e7c10b5fcbbcfb81315bb7a0da20)
#### Monday 2022-02-21 05:04:08 by W. Trevor King

config/v1/types_cluster_version: Add capabilties properties

Roughly as described in [enhancement].  After discussion with Ben and
David, we've made the following changes:

# spec

## capabilities

The [enhancement] didn't have an opinion on whether or not this should
be a pointer.  I've gone with pointer, because I'm fine allowing folks
to leave this unset.  The docs for this pointer property point out
that there's no distinction between nil (Go, or for JSON, null) and an
empty object (&ClusterVersionCapabilitiesSpec{} in Go, {} in JSON), so
we don't have to rehash all the ClusterVersionCapabilitiesSpec
children defaults here, where they'd likely go stale as folks update
defaults within ClusterVersionCapabilitiesSpec or add new child
properties.

### baselineCapabilitySet

David prefered this name to the [enhancement]'s inclusionDefault, and
Ben and I are fine with that name.

David also prefered None to Exclude and vCurrent to Include, with
additional values like v4.11 for "give me the 4.11 stuff, but not new
4.12 stuff, until I have time to look that over after I update to
4.12".  That seems overly complicated to me, and also like we coulld
add v4.11 later if folks felt None and vCurrent weren't convenient
enough, but David wanted v4.11 out of the gate.  We can always see how
it plays out in production, and we can stop adding new v4.y forms if
they aren't popular enough to be worth maintaining.  There's an enum
type to make it easy to validate, and hard to typo, these values.

There's also a map, so consumers like the cluster-version operator who
vendor the API repository can get the API-maintainer-intended
capability membership for each set, now that those semantics are more
complicated than all or nothing.

There were a few ways we could have taken the property default here:

a. Explicit +kubebuilder:default:=... .  No option for folks to sit on
   the fence, or to adjust existing clusters later without the admin's
   explicit buy-in.  But no ambiguity about what happens if the user
   has no opinion.

b. omitempty, and docs for "we'll pick a sane default if you don't
   care", that don't commit to a specific default.  Great for when we
   decide to change our default preference, because we don't need to
   hunt down buy-in from admins that have deferred to us.  Not great
   for folks who are mildly curious about our current choice, but who
   still trust us to evolve the default (I think this set is nearly
   empty).

c. omitempty, and docs for "the current default is A, but who knows
   tomorrow".  Effectively (b), but also gives folks some information
   that's not actionable which can go stale as soon as they close
   their eyes.

(a) makes sense if we are confident we will never want to change our
default, and that seems plausible in this case.  (b) makes sense when
we think we might change our default, and I'm fine with that in this
case too.  I don't really understand the use case for (c), but as
David points out, even if we do change the default, we don't expect to
change it often, so maybe my personal take is off and there are a
bunch of folks who are mildly curious about our current choice, but
who still trust us to evolve the default.  Anyhow, David's the
approver, so we're going with (c).

### additionalEnabledCapabilities

David prefered this name to the [enhancement]'s inclusionDefault, and
Ben and I are fine with that name.

In the [enhancement], Ben had intended to distribute the ability to
create new capabilities to all manifest-providing repositories, simply
by declaring the capability.openshift.io/name annotation.  David was
worried about validation, and also possibly about insufficiently
scoped names between separate teams, so this pull request declares a
central enum where API maintainers can review and approve new
capability names, and work them into the appropriate entries in the
set maps.  The installer and cluster-version operator will have to
bump their vendored API version after each addition to pick up the new
changes, but new capability additions shouldn't be too frequent to
make that particularly painful.

### exclude

The [enhancement] also provided a way to drop specific capabilities
from the selected set (inclusionDefault or baselineCapabilitySet).
Ben still feels like that will be popular, but David is skeptical, and
because we can always add a property in this space later without
breaking backwards compatibility, we're leaving it off for now.

# status

## capabilities

The [enhancement] didn't have an opinion on whether or not this should
be a pointer.  I've gone with non-pointer, because we will always
declare at least some capabilities (e.g. knownCapabilities), so users
will be able to discover additional capabilities which they might want
to enable in their cluster.

### enabledCapabilities

David prefered this name to the [enhancement]'s include, and Ben's ok
with that name.  I'm not wild about 'Capabilities' in:

  status:
    capabilities:
      enabledCapabilities: ...

but David was committed, citing the example of:

  FeatureGateSelection.FeatureSet

Although FeatureGateSelection is consumed with less context:

  type FeatureGateSpec struct {
	FeatureGateSelection `json:",inline"`
  }

I'd pushed back against the stuttering in [stutterPrecedent], but
without success, and :shrug:, doesn't matter all that much if folks
have to type a few redundant characters to use this property.

### knownCapabilities

The [enhancement] had floated 'exclude'.  There are a few capability
sets in play for the status listings:

* A is the set of all caps.
* I is the set of included caps.
* E is the set of excluded caps.
* Each cap must be either included or excluded, so I and E are disjoint, and the union of I and E is A.

So you can take any two of those three sets and construct the one
you're missing:

* A = I ∪ E
* E = A - I
* I = A - E

If we have to pick two to include in status, picking I and E gives us
all the data we need, and saves a few bytes by excluding the largest,
which is A.  But David preferred picking I (as enabledCapabilities)
and A (as knownCapabilities) [knownCapabilities], so that's what we're
doing in this commit.

### inclusionDefault

The [enhancement] also provided a way to echo the spec set in an
inclusionDefault status property.  I've left that out of the status
structure, because I'm using explicit, exhaustive list for
enabledCapabilities and knownCapabilities there.  The exhaustive lists
will provide a convenient set (via A - I set subtraction) of "things
you don't have right now, but which you could choose to install right
now", so admins don't have to guess about their options there.  With
the exhaustive lists, reflecting the default setting didn't seem to
add much useful information.  And we can always add that property to
the status structure later if we do decide it would be useful.

## conditions

I have not created a constant with the status.conditions[] type that
will be used to declare "we are installing a capability you have not
asked for, because we don't support uninstalling capabilities, and
that one was tainted in via your cluster's history".  We can come back
and declare that constant later if we want, although that's somewhat
complicated by the fact that we use ClusterOperatorStatusCondition,
and the new condition type would not be something that makes sense for
ClusterOperator.

[enhancement]: https://github.com/openshift/enhancements/blob/88cb7438f3ac0a8121e3cef87cb144097ece8cda/enhancements/installer/component-selection.md
[knownCapabilities]: https://github.com/openshift/api/pull/1106#discussion_r799819632
[validation]: https://book.kubebuilder.io/reference/generating-crd.html#validation
[statusPropertyNames]: https://github.com/openshift/api/pull/1106#discussion_r799819632
[stutterPrecedent]: https://github.com/openshift/api/pull/1106#discussion_r799879689

---
## [swifterjack/Shiptest](https://github.com/swifterjack/Shiptest)@[031c0866ed...](https://github.com/swifterjack/Shiptest/commit/031c0866ed35af71a3ac4782fe4d6aa9e6464f53)
#### Monday 2022-02-21 07:14:21 by SweetBlueSylveon

Nanotrasen Deserter Vault Ruin (#732)

* Nanotrasen Deserter Vault Ruin

A ruin based around a Nanotrasen ultra secure vault. It should spawn on the ice planet. This commit adds everything.

* Map Changes

-Replaces Glockroach family with Jack and Jill, Slaughter and Laughter demons.
-Replaces Sniper Rifle with Particle Acceleration Rifle.
-Replaces Sniper Rifle ammo with a single upgraded weapon power cell.
-Adds a sentience potion and cns rebooter implant to vault safe since there were only mats in it otherwise.

* Minor commit

Removes a cybernetic that should have been removed before the last commit.

* Update code/game/area/areas/ruins/icemoon.dm

I'm dumb and didn't realize I did this. Also didn't realize linters was the code checker, so I didn't realize to check the code. I know now! Thanks for the help.

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

* Adds the knight gear design disk.

Adds the "magical disk of smithing" to the safe.

* Unmodularizes your Modularization

Moves the datum to an unmodularized folder.

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

---
## [freedesktop/NetworkManager](https://github.com/freedesktop/NetworkManager)@[dac12a8d61...](https://github.com/freedesktop/NetworkManager/commit/dac12a8d6178a6d82fc0913ad8825c8556380ba8)
#### Monday 2022-02-21 07:16:24 by Thomas Haller

platform: support IPv6 mulitpath routes and fix cache inconsistency

Add support for IPv6 multipath routes, by treating them as single-hop
routes. Otherwise, we can easily end up with an inconsistent platform
cache.

Background:
-----------

Routes are hard. We have NMPlatform which is a cache of netlink objects.
That means, we have a hash table and we cache objects based on some
identity (nmp_object_id_equal()). So those objects must have some immutable,
indistinguishable properties that determine whether an object is the
same or a different one.

For routes and routing rules, this identifying property is basically a subset
of the attributes (but not all!). That makes it very hard, because tomorrow
kernel could add an attribute that becomes part of the identity, and NetworkManager
wouldn't recognize it, resulting in cache inconsistency by wrongly
thinking two different routes are one and the same. Anyway.

The other point is that we rely on netlink events to maintain the cache.
So when we receive a RTM_NEWROUTE we add the object to the cache, and
delete it upon RTM_DELROUTE. When you do `ip route replace`, kernel
might replace a (different!) route, but only send one RTM_NEWROUTE message.
We handle that by somehow finding the route that was replaced/deleted. It's
ugly. Did I say, that routes are hard?

Also, for IPv4 routes, multipath attributes are just a part of the
routes identity. That is, you add two different routes that only differ
by their multipath list, and then kernel does as you would expect.
NetworkManager does not support IPv4 multihop routes and just ignores
them.
Also, a multipath route can have next hops on different interfaces,
which goes against our current assumption, that an NMPlatformIP4Route
has an interface (or no interface, in case of blackhole routes). That
makes it hard to meaningfully support IPv4 routes. But we probably don't
have to, because we can just pretend that such routes don't exist and
our cache stays consistent (at least, until somebody calls `ip route
replace` *sigh*).

Not so for IPv6. When you add (`ip route append`) an IPv6 route that is
identical to an existing route -- except their multipath attribute -- then it
behaves as if the existing route was modified and the result is the
merged route with more next-hops. Note that in this case kernel will
only send a RTM_NEWROUTE message with the full multipath list. If we
would treat the multipath list as part of the route's identity, this
would be as if kernel deleted one routes and created a different one (the
merged one), but only sending one notification. That's a bit similar to
what happens during `ip route replace`, but it would be nightmare to
find out which route was thereby replaced.
Likewise, when you delete a route, then kernel will "subtract" the
next-hop and sent a RTM_DELROUTE notification only about the next-hop that
was deleted. To handle that, you would have to find the full multihop
route, and replace it with the remainder after the subtraction.

NetworkManager so far ignored IPv6 routes with more than one next-hop, this
means you can start with one single-hop route (that NetworkManger sees
and has in the platform cache). Then you create a similar route (only
differing by the next-hop). Kernel will merge the routes, but not notify
NetworkManager that the single-hop route is not longer a single-hop
route. This can easily cause a cache inconsistency and subtle bugs. For
IPv6 we MUST handle multihop routes.

Kernels behavior makes little sense, if you expect that routes have an
immutable identity and want to get notifications about addition/removal.
We can however make sense by it by pretending that all IPv6 routes are
single-hop! With only the twist that a single RTM_NEWROUTE notification
might notify about multiple routes at the same time. This is what the
patch does.

The Patch
---------

Now one RTM_NEWROUTE message can contain multiple IPv6 routes
(NMPObject). That would mean that nmp_object_new_from_nl() needs to
return a list of objects. But it's not implemented that way. Instead,
we still call nmp_object_new_from_nl(), and the parsing code can
indicate that there is something more, indicating the caller to call
nmp_object_new_from_nl() again in a loop to fetch more objects.

In practice, I think all RTM_DELROUTE messages for IPv6 routes are
single-hop. Still, we implement it to handle also multi-hop messages the
same way.

Note that we just parse the netlink message again from scratch. The alternative
would be to parse the first object once, and then clone the object and
only update the next-hop. That would be more efficient, but probably
harder to understand/implement.

https://bugzilla.redhat.com/show_bug.cgi?id=1837254#c20

---
## [crawl/crawl](https://github.com/crawl/crawl)@[37ed61cfd3...](https://github.com/crawl/crawl/commit/37ed61cfd31eba42ae987bc4ed6f9854b2d0d735)
#### Monday 2022-02-21 07:47:25 by Nicholas Feinberg

Improve characters' starting kits (Hellmonk)

One of the most interesting and exciting decisions in Dungeon Crawl
is when and where to use your consumable items. In the very early
game, characters may not yet have any consumables, which diminishes
the tactical aspect of the game.

So, let's try to give most characters some options which, if used
wisely, can help them with a tough situation.

- All 'mages' ('pure casters') start with a potion of magic.
- Fighters get an additional potion of might.
- Gladiators get a few throwing weapons, roughly half of what the AM
  throwing start got.
- Monks get a potion of ambrosia. (See, it's divine.)
- Hunters get a throwing net. (Not sure about this one.)
- Brigands get an additional poisoned & curare dart.
- Artificers trade their xom piece for three charges of iceblast.
- Wanderers get an additional random potion or scroll.
- Delvers get nothing, for now, since I'm already pretty happy with
  how they play. They're a challenge anyway, really. :)
- Berserkers and Cinder Acolytes likewise get nothing. They already
  have perfectly good early game buttons.
- Abyssal Knights start at 60 piety (just over 2*) instead of 38 (just
  over 1*). This should allow them to use Bend Space if needed.
  (I think they're still quite weak.)
- Chaos Knights get Artificer's xom chesspiece.
- Transmuters get a potion of lignification, which should work well
  with their unarmed combat focus. It's also very thematic.
- Warpers get another scroll of blinking and a few more boomerangs of
  dispersal. This is one of the strongest boosts, but warpers were
  not particularly strong to start with.
- Arcane Markspersons get a few boomerangs of dispersal too. I'm sort
  of hoping to rework this background more broadly at some point.
- Enchanters get another potion of invisibility.

This should also be a nice compensation for various recent changes that
increased early game difficulty.

---
## [mawrick26/SM8250](https://github.com/mawrick26/SM8250)@[b22c2c7338...](https://github.com/mawrick26/SM8250/commit/b22c2c733813b0d40328abd5f1d4a18032802528)
#### Monday 2022-02-21 08:40:40 by George Spelvin

lib/sort: make swap functions more generic

Patch series "lib/sort & lib/list_sort: faster and smaller", v2.

Because CONFIG_RETPOLINE has made indirect calls much more expensive, I
thought I'd try to reduce the number made by the library sort functions.

The first three patches apply to lib/sort.c.

Patch #1 is a simple optimization.  The built-in swap has special cases
for aligned 4- and 8-byte objects.  But those are almost never used;
most calls to sort() work on larger structures, which fall back to the
byte-at-a-time loop.  This generalizes them to aligned *multiples* of 4
and 8 bytes.  (If nothing else, it saves an awful lot of energy by not
thrashing the store buffers as much.)

Patch #2 grabs a juicy piece of low-hanging fruit.  I agree that nice
simple solid heapsort is preferable to more complex algorithms (sorry,
Andrey), but it's possible to implement heapsort with far fewer
comparisons (50% asymptotically, 25-40% reduction for realistic sizes)
than the way it's been done up to now.  And with some care, the code
ends up smaller, as well.  This is the "big win" patch.

Patch #3 adds the same sort of indirect call bypass that has been added
to the net code of late.  The great majority of the callers use the
builtin swap functions, so replace the indirect call to sort_func with a
(highly preditable) series of if() statements.  Rather surprisingly,
this decreased code size, as the swap functions were inlined and their
prologue & epilogue code eliminated.

lib/list_sort.c is a bit trickier, as merge sort is already close to
optimal, and we don't want to introduce triumphs of theory over
practicality like the Ford-Johnson merge-insertion sort.

Patch #4, without changing the algorithm, chops 32% off the code size
and removes the part[MAX_LIST_LENGTH+1] pointer array (and the
corresponding upper limit on efficiently sortable input size).

Patch #5 improves the algorithm.  The previous code is already optimal
for power-of-two (or slightly smaller) size inputs, but when the input
size is just over a power of 2, there's a very unbalanced final merge.

There are, in the literature, several algorithms which solve this, but
they all depend on the "breadth-first" merge order which was replaced by
commit 835cc0c8477f with a more cache-friendly "depth-first" order.
Some hard thinking came up with a depth-first algorithm which defers
merges as little as possible while avoiding bad merges.  This saves
0.2*n compares, averaged over all sizes.

The code size increase is minimal (64 bytes on x86-64, reducing the net
savings to 26%), but the comments expanded significantly to document the
clever algorithm.

TESTING NOTES: I have some ugly user-space benchmarking code which I
used for testing before moving this code into the kernel.  Shout if you
want a copy.

I'm running this code right now, with CONFIG_TEST_SORT and
CONFIG_TEST_LIST_SORT, but I confess I haven't rebooted since the last
round of minor edits to quell checkpatch.  I figure there will be at
least one round of comments and final testing.

This patch (of 5):

Rather than having special-case swap functions for 4- and 8-byte
objects, special-case aligned multiples of 4 or 8 bytes.  This speeds up
most users of sort() by avoiding fallback to the byte copy loop.

Despite what ca96ab859ab4 ("lib/sort: Add 64 bit swap function") claims,
very few users of sort() sort pointers (or pointer-sized objects); most
sort structures containing at least two words.  (E.g.
drivers/acpi/fan.c:acpi_fan_get_fps() sorts an array of 40-byte struct
acpi_fan_fps.)

The functions also got renamed to reflect the fact that they support
multiple words.  In the great tradition of bikeshedding, the names were
by far the most contentious issue during review of this patch series.

x86-64 code size 872 -> 886 bytes (+14)

With feedback from Andy Shevchenko, Rasmus Villemoes and Geert
Uytterhoeven.

Link: http://lkml.kernel.org/r/f24f932df3a7fa1973c1084154f1cea596bcf341.1552704200.git.lkml@sdf.org
Signed-off-by: George Spelvin <lkml@sdf.org>
Acked-by: Andrey Abramov <st5pub@yandex.ru>
Acked-by: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Reviewed-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Cc: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Cc: Geert Uytterhoeven <geert@linux-m68k.org>
Cc: Daniel Wagner <daniel.wagner@siemens.com>
Cc: Don Mullis <don.mullis@gmail.com>
Cc: Dave Chinner <dchinner@redhat.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [Iamgoofball/-tg-station](https://github.com/Iamgoofball/-tg-station)@[cbb4a1f521...](https://github.com/Iamgoofball/-tg-station/commit/cbb4a1f521edfa7aa95028c1d97458d4521bfd53)
#### Monday 2022-02-21 08:58:05 by Iamgoofball

Sentient Diseases no longer INSTANTLY FUCKING DIE if someone with a different disease walks on the same screen as you right after you pick your host and spawn. Fuck virology code, holy shit.

I hope whoever thought this was a good idea never gets a job in the games industry.

---
## [MDP43140/BaDomain](https://github.com/MDP43140/BaDomain)@[da31703ef5...](https://github.com/MDP43140/BaDomain/commit/da31703ef577be819d7220d7c0c2efb0ec20e19e)
#### Monday 2022-02-21 09:01:19 by MDP43140

added more bad domains

Thanks ThioJoe for the domain list
Added these bad domains:
demo.mipunet.cn
mipunet.cn
hichina.com
dns9.hichina.com
hostmaster.hichina.com
247extratech.com
247hacks.net
aisuru.tokyo
asianteen.space
astratech.pro
baby-girls.my.id
beautygirls.online
beautyzone.cam
beautyzone.com
bestdate.top
bigasschubby.com
bigbooty.online
bunnygirlss.site
buxadder.club
cashend.me
centre.baby
datting.link
datting.online
derk.bar
dhisex.uno
dollarbrite.com
dosgen.monster
easymakesolution.com
everyday.cf
exploitbyte.net
eyeonsight.net
fafa.bar
fluxmud.quest
forepl4y.com
funnymuvie.online
gametool10.ml
germs-love.store
hhhh.uno
houseof-lust.xyz
localdate.monster
netpayjob.com
newdebut-av.monster
nmnm.lol
orxhacks.com
owap.bar
ozap.bar
podrbx.best
qotu.bar
rbxr.monster
rbxton.online
robyoc.online
romanhackers.com
sex69.uno
sexxdating.site
shake-body.com
smarthackerstech.org
snapgirls.date
snapgirls.today
snapgirls.uno
specialdate.my.id
technopawns.com
thespacehackers.com
toprbx.best
trojanarticle.com
tubesex.uno
universehackworld.org
wedn.best
xbritclone.net

---
## [mawrick26/SM8250](https://github.com/mawrick26/SM8250)@[0a41a0c700...](https://github.com/mawrick26/SM8250/commit/0a41a0c7004e111a2a9bbb0921918a72860eb24b)
#### Monday 2022-02-21 09:14:33 by George Spelvin

lib/list_sort: optimize number of calls to comparison function

CONFIG_RETPOLINE has severely degraded indirect function call
performance, so it's worth putting some effort into reducing the number
of times cmp() is called.

This patch avoids badly unbalanced merges on unlucky input sizes.  It
slightly increases the code size, but saves an average of 0.2*n calls to
cmp().

x86-64 code size 739 -> 803 bytes (+64)

Unfortunately, there's not a lot of low-hanging fruit in a merge sort;
it already performs only n*log2(n) - K*n + O(1) compares.  The leading
coefficient is already at the theoretical limit (log2(n!) corresponds to
K=1.4427), so we're fighting over the linear term, and the best
mergesort can do is K=1.2645, achieved when n is a power of 2.

The differences between mergesort variants appear when n is *not* a
power of 2; K is a function of the fractional part of log2(n).  Top-down
mergesort does best of all, achieving a minimum K=1.2408, and an average
(over all sizes) K=1.248.  However, that requires knowing the number of
entries to be sorted ahead of time, and making a full pass over the
input to count it conflicts with a second performance goal, which is
cache blocking.

Obviously, we have to read the entire list into L1 cache at some point,
and performance is best if it fits.  But if it doesn't fit, each full
pass over the input causes a cache miss per element, which is
undesirable.

While textbooks explain bottom-up mergesort as a succession of merging
passes, practical implementations do merging in depth-first order: as
soon as two lists of the same size are available, they are merged.  This
allows as many merge passes as possible to fit into L1; only the final
few merges force cache misses.

This cache-friendly depth-first merge order depends on us merging the
beginning of the input as much as possible before we've even seen the
end of the input (and thus know its size).

The simple eager merge pattern causes bad performance when n is just
over a power of 2.  If n=1028, the final merge is between 1024- and
4-element lists, which is wasteful of comparisons.  (This is actually
worse on average than n=1025, because a 1204:1 merge will, on average,
end after 512 compares, while 1024:4 will walk 4/5 of the list.)

Because of this, bottom-up mergesort achieves K < 0.5 for such sizes,
and has an average (over all sizes) K of around 1.  (My experiments show
K=1.01, while theory predicts K=0.965.)

There are "worst-case optimal" variants of bottom-up mergesort which
avoid this bad performance, but the algorithms given in the literature,
such as queue-mergesort and boustrodephonic mergesort, depend on the
breadth-first multi-pass structure that we are trying to avoid.

This implementation is as eager as possible while ensuring that all
merge passes are at worst 1:2 unbalanced.  This achieves the same
average K=1.207 as queue-mergesort, which is 0.2*n better then
bottom-up, and only 0.04*n behind top-down mergesort.

Specifically, defers merging two lists of size 2^k until it is known
that there are 2^k additional inputs following.  This ensures that the
final uneven merges triggered by reaching the end of the input will be
at worst 2:1.  This will avoid cache misses as long as 3*2^k elements
fit into the cache.

(I confess to being more than a little bit proud of how clean this code
turned out.  It took a lot of thinking, but the resultant inner loop is
very simple and efficient.)

Refs:
  Bottom-up Mergesort: A Detailed Analysis
  Wolfgang Panny, Helmut Prodinger
  Algorithmica 14(4):340--354, October 1995
  https://doi.org/10.1007/BF01294131
  https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.6.5260

  The cost distribution of queue-mergesort, optimal mergesorts, and
  power-of-two rules
  Wei-Mei Chen, Hsien-Kuei Hwang, Gen-Huey Chen
  Journal of Algorithms 30(2); Pages 423--448, February 1999
  https://doi.org/10.1006/jagm.1998.0986
  https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.4.5380

  Queue-Mergesort
  Mordecai J. Golin, Robert Sedgewick
  Information Processing Letters, 48(5):253--259, 10 December 1993
  https://doi.org/10.1016/0020-0190(93)90088-q
  https://sci-hub.tw/10.1016/0020-0190(93)90088-Q

Feedback from Rasmus Villemoes <linux@rasmusvillemoes.dk>.

Link: http://lkml.kernel.org/r/fd560853cc4dca0d0f02184ffa888b4c1be89abc.1552704200.git.lkml@sdf.org
Signed-off-by: George Spelvin <lkml@sdf.org>
Acked-by: Andrey Abramov <st5pub@yandex.ru>
Acked-by: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Reviewed-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Cc: Daniel Wagner <daniel.wagner@siemens.com>
Cc: Dave Chinner <dchinner@redhat.com>
Cc: Don Mullis <don.mullis@gmail.com>
Cc: Geert Uytterhoeven <geert@linux-m68k.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[6bdffe3723...](https://github.com/odoo-dev/odoo/commit/6bdffe372350f8b9d1b5d480b57a0449ecfd2508)
#### Monday 2022-02-21 11:20:17 by Julien Castiaux

[REF] core: HTTPocalypse (9) ORM initialization

This commit is the 9th commit of a comprehensive refactor of our HTTP
framework. See odoo/odoo#78857 for complete historic, discussions and
rationnals.

When the "new" ORM API was implemented back in 2013, the HTTP was not
entirely ported to the new API. The authors of the new ORM API confessed
that they just "made it works" without much care for the HTTP API. A
decade later it is clear that the "lazy" approach prooved difficult
to reason about where and when the various ORM objects (cursor registry,
environment, context, user id) are set and modified.

Thanks to the HTTPocalypse, creation and modifications of those ORM
objects are now greedy, when one attempts to change the context, the
environment is greedely re-created using the modified context. The
previous approach was to wait until we re-use the environment to
re-create it.

The various ORM object properties setter have been removed and replaced
by `request.update_env` and `request.update_context`. The various ORM
object properties getter have not been modified and still act as alias
to the request environment.

The `check` function of `odoo.service.model` was kinda old, kinda
bloated with a kinda bad signature. The function have been renamed and
refactored. Because the function was a decorator, the visual clue
"this function is serialization-error safe" was at the function
definition. Actually it is the caller that needs the visual clue "I want
to protect this function call". The `check` function is no more a
decorator, it is a `asyncio.call_soon`-like function, passing arguments
is possible via `functools.partial`.

PR: odoo#78857
Task: 2571224

---
## [Kneba/android_kernel_asus_sdm660](https://github.com/Kneba/android_kernel_asus_sdm660)@[870077d7dd...](https://github.com/Kneba/android_kernel_asus_sdm660/commit/870077d7dd82185e1d7a28e0d3132b134521ffc8)
#### Monday 2022-02-21 12:54:58 by Dave Chiluk

sched/fair: Fix low cpu usage with high throttling by removing expiration of cpu-local slices

commit de53fd7aedb100f03e5d2231cfce0e4993282425 upstream.

It has been observed, that highly-threaded, non-cpu-bound applications
running under cpu.cfs_quota_us constraints can hit a high percentage of
periods throttled while simultaneously not consuming the allocated
amount of quota. This use case is typical of user-interactive non-cpu
bound applications, such as those running in kubernetes or mesos when
run on multiple cpu cores.

This has been root caused to cpu-local run queue being allocated per cpu
bandwidth slices, and then not fully using that slice within the period.
At which point the slice and quota expires. This expiration of unused
slice results in applications not being able to utilize the quota for
which they are allocated.

The non-expiration of per-cpu slices was recently fixed by
'commit 512ac999d275 ("sched/fair: Fix bandwidth timer clock drift
condition")'. Prior to that it appears that this had been broken since
at least 'commit 51f2176d74ac ("sched/fair: Fix unlocked reads of some
cfs_b->quota/period")' which was introduced in v3.16-rc1 in 2014. That
added the following conditional which resulted in slices never being
expired.

if (cfs_rq->runtime_expires != cfs_b->runtime_expires) {
	/* extend local deadline, drift is bounded above by 2 ticks */
	cfs_rq->runtime_expires += TICK_NSEC;

Because this was broken for nearly 5 years, and has recently been fixed
and is now being noticed by many users running kubernetes
(https://github.com/kubernetes/kubernetes/issues/67577) it is my opinion
that the mechanisms around expiring runtime should be removed
altogether.

This allows quota already allocated to per-cpu run-queues to live longer
than the period boundary. This allows threads on runqueues that do not
use much CPU to continue to use their remaining slice over a longer
period of time than cpu.cfs_period_us. However, this helps prevent the
above condition of hitting throttling while also not fully utilizing
your cpu quota.

This theoretically allows a machine to use slightly more than its
allotted quota in some periods. This overflow would be bounded by the
remaining quota left on each per-cpu runqueueu. This is typically no
more than min_cfs_rq_runtime=1ms per cpu. For CPU bound tasks this will
change nothing, as they should theoretically fully utilize all of their
quota in each period. For user-interactive tasks as described above this
provides a much better user/application experience as their cpu
utilization will more closely match the amount they requested when they
hit throttling. This means that cpu limits no longer strictly apply per
period for non-cpu bound applications, but that they are still accurate
over longer timeframes.

This greatly improves performance of high-thread-count, non-cpu bound
applications with low cfs_quota_us allocation on high-core-count
machines. In the case of an artificial testcase (10ms/100ms of quota on
80 CPU machine), this commit resulted in almost 30x performance
improvement, while still maintaining correct cpu quota restrictions.
That testcase is available at https://github.com/indeedeng/fibtest.

Fixes: 512ac999d275 ("sched/fair: Fix bandwidth timer clock drift condition")
Signed-off-by: Dave Chiluk <chiluk+linux@indeed.com>
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Reviewed-by: Phil Auld <pauld@redhat.com>
Reviewed-by: Ben Segall <bsegall@google.com>
Cc: Ingo Molnar <mingo@redhat.com>
Cc: John Hammond <jhammond@indeed.com>
Cc: Jonathan Corbet <corbet@lwn.net>
Cc: Kyle Anderson <kwa@yelp.com>
Cc: Gabriel Munos <gmunoz@netflix.com>
Cc: Peter Oskolkov <posk@posk.io>
Cc: Cong Wang <xiyou.wangcong@gmail.com>
Cc: Brendan Gregg <bgregg@netflix.com>
Link: https://lkml.kernel.org/r/1563900266-19734-2-git-send-email-chiluk+linux@indeed.com
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Signed-off-by: Ratoriku <a1063021545@gmail.com>
Signed-off-by: Peppe289 <gsperanza204@gmail.com>
Signed-off-by: RyuujiX <saputradenny712@gmail.com>
Signed-off-by: Kneba <abenkenary3@gmail.com>

---
## [gtr/cockroach](https://github.com/gtr/cockroach)@[255c1fb027...](https://github.com/gtr/cockroach/commit/255c1fb02708f99fef62b0af719af5e0984d9de3)
#### Monday 2022-02-21 14:59:53 by craig[bot]

Merge #71542 #73319 #74077 #76401 #76748

71542: backupccl: Support RESTORE SYSTEM USERS from a backup r=gh-casper a=gh-casper

Support a new variant of RESTORE that recreates system users that don't exist in current cluster from a backup that contains system.users and also grant roles for these users. Example invocation: RESTORE SYSTEM USERS FROM 'nodelocal://foo/1';

Similar with full cluster restore, we firstly restore a temp system database which contains system.users and system.role_members into the restoring cluster and insert users and roles into the current system table from the temp system table.

Fixes: #45358

Release note (sql change): A special flavor of RESTORE, RESTORE SYSTEM USERS FROM ..., is added to support restoring system users from a backup. When executed, the statement recreates those users which are in a backup of system.users but do not currently exist (ignoring those who do) and re-grant roles for users if the backup contains system.role_members.

73319: jobs: Execute scheduled jobs on a single node in the cluster. r=miretskiy a=miretskiy

Execute scheduled jobs daemon on a single node -- namely, the lease
holder for meta1 range lease holder.

Prior to this change, scheduling daemon was running on each node,
polling scheduled jobs table periodically with a `FOR UPDATE` clause.
Unfortunately, job planning phase (namely, the backup planning phase) could
take significant amount of time.  In such situation, the entirety
of the scheduled jobs table would be locked, resulting in inability
to introspect the state of schedules (or jobs) via `SHOW SCHEDULES` or similar
statements.

Furthermore, dropping `FOR UPDATE` clause by itself is not ideal because
that would lead to expensive backup planning being executed on almost every
node, with all but 1 node making progress.

The single node mode is disabled by default, but can be enabled
via a `jobs.scheduler.single_node_scheduler.enabled` setting.

Release Notes: scheduled jobs scheduler now runs on a single node by default
in order to reduce contention on scheduled jobs table.

74077: kvserver: lease transfer in JOINT configuration r=shralex a=shralex

Previously:
1. Removing a leaseholder was not allowed.
2. A VOTER_INCOMING node wasn't able to accept the lease.

Because of (1), users needed to transfer the lease before removing
the leaseholder. Because of (2), when relocating a range from the
leaseholder A to a new node B, there was no possibility to transfer
the lease to B before it was fully added as VOTER. Adding it as a
voter, however, could degrade fault tolerance. For example, if A
and B are in region R1, C in region R2 and D in R3, and we had
(A, C, D), and now adding B to the cluster to replace A results in
the intermediate configuration (A, B, C, D) the failure of R1 would
make the cluster unavailable since no quorum can be established.
Since B can't be added before A is removed, the system would
transfer the lease out to C, remove A and add B, and then transfer
the lease again to B. This resulted a temporary migration of leases
out of their preferred region, imbalance of lease count and degraded
performance.

The PR fixes this, by (1) allowing removing the leaseholder, and
transferring the lease right before we exit the JOINT config. And (2),
allowing a VOTER_INCOMING to accept the lease.

Release note (performance improvement): Fixes a limitation which meant 
that, upon adding a new node to the cluster, lease counts among existing
nodes could diverge until the new node was fully upreplicated.

Here are a few experiments that demonstrate the benefit of the feature.
1. 
> roachprod create local -n 4 // if not already created and staged
> roachprod put local cockroach
> roachprod start local:1-3 --racks=3 // add 3 servers in 3 different racks
> cockroach workload init kv --splits=10000
> roachprod start local:4 --racks=3 // add a 4th server in one of the racks

Without the change (master):
<img width="978" alt="Screen Shot 2022-02-09 at 8 35 35 AM" src="https://user-images.githubusercontent.com/6037719/153458966-609dbb7e-ca3d-4db6-9cfb-adc228f2bdf2.png">

With the change:
<img width="986" alt="Screen Shot 2022-02-08 at 8 46 41 PM" src="https://user-images.githubusercontent.com/6037719/153459366-2d4e2def-37cf-405b-b601-8be57419ae02.png">

We can see that without the patch the number of leases on server 0 (black line) goes all the way to 0 before it goes back up and that the number of leases in other racks goes up, both undesirable. With the patch both things are no longer happening.

2. Same as 1, but with a leaseholder preference of rack 0:

ALTER RANGE default CONFIGURE ZONE USING lease_preferences='[[+rack=0]]';

Without the change (master):
<img width="966" alt="Screen Shot 2022-02-09 at 10 45 27 PM" src="https://user-images.githubusercontent.com/6037719/153460753-bce048f0-f6da-4e21-afdc-317620c035b2.png">

With the change:
<img width="983" alt="leaseholder preferences - with change" src="https://user-images.githubusercontent.com/6037719/153460780-55795866-cf47-404d-b77a-45d9e011f972.png">

We can see that without the change the number of leaseholders in racks 1 and 2 together (not in preferred region) grows from 300 to 1000, then goes back to 40. With the fix it doesn’t grow at all.






76401: pgwire: add server.max_connections public cluster setting r=rafiss a=ecwall

This setting specifies a maximum number of connections that a server can have open at any given time.
<0 - Connections are unlimited (existing behavior)
=0 - Connections are disabled
>0 - Connections are limited
If a new non-superuser connection would exceed this limit, the same error message is
returned as postgres: "sorry, too many connections" with the 53300 error code
that corresponds to "too many connections".

Release note (ops change): An off-by-default server.max_connections cluster
setting has been added to limit the maximum number of connections to a server.

76748: sql: add missing specs to plan diagrams r=rharding6373 a=rharding6373

This change allows missing specs (e.g., RestoreDataSpec and
SplitAndScatterSpec) to be shown in plan diagrams. Before this change a
plan involving these types would result in an error generating the
diagrams. Also added a test to make sure future specs implement the
`diagramCellType` interface, which is required to generate diagrams.

Release note: None


Co-authored-by: Casper <casper@cockroachlabs.com>
Co-authored-by: Yevgeniy Miretskiy <yevgeniy@cockroachlabs.com>
Co-authored-by: shralex <shralex@gmail.com>
Co-authored-by: Evan Wall <wall@cockroachlabs.com>
Co-authored-by: rharding6373 <rharding6373@users.noreply.github.com>

---
## [AvanaPY/DV1629_Labb3](https://github.com/AvanaPY/DV1629_Labb3)@[506163d461...](https://github.com/AvanaPY/DV1629_Labb3/commit/506163d4612b4e8c6713f89494fdb5d9f6661d85)
#### Monday 2022-02-21 15:39:27 by Emil Karlström

fuck you håkan I will remember this until my next life where I will hunt
you down and tell the tale of the horrible operativsystem föreläsaren
med interna kommunikationsproblem med labbhanteraren som sa att vi fick
godkänt men sedan kommer du o säger nej, fy. Usch.

---
## [EladNLG/NorthstarLauncher](https://github.com/EladNLG/NorthstarLauncher)@[db0af63704...](https://github.com/EladNLG/NorthstarLauncher/commit/db0af63704a6fbc57e80a9db01bbc01b79339d9f)
#### Monday 2022-02-21 15:54:22 by Emma Miler

Added code for chathooks

This may not seem like much to a passing observer, but this commit took me 30 hours of blood, sweat, tears, IDA debugging, server crashes, and insanity.

---
## [deathandmayhem/jolly-roger](https://github.com/deathandmayhem/jolly-roger)@[c3ffbee79c...](https://github.com/deathandmayhem/jolly-roger/commit/c3ffbee79cc53ea2eb184a8f99c76e0cc4ffa4af)
#### Monday 2022-02-21 16:06:47 by Evan Broder

Improve fixture hunt data

This replaces the old fixture data from the 2015 hunt with a new set of
fixtures from the 2018 hunt. This improves on the old fixtures in a few
notable ways:

- The hunt is no longer complete. Our old fixture data had the hunt
  after all puzzles had been solved. The new fixture data is about
  halfway through the hunt (the team in our fixtures has fully solved
  the Emotions round, unlocked Hacking Island and Games Island but not
  completely solved either). We also now include guesses. The old
  fixtures didn't create guess objects, meaning that the guess queue
  didn't work as expected.
- The hunt has interesting structural components. The 2015 hunt was a
  great hunt, but mostly flat structurally. Thus it provides a
  suboptimal example of Jolly Roger's more sophisticated organization
  schemes. 2018 had much more going on structurally (including
  overlapping metas and multi-level round structure)

In order to make the experience more pleasant, if you are an admin and
there are no hunts, we add a button to the hunt list page to create the
fixtures (instead of needing to invoke the Meteor API method manually
from the JS console).

---
## [ltratt/yk](https://github.com/ltratt/yk)@[2991db3271...](https://github.com/ltratt/yk/commit/2991db327147d55a16efc9b2347a09d62f87f881)
#### Monday 2022-02-21 16:09:02 by Laurence Tratt

Remove that which haunted my dreams.

Finally we can get rid of the awful "we can't return from a closure used
to access a thread local" hack introduced in e953b799d!

---
## [avar/git](https://github.com/avar/git)@[be7bf32991...](https://github.com/avar/git/commit/be7bf329914b710089b53764e7c8636cbe22bf79)
#### Monday 2022-02-21 16:24:00 by Ævar Arnfjörð Bjarmason

usage API: use C99 macros for {usage,usagef,die,error,warning,die}*()

Change the "usage" family of functions to be defined in terms of C99
variadic macros, as we've optionally done with the BUG() macro and
BUG_fl() function since d8193743e08 (usage.c: add BUG() function,
2017-05-12), and unconditionally since 765dc168882 (git-compat-util:
always enable variadic macros, 2021-01-28).

This would have been possible before having a hard dependency on C99,
but as the dual implementations of C99 and pre-C99 macros and
functions adjusted in preceding commits show, doing so would have been
rather painful.

By having these be macros we'll now log meaningful "file" and "line"
entries in trace2 events. Before this we'd log "usage.c" in all of
them, and the line would be the relevant locations in that file.

To do this we need to not only introduce X_fl() functions for
{die,error,warning,die}{,_errno}(), but also change all the callers of
the set_*() and get_() functions in usage.h to take "file" and "line"
arguments.

Neither the built-in {die,error,warning,die}{,_errno}() nor anyone
else does anything useful with these "file" and "line" arguments for
now, but it means we can define all our macros and functions
consistently.

It also opens the door for a follow-up change where these functions
could optionally emit the file name and line number, e.g. for
DEVELOPER=1 builds, or depending on configuration.

It might be a good change to remove the "fmt" key from the "error"
events as a follow-up change. As these few examples from running the
test suite show it's sometimes redundant (same as the "msg"), rather
useless (just a "%s"), or something we could now mostly aggregate by
file/line instead of the normalized printf format:

      1 file":"builtin/gc.c","line":1391,"msg":"'bogus' is not a valid task","fmt":"'%s' is not a valid task"}
      1 file":"builtin/for-each-ref.c","line":89,"msg":"format: %(then) atom used more than once","fmt":"%s"}
      1 file":"builtin/fast-import.c","line":411,"msg":"Garbage after mark: N :202 :302x","fmt":"Garbage after mark: %s"}

"Mostly" here assumes that it would be OK if the aggregation changed
between git versions, which may be what all users of trace2 want. The
change that introduced the "fmt" code was ee4512ed481 (trace2: create
new combined trace facility, 2019-02-22), and the documentation change
was e544221d97a (trace2: Documentation/technical/api-trace2.txt,
2019-02-22).

Both are rather vague on what problem "fmt" solved exactly, aside from
the obvious one of it being impossible to do meaningful aggregations
due to the "file" and "line" being the same everywhere, which isn't
the case now.

In any case, let's leave "fmt" be for now, the above summary was given
in case it's interesting to remove it in the future, e.g. to save
space in trace2 payloads.

The change here in git_die_config() is the bare minimum needed to get
it working, but better would be a change[1] to correctly report the
caller file and line numbers. Let's leave that for later, it can be
done later.

1. https://lore.kernel.org/git/patch-4.4-e0e6427cbd3-20211206T165221Z-avarab@gmail.com/#t

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [avar/git](https://github.com/avar/git)@[93e768e14c...](https://github.com/avar/git/commit/93e768e14c1af7bf6706b834fbb5f310956c6863)
#### Monday 2022-02-21 16:24:10 by Ævar Arnfjörð Bjarmason

usage API: make the "{usage,fatal,error,warning,BUG}: " translatable

In preceding commits the vreportf() function was made static, so we
know it's only being called with a limited set of fixed prefixes. Pass
an enum indicating the kind of usage message we're emitting instead,
which means that we can fold the BUG_vfl_common() functionality
directly into it.

Since we've now got one place were we're emitting these usage messages
we can make them translatable.

We need to be careful with this function to not malloc() anything, as
a failure in say a use of strbuf_vaddf() would call xmalloc(), which
would in turn call die(), but here we're using static strings, either
from libintl or not.

I was on the fence about making the "BUG: " message translatable, but
let's do it for consistency. Someone who doesn't speak a word of
English may not know what "BUG" means, but if it's translated they
might have an easier time knowing that they have to report a bug
upstream. Since we'll always emit the line number it's unlikely that
we're going to be confused by such a report.

As we've moved the BUG_vfl_common() code into vsnprintf() we can do
away with one of the two checks for buffer sizes added in
116d1fa6c69 (vreportf(): avoid relying on stdio buffering, 2019-10-30)
and ac4896f007a (fmt_with_err: add a comment that truncation is OK,
2018-05-18).

I.e. we're being overly paranoid if we define the fixed-size "prefix"
and "msg" buffers, are OK with the former being truncated, and then
effectively check if our 256-byte buffer is larger than our 4096-byte
buffer. I wondered about adding a:

    assert(sizeof(prefix) < sizeof(msg)); /* overly paranoid much? */

But I think that would be overdoing it. Anyone modifying this function
will keep these two buffer sizes in mind, so let's just remove one of
the checks instead.

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [avar/git](https://github.com/avar/git)@[c8a5d35e93...](https://github.com/avar/git/commit/c8a5d35e93d68ea3b4c7548202f6979639584e35)
#### Monday 2022-02-21 16:24:18 by Ævar Arnfjörð Bjarmason

usage API: add "core.usageAddSource" config to add <file>:<line>

Optionally extend the support that BUG() has had for emitting line
numbers to the {usage,fatal,error,warning}{,_errno}() functions.

Before we'd unconditionally get error messages like:

    $ git -c core.x=y config --get --bool core.x
    fatal: bad boolean config value 'y' for 'core.x'

Which can be changed with core.usageAddSource=true to include the file
and line numbers:

    $ git -c core.usageAddSource=true -c core.x=y config --get --bool core.x
    fatal: config.c:1241: bad boolean config value 'y' for 'core.x'

As the added documentation notes this is primarily intended to be
useful to developers of git itself, but is being exposed as a user
setting to e.g. help file better bug reports.

This also adds a "GIT_TEST_USAGE_ADD_SOURCE" setting intended to run
the test suite in this mode.

Currently it has a lot of failures. Most of those are rather trivial,
and can be "fixed" by pointing GIT_TEST_CMP to a "diff -u" that does a
s/^(usage|fatal|error|warning): [^:]+:[0-9]+/$1/g on its input files,
and likewise for a "grep" wrapper that does the same.

Even if we can't run the tests in this mode yet I'd like to have this
for ad-hoc debugging, and to make it easier to work towards running
the tests in this mode. If we can turn this on permanently it'll be
much easier to read test output, as we won't need to worry about the
indirection of looking up where an error might have been emitted,
which can be especially painful when the message being emitted isn't
unique within git.git.

This new code needs to be guarded by the "dying" variable for the
reasons explained in 2d3c02f5db6 (die(): stop hiding errors due to
overzealous recursion guard, 2017-06-21), and for those same reasons
it's racy under multi-threading.

Here the worst case is that incrementing the variable will run away
from us, and we won't get our desired <file>:<line> number. That's OK
in this case, those cases should be isolated to the config code (if we
can't parse the config), memory allocation etc, but we'll get it right
in the common cases.

Using GIT_TEST_USAGE_ADD_SOURCE should be immune from any racyness, as
it only needs a getenv() and git_parse_maybe_bool(), which won't die.

Add a repo_cfg_bool_env() wrapper to repo-settings.c for
GIT_TEST_USAGE_ADD_SOURCE, in 3050b6dfc75 (repo-settings.c: simplify
the setup, 2021-09-21) I indicated that the GIT_TEST_MULTI_PACK_INDEX
env variable/config pair in that file has odd semantics, but users of
repo_cfg_bool_env() have straightforward and expected semantics. If
the environment variable is set (true or false) we'll use it,
otherwise we'll use the config, and finally fall back on the
default (of "false", in this case).

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [cherscarlett/engineering-for-good](https://github.com/cherscarlett/engineering-for-good)@[5b9a174525...](https://github.com/cherscarlett/engineering-for-good/commit/5b9a1745255b7f855be62d1fba198a324fc38e28)
#### Monday 2022-02-21 16:49:31 by Emi Dunn-Rankin

Remove Khan Academy re workplace & values concerns

A lot of good work has happened at Khan Academy over the years, but Sal himself is unfortunately not an especially values-oriented leader, in my opinion.

We had to organize a strike in order to force him to allow any anti-racism education or action during the Black Lives Matter uprisings in 2019. We also demanded that he *not* invite a known racist politician onto his podcast during that time, to which he responded with a contemptuous email reminding us to keep an open mind and not silence people we happen to disagree with politically.

Staff and executives have been fleeing since, which means Sal is even more empowered to take unilateral action, like his recent NFT gambling game partnership that he advertised on the official school YouTube channels for children, and in a special CNBC interview. When former employees started raising concerns in the company's Slack channel for us, Sal personally banned all the people who did (except the white men), and eventually shut down the channel altogether.

I've also personally witnessed *many* instances of discrimination in the engineering department, and concerns are consistently met with career-ending retaliation. And it doesn't help that Sal in particular loves to surround himself with young starry-eyed industry newcomers, who are primed to believe whatever he and the company say. Practically all of my personal friends during my 5 years left the org confused and broken, taking years to recover 😖

Former employees have been talking about it more recently, here's a link summary thread from Caroline Charrow: https://twitter.com/CarolineCharrow/status/1492695969917407232

Good things have happened at Khan Academy, but I worry that's increasingly in the past; and I would strongly warn marginalized people not to trust management whatsoever. If it were me, I wouldn't include the company on a list of recommendations. Thank you for considering!

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[9ba17ad234...](https://github.com/mrakgr/The-Spiral-Language/commit/9ba17ad234ebea1fd46c087bb65ce5726956a29e)
#### Monday 2022-02-21 17:39:54 by Marko Grdinić

"11:25am. My sleep tonight has been bad. I must have been obsessing all night about my regrets. I really don't know what to do about them except make money. Money is ultimately the difference between an adult and a kid. A kid has nothing except what his parents give him. And that is exactly my situation currently. I need to make money. I can't keep scamming myself with ML. If it is really meant to be, maybe that social media post will give me a pull and I will be able to get my hands on the AI chips on schedule. Otherwise I'll have to proceed on my current path and hope it connects with the old one at some point.

11:30am. Well, let me chill and then I'll have breakfast.

12:30pm. I am having breakfast. I watched the 4th Solaris video and I had enough of that. The Solaris stuff is pretty much useless to me apart from allowing me to use Karma in the viewport. There is no reason for me to learn this, it is such a waste of time.

When it is time to start what I am going to do is get back to texturing. I need to do the pool water first.

2:05pm. I am back. Let me start.

Actually, before the pool water, I need to figure out how to load the textures into the MaterialX shader.

Before that, I want to work more on the pool UVs. I should separate the inner part from the rest properly, so it does not overlap...

No it does not matter. This is because it not visible. It is just my perfectionism talking.

Then, let me load the textures.

2:15pm. Huh, what was the Mtlx Principled Shader? Wasn't it Mtlx Surface? But that can't be it. Let me check out the video again.

https://youtu.be/tI4zqTezniI?t=452

It is standard surface.

2:25pm. I need to ask a question in the Houdini thread.

https://www.youtube.com/results?search_query=houdini+materialx

Also I should watch some of these tuts. I really have no idea how to load textures.

2:35pm. Asked. Focus me. Focus on loading the textures.

2:40pm. No, I can't figure it out. The nodes are simply not working. The roughness is not working for some reason either.

Why does the viewport not respond when I move the sliders?

2:45pm. Oh, it worked. What the hell, I only changed the contexts. This is Houdini being quite buggy.

What do I do about the rest of the textures? There is no way around it, let me watch the tutorials.

https://www.youtube.com/watch?v=FVmFFn7EPdA
Building Shaders With MaterialX in Solaris | Houdini

https://youtu.be/FVmFFn7EPdA?t=276

What is this Mtlx Image Albedo. He says the texture comes in here.

Yeah, it works.

And now the viewport is not reacting properly again.

Sigh. Also I can't see displacement on the Mtlx Surface.

Also I've completely forgotten what specular is supposed to be doing.

https://youtu.be/FVmFFn7EPdA?t=309

Here is something regarding displacement.

https://youtu.be/FVmFFn7EPdA?t=480

Let me pause this here. This is too advanced for me right now. I am not interested in how to build the principled shader from scratch.

https://youtu.be/QjDMZAJAeCs
Enabling Displacement in Material X and Karma | Houdini 19

Let me watch this first since it is only 5m.

https://youtu.be/QjDMZAJAeCs?t=153

There is a restart render option.

3:10pm. So far my impression that this is lower quality than Blender. Cycles is always responsive and does not require manual restarts.

https://www.youtube.com/watch?v=ABF7op2W8pM
Karma XPU and MaterialX | Adam Swaab | Houdini 19 HIVE

Let me watch this. I might end up dropping Houdini here after all.

3:30pm. Yeah, before I can progress, I need to figure out why stage is not importing normals. I really hate Houdini when it does things like this.

3:50pm. It turns out I forgot to add the normals to the object. But now that I've fixed that, I find that the UVs are messed up in Karma XPU.

Hmmm, it seems the UVs work fine with regular Karma.

4pm. https://youtu.be/ABF7op2W8pM?t=1675

Here the actual tutorial part starts.

Sigh, I wish I could be faster in figuring out how to get the rendered going. I really wanted to do the pool instead of fiddle with setting it up.

4:05pm. In Blender I want to try something out. I had the idea for it during the night and thought about it only now. Is there a select parent option?

Yep. You can access it with Shift + G. The brilliant thing about Blender is that it remembers the last use and positions the menu so the cursor comes under it. This UI design is a far cry from Houdini who always expects you to haul everything yourself.

4:25pm. I think I am fucked with Karma XPU.

Hmmmm...

Let me try changing things a bit. The overlapping UVs might be the problem.

4:45pm.

///

>>883907
>Is that object set to render as subdivision surfaces in /obj by any chance?
No. Maybe it has something to do with the way the object tree is structured. I have packed prims and another object that does not have UVs, but I do not want to start taking things apart to figure out what is wrong.

I think at this point I have two options:

* Do the lookdev in Houdini using the regular rendered and let the Karma CPU grind away at the finished scene for a while.
* Find a way to export the scene into Blender and do the lookdev there using Cycles.

Yesterday I watched the Entagma guys talking how easier it is to do the lookdev in Blender, and I am mostly interested in Houdini for generating procedural environments rather than doing simulations, so that kind of workflow might be a good fit for me. The reason I decided to try out Houdini is to generate those big vines.

What are my options for exporting given that I have the non-commercial license? The regular export options are grayed out, but I saw a video on exporting geometry into .obj using the File SOP. I've never tried it so I am not sure whether that would deal with packed instances correctly. There are about 20k of them in the scene and I do not want them to be put into a collection, let alone output as separate geometry.

///

Let me finish the tutorial. I'll just use the CPU renderer. I want to go into Blender, but that would lead to its own problems. I'll have to do the scene in Houdini. Using the raster renderer is good enough for my purpose.

4:50pm. I am trying to save the vines to file, and given how long it is taking most likely it is outputting everything.

Holy shit, where did it put the file?

I should have put `$HIP/` before the file name.

Now I have a 2gb obj file wasting space somewhere.

It is in the $JOB folder...Which is also my Users folder.

Deleted.

5:10pm. I am just wasting time here now. I do not need the tutorials, but raw grit instead.

It was a mistake doing this in Houdini after all. But I can finish the scene and have it look good regardless.

5:15pm. Hmmm, is the MaterialX shader not working with the raster rendered after all?

5:20pm. Forget the MaterialX shaders. I do not know why, but they stopped working with the regular view. I could have sworn it worked for me earlier.

This is just another aspect of Houdini's general shittiness at rendering.

I am going to have to use the Principal Shader. I guess Mtlx stuff is in alpha as well.

5:25pm. What the hell is going on here? Why did the base texture suddenly stop working.

5:35pm. I have no idea, I had to create a new shader.

6:40pm. I am starting to hear thunder let me close here early."

---
## [MeowcaTheoRange/FNF-PsychEngine](https://github.com/MeowcaTheoRange/FNF-PsychEngine)@[dfedd791ac...](https://github.com/MeowcaTheoRange/FNF-PsychEngine/commit/dfedd791ac86cc6bb264bc12da52454c4e884bb3)
#### Monday 2022-02-21 18:00:09 by ShadowMario

Merge pull request #756 from MeowcaTheoRange/patch-3

funny issue template shit that I'm Sure won't fuck up everything this time

---
## [MeowcaTheoRange/FNF-PsychEngine](https://github.com/MeowcaTheoRange/FNF-PsychEngine)@[ac3c9ef92e...](https://github.com/MeowcaTheoRange/FNF-PsychEngine/commit/ac3c9ef92ed1c32a2d5e1814e976a55fa89db74b)
#### Monday 2022-02-21 18:00:09 by ShadowMario

Merge pull request #704 from MeowcaTheoRange/patch-2

This was fucking hell I'm *so* sorry @ShadowMario

---
## [FleetAdmiralKraken/SticksAndStoneEDE](https://github.com/FleetAdmiralKraken/SticksAndStoneEDE)@[634cd6da22...](https://github.com/FleetAdmiralKraken/SticksAndStoneEDE/commit/634cd6da220cf60e6ec2832c27941e98947ba32f)
#### Monday 2022-02-21 18:49:14 by Alex Lopez

Fucked camera render textures off

Fuck that pissing dumb shit which doesn't work goddamnit

---
## [JohnKnee3/zookeepr](https://github.com/JohnKnee3/zookeepr)@[f530421036...](https://github.com/JohnKnee3/zookeepr/commit/f530421036858cfd1a0af4154957a30125dacb4e)
#### Monday 2022-02-21 19:48:42 by john.a.clark3

11.1.5

We first used a simple
app.get('/api/animals', (req, res) => {
  res.send('Hello!');
});
That sent Hello if our .get was talking to animals.json animals object.

Then we updated it
app.get('/api/animals', (req, res) => {
  res.json(animals);
});
To grab the entire animals array using .get instead of .send.

Then we used this

app.get('/api/animals', (req, res) => {
  let results = animals;
  console.log(req.query)
  res.json(results);
});
+
 http://localhost:3001/api/animals?name=Erica
To console log the name Erica.

Finally we updated the .get into it's final form
app.get('/api/animals', (req, res) => {
  let results = animals;
  if (req.query) {
    results = filterByQuery(req.query, results);
  }
  res.json(results);
});
to set it up to receive .querys that talk to the function filterbyQuery.

function filterByQuery(query, animalsArray) {
  let filteredResults = animalsArray;
  if (query.diet) {
    filteredResults = filteredResults.filter(animal => animal.diet === query.diet);
  }
  if (query.species) {
    filteredResults = filteredResults.filter(animal => animal.species === query.species);
  }
  if (query.name) {
    filteredResults = filteredResults.filter(animal => animal.name === query.name);
  }
  return filteredResults;
}
Which will look at what you type for example
http://localhost:3001/api/animals?name=Erica
grabs Erica's object
{
      "id": "2",
      "name": "Erica",
      "species": "gorilla",
      "diet": "omnivore",
      "personalityTraits": ["quirky", "rash"]
    },
and
http://localhost:3001/api/animals?species=gorilla
would grab
{
"id": "1",
"name": "Terry",
"species": "gorilla",
"diet": "omnivore",
"personalityTraits": [
"anxious",
"goofy"
]
},
{
"id": "2",
"name": "Erica",
"species": "gorilla",
"diet": "omnivore",
"personalityTraits": [
"quirky",
"rash"
]
}
We finally set up the personalityTraits query which is a bit more involved because it is an array.

function filterByQuery(query, animalsArray) {
  let personalityTraitsArray = [];
  // Note that we save the animalsArray as filteredResults here:
  let filteredResults = animalsArray;
  if (query.personalityTraits) {
    // Save personalityTraits as a dedicated array.
    // If personalityTraits is a string, place it into a new array and save.
    if (typeof query.personalityTraits === "string") {
      personalityTraitsArray = [query.personalityTraits];
    } else {
      personalityTraitsArray = query.personalityTraits;
    }
    // Loop through each trait in the personalityTraits array:
    personalityTraitsArray.forEach((trait) => {
      // Check the trait against each animal in the filteredResults array.
      // Remember, it is initially a copy of the animalsArray,
      // but here we're updating it for each trait in the .forEach() loop.
      // For each trait being targeted by the filter, the filteredResults
      // array will then contain only the entries that contain the trait,
      // so at the end we'll have an array of animals that have every one
      // of the traits when the .forEach() loop is finished.
      filteredResults = filteredResults.filter(
        (animal) => animal.personalityTraits.indexOf(trait) !== -1
      );
    });
  }
was added to the top and used the initial if statement to check if you one trait else you checked for multiple.  Then it assings it to the personality traits array let.  Then using for each it finds each query and grabs what is needed.

Very dense and may need to read again.

---
## [gedack/neonbee](https://github.com/gedack/neonbee)@[b578bace73...](https://github.com/gedack/neonbee/commit/b578bace738e82646da062b2723f61909da33b62)
#### Monday 2022-02-21 19:59:45 by Kristian Kraljic

feat: improve `Launcher`, `Deployable`, `EntityModelManager` and more

This change is huge... I am sorry, but here is a video of me explaining why the change got so huge [1]. Sorry? Good news tough: All changes have been made interface and thus downwards compatible to the old NeonBee version, thus no adaptions to existing functionality should become necessary. Let me go into detail what changed and which quality of life / boy scout rule improvements have been made:

- Many NeonBee methods had been introduced in a pre-Vert.x 4-era. Meaning they did not take advantage of the futurization process Vert.x went through. This change rewrites many methods and simplifies them by switching the futurized methods, instead of methods using handlers.

- Improved the NeonBee bootstrap by making it more asynchronous, by changing the structure of method calls throughout the boot process and wrapping blocking code in `AsyncHelper.executeBlocking` calls.

- Simplified implementation of the `Launcher` class. Instead of manually defining and parsing all options in the launcher to get to a `NeonBeeOption` instance, instead switching to Vert.x's annotation-based `CLIConfigurator` implementation. Annotations are now defined directly in the `NeonBeeOptions` and injected into the `NeonBeeOptions` instance by the `CLIConfigurator`. This makes it much simpler and less error prone to define options and makes it also clear: everything that is in `NeonBeeOptions` can be defined through the command-line or environment. For the latter a `EnvironmentAwareCommandLine` was introduced, that also considers the environment variables if no options are set as arguments, deprecating all "helper methods" that have been there for only this reason.

- Added a new `development_conventions.md` document, that elaborates many "hidden rules" that we came up over the years, when it comes to coding conventions, such as: naming conventions for NeonBee variables, whether to use an instance to `NeonBee` or to `Vertx`, where to place `Context` variables in method signatures and how to properly correlate log messages. Then, in this change, a couple of old methods have been cleaned up to fit this new guiding document.

- The old naming choice for the "/verticles" subfolder does no longer make sense, because not only verticles are deployed by the `DeployerVerticle`, but full "modules". Thus, introduced a new `getModulesDirectory` method to `NeonBeeOptions` and deprecated the old `getVerticlesDirectory`. Two `DeployerVerticle` will now take care to deploy the old and the new directory if necessary (present).

- Introduced a new --module-jar-paths option to NeonBee options, that allows to define paths to module JARs, that will get deployed during the bootstrap phase of NeonBee into own self-first class-loaders. Previously the only option to deploy modules was through NeonBees `DeployerVerticle`, that was watching the `verticles` sub-directory for changes. The new option grants to also deploy modules that are not physically in that folder.

- Split up `EntityModelManager` into its (previously embedded) sub-classes by introducing a package private `EntityModelLoader` class. Futurized many of its methods and improved the concept for registering "external models": Previously modules did register / unregister models to the `EntityModelManager` by using their module identifier as a unique key. The `EntityModelManager` kept a private map of these IDs (`BUFFERED_MODULE_MODELS`) mapping to a set of compiled `EntityModel` objects. Now the concept was changed by introducing a new `EntityModelDefinition` object, that can be used to influence compilation of models of the `EntityModelManager`. Whenever a `EntityModelDefinition` is added / removed from the `EntityModelManager` it will attempt to compile a new "global" set of models. This allows for inter-dependent models and sets up the `EntityModelManager` for an upcoming change to be completely remodeled in order to support versioned models going forward (see the roadmap). It also makes managing the "external models" more easy, because no longer we need to hold a map of identifiers, but only a `Set<EntityModelDefinition>` to be maintained by the `EntityModelManager`. This makes it useful not only to modules, but any object that needs to deal with model generation can now supply a `EntityModelDefinition`.

- Removed `NeonBeeModule` in favor of a new `DeployableModule`. The `Deployable` interface was thought to become a generic object. Everything that can be deployed to NeonBee should inherit `Deployable`. `NeonBeeModule` violated this pattern and implemented much the same logic. Now the whole `io.neonbee.internal.deploy` package is consistent again, by introducing a `DeployableModels` (that can deploy `EntityModelDefinition` object), `DeployableModule` (that parses JAR files and splits them up into `DeployableModels` and `DeployableVerticles`) and a generic `Deployables` class, that handles deployments of multiple `Deployable` objects. This makes the whole deployment much cleaner, as for NeonBee everything is now a `Deployable` and the logic, whether it is a module, or a verticle, or a model that is being deployed, is now completely hidden away inside of the respective `Deployable` implementation. After deployment, everything results in the same `Deployment` instance, that can be undeployed again in the same fashion.

- Quality of life improvements to `AsyncHelper` by introducing runnables, cosumers and suppliers that can throw an exception. This allowed to replace existing calls like `AsyncHelper.executeBlocking(vertx, () -> { try { ... } catch (e) { return failedFuture(e); } })` with `AsyncHelper.executeBlocking(vertx, () -> ...)`.

- Simplified `ClassPathScanner` and introduced a new `CloseableClassPathScanner` that closes the underlying `URLClassLoader` to stop leaking resources.

- Introduced a new `ThreadHelper` class, that can be used to retrieve the calling or own class, as well as the class-loader of the current thread.

- Made `NeonBeeProfile` behave the same as for `moduleJarPaths` when getting parsed, meaning that you can define multiple profiles separated by comma.

- Renamed CollectionsHelper to CollectionHelper, because it was the only helper with a plural name.

- Improve many tests (esp. Deployable ones) mainly by mocking more and spying less.

- Made `setEnvironment` and `withEnvironment` work on Windows, to be able to remove `@DisableOnOS` annotation for tests changing environment variables.

---
## [adambennett/StS-DuelistMod](https://github.com/adambennett/StS-DuelistMod)@[de37342c54...](https://github.com/adambennett/StS-DuelistMod/commit/de37342c54d887305c5a983254603a2f4b68b74a)
#### Monday 2022-02-21 20:22:38 by Adam Bennett

v3.481.18 (#31)

Bug Fixes
----------
- Fixed a major issue with certain relics/cards/powers disabling Duelist cards from being playable
- This fix should include improvements to the message that yugi will display when a card is unusable due to a DuelistMod trigger
- Fixed an issue with the way the Obliterate power worked
- Nimble Angler: fixed card not summoning
- Tribute to the Doomed: fixed card crashing when magic number is reduced below 1
- Cloning: fixed card crashing when magic number is reduced below 1
- Dark Paladin: fixed card crashing when magic number is reduced below 1
- Fairy Box: fixed card crashing when magic number is reduced below 1
- Phoenix Feather: fixed card crashing when magic number is reduced below 1
- Predapruning: fixed card crashing when magic number is reduced below 1
- Wiretap: fixed card crashing when magic number is reduced below 1
- Reinforce Truth: fixed power crashing the game
- Spirit Force: fixed power crashing the game
- Weapon Change: fixed power crashing the game
- Bombchain: prevent occasional game crash
- Spellheart (relic): prevented Soulbound cards from being removed
- Improvements to some Exodia deck issues surrounding other sources of card removal & adding
- MegaConfusion checks cards to ensure they have summons/tributes to modify before updating any of those values, preventing odd behavior
- Duelist Power (relic): now properly grants Vigor every other turn
- Power Kaishin: now actually uses magic number to apply Magicka
- Mayakashi Metronome: now will actually resummon cards
- Parasite Paracide: now tributes properly
- Call of Mummy: now will work correctly when played while using the Metronome Deck


Balance Updates
----------------
- Removed Fairy Bottle (potion)
- Light orb: completely changed the passive mechanic from increasing buff stacks -> random chance at increased max HP
- Witch of Black Rose: increased cost from 1 -> 2, upgrade now increases summons instead of base cost
- Armed Dragon Lv. 5: added upgrade to damage
- Egg Token (relic): reduced Monster Egg copies added to your deck from 3 -> 2
- MegaConfusion no longer will modify tributes on cards while playing below Challenge level 2
- Simplified the odds calculations for Raigeki and Crystal Raigeki stun effects, which should make them easier to modify using Solder effects
- Electricity now greatly improves the odds of Raigeki triggering the stun effect
- Lost World: now increases damage by 15%(25%) instead of 10%(10%)
- Jurassic Impact: slightly modified the percentages on the upgraded version
- Frostosaurus: reduced base cost from 2 -> 1, upgrade now switches to X+1 effect instead of lowering base cost
- Iris Earth Mother: reduced channeled orbs from 2 -> 1, upgrade no longer increases orbs channeled
- Magician's Rod: upgrade no longer deceases base cost, now improves magic number 2 instead of 1
- Sabersaurus: reduced base summons from 3 -> 1, upgrade no longer increaes damage or summons, upgrade now reduces base cost by 1
- Blizzard Warrior: increased damage from 8 -> 10
- Dark Horizon: increased tributes from 1 -> 2
- Dark Paladin: decreased damage from 24 -> 18, upgrade switched from reduced tributes to increased damage
- Doom Shaman: block from 11 -> 10, orbs channeled from 3 -> 2, orb strength from 6 -> 5, tributes from 3 -> 4, upgrade switched from block +5 -> orbs channeled +1
- Icy Crevasse: focus from 3 -> 2, max summon reduce from 3 -> 2, frost channeled from 2 -> 1
- Power Kaishin: magicka gain from 2 -> 4, upgrade increases magic number further by 1
- White Magical Hat: magicka gain from 3 -> 4, upgrade increases magic number futher by 1
- Several Mayakashi cards have lost their Exempt status to make the Mayakashi Metronome work correctly


QoL
----------
- Added a new config menu option to disable tier score buttons from opening the website when clicked
- Actions taked via the Haunted debuff are now logged into the dev console so you can view a history of the last few actions by pressing ~
- Nameless (relic): Added actual gameplay description to the nameless tomb relic


Art/FX
----------
- Updated and improved cart art and googly eyes for the following cards: Fossil Dragon, Fossil Knight, Fossil Skullbuggy, Fossil Skull Convoy, Fossil Skull King, Fossil Skull Knight
- Added relic art for the following relics: Point Pass, HP Box, Metronometry, Wirebundle
- Added power art for the following powers: Anti-Fusion Device, Bacon Saver, Berserk Scales, Berserking, Book of Moon, Book of Taiyou, Damp debuff, Dragon Mastery, Dragon Mirror, Ice Hand, Mako's Blessing, Silver Wing, Vampire Kingdom, White Horn Dragon 
- Updated power art for the following powers: Reinforce Truth, Sphere Kuriboh, Swords of Burning Light, Swords of Concealing Light, Swords of Revealing Light
- Updated endgame Duelist tower image


Metrics
----------
- Fixed a backend bug that was preventing tier scores from updating since 06/2021
- Tier scores have been updated again as of 2/21/22 and will continue to be monitored for daily updates

---
## [Sealed101/tgstation](https://github.com/Sealed101/tgstation)@[906fb0682b...](https://github.com/Sealed101/tgstation/commit/906fb0682bab6a0975b45036001c54f021f58ae7)
#### Monday 2022-02-21 20:25:44 by necromanceranne

Ballistic to Energy: Autorifles for Thermal Pistols; Adds .38 Crate to Cargo (#64280)

About The Pull Request
The design doc behind this PR, which is only mildy been deviated from on some of the end particulars. Cobby-Approved! Maintainer Discussed!
https://hackmd.io/@6DbtsAKCTtW_9MByKFjZqg/r1xYKCNOt

Cargo Changes
Cargo has had all WT-550's removed and replaced with Thermal Pistols.
Cargo can now order Thermal Pistols, a kind of energy/ballistic hybrid weapon shooting chunks of altered nanites into people. We couldn't use them in people, so maybe we'll use them as bullets! Magma/Ice bullets, to be exact.
You can, after paying a whopping 4K on a goodie pack (you have to pay from your own personal account) buy a .38 revolver. This is mostly to help some poor detective who lost their revolve in what I'm sure will be an inevitable scramble for ballistics. If even the 4K pricetag isn't enough, at least it requires detective access to open the pack...I hope.
Some of the crates that contained autorifle related items have been changed/removed.

unknown (2)

securarevolver 4 0

Science Changes
Ballistic Weaponry node no longer exists, and has been replaced with Exotic Ammo as both the pre-requisite to other nodes, as well as being able to be researched as soon as the Weaponry node is unlocked and not Advanced Weaponry.

Thermal Pistols
-Fairly average bullet statistics; 10 AP but shooting into Energy armor. 20 damage (Brute for cryo, Burn for inferno). Decent wounding potential, but individually much lower ammo counts than lasers.
-Bought in twinned pairs in a two gun holster (just for normal sized energy guns). They're normal sized.
-Each gun has 8 shots (thereabouts). 16 between two.
-Cryo pistols do a knockdown and extra damage against extremely hot targets. Inferno pistols do an explosion cantered on the target against extremely cold targets.
-The guns are EMP-proof.

Why It's Good For The Game
The current gameplay loop of crew combatants is them relying on backup and retreating as necessary to reload their weapons during fights. The ability to repeatedly harry opponents in the field reloads is something that should be moved away from for crew equipment, as it emphasizes lone wolf tactics and one-man army problems, with boxes full of spare ammo usually allowing any single combatant to outlast multiple foes. In addition, ballistics often are not subject to the same (interesting) limitations of energy weapons, so they're typically a no-brainer choice. We shouldn't have such an easy choice be readily available like that.

The thermal pistols present a more challenging weapon to use as a solo combatant but become far more versatile and potent when paired with a decent buddy and basic level co-ordination. They're not a straightforward choice for every situation, but instead are a weapon employed given the right circumstances for them to shine.

In addition to the gameplay issues that ballistics pose, we're in a goddamn spacegame. Unless the ballistics are noticeably weird (they're not), we should expect that our more advanced research station has some pretty odd guns of the energy variety.

Changelog
🆑 Necromanceranne, quin
add: Adds the Inferno and Cryo Pistols. A hybrid energy/ballistic weapon, to cargo. It can be purchased in either a goodies pack or a normal crate order.
add: Thermal Pistols do more damage and a special based on temperature of the target hit.
add: Inferno pistols cause an explosion when they hit a severely cold target.
add: Cryo pistols cause a knockdown and extra damage if they hit a severely hot target.
add: There is a special nanite pistol, which is admin spawned. Don't tell anyone about the forbidden ballistic energy gun.
add: You can order a .38 revolver as a goodie pack. It is expensive.
del: Removes WT-550's from cargo and related content from the techweb/protolathes.
balance: Exotic Ammo is now much earlier in the tech web to take the place of Ballistic Weaponry.
/🆑

---
## [chef/chef](https://github.com/chef/chef)@[9c615241b5...](https://github.com/chef/chef/commit/9c615241b52a3947549bc17ab85e256dc47be7ab)
#### Monday 2022-02-21 20:27:32 by Lamont Granquist

Disable knife gem install in kitchen tests

This causes horrible issues.

We are installing knife in a TK virt and can't really build it and
install it as a test (hacking up appbundler to do this would largely
invalidate the test since we wouldn't be testing customer behavior)
and as such it needs to be installed from rubygems.  That means
installing knife-17, which pulls down chef-17 which currently has
a dep on diff-lcs 1.3.x which conflicts with 1.5.x which throws
the errors around the binstubs conflicting (which may or may not be
a rubygems bug, I investigated that a bit and couldn't determine
why that is happening since the 3rd line has the magic rubygems
comment).  We can't just use "--force" as an option since that'll
ignore deps and stuff as well which is precisely the kinds of things
that we're trying to catch.  So for now this test is more pain
that it is worth.

Signed-off-by: Lamont Granquist <lamont@scriptkiddie.org>

---
## [lsloan/ccm](https://github.com/lsloan/ccm)@[07dbb37fd3...](https://github.com/lsloan/ccm/commit/07dbb37fd388eb930b18178b5cd8dbea0e304acb)
#### Monday 2022-02-21 21:19:46 by Mr. Lance E Sloan (lsloan)

#221 - more eslint god appeasement 🗿🗿🗿🗿🗿

eslint in MS' Visual Studio Code isn't that great.  It told me that the previous commit was all that needed to be fixed.  However, Codacy disagreed.  Upon opening each of the files that Codacy reported, only THEN did VSC's eslint say, "oh yeah… there's one problem in this file.  Umm…  Yup!  There's two files in that file, too.  You're good at this!  Maybe you don't need eslint in VSC at all, just keep checking Codacy's reports.  Can you go away and leave me alone now?  Thanks!"

---
## [TOLiving/code-busters](https://github.com/TOLiving/code-busters)@[ee43c7f4d5...](https://github.com/TOLiving/code-busters/commit/ee43c7f4d51161faa2366360d17252f673a5ec8d)
#### Monday 2022-02-21 22:30:50 by TOLiving

Updated version of v3. 1

I'm an idiot and I should honestly just stop coding but I won't because this is fun I'm just dumb holy crap

---

