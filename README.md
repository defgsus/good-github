## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-11-14](docs/good-messages/2023/2023-11-14.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,475,527 were push events containing 3,912,779 commit messages that amount to 325,457,149 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 69 messages:


## [KDr2/pytorch](https://github.com/KDr2/pytorch)@[3afb4e5cf7...](https://github.com/KDr2/pytorch/commit/3afb4e5cf7b0162c532449fb5c9e7c7058a4c803)
#### Tuesday 2023-11-14 00:03:29 by Brian Hirsh

AOTAutograd: handle set_(), detect metadata mutations that cancel out (#111554)

This should be enough to get @voznesenskym 's FSDP branch to plumb `set_()` through AOTAutograd properly and have everything properly no-op out. Main changes are:

(1) graph break on `aten::set_.source_Tensor_storage_offset` (we could support it but it isn't needed, seems safer to graph break)

(2) Functionalization: add a "proper" functionalization kernel for `aten::set_.source_Tensor`. The previous one we had was codegen'd and it was wrong (it would just clone() and call set_(), which does not do the right thing). I also manually mark on the `FunctionalTensorWrapper` when a given tensor has been mutated by a `set_()` call.

(3) AOTAutograd: I added a new field, `InputAliasInfo.mutates_storage_metadata`, so we can distinguish between "regular" metadata mutations, and metadata mutations due to `set_()` calls. This is mainly because at runtime, one requires calling `as_strided_()` to fix up metadata, while the other requires calling `set_()`.

(4) Made AOTAutograd's detection for metadata mutations / set_() mutations smarter and detect no-ops (if the storage and metadata are all the same).

I also killed `was_updated()` and `was_metadata_updated()`, and replaced them with (existing) `has_data_mutation() ` and (new) `has_data_mutation()`, which can more accurately distinguish between data-mutation vs. `set_()` calls vs. metadata-mutation

**This PR is still silently correct in one case though**, which I'd like to discuss more. In particular, this example:
```
def f(x):
    x_view = x.view(-1)
    x.set_(torch.ones(2))
    x_view.mul_(2)
    return
```

If you have an input that experiences both a data-mutation **and** a `x_old.set_(x_new)` call, there are two cases:

(a) the data mutation happened on the storage of `x_new`. This case should be handled automatically: if x_new is a graph intermediate then we will functionalize the mutation. If x_new is a different graph input, then we will perform the usual `copy_()` on that other graph input

(b) the data mutation happened on the storage of `x_old`. This is more of a pain to handle, and doesn't currently work. At runtime, the right thing to do is probably something like:
```

def functionalized_f(x):
    x_view = x.view(-1)
    # set_() desugars into a no-op; later usages of x will use x_output
    x_output = torch.ones(2)
    # functionalize the mutation on x_view
    x_view_updated = x.mul(2)
    x_updated = x_view_updated.view(x.shape)
    # x experienced TWO TYPES of mutations; a data mutation and a metatadata mutation
    # We need to return both updated tensors in our graph
    return x_updated, x_output
def runtime_wrapper(x):
    x_data_mutation_result, x_set_mutation_result = compiled_graph(x)
    # First, perform the data mutation on x's old storage
    x.copy_(x_data_mutation_result)
    # Then, swap out the storage of x with the new storage
    x.set_(x_set_mutation_result)
```

There are two things that make this difficult to do though:

(1) Functionalization: the functionalization rule for `set_()` will fully throw away the old `FunctionalStorageImpl` on the graph input. So if there are any mutations to that `FunctionalStorageImpl` later on in the graph, the current graph input won't know about it. Maybe we can have a given `FunctionalTensorWrapper` remember all previous storages that it had, and track mutations on all of them - although this feels pretty complicated.

(2) AOTAutograd now needs to know that we might have *two* graph outputs that correspond to a single "mutated input", which is annoying.

It's worth pointing out that this issue is probably extremely unlikely for anyone to run into - can we just detect it and error? This feels slightly easier than solving it, although not significantly easier. We would still need `FunctionalTensorWrapper` to keep track of mutations on any of its "previous" storages, so it can report this info back to AOTAutograd so we can raise an error.

Pull Request resolved: https://github.com/pytorch/pytorch/pull/111554
Approved by: https://github.com/ezyang

---
## [AlexMarrinan/RavenGuard](https://github.com/AlexMarrinan/RavenGuard)@[c45a9c48dd...](https://github.com/AlexMarrinan/RavenGuard/commit/c45a9c48dda83a17e81b3065b70d9f56f4d14ecc)
#### Tuesday 2023-11-14 00:24:22 by Woodemen

MagicKnightAttack

I hope this is correct. It took me like 3 hours trying to remember/figure out how to set up this animation correctly so if its wrong or broken for some reason let me know what is is because WOW I am out of my depth lol. Also out of pure fear I checked that this was uploaded to the CORRECT BRANCH as to not decimate the fuckin files.

---
## [Citadel-Station-13/Citadel-Station-13-RP](https://github.com/Citadel-Station-13/Citadel-Station-13-RP)@[33cae266af...](https://github.com/Citadel-Station-13/Citadel-Station-13-RP/commit/33cae266af864b22c509f65ffff3ad7277bbb459)
#### Tuesday 2023-11-14 00:33:09 by Captain277

Subtypes Corporate Crates, Fixes Mapped Biohazard Crate, Renames Advanced Voidsuit (#6126)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

1. *Fixes Bug With Corporate Crates, Subtypes Them.*
2. *Removes Varedited Biohazard Bin and Places Normal Biohazard Bin.*
3. *Changes Advanced Voidsuit Name to Advanced Hardsuit.*

## Why It's Good For The Game

1. _I received reports of one specific corporate crate not rendering
properly when opened. As I inspected it, I realized it would be more
efficient to subtype all corporate crates, so I did that. HOWEVER, this
did not repair the initial bug. For some reason the crate was not
rendering its 'aethersecureopen' state, even though all variables and
code seemed to be working properly. No other crate exhibited this issue.
I discovered that by changing the name of the icon state from
'aethersecureopen' to 'aethersecopen', the state began to enforce and
render properly. I suspected it might be a name length issue, but tests
with other equally long icon states in the crate section disproved this
theory. This may warrant further investigation._
2. _This one avoided detection during my initial sweep through. Can't
remember who just went in and tried to varedit bins to fix biohazards,
but hopefully this is the last one they touched._
3. _This has been driving me crazy for a few days, and yesterday
especially. The Advanced Voidsuit is clearly misnamed, as it is in fact
a Hardsuit. When I tried to order these yesterday I overlooked this
cargo entry twice because I was looking for a hardsuit, not a voidsuit.
This just fixes the name._

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
add: Adds Corporate Crate Subtype, Reassigns Corporate Crates to It.
fix: Fixes incorrectly mapped biohazard bin.
tweak: Changes Name: Advanced Voidsuit to Advanced Hardsuit.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[1531a570c9...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/1531a570c941d9c87a7013ac5bfef29c3dcc1dcd)
#### Tuesday 2023-11-14 00:33:43 by Andrew

Pipe painting, spraycan preset colors (#79521)

![dreamseeker_AZs0erdnrs](https://github.com/tgstation/tgstation/assets/3625094/06a12d22-387b-4a33-8b61-59bbe3495c82)

## About The Pull Request

Made pipe painter properly paint pipe colors, work on pipe items, and
added the same functionality to regular spraycans.

Spraycans now have the color presets in UI for easier selection of the
valid pipe colors.

## Why It's Good For The Game

Bug fixing is good.
It was weird that spraycans couldn't paint pipes, but some other device
could.
Also custom spraycan color is too clunky, presets are nice for quick
spraycan color selection.

## Changelog

:cl:
fix: fixed pipe painter not applying pipe color properly
qol: made spraycans work also as pipe painters
qol: spraycans now have basic color presets for quick selection
/:cl:

---
## [sthagen/rust-lang-rust-clippy](https://github.com/sthagen/rust-lang-rust-clippy)@[c3a6b376a4...](https://github.com/sthagen/rust-lang-rust-clippy/commit/c3a6b376a43e1ce10c6f17872fd48e99ee294388)
#### Tuesday 2023-11-14 00:34:30 by bors

Auto merge of #11800 - blyxyas:meow-meow, r=Centri3

Removing @Centri3 from reviewer rotation

Catherine decided that the best course of action would be to (maybe temporarily) remove her from the reviewer's rotation (but not unassign her from her current reviews). This PR does that. She'll always be welcomed back if she wants to review some more :heart:

> Alejandra González: [youremyfrennow.mp4](https://rust-lang.zulipchat.com/user_uploads/4715/7nE2W6cb8Q02gcK-vubvmsPM/youremyfrennow.mp4)
>
>Catherine, Fred (`@xFrednet` ) noticed that you aren't as active as in the summer, and proposed that maybe you preferred to be removed from the reviewer rotation. Don't worry, you aren't being taken out of the team, just wanted to know if you maybe preferred to not have those reviews pilling up (they can be pretty stressful to see).
>
>If you decide to step out of the reviewers rotation, you wouldn't be removed from the team, you just wouldn't have that responsability. Everyone takes break and that's fine, so yeah, if you want to not have to review PRs, let me know!
>
>So yeah, from weird teenager transfem to (probably weird) teenager transfem, the choice is in your hand.
>
>Alejandra González: meow meow ^•ﻌ•^
>
>Catherine (Centri3): Yeah that's probably best now, I'll still try with any I'm currently assigned to but I would prefer not to get anymore until then
>Catherine (Centri3): meow meow :3

changelog:none

r? `@Centri3`

---
## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[d751e1c642...](https://github.com/MTandi/tgstation/commit/d751e1c64246612f02089bc4059f3dc686edad2a)
#### Tuesday 2023-11-14 00:43:53 by DaCoolBoss

Adds garbage dumpster ruins (#79446)

## About The Pull Request
Adds 4 small space ruins. Each is a dumpster in space containing hostile
mobs to fight and items to bring back to the station. There's a
decommissioned garbage truck pulling each dumpster which acts as a
staging area before you take on the mobs inside.
All the fights are in cramped dark areas with full pressure, air is
breathable but sometimes has miasma in it so beware of getting sick. So
you can drop your space suit and put on armour, but PKAs won't fire at
full power and keeping a gas mask on is recommended.
Also all the dumpsters look the same from the outside so you gotta crawl
inside to know what's inside. And no you can't metagame it with mesons
either.

Comes in the following flavours:
Food Waste
Full of trash from kitchens, and food. Some of the food is still edible.
There's a lot of territorial rats. You can chop them up into meat if you
want more food. The big prize is a big vat of cooking oil.

Medical Waste
Spare organs, cyberorgans and almost a full set of old surgical gear.
There's a syndicate agent here up to no good and he has a GUN. The gun
blows up when the agent dies so you can't get it. There's a few corpses
of different species in bodybags and some spare corpse parts so you can
bring them back to the station and give them to the coroner. Also a
single use eyestealer in a safe (the cool way to do surgery) and a bug
from the old traitor objective that doesn't do jack but can probably
still get you thrown in perma.

Construction Garbage
Tools and construction materials here, including a cool hammer that fits
in a tool belt and can function as a crowbar. There's also a drug lab
with plenty of weird pills to eat, cigarettes to eat and an angry
russian drug dealer who will stab you if he sees you. He has a badass
lighter and a flamethrower you can take after you kill him. Setting fire
to things in here is not recommended because of all the welding fuel.

Mall Trash
Action figures, trading cards, Christmas crackers and other trash the
local mall tossed out. Also a mothman used to live here but he got eaten
by giant spiders so you can grab his stuff, including snacks and a
civilian modsuit with no mods (wow). You can cut through the webs to
kill the spiders or let them eat you too if you want.
## Why It's Good For The Game
More content for space explorers.
More variety to the potential dangers of space, now u can get sick and
die or get eaten by rats (this is hobo RP)
Better environmental storytelling. Now instead of players left asking
"what happens to the garbage when it goes into space" they can rest
assured that there's busted ass garbage trucks in space. All their
questions are answered.
Loot that encourages working with people on the station. Raw food for
the kitchen, rats for genetics, organs for the coroner, etc
## Changelog
:cl:
add: 4 new space ruins
/:cl:

---
## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[a5fabd8819...](https://github.com/MTandi/tgstation/commit/a5fabd881961cc0c26fdcc93a23a973af1c5cdc3)
#### Tuesday 2023-11-14 00:43:53 by Profakos

Changes to the lore of Knock (#79542)

## About The Pull Request

This PR renames Knock to Lock, and changes most of the knowledge gain
lore.

## Why It's Good For The Game

The Knock Lore, is based on the Knock Principle from Cultist Simulator,
with the path description being copied from the wiki. Many other
keywords and concepts are fully lifted from that game (Locksmith's
Secret, Mother Of Ants, etc). In my vision, if a heretic path has to be
based on a principle from cultist simulator, it should have its own
spin, and also, the knowledge gain texts should tell a story. For
example, Ash tells the story of a watchman burning down their city after
being betrayed, and Cosmic is a love story between a knowledge seeker
and a monster from the beyond.

So I have decided to reflavour Knock. I have changed the name to Lock,
so at least it would feel similar, just like how Blade is akin to Edge.
Many powers also block people or confuse their paths instead of opening
new ways, and thus, I feel a path whose name implies that it *both*
opens and closes would be more self describing.

I have changed most of its lore to be about the Locked Labyrinth, where
knowledge seekers willingly trap themselves and submit themselves to
servitude to find ultimate freedom by progressing through its trials.
These are the Stewards, who are basically workers in an infinite and
malicious hotel in their dreams. Consider them assistants if you will
(this wasn't my intention when I wrote the lore, but thinking about it
in retrospect, it honestly fits). In the implied story, the heretic
joins their ranks, but keeps getting closer to the more corrupt members,
along with parasitic spirits. Ultimately, they manage to open the
Labyrinth's core, letting out the Stewards, allowing them to manifest in
the forms of heretic summon creatures.

The side path spells and the lock knowledge ritual I have not touched,
they were fine. Some items have been renamed and repathed.

I have kept the distinctive sound effect for using the Grasp, as its
unique enough. Though if someone did have a nice sound effect for
turning a lock and added some filters, I would add it.

**DB Issue**

I have renamed the achievement's define to MEDAL_LOCK_ASCENSION but kept
the value as "Knock", as I don't know how trigger a change in the DB. If
this is a blocking change, I'll try to figure out how to make a
migration file.

**Future improvements**

I would also come back later with another PR, that hands out names to
the eldritch beings spawned by the portal, based on the Stewards in the
knowledge gain lore that I added, along with some new ones that fit the
theme, and some jokey ones like Minotaur.

## Changelog

:cl:
spellcheck: Renamed Knock to Locks, and changed most of the flavor text
of knowledge gain, and renamed some items and knowledges from the path.
/:cl:

---
## [Gofawful5/Skyrat-tg](https://github.com/Gofawful5/Skyrat-tg)@[69ea3c81ad...](https://github.com/Gofawful5/Skyrat-tg/commit/69ea3c81ad86a0356af947f11fe3bd2ca953b0af)
#### Tuesday 2023-11-14 00:58:13 by SkyratBot

[MIRROR] Mafia can be played on your PDA [MDB IGNORE] (#24485)

* Mafia can be played on your PDA (#78576)

## About The Pull Request

Mafia is now friggin playable from the PDA, I also changed other stuff
too

- You can't use abilities on dead people if you're not supposed to (cant
kill the same person over and over)
- Changelings cant kill other Changelings
- Changelings can now only talk to eachother at night, rather than using
:j
- Everyone starts spawned in the center of the map, since people playing
on PDA can't move their characters. This is so everyone can hear PDA
users in person, as I don't want the chat log to be mandatory.

To do this, all messages you are meant to be able to see, is now logged
for you to see in your Mafia panel. This essentially means that people
playing through the PDA get a downgraded version of it, but I don't know
how much larger I want this UI to be.

Playing Mafia through the PDA will not tell you of other players ahead
of time when signing up (as it shows ckeys + pdas), but they can see the
names in-game. Unfortunately this means we'll have to remove your
customization coming with you, to prevent using it to tell who is dead
in round.

Things I am missing
- Program overlays on PDA/Laptop/Computer
- Icon for the app's header while a game is active

I'm not a spriter and can't make either of these

This is the new UI

![image](https://github.com/tgstation/tgstation/assets/53777086/7cf503d9-b2e2-4127-874a-acad6425d649)

I also fixed alert calls for PDAs and stuff

![image](https://github.com/tgstation/tgstation/assets/53777086/e09b2e5e-b9e7-43ae-9273-c168e9c8e642)

and removed the X at the top on computers since they had no battery

![image](https://github.com/tgstation/tgstation/assets/53777086/d3dd8307-805c-4aba-be5e-4c24a0bdcb91)

Looks a little better now hopefully 👍

## Why It's Good For The Game

- The current Arcade app sucks, and is a solo game. This is much more
entertaining and you can talk to others in it, which is swag as fuck.
- There's a larger potential playerbase for the Minigame making it more
likely to be played.
- Sets groundwork for a better version of
https://github.com/tgstation/tgstation/pull/75879
- Adds more suspense and teamwork in the minigame.

## Changelog

:cl: JohnFulpWillard, sprites by CoiledLamb
add: You can now play Mafia on your PDA.
balance: Mafia changelings can now only talk to eachother during the
night.
fix: Mafia abilities can't be repeatedly used on people.
/:cl:

* Mafia can be played on your PDA

---------

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>

---
## [Gofawful5/Skyrat-tg](https://github.com/Gofawful5/Skyrat-tg)@[c63f897521...](https://github.com/Gofawful5/Skyrat-tg/commit/c63f897521485898e00425a6c001495f7eef5de6)
#### Tuesday 2023-11-14 00:58:13 by SkyratBot

[MIRROR] It is now possible to survive the Mansus  [MDB IGNORE] (#24490)

* It is now possible to survive the Mansus  (#79131)

## About The Pull Request

Fixes #79113

There were a handful of bugs with the Mansus realm, this PR fixes them.

Firstly an most importantly, a refactor to damage handling touched the
"unholy determination" effect incorrectly (and I'm not even sure why?),
causing it to damage you instead of healing you most of the time. This
damage was not avoidable, so most people would be crit shortly after
entering the area and stay there.

Secondly, some of the heretic realms were unlit. A change to when
lazyloaded template atmosphere initialises means that the bonfires were
trying to light themselves with no air. Now they do this in
late_initialize instead, giving time for air to arrive.

Thirdly, the spooky hands were runtiming when passing through transit
tiles outside of the bounds of the heretic map. They shouldn't be
effected by shuttle drag anyway, so now they aren't.

Fourthly, I removed a row of empty space at the edge of the heretic map,
just because it annoyed me slightly.

Finally, while I was touching the heretic buff I made it heal you 1/4 as
much as it originally did. This is a balance change rather than a fix,
I'll atomise it out if it is controversial but I don't really expect it
to be.
In the future I would like to come back to these and make each realm
more specific to the path, because I think we could make these both more
exciting and more characterful.

## Why It's Good For The Game

Once it is working properly, the hand dodging minigame is actually
extremely forgiving, even if you don't move very much and get frequently
hit. This means some of those hits might actually add some tension.

## Changelog

:cl:
fix: You should be revived properly when entering the mansus realm
following a heretic sacrifice
fix: The buff which is supposed to heal you in the mansus realm will now
do that instead of unavoidably damaging you
balance: The mansus realm's healing buff heals for 25% as much as it did
before it was broken
/:cl:

* It is now possible to survive the Mansus

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Gofawful5/Skyrat-tg](https://github.com/Gofawful5/Skyrat-tg)@[53cfff6ae1...](https://github.com/Gofawful5/Skyrat-tg/commit/53cfff6ae1cd62766395534a6f4c8aa468c5066c)
#### Tuesday 2023-11-14 00:58:13 by SkyratBot

[MIRROR] Actually supports alpha passed into emissive stuff [MDB IGNORE] (#24481)

* Actually supports alpha passed into emissive stuff (#79117)

## About The Pull Request

Ok so like, the emissive procs have an alpha argument right? The thing
is, the thing is it doesn't fucking do anything.

Alpha is a component of the color var (at least when it's a matrix), so
when we set alpha and then set color to a matrix, the alpha gets
overriden. Inverse is also true.

I want to support alpha args, since I like the idea of dimmable
emissives. Soooooo
Let's take the alpha arg, divide it by 255, and replace everything that
cares about alpha (as an intensity thing) with it.

This lets us do transparent emissives and transparent emissive blockers.

I added some guard checks to hopefully avoid the list init most of the
time (it is in theory comprable since color sets should copy but I don't
trust byond to optimize for that)
Also modified the macros to suppport what I'm doing nicely

## Why It's Good For The Game

We should support this, and now we do

* Actually supports alpha passed into emissive stuff

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [Shadowjumper3000/HHHausaufgaben](https://github.com/Shadowjumper3000/HHHausaufgaben)@[53516f5b58...](https://github.com/Shadowjumper3000/HHHausaufgaben/commit/53516f5b58d6421a7f6a3e0a9cf7320266159475)
#### Tuesday 2023-11-14 01:07:47 by Shadowjumper3000

getPlayer2Move

idfk, i spent too long on this already, i fuckin give up, it shouldn't be this goddamn difficult, will retry in morning

---
## [FEX-Emu/FEX](https://github.com/FEX-Emu/FEX)@[bd4464bd5e...](https://github.com/FEX-Emu/FEX/commit/bd4464bd5ee82c34214e5e4e6568d494b73482bb)
#### Tuesday 2023-11-14 01:20:09 by Alyssa Rosenzweig

InstructionCountCI: Remove Optimal flags

Instruction count CI has transformed the way we work on FEX… I love the system
and want to make it better. there’s one part of instruction count CI that isn’t
so lovable: the problematic “optimal” flag on instructions.

There are several issues with this flag, both philosophical and practical.

– it is tedious to update the optimal flag when making an implementation
optimal. The effect of that is discouraging people from making instructions,
optimal, or encouraging people to fail to update the flag, and dilute the value
of it. Either way, since we care far more about optimal implementations, then we
do about updating the flag, clearly we should prioritize the implementation and
not the flag. This issue was not obvious at the outset, when instruction count,
CI was introduced, and still quite small. The problem magnified when we started
duplicating instructions in bulk for different combinations of CPU features
(flagm, AFP, etc.) that intern multiplies the manual work required to update the
flags by the corresponding constant factor. if it comes down to a choice between
removing this extra coverage and removing the flag, I think we all agree that
removing the flag is the lesser evil.

– The definition of “optimal” is fundamentally problematic. I have often
improved the instruction count of an instruction that was already “optimal”.
This is all kinds of silly, and calls into question whether there’s any value
whatsoever in the existing classifications of the flag. Furthermore, it is often
unknowable, whether an implementation really is optimal. Is it possible to
implement BZHI (with flag calculations) in fewer than eight instructions? We
don’t know, and it’s silly to pretend that we do.

– as a consequence of the problematic definitions , there are so many errors in
both directions that I don’t think there’s much value in preserving the existing
classification at the expense of +progress. Being able to say “32% of
instructions are translated optimally” is neat, but it really doesn’t tell us
anything whatsoever when you dig a little deeper.

So, as the flag is misleading at best and perhaps harmful at worst, let’s remove
it and make the instruction count CI, more useful overall. let’s let the
expected count and the assembly speak for themselves, and cut away the chaff. if
we want a meaningless number to report to management, we can instead calculate
the average blowup factor ;-)

Signed-off-by: Alyssa Rosenzweig <alyssa@rosenzweig.io>

---
## [Zergspower/tgstation](https://github.com/Zergspower/tgstation)@[81a7c75583...](https://github.com/Zergspower/tgstation/commit/81a7c75583f75f76d8487b88e63ebaf1402af85b)
#### Tuesday 2023-11-14 01:22:42 by necromanceranne

Hey what if I made Sleeping Carp better at nonlethal takedowns and also deflect with combat mode instead of throw mode (but cost more) (#79517)

## About The Pull Request

It's been a hot minute hasn't it?

When I initially reworked Sleeping Carp, we didn't have combat mode. Now
that we do, and that Sleeping Carp has substantially less defensive
power to justify having to make a choice between deflection and
attacking, it's probably about time we updated this aspect back to what
it was before my rework. Sorta.

Now, we can have all the deniability of the previous method, while also
letting you reliably protect yourself from ranged attacks at all times
while it matters. Because of this, I increased the price up to 17 TC
because of this change just to be on the safe side. The higher uptime of
projectile immunity while also being able to attack during that time
makes this a lot stronger overall.

Secondly, Sleeping Carp presently just isn't as good as a good ol'
baton. It takes a lot more hits to accomplish the same task that a baton
can. Many people feel like they can't even reasonably fight anyone for
fear of the baton, or they would rather use a baton and kill someone at
their leisure. So we've updated some of the moves in order to facilitate
Sleeping Carp as a substantial contender for 1v1 fighting, and lessen
the need for a baton by adding a lot more Stamina damage overall to the
various attacks;

**Keelhaul**: Now a Shove Shove combo. Does literally zero lethal
damage, but now temporarily blinds and dizzies the target as well as its
previous effects. The amount of lethal damage it did was...extremely
small, so this isn't a particularly big loss.

**Grabs and Shoves**: Deal some amount of stamina damage (20). You need
to be in combat mode in order to perform these special attacks (more
deniability). Grabbing someone while they have 80 Stamina damage or more
will cause them to fall unconscious. Yes, I really did just want to add
a Vulcan Nerve Pinch, what do you want from me?

That's it actually. Oh, I guess they are heavy sleepers now too. Because
its funny.

## Why It's Good For The Game

I often get told (read: thrown various insults and slurs at me while
mentioning this as the justification) that Sleeping Carp is not very
strong anymore since it lost all that invisible armor I added way back +
I removed the stuns in my initial rework. This made some people upset (I
think at least one person wished for my death).

So, having given it at least 2 years, I wanted to recapture parts of
what made the older Sleeping Carp (before my rework) strong, some of the
benefits of the new version, and introduce a brand new aspect; nonlethal
takedowns. This makes it beneficial for pacifists, as well as for
kidnapping.

This should not meaningfully make Sleeping Carp any stronger against the
things that typically ruin its day. I suspect in a straight joust with a
baton, Sleeping Carp will still struggle. But against what should be its
strong points (lone targets and ranged weapons), it will be strong once
again rather than clumsily unable to do very much at all.

## Changelog
:cl:
balance: Harnessing Shoreline Quay (bluespace energy, probably), a
mystical energy (total bullshit) that permeates the Astral Waterways
(bluespace quantum dimensions, probably), Sleeping Carp users can now
once against deflect projectiles with their bare hands when focused in
on battle (in combat mode).
balance: The Keelhaul technique is now nonlethal (a philosophical
acknowledgement of the familial bond of sleep and death), but causes the
target to become temporarily blind and dizzy along with its previous
effects.
balance: Sleeping carp users, while in combat mode, deal Stamina damage
with their grabs and shoves. If the target of their grab has enough
Stamina damage (80), they are knocked unconscious from a well placed
nerve pinch.
balance: Sleeping carp users find it very hard to wake up once they fall
asleep....
/:cl:

---
## [dtcxzyw/alive2](https://github.com/dtcxzyw/alive2)@[e031ebd9c1...](https://github.com/dtcxzyw/alive2/commit/e031ebd9c18be1a4fc7f37ab193b4b158b92dd9a)
#### Tuesday 2023-11-14 02:29:21 by Flash Sheridan

Friendlier CMake output and ReadMe tips (#949)

* Report CMAKE_PREFIX_PATH, since the error message
with BUILD_TV set can be puzzling if you forget to set this.

* ReadMe:  CMake may look in /opt/

CMake’s find_package() “searches well-known locations” for configuration information, which can be a nightmare for those of us who have ever had to run an ill-behaved build script, even if we renamed the result, it is not in $PATH, and thought we were safe: https://cmake.org/cmake/help/latest/guide/using-dependencies/index.html#using-pre-built-packages-with-find-package

* Less output for long Lit test

`llvm-lit -s` rather than `-vv` for thousands of tests.

* Detecting unsound transformations in a local run

* README.md CMake advice

Check the “LLVMConfig.cmake” and “CMAKE_PREFIX_PATH” output.

* Painful lessons trying to build for our 15.0.4 fork

* Tightly coupled to LLVM top of tree source:  E.g., the source ca. 15.0.7 was broken for our 15.0.4 fork, due to LLVM f09cf34d00 moving Triple.h ⇒ Alive2 805cf71032e00.
* Experiment with Clang versions and vendors: I couldn’t compile alive2/ir/memory.h:90 with Homebrew Clang 16.0.5, but (surprisingly) could with Apple clang-1400.0.29.202, which is normally worse on open source projects.  This may have been LLVM bug 32386.

* Troubleshooting tip about `BUILD_SHARED_LIBS`

Troubleshooting tip about `BUILD_SHARED_LIBS` with `USEDLIBS` and `LLVMLIBS` and perhaps `dd_llvm_target`.  The first two are from https://llvm.org/docs/Projects.html#variables-for-building-programs. I got further, but not far enough, in linking when I supplemented `dd_llvm_target` with conditional `link_libraries`.

---
## [TheBronJameOffical/lobotomy-corp13](https://github.com/TheBronJameOffical/lobotomy-corp13)@[e23ea7b596...](https://github.com/TheBronJameOffical/lobotomy-corp13/commit/e23ea7b5965a446e5b34f30baa0d4e4dc2d5b868)
#### Tuesday 2023-11-14 03:24:47 by Táculo

Updates La Luna, Pinnochio for Rcorp and playables, gives minions NV on Rcorp AND moves CheckCombat to simple_animal. (#1621)

* Adds Everything

adds nv combat checks to
nosferatu bats
ml slimes
censored minis
tbird spawns
la luna spawned mob

adds mind transfer to pinocchio and la luna
add check for combat to initialize ai controllers for pinocchio, gives him a seclite on rcorp
add check for combat to spawn the breached la luna mob on its position instead of in a random department and to disable the timer.

makes pino ai disabled while a client is possesing it.

* removes one line

* Changes CheckCombat location, applies it to all minions.

* Makes button refuse pino.

fuck you pinocchio

* moves blocking code to pinocchio's

* moves the nightvision checks to simple_animal

moves the nightvision checks to simple_animal

removes the checks from censored, luna, tbird, ml, nosferatu

---
## [TheNeoGamer42/Shiptest](https://github.com/TheNeoGamer42/Shiptest)@[b22529fc74...](https://github.com/TheNeoGamer42/Shiptest/commit/b22529fc74e5af32967ac91679cbce3e7e06c4ca)
#### Tuesday 2023-11-14 03:50:15 by zevo

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
## [cparadis777/GithubGameOff2023](https://github.com/cparadis777/GithubGameOff2023)@[382b40c4d5...](https://github.com/cparadis777/GithubGameOff2023/commit/382b40c4d51e086ce24ee030025672f7e98ab00b)
#### Tuesday 2023-11-14 04:19:09 by plexsoup

fucking with other peoples shit (sorry)

feel free to overwrite with your version if there's a conflict.

---
## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[830e002a27...](https://github.com/realforest2001/forest-cm13/commit/830e002a27b7b4115815e450b8506832cb403a02)
#### Tuesday 2023-11-14 04:29:45 by QuickLode

Adds a Colony Synthetic variant, with bug fixes (#4760)

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

1. should fix fax machine problem(thx forest)
2.  gives trucker synth the frontier jumpsuit(Thwomplert)
3. adds Freelancer Synthetic. This Synth is one that was bought off a
civi market and reprogrammed, or stolen and reprogrammed, or hacked, You
get the point - its going with a band of freelancers. The idea behind it
is that this synth's team is dead and they are just programmed as a merc
for pay - hoping to someday find their boss boss and give the money as
set up. I always thought about this one for a long time and decided to
put him in the civilian category, where its hard to roll and also gives
you freedom to choose your allegiance. In this case I hope that a
freelancer synthetic will open up unique avenue of RP and allegiance.
I've only explored it once ingame, but it was very good for RP!
Hopefully people can recreate this success.

was hard to make this guy look cool and I also wasn't sure on what his
loadout would be. I ended up giving him random generic stuff while
looking like a beat up freelancer(missing the armor especially hurt his
look, since thats the largest piece of a freelancer - the curiass, but I
don't want to give armor for balance reasons) and no beret because its
for a SL only.

as usual, if a synth wants to change RP avenues and don different
clothes for different RP, no one would know the difference
# Explain why it's good for the game
1. bug bad
2. a beat up UA laborer that so happens to be synthetic. you wouldn't
expect it because there's so many similar looking people! exactly the
job of a synth - to blend in.
3. Freelancer colony synth hopefully will open up a unique avenue of RP.
If they don't want to they can always ditch it - but its on a relatively
rare and uncommon roll anyways.
# Testing Photographs and Procedure
<details>
<summary>[Screenshots &
Videos](https://cdn.discordapp.com/attachments/490668342357786645/1166307813719556187/image.png?ex=654a03cb&is=65378ecb&hm=7108218bbaab61c78c0bedcecbfdcc07bdf9db87a3fefe9fb94b28d3430cc815&)</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:
add: adds another Colony Synthetic variant, changes up some existing
ones(trucker,CMB)
fix: fixes a small problem with WY-Colony Synthetic access(thx forest),
adds WY subtype of Synthetics for admin building/faxes
fix: fixes problems with organic spawning ferret industries Trucker
Synthetic
/:cl:

---
## [LueKely/WYU-Frontend](https://github.com/LueKely/WYU-Frontend)@[03f0e9f759...](https://github.com/LueKely/WYU-Frontend/commit/03f0e9f7591ee19180272a1e30fc9f7959fec705)
#### Tuesday 2023-11-14 06:07:41 by LueKely

Mainpage creation (#11)

* Init: home page

* skeleton added

* TANGINA MO FUCK YOu

* im done with this shit

---
## [kingsleyzhong/feeldesign](https://github.com/kingsleyzhong/feeldesign)@[735dc3b041...](https://github.com/kingsleyzhong/feeldesign/commit/735dc3b041393ca8cd246b17695ecd5f5651a1b6)
#### Tuesday 2023-11-14 06:38:14 by Kingsley Zhong

build really failed cuz of downArrow vs downarrow fuck you vercel

---
## [elizazavlieva/Fundamentals-with-Python-_09_2023](https://github.com/elizazavlieva/Fundamentals-with-Python-_09_2023)@[2982170e76...](https://github.com/elizazavlieva/Fundamentals-with-Python-_09_2023/commit/2982170e767c8b57a3c2dae91c067abcc83a2752)
#### Tuesday 2023-11-14 07:26:14 by elizazavlieva

Create rage_quit

9.	 *Rage Quit
Every gamer knows what rage-quitting means. It's when you're just not good enough, and you blame everybody else for losing a game - you press the CAPS LOCK key on the keyboard and flood the chat with gibberish to show your frustration.
Peter is a gamer, a bad one. When he rage-quits, he wants to be the most annoying kid on his team; he wants something truly spectacular. He asks for your help.
He'll give you a series of strings (containing only non-numerical characters) followed by non-negative numbers (N), e.g., "a3". You need to convert the letters to uppercase for each string and print it repeatedly N times on the console. In the example, you need to write back "AAA".
First, on the output, you should print a statistic of the number of unique symbols used (case-insensitive) in the format: "Unique symbols used {0}".
Next, print the rage message itself.
The strings and numbers will not be separated by anything. The input will always start with a non-numeric symbol, and for each string, there will be a corresponding number. The input will be given on a single line.
Input
•	The input data should be read from the console.
•	It consists of a single line holding a series of string-number sequences.
•	The input data will always be valid. There is no need to check it explicitly.
Output
•	The output should be printed on the console. It should consist of exactly two lines:
o	On the first line, print the number of unique symbols used in the message in the format described above.
o	On the second line, print the rage message.
Constraints
•	The count of string-number pairs will be in the range [1 … 20 000].
•	Each string will contain any character except digits. The length of each string will be in the range [1 … 20].
•	The repeat count for each string will be an integer in the range [0 … 20].
•	Allowed working time for your program: 0.3 seconds. Allowed memory: 64 MB.

---
## [walterra/kibana](https://github.com/walterra/kibana)@[cd909f03b1...](https://github.com/walterra/kibana/commit/cd909f03b1d71da93041a0b5c184243aa6506dea)
#### Tuesday 2023-11-14 07:33:21 by Kyle Pollich

[Fleet] Fix inability to upgrade agents from 8.10.4 -> 8.11 (#170974)

## Summary

Closes https://github.com/elastic/kibana/issues/169825

This PR adds logic to Fleet's `/api/agents/available_versions` endpoint
that will ensure we periodically try to fetch from the live product
versions API at https://www.elastic.co/api/product_versions to make sure
we have eventual consistency in the list of available agent versions.

Currently, Kibana relies entirely on a static file generated at build
time from the above API. If the API isn't up-to-date with the latest
agent version (e.g. kibana completed its build before agent), then that
build of Kibana will never "see" the corresponding build of agent.

This API endpoint is cached for two hours to prevent overfetching from
this external API, and from constantly going out to disk to read from
the agent versions file.

## To do
- [x] Update unit tests
- [x] Consider airgapped environments

## On airgapped environments

In airgapped environments, we're going to try and fetch from the
`product_versions` API and that request is going to fail. What we've
seen happen in some environments is that these requests do not "fail
fast" and instead wait until a network timeout is reached.

I'd love to avoid that timeout case and somehow detect airgapped
environments and avoid calling this API at all. However, we don't have a
great deterministic way to know if someone is in an airgapped
environment. The best guess I think we can make is by checking whether
`xpack.fleet.registryUrl` is set to something other than
`https://epr.elastic.co`. Curious if anyone has thoughts on this.

## Screenshots


![image](https://github.com/elastic/kibana/assets/6766512/0906817c-0098-4b67-8791-d06730f450f6)


![image](https://github.com/elastic/kibana/assets/6766512/59e7c132-f568-470f-b48d-53761ddc2fde)


![image](https://github.com/elastic/kibana/assets/6766512/986372df-a90f-48c3-ae24-c3012e8f7730)

## To test

1. Set up Fleet Server + ES + Kibana
2. Spin up a Fleet Server running Agent v8.11.0
3. Enroll an agent running v8.10.4 (I used multipass)
4. Verify the agent can be upgraded from the UI

---------

Co-authored-by: Kibana Machine <42973632+kibanamachine@users.noreply.github.com>

---
## [Fluffy-Frontier/FluffySTG](https://github.com/Fluffy-Frontier/FluffySTG)@[aac7245f72...](https://github.com/Fluffy-Frontier/FluffySTG/commit/aac7245f72184fd33617b8594c69c50b6a95bc5d)
#### Tuesday 2023-11-14 08:03:15 by Iajret Creature

[FIX] Fixes Kick Damage (#24996) (#616)

* holy shit yeah

* Update code/modules/mob/living/carbon/human/_species.dm

---------

Co-authored-by: Nerevar <12636964+Nerev4r@users.noreply.github.com>
Co-authored-by: Snakebittenn <12636964+Snakebittenn@users.noreply.github.com>
Co-authored-by: Bloop <13398309+vinylspiders@users.noreply.github.com>

---
## [Bird-Lounge/Naakas-Lounge](https://github.com/Bird-Lounge/Naakas-Lounge)@[1f1cdc609d...](https://github.com/Bird-Lounge/Naakas-Lounge/commit/1f1cdc609df04a4749b2f3f5d5500551c86021a8)
#### Tuesday 2023-11-14 09:12:08 by Nerevar

[FIX] Fixes Kick Damage (#24996)

* holy shit yeah

* Update code/modules/mob/living/carbon/human/_species.dm

---------

Co-authored-by: Snakebittenn <12636964+Snakebittenn@users.noreply.github.com>
Co-authored-by: Bloop <13398309+vinylspiders@users.noreply.github.com>

---
## [Project-Mist-OS/frameworks_base](https://github.com/Project-Mist-OS/frameworks_base)@[7fde47c20f...](https://github.com/Project-Mist-OS/frameworks_base/commit/7fde47c20fefb9695c0d72f3fcdbaf611bc7de25)
#### Tuesday 2023-11-14 09:23:57 by Kuba Wojciechowski

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
Signed-off-by: Hưng Phan <phandinhhungvp2001@gmail.com>

---
## [Bird-Lounge/Naakas-Lounge](https://github.com/Bird-Lounge/Naakas-Lounge)@[1a2ddececa...](https://github.com/Bird-Lounge/Naakas-Lounge/commit/1a2ddececa5cbc3b3aed161765eab4ebdda105c7)
#### Tuesday 2023-11-14 10:07:51 by SkyratBot

[MIRROR] new space ruin, the biological research outpost [MDB IGNORE] (#24662)

* new space ruin, the biological research outpost (#79149)

## About The Pull Request

![2023-10-21 18 02
39](https://github.com/tgstation/tgstation/assets/70376633/5829e939-3b04-465f-a186-095ceb360bba)

adds this ruin to space ruin pool
this is a shady (as NT always is) bioresearch outpost that got fucked up
by an experiment
this has like some puzzle aspect to it since you gotta find keycards and
shit and press buttons to unlock shield gates
this ends with you fighting a heart which if you defeat, destroys the
blockade that prevents you from entering the outpost vault

also you can no longer literally just cut indestructible grilles or
unanchor indestructible windows

### new puzzle elements or something idk
variant of pressure plate that you cannot remove and it sends a puzzle
signal
cooler red puzzle doors that look very foreboding or something idk
theyre for this ruin
also puzzle blockades, which are indestructible dense objects that are
destroyed if they receive a puzzle signal
and also buttons and keycard pads for puzzles

https://github.com/tgstation/tgstation/assets/70376633/c98807ec-1e7b-49c4-a757-cdbb76a1b566

https://github.com/tgstation/tgstation/assets/70376633/9d5d9dd1-5868-44e6-a978-5ea57b30c298

stuff that throws electric shocks in a pattern, ignores insuls and only
knocks down, and no you cannot just run past

https://github.com/tgstation/tgstation/assets/70376633/5772917c-a963-48a4-a743-b0f610801d25

### enemies
living floor, it can only attack stuff on top of it and it attacks until
the victim is dead
it is invincible to all but a crowbar, and it cannot move, and it
remains hidden until a victim is in range

https://github.com/tgstation/tgstation/assets/70376633/aa1d54f6-b259-4e58-9d44-e393d2131acf

living flesh, it can replace your limbs with itself
the conditions for that are; the limb must have 20 or more brute, victim
must be alive and dismemberable, the limb may not be torso or head, or
the limb may not be living flesh
alternatively it can replace a missing limb
these are all checked with every attack
they have 20 hp
the limbs in question will sometimes act up, while passively draining
nutrition, arms will randomly start pulling nearby stuff, legs may step
randomly
limbs when detached, turn into mobs and reactivate AI 2 seconds later.
if the host is shocked, all living flesh limbs will detach, or if the
host dies they will also do that

https://github.com/tgstation/tgstation/assets/70376633/765cc99e-c800-4efb-aabe-d68817bbd7ae

## Why It's Good For The Game

ruin variety is cool i think
also the other things i added should be useful for other mappers for
bitrunning or whatever

also bug bad for that one fix
## Changelog
:cl:
add: living floor, living flesh, and other stuff for the bioresearch
outpost ruin
add: bioresearch outpost ruin
fix: you may not defeat indestructible grilles and windows with mere
tools
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@ gmail.com>

* new space ruin, the biological research outpost

---------

Co-authored-by: jimmyl <70376633+mc-oofert@users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@ gmail.com>

---
## [CliffracerX/Skyraptor-SS13](https://github.com/CliffracerX/Skyraptor-SS13)@[3a299fb994...](https://github.com/CliffracerX/Skyraptor-SS13/commit/3a299fb994067172e0c2891aae549a17992e3fae)
#### Tuesday 2023-11-14 10:10:50 by lizardqueenlexi

[CI Fix] The Demonic Frost-Miner will not attack corpses. (#79294)

## About The Pull Request

Fixes #79147.

Prevents the Demonic Frost-Miner from shooting at corpses by returning
early from `OpenFire()`. Also adds the "gutted" status effect to the
corpses in its arena so it won't try to gut them.
## Why It's Good For The Game

#78826 introduced an unfortunate bug by placing corpses in the Frost
Miner's arena. There were a combination of three factors at play here:
that the Miner attacks corpses, that it happens to use colossus bolts in
its attacks, which dust corpses, and that some unfortunate quirk of life
code causes runtimes if, as far as I can tell, a life tick goes off when
a mob is at the wrong point in the dusting process. The time this
process takes happened to perfectly coincide with the Monkey Business
unit test (being the first test that takes a significant period of
time), causing it to randomly fail.

So, this fixes a flaky test that has been a pain in the ass for the last
five days, is the big thing.

Also, it can't possibly have been intended for the Miner to run around
obliterating the aesthetic corpses in its arena within the first 15
seconds of any given round. Completely ruining the mood!

I'll point out that this particular boss may have been forgotten in
#77731, which set out to make only the colossus still gib/dust you, but
even were that not the case I think it would be a bit silly for the
Miner to be busy shooting lifeless corpses when a player shows up to
challenge it, rather than standing in its scary ritual circle.
## Changelog
:cl:
fix: The Demonic Frost-Miner will no longer run around destroying the
corpses in its arena the moment the round begins.
/:cl:

---
## [nmagnezi/assisted-service](https://github.com/nmagnezi/assisted-service)@[564650feca...](https://github.com/nmagnezi/assisted-service/commit/564650feca372064314282d98d6fd9c6ee69bd2c)
#### Tuesday 2023-11-14 11:04:54 by Omer Tuchfeld

MGMT-10973: Enable DNS validations if coredns or keepalived static pod manifests in day-2 connectivity-check ignition (#4072)

For context, this is a service-side follow-up to:

https://github.com/openshift/assisted-installer-agent/pull/388

and also this small agent fix https://github.com/openshift/assisted-installer-agent/pull/403

# Goal

During day-2 installations, we want the service to optionally perform
DNS validations when the worker attempts to join none-platform clusters.

# Issue

When the cluster is imported via our `.../v2/clusters/import` endpoint,
we have no way to know whether that cluster is a none-platform cluster
or cluster with managed networking (e.g. baremetal), so we have no way
to know whether we should perform the DNS validation or not. We wouldn't
like to have that validation on all the time, because it's unnecessarily
annoying for clusters with managed networking.

# Background

As part of our existing API connectivity-check, the service asks the
agent to download the worker.ign file from the to-be-joined-cluster's
machine-config-server, then send that back to the service.

# Solution

The contents of that file include information that will allow the
service to make an educated guess about whether the ignition originated
from a cluster with managed networking or not.

Also, a new "imported" column has been added to clusters, to indicate
whether they were created through a conversion or through being
imported. This is important because the solution should only be
applied for imported clusters, and this will provide a good way
to tell apart imported from non-imported clusters.

Also, when a user imports a cluster, we will inspect the `params.NewImportClusterParams.APIVipDnsname`
parameter and extract:

- The cluster name
- The cluster base domain

The cluster name will override the name given in `params.NewImportClusterParams.Name`,
see diff comment for more information on why.

The cluster base domain will be used to set the `BaseDNSDomain` of the
cluster, because up until now we didn't set it for imported cluster.

The reason `BaseDNSDomain` and `Name` have to be correctly set is
because the DNS validations use them to construct the domain names
that are being validated.

Also updated some validation messages for the API connectivity check and
DNS validations.

Also, the clusterdeployments_controller can now import SNO clusters,
it was an oversight that should have been done as part of 4cda26533d377f453f68783e8b2eae438734555d (#3404)

# Ignition Files

The ignition files we currently look at are:

```
/etc/kubernetes/manifests/coredns.yaml
/etc/kubernetes/manifests/keepalived.yaml
```

This is a hack - since we have no official way to know whether a worker
ignition file originated from a cluster with managed networking or not,
we instead rely on the presence of coredns and keepalived pod manifests
to indicate that. We only expect those to be present in clusters with
managed networking. To be a bit more robust, the service will consider
the presence of any one of them to mean that the cluster has managed
networking. This gives us better forwards compatibility if one of them
gets renamed / replaced with other technologies in future OCP versions.

Another way in which this is hacky is that users could manually create
static pods with the same name as part of their machine-configs, in
which case we would have a false-positive detection. But that is
admittedly very unlikely.

Hopefully we can negotiate with the relevant OCP teams to have a more
official, stable way to have this detection - like a magic empty file
placed somewhere in the ignition that we can check for the presence of.
Once we have such file, we can slowly deprecate this detection mechanism
and fully move to the new one by inspecting that file instead.

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[2b0bf5ea5e...](https://github.com/TaleStation/TaleStation/commit/2b0bf5ea5e6afa983130a925463467a26ece0955)
#### Tuesday 2023-11-14 11:45:51 by TaleStationBot

[MIRROR] [MDB IGNORE] Basic Guardians/Holoparasites (#8552)

Original PR: https://github.com/tgstation/tgstation/pull/79473
-----
## About The Pull Request

Fixes #79485
Fixes #77552

Converts Guardians (aka Holoparasites) into Basic Mobs.
Changes a bunch of their behaviours into actions or components which we
can reuse.
Replaces some verbs it would give to you and hide in the status panel
with action buttons that you may be able to find more quickly.

They _**should**_ work basically like they did before but a bit
smoother. It is not unlikely that I made some changes by accident or
just by changing framework though.

My one creative touch was adding random name suggestions.
The Wizard federation have a convention of naming their arcane spirit
guardians by combining a colour and a major arcana of the tarot. The
Syndicate of course won't truck with any of that mystical claptrap and
for their codenames use the much more sensible construction of a colour
and a gamepiece.

This lets you be randomly assigned such creative names as "Sparkling
Hermit", "Bloody Queen", "Blue World", or "Purple Diamond".
You can of course still ignore this entirely and type "The Brapmaster"
into the box if so desired.

I made _one_ other intentional change, which is to swap to Mothblocks'
nice leash component instead of instantly teleporting guardians back to
you when they are pulled out of the edge of their range. They should now
be "dragged" along behind you until they can't path, at which point they
will teleport. This should make the experience a bit less disorienting,
you have the recall button if you _want_ to instantly catch up.

This is unfortunately a bumper-sized PR because it did not seem
plausible to not do all of it at once, but I can make a project branch
for atomisation if people think this is too much of a pain in the ass to
review.

Other changes:
- Some refactoring to how the charge action works so I could
individually override "what you can hit" and "what happens when you hit"
instead of those being the same proc
- Lightning Guardian damage chain is now a component
- Explosive Guardian explosive trap is now a component
- Added even more arguments to the Healing Touch component to allow it
to heal tox/oxy damage and require a specific click modifier
- Life Link component which implements the Guardian behaviour of using
another mob as your health bar
- Moved some stuff about deciding what guardians look and are described
like into a theming datum
- Added a generic proc which can return whether your mob is meant to
apply some kind of damage multiplier to a certain damage type. It's not
perfect because I couldn't figure out how ot cram limb modifiers in
there, which is where most of it is on carbons. Oh well.
- Riders of vehicles now inherit all movement traits of those vehicles,
so riding a charging holoparasite will let you cross chasms. Also works
if you piggyback someone with wings, probably.

## Changelog

:cl:
refactor: Guardians/Powerminers/Holoparasites now use the basic mob
framework. Please report any unexpected changes or behaviour.
qol: The verbs used to communicate with, recall, or banish your Guardian
are now action buttons.
balance: If (as a Guardian) your host moves slightly out of range you
will now be dragged back into range if possible, rather than being
instantly teleported to them.
balance: Protectors now have a shorter leash range rather than a longer
one, in order to more easily take advantage of their ability to drag
their charge out of danger.
balance: Ranged Guardians can now hold down the mouse button to fire
automatically.
balance: People riding vehicles or other mobs now inherit all of their
movement traits, so riding a flying mob (or vehicle, if we have any of
those) will allow you to cross chasms and lava safely.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: san7890 <the@san7890.com>

---
## [amameuser/mame](https://github.com/amameuser/mame)@[65ec4542ca...](https://github.com/amameuser/mame/commit/65ec4542ca3c0092247ebcab86d21eff987e4472)
#### Tuesday 2023-11-14 11:49:16 by wilbertpol

msx2_flop.xml: Added 54 items (49 working) and replaced one item with a better dump. (#11698)

* Replaced VS Rotation (Japan) with a better dump. [file-hunter]
* Removed Ultima IV - Quest of the Avatar (Japan, alt disk 2) (disk 2 is from an English translation).
* Removed Vectron (Netherlands) and Vectron (Netherlands, alt) (extracted from a compilation).
* Removed Zoo (Netherlands, alt) and Zoo (Netherlands, alt 2) (hacked versions)

New working software list items (msx2_flop.xml)
-------------------------------
Konami Game Collection Bangai-hen (Japan, alt) [file-hunter]
The Legend of Shonan (Japan) [file-hunter]
Sailor-fuku Senshi Felis (Japan) [file-hunter]
Tempo Typen (Netherlands) [file-hunter]
Tenkyuhai Special - Tougen no Utage (Japan) [file-hunter]
Tenkyuhai Special - Tougen no Utage II (Japan) [file-hunter]
Thanatos (Japan) [file-hunter]
Tokimeki Sports Gal (Japan) [file-hunter]
Tominaga Koukou Tantei-bu (Japan) [file-hunter]
Trilogy Kuki Youka Shinden (Japan) [file-hunter]
The Tucs (Japan) [file-hunter]
Tulip Ichigou (Japan) [file-hunter]
Ultima II - The Revenge of the Enchantress (Japan) [file-hunter]
Undead Line (Woomb) [file-hunter]
Wizardry Scenario #3 - The Legacy of Llylgamyn (Japan) [file-hunter]
Xak - The Art of Visual Stage (Japan, Woomb) [file-hunter]
Yoshida Koumuten Data Library Vol. 2 (Japan) [file-hunter]
Yoshida Koumuten Data Library Vol. 3 (Japan) [file-hunter]
Yume Pro RPG Shaon-ban (Japan) [file-hunter]
Yumeji Asakusa-Kitan (Japan) [file-hunter]
Yuurei-kun (Japan) [file-hunter]
Zoo (Europe) [file-hunter]
GAME100 (Japan) [file-hunter]
Go! Volcano [NAGI-P SOFT]
Las Aventuras de Rudolphine Rur (Spanish) [Dwalin]
MSX Light [MSXdev]
Siege [NAGI-P SOFT]
Teddy's in Action Part 2 [file-hunter]
Terrahawks [file-hunter]
Tetravex (Netherlands) [file-hunter]
Tetris Master (Japan) [file-hunter]
Tetris Master - Operation Maison Ikkoku (Japan) [file-hunter]
Tetris Master - Operation Orange Road (Japan) [file-hunter]
Tetris Master - Operation Ranma 1/2 (Japan) [file-hunter]
Tetris Master - Series 1 Ranma 1/2 (Japan) [file-hunter]
Thunderbirds are Go (Netherlands, promo) [file-hunter]
Thunderbirds to the Rescue (Netherlands, promo) [file-hunter]
Tile Golf [NAGI-P SOFT]
Triplex (Netherlands) [file-hunter]
Trivial Pursuit (Netherlands) [file-hunter]
Trivial Pursuit - Aanvulling Jaareditie 1995 (Netherlands) [file-hunter]
Tunez: Garfield Edition [file-hunter]
The UHF Painter (Italy) [file-hunter]
War World FM-PAC Demo (Netherlands) [file-hunter]
Wiz Kids (Japan) [file-hunter]
Yupipati (demo) [file-hunter]
Zombie Night [Alberto Sgaggero]
Zoo Rally (Russia) [file-hunter]
Zoto (Germany?) [file-hunter]

New NOT_WORKING software list additions (msx2_flop.xml)
------------------------------------------
HBI-V1 Video Digitizer (Japan) [file-hunter]
Himitsu no Hanazono (Japan) [file-hunter]
Veldslag (Netherlands) [file-hunter]
Zeeslag (Netherlands) [file-hunter]
Zeeslag (Netherlands, demo) [file-hunter]

---
## [gvmii/gumi.gay](https://github.com/gvmii/gumi.gay)@[4d1cd5e17a...](https://github.com/gvmii/gumi.gay/commit/4d1cd5e17a789f376d4157e0fc1a285f4dbfa4d7)
#### Tuesday 2023-11-14 12:00:34 by Gumi

do insane fucking shit. INSANE!!! INSANE FUCKING SHIT LOOK HOW COOL THIS IS

---
## [argilla-io/argilla](https://github.com/argilla-io/argilla)@[300bfa58f1...](https://github.com/argilla-io/argilla/commit/300bfa58f1a7469019921f921f411f1c25bcd984)
#### Tuesday 2023-11-14 12:06:54 by Ayan Joshi

Updated Broken Links  (#4076)

# Argilla Community Growers

Thanks for your contribution! As part of our Community Growers
initiative 🌱, we're donating Justdiggit bunds in your name to reforest
sub-Saharan Africa. To claim your Community Growers certificate, please
contact David Berenstein in our Slack community or fill in this form
https://tally.so/r/n9XrxK once your PR has been merged.

# Pull Request Templates

Please go the the `Preview` tab and select the appropriate sub-template:

* [🐞-bug](?expand=1&template=bug.md)
* [📚-documentation](?expand=1&template=docs.md)
* [🆕-features](?expand=1&template=features.md)

# Generic Pull Request Template

Please include a summary of the changes and the related issue. Please
also include relevant motivation and context. List any dependencies that
are required for this change.



**Type of change**

(Please delete options that are not relevant. Remember to title the PR
according to the type of change)

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing
functionality to not work as expected)
- [ ] Refactor (change restructuring the codebase without changing
functionality)
- [x] Improvement (change adding some improvement to an existing
functionality)
- [x] Documentation update

**How Has This Been Tested**

(Please describe the tests that you ran to verify your changes. And
ideally, reference `tests`)

- [ ] Test A
- [ ] Test B

**Checklist**

- [x] I added relevant documentation
- [ ] follows the style guidelines of this project
- [ ] I did a self-review of my code
- [ ] I made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my
feature works
- [ ] I filled out [the contributor form](https://tally.so/r/n9XrxK)
(see text above)
- [ ] I have added relevant notes to the CHANGELOG.md file (See
https://keepachangelog.com/)

There were two broken links in the Readme , I fixed it of the
cheatsheets and the Contribution guidelines Have a look
at my pr @davidberenstein1957

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[5175ae0637...](https://github.com/tgstation/tgstation/commit/5175ae06374450b87324bb280c754e53880b7b16)
#### Tuesday 2023-11-14 13:17:43 by John Willard

TGUI Destructive Analyzer (#79572)

## About The Pull Request

I made this to help me move more towards my goals [laid out
here](https://hackmd.io/XLt5MoRvRxuhFbwtk4VAUA) which currently doesn't
have much interest.

This makes the Destructive Analyzer use a little neat TGUI menu instead
of its old HTML one. I also touch a lot of science stuff and a little
experimentor stuff, so let me explain a bit:
Old iterations of Science had different items that you can use to boost
nodes through deconstruction. This has been removed, and its only
feature is the auto-unlocking of nodes (that is; making them visible to
the R&D console). I thought that instead of keeping this deprecated code
around, I would rework it a little to make it clear what we actually use
it for (unhiding nodes).
All vars and procs that mentioned this have been renamed or reworked to
make more sense now.

Experimentor stuff shares a lot with the destructive analyzer, so I had
to mess with that a bit to keep its decayed corpse of deprecated code,
functional.

I also added context tips to the destructive analyzer, and added the
ability to AltClick to remove the inserted item. Removing items now also
plays a little sound because it was kinda lame.
Also, balloon alerts.

## Why It's Good For The Game

Moves a shitty machine to TGUI so it is slightly less shitty, now it's
more direct and compact with more player-feedback.
Helps me with a personal project and yea

### Video demonstration

I show off connecting the machine to R&D Servers, but I haven't changed
the behavior of that and the roundstart analyzers are connected to
servers by default.


https://github.com/tgstation/tgstation/assets/53777086/65295600-4fae-42d1-9bae-eccefe337a2b

## Changelog

:cl:
refactor: Destructive Analyzers now have a TGUI menu.
/:cl:

---
## [hironow/argilla](https://github.com/hironow/argilla)@[503c0d42ea...](https://github.com/hironow/argilla/commit/503c0d42eab2d617f7e556789c6f3c4b091ef0f9)
#### Tuesday 2023-11-14 13:50:18 by David Berenstein

docs: changed some warning to more friendly notes (#4108)

<!-- Thanks for your contribution! As part of our Community Growers
initiative 🌱, we're donating Justdiggit bunds in your name to reforest
sub-Saharan Africa. To claim your Community Growers certificate, please
contact David Berenstein in our Slack community or fill in this form
https://tally.so/r/n9XrxK once your PR has been merged. -->

# Description

changed some warning to more friendly notes

Closes #4107

**Type of change**

(Remember to title the PR according to the type of change)

- [X] Documentation update

**How Has This Been Tested**

(Please describe the tests that you ran to verify your changes.)

- [X] `sphinx-autobuild` (read [Developer
Documentation](https://docs.argilla.io/en/latest/community/developer_docs.html#building-the-documentation)
for more details)

**Checklist**

- [X] I added relevant documentation
- [X] I followed the style guidelines of this project
- [X] I did a self-review of my code
- [X] I made corresponding changes to the documentation
- [X] My changes generate no new warnings
- [ ] I filled out [the contributor form](https://tally.so/r/n9XrxK)
(see text above)
- [X] I have added relevant notes to the `CHANGELOG.md` file (See
https://keepachangelog.com/)

---
## [JarRaid/HorrorGame](https://github.com/JarRaid/HorrorGame)@[227bec7b9d...](https://github.com/JarRaid/HorrorGame/commit/227bec7b9d91f1256063442bbff6d438a2877c60)
#### Tuesday 2023-11-14 14:35:46 by salataa1

Chandelier and window 4 update

Added other andrew's shitty ass chandelier that i had to basically redo the unwrap for. made it as pretty as I could. If he submits one in his push for the merge, use this one instead. also changed the alpha map on the top down view of the church window to reflect the nursery location we're going with

---
## [facebook/buck2-prelude](https://github.com/facebook/buck2-prelude)@[fc7a6a72a1...](https://github.com/facebook/buck2-prelude/commit/fc7a6a72a1530896dbe0378fce5f0ce47866e3da)
#### Tuesday 2023-11-14 14:45:15 by Jakob Degen

toolchain: Set up no-sysroot deps toolchain

Summary:
This diff lays out how I want to avoid the cyclic dependency issue with explicit sysroot deps compiled from source.

Doing this by defining a second toolchain is generally appropriate I think. Asking crates that expect to be compiled as members of the sysroot to declare that by specifying a non-default toolchain seems correct. Also, a constraint would be inappropriate here because we do not generally want to propagate this to all target dependencies, and because it runs into risks of accidentally ending up with the same dep in your build twice, under two different configurations.

I didn't bother trying to add support to `override_rust_toolchain` for this because we'd need something like `attrs.struct()` to make that not super ugly. Plus, rules are good and people should write more of them.

The one potentially controversial decision in this diff is the choice to put the override above the massive toolchain select tree, instead of below. On balance, I'd guess that this is the better thing to do. This override is only responsible for inserting the sysroot targets; I expect that it'll only ever grow two cases, one for fbcode sysroot targets and one for fbsource ones. That means we'll never need all the complicated machinery that's in the big select tree. Plus, selectified toolchains are good anyway.

Reviewed By: capickett

Differential Revision: D51014702

fbshipit-source-id: 970de5291aa725e1e5e1e22fdde53603e1e4d412

---
## [SevenworksDev/DeadHack](https://github.com/SevenworksDev/DeadHack)@[877b94b6cd...](https://github.com/SevenworksDev/DeadHack/commit/877b94b6cdc3b11aabde19fee02a74beb2e851dd)
#### Tuesday 2023-11-14 14:45:48 by Sevenworks

Delete dont use, i hate file transfer so much i want to throw someone off a god damn building.pyw

---
## [TetraK1/tgstation](https://github.com/TetraK1/tgstation)@[9e18c6575a...](https://github.com/TetraK1/tgstation/commit/9e18c6575a3cb9e73c3e699d4fe51b904b76e2f6)
#### Tuesday 2023-11-14 14:52:22 by lizardqueenlexi

Basic Pirate NPCs (#79284)

## About The Pull Request

Converts hostile pirate NPCs to basic mobs - specifically, a subtype of
trooper. As their behavior is not meaningfully distinct from other
troopers, this conversion mostly just sticks them on the existing AI
behavior while keeping the rest the same.

Pirates do have one new thing going for them, though, to differentiate
them from other troopers. They use the new **plundering attacks**
component, which means that every time they land a melee attack, they
steal money from the bank account of whoever they hit. This requires the
target to be wearing an ID with a linked bank account, so it's not the
hardest thing in the world to hide your money from them - but it's still
something to be wary of! If killed, any mob with this component will
drop everything they've stolen in a convenient holochip.
## Why It's Good For The Game

Takes down 5 more simplemobs, and (I think) converts the last remaining
trooper-type enemy to be a basic trooper. (It's possible there's more
I've forgotten that could use the same AI, though.)

The money-stealing behavior is mostly good because I think it's funny,
but it also makes the pirates something a little distinct from "yet
another mob that runs at you and punches you until you die". They still
do that, but now there's a little twist! This can be placed on other
mobs too, if we want to make any other sorts of thieves or brigands.
## Changelog
:cl:
refactor: Pirate NPCs now use the basic mob framework. They'll be a
little smarter in combat, and if you're wearing your ID they'll siphon
your bank account with every melee attack! Beware! Please report any
bugs.
/:cl:

---
## [EvaEvaEvaEvaEva/shaptest](https://github.com/EvaEvaEvaEvaEva/shaptest)@[40dfaf3734...](https://github.com/EvaEvaEvaEvaEva/shaptest/commit/40dfaf3734000b5e74e4101ab86516702f59425f)
#### Tuesday 2023-11-14 15:21:10 by Imaginos16

Reworks The Visuals Of Independent And Nanotrasen Captains (#2453)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Does what it says in the title. This is a demented PR that touches a lot
of things, but its main benefit is that now regular independent
captains, cowboy independent captains, and nanotrasen captains have a
unique identity.

Of those changed, it includes:

- The Nanotrasen Captain (parade)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/48a31cb1-b266-43cb-9b6e-525028893011)

- The Nanotrasen Captain (regular)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/799c88f0-b7ce-4736-956d-2e9c0a096433)

- The Independent Captain (regular/parade)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/17ecb3d3-5f2f-4ce0-a518-81366945ebdf)

- The Independent Captain (western)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/a56a798c-5adf-41d7-917a-730661f306ed)

The PR also axes a bunch of unused, or frankly quite basic lieutenant
outfits that were nothing more than set dressing with not much substance
behind them. The roles were not removed for now, and they have
appropriate outfits as a placeholder pending a full removal.

This also means that the Head of Personnel was slightly touched up,
mostly by having a coat and hat similar to the western captain's when
appropriate. The role itself is pending a full visual rework for later
that is beyond the scope of this PR.

Speaking of removals, this also means that captain outfits/roles that
were there as a legacy of removed ships, were finally axed for good.
Goodbye deserter captain for Riggs variant number 4, you will not be
missed.

This PR also touches several (a lot) of maps, mostly adding/removing
outfits that were either missing, or didn't fit with the dress code of
the vessel.

Also the PR fixes an oversight by @MarkSuckerberg by making the BYOND
version warning an actual warning, instead of an error when compiling.
Etto bleh.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Visual cohesion is important, and dear fucking god if I see one more
independent western captain not wearing the duster because it wasn't in
the ship, I will weep, and my weeping will cause a biblical deluge.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy
imageadd: Outfits for independent and Nanotrasen captains have been
violently reworked.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [yadamvijaykumar/codetice_taskno_1](https://github.com/yadamvijaykumar/codetice_taskno_1)@[6c75da4f8c...](https://github.com/yadamvijaykumar/codetice_taskno_1/commit/6c75da4f8c648f88156d0a44734b193d98c38db4)
#### Tuesday 2023-11-14 15:37:01 by yadamvijaykumar

Add files via upload

# URL Shortener Project

## Overview

This URL Shortener project is a simple yet effective tool for shortening long URLs using Tkinter for the graphical user interface and the pyshorteners library for URL shortening functionality.

## Author

*Author:* YADAM VIJAY KUMAR

*LinkedIn:* [ YADAM VIJAY KUMAR ] (https://www.linkedin.com/in/vijaykumar-yadam-300155264)

## Project Structure

The project is structured as a Python script using Tkinter for the GUI. The main features include:

- User-friendly Interface
- URL Shortening with TinyURL
- Error Handling for a smooth user experience

## Usage

1. Run the script.
2. Enter a long URL in the provided entry field.
3. Click the "Shorten URL" button.
4. The shortened URL will be displayed in the output entry field.

## Dependencies

Ensure that you have the required libraries installed by running the following command:

bash
pip install tk pyshorteners


## Contribution

Feel free to contribute or provide feedback to enhance the functionality of this simple URL shortener. Your suggestions are valuable!

## About the Author

Pydisetti Vineesh is currently interning under Codetice Company. Connect with him on [LinkedIn](https://www.linkedin.com/in/vineesh-pydisetti-28464421b/) for more updates and discussions.

Enjoy shortening your URLs! 🚀

---
## [NetBSD/pkgsrc](https://github.com/NetBSD/pkgsrc)@[df7f72586d...](https://github.com/NetBSD/pkgsrc/commit/df7f72586d191d81a209f924851daea24e31cb92)
#### Tuesday 2023-11-14 15:45:45 by wiz

cairo: update to 1.18.0.

Merge cairo-gobject into this, per discussion on tech-pkg.

Release 1.18.0 (2023-09-20 Emmanuele Bassi <ebassi@gnome.org>)
==============================================================

The first stable cairo release in five years should be cause for celebration.

All the API added in the 1.17 development cycle is now considered stable, and
will not change.

Many thanks to all the contributors for this release.

The cairo-sphinx tool has been removed; we could not find any instruction on
how to use it, and no user answered our call for help. If you were using
cairo-sphinx, please reach out to the cairo maintainers.

Cairo now implements Type 3 color fonts for PDF. Thanks to Adrian Johnson for
his work on this feature.

Khaled Hosny contributed multiple documentation fixes, to ensure that the
cairo API reference is up to date. Khaled also fixed multiple compiler
warnings generated when building cairo.

The XML surface has been removed; it was disabled by default when building
cairo, and we could not find any downstream distributor that would enable
it.

The Tee surface is now automatically enabled. Downstream distributors of
cairo have been enabling for years it in order to build Firefox.

Fujii Hironori and Adrian Johnson fixed multiple issues with the DWrite
font backend.

John Ralls improved the Quartz surface; mainly, Quartz surfaces now use
the main display ColorSpace, speeding up rendering operations.

Cairo now hides all private symbols by default on every platform; the old
"slim" symbols hack to alias internally used symbols has been dropped, in
favor of using `-Bsymbolic-functions` with toolchains that support it.

Uli Schlachter fixed multiple memory leaks in the code base and test suite,
and helped with many reviews and general maintenance.

Marc Jeanmougin added new API to expose the Pixman dithering filter to cairo
patterns; this is currently implemented only for image surfaces.

Release 1.17.8 (2023-01-30 Emmanuele Bassi <ebassi@gnome.org>)
==============================================================

A new cairo snapshot! And it only took less than one year, this time!

Many thanks to everyone who contributed to cairo, and especially
to (in no particular order):

- Adrian Johnson
- Khaled Hosny
- Behdad Esfahbod
- Matthias Clasen
- Uli Schlachter
- Manuel Stoeckl
- Fujii Hironori
- Tim-Philipp Müller
- Luca Bacci
- Caolán McNamara
- John Ralls

In a continuing effort to reduce the amount of legacy code, and increase
the long-term maintainability of cairo, the following backends have been
removed:

- GL and GLES drawing

Additionally, cairo's Autotools build system has been removed; from now on,
cairo will only support the Meson build system. While the end result should
be identical, further testing is appreciated.

In this snapshot, cairo gained support for rendering COLRv1 fonts, and
rendering SVG and COLRv1 fonts with custom palettes.

Support for macOS and Windows has been improved, with lots of build and bug
fixes.

Lots of safety issues have been fixed, with array bounds checking and
plugging memory leaks, as well as fixes for bugs identified via fuzzying.

This is going to be the last snapshot of the 1.17 development cycle; we only
expect minor bug fixing and improvements until the 1.18.0 release.

Release 1.17.6 (2022-03-18 Emmanuele Bassi <ebassi@gnome.org>)
==============================================================

I spy with my little eye… a cairo snapshot!

First of all, many, many thanks to everyone who contributed to cairo
during this development cycle. A special thank you goes to:

- Adrian Johnson
- Uli Schlachter

for their tireless efforts in ensuring that the lights are still on
in the cairo project.

This snapshot sees the removal of the following backends and platform
support:

- Qt4
- BeOS
- OS/2
- DirectFB
- DRM
- Cogl
- OpenVG

Thanks to all past contributors for their work on them. If you were using
any of these backends then you will need to stick to cairo 1.16.

To offset the removal of the backends above, Adrian Johnson landed the
DWrite font rendering backend on Windows.

There have been multiple improvements in the Quartz backend, courtesy of
John Ralls.

Tim-Philipp Müller has kept the Meson build in top shape.

This snapshot is going to be the **last** release of cairo with the
Autotools build system. The Meson build has seen many improvements and
it is considerably easier to maintain and faster to build.

Release 1.17.4 (2020-11-27 Bryce Harrington <bryce@bryceharrington.org>)
========================================================================

Thank you to the many people who have contributed the large number of
bug fixes and refinements since 1.17.2.

A particularly noteworthy improvement in this release is the addition of
the meson build system as an alternative to autotools.  Autotools is
still used for producing the releases, so will be the default in the
tarball and presumably will still be preferred by distro packagers of
Cairo.  It should be possible to build the release tarball using meson,
but as this is new functionality consider it still a work in progress.
The meson configuration has striven to track the autotools
implementation but be aware there may still be some differences between
the two.

Continuous Integration configurations have been added that enable
testing on a variety of platforms including Fedora, Windows MSVC, etc.
This work has helped in identifying updates and fixes including
adjusting to changes in API calls in dependencies like rsvg and
fontconfig, and to fix platform-specific build issues.

The cogl Cairo backend underwent significant development this cycle.
Cogl provides GPU accelerated drawing support.  The development work
includes implementation of core functionality, performance
optimizations, and stabilization.

Subpixel positioning support allows improved glyph outlines with the
FreeType font backend.

For a complete log of changes, please see

    https://cairographics.org/releases/ChangeLog.1.17.4

[On a personal note, this will be my last release for Cairo.  My Cairo
time availability has been non-existent (particularly this crazy past
year).  The release process is well documented and hopefully will help
whomever picks up the baton from here.]


Release 1.17.2 (2019-01-31 Bryce Harrington <bryce@bryceharrington.org>)
========================================================================
This snapshot provides the new support for writing floating point
formats as 16 bpc PNGs, with support for RGBA128F and RGB96F formats.
This new feature increases Cairo's pixman version requirement to 0.36.0.

Beyond this are a range of bugfixes and some work on establishing CI for
Cairo.

For a complete log of changes, please see

    https://cairographics.org/releases/ChangeLog.1.17.2

API Changes
-----------
None

Dependency Changes
------------------
pixman 0.36.0

---
## [ImSpiDy/kernel_xiaomi_lavender-4.19](https://github.com/ImSpiDy/kernel_xiaomi_lavender-4.19)@[fd091d61b5...](https://github.com/ImSpiDy/kernel_xiaomi_lavender-4.19/commit/fd091d61b589f68379d95c76114e0caedd8ee577)
#### Tuesday 2023-11-14 16:34:25 by Angelo G. Del Regno

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
5      	      20220479
2      	      20940223
1      	      21231290

Remember again that we're loading from a UFS card and that
we are loading ~1.1MB more out of a 20MB file.
If you're smart enough you surely know already about RAM and CPU
overhead of very high compression levels.

If you still disagree with what I just did, read this commit description
another 20 times, or more, until you understand it. :)))

Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>
Signed-off-by: ImSpiDy <SpiDy2713@gmail.com>

---
## [matrix-org/matrix-js-sdk](https://github.com/matrix-org/matrix-js-sdk)@[31f38550e3...](https://github.com/matrix-org/matrix-js-sdk/commit/31f38550e3fb0ed7312e52b896985477b22f01c3)
#### Tuesday 2023-11-14 17:09:58 by David Baker

Refactor & make base64 functions browser-safe

We had two identical sets of base64 functions in the js-sdk, both
using Buffer which isn't really available in the browser unless you're
using an old webpack (ie. what element-web uses). This PR:

 * Takes the crypto base64 file and moves it out of crypto (because
   we use base64 for much more than just crypto)
 * Makes them work in a browser without the Buffer global
 * Removes the other base64 functions
 * Changes everything to use the new common ones
 * Adds a comment explaining why the function is kinda ugly and how
   soul destroyingly awful the JS ecosystem is.
 * Runs the tests with both impls
 * Changes the test to not just test the decoder against the encoder
 * Adds explicit support & tests for (decoding) base64Url (I'll add an
   encode method later, no need for that to go in this PR too).

---
## [FalloutFalcon/Shiptest](https://github.com/FalloutFalcon/Shiptest)@[590e8cb752...](https://github.com/FalloutFalcon/Shiptest/commit/590e8cb752400295fe770c303cf5b65a0089fc97)
#### Tuesday 2023-11-14 17:12:25 by Imaginos16

Adds the Inkwell-class Supply Freighter (#2385)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->
## Wait, isn't there a freeze right now?
Correct, there is a ship freeze currently, but I have received
permission from @Apogee-dev to create the PR for this vessel, as it was
a ship I've been working on since at least early-to-mid August.

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/653635cc-b83d-44d8-a9e3-384ffbd9367b)

If any other maptainer would like to overrule Apogee, I'd be more than
happy to temporarily close the PR. Until then, here it is!
## About The Pull Request
Hello everyone! Mr. SolGov here again to add yet another ship to be
tested!

This PR adds a completely new vessel, that being the **Inkwell-class
Supply Freighter**, a ship known for its vast cargo space!

![2023-10-13 13 54
57](https://github.com/shiptest-ss13/Shiptest/assets/77556824/9a70d97e-ab17-45af-a690-e528574b95cb)

![2023-10-13 13 54
59](https://github.com/shiptest-ss13/Shiptest/assets/77556824/2d9d6d0a-85e2-4c46-9754-d49f15be0560)

With extra starter money, three sonnensöldners, and three miners,
players can enjoy completing bounties like no tomorrow, have drinks with
their crewmates in peace, and supply other SolGov vessels with much
needed equipment in less time than you can say "I ran out of ammo!"

Notable things in this ship include:
- Turrets (with IFF!)
- A bar!
- A full-blown cafeteria with a small kitchen and lounge!
- An office space for bureaucrats and scribes!
- Decently-sized quarters for the Logistics Deck Officer and Captain!
- A massive cargo bay with pre-existing supplies!
- A secret compartment for private storage!

And finally, as for jobs, there are:
- 1 Captain
- 1 Logistics Deck Officer
- 3 Sonnensöldneren
- 2 Space Engineers
- 3 Field Engineers
- 2 Bureaucrats
- 6 Scribes
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
More SolGov content is nice! Especially when it comes to ships, for a
faction that only has two existing at the moment, haha.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy
add: The Solarian Port Authority Has Now Permitted Inkwell-class Vessels
To Explore The Stars!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: spockye <79304582+spockye@users.noreply.github.com>

---
## [stephmilovic/kibana](https://github.com/stephmilovic/kibana)@[38ea8093aa...](https://github.com/stephmilovic/kibana/commit/38ea8093aa140e0da7ee021ed4a1e0f98b05368c)
#### Tuesday 2023-11-14 17:31:09 by Vitalii Dmyterko

[Security Solution][Detection Engine] improves new terms rule for multiple fields (#157413)

## Summary

As described in our README for new terms rule type:

> Runtime field supports only 100 emitted values. So for large arrays or
combination of values greater than 100, results may not be exhaustive.
This applies only to new terms with multiple fields.
  Following edge cases possible:
- false negatives (alert is not generated) if too many fields were
emitted and actual new values are not getting evaluated if it happened
in document in rule run window.
- false positives (wrong alert generated) if too many fields were
emitted in historical document and some old terms are not getting
evaluated against values in new documents.

To avoid this and deliver the better experience for our customers, this
PR is moving from current implementation(emitting aggregated values for
multiple new terms fields) towards using composite aggregation for each
page from phase 1, split in chunks by 500.
This allowed to be done due
[order](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations-bucket-composite-aggregation.html#_order)
of composite aggregation results

NOTE: implementation for a single new terms filed is the same, due to
performance reasons


### Performance measurements

Implementation | Shards | Docs per shard | Simultaneous Rule Executions
| Fields cardinality | Rule Execution Time Runtime field(current
implementation) | On week work
-- | -- | -- | -- | -- | -- | -- 
array of unique values length 10 |   |   |   |   |   |   
Terms 1 field | 10 | 900,000 | 1 | 100,000 | |   
Terms 2 fields | 10 | 900,000 | 1 | 100,000 | 30s  |  41s
Terms 3 fields | 10 | 900,000 | 1 | 100,000 | 40s | 56s

Implementation | Shards | Docs per shard | Simultaneous Rule Executions
| Fields cardinality | Rule Execution Time Runtime field(current
implementation) | On week work 1,000 per batch | On week work 500 per
batch
-- | -- | -- | -- | -- | -- | -- | --
Terms 2 fields | 10 | 9,000,000 | 1 | 100,000 | 19s | 41s | 35s 
Terms 3 fields | 10 | 9,000,000 | 1 | 100,000 | 21s | 52s| 47s 
CPU % | | | | | 400-450% |500-600% | 400-450%

I selected size of the chunk as 500, since it's a bit faster and less
load on CPU

### Considerations on parallel composite search requests in phase 2

When running composite search requests in parallel, noticed significant
CPU increase in Elasticsearch ~ 1,000% for 2 requests in parallel
against ~ 500% for single.
Where win in performance was not that big: ~ 35s for 2 in parallel, 43s
for a single request. I think, having only one request is the better
option to go, that will prevent unnecessary CPU usage

### Test cases
I've added several functional test cases, that ensures, no missing/false
positives alerts are occurring. Applied to the old implementation, they
would fail

### Retry on max_clause_count error
Because we create query, that can have few thousands clauses, it is
possible it may fail due to [the maximum number of allowed
clauses](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-settings.html)
I implemented retry that: If request fails with batch size of 500
(default value), we will try to reduce it in twice per each retried
request, up until 125. Per ES documentation, max_clause_count min value
is 1,000 - so with 125 we should be able execute query below
max_clause_count value

### Checklist

Delete any items that are not applicable to this PR.

- [x] [Unit or functional
tests](https://www.elastic.co/guide/en/kibana/master/development-tests.html)
were updated or added to match the most common scenarios

---------

Co-authored-by: kibanamachine <42973632+kibanamachine@users.noreply.github.com>

---
## [halohoang/TagTheGame](https://github.com/halohoang/TagTheGame)@[050cc639a7...](https://github.com/halohoang/TagTheGame/commit/050cc639a7bbd8d4820b52f1e3c8a42e835c4f12)
#### Tuesday 2023-11-14 17:34:33 by JMindbender

Ai-Tweaks, Implementation of interactable doors into test scene, BulletColliion Ignorance

- tweaked Enemy AI, they won't behave that clunky when running into another enemy anymore (still clunky but not that clunky)
- implemted interactable doors to my testscene they work
- created and implemented Interactable Door Consoles for opening, closing the elevator doors (Elevator Doors are actual a ChildObject of the interactable Console)
- improved interactable scipt in that way that now there is a 2. interactable type choosable in the inspector ('console') that references at least one (array) other objects that will be enabled or disabled on interaction with the console object
- implemented working logic for the enemy bullets to not collide with EnemyAI-Objects anymore, so for the enemies there is no friendly fire anymore
-

---
## [andrewbaptist/cockroach](https://github.com/andrewbaptist/cockroach)@[e174990dd5...](https://github.com/andrewbaptist/cockroach/commit/e174990dd5015a38b1e9bc6723f270dbe647c3a3)
#### Tuesday 2023-11-14 17:43:20 by craig[bot]

Merge #113809

113809: kvstreamer: add limit to how many eager batches are issued r=yuzefovich a=yuzefovich

**kvstreamer: add limit to how many eager batches are issued**

This commit fixes extremely suboptimal behavior of the streamer in the
InOrder mode in some cases. In particular, previously it was possible
for the buffered responses to consume most of the working budget, so the
streamer would degrade to processing all requests effectively one
BatchRequest with one Get / Scan at a time, significantly increasing the
latency. For example, the query added as a regression test that performs
30k Gets across 10 ranges would usually take on the order of 1.5s (which
is not great already since in the non-streamer path it takes 400ms), but
in the degenerate cases it could be on the order of 20-30s.

Similar behavior could occur in the OutOfOrder mode too where we would
issue more BatchRequests in which only one request could be satisfied
(although in OutOfOrder mode the problem is not as severe - we don't
buffer any results since we can always return them right away).

This problem is now fixed by imposing the limit on the budget's usage at
which point the streamer stops issuing "eager" requests. Namely, now,
when there is at least one request in flight, the streamer won't issue
anymore requests once `limit * eagerFraction` is exceeded. This
effectively reserves a portion of the budget for the "head-of-the-line"
batch.

The "eager fraction" is controlled by a session variable, separate for
each mode. The defaults of 0.5 for InOrder and 0.8 for OutOfOrder modes
were chosen after running TPCH queries and the query that inspired this
commit. These values bring the number of gRPC calls for the reproduction
query from 1.5k-2k range to below 200 and the query latency to be
reliably around 400ms.

I don't really see any significant downsides to this change - in the
worst case, we'd be utilizing less of the available memory budget which
is not that big of a deal, so I intend to backport this change. Also,
setting the eager fractions to large values (greater than 1.0 is
allowed) would disable this limiting behavior and revert to the previous
behavior if we need it.

Fixes: #113729.

Release note (bug fix): Previously, when executing queries with
index / lookup joins when the ordering needs to be maintained,
CockroachDB in some cases could get into a pathological behavior
which would lead to increased query latency, possibly by 1 or 2 orders
of magnitude. This bug was introduced in 22.2 and is now fixed.

**kvstreamer: increase default avg response multiple**

This commit increases the default value for
`sql.distsql.streamer.avg_response_size_multiple` cluster setting from
1.5 to 3.0. This setting controls the factor by which the current "avg
response size" estimate is multiplied and allows for TargetBytes
parameter to grow over time. In the reproduction query from the
previous commit it was determined that the growth might not be as quick
as desirable.

The effect of this change is as follows:
- if we have responses of varying sizes, then we're now likely to be more
effective since we'll end up issuing less BatchRequests
- if we have responses of similar sizes, then we might pre-reserve too
much budget upfront, so we'll end up with lower concurrency across
ranges.

Thus, we don't want to increase the multiple by too much; however,
keeping it at 1.5 can be quite suboptimal in some cases - 3.0 seems like
a decent middle ground. This number was chosen based on running TPCH
queries (both via InOrder and OutOfOrder modes of the streamer) and the
reproduction query. (For the latter this change reduces the number of
gRPC calls by a factor of 3 or so.)

Release note: None

Co-authored-by: Yahor Yuzefovich <yahor@cockroachlabs.com>

---
## [BelleNottelling/FOSSBilling](https://github.com/BelleNottelling/FOSSBilling)@[b3321a8dd3...](https://github.com/BelleNottelling/FOSSBilling/commit/b3321a8dd33dfbd084899709a37b7e3a5c626300)
#### Tuesday 2023-11-14 17:44:15 by Adam Daley

Update to Sentry v4 (#1780)

* Bump minimum PHP version to 8.1

* Missed these too

* Shit's broke and stupid as fuck

* Update SentryHelper.php

* Update package-lock.json

* I did the fixing

---------

Co-authored-by: Belle Aerni <belleaerni@gmail.com>

---
## [yogstation13/Yogstation](https://github.com/yogstation13/Yogstation)@[bc3374c7da...](https://github.com/yogstation13/Yogstation/commit/bc3374c7dacf3b2db39fe1c4dc36551d7ba82f79)
#### Tuesday 2023-11-14 18:07:53 by cowbot92

Even Further Heretic Adjustments: New minor things, Bug fixes, Heretic path adjustments and movement adjustments! (#20843)

* a whole lot of shit

yessir

* gun stuff

crazy

* haha

fuck guns

* my brain bursts

it hurts

* so much shit

im done

* fuck forgot this

god damn low memory mode

* removes backslashes

really linter

* oops

typos

---
## [Opentrons/opentrons](https://github.com/Opentrons/opentrons)@[30425f7a3b...](https://github.com/Opentrons/opentrons/commit/30425f7a3bd4a7ddb8ba9d3c14b05cdff13ccf34)
#### Tuesday 2023-11-14 18:22:45 by Seth Foster

feat(app): Update robots from USB flash drive (#13923)

* feat(app-shell-odd): watch for USB drives

The Flex operating system automatically mounts the filesystems of
well-formatted USB drives (FAT and ext4 and maybe ntfs but that's a bit
iffy) to /media when those USB drives are inserted on the robot. In
theory it will in fact do this for _any_ kind of media that presents a
filesystem interface.

To that end, add a node task that will use a node filesystem watch to
keep an eye on /media, and
- when something that looks like a USB drive (/media/sd\w\d+) appears,
notify via redux actions
   - then enumerate all the files on it and notify those via redux
   actions
- when something we were keeping an eye on disappears, notify via
redux actions

The redux actions don't alter state and so don't need new reducers or
selectors; they exist because it's a handy mechanism to talk between our
components.

This code is very tightly coupled to the way the node fs interfaces work
and so I don't see a lot of point in unit tests for it; it's almost
entirely fs calls originating everything and providing all of the data,
and all the complexity is from working around weirdnesses in those calls
and in the underlying system. For instance,
- There's a little bit of time in between when the fs watch on /media
fires and when you can actually find the contents of the newly-present
directory; if you readdir before that you'll get an empty list, so we
wait a second
- The node fs.watch interface looks very fully features but is
absolutely chock-full of warnings about various features not being
reliable. A lot of that unreliability is _probably_ across systems and
everything works as we expect on linux, but just in case we have a lot
of fallbacks for if our callback doesn't get filepaths, etc

* fix(app-shell-odd): handle errors in readstreams in http.post

We have our custom http interface that wraps around node-fetch that
provides things like "doing your own read stream when posting a file",
and "mapping everything into the promise interface", which is nice,
but has an issue specifically for that read stream: we don't monitor
errors on it. Read streams surface errors by emitting an 'error' event;
we hook up a listener to that error event _while we're creating the
stream_, but then we disconnect it. So if you have an error in the
stream - for instance, you're reading from a file on a USB flash drive
and the user unplugs the flash drive - then the error will never get
surfaced.

Unfortunately the fix to this is a bit fiddly. We can hook up an error
listener fine, but it needs to do something; specifically, it needs to
turn the error from a callback into a promise rejection. That means it
needs to have a promise to reject that has the same lifetime as the
stream itself. http.post didn't provide that because it returns a whole
big promise chain, and each time you move a link in that chain the old
promise is gone and a new one happens, so we'd need to move the listener
around.

Since promises are monadic, a better fix is to have post return a single
promise and do all the promise chaining _inside_ that promise; then, the
read stream error handler can reject the outer promise directly, while
relying on promises bubbling up rejections to preserve error handling
capability for the promises in the internal chain.

* fix(app): Poll for updates on the ODD

Though we have everything set up to automatically fetch, prompt for, and
execute robot updates from the ODD, we weren't actually _checking_ for
those updates except once on boot (which then wouldn't work if the robot
wasn't internet-connected during boot). This means in particular that
the software updates during onboarding were guaranteed to fail.

We can use the same hook in the ODD app root that we do in the desktop
app route, but if we're going to do that then we better remove a log
message that suddenly becomes extremely spammy.

* feat(app-shell-odd): Supply "system updates" from flash drives

Adds the capability to provide system updates from flash drives to the
ODD app-shell.

These are "system updates" in that the app-shell determines their
availability and provides it to the app, rather than the user indicating
the presence of a file alongside their intent to update. The app-shell
will advertise the flash drive updates in the same way it advertises
internet-discovered updates, with a RobotUpdateInfo redux message; since
those now provide the path to the file they mean, it will be easy for
the app to specify the system update to load.

We can duplicate the logic that we use for system updates by adding a
second let cache for the "current update"; the system-updates code will
then prefer an update in the mass storage update cache to an update in
the old system updates cache, and send new robot update info messages in
all the state changes between neither cache being full; either cache
being full; and both caches being full.

The determination that a flash drive system update is present is
triggered by a mass storage enumerated message; when that flash drive
gets removed, we'll get a removal message.

To figure out whether updates are actually present, we can the list of
files that just got enumerated for things that end with .zip, and then
try to open them as zip files and read the VERSION.json information out
of them. This is a somewhat fraught process; the file could not be a zip
file, it could be a zip file but corrupted, it could be a zip file but
not an update, it could be an update but it's for an OT-2,  and we need
to handle all that, so there's a pretty excessive amount of error
handling in here. Once we're sure that there are one or more zip files
containing robot system updates, we can provide something to redux; we
provide the highest-version update present.

There is one way in which updates from flash drives differ from system
updates found on the internet, however: plugging in a flash drive
requires user intent, while checking for updates on the internet
doesn't. Therefore, if the user plugs in a flash drive with an update
file, we always want to make that update file available no matter the
relative versions of the robot and the update file. So we can add a bool
to the system update message (and then to the update state) that shows
that this is a "forced notification" update, and the app can know to
display it without caring about the upgrade/downgrade/reinstall state.

Since there's a lot of duplication, we can also factor out some common
logic to make it feel a little better.

That process of duplication also fixes a bug that would have prevented
the ODD from ever prompting for updates. The function that gets
information about updates used the same promise to read the release
notes and provide the update information; but we overrode the downloaded
release files to null out the release notes, meaning that promise would
always fail, and we'd never get the notification. We no longer override
the release notes to be null, and we also treat reading the release
notes separately from reading the rest of the update.

* feat(app): allow robot updates from USB files

Now that the odd app-shell provides us with notifications of updates
from USB flash drives, we can allow the user to install them. While the
redux mechanisms allow this pretty easily - a system update is a system
update, after all, and with the force mechanism the app wouldn't even
know if the update was a downgrade or anything - we ran into a problem
where the general robot update machinery in the ODD was very tightly
bound with the onboarding experience for the ODD, since that's the
context in which it was developed.

This commit extracts the robot update mechanisms from onboarding by
- Hoisting onboarding-related logic out of lower level components and
instead injecting that logic into the organisms code from the top level
page
- Moving the current update page to a new one that is focused on
onboarding at a new route, and copying just the update-related code to
a generic RobotUpdate page

This means that the two pages - RobotUpdate and
RobotUpdateDuringOnboarding - share most of the same code but are bound
to different routes and can have different top level behavior by
injecting different contexts to the finish and error handling behaviors
of the update. RobotUpdateDuringOnboarding sets the unfinished
onboarding page breadcrumbs appropriately, and uses display language
appropriate to the update being just a component of the larger workflow,
and moves on to estop handling when cancelled; RobotUpdate doesn't touch
any of that, and goes back to the settings page when cancelled, and uses
wording more appropriate to being its own topline flow.

Closes RAUT-829

---
## [yarnpkg/berry](https://github.com/yarnpkg/berry)@[6256fdd734...](https://github.com/yarnpkg/berry/commit/6256fdd7345429dcccbe356184ad291e90047ec3)
#### Tuesday 2023-11-14 18:32:47 by Maël Nison

Adds support for running native binaries without JS intermediaries (#5508)

**What's the problem this PR addresses?**

Yarn currently cannot run native binaries without going through a JS
jumper script. Other package managers don't have this restriction, and
it makes the `yarn run` overhead worse on some scripts for little
reasons - or doesn't work at all when packages don't use jumper scripts.

**How did you fix it?**

Two mechanisms are used:

- First we check for the binary extension
- Then we check its magic number

If one of the two match a predetermined list, the binary is spawned
without going through Node. This ensures that this logic is called only
when the binary is truly a native binary, and will not affect the
behaviour of other existing scripts.

**Checklist**
<!--- Don't worry if you miss something, chores are automatically
tested. -->
<!--- This checklist exists to help you remember doing the chores when
you submit a PR. -->
<!--- Put an `x` in all the boxes that apply. -->
- [x] I have read the [Contributing
Guide](https://yarnpkg.com/advanced/contributing).

<!-- See
https://yarnpkg.com/advanced/contributing#preparing-your-pr-to-be-released
for more details. -->
<!-- Check with `yarn version check` and fix with `yarn version check
-i` -->
- [x] I have set the packages that need to be released for my changes to
be effective.

<!-- The "Testing chores" workflow validates that your PR follows our
guidelines. -->
<!-- If it doesn't pass, click on it to see details as to what your PR
might be missing. -->
- [x] I will check that all automated PR checks pass before the PR gets
reviewed.

---
## [ioccc-src/temp-test-ioccc](https://github.com/ioccc-src/temp-test-ioccc)@[2e5782f930...](https://github.com/ioccc-src/temp-test-ioccc/commit/2e5782f930a8b6652cd02c8c9ab5de399d112076)
#### Tuesday 2023-11-14 18:40:37 by Cody Boone Ferguson

Improve 1996/huffman/try.sh

Get CC, defaulting to cc.

   So, that's to end the story for you and me
   If you still give a listen, you just may
   Hear a big wolf-man or little piggy say
   Little pig, little pig, let me in
   Not by the hair of my chinny, chin, chin
   Little pig, little pig, let me in
   Not by the hair of my chinny, chin, chin
   Well, I'm huffin', I'm puffin', I'll blow your house in
   Huffin', puffin', blow your house in
   Huffin', puffin', blow your house in
   Huffin' and a puffin' and I'll blow your house in!
   And the moral of the story is
   band with no talent can easily amuse
   Idiots with a stupid, puppet show

:-)

---
## [PhenolLully/group-project1](https://github.com/PhenolLully/group-project1)@[dbc8725a3a...](https://github.com/PhenolLully/group-project1/commit/dbc8725a3a357def4e398597ff01bd5927780c50)
#### Tuesday 2023-11-14 19:07:44 by Bdubs

added response.statusText to the error handler so when troubleshooting we know exactly what the status code is, removed the event handlers which showed alerts,removed the both joke function as it was preventing new jokes from displaying on click, created a new function which adds the joke in based on thier respective apis and updated our jquery method.

---
## [ImSpiDy/kernel_xiaomi_lavender-4.19](https://github.com/ImSpiDy/kernel_xiaomi_lavender-4.19)@[9189993765...](https://github.com/ImSpiDy/kernel_xiaomi_lavender-4.19/commit/918999376540c1068a6feb94943f75361dc15933)
#### Tuesday 2023-11-14 19:41:38 by Dan Pasanen

power: don't ever reboot to verity red

* We get it, shit's broken. We're flashing custom stuff, shit's bound
  to break. Don't pop this annoying screen up, we're not even using
  verity anyway.

Change-Id: Icd77b70ec1df9108a4ba9e7fd8cb9623b35b78db
Signed-off-by: celtare21 <celtare21@gmail.com>
Signed-off-by: sohamxda7 <sensoham135@gmail.com>
Signed-off-by: Oktapra Amtono <oktapra.amtono@gmail.com>
Signed-off-by: clarencelol <clarencekuiek@icloud.com>
Signed-off-by: pix106 <sbordenave@gmail.com>
Signed-off-by: ImSpiDy <SpiDy2713@gmail.com>

---
## [Kiara-Miller/cmss13](https://github.com/Kiara-Miller/cmss13)@[3e9d54628d...](https://github.com/Kiara-Miller/cmss13/commit/3e9d54628d68fe91319ae87ad7ebd7aef9500811)
#### Tuesday 2023-11-14 20:04:41 by Ben

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
## [oxidecomputer/omicron](https://github.com/oxidecomputer/omicron)@[2fc0dfd8c1...](https://github.com/oxidecomputer/omicron/commit/2fc0dfd8c11f31e66cfaf8ee80586bb2ed607216)
#### Tuesday 2023-11-14 20:08:20 by Andrew J. Stone

Extract storage manager related code from sled-agent (#4332)

This is a large PR. The changes are in many ways *just* moving code
around,
and at a cursory glance may appear to be a giant waste of time. To
justify
these changes and my rationale I will first present the goals I believe
we
should strive to meet in general sled-agent development. I'll then go
into
how I believe these goals can be realized via code patterns. I'll then
discuss
the concrete changes in this PR and how they implement the discussed
patterns.
Lastly, I'll list a few open questions about the implementation in the
PR.

I want to emphasize that a lot of what I talk about below is already
done in
sled-agent, at least part way. We can pick the best patterns already in
use and
standardize on them to build a more coherent and yet decoupled
architecture for
easier testing and understanding.

# Goals

This PR is an attempt to start making sled-agent easier to maintain. In
order to
make things easier to maintain, I believe we should attempt to realize a
few key
goals:

1. Initial startup and control code should read linearly. You shouldn't
have to
jump around to follow the gist of what's going on.
2. Tasks, like functions, should live at a certain abstraction level. It
must be clear
 what state the task is managing and how it gets mutated.
3. A developer must be able to come into the codebase and know where a
given
functionality should live and be able to clearly follow existing
patterns such
that their new code doesn't break or cross abstractions that make
following the
code harder in the future.
4. Tests for individual abstractions and task driven code should be easy
to
write. You shouldn't need to spin up the whole sled-agent in order to
test an
algorithm or behavior.
 5. Hardware should be abstracted out, and much of the code shouldn't 
 deal with hardware directly.

# Patterns

## Task/Handle

In my opinion, the most important pattern to follow for async rust
software
is what I call the "task/handle" pattern. This pattern helps code
maintenance
by explicitly managing state and making task driven code easier to test.
All
tasks that provide services to other tasks should follow this pattern.
In this
pattern, all state is contained in a type owned by the task and
inaccessible
directly to other tasks. The task has a corresponding handle which must
be
`Send` and `Clone`, and can be used to make requests of the task. The
handle
interacts with the task solely via message passing. Mutexes are never
used.

A few things fall directly out of this pattern:

* Code that manipulates state inside and outside the task can be
synchronous
* We don't have to worry about mutex behavior with regards to
cancellation,
   await points, etc...
 * Testing becomes easier:
   * We can test a bunch of the code without spawning a task in many
cases. We just [directly construct the state object and call
functions](https://github.com/oxidecomputer/omicron/pull/4332/files#diff-08315639e20a9323f2740455a7813d83ca43b05dca197ebbda66c13f750d446bR634-R656),
     whether sync or async.
   * When testing sequential operations that are fire and forget,
we [know when they have been processed by the task
loop](https://github.com/oxidecomputer/omicron/pull/4332/files#diff-08315639e20a9323f2740455a7813d83ca43b05dca197ebbda66c13f750d446bR702-R709),
     because our next request will only run after those operations. 
This is a direct result of the fifo channel between handle and task.
This is not possible with state shared outside the task via a mutex.
     We must poll that mutex protected state until it either changes to
     the value we expect or we get a timeout. If we expect no change, we
     must use a side-channel.
   * We can write complex state handling algorithms, such as those in 
      maghemite or bootstore, in a deterministic, synchronous style that
allows property based testing and model checking in as straightforward
     a manner as possible.
* We can completely [fake the
task](https://github.com/oxidecomputer/omicron/pull/4332/files#diff-08315639e20a9323f2740455a7813d83ca43b05dca197ebbda66c13f750d446bR163-R223)
without changing any of the calling code except the constructor. The
real
handle can instead send messages to a fake task. Importantly, this
strategy
can also be used to abstract out hardware for unit tests and simulation.

Beyond all that though, the understanding of how state is mutated and
accessed
is clear. State is only mutated inside the task, and can only be
retrieved from
code that has a copy of the handle. There is no need for separate
`_locked`
methods, and no need to worry about order of locking for different bits
of task
state. This can make the task code itself much shorter and easier to
read as
demonstrated by the new `StorageManager` code in `sled_storage`. We can
also
maintain internal stats for the task, and all of this can be retrieved
from the
handle for reporting in `omdb`.

There is one common question/problem with this pattern. How do you
choose a
bounded channel size for handle to task messages?

This can be tricky, but in general, you want the channel to *act*
unbounded,
such that sends never fail. This makes the channels reliable, such that
we never
drop messages inside the process, and the caller doesn't have to choose
what to
do when overloaded. This simplifies things drastically for developers.
However,
you also don't want to make the channel actually unbounded, because that
can
lead to run-away memory growth and pathological behaviors, such that
requests
get slower over time until the system crashes.

After discussions with @jgallagher and reflections from @sunshowers and
@davepacheco on RFD 400, the solution is to choose a large enough bound
such that we should never hit it in practice unless we are truly
overloaded.
If we hit the bound it means that beyond that requests will start to
build
up and we will eventually topple over. So when we hit this bound, we
just
[go ahead and
panic](https://github.com/oxidecomputer/omicron/pull/4332/files#diff-08315639e20a9323f2740455a7813d83ca43b05dca197ebbda66c13f750d446bR75-R77).

Picking a channel bound is hard to do empirically, but practically, if
requests are
mostly mutating task local state, a bound of 1024 or even 8192 should be
plenty.
Tasks that must perform longer running ops can spawn helper tasks as
necessary
or include their own handles for replies rather than synchronously
waiting. Memory
for the queue can be kept small with boxing of large messages.

It should also be noted that mutexes also have queues that can build up
and
cause pathological slowness. The difference is that these queues are
implicit
and hard to track.

## Isolate subsystems via the message driven decoupling

We have a bunch of managers (`HardwareManager`, `StorageManager`,
`ServiceManager`, `InstanceManager`) that interact with each other to
provide sled-agent services. However, much of that interaction is ad-
hoc with state shared between tasks via an `Inner` struct protected
by a mutex. It's hard to isolate each of these managers and test
them independently. By ensuring their API is well defined via a
`Handle`,
we can fake out different managers as needed for independent testing.
However, we can go even farther, without the need for dependency
injection
by having different managers announce their updates via [broadcast or
watch

channels](https://github.com/oxidecomputer/omicron/pull/4332/files#diff-08315639e20a9323f2740455a7813d83ca43b05dca197ebbda66c13f750d446bR129-R133).

With this strategy, we can drive tests for a task by using the handle to
both
trigger operations, and then wait for the outflow of messages that
should occur
rather than mocking out the handle API of another task directly and
checking
the interaction via the fake. This is especially useful for lower level
services
that others depend upon such as `StorageManager`, and we should do this
when we
can, rather than having tasks talk directly to each other. This strategy
leads
directly to the last pattern I really want to mention, the `monitor`
pattern.

## High level interaction via monitors

Remember that a primary goal of these patterns is to make the sled-agent
easier
to read and discover what is happening at any given point in time. This
has to
happen with the inherent concurrency of all the separate behaviors
occurring
in the sled-agent such as monitoring for hardware and faults, or
handling user
requests from Nexus. If our low level managers announce updates via
channels
we can have high level `Monitors` that wait for those updates and then
dispatch
them to other subsystems or across clients to other sleds or services.
This
helps further decouple services for easier testing, and also allows us
to
understand all the asynchrony in the system in fewer spots. We can put
RAS code
in these monitors and use them as central points to maintain stats and
track the
overall load on the system.

# The punchline

How do the patterns above satisfy the goals? By decoupling tasks and
interacting
solely via message passing we make testing easier(goal 4). By separating
out
managers/ services into separate tasks and maintaining state locally we
satisfy
goals 2 and 5. By making the tasks clear in their responsibilities, and
their
APIs evident via their handles, we help satisfy goal 3. Goal 3 is also
satisfied
to a degree by the elimination of sharing state and the decoupling via
monitors.
Lastly, by combining all the patterns, we can spawn all our top level
tasks and
monitors in one place after initializing any global state. This allows
the code
to flow linearly.

Importantly, it's also easy to violate goal 3 by dropping some mutexes
into the
middle of a task and oversharing handles between subsystems. I believe
we can
prevent this, and also make testing and APIs clearer, by separating
subsystems
into their own rust packages and then adding monitors for them in the
sled-agent.
I took a first cut at this with the `StorageManager`, as that was the
subsystem I was
most familiar with.

# Concrete Code changes

Keeping in line with my stated goals and patterns, I abstracted the
storage
manager code into its own package called `sled-storage`. The
`StorageManager`
uses the `task/handle` pattern, and there is a monitor for it in
sled-agent
that takes notifications and updates nexus and the zone bundler. There
are also a
bunch of unit tests where none existed before. The bulk of the rest of
the code
changes fell out of this. In particular, now that we have a separate
`sled-storage`
package, all high level disk management code lives there. Construction
and
formatting of partitions still happens in `sled-hardware`, but anything
above the
zpool level occurs in `sled-storage`. This allows testing of real
storage code on
any illumos based system using file backed zpools. Importantly, the
key-management
code now lives at this abstraction level, rather than in
`sled-hardware`, which
makes more sense since encryption only operates on datasets in ZFS.

I'd like to do similar things to the other managers, and think that's a
good way
to continue cleaning up sled-agent.

The other large change in this code base is simplifying the startup of
the bootstrap agent such that all tasks that run for the lifetime of
the sled-agent process are spawned in `long_running_tasks`. There is a
struct called `LongRunningTaskHandles` that allows interaction with all
the
"managers" spawned here. This change also has the side effect of
removing the
`wait_while_handling_hardware_updates` concurrent future code, since we
have
a hardware monitor now running at the beginning of time and can never
miss
updates. This also has the effect of negating the need to start a
separate
hardware manager when the sled-agent starts up. Because we now know
which
tasks are long running, we don't have to save their tokio `JoinHandle`s
to display
ownership and thus gain clonability.

# Open Questions

* I'm not really a fan of the name `long_running_task_handles`. Is there
a better
name for these?
* Instead of calling `spawn_all_longrunning_tasks` should we just call
the
individual spawn functions directly in `bootstrap/pre_server`? Doing it
this
way would allow the `ServiceManager` to also live in the long running
handles
and remove some ordering issues. For instance, we wait for the bootdisk
inside
`spawn_all_longrunning_tasks` and we also upsert synthetic disks.
Neither
of these is really part of spawning tasks.

---
## [Bjarl/Shiptest](https://github.com/Bjarl/Shiptest)@[2fc01ad8be...](https://github.com/Bjarl/Shiptest/commit/2fc01ad8be958492a38b3200023b8aa0c4bad9f5)
#### Tuesday 2023-11-14 20:25:36 by Skrem_7

Skrem's Quick Ballistic Glanceover (#2354)

## About The Pull Request

If maintainers want me to shorten the changelog, I can, I tend to start
there so I know what to talk about up here.

What started as a PR meant to buff up rubber rounds ended up turning
into a general passover I gave to much of the syntax and presentation of
ballistics. PR doesn't actually change that much function-wise, but it
changes a lot of lines due to a lot of changed pathing to better
establish consistency within ballistic code as well as overviewing a lot
of descriptions, names, and inherit moments.

Functionally, less-lethals and sniper rounds have been changed the most
by this PR. To a lesser extent, .38 special and shotgun rounds have been
tweaked. Finally, the PR stamps out a missing sprite bug with the WT-550
magazines, buffs up the surplus rifle (yeah, that old thing), tinkers
with some projectile speeds, makes match rounds slightly better, and
goes over A LOT of descriptions. I apologize for the massive wall of
text that's to follow.

Will take a look at energy weapons when I feel like it (might kill
disablers, I don't like mapping though).

## Why It's Good For The Game

### Slug and Pellet Changes
The pellet changes are actually just systemizing what was supposed to be
intentional design according to code comments, it just hadn't reached
every single pellet-based shotgun projectile. The improvised shell buff
is to make it not a potential complete whiff because RNG mechanics are
generally bad and not fun to play with.

### Less-Lethal Changes
Several implementations of less-lethal (rubber) ammunition on shiptest
are strictly worse than their standard alternatives. While this isn't a
PvP server, it feels very not-fun meta-wise to POTENTIALLY arm for SOME
insubordination and still fire what may as well be a round that bleeds
someone out (as they'll cause bleeding anyway). Increasing the stamina
damage on each of these makes it so they actually have a vague trade-off
(maybe stamina damage can do something like slow simplemobs in the
future, I don't know, I'd love to do it but simplemob code makes me
screech).

To make them not directly better in PvP and not the staple of taking
down the Super Scary Syndicate Shocktrooper Guy, they've had their
negative AP doubled. Not as good against combatants, but still perfectly
adept, if not better at general riot control against civilians. Makes
sense and puts them in their niche a little better.

### .38 Changes
The .38 special round relatively has more "power" and "velocity"
compared to the 9mm round, though it does not quite reach the levels
that .45 automatic or 10mm does in the IRL server. Furthermore, .38
special was specifically designed not to over-penetrate targets so as to
minimize the chance of collateral damage in police work. These are the
ultimate justifications behind giving it the worst AP out of all the
pistol calibers (-30, instead of -20) while still raising its damage to
25.

This should make the Winchester a better staple for taking out weaker
enemies such as legions or unarmored hermits, but it'll perform worse
against goliaths, frontiersmen, and the like. All-in-all, a more
"early-game" caliber, if you will, which is kinda what it's always been.

### Projectile Speed and Match Changes
Match rounds don't really exist as far as I've seen. That being said,
they're meant to be of higher quality, so their getting slightly higher
AP and speed makes sense, even if they're mostly just a meme round.

The speed increase of DMR/sniper rounds is primarily meant to
differentiate them better from AR rounds beyond having 20 more AP.
Assault rifles so far have pretty much dominated with better magazine
size, fire rate, and the exact same force as the DMR calibers, just
doing less damage against armored targets (doesn't matter too much when
you can just vomit rounds). I'd like to buff up the DMR damage even more
(sniper is fine), but I'd rather get some feedback on changing them to
35 baseline before doing so.

The speed decrease on shotguns is meant to cement them as CQC weapons.
Slugs are heavy. Shotguns are meant for close range. It's not much, but
it's thematically a good way to keep them in their lane, not that
they're even that problematic, hence only the slight change.

### Sniper Rifle Knockdown Change
Having a big-ass bullet that does 70 damage with 50 AP hit you is
already a middle finger. Making it potentially knock off an arm or a leg
is another middle finger. Being hardstunned for ten seconds after is the
icing on the cake. Changed it to a knockdown because we hate ranged
tasers.

### Surplus Rifle Fire Rate Buff
This thing is a joke. I haven't even seen it on the server, but I'd
rather make it vaguely competitive considering 10mm isn't super deadly
and only otherwise exists on the stechkin or the one Inteq SMG that you
never see (Colossus-only).

It's still clunky and terrible, but it should be less comedic and more
of a potential option if you have NOTHING else (will never happen).

### Boarder Magazine Change
Top-loading magazine fits into a standard assault rifle? No. Doesn't
make sense. Someone should probably just kill this gun, it's stupid and
looks stupid last I checked.

### WT-550 Magazine Fix
Don't think I've seen anyone use this weapon, I've only printed out
their magazines to dump AP rounds into my NT-SVG carbine. Noticed they
were invisible then. Someone increased their capacity to 30 without a
care for how its update_icon works. Not cool. Anyway, fixes are good.
Moving on.

### Syntax, Description, Spelling, and Overall Presentation Changes
Something very important when maintaining code is generally keeping
consistency in how things are not only presented, but how they're stored
as well. While I'd love to do EVEN more in the method of refactoring to
better align how so much of gun code works, this was something I wanted
to keep as a one-day project, so I mostly tinkered with pathing,
inherits, and groupings.

In the avenue of spelling and description changes, that's just 1)
Cleaning up errors that PR authors and maintainers missed and 2) Making
things more concise and just... better. Some of the SolGov descriptions
were a real headache to look at, and not because of the frequent
spelling and syntax errors.

Whoever misspelled and caused an entire series of items to be
/obj/item/gun/ballistic/automatic/assualt may wish to avoid any crows
for the next three months.

Perfectly willing to adjust or reel back some of my descriptions if
someone can offer something better than what I've written out if there's
some soul they REALLY want to keep.

## Changelog

:cl:
tweak: The NT 'Boarder' ARG now loads standard P-16 magazines, rather
than the M-90gl toploaders.
balance: .38 special does 25 damage up from 20. AP has been reduced to
-30 from -20.
balance: Standardizes pellet projectiles to lose 10% damage of both
types per tile across the board. Improvised pellets no longer have a
hardcapped 1-8 tile range.
balance: Less-lethal rounds now do 50% more stamina than the force of
their lethal counterparts, with 25% the normal force and double the
negative AP. If the round had positive or zero AP, it was subtracted by
20.
balance: Shotgun slugs do 40 damage, down from 60, but have zero AP,
rather than -10. FRAG-12 and meteor slugs have had their damage adjusted
to reflect their relative force.
balance: Surplus rifle fire_delay has been cut to 1 second from 3.
balance: .50 BMG knocks down instead of hardstunning.
balance: Any DMR, match, or sniper round now travels slightly faster
than other bullets. Shotgun slugs and pellets now travel slightly slower
than other bullets.
balance: Match rounds have had their AP slightly increased.
fix: Fixed WT-550 magazines not displaying properly.
spellcheck: Went over (almost) every single ballistic description,
including the guns themselves, magazines, ballistic casings, and speed
loaders/stripper clips to not only have better consistency and
readability, but also be more clear on the general effectiveness of each
caliber.
spellcheck: Assualt is gone.
code: Repaths/renames most ballistic ammo pathing to maintain
consistency or take advantage of inherits, when possible.
/:cl:

---
## [spockye/Shiptest](https://github.com/spockye/Shiptest)@[2a74c23d62...](https://github.com/spockye/Shiptest/commit/2a74c23d62916ddb6b1fdfab8c969b7702299067)
#### Tuesday 2023-11-14 20:25:52 by Imaginos16

Nerfs the everloving almighty shit out of the jungle demonic office ruin (#2430)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Nerfs the ruin by removing most of its gamer gear, and changing the
syndicate hardsuit you find into a scarlet hardsuit.


Not to mention the two goddamn deathsquad hardsuits all there,
wholesale, for free.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/a8333190-37ce-441f-a746-bb5f2fc26828)

This shit is not okay jesus fucking christ, two deathsquad hardsuits?
Are you insane?
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy
balance: The Jungle Demonic Office Ruin has now been appropriately
balanced, now only having a scarlet hardsuit, decent syndicate armor,
and a bulldog with no spare mags.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [spockye/Shiptest](https://github.com/spockye/Shiptest)@[bf4671ff83...](https://github.com/spockye/Shiptest/commit/bf4671ff83e2cb937a019f7f0515e6f23c32f493)
#### Tuesday 2023-11-14 20:25:52 by retlaw34

Gun rework (#1601)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
WIP.

if it wasn't obvious, very based off tgmc 

this reworks how guns work, by making them 4x more lethal without
touching a single damage value

its a bit difficult to put into words what this does, so i think these 3
gunfights i did with a good friend explains it better than i ever could

https://streamable.com/09in19
https://streamable.com/yel56o
https://streamable.com/x2a0he

if you didnt watch these videos:
- New guns sounds, TGMC as usual. but some racking sounds are from CEV
eris
- guns now can be wielded, if unwielded, they may cause recoil which not
only makes your shots less accurate, but 'scrolls' your screen
- new suppression effects
- getting hit hard enough scrolls your screen
- anything getting hit shakes you as feedback, not just bullets
- bullets can ricochet naturally upon hitting a surface at a step angle.
does not auto aim at your target, so be careful. ricochet sfx taken from
CEV eris
- new effects for bullet impacts. sound effects were taken from TGMC and
https://github.com/Skyrat-SS13/Skyrat-tg/pull/11697
- adds the cattleman revolver and Himehabu 22lr pistol. sprites by yours
truely

big problem is, in order for all of this to work, a certain key needs to
be binded to rack the gun. by default this is SPACE, but moost already
have it binded to 'hold throw mode', which is an issue. for one, not
only you need to ask everyone to rebind their controls to a very
important key, but also a key dedicated to just racking the gun can
cause issues. im up for any solutions

- [x] I affirm that I have tested all of my proposed changes and that
any issues found during tested have been addressed.

## Why It's Good For The Game

people dont fear gunfights. they think its just a way to pvp. people
should be afraid of gunfights, feel the pain OOCly when their blorbo
gets hit

## Changelog

:cl:
add: 22lr and cattleman revolver
add: many gun sounds
balance: guns reworked
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: retlaw34 <bruhasdfasdfasdf@waifu.club>

---
## [Odilf/chessagon](https://github.com/Odilf/chessagon)@[78cd33b872...](https://github.com/Odilf/chessagon/commit/78cd33b87204cef4436dbbb292abfeca49008e12)
#### Tuesday 2023-11-14 20:37:35 by Odilf

rolled back the fucking date fucking bullshit piece of shit

---
## [Tunguso4ka/CM-14](https://github.com/Tunguso4ka/CM-14)@[6f831b34cd...](https://github.com/Tunguso4ka/CM-14/commit/6f831b34cd4d0085be7433a188e97d4117574c72)
#### Tuesday 2023-11-14 20:55:35 by Tunguso4ka

fuck you swap file and i found where are job icons are

---
## [MrMelbert/tgstation](https://github.com/MrMelbert/tgstation)@[1a62886a8b...](https://github.com/MrMelbert/tgstation/commit/1a62886a8b83afe5b827947051b9d85ac2ed1a8a)
#### Tuesday 2023-11-14 21:01:18 by san7890

Fixes Shaving Beards + Mirror Code Improvement (#79529)

## About The Pull Request

Fixes #79519

Basically we did a lot of assumptions that we really shouldn't do in the
whole magical mirror framework (like having a boolean value for magical
mirrors, what?). Anyways, I just made the UX experience a lot better
when it came to bearded persons with feminine physiques to easily shave
off their beard with an additional confirmatory prompt + details as well
as keeping the nature of the magical mirror (giving you a swagadocious
beard due to magic:tm:) intact.
## Why It's Good For The Game

There was a lot of convoluted code that skipped through the quality
filter checks (it was me i think) so let's both make the code far easier
to grasp as well as ensure that people who legitimately acquire beards
and wish to keep them, keep them.

We were also doing some FUCK shit on attack_hand and the like
(overriding a FALSE return signal to return TRUE is not what we should
be doing there)- so that's also cleaned up.
## Changelog
:cl:
fix: Both magic mirrors and regular mirrors are far better at respecting
the choice of the beard you wish to wear (within reason, of course).
/:cl:

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[bed92e193c...](https://github.com/tgstation/tgstation/commit/bed92e193ce4a79824fd4fd30a900245dca870ae)
#### Tuesday 2023-11-14 21:28:01 by san7890

Further Prevention of Disposals Qdeletion (#79714)

## About The Pull Request

Fixes the consequences of #79629 - Verdict is still out on what the root
issue is

This has been an issue for the last two years and everything I go
bananas trying to get a consistent reproduction case to figure out the
root issue. After three session of picking, I think it's just a
consequence of certain thing in disposals code sleeping due to
`addtimer()` and whatnot so I'm just throwing in the towel and just
making it so we stop sending atoms to nullspace for no reason.

`target_turf` is typically always a present arg, but regardless we are
guaranteed to get a valid turf to send people to instead of the deleted
mob room. We still `stack_trace()` whenever this happens, so tracking
this issue doesn't change any more than the present status quo- we just
don't keep torturing mobs by sending them to the shadow realm.
## Why It's Good For The Game

One day we'll figure out why we keep getting `null` passed into
`forceMove()` like this but today is not that day. i know turfs
technically can't be deleted but it's just there as a safety since we
nullcheck anyways (which is the whole point of this fix). Let's just
stop screwing with players for the time being

also the code looks much better
## Changelog
:cl:
fix: Safeties in the code have been added to prevent things in disposals
going into nullspace whenever they get ejected from a pipe - you will
just magically spawn at the turf that you were meant to be flung
towards.
/:cl:

---
## [Janoti1/Vermintide2_Mods](https://github.com/Janoti1/Vermintide2_Mods)@[2b8d0d5755...](https://github.com/Janoti1/Vermintide2_Mods/commit/2b8d0d5755d72c071bd16ede487344b18d348259)
#### Tuesday 2023-11-14 21:36:44 by Janoti!

v2.0 Added many Options

Changelog v2.0:
- Rebranded The Mod from "Geheimnisnacht+" to "Geheimnisnacht Unlimited"
- Changed Thumbnail
- Changed the locations of the Ritual sites to the position that fatshark used in the event.
(Maps affected: Festering Ground, Khazukan Kazakit-ha!, War Camp, Tower of Treachery, Blood in the Darkness)
- Added multiple new options in the mod menu:
	- You can Choose to pick the event in the version it used to in 2021 and 2022 or in 2023
	- You can toggle the Night mode (Helloween Image Filter) seperately
	- You can change the eye color of enemies without having to play the deed/ picking up the skull
	- Added another Event modifier "Skulls for the Skull Throne"
	- Removed various chat prompts to less spam the chat

Notes:
	- ALL party members need to have this mod installed
	- The Hosts settings will override the clients ones
	- Removes the pickup ban on skulls in tourney balance (You can play the Skull Mutator with Tourney Balance Enabled)
	- Added Texture for Eye Deed
	- The Eye Deed is purely cosmetic and doesnt change enemy behaviour

---
## [KenAdeniji/WordEngineering](https://github.com/KenAdeniji/WordEngineering)@[6abe004311...](https://github.com/KenAdeniji/WordEngineering/commit/6abe004311ae8bd919bc0a088837f4c9e8a8cef3)
#### Tuesday 2023-11-14 21:47:25 by Ken Adeniji

2023-11-07T03:03:00...2023-11-07T03:52:00

http://github.com/KenAdeniji/WordEngineering/blob/main/IIS/WordEngineering/2018-05-03Correspondence/2023-11-07T0303CommonwealthBankOfAustralia_-_IWouldLikeToSet-upAVISACreditCardOnMyAccount215110005724.txt

2023-11-07T03:20:00 Please kindly accept my request for a VISA credit card on my account 215 11000 5724.

mailto:customeradvocate@cba.com.au,CustomerRelations@cba.com.au,Stefan.Stankovic@cba.com.au,Wendy.Alo@cba.com.au

Kehinde Adewumi Adeniji
mailto:KenAdeniji@hotmail.com
http://www.JesusInTheLamb.com
(510) 796-8121
4762 Canvasback Common
Fremont, California (CA) 94555
United States of America (USA)

2023-11-14T08:04:00
From: Shanae.Hajsinger@cba.com.au <Shanae.Hajsinger@cba.com.au>Sent: Tuesday, November 14, 2023 3:51 AMTo: kenadeniji@hotmail.com <kenadeniji@hotmail.com>Subject: Your CommBank complaint outcome CF-13636381C

Dear Kehinde,
I have closed your complaint

I am writing to let you know that I have closed your complaint about a Visa card as I haven’t been able to reach you.

I have tried to contact you to discuss your concerns by:

    phone on 10/11/2023, 13/11/2023 & 14/11/2023
    email on 10/11/2023

Additional support

Support is available when you need it. You can find support options at www.commbank.com.au/support/financial-support.

Please get in touch if you would like to reopen this complaint.

Your options

If you are not satisfied with the outcome of our investigation you can:

Contact the Australian Financial Complaints Authority (AFCA), an independent external dispute resolution body approved by ASIC(time limits may apply, visit AFCA, afca.org.au, website for more information)	Write to: Australian Financial Complaints Authority, GPO Box 3, Melbourne VIC 3001Email: info@afca.org.auCall: 1800 931 678 (free call Monday to Friday 9am–5pm, AEST)

If you would like more information, you can contact me on +61 2 83883795 or at Shanae.Hajsinger@cba.com.au.

Regards,
Shanae Hajsinger
Customer Relations Specialist
Commonwealth Bank of Australia
Commonwealth Bank of Australia

************** IMPORTANT MESSAGE *****************************
This e-mail message is intended only for the addressee(s) and contains information which may be
confidential.
If you are not the intended recipient please advise the sender by return email, do not use or
disclose the contents, and delete the message and any attachments from your system. Unless
specifically indicated, this email does not constitute formal advice or commitment by the sender
or the Commonwealth Bank of Australia (ABN 48 123 123 124 AFSL and Australian credit licence 234945)
or its subsidiaries.
We can be contacted through our web site: commbank.com.au.
If you no longer wish to receive commercial electronic messages from us, please reply to this
e-mail by typing Unsubscribe in the subject line.
**************************************************************

2023-11-14T08:04:00...2023-11-14T08:22:00
Shanae.Hajsinger@cba.com.au, Beau.Sotingco@cba.com.au, CustomerRelations@cba.com.au, pottspoint.nsw@cba.com.au, cbaideas@cba.com.au, julie.gallagher@cba.com.au, amanda.hobbins@cba.com.au, mckaych@cba.com.au, fiona.turkovic@cba.com.au, Bobbi.Deacon@cba.com.au, Tony.White@cba.com.au, Stefan.Stankovic@cba.com.au
Shanae Hajsinger
I did not receive any telephone call from you. Your e-mail did not ask me to take any action.
You may telephone me on +1 (510) 796-8121.

2023-11-07T03:20:00 Please kindly accept my request for a VISA credit card on my account 215 11000 5724.

2023-11-14T11:16:00...2023-11-14T11:27:00
Francois@ljhcampsie.com.au, Campsie@ljh.com.au, Shanae.Hajsinger@cba.com.au, Beau.Sotingco@cba.com.au, CustomerRelations@cba.com.au, pottspoint.nsw@cba.com.au, cbaideas@cba.com.au, julie.gallagher@cba.com.au, amanda.hobbins@cba.com.au, mckaych@cba.com.au, fiona.turkovic@cba.com.au, Bobbi.Deacon@cba.com.au, Tony.White@cba.com.au, Stefan.Stankovic@cba.com.au

Please e-mail me the telephone numbers, e-mail addresses, and web addresses of the elected political representatives of Campsie.

From: Shanae Hajsinger <Shanae.Hajsinger@cba.com.au>Sent: Tuesday, November 14, 2023 9:26 PMTo: Ken Adeniji <kenadeniji@hotmail.com>Subject: RE: Your CommBank complaint outcome CF-13636381C

[ CBA Information Classification: Confidential ]

Hello,

My apologies, the phone number I was calling was an Australian number and was not the number listed below.

Are you wanting to add a card to your account or to apply for a credit card?

Thank you

cid:image001.png@01DA026D.C17A9CE0

Shanae Hajsinger

Customer Relations Specialist

Group Customer Relations

Customer and Community Advocacy

Phone: 02 8388 3795

Email: Shanae.Hajsinger@cba.com.au

[ CBA information handling guidelines can be found on our web site: commbank.com.au/DataClass ]

2023-11-14T13:28:00...2023-11-14T13:44:00
Shanae Hajsinger

I need a VISA card for making payments.

Therefore, an ATM or EFTPOS card will suffice.

Thank you, and God blesses.

---
## [RedBaronFlyer/RedBaronFlyer](https://github.com/RedBaronFlyer/RedBaronFlyer)@[0f5d14e68b...](https://github.com/RedBaronFlyer/RedBaronFlyer/commit/0f5d14e68b19111592301efe52a03de80aced61e)
#### Tuesday 2023-11-14 22:44:43 by Ben10Omintrix

Mook village and basic mook refactor (#78789)

## About The Pull Request
refactors mooks into basic mooks and re-adds them to the game

## Why It's Good For The Game
this refactors mooks into basic mobs and re adds them to the game. mooks
are now a part of lavaland. they come as a part of a random ruin which
consist of a entire village of friendly mooks. Mooks will aid players
but they will still attack ashwalkers because of some troubled history
between them.

![mookvillage](https://github.com/tgstation/tgstation/assets/138636438/ad1c5d63-c168-475a-a85d-b727dff43e7b)

mooks are a very diseased specie. nanotrasen discovered a small tribe of
mooks and cut a deal with their tribal chief to aid ss13 miners in
exchange for medical supplies.

tribal chief in his decked out home

![tribalchief](https://github.com/tgstation/tgstation/assets/138636438/cc0e0a11-9bf0-4322-b3ae-c7be43092ee8)

male mooks go out and mine and haul ore off back to their village. they
will deposit ores into a stand which is managed by another mook. they
will all return to their village to rest once a lavastorm comes.

![mookstand](https://github.com/tgstation/tgstation/assets/138636438/c7adbf4e-6322-4347-acfc-4e8d45aff798)

players can use this stand to withdraw any ore they like

![mookui](https://github.com/tgstation/tgstation/assets/138636438/a1318be8-50f7-49b2-827c-97bafdb2488a)

female mooks will stay behind in the village to guard it from
ashwalkers. they will also heal male mooks when they come back from a
long day of work. the tribal chief is a bum and chooses not to go out
and mine. he will stay behind in the village and issue commands to his
people rather than work

the village also has its own bard! he follows player visitors and plays
nice music for them while they are in the village (although he is not
very talented).

![mookbard](https://github.com/tgstation/tgstation/assets/138636438/5123e492-6657-4755-9dc7-ab94d4beb554)

he is still a warrior at heart tho so he will be smashing his guitar
over ashwalker skull

![mookshmash](https://github.com/tgstation/tgstation/assets/138636438/bf211bf0-e963-4dbb-b004-e653e06e3974)




## Changelog
:cl:
refactor: mooks are now basic mobs. please report any bugs
feature: added mook village to lavaland ruins!
/:cl:

---
## [RaeClay/flair_pair](https://github.com/RaeClay/flair_pair)@[5842974c22...](https://github.com/RaeClay/flair_pair/commit/5842974c2206ce7b36bf6ff5c9489f75b441fce5)
#### Tuesday 2023-11-14 22:50:28 by JohnAmick1

- homepage app bar done

BUG: when hot reloaded on the homepage the formatting is perfectly fine when navigating to the homescreen by pressing the home icon in the nav bar the app bar shifts everything in it to the right. Makes absolutely 0 fucking sense, fuck this shitty ass, cringey, fuckboy programming language

---
## [silencer-pl/cmss13](https://github.com/silencer-pl/cmss13)@[e7caf52c21...](https://github.com/silencer-pl/cmss13/commit/e7caf52c21e01e4580cbf03ff1c61579054dd7a2)
#### Tuesday 2023-11-14 23:13:19 by fira

Rewrite Xeno Acid processing (#4759)

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

Rewrites scheduling of xeno acid to hopefully finally be done with
dangling references warnings with acid. Also generally improves the
awful code quality

# Explain why it's good for the game
Like, dude, some of these values were outright inversed.
acid_**strength**=2.5 is noted as "250% speed" when it multiplies the
sleep delays. Can't leave code in that state.

# Testing Photographs and Procedure
Summary testing, timing appear correct overall but I'm not entirely
certain it's perfect due to random delays and obtuse code


# Changelog
:cl:
code: Rewrote Xeno Acid ticking code.
fix: Weather updates won't cause turfs to acid melt more rapidly anymore
/:cl:

---
## [silencer-pl/cmss13](https://github.com/silencer-pl/cmss13)@[e120ab795b...](https://github.com/silencer-pl/cmss13/commit/e120ab795ba0e92e4eb0f91fda194c59f83cb5aa)
#### Tuesday 2023-11-14 23:13:19 by fira

Add Item & Footprints offsets (#4762)

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

This:
* Adds transverse offsets to blood footprints
* Adds notable pixel offsets to a few items
* Adds a very slight pixel offset to all items
* Enables rotation for thrown flashlights
* Cause objects exiting a surface (rack/table) to regenerate offset
instead of being stuck at center
* Stops random offsets from overwriting mapped offsets

# Explain why it's good for the game
The goal is to have map visuals more organic when we have a lot of
objects on the ground - targeting in particular items you find readily
in dense areas such as Reqs or a FOB.

Consider this for example, the blood footprints are all aligned, in more
extreme situations (eg WO) it makes an actual "grid" which i personally
find very immersion breaking

![image](https://github.com/cmss13-devs/cmss13/assets/604624/83883e15-a9a0-4a2d-aa90-41c785e047b9)

Adding a slight offset helps counter that:

![image](https://github.com/cmss13-devs/cmss13/assets/604624/504d1baf-385c-4774-86f3-6331c4ac87ed)

# Changelog
:cl:
add: Bloody footprints are now slightly offset to break long visual
straight lines.
fix: Items do not align back to the center of turfs anymore when picked
from a surface (table or rack)
add: Some more items now have offsets on the map display, and they all
can be slightly offset.
/:cl:

---------

Co-authored-by: harryob <me@harryob.live>

---

