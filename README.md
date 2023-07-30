## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-07-29](docs/good-messages/2023/2023-07-29.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,789,125 were push events containing 2,539,166 commit messages that amount to 151,477,578 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 49 messages:


## [Merek2/coyote-bayou](https://github.com/Merek2/coyote-bayou)@[bb08166bcf...](https://github.com/Merek2/coyote-bayou/commit/bb08166bcfe011671ddf3b944e44c8e5a69c5195)
#### Saturday 2023-07-29 00:00:41 by Tk420634

I hate cameras to death

And atmos shit die die die die die die die die die die die die die die die die die die die die die die die die die die die die die die die die die die die die

---
## [lewcc/Paradise](https://github.com/lewcc/Paradise)@[2d10818063...](https://github.com/lewcc/Paradise/commit/2d1081806334fc023de600338b836d55dd6fa5ee)
#### Saturday 2023-07-29 00:27:34 by ATP-Engineer

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
## [peptron1/tgstation](https://github.com/peptron1/tgstation)@[867c217c57...](https://github.com/peptron1/tgstation/commit/867c217c57bbcbb644e06bfcb6d362e494a895ee)
#### Saturday 2023-07-29 03:02:47 by GuillaumePrata

New Wizard spell "branch": Vendormancy (#75679)

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

Co-authored-by: Time-Green <7501474+Time-Green@users.noreply.github.com>

---
## [Raymi306/zola-fork](https://github.com/Raymi306/zola-fork)@[b5a90dba5d...](https://github.com/Raymi306/zola-fork/commit/b5a90dba5d12ea6760c3aa18fec40f8af4d7cbc7)
#### Saturday 2023-07-29 03:41:11 by sinofp

Add support for lazy loading images (#2211)

* Add optional decoding="async" loading="lazy" for img

In theory, they can make the page load faster and show content faster.

There’s one problem: CommonMark allows arbitrary inline elements in alt text.
If I want to get the correct alt text, I need to match every inline event.

I think most people will only use plain text, so I only match Event::Text.

* Add very basic test for img

This is the reason why we should use plain text when lazy_async_image is enabled.

* Explain lazy_async_image in documentation

* Add test with empty alt and special characters

I totaly forgot one can leave the alt text empty.
I thought I need to eliminate the alt attribute in that case,
but actually empty alt text is better than not having an alt attribute at all:
https://www.w3.org/TR/WCAG20-TECHS/H67.html
https://www.boia.org/blog/images-that-dont-need-alternative-text-still-need-alt-attributes
Thus I will leave the empty alt text.

Another test is added to ensure alt text is properly escaped.
I will remove the redundant escaping code after this commit.

* Remove manually escaping alt text

After removing the if-else inside the arm of Event::Text(text),
the alt text is still escaped.
Indeed they are redundant.

* Use insta for snapshot testing

`cargo insta review` looks cool!

I wanted to dedup the cases variable,
but my Rust skill is not good enough to declare a global vector.

---
## [Sebasssssss/Music-player-with-ChatGPT](https://github.com/Sebasssssss/Music-player-with-ChatGPT)@[68f75d2be5...](https://github.com/Sebasssssss/Music-player-with-ChatGPT/commit/68f75d2be59765e0db9fcea19a317be5aa17c4d4)
#### Saturday 2023-07-29 04:29:24 by Sebasssssss

Finally fix this fucking shit. If you seeing this commit, sorry for the language. I strugge 2 fucking months to fix this shit. Audio working correctly on every fucking route of this fucking hilarious app

---
## [fesh0r/mame-full](https://github.com/fesh0r/mame-full)@[6db28f4041...](https://github.com/fesh0r/mame-full/commit/6db28f40416aa72a75128537e29b20985c26c75d)
#### Saturday 2023-07-29 04:29:37 by A-Noid33

New working software list items (mac - macii) 123 dumps (#11432)

* Initial softlist for mac moof 400/800 floppy disks

* Added mac moof software list support

New working software list items (123 working dumps)
-------------------------------
mac_flop_orig:

Lode Runner (version 1.0) [4AM, Anoid]
Balance of Power (version 1.03) [4AM, Anoid]
Shanghai (version 1.0) [4AM, Anoid]
Skyfox [4AM, Anoid]
Temple of Apshai Trilogy [4AM, Anoid]
The Surgeon (version 1.5) [4AM, Anoid]
Uninvited [4AM, Anoid]
King's Quest (version 1.10) [4AM, Anoid]
Smash Hit Racquetball (version 1.01) [4AM, Anoid]
The Ancient Art of War [4AM, Anoid]
Hacker II [4AM, Anoid]
Rambo: First Blood Part II [4AM, Anoid]
One on One [4AM, Anoid]
Indiana Jones and the Revenge of the Ancients [4AM, Anoid]
Winter Games (version 1985-10-24) [4AM, Anoid]
Winter Games (version 1985-10-31) [4AM, Anoid]
Star Trek: The Kobayashi Alternative (version 1.0) [4AM, Anoid]
Mac Attack [4AM, Anoid]
GATO (version 1.3) [4AM, Anoid]
Dark Castle (version 1.0) [4AM, Anoid]
Oids (version 1.4) [4AM, Anoid]
MacWars [4AM, Anoid]
Shadowgate [4AM, Anoid]
Seven Cities of Gold [4AM, Anoid]
Enchanted Scepters [4AM, Anoid]
Beyond Dark Castle [4AM, Anoid]
Arkanoid (version 1.00) [4AM, Anoid]
The Chessmaster 2000 (version 1.02) [4AM, Anoid]
Maze Survival [4AM, Anoid]
Frogger (version 1.0) [4AM, Anoid]
SimCity (version 1.2, black & white) [4AM, Anoid]
Falcon (version 1.0) [4AM, Anoid]
Cutthroats (release 23 / 840809-C) [4AM, Anoid]
The Witness (release 22 / 840924-C) [4AM, Anoid]
Seastalker (release 15 / 840522-C) [4AM, Anoid]
Zork III (release 17 / 840727-C) [4AM, Anoid]
A Mind Forever Voyaging (release 77 / 850814-E) [4AM, Anoid]
Hollywood Hijinx (release 37 / 861215-I) [4AM, Anoid]
Nord and Bert Couldn't Make Head or Tail of It (release 19 / 870722-I) [4AM, Anoid]
Border Zone (release 9 / 881008-3B) [4AM, Anoid]
The Hitchhiker's Guide to the Galaxy (release 47 / 840914) [4AM, Anoid]
Zork I: The Great Underground Empire (release 76 / 840509) [4AM, Anoid]
Deadline (release 27 / 831005-C) [4AM, Anoid]
Infidel (release 22 / 840522-C) [4AM, Anoid]
Suspect (release 14 / 841005-C) [4AM, Anoid]
Planetfall (release 29 / 840118-B) [4AM, Anoid]
Ballyhoo (release 97 / 851218-G) [4AM, Anoid]
Enchanter (release 24 / 851118-G) [4AM, Anoid]
Spellbreaker (release 63 / 850916-F) [4AM, Anoid]
Trinity (release 11 / 860509-3H) [4AM, Anoid]
Stationfall (release 107 / 870430-G) [4AM, Anoid]
The Lurking Horror (release 203 / 870506-G) [4AM, Anoid]
Alter Ego (male version 1.0) [4AM, Anoid]
Alter Ego (version 1.1 female) [4AM, Anoid]
The Print Shop (version 1.2) [4AM, Anoid]
Flight Simulator (version 1.02) [4AM, Anoid]
Run for the Money [4AM, Anoid]
Master Tracks Pro (version 4.0) [4AM, Anoid]
Where in Time is Carmen Sandiego? (version 1.0) [4AM, Anoid]
Deluxe Music Construction Set (version 1.0) [4AM, Anoid]
Apache Strike (version 1.2) [4AM, Anoid]
Wizardry VI: Bane of the Cosmic Forge [4AM, Anoid]
Harrier Strike Mission [4AM, Anoid]
Airborne! [4AM, Anoid]
Mac Vegas (version 1.1) [4AM, Anoid]
Dragonworld [4AM, Anoid]
MacDraft (version 1.2) [4AM, Anoid]
The Mind Prober (version 1.0) [4AM, Anoid]
The Toy Shop (version 1.1) [4AM, Anoid]
Strategic Conquest (version 1.2) [4AM, Anoid]
The Home Accountant (version 1.01) [4AM, Anoid]
Sub Battle Simulator [4AM, Anoid]
Vegas Video Poker [4AM, Anoid]
The Pawn (version 2.3) [4AM, Anoid]
Downhill Racer [4AM, Anoid]
Dollars and Sense (version 1.3) [4AM, Anoid]
Alternate Reality: The City (version 3.0) [4AM, Anoid]
Borrowed Time [4AM, Anoid]
The Quest [4AM, Anoid]
The Crimson Crown [4AM, Anoid]
Mindshadow [4AM, Anoid]
Pensate (version 1.1) [4AM, Anoid]
Sierra Championship Boxing [4AM, Anoid]
Championship Star League Baseball [4AM, Anoid]
Forbidden Castle [4AM, Anoid]
Defender of the Crown [4AM, Anoid]
The King of Chicago [4AM, Anoid]
Macintosh Pascal (version 1.0) [4AM, Anoid]
Fusillade [4AM, Anoid]
Orb Quest: Part I: The Search for Seven Wards (version 1.04) [4AM, Anoid]
Speed Reader II (version 1.1) [4AM, Anoid]
][ in a Mac (version 2.03) [4AM, Anoid]
Q-Sheet (version 1.0) [4AM, Anoid]
Fontographer (version 2.4.1) [4AM, Anoid]
Mouse Stampede (version 1.00) [4AM, Anoid]
The Mist [4AM, Anoid]
Tass Times in Tonetown [4AM, Anoid]
Pinball Construction Set [4AM, Anoid]
Transylvania [4AM, Anoid]
Déjà Vu: A Nightmare Comes True!! [4AM, Anoid]
Déjà Vu II: Lost in Las Vegas!! [4AM, Anoid]
Rogue (version 1.0) [4AM, Anoid]
Bridge (version 6.0) [4AM, Anoid]
Harrier Strike Mission II (version 1.2) [4AM, Anoid]
Patton vs. Rommel (version 1.05) [4AM, Anoid]
Moebius: The Orb of Celestial Harmony (version 1.03) [4AM, Anoid]
Tesserae (version 1.06) [4AM, Anoid]
Where in Europe is Carmen Sandiego? (version 1.0) [4AM, Anoid]
Shufflepuck Cafe (version 1.0) [4AM, Anoid]
Geometry (version 1.1) [4AM, Anoid]
Physics (version 1.2) [4AM, Anoid]
SimCity (version 1.1) [4AM, Anoid]
Murder by the Dozen [4AM, Anoid]
The Duel: Test Drive II [4AM, Anoid]
Master Tracks Pro (version 1.10) [4AM, Anoid]
Master Tracks Pro (version 2.00h) [4AM, Anoid]
Master Tracks Pro (version 3.4a) [4AM, Anoid]
Squire (version 1.1) [4AM, Anoid]
Millionaire (version 1.0) [4AM, Anoid]
Microsoft File (version 1.04) [4AM, Anoid]
Microsoft Excel (version 1.00) [4AM, Anoid]
The Fool's Errand (version 2.0) [4AM, Anoid]
MacGammon! (version 1.0) [4AM, Anoid]

---------

Co-authored-by: Bob Schultz <bobschultz03@gamil.com>

---
## [Workbench-Team/space-station-14](https://github.com/Workbench-Team/space-station-14)@[31607a0be0...](https://github.com/Workbench-Team/space-station-14/commit/31607a0be0e2ef24f4d53c7611172ec6d40a3a2b)
#### Saturday 2023-07-29 04:47:43 by Emisse

hardsuit/firesuit cleanup (#18308)

* real

* hjoly fuck you guy sare annoying

* fix cargo arbitrage idk why tf it changed from editing armor values but fuck my life i guess

* why god

* Update suits.yml

* Update cargo_emergency.yml

---
## [beartype/beartype](https://github.com/beartype/beartype)@[0d2ad58a76...](https://github.com/beartype/beartype/commit/0d2ad58a76b60f69c9755bb3c2174140dd2bbc80)
#### Saturday 2023-07-29 06:54:27 by leycec

`beartype.claw` + Python's `-m` CLI option x 2.

This commit is the next in a commit chain generalizing our nascent
`beartype.claw` import hook API to support direct execution of
third-party package submodules via Python's `-m` CLI option (e.g., as
`python3 -m {your_package}.{your_submodule}`), en-route to resolving
issue #269 kindly submitted by Germanic bear-bro @MaxSchoenau.
Specifically, this commit:

* Adds a comprehensive set of data packages to our test suite exercising
  this issue, modelled after the inspirational minimal-reproducible
  example (MRE) supplied by @MaxSchoenau as an archive file attached to
  his initial issue submission. You rock, @MaxSchoenau!
* Exhaustively tests our resolution for this issue via battery of
  **extraprocess unit tests** (i.e., unit tests running Python
  subprocesses forked from the active Python process, enabling those
  tests to pass the `-m` CLI option to those subprocesses).
* Did many other things, which I am too tired to document. Look, it's
  Friday night for crying out loud. What are any of us even doing here!?

Although this technically suffices to resolve this issue, we'd like to
streamline our admittedly hacky implementation for future
maintainability. The longest journey continues being long. (*Heed the lockstep Lockheed!*)

---
## [Supsource/rerun](https://github.com/Supsource/rerun)@[926bf048e2...](https://github.com/Supsource/rerun/commit/926bf048e28a8f4c637afce3c57d793ec8de8454)
#### Saturday 2023-07-29 07:01:47 by Emil Ernerfeldt

Use `camino` crate for UTF8 paths in `re_types_builder` (#2637)

### What
TLDR: camino paths are a more ergonomic, since they implement
`to_string`, `as_str` etc. I think we should use it in more places.

From [the docs of `camino`](https://crates.io/crates/camino):

#### Why camino?
`camino`'s `Utf8PathBuf` and `Utf8Path` types are like the standard
library's `PathBuf` and `Path` types, except
they are guaranteed to only contain UTF-8 encoded data. Therefore, they
expose the ability to get their
contents as strings, they implement `Display`, etc.

The `std::path` types are not guaranteed to be valid UTF-8. This is the
right decision for the standard library,
since it must be as general as possible. However, on all platforms,
non-Unicode paths are vanishingly uncommon for a
number of reasons:
* Unicode won. There are still some legacy codebases that store paths in
encodings like [Shift JIS], but most
  have been converted to Unicode at this point.
* Unicode is the common subset of supported paths across Windows and
Unix platforms. (On Windows, Rust stores paths
as [an extension to UTF-8](https://simonsapin.github.io/wtf-8/), and
converts them to UTF-16 at Win32
  API boundaries.)
* There are already many systems, such as Cargo, that only support UTF-8
paths. If your own tool interacts with any such
system, you can assume that paths are valid UTF-8 without creating any
additional burdens on consumers.
* The ["makefile
problem"](https://www.mercurial-scm.org/wiki/EncodingStrategy#The_.22makefile_problem.22)
asks: given a
Makefile or other metadata file (such as `Cargo.toml`) that lists the
names of other files, how should the names in
the Makefile be matched with the ones on disk? This has *no general,
cross-platform solution* in systems that support
non-UTF-8 paths. However, restricting paths to UTF-8 eliminates this
problem.

[Shift JIS]: https://en.wikipedia.org/wiki/Shift_JIS

Therefore, many programs that want to manipulate paths *do* assume they
contain UTF-8 data, and convert them to `str`s
as necessary. However, because this invariant is not encoded in the
`Path` type, conversions such as
`path.to_str().unwrap()` need to be repeated again and again, creating a
frustrating experience.

Instead, `camino` allows you to check that your paths are UTF-8 *once*,
and then manipulate them
as valid UTF-8 from there on, avoiding repeated lossy and confusing
conversions.


### Checklist
* [x] I have read and agree to [Contributor
Guide](https://github.com/rerun-io/rerun/blob/main/CONTRIBUTING.md) and
the [Code of
Conduct](https://github.com/rerun-io/rerun/blob/main/CODE_OF_CONDUCT.md)
* [x] I've included a screenshot or gif (if applicable)
* [x] I have tested [demo.rerun.io](https://demo.rerun.io/pr/2637) (if
applicable)

- [PR Build Summary](https://build.rerun.io/pr/2637)
- [Docs preview](https://rerun.io/preview/pr%3Aemilk%2Fcamino/docs)
- [Examples
preview](https://rerun.io/preview/pr%3Aemilk%2Fcamino/examples)

---
## [Fennec82/ChaosStation-YW](https://github.com/Fennec82/ChaosStation-YW)@[1724d5a477...](https://github.com/Fennec82/ChaosStation-YW/commit/1724d5a477c2ad2f303ce5b38a9981341ec7f673)
#### Saturday 2023-07-29 07:41:22 by Fennec82

Holy shit Github actions actually found something


CI build failed due to an active edge. Presumably fixed by map merge.

Please, for the love of god, run map merge!


Signed-off-by: Fennec82

---
## [Time-Green/tgstation](https://github.com/Time-Green/tgstation)@[4e91d057d7...](https://github.com/Time-Green/tgstation/commit/4e91d057d7d627bd8c356a2251195eb579106707)
#### Saturday 2023-07-29 07:44:06 by MrMelbert

Adds a wizard Right and Wrong that lets the caster give one spell (or relic) to everyone on the station (#76974)

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

---
## [RalphHightower/RalphHightower](https://github.com/RalphHightower/RalphHightower)@[2a8a7d08ab...](https://github.com/RalphHightower/RalphHightower/commit/2a8a7d08aba47c9d6bba7406e0cbc42137856f73)
#### Saturday 2023-07-29 08:32:29 by Ralph Hightower

docs: copy Dune from ChattingWithChatGPT to Dune


#### Dune by Frank Herbert 

| *"RalphHightower"* / [ChatGPT](https://chat.openai.com/) |
|----|
| *"Can you describe Dune to me?"* |
| Sure! Dune is a science fiction novel by American author Frank Herbert, published in 1965. It is set in the distant future and depicts a feudal society on the planet Arrakis, a desert planet home to the valuable resource known as "spice." The story follows the journey of a young man named Paul Atreides, who becomes embroiled in a power struggle for control of Arrakis and its spice. Along the way, Paul discovers that he possesses special powers and is destined to become a leader in the fight for control of the spice. Dune is a complex and detailed work that explores themes of politics, religion, and the human condition. It is widely regarded as a classic of science fiction and has inspired numerous adaptations in various media. |
| *"Why do different factions want to control the spice?"*|
| In the world of Dune, the spice melange is a valuable and highly sought-after resource that is only found on the planet Arrakis, also known as Dune. It is a rare and valuable substance that has many uses, including as a spice for food, as a medicine, and as a psychoactive drug that enhances mental abilities. The spice is also used to help fold space, which allows for faster-than-light travel between the stars. As a result, control of the spice is highly coveted by the various factions in the Dune universe. In the novel, the noble House Atreides is given control of Arrakis by the ruling emperor, but they are betrayed by their rivals and a power struggle ensues as various factions vie for control of the spice. |
| *"Who are the Bene Gesserit?"*|
| The Bene Gesserit are a powerful and secretive organization in the Dune universe. They are an all-female group that has been around for thousands of years and has a long tradition of training their members in physical and mental disciplines, as well as genetic manipulation. The Bene Gesserit use their skills and knowledge to gain power and influence, and they often operate behind the scenes, manipulating events to their advantage. They are known for their ability to control their own bodies and emotions, and for their use of a specialized form of communication called "Voice," which allows them to influence and control others through speech and persuasion. The Bene Gesserit are highly respected and feared, and they play a significant role in the events of the Dune novels. |
| *"And the Spacing Guild?"*|
| The Spacing Guild is another important organization in the Dune universe. It is a group of powerful and influential people who control the means of interstellar travel, making them an essential part of the economy and politics of the known universe. The Guild is known for its use of Guild Navigators, who are humans that have been genetically altered and trained to navigate space using the spice melange, which allows them to fold space and travel vast distances in a short amount of time. The Navigators are able to achieve this feat by using their heightened mental abilities and by remaining in a tank of melange gas, which helps them to "see" the folds of space. The Guild is a powerful and mysterious organization that wields significant influence in the world of Dune. |
| *"How do the sandworms factor in Arrakis?"*|
| The sandworms of Arrakis, also known as Dune, are giant, ferocious creatures that live in the desert sands of the planet. They are native to Arrakis and are a central part of the ecosystem there. The sandworms are sensitive to vibrations and are attracted to sounds, and they are known to attack and consume anything that disturbs them. The sandworms are also the source of the spice melange, which is produced in their bodies and released onto the surface of the planet when they die. As a result, the sandworms are highly valuable and are closely guarded by the native population of Arrakis, the Fremen. In the Dune novels, the sandworms play a significant role in the story and are an important part of the culture and economy of Arrakis. |
| *"What about the House of Atreides?"*|
| The House of Atreides is a noble family in the Dune universe. They are descended from the royal line of the planet Caladan and are known for their wisdom, strength, and honor. The Atreides family is led by Duke Leto Atreides, who is a just and fair ruler and is respected by his subjects. The Atreides are also known for their fierce loyalty to their family and to their allies. In the Dune novel, the Atreides family is given control of the planet Arrakis by the ruling emperor, but they are betrayed by their rivals and a power struggle ensues as various factions vie for control of the valuable spice that is produced on Arrakis. The story follows the journey of Duke Leto's son, Paul Atreides, as he becomes embroiled in the conflict and ultimately rises to power as the leader of the Fremen, the native population of Arrakis. | 
| *"Who are the Harkonnen?"*|
| The Harkonnen family is a noble house in the Dune universe. They are depicted as cruel, ruthless, and power-hungry, and are the main antagonists in the Dune novel. The Harkonnen are the sworn enemies of the Atreides family and will stop at nothing to destroy them and gain control of the valuable spice that is produced on the planet Arrakis. The Harkonnens are known for their brutal tactics and are feared throughout the universe. They are led by Baron Vladimir Harkonnen, who is a cruel and sadistic man who takes pleasure in causing pain and suffering. The Harkonnens play a significant role in the Dune novel and are an important part of the story. |
| *"How are sandworms detected?"*|
| Sandworms on the planet Arrakis, also known as Dune, are difficult to detect because they live deep beneath the sand and are sensitive to vibrations and sounds. They are attracted to anything that disturbs them and will emerge from the sand to attack and consume it. To avoid attracting the attention of sandworms, the native population of Arrakis, the Fremen, have developed special techniques for detecting and avoiding them. One method is the use of "thumper" devices, which are large, mechanical drums that are used to create vibrations in the sand. By creating a rhythmic pattern of vibrations, the Fremen are able to communicate with each other and to attract sandworms to a specific location, where they can be harvested for their spice. The Fremen are also trained to recognize the signs of sandworm activity, such as the appearance of "worm tracks" on the surface of the sand. |
| *"Why did Paul's mother disobey orders and bear a son?"* |
| Paul Atreides' mother, Lady Jessica, was a member of the Bene Gesserit, a powerful and secretive organization in the Dune universe. As a member of the Bene Gesserit, Lady Jessica was trained in physical and mental disciplines and was expected to follow the orders of the organization. However, she was also the personal concubine of Duke Leto Atreides and became pregnant with his son, Paul, despite orders from the Bene Gesserit not to bear children. Lady Jessica disobeyed these orders because she loved Duke Leto and wanted to have his child, and because she believed that Paul had the potential to be a special and important person. Despite the risks involved, Lady Jessica chose to bear a son and raised him according to the teachings of the Bene Gesserit, instilling in him the skills and knowledge he would need to survive in the dangerous and unpredictable world of Dune. |
| *"Does Paul have a sister?"* |
| Yes, Paul Atreides has a sister in the Dune novels. Her name is Alia Atreides, and she is the daughter of Duke Leto Atreides and Lady Jessica. Alia is born after her parents arrive on the planet Arrakis, also known as Dune, and is raised according to the teachings of the Bene Gesserit, an all-female organization that her mother belongs to. Alia is a precocious and intelligent child who possesses special abilities, including the ability to access the memories and skills of her ancestors. Like her brother, Paul, Alia is a key player in the events of the Dune novels and plays a significant role in the story. |
| *"What are Alia's powers?"* |
| Alia Atreides is a special and unique character in the Dune novels because she possesses a number of special abilities that set her apart from other people. One of her most notable abilities is the ability to access the memories and skills of her ancestors, which is a result of her mother, Lady Jessica, having taken the spice melange during pregnancy. This allows Alia to access the collective knowledge and experiences of her ancestors and to use them to her advantage. Alia is also highly intelligent and possesses advanced mental and physical skills, which she has been trained in by the Bene Gesserit, an all-female organization that her mother belongs to. In addition to these abilities, Alia also has enhanced senses and reflexes, and is capable of extraordinary physical feats. She is a formidable and formidable character in the Dune novels and plays a significant role in the story. |
| *"Can you tell me about Paul's wife?"* |
|Paul Atreides, the main character in the Dune novels, marries several times throughout the course of the story. One of his most notable wives is Chani, a native of the planet Arrakis and a member of the Fremen, the native population of the planet. Chani is a strong and capable woman who becomes Paul's closest ally and companion. She is fiercely loyal to Paul and helps him in his quest to take control of Arrakis and its valuable spice. Chani is a skilled fighter and is trained in the ways of the Fremen, and she plays a key role in helping Paul to lead the Fremen in their struggle against the Harkonnen, the sworn enemies of the Atreides family. Chani and Paul are deeply in love and have several children together, who play important roles in the events of the Dune novels. |
| *"Can you tell me about Paul's children?"* |
| Paul Atreides and his wife, Chani, have several children together in the Dune novels. Their first child is a son named Leto Atreides II, who is named after Paul's father, Duke Leto Atreides. Leto II is born on the planet Arrakis and is raised according to the teachings of the Fremen, the native population of the planet. Like his father, Leto II possesses special abilities and is destined to become a powerful and influential figure in the Dune universe. He goes on to play a significant role in the events of the Dune novels and becomes the central character in several of the sequels to the original novel.|
|Paul and Chani also have several other children together, including daughters named Ghanima and Irulan. Ghanima is born on Arrakis and is raised according to the Fremen way of life, while Irulan is born on Caladan, the ancestral home of the Atreides family. Both Ghanima and Irulan play important roles in the events of the Dune novels and go on to have significant impact in the story. |
| *"Tell me about Leto II, Ghanima, and Irulan."* |
| Leto II Atreides is the son of Paul Atreides and Chani and is the central character in several of the Dune novels. He is named after his grandfather, Duke Leto Atreides, and is raised according to the teachings of the Fremen, the native population of the planet Arrakis. Like his father, Leto II possesses special abilities and is destined to become a powerful and influential figure in the Dune universe. He becomes the ruler of Arrakis and the head of the Atreides family, and is known for his wisdom, strength, and honor. Leto II is a key player in the events of the Dune novels and his actions have a significant impact on the story.|
|Ghanima Atreides is the daughter of Paul Atreides and Chani and is born on the planet Arrakis. She is raised according to the Fremen way of life and is trained in their customs and traditions. Ghanima is a skilled fighter and possesses special abilities, including the ability to access the memories and skills of her ancestors. She plays an important role in the events of the Dune novels and goes on to have a significant impact on the story.|
|Irulan Atreides is the daughter of Paul Atreides and Chani and is born on the planet Caladan, the ancestral home of the Atreides family. She is raised according to the customs and traditions of the Atreides family and is well-educated and highly intelligent. Irulan is a key player in the events of the Dune novels and goes on to have a significant impact on the story. She is also the author of several books about the history and culture of the Dune universe and is a respected and influential figure in her own right. |
| *"What do you think of the newest movie of Dune?"* |
| I'm sorry, but I am a language model and do not have the ability to watch movies. I also have a knowledge cutoff date of 2021, so I am not aware of any movies or other adaptations of Dune that have been released after that time. However, I can tell you that Dune has been adapted into various media over the years, including movies, television shows, video games, and other works of fiction. Some of these adaptations have been well-received, while others have received mixed reviews. It would be up to individual viewers to decide whether or not they enjoyed any particular adaptation of Dune. |
| *"Thank you. You've been very helpful."*|
| You're welcome! I'm glad that I could help. If you have any other questions, please don't hesitate to ask. |

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[3e9d54628d...](https://github.com/cmss13-devs/cmss13/commit/3e9d54628d68fe91319ae87ad7ebd7aef9500811)
#### Saturday 2023-07-29 08:36:15 by Ben

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
## [CADindustries/toolcad-23](https://github.com/CADindustries/toolcad-23)@[b23efeb146...](https://github.com/CADindustries/toolcad-23/commit/b23efeb146a98db5d8c9eb392748013ee780ddeb)
#### Saturday 2023-07-29 08:45:07 by Airat

Removed previewWindow because of cringe competition fuck this shite, I should create my own SoftHub

---
## [ConsistencyPlus/Obsidian-Slabs](https://github.com/ConsistencyPlus/Obsidian-Slabs)@[874711520a...](https://github.com/ConsistencyPlus/Obsidian-Slabs/commit/874711520af1f7684eae0b012d946644c28d12bd)
#### Saturday 2023-07-29 08:45:30 by Siuol

"Carter is a bitch ass motherfucker he pushed my fucking Obsidian Slab"

---
## [Drulikar/cmss13](https://github.com/Drulikar/cmss13)@[ce09b07afd...](https://github.com/Drulikar/cmss13/commit/ce09b07afd0f8d433ffee1a43bc4dfeb978f45f1)
#### Saturday 2023-07-29 08:58:49 by ihatethisengine

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
## [gipawu/yuzu](https://github.com/gipawu/yuzu)@[8e703e08df...](https://github.com/gipawu/yuzu/commit/8e703e08dfcf735a08df2ceff6a05221b7cc981f)
#### Saturday 2023-07-29 09:00:07 by comex

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
## [AussieSpaceman/tgstation](https://github.com/AussieSpaceman/tgstation)@[41f20bc3ce...](https://github.com/AussieSpaceman/tgstation/commit/41f20bc3ced4e7853a09f2d5e1dcf46346f2e51f)
#### Saturday 2023-07-29 09:08:49 by LemonInTheDark

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
## [Steelpoint/cmss13](https://github.com/Steelpoint/cmss13)@[9c79c3af49...](https://github.com/Steelpoint/cmss13/commit/9c79c3af49ba90e18f85c1624ba4e80d608debf2)
#### Saturday 2023-07-29 10:40:10 by spartanbobby

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
## [Burnt-o/HaloCheckpointManager](https://github.com/Burnt-o/HaloCheckpointManager)@[e3a2acb096...](https://github.com/Burnt-o/HaloCheckpointManager/commit/e3a2acb096433fbc5fb7e4a20074375273635751)
#### Saturday 2023-07-29 11:09:53 by Burnt

This is a real in-the-weeds commit, I'm working thru a lot of issues rn. Cp dumping is kinda working, injection is not. My real struggle has been the rpc stuff, and the reason I'm committing this is that I think I want to change how I'm doing that. Right now interproc sets up an rpc server to comm with internal, but then needs to use callbacks to comm with external. Having this interproc middleman is giving me a huge headache, so I think I'll look to use some other rpc library where I can just setup the rpc server directly in external. Tho I'll still keep interproc around just for the dll injection functions.

Of course there's a million other things I need to fix too. I need to make internals optionstate events spawn on new threads to prevent blocking ui. I need to make gui elements aware of when their dependent services didn't setup successfully - I'll probably do some gamestate-templating shenanigans similar to cheatbase. Maybe have each gui element init the services too as it goes, so the ideally-supported-games comes from the gui instead of cheatmanager. Anyway I'm rambling

---
## [rdragan/tgstation](https://github.com/rdragan/tgstation)@[f44adfde1e...](https://github.com/rdragan/tgstation/commit/f44adfde1eaa96b5f565937423603580cb19b3a6)
#### Saturday 2023-07-29 12:11:26 by nikothedude

Refactors vendor tipping and adds 2 new malf modules: Remote vendor tipping, and the ability to roll around and crush anything in your path. (#76635)

## About The Pull Request

Title.

Vendor tipping code is now on /atom/movable, and any movable can fall
over like a vendor does. Things like crits have been moved to
type-specific availability tables, their effects are now held in their
own proc, are now random per crushed item, have probability weights,
etc.

In the process of making this PR I also had to fix another issue, where
a bunch of take_damage() overrides had incorrect args, so that explains
the take_damage changes I made.

Tipping now also attacks any atoms on the target, given they use
integrity.

Adds 2 new malf modules.

1. REMOTE VENDOR TIPPING: A mid-cost and mid-supply module allows malf
AIs to remotely tip a vendor in any of the 8 directions. After 0.5
seconds of delay and a visual indicator (along with other warnings), the
vendor falls over.
1.1. In the process of making this I had to expand a arrow sprite to
have orthogonal directions, which is why you may see the testing dmi
being changed.
2. CORE ROLLING: A mid-cost but low-supply ability that allows the AI to
roll around and crush anything it falls on, including mobs. This has a
5% chance to have a critical hit so it isnt THAT terrible - plus it's
guaranteed to never stunlock. It's real utility lies in the fact the AI
now has limited movement without borgs. Also, the psychological factor.

As a bonus, vendor tipping now uses animate and transforms instead of
replacing matrices.
## Why It's Good For The Game

1. Generifying vendor tipping code is just good, period. It's a very
wacky and silly little piece of code that really doesn't need to be
isolated to vendors exclusively. ANY big and heavy object can fall over
and do a ton of damage.
1.1. Also, adding weights to critical hits is really good, because it
lets things like the headgib finally be a lot less terrifying, as
they're a lot less likely to happen.

2. Remote vendor tipping is a bit of a goofy ability that isn't really
THAT practical but has a chance of catching someone unaware and doing
some serious damage to that person alone.
2.1. Atop of this, vendor tipping isn't that loud of an action as say,
blowing things up, or doing a plasma flood. Even overrides aren't this
silent or a non-giveaway. A vendor falling on someone, though, is a
mundane thing that happens a lot. This is a decent way to assassinate
people before going loud (or at least, damage people) that isn't offered
yet.

4.
3.1. For real though, AIs rolling around is just fucking hilarious. The
ability to move isn't offered right now (which isn't that much of a bad
things), but with sufficiently limited charges (or limits to how many
times you can buy the ability), this can be a funny little t hing that
lets the AI potentially hide somewhere on the sat (or just relatively
close to the sat, such as engineering [it can't go through the
teleporter with this but it can go through transit tubes]) without the
need for borgs.
3.2. Also, it lets the AI sacrifically execute people by blowing up
their brains.

---
## [rdragan/tgstation](https://github.com/rdragan/tgstation)@[cc57581b73...](https://github.com/rdragan/tgstation/commit/cc57581b73e2979d775dfd9408978e4987b6635b)
#### Saturday 2023-07-29 12:11:26 by Sealed101

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
## [chizzy376/TerraGov-Marine-Corps](https://github.com/chizzy376/TerraGov-Marine-Corps)@[ca4b66185f...](https://github.com/chizzy376/TerraGov-Marine-Corps/commit/ca4b66185ffa363692529f8340a43cccab02cbf1)
#### Saturday 2023-07-29 12:14:52 by chizzy376

Gives the Umbilical Tad shutters on side windows. (#13490)

* y

* Update combat_patrol.dm

* Update combat_patrol.dm

Sometimes I think about if life is really worth the hassle, if I really have to deal with so much bs only to then have to believe hard enough to get into heaven. Am I a good person for heaven? Do I deserve it? fuck if i know

* Finish fixing my fuckup

---
## [zydras/Skyrat-tg](https://github.com/zydras/Skyrat-tg)@[2f2ec4b9d6...](https://github.com/zydras/Skyrat-tg/commit/2f2ec4b9d64c448e5b544ecbcdca42a7dae0f094)
#### Saturday 2023-07-29 13:22:53 by SkyratBot

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
## [arinc9/linux](https://github.com/arinc9/linux)@[fcfe2abf25...](https://github.com/arinc9/linux/commit/fcfe2abf25b97f09a0a8f75f8ef3ef782571af21)
#### Saturday 2023-07-29 13:22:59 by Yury Norov

sched/topology: add for_each_numa_{,online}_cpu() macro

for_each_cpu() is widely used in the kernel, and it's beneficial to
create a NUMA-aware version of the macro to improve on node locality..

Recently added for_each_numa_hop_mask() works, but switching existing
codebase to using it is not an easy process.

New for_each_numa_cpu() is designed to be similar to the for_each_cpu().
It allows to convert existing code to NUMA-aware as simple as adding a
hop iterator variable and passing it inside new macro. for_each_numa_cpu()
takes care of the rest.

At the moment, we have 2 users of NUMA-aware enumerators. One is
Melanox's in-tree driver, and another is Intel's in-review driver:

https://lore.kernel.org/lkml/20230216145455.661709-1-pawel.chmielewski@intel.com/

Both real-life examples follow the same pattern:

	for_each_numa_hop_mask(cpus, prev, node) {
 		for_each_cpu_andnot(cpu, cpus, prev) {
 			if (cnt++ == max_num)
 				goto out;
 			do_something(cpu);
 		}
		prev = cpus;
 	}

With the new macro, it would look like this:

	for_each_numa_online_cpu(cpu, hop, node) {
		if (cnt++ == max_num)
			break;
		do_something(cpu);
 	}

Straight conversion of existing for_each_cpu() codebase to NUMA-aware
version with for_each_numa_hop_mask() is difficult because it doesn't
take a user-provided cpu mask, and eventually ends up with open-coded
double loop. With for_each_numa_cpu() it shouldn't be a brainteaser.
Consider the NUMA-ignorant example:

	cpumask_t cpus = get_mask();
	int cnt = 0, cpu;

	for_each_cpu(cpu, cpus) {
		if (cnt++ == max_num)
			break;
		do_something(cpu);
 	}

Converting it to NUMA-aware version would be as simple as:

	cpumask_t cpus = get_mask();
	int node = get_node();
	int cnt = 0, hop, cpu;

	rcu_read_lock();
	for_each_numa_cpu(cpu, hop, node, cpus) {
		if (cnt++ == max_num)
			break;
		do_something(cpu);
 	}
	rcu_read_unlock();

The latter looks more verbose and avoids from open-coding that annoying
double loop. Another advantage is that it works with a 'hop' parameter with
the clear meaning of NUMA distance, and doesn't make people not familiar
to enumerator internals bothering with current and previous masks machinery.

Signed-off-by: Yury Norov <yury.norov@gmail.com>

---
## [ruvn-1fgas/white](https://github.com/ruvn-1fgas/white)@[b80c09c566...](https://github.com/ruvn-1fgas/white/commit/b80c09c566adc9607b577a11ae0bd95580f4bf5c)
#### Saturday 2023-07-29 13:40:35 by Valtos

fuck this hud fuck you jannies fuck everyone fuck fuck fuck fuck

---
## [HWSensum/Fluffy-Frontier-Sensum](https://github.com/HWSensum/Fluffy-Frontier-Sensum)@[9e523715ac...](https://github.com/HWSensum/Fluffy-Frontier-Sensum/commit/9e523715acd373ce1a74bdc8f9c2fe422c2ad61e)
#### Saturday 2023-07-29 13:42:04 by SkyratBot

New planetary exclusive random event/unfavorable situation, Chasmic Earthquake [MDB IGNORE] (#21778)

* New planetary exclusive random event/unfavorable situation, Chasmic Earthquake (#75864)

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

* New planetary exclusive random event/unfavorable situation, Chasmic Earthquake

---------

Co-authored-by: Rhials <Datguy33456@gmail.com>

---
## [B--B/android_kernel_xiaomi_sdm710](https://github.com/B--B/android_kernel_xiaomi_sdm710)@[6ca94e39e3...](https://github.com/B--B/android_kernel_xiaomi_sdm710/commit/6ca94e39e361d4e683650937b71ed8db40785332)
#### Saturday 2023-07-29 13:45:32 by Dave Chiluk

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
Change-Id: I7d7a39fb554ec0c31f9381f492165f43c70b3924
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
Signed-off-by: Marco Zanin <mrczn.bb@gmail.com>

---
## [thwompa/cmss13](https://github.com/thwompa/cmss13)@[cb855f807b...](https://github.com/thwompa/cmss13/commit/cb855f807b4f5538d623e78363e76aabd5f8d80a)
#### Saturday 2023-07-29 13:48:59 by forest2001

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
## [Hamed-Hasan/shofy-ecommerce-client](https://github.com/Hamed-Hasan/shofy-ecommerce-client)@[d4f289f713...](https://github.com/Hamed-Hasan/shofy-ecommerce-client/commit/d4f289f71303ae01048c341de2ef322bf1b60eff)
#### Saturday 2023-07-29 14:56:02 by John Doe

feat: Add powerful features and updates to Shofy eCommerce app

In this commit, we've introduced a range of exciting features and enhancements to the Shofy eCommerce web application. The updates include:
- Implemented dynamic Next.js for improved performance and scalability.
- Enhanced backend with robust Express.js for efficient data handling.
- Integrated MongoDB with Mongoose for seamless application data modeling.
- Added secure and reliable payment options through Stripe integration.
- Implemented user authentication with Google login and email verification.
- Introduced Redux Toolkit for efficient state management.
- Implemented fast data fetching and caching with RTK Query.
- Leveraged TypeScript + Next.js for more reliable codebase.
- Ensured responsive and touch-friendly design for optimal user experience.
- Improved form validation and utilized Bootstrap 5 framework.

Additionally, we've introduced several powerful additional features to enhance the eCommerce experience:
- Variation Swatch for captivating product pages.
- Pagination, Filters by Size & Color for improved user experience.
- Video Gallery for detailed product views.
- Sale Countdown Timer to increase engagement.
- Product Quick View and Quantity Select for convenience.
- Google and Email Password-based Authentication for secure accounts.
- User Profile and Information Update for easy data management.
- Powerful Payment Gateway Integration using Stripe for seamless transactions.

Thank you for choosing Shofy! We hope you enjoy the new features. If you have any questions or encounter any issues, feel free to reach out to our support team at swe.hamedhasan@gmail.com.

Happy selling! 🚀🛍️

---
## [eskolnik/townsquare](https://github.com/eskolnik/townsquare)@[974bbb1a0f...](https://github.com/eskolnik/townsquare/commit/974bbb1a0f35ab2a3333ba2a28955956e24fd900)
#### Saturday 2023-07-29 14:59:36 by Dae Lorant

Updated night order for all roles

Updated night order for all roles to match the order at https://script.bloodontheclocktower.com/data/nightsheet.json

Some noticeable changes:
- Legion was moved much earlier in the order of demons (relevant if a another demon is made in a legion game, you can keep it around and kill it with legion before it kills on a subsequent night)
- Amnesiac was moved much later in night order (a more reasonable place for the most common type of amni abilities)
- Magician was given a night order for N1
- Pixie was given a night order for other nights

---
## [c0ntradicti0n/dialectics](https://github.com/c0ntradicti0n/dialectics)@[1b92049c58...](https://github.com/c0ntradicti0n/dialectics/commit/1b92049c5832a7ae6e1f6cdd31984a08b3a2bff4)
#### Saturday 2023-07-29 15:05:36 by c0ntradicti0n

Automated Commit: 2/2/1/3/2/.Style.md 1/2/1/2/2/.Growth.md 3/3/3/3/_Tonic-Dominant.md 2/3/3/1/1/.Physics.md 3/3/3/2/3/.Scale.md 3/1/1/1/_Individual-Collective.md 3/1/2/1/_Mono-Poly.md 3/1/1/3/2/.Community.md 2/2/3/2/3/.Desire.md 2/3/3/3/_Theory-Practice.md 3/3/1/1/1/.Pattern.md 3/3/2/1/2/.Low.md 2/2/2/1/2/.Provocation.md 2/2/3/3/2/.Adaptation.md 2/3/1/3/3/.Galaxies.md 2/3/3/2/1/.Ideology.md 1/2/1/3/2/.Moment.md 2/1/3/3/1/.Benevolence.md 3/2/2/1/3/.Data.md 2/3/1/3/1/.Stars.md 3/1/3/2/2/.Break.md 2/2/3/1/2/.Repulsing.md 3/2/2/1/1/.Observation.md 2/1/1/1/1/.Rule.md 3/1/1/3/3/.Society.md 2/1/2/1/2/.Guilt.md 1/2/1/1/2/.Age.md 2/3/3/3/3/.Proficiency.md 3/1/3/2/3/.Interrupt.md 2/1/3/1/3/.Discrimination.md 3/1/1/2/3/.Truth.md 3/3/3/1/1/.Scale.md 2/2/1/1/2/.Aversion.md 3/1/2/3/_Here-There.md 3/3/1/3/_Harmony-Disharmony.md 3/3/1/1/2/.Sequence.md 3/3/3/3/3/.Atonality.md 2/1/3/2/1/.Equity.md 2/1/1/1/_Permission-Prohibition.md 1/2/1/2/3/.Prediction.md 3/3/1/1/3/.Cycle.md 3/3/3/2/1/.Key.md 3/3/1/3/1/.Chord.md 2/2/2/1/1/.Offensive.md 2/1/3/2/_Fairness-Prejudice.md 2/3/3/2/3/.Epistemology.md 2/2/2/1/3/.Desecration.md 3/1/3/1/3/.Tempo.md 2/2/1/1/_Repulsive-Attractive.md 2/1/1/3/2/.Jurisdiction.md 2/2/1/2/1/.Pleasure.md 3/1/1/2/2/.Reason.md 3/1/1/1/3/.Identity.md 3/3/2/1/_Frequency-Wavelength.md 2/1/2/1/_Harm-Benefit.md 3/1/1/1/1/.Self.md 3/3/2/2/3/.Polyphony.md 3/3/3/2/_Home-Away.md 3/3/2/2/1/.Tone.md 2/1/2/3/_Obligation-Freedom.md 1/2/1/2/_Change-Stagnation.md 3/2/2/3/_Compare-Contrast.md 3/3/2/2/2/.Overtones.md 2/1/3/1/_Prejudice-Fairness.md 2/2/3/3/_Balance-Imbalance.md 3/1/2/1/2/.Resonance.md 3/3/3/1/_Transposition-Modulation.md 3/1/2/1/3/.Tone.md 3/1/2/3/2/.Direction.md 2/2/1/1/3/.Repugnant.md 2/2/1/2/3/.Delight.md 2/2/3/2/_Attraction-Rejection.md 3/3/1/2/2/.Harmony.md 3/3/3/3/2/.Tonality.md 2/2/3/3/1/.Stability.md 2/3/3/3/1/.Craft.md 3/3/2/1/3/.Octave.md 3/2/2/2/_Objective-Subjective.md 2/1/2/3/2/.Duty.md 1/2/1/1/1/.Yesterday.md 2/3/3/1/2/.Chemistry.md 2/1/3/2/2/.Impartiality.md 2/1/3/3/_Fairness-Inequality.md 3/3/1/1/_Repeat-Vary.md 3/3/3/2/2/.Accidentals.md 3/3/1/3/2/.Consonance.md 2/1/2/1/3/.Punishment.md 2/2/1/3/3/.Trends.md 1/2/1/3/3/.Occurrence.md 2/2/1/2/2/.Attraction.md 3/1/1/1/2/.Consciousness.md 2/2/2/3/2/.Balance.md 2/3/3/2/_Belief-Knowledge.md 3/1/3/2/1/.Pause.md 2/1/2/2/2/.Merit.md 3/2/2/1/_Objective-Subjective.md 2/2/3/1/1/.Repellant.md 2/1/1/1/2/.Transgression.md 2/2/2/3/3/.Peace.md 2/3/3/1/_Theory-Practice.md 3/1/3/1/2/.Rhythm.md 3/3/3/1/3/.Tuning.md 2/2/3/1/3/.Distancing.md 2/2/2/3/_Stability-Imbalance.md 1/2/1/1/3/.History.md 3/1/1/2/1/.Logic.md 2/1/2/3/3/.Responsibility.md 3/1/2/3/1/.Location.md 3/1/3/1/1/.Pulse.md 3/3/2/3/3/.Brightness.md 2/1/1/1/3/.Consequence.md 2/1/2/1/1/.Evil.md 3/1/2/3/3/.Space.md 2/3/3/3/2/.Skills.md 2/2/2/3/1/.Calming.md 3/3/1/2/_Tone-Untone.md 3/2/2/2/3/.Theory.md 2/1/2/2/_Benefit-Harm.md 2/3/1/3/2/.Planets.md 3/2/2/3/2/.Correction.md 2/2/3/2/1/.Temptation.md 3/1/3/2/_Sounding-Silent.md 2/2/3/1/_Rejection-Attraction.md 2/1/3/1/1/.Inequality.md 2/3/3/1/3/.Biology.md 3/2/2/3/1/.Critique.md 2/2/1/3/1/.Art.md 3/1/2/1/1/.Frequency.md 2/1/1/3/_Law-Anarchy.md 1/2/1/1/_Old-New.md 2/2/1/2/_Attractive-Repulsive.md 3/3/2/3/1/.Texture.md 2/1/2/2/3/.Reward.md 3/3/1/2/1/.Note.md 2/1/3/1/2/.Bias.md 2/1/2/3/1/.Right.md 2/2/2/1/_Harsh-Soft.md 2/2/3/2/2/.Longing.md 3/3/2/1/1/.High.md 2/3/3/2/2/.Metaphysics.md 3/2/2/2/1/.Logic.md 2/1/3/3/3/.Equality.md body.md" 2/1/3/3/2/.Justice.md 1/2/1/3/_Instant-Eternity.md 2/1/1/3/1/.Legislation.md 3/1/1/3/_Individual-Collective.md 3/2/2/2/2/.Hypothesis.md 3/1/3/1/_Slow-Fast.md 3/3/2/3/2/.Resonance.md 3/3/2/3/_Soft-Hard.md 2/3/1/3/_Macro-Micro.md 1/2/1/3/1/.Today.md 2/2/1/1/1/.Disgust.md 2/2/1/3/_Classic-Modern.md 3/2/2/1/2/.Experiment.md 3/3/1/3/3/.Dissonance.md 3/3/3/1/2/.Key.md 3/3/3/3/1/.Mode.md 1/2/1/2/1/.Tomorrow.md 2/1/1/3/3/.Enforcement.md 3/3/1/2/3/.Melody.md 3/1/1/2/_False-True.md 3/1/1/3/1/.Group.md 2/2/3/3/3/.Homeostasis.md 3/2/2/3/3/.Improvement.md 2/1/2/2/1/.Good.md 2/1/3/2/3/.Neutrality.md 3/3/2/2/_Macro-Micro.md

---
## [c0ntradicti0n/dialectics](https://github.com/c0ntradicti0n/dialectics)@[b067c9b44b...](https://github.com/c0ntradicti0n/dialectics/commit/b067c9b44bca0e3a7f7b736dba4361ef8b25266f)
#### Saturday 2023-07-29 15:05:36 by c0ntradicti0n

Automated Commit: 1/3/1/.Idea.md 2/2/2/.Ugliness.md 3/.Anthropology.md Theory.md" 1/3/1/.Speculation.md 2/2/1/.Repulsion.md 3/3/1/.Sound.md 2/1/3/3/.Equity.md 2/1/2/2/.Moral.md 3/2/.Linguistics.md 3/_Silence-Noise.md 3/3/3/.Harmony.md 2/2/_Negative-Positive.md 3/_Individual-Community.md 3/1/.Sound.md 1/3/3/.Theory.md 3/3/2/.Note.md 2/1/3/1/.Unfair.md 2/2/1/.Beauty.md 3/3/2/.Melody.md 3/3/1/.Rhythm.md 3/2/.Note.md 2/2/2/.Attraction.md 1/3/_Concrete-Abstract.md 1/3/.Logic.md 2/2/.Aesthetics.md 1/3/2/.Practice.md 2/2/3/.Balance.md Science.md" theory.md" 3/3/.Sounds.md 2/1/3/2/.Fair.md 1/3/2/.Evaluation.md 3/3/_Tone-Pitch.md 3/3/_Beat-Pattern.md 2/2/_Fear-Desire.md 1/3/3/.Confirmation.md 2/2/3/.Sublime.md 1/3/_Complexity-Simplicity.md 2/1/2/1/.Immoral.md 2/1/2/3/.Morality.md 2/2/.Sublime.md

---
## [CyanMatter/atlas-2023](https://github.com/CyanMatter/atlas-2023)@[e348042f1c...](https://github.com/CyanMatter/atlas-2023/commit/e348042f1c3bb42abe2a720c1c88100843b2ba31)
#### Saturday 2023-07-29 15:05:56 by Cyan

Replace description of Germany x The Netherlands Kabedon

The current description is meant to be funny, not informative. The two jokes in it are copied comments from a Reddit post; and the statement that the line about 'Duitsland-san' is on the canvas is inaccurate. Half of the description is dedicated to explaining one of the jokes.

This commit proposes to replace the description to include an description of kabedon, the PlaceDE & PlaceNL collaboration, and a visual summary of the boy and the girl.

---
## [PastelPrinceDan/Skyrat-tg](https://github.com/PastelPrinceDan/Skyrat-tg)@[9701b40ca0...](https://github.com/PastelPrinceDan/Skyrat-tg/commit/9701b40ca03e164bd8bd4238fafb6cf778c52efe)
#### Saturday 2023-07-29 15:51:54 by SkyratBot

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
## [visionvault/visionaryGPT](https://github.com/visionvault/visionaryGPT)@[e014b3f8e8...](https://github.com/visionvault/visionaryGPT/commit/e014b3f8e827e7769d9fb3bca97ab12001c07209)
#### Saturday 2023-07-29 15:52:25 by visionvault

Create askcicero.py

If you're looking to enhance your impromptu speaking skills and unleash the power of persuasive rhetoric, I have some interesting news for you!

The next historical personality to be brought to life using Generative AI is 'Cicero', the master orator. I am one of those people who is not great at impromptu speaking. I have been trying to improve it over the past few years and thanks to some wonderful mentors at Toastmasters International, I have learned immensely. What if using Generative AI, you too can have someone like Cicero as a mentor?

Launching 'AskCicero' – a Gen AI app that brings the wisdom of Cicero to your fingertips! With the power of large language models, this app will analyze your speech and provide feedback just like the great orator himself.

Whether you're a seasoned speaker seeking to refine your craft or someone who wants to excel at impromptu speaking, 'AskCicero' is your ultimate mentor. 

How it works:

1.Read topic presented at the top of the screen and hit record.
2.Let your thoughts flow as you speak your mind.
3.End the recording and submit your speech.

In no time, you'll receive an in-depth evaluation report crafted with Cicero's legendary 'five canons of rhetoric': Invention, Arrangement, Style, Memory, and Delivery. Discover your strengths and areas for improvement, tailored to your unique speaking style.

Let 'AskCicero' be your guide on the path to becoming a compelling speaker! Join the journey now, and leave a lasting impression with every word you speak.

---
## [zoton2/LiveSplit.Scripts](https://github.com/zoton2/LiveSplit.Scripts)@[1be3ab24d6...](https://github.com/zoton2/LiveSplit.Scripts/commit/1be3ab24d6723a326cfe619e7cda40cdeaeccf19)
#### Saturday 2023-07-29 15:54:50 by Random-Machine

Update LiveSplit.WatchDogs2.asl to Percentage Autosplitter

Makes the autosplitter more robust by using a new percentage variable to split for individual missions. Also adds a lot of options. 

1. Must have No Compromise and Human Conditions DLC uninstalled for the percentages to match up. Must also follow the speedrun route in the WR.
2. Only works on latest patch.
3. Has options for splitting after Walk in the Park, Sunday Schooled, and Mark Up, but they're disabled by default. 
4. Removed old follower count variable & splitting.
5. Still have to manual split for the last split when completing Motherload.
6. Supports splitting for individual missions and has options to disable them.
7. Does not support splitting for these individual missions/cutscenes & call(s) because there isn't much point:
-Intro mission/stuff before Walk in the Park (Buy Pants option was removed.)
-Newly Dawned (False Profits)
-ICU (Wrench Cutscene at start of Heist Sweet Heist)
-Zero Days (Heist Sweet Heist)
-Trouble at Home (Looking Glass)
-Second Wind (Alphabet Soup)
-Nine Lives (Hacker War)
-Café Culture (W4tched)
-The Waiting Game (Hack teh World)
-Spinal Tap (Shanghaied)
-Social Media and the Congressman (Power to the Sheeple)
-Like Minds (Robot Wars)
-Motherload Call (for mission to show up)

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[20aaf9b197...](https://github.com/treckstar/yolo-octo-hipster/commit/20aaf9b1977f7921748cc54c3a4de85dc72a163c)
#### Saturday 2023-07-29 17:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [CenkTheRaptor/Bubberstation](https://github.com/CenkTheRaptor/Bubberstation)@[a6763aee3e...](https://github.com/CenkTheRaptor/Bubberstation/commit/a6763aee3e8ab0c8f42325a75be42adf172a12ad)
#### Saturday 2023-07-29 17:30:42 by BurgerLUA

Hugboxes pierced realities (#281)

## About The Pull Request

- Pierced realities no longer gib your entire head when you click on
them with TK.
- Pierced realities no longer dismember your arms when you click on them
without TK.
- Pierced realities no longer make you want to die when you examine them
(still give drain bamage).

## Justification

New players won't get baited into clicking on the pierced reality. This
is funny, but it's just annoying for medical.
Veteran players won't get baited into clicking on the pierced reality
with TK because they're curious to see what would happen.
The mood debuff is ultimately pointless and no one ever takes it
seriously anyways.

## Changelog

:cl: BurgerBB
del: Hugboxes pierced realities by removing some non-heretic
functionality.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [leicester70/very-big-spring-boot-idk-lol](https://github.com/leicester70/very-big-spring-boot-idk-lol)@[13577fe338...](https://github.com/leicester70/very-big-spring-boot-idk-lol/commit/13577fe338999fe834721fff8c4edef42072e1af)
#### Saturday 2023-07-29 17:50:00 by leicester70

more souts more souts more souts and refactored package path.
It works half-ass as fuck, i have two alrms now but it kinda just died halfway waiting for the next alarm

---
## [TypeVar/Shiptest](https://github.com/TypeVar/Shiptest)@[f07cb3bd3b...](https://github.com/TypeVar/Shiptest/commit/f07cb3bd3b52bfbdb7994aaf4ae68dcf90d57d2f)
#### Saturday 2023-07-29 19:12:31 by Bjarl

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
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[1fe7b10e33...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/1fe7b10e339ea0d6a3d49f864e1badc5c831e791)
#### Saturday 2023-07-29 19:25:18 by SkyratBot

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
## [CliffracerX/Skyraptor-SS13](https://github.com/CliffracerX/Skyraptor-SS13)@[daa33d89fe...](https://github.com/CliffracerX/Skyraptor-SS13/commit/daa33d89fef10650f89f7db160f110141ab99e5d)
#### Saturday 2023-07-29 20:00:42 by IndieanaJones

Xenomorph/Alien Rework 2023: Part 1 (#75286)

## About The Pull Request

Alternative to #75277

Kept you waiting, huh?

This PR is the first part of a Xenomorph rework which seeks to make the
big lugs more balanced and up to date with /tg/'s current design. This
mainly involves curtailing xenomorph's infamous hardstuns into more
interactive forms of combat, while also giving some buffs to the
xenomorph's more unique abilities in order to keep them threatening.

Part 1 will focus on simple number changes and some simple mechanic
changes. In the future, changes will be made to endgame involving
xenomorphs, along with changes to other facets of Xenomorphs.

Highly based off of #55937.

Changes:

- Xenomorph disarm has been completely reworked. While a disarm will
attempt to, well, disarm, a human opponent should they be holding
something, it will no longer immediately hardstun targets when they
aren't. Instead, the xenomorph will shove the target several tiles back
and inflict 35 stamina damage. If the target slams into a wall, this
will also come with the added effect of knocking them down. If a human
is incapacitated, however, right click will slam them into the ground,
which paralyzes them for a lengthy 5 seconds (which is ultimately half
the time xenos could stun you for before), allowing for safe transport
back to the nest as long as you keep them close.

- Humans can now shove xenomorphs. Due to being the superior predator,
however, you can't knock down xenomorphs from shoving. You can slow them
for a little bit akin to humans though.

- Neurotoxin no longer is a hardstun. Instead, it deals 50 stamina
damage on contact. It is still resisted by BIO armor.

**HUNTER:**
- Speed reduced from -1 to -0.3.
- Pounce speed is twice as fast as before (1 to 2)
- Hardstun time on pounce reduced from 10 seconds to 5 seconds.

Hunters being insanely fast has been a major balance-ruining factor of
xenomorphs for many years now. These buggers could practically ambush
anyone, hardstun them immediately, and then leave before anyone could do
anything. Now, with their speed nerfed and in combination with the xeno
shove changes, hunters will need to spend more time to down a target.
Their pounce was practically useless, so its been sped up in order to
make it more practical to use.

**SENTINEL**
- Speed reduced from 0 to 0.2
- Cloak alpha reduced from 0.75 to 0.25 (you're more hidden now)

Sentinels receive a large nerf in regards to their spit, but their
before useless cloaking ability has been greatly improved upon as
compensation. They now serve better as defenders and ranged ambushers.

**XENOMORPH DRONE**
- No changes

As in the original PR, drones are perfeclty balanced in my eyes, so no
changes were required.

**XENOMORPH PRAETORIAN**
- Speed increased from 1 to 0.5
- No changes

Praetorians get affected by the nerfs of the other xeno abilities, but
now they're a bit faster in order to close the gap to use their
abilities.

**XENOMORPH QUEEN**
- Speed increased from 3 to 2
- Health increased from 400 to 500
- Damage increased from 20 to 50

Xenomorph queens have been sped up and made more tanky and lethal in
close-range combat. Fighting this beast up-close should be a death
sentence to almost anything else in the game. Speed increases will help
her re-position and close the gap on potential prey.

**OTHER CHANGES**
- Fixed a bug where simplemobs didn't actually use xenomorph's damage
values when they were attacked by them.

## Why It's Good For The Game

Xenomorphs are old, and haven't been updated for quite a long time. This
has left them as sources of a bunch of hardstuns which made counterplay
from a modern spaceman extremely difficult. With these changes, fighting
xenomorphs is more interactive and should end up being more enjoyable
for both crew and xenos. Buffs were also given out to incentivize usage
of xenomorph's unique abilities as opposed to the standard disarm spam
which was most effective for them until now.

## Changelog
:cl:
balance: Xenos have been rebalanced, removing their hardstuns on their
disarm and neurotoxin, along with a slew of other changes. Xenos have
received buffs to their more unique abilities in return.
fix: Fixed simplemobs ignoring xenomorph's melee damage values when
being attacked by them.
/:cl:

---
## [selliott512/freedoom](https://github.com/selliott512/freedoom)@[8c076fcba9...](https://github.com/selliott512/freedoom/commit/8c076fcba9bb94637d22431b21b862a481fff01f)
#### Saturday 2023-07-29 20:42:03 by mc776

levels: minor Phase 2 fixes. (#964)

* levels: minor Phase 2 fixes.

Mostly for addressing #694.

Map05
Realigned grey hex textures around soulsphere switch. Now the odd one out is the door.

Map09
Fixed up the lighting in the start room.
Reflagged some secret doors as secret rather than hidden.
Consolidated the two W1 Floor to LAC triggers around the yellow key.
The red key rocket launcher sequence could potentially mess someone up who - given the hatchling closet, quite reasonably - avoids grabbing the rocket launcher. It seems needlessly convoluted, but it is a funny prank how the switch makes the red key disappear entirely for a bit. Instead of untangling this I'm just going to add some health bonuses around the rocket launcher so the player will eventually go there.
Tried to mitigate the worst of the various crimes against texture alignment in the crate maze, adding a light source in the process. It would take a *lot* of work to make it actually look good, a lot more than can be done in a batch bugfix PR.

Map10
Lower unpegged sector 70 (red door leading outside) door tracks.
Added matching midtexes to the insides of the fences around the lights by the door leading to the final corridor.
Line 839 (south-southeast red armour behind waterfall) flagged secret and the lines on the other side flagged hidden.

Map11
Realigned grey hexes in corridor around minigunner switch room.
Added an evil eye right in front of the shootwall secret.

Map12
Change line 330 midtex to the new MIDSPCSM with no offset.
Lower-unpegged line 4787 doortrack.

Map13
Sectors 243 no longer uses mismatching TLITE6_5 flat. (Sector 170 actually looks okay ingame.)
Realigned line 260.

Map15
Line 163 W1 changed to WR to prevent a potential softlock.
Aligned COMPSPAN on sector 561 to match surroundings.
Fixed some textures in the green corridor in the west overlooking the nukage. Also set those zombies in there to ambush since that seems to be the intention based on their placement, and made that big block thingy on the east end of that corridor a more normal-looking door.
Touched up greyhex near sector 491.
Flagged linedef 5293 secret.
Sectors 145 and 116 (rock fringe around nukage around red key platform) consolidated into one sector, made non-damaging, and without the invisible blocking lines.

Map16
Changed Line 1089 to SR instead of S1. (Switch that opens the secret to the east)
Realigned all the SUPPORT3s in that little painlord corridor while shrinking the "ribs" a bit; also widened the little exit atrium so the space between the lights is as wide as the door. (After looking at the others I am not going to widen any more corridors at this time.)
Grossly simplified the twisty yellow key corridor, and lowered the ceiling of the outside of the door so the yellow door stripe would fit properly. One doortrack needed to be given the DOORTRAK texture. The remaining "ribs" are recessed further inside the wall so they do not impede movement at all.
Lowered the ceiling above the other yellow marked door as well. The corridor around the corner has been expanded slightly.

Map22
Flagged line 830 secret.

Map23
Fixed candle placement on east end of zombieman corridor.
Consolidated some identical sectors around the big "AGM" floor and lowered the torch platforms so they wouldn't clip into the ceiling.
Raised the ceilings on the techpillars right after the first long lift. The walls in front of them now match their surroundings.
Removed lower unpegged from lines 2066, 2082, 2062, 2075. ("Door"tracks for the route across those pillars in the southeast - they're actually lifts not doors)
SSG secret fixed. (And marked.)

Map28
Lines 2326, 622 lagged secret.
Realigned lines 4594 and 4671.
Realigned scrolling textures around sector 517.
Touched up monster closet around sector 399, changing to to 8 about HAF fast and making the closet a bit taller so there'd be a better natural threshold between those areas. The doortracks were fine, if a bit complex.
Raised sector 474 ceiling to match marble brick seams.
Made sector 147 (cubes hanging over hot rocks) do damage and sectors 91 and 115 (teleport pads) not.

Map29
Swapped out the textures on the sides of the big green skull pad.

* levels: fix up map23 southeast secret textures.

I messed up the texture replacement around the green torch, the extreme sudden darkness ruined the blue AGM text, the pillar lift-doors needed a better division between the tekwall and red rock, and that huge swathe of DOORTRAK hurt to look at in vanilla.

* levels: map07 aesthetic fixes.

Replaced BIGDOOR1 on sector 50 as it was giving tutti-frutti.

Fixed the textures on the lifts in the green area beyond the outdoor area.

Miscellaneous texture alignment fixes and added some more thresholds between materials.

---
## [Moemiset/TsholofeloM](https://github.com/Moemiset/TsholofeloM)@[24f2cccaec...](https://github.com/Moemiset/TsholofeloM/commit/24f2cccaecc902bd376a5ca131e126e742e28011)
#### Saturday 2023-07-29 21:11:27 by Moemiset

Add files via upload

MyStudentLife Your All-in-One Solution for Seamless Student Living

Are you a student residing in school accommodation? Look no further! We are thrilled to present to you the ultimate companion for your student life - the MyStudentLife application. This innovative app is meticulously designed to provide you with a seamless living experience, offering access management, bus trip monitoring, emergency support, and essential services information at your fingertips.

Key Features:

1. Access Management:
No more fumbling with physical keys or access cards! Our app revolutionizes the way you enter and exit your school residence. With a simple tap on your smartphone, you can unlock your dormitory door securely. The app also allows authorized personnel, such as resident assistants and staff, to grant access permissions and maintain a secure living environment.

2. Bus Trip Monitoring:
Say goodbye to uncertainty about bus schedules! Our app integrates real-time bus tracking, enabling you to stay informed about the arrival and departure times of school buses. Never miss a bus again, and efficiently plan your trips to and from the campus.

3. Emergency Numbers:
Your safety is our top priority. In any unforeseen situation, MyStudentLife provides quick access to essential emergency numbers, including campus security, medical services, and local authorities. Rest assured, help is just a tap away.

4. Water and Electricity Services:
Managing utilities should never be a hassle. We simplify the process by providing up-to-date information on water and electricity services. Stay informed about any scheduled maintenance, outages, or important announcements, ensuring you have continuous access to essential utilities. Loading of prepaid electricity and water all at your finger tips

5. Announcements and Events:
Stay connected and engaged with your school community through our app's announcement and events section. Get notified about campus events, workshops, seminars, and important announcements from the university and residence management, fostering a vibrant and inclusive living experience. Linked to Blackboard and other services.

6. Community Forum:
Connect and collaborate with your fellow residents using the community forum feature. Share information, seek advice, and build a supportive network with your peers, creating a sense of belonging and camaraderie.

7. Personalized Settings:
MyStudentLife is tailored to suit your preferences. Customize notifications, choose your preferred language, and set your time zone for a personalized experience that meets your needs.

MyStudentLife we understand the importance of a conducive and comfortable living environment for your academic success. My app is designed to enhance your living experience, simplify everyday tasks, and foster a secure and thriving community within your school residence.

The exciting journey of enhanced student living! MyStudentLife gives you the full school residence experience. Live smarter, safer, and stay connected like never before!

---
## [navithedragon/navithedragon](https://github.com/navithedragon/navithedragon)@[bb9d8ad4fa...](https://github.com/navithedragon/navithedragon/commit/bb9d8ad4fa4957d55f585f6e29f2f0e82d70eafb)
#### Saturday 2023-07-29 21:13:31 by Navi

Update README.md

shitty website not allowing cross site embeds fuck you

---
## [Moemiset/TsholofeloM](https://github.com/Moemiset/TsholofeloM)@[9b39456b6c...](https://github.com/Moemiset/TsholofeloM/commit/9b39456b6cb227527e61a6b3b40d4871423d7cd9)
#### Saturday 2023-07-29 21:35:20 by Moemiset

Add files via upload

User-friendly Municipality Water Management Application – the ultimate solution for enhancing the efficiency, accessibility, and convenience of water services, public transportation, and emergency assistance in the city. With a focus on modernizing urban living, our application offers a seamless experience for residents, businesses, and municipal authorities alike.

Key Features:

1. Water Services Access: Say goodbye to long queues and frustrating paperwork! Our application empowers residents to effortlessly access and manage their water services. Users can check their water bills, view consumption patterns, and make online payments securely with just a few taps.

2. Electricity Services: In addition to water services, our application also integrates electricity services. Users can monitor their energy consumption, review billing information, and even set up automated payment options, ensuring a hassle-free experience with their electricity usage.

3. Public Transportation Monitoring: Keeping track of bus schedules and routes has never been easier. Our app provides real-time bus tracking, allowing commuters to plan their journeys more efficiently. Receive live updates on bus locations, estimated arrival times, and any route changes to minimize wait times and optimize travel routes.

4. Emergency Contact Numbers: Safety is paramount. The application features a dedicated section for essential emergency contact numbers. Residents can quickly access police, fire, medical, and other important services in times of need, enabling a prompt response to emergencies.

5. Service Requests and Complaints: With our application, reporting issues or requesting services is a breeze. Users can submit service requests or complaints directly through the app, streamlining communication with the municipality and expediting resolution times.

6. Notifications and Alerts: Stay informed with timely notifications and alerts. Whether it's an impending water outage, bus delays, or critical municipal updates, our app ensures that users are always up-to-date with the latest information.

7. User-Friendly Interface: Designed with simplicity in mind, our application offers an intuitive and user-friendly interface. Residents of all ages and technical abilities can easily navigate through its features, making it accessible to everyone in the community.

8. Secure Data Protection: We understand the importance of data privacy. Our app adheres to the highest security standards, safeguarding user information and financial transactions through advanced encryption measures.

Municipal services and transportation options into a single, comprehensive platform, our Municipality Water Management Application revolutionizes urban living. It enhances citizen-government interactions, optimizes resource allocation, and fosters a sustainable and smart city ecosystem.

Building a smarter, more connected municipality for all.

---
## [ZachLegros/quant_service_data_aggregator](https://github.com/ZachLegros/quant_service_data_aggregator)@[99a2cf2e38...](https://github.com/ZachLegros/quant_service_data_aggregator/commit/99a2cf2e385b1bff5ae7c1db1c6978f3f56c5a9d)
#### Saturday 2023-07-29 21:47:45 by Zach Legros

HOLY FUCK THIS WAS LONG AND PAINFUL I HATE/LOVE WEBPACK AND NODEJS AND TYPESCRIPT.

---
## [InsightfulParasite/lobotomy-corp13](https://github.com/InsightfulParasite/lobotomy-corp13)@[171b1478f9...](https://github.com/InsightfulParasite/lobotomy-corp13/commit/171b1478f9d01a40841ca0bb131394fe8a2039b2)
#### Saturday 2023-07-29 22:54:32 by vampirebat74

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

