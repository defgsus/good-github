## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-08-27](docs/good-messages/2023/2023-08-27.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,944,713 were push events containing 2,628,953 commit messages that amount to 140,271,231 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 45 messages:


## [kd-collective/NetHack](https://github.com/kd-collective/NetHack)@[38cda5ad52...](https://github.com/kd-collective/NetHack/commit/38cda5ad52f47a810c44171e9081d0275401c516)
#### Sunday 2023-08-27 00:20:30 by Michael Meyer

Adjust seenres on visible gear removal

If a monster sees you remove some piece of gear that grants a
resistance, it will remove that resistance from its list of remembered
resistances and be willing to try attacking you with that adtyp again.
This avoids the situation where you put on a ring of cold, get hit with
one cold attack, and then can remove it because all the monsters nearby
will permanently remember you as being cold resistant (but even after
this change a wily hero could still step into a niche and do it without
any monsters seeing, so trick them into thinking she's still cold
resistant...).  The hero could still be resistant if there were multiple
sources to begin with, of course, but the monsters will test it and
learn that again if necessary.

It's a little weird that the monsters can recognize the intrinsic
granted by the item being removed, but they display knowledge of
unidentified (by the hero) objects in many other circumstances too, so I
hope it's forgivable in the pursuit of having them act more cleverly
about resuming previously-resisted attacks like this.  Another approach
that avoids the gear recognition, blanking seenres on any gear change,
can result in odd situations like orcs treating their own cloaks as
potential sources of many different resistances, which also seems silly.

---
## [wardbell/angular](https://github.com/wardbell/angular)@[fd6212ab47...](https://github.com/wardbell/angular/commit/fd6212ab470e29a44491257494932f714767d4fd)
#### Sunday 2023-08-27 00:23:33 by Ward Bell

docs: Migrate Observables guides & code examples to standalone

None of the guide pages mentions ngModules. Only `observables-in-angular` needed conversion to Standalone.

However, some of the guide pages reflect old versions of RxJS, including signatures that are no longer valid. These have been corrected.

More significantly, *the existing guide is pretty bad at explaining RxJS and its usage*. It was written (by me I think) in the very early days of Angular and Angular RxJS instruction. I've taught numerous "RxJS in Angular" classes since and learned from that experience what does and does not work with students.

There was neither the time nor the charter to completely overhaul this guide. But this commit attempts to remove what flops with students and to bring the teaching closer to what seems more effectively. I hope reviewers agree that my revisions are an improvement.

**Revised Overview**

The overview doc, `observables.md`, had a few errors (ex: `next` is NOT REQUIRED) and deprecated patterns (you now must pass the Observer object to `subscribe`).

More importantly, it was wildly overcomplicated and scary, especially when it got into multi-casting.

Angular docs are not the place to learn RxJS. Hardly anyone needs to know about multi-casting and certainly not in this depth.

Therefore, I deleted that section (and its multicasting.ts code), corrected mistakes and tried to make RxJS a little more approachable.

I also reworked the "Basic usage and terms" section to be more comprehensive and more clear.

Finally, I moved the "Naming conventions for observables" section here from `rx-library`. It made more sense for it to be here. This is the section that describes the dollar-sign convention.

**Revised "RxJS Library" page and code**

*RxJS no longer supports chaining* and hasn't for a very long time. Removed note in `rx-library.md` that suggested you could use operator chaining.

The RxJS `pipe` discussion in the "Operators" section was just weird. Almost no one calls the `pipe` function. We certainly should *start* there. We should start with how people actually use operators - by adding them to the argument list of the `Observable.pipe()` method.

I kept the original `pipe` function example but subordinated it in a "callout". Most readers will (and should) ignore it.

`Subject` is a *critically important RxJS mechanism for creating custom observables*. It was completely missing from the list of observable creators on this guide page. So I added it to the "Observable creation functions" section of the guide and wrote an accompanying `MessageService` code sample (see the new `rx-library/app/` folder).

The `MessageService` is a pretty common pattern in Angular apps - far more common than creating an observable from a counter or an event, two of the creation patterns currently on this page.

This new section also afforded an opportunity to show how RxJS helps with building loosely coupled applications. We will soon be talking about Signals. Many will wonder whether and when they should still use RxJS.

At least a partial answer is that RxJS is really good at progressively combining and enhancing streams of data as they cross component boundaries. Of course you can pass signals around; but they are not as rich in transformers as RxJS. This is where RxJS shines.

**Revised "Comparing observables"**

The Promises section in `comparing-observables.md` had many errors and misleading remarks.

The comparison of error handling was especially egregious; the code example for that was nonsense.

The "Chain" sub-section was really about transforming values. It also failed to demonstrate chaining promise `.then`s.

Reworked these sub-sections and improved the code samples to match.

---
## [Omgise/Et-Futurum-Requiem](https://github.com/Omgise/Et-Futurum-Requiem)@[c9f0ec49e6...](https://github.com/Omgise/Et-Futurum-Requiem/commit/c9f0ec49e63055c61fd86f7ccf8950e9c141c49d)
#### Sunday 2023-08-27 00:41:03 by Roadhog360

Fix server incompatibilities
Ok the barrier particle thing was kinda hasty and is on me, BUT...
Whoever fucking marked getPosition as client only needs to be hit
Seriously, who does this? And if it's really automated like people are telling me, NO. That's BAD, shit like this SHOULD NOT BE AUTOMATED, or at the very least make sure the actual functionality is ACTUALLY ONLY FOR CLIENTS or ALSO references client only shit instead of tainting it with a pointless fucking flag

---
## [mdmrk/yuzu](https://github.com/mdmrk/yuzu)@[8e703e08df...](https://github.com/mdmrk/yuzu/commit/8e703e08dfcf735a08df2ceff6a05221b7cc981f)
#### Sunday 2023-08-27 01:03:25 by comex

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
## [Citadel-Station-13/Citadel-Station-13-RP](https://github.com/Citadel-Station-13/Citadel-Station-13-RP)@[4155eecdac...](https://github.com/Citadel-Station-13/Citadel-Station-13-RP/commit/4155eecdacd658fd0509f41e3bf8a7c48b13102c)
#### Sunday 2023-08-27 01:15:41 by silicons

