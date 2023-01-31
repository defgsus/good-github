## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-01-30](docs/good-messages/2023/2023-01-30.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,195,247 were push events containing 3,361,023 commit messages that amount to 279,380,574 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 40 messages:


## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[059554ae16...](https://github.com/TaleStation/TaleStation/commit/059554ae16e6eb4efe68dc2f9a4c0df031622998)
#### Monday 2023-01-30 00:03:47 by TaleStationBot

[MIRROR] [MDB IGNORE] Refactors Suicide Verb + Basic Mobs (actually all (most) living mobs) Can Now Suicide (#4258)

Original PR: https://github.com/tgstation/tgstation/pull/72919
-----
## About The Pull Request

On the tin. There was a lot of needless copy-paste and a lot of
single-letter vars and weird indentation and... well just all of it was
at least eight years old. So, I decided to "abstract" as much as I could
of it out instead of piling onto the big copypaste clusterfuck for
implementing basic mob suicide.
## Why It's Good For The Game

Fixes #72903

Having more procs that can be easily repeatably called to the same
results is much better than having to transplant the same exact three
lines everywhere. It's also a good first step to further in-depth
behavior by allowing sub-type overrides of certain procs (which is quite
nice). Just feels more extensible overall for the next guy who wants to
add funny suicide behavior whenever they might come around.

There's probably a few better ways to do what I did, but I wrote code
comments explaining why I did what I did. I think there's a few ways to
make it more agnostic, but I think that'll be another can of worms that
will bloat out an already quite large PR. Let's just get the framework
set.

(this refactor should also make it quite easy to unit test suicide
actions :eyes:)
## Changelog
:cl:
fix: All Mobs (including Basic mobs) are now able to suicide. (warning:
some exclusions remain)
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [ktoma36/Citadel-Station-13-RP](https://github.com/ktoma36/Citadel-Station-13-RP)@[287fb079d1...](https://github.com/ktoma36/Citadel-Station-13-RP/commit/287fb079d1d52c8f244c7f08b3efa18de567f1cd)
#### Monday 2023-01-30 00:09:06 by Felix

Whitelist backend changes (#4996)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Whitelist are run by name, so renaming a whitelisted species also needs
an update to the WL as well.
Removes a shitty gimmick of a mirror most people dont have access to
because its a fucking nightmare of conditions we partially removed
and a fix for both runtimes and uninteded stat cheating
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
del: Removed the code behind the raider mirror
fix: fixed the shadekin traits applying to non shadekin
config: changed WL using Species ID rather than name
refactor: changed character species to always have a superspecies_id
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [wolframowy/tgstation](https://github.com/wolframowy/tgstation)@[63561ca455...](https://github.com/wolframowy/tgstation/commit/63561ca455933a38f3390f7fcfa6266fda3c53b3)
#### Monday 2023-01-30 00:25:49 by san7890

Guards against uplink failsafe code being the same as unlock code (#72113)

## About The Pull Request

There's probably a better way to do this to be honest, but I think it's
silly for both to potentially be the same and this should work alright.
## Why It's Good For The Game

Fixes #71446.

I don't think the Syndicate is that stupid.
## Changelog
:cl:
fix: After a recent mishap with a high-ranking Syndicate operative, the
uplink's unlock code and failsafe code (the one that makes it blow up if
you say it) should never turn out to be the same.
/:cl:

---
## [goonstation/goonstation](https://github.com/goonstation/goonstation)@[a02c0a6ff9...](https://github.com/goonstation/goonstation/commit/a02c0a6ff97eb3057ffbe8aea95edf9f810822d8)
#### Monday 2023-01-30 01:05:27 by Xkeeper

emergency api shutoff version 3: holy shit, shut up

---
## [DaedalusDock/daedalusdock](https://github.com/DaedalusDock/daedalusdock)@[4b69f5d536...](https://github.com/DaedalusDock/daedalusdock/commit/4b69f5d53635f72e87dd045b4ba00bc7478ce83a)
#### Monday 2023-01-30 01:06:30 by Kapu1178

Speed up the roundstart significantly (#147)

* Resolves is_banned_from headaches and lag (Speeds up roundstart significantly) (#69376)

About The Pull Request

Just to be clear, when I refer to time here, I am not talking about cpu time. I'm talking about real time.
This doesn't significantly reduce the amount of work we do, it just removes a lot of the waiting around we need to do for db calls to finish.

Adds queuing support to sql bans, so if an ongoing ban retrieval query is active any successive ban retrieval attempts will wait for the active query to finish

This uses the number/blocking_query_timeout config option, I hope it's still valid

This system will allow us to precache ban info, in parallel (or in batches)
With this, we can avoid needing to setup all uses of is_banned_from to support parallelization or eat the cost of in-series database requests

Clients who join after initialize will now build a ban cache automatically

Those who join before init is done will be gathered by a batch query sent by a new subsystem, SSban_cache.

This means that any post initalize uses of is_banned_from are worst case by NATURE parallel (since the request is already sent, and we're just waiting for the response)

This saves a lot of headache for implementers (users) of the proc, and saves ~0.9 second from roundstart setup for each client (on /tg/station)

There's a lot of in series is_banned_from calls in there, and this nukes them. This should bring down roundstart join times significantly.

It's hard to say exactly how much, since some cases generate the ban cache at other times.
At base tho, we save about 0.9 seconds of real time per client off doing this stuff in parallel.
Why It's Good For The Game

    When I use percentages I'm speaking about cost per player

I don't like how slow roundstart feels, this kills about 66% of that. the rest is a lot of misc things. About 11% (it's actually 16%) is general mob placing which is hard to optimize. 22% is manifest generation, most of which is GetFlatIcons which REALLY do not need to be holding up the main thread of execution.

An additional 1 second is constant cost from a db query we make to tell the server we exist, which can be made async to avoid holding the proc chain.

That's it. I'm bullying someone into working on the manifest issue, so that should just leave 16% of mob placing, which is really not that bad compared to what we have now.
Changelog

cl
code: The time between the round starting and the game like, actually starting has been reduced by 66%
refactor: I've slightly changed how ban caches are generated, admins please let me know if anything goes fuckey
server: I'm using the blocking_query_timeout config. Make sure it's up to date and all.
/cl

* manifest_inject() stuff

* Fixes role banned players not being banned from roles that they are banned from (Option Two) (#69703)

I feex

* Saves on average 10 seconds from roundstart times (#71730)

## About The Pull Request

When runlevels change mid work, subsystems running behind have their
next_fire updated.
It's offset by a sum of random numbers, so things don't bunch up,
especially KEEPTIME SSs

The trouble is we have so many subsystems that get added at roundstart
that this offset gets LARGE, like 10 seconds on average.

So instead of randomly offsetting, why not "fill" a set of time slots?
Only 1 keeptime subsystem a tick, and 4 others. Then we just fill up
those buckets and get to it (also don't offset things that are already
processing)

I've talked to mso a bit about this. What he reccomended was sampling a
random time withing a 2 second window.
I'm not totally sure why, kinda waiting for him to tell me off, if he
does I'll fix things up.

This pattern takes the max possible delay from 16 (76 * 5 / 20)) seconds
to 0.7 (56 / 4 / 20)
It obviously scales with subsystem count, but I like this scaling a bit
better

I've applied the same pattern to the offsetting we do at the start of
Loop(), for ticker subsystems. I am less confident in this, it does take
last fire times from at worst 3.75 seconds (15 * 5 / 20) to a static
0.75 (15 / 20)
As stated I'm less sure of this, hoping to get mso'd so I can clean
things up

## Why It's Good For The Game

Makes roundstart snappier

## Changelog
:cl:
code: Roundstart "starting" should be much snappier now
/:cl:

Co-authored-by: Kyle Spier-Swenson <kyleshome@gmail.com>

* fix missing macro

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Timberpoes <silent_insomnia_pp@hotmail.co.uk>
Co-authored-by: Kyle Spier-Swenson <kyleshome@gmail.com>

---
## [clintjedwards/gofer](https://github.com/clintjedwards/gofer)@[d90ca94280...](https://github.com/clintjedwards/gofer/commit/d90ca942806b3772a9c52a887186ef664e00889a)
#### Monday 2023-01-30 03:04:56 by Clint J Edwards

feat: Pipelines are now versioned

In order to eventually have canary-able deployments in Gofer we must
first support versioned pipelines.

This allows us to:
* Have a good target in which to roll back and forward.
* Understand what we are gaining and losing on each change.
* Track each update as it happens.

This is not easy though as pipelines have parts which are easy to version
(namely the config) and parts which are much harder to version (how do
we handle the cutting over of triggers?).

Because of this nuance, we've had to redesign a lot of earlier
assumptions for how Gofer models worked. This was a major refactor and
since I was here I made a few other large sweeping changes.

* Full storage package refactor: The storage layer was hard to use,
brittle, and inflexible. I've refactored it, leaning a bit more on
sqlx and going back to basics. I tried to make the storage package
work in the past by keeping the domain models to a minimum. I've since
learned this does not work once things become reasonably complicated. One
of the main refactors to the storage package is the introduction of
dedicated storage models. This means that I have to write a bunch of
boilerplate code to switch from in-memory models to the storage ones,
but the looser coupling is worth it. More storage refactors coming
as I learn what works at large scale and what doesn't.
https://github.com/go-jet/jet looks interesting.

* Removal of Triggers as Pipeline configuration: I desparately wanted
to have pipeline configurations encompass everything a pipeline would
have to offer, so that it was easy to look at a config and know exactly
what was going on in a particular pipeline. Triggers were a pain in the
ass though. Triggers unfortunately occupy a very special place in Gofer's
archetecture. Without triggers nothing really gets done. And so allowing
the user to apply all the same functionality to triggers as they would
with any other deployment was short-sighted. Triggers don't make a lot
of sense as a canary deployment. Triggers aren't ephemeral, they are
either on or their off. No in-between.

Instead Triggers can now be added to your pipeline via the command line.
This way trigger subscriptions aren't held down by the paradigms of
configuration change.

* Pipelines are now versioned: Not only have we added versions to pipelines,
but they now have deployments and configurations and metadata and a lot
of smaller loosely coupled parts so that they aren't a huge data monolith.
This means a lot of breaking changes for outward (and inward for that matter)
apis.

* Just lots of general breakages everywhere: Pretty much a large percentage
of things just aren't the same anymore.

---
## [lessthnthree/Skyrat-tg](https://github.com/lessthnthree/Skyrat-tg)@[a9c430a5e4...](https://github.com/lessthnthree/Skyrat-tg/commit/a9c430a5e43a638d3b56f57b663104e1e6a57364)
#### Monday 2023-01-30 03:15:26 by SkyratBot

[MIRROR] Basic Mobs Now Actually Have A Deathgasp [MDB IGNORE] (#19002)

Basic Mobs Now Actually Have A Deathgasp (#72950)

## About The Pull Request

Pretty obviously an oversight since we only checked for simple_animal
for this, but should also factor in the fact that we could now be a
basic mob.

Actually I tested it on Sybil just now and deathgasps just never worked.
We were setting death_message for... I guess when they die? It's just
fucked but it works on my local now. blurgh
## Why It's Good For The Game

Ported simple animals that are now basic mobs were able to deathgasp
this time last year. Silly that they aren't able to do that now.
## Changelog
:cl:
fix: Basic Mobs are now able to deathgasp.
/:cl:

Let me know if the new variable name for the string is cringe, I just
settled on that since it mirrored the type of check we run in
select_message_type().

Co-authored-by: san7890 <the@san7890.com>

---
## [ScipioWright/NoitaArchipelago](https://github.com/ScipioWright/NoitaArchipelago)@[8e554ead56...](https://github.com/ScipioWright/NoitaArchipelago/commit/8e554ead56a074f48adbc2626b9aa45870092252)
#### Monday 2023-01-30 05:09:57 by Scipio Wright

Orbs now correctly spawn! All it took was 33 separate orb files, and would probably take a single small block of code for someone more knowledgeable with lua! But maybe Noita is just frustrating like that, idk.

Added some more items to the item list, mostly silly stuff. One less silly thing is adding the map perk to the item list, with the intention that it only gets shuffled in if Toveri is one of the checks. Note to self: make sure it doesn't get shuffled and placed on Toveri.

Added a couple of debug wands, as well as the unlimited spells wand to the debug perks.
One of the debug wands is just a digging wand straight out of Noita's files. The other is a wand pulled from the wiki to travel between parallel worlds -- to make testing stuff regarding them easier.

This is going to be a draft pull request since shops are DEFINITELY broken in this one.

---
## [samzabala/ghost-stories-dub-ipsum](https://github.com/samzabala/ghost-stories-dub-ipsum)@[9113472a0e...](https://github.com/samzabala/ghost-stories-dub-ipsum/commit/9113472a0ea33856a88c1193bce53f5b67f8ce9b)
#### Monday 2023-01-30 06:30:49 by samzabala

1.1 i still have caffeine in my system fuck you all

---
## [TuriansNotBad/azerothcore-wotlk-luaB](https://github.com/TuriansNotBad/azerothcore-wotlk-luaB)@[ef949f9ff0...](https://github.com/TuriansNotBad/azerothcore-wotlk-luaB/commit/ef949f9ff0a89e837c67258d7e199da1706bc438)
#### Monday 2023-01-30 07:09:01 by ICXCNIKA

fix(DB/Locale): deDE fix request items texts #02 (#14615)

Process of translation: only original sources of deDE texts by
researching multiple sources, reverse translation by searching for
related quest items/NPCs and using these names to reconstruct a proper
translation.

This fixes the terms

Coldtooth-Mine (Eisbeißermine), Doomhammer (Schicksalshammer), Fizzle
(Zischel), Fizzledowser (Rutenwünschels), Fizzlebub (Zischelbub),
Burning Blade (Brennende Klinge), Ashenvale (Eschental),
Bloodscalp/s/stamm (Blutskalpe, Blutskalpstamm),
Darkspeartrolle/Darkspears/Darkspearstamm (Dunkelspeere,
Dunkelspeertrolle, -stamm), Moonglade (Mondlichtung), Starblaze
(Sternenschauer), Shadowglen (Laubschattental), Darrowshire (Darroheim),
Booty Bay (Beutebucht), Ratchet (Ratschet), Dizzywig (Flunkerblick),
Hearthglen (Herdweiler), Chillwindspitze (Zugwindspitze), Stormrage
(Sturmgrimm), Stormpike (Sturmlanze/n), Ironforge (Eisenschmiede),
Thunderhorn (Donnerhörner), Steamboil (Kesseldampf), Twilight-Hammer,
-klan (Schattenhammer/Schattenhammerklan), Fathom-Kern (Tiefenkern),
Blackfathom Deeps (Tiefschwarze Grotte), Blackrock-* (Schwarzfels-*),
Hawkwind (Falkenwind), Feathermoon (Mondfeder), Moonrage (Mondzorn),
Firemane (Feuermähne), Searingblade (Sengende Klinge), Ragefireabgrund
(Flammenschlund), Ironbands Areal (Eisenbands Lager), Zandalar
(Zandalari), Southshore (Süderstade)

for quest progress/request text entries for the deDE localisation with
proper casus/declension (these are not proper translated names of
locations/NPCs that have been left over by Blizzard since their language
localisations in TBC in 2006 and onward).

Added missing progress/request text entries for 308, 311, 417, 1644,
1787, 5059, 5060, 5721, 6004, 6023, 6025, 6187, 8042, 8043, 8044, 8046,
8047, 8048, 8050-8079, 8102, 8107, 8108, 8111, 8112, 8113, 8117, 8118,
8142, 8143, 8147, 8183-8195, 8238, 8239, 8240, 8243, 8246, 8860, 9594,
9692, 9707, 10414, 10415, 10919, 11451. (A lot of them are
Zandalari/Zul'Gurub related quests.)

Replaced post-Cataclysm progress/request text entries for 933, 935,
6387, 7383.

Fixed a wrong $R with plain text at progress/request text for 9147.

Added missing female gender equivalent to 6391.

(There are probably more changes in the file that aren't further
explained here as it was hard to keep track of everything. If you think
I made a mistake or have questions please contact me directly.)

<!-- First of all, THANK YOU for your contribution. -->

## Changes Proposed:
-  Fixing a lot in the quest_request_items_locale table.

## Issues Addressed:
<!-- If your fix has a relating issue, link it below -->
- Fixing some of the tasks in
https://github.com/azerothcore/azerothcore-wotlk/issues/14244
Referring to my other two bug reports from CC Github:
- https://github.com/chromiecraft/chromiecraft/issues/4697
- https://github.com/chromiecraft/chromiecraft/issues/4745

## SOURCE:
<!-- If you can, include a source that can strengthen your claim -->
- Read the text on top.

## Tests Performed:
<!-- Does it build without errors? Did you test in-game? What did you
test? On which OS did you test? Describe any other tests performed -->
- Not tested.


## How to Test the Changes:
<!-- Describe in a detailed step-by-step order how to test the changes
-->
All of the changes are to reward texts of quests, can be tested by
completing quests or simply reviewing the changed file.

## Known Issues and TODO List:
<!-- Is there anything else left to do after this PR? -->

- [ ]
- [ ]

<!-- If you intend to contribute repeatedly to our project, it is a good
idea to join our discord channel. We set ranks for our contributors and
give them access to special resources or knowledge:
https://discord.com/invite/DasJqPba)
Do not remove the instructions below about testing, they will help users
to test your PR -->
## How to Test AzerothCore PRs
 
When a PR is ready to be tested, it will be marked as **[WAITING TO BE
TESTED]**.

You can help by testing PRs and writing your feedback here on the PR's
page on GitHub. Follow the instructions here:

http://www.azerothcore.org/wiki/How-to-test-a-PR

**REMEMBER**: when testing a PR that changes something **generic** (i.e.
a part of code that handles more than one specific thing), the tester
should not only check that the PR does its job (e.g. fixing spell XXX)
but **especially** check that the PR does not cause any regression (i.e.
introducing new bugs).

**For example**: if a PR fixes spell X by changing a part of code that
handles spells X, Y, and Z, we should not only test X, but **we should
test Y and Z as well**.

---
## [avboy1337/proxychains-ng](https://github.com/avboy1337/proxychains-ng)@[7fe8139496...](https://github.com/avboy1337/proxychains-ng/commit/7fe813949644b115b0127279517dc7c0ee2d63b9)
#### Monday 2023-01-30 07:17:34 by rofl0r

experimental new feature: proxy_dns_daemon

since many users complain about issues with modern, ultracomplex
clusterfuck software such as chromium, nodejs, etc, i've reconsidered
one of my original ideas how to implement remote dns lookup support.
instead of having a background thread serving requests via a pipe,
the user manually starts a background daemon process before running
proxychains, and the two processes then communicate via UDP.
this requires much less hacks (like hooking of close() to prevent
pipes from getting closed) and doesn't need to call any async-signal
unsafe code like malloc(). this means it should be much more compatible
than the previous method, however it's not as practical and slightly
slower.

it's recommended that the proxychains4-daemon runs on localhost, and
if you use proxychains-ng a lot you might want to set ip up as a service
that starts on boot. a single proxychains4-daemon should theoretically
be able to serve many parallel proxychains4 instances, but this has not
yet been tested so far. it's also possible to run the daemon on other
computers, even over internet, but currently there is no error-checking/
timeout code at all; that means the UDP connection needs to be very
stable.

the library code used for the daemon sources are from my projects
libulz[0] and htab[1], and the server code is loosely based on
microsocks[2]. their licenses are all compatible with the GPL.
if not otherwise mentioned, they're released for this purpose under
the standard proxychains-ng license (see COPYING).

[0]: https://github.com/rofl0r/libulz
[1]: https://github.com/rofl0r/htab
[2]: https://github.com/rofl0r/microsocks

---
## [landonb/home-fries](https://github.com/landonb/home-fries)@[74935ea22f...](https://github.com/landonb/home-fries/commit/74935ea22f2cd8f4caf4ff5a49b02dd612d5dcbe)
#### Monday 2023-01-30 07:24:07 by landonb

UX: Enhance: Reinvigorate startup's Bash version messaging.

- First, Return to WAD: Add Homebrew-awareness when deciding to print
  Bash version.

  - The Bash version message on Homefries startup was meant to alert
    the user when they were running a custom Bash version.

    But on macOS, it doesn't recognize the path as Homebrew Bash, so
    Homefries always prints the version message. But that's not the
    point of the message.

    - I added this check years ago, when I was building Bash v4 for
      some very particular reason because whatever Linux Mint I was
      on did not support some new feature or bugfix I needed (if I
      had to pick, I'd guess it was a bugfix, because I probably
      wanted a little nagging so I'd remember to eventually return
      to the distro version, so I wouldn't be responsible for
      periodically updating and rebuilding Bash).

    So now we're back to roots, print Bash version when custom Bash.

- Next, I decided to add back a similar version message, but briefer.

  - See the new `HOMEFRIES_HELLO`, which I'm defaulting enabled, to
    see how it feels. (I don't mind a little ho on terminal startup,
    usually. I suppose for a vanilla terminal, sure, don't say a
    thing, but a --noprofile --norc is meant to be a quick start,
    something that just does its job, sunglasses on, looking straight
    ahead, doesn't interact with me. But for Homefries, especially on
    macOS where it takes a dozen seconds to boot (lately), let's be
    friendly. The user already waited so long, let's say Hi. (And
    while we're at it, here's the Bash version; and here's how long
    it took Homefries to load.))

    - (Per last metric, I like knowing how long boot takes because
       when I got an M1 Mac recently (Oct, 2022), Homefries took a
       whopping 120 secs. to load. 4 months later (recently), it's
       taking 12 secs. [While I found and fixed a few issues, most
       of the gain was likely Apple and/or Homebrew fixing issues
       upstream (I assume; or magic)]. (For posterity, on Linux Mint,
       Homefries starts in under a second. Go figure.))

---
## [SyncIt21/The-TG-Station-Fork](https://github.com/SyncIt21/The-TG-Station-Fork)@[ae08395328...](https://github.com/SyncIt21/The-TG-Station-Fork/commit/ae08395328672ee40c5abb7f2bd1452bb932d6d4)
#### Monday 2023-01-30 08:10:06 by san7890

Syndicate Bomb Core Payloads Can Only Be Triggered via the Bomb (#72986)

## About The Pull Request

Basically, you can't extract the bomb core, slap a 10-second c4 on it/on
the shell/and run off having triggered an incredibly powerful explosion.
This is accomplished by having the syndicate bomb override ex_act (it
will be deleted if the explosion goes off), as well as the payload
itself being subtyped into something resistant to bombs and burning.

In-universe, this is described as the shell being quite resistant to
forms of external explosive force- but if any explosive force comes from
within the bomb's shell: kabloom. The bombcore itself has been
redesigned (in a rare moment of non-ineptude) by Donk Co., who has
redesigned the bomb core payload from the ground up- meaning that it can
only be detonated electronically by an impulse from the bomb machinery.
Cutting the wrong wire and attempting to get rid of the bomb by hitting
it with an axe or something will still cause it to blow up, but you know
how those things can be.
## Why It's Good For The Game

I feel like the point of the syndicate bomb is to be a threat for the
crew to match up against. I want a clown in bomb squad gear to head out
to the site and sweat trying to figure out which wire it is, until....
KA-BLHONK: red mist. Or, I want some "helpful" assistant to interrupt
someone's session by going "I KNOW WHAT WIRE IT IS", and having those
odds of either blowing everyone around them up or actually saving the
day.

Being able to detonate something that was balanced and designed to have
_at least_ one minute and a half in **10 SECONDS** is just so injurious
to the game. You can buy a shitload of these bombs, extract the cores,
slap c4 on it and go around the station doling out some serious
explosions. You can run into medbay, wrench it down, slap a c4 on it AND
NO ONE CAN DO ANYTHING ABOUT IT! They can't cut wires, they can't figure
it out to save the day, all they can do is run. Running from danger is
fine and acceptable, but it's just completely stacked against the crew
in a way that I feel needs to be rectified somehow.

I like the idea of purposefully fucking with the wires on the spot so
you sacrificially kill everyone, that feels quite fair to me. I just
simply don't like the fact that you can waltz around the station
punching huge gaps in the hull (remember, putting c4 on the bomb core
itself would cause it to go kabloom) with nearly nothing as far as risk.
It's way too rewarding for something very easy to accomplish (there's a
reason why it's 90 seconds- it's not meant to be easy to accomplish).

This doesn't affect base bombcore behavior, just the explodey ones that
come standard in syndicate bombs.
## Changelog
:cl:
balance: After an unfortunate event occuring when some nuclear
operatives took the ship to a Fireworks Store, the Syndicate have
re-engineered their bomb cores to only explode when electronically
triggered by the bomb shell itself. The payload inside a standard
syndicate bomb can not be exploded with another explosion, you must keep
it in the bomb machinery for it to actually do some explodey stuff.
/:cl:

---
## [JackiePengp/hi-there](https://github.com/JackiePengp/hi-there)@[b9a6306b3d...](https://github.com/JackiePengp/hi-there/commit/b9a6306b3d6471d9f46cb2f244d9431d2285f926)
#### Monday 2023-01-30 08:28:13 by Pengyang(jackie)

Update README.md

# hi-there
😆Hi, I’m pengyang(Jackie), currently am working as operation role at Affine. 
🤔Before joining Affine, I'm a guy with around 3years experiences in product operation within tiktok, which's mainly focusing on NLP/CV model training, deployment and successfully delivery.
📧I sometimes publish info/announcements regarding to Affine via our social media channel.
🤖I’m looking forward to having more active engagements with anyone who may find Affine cool and intriguing to use. Thus, any problems, bugs, requirements, painpoints about Affine that beset you are always welcome to tell.
🪐Anyone interested in Affine and wanting to do something to bring about some changes to the world is welcome to join Affine's ambassador plan(feel free to let know)

---
## [grimuars/LycanitesMobs](https://github.com/grimuars/LycanitesMobs)@[7689515c14...](https://github.com/grimuars/LycanitesMobs/commit/7689515c14787c3e06e366e36acccd8cc7f4bc2d)
#### Monday 2023-01-30 10:22:24 by Richard Nicholson

Update 1.10.9.6: Blood!

Bug Fix: Extended world properties are now world independent, the global
world save data was being incorrectly used for each world which would
mess up the events system when running in multiple dimensions.

Balancing: The Death spawn type (Phantom Spawner) will now only be able
to spawn mobs at night when in the overworld.

Balancing: Grue can now only teleport to their target if it is in a dim
or dark light level, this means that if you stand by a torch when
fighting a Grue, it will no longer by able to teleport behind you, it
can still however fly over to you.

Config Change: The Underground Spawn Type (Spawns Chupacabras) can now
have the maximum Y level set via the config on a per dimension basis,
this config entry also includes a default Y level set for the Twilight
Forest dimension.

Tweaks: The Asmodi Demon Mob has been renamed to Astaroth.

Tweaks: Rare Mobs (such as the Celestial Geonach) will now always be
immune to suffocation.

---
## [edwarda21/VA_prvni](https://github.com/edwarda21/VA_prvni)@[08642234ff...](https://github.com/edwarda21/VA_prvni/commit/08642234ff373cc871e3be00905e80728ae56e03)
#### Monday 2023-01-30 10:42:52 by edwarda21

tried some things out for the leaderboard but they are not working and now I am sad because my girlfriend is depressed and I dont know what to do because the feeling that I know she is suffering and I cant do anything about it is eating me up inside and I just want to cry and do nothing but I cant, I cant show people I am weak and vulnerable...

---
## [HaraldKorneliussen/Et-Futurum-Requiem](https://github.com/HaraldKorneliussen/Et-Futurum-Requiem)@[dc506a9fe1...](https://github.com/HaraldKorneliussen/Et-Futurum-Requiem/commit/dc506a9fe1c1448eaec73af46604a68fc52af553)
#### Monday 2023-01-30 11:14:11 by Roadhog360

Thanks Eclipse for not saving this

Seriously getting sick of Eclipse's "save undo" horse shit
Might switch to IntelliJ because I keep saving in Eclipse only to go back to see it DIDN"T save and I have to save the same fucking changes again for them to apply and make these stupid micro-commits to push stuff that should have already been fucking pushed

---
## [bensimner/starling-tool](https://github.com/bensimner/starling-tool)@[521d8db54b...](https://github.com/bensimner/starling-tool/commit/521d8db54b1b7dc5f1cc925745e3f9a7fe7bf738)
#### Monday 2023-01-30 11:52:45 by Matt Windsor

Allow variables of the same type and class to be declared together.

Instead of:

shared int x;
shared int y;

one can now write

shared int x, y;

I thought this would save some real estate for the PLDI paper, but
in fact I'm a stupid: the ARC doesn't have any shared variables.
So yeah, this was fairly pointless and wasted time that could have
been spent elsewhere.  Damn my time management skills.

Maybe it'll help with the other examples?

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[35295d3153...](https://github.com/odoo-dev/odoo/commit/35295d3153c174846f572b537d6e6b33f700eecc)
#### Monday 2023-01-30 13:41:45 by Arnold Moyaux

[FIX] stock,purchase,mrp: accumulative security days

Usecase to reproduce:
- Set the warehouse as 3 steps receipt
- Put a security delay of 3 days for purchase
- Set a product with a vendor and 1 days as LT
- Replenish with the orderpoint

You expect to have a schedule date for tomorrow that contains all the
product needed in the incoming 4 days.

Currenly the internal transfer from QC -> Stock is for tomorrow (ok).
The transfer from Inpur -> QC is plan for 2 days in the past. (not ok)
The PO date is plan for 5 days in the past. (not ok)

It happens because the system check at each `stock.rule` application if
purchase is part of the route. If it's then it applies the security lead
time. It's a mistake because we should apply it only the first time.

To fix it we directly set it when the orderpoint run and not during
`stock.move` creation.
However for MTO it's not that easy. We don't want to deliver too
early the customer. So we keep applying the delay during the
`stock.move` creation but only when it goes under the warehouse stock
location.

---
## [SOVIET-ANDROID/kernel_xiaomi_raphael](https://github.com/SOVIET-ANDROID/kernel_xiaomi_raphael)@[3b068dd51a...](https://github.com/SOVIET-ANDROID/kernel_xiaomi_raphael/commit/3b068dd51aeb4fc5b5cc5b2934d595cb48b25fba)
#### Monday 2023-01-30 13:44:59 by kondors1995

raphael_defconfig: Revert FBEv2 defconfig changes

To maiteiners who still use FBEv1 Fuck you in particular

https://www.youtube.com/watch?v=Ok3xVYz8Ibs

---
## [DTCurrie/viam-rdk](https://github.com/DTCurrie/viam-rdk)@[66cdb282a1...](https://github.com/DTCurrie/viam-rdk/commit/66cdb282a1ab2130f9bfd9d3fda12feac5298c9f)
#### Monday 2023-01-30 14:08:27 by Alan Davidson

[RSDK-923] Make GPS-RTK code more robust, remove bad test (#1679)

Changes include:
- Migrate go statements to `utils.PanicCapturingGo()`
- Don't start the background goroutine unless the rest of startup succeeds (to prevent leaking goroutines)
- Lock the mutex whenever you read or write any data that is also read/written from a different goroutine (this was the actual cause of the race conditions!)
- Remove the test that sometimes fails due to a bug in third-party code. It sucks that it sometimes fails, but all the problems are down in the bowels of https://github.com/de-bkg/gognss, and not in code we own.

Things I kinda wanted to change but didn't: 
 - `RTKMovementSensor.GetStream()` is nearly identical to `ntripCorrectionSource.GetStream()`, and the only times you call the RTK version, you always pass in the same state stored in an ntrip object. Unfortunately, it's a _different_ ntrip object defined in the same file as `ntripCorrectionSource`. Should the function be moved to that class instead, or removed entirely? I dunno. Something in here is redundant, but I couldn't remove the duplication without thinking a lot more.

I ran the tests 1,000 times: no failures. It's possible I'm being overly cautious with the mutex, and if you have specific ones you want me to remove, I'm happy to do so. It's possible I'm writing non-idiomatic Go code, and I'm happy to rewrite this whole thing if you have a different style I should match.

---
## [AshfordGraye/ProjectRPG](https://github.com/AshfordGraye/ProjectRPG)@[9fc7ba666e...](https://github.com/AshfordGraye/ProjectRPG/commit/9fc7ba666ea976d6e6a86edc2120ac65a11e55bb)
#### Monday 2023-01-30 14:55:53 by Ash

A learning experience I'm sure all programmers go through...

After a machine restore and cloning the repo back from GitHub it became apparent that all local files previously present but assigned to .gitignore had been lost - including the OriginalAppBuild folder which included the original application from which this unfinished one was built. 

Well, obviously - I told it to ignore them didn't I...

The absolute kicker? I deleted the backup while cleaning up my documents folder on autopilot before restoring my machine...

A classic example of being reminded the hard way that computers do EXACTLY what you tell them to and that having backups are only good if you keep them somewhere you wont touch them by mistake.

The only upshots here are that my written work was in a totally separate location, and the actual code itself is of course exactly how I Ieft it - Praise the Omnissiah.

This commit recreates a documents folder and adds the base files for some documents I can recreate easily like the .drawio files. Added the assignment brief and some files for code snips and pseudocode writing for the assignment itself. The OriginalAppBuild is completely gone - there's no way I can reverse engineer what the code has now turned into back into what it was. Be like turning an omelette back into eggs.

---
## [BuprenorphineKid/GoLabs](https://github.com/BuprenorphineKid/GoLabs)@[54d9f3332b...](https://github.com/BuprenorphineKid/GoLabs/commit/54d9f3332b8a37240944f5d64454e2fdece4ca54)
#### Monday 2023-01-30 14:59:43 by Alek Stewart

omg... im a fucking idiot lmfao: i forgot to edit paths in the scripts after nesting one level deeper. that was it.

---
## [irulanCorrino/audacity-2-4-2](https://github.com/irulanCorrino/audacity-2-4-2)@[4d4ba2c716...](https://github.com/irulanCorrino/audacity-2-4-2/commit/4d4ba2c716532c17e1c3b6fb6c99ef8dd87dc889)
#### Monday 2023-01-30 15:52:16 by sov thade tage em ereb

oh God i`m so lucky! truant

i am insanely happy i had left that corrupted postsoviet institute back then in my eighteen!
or i would be forced to work with idiotic Borland stuff and Pascal 5.0 & C++...
and fucking 'transparent tatar government' ...RIP! fuck you hypocrites!

---
## [Msiusko/web3privacy](https://github.com/Msiusko/web3privacy)@[3b8c3a45d0...](https://github.com/Msiusko/web3privacy/commit/3b8c3a45d068b888c3c862ce8dfcdaa4d11ee3b6)
#### Monday 2023-01-30 16:37:04 by huxian333

Update Readme.md

Heyho, I've proposed some changes - but no mayor modifications.
1) I generally gave a fresh look to the copy to make it a bit crispier (and corrected some typos, grammar etc)
2) this was a bit unorthodox from me i know but: I've kind of got rid of most *web3* term from the text itself. Since the whole platform is named like this, and the brand is this too - I felt it's redundant and exclusive. You can see changes everywhere like *new web* or *privacy industry*.  in this spirit I've also added a new PR value point (non-web3 literate ppl - but thats like the only place where I felt that we need to specify benefits for web3 people. I've tried to add wider angles to the copy wherever I felt it should be there.
3) Id like to propose for you to consider adding pnproxy for the team - as a somewhat lunarish privacy dao with a cool github and some education articles from around nym, etc etc. I've put it next to you at research and to the community role. I think this would be a good match and kinda in the alley of our previous cooperation model. lmk
4) on the images I could not propose new stuff but: 
"What's broken, and could be cured?"
4.1) No transparent scoring of privacy services & products
4.3) Lack of independent, gated and community reviwed research articles"
5) Components of healing potion (not necessary, but would be cool to refer to online gaming here imo)

last - why no BTC donation address? :) it would decrease chances?

---
## [PixelExperience-Devices/device_samsung_sm7125-common](https://github.com/PixelExperience-Devices/device_samsung_sm7125-common)@[9900eff140...](https://github.com/PixelExperience-Devices/device_samsung_sm7125-common/commit/9900eff14024a0a7f45a687102d60ea01bb14699)
#### Monday 2023-01-30 16:55:01 by Ruchit

sm7125: (note to self) dont pick this ye dumb idiot its only for wip branch so you can test shit better k bye

---
## [Cheaterman/calendar_widget](https://github.com/Cheaterman/calendar_widget)@[6a3552f36e...](https://github.com/Cheaterman/calendar_widget/commit/6a3552f36e71db15e212d0d456470dbaf1316c5d)
#### Monday 2023-01-30 17:53:20 by The Cheaterman

Fix invalid active date when changing month... genuine WTF

At this point I really think it would have been faster to just
reimplement the whole fucking thing - you guys have no idea how much
time I had to waste on this shit already.

---
## [RalphHightower/RalphHightower](https://github.com/RalphHightower/RalphHightower)@[288e8e710b...](https://github.com/RalphHightower/RalphHightower/commit/288e8e710b7d15fdc51c9d5dea5a557a8e21875f)
#### Monday 2023-01-30 18:17:35 by Ralph Hightower

docs: DEC VAX conversation (closes #6)

## DEC VAX Family

| *"RalphHightower"* / ChatGPT |
|----|
|*"Greetings Assistant. "*|
|Hello! How can I help you today?
|*"Are you familiar with the Digital Equipment Corporation VAX 11/780?"*|
|Yes, I am familiar with the Digital Equipment Corporation (DEC) VAX 11/780. It was a high-end computer system based on the VAX architecture, which was introduced by DEC in the late 1970s. The VAX 11/780 was the first model in the VAX 11 series, and it was introduced in 1977. It was known for its high performance and scalability, and it was widely used in scientific and engineering applications, as well as in the commercial and government sectors. The VAX 11/780 was also the first VAX model to use the MicroVAX chipset, which allowed for the creation of smaller VAX systems.|
|*"Can you provide me some information on the instruction set?"*|
|The VAX instruction set is a complex instruction set computer (CISC) instruction set, which means that it has a large number of instructions with a wide range of capabilities.|
|It was designed to provide a high level of compatibility with the PDP-11, a popular minicomputer also produced by DEC, and to support high-level languages such as FORTRAN, COBOL, and PL/I.|
|The VAX instruction set includes instructions for basic data manipulation, such as load, store, move, and compare; instructions for arithmetic operations, such as add, subtract, and multiply; and instructions for control flow, such as branch, jump, and call. It also includes a variety of specialized instructions, such as instructions for floating-point operations, bit manipulation, and string operations.|
|The VAX also featured a large number of addressing modes. It had eight general-purpose registers and eight floating-point registers. It also had a large memory addressing capability of up to 4GB.|
VAX also had a feature called "Virtual Memory" which allowed the system to treat the physical memory as a virtual memory space which is much larger than the physical memory installed in the system. This feature was an important factor in the success of the VAX architecture, as it allowed programs to run on systems with limited physical memory.|
|*"What operating systems could run on the VAX?"*|
|The VAX 11/780 and other VAX systems were compatible with a variety of operating systems, including:<br>• VMS (Virtual Memory System): This was the primary operating system for the VAX, developed and sold by DEC. VMS was a multi-user, multitasking operating system that supported a wide range of features, such as virtual memory, security, and network connectivity. It was widely used in commercial and government environments.<br>• Ultrix: This was a version of the Unix operating system developed by DEC for the VAX and other systems. Ultrix was based on the BSD variant of Unix and was compatible with VMS. It was commonly used in scientific and engineering environments.<br>• RSX-11: This was an older operating system developed by DEC for the PDP-11, but it was also compatible with the VAX. RSX-11 was a single-user, single-tasking operating system that was widely used in industrial and process control applications.<br>• OpenVMS: This is a rebranded version of VMS which is developed and sold by VMS Software Inc.(VSI) after DEC's bankruptcy. It is still being developed and supported by VSI today.|
|Additionally, third-party operating systems were also available for the VAX, such as 4.3BSD UNIX, Xenix and others, but they were less popular than the ones mentioned above.|
|*"Up to your knowledge base, do you know if there are still any vaxes that are still in use?"*|
|As of my knowledge cutoff in 2021, it is unlikely that there are still many VAX systems in active use. The VAX architecture was phased out in the 1990s as newer systems based on other architectures, such as the Alpha and the Intel x86, became more popular.|
|However, it is possible that some organizations may still be using older VAX systems for legacy applications that cannot be easily ported to newer systems. And also some companies and individuals still use OpenVMS on VAX and Alpha platforms for mission critical applications. Some enthusiasts also keep VAX systems running as a hobby.|
|It should be noted that OpenVMS, which is based on VAX architecture, is still being developed and supported by VMS Software Inc (VSI), and some companies still use it for their critical applications, this means that some VAX hardware are still being used and maintained to run OpenVMS.|
|*"I have a VAXStation II/GPX at home; it's just the bare box, with the circuit boards and tape drive. What peripherals do I need to get it up and running and connected to my home network? Monitor? What type of monitor? It has a DB-9 Ethernet connection. "*|
|To get your VAXStation II/GPX up and running, you will need a few additional peripherals:<br>• A monitor: The VAXStation II/GPX uses a standard VGA connector, so you will need a VGA-compatible monitor. Any VGA monitor will work, but you may need a VGA-to-DB15 adapter if the monitor does not have a DB15 connector.<br>• A keyboard: The VAXStation II/GPX uses a standard PS/2 keyboard connector, so you will need a PS/2 keyboard.<br>• A mouse: The VAXStation II/GPX uses a serial mouse, so you will need a serial mouse or a PS/2 mouse with a serial to PS/2 converter<br>• A power cord: You will need a power cord to connect the VAXStation II/GPX to a power source.<br>• A Ethernet cable: You will need a Ethernet cable to connect the VAXStation II-RT/GPX to your home network.<br>• A boot media: You will need a boot media to boot the VAXStation II/GPX, it could be a tape drive, a floppy disk drive, or a hard drive.| 
|It's also worth noting that the VAXStation II/GPX is an older computer, so it may be difficult to find compatible peripherals. You may need to look for used or refurbished peripherals to get everything you need.|
|Additionally, you will need to have an operating system installed on the VAXStation II/GPX. If you don't have any, you can look for OpenVMS media or install files online, or you can contact VMS Software Inc (VSI) for assistance.|
|*"I'm not going to install VMS. I don’t feel like learning a new OS. An OS where I can use my knowledge of Unix and Linux would be ideal."*| 
|If you're not interested in learning VMS and you would prefer to use an operating system that is more similar to Unix or Linux, you can look into installing one of the following operating systems on your VAXStation II/GPX:<br>• NetBSD: This is a free and open-source operating system that is based on the BSD variant of Unix. NetBSD has been ported to the VAX architecture and can run on the VAXStation II/GPX.<br>• OpenBSD: This is another free and open-source operating system that is based on the BSD variant of Unix. OpenBSD has also been ported to the VAX architecture and can run on the VAXStation II/GPX.<br>• Linux: Linux is a free and open-source operating system that is based on Unix. Linux has been ported to the VAX architecture, but it is less common than the BSD operating systems.|
|Keep in mind that those are not the only options, and the support for VAX architecture could be limited and hard to find, also those operating systems would not be able to take advantage of the specific hardware features of the VAXstation II/GPX. Also, it could be difficult to find the installation media and support for those operating systems on VAX hardware.|
|It's also worth noting that these operating systems were not originally designed to run on the VAX architecture, so performance and compatibility may be limited compared to VMS.|
|Please also be aware that installing a new operating system will erase the original one, and the process of installing it could be complicated and time-consuming, specially if you are not familiar with the VAX hardware|
|*"It is okay to erase the operating system since I don’t have the login credentials for whatever is installed. "*|
|If you don't have the login credentials for the operating system that is currently installed on your VAXStation II/GPX, then you will not be able to access the system and you may need to install a new operating system.|
|As I mentioned earlier, installing an operating system on a VAXStation II/GPX can be complicated and time-consuming, especially if you are not familiar with the VAX hardware.|
|Here are the general steps you will need to follow in order to install a new operating system on your VAXStation II/GPX:|
|• Obtain the installation media for the operating system you wish to install. This could be a set of installation floppy disks or a bootable CD-ROM, depending on the operating system.|
|• Connect the VAXStation II/GPX to a monitor, keyboard, and mouse.|
|• Connect the VAXStation II/GPX to a power source.|
|• Insert the installation media into the appropriate drive (floppy drive or CD-ROM drive).|
|• Turn on the VAXStation II/GPX and follow the instructions provided by the operating system installation program. |
|• This will typically involve formatting the hard drive, partitioning the hard drive, and copying the operating system files to the hard drive.|
|• Configure the operating system settings, such as the network settings, and create user accounts.|
|• Install any additional software or applications that you need.|
|Please note that you will also need to have some knowledge of the VAX architecture and the specific hardware of the VAXStation II/GPX in order to perform the installation process and to troubleshoot any issues that may arise.|
|It's also important to note that once the new operating system is installed, the original operating system and all the data on the VAXStation II/GPX will be lost.| 
|If you are not comfortable with the process, it would be better to seek help from someone who is more familiar with VAX hardware and operating systems.|
|*"I am not familiar with the hardware, but I have decades of experience with Unix that has been leveraged in using Linux."*|
|If you have decades of experience with Unix and have leveraged that experience to work with Linux, then you may be able to use that knowledge to help with the installation of a Unix-like operating system on your VAXStation II/GPX. However, please be aware that there are significant differences between VAX architecture and the more common architectures that Linux and Unix are running on, and also the process of installing a new operating system on a VAXStation II/GPX can be complicated, specially if you are not familiar with the VAX hardware.|
|Here are a few things you should keep in mind when installing a Unix-like operating system on a VAXStation II/GPX:|
|The VAX architecture is a unique architecture that is not commonly used in modern computers. Some of the commands and utilities that you are used to using on Linux or Unix systems may not be available or may work differently on a VAXStation II/GPX.|
|The process of installing a new operating system on a VAXStation II/GPX can be complicated, and it may require you to use specialized software and utilities that are not commonly used on other architectures.|
|The support for VAX architecture could be limited and hard to find, also those operating systems would not be able to take advantage of the specific hardware features of the VAXstation II/GPX.|
|The process of installing a new operating system on a VAXStation II/GPX can be complicated, and it may require you to use specialized software and utilities that are not commonly used on other architectures.|
|Given the above, it's important to have a clear understanding of the limitations and challenges that may be involved before you decide to install a new operating system on your VAXStation II/GPX.|
|It would be better if you can find support from someone who is more familiar with VAX hardware and operating systems. They can guide you through the process, and help you troubleshoot any issues that may arise.|
|*"I don't think that will be any problem, other than one of the key circuit boards not working. If so, then it would could be turned into use as an end table. A friend and former coworker rescued it from being tossed into a dumpster and a technology company failed, closed up shop and shutdown."*|
|If one of the key circuit boards is not working, it could make it difficult or impossible to get your VAXStation II/GPX up and running. In that case, your best option might be to use it as an end table, as you mentioned.|
|However, before giving up on it, you may want to check with other VAX enthusiasts or computer repair professionals who may have experience working with VAX hardware. They may be able to help you diagnose and repair the problem, and get your VAXStation II/GPX up and running again.| 
|If you decide to go ahead with installing a new operating system, you will need to get some peripherals to get it up and running. You will need a monitor, keyboard, and mouse to interact with the VAXStation II/GPX. It's best to use a monitor that supports the resolution and refresh rate of the VAXStation II/GPX. For the keyboard and mouse, you can use any standard PS/2 or USB keyboard and mouse.|
|For connecting to a network, you can use the built-in DB-9 Ethernet port. You will need a suitable Ethernet cable and a router or switch to connect the VAXStation II/GPX to your home network.|
|Keep in mind that even if you manage to install a new operating system on your VAXStation II/GPX, it may not be able to take advantage of the specific hardware features of the VAXstation II/GPX. |||
|Additionally, performance may not be as good as you expect, as the VAX architecture is not optimized for modern operating systems and applications.|
|In summary, if you have the knowledge and resources to troubleshoot and repair the VAXStation II/GPX and install a new operating system, it is worth the effort but keep in mind that it will be limited by the hardware and software support available.|
|*"Wow! You have a great sense of humor. LOL! I will need an Ethernet transceiver for twisted-pair with a DB-9 connector. "*|
|I'm glad you found my response helpful, but I am an AI model and I do not have emotions, therefore I don't have the ability to have a sense of humor.|
|Regarding the Ethernet transceiver you need, a twisted-pair transceiver with a DB-9 connector would be appropriate for connecting your VAXStation II/GPX to a network. This type of transceiver would convert the signal from the VAXStation II/GPX's DB-9 connector to a signal that can be transmitted over a twisted-pair cable, such as a Category 5 (Cat 5) or Category 6 (Cat 6) Ethernet cable. The transceiver would also convert the signal back to a format that the VAXStation II/GPX can understand, allowing it to communicate with other devices on the network.|
|Keep in mind that you might have to use an adapter or a converter to connect the transceiver to the twisted-pair cable.|
|Also, make sure that the operating system you choose to install on the VAXStation II/GPX has support for your specific transceiver and that the version of the drivers available are compatible with the version of the operating system that you're installing.|
|*"Do you know where I can buy a transceiver with DB-9 for cat 6? I checked BlackBox and I didn't find any."*|
|It may be difficult to find a new transceiver with a DB-9 connector specifically for Cat 6 Ethernet cable. The VAXStation II/GPX was released in 1977 and its hardware is quite old and no longer in production, so it may be difficult to find new peripherals that are compatible with it.|
|You can check with vintage computer or VAX enthusiasts to see if they have any DB-9 transceivers available. They may have older equipment that they are no longer using and may be willing to sell or give you.|
|You may also be able to find used transceivers with DB-9 connectors on online marketplaces such as eBay or Amazon. Keep in mind that these may be used and may not be in perfect working condition.|
|Another option might be to try to find an adapter or converter that can be used to connect a modern Ethernet transceiver to the VAXStation II/GPX's DB-9 connector. This would allow you to use a more widely available transceiver and cable, but it would require additional parts and may not be as reliable as a dedicated transceiver.|
|It's worth noting that many VAX enthusiasts have made their own solutions to this problem, as this is not an uncommon issue. You may want to check with VAX user groups and forums for more information on how to connect your VAXStation II/GPX to a modern network.|
|*"Thank you. It was great talking with you about vintage computers. "*|
|You're welcome! I'm glad I could help. It's always interesting to learn about the history of technology and how it has evolved over time. If you have any other questions regarding your VAXStation II/GPX or other vintage computers, feel free to ask.|
|*"Thank you. Bye for now."*|
|You're welcome, have a great day! Don't hesitate to reach out if you have any other questions in the future.|

---
## [odoo/odoo](https://github.com/odoo/odoo)@[39d51d26e5...](https://github.com/odoo/odoo/commit/39d51d26e54f208e44598dc435b8916eb5efc944)
#### Monday 2023-01-30 18:37:12 by Romain Derie

[FIX] website: redirect to case insensitive URL if not exact match

Before this commit, if a link to a page was not correct because of a
case mismatch, it would simply land on a 404 page.
While it's correct, as URL are case sensitive, it leads to a few bad UX
flow at the admin/editor level:
- Create a link in your page (on a text or a button eg), type an URL
  which does not exists (to create it after) like /Page
- Click on the link/button you just made, you are redirected to /Page
  which display a 404 with the "Create page" option (correct)
- When you click on that button, it will actually create a page with
  /page URL, leading to a mismatch between the URL you created and the
  page URL.
  Your link/button will still lead to a 404 URL as it points to /Page.

Since it's just a fallback when an exact URL match is not found, it
should not break anything and should not have bad impact at any level
(seo/speed etc).
Indeed:
- It's done through a 302 redirect
- `_serve_page()` is already a fallback case, so it will only make
  the `website.redirect` and 404 cases a bit slower due to the extra
  search query.

The only possible scenario seems to be if the user (mind the uppercase):
- Created a /Page page
- Created a redirect from /page to /another-page

In this case, /page won't land on /another-page but on /Page.
This flow seems unlikely and is not actually wrong either way.
At least, it certainly is less important than ensuring a case
insensitive fallback.

Finally, note that another solution would have been to either:
- Force page URL to lower case.
  -> This is not stable friendly, people might be relying on this to
     create pages with different casing:
     `/Batman-VII-The-Dark-Knight-Whatevers`, while not recommended,
     doesn't sounds idiot.
     On top of not being stable friendly, we probably want to keep
     offering this possibility
- Redirect all URLs to lowercase endpoints.
  -> This is obviously not stable and not Odoo's jobs. It should be
     something decided by the sysadmin and done at nginx (etc) level.

task-3110294
opw-3104030

---
## [Zytolg/tgstation](https://github.com/Zytolg/tgstation)@[10a344bde0...](https://github.com/Zytolg/tgstation/commit/10a344bde0d48fb250dcb7a9eb4a1e98b9bb6df5)
#### Monday 2023-01-30 18:56:20 by Time-Green

External Organ Rework: new bodypart_overlay system (#72734)

Bodypart overlays are now drawn by the new /datum/bodypart_overlay
datum.

External organs no longer draw anything and instead add a special
/datum/bodypart_overlay/mutant to the bodypart, which draws everything

Makes it way easier to add custom overlays to limbs, since the whole
system is now modularized and external organs are just one
implementation of it

I haven't moved anything but external organs to this new system, I'll
move eyes, bodymarkings, hair, lipstick etc to this later

New pipeline is as follows:
- External organ added to limb
- External organ adds /datum/bodypart_overlay/mutant to limb to
bodypart_overlays
- Limb updates its icon, looks for all /datum/bodypart_overlay in
bodypart_overlays
- Very cool new overlay on your limb!

closes #71820

:cl:
refactor: External organs have been near-completely refactored. 
admin: Admin-spawned external organs will load with a random icon and
color
fix: fixes angel wings not working for non-humans (it was so fucking
broken)
fix: fixes external organs being invisible if they werent initialized
with a human
/:cl:

### Why this is good for the game
External organs are cool but are pretty limited in some ways. Making
stuff like synthetic organs is kinda fucked. I tried and it was dogshit.
Now you can just give an icon state and icon and you're good (using
/datum/bodypart_accessory/simple)

Stuff like eyes, cat ears and hair seem like good choices for extorgans,
but don't quite work for it because their icons work a lot differently.
This solves for it completely since any organ (or object or whatever)
can add it's own icon to a bodypart.

Want to add an iron plate to someones head? Go ahead. Want a heart to
stick out of someones chest? No problem.

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[f1b769fa8a...](https://github.com/mrakgr/The-Spiral-Language/commit/f1b769fa8a05cfaf18923ada63d7009d0ef7a973)
#### Monday 2023-01-30 19:08:35 by Marko Grdinić

"1:25pm. It seems the verification mail for Puzo was in Spam. Thunderbird doesn't check for those automatically so I missed them. I did a search for Audiate and it does not have it. Yeah, I give. Maybe some site has it, but I can't spend all my time excavating the warez sites. Maybe something will come up in the future.

At any rate, let me finish breakfast and I will write the review.

1:50pm. Let me chill a bit first and then I will start the review. After that I'll start working on the setting up video.

2:30pm. Let me start. It is time to start the next part of the series.

Just start the recording.

2:55pm. I did the recording, but it was pretty awful.

3pm. Ah, I was supposed to do the monthly review? Agh.

Nevermind, I need to do a retake anyway. Too many surprising things happened this time. It is good to try it once and then do it once again.

///

Long time since I last did this review. I've done plenty of improvements on [Spiral](https://github.com/mrakgr/The-Spiral-Language) like better pattern matching compilation as well as fixing bugs in the type inferencer and the ref counter in the C backend. Most notably, I've done an [UPMEM backend](https://github.com/mrakgr/PIM-Programming-In-Spiral-UPMEM-Demo). UPMEM doesn't seem to be interested in programming in a high level functional language. Their loss, but doing the backend for it made me realize that I've recovered some of my taste for programming.

For the past year and a half I've been studying 3d [art](https://twitter.com/Ghostlike), as well as doing [writing](https://www.royalroad.com/fiction/57747/simulacrum-heavens-key). But it is really difficult to make it on your own. 600 pages posted on RR, and I only have a single Patron contributing 4E/month. That is not going to go anywhere. So what I am doing now is looking for a job. You can see my [resume here](https://docs.google.com/document/d/1D6roVeWFWkwtSfSRr5ac3utd-qSvTtTgBMIbaQ0ZoTo/edit), it is also pinned on my Twitter profile. I do not suppose any of you here would like to hire me on a remote basis?

Since I've started applying, I want to get better at talking, so I've started doing Youtube videos. What motivates this is partly my interview anxiety, and partly the fact that when I showed Spiral to UPMEM one of the engineering directors asked me for a presentation of all things! So now I am doing a small series on [setting up Stable Diffusion on Paperspace](https://www.youtube.com/playlist?list=PL04PGV4cTuIVGO5ImYTk9wPVmbgdYbe7J). It is actually much harder than I thought it would be. Yesterday to make a 11.5m video, I needed to spend over 5 hours editing it. Those Youtubers with slick presentations make it look much easier than it is.

Besides that I got some interesting news regarding AI hardware. I've been eyeing Tenstorrent for a while, and got an ETA of 6 months until they open source their SDK and allow consumers to program their devices. Out of all the AI hardware companies, Tenstorrent is the most interesting to me as they are making cheaps that you could slot into your home rig. All the other companies are focusing on the big fish, so I am hoping Tenstorrent will deliver something worth programming in. One of their claims is that their devices will be easier to program than GPUs so I have great expectations. Right now I have a big problem because at the rate things are going I won't be able to afford that hardware when it comes out.

The only way to resolve this problem is to get a job for the first time. I really hope that I won’t stay as a Youtuber for too long as in contrast to writing, I hate talking.

///

This should be good enough for tomorrow.

3:45pm. Now let me do a retake.

3:50pm. I am pretty depressed. If I were doing Youtube vids seriously, at this point I'd ditch doing the voice myself completely and reach for voice overs. Well, let me give it a try again.

4:05pm. Ah, damn it. Let me try the trial version of Audiate.

Nevermind, I can edit it later. Actually, I want to do it now.

4:15pm. It wants to log into my account. Forget it. I'll have to do it all manually. Let me clean up the video by hand and I will post it online.

///

A closeup of castle on a snowy mountain. God rays. Vibrant colors. Best quality, highest detail, 4k, masterpiece. By Jessica Rossier.
Negative prompt: ugly, blurry, dull
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 43409684, Size: 512x512, Model hash: cc6cb27103, Model: v1-5-pruned-emaonly, Denoising strength: 0.65, Hires upscale: 2.5, Hires upscaler: Latent

///

You really need the 2M Karras when upscaling otherwise it messed up the image.

https://youtu.be/Y_5L7pKan7M
Camtasia Tutorial - Lesson 63 - Audio Compressor Effect

https://youtu.be/kCc8FmEb1nY
Let's build GPT: from scratch, in code, spelled out.

This caught my attention on the sidebar. He got 517k views. So maybe there is demand for ML stuff, but I am sure this is getting a lot of views because it is Karpathy. Forget it for now.

4:30pm. I really need something to make it easier to clean up the taking of breaths and smacking of lips.

4:35pm. Ok, I won't correct every little thing with 100s of cuts otherwise it would take forever. I need a pro audio tool in order to get rid of the lip smacking sounds.

https://www.reaper.fm/

Let me give this a try.

https://www.reddit.com/r/audioengineering/comments/1xtm1r/are_there_any_good_ways_to_remove_mouth_noises_in/

///

Editing it out by hand is the only real solution. I know because this is what I do for a living. If I could find a shortcut, I'd get employee of the decade and then swiftly fired and replaced by a circus chimp. To avoid the jarring effect, you have to zoom way in and cut out just the wave that has the offending noise in it. Striking a balance between removing the noise and making it unnoticeable is a constant chore. Another trick if the spot you're removing is longer, like a breath, you can do a quick fade right before the spot and mute the noise then fade back in. Depending on the kind of noise, there's a different approach.

As far as preventative measures, I've heard all kinds of witch-doctor tricks to try and had varying degrees of success. Some people say eat green apples before a session. Some people say keep your mouth dry. some people say keep your mouth wet. It's different for everybody.

///

Oh damn.

5:15pm. This time things are better as I am not fixing every little thing. Amazing how making two takes makes a difference. But I really need to be more sensitive in the future as to how I speak. Those lip smacking sounds that I take before I start speaking really gets picked up by the mic! I am also constantly taking in breath. I am not sure what to do about that.

5:20pm. I think I could avoid to smack my lips before I start speaking, but breathing is something I simply have to do.

https://www.youtube.com/watch?v=E_QQ_25GW9A
Camtasia 2021: How To Remove Background Noise, Ums, Ahs, Breathing Inhales and Other Noise Reduction

This got posted two days ago.

Let me watch it.

https://youtu.be/E_QQ_25GW9A?t=123

Is this how it is used? I admit, I have no idea what the various options in the noise removal node do. I had no idea the range had anything to do with it.

https://youtu.be/E_QQ_25GW9A?t=241

How long is he going to demo it? Will this really get rid of the breathing?

https://youtu.be/E_QQ_25GW9A?t=355

Removing it manually is what I was doing yesterday. Is there a better way?

https://youtu.be/E_QQ_25GW9A?t=400

Hmmm, I was just ripple deleting it. I thought he would use something like a node. This is still doing it manually.

Let me ask in the ML sub, whether there are NN plugins to assist sound editing.

https://www.reddit.com/r/MachineLearning/comments/10p7hup/d_are_there_neural_net_plugins_to_assist_audio/

I asked. Let me continue editing.

Oh, right. Let me watch it from the start and then I will do an extra section.

6:15pm. I think I am getting more efficient at this. Let me record an extra section.

7:05pm. Done with both lunch and editing the video.

7:15pm. Forgot to put in the transition.

7:30pm. https://youtu.be/1Bqbfr8wOIs
How To Setup The Paperspace Gradient Notebook

Finally done. Today felt a bit better than yesterday, but then again, the video wasn't as long.

///

Thanks for the tip! There is a program called Descript that will remove the ums and ahs, but it's just another thing to have to export and use, then reimport into Camtasia. I think Camtasia should license these tools and include them in the software. https://www.descript.com/ Adobe also has a free tool that does an amazing job at background noise removal and voice enhancement: https://podcast.adobe.com/enhance

///

Hmmm...

7:35pm. Well, I am done for the day. I got some good practice in. No emails so far. Maybe they will come overnight.

7:50pm. I'll watch Eiyuuou here.

Tomorrow, I'll still have time for another video. As foretold, I'll show how to download and use other models. Then I will do a few vids on regular prompting. And then I will be done with that series in Youtube style.

8pm. Hmmm, I am just to depressed to program in Spiral right now. I could do the RL thing, but what I really want is to program for money. I want to program AI chips, not mess with these stupid toy devices like GPUs and CPUs. I am hungry. I want a real taste of success. I am just hungry for acceptance. If I do not get parties interested in my resume, I'll pick freelancing even if it pays crap. Backends, platforms, whatever. It is not like I cannot do it."

---
## [Koi-3088/ForkBot.NET](https://github.com/Koi-3088/ForkBot.NET)@[4c37bc7aca...](https://github.com/Koi-3088/ForkBot.NET/commit/4c37bc7aca0138710af6ab9f16fc1f4262fbe131)
#### Monday 2023-01-30 19:51:52 by Koi

Mr. Mime is a thing, unfortunately.
Mild clean, some more Cherish set handling attempts.
Exclude set MetDate from mystery gifts.
Fix daycare enum parsing.
Check for no result in case $qc was used or some other weird thing happens.
Remove FixOT and TradeCord as routine types (FlexTrade handles both).
Try to apply trainer info for Mystery gifts.
Re-add fixed met date if not GO origin.
Update DenBot distribution data, minor fixes.
Fix Yamask-Galar in daycare, some more oopsies.
-Add DenBot - a seed lookup and day skipper bot for raids.
-Change AutoRoll's behavior to make use of some of DenBot's functionality.
Minor clean.
Revise TradeCord "traded" check, remove potential user path straggler entries because paranoia, some minor fixes.
TradeCord fixes (shocker, I know).
Extract Json serializer.
Minor clean and fixes.
Minor fixes.
Fix Milcery when an Alcremie variant is a parent.
Update to latest Core and ALM dependencies.
Handle non-shiny events in a better way.
Work around a race condition?
Simplify and de-bugify trade completion check.
Fix indexing, improve chance for Melmetal-Gmax because it's nigh impossible to get.
Rework TradeCord internals, add new functionality:
-Migrate user data from ".txt" files to a serialized Json (migration for a large amount of users will take a few minutes, be patient).
-Make TradeCord configurable, add its own settings category.
-Add some template events with an optional end timer (YYYY/MM/DD 8PM as an example, though any local time format should work).
-Add barebones Pokedex (counter, flavor text).
-Can check dex completion by typing `$dex`, check missing entries by typing `$dex missing`.
-Completing the Pokedex will slightly improve shiny rate.
-Can now mass release cherish event Pokemon and shinies ($massrelease shiny/cherish).
-Various tweaks, improvements, and bugfixes.

Slightly change FixOT's behavior:
-If a shown Pokemon is illegal and an event, attempt to find a match within the MGDB first.
-Try to force users to trade away the shown Pokemon, log attempt to change shown Pokemon.
Add consideration for easter eggs being enabled in settings, fix Suicune
Change species rng for TradeCord, some bugfixes (I really need to rewrite this mess)
Add check if we're using ListUtil for Giveaway instead of TradeCord.
Amend commit since I'm squashing and force-pushing while bringing the fork in line with the main branch
Add Giveaway module to Discord bot (#22)

Thanks, rigrassm.
Co-authored-by: Koi-3088 <61223145+Koi-3088@users.noreply.github.com>
Specify USB port instead of adding the first result (can be found via Device Manager).
Re-add boolean check because we don't want to fix everything
FixOT will attempt to regenerate illegal Pokémon.
Apply trash bytes for reasons.
Minor TradeCord fixes and adjustments.
Minor clean for C#9
Use "GetValidPreEvolutions()" instead of "GetPreEvolutions()".
Index forms correctly.
Fix the fixed and re-introduced empty daycare index error.
*an* Ultra Ball.
Add EvoTree breeding for TradeCord.
Remove unnecessary value declarations for pinging on encounter match.
Mildly beautify EncounterBot mark output.
Integrate Anubis' system update prevention into Soft Reset and Regigigas Encounter Modes.
Rename "Regi" Encounter Mode to "Soft Reset".
Speed up "A" clicks for Regigigas and Soft Reset modes.
Add Mark logging output for EncounterBot.
Fix oops (re-order logic, remove unnecessary lines).
Add optional species and form specification for $massrelease
Use an obscure string splitter because people like symbols in their names.
Fix things that broke after rebasing to the latest main repo commit.
Use a less unfortunate field name and value splitter...again.
Fix Marowak-Alola always generating as an NPC trade.
Add filters for "$list <species>" to narrow down results.
Fix Cherish Pichu and Octillery
Stop making dumb mistakes, me (implying the rest of it isn't a dumb mistake).
Can't breed antiques.
Use a less unfortunate embed name and value splitter
Add Melmetal-Gmax to TradeCord.
Add ability to search by caught ball.
Have MassRelease ignore events.
Add specific regional form breeding.
Revise egg rate and egg shiny chance.
Have trade evolutions hold an Everstone.
Add an extra right click when navigating to settings for AutoRoll.
Add reworked encounter/egg/fossil logs.
Minor clean.
Minor clean.
Get rid of EncounterBot, FossilBot, EggFetch text logs until I properly rework them.
Break on an empty page due to aggressive rounding
Add multi-page lists for Tradecord.
More random bugfixes.
Fix some bugs before major clean
Add Language parameter for TradeCord.
Change trainer info input format for TradeCord.
Move focus on Showdown set instead of randomizing a pkm file.
Allow user to enter whatever they want for $list, handle edge cases like Kommo-o
Add "$list all" to show non-duplicate caught species.
Automatically remove from favorites if trading or gifting (small QOL thing).
Change how favorites are removed from user file.
Revert base egg shiny chance nerf.
Fix daycare
Add favorites command to TradeCord.
Slightly nerf eggs.
Fix TradeCord list for shinies
Add TradeCord (my dumbest and messiest project so far, Archit pls don't hate the mess).
Add Showdown output for Star/Square shinies and OTGender.
Add optional link code input for FixOT.
Change how OTName, TID, SID is displayed.
Add Regigigas SR bot.
Add SoJ Camp SR bot.
Ribbons now work with EggTrade (remove ribbons if egg).
Remove EggRoll.
Add another filter for FixOT
Fix.. FixOT
Update offsets for EncounterBot catching.
Slightly change StrongSpawn to work with Regi SR and make it its own mode.
Make SpinTrade only available for USB-Botbase
Update valid eggs for CT
winforms: resize icon.ico to fix crash at startup on unix using mono
Rework Spin, read initial in-game coordinates in order to correct drift
Add TID, SID, Language output for Showdown
Remove obsolete OT and Language parsing
Very minor clean until I have time for a proper one.
Detach controller when stopping USB bot.
Actually set LastUsedBall for EncounterBot (missed when bringing in line with main repo)
Move extra RaidBot timings following the official commit
Remove PKHeX Discord invite from Readme.md

Maybe fewer people will pester devs now about my unofficial fork?
Update for latest main repo EncounterBot commits.
Update README.md
Add back best commit: Red's SpinTrade.
Add egg trades, foreign Dittos and OT for Twitch.
If ItemMule is enabled, also display the item a user is receiving.
Add periodic time sync toggle for all methods of hosting (except for non-soft locked AutoRoll) to (hopefully) prevent den rollover during extended hosts.

Add routine to exit a lobby for SoftLock if no players are ready in time (to preserve soft lock).

Add a routine to recover from disbanded lobbies (when someone disconnects unexpectedly) for SoftLock.

Add a routine to restart game if all else fails and we're stuck in a raid.

Add a routine for adding and deleting friends if we're soft locked and raids go empty.

Slightly reorganize settings, extract methods, minor clean.
Don't use such a generic file name for stream assets.
Check USB port index for running bots. Should fix adding additional USB bots when no config is saved.
Add fixed met date for FixOT.
How do I boolean
Change airplane mode logic, tweak timings and routine for soft lock lobby exit
Rework EggRoll cooldown (static list in favor of a txt file).
Start clean up and refactor
Add setting to increase delay after pressing "Home" after a date skip.
Use USB port index for blocking and sprite pngs if connection type is USB
Add option for airplane host (usb-botbase required)
Add option to softlock on selected species for AutoRoll
Add automatic compatibility for all console languages when date skipping (have to set ConsoleLanguage under ScreenDetection)
Attempt to fix multiple USB device add and connect...again
Minor clean
Fix oops?
Handle add/remove of bots
Distinguish between multiple USB devices, tweak BotRemoteControl for USB, other various fixes
Add SpA modifier for foreign Dittos
Add alpha USB-Botbase support
Fix DateTime parsing for European format for EggRoll
Set fixed EggMetDate and MetDate for EggRoll
More FixOT filters
Remove Beheeyem. Oops.
Split EggRoll into its own routine and trade type, only output "Receiving: Mysterious Egg" if routine is EggRoll, other minor tweaks and fixes
Make FixOT its own queue with roles and counts
Add a couple more OTs to $fix
Parsing for EggRaffle auto-clear and $clearcooldown
Adjust timings and split Watt collecting clicks for AutoRoll
Fix oops with file attachments for Ditto
Further improvements for OT, memes for invalid pokemon (disable EasterEggs)
Add spaces, digits for OT
Randomize memes, cut down bloat
Fix miscellaneous bots after Anubis' recent QOL additions
-Ignore events for OT because headache.
-Add overlooked "$convert <generation>" input for OT.
-Move $clearcooldown to SudoModule
-Clear timer automatically if NoTrainerFound
-More reliable Dittos
-Foreign Dittos for $convert
-Command to clear cooldown for EggRaffle in case trade gets disconnected
-Fix "Trade finished" line to keep result secret
-EggRaffle as a toggle, option to specify channels
-Seed Check output to both DMs and Channel (apparently some want it)
-Randomly generated egg raffle via a "$roll" command with a configurable cooldown
-FixAdOT reworked, has its own command "$fix" and no longer overrides $clone
-Ball: <value> output for Showdown sets
-Fix oversight
-Option to output Seed Check results to Discord channel with a User mention
-Showdown set output for OT name and eggs
-Basic "OT: <name>" option without Showdown set output
-Initial $convert support for EggTrade
-Egg moves for EggTrade test attempt
-Minor update
-EggTrade (by nicknaming a Pokémon "Egg" using $trade)
-Failsafe for memes if enabled but field left blank or incomplete
-Niche breedable Ditto trade mode.
Add minimize button
EggFetch text logs
StrongSpawn mode for EncounterBot
Re-add EncounterBot Master Ball catching
More parsing for FixAdOTs
Park Ball as held item instead of string
Actually remove the offset instead of saying I did
Initial DLC commit
Faster code entry
Removed catching for EncounterBot (need a new offset)
CloneBot mode to fix Nickname and OT if adverts detected

---
## [JoeBidenWhatAreYouHiding/kx](https://github.com/JoeBidenWhatAreYouHiding/kx)@[2e35b2b39b...](https://github.com/JoeBidenWhatAreYouHiding/kx/commit/2e35b2b39b85f774bbb5ec021e0b9ea9cf54a6f7)
#### Monday 2023-01-30 20:10:02 by Todd Howard

this is DAHOMEY bitch!!! we clown in this muthafucka better take yo sensitive ass back to GHANA

---
## [kokizzu/kui](https://github.com/kokizzu/kui)@[a39168b327...](https://github.com/kokizzu/kui/commit/a39168b327cdfc9b52dd031db090a7de4d15b61d)
#### Monday 2023-01-30 20:31:51 by Nick Mitchell

fix: improved fix for externalizing electron/remote

- We should be using the `webpackIgnore: true` magic comment, rather than the silly hack we had from #9265
- #9265 missed the second import of electron/remote

---
## [RalphHightower/RalphHightower](https://github.com/RalphHightower/RalphHightower)@[7da2bacfb9...](https://github.com/RalphHightower/RalphHightower/commit/7da2bacfb9f8541233537cd1d566c5bbdc6a9cb8)
#### Monday 2023-01-30 22:18:08 by Ralph Hightower

docs: 2023-01-25 FITSNews update (closes #604)

| **January 25, 2023** |
| [‘Murdaugh Murders’ Saga: Alex Murdaugh’s Clothes From Night Of Murder Are Missing](https://www.fitsnews.com/2023/01/25/murdaugh-murders-saga-alex-murdaughs-clothes-from-night-of-murder-are-missing/) |
More missing evidence?
|Accused killer Alex Murdaugh made multiple wardrobe changes on the evening of June 7, 2021 – the night prosecutors say he savagely murdered his wife and younger son on his family’s Lowcountry, South Carolina hunting property.<br>Why does this matter? Because the clothes he removed in at least one of these wardrobe changes have reportedly vanished without a trace, sources say … not unlike the weapons Murdaugh allegedly used to kill his wife, 52-year-old Maggie Murdaugh, and youngest son, 22-year-old Paul Murdaugh on the family’s 1,700-acre hunting property in Colleton County on June 7, 2021.<br>News of at least one of Murdaugh’s wardrobe changes on the night of the murders was reported Wednesday afternoon by Columbia, S.C. criminal defense attorney Lori Murray – whose TikTok page has been a big hit among those tracking the ‘Murdaugh Murders‘ crime and corruption saga.<br>Murray specifically discussed clothes Murdaugh was wearing in a Snapchat video sent from Paul Murdaugh at 7:56 p.m. EDT on the night of the murders.<br>*“I think I finally know what was on the Snapchat video Paul (Murdaugh) sent to his friends at 7:56 p.m. on the night he was killed,”* Murray said in her clip. *“Alex Murdaugh can be seen on that video wearing long pants and a dress shirt – not the clothes he was seen wearing when police arrived after he called 9-1-1.”*<br>*“He changed clothes a lot that day,”* one source familiar with the status of the case told me.<br>Lead prosecutor Creighton Waters did not reference them during his opening arguments on Wednesday afternoon – in which he laid out several new details of the case agains Murdaugh.<br>Curiously, the 7:56 p.m. EDT Snapchat video was referenced by lead defense attorney Dick Harpootlian in his opening statement – as purported evidence of the closeness between Alex Murdaugh and his son, whom he referred to as *“the apple of his (father’s) eye.”*<br>Harpootlian also seemed to invite scrutiny of the wardrobe changes during his opening argument when he asked jurors about the lack of physical evidence in the case.<br>*“Where are the bloody clothes?”* Harpootlian asked jurors.<br>That’s a very good question … but the fact we are having to ask it at all could wind up backfiring on Murdaugh’s attorneys in a big way if the clothes Murdaugh was wearing on the night of the murders have truly vanished.|

---
## [RalphHightower/RalphHightower](https://github.com/RalphHightower/RalphHightower)@[6d0a1f3d94...](https://github.com/RalphHightower/RalphHightower/commit/6d0a1f3d946654ed2c963270e1e9e9e5ff446e4c)
#### Monday 2023-01-30 22:18:08 by Ralph Hightower

docs: 2023-01-25 P&C update (closes #6xx)

| [Alex Murdaugh trial begins with explosive opening statements, support from relatives](https://www.postandcourier.com/murdaugh-updates/alex-murdaugh-trial-begins-with-explosive-opening-statements-support-from-relatives/article_5b67bd1c-9cc8-11ed-8eeb-7f00639e747d.html)<br>*“You’re going to see what he did to Maggie and Paul,”* Waters said. *“It’s going to be gruesome. There’s no other way around it.”<br>The Columbia trial attorney and state senator countered that his client was a loving husband and father who was incapable of inflicting the shotgun blasts that killed Paul, the 22-year-old “apple of his eye,” or the rifle shots that took down Maggie, 52.<br>Harpootlian described the scene in great and gory detail. Shot at close range, Paul’s head exploded *“like a watermelon,”* he said, describing that brain matter was sprayed all over the walls and floor of the feed room he was standing in by the property’s dog kennels. Only the front of his face was left intact, Harpootlian said.<br>Maggie was shot next as she ran away from the scene, Harpootlian said. She had fallen and was lying prone when the killer fired the fatal shot into the back of her head, the defense attorney said.<br>Harpootlian repeatedly used words like “butchered,” “slaughtered” and “executed” to describe the slayings, contrasting the horrific violence against what he described as a lack of evidence of discord in the family.<br>*“He didn’t kill — butcher — his son and wife,”* Harpootlian said.<br> Yet state investigators spent some 13 months trying to prove it, rather than pursue an objective investigation to find the real killer, Harpootlian said.<br>*“They decided that night: He did it,”* Harpootlian said. *“They’ve been pounding that square peg in that round hole.”*<br>In a twist, Murdaugh’s surviving son, Buster; brothers Randy and John Marvin; sister Lynn Murdaugh Goette; and sister-in-law Liz Murdaugh appeared in court. They declined to speak with reporters outside the courthouse. But they sat in the second row behind the defendant and at times spoke with him as he turned around in his chair to face them.<br>Murdaugh’s relatives had skipped Alex Murdaugh’s prior court appearances, hoping to avoid the publicity that would surely follow.<br>Murdaugh’s lawyers have named each of them as potential witnesses in the trial. It is unclear what they might say. But their testimony would come later in the trial, if at all. |

---
## [Bee-Have/Inception_duck](https://github.com/Bee-Have/Inception_duck)@[88881ede0b...](https://github.com/Bee-Have/Inception_duck/commit/88881ede0b9498966ff9242bf2d8654f6005d7cb)
#### Monday 2023-01-30 22:44:34 by amarini-

✨🚧 -Added Dockerfile for mariadb and wordpress. it's not working but it's a fucking start so fuck you

---
## [git/git](https://github.com/git/git)@[69bbbe484b...](https://github.com/git/git/commit/69bbbe484ba10bd88efb9ae3f6a58fcc687df69e)
#### Monday 2023-01-30 23:10:07 by Jeff King

hash-object: use fsck for object checks

Since c879daa237 (Make hash-object more robust against malformed
objects, 2011-02-05), we've done some rudimentary checks against objects
we're about to write by running them through our usual parsers for
trees, commits, and tags.

These parsers catch some problems, but they are not nearly as careful as
the fsck functions (which make sense; the parsers are designed to be
fast and forgiving, bailing only when the input is unintelligible). We
are better off doing the more thorough fsck checks when writing objects.
Doing so at write time is much better than writing garbage only to find
out later (after building more history atop it!) that fsck complains
about it, or hosts with transfer.fsckObjects reject it.

This is obviously going to be a user-visible behavior change, and the
test changes earlier in this series show the scope of the impact. But
I'd argue that this is OK:

  - the documentation for hash-object is already vague about which
    checks we might do, saying that --literally will allow "any
    garbage[...] which might not otherwise pass standard object parsing
    or git-fsck checks". So we are already covered under the documented
    behavior.

  - users don't generally run hash-object anyway. There are a lot of
    spots in the tests that needed to be updated because creating
    garbage objects is something that Git's tests disproportionately do.

  - it's hard to imagine anyone thinking the new behavior is worse. Any
    object we reject would be a potential problem down the road for the
    user. And if they really want to create garbage, --literally is
    already the escape hatch they need.

Note that the change here is actually in index_mem(), which handles the
HASH_FORMAT_CHECK flag passed by hash-object. That flag is also used by
"git-replace --edit" to sanity-check the result. Covering that with more
thorough checks likewise seems like a good thing.

Besides being more thorough, there are a few other bonuses:

  - we get rid of some questionable stack allocations of object structs.
    These don't seem to currently cause any problems in practice, but
    they subtly violate some of the assumptions made by the rest of the
    code (e.g., the "struct commit" we put on the stack and
    zero-initialize will not have a proper index from
    alloc_comit_index().

  - likewise, those parsed object structs are the source of some small
    memory leaks

  - the resulting messages are much better. For example:

      [before]
      $ echo 'tree 123' | git hash-object -t commit --stdin
      error: bogus commit object 0000000000000000000000000000000000000000
      fatal: corrupt commit

      [after]
      $ echo 'tree 123' | git.compile hash-object -t commit --stdin
      error: object fails fsck: badTreeSha1: invalid 'tree' line format - bad sha1
      fatal: refusing to create malformed object

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[ca11b0640a...](https://github.com/git-for-windows/git/commit/ca11b0640aa6f17bc53f55a4b41cf1bffa6ddc13)
#### Monday 2023-01-30 23:14:24 by Johannes Schindelin

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
## [KabKebab/GS13](https://github.com/KabKebab/GS13)@[bf39fb7536...](https://github.com/KabKebab/GS13/commit/bf39fb75364bfbe0b3efe9760dd73ac7fe25c74d)
#### Monday 2023-01-30 23:53:29 by Sonoida

FUCK YOU, RADSTORMS!

Removed radstorms. They're an interesting event, but cause more distraction and interruption to RP than actual fun. Not a good fit for lowpop RP place.

---

