## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-10-14](docs/good-messages/2022/2022-10-14.md)


2,191,974 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,191,974 were push events containing 3,237,834 commit messages that amount to 240,048,725 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 44 messages:


## [lalitkanojiya/Animated-Instagram-Logo-Using-HTML-CSS](https://github.com/lalitkanojiya/Animated-Instagram-Logo-Using-HTML-CSS)@[f6b920e13f...](https://github.com/lalitkanojiya/Animated-Instagram-Logo-Using-HTML-CSS/commit/f6b920e13f27b6fc901e8a8d8531001a875b7dfe)
#### Friday 2022-10-14 00:43:59 by Lalit Kanojiya

Add files via upload

Everybody is aware that any software must have an icon to indicate its purpose. Therefore, Instagram is a social networking platform that enables users to communicate with their friends, family, and other acquaintances. We made the decision to create an animated Instagram logo.

---
## [Offroaders123/Smart-Text-Editor](https://github.com/Offroaders123/Smart-Text-Editor)@[cb5a710d12...](https://github.com/Offroaders123/Smart-Text-Editor/commit/cb5a710d1209a67c99611c00a6e56d4aa2e0fafa)
#### Friday 2022-10-14 01:16:09 by Offroaders123

A Modern Legacy - Version Four

Changes:
- Upgrading to a new version! I felt a little whim of giving STE an update again. It has fallen to the side in favor of my other new projects also being worked on, so it hasn't had much love in a long time. I have learned a TON more new things since the last edits were made to STE, so pretty much the whole project feels like a spaghetti soup of legacy code. But, now with my work in TypeScript (or rather, work in other structures like class, and in Node), I think I can re-sort things back out again. I think STE kind of fell apart to the growing pains that come with learning how to code, haha. A lot of the codebase is way different to how I'd do things now (but I didn't know about the things I do now, so I don't blaim myself! I didn't know the other things out there), and I didn't want to keep going with the API that I had going before. Rather than adding to the mess, I knew that I should probably let the project rest a bit, then come back when I had a fresh set of eyes for it. And boy do I! The biggest things that could vastly help out STE's structure: Web Components, ES Modules, TypeScript (even simply `allowJS` / `checkJS`), and Async-Await.
- I likely will just work on STE here and there, until it's a bit more stable to work with. Or, like everything else I seem to do, it will be the project for the next few weeks, and I will get everything reworked in Web Components and TypeScript, all modernized. Here's to hoping I work on it moderately! XD

- So this update is the initial step in getting things sorted out again. I moved the styles and scripts into their own folders and files, just so `index.html` can breathe again XD
- Streamlined all relative URLs so they start with `./`, just like I've been making standard in my other projects. It didn't really matter before, but now it makes a bit more sense to have it the same everywhere, because ES Modules *require* (pun not intended) relative URLs to start with `./`. Consistency for the win!
- I also wanted to break up the files so that the GitHub language graph makes a bit more sense too, as right now, I think it says 98% HTML! Pretty much everything that could be inlined into the page, was inlined. Now that I actually have a domain, STE has room to spread out a bit, and it doesn't have to all fit in the one HTML file anymore. That was one of my early requirements for the app, since I used it almost exclusively over the `file://` protocol. News flash, it's been a PWA for about 2 years already! It can probably use separate files now XD

I really am looking forward to seeing what this will do for STE. I think I held off on updating it also because I had been wanting to focus on my NBT parser for the last while, and I wanted to get that set up first. Tied into that, I *100%* want to make STE a compatible NBT editor! It would be ff-ing amazing to open an NBT file using the File System Access API, view the NBT as SNBT right in the editor, then to just save it again with `Ctrl+S`. I'll have to rework the Editor/File workspace setup for STE though, as it will have to handle the `NBTData` class, and the UI would have to somehow give an option to edit the raw NBT data's file info, like the endianness, compression, and file headers. Right now STE only has to focus on the file data itself, and it's name. I'll probably add a settings cog or something to the Editor tab, and it could have the options there.

Oh yeah, and I also moved my old experimental branches into their own `archive/---` branches, as I think I will mostly just use them for inspiration rather than building on top of them at this point. Ideally I would've come back to them, but I went to work on other things instead :)

---
## [IndieanaJones/tgstation](https://github.com/IndieanaJones/tgstation)@[422accbe4e...](https://github.com/IndieanaJones/tgstation/commit/422accbe4e9b53f075f9a76ba6293435cb3399da)
#### Friday 2022-10-14 02:23:24 by John Willard

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
## [Exoricstuffer/exotic-web](https://github.com/Exoricstuffer/exotic-web)@[9b30632458...](https://github.com/Exoricstuffer/exotic-web/commit/9b30632458c1c326c37676ef34cbf4bcb647e978)
#### Friday 2022-10-14 02:34:09 by exoric stuffers

aaaaaaaaaaaaaaaaa i need to fix bug please work i hate my lifeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee

---
## [Lillecarl/bees](https://github.com/Lillecarl/bees)@[14ce81c081...](https://github.com/Lillecarl/bees/commit/14ce81c081e2aa3104e78bb74a54ecccd4624d0d)
#### Friday 2022-10-14 02:51:29 by Zygo Blaxell

fs: get rid of silly base class that causes build failures now

The base class thing was an ugly way to get around the lack of C99
compound literals in C++, and also to make the bare ioctls usable with
the derived classes.

Today, both clang and gcc have C99 compound literals, so there's no need
to do crazy things with memset.  We never used the derived classes for
ioctls, and for this specific ioctl it would have been a very, very bad
idea, so there's no need to support that either.  We do need to jump
through hoops for ostream& operator<<() but we had to do those anyway
as there are other members in the derived type.

So we can simply drop the base class, and build the args object on the
stack in `do_ioctl`.  This also removes the need to verify initialization.

There's no bug here since the `info` member of the base class was
never used in place by the derived class, but new compilers reject the
flexible array member in the base class because the derived class makes
`info` be not at the end of the struct any more:

	error: flexible array member btrfs_ioctl_same_args::info not at end of struct crucible::BtrfsExtentSame

Fixes: https://github.com/Zygo/bees/issues/232
Signed-off-by: Zygo Blaxell <bees@furryterror.org>

---
## [Zonespace27/tgstation](https://github.com/Zonespace27/tgstation)@[23bfdec8f4...](https://github.com/Zonespace27/tgstation/commit/23bfdec8f43046f7b54906509e38ed1ad91f5096)
#### Friday 2022-10-14 03:08:13 by LemonInTheDark

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
## [Zonespace27/tgstation](https://github.com/Zonespace27/tgstation)@[1810b85553...](https://github.com/Zonespace27/tgstation/commit/1810b855536f05891593b1379e455164f45fab3a)
#### Friday 2022-10-14 03:08:13 by tralezab

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
## [Zonespace27/tgstation](https://github.com/Zonespace27/tgstation)@[cee07f804c...](https://github.com/Zonespace27/tgstation/commit/cee07f804cc1df6d9cb0ff783ad4504458cf2c8b)
#### Friday 2022-10-14 03:08:13 by LemonInTheDark

Airlock open delay audit (#69905)


About The Pull Request

A: Mineral doors no longer take 6 SECONDS to open if you bump anything beforehand. Holy shit why would you do this.
B: Airlocks no longer require you to have not bumped anything in a second, lowered to 0.3 seconds. This is safe because I've moved shock immunity to its own logic. This should make opening doors feel less horrible
Why It's Good For The Game

Feels better.
Changelog

cl
balance: Airlocks will open on bump in series much faster now. As a tradeoff, you're immune to shocks from them for a second after you last got shocked by one.
fix: Mineral doors will no longer take 6 WHOLE SECONDS to open if you've bumped something else recently
/cl

---
## [TheKnightofAura/Citadel-Station-13-RP](https://github.com/TheKnightofAura/Citadel-Station-13-RP)@[24aca0ae55...](https://github.com/TheKnightofAura/Citadel-Station-13-RP/commit/24aca0ae55ce2204474ec23fed6d23cb46b6645e)
#### Friday 2022-10-14 03:12:29 by LordPapalus

Cargonia, but with less weapons (#4370)

* Cargonia is no more

Fuck you

* PLEASE

* Zandario, I will suck your PP

---
## [br-cz/abode](https://github.com/br-cz/abode)@[f9af02d72a...](https://github.com/br-cz/abode/commit/f9af02d72acbae20ec312260db26300c3063cd06)
#### Friday 2022-10-14 03:49:43 by Bricz

GOD DAMMIT I FUCKING HATE GCLOUD WHY DID U CHANGE MY LOAD BALANCER IP CMON BRO WTF HOURS GONE

---
## [Mu-L/hhvm](https://github.com/Mu-L/hhvm)@[cbeeb6fc89...](https://github.com/Mu-L/hhvm/commit/cbeeb6fc896d862aff10cd75bc42ee79beb962a9)
#### Friday 2022-10-14 04:49:32 by Lucian Wischik

I believe we never use changes_since_baseline

Summary:
Naming_sqlite stores a table that only ever has a single row: NAMING_LOCAL_CHANGES, whose row contains (1) an ocaml blob of local changes, (2) the revision for this saved-state.

The ocaml blob of local changes had been used for fast incremental naming table generation, as an ugly hack that was faster than generating the entire new naming-table from scratch i.e. writing 6M rows. In D31413518 (https://github.com/facebook/hhvm/commit/8f9e9d2f1568b084660bda8fe87b8725d61674d1) (Oct 2021) bobrenjc93 changed it to a much better technique, namely, inserting/removing only the delta rows. But it left behind the ocaml-blob of local changes. I wrote at the time "We should get rid of it: either in this diff or the next, delete the entire LocalChanges module." What gives us surety that it's okay to delete the ocaml-blob is that I had added telemetry D28839883 (https://github.com/facebook/hhvm/commit/330e97ccd08b144117c21a3ebefa248061d3d5ed) (June 2021) on the code-paths which read the ocaml-blob, and the telemetry shows that we only ever read an empty ocaml-blob.

But what about the second item, "(2) revision for this saved-state"? Do we ever use that? Reading the code shows that the only place "revision-for-saved-state" is ever consumed is by Hulk.v1 in a codepath that appears not to exist any longer, inside Naming_table.choose_local_changes. I think that Hulk.v1 used to provide a naming-table-delta along with the revision that the delta is with respect to, and it used to compare that revision against the naming-table-sqlite that it got from disk, and fail if they were different. This check had been introduced in D18723777 (https://github.com/facebook/hhvm/commit/7c671def9ee84762cf38e16d761c140a4bf01eca) (Nov 2019) for hulk remote workers. My hunch is that we're not using it any longer.

Therefore, this diff adds telemetry on the only codepath that uses "revision-for-saved-state" from the NAMING_LOCAL_CHANGES row. If this telemetry proves that we don't use it, and we already have telemetry which proves that ocaml-blob is always empty, then we'll be confident in deleting NAMING_LOCAL_CHANGES.

Reviewed By: bobrenjc93

Differential Revision: D40118751

fbshipit-source-id: 0b8e2eac4cfe8513cc5d0155184b7d15efd99dc8

---
## [mahak/cockroach](https://github.com/mahak/cockroach)@[f50670b344...](https://github.com/mahak/cockroach/commit/f50670b3440e91bec05aebc1bc425e4dd465583f)
#### Friday 2022-10-14 04:59:31 by Tobias Grieger

rpc: re-work connection maintenance

This commit simplifies the `rpc` package.

The main aim is to make the code and the logging it produces somewhat
clearer and to pave the way for an ultimate merging of `nodedialer` with
`rpc` as well as adoption of the `util/circuit` package (async-based
circuit breaker).

`rpc.Context` hadn't aged well. Back in the day, it was a connection
pool that held on to connections even when they failed. The heartbeat
loop would run forever and its latest outcome would reflect the health
of the connection. We relied on gRPC to reconnect the transport as
necessary.

At some point we realized that leaving the connection management to
gRPC could cause correctness issues. For example, if a node is de-
commissioned and brought up again, gRPC might reconnect to it but
now we have a connection that claims to be for node X but is actually
for node Y. Similarly, we want to be able to vet that the remote
node's cluster version is compatible with ours before letting any
messages cross the connection.

To achieve this, we added `onlyOnceDialer` - a dialer that fails
all but the first attempt to actually connect, and in particular
from that point on connections were never long lived once they
hit a failure state.

Still, the code and testing around the heartbeat loop continued
to nurture this illusion. I found that quite unappealing as it
was sure to throw off whoever would ultimately work on this code.

So, while my original impetus was to produce better log messages
from `rpc.Context` when there were connection issues, I took
the opportunity to simplify the architecture of the code to
reflect what it actually does.

In doing so, a few heartbeat-related metrics were removed, as they made
limited sense in a world where failing connections get torn down (i.e.
our world).

Connection state logging is now a lot nicer. Previously, one would very
frequently see the onlyOnceDialer's error "cannot reuse client
connection" which, if one is not familar with the concept of the
onlyOnceDialer is completely opaque, and for those few in the know is an
unhelpful error - you wanted the error that occurred during dialing.

I paid special attention to the "failfast" behavior. If connections
don't stay in the pool when they are unhealthy, what prevents us from
dialing down nodes in a tight loop? I realized that we got lucky with
our use of onlyOnceDialer because it would always prompt gRPC to do
one retry, and at a 1s backoff. So, the connection would stay in the
pool for at least a second, meaning that this was the maximum frequency
at which we'd try to connect to a down node.

My cleanups to onlyOnceDialer in pursuit of better logging elimitated
this (desirable) property. Instead we now skip the log messages should
they become too frequent. I claim that this is acceptable for now since
the vast majority of callers go through a `node.Diaelr`, which has a
circuit breaker (letting callers through at most once per second).

We previously configured gRPC with a 20s dial timeout. That means that
if a remote is unreachable, we'd spend 20s just trying to dial it,
possibly tying up callers that could be trying a reachable node in the
meantime. That seemed wildly too large; I am reducing it to 5s here
which is still generous (but there's a TLS handshake in here so better
not make it too tight).

We previously tried to re-use connections that were keyed with a NodeID
for dial attempts that didn't provide a NodeID. This caused some issues
over the years and was now removed; the extra RPC connections are
unlikely to cause any issues.

The internal connection map is now a plain map with an RWMutex. This is
just easier and gets the job done. The code has simplified as a result
and it's clearer that it's correct (which it repeatedly was not in the
past).

I implemented redactability for gRPC's `status.Status`-style errors,
so they format nicer and at least we get to see the error code (the
error message is already flattened when gRPC hands us the error,
sadly).

There are various other improvements to errors and formatting. The
following are excerpts from the health channel when shutting down
another node in a local cluster:

Connection is first established:

> [n3,rnode=1,raddr=‹127.0.0.1:26257›,class=system,rpc] 3  connection is now ready

n1 goes down, i.e. existing connection is interrupted (this error comes
from `onlyOnceDialer`):

> [n3,rnode=1,raddr=‹127.0.0.1:26257›,class=system,rpc] 35  closing
connection after: ‹rpc error: code = Unavailable desc = connection
error: desc = "transport: Error while dialing connection interrupted
(did the remote node shut down or are there networking issues?)"›

Reconnection attempts; these logs are spaced 1-2s apart:

> [n3,rnode=1,raddr=‹127.0.0.1:26257›,class=system,rpc] 37  unable to
connect (is the peer up and reachable?): initial connection heartbeat
failed: ‹rpc error: code = Unavailable desc = connection error: desc =
"transport: Error while dialing dial tcp 127.0.0.1:26257: connect:
connection refused"›

n3 is back up:

> [n3,rnode=1,raddr=‹127.0.0.1:26257›,class=system,rpc] 49  connection is now ready

There are other connection errors in the logs that stem from operations
checking for a healthy connection, failing to get through circuit
breakers, etc., such as these:

> [n3,intExec=‹claim-jobs›,range-lookup=/Table/15/4/‹NULL›] 33  unable
to connect to n1: failed to check for ready connection to n1 at
‹127.0.0.1:26257›: ‹connection not ready: TRANSIENT_FAILURE›

Release note (general change): Previously, CockroachDB employed a 20s
connection timeout for cluster-internal connections between nodes.  This
has been reduced to 5s to potentially reduce the impact of network
issues.

Release note (general change): Previously, CockroachDB (mostly) shared a
TCP connection for the KV and Gossip subsystems. They now use their own
connection each, so the total number of outgoing and incoming TCP
connections at each node in the cluster will increase by 30 to 50
percent.

---
## [shubham1994s/AppynittyWebApp](https://github.com/shubham1994s/AppynittyWebApp)@[e1fbc530f5...](https://github.com/shubham1994s/AppynittyWebApp/commit/e1fbc530f57bf97eda005e37ebd02fec75b4cdb4)
#### Friday 2022-10-14 05:23:49 by umeshl@appynitty.com

changes done By my side  i will be definetly sucessfull in this year in trading i can do anything with my life god always with me gods energy passing through me thanku for support that give me forgive me for any mistake i am always your child forgive me negative thoughts and thnaku very giveing me all chance for grow in my life

---
## [LeonCanek/JustoLeon](https://github.com/LeonCanek/JustoLeon)@[fe2aeeb67c...](https://github.com/LeonCanek/JustoLeon/commit/fe2aeeb67c68476068121321a07260a6c194fdd8)
#### Friday 2022-10-14 05:27:55 by Justo Leon

Hoy fue un buen dia

Well, if you wanted honesty
That's all you had to say
I never want to let you down
Or have you go, it's better off this way

For all the dirty looks
The photographs your boyfriend took
Remember when you broke your foot
From jumping out the second floor?

I'm not okay
I'm not okay
I'm not okay
You wear me out

What will it take to show you
That it's not the life it seems? (I'm not okay)
I've told you time and time again
You sing the words, but don't know what it means (I'm not okay)

To be a joke and look
Another line without a hook
I held you close as we both shook
For the last time, take a good hard look

I'm not okay
I'm not okay
I'm not okay
You wear me out

---
## [petre-symfony/symfony-6-and-the-database](https://github.com/petre-symfony/symfony-6-and-the-database)@[2fd8ad12ad...](https://github.com/petre-symfony/symfony-6-and-the-database/commit/2fd8ad12ad03faf326d130b2367fa1498991f472)
#### Friday 2022-10-14 06:46:22 by petrero

11.5 The Query Builder

  Reusing Query Builder Logic
  - As your project gets bigger and bigger, you're going to create more and more methods in your repository for custom queries. And you may start repeating the same query logic over and over again. For example, we might order by the votes in a bunch of different methods in this class.

  To avoid duplication, we can isolate that logic into a private method. Check it out! Add private function addOrderByVotesQueryBuilder(). This will accept a QueryBuilder argument (we want the one from Doctrine\ORM), but let's make it optional. And we will also return a QueryBuilder.

  The job of this method is to add this ->orderBy() line. And for convenience, if we don't pass in a , we'll create a new one.

  To allow that, start with $queryBuilder = $queryBuilder ?? $this->createQueryBuilder('mix'). I'm purposely using mix again for the alias. To keep life simple, choose an alias for an entity and consistently use it everywhere.

  Anyways, this line itself may look weird, but it basically says:

    If there is a QueryBuilder, then use it. Else, create a new one.

  Below return $queryBuilder... go steal the ->orderBy() logic from up here and... paste. Awesome!

  PhpStorm is a little angry with me... but that's just because it's having a rough morning and needs a restart: our code is, hopefully, just fine.

  Back up in the original method, simplify to $queryBuilder = $this->addOrderByVotesQueryBuilder() and pass it nothing.

  Isn't that nice? When we refresh... it's not broken! Take that PhpStorm!

  Next, let's add a "mix show" page where we can view a single vinyl mix. For the first time, we'll query for a single object from the database and deal with what happens if no matching mix is found.

---
## [AnywayFarus/tgstation](https://github.com/AnywayFarus/tgstation)@[fc7c186957...](https://github.com/AnywayFarus/tgstation/commit/fc7c186957088b6ffd0605f814bea754670c0212)
#### Friday 2022-10-14 07:25:04 by RikuTheKiller

Brains can now be healed with mannitol without being fully decayed among other quality of life tweaks (#70357)

Removed the minimum amount of mannitol required to pour it since limiting this made barely any sense in the first place. Why oh why must we coders implement useless restrictions? (Useless restrictions caused the decay bug anyways.)

Brains no longer care about whether or not they're fully decayed when checking if they can be healed by pouring mannitol on them. They instead check if they're damaged at all and if they are, they'll let you pour mannitol on them.

The amount of time it takes to pour mannitol onto a brain is now 3 seconds instead of 6 seconds as it was way too slow. (Especially since something like a surgery step takes less time than 6 seconds.)

The solution is now only partially consumed as well, meaning if you need 20u of mannitol to fix a brain and you have a mixture of 40u of mannitol and 40u of mercury for example, pouring it will consume 40u of the mixture since you can't magically separate out the mannitol. This is rounded up, by the way. (Before this it simply consumed all of the mannitol, somehow you apparently can't stop pouring even while slowly pouring, according to the text.)

I've also very slightly increased the consistency of the pouring messages.

Fixes #70355

---
## [infecsean/Obsidian-Cloud](https://github.com/infecsean/Obsidian-Cloud)@[cf7859bf19...](https://github.com/infecsean/Obsidian-Cloud/commit/cf7859bf197f77daaa0e7aecd8f31bd00702c5f1)
#### Friday 2022-10-14 07:58:35 by infecsean

holy fuck what the fuck is happening why are there so many summatives hello???

the fucking everybody can go suck my fuckin enormous penous and oh my god we have chinese next next thursday i just remembered what the fuck why do we even have all this shit due when we also have so many colleges to do oh my gawd holy shit

---
## [ProgrammerDuck2/School_MilkyPotion](https://github.com/ProgrammerDuck2/School_MilkyPotion)@[6215fe9c7e...](https://github.com/ProgrammerDuck2/School_MilkyPotion/commit/6215fe9c7e455d2b651fb5d1d235b9f28f08457c)
#### Friday 2022-10-14 08:02:58 by Lasse B. I

Material, audio.

Added new materials on the walls. Re-added old audio. Also fixed the issue with water. Changed the value multiplied with the insanity filter to increase time. This was a magic number? I hope I did not fuck anything up. God have mercy on our souls.

---
## [open-policy-agent/opa](https://github.com/open-policy-agent/opa)@[965301f90e...](https://github.com/open-policy-agent/opa/commit/965301f90e1c10900c2c134ee21e486993796a20)
#### Friday 2022-10-14 08:15:57 by Stephan Renatus

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[76aab2d56e...](https://github.com/treckstar/yolo-octo-hipster/commit/76aab2d56e6e3a0e13f080a727deeb658650b183)
#### Friday 2022-10-14 08:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [petre-symfony/symfony-6-and-the-database](https://github.com/petre-symfony/symfony-6-and-the-database)@[44cfc9a285...](https://github.com/petre-symfony/symfony-6-and-the-database/commit/44cfc9a2852aef452042818ec66fdb5e282a7081)
#### Friday 2022-10-14 08:25:00 by petrero

15.2 Updating an Entity

  Redirecting to Another Page
  - So... we are successfully saving the new vote count to the database! Now what? Because... I don't think this die statement is going to look good on production.

  Well, anytime you submit a form successfully, you always do the same thing: redirect to another page. How do we redirect in Symfony? With return $this->redirect() passing whatever URL you want to redirect to. Though, usually we're redirecting to another page on our site... so we use a similar shortcut called redirectToRoute() and then pass a route name.

  Let's redirect back to the show page. Copy the app_mix_show route name, paste... and just like with the Twig path() function, this accepts a second argument: an array of the route wildcards that we need to fill in. In this case, we have an {id} wildcard... so pass id set to $mix->getId().

  Now, remember: controllers always return a Response object. And, whelp it turns out that a redirect is a response. It's a response that, instead of containing HTML, basically says:

    Please send the user to this other URL

  The redirectToRoute() method is a shortcut that returns this special response object, called a RedirectResponse.

  Anyways, let's test the whole flow! Refresh, and... got it! After voting, we end up right back on this page. And, thanks to Turbo, this is all happening via Ajax calls... which is a nice bonus.

  The only problem is that... it's so smooth that it's not super obvious that my vote was actually saved - other than seeing the vote number change. It might be better if we showed a success message. Let's do that next by learning about flash messages. We're also going to make our VinylMix entity trendier by exploring the concept of smart versus anemic models.

---
## [petre-symfony/symfony-6-and-the-database](https://github.com/petre-symfony/symfony-6-and-the-database)@[8122d0067c...](https://github.com/petre-symfony/symfony-6-and-the-database/commit/8122d0067c779f79285b413040fb5d3ffcc69207)
#### Friday 2022-10-14 08:25:00 by petrero

17.2 Doctrine Extensions: Timestampable

  Enabling Timestampable
  - So this bundle obviously has its own documentation. You can search for stof/doctrine-extensions-bundle and find it on Symfony.com. But the majority of the docs live on the underlying DoctrineExtensions library... which contains a bunch of really cool behaviors, including "sluggable" and "timestampable". Let's add "timestampable" first.

  Step one: go into config/packages/ and open the configuration file it just added. Here, add orm because we're using Doctrine ORM, then default, and lastly timestampable: true.

  This won't really do anything yet. It just activates a Doctrine listener that will be looking for entities that support timestampable each time an entity is inserted or updated. How do we make our VinylMix support timestampable? The easiest way (and the way I like to do it) is via a trait.

  At the top of the class, say use TimestampableEntity.

  That's it. We're done! Lunch break!

  To understand this black magic, hold "cmd" or "ctrl" and click into TimestampableEntity. This adds two properties: createdAt and updatedAt. And these are just normal fields, like the createdAt that we had before. It also has getter and setter methods down here, just like we have in our entity.

  The magic is this #[Gedmo\Timestampable()] attribute. This says that:

    this property should be set on: 'update'

  and

    this property should be set on: 'create'.

  Thanks to this trait, we get all of this for free! And... we no longer need our createdAt property... because it already lives in the trait. So delete the property... and the constructor... and down here, remove the getter and setter methods. Cleansing!

---
## [petre-symfony/symfony-6-and-the-database](https://github.com/petre-symfony/symfony-6-and-the-database)@[4709083e60...](https://github.com/petre-symfony/symfony-6-and-the-database/commit/4709083e60a699b6eacd91550015e5c960e70cfd)
#### Friday 2022-10-14 08:25:00 by petrero

14.1 The Request Object

  New goal team: to allow users to upvote and downvote a mix. To accomplish this, in the VinylMix entity, when a user votes, we need to send an UPDATE query to change the  integer property in the database.

  Adding a Simple Form
  - Let's first focus on the user interface. Open templates/mix/show.html.twig. To start, print {{ mix.votesString }} votes so we can see that here.

  And... perfect! To add the upvote and downvote functionality, we could use some fancy JavaScript. But we're going to keep it simple by adding a button that posts a form. Well this will actually be fancier than it sounds. In the first tutorial, we installed the Turbo JavaScript library. So even though we'll use a normal <form> tag and button, Turbo will automatically submit it via AJAX for a smooth experience.

  By the way, Symfony does have a form component and we'll talk about that in a future tutorial. But this form is going to be so simple that we don't really need it anyway. Add a beautifully boring <form> tag with action set to the path() function.

  The form will submit to a new controller that... we still need to create!

  Head over to MixController and add a new public function called vote(). Give this the #[Route()] attribute with the URL /mix/{id}/vote. And because we need to link to this, add a name: app_mix_vote.

  The {id} route wildcard will hold the id of the specific VinylMix that the user is voting on. To query for that, use the trick we learned earlier: add an argument type-hinted with VinylMix and call it $mix. Oh, and while we don't need to, I'll add the Response return type. Adding this is just a good practice.

  Inside, to make sure things are working, dd($mix).

  Cool! Copy the name of the route, go back to the template - show.html.twig - and inside path(), paste. And because this route has an {id} wildcard, pass id set to mix.id. Also give the form method="POST"... because anytime that submitting a form will change data on your server, it should submit with POST.

  Heck, we can even enforce this requirement on our route by adding methods: ['POST']. That's optional, but now, if someone, for some reason, goes directly to this URL, which is a GET request, it won't match the route. Handy!

  Head back over to the form. This form... will be kind of strange. Instead of having fields the user can type into, all we need is a button. Add <button> with type="submit"... and then some classes for styling. For the text, use a Font Awesome icon: a <span> with class="fa fa-thumbs-up".

  Perfecto! Let's go check it out. Refresh and... thumbs up! And when we click it... beautiful! It hits the endpoint! Notice that the URL didn't change... that's just because Turbo submitted the form via Ajax... and then our dd() stopped everything.

  Ok, in a minute, we're going to add another button with a thumbs down. So, somehow, in our controller, we're going to need to figure out which button - up or down - was just pushed.

  To do that, on the button, add name="direction" and value="up". Now, if we click this button, it will send one piece of POST data called direction set to the value up... almost as if the user typed the word up into a text field.

---
## [petre-symfony/symfony-6-and-the-database](https://github.com/petre-symfony/symfony-6-and-the-database)@[830c8f4d3e...](https://github.com/petre-symfony/symfony-6-and-the-database/commit/830c8f4d3eb3b2f367e54c29ff87afc56808ce21)
#### Friday 2022-10-14 08:25:00 by petrero

16.1 Flash Message & Rich vs Anemic Models

  After we submit a form successfully, we always redirect. Often times, we'll also want to show the user a success message so they know everything worked. Symfony has a special way to handle this: flash messages.

  To set a flash message, before redirecting, call $this->addFlash() and pass, in this situation, success. For the second argument, put the message that you want to show to the user, like Vote counted./bin/console make:entity

  The success key could be anything... it's kind of like a category for the flash message... and you'll see how we use that in a minute.

  Flash messages have a fancy name, but they're a simple idea; Symfony stores flash messages in the user's session. What makes them special is that Symfony will remove the message automatically as soon as we read it. They're like self-destructing messages. Pretty cool.

  Reading Flash Messages
  - So... how do we read them? The way I like to do it is by opening up my base template - base.html.twig - and reading and rendering them here. Let's put it right after the navigation but before the {% block body %}. Say {% for message in %}. Then, we want to read out any success category flash messages we might have. To do this, we can leverage the one global Twig variable in Symfony: app. This has several methods on it, like environment, request, session, the current user, or one called app.flashes. Pass this the category (in our case,success). As I mentioned, this could be anything. If you put dinosaur as the key in a controller, then you'd read the dinosaur messages out here. Finish with {% endfor %}.

  Typically, you'll only have one success message in your flash at a time, but technically you can have multiple. That's why we're looping over them.

  Inside of this, render a <div> with class="alert alert-success" so it looks like a happy message. Then, print out message.

  So if this works correctly, it will read all of our success flash messages and render them. And once they've been read, Symfony will remove them so that they won't render again on the next page load. By putting this in the base template, we can now set flash messages from anywhere in our app and they'll be rendered on the page. Pretty cool.

  Watch. Head back to our page, upvote and... beautiful! We'll probably want to remove this extra margin in a real project, but we'll leave it for now.

---
## [orangebees/PolarDB-for-PostgreSQL](https://github.com/orangebees/PolarDB-for-PostgreSQL)@[925f46ffb8...](https://github.com/orangebees/PolarDB-for-PostgreSQL/commit/925f46ffb82f0b25c94e7997caff732eaf14367d)
#### Friday 2022-10-14 09:47:56 by Tom Lane

Fix handling of targetlist SRFs when scan/join relation is known empty.

When we introduced separate ProjectSetPath nodes for application of
set-returning functions in v10, we inadvertently broke some cases where
we're supposed to recognize that the result of a subquery is known to be
empty (contain zero rows).  That's because IS_DUMMY_REL was just looking
for a childless AppendPath without allowing for a ProjectSetPath being
possibly stuck on top.  In itself, this didn't do anything much worse
than produce slightly worse plans for some corner cases.

Then in v11, commit 11cf92f6e rearranged things to allow the scan/join
targetlist to be applied directly to partial paths before they get
gathered.  But it inserted a short-circuit path for dummy relations
that was a little too short: it failed to insert a ProjectSetPath node
at all for a targetlist containing set-returning functions, resulting in
bogus "set-valued function called in context that cannot accept a set"
errors, as reported in bug #15669 from Madelaine Thibaut.

The best way to fix this mess seems to be to reimplement IS_DUMMY_REL
so that it drills down through any ProjectSetPath nodes that might be
there (and it seems like we'd better allow for ProjectionPath as well).

While we're at it, make it look at rel->pathlist not cheapest_total_path,
so that it gives the right answer independently of whether set_cheapest
has been done lately.  That dependency looks pretty shaky in the context
of code like apply_scanjoin_target_to_paths, and even if it's not broken
today it'd certainly bite us at some point.  (Nastily, unsafe use of the
old coding would almost always work; the hazard comes down to possibly
looking through a dangling pointer, and only once in a blue moon would
you find something there that resulted in the wrong answer.)

It now looks like it was a mistake for IS_DUMMY_REL to be a macro: if
there are any extensions using it, they'll continue to use the old
inadequate logic until they're recompiled, after which they'll fail
to load into server versions predating this fix.  Hopefully there are
few such extensions.

Having fixed IS_DUMMY_REL, the special path for dummy rels in
apply_scanjoin_target_to_paths is unnecessary as well as being wrong,
so we can just drop it.

Also change a few places that were testing for partitioned-ness of a
planner relation but not using IS_PARTITIONED_REL for the purpose; that
seems unsafe as well as inconsistent, plus it required an ugly hack in
apply_scanjoin_target_to_paths.

In passing, save a few cycles in apply_scanjoin_target_to_paths by
skipping processing of pre-existing paths for partitioned rels,
and do some cosmetic cleanup and comment adjustment in that function.

I renamed IS_DUMMY_PATH to IS_DUMMY_APPEND with the intention of breaking
any code that might be using it, since in almost every case that would
be wrong; IS_DUMMY_REL is what to be using instead.

In HEAD, also make set_dummy_rel_pathlist static (since it's no longer
used from outside allpaths.c), and delete is_dummy_plan, since it's no
longer used anywhere.

Back-patch as appropriate into v11 and v10.

Tom Lane and Julien Rouhaud

Discussion: https://postgr.es/m/15669-02fb3296cca26203@postgresql.org

---
## [ppajda/android_kernel_oneplus_sm8250](https://github.com/ppajda/android_kernel_oneplus_sm8250)@[8d968b46e8...](https://github.com/ppajda/android_kernel_oneplus_sm8250/commit/8d968b46e8e1d49d5ab519bf1ba788c32e8d0b1a)
#### Friday 2022-10-14 11:19:37 by Jason A. Donenfeld

random: use linear min-entropy accumulation crediting

commit c570449094844527577c5c914140222cb1893e3f upstream.

30e37ec516ae ("random: account for entropy loss due to overwrites")
assumed that adding new entropy to the LFSR pool probabilistically
cancelled out old entropy there, so entropy was credited asymptotically,
approximating Shannon entropy of independent sources (rather than a
stronger min-entropy notion) using 1/8th fractional bits and replacing
a constant 2-2/√𝑒 term (~0.786938) with 3/4 (0.75) to slightly
underestimate it. This wasn't superb, but it was perhaps better than
nothing, so that's what was done. Which entropy specifically was being
cancelled out and how much precisely each time is hard to tell, though
as I showed with the attack code in my previous commit, a motivated
adversary with sufficient information can actually cancel out
everything.

Since we're no longer using an LFSR for entropy accumulation, this
probabilistic cancellation is no longer relevant. Rather, we're now
using a computational hash function as the accumulator and we've
switched to working in the random oracle model, from which we can now
revisit the question of min-entropy accumulation, which is done in
detail in <https://eprint.iacr.org/2019/198>.

Consider a long input bit string that is built by concatenating various
smaller independent input bit strings. Each one of these inputs has a
designated min-entropy, which is what we're passing to
credit_entropy_bits(h). When we pass the concatenation of these to a
random oracle, it means that an adversary trying to receive back the
same reply as us would need to become certain about each part of the
concatenated bit string we passed in, which means becoming certain about
all of those h values. That means we can estimate the accumulation by
simply adding up the h values in calls to credit_entropy_bits(h);
there's no probabilistic cancellation at play like there was said to be
for the LFSR. Incidentally, this is also what other entropy accumulators
based on computational hash functions do as well.

So this commit replaces credit_entropy_bits(h) with essentially `total =
min(POOL_BITS, total + h)`, done with a cmpxchg loop as before.

What if we're wrong and the above is nonsense? It's not, but let's
assume we don't want the actual _behavior_ of the code to change much.
Currently that behavior is not extracting from the input pool until it
has 128 bits of entropy in it. With the old algorithm, we'd hit that
magic 128 number after roughly 256 calls to credit_entropy_bits(1). So,
we can retain more or less the old behavior by waiting to extract from
the input pool until it hits 256 bits of entropy using the new code. For
people concerned about this change, it means that there's not that much
practical behavioral change. And for folks actually trying to model
the behavior rigorously, it means that we have an even higher margin
against attacks.

Cc: Theodore Ts'o <tytso@mit.edu>
Cc: Dominik Brodowski <linux@dominikbrodowski.net>
Cc: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Reviewed-by: Eric Biggers <ebiggers@google.com>
Reviewed-by: Jean-Philippe Aumasson <jeanphilippe.aumasson@gmail.com>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [tomMoulard/dwm-fork](https://github.com/tomMoulard/dwm-fork)@[67d76bdc68...](https://github.com/tomMoulard/dwm-fork/commit/67d76bdc68102df976177de351f65329d8683064)
#### Friday 2022-10-14 12:19:29 by Chris Down

Do not allow focus to drift from fullscreen client via focusstack()

It generally doesn't make much sense to allow focusstack() to navigate
away from the selected fullscreen client, as you can't even see which
client you're selecting behind it.

I have had this up for a while on the wiki as a separate patch[0], but
it seems reasonable to avoid this behaviour in dwm mainline, since I'm
struggling to think of any reason to navigate away from a fullscreen
client other than a mistake.

0: https://dwm.suckless.org/patches/alwaysfullscreen/

---
## [GitGudTesting/secrets_testing_biggie-GordonArscott](https://github.com/GitGudTesting/secrets_testing_biggie-GordonArscott)@[4637cf649c...](https://github.com/GitGudTesting/secrets_testing_biggie-GordonArscott/commit/4637cf649c3ebb204c67991028c42f376415d85b)
#### Friday 2022-10-14 13:15:22 by Gordonias

Putting the dump folder in the actual student repo so that i don't have to bother with some weird curl yml dodgy imports. If this works i might try and put it in the yml file but honestly i actually dont see a massive point, the students can kinda just live with it and i'll tell them not to delete it. COs it's probably more trouble than it's worth.

---
## [Jureiia/Skyrat-tg](https://github.com/Jureiia/Skyrat-tg)@[23b7daee59...](https://github.com/Jureiia/Skyrat-tg/commit/23b7daee59100e34f488893b57cd3787a0c08b99)
#### Friday 2022-10-14 13:20:08 by SkyratBot

[MIRROR] Simplifies SM damage calculation, tweaks the numbers. [MDB IGNORE] (#16733)

* Simplifies SM damage calculation, tweaks the numbers. (#70347)

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

* Simplifies SM damage calculation, tweaks the numbers.

Co-authored-by: vincentiusvin <54709710+vincentiusvin@users.noreply.github.com>

---
## [GNOME/glib](https://github.com/GNOME/glib)@[b8e1ecdd6b...](https://github.com/GNOME/glib/commit/b8e1ecdd6bfd6ff00b7b70f6177549f3a8d3cba3)
#### Friday 2022-10-14 15:31:45 by Michael Catanzaro

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
## [kleinerm/Psychtoolbox-3](https://github.com/kleinerm/Psychtoolbox-3)@[0ecdccb774...](https://github.com/kleinerm/Psychtoolbox-3/commit/0ecdccb774ab08cbd27b69ac681420ca4827279e)
#### Friday 2022-10-14 16:02:53 by Mario Kleiner

PsychVulkan/Linux: Add new bug fix for Mesa Vulkan direct display bug.

As of current Mesa 22.3-devel git snapshot and earlier versions, running
in fullscreen Vulkan direct-display mode only works the first time in a
session. On successive runs, the driver will error in vkQueuePresentKHR()
with a VK_ERROR_SURFACE_LOST error, and we are dead with a hard hang!

This only happens if the RandR output which we lease and switch to Vulkan
direct display mode has a non-zero (x,y) top-left corner viewport offset,
not on a single-display setup, a mirror setup, or a one video output per
X-Screen multi-X-Screen/multi-Display setup, as in those configs, the
viewport offset is always (0,0). Multi-output on single X-Screen however
dies for all but the one output at (0,0).

I tracked this down to a Mesa/Vulkan/WSI/DirectDisplay state caching bug,
developed and tested a bug fix and will upstream that fix soon. Basically
the WSI internal wsi_display_connector->active state for the used output
does not get reset to false == Inactive at the end of a session when the
display gets released back to the Window server / X-Server at call to
vkReleaseDisplay(). So if the same output is switched to direct display
mode again in the next session, with the same video mode, WSI thinks the
output is still active and at proper video mode and skips a full modeset,
instead directly goes to pageflip submission. This goes ok for a output
with RandR viewport (0,0, fbwidth, fbheight), but on a RandR output with
non-zero (x,y) offsets, the X-Server will have set a mode with corresponding
offsets into the X-Screens big shared (across all RandR outputs / crtcs).
The current Vulkan WSI has a framebuffer per VKDisplay and requires a
viewport offset of (0,0), so the viewport fits into the Vulkan framebuffer.
This is violated if WSI skips the modeset to (0,0) offset, and the kernel
subsequently aborts the pageflip with a -ENOSPACE error code, which itself
puts the Vulkan swapchain into VK_ERROR_SURFACE_LOST state and game over!

Error handling as recommended by spec (destroy and recreate the swapchain)
would not help, as connector state is cached at VkInstance level, not at
swapchain level.

A proper fix is to reset WSI connector logical state to inactive at
vkReleaseDisplay() time - Fix to be upstreamsn.

Our hacky workaround is to detect the trigger condition fullscreen on
output with non-zero (x,y) offset on a Mesa Vulkan driver with a Mesa
version before the properly fixed version, and then schedule a
'clear PsychVulkanCore' between runs to completely destroy the Vulkan
instance, thereby get rid of the stale connector state cache. This
resolves the bug for now. Ergo reenable that ugly needsMesaDDMWa=1 full
driver shutdown workaround again on Linux + Fullscreen + Mesa < 30.0.0,
until my bug fix makes it into a Mesa bug fix upstream release.

-> With this workaround, the PsychImaging 'MirrorDisplayTo2ndOutputHead'
   display mirroring with Vulkan for primary stimulus window and standard
   Screen OpenGL for the experimenter feedback "Mirror" slave window now
   works as tested on a single-X-Screen, dual-display setup under both
   Ubuntu 20.04.5-LTS, X-Server 1.20.13 with Intel Kabylake gpu and on
   Ubuntu 22.04.1-LTS, X-Server 21 with AMD Polaris gpu, where the main
   Vulkan onscreen window is fullscreen on a 120 Hz refresh video output,
   and the OpenGL mirror slave window is windowed on a standard 60 Hz
   standard KDE or Ubuntu desktop GUI. Main stimulation runs unthrottled
   with perfect timing at full 120 fps on 120 Hz display, whereas the
   mirror window tears on the 60 Hz display, as expected, with effects
   more spectacular when the desktop compositor is off than when it is on.

   Testing on macOS 12.6 on same setup with AMD Polaris showed that it
   works as well, both in Vulkan mode and OpenGL native mode, and the
   framerate is improved with slave window vsync off, but the improvement
   is more modest and performance of the same hardware under macOS 12 is
   much worse than under Ubuntu 22.04.1-LTS. But this is due to macOS
   deficiency, not problems with our mirroring approach.

---
## [dunkanos/Angel-Arena-Reborn](https://github.com/dunkanos/Angel-Arena-Reborn)@[90573812a2...](https://github.com/dunkanos/Angel-Arena-Reborn/commit/90573812a2d3342b57555316986f78b6dce37f67)
#### Friday 2022-10-14 16:31:06 by Dunkan

Patch 25.06.2022

Hero changes:

Abaddon
	- 1 skill self damage	changed from 30/35/40/45/50/55/60 to 50
	- 2 skill cast point  changed from 0.452 to 0.3
	- 2 skill duration  changed from  13 to 15
	- 3 skill movement speed changed from 25 to 15/17/19/21/23/25/25"

Abyssal Underlord
	- 2 skill root duration 	1.0/1.2/1.4/1.5/1.6/1.7/2.1" to 1.0/1.2/1.3/1.4/1.5/1.6/1.7

Alkchmist
	- shard skill Berserk Potion bonus ms 0 to 30

Ancient Аpparation
	- 2 skill shard damage changed from 40 to 150
	- 2 skill shard attack speed slow changed from 20 to 50

Dragon Knight
	- Fireball damage changed from 75 to 150

Furion
	- 1 skill Cooldown changed from 14/13/12/11/10/9/8 to 15
	- 3 skill treant health changed from 550/650/750/850/950/1050/1150 to 550/600/650/700/750/850/1100
	- 3 skill treant damage changed from 45/55/65/75/85/95/105 to 25/30/45/55/60/65/105
	- 4 skill Cooldown changed from 50 to 65

Huskar
	- 4 skill health damage changed from 45 to 20/22/25/27/33/36/45

Chaos Knight
 	- 3 skill crit chance changed from 30 to 25
 	- 3 skill crit max changed from 190/220/250/280/310/350/400 to 170/190/220/250/290/320/350
 	- 3 skill lifesteal changed from 30/35/40/45/50/55/60 to 25/30/35/40/45/50/55

Crystal Maiden's

 	- 3 skill mana per cast 10/15/20/25/30/35/40

Centaur
 	- 1 skill stun duration changed from 2.0 to 2.0/2.1/2.2/2.3/2.4/2.5/2.6

Dawnbreaker
 	- 4 skill damage of pulsation changed from 30/50/70/80/90/100/110 to 50/75/100/125/150/175/200
 	- 4 skill heal of pulsation changed from 50/70/90/110/130/150/170 to 50/75/100/125/150/175/200
 	- 4 skill damage changed from 130/160/190/220/250/280/310 to 200/300/400/500/600/700/800

Medusa
	- Cold Blooded Cooldown changed from 6 to 10

Marci
	- 4 skill Cooldown changed from 110/100/90/80/70/60/50 to 80/75/70/65/60/55/50
	- 4 skill between flurries changed from 1.75 to 1.55/1.50/1.45/1.40/1.35/1.30/1.25
	- 4 skill attack Stacks changed from 3/4/5/6/7/8/9 to 4/5/6/7/8/9/10
	- talent 25lvl silence duration changed from 1.5sec to 0.5sec

Primal Beast
	- Added to Angel Arena

Techies
	- Added techies skill frm dota

Undying
	- 4 skill Cooldown changed from 40 to 60
	- Shard Cooldown ultimate changed from 35 to 20

Item changes:

Tome of heroes
	- stack start game 5
	- delay before the start of the game 600sec
	- Max stack 40
	- Cooldown stack 20sec
	- Cost changed from 1250 to 1500

Ethereal Blade
	- Craft changed from Ghost scepter + Recipe to Mystic staff + Ghost scepter + Recipe

Gem
	- cast range changed from 300 to 500
	- active skill radius changed from 300 to 500
	- duration active skill changed from 4 to 8
	- Cooldown active skill changed from 12 to 30

Bosses:

Keymaster
	- now Ignores terrain
	- ms changed from 365 to 400

Creeps:

Satyr hand
	- 3 skill magic amplify changed from 50 to 20

Fixes:
Storm Spirit 1 skill damage fixed
Earth Spirit ultimate fixed
Elder Titan ultimate fixed
Abyssal Underlord ultimate fixed
Omniknight 3 skill and ultimate fixed
Pudge 3 skill fixed
Templar Assassin 3 skill fixed
Shadow Fiend aghanim fixed
Hoodwink shard skill fixed
Morphlimg 1 skill fixed
Swift blink range fixed
Overwhelming blink range fixed
Arcane blink range fixed

---
## [dunkanos/Angel-Arena-Reborn](https://github.com/dunkanos/Angel-Arena-Reborn)@[24633a752b...](https://github.com/dunkanos/Angel-Arena-Reborn/commit/24633a752b5738342b0364e0ebb34764f2e2d41b)
#### Friday 2022-10-14 16:31:06 by Dunkan

Patch 25.06.2022

Hero changes:

Abaddon
	- 1 skill self damage	changed from 30/35/40/45/50/55/60 to 50
	- 2 skill cast point  changed from 0.452 to 0.3
	- 2 skill duration  changed from  13 to 15
	- 3 skill movement speed changed from 25 to 15/17/19/21/23/25/25"

Abyssal Underlord
	- 2 skill root duration 	1.0/1.2/1.4/1.5/1.6/1.7/2.1" to 1.0/1.2/1.3/1.4/1.5/1.6/1.7

Alkchmist
	- shard skill Berserk Potion bonus ms 0 to 30

Ancient Аpparation
	- 2 skill shard damage changed from 40 to 150
	- 2 skill shard attack speed slow changed from 20 to 50

Dragon Knight
	- Fireball damage changed from 75 to 150

Furion
	- 1 skill Cooldown changed from 14/13/12/11/10/9/8 to 15
	- 3 skill treant health changed from 550/650/750/850/950/1050/1150 to 550/600/650/700/750/850/1100
	- 3 skill treant damage changed from 45/55/65/75/85/95/105 to 25/30/45/55/60/65/105
	- 4 skill Cooldown changed from 50 to 65

Huskar
	- 4 skill health damage changed from 45 to 20/22/25/27/33/36/45

Chaos Knight
 	- 3 skill crit chance changed from 30 to 25
 	- 3 skill crit max changed from 190/220/250/280/310/350/400 to 170/190/220/250/290/320/350
 	- 3 skill lifesteal changed from 30/35/40/45/50/55/60 to 25/30/35/40/45/50/55

Crystal Maiden's

 	- 3 skill mana per cast 10/15/20/25/30/35/40

Centaur
 	- 1 skill stun duration changed from 2.0 to 2.0/2.1/2.2/2.3/2.4/2.5/2.6
Charon
        - Ultimate root can be dispelled

Dawnbreaker
 	- 4 skill damage of pulsation changed from 30/50/70/80/90/100/110 to 50/75/100/125/150/175/200
 	- 4 skill heal of pulsation changed from 50/70/90/110/130/150/170 to 50/75/100/125/150/175/200
 	- 4 skill damage changed from 130/160/190/220/250/280/310 to 200/300/400/500/600/700/800

Medusa
	- Cold Blooded Cooldown changed from 6 to 10

Marci
	- 4 skill Cooldown changed from 110/100/90/80/70/60/50 to 80/75/70/65/60/55/50
	- 4 skill between flurries changed from 1.75 to 1.55/1.50/1.45/1.40/1.35/1.30/1.25
	- 4 skill attack Stacks changed from 3/4/5/6/7/8/9 to 4/5/6/7/8/9/10
	- talent 25lvl silence duration changed from 1.5sec to 0.5sec

Primal Beast
	- Added to Angel Arena

Techies
	- Added techies skill frm dota

Undying
	- 4 skill Cooldown changed from 40 to 60
	- Shard Cooldown ultimate changed from 35 to 20

Item changes:

Tome of heroes
	- stack start game 5
	- delay before the start of the game 600sec
	- Max stack 40
	- Cooldown stack 20sec
	- Cost changed from 1250 to 1500

Ethereal Blade
	- Craft changed from Ghost scepter + Recipe to Mystic staff + Ghost scepter + Recipe

Gem
	- cast range changed from 300 to 500
	- active skill radius changed from 300 to 500
	- duration active skill changed from 4 to 8
	- Cooldown active skill changed from 12 to 30

Bosses:

Keymaster
	- now Ignores terrain
	- ms changed from 365 to 400

Creeps:

Satyr hand
	- 3 skill magic amplify changed from 50 to 20

Fixes:
Storm Spirit 1 skill damage fixed
Earth Spirit ultimate fixed
Elder Titan ultimate fixed
Abyssal Underlord ultimate fixed
Omniknight 3 skill and ultimate fixed
Pudge 3 skill fixed
Templar Assassin 3 skill fixed
Shadow Fiend aghanim fixed
Hoodwink shard skill fixed
Morphlimg 1 skill fixed
Swift blink range fixed
Overwhelming blink range fixed
Arcane blink range fixed

---
## [Mi5Devs/android_kernel_xiaomi_msm8996](https://github.com/Mi5Devs/android_kernel_xiaomi_msm8996)@[f3575ca724...](https://github.com/Mi5Devs/android_kernel_xiaomi_msm8996/commit/f3575ca7248b2e019c875c0d522f1698ea5de7bb)
#### Friday 2022-10-14 16:39:04 by Christian Brauner

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
## [argrath/NetHack](https://github.com/argrath/NetHack)@[b02e018225...](https://github.com/argrath/NetHack/commit/b02e01822564e5bee3c31082e978419edea6a37c)
#### Friday 2022-10-14 17:41:55 by Michael Meyer

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
## [OneAsianTortoise/tgstation](https://github.com/OneAsianTortoise/tgstation)@[f923f61011...](https://github.com/OneAsianTortoise/tgstation/commit/f923f6101103e4ff1aeefd57d0531a3bc437a77a)
#### Friday 2022-10-14 17:57:23 by MMMiracles

Tramstation: Modular Maintenance Insanity (#69000)

About The Pull Request
Every single part of maintenance has been segmented into modules with multiple variants with different themes. As it stands, there are currently 80 modular parts that come together to form the entire maintenance layout for both levels. Part 1 of a 2 part PR set, requires #69486 to have full effect.

Why It's Good For The Game
Maintenance as it stands is a bit barren, not much reason to explore it with boring same-same rooms despite current randomized modules. With these issues in mind, I completely scrapped maintenance as it was and rebuilt it in mind with full modular segments with proper documentation on what each piece is and where it is located. These changes were also designed to make maintenance more friendly for our dark-dwelling antags and xenos alike, as each major module now has an air vent and scrubber.

Fixes #68320

Main Event:

Every single part of maintenance was turned into module chunks. Sections of the map that originally had maintenance was traced out with checkered flooring so mappers can still see the general layout of the tunnels when making larger edits.
Every module has been documented with proper nodes with descriptions of where each module is located on the map.
Each main module has a regular variant and an abandoned variant. Abandoned variants have blocked access routes and look more like unfinished carved out tunnels than regular maintenance.
Each module has 2 attachment points barring 2. Each attachment has 3 potential layouts that are chosen each round. A storage room with construction supplies one round might be a carved out room with minerals the next.
QoL/General Fixes:

Maintenance should have much more xeno/antag spawns to give various mid-round antags better chances at starting.
Camera network has been given a once-over with duplicate/floating cameras fixed.
The helpful bots in the lower tunnel should now actually do full rotations instead of whatever the hell they were doing before.
I still need to do some testing with disposals and final touch ups to make sure there aren't any weird overlaps, but as of right now the actual mapping quality is ready for review.

---
## [brianwang30/SoftDev](https://github.com/brianwang30/SoftDev)@[3675888ddd...](https://github.com/brianwang30/SoftDev/commit/3675888dddb5b0986e10c6d055bf06f2e1dd8434)
#### Friday 2022-10-14 18:05:46 by brianwang30

how long of an input does the text query accept? I'm interested. Usually I would never make a username this long, but I suppose this instance is different. But exceptions make for the best stories. I remember 5 years ago, when I ate a whole bag of sour patch kid gummies. I would usually never eat a whole pack of sour patch kid gummies, but I decided to that day because I felt like making an exception. As I was happily wolfing down the bag, my tongue began to sting. The sour patch kid gummies were, indeed, sour patch kid gummies, instead of sweet patch kid gummies, or alive patch kid gummies. Being the dumbass that I was and am, however, I decided to soldier on and continue eating more sour patch kid gummies. The sour patch kid gummies each fought for their life, burning my tongue with their sour acidic blood. Eventually, by the end, my teeth hurt, my tongue burned, and I had a very horrible experience. I would not advise anybody to eat a whole sour patch kid bag of gummies, unless they too want teeth pain. Or maybe I just have sensensitive teeth. This reminds me of that time I ate a whole pineapple. An entire pineapple. With pineapple juice. I believe that the acidic pineapple slowly eroded my teeth armor, until my inner teeth were all outer teeth. So, like I would not advise eating a whole bag of sour patch kid gummies, I would also not advise eating a whole pineapple.

---
## [git/git](https://github.com/git/git)@[a88ba63cb3...](https://github.com/git/git/commit/a88ba63cb31970a5f5df973849d84ff62d0fcb36)
#### Friday 2022-10-14 19:10:38 by Ævar Arnfjörð Bjarmason

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
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [kleinerm/Psychtoolbox-3](https://github.com/kleinerm/Psychtoolbox-3)@[5e67e1c1c6...](https://github.com/kleinerm/Psychtoolbox-3/commit/5e67e1c1c696a2f5912a9e033cb8e78fa041f3bc)
#### Friday 2022-10-14 19:22:39 by Mario Kleiner

Screen/Linux/GLX: Rewrite PsychOSSetVBLSyncLevel() for best vsync control.

Mesa supports GLX_EXT_swap_control since Mesa 20.3.0, and the proprietary
drivers from NVidia since 2011, from ATI since 2013, so any non-ancient
Linux distro should have it for the same functionality as our previously
used GLX_MESA_swap_control on MESA, but more efficient, as it saves an
OpenGL context switch, and cross-vendor OSS and proprietary.

We keep the GLX_MESA_swap_control fallback, which should work on all
FOSS drivers since around 2003. For completeness also support the very
limited lowest common denominator fallback GLX_SGI_swap_control from before
the year 2000, assuming we'll never hit it ever again. It doesn't allow
query of actual swap interval, and worse, it doesn't allow zero swap
interval, so one can't programmatically disable vsync for benchmarking,
certain debugging and diagnostics, windowed NetWM timing or for
mirror mode with high efficiency - all thing that need vsync disable.

Now we fully rely on GLEW for detecting and setting up extensions instead
of a mix of GLEW, own extension queries and function pointer hackery. This
also removes that weird bug where vsync can't get disabled during the first
session after startup or clear Screen, clear all etc, but only on followup
runs. Turned out on first run, glXSwapIntervalSGI() was bound, which would
error out on vsync disable requests, but on successive runs, the proper
glXSwapIntervalMESA() was bound to the glXSwapIntervalSGI function pointer.
Weird, but true, as long debugging with the debugger showed. It baffles me
how this is possible at all?!? Probably weird interactions between our
pointer assignments, GLEW, and possible GL vendor neutral dispatch??

Anyway, this rewrite makes us more efficient and clean and fixes that
annoying bug.

We should get optimal swap control this way on MESA back to the year 2003,
and on NVidia/ATI proprietary back to the years 2011 (NVidia) and 2013 (AMD).

Tested on Intel + Mesa 21.2.6 Ubuntu 20.04.5-LTS so far.

---
## [newstools/2022-metro](https://github.com/newstools/2022-metro)@[2fcc6e07ca...](https://github.com/newstools/2022-metro/commit/2fcc6e07ca070ed6f7b19ef243aeac77f2cf9f95)
#### Friday 2022-10-14 20:30:04 by Billy Einkamerer

Created Text For URL [metro.co.uk/2022/10/14/i-hate-you-review-friday-night-dinner-writer-back-with-more-silliness-17567786/]

---
## [bellegarde-c/android_kernel_samsung_sdm670](https://github.com/bellegarde-c/android_kernel_samsung_sdm670)@[c265c44dbb...](https://github.com/bellegarde-c/android_kernel_samsung_sdm670/commit/c265c44dbb553c5e251fac4b1d103da16adfc7f9)
#### Friday 2022-10-14 20:41:50 by George Spelvin

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
Signed-off-by: Yousef Algadri <yusufgadrie@gmail.com>
Signed-off-by: Panchajanya1999 <panchajanya@azure-dev.live>
Signed-off-by: Zlatan Radovanovic <zlatan.radovanovic@fet.ba>

---
## [Kordasauter/roprime-simulator.com](https://github.com/Kordasauter/roprime-simulator.com)@[97f1e9a5dd...](https://github.com/Kordasauter/roprime-simulator.com/commit/97f1e9a5dd7c5e74d67b119770960e7a2ddb7d8d)
#### Friday 2022-10-14 22:40:32 by Kordasauter

Bio 5 update

14/10/2022:
Has been fixed :
Fixed error in Aura Blade formula
Fixed error in Vit Glove HP bonus
Fixed a typo on Temporal Luk Boot [1]
Fixed the Shadow Sura Glove's cooldown reduction for Rampage Blaster
Has been added :
The Royal Banquet Cards
Frozen Wolf Cards
Taffy Card
Watcher Card
Sky Fortress Invasion Cards
Room of Consciousness Equipments
City Map (Accessory)
Shining Holy Water (Accessory)
Royal Guard Shield
Prontera Badge (Accessory)
Flattery Robe
Abusive Robe
Spoon
Room of Consciousness Cards
Powerful Amdarais Card
Powerful Archer Skeleton Card
Powerful Skeleton Card
Powerful Soldier Skeleton Card
Bijou Card
Nightmare Glastheim Equipments
Cursed Book
Tomb of Honor Equipments and Enchants
Old Rune Circlet
Old Mitra
Old Driver Band (Red)
Old Driver Band (Yellow)
Old Shadow Handicraft
Old Maestro Song's Hat
Old Midas Whisper
Old Magic Stone Hat
Old Blazing Soul
Old Wind Whisper
Old Dying Swan
Old Camouflage Bunny Hood
Old Bone Circlet
Old Casket of Protection
Fallen Warrior Manteau
Tomb of Honor Cards
True Alphoccio Basil Card
True Celia Alde Card
True Chen Lio Card
True Eremes Guile Card
True Flamel Emure Card
True Gertie Wie Card
True Howard Alt-Eisen Card
True Kathryne Keyron Card
True Margaretha Sorin Card
True Randel Lawrence Card
True Seyren Windsor Card
True Cecil Damon Card
True Trentini Card
Maestro Alphoccio Card
Sorcerer Celia Card
Sura Chen Card
Guillotine Cross Eremes Card
Geneticist Flamel Card
Shadow Chaser Gertie Card
Mechanic Howard Card
Warlock Kathryne Card
Arch Bishop Margaretha Card
Royal Guard Randel Card
Rune Knight Seyren Card
Ranger Cecil Card
Wanderer Trentini Card

---
## [ejeba72/pizza_app](https://github.com/ejeba72/pizza_app)@[be1742e380...](https://github.com/ejeba72/pizza_app/commit/be1742e3806fbb7b461fb411eaad57a0b7e5e05b)
#### Friday 2022-10-14 22:55:12 by Emmanuel Eni

YesSss! I managed to "engineer" an algorithm to authenticate users. What I did was to carefully study the response header, and how to obtain what I want from it. Omo! I made loads of mistakes! It was like a roller coaster experience of frustration and triumph. \n\nFor instance, I am now familiar with "req.body". So I assumed that the equivalent for the request header, would be req.header (instead of req.headers). You need to see my frustration and utter confusion when I was yet to realise that it was a simple issue of appending an "s" to req.header. It took me a while to figure that out. \n\nFurthermore, I had to figure out precisely how to retrieve a document from the user collection using the username item (Na only find() and findById() I sabi before now). Also, the fact that the document came wrapped in an array cause confusion too. I no go fit continue this story. \n\nBut the long and short of it, is that my logical and rational faculty was firing on all cylinders as I delicately figured out each step I took to create a very simple authencation algorithm. I acknowledge that the aforementioned algorithm is not secured enough (for instance, I did not hash the user passwords). \n\nHowever, it was surely a beautiful learning experience for me. Moreover, I haven't completed work on it o! What I have done is to carefully conduct an experiment on only the "Get-All" order route, to ascertain if the idea I had in my head was even possible at all. Now that it worked, my next palaver is to see how I can put the authentication algorithm in a module. And apply it to all the http methods in the order route, without repeating code, unnecessarily.

---
## [DesmontTiney/tgstation](https://github.com/DesmontTiney/tgstation)@[d34fa4c642...](https://github.com/DesmontTiney/tgstation/commit/d34fa4c642839215df5ba985d098a04e4d555b5b)
#### Friday 2022-10-14 23:18:47 by LemonInTheDark

Macro optimizes SSmapping saving 50%  (#69632)

* 'optimizes' space transitions by like 0.06 seconds, makes them easier to read tho, so that's an upside

* ''''optimizes'''' parsed map loading

I'm honestly not sure how big a difference this makes, looked like small
percentage points if anything
It's a bit more internally concistent at least, which is nice. Also I
understand the system now.

I'd like to think it helped but I think this is kinda a "do you think
it's easier to read" sort of situation. if it did help it was by the
skin of its teeth

* Saves 0.6 seconds off loading meta and lavaland's map files

This is just a lot of micro stuff.
1: Bound checks don't need to be inside for loops, we can instead bound the iteration counts
2: TGM and DMM are parsed differently. in dmm a grid_set is one z level,
   in tgm it's one collumn. Realizing this allows you to skip copytexts and
   other such silly in the tgm implemenentation, saving a good bit of time
3: Min/max bounds do not need to be checked inside for loops, and can
   instead be handled outside of them, because we know the order of x
   and y iteration. This saves 0.2 seconds

I may or may not have made the code harder to read, if so let me know
and I'll check it over.

* Micro ops key caching significantly. Fixes macros bug

inserting \ into a dmm with no valid target would just less then loop
the string. Dumb

Anyway, optimizations. I save a LOT of time by not needing to call
find_next_delimiter_position for every entry and var set. (like maybe 0.5
seconds, not totally sure)
I save this by using splittext, which is significantly faster. this
would cause parsing issues if you could embed \n into dmms, but you
can't, so I'm safe.

Lemme see uh, lots of little things, stuff that's suboptimal or could be
done cheaper. Some "hey you and I both know a \" is 2 chars long sort of
stuff

I removed trim_text because the quote trimming was never actually used,
and the space trimming was slower then using the code in trim. I also
micro'd trim to save a bit of time. this saves another maybe 0.5.

Few other things, I think that's the main of it. Gives me the fuzzy
feelings

* Saves 50% of build_coordinate's time

Micro optimizing go brrrrr
I made turf_blacklist an assoc list rather then just a normal one, so
lookups are O(log n) instead of O(n). Also it's faster for the base case
of loading mostly space.

Instead of toggling the map loader right before and right after New()
calls, we toggle at the start of mapload, and disable then reenable if
we check tick. This saves like 0.3 seconds

Rather then tracking an area cache ourselves, and needing to pass it
around, we use a locally static list to reference the global list of
area -> type. This is much faster, if slightly fragile.

Rather then checking for a null turf at every line, we do it at the
start of the proc and not after. Faster this way, tho it can in theory
drop area vvs.

Avoids calling world.preloader_setup unless we actually have a unique
set of attributes. We use another static list to make this comparison
cheap. This saves another 0.3

Rather then checking for area paths in the turf logic, or vis versa, we
assume we are creating the type implied by the index we're reading off.
So only the last type entry will be loaded like a turf, etc.
This is slightly unsafe but saves a good bit of time, and will properly
error on fucked maps.

Also, rather then using a datum to hold preloader vars, we use 2 global
variables. This is faster.

This marks the end of my optimizations for direct maploading. I've
reduced the cost of loading a map by more then 50% now. Get owned.

* Adds a define for maploading tick check

* makes shuttles load again, removes some of the hard limits I had on the reader for profiling

* Macro ops cave generation

Cave generation was insanely more expensive then it had any right to be.
Maybe 0.5 seconds was saved off not doing a range(12) for EVERY SPAWNED
MOB.
0.14 was saved off using expanded weighted lists (A new idea of mine)
This is useful because I can take a weighted list, and condense it into
weight * path count. This is more memory heavy, and costs more to
create, but is so much faster then the proc.

I also added a naive implementation of gcd to make this a bit less bad.
It's not great, but it'll do for this usecase.

Oh and I changed some ChangeTurfs into New()s. I'm still not entirely
sure what the core difference between the two is, but it seems to work
fine.
I believe it's safe because the turf below us hasn't init'd yet, there's
nothing to take from them. It's like 3 seconds faster too so I'll be sad
when it turns out I'm being dumb

* Micros river spawning

This uses the same sort of concepts as the last change, mostly New being
preferable to ChangeTurf at this level of code.
This bit isn't nearly as detailed as the last few, I honestly got a bit
tired. It's still like 0.4 seconds saved tho

* Micros ruin loading

Turns out it saves time if you don't check area type for every tile on a
ruin. Not a whole ton faster, like 0.03, but faster.

Saves even more time (0.1) to not iterate all your ruin's turfs 3 times
to clear away lavaland mobs, when you're IN SPACE who wrote this.

Oh it also saves time to only pull your turf list once, rather then 3
times

---