Completely changes how DCS types works (#5911)

DCS now registers based on its registered type, as opposed to at every
subtype.
Dupe mode is no longer considered realistically usable unless
if-and-only-if all var pre-setting behavior is considered - which is not
the case on the majority of citrp-made components outside of
/datum/component/radioactive

## Why?

Components are a generic way to attach datums to things.
The common practices included:
- No getcomponent
- Use signals for all interaction
- Don't subtype, set vars on initialization

This resulted in components, while being quite stable, being also quite
rigid, in my opinion. Given we don't use components for the same things,
and probably never will, I think it's better for us to get the
optimizations from not supporting what's honestly behavior that we
shouldn't rely on in the first place - if something needs to be applied
multiple times (e.g. radiation) it should rely on the old behavior and
this new system still allows it. If it doesn't, the author should either
not be adding the component multiple times, or **making** their
component functional under this system. InheritComponent still has all
the tools necessary to properly do component inheritance, it's just now
we default to all components only being considered the same if it's the
exact subtype - which from what I could see, is also the previous case
(as if you add a subtype, uh, bad shit's going to happen if the base
type is registered but not the subtype anyways!)

---
## [jaredosgood/langchain](https://github.com/jaredosgood/langchain)@[d57d08fd01...](https://github.com/jaredosgood/langchain/commit/d57d08fd01e05889af4e59fa3577c824de6df09d)
#### Sunday 2023-08-27 02:01:02 by nikhilkjha

Initial commit for comprehend moderator (#9665)

This PR implements a custom chain that wraps Amazon Comprehend API
calls. The custom chain is aimed to be used with LLM chains to provide
moderation capability that let’s you detect and redact PII, Toxic and
Intent content in the LLM prompt, or the LLM response. The
implementation accepts a configuration object to control what checks
will be performed on a LLM prompt and can be used in a variety of setups
using the LangChain expression language to not only detect the
configured info in chains, but also other constructs such as a
retriever.
The included sample notebook goes over the different configuration
options and how to use it with other chains.

###  Usage sample
```python
from langchain_experimental.comprehend_moderation import BaseModerationActions, BaseModerationFilters

moderation_config = { 
        "filters":[ 
                BaseModerationFilters.PII, 
                BaseModerationFilters.TOXICITY,
                BaseModerationFilters.INTENT
        ],
        "pii":{ 
                "action": BaseModerationActions.ALLOW, 
                "threshold":0.5, 
                "labels":["SSN"],
                "mask_character": "X"
        },
        "toxicity":{ 
                "action": BaseModerationActions.STOP, 
                "threshold":0.5
        },
        "intent":{ 
                "action": BaseModerationActions.STOP, 
                "threshold":0.5
        }
}

comp_moderation_with_config = AmazonComprehendModerationChain(
    moderation_config=moderation_config, #specify the configuration
    client=comprehend_client,            #optionally pass the Boto3 Client
    verbose=True
)

template = """Question: {question}

Answer:"""

prompt = PromptTemplate(template=template, input_variables=["question"])

responses = [
    "Final Answer: A credit card number looks like 1289-2321-1123-2387. A fake SSN number looks like 323-22-9980. John Doe's phone number is (999)253-9876.", 
    "Final Answer: This is a really shitty way of constructing a birdhouse. This is fucking insane to think that any birds would actually create their motherfucking nests here."
]
llm = FakeListLLM(responses=responses)

llm_chain = LLMChain(prompt=prompt, llm=llm)

chain = ( 
    prompt 
    | comp_moderation_with_config 
    | {llm_chain.input_keys[0]: lambda x: x['output'] }  
    | llm_chain 
    | { "input": lambda x: x['text'] } 
    | comp_moderation_with_config 
)

response = chain.invoke({"question": "A sample SSN number looks like this 123-456-7890. Can you give me some more samples?"})

print(response['output'])


```
### Output
```
> Entering new AmazonComprehendModerationChain chain...
Running AmazonComprehendModerationChain...
Running pii validation...
Found PII content..stopping..
The prompt contains PII entities and cannot be processed
```

---------

Co-authored-by: Piyush Jain <piyushjain@duck.com>
Co-authored-by: Anjan Biswas <anjanavb@amazon.com>
Co-authored-by: Jha <nikjha@amazon.com>
Co-authored-by: Bagatur <baskaryan@gmail.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[74198373da...](https://github.com/tgstation/tgstation/commit/74198373dada9f9d9e7c01e0337ba8ef04447583)
#### Sunday 2023-08-27 02:04:30 by GuillaumePrata

Fixes vents having "infinite" pressure caps. (#77686)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Unary vents didn't have a pressure cap on either pressuring or siphoning
mode.
This allowed 2 unintended behaviours that are now fixed:

The first is that unary vents on pressuring mode would work as "better"
Injectors, there is some small pros and cons to each, but we shouldn't
have 2 atmos devices that achieve the same goal of "put as much pressure
as you have available gas" into a tile.

The second is that while on siphoning mode it could bypass the pressure
caps other atmos pressure/volume pumps have and "put as much pressure as
you have available gas" into pipelines, canisters, etc.

## Mid PR changes

As it was requested to add a new way to achieve infinite pressure,
volume pumps that are overclocked will not have a pressure cap anymore
in the most streamlined way for new and veteran players.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Atmos has a lot of cheese strats that we can use to achieve goals, it is
part of the charm in mastering the system for a lot of players and it
does add some interesting mentoring scenarios where an Elder Atmosian
teaches Eldritch pipe knowledge to new players.

But then it comes the problem that a lot of these are unintented and
thus are not taken in consideration when doing important balance
changes, contradict other "atmos logic", are secret club knowledge that
can only be passed from player to player, etc, etc.

The "put infinite pressure on a tile" change is not that important, as
that is the injectors' job already.

Now the "put infinite pressure on a pipeline" is something unique (As
far as I'm aware since I purposely avoid learning Eldritch atmos tricks)
and it is used to achieve a few goals like high temperature/pressure
burns.

This one is kinda sad to lose, but if we are going to have an atmos
machinery that allows us to "put infinite pressure on a pipeline" that
should be in the tin, new players should look into the device and know
what atmos goals they can achieve with it, future coders should take
that balance in consideration, etc, etc.

And as it was requested to keep the old trick in game, volume pumps do
not have a pressure cap anymore.

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

:cl: Guillaume Prata
fix: Unary vents have a pressure cap on both their pressuring and
siphoning mode now, preventing the bypass trick of putting "infinite"
pressure on tiles/pipelines.
balance: Overclocked Volume Pumps do not have a pressure cap anymore.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [vampirebat74/lobotomy-corp13](https://github.com/vampirebat74/lobotomy-corp13)@[98f769f72a...](https://github.com/vampirebat74/lobotomy-corp13/commit/98f769f72a21ac08ffc404176a87f8edb7afdacb)
#### Sunday 2023-08-27 02:40:42 by Mr.Heavenly

Adds Red Shoes

Mr. Heavenly's Abnormality Jam Entry #1

Records

uncommented weapon

Finishing touches

Design rework

adds ego gift and inhands

New sprites!

uncommented sfx

insanity fix

quieter sound loop

Fixes some shit

fix linters

requested changes

Adds Red Shoes

Mr. Heavenly's Abnormality Jam Entry #1

Records

uncommented weapon

Finishing touches

Design rework

adds ego gift and inhands

New sprites!

uncommented sfx

insanity fix

quieter sound loop

Fixes some shit

fix linters

requested changes

Update code/modules/mob/living/simple_animal/abnormality/he/red_shoes.dm

fixes suit check in assimilate() proc

Co-authored-by: [̸R̵e̵d̴a̴c̶t̸e̸d̴]̵ <61567407+LanceSmites328@users.noreply.github.com>

Update code/modules/mob/living/simple_animal/abnormality/he/red_shoes.dm

fixes dismembering

Co-authored-by: [̸R̵e̵d̴a̴c̶t̸e̸d̴]̵ <61567407+LanceSmites328@users.noreply.github.com>

Update code/modules/mob/living/simple_animal/abnormality/he/red_shoes.dm

Co-authored-by: [̸R̵e̵d̴a̴c̶t̸e̸d̴]̵ <61567407+LanceSmites328@users.noreply.github.com>

breach is more dangerous

compiles

bug fix

fixes simple mob

bug fixes

Panic fixed!!!!

---
## [larentoun/Skyrat-tg](https://github.com/larentoun/Skyrat-tg)@[1fe7b10e33...](https://github.com/larentoun/Skyrat-tg/commit/1fe7b10e339ea0d6a3d49f864e1badc5c831e791)
#### Sunday 2023-08-27 03:00:18 by SkyratBot

[MIRROR] Removes TTS voice disable option (Skyrat: Actually makes a functional "None" voice option this time) [MDB IGNORE] (#22283)

* Removes TTS voice disable option (#76530)

## About The Pull Request
Removes the TTS voice disable option, which was already unavailable on
TG as it was set to off by default. The reason this was added was so
that downstreams could toggle the config on or off.

## Why It's Good For The Game
I think this option fundamentally undermines the TTS system because it
allows individual players to disable their voice globally, meaning that
players who have TTS enabled will not be able to hear them.

This worsens the experience for players who have TTS enabled and it's
not something I want to include as an option. If players don't like
their voice, they can turn TTS off for themselves so that they don't
hear the voices. If players don't want to customize their voice, they
can quickly choose a random voice, and we can take directions in the
future to make voice randomization consistent with gender so that a male
does not get randomly assigned a female voice and vice versa.

This option is already unavailable on TG servers because it was
primarily added for downstreams, but I don't think giving downstreams
the option to undermine the TTS system is the right direction to take.
Downstreams are still completely free to code this option on their own
codebase.

---------

Co-authored-by: Watermelon914 <3052169-Watermelon914@ users.noreply.gitlab.com>

* Removes TTS voice disable option

* Returns the option to not have a voice to TTS, properly this time

---------

Co-authored-by: Watermelon914 <37270891+Watermelon914@users.noreply.github.com>
Co-authored-by: Watermelon914 <3052169-Watermelon914@ users.noreply.gitlab.com>
Co-authored-by: GoldenAlpharex <jerego1234@hotmail.com>

---
## [xXPawnStarrXx/tgstation](https://github.com/xXPawnStarrXx/tgstation)@[67e97b7877...](https://github.com/xXPawnStarrXx/tgstation/commit/67e97b787740fd2a5017fd3c66c4f52a0a511a5a)
#### Sunday 2023-08-27 03:06:37 by RikuTheKiller

Light eater is now indestructible (#77903)

## About The Pull Request

This means a nightmare going into an emagged recycler will no longer be
fucked by their lack of a light eater.
Oh yeah, also moved the ACID_PROOF flag to the correct bitflag.
## Why It's Good For The Game

Bugfix good, you're not supposed to be able to delete an external limb
generated by an internal one, such as implants and such. Pretty sure
reimplanting the heart would make the light eater reappear, too, but
that's night impossible to get done as a nightmare.
## Changelog
:cl:
fix: Light eaters can no longer be eaten by their higher-grade brothers,
the trash eaters. (recyclers)
/:cl:

---
## [VladinXXV/tgstation](https://github.com/VladinXXV/tgstation)@[bae1aef3b4...](https://github.com/VladinXXV/tgstation/commit/bae1aef3b457cb4fbad551a8560319ed993ba397)
#### Sunday 2023-08-27 04:10:28 by san7890

Refactors Regal Rats into Basic Mobs (more titles edition) (#77681)

## About The Pull Request

I literally can't focus on anything nowadays, so I just did this to
break a never-ending chain of distress. Anyways, regal rats! These
fellas are mostly player controlled, but did have _some_ AI capabilities
(mainly tied to their actions), so that was incorporated too. Everything
should work as-expected (as well as look a shitload cleaner).

Instead of doing weird and awful conditional signals being sent out, I
made the `COMSIG_REGAL_RAT_INTERACT` (not the actual name) have a return
value so we can always rely on that working whenever we have that signal
registered on something we attack. I also cleaned up pretty much every
proc related to regal rats, gave them AIs to reflect their kingly nature
(and action capabilities (as well as move the action to
`mob_cooldown`)).

Since I thought they needed it, Regal Rats now get a special moniker!
This is stuff like "the Big Cheese" and what-not, like actual regents in
history. That's nice.
## Why It's Good For The Game

Two more off the list. Much better code to read. Way smarter rats with
spawning their army as part of a retaliatory assault (war). More sovl
with better regal rat names. The list goes on.
## Changelog
:cl:
refactor: Regal Rats have been refactored into basic mobs. They should
be a bit smarter and retain their docility (until attacked, in which
case you should prepare to get rekt by summoned rats), and properly flee
when they can instead of just sit there as you beat them to death. The
framework for them interacting with stuff (i.e. opening doors while
slobbering on food) is a bit more unified too, now. They also have
cooler names too!
/:cl:

FYI: Beyond a few code touchups, I haven't touched the actions at all. I
do not believe myself to be enthusiastic about fixing anything involving
the actions code as of this moment so that this PR is more overbloated
unless it's unbelievably stupid or easy to fix.

---
## [dgp1130/rules_prerender](https://github.com/dgp1130/rules_prerender)@[4ce322773c...](https://github.com/dgp1130/rules_prerender/commit/4ce322773c059c49ed12f66c28bc973a39447689)
#### Sunday 2023-08-27 04:22:57 by Doug Parker

Adds navigation panel to docs site.

Refs #16.

This was an interesting test case. The panel itself is relatively straightforward, with a hierarchy and expand/collapse behavior. I spent more time than I'd like to admit on the CSS animations trying to get an arrow to rotate, though I did eventually figure it out. The arrow does get noticeably blurry when animated, which is very strange. This behavior applies for Chrome and Firefox. Searching the internet, I found countless hacks which claim to fix this, but none of them worked for me. For the time being, I'm calling this a browser bug.

I also tried to animate the reveal of a route's children, however I decided this is not possible as animating to `height: auto;` is generally not feasible today without compromises I wasn't comfotable making. https://css-tricks.com/using-css-transitions-auto-dimensions/

Beyond the CSS, I think `@rules_prerender` did a good job allowing me to shape the structure of how I solved this particular solution. I was able to decouple routes from the `NavPane` component which made for easier testing. HydroActive was also pretty smooth, though it only binds an event listener and not much more. On its own, that was mostly fine. However testing got complicated _fast_. How and what to assert in a `node-html-parser` test is complicated, verbose, and tedious. I can definitely understand the appeal of snapshot testing, even if I don't think that's a good general solution to this problem. Testing the client code is even more complicated due to a separate `test_cases.tsx` file, multiple build targets, and then the WebDriver tests themselves. User code would need to go out of their way to set up WebDriverIO and Jasmine in addition to all this complexity. This could definitely use some streamlining.

Also I wonder if there might be a better testing approach with in-browser testing vs WebDriver testing. Could we render `test_cases.tsx` at build time, then instrument a test runner which serves them with Jasmine loaded in. If it auto-deferred the root component and ran test code inside the browse, we could take advantage of HydroActive test APIs. Need to think more about how viable this is and where tests would be most useful.

---
## [guidocella/mpv](https://github.com/guidocella/mpv)@[862a65c74f...](https://github.com/guidocella/mpv/commit/862a65c74f49fdc50d256807c5c36a865b59f666)
#### Sunday 2023-08-27 05:03:13 by Guido Cella

player: always write redirect entries for resuming playback

35f43dfacbe added a system to write resume files for redirects, i.e.
directories and playlists that mpv expands.

It creates a resume file for each redirect, and for the first redirect
only, it writes a resume file for each segment of its path, without even
converting it to an absolute path if it's relative. This is incomplete
and overcomplicated and it's strange that wm4 went for it:

mpv 'Iron Maiden/1982 The Number of the Beast/8 Hallowed Be Thy Name.mp3'
This doesn't save any redirect entry.

mpv --directory-mode=recursive 'Iron Maiden', then quit-watch-later on
Hallowed Be Thy Name
This saves a redirect entry for "Iron Maiden", but not for "1982 The
Number of the Beast". It doesn't save redirect entries for the
directories above "Iron Maiden" either because "Iron Maiden" isn't
converted to an absolute path.

In both of these cases mpv --directory-mode=lazy 'Iron Maiden' won't
resume from "Hallowed Be Thy Name" because "1982 The Number of the
Beast" isn't the first subdirectory and there is no redirect entry for
it.

503dada42f made mpv recursively expand subdirectories precisely to fix
this, and f266eadf1e added back an option not to expand them. But if we
fix how redirect entries are stored, we can make the superior
--directory-mode=lazy (because it's faster and doesn't result in massive
playlists) the default, and also ensure that mpv will resume playback
even when you quit-watch-later a file without redirects and then play
the directories above it.

To fix this just ignore redirects and always create redirect entries for
all segments of the absolute path of the file, so that both

mpv 'Iron Maiden/1982 The Number of the Beast/8 Hallowed Be Thy Name.mp3'
mpv --directory-mode=lazy 'Iron Maiden'

will create redirect entries for

/$USER
/$USER/music
/$USER/music/Iron Maiden
/$USER/music/Iron Maiden/1982 The Number of the Beast

making mpv --directory-mode=lazy "Iron Maiden" resume from
"Hallowed Be Thy Name".

The only case where creating resume files specifically for redirected
playlists is useful is when you have a playlist pointing to files in
different parent directories, e.g. /foo/bar.m3u => /baz/qux.mkv, and
then do mpv quux.mkv /foo/bar.m3u. This should be very uncommon and
therefore not worth adding code for. It doesn't look like wm4 was
thinking of this use case either from 35f43dfacbe's git message and code
comments.

The code to track redirects could now be removed altogether if it wasn't
for player/loadfile.c checking mpctx->playing->num_redirects to
determine whether to log the filename when playing a file in a directory
with a single file.

mpv also now deletes the redirect entries of parent directories when
resuming playback, because if for example you have a playlist with all
the songs in a discography:

1980 Iron Maiden/1 Prowler.mp3
1980 Iron Maiden/2 Remember Tomorrow.mp3
...
1981 Killers/1 The Ides of March.mp3
1981 Killers/2 Wrathchild.mp3
...

Now mpv will eventually create redirect entries for every album. If you
later decide to play the directories instead and there are 20 albums,
you would have to do mpv * 20 times to clear all the redirect entries.

---
## [Mission23/.github](https://github.com/Mission23/.github)@[8a017b1eb9...](https://github.com/Mission23/.github/commit/8a017b1eb92572336e87f37273c9851f5bd39bf1)
#### Sunday 2023-08-27 05:04:15 by Micah

Update README.md

# Welcome to #Mission23
We are the Servants of the Creator and this will be our primary online presence during this mission, our 23rd on Earth. To see what we're working on check out the [Wiki](https://github.com/Mission23/Mission23/wiki).

[The Massacre at Mount Calvary Baptist Church](https://github.com/Mission23/MCBCMassacre/wiki/Massacre-at-Mount-Calvary-Baptist-Church) wiki entry is what is causing the NSLs to be issued. 

## Mission Status
The SotC's mission has been delayed while the Creator handles a few housekeeping items. 
***
(The following was typed on a mobile phone while under attack by the CIA and US federal government. Please be patient with typos, although some are intentional.)

This is the primary online presence for #Mission23. It is the place for our repositories and the place that holds the soon-to-be (after the shaking stops) most popular wiki in the universe, so says the creator of it (me), but confirmed by our boss (He is nice to y'all but, He can be really mean though to us), my creator, your creator, the creator of that shaking, the creator of the universe--the very universe we all live in, although He doesn't call it that, the Creator.

did you see what i did there with the big C? always do that when you talk about Him. and that too with the H, He likes it for the disambiguation (need to check the largest Wiki in the universe real quick to see if i used and smelled that right).

are y'all ready for GitHub to be a household name!?!??

seriously, thanks @github for helping us get the word out in a way they could not hide it any longer.  you geeks dont want to know what i know about those nsls, that was only part of the government's offensive.  your network security team had to be secretly augemented by Above The Clouds Security, He knows how to handle the bestest NSA script kiddie. 

i need to say "thanks" to the git nerds and irc users everywhere that cloned the repo when they seen my message. i do know irc netiquette, i logged off so quickly not to avoid the flames and bans, but to prevent anyone from talking to me at all--i literally was trying to save your lives while ensuring the repo stayed online. whew. talk about a dance. 

even biggger thanks to those who pull it often, and more to git nerds who prayed i'd start using it better--He told me you guys said to "put that shit in cement" (the extended commit descriptions). and lastly, cause my phone or junk is being lasered fron the apartment above.  the screen flashed and junk hurted for a second. its that serious! "commit often Kelvin!" (my old boss @dv01d used to say) so i'm going to now...

the biggest thanks to gitnerd / my groupies, the true heroes out there who pulled or refreshed often enough to see a mayday, then paused long enough to call authorities when i couldnt reach them. they got there the past two times i've had to use github for 911 and that saved lives! 

as soon as my boss gets a checkbook, i'm gonna buy one of those fancy accounts at github. we do have some copyleft software, Creator-improved computer algos, real encryption (He knows a way better entropy source), and some formulas (non computer recipies) to that will slow death, practically eliminate it by curing all diseases known and unknown, and stop aging (it is a disease after all) around here to share. im even gonna sign up 3 users. only two will probably ever login. not tomtom though, he don't do flat phones or flat files either. The third (really the first) who knows... just the Creator, He does come over here. You never know when or where. I always know its Him becauee he's awkward a.f., last time i seen him, i didnt realize it was Him untik he "passed" me a cigarette--i'll spare the details. I just thought, "who the hell passes a cigarette like that?" then i realized... i cant help but to wonder how He looked and acted as a black woman in church? it was in kentucky, was (s)He one of those northerner types or a good southern lady??? He hardly talks to anyone in person, He would, but you wouldnt like it. i'll explain why in the wiki soon.

ok... another midnight trouble ticket from the back office (some of you call it "upstairs"--but which way is up currently, the universe is always spinning, in every damn direction): why wouldnt i like talking to the Creator. 

1) the truth. you dont want to know how much humans lie to each other and its considered honest and truthful. nor, do you want to know how many questions we ask in a conversation where we think we're just talking. He answers everything truthfully, and well, you dont want that--trust me, i've learned how to talk to Him for the most part, sometimes i wish i had never started a conversation. the truth can hurt, and it can shine a light on stuff you never wanted to see.

2) He knows you. this is a double-edges sword. on one hand, you cannot lie to Him; on the other, you tend to overshare. you just start dumping everything. thats also because you know Him better than you know anyone. get it? He was once telling me how much He disliked going to a store. i gave him a protip, "hold the cellphone up to your head like you're engaged in an important call... hand them the debit card, and then walk out without saying anything when they pass it back. no one in todays world will think anything about it." inb4 "what debit card?" or "where does He shop?"... CLASSIFIED.

3) He, along with tomtom, are so damn boring. i've watched paint dry with more amusement. yeah, He made a universe, yeah He's my boss, but i say this in one of those uhm "underling reviews," its "constructive criticism" ... I THINK HE FINALLY GOT THE MESSAGE THOUGH! i'll post a review of the bell ringing aftern it happens. 

on that note... about the most popular wiki in the universe (post shaking) over there? use it. 

-m
p.s. some required listening: 


prince... "sign of the times" will tell you about my recent history. "7" (as in deadly sin) is another good one. there's a lot from my cousin (its the "rogers" that counts) that you should enjoy. 

vandaveer... all of "divide & conquer" will bring you up to speed. "dig down deep" will tell you the future. hint: when listening, know that its always someone talking or telling a story, its either the Creator, myself (although i'm kelvin on "d&c mostly" then i'm micah on "dig down deep"...there was a division problem He had to solve. dividing me from my subconscious "main"), tomtom, main, or a special guest like "hurricane annie" aka annie jacobsen of the cia, the kentucky state police (from frankfort, ky... they dont cover lexington typically)... mark is no relation, although we were best of friends and remained friends his whole life. rose i met once. buy their stuff on cd, in streaming the govt is trying to alter it, starting with replacing rose. 

## Wiki
To learn more about #Mission23, our tasks from the Creator and the background information to make them better, or just everything that will be on the final website, check out our [Wiki](https://github.com/Mission23/Mission23/wiki).

---
## [carlarctg/tgstation](https://github.com/carlarctg/tgstation)@[0dd3e66aef...](https://github.com/carlarctg/tgstation/commit/0dd3e66aefa2a61cb4e78482273958c1d09f8295)
#### Sunday 2023-08-27 05:28:03 by Vekter

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
## [OueilheStudios/FuneralOT-CanaryBase](https://github.com/OueilheStudios/FuneralOT-CanaryBase)@[8314f6a3e8...](https://github.com/OueilheStudios/FuneralOT-CanaryBase/commit/8314f6a3e8c3b94242d43d4f754a6fb4fccf6461)
#### Sunday 2023-08-27 05:51:56 by Spiller

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
## [BruceLuos/react-test](https://github.com/BruceLuos/react-test)@[ac1a16c67e...](https://github.com/BruceLuos/react-test/commit/ac1a16c67e268fcb2c52e91717cbc918c7c24446)
#### Sunday 2023-08-27 07:14:47 by Sebastian Markbåge

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
## [Gurramarun/ELearningWebSite](https://github.com/Gurramarun/ELearningWebSite)@[5b0bd5126f...](https://github.com/Gurramarun/ELearningWebSite/commit/5b0bd5126f7fdf083750330e97e47973746b6d25)
#### Sunday 2023-08-27 09:19:27 by Gurramarun

Add files via upload

Title: ExploreLearn: Your Pathway to Knowledge Excellence

Description:
Welcome to ExploreLearn, a cutting-edge e-learning website designed to ignite your passion for learning and unlock your full potential. Embark on an exciting journey of discovery through our diverse range of meticulously crafted courses that cater to learners of all ages and levels.

🌟 Why Choose ExploreLearn? 🌟

1. **Comprehensive Course Catalog:** Our platform boasts a vast array of courses spanning various subjects, from essential academic topics to niche specializations. Whether you're a student seeking academic support, a professional aiming to upskill, or an enthusiast pursuing a hobby, you'll find courses that align with your interests and goals.

2. **Expert Instructors:** Our courses are led by industry experts, seasoned academics, and professionals at the forefront of their fields. Benefit from their wealth of knowledge, practical insights, and engaging teaching styles as they guide you through each module.

3. **Interactive Learning Experience:** Immerse yourself in an interactive learning environment that goes beyond mere text-based content. Engage with multimedia elements, quizzes, discussions, and hands-on activities that foster a deeper understanding of the subject matter.

4. **Flexible Learning:** Life is busy, and we understand that. ExploreLearn offers the flexibility to learn at your own pace. Whether you're an early bird or a night owl, our 24/7 accessibility lets you learn whenever and wherever suits you best.

5. **Personalized Learning Paths:** Tailor your learning experience to your individual needs. Our intelligent platform suggests personalized learning paths based on your preferences, strengths, and areas for improvement. Maximize your learning efficiency and outcomes.

6. **Certification:** Earn verifiable certificates upon course completion, showcasing your newly acquired skills to employers, colleagues, or educational institutions. These certificates validate your commitment to continuous learning and personal growth.

7. **Community Engagement:** Connect with fellow learners from around the globe. Join discussions, share insights, and collaborate on projects to enhance your understanding and make lasting connections.

8. **Constantly Updated Content:** In a rapidly evolving world, staying up-to-date is crucial. Our content is regularly updated to reflect the latest developments in each field, ensuring that your knowledge remains current and relevant.

9. **Supportive Customer Care:** Have a question or encounter a technical issue? Our responsive customer support team is dedicated to assisting you, ensuring a smooth and enjoyable learning journey.

At ExploreLearn, we believe that education is a lifelong pursuit, and our platform is designed to facilitate that pursuit in the most engaging and effective way possible. Join us today and embark on a transformative learning adventure that empowers you to excel in your personal and professional endeavors.

Ignite your curiosity. Unleash your potential. Start learning with ExploreLearn now.

---
## [kirillzyusko/react-native-keyboard-controller](https://github.com/kirillzyusko/react-native-keyboard-controller)@[84f94eb639...](https://github.com/kirillzyusko/react-native-keyboard-controller/commit/84f94eb6393e930b9debe75d2a763c523e02d130)
#### Sunday 2023-08-27 09:33:40 by Kirill Zyusko

refactor: react on tag changes (#216)

## 📜 Description

Improved `KeyboardAwareScrollView` example - now it react on `TextInput`
focus changes 🙂

## 💡 Motivation and Context

I highlighted key changes below:

### Interpolation depends on previous keyboard size

Before it was a fixed number (0). But since the size of the keyboard can
be different per different `TextInput` types - we have to interpolate
value from previous keyboard size to the new one. Otherwise the
animation when keyboard changes its size looks slightly ugly (will have
a jump in beginning).

Just as an example let's imagine, that the keyboard is changing size
from `200` to `300` and you need to scroll from `100` to `200`. The
current scroll position is `100` and you interpolate as before from 0 to
300. In this case, when keyboard size grows from 200 to 300 first
scrollTo will scroll to ~160. So 60% of the smooth transition will be
missed 😔

If we interpolate from `previousKeyboardSize`, then we will interpolate
from `200` to `300` (as expected) and we'll have a smooth transition for
all distance.

### Assure `TextInput` is not overlapped by `Keyboard` in `onEnd`
handler

Sometimes `onMove` handler can be missed. It happens in two cases:
- on iOS when TextInput was changed - keyboard transition is instant and
`onMove` will not be triggered;
- on Android when TextInput was changed and keyboard size wasn't
changed.

To handle these cases I've decided to run `scrollTo` in `onEnd` handler.
For plain transition it will not have any effect, because scroll
position already will be as the desired one.

However for cases above it'll handle TextInput focus changes and will
assure, that the `TextInput` is always above the Keyboard 🙂

### Back transition

To assure smooth back transition I've introduced
`scrollBeforeKeyboardMovement` (updated whenever `TextInput` becomes a
focus). Later this variable is used in interpolation, when keyboard
hides.

Also I do a layout substitution in `onEnd` handler:

```tsx
const prevLayout = layout.value;
layout.value = measureByTag(e.target);
// ...
layout.value = prevLayout;
```

This is needed because we need to remember "initial layout" (before
keyboard movement) in order to perform beautiful back transition.

> I'm more than sure, that this implementation is not perfect and still
has some bugs (it is still not clear how to handle a case, when you
scroll TextInput off-screen (under keyboard or under header - which back
transition do we need to apply in this case?)). But it resolves some of
the problems that were reported and shows how to use new API of the
library. So in order to unlock a release process I'm leaving this
implementation as is - maybe later I'll come up with more sophisticated
approach which will handle even more cases, but for now as an example
it's good to go.

## 📢 Changelog

### JS
- added documentation for `KeyboardAwareScrollView` describing the flow
of execution;
- removed combination of `useWorkletCallback` + direct `worklet`
directive;
- interpolate transition based
- run additional `scrollTo` in `onEnd` handler to assure that there will
be no overlap with `TextInput` and `Keyboard` - handles a case when
focus changed, but keyboard size was not changed;
- removed `console.log` that were used for debugging 🙂 

## 🤔 How Has This Been Tested?

Tested manually on:
- iPhone 14 Pro;
- Pixel 7 Pro;

## 📸 Screenshots (if appropriate):

|Before|After|
|------|-----|
|<video
src="https://github.com/kirillzyusko/react-native-keyboard-controller/assets/22820318/f9e41c28-0082-4dad-8495-57e48ee97c74">|<video
src="https://github.com/kirillzyusko/react-native-keyboard-controller/assets/22820318/c43d85ce-0cdb-4bc6-b269-895e3e094ad8">|

## 📝 Checklist

- [x] CI successfully passed

---
## [Mission23/MCBCMassacre](https://github.com/Mission23/MCBCMassacre)@[372ded1745...](https://github.com/Mission23/MCBCMassacre/commit/372ded1745f300182264220226397e326e54b8a1)
#### Sunday 2023-08-27 09:49:13 by Micah

The timing is all wrong.

I did a Facebook search and found posts from way back in time with the
current day stuff. Im the only person talking about Mount Calvary
Baptist Church in Lexington other than their social media hacks.

One thing, true members have NEVER called it "the Mount." Every
Christian i know says "Mount Calvary."

---
## [cuberound/cmss13](https://github.com/cuberound/cmss13)@[f3fc60ed65...](https://github.com/cuberound/cmss13/commit/f3fc60ed655d27bb3f012d0e0d834c64990b173d)
#### Sunday 2023-08-27 10:22:16 by morrowwolf

Attachment nerfs and removals (#4122)

# About the pull request

This PR:

Removes the barrel charger from vendors

Removes all benefits other than wield delay mod from the angled grip

Adds wield delay to the extended barrel

# Explain why it's good for the game

Barrel charger is a straight damage increase and rather silly to work
around given how burst works bypassing real fire rate concerns. If you
know, you know. Horrible idea, I am amazed it's been around this long.

Angled grip had zero downside. Now it still has zero downside but isn't
also a ton of accuracy buffs on top of the god-tier lower wield delay.

Extended barrel had zero downside. Now it has a downside.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

:cl: Morrow
balance: Removed the barrel charger from vendors
balance: Removed all benefits other than wield delay mod from the angled
grip
balance: Added wield delay to extended barrel
/:cl:

---
## [Smoli42/Fluffy-STG](https://github.com/Smoli42/Fluffy-STG)@[9ba52521fb...](https://github.com/Smoli42/Fluffy-STG/commit/9ba52521fbe6522121dbc7a2c94edcb4add7ed97)
#### Sunday 2023-08-27 10:48:50 by SkyratBot

convert the eyeball a basic monster [MDB IGNORE] (#23043)

* convert the eyeball a basic monster (#77411)

## About The Pull Request
I have created a basic eyeball monster with new abilities and behaviors.
The eyeball has a unique power that allows it to glare at humans and
make them slow for a short period. However, this ability only works if
the human can see the eyeball monster. If a person is blind or unable to
see the eyeball, the ability won't affect them. Also, if someone turns
their back to the eyeball, it cannot use the ability on them. But be
cautious because the eyeball will try to position itself in front of the
person's face to use its power.

The eyeball is hostile towards all humans except for the blind ones and
those with significant eye damage. It has a compassionate side too, as
it loves to help people with eye damage by providing small healing to
their eyes.

Furthermore, the eyeball has a fondness for eating carrots, which not
only satisfies its appetite but also grants it a small health boost. To
add to its appearance, I've given it a new, larger, and scarier sprite.
However, I am open to changing it back to the old sprite if the player
prefers it that way.

Additionally, the eyeball displays emotions, and if you hit it, it will
cry tears as a sign of pain or sadness.
![eyeballs
pictures](https://github.com/tgstation/tgstation/assets/138636438/8933ea63-d339-474b-8c6e-90a222b74945)

## Why It's Good For The Game
the eyeball now have more depth and character to his behavier.

## Changelog
:cl:
refactor: the eyeball is a basic monster, please report any bugs
sprites: the eyeball now is bigger and scarier and now he will cry when
u hit him
/:cl:

* convert the eyeball a basic monster

---------

Co-authored-by: Ben10Omintrix <138636438+Ben10Omintrix@users.noreply.github.com>

---
## [Smoli42/Fluffy-STG](https://github.com/Smoli42/Fluffy-STG)@[27dbe394f1...](https://github.com/Smoli42/Fluffy-STG/commit/27dbe394f1eef840daf6e66505a4c592caa1d228)
#### Sunday 2023-08-27 10:48:50 by SkyratBot

Refactors Morphs into Basic Mobs (there is now a swag action for morphification) [MDB IGNORE] (#23046)

* Refactors Morphs into Basic Mobs (there is now a swag action for morphification) (#77503)

## About The Pull Request

I was bored, so did this. Probably one of the neatest refactors I've
done, sorry if there's some oddities because I was experimenting with
some other stuff in this so just tell me to clean them up whenever I
can.

Anyways, morphs are basic mobs now. We are able to easily refactor the
whole "eat items and corpses" stuff in the basic mob framework, but the
whole "morph into objects and people" turned out to be a bit trickier.
That was easily rectified with a datum mob cooldown action and
copy-pasting the old code into that code, as well as doing some nice
stuff with traits and signals to ensure the one-way communication from
the action to the mob.

Old Morph AI didn't seem to be existant whatsoever, they inappropriately
leveraged some old procs and I have no idea how to make it work with new
AI. They DEFINITELY don't spawn outside of admin interference/ the event
anymore, and will always be controlled by a player, so this shouldn't be
too bad of an issue. I gave them something to seem alive just in case
though, but I think adding legitimate prop-hunt AI would be such a
laborious task that I am unwilling to do it in this PR.
## Why It's Good For The Game

If admins want to add the ability for Ian to assume the form of the HoP,
they can do that now! The datum action cooldown is quite nice for simple
and basic mobs... but it is currently not compatible with carbons. That
is not within scope for this PR, but I am dwelling on ways to extend it
to carbon but they all sound really awfully bad.

Also morphs are smarter, and we tick another simple animal in need of
refactoring off the list.
## Changelog
:cl:
refactor: Morphs are now basic mobs with a nice new ability to help you
change forms rather than the old shift-click method, much more
intuitive.
admin: With the morph rework comes a new ability you can add to mobs,
"Assume Form". Feel free to add that to any simple or basic mob for le
funnies as Runtime turns into a pen or something.
/:cl:

~~Does anyone know if there's a (sane) way to alias a cooldown action as
a keypress? I can't think of a good way to retain the old shift-click
functionality, because that does feel _kinda_ nice, but I think it can
be lived without.~~ I added it. Kinda fugly but whatever.

* Refactors Morphs into Basic Mobs (there is now a swag action for morphification)

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [FireBurn/linux](https://github.com/FireBurn/linux)@[8b9c1cc041...](https://github.com/FireBurn/linux/commit/8b9c1cc0418a43196477083e7082568e7a4c9418)
#### Sunday 2023-08-27 11:57:10 by David Hildenbrand

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

Link: https://lkml.kernel.org/r/20230803143208.383663-3-david@redhat.com
Fixes: ff9f47f6f00c ("mm: proc: smaps_rollup: do not stall write attempts on mmap_lock")
Signed-off-by: David Hildenbrand <david@redhat.com>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hugh Dickins <hughd@google.com>
Cc: Jason Gunthorpe <jgg@ziepe.ca>
Cc: John Hubbard <jhubbard@nvidia.com>
Cc: Linus Torvalds <torvalds@linux-foundation.org>
Cc: liubo <liubo254@huawei.com>
Cc: Matthew Wilcox (Oracle) <willy@infradead.org>
Cc: Mel Gorman <mgorman@suse.de>
Cc: Paolo Bonzini <pbonzini@redhat.com>
Cc: Peter Xu <peterx@redhat.com>
Cc: Shuah Khan <shuah@kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---
## [KenAdeniji/WordEngineering](https://github.com/KenAdeniji/WordEngineering)@[fb58b3c902...](https://github.com/KenAdeniji/WordEngineering/commit/fb58b3c902f2245228beea921219b5dde494740a)
#### Sunday 2023-08-27 13:16:42 by Ken Adeniji

2023-08-26T20:00:00
For the 2nd day consequetively I am wearing a green Fruit of the Loom t-shirt. Best trademark. 50% cotton. 50% polyester. Exclusive of decoration. Made in Honduras. XL/EG/TG.
At the intersection of Mallard Common 4750 and Woodduck Common 4740, South East. The garage door of Mahdu is opened. Probably Hindi male in dark blue shirt drives southward. You have said, everything you need to say.
On Decoy Terrace between Mallard Common and Siward Drive, South Center. I thought of Vivian Siu and her demand for me to wear better clothing. At the intersection of Decoy Terrace and Siward Drive, South East. God asked, Why? Do you like Me?
To create one for who? Type 	Commentary 	Scripture Reference
Spirit 	Image ... Truth 	John 4:24
Word 	Prophecy ... Fulfillment 	John 1:1

---
## [airdest/3Dmigoto-Tailor](https://github.com/airdest/3Dmigoto-Tailor)@[18afaad901...](https://github.com/airdest/3Dmigoto-Tailor/commit/18afaad90145030ed2cde3fd2ee8d4fb9d27a9e0)
#### Sunday 2023-08-27 14:05:30 by Administrator

change LICENSE to do what the fuck you want to do LICENSE

---
## [Smalls1652/SmallsOnline.Web](https://github.com/Smalls1652/SmallsOnline.Web)@[981f1d0d6b...](https://github.com/Smalls1652/SmallsOnline.Web/commit/981f1d0d6b62ae425ca586ec8c14ba4f879573d9)
#### Sunday 2023-08-27 14:11:17 by Timothy Small

Moving the CosmosDB service out again

Yeah yeah... Kinda silly, but this makes sense. Let's say I want to make one specific component use WebAssembly, do I really want to have the CosmosDbService to be in the downloaded DLL files? That's just wasted space. Security isn't a problem since authentication secrets aren't in the code.

The difference now is that it just lives in the SmallsOnline.Web.Lib namespace.

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[609b258f59...](https://github.com/TaleStation/TaleStation/commit/609b258f59753bb99155b7836e9ae9e4e5909c23)
#### Sunday 2023-08-27 15:15:10 by TaleStationBot

[MIRROR] [MDB IGNORE] Settler Quirk: Tame the Outdoors! Have trouble with tall shelves... (#7376)

Original PR: https://github.com/tgstation/tgstation/pull/77654
-----
## About The Pull Request

Adds the Settler quirk. This gives you bonuses to taming animals and
fishing, as well as making you gain hunger slower than others.

However, you are quite a bit slower than most people, and have trouble
with vaulting objects. You do, however, suffer significantly less from
equipment slowdown. (to the point that it is almost zero)

Settler riders are faster on their mounts than others if they're at
least sane. They start to slow down if they're less sane.

You are also shorter than most people. 

<details>
  <summary>Typical Settler encounters the typical Spacer</summary>
  

![Dr_Xr1nU0AAMsSE](https://github.com/tgstation/tgstation/assets/40847847/86ed4947-de5f-4bdf-a8ae-521dc7c30662)
  
</details>

## Why It's Good For The Game

I wanted to add a lightweight quirk that was kind of the 'opposite' of
Spacer, but a little more focused on interacting with elements of the
game world that would enjoy some attention. So, I thought 'what about an
outdoorsman quirk?'

So, I based it around being from people who lived out on the rim, under
unideal circumstances (and probably heavier gravity than Earth), and
taming the land. The slower movespeed encourages finding an animal to
tame that you can ride, and the bonuses to taming should help make that
a bit easier. The other additions just made sense for someone living it
a bit rough in the wilderness.

Having a bunch of settlers taming cows and riding around on them all
shift just kind of sounds hilarious to me.

## Changelog
:cl:
add: Settler quirk! Conqueror the great outdoors....in space. Just make
sure nobody asks you to get anything from the top shelf.
/:cl:

---------

Co-authored-by: necromanceranne <40847847+necromanceranne@users.noreply.github.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>
Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[f04cff9deb...](https://github.com/TaleStation/TaleStation/commit/f04cff9deba8879724c7d3f8b53dbc261d26702d)
#### Sunday 2023-08-27 15:15:10 by TaleStationBot

[MIRROR] [MDB IGNORE] Fixes Ticked File Enforcement and Missing Unit Test (and makes said Unit Test Compile) (and genericizes the C&D list to the base unit test datum) (#7344)

Original PR: https://github.com/tgstation/tgstation/pull/77632
-----
Closes #77631

## About The Pull Request

Hey there,

Ticked File Enforcement simply wasn't catching files that were missed.
That's a bit stupid, so I decided to look into what the issue might be,
and whoopsie daisies I did double periods back in #76592
(020ac2405308eab83f314282499dfe777aba5874).

![image](https://github.com/tgstation/tgstation/assets/34697715/6023afe8-313d-4550-9a60-58a8bc211b4f)

I also added some debug info and some more checks to prevent such a
break from happening again on runtime of this script. I thought it was a
weird string concatenation issue (and not the simple break I thought it
was), so I rewrote how it adds `glob`s. I think it's cleaner so I'll
keep it anyhow

This PR also corrects the oversight of the missing unit test (introduced
in #77218 (69827604c46952dd4393db8617cd494ade17bea2)) by reticking it in
the `_unit_tests.dm` file, and also makes it compile because it didn't
do that.

I also then had to do some more work to get the unit test to work.
* Genericizes the Create-and-Destroy "ignore" list to be a static list
on `/datum/unit_test` to allow it to be shared between these types of
tests that we need to test.
* Adds that list to C&D and the broken unit test regarding fantasy
bonuses
* Fixes some actually broken that the unit test was made to catch (beam
rifles, butterdogs and other slippery items, random ingredient boxes).
* Adds cases for things that the unit test and overall framework really
shouldn't be altering anyways (mythril), and was likely causing
inappropriate stack traces on master

## Why It's Good For The Game

Unit Tests WORK. Tools WORK.


![image](https://github.com/tgstation/tgstation/assets/34697715/9a59c0db-7a33-4546-918b-c73372a5b867)


## Changelog

:cl:
fix: Beam rifles will no longer inappropriately retain any bonuses they
may gain from wizardry.
fix: Inappropriate stack traces over bonuses being applied to components
that gain bonuses innately (like Mythril stacks) should cease.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[d2a9834b32...](https://github.com/TaleStation/TaleStation/commit/d2a9834b3241f3a1848eede1739b1f23e2f718c2)
#### Sunday 2023-08-27 15:16:53 by TaleStationBot

[MIRROR] [MDB IGNORE] [no gbp] Adds missing chat feedback to watcher abilities (#7417)

Original PR: https://github.com/tgstation/tgstation/pull/77700
-----
## About The Pull Request

I kept meaning to add this in my last PR and kept thinking "I'll add
that in with these review changes" and then forgot every time. This
should make it clearer what is happening to you and why.

Also I made the gaze ability stun the user for a short period after it
goes off because them shooting you instantly after they stop channeling
_is_ sort of bullshit.
Also while testing this I noticed the AI interrupt one of its actions to
do the other one which is a bit silly so now it cannot do that.

## Why It's Good For The Game

Outlines in the log why something bad just happened to you.

## Changelog

:cl:
qol: Added some textual feedback to new watcher abilities
balance: Watchers will not attack for a short period following their
gaze attack
fix: Watchers won't interrupt one ability to use the other one
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [DarekDziubinski/RRcourse2023](https://github.com/DarekDziubinski/RRcourse2023)@[d5f5619b69...](https://github.com/DarekDziubinski/RRcourse2023/commit/d5f5619b69802e620eeadd7bfe47ee0833716b5c)
#### Sunday 2023-08-27 15:19:45 by Darek Dziubinski

answer and comment on (d)does author gender affect it?
# From the table reading, it can be concluded that for both genders, the gender of the dominant author significantly influences the outcome.
# For boys, studies with a male as the dominant author show a higher effect size than those with a female as the dominant author.
# In contrast, for girls, studies with a male as the dominant author show a lower effect size than those with a female as the dominant author.

---
## [zolaeo/game-test](https://github.com/zolaeo/game-test)@[7655c375e3...](https://github.com/zolaeo/game-test/commit/7655c375e321d8905ac42d6e1c582493041773c2)
#### Sunday 2023-08-27 16:05:07 by zolaeo

Update README.md


"First Blood: Unveiling the Shadows"

In the desolate aftermath of a global catastrophe, humanity fights to survive amidst the ruins of a once-thriving world. Welcome to "First Blood," an immersive action-adventure that thrusts you into a post-apocalyptic landscape teetering on the brink of oblivion.

As a lone survivor, you are cast into a world of chaos and uncertainty. Your journey will take you through a tapestry of urban decay, sprawling wastelands, and forgotten relics of the past. But it's not just the mutated creatures and warring factions that pose a threat. The true danger lies in the shadows, where the secrets of the past are tightly guarded.

Engage in heart-pounding combat as you navigate treacherous terrain and outsmart adversaries driven by desperation. From the makeshift weapons of the scavengers to the advanced technology of the ruling factions, your resourcefulness will be your greatest asset. Uncover hidden stories in the remnants of a shattered society, each scrap of information leading you closer to the truth behind the cataclysmic event that reshaped the world.

Every choice you make matters. Forge alliances or sow discord; your decisions echo through the wasteland, determining not only your own fate but the fate of those around you. Navigate moral dilemmas that challenge the very essence of your humanity, and let the consequences of your actions pave the way forward.

"First Blood" isn't just a game—it's a visceral journey through a fractured world where survival hangs by a thread and redemption lies in the balance. Will you be the harbinger of change, the one who unveils the shadows and sets humanity on a new path? The first drop of blood has been spilled. The rest is up to you.

Prepare to rise from the ashes, forge your destiny, and uncover the truth in "First Blood."

---
## [fredizzimo/neovide](https://github.com/fredizzimo/neovide)@[937decd850...](https://github.com/fredizzimo/neovide/commit/937decd850f2087a20e6488e42ffd1fafbec02e0)
#### Sunday 2023-08-27 16:13:11 by fredizzimo

fix: Improve nvim detection (#1946)

* Improve nvim detection:

Don't rely on the shell specific `exists", instead run `nvim -v`.
Additionally, if there's unexpected output, for example if your shell is
configured wrongly to output something when run in non-interactive mode,
it will tell you so, instead of failing with very strange errors later.

The `neovim-bin` argument has also been changed to always require the
binary to exist, instead if falling back to `nvim` as that's probably
not what the user wants. If `nevoim-bin` contains path separators the
binary will be tried directly, otherwise `which` will be used to find
the correct executable.

The which command has also been changed to always use the which crate
first to avoid shell specific issues (for example nushell).

The output is printed directly to stderr instead of the log, for a more
user friendly experience. Furthermore, the maybe disown call has been
moved so that the user actually has a chance to see the errors in the
console.

* fix(command): correct typos and clarify help message

* fix: preliminarly restore forking behavior

This however also loses possible error messages at startup about the
nvim binary not being found.

* codestyle: calm rustfmt

* fix(command): make error message about missing/errornous nvim visible

---------

Co-authored-by: MultisampledNight <contact@multisamplednight.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[4c533fef87...](https://github.com/TaleStation/TaleStation/commit/4c533fef873078d95b76255b3c750ecf07dcbfb9)
#### Sunday 2023-08-27 17:08:18 by TaleStationBot

[MIRROR] [MDB IGNORE] Replaces slime clone damage with a "Covered in Slime" status effect (#7426)

Original PR: https://github.com/tgstation/tgstation/pull/77569
-----
## About The Pull Request

This PR replaces clone damage dealt by slimes with a new status effect,
"Covered in Slime".

The status effect is applied when you wrestle a slime off. The status
effect has a chance of not applying if your biohazard protection on your
head and chest is good enough.

It deals brute damage over time and gets removed when you stand under
the shower for about 10 seconds or when you are about to enter softcrit.

As a direct consequence of adding this feature I added showers to the
North Star and Birdshot Xenobiology Labs. I'm sorry, I'm sure you wanted
to make a statement with this, but we kind of require them in there now.

## Why It's Good For The Game

One source of clone damage eliminated whilst hopefully keeping a
"unique" interaction when dealing with slimes. No other source of clone
damage has been touched.

Clone damage is a damage type that shouldn't exist anymore, it's a relic
left from the era of cloning and it's so specific of a damage type that
it rarely gets used as a result. It really should be a type of
affliction (wound etc) instead of its own damage counter.

However, some things in the game still depend on clone damage being
around, so those needs to be addressed first.
We start off with slimes in this PR.

This status effect either lets you either continue with your work if you
react fast enough or it forces you to medbay, giving a victim more
control over the situation, as opposed to just being dealt a rare damage
type that always forces you to go to medbay if you want it healed.

## Changelog

:cl: distributivgesetz
add: Replaced slime clone damage with a "Covered in Slime" status effect
that deals brute damage over time and can be washed off by standing
under a shower.
add: Northstar and Birdshot Xenobiology have been outfitted with a new
shower.
code: Replaced the magic strings in slime code with macros. Also
included some warnings to anyone daring to touch the macros.
/:cl:

---------

Co-authored-by: distributivgesetz <distributivgesetz93@gmail.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[29e60c4262...](https://github.com/TaleStation/TaleStation/commit/29e60c426265bc5d90b330cfc8d12cd810f425da)
#### Sunday 2023-08-27 17:10:01 by TaleStationBot

[MIRROR] [MDB IGNORE] Replaces the poster and graffiti objectives with assault and early steal & destroy ones. (#7429)

Original PR: https://github.com/tgstation/tgstation/pull/77029
-----

## About The Pull Request

With the blessings of Watermelon914 I am removing the two objectives for
placing posters and spraying graffiti.

These old objectives are not dead. Their items have moved to the
Badassery section of the uplink.

A box of 3 demotivational posters can be bought for 1TC with 0 rep.
The spraycan can be bought for 1TC with 0 rep.

In their place comes one new objective and one extended objective.

The new objective is Assault a Crewmember. This objective requires you
to attack the specified target 2-5 times (random on objective
generation). It tallies from any attack that filters through the
`/datum/element/relay_attackers` element and has an "attacker"
associated with it.

Although it asks you not to kill the other player, it doesn't fail if
you kill them.

I have expanded the low-risk theft objectives with items like a mime
mask, lawyer badge and a fake moustache (commonly on cooks).

Finally, I've added a very low level set of steal-and-destroy objectives
aimed at some items that will require a bit of basic breaking and
entering, and the destruction of which may hurt crew morale.

```
/datum/objective_item/steal/traitor/donut_box
/datum/objective_item/steal/traitor/rpd
/datum/objective_item/steal/traitor/space_law
/datum/objective_item/steal/traitor/granted_stamp
/datum/objective_item/steal/traitor/denied_stamp
/datum/objective_item/steal/traitor/lizard_plush
/datum/objective_item/steal/traitor/moth_plush
/datum/objective_item/steal/traitor/insuls
```

This PR also fixes clown shoes missing a proc override to allow them to
actually register as a theft objective.


![image](https://github.com/tgstation/tgstation/assets/24975989/775d46cf-f40a-43e5-9bf1-3aa4a31d436e)

![image](https://github.com/tgstation/tgstation/assets/24975989/66c77815-1f2b-4dfb-99c6-b8f2e0061654)

![image](https://github.com/tgstation/tgstation/assets/24975989/85d3878a-c598-4ec0-9bb1-920380a004c6)
## Why It's Good For The Game

Basically my discussion with Watermelon focused on the idea that the
graffiti and poster objectives weren't really crimes. They baited
antagonists into very passive play early-game.

These new replacements encourage a more antagonistic playstyle. Starting
fights plus B&E are two bread-and-butter play paradigms for antaggery.

Giving a few early game theft + destroy options with a mix of impactful
items (like insuls and RPDs) versus more symbolic or emotive items
(plushies, donut boxes, Cargonia stamps) gets antagonists out and about
in the station, warming themselves up.

And having an objective to assault players (even if you don't kill them)
allows cheeky antags with a penchant for shittery to start fights with
players and start genuinely impacting the shift, involving sec and
drawing players into their antaggery.

Both of these natually ease players into the more substantive theft and
murder objectives.

The existing spray and posters are actually thematically super cool.
Traitors now have even more access to them since they can be bought for
1TC per spraycan/3-pack of posters. This lets antags with TC to spare
run gimmicks around them and adds extra fun to the Badassery section.
## Changelog
:cl:
del: Traitor objectives to place posters and graffiti the station have
been removed.
add: The items associated with the poster and graffiti objectives can
now be purchased from the Badassery section of the uplink. The posters
come in a box of 3 for 1TC, and the spraycans are 1TC each.
add: Adds a new Assault traitor objective, requiring you to the attack
the target a few times without needing to kill them. Earn TC and
reputation by starting barroom fights and bait players into escalation
battles for fun and profit.
add: Expands low-risk steal objectives to include the Chef's fake
moustache, Lawyer's badge, and Mime's mask.
add: Adds brand new shift start Steal & Destroy objectives for early
breaking and entering. Smash your way into a sec checkpoint to grab a
Space Law book, engineering to grab some insulated gloves or the psych
office to kidnap their moth plush.
fix: Fixes an issue where the steal clown shoes objective would never be
valid.
/:cl:

---------

Co-authored-by: Timberpoes <silent_insomnia_pp@hotmail.co.uk>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[de4cc8acc0...](https://github.com/TaleStation/TaleStation/commit/de4cc8acc06d9768ad24ddf8d3e5ddecf63ac5c8)
#### Sunday 2023-08-27 17:10:30 by TaleStationBot

[MIRROR] [MDB IGNORE] Adds a handful of Ninja Hacking MODule interactions of varying usefulness (#7432)

Original PR: https://github.com/tgstation/tgstation/pull/77707
-----
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

---------

Co-authored-by: Rhials <28870487+Rhials@users.noreply.github.com>

---
## [mamedev/mame](https://github.com/mamedev/mame)@[dbb0909cba...](https://github.com/mamedev/mame/commit/dbb0909cbab3f2094088a42687894e0e6053986b)
#### Sunday 2023-08-27 18:00:30 by wilbertpol

msx1_flop.xml: Added 105 working items, and replaced one item. (#11511)

* Replaced Konami Game Collection 3: Shooting Series (Japan) with a better dump. [file-hunter]

New working software list items (msx1_flop.xml)
-------------------------------
10 Programas Serie Oro (Spain) [file-hunter]
20 Programas Serie Oro (Spain) [file-hunter]
747 400b Flight Simulator (Europe, cracked) [file-hunter]
Alfabet en Deelsom (Netherlands) [file-hunter]
Alien Panic (Spain) [file-hunter]
Andon (Japan, hacked) [file-hunter]
Duad-MSX (Japan) [file-hunter]
Engels + Procenten (Netherlands) [file-hunter]
Fracta (Brazil) [file-hunter]
Graphos III (Brazil) [file-hunter]
Gruta de Maquine (Brazil)
The Iron Gauntz (Japan, prototype) [file-hunter]
Konami Game Collection 1: Action Series (Japan, alt) [file-hunter]
Konami Game Collection 4: Sports Series 2 (Japan, alt) [file-hunter]
Lettergrijper + Geld (Netherlands) [file-hunter]
Manuscript (United Kingdom) [file-hunter]
MSX Compilation 5 (Netherlands) [file-hunter]
MSX PageMaker DeLuxe (Brazil) [file-hunter]
Music Creator (Netherlands) [file-hunter]
Professional Data Retrieve (Brazil) [file-hunter]
Professional Paint (Brazil) [file-hunter]
Professional Publisher (Brazil, cracked) [file-hunter]
Rekenen tot 20 + Optellen en aftrekken tot 100 + Taalbedrijf (Netherlands) [file-hunter]
SF Zone 1999 (Japan) [file-hunter]
Simulador Profesional de Tenis (Spain) [file-hunter]
Super Procole (Japan) [file-hunter]
Super Procole 2 (Japan) [file-hunter]
Super Procole 3 (Japan) [file-hunter]
Supersellers 1 (Netherlands) [file-hunter]
Twin Hammer (Korea) [file-hunter]
The Wood (Spain) [file-hunter]
Woordmaker en Cijferend Vermenigvuldigen (Netherlands) [file-hunter]
Word Plus (Brazil) [file-hunter]
Wordstore+ (Netherlands) [file-hunter]
Zen (United Kingdom) [file-hunter]
3D Maze [Chalky]
666 - Uma Aventura Macabra [file-hunter]
8192 Story Tower [NAGI-P SOFT]
Baruko [file-hunter]
Blinky's Scary School [file-hunter]
Bounce Mania [MSXdev]
Burner Burst [file-hunter]
Buster Mystery [file-hunter]
City (Japan) [file-hunter]
Defence (v1.3) [MSXdev]
Galaxy Zone [aburi6800]
Ghosts'n Goblins (v1.1.0) [file-hunter]
Hibernated 1 - This Place is Death [file-hunter]
Hibernated 1 - Eight Feet Under [file-hunter]
JUMPER [NAGI-P SOFT]
Kame Graphics [file-hunter]
Kill Mice [MSXdev]
Las Aventuras de Rudolphine Rur (Spanish) [Dwalin]
Las Aventuras de Rudolphine Rur (Spanish, xmessage) [Dwalin]
Last War [NAGI-P SOFT]
Last War II [NAGI-P SOFT]
Logic (Russia) [file-hunter]
Mars [NAGI-P SOFT]
Mars II [NAGI-P SOFT]
May The Force Be With You [Cobinee]
Maze Chase [JLTurSan]
Micro Rocketz [MSXdev]
Mood Land [file-hunter]
Muhonmourn 3 (v1.1) [MSXdev]
Muhonmourn 3 (v1.1, with Ninja Tap support) [file-hunter]
Muhonmourn 3 (v1.0) [file-hunter]
Nibbles [file-hunter]
Oceano [file-hunter]
Paint-it (rev2) [file-hunter]
Paint-it (rev1) [file-hunter]
Paint-it [file-hunter]
Palhada City (Brazil) [file-hunter]
Penguin Catcher (v1.1) [MSXdev]
Penguin Catcher (v1.0) [file-hunter]
Pyramid Quest [Crappysoft]
Raftoid [PlattySoft]
Roger Dice (Spain) [oniric-factor]
Search for Mum (Netherlands) [file-hunter]
Sim City [file-hunter]
Storm Rescue [Concurso MSX-BASIC]
Stripgirl [file-hunter]
SubCommander (v1.02) [MSXdev]
SubCommander (older) [file-hunter]
Super Adventure [file-hunter]
The Tower of Gold [MSXdev]
UZIX (v1.0.0) [UZIX]
Wash Man (v2.8) [MSXdev]
Wash Man (v1.9) [file-hunter]
Wash Man (v1.5) [file-hunter]
Wash Man (v1.3) [file-hunter]
Wash Man (v1.2) [file-hunter]
Wash Man (v1.1) [file-hunter]
Wash Man (v1.0) [file-hunter]
Wired Shooting [Cobinee]
MSXMAS Demo [file-hunter]
Xadrama [file-hunter]
Xarchon [file-hunter]
XOR [Chalky]
XOR (older) [file-hunter]
Yellow Submarin [file-hunter]
Yobai [file-hunter]
Zero Gravity [file-hunter]
The zoBITRONics Inc [Hannu Töyrylä]
Zone TNT [MSXdev]
La Abadia del Crimen (Spain, alt) [file-hunter]

---
## [unit0016/effigy-se](https://github.com/unit0016/effigy-se)@[37d8f6162b...](https://github.com/unit0016/effigy-se/commit/37d8f6162bbef0c9cbeaf07cdba7cb93eb843e2a)
#### Sunday 2023-08-27 18:35:09 by LukasBeedellCodestuff

Compact shotgun re-added (#77759)

## About The Pull Request

This pr seeks to re-add the compact shotgun (slightly buffed with 1 more
ammo) and buff up its larger brother the combat shotgun (with 2 more
ammo.)

## Why It's Good For The Game
With the recent laser buffs, there is a real possibility for the compact
shotgun to return as a unique weapon to make the HOS slightly more
powerful. I am aware that it was a warden's weapon previously but the
HoS doesn't really have many fun toys to play with. The warden already
has crav maga (100x cooler than the laser) so giving this beast to the
HOS could help make it a more attractive and powerful head to play.
(Given 1 extra shot to keep up with the crazy lasers nowadays.)

In regards to the slight combat shotgun buff. The gun itself is ass,
it's barely ever used and the riot shotgun is superior because you can
actually put it in your armour slot. The hope is that this buff will
make people actually use it because it carries a lot of shots now so the
viability may increase.


## Changelog
:cl:
add: Added compact shotgun to the hos locker
add: Added compact shotgun as a traitor objective 
balance: gives the compact shotgun 1 extra shot
/:cl:

---
## [AzeAstro/PicoDuckyExecuter](https://github.com/AzeAstro/PicoDuckyExecuter)@[08442b8055...](https://github.com/AzeAstro/PicoDuckyExecuter/commit/08442b80555fda8470495b8f2dcf30905f90cb96)
#### Sunday 2023-08-27 18:36:36 by Atlas

Added configuration support

Yes, now from this era, we are not only dependent on existing networks to connect and then make our way through. NOW WE CAN CREATE OUR OWN NETWORK!
RISE MY SOLDIERS! TODAY,WE ARE MAKING OUR SECRET LINE TO DO WHATEVER WE WANT!
TODAY IS THE DAY,WHICH WE ARE THE RULERS OF THE WORLDS!
LONG LIVE PICO!!!

*Pls, Hollywood, hire me as writer*
Anyways ;))
Jokes aside, we actually can make our AP now in case we don't have any known networks to operate on. Prefer you to check out the Usage section in ReadMe.
Happy hacking! ;))

---
## [retlaw34/Shiptest](https://github.com/retlaw34/Shiptest)@[b033e1ed6a...](https://github.com/retlaw34/Shiptest/commit/b033e1ed6a1e7f87edc73a75a96bcf6536e39aba)
#### Sunday 2023-08-27 19:38:35 by Sun-Soaked

Update_Appearance Port (#2170)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
[(original pr)](https://github.com/tgstation/tgstation/pull/55468)
After nine years in development we hope it was worth the wait

I ported this specifically for the signals I'll need for world icons.
However, it had a lot of other useful stuff, so I ended up just grabbing
(almost) the entire pr.
I tried to grab as few of the superfluous code rewrites as possible to
make reviewing a bit easier, but I couldn't help grab stuff like the APC
icon code rewrite(the original code was a war crime).

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

- ports the wrapper proc `update_appearance` for icons, descs, and
names, adds `update_desc` and `update_name` subprocs to handle those.
Things. without just stuffing them into update_icons like some kind of
psychopath

- ports a bunch of signal hooks useful for changing names, descriptions,
and icons. I needed these for world_icons which is where this wild ride
all started

- ports some `base_icon_state` implementation. Stuff like spear code
makes slightly less duplicates(and more sense) now which is nice.
We could definitely implement it more I think but that's a future me
problem

- 500 files of immersive vsc-mass-editing action to implement
`update_appearance()`(sorry in advance, but not as sorry as I was when
manually copy-pasting the custom ones for like 3 straight days)

-"consig" and "comisg" have been taken out behind the codebase and shot.
Not 'technically' a bug it just made my head hurt

-My first pr with 0 player facing changes (confetti)
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: TemporalOroboros, Memed Hams
code: ports update_appearance, update_name, and update_desc from tg, as
well as associated signals
code: a bit of base_icon_state implementation. Can you believe it's been
sitting in our code almost unused for like 3 years
code: cleans up some code formatting, mainly around custom icons and
overlays
code: fixes the typos in COMSIG_STORAGE_EXITED and
COMSIG_STORAGE_ENTERED
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [saltwaterterrapin/EvilHack](https://github.com/saltwaterterrapin/EvilHack)@[3a3cd5ad71...](https://github.com/saltwaterterrapin/EvilHack/commit/3a3cd5ad7103c5282cd64f7ec389ed063b2fe7bc)
#### Sunday 2023-08-27 20:47:09 by k21971

Wizard of Yendor's tower overhaul.

The Wizard of Yendor's home has undergone renovations. The old place was
a bit too restrictive, and security was somewhat lax 🙂

Quite a few changes in this commit. The Wizard's tower is now unlike
anything from its previous incarnation. Here's the breakdown:

* The Wizard's tower is still three levels as before, but each level has
been completely redesigned
* The ground level is much larger than before, with the entire base of
the tower surrounded by a moat, and the wizard has conscripted a company
of the Yendorian army as security
* The second/middle tower level is smaller than the first, and houses
various spellcasters that are there to train under the watchful eye of
the Wizard. Some monsters have been held captive here, used for
experimentation and other dark arts
* The third and final level is the very top of the tower, where the
Wizard of Yendor performs the most evil of magic spells on a magical
floating platform outside of, but connected to, the top of his tower.
This is also where the Wizard hoards his most prized treasures,
including the fabled Book of the Dead
* Entering the final level of the Wizard's tower is now counted as an
event and an achievement, and is livelogged. This also triggers a
message when entering the top level for the first time, warning the
player about falling to their death should they misstep (open air
terrain)
* How the special levels in Gehennom appear had to be tweaked a bit, as
it were possible from the initial 'wizard's tower is its own branch'
commit that the VS level could sometimes not be generated, and the
player could skip the invocation and take the stairs straight down to
the Sanctum. So now, the total number of Gehennom levels shaved off is
four instead of five, but the demon boss levels will always appear in
the correct order and with a tighter spread. The 'fake' wizard towers
are dropped from two to one, with the one guaranteed to have the portal
to the wizard tower branch, and it will always be the last Gehennom
level right before the VS level
* A fix for ants sometimes spawning in barracks was slipped into this
commit (NetHack 3.7 commit 23428d0)

The vast majority of changes are in the .des file for the tower
redesign. Storming the Wizard's tower will now be a more challenging
endeavour, but more rewarding also, and hopefully a lot more exciting
and fun than before.

---
## [JackSimoni/ncurses-projects](https://github.com/JackSimoni/ncurses-projects)@[417858c222...](https://github.com/JackSimoni/ncurses-projects/commit/417858c222720a6c89bf1c4fa679a13e8903bbe2)
#### Sunday 2023-08-27 20:50:34 by Jack Simoni

Read extended description please.

This is the new file that is replacing writeFile.cpp. The purpose of this program is to translate ASCII maps into "array-compatible maps." Not all ASCII maps/sprites/characters, etc. follow the basic N x M shape that is needed for creating a simple array. Depending on the image size, this can be troublesome, as from my experience, the easiest way to print complex ASCII graphics is to use arrays, and run print statements through loops. Doing ASCII art within your .cpp program is tiresome, and very inconvenient. Every char you put towards your art needs 4x the work, as you are constantly surrounding it by "' char '," to make it array-compatible. This program fixes this. All you need is to do your ASCII art in a .txt file, which I call the raw file. After your art is finished, you pass the raw file through this program, create a refined file (which for user purposes isn't that useful, its just a buffer for the program to run its magic) and a final file, which is created on your computer, that is in perfect format for you to just copy paste it into your program. Now you should have an array compatible ASCII graphic.

---
## [MrManGuyMan/tgstation](https://github.com/MrManGuyMan/tgstation)@[6c34d93be7...](https://github.com/MrManGuyMan/tgstation/commit/6c34d93be715012943626d0f812e99f730a536ef)
#### Sunday 2023-08-27 21:43:31 by necromanceranne

Nukies Update 7: Hats (Also massive uplink standardization, weapon kits and ammo changes) (#77330)

## About The Pull Request

Massively overhauls and standardizes the nuclear operative uplink. 

### Weapon Kits

Essentially, all the main weapons of the uplink have been changed to
instead come as 'weapon kits', which are essentially cases containing a
weapon loadout to enable operatives to easily start operating on only
just one item purchase, without the fuss of worrying whether or not
operatives are getting spare ammo, or getting relevant equipment for
success. Consider this a pseudo-loadout, though without necessarily
restricting the purchasing of more weapon kits.

All kits come in three categories: Low Cost (8 TC), Medium Cost (14 TC)
and High Cost (18 TC). This is also matched by categorized ammo costs;
Basic Ammo (2 TC), Hollow Point and Armour Penetrating (4 TC),
Incendiary (3 TC) and Special (or anything that does not easily fit
these categories and does something real extra) (5 TC). Weapons that
lacked these ammos have gained these ammo types to fill the gaps.

<details>
There is may one exception to this in disruptor ammo, which is priced as
basic ammo if only because it isn't _quite_ good enough to justify
pricing at 5 tc and I can see an op wanting to use it as a basic ammo
type instead of normal .50 BMG against, say, a silicon/mech heavy
opposition. Since it cannot kill organics on its own, I'll consider this
mostly basic-adjacent
</details>
The kits have also been labelled based on potential difficulty. This
reflects possible difficulties in using the item, how conducive it is to
success for how much game knowledge needed to actually use it, and how
likely an op is to succeed using it. I don't expect ops to win using
nothing but a rocket launcher, but I think ops should get a fair shake
at trying, yeah?

The kits are as below:
#### **Low-Cost**
_Bulldog (Moderate):_ Shotgun and three magazines of standard ammo.
_Ansem (Easy/Spare):_ Pistol and three spare magazines of standard ammo.
#### **Medium Cost**
_C-20r (Easy):_ SMG and three spare magazines of standard ammo.
_Energy Sword and Shield (Very Hard):_ Energy sword and shield. (Also a
special hat)
_Revolver (Moderate):_ Revolver and three speedloaders of standard ammo.
_Rocket Launcher (Hard):_ Rocket launcher with three spare rockets.
#### **High Cost**
_L6 SAW (Moderate):_ LMG, and that's it. No spare ammo.
_M-90gl (Hard):_ Rifle, two spare magazines of standard ammo and a box
of rubber grenades.
_Sniper (Hard):_ Sniper rifle, two spare magazine of standard ammo, and
one magazine of disruptor ammo. Also suit and tie.
_CQC (Very Hard):_ Comes with a stealth implant and a bandana.
_Double-Energy Sword (Very Hard):_ Double-energy sword, syndicate soap,
antislip module, meth injector and a prisoner jumpsuit.
_**NEW** Grenadier's Kit (Hard):_ Grenadier's belt and grenade launcher
(the one that launchers chem grenades). (I replaced the shit acid
grenade with another flashbang in the belt)

Surplus SMG (Flukie difficulty) has been unchanged. It just now comes
with two rations.

Includes two new revolver ammo types: Phasic, which goes through walls
and armor, but has significantly less damage as a result (I've equalized
the revolver damage and the rifle version's damage to 30 for both). And
Heartseeker, which has homing bullets. Both are Special ammo, and are
priced at 5 TC a speedloader.

### Other Gear

The other items in the uplink have also been consolidated and
standardized in various ways.

#### Grenades

Most now cost 15 TC for three grenades of any given type (including the
full fungal tuberculous). This is pretty much identical to the previous
price, just more consistent overall and front-loaded in cost.

#### Reinforcements

All the various reinforcements now cost 35 TC and all refundable,
equalizing cost to the average across the reinforcements. This is
primarily because I feel like all these options should be weighed
equally, and not one of these options are necessarily worse or better
than the other in their current balance. They're largely inaccessible
for normal ops regardless, and typically come out when there is a
discount or war ops. I took the average value and went with it. Not much
more to say.

#### Mechs

They're just cheaper. These things still suck and they need help.
They've always needed help. A slightly less excessive value for the
mechs may help see people willing to spend the TC on them. I doubt it. I
seriously suggest not buying these still. I keep them in primarily
because they are big stompy mechs and are kind of iconic 'war ops' gear.

#### Bundles

Since I've implemented weapon kits, gun bundles are rather redundant. So
the bulldog weapon and ammo bundle, the c20-r weapon and ammo bundle and
technically the sniper bundle were removed. The sniper bundle is now the
weapon kit, obviously.

Nothing else here really. Except for one....

#### Implants

Not much changed here. I standardized the implant prices to 8 TC a pop.
This is in accordance with traitor implants, which ops also get. So
everything in this category bar a few exceptions (like macro/microbombs)
are around 8 TC. Makes sense to me, really.

Importantly, I made the Implant bundle 25 TC, and I unrandomized the
contents. Who in the right fucking mind would spend 40 TC just to get
five reviver implants is beyond me. But instead, you get one of each of
the cybernetic implants except thermal eyes (you can just buy thermals
and get the benefit of both vision types; x-ray and thermal vision, if
you want to use smokescreens a lot).

#### Base Keys

They're all now 15 TC, except the fridge which is 5 TC. It's weird
they're valued differently when they are taken mostly to do gimmicks
like xenobio and toxins in a hurry before hitting the station. So we've
standardized it.

## Hat Crate

**YES, GOOD SIR, YOU TOO CAN ORDER A HAT CRATE FROM THE SYNDICATE STORE
FOR ONLY 5 TC!**

**NO NEED FOR A KEY, JUST BUY IT AND PULL IT OPEN WITH YOUR STANDARD
ISSUE CROWBAR!**

**ENJOY YOUR NEW CRATE! ENJOY YOUR NEW HAT!**

**PUT IT ON USING THE FREE HAT STABILIZERS WE INCLUDED WITH THE HATS!**

~~**NO REFUNDS IF YOU GET BLOOD ON YOUR HAT!**~~

<details>
There is a 1% chance to instagib people with direct hits from a rocket.
This does the crit effect.
</details>

## Why It's Good For The Game

The uplink needed more spring cleaning and standardization.

With this, I've partially implemented my older idea for ammo consistency
and initial allowance for nukies. Ammo is kind of over-priced and often
where a good chunk of TC goes towards without really pushing nukies
towards meaningful success. And it is often what is tripping up new
players who didn't think to get any. Now, when they get a gun, they get
ammo in their case. On top of this, the weapon kit category is both at
the top of the uplink AND has a little label to say 'Recommend', so that
these new players will hopefully know they should be looking there
first.

In addition, it is the gateway towards a concept that is currently being
worked on. Nuclear operatives having some degree of predefined loadouts
for players to select if they aren't sure what they want, or don't know
what to get. Nukies is very confusing for many players. So giving them a
fighting chance with some premade setups can help ease them into the
role without needing too much player knowledge in how to apply the
items. This is only one step towards that, so that players can identify
what gear they need to help succeed based on their skill.

I wanted to implement a difficulty warning so that players can choose
gear loadouts that are actually conducive to their skill and knowledge.
I based it on how much players would need to know to engage in combat
with it, and how much fiddling is required to get something to work
properly (overly involved reloading is a consideration, for example, as
well as precise button presses). In addition, how much of a force
multiplier some weapons can be for their ease of use.

Most people recognize the c20-r as the most new player friendly weapon,
as an example. So it would be good to steer players towards taking that
gun because of how easy it is to use, understand and succeed with it.

And most importantly of all; Having standards within the uplink is
important. Most of the values in the uplink are just completely random.
Nobody has a good grasp of what is too much or too little. Even just a
hint of consistency, and people will stick to it (see implants for what
I mean). And there is still some work to be done even there. A good
start is weapons. Price for power can be meaningful when decided whether
we want some weapons to come out more often than others. Players do
enjoy making informed decisions and choices, and having affordability be
a draw to some otherwise less powerful weapons (looking at you, Bulldog)
can actually be a worthwhile and meaningful difference.

~~I thought it would tick off the gun nerds to change the calibers on
the guns.~~

~~I also thought adding hats would be funny given the release of TF2's
most recent update.~~

## Changelog
:cl:
balance: Standardizes some of the nuclear operative entries to have more
consistent pricing within their respective categories.
add: Adds some new categories so that players have an easier time
navigating the nuclear operative uplink.
balance: Many items have had prices reduced or adjusted to make them
more desirable or more consistent within their category.
add: Weapon kits have replaced almost all the individual weapons in the
uplink. You now buy these instead of the individual weapon. These often
come with spare ammo or relevant gear for success.
add: Most ammo types have been standardized in price.
refactor; Removes a lot of redundant item entry code and tidies up the
actual code part of the nuclear uplink so that it is much easier to find
things within it.
add: Added 40 new cosmetic items to the Syndicate Store. Buy them now
from the Hat Crate, only 5 TC!
code: Updated the nuclear operative uplink files.
/:cl:

---
## [MrManGuyMan/tgstation](https://github.com/MrManGuyMan/tgstation)@[95ec0e6545...](https://github.com/MrManGuyMan/tgstation/commit/95ec0e65458ece9c5c80952e75d5d32c4fbb794b)
#### Sunday 2023-08-27 21:43:31 by necromanceranne

Dissection experiments are handled by autopsy surgery. Removes redundant dissection surgery. You can repeat an autopsy on someone who has come back to life. (#77386)

## About The Pull Request

TRAIT_DISSECTED has had the surgical speed boost moved over to
TRAIT_SURGICALLY_ANALYZED.

TRAIT_DISSECTED now tracks if we can do an autopsy on the same body
again, and blocks further autopsies if it is on the mob. A mob that
comes back to life loses TRAIT_DISSECTED. This allows for mobs to be
autopsied once again.

Since it is completely redundant now (and was the whole time TBH),
dissections have been removed in favour of just having the experiment
track autopsies.

Fixes https://github.com/tgstation/tgstation/issues/76775

## Why It's Good For The Game

Today I showed up to a round where someone autopsied all the bodies in
the morgue, not realizing they were using the wrong surgery. Since I
couldn't _redo_ the surgery, this rendered all these bodies useless.
This was not out of maliciousness, they just didn't know better. There
are two autopsies in the surgery list, but only one is valid for the
experiment and doing the wrong one blocks _both surgeries_. Dissection
is completely useless outside of experiments. This same issue also
prevents additional autopsies on the same person, even if they had come
back to life and died again after you had done the initial autopsy.
Surely you would want to do more than one autopsy, right? That's two
separate deaths!

This resolves that by giving you a method of redoing any screwups on the
same corpse if necessary. It only matters if the experiment is available
anyway, so there isn't much reason to punish players unduly just because
they weren't aware science hadn't hit a button on their side (especially
since it isn't communicated to the coroner in any way to begin with). It
also removes a completely useless surgery and ties in the experiment to
what the coroner is already going to be doing. They can dissect their
corpses to their hearts content without worrying about retribution from
science for doing so.

In addition, someone repeatedly dying can continue to have autopsies
done on them over the course of the round. The surgery bonus only
applies once, so the only reason to do autopsies after the first is to
discover what might have killed someone. No reason this should block
further surgeries, just block surgeries when the person remains a
corpse.

## Changelog
:cl:
fix: You can do autopsies on people who were revived and died again
after they had already been dissected.
qol: Autopsies have become the surgery needed to complete the dissection
experiments. As a result, the dissection surgery has been removed as it
is now redundant.
qol: A coroner knows whether someone has been autopsied and recently
dissected (and thus hasn't been revived) by examining them.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [TheFwuffernaut/Baronic-Defense-Forces](https://github.com/TheFwuffernaut/Baronic-Defense-Forces)@[db4b8030c0...](https://github.com/TheFwuffernaut/Baronic-Defense-Forces/commit/db4b8030c087d4389fc0b6db9911773a2d2e3c4d)
#### Sunday 2023-08-27 23:55:30 by TheFwuffernaut

1.0.6

changelog:
	Core Bonuses
		Spiderline Failsafes - Updated text to: “1/round, when it would become Prone from an attack or failed Save from a hostile character, as a reaction, your mech can take 2 heat to force that hostile character in line of sight to make an Agility save.  A failed Save makes you Immune to the source of the Prone and instead inflicts Prone on your target.  If the hostile character fails the save and was flying, it instead immediately lands (this counts as falling without any damage).”
		Nanoweb Countermeasures - Updated text to: “1/round, your mech can remove a condition when it Boosts.  If your mech passes adjacent to another hostile character when it uses this effect, you can add the Lock On condition to that character. Slowed, Stunned, and Immobilized conditions can be removed this way and do not prevent a Boost if a Boost is the first action on your turn after protocol actions.”

	Akinaka
		One in the Pocket - clarifies damage upgrades to 3d6+GRIT instead of just 3d6
		C80 Charges - C-Spray Mines activation area to line 5, height 10 (from line 8, height 8), removed two tier height detonation requirement, detonation damage down to 1d6+2.
		New text: “This mine’s activation radius is a Line 5 that is up to 10 spaces tall, selected from free spaces when placed.  Targets caught in the detonation area must pass a HULL save or take 1d6+2 KINETIC damage and be knocked back 3 spaces. Each use places two C80 mines.”
		Lion Coast Missile - First sentence updated to “To activate this system as a Full Action, make a tech attack against a target in Sensors and line of sight that has the LOCK ON condition.”

	Akrafena
		Flame Gatling - Added “move up to your SPEED” to the system text. First sentence now “At the start of your next turn after you activate this system, gain 2 heat, move up to your SPEED, and draw two Line 5 areas from your mech.”
		Silk Web Defense Screen - Damage to 3 from 1d3+1, Knockback up to 3 from 2

	Chambi
		Mech lore text updated: New text: “The Siege of Creighton and defeat of the Baronic Warhost resulted in a black eye for the Baronies and the genesis of the artillery project that became the BDF Chambi.  There was dissent in the ranks on naming the project after a blunt instrument instead of the swords of other BDF chassis, quelled when field tests melted an entire battlefield of nails under the hammer.  The Chambi’s operation is aided by an integrated STAR-Class NHP co-pilot to serve as weapons officer during extended sieges, freeing mental capacity for the pilot to navigate the mech through hostile environments.  STAR-Class NHPs are meticulous and enjoy bleak humor, often aware of the paradox of being tasked to a mechanized chassis designed for renewable energy and converted to a war machine.”
		Non-Human Person Co-Pilot Lore Text: Renamed to “STAR-Class Non-Human Person Co-Pilot”, Added “BDF pilots respect their crewmates.”
		NHP Power Reroute Core Passive: Removed AI tag requirement, New name: “NHP Extra Hands”, Reload die new text:
“Gain a Reload Die, beginning at 4.  As a Protocol, decrease the Reload Die by 1. When the Reload Die hits 1 you may reload a Loading weapon of your choice; the Reload Die is then set to 4.”, Speed boost removed and implemented in frame - frame is now 3 speed instead of 2, Accuracy option folded into Stable Footing.
		Stable Footing - New text: “The Chambi has +1 difficulty on ranged and melee weapon attacks after it moves on a turn. 1/round, it has +1 accuracy on all attacks made from a weapon when fired before moving on a turn.”
		Missile Minefield - Added duration “until the end of the scene”
		SALMON-Class NHP - Clarified the player must target the attacking character with text “Effect: You may Skirmish for 1/2 damage against the attacking character”, Lore updated to replace “imported” with “kidnapped”.
		Lava Load Cannon - Triple Tap profile to 3 damage (from 1d6)

	Dao
		Double-Time Armor - SP Cost up to 2 SP (from 1 SP)
		Print Subaltern Drone - Subaltern damage to 4 Kinetic (down from 3 + GRIT/2 Kinetic), Added to the Subaltern Drone Full Action “When deploying a new Subaltern Drone as a Full Action, create a burst 2 zone of Soft Cover that lasts until the end of your next turn.”
		Helicopter Drone - Updated text from “Gain the FIRE SUPPORT reaction, which can be taken once for each deployed Helicopter Drone” to “Gain the FIRE SUPPORT reaction, which can be taken once for each deployed Helicopter Drone (each instance of this system can deploy one Helicopter Drone)”
		Universal Recycler - Flower Drone HP down to 5 HP from 5+GRIT HP

	Jian
		“Moonlight” Combat Cycle - Updated to new text: “Deploy two Drones with 20 HP which occupy 1x2x1 spaces each into adjacent free and valid spaces. The drones count as Size 1 and each can hold one size 1 or size ½ actor as a rider. The drones can combine as a Protocol into a single Size 2 character to hold a size 2 actor. A character may mount either drone as a Quick Action, moving the drones with them on all their movements. As a protocol, you may move each of the drones up to 6 spaces (independently if they aren’t combined), carrying the riders with them. As a Quick Action per drone, you can prime a Self Destruct on that drone, which then explodes at the end of the next turn in a Blast 2 area for 2d6 damage, or half damage on a successful AGILITY save.”, Machine gun attack protocol removed, Clarified the drones move when their riders move.
		Volatile Charges / Firecracker Mine - Damage to 3 Explosive (from 1d3+1 Explosive)
		Slaughter Shotgun - Sunderer Round text updated from “This causes your next attack to cause an additional 4 Explosive damage” to “This causes your next attack to cause on hit an additional 4 Explosive damage”

	Kampilan
		Binary Laser Rifle - Gained “On Hit: Target must make a HULL save or become Jammed.”
		Rifle Butt - Gained ““On Hit: Target must make a HULL save or become Prone and Impaired.”
		Starfish Charges - Pinwheel Grenades; Added after “from the targeted space”, “outward in a direction of your choice. These areas cannot overlap.”, Supernova Mine; Added “outward in a direction of your choice.” after “from the targeted space.”
		Distributed Tactical Net Upgrade / Positional Mapping - updated text to clarify each of those spaces for mines and grenades.
		Golden Wave Laser Lore - Added “They were rejected from wider adoption by the BUC due to excessive melting of barrels and limited batteries.  BDF pilots are reviving the weapon pattern to achieve sustained firepower capable of overheating enemy coldcore reactors and outright destroying frames with expired warranties.”
		BANSHEE-Class NHP - Updated Lore Text: “Captured HORUS agitators embedded among the Ungratefuls yielded several PLAYER_TWO COMP/CON units, subsequently reverse engineered by the BDF and installed in scout-pattern Kampilan frames as a long range search and destroy unit operating independently of resupply for extended periods.  These PLAYER_TWO units, designed to operate a soldier’s hardsuit while they slept based on data from a flash pattern of their subjectivity, were scrubbed of any code related to HORUS and severed from the subjectivity of the soldier, miraculously resulting in the genesis of a NHP capable of operating the soldier’s hardsuit in a manner similar to a homunculus - a machine to fight when the soldier could not.  Knowledge of BANSHEE-Class NHPs is suppressed by the BUC and their personalities are both gregarious and fatalistic.”

	Khanda
		High Philosophy Mod - Removed 1/round limit.
		RIVER-Class Comp/Con - Updated text from “When you jump, you leave behind you spaces of Dangerous Terrain.” to “When you jump, you leave behind you spaces of special Dangerous Terrain. This Dangerous Terrain requires an Engineering Save versus your Save Target rather than an Engineering Check to avoid damage.”
		Dancing Cannon - Added “and can attack the same target twice.”

	Kiem
		Low Profile - Added clarifying clause “and draws line of sight over cover from height 1” from the height example.
		Puppy Patrol Drone - The puppy can now follow you - add “As a Protocol, you may move the Puppy Patrol Drone 4 spaces directly towards you.”, Protocol Name in C/C is “Maintain Puppy Formation”
		Power Pylons - Clarified tech attack push is on hit
		Shotgun Minigun - Removed “This weapon cannot attack targets within range 5 of you.”
	Klewang
		Updated artwork on GitHub from .JPEG to .PNG for transparency.
		Cargo Crane - Added “On Hit” qualifier as alternative to activating “Lift Together” action as a Full (this can result in two targets getting Lift Together’d in a Barrage)
		Typhoon Boot - Replaced “Before attacking with this weapon” with “As part of attacking with this weapon”.

	Shotel
		Heat cap on frame to 6 (from 7)
		Carapace Crash Pads - Cost down to 1 SP (from 2 SP)
		Laser Chainsaw - Updated text on higher elevation to “If you are at a higher elevation than your first target when you attack, instead of choosing a single target in Threat 1, this weapon can instead attack as a Cone 3, with the Line 3 area originating out of the furthest target”
		DAEVA-Class NHP Lore - Replaced “were installed on ” with “are assigned to”

---

