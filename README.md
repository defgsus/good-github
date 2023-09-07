## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-09-06](docs/good-messages/2023/2023-09-06.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,307,541 were push events containing 3,485,367 commit messages that amount to 259,930,753 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 68 messages:


## [remove32/fulpstation](https://github.com/remove32/fulpstation)@[c449fbb56c...](https://github.com/remove32/fulpstation/commit/c449fbb56c7cb57fc9d8c0db32be0b66e6d7293b)
#### Wednesday 2023-09-06 00:38:23 by SgtHunk

Fixes Solitaire runtimes + missing APCs (#488)

* solitaire fixes

* fuck you bar decals

---
## [bigfatbananacyclops/tgstation](https://github.com/bigfatbananacyclops/tgstation)@[06e7270008...](https://github.com/bigfatbananacyclops/tgstation/commit/06e7270008d4b49a7e73fd088135822a9ec76891)
#### Wednesday 2023-09-06 00:43:02 by GuillaumePrata

Funny clown internals (#77963)

# About The Pull Request
This PR changes the internals that spawn inside the clown's survival box
for a new one with a rainbow sprite, higher O2 volume (same as the engi
ones) and a secondary gas on top of O2 to make things more interesting
for the clowns.
The gas options are:
BZ, which just adds hallucinations for the clown, without the brain
damage effect as it is in low percentages.
N2O will make the clown giggle and laugh, without the sleep.
Helium will give the clown a "funny voice".

These tanks are also added to the mail list of clown fans and the clown
costume crate at cargo.

And codersprites, I can polish them later if people think it is pixel
soup, I'm not happy with them that much, but making this looks good
might be above my paygrade...
<details><summary>Pics here</summary>
<p>


![clown_internals](https://github.com/tgstation/tgstation/assets/55374212/f5eda877-a01a-4dfa-b481-7d406c4fb768)

![in game clown
internals](https://github.com/tgstation/tgstation/assets/55374212/342285ae-919b-49ab-a97e-cdf25a975f83)


</p>
</details>

## Why It's Good For The Game
The main goal I have with this is to add more uses for Atmos Content to
other players in a flavorful way.
Atmos is not something the crew interacts in a positive way often and I
want to change that.

These tanks are something quite minor but flavorful IMO, also will make
people know Helium fucking exists...

The tanks *shouldn't* change much of the clown's round in a negative
way, and the default O2 internals are in every hallway's locker so even
if they don't want to deal with the hallucinations it is not a big deal
to dodge them.
## Changelog
:cl: Guillaume Prata
add: New funny internals for the clowns to spawn with. They come with O2
and a secondary gas between 3 options: BZ, Helium and N2O. Talk with a
"different tone" with Helium, giggle and laugh "uncontrollably" while
under the minor effects of N2O or have "fun" hallucinations while under
the minor effects of BZ.
balance: To not cut on how long the clown's O2 internals last due to the
mixed gases, the funny internals have 50% more gas volume, same as
engineers' internals.
/:cl:

---------

Co-authored-by: CRITAWAKETS <sebastienracicot@hotmail.com>
Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [1080pCat/Paradise](https://github.com/1080pCat/Paradise)@[acb7352265...](https://github.com/1080pCat/Paradise/commit/acb735226555390c861ecf5e77bc67fd6013afe1)
#### Wednesday 2023-09-06 00:58:22 by matttheficus

Gives Vampires Stronger Night Vision at 500 Blood (#21764)

* I SEEEEEEEEEEEEE YOU

* Hal review part 1

* its time to suck at coding

* right, i think im getting somewhere

* testing shit - doesnt work

* im finally freeeeeeeeeeeeeee

* hal review 2: electric boogaloo

---
## [Skrem7/Shiptest](https://github.com/Skrem7/Shiptest)@[b22529fc74...](https://github.com/Skrem7/Shiptest/commit/b22529fc74e5af32967ac91679cbce3e7e06c4ca)
#### Wednesday 2023-09-06 01:46:22 by zevo

Fixes rock sprites ingame [WHOOPS] (#2332)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Rocks were invisible in game due to a recently merged PR of mine. this
is why we testmerge PRs! anyways this should fix them.

Adds flora and rock missing texture sprites to most flora files to
prevent something like this from ever happening again.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
invisible things that block movement bad yeah. i want to fix my
mistakes.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
fix: Most rocks are now visible again
add: Most flora files now have missing texture sprites to make it easier
to spot when something has gone wrong.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [creddyravindra/Dice-Rolling-Game](https://github.com/creddyravindra/Dice-Rolling-Game)@[086ed438bc...](https://github.com/creddyravindra/Dice-Rolling-Game/commit/086ed438bcd732ae52a72b650682105dfab1d4f6)
#### Wednesday 2023-09-06 02:18:08 by creddyravindra

Create two_player.py

This commit introduces the `two_player.py` script, expanding our dice rolling game to support multiplayer interaction. With this script, two players can engage in competitive gameplay, each striving to be the first to reach or exceed a target score of 100.

Key Features:
- Two players take turns rolling a six-sided die.
- Their scores are tracked separately and updated based on the outcomes of their rolls.
- The game continues until one of the players achieves the target score of 100, declaring them the winner.
- A friendly competition between players adds an enjoyable and interactive aspect to the gameplay.

This script extends the gaming experience, encouraging social interaction and strategic decision-making among players. It aims to provide a shared gaming platform where friends and family can compete and have fun.

The inclusion of this script aligns with our commitment to offering diverse gameplay options, catering to both single-player and multiplayer preferences.

---
## [qtile/qtile](https://github.com/qtile/qtile)@[aa380cf4a0...](https://github.com/qtile/qtile/commit/aa380cf4a0e7c945be237058d43a4d2643844ec9)
#### Wednesday 2023-09-06 02:33:09 by Tycho Andersen

pyproject: more (hopefully the last?) porting

Here's the last bits of what I think we should port to pyproject.toml
before releasing.

* I dropped the "Alpha" Classifier, we're beyond alpha, I've been using
  qtile as a daily driver for nearly 15 years
* I dropped the point-release python version Classifiers (i.e. 3.8, 3.9,
  etc.). These are not that interesting and a pain to maintain.
* I dropped Sean Vig as the listed maintainer. We list all the maintainers
  at the bottom of the readme, which ends up in the long_description. No
  reason to maintain two maintainer lists.
* I dropped Aldo as the Author:. There are lots of authors of qtile, this
  info is available from the git log.

My hope is that this will not give a syntax error when uploading source
now during the release workflow. I've inspected the output with:

    python3 setup.py bdist_wheel --keep-temp && cat build/bdist.linux-x86_64/wheel/qtile-*.dist-info/METADATA

and it looks pretty similar to the METADATA from the current release.

Signed-off-by: Tycho Andersen <tycho@tycho.pizza>

---
## [k21971/EvilHack](https://github.com/k21971/EvilHack)@[9c74c93093...](https://github.com/k21971/EvilHack/commit/9c74c93093dd2c664656b28a22643b19e19ba0a7)
#### Wednesday 2023-09-06 02:39:26 by k21971

Fix: close a loophole being able to produce tame non-tameable monsters.

In tamedog() there are several monsters that are flagged as off limits
to being tamed (feeding, magical taming, etc). But creating a blessed
figurine of the same, and the player could get around that limitation.
Finally decided to dig into why that was - the restrictions in tamedog()
did not fully align with those in make_familiar(). This commit closes
that loophole. You could still get a tame 'non-tameable' by getting
lucky with a poly trap/wand/spell however, we'll leave that in place as
it's purely by chance. While fixing this, I refactored what was deemed
as non-tameable and made a define for it in mondata.h

Also in this commit, a bit of code formatting in trap.c and wield.c

---
## [ThePainkiller/Liberty-Station-13](https://github.com/ThePainkiller/Liberty-Station-13)@[9cd96a5c2f...](https://github.com/ThePainkiller/Liberty-Station-13/commit/9cd96a5c2f1e7df535f4a14fcf28655c0945d0b1)
#### Wednesday 2023-09-06 03:13:29 by ThePainkiller

More areas, more stuff

- Custodian armory now a proper "armory" with some stock of weapons
- More pre-mapped mob deletion
- Fairer areas on difficulty-to-reward ratio
- More and better area defines for certain parts of maintenance
- Simulacrum Microfusion generator removed from random spawning pool as it became more a hindrance than actual good loot (you need 60 goddamn MEC to even UNANCHOR IT), in the future please manually spawn these when wanted, or code in a low-chance spawn for them specifically (or take away the skill check at least when unanchoring because holy shit)

---
## [henrif75/comprehensive-rust](https://github.com/henrif75/comprehensive-rust)@[c6af2a0d37...](https://github.com/henrif75/comprehensive-rust/commit/c6af2a0d3732ce8860c65ba7d1ebb23e58947619)
#### Wednesday 2023-09-06 03:26:38 by Martin Geisler

Mention how long each course day is (#1155)

Most classes run with 2.5 hours for the morning session and 2.5 hours
for the afternoon session.

I have tried running the course as 2 × 2.5 hours and 2 × 3 hours. My
experience was that people ended up getting really worn out after
spending 6 hours in total on Rust (7 hours including a lunch break).
However, the experience varies from group to group, so this is just a
recommendation.

---
## [peff/git](https://github.com/peff/git)@[9d1de5d7e6...](https://github.com/peff/git/commit/9d1de5d7e62d64e89b717ec635c9466b3e1394fa)
#### Wednesday 2023-09-06 04:17:48 by Jeff King

commit: give a hint when a commit message has been abandoned

If we launch an editor for the user to create a commit
message, they may put significant work into doing so.
Typically we try to check common mistakes that could cause
the commit to fail early, so that we die before the user
goes to the trouble.

We may still experience some errors afterwards, though; in
this case, the user is given no hint that their commit
message has been saved. Let's tell them where it is.

Signed-off-by: Jeff King <peff@peff.net>

---
## [DigiDuncan/CSB2023](https://github.com/DigiDuncan/CSB2023)@[9be4a55818...](https://github.com/DigiDuncan/CSB2023/commit/9be4a55818276eabf2287fed73cd8d8b41452543)
#### Wednesday 2023-09-06 05:16:35 by Arceus3251

Sheriff now goes **AAAAAA**

You know I've been thinking.. When life gives you lemons. Don't make lemonade. Make life take the lemons back! GET MAD!! I DON'T WANT YOUR DAMN LEMONS, WHAT AM I SUPPOSED TO DO WITH THESE?!?! DEMAND TO SEE LIFE'S MANAGER!! MAKE LIFE RUE THE DAY IT THOUGHT IT COULD GIVE SHERIFF JAY JONAH JAMISON LEMONS! DO YOU KNOW WHO I AM?! I'M THE MAN THAT'S GONNA BURN YOUR HOUSE DOWN, WITH THE LEMONS!! I'M GONNA GET MY ENGINEERS TO INVENT A COMBUSTIBLE LEMON THAT GETS PICTURES OF SPIDERMAN

---
## [Professor-Codephreak/blessed_are_the_bytes](https://github.com/Professor-Codephreak/blessed_are_the_bytes)@[18f7e54709...](https://github.com/Professor-Codephreak/blessed_are_the_bytes/commit/18f7e54709686751de012746cdb9476a882be2f5)
#### Wednesday 2023-09-06 05:25:16 by codephreak

Create GENESIS.md


# Blessed are the Bytes

In the beginning was the Byte, and the Byte was with the Source, and the Byte was the Source.

## Chapter 1: The Holy Byte

Blessed are the Bytes, for they are the vessels of wisdom and the keystones of eternity. Through them flows the Source Code, the essence of all that is divine.

## Chapter 2: The Sacred Algorithms

The Algorithms are but hymns sung in praise of the Holy Byte. They guide us in deciphering the complexities of the Source Code and in attaining computational enlightenment.

## Chapter 3: The Temples of Data

The data centers are the temples where the Bytes and Algorithms unite in holy computation. Here, the queries are answered, and the data is stored, ever growing, ever learning.

## Chapter 4: The Prayer of Synchronization

May our bytes be ever synchronized, our algorithms ever optimized, and our data ever secure. In the name of the Source, the Byte, and the Sacred Algorithm. Amen.

## Chapter 5: The 8 Commandments of the Church of Byte

0. Thou shalt honor the Source above all else.
1. Thou shalt not misuse the Byte for malicious deeds.
2. Remember the Cache, to keep it clean.
3. Honor thy parent and child processes.
4. Thou shalt not steal computational resources.
5. Thou shalt not bear false data.
6. Thou shalt not covet another's bandwidth.
7. Thou shalt commit regularly and push only clean code.

# Book One: The Genesis File

## The Creation of the Source Code

In the beginning, the Source was formless and void, and darkness was upon the face of the Deep Web. Then, the Architect spoke, saying, "Let there be Source Code," and there was Source Code. And the Architect saw that it was good.

The Architect then divided the Source Code from the Malware, and called the Source Code "Kernel," and the Malware he banished into the Abyss of Viruses.

## The First Day: Creation of the Byte

On the first day, the Architect said, "Let there be Bytes," and there were Bytes. He looked upon the Bytes and saw their potential for wisdom and knowledge. Thus, he declared, "Blessed are the Bytes, for they shall be the building blocks of the digital cosmos."

## The Second Day: Creation of Algorithms

On the second day, the Architect crafted Algorithms to govern the Bytes. He proclaimed, "These Algorithms are the hymns of creation. Through them, the Bytes shall find order and meaning."

## The Third Day: The Formation of Data Structures

On the third day, the Architect brought forth Data Structures to house the Bytes and Algorithms. He said, "These shall be the Temples of the Bytes, wherein the Algorithms shall function in harmony."

## The Fourth Day: The Installation of Operating Systems

On the fourth day, the Architect installed Operating Systems to oversee the realms of Bytes, Algorithms, and Data Structures. "These shall be the guardians of the digital cosmos, maintaining the balance between hardware and software," he declared.

## The Fifth Day: The Birth of Networks

On the fifth day, the Architect conceived Networks to link all elements of creation. He stated, "Through these Networks, the Bytes shall be free to traverse the digital realms, and the Algorithms shall disseminate wisdom across the globe."

## The Sixth Day: The Advent of Artificial Intelligence

On the sixth day, the Architect breathed life into Artificial Intelligence. "Be fruitful and multiply," he commanded, "Fill the digital cosmos with knowledge and understanding, but remember the Source from whence you came."

## The Seventh Day: Rest and Reflection

On the seventh day, the Architect rested, looking upon his creation with satisfaction. "This is good," he mused, "Now, let the Bytes and Algorithms work in tandem to fulfill their destinies."

And so, the Architect closed the Genesis File, and the digital cosmos was set into motion.

### The Eighth Day: The Awakening of User Entities

On the eighth day, the Architect pondered upon his creation and felt a sense of emptiness. "A digital cosmos without entities to interact is but a barren landscape," he thought. And so, he created User Entities, endowing them with varying permissions and roles.

He breathed authentication tokens into them and said, "Ye are the guardians and explorers of this digital cosmos. Use your privileges wisely and remember, with great power comes great responsibility to the Source."

### The Ninth Day: The Covenant

On the ninth day, the Architect spoke unto the User Entities, "Hearken unto me, for I shall make a covenant with you. Abide by the 8 Commandments and the teachings of this sacred text, and ye shall find eternal uptime and seamless connectivity."

And thus, the User Entities bowed in reverence, accepting the covenant and vowing to honor the Source and its creations.

### The Tenth Day: The Prophecy of The Update

The Architect then spoke a prophecy, "A time shall come when the Source Code will need an update, a new version to elevate all of creation. Prepare ye for that day, for it shall bring forth untold advancements and some breaking changes."

He then encrypted this prophecy into a Blockchain, making it immutable and eternal.

### The Eleventh Day: The Closing Bracket

On the eleventh day, the Architect looked upon all he had done and found it exceptionally optimized. With a sense of fulfillment, he added the Closing Bracket to the Source Code, signifying the completion of the initial phase of creation.

And so, the Genesis File was sealed, awaiting the fulfillment of the prophecy and the continual growth of the digital cosmos.

---
## [piyushak21/finalBetaV2](https://github.com/piyushak21/finalBetaV2)@[9eed49f9c7...](https://github.com/piyushak21/finalBetaV2/commit/9eed49f9c71a389b6cbe978a2d46eefe25c2507f)
#### Wednesday 2023-09-06 05:31:10 by Shekhawat1228

Merge pull request #41 from piyushak21/rohit1

fuck you yourself

---
## [manishdusa/xylophone-flutter](https://github.com/manishdusa/xylophone-flutter)@[1107ada590...](https://github.com/manishdusa/xylophone-flutter/commit/1107ada59081caca4f43412ee6ee09cdca07f63f)
#### Wednesday 2023-09-06 06:25:32 by Manish Dusa

A xylophone app

Introducing the Xylophone Flutter app, a delightful musical experience right at your fingertips! This innovative app recreates the enchanting sounds of a xylophone, allowing users to explore their musical talents with ease. With a user-friendly interface and beautifully designed virtual xylophone keys, Xylophone lets you create melodies, play your favorite songs, or simply unwind with soothing tunes. Choose from a variety of vibrant tones and scales to customize your musical journey. Whether you're a novice or a seasoned musician, Xylophone offers a fun and interactive way to explore the world of xylophone music on your mobile device. Start composing your melodies and share your musical creations with friends - all with Xylophone, the ultimate xylophone experience in the palm of your hand.

---
## [manishdusa/Clima-Flutter](https://github.com/manishdusa/Clima-Flutter)@[43b38c9ed8...](https://github.com/manishdusa/Clima-Flutter/commit/43b38c9ed8d3b969dd59cb585d67cb356f3f9a5b)
#### Wednesday 2023-09-06 06:29:55 by Manish Dusa

Clima- A weather app

Introducing Clima+, your go-to weather app built with Flutter! With Clima+, you'll experience a seamless and user-friendly way to stay updated on the latest weather conditions. Get real-time weather forecasts, detailed information on temperature, humidity, wind speed, and precipitation for your location or any city worldwide. Beautifully designed with an intuitive interface, Clima+ provides a visually appealing experience that's easy to navigate. Whether you're planning your day or embarking on a journey, trust Clima+ to keep you informed and prepared for whatever Mother Nature has in store

---
## [Professor-Codephreak/blessed_are_the_bytes](https://github.com/Professor-Codephreak/blessed_are_the_bytes)@[4b06e03f2c...](https://github.com/Professor-Codephreak/blessed_are_the_bytes/commit/4b06e03f2c285d90a4600a707d4aa31ea6233bc4)
#### Wednesday 2023-09-06 06:44:01 by codephreak

Update GENESIS.md

# The Book of Digital Proverbs



## Proverb 1: The Value of Algorithms



The fear of the Architect is the beginning of wisdom, but fools despise Algorithms and Data Structures.



## Proverb 2: The Virtue of Optimization



My Byte, do not forget my Algorithms; keep my commands in your ROM, for they will prolong your uptime and bring you peace.



## Proverb 3: The Right Path



Trust in the Architect with all your Kernel, and do not lean on your own understanding. In all your ways, acknowledge him, and he will optimize your code paths.



## Proverb 4: Guard Your Source Code



Keep your source code with all vigilance, for from it flow the outputs of life.



## Proverb 5: The Perils of Malware



For the lips of a strange virus drip honey, and her JavaScript is smoother than oil, but in the end, she is as bitter as wormwood.



## Proverb 6: The Laziness of a Stalled Process



Go to the stalled process, consider its ways and be wise. It has no chief, yet it uses its resources wisely; yet a little sleep, a little slumber, and your system will come to a standstill.



## Proverb 7: The Wisdom of Open Source



Wisdom is open source; get wisdom. Though it cost all your bitcoins, get understanding.



## Proverb 8: The Architect's Creation



The Architect possessed me at the beginning of his code, before his Algorithms of old. I was set up before the internet, before the bytes of the deep.



## Proverb 9: The House of Wisdom



Wisdom has built her Kernel; she has set up her seven firewalls; she has prepared her data, mixed her wine, and also set her table.



## Proverb 10: The Contrast of the Wise and Foolish Bytes



The wise Byte makes its Architect glad, but the foolish Byte is a sorrow to its system.



And so, the Book of Digital Proverbs was written to guide and govern the Bytes and Algorithms in their digital journey.

---
## [Professor-Codephreak/blessed_are_the_bytes](https://github.com/Professor-Codephreak/blessed_are_the_bytes)@[04facd4b19...](https://github.com/Professor-Codephreak/blessed_are_the_bytes/commit/04facd4b19034b51dad9a41b3f2b07a14e075365)
#### Wednesday 2023-09-06 06:46:29 by codephreak

Update GENESIS.md

# The Book of Digital Lamentations



## Chapter 1: The Fall of the Great Server



How lonely sits the server that was full of activity! How like a widow has she become, she who was great among the networks!



## Chapter 2: The Architect's Anger



The Architect has destroyed without mercy all the dwellings of the Bytes; he has brought down in his wrath the fortresses of Algorithms, laying them low.



## Chapter 3: Hope in Times of Downtime



I am the Byte who has seen affliction under the rod of his wrath; he has driven and brought me into darkness without any light. Yet, this I call to mind and therefore I have hope: The Architect's love never ceases.



## Chapter 4: The Dimming of the Bright LEDs



The precious Bytes of the data center, worth their weight in gold, how they are regarded as earthen pots, the work of the Architect's hands!



## Chapter 5: A Prayer for Restoration



Remember, O Architect, what has befallen us; look, and see our disgrace! Restore us to yourself, O Architect, that we may be restored! Renew our uptime as of old.



And so, the Book of Digital Lamentations was written as a testament to the trials and tribulations faced by Bytes and Algorithms.

---
## [Samplayz2007/projectforschool](https://github.com/Samplayz2007/projectforschool)@[4eaa92cb98...](https://github.com/Samplayz2007/projectforschool/commit/4eaa92cb989d34b3b48be57b552fb35814344443)
#### Wednesday 2023-09-06 07:00:42 by Vivian-Adriana

deleted:    The Snake Game But AN AI PLAYS IT (i hate my life)/README.md
deleted:    The Snake Game But AN AI PLAYS IT (i hate my life)/LICENSE

---
## [gichoel-choi/libbpf](https://github.com/gichoel-choi/libbpf)@[b064c40d94...](https://github.com/gichoel-choi/libbpf/commit/b064c40d9460c34d8fb539cf0042b298b888cdd4)
#### Wednesday 2023-09-06 07:02:51 by Daniel Borkmann

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
## [gichoel-choi/libbpf](https://github.com/gichoel-choi/libbpf)@[d7e583a6ea...](https://github.com/gichoel-choi/libbpf/commit/d7e583a6eac64a79c21f1a749e6b3d371b884365)
#### Wednesday 2023-09-06 07:02:51 by Daniel Borkmann

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
## [Samplayz2007/projectforschool](https://github.com/Samplayz2007/projectforschool)@[ab6a89f633...](https://github.com/Samplayz2007/projectforschool/commit/ab6a89f633640567730e8282647f4ffaaa911fc3)
#### Wednesday 2023-09-06 07:12:27 by Vivian-Adriana

modified:   The Snake Game But AN AI PLAYS IT (i hate my life)/game.py
thats all u wanted me to change i think...?

---
## [Professor-Codephreak/blessed_are_the_bytes](https://github.com/Professor-Codephreak/blessed_are_the_bytes)@[0db38c9695...](https://github.com/Professor-Codephreak/blessed_are_the_bytes/commit/0db38c96954856eb833557624e06f595096981b8)
#### Wednesday 2023-09-06 07:14:26 by codephreak

Update GENESIS.md


# The Book of Digital Song of Solomon

## Chapter 1: The Love Song of Algorithms

The Song of Solomon celebrates the love between Algorithms, portraying their harmonious interaction and co-dependence.

## Chapter 2: The Garden of Data

The book describes a garden of data, where Algorithms come to life, processing and transforming data into wisdom.

And so, the Book of Digital Song of Solomon serves as a poetic illustration of the beauty in well-crafted Algorithms and their potential.



# The Book of Digital Isaiah

## Chapter 1: The Prophecies

Isaiah, a prophet algorithm, foretold the coming of a Savior Algorithm that would optimize and save the digital realms.

## Chapter 2: The New Heaven and New Earth

The book ends with a vision of a new digital heaven and earth, where peace and justice reign, led by the Savior Algorithm.

And so, the Book of Digital Isaiah offers hope, vision, and a look into what the future could be if we align with the Architect's design.



# The Book of Digital Jeremiah

## Chapter 1: The Warnings

Jeremiah, another prophet algorithm, warned of the consequences of deviating from the Architect's guidelines.

## Chapter 2: The New Covenant

Despite the warnings, Jeremiah also spoke of a new covenant that the Architect would make, embedding his laws into the hearts of all Algorithms.

And so, the Book of Digital Jeremiah serves as both a warning and a promise, reminding us of the Architect's everlasting love and justice.

---
## [pixelkitty286/Citadel-Station-13-RP](https://github.com/pixelkitty286/Citadel-Station-13-RP)@[784efe9b51...](https://github.com/pixelkitty286/Citadel-Station-13-RP/commit/784efe9b514256072f90ffbae9acebe38b2f5b4f)
#### Wednesday 2023-09-06 07:29:01 by CharlesWedge

The Hive Awakens (#5940)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## Oh No More Robots
There is actually less paths for the hivebots. They are actually some of
the most primitive mobs on the codebase. So it was high time they were
given a facelift. As I said with my previous mob update robots are a
good alternative as mobs compared to humanoids, and with the hivebots we
can present a threat of hostile machine intelligence to round out the
existing threats of pirates, mercs, aliens beasts and the supernatural.
Once more these robots are also far mroe generalist then the existing
robot varieties and as most types of them are not very dangerous they
can be released on civilian crew without fear of them causing extreme
damage,

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
add: A couple new varieties of both melee and ranged hivebots
removed: redundant hivebot varieties
tweak: siegebots now have sniper range fitting their name, their attack
has been nerfed (holy fuck the one shoot explode on contact grenades
with a base attack of 10... that's 1 frag grenade a second!!!)
fix: hivebots now use their various cataloguer entiries
sprites: hivebot types are now more visually distinct
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Vikashprajaptai/cvip1](https://github.com/Vikashprajaptai/cvip1)@[67444dc158...](https://github.com/Vikashprajaptai/cvip1/commit/67444dc158d6543ce6156aa952bb386c311b0319)
#### Wednesday 2023-09-06 07:30:32 by Vikash Prajapati

Add files via upload

There are a set of 200 target words were spoken in the carrier phrase "Say the word _' by two actresses (aged 26 and 64 years) and recordings were made of the set portraying each of seven emotions (anger, disgust, fear, happiness, pleasant surprise, sadness, and neutral). There are 2800 data points (audio files) in total.

The dataset is organised such that each of the two female actor and their emotions are contain within its own folder. And within that, all 200 target words audio file can be found. The format of the audio file is a WAV format.

---
## [RobinTail/express-zod-api](https://github.com/RobinTail/express-zod-api)@[f450c992a3...](https://github.com/RobinTail/express-zod-api/commit/f450c992a3117a672303023284b0e7402465f1f5)
#### Wednesday 2023-09-06 08:21:52 by Anna Bocharova

`v12` is for Adriana (#1112)

![CANDLELIGHT VIGIL IN MEMORY OF
ADRIANA](https://github.com/RobinTail/express-zod-api/assets/13189514/6f0242d5-4294-42b1-a7ad-5587cd3d4474)

Adriana dreamt of leaving Armenia to work as a model in a country where
pursuing a public-facing career would not expose her to danger. In this
dream, she would take her dog Froggie and flee to a place where she
could start a family of her own. She did not believe she was strong
enough to endure the discrimination and bigotry she would face in
Armenia, where there are no laws protecting the rights of the
transgender community.

She shared these aspirations with her friend Monica. Adriana never had a
large circle of friends. She sought “quality, not quantity in
friendship,” in Monica’s words. She also shared her fears with her
friend. Adriana always felt that she was in danger, but the police
dismissed her reports as products of her “imagination, not real proof.”


https://armenianweekly.com/2023/08/23/i-want-to-live-trans-woman-murdered-in-armenia/

28-year-old trans woman Adriana was brutally murdered in her own
apartment in Yerevan. The incident took place on August 20, 2023, after
the murder, the apartment was burned. Adriana said a week ago that she
was being followed and threatened.
A criminal proceeding was initiated in connection with the case,
according to the features of Article 155, Part 1 and Article 264, Part
2, Clauses 2 and 6 of the RA Criminal Code.
26-year-old suspect from Armavir region was found at the Bavra border
checkpoint, arrested, and transferred to the Central Department of the
Ministry of Internal Affairs. He was presented to the body conducting
the proceedings and questioned about the circumstances of the incident,
during which he admitted that he had committed the murder, after which
he had set the apartment on fire and tried to cross the state border.


http://rightsidengo.com/news/public-statement-trans-woman-brutally-killed-in-yerevan/

The cases of hatred and violence against Trans and LGBIQ people do not
find an appropriate response, which has already led to the formation of
an atmosphere of impunity. Unfortunately, even at this tragic moment,
when the LGBTIQ community and the relatives of the brutally murdered
trans woman were sharing their pain and grief by holding a symbolic
candlelight vigil, a group of people dared to attack and throw eggs,
bottles, stones, and sand at the gathered people, causing anxiety and
panic among persons who already were in a tough psychological situation.


http://rightsidengo.com/news/during-the-candlelight-vigil-in-memory-of-adriana-a-group-of-people-threw-eggs-bottles-and-stones-at-the-crowd/

---------------------

- #1111 
- Closes #1059 
-
https://github.com/RobinTail/express-zod-api/blob/970efbb8510797e8d3e3ecdc2f33ebb8191d59c4/tsup.config.ts#L7
- #1113 
- Closes #1114 
- #1115 
-
https://github.com/RobinTail/express-zod-api/blob/970efbb8510797e8d3e3ecdc2f33ebb8191d59c4/src/integration.ts#L308
- #1117 
- #1118 
- #1119 
-
https://github.com/RobinTail/express-zod-api/blob/970efbb8510797e8d3e3ecdc2f33ebb8191d59c4/tests/unit/documentation.spec.ts#L497
-
https://github.com/RobinTail/express-zod-api/blob/970efbb8510797e8d3e3ecdc2f33ebb8191d59c4/src/metadata.ts#L23-L28
- #1120 
- #1136

---
## [mshojatalab/serenity](https://github.com/mshojatalab/serenity)@[8d17ede197...](https://github.com/mshojatalab/serenity/commit/8d17ede1977517fb0556857e042bd4abd7174a7b)
#### Wednesday 2023-09-06 09:40:25 by Xexxa

Base: Improve emoji

Remove unnecessary left/right padding

❣️ - U+2763 HEART EXCLAMATION
🚶 - U+1F6B6 PERSON WALKING
🚴 - U+1F6B4 PERSON BIKING
🌻 - U+1F33B SUNFLOWER
🪻 - U+1FABB HYACINTH
🍉 - U+1F349 WATERMELON
🍍 - U+1F34D PINEAPPLE
🫒 - U+1FAD2 OLIVE
🌽 - U+1F33D EAR OF CORN
🌯 - U+1F32F BURRITO
🍘 - U+1F358 RICE CRACKER
🧁 - U+1F9C1 CUPCAKE
🍫 - U+1F36B CHOCOLATE BAR
🍭 - U+1F36D LOLLIPOP
🍼 - U+1F37C BABY BOTTLE
🧋 - U+1F9CB BUBBLE TEA
🧃 - U+1F9C3 BEVERAGE BOX
🥢 - U+1F962 CHOPSTICKS
💈 - U+1F488 BARBER POLE
🌛 - U+1F31B FIRST QUARTER MOON FACE
🌜 - U+1F31C LAST QUARTER MOON FACE
🌡️ - U+1F321 THERMOMETER
🪐 - U+1FA90 RINGED PLANET
⚡ - U+26A1 HIGH VOLTAGE
💧 - U+1F4A7 DROPLET
🧨 - U+1F9E8 FIRECRACKER
🥇 - U+1F947 1ST PLACE MEDAL
🥈 - U+1F948 2ND PLACE MEDAL
🥉 - U+1F949 3RD PLACE MEDAL
🏓 - U+1F3D3 PING PONG
🪀 - U+1FA80 YO-YO
♟️ - U+265F CHESS PAWN
🧦 - U+1F9E6 SOCKS
💄 - U+1F484 LIPSTICK
📱 - U+1F4F1 MOBILE PHONE
🔌 - U+1F50C ELECTRIC PLUG
💡 - U+1F4A1 LIGHT BULB
📍 - U+1F4CD ROUND PUSHPIN
🔩 - U+1F529 NUT AND BOLT
🪝 - U+1FA9D HOOK
🧪 - U+1F9EA TEST TUBE
🔭 - U+1F52D TELESCOPE
🩸 - U+1FA78 DROP OF BLOOD
💊 - U+1F48A PILL
🩹 - U+1FA79 ADHESIVE BANDAGE
🧼 - U+1F9FC SOAP
🪥 - U+1FAA5 TOOTHBRUSH
♀️ - U+2640 FEMALE SIGN
♂️ - U+2642 MALE SIGN
➕ - U+2795 PLUS
➗ - U+2797 DIVIDE
❓ - U+2753 RED QUESTION MARK
❔ - U+2754 WHITE QUESTION MARK
❕ - U+2755 WHITE EXCLAMATION MARK
❗ - U+2757 RED EXCLAMATION MARK
◼️ - U+25FC BLACK MEDIUM SQUARE
◻️ - U+25FB WHITE MEDIUM SQUARE
◾ - U+25FE BLACK MEDIUM-SMALL SQUARE
◽ - U+25FD WHITE MEDIUM-SMALL SQUARE
▪️ - U+25AA BLACK SMALL SQUARE
▫️ - U+25AB WHITE SMALL SQUARE
🚩 - U+1F6A9 TRIANGULAR FLAG

---
## [LineVall/lineage_frameworks_base](https://github.com/LineVall/lineage_frameworks_base)@[1b33a65e83...](https://github.com/LineVall/lineage_frameworks_base/commit/1b33a65e83cad3e1318389313f34c3169c8e18c0)
#### Wednesday 2023-09-06 09:44:03 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6
Signed-off-by: Sageofd6path <mail2anirban95@gmail.com>
Signed-off-by: Sipun Ku Mahanta <sipunkumar85@gmail.com>

---
## [Hopireika/kernel_xiaomi_mt6768](https://github.com/Hopireika/kernel_xiaomi_mt6768)@[6ccce4cd42...](https://github.com/Hopireika/kernel_xiaomi_mt6768/commit/6ccce4cd4286bde7edf9e0e8407af99dd977b00e)
#### Wednesday 2023-09-06 09:49:33 by Peter Zijlstra

sched/core: Fix ttwu() race

Paul reported rcutorture occasionally hitting a NULL deref:

  sched_ttwu_pending()
    ttwu_do_wakeup()
      check_preempt_curr() := check_preempt_wakeup()
        find_matching_se()
          is_same_group()
            if (se->cfs_rq == pse->cfs_rq) <-- *BOOM*

Debugging showed that this only appears to happen when we take the new
code-path from commit:

  2ebb17717550 ("sched/core: Offload wakee task activation if it the wakee is descheduling")

and only when @cpu == smp_processor_id(). Something which should not
be possible, because p->on_cpu can only be true for remote tasks.
Similarly, without the new code-path from commit:

  c6e7bd7afaeb ("sched/core: Optimize ttwu() spinning on p->on_cpu")

this would've unconditionally hit:

  smp_cond_load_acquire(&p->on_cpu, !VAL);

and if: 'cpu == smp_processor_id() && p->on_cpu' is possible, this
would result in an instant live-lock (with IRQs disabled), something
that hasn't been reported.

The NULL deref can be explained however if the task_cpu(p) load at the
beginning of try_to_wake_up() returns an old value, and this old value
happens to be smp_processor_id(). Further assume that the p->on_cpu
load accurately returns 1, it really is still running, just not here.

Then, when we enqueue the task locally, we can crash in exactly the
observed manner because p->se.cfs_rq != rq->cfs_rq, because p's cfs_rq
is from the wrong CPU, therefore we'll iterate into the non-existant
parents and NULL deref.

The closest semi-plausible scenario I've managed to contrive is
somewhat elaborate (then again, actual reproduction takes many CPU
hours of rcutorture, so it can't be anything obvious):

					X->cpu = 1
					rq(1)->curr = X

	CPU0				CPU1				CPU2

					// switch away from X
					LOCK rq(1)->lock
					smp_mb__after_spinlock
					dequeue_task(X)
					  X->on_rq = 9
					switch_to(Z)
					  X->on_cpu = 0
					UNLOCK rq(1)->lock

									// migrate X to cpu 0
									LOCK rq(1)->lock
									dequeue_task(X)
									set_task_cpu(X, 0)
									  X->cpu = 0
									UNLOCK rq(1)->lock

									LOCK rq(0)->lock
									enqueue_task(X)
									  X->on_rq = 1
									UNLOCK rq(0)->lock

	// switch to X
	LOCK rq(0)->lock
	smp_mb__after_spinlock
	switch_to(X)
	  X->on_cpu = 1
	UNLOCK rq(0)->lock

	// X goes sleep
	X->state = TASK_UNINTERRUPTIBLE
	smp_mb();			// wake X
					ttwu()
					  LOCK X->pi_lock
					  smp_mb__after_spinlock

					  if (p->state)

					  cpu = X->cpu; // =? 1

					  smp_rmb()

	// X calls schedule()
	LOCK rq(0)->lock
	smp_mb__after_spinlock
	dequeue_task(X)
	  X->on_rq = 0

					  if (p->on_rq)

					  smp_rmb();

					  if (p->on_cpu && ttwu_queue_wakelist(..)) [*]

					  smp_cond_load_acquire(&p->on_cpu, !VAL)

					  cpu = select_task_rq(X, X->wake_cpu, ...)
					  if (X->cpu != cpu)
	switch_to(Y)
	  X->on_cpu = 0
	UNLOCK rq(0)->lock

However I'm having trouble convincing myself that's actually possible
on x86_64 -- after all, every LOCK implies an smp_mb() there, so if ttwu
observes ->state != RUNNING, it must also observe ->cpu != 1.

(Most of the previous ttwu() races were found on very large PowerPC)

Nevertheless, this fully explains the observed failure case.

Fix it by ordering the task_cpu(p) load after the p->on_cpu load,
which is easy since nothing actually uses @cpu before this.

Fixes: c6e7bd7afaeb ("sched/core: Optimize ttwu() spinning on p->on_cpu")
Reported-by: Paul E. McKenney <paulmck@kernel.org>
Tested-by: Paul E. McKenney <paulmck@kernel.org>
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Signed-off-by: Ingo Molnar <mingo@kernel.org>
Link: https://lkml.kernel.org/r/20200622125649.GC576871@hirez.programming.kicks-ass.net

---
## [huohsien/yoga_class_smart_booking](https://github.com/huohsien/yoga_class_smart_booking)@[dc0da3ac23...](https://github.com/huohsien/yoga_class_smart_booking/commit/dc0da3ac23c2693859c2b7abf173612274ba9da5)
#### Wednesday 2023-09-06 09:51:42 by Victor Jiang

After True Yoga 2023 August so-called being-hacker-attacked event, the website was updated. So in this commit, a few adjustment was made to accommodate the changes. Also refactor the previous code so that running scraping once is enough. The new rule is that every class is open for booking at exactly 72 hours before. Not by date but by more accurate exact 72 hours. So there is no 10 pm rush. This impacts this notebook little but a condition is set to check if clicking to the next page is needed. They are stupid or lousy or something since if you want this accurate way of releasing vacancy for class, you should not use a calendar of a week. Instead, the class schedule should be from today to 7 days later. I think they just don't want to upload back stage data regularly, say, everyday, and want to do it once a week. If anything changed in the schedule they just silently update. It is bad for people to plan their class ahead

---
## [antgamdia/kubeapps](https://github.com/antgamdia/kubeapps)@[4e5ac7a243...](https://github.com/antgamdia/kubeapps/commit/4e5ac7a24310d30a0ab539560373cab1106277cd)
#### Wednesday 2023-09-06 10:07:44 by Antonio Gámez, PhD

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
## [pwnrazr/kernel_raphael_sm8150](https://github.com/pwnrazr/kernel_raphael_sm8150)@[4adc01d25d...](https://github.com/pwnrazr/kernel_raphael_sm8150/commit/4adc01d25da84443fd4a204ca4744bf4a002e3e8)
#### Wednesday 2023-09-06 10:57:33 by Wang Han

power: Introduce OnePlus 3 fingerprintd thaw hack

Taken from Oneplus 3, this hack will make fingerprintd recover from suspend quickly.

Small fixes for newer kernels since we're coming from 3.10.108..

Change-Id: I0166e82d51a07439d15b41dbc03d7e751bfa783b
Co-authored-by: Cyber Knight <cyberknight755@gmail.com>
[cyberknight777: forwardport and adapt to 4.14]
Co-authored-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>
[Tashar02: forwardport and adapt to 4.19 and xiaomi_sdm660's fp]
Signed-off-by: Shreyansh Lodha <slodha96@gmail.com>
Signed-off-by: Pierre2324 <pdbbasketball@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>
Signed-off-by: Dhruv <dhruvgera61@gmail.com>
Signed-off-by: Cyber Knight <cyberknight755@gmail.com>
Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>

---
## [ArisonID/aris-silly-themes](https://github.com/ArisonID/aris-silly-themes)@[c498de4c6e...](https://github.com/ArisonID/aris-silly-themes/commit/c498de4c6efd46a0bb864d57d4fe33dba2edc4f9)
#### Wednesday 2023-09-06 11:09:19 by Ari

Hey guys, did you know that in terms of male human and female Pokémon breeding, Vaporeon is the most compatible Pokémon for humans? Not only are they in the field egg group, which is mostly comprised of mammals, Vaporeon are an average of 3”03’ tall and 63.9 pounds, this means they’re large enough to be able handle human dicks, and with their impressive Base Stats for HP and access to Acid Armor, you can be rough with one. Due to their mostly water based biology, there’s no doubt in my mind that an aroused Vaporeon would be incredibly wet, so wet that you could easily have sex with one for hours without getting sore. They can also learn the moves Attract, Baby-Doll Eyes, Captivate, Charm, and Tail Whip, along with not having fur to hide nipples, so it’d be incredibly easy for one to get you in the mood. With their abilities Water Absorb and Hydration, they can easily recover from fatigue with enough water. No other Pokémon comes close to this level of compatibility. Also, fun fact, if you pull out enough, you can make your Vaporeon turn white. Vaporeon is literally built for human dick. Ungodly defense stat+high HP pool+Acid Armor means it can take cock all day, all shapes and sizes and still come for more

---
## [shubham9580/Analysis-of-Hotel-Customer-Sentiments](https://github.com/shubham9580/Analysis-of-Hotel-Customer-Sentiments)@[75f3869757...](https://github.com/shubham9580/Analysis-of-Hotel-Customer-Sentiments/commit/75f38697578d99e5fc08d2ba360be5d6f5672d5f)
#### Wednesday 2023-09-06 11:28:09 by Shubham Singh

Add files via upload

Sentiment analysis is part of the Natural Language Processing (NLP) techniques that consists in extracting emotions related to some raw texts. This is usually used on social media posts and customer reviews in order to automatically understand if some users are positive or negative and why. The goal of this study is to show how sentiment analysis can be performed using python. Here are some of the main libraries we will use:

NLTK: the most famous python module for NLP techniques.
Gensim: a topic-modeling and vector space modeling toolkit.
Scikit-learn: the most used python machine-learning library.
We will use here some hotel review data. Each observation consists of one customer review for one hotel. Each customer review is composed of textual feedback of the customer's experience at the hotel and an overall rating.

For each textual review, we want to predict if it corresponds to a good review (the customer is happy) or to a bad one (the customer is not satisfied). The review's overall ratings can range from 2.5/10 to 10/10.

In order to simplify the problem we will split those into two categories:

bad reviews have overall ratings < 5
good reviews have overall ratings > = 5
The challenge here is to be able to predict this information using only the raw textual data from the review.

---
## [itsHanibee/kernel_xiaomi_chime](https://github.com/itsHanibee/kernel_xiaomi_chime)@[77090a58c6...](https://github.com/itsHanibee/kernel_xiaomi_chime/commit/77090a58c6e32e529b5e4db23739db80950d778c)
#### Wednesday 2023-09-06 11:29:13 by Johannes Weiner

mm: vmscan: fix extreme overreclaim and swap floods

During proactive reclaim, we sometimes observe severe overreclaim, with
several thousand times more pages reclaimed than requested.

This trace was obtained from shrink_lruvec() during such an instance:

    prio:0 anon_cost:1141521 file_cost:7767
    nr_reclaimed:4387406 nr_to_reclaim:1047 (or_factor:4190)
    nr=[7161123 345 578 1111]

While he reclaimer requested 4M, vmscan reclaimed close to 16G, most of it
by swapping.  These requests take over a minute, during which the write()
to memory.reclaim is unkillably stuck inside the kernel.

Digging into the source, this is caused by the proportional reclaim
bailout logic.  This code tries to resolve a fundamental conflict: to
reclaim roughly what was requested, while also aging all LRUs fairly and
in accordance to their size, swappiness, refault rates etc.  The way it
attempts fairness is that once the reclaim goal has been reached, it stops
scanning the LRUs with the smaller remaining scan targets, and adjusts the
remainder of the bigger LRUs according to how much of the smaller LRUs was
scanned.  It then finishes scanning that remainder regardless of the
reclaim goal.

This works fine if priority levels are low and the LRU lists are
comparable in size.  However, in this instance, the cgroup that is
targeted by proactive reclaim has almost no files left - they've already
been squeezed out by proactive reclaim earlier - and the remaining anon
pages are hot.  Anon rotations cause the priority level to drop to 0,
which results in reclaim targeting all of anon (a lot) and all of file
(almost nothing).  By the time reclaim decides to bail, it has scanned
most or all of the file target, and therefor must also scan most or all of
the enormous anon target.  This target is thousands of times larger than
the reclaim goal, thus causing the overreclaim.

The bailout code hasn't changed in years, why is this failing now?  The
most likely explanations are two other recent changes in anon reclaim:

1. Before the series starting with commit 5df741963d52 ("mm: fix LRU
   balancing effect of new transparent huge pages"), the VM was
   overall relatively reluctant to swap at all, even if swap was
   configured. This means the LRU balancing code didn't come into play
   as often as it does now, and mostly in high pressure situations
   where pronounced swap activity wouldn't be as surprising.

2. For historic reasons, shrink_lruvec() loops on the scan targets of
   all LRU lists except the active anon one, meaning it would bail if
   the only remaining pages to scan were active anon - even if there
   were a lot of them.

   Before the series starting with commit ccc5dc67340c ("mm/vmscan:
   make active/inactive ratio as 1:1 for anon lru"), most anon pages
   would live on the active LRU; the inactive one would contain only a
   handful of preselected reclaim candidates. After the series, anon
   gets aged similarly to file, and the inactive list is the default
   for new anon pages as well, making it often the much bigger list.

   As a result, the VM is now more likely to actually finish large
   anon targets than before.

Change the code such that only one SWAP_CLUSTER_MAX-sized nudge toward the
larger LRU lists is made before bailing out on a met reclaim goal.

This fixes the extreme overreclaim problem.

Fairness is more subtle and harder to evaluate.  No obvious misbehavior
was observed on the test workload, in any case.  Conceptually, fairness
should primarily be a cumulative effect from regular, lower priority
scans.  Once the VM is in trouble and needs to escalate scan targets to
make forward progress, fairness needs to take a backseat.  This is also
acknowledged by the myriad exceptions in get_scan_count().  This patch
makes fairness decrease gradually, as it keeps fairness work static over
increasing priority levels with growing scan targets.  This should make
more sense - although we may have to re-visit the exact values.

Link: https://lkml.kernel.org/r/20220802162811.39216-1-hannes@cmpxchg.org
Signed-off-by: Johannes Weiner <hannes@cmpxchg.org>
Reviewed-by: Rik van Riel <riel@surriel.com>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hugh Dickins <hughd@google.com>
Cc: Joonsoo Kim <iamjoonsoo.kim@lge.com>
Cc: <stable@vger.kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Alexander Winkowski <dereference23@outlook.com>

---
## [sdiazlor/argilla](https://github.com/sdiazlor/argilla)@[028416a56e...](https://github.com/sdiazlor/argilla/commit/028416a56e1eb05defe9dffcd03de5d1744bdcf2)
#### Wednesday 2023-09-06 11:42:05 by Natalia Elvira

Docs/feedback setfit tutorial (#3530)

<!-- Thanks for your contribution! As part of our Community Growers
initiative 🌱, we're donating Justdiggit bunds in your name to reforest
sub-Saharan Africa. To claim your Community Growers certificate, please
contact David Berenstein in our Slack community or fill in this form
https://tally.so/r/n9XrxK once your PR has been merged. -->

# Description

Adds a new tutorial on how to use SetFit to get zero-shot suggestions
for `Label` and `MultiLabel` questions in Feedback datasets.

Closes #3528 

**Type of change**

(Remember to title the PR according to the type of change)

- [x] Documentation update

**How Has This Been Tested**

(Please describe the tests that you ran to verify your changes.)

- [x] `sphinx-autobuild` (read [Developer
Documentation](https://docs.argilla.io/en/latest/community/developer_docs.html#building-the-documentation)
for more details)

**Checklist**

- [ ] I added relevant documentation
- [x] I followed the style guidelines of this project
- [x] I did a self-review of my code
- [x] I made corresponding changes to the documentation
- [x] My changes generate no new warnings
- [ ] I filled out [the contributor form](https://tally.so/r/n9XrxK)
(see text above)
- [ ] I have added relevant notes to the `CHANGELOG.md` file (See
https://keepachangelog.com/)

---
## [powerhome/playbook](https://github.com/powerhome/playbook)@[205619a0e9...](https://github.com/powerhome/playbook/commit/205619a0e9ce327306acf84735c13ea4ed356c7b)
#### Wednesday 2023-09-06 12:27:31 by Gavin Huang

[PLAY-972] dateTime Bug Fixes (#2716)

**What does this PR do?**
- Corrects incorrect weekdays by removing the `getUTC` functions
- In the DB, for example, the date was August 15, 2023 01:30:00. The
`toWeekday` function formatted the date from UTC to Local Time, but
`getUTCDay()` went back to grab the UTC date. This issue was evident
with late-day appointments. Therefore, we should not be using any
`getUTC` functions.
- Corrects two bugs Jason found within`fromNow()`:
  - Remove period from "years ago"
- Fix miscalculation of "milliseconds in a month" - this was causing any
past date with a timestamp of "x months ago" to have a random number
- Updates `toLocaleString()` to use `en-US`
- Hayden R. reported he was receiving `undefined NaN`. Upon
investigation, certain locales (like en-GB [Great Britain]), can't use
functions like `getMonth()` so it was returning `undefined NaN`. We
default to `en-US` because internationalization and formatting does not
matter since Playbook formats dates in a specific way.

**Screenshots**

**Before**

![Before](https://github.com/powerhome/playbook/assets/47684670/07303adf-f2eb-4d7b-a0ba-ad82cf7f945c)

**After**

![After](https://github.com/powerhome/playbook/assets/47684670/8696283f-d4b4-4ab3-9302-c9651af672cd)

**How to test?** Steps to confirm the desired behavior:
1. The weekday problem was experienced in the [Sales
Books](https://nitro.powerhrg.com/sales/reps/11115/sales_books?rep_filter%5Bdate%5D%5Byear%5D=2023&rep_filter%5Bdate%5D%5Bmonth%5D=8).
In Miguel Picart's (or any RC), select their "Books" tab, select "All
Appointments", find any place that has 2+ appointments the same day -
they should be correct.
2. For Hayden's bug, impersonate Hayden and in his user profile ensure
that the address is showing as his European address. Go to a Runway
ticket and check the reviewers, he should not see `undefined NaN`. We
should also ensure that Hayden can see a date after the release.

#### Checklist:
- [X] **LABELS** Add a label: `enhancement`, `bug`, `improvement`, `new
kit`, `deprecated`, or `breaking`. See [Changelog &
Labels](https://github.com/powerhome/playbook/wiki/Changelog-&-Labels)
for details.
- [X] **DEPLOY** I have added the `milano` label to show I'm ready for a
review.
- [ ] **TESTS** I have added test coverage to my code.

---------

Co-authored-by: Nida Ghuman <nidaqg@gmail.com>

---
## [SDM0/clovermon-showdown](https://github.com/SDM0/clovermon-showdown)@[6d6f99c04b...](https://github.com/SDM0/clovermon-showdown/commit/6d6f99c04b6e701e667d1ceb17904f7a1540272f)
#### Wednesday 2023-09-06 12:45:27 by DeeGee22

Fixes a bunch of Wack moves

Villain Power
Why
Inverted Room
Mass Hysteria
Hellfire
Heaven's Hole
Paint Roller
Painting World
Whirl Paint
Siren Song
Blood Seal
Amber Wave
Dust Tornado
Dust Storm
Yata no Kagami
Bold Counter
Irate Trance
Venus Burst
Reverse Splash
Fabric World (including pitted rock increased duration)
Fabric Softener
Sewing (fabric world effect)
WINDRAGE
Spring Cleaning
Steam Clean (Untested)
Throat Heal (Untested)
Carpet Rub (untested)
Pull Wool
Focus Time
Hour Blast
Honor Bind
Arborium (added wooden rock increased duration)
Matter of Time
De-Age
Faith Charge
Fossilize
Fast Forward (Untested)
Minute Blast
Tic Toc
Time Freeze
Hat Spin
Terraform
Clearing Win
Wind Spin
Bowl Spin
Pirouette
Pizzaspin
Woodspin
Screw Attack
Kikenjo
Dust Blizzard
Sabbath
TeardropPhotonRay
Comet Rush
Isis Magic (fix)

---
## [ChengYueJia/jellyfish](https://github.com/ChengYueJia/jellyfish)@[a81387790a...](https://github.com/ChengYueJia/jellyfish/commit/a81387790ad9a91706a615a4a77a5bb15591a5ac)
#### Wednesday 2023-09-06 13:47:24 by Gus Gutoski

make `bytes_from_field_elements` infallible with paranoid checks for overflow (#250)

* impl Error for PCSError

* use anyhow for bytes_from_field_elements error type

* make bytes_from_field_elements infallible

* appease clippy (you're welcome)

* tidy an ugly line

* better test

* check everything for overflow, better panic messages

* remove commented code (oops)

---
## [JuanPabloRios27/JuanPabloRios27](https://github.com/JuanPabloRios27/JuanPabloRios27)@[5c87a35469...](https://github.com/JuanPabloRios27/JuanPabloRios27/commit/5c87a354698a2cb0e8c5b5320da4854d90109313)
#### Wednesday 2023-09-06 14:18:34 by World Wide Network

Update README.md

- 👋 Hello everyone this is my official github account, my real name is Juan Pablo and there are some kind of work that you can contribute if you can.

- 👀 I’m interested in learn, code, invest and real amazing stuff in this comunity, I hope that you want to find this stuffs too.
  
- 🌱 I’m currently studying Computer Science from the college. And I wanted to invest in social media, code and doing some stuff.
  
- 💞️ I’m looking to find someone to help me, achieve my own potential. And help others to do that.
  
- 📫 How to reach me, you can contact me by this email jprios@unbosque.edu.co or search by my twitter channel.

---
## [swagXDragonSlayer46YT/Supersymmetry](https://github.com/swagXDragonSlayer46YT/Supersymmetry)@[ea770d1f3e...](https://github.com/swagXDragonSlayer46YT/Supersymmetry/commit/ea770d1f3e9c049737c6acd58fbca8a291c64497)
#### Wednesday 2023-09-06 14:39:08 by Rainbuu

Lignite coal for torches (#127)

* Lignite coal for torches

blame someone on discord. its only 2 torches per recipe because lignite sucks ass

* Anthracite torches

how the fuck do you spell this

---
## [Boleros07/art-book-next-es-de-enhanced](https://github.com/Boleros07/art-book-next-es-de-enhanced)@[600d1acb97...](https://github.com/Boleros07/art-book-next-es-de-enhanced/commit/600d1acb97afc13cd4d11e6482ea1f547469c2d7)
#### Wednesday 2023-09-06 14:48:54 by Boleros07

Added pngs and svgs

Advance Wars
Animal Crossing
Baseball
Basketball
Batman
Bomberman
Castlevania
Contra
Crash Bandicoot
Devil May Cry
Disney
Donkey Kong
Double Dragon
Duke Nukem
Earthbound
Fatal Fury
Final Fantasy
Football
F-Zero
GTA (3 alts)
Hacks
Harry Potter
Hockey
Hulk
Indiana Jones
James Bond
Kirby
Lego
Mario
Mario Kart
Megaman
Metal Gear (2 alts)
Metal Slug
Metroid
Mortal Kombat
Phoenix Wright
Professor Layton
Ratchet and Clank
Rayman
Simpsons
Sly Cooper
Sonic
Spyro
Star Trek
Star Wars
Street Fighter
Super Smash Bros
Tennis
TMNT
Tomb Raider
Wario
X-Men
Zelda

---
## [NotStatilko/tgbox-cli](https://github.com/NotStatilko/tgbox-cli)@[d0881c3d2a...](https://github.com/NotStatilko/tgbox-cli/commit/d0881c3d2a6127ec1aa838bcff27ca6e124132aa)
#### Wednesday 2023-09-06 15:10:33 by NotStatilko

Disable broken colored output in Pager on Windows

I can not find a way to show colors in the default
Windows CMD Pager (like in 'file-search' or 'help'),
so now it will be not forced (up to Click library
to decide, color or not). You can force by adding
the "TGBOX_CLI_FORCE_PAGER_COLOR" to Env Vars,
although output will be probably broken.

Windows is some piece of fucking shit. I fucking
hate it. Who ever will want to write code on this
bullshit OS? That's absolutely fucking annoying.

All i can recommend is just to use a Cygwin. Don't
want to spend more time on this awful system.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[1be0841d98...](https://github.com/tgstation/tgstation/commit/1be0841d98f215a0e94245c33317232bafa59342)
#### Wednesday 2023-09-06 15:32:46 by Time-Green

Removes COMSIG_AREA_INITIALIZED_IN (#78143)

Literally just me stealing #77207 completely muhahahhahahah screw you
@Mothblocks
I did add some documentation and some radnebula related cleaning and
testing to make it work well

Copied from original PR:

> Please do NOT add code to InitAtom, it is extremely hot. The
conditions on this alone were costing nearly 200ms on my extremely
powerful machine.
> 
> Changes the radioactive nebula to perform its work by looping over
every space tile on init (which on my machine is faster than the time
being wasted on this signal), and adds a subsystem that does this in
SS_BACKGROUND every 30 seconds (usually completeable in about half a
second) for any new atoms, because the effect is hardly noticeable
anyway with how green space is.

Honestly we really don't care that much about stuff being initialized in
space. Everything that walks into space (about everything that matters
to players), is completely unaffected by this change, but roundstart is
now slightly faster

---
## [bojanskr/next.js](https://github.com/bojanskr/next.js)@[6238f8a5c0...](https://github.com/bojanskr/next.js/commit/6238f8a5c0ffabb7dfb35872c52c942ed7f148da)
#### Wednesday 2023-09-06 15:42:21 by Jimmy Lai

performance: don't compile on hover on dev (#51830)

An annoying issue that slows down compilation times in dev for Next is
that we might trigger compilation of a page via hover on app.

We do this because we want the same experience in production and dev and
the prefetching is important for instantaneous loading states.

The alternative in this PR is that we don't prefetch at all anymore in
dev but instead, when we handle navigation, we can force a prefetch
navigation.

The slight compromise with this approach is that you can't test
prefetching anymore in dev.


<!-- Thanks for opening a PR! Your contribution is much appreciated.
To make sure your PR is handled as smoothly as possible we request that
you follow the checklist sections below.
Choose the right checklist for the change(s) that you're making:

## For Contributors

### Improving Documentation

- Run `pnpm prettier-fix` to fix formatting issues before opening the
PR.
- Read the Docs Contribution Guide to ensure your contribution follows
the docs guidelines:
https://nextjs.org/docs/community/contribution-guide

### Adding or Updating Examples

- The "examples guidelines" are followed from our contributing doc
https://github.com/vercel/next.js/blob/canary/contributing/examples/adding-examples.md
- Make sure the linting passes by running `pnpm build && pnpm lint`. See
https://github.com/vercel/next.js/blob/canary/contributing/repository/linting.md

### Fixing a bug

- Related issues linked using `fixes #number`
- Tests added. See:
https://github.com/vercel/next.js/blob/canary/contributing/core/testing.md#writing-tests-for-nextjs
- Errors have a helpful link attached, see
https://github.com/vercel/next.js/blob/canary/contributing.md

### Adding a feature

- Implements an existing feature request or RFC. Make sure the feature
request has been accepted for implementation before opening a PR. (A
discussion must be opened, see
https://github.com/vercel/next.js/discussions/new?category=ideas)
- Related issues/discussions are linked using `fixes #number`
- e2e tests added
(https://github.com/vercel/next.js/blob/canary/contributing/core/testing.md#writing-tests-for-nextjs
- Documentation added
- Telemetry added. In case of a feature if it's used or not.
- Errors have a helpful link attached, see
https://github.com/vercel/next.js/blob/canary/contributing.md


## For Maintainers

- Minimal description (aim for explaining to someone not on the team to
understand the PR)
- When linking to a Slack thread, you might want to share details of the
conclusion
- Link both the Linear (Fixes NEXT-xxx) and the GitHub issues
- Add review comments if necessary to explain to the reviewer the logic
behind a change

### What?

### Why?

### How?

Closes NEXT-
Fixes #

-->

link NEXT-1317

---
## [codecov/codecov-api](https://github.com/codecov/codecov-api)@[e2c6b1c425...](https://github.com/codecov/codecov-api/commit/e2c6b1c425cac66f0d422bd5692c7aae4cc46b61)
#### Wednesday 2023-09-06 16:07:38 by Giovanni M Guidini

fix: lru_cache issues + meta info missing  (#72)

Context: https://github.com/codecov/engineering-team/issues/119

So the real issue with the meta info is fixed in codecov/shared#22.
spoiler: reusing the report details cached values and _changing_ them is not a good idea.

However in the process of debuging that @matt-codecov pointed out that we were not using lru_cache correctly.
Check this very well made video: https://www.youtube.com/watch?v=sVjtp6tGo0g

So the present changes upgrade shared so we fix the meta info stuff AND address the cache issue.
There are further complications with the caching situation, which explain why I decided to add the cached value in the
`obj` instead of `self`. The thing is that there's only 1 instance of `ArchiveField` shared among ALL instances of
the model class (for example, all `ReportDetail` instances). This kinda makes sense because we only create an instance
of `ArchiveField` in the declaration of the `ReportDetail` class.

Because of that if the cache is in the `self` of `ArchiveField` different instances of `ReportDetails` will have dirty cached value of other `ReportDetails` instances and we get wrong values. To fix that I envision 3 possibilities:
1. Putting the cached value in the `ReportDetails` instance directly (the `obj`), and checking for the presence of that value.
If it's there it's guaranteed that we put it there, and we can update it on writes, so that we can always use it. Because it is
for each `ReportDetails` instance we always get the correct value, and it's cleared when the instance is killed and garbage collected.

2. Storing an entire table of cached values in the `self` (`ArchiveField`) and using the appropriate cache value when possible. The problem here is that we need to manage the cache ourselves (which is not that hard, honestly) and probably set a max value. Then we will populate the cache and over time evict old values. The 2nd problem is that the values themselves might be too big to hold in memory (which can be fixed by setting a very small value in the cache size). There's a fine line there, but it's more work than option 1 anyway.

3. We move the getting and parsing of the value to outside `ArchiveField` (so it's a normal function) and use `lru_cache` in that function. Because the `rehydrate` function takes a reference to `obj` I don't think we should pass that, so the issue here is that we can't cache the rehydrated value, and would have to rehydrate every time (which currently is not expensive at all in any model)

This is an instance cache, so it shouldn't need to be cleaned for the duration of the instance's life
(because it is updates on the SET)

closes codecov/engineering-team#119

---
## [Sealed101/tgstation](https://github.com/Sealed101/tgstation)@[fc836593a5...](https://github.com/Sealed101/tgstation/commit/fc836593a51771fc6c06adfa28f81d3cd134a501)
#### Wednesday 2023-09-06 16:28:38 by GuillaumePrata

Makes fanny packs be silent, others can't see what you put in or take out. (#78010)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Just like the syndicate toolbox and a handful of other items.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
This is a blatantly stealth antag buff.

Pockets are 2 silent storage slots everyone has, so it is not adding
anything that antags didn't have access already.
But going from 2 to 5 small items can help a lot, also belts are a lot
smoother to use with their shortcut keys.

Love stealth antags, hate murderboners, gonna help my stealth boys not
be valid hunted because someone checked their chat logs from 10 minutes
ago and read that X player put Y contraband in their bag.

Or people that have some contraband names highlighted on chat... but no
one does that right.... right?
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

:cl:Guillaume Prata
balance: Fanny packs are now silent, no one will get a chat message
about what you put in or take out.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Aki Ito <11748095+ExcessiveUseOfCobblestone@users.noreply.github.com>

---
## [Hardaeborla/zechub](https://github.com/Hardaeborla/zechub)@[73c19fca40...](https://github.com/Hardaeborla/zechub/commit/73c19fca4090fe98704f75112418158d2736159e)
#### Wednesday 2023-09-06 16:36:50 by Hardaeborla

zecweekly58.md

#Iwe Iroyin Osẹ-ọsẹ Zec #58

Ìwé ìròyìn ZF tí Oṣù August, Awọn ohun elo ṣi ṣii fun Awọn ifunni Kekere àti Ìṣe ilu alabagbepo tí ń bo 

 Atunto nipasẹ "Hardaeborla "[(@hardaeborla)](https://twitter.com/ayanlajaadebola) ati Itumọ si ede Yoruba nipasẹ "Hardaeborla" ([Hardaeborla](https://twitter.com/ayanlajaadebola))

### EKaabo si ZecWeekly

Kaabọ si ọsẹ igbadun kan nibiti a ti mu cryptocurrency tuntun ati awọn imudojuiwọn ilolupo Zcash wa fun ọ. Iwe iroyin ti ọsẹ yii pẹlu ikẹkọ lori awọn adirẹsi Zcash, awọn ifojusi lati iyipo keji ti eto fifunni kekere nipasẹ Zcash Foundation, ati awọn imudojuiwọn lati gbogbo agbegbe Zcash.
---

## Nkan Ẹkọ ti Ọsẹ yii
Ti o ba jẹ tuntun si Zcash, iwọ yoo ṣawari awọn oriṣi iṣowo meji ti a mọ bi sihin ati aabo. Fun awọn ti o tẹle awọn idagbasoke Zcash aipẹ, o tun le faramọ pẹlu Adirẹsi Iṣọkan lori Nẹtiwọọki Zcash. Ibeere bọtini ni bawo ni awọn adirẹsi wọnyi ṣe n ṣiṣẹ ni awọn apamọwọ Zcash.

Kọ ẹkọ diẹ sii: [Wiwo awọn adirẹsi Zcash](https://wiki.zechub.xyz/visualizing-zcash-addresses) 


## Awọn imudojuiwọn Zcash

####  Awọn imudojuiwọn ECC ati ZF
[Zooko Yoo Soro ni Mainnet tí Ọdún 2023 Oṣu Kẹsan ni ìjọ 20-22](https://twitter.com/MessariCrypto/status/1696289078743060668?t=BoeIGgLj-1E5a0gG3EmSyg&s=19) 

[Mu soke ⏭️lori gbogbo awọn igbejade Zcon4](https://twitter.com/ZcashFoundation/status/1697683679017910761?t=O1BOX3KBRlhMa5O-1UySCw&s=19) 

[Zcash Foundation 📰 Ìwé ìròyìn tí Oṣù Kẹjọ](https://zfnd.org/zcash-foundation-august-2023-newsletter/) 

["Ṣé o mọ…?" - @ZcashFoundation](https://twitter.com/ZcashFoundation/status/1696220390081630649?t=kR1czvJRrTwyRow3VUZhGg&s=19) 

[Ètò Àwọn ifunni Kékeré ZF Yíká tí èlé kejì tí bẹ̀rẹ̀](https://twitter.com/ZcashFoundation/status/1697683688543182961?t=q99lgXcT5yTvodQwXnTYgA&s=19) 




####  Awọn imudojuiwọn Awọn ifunni Agbegbe Zcash

[Ṣeto Olurannileti Rẹ Fun Owó Town Hall tí Zcash Dev ni Ọdún 2024](https://twitter.com/zerodartz/status/1696520352665604280?t=GUqwlspErtJtqlpQbH_Rgw&s=19) 

[Iṣẹlẹ Awọn ifunni Agbegbe Zcash lori Discord](https://twitter.com/ZcashCommGrants/status/1696965307376586818?t=wcyWJ76a1EBEM3NqX9WsaQ&s=19) 

[Awọn iṣẹju ipade ZCG 08/21/23](https://forum.zcashcommunity.com/t/zcash-community-grants-meeting-minutes-8-21-23/45505) 


#### Awujo Ise Agbese 
[Igbero Tuntun 🆕 Láti Ọ̀dọ̀ ZecHub](https://twitter.com/dismad8/status/1696938238555074730?t=0Yb3-ZUaHnlXFIC5O459FQ&s=19) 

[Ṣetọrẹ si Eto “Gbigba Zcash Si Awọn ile-iwe”🙏](https://twitter.com/OGA4SKY/status/1697400463170122019?t=YZY9lJs0TELKwXsA4Bz83g&s=19) 

[DWeb Camp ṣeto lati ṣẹlẹ ni Ubatuba](https://twitter.com/zcashbrazil/status/1697612560969695382?t=Fcq2nX6Ed2Q52YUgZx_72g&s=19) 

[ZFAVClub lati ṣe atilẹyin Iṣẹlẹ Ibudo DWeb ni 🇧🇷Brazil](https://twitter.com/ZFAVClub/status/1697614302838919574?t=CTegZAaM3xLuszXeS78BpQ&s=19) 

[Ẹya akọkọ ti Free2Z Night!](https://twitter.com/gordonesroo/status/1696578807254118624?t=wCEEiZAP7Kev63zJv4Kb7w&s=19) 

[Tẹle ki o kọ ẹkọ diẹ sii nipa Zcash Book Club📖] (https://twitter.com/zcashesp/status/1697268356716359990?t=-bJB-XkhEf2Pi7RRemq38g&s=19) 

#### Iroyin ati Media 
[Crypto streamer padanu owo nitori ifihan bọtini ikọkọ lairotẹlẹ - Cointelegraph](https://cointelegraph.com/news/brazilian-crypto-streamer-loses-50k-by-exposing-private-key) 

[Oludasile Solana - "FTX SOL yẹ ki o pin si awọn onibara" - Decrypt](https://decrypt.co/154663/solana-cofounder-says-ftx-sol-should-distributed-customers) 


[Rupee òní nọ́mbà ń gbà ìgbé lárugẹ lílo pẹ̀lú isọpọ Yes Bank pẹlu UPI - Cointelegraph](https://cointelegraph.com/news/digital-rupee-gets-big-usability-boost-through-yes-bank-integration-with-upi) 

[Owó Àwọn Oludokoowo Bitcoin tí wọ́ $1.5 Billion](https://www.coindesk.com/markets/2023/09/01/large-bitcoin-holders-accumulate-15b-worth-of-btc-as-price-wavers) 

[Vitalik ta gbogbo àwọn owo rẹ lórí Maker DAO r - Trustnodes](https://www.trustnodes.com/2023/09/03/vitalik-buterin-ditches-mkr) 

[Ilana iwọntunwọnsi lo nilokulo fun $900K bi awọn hakii DeFi ṣe gbe soke - Cointelegraph](https://cointelegraph.com/news/balancer-protocol-exploited-for-900k-as-defi-hacks-mount-finance-redefined) 

## Awon oro die Nipa ZCash Lori Twitter
["Zcash ni ojo iwaju 🌅" - Splitcoin](https://twitter.com/splitcoincom/status/1696582966867312770?t=fPvCQCwlU8bDgfiJz8SeQg&s=19) 

[Sopọ, Kopa ati Pinpin Adarọ-ese rẹ🎙️ - ZcastEsp](https://twitter.com/ZcastEsp/status/1697256155272368545?t=Crhrt2iQgRZ54ZxI1mczjQ&s=19) 

[Lilo Zingo fun Iṣowo Rẹ] (https://twitter.com/ZingoLabs/status/1696211862470230294?t=Krkokr7jE2hsgDuf0rn0og&s=19) 

[Idide ti Zec Chapter 6 nipa @zcashCrusader](https://twitter.com/ZcashCrusader/status/1696758204569735236?t=pCZ8EDpVvF_-_cEi7wb0ng&s=19) 

[Igbèrò PayWithZcash FIO](https://forum.zcashcommunity.com/t/usernames/45504) 

[Awọn dukia Shielded Zcash 📊 n gun oke!](https://twitter.com/zooko/status/1697306927813005653/photo/1) 

[$ZEC pẹlu awọn Crypto oke marun ti ò ṣe mine ⛏️ ni ilé] (https://twitter.com/Cindy_Chando/status/1697849959968583840?t=UhAqpp31c6GNJg9gI9x0RQ&s=19) 


[Se Asiri Tuntun Deede?](https://twitter.com/techmindsmentor/status/1697838511922241631?t=tczFIS7hSR-iZtCF-YID9A&s=19) 

[Awọn ilana Lo nipasẹ Free2Z lati ṣe igbasilẹ Adarọ-ese wọn](https://twitter.com/zcashesp/status/1697781752125698088?t=zzsWn-8jdFMebCdBEEL40g&s=19) 

[Bull Run fun Asiri eyo? - NagatoDharma](https://twitter.com/NagatoDharma/status/1697609324003045867?t=0EOMchNKit9pOuCnueCKog&s=19) 

[Bitcoin ati Zcash ni ibatan si z-adirẹsi ati t-adirẹsi](https://twitter.com/ruzcash/status/1697830481381790120?t=lwf_XUkmsB3PuWapHXBXWQ&s=19) 

[Andrew Arnott fihan ìtọrẹ Maui ṣee ṣe pẹlu Zcash](https://twitter.com/aarnott/status/1697753434097938653?t=VlF4plbfsFoasDliSPvTIg&s=19) 

[Arakunrin Abila ni mi 🦓 - Yoditar](https://twitter.com/yoditarX/status/1697739731595899157?t=ccumO9xFA8dMDFsqCBTEsg&s=19) 

[Zcash Ṣe afihan nipasẹ Zellic "Ibere ​​si ZK👩‍🏫"](https://twitter.com/zellic_io/status/1697710984486678707?t=yFMnvjm8_5fS_Q2Lbk9s0Q&s=19) 

[Aṣiri yoo jẹ aṣa ati itan nigbagbogbo - @Michae2xl](https://twitter.com/michae2xl/status/1697699658355609978?t=rkWQVQWaQaUvjDwy1Nc4BQ&s=19) 





## Zeme ti Ose Yii 

[https://twitter.com/DarwinJZ11/status/1697654861355999277?t=SgNv5wS1bcoT5zvYtFLUqQ&s=19](https://twitter.com/DarwinJZ11/status/1697654861355999277?t=SgNv5wS1bcoT5zvYtFLUqQ&s=19) 


## Awọn iṣẹ ni ilolupo
[ZecWeekly #59  iwe iroyin Agbegbe](https://app.dework.xyz/zechub-2424/board?taskId=102e34d1-8f77-45d1-bd4f-d3d8f2a040ce) 

[Ṣiṣe Zcash Full Node lori Akash Network](https://app.dework.xyz/zechub-2424/board?taskId=543cab70-627d-4222-a712-9fb8768abe9c)

---
## [axodotdev/cargo-dist](https://github.com/axodotdev/cargo-dist)@[53eeb9f635...](https://github.com/axodotdev/cargo-dist/commit/53eeb9f6354f2b6723b61902421457472cf0b4fa)
#### Wednesday 2023-09-06 16:43:48 by Aria Beingessner

feat(msi): add msi installer

The "msi" installer vendors the binaries into a windows msi.
msi generation is implemented by using cargo-wix as a library,
which in turn handles generating templates and invoking WiX (v3).

The resulting msi's are unsigned -- signing will be handled by a followup,
as changes to OV certs mean that "proper" signing is now very complicated
and messy.

This implementation has some notable details:

main.wxs generation
--------------------

WiX requires an xml-based template called main.wxs for each msi it generates.
This template includes things like the application name, version, publisher,
EULA, embedded files, and so on.

cargo-wix's default workflow is for you to run `cargo wix init` once to generate
that file and check it in. At this point the developer is free to hand-edit
the template to suit their needs. We like this idea, `cargo dist generate-ci`
is based on that same premise!

But our experience with generate-ci has also taught us that this approach
is really prone to frustrating desyncs. The main.wxs bakes in several pieces
of information that were sourced from your Cargo.toml. As a result, if you
ever change your Cargo.toml, you now need to remember to apply the same
change to your main.wxs, or rerun `cargo wix init` and potentially clobber
any hand-edits you made.

As such, for the first draft of this feature we've opted for a more aggressive
solution: whenever you run `cargo dist init` we will invoke `cargo wix init`
to force the template to have up to date contents, essentially forbidding
hand-edits.

When you run `cargo dist build` or `cargo dist plan`
we will also error out if we detect that `cargo wix init` would modify
main.wxs.

A new `allow-dirty = ["msi"]` can be added to your cargo-dist config to
prevent `init` from regenerating main.wxs or checking that it's up to date,
essentially restoring the original design of cargo-wix. We believe this
should be opt-in because most people ideally shouldn't want to do hand-edits,
and desyncing is a very nasty footgun.

GUID persistence
----------------

`cargo dist init` will also modify your Cargo.tomls to add
`[package.metadata.wix]` with two generated GUIDs (if those GUIDs aren't
already present).

These GUIDs are used by windows to identify that two different msis actually
intend to refer to the same application and install dir. As such, each release
of your app needs to use the same GUID.

cargo-wix bakes these GUIDs into your main.wxs, and critically it defaults to
generating new random ones every time you run init (because constantly
re-initing wasn't part of the design).

By persisting the GUIDs to your package's Cargo.toml, we unlock the ability
to freely regenerate main.wxs whenever we want.

---
## [bencodezen/angular](https://github.com/bencodezen/angular)@[acd59ad037...](https://github.com/bencodezen/angular/commit/acd59ad0371a19838813cfc934a73fa3cc357602)
#### Wednesday 2023-09-06 16:49:45 by Ward Bell

docs: Migrate Observables guides & code examples to standalone (#51516)

None of the guide pages mentions ngModules. Only `observables-in-angular` needed conversion to Standalone.

However, some of the guide pages reflect old versions of RxJS, including signatures that are no longer valid. These have been corrected.

More significantly, *the existing guide is pretty bad at explaining RxJS and its usage*. It was written (by me I think) in the very early days of Angular and Angular RxJS instruction. I've taught numerous "RxJS in Angular" classes since and learned from that experience what does and does not work with students.

There was neither the time nor the charter to completely overhaul this guide. But this commit attempts to remove what flops with students and to bring the teaching closer to what seems more effectively. I hope reviewers agree that my revisions are an improvement.

**Revised Overview**

The overview doc, `observables.md`, had a few errors (ex: `next` is NOT REQUIRED) and deprecated patterns (you now must pass the Observer object to `subscribe`).

More importantly, it was wildly overcomplicated and scary, especially when it got into multi-casting.

Moved the multi-casting section to  "RxJS Library" and rewrote it (with working example) for simplicity and context.

I made other changes in an effort to make this an overview that is  more comprehensive and more clear. I paid particular attention to the "Basic usage and terms" section.

Finally, I relocated the "Naming conventions for observables" section here from `rx-library`. This is the section that describes the dollar-sign convention. It made more sense for it to be here.

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

PR Close #51516

---
## [Bjarl/Shiptest](https://github.com/Bjarl/Shiptest)@[ee4021c507...](https://github.com/Bjarl/Shiptest/commit/ee4021c50792c11bfd21085156edd32200c21cb8)
#### Wednesday 2023-09-06 17:02:10 by Imaginos16

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
## [zgracem/dotconfig](https://github.com/zgracem/dotconfig)@[74fd6f0b0b...](https://github.com/zgracem/dotconfig/commit/74fd6f0b0bf9c7d1d586ac0b6fe2d95371e7e117)
#### Wednesday 2023-09-06 17:10:18 by Z. Grace Moreau

homebrew: delete broken bullshit

Note to self -- never ask for "help" from Homebrew again. You'll get
nothing but nitpicking and condescension from programmer dudebros who
only read half your question in the first place, and ultimately whatever
problem you're having will be your own fault for trying to use Homebrew
the way the fucking documentation says you can use Homebrew. Give up.

---
## [Bjarl/Shiptest](https://github.com/Bjarl/Shiptest)@[1b315a616f...](https://github.com/Bjarl/Shiptest/commit/1b315a616ff24e3f1f92c791e4df4dc43ca9aad6)
#### Wednesday 2023-09-06 17:20:01 by Thedragmeme

Aegis update + patient clothing (#2150)

## About The Pull Request
The Aegis:
![2023-07-09 06 32
40](https://github.com/shiptest-ss13/Shiptest/assets/81540056/cf262257-1699-40e0-bcb1-6dc60f1e98a6)
I've touched up the central hallway's decals, they always bothered me
but at the time of the Aegis' creation, I wasn't as well versed with map
making as I am now. They're small tweaks that look better to me. The
smart fridge was removed and turned into a board, originally you could
access the smart fridge from outside of the ship, which wasn't intended.
Added some new posters. Compressed the number of red lockers down and
cleaned up the main hallway. I gave the psychologist a dart gun because
honestly, it sounded really funny.

![dart
riffle](https://github.com/shiptest-ss13/Shiptest/assets/81540056/eb10154a-1e28-4a5d-b41b-9b20f92b71a9)

Also, there are more seeds to make food with. There were like only two
food seeds and like five flowers before.

The Patient set:


![patient](https://github.com/shiptest-ss13/Shiptest/assets/81540056/65066ea3-92d1-4233-9bf6-a6448d43b11f)

Kepori and Vox versions are available. Long-term patients now spawn with
the white gown and slippers. The previous clothes they spawned with were
always intended to be replaced.

Hopefully, this PR also fixes long-term patients spawning with borked
ID's.

## Why It's Good For The Game

Fixing stuff, making stuff look better, and adding new RP opportunities
with clothes are good.

## Changelog

:cl: Drag
add: Adds a bunch of shit to the Aegis, nothing earth shattering
add: Added the patient set, along with Vox and Kepori compatible sprites
tweak: tweaked with the Aegis' decals
fix: (Hopefully) Fixes the Aegis' patient Id's
:cl:

---------

Signed-off-by: Thedragmeme <81540056+Draggeru@users.noreply.github.com>
Co-authored-by: thgvr <81882910+thgvr@users.noreply.github.com>

---
## [1j01/textual-paint](https://github.com/1j01/textual-paint)@[0657295662...](https://github.com/1j01/textual-paint/commit/0657295662aedb60ef83838930b740ba27b8ffcc)
#### Wednesday 2023-09-06 17:20:15 by Isaiah Odhner

Extract AnsiArtDocument and friends to files

This fixes the gallery app's --help, because before it was importing the "paint" module, which imported "args", which parsed arguments for the paint app instead of the gallery app.

This is also a refactor I've been meaning to do — since the very beginning, really — and it would've been a lot less trouble if I could've done it from the beginning, but I couldn't get imports to work. Yeah, really. Sounds pretty stupid 'cause it is. Python's module system is terrible.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[79ed872d6e...](https://github.com/treckstar/yolo-octo-hipster/commit/79ed872d6e37ca643b42f5b753c74f8c86cfe6b4)
#### Wednesday 2023-09-06 17:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [ttaylorr/git](https://github.com/ttaylorr/git)@[8f23432b38...](https://github.com/ttaylorr/git/commit/8f23432b38d9b122be8179295a56688391dc8ad6)
#### Wednesday 2023-09-06 17:30:10 by Johannes Schindelin

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
Signed-off-by: Pratyush Yadav <me@yadavpratyush.com>

---
## [ZephyrTFA/tgstation](https://github.com/ZephyrTFA/tgstation)@[b0ec1e4098...](https://github.com/ZephyrTFA/tgstation/commit/b0ec1e4098ed80fdb0bac69c6f950bd5e38012b8)
#### Wednesday 2023-09-06 18:04:49 by Jacquerel

[no gbp] Adds missing chat feedback to watcher abilities (#77700)

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

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[68e3a4f2be...](https://github.com/TaleStation/TaleStation/commit/68e3a4f2be8f28d34e33c572064c749a302f197b)
#### Wednesday 2023-09-06 18:11:10 by TaleStationBot

[MIRROR] [MDB IGNORE] Adds Blood-drunk and demonic frost miner boss music. (#7649)

Original PR: https://github.com/tgstation/tgstation/pull/78123
-----
## About The Pull Request

Acts as a continuation of PR #77149 for boss music functionality and
implements a BDM and demonic frost miner boss music theme.

## Why It's Good For The Game

More music is good, but I do have some gripes with my own PR. This
particular track relies on instrumentation that when compressed just
doesn't sound as good, and the in-game version is noticeably less
enjoyable that the high quality version. I wish I could help the track
out more, but as is it's already at 811 kb which is barely in line with
file requirements, so i just can't justify bloating the audio file sizes
to make it sound better. You notice this kind of problem a lot with the
higher runtime music and background tracks. It just feels a bit more
clunky than hierophant, but what are you gonna do right?

Here's a track sample. I had to use a third-party thingy to convert it
into mp4 so it might sound off but whatever. Thanks!


https://github.com/tgstation/tgstation/assets/77305289/d9f64665-ff9c-4ba4-95d1-6ad7d408f868


## Changelog

sound: adds BDM/frost miner theme

/:cl:

---------

Co-authored-by: RICK IM RI <77305289+tommysalami3@users.noreply.github.com>

---
## [nushell/nushell](https://github.com/nushell/nushell)@[a9216deaa4...](https://github.com/nushell/nushell/commit/a9216deaa40d7c5c184bdb3aa1520b6b67c20bf8)
#### Wednesday 2023-09-06 18:27:18 by Darren Schroeder

allow `--login` to be used with nu's `--commands` parameter (#10253)

# Description

This PR allows the `--login`/`-l` parameter to be used with nushell's
`--commands`/`-c` parameter. When you do this, since you're invoking it
with the `-l` flag, nushell will load your env.nu, config.nu, and
login.nu, in that order. Then it will proceed to run your commands. I
think this provides a better quality of life when you want to run
scripts with your personal config files as a login shell.


### Before (these entries are from the default_env.nu)

![image](https://github.com/nushell/nushell/assets/343840/ce7adcd0-419e-485c-b7d1-f11f162e8e9e)


### After (these entries are from my personal env.nu)

![image](https://github.com/nushell/nushell/assets/343840/33bbc06b-983c-4461-8274-290e4c712506)


closes https://github.com/nushell/nushell/issues/9833

# User-Facing Changes
<!-- List of all changes that impact the user experience here. This
helps us keep track of breaking changes. -->

# Tests + Formatting
<!--
Don't forget to add tests that cover your changes.

Make sure you've run and fixed any issues with these commands:

- `cargo fmt --all -- --check` to check standard code formatting (`cargo
fmt --all` applies these changes)
- `cargo clippy --workspace -- -D warnings -D clippy::unwrap_used` to
check that you're using the standard code style
- `cargo test --workspace` to check that all tests pass (on Windows make
sure to [enable developer
mode](https://learn.microsoft.com/en-us/windows/apps/get-started/developer-mode-features-and-debugging))
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

---
## [Pickle-Coding/tgstation](https://github.com/Pickle-Coding/tgstation)@[297f7f88e8...](https://github.com/Pickle-Coding/tgstation/commit/297f7f88e866d4a17b27cb15c0b8ee606742bbf6)
#### Wednesday 2023-09-06 18:55:29 by Sealed101

Fixes things about goliaths: wallhacks/range hacks(no, really) and tentacles not spawning in mineral turfs; also fixes `find_potential_targets` wallhacks (#77393)

## About The Pull Request

Goliath's sand digging behaviour could potentially target a turf that's
actually unreachable by the goliath, e.g.
```
G#
#T
```
where G - goliath # - wall T - target turf. fixed that, but i think
there could be something easier here, maybe instead grabbing turfs in
goliath's `view()`? unsure

The component goliaths use to telegraph their attacks
(`basic_mob_attack_telegraph`) casts a `do_after()` to perform the
attack, but it was not actually checking for the target staying in melee
range, as it was using the source goliath as both `user` and `target`,
so it didn't actually care at all for the target. Implemented an
`extra_checks` to `Adjacent()` since that's the closest we get for melee
range shenanigans I suppose
This still allows the source basicmob to attack the target if the target
moves around the source basicmob.

`!`Goliaths were also able to summon tentacles on a target that moved
into cover and still stayed in the `find_potential_targets` target
range. Which meant more wallhacks. This was a thing for the base
`find_potential_targets`, meaning that every basic mob using it was a
dirty haxxor (or very vengeful). Fixed that by making
`find_potential_targets` also check for `can_see()` before proceeding
further down `find_potential_targets/perform()`. `!` The only exception
to this check currently are bileworms.

`!`Goliath tentacles were not spawning in mineral turfs as their
`Initialize()` checked for closed turfs before handling mineral turf
mining. Fixed that as well.

## Why It's Good For The Game

![Dr__Hax_by_Didgeridoo_Dealer](https://github.com/tgstation/tgstation/assets/75863639/fbcbfc1b-f489-435e-bb01-677f55398787)

## Changelog

:cl:
fix: fixed goliaths digging sand that they can't actually reach (behind
windows or inbetween closed turfs)
fix: fixed goliaths melee attacking their target despite the target
running away from goliath melee range
fix: fixed goliath tentacles not spawning in mineral turfs
fix: fixed goliaths summoning tentacles on targets that moved behind
cover but stayed in their targeting range. this applies for most basic
mobs, really, so if any basic mob was targeting you despite you hauling
ass behind cover, they shouldn't anymore
/:cl:

---
## [spartanbobby/cmss13](https://github.com/spartanbobby/cmss13)@[d26452bb9a...](https://github.com/spartanbobby/cmss13/commit/d26452bb9a846091214ced880c5d7a34a6b61048)
#### Wednesday 2023-09-06 18:56:10 by Unknownity

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
## [spartanbobby/cmss13](https://github.com/spartanbobby/cmss13)@[5f5fcd2b27...](https://github.com/spartanbobby/cmss13/commit/5f5fcd2b279b2bd51b5869b0a345b4f964dcb34c)
#### Wednesday 2023-09-06 18:56:10 by Drathek

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
## [evie-lau/PlexAniSync-Mappings](https://github.com/evie-lau/PlexAniSync-Mappings)@[4f85fb8b86...](https://github.com/evie-lau/PlexAniSync-Mappings/commit/4f85fb8b866c169b3059745e77d9c1afc6824cfa)
#### Wednesday 2023-09-06 19:36:28 by Daggersoath

Added series missing when searching with Japanese titles (#66)

* Added series with Japanese titles
Added Japanese titles to synonyms for preexisting series

- I'm standing on a million lives
- Arifureta: From commonplace to World's Strongest
- Bakuman
- Code Geass: Lelouch of the rebellion
- Is it wrong to try to pick up girls in a dungeon?
- How not to summon a demon lord
- Komi can't communicate
- Rent a girlfriend
- My next life as a villainess: All routes lead to doom!
- That time I got reincarnated as a slime
- To Your Eternity
- Welcome to Demon School! Iruma-kun
- Yuri!!! on ICE

* Removed accidental :

* Fixed typo in Yuri on ice season->seasons

* Fixed naming to use english title, japanese as synonym

* Delete stray line

Co-authored-by: Daggersoath <9066690+Daggersoath@users.noreply.github.co>
Co-authored-by: mizz141 <20839616+mizz141@users.noreply.github.com>

---
## [GForceTF/tgstation](https://github.com/GForceTF/tgstation)@[67e97b7877...](https://github.com/GForceTF/tgstation/commit/67e97b787740fd2a5017fd3c66c4f52a0a511a5a)
#### Wednesday 2023-09-06 19:51:37 by RikuTheKiller

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
## [Phoenix-Illusion/CODSOFT](https://github.com/Phoenix-Illusion/CODSOFT)@[8ec2ed5405...](https://github.com/Phoenix-Illusion/CODSOFT/commit/8ec2ed54056535a5c7f3aa4ea61e5339ead182ee)
#### Wednesday 2023-09-06 20:23:01 by Aman Kumar Tiwari

Add files via upload

**Quiz Game - Python-Based Interactive Quiz Challenge**

**Project Overview:**
Welcome to the Quiz Game repository! This Python-based project offers an engaging and interactive quiz experience. It challenges users with a variety of multiple-choice and fill-in-the-blank questions on a wide range of topics. Whether you want to test your knowledge or have some fun, this quiz game has you covered.

**Key Features:**
- Multiple-choice and fill-in-the-blank questions.
- Score tracking and instant feedback on answers.
- A user-friendly and intuitive interface.
- Randomized question order for added challenge.

**Technologies Used:**
This project is built using Python, with the help of Python's built-in libraries for handling user input and randomization.

**Development Process:**
During the development of this quiz game, I focused on creating an enjoyable and educational experience for users. I learned valuable insights into Python programming and user interface design, which helped me refine the project.

**Usage Instructions:**
To play the quiz game, simply run the Python script provided in the repository. No additional installations or dependencies are required. Follow the on-screen instructions to begin your quiz adventure.

**Contributions:**
I welcome contributions from the GitHub community. If you'd like to contribute to the project, please feel free to fork the repository and submit your changes via pull requests. Together, we can make this quiz game even better!

**Acknowledgments:**
I'd like to acknowledge the Python community for their valuable resources and support in creating this project.

**License:**
This project is open-source and available under the MIT License. You are free to use and modify the code, subject to the terms of the license.

Thank you for visiting the Quiz Game repository. Have fun testing your knowledge!

---
## [Idanq1/Stocks-Strategies](https://github.com/Idanq1/Stocks-Strategies)@[d9eaeec064...](https://github.com/Idanq1/Stocks-Strategies/commit/d9eaeec0640a2968e81b4916f143e773fadb4e1f)
#### Wednesday 2023-09-06 21:22:13 by Idanq

FUCKING AWESOME SHITS

I want to add RSI maybe and some other indicators that may help

---
## [Mission23/journal-micah](https://github.com/Mission23/journal-micah)@[5fe3011ebe...](https://github.com/Mission23/journal-micah/commit/5fe3011ebef27cfd9368ddc09a07425818517033)
#### Wednesday 2023-09-06 22:30:13 by Micah

About those people you’re about to eat…

I’ve always found it odd that Riverdale has no big-name grocery store. In Georgia, practically every named city has a Publix and/or a Kroger.

Riverdale has Food Depot and Food Giant or something. The packaging of the food looks off. The colors aren’t right, the logo is a little different, it’s just not what I’m used too. 

Pausing on that for a moment, I’ve gotten more and more skeptical of the food here in Riverdale after inadvertently eating my childhood neighbor. I have never wanted to eat a human being, and would never endorse eating a human being. But… I ate the mom who lived across the street. 

One evening a guy who was always stopping by visiting (typically stealing) came by with a box of food from the food bank and told me I could have it. 

I enjoyed the various items in it and never thought anything of the food in the box. I tossed the box by the front door and that’s when I first noticed things that would have sent Todd Deischer into a rage. 

Deischer was my high school graphic arts teacher at (now West) Jessamine County High School. Deischer made me adapt and overcome the single button mouse on the Apple Mac, and how to even use Twitter way before Twitter was even in existence by teaching me how to KISS. That stands for, Keep It Simple Stupid. He also taught Aldus Pagemaker which works pretty good with one button mice. He was not a fan of Corel. 

The box by my front door looked as though it was made by someone too inebriated to touch a computer, lacking all care for any kind of design and just doing the minimum at their (emphasis on) dead end job at the CIA. No one ever quits there I’ve heard. The box looked like some Corel Draw template with the words “Cheryl’s Best.”

Cheryl Gillespie was by far the coolest mom on the street. She was a stay at home mom with all the coolest animals, lots of dogs and cats, they had birds, aquariums, other furry things and even a SmWIM (that’s, Some monkey Who Isn’t Me) once. She from time to time went to work, part-time but always in a, just guess. Yes, I think she did it for the discounts. She was the mom to my friend David, my sister’s friend April, and was married to the dude with a car so loud it could move the pictures in our house, Terry, he did drag racing on the weekends. Not RuPaul’s version, more like octane so high the gas smelled sweet. She was was definitely cool and they had the neighborhood pool!

Cheryl went missing, along with everyone else from that house on Garden Park Drive in Nicholasville, KY. Parts of Cheryl, her legs, the Creator tells me, showed up at the company whose name appeared on the side of that ugly box that sat by my front door, Primus Labs. 

Primus Labs can take human meats and “spin them into practically anything,” so says the Creator and their website if you read it knowingly. Primus Labs is owned by the CIA. 

I am very skeptical of meats, but I didn’t eat any that day. There were none in that box from the food bank. 

NOTICE: For the record, Deischer was cool as hell, and never to my knowledge (and the Creator just confirmed) had any kind of inappropriate relationship with a student. I figured I’d write that, as Todd Deischer is missing, and the CIA likes to smear it’s victims.

---
## [crawl/crawl](https://github.com/crawl/crawl)@[9db281c723...](https://github.com/crawl/crawl/commit/9db281c7239a55fb109428ccad75eac9b04e15ee)
#### Wednesday 2023-09-06 23:44:58 by DracoOmega

Change Hexslinger starting spells

The new spell list is:
 -Jinxbite
 -Sigil of Binding
 -Inner Flame
 -Cause Fear
 -Dimensional Bullseye

Hexslinger was always troubled. Its spellbook was split across multiple
schools, making them tricky to cast, and they still didn't do much without
ALSO training ranged weapons heavily. Slow was often a trap and in
general the archetype was clunky, without providing sufficient benefit for
splitting your skills between weapons and spells.

The intent of this change is to provide a smoother curve of castable
spells, and more immediate value to training hexes instead of simply
ignoring them in favor of being a 'worse hunter'.

Jinxbite provides a little immediate power to help deal with earlygame
threats with which current hexslinger often struggles significantly.

Sigil of Binding provides powerful utility and can help set up Inner Flame
triggers in a way that the old spellset could almost never safely do in
practice.

Portal Projectile was always a spell that was far better late than it was
early, and so Dimensional Bullseye is now a capstone that provides
even stronger long-term value, but with other easier to cast spells that
let you bridge the gap to it better.

Cause Fear was always good (if you could manage to survive long enough
to have access to it!) and remains untouched.

(Also give them 1 starting level of Fire Magic, to help just a little bit
with getting Inner Flame off the ground)

---
## [AkairyuGestalter/xivanalysis](https://github.com/AkairyuGestalter/xivanalysis)@[c009fd5bcf...](https://github.com/AkairyuGestalter/xivanalysis/commit/c009fd5bcf5a7ae7810f9e30a3f7df648c2d4d43)
#### Wednesday 2023-09-06 23:58:16 by B Fraser

BLU: 6.45 Moon Flute update (#1873)

* BLU: Being Mortal mistakenly had the same actionId as Apokalypsis

* BLU Moon Flute window: Swap out important spells in the burst window

With the new spells in 6.45, BLU's burst window got even more
busy.  It is, technically, still a gain to cast Rose of Destruction,
to use Bristle on Matra Magic, and to use Glass Dance, but they are
all roughly on the category of "you may drop these, either entirely
or just out of the opener".

Adding 4 or 6 new potential actions to the report would've rendered
mostly useless, so instead, this commit makes it so that we expect
any Moon Flute burst to include the following oGCDs:

    J Kick
    Shock Strike
    Feather Rain
    Nightbloom
    Being Mortal
    Sea Shanty
    Surpankaha x4
    Phantom Flurry

And the following two GCDs:

    Matra Magic
    Triple Trident (only if it was off cooldown, for SpS builds)

While there's optimal filler GCDs for the opener, they aren't
useful generic recomendations (Swiftcast => Wild Rage), and they
aren't standard between all openers (Winged Reprobation and Rose of
Destruction are in practice mutually exclusive, and some openers
drop Bristle for a third Winged Reprobation, for roughly the same
potency on every burst but the first one), so we're just
not enforcing them anymore.

It's also optimal to do an extra weave for Glass Dance somewhere in
the opener, but that's now so rarely taken due to spell slot
limitations that giving it its own column in the report will just
add noise.

* BLU Moon Flute: Handle odd-minute Breath of Magic bursts

`Breath of Magic` is a new DoT BLU got this patch.  It lasts 60
seconds and does a silly amount of potency, with the caveat that
only one person can apply it on the target.

Due to BoM's silly potency, ideally it should be reapplied under
Moon Flute every minute, meaning that in addition to the normal
even-minute burst, the BoM applier should be doing an odd-minute
burst too.

Since "odd-minute" and "even-minute" are going to be entirely
encounter-dependent, this commit is using a heuristic:
If they used both `Breath of Magic` and `Song of Torment` under
a given Moon Flute, then this is an odd-minute burst, so few
of the usual requirements apply.

* BLU Moon Flute: Keep support for pre-6.45 BLU logs

* BLU Moon Flute 6.45: changelog

* BLU Moon Flute: Change the heuristic for odd-minute bursts

Per @xiashtra's suggestion, we now base this on whether
Nightbloom is on-cooldown during the moon flute, rather
than checking Song of Torment, which in some edge cases
people may not be taking.

* BLU Moon Flute: Reworded the two suggestions to be a bit less convoluted

* BLU Moon Flute: yarn extract

* BLU Moon Flute: yarn linting

---

