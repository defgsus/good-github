## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-07-24](docs/good-messages/2023/2023-07-24.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,237,364 were push events containing 3,495,918 commit messages that amount to 292,618,387 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 67 messages:


## [JWCS/beartype](https://github.com/JWCS/beartype)@[214ffdb2e6...](https://github.com/JWCS/beartype/commit/214ffdb2e64ddd631ec7283ddddfb8fa34834449)
#### Monday 2023-07-24 00:36:14 by leycec

`README.rst` -> Read the Docs (RTD) x 20.

This commit is the next in a commit chain coercing our monolithic
`README.rst` documentation onto Read the Docs (RTD), en-route to
resolving issue #203 kindly submitted by @LittleBigGene (AKA the dynamo
of the cell). Specifically, this commit circumvents upstream theme
issues pydata/pydata-sphinx-theme#90, pydata/pydata-sphinx-theme#221,
and pydata/pydata-sphinx-theme#1181 with the "standard"
`_templates/sidebar-nav-bs.html` hack shamelessly copy-pasted into
literally *every* project requiring that theme. This includes @beartype,
because why not spew boilerplate that nobody understands everywhere?
Sadly, doing so now requires pinning to a maximum obsolete version of
this theme that will also surely die soon. And this is why I facepalm.
(*Illogical ontological topology!*)

---
## [vonchenplus/yuzu](https://github.com/vonchenplus/yuzu)@[8e703e08df...](https://github.com/vonchenplus/yuzu/commit/8e703e08dfcf735a08df2ceff6a05221b7cc981f)
#### Monday 2023-07-24 00:58:51 by comex

Implement SSL service

This implements some missing network APIs including a large chunk of the SSL
service, enough for Mario Maker (with an appropriate mod applied) to connect to
the fan server [Open Course World](https://opencourse.world/).

Connecting to first-party servers is out of scope of this PR and is a
minefield I'd rather not step into.

 ## TLS

TLS is implemented with multiple backends depending on the system's 'native'
TLS library.  Currently there are two backends: Schannel for Windows, and
OpenSSL for Linux.  (In reality Linux is a bit of a free-for-all where there's
no one 'native' library, but OpenSSL is the closest it gets.)  On macOS the
'native' library is SecureTransport but that isn't implemented in this PR.
(Instead, all non-Windows OSes will use OpenSSL unless disabled with
`-DENABLE_OPENSSL=OFF`.)

Why have multiple backends instead of just using a single library, especially
given that Yuzu already embeds mbedtls for cryptographic algorithms?  Well, I
tried implementing this on mbedtls first, but the problem is TLS policies -
mainly trusted certificate policies, and to a lesser extent trusted algorithms,
SSL versions, etc.

...In practice, the chance that someone is going to conduct a man-in-the-middle
attack on a third-party game server is pretty low, but I'm a security nerd so I
like to do the right security things.

My base assumption is that we want to use the host system's TLS policies.  An
alternative would be to more closely emulate the Switch's TLS implementation
(which is based on NSS).  But for one thing, I don't feel like reverse
engineering it.  And I'd argue that for third-party servers such as Open Course
World, it's theoretically preferable to use the system's policies rather than
the Switch's, for two reasons

1. Someday the Switch will stop being updated, and the trusted cert list,
   algorithms, etc. will start to go stale, but users will still want to
   connect to third-party servers, and there's no reason they shouldn't have
   up-to-date security when doing so.  At that point, homebrew users on actual
   hardware may patch the TLS implementation, but for emulators it's simpler to
   just use the host's stack.

2. Also, it's good to respect any custom certificate policies the user may have
   added systemwide.  For example, they may have added custom trusted CAs in
   order to use TLS debugging tools or pass through corporate MitM middleboxes.
   Or they may have removed some CAs that are normally trusted out of paranoia.

Note that this policy wouldn't work as-is for connecting to first-party
servers, because some of them serve certificates based on Nintendo's own CA
rather than a publicly trusted one.  However, this could probably be solved
easily by using appropriate APIs to adding Nintendo's CA as an alternate
trusted cert for Yuzu's connections.  That is not implemented in this PR
because, again, first-party servers are out of scope.

(If anything I'd rather have an option to _block_ connections to Nintendo
servers, but that's not implemented here.)

To use the host's TLS policies, there are three theoretical options:

a) Import the host's trusted certificate list into a cross-platform TLS
   library (presumably mbedtls).

b) Use the native TLS library to verify certificates but use a cross-platform
   TLS library for everything else.

c) Use the native TLS library for everything.

Two problems with option a).  First, importing the trusted certificate list at
minimum requires a bunch of platform-specific code, which mbedtls does not have
built in.  Interestingly, OpenSSL recently gained the ability to import the
Windows certificate trust store... but that leads to the second problem, which
is that a list of trusted certificates is [not expressive
enough](https://bugs.archlinux.org/task/41909) to express a modern certificate
trust policy.  For example, Windows has the concept of [explicitly distrusted
certificates](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn265983(v=ws.11)),
and macOS requires Certificate Transparency validation for some certificates
with complex rules for when it's required.

Option b) (using native library just to verify certs) is probably feasible, but
it would miss aspects of TLS policy other than trusted certs (like allowed
algorithms), and in any case it might well require writing more code, not less,
compared to using the native library for everything.

So I ended up at option c), using the native library for everything.

What I'd *really* prefer would be to use a third-party library that does option
c) for me.  Rust has a good library for this,
[native-tls](https://docs.rs/native-tls/latest/native_tls/).  I did search, but
I couldn't find a good option in the C or C++ ecosystem, at least not any that
wasn't part of some much larger framework.  I was surprised - isn't this a
pretty common use case?  Well, many applications only need TLS for HTTPS, and they can
use libcurl, which has a TLS abstraction layer internally but doesn't expose
it.  Other applications only support a single TLS library, or use one of the
aforementioned larger frameworks, or are platform-specific to begin with, or of
course are written in a non-C/C++ language, most of which have some canonical
choice for TLS.  But there are also many applications that have a set of TLS
backends just like this; it's just that nobody has gone ahead and abstracted
the pattern into a library, at least not a widespread one.

Amusingly, there is one TLS abstraction layer that Yuzu already bundles: the
one in ffmpeg.  But it is missing some features that would be needed to use it
here (like reusing an existing socket rather than managing the socket itself).
Though, that does mean that the wiki's build instructions for Linux (and macOS
for some reason?) already recommend installing OpenSSL, so no need to update
those.

 ## Other APIs implemented

- Sockets:
    - GetSockOpt(`SO_ERROR`)
    - SetSockOpt(`SO_NOSIGPIPE`) (stub, I have no idea what this does on Switch)
    - `DuplicateSocket` (because the SSL sysmodule calls it internally)
    - More `PollEvents` values

- NSD:
    - `Resolve` and `ResolveEx` (stub, good enough for Open Course World and
      probably most third-party servers, but not first-party)

- SFDNSRES:
    - `GetHostByNameRequest` and `GetHostByNameRequestWithOptions`
    - `ResolverSetOptionRequest` (stub)

 ## Fixes

- Parts of the socket code were previously allocating a `sockaddr` object on
  the stack when calling functions that take a `sockaddr*` (e.g. `accept`).
  This might seem like the right thing to do to avoid illegal aliasing, but in
  fact `sockaddr` is not guaranteed to be large enough to hold any particular
  type of address, only the header.  This worked in practice because in
  practice `sockaddr` is the same size as `sockaddr_in`, but it's not how the
  API is meant to be used.  I changed this to allocate an `sockaddr_in` on the
  stack and `reinterpret_cast` it.  I could try to do something cleverer with
  `aligned_storage`, but casting is the idiomatic way to use these particular
  APIs, so it's really the system's responsibility to avoid any aliasing
  issues.

- I rewrote most of the `GetAddrInfoRequest[WithOptions]` implementation.  The
  old implementation invoked the host's getaddrinfo directly from sfdnsres.cpp,
  and directly passed through the host's socket type, protocol, etc. values
  rather than looking up the corresponding constants on the Switch.  To be
  fair, these constants don't tend to actually vary across systems, but
  still... I added a wrapper for `getaddrinfo` in
  `internal_network/network.cpp` similar to the ones for other socket APIs, and
  changed the `GetAddrInfoRequest` implementation to use it.  While I was at
  it, I rewrote the serialization to use the same approach I used to implement
  `GetHostByNameRequest`, because it reduces the number of size calculations.
  While doing so I removed `AF_INET6` support because the Switch doesn't
  support IPv6; it might be nice to support IPv6 anyway, but that would have to
  apply to all of the socket APIs.

  I also corrected the IPC wrappers for `GetAddrInfoRequest` and
  `GetAddrInfoRequestWithOptions` based on reverse engineering and hardware
  testing.  Every call to `GetAddrInfoRequestWithOptions` returns *four*
  different error codes (IPC status, getaddrinfo error code, netdb error code,
  and errno), and `GetAddrInfoRequest` returns three of those but in a
  different order, and it doesn't really matter but the existing implementation
  was a bit off, as I discovered while testing `GetHostByNameRequest`.

  - The new serialization code is based on two simple helper functions:

    ```cpp
    template <typename T> static void Append(std::vector<u8>& vec, T t);
    void AppendNulTerminated(std::vector<u8>& vec, std::string_view str);
    ```

    I was thinking there must be existing functions somewhere that assist with
    serialization/deserialization of binary data, but all I could find was the
    helper methods in `IOFile` and `HLERequestContext`, not anything that could
    be used with a generic byte buffer.  If I'm not missing something, then
    maybe I should move the above functions to a new header in `common`...
    right now they're just sitting in `sfdnsres.cpp` where they're used.

- Not a fix, but `SocketBase::Recv`/`Send` is changed to use `std::span<u8>`
  rather than `std::vector<u8>&` to avoid needing to copy the data to/from a
  vector when those methods are called from the TLS implementation.

---
## [Latentish/Shiptest](https://github.com/Latentish/Shiptest)@[f07cb3bd3b...](https://github.com/Latentish/Shiptest/commit/f07cb3bd3b52bfbdb7994aaf4ae68dcf90d57d2f)
#### Monday 2023-07-24 01:20:09 by Bjarl

