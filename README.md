## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-08-12](docs/good-messages/2023/2023-08-12.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,906,459 were push events containing 2,617,316 commit messages that amount to 148,982,398 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 65 messages:


## [t0nysama/tonystation](https://github.com/t0nysama/tonystation)@[dc6ddd821b...](https://github.com/t0nysama/tonystation/commit/dc6ddd821b1d9fe4783cf5d05c4ed2aa96f98e89)
#### Saturday 2023-08-12 00:00:28 by Cheshify

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
## [EuSouAFazer/tgstation](https://github.com/EuSouAFazer/tgstation)@[4e91d057d7...](https://github.com/EuSouAFazer/tgstation/commit/4e91d057d7d627bd8c356a2251195eb579106707)
#### Saturday 2023-08-12 00:27:27 by MrMelbert

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
## [NiLuJe/koreader](https://github.com/NiLuJe/koreader)@[f53768ea1c...](https://github.com/NiLuJe/koreader/commit/f53768ea1cc35e38472b5172f44d3d2cf5b75449)
#### Saturday 2023-08-12 00:48:28 by NiLuJe

ReaderActivityIndicator: Oh god, my eyes, they buuuuurn.

Make this a real boy, with a transient lipc handle.
And get rid of the insane 1s sleep on affected ReaderView paints,
because ouchy.

This is completely deprecated anyway, so this is entirely pointless,
and mainly to prevent implementation details from creeping into
reader.lua.

---
## [damonitor/linux](https://github.com/damonitor/linux)@[208532dc3b...](https://github.com/damonitor/linux/commit/208532dc3bdaac2cdc0017f00444293ea2dadb0c)
#### Saturday 2023-08-12 01:08:46 by David Hildenbrand

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
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[ce26e0b8c0...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/ce26e0b8c0d3d7441d2c18d7fadb080e305e3488)
#### Saturday 2023-08-12 01:10:38 by Pickle-Coding

