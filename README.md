## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-09-10](docs/good-messages/2023/2023-09-10.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,992,595 were push events containing 2,719,517 commit messages that amount to 145,045,249 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 57 messages:


## [kd-collective/NetHack](https://github.com/kd-collective/NetHack)@[1a64ee1c28...](https://github.com/kd-collective/NetHack/commit/1a64ee1c285f8d9a27e58efa3989a281413f9b8e)
#### Sunday 2023-09-10 00:21:00 by PatR

github PR #259 - paranoid_confirmation:trap

Fairly old pull request from copperwater:  add new paranoid_confirm
setting 'trap'.

The old commit suffered from bit rot and merging needed too much
fixing up despite there not being many bands of change in the commit's
diffs.  I ultimately redid it from scratch, although the two biggest
chunks of code started with copy+paste of the pull request's commit.

It operates like paranoid:pray.  Setting paranoid:trap adds a new
"Really step into <trap>?" y/n prompt when attempting to move
into/onto a known trap, even if an object covers it on the map.
Setting both 'paranoid:Confirm trap' turns that into a yes/no prompt.
(Adding 'Confirm' affects other paranoid confirmations; in addition
to requiring yes<return> rather than just y to accept, it also forces
no<return> to reject.)

However, moving into a known trap that is considered to be harmless
behaves as if no trap was present.  Some of the trap classification
might be out of date; several types of traps have undergone changes
since implementation of the original pull request, notably anti-magic
field.  When the hero is hallucinating, all known traps are considered
harmful since the map no longer reliably describes them.

Preceding a movement command with the 'm' prefix also behaves as if
no trap was present, bypassing confirmation for that move, similar to
how paranoid:swim currently behaves.  Being stunned or confused also
behaves as if no trap was present, taking priority over hallucination.

This updates the documentation.

Supersedes #259
Closes #259

---
## [kesumod/lobotomy-corp13](https://github.com/kesumod/lobotomy-corp13)@[b420c1d519...](https://github.com/kesumod/lobotomy-corp13/commit/b420c1d519b30cd75759de68f6b2abbe0b12a055)
#### Sunday 2023-09-10 01:01:33 by vampirebat74

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
## [cleong14/neovim](https://github.com/cleong14/neovim)@[5970157e1d...](https://github.com/cleong14/neovim/commit/5970157e1d22fd5e05ae5d3bd949f807fb7a744c)
#### Sunday 2023-09-10 01:12:28 by bfredl

refactor(map): enhanced implementation, Clean Code™, etc etc

This involves two redesigns of the map.c implementations:

1. Change of macro style and code organization

The old khash.h and map.c implementation used huge #define blocks with a
lot of backslash line continuations.

This instead uses the "implementation file" .c.h pattern. Such a file is
meant to be included multiple times, with different macros set prior to
inclusion as parameters. we already use this pattern e.g. for
eval/typval_encode.c.h to implement different typval encoders reusing a
similar structure.

We can structure this code into two parts. one that only depends on key
type and is enough to implement sets, and one which depends on both key
and value to implement maps (as a wrapper around sets, with an added
value[] array)

2. Separate the main hash buckets from the key / value arrays

Change the hack buckets to only contain an index into separate key /
value arrays
This is a common pattern in modern, state of the art hashmap
implementations. Even though this leads to one more allocated array, it
is this often is a net reduction of memory consumption. Consider
key+value consuming at least 12 bytes per pair. On average, we will have
twice as many buckets per item.
Thus old implementation:

  2*12 = 24 bytes per item

New implementation

  1*12 + 2*4 = 20 bytes per item

And the difference gets bigger with larger items.
One might think we have pulled a fast one here, as wouldn't the average size of
the new key/value arrays be 1.5 slots per items due to amortized grows?
But remember, these arrays are fully dense, and thus the accessed memory,
measured in _cache lines_, the unit which actually matters, will be the
fully used memory but just rounded up to the nearest cache line
boundary.

This has some other interesting properties, such as an insert-only
set/map will be fully ordered by insert only. Preserving this ordering
in face of deletions is more tricky tho. As we currently don't use
ordered maps, the "delete" operation maintains compactness of the item
arrays in the simplest way by breaking the ordering. It would be
possible to implement an order-preserving delete although at some cost,
like allowing the items array to become non-dense until the next rehash.

Finally, in face of these two major changes, all code used in khash.h
has been integrated into map.c and friends. Given the heavy edits it
makes no sense to "layer" the code into a vendored and a wrapper part.
Rather, the layered cake follows the specialization depth: code shared
for all maps, code specialized to a key type (and its equivalence
relation), and finally code specialized to value+key type.

---
## [ItsMarmite/Paradise](https://github.com/ItsMarmite/Paradise)@[acb7352265...](https://github.com/ItsMarmite/Paradise/commit/acb735226555390c861ecf5e77bc67fd6013afe1)
#### Sunday 2023-09-10 01:26:05 by matttheficus

Gives Vampires Stronger Night Vision at 500 Blood (#21764)

* I SEEEEEEEEEEEEE YOU

* Hal review part 1

* its time to suck at coding

* right, i think im getting somewhere

* testing shit - doesnt work

* im finally freeeeeeeeeeeeeee

* hal review 2: electric boogaloo

---
## [hoffination/smallweb](https://github.com/hoffination/smallweb)@[4be4b78e5b...](https://github.com/hoffination/smallweb/commit/4be4b78e5be3af5ffef591a389c3ac94fa6e6fc7)
#### Sunday 2023-09-10 01:34:07 by Andy

Add https://www.cerealously.net/feed

A wonderful website authored by an a single individual (Dan) about news and reviews in the world of American breakfast cereals. The writing is genuinely lovely, and clearly a product of personal passion.

Note that this is NOT a link affiliate/marketing spam blog for cereals. The author has no direct relation to any cereal companies (at least to my best knowledge), and the writing is clearly the author's direct, personal feelings about the subject matter.

Highly recommend for the small web :)

---
## [DETrooper/Begotten-III](https://github.com/DETrooper/Begotten-III)@[6fc108063f...](https://github.com/DETrooper/Begotten-III/commit/6fc108063ffe73b22cfeeaaad8fdce391117da16)
#### Sunday 2023-09-10 02:28:26 by DETrooper

Kinisger Overhaul, XP Overhaul, Coinslot Changes, Bug Fixes

	- Added alliedfactions table to faction tables, used for the Holy Hierarchy and Gatekeepers.
	- Added missing firearm cloak cooldown to the 'Cloak of the Black Hat' ritual cloaking.
	- Added new tactile sounds for the Coinslot.
	- Added status effects in the tab menu for the 'Favored' belief, as well as the following traits: 'Clumsy', 'Cross Eyed', 'Gluttony', 'Insane', 'Pacifist', 'Scavenger', and 'Winded'.
	- Added the 'Forgemaster', 'Master Medicus' and 'Squire' Gatekeeper ranks to the ranks of authority table, allowing them to proclaim and open tower blastdoors.
	- Buffed the blood loss reduction of the 'Embalmed Heart' charm from 25% to 40%.
	- Damage/Kill XP Rework:
		- Characters of the same faction (excluding wanderers) no longer receive XP for damaging/killing eachother unless possessed. This also applies one-sidedly for Kinisgers so as to not blow their cover.
		- Damage XP now scales with enemy sacrament level similar to kill XP.
		- Damage XP is now capped with the enemy's remaining HP. This will prevent you from getting crazy XP from doing crazy damage that exceeds someone's health (i.e. with the 'Assassin' belief).
		- Decreased the amount of XP that killing other characters gives you, but this should be compensated by the increased damage XP.
	- Disguised Kinisgers are now highlighted in blue for friendly Children of Satan when in close enough range, and also will show fellow CoS characters which subfaction they're disguised as in their subfaction description.
	- Disabled famine variable that was still enabled in the code for Gatekeeper Rations.
	- Fixed a bug recently introduced where you couldn't close doors.
	- Fixed the Advanced Blood Test Kit not detecting Kinisgers.
	- Fixed the 'Enduring is the Bear' belief giving more gunshot injury resistance than intended.
	- Fixed the /promote and /demote commands requiring a charswap if run on a character other than oneself.
	- Fixed UI bugs with the Kinisger appearance change ritual.
	- Fixed unrecognized Kinisgers having yellow physdesc text.
	- Gatekeeper standard issue kits will now be issued from the Coinslot automatically, provided there is enough coin in the treasury.
	- Improved the blacklisted names for character creation to account for schema faction ranks dynamically.
	- Increased maximum banked Gatekeeper salaries from 3 to 4.
	- Kinisgers can no longer disguise as the Holy Hierarchy.
	- Kinisgers can no longer disguise as specific Gatekeeper ranks, instead they will start at the beginning rank of whichever subfaction they choose.
	- Kinisgers can now use the vendors of factions they're disguised as.
	- Kinisgers disguised as Gatekeepers can now obtain salaries and Gatekeeper rations from the Coinslot.
	- Restored 'Faith of the Dark' as a faith option for Clan Reaver Gores.
	- Sacrificing characters at the altar or selling them to the Reaver Despoiler will now increase your character's kill counter.
	- Salesmen in the Tower of Light now pay a tax to the Tower treasury when buying or selling items.
	- The 'Cunning of the Sister' belief now gives XP for damaging as well. Made the belief also apply for selling characters into slavery for the Reaver Despoiler.
	- The 'Faith of the Mother' belief now gives double XP for healing other characters.
	- The 'Strength of the Father' belief now gives double kill XP to bears and thralls, and now also gives XP for damaging as well.
	- The 'Watchful is the Raven' belief now reduces the chance of receiving injuries by 50%. This can be stacked with 'Hide of Steel' for total immunity to injuries.
	- The blastdoors of the Tower of Light can now only be opened from the outside by Gatekeepers of Emissary rank or higher, as well as Holy Hierarchy members. This includes Kinisgers as well.
	- The /promote and /demote commands now work for disguised Kinisger gatekeepers. Also added the ability for Kinisgers to use these commands if they advance high enough in rank.
	- The 'Favored' belief can now save you from blood test false positives.
	- Trying to collect a salary from the Coinslot when none are available now displays a more clear message.
	- Updated default salesman to remove exploit items, as well as some adjustments to flavor text and item prices.

---
## [doppelxyz/metamask-blocklist](https://github.com/doppelxyz/metamask-blocklist)@[10af18a6a0...](https://github.com/doppelxyz/metamask-blocklist/commit/10af18a6a09dfae9b0506c4d475a7cad624f3848)
#### Sunday 2023-09-10 03:04:39 by Mich

