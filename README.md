## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-12-28](docs/good-messages/2023/2023-12-28.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,785,868 were push events containing 3,618,310 commit messages that amount to 199,049,752 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 51 messages:


## [bruceSz/pytorch](https://github.com/bruceSz/pytorch)@[ddf1cb7870...](https://github.com/bruceSz/pytorch/commit/ddf1cb78705dcf79fe8c8df01f6f18ca4a218c55)
#### Thursday 2023-12-28 00:02:03 by voznesenskym

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
ghstack dependencies: #113926

---
## [Cthulhu80/cmss13](https://github.com/Cthulhu80/cmss13)@[fa754d7a7f...](https://github.com/Cthulhu80/cmss13/commit/fa754d7a7f71e0a10b8b424037cf344d82d653b0)
#### Thursday 2023-12-28 00:05:25 by InsaneRed

Fixes synths being unlungeable while in "critical state" (#5303)

# About the pull request

Synths were given immunity to dragging from old code back when they
could go into 'crit' so they dont get dragged to hell, however they no
longer have a crit state but still keep the immunity lunges also do not
work because of this. this is not intended.

# Explain why it's good for the game

bugfix


# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>
yeah i tested it also no you cant get dragged while dead

</details>


# Changelog
:cl:
fix: Synths are no longer immune to lunges / dragging while in 'critical
state' since they dont go into crit.
/:cl:

Co-authored-by: InsaneRed <prodexter31@outlook.comm>

---
## [ReturnToZender/ReturnsBubber](https://github.com/ReturnToZender/ReturnsBubber)@[8f3d1036c8...](https://github.com/ReturnToZender/ReturnsBubber/commit/8f3d1036c8f4f7b51acc6bad8b28009a81e20ac4)
#### Thursday 2023-12-28 00:05:39 by SkyratBot

[MIRROR] Refactor icemoon wolves into basic mobs and add taming + pack behavior [MDB IGNORE] (#25126)

* Refactor icemoon wolves into basic mobs and add taming + pack behavior (#79736)

## About The Pull Request

Ports icemoon wolves over to the basic mob framework with a bit of extra
stuff:

- Wolves call for help when attacked within a decently large radius.
Because you know, pack animals.
- Wolves can now be tamed with a slab of meat
- When tamed, wolves can be ridden like goliath mounts. Ride wolf, life
good. Pretend you're playing ARK and start shivering to death in thatch
huts for that High Roleplay experience.
- Tamed wolves have access to a bunch of pet commands (following, point
fetching, point attacking, play dead, etc) and will also defend their
owners vehemently if they're attacked.

You can probably tame multiple if you wanted to.

## Why It's Good For The Game

What part about riding wolves isn't entertaining? I don't really play
/tg/ that much so I can't argue too much about the balance implications
this might pose, but it's undoubtedly a stupid little gimmick and is
likely to be used by bored assistants and miners with too much time on
their hands.

Especially robust individuals will probably find a million things to do
with a basic mob capable of fetching, attacking on command and generally
being able to defend themselves decently well.

## Changelog

:cl: yooriss
refactor: Icemoon wolves now use the basic mob framework and should act
more intelligently, defending their pack.
add: Icemoon wolves can be tamed with slabs of meat and can be ridden as
mounts once friendly. Being rather large dogs, they also have access to
most of the pet commands you'd expect, such as fetching things, and
violently mauling people their owners point at.
/:cl:

---------

Co-authored-by: san7890 <the@ san7890.com>

* Refactor icemoon wolves into basic mobs and add taming + pack behavior

---------

Co-authored-by: Ephemeralis <Ephemeralis@users.noreply.github.com>
Co-authored-by: san7890 <the@ san7890.com>

---
## [an0rak-dev/Avatar](https://github.com/an0rak-dev/Avatar)@[a064cfcc4f...](https://github.com/an0rak-dev/Avatar/commit/a064cfcc4f40ff2d9caf30abc545ae15333b4cb2)
#### Thursday 2023-12-28 00:19:54 by Sylvain Nieuwlandt

Add Readme, License and CI.

It's not because I'm working alone on this that I should work as a
savage. I thought it will be fun to integrate the linting steps as
reviews from the github action bot (Yeah, I know it might not sound
fun but it is !).

Got a MetaQuest 3 for Christmas from my insanely crazy wife. Guess
that this project will take another slow down because I'll try to
create a commercial game with it.

Changelog: other

---
## [axiangcoding/langchain](https://github.com/axiangcoding/langchain)@[d4f45b1421...](https://github.com/axiangcoding/langchain/commit/d4f45b1421ec8b56fe6aeed84f81ca1b3f91383f)
#### Thursday 2023-12-28 00:31:25 by Sypherd

core(minor): Allow explicit types for ChatMessageHistory adds (#14967)

<!-- Thank you for contributing to LangChain!

Replace this entire comment with:
  - **Description:** a description of the change, 
  - **Issue:** the issue # it fixes (if applicable),
  - **Dependencies:** any dependencies required for this change,
- **Tag maintainer:** for a quicker response, tag the relevant
maintainer (see below),
- **Twitter handle:** we announce bigger features on Twitter. If your PR
gets announced, and you'd like a mention, we'll gladly shout you out!

Please make sure your PR is passing linting and testing before
submitting. Run `make format`, `make lint` and `make test` to check this
locally.

See contribution guidelines for more information on how to write/run
tests, lint, etc:
https://python.langchain.com/docs/contributing/

If you're adding a new integration, please include:
1. a test for the integration, preferably unit tests that do not rely on
network access,
2. an example notebook showing its use. It lives in `docs/extras`
directory.

If no one reviews your PR within a few days, please @-mention one of
@baskaryan, @eyurtsev, @hwchase17.
 -->
## Description
Changes the behavior of `add_user_message` and `add_ai_message` to allow
for messages of those types to be passed in. Currently, if you want to
use the `add_user_message` or `add_ai_message` methods, you have to pass
in a string. For `add_message` on `ChatMessageHistory`, however, you
have to pass a `BaseMessage`. This behavior seems a bit inconsistent.
Personally, I'd love to be able to be explicit that I want to
`add_user_message` and pass in a `HumanMessage` without having to grab
the `content` attribute. This PR allows `add_user_message` to accept
`HumanMessage`s or `str`s and `add_ai_message` to accept `AIMessage`s or
`str`s to add that functionality and ensure backwards compatibility.

## Issue
* None

## Dependencies
* None

## Tag maintainer
@hinthornw
@baskaryan 

## Note
`make test` results in `make: *** No rule to make target 'test'.  Stop.`

---
## [winterboekje/tgstation](https://github.com/winterboekje/tgstation)@[7fce8cd805...](https://github.com/winterboekje/tgstation/commit/7fce8cd8054cc1d0b048db12d7e9587b42fcdef2)
#### Thursday 2023-12-28 00:50:28 by san7890

Codifies male goats not having an udder (#79722)

## About The Pull Request

This was addressed in #78759 (1b1fde4908826ef5c54ffc0734e74028270af3fd)
and reviewed (and merged even though I didn't respond to it, oh well),
but I half-assed it because the whole point was to prevent male goats
from having an udder, but I only added it to the subtype of Pete i made
in that PR. Let's expand that to all male goats now.
## Why It's Good For The Game

It doesn't make biological nor morphological sense as to why a male goat
can provide milk. Ideally this should be like this for all animals
(because that's real life) but that's a later issue with further balance
implication.

I think it's still an interesting idea that Nanotrasen will just send
you any old goat despite it being "useless" beyond being very good at
eating plants. Maybe cargo should have a way to guarantee getting a
female goat in the future? It's just like real life where zoos and farms
have to constantly dealw ith female animals (such as giraffes or other
exotic stuff) tending to be far rarer/cost far more than their male
variants due to the potential to generate offspring (there's more nuance
to husbandry than this but just play along)... and in space, every
animal is "exotic".

It still remains possible to biogenerate milk, which tends to be far
faster than feeding/milking goats- which is something that the cook
should have access to anyways.
## Changelog
:cl:
balance: Male Goats should no longer spawn with an udder, instead of it
just being Pete.
/:cl:

---------

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [Shroopy/tgstation](https://github.com/Shroopy/tgstation)@[66b8b1d866...](https://github.com/Shroopy/tgstation/commit/66b8b1d8669379eac50fa358a3eb5e7707b46f25)
#### Thursday 2023-12-28 01:06:49 by Fikou

Revert "if you die in a mech you are ejected" (#79768)

Reverts tgstation/tgstation#79380
this is literally what the mech removal tool is for. gameplay reasons
for that tool missing do not mean that we need to remove its use - if
you want a better solution then let people purchase it... or just smash
the mech- you saving their life and them being sad about their mech is
really funny
the original pr being marked as qol when that was a specific balance
change is very stupid

## Changelog
🆑
del: if you die in a mech you again don't automatically eject
/🆑

---
## [Jolly-66/tgstation](https://github.com/Jolly-66/tgstation)@[33e10634ba...](https://github.com/Jolly-66/tgstation/commit/33e10634ba89c28c1ca3518068e916ec0a10b33e)
#### Thursday 2023-12-28 01:09:15 by Iamgoofball

Fixes Holy Water performing water metabolization twice, giving more blood and making you less drunk (#80440)

## About The Pull Request

~~Fixes Holy Water taking double the time it's supposed to take to
deconvert, and fixes it metabolizing out at twice the normal speed.~~

Fixes Holy Water performing water metabolization twice, giving more
blood and making you less drunk

## Why It's Good For The Game

lmfao ~~this is why deconversion for cult sucked~~ so bad

## Changelog

:cl:
fix: Fixes Holy Water giving you more blood and making you less drunk
than water normally does.
/:cl:

---
## [Sonic121x/FluffySTG](https://github.com/Sonic121x/FluffySTG)@[e44cfc63c7...](https://github.com/Sonic121x/FluffySTG/commit/e44cfc63c7451181e1b5b9dec33e6805b384c3b0)
#### Thursday 2023-12-28 01:46:52 by Iajret Creature

[THE HALF-MODULAR PRINCE] Snalance (Snail Balance) and Snissues (Snail Issues) Adjustment (#1219)

* initial d

* holy shit i forgot

* i got so much cheese in my pocket, they thought I was a fucking calzone

* opp was sneak-dissing on the 'gram, turned his city into pompeii

* Just fixing some diffs (line breaks should match tg)

* Fixes these edit comments

---------

Co-authored-by: Nerevar <12636964+Nerev4r@users.noreply.github.com>
Co-authored-by: Giz <13398309+vinylspiders@users.noreply.github.com>

---
## [Bubberstation/Bubberstation](https://github.com/Bubberstation/Bubberstation)@[25be46a37d...](https://github.com/Bubberstation/Bubberstation/commit/25be46a37dfd73308619ad393479bb06cc233ced)
#### Thursday 2023-12-28 01:51:27 by aKromatopzia

fixes for teshvali cybernetics (#900)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

# OOPS
So in the previous and now closed PR
(https://github.com/Bubberstation/Bubberstation/pull/871#issue-2049760879)
I forgot to commit changes to tgstation.dme. So while the files are now
in the code... they're not enabled. Oops.

## About The Pull Request

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

I didn't notice some more minor changes in the testmerge. This rectifies
some of that - new vars, and such. After I fix the new bugs inherent to
this... Which have now been fixed. ~~Although the current version should
still be functional, teshari cybernetic limbs take approximately 10%
more damage than they should due to the missing var. I think. The var is
weird, and honestly seems to be a redundancy? better safe than sorry.~~
This PR actually enables the previous PR and fixes some things which
would have caused minor statistical inconsistencies on the scale of
+-1-5 damage taken.
### Advanced Raptor limbs
Oh, also advanced cybernetic limbs were implemented since the downstream
made them obtainable. They're a bit brighter than the regular limbs.

![Screenshot_57](https://github.com/Bubberstation/Bubberstation/assets/94389683/9421bc98-1944-4bfe-b707-817123ab8ce1)
![Screenshot_56](https://github.com/Bubberstation/Bubberstation/assets/94389683/870b334a-ce7f-4708-ad97-e0a9d1972b42)
![Screenshot_58](https://github.com/Bubberstation/Bubberstation/assets/94389683/b681ebea-2272-4f38-87ea-adcd75a6aed7)



<!-- Please make sure to actually test your PRs. If you have not tested
your PR mention it. -->

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
fix: ACTUALLY enables teshvali cybernetics
add: advanced raptoral cybernetics
fix: some vars that were added in the downstream are now correctly
implemented.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

<!-- By opening a pull request. You have read and understood the
repository rules located on the main README.md on this project. -->

---------

Co-authored-by: Waterpig <49160555+Majkl-J@users.noreply.github.com>
Co-authored-by: projectkepler-RU <99981766+projectkepler-ru@users.noreply.github.com>

---
## [hokaze/Orcus-Compendium](https://github.com/hokaze/Orcus-Compendium)@[f4e28348fa...](https://github.com/hokaze/Orcus-Compendium/commit/f4e28348fa3ef3b6146589dfc8c839f2e2426911)
#### Thursday 2023-12-28 01:59:35 by hokaze

UPDATING TO MERGE IN CHANGES FROM ORCUS 1.0 and 1.1 RELEASES...

Orcus has had its big 1.0 release in the time since I last updated this, so let's merge all those changes in, after putting it off for months and months!

(UGH this is a mess and overly verbose for a commit message but makes sense to log procedure here to double-check I've gotten everything and to make future big merges easier)

== SOURCE MARKDOWN ==
Pretty much all the markdown files have been adjusted, so just brought those up to date, no conversions needed:

- Orcus Advanced Options - current.md
- Orcus Classes and Powers - current.md
- Orcus Player Options - current.md
- Orcus Rulebook - current.md

Can just run the markdown-to-html tools to cover things like the class descriptions, epic paths, companions, prestige paths...trickier bit is that for the table display those CSVs were made by hand, will cross that bridge later.

== SOURCE XLSX ==
This is the trickier bit, as I don't use the excel spreadsheets directly, but instead have CSVs (some of which have been adjusted to fix broken lines, image tags or added extra columns useful for the compendium) so aren't a 1:1 comparison.

Have updated the source excel files - to update the derived CSVs, have had to grab the old XLSX, convert old and new to CSV then run diffs and manually update the CSVs.

== DERIVED CSVs (from XLSX) ==

= species.csv (from Ancestries xlsx) =
- Just replaced outright, things are in a different order and my csv uses the same columns as the original with no changes that I can recall
(the compendium doesn't display all the info actually stored here IIRC, as species as an optional rule was given less priority, + was awkward to display everything for)

- For consistency with my other CSVs, have removed the <figure> and <img> tags from the few advanced ancestries that had them, as we don't use them in the compendium
(presumably Sanglorian's workflow for making those pdfs has some xslx -> markdown -> pdf steps where it made sense to include images here?)

= arts.csv (from Arts xlsx) =
- Row 72, Craft Wondrous Items, Description column ("bag of ogres" -> "bag of tricks")

- Row 75, Detect Otherworldly, Description column, fixed missing captialisation of Celestial, Demon, Devil, Undead tags

- Row 82, Forbid Intrusion, Description column, fixed missing capitalisation on Air, Celestial, Cold, Demon, Devil, Earth, Fire Water and Undead tags

- Not an actual change in the xlsx, but have removed some of the <figure> and <img> tags used to display images, as we don't use them in the compendium

= classes.csv (from Classes xlsx) =
- Row 9, Magician, Talents Text column, "Summon keyword" -> "Summons tag"

- Row 14, Shaper, 4 - Desc column, "Augmentable keyword" -> "Augmentable tag"

= companions.csv (from Companions xlsx) =
- No changes I could detect between the 2 converted xlsx files. Only real difference between the convert xlsx->csv and companions.csv is the removal of some <figure> and <img> tags orcus uses to display images in the markdown and final PDFs that is removed as the compendium doesn't use them

= powers.csv (from powers xlsx) =
- Too many to possibly list! Looking at the diffs, some powers changes lines, a lot are completely different lines where columns went from blank to being filled in, which is what I feared

- Very tricky to actually figure out what's changed per individual power, and powers.csv is one where I thought I'd made quite a few custom changes, but even with that might be easier to rebase everything off the new xlsx -> csv then bring the old csv changes forward, as I think the main differences were a few individual cell changes on a few powers and the addition of the "Summons" column which I think was purely to help link Summon powers to the relevant creature statblocks

--> Summons column:
---> Add column back in, only needed for these powers:
    Least Binding (row 215->216: Demon Toad, Hopping Imp)
    Minor Binding (row 218->219: Burner Demon, Hellhound)
    Lesser Binding (row 212->223: Vulture Demon, Hungry Maw, Hezrou)
    Prestige Binding (row 226->227: Big Burner)
    Advanced Binding (row 231->232: Frenzy Demon, Boar Demon (Nalfeshnee), Pincer Demon (Glabrezu))
    Greater Binding (row 235->236: Laughing Demon)
    Ultimate Binding (row 237->238: Balor, Marilith)
---> Flanking Echo also has the Summons tag, but the stat block for a "dimension echo" doesn't exist in companion data, so I think it literally just flanks as per the power description

--> Sources column:
---> For Disciplines, looks like the format changed, previously had "Commander (class), Priest (classes), Embodies Charisma (kit), Worships the God of Peace (kits)" which was inconsistent, sometimes singular, sometimes plural, while new format groups them together and only has classes/kits once: Commander, Priest (classes), Embodies Charisma, Worships the God of Peace (kits)"
---> Will use the new format, although in future I might want to change this slightly to make it something like "Commander (class), Priest (class)" to make it easier to detect and add in hyperlinks to the relevant classes or kits

- Could have sworn I'd made more changes to powers, but it looks like we can more or less use the converted xslx -> csv just fine and just need to add the sources column back in (not quite 1:1 as the summoning powers are now on different rows), I think I was getting mixed up with some of the CSVs derived from markdown, like feats.csv and how I add in links to powers for the handful of feats that grant powers

== DERIVED CSVs (from Markdown) ==
No existing spreadsheets, these were all manual-entered by me based on the markdown and PDFs, so good news is no big changes to columns or rows or having to convert file formats to get diffs, bad news is I have to review the markdown diffs by hand and puzzle out which changes actually correspond to the CSVs, as most of the markdown changes won't be relevant.

= cruxes.csv (from Player Options) =
- no changes I could find from the diff

= heritages.csv (from Player Options) =
- Heretic, Feature Description "You have proficiency with orbs, staffs and wands." -> "You have proficiency with the following focuses: orbs, staffs and wands."

- Mountainfolk, Feature Description, replace the description of Relentless Endurance as a feature with it as an explicit encounter power with relevant keywords and such. Also, Feature Name has dropped the "(1/encounter)" text as this is now covered by the power.
(power DOES exist in powers.csv, so can add in a new column for power and work out a link to the proper power card later, but for now will use the markdown html)

= feats.csv (from Player Options) =
- As One (Weapon Shard Feat), fixed missing capitalisation, should be "Martial tag" in description

- Extended Weapon (Weapon Shard Feat), description changed from "Your weapon shard becomes a reach weapon." to "Your weapon shard is a reach weapon."

= kits.csv (from Player Options) =
- Sculpts Their Body, Adaptable Body, should say "Transmutation tag" instead of "Transmutation keyword"...but we don't actually put the feature description in the csv, so this will be picked up automatically by the markdown-to-html conversion tool

- no changes

= prestige.csv (from Classes and Powers) =
- Spellwright path, 16th feature, Instinctive Counterspell, should be "tag" instead of "keyword" again...and again, full description not in csv to begin with, just the feature name

- no changes

= epic.csv (from Classes and Powers) =
- no changes I could find from the diff

== OTHER CHANGES ==
- For the Mountainfolk Heritage, updated heritages.js to include a link to show the powercard for Relentless Endurance, similar to how it's handle for feats that grant powers (like Acid Blast)

- Fixed powers.js excluding all the ancestry powers, now we actually need to show them for heritages and not just species

- Update README.md and compendium.html with changes and version bump to v0.12

---
## [Memerguyy/Memerguyy.github.io](https://github.com/Memerguyy/Memerguyy.github.io)@[46d153ff84...](https://github.com/Memerguyy/Memerguyy.github.io/commit/46d153ff848bfc54537929bc56df59176605583a)
#### Thursday 2023-12-28 02:02:53 by Memerguy

I FORGOT TO INCLUDE THE LINK TO THE FUCKING OH MY GOD IM SO STUPID

---
## [letangphuquy/Sandbox](https://github.com/letangphuquy/Sandbox)@[e707ca3fbc...](https://github.com/letangphuquy/Sandbox/commit/e707ca3fbc22ec540d1e88696cde0dba66fb06ef)
#### Thursday 2023-12-28 04:25:43 by Le Tang Phu Quy

connect to mongodb

yeah just analog to `Class.forname` and shit like that in Java.
Thinking how to code a web app??? Especially my designated project.
Good luck!

---
## [ma44/NCRvL-OWB](https://github.com/ma44/NCRvL-OWB)@[681cfaefb7...](https://github.com/ma44/NCRvL-OWB/commit/681cfaefb792742dd726ececefc4e2325b8bfcfb)
#### Thursday 2023-12-28 04:39:20 by Micheal Fuller

Next Update Many Changes

Fixed:
Fixed "Wet Ammo Stowage" in Vehicle tree granting 50% defense instead of 5%.

General:
Added new Main Menu Logo, credit and thanks to Lia and Scatterman for their help. Added many fixes to Trade Nodes across the map, credit and thanks to Array (Bellorisa). Max Mills and Civs that can be built in any given state raised from 20 to 30 so you are no longer restricted in where they can be built. Civs now trade for 10 Resources of each type per Civ to make Trading Micro easier.

Units:
Power Armor and Motorized Demo, AT, and MGs reduced from 2 to 1.5W. Super Mutant Infantry Org increased from 35 to 45. Super Mutant Auxilaries Org increased from 50 to 60. Nightkin Org increased from 45 to 60. Nightkin granted 10% more Soft and Hard Attack modifiers and 25% Defense modifier.

Tech:
Mechanized Forces Conventional Warfare Doctrine no longer removes Entrenchment. Combined Arms Refined Warfare Doctrine Power Armor Support 5% Soft and Hard Attack increased to 10%. Human Commanders Automated Warfare Doctrine now grants 2% Initiative to CNC Robots. Field Maintenance Automated Warfare Doctrine granted Maintence Support 15% Trickleback, -15% EXP loss, 10% Intiative, and 2 Recon. The Flesh is Weak Automated Warfare Doctrine granted 15% Hard Attack bonus to Robots and 10% Breakthrough and Soft Attack raised to 15%. Refined Construction Automated Warfare Doctrine 10% Defense and Hardness increased to 15%. Automated Distribution Automated Warfare Doctrine granted 10% Factory Output bonus. Rushed Production Doctrine Granted 0.2 Combat Width reduction to Combat Robots and Security Bots and -1% Reliability penalty removed. Self-Replicating Machinery granted 5% Conscritpion Bonus. Networked AI Automated Warfare granted 10% Max Planning bonus and Planning Speed increased to 10%. Internal Replicators Automated Warfare Doctrine Hardness and Armor increased to 15% and granted 5% Factory Output. War Games Automated Warfare CNC Robots Soft and Hard Attack bonus increased to 15%. Human Commanders Automated Warfare Doctrine Soft and Hard Attack bonus increased from 10% to 15% and Planning Speed bonus increased from 10% to 20%. Age of the Machine Automated Warfare Doctrine CNC Robots Soft and Hard Attack bonus increased to 15%. Combat Robots main stats increased by 2 and rounded up if at the decimal point. K9 Integration removed from Motorized Enforcers. Removed Warforms Technology From Implant Tree. Dog Integration no longer affects Motorized Enforcers, but now affects Sentinel Power Armor.

NCR:
Hayes's For All Tommorows Focus now grants cores on all of the Legion if he owns Quartz Site. Kimball's The Baja Homestead Act focus now grants 4 Building Slots, 2 Infrastructure, 2 Civs on every Baja State instead of 2 Building Slots, 1 Infrastructure, 1 Civs. Changed all Hayes first election focuses from 30 days to 15 each. Reduced NCR Rapid's Navy tree from 30 Days to 15 Days each. NCR's Look to the West focus now grants Sophisticated Naval Technology. Removed Shi Wargoals tree, instead just invites them. Rangers Lead the Way Spirits granted 10% Special Forces Capacity Multiplier for first spirit and 20% for the second. Added 1000 Grenade Machine Guns and a small National Spirit to the Blast From the Past focus. Changed the Full Steam Ahead Event in Hayes Focus tree to Learning From the Worst from For All Tomorrows. Moved Hayes Research Slot from For All Tomorrows to Stiffle Brotherhood Overreach. Added 5% Special Forces Capacity to Kimball's Grand Army of the Republic tree. Added 10% Special Forces Capacity Multiplier to NCR PA Army Tree. Removed Hayes's Caps Expenses penalty from Heightened Military Tensions. Changed one of Kimball's Diplomatic focuses to grant Arroyo and Vault Cores and Integration on Oregon to make up for not having a Timberline player. NCR's Mojave Victory/Loss Focuses all reduced to 7 Days each, tree trimmed, and they can now bring the War to the Legion on the 15th of September (Democracy Day) after Legion was supposed to have already declared war. Now start with Power Armor Frame and the first two Passive Upgrade technologies and Pioneer Kit. Removed Redding's Tree as I have no intents on making it playable in the future unlike Bill Calhoun and Casandra Moore.

Vault City:
Now start at 100% Intellectual support to prevent accidently losing the Selection. Moved Vault City's Sentinel Unit unlock tech to Power Armor Practice instead of The Nevada Postal Service focus. Vault City's puppet integration now grants the land of Vipers to Desert Rangers with cores for better looking borders.

Desert Rangers:
Changed Coring Lawkeeper Divisions Demolition Battalions to Fireteams. Reduced Land Doctrine Research Penalty on Starting National Spirit from -25% to -15%.

Arroyo:
Granted Spec Ops Cap 40 + 5% from game start.

New Reno:
New Reno's Chains that Bind idea now grants a 5% Spec Ops Capacity Multiplier and 40 Minimum Cap.

Shi:
Shi's Recruitment Law now grants 5% Spec Ops Capacity Multiplier.

Eureka:
Eureka Power Armor Training Idea now grants 10% and 60 Special Forces Cap instead of 5% and 50.

Mojave Territories:
Granted Spec Ops Cap 40 + 5% from game start that upgrades to 60 + 10% later in the tree after the Dam War.

Los Banditos de Baja:
Added Sophisticated Naval Technology access to the "Gulf of California" focus.

Vegas:
Added a generic Military Theorist. Securitron IC Cost reduced from 24.5 to 20, Soft and Hard Attack increased from 10 to 12.5, Piericing Increased from 20 to 30, Air Attack increased from 1.5 to 3, Armor increased from 30 to 35, Breakthrough increased from 5.5 to 10, Defense increased from 14 to 15, Speed increased from 5.5 to 6, Reliability increased 80% to 85%, Securitron Hardness increased from 45% to 50%. Added 50% Defense Increase to Securitron Upgrade Techs. Securitron Upgrade Tech Hardness increased to 50% bonus and HP bonus increased to 500%.

Legion:
Legion now starts with Intermediate Naval Technology. Removed Canine Integration from Vulpes Focuses. Ceasar's The Principate focus now grants Sophisticated Naval Technology. Ceasar's Honeyed Words focus now grants Cores on all of the NCR if he controls Boneyard. Ceasar's Aequitas focus now grants 15% Spec Ops Capacity Multiplier and 20 Minimum Capacity. Vulpes's The Harvesters focus now grants 10% Spec Ops Capacity Multiplier. Lanius Focus Tree Army EXP requirements cut in half. Ceasar's Principate focus now only requires one side to be finished to access. Cult of Vulcan's The Hammers of Vulcan focus now grants a 10% Special Forces Capacity Multiplier.

Two Sun:
Two Sun's Capital now starts with 12 Slots instead of 10 and 3 more Civilian Factories. Reduced Focus Times for Scavenging Programs, Technological Excavation, Taking Inventory, Industrial Development, Build Water Pumps in Nogales, Develop Farming in Nogales, Tombstone Garages, Hilltop Garages, Ideas are Easy, Implementation is Hard, Hiring a Real Bastard, New Products for New Buyers, Speed is the Heart of Battle, The Great Game, and Thunderstruck from 30 to 15 days each. The focuses Incorporating the Ranches and Tohono's Integration now cores Cowboy Country and Tohono instead of granting a Coring Bonus. Removed the Gente War Goal path. Weapons to Surpass Metal Gears focus now grants 1K Gauss Rifles instead of 400. Joined Arms Production focus now grants 4 Mills and Building Slots instead of 2. Energy for the Suns focus now grants 2 Power Plants of Planta Grupo and Gente City instead of Dockyards. New Industry focus now grants 6 Civs and Building Slots on Hilltop and Oputo instead of 6 on just Hilltop. Our Own Design focus now also grants Intermediate Support Tech to Two Sun. The Sanora Cohort focus now grants Chariots Technology. Dreams Fufilled focus no longer removes the Infrastructure Construction bonus. Under the Protection of the Bull Focus now frees Two Sun from Puppet Status to Legion. Ceasar's Rule starting 7 Day focus changed to be a more interesting choice and techs that were previously there have been moved later in the tree. Added 40 + 5% to Two Sun's Integrate The Rangers Focus.

Gente Del Sol:
Technological Tyrant focus now grants 1 Research Slot.

Iron Alliance:
Men of Iron National Spirit granted 5% Spec Ops capacity Multiplier.

Cypher Warband:
Now start with Intermediate Spec Ops and are granted access to Sophisticated upon joining Legion. Granted 5% More Breakthrough, and 40 and 5% Special Forces Capacity.

Painted Rock:
Now start with Intermediate Vehicles and are granted access to Sophisticated upon joining Legion.

Shale:
Added 1 Starting Research Slot.

Navajo:
Legion can no longer deny Navajo's Land Claims.

---
## [ma44/NCRvL-OWB](https://github.com/ma44/NCRvL-OWB)@[7f05045a78...](https://github.com/ma44/NCRvL-OWB/commit/7f05045a784789620726c8a095b918bab8816b2e)
#### Thursday 2023-12-28 04:46:01 by Micheal Fuller

Work In Progress Next Update

Fixed:
Fixed "Wet Ammo Stowage" in Vehicle tree granting 50% defense instead of 5%.

General:
Max Mills and Civs that can be built in any given state raised from 20 to 30 so you are no longer restricted in where they can be built.

Tech:
Mechanized Forces Conventional Warfare Doctrine no longer removes Entrenchment. Combined Arms Refined Warfare Doctrine Power Armor Support 5% Soft and Hard Attack increased to 10%. Human Commanders Automated Warfare Doctrine now grants 2% Initiative to CNC Robots. Field Maintenance Automated Warfare Doctrine granted Maintence Support 15% Trickleback, -15% EXP loss, 10% Intiative, and 2 Recon. The Flesh is Weak Automated Warfare Doctrine granted 15% Hard Attack bonus to Robots and 10% Breakthrough and Soft Attack raised to 15%. Refined Construction Automated Warfare Doctrine 10% Defense and Hardness increased to 15%. Automated Distribution Automated Warfare Doctrine granted 10% Factory Output bonus. Rushed Production Doctrine Granted 0.2 Combat Width reduction to Combat Robots and -1% Reliability penalty removed. Self-Replicating Machinery granted 5% Conscritpion Bonus. Networked AI Automated Warfare granted 10% Max Planning bonus and Planning Speed increased to 10%. Internal Replicators Automated Warfare Doctrine Hardness and Armor increased to 15% and granted 5% Factory Output. War Games Automated Warfare CNC Robots Soft and Hard Attack bonus increased to 15%. Human Commanders Automated Warfare Doctrine Soft and Hard Attack bonus increased from 10% to 15% and Planning Speed bonus increased from 10% to 20%. Age of the Machine Automated Warfare Doctrine CNC Robots Soft and Hard Attack bonus increased to 15%. Combat Robots main stats increased by 2 and rounded up if at the decimal point. K9 Integration removed from Motorized Enforcers. Removed Warforms Technology From Implant Tree. Dog Integration no longer affects Motorized Enforcers, but now affects Sentinel Power Armor.

Los Banditos de Baja:
Added Sophisticated Naval Technology access to the "Gulf of California" focus.

Two Sun:
Two Sun's Capital now starts with 12 Slots instead of 10 and 3 more Civilian Factories. Reduced Focus Times for Scavenging Programs, Technological Excavation, Taking Inventory, Industrial Development, Build Water Pumps in Nogales, Develop Farming in Nogales, Tombstone Garages, Hilltop Garages, Ideas are Easy, Implementation is Hard, Hiring a Real Bastard, New Products for New Buyers, Speed is the Heart of Battle, The Great Game, and Thunderstruck from 30 to 15 days each. The focuses Incorporating the Ranches and Tohono's Integration now cores Cowboy Country and Tohono instead of granting a Coring Bonus. Removed the Gente War Goal path. Weapons to Surpass Metal Gears focus now grants 1K Gauss Rifles instead of 400. Joined Arms Production focus now grants 4 Mills and Building Slots instead of 2. Energy for the Suns focus now grants 2 Power Plants of Planta Grupo and Gente City instead of Dockyards. New Industry focus now grants 6 Civs and Building Slots on Hilltop and Oputo instead of 6 on just Hilltop. Our Own Design focus now also grants Intermediate Support Tech to Two Sun. The Sanora Cohort focus now grants Chariots Technology. Dreams Fufilled focus no longer removes the Infrastructure Construction bonus. Under the Protection of the Bull Focus now frees Two Sun from Puppet Status to Legion. Ceasar's Rule starting 7 Day focus changed to be a more interesting choice and techs that were previously there have been moved later in the tree.

Legion:
Legion now starts with Intermediate Naval Technology. Removed Canine Integration from Vulpes Focuses. Ceasar's The Principate focus now grants Sophisticated Naval Technology. Ceasar's Honeyed Words focus now grants Cores on all of the NCR if he controls Boneyard. Ceasar's Aequitas focus now grants 15% Spec Ops Capacity Multiplier and 20 Minimum Capacity. Vulpes's The Harvesters focus now grants 10% Spec Ops Capacity Multiplier. Lanius Focus Tree Army EXP requirements cut in half.

NCR:
Hayes's For All Tommorows Focus now grants cores on all of the Legion if he owns Quartz Site. Kimball's The Baja Homestead Act focus now grants 4 Building Slots, 2 Infrastructure, 2 Civs on every Baja State instead of 2 Building Slots, 1 Infrastructure, 1 Civs. Changed all Hayes first election focuses from 30 days to 15 each. Reduced NCR Rapid's Navy tree from 30 Days to 15 Days each. NCR's Look to the West focus now grants Sophisticated Naval Technology. Removed Shi Wargoals tree, instead just invites them. Rangers Lead the Way Spirits granted 10% Special Forces Capacity Multiplier for first spirit and 20% for the second.

Arroyo:
Granted Spec Ops Cap 40 + 5% from game start.

Mojave Territories:
Granted Spec Ops Cap 40 + 5% from game start that upgrades to 60 + 10% later in the tree after the Dam War.

Shale:
Added 1 Starting Research Slot.

---
## [crawl/crawl](https://github.com/crawl/crawl)@[9677d6cc8b...](https://github.com/crawl/crawl/commit/9677d6cc8bddf1d013591b4c4c36e818a48b9c99)
#### Thursday 2023-12-28 05:09:29 by regret-index

Gloorx's level: (crawlers ->) weavers -> flayed / skulls (Ge0ff)

While I'd still like to find another home for the very sparsely used
entropy weavers, and they're a lot less harmless than demonic crawlers
were, I'll admit the former are pretty tangential to Gloorx Vloq's current
mix of skeletons, ghosts, miasma, poison, and torment. I'm swapping them
out for a mix of the first two, barring more obvious options (and while
there's only one summoning demon besides ynoxinuls). Flayed ghosts and
laughing skulls both aren't too prominent in the immediately-comparable
Tomb or Tartarus, the former has more percentage-based damage, and the
latter has unique mechanics we can play more around with.

---
## [GamingxRelic/2D-Survival-Test](https://github.com/GamingxRelic/2D-Survival-Test)@[6baae10a0d...](https://github.com/GamingxRelic/2D-Survival-Test/commit/6baae10a0d221ee4679ed8e7dd7e4ccb487f77e5)
#### Thursday 2023-12-28 05:26:17 by GamingxRelic

New ResourceNode Spawning, Beginning a Inventory System

Added new art for the tiles. Thanks Neomenight!

Reworked the resource node spawning mechanic. Instead of having a collider that moves around to each resource node spawning attempt (which was very slow), it now checks the distance from the position of the new attempted node to the last spawned node and if it is greater than or equal to the range in the parameters, it passes the check and can spawn there. This is significantly faster than it previously was. It used to be at least 0.05s per check (painfully slow) since there were usually around 70 nodes spawning for a 256 tile wide area), but now it is fast and happens by the time the game even loads in.

 Finally, began work on an inventory system. Currently, there is a function for adding items to the inventory's item array, which makes sure items don't go past their max_quantity amount. It works recursively to guarantee this.

I am very happy with the progress so far. Lastly, we are now at 24.5 hours (roughly) on the project! I really like tracking the hours on a spreadsheet, it is cool to see how much progress I am getting done in the time I work on it.

---
## [Bikatr7/Seisen](https://github.com/Bikatr7/Seisen)@[7db8b1652b...](https://github.com/Bikatr7/Seisen/commit/7db8b1652be3a779ec4ae368c5020c38e76df814)
#### Thursday 2023-12-28 05:51:00 by Bikatr7

I AM SO SORRY

Note a lot these changes are really rough and im just trying to get the commit out

Changes:
added countermeasures for mysql not installed (untested)

CSEP is now called Synonym

A FUCK TON of paths have been fixed and renamed for better clarity

A lot of documentation and style changes

Better outputs

Better naming conventions in general

Word_type is now no longer an int disugising itself as  string

better failsafe's in general for connection handling

lot more file util functions

better logging

Code is a lot neater (Still needs work)

massive database restrucurting (nobody uses this shit anyways besides me so no i will not add migration fuck you)

lot better esacaping for input sanitzation

---
## [nushell/nushell](https://github.com/nushell/nushell)@[21b3eeed99...](https://github.com/nushell/nushell/commit/21b3eeed99b3beb45b10a266ec05f4eabf897796)
#### Thursday 2023-12-28 07:43:22 by Yash Thakur

Allow spreading arguments to commands (#11289)

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

Finishes implementing https://github.com/nushell/nushell/issues/10598,
which asks for a spread operator in lists, in records, and when calling
commands.

# Description
<!--
Thank you for improving Nushell. Please, check our [contributing
guide](../CONTRIBUTING.md) and talk to the core team before making major
changes.

Description of your pull request goes here. **Provide examples and/or
screenshots** if your changes affect the user experience.
-->

This PR will allow spreading arguments to commands (both internal and
external). It will also deprecate spreading arguments automatically when
passing to external commands.

# User-Facing Changes
<!-- List of all changes that impact the user experience here. This
helps us keep track of breaking changes. -->

- Users will be able to use `...` to spread arguments to custom/builtin
commands that have rest parameters or allow unknown arguments, or to any
external command
- If a custom command doesn't have a rest parameter and it doesn't allow
unknown arguments either, the spread operator will not be allowed
- Passing lists to external commands without `...` will work for now but
will cause a deprecation warning saying that it'll stop working in 0.91
(is 2 versions enough time?)

Here's a function to help with demonstrating some behavior:
```nushell
> def foo [ a, b, c?, d?, ...rest ] { [$a $b $c $d $rest] | to nuon }
```

You can pass a list of arguments to fill in the `rest` parameter using
`...`:
```nushell
> foo 1 2 3 4 ...[5 6]
[1, 2, 3, 4, [5, 6]]
```

If you don't use `...`, the list `[5 6]` will be treated as a single
argument:

```nushell
> foo 1 2 3 4 [5 6] # Note the double [[]]
[1, 2, 3, 4, [[5, 6]]]
```

You can omit optional parameters before the spread arguments:
```nushell
> foo 1 2 3 ...[4 5] # d is omitted here
[1, 2, 3, null, [4, 5]]
```

If you have multiple lists, you can spread them all:
```nushell
> foo 1 2 3 ...[4 5] 6 7 ...[8] ...[]
[1, 2, 3, null, [4, 5, 6, 7, 8]]
```

Here's the kind of error you get when you try to spread arguments to a
command with no rest parameter:

![image](https://github.com/nushell/nushell/assets/45539777/93faceae-00eb-4e59-ac3f-17f98436e6e4)

And this is the warning you get when you pass a list to an external now
(without `...`):


![image](https://github.com/nushell/nushell/assets/45539777/d368f590-201e-49fb-8b20-68476ced415e)


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

Added tests to cover the following cases:
- Spreading arguments to a command that doesn't have a rest parameter
(unexpected spread argument error)
- Spreading arguments to a command that doesn't have a rest parameter
*but* there's also a missing positional argument (missing positional
error)
- Spreading arguments to a command that doesn't have a rest parameter
but does allow unknown arguments, such as `exec` (allowed)
- Spreading a list literal containing arguments of the wrong type (parse
error)
- Spreading a non-list value, both to internal and external commands
- Having named arguments in the middle of rest arguments
- `explain`ing a command call that spreads its arguments

# After Submitting
<!-- If your PR had any user-facing changes, update [the
documentation](https://github.com/nushell/nushell.github.io) after the
PR is merged, if necessary. This will help us keep the docs up to date.
-->

# Examples

Suppose you have multiple tables:
```nushell
let people = [[id name age]; [0 alice 100] [1 bob 200] [2 eve 300]]
let evil_twins = [[id name age]; [0 ecila 100] [-1 bob 200] [-2 eve 300]]
```

Maybe you often find yourself needing to merge multiple tables and want
a utility to do that. You could write a function like this:
```nushell
def merge_all [ ...tables ] { $tables | reduce { |it, acc| $acc | merge $it } }
```

Then you can use it like this:
```nushell
> merge_all ...([$people $evil_twins] | each { |$it| $it | select name age })
╭───┬───────┬─────╮
│ # │ name  │ age │
├───┼───────┼─────┤
│ 0 │ ecila │ 100 │
│ 1 │ bob   │ 200 │
│ 2 │ eve   │ 300 │
╰───┴───────┴─────╯
```

Except they had duplicate columns, so now you first want to suffix every
column with a number to tell you which table the column came from. You
can make a command for that:
```nushell
def select_and_merge [ --cols: list<string>, ...tables ] {
  let renamed_tables = $tables
    | enumerate
    | each { |it|
      $it.item | select $cols | rename ...($cols | each { |col| $col + ($it.index | into string) })
    };
  merge_all ...$renamed_tables
}
```
And call it like this:
```nushell
> select_and_merge --cols [name age] $people $evil_twins
╭───┬───────┬──────┬───────┬──────╮
│ # │ name0 │ age0 │ name1 │ age1 │
├───┼───────┼──────┼───────┼──────┤
│ 0 │ alice │  100 │ ecila │  100 │
│ 1 │ bob   │  200 │ bob   │  200 │
│ 2 │ eve   │  300 │ eve   │  300 │
╰───┴───────┴──────┴───────┴──────╯
```

---

Suppose someone's made a command to search for APT packages:

```nushell
# The main command
def search-pkgs [
    --install                   # Whether to install any packages it finds
    log_level: int              # Pretend it's a good idea to make this a required positional parameter
    exclude?: list<string>      # Packages to exclude
    repositories?: list<string> # Which repositories to look in (searches in all if not given)
    ...pkgs                     # Package names to search for
] {
  { install: $install, log_level: $log_level, exclude: ($exclude | to nuon), repositories: ($repositories | to nuon), pkgs: ($pkgs | to nuon) }
}
```

It has a lot of parameters to configure it, so you might make your own
helper commands to wrap around it for specific cases. Here's one
example:
```nushell
# Only look for packages locally
def search-pkgs-local [
    --install              # Whether to install any packages it finds
    log_level: int
    exclude?: list<string> # Packages to exclude
    ...pkgs                # Package names to search for
] {
  # All required and optional positional parameters are given
  search-pkgs --install=$install $log_level [] ["<local URI or something>"] ...$pkgs
}
```
And you can run it like this:
```nushell
> search-pkgs-local --install=false 5 ...["python2.7" "vim"]
╭──────────────┬──────────────────────────────╮
│ install      │ false                        │
│ log_level    │ 5                            │
│ exclude      │ []                           │
│ repositories │ ["<local URI or something>"] │
│ pkgs         │ ["python2.7", vim]           │
╰──────────────┴──────────────────────────────╯
```

One thing I realized when writing this was that if we decide to not
allow passing optional arguments using the spread operator, then you can
(mis?)use the spread operator to skip optional parameters. Here, I
didn't want to give `exclude` explicitly, so I used a spread operator to
pass the packages to install. Without it, I would've needed to do
`search-pkgs-local --install=false 5 [] "python2.7" "vim"` (explicitly
pass `[]` (or `null`, in the general case) to `exclude`). There are
probably more idiomatic ways to do this, but I just thought it was
something interesting.

If you're a virologist of the [xkcd](https://xkcd.com/350/) kind,
another helper command you might make is this:
```nushell
# Install any packages it finds
def live-dangerously [ ...pkgs ] {
  # One optional argument was given (exclude), while another was not (repositories)
  search-pkgs 0 [] ...$pkgs --install # Flags can go after spread arguments
}
```

Running it:
```nushell
> live-dangerously "git" "*vi*" # *vi* because I don't feel like typing out vim and neovim
╭──────────────┬─────────────╮
│ install      │ true        │
│ log_level    │ 0           │
│ exclude      │ []          │
│ repositories │ null        │
│ pkgs         │ [git, *vi*] │
╰──────────────┴─────────────╯
```

Here's an example that uses the spread operator more than once within
the same command call:
```nushell
let extras = [ chrome firefox python java git ]

def search-pkgs-curated [ ...pkgs ] {
  (search-pkgs
      1
      [emacs]
      ["example.com", "foo.com"]
      vim # A must for everyone!
      ...($pkgs | filter { |p| not ($p | str contains "*") }) # Remove packages with globs
      python # Good tool to have
      ...$extras
      --install=false
      python3) # I forget, did I already put Python in extras?
}
```

Running it:
```nushell
> search-pkgs-curated "git" "*vi*"
╭──────────────┬───────────────────────────────────────────────────────────────────╮
│ install      │ false                                                             │
│ log_level    │ 1                                                                 │
│ exclude      │ [emacs]                                                           │
│ repositories │ [example.com, foo.com]                                            │
│ pkgs         │ [vim, git, python, chrome, firefox, python, java, git, "python3"] │
╰──────────────┴───────────────────────────────────────────────────────────────────╯
```

---
## [SapphicOverload/Shiptest](https://github.com/SapphicOverload/Shiptest)@[247a4e02ea...](https://github.com/SapphicOverload/Shiptest/commit/247a4e02eab24ccfa191ea0447e587aeaf4c1235)
#### Thursday 2023-12-28 07:58:12 by BluBerry016

{Icemoon, Ruin} The Crashed Holemaker (#2413)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Adds a brand-new - well, [new to
shiptest](https://cohost.org/bluwu016/post/885120-a-compilation-of-my) -
ruin to the Icemoon roster, focused on the service department.

It's flavored around being an *incredibly* old NT Spaceworks vessel
that's been carved in half and crashed - what's present only being the
fore of the ship. Being mainly service-focused, it's loot is pretty dry
~~as is it's sole threat.~~
If more current-day mappers/balance-heads have any words about how to
fluff out either of those pools a bit more with the screenshots below,
lemme know. I'll listen well.

(Notarized loot summary removed as updating it was a pain in the ass,
lmao.)

It strikes me as leaning on the underwhelming side from looking at the
other ruins present here but we'll. See? I suppose? It's good practice
for me in the whole, "making something I have memorized and that looks
good normally look sicker ruined".

<details><summary>Pictures (All but SDMM Outdated)</summary>
<p>

Ignore that there's no rust, the firelocks are open here, and some
stuff's knocked around, I was testing it prior to me tacking the rust on
and took pics after running around it in-person.


![image](https://github.com/shiptest-ss13/Shiptest/assets/50649185/51a3cc54-1727-4241-9592-639f892621bf)


![image](https://github.com/shiptest-ss13/Shiptest/assets/50649185/580e39fe-bbf9-481f-aff8-cc25f860638d)

StrongDMM View:

![2023-11-09 15 02
20](https://github.com/shiptest-ss13/Shiptest/assets/50649185/5b94af63-d2d8-42bd-a823-0d300d66191f)

</p>
</details> 
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
This isn't what I intended to do when I was like, "oh yeah, I have a
goofy ahh downstream out of boredom, ya'll want some of our better
ships" but w/e here it is anyways. Ya'll need ruins. I made (another)
ruin.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: A new icemoon ruin has been added, should you be in need of service
department goodies.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: BluBerry016 <50649185+unit0016@users.noreply.github.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[54984affcd...](https://github.com/treckstar/yolo-octo-hipster/commit/54984affcd6a180bab9715ce3bf3379ae104732a)
#### Thursday 2023-12-28 09:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [swordcube/hxsdl](https://github.com/swordcube/hxsdl)@[e358ea3711...](https://github.com/swordcube/hxsdl/commit/e358ea37113f74e69eab3abec1ae24e6538e09ff)
#### Thursday 2023-12-28 09:31:11 by swordcube

library rework (W.I.P, untested)

all enums, structs, and classes now go in Types.hx, and all functions now go in SDL.hx

functions are being rewritten from scratch, we're currently at SDL_render.h right now

Types.hx is a clusterfuck of shit please do not look at it i beg of you it's a horrible mess

---
## [Midoriya-Izuku-Coder/VroomVroom](https://github.com/Midoriya-Izuku-Coder/VroomVroom)@[378abffe9f...](https://github.com/Midoriya-Izuku-Coder/VroomVroom/commit/378abffe9f059075bc7d406ba3182c9dc3ded351)
#### Thursday 2023-12-28 10:27:31 by HaysonWong

I wake up in the morning sinking halfway through the bottom there's a loud distorted screaming in my soul

Everything is dark and empty and I don't know how to fix it so I curl up in a ball and cry in the comfort of my home
I don't know why, I feel like shit
I will not see a therapist
ISWEARTOFUCKINGGODFINALVROOMVROOM

---
## [2-ajones1/AnnaJNEA](https://github.com/2-ajones1/AnnaJNEA)@[1a0382856f...](https://github.com/2-ajones1/AnnaJNEA/commit/1a0382856fcbc2501eb10363c085436028a721e0)
#### Thursday 2023-12-28 10:48:34 by anna

28/12/2023

i've spent the last few weeks scared out of my mind. for both of us! and all of that time i've been trying to...manage you. you're happy as larry one moment, furious or upset the next. i've heard you scream in the night. i've heard you crying in the mornings- do you think this is fun for me?

---
## [cam900/mame](https://github.com/cam900/mame)@[6557f865fb...](https://github.com/cam900/mame/commit/6557f865fbd6398553f7e469812f3c57ca2379ac)
#### Thursday 2023-12-28 10:54:51 by ArcadeShadow

spectrum_cass.xml: Added 112 items (110 working), and replaced one item with a better dump. (#11871)

* Replaced Bloody with a better dump. [Spectrum Computing]
* Removed Bobo (Erbe) as it is a duplicate dump.
* Cleaned up metadata based on information from Spectrum Computing.

New working software list items (spectrum_cass.xml)
--------------------------------------------
Advanced Zombie Survival Lawnmower Simulator [Spectrum Computing]
Adventures of Buratino [Spectrum Computing]
Aknadach [Spectrum Computing]
Aknadach (Softhouse) [Spectrum Computing]
Airborne Ranger (Erbe, two sided tapes) [Spectrum Computing]
Aliens: Neoplasma (v1.3, English, AY sound) [Spectrum Computing]
Aliens: Neoplasma (v1.3, English, Turbo Sound) [ZX Online]
Aliens: Neoplasma (v1.3, Russian, AY sound) [Spectrum Computing]
Aliens: Neoplasma (v1.3, Russian, Turbo Sound) [ZX Online]
Aliens: Neoplasma (v1.3, Spanish, AY sound) [Spectrum Computing]
Aliens: Neoplasma (v1.3, Spanish, Turbo Sound) [Spectrum Computing]
All Hallows: Rise of the Pumpkin [Spectrum Computing]
All Hallows: Rise of the Pumpkin (ULA Plus) [Spectrum Computing]
Alta Tension (Erbe - Serie Leyenda) [Spectrum Computing]
Angel Nieto Pole 500cc (IBSA - Serie Leyenda) [Spectrum Computing]
Autocrash [Spectrum Computing]
Black Lamp [Spectrum Computing]
Bloody Paws [Spectrum Computing]
Bloody Paws (bug fix) [Spectrum Computing]
Bomb Bomb Buster [Spectrum Computing]
Bomb Bomb Buster (first version) [Spectrum Computing]
Bomb Bomb Buster (alt) [Spectrum Computing]
Bomb Bomb Buster (easy version) [Spectrum Computing]
Captain America in the Doom Tube of Dr Megalomann [Spectrum Computing]
Comando Quatro [Spectrum Computing]
Comando Tracer [Spectrum Computing]
Corrupt [Spectrum Computing]
Cosmic Payback [Spectrum Computing]
Crimbo - A Gloop Troops Tale [Spectrum Computing]
Dirty Dozer [Spectrum Computing]
Dizzy III - Fantasy World Dizzy - Extended Edition 2023 (English, mod) [The Dizzy Fansite]
Dizzy III - Fantasy World Dizzy - Extended Edition 2023 (Russian, mod) [The Dizzy Fansite]
Doom (pre-release) [Spectrum Computing]
Doombase (System 4) [Spectrum Computing]
Emilio Butragueño Futbol 2 (large cardboard case) [Spectrum Computing]
Equinox (Erbe, medium case) [Spectrum Computing]
Equinox (Erbe - Serie Leyenda) [Spectrum Computing]
Evil Realm + Bugout [Planeta Sinclair]
Existenz: Crazy Delfox [Spectrum Computing]
Fire Desire [Spectrum Computing]
Fist-Ro Fighter [Spectrum Computing]
Frost Byte (Erbe - Serie Leyenda) [Spectrum Computing]
Funky Fungus Reloaded (English) [World of Spectrum Classic]
Funky Fungus Reloaded (French) [World of Spectrum Classic]
Funky Fungus Reloaded (German) [World of Spectrum Classic]
Funky Fungus Reloaded (Italian) [World of Spectrum Classic]
Funky Fungus Reloaded (Portuguese) [World of Spectrum Classic]
Funky Fungus Reloaded (Spanish) [World of Spectrum Classic]
Get Out of Mars [Spectrum Computing]
Gloop Troops [Spectrum Computing]
Gloop Troops: The Lost Crown [Spectrum Computing]
Hammer Boy [Spectrum Computing]
Impossible Mission (Compulogical) [Spectrum Computing]
Ivan 'Ironman' Stewart's Super Off Road Racer (MCM) [Spectrum Computing]
Jackson City [Spectrum Computing]
Justin [Spectrum Computing]
Justin and The Lost Abbey [Spectrum Computing]
Leaderboard (Erbe) [Spectrum Computing]
Load'N'Run (Italy) N. 6 - Giugno 1984 [Edicola 8 Bit]
Load'N'Run (Italy) N. 7 - Luglio-Agosto 1984 [Edicola 8 Bit]
Load'N'Run (Italy) N. 8 - Settembre 1984 [Edicola 8 Bit]
MagicAble [Spectrum Computing]
Mantronix (Zafi Chip) [Spectrum Computing]
Mapsnatch [Spectrum Computing]
Marie Celeste (Clube Nacional de Aventura, pirate) [Planeta Sinclair]
Marsmare: Alienation [Spectrum Computing]
Mega-Corp [Spectrum Computing]
Metal Man [Spectrum Computing]
Metal Man Reloaded (English) [Spectrum Computing]
Metal Man Reloaded (Czech) [Spectrum Computing]
Metal Man Reloaded (Italian) [Spectrum Computing]
Metal Man Reloaded (Polish) [Spectrum Computing]
Metal Man Reloaded (Russian) [Spectrum Computing]
Metal Man Reloaded (Spanish) [Spectrum Computing]
Metal Man Remixed [Spectrum Computing]
Mr. Hair & The Fly [Spectrum Computing]
Mr. Hair & The Fly (alt) [Lee Stevenson]
Nemesis the Warlock (Erbe) [Spectrum Computing]
Oberon 69 [Spectrum Computing]
Rana Rama [Spectrum Computing]
Robot - The Impossible Mission (QAOP keys) [Spectrum Computing]
Robot - The Impossible Mission (ZXKM keys) [Spectrum Computing]
Rubicon (Rucksack Games) [Spectrum Computing]
Rubicon (Rucksack Games, ULA Plus) [Spectrum Computing]
Schizoids (Nuova Newel) [Planeta Sinclair]
Seraphima (English) [ZOSYA entertainment]
Seraphima (Portuguese) [ZOSYA entertainment]
Seraphima (Russian) [ZOSYA entertainment]
Seraphima (Yandex Retro Games Battle v3 competition) [ZOSYA entertainment]
Simon [Spectrum Computing]
Skull & Crossbones (Dro Soft) [Spectrum Computing]
Sky Runner (Z Cobra) [World of Spectrum]
Souls Remaster [Spectrum Computing]
Space Monsters Meet THE HARDY [Spectrum Computing]
Starring Charlie Chaplin (Erbe) [Spectrum Computing]
Starring Charlie Chaplin (Erbe - Serie Leyenda) [Spectrum Computing]
The Hair-Raising Adventures of Mr. Hair [Spectrum Computing]
The Prayer of the Warrior [Spectrum Computing]
The Prayer of the Warrior (demo) [Spectrum Computing]
The World War Simulator: Part One (English) [Spectrum Computing]
The World War Simulator: Part One (Spanish) [Spectrum Computing]
The World War Simulator: Part II (Spanish) [Spectrum Computing]
Tokyo Gang [Spectrum Computing]
Toyota Celica GT Rally (Dro Soft) [Spectrum Computing]
Tus Juegos №3 [Planeta Sinclair]
W.A.R (Erbe) [Spectrum Computing]
Xarax (Potz Blitz) [Spectrum Computing]
Xecutor (Dro Soft) [World of Spectrum]
Yokai Monk (v1.7) [Spectrum Computing]
Yokai Monk (v1.8) [Spectrum Computing]

New software list items marked not working (spectrum_cass.xml)
--------------------------------------------
Cosmic Debris (ZX Data) [Spectrum Computing]
Zorro (Erbe, medium case) [Spectrum Computing]

---
## [Majkl-J/tgstation](https://github.com/Majkl-J/tgstation)@[ef52047274...](https://github.com/Majkl-J/tgstation/commit/ef520472740e57f253545c24c7526e45e47b5ec2)
#### Thursday 2023-12-28 11:07:58 by necromanceranne

[READY] The Tackleling: Unarmed bonuses and features contribute to tackle success and failure, significant outcome overhaul, among other things (#79721)

## About The Pull Request

### Tackling Outcomes

Tackling now determines success based on outcome categories. These are
derived from the typical attacker/defender roll that would have
previously determined the outcome on its own. A negative roll results in
a negative outcome, a positive roll a positive outcome, and a result of
exactly 0 resulting in a neutral outcome.

The result of your roll are then passed along to the relevant proc to
determine severity. The derived roll is multiplied by 10 (or -10 for the
negative roll to get a positive value to roll with). Then we see if our
final roll fits a severity bracket. Negative outcomes will roll to
determine their outcome, and potentially could roll a less severe
outcome than what our first roll would suggest.

For positive outcomes, the defender's melee armor reduces the severity
of the outcome.
For negative outcomes, the attacker's melee armor improves the potential
outcome and at least prevents more severe backlash. It'll still be
negative, you can't move from a negative outcome to a positive outcome
just from good armor.

Most of the outcomes are fairly similar to the current outcomes, but
with the inclusion of staggering one or both parties to make the
subsequent potential grabs _stickier_, if that makes sense.

Neutral is now a mutual stagger, but also the tackler being left
upright. It's effectively net zero.

### Blocking

Blocking is checked on impact, and results in a neutral outcome if the
defender successfully blocks. This means our tackler isn't too severely
impacted from an unsuccessful tackle

### Additional Changes

Your arms ``unarmed_effectiveness`` now contributes to the attack mod
and defense mod of tackles. For humans tackling humans, this often
results in a net neutral result. But if you have a better arm, or the
tackle target has worse arms, this can alter the outcome significantly.

Any tackler with the trait TRAIT_NOGUNS (like bezerkers, Sleeping Carp
users or the very unlikely chance ninjas are tackling while wearing
their armor) gains a bonus to their tackles.

Any suit that prevents shove knockdowns grants an attack bonus, and not
just riot armor. This now includes Mk.1 Swat suits, the ones from the
SWAT crate in cargo.

Settlers are vulnerable to tackles, much like their dwarf cousins.
They're also just as bad at tackles.

Security lockers come with gripper gloves, and the sec vendor has 5 sets
of gripper gloves as standard items. They also have a +1 skill bonus.
This should encourage people to use tackling a bit more without having
to always seek out the best gear to accomplish the task. (particularly
since security is inherently pretty good at tackling with the outcome
changes).

The HoS gets a pair of gorilla gloves in his garment bag. If he wants
them.

The shove slowdown is now a new status effect, Staggered. This is just
better functionality overall. Any instance of adding the shove slowdown
now makes our target staggered.

## Why It's Good For The Game

Tackling is a bit outdated, to say the least. Not much content has been
added for a while that isn't strictly meme content. With these changes,
tackling should be slightly more nuanced, considering elements such as
unarmed effectiveness, the presence of martial arts, and actually
properly checking block rather than notionally checking block. There is
also more opportunity to protect yourself from tackle outcomes, both
positive and negative.

It also should be a little fairer to be on the receiving end of tackles
if you have taken the time to layer up defenses against it. Attackers
often overwhelmed defenders due to numbers favoring attackers more than
defenders.

Closes some really outdated design that was resulting in some really
bizarre behaviour with regards to layered defenses against attack not
having the same meaning against tackles, if only because it was looking
for the wrong things and not even the correct parts of what it was
looking for. Namely, blocking and shielding.

The inclusion of more gripper gloves and a good outcome from using them
will hopefully incentivize people to consider tacking as a useful tool,
if a bit risky still due to the splat mechanics.

## Changelog
:cl:
balance: Judo Joe, archnemesis of Maint Khan, has begun re-airing his
midnight infomercials shilling his extremely expensive Tackle Supreme
Judo Karate Training video tapes. Unable to pass up a 'bargain',
Nanotrasen has purchased these tapes en masse. Tackling techniques have
started to improve, as well as Nanotrasen's tackling instructional
algorithms within tackle gloves.
balance: The outcomes for tackling are more equalized. It isn't as feast
or famine, and should be somewhat more controllable without becoming too
severe.
add: Blocking successfully against a tackle will force the tackle to be
a neutral outcome.
add: Unarmed effectiveness from arms now contributes to attacking with
and defending from tackles.
add: Those who refuse to use firearms (like Sleeping Carp users and
insane unholy berzerkers) are better at tackling others.
add: Riot specialized armor, and not just riot armor, now contributes
meaningfully to tackling effectiveness.
balance: MK.1 Swat Suits, the ones that come in SWAT crates, now
functions similarly to riot armor.
add: Settlers from the outer rims have noticed they aren't very good at
protecting themselves against Judo Joe's clearly discriminatory tackling
techniques.
add: Security lockers come with gripper gloves, security vendors now
sell them as standard items, and the HoS' garment bag now has a pair of
gorilla gloves. Gripper gloves have a positive skill bonus to tackling.
add: Being insane also makes you INSANELY good at tackling but also
INSANELY likely to eat shit on a whiff. DO OR DIE, BITCH.
refactor: Shoving slowdown and all its implementations now use a status
effect, Staggered.
/:cl:

---
## [Mu-L/crawl](https://github.com/Mu-L/crawl)@[645d2ae13f...](https://github.com/Mu-L/crawl/commit/645d2ae13f9e5acbda4b4080bf64c5fbcc20e7d9)
#### Thursday 2023-12-28 14:26:53 by regret-index

Spruce up each rune-guarding Pan lords' realm

The bulk of particular enemy decisions for most of the four fixed Pan lords
enemies were made ages ago, before we had nearly so many varied monsters
for almost any branch in general. Since there's been such a massive influx
of new monsters to work with compared to so far back in the past, it'd be
reasonable to further add to the gimmickry the lords themselves already
brandish, rather than focus on plain + common + weak flavour choices for
Pan vaults like occultists, large abominations, or weaker skeletons.

 * Mnoleg's level uses very few very ugly things, abominations, or
   tentacled monstrosities for a lot more protean progenitors and shadow
   demons- the former for more interesting shapechanging, the latter to
   fit the summoning (and since Tartarus lost them). There's far too many
   of the former melee-only types before extended, and Mnoleg lacks much
   for noticeable spawns beyond eyes and cacodemons- these two will both
   help. (Note: Don't use proteans beyond Zot, Zigs, and Mnoleg's floor.
   Zot non-draconians get very limited to no non-Zig drift or bleed to
   keep them distinct and dramatic.)

 * Gloorx Vloq's level loses lorocyproca and demonic crawlers for reapers
   and entropy weavers, while upgrading the skeletons hard. While this
   loses a bit of spectral flavour and demon presence, demonic crawlers
   have no real threat in Pan and there's some interest in removing
   lorocyprocas for more interesting tier-2 designs in the future.
   Meanwhile, entropy weavers still can corrode even extended characters,
   and reapers have a new effect plus aren't much prominent in Tartarus
   anymore. (This is a bit of placeholder future-proofing: if a new
   summoning tier-2 does end up existing, then shadow demons could fit
   here better over some other spawns, like shadow wraith and soul eater
   explicit placements, and those demons can replace Mnoleg's shadow
   demons.)

 * Lom Lobon's level loses arcanists and occultists, as they're pretty
   mundane mortal scholars of magic for extended. Instead, to represent
   more interesting mystics across the Dungeon, there's now small amounts
   of one conjurer from each of the Lair roulette branches- nagaraja,
   merfolk aquamancers, fenstrider witches, and jorogumo. They readily
   match up with the green deaths or blizzard demons already present, and
   while mostly not too extra dangerous at Pan depth they're more
   interesting to see than the prior options.

 * Cerebov, the most infamous and intimidating lord of Pandemonium, loses
   orange demons and crimson imps for pretty rainbow fluttering insects.
   They're definitely not the newly revised, rarely used elsewhere,
   very fire-focused sun moths.

 * Each of the unrand lords vaults places an increasing clump of demonspawn
   related to the lord in question for each rune you have on you when
   entering. Mnoleg gets corrupters (summoning), Gloorx Vloq gets black
   suns (necromancy), Lom Lobon gets blood saints (conjurations), and
   Cerebov gets warmongers (big equipment). There's not any extra in the
   given levels beyond those initial counts, though, so they shouldn't
   make the levels blend together too hard with the rest of Pan.

 * Also, the non-holy guaranteed demonic rune vaults and Mnoleg's realm
   both contain some potions of mutation now, to compensate for when the
   old potion of cure / beneficial mutation shuffling removed the (very
   delayed, unreliable, heavily guarded) potions of cure mutation in the
   holy pan level. Those holies should be revised to be less boring, at
   some point, but for now, it should make those vaults feel more
   worthwhile.

This also updates arenasprint and the chasing-across-Pan / orb run spawns
of the lords for those four new sets, a few new tile choices to reduce the
use of generic D floor and wall tiles, deals with teleport islands in Lom's
realm, and tweaks a varied number of vaults to even out some higher and
lower vault lethality ends. Maybe eventually Pan will be varied enough to
be made yet shorter and extended could be made shorter in general?...

---
## [htmambo/NootedRed](https://github.com/htmambo/NootedRed)@[334dc21935...](https://github.com/htmambo/NootedRed/commit/334dc219356ac9931d9829aa46a7b50fee02b47e)
#### Thursday 2023-12-28 14:31:00 by Visual Ehrmanntraut

Linux, fuck you

Fixes #167
Signed-off-by: Visual Ehrmanntraut <30368284+VisualEhrmanntraut@users.noreply.github.com>

---
## [ProfessorSidon/VGC-Damage-Calculator-Chinese](https://github.com/ProfessorSidon/VGC-Damage-Calculator-Chinese)@[90ebab0707...](https://github.com/ProfessorSidon/VGC-Damage-Calculator-Chinese/commit/90ebab070756a16e150c0b43c34b2618817bce6b)
#### Thursday 2023-12-28 15:23:40 by nerd-of-now

Added ??? type, remember gen/level, 2x BP button, more nat dex field conditions, minor damage adjustments

- Added the ??? type to gens 2-4, yes it's different from no typing
- The calc will now remember the last level system and gen that the user used
- Changed the 2x attack field from a dropdown list to a button
- Removed Typeless from the options for Tera Type
- Changed where Aura Wheel checks for its type change
- Changed how the calc handles ignoring abilities so that the moves that ignore abilities will also affect things like Friend Guard and Aura Break
- Added a check for Struggle to Wonder Guard
- Fixed OHKO move logic (was reverse of what it was supposed to be)
- Fixed the Hydro Steam/Utility Umbrella interaction
- Fixed the Power-Up Punch/Parental Bond interaction (a +6 Power-Up Punch would incorrectly calc for a +7 second hit)
- The calc will correctly save and export male Indeedee now
- Added a few more default abilities

---
## [Badr98-t/kernel-realme-bitra](https://github.com/Badr98-t/kernel-realme-bitra)@[a16e50806f...](https://github.com/Badr98-t/kernel-realme-bitra/commit/a16e50806f91eecefa23ffa36748ae6f33acc938)
#### Thursday 2023-12-28 16:05:19 by Wang Han

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
## [WarlockD/tgstation](https://github.com/WarlockD/tgstation)@[5f305ca5f7...](https://github.com/WarlockD/tgstation/commit/5f305ca5f7b3143360c2107102ea10ad96326839)
#### Thursday 2023-12-28 17:40:44 by ATH1909

Removes an exploit that can farm Russian revolver moodlets, adds Russian revolvers to the contraband section of games vendors (#80159)

## About The Pull Request

Fixes https://github.com/tgstation/tgstation/issues/80158 by making
curses block you from playing Russian roulette regardless of whether or
not there's a live bullet in your Russian revolver's chamber.

A Russian revolver has been added to the contraband section of each Good
Clean Fun vendor.

## Why It's Good For The Game

The bug is incredibly funny, but ~~I want GBP~~ probably should be
fixed.

There's no actual way to get (more) Russian revolvers outside of the
mapstart ones, and that can be a bit stifling to gimmicks that involve
them. And Russian roulette IS a game.

Like the roundstart ones, you could unload these vendor revolvers for
.357 bullets, but you can already just print .357 bullets from a hacked
autolathe directly, so I don't think that's an issue.

## Changelog

:cl: ATHATH
fix: Spacemen can no longer use curses to cheat at Russian roulette by
selectively blocking attempts to shoot themselves.
add: A Russian revolver has been added to the contraband section of each
Good Clean Fun vendor.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [lizardqueenlexi/orbstation](https://github.com/lizardqueenlexi/orbstation)@[45405782ed...](https://github.com/lizardqueenlexi/orbstation/commit/45405782edea70043d687f6bda6f71cb8d43bfce)
#### Thursday 2023-12-28 17:44:28 by Rhials

Deviant Crew antag panel category, Obsessed crew now shown in orbit menu, Paradox Clone orbit tab is now white (#80450)

## About The Pull Request

This rounds up the "Other" (Brainwashed, Hypnotised, Wizard Revenge, and
Obsession) antagonist category into the new "Deviant Crew" category.
This tab is white!

Obsessed crew are now displayed in the orbit panel (no other antagonists
in this group are though).

The Spacetime Aberrations (Paradox Clone) group has also been changed to
be white.

Here's how that looks:


![image](https://github.com/tgstation/tgstation/assets/28870487/415b8cbb-7ac3-4e24-9f74-466480c2aab0)
## Why It's Good For The Game

As was the case with paradox clones, observers can already discern when
a player is obsessed. It shouldn't be a pain to observe these guys,
especially when they're a more RP oriented antag that are (usually)
deserving of the audience.

I made paradox clones and obsessed the same color because they're both
in the broader spectrum of "fucked up crew".

Also converts common text entries to a single define. That is good
coding practice I think.
## Changelog
:cl: Rhials
qol: Obsessed crewmembers are now displayed in the orbit panel.
qol: The Paradox Clone orbit menu tab is now white. Neat!
/:cl:

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[da4c03da8f...](https://github.com/shiptest-ss13/Shiptest/commit/da4c03da8f9f95952acba2e0d2a236c297fed2d3)
#### Thursday 2023-12-28 17:45:49 by zevo

Nerfs legion core implanting to not be an aheal (#2590)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
The legion core implant now gives you a potent heal of all four damage
types (-100 brute -100 burn -50 tox -50 oxy) instead of a literal aheal.
It now also deals 10 clone damage as a drawback to organics/FBPS (IPCS
excluded because they cant use clone damage medicine).
Due to how adjustBruteLoss and adjustBurnLoss work, the implanted core
no longer heals mechanical bodyparts, making it mostly useless for IPCs
and FBPs only healing oxygen and toxin damage.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
1. Player accessible aheals are not good and encourage exploiting to
cure ailments or gain an advantage.
2. Synthetics could use self-surgery to implant legion cores on the go
for a safety net heal. While not necessarily bad, it was insanely
powerful as an aheal and negated the requirement of stabilizing the core
and getting another person to put it in you.
3. It had literally no drawbacks. A strong consumable healing ability is
cool, but it should come with a cost.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
fix: legion core implanting no longer aheals you on use
add: legion core implant now just does a potent organic heal with minor
clone damage when used
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: zevo <95449138+Zevotech@users.noreply.github.com>
Co-authored-by: Mark Suckerberg <mark@suckerberg.gay>

---
## [sevenfalling/ringing_bell](https://github.com/sevenfalling/ringing_bell)@[db40479921...](https://github.com/sevenfalling/ringing_bell/commit/db4047992195602139d5b2a55d8603f4ffe08c43)
#### Thursday 2023-12-28 17:52:53 by micah in public

Update README.md

(current contents - note the time)
# the ringing of the bell
we know you’re gonna feel it. it’s better than fire and sulfur isn’t it?

## who
only the Creator can make the earth shake like this. 

## why
that’s as close to being put over His knee as the u.s. government and the c.i.a. want to get. 

all unaffiliated people with this tragedy should know He’s not upset with you, but it should serve as a reminder He hears all prayers and makes life His number one priority. that’s why we were deployed this time: to make life way longer and healthier than currently imaginable through one-time, low-cost or free, single-dose formulations designed by the Creator, that we are to distribute globally. 

## what 
we’ve been referring to this as the ringing of the bell. not because we get wings. but it’s what scientists say about the earth after a great quake. 

this is because the Creator is quite upset. see the why. 

(copypasta’d from our mission23)

### Orr Chapel Quake
This earthquake’s epicentre will be located  in Sandy Hook, TN (the former unincorporated city near, now neighborhood of Mount Pleasant) in Maury county. The Rogers family farm. 

This will be a large earthquake for the CIA’s destruction of Orr Chapel ([Google Maps](https://goo.gl/maps/XMMdNdpGjU3SMMKQ8)) and the murder of all of it’s identified members. 

This quake also recognises Micah’s slain family and his family’s graveyard that was destroyed, both by or at the direction of the CIA. 

### Mount Calvary Baptist Church Quake
This earthquake’s epicentre will be located at Mount Calvary Baptist Church in Lexington, KY (4742 Todds Road). 

This will be the largest quake for the massacre that occurred there.

See: [The Massacre of Mount Calvary Baptist Church](https://github.com/sevenfalling/mount_calvary/wiki)

### The Micah Quake 
This earthquake’s epicentre will be in Jessamine county, KY. It will signal when Micah (born: Kelvin Eugene Williams on March 23, 1977) has started his mission for the Creator. This will be Micah’s 23rd mission on Earth. 

This minor quake will also be to recognize the lives lost in Jessamine county, mostly Micah’s friends, throughout the larger tragedy. 

### The TomTom Quake
This earthquake’s epicentre will be in Kanawha county (Hughes Creek), WV. It will signal when Thomas (to practically everyone TomTom, to others Thomas, born: September 23, 1978) has started his mission for the Creator. This also is TomTom’s 23rd mission on Earth. 

This minor quake will also recognize the lives lost in Kanawha county, mostly TomTom’s friends and family, throughout the larger tragedy. 

## when
any moment. please note the commit times, only We knew in advance. 

## where
this place we call earth, the whole damn thing

## media information
broadcast and print media professionals should see the media repository [here](https://github.com/sevenfalling/media).

## discussions
visit the [discussion forums](https://github.com/sevenfalling/ringing_bell/discussions) and join in. we will try to respond as much as we are pulled in, He may even answer questions after He puts this bell back together.

---
## [LibreOffice/core](https://github.com/LibreOffice/core)@[2e1f9da8a6...](https://github.com/LibreOffice/core/commit/2e1f9da8a6359c8909e087a92239aefd4851b116)
#### Thursday 2023-12-28 18:39:10 by Armin Le Grand (allotropia)

Decouple ScPatternAttr from SfxItemPool

ScPatternAttr is traditionally derived from SfxPoolItem
(or better: SfxSetItem) and held in the ScDocumentPool
as Item.

This is only because of 'using' the 'poolable'
functionality of the Item/ItemSet/ItemPool mechanism.
Lots of hacks were added to sc and Item/ItemSet/
ItemPool to make that 'work' which shows already that
this relationship is not optimal.

It uses DirectPutItemInPool/DirectRemoveItemFromPool
to do so, also with massive overhead to do that (and
with not much success). The RefCnt in the SfxPoolItem
that is used for this never worked reliably, so the
SfxItemPool was (ab)used as garbage collector (all
Items added and never removed get deleted at last
for good when the Pool goes down). For this reasons
and to be able to further get ItemSets modernized
I changed this. I did two big changes here:

(1) No longer derive ScPatternAttr from SfxItemSet/
    SfxSetItem, no longer hold as SfxPoolItem

(2) Add tooling to reliably control the lifetime of
    ScPatternAttr instances and ther uniqueness/
    reusage for memory reasons

It is now a regular non-derived class. The SfxItemSet
formally derived from SfxSetItem is now a member. The
RefCnt is now also a member (so independent from
size/data type of SfxPoolItem). All in all it's pretty
much the same size as before.

To support handling it I created a CellAttributeHelper
that is at/owned by ScDocument and takes over tooling
to handle the ScPatternAttr. It supports to guarantee
the uniqueness of incarnated ScPatternAttr instances for
a ScDocument by providing helpers like registerAndCheck
and doUnregister. It hosts the default CellAttribute/
ScPatternAttr. That default handling was anyways not
using the standard default-handling of Items/Pools.

I adapted whole SC to use that mainly by replacing calls
to DirectPutItemInPool with registerAndCheck and
DirectRemoveItemFromPool with doUnregister, BUT: This
was not sufficient, the RefCnt kept to be broken.

For that reason I decided to also do (2) in this change:
I added a CellAttributeHolder that owns/regulates the
lifetime of a single ScPatternAttr. Originally it also
contained the CellAttributeHolder, but after some
thoughts I decided that this is not needed - if there
is no ScPatternAttr set, no CellAttributeHolder is
needed for safe cleanup at destruction of the helper.

So I moved/added the CellAttributeHolder to ScPatternAttr
where it belongs more naturally anyways. The big plus is
that CellAttributeHolder is just one ptr, so not bigger
than having a simple ScPatternAttr*. That way, e.g.
ScAttrEntry in ScAttrArray did not 'grow' at all. In
principle all places where a ScPatternAttr* is used can
now be replaced by using a CellAttributeHolder, except
for construction. It is capable to be initialized with
either ScPatternAttr instances from the heap (it creates
a copy that then gets RefCounted) or allocated (it
supports ownership change at construction time).

Note that ScAttrEntry started to get more a C++ class
in that change, it has a constructor. I did not change
the SCROW member, but that should also be done.

Also made registerAndCheck/doUnregister private in
CellAttributeHelper and exclusively used by
CellAttributeHolder. That way the RefCnt works, and a
lot of code gets much simpler (check ScItemPoolCache,
it's now straightforward) and safer and ~ScPatternAttr()
uses now a hard
    assert(!isRegistered());
which shows that RefCnt works now (the 1st time?).

There can be done more (see ToDo section below) but I
myself will concentrate on getting ItemSets forward.

This decoupling makes both involved mechanisms more safe,
less complex and more stable. It also opens up
possibilities to further optimize ScPatternAttr in SC
without further hacking Item/ItemSet/ItemPool stuff.

NOTE: ScPatternAttr *should* be renamed to 'CellAttribute'
which describes what it is. The experiencd devs may know
what it does, but it is a hindrance for understanding for
attacting new devs. I already used now names like
CellAttributeHelper/CellAttributeHolder etc., but
abstained from renaming ScPatternAttr, see ToDo list below.

SfxItemSet discussion:

ScPatternAttr still contains a SfxItemSet, or better, a
SfxSetItem. For that reason it still depends on access to
an SfxItemPool (so there is acces in CellAttributeHelper).

This is in principle not needed - no Item (in the range
[ATTR_PATTERN_START .. ATTR_PATTERN_END]) needs that.
In principle ScPatternAttr could now do it's own handling
of those needed Items, however this might be done (linear
array, hash-by-WhichID, ...). The Items get translated
to and from this to the rest of the office anyways.

Note that *merging* of SfxItemSets is *still* needed what
means to have WhichID slots in SfxItemState::DONTCARE,
see note in ScPatternAttr::ScPatternAttr about that. And
there is also the Surrogates stuff which would have to be
checked.

The other extreme is to use SfxItemSet *more*, e.g. directly
derive from SfxItemSet what would make stuff easier, maybe
even get back to using the 'regular' Items like all office,
I doubt that that would be much slower, so why...?

Also possible is to remove that range of Items exclusively
used by ScPatternAttr from ScDocumentPool *completely* and
create an own Pool for them, owned by CellAttributeHelper.
That Pool might even be static global, so all SC Docs could
share all those Items - maybe even the ScPatternAttr
themselves (except the default per document). That would
remove the dependency of ScPatternAttr from a Pool
completely.

ToDo-List:
- rename ScPatternAttr to CellAttribute or similar
- use SfxItemSetFixed with range [ATTR_PATTERN_START
  .. ATTR_PATTERN_END] instead of regular SfxItemSet
  (if the copy-construtor works now...?)
- maybe create own/separate Pool for exclusive Items
- make ScAttrEntry more a C++ class by moving SCROW
  to the private section, add get/set methods and
  adapt SC

Had to add some more usages of CellAttributeHolder
to the SC Sort mechanism, there were situations where
the sorted ScPatternAttr were replaced in the Table,
but the 'sorted' ones were just ScPatternAttr*, thus
deleting the valid ones in the Table already. Using
CellAttributeHolder makes this safe, too.

Added a small, one-entry cache to CellAttributeHelper
to buffer the last found buffered ScPattrnAttr. It
has a HitRate of ca. 5-6% and brings the UnitTest
testSheetCellRangeProperties from 0m48,710s to
0m37,556s. Not too massive, but erery bit counts :-)
Also shows that after that change optimizations in
the now split functionality is possible and easy.

Change-Id: I268a7b2a943ce5ddfe3c75b5e648c0f6b0cedb85
Reviewed-on: https://gerrit.libreoffice.org/c/core/+/161244
Tested-by: Jenkins
Reviewed-by: Armin Le Grand <Armin.Le.Grand@me.com>

---
## [thecryptojimmy/pingpongpolitics](https://github.com/thecryptojimmy/pingpongpolitics)@[c63976864c...](https://github.com/thecryptojimmy/pingpongpolitics/commit/c63976864c71893d5677ec88cc21563f4473573d)
#### Thursday 2023-12-28 18:45:16 by j1mmy

Add files via upload

# Ping Pong Politics

Welcome to Ping Pong Politics, a fun and engaging ping pong game created by Jimmy, a beginner coder. This is my first game, and I'm thrilled to share it with the GitHub community!

## About the Game

Ping Pong Politics is a simple yet captivating game where players control paddles to hit a ball back and forth, similar to traditional ping pong or table tennis. The game features a political theme with paddles representing different political figures.

### Features

- Single-player mode against an AI opponent.
- Two-player mode for local multiplayer fun.
- Custom graphics and sound effects to enhance the gaming experience.

### How to Play

- In single-player mode, use the `W` and `Z` keys to move the left paddle up and down.
- In two-player mode, the right paddle can be controlled with the Up and Down arrow keys.
- The objective is to hit the ball past your opponent's paddle.

## Technical Details

The game is developed using Python and Pygame, a set of Python modules designed for writing video games. It demonstrates basic game development concepts such as game loops, event handling, collision detection, and more.

### What Can Be Improved

- Adding more features and power-ups to enhance gameplay.
- Implementing an online multiplayer mode.
- Enhancing the AI for a more challenging experience.
- Refining the graphics and user interface for a more polished appearance.

## Installation

To play the game, you'll need Python and Pygame installed on your computer. You can download the game's source code from this repository and run it locally.

## Feedback and Contributions

As a beginner in coding and game development, I welcome feedback and contributions to improve Ping Pong Politics. Feel free to fork the repository, make changes, and submit pull requests. Any suggestions or tips are also greatly appreciated!

Thank you for checking out my first game. I hope you enjoy playing Ping Pong Politics!

Best regards,
Jimmy

---
## [lavillastrangiato/lvs-aurora](https://github.com/lavillastrangiato/lvs-aurora)@[8e6b4cc633...](https://github.com/lavillastrangiato/lvs-aurora/commit/8e6b4cc63352160f8716441bc9d59f0752f8a5fb)
#### Thursday 2023-12-28 19:30:16 by RustingWithYou

More Ninja Hardsuits & Gear Crates (#18020)

* ninja hardsuits

but here's the warbler

balance tweaks to bug armor

yeah??? fucker.

we're so back we're so back we're so

and icons

changelog and syntax fixes

guh

* oops

* rig nerf

---
## [unit0016/effigy-se](https://github.com/unit0016/effigy-se)@[91722f5826...](https://github.com/unit0016/effigy-se/commit/91722f58264d1e4cffed9c0960e1e47287029a15)
#### Thursday 2023-12-28 19:32:17 by SSensum

New Quirk! Cyborg Lover! (#80023)

## About The Pull Request

This PR adds a new quirk for people, who want to play as
silicon-friendly crew.

Basic quirk info:
- It costs 2 points.
- It has minor additions to person's mail goodies list (cable coils,
basic cells, etc).
- It has a few simple mood events, when you pet a borg or being
touched/hugged by borg.

## Why It's Good For The Game

I think it is nice to have a chance to play as ~~robo-creep~~ person who
loves borgos.

## Changelog

:cl:
add: Added new quirk: Cyborg Lover!
/:cl:

---------

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [Grifthegnome/OutlawMod](https://github.com/Grifthegnome/OutlawMod)@[beaa0abf86...](https://github.com/Grifthegnome/OutlawMod/commit/beaa0abf8639412a8921d39650ff57f4621c73da)
#### Thursday 2023-12-28 20:02:13 by Grifthegnome

Added AiTaskReactToProjectiles, Fixed Morale Bug, Changed AiTaskStayCloseToHerd to take combat into account, AI LKP improvements. ManagedEntityArray Class.

AiTaskReactToProjectiles
1. AI With this task will aggro to an entity that shot a projectile when that projectile passes near them. This makes them look smarter and more responsive when they ecounter near misses.
2. I had to write an entity manager system to track all projectiles, as WalkInteractveEntities no longer tracks EntityProjectiles or EntityItems.
3. Currently this tracks all protiles in one pool, but we should really distinguish between projectiles in flight and ones that have landed.

Fixed Morale Bug
1. Fixed a bug where an if statement was checking AI Awareness incorrectly.

AITaskStayCloseToHeard Now Accounts For Combat
1.When an AI looks for a new herd master, it will prioritize herd members that are in combat.

Improved Lask Known Position
1. Added "attackEntity" notification that is caught by AiTaskShootProjectileAtEntity and AiTaskPersueAndEngageEntity. This sets the last known positon for these behaviors based on events the AI percieve, such as a passing arrow or an friendly who gets killed, this allows the AI to react much more dynamically as a group and seek out the source of an attack.
2. The result is that the AI push players much more agressively.

ManagedEntityArray Class
1. This is a self compacting array class that does not allow sparse entries.
2. Any time its contents are gotten or counted it removes all null entires.
3. This is an ideal structure for tracking Entities that frequently become invalid at runtime.

---
## [WEareinthebeam/restoration-mod](https://github.com/WEareinthebeam/restoration-mod)@[935e0b655d...](https://github.com/WEareinthebeam/restoration-mod/commit/935e0b655d61cd1badc0fd572d5d23a4135006dc)
#### Thursday 2023-12-28 20:20:35 by Noep

Added support for RJC's BOCW G11-at-home

fuck you 3arc

---
## [MatiasPastori/VEManager](https://github.com/MatiasPastori/VEManager)@[8047c19260...](https://github.com/MatiasPastori/VEManager/commit/8047c192607707a8aaf615c91cd0a6d0820108d6)
#### Thursday 2023-12-28 20:22:30 by MatiasPastori

Major changes:

Messed around with the default presets values (Still needs some work, specially in the case where we are transitioning from deep night into morning)

VEM now supports default presets to be replaced for another registered dynamic preset.

Refactor/Stability, changes in the time module
There was a bug that allowed old presets from a past map to still be in the lists of the sorted presets when a new map begun.

Now we have a vanilla preset placeholder that gets filled up getting the default values while we load the presets on level load. The Vanilla preset will be loaded as a default until the user indicates via chat which preset does he want or when he enables the time cycle.

Added utility functions for tables.

TODO : We need to find a better way of iterating through the presets when the time cycle is enabled, as it is right now we are iterating through ALL of the sorted presets causing the presets, that aren't the current nor the next, to be initiliazed and destroyed in a matter of seconds for nothing.
Haven't seen any performance issue TBH but it would be nice to do this in another way (couldn't find out a better one yet)

this commit is way to long :S

Refactored the VEM server script to be similar to the client one as a separated file and now the chat commands work properly.

Patches seems to be working fine, brought some stuff from Darkness Unleashed regarding spotlights and such.

---
## [Ua-Gi-Oh/UA_EDO](https://github.com/Ua-Gi-Oh/UA_EDO)@[45953ba79d...](https://github.com/Ua-Gi-Oh/UA_EDO/commit/45953ba79df9139c0efd68abc70ed5379bb1d29e)
#### Thursday 2023-12-28 20:44:05 by Ua-Gi-Oh

Перекладені карти

1 - Kozaky's Self-Destruct Button
2 - Cupid Pitch
3 - Heroic Advance
4 - Evil HERO Lightning Golem
5 - Performapal Gentrude
6 - Mermail Abyssmegalo
7 - Dragon Horn Hunter
8 - Inzektor Giga-Weevil
9 - Beast Magic Attack
10 - Starry Knight Arrival
11 - Cipher Twin Raptor
12 - Starry Knight Balefire
13 - Steelswarm Moth
14 - Predaplant Moray Nepenthes
15 - Hero Signal
16 - Curtain of the Dark Ones
17 - Megamorph
18 - Battle Break
19 - Vampire Genesis
20 - Elemental HERO The Shining

---
## [ogbigboss/the-test-subject](https://github.com/ogbigboss/the-test-subject)@[9e13c3c4f6...](https://github.com/ogbigboss/the-test-subject/commit/9e13c3c4f6bdc61586c55d0645874775f090f65a)
#### Thursday 2023-12-28 21:12:32 by ogbigboss

"when writing as the test subject, remember to say fuck a lot" - note to self

---
## [niclaz/web3privacy](https://github.com/niclaz/web3privacy)@[3678a491d2...](https://github.com/niclaz/web3privacy/commit/3678a491d25b756a27473d46722b0ce171a13557)
#### Thursday 2023-12-28 21:50:31 by niclaz

broken links - final edits of README.md

Fixed broken urls in the repository

I used https://www.deadlinkchecker.com which listed 61 errors - only some were valid html 4** errors and so I went through the list and made the following edits:

###Edited listing: 
- Parallelchain - website url updated
- Brume wallet - website and github urls updated
- Added **sunset** to Zoker wallet - website url is broken and I can not find other information about it searching... probably a dead: https://twitter.com/etherealHunt/status/1633496991488507906
- zk money - linked the github repository instead of docs (broken URL) and added **sunset** to its status in table.
- yellow submarine - linked Medium instead of gitbooks docs (broken URL) and added **sunset** to its status in table
- left broken URL for Sacred Finance but added **sunset** to name and status entries in the table. Not a single commit in the github repository since November 2022.
- 
- CIA Protocol - added github link and **sunset** to status, no activity on Github since 2021 or twitter since 2022 and the website is down.
- Coinbook - added github link and **sunset** to status - no activity on Github since April 2022, their twitter and medium have been deleted, and website is down
- COG project - updated website user - formerly https://cogfi.org now https://cogcrypto.com/
- Boring Protocol - added Github link to project, the url for their website is broken but their project had activity 8 months ago on Github and don't seem to be in sunset state just yet. Nothing this for future revisions of the database.
- Findora CR - from research this was rebranded to zkDID (https://docs.findora.org/developers/developer-sdks/zkdid-sdk) and there was a v 0.0.1 release in November 2022... potential sunset project in future
- Notebook - their docs url was broken, edited to make it work again but this may break again as it does not seem they have it linked anywhere else online. Also searched Github and found not publicly available repository
- kycnot.me - code repository got moved to new gitlab account, updated url
- speakeasy - their website is down, domain has no SSL - I found a repo hosted by xx network and linked that instead as well as some guide I found. Possible sunset project.
- 1RPC - updated docs url and project description and set status to live
- Skiff - updated the url and added team url to database
- Ethermail - added live status and team url to database
- Semaphore - updated one url that needed redirect
- AirGap wallet - updated docs links to tezos sapling guide, added live status, github link, and team url link
- NuCypher - their website is down,  but from activity on github it looks like this might be a false positive of the broken url check (no action taken)
- AnyType - updated their github url
- Highline.dev - I think they rugged... website is broken and all I can find it a Twitter account with 0 tweets on it... adding **sunset** for now
- Decentra Life - their .app website was down, I think the .org url I found is the new one... but probably this might need to be exluded from database (not very privacy focused to be honest)
- BetterCallRaul - Seems that their website is offline, changing their link to a linktree one I found on the twitter account. Potential project sunset.
- anonZK - their Twitter https://twitter.com/AnonAZK/with_replies has not been active since April and the two tools on their subdomains are not reachable... I am adding sunset to the status, to be checked again in future.
- zkchaos - website is down, I added the Github, and after checking Twitter it looks like it might have sunset... pending review
-Namachain - added **sunset** to status and the github link. No activity on Twitter or Github in over a year.
- Sismo - added the **sunset** status as they are fading out the service, code is still available online on Github. Worth to keep listed?
Source: https://twitter.com/dhadrien_/status/1733124453523919332
-TeleBridge - found on their Twitter they rebranded in July 2023 to HYPE (https://hype-eth.com) - source: https://twitter.com/TelebridgeERC/status/1684673716154757120 - have edited their entry to point ot HYPE as it also offers web3 privacy tooling
- Automata AnyDao - updated Docs link to a Github repo of the content (404 error)
- Weavemail - rebranded as Weve and had a new url, added live status and team link to the listing
- Beepo App - updated URL and added more information to listing
- XMTP x Lens - added Github link and mainnet status


###Deleted:
- Duplicate Findora entry under 'Computing Network' section as it was already listed in 'Infrastructure' section and felt that was a more relevant category.
- Bid Shop listing - no other mention online except our repo, seems they rugged themselves.
- stealthpay.cash is a dead project, creator tweet: https://twitter.com/CryptoADong
- Void Cash - website, github, and medium have been deleted it seems, twitter account has 0 tweets. All I could find on Github was this:
https://github.com/plotchy/defi-detective/blob/c2bb3cee58223bf52ded40cfd3681e65cbb607d3/00byaddress/000faaf7c3b3c3c63f62edde58b9081525d8bc31.sol#L6
- Onion mixer - https://onionmixer.gitbook.io/onion-mixer/ is offline and only the information we have on the repo can be found: "Onion Mixer is the first decentralized protocol for anonymous cross-chain transactions." Dead project in my opinion
- AnonZK Incognito - https://incognito.anonzk.io) - like the url vcc.anonzk.io the domain is dead and twitter has low activity. Since the above reference to AnonZK is labeled **sunset** I opted to delete this to make the database more lean.
- Arcana Private NFT - links are broken, blog announcement post has been deleted, and only found a Github repo that discusses the idea but I think this feature has been killed.
- Osiris - https://www.decenternet.net/osiris - webpage is a 404 and the company seems to have pivoted away from making a web3 browser. Deleted.
- Crypviser Secure Messenger - https://crypviser.network - seems website is broken, went looking and it had issues in May 2022, and then the parent company CVNX seems to have restructured... I think this is a dead product.
source: https://twitter.com/crypviser/with_replies + https://twitter.com/CvnxGov/with_replies
- [NOTE: Personal bias in decision] deleted Cirus foundation - https://cirusfoundation.com - as from my reading it seeks to monetise user data and is actually anti-privacy in philosophical terms. I leave this link to support my claim: https://support.cirusfoundation.com/en/knowledge/the-5-vs-of-big-data
- okSign - https://www.oksign.app is broken and their Twitter has not been active since Jan 2002, with only a handful of followers, no repository found on Github. Project is deemed dead.
- Literully - searched on Twitter and found that they disolved the company in March 2022: https://twitter.com/UnconstrainedM/status/1634855659752804352



###Added

| [XMTP web3 social](https://xmtp.org/docs/use-cases/deso) | Lens Protocol and CyberConnect apps use XMTP to provide secure, private messaging to their users. | [XMPT Labs Github](https://github.com/xmtp-labs) | mainnet | - |

Came across this researching XMTP x Lens listing, decided to distinguish the two pages and code repositories

---
## [Cryomundus/Cozis-Offworld-Wares](https://github.com/Cryomundus/Cozis-Offworld-Wares)@[5b83fa3764...](https://github.com/Cryomundus/Cozis-Offworld-Wares/commit/5b83fa37640e5fb0a4591710f445d85b67c0f0cc)
#### Thursday 2023-12-28 22:13:05 by Cozi

Huge November Update

Ahoy Destructors! Cozi here, back with another "oh god why the fuck did he add this?" Update!

I know it's been a while but quite bluntly I burned out hard on HD modding, kinda lost the vision on what I wanted with this project and didn't want to return until I felt I could actually set goals that I could meet, alongside starting to finish the projects I have started here. So far we have...

-Musket is a lot better animation-wise now, alongside having a "Gunk" system where the barrel will get too dirty causing inaccuracy and require cleaning using Alt. Reload + Alt. Fire, don't clean a loaded rifle! It won't work.
(Also make sure to ram multiple times! there's now a chance to fail :] )

Next up is Blue Rum, with matt's recent changes to how stims and such work, I had to rewrite the cleaner and now rum simply to get them into a spot I'm happier with. Cleaner's... The same. Blue Rum however is not.
You can now feed you downed friends blue rum with alt. fire! It's a bit WIP so I'll likely add some limitations and such (kinda thrown together but in fairness the whole update threw me off for a month)

Also, we've added Heartstopper Cigarettes! They're a loadout only item so far but you can use them to give a little of aggro damage, but balance out your heartbeat and relieve some stun. allowing you to stay cool under pressure!

The flintlock is while still missing good spriting, in a pretty okay spot now. They're the same as the musket, sans the failchance on ramming and needing to be cleaned more often due to the smaller barrel. It's alright, not my proudest work.

Defib Fans? Uh... Sorry nothing still there.

Anywho, thanks to everyone who tested and helped me with this, you guys are the best.

---
## [effigy-se/effigy-se](https://github.com/effigy-se/effigy-se)@[4c32b30565...](https://github.com/effigy-se/effigy-se/commit/4c32b305659c00804eda67e56249b6edb92fa907)
#### Thursday 2023-12-28 22:33:16 by Time-Green

Organ movement refactor *Un-nullspaces your organs* (#79687)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

closes #53931, #70916, #53931

Organs were previously stored in nullspace. Now they are stored in their
prospective bodyparts. Bodyparts are now stored in the mob.

I've also had to refactor a lot of code concerning organ movement.
Previously, organs were only moved into bodyparts once the bodyparts
were removed. To accomodate this change, two major distinctions have
been made:

**Bodypart removal/insertion**
Called only when an organ is taken out of a bodypart. Bodypart overlays,
damage modifiers or other changes that should affect a bodypart itself
goes here.

**Mob insertion/removal**
Called when an organ is removed from a mob. This can either be directly,
by taking the organ out of a mob, or by removing the bodypart that
contains the organ. This lets you add and remove organ effects safely
without having to worry about the bodypart.

Now that we controle the movement of bodyparts and organs, we can fuck
around with them more. Summoning someones head or chest or heart will
actually kill them now (and quite violently I must say (chest summoning
gibs lol)).

https://github.com/tgstation/tgstation/assets/7501474/5efc9dd3-cfd5-4ce4-b70f-d0d74894626e

I´ve also added a unit test that violently tears apart and reconstructs
a person in different ways to see if they get put toghether the right
way

This will definitely need a testmerge. I've done a lot of testing to
make sure interactions work, but more niche stuff or my own incompetence
can always slip through.

<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

A lot of organ work is quite restricted. You can't C4 someones heart,
you cant summon their organs and a lot of exceptions have to be made to
keep organs in nullspace. This lets organs (and bodyparts) play more
nicely with the rest of the game. This also makes it a lot easier to
move away from extorgans since a lot of their unique movement code has
been removed and or generalized.

I don't like making PRs of this size (I'm so sorry reviewers), but I was
in a unique position to replace the entire system in a way I couldn't
have done conveniently in multiple PRs

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
refactor: Your organs are now inside your body. Please report any issues
with bodypart and organ movement, including exotic organ, on github and
scream at me
fix: Cases of unexpected organ movement, such as teleporting bodyparts
and organs with spells, now invokes a proper reaction (usually violent
death)
runtime: Fixes HARS runtiming on activation/deactivation
fix: Fixes lag when species swapping
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [LovliestPlant/Skyrat-tg](https://github.com/LovliestPlant/Skyrat-tg)@[41026ae8b1...](https://github.com/LovliestPlant/Skyrat-tg/commit/41026ae8b1a14b9380ca7af9885939c9f2dc060e)
#### Thursday 2023-12-28 22:34:16 by SkyratBot

[MIRROR] Replaces the fake monkey cube in Birdshot tool storage with a less lethal one, adds something else fun [MDB IGNORE] (#25365)

* Replaces the fake monkey cube in Birdshot tool storage with a less lethal one, adds something else fun (#80030)

## About The Pull Request
One of the "monkey cubes" in Birdshot's tool storage was actually a
gorilla cube. This was funny up until people realized it was a thing and
now people are using it intentionally to grief. I'd rather not.

It's a different cube now. I don't want to spoil it but it won't kill
anyone, just make people laugh.

I added a different fun item to another tile in tool storage. Again, no
spoilers, read the code if you really want to know what it was.

## Why It's Good For The Game
I like the "cube says it's a monkey but it's not" joke. It was funny
when people thought it was a monkey, used it, and got killed by it.
Problem is, people know what it is now and have used it for grief
purposes, so we can't have nice things. Gorillas are stupid hard to kill
and will de-limb people by looking at them.

I wanted to add something else fun to replace it that isn't just the
exact same joke but now it won't kill you, so I did.

## Changelog
:cl: Vekter
del: Replaced the "monkey cube" in Birdshot's tool storage with a
different "monkey cube".
add: Added a fun surprise item to Birdshot's tool storage to compensate
for the above change.
/:cl:

* Replaces the fake monkey cube in Birdshot tool storage with a less lethal one, adds something else fun

---------

Co-authored-by: Vekter <TheVekter@users.noreply.github.com>

---
## [TheWolfBunny64/gambatte-libretro](https://github.com/TheWolfBunny64/gambatte-libretro)@[4d531d931e...](https://github.com/TheWolfBunny64/gambatte-libretro/commit/4d531d931edcaa132982539755b1875b8d4dc0f8)
#### Thursday 2023-12-28 22:34:37 by Patrick Adams

New Year, New Shades, 53 Overhauled Palettes!

Happy New Year to the gambatte-libretro community! 2024 marks my 5th year of creating Game Boy palettes for everyone to use! For those who have been using my Game Boy palettes for their portable adventures on the Miyoo Mini (or even the Miyoo Mini Plus), I'd like to take this moment you thank you all! 2024 also marks the 35th anniversary of the Nintendo Game Boy, so to commemorate, a new major update is on the way! Almost all of my palettes you see here have gotten new brighter overhauls thanks to color-hex!

Context: I used to go to a Japanese site called SYNCER which made my Game Boy palettes possible; chiefly with its Color Explorer tool. Today, that tool no longer exists, so I decided to move over to color-hex. As of this update, almost all of my palettes are going to be receive brighter and better updates, whilst 53 already-existing palettes are getting new makeovers entirely. Which palettes of the 53 are changed altogether? You'll just have to go and see for yourself!

---
## [cheesePizza2/Foundation-19](https://github.com/cheesePizza2/Foundation-19)@[b7ca70e472...](https://github.com/cheesePizza2/Foundation-19/commit/b7ca70e472782606c7fac09026471575745ccb74)
#### Thursday 2023-12-28 23:14:22 by cheesePizza2

Fixes goals system harddels (#1316)

* shit

* fuck you

* removes spaces

---
## [cheesePizza2/Foundation-19](https://github.com/cheesePizza2/Foundation-19)@[a666b103d3...](https://github.com/cheesePizza2/Foundation-19/commit/a666b103d3adcbcc9d954d05bad4e348f0d6ffaa)
#### Thursday 2023-12-28 23:14:22 by cheesePizza2

Fixes CDZ Medical Checkpoint windoors (#1386)

* changes

* fuck me

* fuck you

---
## [Sala/adventofcode](https://github.com/Sala/adventofcode)@[6d6007c928...](https://github.com/Sala/adventofcode/commit/6d6007c9280dac7eb6e4d0703e25acf4659fa80d)
#### Thursday 2023-12-28 23:20:00 by sala

not gonna lie, when I got the second star I was partially surprised and also proud.

this puzzle was a really hard one and to be honest at the beginning I didn't knew how to approach it. I had some ideas, but none of them could provide the correct answer, only a near to perfect one. after I understood how I should work my way to a solution I've built my own implementation with its optimizations, and it works for both parts perfect.

in other news, tomorrow we're hosting the annual Christmas Dinner. I've juts finished preparing an oreo cheesecake and decide to finish this puzzle. but also had two beers and some sour cherry liquor and prepared some plans for next summer.

---