Changeling armblade gets 35% armour penetration + better wounding. (#77416)

## About The Pull Request
Gives the changeling armblade an armour penetration of 35%. Sets their
bare_wound_bonus to 10 (from 20), and a wound_bonus of 10 (from -20).
## Why It's Good For The Game
The wound bonuses basically gave massive punishment if they attacked
anything but the skin. It honestly felt kinda lame. The better wounding
potential will help bring a bloodier and more exciting atmosphere when a
changeling whips out the blade.

The armour penetration will help reduce dragged out fights that get a
little silly, while keeping the wounding more consistent.
## Changelog
:cl:
balance: Changeling arm blade has an armour penetration of 35%.
balance: Changeling arm blade has a wound bonus of 10, from -20.
balance: Changeling has a bare wound bonus of 10, from 20.
/:cl:

---
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[88717966e1...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/88717966e13e5a55e207d356ee193b1ee6753ea2)
#### Saturday 2023-08-12 01:11:06 by carlarctg

Drill module automatically disables if it's about to drill into gibtonite (#77385)

## About The Pull Request

Drill module automatically disables if it's about to drill into
gibtonite.

## Why It's Good For The Game

> Drill module automatically disables if it's about to drill into
gibtonite

There's not enough time to react, the mining scanner is surprisingly
slow sometimes and it means you drill straight into gibtonite, which
primes it the first drill and blows it up the second, which is a lot
more of a pain than it sounds because drilling is night-instant. These
explosions are usually enough to crit you, and if they don't, the stun
and area clear means any fauna can wander in and finish you off.

The auto-disable still makes it an annoyance to stumble upon gibtonite,
but it won't round end you for using modsuits.

## Changelog

:cl:
qol: Drill module automatically disables if it's about to drill into
gibtonite
/:cl:

---
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[835da329cf...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/835da329cfe3eec610d827e4830af64a673b7272)
#### Saturday 2023-08-12 01:19:02 by carlarctg

Restricts Scrapheap & Lepton Violet behind conditions, alters Rollerdome (#77277)

## About The Pull Request

Lepton Violet (wabbajack) shuttle must be unlocked by having some form
of polymorph happen in-game first (Pride Mirror or the cursed springs
are the most accessible sources)

Scrapheap shuttle can only be bought if the Cargo budget is below 600
credits, and the shuttle has just less than half of its usual refueling
time left. However, it gives the cargo budget an influx of 3000 credits!

Uncle Pete's Rollerdome has had its price increased, and the disco
machine is no longer unbreakable.

## Why It's Good For The Game

First off, here is my reasoning for why these need altering at all.

Players will always naturally gravitate to the wackiest and
most-out-there options, in this case this applies to shuttles. It's why
the Monastery or the Asteroid or Daniel are reasonably common sights,
more common than some of the 'boring' shuttle options that don't need
unlock with an emag.

The problem here, as I see it, is that there is no incentive
what-so-ever to NOT purchase these 'wacky' shuttles. Some of the
shuttles in the code are just way too stupid to be seen on most or even
some rounds (Arena, Disco Inferno?), so they require rare unlocks to
occur. Wacky shuttles being spammed round after round are bad due to
several reasons:
1. Players will run every joke to the ground. Wacky conditionless
shuttles take up a large amount of space in the shuttle memeplex, so
they are disproportionately seen in comparison to any of the
less-extravagant but more grounded and actually interesting options.
(Medisim? Monkeys anyone?). This ends up making the wacky shuttles
actually *less* wacky and just the stale and boring options.
2. Wacky shuttles affect the end-round quite a lot. This is fine, of
course, but not when these wacky shuttles can be seen every round.
3. These wacky shuttles don't have proper facilities. None of them have
a good medical section, or emergency supplies, or enough room. This gets
pretty annoying pretty fast.
4. One Funny Guy (the quintessential example being the clown with a dead
captain's ID) is all but guaranteed to try to buy the funniest and most
annoying shuttle to piss off the rest of the crew. With how Funny and
Annoying these shuttles are, not to mention how dirt-cheap they are (or
literally give you money!), they're easily the most seen alternate
shuttles, which isn't good when they alter how the round-end plays so
heavily.

> Lepton Violet (wabbajack) shuttle must be unlocked by having some form
of polymorph happen in-game first (Pride Mirror is the most accessible
source)

The Wabbajack has a endless source of voluntary Polymorphs with a
comically low price, which means it is purchased endlessly by crew, not
to mention being literally a source of free syndiborgs and xenos. While
I'm not a balanceposter, this does come with some annoyances especially
for antagonists who just randomly get blown up by an assault borg. This
is fine and fun every so often, but not as a common occurrence, not as a
guaranteed every-round option. I think it's an excellent candidate for
an unlock condition.

> Scrapheap shuttle can only be bought if the Cargo budget is below 600
credits, and the emergency shuttle is more than halfway refueled.
However, it gives the cargo budget an influx of 3000 credits!

This is LITERALLY 'haha grief shuttle', I have no idea how it even got
in as a condition-less shuttle. You see the captain buy it For No Raisin
Lul 2 minutes in, sigh to yourself, and secure an EVA suit when the
shuttle lands to try to survive in the unbelievably cramped space.
(Someone always blows it up.)

Instead of being JUST Grief Shuttle, now it has some interesting reasons
to exist. Revs and you're dirt-poor? Nukies just declared war after the
Clown bought ten crates of creampie dufflebags? Buy this shuttle and get
an influx of money.

> Uncle Pete's Rollerdome has had its price increased, and the disco
machine is no longer unbreakable.

This one isn't as egregious as the above, but I believe my personal
dislike of it extends to a game design level, to an extent. One person
can buy this shuttle and the crew as a whole are left to groan as they
prepare for a noisy, confusing shuttle in which everyone is ten tiles
shifted to their left as their sprite does the most ridiculous dance
seen in SS13 history. 'Just turn the music off!': I'm glad this is an
option, but it doesn't change how much this shuttle alters things. It's
fine as a sendoff to a nice, chill greenshift, but as a constant sight
in red shifts it's just... frustrating. And purchased BECAUSE it's
frustrating, to the short-lived schadenfreude of one person and the
frustration of others.

And then the unbreakable disco machine. Why is it unbreakable. If the
crew doesn't want to listen to the thing, let them break it? Buy Disco
Inferno if you want an unbreakable disco.

Some of these changes are probably over-the-top, but remember that these
will still be seen in-game, just a bit rarer. Worst case scenario the
shuttle replacement event will let them have their time in the
limelight.

## Changelog

:cl:
balance: Lepton Violet (wabbajack) shuttle must be unlocked by having
some form of polymorph happen in-game first (Pride Mirror or the cursed
springs are the most accessible sources)
balance: Scrapheap shuttle can only be bought if the Cargo budget is
below 600 credits, and the shuttle has just less than half of its usual
refueling time left. However, it gives the cargo budget an influx of
3000 credits!
qol: Uncle Pete's Rollerdome has had its price increased, and the disco
machine is no longer unbreakable.
/:cl:

---
## [KastanDay/langchain-improved-agents](https://github.com/KastanDay/langchain-improved-agents)@[16af5f8690...](https://github.com/KastanDay/langchain-improved-agents/commit/16af5f86905705096552507f8739b5cfcaa77aa4)
#### Saturday 2023-08-12 01:23:10 by niklub

Add LabelStudio integration (#8880)

This PR introduces [Label Studio](https://labelstud.io/) integration
with LangChain via `LabelStudioCallbackHandler`:

- sending data to the Label Studio instance
- labeling dataset for supervised LLM finetuning
- rating model responses
- tracking and displaying chat history
- support for custom data labeling workflow

### Example

```
chat_llm = ChatOpenAI(callbacks=[LabelStudioCallbackHandler(mode="chat")])
chat_llm([
    SystemMessage(content="Always use emojis in your responses."),
        HumanMessage(content="Hey AI, how's your day going?"),
    AIMessage(content="🤖 I don't have feelings, but I'm running smoothly! How can I help you today?"),
        HumanMessage(content="I'm feeling a bit down. Any advice?"),
    AIMessage(content="🤗 I'm sorry to hear that. Remember, it's okay to seek help or talk to someone if you need to. 💬"),
        HumanMessage(content="Can you tell me a joke to lighten the mood?"),
    AIMessage(content="Of course! 🎭 Why did the scarecrow win an award? Because he was outstanding in his field! 🌾"),
        HumanMessage(content="Haha, that was a good one! Thanks for cheering me up."),
    AIMessage(content="Always here to help! 😊 If you need anything else, just let me know."),
        HumanMessage(content="Will do! By the way, can you recommend a good movie?"),
])
```

<img width="906" alt="image"
src="https://github.com/langchain-ai/langchain/assets/6087484/0a1cf559-0bd3-4250-ad96-6e71dbb1d2f3">


### Dependencies
- [label-studio](https://pypi.org/project/label-studio/)
- [label-studio-sdk](https://pypi.org/project/label-studio-sdk/)

https://twitter.com/labelstudiohq

---------

Co-authored-by: nik <nik@heartex.net>

---
## [Vincent983/tgstation](https://github.com/Vincent983/tgstation)@[f0dc574c37...](https://github.com/Vincent983/tgstation/commit/f0dc574c37c6defc0a9e2d4117d20c3963a11d86)
#### Saturday 2023-08-12 01:43:36 by carlarctg

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
## [effigy-se/effigy-se](https://github.com/effigy-se/effigy-se)@[297f7f88e8...](https://github.com/effigy-se/effigy-se/commit/297f7f88e866d4a17b27cb15c0b8ee606742bbf6)
#### Saturday 2023-08-12 01:44:30 by Sealed101

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
## [Gooseverse/Daily-Joke-Website](https://github.com/Gooseverse/Daily-Joke-Website)@[3fb22acaea...](https://github.com/Gooseverse/Daily-Joke-Website/commit/3fb22acaea604a2233de64238c32a08d69d34bbb)
#### Saturday 2023-08-12 02:15:23 by Gooseverse

Create DJW-html

Copy and paste this code into an HTML file, and you'll have a basic website that displays a random funny joke every day. You can customize the list of jokes by adding more entries to the jokes array in the <script> section.

---
## [Madhu-0203/UX-UI-Figma](https://github.com/Madhu-0203/UX-UI-Figma)@[f6584d5977...](https://github.com/Madhu-0203/UX-UI-Figma/commit/f6584d59774751af0835dcedecfddb1ef4a0aaa3)
#### Saturday 2023-08-12 02:30:20 by Madhu-0203

Create README.md

Hello friends :) 

I had been working with Figma for a year now when I was on the design team of the IEEE - IAS chapter. I started learning basic designing through Canvas, 
Later I worked my way up by learning the color theory, how to choose the right template, how to put the right elements, and position them. 
Here, I am attaching one of my UX/UI design projects that I did during my IEEE tenure. I have designed a music player web front end using Figma. My top inspirations were Spotify and Gaana.

---
## [newtonick/seedsigner](https://github.com/newtonick/seedsigner)@[d2a657f2d4...](https://github.com/newtonick/seedsigner/commit/d2a657f2d43c6e77e9c48cb1f859e8f4984a5f00)
#### Saturday 2023-08-12 02:57:50 by Marc G

Various edits B4 upstream submission

After a long hiatus, I have finally completed my proposed changes to the software verification section of our readme.

The verification focuses on keybase.io now storing and verifying the 3 online properties (seedsigner.com, twitter.com/seedsigner and github.com/seedsigner)

This makes the key more secure, easier to import and generally less hassle. its also revokable.  

There is more detail about how/why in the expand blocks, but It was suggested to me to keep the instructions straightforward (ie do this and now do that) , so I have reduced focus much on the why. 
However, some basic "why & how" has also been placed in new collapsible sections, at the end of each step. 

Later on, I want to add color to the collapse sections so that they show a natural boundary, but so far that markdown code is elusive to me. ;) 
Done is better than perfect....
The same for getting my external links to open in a new tab/window. sigh. Markdown is ... well....tricky. 

I can make the screenshots smaller. please comment on their size.


The Verification is done in 3 steps:
1. import the public key
2. Verify its the correct key by verying it and then comparing the Key ID to Keybase.io/seedsigner. If it matches, then its the real seedsigner project person that signed.
this is arguablly the most critical step of verifying and hence we ask the user to check for themselves that the key ID from verify is the same as on keybase.io. Hence the Key ID's are blurred in the screenshots. We dont want the user to compare the screenshots to each other. we want them to compare their result to their browser. 

3. Verify that the other files (at this stage just the .zip file) are also not altered. This does a comparision of the various files actual and expected hashes.

If all is well here, then tell the user about their success :). 
Explain the warnings, which ones are benign, and what to do if verification fails.


Lastly, "Write the software to the MicroSD' section - 
I have got draft text for this, but havent published it yet. 
The verify PR is big enough !!

Please review for my PR flow and clarity, I do still want to improve the formatting,  but wanted to get everyone's thoughts before messing with the detailed formatting and line breaks, which are especially painful!

FYI - I have done my screenshots using layers, so it easy to edit in the future. I think they

---
## [ss220club/Skyrat-tg](https://github.com/ss220club/Skyrat-tg)@[d5655c3c55...](https://github.com/ss220club/Skyrat-tg/commit/d5655c3c55fab0f4450659947fad1a40043893dc)
#### Saturday 2023-08-12 03:17:53 by SkyratBot

[MIRROR] Adds Summon Simians & Buffs/QoLs Mutate [MDB IGNORE] (#22970)

* Adds Summon Simians & Buffs/QoLs Mutate (#77196)

## About The Pull Request

Adds Summon Simians, a spell that summons four monkeys or lesser
gorillas, with the amount increasing per upgrade. The monkeys have
various fun gear depending on how lucky you get and how leveled the
spell is. If the spell is maximum level, it only summons normal
gorillas.

Added further support for nonhuman robed casting: Monkeys, cyborgs, and
drones can all now cast robed spells as long as they're wearing a
wizardly hat as well.

Made monkeys able to wield things again.

Wizard Mutate spell works on non-human races. It also gives you
Gigantism now (funny). If the Race can't support tinted bodyparts, your
whole sprite is temporarily turned green.

Made Laser eyes projectiles a subtype of actual lasers, which has
various properties such as on-hit effects and upping the damage to 30.

Improved some monkey AI code.

## Why It's Good For The Game

> Adds Summon Simians, a spell that summons four monkeys or lesser
gorillas, with the amount increasing per upgrade. The monkeys have
various fun gear depending on how lucky you get and how leveled the
spell is. If the spell is maximum level, it only summons normal
gorillas.

It's criminal we don't have a monky spell, and this is a really fun spin
on it. Total chaos, but total monky chaos. It's surprisingly strong,
but! it can very well backfire if you stay near the angry monkeys too
long and your protection fades away. Unless you become a monkey
yourself!!

> Wizard Mutate spell works on non-human races.

This spell is great but it's hampered by the mutation's human
requirement, which is reasonable in normal gameplay. Wizards don't need
to care about that, and the human restriction hinders a lot of possible
gimmicks, so off it goes. Also, wizard hulk does't cause chunky fingers
for similar reasons

> Made Laser eyes projectiles a subtype of actual lasers, which has
various properties such as on-hit effects and upping the damage to 30.

Don't really caer about the damage so much, this is more so that it has
effects such as on-hit visuals. Can lower the damage if required, but
honestly anything that competes against troll mjolnir is good.

> Added further support for nonhuman robed casting: Monkeys, cyborgs,
and drones can all now cast robed spells as long as they're wearing a
wizardly hat as well.

SS13 is known for 'The Dev Team Thinks of Everything' and I believe this
is a sorely lacking part of this or something. It's funny.
I want to see a monkey wizard.

> Made monkeys able to wield things again.

I really don't know why this was a thing and it was breaking my axe and
spear wielding primal monkeys. Like, why?

## Changelog

:cl:
add: Adds Summon Simians, a spell that summons four monkeys or lesser
gorillas, with the amount increasing per upgrade. The monkeys have
various fun gear depending on how lucky you get and how leveled the
spell is. If the spell is maximum level, it only summons normal
gorillas.
balance: Wizard Mutate spell works on non-human races. It also gives you
Gigantism now (funny). If the Race can't support tinted bodyparts, your
whole sprite is temporarily turned green.
balance: Made Laser eyes projectiles a subtype of actual lasers, which
has various properties such as on-hit effects and upping the damage to
30.
add: Added further support for nonhuman robed casting: Monkeys, cyborgs,
and drones can all now cast robed spells as long as they're wearing a
wizardly hat as well.
balance: Made monkeys able to wield two-handed things again.
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@ users.noreply.github.com>

* Adds Summon Simians & Buffs/QoLs Mutate

* Updates our modular file to take this into account (I hate that this exists)

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@ users.noreply.github.com>
Co-authored-by: GoldenAlpharex <jerego1234@hotmail.com>

---
## [ss220club/Skyrat-tg](https://github.com/ss220club/Skyrat-tg)@[3782e4b710...](https://github.com/ss220club/Skyrat-tg/commit/3782e4b71098d12588696d9263f2ee8748caf9bf)
#### Saturday 2023-08-12 03:17:53 by Bloop

[MISSED MIRROR] Martian Food: A Taste of the Red Planet (#75988) (#23013)

Martian Food: A Taste of the Red Planet (#75988)

## About The Pull Request
Adds a selection of new foods and drinks based around Mars.
More information on Mars can be found here:
https://github.com/tgstation/common_core/blob/master/Interesting%20Planets/Human%20Space/The%20Sol%20System.md
To summarise for the general audience, Mars is a vital colony of the
Terran Federation, having been primarily settled (at least originally)
by Cybersun Industries to harvest its lucrative supplies of plasma, the
second largest in human space behind Lavaland. This has given Mars a
diverse culture evolving from the mostly East Asian colonists, and their
food reflects this.

Thanks to Melbert for their work on the soup portion of this PR.

The food:
Martian cuisine draws upon the culinary traditions of East Asia, and
adds in fusion cuisine from the later colonists. Expect classics such as
ramen, curry, noodles and donburi, as well as new takes on the formula
like the Croque-Martienne, Peanut Butter Ice Cream Mochi, and the
Kitzushi- chilli cheese and rice inside a fried tofu casing. Oh, and
lots of pineapple. The Martians love pineapple:

![image](https://github.com/tgstation/tgstation/assets/58124831/c9ae33a1-e03a-4f94-8ce0-8ad124e88e8d)
Also included are some foods for Ethereals, which may or may not be
hinting at something I've got planned...

The drinks:
Four new base drinks make their way to the game, bringing with them a
host of new cocktails: enjoy new ventures in bartending with Coconut
Rum, Shochu/Soju, Yuyake (our favourite legally-distinct melon liqueur),
and Mars' favourite alcoholic beverage, rice beer. Each is available in
the dispenser, as well as bottles in the booze-o-mat:

![image](https://github.com/tgstation/tgstation/assets/58124831/914a6e2a-7ef5-4791-ae31-d08fa9211083)

The recipes:
To make your (and the wiki editors) lives easier, please find below the
recipes for both foods and drinks:
Food: https://hackmd.io/@EOBGames/BkVFU0w9Y
Drinks: https://hackmd.io/@EOBGames/rJ1OhnsJ2
## Why It's Good For The Game
Another lot of variety for the chef and bartender, as well as continuing
the work started with lizard and moth food in getting Common Core into
the game in a tangible and fun way.
## Changelog
:cl: EOBGames, MrMelbert
add: Mars celebrates the 250th anniversary of the Martian Concession
this year, and this has brought Martian cuisine to new heights of
popularity. Find a new selection of Martian foods and drinks available
in your crafting menu today!
/:cl:

---------

Co-authored-by: EOBGames <58124831+EOBGames@users.noreply.github.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[042005b010...](https://github.com/treckstar/yolo-octo-hipster/commit/042005b010922a3d8773eb32da6703b35fe0db94)
#### Saturday 2023-08-12 04:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [capybara26/capybot](https://github.com/capybara26/capybot)@[3cc9b21555...](https://github.com/capybara26/capybot/commit/3cc9b2155543931a5c0dc7cfd2106e65e925144f)
#### Saturday 2023-08-12 04:41:11 by capybara26

Add files via upload

Capy AI bot!
Capy AI Bot
Welcome to Capy AI Bot, the future of interactive AI conversations! Imagine having conversations with an AI that not only understands your words but responds with distinct personalities. Capy brings you a groundbreaking experience by allowing you to choose from a variety of personalities for your AI companion. Whether you're looking for an insightful adviser, a witty conversationalist, or a creative thinker, Capy has a personality to match your mood.

Getting Started
Download: Head over to the Releases section of this repository and download the "built.exe" file.

Run the Executable: Once the download is complete, locate the "built.exe" file and double-click to run it. This initiates Capy's setup process.

Initialization: Depending on your computer's processing power, the initialization process might take a few moments. Please be patient; Capy is preparing to provide you with a unique experience.

Choose Your Companion: After initialization, you'll be introduced to a range of captivating personalities. Select the one that resonates with you at the moment, and watch as Capy transforms into your chosen persona.

Engage and Explore: Now comes the exciting part! Start conversing with Capy. Ask questions, share thoughts, or simply enjoy a friendly chat. Your chosen personality will infuse each response with a distinct flair, ensuring that every interaction feels tailor-made for you.

---
## [bhos1242/Java-Programming-Notes](https://github.com/bhos1242/Java-Programming-Notes)@[032887f266...](https://github.com/bhos1242/Java-Programming-Notes/commit/032887f2663e0547a595bf7c33ee899725120193)
#### Saturday 2023-08-12 04:49:38 by vivek1242

start(): Imagine you're launching a rocket. The start() method ignites the thread and begins its execution. It's like pressing the "launch" button for a thread.

run(): This method contains the actual task the thread will perform. It's like the instructions for the rocket's flight. When you call start(), it's as if you've given the rocket the green light to follow those instructions.

sleep(): Think of this as a pause button. The sleep() method lets the thread pause for a specified amount of time before continuing. It's like having the rocket pause for a moment before resuming its flight.

join(): Imagine you're in a car rally and want to wait for your friend's car to catch up. The join() method makes the current thread wait for another thread to finish before it continues. It's like waiting for your friend's car to catch up before you proceed.

yield(): This method is like saying, "I'm giving other threads a chance to work." It's a hint to the system that the thread is willing to yield its turn to other threads. It's like letting other cars take a turn on the road.

isAlive(): This method checks whether a thread is still active. It's like asking if the rocket is still in the air or has landed.

getName(): Just as you have a name, a thread has a name too. This method gets the name of the thread. It's like finding out the name of a car in the rally.

setPriority(): This method sets the priority of the thread, indicating how important it is. It's like giving a car a priority level in the rally, determining how much attention it gets.

getId(): Every thread has a unique identifier. This method gets the ID of the thread. It's like having a special number for each car in the rally.

interrupt(): Think of this as sending a signal to stop a thread's current operation. It's like using a signal to stop a car on the road.

Remember, these methods are tools you can use to control and manage threads, making your Java programs more efficient and responsive. Just like using tools to navigate and manage different aspects of a race or journey, these thread methods help you guide your threads in the right direction.

---
## [t895/yuzu](https://github.com/t895/yuzu)@[8e703e08df...](https://github.com/t895/yuzu/commit/8e703e08dfcf735a08df2ceff6a05221b7cc981f)
#### Saturday 2023-08-12 04:55:52 by comex

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
## [RorriMaesu/quizbrain](https://github.com/RorriMaesu/quizbrain)@[56f4c7411c...](https://github.com/RorriMaesu/quizbrain/commit/56f4c7411c1cd6bd811cfd50f647b885eadd41d7)
#### Saturday 2023-08-12 05:20:31 by Andrew J. Green

Create README.md

QuizBrain: Dive Deeper into the World of Trivia
A World of Knowledge at Your Fingertips:
QuizBrain isn't just another trivia game; it's a deep dive into a vast ocean of knowledge. With almost a thousand meticulously curated questions spanning eight diverse categories, this game is designed to engage, entertain, and educate. Whether you're a pop culture enthusiast, a history buff, or a Python geek, QuizBrain has something for everyone.

Category Breakdown:

Geography (124 questions): Traverse continents, explore landmarks, and discover hidden geographical gems. How well do you know our world?

History (139 questions): Journey through time, from ancient civilizations to modern-day events. Are you ready to relive the moments that shaped our world?

Math (121 questions): Challenge your numerical prowess and problem-solving skills. Do numbers speak to you?

Movies & TV Shows (131 questions): Dive into the world of entertainment, from iconic classics to the latest blockbusters. Are you the ultimate film and TV aficionado?

Pop Culture (116 questions): From music legends to viral trends, test your knowledge of the phenomena that define popular culture.

Python (96 questions): For the coders and tech enthusiasts, tackle questions on one of the most popular programming languages in the world.

Science (116 questions): Unravel the mysteries of the universe, from the tiniest atoms to vast galaxies. How deep does your scientific curiosity go?

Sports (153 questions): Relive iconic moments, know your athletes, and delve into the world of sports. Are you game?

An Ever-Evolving Experience: With a total of 996 questions and counting, QuizBrain ensures that players always have fresh challenges awaiting them. Plus, with our commitment to continuous updates, you can expect even more categories and questions in the future.

Why QuizBrain:

Diverse Categories: Catering to a wide range of interests, ensuring that every player finds their niche.
Educational Value: Not just for fun, but also a tool for learning and expanding one's horizons.
Replayability: With such a vast question bank, every game feels new and challenging.
User-Centric Design: Easy to navigate, visually appealing, and optimized for all devices.
Whether you play solo, challenge a friend, or engage in a group trivia night, QuizBrain promises hours of fun and learning. Ready to unleash the trivia master in you?

---
## [nattolecats/device_oneplus_denniz](https://github.com/nattolecats/device_oneplus_denniz)@[e1e28f9f63...](https://github.com/nattolecats/device_oneplus_denniz/commit/e1e28f9f638ebead1e769ff5dde9efa26bfd9be7)
#### Saturday 2023-08-12 05:57:18 by lahaina

Revert "denniz: rootdir: Disable EAS and switch HMP"
* This might battery sucking as fuck.

This reverts commit e77a11c593430c93d88060834c1d1928e63535b1.

---
## [spartanbobby/cmss13](https://github.com/spartanbobby/cmss13)@[f3fc60ed65...](https://github.com/spartanbobby/cmss13/commit/f3fc60ed655d27bb3f012d0e0d834c64990b173d)
#### Saturday 2023-08-12 06:14:47 by morrowwolf

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
## [isaacs/clock-mock](https://github.com/isaacs/clock-mock)@[8bf7c85e3c...](https://github.com/isaacs/clock-mock/commit/8bf7c85e3c48a869d94be78ef6454ab49eb07b68)
#### Saturday 2023-08-12 06:14:55 by isaacs

start at 1, not zero

There are some weird edge cases that can occur when the initial time is
falsey.

In real life, it's not like we'll ever be running code on midnight of
new years eve 1970, so I think it's perfectly fine to start at a truthy
value and avoid those edge cases.

---
## [brain-tec/runbot](https://github.com/brain-tec/runbot)@[7348e4d7a4...](https://github.com/brain-tec/runbot/commit/7348e4d7a4d3565433423cc2d91307d40fd46d35)
#### Saturday 2023-08-12 06:17:39 by Xavier Morel

[IMP] runbot_merge: ensure at least 1s between mutating GH calls

Mostly a temporary safety feature after the events of 07-31: it's
still not clear whether that was a one-off issue or a change in
policy (I was not able to reproduce locally even doing several
set_refs a second) and the gh support is not super talkative, but it
probably doesn't hurt to commit the workaround until #247 gets
implemented.

On 2023-07-31, around 08:30 UTC, `set_ref` started failing, a lot
(although oddly enough not continuously), with the unhelpful message
that

> 422: Reference cannot be updated

This basically broke all stagings, until a workaround was implemented
by adding a 1s sleep before `set_ref` to ensure no more than 1
`set_ref` per second, which kinda sorta has been the github
recommendation forever but had never been an issue
before. Contributing to this suspicion is that in late 2022, the
documentation of error 422 on `PATCH git/refs/{ref}` was updated to:

> Validation failed, or the endpoint has been spammed.

Still would be nice if GH was clear about it and sent a 429 instead.

Technically the recommendation is:

> If you're making a large number of POST, PATCH, PUT, or DELETE
> requests for a single user or client ID, wait at least one second
> between each request.

So... actually implement that. On a per-worker basis as for the most
part these are serial processes (e.g. crons), we can still get above
the rate limit due to concurrent crons but it should be less likely.

Also take `Retry-After` in account, can't hurt, though we're supposed
to retry just the request rather than abort the entire thing. Maybe a
future update can improve this handling.

Would also be nice to take `X-RateLimit` in account, although that's
supposed to apply to *all* requests so we'd need a second separate
timestamp to track it. Technically that's probably also the case for
`Retry-After`. And fixing #247 should cut down drastically on the API
calls traffic as staging is a very API-intensive process, especially
with the sanity checks we had to add, these days we might be at 4
calls per commit per PR, and up to 80 PRs/staging (5 repositories and
16 batches per staging), with 13 live branches (though realistically
only 6-7 have significant traffic, and only 1~2 get close to filling
their staging slots).

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[b033e1ed6a...](https://github.com/shiptest-ss13/Shiptest/commit/b033e1ed6a1e7f87edc73a75a96bcf6536e39aba)
#### Saturday 2023-08-12 06:51:35 by Sun-Soaked

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
## [mitaroThanken/try-vite-react](https://github.com/mitaroThanken/try-vite-react)@[5a6f29ec67...](https://github.com/mitaroThanken/try-vite-react/commit/5a6f29ec67b7490f107f2dd74369046c6a488e2f)
#### Saturday 2023-08-12 09:43:41 by YAMAMI Taro

npx storybook@latest init

node ➜ /workspaces/sample (feature/storybook) $ npx storybook@latest init
Need to install the following packages:
  storybook@7.2.3
Ok to proceed? (y)

 storybook init - the simplest way to add a Storybook to your project.

 • Detecting project type. ✓
 • Preparing to install dependencies. ✓

up to date, audited 152 packages in 632ms

37 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
. ✓
 • Detected Vite project. Setting builder to Vite. ✓
 • Adding Storybook support to your "React" app
  ✔ Getting the correct version of 9 packages
✔ We have detected that you're using ESLint. Storybook provides a plugin that gives the best experience with Storybook and helps follow best practices: https://github.com/storybookjs/eslint-plugin-storybook#readme

Would you like to install it? … yes
    Configuring Storybook ESLint plugin at .eslintrc.cjs
  ✔ Installing Storybook dependencies
. ✓
 • Preparing to install dependencies. ✓

up to date, audited 991 packages in 1s

193 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
. ✓

attention => Storybook now collects completely anonymous telemetry regarding usage.
This information is used to shape Storybook's roadmap and prioritize features.
You can learn more, including how to opt-out if you'd not like to participate in this anonymous program, by visiting the following URL:
https://storybook.js.org/telemetry

╭──────────────────────────────────────────────────────────────────────────────╮
│                                                                              │
│   Storybook was successfully installed in your project! 🎉                   │
│   To run Storybook manually, run npm run storybook. CTRL+C to stop.          │
│                                                                              │
│   Wanna know more about Storybook? Check out https://storybook.js.org/       │
│   Having trouble or want to chat? Join us at https://discord.gg/storybook/   │
│                                                                              │
╰──────────────────────────────────────────────────────────────────────────────╯

Running Storybook
Need to install the following packages:
  npm@9.8.1
Ok to proceed? (y)

> sample@0.0.0 storybook
> storybook dev -p 6006 --initial-path=/onboarding --quiet

@storybook/cli v7.2.3

info => Starting manager..
8:41:31 AM [vite] ✨ new dependencies optimized: @storybook/blocks
8:41:31 AM [vite] ✨ optimized dependencies changed. reloading
^C

---
## [madhumala16/To-DoAPP](https://github.com/madhumala16/To-DoAPP)@[368971c1a5...](https://github.com/madhumala16/To-DoAPP/commit/368971c1a5b42b55b33d51d1e81a07be2dad636c)
#### Saturday 2023-08-12 10:03:42 by madhumala16

commit

"🚀 Dynamic To-Do App with React, Redux-Toolkit, Framer-Motion, and Tailwind CSS 📝

Welcome to our cutting-edge Dynamic To-Do Application built with the synergy of top-tier JavaScript technologies! This project harnesses the power of React, the simplicity of Redux-Toolkit, the fluid animations of Framer-Motion, and the responsive design of Tailwind CSS to provide you with an unparalleled to-do list experience.

🌟 Features:

Seamless User Experience: Crafted with React, our app offers a smooth and responsive user interface that adapts flawlessly to various devices.
Efficient State Management: Redux-Toolkit optimizes state management, enabling lightning-fast updates and synchronization across components.
Stunning Animations: Framer-Motion breathes life into the app with delightful animations, creating an engaging and interactive environment.
Intuitive To-Do Management: Add, edit, and delete tasks effortlessly while enjoying real-time updates thanks to Redux-Toolkit's robust state handling.
Sleek Design: Tailwind CSS guarantees an aesthetically pleasing and fully responsive layout, ensuring the app looks great on any screen.
🔧 Tech Stack:

React: A leading JavaScript library for building dynamic user interfaces.
Redux-Toolkit: A comprehensive state management solution for efficient and predictable state updates.
Framer-Motion: A powerful animation library that enhances user interaction and engagement.
Tailwind CSS: A utility-first CSS framework that streamlines styling and ensures consistent design.
🚀 Dive In:
Elevate your to-do list experience with our feature-rich app. Whether you're a productivity enthusiast or just want an efficient task management tool, our app has got you covered. Explore the seamless blend of React, Redux-Toolkit, Framer-Motion, and Tailwind CSS – all designed to empower your workflow . Start revolutionizing your task management with our Dynamic To-Do App. Embrace efficiency, embrace productivity! 💼📅"

---
## [lkulasek/Ortho4XP](https://github.com/lkulasek/Ortho4XP)@[dfd67784ed...](https://github.com/lkulasek/Ortho4XP/commit/dfd67784edb8f10ce08f2bf0bcdce5bed3fa2ddd)
#### Saturday 2023-08-12 10:42:10 by Erwin Kaats

In the example for pyproj it seems like you cannot first initialize the projections, but need to do it like this. Conversely, we could initialize the transformers, but then we'd need pairs per provider because we need to be able to transform to and from the given projection.

Some quick testing makes me think this is not that expensive though, but I haven't profiled it yet to really check how expensive it is to create a new Transformer every time.

This also means the Slovenia hack won't work for now, but that provider wasn't working anyway.

---
## [lbnesquik/TerraGov-Marine-Corps](https://github.com/lbnesquik/TerraGov-Marine-Corps)@[fb4899d20e...](https://github.com/lbnesquik/TerraGov-Marine-Corps/commit/fb4899d20e990a0a65b8cb5b0ad19b1ef9ab083e)
#### Saturday 2023-08-12 10:57:51 by KM-Catman

Slight redesign of Valhalla Vendors and Chemistry. Adds FC and Synth to Valhalla. (#13612)

* Valhalla Fixes

Start room is now all Hulls, adds a Friend, Materializes the Chaplain's chained demon, and adds more Xeno Huds.

* FC and Synth Added. Slight readjustment.

* Changed the vendor section as per Grayson's request

* Adds three new Warning Stripes.

Adds a FCDR, Synth, and Mech warning stripe. Adds them in front of the prep rooms

* Duct Taped Space

* Removed random bedsheet (Goddamn you hotkeys)

---
## [Latentish/Shiptest](https://github.com/Latentish/Shiptest)@[ee4021c507...](https://github.com/Latentish/Shiptest/commit/ee4021c50792c11bfd21085156edd32200c21cb8)
#### Saturday 2023-08-12 11:11:21 by Imaginos16

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
## [Lambdagon/tf_coop_lambda](https://github.com/Lambdagon/tf_coop_lambda)@[3d279ba66c...](https://github.com/Lambdagon/tf_coop_lambda/commit/3d279ba66c7aa7feb510b2509d64244c7f2829bc)
#### Saturday 2023-08-12 11:38:37 by Average_Medal_Enjoyer

also wtf why aren't these pushed already, fuck you git

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[bf28afc702...](https://github.com/treckstar/yolo-octo-hipster/commit/bf28afc70281ce424ee252347e98163beb281748)
#### Saturday 2023-08-12 12:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [EOBGames/tgstation](https://github.com/EOBGames/tgstation)@[4c99fb2ebb...](https://github.com/EOBGames/tgstation/commit/4c99fb2ebb26179044c582ae6494338cb2aa35e2)
#### Saturday 2023-08-12 12:26:18 by carlarctg

Coroner additions and tweaks (#76534)

## About The Pull Request

Serrated bone shovels can be created with any kind of shovel now, not
just a spade (???)

Serrated bone shovels can be used in place of circular saw in most
surgeries.

Added a duller (still deadly) variant of the serrated bone shovel as
coroner mail.

Autopsy scanners now act as advanced health analyzers on dead and
seemingly-dead people.

Increased the force, throwforce, and wound bonus of inert ritual knives
and scythes.

Coroner gloves can quickly apply medicine like nitrile gloves.
## Why It's Good For The Game

> Serrated bone shovels can be created with any kind of shovel now, not
just a spade (???)

Weird ass bug.

> Serrated bone shovels can be used in place of circular saw in most
surgeries.

It's serrated, it's cool, it's rare, it has a fast toolspeed.

> Added a duller (still deadly) variant of the serrated bone shovel as
coroner mail.

Very thematic for the coroner, should probably also be a heirloom item
but whatevs. Weaker so there's still a reason to seek out the OG.

> Autopsy scanners now act as advanced health analyzers on dead and
seemingly-dead people.

Scanning corpses is pretty important during surgery - it tells you how
much blood they have, organ damage, diseases... these things don't
appear in the surgical computer readout, which means the coroner has to
go out of his cave to pick up a boring light blue meatbag wound scanner.
This also incentivizes coroners to do their job by giving them something
cool that only works on dead bodies.

> Increased the force, throwforce, and wound bonus of inert ritual
knives and scythes.

These two options in the MortiDrobe are pretty frickin' badass,
especially with how SICK the Coroner looks with them, double especially
in combat.


![image](https://github.com/tgstation/tgstation/assets/53100513/98c6f8a5-3e5a-41a9-8a9c-cb6b82ecc0b8)

However, there's the large issue that as actual weapons they're really,
really weak. Not enough damage, when I use them in combat I both feel
badass but also get a nagging feeling in the back of my mind that I'm
intentionally gimping myself, and with only 10 damage I can *really*
feel it. I find it unfair that these are objectively worse than a
welding tool or even a Butcher's Cleaver when they're a lot more
involved to find, and scarce besides. These arguments apply equally to
the Wizard's ritual knife, and the scythe.

Additionally on the scythe, the crew really needs more good ghetto
weaponry that isn't the boring same ol' of baseball bats, spears,
cleavers... and making scythes useful is a great way to help bridge that
gap. They deal a satisfying amount of damage now, with the clear
downside, of course, being that they're bulky and hard to lug around.

> Coroner gloves can quickly apply medicine like nitrile gloves.

'Fast medicine' doesn't just cover sutures, it also covers medical gel.
Specifically, sterilizer gel. I find it annoying that the Coroner is
encouraged to give up his drip for the boring life-saver nitrile gloves,
because the difference in applying time really does make a difference -
it makes gel applying go from annoying to smooth, which is important
considering the whole purpose of sterilizer gel is to make surgeries go
faster. The Coroner has surgery and thus medical locker access to begin
with, so this isn't a balance problem, (and nitrile gloves are found by
the dozen anyways) especially with how rare the coroner gloves are.
## Changelog
:cl:
fix: Serrated bone shovels can be created with any kind of shovel now,
not just a spade (???)
add: Serrated bone shovels can be used in place of circular saw in most
surgeries.
add: Added a duller (still deadly) variant of the serrated bone shovel
as coroner mail.
add: Autopsy scanners now act as advanced health analyzers on dead and
seemingly-dead people.
add: Increased the force, throwforce, and wound bonus of inert ritual
knives and scythes.
add: Coroner gloves can quickly apply medicine like nitrile gloves.
/:cl:

---
## [EOBGames/tgstation](https://github.com/EOBGames/tgstation)@[721fd30837...](https://github.com/EOBGames/tgstation/commit/721fd308378dc6ef7595c1ea4b92d679ba723188)
#### Saturday 2023-08-12 12:26:18 by carlarctg

Heavily reworks and resprites first aid analyzers. (#76533)

## About The Pull Request

Heavily reworks and resprites first aid analyzers. They now display if
they're happy, sad, angry, or warning you! Also a 'pricking' animation.

First aid analyzers are now found in all basic and specialized medkits.
Toxin medkits get a new* disease analyzer. Miners get a miner-colored
one in their box.

Scanning yourself with a first aid analyzer will 'create a holo-image
with treatment instructions next to your wounds', doubling the speed of
treatment of scanned wounds!

Health analyzers now have a scanning sound, courtesy of CM.

Refactored some wound code to make treatment duration changes and
changes in the description of wounds easier.

Fixed a dummy parent feature of the health analyzer (Verbose mode)
showing up, uselessly, on the disease and first aid subtypes.

Surgical processors and slime scanners have recieved a similar resprite.
## Why It's Good For The Game

> Heavily reworks and resprites first aid analyzers. They now display if
they're happy, sad, angry, or warning you! Also a 'pricking' animation.

These things have long, long needed some sprite love. Displaying emotion
will make them have a lot more 'weight' to them, same with the prick.
The old, shitty spectrometer sprites have gone directly into the
dumpster.

> First aid analyzers are now found in all basic and specialized
medkits. Toxin medkits get a new* disease analyzer. Miners get a
miner-colored one in their box.

They have also needed some gameplay love! Placing them in these kits is
not going to be a massive game-changer when they were already easily
found around the station in emergency medkits, but it will fill up that
awkward empty slot.

> Scanning yourself with a first aid analyzer will 'create a holo-image
with treatment instructions next to your wounds', doubling the speed of
treatment of scanned wounds!

The biggest gameplay-impacting change in this PR, I *sincerely* believe
this is the perfect solution to first aid analyzers being completely
redundant with eyesight. This lets you/someone else scan your wounds to
speed up treatment, with a neat in-character reason for it -
'holo-images' appearing on your body, like penlights.

This will speed up wound treatment, but I believe that is for the best,
as currently treating wounds is so slow that half the time it's not
worth it (or more accurately, it doesn't feel worth it in comparison to
the effort you're putting in) and you're better off shrugging off minor
wounds. It will do so in a way that requires a modicum of effort, so
it's not just a flat buff across the land.

> Health analyzers and gene scanners now have a scanning sound, courtesy
of CM.

It's a neat sound that will make medbay feel more alive. First aid
analyzers get a beeboop instead.

> Surgical processors and slime scanners have recieved a similar
resprite.

IT'S SPRITE MANIA IN HERE
## Changelog
:cl:
Carlarc, Weird Orb
image: Heavily reworks and resprites first aid analyzers. They now
display if they're happy, sad, angry, or warning you! Also a 'pricking'
animation.
add: First aid analyzers are now found in all basic and specialized
medkits. Toxin medkits get a new* disease analyzer. Miners get a
miner-colored one in their box.
balance: Scanning yourself with a first aid analyzer will 'create a
holo-image with treatment instructions next to your wounds', doubling
the speed of treatment of scanned wounds!
sound: Health analyzers and gene scanners now have a scanning sound,
courtesy of CM.
refactor: Refactored some wound code to make treatment duration changes
and changes in the description of wounds easier.
fix: Fixed a dummy parent feature of the health analyzer (Verbose mode)
showing up, uselessly, on the disease and first aid subtypes.
image: Surgical processors and slime scanners have recieved a similar
resprite.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [EOBGames/tgstation](https://github.com/EOBGames/tgstation)@[a2c8cce535...](https://github.com/EOBGames/tgstation/commit/a2c8cce5359162a8a697ce109801ec268bf0c8a5)
#### Saturday 2023-08-12 12:26:18 by John Willard

Bilingual can now choose their language (#76609)

## About The Pull Request

This was one of the tradeoffs for removing other, more consistent
sources of languages, and was requested by Melbert among many others.
This does go against my wanted goal of decreasing the risk of
eavesdropping by other players through just magically knowing a
language, but it is an expensive quirk and it is in their medical
records, which makes it better than language encryption keys or silicon
just innately knowing them.

This also limits Bilingual to only roundstart languages (+Uncommon),
rather than being randomly selected from a list (that had very useless
ones like monkey, podpeople, and beachbum). This is mostly just for
modularity, I didn't want to make it look terrible code-wise and thought
this may be the optimal way to handle it.

This is also me going back on
https://github.com/tgstation/tgstation/pull/71773 - which I had closed
myself.

## Why It's Good For The Game

If we're gonna keep the Bilingual quirk, it might as well be something
players can choose the language of, it's their character and they should
be allowed to decide how their character is, and it is my fault that
this stupid compromise of "getting a random language" was made in the
first place. It never should've happened.
It now actually limits it to roundstart-only languages, so there's no
way you can spy on people who prepare in advance through becoming
podpeople, or monkeys, etc.

## Changelog

:cl:
balance: Bilingual quirk now lets you choose your language between ones
given to roundstart species.
balance: Foreigner and Bilingual are now mutually exclusive languages.
/:cl:

---
## [EOBGames/tgstation](https://github.com/EOBGames/tgstation)@[32afa856db...](https://github.com/EOBGames/tgstation/commit/32afa856dbb5bcc0a38bc48ee9f4b383c7ca0f86)
#### Saturday 2023-08-12 12:26:18 by John Willard

Makes cult leader handling work off of the Cult datum (#76556)

## About The Pull Request

Removes Cult master's datum, it's not handled by the Cultist itself,
using a helper to promote/demote people to leader.
In practice, the only way someone would be demoted is through Admins, so
this adds support for Admins to intervene in this Cult stuff if
necessary.

Moves cult objectives and cult team to their own files

Removes the cult master's status effect that constantly processes to
send a deathrattle, and instead moves it to a signal hooked to stat
change.

Also moves some things from ``get_antag_minds`` to checking the team,
which doesn't change anything in-game but it does help add the currently
non-functional support for several cult teams. Iunno.


https://github.com/tgstation/tgstation/assets/53777086/573a4f13-35e1-4f34-9952-62fed10b49c9

## Why It's Good For The Game

Having the cult leader be its own datum has actually been handled like
shit. To promote someone to cult leader, we currently make their current
cult datum silent, then remove it, and finally add the cult leader
datum. This means they lose their spells unless manually given back
post-promotion, which sucks (and also, no one has done yet, meaning they
just lose all their spells).
It also means there's a lot more snowflake things, did you know there's
a var to bypass converting mindshielded people? That's so cult masters
can be promoted by Cultists who were mindshielded, and they have to be
"ownable", that var is to bypass the check for mindshield to "convert"
them to leader cultist.

## Changelog

:cl:
fix: Cultists promoted to Leader no longer lose their spells (rip
whoever tried saving up blood rites)
admin: Admins can now force promote/demote people from Cult Leader if
necessary.
/:cl:

---
## [EOBGames/tgstation](https://github.com/EOBGames/tgstation)@[fc854e7076...](https://github.com/EOBGames/tgstation/commit/fc854e70760354181a049aa73f5a2ac06b0b8a49)
#### Saturday 2023-08-12 12:26:18 by Watermelon914

Removes TTS voice disable option (#76530)

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

Co-authored-by: Watermelon914 <3052169-Watermelon914@users.noreply.gitlab.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[2fd11cc8be...](https://github.com/TaleStation/TaleStation/commit/2fd11cc8beedaf08fab97dcae5c1826090588364)
#### Saturday 2023-08-12 12:40:44 by TaleStationBot

[MIRROR] [MDB IGNORE] Nukies Update 7: Hats (Also massive uplink standardization, weapon kits and ammo changes) (#7194)

Original PR: https://github.com/tgstation/tgstation/pull/77330
-----
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

---------

Co-authored-by: necromanceranne <40847847+necromanceranne@users.noreply.github.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[478bc1e68f...](https://github.com/TaleStation/TaleStation/commit/478bc1e68ff2f81a5f6f22774d3033712739b228)
#### Saturday 2023-08-12 12:40:44 by TaleStationBot

[MIRROR] [MDB IGNORE] Chen And Garry's Ice Cream: Ice Cream DLC (LIZARD APPROVED!) (#7183)

Original PR: https://github.com/tgstation/tgstation/pull/77174
-----
## About The Pull Request

Authored with help and love from Thalpy 

I scream for ice cream!!


![image](https://github.com/tgstation/tgstation/assets/10399117/db1e559b-7dab-499b-a076-8f12748ba2e8)

Introduces many new flavours of ice cream:
-Caramel
-Banana
-Lemon Sorbet
-Orange Creamsicle
-Peach (Limited Edition!)
-Cherry chip
-Korta Vanilla (made with lizard-friendly ingredients!)


![image](https://github.com/tgstation/tgstation/assets/10399117/99a87615-f55c-49be-8caf-2b1ac4c7f03f)

Korta Cones! Now too can Nanotrasen's sanitation staff enjoy the wonders
of ice cream!
You can also substitute custom ice cream flavours with korta milk!
Finally, the meaty ice cream lactose-intolerants asked for is in reach!

## Why It's Good For The Game

I always thought the ice cream vat could use more flavours. The custom
flavour besides, it isn't as intuitive to rename the cone and the added
variety is good. The lack of a banana flavour already was questionable.
All the ice cream flavours used a selection of five sprites, now it's
just one sprite and better supporting more additions.
Some of the flavours don't use milk! You can't do this with the custom
flavour, making it slightly more interesting.

## Changelog
:cl: YakumoChen, Thalpy
add: Chen And Garry's Ice Cream is proud to debut a wide selection of
cool new frozen treat flavours on a space station near you!
add: Chen And Garry's Ice Cream revolutionary Korta Cones allow our ice
cream vendors to profit off the lizard demographic like never before!
code: Ice cream flavours now are all greyscaled similarly to GAGs
/:cl:

---------

Co-authored-by: YakumoChen <king_yoshi42@yahoo.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[723ae170dd...](https://github.com/TaleStation/TaleStation/commit/723ae170dd959f622e8035c2464c03d3d6f3e624)
#### Saturday 2023-08-12 12:40:44 by TaleStationBot

[MIRROR] [MDB IGNORE] Dissection experiments are handled by autopsy surgery. Removes redundant dissection surgery. You can repeat an autopsy on someone who has come back to life. (#7193)

Original PR: https://github.com/tgstation/tgstation/pull/77386
-----
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

Co-authored-by: necromanceranne <40847847+necromanceranne@users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[65cd27a3ad...](https://github.com/TaleStation/TaleStation/commit/65cd27a3ad7f46a6d4db16da0fd0251f9aead27e)
#### Saturday 2023-08-12 12:41:12 by TaleStationBot

[MIRROR] [MDB IGNORE] resprites all soda cans, adds wellcheers juice (#7210)

Original PR: https://github.com/tgstation/tgstation/pull/77424
-----
## About The Pull Request
this one was a labor of love. all the existing soda cans have been
resprited, with the help of retlaw34 (new top palettes), Imaginos16 (new
top shapes, can palettes), and some original sprites done by Krysonism
(monkey energy, the 13 loko).
you can see the before and afters here: 

![image](https://github.com/tgstation/tgstation/assets/110322848/f23f0b06-d3b3-40dd-b0f9-353fb5864b92)
(now includes crushed cans, and inhands!)
let me know if there's any promotional stuff i should also include in
this PR, like if sol dry has a poster somewhere, and i'll go update that
with any changes made.

also adds a new drink, idea courtesy of YesterdaysPromise: 
wellcheers juice!

![image](https://github.com/tgstation/tgstation/assets/110322848/96c6d57a-79c3-4b70-8bd5-c8f3d1bbec41)
it will make you drowsy, and has a variable affect on your mood
if you are unhappy, it will deal stamina damage
if you are neutral, it will give you a mood boost
if you are happy, it will heal some brute damage

also, six packs of cans have been resprited. can i interest anyone in an
alamo? or just a space beer?

![image](https://github.com/tgstation/tgstation/assets/110322848/567d677b-d89b-4c52-b576-b15293aabf49)

## Why It's Good For The Game
old can sprites were _crusty_. it was nearly impossible to tell what
some of the logos were, and the palettes were dated as well. this tries
to keep the logo similar where possible, giving them new life where i
can, and sometimes reimagining them. the result is still internally
consistent, but much more polished.
## Changelog
:cl:
add: Added wellcheers, a contraband soda with various side effects.
image: resprites all cans in the drinks icon file
image: resprites the canholder sprite in storage.dmi
/:cl:

---------

Co-authored-by: Lamb <110322848+CoiledLamb@users.noreply.github.com>

---
## [sst-inc/Vexential-Inc.](https://github.com/sst-inc/Vexential-Inc.)@[b9ff2c11a5...](https://github.com/sst-inc/Vexential-Inc./commit/b9ff2c11a5d831fbdcea25366d43e4be04040fe9)
#### Saturday 2023-08-12 13:23:37 by mushroomthatcodes

calendar !!!!

fucking hell this shit is trying to make me kill myself but ya i made the fucking calendar

---
## [nikqo/Eden](https://github.com/nikqo/Eden)@[8873878d83...](https://github.com/nikqo/Eden/commit/8873878d83d92cb1688767a53a5e2d5680c97f64)
#### Saturday 2023-08-12 14:04:54 by nikqo

started unit testing and crud operations

added some uhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh tests for create_command in the commands table but thats honestly it i gotta overhaul a lot of shit which is a paoin in the ass. i doubt anyone reads these aynway. yeehaw

---
## [Arctic-Husky/space-station-14](https://github.com/Arctic-Husky/space-station-14)@[06747e0f7e...](https://github.com/Arctic-Husky/space-station-14/commit/06747e0f7e7d04cf87e63a359a3a86b1a35442cc)
#### Saturday 2023-08-12 14:28:30 by Emisse

some silly paintings and posters (#17872)

* webedit

* Update meta.json

* god is real hes here with us

* so true

* so truers rise

* worst meta.json ive seen in my life

* so true

---
## [icornelius/styles](https://github.com/icornelius/styles)@[1194e363eb...](https://github.com/icornelius/styles/commit/1194e363eb26ef6c09b4ab40647fe74cb15a7af9)
#### Saturday 2023-08-12 14:49:51 by icornelius

Releasing acm-sig-proceedings-long-author-list.csl acm-sig-proceedings.csl acta-palaeontologica-polonica.csl al-jamiah-journal-of-islamic-studies.csl american-journal-of-botany.csl american-society-for-horticultural-science.csl american-sociological-association.csl apa-6th-edition-no-ampersand.csl apa-6th-edition.csl apa-annotated-bibliography.csl apa-cv.csl apa-eu.csl apa-no-ampersand.csl apa-no-doi-no-issue.csl apa-no-initials.csl apa-numeric-superscript-brackets.csl apa-numeric-superscript.csl apa-old-doi-prefix.csl apa-single-spaced.csl apa-with-abstract.csl apa.csl arachnologische-mitteilungen.csl association-for-computational-linguistics.csl begell-house-apa.csl bern-university-of-applied-sciences-school-of-agricultural-forest-and-food-sciences-hafl.csl bibliothek-forschung-und-praxis.csl bio-protocol.csl bluebook-law-review.csl business-and-human-rights-journal.csl cardiff-university-harvard.csl chicago-annotated-bibliography.csl chicago-author-date.csl chicago-fullnote-bibliography-short-title-subsequent.csl chicago-fullnote-bibliography-with-ibid.csl chicago-fullnote-bibliography.csl chicago-library-list.csl chicago-note-bibliography-with-ibid.csl chicago-note-bibliography.csl citation-compass-apa-note.csl czech-journal-of-international-relations.csl dependent/consumption-and-society.csl dependent/critical-and-radical-social-work.csl dependent/emotions-and-society.csl dependent/european-journal-of-politics-and-gender.csl dependent/european-social-work-research.csl dependent/evidence-and-policy.csl dependent/families-relationships-and-societies.csl dependent/global-discourse.csl dependent/global-political-economy.csl dependent/global-social-challenges-journal.csl dependent/harvard-the-university-of-melbourne.csl dependent/international-journal-of-care-and-caring.csl dependent/jci-insight.csl dependent/journal-of-gender-based-violence.csl dependent/journal-of-poverty-and-social-justice.csl dependent/journal-of-psychosocial-studies.csl dependent/journal-of-public-finance-and-public-choice.csl dependent/justice-power-and-resistance.csl dependent/longitudinal-and-life-course-studies.csl dependent/magnetic-resonance-in-medicine.csl dependent/molecular-physics.csl dependent/monash-university-harvard.csl dependent/policy-and-politics.csl dependent/turabian-fullnote-bibliography.csl dependent/voluntary-sector-review.csl dependent/work-in-the-global-economy.csl duale-hochschule-baden-wurttemberg-department-of-international-business.csl ecosistemas.csl elsevier-american-chemical-society.csl energy-research-and-social-science.csl environmental-and-engineering-geoscience.csl european-review-of-agricultural-economics.csl food-and-agriculture-organization-of-the-united-nations-numeric.csl fundamental-and-applied-limnology.csl geographie-et-cultures.csl german-council-of-economic-experts.csl harvard-anglia-ruskin-university.csl harvard-deakin-university.csl harvard-stellenbosch-university.csl harvard-university-of-the-west-of-england.csl harvard-xi-an-jiaotong-liverpool-university.csl haute-ecole-de-gestion-de-geneve-iso-690.csl hochschule-fur-soziale-arbeit-fhnw.csl howard-hughes-medical-institute.csl iainutuban-tarbiyah.csl ieee-with-url.csl ieee.csl isara-iso-690.csl iso690-author-date-es.csl journal-of-dental-traumatology.csl journal-of-emerging-investigators.csl journal-of-experimental-botany.csl journal-of-human-nutrition-and-dietetics.csl journal-of-neolithic-archaeology.csl journal-of-paleontology.csl journal-of-the-american-philosophical-association.csl journal-of-the-marine-biological-association-of-the-united-kingdom.csl jurnal-teknik-mesin-indonesia.csl la-nouvelle-revue-du-travail.csl lethaia.csl masarykova-univerzita-pravnicka-fakulta.csl medizinische-universitat-innsbruck-vancouver.csl microbiome-research-reports.csl modern-language-association.csl mots.csl netherlands-journal-of-geosciences-geologie-en-mijnbouw.csl norsk-apa-manual-note.csl norsk-apa-manual.csl norsk-henvisningsstandard-for-rettsvitenskapelige-tekster.csl north-pacific-anadromous-fish-commission-bulletin.csl offa.csl open-window.csl organization-studies.csl palaeontology.csl paleobiology.csl polish-archives-of-internal-medicine.csl publicatiewijzer-voor-de-archeologie.csl retina.csl silva-fennica.csl slovensko-drustvo-za-medicinsko-informatiko.csl springer-vancouver-brackets.csl stanovnistvo.csl studii-teologice.csl taylor-and-francis-aip.csl technische-universitat-dresden-betriebswirtschaftslehre-rechnungswesen-controlling.csl the-accounting-review.csl the-journal-of-clinical-investigation.csl the-quarterly-journal-of-economics.csl trames.csl travail-et-emploi.csl turabian-fullnote-bibliography-8th-edition.csl turcica.csl ucl-university-college-apa.csl uni-fribourg-theologie.csl united-states-international-trade-commission.csl universitat-basel-iberoromanistik.csl universitat-bern-institut-fur-sozialanthropologie.csl universite-de-bordeaux-ecole-doctorale-de-droit.csl universite-du-quebec-a-montreal-etudes-litteraires-et-semiologie.csl universite-du-quebec-a-montreal.csl university-of-gothenburg-apa-7th-edition-swedish-legislations.csl university-of-pretoria-harvard-theology-religion.csl uppsala-university-library-harvard.csl van-yuzuncu-yil-universitesi-fen-bilimleri-enstitusu.csl vancouver.csl veterinary-clinical-pathology.csl wiley-was.csl zitierguide-leitfaden-zum-fachgerechten-zitieren-in-rechtswissenschaftlichen-arbeiten.csl zoological-journal-of-the-linnean-society.csl dependent/energy-research-and-social-science.csl dependent/retina.csl harvard-the-university-of-melbourne.csl jci-insight.csl magnetic-resonance-in-medicine.csl monash-university-harvard.csl turabian-fullnote-bibliography.csl

---
## [Cenrus/Daedalus-Dock](https://github.com/Cenrus/Daedalus-Dock)@[8f0512b923...](https://github.com/Cenrus/Daedalus-Dock/commit/8f0512b92377a891a728e83d1d269820e4c1d5f8)
#### Saturday 2023-08-12 15:13:51 by Kapu1178

Spatialgridports (#352)

* adds an error message to movables not being removed from the grid... again (#75161)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

I swear i didnt fail at this like 3 times i tested it this time.

adds a descriptive error of what spatial grid cells a movable is stuck
in, and in what channels. This only runs during unit tests. hopefully
this should be enough information to go off of to fix the spurious
cockroach error. if its not then i can try tracking all grid cell
changes during unit tests.
error looks like this:
```
[2023-05-03 04:16:34.009] runtime error: /mob/living/trolls_the_maintainer instance, which is in nullspace, and thus not be within the contents of any spatial grid cell, was in the contents of 2 spatial grid cells when it was only supposed to be in one! within the contents of the following cells: {(221, 119, 11), within channels: hearing}, {coords: (136, 136, 14), within channels: hearing}. (code/controllers/subsystem/spatial_gridmap.dm:581)
```
for something located in nullspace but still in the contents of >0 cells
and:
```
runtime error: /mob/living/trolls_the_maintainer instance, which is supposed to only be in the contents of a spatial grid cell at coords: (136, 136, 14), was in the contents of 6 spatial grid cells when it was only supposed to be in one! within the contents of the following cells: {(68, 153, 2), within channels: hearing}, {coords: (221, 170, 3), within channels: hearing}, {coords: (255, 153, 11), within channels: hearing}, {coords: (170, 238, 13), within channels: hearing}, {coords: (204, 119, 14), within channels: hearing}, {coords: (136, 136, 14), within channels: hearing}.
```
if its not in nullspace but its within more than 1 grid cell.

the coordinates here are translated from the index of the given cell to
world coordinates.

mothblocks has been standing outside my house for weeks i am fearing for
my life

---------

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

* fixes contents not being removed from the spatial grid when deleted during movement between 2 grid cells (#75658)

## About The Pull Request
fixes the flaky test reports for cockroaches being stuck in the spatial
grid (which mothblocks seems to have closed all of)

cockroaches get deleted when they die, so theres a spurious unit test
failure where if a cockroach is on a tile in grid cell A and moves to a
lava tile in grid cell B, they will get killed when lava.Entered() is
called, then deleted, and when /atom/movable/Destroy() is called we try
to take them out of grid cell B (because their loc is the lava tile) but
they were never added to that cell yet because their movement never
finished, so that doesnt do anything. THEN moveToNullspace() is called,
that movement finishes before the first movement, and then in
Moved(old_loc = lava turf) we try to remove it from grid cell B which
again doesnt work, and then the first movements Moved(old_loc = original
turf) is called where we can actually remove them from the correct grid
cell, except we cant because in exit_cell() we subtract
`old_target.important_recursive_contents[channel]` from the cells
content lists, and since the target is deleted by this point it doesnt
have important_recursive_contents. so the fix here is changing this so
it subtracts `old_target.important_recursive_contents?[type] ||
old_target` instead, which works if the target is deleted.

also fixes some Entered() overrides that dont call parent and improves
documentation on spatial grid defines
## Why It's Good For The Game
fixes it without needing the change_loc() setter

* update for us

* missed this

---------

Co-authored-by: Kylerace <kylerlumpkin1@gmail.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [Bjarl/Shiptest](https://github.com/Bjarl/Shiptest)@[1b315a616f...](https://github.com/Bjarl/Shiptest/commit/1b315a616ff24e3f1f92c791e4df4dc43ca9aad6)
#### Saturday 2023-08-12 15:51:34 by Thedragmeme

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
## [DGamerL/Paradise](https://github.com/DGamerL/Paradise)@[a3dc32cf34...](https://github.com/DGamerL/Paradise/commit/a3dc32cf344dbd441e85f6cbb694b166dc1f5e4b)
#### Saturday 2023-08-12 17:49:18 by ATP-Engineer

Fixes issue where Turret Control sprites arent actually updated in previous PR (#21538)

* Removes actual turret file

FUCK

* Fixes turret controllers not actually being changed

GOD DAMNIT.

---
## [Geremia/AquinasOperaOmnia](https://github.com/Geremia/AquinasOperaOmnia)@[9381163867...](https://github.com/Geremia/AquinasOperaOmnia/commit/9381163867c651955f5fe1fe30f906f154e98697)
#### Saturday 2023-08-12 18:27:00 by Eric Wong

good it attained -> good is attained
acu*vity -> activity
plabsible -> plausible
the,other -> the other
Rut the -> But the
othex -> other
Ile -> The, or He
be cause every -> because every
life' -> life
toolive -> to live
unchgnueable -> unchangeable
Aristotlb -> Aristotle
frienship -> friendship
goodwillthis -> goodwill this
view& -> view
sorrowis -> sorrow is
seeme’ -> seems’
mat enjoy -> man enjoy
ch95en -> chosen
Ncxt -> Next
.from -> . From or from
activityas -> activity as
.consequently -> , consequently

admit,of -> admit of

capacityis -> capacity is
activity:s -> activity is
appearse -> appears
Ichief -> chief
).we -> ), we
fat this -> that this
wisdom.,This -> wisdom. This
ultimqte -> ultimate
[a-z]q[a-pr-tv-z] -> case by case fixes for q OCR

enerdies -> enemies
lie lives -> he lives
of -actions -> of actions
conterLplation -> contemplation

---
## [mctaylors/Boyfriend-CSharp](https://github.com/mctaylors/Boyfriend-CSharp)@[940f2e64a0...](https://github.com/mctaylors/Boyfriend-CSharp/commit/940f2e64a0bf065acf07add976e27a61daef730d)
#### Saturday 2023-08-12 18:40:12 by Macintosh II

Add soundtracks from different games (#74)

This PR adds some soundtracks from five different games to the bot's
listening activity.

List of soundtracks added:
- Jukio Kallio, Daniel Hagström - Fall 'n' Roll (Fall Guys)
- SCATTLE - Hypertension (Super Meat Boy)
- KEYGEN CHURCH - Tenebre Rosso Sangue (ULTRAKILL)
- Chipzel - Swing Me Another 6 (Dicey Dungeons)
- ~Floex - The Glasshouse With Butterfly (Machinarium)~
- Noisecream - Mist of Rage (My Friend Pedro)

---
## [awtybots/FRC-2023-Offseason](https://github.com/awtybots/FRC-2023-Offseason)@[bbf7085678...](https://github.com/awtybots/FRC-2023-Offseason/commit/bbf7085678bacd5083d0862aeef1f8b1d49db336)
#### Saturday 2023-08-12 18:42:33 by 24cirinom

PID Tuning for Improved Shooter Performance and Formal Apology for Inappropriate Previous Commit Message

This commit comes with a two-fold purpose; primarily, it includes the PID tuning for our shooter that will certainly improve its performance and efficiency. The changes should lead to more accurate shooting and an overall improvement in our team's performance.

However, before discussing the technical details, there's another matter that needs to be addressed. In my last commit, I used a message that was entirely inappropriate, insensitive, and offensive - "ABOUT AS BIG AS MY LAST PUSH INTO YOUR MOM". I wish to extend my deepest and sincerest apologies for this comment.

Being part of this team, I ought to uphold a level of respect, dignity, and maturity; but my tactless message failed to reflect any of these values. Not only did it breach the professional boundaries of our team, but it spoke poorly of the respect we must harbor for the people in our lives, especially our families.

I let the pressure of deadlines cloud my judgment and I allowed immature humor to seep into our workspace, a place that should be inclusive, respectful, and conducive to healthy communication. These are not justifications for my actions. I take full responsibility for my lapse in judgment.

Looking back, I'm saddened that I allowed this joke to undermine the serious nature of our work, and the respect we have always maintained within our team. I humbly apologize to each member of our team who may have felt insulted or disrespected due to my inappropriate comment.

To ensure that this situation does not set a precedent, it's important for us to remember that the language we use in our commit messages reflects not just on us as individuals, but on our organization and our project as well. We should strive to maintain our professionalism and respect, particularly in our communication.

Moving forward, I commit to maintaining a respectful and considerate tone in all our interactions, and especially in our commit messages. I would also deeply appreciate your understanding and forgiveness.

Switching gears, concerning the technical aspect of the commit, I have adjusted the PID values for the shooter. I tuned the proportional, integral, and derivative gains to optimize the shooting performance. You should notice a significant improvement in targeted shots.

Again, I wholeheartedly apologize for my previous transgression and I hope that we can foster a cordial and productive environment going forward. Please review the PID adjustments for the shooter and provide any feedback.

Thank you for your understanding.

---
## [Danielkaas94/DTAP](https://github.com/Danielkaas94/DTAP)@[6307e0269e...](https://github.com/Danielkaas94/DTAP/commit/6307e0269e4ebb120b32afce3fc299e60bd076cd)
#### Saturday 2023-08-12 18:54:42 by Daniel Kaas Bundgaard Jørgensen

One Day ☮️🕊️

Sometimes I lay under the moon
And thank God I'm breathin'
Then I pray, "Don't take me soon
'Cause I am here for a reason."

Sometimes in my tears I drown
But I never let it get me down
So when negativity surrounds
I know some day it'll all turn around because

All my life I've been waitin' for
I've been prayin' for
For the people to say
That we don't wanna fight no more
There'll be no more war
And our children will play

One day, one day, one day, oh
One day, one day, one day, oh

It's not about win or lose, 'cause we all lose
When they feed on the souls of the innocent
Blood-drenched pavement
Keep on movin' though the waters stay ragin'

In this maze
You can lose your way, your way
It might drive you crazy but
Don't let it faze you, no way, no way!

Sometimes in my tears I drown
But I never let it get me down
So when negativity surrounds
I know some day it'll all turn around because

All my life I've been waitin' for
I've been prayin' for
For the people to say
That we don't wanna fight no more
There'll be no more war
And our children will play

One day, one day, one day, oh
One day, one day, one day, oh

One day this all will change, treat people the same
Stop with the violence, down with the hate
One day we'll all be free, and proud to be
Under the same sun, singin' songs of freedom like

Why-ohh! (One day, one day) why-oh, oh, oh!
Why-ohh! (One day, one day) why-oh, oh, oh!

All my life I've been waitin' for
I've been prayin' for
For the people to say
That we don't wanna fight no more
There'll be no more war
And our children will play

One day, one day, one day, oh
One day, one day, one day, oh

---
## [Philasande-Ngubo/Using-input-and-message-Dialogs-Java](https://github.com/Philasande-Ngubo/Using-input-and-message-Dialogs-Java)@[d379990210...](https://github.com/Philasande-Ngubo/Using-input-and-message-Dialogs-Java/commit/d3799902108d224de731af34435713c3967a11d5)
#### Saturday 2023-08-12 18:57:55 by Philasande Ngubo

Add files via upload

This a simple program written in Java. It is my own introduction to graphical user interface.
This program prompts for a name with an input dialog and greet the user according to the time of the day.
For this project's sake.
5 -10 is morning.
11is day.
12-16 is afternoon.
17 - 20 evening
21 - 4 is Night.

This program uses JOptionPane for Dialog and calendar to get system time.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[7f1d53e719...](https://github.com/tgstation/tgstation/commit/7f1d53e719d8d097e8af41b9b80a829b84b105ce)
#### Saturday 2023-08-12 19:15:30 by Ben10Omintrix

convert the eyeball a basic monster (#77411)

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

---
## [HaultyAnonie/Foundation-19](https://github.com/HaultyAnonie/Foundation-19)@[b4642dc835...](https://github.com/HaultyAnonie/Foundation-19/commit/b4642dc835dc801d801fd543cfd34bd44ca23929)
#### Saturday 2023-08-12 19:21:49 by cheesePizza2

Armor improvements (#1251)

* the fixes

* FUCK YOU

* few more improvements

* bring em back

* fuck you

---
## [bplaat/serenity](https://github.com/bplaat/serenity)@[8d17ede197...](https://github.com/bplaat/serenity/commit/8d17ede1977517fb0556857e042bd4abd7174a7b)
#### Saturday 2023-08-12 19:24:19 by Xexxa

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
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[b22ff1a4eb...](https://github.com/tgstation/tgstation/commit/b22ff1a4ebfd0a1dd1b75d6979edc73e6f4556b2)
#### Saturday 2023-08-12 19:41:15 by Sealed101

Laser pointer update: Shining Through Walls Edition (feat. fixes!) (#77007)

# _PR PSA_


![augh](https://github.com/tgstation/tgstation/assets/75863639/6dc87fc7-65a3-4b7c-9b8d-a1432cacbe93)


## About The Pull Request
Cleans up code for laser pointers, fixing some bugs like the
forever-charging state or affecting dead cats along the way.
Remaining charge is now available upon examine.
Canonizes #45834 by implementing an upgrade to the laser pointers:
installing a bluespace crystal into a laser with tier 3 or higher laser
diode lets it shine through walls. Using an upgraded laser uses twice
the charge of a normal one. Of course, you can only shine it on
something if you can see the target behind the wall, like via x-ray or
thermals. Mesons don't count, however.
If one tries to jam a crystal into a pointer with a tier 1/2 laser (or a
tier 1/2 laser in a pointer with an installed crystal), _something_ will
get teleported, crushing the crystal.
You can uninstall the crystal with wirecutters or a hemostat. The
pointer will _hint_ on closer examination (`examine_more`) at a
possibility of a crystal being installed if you upgrade the laser
(different messages for tier 1/2/3,4).
Removes one stupid 1% increase for a recharge chance per process tick if
your laser was in a full recharge state because it was insignificant and
irrelevant.

i've had a branch for this for almost 9 months and i was always laying
it off for some day later. today i just completely fucked the branch.
whoops. i'm not even sure at this point what else did i fix while here,
double whoops

## Why It's Good For The Game
Closes #45834 - Canonizes a bug into a feature.
Fixes #77003 - lol
Cleaner code, possibly more robust even.
Seeing the remaining charge was not available at all and the only hint
was when you tried shining the pointer on something. That sucks.

## Changelog
:cl:
add: you can upgrade laser pointers with a bluespace crystal to let them
shine through walls at double the power cost, if the laser in the
pointer is of tier 3 or higher.
qol: laser pointer charge can be seen by examining it
fix: fixed laser pointers luring dead cats when shone upon
code: laser pointer code cleaned up a tad
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Devoleksiy/hestiacp](https://github.com/Devoleksiy/hestiacp)@[365dab5670...](https://github.com/Devoleksiy/hestiacp/commit/365dab5670f6d1a862858be01638072eeb2ec1db)
#### Saturday 2023-08-12 20:18:29 by divinity76

Use secure RNG to generate passwords (#2726)

* use secure rng to generate passwords

quoting MDN:
>Math.random() does not provide cryptographically secure random numbers. Do not use them for anything related to security. Use the Web Crypto API instead

My rng is kinda shitty, i know there is some fast way to cut down higher digits to get a digit in range without introducing bias, but i also know that other people have introduced bias by trying to do that on an initially secure rng and getting it wrong (iirc it's discussed here? https://www.youtube.com/watch?v=LDPMpc-ENqY - been years since i saw the talk, but i know Lavavej discussed it in one of his presentations, i think it was that one)  , but anyway this is fast enough, and secure.

* shorter name

* randomString2 / centralize js string generation

* missed 2

---
## [Dev-msm8953/kernel_xiaomi_msm8953](https://github.com/Dev-msm8953/kernel_xiaomi_msm8953)@[56b7bfadd0...](https://github.com/Dev-msm8953/kernel_xiaomi_msm8953/commit/56b7bfadd02f3b00a50165cfbfb033ab476525f0)
#### Saturday 2023-08-12 20:21:44 by Angelo G. Del Regno

Merge: Performance improvements.

This patchset brings some performance improvements and the addition of the LZO-RLE
algorithm to the kernel, also usable in zram (yup, tested, works but LZ4 is still ok for us).

The main performance improvement is for SWAP space: the locking has changed and
the swap cache is now split in 64MB trunks.
This gives us a reduction of the median page fault latency of 375%, from 15uS to 4uS,
and an improvement of 192% on the swap throughput (this includes "virtual" swap
devices, like zRAM!). The real world user experience improvement of this on a mobile
device is seen after a day or two of usage, where it usually starts losing just a little
performance due to the large amount of apps kept open in background: now I cannot
notice any more performance loss and the user experience is now basically the same as
if the phone was in its first 2 hours of boot life.

Other performance improvements include, in short:

    UDP v4/v6: 10% more performance on single RX queue
    Userspace applications will be faster when checking running time of threads
    2-5% improvements on heavy multipliers (yeah, not a lot, but was totally free...)
    Improvements on rare conditions during sparsetruncate of about 0.3% to a
    way more rare around 20% improvement (that's never gonna happen, but there
    is no performance drop anywhere).

Tested on SoMC Tama Akatsuki RoW

This was taken from
Repo:
https://github.com/sonyxperiadev/kernel
PR: 2039 ([2.3.2.r1.4] Performance improvements)

Signed-off-by: TogoFire <italomellopereira@gmail.com>
Change-Id: I929d9483d7d0562986facc5037e56bd7c630be88

---
## [petre-symfony/symfony-asset-mapper-2023](https://github.com/petre-symfony/symfony-asset-mapper-2023)@[9dfdc38485...](https://github.com/petre-symfony/symfony-asset-mapper-2023/commit/9dfdc384859327c76d89fa3aa3de622d5f2b7a56)
#### Saturday 2023-08-12 20:40:43 by Petre Ro

12.3 How our Controllers are Registered
 - Okay, so we're loading this loader.js file, and we can see that over here. In your browser, refresh... go to your Network tools, and search for "loader". There it is! Open this up in a new tab.

 This code has functions to start the Stimulus application and register the controllers from our app - like hello_controller.js. But... wait. This is just a hard-coded file. How is it able to dynamically find and load the files that live inside our assets/controllers/ directory?

 The key is on top: import, isApplicationDebug, eagerControllers, lazyControllers from ./controllers.js. This... is a bit of magic. Go back to the Network tools and search for "controllers"... there it is - controllers.js. Open this new tab. Woh! It has import controller_0 from ../../controllers/hello_controller.js, which it then exports to a variable called eagerControllers.

 This file is crafted dynamically by the bundle. If we look down in the vendor/ directory, loader.js is a nice static file. But if you look at controllers.js, it doesn't look like at all like what we have in the browser! When this file is served, AssetMapper intercepts it, looks inside of our assets/controllers/ directory, finds all the controllers there, and then returns dynamic contents based on these.

 Watch. Create another file called goodbye-controller.js (you can use dashes or underscores). Change the text to Goodbye controller./bin/console cache:clear

 You might expect that, when we refresh the file, we'll see the new controller pop in here. And you're almost right. What really happens is... nothing! No change! Or you might even get a 404 error. That's because the content of this file just changed and so the hash will also change. We're looking at an out-of-date version of the file!

 Back on the site, if we refresh, we should see a new file with a new hash. We don't... due to a caching bug which has already been fixed. To work around that, I'll run:

  php bin/console cache:clear
 Then go refresh. Now I see that this has a different file name, and the contents have dynamically changed to include goodbye-controller.js!

S o there you have it, the thrilling journey into the heart of how Stimulus and AssetMapper became best friends. bootstrap.js loads a file that starts Stimulus... and that automatically loads everything inside the assets/controllers/ directory... as well as any 3rd party UX packages in assets/controllers.json. Let's talk about those 3rd party packages next.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[31f1924324...](https://github.com/tgstation/tgstation/commit/31f1924324b04086f24034aaf754d5f85cb595a8)
#### Saturday 2023-08-12 21:35:27 by san7890

Refactors Morphs into Basic Mobs (there is now a swag action for morphification) (#77503)

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

---
## [UnFamousSoul/VEGA](https://github.com/UnFamousSoul/VEGA)@[1dd4e24dc1...](https://github.com/UnFamousSoul/VEGA/commit/1dd4e24dc1248376249f429184754b1cadabd633)
#### Saturday 2023-08-12 21:58:36 by UFS

Update DOC.md

Another small text edit

Hey guys, did you know that in terms of male human and female Pokémon breeding, Vaporeon is the most compatible Pokémon for humans? Not only are they in the field egg group, which is mostly comprised of mammals, Vaporeon are an average of 3”03’ tall and 63.9 pounds, this means they’re large enough to be able handle human dicks, and with their impressive Base Stats for HP and access to Acid Armor, you can be rough with one. Due to their mostly water based biology, there’s no doubt in my mind that an aroused Vaporeon would be incredibly wet, so wet that you could easily have sex with one for hours without getting sore. They can also learn the moves Attract, Baby-Doll Eyes, Captivate, Charm, and Tail Whip, along with not having fur to hide nipples, so it’d be incredibly easy for one to get you in the mood. With their abilities Water Absorb and Hydration, they can easily recover from fatigue with enough water. No other Pokémon comes close to this level of compatibility. Also, fun fact, if you pull out enough, you can make your Vaporeon turn white. Vaporeon is literally built for human dick. Ungodly defense stat+high HP pool+Acid Armor means it can take cock all day, all shapes and sizes and still come for more

---
## [TSS-sniper/Text_Generation_using_LSTM](https://github.com/TSS-sniper/Text_Generation_using_LSTM)@[f4b99e7533...](https://github.com/TSS-sniper/Text_Generation_using_LSTM/commit/f4b99e75337a2d5c111dabaa42dee102de24875d)
#### Saturday 2023-08-12 22:00:58 by Tarun Sheoran

Add files via upload

This is the Text Corpus on which the Text Generation model is trained upon. It comprises of the first 5 parts of a story "The Enemy" written by Pearl Sydenstricker Buck. The story revolves around a Japanese surgeon whose name is Sadao. He studies in America, marries a Japanese girl named Hana there and comes back to Japan to settle down. World War II broke during that time. All the doctors were under the obligation to go to the Japanese army. However, Sadao stayed back with an old general. As the old general was ailing, he was in need of Sadao. However, an American Navy man finds his way into Sadao’s life. As the soldier was not well, Sadao offers him medical help. Sadao was not willing to help the enemy but he does that anyway. He knows the risk of helping the enemy. Due to this, Sadao conspires to kill the soldier in his sleep. However, Sadao decides not to do so because of humanity.

---
## [Sh4dow8080/cfx-luaparse](https://github.com/Sh4dow8080/cfx-luaparse)@[ddc18d6b97...](https://github.com/Sh4dow8080/cfx-luaparse/commit/ddc18d6b97ca98cc0a974e9d1ff3999070d84bb6)
#### Saturday 2023-08-12 23:25:07 by Sh4dow8080

Fixed my late night shitty ass check for compileTimeJenkins, holy shit

---
## [JimFlannigan1087/UACDR-Halloween-Hack](https://github.com/JimFlannigan1087/UACDR-Halloween-Hack)@[e35902597c...](https://github.com/JimFlannigan1087/UACDR-Halloween-Hack/commit/e35902597ce6d51efadf8799ef849bdc7795fff0)
#### Saturday 2023-08-12 23:33:41 by Jim Flannigan

ok im a fucking retard

I forgot to set powerupduration tro like 5 bazillion years for my level up powerups, and I was wondering why I kept losing that shit

---

