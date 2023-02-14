## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-02-13](docs/good-messages/2023/2023-02-13.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,346,617 were push events containing 3,555,567 commit messages that amount to 285,350,490 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 42 messages:


## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[b53c9f0531...](https://github.com/cmss13-devs/cmss13/commit/b53c9f0531897023fe365961c16863d8f41983d9)
#### Monday 2023-02-13 00:07:31 by carlarctg

Turns all instances of 'colour' into 'color' (#2609)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

Turns all instances of 'colour' into 'color'.

Changed a shittily-named crayon variable's name.

# Explain why it's good for the game

We use burgerclapper english and we should standardize this

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
spellcheck: Removed all instances of 'colour' and replaced them with
'color'
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[0a745f6b57...](https://github.com/treckstar/yolo-octo-hipster/commit/0a745f6b57a76669c2be10d14faa84b8e1db57b4)
#### Monday 2023-02-13 00:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[5f9f60713b...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/5f9f60713b7f79f548eb9d02baeec793c1e50243)
#### Monday 2023-02-13 01:00:54 by SkyratBot

[MIRROR] Starlight Polish (Space is blue!) [MDB IGNORE] (#19059)

* Starlight Polish (Space is blue!) (#72886)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Adds support to underlays to realize_overlays
Ensures decals properly handle plane offsets
Fixes space lighting double applying if it's changeturf'd into. this
will be important later
Makes solar vis_contents block emissives as expected
Moves transit tube overlays to update_overlays, adds emissive blockers
to them

#### Adds render steps

An expansion on render_target based emissive blockers. 
They allow us to hijack an object's appearance and draw it somewhere
else, or even modify it, THEN draw it somewhere else.
They chain quite nicely

Fixes shuttles deleting z holder objects

#### Makes space emissive, makes walls and floors block emissives
The core idea here goes like this:
We make space glow, and give its overlays some color

This way, the tile and space parallax remain fullbright, along with
anything that doesn't block emissives, but anything that does block
emissives will instead get shaded the color of starlight

This requires a bit of extra work, see later

This is done automatically with render relays, which now support
specifiying layer and color (Need to make an editor for these one of
these days)

The emissive blocking floor stuff requires making a second render plate
to prevent double scaling

Also adds some new layering defines for lighting, and ensures all turf
lights have a layer. We'll get to this soon

#### Makes things in space blue

We color them the same as starlight, by taking advantage of space being
emissive
This means that things in space that block emissive will block it
correctly and be colored blue by the light overlay, but space itself
will remain fullbright

This does require redefining what always_lit means, but nothing but
cordons use that so it's fineee


#### Makes glass above space glow, and some other stuff

Glass tiles that sit above space will now shine light with matching
color to the glasses color. This includes mat tiles.

Glass tiles (not mat because they have no alpha) also only partially
block emissives.
Adds a new proc that uses render steps to acomplish this, essentially
we're cutting out bits below X alpha and drawing what remains as an
emissive.

#### Modifies partial space showing to support glow

Essentially, alongside displaying space as an underlay, we also display
a light overlay colored like starlight.
That starlight overlay gets masked to only be visible in bits that do
not contain any alpha.

We also mask the turf lighting to not go into bits that have no alpha,
to ensure we get the effect we want.
This is done with that lighting layer thing I mentioned earlier.

#### Makes appearance realization's list output ordered

I want it output in order of overlay, sub overlay suboverlay, next
overlay
Need to use insert for that

## Why It's Good For The Game

Pretty!
Also having space be emissive is a very very good way to test for fucked
emissive blockers (If it's broken why are we even drawing the overlay)
I know for a fact mob blockers on lizards and socks are kinda yorked, I
think there's more

<details>
<summary>
Old
</summary>


![image](https://user-images.githubusercontent.com/58055496/213916157-d4b38aa7-3ab6-42a4-989f-7bfba2dc2cba.png)

![image](https://user-images.githubusercontent.com/58055496/213916077-637fa288-bbee-477d-aded-730d9683477e.png)

![image](https://user-images.githubusercontent.com/58055496/213916088-0657a8a2-5627-48e2-8c4b-870c90ef2072.png)

</details>


<details>
<summary>
New
</summary>


![image](https://user-images.githubusercontent.com/58055496/213916107-2af74e64-1817-4a44-b528-180a9160cb9e.png)

![image](https://user-images.githubusercontent.com/58055496/213916115-5fa36fcc-b988-4ccf-850e-21c26ed463d0.png)

![image](https://user-images.githubusercontent.com/58055496/213916120-6833187d-b12e-42a7-ac4b-63c56deb71e5.png)

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
add: Space now makes things in it starlight faintly blue
fix: Glass floors that display space now properly let space shine
through them, rather then hiding it in the dark
add: Glass floors above space now glow faintly depending on their glass
type
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

* update modular

* Update _decal.dm

* Update _decal.dm

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>
Co-authored-by: Tom <8881105+tf-4@users.noreply.github.com>
Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>

---
## [ArtemisStation/artemis-tg](https://github.com/ArtemisStation/artemis-tg)@[728a0f1b91...](https://github.com/ArtemisStation/artemis-tg/commit/728a0f1b9147197bb81f22d946f67e9d08719d5a)
#### Monday 2023-02-13 01:10:21 by Jacquerel

Grand Ritual: Alternate Wizard objective (Wizard Events II) (#72918)

Adds an alternate greentext objective for Wizards known as the "Grand
Ritual". This was initially the gimmick of a different wizard-related
antagonist downstream. I didn't get permission to port it, so I'm
attaching it to regular Wizards instead.

Wizards will spawn in with a new Grand Ritual button next to their
antagonist info button. Pressing it will pinpoint them towards their
next Ritual Location (a randomly chosen region of the space station).
Once within that location, pressing it will summon a magic circle and
obliterate any dense objects which are in the way. This also puts the
ability on a two minute cooldown.
Clicking on the magic circle with an empty hand will begin a three-stage
invocation to gather magical power. You can interrupt this invocation at
any time and will resume from the last stage you completed (if you
finished two stages you only need to do one more).
Once you complete a ritual, a random event will be triggered based on
how many rituals you have performed so far. These tend to be ones which
annoy the crew in some manner, and Wizard Events are included in the
list. Additionally, something weird will usually happen to the room you
are in.
Then you are assigned a new location and can toddle off to do it again.

Once you have done this three times, you will be picked up by the
station's sensors every time you start a subsequent ritual and should
expect annoyed company to come investigate.
Once you have done this six times, you can finally spend all of that
accumulated power on the seventh Grand Finale ritual. Completing this
grants you victory at the end of the round and will have a larger,
flashier effect which you can pick from a list of options, think of it
like a wizard equivalent of a Traitor Final Objective or Heretic
Ascension.
After that you can still keep doing rituals if you want to pester the
crew further by summoning more random events, you've already "won" at
this point so now it's your job to make them want to go home.

I think it'd be more fun to just find out what the Finale ritual can do
by seeing it happen but maintainers will probably want a list of its
precise capabilities, so here it is:

Currently completing a ritual also has a chance to create Heretic
Reality Tears (of both varieties, available for Heretics to eat and
visible to crew) as a kind of cross-antagonist interaction which seemed
to make sense to me but if this seems thematically or mechanically
inappropriate it's easy to strip out.

---
## [Chris-plus-alphanumericgibberish/dNAO](https://github.com/Chris-plus-alphanumericgibberish/dNAO)@[d32aa24764...](https://github.com/Chris-plus-alphanumericgibberish/dNAO/commit/d32aa24764c948cdaa3573651266e73743a78d4a)
#### Monday 2023-02-13 01:14:14 by chris

Dro Healer Crowning Gifts

Esscooahlipboourrr
-Remove arta_drain, handle drain by special-case
--Drain goes off the attk bonus, and Esscoo's is AD_PHYS
--Leave it this way for the standard case so that bane weapons can have drain or what have you.

The Robe of Closed Eyes
-First gift
-Leather Robe
-Grants invis and gaze resistance.

The Red Cords of Ilmater
-Lawful crowning gift
--Not randomly gifted, but CAN be wished for. Lawful monks may want to do this.
-Cloth Hand Wraps (new largely-worthless glove (0 AC 0 DR 1 MC))
-Grant free action and stone res
-Grant 25 Con
-Transfer wounds (healing one party at the expense of another, capped at 1/2 the wound recipient's current HP)
--In melee: transfers wounds from attacker to target on a hit (capped at 1/2 the target's current HP)
--When applied: auto hit, transfers wounds TO a hostile monster, or FROM a peaceful monster TO the PC. Capped at 1/2 the wound recipient's current HP.
---Note: does not need to be worn or wielded to apply.

The Crown of the Percipient
-Neutral crowning gift
-Flesh helm of brilliance (also increases Cha)
-Grants a wide variety of useful resistances when worn (drain, stone, fire, cold, elec, sleep, hallucination, and confusion)
-Grants MR while in open inventory
-Grants spell recall when worn (the PC can cast spells that they've "forgotten")
-Invoke for enlightenment
-Sometimes cancels adjacent monsters (1/11th chance per turn to attempt, monster rolls MR as normal for cancellation)

The Ruinous Descent of Stars
-The #invoke power now allows the player to target the initial impact point, as for firestorm etc.
--Subsequent impacts still occur in random locations.
-Now an insight weapon
--6+ insight: Deals +(insight/6)d6 fire damage to target, capping at 6d6 fire damage at 36 insight.
--4+ Insanity (Nightmare/Clear Thoughts aware): Deals +2d(Insanity/4) Acid damage, capping at 2d12 acid damage at 48 insight. Clear Thoughts reduces this to 1d damage (as well as limiting the die size to at most d2)
--42+ insight: "Falling star" impacts may happen at random whenever Ruinous Descent hits a target.
---Never triggers an earthquake effect, so it won't dig holes
---Cannot be aimed, so this is not a good thing to use around friendly monsters.
---Occurs if insight > rn2(73).
---The number of secondary explosions depends on insight (insight - 36)/6, capping at 6 at 72 insight
---.: This effect maxes out at 72 insight.

misc:
-increase max artifact properties from 8 to 10.
-refactor gaze resistance from eyes of the overworld to be a property.
-refactor explosions to allow muting the distant "sound" of the secondary explosions from Ruinous Descent.

---
## [jeramysoucy/kibana](https://github.com/jeramysoucy/kibana)@[43fa5174f8...](https://github.com/jeramysoucy/kibana/commit/43fa5174f813ce7999dbc65b71cbb9ba0168fb1d)
#### Monday 2023-02-13 02:29:42 by Clint Andrew Hall

[kibana] Thank you for everything, Spencer! 🧔🏻‍♂️ (#150759)

## Summary

> _Inspired by @kertal, and extracted from his PR
https://github.com/elastic/kibana/pull/150660, specifically
@thomasneirynck's
[proposal](https://github.com/elastic/kibana/pull/150660/files#r1101795511)._
>
> _Holding for 24 hours, for our friends in later time zones._

Several of us felt a dev-only easter egg-- where, if you're lucky,
@spalger joins you as you test your latest feature-- would be a fun
tribute as he leaves us for new and exciting opportunities.

Elasticians, feel free to send your love to @spalger in the channel of
your choice, of course, but we'd appreciate your review of this pull
request. ❤️


![image](https://user-images.githubusercontent.com/1178348/217867285-b23dcf1f-1a4a-45fd-b828-f6b24215fef2.png)

---------

Co-authored-by: spalger <spencer@elastic.co>

---
## [npalaska/pbench](https://github.com/npalaska/pbench)@[36cbbd1c8f...](https://github.com/npalaska/pbench/commit/36cbbd1c8f98ddd4c46ccd7405fbca6263245753)
#### Monday 2023-02-13 03:37:59 by David Butenhof

Fix operation synchronization (#3232)

* Fix operation synchronization

PBENCH-993

This is fairly large, but yet much smaller than it started out. This solves
two problems in Pbench Server task scheduling:

1. The default SQLAlchemy transaction model is to start a transaction on any
   SELECT and end it on any UPDATE or INSERT; this means there's no potential
   for atomic update. This impacts the management of all internal context, but
   serious problems have been observed with the "operation" and "state" of the
   datasets.
2. I began the dataset with the concept of a "state", as the dataset
   progresses through upload, backup, unpack, index, and delete. I quickly
   discovered that this wasn't ideal, but had trouble backing off completely
   from the concept. When I added the DB-based "operation" to replace the old
   filesystem links, the relationship between "operation" and "state" became
   even messier.

The primary change here is to divorce the `Sync` class entirely from general
metadata. (I originally set out to make `Metadata` management atomic, and the
fan-out was enormous: I'll tackle that again later, but while important in the
long run, getting `Sync` working is immediately critical.)

There is a new `Operation` DB object associated with a `Dataset`, and this is
entirely managed within the `Sync` class. For visibility, `Dataset.as_json`
will collect associated rows just as it does for `dataset.metalog`, but this
doesn't require any special transactional management. (It's a snapshot.)

I've completely *removed* the `Dataset.state` column (and its associated "last
transition" timestamp). "State" is tracked and observed by the various `Operation`
rows created and managed by `Sync`. This corresponds to the previous
dataset.status` sub-object managed by the old `Sync`: each named operation
(`OperationName` enum) that's been associated to a dataset will have a row with
`state` and `message` columns. The `state` can be advanced through `READY`,
`WORKING`, `OK`, and `FAILED`, and a message can be associated with each
row (on error via `Sync.error` or as part of transition via `Sync.update`).

While I was modifying the Dataset schema, I also removed the `created` column;
it's really redundant with `dataset.metalog.pbench.date`, and we'll need to
understand that for "non-Pbench-standard" tarballs we might not be able to get
this anyway. This wasn't quite as "easy" as I'd thought, because it meant that
I had to refactor date-range operations to work on `uploaded` (perhaps they
should have been that way originally).

`Sync.__init__`: Construct a sync object for a particular named operation.
`Sync.next`: Return a list of datasets which have `Operation` rows for the
   sync component that are in `READY` state.
`Sync.update`: Change the state of the sync component's `Operation`,
   optionally add a message to that `Operation`, and set a list of named
   operations for that dataset to `READY`.
`Sync.error`: Change the state of the sync component's `Operation` to `FAILED`
   and record an explanatory message for the failure.

To avoid rippling massive SQLAlchemy transaction model changes across all our
code, I've added a second session factory in `Database` with the most strict
integrity level, `SERIALIZABLE`. (In fact, I *think* that `"REPEATABLE READ"`
would be enough, and slightly more efficient, but sqlite3 doesn't support that
and I don't think I want to trust the weaker model it does support.)

*Only* the `Sync` class in `sync.py` currently uses that alternate session
factory. To avoid conflicts and confusions with autoflush and autocommit and
other SQLAlchemy "help", I'm creating new sessions on-the-fly for each call
and retiring them after commit/rollback. Note that the idiom
`with Database.maker.begin() as session:` constructs a new session with fresh
state, allows a sequence of session operations, and then implicitly tears down
the session after it commits on success or rolls back on an exception.

To avoid multiple `SELECT` statements within our transaction, `Sync.update`
fetches all relevant rows in a single `SELECT`, and then organizes them for
selective updates. This ensures we have no `SELECT` following the update of any
proxy object, which confuses SQLAlchemy in normal configuration.

`Sync.update` and `Sync.error` will loop up to 10 times on commit failure to
re-try with fresh data. Note that I've observed the retry logic in dozens of
functional test runs; and while I wonder vaguely whether I should be concerned
with the constant 10, I rarely see more than one or two retries since I added
a small delay to minimize thrashing.

NOTE: Alembic schema changes for Operation table

After working with Pete get get alembic to successfully generate a revision
file for my changes, we realized what a pain it would be to migrate (and
test) an actual live database. We need to have a functional test framework to
stand up an "old" functional DB, upgrade it to the latest revision, and then
validate the correctness.

---
## [MemedHams/Shiptest](https://github.com/MemedHams/Shiptest)@[0d19f3c85d...](https://github.com/MemedHams/Shiptest/commit/0d19f3c85d39f58ee663935eb75b72fd502752af)
#### Monday 2023-02-13 04:21:32 by Bjarl

Patches the Bombed Starport To Be Less Bad (#1754)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

![image](https://user-images.githubusercontent.com/94164348/217633782-c0dca540-0915-4acf-99f7-1031ea47f5ec.png)

![dreamseeker_vlOQGOERgI](https://user-images.githubusercontent.com/94164348/217633806-269717de-78fb-4fc2-8ab6-a7ee7a1c3b6e.png)

![dreamseeker_pP6WKD1PQT](https://user-images.githubusercontent.com/94164348/217633810-87471403-d8ad-4e46-bd3f-7a49c5eaad5d.png)
Puts some funny signs I painted over around, fixes the lighting, and
does a small pipe fix
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
I watched like 4 people walk into this ruin completely unaware that it
was horrifically radioactive and that was just kinda not fun.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
fix: Bombed Starport lighting now works properly
imageadd: fokrads sign
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
Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

---
## [Kapu1178/daedalusdock](https://github.com/Kapu1178/daedalusdock)@[c9a7611c75...](https://github.com/Kapu1178/daedalusdock/commit/c9a7611c75ca8d6fbbe413cc52607ab495017cb8)
#### Monday 2023-02-13 04:33:44 by Kapu1178

Fixes asset caching (#69852) (#193)

The asset was being loaded, seeing that fully_generated is false, so it
attempts to rebuild. The rebuilding clears the existing file cache, and
fucks us.

Life is pain.

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [s9ori/integratenyc](https://github.com/s9ori/integratenyc)@[ba9d360280...](https://github.com/s9ori/integratenyc/commit/ba9d360280ec39154c5bfc5f47fbdf0f4cc26c96)
#### Monday 2023-02-13 04:46:16 by s9ori

During the early 60s, the focus of civil rights activists was on changing existing institutions to achieve equal rights. However, the limitations of these reforms, ongoing police brutality, economic exploitation, and international struggles led activists to look for a new method of change that addressed the root causes of these problems. In the late 60s, a new consciousness emerged around revolution. This new revolutionary consciousness was different from the mainstream civil rights struggle in that it looked for solutions and methods that would give people more control over their own lives.

As the conversation about civil rights continued, division arose among activists about the limitations of legislative equality, the failure of reform, and non-violent strategies. This led to a desire for a more radical method of change. The international liberation movements of the colonized world and the Vietnam War also played a role in shaping the new revolutionary consciousness. Activists saw their struggles as connected to those around the world and realized that capitalism was the root cause of many of the problems they faced.

Leaders like Stokely Carmichael and women, queer, and trans people of color played a significant role in advancing this new consciousness. They created radical experiments in areas like schooling, healthcare, housing, and community safety to empower people and give them more control over their lives.

Martin Luther King Jr. also reached the limits of reform-oriented strategies and realized that it would take a revolution to truly transform the United States. He criticized the U.S. for prioritizing profits and imperialism over ending the exploitation of Black Americans and called for reparations, a radical revolution of values, and the funding of social programs.

The legacy of Martin Luther King Jr. is often associated with nonviolence and civil rights legislation, but he later realized the limits of these strategies and offered a more radical alternative for change. Education has always been a pathway to freedom for Black people, but they often had to fight against racist treatment and curricula. During Reconstruction, public education expanded in the South as a result of Black activism, but then white Southerners established Jim Crow laws to deny access to quality education for Black people.

Black teachers worked hard to provide the best education they could for their students, both in the South and North. Despite the success of Black activists in fighting school segregation laws at the state level in the North, most school systems still found ways to maintain separate and unequal education.

It is difficult to understand why working-class white people would support the establishment of anti-Black Jim Crow laws, despite benefiting from Black activism. In the early 20th century, as Black people moved to the North, segregation worsened. Black people from around the African diaspora came together to imagine a future of Black freedom beyond the boundaries of the United States, leading to movements for Black civil and human rights in response to Jim Crow laws, segregation, and the ongoing struggle against European colonization.

Black activists debated different strategies to achieve education for freedom, including questions about who should control the education of Black children, who should teach them, what they should learn, and who their classmates should be. Some, such as followers of Marcus Garvey and members of the Nation of Islam, favored all-Black independent schools, while others worked to address racism in the public school system. The advantages and disadvantages of seeking racial justice in public versus independent schools are complex and open to debate.

In the 1960s, Northern Cities organized school boycotts to protest the persistence of segregated schooling, leading to the creation of Freedom Schools as an alternative for students during the boycotts. The Student Nonviolent Coordinating Committee (SNCC) used these models to create Freedom Schools in Mississippi, which provided Black students with basic reading, writing, and math skills and encouraged them to challenge racist myths, be creative, be empowered by their history, and organize actions in the name of freedom.

The history of Freedom Schools serves as a reminder of the potential for schooling to empower individuals and communities to challenge oppression and promote intellectual curiosity and critical thinking.

The Mendez v. Westminster case in 1946 saw the Mendez family in Orange County, California fighting for equal access to education for their children and other Mexican-American families. The court ruled that segregated "Mexican Schools" were unconstitutional, leading to the desegregation of all California schools and setting the stage for the later Brown v. Board case.

In 1964, the Citywide Committee for Integrated Schools in New York City declared February 3rd "Freedom Day," in response to the persistence of segregation in the schools despite a decade of organizing by Black and Puerto Rican parents and other activists. Over 400,000 students stayed out of class to demand integration and over 100,000 students attended Freedom Schools during the boycott.

The Rainbow Coalition, formed in the 1960s by African Americans, Puerto Ricans, and other poor and working-class people of color, aimed to address poverty, police brutality, and lack of resources in urban communities. They fought for affordable housing, healthcare, fair policing, and equal access to basic services. The Black Panthers started the Free Breakfast for Children program in 1969, which served breakfast to over 10,000 children in church basements nationwide. The FBI considered these programs a threat to national security and worked to shut them down.

The Boston Busing Crisis and MOSAIC saw African American parents and students in Boston fighting for school integration throughout the 1960s. Despite organizing boycotts and Freedom Schools, it wasn't until the ruling on Morgan v. Hennigan in 1974 that the court mandated the busing of students to balance enrollment and address segregation in the schools. Despite resistance from some white parents and communities, the ruling marked a significant step towards desegregation in the Boston Public Schools.

Black teachers worked hard to provide the best education for their students, but despite their efforts, segregation and inequality still existed in schools, especially in the North. This was due to anti-Black Jim Crow laws being established, despite the efforts of Black activists to fight against them. In the early 20th century, segregation worsened in the North as more Black people moved there, leading to movements for Black civil and human rights. The question of who should control Black education and what should be taught was a subject of debate among Black activists, with some favoring independent all-Black schools and others working to address racism in the public school system. In the 1960s, Northern cities organized school boycotts to protest segregation, and Black activists created Freedom Schools as an alternative for students during the boycotts. The SNCC Freedom Schools taught basic reading, writing, and math skills and encouraged students to challenge society's racist myths, be creative, and empower themselves through their history. The history of Freedom Schools shows that it is possible for schooling to empower students and intervene in oppression.

In 1946, the Mendez family in Orange County, California fought for equal access to education, leading to the desegregation of all California schools. In 1954, the Supreme Court ruled that segregated schools were unconstitutional, but New York City's schools were still segregated in 1964. The Citywide Committee for Integrated Schools organized Freedom Day, a boycott attended by over 400,000 students and 100,000 students in Freedom Schools.

In the cities of the 1960s, there was segregation by race and class, leading to a lack of resources in urban communities. The Black Panther Party and the Young Lords were formed to fight poverty and police brutality, and they joined with other groups to form the Rainbow Coalition. The coalition fought for affordable housing, healthcare, and equal access to resources, and started programs to feed children, such as the Free Breakfast for Children program.

The Boston busing crisis was a result of the lack of relationships between White and African American families and structural racism. In response, African American and White students created a literary magazine called MOSAIC to build relationships and express their creativity.

Restorative justice was a subject of concern after events such as Operation Shutdown and the Parkland Shooting, even after a half million students boycotted New York City schools demanding integration.

In the spring of 1968, the Ocean Hill-Brownsville board attempted to transfer predominantly white Jewish teachers and supervisors out of the district, causing conflict with the unions who accused the board of anti-Semitism. This led to three strikes in the fall of 1968 which shut down schools citywide for months. The board hired new teachers, most of whom were also white and Jewish, to replace the strikers. These new teachers were willing to work under the leadership of educators and parents of color, to prove that all children can perform at a high level if treated with dignity and affirmed in their culture. The strikes ended with a negotiation between the Board of Ed and the teachers union, and the community control experiment only lasted for three years.

New York City has some of the most segregated schools in the country, more than six decades after the US Supreme Court ruled on Brown vs Board of Education. Standardized testing creates stressful and competitive learning environments that harm students' growth, and are especially harmful to students of color and marginalized groups. The high school admissions process in New York City is called "open choice," but the choices students have are dictated by factors such as zip code, grades, suspensions, and interviews. This process does not accurately measure a student's potential and perpetuates segregation.

COVID-19 has had a disproportionate impact on communities of color and low-income communities in New York City. Black and Latinx New Yorkers are 1.5 times more likely to be infected and 2 times more likely to die from COVID-19. Essential workers, who are predominantly black and Latinx, have been more affected by the virus. Racism has been ingrained in New York City's planning practices for decades, through redlining and segregation, leading to the concentration of privilege and vulnerability in schools and communities.

Systemic racism in NYC school admissions is perpetuated by exclusionary policies that discriminate against marginalized groups. The push for equitable admissions policies has been further complicated by COVID-19, and the NYC public schools are some of the most segregated in the country. IntegrateNYC, a youth-led organization working to repair the harms of segregation and build integration and equity, has created a short video to better understand how NYC public schools became so segregated.

Redlining has a significant impact on today's school communities, perpetuating segregation and depriving historically marginalized communities of important resources. Modern tools such as screens reinforce these historic inequities. The relationship between redlining and current school demographics and funding is shown in the infographic below. Just as segregation in schools reflects historic injustice and present education policy, racist policing also impacts marginalized communities, particularly Black, Latinx, and Indigenous youth. With 88% of police interventions in schools targeting these children, it is important to rethink disciplinary practices and cease using admissions criteria that have a racist impact, such as behavior scores.

IntegrateNYC's 5Rs of Real Integration framework addresses not only segregating admissions practices, but also resource inequity, curriculum injustice, teacher diversity, and the school-to-prison pipeline. This holistic approach is the only way to transform schools. Disadvantaged students, such as those of color, low-income students, students with disabilities, and emerging multilingual learners, have always faced inequities. The Admissions Impact Score takes into consideration the community and individual impact of injustices exposed by COVID-19 and places students most impacted into a priority group for the admissions process.

In 2016, IntegrateNYC began redesigning the school admissions algorithm with the help of an engineer from MIT, Data 4 Black Lives, and the Bleeker Network. The Student Priority Score reviews a student's individual and community factors to determine their priority group during the admissions process.

Our Admissions Policy Proposal takes into account the uneven burden families have faced recently, as informed by NYC DOE students and integration advocates. The proposal uses variables such as COVID-19 data, percent uninsured, linguistic isolation, children below poverty line, average household size, and children without computer access. These variables are analyzed to create an impact map and corresponding priority score based on the student's home address.

---
## [OxygenCobalt/Auxio](https://github.com/OxygenCobalt/Auxio)@[1826ae3215...](https://github.com/OxygenCobalt/Auxio/commit/1826ae32150455dea85c0def4a9adf3ba74bd8ff)
#### Monday 2023-02-13 04:49:03 by Alexander Capehart

deps: update to mdc 1.8.0-alpha01

FINALLY update to MDC 1.7.0. After over half a year.

I have been continually blocked by doing this due to this absurd ripple
bug that was so continually frustrating. Today, I finally figred out
how to hack a fix in by using R E F L E C T I O N and manually
disabling the bugged code path since google apparently can't be bothered
to fix it.

Now, you might wonder why I didn't update to 1.8.0. That is because
there is ANOTHER RIPPLE BUG. THIS TIME WITH THE TAB LAYOUT. AND ONLY IF
IT'S IN A COLLAPSING TOOLBAR LAYOUT. Can't wait to finally use the new
1.8.0 features in December!

---
## [CluckeyMcCormick/ncg2](https://github.com/CluckeyMcCormick/ncg2)@[a00717e8ea...](https://github.com/CluckeyMcCormick/ncg2/commit/a00717e8eaaa2c47debb5ad0e79a87dd50697f93)
#### Monday 2023-02-13 06:02:16 by frick-nedrickson

Add a new texture-data dependent light shader

After Thanksgiving and Christmas, a vacation, and the Super Bowl, I am
finally back to the neon-city project. And just in time for the
February deadline I set for myself. Or just in time to PANIC about the
deadline I set for myself.

Anyway, so the trouble with the previous shader was that packing all
that information in was far too information rich. Slowed the program
down. ESPECIALLY for all of our decorations. And we can't be without
our decorations - they really tie the whole city together!

The solution I came up with was to basically move the packing -
instead of packing everything into a building, we pack it into a
texture and just look at it. Not exactly innovative but GOOD ENOUGH!
We make use of all 3 channels - RGB - and generate this in GIMP via
the "Hurl" filter (which is why the next texture is "hurl noise").

The new shader has variation for both range and offset. It's
unforunate that we can't get the lights to scale proportionally to the
buildings but frankly nothing is perfect here.

The problem I'm having is making everything look good - it's just a
few too many levers. Or rather, the offset and range variation need to
be set PER COLOR SCHEME. Some schemes need less range, or more offset;
some need more variance and others less. Think I'm gonna have to cook
up a GUI...

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[91f06a97d3...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/91f06a97d3f24c849241bf909b7de28b9b6ec951)
#### Monday 2023-02-13 06:24:34 by candle :)

Small VoxPrimalis Fixes (#18944)

* fuck you i don't need to give you a fucking summary

* fixes

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[d95ca04819...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/d95ca048192f08a8fbaf524fdb4ab0ca498b319e)
#### Monday 2023-02-13 06:24:34 by Rimi Nosha

[MODULAR] Fixes All Known Modular Persistence (NIF) Saving Issues (#19096)

* Fuck

* Holy shit

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[8500d62b79...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/8500d62b798a45812832be0c686f532f877f1e3a)
#### Monday 2023-02-13 06:24:34 by SkyratBot

[MIRROR] Abductor scientist self-retrieve failure/runtime fix [MDB IGNORE] (#19179)

* Abductor scientist self-retrieve failure/runtime fix (#73172)

## About The Pull Request

Since the abductor outfit/implant would load before the abductor ship
(and it's teleport pad) when first generating a team, a runtime would
occur when trying to link the pad to the implant. Another would occur
every time you attempted to retrieve yourself (as the linked pad would
be null), preventing recall and completely neutering an abductor team's
most important maneuver.

Now, using the implant will perform the linking process again if no
linked pad is found, and provides the owner with a warning if (by some
great calamity) they genuinely have no pad to teleport back to. This
solves the issue of the implant sometimes not linking to a pad properly
on initialize, and makes them way less prone to breaking.

Apparently this has been broken for a while, presumably since the
abductor ship was made into a lazyloading template.
## Why It's Good For The Game

The funny silly grey men get to torture the poor hapless crew once
again.
## Changelog
:cl:
fix: abductor scientist's retrieval implants will now properly recall
the owner, and inform them upon recall failure.
/:cl:

* Abductor scientist self-retrieve failure/runtime fix

---------

Co-authored-by: Rhials <Datguy33456@gmail.com>

---
## [XuehaiPan/pytorch](https://github.com/XuehaiPan/pytorch)@[d09cd15216...](https://github.com/XuehaiPan/pytorch/commit/d09cd152161626381cae7780bbd2c44eedeb33d7)
#### Monday 2023-02-13 06:57:08 by Taylor Robie

[Profiler] Defer recording startup python events (take 2) (#91684)

This is my commandeer of https://github.com/pytorch/pytorch/pull/82154 with a couple extra fixes.

The high level idea is that when we start profiling we see python frames which are currently executing, but we don't know what system TID created them. So instead we defer the TID assignment, and then during post processing we peer into the future and use the system TID *of the next* call on that Python TID.

As an aside, it turns out that CPython does some bookkeeping (https://github.com/python/cpython/blob/ee821dcd3961efc47262322848267fe398faa4e4/Include/cpython/pystate.h#L159-L165, thanks @dzhulgakov for the pointer), but you'd have to do some extra work at runtime to know how to map their TID to ours so for now I'm going to stick to what I can glean from post processing alone.

As we start observing more threads it becomes more important to be principled about how we start up and shut down. (Since threads may die while the profiler is running.) #82154 had various troubles with segfaults that wound up being related to accessing Python thread pointers which were no longer alive. I've tweaked the startup and shutdown interaction with the CPython interpreter and it should be safer now.

Differential Revision: [D42336292](https://our.internmc.facebook.com/intern/diff/D42336292/)
Pull Request resolved: https://github.com/pytorch/pytorch/pull/91684
Approved by: https://github.com/chaekit

---
## [morrowwolf/cmss13](https://github.com/morrowwolf/cmss13)@[766f5529bf...](https://github.com/morrowwolf/cmss13/commit/766f5529bfca454129f6d62f1ed626d6a70d5432)
#### Monday 2023-02-13 08:15:29 by carlarctg

Removes Autodocs from the Almayer (#2607)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Removes autodocs from medbay. They're replaced with 2 random potted
plants. :)

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->



EDIT: Tomorrow I will update this PR to give nurses surgery skill.

Autodocs fundamentally and inseparably, irrevocably, DESTROY medbay and
surgery gameplay. There is NO REASON, EVER to put someone through manual
surgery when you could just haha autodoc them instead. Autodocs kill the
good old hell medbay lines, they make surgeons extremely lazy and
stagnant (Tales of surgeons doing surgery for a few minutes, then giving
up and autodoccing the patient are common, not to mention the times
where they miss something in the autodoc schedule), they remove all
skill depth, floor, ceiling, the middle from medbay, and they also make
marines complacent by having them want the funny magic robot machine
rather than an actual human to treat them.

I understand that this may be too sudden of a change. If so, I propose
the following: Cryo tubes could slowly heal a marine up entirely,
removing organ damage and bone breaks through the course of a very slow
5-10 minutes. This will allow marines and nurses to get treated if
there's no doctor around or alive. However, I think the best course of
action is to just ram this change through and make medbay adapt. Embrace
the suck.

# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
balance: Removes Autodocs from the Almayer
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [morrowwolf/cmss13](https://github.com/morrowwolf/cmss13)@[7f5cd54b2b...](https://github.com/morrowwolf/cmss13/commit/7f5cd54b2bab2fdbd25a3f970e9a7f55d415dfe9)
#### Monday 2023-02-13 08:15:29 by carlarctg

Colony Guns Part 3: Longarms Rework (#2334)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Updates and buffs the following weapons:

- Basira-Armstrong Rifle
- Model 12 Bolt-Action Rifle
- M37-17 pump shotgun
- Dragunov sniper rifle

### Basira-Armstrong Rifle

- The BA rifle has been reflavored as the removed 'ceremonial' ABR-40,
now a hunting-civilian version of the L42. It effectively has the same
stats as the L42, just don't take the stock off!
- Its magazines can only fit 12 bullets, but they still have the classic
L42 kick to them. The magazines are completely compatible between both
military and civilian gun types.
- Additionally, there are now holo-targeting magazines available for the
ABR-40, for hunting target capture purposes.
- - The Contractor ERT has a chance to spawn with a tacticool ABR-40
loadout, with three spare holotarget magazines on their webbing.

### Model 12 Bolt-Action Rifle

- Like its sprite implies, this is now the new Basira-Armstrong rifle.
- Its stats have recieved an overhaul and it can now hold its own
against a Xenomorph (or marine if you're CLF)
- Additionally, its bullets will push back (not stun) targets within
three meters, to increase viability for colony usage.

### M37-17 Pump Shotgun

- Did you know that the 10% damage mod this gun was supposed to have
didn't work? Now it does! And it deals 15% more damage to make up for
it.
- However, it can now be melted down.

### Dragunov Sniper Rifle

- The dragunov has been revamped into a DMR, needing no skill to fire,
dealing good damage, and having the same push-back feature the
bolt-action now has.

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

All of these weapons are seen as, and are, a complete joke and ignored
in favor of chungillionaire among us sus impostor running around PBing
xenos with buckshot. Buffing them to be useful paves the way for
civilians to use civilian weaponry instead of chungillionarius.

### ABR-40 Hunting Rifle

This is intended as asset recycling. IIRC, Triiodine disliked the
existence of a ceremonial rifle and thought that was goofy, which is an
understandable opinion, but it pains me to see the gun's cool assets go
unused. I took the opportunity and made the lame and mediocre Basira
into this cool gun which marines and survivors will take a lot more
interest in than a Basira plinker.

While it does have L42 stats, colonists won't be able to locate any L42A
ammo on the colony, meaning they are limited to 12-round magazines.
Still, giving them a weapon like this is a great way to incentivize them
to step out of their chungus zone.

As for the contractor addition, these are supposed to be ex-USCM
mercenaries, who are trained in the usage of marine equipment. It makes
sense that they'd grab the civilian version of a primary marine gun and
tune it to their liking.

### Basira-Armstrong Bolt-Action Hunting Rifle

Chomp made this really cool backend for a bolt-action that tragically
ended up never being used, not really, aside from a half-hearted few
rifles being thrown in at Shiva's Snowball. Since these guns are so
weak, it's plain to see why nobody even looks at them twice. So I
changed that.

### M37-17 Pump Shotgun

Bugfix and a small damage buff to make up for it. It being unacidable
was lame anyways. Spread projectiles are still bugged and don't inherit
the base gun's damage mod, but that's out of scope.

### Dragunov Designated Marksman Rifle

This gun has been a joke since 2017, it's time to give it some love.
Still needs one-hand sprites but not my problem.

# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
balance: Updates and buffs the following weapons: Basira-Armstrong
Rifle, Model 12 Bolt-Action Rifle, M37-17 pump shotgun, Dragunov sniper
rifle
imageadd: The Basira rifle has been reflavored as the removed
'ceremonial' ABR-40, now a hunting-civilian version of the L42. It
effectively has the same stats as the L42, just don't take the stock
off!
add: Its magazines can only fit 12 bullets, but they still have the
classic L42 kick to them. The magazines are completely compatible
between both military and civilian gun types.
add:: Additionally, there are now holo-targeting magazines available for
the ABR-40, for hunting target capture purposes.
add: The Contractor ERT has a chance to spawn with a tacticool ABR-40
loadout, with three spare holotarget magazines on their webbing.
balance: Like the bolt-action rifle's sprite implies, this is now the
new Basira-Armstrong rifle.
add: Its stats have recieved an overhaul and it can now hold its own
against a Xenomorph (or marine if you're CLF)
add: Additionally, its bullets will push back (not stun) targets within
three meters, to increase viability for colony usage.
balance: Did you know that the 10% damage mod the M37-17 pump shotgun
was supposed to have didn't work? Now it does! And it deals 15% more
damage to make up for it.
del: However, it can now be melted down.
balance: The dragunov has been revamped into a DMR, needing no skill to
fire, dealing good damage, and having the same push-back feature the
bolt-action now has.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [morrowwolf/cmss13](https://github.com/morrowwolf/cmss13)@[b4954e1402...](https://github.com/morrowwolf/cmss13/commit/b4954e14028909b107d0b204da0ad06c5dfeb50a)
#### Monday 2023-02-13 08:15:29 by carlarctg

zombie powder fix (#2315)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

Fixes Zombie Powder bugging the fuck out by slapping a ton of FAKEDEATH
checks everywhere. It now properly shows the holder as dead on HUDs and
scans.

Fixed an issue in which sometimes qdeleted reagents still procced on
life.

Fixed examining things changing your direction if you're incapacitated.

Added FAKEDEATH to the mob_incapacitated() check.


# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
fix: Fixes Zombie Powder bugging the fuck out by slapping a ton of
FAKEDEATH checks everywhere. It now properly shows the holder as dead on
HUDs and scans.
fix: Fixed an issue in which sometimes qdeleted reagents still procced
on life.
fix: Fixed examining things changing your direction if you're
incapacitated.
fix: Added FAKEDEATH to the mob_incapacitated() check.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: harryob <me@harryob.live>

---
## [amjoseph-nixpkgs/nixpkgs](https://github.com/amjoseph-nixpkgs/nixpkgs)@[7483b8124f...](https://github.com/amjoseph-nixpkgs/nixpkgs/commit/7483b8124fef5c44e6912c974b74232f63426664)
#### Monday 2023-02-13 08:57:50 by Adam Joseph

stdenv: external gcc bootstrap

 #### Summary

By default, when you type `make`, GCC will compile itself three
times.  This PR inhibits that behavior by activating GCC's
`--disable-bootstrap` flag and implements the triple-rebuild using
Nix rather than `make`/`sh`.

 #### Immediate Benefits

- Allow `gcc11` on `aarch64`
- No more copying `libgcc_s` out of the bootstrap-files or other
  derivations
- No more [static lib{mpfr,mpc,gmp,isl}.a hack]
- *Zero* additional `gcc` builds (stage1+stage2+stageCompare)
  - The `gcc` derivation builds `gcc` once instead of three times.
  - The libraries that are linked into the final `pkgs.gcc` (`mpfr`,
    `mpc`, `gmp`, `isl`, `glibc`) are built by
    `stdenv.__bootPkgs.gcc` rather than by the `bootstrapFiles`.  No
    more Frankenstein compiler!
  - stageCompare runs **concurrently** with (not in series with) with `stdenv`'s dependees.
- Many other `stdenv` hacks eliminated.
  - `gcc` and `clang` share the same codepath for more of
    `cc-wrapper`.
  - Makes the cross and native codepaths much more similar --
    another step towards "cross by default".

Note that *all* the changes in this PR are controlled by flags; no old codepaths need to be removed until/if we're completely certain that this is the right way to go.

 #### Future Benefits

- This should allow using a [foreign] `bootstrap-files` so long as
  `hostPlatform.canExecute bootstrapFiles`.
- There will be an "avalanche of simplification" when we set
  `enableGccExternalBootstrap=true` and run dead code elimination.
  It's really quite a huge amount of code that goes away.
  Native-gcc has its own special codepath in so many places, while
  cross-gcc and clang work the same way (and are much simpler).
- This should allow each of the libraries that ship with `gcc`
  (`lib{backtrace,atomic,cc1,decnumber,ffi,gomp,iberty,offloadatomic,quadmath,sanitizer,ssp,stdc++-v3,vtv}`)
  to be built in separate (one-liner) derivations which `inherit
  src;` from `gcc`.
  - Building `libstdc++-v3` in a separate derivation will eliminate
    a lot of accidental-reference-to-the-`bootstrapFiles` landmines.

 #### Incorporates

- https://github.com/NixOS/nixpkgs/pull/209054
- https://github.com/NixOS/nixpkgs/pull/210004
- https://github.com/NixOS/nixpkgs/pull/36948 (unreverted)
- https://github.com/NixOS/nixpkgs/pull/210325
- https://github.com/NixOS/nixpkgs/pull/210118
- https://github.com/NixOS/nixpkgs/pull/210132
- https://github.com/NixOS/nixpkgs/pull/210109
- https://github.com/NixOS/nixpkgs/pull/213909

 #### Closes

- Closes #108305
- Closes #108111
- Closes #201254
- Closes #208412

 #### Build history

- First successful builds (stage1/stage2):
  - powerpc64le-linux at 9c7e9ef256714455914180c0bcb434e014e5b75a
  - x86_64-linux at 9c7e9ef256714455914180c0bcb434e014e5b75a
  - aarch64-linux at 4d5bc7dabfbe1f8758559390e373b91dda9d401e

- First successful comparisons (stageCompare):
  - at 81949cffa3272f8f9bdc8cfda8effb34be517d2f
  - [aarch64-linux][aarch64-compare-ofborg]
  - [x86\_64-linux][amd64-compare-ofborg]

 #### Credits

This project was made possible by three important insights, none of
which were mine:

1. @ericson2314 was the first to advocate for this change, and
   probably the first to appreciate its advantages.  External bootstrap
   is "cross by default".

2. @trofi has figured out a lot about how to get gcc to not mix up
   the copy of `libstdc++` that it depends on with the copy that it
   builds.  Now that gcc is written in C++, it depends on
   `libstdc++`, builds a copy of `libstdc++`, and builds auxiliary
   products (like `libplugin`) which depend on `libstdc++`.  @trofi
   developed an technique for keeping this straight: moving the
   `bootstrapFiles`' `libstdc++` into a [versioned directory].
   Without this discovery, external bootstrap would be impossible,
   because the final gcc would still have references to the
   `bootstrapFiles`.

3. Using the undocumented variable [`user-defined-trusted-dirs`]
   when building glibc.  When glibc `dlopen()`s `libgcc_s.so`, it
   uses a completely different and totally special set of rules for
   finding `libgcc_s.so`.  This trick is the only way we can put
   `libgcc_s.so` in its own separate outpath without creating
   circular dependencies or dependencies on the bootstrapFiles.  I
   would never have guessed to use this (or that it existed!) if it
   were not for a [comment in guix] which @Mic92 [mentioned].

My own role in this PR was basically: being available to go on a
coding binge at an opportune moment, so we wouldn't waste a
[crisis].

[aarch64-compare-ofborg]: https://github.com/NixOS/nixpkgs/pull/209870/checks?check_run_id=10662822938
[amd64-compare-ofborg]: https://github.com/NixOS/nixpkgs/pull/209870/checks?check_run_id=10662825857
[nonexistent sysroot]: https://github.com/NixOS/nixpkgs/pull/210004
[versioned directory]: https://github.com/NixOS/nixpkgs/pull/209054
[`user-defined-trusted-dirs`]: https://sourceware.org/legacy-ml/libc-help/2013-11/msg00026.html
[comment in guix]: https://github.com/guix-mirror/guix/blob/5e4ec8218142eee8e6e148e787381a5ef891c5b1/gnu/packages/gcc.scm#L253
[mentioned]: https://github.com/NixOS/nixpkgs/pull/210112#issuecomment-1379608483
[crisis]: https://github.com/NixOS/nixpkgs/issues/108305
[foreign]: https://github.com/NixOS/nixpkgs/pull/170857#issuecomment-1170558348
[static lib{mpfr,mpc,gmp,isl}.a hack]: https://github.com/NixOS/nixpkgs/blob/2f1948af9c984ebb82dfd618e67dc949755823e2/pkgs/stdenv/linux/default.nix#L380

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[c68a159884...](https://github.com/odoo-dev/odoo/commit/c68a15988432b201ae3786eb54bac3110c4242f4)
#### Monday 2023-02-13 09:13:15 by Arnold Moyaux

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

X-original-commit: 97f52bd40d97109a7983549d252476959ddceada
Part-of: odoo/odoo#112325

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[f05491105f...](https://github.com/odoo-dev/odoo/commit/f05491105f93939490cbeb078cb7653c38685644)
#### Monday 2023-02-13 09:15:02 by Romain Derie

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

closes odoo/odoo#111531

X-original-commit: 8f24aba86faf2639109b56887781b0daaf60be98
Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>

---
## [amjoseph-nixpkgs/nixpkgs](https://github.com/amjoseph-nixpkgs/nixpkgs)@[9dacac7b75...](https://github.com/amjoseph-nixpkgs/nixpkgs/commit/9dacac7b75ce13841c0053e59c23c57d0df6707c)
#### Monday 2023-02-13 09:39:30 by Adam Joseph

stdenv: external gcc bootstrap

 #### Summary

By default, when you type `make`, GCC will compile itself three
times.  This PR inhibits that behavior by activating GCC's
`--disable-bootstrap` flag and implements the triple-rebuild using
Nix rather than `make`/`sh`.

 #### Immediate Benefits

- Allow `gcc11` on `aarch64`
- No more copying `libgcc_s` out of the bootstrap-files or other
  derivations
- No more [static lib{mpfr,mpc,gmp,isl}.a hack]
- *Zero* additional `gcc` builds (stage1+stage2+stageCompare)
  - The `gcc` derivation builds `gcc` once instead of three times.
  - The libraries that are linked into the final `pkgs.gcc` (`mpfr`,
    `mpc`, `gmp`, `isl`, `glibc`) are built by
    `stdenv.__bootPkgs.gcc` rather than by the `bootstrapFiles`.  No
    more Frankenstein compiler!
  - stageCompare runs **concurrently** with (not in series with) with `stdenv`'s dependees.
- Many other `stdenv` hacks eliminated.
  - `gcc` and `clang` share the same codepath for more of
    `cc-wrapper`.
  - Makes the cross and native codepaths much more similar --
    another step towards "cross by default".

Note that *all* the changes in this PR are controlled by flags; no
old codepaths need to be removed until/if we're completely certain
that this is the right way to go.

 #### Future Benefits

- This should allow using a [foreign] `bootstrap-files` so long as
  `hostPlatform.canExecute bootstrapFiles`.
- There will be an "avalanche of simplification" when we set
  `enableGccExternalBootstrap=true` and run dead code elimination.
  It's really quite a huge amount of code that goes away.
  Native-gcc has its own special codepath in so many places, while
  cross-gcc and clang work the same way (and are much simpler).
- This should allow each of the libraries that ship with `gcc`
  (`lib{backtrace, atomic, cc1, decnumber, ffi, gomp, iberty,
  offloadatomic, quadmath, sanitizer, ssp, stdc++-v3, vtv}`) to be
  built in separate (one-liner) derivations which `inherit src;`
  from `gcc`.
  - Building `libstdc++-v3` in a separate derivation will eliminate
    a lot of accidental-reference-to-the-`bootstrapFiles` landmines.

 #### Incorporates

- https://github.com/NixOS/nixpkgs/pull/209054
- https://github.com/NixOS/nixpkgs/pull/210004
- https://github.com/NixOS/nixpkgs/pull/36948 (unreverted)
- https://github.com/NixOS/nixpkgs/pull/210325
- https://github.com/NixOS/nixpkgs/pull/210118
- https://github.com/NixOS/nixpkgs/pull/210132
- https://github.com/NixOS/nixpkgs/pull/210109
- https://github.com/NixOS/nixpkgs/pull/213909

 #### Closes

- Closes #108305
- Closes #108111
- Closes #201254
- Closes #208412

 #### Build history

- First successful builds (stage1/stage2):
  - powerpc64le-linux at 9c7e9ef256714455914180c0bcb434e014e5b75a
  - x86_64-linux at 9c7e9ef256714455914180c0bcb434e014e5b75a
  - aarch64-linux at 4d5bc7dabfbe1f8758559390e373b91dda9d401e

- First successful comparisons (stageCompare):
  - at 81949cffa3272f8f9bdc8cfda8effb34be517d2f
  - [aarch64-linux][aarch64-compare-ofborg]
  - [x86\_64-linux][amd64-compare-ofborg]

 #### Credits

This project was made possible by three important insights, none of
which were mine:

1. @ericson2314 was the first to advocate for this change, and
   probably the first to appreciate its advantages.  External bootstrap
   is "cross by default".

2. @trofi has figured out a lot about how to get gcc to not mix up
   the copy of `libstdc++` that it depends on with the copy that it
   builds.  Now that gcc is written in C++, it depends on
   `libstdc++`, builds a copy of `libstdc++`, and builds auxiliary
   products (like `libplugin`) which depend on `libstdc++`.  @trofi
   developed an technique for keeping this straight: moving the
   `bootstrapFiles`' `libstdc++` into a [versioned directory].
   Without this discovery, external bootstrap would be impossible,
   because the final gcc would still have references to the
   `bootstrapFiles`.

3. Using the undocumented variable [`user-defined-trusted-dirs`]
   when building glibc.  When glibc `dlopen()`s `libgcc_s.so`, it
   uses a completely different and totally special set of rules for
   finding `libgcc_s.so`.  This trick is the only way we can put
   `libgcc_s.so` in its own separate outpath without creating
   circular dependencies or dependencies on the bootstrapFiles.  I
   would never have guessed to use this (or that it existed!) if it
   were not for a [comment in guix] which @Mic92 [mentioned].

My own role in this PR was basically: being available to go on a
coding binge at an opportune moment, so we wouldn't waste a
[crisis].

[aarch64-compare-ofborg]: https://github.com/NixOS/nixpkgs/pull/209870/checks?check_run_id=10662822938
[amd64-compare-ofborg]: https://github.com/NixOS/nixpkgs/pull/209870/checks?check_run_id=10662825857
[nonexistent sysroot]: https://github.com/NixOS/nixpkgs/pull/210004
[versioned directory]: https://github.com/NixOS/nixpkgs/pull/209054
[`user-defined-trusted-dirs`]: https://sourceware.org/legacy-ml/libc-help/2013-11/msg00026.html
[comment in guix]: https://github.com/guix-mirror/guix/blob/5e4ec8218142eee8e6e148e787381a5ef891c5b1/gnu/packages/gcc.scm#L253
[mentioned]: https://github.com/NixOS/nixpkgs/pull/210112#issuecomment-1379608483
[crisis]: https://github.com/NixOS/nixpkgs/issues/108305
[foreign]: https://github.com/NixOS/nixpkgs/pull/170857#issuecomment-1170558348
[static lib{mpfr,mpc,gmp,isl}.a hack]: https://github.com/NixOS/nixpkgs/blob/2f1948af9c984ebb82dfd618e67dc949755823e2/pkgs/stdenv/linux/default.nix#L380

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[fedf2f3a26...](https://github.com/LemonInTheDark/tgstation/commit/fedf2f3a26869848f5fc8f41381d1aff944ed9f6)
#### Monday 2023-02-13 10:19:55 by Sol N

more span macro changes in brain traumas and disease files (#73273)

## About The Pull Request

i was fucking around with brain traumas on a downstream and noticed they
had similar issues to quirks so i decided to continue work from #73116


![Code_Klx14O288V](https://user-images.githubusercontent.com/116288367/217046732-765ffe27-73c9-416a-833e-e0d9e2aa7a86.png)
(search in VSC for span class = 'notice')
its going to be a bit of a thing to get all of these but this is a
decent chunk i think

there was only one annoying/tough file.
imaginary_friend.dm had class = 'game say' and class = 'emote' both of
which after some testing did not seem like they did anything. ill try to
keep that in mind in other files if i continue to do this but i either
omitted them because they didnt have any formatting or, in the case of
emote, turned it into name, which i think is what you'd want those
messages to look like.

there were also a few small spelling errors that i fixed

## Why It's Good For The Game

more consistent and stops people from copying brain trauma formatting
wrong

## Changelog

they should all work the same

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [stanalbatross/cmss13](https://github.com/stanalbatross/cmss13)@[43d54b4097...](https://github.com/stanalbatross/cmss13/commit/43d54b40970cc1a6c8ea8502a74b4d31dfd41b0f)
#### Monday 2023-02-13 11:16:35 by Stan_Albatross

TGUI disposals (#2153)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

converted disposals to TGUI

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


TESTING MY USE OF GITLENS

also fuck nanoui

# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
ui: converted disposals to tgui
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

Co-authored-by: Stan_Albatross <swt91a@gmail.com>

---
## [Satont/tsuwari](https://github.com/Satont/tsuwari)@[5c99f68609...](https://github.com/Satont/tsuwari/commit/5c99f6860954e54bd9149a96d8b71e533146f8c5)
#### Monday 2023-02-13 11:21:06 by Satont

fix(public): add check on empty aliases for commands list

I have no fucking idea what is going on here, frontend world is fucking ugly shit, i do not wanna learn HOW and WHERE it is broken, so i did stupied fix for that bug

---
## [shaffenmeister/squeezelite](https://github.com/shaffenmeister/squeezelite)@[226efa300c...](https://github.com/shaffenmeister/squeezelite/commit/226efa300c4cf037e8486bad635e9deb3104636f)
#### Monday 2023-02-13 13:34:48 by Ralph Irving

So, I've made more tests with a simple HTTP server and a client just download data through a simple GET. It's 100% easy to reproduce the issue if the client throttle at say 160kbits/s and a file of ~3.5MB is transferred. The HTTP server confirms (as does tcpdump) that all is transferred in a record time and using TCPview (or netstat) you can see that the connection is in FIN_WAIT_2.

It is all received because the TCPWindow quickly gets massive (a few MB) and so are the kernel's buffers. Obviously, Windows has a half-open socket timer that is started with the first FIN send and that causes the issue 100% time.

By limiting SO_RCVBUF, the TCPWindow cannot open that large as soon as the application does not get data fast enough. Of course, when we'll fill the stream and output buffers, TCPWindow will open because we absorb data super fast, but it will shrink back as soon as we stop pumping data in because we are full.

Now, 4KB is awfully low and I tried to increase it and it was still fine at 65kB, I could see TCPWindow opening and closing. The funny thing is that when you do a getsockopt, system will return 65kB. If you set what you got, the problem disappear as expected. BUT, if don't set anything, then Windows uses some much larger value (although it told you it does not) and then the issues happens.

-philippe44.

Thanks philippe44 for tracking down the cause of this issue.
Increase squeezelite revision to 1419.

---
## [brokenphilip/bhoptimer-pyrokinesis](https://github.com/brokenphilip/bhoptimer-pyrokinesis)@[4837299eb4...](https://github.com/brokenphilip/bhoptimer-pyrokinesis/commit/4837299eb43cd6dfe0c892c41b7db0eb577f8baa)
#### Monday 2023-02-13 13:46:18 by brokenphilip

attempted to patch a few oob exploits using new zones that can be used to cheat runs. i say 'attempted' because i tried copying the zone entries from my production DB to this clean DB 10 times and i got 10 different results, none of which work fully. note to self: do NOT touch this cancerous fucking DB shit ever again

---
## [SynixeContractors/Missions](https://github.com/SynixeContractors/Missions)@[46d3b0c331...](https://github.com/SynixeContractors/Missions/commit/46d3b0c33162d71f2e341c3bd2f41d5323c766d1)
#### Monday 2023-02-13 14:14:26 by matidp4

CO30_Matias_MilkRun (#68)

* CO30_Matias_MilkRun

"This's nothin' but a milk run, boys. Guns for the good guys -- You'll be back at HQ for breakfast. Don't shit the bed and there'll be bonuses all around. Find me when your back..."

-Phillip Graves

* Add spawn points

* Template update

---
## [RooGhz720/Aghisna_Sweet_Kernel](https://github.com/RooGhz720/Aghisna_Sweet_Kernel)@[954a681c70...](https://github.com/RooGhz720/Aghisna_Sweet_Kernel/commit/954a681c70074ea930b0b766c41385fa56d65354)
#### Monday 2023-02-13 15:06:13 by Wang Han

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
Signed-off-by: Muhammed Ali Simsek <malisimsek17@gmail.com>

---
## [seanpdoyle/turbo](https://github.com/seanpdoyle/turbo)@[4a361a1e52...](https://github.com/seanpdoyle/turbo/commit/4a361a1e52e6f5c191bdd60bb2d0497c15de938e)
#### Monday 2023-02-13 16:03:33 by Sean Doyle

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
## [snagglegrolop/iHW-WatchOS](https://github.com/snagglegrolop/iHW-WatchOS)@[1a7cdb10cd...](https://github.com/snagglegrolop/iHW-WatchOS/commit/1a7cdb10cd8e050c0ef4554a8a7faf552b5159c5)
#### Monday 2023-02-13 16:11:25 by snagglegrolop

Xcode is being weird and not letting me see the changes I made since last commit so I'm going off of memory here. I got middle school schedules to now be able to know when the start of next period is or the end of 9th period. it turns red when there's only 5 minutes left too, kinda cool. I still need to have the program know when its a weekend, which will probably consist of stating a new value other than miscounter and it'll see if the date corresponds with what mscounter returns and if thats true then it'll show me the school day, if not then you can guess but yeah. I don't believe I did anything else. That took a big chunk of time anyways, so yeah.

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[1fe9efd00a...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/1fe9efd00aeb0e2d4f4dedf89460abacecef9d1b)
#### Monday 2023-02-13 18:06:56 by SkyratBot

[MIRROR] Rebuilds Luxury Shuttle (mostly), makes it emag-only [MDB IGNORE] (#19229)

* Rebuilds Luxury Shuttle (mostly), makes it emag-only (#72940)

## About The Pull Request
![2023 02 07-06 49
54](https://user-images.githubusercontent.com/70376633/217159751-790e6ded-8525-4d13-a5b5-6a3d8076a00e.png)
Changes the really goofy old lux shuttle to a cooler layout with some
additions to make it a luxury and not just
"anti-poor-people protection + food"

Shuttle was made bigger to make it less cramped for the luxury class,
pool was moved to its own room, added an arcade
and a bar corner, has real lasers to shoot poors with (20c each shot),
has fire extinguishers now
Adds a new preopen variant of hardened shutters
Adds a paywall pin subtype for the luxury shuttle, and a laser gun
subtype

Made emag-only at a price of 10000 credits
## Why It's Good For The Game

The old luxury shuttle looked REALLY awful with its pool, was pretty
cramped even in the luxury section and BARELY resembled a luxury..
This luxury shuttle provides luxuries such as a less poorly designed
pool, more space for legs, arcade, to make it resemble a luxury unlike
the old one

## Changelog
:cl:
add: Luxury Shuttle is now bigger, and less ugly! Poor people still get
it rough though...
/:cl:

* Rebuilds Luxury Shuttle (mostly), makes it emag-only

---------

Co-authored-by: jimmyl <70376633+mc-oofert@users.noreply.github.com>

---
## [ahmad-jundi/CIS345Project1](https://github.com/ahmad-jundi/CIS345Project1)@[d84e9b7f6e...](https://github.com/ahmad-jundi/CIS345Project1/commit/d84e9b7f6e8dbbae19199cd23d56ac3f6e689018)
#### Monday 2023-02-13 18:53:52 by ahmad-jundi

Adding Parallel Reduction

Sorry for the mess with the comments boys, I needed to organize my thoughts somewhere and ended up adding way too many comments :(  This can be cleaned up but this is a solid base until Naddie checks it over

---
## [oarenaucla/phillygis](https://github.com/oarenaucla/phillygis)@[20d241eb87...](https://github.com/oarenaucla/phillygis/commit/20d241eb8716304b47a3261ae11e168f476c2657)
#### Monday 2023-02-13 19:31:05 by Olivia Arena

Updated project proposal

# **Updated Midterm Proposal** 
**Group Name**: Logan Triangle: Health, History, and Home in Philadelphia
**Members:** Olivia Arena, Deja McCauley, Lindsey Morris, Cassie Truong

## **Changes**

- We’ve lost initial group members, so we’ve recalibrated the scope of our project. 
- We have also changed the way we are approaching our topic of Logan Neighborhood. Rather than thinking of the conditions of Logan Neighborhood as independent and fixed attributes, we want to think about community investment and divestment. We want to look at ways in which we can think about how to invest in Logan in ways that challenge historical disinvestment. 
- To do this, we have focused on broader buckets of public risk, housing, employment, and access to parks. We hope that future explorations will look at how to prioritize investments to strengthen community networks, protect residents from displacement while improving housing conditions, ensuring there are opportunities for small businesses, and that there is adequate access to open space and transit. 
- Our presentation follows this order: public risk, housing, unemployment, and access to parks. 

## **Research Question**
In terms of public health, affordable housing, amenities, and open space, what community needs emerge as a priority for North Philadelphia’s Logan neighborhood when using indicators (race, unemployment, food accessibility, open space access, and housing) to compare the area to the city as a whole?

## **Why this Matters**
Within the Logan neighborhood of Philadelphia, there is an area called Logan Triangle, which encompasses 48 vacant acres - making it one of the city’s largest sites of contiguous unused land. This area has been a site of environmental degradation, which has caused physical harm to the surrounding physical environment and likely the health of residents. Since the early 20th century, Logan Triangle’s history has been fraught. Although it was once home to over 5,000 Philadelphians, the instability of the land and other environmental hazards (both human-caused) led to the demolition of homes and displacement of residents. The 2023 American Planning Association’s Student Design Competition, uses Logan Triangle as a case study. Our team is tasked with creating a long-term plan for the area that focuses on public health, open space and nature, affordable housing, inclusive design and amenities, and the neighborhood’s history. There is an opportunity and need to redress the physical, environmental, and emotional harms that have occurred in Logan Triangle and the intent of the project is to envision a site that best serves the surrounding and future community of Logan Triangle. In this course, we plan to use spatial data and GIS to better understand existing conditions and community needs.

## **Spatial Scope**
The subject area will encompass the Logan Neighborhood of Philadelphia, as defined by the Logan Comprehensive Neighborhood Plan. The Neighborhood is bound by Olney Avenue on the North, E. Wister Street and Stenton Avenue on the West, N. 6th Street on the East, and W. Wingohocking Street on the South. 

For this project, we defined six census tracts as making up the “Logan Neighborhood.” These tracts include (FIPS codes): "42101028000", "42101028100", "42101028200", "42101028300", "42101028400", "42101028500." The Logan Triangle lies in the center of the neighborhood; this 48-acre block of land targeted for redevelopment was the site of a subsidence crisis where all residential homes were eventually demolished and its residents displaced. Because the Triangle has been cleared out of housing, there are no residents to include in Census analysis. Because of the absence of data, we extended our study area to look at the broader neighborhood. 

<img width="777" alt="Screen Shot 2023-02-12 at 11 47 18 PM" src="https://user-images.githubusercontent.com/122328335/218554096-d86e18df-77e7-43ed-9031-a283768a7b8b.png">

## **Data Sources**
Our team will use [Social Explorer](https://www.socialexplorer.com/) and [Philadelphia Open Data](https://www.opendataphilly.org/dataset) to analyze the neighborhood around the Logan Triangle and the greater Philadelphia area. Social Explorer will provide census data needed to better understand the community in Logan. Data downloaded from Social Explorer will include housing, demographics, and health. The majority of our data will come from Philadelphia Open Data, which provides datasets on planning/zoning, transportation, parks/recreation, and the environment. The specific data sources include: 

- Social Explorer (ACS 5-Year Estimates 2017-2021)
- OpenDataPhilly (Census Tracts, Affordable Housing Production from DHCD, Complaints against Police, SEPTA Locations API, Parks and Recreation)

## **Conclusion & Expectations** 
Through our research, we expect to gain insights on the type of community needs present for North Philadelphia’s Logan neighborhood residents. Specifically, we would like to gain a quantitative understanding of the access that Logan residents have to public health services, affordable housing, amenities, and open space. Furthermore, we would like to compare the access that Logan residents have in comparison to the city as a whole. In the future, there will also be opportunities to analyze how variables, such as race and income, intersect with Philadelphia resident’s access to services and amenities. Ultimately, we hope to develop a comprehensive spatial data analysis and produce powerful visuals that demonstrate the community needs of Logan, Philadelphia to inform the recommendations proposed for Logan Triangle. 

## **Future Exploration**
As we reframe our study, we want to look at the specific conditions of the housing stock (age, condition), calls to 311 about needed investment, small businesses and other community amenities, and potential expansion of transportation.

---
## [rn/linuxkit](https://github.com/rn/linuxkit)@[860934d5d9...](https://github.com/rn/linuxkit/commit/860934d5d98f0024ebc86896715863526f8fe96c)
#### Monday 2023-02-13 19:34:58 by Davide Brini

New output format: iso-efi-initrd

This option was previously not available and required postprocessing of a `tar-kernel-initrd` output.

Comparison with `iso-efi`:

`iso-efi` only loads the kernel at boot, and the root filesystem is mounted from the actual boot media (eg, a CD-ROM - physical or emulated). This can often cause trouble (it has for us) for multiple reasons:
- the linuxkit kernel might not have the correct drivers built-in for the hardware (see #3154)
- especially with virtual or emulated CD-ROMs, performance can be abysmal: we saw the case where the server IPMI allowed using a ISO stored in AWS S3 over HTTP...you can imagine what happens when you start doing random I/O on the root fs in that case.
- The ISO image has the root device name baked in (ie, `/dev/sr0`) which fails if for some reason the CD-ROM we're running from doesn't end up using that device, so manual tweaking is required (see #2375)

`iso-efi-initrd`, on the other hand, packs the root filesystem as an initramfs (ie similar to what the raw output does, except that in this case we're preparing an ISO image), so both the kernel and the initramfs are loaded in memory by the boot loader and, once running, we don't need to worry about root devices or kernel drivers (and the speed is good, as everything runs in RAM).

Also, the generated ISO can be copied verbatim (eg with `dd`) onto a USB media and it still works.

Finally, the image size is much smaller compared to `iso-efi`.

IMHO, `iso-efi-initrd` could be used almost anywhere `iso-efi` would be used, or might even supersede it. I can't think of a scenario where one might explicitly want to use `iso-efi`.

Points to consider:

- Not tested under aarch64 as I don't have access to that arch. If the automated CI tests also test that, then it should be fine.
- I'm not sure what to put inside `images.yaml` for the `iso-efi-initrd` image. As it is it works of course (my personal image on docker hub), but I guess it'll have to be some more "official" image. However, that cannot be until this PR is merged, so it's kind of a chicken and egg situation. Please advise.
- I can look into adding the corresponding `iso-bios-initrd` builder if there is interest.

![cute seal](https://sites.psu.edu/siowfa16/files/2016/09/baby-seal-29vsgyf-288x300.jpg)

Signed-off-by: Davide Brini <waldner@katamail.com>

---
## [GameDevNoOne/Rouge-Like](https://github.com/GameDevNoOne/Rouge-Like)@[009c7d3816...](https://github.com/GameDevNoOne/Rouge-Like/commit/009c7d3816972e5d39392df9b4d6aca713ce15ea)
#### Monday 2023-02-13 20:25:31 by GameDevNoOne

This was a stupid mistake.

I swear to god if my Math teacher saw this he'd kill me.

---
## [software-mansion/react-native-reanimated](https://github.com/software-mansion/react-native-reanimated)@[b83625045f...](https://github.com/software-mansion/react-native-reanimated/commit/b83625045f314e498fe32adc34b43ce20a77f946)
#### Monday 2023-02-13 20:43:03 by Angelika Serwa

Fix reloading when using useAnimatedKeyboard (#3932)

<!-- Thanks for submitting a pull request! We appreciate you spending
the time to work on these changes. Please follow the template so that
the reviewers can easily understand what the code changes affect. -->

## Summary

Fixes
https://github.com/software-mansion/react-native-reanimated/issues/3786

### Why it crashes: 
On the main thread `CADisplayLink` calls `updateKeyboardFrame` 60 times
per second. Calling `updateKeyboardFrame` calls listener on the JS side.
When reloading the runtime gets destroyed on the JavaScript thread. So
when those two things happen at the same time (which in this case
happens often) we get the crash that we're trying to call a js function
on destroyed js runtime.

### Why don't you just remove the listeners in
`NativeReanimatedModule::~NativeReanimatedModule()`, we're cleaning up
everything here:
I've tried and it appeared to work at first but I still got crashes when
running [the 1000 listeners
example](https://github.com/software-mansion/react-native-reanimated/pull/3911)
and probably that's why:

![Screenshot 2023-01-11 at 23 02
18](https://user-images.githubusercontent.com/6280457/211935579-16ff642d-fb15-469b-909e-e36ba9d72781.png)
![Screenshot 2023-01-11 at 23 02
35](https://user-images.githubusercontent.com/6280457/211935599-88cb9e81-20d7-4f96-bfd0-9c3b5da13b24.png)

So when `~NativeReanimatedModule` is being called the runtime related
stuff is already deleted and there is a short window of time that the
runtime is being deleted and we still call js stuff, or at least that's
my theory 🤷‍♀️

So my proposition for now is to listen for
`RCTBridgeDidInvalidateModulesNotification` notification. It's called
just before deleting happens. Also I'm using
`RCTUnsafeExecuteOnMainQueueSync` because I want to wait until the
listeners are completely deleted on the main thread and then delete js
stuff.

### A nicer solution? 
If you look a bit above `[[NSNotificationCenter defaultCenter]
postNotificationName:RCTBridgeDidInvalidateModulesNotification` line in
React code you'll see that React calls `invalidate` on all modules' data
before even posting the notification. Maybe we should clean reanimated
stuff here. I haven't explored that though yet and I don't know where is
reanimated's module data and what is module data at all and where to put
that `invalidate` function, I just got this idea while posting this PR.

## Test plan

Just run AnimatedKeyboardExample and reload the app.
Also the [the 1000 listeners
example](https://github.com/software-mansion/react-native-reanimated/pull/3911)
nicely catches other data races.

Tested with changes from
https://github.com/software-mansion/react-native-reanimated/pull/3911
and it works
Also tested on FabricExample and surprisingly it also works.

---
## [Conga0/Apotheosis](https://github.com/Conga0/Apotheosis)@[3738888f0f...](https://github.com/Conga0/Apotheosis/commit/3738888f0fe01d1eb4b8b7d8c42e94f533d799d2)
#### Monday 2023-02-13 21:31:12 by Conga Lyne

Rebalances, Fixes & Compatibility

Added Projectile failsafe to pitboss incase it copies too many projectiles
Moved teleport_liquid_powered.xml changed to vanilla_appends.lua
Increased Health of Polymorph Crystals in heaven from 40 to 80
Masters of Exchange no longer swap non-mortal entities
Weakening Curse Spells now increase damage vulnerabilities by 100% instead of a flat 0.25 increment
Reduced the price & recoil of various bounce modifiers
Significantly reduced damage of Juvenile Fire Lukki meteors
Giant Whisp no longer creates a trail of flame underneath itself (It feels unnecessary to punish the player for trying to avoid the whisp for going under, might undo this decision; but for now I feel confident you shouldn't be punished for trying to dodge the Whisp's charge by going in a specific direction instead of another)
Fixed Coral Chest Leviathan portal bringing you to the wrong location
Fixed Enemies with significantly increased HP having drastically more blood than intended

---
## [dallmeyer/jak-project](https://github.com/dallmeyer/jak-project)@[c249dbc437...](https://github.com/dallmeyer/jak-project/commit/c249dbc43750b0b811bbe4d10d29663bec39b9ae)
#### Monday 2023-02-13 21:40:11 by water111

[jak2] improve loader for jak 2 levels (#2206)

Add a debug window for the loader to show levels and fix an issue with
jak 2 level unloading. I never really thought about how this works for >
2 levels, and there is a chance that you could unload the wrong level in
some cases.

The problem is some combination of merc-only levels not counting toward
the "in use" detection, and the unloader ignoring what the game wants to
load.

I don't remember why using merc models doesn't contribute to "in use"
but I'm afraid to change this for jak 1. Instead, we can have the
unloader avoid unloading levels that the game is telling us are loaded.
This is what we should have done originally, but there was a time when
Jak 1 didn't tell the loader anything, and we had this stupid detection
thing.

I think this is the first step toward just getting rid of the "in use"
detection and trusting the game for everything.

---
## [amjoseph-nixpkgs/nixpkgs](https://github.com/amjoseph-nixpkgs/nixpkgs)@[ec41fea05b...](https://github.com/amjoseph-nixpkgs/nixpkgs/commit/ec41fea05b39e61421e62e1cb1741858866b8d6d)
#### Monday 2023-02-13 21:59:42 by Adam Joseph

stdenv: Nix-driven bootstrap of gcc

 #### Summary

By default, when you type `make`, GCC will compile itself three
times.  This PR inhibits that behavior by configuring GCC with
`--disable-bootstrap`, and reimplements the triple-rebuild using
Nix rather than `make`/`sh`.

 #### Immediate Benefits

- Allow `gcc11` and `gcc12` on `aarch64` (without needing new
  `bootstrapFiles`)
- No more copying `libgcc_s` out of the bootstrap-files or other
  derivations
- No more [static lib{mpfr,mpc,gmp,isl}.a hack]
- *Zero* additional `gcc` builds (stage1+stage2+stageCompare)
  - The `gcc` derivation builds `gcc` once instead of three times.
  - The libraries that are linked into the final `pkgs.gcc` (`mpfr`,
    `mpc`, `gmp`, `isl`, `glibc`) are built by
    `stdenv.__bootPkgs.gcc` rather than by the `bootstrapFiles`.  No
    more Frankenstein compiler!
  - stageCompare runs **concurrently** with (not in series with)
    with `stdenv`'s dependees.
- Many other `stdenv` hacks eliminated.
  - `gcc` and `clang` share the same codepath for more of
    `cc-wrapper`.
  - Makes the cross and native codepaths much more similar --
    another step towards "cross by default".

Note that *all* the changes in this PR are controlled by flags; no
old codepaths need to be removed until/if we're completely certain
that this is the right way to go.

 #### Future Benefits

- This should allow using a [foreign] `bootstrap-files` so long as
  `hostPlatform.canExecute bootstrapFiles`.
- There will be an "avalanche of simplification" when we set
  `enableGccNixDrivenBootstrap=true` and run dead code elimination.
  It's really quite a huge amount of code that goes away.
  Native-gcc has its own special codepath in so many places, while
  cross-gcc and clang work the same way (and are much simpler).
- This should allow each of the libraries that ship with `gcc`
  (`lib{backtrace, atomic, cc1, decnumber, ffi, gomp, iberty,
  offloadatomic, quadmath, sanitizer, ssp, stdc++-v3, vtv}`) to be
  built in separate (one-liner) derivations which `inherit src;`
  from `gcc`.
  - Building `libstdc++-v3` in a separate derivation will eliminate
    a lot of accidental-reference-to-the-`bootstrapFiles` landmines.

 #### Incorporates

- https://github.com/NixOS/nixpkgs/pull/209054
- https://github.com/NixOS/nixpkgs/pull/210004
- https://github.com/NixOS/nixpkgs/pull/36948 (unreverted)
- https://github.com/NixOS/nixpkgs/pull/210325
- https://github.com/NixOS/nixpkgs/pull/210118
- https://github.com/NixOS/nixpkgs/pull/210132
- https://github.com/NixOS/nixpkgs/pull/210109
- https://github.com/NixOS/nixpkgs/pull/213909

 #### Closes

- Closes #108305
- Closes #108111
- Closes #201254
- Closes #208412

 #### Build history

- First successful builds (stage1/stage2):
  - powerpc64le-linux at 9c7e9ef256714455914180c0bcb434e014e5b75a
  - x86_64-linux at 9c7e9ef256714455914180c0bcb434e014e5b75a
  - aarch64-linux at 4d5bc7dabfbe1f8758559390e373b91dda9d401e

- First successful comparisons (stageCompare):
  - at 81949cffa3272f8f9bdc8cfda8effb34be517d2f
  - [aarch64-linux][aarch64-compare-ofborg]
  - [x86\_64-linux][amd64-compare-ofborg]

 #### Credits

This project was made possible by three important insights, none of
which were mine:

1. @ericson2314 was the first to advocate for this change, and
   probably the first to appreciate its advantages.  Nix-driven
   (external) bootstrap is "cross by default".

2. @trofi has figured out a lot about how to get gcc to not mix up
   the copy of `libstdc++` that it depends on with the copy that it
   builds, by moving the `bootstrapFiles`' `libstdc++` into a
   [versioned directory].  This allows a Nix-driven bootstrap of gcc
   without the final gcc would still having references to the
   `bootstrapFiles`.

3. Using the undocumented variable [`user-defined-trusted-dirs`]
   when building glibc.  When glibc `dlopen()`s `libgcc_s.so`, it
   uses a completely different and totally special set of rules for
   finding `libgcc_s.so`.  This trick is the only way we can put
   `libgcc_s.so` in its own separate outpath without creating
   circular dependencies or dependencies on the bootstrapFiles.  I
   would never have guessed to use this (or that it existed!) if it
   were not for a [comment in guix] which @Mic92 [mentioned].

My own role in this PR was basically: being available to go on a
coding binge at an opportune moment, so we wouldn't waste a
[crisis].

[aarch64-compare-ofborg]: https://github.com/NixOS/nixpkgs/pull/209870/checks?check_run_id=10662822938
[amd64-compare-ofborg]: https://github.com/NixOS/nixpkgs/pull/209870/checks?check_run_id=10662825857
[nonexistent sysroot]: https://github.com/NixOS/nixpkgs/pull/210004
[versioned directory]: https://github.com/NixOS/nixpkgs/pull/209054
[`user-defined-trusted-dirs`]: https://sourceware.org/legacy-ml/libc-help/2013-11/msg00026.html
[comment in guix]: https://github.com/guix-mirror/guix/blob/5e4ec8218142eee8e6e148e787381a5ef891c5b1/gnu/packages/gcc.scm#L253
[mentioned]: https://github.com/NixOS/nixpkgs/pull/210112#issuecomment-1379608483
[crisis]: https://github.com/NixOS/nixpkgs/issues/108305
[foreign]: https://github.com/NixOS/nixpkgs/pull/170857#issuecomment-1170558348
[static lib{mpfr,mpc,gmp,isl}.a hack]: https://github.com/NixOS/nixpkgs/blob/2f1948af9c984ebb82dfd618e67dc949755823e2/pkgs/stdenv/linux/default.nix#L380

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[645054b489...](https://github.com/tgstation/tgstation/commit/645054b489212a34d80e6e1a7fa1320e35d9bfc7)
#### Monday 2023-02-13 22:28:50 by MrMelbert

Fixes encoding on syndicate declaration of war, Fixes a way to send unencoded text to newscasters (#73366)

## About The Pull Request

Ugly


![image](https://user-images.githubusercontent.com/51863163/218280311-f282bd75-2f6e-4290-b3f4-d9d856ff36d3.png)

Nice


![image](https://user-images.githubusercontent.com/51863163/218280315-233da635-f777-4006-8778-c673b83e887e.png)

War dec: 

- TGUI inputs for syndicate declaration of war no longer double-encode
sending customized messages into the announcement
- The alert box for the war declaration no longer has multiple errors
(an extra bracket, negative seconds)
- Reduces some copy and paste in the war declaration device
- Adds a debug item that's a war declaration device but it only does the
sound and message. Please don't fake war decs admins it's a horrible
idea

Additionally

- Documented `priority_announcement`
- Ensures all uses of text and title in the priority announcement
message are encoded (Some were not!)

## Why It's Good For The Game

Encoding looks bad, unencoded text is also bad

## Changelog

:cl: Melbert
fix: Syndicate declarations of war no longer murder apostrophes and
their friends
fix: The alert box for the declaration of war no longer looks funky, and
counts forwards in time rather than backwards
fix: Fixed being able to send unencoded HTML to newscasters
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---

