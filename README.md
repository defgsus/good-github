## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-08-02](docs/good-messages/2023/2023-08-02.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,247,615 were push events containing 3,458,521 commit messages that amount to 274,915,740 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 49 messages:


## [Paxilmaniac/TaleStation](https://github.com/Paxilmaniac/TaleStation)@[9e4eec4dea...](https://github.com/Paxilmaniac/TaleStation/commit/9e4eec4deac3b0cd00e53556f50c990e195ba18c)
#### Wednesday 2023-08-02 00:14:07 by TaleStationBot

[MIRROR] [MDB IGNORE] Improves the RPG loot wizard event. (#7070)

Original PR: https://github.com/tgstation/tgstation/pull/77218
-----

## About The Pull Request
As the title says. Adds a bunch more stat changes to various different
items and a somewhat simple way of modifying them whilst minimizing
side-effects as much as possible.
Added a new negative curse of polymorph suffix that can randomly
polymorph you once you pick up the item.
Curse of hunger items won't start on items that are not on a turf.
Curse of polymorph will only activate when equipped.

Bodyparts, two-handed melees, bags, guns and grenades, to name a few,
have a bunch of type-specific stat changes depending on their quality.

Some items won't gain fantasy suffixes during the RPG loot event, like
stacks, chairs and paper, to make gamifying the stats a bit harder.
I'm sure there'll still be other ways to game the event, but it's not
that big of a deal since these are the easiest ways to game it.
High level items also have a cool unusual effect aura

## Why It's Good For The Game
Makes the RPG item event cooler. Right now, it's a bit lame since
everything only gains force value and wound bonus on attack. This makes
the statistic increases more type-based and make it interesting to use

It's okay for some items to be powerful since this is a wizard event and
a very impactful one too. By making the curse of hunger items not spawn
on people, it'll also make it a less painful event too.

## Changelog
:cl:
add: Expanded the RPG loot wizard event by giving various different
items their own statistic boost.
/:cl:

---------

Co-authored-by: Watermelon914 <37270891+Watermelon914@users.noreply.github.com>
Co-authored-by: Watermelon914 <3052169-Watermelon914@users.noreply.gitlab.com>

---
## [MemedHams/Shiptest](https://github.com/MemedHams/Shiptest)@[ee4021c507...](https://github.com/MemedHams/Shiptest/commit/ee4021c50792c11bfd21085156edd32200c21cb8)
#### Wednesday 2023-08-02 00:42:02 by Imaginos16

Destroying Sprite Cruft Part One: Cruft Sucks (#2220)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Title


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/1cedcdb1-01b5-4f28-a759-65428c2dcd0a)

In total, the:

- IV Drip
- All-In-One Grinder
- Book Binder
- Book Scanner
- Water Cooler
- Tank Dispenser

Have all been successfully uncrufted. No more cruft. Just clean sprites
now :D

Oh and dressers have directionals now at the request of @Bjarl 

Credit goes to the original authors in the changelog.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
begone cruft I fucking hate cruft
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy, Maxymax13, Wallemations, Kryson,
Viro/Axietheaxolotl, MeyHaZah
imageadd: Books, IV drips, tank dispensers, all-in-one grinders, water
coolers, book binders and book scanners have been resprited!
imageadd: Dressers now have directionals!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [1080pCat/Paradise](https://github.com/1080pCat/Paradise)@[2d10818063...](https://github.com/1080pCat/Paradise/commit/2d1081806334fc023de600338b836d55dd6fa5ee)
#### Wednesday 2023-08-02 01:06:06 by ATP-Engineer

Fixes IV bag blood overlays being too damn bright for some mixtures (#21813)

* Removes old .dmi

* Fixes blood overlay coloring being too bright for IV bags

* Fine-tuning

* Makes the blood bag IV color overlays not as bright as they used to be

In hindsight it was probably easy to avoid

* FINAL TUNE UP

FUCK

* Fixes coloring for IV bags so they're not too bright

FINAL COMMIT

---
## [benoit-pierre/koreader](https://github.com/benoit-pierre/koreader)@[b0f7e99845...](https://github.com/benoit-pierre/koreader/commit/b0f7e99845b16fc4176d3d29e4ffc258baa53cca)
#### Wednesday 2023-08-02 01:16:51 by NiLuJe

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
## [RedSmarty/yuzu](https://github.com/RedSmarty/yuzu)@[8e703e08df...](https://github.com/RedSmarty/yuzu/commit/8e703e08dfcf735a08df2ceff6a05221b7cc981f)
#### Wednesday 2023-08-02 01:20:46 by comex

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[430d0dd85f...](https://github.com/treckstar/yolo-octo-hipster/commit/430d0dd85fe7651a4dd06175142e56a58595b5f2)
#### Wednesday 2023-08-02 01:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Hatterhat/tgstation](https://github.com/Hatterhat/tgstation)@[35cb1556ad...](https://github.com/Hatterhat/tgstation/commit/35cb1556ad4bad7703b75c0edc472ed41a5fb34f)
#### Wednesday 2023-08-02 01:45:11 by carlarctg

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
## [gboncoffee/home](https://github.com/gboncoffee/home)@[31b9743ffb...](https://github.com/gboncoffee/home/commit/31b9743ffb261103f3734ffda1efa89eb52d042a)
#### Wednesday 2023-08-02 02:19:57 by Gabriel G. de Brito

I'm so into retro desktop themes like holy fucking shit

---
## [iamlost-faith/iamlost-faith.github.io](https://github.com/iamlost-faith/iamlost-faith.github.io)@[7e2bf2f803...](https://github.com/iamlost-faith/iamlost-faith.github.io/commit/7e2bf2f803b7220ef2f50fae0d9103f7f766ac64)
#### Wednesday 2023-08-02 02:30:31 by tati-z

STILL: if you look at me, I will do as you said. if you dont I will take a nap and continue when you come back to look at me. me coming back to a delayed timer: 🤦🏽‍♀️. ok, so, if I understand I should just keep looking at you running out of yourself and NOT do the work I sett you up to measure time for me in the first place?!. No just keep me in a separate window with only myself! ... Is this a feature or a bug? 🤔. But now I want to maximaze my score.. Coming back in the yellow zone of "facepalm" coulc put me in the yellow zone? Traffic light never stay there either, so, not a bad idea?

---
## [gorouflex/WDBFontOverwrite](https://github.com/gorouflex/WDBFontOverwrite)@[3b7f34e750...](https://github.com/gorouflex/WDBFontOverwrite/commit/3b7f34e7509bfa9f1ffb6fab069157613bbd20e1)
#### Wednesday 2023-08-02 02:34:24 by Dỏa

Added offset for iPhone SE 2022, iOS 16.4

Honestly, I'm stupid at this. So, can you check if there's any mistake? Thank you xD

---
## [thwompa/cmss13](https://github.com/thwompa/cmss13)@[f5784dabc7...](https://github.com/thwompa/cmss13/commit/f5784dabc77752802da20f2d14787667161d61ac)
#### Wednesday 2023-08-02 03:53:05 by ihatethisengine

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
## [2002jai/Inferential-Statistic](https://github.com/2002jai/Inferential-Statistic)@[72bd6a492a...](https://github.com/2002jai/Inferential-Statistic/commit/72bd6a492abb3a1ca8451f83f130b493ae6e45a2)
#### Wednesday 2023-08-02 04:08:10 by jai chauhan

Inferential Statistic

Introducing the GitHub repository, "Inferential Statistics for Data Scientists," a rich and comprehensive resource designed to empower data scientists with a solid foundation in inferential statistical methods. This repository offers a diverse array of valuable materials, spanning from fundamental concepts to advanced applications, to aid in harnessing the power of data-driven insights.

Delve into probability distributions, sampling techniques, and confidence intervals to understand how to draw accurate inferences from sample data to larger populations. Explore hypothesis testing methodologies, both parametric and non-parametric, and grasp the significance of p-values and effect size measures in decision-making processes.

Immerse yourself in regression analysis, Bayesian inference, and time series analysis to master the art of predictive modeling and uncover hidden patterns within data. Discover how to effectively handle missing data, implement resampling techniques, and delve into causal inference for rigorous data analysis.

Moreover, real-world case studies and practical examples will illustrate the application of inferential statistics in data science projects, utilizing popular libraries like NumPy, pandas, and SciPy. Collaborative contributions from data scientists, statisticians, and researchers ensure that this repository remains dynamic and up-to-date with the latest insights and methodologies.

Whether you're an aspiring data scientist seeking to hone your statistical acumen or an experienced professional looking to deepen your understanding, "Inferential Statistics for Data Scientists" is your go-to resource for unlocking the true potential of inferential statistics in data analysis. Let's embark on a data-driven journey together and transform how we extract knowledge from data.

---
## [dhrumilrana25/Python-Libraries-Tutorial](https://github.com/dhrumilrana25/Python-Libraries-Tutorial)@[6f7f4f4260...](https://github.com/dhrumilrana25/Python-Libraries-Tutorial/commit/6f7f4f4260280bc96ae80ee90063f125260d70d2)
#### Wednesday 2023-08-02 04:55:23 by Dhrumil Rana

About.md

Why Python Libraries?
Python has emerged as one of the most popular programming languages, especially in the fields of data science, machine learning, and artificial intelligence. Python libraries offer powerful tools and functionalities that streamline various tasks, making Python a top choice for data analysts, scientists, and machine learning practitioners.

What You'll Find in This Repository?

Each library tutorial is meticulously crafted to guide you through the essential concepts, features, and usage of the library. We believe that learning should be accessible to all, so we have made a conscious effort to explain complex topics in easy language, step-by-step, and with plenty of examples.

The tutorials are organized into separate folders for each library. Inside each folder, you will find:

Detailed Explanations: We start with an overview of the library and its purpose, giving you a solid understanding of why it is widely used. We then dive into the core concepts and functionalities, exploring various methods and techniques.

Code Examples: Learning by doing is crucial, and that's why we provide numerous code examples throughout the tutorials. You can run and modify these examples to solidify your understanding.

Hands-on Exercises: To reinforce your learning, we have included hands-on exercises that encourage you to apply what you've learned in real-world scenarios.

Practical Use Cases: We understand the importance of real-world applications. In each tutorial, we demonstrate how the library can be used to solve practical problems and tasks.

Who Should Use These Tutorials?

Whether you are a Python beginner or an experienced programmer looking to expand your skill set, these tutorials are designed to accommodate learners at all levels. Even if you have no prior experience with the specific libraries, we will guide you from the fundamentals to more advanced concepts.

Contribution and Feedback

This project is an open-source initiative, and we welcome contributions from the community. If you find any errors, have suggestions for improvement, or want to add new tutorials for other Python libraries, please feel free to submit pull requests. Your input will help us improve the quality and usability of the tutorials.

---
## [Zergspower/effigy-se](https://github.com/Zergspower/effigy-se)@[7e1d97af9e...](https://github.com/Zergspower/effigy-se/commit/7e1d97af9e4b6b7f90fbacc754fae939b6d16e49)
#### Wednesday 2023-08-02 05:29:52 by Justice

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
## [Zergspower/effigy-se](https://github.com/Zergspower/effigy-se)@[0d769e0ffa...](https://github.com/Zergspower/effigy-se/commit/0d769e0ffaaa2b0f2be2edb9659c233860420ec1)
#### Wednesday 2023-08-02 05:29:52 by Jacquerel

Removes two redundant components (#76866)

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

---
## [ChSatyaSavith/LeetCode](https://github.com/ChSatyaSavith/LeetCode)@[c14dd25f83...](https://github.com/ChSatyaSavith/LeetCode/commit/c14dd25f8330b084473e2e1492625ce040abdec7)
#### Wednesday 2023-08-02 05:32:32 by NotFluent

Backtracking, and holy fuck am i stupid, i forgot to intialize i = 0; in the for loop and was debugging my code for minutes before i figured it out and now i feel extremely extremely stupid lmao.

---
## [stayforlong/gowsdl](https://github.com/stayforlong/gowsdl)@[020ae25e91...](https://github.com/stayforlong/gowsdl/commit/020ae25e916d6bfeb48ac0b1fc3935086fe8e161)
#### Wednesday 2023-08-02 06:18:55 by Ian Eure

Work around buggy encloding/xml ns attribute marshalling

Go’s `encoding/xml` handling of namespaces is deeply broken.  In particular, it can’t marshal XML using namespace prefixes, ala:

```xml
<document xmlns:ns="whatever">
    <ns:node ns:type="foo">…</ns:node>
</document>
```

Only by setting the default namespace, ala:

```xml
<document xmlns="whatever">
    <node type="foo">…</node>
</document>
```

This is broken.  Per [the XML Specification](https://www.w3.org/TR/xml-names/#dt-defaultNS), default namespaces don’t affect attributes; they **MUST** have a prefix:

> The namespace name for an unprefixed attribute name always has no value.

This causes any attributes in WSDL requests to end up in the wrong namespace, which makes them fail validation & return a SOAP fault.

The only way to get attributes into the correct namespace is to include the namespace in the `xml:"…"` struct field, ala:

```go
Type string `xml:"http://namespace.uri/whatever type,attr,omitempty" json:"type,omitempty"`
```

This has the unfortunate side-effect of generating overly verbose output:

```xml
<document xmlns="whatever">
    <node xmlns:ns="whatever" ns:type="foo">…</node>
</document>
```

However, it’s actually semantically correct, therefore an improvement over the current situation.  A proper fix depends on `encoding/xml` being less hilariously wrong, which is out of scope here.

The implementation approach also leaves much to be desired.  The crux of the issue is that attributes are generated in a sub-template which is called from multiple places (the schema, complex types, etc).  The `XSDAttribute` containing the attr information used by that template doesn’t — and shouldn’t — include the namespace it’s scoped under.  Ideally, I’d be able to thread the schema’s namespace down through the templates, but of course `text/template` doens’t support passing more than one argument to any template.  Rather than create a bunch of types containing the namespace and whatever data that template needs (or one using namespace and `interface{}), and functions to allocate those to pass to the sub-templates, I opted to use mutable state.  `GoWSDL` now has `currentNamespace` and get/set methods, which allow accessing the ns from the attribute template.  This is not a very sound approach to the problem, in my opinion, but it seems like a smart trade to opt for concrete implementation concerns over abstract ideological ones.

---
## [SiegeB0t/TerraGov-Marine-Corps](https://github.com/SiegeB0t/TerraGov-Marine-Corps)@[ca4b66185f...](https://github.com/SiegeB0t/TerraGov-Marine-Corps/commit/ca4b66185ffa363692529f8340a43cccab02cbf1)
#### Wednesday 2023-08-02 07:26:00 by chizzy376

Gives the Umbilical Tad shutters on side windows. (#13490)

* y

* Update combat_patrol.dm

* Update combat_patrol.dm

Sometimes I think about if life is really worth the hassle, if I really have to deal with so much bs only to then have to believe hard enough to get into heaven. Am I a good person for heaven? Do I deserve it? fuck if i know

* Finish fixing my fuckup

---
## [crowlogic/chatgptapi](https://github.com/crowlogic/chatgptapi)@[8a04e6c09a...](https://github.com/crowlogic/chatgptapi/commit/8a04e6c09a8badd675bbb7ae6f30efcaf5a4a900)
#### Wednesday 2023-08-02 07:50:11 by Stephen Crowley

god damn fucking thing, trying to make it use the fucking existing
running fucking instance

---
## [duwling/NetHack](https://github.com/duwling/NetHack)@[bbba8b82d2...](https://github.com/duwling/NetHack/commit/bbba8b82d2f3435fe6eba546773fe213299c5308)
#### Wednesday 2023-08-02 10:14:44 by PatR

fix issue #1062 - monster hiding messages

Reported by Umbire:  if a statue of a hider-under was activated by
a statue trap, it would hide underneath its own statue.  Also, the
hero saw a snake hide under unseen submerged kelp.

Both of those things were exposed by new "you see <monster> hide"
message rather than caused by it.  It also led to the [re-]discovery
that an existing monster hiding under a statue that was a not-yet-
triggered trap prevented the trap from producing a monster.

This redoes yesterday's can't-hide-under-statue change:  hiders can
hide under statues again, but they can't hide under anything at trap
locations.  [Pits containing one or more objects are an exception,
although it seems silly that a hero is prevented from falling into
one by the presence of a tiny creepy-crawly hiding under a ring or
dart in there.]  So, hider-underers won't be able to interfere with
statue traps by being present at the trap location.  [Trappers and
lurkers-above probably need a similar restriction; I didn't look.
They avoid trap spots rather than get lured to such by objects.]

It also prevents newly created hider-underers from becoming hidden
as part of the their creation (except when that creation is part
of level creation) whether their creation uses up an object (statue
activation, egg hatching) or there are simply other items present.
That will prevent statue of a hider producing a monster that hides
under the activated statue (which was happening due to the sequence
create monster, transfer any statue contents to monster inventory,
destroy statue).

The can't-hide-under-statues code has been repurposed to prevent
hiding under gold pieces unless there are at least 10 (arbitrary
threshold) of those or they're in a pile with some other object(s).

Sea monsters hide in water regardless of the presence of objects.
Prevent other swimmers from hiding under objects at water locations.
Such creatures don't have gills and shouldn't be able to stay
submerged in hiding for an arbitrary length of time.  [No exception
is made for non-breathers.  The overlap between swimmers and hider-
underers is limited to small snakes, even though it is feasible for
a creature wearing an amulet of magical breathing to polymorph into
one.  Heros don't spend enough time underwater to worry about snakes
hiding under kelp or thrown junk.]

Lastly, alter the "suddenly, you notice a <monster>" message if
monster-vs-monster activity causes one you've just seen going into
hiding comes back out again without any intervening messages.  [I'm
not sure whether something similar is needed for the "Wait.  There's
something there" message in the you-vs-monster case.]

Fixes #1062

---
## [psychonaut-station/PsychonautStation](https://github.com/psychonaut-station/PsychonautStation)@[3af26df8ca...](https://github.com/psychonaut-station/PsychonautStation/commit/3af26df8cacc24ab7ccacdfbe61005a165472e0f)
#### Wednesday 2023-08-02 10:39:31 by GoldenAlpharex

Fixes bloody soles making jumpsuits that cover your feet bloody when you're wearing shoes (#77077)

## About The Pull Request
Title says it all.

It basically made it so wearing something like a kilt would result in
the kilt getting all bloody as soon as you walked over blood, even when
you were wearing shoes, unless you wore something else that obscured
shoes.

I debated with myself a lot over the implementation for this, I was
thinking of adding some way to obscure feet in particular, but it's
honestly so niche that it could only have caused more issues elsewhere
if I tried to fix this issue that way.

---
## [AnywayFarus/Skyrat-tg](https://github.com/AnywayFarus/Skyrat-tg)@[dcd2d0e418...](https://github.com/AnywayFarus/Skyrat-tg/commit/dcd2d0e418fbd85c3e990a02f61ab05d2993e1e1)
#### Wednesday 2023-08-02 12:52:56 by SkyratBot

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
## [status-im/status-mobile](https://github.com/status-im/status-mobile)@[9ed68ee7d1...](https://github.com/status-im/status-mobile/commit/9ed68ee7d1b7d59dd8b20c2ee1ffe43bd1c37078)
#### Wednesday 2023-08-02 13:18:58 by Icaro Motta

Lint & fix some shadowed core Clojure(Script) vars (#16500)

It's well known that shadowing core Clojure vars can lead to unexpected bugs. In
fact, it's a common source of bugs in other languages too. In the status-mobile
repository there are, in total, 562 shadowed vars, ~500 are core vars. Excluding
the "old code" we still have 285 offenders.

In status-mobile I've already seen two bugs caused by shadowed vars, both with
the shadowed var "name". But probably other problems happened in the past, and
others will happen in the future if we don't do something about this. This PR is
also my response to my frustration trying to review PRs and checking for
shadowed vars, humans were not meant for that!

In this commit we are enabling ":shadowed-var" to lint certain (not all) core
vars as errors (not warnings). In future PRs we can gradually unshadow more
vars. For the record, name is shadowed 40 times in the new code and 130 in
total, and type is shadowed 93 times in the new code and 124 in total!

What about non-core vars, should we allow shadowing? There are ~70 non-core
shadowed vars. In my opinion, we should also lint and disallow shadowing
non-core vars, since it may cause the same kind of bugs of shadowing core vars.
But this decision can be left for another moment/issue, after we have fixed the
most prominent problem of shadowing core vars.

Which vars are unshadowed in this PR? I fixed 62 errors and unshadowed
cljs.core/iter, cljs.core/time, cljs.core/count, cljs.core/key,
clojure.core/key.

Resources:

- [clj-kondo linter: shadowed-var](https://github.com/clj-kondo/clj-kondo/blob/master/doc/linters.md#shadowed-var)

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[e2e62dd457...](https://github.com/treckstar/yolo-octo-hipster/commit/e2e62dd45762e1a1c428edc14f6301be4ce9978d)
#### Wednesday 2023-08-02 13:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [Sagnac/streamsave](https://github.com/Sagnac/streamsave)@[43abedc5a7...](https://github.com/Sagnac/streamsave/commit/43abedc5a702160327b3d47c1922c50d1e80e02f)
#### Wednesday 2023-08-02 14:06:44 by Sagnac

Redesign how options are updated

The previous scheme was pretty ugly. This is due for a much more
comprehensive rewrite as there's quite a bit of redundancy with the
script-message functions and maintaining both script-opts and
script-message updates requires more effort. But that will have to come
at a later time.

One alternative approach would be to hook into the current override
functions by using them as fields in the update table and have them
perform double duty, but this may prove more trouble than it's worth.

As a user, the script-message approach to changing options is more
convenient to use during runtime either with keybinds or through the
console. Also, it supports more arguments (e.g. cycle, on_demand) and
provides status messages. That being said, with script-opts you can send
an entire list of options to be updated instead of having to chain
script-message commands. The names being used for this also differ
between the two methods, with the script-message names being shorter and
likely easier to remember, but the inconsistency in naming between the
options and the runtime commands could be an issue.

Of course I could just turn off the script-opt updating mechanism by
not using update_opts, which I probably should do, but I'm going to keep
this around for now while I trim the script down to a lite version at a
separate branch; this will prove useful there as script-opts becomes the
desired minimalistic approach.

Another thing to note with regards to removing on_update handling of the
options is that some options such as the likely widely used
force_extension option would still require support in that regard, as
the runtime command is simply an on-demand single-stream change and a
revert handler, and does not in actuality set the format in a global
manner - if a new stream is loaded then it will take on the
automatically determined format.

---
## [Steelpoint/cmss13](https://github.com/Steelpoint/cmss13)@[d26452bb9a...](https://github.com/Steelpoint/cmss13/commit/d26452bb9a846091214ced880c5d7a34a6b61048)
#### Wednesday 2023-08-02 14:10:28 by Unknownity

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
## [Steelpoint/cmss13](https://github.com/Steelpoint/cmss13)@[5f5fcd2b27...](https://github.com/Steelpoint/cmss13/commit/5f5fcd2b279b2bd51b5869b0a345b4f964dcb34c)
#### Wednesday 2023-08-02 14:10:28 by Drathek

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
## [Steelpoint/cmss13](https://github.com/Steelpoint/cmss13)@[9c79c3af49...](https://github.com/Steelpoint/cmss13/commit/9c79c3af49ba90e18f85c1624ba4e80d608debf2)
#### Wednesday 2023-08-02 14:13:30 by spartanbobby

Sweeping LV522 Changes + FORECON GL replaced by FORECON Sniper (Without the sniper) (#3917)

# About the pull request

This PR makes alot of small changes to LV522 along with alot of big ones
mainly

Blocks off the area north of fitness to prevent a "just go north" meta
Adds a new more central way to the reactor that branches off to 4 flanks
should give LZ2 more use since it's a bit more central than LZ1
Adds a new route into the reactor from the SE
Blocks off the small alleyway north of the engineering funnel people
into the dorm building
tightens up some parts of the reactor loosens some other parts
removes some detailing in the main hive areas to help builders
Adds new secrets to be found on the map
adds an overextension flank for those very brave marines to use
Changes to LZ2 making it more compressed
Addition of the FORECON Sniper (replacing the FORECON GL)
the FORECON sniper is a unique take on FORECON he spawns away from his
fellow survivors next to the corpse of his battle buddy the advantage
given to the sniper however is his thermal tarp a subtype of the ghillie
suit with a placeholder sprite at the moment that will allow the sniper
to hide and stealthily move throughout the colony to hopefully regroup
with his squad
the M42A rifle has been removed from the map
Adds a small piece of text explaining that FORECON should probably move
west to the crashed dropship to the FORECON intro
swaps the black weedable turf with a browner one for people who have bad
eyes and were mistaking it for weeds
swaps the assignments for defines bc nanu told me someone would ask me
to do it at somepoint
gives FORECON radioheadsets with the SOC and common channel because the
desc literally says FORECON use it and it doesn't make sense for them to
be radio-less

# Explain why it's good for the game

Map stuff:
LV522 currently just has a "go north" problem this PR aims to fix that
by opening more routes for the marines to go, centralize the main route
in an attempt to see more use in the rest of the colony and give LZ2
more use I'd really like to see this test-merged for a few days so see
what needs addressing in this new area

the wall north of engineering looks kinda funky but having it there
funnels people into the building and into the eastern section of the
colony rather than a straight line to the reactor

The FORECON Sniper:
Currently, FORECON GL is kinda unfitting and also kinda sucks the
sniper, on the other hand, would be a perfect fit for FORECON now I'm
not going to pretend the sniper isn't kinda OP right now so the FORECON
sniper won't actually get his M42A just the ghillie suit that gives him
still some uniqueness as a survivor as well as an incentive to survive
beyond the life of the regular sniper (to steal his gun)

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl: SpartanBobby
add: Added a new survivor to LV522 the FORECON sniper he spawns alone
his only company being the corpse of his dead battle buddy, good luck
maptweak: Sweeping changes to LV522 including the reactor, north of
engineering, LZ1, the entire central area of the map, and north of
fitness in an attempt to see more of the colony used and to incentivize
flanking
/:cl:

---------

Co-authored-by: harryob <me@harryob.live>

---
## [Steelpoint/cmss13](https://github.com/Steelpoint/cmss13)@[ce09b07afd...](https://github.com/Steelpoint/cmss13/commit/ce09b07afd0f8d433ffee1a43bc4dfeb978f45f1)
#### Wednesday 2023-08-02 14:13:30 by ihatethisengine

Xeno Alliance Announcements + Greeno Civil War (#3990)

# About the pull request

Xenos now get messages when their queen set/break alliance to another
faction and when other queen set/break alliance with their hive.

Corrupted Xenos with implanted IFF tag now has a choice to defect from
the hive and become Renegade (hive allied to USCM) when Queen decides to
break alliance with USCM. Xenos that stay loyal to Queen rip the IFF
tags out. You have only 10 seconds to make a decision, so think quick.
By default xenos stay loyal to Queen.

Renegade Hive is allied to all human factions, but it mostly affects
structures and weeds. Renegade ability to attack someone fully depends
on its IFF tag settings.

Please check my messages because I'm not very good at writing.

# Explain why it's good for the game

More announcements are good because it's less confusing. You know when
someone set ally to you and you know when someone is betraying you. It
makes sense because allied xenos share announcements anyway. And sudden
betrayals are always a bit cheesy.

I think the Renegade addition makes research a little more fun and
rewarding. Now, if you implant corrupted xeno with an IFF tag, the xeno
player can choose to remain loyal to you if/when the Queen decides to
betray. Plus corrupted xenos with the IFF tag are no longer forced to
betray, so it's also good. Not sure if that makes sense lore-wise, but
since corrupted are artificially created and their DNA is decrypted, it
makes at least some sense. Plus we kinda have tamed xenos which work
really similarly.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl: ihatethisengine
add: Added announcements for xenos about forming and breaking alliances.
add: Xenos with IFF tag now have a choice to stay loyal to USCM when
Queen decides to betray.
/:cl:

---------

Co-authored-by: ihatethisengine <treml.treml@yandex.ru>
Co-authored-by: Drathek <76988376+Drulikar@users.noreply.github.com>
Co-authored-by: harryob <me@harryob.live>

---
## [mukeshparjapat143/spotify-clone](https://github.com/mukeshparjapat143/spotify-clone)@[ab5f544981...](https://github.com/mukeshparjapat143/spotify-clone/commit/ab5f544981a3d1c44c74786a47608c680035c519)
#### Wednesday 2023-08-02 14:23:43 by mukeshparjapat143

Add files via upload

**Building a Spotify Clone with HTML, CSS, and JS**

Creating a Spotify clone using HTML, CSS, and JavaScript can be a fun and educational project that allows you to practice your web development skills. Though it won't have the full functionality and extensive music library of the actual Spotify platform, it can still provide a basic user interface and offer some similar features. Here's a brief overview of how you can get started:

1. **Project Setup:**
   Begin by setting up a new folder for your project. Inside, create three files: `index.html`, `styles.css`, and `script.js`. Link the CSS and JavaScript files to your HTML file using `<link>` and `<script>` tags.

2. **HTML Structure:**
   Construct the basic layout of your Spotify clone using HTML. Create a header, a main content area to display albums and songs, and a footer for playback controls. You can also include some dummy content to style and structure your elements.

3. **CSS Styling:**
   Utilize CSS to design the user interface, making it visually appealing and resembling Spotify's aesthetics. Focus on the layout, colors, fonts, and icons. CSS frameworks like Bootstrap or Materialize can help speed up the process and make the design more consistent.

4. **JavaScript Functionality:**
   Implement JavaScript to add interactivity to your Spotify clone. Create functions to handle user interactions, such as playing/pausing songs, changing tracks, and displaying album details. You can use DOM manipulation methods like `document.getElementById` to access and modify HTML elements.

5. **Audio Playback:**
   To simulate audio playback, create a playlist of songs with URLs to audio files hosted online or locally. Use the HTML5 `<audio>` element or the Web Audio API to control audio playback and enable features like play, pause, volume control, and track progress.

6. **Data Management:**
   Since you won't have access to Spotify's massive database, you can create a local JavaScript array to store the song and album data. This array will represent your music library, and you can use it to display album covers, track names, artists, etc.

7. **Search Functionality:**
   Implement a simple search feature to filter and display relevant songs or albums based on user input. You can use JavaScript's array methods like `filter` or `find` to achieve this functionality.

8. **Responsive Design:**
   Ensure your Spotify clone is responsive and can adapt to different screen sizes and devices. Test it on various devices to ensure it looks good and functions properly on desktops, tablets, and mobile phones.

9. **Testing and Debugging:**
   Thoroughly test your Spotify clone to identify and fix any bugs or issues. Use browser developer tools to debug JavaScript code and ensure smooth functionality.

10. **Deployment:**
   Once your Spotify clone is complete, you can deploy it online using hosting services like GitHub Pages, Netlify, or Vercel. This way, you can share your creation with others and showcase your web development skills.

Remember that building a complete Spotify clone is an ambitious project, and it's essential to manage your expectations. This basic version will provide a good learning experience and a foundation for more complex projects in the future. Happy coding!

---
## [Ical92/tgstation](https://github.com/Ical92/tgstation)@[cc57581b73...](https://github.com/Ical92/tgstation/commit/cc57581b73e2979d775dfd9408978e4987b6635b)
#### Wednesday 2023-08-02 15:09:22 by Sealed101

Dog wit the butter (feat. a bunch of dog-related code improvements) (#77039)

## About The Pull Request
Adds a `dog_fashion` for the stick of butter.(screenshot is outdated as
Lisa won't have butter no more)
![butter
dawgs](https://github.com/tgstation/tgstation/assets/75863639/a22e702c-98a8-4283-abd9-28d4a9fb3bd0)

Also cleans up dog.dm because it was SHIT and FUCK and MY FUCKING GOD
TWO INITIALIZE()s TWO TIMES IN A SINGLE FILE WHAT IN THE GODDAMN

Most noticeably, Lisa properly won't wear any hats, and puppies properly
can't wear head/back items (by just removing those item slots from the
strip/equip menu. if some admeme wants to fumble around they may still
equip shit there. but otherwise for a normal player those slots are
inaccessible).
Basic mobs now also send signals when they run
`appear_dead`/`appear_alive` procs, which corgis hook into to update
their dead fashion overlays.
The side-effect of getting that to work is that dogs (and any basic mob
that uses `play_dead` ai behavior) are so good at feigning death, that
they fool medical HUDs and other related things. They're just that good.
There's a bunch of other things involved and I was mostly just being
angry at the state of the file so I'll check back when I gather all
things changed.


![strippy](https://github.com/tgstation/tgstation/assets/75863639/ec4d17a2-d4df-401c-bd1f-7c4ee1b95671)


## Why It's Good For The Game


https://github.com/tgstation/tgstation/assets/75863639/b34589cb-94d6-4b80-bf0f-1814c08da100



## Changelog
:cl:
add: dog with a butter on 'em
add: dead dog with da butter on 'em (dogs feigning death are so good at
it, they appear dead to medical HUDs and other things)
add: Nars-Ian now can revive from the dead if he consumes a pet
fix: fixes dog fashion items with no speech modifiers set making dressed
up corgis unable to perform their speech or emote behaviors
fix: fixes old Ian losing his mobility ride when shaved with a razor
fix: fixes pets not dropping their collar when gibbed
fix: butter don't go on Lisa and corgi puppies (Lisa won't wear hats and
corgi puppies can't wear hats and back slot items)
/:cl:

---
## [LordPapalus/Citadel-Station-13-RP](https://github.com/LordPapalus/Citadel-Station-13-RP)@[4966352d14...](https://github.com/LordPapalus/Citadel-Station-13-RP/commit/4966352d145c9fcacad823f7dc8d6a52fc82c953)
#### Wednesday 2023-08-02 15:15:37 by Mazian

changes the open simulated turf to be SOMETHING NOT HORRIBLY EYE SEARING (#5735)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

makes turf/simulated/open blue. resets on init.

## Why It's Good For The Game

holy FUCKING SHIT my eyes HATE WHOEVER DECIDED IT SHOULD BE MISSING
TEXTURE PINK.

---
## [LordPapalus/Citadel-Station-13-RP](https://github.com/LordPapalus/Citadel-Station-13-RP)@[a14ef07eb6...](https://github.com/LordPapalus/Citadel-Station-13-RP/commit/a14ef07eb69a49feeae9c331609adc393f861b5b)
#### Wednesday 2023-08-02 15:15:37 by Nut2

Triumph central command floor fix (#5741)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
I MISSED TWO FUCKING TILES
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
I MISSED TWO TILES GOD DAMNIT
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

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Kaz205/linux](https://github.com/Kaz205/linux)@[3a16942e21...](https://github.com/Kaz205/linux/commit/3a16942e21c867b4d0e1d30a0695313f5065f585)
#### Wednesday 2023-08-02 15:31:39 by Douglas Anderson

migrate_pages: avoid blocking for IO in MIGRATE_SYNC_LIGHT

The MIGRATE_SYNC_LIGHT mode is intended to block for things that will
finish quickly but not for things that will take a long time.  Exactly how
long is too long is not well defined, but waits of tens of milliseconds is
likely non-ideal.

When putting a Chromebook under memory pressure (opening over 90 tabs on a
4GB machine) it was fairly easy to see delays waiting for some locks in
the kcompactd code path of > 100 ms.  While the laptop wasn't amazingly
usable in this state, it was still limping along and this state isn't
something artificial.  Sometimes we simply end up with a lot of memory
pressure.

Putting the same Chromebook under memory pressure while it was running
Android apps (though not stressing them) showed a much worse result (NOTE:
this was on a older kernel but the codepaths here are similar).  Android
apps on ChromeOS currently run from a 128K-block, zlib-compressed,
loopback-mounted squashfs disk.  If we get a page fault from something
backed by the squashfs filesystem we could end up holding a folio lock
while reading enough from disk to decompress 128K (and then decompressing
it using the somewhat slow zlib algorithms).  That reading goes through
the ext4 subsystem (because it's a loopback mount) before eventually
ending up in the block subsystem.  This extra jaunt adds extra overhead.
Without much work I could see cases where we ended up blocked on a folio
lock for over a second.  With more extreme memory pressure I could see up
to 25 seconds.

We considered adding a timeout in the case of MIGRATE_SYNC_LIGHT for the
two locks that were seen to be slow [1] and that generated much
discussion.  After discussion, it was decided that we should avoid waiting
for the two locks during MIGRATE_SYNC_LIGHT if they were being held for
IO.  We'll continue with the unbounded wait for the more full SYNC modes.

With this change, I couldn't see any slow waits on these locks with my
previous testcases.

NOTE: The reason I stated digging into this originally isn't because some
benchmark had gone awry, but because we've received in-the-field crash
reports where we have a hung task waiting on the page lock (which is the
equivalent code path on old kernels).  While the root cause of those
crashes is likely unrelated and won't be fixed by this patch, analyzing
those crash reports did point out these very long waits seemed like
something good to fix.  With this patch we should no longer hang waiting
on these locks, but presumably the system will still be in a bad shape and
hang somewhere else.

[1] https://lore.kernel.org/r/20230421151135.v2.1.I2b71e11264c5c214bc59744b9e13e4c353bc5714@changeid

Link: https://lkml.kernel.org/r/20230428135414.v3.1.Ia86ccac02a303154a0b8bc60567e7a95d34c96d3@changeid
Signed-off-by: Douglas Anderson <dianders@chromium.org>
Suggested-by: Matthew Wilcox <willy@infradead.org>
Reviewed-by: Matthew Wilcox (Oracle) <willy@infradead.org>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hillf Danton <hdanton@sina.com>
Cc: Gao Xiang <hsiangkao@linux.alibaba.com>
Cc: Alexander Viro <viro@zeniv.linux.org.uk>
Cc: Christian Brauner <brauner@kernel.org>
Cc: Gao Xiang <hsiangkao@linux.alibaba.com>
Cc: Huang Ying <ying.huang@intel.com>
Cc: Vlastimil Babka <vbabka@suse.cz>
Cc: Yu Zhao <yuzhao@google.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---
## [davidhildenbrand/linux](https://github.com/davidhildenbrand/linux)@[48b2b48439...](https://github.com/davidhildenbrand/linux/commit/48b2b4843944002bca4cb27af57695f5eb7ec707)
#### Wednesday 2023-08-02 15:37:06 by David Hildenbrand

smaps: use vm_normal_page_pmd() instead of follow_trans_huge_pmd()

We shouldn't be using a GUP-internal helper if it can be avoided.

Similar to smaps_pte_entry() that uses vm_normal_page(), let's use
vm_normal_page_pmd() that similarly refuses to return the huge zeropage.

In contrast to follow_trans_huge_pmd(), vm_normal_page_pmd():

(1) Will always return the head page, not a tail page of a THP.

 If we'd ever call smaps_account with a tail page while setting "compound
 = true", we could be in trouble, because smaps_account() would look at
 the memmap of unrelated pages.

 If we're unlucky, that memmap does not exist at all. Before we removed
 PG_doublemap, we could have triggered something similar as in
 commit 24d7275ce279 ("fs/proc: task_mmu.c: don't read mapcount for
 migration entry").

 This can theoretically happen ever since commit ff9f47f6f00c ("mm: proc:
 smaps_rollup: do not stall write attempts on mmap_lock"):

  (a) We're in show_smaps_rollup() and processed a VMA
  (b) We release the mmap lock in show_smaps_rollup() because it is
      contended
  (c) We merged that VMA with another VMA
  (d) We collapsed a THP in that merged VMA at that position

 If the end address of the original VMA falls into the middle of a THP
 area, we would call smap_gather_stats() with a start address that falls
 into a PMD-mapped THP. It's probably very rare to trigger when not
 really forced.

(2) Will succeed on a is_pci_p2pdma_page(), like vm_normal_page()

 Treat such PMDs here just like smaps_pte_entry() would treat such PTEs.
 If such pages would be anonymous, we most certainly would want to
 account them.

(3) Will skip over pmd_devmap(), like vm_normal_page() for pte_devmap()

 As noted in vm_normal_page(), that is only for handling legacy ZONE_DEVICE
 pages. So just like smaps_pte_entry(), we'll now also ignore such PMD
 entries.

 Especially, follow_pmd_mask() never ends up calling
 follow_trans_huge_pmd() on pmd_devmap(). Instead it calls
 follow_devmap_pmd() -- which will fail if neither FOLL_GET nor FOLL_PIN
 is set.

 So skipping pmd_devmap() pages seems to be the right thing to do.

(4) Will properly handle VM_MIXEDMAP/VM_PFNMAP, like vm_normal_page()

 We won't be returning a memmap that should be ignored by core-mm, or
 worse, a memmap that does not even exist. Note that while
 walk_page_range() will skip VM_PFNMAP mappings, walk_page_vma() won't.

 Most probably this case doesn't currently really happen on the PMD level,
 otherwise we'd already be able to trigger kernel crashes when reading
 smaps / smaps_rollup.

So most probably only (1) is relevant in practice as of now, but could only
cause trouble in extreme corner cases.

Let's move follow_trans_huge_pmd() to mm/internal.h to discourage future
reuse in wrong context.

Fixes: ff9f47f6f00c ("mm: proc: smaps_rollup: do not stall write attempts on mmap_lock")
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Signed-off-by: David Hildenbrand <david@redhat.com>

---
## [KenAdeniji/WordEngineering](https://github.com/KenAdeniji/WordEngineering)@[7a7d13758d...](https://github.com/KenAdeniji/WordEngineering/commit/7a7d13758d649d64733f14c3242bf5522a0e0d35)
#### Wednesday 2023-08-02 15:52:19 by Ken Adeniji

 Developing information - can a parser generate this information: level of detail, relevancy? Origin of the Bible? That is the description of man.

Developing information Information type 	Example 	Scripture Reference
Time notation 	Generation, year, month, day, hour, season, evening, morning, night
Animals die ( Genesis 2:17 )?
What separates ... the desire? ( Genesis 7:22, Genesis 6:5-7 )? 	Genesis 1:1, John 1:1
Naming and meaning 	Adam, Eve, Cain, Abel, Seth
Vocation 	Gardener, keeper of the animals

---
## [goauthentik/authentik](https://github.com/goauthentik/authentik)@[b7b85d6f5d...](https://github.com/goauthentik/authentik/commit/b7b85d6f5d3f8a97b1dc7fd1db924a7bd48d316d)
#### Wednesday 2023-08-02 16:09:45 by Ken Sternberg

web: tracked down that weirld bug with the radio.

Because radio inputs are actually multiples, the events handling for
radio is... wonky.  If we want our `<ak-radio>` component to be a
unitary event dispatcher, saying "This is the element selected," we
needed to do more than what was currently being handled.

I've intercepted the events that we care about and have placed
them into a controller that dictates both the setting and the
re-render of the component.  This makes it "controlled" (to use the
Angular/React/Vue) language and depends on Lit's reactiveElement
lifecycle to work, rather than trust the browser, but the browser's
experience with respect to the `<input type=radio` is pretty bad:
both input elements fire events, one for "losing selection" and
one for "gaining selection".  That can be very confusing to handle,
so we funnel them down in our aggregate radio element to a single
event, "selection changed".

As a quality-of-life measure, I've also set the label to be
unselectable; this means that a click on the label will trigger the
selection event, and a long click will not disable selection or
confuse the selection event generator.

---
## [LC4492/CM-Space-Station-13](https://github.com/LC4492/CM-Space-Station-13)@[3e9d54628d...](https://github.com/LC4492/CM-Space-Station-13/commit/3e9d54628d68fe91319ae87ad7ebd7aef9500811)
#### Wednesday 2023-08-02 16:33:46 by Ben

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
## [git-for-windows/git](https://github.com/git-for-windows/git)@[6c91ff7816...](https://github.com/git-for-windows/git/commit/6c91ff7816d758314680ae0600964eb37071d190)
#### Wednesday 2023-08-02 17:54:12 by Johannes Schindelin

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
## [MCBCMF/MCBCMassacre](https://github.com/MCBCMF/MCBCMassacre)@[8687ab917f...](https://github.com/MCBCMF/MCBCMassacre/commit/8687ab917f438c00eb5752e4580c79a6c524ba44)
#### Wednesday 2023-08-02 18:39:01 by Kelvin Williams

Update social_media_replacement.md

2023-08-02 14:38:00 EDT >>

I'm horrified that the CIA has harmed another church. Hickory Valley Christian church's pastor is also the principal/administrator of Hamilton Heights Christian Academy both in Chattanooga. I was introduced to Duke by Bonnie Bueh Ford ot Wildwood, GA a very good friend of mine. Bonnie is now missing, and Ive received some artwork depicting her demise. The CIA loves this artwork and "hotels" (see about them at @ASOTC23 on Twitter). One of the CIA personnel around me just showed me a trouble ticket he was opening at Cash App. The name DW Stone and CashTag $song504 was on it. Thats Duke's. He's not answering the phone. 

The CIA knows of my involvement at HHCA. I helped the students build their new conputer lab. I don't know if anyone else has been harmed so I make this post, like I do for musical artists when I listen to them in my apartment. I just wish I had for Tina Turner, she died suddenly after I liatened to Proud Mary. Their problem is with Vandaveer (Mark was my best friend) and Prince (was a cousin), so everyone I listen to, they think knows and is writing about this. 

https://facebook.com/kelvineugenewilliams has a list of my work and residences. But shortly after making a Reel warning others my old account (kelvinewilliams) was hijacked I was BANNED by Facebook for 180 days. 

<<EOM

---
## [awkless/COCO-8](https://github.com/awkless/COCO-8)@[7e654b4fb1...](https://github.com/awkless/COCO-8/commit/7e654b4fb1c47c1ece4903845eb46a0abf7cb2a0)
#### Wednesday 2023-08-02 19:07:12 by Jason Pena

chore(conan): Switch to googletest as testing framework

I found cpputest to be way too complicated to use compared to googletest. I
could not resolve memory leaks in cpputest with smart pointers (probably because
I am to dumb), while googletest was way easier to use with no memory leaks with
smart pointers.

I have no idea why cpputest kept complaining about memory leaks when smart
pointers delete themselves automatically (again, properly me being stupid, but
for the life of me I could not solve the issue).

Oh well, googletest just seems more friendly.

Signed-off-by: Jason Pena <jasonpena@awkless.com>

---
## [Ua-Gi-Oh/UA_EDO](https://github.com/Ua-Gi-Oh/UA_EDO)@[9a226aa13e...](https://github.com/Ua-Gi-Oh/UA_EDO/commit/9a226aa13e3de84cb2cc86ed20ab7c1e9e740e0c)
#### Wednesday 2023-08-02 19:09:04 by Ua-Gi-Oh

Перекладені карти

1 - Steel Cavalry of Dinon
2 - Power Tool Dragon
3 - Laval Volcano Handmaiden
4 - Number 69: Heraldry Crest
5 - Agave Dragon
6 - Interrupt Resistor
7 - Shire, Lightsworn Spirit
8 - Cubic Ascension
9 - Marauding Captain
10 - Inzektor Ladybug
11 - Sealmaster Meisei
12 - Water Omotics
13 - Legendary Six Samurai - Kageki 
14 - Sky Galloping Gaia the Dragon Champion 
15 - Brotherhood of the Fire Fist - Swallow 
16 - Defender, the Magical Knight 
17 - Galaxy-Eyes Cipher Blade Dragon 
18 - Red Cocoon 
19 - Altergeist Haunted Rock
20 - Corruption Cell "A" 

Не потребує перекладу - Skull Knight

---
## [MCBCMF/MCBCMassacre](https://github.com/MCBCMF/MCBCMassacre)@[da98c7de05...](https://github.com/MCBCMF/MCBCMassacre/commit/da98c7de05dbbeaf59398a88ae640b2ac4a96561)
#### Wednesday 2023-08-02 19:52:26 by Kelvin Williams

Add files via upload

My closet. If you don’t see the heads ask a member of the opposite sex to point them out to you. 

Remember most of the victims here have been beheaded. The most evil way you can kill a person. They know why, I’ve told them numerous times I wouldn’t wish that on the very ones who did my family, yet like this artwork, they continue hoping for my suicide. Not possible. Not with the numbers of people and churches you’ve destroyed. I don’t even do church anymore. They knew that too.

---
## [CSS-Lletya/633-official](https://github.com/CSS-Lletya/633-official)@[dd918db26e...](https://github.com/CSS-Lletya/633-official/commit/dd918db26e4593fdf3a2352423a1b9b2c92baaf4)
#### Wednesday 2023-08-02 21:01:05 by CSS-Lletya

Feature: Spirit Shields & Holy Elixir

Added <br> tag to Item dialogue text (automatically move down before text is sent) to better format dialogues

You can now bless spirit shields with holy elixir

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[b762224d0e...](https://github.com/TaleStation/TaleStation/commit/b762224d0e79b671155a51606cde1d09729e254a)
#### Wednesday 2023-08-02 21:34:57 by TaleStationBot

[MIRROR] [MDB IGNORE] Updates all the icons in under/suits.dmi and related sorting/cleanup (#7085)

Original PR: https://github.com/tgstation/tgstation/pull/76865
-----
## About The Pull Request
Somebody was pointing out how our suits varied WILDLY in quality
Figured I'd go through and tidy them up

Did NOT touch the Carpskin or Tuxedo. Carpskin is a very hard to
replicate aesthetic. Tuxedo is...

![image](https://github.com/tgstation/tgstation/assets/76465278/c716f88f-9a58-43d9-be70-2f8e8ce430ee)
... out of my hands. It's on its own path in life.

Full Changelist:
- The obvious: resprites all the suits in under/suits.dmi
- Updates Buttondown sprites to fit the 'folded' standard
- Moves "good lawyer's suit" obj icon into the under/suits.dmi instead
of civilian.dmi (the lawyer suits need to be done in another PR and
hopefully all icons moved into these ones since them being separate
sucks)
- Repaths "henchmen jumpsuit" from being under/suit to being
under/costume (why was it ever a suit)
- Removes old `under/suit/black`, which was a white shirt with black
pants. This now uses
`/obj/item/clothing/under/costume/buttondown/slacks/service`, which is a
pre-colored version of the GAGS item
- Removes `under/suit/sl` for the same reason
- Repaths `under/suit/blacktwopiece` to just use the now-unused
`under/suit/black` (saving me from a lot of changes to, say, the Dye
registry or some maps)
- Removes the "white on white" suit since it's the same as the white
suit (besides the blue undershirt being violent neon green)
- A lot of sorting of the main file
## Why It's Good For The Game
Old

![undersuit](https://github.com/tgstation/tgstation/assets/76465278/9d58f9ea-22cd-4ea7-b276-2d1f879d5036)
New

![image](https://github.com/tgstation/tgstation/assets/76465278/7c9daa8b-23ef-49c2-a2a9-630027301e1a)

New buttondown object (with suit to compare)

![image](https://github.com/tgstation/tgstation/assets/76465278/d19bc914-36a2-4861-8232-23e77bd2056f)

## Changelog
:cl:
image: resprited a lot of formal undersuits, enjoy!
add: Added a pre-colored type of buttondown slacks for some service
roles, to replace the "black suit" and "amish suit"
del: Removed the "amish suit", "black suit", and one of the two "white
suit"s
/:cl:

---------

Co-authored-by: OrionTheFox <76465278+OrionTheFox@users.noreply.github.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [MCBCMF/MCBCMassacre](https://github.com/MCBCMF/MCBCMassacre)@[cadd693a7b...](https://github.com/MCBCMF/MCBCMassacre/commit/cadd693a7bbb3c6a9ed82a966a53fa4943910860)
#### Wednesday 2023-08-02 22:19:01 by Kelvin Williams

New Acquaintance 

I talk to people on various social media and they have vanished quickly never to be seen or heard from again. 

Now I’m posting their photos immediately. 

Do not take my communication with them on any particular platform as meaning anything. I may be seeking assistance to eat, a partner for sex, a ride to church, or help cleaning my apartment. Got it?

I’m saving innocent lives.

---
## [BradleyMasters2022-23/MastersProject](https://github.com/BradleyMasters2022-23/MastersProject)@[216e7e98d7...](https://github.com/BradleyMasters2022-23/MastersProject/commit/216e7e98d72abec053c9fa3eca81477c8d3a6828)
#### Wednesday 2023-08-02 22:32:24 by BenSchu438

Fixing merge fuckery

fuck you github, penny shall perish

---
## [c0ntradicti0n/dialectics](https://github.com/c0ntradicti0n/dialectics)@[45bc699467...](https://github.com/c0ntradicti0n/dialectics/commit/45bc699467fcf796b9c0ba0bbbdd523743de906d)
#### Wednesday 2023-08-02 23:23:07 by c0ntradicti0n

Automated TOC Commit: 2/2/1/1/1/.Proposition.md 2/2/2/2/2/1/_Harsh-Soft.md 1/1/2/3/2/.Energy.md Arithmetic.md" wisdom.md" 2/2/2/1/1/3/2/.Jurisdiction.md Clusters.md" 3/1/2/2/2/2/_Objective-Subjective.md 2/2/2/1/2/1/1/.Evil.md 1/3/3/1/2/1/3/3/.Harmony.md 2/2/2/2/3/3/1/.Stability.md 2/2/2/3/1/2/1/1/1/3/.Knowledge.md 3/1/1/3/1/2/.Rhythm.md 1/2/1/1/1/3/.Historicity.md 3/1/1/2/1/1/.Scale.md 1/3/3/1/2/1/3/1/.Sound.md 2/2/2/3/3/1/3/.Biology.md 2/2/2/1/1/1/_Permission-Prohibition.md 2/2/2/1/1/_Virtue-Sin.md 2/2/1/3/2/3/.Proofs.md 2/2/2/1/3/1/.Unfair.md 2/2/1/1/2/.Argument.md 2/2/2/3/2/.Ignorance.md 1/1/3/2/2/1/3/1/.Modulus.md 2/2/2/1/3/2/2/.Impartiality.md 2/2/2/2/2/3/1/.Calming.md 3/1/3/2/_Finite-Infinite.md 1/3/3/3/_Autotrophic-Heterotrophic.md 2/2/2/2/2/1/3/.Desecration.md 2/2/2/1/1/1/3/.Consequence.md 2/2/2/3/.Logic.md 2/2/2/2/2/1/.Taste.md Theory.md" 1/1/3/3/2/.Variable.md 2/2/2/1/2/3/3/.Responsibility.md 2/2/1/2/3/1/.Speculation.md 1/1/3/2/2/1/3/.Exponentiation.md Rights.md" 3/1/2/2/3/2/3/.Sign.md 3/1/1/2/1/_Mono-Poly.md Algebra.md" logic.md" 3/1/1/3/2/_Sounding-Silent.md 2/2/2/1/1/1/.Legal.md 1/1/3/2/3/1/2/.Variables.md 1/3/3/2/1/3/.Mixture.md 2/2/2/2/1/3/3/.Trends.md theory.md" 2/2/1/2/1/1/.Hypothesis.md Reasoning.md" 1/1/3/3/1/1/1/.Singleton.md 2/2/2/3/3/3/_Theory-Practice.md 3/1/1/3/.Rhythm.md 2/2/2/2/3/1/2/.Repulsing.md 2/2/2/3/1/.Knowledge.md Knowledge.md" Particle-Field.md" 2/2/2/1/3/2/_Fairness-Prejudice.md 1/3/3/2/1/2/.Compound.md 2/2/2/2/1/3/2/.Style.md 1/1/3/2/2/1/3/3/.Logarithm.md 2/2/2/1/1/3/3/.Enforcement.md 1/3/3/1/2/1/3/1/.Noise.md 2/2/1/3/2/2/.Theorems.md 2/2/2/1/3/1/1/.Inequality.md 1/1/2/1/1/.Presence.md 2/2/2/1/2/1/_Harm-Benefit.md 3/1/3/2/1/.Discrete.md 2/2/2/2/1/1/.Consequentialism.md 3/1/1/3/2/.Rests.md 2/1/1/3/.Responsibilities.md 1/2/2/2/2/1/.Dot.md 3/1/1/1/1/.Audible.md Development.md" 3/1/1/3/3/3/2/.Upbeat.md 2/2/1/3/1/_Deduction-Induction.md 1/2/2/2/2/3/.Plane.md 2/2/2/3/3/2/3/.Epistemology.md 1/3/3/1/2/2/1/3/.Rainbow.md 3/1/1/3/_Meter-Pulse.md 3/1/3/1/1/.Line.md 2/2/2/2/3/1/1/.Repellant.md 3/1/1/2/1/3/.Tone.md 1/1/2/2/3/.Limit.md 2/2/2/1/3/2/.Fair.md 3/1/1/3/3/.Mensuration.md 3/1/2/2/3/2/1/.Meaning.md 2/2/2/2/2/3/2/.Balance.md 2/2/2/1/3/1/2/.Bias.md 1/1/3/2/2/1/1/3/.a+b=a-b.md 1/1/3/2/2/1/3/1/.Exponentiation.md 2/2/2/2/2/1/.Offense.md 2/2/2/3/3/3/2/.Skills.md 2/2/2/1/2/2/.Moral.md 1/1/3/2/3/1/2/.Quaternion.md 2/2/2/1/2/2/_Benefit-Harm.md 3/1/2/2/5/2/3/.Rhythm.md 2/2/2/3/3/2/_Belief-Knowledge.md Sciences.md" Framework.md" 2/2/2/2/2/3/_Stability-Imbalance.md 1/3/3/3/_Individual-Community.md 3/1/1/2/1/.Pitch.md 2/2/2/1/3/1/3/.Discrimination.md 2/2/2/1/3/3/_Fairness-Inequality.md 3/1/1/3/1/.Beats.md 3/1/2/2/2/2/.Symbolism.md 1/1/3/2/2/1/1/3/.a+b=a--b.md 1/1/3/2/2/1/3/2/.Residue.md 2/2/2/2/3/3/.Balance.md 3/1/1/1/3/.Semiotics.md 2/2/2/1/1/.Right.md 1/1/2/3/3/.Information.md 1/3/3/3/2/3/.Evolution.md 1/3/3/1/1/2/1/_Force-Field.md quo.md" 2/2/2/2/1/1/3/.Repugnant.md 2/2/2/1/.Ethics.md 3/1/3/3/1/.Number.md 2/2/1/2/3/3/.Confirmation.md 2/_Objective-Subjective.md 2/2/2/2/1/1/1/.Disgust.md 2/2/2/1/3/3/.Equity.md Class.md" 1/3/3/1/1/2/1/3/.Fields.md 2/2/2/1/3/1/_Prejudice-Fairness.md 3/1/2/2/2/2/.Rationalism.md 2/2/2/3/3/1/_Theory-Practice.md Inquiry.md" 2/2/2/1/3/.Justice.md 2/2/2/1/2/3/.Morality.md 2/2/2/3/3/2/1/.Ideology.md 1/3/3/1/2/1/3/_Absence-Presence.md 2/2/2/1/2/2/1/.Good.md 2/2/2/1/2/1/.Immoral.md 1/2/1/1/2/3/.Immediacy.md Inversion.md" (Dasein).md" Algebra.md" Knowledge.md" 2/2/2/2/3/3/2/.Adaptation.md 2/2/2/1/3/2/1/.Equity.md Music.md" Space.md" 1/2/2/1/2/1/.Localization.md 2/2/2/1/2/2/2/.Merit.md 2/2/2/2/1/1/.Distaste.md 2/2/2/3/3/3/3/.Proficiency.md 2/2/2/2/1/3/_Classic-Modern.md 1/1/2/2/3/.Boundary.md 2/2/2/1/2/3/1/.Right.md Ignorance.md" Reasoning.md" 2/2/2/2/1/3/.Deontology.md Meter.md" 3/1/3/2/2/.Continuous.md Texture.md" 1/3/3/3/2/1/.Replication.md 2/2/2/1/3/3/1/.Benevolence.md logic.md" 3/1/1/3/3/3/1/.Downbeat.md 2/2/2/2/2/1/2/.Provocation.md 1/3/3/1/3/1/3/_Macro-Micro.md 1/3/3/2/_Homogenous-Heterogenous.md 1/3/3/3/2/1/.Life.md 2/2/2/1/1/3/_Law-Anarchy.md 2/2/2/2/3/1/.Repulsion.md Progression.md" 3/1/3/.Mathematics.md 1/1/2/1/3/.Something.md 2/2/1/3/3/3/.Contingency.md 2/2/2/3/1/2/1/1/1/1/.Ignorance.md 1/1/3/3/1/1/3/.Majority.md 1/3/3/2/2/2/.Decomposition.md Geometry.md" 1/3/3/1/2/1/3/3/.Melody.md 3/1/3/_Order-Chaos.md 2/2/1/2/2/1/.Questioning.md 2/2/1/1/3/.Proof.md 2/2/1/2/2/.Epistemology.md Combinatorics.md" 2/2/2/1/1/2/.Illegal.md 2/2/2/3/2/1/_Unknowing-Knowing.md Worlds.md" 2/2/2/2/.Aesthetics.md 3/1/3/2/3/.Measurement.md 1/1/2/3/1/.Matter.md 3/1/1/3/2/3/.Interrupt.md 2/2/2/2/2/3/3/.Peace.md 2/2/2/1/2/3/_Obligation-Freedom.md 1/1/3/2/.Algebra.md 2/2/1/2/3/_Complexity-Simplicity.md 2/2/2/2/3/1/3/.Distancing.md 3/1/1/1/3/.Readable.md 2/2/2/1/1/1/1/.Rule.md 2/2/2/2/1/1/_Repulsive-Attractive.md 1/3/3/3/1/1/3/.Eukaryote.md Meter.md" 2/2/2/3/3/_Thought-Action.md 2/2/1/2/1/3/.Theory.md 2/2/2/1/2/3/2/.Duty.md 2/2/1/2/3/2/.Evaluation.md 3/1/3/3/3/.Proof.md Extraction.md" 3/1/1/3/2/1/.Pause.md 2/2/1/2/2/2/.Mistaking.md Enlightenment.md" 1/1/2/2/1/.Contrast.md Diagram.md" 1/2/1/1/2/2/.Expansion.md particles.md" 2/2/2/2/1/3/.Aesthetic.md 2/1/1/1/.Laws.md 2/2/2/1/2/1/3/.Punishment.md Rights.md" 1/2/2/1/1/3/.Manifold.md 1/1/1/1/.Existence.md 3/1/1/3/3/3/3/.Offbeat.md 2/2/2/3/3/1/2/.Chemistry.md Characteristics.md" 2/2/1/3/3/2/.Necessity.md 2/2/2/1/_Just-Unjust.md Selection.md" Norms.md" 1/3/3/1/3/1/2/1/.Asteroids.md 3/1/2/.Music.md Logic.md" 2/2/2/2/3/3/3/.Homeostasis.md 3/1/1/2/1/_Tone-Pitch.md 1^0.md" 3/1/3/1/.Geometry.md 3/1/3/3/_Value-Variable.md 3/1/2/3/_Improvisation-Composition.md 2/2/2/3/3/2/2/.Metaphysics.md 2/2/1/2/2/3/.Improving.md 3/1/2/2/2/2/1/.Logic.md 2/2/2/2/2/3/.Sublime.md 1/3/3/3/1/1/1/.Prokaryote.md 3/1/2/2/2/2/3/.Theory.md 2/2/2/2/3/1/_Rejection-Attraction.md Combinatorics.md" 3/1/1/3/1/_Slow-Fast.md 1/1/3/2/2/1/2/_Linearity-Nonlinearity.md Form.md" 3/1/3/2/.Calculus.md 2/2/2/1/1/2/3/.Punishment.md Cone.md" 3/1/3/1/_Shape-Alignment.md Reactions.md" 3/1/1/2/1/.Melody.md 1/3/3/2/.Chemistry.md 1/1/2/2/1/.Otherness.md wisdom.md" 1/3/3/1/3/1/3/_Micro-Macro.md 2/2/1/1/.Logic.md theory.md" Logic.md" 2/2/2/2/1/1/2/.Aversion.md 3/1/1/3/2/2/.Break.md 2/2/1/2/3/.Logic.md 2/2/2/1/2/.Wrong.md 3/1/2/3/.Composition.md 3/1/1/1/1/.Phonetics.md 2/2/1/3/2/1/.Axioms.md 2/2/2/1/3/3/3/.Equality.md Thinking.md" Consonance.md" 2/2/1/2/3/.Metaphysics.md .md" 1/1/1/1/.Being.md 3/1/1/3/1/3/.Tempo.md 2/2/2/2/1/3/1/.Art.md 3/1/1/.Language.md wisdom.md" 2/.Anthropology.md 1/1/2/3/3/.Boundary.md 3/1/2/2/2/2/2/.Hypothesis.md 3/1/1/2/1/3/.Chord.md 2/2/2/1/1/2/2/.Breaches.md 2/2/2/1/2/1/2/.Guilt.md 3/1/3/1/2/.Surface.md 3/1/1/3/1/1/.Pulse.md 3/1/1/.Linguistics.md 1/1/2/3/2/.Infinite.md 3/1/2/2/2/1/.Beat.md Conduct.md" logic.md" 1/1/2/3/1/.Finite.md 3/1/2/2/1/3/.Key.md 1/1/1/1/3/.Transition.md 3/1/3/3/2/.Equation.md 2/2/2/2/2/1/1/.Offensive.md 2/2/2/2/2/3/.Equilibrium.md 2/2/2/1/1/1/2/.Transgression.md 2/2/2/2/.Sublime.md Synthesis.md" 3/1/3/3/.Algebra.md 2/2/2/3/3/1/1/.Physics.md 3/1/3/1/3/.Volume.md 2/2/2/1/2/2/3/.Reward.md 1/3/3/2/1/1/.Element.md 3/1/2/2/3/1/3/_Monophony-Polyphony.md 1/1/3/2/2/1/3/3/_sameness-difference.md 2/2/1/1/_Truth-Falsehood.md 2/_Emergence-of-Thought.md 3/1/1/2/1/1/.Frequency.md 2/2/1/2/2/.Methodology.md 2/2/2/1/3/3/2/.Justice.md 1/2/2/1/2/3/.Ubiquity.md interval.md" 2/1/1/2/.Rights.md 1/3/3/1/2/1/3/_Noise-Harmony.md wisdom.md" 2/2/1/2/1/1/.Observation.md System.md" 2/2/2/3/2/1/1/1/2/.Curiosity.md 2/2/2/3/3/3/1/.Craft.md 2/2/2/2/3/3/_Balance-Imbalance.md Chemistry.md" forces.md" 1/3/3/2/2/3/.Stability.md 2/2/1/2/2/_Infallibility-Fallibility.md 2/2/2/1/3/2/3/.Neutrality.md 2/2/2/1/1/3/1/.Legislation.md 1/3/3/1/2/2/1/3/.Colors.md 2/2/1/2/1/3/.Interpretation.md Inquiry.md" Process.md" Ethics.md" 2/2/2/3/1/2/1/1/1/2/.Inquiry.md 1/1/2/1/3/.Alteration.md logic.md" 3/1/2/2/1/1/.Scale.md Orbitals.md"

---
## [Rhials/tgstation](https://github.com/Rhials/tgstation)@[2d0b4f053f...](https://github.com/Rhials/tgstation/commit/2d0b4f053f1db70d9f3ab6548f58b7928f159eaf)
#### Wednesday 2023-08-02 23:27:02 by san7890

Refactors Slaughter/Laughter Demons into Basic Mobs (#77206)

## About The Pull Request

On the tin, the former "imp" is now refactored into basic mob code. Very
simple since these are only meant to be controlled by players, and all
of their stuff was on Signal Handlers and Cooldown Actions anyways. Just
lessens the amount of stupidity.

Did you know that we were trying to make demons spawn in a `pop`'d cat
named "Laughter"? Embedded in the list? I've literally never seen this
cat, so I'm under heavy suspicion that the code we were using was broken
for the longest time (or may have never worked), and we now instead just
do it a much more sane way of having a cat spawn on our demise.

## Why It's Good For The Game

Cleaner code! Less simple mob jank to deal with. Trims down the list of
simple animals to refactor. No more duplicated code that we were already
doing on parent! It's so good man literally everything was seamless with
a bit of retooling and tinkering. The typepath is also no longer `imp`,
it's actually `demon`, which I'm happy with because there's no other
demons to have it be confused with anymore.

We were also doing copypasta on both the demon spawner bottle and the
demon spawning event so I also just unified that into the mob. I also
reorganized the sprites to be a bit clearer and match their new
nomenclature

## Changelog
:cl:
refactor: Slaughter and Laughter Demons have been refactored, please
place an issue report for any unexpected things/hitches.
fix: Laughter Demons should now actually drop a kitten.
/:cl:

---

