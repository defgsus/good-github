## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-08-26](docs/good-messages/2023/2023-08-26.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,906,434 were push events containing 2,607,725 commit messages that amount to 150,117,069 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 56 messages:


## [NeatNerdPrime/linux](https://github.com/NeatNerdPrime/linux)@[8b9c1cc041...](https://github.com/NeatNerdPrime/linux/commit/8b9c1cc0418a43196477083e7082568e7a4c9418)
#### Saturday 2023-08-26 00:02:51 by David Hildenbrand

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
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[0dd3e66aef...](https://github.com/necromanceranne/tgstation/commit/0dd3e66aefa2a61cb4e78482273958c1d09f8295)
#### Saturday 2023-08-26 00:29:04 by Vekter

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
## [shorthills-ai/langchain](https://github.com/shorthills-ai/langchain)@[d57d08fd01...](https://github.com/shorthills-ai/langchain/commit/d57d08fd01e05889af4e59fa3577c824de6df09d)
#### Saturday 2023-08-26 00:52:24 by nikhilkjha

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
## [eltociear/codecov-api](https://github.com/eltociear/codecov-api)@[e2c6b1c425...](https://github.com/eltociear/codecov-api/commit/e2c6b1c425cac66f0d422bd5692c7aae4cc46b61)
#### Saturday 2023-08-26 00:53:20 by Giovanni M Guidini

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
## [Sonic121x/Skyrat-tg](https://github.com/Sonic121x/Skyrat-tg)@[d7542fb5e3...](https://github.com/Sonic121x/Skyrat-tg/commit/d7542fb5e3a73383b5b09f2d8758d0511466626f)
#### Saturday 2023-08-26 00:56:33 by SkyratBot

[MIRROR] [no gbp] Adds missing chat feedback to watcher abilities [MDB IGNORE] (#23212)

* [no gbp] Adds missing chat feedback to watcher abilities (#77700)

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

* [no gbp] Adds missing chat feedback to watcher abilities

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [CoiledLamb/lorbstation](https://github.com/CoiledLamb/lorbstation)@[7f1d53e719...](https://github.com/CoiledLamb/lorbstation/commit/7f1d53e719d8d097e8af41b9b80a829b84b105ce)
#### Saturday 2023-08-26 01:05:48 by Ben10Omintrix

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
## [CoiledLamb/lorbstation](https://github.com/CoiledLamb/lorbstation)@[b22ff1a4eb...](https://github.com/CoiledLamb/lorbstation/commit/b22ff1a4ebfd0a1dd1b75d6979edc73e6f4556b2)
#### Saturday 2023-08-26 01:05:48 by Sealed101

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
## [vincentiusvin/tgstation](https://github.com/vincentiusvin/tgstation)@[0d769e0ffa...](https://github.com/vincentiusvin/tgstation/commit/0d769e0ffaaa2b0f2be2edb9659c233860420ec1)
#### Saturday 2023-08-26 01:13:51 by Jacquerel

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
## [YakaryBovine/WarcraftLegacies-Fork](https://github.com/YakaryBovine/WarcraftLegacies-Fork)@[5c43577cce...](https://github.com/YakaryBovine/WarcraftLegacies-Fork/commit/5c43577cce48c18eecc9a0d6d501e64a1849d105)
#### Saturday 2023-08-26 01:19:47 by Technopig1992

3.6.2 balance changes multiple factions (#2027)

* Sentinels Changes 3.6.2

Chimaera’s now start with the Lightning Barrage ability.
Lightning Barrage level 1 attack speed increase reduced 250%>150%.
Lighting Barrage can now be upgraded.
Lighting Barrage upgrade cost reduced.
Chimaera attack speed increased 2.6>2.4.

* Goblin changes for 3.6.2

Assault Tank damage decreased 60>55.
Added 2 Improved Rocket Towers to Goblin starting base.
Added 1 Rocket Tower to Goblin starting base.
Added 1 Burrow to Goblin starting base.
Personal Tank mana increased 0>1300.
Personal Tank starting mana increased 250>350..
Siege Walker Attack 1 damage base reduced 73>66.
Siege Walker Attack 1 cooldown time increased 2>2.1.
Siege Walker Attack 2 damage base reduced 35>31.
Siege Walker Attack 2 cooldown time increased 1.5>1.6.
Siege Walkers now have the Overflow ability.

* Frostwolf changes 3.6.2

Batriders gold cost increased 13>15.
Batriders now start with the Liquid Fire ability.
New upgrade for Batrider, Airborne Toxins 125g, 50w.
Unstable Concoction primary damage reduced 700>400.
Unstable Concoction splash damage reduced 200>100.

* Kul Tiras changes 3.6.2

Katherine exp reward lowered
Old Hatreds quest experience reward reduced 5000>4000.
Old Hatreds quest requirement changed to be outside of Hellfire Citadel instead of Nethergarde.
Meradith Waycrest starting level reduced 6>5.
The High Bank quest gold reward reduced 700>450.
The High Bank quest experience reward reduced 3000>2000.

* Ironforge changes 3.6.2

Storming Brew ability area of effect reduced 600>125.
Storming Brew cooldown reduced 45>30.
Storming Brew hit points gained reduced 125>100.
Storming Brew mana cost reduced 100>75.
Reduced Rifleman damage sides per die 6>5.
Reduced Riflemen number of dice 3>2.
Rifleman spell and magic resistance reduced 30%>15%.
Adjusted Aeries Peak so units no longer get stuck.
Aeries Peak is now locked until turn 15.
Falstad Wildhammer’s starting level increased 4>8.
Dreadnought lumber cost reduced 800>600.
War Golem lumber cost reduced 250>150.

* Stormwind changes 3.6.2

Increase Pikeman gold cost
Galen Trollbane's starting level increased 4>8.
Pikeman Magic resistance reduced 20%>10%.
Safegaurd ability Magic and Spell resistance reduced 95%>85%.
Safeguard ability Piercing resistance reduced 95%>80%.
Stormwind Champion ability order corrected.
Stormgaurde now locked until turn 15.
Inner Fire buffed
Damage increased by 10%>15%
Defense increased 5>6
Mana cost 35>25

* Amendments for 3.6.2

Removed Personal Tank changes
Moved Fel Horde Treasury closer into region to prevent TK when Sunfury is picked.
Falstad level 4>8
Galen level 4>8

* Quel'Thalas changes 3.6.2

Outpost added in hinterlands.
Quel'Danil lodge moved to north eastern Hinterlands.
Quel'Danil Lodge food produced 10>45.

Misc
Jaina's Sanctum food produced 10>45.
Violet Citadel rotated to face the gate.
Added some rocks by the right most Anderhal bridge in an attempt to stop Plague Cauldron's spawning there.

* Dalaran changes 3.6.2

Reduced level of Death Revenant 9>7.
Slow ability level 2 Attack Speed reduction decreased  90%>70%.
Slow ability level 2 Movement Speed reduction decreased 70%>50%.
Removed Durnholde Improved Creep Guard Tower
Added Durnholde Creep Guard Tower.
Jaina’s Sanctum total food produced increased 10>45.
Archmage Antonidas base hit points reduced 600>300.
Archmage Antonidas' strength per level increased 1.7>1.8.

* Veteran Footman Buffs

Veteran Footman reworked:
Perfect Defend now gives 15% magic resistance.
Base attack increased 25>27
Base HP increased 800>825
Changed Combat Experience to Veterans Insight

Misc
Fixed ATCBTN for Invoke Spiders ability
Changed Minor Holy Light to crimson renewal with new art and icon.

---
## [Rlzt/rlzt.github.io](https://github.com/Rlzt/rlzt.github.io)@[cdaded976f...](https://github.com/Rlzt/rlzt.github.io/commit/cdaded976f80eca54d36619ec1ef9b50a1d2e891)
#### Saturday 2023-08-26 01:22:39 by wuid

Added Random Chrome Extension Idea Picker. 

holy shit ikr long ass name

Signed-off-by: wuid <125801210+Rlzt@users.noreply.github.com>

---
## [vinylspiders/tgstation](https://github.com/vinylspiders/tgstation)@[3645fa7d89...](https://github.com/vinylspiders/tgstation/commit/3645fa7d8956bed2d3ebff86b072f8b9544d383d)
#### Saturday 2023-08-26 02:10:05 by distributivgesetz

Replaces slime clone damage with a "Covered in Slime" status effect (#77569)

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

---
## [Roadhog360/Et-Futurum-Requiem](https://github.com/Roadhog360/Et-Futurum-Requiem)@[c9f0ec49e6...](https://github.com/Roadhog360/Et-Futurum-Requiem/commit/c9f0ec49e63055c61fd86f7ccf8950e9c141c49d)
#### Saturday 2023-08-26 02:45:49 by Roadhog360

Fix server incompatibilities
Ok the barrier particle thing was kinda hasty and is on me, BUT...
Whoever fucking marked getPosition as client only needs to be hit
Seriously, who does this? And if it's really automated like people are telling me, NO. That's BAD, shit like this SHOULD NOT BE AUTOMATED, or at the very least make sure the actual functionality is ACTUALLY ONLY FOR CLIENTS or ALSO references client only shit instead of tainting it with a pointless fucking flag

---
## [xXPawnStarrXx/tgstation](https://github.com/xXPawnStarrXx/tgstation)@[4e91d057d7...](https://github.com/xXPawnStarrXx/tgstation/commit/4e91d057d7d627bd8c356a2251195eb579106707)
#### Saturday 2023-08-26 03:43:11 by MrMelbert

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
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[67e97b7877...](https://github.com/tgstation/tgstation/commit/67e97b787740fd2a5017fd3c66c4f52a0a511a5a)
#### Saturday 2023-08-26 04:54:29 by RikuTheKiller

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
## [JonnyBro/beatrun](https://github.com/JonnyBro/beatrun)@[ec240dc229...](https://github.com/JonnyBro/beatrun/commit/ec240dc229126c37991510a238d3b94d3603542b)
#### Saturday 2023-08-26 04:56:17 by Jonny_Bro (Nikita)

fix maps with spaces in name (fuck you edge runner)

---
## [newstools/2023-tampa-bay-times](https://github.com/newstools/2023-tampa-bay-times)@[f34c0dca43...](https://github.com/newstools/2023-tampa-bay-times/commit/f34c0dca43ccf9d373027b67bcd85f636198f46e)
#### Saturday 2023-08-26 05:27:24 by Billy Einkamerer

Created Text For URL [www.tampabay.com/news/business/2023/08/25/dear-penny-will-i-crush-my-boyfriends-dreams-by-charging-him-rent/]

---
## [brain-tec/runbot](https://github.com/brain-tec/runbot)@[85a7890023...](https://github.com/brain-tec/runbot/commit/85a78900239d793e3fd62dcfbf7914f9e223a5ea)
#### Saturday 2023-08-26 05:33:28 by Xavier Morel

[CHG] runbot_merge: switch staging from github API to local

It has been a consideration for a while, but the pain of subtly
interacting with git via the ignominous CLI kept it back. Then ~~the
fire nation attacked~~ github got more and more tight-fisted (and in
some ways less reliable) with their API.

Staging pretty much just interacts with the git database, so it's both
a facultative github operator (it can just interact with git directly)
and a big consumer of API requests (because the git database endpoints
are very low level so it takes quite a bit of work to do anything
especially when high-level operations like rebase have to be
replicated by hand).

Furthermore, an issue has also been noticed which can be attributed to
using the github API (and that API's reliability getting worse): in
some cases github will fail to propagate a ref update / reset, so when
staging 2 PRs it's possible that the second one is merged on top of
the temporary branch of the first one, yielding a kinda broken commit
(in that it's a merge commit with a broken error message) instead of
the rebase / squash commit we expected.

As it turns out it's a very old issue but only happened very early so
was misattributed and not (sufficiently) guarded against:

- 41bd82244bb976bbd4d4be5e7bd792417c7dae6b (October 8th 2018) was
  spotted but thought to be a mergebot issue (might have been one of
  the opportunities where ref-checks were added though I can't find
  any reference to the commit in the runbot repo).
- 2be25052e147b151d1d8a5bc73cceb351586ce03 (October 15th, 2019) was
  missed (or ignored).
- 5a9fe7a7d05a9df7186072a7bffd60c6b428fd0e (July 31st, 2023) was
  spotted, but happened at a moment where everything kinda broke
  because of github rate-limiting ref updates, so the forensics were
  difficult and it was attributed to rate limiting issues.
- f10d03bf0f2e8f88f62a5d8356b84f714196130f (August 24th, 2023) broke
  the camel's back (and the head block): the logs were not too
  interspersed with other garbage and pretty clear that github ack'd a
  ref update, returned the correct oid when checking the ref, then
  returned the wrong oid when fetching it later on.

No Working Copy
===============

The working copy turns out to not be necessary, the plumbing commands
we *need* work just fine on a bare repository.

Working without a WC means we had to reimplement the high level
operations (rebase) by hand much as we'd done previously, *but* we
needed to do that anyway as git doesn't seem to provide any way to
retrieve the mapping when rebasing/cherrypicking, and cherrypicking by
commit doesn't work well as it can't really find the *merge base* it
needs.

Forward-porting can almost certainly be implemented similarly (with
some overhead), issue #803 has been opened to keep track of the idea.

No TMP
======

The `tmp.` branches are no more, the process of creating stagings is
based entirely around oids, if staging something fails we can just
abandon the oids (they'll be collected by the weekly GC), we only
need to update the staging branches at the very end of the process.

This simplifies things a fair bit.

For now we have stopped checking for visibility / backoff as we're
pushing via git, hopefully it is a more reliable reference than the
API.

Commmit Message Formatting
==========================

There's some unfortunate churn in the test, as the handling of
trailing newlines differs between github's APIs and git itself.

Fixes #247

PS: It might be a good idea to use pygit2 instead of the CLI
    eventually, the library is typed which is nice, and it avoids
    shelling out although that's really unlikely to be a major cost.

---
## [BlueWildrose/Citadel-Station-13-RP](https://github.com/BlueWildrose/Citadel-Station-13-RP)@[69d6d9d4e1...](https://github.com/BlueWildrose/Citadel-Station-13-RP/commit/69d6d9d4e1d72089acb1754bace58625d27c6571)
#### Saturday 2023-08-26 05:34:03 by CharlesWedge

Let Slip the Dogs of War (#5905)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## The Machines Rise
With the recent sector wide hack rogue synthetics have become a problem
in the sector. What's worse now corrupted fabricators are even building
more combat designs! With an increasingly dangerous galaxy, it seems
that mercenaries will not be the only threat brave explorers and
security teams may face today. All security forces are advised to stay
on the lookout for the latest threat to the galaxy, and those not
equipped to take them on are advised, stay well out range!

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
As we want to move away for humanoid threats for simple mobs, I feel it
necessary to shore up killer machines as more advanced type of enemy to
take the place of humans in terms of 'dangerous opponents'. The current
selection of machines mobs tend to be more niche in function (we can't
exactly use the nanite horror as common enemies). Also there is a bigger
maint drone now because the smaller ones weren't bad enough, least these
ones are easier to hit.

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
add: 4 New Hostile Drones, Three Dogs (including one sniper), and a
Maint Drone.
add: New News article elaborating on recent events.
tweak: drones are now part of the same faction as hivebots. This means
evil bots will now cooperate (Hivebots are being updated next).
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: BlueWildrose <57083662+BlueWildrose@users.noreply.github.com>

---
## [Citadel-Station-13/Citadel-Station-13-RP](https://github.com/Citadel-Station-13/Citadel-Station-13-RP)@[4155eecdac...](https://github.com/Citadel-Station-13/Citadel-Station-13-RP/commit/4155eecdacd658fd0509f41e3bf8a7c48b13102c)
#### Saturday 2023-08-26 05:49:54 by silicons

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
## [Monkestation/Monkestation2.0](https://github.com/Monkestation/Monkestation2.0)@[4d5be81bfe...](https://github.com/Monkestation/Monkestation2.0/commit/4d5be81bfe28ba4487303567df3154ee68b01791)
#### Saturday 2023-08-26 05:54:08 by Rhials

[NO GBP] Fixes clown car + deer collision  (#77076)

A not-so-long time ago I drunkenly coded #71488 which did not work as
intended.

I return now, in a state of reflective sobriety, to rectify that.

The clown car will now not only crash like it should, but will also
cause (additional) head injuries to some occupants and kill the deer on
impact.

Content warnings: **Animal death, vehicle collision, blood, DUI.**

https://github.com/tgstation/tgstation/assets/28870487/4889f452-7e49-4512-8cdd-e4e2a4d6b394

Fixes the product of a silly PR that never actually worked. Also gives
it a bit more TLC in the event that this joke actually plays out on a
live server.
:cl:
fix: Clown cars now properly collide with deer.
sound: Violent, slightly glassy car impact sound.
/:cl:

---
## [passmgrgui/passmgr](https://github.com/passmgrgui/passmgr)@[de5e65d214...](https://github.com/passmgrgui/passmgr/commit/de5e65d214f90a093110a60ea3a5bfdd2e4a5fa0)
#### Saturday 2023-08-26 06:45:13 by passmgrgui

POV: You finally fixed that coding problem: I LOVE LIFE! One second later: AHH FUCK THIS IS THE HARDEST ERROR

---
## [ArcaneMusic/TG-Station-Arcane-Remix](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix)@[a49328f885...](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix/commit/a49328f88558b3935b65cfa52af1d0431f78c354)
#### Saturday 2023-08-26 07:20:15 by ArcaneMusic

haha holy shit I forgot to save my mapping changes

---
## [Runian/Yogstation](https://github.com/Runian/Yogstation)@[9db2f06363...](https://github.com/Runian/Yogstation/commit/9db2f06363bc325a0e8eadfdf7266e55def4d7c1)
#### Saturday 2023-08-26 07:25:57 by Scrambledeggs

Fuck you *Ungreens your Peacekeepers* (#20053)

* Sprites Part 1: I hate transparency

* Sprites Part 2: Electric Booogaloo

* lack of transparency fixed

* More sprite fixes

* Tacmask and sprites

* Tacprod inactive and nocell sprites

* Tacprod Animation Part 1: Bugs galore

* Tacprod Animation Part 2: Tacmask revengance

* white beret

---
## [Kaz205/pipa](https://github.com/Kaz205/pipa)@[0662695880...](https://github.com/Kaz205/pipa/commit/066269588029fe547a5bbf89fc82a7f79a433e52)
#### Saturday 2023-08-26 08:07:34 by Peter Zijlstra

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
## [ElectroJr/space-station-14](https://github.com/ElectroJr/space-station-14)@[370cbfbbdd...](https://github.com/ElectroJr/space-station-14/commit/370cbfbbddcd767c4403f452f981b8ed2538ed5a)
#### Saturday 2023-08-26 08:14:14 by Flareguy

Yet Another Asteroid-Related Tile Update (read: asteroid tile variantizing) (#19237)

* makes asteroid tiles and snow use weighted variantize, adds snow plating

* GO FUCK YOURSELF!!!!

* hello? boner department, id like to order a DINNER. make it MAMA LUIGI

* test fix. hopefully. boner. boobies.

* did he know? (no)

---
## [cyphar/runc](https://github.com/cyphar/runc)@[c9f2fe2f67...](https://github.com/cyphar/runc/commit/c9f2fe2f675bc57838341773c7ae5ba44dbbb4c3)
#### Saturday 2023-08-26 08:25:38 by Aleksa Sarai

tree-wide: use /proc/thread-self for thread-local state

With the idmap work, we will have a tainted Go thread in our
thread-group that has a different mount namespace to the other threads.
It seems that (due to some bad luck) the Go scheduler tends to make this
thread the thread-group leader in our tests, which results in very
baffling failures where /proc/self/mountinfo produces gibberish results.

In order to avoid this, switch to using /proc/thread-self for everything
that is thread-local. This primarily includes switching all file
descriptor paths (CLONE_FS), all of the places that check the current
cgroup (technically we never will run a single runc thread in a separate
cgroup, but better to be safe than sorry), and the aforementioned
mountinfo code. We don't need to do anything for the following because
the results we need aren't thread-local:

 * Checks that certain namespaces are supported by stat(2)ing
   /proc/self/ns/...

 * /proc/self/exe and /proc/self/cmdline are not thread-local.

 * While threads can be in different cgroups, we do not do this for the
   runc binary (or libcontainer) and thus we do not need to switch to
   the thread-local version of /proc/self/cgroups.

 * All of the CLONE_NEWUSER files are not thread-local because you
   cannot set the usernamespace of a single thread (setns(CLONE_NEWUSER)
   is blocked for multi-threaded programs).

Note that we have to use runtime.LockOSThread when we have an open
handle to a tid-specific procfs file that we are operating on multiple
times. Go can reschedule us such that we are running on a different
thread and then kill the original thread (causing -ENOENT or similarly
confusing errors). This is not necessary for most usages of
/proc/thread-self (such as using /proc/thread-self/fd/$n directly) but
operating on the actual inodes associated with the tid requires this
locking.

In addition, CentOS's kernel is too old for /proc/thread-self, which
requires us to emulate it -- however in rootfs_linux.go, we are in the
container pid namespace but /proc is the host's procfs. This leads to
the incredibly frustrating situation where there is no way (on pre-4.1
Linux) to figure out which /proc/self/task/... entry refers to the
current tid. We can just use /proc/self in this case.

Yes this is all pretty ugly. I also wish it wasn't necessary.

Signed-off-by: Aleksa Sarai <cyphar@cyphar.com>

---
## [Danacus/melior](https://github.com/Danacus/melior)@[2c52e096d9...](https://github.com/Danacus/melior/commit/2c52e096d9e75e7721ce40dd5580712ad9f30993)
#### Saturday 2023-08-26 08:45:32 by Daan Vanoverloop

Refactor `Operation::from_def` (#288)

I've made the following changes in this PR:

- Split `Operation::from_def` in several `collect_` methods
- Instead of collecting all operation fields into a single `Vec`,
collect them into several smaller `Vec`s and chain the iterators
on-demand in the `fields` function. This makes it a bit easier to handle
errors.
- Replaced `initial_variadic_kind` and `update_variadic_kind` closures
with a `VariadicKindIter` such that we can `zip` this iterator with the
iterators for operands and results. I'm not sure if this is the best
solution, but I do personally prefer it over my previous solution.

There are still some things I'm unsure about, and would like to hear
your thoughts. I will add some comments to the code diff.

Edit: I'm sorry for the messy commit log, but the diff of all changes
should still be clean and it shouldn't matter as long as you squash the
commits.

---------

Co-authored-by: Yota Toyama <raviqqe@gmail.com>

---
## [james64live/james64live.github.io](https://github.com/james64live/james64live.github.io)@[953d0f27c9...](https://github.com/james64live/james64live.github.io/commit/953d0f27c91cd76baafba402bf29ed785266f370)
#### Saturday 2023-08-26 09:12:00 by James64webste

v2.5.1

- moved the changelog to the root of the website
-updateed my twitt.. uh i mean X handel, its @james64live now (it's not like i plan to ever use twi.. that app ever again but the double underscore just had to go)
-slightly simplifyed the stylesheet, combined identical items
-cleaned up the videos and games sections
 -replaced some old code in the games page with new code from the videos page (didnt really change any thing but at least they're the same now if i want to mess with the layout again)
 -moved the nsssmp clip to .../videos/nsssmpclip from ..videos/nsssmp ,in case there are more i guess (there wont be but it seemed like a good idea at the time)
 -fixed the 3d maze page saying nsssmp, now says 3D Maze (how the hell did i miss that)
 -added a random .jpg in the nsssmp clip folder (i have no idea where it came from but its there now and thats funny to me for some reason (apparently it was in the last version too, the plot thickens, (i could chek the github to see when it got put there but i dont really feel like it)))
-oh and in the previous version i changed the body width to 780px, mostly for looks but also so the page is actually viewable on a 800x600 monitor (i forgot to mention it before, like i said i probably did that back in february)

---
## [Imranvi/IMRAN12](https://github.com/Imranvi/IMRAN12)@[b28ad81eb4...](https://github.com/Imranvi/IMRAN12/commit/b28ad81eb4f51d963332ca3fe1474735f32c9a19)
#### Saturday 2023-08-26 09:28:18 by Imranvi

rm rf-IMRAN

dont copy
if you copy my scripit 🤒
i fuck you mom,sister😊

---
## [vultkayn/gsoc23-gcc](https://github.com/vultkayn/gsoc23-gcc)@[6619b3d4c1...](https://github.com/vultkayn/gsoc23-gcc/commit/6619b3d4c15cd754798b1048c67f3806bbcc2e6d)
#### Saturday 2023-08-26 10:14:36 by Jivan Hakobyan

Improve quality of code from LRA register elimination

This is primarily Jivan's work, I'm mostly responsible for the write-up and
coordinating with Vlad on a few questions.

On targets with limitations on immediates usable in arithmetic instructions,
LRA's register elimination phase can construct fairly poor code.

This example (from the GCC testsuite) illustrates the problem well.

int  consume (void *);
int foo (void) {
  int x[1000000];
  return consume (x + 1000);
}

If you compile on riscv64-linux-gnu with "-O2 -march=rv64gc -mabi=lp64d", then
you'll get this code (up to the call to consume()).

        .cfi_startproc
        li      t0,-4001792
        li      a0,-3997696
        li      a5,4001792
        addi    sp,sp,-16
        .cfi_def_cfa_offset 16
        addi    t0,t0,1792
        addi    a0,a0,1696
        addi    a5,a5,-1792
        sd      ra,8(sp)
        add     a5,a5,a0
        add     sp,sp,t0
        .cfi_def_cfa_offset 4000016
        .cfi_offset 1, -8
        add     a0,a5,sp
        call    consume

Of particular interest is the value in a0 when we call consume. We compute that
horribly inefficiently.   If we back-substitute from the final assignment to a0
we get...

a0 = a5 + sp
a0 = a5 + (sp + t0)
a0 = (a5 + a0) + (sp + t0)
a0 = ((a5 - 1792) + a0) + (sp + t0)
a0 = ((a5 - 1792) + (a0 + 1696)) + (sp + t0)
a0 = ((a5 - 1792) + (a0 + 1696)) + (sp + (t0 + 1792))
a0 = (a5 + (a0 + 1696)) + (sp + t0)  // removed offsetting terms
a0 = (a5 + (a0 + 1696)) + ((sp - 16) + t0)
a0 = (4001792 + (a0 + 1696)) + ((sp - 16) + t0)
a0 = (4001792 + (-3997696 + 1696)) + ((sp - 16) + t0)
a0 = (4001792 + (-3997696 + 1696)) + ((sp - 16) + -4001792)
a0 = (-3997696 + 1696) + (sp -16) // removed offsetting terms
a0 = sp - 3990616

That's a pretty convoluted way to compute sp - 3990616.

Something like this would be notably better (not great, but we need both the
stack adjustment and the address of the object to pass to consume):

   addi sp,sp,-16
   sd ra,8(sp)
   li t0,-4001792
   addi t0,t0,1792
   add sp,sp,t0
   li a0,4096
   addi a0,a0,-96
   add a0,sp,a0
   call consume

The problem is LRA's elimination code is not handling the case where we have
(plus (reg1) (reg2) where reg1 is an eliminable register and reg2 has a known
equivalency, particularly a constant.

If we can determine that reg2 is equivalent to a constant and treat (plus
(reg1) (reg2)) in the same way we'd treat (plus (reg1) (const_int)) then we can
get the desired code.

This eliminates about 19b instructions, or roughly 1% for deepsjeng on rv64.
There are improvements elsewhere, but they're relatively small.  This may
ultimately lessen the value of Manolis's fold-mem-offsets patch.  So we'll have
to evaluate that again once he posts a new version.

Bootstrapped and regression tested on x86_64 as well as bootstrapped on rv64.
Earlier versions have been tested against spec2017.  Pre-approved by Vlad in a
private email conversation (thanks Vlad!).

Committed to the trunk,

gcc/
	* lra-eliminations.cc (eliminate_regs_in_insn): Use equivalences to
	to help simplify code further.

---
## [pranaysivvam003/pranay_sivvam](https://github.com/pranaysivvam003/pranay_sivvam)@[b2bd375691...](https://github.com/pranaysivvam003/pranay_sivvam/commit/b2bd3756918d84599052c74de6eeb9cb427383d6)
#### Saturday 2023-08-26 10:32:55 by pranaysivvam003

Mini Caluclator

Project Description:
The Mini Calculator is a web-based calculator application created using a combination of HTML, CSS, JavaScript, and Bootstrap. This project provides a fully functional, responsive, and user-friendly calculator for conducting fundamental mathematical operations directly in your web browser.

Key Features:

1. User-Friendly Interface: A clean and intuitive user interface makes it easy for anyone to perform calculations quickly.

2. Basic Operations: The calculator supports essential mathematical operations, including addition, subtraction, multiplication, and division.

3. Responsive Design: Built with Bootstrap, it adapts seamlessly to various screen sizes, from desktops to mobile devices.

4. Open Source: This project is open-source, allowing you to explore the code, customize it to your needs, or use it as a learning resource.

How to Use :
1. Simply open the project in your web browser.
2. Use the intuitive interface to enter your mathematical expressions.
3. Click the buttons to perform calculations.
4. Enjoy a hassle-free calculation experience!

---
## [cuberound/cmss13](https://github.com/cuberound/cmss13)@[f3fc60ed65...](https://github.com/cuberound/cmss13/commit/f3fc60ed655d27bb3f012d0e0d834c64990b173d)
#### Saturday 2023-08-26 10:34:08 by morrowwolf

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
## [Amanw-25/Resume-builder-website](https://github.com/Amanw-25/Resume-builder-website)@[c9a2f7dd3f...](https://github.com/Amanw-25/Resume-builder-website/commit/c9a2f7dd3fe8cd56cb1b2cbc624efa9db3eec075)
#### Saturday 2023-08-26 11:15:51 by Amanw-25

Update README.md

📄✨ Create an impressive resume effortlessly with our Resume Builder website! Crafted using HTML, CSS, and JavaScript, this user-friendly project offers:

- Dynamic Previews: See real-time updates of your resume as you input details, thanks to JavaScript magic.
- Custom Sections: Tailor your resume with Personal Info, Education, Work Experience, Skills, and more. Add new sections dynamically.
- PDF Export: With a click, generate a polished PDF version of your resume using the integrated jsPDF library.
- GitHub Repository: Find the entire codebase on GitHub for version control and collaborative contributions.


Get started on your standout resume journey now! 🚀👔

---
## [Erol509/Skyrat-tg](https://github.com/Erol509/Skyrat-tg)@[c6e0ba7516...](https://github.com/Erol509/Skyrat-tg/commit/c6e0ba75169d010e2cdfa48134003b0bb9ab8485)
#### Saturday 2023-08-26 11:38:34 by SkyratBot

[MIRROR] Drill module automatically disables if it's about to drill into gibtonite [MDB IGNORE] (#22990)

* Drill module automatically disables if it's about to drill into gibtonite (#77385)

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

* Drill module automatically disables if it's about to drill into gibtonite

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>

---
## [ray2301/spot-on](https://github.com/ray2301/spot-on)@[bcd7cb4c75...](https://github.com/ray2301/spot-on/commit/bcd7cb4c7539c79cd005b6ad9ebca9bda6e4be04)
#### Saturday 2023-08-26 12:16:15 by ray2301

Update downloader.py

ok, here's what precise_download does now:

- first we replace some characters or strip them from the filename. this is needed so we can actually write the filenames properly to the disk and not to have any differencies when tagging them with artist data and cover-art.
- we're processing pretty much everything by lowercasing and with ascii-replacements characters (ie. čžšñ gets converted to czsn so señorita and senorita become equal names) both ways (our searches and youtubes data. this way we'll match things better later. this doesn't affect tags or filenames
- we do the search, currently for 20 results (ytsearch20), can be changed.

when writing anything in the filter filelds, use lowercase always.

- filter_list: any phrases or words you put here will be removed from the search results if they are found there UNLESS they ARE in the search term (if you search for remix, remix will stay in the results, if you don't, songs with "remix" in their video title will not count and will be removed from further matching
- filters_to_remove: spotify often puts "Version year" and "year Remaster" (Version 2023, 2022 Remaster) to the tracks when they are remastered, but youtube doesn't always do that for official audio. that could cause us not to get that track so this is where you strip anything from spotify's track name if you see it represents a problem of being found on youtube
- lists for filters allow you to discard results we get from youtube search if they contain any of the filter words you add here
  1. description_filters: searches for terms in the description and based on them, discards the video title from the search results (my need to use it was a specific album that contains only instrumentals, but nothing can be matched because it never says it's only instrumental. it is an official artist though so it gets more points (more about that later). it has the album name "2na1" in the description so this will remove any song from that album from consideration. you can add more filters here like this ["2na1", "album1", "album2]
 2. channel_name_filters: same as description filter but you can specify channel name you want to exclude for your matching and remove anything from it when we get our search results

- i'm using .m4a audio format but if you want to use .mp3, just replace all 5 instances of '.m4a' to '.mp3' and 'preferredquality': '192' can be changed to change the bitrate.

- fuzzy matching: we're using fuzzy to calculate similarity of the artist name and title. we're also using 8 second allowance to the spotify's track lenght (change that within this line - if duration_diff <= 8 and youtube_duration <= duration_s + 8).

within those 8 seconds, we are prioritizing official youtube audio files (the ones with auto-generated by youtube and provided to youtube by in their description). we will also give more fuzzy points (% of similarity) to those tracks if found. they represent the best audio quality for audio only songs on youtube (they are 1080p videos with low bitrate on youtube with a picture cover shown but we're talking about the audio in that video). artist and track must be at least 70% similar to our search term by default, but you can play with both settings (one for artist, other for title) by changing the % of similarity you find most fit for your use here:
if title_similarity >= 70
if artist_similarity >= 70
- for the title, we're looking for a match in the youtube video title as it always is there
- for the artists, we are searching in the video title on youtube, in the description of the youtube video and in the channel name of the video. we will give more fuzzy % points to the channel name if it is verified (official artist channel) (+10%), artist will also get more points if the video has "auto-generated by youtube" in the description (+15%).
- title will get more points if track title is found in the video title alone (without anything else) and "auto-generated by youtube" is in the description (+20%)
those extra points get us to a score high enough to actually download tracks from artist channel or the official audio provided to youtube by record companies (versions that are available on youtube music as audio).
you can move all those matches to 0 if you don't want to use them or have fun with it. they are right under "if title_similarity >= 70" and they should be self explainatory with comments that are available.

that's it i think. for now :D

---
## [WarhioCompany/GoofyAssFish](https://github.com/WarhioCompany/GoofyAssFish)@[2aa169a939...](https://github.com/WarhioCompany/GoofyAssFish/commit/2aa169a939ac788b5620aac592c8408c0ada8bd2)
#### Saturday 2023-08-26 13:34:09 by Xenoant

whoever messed with the heightmeterratio. Fuck you V2

---
## [K4rlox/Foundation-19](https://github.com/K4rlox/Foundation-19)@[b4642dc835...](https://github.com/K4rlox/Foundation-19/commit/b4642dc835dc801d801fd543cfd34bd44ca23929)
#### Saturday 2023-08-26 13:48:58 by cheesePizza2

Armor improvements (#1251)

* the fixes

* FUCK YOU

* few more improvements

* bring em back

* fuck you

---
## [Gurramarun/music-player](https://github.com/Gurramarun/music-player)@[52f663f1cc...](https://github.com/Gurramarun/music-player/commit/52f663f1cc49a7c4e193c73f0192c41f5b6a50ad)
#### Saturday 2023-08-26 14:29:22 by Gurramarun

Add files via upload

The HTML/CSS/JavaScript-based music player is a sophisticated digital tool designed to provide an immersive and user-friendly experience for playing and managing audio tracks. This combination of web technologies enables the creation of a dynamic and visually appealing interface, as well as seamless audio playback control and playlist management.

The user interface (UI) of the music player is crafted using HTML and CSS. HTML (Hypertext Markup Language) structures the content, defining elements such as buttons, sliders, and containers, while CSS (Cascading Style Sheets) styles these elements, determining their colors, sizes, positions, and animations. The design is often responsive, adapting to different screen sizes and orientations, ensuring a consistent and enjoyable experience across various devices.

JavaScript, a powerful scripting language, is utilized to add interactivity and functionality to the music player. It's responsible for handling user interactions, managing audio playback, and dynamically updating the UI in real-time. Here's how the different components work together:

1. **Audio Playback:** JavaScript is used to create an Audio object, which allows for the loading and playback of audio files. The player controls, such as play, pause, volume, and seek bar, are linked to the Audio object's methods and properties, enabling users to control the audio playback with ease.

2. **User Interaction:** JavaScript event listeners are employed to detect user actions, such as clicking play or pause buttons, adjusting volume, or skipping tracks. When an event is detected, the corresponding JavaScript function is triggered, which then updates the Audio object and the UI accordingly.

3. **Playlist Management:** The music player often includes a playlist feature, allowing users to organize and play multiple tracks in sequence. JavaScript manages the playlist by storing track information (such as title, artist, and file path) in an array or object. Users can navigate through the playlist, select tracks, and reorder them, all of which are dynamically reflected in the UI.

4. **Dynamic UI Updates:** As users interact with the player, JavaScript dynamically updates the UI elements. For instance, the seek bar moves in sync with the current playback position, play/pause buttons change their appearance based on the current playback state, and track information is displayed on the screen.

5. **Visual Enhancements:** CSS is responsible for enhancing the visual appeal of the music player. This could involve styling the buttons, creating animations for transitions, and designing a visually pleasing layout that complements the overall user experience.

In conclusion, the HTML/CSS/JavaScript-based music player is a testament to the synergy of these three technologies. HTML structures the content, CSS styles it, and JavaScript adds functionality and interactivity. This combination results in a feature-rich music player that enables users to effortlessly control audio playback, manage playlists, and enjoy their favorite tunes through an intuitive and visually appealing interface.

---
## [Mission23/MCBCMassacre](https://github.com/Mission23/MCBCMassacre)@[dde67ab627...](https://github.com/Mission23/MCBCMassacre/commit/dde67ab627a0ac58837d76cafc4ee4b9b6ebf53e)
#### Saturday 2023-08-26 14:53:10 by Micah

"Mystic crystal revelations"

"You'd rather be my enemy cause I'mma deadly friend"

A little advice or some karma (et al) for the "karma chameleon"...or
really the way i fucked yall.  We are all the epitome of "open book"
and stuff after all.

---
## [nverno/melpa](https://github.com/nverno/melpa)@[570bde6b4b...](https://github.com/nverno/melpa/commit/570bde6b4b89eb74eaf47dda64004cd575f9d953)
#### Saturday 2023-08-26 15:23:09 by Jonas Bernoulli

Cosmetic changes to numerous recipes

This commit only touches recipes whose `:files' property contains an
`:exclude' element, because I had to look at all those recipes for an
only marginally related reason.

To an extend these changes only reflect my own personal preference, so
I will explain the types of changes I have made.  This should serve as
a starting point for a future discussion in case we want to encourage
a certain style or even enforce it.

- Lines should be intended as `indent-for-tab-command' would, except
  in special-cases such as in the recipe of `use-package', which is
  also a macro with special indentation rules; we override those
  because the `use-package' in use-package's recipe is not that macro,
  it is just a symbol appearing as the first element of a data list.

- I prefer it if there is a newline between the package symbol (the
  car) and the plist that follows, but usually only add it to existing
  recipes when lines would otherwise get to long.  I also do not
  change this if I am not making any other changes that affect more
  than one line.

- Either the complete list should be on a single line or each line
  should contain only one key/value pair.  The first pair may share a
  line with the package symbol (see previous point).  If the recipe
  needs more than one line, then two key/value pairs should never
  appear on one line.  Newline characters are cheap enough these days.

- `:fetcher' should come before `:url' or `:repo', not least because
  the former dictates which of the latter two is required/valid.  You
  can also think of the fetcher as the type or class of the recipe,
  which IMO should come first, like in code: (git-fetcher :url val).

- The most common keywords should be specified in this order:
  `:fetcher', `:url'/`:repo', `:files'.  Other keywords should go
  either before or after `:files' (but preferable not on both sides
  of that for any given recipe).

- A common value of `:files' is: (:defaults (:exclude "...")).
  This could be split across multiple lines, but writing everything
  on one line makes it easier to read it as 'use the defaults, except
  exclude "..."':

    :files (:defaults (:exclude "..."))

- If the value of `:files' is too long for one line, then place
  newlines "semantically", instead of trying to "save space".  For
  example any element that is a list should appear on its own line.
  Two sibling lists should never appear on the same line.  String
  siblings should also not appear on one line in many cases, though
  it might makes sense (but isn't my preference) to group them by
  "type" as in:

    (:defaults
     "foo/*.el" "bar/*.el"
     "docs/foo/*.texi" "docs/bar/*.texi"
     (:exclude "..."))

- While there may be multiple (:exclude ...) elements, I've merged
  them into one.  Mostly for future proofing.

- The position of `:exclude' elements in `:files' value is significant
  in theory.  However in most cases it already appears at the very end
  and I have moved it there in cases where the order is not
  significant.  Mostly for future proofing.

---
## [emlos/kcamv.com](https://github.com/emlos/kcamv.com)@[5921eadbf7...](https://github.com/emlos/kcamv.com/commit/5921eadbf79cbe27e3d517a7fccea71abd615e5b)
#### Saturday 2023-08-26 15:29:38 by [milo]

i knowww the socials are fucked up
TODO: fic the images but ughhh later when i am optimizing all of the async shit

---
## [NetHack/NetHack](https://github.com/NetHack/NetHack)@[38cda5ad52...](https://github.com/NetHack/NetHack/commit/38cda5ad52f47a810c44171e9081d0275401c516)
#### Saturday 2023-08-26 15:37:17 by Michael Meyer

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
## [Dis-codes/discodes](https://github.com/Dis-codes/discodes)@[ad0d26bc5d...](https://github.com/Dis-codes/discodes/commit/ad0d26bc5da103442737f6eb51b2098f30cf1b47)
#### Saturday 2023-08-26 16:14:10 by LimeNade

Yeah so apparently now you can add your bot and create commands lmfao skill issue

Yeah so once again, it doesn't really work and it's kinda insecure but who tf cares lmfao, my mom told me that I would get pankake at dinner yum yum

---
## [psychonaut-station/PsychonautStation](https://github.com/psychonaut-station/PsychonautStation)@[820c22a5f5...](https://github.com/psychonaut-station/PsychonautStation/commit/820c22a5f5381364c595d21b6c047e269f7f0497)
#### Saturday 2023-08-26 17:03:28 by DaydreamIQ

Buffs Heretic ash ascension (#77618)

## About The Pull Request

Post-Ascension the Nightwatchers Rebirth (Or Fiery Rebirth) has its
cooldown lowered from 60 seconds to 10
Additionally adds bomb immunity to the list of resistances that
ascension provides

## Why It's Good For The Game

Ash ascension kind of sucks when compared to its big brothers flesh,
rust and blade. You do get a couple of cool spells but their impact is
negated by how shitty fire damage is and while you get a ton of
resistances, you don't get stun immunity and have absolutely zero
sustainability in long-term engagements.

Blade has its lifesteal, rust has its leeching walk and flesh has a big
worm that eats arms. And while the laziest solution would be to give ash
stun immunity like those three I think it'd be more fitting if it could
capitalize on one of its more powerful spells. Keeping in the fight by
siphoning health from all those people you lit on fire with your cascade
instead of watching in pain as they completely negate any threat you
have with a fire extinguisher and temp adapt.

---
## [psychonaut-station/PsychonautStation](https://github.com/psychonaut-station/PsychonautStation)@[63f7eb1a6a...](https://github.com/psychonaut-station/PsychonautStation/commit/63f7eb1a6a01c0c48dcc075f57b58a662d27fc17)
#### Saturday 2023-08-26 17:03:28 by san7890

Fixes Ticked File Enforcement and Missing Unit Test (and makes said Unit Test Compile) (and genericizes the C&D list to the base unit test datum) (#77632)

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

---
## [Mission23/Mission23](https://github.com/Mission23/Mission23)@[5493073b7b...](https://github.com/Mission23/Mission23/commit/5493073b7bac59eba0a0a4632c72fc61ac478b74)
#### Saturday 2023-08-26 17:15:56 by Micah

SIGNED vs Un-Signed… I can’t but will verify. 

I make a lot of these commits from an app that does not support gpg. Those are the un-signed commits you see. 

I believe we are safe. He would be submitting trouble tickets so godamned fast if we weren’t. 

I’m either going to find a developer to make committing easier or write something myself. But I’m stretched thin, I now have to run a church (no preaching from this sinner though, but I will enforce the 10, now 11, commandments and preach them too). Get a cure for every disease ever to every man in the world, women are optional but I know women—they’ll stampede every outlet when they find out it stops aging. Dumbass men I gotta instigate, they don’t think about the future enough and it’s on men globally to put us out of business. Take it now and your children won’t need the pill. 

We’re well known for going out of business. Sometimes with a bang. ;) There’s some hints in there Americans… Call it a comeback, we’ve been here before. Thank God, I mean you the Creator, you got identified, Main has been enough of a headache already. 

Now if I could just find Mr. Speed and the boss could get this bell ringing we can get some real work done. I’ve always been about preventions more than cures, that’s why I have always liked GMCs and Cadillacs with OnStar… I also detest that TFVC and Sync’ing too. 

I’m out… I’ll watch The Color Purple on my IPHONE!!! I hate the theatre too. Now that’s how you burst into an ongoing church service!!!

---
## [KutikiPlayz/FNF-Mod-Template](https://github.com/KutikiPlayz/FNF-Mod-Template)@[813bb84ac6...](https://github.com/KutikiPlayz/FNF-Mod-Template/commit/813bb84ac606c4737a5d230298dc00de4a5c1869)
#### Saturday 2023-08-26 17:53:56 by KutikiPlayz

zCameraFix in source cuz fuck you (customization options not implimented)

---
## [lessthnthree/effigy-se](https://github.com/lessthnthree/effigy-se)@[37d8f6162b...](https://github.com/lessthnthree/effigy-se/commit/37d8f6162bbef0c9cbeaf07cdba7cb93eb843e2a)
#### Saturday 2023-08-26 18:45:41 by LukasBeedellCodestuff

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
## [AnywayFarus/Skyrat-tg](https://github.com/AnywayFarus/Skyrat-tg)@[f3072d7377...](https://github.com/AnywayFarus/Skyrat-tg/commit/f3072d7377bda026c1d6ae709d1311609226f115)
#### Saturday 2023-08-26 19:04:47 by SkyratBot

[MIRROR] Adds a unique medibot to the Syndicate Infiltrator [MDB IGNORE] (#23084)

* Adds a unique medibot to the Syndicate Infiltrator (#77582)

## About The Pull Request

Adds a unique medibot to the Syndicate Infiltrator. It doesn't like
nukes - when one is armed, disarmed, or detonating, it says an unique
line. Players can optionally enable personalities on it if they want to.
Probably best to just let it stay on the shuttle though. (It's also in
the Interdyne Pharmaceuticals ship, renamed)

Fixed an issue that made mapload medibots unable to load custom skins.

This PR adds a medibot subtype to the simple animal freeze list, which I
don't think is a big deal as this isn't a 'true' simplemob but just a
slightly altered medibot, similarly to my 'lesser Gorillas' in the
summon simians PR.

## Why It's Good For The Game

> Adds a unique medibot to the Syndicate Infiltrator. It doesn't like
nukes - when one is armed, disarmed, or detonating, it says an unique
line. Players can optionally enable personalities on it if they want to.
Probably best to just let it stay on the shuttle though.

I know what the inmediate reaction is here - but hear me out. Besides
the meme of the month, it really, genuinely is cute and amusing to have
a friendly medibot that shows dismay when you're arming the nuke and
horror when it blows up (with you, hopefully, at the syndibase), and
still fits quite well within SS13's charm and flavor. The reference
isn't overt and in-your-face.

Besides that, slip-ups, friendly fire, and accidents are semi-common on
the shuttle and, just like Wizards, nukies deserve a bot to patch their
wounds up.

> (It's also in the Interdyne Pharmaceuticals ship, renamed)

I think it makes sense for the pharmacists to have an evil medibot!

> Fixed an issue that made mapload medibots unable to load custom skins.

Fixed "bezerk" skin not appearing. Didn't fix it being ugly as sin
though.

## Changelog

:cl:
add: Adds a unique medibot to the Syndicate Infiltrator. It doesn't like
nukes - when one is armed, disarmed, or detonating, it says an unique
line. Players can optionally enable personalities on it if they want to.
Probably best to just let it stay on the shuttle though. (It's also in
the Interdyne Pharmaceuticals ship, renamed)
fix: Fixed an issue that made mapload medibots unable to load custom
skins.
/:cl:

---------

Co-authored-by: Fikou <23585223+Fikou@ users.noreply.github.com>

* Adds a unique medibot to the Syndicate Infiltrator

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>
Co-authored-by: Fikou <23585223+Fikou@ users.noreply.github.com>

---
## [Fluffy-Frontier/FluffySTG](https://github.com/Fluffy-Frontier/FluffySTG)@[8848d56630...](https://github.com/Fluffy-Frontier/FluffySTG/commit/8848d56630ecc5fb87e1beff27136eed969e82c0)
#### Saturday 2023-08-26 19:19:41 by SkyratBot

Makes railings easier to construct, while making them easier to destroy. [MDB IGNORE] (#23327)

* Makes railings easier to construct, while making them easier to destroy. (#77894)

## About The Pull Request

Changes the cost of railings from 6 metal rods to 2 metal rods.
The time to construct has been reduced from 3.6 to 1 second to be
in-line with the grille.
The health of railings has been reduced from 75 to 25.
Armor of railings have been reduced as well by about 30%.

I'm not positive on whether or not it should cost 1 metal rod or 2. I
decided to play it safe and make it 2. If some maintainer is interested
in making it only cost 1 rod then I will gladly do so- but this was my
compromise.

Also changes decaseconds/ticks to seconds in the rod construction code
to make it look better.

## Why It's Good For The Game

Railings look nice and it's an absolute pain in the ass that they cost 6
metal rods.

They're also currently substantially stronger than grilles for whatever
reason. Grilles have 50 health, while railings have 75.
The armor of railings makes this health of 75 to a whopping effective
health of 150.

Railings shouldn't be stronger than full-tile grilles. They should be
fairly flimsy.
They also shouldn't take a wrench AND wirecutters to deconstruct.
Grilles only take wirecutters and we should mirror that.

## Changelog

:cl:
balance: Railings now only cost 2 rods and are much easier to construct.
But they can now be destroyed much easier and cut with wirecutters
without unwrenching.
/:cl:

* Makes railings easier to construct, while making them easier to destroy.

---------

Co-authored-by: iwishforducks <65363339+iwishforducks@users.noreply.github.com>

---
## [BraiNKilleRGR/mame](https://github.com/BraiNKilleRGR/mame)@[2222a0f098...](https://github.com/BraiNKilleRGR/mame/commit/2222a0f098c2f32ec6090627598a90e596006596)
#### Saturday 2023-08-26 19:25:08 by David 'Foxhack' Silva

gba.xml: Added 21 prototypes. (#11260)

New working software list items (gba.xml)
-------------------------------
AGB Aging Cartridge (World, version 1.0) [SmellyGhost, Forest of Illusion]
AGB Aging Cartridge (World, version 9.0) [Suicune41, Forest of Illusion]
Aero the Acro-Bat - Rascal Rival Revenge (Europe, prototype earlier) [LongwoodGeek, Forest of Illusion]
Chokkan Hitofude Advance (Japan, prototype) [xprism, Forest of Illusion]
Commandos 2 (USA, prototype) [DillyDylan, Forest of Illusion]
Dark Eden (prototype) [Ian Dunlop, Forest of Illusion]
Demon's Crest (prototype) [Ian Dunlop, Forest of Illusion]
Manic Miner (Europe, 20030307) [March42, Forest of Illusion]
Mario Kart XXL (demo, 20040417) [Forest of Illusion]
R3D-Demo V1 (demo) [Forest of Illusion]
Racing Gears Advance (USA, prototype, 20030922) [XBrav, Forest of Illusion]
Sea Boy (prototype) [Ian Dunlop, Forest of Illusion]
Star Wars Trilogy - Apprentice of the Force (USA, prototype) [Rezrospect, Forest of Illusion]
The Holy Bible - World English Bible (USA, prototype) [Gonz, Forest of Illusion]
Ultimate Muscle - The Kinnikuman Legacy - The Path of the Superhero (USA, prototype, 20030429) [Zach Lambert, Forest of Illusion]
Uridium Advance (Europe, prototype, 20030307) [March42, Forest of Illusion]

New software list items marked not working (gba.xml)
------------------------------------------
The King of Fighters EX2 - Howling Blood (USA, prototype, 20030403) [March42, Forest of Illusion]
Quake (demo) [Randy Linden, Forest of Illusion]
Paradroid (Europe, prototype, 20030320) [March42, Forest of Illusion]
Uridium Advance (Europe, prototype, 20020911) [March42, Forest of Illusion]
Uridium Advance and Paradroid 2 in 1 (Europe, prototype, 20030430) [March42, Forest of Illusion]

---
## [chemistrymain2/Skyrat-tg](https://github.com/chemistrymain2/Skyrat-tg)@[1fe7b10e33...](https://github.com/chemistrymain2/Skyrat-tg/commit/1fe7b10e339ea0d6a3d49f864e1badc5c831e791)
#### Saturday 2023-08-26 19:49:27 by SkyratBot

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
## [Ankitsindoriya/ANKIT-Django-portfolio.github.io](https://github.com/Ankitsindoriya/ANKIT-Django-portfolio.github.io)@[98995f5aa7...](https://github.com/Ankitsindoriya/ANKIT-Django-portfolio.github.io/commit/98995f5aa75671b59608d7b5adeff1a3a39c48e6)
#### Saturday 2023-08-26 20:02:20 by ANKIT SINDORIYA

Update README.md

Project Name: MyDjangoWebsite

Description:

MyDjangoWebsite is a dynamic web application developed using the Django web framework. This project showcases my skills in web development, leveraging the power and flexibility of Django to create a feature-rich online platform.

Key Features:

Modern Web Development: Built using the latest web development practices and Django's best practices, providing a solid foundation for scalability and maintainability.

User-Friendly Interface: A user-friendly interface designed for optimal user experience. Seamlessly navigate through pages, interact with dynamic content, and enjoy smooth interactions.

Database Management: Utilizes Django's ORM to efficiently manage data. Models define the data structure and relationships, while the admin interface simplifies data management tasks.

Secure by Design: Implements security measures to guard against common web vulnerabilities, ensuring a robust and safe environment for users.

Modular and Extensible: Structured using Django's app-based architecture, enabling easy integration of new features and functionalities. Each app encapsulates specific functionalities.

Responsive Design: Designed to be responsive across various devices, ensuring a consistent and engaging experience on desktops, tablets, and smartphones.

Usage:

Clone the repository: git clone https://github.com/yourusername/MyDjangoWebsite.git
Create a virtual environment: python -m venv venv
Activate the virtual environment: source venv/bin/activate (Linux/macOS) or venv\Scripts\activate (Windows)
Install dependencies: pip install -r requirements.txt
Configure database settings in settings.py
Apply migrations: python manage.py migrate
Create a superuser for the admin panel: python manage.py createsuperuser
Run the development server: python manage.py runserver

---
## [wilbertpol/mame](https://github.com/wilbertpol/mame)@[e97630981c...](https://github.com/wilbertpol/mame/commit/e97630981c406ba446e2d7fb1bf8ecf8d3a6b93b)
#### Saturday 2023-08-26 20:26:56 by A-Noid33

Added software list for cracked Macintosh floppy images. (#11454)

New working software list items (mac_flop_orig.xml)
-------------------------------
Alter Ego (male version 1.0) (san inc crack) [4am, san inc, A-Noid]
Alter Ego (version 1.1 female) (san inc crack) [4am, san inc, A-Noid]
Alternate Reality: The City (version 3.0) (san inc crack) [4am, san inc, A-Noid]
Animation Toolkit I: The Players (version 1.0) (4am crack) [4am, A-Noid]
Balance of Power (version 1.03) (san inc crack) [4am, san inc, A-Noid]
Borrowed Time (san inc crack) [4am, san inc, A-Noid]
Championship Star League Baseball (san inc crack) [4am, san inc, A-Noid]
Cutthroats (release 23 / 840809-C) (4am crack) [4am, A-Noid]
CX Base 500 (French, version 1.1) (san inc crack) [4am, san inc, A-Noid]
Deadline (release 27 / 831005-C) (4am crack) [4am, A-Noid]
Defender of the Crown (san inc crack) [4am, san inc, A-Noid]
Deluxe Music Construction Set (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Déjà Vu (version 2.3) (4am crack) [4am, A-Noid]
Déjà Vu: A Nightmare Comes True!! (san inc crack) [4am, san inc, A-Noid]
Déjà Vu II: Lost in Las Vegas!! (san inc crack) [4am, san inc, A-Noid]
Dollars and Sense (version 1.3) (4am crack) [4am, A-Noid]
Downhill Racer (san inc crack) [4am, san inc, A-Noid]
Dragonworld (4am crack) [4am, A-Noid]
ExperLisp (version 1.0) (4am crack) [4am, A-Noid]
Forbidden Castle (san inc crack) [4am, san inc, A-Noid]
Fusillade (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Geometry (version 1.1) (4am crack) [4am, A-Noid]
Habadex (version 1.1) (4am crack) [4am, A-Noid]
Hacker II (san inc crack) [4am, san inc, A-Noid]
Harrier Strike Mission (san inc crack) [4am, san inc, A-Noid]
Indiana Jones and the Revenge of the Ancients (san inc crack) [4am, san inc, A-Noid]
Infidel (release 22 / 840522-C) (4am crack) [4am, A-Noid]
Jam Session (version 1.0) (4am crack) [4am, A-Noid]
Legends of the Lost Realm I: The Gathering of Heroes (version 2.0) (4am crack) [4am, A-Noid]
Lode Runner (version 1.0) (4am crack) [4am, A-Noid]
Mac Pro Football (version 1.0) (san inc crack) [4am, san inc, A-Noid]
MacBackup (version 2.6) (4am crack) [4am, A-Noid]
MacCheckers and Reversi (4am crack) [4am, A-Noid]
MacCopy (version 1.1) (4am crack) [4am, A-Noid]
MacGammon! (version 1.0) (4am crack) [4am, A-Noid]
MacGolf (version 2.0) (4am crack) [4am, A-Noid]
MacWars (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 1.10) (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 2.00h) (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 3.4a) (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 4.0) (san inc crack) [4am, san inc, A-Noid]
Math Blaster (version 1.0) (4am crack) [4am, A-Noid]
Maze Survival (san inc crack) [4am, san inc, A-Noid]
Microsoft Excel (version 1.00) (san inc crack) [4am, san inc, A-Noid]
Microsoft File (version 1.04) (san inc crack) [4am, san inc, A-Noid]
Mindshadow (san inc crack) [4am, san inc, A-Noid]
Moriarty's Revenge (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Moriarty's Revenge (version 1.03) (4am crack) [4am, A-Noid]
Mouse Stampede (version 1.00) (4am crack) [4am, A-Noid]
Murder by the Dozen (Thunder Mountain) (4am crack) [4am, A-Noid]
My Office (version 2.7) (4am crack) [4am, A-Noid]
One on One (san inc crack) [4am, san inc, A-Noid]
Orb Quest: Part I: The Search for Seven Wards (version 1.04) (san inc crack) [4am, san inc, A-Noid]
Patton Strikes Back (version 1.00) (san inc crack) [4am, san inc, A-Noid]
Patton vs. Rommel (version 1.05) (san inc crack) [4am, san inc, A-Noid]
Pensate (version 1.1) (4am crack) [4am, A-Noid]
PFS File and Report (version A.00) (4am crack) [4am, A-Noid]
Physics (version 1.0) (4am crack) [4am, A-Noid]
Physics (version 1.2) (4am crack) [4am, A-Noid]
Pinball Construction Set (version 2.5) (san inc crack) [4am, san inc, A-Noid]
Pipe Dream (version 1.2) (4am crack) [4am, A-Noid]
Professional Composer (version 2.3Mfx) (san inc crack) [4am, san inc, A-Noid]
Q-Sheet (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Rambo: First Blood Part II (san inc crack) [4am, san inc, A-Noid]
Reader Rabbit (version 2.0) (4am crack) [4am, A-Noid]
Rogue (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Seastalker (release 15 / 840522-C) (4am crack) [4am, A-Noid]
Seven Cities of Gold (san inc crack) [4am, san inc, A-Noid]
Shadowgate (san inc crack) [4am, san inc, A-Noid]
Shanghai (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Shufflepuck Cafe (version 1.0) (4am crack) [4am, A-Noid]
Sierra Championship Boxing (4am crack) [4am, A-Noid]
SimCity (version 1.1) (4am crack) [4am, A-Noid]
SimCity (version 1.2, black & white) (4am crack) [4am, A-Noid]
SimEarth (version 1.0) (4am crack) [4am, A-Noid]
Skyfox (san inc crack) [4am, san inc, A-Noid]
Smash Hit Racquetball (version 1.01) (san inc crack) [4am, san inc, A-Noid]
SmoothTalker (version 1.0) (4am crack) [4am, A-Noid]
Speed Reader II (version 1.1) (4am crack) [4am, A-Noid]
Speller Bee (version 1.1) (4am crack) [4am, A-Noid]
Star Trek: The Kobayashi Alternative (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Stratego (version 1.0) (4am crack) [4am, A-Noid]
Suspect (release 14 / 841005-C) (4am crack) [4am, A-Noid]
Tass Times in Tonetown (san inc crack) [4am, san inc, A-Noid]
Temple of Apshai Trilogy (version 1985-09-30) (san inc crack) [4am, san inc, A-Noid]
Temple of Apshai Trilogy (version 1985-10-08) (san inc crack) [4am, san inc, A-Noid]
The Chessmaster 2000 (version 1.02) (4am crack) [4am, A-Noid]
The Crimson Crown (san inc crack) [4am, san inc, A-Noid]
The Duel: Test Drive II (san inc crack) [4am, san inc, A-Noid]
The Hitchhiker's Guide to the Galaxy (release 47 / 840914-C) (4am crack) [4am, A-Noid]
The King of Chicago (san inc crack) [4am, san inc, A-Noid]
The Lüscher Profile (san inc crack) [4am, san inc, A-Noid]
The Mind Prober (version 1.0) (san inc crack) [4am, san inc, A-Noid]
The Mist (san inc crack) [4am, san inc, A-Noid]
The Quest (4am crack) [4am, A-Noid]
The Slide Show Magician (version 1.2) (4am crack) [4am, A-Noid]
The Surgeon (version 1.5) (san inc crack) [4am, san inc, A-Noid]
The Toy Shop (version 1.1) (san inc crack) [4am, san inc, A-Noid]
The Witness (release 22 / 840924-C) (4am crack) [4am, A-Noid]
ThinkTank 128 (version 1.000) (4am crack) [4am, A-Noid]
Uninvited (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Uninvited (version 2.1D1) (san inc crack) [4am, san inc, A-Noid]
Where in Europe is Carmen Sandiego? (version 1.0) (4am crack) [4am, A-Noid]
Winter Games (version 1985-10-24) (san inc crack) [4am, san inc, A-Noid]
Winter Games (version 1985-10-31) (san inc crack) [4am, san inc, A-Noid]
Wishbringer (release 68 / 850501-D) (4am crack) [4am, A-Noid]
Wizardry: Proving Grounds of the Mad Overlord (version 1.10) (san inc crack) [4am, san inc, A-Noid]
Zork II (release 48 / 840904-C) (4am crack) [4am, A-Noid]
Zork III (release 17 / 840727-C) (4am crack) [4am, A-Noid]

---
## [ImSpiDy/kernel_xiaomi_lavender-4.19](https://github.com/ImSpiDy/kernel_xiaomi_lavender-4.19)@[39d3dacd34...](https://github.com/ImSpiDy/kernel_xiaomi_lavender-4.19/commit/39d3dacd349e628a59ed3037b9f0b16558de40c6)
#### Saturday 2023-08-26 20:53:18 by Dan Pasanen

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
## [wardbell/angular](https://github.com/wardbell/angular)@[3838aaab4d...](https://github.com/wardbell/angular/commit/3838aaab4d65531b5cb72a50faea041841275737)
#### Saturday 2023-08-26 21:31:22 by Ward Bell

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

**Revised "RxJS Library* page and code**

*RxJS no longer supports chaining* and hasn't for a very long time. Removed note in `rx-library.md` that suggested you could use operator chaining.

The RxJS `pipe` discussion in the "Operators" section was just weird. Almost no one calls the `pipe` function. We certainly should *start* there. We should start with how people actually use operators - by adding them to the argument list of the `Observable.pipe()` method.

I kept the original `pipe` function example but subordinated it in a "callout". Most readers will (and should) ignore it.

`Subject` is a *critically important RxJS mechanism for creating custom observables*. It was completely missing from the list of observable creators on this guide page. So I added it to the "Observable creation functions" section of the guide and wrote an accompanying `MessageService` code sample (see the new `rx-library/app/` folder).

The `MessageService` is a pretty common pattern in Angular apps - far more common than creating an observable from a counter or an event, two of the creation patterns currently on this page.

This new section also afforded an opportunity to show how RxJS helps with building loosely coupled applications. We will soon be talking about Signals. Many will wonder whether and when they should still use RxJS.

At least a partial answer is that RxJS is really good at progressively combining and enhancing streams of data as they cross component boundaries. Of course you can pass signals around; but they are not as rich in transformers as RxJS. This is where RxJS shines.

---

