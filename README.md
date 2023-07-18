## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-07-17](docs/good-messages/2023/2023-07-17.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,130,529 were push events containing 3,471,056 commit messages that amount to 292,630,270 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 69 messages:


## [Prussen/tgstation](https://github.com/Prussen/tgstation)@[d1cb2e8751...](https://github.com/Prussen/tgstation/commit/d1cb2e87519869b5c7baafd66d0e2454cfa6282b)
#### Monday 2023-07-17 00:00:04 by Rhials

New planetary exclusive random event/unfavorable situation, Chasmic Earthquake (#75864)

## About The Pull Request


https://github.com/tgstation/tgstation/assets/28870487/2451bc69-db1e-420d-9a18-2f899ca65427

This introduces a new unfavorable situation (non-antagonist random
events that dynamic triggers under certain circumstances), restricted to
planetary maps (Icebox). An earthquake occurs, felt by everyone on the
map, forming a fault that tears the a hole somewhere on the station.

The fault zone is indicated by shaking tiles, which gives a chance
(about 30 seconds) for you to move your machinery/property/crewmembers
out of the way. If you're on those tiles when the fault forms, get ready
to take a nasty fall.

Anything caught in the fault zone as it collapses inward will be
destroyed, violently, _before_ being dropped down into the z-level
below.


![image](https://github.com/tgstation/tgstation/assets/28870487/56916c9f-c8da-4ffb-9d8b-7e940e92bbc2)

These can also happen as a random event, however their rarity is on-par
with that of a meteor storm.

This also adds a helper for finding a midpoint turf between two provided
turfs, thanks to ZephyrTFA.

This idea basically possessed me over the course of a few days, and I
found myself unable to work on anything else until I had it complete.
I'm glad its done.
## Why It's Good For The Game

Gives Icebox its own big "environmental disaster" event. I'm hoping it
isn't received as being too destructive, but mind that this is meant to
be an equal to the dreaded meteor storm.

Also makes it so that unfavorable events aren't a coinflip between a
portal storm/rod on planetary maps.
## Changelog
:cl: Rhials
add: Chasmic Earthquake random event, exclusive to Icebox. Tears a huge
chasm in the hull of the station. Watch out for shaking tiles!
sound: Adds sounds for distant rumbling, metal creaking, and rubble
shaking.
imageadd: Achievement icon for getting sucked up in an earthquake chasm.
/:cl:

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[7979597798...](https://github.com/TaleStation/TaleStation/commit/7979597798ddd047907218251ff69fe777334dee)
#### Monday 2023-07-17 00:02:47 by TaleStationBot

[MIRROR] [MDB IGNORE] Imports and Contraband 2: Landfill Gacha Addiction (I put trash randomizers into cargo crates and called it content) (#6804)

Original PR: https://github.com/tgstation/tgstation/pull/76771
-----

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

---------

Co-authored-by: necromanceranne <40847847+necromanceranne@users.noreply.github.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[746b75844c...](https://github.com/tgstation/tgstation/commit/746b75844c0e05b521a2973cb0705fca304d287f)
#### Monday 2023-07-17 00:12:09 by necromanceranne

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
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[9286933739...](https://github.com/tgstation/tgstation/commit/92869337395a34eb372d7af6b3afaee4be4a7bef)
#### Monday 2023-07-17 00:12:09 by Jacquerel

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
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[4aec91cc06...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/4aec91cc069b1beb1ec6593522dc5f65f7c5c7aa)
#### Monday 2023-07-17 00:33:36 by GoldenAlpharex

[MANUAL MIRROR] Fixes carbon bodytypes not always being synchronized with bodyparts + Fixes dumb usage of TRAIT_LIVERLESS_METABOLISM i caused [MDB IGNORE] (#22519)

* Fixes carbon bodytypes not always being synchronized with bodyparts (#76522)

Fixes https://github.com/tgstation/tgstation/issues/76481
TLDR /mob/living/carbon/human/species subtypes were NOT updating their
bodytypes on spawn due to absurd and wacky carbon bodypart creation code
that meant try_attach_limb() never got called (What the FUCK?)

* Fixes CI too

* [NO GBP] Fixes dumb usage of TRAIT_LIVERLESS_METABOLISM i caused (#76500)

## About The Pull Request

TRAIT_LIVERLESS_METABOLISM should do what it implies, and make you
always metabolize as if you were liverless.
This was a stupid mistake on my part because I wasn't aware
TRAIT_STABLELIVER was a thing.

## Why It's Good For The Game

TRAIT_LIVERLESS_METABOLISM and TRAIT_STABLELIVER should not behave the
exact same.

## Changelog

Not quite player facing.

* I fucking swear I fixed this before

---------

Co-authored-by: ChungusGamer666 <82850673+ChungusGamer666@users.noreply.github.com>

---
## [ivanmixo/TerraGov-Marine-Corps](https://github.com/ivanmixo/TerraGov-Marine-Corps)@[ca4b66185f...](https://github.com/ivanmixo/TerraGov-Marine-Corps/commit/ca4b66185ffa363692529f8340a43cccab02cbf1)
#### Monday 2023-07-17 00:36:32 by chizzy376

Gives the Umbilical Tad shutters on side windows. (#13490)

* y

* Update combat_patrol.dm

* Update combat_patrol.dm

Sometimes I think about if life is really worth the hassle, if I really have to deal with so much bs only to then have to believe hard enough to get into heaven. Am I a good person for heaven? Do I deserve it? fuck if i know

* Finish fixing my fuckup

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[a8e0d7c8d2...](https://github.com/tgstation/tgstation/commit/a8e0d7c8d202027d36c96391ed9a43cb5d708065)
#### Monday 2023-07-17 00:54:40 by MrMelbert

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
## [vdavalon01/yuzu](https://github.com/vdavalon01/yuzu)@[8e703e08df...](https://github.com/vdavalon01/yuzu/commit/8e703e08dfcf735a08df2ceff6a05221b7cc981f)
#### Monday 2023-07-17 00:59:22 by comex

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
## [mamh-mixed/microsoft-terminal](https://github.com/mamh-mixed/microsoft-terminal)@[21464fe41c...](https://github.com/mamh-mixed/microsoft-terminal/commit/21464fe41c9c09eac4b9e2d85225f18f1f3c2c7b)
#### Monday 2023-07-17 03:03:28 by Mike Griese

Manually hide our DesktopWindowXamlSource (#15165)

As discussed in #6507

Newer builds of Windows do this automatically. However, this was spotted
in the wild on 1.18. It's possible the threading changes created a
situation where the OS-side fix no longer applied to us. So let's just
do it manually. It doesn't have any side effects.

I saw this once on Win11, but couldn't repro it this morning when I
tried to add this fix. I'm just gonna assume this worked, despite the
fact that I can't repro it on win11 anymore.

closes #6507

See also #14957

## detailed description

> `WindowsXamlManager::XamlCore::Initialize` calls
`ConfigureCoreWindow`, which creates a `CoreWindow` on the thread

> Problem is, we're calling that on the main thread (which doesn't have
_any_ windows), and then eventually creating a `DesktopWindowXamlSource`
on a second thread for the actual window

> It's not that it "manages a window", it's that it "manages xaml on
Windows OS". just use ICoreWindowInterop -- QI for ICoreWindowInterop
and call get_WindowHandle.

Also see:
*
[ICoreWindowInterop](https://learn.microsoft.com/en-us/windows/win32/api/corewindow/nn-corewindow-icorewindowinterop)
*
[WindowsXamlManager.InitializeForCurrentThread](https://learn.microsoft.com/en-us/uwp/api/windows.ui.xaml.hosting.windowsxamlmanager.initializeforcurrentthread?view=winrt-22621#windows-ui-xaml-hosting-windowsxamlmanager-initializeforcurrentthread)
* The source code in
`onecoreuap\windows\dxaml\xcp\dxaml\lib\WindowsXamlManager_Partial.*`
* os.2020!6102020 which fixed MSFT:33498969, MSFT:27807465,
MSFT:21854264

---
## [mamh-mixed/microsoft-terminal](https://github.com/mamh-mixed/microsoft-terminal)@[77215d9d77...](https://github.com/mamh-mixed/microsoft-terminal/commit/77215d9d77b99b48d1ee8302736178f2ec9f3a77)
#### Monday 2023-07-17 03:03:42 by Mike Griese

Fix `ShowWindow(GetConsoleWindow())` (#13118)

A bad merge, that actually revealed a horrible bug.

There was a secret conflict between the code in #12526 and #12515. 69b77ca was a bad merge that hid just how bad the issue was. Fixing the one line `nullptr`->`this` in `InteractivityFactory` resulted in a window that would flash uncontrollably, as it minimized and restored itself in a loop. Great. 

This can seemingly be fixed by making sure that the conpty window is initially created with the owner already set, rather than relying on a `SetParent` call in post. This does pose some complications for the #1256 future we're approaching. However, this is a blocking bug _now_, and we can figure out the tearout/`SetParent` thing in post. 

* fixes #13066.
* Tested with the script in that issue.
* Window doesn't flash uncontrollably.
* `gci | ogv` still works right
* I work here.
* Opening a new tab doesn't spontaneously cause the window to minimize
* Restoring from minimized doesn't yeet focus to an invisible window
* Opening a new tab doesn't yeet focus to an invisible window
* There _is_ a viable way to call `GetAncestor` s.t. it returns the Terminal's hwnd in Terminal, and the console's in Conhost


The `SW_SHOWNOACTIVATE` change is also quite load bearing. With just `SW_NORMAL`, the pseudo window (which is invisible!) gets activated whenever the terminal window is restored from minimized. That's BAD.


There's actually more to this as well. 


Calling `SetParent` on a window that is `WS_VISIBLE` will cause the OS to hide the window, make it a _child_ window, then call `SW_SHOW` on the window to re-show it. `SW_SHOW`, however, will cause the OS to also set that window as the _foreground_ window, which would result in the pty's hwnd stealing the foreground away from the owning terminal window. That's bad.

`SetWindowLongPtr` seems to do the job of changing who the window owner is, without all the other side effects of reparenting the window. 

Without `SetParent`, however, the pty HWND is no longer a descendant of the Terminal HWND, so that means `GA_ROOT` can no longer be used to find the owner's hwnd. For even more insanity, without `WS_POPUP`, none of the values of `GetAncestor` will actually get the terminal HWND. So, now we also need `WS_POPUP` on the pty hwnd. To get at the Terminal hwnd, you'll need

```c++
GetAncestor(GetConsoleWindow(), GA_ROOTOWNER)
```

---
## [mamh-mixed/microsoft-terminal](https://github.com/mamh-mixed/microsoft-terminal)@[9ccd6ecd74...](https://github.com/mamh-mixed/microsoft-terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Monday 2023-07-17 03:03:42 by Mike Griese

Manually copy trailing attributes on a resize (#12637)

## THE WHITE WHALE

This is a fairly naive fix for this bug. It's not terribly performant,
but neither is resize in the first place.

When the buffer gets resized, typically we only copy the text up to the
`MeasureRight` point, the last printable char in the row. Then we'd just
use the last char's attributes to fill the remainder of the row.

Instead, this PR changes how reflow behaves when it gets to the end of
the row. After we finish copying text, then manually walk through the
attributes at the end of the row, and copy them over. This ensures that
cells that just have a colored space in them get copied into the new
buffer as well, and we don't just blat the last character's attributes
into the rest of the row. We'll do a similar thing once we get to the
last printable char in the buffer, copying the remaining attributes.

This could DEFINITELY be more performant. I think this current
implementation walks the attrs _on every cell_, then appends the new
attrs to the new ATTR_ROW. That could be optimized by just using the
actual iterator. The copy after the last printable char bit is also
especially bad in this regard. That could likely be a blind copy - I
just wanted to get this into the world.

Finally, we now copy the final attributes to the correct buffer: the new
one.  We used to copy them to the _old_ buffer, which we were about to
destroy.

## Validation

I'll add more gifs in the morning, not enough time to finish spinning a
release Terminal build with this tonight.

Closes #32 🎉🎉🎉🎉🎉🎉🎉🎉🎉
Closes #12567

(cherry picked from commit 855e1360c0ff810decf862f1d90e15b5f49e7bbd)

---
## [icvntechstudio/djoser](https://github.com/icvntechstudio/djoser)@[4ebdc10add...](https://github.com/icvntechstudio/djoser/commit/4ebdc10add211cb238002fcc79a7cf8409d99825)
#### Monday 2023-07-17 03:30:04 by github

Fix for Friendly tips when Missing SOCIAL_AUTH_ALLOWED_REDIRECT_URIS

i forget add SOCIAL_AUTH_ALLOWED_REDIRECT_URIS to my config

it return 400 error, i don't know why ,  i pay more time find the issues

so  i add Friendly tips

-- sorry  , my english is not well

and thank you all

---
## [SoeunKimsong/StudentAttendanceProject](https://github.com/SoeunKimsong/StudentAttendanceProject)@[925ea72ea3...](https://github.com/SoeunKimsong/StudentAttendanceProject/commit/925ea72ea314703af3c9774e53606a062d8d9ec0)
#### Monday 2023-07-17 03:34:48 by kim_songular

Merge pull request #4 from SoeunKimsong/brovit

lol fuck you

---
## [faaaay/Bubberstation](https://github.com/faaaay/Bubberstation)@[c4b550c1a9...](https://github.com/faaaay/Bubberstation/commit/c4b550c1a94670ae333df12b8200ff33f7f7f175)
#### Monday 2023-07-17 04:24:43 by SkyratBot

[MIRROR] New Wizard spell "branch": Vendormancy [MDB IGNORE] (#22008)

* New Wizard spell "branch": Vendormancy (#75679)

## About The Pull Request
New item for wizards, ~~the Staff~~ Scepter of Runic Vendormancy.

With it, you can summon Runic Vending machines to block your enemies,
push them 2 tiles back around the summoning tile, throw the vendors 4
tiles away to squash them or simple detonate the vendors for direct
damage against enemies within a 2 tile range.

The scepter has 3 charges that can be recharged after a "long" channel
so while powerful, it is a tactical weapon and wizards can't directly
steamroll the crew with endless vendors. (Unless they buy multiple
scepters, but that is just funny.)

Also, there is a bug with the throw... I copied how baseball bats deal
with knockback, but they consistently don't push the vendors back, just
spin them on the same tile... I appreciate if anyone has any idea on how
to fix or change that to a better system.

## New changes I made
The vendor has a random set of REAL wizard robes and hat, sandals and a
foam vendor scepter as products to sell now.
This gives the crew some real armor, and if it is considered too much, I
can swap it for the fake versions.
IMO the real clothes work as the perfect bait for the crew to approach
the vendors and get exploded in the process, and while a random
assistant might get real wizard armor to go valid hunt the wizard, the
crew might just mistake them for the real wizard and beat them to death,
which is too funny.
## Why It's Good For The Game

![vendormancerPR](https://github.com/tgstation/tgstation/assets/55374212/f9d98f3e-5916-4a17-987e-249f4cdb7185)

About a year ago I played Stoneshard, and it has such an amazing
Geomancy Wizard that I wanted to port some of its gameplay to SS13 as
our wizards, while funny and destructive, are kinda simple to play...

Summoning and blowing up rocks was nice, but I randomly had the idea of
summoning Vendors while at work and vendors squashing people has become
such an iconic SS13 thing to me that I had to stop being lazy and start
working on this.

Something, something, enviromental combat wizard.
## Changelog
Gonna polish the changelog later too...
:cl: Guillaume Prata
add: New Wizard spell branch: Vendormacy! Summon runic vending machines
with your Vending Scepter, force push them on your enemies to squish
them or blow them up while they are busy buying from the machines.
/:cl:

---------

Co-authored-by: Time-Green <7501474+Time-Green@ users.noreply.github.com>

* New Wizard spell "branch": Vendormancy

---------

Co-authored-by: GuillaumePrata <55374212+GuillaumePrata@users.noreply.github.com>
Co-authored-by: Time-Green <7501474+Time-Green@ users.noreply.github.com>

---
## [Wulferion/cmss13](https://github.com/Wulferion/cmss13)@[d26452bb9a...](https://github.com/Wulferion/cmss13/commit/d26452bb9a846091214ced880c5d7a34a6b61048)
#### Monday 2023-07-17 04:25:05 by Unknownity

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
## [Wulferion/cmss13](https://github.com/Wulferion/cmss13)@[5f5fcd2b27...](https://github.com/Wulferion/cmss13/commit/5f5fcd2b279b2bd51b5869b0a345b4f964dcb34c)
#### Monday 2023-07-17 04:25:05 by Drathek

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
## [IdkSomethingTemporary/ZK-Futurewars-Mod](https://github.com/IdkSomethingTemporary/ZK-Futurewars-Mod)@[febd347482...](https://github.com/IdkSomethingTemporary/ZK-Futurewars-Mod/commit/febd347482e5cf6a0c1c73596c40e98fce11930d)
#### Monday 2023-07-17 04:25:43 by IdkSomethingTemporary

Power Vacuum - Balance changes for striders, commanders, drones and more

Major Changes:

Mogul:
Mogul just had an identiy crisis where it's long range missiles wanted it to stay at the back and shell the enemy lines while it's short range EMP and it's high health wanted it to go to the front and fight the enemy, and it didn't help that it's laser tracker being blocked by terrain meant it could almost never fire at it's max range. We already have strider-class strategic artillery in the form of merlin, garmr, liberator and artillery commander so it made more sense to rework Mogul back into it's vanilla role of fire support. Mogul's range gets cut in half while it's DPS goes up massively. It's cost is also cut to distinquish it more from titan

Drones:
All drones now have been tweaked to have a build time close to or equal to their reload time - it feels janky to have drone pads sit empty before startind drone construction, so now drone pads will always be occupied. I've considered just nuking reload from high orbit but that probably would make drones too good vs AA. In practice the rate of new drones should not be changed much. Additionally, PW buildings have had their drone swarms buffied heavily in preperation for project homefront

Funnelweb:
Funnelweb just kinda sucked. at 6400k and no buildpower it's quite weak for a FW strider, so now it's gaining quite a few more abilities to it's toolbox to make it fit more into the support role: 4 responders, 6 fireflies, 2 vipers, 60 BP and the hoverfac armor field

Guardian:
Guardian's damage output is massively buffed (in total around 3x) and it now has much higher single target damage in order to give shieldbots a way to deal with heavies in exchange for leaning much more into it's vanilla gimmick of shield drain with around 3k shield drain. The stats are around that of 5 felons. The range has been reduced down to 500 to make it less capable of deleting skirmishers

Cloakybots:
All cloakybots (except Gremlin, Mirage and Lurker) have their damage, health and splash increased by 10% and their cost decreasd by 10%
All cloakybots now have all have cloakstrike of 3x damage for 1.5s (except sparky and gremlin, which have none, and assailant, whick keep it's 2 seconds, and yes this affects phantom how you think it does), 1.5x movesped while cloaked (no speed penalty while not cloaked)
Snare Cloak costs doubled in order to account for these buffs

Minor Balance change:
 - Artillery Commander's heavy conversion kit is now cheaper but the weapons themselves got rebalanced
 - Riot comamnder's Vacuum gun is now far weaker as it could one-shot comms at long range
 - Desintergrator for commanders is now more expensive to account for the buffs to ghost commander's cloak.
 - Strike servos are now a bit more expensive and unlock a bit later to give super servos some use
 - Liberator got some of it's upcoming changes early with a slight rework to it's weapon
 - Merlin's rockets are less terrifying to cons and more terrifying to armies
 - Bloom loses it's responder as it was too oppressive
 - Flare loses leash range on it's drone
 - Reef now has 12 gulls and 3 responders for a more swarmy feel. It's disarm missile damage has also been buffed
 - Gull now has 66% the stats to give reef a more swarmy feel
 - Nebula now has 24 spiculas and ultilise all it's pads for spiculas
 - Spicula how has 4x the HP and slightly increased damage. A full nebula swarm has around 4k raw dps, though given fighter AI it's likely closer to 1-2k
 - Responder is now more about buildpower and less about shield health
 - Preserver disarm damage x2.5, disarm time doubled

---
## [Daddooott/Tweakers-click-here](https://github.com/Daddooott/Tweakers-click-here)@[b2f52fa35c...](https://github.com/Daddooott/Tweakers-click-here/commit/b2f52fa35c553afa7a5e4141494221c12ea12250)
#### Monday 2023-07-17 04:27:17 by Daddooott

Create I have been calling your phone number fuck off

Everything I've already written to you in messages I don't need to write again everything I've already said to your father on the phone who denies knowing you I don't need to say to you. What I will tell you is I know exactly where you live I know what your phone numbers are I know who you're associates are I have skills and areas that you don't. Just because your life sucks and you have retarded children and I was successful in my life didn't want children and didn't fuck up and have them, it gives you no right to fuck with me. You have committed multiple federal crimes and I've already been in touch with the FBI hear where I live and in two other states including North Carolina and Illinois and New Jersey is coming soon so you don't have to worry about that You're fucked You're definitely going to be arrested You're definitely going to be questioned and you're most likely going to be prosecuted. I am not hiding from you You have blocked me from adding you as a friend you have blocked me when I tried to contact you on LinkedIn You refuse to pick up the phone every time a toggle you call your account so don't tell me I'm not a big boy. You also have full control of my computer so you can contact me there. But you're the little piece of shit fag pussy aren't you not me You be a big boy actually you're already a pretty big boy pretty fat fat ass boy weird fuck. You contact me back anytime you want

---
## [humanist-bean/mountainai-svelte](https://github.com/humanist-bean/mountainai-svelte)@[5ada16b5da...](https://github.com/humanist-bean/mountainai-svelte/commit/5ada16b5daa738f487506ee2ede05a1f1ee43fc5)
#### Monday 2023-07-17 04:38:19 by Alder French

Finally figured out a way to serve fastai .pkl model! Turns out vertex ai is not very useful with its 1.5mb upload limit. After countless hour wasted on trying to get vertex ai to work (like literally 15+) I gave up and switched to making a flask server. I was able to get it working in a couple hours :/ Moral of the story is know when to quit... Anyways app.py and test_app.py in flask server contain the code to get a working REST API with the original .pkl fastai model. Now all I have to do is deploy it to google cloud, which is totally not gonna suck based on my previous experiences with google today :P

---
## [mentalisttraceur/esceval](https://github.com/mentalisttraceur/esceval)@[62cb8272fa...](https://github.com/mentalisttraceur/esceval/commit/62cb8272fa6623085455fa09696dcf6345af70d6)
#### Monday 2023-07-17 06:04:12 by Alexander Kozhevnikov

Fix edge case in escevalenv.sh

Discovered by the new testing. Nice. In
principle I should've caught this. Years
ago I prided myself on always having these
kinds of edge-cases in my thoughts whenever
I was shell-scripting. But now? I'm not so
sure that's a good use of my human brain.

Little-known, rarely-encountered quirk of
Bourne-shell command substitution: trailing
newlines are stripped off the output of the
command. Any number of them, in most shells.

So if, for example, you have a value with a
newline at the end, and you, say, `printenv`
it (`printenv` writes the value followed by
one newline), both `printenv`'s newline and
the value's newline are stripped off when
capturing that output in a variable.

The robust/general solution is seen in this
commit: we echo another character inside
the command substitution after the desired
output, which shields all trailing newlines
in the `printenv` output, then delete that
character and one trailing newline (added
by `printenv`) afterwards.

---
## [Lapwell/personal-website](https://github.com/Lapwell/personal-website)@[08a0ea5c99...](https://github.com/Lapwell/personal-website/commit/08a0ea5c99af81a7cf560f5786c4f3a8c16cea7b)
#### Monday 2023-07-17 06:04:14 by Byron.C

Progress made on the goddamn codersrank svg shit. theyre widgets are annoying af

---
## [zimokernel/bevy](https://github.com/zimokernel/bevy)@[fb4c21e3e6...](https://github.com/zimokernel/bevy/commit/fb4c21e3e62b3789e8e768ac63dc2205ddec698f)
#### Monday 2023-07-17 06:50:18 by Ida "Iyes

bevy_audio: ECS-based API redesign (#8424)

# Objective

Improve the `bevy_audio` API to make it more user-friendly and
ECS-idiomatic. This PR is a first-pass at addressing some of the most
obvious (to me) problems. In the interest of keeping the scope small,
further improvements can be done in future PRs.

The current `bevy_audio` API is very clunky to work with, due to how it
(ab)uses bevy assets to represent audio sinks.

The user needs to write a lot of boilerplate (accessing
`Res<Assets<AudioSink>>`) and deal with a lot of cognitive overhead
(worry about strong vs. weak handles, etc.) in order to control audio
playback.

Audio playback is initiated via a centralized `Audio` resource, which
makes it difficult to keep track of many different sounds playing in a
typical game.

Further, everything carries a generic type parameter for the sound
source type, making it difficult to mix custom sound sources (such as
procedurally generated audio or unofficial formats) with regular audio
assets.

Let's fix these issues.

## Solution

Refactor `bevy_audio` to a more idiomatic ECS API. Remove the `Audio`
resource. Do everything via entities and components instead.

Audio playback data is now stored in components:
- `PlaybackSettings`, `SpatialSettings`, `Handle<AudioSource>` are now
components. The user inserts them to tell Bevy to play a sound and
configure the initial playback parameters.
- `AudioSink`, `SpatialAudioSink` are now components instead of special
magical "asset" types. They are inserted by Bevy when it actually begins
playing the sound, and can be queried for by the user in order to
control the sound during playback.

Bundles: `AudioBundle` and `SpatialAudioBundle` are available to make it
easy for users to play sounds. Spawn an entity with one of these bundles
(or insert them to a complex entity alongside other stuff) to play a
sound.

Each entity represents a sound to be played.

There is also a new "auto-despawn" feature (activated using
`PlaybackSettings`), which, if enabled, tells Bevy to despawn entities
when the sink playback finishes. This allows for "fire-and-forget" sound
playback. Users can simply
spawn entities whenever they want to play sounds and not have to worry
about leaking memory.

## Unsolved Questions

I think the current design is *fine*. I'd be happy for it to be merged.
It has some possibly-surprising usability pitfalls, but I think it is
still much better than the old `bevy_audio`. Here are some discussion
questions for things that we could further improve. I'm undecided on
these questions, which is why I didn't implement them. We should decide
which of these should be addressed in this PR, and what should be left
for future PRs. Or if they should be addressed at all.

### What happens when sounds start playing?

Currently, the audio sink components are inserted and the bundle
components are kept. Should Bevy remove the bundle components? Something
else?

The current design allows an entity to be reused for playing the same
sound with the same parameters repeatedly. This is a niche use case I'd
like to be supported, but if we have to give it up for a simpler design,
I'd be fine with that.

### What happens if users remove any of the components themselves?

As described above, currently, entities can be reused. Removing the
audio sink causes it to be "detached" (I kept the old `Drop` impl), so
the sound keeps playing. However, if the audio bundle components are not
removed, Bevy will detect this entity as a "queued" sound entity again
(has the bundle compoenents, without a sink component), just like before
playing the sound the first time, and start playing the sound again.

This behavior might be surprising? Should we do something different?

### Should mutations to `PlaybackSettings` be applied to the audio sink?

We currently do not do that. `PlaybackSettings` is just for the initial
settings when the sound starts playing. This is clearly documented.

Do we want to keep this behavior, or do we want to allow users to use
`PlaybackSettings` instead of `AudioSink`/`SpatialAudioSink` to control
sounds during playback too?

I think I prefer for them to be kept separate. It is not a bad mental
model once you understand it, and it is documented.

### Should `AudioSink` and `SpatialAudioSink` be unified into a single
component type?

They provide a similar API (via the `AudioSinkPlayback` trait) and it
might be annoying for users to have to deal with both of them. The
unification could be done using an enum that is matched on internally by
the methods. Spatial audio has extra features, so this might make it
harder to access. I think we shouldn't.

### Automatic synchronization of spatial sound properties from
Transforms?

Should Bevy automatically apply changes to Transforms to spatial audio
entities? How do we distinguish between listener and emitter? Which one
does the transform represent? Where should the other one come from?

Alternatively, leave this problem for now, and address it in a future
PR. Or do nothing, and let users deal with it, as shown in the
`spatial_audio_2d` and `spatial_audio_3d` examples.

---

## Changelog

Added:
- `AudioBundle`/`SpatialAudioBundle`, add them to entities to play
sounds.

Removed:
 - The `Audio` resource.
 - `AudioOutput` is no longer `pub`.

Changed:
 - `AudioSink`, `SpatialAudioSink` are now components instead of assets.

## Migration Guide

// TODO: write a more detailed migration guide, after the "unsolved
questions" are answered and this PR is finalized.

Before:

```rust

/// Need to store handles somewhere
#[derive(Resource)]
struct MyMusic {
    sink: Handle<AudioSink>,
}

fn play_music(
    asset_server: Res<AssetServer>,
    audio: Res<Audio>,
    audio_sinks: Res<Assets<AudioSink>>,
    mut commands: Commands,
) {
    let weak_handle = audio.play_with_settings(
        asset_server.load("music.ogg"),
        PlaybackSettings::LOOP.with_volume(0.5),
    );
    // upgrade to strong handle and store it
    commands.insert_resource(MyMusic {
        sink: audio_sinks.get_handle(weak_handle),
    });
}

fn toggle_pause_music(
    audio_sinks: Res<Assets<AudioSink>>,
    mymusic: Option<Res<MyMusic>>,
) {
    if let Some(mymusic) = &mymusic {
        if let Some(sink) = audio_sinks.get(&mymusic.sink) {
            sink.toggle();
        }
    }
}
```

Now:

```rust
/// Marker component for our music entity
#[derive(Component)]
struct MyMusic;

fn play_music(
    mut commands: Commands,
    asset_server: Res<AssetServer>,
) {
    commands.spawn((
        AudioBundle::from_audio_source(asset_server.load("music.ogg"))
            .with_settings(PlaybackSettings::LOOP.with_volume(0.5)),
        MyMusic,
    ));
}

fn toggle_pause_music(
    // `AudioSink` will be inserted by Bevy when the audio starts playing
    query_music: Query<&AudioSink, With<MyMusic>>,
) {
    if let Ok(sink) = query.get_single() {
        sink.toggle();
    }
}
```

---
## [TommyVinseti/tgstation](https://github.com/TommyVinseti/tgstation)@[16cecf864d...](https://github.com/TommyVinseti/tgstation/commit/16cecf864d4b6ff864956cbc9d0cf7af4cfe1f26)
#### Monday 2023-07-17 08:00:06 by Jacquerel

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
## [ArtifexSoftware/ghostpdl](https://github.com/ArtifexSoftware/ghostpdl)@[6b014dbbad...](https://github.com/ArtifexSoftware/ghostpdl/commit/6b014dbbada0d64c83c6da241dc161733571a38a)
#### Monday 2023-07-17 08:01:21 by Ken Sharp

Graphics library - avoid divide by zero with ridiculous resolutions

Bug #706847 "FPE gs_screen_enum_init_memory / zscreen_enum_init"

The specimen file consists solely of:

<< /HWResolution [32 65535] >> setpagedevice

Which, while legal, is plainly ridiculous. The code for selecting a
halftone tile wasn't checking for a potential divide by zero (caused
by the resolution).

So check for that and just continue if we would get a divide by zero.
Either we'll find a better match or, for silly cases like this, end
up using the default. The result will be awful no matter what, in this
case.

---
## [iqba78/android_kernel_xiaomi_sdm660_southwest](https://github.com/iqba78/android_kernel_xiaomi_sdm660_southwest)@[5f839dec24...](https://github.com/iqba78/android_kernel_xiaomi_sdm660_southwest/commit/5f839dec24051c02b4078a4d44dde30b92766af9)
#### Monday 2023-07-17 08:11:04 by Angelo G. Del Regno

Makefile.lib: Lower kernel gzip compression to fastest

You're reading this - so you're trying to understand "JUST WHY OMG".
That's already a good step.

First of all, this is a downstream kernel - always keep that in mind!
Now, this kernel is targeting new *very powerful* Qualcomm platforms
like SM8250 and the Sony Edo platform - which has a very fast UFS card.

Keep in mind that the bootloader sets the CPU at a frequency that is
slightly faster than the "in the middle" ones, which is anyway not
veeeery fast - but that's good, really. I agree.

So.. check this out:   for Image.gz-dtb.....
COMP_LEVEL    SIZE
9             20116171
5	      20220479
2	      20940223
1	      21231290

Remember again that we're loading from a UFS card and that
we are loading ~1.1MB more out of a 20MB file.
If you're smart enough you surely know already about RAM and CPU
overhead of very high compression levels.

If you still disagree with what I just did, read this commit description
another 20 times, or more, until you understand it. :)))

Signed-off-by: Tiktodz <ewprjkt@proton.me>

---
## [qianqiangotoTHU/Codeforces](https://github.com/qianqiangotoTHU/Codeforces)@[5595a64eff...](https://github.com/qianqiangotoTHU/Codeforces/commit/5595a64effc5b85ea0824f8d781010cfbd230e62)
#### Monday 2023-07-17 08:22:32 by qianqiangotoTHU

#866-A Yura's New Name

https://codeforces.com/contest/1820/problem/A

After holding one team contest, boy Yura got very tired and wanted to change his life and move to Japan. In honor of such a change, Yura changed his name to something nice.

Fascinated by this idea he already thought up a name s

consisting only of characters "_" and "^". But there's a problem — Yura likes smiley faces "^_^" and "^^". Therefore any character of the name must be a part of at least one such smiley. Note that only the consecutive characters of the name can be a smiley face.

More formally, consider all occurrences of the strings "^_^" and "^^" in the string s
. Then all such occurrences must cover the whole string s, possibly with intersections. For example, in the string "^^__^_^^__^" the characters at positions 3,4,9,10 and 11 are not contained inside any smileys, and the other characters at positions 1,2,5,6,7 and 8

are contained inside smileys.

In one operation Jura can insert one of the characters "_" and "^" into his name s

(you can insert it at any position in the string). He asks you to tell him the minimum number of operations you need to do to make the name fit Yura's criteria.
Input

Each test consists of multiple test cases. The first line contains a single integer t
(1≤t≤100

) —the number of test cases. The description of test cases follows.

The first and only line of each test case contains a single string s
(1≤|s|≤100

), consisting of characters "_" and "^",  — the name to change.
Output

For each test case, output a single integer — the minimum number of characters you need to add to the name to make it fit for Yura. If you don't need to change anything in the name, print 0

.
Example
Input
Copy

7
^______^
___^_^^^_^___^
^_
^
^_^^^^^_^_^^
___^^
_

Output
Copy

5
5
1
1
0
3
2

Note

In the first test case, you can get the following name by adding 5

characters:

^_^_^_^_^_^_^

In the third test case, we can add one character "^" to the end of the name, then we get the name:

^_^

In the fourth test case, we can add one character "^" to the end of the name, then we get the name:

^^

In the fifth test case, all of the characters are already contained in smiley faces, so the answer is 0

.

In the seventh test case, you can add one character "^" at the beginning of the name and one character "^" at the end of the name, then you get the name:

^_^

---
## [clown-team/git](https://github.com/clown-team/git)@[07f91e5e79...](https://github.com/clown-team/git/commit/07f91e5e79810a8f17de745d2d84c384add75f0a)
#### Monday 2023-07-17 08:58:07 by Jeff King

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
## [ritorizo/Shiptest](https://github.com/ritorizo/Shiptest)@[18819cc7fb...](https://github.com/ritorizo/Shiptest/commit/18819cc7fb78eb4eaf11691e4a07b1294b76358a)
#### Monday 2023-07-17 09:14:40 by zevo

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
## [dmatos2012/nushell](https://github.com/dmatos2012/nushell)@[0567407f85...](https://github.com/dmatos2012/nushell/commit/0567407f853c23f54215020a10f4a831ae2aef47)
#### Monday 2023-07-17 09:17:39 by Antoine Stevan

standard library: bring the tests into the main CI (#8525)

Should close one of the tasks in #8450.

# Description
> **Note**
> in order of appearance in the global diff

- 1b7497c41966306aa3103a95a9b5ef5df7111ee4 adds the `std-tests` job to
the CI which
  1. installs `nushell` in the runner
  2. run the `tests.nu` module
> see `open .github/workflows/ci.yml | get jobs.std-tests | to yaml`

-
[`ec85b6fd`..`9c122115`](ec85b6fd3fc004cd94e3fada5c8e5fe2714fd629..9c12211564ca8ee90ed65ae45776dccb8f8e4ef1)
is where all the magic happens => see below
- :test_tube: 799c7eb7fd5f140289b36b9dbc00329c50e2fbda introduces some
bugs and failing test to see how the CI behaves => see how the [tests
failed](https://github.com/nushell/nushell/actions/runs/4460098237/jobs/7833018256)
as expected :x:
- :test_tube: and c3de1fafb5c5313e30c08c9ca57e09df33b61b74 reverts the
failing tests, i.e. the previous commit, leaving a standard library
whose tests all pass :tada: => see the [tests
passing](https://github.com/nushell/nushell/actions/runs/4460153434/jobs/7833110719?pr=8525#step:5:1)
now :heavy_check_mark:

## the changes to the runner
> see
[`ec85b6fd`..`9c122115`](ec85b6fd3fc004cd94e3fada5c8e5fe2714fd629..9c12211564ca8ee90ed65ae45776dccb8f8e4ef1)

the issue with the previous runner was the following: the clever trick
of using `nu -c "use ...; test"` did print the errors when occuring but
they did not capture the true "failure", i.e. in all cases the
`$env.LAST_EXIT_CODE` was set to `0`, never stopping the CI when a test
failed :thinking:

i first tried to `try` / `catch` the error in
ec85b6fd3fc004cd94e3fada5c8e5fe2714fd629 which kinda worked but only
throw a single error, the first one

i thought it was not the best and started thinking about a solution to
have a complete report of all failing tests, at once, to avoid running
the CI multiple times!

the easiest solution i found was the one i implemented in
9c12211564ca8ee90ed65ae45776dccb8f8e4ef1
> **Warning**
> this changes the structure of the runner quite a bit, but the `for`
loops where annoying to manipulate structured data and allow the runner
to draw a complete report...

now the runner does the following
- compute the list of all available tests in a table with the `file`,
`module` and `name` columns (first part of the pipe until `flatten` and
`rename`)
- run the tests one by one computing the new `pass` column
  - with a `log info`
- captures the failing ones => puts `true` in `pass` if the test passes,
`false` otherwise
- if at least one test has failed, throw a single error with the list of
failing tests

### hope you'll like it :relieved: 

# User-Facing Changes
```
$nothing
```

# Tests + Formatting
the standard tests now return a true error that will stop the CI

# After Submitting
```
$nothing
```

---
## [dmnct/space-station-14](https://github.com/dmnct/space-station-14)@[06747e0f7e...](https://github.com/dmnct/space-station-14/commit/06747e0f7e7d04cf87e63a359a3a86b1a35442cc)
#### Monday 2023-07-17 09:18:07 by Emisse

some silly paintings and posters (#17872)

* webedit

* Update meta.json

* god is real hes here with us

* so true

* so truers rise

* worst meta.json ive seen in my life

* so true

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[bd8ca161e4...](https://github.com/treckstar/yolo-octo-hipster/commit/bd8ca161e4f02f4369673da1bcb90357022fe953)
#### Monday 2023-07-17 09:22:05 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [vdaular-dev/linksfordevs](https://github.com/vdaular-dev/linksfordevs)@[bd450dd172...](https://github.com/vdaular-dev/linksfordevs/commit/bd450dd172a1c9e13157564c086a3b358606c7dc)
#### Monday 2023-07-17 09:29:13 by Ben Dornis

Updating: 7/16/2023 9:00:00 PM

 1. Added: Re: Ansible
    (https://www.eneigualauno.com/rant/2023/07/15/re-ansible.html)
 2. Added: How to register a Kei truck in Pennsylvania
    (https://danwilkerson.com/posts/2023-05-30-how-to-register-a-kei-truck-in-pa)
 3. Added: Dev Therapy part II: Recoveries · Melatonin
    (https://melatonin.dev/blog/dev-therapy-part-ii-recoveries/)
 4. Added: So You Want to Hire for Developer Tooling | Hazel Weakly
    (https://hazelweakly.me/blog/so-you-want-to-hire-for-developer-tooling/)
 5. Added: Jeremy Mikkola - What makes developers productive?
    (https://jeremymikkola.com/posts/developer_productivity.html)
 6. Added: The Private Equity Model in Medicine is Flawed | Ben White
    (https://www.benwhite.com/medicine/the-private-equity-model-in-medicine-is-flawed/)
 7. Added: Entity framework features I wish I knew earlier
    (https://timdeschryver.dev/blog/entity-framework-features-i-wish-i-knew-earlier#hasqueryfilter?utm_source=hnblogs.substack.com)
 8. Added: No local GPU? No Problem! Running Andrej Karpathy’s NanoGPT on Modal.com – Martin Capodici
    (https://martincapodici.com/2023/07/15/no-local-gpu-no-problem-running-andrej-karpathys-nanogpt-on-modal-com/)
 9. Added: Fun with DNS TXT Records
    (https://thoughts.theden.sh/posts/dns-txt-record-fun/)
10. Added: Why do we minimize the mean squared error?
    (https://www.alexmolas.com/2022/05/25/mean-squared-error.html)
11. Added: Lemmy frontend alternatives are popping off
    (https://blog.erlend.sh/lemmy-frontend-alternatives-are-popping-off)
12. Added: Beyond the Marketing: Assessing Anti-Bot Platforms through a Hacker's Lens
    (https://blog.umasi.dev/antibots-1)
13. Added: An Alternative Approach to Deep Tech VC
    (https://www.freaktakes.com/p/an-alternative-approach-to-deep-tech)
14. Added: Score-Based Diffusion Models
    (https://fanpu.io/blog/2023/score-based-diffusion-models/)
15. Added: Bypassing Internet Censorship Using SSH
    (https://znano.eu.org/blog/posts/bypassing-internet-censorship-using-ssh)
16. Added: wuko.ai: Evolve your mailbox into an intelligent read-it-later hub
    (https://katat.me/blog/wuko/intro-email-gpt)
17. Added: How I Wrote a Book Last Night
    (https://www.pulent.com/posts/how-i-wrote-a-book-last-night-unleashing-the-power-of-ai/)
18. Added: Building Intelligent Applications with OpenAI and C#: A Step-by-Step Guide to Get Started
    (https://neelbhatt.com/2023/07/16/building-intelligent-applications-with-openai-and-c-a-step-by-step-guide-to-get-started/)

Generation took: 00:11:06.3046751
 Maintenance update - cleaning up homepage and feed

---
## [IdkSomethingTemporary/ZK-Futurewars-Mod](https://github.com/IdkSomethingTemporary/ZK-Futurewars-Mod)@[6dcb03dea7...](https://github.com/IdkSomethingTemporary/ZK-Futurewars-Mod/commit/6dcb03dea78cae13d5e71843b6f08667ff939f2e)
#### Monday 2023-07-17 09:36:33 by IdkSomethingTemporary

Power Vacuum - Balancing for striders, commanders and more

**Major Changes:**

Mogul:
Mogul just had an identiy crisis where it's long range missiles wanted it to stay at the back and shell the enemy lines while it's short range EMP and it's high health wanted it to go to the front and fight the enemy, and it didn't help that it's laser tracker being blocked by terrain meant it could almost never fire at it's max range. We already have strider-class strategic artillery in the form of merlin, garmr, liberator and artillery commander so it made more sense to rework Mogul back into it's vanilla role of fire support. Mogul's range gets cut in half while it's DPS goes up massively. It's cost is also cut to distinquish it more from titan

Drones:
All drones now have been tweaked to have a build time close to or equal to their reload time - it feels janky to have drone pads sit empty before startind drone construction, so now drone pads will always be occupied. I've considered just nuking reload from high orbit but that probably would make drones too good vs AA. In practice the rate of new drones should not be changed much. Additionally, PW buildings have had their drone swarms buffied heavily in preperation for project homefront

Funnelweb:
Funnelweb just kinda sucked. at 6400k and no buildpower it's quite weak for a FW strider, so now it's gaining quite a few more abilities to it's toolbox to make it fit more into the support role: 4 responders, 6 fireflies, 2 vipers, 60 BP and the hoverfac armor field

Guardian:
Guardian's damage output is massively buffed (in total around 3x) and it now has much higher single target damage in order to give shieldbots a way to deal with heavies in exchange for leaning much more into it's vanilla gimmick of shield drain with around 3k shield drain. The stats are around that of 5 felons. The range has been reduced down to 500 to make it less capable of deleting skirmishers

Cloakybots:
All cloakybots (except Gremlin, Mirage and Lurker) have their damage, health increased by 10% and their cost decreasd by 10%. Gremlin lost 10% damage, health and gained 10% cost as it was too terrifying to air

**Minor Balance change:**
 - Artillery Commander's heavy conversion kit is now cheaper but the weapons themselves got rebalanced
 - Riot comamnder's Vacuum gun is now far weaker as it could one-shot comms at long range before.
 - Desintergrator for commanders is now more expensive to account for the buffs to ghost commander's cloak.
 - Strike servos are now a bit more expensive and unlock a bit later to give super servos some use
 - Liberator got some of it's upcoming changes early with a slight rework to it's weapon
 - Merlin's rockets are less terrifying to cons and more terrifying to armies
 - Bloom loses it's responder as it was too oppressive
 - Flare loses leash range on it's drone
 - Reef now has 12 gulls and 3 responders for a more swarmy feel. It's disarm missile damage has also been buffed
 - Gull now has 66% the stats to give reef a more swarmy feel
 - Nebula now has 24 spiculas and ultilise all it's pads for spiculas
 - Spicula how has 4x the HP and slightly increased damage. A full nebula swarm has around 4k raw dps, though given fighter AI it's likely closer to 1-2k
 - Responder is now more about buildpower and less about shield health
 - Preserver disarm damage x2.5, disarm time doubled
 - Breaker lost some damage as it was a touch too damaging for it's cost in exchange for armor pen and extra shield damage like hardpoint
 - Disco Rave Party now can fire at it's maximium range and Rainbow Ruiner now releases all it's submunitions upon collidng with a shield (can't be bothered to input the total shield damage of all drp shots)
 - Titan gains armor peircing because why the fuck not
 - The napalm dropped by trailblazer is spread over a smaller area

**Fluff:**
 - Titan's Gigawatt laser renamed to Terawatt laser - Gigawatt just honestly isn't a lot at a stage of the game where strategic and tactical nukes are thrown around like paper airplanes. Terawatt is closer to Titan's level of power when factoring it that it's a small, armor peircing laser
 - "Napalm" regex'd with "Thermite". Thermite is just cooler and scarier than napalm, and mere fire doesn't really make sense to be damaging future death robots anyways

---
## [getsentry/sentry-javascript](https://github.com/getsentry/sentry-javascript)@[d2204eba90...](https://github.com/getsentry/sentry-javascript/commit/d2204eba90613290d8fc678eea8c1749e332eeab)
#### Monday 2023-07-17 09:39:40 by Lukas Stracke

fix(nextjs): Avoid importing SentryWebpackPlugin in dev mode (#8543)

As reported in #8541, our NextJS SDK currently breaks dev mode for the
newest NextJS 13.4.10 version

I have absolutely no idea which of the changes in
[13.4.10](https://github.com/vercel/next.js/releases/tag/v13.4.10) is
causing this.
However, I traced the error back and it happens as soon as our NextJS
SDK package requires @sentry/webpack-plugin:

* @sentry/nextjs calls `require('@sentry/webpack-plugin')`
* @sentry/webpack-plugin calls `const { RawSource } =
require('webpack-sources');`
* For _whatever_ reason, NextJS can't require `webpack-sources` and
throws 💥

Since we don't enable our Webpack plugin [in dev
mode](https://github.com/getsentry/sentry-javascript/blob/723f851f358b75cd39da353804c51ff27ebb0c11/packages/nextjs/src/config/webpack.ts#L305)
anyway, one way to get rid of this error is to only require it if we're
_not_ in dev mode.

This hotfix therefore moves the top-level require of
`@sentry/webpack-plugin` to a dynamic require. This isn't a great
solution and honestly quite ugly but if it unblocks users for now I'd
say we merge it. I think we should definitely revisit this though once
we know more about why NextJS suddenly isn't able to import
`webpack-sources`.

ref #8541

---
## [NotEnoughUpdates/NotEnoughUpdates-REPO](https://github.com/NotEnoughUpdates/NotEnoughUpdates-REPO)@[e458513360...](https://github.com/NotEnoughUpdates/NotEnoughUpdates-REPO/commit/e4585133608ba4add475be13a9f414c989fe1b8b)
#### Monday 2023-07-17 10:10:30 by jani270

Fixed lore of Arrow Poison (#958)

Before disabling any content in relation to this takedown notice, GitHub
- contacted the owners of some or all of the affected repositories to give them an opportunity to [make changes](https://docs.github.com/en/github/site-policy/dmca-takedown-policy#a-how-does-this-actually-work).
- provided information on how to [submit a DMCA Counter Notice](https://docs.github.com/en/articles/guide-to-submitting-a-dmca-counter-notice).

To learn about when and why GitHub may process some notices this way, please visit our [README](https://github.com/github/dmca/blob/master/README.md#anatomy-of-a-takedown-notice).

---

**Are you the copyright holder or authorized to act on the copyright owner's behalf?**

Yes, I am the copyright holder.

**Are you submitting a revised DMCA notice after GitHub Trust & Safety requested you make changes to your original notice?**

No

**Does your claim involve content on GitHub or npm.js?**

GitHub

**Please describe the nature of your copyright ownership or authorization to act on the owner's behalf.**

I am the [private] of the Skytils project available on Github. (https://github.com/Skytils/SkytilsMod)

**Please provide a detailed description of the original copyrighted work that has allegedly been infringed. If possible, include a URL to where it is posted online.**

I have read and understand GitHub's Guide to Filing a DMCA Notice. I am filing this notice based on the best of my knowledge after conducting my own investigation. This investigation was conducted on [private].

I am the [private] for SkytilsMod, a Minecraft Forge mod that provides quality of life features for Hypixel Skyblock. Skytils is located on GitHub at the repository https://github.com/Skytils/SkytilsMod

SkyblockFeatures appears to be based off a copy of SkytilsMod, available on the 0.x branch of Skytils/SkytilsMod, and contains large amounts of code from SkytilsMod and violates our open-source license.

SkyblockFeatures also infringes on multiple other projects' licenses, however, I am not the copyright holder nor authorized to act as the copyright holder for those projects, so they will not be included in this complaint.

**What files should be taken down? Please provide URLs for each file, or if the entire repository, the repository’s URL.**

https://github.com/MrFast-js/SkyblockFeatures/

The entire repository and its forks must be taken down due to the amount of files that contain code from my project.

**Do you claim to have any technological measures in place to control access to your copyrighted content? Please see our <a href="https://docs.github.com/articles/guide-to-submitting-a-dmca-takedown-notice#complaints-about-anti-circumvention-technology">Complaints about Anti-Circumvention Technology</a> if you are unsure.**

No

**<a href="https://docs.github.com/articles/dmca-takedown-policy#b-what-about-forks-or-whats-a-fork">Have you searched for any forks</a> of the allegedly infringing files or repositories? Each fork is a distinct repository and must be identified separately if you believe it is infringing and wish to have it taken down.**

All forks must be taken down as they include my project's code.  
The only visible fork I see is [invalid], which does not include a license.

**Is the work licensed under an open source license?**

Yes

**Which license?**

Our current branch uses GNU Affero General Public License 3.0 with Exceptions

https://github.com/Skytils/SkytilsMod/blob/1.x/LICENSE.md

However, some code they have copied appears to be from our 0.x branch, which is also GNU Affero General Public License 3.0 available at  
https://raw.githubusercontent.com/Skytils/SkytilsMod/0.x/LICENSE

**How do you believe the license is being violated?**

The project License is incompatible with the GNU Affero General Public License 3.0, the project is licensed under the MIT License, while the fork listed appears not to include a license.
The author makes no attempt at following our license, bundling our code with other code from projects that may have incompatible licenses, or even All Rights Reserved code which does not belong to them.

**What changes can be made to bring the project into compliance with the license? For example, adding attribution, adding a license, making the repository private.**

The License must be compatible with the GNU AGPL 3.0, include license and copyright notice
State the changes made to our code
Remove any code that may not fulfill the terms of the GNU AGPL 3.0 license

**What would be the best solution for the alleged infringement?**

Reported content must be removed

**Do you have the alleged infringer’s contact information? If so, please provide it.**

No, I do not have the contact information.

**I have a good faith belief that use of the copyrighted materials described above on the infringing web pages is not authorized by the copyright owner, or its agent, or the law.**

**I have taken <a href="https://www.lumendatabase.org/topics/22">fair use</a> into consideration.**

**I swear, under penalty of perjury, that the information in this notification is accurate and that I am the copyright owner, or am authorized to act on behalf of the owner, of an exclusive right that is allegedly infringed.**

**I have read and understand GitHub's <a href="https://docs.github.com/articles/guide-to-submitting-a-dmca-takedown-notice/">Guide to Submitting a DMCA Takedown Notice</a>.**

**So that we can get back to you, please provide either your telephone number or physical address.**

[private]

Email is more preferable for contacting me, [private]

**Please type your full legal name below to sign this request.**

[private]

---
## [sertdfyguhi/shitlang](https://github.com/sertdfyguhi/shitlang)@[4639eca21a...](https://github.com/sertdfyguhi/shitlang/commit/4639eca21a1fad3c30ff7e02d5db9b40ec8e205a)
#### Monday 2023-07-17 11:18:30 by sertdfyguhi-git

i hate troubleshooting like what the FUCK is the problem rn

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[63d6c2e962...](https://github.com/tgstation/tgstation/commit/63d6c2e9628be7af04948f59488043f109f1faab)
#### Monday 2023-07-17 11:23:33 by CRITAWAKETS

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
## [SmiLeYre/BlueMoon-Station-13](https://github.com/SmiLeYre/BlueMoon-Station-13)@[183f026a4a...](https://github.com/SmiLeYre/BlueMoon-Station-13/commit/183f026a4a8f883201fcc408c6d42b97167545ac)
#### Monday 2023-07-17 12:55:33 by BongaTheProto

I'm sorry to interrupt you elizabeth

If you still even remember that name.
But I'm afraid you've been misinformed.
You are not here to receive a gift.
Nor, have you been called here by the individual you assume.
Although, you have indeed been called.
You have all been called here.
Into a labyrinth of sounds and smells, misdirection and misfortune.
A labyrinth with no exit, a maze with no prize.
You don't even realize that you are trapped.
Your lust of blood has driven you in endless circles.
Chasing the cries of children in some unseen chamber.
Always seeming so near, yet somehow out of reach.
But, you will never find them, none of you will.
This is where your story ends.

And to you, my brave volunteer.
Who somehow found this job listing not intended for you.
Although, there was a way out planned for you,
I have a feeling that's not what you want.
I have a feeling that you are right where you want to be.

I am remaining as well. I am nearby.
This place will not be remembered.
And the memory of everything that started this.
Can finally begin to fade away.
As the agony of every tragedy should.
And to you monsters trapped in the corridors.
Be still, and give up your spirits.
They don't belong to you.
For most of you, I believe there is peace and perhaps, warm.
Waiting for you after the smoke clears.
Although, for one of you.
The darkest pit of Hell has opened to swallow you whole.
So, don't keep the Devil waiting, old friend.
My daughter, if you can hear me.
I knew you would return as well.
It's in your nature to protect the innocent.
I'm sorry that on that day.
The day you were shut out and left to die.
No one was there to lift you up in their arms.
The way you lifted others into yours.
And then, what became of you?
I should have known, you wouldn't be content to disappear.
Not my daughter. I couldn't save you then, so let me save you now.
It's time to rest, for you, and for those you have carried in your arms.

---
## [SmiLeYre/BlueMoon-Station-13](https://github.com/SmiLeYre/BlueMoon-Station-13)@[defdf2f6b2...](https://github.com/SmiLeYre/BlueMoon-Station-13/commit/defdf2f6b2269cd8fc953ef71219109159ddfcd4)
#### Monday 2023-07-17 12:55:33 by PhazeJump

FIXING MY OWN SHIT CODE MAKES ME FUCKING SCREAM

anyways
techpriest robes are now un-shitty-fixed and fixed again. Should be working properly now. No idea how to get the naga taur sprite working because it was supposed to be added in sand modular but sand modular was the one breaking it all so :shrug:

---
## [UltiMafia/Ultimafia](https://github.com/UltiMafia/Ultimafia)@[dd00c2d0d8...](https://github.com/UltiMafia/Ultimafia/commit/dd00c2d0d8e913bcb1603f69c6fbed21fa309004)
#### Monday 2023-07-17 14:02:22 by Golbolco

feat: Filibuster, Queen Bee, Dignitary, Mechanic, Occultist; Priest rework; Killer Bee is Terrorist (#675)

Most of this code is from /v/ with some tweaks from moi.

Filibuster returns from EM unchanged as a Mafia role.

Queen Bee returns with her same power but now as a Cult role.

Dignitary is a renamed Civilian from EM.

Mechanic returns in full glory: no longer a mere reflexive role, but a
full blown power role that fixes cursed items!!

Occultist is a Cult-sided Traitor-like role, necessary for the Priest
rework.

Priest has been given an additional power returning from EM; if targeted
by a killing role, it will convert its killer based on its alignment.
Villagers turn blue, Mafia turn Traitor, Cultists turn Occultist, and
Indies turn Survivor.

Killer Bee has been renamed Terrorist. This may be controversial.
Refresh yourself that Mafia is a game about racially profiling and
lynching people involved with organize crime, which itself is a form of
domestic terrorism. All Mafiosos are terrorists, yo.

---------

Co-authored-by: joyce <24848927+pikulet@users.noreply.github.com>

---
## [Bjamcham/Paradise](https://github.com/Bjamcham/Paradise)@[a3dc32cf34...](https://github.com/Bjamcham/Paradise/commit/a3dc32cf344dbd441e85f6cbb694b166dc1f5e4b)
#### Monday 2023-07-17 14:02:40 by ATP-Engineer

Fixes issue where Turret Control sprites arent actually updated in previous PR (#21538)

* Removes actual turret file

FUCK

* Fixes turret controllers not actually being changed

GOD DAMNIT.

---
## [IdkSomethingTemporary/ZK-Futurewars-Mod](https://github.com/IdkSomethingTemporary/ZK-Futurewars-Mod)@[0877d01bf1...](https://github.com/IdkSomethingTemporary/ZK-Futurewars-Mod/commit/0877d01bf152917c593a87a28542aaa013f443c9)
#### Monday 2023-07-17 14:25:15 by IdkSomethingTemporary

Power Vacuum - Balancing for striders, commanders and more

**Major Changes:**

Mogul:
Mogul just had an identiy crisis where it's long range missiles wanted it to stay at the back and shell the enemy lines while it's short range EMP and it's high health wanted it to go to the front and fight the enemy, and it didn't help that it's laser tracker being blocked by terrain meant it could almost never fire at it's max range. We already have strider-class strategic artillery in the form of merlin, garmr, liberator and artillery commander so it made more sense to rework Mogul back into it's vanilla role of fire support. Mogul's range gets cut in half while it's DPS goes up massively. It's cost is also cut to distinquish it more from titan

Drones:
All drones now have been tweaked to have a build time close to or equal to their reload time - it feels janky to have drone pads sit empty before startind drone construction, so now drone pads will always be occupied. I've considered just nuking reload from high orbit but that probably would make drones too good vs AA. In practice the rate of new drones should not be changed much. Additionally, PW buildings have had their drone swarms buffied heavily in preperation for project homefront

Funnelweb:
Funnelweb just kinda sucked. at 6400k and no buildpower it's quite weak for a FW strider, so now it's gaining quite a few more abilities to it's toolbox to make it fit more into the support role: 6 responders, 9 fireflies, 3 vipers, 60 BP and a nanoshealth field

Guardian:
Guardian's damage output is massively buffed (in total around 3x) and it now has much higher single target damage in order to give shieldbots a way to deal with heavies in exchange for leaning much more into it's vanilla gimmick of shield drain with around 3k shield drain. The stats are around that of 5 felons. The range has been reduced down to 500 to make it less capable of deleting skirmishers

Reef:
Reef now fits into a much more of a support role. It now has 16 gulls and gulls can now fire against underwater targets in order to prevent cancerous UW comm weapons. Reef now has a buffed disarm missile, an antinuke, a jammer, and an Adv Radar on board all for an 8k package.

**Minor Balance change:**
 - Artillery Commander's heavy conversion kit is now cheaper but the weapons themselves got rebalanced
 - Riot comamnder's Vacuum gun is now far weaker as it could one-shot comms at long range before.
 - Desintergrator for commanders is now more expensive to account for the buffs to ghost commander's cloak.
 - Strike servos are now a bit more expensive and unlock a bit later to give super servos some use
 - Liberator got some of it's upcoming changes early with a slight rework to it's weapon
 - Merlin's rockets are less terrifying to cons and more terrifying to armies
 - Bloom loses it's responder as it was too oppressive
 - Flare loses leash range on it's drone
 - Nebula now has 18 spiculas and ultilise all it's pads for spiculas
 - Spicula how has 3x the HP
 - Responder is now more about buildpower and less about shield health
 - Preserver disarm damage x2.5, disarm time doubled
 - Breaker lost some damage as it was a touch too damaging for it's cost in exchange for armor pen and extra shield damage like hardpoint
 - Disco Rave Party now can fire at it's maximium range and Rainbow Ruiner now releases all it's submunitions upon collidng with a shield (can't be bothered to input the total shield damage of all drp shots)
 - Titan gains armor peircing because why the fuck not
 - The napalm dropped by trailblazer is spread over a smaller area

**Fluff:**
 - Titan's Gigawatt laser renamed to Terawatt laser - Gigawatt just honestly isn't a lot at a stage of the game where strategic and tactical nukes are thrown around like paper airplanes. Terawatt is closer to Titan's level of power when factoring it that it's a small, armor peircing laser
 - "Napalm" regex'd with "Thermite". Thermite is just cooler and scarier than napalm, and mere fire doesn't really make sense to be damaging future death robots anyways

---
## [delingar/FluffySTG](https://github.com/delingar/FluffySTG)@[24cab6d9f9...](https://github.com/delingar/FluffySTG/commit/24cab6d9f91ea45cb420bdac188d3142eebb004b)
#### Monday 2023-07-17 14:29:23 by SkyratBot

Plasma objects no longer violently explode when ignited [MDB IGNORE] (#22216)

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
## [delingar/FluffySTG](https://github.com/delingar/FluffySTG)@[c5f60969da...](https://github.com/delingar/FluffySTG/commit/c5f60969da9465d10482ef0c122428fa42bfcb2c)
#### Monday 2023-07-17 14:29:23 by SkyratBot

Rat RP expansion [MDB IGNORE] (#22204)

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
## [sourcegraph/sourcegraph](https://github.com/sourcegraph/sourcegraph)@[340b0dea25...](https://github.com/sourcegraph/sourcegraph/commit/340b0dea25f073119d0506b8dd3c6228516cf9c4)
#### Monday 2023-07-17 14:35:26 by David Veszelovszki

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
## [Spore-Biometh-team/Spore-expandsion](https://github.com/Spore-Biometh-team/Spore-expandsion)@[ca7a32a85a...](https://github.com/Spore-Biometh-team/Spore-expandsion/commit/ca7a32a85a49b46e05780340f84f7b830552d418)
#### Monday 2023-07-17 15:23:52 by Horizon

It starts with one thing, I don't know why It doesn't even matter how hard you try Keep that in mind I designed this rhyme To explain in due time

All I know Time is a valuable thing Watch it fly by as the pendulum swings Watch it count down to the end of the day The clock ticks life away

It's so unreal Didn't look out below Watch the time go right out the window Tryin' to hold on, did-didn't even know I wasted it all just to watch you go (watch you go!) I kept everything inside and even though I tried It all fell apart

What it meant to me will eventually Be a memory of a time when I tried so hard I tried so hard, and got so far In the end, it doesn't even matter

I had to fall, to lose it all in the end, it doesn't even matter One thing, I don't know why

It doesn't even matter how hard you try Keep that in mind, I designed this rhyme To remind myself how I tried so hard In spite of the way you were mockin' me Acting like I was part of your property Remembering all the times you fought with me I'm surprised it got so far Things aren't the way they were before You wouldn't even recognize me anymore Not that you knew me back then But it all comes back to me in the end You kept everything inside and even though I tried It all fell apart

What it meant to me will eventually Be a memory of a time when I tried so hard I tried so hard, and got so far in the end, it doesn't even matter I had to fall, to lose it all in the end, it doesn't even matter I've put my trust in you Pushed as far as I can go

For all this There's only one thing you should know I've put my trust in you Pushed as far as I can go For all this There's only one thing you should know I tried so hard, and got so far in the end, it doesn't even matter I had to fall, to lose it all in the end, it doesn't even matter

---
## [Katskan/cmss13](https://github.com/Katskan/cmss13)@[d045a5d654...](https://github.com/Katskan/cmss13/commit/d045a5d6547dcda9fc04be9b6cd50d2ff44e672f)
#### Monday 2023-07-17 15:43:47 by Drathek

Larva Queue Late Joiner Nerf (#3803)

# About the pull request

This PR makes it so players who haven't played yet have their join time
recorded, and that is used for their initial sorting value rather than
0. This means late joiners will be at the back of the line as if they
had just died.

This PR also fixes an oversight where ghosting as a facehugger would
count as death. Even though they really shouldn't be ghosting when
alive, they still shouldn't be penalized as far as the queue is
concerned.

# Explain why it's good for the game

Its not; its a bad experience for everyone that hasn't even gotten one
life in the round. However it seems I'm in the minority thinking that a
xeno shouldn't squander their first life and that death shouldn't bear
more consequences.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

The new informational message if you press join as xeno while currently
ineligible to be a xeno candidate:

![image](https://github.com/cmss13-devs/cmss13/assets/76988376/9fb295c2-e654-4843-9e3e-bf37f2c8755e)

</details>


# Changelog
:cl: Drathek
del: Remove first life priority for larva queue
fix: Fix ghosting as a facehugger counting as death for the larva queue
/:cl:

---
## [natanrauber/forgotten-land-server-engine](https://github.com/natanrauber/forgotten-land-server-engine)@[8314f6a3e8...](https://github.com/natanrauber/forgotten-land-server-engine/commit/8314f6a3e8c3b94242d43d4f754a6fb4fccf6461)
#### Monday 2023-07-17 15:44:29 by Spiller

feat: add several missing bosses (#708)

• See the pull request description to read detailed information.

Add bosses from some quests there were not developed. This PR adds only the bosses, levers mechanics for simple functionality.
This doesn't add the bosses mechanics! If someone is willing to contribute with the mechanics, feel free to contribute with the PR.
The bosses added are:

• A pirate's tail: Ratmiral Blackwhiskers, Tentugly's head;
• Adventures of Galthen: Megasylvan Yselda;
• Feaster of Souls: The Fear Feaster, The Unwelcome, The Dread Maiden, Irgix the Flimsy, Unaz the Mean, Vok The Freakish;
• Grave Danger (rework): Lord Azaram, Duke Krule, Count Vlarkorth, Sir Nictros & Sir Baeloc, Earl Osam, King Zelos;
• Grimvale/Ancient Feud: Katex Blood Tongue, Srezz Yellow Eyes, Utua Stone Sting, Yirkas Blue Scales, Bloodback, Darkfang, Sharpclaw, Shadowpelt, Black Vixen;
• Soul War: Goshnar's Cruelty, Goshnar's Greed, Goshnar's Hatred, Goshnar's Malice, Goshnar's Spite, Goshnar's Megalomania;
• The Dream Courts: The Nightmare Beast, Izcandar the Banished, Alptramun, Plagueroot, Malofur Mangrinder, Maxxenius;
• The Secret Library: Ghulosh, Gorzindel, Lokathmor, Mazzinor, Scourge of Oblivion.
• The SoulWar reward was added. In order to get the reward, the player needs to kill all the bosses and the final boss.
• The Dream Court's World change was added.

• All the access needed were granted on FreeQuests.lua. If you are already running a server, you'll need to update freeQuestStage on config.lua to one number higher than it is. So, all the players of your server will have the access granted.

---
## [SuperiorOS-beta/android_frameworks_base](https://github.com/SuperiorOS-beta/android_frameworks_base)@[314284f1b7...](https://github.com/SuperiorOS-beta/android_frameworks_base/commit/314284f1b71523b5e0b84206f19dad05c2c17464)
#### Monday 2023-07-17 15:56:12 by Kuba Wojciechowski

[SQUASHED] core: Blacklist pixel system feature from Google Photos

    We want to include the P21 experience flag to enable new features,
    however it seems like Google Photos uses it to decide whether to use the
    TPU tflite delegate. There doesn't seem to be any fallback so we need to
    make sure the feature is not exposed to the app so that a normal
    NNAPI/GPU delegate can be used instead.

    Test: Google Photos editor with PIXEL_2021_EXPERIENCE feature in product
    Signed-off-by: Kuba Wojciechowski <nullbytepl@gmail.com>
    Change-Id: I51a02f8347324c7a85f3136b802dce4cc4556ac5

commit 67eb31b3bb43d06fcc7f6fdb2f92eb486451cae6
Author: kondors1995 <normandija1945@gmail.com>
Date:   Thu Jun 9 17:39:25 2022 +0530

    Core: Extend Pixel experience Blacklist For Google Photos

    Turns out having these brakes Original quality backups.
    Since these indicate that the device is pixel 4 with in the turn brakes device spoofing as OG pixel

    Change-Id: I336facff7b55552f094997ade337656461a0ea1d

commit 508a99cde60b73dc3f1e843d569bca31def35988
Author: ReallySnow <reallysnow233@gmail.com>
Date:   Fri Dec 31 16:40:23 2021 +0800

    base: core: Blacklist Pixel 2017 and 2018 exclusive for Google Photos

    * In this way can use PixelPropsUtils to simulate the Pixel XL prop
      method to use the unlimited storage space of Google Photos
    * Thanks nullbytepl for the idea

    Change-Id: I92d472d319373d648365c8c63e301f1a915f8de9

commit aaf07f6ccc89c2747b97bc6dc2ee4cb7bd2c6727
Author: Akash Srivastava <akashniki@gmail.com>
Date:   Sat Aug 20 19:04:32 2022 +0700

    core: Pixel experience Blacklist For Google Photos for Android 13

    * See, in Android 13 pixel_experience_2022_midyear was added, which needs to be blacklisted aswell

    Change-Id: Id36d12afeda3cf6b39d01a0dbe7e3e9058659b8e

commit 9d6e5749a988c9051b1d47c11bb02daa7b1b36fd
Author: spezi77 <spezi7713@gmx.net>
Date:   Mon Jan 31 19:17:34 2022 +0100

    core: Rework the ph0t0s features blacklist

    * Moving the flags to an array feels more like a blacklist :P
    * Converted the flags into fully qualified package names, while at it

    Signed-off-by: spezi77 <spezi7713@gmx.net>
    Change-Id: I4b9e925fc0b8c01204564e18b9e9ee4c7d31c123

commit d7201c0cff326a6374e29aa79c6ce18828f96dc6
Author: Joey Huab <joey@evolution-x.org>
Date:   Tue Feb 15 17:32:11 2022 +0900

    core: Refactor Pixel features

    * Magic Eraser is wonky and hard to
      enable and all this mess isn't really worth
      the trouble so just stick to the older setup.

    * Default Pixel 5 spoof for Photos and only switch
      to Pixel XL when spoof is toggled.

    * We will try to bypass 2021 features and Raven
      props for non-Pixel 2021 devices as apps usage
      requires TPU.

    * Remove P21 experience system feature check

Change-Id: Iffae2ac87ce5428daaf6711414b86212814db7f2

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[74892ae7ec...](https://github.com/tgstation/tgstation/commit/74892ae7ec80d47c64bf786f62985a1bd07d06f7)
#### Monday 2023-07-17 15:56:26 by LemonInTheDark

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
## [getsentry/sentry-javascript](https://github.com/getsentry/sentry-javascript)@[0ca73897a8...](https://github.com/getsentry/sentry-javascript/commit/0ca73897a895d1673d0a7b2c3145b10dd52953f3)
#### Monday 2023-07-17 16:10:12 by Lukas Stracke

fix(nextjs): Avoid importing `SentryWebpackPlugin` in dev mode (#8557)

As reported in #8541, our NextJS SDK currently breaks dev mode for the
newest NextJS 13.4.10 version

I still have absolutely no idea which of the changes in
[13.4.10](https://github.com/vercel/next.js/releases/tag/v13.4.10) is
causing this.
However, I traced the error back and it happens as soon as our NextJS
SDK package requires @sentry/webpack-plugin:

* @sentry/nextjs calls `require('@sentry/webpack-plugin')`
* @sentry/webpack-plugin calls `const { RawSource } =
require('webpack-sources');`
* For _whatever_ reason, NextJS can't require `webpack-sources` and
throws

Since we don't enable our Webpack plugin [in dev

mode](https://github.com/getsentry/sentry-javascript/blob/723f851f358b75cd39da353804c51ff27ebb0c11/packages/nextjs/src/config/webpack.ts#L305)
anyway, one way to get rid of this error is to only require it if we're
_not_ in dev mode.

This hotfix therefore moves the top-level require of
`@sentry/webpack-plugin` to a dynamic require. This isn't a great
solution and honestly quite ugly but if it unblocks users for now I'd
say we merge it. I think we should definitely revisit this though once
we know more about why NextJS suddenly isn't able to import
`webpack-sources`.

closes #8541

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[063bf74f31...](https://github.com/tgstation/tgstation/commit/063bf74f31a27ec8096fe10b844d5883be6d13a9)
#### Monday 2023-07-17 16:43:51 by carlarctg

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
## [microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel)@[eab7a8f63a...](https://github.com/microsoft/semantic-kernel/commit/eab7a8f63a0bfd289070e82b423ac78bd306ee5b)
#### Monday 2023-07-17 17:56:48 by Sailesh R

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
## [GingertronMk1/Eldorado](https://github.com/GingertronMk1/Eldorado)@[8d92c0543b...](https://github.com/GingertronMk1/Eldorado/commit/8d92c0543b285f932b760e78ba5a28d9b4ba67ac)
#### Monday 2023-07-17 19:18:40 by Jack Ellis

oh my god fuck you phpstan

he says, having configured phpstan to be the biggest possible dickhead

---
## [Ben10Omintrix/tgstation](https://github.com/Ben10Omintrix/tgstation)@[52c8da7ea4...](https://github.com/Ben10Omintrix/tgstation/commit/52c8da7ea49ef566c9a997a4b7cfc5d3d2a59178)
#### Monday 2023-07-17 19:38:18 by Jacquerel

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
## [Chirynnn/Bubberstation](https://github.com/Chirynnn/Bubberstation)@[54011a20b9...](https://github.com/Chirynnn/Bubberstation/commit/54011a20b903317639fdefb82fa11ad1c03eb710)
#### Monday 2023-07-17 19:41:18 by SkyratBot

[MIRROR] Replaces the syndicate corpse Legions can drop with one without a MODSuit [MDB IGNORE] (#21517)

* Replaces the syndicate corpse Legions can drop with one without a MODSuit (#75700)

## About The Pull Request
This is part of a pass I'm working on doing where I go through and
remove instances of antag gear outside of their normal context. This is
mostly going to involve replacing space/Lavaland ruin gear with
something close to the same power level but not distinctly something
only antags should be able to get. I want to keep ruins rewarding but I
don't want explicit antag gear to be something you can obtain without
needing an uplink.

The first part of this is me removing the MODSuit from the syndicate
operative corpse. The new one drops a turtleneck, a syndicate gas mask,
and gripper gloves.

## Why It's Good For The Game
It's my opinion that antag gear should probably stay in antag hands
unless you manage to kill one or steal an uplink. The main impetus for
this was a discussion I had a while back about how blood red hardsuits
used to _just_ be an antag thing. I kind of miss that general feeling of
paranoia that came from seeing someone wearing it, as opposed to seeing
it these days and just thinking "Yeah, it's probably someone who got it
from space".

In this specific instance, Syndicate MODSuits are pretty strong anyway
and, regardless of the low odds of getting one, I really don't think it
should be available as loot off a fairly easy-to-kill mob.

## Changelog
:cl:
balance: Syndicate corpses dropped from killing a Legion no longer come
with a MODSuit.
/:cl:

* Replaces the syndicate corpse Legions can drop with one without a MODSuit

---------

Co-authored-by: TheVekter <TheVekter@users.noreply.github.com>

---
## [anoopsonar30/drake](https://github.com/anoopsonar30/drake)@[f90899e13f...](https://github.com/anoopsonar30/drake/commit/f90899e13fd6b703ac5c7da3d1b7c0584a793769)
#### Monday 2023-07-17 20:14:05 by Jeremy Nimmer

[geometry] Add Meshcat::GetRealtimeRate (#19700)

Tidy up recent Meshcat changes:
- Add missing pydrake bindings.
- Strongly prefer testing the public API (eschew test-friendship hacks).
  We want to guard against regressions in the end-user experience;
  using private API goes against that goal.
- Fix indentation, typos, and eschew abbreviation.

---
## [Fluffy-Frontier/FluffySTG](https://github.com/Fluffy-Frontier/FluffySTG)@[f17bfbcbad...](https://github.com/Fluffy-Frontier/FluffySTG/commit/f17bfbcbad67d5c2d6d66d1aa61d4893f64acb09)
#### Monday 2023-07-17 20:22:02 by GoldenAlpharex

SPECIES NUKING 2023: Head flags 3 & Knuckles: Fixes some growing pains with head flags [MDB IGNORE] (#22516)

* SPECIES NUKING 2023: Head flags 3 & Knuckles: Fixes some growing pains with head flags  (#76440)

Fixes https://github.com/tgstation/tgstation/issues/76422
This was caused by me somehow not using the wrapper there and not
noticing it

Also fixes hair gradients and facial hair gradients. I am pretty sure
they were uhh, being hidden behind the actual hair/facial hair. Oops.

Also also fixes spawning yourself as a human as admin and getting random
hair colors. That was just a failure to update the icon after updating
everything, I think?

Additionally, to totally babyproof all of this, ensures that head_flags
involved stuff gets applied AFTER species by creating a new preference
priority, and uses two separate wrappers to apply gradient style and
color.

Here's this absolute hellspawn to prove that everything works.

![image](https://github.com/tgstation/tgstation/assets/82850673/7ed29a68-cb60-4b28-996c-3be0e7331be8)

![image](https://github.com/tgstation/tgstation/assets/82850673/e57128be-0d7c-46ad-90dd-ee25981d0fea)

![image](https://github.com/tgstation/tgstation/assets/82850673/5c3619a8-fe6f-42b3-9fdc-12277d568e8d)

![image](https://github.com/tgstation/tgstation/assets/82850673/fdd13000-2220-47ad-8e02-44bc75a4a907)

Sorry for being so damn good at breaking this codebase.

Bugs are bad they make you mad

:cl:
fix: Hair and facial hair gradients work again now
fix: Facial hair colors apply properly again
fix: Admin spawned characters will get hair color preferences applied
properly
/:cl:

* Fixed a compile error (whoops)

* Whoops fixed that wrong

* Okay now I compiled and made sure it was fixed for real, I swear!

---------

Co-authored-by: ChungusGamer666 <82850673+ChungusGamer666@users.noreply.github.com>

---
## [gioui/gio](https://github.com/gioui/gio)@[6ea4119a3c...](https://github.com/gioui/gio/commit/6ea4119a3ceb36f009af1486e41b47f08c2239bd)
#### Monday 2023-07-17 20:36:44 by Chris Waldon

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
## [create-research-and-development-team/Research-And-Development](https://github.com/create-research-and-development-team/Research-And-Development)@[f5c61c09de...](https://github.com/create-research-and-development-team/Research-And-Development/commit/f5c61c09de846c55ca02ea5498f1df93379a9fa3)
#### Monday 2023-07-17 21:15:38 by PriestOfFerns

don't care + didn't ask + ratio + you fell off + cope + seethe + mald + dilate + L + hoes mad + W + cry about it + stay mad + touch grass + pound sand + skill issue + quote tweet + get real + no bitches? + banned + cancelled + suspended + terminated + deleted + kys + you're* + not funny didn't laugh + radio + the audacity + go outside + cringe + get clapped + triggered + ggez + cap + whipped and nae nae'd + i own u + fatherless + motherless + brotherless + motherless + familyless

---
## [newstools/2023-sundiata-post](https://github.com/newstools/2023-sundiata-post)@[89f6b625e3...](https://github.com/newstools/2023-sundiata-post/commit/89f6b625e33231717b9cd92e35da67a0cdf156e2)
#### Monday 2023-07-17 21:18:35 by Billy Einkamerer

Created Text For URL [sundiatapost.com/popular-nigerian-punter-killaboi-confesses-to-killng-his-girlfriend-on-social-media-two-years-after-he-was-arrested-for-internet-fraud-b-efcc/]

---
## [inkoalawetrust/Military-Vehicles-Pack](https://github.com/inkoalawetrust/Military-Vehicles-Pack)@[eb84b38aa9...](https://github.com/inkoalawetrust/Military-Vehicles-Pack/commit/eb84b38aa96ba2e1e75d70906928664ae07555e0)
#### Monday 2023-07-17 21:24:04 by inkoalawetrust

Tank now intentionally runs over enemies & corpses

- Gave the tank the ability to deliberately run over enemies as an attack. If the tanks' enemy is weak enough and not a ranged enemy (e.g a Demon, but not some kind of melee enemy with as much health as a Hell Baron) it will intentionally attack by running them over. Alternatively, it will crush even ranged enemies, as long as they are weak enough, such as Zombiemen.
- Added the ability for the tank to crush corpses like the APC. Also controlled through User_CrushMode, it doesn't affect the tanks' ability to push things out of the way however.
- Doubled the tanks' crushing damage from 6 to 12 per step.
- Finished the hulls' obituaries.
- Fixed a magical regression caused in the corpse seeking code during the GetClosestActor() call.

---
## [Jolly-66/JollyStation](https://github.com/Jolly-66/JollyStation)@[cf70bc7948...](https://github.com/Jolly-66/JollyStation/commit/cf70bc7948f441a9d19fd1a72f027731a56f1334)
#### Monday 2023-07-17 21:45:30 by TaleStationBot

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
## [koreader/koreader-base](https://github.com/koreader/koreader-base)@[b0f7e99845...](https://github.com/koreader/koreader-base/commit/b0f7e99845b16fc4176d3d29e4ffc258baa53cca)
#### Monday 2023-07-17 21:48:21 by NiLuJe

Build: RPATH & escaping cleanup (#1638)

* Stop everything from including crappy build-time rpaths into binaries (lookin' at you, libtool).
* Enforce a set of DT_RPATH on everything we build to ensure we prefer our own libs over the system's.
* Do so via an ld include file, in order to go through all the buildsystem bullshit in order to defeat potential escaping issues.
* In the same vein, rework how we escape things in both makefiles and CMake files, in order to limit the interaction and/or dependency on shell escaping and/or globbing.
* Enforce DT_RPATH over DT_RUNPATH, because it gets honored for transitive dependencies, which will avoid some hilariously stupid things from happening once we get rid of LD_LIBRARY_PATH, which this moves also allows us to do.

Many thanks to @benoit-pierre for his insight, testing and reviews, this would have been way clunkier without his input ;).

---------

Co-authored-by: Benoit Pierre <benoit.pierre@gmail.com>

---
## [ryandotsmith/32k.io](https://github.com/ryandotsmith/32k.io)@[46af85efe0...](https://github.com/ryandotsmith/32k.io/commit/46af85efe0c6c6cf940ddf138c8c9c1127f6e581)
#### Monday 2023-07-17 21:57:45 by Ryan Smith

r/docs: spiritual updates

I'm removing a few of my spiritual posts from the index. They will live
in the history of this repo, but I don't necessarily want to advertise
these thoughts. My views have changed over the last couple of years. I
think I over indexed on emotional experiences. I'm still converging.

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[e8930f5a26...](https://github.com/Buildstarted/linksfordevs/commit/e8930f5a267083397149032f5189514d0e77acd0)
#### Monday 2023-07-17 22:09:29 by Ben Dornis

Updating: 7/17/2023 10:00:00 PM

 1. Added: I
found a (microscopic) ruby bug and it got fixed in 3 hours
    (https://pineman.github.io/ruby-bug-shell-gem.html)
 2. Added: Baby's second garbage collector
    (https://jennyjams.net/blog/copygc/)
 3. Added: Programming Pearls
    (https://book-notes.pages.dev/programming-pearls/)
 4. Added: Writing for Others
    (https://notes.npilk.com/writing-for-others)
 5. Added: Matt Watson | Let me live dangerously, PHP
    (https://www.mattwatson.org/blog/20230716-let-me-live-dangerously-php/)
 6. Added: Setting up PostgreSQL with Ansible
    (https://rischmann.fr/blog/setting-up-postgresql-with-ansible)
 7. Added: Looking for additional maintainers on a few projects
    (https://blog.yossarian.net/2023/07/16/Looking-for-additional-maintainers-on-a-few-projects)
 8. Added: Why kernel drivers in Anti-Cheat aren't so bad
    (https://blog.levitati.ng/articles/6)
 9. Added: Has anyone thought that WFH is just sustainable?
    (https://jetunsetter.com/2023/07/17/has-anyone-thought-that-wfh-is-just-sustainable/)
10. Added: Stop Overengineering
    (https://matt-rickard.com/stop-overengineering)
11. Added: Hamilton’s Quaternions, or, The Trouble with Triples
    (https://mathenchant.wordpress.com/2023/05/17/hamiltons-quaternions-or-the-trouble-with-triples/)
12. Added: Using XPath in 2023
    (https://denizaksimsek.com/2023/xpath/)
13. Added: My two semesters of teaching
    (https://avikdas.com/2023/07/17/my-two-semesters-of-teaching.html)
14. Added: Store age identities inside the TPM: age-plugin-tpm
    (https://linderud.dev/blog/store-age-identities-inside-the-tpm-age-plugin-tpm/)
15. Added: Trophy Jobs
    (https://anuatluru.com/blog/trophyjobs)
16. Added: Let me talk to my algorithms
    (https://blog.erlend.sh/let-me-talk-to-my-algorithms)
17. Added: ASP.NET Community Standup | Reliable web app pattern for .NET
    (https://youtu.be/_dkUZZP8uZY)
18. Added: On .NET Live - Getting Started with ChatGPT in .NET
    (https://youtube.com/watch?v=TXjcssxdA5M)
19. Added: Azure DevOps at a Glance
    (https://jinget.medium.com/azure-devops-at-a-glance-4319d94c26e4)
20. Added: Announcing the HackTogether: Microsoft Teams Global Hack winners - Microsoft 365 Developer Blog
    (https://devblogs.microsoft.com/microsoft365dev/announcing-the-hacktogether-microsoft-teams-global-hack-winners/)

Generation took: 00:09:17.8454578

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[2ee79d7077...](https://github.com/san7890/bruhstation/commit/2ee79d7077804f4e918d6c4bdbe856570cf24a01)
#### Monday 2023-07-17 22:30:11 by Jacquerel

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
## [flutter/.github](https://github.com/flutter/.github)@[231e1d3971...](https://github.com/flutter/.github/commit/231e1d3971f844bbafdbd1ac3da7083257983859)
#### Monday 2023-07-17 23:26:22 by Andrew Kolos

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
## [parkerfreestone/Unreal-Game-Docs](https://github.com/parkerfreestone/Unreal-Game-Docs)@[e5f323643b...](https://github.com/parkerfreestone/Unreal-Game-Docs/commit/e5f323643b6bcb101bd7f1e31cb2ed2c1b18d174)
#### Monday 2023-07-17 23:37:14 by parkern

:memo: holy shit this is the most cringe thing I've ever done... father forgive me.

---