Block 187 scams (#13467)

* block scams

``
    "0xcoin.in",
    "2muskx.cc",
    "2tesla.cc",
    "2xmusk.space",
    "2xtesla.cc",
    "500px.com",
    "abict.pro",
    "aerodrome.capital",
    "aibb.claims",
    "ait.gifts",
    "akidcalledbeast.gift",
    "algotradersguild.com",
    "alskafu.com",
    "alskafu.net",
    "anaxine.finance",
    "angrycat.best",
    "angrycat.guru",
    "app-1icnh.com",
    "app-unislwap.org",
    "app3-vniswsepprotocols.top",
    "applediscounter.store",
    "appsv3-panskiekprotocol.top",
    "appsv3-pasnekekswap.top",
    "appv3-unisqswops.top",
    "appv3-unsiwpawprotccol.top+",
    "arbitruun.foundation",
    "arkhamintellingence.net",
    "articlesfox.com",
    "autisminteligence.lol",
    "avifavindia.com",
    "axieinflnity.com",
    "axretailgroup.com",
    "babydogenft.org",
    "balances-celsius.network",
    "bald-base.com",
    "bestaq.com",
    "bigeyescoinclaim.netlify.a",
    "bitinauts.zone",
    "blogsbeta.com",
    "bps-sber24.online",
    "bpsbank24-by.online",
    "c-elsius-withdraw.network",
    "c-elsius.com",
    "cake.claims",
    "cascadune.co",
    "celsi-us-recover-assets.com",
    "celsiius-withdraw.com",
    "celsiu-s-network.com",
    "celsius.pages.dev",
    "celssius-network.com",
    "chainlinks.gift",
    "circleclaim.org",
    "claim-boredapes.com",
    "claim-celsius.network",
    "claimcrv.com",
    "claims-celsius.network",
    "claims-coinbase.com",
    "co-nextget.com",
    "coinstats-app.online",
    "connextairdrop.pages.dev",
    "connextdrop.network",
    "coredao.to",
    "correosprepaqa.com",
    "creditors-celsius.network",
    "crypto-uniswap.org",
    "cryptrecover.com",
    "customer-club.com",
    "customersurveypanel.net",
    "datebest.net",
    "dexstools.com",
    "dfgdsasd.ru",
    "digicask.com",
    "discussionarchive.com",
    "dnrbpo.com",
    "dodo-opros.online",
    "drop-aave.com",
    "drop-jasmy.com",
    "drops-pancakeswap.org",
    "duozap.com",
    "edveno.com",
    "enter-milady.xyz",
    "ethereum-pow.online",
    "evilpepecoin.top",
    "evri-resend.com",
    "exchange-okx.com",
    "finttv.cc",
    "finttv.ga",
    "freeclaim.xyz",
    "friendclaim.live",
    "huangcdev.com",
    "investavoyager.com",
    "invisible.sale",
    "kidsofapocalypse.us",
    "layerzcro.network",
    "layerzeronatwork.xyz",
    "link3tcyberconnect2.tech",
    "livedappsconnect.website",
    "lovelys.gift",
    "mailapp-metamask.com",
    "mailserver-metamask.com",
    "meetyemmy.com",
    "metamask.free-claim.pro",
    "metamask4.app",
    "metamaskjobs.io",
    "metamasktokens-drop.com",
    "metamseak.io",
    "mong.gift",
    "moonbirds.gift",
    "msdrainer.site",
    "mummy.gift",
    "musk-2023.com",
    "musk2xbtc.space",
    "muskbtc2x.space",
    "muskx2.cc",
    "muskx2k.cc",
    "mute.claims",
    "nftangrycat.online",
    "opepen.gift",
    "opnx.gift",
    "org-polygon-v3-defi.site",
    "pancakeswap.affiliate-program.online",
    "pasnkakesvawp-fknance.com",
    "pepexplorers.com",
    "pepperjellys.com",
    "pinkrsale.com",
    "pinkrsale.org",
    "pyusderc.com",
    "quickswap.claims",
    "rdnt.capital",
    "recoverassetscellsius.network",
    "recovercellsius-assets.com",
    "rizmonkey.com",
    "robinsood.info",
    "rtfkt.gifts",
    "s2tesla.cc",
    "s2tesla.com",
    "schasb.com",
    "shabaswap.com",
    "shibarium-claim.com",
    "shibavoucher.top",
    "shibavpepe.io",
    "shilbarum.online",
    "shimbarium.online",
    "slingshot.claims",
    "sonikcoinsofficial.com",
    "sonikcoirn.org",
    "spectacuiardate.com",
    "spsinghcharitabletrust.com",
    "stepnairdrop.top",
    "sushirewards.org",
    "swaprum.io",
    "tesla-giveaway.pro",
    "tesla-stocks.com",
    "tesla-stocks.us",
    "tesla2.cc",
    "tesla2s.cc",
    "teslasx2.com",
    "teslax.cc",
    "teslax2e.cc",
    "teslax2s.cc",
    "teslax2s.com",
    "thetaclaim.com",
    "tradingview.expert",
    "usdcoincrypto.com",
    "usuperfund.com",
    "vela.claims",
    "velocore.gifts",
    "verify-metamask.business",
    "vitalik-qr.com",
    "vizebasvurusu.online",
    "vulcanforged-event.com",
    "wallet-web3.com",
    "wallrstmemes.com",
    "web-uniswap.org",
    "web3-metamaskd.com",
    "withdraw-cellsius.network",
    "withdraw-celsius.network",
    "withdraw-stretto.com",
    "world-circle.net",
    "worldcoin.is",
    "wrapped-gifts.io",
    "x-coin.in",
    "x2teslas.com",
    "xlretailgroup.com",
    "xmusk2.cc",
    "xrpspot.info",
    "xtesla.cc",
    "xtesla2.cc",
    "xteslas2.cc",
    "yearnn.com",
    "yecoin.in",
    "zerc.pro",
    "zksyncy.com",
    "zoras.org",
```

* fix json

* Update config.json

* fix json

* block

```
    ""syntehtix.io",
    "convex.gift",
    "join-gamma.com",
    "inverse.exchange",
```

* Update config.json

block
```
    "claimscrv.com",
    "beincrypto.company",
    "claim0x.org",
```

* Update config.json

* dupe

dupe

* Update config.json

* dupe `drop-aave.com`

newly appeared dupe `drop-aave.com`

---------

Co-authored-by: deshvin <2859402+deshvin@users.noreply.github.com>

---
## [RikerW/dNAO](https://github.com/RikerW/dNAO)@[ff36e9df57...](https://github.com/RikerW/dNAO/commit/ff36e9df5756254fa9abdb222301deef8f5bb6ac)
#### Sunday 2023-09-10 03:14:28 by RikerW

add #style toggle for passive-safe attacks and refactor #style code

refactors #style code to better handle generic "fighting forms" not just lightsaber vs. breaking out early for mystic forms vs. whatever
now, it handles mystic, lightsaber, passive toggle, and has handling for an as-of-yet non-existent knight forms. further categories of forms WILL need to have handling added, but it should be pretty simple - some function doFooForm() that handles the window code or whatever, and the criteria under which to have that as a list option / the code for adding it as a list option to the #style menu itself

also removes the inability to use #style ls forms if you're not wielding a lightsaber. now you can do it if wielding, uswapwielding, and if you have trained any lightsaber skills before. this DOES remove the check for weapon skill since its not always true, so better messaging for that could be nice, but it shouldn't be a huge deal - since you still have to be wielding a saber, and it'll tell you if you're unskilled in shii-cho or something. dunno. open to suggestions for improvements here
shitty knight form defines are based on the ones in the etherpad with absolutely no handling for any of them to do anything, just what's needed to set/check them without impossibles. there is no way to get those skills so they never show up and shouldn't matter

also refactors form setting/checking code slightly. now, each batch of 32 forms is mutually exclusive - so FFORMs 0-31, 32-63, etc. this is so that you can have both a lightsaber AND a knight form active, but not two ls or two knight forms active. this cannot be extended to monk forms since they can all be individually toggled.

passive avoidance code uses the new u.uavoid_passives to determine if you're a coward or not, and refactors my previosu stuff into the new non_contact_attk(attk) macro. its only available in #style if your current attack routine (NOT by the book, so including star emp ring or black web or something) includes a non_contact_attk(attk) to prevent it from confusing people when not relevant. however, if you're currently avoiding unsafe attacks, you can always turn that off - so that if you take off the ring or unbind web or something you're not stuck making no attacks forever or until you regain the ability to turn it off

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[009af8c2ce...](https://github.com/lessthnthree/tgstation/commit/009af8c2ce5c18ca4fdaceb4e4d2c17d8e8d6d00)
#### Sunday 2023-09-10 03:16:44 by nikothedude

[TEST-MERGE FIRST] Wound refactor number two: Full synthetic support (#78124)

## About The Pull Request

Heavily refactors wounds AGAIN.

The primary thing this PR does is completely change how wounds are
generated and added - while the normal "hit a guy til they bleed" stuff
works about the same, asking for a specific type of wound, say, like how
vending machines try to apply a compound fracture sometimes, isnt going
to work if we ever get any non-organic wounds, which the previous
refactor allowed.

With this PR, however...
* You can now ask for a specific type of wound via
get_corresponding_wound_type(), which takes wound types, a limb, wound
series, etc. and will try to give you a wound fitting those
specifications - but also, a wound that can be applied to a limb.
* This will allow for a vending machine to apply a compound fracture to
a human, but a collapsed superstructure (assuming my synth wounds go in)
to a robot

There are now new "series types" and "wound specific types" that allow
us to designate what series are "mainline" and randomly generatable, and
what are "alternate types" and must be generated manually - you can see
the documentation in wounds.dm.

The behavior of limping and interaction delays has been abstracted to
datum/wound from bone wounds to allow just, general ease of development

Pregen data now allows for series-specific wound penalties. Example: You
could set a burn wound's series wound penalty to 40, which would make
wound progression in the burn category easier - but it would not make it
any easier to get a slashing wound. As it stands wound penalties are for
wounds globally

Scar files are now picked in a "priority" list, where the wound checks
to see if the limb has a biostate before moving down in said list.
Example: Wounds will check for flesh first, if it finds it - it will use
the flesh scar list. Failing that, they then check bone - if it uses
that, it will use the bone scar list. This allows for significantly more
modular scars that dont even need much proc editing when a new wound
type is added

Misc changes: most initial() usage has been replaced by singleton
datums, wound_type is now wound_types and thus wounds can accept
multiple wound types, wounds can now accept multiple tool behaviors for
treatment, wounds now have a picking weight so we can make certain
wounds rarer flatly,

This PR also allows for wounds to override lower severity wounds on
generation, allowing eswords to jump to avulsions - but in spirit of
refactoring, this has been disabled by default (see pregen data's
competition_mode var).
## Why It's Good For The Game

Code quality is good!

Also, all the changes above allow wounds to be a MUCH more modular
system, which is one of its biggest problems right now - everything is
kinda hardcoded and static, making creative work within wounds harder to
do.

## Changelog
:cl:
refactor: Refactored wounds yet again
fix: Wounds are now picked from the most severe down again, meaning
eswords can jump to avulsions
fix: Scar descs are now properly applied
/:cl:

---
## [Chris-plus-alphanumericgibberish/dNAO](https://github.com/Chris-plus-alphanumericgibberish/dNAO)@[2390fc0afa...](https://github.com/Chris-plus-alphanumericgibberish/dNAO/commit/2390fc0afaf7d161022f9b0addab607171c0615f)
#### Sunday 2023-09-10 03:25:53 by ChrisANG

Squashed commit of the following:

commit efef78be8af879d37a73949ee49c6019f0feba9a
Author: chris <ohmygod.stopitwiththis.com>
Date:   Sun Aug 27 16:08:44 2023 -0400

    YogSothoth twincast: Adjust make web monster spell to barf bolt

    Web is really annoying

commit e504c955ca771b5932933b1b077441b05849ad7a
Author: chris <ohmygod.stopitwiththis.com>
Date:   Sun Aug 27 13:02:43 2023 -0400

    Wizcult debug command

    Join any cult, manipulate cult mutagen, favor, and devotion levels.

commit 4bab4cf7fe3fa2a5891df15983837f234fa0fee9
Author: chris <ohmygod.stopitwiththis.com>
Date:   Sun Aug 27 12:33:56 2023 -0400

    Bugfix: Illumination of Shub gave no benefit

    Failed to use the modified en bonus.

commit ac56c820d3b00d33437f87d5deafd8719f63950c
Author: chris <ohmygod.stopitwiththis.com>
Date:   Sun Aug 27 12:32:25 2023 -0400

    Improve "make weaker"/bubbling yog-sothoth weapon effect

    Now drains 2d6 hp (leaving at least 1 current HP)

    Rolls resistance vs artifact weapons, draining a like amount of hp bonus (vs. PC) or maxHP/levels (vs. monsters) on a fail.

    This makes it non-pointless vs. the vast majority of targets.

commit e6c258aa4d37a8af23a844a5d1f93e8d2b569eea
Author: ChrisANG <you@example.com>
Date:   Fri Aug 18 15:30:43 2023 -0400

    Tweak: Dark young can talk

    They can in lore, and not being able to talk is pretty bad in a permanent form.

commit cfdd304dd0943f66e3fd2818a6259e4a4869da75
Author: chris <ohmygod.stopitwiththis.com>
Date:   Sun Jul 30 01:20:40 2023 -0400

    Yog-Sothoth Cult and cult revisions

    Madmen now gain cult value at 70% the normal rate (which makes it easier for them to get multiple major boons/fully exploit cults as a Bokrug madman).

    Cult mutations general handling
    -Unified list+basic utility macros in mutations.c and mutations.h
    -All cults track mutagen consumed and mutations granted.
    --Only Shubbie and Yog actually use these counters currently.
    -Mutations have a body part associated with them. This is not currently used.

    Yog-Sothoth (based heavily on Through the Gates of the Silver Key and The Dunwich Horror, and also Elden Ring)
    -Binder spirit
    --Binding duration will not count down while you have the silver key in inventory
    --Causes you to passively attack adjacent targets with blood-sucking tentacles for 3d3 damage
    --Monsters with a keen sense of smell typically spawn hostile, and always know your position (As a foulness shall ye know Them)
    --Ritual: The seal must be drawn on a square with a portal, teleport trap, or levelport trap, OR you must have the silver key in open inventory.
    --Skill: Firearms (time travel)
    --Passive: Protection from shape changers, bloodsense
    --Actives:
    ---Burst of Madness: Fire a ray of magenta fire in the chosen direction. This ray can be reflected but does not bounce off walls. The ray deals fire and magic damage, and exposes the target to your madnesses (sharing your madnesses gains cult credit).
    ---Unendurable Madness: Causes multiple magenta fire explosions in the chosen direction. These explosions repeatedly expose targets to your madnesses. These explosions require both fire and magic res to resist the damage.
    ---Contact Yog-Sothoth: Gain a boon or major boon from Yog if your cult credit is good.
    --Mark: the tentacles, strange feet, possibly flaming eyes if those mutations are chosen.
    ---Requires clothing, boots, and sufficient eyewear.
    --Taboo: destroying a trap (levelport, teleport, magic, or polymorph) with a wand of cancellation.
    -Boons
    --Yog-Sothoth weapon oprop (major)
    --Lesser magic oprop (major)
    --Create twin sibling monster (major)
    --Mutate (mutagen)
    --Escape from curses(minor): Teleport cursed items to floor
    --Return of memory (minor): +10% memory for all spells
    --Continued companionship (minor): +20% (1000 moves) for all binding durations
    --Return of your twin (minor): Summons the twin sibling, retreving it from another level and/or restoring it from "death"
    --Primordial waters: technically a potion type, mostly granted as a boon effect. Acid damage fixes petrification, increases energy. Builds Yog-Sothoth mutagen.
    -Weapon oprop
    --As with shubbie's oprop, changes effects. Unlike shubbies oprop, "ticks" at a rate of 1/100 turns.
    --Teleport theft (starry): Teleports one piece of armor off the target's body, or deals +1x damage if they aren't wearing armor.
    ---Random-teleport-obj code is refactored to avoid placing the object at your feet before relocating it.
    --Vampiric (grasping): Drains the target's blood, healing you, giving sothoth credit, and possibly draining levels from the target.
    --Flame and fear (groaning): +1d6 damage, +1d6 additional if non-fire-immune, inflicts fear/panic on the target
    --Depower (bubbling): Polymorphs the target into their least-mature form, if they fail a resist check.
    --Dessicate (auroral): +1x vs. watery monsters, +0x vs. nonliving or anhydrous monsters, +.5x otherwise, healing wielder, grants sothoth credit.
    --Stench (stinking): +1d6 vs. non-breathless non-poison-immune targets. Targets that eat may vomit, losing turns (if you are hit you become vomiting, which is a very dangerous situation!)
    --Magic (cerulean): +4d6+spe magic damage (min +1)
    --Mad fire (magenta-burning): Exposes the target to your madnesses if you *fail* a generic unblockable madness check, deals +2d6 damage to non-fire-res targets AND +4d4+spe damage to non-magic-res targets if they are exposed.
    -Mutations:
    --The total amount of mutagen requried for each new mutation grows quadratically ((m+2)^2, where m is the number of mutations granted so far)
    --Gaze 1: Enables the first mad fire active ability (burst of madness). The twin also gains a version of this spell, if it has spellcasting.
    --Gaze 2: Can only be chosen after gaze 1. Enables the second mad fire active spirit ability (unendurable madness). Increases the chance of the Twin casting its madness-fire ray spell.
    --Twin mind: While Yog is bound, you make passive monster spellcasting attacks with range 2 if you don't make a tentacle attack. Also gives the twin spellcasting.
    --Twin dreams: While Yog is bound, grants a mind blast or boosts existing mind blast (+(lev+7)/14 dice, two rolls to hit (twin dice only apply if the first roll hits)).
    --Twin lifesave: While Yog is bound and the twin sibling is visible, Lifesaves the PC at the expense of the pet twin (The twin can be revivied as a minor boon, but the mutation will need to be re-applied).
    -Hyperborean dial
    --This puzzle/tool teaches the PC the Yog Sothoth seal when completed.
    --The puzzel can only be completed while asleep (though extra puzzles can be completed up to the current limit by applying them)
    --Applying a puzzle that is at the current limit reminds the player that the PC solved it while asleep.
    -Outlands inclusion: Sentenel Clearing
    --A ring of "standing stones" (boulders in rock squares) and some leveled-up shaman/cleric monsters of the yog-sothoth faction.
    --Has a special levelport trap in the center of the ring. Being affected by this trap (meaning *not* magic resistant!) teaches the PC the Yog-Sothoth seal.
    -Invoking the Silver Key while standing on a Yog-Sothoth altar (such as those found in R'lyeh) teaches the Yog-Sothoth seal.
    --This sets the artifact invoke timer.

    -Twin Sibling
    --2d6 vampire, d12 phys, d6 spells, phys scaling, clings to ceiling.
    --Attacks adjacent monsters with passive blood-sucking tentacles
    --Imune to polymorph
    --Vanishes while Yog-Sothoth binder spirit is not bound.
    --While not on level, has a 1/6th chance to move one level closer or farther from you, and a 1/66th chance to move between dungeons to follow you.
    ---This behavior can be suppressed by instructing it to "wait"
    --Does not actually die when killed, but does vanish until you re-summon it as a minor boon.
    --Gains spellcasting if you have the "Twin Mind" mutation
    --Gains no cooldown casting if you have the Shubbie Radiance mutation
    --Gains mind blasts if you have the Yog-Sothoth Twin Dreams mutation
    --If lower level than you, gains a HP from every kill, rapidly leveling up as a result.

    Shub Nugganoth revisions
    -Add a semi-dedicated "itinerant priestess" creature to replace the generic shubbie priestess in the Madman quest
    --Weapon, offhand weapon, holy touch after insight 40, d6 clerical spellcasting, 4d4 magm retalitory attack, naturally magic-immune, can reach level 30. An alien from the universe next-door.
    --Is a "monk" as well as a "priest"
    --Gets the two Shubbie priestess spells
    --Can heal as a touch after 40 insight, and has a built-in unicorn horn
    --Can sing to back up the PC (showing off the adjusted messages for mistweaver monsters generally)
    -Add mutations. Mutations are minor boons. The first mutation requires 3 goat's milk potions to have been drunk, each subsequent mutation requires one more potion than the previous (so 4 more/7 total, then 5 more/12 total, etc.)
    --Abohorrent spore: Slotless lifesaving that converts the PC into a permapoly'd dark young. This uses up the spore, though the PC can re-purchase the mutation.
    --Crawling Flesh
    ---Improves healing. 1/3rd chance of healling 1 HP as a result of a "failed" flat madness role.
    ---When below 1/2 HP, may suddenly heal +1/2 HP as a result of a successful insight check. This costs 40 to 100 nutrition and drives nearby monsters insane and/or causes them to puke and become immoble for 4 turns and flee for 44 turns.
    ---Also causes the Yog-Sothoth Twin to heal +1 HP per turn.
    --Tendril hair
    ---Prevents item theft attacks.
    ---Gives bonus to resist seduction attacks.
    --Mindstealing tongue
    ---Adds an extra attack that causes the struck target to attack an ally
    ---If the yog-sothoth twin pet can cast spells, this enables a crush bolt spell.
    --Radiance
    ---Reduces your HP bonus by your Insanity, increases your energy bonus by Insanity.
    ---Since the HP bonus adjustment happens before diminishing returns is calculated, this can be a good deal if you have drunk lots of full healing.
    --Shifting mind
    ---"Un allocates" all skill points, allowing respecing. This mutation isn't gained, and can be re-selected later.
    --Claws
    ---If the yog-sothoth twin can cast spells, this enables a spacewarp spell.

    Silver Flame revisions
    -Curse proof glaze revised to be body armor only, 100%
    -Wrath gloves: Increases damage bonus by 50%.
    -Share burdens footwear: +200 (or 20%) carry cap.
    -Preserve life helms: Your helm provides life saving when worn. The property is removed when the effect triggers; the helm is not destroyed. The helm will be eligible to have the property re-added as a later major boon.

    Ibite Arm revisions
    -Add upgrades, favor, and a boon counter.
    --The Arm can be upgraded via #invoke (uses invoke timer)
    --These upgrades don't increment other boon/wish counters, so the Arm stacks with other cults very effectively
    -Favor:
    --Gains favor when killing human mercenaries, nobility, or priests
    --Deals +1d10 damage vs. all humans (human-bane, effectively)
    -Upgrades:
    --Wave: The hand portion (not the elbow/primary attack) deals +6d6 water damage instead of +2d4
    --Revoke: The hand portion takes the targets inventory and drops it on your square. The target rolls resistance *after* each item is taken, ending the effect on a success.
    --Destroy: Deals +1x damage vs. unalive targets. The hand portion digs out squares.
    --Teleport: The Arm can be used to teleport via #invoke (uses invoke timer)
    --Levelport: The Arm can be used to levelport via #invoke (uses invoke timer)
    --Branchport: The Arm can be used to branchport via #invoke (uses invoke timer)
    ---Branchport code is re-factored to avoid copypasta.
    --Reflect: The Arm grants Reflection when wielded, AND can have Silver Flame oprops applied.
    -Influenced by some other effects
    --Shubbies clawed hand mutation confers claws to the arm as well

    Quest revision
    -Bergonic chair
    --Starts with 3d3 charges.
    --Sitting consumes a charge, shocks you, and may
    ---Give a point of int (or other mental stat, 33%)
    ---Drain a point of wis (or other mental stat, 33%)
    ---Give 500-599 turns of clairvoyance.
    ---Do enlightenment
    ---Grant knowledge of your pack contents (0(all)-4 items) plus 2-7 random objects.
    ---Aggravate monsters
    ---Deal fire damage as well
    ---Enchant helmet by +1 (to a max of +5)
    ---Inflict nightmares (hallu plus confusion) and sleep for 200-399 turns.
    -Side area on observation level: currently contains a room with a hyperborean dial, a bed, a bergonic chair, and a writing desk with some sleeping potions. Overall should be a pretty big hint about how to use the dial, though you probably don't want to do it in the quest. The lower regions of the quest also contain bedrolls.

    Bugfixs:
    -Shuby should give *subsequent* holy symbols with 1/4 probability, not the first (which still depends on gifts?)
    -Centaur chieftains in the lost cities are goat monsters.
    -"straitjacketed_mon" now includes shackled arms
    -Fixed a bug in the code that doubles cold explosion damage for fire-resistant monsters.
    -Cha casters (Psions) can also spellcast through helms of telepathy
    -A_NONE PCs are also burned by holy water
    -A_NONE PCs also get alignment from foocubi
    -Monsters with ONLY telepathic vision are always affected by PC mind blasts (similar to how a blind PC is affected).

---
## [Rvali/Skyrat-tg](https://github.com/Rvali/Skyrat-tg)@[450a9d0ea0...](https://github.com/Rvali/Skyrat-tg/commit/450a9d0ea05703cbf40657d8d16e8955c3b59a93)
#### Sunday 2023-09-10 03:55:05 by SkyratBot

[MIRROR] Funny clown internals [MDB IGNORE] (#23457)

* Funny clown internals (#77963)

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

Co-authored-by: CRITAWAKETS <sebastienracicot@ hotmail.com>
Co-authored-by: Ghom <42542238+Ghommie@ users.noreply.github.com>

* Funny clown internals

---------

Co-authored-by: GuillaumePrata <55374212+GuillaumePrata@users.noreply.github.com>
Co-authored-by: CRITAWAKETS <sebastienracicot@ hotmail.com>
Co-authored-by: Ghom <42542238+Ghommie@ users.noreply.github.com>

---
## [Rvali/Skyrat-tg](https://github.com/Rvali/Skyrat-tg)@[5f9e018543...](https://github.com/Rvali/Skyrat-tg/commit/5f9e0185438ddfc3011a22fa237d714e9bcf367b)
#### Sunday 2023-09-10 03:55:05 by Nerevar

[IT'S READY NOW!] [MODULAR] Razor Claws Augment (#23050)

* initial

* god i hate byond

* there we go

* oh right

* Apply suggestions from code review

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

* wew

* Manual map merge

* wew

* Apply suggestions from code review

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---------

Co-authored-by: Snakebittenn <12636964+Snakebittenn@users.noreply.github.com>
Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>
Co-authored-by: Giz <13398309+vinylspiders@users.noreply.github.com>

---
## [BlueWildrose/Citadel-Station-13-RP](https://github.com/BlueWildrose/Citadel-Station-13-RP)@[784efe9b51...](https://github.com/BlueWildrose/Citadel-Station-13-RP/commit/784efe9b514256072f90ffbae9acebe38b2f5b4f)
#### Sunday 2023-09-10 04:35:25 by CharlesWedge

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
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[ed10226825...](https://github.com/tgstation/tgstation/commit/ed10226825bbef4e605d7e831ebb1d8f30f805f4)
#### Sunday 2023-09-10 04:42:09 by Jacquerel

Desouls Hivelord (#78213)

## About The Pull Request


![dreammaker_RJz4brjobM](https://github.com/tgstation/tgstation/assets/7483112/e5e4a3e9-ea6b-47f9-887c-3339d24d3fa8)

Replaces the sprite of the hivelord with a new one, in my continuing
quest to annihilate the old asteroid mob sprites.
A (never completed) asteroid mob resprite was actually my first PR, this
one is my 200th.
I am also planning on fucking with basic mob versions of these mobs some
time but the sprites can be atomised out.

In addition to replacing the old-ass MSPaint sprites, this PR also adds
a short death animation effect to the hivelord brood (from hivelords or
legions) which looks nicer than them just vanishing instantly upon
death.

Look at this video for an example of the animation:
https://www.youtube.com/watch?v=cKaskN5-y2A

## Why It's Good For The Game

Looks nicer.

## Changelog

:cl:
image: Hivelords have a new sprite.
image: Hivelord and Legion brood have a death animation.
/:cl:

---
## [mitaka78/room-of-1000-petals](https://github.com/mitaka78/room-of-1000-petals)@[dd80edd9f4...](https://github.com/mitaka78/room-of-1000-petals/commit/dd80edd9f47aa662e3cb35268e6a510d4c1192cd)
#### Sunday 2023-09-10 04:42:55 by mitaka78

fucing hell.  weird ass implementaiton of the fucking path  thing. idk. You cantcheck if a path exists. So I have to use a try catch block insead. Fucking Incorrect and correct drink message implementaiton softcoded and all that moter

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[d1afd66508...](https://github.com/necromanceranne/tgstation/commit/d1afd66508ed3474ca6179d54294742bef531419)
#### Sunday 2023-09-10 05:14:29 by san7890

The Curse Of The Slot Machine - Now Clone-less (#77841)

## About The Pull Request

Hey there,

I think it's commonly held that clone damage sucks and is overused. One
of the last places where it was in slot machine code as a type of
"immutable" damage that would cause you to die if you didn't leave and
get medical attention. It had a lot of silliness and I'm not sure if a
lot of it was meant to work the way it was, but here we are.

So, what's the changes?

* The Cursed Slot Machine will give you a status effect that will
"curse" you with repeated damage. After five curses, you get gibbed
(similar to the old behavior of the machine). Each curse has it's own
change to the status effect, with a lot of depth included. Let me know
if the fluff messages about the status effect change sucks, I think it's
neat though.
* A person with the curse will smoke. I wanted this to look a bit more
"steamy" or grey, but I think it's a decent way of communicating that
shit is fucked up with that dude.
* You also get a branded wound after your first failure at the slot
machine. Ouchers. Should get it looked at by a doctor.
* We also throw a nice screen alert and all of that jazz.
* I also cleaned up all of the code relating to the slot machine
(including a stupid double and), and did some tinkering with the status
effects framework to get the desired effect I wanted. I hope you enjoy
it as much as I did making it. We use cooldowns and stuff between slot
machine pulls.
* If _anyone_ wins on the slot machine, all curses/brands are lifted.
Lucky jackpot!
* A lot of the stuff in this code has a lot of vars that might not be
modified codewise in case admins still want to jank with this for
events.
## Why It's Good For The Game

Clone damage stinks, and I don't really like it as a way to subvert the
whole "oh you can't use legion cores to get your way". It's a cursed
slot machine, and it should do long term damage so that even if you
expend all of the resources on the station, it might all be for naught.
It's a horrible price to pay in your search for that d20. I think the
negative side effects are pretty OK as far as balance, earlier
iterations of this concept had you die _way_ too fast.

All in all, it's just way more of an interesting interaction than "you
take damage and then go to medbay and then come back in the hopes of
gambling a d20".
## Changelog
:cl:
add: The Lavaland Cursed Slot Machine of Greed suddenly seems a lot more
sinister...
refactor: Instead of taking clone damage from the cursed slot machine,
you now get a status effect with a number of curses associated with it.
There's some interesting florid language associated with the status
effect as a nicety until your eventual gibbing from chasing that prize.
/:cl:

I remain undecided if I should keep the curse limit uncapped (but have
the damages increase rapidly after the 5-curse threshold), so I left it
as the `gib()` from the old code. Let me know your thoughts, but I
really don't like the thought that getting the fabled d20 is easy.

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [Praytic/youtd2](https://github.com/Praytic/youtd2)@[a54a2d0bd2...](https://github.com/Praytic/youtd2/commit/a54a2d0bd2f2f79b6f0b93050819feab45b3aeb3)
#### Sunday 2023-09-10 05:43:01 by Kvel2D

Fix buff cleanup for some cases

Cleanup was not being performed for cases like "Stun Revenge" creeps
\ stunning tower and then tower getting sold or transformed
This happened because none of the usual triggers for cleanup happened:
\ - tower didn't die, so target.death didn't happen
\ - buff timeout didn't happen because tower is sold before buff expires
\ - buff handler wasn't removed because the handler is the buff type
\ which is a global variable in WaveSpecial
Fix by adding another trigger for cleanup which happens on buff's
\ own tree_exiting signal

---
## [CLimeburner/Iconic-Affordance-Interactions](https://github.com/CLimeburner/Iconic-Affordance-Interactions)@[5ad17d4335...](https://github.com/CLimeburner/Iconic-Affordance-Interactions/commit/5ad17d43359ef6de6b5777c910dbe8cc269e7f97)
#### Sunday 2023-09-10 06:12:33 by CLimeburner

Built the shooter prototype.

Prototype is in accordance with circuit.png under the v001 folder, where the laser diode is nominally 5v, 20mA, but resistor A in the diagram is initially using a 120 ohm resistor, overdriving the diode during it's brief flashes because it seemed a bit dim otherwise. Shooter is running splatshooter.ino on its arduino uno board and luckily it was simple enough code that i was able to bang it out without any bugs on the first go-through. Currently the shooter flashes once, so there is no team discrimination, so I will have to experiment with adding team discrimination next.

Having tested this initial prototype, the "single shot" effect created by the flash rather than the continuous stream of the previous laser pointer definitely changes the feel of the splat. I know I abandoned animation earlier in the project, but I may want to return to animation give the splat a little more life. Right now it feels a little bit stiff and unresponsive in a way that's hard to describe other than "yes, the laser dot sure makes a static blob shape on the screen." I won't jump right into adding animation first though, since I know I want to add sound anyways. Adding the sound might make the splat feel more "splat-like" so I may not actually need anything further once that's implemented.

Finally, I hadn't initially figured I would prototype a casing for the shooter at this stage, but in it's current state, (see shooter-side and shooter-front) as essentially loose parts held together with tape, I think it's probably neccessary to give some thought to basic ergonomics, even at this stage. Not sure how I'll approach this, either modelling and 3D printing a casing, or just hacking something from recycling bin contents, but it's otherwise such a hassle to have to hold the shooter together while using it, that I think it can't help but influence perception of the affordance.

---
## [mc776/freedoom](https://github.com/mc776/freedoom)@[370032a5a4...](https://github.com/mc776/freedoom/commit/370032a5a4f6f2dfb7d57c7e7831daca88818ee8)
#### Sunday 2023-09-10 06:29:38 by mc776

levels: tweak Map23 exit.

This is a mandatory damage exit that could kill someone even if they do everything else (more or less) right in beating this map. Worst case scenario, they "learn" from their "mistake", "realize" this is a "fake exit", and spend forever trying to find the "real" exit before giving up and learning much later that they'd actually found it before.

- You can pick up at least 30 health right next to the exit teleporter pad.
- The actual teleport landing itself is not a hurtfloor. It is, however, extremely narrow and right in front of an ambushing trilobite. The only way to dodge its fireball is down.
- Made the exit portal huge and fireblu and not a St. Peter's cross (which is often used elsewhere as a purely decorative thing).
- The "EXIT" map lines are now actually faintly glowing on the floor.

As an additional bonus edit: if you exit without finding that creepy area in the facility and have all those guys warp in, those un-warped guys are now all free to roam the entire area as soon as you fall off that high ledge. This means the necromancers can go into that crowd of zombies and raise them, as well as close range to attack you. Enjoy this epic battle - or panicked rush for the exit.

---
## [lunakittyyy/SlingshotIndicatorAlways](https://github.com/lunakittyyy/SlingshotIndicatorAlways)@[297c38dda0...](https://github.com/lunakittyyy/SlingshotIndicatorAlways/commit/297c38dda0c98929f181321beec247f7e2433f03)
#### Sunday 2023-09-10 06:48:48 by Luna

can now compile against unity 2022 assemblies

yeah its literally 1 number
also fuck gitignore I told you to do this shit already

---
## [JuanDluna/Examen1erParcialWeb](https://github.com/JuanDluna/Examen1erParcialWeb)@[199245992c...](https://github.com/JuanDluna/Examen1erParcialWeb/commit/199245992cb8e6e759eb0f65b44e12217d4bbaf3)
#### Sunday 2023-09-10 07:06:42 by JuanDluna

A little changes, this work excelent

fuck you ulises x2

---
## [SThushara/HostelManagementSystem](https://github.com/SThushara/HostelManagementSystem)@[8f0c85bb5f...](https://github.com/SThushara/HostelManagementSystem/commit/8f0c85bb5fbfedcb4bbdf6c8d39b3cc15d7b7f95)
#### Sunday 2023-09-10 07:42:28 by SThushara

Add files via upload

Title: Hostel Database Management System

Description:

The Hostel Database Management System is a comprehensive software solution designed to efficiently manage and streamline the operations of a hostel or dormitory facility. This system is specifically developed to cater to the needs of both hostel administrators and residents, offering a user-friendly interface and a wide range of features to enhance the overall hostel management experience.

Key Features:

1. User Authentication:
   - Secure login credentials for both administrators and residents.
   - Role-based access control to ensure data privacy and security.

2. Resident Management:
   - Easy registration and check-in/check-out processes.
   - Profile management for residents with personal details and contact information.
   - Room allocation and assignment based on preferences and availability.

3. Room and Facility Management:
   - Real-time room availability status and allocation.
   - Management of room types, pricing, and occupancy rules.
   - Tracking and scheduling of maintenance and cleaning tasks.

4. Billing and Payment:
   - Automated billing and invoicing for residents.
   - Support for various payment methods, including cash, credit cards, and online payments.
   - Generation of receipts and financial reports.

5. Attendance and Check-In/Check-Out:
   - Attendance tracking for residents and guests.
   - Seamless check-in and check-out procedures.
   - Notifications for overdue check-outs and room turnovers.

6. Complaint and Request Management:
   - Resident portal for submitting complaints and service requests.
   - Ticketing system to prioritize and address issues efficiently.
   - Notification system to keep residents informed of the status of their requests.

7. Visitor Management:
   - Guest registration and authorization process.
   - Monitoring and logging of visitor activity.
   - Security features to ensure the safety of residents.

8. Reporting and Analytics:
   - Generation of comprehensive reports on occupancy, revenue, and expenses.
   - Data analytics to identify trends and optimize hostel operations.
   - Exporting reports in various formats for further analysis.

9. Communication and Messaging:
   - In-app messaging system for communication between residents and administrators.
   - Broadcast announcements and updates to all residents.
   - Email and SMS notifications for important events and reminders.

10. Security and Backup:
    - Data encryption and secure storage of sensitive information.
    - Regular automated backups to prevent data loss.

11. Mobile Accessibility:
    - Mobile-friendly interface for residents to access their accounts and make requests.
    - Administrators can manage the system remotely via a mobile app.

The Hostel Database Management System is a valuable tool for hostel administrators looking to improve their operations, enhance resident satisfaction, and streamline administrative tasks. It provides a centralized platform for managing all aspects of hostel life, ensuring efficiency, transparency, and a seamless experience for both residents and staff.

---
## [SThushara/QuoraCloneApplication](https://github.com/SThushara/QuoraCloneApplication)@[46bbc8a3c9...](https://github.com/SThushara/QuoraCloneApplication/commit/46bbc8a3c9bba561f3ae065ba7b320143830b17c)
#### Sunday 2023-09-10 07:47:25 by SThushara

Add files via upload

Title: Quora Clone Application

Description:

The Quora Clone Application is a versatile and feature-rich platform designed to replicate the popular question-and-answer community of Quora while offering a unique value proposition. This application allows users to ask questions, share knowledge, engage in discussions, and connect with others who share their interests. It is a comprehensive solution for building a vibrant online community and fostering knowledge-sharing among users.

Key Features:

1. User Registration and Profiles:
   - User-friendly registration process with email, social media, or Google login options.
   - User profiles with customizable avatars, biographies, and expertise tags.
   - Reputation scoring based on user activity and contributions.

2. Question and Answer Posting:
   - Intuitive interface for asking and answering questions.
   - Support for rich text formatting, including images and links.
   - Option to follow specific topics and receive notifications about related questions.

3. Voting and Ranking System:
   - Upvoting and downvoting of answers to determine their visibility.
   - Sorting answers by popularity or recency.
   - A reputation-based system to recognize knowledgeable users.

4. Topic Categorization:
   - A well-organized taxonomy of topics and categories.
   - User-generated topics and subtopics.
   - Tagging questions with relevant keywords for easy search.

5. Notifications and Feeds:
   - Personalized activity feeds showing questions, answers, and updates from followed topics and users.
   - Push notifications for new responses and mentions.
   - Email digests for users to stay updated on their favorite topics.

6. Messaging and Engagement:
   - Private messaging between users for discussions and collaboration.
   - Commenting on questions and answers.
   - Mentioning other users to draw their attention to specific content.

7. Content Moderation and Reporting:
   - Flagging and reporting of inappropriate content.
   - Moderation tools for administrators to ensure a safe and respectful environment.
   - Machine learning algorithms to assist in content moderation.

8. Analytics and Insights:
   - User engagement analytics to track views, upvotes, and shares.
   - Insights into popular topics and trending questions.
   - User behavior analytics for personalized content recommendations.

9. Mobile Accessibility:
   - Native mobile apps for Android and iOS devices.
   - Responsive web design for mobile web users.
   - Seamless cross-platform experience.

10. Monetization Options:
    - Advertisement placements for generating revenue.
    - Subscription plans for premium features.
    - Sponsored content and partnerships with businesses.

11. Community Guidelines and Help Center:
    - Clear guidelines for user behavior and content policies.
    - Comprehensive help center and FAQ section.
    - User reporting system for enforcing community standards.

The Quora Clone Application empowers users to seek knowledge, share expertise, and build connections within a vibrant online community. Whether users are looking for answers to specific questions, sharing their insights, or engaging in meaningful discussions, this platform offers a user-friendly and feature-rich experience that encourages knowledge-sharing and fosters a sense of belonging within the community.

---
## [adityaec2024/MyPortfolio](https://github.com/adityaec2024/MyPortfolio)@[d99b55a6f4...](https://github.com/adityaec2024/MyPortfolio/commit/d99b55a6f48a6791b8964b01a3bf256fe0012a8d)
#### Sunday 2023-09-10 08:20:22 by ADITYA KUMAR GUPTA

Add files via upload

Welcome to the future of portfolio websites on GitHub! Our Interactive Portfolio Website is designed to take your online portfolio to the next level, providing an engaging and dynamic experience for visitors. Say goodbye to static, outdated portfolio pages, and embrace the power of interactivity to showcase your work like never before.

Key Features:

1. **Responsive Design**: Our portfolio website is responsive, ensuring a seamless experience across all devices, from desktops to smartphones and tablets.

2. **Interactive Project Showcase**: Your projects come to life with interactive elements. Visitors can click, swipe, and explore your work, truly immersing themselves in your creative process.

3. **Customizable Themes**: Choose from a wide range of professionally designed themes to match your style and personality. You can also customize colors, fonts, and layouts to make it uniquely yours.

4. **Dynamic Resume**: Your resume is no longer just a static document. It's an integral part of your portfolio, allowing visitors to learn about your skills, experiences, and achievements while navigating your site.

5. **Media Integration**: Easily embed images, videos, and interactive media to provide in-depth insights into your projects. Showcase every angle of your work.

6. **Contact and Social Links**: Make it easy for potential collaborators, clients, or employers to get in touch. Include links to your social profiles and a contact form for direct communication.

7. **Blog Integration**: Share your insights, thoughts, and experiences through an integrated blog section. This feature helps you establish your expertise and keeps your audience engaged.

8. **GitHub Integration**: Since it's hosted on GitHub, your portfolio website can be easily updated by pushing changes to your GitHub repository, making maintenance a breeze.

9. **Analytics**: Gain valuable insights into your portfolio's performance. Track visitor engagement, popular projects, and user behavior to refine your content over time.

10. **SEO Optimization**: We've implemented best practices to ensure your portfolio ranks well in search engines, making it easier for potential clients or employers to discover your work.

11. **Security**: Rest easy knowing that GitHub provides robust security features, protecting your portfolio and data from potential threats.

12. **Community and Collaboration**: GitHub fosters a collaborative environment. Connect with other developers, designers, and creators to exchange ideas and improve your portfolio.

13. **Documentation and Support**: Access detailed documentation and support resources to help you set up and maintain your interactive portfolio website hassle-free.

---
## [joaomacedx/alugaCar](https://github.com/joaomacedx/alugaCar)@[361b9178d9...](https://github.com/joaomacedx/alugaCar/commit/361b9178d9b3aeb719a6b8d7bd76d16281207c54)
#### Sunday 2023-09-10 09:35:02 by João Gabriel dos Reis Hermida Macêdo

✨ feat | Implement option for user to CUD an avatar CREATE, UPDATE, DELETE

**Is your feature request related to a problem? Please describe.**
The issue we are facing is that currently, we do not offer users the ability to Create (C), Update (U), or Delete (D) their profile avatars. This limits user flexibility in customizing their presence on our system and can be a drawback for our platform, especially in terms of user experience and engagement.

**Describe the solution you'd like**
We would like to implement a feature that allows users to perform Create (CREATE), Update (UPDATE), and Delete (DELETE) operations on their profile avatars. To achieve this, we plan to add an avatar management section on the user profile page, where they can upload new images to create or update their avatars. Additionally, they should have the option to delete their existing avatar if they wish to revert to the default avatar or remove their profile picture entirely.

**Describe alternatives you've considered**
We have considered some alternatives to address this issue. One of them would be to allow users to link their profiles to third-party services such as Gravatar or social networks to automatically import avatars. However, this approach may not be suitable for users who want to maintain their privacy and do not wish to link their profile to external services. Therefore, we have opted to implement an internal avatar management system for greater user control and flexibility.

**Additional context**
This functionality will not only enhance the user experience, making our system more appealing and customizable, but it can also have positive implications for user engagement, as customization is an important factor in retaining users on our platform. Additionally, it is important to ensure that the system is designed securely to protect the integrity of profile images and prevent abuse. Therefore, security measures such as file validation and size restrictions should be implemented as part of this feature.

---
## [StrangeWeirdKitten/Bubberstation](https://github.com/StrangeWeirdKitten/Bubberstation)@[43dfda3f4a...](https://github.com/StrangeWeirdKitten/Bubberstation/commit/43dfda3f4a9fc995792d92f45b2eeb1c48c9d078)
#### Sunday 2023-09-10 09:46:07 by StrangeWeirdKitten

God does not exist (prisoners will now get shot by turrets)

Do you think god only stays in heaven because he too fears what he's created? Anyway, this is fixing a bad idea.

---
## [space-wizards/docs](https://github.com/space-wizards/docs)@[1c598febed...](https://github.com/space-wizards/docs/commit/1c598febed6fb4e54d4f2a2904281b01d4ee0315)
#### Sunday 2023-09-10 09:50:01 by Kara

oh my god nevermind its rust compile times

we are caching this shit gentlemen

---
## [AyaShibbi/CODSOFT_WebDevelopment](https://github.com/AyaShibbi/CODSOFT_WebDevelopment)@[8409a7b1f8...](https://github.com/AyaShibbi/CODSOFT_WebDevelopment/commit/8409a7b1f8bd1e167648e8821315698dd9bae8a0)
#### Sunday 2023-09-10 10:05:25 by AyaShibbi

Add files via upload

Welcome to my portfolio—a dynamic showcase of my journey and expertise in the world of web development! This portfolio is thoughtfully divided into distinct sections to provide you with a comprehensive glimpse of my skills and projects. From the inviting header that introduces you to my world, to the About section with a personal touch, you'll find an array of engaging content. The Skills section highlights my technical proficiency, while the Projects Gallery offers a visual journey through my work. You can even view my resume from the Resume section. To get in touch, head over to the Contact section, where you'll find my email address, LinkedIn account, and Github account. What's more, this portfolio is fully responsive, ensuring a seamless experience across various devices. It's a testament to the power of HTML, CSS, and Bootstrap, demonstrating how these tools can bring creativity and functionality to life in the digital realm. Explore and enjoy!

---
## [Dimasw99/Citadel-Station-13-RP](https://github.com/Dimasw99/Citadel-Station-13-RP)@[8117b28946...](https://github.com/Dimasw99/Citadel-Station-13-RP/commit/8117b28946d2e07f902e8800245c34d008336ccc)
#### Sunday 2023-09-10 10:23:43 by nevimer

makes AI experience not fullbright and fixes AI runtiming because they receive a mirror implant (#5179)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

![dreamseeker_sJwmVJw0Yp](https://user-images.githubusercontent.com/77420409/224618392-c9d94b76-05fa-456f-945c-784da7b962a3.png)

![dreamseeker_T7pXJJvDgH](https://user-images.githubusercontent.com/77420409/224618408-838a5156-91df-479f-ac48-4042692e887e.png)



## Why It's Good For The Game

Bug
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
fix: made AI's not see fullbright
balance: silicons don't become a traitor anymore on HUD UPDATES WHY
code: changes the call structure of cyborgs and moves life code down to
silicon level in some places, to make AI code work better.
fix: only human types are effected by mirror implants
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: silicons <2003111+silicons@users.noreply.github.com>
Co-authored-by: Lohikar <lohikar@protonmail.com>

---
## [stormasm/nushell](https://github.com/stormasm/nushell)@[fed4233db4...](https://github.com/stormasm/nushell/commit/fed4233db4d81de00068ffa7cf1c0d09506bc150)
#### Sunday 2023-09-10 10:24:21 by David Matos

use uutils/coreutils cp command in place of nushell's cp command (#10097)

<!--
if this PR closes one or more issues, you can automatically link the PR
with
them by using one of the [*linking
keywords*](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword),
e.g.
- this PR should close #xxxx
- fixes #xxxx

you can also mention related issues, PRs or discussions!
-->

# Description
Hi. Basically, this is a continuation of the work that @fdncred started.
Given some nice discussions on #9463 , and [merged uutils
PR](https://github.com/uutils/coreutils/pull/5152) from @tertsdiepraam
we have decided to give the `cp` command the `crawl` stage as it was
named.

> [!NOTE] 
Given that the `uutils` crate has not made the release for the merged
PR, just make sure you checkout latest and put it in the required place
to make this PR work.

The aim of this PR is for is to see how to move forward using `uutils`
crate. In order to getting this started, I have made the current
`nushell cp tests` pass along with some extra ones I copied over from
the `uutils` repo.

With all of that being said, things that would be nice to decide, and
keep working on:

Crawl:
- Handling of certain `named` flags, with their long and short
forms(e.g. --update, --reflink, --preserve, etc), and using default
values. Maybe `-u` can already have a `default_missing_value`.
- Should we maybe just support one single option `switch` flags (see
`--backup` in code) as a contrast to the other named args.
- Complete test coverage from `uutils`. They had > 100 tests, and I
could only port like 12 as they are a bit time consuming given they
cannot be straight up copy pasted. Maybe we do not need all >100, but
maybe the more relevant to what we want.
- Refactor this code

Walk:
- Non fatal errors on `copy` from `utils`. Currently it just sends it to
stdout but errors have no span
- Better integration 

An added possibility is the addition of `SyntaxShape::OneOf()` for
`Named` arguments which was briefly mentioned in the discord server, but
that is still to be decided. This could greatly improve some of the
integration. This would enable something like `cp --preserve [all
timestamp]` or `cp --preserve all` to both work.

I did not want to keep holding on this, and wait till I was happy with
the code because I think its nice if everyone can start up and suggest
refactors, but the main important part now was getting it out the door,
as if I take my sweet time this will take way longer :stuck_out_tongue:

<!--
Thank you for improving Nushell. Please, check our [contributing
guide](../CONTRIBUTING.md) and talk to the core team before making major
changes.

Description of your pull request goes here. **Provide examples and/or
screenshots** if your changes affect the user experience.
-->

# User-Facing Changes
<!-- List of all changes that impact the user experience here. This
helps us keep track of breaking changes. -->

# Tests + Formatting

Make sure you've run and fixed any issues with these commands:

- [X] cargo fmt --all -- --check` to check standard code formatting
(`cargo fmt --all` applies these changes)
- [X] cargo clippy --workspace -- -D warnings -D clippy::unwrap_used` to
check that you're using the standard code style
- [X] cargo test --workspace` to check that all tests pass
- [X] cargo run -- -c "use std testing; testing run-tests --path
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

---------

Co-authored-by: Darren Schroeder <343840+fdncred@users.noreply.github.com>

---
## [AyaShibbi/CODSOFT_WebDevelopment](https://github.com/AyaShibbi/CODSOFT_WebDevelopment)@[0180d00948...](https://github.com/AyaShibbi/CODSOFT_WebDevelopment/commit/0180d0094808cbeabb513f4d14a1c52745760d58)
#### Sunday 2023-09-10 10:26:35 by AyaShibbi

Add files via upload

Welcome to my portfolio—a dynamic showcase of my journey and expertise in the world of web development! This portfolio is thoughtfully divided into distinct sections to provide you with a comprehensive glimpse of my skills and projects. From the inviting header that introduces you to my world, to the About section with a personal touch, you'll find an array of engaging content. The Skills section highlights my technical proficiency, while the Projects Gallery offers a visual journey through my work. You can even view my resume from the Resume section. To get in touch, head over to the Contact section, where you'll find my email address, LinkedIn account, and GitHub account. What's more, this portfolio is fully responsive, ensuring a seamless experience across various devices. It's a testament to the power of HTML, CSS, and Bootstrap, demonstrating how these tools can bring creativity and functionality to life in the digital realm. Explore and enjoy!

---
## [du-top/sojourn-station](https://github.com/du-top/sojourn-station)@[1e51e36c62...](https://github.com/du-top/sojourn-station/commit/1e51e36c6224c5e0e7f3e50d40ea3d950ecf6286)
#### Sunday 2023-09-10 10:33:47 by CDB

Drip or Drown; Premier style update. And some other clothing related stuff. (#4757)

* Buncha stuffff

First and foremost, it's been like four years - No one has come with a better set of equipment for the Premier in terms of aesthetics and quality.

Replaces much of the Premiers old/mismatched green shit with newer eris captain sprites, if we want to re-color this a bit that's fine but either way we /desperately/ need to replace these ancient sprites.

Premier additionally now actually starts with their coat, and gets a pair of dress shoes instead of the old scuffed brown shoes.

Mind, the original hat/coat/uniform are still available as alternatives if for SOME reason you want to dress up like a christmas tree. I did not add an alt for the space armor/helmet due to them A. not matching and B. being old sprites. I guess if someone REALLY wants I'll port the /tg/ carapace armor/helmets more up to date sprites as an alt.

Ports the funny cyberpunk jacket from eris(in the loadout.)

ports the eris preacher robes icons, but doesn't code them in quite yet. I couldn't be fucked, there's SO many.

Actually adds the formal IH uniform in as well as doing some tweaks to the icon so that WO + spec can also get a formal uniform with their normal rank pips

ports the eris syndie berets.

As always, a big thanks to the talented spriters over at Eris

* new stuff. Also fixes linters lol oops

Adds to the greyson loot pool an armored void using sprites from Près de l'oiseau#2625 over on the Eris discord.

Replaces some more,  old sprites. Miner suit is replaced as pictured as well as the industrial RIG - sprites by Près once more.

* Update station.dm

* Fixes spawning of the greyson combat void helmet

* puts credits in the code instead of on the PR

* minor stuff.,

Slighjtly fixes syndie beret- the north facing sprites were 1 pixel too far down.

WO helmet is no longer missing its verb to turn the light on. Good work there, Rebel - how did no one notice this till now?

* actually fixes it. ugh.

* BUNCHA new church stuff

Primes hat now has 9 alts

Primes coat now has 5

credit to Près de l'oiseau#2625 once more for the fantastic sprites.

---
## [axelzonvolt/lizardsmashingkeyboard](https://github.com/axelzonvolt/lizardsmashingkeyboard)@[b22529fc74...](https://github.com/axelzonvolt/lizardsmashingkeyboard/commit/b22529fc74e5af32967ac91679cbce3e7e06c4ca)
#### Sunday 2023-09-10 11:20:54 by zevo

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
## [dead10ck/nushell](https://github.com/dead10ck/nushell)@[a9216deaa4...](https://github.com/dead10ck/nushell/commit/a9216deaa40d7c5c184bdb3aa1520b6b67c20bf8)
#### Sunday 2023-09-10 12:00:40 by Darren Schroeder

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
## [shiftyp/ts-turbo](https://github.com/shiftyp/ts-turbo)@[6cea7428c2...](https://github.com/shiftyp/ts-turbo/commit/6cea7428c2d29ed0c7d765d9355645218b7cef37)
#### Sunday 2023-09-10 13:14:25 by Sean Doyle

Extract `FrameVisit` to drive `FrameController`

The problem
---

Programmatically driving a `<turbo-frame>` element when its `[src]`
attribute changes is a suitable end-user experience in consumer
applications. It's a fitting black-box interface for the outside world:
change the value of the attribute and let Turbo handle the rest.

However, internally, it's a lossy abstraction.

For example, when the `FrameRedirector` class listens for page-wide
`click` and `submit` events, it determines if their targets are meant to
drive a `<turbo-frame>` element by:

1. finding an element that matches a clicked `<a>` element's `[data-turbo-frame]` attribute
2. finding an element that matches a submitted `<form>` element's `[data-turbo-frame]` attribute
3. finding an element that matches a submitted `<form>` element's
   _submitter's_ `[data-turbo-frame]` attribute
4. finding the closest `<turbo-frame>` ancestor to the `<a>` or `<form>`

Once it finds the matching frame element, it disposes of all that
additional context and navigates the `<turbo-frame>` by updating its
`[src]` attribute. This makes it impossible to control various aspects
of the frame navigation (like its "rendering" explored in
[hotwired/turbo#146][]) outside of its destination URL.

Similarly, since a `<form>` and submitter pairing have an impact on
which `<turbo-frame>` is navigated, the `FrameController` implementation
passes around a `HTMLFormElement` and `HTMLSubmitter?` data clump and
constantly re-fetches a matching `<turbo-frame>` instance.

Outside of frames, page-wide navigation is driven by a `Visit` instance
that manages the HTTP life cycle and delegates along the way to a
`VisitDelegate`. It also pairs calls to visit with a `VisitOption`
object to capture additional context.

The proposal
---

This commit introduces the `FrameVisit` class. It serves as an
encapsulation of the `FetchRequest` and `FormSubmission` lifecycle
events involved in navigating a frame.

It's implementation draws inspiration from the `Visit`, `VisitDelegate`,
and `VisitOptions` pairing. Since the `FrameVisit` knows how to unify
both `FetchRequest` and `FormSubmission` hooks, the resulting callbacks
fired from within the `FrameController` are flat and consistent.

Extra benefits
---

The biggest benefit is the introduction of a DRY abstraction to
manage the behind the scenes HTTP calls necessary to drive a
`<turbo-frame>`.

With the introduction of the `FrameVisit` concept, we can also declare a
`visit()` and `submit()` method for `FrameElementDelegate`
implementations in the place of other implementation-specific methods
like `loadResponse()` and `formSubmissionIntercepted()`.

In addition, these changes have the potential to close
[hotwired/turbo#326][], since we can consistently invoke
`loadResponse()` across `<a>`-click-initiated and
`<form>`-submission-initiated visits. To ensure that's the case, this
commit adds test coverage for navigating a `<turbo-frame>` by making a
`GET` request to an endpoint that responds with a `500` status.

[hotwired/turbo#146]: https://github.com/hotwired/turbo/pull/146
[hotwired/turbo#326]: https://github.com/hotwired/turbo/issues/326

---
## [nuumio/lr-mame](https://github.com/nuumio/lr-mame)@[dbb0909cba...](https://github.com/nuumio/lr-mame/commit/dbb0909cbab3f2094088a42687894e0e6053986b)
#### Sunday 2023-09-10 13:29:29 by wilbertpol

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
## [AnywayFarus/Skyrat-tg](https://github.com/AnywayFarus/Skyrat-tg)@[f26e134c80...](https://github.com/AnywayFarus/Skyrat-tg/commit/f26e134c80678ea78430c84ed3178a1a7b749c80)
#### Sunday 2023-09-10 13:37:10 by SkyratBot

[MIRROR] Fixes vents having "infinite" pressure caps. [MDB IGNORE] (#23356)

* Fixes vents having "infinite" pressure caps. (#77686)

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

* Fixes vents having "infinite" pressure caps.

---------

Co-authored-by: GuillaumePrata <55374212+GuillaumePrata@users.noreply.github.com>

---
## [JarelEze1/3D-Printer-Kit-Sales-Website](https://github.com/JarelEze1/3D-Printer-Kit-Sales-Website)@[d8a4379fa2...](https://github.com/JarelEze1/3D-Printer-Kit-Sales-Website/commit/d8a4379fa2c9b607b94b565932dcecae42551217)
#### Sunday 2023-09-10 13:57:51 by Ezenwa .j. Agbanusi

Update README.md

3D Printer Kit Sales Website

🌟 Explore the world of 3D printing with our high-quality 3D printer kits! This responsive website allows you to effortlessly browse, select, and order the perfect kit for your creative journey. Experience the magic of JavaScript-driven interactivity for a smooth and secure shopping experience. Join our 3D printing community today!

🚀 Key Features:

Detailed product information
Seamless order placement
Secure payment options (PayPal & credit card)
Responsive design for all devices

🛠️ JavaScript Magic: Discover how we've leveraged JavaScript to enhance the user experience, from dynamic form fields to stylish modal pop-ups.

🙌 Contributions Welcome: Help me improve this project and contribute to the 3D printing community.

📝 License: This project is licensed under the MIT License.

Join me in the exciting world of 3D printing! Start creating and exploring today. 💡

---
## [Sandra-Cai/ABFaucet](https://github.com/Sandra-Cai/ABFaucet)@[0391771ea2...](https://github.com/Sandra-Cai/ABFaucet/commit/0391771ea29b294b8cdb3066ee9671615e4b1ea1)
#### Sunday 2023-09-10 14:34:09 by Sandra-Cai

Update README.md

Inspiration
Nowadays, AI and blockchain are emerging in the tech industry. But they are rarely put into use in our daily lives. ABFaucet wants to utilize these solutions to help people have better sentiments hence a happier life.

What it does
It helps users to have a better dating experience using AI and Blockchain technologies.

How we built it
We first use Twilio for KYC in order to have users have an account. In the meantime, we have users to have tokens registered in order for us to proceed with the blockchain DiD verification to achieve transparency and decentralization. In order to achieve the transparency part, we have come up with a matching algorithm using ML as our AI solution where it is statistical-based and distributive-based and zero-knowledge proof as our blockchain solution.

Challenges we ran into
We ran into challenges like not being able to utilize some existing APIs for us to come up with results so we ended up building our own AI with unique features of being able to date with our chatbox if users do not feel prepared for the real-time dating.

Accomplishments that we're proud of
We created our own matching algorithm.

Firstly, we will have users fill out the features they want in the ideal partners; Secondly, we will based on the results recommend a list of profiles; Then, we will based on the "like" and "dislike" results run a logistic regression model to learn users' behavior; Then, we will have better classification which is personalized for the user and it is constantly changing and iterating just for the user; In addition, we also offer an option for users to "date" with a robot if they are not ready for the real dating matching mechanism to happen.

What we learned
Building this app out is so much fun and we enjoyed it!

What's next for ABFaucet
We hope to build the actual application out on iOS and we wish to get funding to keep it going as we have support from PhD students who are researching blockchain topics and making sure the model is accurate.

Built With
ai
javascript
leo
machine-learning
python
react
smart-contract
solidity
Try it out
 GitHub Repo

---
## [Kem-ma/Kem-ma](https://github.com/Kem-ma/Kem-ma)@[44c8df93d4...](https://github.com/Kem-ma/Kem-ma/commit/44c8df93d4b3ac87c0a258018ba3698f5f57f742)
#### Sunday 2023-09-10 15:02:31 by Keukang C

Add files via upload

For the 4th task, I was provided with a medical student data set for me to clean and create a pivot table.

Question 1 required me to display the average values of age, BMI, temperature, heart rate, blood pressure, cholesterol for male and female.

---
## [sammyfilly/react](https://github.com/sammyfilly/react)@[ac1a16c67e...](https://github.com/sammyfilly/react/commit/ac1a16c67e268fcb2c52e91717cbc918c7c24446)
#### Sunday 2023-09-10 15:54:44 by Sebastian Markbåge

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
## [MarkusTheOrt/bevy](https://github.com/MarkusTheOrt/bevy)@[44f677a38a...](https://github.com/MarkusTheOrt/bevy/commit/44f677a38a6c99b8dcf79426d5b615a1266dde2d)
#### Sunday 2023-09-10 16:15:55 by Sélène Amanita

Improve documentation relating to `Frustum` and `HalfSpace` (#9136)

# Objective

This PR's first aim is to fix a mistake in `HalfSpace`'s documentation.

When defining a `Frustum` myself in bevy_basic_portals, I realised that
the "distance" of the `HalfSpace` is not, as the current doc defines,
the "distance from the origin along the normal", but actually the
opposite of that.

See the example I gave in this PR.

This means one of two things:
1. The documentation about `HalfSpace` is wrong (it is either way
because of the `n.p + d > 0` formula given later anyway, which is how it
behaves, but in that formula `d` is indeed the opposite of the "distance
from the origin along the normal", otherwise it should be `n.p > d`)
2. The distance is supposed to be the "distance from the origin along
the normal" but when used in a Frustum it's used as the opposite, and it
is a mistake
3. Same as 2, but it is somehow intended

Since I think `HalfSpace` is only used for `Frustum`, and it's easier to
fix documentation than code, I assumed for this PR we're in case number
1. If we're in case number 3, the documentation of `Frustum` needs to
change, and in case number 2, the code needs to be fixed.

While I was at it, I also :
- Tried to improve the documentation for `Frustum`, `Aabb`, and
`VisibilitySystems`, among others, since they're all related to
`Frustum`.
- Fixed documentation about frustum culling not applying to 2d objects,
which is not true since https://github.com/bevyengine/bevy/pull/7885

## Remarks and questions

- What about a `HalfSpace` with an infinite distance, is it allowed and
does it represents the whole space? If so it should probably be
mentioned.
- I referenced the `update_frusta` system in
`bevy_render::view::visibility` directly instead of referencing its
system set, should I reference the system set instead? It's a bit
annoying since it's in 3 sets.
- `visibility_propagate` is not public for some reason, I think it
probably should be, but for now I only documented its system set, should
I make it public? I don't think that would count as a breaking change?
- Why is `Aabb` inserted by a system, with `NoFrustumCulling` as an
opt-out, instead of having it inserted by default in `PbrBundle` for
example and then the system calculating it when it's added? Is it
because there is still no way to have an optional component inside a
bundle?

---------

Co-authored-by: SpecificProtagonist <vincentjunge@posteo.net>
Co-authored-by: Alice Cecile <alice.i.cecile@gmail.com>

---
## [0livare/zach-blog-v5](https://github.com/0livare/zach-blog-v5)@[7430ee677d...](https://github.com/0livare/zach-blog-v5/commit/7430ee677d89a42df68fb4c6dd4bf421849335fc)
#### Sunday 2023-09-10 17:07:52 by Zach Olivare

Get code blocks looking decent

This was frustrating.

Astro highlights code blocks by default, but doesn't pass the raw code
strings to the markdown components when you override them. So to get the
code and the language you have to first disable the default syntax
highlighting with by setting markdown.syntaxHighlight=false in the astro
config, and then burrow down into shit like props.children.props.value
when overriding the markdown pre or code component.

But even after all that it seemed like every time the pres and codes were
all rendering twice. The first time I could access that information (source
code and language) and the second time everything was undefined. I don't know
what that's about.

So in the end I gave up using react-code-blocks like I was before and just
found a way to style the default implementation.

Note: In order for any given blog post to use the overridden markdown components,
they have to be exported from each mdx file annoyingly.

  import {mdxComponents} from '~/components'
  export const components = mdxComponents

---
## [firstdarkdev/CraterLib](https://github.com/firstdarkdev/CraterLib)@[3e7598e679...](https://github.com/firstdarkdev/CraterLib/commit/3e7598e679b0d801c40a42063e6fa5fd00d13be6)
#### Sunday 2023-09-10 17:12:20 by HypherionMC

[CHORE] Fix Maven publishing for Fabric.... FUCK YOU LOOM

---
## [torvalds/linux](https://github.com/torvalds/linux)@[1548b060d6...](https://github.com/torvalds/linux/commit/1548b060d6f32a00a2f7e2c11328205fb66fc4fa)
#### Sunday 2023-09-10 19:05:26 by Linus Torvalds

Merge tag 'topic/drm-ci-2023-08-31-1' of git://anongit.freedesktop.org/drm/drm

Pull drm ci scripts from Dave Airlie:
 "This is a bunch of ci integration for the freedesktop gitlab instance
  where we currently do upstream userspace testing on diverse sets of
  GPU hardware. From my perspective I think it's an experiment worth
  going with and seeing how the benefits/noise playout keeping these
  files useful.

  Ideally I'd like to get this so we can do pre-merge testing on PRs
  eventually.

  Below is some info from danvet on why we've ended up making the
  decision and how we can roll it back if we decide it was a bad plan.

  Why in upstream?

   - like documentation, testcases, tools CI integration is one of these
     things where you can waste endless amounts of time if you
     accidentally have a version that doesn't match your source code

   - but also like the above, there's a balance, this is the initial cut
     of what we think makes sense to keep in sync vs out-of-tree,
     probably needs adjustment

   - gitlab supports out-of-repo gitlab integration and that's what's
     been used for the kernel in drm, but it results in per-driver
     fragmentation and lots of duplicated effort. the simple act of
     smashing an arbitrary winner into a topic branch already started
     surfacing patches on dri-devel and sparking good cross driver team
     discussions

  Why gitlab?

   - it's not any more shit than any of the other CI

   - drm userspace uses it extensively for everything in userspace, we
     have a lot of people and experience with this, including
     integration of hw testing labs

   - media userspace like gstreamer is also on gitlab.fd.o, and there's
     discussion to extend this to the media subsystem in some fashion

  Can this be shared?

   - there's definitely a pile of code that could move to scripts/ if
     other subsystem adopt ci integration in upstream kernel git. other
     bits are more drm/gpu specific like the igt-gpu-tests/tools
     integration

   - docker images can be run locally or in other CI runners

  Will we regret this?

   - it's all in one directory, intentionally, for easy deletion

   - probably 1-2 years in upstream to see whether this is worth it or a
     Big Mistake. that's roughly what it took to _really_ roll out solid
     CI in the bigger userspace projects we have on gitlab.fd.o like
     mesa3d"

* tag 'topic/drm-ci-2023-08-31-1' of git://anongit.freedesktop.org/drm/drm:
  drm: ci: docs: fix build warning - add missing escape
  drm: Add initial ci/ subdirectory

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[5e9e45f1b6...](https://github.com/tgstation/tgstation/commit/5e9e45f1b6c60a2d00a3823ad619f8292720f671)
#### Sunday 2023-09-10 19:09:03 by Sealed101

Polymorph belt blacklists several biotypes instead of allowing only organics (#78229)

## About The Pull Request

Title; this makes the belt able to morph into _more_ mobs, but _less
problematic/abusable_ mobs hopefully. It still only functions on
basic/simple_animals, however.

~~Headslugs get a `MOB_UNDEAD` bioflag to prevent morphing into them
completely. Though catching a sentient ling slug and morphing everyone
into it is funny, it's only funny the first 5 times someone does it.
(disclaimer: this is an approximation, i did not actually see a
polymorph belt in-game because i currently play miner and like 10 games
a week tops)
Arguably, this isn't ideal, but it's the closest we get unless we rename
`MOB_EPIC` or something into `MOB_SPECIAL` and let that one be the go-to
bioflag for mobs we don't want **fun** things happen to.~~
`MOB_EPIC` is now `MOB_SPECIAL`. Headslugs get that.
I think the alternative methow could use whatever the gold cores use to
determine what to spawn but that would shift the mobs available for the
belt even more and I can't be assed to figure out how _much_ of a shift
that would be. Dragons or slimes or lavaland mobs would be out, for
example. Don't really vibe with that.

Fixes headslug's description bit that discerns a sentient slug from an
AI one showing up on a dead slug. It can't move while it's dead, no
matter its mind/AI.

Also adds simple dmdoc comments to the defines to help discern a few of
them more easily. Non-quip text suggestions welcome.

## Why It's Good For The Game
- Resolves #77756
- Resolves #78227

More mobs available for the funny belt but less _fun_ mobs should allow
for more stable use of the damn thing. Arguably, some of the mobs that
have been found to be incompatible with the belt are simply lacking a
`MOB_ORGANIC` flag, some of them with no apparent reason. However,
blacklisting potentially problematic biotypes should be easier to design
the unwanted mobs around.
Also consistency, less all-ling stations, code clarity. Whatever.

## Changelog

:cl:
balance: polymorph belt now blacklists mobs that are undead, humanoid,
robotic or spiritual (in nature, not religiously), as well as megafauna
balance: however, this means that it works with more mobs that it should
logically work with, like slimes/bugs/lightgeists etc
fix: fixed headslug shenanigans with the polymorph belt hopefully for
good this time
fix: fixed headslug description mentioning its movement despite the slug
being dead
/:cl:

---
## [Alchav/Archipelago](https://github.com/Alchav/Archipelago)@[6d13dc4944...](https://github.com/Alchav/Archipelago/commit/6d13dc494455bef97e0f1afc8928853f71d5b5ad)
#### Sunday 2023-09-10 19:19:47 by el-u

lufia2ac: new features, bug fixes, and more (#1549)

### New features

- ***Architect mode***
  Usually the cave is randomized by the game, meaning that each attempt will produce a different dungeon. However, with this new feature the player can, between runs, opt into keeping the same cave. If activated, they will then encounter the same floor layouts, same enemy spawns, and same red chest contents as on their previous attempt.   

- ***Custom item pool***
  Previously, the multiworld item pool consisted entirely of random blue chest items because, well, the permanent checks are blue chests and that's what one would normally get from these. While blue chest items often greatly increase your odds against regular enemies, being able to defeat the Master can be contingent on having an appropriate equipment setup of red chest items (such as Dekar blade) or even enemy drops (such as Hidora rock), most of which cannot normally be obtained from blue chests.
  With the custom item pool option, players now have the freedom to place any cave item into the multiworld itempool for their world.

- ***Enemy floor number, enemy sprite, and enemy movement pattern randomization***
  Experienced players can deduce a lot of information about the opposition they will be facing, for example: Given the current floor number, one can know in advance which of the enemy types will have a chance to spawn on that floor. And when seeing a particular enemy sprite, one can already know which enemy types one might have to face in battle if one were to come in contact with it, and also how that enemy group will move through the dungeon.
  Three new randomization options are added for players who want to spice up their game: one can shuffle which enemy types appear on which floor, one can shuffle which sprite is used by which enemy type, and one can shuffle which movement pattern is used by which sprite.

- ***EXP modifier***
  Just a simple multiplier option to allow people to level up faster. (For technical reasons, the maximum amount of EXP that can be awarded for a single enemy is limited to 65535, but even with the maximum allowed modifier of 500% there are only 6 enemy types in the cave that can reach this cap.)


### Balance change

- ***proportionally adjust chest type distribution to accommodate increased blue chest chance***
  One of the main problems that became apparent in the current version has to do with the distribution of chest contents. The game considers 6 categories, namely: consumable (mostly non-restorative), consumable (restorative), blue chest item, spell, gear, and weapon. Since only blue chests count as multiworld locations, we want to have a mechanism to customize the blue chest chance.
  Given how the chest types are detetermined in game, a naive implementation of an increased blue chest chance causes only the consumable chance to be decreased in return. In practice, this has resulted in some players of worlds with a high blue chest chance struggling (more than usual) to keep their party alive because they were always low on comsumables that restore HP and MP.
  The new algorithm tries to avoid this one-sided effect by having an increase in blue chest chance resulting in a decrease of all other types, calculated in such a way that the relative distribution of the other 5 categories stays (approximately) the same.


### Bug fixes

- ***prevent using party member items if character is already in party***
  This should have been changed at the same time that 6eb00621e39c930f5746f5f3c69a6bc19cd0e84a was made, but oh well... 

- ***fix glitched sprite when opening a chest immediately after receiving an item***
  When opening a chest right after receiving a multiworld item (such that there were two item get animations in the exact same iteration of the game main loop), the item from the chest would display an incorrect sprite in the wrong place. Fixed by cleaning up some relevant memory addresses after getting the multiworld item.

- ***fix death link***
  There was a condition in `deathlink_kill_player` that looked kinda smart (it checked the time against `last_death_link`), but actually wasn't smart at all because `deathlink_kill_player` is executed as an async task and the main thread will update `last_death_link` after creating the task, meaning that whether or not the incoming death link would actually be passed to the game seems to have been up to a race condition. Fixed by simply removing that check.


### Other

- ***add Lufia II Ancient Cave (and SMW) to the network diagram***
  These two games were missing from the SNES sector.

- ***implement get_filler_item_name***
  Place a restorative consumable instead of a completely random item. (Now the only known problem with item links in lufia2ac is... that noone has ever tested item links. But this should be an improvement at least. Anyway, now #1172 can come ;)
  And btw., if you think that the implementation of random selection in this method looks weird, that's because it is indeed weird. (It tries to recreate the algorithm that the game itself uses when it generates a replacement item for a chest that would contain a spell that the party already knows.)

- ***store all options in a dataclass***
  This is basically like using #993 (but without actual support from core). It makes the lufia2ac world code much nicer to maintain because one doesn't have to change 5 different places anymore when adding or renaming an option.

- ***remove master_hp.scale***
  I have to admit: `scale` was a mistake. Never have I seen a single option value cause so many user misconceptions. Some people assume it affects enemies other than the Master; some people assume it affects stats other than HP; and many people will just assume it is a magic option that will somehow counterbalance whatever settings combination they are currently trying to shoot themselves in the foot with.
  On top of that, the `scale` mechanism probably doesn't provide a good user experience even when used for its intended purpose (since having reached floor XY in general doesn't mean you will have the power to deplete XY% of the Masters usual HP; especially given that, due to the randomness of loot, you are never guaranteed to be able to defeat the vanilla Master even when you have cleared 100% of the floors).
  The intended target audience of the `master_hp` option are people who want to fight the Master (and know how to fight it), but also want to lessen (to a degree of their choosing) the harsh dependence on the specific equipment setups that are usually required to win this fight even when having done all 99 floors. They can achieve this by setting the `master_hp` option to a numeric value appropriate for the level of challenge they are seeking. Therefore, nothing of value should be lost by removing the special `scale` value from the `master_hp` option, while at the same time a major source of user confusion will be eliminated.

- ***typing***
  This (combined with the switch to the option dataclass) greatly reduces the typing problems in the lufia2ac world. The remaining typing errors mostly fall into 4 categories:
  1. Lambdas with defaults (which seem to be incorrectly reported as an error due to a mypy bug)
  1. Classmethods that return instances (which could probably be improved using PEP 673 "Self" types, but that would require Python 3.11 as the minimum supported version)
  1. Everything that inherits from TextChoice (which is a typing mess in core)
  1. Everything related to asar.py (which does not have proper typing and lies outside of this project)

## How was this tested?

https://discord.com/channels/731205301247803413/1080852357442707476 and others

---
## [mouseandthebillionaire/_lestTenHorizonsCry](https://github.com/mouseandthebillionaire/_lestTenHorizonsCry)@[93f0236a48...](https://github.com/mouseandthebillionaire/_lestTenHorizonsCry/commit/93f0236a486f930bcf75cac30428ed1b8ea8d5b2)
#### Sunday 2023-09-10 19:49:39 by mouseandthebillionaire

docs: Initial Precedent Study

Looking at a lot of things here. The ideation phase is happening in tandem, but that documentation comes later. It is worth nothing, however, that a large design value has been established while thinking about these previous projects. As of now, it is best stated as "creating something with many ambiguous ideal states over one specific ideal state." Mainly this is a pushback on the idea of "oh I get it. Like the music sounds better if you're doing the right thing?" How to make a musical experience in a game where there is no "bad" audio, but rather "many compelling states" of audio?

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[dc6ddd821b...](https://github.com/timothymtorres/tgstation/commit/dc6ddd821b1d9fe4783cf5d05c4ed2aa96f98e89)
#### Sunday 2023-09-10 20:07:08 by Cheshify

North Star Science Rework And More (#77439)

## About The Pull Request
I fixed a few miscellaneous issues and also redid science (mainly
genetics, cytology, and xenobiology)
This is genetics, it's basically the same but moneky have bananas and I
rotated it so they'll be visible from the front desk.

![geneticsnew](https://github.com/tgstation/tgstation/assets/73589390/7c10d75b-2a7a-47b2-a6ca-a30354d713c3)

Holy fuck it's Cytology as a proper area. It now has main hall access
and a public access petting zoo. Now you can show off all your new
creatures (it also has some items cytologists generally want)

![cytonew](https://github.com/tgstation/tgstation/assets/73589390/7d9256c9-b39a-4502-b599-9226a2ca5cd8)

Upstairs is Xenobio, which is now much larger and soulless. Instead of a
normal holding cell there's a prefilled room of oxygen and BZ (the
holding room, why is BZ invisible?)

![xenonew](https://github.com/tgstation/tgstation/assets/73589390/5dc28dba-a051-4858-a9fc-16d51e987c33)

I also gave Ordnance 5 TTVs, same as other maps.
Also the coroner no longer has an unreachable box of bodybags
Also sec now has 2 secways + 2 keys for their usage
## Why It's Good For The Game
I'm forcing xenobiologists to be closer to a hall so they might actually
interact with people, and giving cytologists a reason to do anything
ever because they have a petting zoo to show their creatures off in. Oh
yeah also cytology gets equipment they should just have (a botany tray,
tools to butcher with, a shitty old laser gun to kill experiments gone
wrong)
Genetics is just better because people from the hall can see the
Geneticists working so they can bug them for stuff.

A few of the fixes are very tiny, like moving a few areas by the service
hall and adding a single pipe to the AI SAT
## Changelog
:cl:
qol: North Star's Cytology and Xenobiology are now significantly more
usable.
add: North Star's Genetics has been tweaked.
fix: The North Star's AI SAT has a working vent and it's service hall
has a working lightswitch
/:cl:

---
## [jvanabra/dimensional-integral](https://github.com/jvanabra/dimensional-integral)@[89040e34d0...](https://github.com/jvanabra/dimensional-integral/commit/89040e34d0960c6225e850af28a45c048a9004c2)
#### Sunday 2023-09-10 20:19:33 by Joshua Van Abrahams

The marriage of Sense and Soul

Many of the ideas I present to the GitHib dimensional-integral have been in development for 13 years through the throws of meth addiction and Holosync and a type of Outsider Art and honest hard work through writing repository after repository and literally experiencing heaven and hell, but mostly hell honestly.  The direction of this work is not christian because that is an outside determination, but christ of self exploration of how much can we bring under the umbrella and not self contradict?  This is why I expand christ to interoperate with shiva, and karma, through expression in the soul plane I manifest.

---
## [Ghilker/tgstation](https://github.com/Ghilker/tgstation)@[4b8de7b79f...](https://github.com/Ghilker/tgstation/commit/4b8de7b79f0a343dc587d0d17eb9361ecc7103c1)
#### Sunday 2023-09-10 20:25:06 by san7890

Refactors the `notransform` variable into a trait. (#78146)

## About The Pull Request

Hey there,

There were more than a few times (like in cinematic code) where we might
need to accurately know the source of what's adding this trait (or have
multiple sources for the whole 'we don't want this mob to do shit while
we transform this mob'), so in order to rectify this potential issue,
let's refactor it into a trait.

## Why It's Good For The Game

Some code already declared that there might be issues with this being a
boolean var (with no way of knowing _why_ we don't want this mob to not
transform (or not do anything idk). Let's remove those comments and any
future doubt in those instances with the trait macros. Also, stuff like
`TRAIT_IMMOBILIZED` which does a similar thing in many contexts was
already a trait that was regularly added in conjunction with flipping
the variable, so we're able to flatten all that stuff into
`add_traits()` and `remove_traits()` now. nice

I also cleaned up quite a bit of code as I saw it, let me know if it
should be split out but I guarantee that if I didn't do it- no one will
for the next two years.

## Changelog

:cl:
refactor: If you transform into another mob and notice bugs with
interacting with the game world, please create a bug report as this
framework was recently refactored.
/:cl:

Probably fucked up somewhere, lmk

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [Ghilker/tgstation](https://github.com/Ghilker/tgstation)@[1be0841d98...](https://github.com/Ghilker/tgstation/commit/1be0841d98f215a0e94245c33317232bafa59342)
#### Sunday 2023-09-10 20:25:06 by Time-Green

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
## [russ-money/russ-station](https://github.com/russ-money/russ-station)@[f0dc574c37...](https://github.com/russ-money/russ-station/commit/f0dc574c37c6defc0a9e2d4117d20c3963a11d86)
#### Sunday 2023-09-10 20:42:47 by carlarctg

Added Omen Spontaneous Combustion and light tube and mirror effects (#77175)

## About The Pull Request

Cursed crewmembers can randomly, extremely rarely, spontaneously combust
for no reason.

Cursed crewmembers can get zapped by nearby light tubes.

Cursed crewmembers can freak out when passing by mirrors.

To make up for these, triggering a cursed effect is slightly less than
half as likely now when walking around now.

## Why It's Good For The Game

Cursed is fun as hell, but after a certain point it gets kind of
monotonous - it's airlocks, vending machines, and the rest is too rare
to count. We need more ways to comically get hurt in the game.

You might dislike the 'reduced effects' bit but trust me it is
incredibly frickin' common to have shit happen to you. Add to the
occasional vending machine and airlock crushes the near-constant light
tubes all over the station? Yeah, that needs a toning down else it will
be just a tad too miserable to be funny. Also cause the poor janitor
unneeded stress.

## Changelog

:cl:
add: Cursed crewmembers can randomly, extremely rarely, spontaneously
combust for no reason.
add: Cursed crewmembers can get zapped by nearby light tubes.
add: Cursed crewmembers can freak out when passing by mirrors.
add: To make up for these, triggering a cursed effect is slightly less
than half as likely now when walking around now.
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>
Co-authored-by: Time-Green <7501474+Time-Green@users.noreply.github.com>

---
## [swordcube/Droplet-Game-Framework](https://github.com/swordcube/Droplet-Game-Framework)@[f05ed0cf58...](https://github.com/swordcube/Droplet-Game-Framework/commit/f05ed0cf587d14bc0d632ff0e50d5da7116c1ac3)
#### Sunday 2023-09-10 21:52:26 by swordcube

cameras now have separated bg colors from window (unless they're set to be transparent) because fuck you

also the missing graphic always stays in memory now :3

---
## [DeerJesus/tgstation](https://github.com/DeerJesus/tgstation)@[bae1aef3b4...](https://github.com/DeerJesus/tgstation/commit/bae1aef3b457cb4fbad551a8560319ed993ba397)
#### Sunday 2023-09-10 22:18:07 by san7890

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
## [vimpostor/vim-tpipeline](https://github.com/vimpostor/vim-tpipeline)@[2889cbdbe7...](https://github.com/vimpostor/vim-tpipeline/commit/2889cbdbe756324e1e21716a34b3d36b058f959e)
#### Sunday 2023-09-10 22:37:44 by Magnus Groß

Add workaround for inconsistent statusline eval padding

It seems that neovim applies inconsistent padding when evaluating the
statusline:

- When padding a normal component, e.g. "%5l", then the global fillchars
  option is used
- When padding a grouped component with minwid, e.g. "%2(a%)", then the
  fillchars parameter for nvim_eval_statusline() is used

It is this inconsistent padding that causes our statusline split
heuristic to mistakenly think that a grouped component is the actual
split of the statusline (like "%="), while it is actually not.
This caused some statuslines (in particular heirline, luckily not many
other popular statuslines use grouped components like this) to have very
weird and early right alignment.
This is obviously not the fault of those statuslines, but it turns out
that this bug is not very easy to fix in upstream neovim.
Ideally we would have API in nvim_eval_statusline() that would tell us
the split point directly, then we could avoid these nasty heuristics
altogether.

So instead I came up with a workaround in the meantime. Keep in mind,
this workaround is absolutely horrid, but at least it works. Hopefully
we can resolve this problem properly, but for now I have added a unit
test to make sure that we don't regress this further.

Also fuck whoever masochist came up with 1-based indexes in Lua. It's
causing off-by-one errors literally everywhere, and unfortunately that's
not even the worst part about this horrible language.

Fixes #58

---
## [opussf/Rested](https://github.com/opussf/Rested)@[6a6b81230f...](https://github.com/opussf/Rested/commit/6a6b81230fd2b8a630faf877770927770645b143)
#### Sunday 2023-09-10 22:42:51 by opussf

100107

Fantasy is a necessary ingredient in living, it's a way of looking at life through the wrong end of a telescope, and that enables you to laugh at life's realities.

---