Overmap 4.7: Gas Giants, More Storms, 8 hours of work (#1997)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Adds some content based on sprites I saw sitting around in the overmap
file, mainly carp storms and dust storms.
Carp storms throw space carp at you. Dust storms throw dust.

Also adds gas giants, a place to harvest gasses if you're low, and don't
want to stop at a planet. They *should* be persistent. Your average gas
giant mix is very cold, very high pressure, and absolutely not something
you want to breathe. Plasma giants are cold and allow harvesting of
plasma.

Electrical storms have been rebalanced to not Explode Your Ship. Minor
and Moderate ones will now only shock and damage objects and mobs, major
ones will still explode you, so remain careful.



![image](https://github.com/shiptest-ss13/Shiptest/assets/94164348/84257435-32de-45a5-8a8d-d9aa30021f90)
Example overmap with some carp migrations.


https://github.com/shiptest-ss13/Shiptest/assets/94164348/5c30fa9a-c7e4-453a-99a6-5c3564946b26
flying through a minor electrical storm


https://github.com/shiptest-ss13/Shiptest/assets/94164348/db7fcdf0-3f7a-4830-821e-a4a7106632ba
gas giant


https://github.com/shiptest-ss13/Shiptest/assets/94164348/0a5f0575-b7d9-4e3f-9e13-942a8fdf8617

![image](https://github.com/shiptest-ss13/Shiptest/assets/94164348/6bb5ddc2-373a-4dd9-9a63-0f6f0bdd26a9)

plasma giant

https://github.com/shiptest-ss13/Shiptest/assets/94164348/9268c293-39f3-4306-889e-f8c19067cec1

A particularly dusty solar system

![image](https://github.com/shiptest-ss13/Shiptest/assets/94164348/5b27e2a8-1cc1-47bb-95b8-e9d5c3ba8e71)


I might try and fix ion storms but I don't see what might be breaking
them.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
More content for the overmap / balancing out some old systems
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Planets now can (and will) play a sound when you land on them
add: Gas / Plasma giants, cold, dockable worlds with absolutely no
livable surfaces. As a matter of fact it's all chasm. All highly
pressurized, gas rich, chasm.
add: Dust storms and carp storms now grace the sector. 
add: physical storms (dust, carp, asteroid), will now only trigger if
you go through them too fast. Take it easy and you might get through
unscathed.
add: planets will now have a name on the overmap
add: overmap hazards now have a description
tweak: Space carp can now survive in hyperspace, their natural habitat
balance: minor and moderate electrical storms will no longer Explode you
balance: asteroid storm lists have been trimmed of Extremely Deadly ones
fix: restores planet naming behavior, I believe this was unintentionally
removed at some point
fix: Ion storms work again. Fuck you whoever touched them last.
soundadd: planet_landing_1 and planet_landing_2, (tech_notification and
sos_morse_code from CM respectively. I don't know how to attribute
properly please tell me how if you have issue with this attribution
because I did not make these sounds they're from Colonial Marines)
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: Bjarl <94164348+Bjarl@users.noreply.github.com>

---
## [Drulikar/cmss13](https://github.com/Drulikar/cmss13)@[1d28964d37...](https://github.com/Drulikar/cmss13/commit/1d28964d37f9b95773580cca3471a2a4f5c03eb0)
#### Monday 2023-07-24 01:48:40 by naut

New blood bags (#3961)

# About the pull request

Since we're putting so much emphasis on blood bags lately, I figured I
might as well do my part as spriter and add actual _labels_ to the
things so you can tell what they are at a glance. Also overhauled the
system to use overlays and underlays instead of the cursed
`full/half/empty` thing that it had going beforehand.

# Explain why it's good for the game

You now no longer have to manually inspect blood bags to tell what type
they are! Rejoice.

# Testing Photographs and Procedure
<img width="251" alt="image"
src="https://github.com/cmss13-devs/cmss13/assets/55491249/c4424ec3-bfe6-4d58-8915-595b468a7606">

_Blood bags in action. Sort of. Yes, they actually change color now._

<img width="571" alt="image"
src="https://github.com/cmss13-devs/cmss13/assets/55491249/3b478c65-54b9-4321-bf02-dcfacaf1ad23">

_Icon states! Also sprinkled in some yet-unused labels for future
use(TM). AB types are here, too, because I forgot they weren't in the
game._
# Changelog

:cl: nauticall
imageadd: Resprited blood bags to look nicer and use proper a proper
overlay/underlay system. Their types are also now distinguishable at a
glance.
code: Reworked the way blood bag sprites work behind the scenes to use
the overlay/underlay system.
/:cl:

---
## [SoeunKimsong/StudentAttendanceProject](https://github.com/SoeunKimsong/StudentAttendanceProject)@[925ea72ea3...](https://github.com/SoeunKimsong/StudentAttendanceProject/commit/925ea72ea314703af3c9774e53606a062d8d9ec0)
#### Monday 2023-07-24 02:04:16 by kim_songular

Merge pull request #4 from SoeunKimsong/brovit

lol fuck you

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[2b2a01dfae...](https://github.com/treckstar/yolo-octo-hipster/commit/2b2a01dfaebfc4fdbbd458b4d4e825d0546aadac)
#### Monday 2023-07-24 02:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[f8054819a5...](https://github.com/TaleStation/TaleStation/commit/f8054819a5ecb7f7e3c8d3c21d95f3341356b44a)
#### Monday 2023-07-24 03:20:00 by TaleStationBot

[MIRROR] [MDB IGNORE] Adds in the smoothbore disablers. (#6844)

Original PR: https://github.com/tgstation/tgstation/pull/76773
-----
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

---------

Co-authored-by: CRITAWAKETS <sebastienracicot@hotmail.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[7e29b9ef63...](https://github.com/TaleStation/TaleStation/commit/7e29b9ef63fa1674b30e1b3298d7aef8e9c1805b)
#### Monday 2023-07-24 03:20:00 by TaleStationBot

[MIRROR] [MDB IGNORE] Adds a new positive quirk, "Spacer Born".  (#6840)

Original PR: https://github.com/tgstation/tgstation/pull/76809
-----
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

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [Hatterhat/Skyrat-tg](https://github.com/Hatterhat/Skyrat-tg)@[dcd2d0e418...](https://github.com/Hatterhat/Skyrat-tg/commit/dcd2d0e418fbd85c3e990a02f61ab05d2993e1e1)
#### Monday 2023-07-24 03:55:46 by SkyratBot

[MIRROR] Adds a wizard Right and Wrong that lets the caster give one spell (or relic) to everyone on the station [MDB IGNORE] (#22637)

* Adds a wizard Right and Wrong that lets the caster give one spell (or relic) to everyone on the station (#76974)

## About The Pull Request

This PR adds a new wizard ritual (the kind that require 100 threat on
dynamic)

This ritual allows the wizard to select one spellbook entry (item or
spell), to which everyone on the station will be given or taught said
spell or item. If the spell requires a robe, the spell becomes robeless,
and if the item requires wizard to use, it makes it usable. Mostly.

- Want an epic sword fight? Give everyone a high-frequency blade

- One mindswap not enough shenanigans for you? Give out mindswap

- Fourth of July? Fireball would be pretty hilarious...

The wizard ritual costs 3 points plus the cost of whatever entry you are
giving out. So giving everyone fireball is 5 points.

It can only be cast once by a wizard, because I didn't want to go
through the effort to allow multiple in existence

## Why It's Good For The Game

Someone gave me the idea and I thought it sounded pretty funny as an
alternative to Summon Magic

Maybe I make this a Grand Finale ritual instead / in tandem? That's also
an idea.

## Changelog

:cl: Melbert
add: Wizards have a new Right and Wrong: Mass Teaching, allowing them to
grant everyone on the station one spell or relic of their choice!
/:cl:

* Adds a wizard Right and Wrong that lets the caster give one spell (or relic) to everyone on the station

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[69a3c4440e...](https://github.com/treckstar/yolo-octo-hipster/commit/69a3c4440e8c45c3e242066c1f6c6cc6edbd6c85)
#### Monday 2023-07-24 04:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [TheNeoGamer42/Skyrat-tg](https://github.com/TheNeoGamer42/Skyrat-tg)@[9701b40ca0...](https://github.com/TheNeoGamer42/Skyrat-tg/commit/9701b40ca03e164bd8bd4238fafb6cf778c52efe)
#### Monday 2023-07-24 05:15:02 by SkyratBot

[MIRROR] Plasma objects no longer violently explode when ignited [MDB IGNORE] (#22216)

* Plasma objects no longer violently explode when ignited (#76492)

## About The Pull Request
This is one of those "can I get away with making a change I want" PRs.

I actually didn't know this had been changed before as it's not exactly
something I mess with often, but I really think it sucks. Plasma stuff
is supposed to ignite and cause fires, not explode (unless in a TTV). I
noticed this when I was poking around and found out that apparently
Disco Inferno just explodes now instead of setting on fire which also
sucks.

I figure there's a few fixes for this problem:

1) Nerf how hard plasma stuff explodes. This is an option, but I kind of
dislike that it does it at all more than anything. The biggest issue is
that just the regular statues explode with 20 LIGHT, which is pretty
fucking massive and basically just delimbs everyone around. I'd have to
nerf it HARD for it to get anywhere near what I think is acceptable.
2) Make a snowflake version of the statue that just ignites on hit with
a torch. I also don't like this because it'll make people think the
regular statues don't explode.
3) This option, which I think is cleaner and just makes sense compared
to the others.

I don't know if @ vincentiusvin still codes, but as far as I can tell
this was their doing, so it's only fair they get to speak up.

Fixes #71894

## Why It's Good For The Game
I don't like it, I think it goes against what we're used to for plasma
stuff (that it starts fires, not makes explosions) and it makes one of
my favorite shuttles boring and stupid. That being said, I'm honestly
not going to fight for this too hard if a lot of people like it, but I
am - as always - open to alternatives.

## Changelog
:cl: Vekter
del: Plasma objects (statues, toilets, etc.) no longer explode when
ignited. They just release plasma like everything else plasma. (This
doesn't impact injecting plasma into cells or dipping cigars in plasma,
those still explode.)
/:cl:

* Plasma objects no longer violently explode when ignited

---------

Co-authored-by: Vekter <TheVekter@users.noreply.github.com>

---
## [TheNeoGamer42/Skyrat-tg](https://github.com/TheNeoGamer42/Skyrat-tg)@[2303c452c7...](https://github.com/TheNeoGamer42/Skyrat-tg/commit/2303c452c79a8563076a58ad7e9d9346186a7e7c)
#### Monday 2023-07-24 05:15:02 by SkyratBot

[MIRROR] Rat RP expansion [MDB IGNORE] (#22204)

* Rat RP expansion (#76455)

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

* Rat RP expansion

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [OrionTheFox/tgstation](https://github.com/OrionTheFox/tgstation)@[cfd40aeef5...](https://github.com/OrionTheFox/tgstation/commit/cfd40aeef5dc1e051e5937e43a69c1df3bb4eca1)
#### Monday 2023-07-24 05:35:29 by necromanceranne

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
## [pirate-party-uk/Pirate-Party-UK-Constitution](https://github.com/pirate-party-uk/Pirate-Party-UK-Constitution)@[b0e068f2d5...](https://github.com/pirate-party-uk/Pirate-Party-UK-Constitution/commit/b0e068f2d5830943917508188855676faeb395d2)
#### Monday 2023-07-24 06:09:19 by PiratePartyUK

Create Inclusive Relationships, Sexual Orientations, and Gender Identity Policy.md

# Inclusive Relationships, Sexual Orientations, and Gender Identity Policy

## Introduction
This policy is intended to promote inclusivity, protect individual rights, and foster a society that embraces diversity in sexual orientations, gender identities, and relationship structures. It acknowledges the significance of respecting personal autonomy, recognizing diverse identities, and ensuring equal treatment and protection under the law for all individuals.

## Objective
The main objective of this policy is to establish legal recognition and protection for individuals with diverse sexual orientations, including asexual, aromantic, and polyamorous individuals, as well as intersex individuals. Additionally, the policy aims to recognize and safeguard the rights of non-binary individuals, offering them the option to refrain from declaring a gender for legal purposes.

## Key Features

### Legal Recognition and Protection
The policy proposes amending existing anti-discrimination laws to explicitly include asexual, aromantic, polyamorous, and intersex individuals, as well as non-binary individuals, as protected groups. This step will ensure their rights are safeguarded across various aspects of life, such as employment, education, healthcare, and public services. Moreover, the policy advocates for respecting the right of intersex individuals to identify their gender without coercion and without unnecessary medical interventions.

### Comprehensive Education and Awareness
To dispel myths and foster understanding and acceptance, the policy advocates for implementing inclusive and accurate sex education. This educational approach will cover diverse sexual orientations, gender identities, relationship structures, and intersex variations. Additionally, awareness campaigns will be promoted to highlight the experiences and challenges faced by individuals with diverse identities, aiming to combat stigma and discrimination.

### Protection from Harmful Practices
The policy takes a strong stance against harmful practices such as conversion therapy and other attempts to alter an individual's sexual orientation, gender identity, or relationship structure. It also calls for prohibiting non-consensual medical interventions on intersex infants and children, ensuring that any medical procedures are medically necessary and conducted with informed consent.

### Privacy and Confidentiality
Respecting individual privacy is crucial. The policy emphasizes safeguarding the medical history and intersex status of individuals, ensuring that sensitive information is not disclosed without informed consent. Additionally, individuals in consensual polyamorous relationships will be protected from intrusive questioning about their relationship structure.

## Implementing Additional Support

### Healthcare and Mental Health Support
The policy advocates for ensuring access to sensitive and inclusive healthcare services that cater to the needs of individuals with diverse sexual orientations, gender identities, and intersex variations without any judgment or prejudice. Additionally, mental health resources will be provided to address the specific challenges and experiences faced by individuals with diverse identities.

### Representation and Inclusivity
Diverse representation plays a vital role in promoting inclusivity. The policy encourages media, literature, and other forms of representation to reflect the full spectrum of human diversity in sexual orientations, gender identities, and relationship structures. Furthermore, the active participation of individuals with diverse identities, including asexual, aromantic, polyamorous, intersex, and non-binary individuals, in policymaking processes will be encouraged to ensure their voices are heard and their rights are considered.

### Building Supportive Communities
Supportive communities can play a significant role in fostering understanding and providing a sense of belonging. The policy recommends providing support and resources for individuals with diverse sexual orientations, gender identities, and relationship structures, such as intersex individuals and those in asexual, aromantic, polyamorous, and non-binary relationships, to connect with others who share similar experiences and challenges.

## Conclusion
This comprehensive policy aims to create a society that celebrates and respects the rights and dignity of all individuals, irrespective of their sexual orientations, gender identities, or relationship structures. By implementing legal protections, inclusive education, and support systems, we can pave the way for an inclusive and accepting environment where diversity is celebrated and discrimination is eradicated.

---
## [Hatterhat/tgstation](https://github.com/Hatterhat/tgstation)@[7e1d97af9e...](https://github.com/Hatterhat/tgstation/commit/7e1d97af9e4b6b7f90fbacc754fae939b6d16e49)
#### Monday 2023-07-24 06:29:48 by Justice

Removes the word "chemical" from "chemical patch" (#76966)

## About The Pull Request
In #76011, I bitched and moaned about how the ChemMaster gives patches a
huge ass name. I've talked to other Medical Doctor mains and I also
heard bitching about the word "chemical", which is just a pain in the
ass. It seems many of us just end up removing it because it's so
repetitive and makes the patch's name long fnr. I don't think the word
"chemical" is really needed in there since you can clearly tell it's a
chemical patch just by looking at the word "patch" and the sprite.

I don't think this should affect anything else in the game in a negative
way. In that same issue, it was suggested that the cap for names was
increased instead, but this also solves the issue of the word "chemical"
taking up so much space in the patch's name without touching unknown
lands.
## Why It's Good For The Game
Less words, more healing!
## Changelog
:cl:
qol: The word "chemical" has been removed from "chemical patch" when
printing patches
/:cl:

---
## [naota/linux](https://github.com/naota/linux)@[ff7ddcf0db...](https://github.com/naota/linux/commit/ff7ddcf0db48a7d9ae536eb0875428117be1d1f1)
#### Monday 2023-07-24 07:05:34 by Linus Torvalds

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
## [ancient-engineer/Monkestation2.0](https://github.com/ancient-engineer/Monkestation2.0)@[79e07c00db...](https://github.com/ancient-engineer/Monkestation2.0/commit/79e07c00db8607513347f8e7e6f2a8520e563680)
#### Monday 2023-07-24 08:28:55 by Aeri

fucking wacky ass goddamn cargo order console locations fixed

---
## [FernandoJ8/tgstation](https://github.com/FernandoJ8/tgstation)@[52c8da7ea4...](https://github.com/FernandoJ8/tgstation/commit/52c8da7ea49ef566c9a997a4b7cfc5d3d2a59178)
#### Monday 2023-07-24 08:50:56 by Jacquerel

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
## [anupamakate/Customer-Personality-Analysis-for-Increment-in-Super-Market-Sales](https://github.com/anupamakate/Customer-Personality-Analysis-for-Increment-in-Super-Market-Sales)@[f0b6c30c3f...](https://github.com/anupamakate/Customer-Personality-Analysis-for-Increment-in-Super-Market-Sales/commit/f0b6c30c3fb4fbb2b4a07d52466085db15d47244)
#### Monday 2023-07-24 08:59:49 by Anupama Kate

Boosting Supermarket Sales with Customer Personality Analysis

Abstract:
In this data science project, we aim to leverage customer personality analysis to enhance sales and customer engagement in a supermarket setting. By understanding the underlying behavioral patterns and preferences of different customer segments, we can tailor marketing strategies, improve product placements, and optimize the overall shopping experience to boost sales and customer satisfaction. This project will utilize advanced data science techniques and machine learning algorithms to analyze customer data, extract meaningful insights, and develop personalized marketing approaches.

Objectives:
1. Analyze customer purchasing patterns and behaviors to identify distinct customer segments.
2. Perform personality analysis using customer data to understand individual shopping preferences and tendencies.
3. Develop personalized marketing strategies for each customer segment to increase product relevance and engagement.
4. Optimize product placements and store layout based on customer preferences to enhance the shopping experience.
5. Measure the impact of personalized marketing interventions on supermarket sales and customer satisfaction.

Methodology:
1. Data Collection: Gather customer transaction data, loyalty program data, demographic information, and any available data related to customer behavior and preferences.
2. Data Preprocessing: Cleanse and preprocess the data to handle missing values, outliers, and data inconsistencies.
3. Customer Segmentation: Utilize clustering algorithms such as k-means, hierarchical clustering, or DBSCAN to group customers into distinct segments based on their purchasing behavior and demographics.
4. Personality Analysis: Apply natural language processing (NLP) techniques to analyze customer reviews, feedback, and social media posts to infer their personalities.
5. Personalized Marketing: Develop recommendation systems and targeted marketing approaches for each customer segment based on their personality traits and shopping preferences.
6. A/B Testing: Implement controlled experiments to measure the impact of personalized marketing interventions on sales and customer satisfaction.
7. Data Visualization: Create visualizations to communicate the findings effectively to stakeholders and decision-makers.

Expected Outcomes:
1. Identification of distinct customer segments with specific shopping behaviors and preferences.
2. Personalized marketing strategies tailored to each customer segment, resulting in improved product relevance and customer engagement.
3. Insights into the effectiveness of personalized marketing on supermarket sales and customer satisfaction.
4. Optimal product placements and store layout recommendations to enhance the shopping experience.
5. Recommendations for future marketing campaigns and strategies to sustain increased sales over time.

Conclusion:
By leveraging customer personality analysis and segmentation, this data science project aims to provide valuable insights into customer behavior, preferences, and motivations. The application of personalized marketing strategies based on these insights can lead to a significant increase in supermarket sales and customer satisfaction. Additionally, the project can guide supermarkets in optimizing store layouts and product placements, creating an overall more pleasant and efficient shopping experience for customers. Ultimately, the findings of this project will assist supermarkets in making data-driven decisions and gaining a competitive edge in the retail industry.

---
## [Toshayo/Hbm-s-Nuclear-Tech](https://github.com/Toshayo/Hbm-s-Nuclear-Tech)@[b443c3449d...](https://github.com/Toshayo/Hbm-s-Nuclear-Tech/commit/b443c3449d37db0017d86a1fe71cf92de3da026f)
#### Monday 2023-07-24 09:01:52 by Bob

fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you

---
## [ImCodist/super-mario-bros-rebuilt](https://github.com/ImCodist/super-mario-bros-rebuilt)@[65c6936899...](https://github.com/ImCodist/super-mario-bros-rebuilt/commit/65c69368997c78507787cdcb32a70caaeded62a2)
#### Monday 2023-07-24 09:09:01 by codist

Work in progress flag

ima go play issac now fuck you

---
## [rust-lang-ci/rust](https://github.com/rust-lang-ci/rust)@[994f4f6e2e...](https://github.com/rust-lang-ci/rust/commit/994f4f6e2e45bef4bebeeabee4e3d67b87727b91)
#### Monday 2023-07-24 09:38:26 by bors

Auto merge of #15290 - igorskyflyer:igorskyflyer-dx-install-extension, r=lnicola

editor/code: [DX] Use notification command links for debugger installation

This PR improves DX (developer experience) when installing the VS Code extension for the first time. When doing so and trying to debug a Rust file, we get an error notification that either CodeLLDB or C++ extension/debugger should be installed (see image below).

<div align="center">
	<img src="https://github.com/rust-lang/rust-analyzer/assets/20957750/e8ebeb1e-85f4-44e2-b79f-c48cf52e5f36" alt="Rust, prompt to install debug extension">
</div>

The PR enhances the links in the given notification and upon clicking instead of opening the Web page of the extension it installs the extension immediately, without the need to leave the editor.

Note: the feature needs to be refined, maybe an "install in progress" message or something similar, I left that for you guys to decide and implement. I think it also possible to first open the sidebar, open the Extensions tab, then run the extension installation command which would make it more user-friendly.

P.S. it is also possible to open the extension's details in VS Code directly via the same links and then the user would have to manually click on the Install button - if installation is not the desired behavior.

Happy coding! 🎉

---
## [pj64team/Project64-Legacy](https://github.com/pj64team/Project64-Legacy)@[9cf39149b7...](https://github.com/pj64team/Project64-Legacy/commit/9cf39149b744d3901fdbf1f81dff58655547c4cb)
#### Monday 2023-07-24 10:08:40 by Jay Oster

Remove Hidden Window and improve stability when resetting

The reset functionality is still very broken. Too many data races
between the GUI thread, CPU thread, and plugin threads.

This is at least a good start; resetting with F1 now works most of the
time. I can still get it to throw the "Emulation thread failed to
terminate plugins" error by hitting F1 ridiculously quickly with the
recompiler core. It doesn't seem to break as badly with the interpreter.

Anyway, yeah, this is just lack of synchronization causing havok.

The hidden window was some kind of ludicrous hack by a previous
contributor that attempted to hack around some other hacks, pile on some
more hacks to "fix" the broken hacks, and we get what we have today.

---
## [iloveyumyumshrimpnoodles/iloveyumyumshrimpnoodles](https://github.com/iloveyumyumshrimpnoodles/iloveyumyumshrimpnoodles)@[c3f72d6dca...](https://github.com/iloveyumyumshrimpnoodles/iloveyumyumshrimpnoodles/commit/c3f72d6dca4ea39922c13a22d7fedf9798723ed7)
#### Monday 2023-07-24 10:58:23 by iloveyumyumshrimpnoodles

Update README.md

fuck you github, with your shitty anti-spam system and fuck you microsoft, you greedy big tech fuckers

---
## [aryanofficialjain/Futuristic-3D-website](https://github.com/aryanofficialjain/Futuristic-3D-website)@[698260a8d6...](https://github.com/aryanofficialjain/Futuristic-3D-website/commit/698260a8d66047ccc44b88c236db808d6f806e93)
#### Monday 2023-07-24 12:03:51 by Aryan Jain

Create README.md

# Futuristic-3D-website

![Futuristic 3D Website](https://aryanofficialjain.github.io/Futuristic-3D-website/)

Welcome to the Futuristic 3D Website repository! This cutting-edge web project brings a whole new dimension to the online experience, showcasing stunning 3D visuals and delivering a seamless user journey. Elevate your web presence and captivate your audience with this immersive website.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Contributing](#contributing)
- [Support](#support)
- [License](#license)

## Introduction

The Futuristic 3D Website is a state-of-the-art web project that combines the latest web technologies to create an unparalleled user experience. With its captivating 3D graphics, smooth interaction, and mobile-first design, the website sets new standards in web development.

![Futuristic 3D Website Preview](https://your-website-url.com/preview.jpg)

## Features

- **Immersive 3D Visuals:** Engage your visitors with stunning 3D graphics that bring your content to life.
- **Smooth User Interaction:** Provide an intuitive and seamless user experience with fluid navigation.
- **Performance-Driven:** Enjoy fast loading times and exceptional responsiveness for enhanced user engagement.
- **Cross-Browser Compatibility:** Ensure consistent rendering across various browsers for a broader reach.
- **Mobile-First Design:** Optimize your website for mobile devices and reach a wider audience on the go.
- **SEO-Optimized:** Boost your search engine rankings and attract organic traffic with our SEO-friendly structure.

## Installation

Follow these steps to get Futuristic 3D Website up and running on your local environment:

1. Clone this repository to your local machine using `git clone https://github.com/your-username/Futuristic-3D-Website.git`.
2. Navigate to the project's root directory.
3. Open `index.html` in your web browser.

That's it! Your Futuristic 3D Website is now running locally.

## Usage

Customize the website's content and appearance to suit your needs. Edit the HTML files to update the page content, and modify the CSS files to tweak the design. We've designed this project to be user-friendly, so even those new to web development can easily make changes.

## Customization

Futuristic 3D Website is highly customizable. You can:

- Change color schemes, fonts, and layouts to match your branding.
- Integrate your own 3D models and graphics for a personalized touch.
- Add new sections or pages to showcase your content creatively.

## Contributing

We welcome contributions from the community to make Futuristic 3D Website even better. If you have suggestions, bug reports, or want to add new features, follow these steps:

1. Fork the repository to your GitHub account.
2. Create a new branch from the main branch with a descriptive name.
3. Make your changes and commit them with clear messages.
4. Push your branch to your forked repository.
5. Create a pull request to the main repository, explaining your changes.

Our team will review your contribution and merge it if it meets our guidelines.

## Support

If you encounter any issues or have questions, feel free to [open an issue](https://github.com/your-username/Futuristic-3D-Website/issues). We'll do our best to assist you.

## License

The Futuristic 3D Website is released under the [MIT License](https://opensource.org/licenses/MIT). You are free to use, modify, and distribute this project following the terms of the license.

---

Thank you for choosing Futuristic 3D Website! We hope this project brings a futuristic and delightful experience to your audience. Happy coding!

---
## [Kubisopplay/tgstation](https://github.com/Kubisopplay/tgstation)@[8788e48378...](https://github.com/Kubisopplay/tgstation/commit/8788e483788db2432b9649313efc9426d324379f)
#### Monday 2023-07-24 12:13:08 by Time-Green

Shuttle events (#76008)

## About The Pull Request


https://github.com/tgstation/tgstation/assets/7501474/a2d83ce8-eba1-42d9-a1f8-9d73f7c40b21

Adds shuttle events! Stuff can now start to happen outside the shuttle,
either benign or spicy (but usually just fun to watch)!
## Why It's Good For The Game

The shuttle escape sequence is an important part of the game, uniting
about every player surviving player. Recently, #71906 has made the
escape sequence more forgiving as well as more interesting by
conditionally doubling the playing field. The area outside the shuttle
is still mostly empty though, except for the few people being spaced,
daredevils and the occasional epic space fight.

This PR adds adds some space events to spice up the outside of the
shuttle! This both gives people something too look at, making the escape
sequence feel less static and more lively, as well as give people a
reason to go outside and get the full experience of ~being decapitated
by a meteor~ swimming with the fishes!

<details>
  <summary>Shuttle Events</summary>

**Friendly carp swarm**
Spawns a group of carp that flies past the shuttle, completely friendly
unless provoked.

**Friendly meteors**
Spawns a lot of strong meteors, but they all miss the shuttle.
Completely safe as long as you don't go EVA

**Maintenance debris**
Picks random stuff from the maintenance spawn pool and throws it at the
shuttle. Completely benign, unless you get hit in the head by a toolbox.
Could get you some cool stuff though!

**Dust storm**
Spawns a bunch of dust meteors. Has a rare chance to hit the shuttle,
doing minimal damage but can damage windows and might need inflight
maintenance

**Alien queen**
One in every 250 escapes. Spawns a player controlled alien queen and a
ripley mech. RIP AND TEAR!! Really not that dangerous when you realize
the entire crew is on the shuttle and the queen is fat as fuck, but can
still be fun to throw people around a bit before being torn to shreds.

**ANGRY CARP**
Once in every 500 escapes. Spawns 12 normal carp and 3 big carps, who
may just decide to go through the shuttle or try and bust through the
window if you look at them wrong. Somewhat dangerous, you could stay
away from the windows and try to hide, or more likely shoot at them and
weld the windows

**Fake TTV**
Lol

**Italian Storm**
Once in every 2000 rounds. Throws pasta, pizza and meatballs at the
shuttle. Definitely not me going off the rails with a testing event

**Player controlled carp trio**
Once in every 100 escapes. Spawns three player controlled carp to harass
the shuttle. May rarely be a magicarp, megacarp or chaos carp. I can't
honestly see them do anything other than be annoying for 3 seconds and
die

There are some other admin only ones: a group of passive carps going
directly through the shuttle and just being little shits, and a magic
carp swarm
</details>

Events are selected seperately, there isn't a crazy weighting system,
each just has a chance to run, and multiple could run at once. They also
don't immediately trigger, so people can get settled a bit, and to make
sure just waiting out the more dangerous ones is still a valid strategy.

## Changelog
:cl:
add: Adds shuttle events! If shuttle escapes weren't exciting before
(doubtful), they definitely are now! I'm joking it's mostly an
atmosphere thing.
admin: Adds an admin panel to interact with shuttle events, under the
Events tab: Change Shuttle Events
fix: Objects spawned in hyperspace will properly catch hyperspace drift
/:cl:

There's a few things I'd like to do later (another PR) (honestly anyone
can do them because I suck at follow-ups), because this is too big as
is:
- Hijack triggered shuttle events
- More events (got a lot of cool suggestions, but I'm putting most of
them on hold)
- Maybe stration announcements if some more dangerous ones get added
- Structures appearing next to the escape shuttle???

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [Dheeraj58627/TicTocToe_game](https://github.com/Dheeraj58627/TicTocToe_game)@[129329054a...](https://github.com/Dheeraj58627/TicTocToe_game/commit/129329054a00b1f197caef31e05697a1f0a925bc)
#### Monday 2023-07-24 12:32:53 by Dheeraj58627

Add files via upload

Tic-Tac-Toe Game Description:

Experience classic fun with our Tic-Tac-Toe game! Built using HTML, CSS, and JavaScript, this digital version of the beloved pen-and-paper game offers endless entertainment for players of all ages. Take turns with a friend  to see who can align three X's or O's in a row, column, or diagonal first. The minimalist design and intuitive interface make gameplay smooth and enjoyable. Whether you're a seasoned strategist or a casual gamer, our Tic-Tac-Toe game promises hours of nostalgic joy and friendly competition. Play now and relive the timeless excitement of this iconic pastime.

---
## [WRTN-Technologies/semantic-kernel](https://github.com/WRTN-Technologies/semantic-kernel)@[eab7a8f63a...](https://github.com/WRTN-Technologies/semantic-kernel/commit/eab7a8f63a0bfd289070e82b423ac78bd306ee5b)
#### Monday 2023-07-24 13:07:18 by Sailesh R

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
## [provinyl09/Car-Wrapping](https://github.com/provinyl09/Car-Wrapping)@[02613a3275...](https://github.com/provinyl09/Car-Wrapping/commit/02613a32751bb14391c9769c4709b9ac853bd96c)
#### Monday 2023-07-24 13:17:46 by provinyl09

My First Commit

Provinyl, your ultimate destination for professional car wrapping services that redefine automotive aesthetics. We are passionate about transforming vehicles into head-turning masterpieces through the art of car wrapping. Whether you're looking to add a touch of personalization, protect your car's original paint, or elevate your brand's identity with stunning vehicle graphics, Provinyl has you covered.

---
## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[74892ae7ec...](https://github.com/MTandi/tgstation/commit/74892ae7ec80d47c64bf786f62985a1bd07d06f7)
#### Monday 2023-07-24 13:21:04 by LemonInTheDark

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
## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[063bf74f31...](https://github.com/MTandi/tgstation/commit/063bf74f31a27ec8096fe10b844d5883be6d13a9)
#### Monday 2023-07-24 13:21:04 by carlarctg

There is no longer a 50% chance of catching a heretic out when examining them drawing influences (#76878)

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

---
## [mmrwoods/dotfiles](https://github.com/mmrwoods/dotfiles)@[25b6fd1803...](https://github.com/mmrwoods/dotfiles/commit/25b6fd1803653a49e4704064da3f772f657de235)
#### Monday 2023-07-24 13:22:18 by Mark Woods

Add z and my z hacks to bash profile

z keeps track of "frequent" dirs and allows you to jump to them

I find the jumping part of this a pretty poor experience, so I use fzf

---
## [gen2inc/gen-2-inc-text-to-emoji](https://github.com/gen2inc/gen-2-inc-text-to-emoji)@[a7e4c6fbd7...](https://github.com/gen2inc/gen-2-inc-text-to-emoji/commit/a7e4c6fbd78d2b1df0a95c22e7de4812e2392d3c)
#### Monday 2023-07-24 13:28:23 by ellie

fix massive bug

how did an ai find this error out? i feel so fucking stupid and i feel like i'll never be a good programmer, i am a shit problem solver and somehow i always get the solution wrong. what the fuck is wrong with my life

---
## [mmrwoods/dotfiles](https://github.com/mmrwoods/dotfiles)@[cc13277e36...](https://github.com/mmrwoods/dotfiles/commit/cc13277e3696e56c37166110e5fceeee71698e97)
#### Monday 2023-07-24 14:23:20 by Mark Woods

Add .node-version file for vimspector adapters

vscode-node-debug2 adapter requires node 16 or lower, running npm run
build on later versions generates the following error:

[15:11:06] Error: You must provide the URL of lib/mappings.wasm by calling SourceMapConsumer.initialize({ 'lib/mappings.wasm': ... }) before using SourceMapConsumer
    at readWasm (/Users/mwoods/dotfiles/vim/pack/bundle/start/vimspector/gadgets/macos/download/vscode-node-debug2/node_modules/gulp-typescript/node_modules/source-map/lib/read-wasm.js:8:13)
    at wasm (/Users/mwoods/dotfiles/vim/pack/bundle/start/vimspector/gadgets/macos/download/vscode-node-debug2/node_modules/gulp-typescript/node_modules/source-map/lib/wasm.js:25:16)
    at /Users/mwoods/dotfiles/vim/pack/bundle/start/vimspector/gadgets/macos/download/vscode-node-debug2/node_modules/gulp-typescript/node_modules/source-map/lib/source-map-consumer.js:264:14
    at process.processTicksAndRejections (node:internal/process/task_queues:95:5)

This is apparently a known issue, and I do vaguely recall working around
it in the past before re-installing plugins, so just add a .node-version
file with a version supported by vscode-node-debug2 and make shit work.

This is a horrible hack, but I've just lost 30 minutes trying to figure
out WTF was going on, and I don't want to repeat that in a few months.

---
## [kirollosd/git](https://github.com/kirollosd/git)@[eaa0fd6584...](https://github.com/kirollosd/git/commit/eaa0fd658442c2b83dfad918d636bba3ca3b4087)
#### Monday 2023-07-24 15:21:54 by Jeff King

git_connect(): fix corner cases in downgrading v2 to v0

There's code in git_connect() that checks whether we are doing a push
with protocol_v2, and if so, drops us to protocol_v0 (since we know
how to do v2 only for fetches). But it misses some corner cases:

  1. it checks the "prog" variable, which is actually the path to
     receive-pack on the remote side. By default this is just
     "git-receive-pack", but it could be an arbitrary string (like
     "/path/to/git receive-pack", etc). We'd accidentally stay in v2
     mode in this case.

  2. besides "receive-pack" and "upload-pack", there's one other value
     we'd expect: "upload-archive" for handling "git archive --remote".
     Like receive-pack, this doesn't understand v2, and should use the
     v0 protocol.

In practice, neither of these causes bugs in the real world so far. We
do send a "we understand v2" probe to the server, but since no server
implements v2 for anything but upload-pack, it's simply ignored. But
this would eventually become a problem if we do implement v2 for those
endpoints, as older clients would falsely claim to understand it,
leading to a server response they can't parse.

We can fix (1) by passing in both the program path and the "name" of the
operation. I treat the name as a string here, because that's the pattern
set in transport_connect(), which is one of our callers (we were simply
throwing away the "name" value there before).

We can fix (2) by allowing only known-v2 protocols ("upload-pack"),
rather than blocking unknown ones ("receive-pack" and "upload-archive").
That will mean whoever eventually implements v2 push will have to adjust
this list, but that's reasonable. We'll do the safe, conservative thing
(sticking to v0) by default, and anybody working on v2 will quickly
realize this spot needs to be updated.

The new tests cover the receive-pack and upload-archive cases above, and
re-confirm that we allow v2 with an arbitrary "--upload-pack" path (that
already worked before this patch, of course, but it would be an easy
thing to break if we flipped the allow/block logic without also handling
"name" separately).

Here are a few miscellaneous implementation notes, since I had to do a
little head-scratching to understand who calls what:

  - transport_connect() is called only for git-upload-archive. For
    non-http git remotes, that resolves to the virtual connect_git()
    function (which then calls git_connect(); confused yet?). So
    plumbing through "name" in connect_git() covers that.

  - for regular fetches and pushes, callers use higher-level functions
    like transport_fetch_refs(). For non-http git remotes, that means
    calling git_connect() under the hood via connect_setup(). And that
    uses the "for_push" flag to decide which name to use.

  - likewise, plumbing like fetch-pack and send-pack may call
    git_connect() directly; they each know which name to use.

  - for remote helpers (including http), we already have separate
    parameters for "name" and "exec" (another name for "prog"). In
    process_connect_service(), we feed the "name" to the helper via
    "connect" or "stateless-connect" directives.

    There's also a "servpath" option, which can be used to tell the
    helper about the "exec" path. But no helpers we implement support
    it! For http it would be useless anyway (no reasonable server
    implementation will allow you to send a shell command to run the
    server). In theory it would be useful for more obscure helpers like
    remote-ext, but even there it is not implemented.

    It's tempting to get rid of it simply to reduce confusion, but we
    have publicly documented it since it was added in fa8c097cc9
    (Support remote helpers implementing smart transports, 2009-12-09),
    so it's possible some helper in the wild is using it.

  - So for v2, helpers (again, including http) are mainly used via
    stateless-connect, driven by the main program. But they do still
    need to decide whether to do a v2 probe. And so there's similar
    logic in remote-curl.c's discover_refs() that looks for
    "git-receive-pack". But it's not buggy in the same way. Since it
    doesn't support servpath, it is always dealing with a "service"
    string like "git-receive-pack". And since it doesn't support
    straight "connect", it can't be used for "upload-archive".

    So we could leave that spot alone. But I've updated it here to match
    the logic we're changing in connect_git(). That seems like the least
    confusing thing for somebody who has to touch both of these spots
    later (say, to add v2 push support). I didn't add a new test to make
    sure this doesn't break anything; we already have several tests (in
    t5551 and elsewhere) that make sure we are using v2 over http.

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [The-Coders-Den/NovaEngine-Godot-FNF](https://github.com/The-Coders-Den/NovaEngine-Godot-FNF)@[cfdec1f8c4...](https://github.com/The-Coders-Den/NovaEngine-Godot-FNF/commit/cfdec1f8c40d50285cff32151ef3cdb09fadfb6f)
#### Monday 2023-07-24 15:41:37 by voiddev

fixed some song event stuff
- and added monochrome cause fuck you

---
## [rust-lang-ci/rust](https://github.com/rust-lang-ci/rust)@[a367073b0b...](https://github.com/rust-lang-ci/rust/commit/a367073b0b085658182079202c18c2b339640bbf)
#### Monday 2023-07-24 15:56:40 by bors

Auto merge of #114011 - RalfJung:place-projection, r=<try>

interpret: Unify projections for MPlaceTy, PlaceTy, OpTy

For ~forever, we didn't really have proper shared code for handling projections into those three types. This is mostly because `PlaceTy` projections require `&mut self`: they might have to `force_allocate` to be able to represent a project part-way into a local.

This PR finally fixes that, by enhancing `Place::Local` with an `offset` so that such an optimized place can point into a part of a place without having requiring an in-memory representation. If we later write to that place, we will still do `force_allocate` -- for now we don't have an optimized path in `write_immediate` that would avoid allocation for partial overwrites of immediately stored locals. But in `write_immediate` we have `&mut self` so at least this no longer pollutes all our type signatures.

(Ironically, I seem to distantly remember that many years ago, `Place::Local` *did* have an `offset`, and I removed it to simplify things. I guess I didn't realize why it was so useful... I am also not sure if this was actually used to achieve place projection on `&self` back then.)

The `offset` had type `Option<Size>`, where `None` represent "no projection was applied". This is needed because locals *can* be unsized (when they are arguments) but `Place::Local` cannot store metadata: if the offset is `None`, this refers to the entire local, so we can use the metadata of the local itself (which must be indirect); if a projection gets applied, since the local is indirect, it will turn into a `Place::Ptr`. (Note that even for indirect locals we can have `Place::Local`: when the local appears in MIR, we always start with `Place::Local`, and only check `frame.locals` later. We could eagerly normalize to `Place::Ptr` but I don't think that would actually simplify things much.)

Having done all that, we can finally properly abstract projections: we have a new `Projectable` trait that has the basic methods required for projecting, and then all projection methods are implemented for anything that implements that trait. We can even implement it for `ImmTy`! (Not that we need that, but it seems neat.) The visitor can be greatly simplified; it doesn't need its own trait any more but it can use the `Projectable` trait. We also don't need the separate `Mut` visitor any more; that was required only to reflect that projections on `PlaceTy` needed `&mut self`.

It is possible that there are some more `&mut self` that can now become `&self`... I guess we'll notice that over time.

r? `@oli-obk`

---
## [Underewarrr/evals](https://github.com/Underewarrr/evals)@[9b0ffc0496...](https://github.com/Underewarrr/evals/commit/9b0ffc04968c9946964f8eb4f6eb2eb7c99e4e00)
#### Monday 2023-07-24 15:58:58 by Domenico

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
## [Underewarrr/evals](https://github.com/Underewarrr/evals)@[300b2ebced...](https://github.com/Underewarrr/evals/commit/300b2ebced056f74df97ccbf8f9dba88cb1a2bf8)
#### Monday 2023-07-24 15:58:58 by cookfish

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
## [Underewarrr/evals](https://github.com/Underewarrr/evals)@[17a89da761...](https://github.com/Underewarrr/evals/commit/17a89da761e50eea4266008b9a00612c1ee6fcb9)
#### Monday 2023-07-24 15:58:58 by mochisky

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
## [Underewarrr/evals](https://github.com/Underewarrr/evals)@[ba5a04065d...](https://github.com/Underewarrr/evals/commit/ba5a04065d6f3b96449fda545a00b1a085128b98)
#### Monday 2023-07-24 15:58:58 by Christopher Gondek

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
## [sjinzh/streamlit](https://github.com/sjinzh/streamlit)@[c464422e1b...](https://github.com/sjinzh/streamlit/commit/c464422e1bbea66b3184769ea22599356d710f9a)
#### Monday 2023-07-24 16:00:12 by Danny Wolf

Upgrade react-range to fix memory usage of sliders (#6764)

As mentioned in
https://blog.streamlit.io/six-tips-for-improving-your-streamlit-app-performance/
memory usage struggles in the browser if you have large ranges:

> Due to implementation details, high-cardinality sliders don't suffer
> from the serialization and network transfer delays mentioned earlier,
> but they will still lead to a poor user experience (who needs to
> specify house prices up to the dollar?) and high memory usage. In my
> testing, the example above increased RAM usage by gigabytes until the
> web browser eventually gave up (though this is something that should
> be solvable on our end. We'll look into it!)

This was caused by a bug in react-range, which I fixed last year.
https://github.com/tajo/react-range/pull/178

At the time, I had figured it would get picked up by a random yarn
upgrade and didn't worry too much about it.
But, apparently yarn doesn't really have an easy way of doing upgrades
of transitive dependencies (see https://github.com/yarnpkg/yarn/issues/4986)?
I took the suggestion of someone in that thread to delete the entry and
let yarn regenerate it.

Some technical details about the react-range fix from the original
commit message (the "application" is a streamlit app):

> We have an application that uses react-range under the hood, and we
> noticed that a range input was taking 2GB of RAM on our machines. I
> did some investigation and found that regardless of whether the marks
> functionality was being used, refs were being created for each
> possible value of the range.

> We have some fairly huge ranges (we're using the input to scrub a
> video with potential microsecond accuracy), and can imagine that
> other people are affected by the previous behavior. This change
> should allow us to continue using large input ranges without
> incurring a memory penalty.

---
## [SweetVitamin/40K-Eipharius](https://github.com/SweetVitamin/40K-Eipharius)@[bed2fa7301...](https://github.com/SweetVitamin/40K-Eipharius/commit/bed2fa7301b0042189c792ead0eea59f51f13d0a)
#### Monday 2023-07-24 16:13:44 by SweetVitamin

Lots of background fixes to Cyborgs

They are still horribly fucked however and needs an experienced coder to rewrite/fix a lot of things like giving them stats & skills & working radio.

---
## [racckun/site](https://github.com/racckun/site)@[9d847b1cd9...](https://github.com/racckun/site/commit/9d847b1cd9e3cfae565dc2d755f5750375598342)
#### Monday 2023-07-24 16:52:13 by raccoon

Ladies and Gentlemen, Colonel PT Chester Whitmore is proud to present Bung Vulchungo and the Zimbabwe Songbirds! Do you see banana man Hopping over on the white-hot sand Here he come with some for me Freshly taken from banana tree (one, two, three, four) Banana man, me want a ton Gimme double and a bonus one Gimme more for all me friends This banana flow will never end Do you want a banana? Peel it down and go, mm-mm-mm-mm Do you want a banana? This banana for you Tonight, we dance around the flame Then we get to play spirit game Spirit names, we shout out loud Shake the thunder from the spirit cloud All the songbirds in the tree Chant a tune to let the spirits free Then we see them in the night Spirits jumping by fire light Do you want a banana? (Do you want a banana?) Peel it down and go, mm-mm-mm-mm Do you want a banana? (Do you want a banana?) This banana for you Look you, you too uptight, you know You could laugh and kick it back and go (wee!) But without a rhythm or a rhyme You do not banana all the time Fly away from city on the run Try to make a little fun Look you, come to the bungalow African't you tell me told you so Don't you love the bumping of the drum? Make you shake until the bum go numb Let de bongo play you 'til you drop This banana never stop (never stop, never stop) Forget all your troubles and go with the flow Forget about whatever you may never know Like whether whatever you are doing is whatever you should And whether anything you do is ever any good And then forget about banana when it stick in your throat And when it make you wanna bellow, but you stuck in a choke And forget about the yellow from the beckoning man Who make you take another one and make a mock of your plan Bungalay, bungalow Make up your mind and tell me no (Shh) Well, it's nine o'clock, and it's getting dark And the sun is falling from the sky I've never left so early, and you may wonder why Tomorrow morning on the plane No banana make you go insane Floating back to busy town No banana make you want to frown Do you want a banana? (Do you want a banana) Peel it down and go, mm-mm-mm-mm Do you want a banana? This banana for... you

---
## [dazscripts/specter](https://github.com/dazscripts/specter)@[ef2161d7f5...](https://github.com/dazscripts/specter/commit/ef2161d7f5a3a8ded7b28e506096008ab58c0bf4)
#### Monday 2023-07-24 16:54:19 by daz

motion sensor should actually work now (im so stupid holy fucking shit)

---
## [Sonic121x/Skyrat-tg](https://github.com/Sonic121x/Skyrat-tg)@[606f0009a1...](https://github.com/Sonic121x/Skyrat-tg/commit/606f0009a1b61472a534b3dbc7e618680b292f55)
#### Monday 2023-07-24 18:07:39 by SkyratBot

[MIRROR] Removes two redundant components [MDB IGNORE] (#22613)

* Removes two redundant components (#76866)

## About The Pull Request

We're starting to get to have enough components that people don't
realise that what they want already exists but doesn't have the name
they expect 🙃

I recently added `track_hierarchical_movement` which is similar enough
to `connect_containers` that it shouldn't independently exist, even if I
like sending a new signal more than the ugly setup pattern for
`connect_loc`.

`trait_loc` is actually older than `give_turf_traits` but
`give_turf_traits` covers more edge cases than `turf_loc` so seems like
the better one to maintain.
HOWEVER `give_turf_traits` held a list of references to atoms in it,
which isn't great in an element. I couldn't think of a way to completely
eliminate the list, but it isn't a list of references any more so it
shouldn't cause any hard deletions.

## Why It's Good For The Game

Having two components which do the same thing but marginally differently
is confusing and going to cause us trouble down the line.

## Changelog

Not player facing

* Removes two redundant components

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [ritorizo/Shiptest](https://github.com/ritorizo/Shiptest)@[18819cc7fb...](https://github.com/ritorizo/Shiptest/commit/18819cc7fb78eb4eaf11691e4a07b1294b76358a)
#### Monday 2023-07-24 18:09:39 by zevo

Minor changes to the Syndicate Battle Sphere ruin (#2045)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Various fixes for provinggrounds.dmm, mainly the server room and SMES.
Server room is no longer filled with black box recorders, but salvagable
servers. There is now one singular black box recorder in the center
where a black box on a table was. The SMES now should actually charge
the ruin. Tossed a medkit in one of the halls for players to use while
clearing the ruin. Replaced about half of the syndicate researcher mobs
with syndicate operatives who will actually fight the players. Rotated
an airlock missed in the map updates for anywalls.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
boy, i sure love functional ruins! also players should not have 25 of a
very rare potential quest item. The ruin can stay as it is otherwise,
because it provides a fun challenge for superbly well armed players (or
a rugged explorer with nothing but a lazer gun and a dream) with a
fitting reward at the end of a mounted LMG.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
fix: Syndicate Battle Dome (provinggrounds.dmm) should now have a
functional SMES and airlocks/blast doors.
fix: Syndicate Battle Dome (provinggrounds.dmm) no longer has ~20 black
box recorders and now only has one.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [ritorizo/Shiptest](https://github.com/ritorizo/Shiptest)@[0e6f7fa646...](https://github.com/ritorizo/Shiptest/commit/0e6f7fa64649dfbf52b8e4b71756e6625e50fdd0)
#### Monday 2023-07-24 18:09:39 by Imaginos16

TileTest Part 1: Big Sweeping Changes! (#2054)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->
## !! WARNING !!
This is a multi-parter PR. Due to the fact that tiles here on shiptest
are an unholy amalgam of decals, greyscale sprites and multiple
spread-out files, things are *bound* to look weird. If they do, feel
free to report it and it will be addressed in future PRs.

## About The Pull Request

This PR finally accomplishes the promise I made to @triplezeta a year
ago, creating a unique tileset for the server that people may enjoy!

To put every single microscopic change I have made would take forever,
so I will instead provide a series of screenshots of it in action!


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/00e9cec0-335a-4367-90f9-1adc572595f3)


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/497310ab-fe06-4b31-8774-70e79338a7d8)


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/80991d0b-c48b-404b-b4a6-cbb1c4c6af3a)


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/cc06d43e-3873-499e-aa12-51a0d7a37c98)

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Utilizing an unique, modernized tileset for our server to differentiate
from our competitors is something that has been requested, and I was
more than happy to lend my hand to make it a reality!
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy
del: Removes several unused floor types, as well as completely
annihilating the "monofloor" and "dirty" floor types, and the "edge"
decal type.
imageadd: Redoes the floors using the TileTest tileset!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Bjarl <94164348+Bjarl@users.noreply.github.com>

---
## [mo-dhia/Afrah-2](https://github.com/mo-dhia/Afrah-2)@[ea4d841743...](https://github.com/mo-dhia/Afrah-2/commit/ea4d841743ec8ee7d96e8f61c5b45bbb824339ee)
#### Monday 2023-07-24 18:20:37 by mo-dhia

header re-usable with wedding page z-index over 100000 issue.
(fuck you ahmed)

---
## [parasyte/Project64-Legacy](https://github.com/parasyte/Project64-Legacy)@[1233fe406e...](https://github.com/parasyte/Project64-Legacy/commit/1233fe406ed1587aa75a9dad147d92c757cebac7)
#### Monday 2023-07-24 18:20:47 by Jay Oster

Fix many bugs in cheat search (#41)

- Memory allocation failures were causing cheat searches to miss millions of potential results. The cause was `realloc()` failures in `CS_AddResult()`. Allocations fail for very large blocks due to memory fragmentation. This is a 32-bit process, so it only has access to a 2 GB address space, and most of that is used for emulation, thread stacks, and a billion small allocations. The cheat search needs to allocate two 64 MB blocks (max) but the free space in the heap may not have two blocks large enough to satisfy it. When this happens, the current cheat results are thrown away and a new, smaller allocation replaces it. But the cheat search doesn't abort, it just continues on oblivious to the data loss.

- Allocation failures were resolved by reducing the total memory required. The new result layout needs only: two 8 MB blocks, one 1 MB block, and a growable block (64 KB to 32 MB) for the address list. In the worst case, memory use is still almost half as small as it was before. And because it's split into multiple blocks, there is a better chance that they will all fit into the fragmented heap.

- Better error handling when the dynamic block reallocation fails. I won't say it's perfect, since it can still have some leaks and bad user experience. But it's a start toward handling allocation failures gracefully.

- Removed `CS_InitResults()`. This was an internal function, users are not supposed to need to even know about it. Now it's inlined with `CS_ReserveSpace()` which is required to be called before using most of the `CS_` functions. (Except `CS_InitSearch()` which has nothing to do with the `CS_RESULTS` struct.)

- Interacting with `CS_RESULTS` and `CS_HITS` has been completely refactored. `CS_HITS` has been split into multiple memory blocks as described above. The "growable address list" has been moved to `CS_RESULTS`, and `CS_BITMAP` replaces the rest of `CS_HITS`. The new `CS_HIT` is a single-element view of the old `CS_HITS` to avoid changing user code too much.

- `CS_AddResult`, `CS_AddHit`, and `CS_GetHit` now all have two variants: one for bytes (8-bit searches) and one for words (16-bit searches). They each return BOOL, indicating errors when FALSE. And `CS_GetHit(Byte|Word)` takes an out-param as its first argument.

- Fixed some memory leaks in `WriteProject64ChtDev()`: `ChtDev->LastSearch->Results` was never freed. Also free memory in early returns.

- Fixed cheat search LiveUpdate thread so it won't deadlock when the emulator window/ROM browser is closed.

- Fixed the prefix find in the results listbox. With the listbox focuses, pressing any hex character on the keyboard will initiate a find. The old algorithm attempted to do prefix matching, but only did masked matches. So most of the time the find function didn't work at all. The new way is much shorter and actually works.

- Added braces on a lot of conditions to avoid goto-fail scenarios.

See also #19, which was caused by the same heap fragmentation issue. That PR only fixed one particular case.

----

TBD: Storing the list of addresses is still very wasteful. The list is necessary for `O(1)` time lookups when interacting with the result listbox. The listbox APIs use item indices for most operations, and the results listbox only contains addresses with "hits" in the cheat search. The naive solution is storing all addresses (32-bits each) in an array (max memory requirement is a 32 MB allocation block). This is the data structure used in both the original code and in this PR.

It is possible to reduce the memory requirement without degrading the lookup time terribly. First, observe that the address list is always sorted. Addresses are arranged in ascending order. Second, note that this sorted list contains a lot of redundancy; In the worst case with a fully populated list of 8-bit addresses, the first 65,536 addresses all share the same upper half; `0x0000`. The next 65,536 addresses also share the same upper half; `0x0001`. This pattern repeats to the end of the list, with upper half = `0x007f`.

Remove this redundancy by storing multiple arrays, let's call them "buckets", of 16-bit values (i.e., only storing the lower half of each address). Each bucket will have exactly 65,536 entries, working out to 128 KB for each. And we only need 128 _total_ buckets for a maximum of 16 MB required. That's a 50% reduction in the worst case. And even better, these smaller 128 KB blocks will be easier to allocate within the fragmented address space!

If it isn't clear by now, the index within the 128 buckets tells you the upper half of the address. Combine it with the lower half that is actually stored in the bucket, and you can recover the full address with half of the memory needed.

Lookups (find the Nth address in the list) can be made `O(log(n))` with a prefix sum tree over the 128 buckets. Constant time (`O(1)`) lookups are not possible because each bucket is dynamically sized (even if its allocation is fixed, though they can be made much smaller). The bucket only stores addresses with search hits. The naive search solution is linear (`O(n)`), requiring visiting each bucket to count how many addresses it contains; in the worst case, it visits all 128 buckets.

The prefix sum tree instead sums the bucket counts in a tree that can be binary searched. For 128 buckets, the log-time search reduces to 7 bucket visits.

One example prefix sum tree data structure that can be used is called a [Fenwick tree](https://en.wikipedia.org/wiki/Fenwick_tree). Storage requirements for it are only the 128 `int`s making up the partial sums for the bucket item counts plus an extra `int` for the total sum.

The only downside to this approach is the additional code complexity. There isn't a lot of code to write, but it is easy to mess it up if you don't know why the data structure is needed (or how it works). It's only marginally slower than the naive constant-time array lookups. More than fast enough for the listbox drawing and find operations.

The upsides are: About half of the memory requirement in the worst case (unknown 8-bit search across the full 8 MB N64 RAM). Much smaller allocations are needed, which is easier for a fragmented heap to satisfy.

I am not planning to implement the prefix sum tree in this PR. But I've decided to write my thoughts here just in case the 32 MB allocations in the cheat search ever become problematic. We'll have something to look back on as a proposed solution.

---
## [EveBaker/holbertonschool-AirBnB_clone_v3](https://github.com/EveBaker/holbertonschool-AirBnB_clone_v3)@[2c6b3fedf8...](https://github.com/EveBaker/holbertonschool-AirBnB_clone_v3/commit/2c6b3fedf897d817276163ff128b31b02af1f77a)
#### Monday 2023-07-24 18:51:54 by gumquat

holy fuck please tell me this fixed my import shit

---
## [ricardoamador/.github](https://github.com/ricardoamador/.github)@[231e1d3971...](https://github.com/ricardoamador/.github/commit/231e1d3971f844bbafdbd1ac3da7083257983859)
#### Monday 2023-07-24 19:03:19 by Andrew Kolos

Update link to good first issues (#28)

Copy-pasted from https://github.com/flutter/flutter/pull/130759:

> Today (Jul 17, 2023), I renamed the `good first contribution` label to
`good first issue`. This is because
> 1) `good first issue` is the more commonly used for this intent and
may be (ever so slightly) more recognizable to potential new
contributors, and, more importantly,
> 2) GitHub recognizes the label `good first issue` when surfacing good
first issues in specific places in GitHub[^1].
> 
> This PR updates Contributing.md to match the new name.
> 
> `grep` did not find any other references to `good first contribution`
to update in this repo.

## Pre-launch Checklist

- [x] I read the [Contributor Guide] and followed the process outlined
there for submitting PRs.
- [x] I read the [Tree Hygiene] wiki page, which explains my
responsibilities.
- [x] I read and followed the [Flutter Style Guide], including [Features
we expect every widget to implement].
- [x] I signed the [CLA].
- [ ] I listed at least one issue that this PR fixes in the description
above. _(not applicable in my opinion. If you'd like me to file an issue
first, let me know what label would be appropriate.)_
- [x] I updated/added relevant documentation (doc comments with `///`).
- [x] I added new tests to check the change I am making, or this PR is
[test-exempt]. _not applicable: docs-only change_
- [x] All existing and new tests are passing.

If you need help, consider asking for advice on the #hackers-new channel
on [Discord].

<!-- Links -->
[Contributor Guide]:
https://github.com/flutter/flutter/wiki/Tree-hygiene#overview
[Tree Hygiene]: https://github.com/flutter/flutter/wiki/Tree-hygiene
[test-exempt]:
https://github.com/flutter/flutter/wiki/Tree-hygiene#tests
[Flutter Style Guide]:
https://github.com/flutter/flutter/wiki/Style-guide-for-Flutter-repo
[Features we expect every widget to implement]:
https://github.com/flutter/flutter/wiki/Style-guide-for-Flutter-repo#features-we-expect-every-widget-to-implement
[CLA]: https://cla.developers.google.com/
[flutter/tests]: https://github.com/flutter/tests
[breaking change policy]:
https://github.com/flutter/flutter/wiki/Tree-hygiene#handling-breaking-changes
[Discord]: https://github.com/flutter/flutter/wiki/Chat

[^1]: [Source (GitHub
docs)](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/encouraging-helpful-contributions-to-your-project-with-labels).
Example: https://github.com/flutter/flutter/contribute. If my vague
memory serves me correctly, this can also appear in certain emails or
the "discovery queue"-type experience that GitHub provides.

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[cb855f807b...](https://github.com/cmss13-devs/cmss13/commit/cb855f807b4f5538d623e78363e76aabd5f8d80a)
#### Monday 2023-07-24 19:07:12 by forest2001

Yautja Gear Recovery Changes (#3455)

# About the pull request
Makes pred gear recovery more dynamic and less blood thirsty.
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
add: Adds a plasma breaching charge that detonates a plasma wave
stunning those opposite it.
add: Adds the name of the tracked item to the Yautja gear tracker.
add: Added an alternate mode for the Plasma Pistol and moved the
incendiary property to it.
add: Added MINIMAP_FLAG_ALL to Yautja globe map.
/:cl:

---------

Co-authored-by: harryob <me@harryob.live>
Co-authored-by: Morrow <darthbane97@gmail.com>

---
## [distributivgesetz/tgstation](https://github.com/distributivgesetz/tgstation)@[41f20bc3ce...](https://github.com/distributivgesetz/tgstation/commit/41f20bc3ced4e7853a09f2d5e1dcf46346f2e51f)
#### Monday 2023-07-24 19:18:36 by LemonInTheDark

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
## [shauntmcgovern/RemoveViolencePrototypesMSDTOpenSource](https://github.com/shauntmcgovern/RemoveViolencePrototypesMSDTOpenSource)@[2d1eec2c73...](https://github.com/shauntmcgovern/RemoveViolencePrototypesMSDTOpenSource/commit/2d1eec2c736761be93f5927e1b8ac92946760ffd)
#### Monday 2023-07-24 19:40:54 by Ted Bundy

Prototype72SchematicCodenameForICanUnderstandAndIK

now thy Terms, more is like it. The more the standard, the better the materials. Once again did you, read the required chapters, is is more more like like itit. Then I was the same'goez. And all that I needed was the district. More like it, call the police now. Where is they located, standard? Ah' I see'C. And more like it see, now the chemicals have become separated, because once again this is an overall. Overall, boldly. This is one of the evening, and one at Night. More like it, the same damn thing as it was Before than it moves from manifold from manifold, as said before 'c' but how does it relate to 'g' ahh' more like it pz. a. The nasty royal term, then you findit once again, and repeat the same process. Asif this is canceling out what we donot kneed to know and what we do infacteffectually need to in fact, know know. And in this same process. What would beit the samez. And then what is different. For we are describing two composites. And finding within each'plane, yes the body of existence in a chemical-physical-biological manner'matter, manifold like finding a piece of Silver. For that would be a good start, then remember to data'lodge it into the mainframe. Ahh' yes once more and nows'letz repeat it once again. And let us, break it the F'down it, once more, until we find our source. What I am after, I am afraid, is killing machines. And who has it, possess it. Then I would find their location, for that is pertinent and completely objectively necessary. Then the U.S. Marine Corps can find it, for us. Let us work together as we move, this entity, this dangerous very dangerous handiwork to the rightful places. The different systems that once again, my U.S. Marine Corps would like to know. As the successor has been chosen to follow his predecessor. And'then the knowhow wherewithanall. There that it 'goez. Is more like it now. As we move through the middle of the mall, with a chopper. A glint, more like it once again. It would be haveto, mainframe, more like a bus on it was the difference ah' humanHands and once again What is the Difference than the other Passerby and the volunteer. What would it be? I see. There it goez' once again and once more, in these Systems? I see, that they are. Juxtaposition. Fractually distance from between me and you, if I was say the victim and you were my be all that is all, enderz. That way it would become a, "New Event." Thats good for now... Once again Prototype 72.

---
## [ViniloTraiteto/Shortscope](https://github.com/ViniloTraiteto/Shortscope)@[7d8667814d...](https://github.com/ViniloTraiteto/Shortscope/commit/7d8667814d9d4e3cae4f72ac7737461d97f501e4)
#### Monday 2023-07-24 20:20:10 by ViniloTraiteto

A FUCKTON of fixes...
Fixed lighting issues on scoreboard.
Fixed Z-Fighting of multiple supply panels.
Fixed occlusion edge cases when hugging walls.
Probably some other shit I forgot...
God Ive had zero motivation for this lately...

---
## [Katskan/cmss13](https://github.com/Katskan/cmss13)@[d26452bb9a...](https://github.com/Katskan/cmss13/commit/d26452bb9a846091214ced880c5d7a34a6b61048)
#### Monday 2023-07-24 20:26:23 by Unknownity

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
## [Katskan/cmss13](https://github.com/Katskan/cmss13)@[5f5fcd2b27...](https://github.com/Katskan/cmss13/commit/5f5fcd2b279b2bd51b5869b0a345b4f964dcb34c)
#### Monday 2023-07-24 20:26:23 by Drathek

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
## [Retrino/lobotomy-corp13](https://github.com/Retrino/lobotomy-corp13)@[171b1478f9...](https://github.com/Retrino/lobotomy-corp13/commit/171b1478f9d01a40841ca0bb131394fe8a2039b2)
#### Monday 2023-07-24 20:53:43 by vampirebat74

Limbus Company E.G.O dump (#1062)

* Adds roseate desire

roseate sfx

datums

weapons

add aedd

sprite adjustments

unfucks suits

new sfx

name fix

aaaa

adds capote

adds sloshing

farmwatch

farmwatch suit

stuff

farmwatch stuff

capote inhands

red sheet finished

sloshing gift

linters

Stuff

stuff

fixes shit

stuff

weapon code cleanup

spicebush finished

removes the heal

code fix

stuff

removes reference

farmwatch hat

new vfx

requested changes

* block duration

---------

Co-authored-by: Mr.Heavenly <davidx3adamhunt@gmail.com>

---
## [ceejbot/soulsy](https://github.com/ceejbot/soulsy)@[53af5a59b4...](https://github.com/ceejbot/soulsy/commit/53af5a59b4c92db5406c1b3cfd0d270f4e4f2a39)
#### Monday 2023-07-24 21:12:47 by C J Silverio

Re-implemented fading in & out, with easing.

I had accidentally removed all triggers for fading when I reworked
how visibility is determined. I've decided to be happy about that,
because I was pretty unhappy with how fading looked.

Some notes about the implementation itself:

I'm using a cubic easing function to scale the transition from the
starting point to the end goal. This is subtle but noticeable
in-game. Fading *in* is twice the speed as fading out, on the
theory that seeing the HUD when you need it is more important than
having it go away. We also handle changing fade direction midway
nicely, so the alpha shouldn't jump.

There's also 750 milliseconds of hysteresis on any decision to
auto-fade. The game will give us a brief moment of thinking the
player's weapons are not drawn when changing what's equipped.
We don't want to start fading out every time that happens.

One last note: imgui doesn't support alphas on the full window, only
on individual elements. So any element draw has to remember to
multiply all its color alphas with the global hud alpha.

Did some misc formatting & tidying. Renamed functions so their
usages are more clear to me, a bear of very little brain. Shuffled
some logging around.

---
## [DianaLS/odoo](https://github.com/DianaLS/odoo)@[9e71094582...](https://github.com/DianaLS/odoo/commit/9e71094582ec4c9b719431e77538da8f91ffa9e3)
#### Monday 2023-07-24 21:21:20 by Xavier Morel

[FIX] core: handle recursion error when resolving stored fields

Issue discovered in the uninstall (and reinstall) of sale_project: a
dump has ~100 tasks, when reinstalling `sale_line_id` has to be
initialised, this is done by marking `sale_line_id` on all extant
tasks as to-recompute, which triggers their computation on the next
`flush`.

Because it's a recursive field, `Field.recompute` ensures only one
record at a time gets recomputed (as there could be cross-dependencies
in the recorset which protection would prevent from resolving).

As the field computation runs, it accesses itself, which triggers a
cache miss, which triggers a `_fetch_field` (to get the currently
stored value), this calls `_read`, which flushes the field we're
trying to read.

The problem here is that for efficiency the cache miss will look for
all records in the cache without a value for the
field (`_in_cache_without`) and try to `fetch` on them as well. This
means rather than not doing anything in flush, we're going to
`Field.recompute` on all records except the one selected the first
time around, which repeats the cycle until there is no more additional
record found in `_in_cache_without`, which could trigger the next
round of `recompute`, and the entire thing unwinds, and we probably
perform a ton of unnecessary additional `compute_value`.

Except that doesn't even happen, because the process from one compute
to the next takes 12~13 stack frames, which given the default
recursion limit of 1000 gives a hard limit of 76 fields before hitting
a RecursionError. As this is less than 100, a recursion error [is what
we get](https://runbot.odoo.com/runbot/build/31726625).

In 15.2, this was fixed by only expanding the fetch on non-recursive
fields, pessimizing recursive
fields (5c2511115b14299516fce4aa3737a62faaf5b653). Test-wise this only
impacted mail performances and in a relatively minor manner.

In 16.0, the mail tests actually match already (so that part was
skipped by the cherrypicking) however this impacts the knowledge perf
tests much more significantly e.g. `test_article_creation_multi_roots`
gets +9 queries when creating 10 top-level articles, which is a bit
much.

So use an alternative which is ugly as hell but which I didn't
consider for 15.2 (may want to backport it one day if the current fix
is an issue): catch the recursion error and use the existing
fallback (of fetching just the requested record's field without
expanding the recordset).

This likely makes for a pretty inefficient situation in the original
case as we're certainly going to hit the recursion limit repeatedly,
but that still fixes the issue, and it avoids deoptimising cases which
fall short of the recursion limit (resolving under 60 records or
so).

Plus despite creating giant stacks we might actually get good
efficiency as we're going to hit recursion limits repeatedly but
that's pure python, once we fall below the limit we can resolve
everything at once with a single SQL query (or something along those
lines).

Part-of: odoo/odoo#119808

---
## [gs-olive/benchmark](https://github.com/gs-olive/benchmark)@[745644f391...](https://github.com/gs-olive/benchmark/commit/745644f391b4d11da107b2c82fe2d7a3eacf561d)
#### Monday 2023-07-24 21:52:31 by Mark Saroufim

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
## [ScarSkit/lobotomy-corp13](https://github.com/ScarSkit/lobotomy-corp13)@[b420c1d519...](https://github.com/ScarSkit/lobotomy-corp13/commit/b420c1d519b30cd75759de68f6b2abbe0b12a055)
#### Monday 2023-07-24 22:05:08 by vampirebat74

Adds tool E.G.O (#1019)

Tool ego

adds tool E.G.O

removes a extra line

fixes shit

swindle

voce

divinity

fixes shit

shifts divinity down a few pixels

This is the fourth time this same commit was made

I hate TG so fucking much like it's unbelievable why does this only fuck up on my PC? WHY?

hyde weapon

stuff

hyde code

hyde fix

new sprites

inhands

destiny effect

heart sfx

stuff

Co-authored-by: Mr.Heavenly <davidx3adamhunt@gmail.com>

---
## [Ben10083/cmss13](https://github.com/Ben10083/cmss13)@[39cf164c60...](https://github.com/Ben10083/cmss13/commit/39cf164c6075f21c280bf75aea538a7dd64a3d81)
#### Monday 2023-07-24 22:37:22 by tool mind

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
## [Ben10083/cmss13](https://github.com/Ben10083/cmss13)@[56007685d7...](https://github.com/Ben10083/cmss13/commit/56007685d77ed8eab65ab2090e347940551fddc4)
#### Monday 2023-07-24 22:37:22 by Zonespace

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
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[f6c3bc93ba...](https://github.com/Buildstarted/linksfordevs/commit/f6c3bc93baea5d39d9e8345dd0d6d6ee9f674560)
#### Monday 2023-07-24 23:09:59 by Ben Dornis

Updating: 7/24/2023 11:00:00 PM

 1. Added: Introduction to Pocket: obfuscator for MBA expressions
    (https://nicolo.dev/en/blog/introduction-pocket-obfuscator/)
 2. Added: Is software getting worse?
    (https://blog.ploeh.dk/2023/07/24/is-software-getting-worse/)
 3. Added: An algorithm for shuffling playlists
    (https://ruudvanasseldonk.com/2023/an-algorithm-for-shuffling-playlists)
 4. Added: Building an E-Ink Joke of the Day Fridge Magnet · Alex Meub
    (https://alexmeub.com/building-an-eink-joke-fridge-magnet/)
 5. Added: You should write your own programming language
    (https://xnacly.me/posts/2023/write-your-own-programming-language/)
 6. Added: Tek scope screen capture with Bash - Andrej's blog
    (https://andrejradovic.com/blog/tek-tds2014-screen-grab/)
 7. Added: Mongo Read Optimisation: Write Concern
    (https://sreevenkat.com/posts/mongo-read-optimisation)
 8. Added: Thriving in the dynamically type-checked hell scape of Clojure
    (https://blog.janetacarr.com/thriving-in-the-dynamically-type-checked-hell-scape-of-clojure/)
 9. Added: I made a new track for teaching swing
    (https://www.ethanhein.com/wp/2023/i-made-a-new-track-for-teaching-swing/)
10. Added: Do films directed by women have more women in the cast?
    (https://stephenfollows.com/do-films-directed-by-women-have-more-women-in-the-cast/)
11. Added: Sharing encrypted data over short-form mediums
    (https://notes.willhackett.com/share-encrypted-short-form-data/)
12. Added: RSA
    (https://joe-ferrara.github.io/2023/07/23/rsa.html)
13. Added: On .NET Live - Lunr Core: Simple search for all .NET apps
    (https://youtube.com/watch?v=7DosTpW0wgM)
14. Added:  What it’s like to be married to a dying man
    (https://jakeseliger.com/2023/07/24/what-its-like-to-be-married-to-a-dying-man/)
15. Added: Commoditized Social Networking
    (https://philip-trauner.me/blog/post/commoditized-social-networking)
16. Added: Why functional programming?
    (https://ianchanning.wordpress.com/2023/07/24/why-functional-programming/)
17. Added: How to choose the target for a migration from RPG - Strumenta
    (https://tomassetti.me/how-to-choose-the-target-for-a-migration-from-rpg/)

Generation took: 00:09:48.2194886
 Maintenance update - cleaning up homepage and feed

---
## [OctoRocket/space-station-14-octo](https://github.com/OctoRocket/space-station-14-octo)@[06747e0f7e...](https://github.com/OctoRocket/space-station-14-octo/commit/06747e0f7e7d04cf87e63a359a3a86b1a35442cc)
#### Monday 2023-07-24 23:19:12 by Emisse

some silly paintings and posters (#17872)

* webedit

* Update meta.json

* god is real hes here with us

* so true

* so truers rise

* worst meta.json ive seen in my life

* so true

---

