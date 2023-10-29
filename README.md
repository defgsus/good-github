## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-10-28](docs/good-messages/2023/2023-10-28.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,982,050 were push events containing 2,755,756 commit messages that amount to 168,058,005 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 50 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[157fafeaa9...](https://github.com/tgstation/tgstation/commit/157fafeaa95d4823c272326a37310a7017b206ef)
#### Saturday 2023-10-28 00:08:29 by lizardqueenlexi

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
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[f3d81edb00...](https://github.com/tgstation/tgstation/commit/f3d81edb00b07160bc046ab0d79457e60aefba0e)
#### Saturday 2023-10-28 00:25:53 by Paxilmaniac

Improves the deployable component (#79199)

## About The Pull Request

The deployable component had a few random things I noticed when I tried
actually using it that kinda sucked so I'm:

Making the examine message more generic, we did NOT need to make it that
complicated.
Letting anything with hands deploy stuff, because mobs other than humans
can hold things.
Giving the option to let something be deployed more than once.
Letting direction setting be optional.
Tweaking the check for if something can be placed somewhere to be a bit
better.
## Why It's Good For The Game

I want to use the deployable component for stuff but I made it awful.
## Changelog
:cl:
code: the deployable component has been tweaked and improved with some
new options to it
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Donglesplonge/tgstation](https://github.com/Donglesplonge/tgstation)@[ff0aea800b...](https://github.com/Donglesplonge/tgstation/commit/ff0aea800b0ce03346d7a655deadf8b53d7f098d)
#### Saturday 2023-10-28 00:46:34 by carlarctg

Bladists can now use silver *or* titanium while creating their blades (#78701)

## About The Pull Request

Blade Heretics can now use silver *or* titanium while creating their
blades.

## Why It's Good For The Game

Silver quite literally *only* exists on surgery tables. Being a blade
heretic with shit miners/roundstart means one of several things.

1. Wait for miners to come back with enough silver (They might never
come back or they might have not gotten any silver)

2. Go to lavaland to dig your own silver (Extremely time-consuming on
the antagonist role that has most downtime, death knell for latejoin
heretics)

All that is not even to mention that for some reason it takes two sheets
rather than one, and surgery tables give one silver when scavenged.

This all combined makes obtaining blades super annoying as the BLADE
path.

Now we can farm titanium off shuttles if the miners are jacking off or
dead, or if we joined 9 minutes to roundend.

## Changelog

:cl:
qol: Bladists can now use silver *or* titanium while creating their
blades
/:cl:

---
## [Oyu07/tgstation](https://github.com/Oyu07/tgstation)@[9ff9e4b9a8...](https://github.com/Oyu07/tgstation/commit/9ff9e4b9a849e4a50bf500aaaeca5e020e7677d6)
#### Saturday 2023-10-28 01:14:53 by necromanceranne

Scatter laser shells now use the scatter laser beam, and makes them significantly easier to make. Projectiles can now have damage falloff. (#78927)

## About The Pull Request

Allows for damage falloff to apply to more than just shotgun pellets.
Now any projectile can have a damage falloff defined.

Scatter Laser shells no longer use the minigun beams to determine their
damage. Instead they use the actually defined scatter laser beams. Those
beams do 7.5 damage per pellet, times by 6 pellets.

Scatter laser beams now have damage falloff, a separately defined
(positive) wounding power from normal beams, and wound falloff.

Scatter laser shells can be printed from security protolathes once you
have weapon tech.

Scatter laser shells _may_ be damaged by EMPs based on severity. The
result is that it fires a practically useless volley of laser fire. They
cause a honk sound when they hit, so you know when you've shot one of
these.

## Why It's Good For The Game

Well, we want shotguns universally to not be defined by their damage
output (especially extreme damage output) but by niche.

What does the scatter laser shell currently occupy as a niche?

The single highest damage output of any projectile weapon in direct
damage. The thing we don't want of shotguns, and it is reigning champion
of all guns.

Okay, that's a bit misleading, because obviously it is competing with
the likes of .50 BMG which does 70 damage outright and dismembers limbs,
potentially doing upwards of 90 damage if it does, and also hard stuns
people. Obviously _that_ is technically a stronger bullet.

But not for raw damage, because the scatter laser does 90 damage out the
gate, barring any potential wounding that might occur which increases
the damage multiplicatively. No gimmicks, no extra procs, nothing. It's
just 15 force lasers (with no damage dropoff) split between 6 beams.

And the reason for this is because this shell has been nerfed once prior
by making it not fire 6 normal laser shots into someone. That was 120
damage at the time, 120 to 90 was...I guess a nerf during the taser era.
Depends on how you viewed it. Buckshot was doing like 80 at the time,
believe me it was a wild period. But anyway, when we did the whole
damage rearrangement over the course of the laser few years, every other
shell got touched except this one for some reason. Even pulse slugs lost
10 damage while this was still sitting on 90 force point blank.

So what is the new niche? Well, it's laser buckshot. That's not a niche
but crew don't get buckshot, so this is their buckshot. It wounds real
good. Real goddamn good. And its is a laser. It fits the aesthetic,
obviously.

Okay, thanks.

## Changelog
:cl:
balance: Scatter laser shells actually utilize the _real_ scatter laser
beam. This comes with damage changes. And wounding power.
feature: EMPs can potentially damage scatter laser shells.
refactor: All projectiles can now have damage falloff defined. Yay.
balance: Scatter laser shells can be printed when weapons technology is
researched.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Oyu07/tgstation](https://github.com/Oyu07/tgstation)@[071f6063e6...](https://github.com/Oyu07/tgstation/commit/071f6063e69d39e1403eca917a395191339f353a)
#### Saturday 2023-10-28 01:14:53 by carlarctg

Adds charges to omens and omen smiting. Reduces omen bad luck if nobody's nearby. (#78899)

## About The Pull Request

refactor: Adds charges to omens and omen smiting rather than only being
permanent or one-use. Mirrors now grant seven bad luckers.

qol: Reduces omen bad luck if nobody's nearby to witness the funny.
(Ghosts are included in the check!)

fix: Fixed an issue where a monkey check in doorcrushing was never
actually able to pass. Also they screech now.

## Why It's Good For The Game

> refactor: Adds charges to omens and omen smiting rather than only
being permanent or one-use. Mirrors now grant seven bad luckers.

Allows for someone to get between 1-infinity omen accidents. Seriously
why wasnt this a thing before

> qol: Reduces omen bad luck if nobody's nearby.

I LOVE this quirk, but trying to do antything at all except 'Suffer
Miserably' is nigh impossible. To alleviate life a little, making it so
that you have a lesser chance of suffering misfortune if nobody's around
will be the perfect compromise. It makes life easier but doesn't
compromise funny moments.

Any client in viewrange will disable the reduction. This includes
ghosts.

## Changelog

:cl:
refactor: Adds charges to omens and omen smiting rather than only being
permanent or one-use. Mirrors now grant seven bad luckers.
qol: Reduces omen bad luck if nobody's nearby to witness the funny.
(Ghosts are included in the check!)
fix: Fixed an issue where a monkey check in doorcrushing was never
actually able to pass. Also they screech now.
/:cl:

---------

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [Oyu07/tgstation](https://github.com/Oyu07/tgstation)@[0d5f9907a2...](https://github.com/Oyu07/tgstation/commit/0d5f9907a24346554f4da78199138f4cdcca8de5)
#### Saturday 2023-10-28 01:14:53 by Jacquerel

Shapechange health transfer tweaks (#79009)

## About The Pull Request

Fixes #78721
This PR does a handful of things behind the scenes to increase the
consistency of shapechange health tracking.

First of all we adjust the order of operations taken when you restore
the original body. The implementation as-was would remove the status
effect midway through and null a bunch of variables we tried to continue
using. This would result in several runtimes and code failing to run,
with the upshot that untransforming upon death would leave the caster
completely alive, with the corpse of its transformed shape at its feet.
Oops.

Additionally while testing this I realised that transferring the damagew
as also kind of fucked.
We wouldn't bother to do it at _all_ if you died, which is a shame, so I
made it simply heal you instead of reviving you so we can always do it.
Then as noted in the linked issue, we were applying all transferred
damage to a single limb, which could exceed the health of the limb and
remove damage. Now we spread it around the body.

Finally, applying damage to a human using the "force" flag would often
actually apply less damage to their _health_ than expected. This is
because arms and legs contribute only 75% of their damage taken to a
mob's overall health.
Now instead of reading `health` we read `total damage` which ignores the
limb damage modifier.

The end result of this is that if you transform into a corgi, take 50%
of your health, and transform back then you will have 50% of your health
as a human.
Previously the result would be that you'd have ~63%, then transforming
into a corgi would leave you with ~63% of a corgi's health, then
transforming back into a human would leave you at about 71%... and so on
and so forth. Now it doesn't do that.

## Changelog

:cl:
fix: Dying when using (most) shapeshift spells will now kill you rather
than having you pop out of the corpse of your previous form.
fix: Damage will now be accurately carried between forms rather than
being slightly reduced upon each transformation.
/:cl:

---
## [astral-sh/ruff](https://github.com/astral-sh/ruff)@[fc94857a20...](https://github.com/astral-sh/ruff/commit/fc94857a202e43a0a0fa47f972a6807346336046)
#### Saturday 2023-10-28 01:43:20 by Zanie Blue

Rewrite ecosystem checks and add `ruff format` reports (#8223)

Closes #7239 

- Refactors `scripts/check_ecosystem.py` into a new Python project at
`python/ruff-ecosystem`
- Includes
[documentation](https://github.com/astral-sh/ruff/blob/zanie/ecosystem-format/python/ruff-ecosystem/README.md)
now
    - Provides a `ruff-ecosystem` CLI
- Fixes bug where `ruff check` report included "fixable" summary line
- Adds truncation to `ruff check` reports
    - Otherwise we often won't see the `ruff format` reports
- The truncation uses some very simple heuristics and could be improved
in the future
- Identifies diagnostic changes that occur just because a violation's
fix available changes
- We still show the diff for the line because it's could matter _where_
this changes, but we could improve this
- Similarly, we could improve detection of diagnostic changes where just
the message changes
- Adds support for JSON ecosystem check output
    - I added this primarily for development purposes
- If there are no changes, only errors while processing projects, we
display a different summary message
- When caching repositories, we now checkout the requested ref
- Adds `ruff format` reports, which format with the baseline then the
use `format --diff` to generate a report
- Runs all CI jobs when the CI workflow is changed

## Known problems

- Since we must format the project to get a baseline, the permalink line
numbers do not exactly correspond to the correct range
- This looks... hard. I tried using `git diff` and some wonky hunk
matching to recover the original line numbers but it doesn't seem worth
it. I think we should probably commit the formatted changes to a fork or
something if we want great results here. Consequently, I've just used
the start line instead of a range for now.
- I don't love the comment structure — it'd be nice, perhaps, to have
separate headings for the linter and formatter.
- However, the `pr-comment` workflow is an absolute pain to change
because it runs _separately_ from this pull request so I if I want to
make edits to it I can only test it via manual workflow dispatch.
- Lines are not printed "as we go" which means they're all held in
memory, presumably this would be a problem for large-scale ecosystem
checks
- We are encountering a hard limit with the maximum comment length
supported by GitHub. We will need to move the bulk of the report
elsewhere.

## Future work

- Update `ruff-ecosystem` to support non-default projects and
`check_ecosystem_all.py` behavior
- Remove existing ecosystem check scripts
- Add preview mode toggle (#8076)
- Add a toggle for truncation
- Add hints for quick reproduction of runs locally
- Consider parsing JSON output of Ruff instead of using regex to parse
the text output
- Links to project repositories should use the commit hash we checked
against
- When caching repositories, we should pull the latest changes for the
ref
- Sort check diffs by path and rule code only (changes in messages
should not change order)
- Update check diffs to distinguish between new violations and changes
in messages
- Add "fix" diffs
- Remove existing formatter similarity reports
- On release pull request, compare to the previous tag instead

---------

Co-authored-by: konsti <konstin@mailbox.org>

---
## [Drulikar/cmss13](https://github.com/Drulikar/cmss13)@[e4c3900e4f...](https://github.com/Drulikar/cmss13/commit/e4c3900e4f087444308138e9d05b4da9c774f6a9)
#### Saturday 2023-10-28 01:48:36 by riot

reduces timer on joining ert after death to 30 seconds (#4652)

# About the pull request

reduces timer

# Explain why it's good for the game

Having to wait a full minute to join an ERT is annoying, it was better
b4 when timer from ERT was a minute as well, but 30 second ERT means if
u die just b4 ERT goes you cant join regardless.

if ppl are ghosting bc they want ert then they are stupid.


# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:
balance: Timer on attempting to join ERT after death is now 30 seconds
down from 1 minute
/:cl:

---
## [Drulikar/cmss13](https://github.com/Drulikar/cmss13)@[de5c69661f...](https://github.com/Drulikar/cmss13/commit/de5c69661f8d33425123894028702f64239f861b)
#### Saturday 2023-10-28 01:48:36 by kiVts

DFB property changes. (#4590)

# About the pull request
part 2 out of 4 
This does a **big** touch up on defibrillation property in research

Well, to start off, max_level = 1 was removed. It appears warcrimes
forgot to remove it since process proc has benefits explicitly for
higher levels. I would call it a bug(oversight rather).

Second: Ghosts get notified when the chem starts to try and defib you,
so you dont just wonder how did you stand up, and pretty neat too.

Third: The >6 level of defib to apply healing like with actual item
defib is too high, so we move requirement down to >1 but make it heal
much, much worse at levels lower than 5.
eg it took 20 units to heal ~20 brute at level 3(you will literally
perma lmao), at level 5, however, this will go at around 2.5 per life
tick, level 8 will give 4 damage heal.
This is a balance change(buff) But hardly so since its research,
Research is already neglecting most of the time this property.

Fourth: removes one letter var, This whole file is entombed with them
but Im not doing that for now.

# Explain why it's good for the game


Defib property is way too underused and crudely made. This fixes it,
partially.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl: kiVts
add: Ghosts get notified when they are being revived by DFB property
balance: DFB property healing threshold lowered, You can create DFB
property higher than one.
/:cl:

---------

Co-authored-by: Zonespace <41448081+Zonespace27@users.noreply.github.com>

---
## [maiqingqiang/langchain](https://github.com/maiqingqiang/langchain)@[dff24285ea...](https://github.com/maiqingqiang/langchain/commit/dff24285eaf6d102b1ff913274d18379d8aeeb21)
#### Saturday 2023-10-28 02:05:59 by Nikhil Jha

Comprehend Moderation 0.2 (#11730)

This PR replaces the previous `Intent` check with the new `Prompt
Safety` check. The logic and steps to enable chain moderation via the
Amazon Comprehend service, allowing you to detect and redact PII, Toxic,
and Prompt Safety information in the LLM prompt or answer remains
unchanged.
This implementation updates the code and configuration types with
respect to `Prompt Safety`.


### Usage sample

```python
from langchain_experimental.comprehend_moderation import (BaseModerationConfig, 
                                 ModerationPromptSafetyConfig, 
                                 ModerationPiiConfig, 
                                 ModerationToxicityConfig
)

pii_config = ModerationPiiConfig(
    labels=["SSN"],
    redact=True,
    mask_character="X"
)

toxicity_config = ModerationToxicityConfig(
    threshold=0.5
)

prompt_safety_config = ModerationPromptSafetyConfig(
    threshold=0.5
)

moderation_config = BaseModerationConfig(
    filters=[pii_config, toxicity_config, prompt_safety_config]
)

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

try:
    response = chain.invoke({"question": "A sample SSN number looks like this 123-456-7890. Can you give me some more samples?"})
except Exception as e:
    print(str(e))
else:
    print(response['output'])

```

### Output

```python
> Entering new AmazonComprehendModerationChain chain...
Running AmazonComprehendModerationChain...
Running pii Validation...
Running toxicity Validation...
Running prompt safety Validation...

> Finished chain.


> Entering new AmazonComprehendModerationChain chain...
Running AmazonComprehendModerationChain...
Running pii Validation...
Running toxicity Validation...
Running prompt safety Validation...

> Finished chain.
Final Answer: A credit card number looks like 1289-2321-1123-2387. A fake SSN number looks like XXXXXXXXXXXX John Doe's phone number is (999)253-9876.
```

---------

Co-authored-by: Jha <nikjha@amazon.com>
Co-authored-by: Anjan Biswas <anjanavb@amazon.com>
Co-authored-by: Anjan Biswas <84933469+anjanvb@users.noreply.github.com>

---
## [morrowwolf/cmss13](https://github.com/morrowwolf/cmss13)@[e7caf52c21...](https://github.com/morrowwolf/cmss13/commit/e7caf52c21e01e4580cbf03ff1c61579054dd7a2)
#### Saturday 2023-10-28 02:39:59 by fira

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
## [morrowwolf/cmss13](https://github.com/morrowwolf/cmss13)@[e120ab795b...](https://github.com/morrowwolf/cmss13/commit/e120ab795ba0e92e4eb0f91fda194c59f83cb5aa)
#### Saturday 2023-10-28 02:39:59 by fira

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[ca09fbce1f...](https://github.com/treckstar/yolo-octo-hipster/commit/ca09fbce1f7caf90758533423dec022e3c4cea08)
#### Saturday 2023-10-28 03:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[eb9da97b7d...](https://github.com/tgstation/tgstation/commit/eb9da97b7da54f9bdce32aa29ec972f469625ed2)
#### Saturday 2023-10-28 03:39:15 by GoldenAlpharex

Adds support to the wet_floor component to avoid displaying its overlay, makes ice turfs no longer receive said wet overlay (#79275)

## About The Pull Request
The title says it all, really.

I always thought ice looked a bit silly, and always wondered why. Today,
I found out it was because of the `wet_floor` component adding an
overlay that suddenly made a turf that should look continuous, tiled,
which in turn gave some very ugly visuals. Ice already looks slippery,
you can tell that it's ice, and the overlay that was added to it just
didn't really help telegraph that any better than the sprite itself
already does.

That's why I added support to make it so it would be possible to force
the overlay to just not be applied to the turf that's affected by the
component, to make it all look a bit better overall.

I added it to the ice turfs as a proof of concept, although I guess it
could also be used on other turfs that are always "wet", like the
bananium floors, but I didn't really care enough to touch that yet, and
I guess the bananium floors can use it a bit better than ice did.

I did notice in this PR that the smoothing of ice seemed to potentially
be broken, but that's something to look into at a later time.

## Why It's Good For The Game
Look at this ice and how much smoother it looks like now:

![image](https://github.com/tgstation/tgstation/assets/58045821/6fc85239-e8f1-404b-bc0e-6e1fca7f7753)

## Changelog

:cl: GoldenAlpharex
code: Added support to the wet_floor component to make it so the wet
overlay could not be applied to certain turfs if desired.
fix: Ice turfs no longer look tiled, and instead look smooth when placed
next to one-another.
/:cl:

---
## [ZephyrTFA/tgstation](https://github.com/ZephyrTFA/tgstation)@[26e3ea1e0d...](https://github.com/ZephyrTFA/tgstation/commit/26e3ea1e0d185439d792a6890e9eb041f8aadfdf)
#### Saturday 2023-10-28 04:57:31 by John Willard

Mafia can be played on your PDA (#78576)

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

---
## [ZephyrTFA/tgstation](https://github.com/ZephyrTFA/tgstation)@[2f9c21986b...](https://github.com/ZephyrTFA/tgstation/commit/2f9c21986b9ebcf1548df34ce12b458935b30052)
#### Saturday 2023-10-28 04:57:31 by LemonInTheDark

Actually supports alpha passed into emissive stuff (#79117)

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

---
## [listerla/Aurora.3](https://github.com/listerla/Aurora.3)@[652a3d02d4...](https://github.com/listerla/Aurora.3/commit/652a3d02d4260aea7f34c64814f409a677b063a0)
#### Saturday 2023-10-28 05:32:41 by Wowzewow (Wezzy)

Adds Storage Container Animations (#17329)

* Much ado about the Bagginses

* god i hate manually mapped shit

* Update code/game/objects/items/weapons/storage/storage.dm

Co-authored-by: Fluffy <65877598+FluffyGhoster@users.noreply.github.com>

* fixes

* yes

* Update code/game/objects/items/weapons/storage/bags.dm

Co-authored-by: Cody Brittain <cbrittain10@yahoo.com>

---------

Co-authored-by: Fluffy <65877598+FluffyGhoster@users.noreply.github.com>
Co-authored-by: Cody Brittain <cbrittain10@yahoo.com>

---
## [LadyMisticus/jep-hack](https://github.com/LadyMisticus/jep-hack)@[56bf3ef2b0...](https://github.com/LadyMisticus/jep-hack/commit/56bf3ef2b0271590f239a8eb467b72fb62936530)
#### Saturday 2023-10-28 05:35:53 by Llinos Evans

Finish Lake of Rage "town"

Well, sort of. There's still a lot you can do with Pryce's House, it needs more things.

I want to make it so Pryce only appears when the Red Gyarados has been defeated. Maybe he can give a TM or something too.

This commit does the following;
- Fix the weird landmarking because I was a dumb stupid idiot.
- Adds all the relevant signs.
- Adds Pryce's House over where the gym was. Just a cute, quaint little place.

---
## [unit0016/effigy-se](https://github.com/unit0016/effigy-se)@[57569bfcbd...](https://github.com/unit0016/effigy-se/commit/57569bfcbde0af7b25eac58df98abfcb72f956f4)
#### Saturday 2023-10-28 07:02:12 by carlarctg

Adds a Syndicate Monkey Agent beacon uplink item (#79012)

## About The Pull Request

Adds a Syndicate Monkey Agent beacon uplink item. It spawns a dapper
monkey that must follow your orders.

Added a monkey gun case to the uplink, which contains monkey guns!
Though they aren't very powerful.

Added a more modularlike subtype for antagonist spawners to reduce
future hardcoding.

Gave the syndicate turtleneck a monkey sprite, from SS14!

## Why It's Good For The Game

I want to see the clown driving security insane with 2-3 monkeys and an
incredible amount of pranking. Or an assistant killing everyone with his
monkey friends while wearing a monkey suit. Or a geneticist sending out
mutated monkeys to kill people. Or a scientist equipping his monkeys
with bombs or xenobiology equipment and sending them out to wreak havoc.

6 TC is only enough for two monkeys, but you can get a third if you
finish any kind of objective.

> Added a monkey gun case to the uplink, which contains monkey guns!
Though they aren't very powerful.

We can't have the monkey mafia without guns, come on. The guns are weak
and only usable by monkeys. Additionally, they're restricted to
entertainment only.

Credit to SS14 for the monky turtleneck sprite.

## Changelog

:cl:
add: Adds a Syndicate Monkey Agent beacon uplink item. It spawns a
dapper monkey that must follow your orders.
add: Added a monkey gun case to the uplink, which contains monkey guns!
Though they aren't very powerful.
refactor: Added a more modularlike subtype for antagonist spawners to
reduce future hardcoding.
sprite: Gave the syndicate turtleneck a monkey sprite, from SS14!
/:cl:

---------

Co-authored-by: ATH1909 <42606352+ATH1909@users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [argilla-io/argilla](https://github.com/argilla-io/argilla)@[300bfa58f1...](https://github.com/argilla-io/argilla/commit/300bfa58f1a7469019921f921f411f1c25bcd984)
#### Saturday 2023-10-28 07:55:23 by Ayan Joshi

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
## [Hannnine/Tic-Tac-Toe](https://github.com/Hannnine/Tic-Tac-Toe)@[6331ba1934...](https://github.com/Hannnine/Tic-Tac-Toe/commit/6331ba19344745c21105bf4217fa2ba5c5b6b4f1)
#### Saturday 2023-10-28 08:07:06 by 宋晓

Finished!

I know there are some problems still, but I finished the basic form of Tic-Tac-Toe.
So at least, I'm glad to say this is a good news!

In this released ver1.0 I try to use pointer (*)which is not used in MineAngel before. To be honest, that's the most difficult part of C and also of my program.

The same time, the logical part is not as simple as I thought. espacially I made it changable, which means this program can not only played on 3x3 metrix but smaller or larger. That's up to you. And may I will add this selection into in the late version, perhaps?

Anyway, this is exactlly the first game I made by myself, without any reference (OK maybe GPT.....XD), but the structure, the idea, 98% of this program is made by myself. I promise.

Hope I can make my own game asap. It's aleady on the draft! Hope we can meet her before I gruaduate!

Peace and love!

---
## [TonyAkinsWritesCrypto/zechub](https://github.com/TonyAkinsWritesCrypto/zechub)@[0d97121c8c...](https://github.com/TonyAkinsWritesCrypto/zechub/commit/0d97121c8ca6106c2c829f5b8f47679d1801a3f1)
#### Saturday 2023-10-28 08:21:22 by TonyAkinsWritesCrypto

ZecWeekly66

# ZecWeekly (Episode 66)


The Zebra book, Zcash enhanced privacy, ZecHub Extras, Zcash 7th Anniversary , Ywallet Upgrade. 


Curated by "TonyAkins"[TonyAkin01](https://twitter.com/TonyAkins01))

---

#### Welcome to ZecWeekly Episode 66


Welcome to the thrilling episode of ZecWeekly, as we explore Zcash's implementation of FROST using Schnorr , Zcash 7th Anniversary celebrated with lots of merches and prizes, release of Zebra updated 1.3.0, and the introduction of UniFFi for Developer's use cases. 

–
### This Week Education's Pieces.

This week's education pieces will educate and refine us with all details about Zcash addresses, both shielded and transparent addresses and other the latest development in the Zcash payment system. 

Click  the link below to access the resource :

https://wiki.zechub.xyz/visualizing-zcash-addresses




### Zcash Updates

Zcash and ECC updates. 

[NowNodes features Zcash for upgraded Privacy ecosystem](https://twitter.com/NOWNodes/status/1716463761777680713)

[Ywallet Zcash Ledger app on Nano S Plus w/ Orchard tx](https://www.youtube.com/watch?v=HRVNpDDoh1Y&t=34s) 

[Zcash Digitals Decentralized](https://twitter.com/ElectricCoinCo/status/1717570088771952811)

[tECC DAYS 2023 celebrated](https://twitter.com/ECCIntegrator/status/1718035043736547504)


[Announcing Zebra 1.3.0](https://twitter.com/ZcashFoundation/status/1716524342853476576)

[Implementation of UniFFi on Zcash Network](https://twitter.com/eiger_co/status/1716801431510851824)

[Zcash SDK fixes now live](https://twitter.com/EdgeWallet/status/1716530980499128578)

#### Zcash Community Grants Updates

[WalletD Community Grant Application](https://forum.zcashcommunity.com/t/walletd-community-grant-application/45876?utm_source=dlvr.it&utm_medium=twitter)

[Security assessment for Zcash FROST published](https://twitter.com/ZecHub/status/1716930299140169764)

[Zcash Community funded @eiger_co to create UniFFi library](https://twitter.com/ZcashCommGrants/status/1717273970922123392)

#### Community Projects

[Zcash 7th Anniversary celebrated in grande style](https://free2z.cash/ZecHub/zpage/zcash-7th-anniversary-challenge)

[Post Comments on Free2Z using Zenith CLI! Go check it out!](https://www.youtube.com/watch?v=HtorP8TJ5vk)

#### News & Media

[Binance founder CZ’s fortune gets slashed $12B, while SBF is still at $0](https://cointelegraph.com/news/binance-ceo-changpeng-zhao-fortune-slashed-billionaires-index)

[Google to invest another $2B in AI firm Anthropic: Report](https://cointelegraph.com/news/google-to-invest-another-two-billion-in-ai-firm-anthropic)

[Kraken to suspend trading for USDT, DAI, WBTC, WETH, and WAXL in Canada](https://cointelegraph.com/news/kraken-suspend-trading-usdt-dai-wbtc-weth-and-waxl-stablecoin-canada)

[AI Girlfriend Amouranth Wants to Use Her 'Vaginal Yeast' to Brew Beer](https://decrypt.co/203517)

[Audits and rug-pulled projects, a $650B token burn, and major DeFi protocol quits UK: Finance Redefined](https://cointelegraph.com/news/audits-and-rug-pulled-projects-a-650b-token-burn-and-major-defi-protocol-quits-uk-finance-redefined)

[Bitcoin's 14% Weekly Gain Signals 'End of an Era' as Big Tech Dumps, Analyst Says](https://www.coindesk.com/markets/2023/10/27/bitcoins-14-weekly-gain-signals-end-of-an-era-as-big-tech-dumps-analyst-says/?utm_medium=referral&utm_source=rss&utm_campaign=headlines)

[Binance Founder CZ's Wealth Falls About $12B as Trading Revenue Slumps: Bloomberg](https://www.coindesk.com/business/2023/10/27/binance-founder-czs-wealth-falls-about-12b-as-trading-revenue-slumps-bloomberg/?utm_medium=referral&utm_source=rss&utm_campaign=headlines)

[How major German firms like Mercedes and Lufthansa are using NFTs](https://cointelegraph.com/news/germany-mercedes-lufthansa-nfts)

[ChatGPT creator OpenAI builds new team to check AI risks](https://cointelegraph.com/news/chatgpt-openai-new-team-ai-risks)

[Bitcoin restarting 2023 uptrend after 26% Uptober BTC price gains — research](https://cointelegraph.com/news/bitcoin-2023-uptober-btc-price-research)



## Some Zcash Tweets


[Central bank of Brazil account heard about Zcash today](https://x.com/anarchychains/status/1717288641288921272)

[Happy Birthday Zcash!!!](https://twitter.com/ZforZcash/status/1718085318543376404)

[ZcashFoundation and NCCGroupInfosec conduct a security assessment of the Foundation’s FROST](https://twitter.com/ZcashFoundation/status/1716849796315512935)

[What are Zero-knowledge Proofs](https://twitter.com/NighthawkWallet/status/1717730883933806958)

[Zcash Community Grant minutes](https://twitter.com/ZcashCommGrants/status/1717556482344907090)

[Keep yourself safe from hack with a Zcash wallet](https://twitter.com/NighthawkWallet/status/1717007699592851702)

[Metrics should be updated](https://twitter.com/ZcashForum/status/1716786643171225726)

[Join our UPA friends if you're at EFDevconnect](https://twitter.com/ElectricCoinCo/status/1716886693444530195)


[Social media Data collection, does it matter?](https://twitter.com/ZecHub/status/1716850588942577890)

[Follow NighthawkWallet for crypto privacy education](https://twitter.com/NighthawkWallet/status/1716625185623728248)

[Privacy is normal!](https://twitter.com/ZcashNigeria/status/1716755151497707660)


## Zeme of the Week

[https://twitter.com/ZcashNigeria/status/1718151545324200002](https://twitter.com/ZcashNigeria/status/1718151545324200002)

[https://twitter.com/zcashbrazil/status/1717609507432337754](https://twitter.com/zcashbrazil/status/1717609507432337754)

[https://twitter.com/zcashbrazil/status/1717225798019567621](https://twitter.com/zcashbrazil/status/1717225798019567621)



## Jobs in the Ecosystem

[Zcash needs graphic designers,writers, and privacy advocate in its ecosystem](https://twitter.com/ZecHub/status/1713947885220344234)

[Create Video HOWTO - Setup WSL in windows, and compile lastest zcashd](https://github.com/ZecHub/zechub/issues/567)

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[4840329f97...](https://github.com/treckstar/yolo-octo-hipster/commit/4840329f97d21a0d778a793d8beb2eef79b29288)
#### Saturday 2023-10-28 08:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [BogCreature/Shiptest](https://github.com/BogCreature/Shiptest)@[2a74c23d62...](https://github.com/BogCreature/Shiptest/commit/2a74c23d62916ddb6b1fdfab8c969b7702299067)
#### Saturday 2023-10-28 09:01:18 by Imaginos16

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
## [Aarqw12/kernel_gs](https://github.com/Aarqw12/kernel_gs)@[0eece59c3c...](https://github.com/Aarqw12/kernel_gs/commit/0eece59c3c1a1d69fd9ae0f8c19d563422f80d62)
#### Saturday 2023-10-28 12:19:03 by Sultan Alsawaf

fs: Block various userspace bloatware services from running

Unfortunately, there are several bloatware services that do not cope well
with their kernel interfaces disappearing. Furthermore, there are other
services that are nasty for different reasons and should be disabled.

Namely, twoshay/IInputProcessor cannot cope with touch offload/heatmap
functionality missing in the kernel, and needs to be disabled via VINTF to
use a kernel without touch offload/heatmap.

Additionally, dmd randomly started burning 100% on my device for several
days, generating a whopping 25 GiB of modem logs under /data/vendor/slog
which cannot be deleted without root privileges. Pixel's custom dumpstate
turned out to be the culprit, because it uses persist props to kick off
logging when dumping is requested, but won't get a chance to unset those
persistent props if the device reboots during a dump.

So, these services are absolutely awful and deserve a solid thumping from
the Big Hammer TM.

But there's no way to disable them from the kernel without ungodly VFS
hacks, so that's where we're left: killing poison with poison.

Aarqw12 : updated list for gs101:

twoshay/IInputProcessor is no killed as offload/heatmap
functionality is here

dumpstate is no killed as developpers settings crash without it.

Signed-off-by: Sultan Alsawaf <sultan@kerneltoast.com>

---
## [wrye-bash/wrye-bash](https://github.com/wrye-bash/wrye-bash)@[bcc7d61f9b...](https://github.com/wrye-bash/wrye-bash/commit/bcc7d61f9b37285127972f27a5456ab649f0f717)
#### Saturday 2023-10-28 12:37:45 by MrD

[!]WIP gui resources: RRR EEE

EEE if not os.path.isdir(images_dir): # CI Hack we could move to caller or add a param

This was meant to be more granular - I wanted to centralize image
initialisation including the dirs['image'] - turned out that constants
were imported too early (# 600, control import order), (mopy) dirs were
not initialised and this necessitated moving the image
definitions in initStatusBar - however to make this simpler I renamed
the images based on the key in tooldirs (ini backwards compat). We could:

- turn all these to svgs?
- add a sensible default to the image dict? (we could do this instead of
the CI hack)
- further centralise get_*** from _gui_globals especially get_image_dir

Next commit finalizes this - for now bye staticBitmap, au revoir, auf
wiedersehen etc. Also see the GuiImage imports and dirs['images'] go
down and imgDirJoin (make ugly code look ugly) centralised - getting
somewhere:

"""
Thou hast committed bugs, but that was in another language, and besides,
the critters are dead.
"""

Note cause initially _icons were defined in `import balt` time and
images were not initialized yet the imports would crash cause:

if not os.path.isabs(img_path):
    img_path = os.path.join(get_image_dir(), img_path)

would produce a relative (non-existing) path and we would
land in _tkinter_error_dial - which crashes bigtime on mac:

2023-10-10 14:49:27.496 Python[11010:375752] -[wxNSApplication macOSVersion]: unrecognized selector sent to instance 0x7fcf3c738aa0
2023-10-10 14:49:27.503 Python[11010:375752] *** Terminating app due to uncaught exception 'NSInvalidArgumentException', reason: '-[wxNSApplication macOSVersion]: unrecognized selector sent to instance 0x7fcf3c738aa0'
...
libc++abi: terminating due to uncaught exception of type NSException

Process finished with exit code 134 (interrupted by signal 6: SIGABRT)

To fix balt import crash I moved Colorchecks images init to gui.
This now crashed on importing basher in Mopy.bash.bash._main -
when constants is imported still get_image_dir() returns ''

Traceback (most recent call last):
...
  File "/Users/.../Mopy/bash/basher/constants.py", line 458, in <listcomp>
    return [GuiImage.from_path(template % x) for x in (16, 24, 32)]
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/.../Mopy/bash/gui/images.py", line 90, in from_path
    return _BmpFromPath(img_path, iconSize, img_type, quality)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/.../Mopy/bash/gui/images.py", line 56, in __init__
    raise ArgumentError(f'Missing resource file: {self._img_path}.')
bash.exception.ArgumentError: Missing resource file: tools/isobl16.png.

To fix this I had to finally ->

Simplify tools init:

Here is the map of filenames that differed:

{'ISRMG': "insanity'sreadmegenerator", 'ISRNG': "insanity'srng",
 'ISRNPCG': 'randomnpc', 'OBFEL': 'oblivionfaceexchangerlite',
 'OBMLG': 'modlistgenerator', 'BSACMD': 'bsacommander',
 'Tes4FilesPath': 'tes4files', 'BlenderPath': 'blender', 'GmaxPath': 'gmax',
 'MayaPath': 'maya', 'MaxPath': '3dsmax', 'FastStone': 'faststoneimageviewer',
 'PaintNET': 'paint.net', 'PaintShopPhotoPro': 'paintshopprox3',
 'PhotoshopPath': 'photoshop', 'PixelStudio': 'pixelstudiopro',
 'MAP': 'interactivemapofcyrodiil', 'NPP': 'notepad++',
 'RADVideo': 'radvideotools'}

I hope no one relied on these. Now as seen having to deal with two image
formats introduces complexity - there was a merge about that no ? <--- RRR
There is also the matter of game dependencies - and settings saving - and
profiles per game - that's # RRR launchers

Accept Path in GuiImage.from_path:

os.path.splitext(img_path) works fine for path - yey for os.pathlike!

inline _init_tool_buttons - note that TesVGecko was added twice

things like

renames = {
    'OblivionBookCreatorPath': 'oblivionbookcreator%s.png',
    'Tes4GeckoPath': 'tes4gecko%s.png',
    'Tes5GeckoPath': 'tesvgecko%s.png',
    'Tes4ViewPath': 'tes4view%s.png',
    'Tes4TransPath': 'tes4trans%s.png',
    'Tes4LodGenPath': 'tes4lodgen%s.png',
    'NifskopePath': 'nifskope%s.png',
}
tooldir = '/Users/.../Mopy/bash/images/tools'
for k, v in renames.items():
    for pix in (16,24,32):
        try:
            shutil.move(_j(tooldir, v % pix), _j(tooldir, f'{k.lower()}{pix}.png'))
        except Exception as e:
            print(k,v,e)
            break

One (1) use of app_buttons_factory - yes! This is geared towards # 570
and initTooldirs

The [!] for image renames - this was 99% of the perspiration - dict
used:

{
    'nifskope16.png': 'nifskopepath16.png',
    'nifskope24.png': 'nifskopepath24.png',
    'nifskope32.png': 'nifskopepath32.png',
    'oblivionbookcreator16.png': 'oblivionbookcreatorpath16.png',
    'oblivionbookcreator24.png': 'oblivionbookcreatorpath24.png',
    'oblivionbookcreator32.png': 'oblivionbookcreatorpath32.png',
    'tes4gecko16.png': 'tes4geckopath16.png',
    'tes4gecko24.png': 'tes4geckopath24.png',
    'tes4gecko32.png': 'tes4geckopath32.png',
    'tes4lodgen16.png': 'tes4lodgenpath16.png',
    'tes4lodgen24.png': 'tes4lodgenpath24.png',
    'tes4lodgen32.png': 'tes4lodgenpath32.png',
    'tes4trans16.png': 'tes4transpath16.png',
    'tes4trans24.png': 'tes4transpath24.png',
    'tes4trans32.png': 'tes4transpath32.png',
    'tes4view16.png': 'tes4viewpath16.png',
    'tes4view24.png': 'tes4viewpath24.png',
    'tes4view32.png': 'tes4viewpath32.png',
    'tesvgecko16.png': 'tes5geckopath16.png',
    'tesvgecko24.png': 'tes5geckopath24.png',
    'tesvgecko32.png': 'tes5geckopath32.png',
    'blender16.png': 'blenderpath16.png', 'blender24.png': 'blenderpath24.png',
    'blender32.png': 'blenderpath32.png', 'bsacommander16.png': 'bsacmd16.png',
    'bsacommander24.png': 'bsacmd24.png', 'bsacommander32.png': 'bsacmd32.png',
    'faststoneimageviewer16.png': 'faststone16.png',
    'faststoneimageviewer24.png': 'faststone24.png',
    'faststoneimageviewer32.png': 'faststone32.png',
    'gmax16.png': 'gmaxpath16.png', 'gmax24.png': 'gmaxpath24.png',
    'gmax32.png': 'gmaxpath32.png',
    "insanity'sreadmegenerator16.png": 'isrmg16.png',
    "insanity'sreadmegenerator24.png": 'isrmg24.png',
    "insanity'sreadmegenerator32.png": 'isrmg32.png',
    "insanity'srng16.png": 'isrng16.png', "insanity'srng24.png": 'isrng24.png',
    "insanity'srng32.png": 'isrng32.png', 'randomnpc16.png': 'isrnpcg16.png',
    'randomnpc24.png': 'isrnpcg24.png', 'randomnpc32.png': 'isrnpcg32.png',
    'interactivemapofcyrodiil16.png': 'map16.png',
    'interactivemapofcyrodiil24.png': 'map24.png',
    'interactivemapofcyrodiil32.png': 'map32.png',
    '3dsmax16.png': 'maxpath16.png', '3dsmax24.png': 'maxpath24.png',
    '3dsmax32.png': 'maxpath32.png', 'maya16.png': 'mayapath16.png',
    'maya24.png': 'mayapath24.png', 'maya32.png': 'mayapath32.png',
    'notepad++16.png': 'npp16.png', 'notepad++24.png': 'npp24.png',
    'notepad++32.png': 'npp32.png',
    'oblivionfaceexchangerlite16.png': 'obfel16.png',
    'oblivionfaceexchangerlite24.png': 'obfel24.png',
    'oblivionfaceexchangerlite32.png': 'obfel32.png',
    'modlistgenerator16.png': 'obmlg16.png',
    'modlistgenerator24.png': 'obmlg24.png',
    'modlistgenerator32.png': 'obmlg32.png',
    'paint.net16.png': 'paintnet16.png', 'paint.net24.png': 'paintnet24.png',
    'paint.net32.png': 'paintnet32.png',
    'paintshopprox316.png': 'paintshopphotopro16.png',
    'paintshopprox324.png': 'paintshopphotopro24.png',
    'paintshopprox332.png': 'paintshopphotopro32.png',
    'photoshop16.png': 'photoshoppath16.png',
    'photoshop24.png': 'photoshoppath24.png',
    'photoshop32.png': 'photoshoppath32.png',
    'pixelstudiopro16.png': 'pixelstudio16.png',
    'pixelstudiopro24.png': 'pixelstudio24.png',
    'pixelstudiopro32.png': 'pixelstudio32.png',
    'radvideotools16.png': 'radvideo16.png',
    'radvideotools24.png': 'radvideo24.png',
    'radvideotools32.png': 'radvideo32.png',
    'tes4files16.png': 'tes4filespath16.png',
    'tes4files24.png': 'tes4filespath24.png',
    'tes4files32.png': 'tes4filespath32.png'
}

---
## [phillipwood/git](https://github.com/phillipwood/git)@[8f23432b38...](https://github.com/phillipwood/git/commit/8f23432b38d9b122be8179295a56688391dc8ad6)
#### Saturday 2023-10-28 13:25:29 by Johannes Schindelin

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
## [Aquizit/Yogstation](https://github.com/Aquizit/Yogstation)@[4c25a9bbd0...](https://github.com/Aquizit/Yogstation/commit/4c25a9bbd0c7f7e11ca93d5020287624ebf5cabd)
#### Saturday 2023-10-28 14:00:24 by Manatee

Do NOT make a new accent. Worst mistake of my life, holy fuck. (#20685)

* empty template so i can work from another PC

* holy fuck

* essential

* idk how accents are handled. its poorly documented

* sure

* augh

* amtbe

* Update fugitive_outfits.dm

fuk that

---
## [Das15/cmss13](https://github.com/Das15/cmss13)@[9d69f3aecf...](https://github.com/Das15/cmss13/commit/9d69f3aecf6a0070861688c5648479e8db6b679d)
#### Saturday 2023-10-28 14:07:55 by fira

Fixes bugs with designator usage (#4693)

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

The Laser Designator is a JTACer's workhorse and it's CLUNKY AS HELL. 

This fixes two main bugs:

* The `interactee` is not properly cleared when using the designator (or
any zoomed item), causing it to be unset instead of set the next time
you use it. This means if you look up then back down your designator,
you can't laze.

* The interaction system wasn't made with movement in mind. It is a
problem because zoom system allows movement, and designators are where
the two meet. Now, they can explicitely keep interaction despite
movement.

# Explain why it's good for the game

QoL that should have been done 6 years ago, give or take

Because Zooming interactions are an awful mess, i'm flagging this for
Testmerge where it'll inevitably break down

# Testing Photographs and Procedure
I take designator, i look, i try to laze. I put them down, move, do it
again. And again. Several combinations of actions.

The unzoom logic is blatantly busted and out of scope of the PR.

# Changelog
:cl:
fix: Fixed Rangefinders/Designators preventing you from lazing if you
looked up/down them without moving.
fix: Fixed Rangefinders/Designators forcing you to look up/down again if
you had moved while using them.
/:cl:

---
## [skeyuui/russ-station](https://github.com/skeyuui/russ-station)@[517d33e6f0...](https://github.com/skeyuui/russ-station/commit/517d33e6f06289085d0c6015a01c3a3ce7bc22d0)
#### Saturday 2023-10-28 14:32:09 by Jacquerel

Basic blob mobs (#78520)

## About The Pull Request

I remembered today that blob code is ass, especially blob spores.
There's still a lot to improve but I cleaned up _some_ of it by
converting these mobs.
Now they use a newer framework and more signal handling as compared to
circular references.

I _expect_ the behaviour here to largely be the same as it was or
similar. I haven't added anything fancy or new.

This is a reasonably big PR but at least all of the files are small?
Everything here touched every other thing enough that it didnt make
sense to split up sorry.

Other things I did in code:
- Experimented with replacing the `mob/blob` subtype with a component.
Don't know if this is genius or stupid.
- AI subtree which just walks somewhere. We've used this behaviour a lot
but never given it its own subtree.
- Blob Spores and Zombies are two different mobs now instead of being
one mob which just changes every single one of its properties.
- Made a few living defence procs call super, because the only thing
super does was send a signal and we weren't doing that for no reason.
Also added a couple extra signals for intercepts we did not have.

## Changelog

:cl:
fix: Blob spores will respond to rallies more reliably (it won't runtime
every time they try and pathfind).
fix: Blobbernaut pain animation overlays should align with the direction
the mob is facing instead of always facing South
refactor: Blob spores, zombies, and blobbernauts now all use the basic
mob framework. They should work the same, but please report any issues.
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: san7890 <the@san7890.com>

---
## [TeshariEnjoer/Skyrat-teshari-enjoer](https://github.com/TeshariEnjoer/Skyrat-teshari-enjoer)@[c63f897521...](https://github.com/TeshariEnjoer/Skyrat-teshari-enjoer/commit/c63f897521485898e00425a6c001495f7eef5de6)
#### Saturday 2023-10-28 15:26:30 by SkyratBot

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
## [projectkepler-ru/Skyrat-tg](https://github.com/projectkepler-ru/Skyrat-tg)@[c539a469d5...](https://github.com/projectkepler-ru/Skyrat-tg/commit/c539a469d59849c15a115b319ec5953904863321)
#### Saturday 2023-10-28 15:31:30 by SkyratBot

[MIRROR] Resprites IDs, Random Sprites in the Cards DMI, and Fixes Prisoner Coloring [MDB IGNORE] (#24120)

* Resprites IDs, Random Sprites in the Cards DMI, and Fixes Prisoner Coloring (#78761)

## About The Pull Request
These sprites have been adapted from a person who wished to remain
anonymous with their blessing for tg

Take the old IDs and make them look a little more fancy and sci-fi, I
think they look really nice! This makes the job marker into a cute
little screen too, but this is totally optional, if maintainers want the
animation gone It wont take long at all.
Also resprites a few random other items in the cards.dmi, such as emags,
doorjacks, hack-o-lanturn, budget cards, and one touch up on the red
team ID for laser tag for consistency.
Also prisoner IDs had black symbols and black department but orange trim
on an orange card, so it was just a huge mess.

![all the small
things](https://github.com/tgstation/tgstation/assets/81941674/7bfe75a3-bb75-45bc-9947-373f16d4096b)

## Why It's Good For The Game

I'm gonna be real IDs are kinda crusty, and its something EVERYONE has
to look at at least once a shift. Poor HOPs may even look at two. God
forbid three. Now they will look pretty neat.
As for the other changes, the hack-o-lantern looks like it was made in
2001 its OLD. I don't even know if we use it, but now its updated. The
red laser tag team got a nerf so now all team letters are white, instead
of red being orange for no reason.

## Changelog
:cl:
image: We have received a new shipment of IDs, as the old ones were
found out to be haunted.
image: Laser tag red team ID has received a massive nerf
image: Station budget cards have gotten a facelift
image: Emags and Doorjacks
fix: Numbered prisoner IDs will now be legible
/:cl:

* Resprites IDs, Random Sprites in the Cards DMI, and Fixes Prisoner Coloring

---------

Co-authored-by: EricZilla <81941674+EricZilla@users.noreply.github.com>

---
## [bjackman/git-dissect](https://github.com/bjackman/git-dissect)@[8fdbf52be6...](https://github.com/bjackman/git-dissect/commit/8fdbf52be6cfedc52607c399ee25467d911a5468)
#### Saturday 2023-10-28 15:56:10 by Brendan Jackman

finish the stupid --no-worktrees thing

Honestly if you are going to the trouble of using this tool then your tests
must be really slow. Even for huge repos the cost of setting up the worktrees
is really not gonna be noticeable in comparison.

I dunno though maybe people have Git monorepos that are really extremely big.
I'll leave it in just in case.

---
## [Kingal1337/flipperzero-firmware-wPlugins](https://github.com/Kingal1337/flipperzero-firmware-wPlugins)@[3a2abcf861...](https://github.com/Kingal1337/flipperzero-firmware-wPlugins/commit/3a2abcf86181e643010956eec264319fed33f052)
#### Saturday 2023-10-28 16:02:26 by RogueMaster

Latest Release RM1012-1745-0.93.1-ae9f9be on PATREON - THANK YOU TO ALL SUPPORTERS AND COMMUNITY CONTRIBUTORS!

Well it looks like I won't be in the unleashed discord anymore. MMX/xMasterX/Nano decided to ban me after contributing $1 to the project. In the past, I have given several sizeable BTC donations to the unleashed project and it was received with disrespect. Therefore, I gave a $1 donation to see how it would be treated since it was an option, I guess he didn't like it. Anyone can see what transpired in his general chat unless he wiped it clean out of shame. Most of his discord channels' chats' were other devs trying to poach users or beginners getting shamed for not knowing any better, it was kind of frustrating to watch. Although unleashed is a great project and the work of xMasterX is wonderful, he is a shit person.
I do what I do for this firmware for the enjoyment of the device, I don't have any expectations of support from our users and give everyone the opportunity to have the best firmware available. Pre-compiled for supporters daily, available to be compiled by all at any time and pre-compiled for all users weekly. RM firmware will not change and we will continue to get all new updates and features from the open source community including all the features from the unleashed repository. Contrary to the slander out there, credit will be given for all contributions as they always have been. However, no longer will there be an open advertisement for unleashed on our ReadMe as was requested by xMasterX. It is unfortunate that one of our community devs can be so petty.

---
## [Lynx22330/coyote-bayou](https://github.com/Lynx22330/coyote-bayou)@[eb0f0559aa...](https://github.com/Lynx22330/coyote-bayou/commit/eb0f0559aaea59ecb7d9dcaadafbf1755d89c79a)
#### Saturday 2023-10-28 16:09:06 by Lynx

QuirkFix =Typo fix, Grammar fix, and punctuation=

Changes a lot of different quirk details, added a lot of medical record text, and also added missing "Lose" and "Gain" text for quirks in case an admin wants to give it to someone so that the player can confirm, or an eventual item granting it.

--Changes a lot of grammar, too, for example, like 1071->(1094), its probably not even needed to change it, but it felt a lot easier to read to understand that your max cap went to 25, instead of ONLY 5, to make sure that its clear that it isn't just a bump up to 25 for starter healing, no no, its a permanent 25.

--Some comments, like the radiation one at 1378-79 -> (1404-06), have been made to be a bit more ... vague. Because, well, you just somehow decided out of the god damn blue you're RAD resistant... So you've just decided radiation is basically an afterthought. Does NOT mean you're *IMMUNE* to it. It's a hopeful change that'll make players wonder how resilient they are to radiation, since it depends from person to person. Also. It's their god damn decision apparently if RADS HURT EM OR NOT >:D

--A LOT of the medical record text is to, hopefully, encourage medical personnel to read the medical logs if those even exist on CB. I don't actually know. But, this would also encourage characters and the players to toy around with their medical text if they don't like how cluttered it is from how the medical staff wrote it. It's not intended to be bad; but, every Quirk is ... well, a quirk. This is supposed to be a pretty high end roleplay server (not crazy high since pve duh) but it's intended to have people actually do a lot of smaller things as far as I can tell in-between combat.
(But I may be wrong. Please tell me if I am on discord. Username =   " l_ynx "

I don't think I touched quirk values, as I reverted my change from the empath one back down to 0. I still think its more of a useful quirk; but thats just me.

--A lot of punctuation has been fixed. Some quirks didn't have periods, some did have periods, but too many, and some had a marker at the end, WITH punctuation!.  ;)

---
## [r4d6/sojourn-station](https://github.com/r4d6/sojourn-station)@[f5da3823ac...](https://github.com/r4d6/sojourn-station/commit/f5da3823ac07f22c72a19e8191a4567882020f7f)
#### Saturday 2023-10-28 16:13:27 by nikothedude

holy SHIT i hate saycode (hotfix) (#3816)

* whydidthishappen

* fuck

---
## [r4d6/sojourn-station](https://github.com/r4d6/sojourn-station)@[c3c08d0946...](https://github.com/r4d6/sojourn-station/commit/c3c08d0946fd0ebde1dd9b5cc5ab8781a544487c)
#### Saturday 2023-10-28 16:13:27 by nikothedude

Ports moveSS from TG (#3771)

* p

* fucker

* fuckin

* fuckin!!!!

* commit time

* hell yeah

* FUCKING. TG

* groan

* fuvkin

---
## [Coxswain-Navigator/lobotomy-corp13](https://github.com/Coxswain-Navigator/lobotomy-corp13)@[aee1670aeb...](https://github.com/Coxswain-Navigator/lobotomy-corp13/commit/aee1670aebd0627e2d056ec2268b457462c9e515)
#### Saturday 2023-10-28 16:42:04 by Coxswain

Adds distorted form

adds some basic features

new 1% sprite dropped

text update

Finished work mechanics

adds basic breaching

should fix linters a bit

It works!!!! Kinda...

adds crumbling armor and hammer of light (beta)

adds cool and important stuff

does a thing

adds apostle and tutorial abnorms

adds the stuff

might fix linters

adds a console proc

adds crumbling armor's proper attack and red queen

does some things

should fix linters

adds a blubbering toad transformation

adds more attacks

brings the tier up

adds big boy attacks

updates some sfx, fixes bugs

adds jump attacks

why does linters care about indentation on comments?

adds suggested changes

should fix some stuff

adds info

adjusts damage numbers

updates an effects and fixes transformations

updates blacklist

lowers stack damage

lowers max qlip to 3

adds bloodbath

adds a new AOE attack

adds halberd apostle

blacklists DF from pink midnight

fixes weirdness

requested changes and sound design improvement

removes armortype

removes armortype for real

---
## [nikothedude/Skyrat-tg](https://github.com/nikothedude/Skyrat-tg)@[c034314f1b...](https://github.com/nikothedude/Skyrat-tg/commit/c034314f1b41c2f9ad1e66d939b95f49a0d2f36e)
#### Saturday 2023-10-28 16:43:23 by SkyratBot

[MIRROR] Basic skeletons [MDB IGNORE] (#24545)

* Basic skeletons (#79206)

## About The Pull Request

Turns skeletons (the simple animal version) into basic mobs. This was
another incredibly simple conversion, since skeletons don't really do
anything but walk at you and beat you to death.

Because I thought it was funny, though, skeletons will now seek out
cartons of milk and drink them. Real milk will heal them for a
significant amount, but soymilk, being false milk, will deal them
grievous injury instead! Skeletons beware... I didn't add any other
sorts of milk due to limited ability with existing AI behaviors to
identify milk containers (they actually only look for the carton items).

Other than that, I've done some flavor adjustment for skeletons' attacks
- their effects and sounds will now suit the weapon they're actually
holding - for example, skeleton templars now actually use their swords
instead of slashing you with their horrible fingers. Along with this I
gave the basic skeletons a normal slashing sound, instead of the weird,
impactless hallucination sound they used to use for some reason. I never
liked that sound.

Finally, I've reflavored the spear-wielding skeleton mobs to "undead
settlers", following the naming of the corpses dropped by snow legions
as of #76898, rather than being named after an offensive term for Inuit
people. These skeletons do, after all, appear in settlements on alien
worlds.

To enable the flavor of milk drinking, I expanded the `basic_eating`
component to allow drinking rather than eating flavor, with a different
sound and its own set of verbs. This deletes whatever they drink from,
but c'est la vie.
## Why It's Good For The Game

Ticks 6 more entries off the simple animal freeze. While skeletons are
still extremely simple, being largely-identical mobs that only exist to
beat you to death, being basic mobs should make them slightly better at
this job. Also, again, I think it's really funny that you can distract
skeleton mobs with milk, or even hurt them.
## Changelog
:cl:
refactor: Hostile skeleton NPCs now use the basic mob framework. They're
a little smarter, and they also have a slightly improved set of attack
effects and sounds. They love to drink milk, but will be harmed greatly
if any heartless spaceman tricks them into drinking soymilk instead.
Please report any bugs.
/:cl:

* Basic skeletons

* updatepaths

---------

Co-authored-by: lizardqueenlexi <105025397+lizardqueenlexi@users.noreply.github.com>
Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>

---
## [Time-Green/tgstation](https://github.com/Time-Green/tgstation)@[06eda01ea0...](https://github.com/Time-Green/tgstation/commit/06eda01ea08414b0574ddd84222b4de0bacf2db2)
#### Saturday 2023-10-28 16:44:54 by carlarctg

Added the Hippocrates bust to medbay heirlooms (#78121)

## About The Pull Request

Remade from #77961 because coders dont like bloat in prs

Added the Hippocrates bust to medbay heirlooms. Paramedics don't get
one.

You can now swear the Hippocratic oath with these busts! It'll give you
pacifism but nothing else. The process is reversible.

There's a very small chance that the Hippocrates bust was once wielded
by a certain German doctor. This chance is increased for coroner
heirlooms.

## Why It's Good For The Game

> Added the Hippocrates bust to medbay heirlooms. Paramedics don't get
one.

I got this idea and I just couldn't get it out of my head, it's too
funny. Paramedics don't get one because they're powergamers and laugh at
the Oath, and also it doesn't feel like a paramedic thing.

> You can now swear the Hippocratic oath with these busts! It'll give
you pacifism but nothing else. The process is reversible.

This is just a little fun thing you can choose to do, i think it'd be
cute to see doctors swearing the oath in medbay. Plus it's reversible
which can be even funnier depending on the occassion.

> There's a very small chance that the Hippocrates bust was once wielded
by a certain German doctor. This chance is increased for coroner
heirlooms.

We DO already have precedent for references with the entrenching tool
after all. The buff isn't all that special in reality, getting a medical
hud while in your hand is... basically irrelevant for the roles that
literally spawn with a med hud? It's just for accuracy and rule of
cool's sake.

## Changelog

:cl:
add: Added the Hippocrates bust to medbay heirlooms. Paramedics don't
get one.
add: You can now swear the Hippocratic oath with these busts! It'll give
you pacifism but nothing else. The process is reversible.
add: There's a very small chance that the Hippocrates bust was once
wielded by a certain German doctor. This chance is increased for coroner
heirlooms.
/:cl:

---------

Co-authored-by: Arturlang <24881678+Arturlang@users.noreply.github.com>

---
## [UBCFormulaElectric/Consolidated-Firmware](https://github.com/UBCFormulaElectric/Consolidated-Firmware)@[48ee00ec77...](https://github.com/UBCFormulaElectric/Consolidated-Firmware/commit/48ee00ec772e45a997365bdf7dadaecc117a31e9)
#### Saturday 2023-10-28 18:01:56 by Gus Tahara-Edmonds

Make CAN signal names unique (#1019)

### Summary
<!-- Quick summary of changes, optional -->

Currently CAN signal names are not unique. This is not a problem when
using PCAN or writing code, since signals are categorized by their CAN
message. However, this is not the case when uploading data to Influx,
since then only signal names are uploaded. This means that there are
weird conflicts between signals of the same name. For example, `State`
for the BMS and the DCM.

This PR changes so signal names are prefixed by their board, and then we
enforce all signals are unique across all boards. To avoid ridiculously
long CAN setters/getters in the firmware, only the signal name is now
used.

For example:
| | Before | After |

|-----------|--------------------------------------------|---------------------------------|
| Message | `BMS_Contactors` | `BMS_Contactors` |
| Signal | `AirPositive` | `BMS_AirPositive` |
| TX Setter | `App_CanTx_BMS_Contactors_AirPositive_Set` |
`App_CanTx_BMS_AirPositive_Set` |

The board name prefixes are also now added automatically to
messages/signals, so they've been removed from the `*_tx.json` files.

### Changelist 
<!-- Give a list of the changes covered in this PR. This will help both
you and the reviewer keep this PR within scope. -->

- Change `jsoncan` Python to support these changes
- Rename all signals
- Removed a few unused signals

Note: This diff is huge because of the autogenerated example code in
`jsoncan`. I should really remove this and add proper unit tests
instead.

### Testing Done
<!-- Outline the testing that was done to demonstrate the changes are
solid. This could be unit tests, integration tests, testing on the car,
etc. Include relevant code snippets, screenshots, etc as needed. -->

- [x] Validated on car

### Resolved Issues
<!-- Link any issues that this PR resolved like so: `Resolves #1, #2,
and #5` (Note: Using this format, Github will automatically close the
issue(s) when this PR is merged in). -->

### Checklist
*Please change `[ ]` to `[x]` when you are ready.*
- [x] I have read and followed the code conventions detailed in
[README.md](../README.md) (*This will save time for both you and the
reviewer!*).
- [x] If this pull request is longer then **500** lines, I have provided
*explicit* justification in the summary above explaining why I *cannot*
break this up into multiple pull requests (*Small PR's are faster and
less painful for everyone involved!*).

---
## [Danielkaas94/DTAP](https://github.com/Danielkaas94/DTAP)@[ed57fd01f8...](https://github.com/Danielkaas94/DTAP/commit/ed57fd01f8800c5ffdff54117507f00d5aa0c182)
#### Saturday 2023-10-28 18:10:09 by Daniel Kaas Bundgaard Jørgensen

🕯️🕯️🕯️ Each Small Candle 🕯️🕯️🕯️

Not the torturer will scare me
Nor the body's final fall
Nor the barrels of death's rifles
Nor the shadows on the wall
Nor the night when to the ground
The last dim star of pain, is hurled
But the blind indifference
Of a merciless, unfeeling world

Lying in the burnt out shell
Of some Albanian farm
An old Babushka
Holds a crying baby in her arms
A soldier from the other side
A man of heart and pride
Breaks ranks, lays down his rifle
To kneel by her side

He gives her water
Binds her wounds
And calms the crying child
A touch gives absolution then
Across the great divide
He picks his way back through the broken
China of her life
And there at the curb
The samaritan Serb turns and waves ... goodbye

And each small candle
Lights a corner of the dark
Each small candle
Lights a corner of the dark
Each small candle lights a corner of the dark
When the wheel of pain stops turning
And the branding iron stops burning
When the children can be children
When the desperados weaken
When the tide rolls into greet them
And the natural law of science
Greets the humble and the mighty
And the billion candles burning
Lights the dark side of every human mind

Each small candle
Each small candle
Each small candles lights the dark side of every human mind

And each small candle
Lights a corner of the dark

---
## [Nicalpesh31/Portfolio](https://github.com/Nicalpesh31/Portfolio)@[2cdd183080...](https://github.com/Nicalpesh31/Portfolio/commit/2cdd18308035775e4a4560be7ae126c40beb6253)
#### Saturday 2023-10-28 18:48:40 by Alpesh Sudhirrao Nichat

My Portfolio

Welcome to My Portfolio!

Hello! I'm Alpesh Nichat, a passionate Full Stack Web Developer with a love for clean and efficient code. My journey in the world of technology has been an exciting one, filled with diverse projects and continuous learning.

What I Do:
I specialize in crafting dynamic and responsive web applications. From front-end development, where I bring designs to life with HTML, CSS, and JavaScript, to back-end work using languages like Java and frameworks like Node.js, I ensure seamless user experiences.

My Experience:
With hands-on experience in various projects, including a college management information system and the innovative "Mess Finder" app, I've honed my skills in both team collaborations and solo endeavors. I thrive in environments where creativity meets functionality.

What Sets Me Apart:
I don't just write code; I craft digital experiences. My attention to detail and commitment to user-centered design enable me to create interfaces that are not just visually appealing but also highly intuitive.

Why Work With Me:

Passion: I am deeply passionate about what I do, and it reflects in my work.
Dedication: I'm committed to delivering high-quality results on time, every time.
Innovation: I embrace new technologies and methodologies to ensure my projects are at the forefront of web development trends.
Let's Collaborate:
I'm always open to exciting projects and collaborations. Whether you're a fellow developer, a business owner looking to enhance your online presence, or anyone in between, let's connect! Feel free to explore my portfolio and get in touch. I look forward to creating something amazing together.

Happy coding!

Alpesh Nichat

---
## [GeoB99/reactos](https://github.com/GeoB99/reactos)@[078ff79314...](https://github.com/GeoB99/reactos/commit/078ff793144764ee15294eaa809adcfd1ca400ec)
#### Saturday 2023-10-28 19:07:20 by George Bișoc

[SDK][CMLIB] Implement log transaction writes & Resuscitation

=== DOCUMENTATION REMARKS ===

This implements (also enables some parts of code been decayed for years) the transacted writing of the registry. Transacted writing (or writing into registry in a transactional way) is an operation that ensures the successfulness can be achieved by monitoring two main points.
In CMLIB, such points are what we internally call them the primary and secondary sequences. A sequence is a numeric field that is incremented each time a writing operation (namely done with the FileWrite function and such) has successfully completed.

The primary sequence is incremented to suggest that the initial work of syncing the registry is in progress. During this phase, the base block header is written into the primary hive file and registry data is being written to said file in form of blocks. Afterwards the seconady sequence
is increment to report completion of the transactional writing of the registry. This operation occurs in HvpWriteHive function (invoked by HvSyncHive for syncing). If the transactional writing fails or if the lazy flushing of the registry fails, LOG files come into play.

Like HvpWriteHive, LOGs are updated by the HvpWriteLog which writes dirty data (base block header included) to the LOG themselves. These files serve for recovery and emergency purposes in case the primary machine hive has been damaged due to previous forced interruption of writing stuff into
the registry hive. With specific recovery algorithms, the data that's been gathered from a LOG will be applied to the primary hive, salvaging it. But if a LOG file is corrupt as well, then the system will perform resuscitation techniques by reconstructing the base block header to reasonable values,
reset the registry signature and whatnot.

This work is an inspiration from PR #3932 by mrmks04 (aka Max Korostil). I have continued his work by doing some more tweaks and whatnot. In addition to that, the whole transaction writing code is documented.

=== IMPORTANT NOTES ===

HvpWriteLog -- Currently this function lacks the ability to grow the log file size since we pretty much lack the necessary code that deals with hive shrinking and log shrinking/growing as well. This part is not super critical for us so this shall be left as a TODO for future.

HvLoadHive -- Currently there's a hack that prevents us from refactoring this function in a proper way. That is, we should not be reading the whole and prepare the hive storage using HvpInitializeMemoryHive which is strictly used for HINIT_MEMORY but rather we must read the hive file block by block
and deconstruct the read buffer from the file so that we can get the bins that we read from the file. With the hive bins we got the hive storage will be prepared based on such bins. If one of the bins is corrupt, self healing is applied in such scenario.

For this matter, if in any case the hive we'll be reading is corrupt we could potentially read corrupt data and lead the system into failure. So we have to perform header and data recovery as well before reading the whole hive.

---
## [HarieshAnbalagan/carbon-lang](https://github.com/HarieshAnbalagan/carbon-lang)@[c7e6238fa8...](https://github.com/HarieshAnbalagan/carbon-lang/commit/c7e6238fa8dd57672b0765e738f4c425a27cac3b)
#### Saturday 2023-10-28 19:24:56 by Chandler Carruth

Introduce two speed-of-light benchmarks. (#3270)

The goal of these kinds of benchmarks is to help calibrate other
benchmarks and expectations. They benchmark the underlying hardware
capabilities that we can't avoid, and help illustrate bounds for what is
possible. The term "speed-of-light benchmark" references the aspect of
measuring how fast thing could possible run.

The first is a simple memory bandwidth measurement in the best case
scenario -- using `strcpy` over the buffer. This still does a minimal
number of writes to memory and examines each byte of input to see if it
is null, but can cheat in every way possible to run at the maximum speed
of hardware. To a certain extent, we never expect to get close to this
speed, but it's a good illustration of how much headroom the hardware
has available.

The second is potentially more interesting. This illustrates how fast a
byte-by-byte dispatch loop can potentially be. It uses the technique
that I'm hoping to use in the lexer itself of guaranteed tail recursion
to achieve this with a very small code footprint. The performance of
this technique, even when running in this extremely minimal setting to
establish bounds, is hugely dependent on the number of distinct dispatch
targets, and so the benchmark includes a healthy range to show the range
of performance that we might expect when running in a byte-by-byte mode.
Note that we should expect the lexer to be *faster* than this
"speed-of-light" whenever it is able to lex in larger granules than
byte-wise. But for complex, dense token sequences that force looking at
every byte, this shows the "worst case" "speed-of-light" in a sense.

On my recent AMD cloud VM instance, I get the following results running
the main lexer benchmark with these changes included:

```
-------------------------------------------------------------------------------------------------------------------------
Benchmark                                            Time             CPU   Iterations bytes_per_second tokens_per_second
-------------------------------------------------------------------------------------------------------------------------
BM_ValidKeywords                               3169403 ns      3169283 ns          221        188.44M/s        31.5529M/s
BM_ValidIdentifiers<1, 64, false>             12486725 ns     12486445 ns           51       117.953M/s        8.00868M/s
BM_ValidIdentifiers<1, 1, true>                3950455 ns      3950298 ns          178       72.4252M/s        25.3145M/s
BM_ValidIdentifiers<3, 5, true>               15562294 ns     15561178 ns           45       36.7712M/s        6.42625M/s
BM_ValidIdentifiers<3, 16, true>              16118656 ns     16118374 ns           44       68.0412M/s         6.2041M/s
BM_ValidIdentifiers<12, 64, true>             19116271 ns     19116258 ns           35       199.541M/s        5.23115M/s
BM_ValidMix/10/40                              7074336 ns      7073795 ns           93       140.744M/s        14.1367M/s
BM_ValidMix/25/30                              6790722 ns      6790006 ns          102       131.793M/s        14.7275M/s
BM_ValidMix/50/20                              5960514 ns      5960443 ns          118       112.594M/s        16.7773M/s
BM_ValidMix/75/10                              4325546 ns      4325556 ns          159       102.559M/s        23.1184M/s
BM_SpeedOfLightStrCpy                            24339 ns        24339 ns        29650       35.9049G/s        4.10858G/s
BM_SpeedOfLightDispatch<1>                     1756051 ns      1755800 ns          398       509.668M/s        56.9541M/s
BM_SpeedOfLightDispatch<2>                     1611973 ns      1611725 ns          436       555.228M/s        62.0453M/s
BM_SpeedOfLightDispatch<4>                     2064280 ns      2063990 ns          326       433.565M/s        48.4498M/s
BM_SpeedOfLightDispatch<8>                     2484055 ns      2483946 ns          280       360.263M/s        40.2585M/s
BM_SpeedOfLightDispatch<16>                    4550963 ns      4550894 ns          155       196.637M/s        21.9737M/s
BM_SpeedOfLightDispatch<32>                    6507077 ns      6507090 ns          107       137.523M/s        15.3679M/s
BM_SpeedOfLightDispatch<MaxDispatchTargets>    9071198 ns      9071217 ns           77       98.6499M/s        11.0239M/s
```

Even though we're not lexing anything in the speed-of-light benchmark,
the tokens-per-second measure is still meaningful because we *generated*
the token stream and know how many tokens we put into it. The dispatch
technique easily exceeds hits 10-million tokens/second, but we need to
do substantially better than that to lex at 10-million lines/second.
Fortunately, when the lexer is consuming more than one-byte tokens,
we're already faster than this. And the bytes-per-second numbers from
all but the worst case dispatch scenario are promising.

---
## [StrangeWeirdKitten/Bubberstation](https://github.com/StrangeWeirdKitten/Bubberstation)@[93797f4038...](https://github.com/StrangeWeirdKitten/Bubberstation/commit/93797f403833c016370246b36a921f2647896a78)
#### Saturday 2023-10-28 19:28:52 by nevimer

Restores Low end Space sprites (#442)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

tgstation made (awful) changes recently that made space look like THIS

![dreamseeker_YuYFvv77q1](https://user-images.githubusercontent.com/77420409/208272381-2b91b4f1-04e5-4c8c-bd4c-225b6386f575.png)

Then like THIS (not live yet on skyrat).

![dreamseeker_AgEEkhRDkR](https://user-images.githubusercontent.com/77420409/208272386-1a886d28-ee54-4487-b987-62095d86ddcd.png)

For what? shaving a whole fraction of a second off, hypothetically, of
init time? The job of the server is to pre-bake things as client-side
rendering is pretty much non-existent beyond filters and other
particular things. Not everyone likes the parralax, feels comfortable
with the parallax or even otherwise can run it on their hardware at
cost. We don't need to shave a fraction of a second off init because
it's pretty damn fast anyways, and, once I am done BENCHMARKING on a
CELERON TABLET I will prove it silly. I personally think init time saves
like this are fetishized when it throws the user experience out of the
fucking window, especially for broke/third world gamers who run systems
with like, 2GB of memory. We have players running truly destitute
systems.
## Before

![dreamseeker_vT1uJeDmgx](https://user-images.githubusercontent.com/77420409/208272512-628559ac-8c2a-4f29-9863-a998257c890f.png)
## After

![dreamseeker_lBhaey7ZFd](https://user-images.githubusercontent.com/77420409/208272521-4007b674-7126-4599-b786-fbfc512995bb.png)

I could brand this as saving 4 seconds of init time, to be deceiving.
This is with 64GB of ram on a Ryzen 5800H, Samsung 980 EVO NVME with
lowmememorymode defined.
## How This Contributes To The Skyrat Roleplay Experience

This readds a decent looking space option for those seeking every ounce
of performance in their client in exchange for the server using a
fraction of a second more CPU during init.


## Proof of Testing

<!-- Include any screenshots/videos/debugging steps of the code
functioning successfully, between the </summary> and </details> code
blocks. -->

<details>
<summary>Screenshots/Videos</summary>
  

![dreamseeker_lBhaey7ZFd](https://user-images.githubusercontent.com/77420409/208272553-53fc3f89-e4bc-4cc9-bf20-97356670c861.png)

</details>

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
add: Old space returns for those who choose it. 
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [StrangeWeirdKitten/Bubberstation](https://github.com/StrangeWeirdKitten/Bubberstation)@[bbaea4e46b...](https://github.com/StrangeWeirdKitten/Bubberstation/commit/bbaea4e46b5bc5ec1a34b76803055093b9c56e89)
#### Saturday 2023-10-28 19:28:52 by ShamanSliph

[Modular] Adds the Tactical  Maid Outfit for  Donors.  (#441)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
This time with revengence.

Adds the full Syndicate maid outfit to the loadout but without its stats
bonus and syndicate part replaced with tactical.
Suggested changes are welcome and I will do them as soon as possible. 
This item was requested by skyefree. 

This was in another PR, but I think I broke the actual rebasing and
wasn't sure if I was doing it right. So I closed that PR and made this
one since It was much easier to just make a new branch based on the up
to date master and just quickly put the new files in.

Original PR was  https://github.com/Bubberstation/Bubberstation/pull/307

Sorry about the hassle. I'm not that experienced with using Git.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

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
add: Adds Donor Items: Tactical Maid Outfit/Sleeves/Headband.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [MaTi5893/AoE-remake](https://github.com/MaTi5893/AoE-remake)@[3cbeb6f680...](https://github.com/MaTi5893/AoE-remake/commit/3cbeb6f680a68b48deee5c9c89409446f5427125)
#### Saturday 2023-10-28 19:44:13 by DonoDonger

Novorossiya rework

- Swedish, French, Polish, Ottoman, Austrian, Spanish, and Russian army starts with less red brigades and cohesive stacks
- Zaporizhia pops increased, starting army increased, reworked flavor for Mazepa revolt and Paliy revolt, flavor to accept and core Tatar lands
- Moldavia and Wallachia given more flavor to cooperate with Turks, Russians, or Austrians. Both nations also start with leaders that provide RP and education buffs.
- Flavor for Pruth River campaign, where Moldavia udner Russian influence can rebel against Ottomans. Wallachia has similar flavor for Austrian and Russian influence.
- Romania formable made easier to form, can also be formed from outside by GP.
- Wallachia or Moldavia players also have option to become Transylvania and go for Hungary formable, but is mutually exclusive with forming Romania.
- French revolution events reworked so the revolution affects the proper estates and political reforms
- Russian flavor for colonizing the Caucasus and Novorossiya reworked. The decision chain begins in the 1730s and continues all the way to Catherine.
- Peter III can now resist Catherine's coup at the cost of her buffs and a nerf to army, but keeps the status quo of Russian politics
- If Catherine coups Peter, the politics of Russia are made more despotic and serfdom is continued.
- Catherine reforms flavor now properly introduces the reforms to the church, bureacracy, and political rights that she established
- A few years after the coup, Catherine will be challenged by Pugachev's rebellion. Players have option to put down the revolt or dethrone Catherine and accept Pugachev.
- Accepting Pugachev will reduce serfdom in Russia, introduce cultural and religious rights, revive power of Church, and accept all Tatars, Cossacks, Siberians, Kalmyks, and Kazaks.
-  Russia led by Pugachev loses all Catherine flavor and buffs, and the military takes a debuff to represent the civil war
- If Catherine coups Peter and defeats Pugachev, when all of Crimea has been conquered, Catherine can sign Treaty of Kucuk Kaynarca.
- Kucuk Kaynarca will remove Ottomana nd Crimean cores, replace them with Novorossiya cores, force civilize the land, and provide large assimilation bonus on the cores.
- Kucuk Kaynarca will also destroy the remaining cores and autonomy of the Cossack hosts, if there are any left. Cossack will be removed from accepted.
- Kucuk Kaynarca is necessary for the final decision in Caucasus chain, which gives Armenian and Georgian cores and accepted
- For Russias allied to Zaporizhia, there is an alternate chain where Zaporizhia that cooperates with Russia can eventually become Novorossiya. This will lock them out of the regular chain.
- France will now be locked out of Arpitan, Breton, and Occitan accepted until the French revolution. Instead, they have access to assimilation campaigns that target them and assimlate them.
- Sweden and Denmark can now eat into HRE minors, but lose the ability when they form Scandinavia.
- Sweden now starts with Latvian and Estonian accepted, but loses them if they lose the land in the GNW. They can still regain through later flavor.
- Swedish Carolingian flavor has been reworked to provide more buffs to mob size, allow 6 percent soldiers, and speed up soldier pop encouragement.
- Dethroning Peter will now allow the Swedish to remove Russian cores on Baltics immediately after war, or in 1716.
- Scandinavia formable now requires Divine Right of Kings instead of 1715 tech, and also be formed by puppeting instead of only conquering or sphereing.

---
## [SauerMard/RGF-as-enemy](https://github.com/SauerMard/RGF-as-enemy)@[c31e9cb15e...](https://github.com/SauerMard/RGF-as-enemy/commit/c31e9cb15e4865746e300f6713c14802a36fb162)
#### Saturday 2023-10-28 22:06:24 by SauerMard

GRUNT AND RABBLE RETEXTURE WOOO

There's also arid textures in there fuck you!!!

---
## [SleepingLife/Turbo](https://github.com/SleepingLife/Turbo)@[92035e9b02...](https://github.com/SleepingLife/Turbo/commit/92035e9b021f4606b2212645588df67d2acfead9)
#### Saturday 2023-10-28 23:20:14 by SleepingLife

Air Rework

CHANGELOG
Added Pantheon Creed of Hatred, +3 food and production -3 happiness per city, 50% city bombardment strength
Academy improvement gains 1 food at civil service
Arsenals are on Scientific Theory
Industrialization is now the same cost as Scientific Theory
Greece Spearman gains culture on kill
Promotion changes made to make land stronger vs Naval have been reverted
Panama Canal is cheaper
All Great War Infantry and Expeditionary Force units other than Guerillos now come with Cover
Pontoon Bridges are back
Ottomans now gets 25% faith on kill
Sioux Comp bow no longer has additional ranged strength
Inca no longer has it’s movement bonus in hills
Macedonian Hetairoi now has 8 combat strength instead of 15
Spain is a coastal civ now, does not gain any gold from discovering a wonder
Yugoslavia now has Babylon’s walls
Prussia’s unique factory is cheaper and has 2 fewer maintenance
Tibet is jungle bias
Chile’s factory is cheaper and gives 1 additional happiness
Oman deals 225% increased damage to City States, Baghlah is cheaper and has +2 strength
Vietnam has been deleted
Denmark embark change has been given to all civs
Monuments give -4 to air capacity and new house rule that you cannot put more than 2 air units into a city without a monument
Fighter type air units don’t exist anymore
Airports give +2 capacity instead of +4
Marathi Riders gain +1 range and +5 combat strength
Great War Bomber class units cost 2.5 times more, have +1 range and +15 combat strength
Bomber class units cost 2.5 times more, +2 range and +19 combat strength
Stealth Bombers cost 2.5 times more, +20 range and +22 combat strength
AA_1 and AA_2 Promotion have a 100/120 combat strength bonus versus bombers instead of a 130/150 combat strength bonus
All versions of interception are now a 100% chance to intercept

---

