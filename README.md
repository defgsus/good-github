## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-11-21](docs/good-messages/2022/2022-11-21.md)


2,115,215 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,115,215 were push events containing 3,172,369 commit messages that amount to 257,725,914 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 36 messages:


## [h-vetinari/scipy](https://github.com/h-vetinari/scipy)@[c73e088350...](https://github.com/h-vetinari/scipy/commit/c73e0883501a21cfaf7220a8118a6155857b5829)
#### Monday 2022-11-21 00:12:07 by Tyler Reddy

MAINT: add `SCIPY_USE_PROPACK` env variable (#16361)

* this is effectively a forward port and modernization
of the release branch `PROPACK` shims that were added in
gh-15432; in short, `PROPACK` + Windows + some linalg backends
was causing all sorts of trouble, and this has never been resolved

* I've switched to `SCIPY_USE_PROPACK` instead of `USE_PROPACK`
for the opt-in, since this was requested, though the change
between release branches may cause a little confusion (another
release note adjustment to add maybe)

* I think the issues are painful to reproduce; for my part,
I did the following just to check the proper skipping/accounting
of tests:

- `SCIPY_USE_PROPACK=1 python dev.py -j 20 -t scipy/sparse/linalg`
  - `932 passed, 172 skipped, 8 xfailed in 115.57s (0:01:55)`
- `python dev.py -j 20 -t scipy/sparse/linalg`
  - `787 passed, 317 skipped, 8 xfailed in 114.80s (0:01:54)`

* why am I doing this now? well, to be frank the process of manually
backporting this for each release is error-prone, and may cause
additional confusion/debate, which I'd like to avoid. Besides, if it
is broken in `main` we may as well have the shims there as well. I would
point out that you may want to add `SCIPY_USE_PROPACK` to 1 or 2 jobs
in CI? The other reason is that if usage of `PROPACK` spreads, I don't
want to be manually applying more skips/shims on each release (which
I already had to do here with two new tests it seems)

---
## [Zergspower/Skyrat-tg](https://github.com/Zergspower/Skyrat-tg)@[317aea0435...](https://github.com/Zergspower/Skyrat-tg/commit/317aea043510ee0c3591ff3a06fdffd360fdfc29)
#### Monday 2022-11-21 00:52:17 by Jolly

[FUCK] [NO GBP] Yeah, fixes something in NuInterlink(?) (#17544)

fucking GODDAMNIT

---
## [SansSarif/orbstation](https://github.com/SansSarif/orbstation)@[84a85c827d...](https://github.com/SansSarif/orbstation/commit/84a85c827d71b3326b482444a204711de38cf518)
#### Monday 2022-11-21 01:07:29 by lizardqueenlexi

Removed TRAIT_PLASMABURNT, fixed plasma river limb transformation. (#71157)

## About The Pull Request

Resolves #67282.

As originally designed, plasma rivers (namely, those on Icebox, though
the turf was originally made for the Snowdin away mission) are meant to
literally strip the flesh from your bones, leaving you with plasmaman
limbs. I'm not certain when this broke entirely, although it seems to
have never been updated to work alongside Kapulimbs.

Transformation of limbs into plasmaman limbs used to be accomplished by
adding the "PLASMABURNT" trait to limbs. However, this trait in the
current code is entirely meaningless, only checked in the proc that
makes plasmamen catch fire. Essentially, the only "interaction" is
having your flesh melted off by a plasma river, donating that specific
limb to a plasmaman, and pranking them with the fact that that specific
limb will still make them burst into flames.

Exciting.

I've removed the trait entirely, as it does functionally nothing, and
restored the ability of plasma rivers to turn your limbs - and
eventually, you - into plasmaman equivalents.

To be honest, I'm not _entirely_ satisfied with the plasmaman
transformation process - it doesn't especially suit the lore of
plasmamen, and if you transform into one in the plasma rivers you'll
probably immediately die from Icemoon's atmosphere anyway. However, this
is something I'd prefer to revisit in a later PR.
## Why It's Good For The Game

There's little reason _not_ to remove a trait that does nothing.

As for plasmafication, it's a fun interaction that was already _meant_
to be there. The message about your flesh melting off has always
printed, even while it's doing exactly nothing to you. It's cool to fall
into the deadly plasma river and come away from it permanently scarred
with a weird skeleton limb. Turning into a plasmaman entirely is
unlikely to happen and will probably just kill you, but it's a fun and
weird way to be dead.
## Changelog
:cl:
del: Removed the useless "plasmaburnt" trait.
fix: Restored a broken interaction with plasma rivers that slowly
transforms you into a plasmaman.
/:cl:

---
## [ZephyrTFA/tgstation](https://github.com/ZephyrTFA/tgstation)@[de662db397...](https://github.com/ZephyrTFA/tgstation/commit/de662db39763674f850977dabc8bbe66388d2c9b)
#### Monday 2022-11-21 01:41:42 by Sol N

Excercise Equipment is now craftable (#71190)

## About The Pull Request

Imagine if you will a humble chaplain who wants nothing more than for
all of the spiritual folk on the station to get as massive gains as they
can, after finding that they can not just make more exercise equipment
and that the station does not have any in public places, they go annoy
security enough to get into permabrig only to find out that they cant
even unwrench the equipment and move it to the church!!!

NOT ANYMORE!!!


![jS2aBMBa0B](https://user-images.githubusercontent.com/116288367/200889423-f1b6365c-24c4-4f45-8ca4-c96c9085cf27.png)
crafting recipies


![dreamseeker_O4BgBRsFa8](https://user-images.githubusercontent.com/116288367/200889002-8dd7c927-0745-46a9-a4bc-578c7279042a.gif)
demonstrating unwrenching and wrenching equipment


![dreamseeker_hCFQJZdzoS](https://user-images.githubusercontent.com/116288367/200889019-5f4c8399-d539-4d84-8a3f-7735c3ba1f68.gif)
crafting a punching bag and punching it

Now you can craft as much exercise equipment as you want! May everyone
on the station get as strong as possible and not just prisoners.

Also I changed the message that plays when you try to use exercise
equipment someone else is using into a balloon alert.

![dreamseeker_PwNesmcR1f](https://user-images.githubusercontent.com/116288367/200890964-4f9fa3ee-ce07-4e6e-815c-a3f4593d06b1.png)

## Why It's Good For The Game

Access to exercise equipment on some maps is limited to static positions
and is currently mostly only for prisoners as every map does not have
public exercise equipment. Expanding the access means that you can have
a Drill Sargent Head of Security or Captain who commands people use
these or allows a psychologist to prescribe healthy exercise habits to
their patients.

I think having the potential for exercise equipment on every map is more
fun and also if prisoners get their hands on tools they should be
allowed to mess with these to annoy security or aid in their escape.

## Changelog
:cl:
add: the punching bag, bench press, and chest press are all able to be
crafted and unanchored.
add: crafting recipes for the above
qol: changed a chat message into a balloon alert
qol: adds screentips to equipment (thanks for suggesting i do this
mothblocks!)
/:cl:

---
## [hashgraph/hedera-services](https://github.com/hashgraph/hedera-services)@[86a33c9031...](https://github.com/hashgraph/hedera-services/commit/86a33c90314f5698e1fac863b4ca980a99078d48)
#### Monday 2022-11-21 01:47:49 by David Bakin

Eliminate Immmutable* as being too much trouble

Turns out Immutable* are too much trouble.  They're especially hard to
read (as Java hasn't yet invented a replacement for type aliases (see
C/C++ `typedef`).  And they're not really necessary here as all users
of the results of these methods are friendly, none are going to
deliberately misuse the ability to modify these collections, and in
fact, there's no reason for them not to.  The attempt to achieve
clarity of semantics by letting the reader know that these data
structures are immutable and thus the reader doesn't have to worry
about keeping "current state" in mind is, in this case, not needed.
Reader can just figure that out on his own.

- So, guava immutable collections replaced by standard collections,
  and Apache ImmutablePair replaced by bespoke record type (which
  _also_ has the big advantage of being able to _name_ the components,
  I shouldn't have been seduced by ImmutablePair _especially_ that
  Java has record types - my bad).

Also, replaced uses in method return values of EntityNum by the actual
wrapped Long.  Nothing in this tool requires the full capabilities of
an EntityNum.  We're only interested in having the tags for the
contracts.

Signed-off-by: David Bakin <117694041+david-bakin-sl@users.noreply.github.com>

---
## [queercpu/script](https://github.com/queercpu/script)@[2e2a4a5f02...](https://github.com/queercpu/script/commit/2e2a4a5f02ff63dfdb1ab7b7713d7715c589d6c1)
#### Monday 2022-11-21 02:06:32 by home.cpu

week is finished... wrote a ton i think... pushing for this sunday.  theres one file thats not sorted its some stuff about twigs, her fantasy of veronica and a lengthy storm about icb complex, and thoughts about the future war....  im really tired today. could barely do anything but even still, i middled some 3d. made the crsytal and an eyeball.

---
## [maxenceLe-brun/site-la-plateforme](https://github.com/maxenceLe-brun/site-la-plateforme)@[b2b1843d61...](https://github.com/maxenceLe-brun/site-la-plateforme/commit/b2b1843d61b9d212bdc3929a766318efbb4d43eb)
#### Monday 2022-11-21 02:12:37 by Maxence Le Brun

sleep update

and yes, your dear programmer is going to sleep. As a human, he sleep once in a while to restore his sanity.
Have a good night everyone, and keep this in mind : if you ask something too hard => no shit sherlock

---
## [seanpdoyle/turbo](https://github.com/seanpdoyle/turbo)@[8fb11ed860...](https://github.com/seanpdoyle/turbo/commit/8fb11ed860c5905bbf063033c7f28851ba114178)
#### Monday 2022-11-21 02:20:19 by Sean Doyle

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
## [JadenArcm/Snowy-Kart](https://github.com/JadenArcm/Snowy-Kart)@[537e39b052...](https://github.com/JadenArcm/Snowy-Kart/commit/537e39b052b5885a2eab329aa6bade6286b06ffa)
#### Monday 2022-11-21 02:46:40 by JadenArcm

add EVERYTHING.

I hate life. GitHub's fork updating is fucking shit. Don't ever believe on it. It destroyed my hopes and dreams.

---
## [rachmayadi/odoo](https://github.com/rachmayadi/odoo)@[61270ee8bf...](https://github.com/rachmayadi/odoo/commit/61270ee8bffb6e85f8ff0d19c7a3889fdce2f486)
#### Monday 2022-11-21 03:03:12 by qsm-odoo

[FIX] website, *: allow to re-edit company team snippet images

*: website_sale

Since [1], it was not possible to edit a company team snippet image
anymore as soon as the page was saved once. Indeed that commit added
o_not_editable/contenteditable="false" on the parent column to make sure
no text can be added in that column and contenteditable="true" on the
images so that they are still editable (even though HTML-specs-wise
adding contenteditable="true" on images probably does not mean much as
images are self-closing tags, our editor understand that as the ability
to edit the image anyway). That contenteditable="true" part is however
removed when leaving edit mode... and was not restored upon entering
edit mode again.

This fixes the problems with a specific JS patch, we'll review to see if
better can be done in master.

Funny enough, that bug was actually gone in 15.0... by mistake. A recent
bug fix actually reintroduced that isolated bug at [2] (by reintroducing
the fact that images in a non-editable environment are not possible to
edit). The 3 opened tickets this commit mentions were actually reported
for 15.0 immediately after that, while the 14.0 being broken about this
since the beginning apparently did not bother anyone.

Note: as a forward-ported fix, this also takes the opportunity to clean
a bit what was done at [3]. (calling `_super`, no duplicated code,
adding comments, ...).

[1]: https://github.com/odoo/odoo/commit/656cac1bf21c7c5a56aa569008aac58436c747fb
[2]: https://github.com/odoo/odoo/commit/e113bae04a64a8bd341a80736086ab7c25079dd3
[3]: https://github.com/odoo/odoo/commit/e2f7b8fad76dc816b2f6864340d3740446117cdb

opw-3031217
opw-3032482
opw-3035289

closes odoo/odoo#104193

X-original-commit: e7c8fed8e373d7005c16c88d3a7bad6f425d13e5
Signed-off-by: Romain Derie (rde) <rde@odoo.com>
Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[f23645154e...](https://github.com/treckstar/yolo-octo-hipster/commit/f23645154e9807d3fa5b7ff75134e3f096d0e1a6)
#### Monday 2022-11-21 03:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [AtlasMediaGroup/TotalFreedomMod](https://github.com/AtlasMediaGroup/TotalFreedomMod)@[99a5897d44...](https://github.com/AtlasMediaGroup/TotalFreedomMod/commit/99a5897d44c42046b7468293cb03454d992c6bcd)
#### Monday 2022-11-21 06:03:10 by Video

Go fuck yourself Codacy
Codacy complained about me forgetting a "default" case in my rewrite of /moblimiter, so I have to do this shit.

---
## [L0stz/chess_weird_java](https://github.com/L0stz/chess_weird_java)@[c4ebc20622...](https://github.com/L0stz/chess_weird_java/commit/c4ebc20622841c44579c501609fd8a56513294da)
#### Monday 2022-11-21 06:45:35 by ForeverCubed

c:

Now, this is a story all about how
My life got flipped-turned upside down
And I'd like to take a minute
Just sit right there
I'll tell you how I became the prince of a town called Bel-Air
In West Philadelphia born and raised
On the playground was where I spent most of my days
Chillin' out, maxin', relaxin', all cool
And all shootin' some b-ball outside of the school
When a couple of guys who were up to no good
Started making trouble in my neighborhood
I got in one little fight and my mom got scared
She said, "You're movin' with your auntie and uncle in Bel-Air"
I begged and pleaded with her day after day
But she packed my suitcase and sent me on my way
She gave me a kiss and then she gave me my ticket
I put my Walkman on and said, "I might as well kick it"
First class, yo this is bad
Drinking orange juice out of a champagne glass
Is this what the people of Bel-Air living like?
Hmm, this might be alright
But wait, I hear they're prissy, bourgeois, all that
Is this the type of place that they just send this cool cat?
I don't think so
I'll see when I get there
I hope they're prepared for the prince of Bel-Air
Well, the plane landed and when I came out
There was a dude who looked like a cop standing there with my name out
I ain't trying to get arrested yet, I just got here
I sprang with the quickness like lightning, disappeared
I whistled for a cab and when it came near
The license plate said, "Fresh" and it had dice in the mirror
If anything I could say that this cab was rare
But I thought "Nah, forget it, yo, holmes to Bel Air"
I pulled up to the house about seven or eight
And I yelled to the cabbie, "Yo holmes, smell ya later"
I looked at my kingdom
I was finally there
To sit on my throne as the prince of Bel-Air

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[bbb956d2a6...](https://github.com/tgstation/tgstation/commit/bbb956d2a670656e546c35a09ec27295e5e06e94)
#### Monday 2022-11-21 07:15:11 by OrionTheFox

Removes Bowls from garbage spawners because they don't fit in trash bags and I'm SICK of not being able to clean! (#71152)

## About The Pull Request
Let me give you a scenario.

---

THIS, is you. Say hi!

![image](https://user-images.githubusercontent.com/76465278/200268480-9dcf1f45-3bc5-402d-b743-b0649deefb08.png)

You're a loyal janitor aboard NT-SS13. You love your job; despite the
dangers, it's generally not too busy or tedious. Just a spray, a sweep,
and put it all in a bag.

---

This. This is your enemy.

![image](https://user-images.githubusercontent.com/76465278/200269058-957ca433-4666-44b5-9c10-ae0da75219cb.png)

Some crewmembers continuously leave them in maintenance, tossing them
into garbage bins as they pass.
This bowl, you cannot spray it. You can sweep it as far as you want, but
in the end, cannot put it into the bag.

![image](https://user-images.githubusercontent.com/76465278/200269156-bbc7758b-9cbe-4a3b-8d17-9aa53254b4b2.png)

---

It exists to torment you.
Nothing more, nothing less.

You hate the bowl. And it hates you.
Wake up.

![image](https://user-images.githubusercontent.com/76465278/200269456-a7fda598-3556-4069-bd2a-44a8793c198f.png)
## Why It's Good For The Game
Usually when you pass a trash pile you expect it to have trash, and
entire bowls aren't technically trash code-wise, nor can you clean them.
Yes, this PR has a modicum of salt. It was salt left behind in THE DAMN
BOWLS.
## Changelog
:cl:
del: NT has decided to begin a Recycling initiative, asking crew to
please stop throwing their bowls away in maintenance. You should only
find trash and grime from now on!
/:cl:

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[c1f0141967...](https://github.com/tgstation/tgstation/commit/c1f01419671ad084a6c048ec7900d008de53bfe2)
#### Monday 2022-11-21 07:15:49 by LemonInTheDark

Fixes mineral turfs having weird lighting (#71219)

## About The Pull Request

Pixel offsets, unlike transforms, offset overlays too. this was breaking
lighting overlays for mineral walls.

We did pixel offsets to save on init time, but we can acomplish the same
thing using an initial matrix. It's static, so there's no additional
cost. S free

Damn moth

## Changelog
:cl:
fix: Mining walls won't have fucked lighting anymore
/:cl:

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[0747099063...](https://github.com/tgstation/tgstation/commit/074709906301e3e396179c861ca0af068c3f36ec)
#### Monday 2022-11-21 07:17:36 by RikuTheKiller

Adds a reagent injector component and BCI manipulators to all circuit labs (#71236)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

This PR adds a reagent injector component that's exclusive to BCIs.
(Requested to be integrated into BCIs by Mothblocks.)
When outside of a circuit, the component itself stores the reagents.
However, if it's inside of a BCI, the storage is moved to the BCI. The
storage can contain up to 15u of reagents and acts like an open
container. (However, it won't spill even if you throw it, it just acts
like an open container code-wise, don't worry about it.)
You can only have one reagent injector in a circuit. Trying to insert
multiple will give you an error message.
The entire dose is administered at once. (Requirement set by
Mothblocks.)

Please don't try to dispute any of the specific limitations in the
comments as they're out of my control. They're reasonable anyways.

Reagent Injector Input/Output:
Inject (Input Signal) - Administers all reagents currently stored inside
of the BCI into the user.
Injected (Output Signal) - Triggered when reagents are injected. Not
triggered if the reagent storage is empty.

New BCI Input:
Show Charge Meter (Number) - Toggles showing the charge meter action.
(Adds some capacity for stealth.)

Install Detector Outputs: (Added following a comment about having to use
weird workarounds for proper loops.)
Current State (Number) - Outputs 1 if the BCI is implanted and 0 if it's
not.
Installed (Signal) - Triggered when the BCI is implanted into it's user.
Removed (Signal) - Triggered when the BCI is removed from it's user.

This PR also adds BCI manipulation chambers to all currently present
circuit labs. (Solution proposed by Mothblocks.)
Yes I had to do some other mapping changes to allow for this. No I don't
have any mapping experience, why do you ask?

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

One small step for BCIs, one giant leap for circuit kind. (First
"proper" circuit to human interaction in the entire game!)

This allows for some funky stuff and also makes it less of a pain in the
ass to use BCIs. What's not to love?

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
add: Added a reagent injector component and BCI manipulators to all
circuit labs. (+ install detector component)
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[bf582cb833...](https://github.com/tgstation/tgstation/commit/bf582cb833d89b7121b4fefa37e8da1773783245)
#### Monday 2022-11-21 07:18:32 by Profakos

Trophy case update (#71015)

## About The Pull Request

I have been chipping away/procrastinating at this since May, but after
several years, I have finally updated how Trophy Cases work.

So, what this PR does is the following:

- Standardized everything in persistence.dm to use snake case, and added
basic autodocs
- Automatically moves trophies from data/npc_saves/TrophyItems.json to
data/trophy_items.json. Removed legacy .sav conversion by request, it
has been a long time.
- Trophy cases are opened and loaded the same way you would open a
regular ID locked display case (used curator access, relevant access
autodoc has been updated)
- Instead of cheap plastic replicas that turn to dust anyways, trophy
cases use holograms, which can be dispelled by hand
- Trophy data gets saved if an item stays in the trophy case when the
shuttle arrives to centcom, and the item has a description set. This is
in line with paintings, which has to still hang on the wall at round
end.
- You can edit the description of new trophies by using the librarian's
key to unlock History Mode
- When you click on a closed trophy case, it will open a tgui, and will
not display the case description. It will still do for open cases.
Vendatrays have been updated to do the same.
- The UI's icon uses icon2base64(getFlatIcon(showpiece, no_anim=TRUE)).
Vendatrays have been updated similarly, so items with directions and
animations are displayed properly. The base64 strings are updated in
update_static_data.
- Fixes vendatrays from displaying some characters in strange ways, such
as displaying /improper.
- Renames some one letter, or nonindicate argument and var names in
trophy case code
- Adds a trophy management admin panel, where admins can finally delete
all the curator ID cards swallowed over the years. Or, they can replace
the paths with funny new paths.
- If an entry has an incorrect, no longer existing path, it will be
marked red in the management panel
- Adds MAX_PLAQUE_LEN define, which 144 characters
- Removes start_showpieces from trophy cases, as it was completely
unused. The start_showpiece_type var is still around.
- Moves trophy_message var to trophy cases. Only a dice collector
display case used them in the Snowdin map.

What this PR does not do

- Sadly, it still only saves the base image of an item, and no layers or
altered image states. This has to come in the future.

<details>
<summary>Click here to see various states of the trophy tgUI</summary>
 

![kép](https://user-images.githubusercontent.com/2676196/199545412-e5b7e7a8-59fb-41e6-aca5-6b07ba33501c.png)
Locked history mode, existing item.


![kép](https://user-images.githubusercontent.com/2676196/199545574-9e705603-9b7a-457d-9575-2d4145ad940d.png)
Unlocked history mode, but holographic trophy is present.


![kép](https://user-images.githubusercontent.com/2676196/199545883-45c3916b-011f-462a-8296-6eb13db32158.png)
Locked history mode, no item.


![kép](https://user-images.githubusercontent.com/2676196/199545967-a33e2501-aa5f-473b-b79f-ebd950df2afc.png)
Unlocked history mode, no item.


![kép](https://user-images.githubusercontent.com/2676196/199546100-718bd639-3199-4df7-ad77-ed3dbf27b290.png)
Unlocked history mode, item placed, default text. (Note: this picture is
out of date. The typo has been fixed, and "record a message" is now
"record a description" for consistency)
 

![kép](https://user-images.githubusercontent.com/2676196/199546202-5ebbbd28-907c-4f2d-b7cd-29d2ef21c7f3.png)
Unlocked history mode, item placed, new text.

</details>

<details>
<summary>Click here to see the admin panel</summary>


![kép](https://user-images.githubusercontent.com/2676196/199553349-8684f23f-4699-42f2-a27e-15cccad29d0b.png)


</details>

## Why It's Good For The Game

Less curator ID's stuck in the Trophy Cases, and the existing ones can
be cleaned up. A more immersive Trophy Case user experience, in general.

## Changelog


:cl:
refactor: refactored trophy cases, to be more user friendly
admin: created a trophy managment admin panel
/:cl:

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[b77cf7c120...](https://github.com/san7890/bruhstation/commit/b77cf7c1205d466b8cb242cd3302891e82b44da2)
#### Monday 2022-11-21 07:29:23 by Iamgoofball

Hotkey-based inventory management now applies the click cooldown to prevent it from being abusable in combat scenarios. (#71325)


About The Pull Request

Hotkey-based inventory management now applies the click cooldown to prevent it from being abusable in combat scenarios.
Why It's Good For The Game

Players have been deploying unbelievable levels of abuse with these hotkeys having completely uncapped speeds.
I watched one cheater do automated inventory management using storage items and weirdly named empty pills to use as inventory delimiters.
Resolves people being able to have a baton hidden in their backpack and then activate and baton someone with it in 0.1 seconds without moving their mouse cursor off of their target.

Players should not be able to interact with their inventory faster than someone moving a mouse and clicking the left mouse button. This cripples the game balance and puts anyone with a worse internet connection, slower reaction speeds, or laggier computer at a distinct disadvantage against people who can macro their inventory management.

I can set up autohotkey so that I can withdraw a stun baton from my backpack, turn it on, and then click someone by just holding down a key and pressing M1 over someone. This shit needs to stop.

If a do_after() on hotkey management is too harsh, we can apply a combat click cooldown every time you use the hotkeys instead to discourage combat macro abuse.
Swapped it over to a click cooldown.
Changelog

cl
balance: Hotkey-based inventory management now applies the click cooldown to prevent it from being abusable in combat scenarios.
/cl

---
## [Ameliyn/Computer-Science](https://github.com/Ameliyn/Computer-Science)@[6d94c59ea3...](https://github.com/Ameliyn/Computer-Science/commit/6d94c59ea33452ae36ae2ea789de7a85e86ae5d2)
#### Monday 2022-11-21 07:50:04 by Skye Russ

I HATE THE SHORTEST CYCLE ONE OML WHAT THE HELL THE INPUT WAS IN THE WRONG FORM AND DIDNT FUCKING WORK.      at least it's done now though. <3

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[cb20ec99f9...](https://github.com/tgstation/tgstation/commit/cb20ec99f9cac1f0ca60da1b9dc912ea4e9eebba)
#### Monday 2022-11-21 07:59:56 by san7890

[MDB Ignore] Unit Tests for Invalid Space Turfs (Area Bullshit Edition) (#70967)

## About The Pull Request

So, there's some bullshit with the map loader(?) sometimes where it'll
let space turfs spawn in spots where we REALLY don't want space turfs.
Or, it could also just be a mapper screwing up. Anyways, we might miss
these, so let's set up a broad Unit Test that checks and verifies that
these round-ruining snagglers do _not_ exist.

In order to help me to do this, I standardized and fixed the
nomenclature such that `/area/ruin/space` is default for any map file in
`_maps/RandomRuins/SpaceRuins`, as well as it's subtypes. I also touched
up how we handle shuttle areas in these scenarios. This got a lot of
Unit Test noise filtered out, and is crucial for its functioning. It
should also be how we did it from the start anyways. I added in an
UpdatePaths for any compatible change, but it was completely
non-workable for some of the area type updates.

I also fixed any organic bugs that didn't require an areas type update.
Cool.

Placing space turfs on IceBox:

![image](https://user-images.githubusercontent.com/34697715/199177940-21c64964-1808-41b0-9a92-bf5b82eee2fa.png)

Organically found issues:

![image](https://user-images.githubusercontent.com/34697715/199177972-b27a89de-0e1a-41e5-8fa4-3bee1763b9da.png)

I also added a `planetary` variable to `/datum/map_config` because I
didn't like the hack I was using to see if we had a planetary map, and
I'd rather it just be an explicit variable in the map's JSON.

## Why It's Good For The Game

The less times we get Space Turfs showing up on IceBoxStation, the
better. It also standardizes areas a bit more, which I like (we were
using some incorrect ones in the wrong spots, so those were touched up
in this PR as well). Like, if it's a space ruin, we don't need to use
the lengthy `/area/ruin/unpowered/no_grav` when `/area/ruin/space` does
the same thing.
## Changelog
Nothing in here should concern a player (unless I broke something)

Expect a few commits as I spam unit tests a few times and play
whack-a-mole with bugs.

---
## [etherware-novice/tgbagilsstation](https://github.com/etherware-novice/tgbagilsstation)@[25d4afc869...](https://github.com/etherware-novice/tgbagilsstation/commit/25d4afc869585373571da5ba4a77fb967ffdedfe)
#### Monday 2022-11-21 08:02:12 by Iamgoofball

Retires explosive lance crafting to a nice farm upstate where it has plenty of room to run around (#71256)

## About The Pull Request

You can no longer craft explosive lances.

## Why It's Good For The Game

Explosive lances are unhealthy for the game in it's current iteration.
Many years ago when the game was more loose and we weren't dealing with
players who treat the game like competitive TTT or Town of Salem,

They are a one shot kill weapon, which is the most powerful kind of
weapon in every gamemode. @JohnFulpWillard likened it to 1f1, a concept
from Town of Salem players where the town trades 1 person for 1 bad guy.

Modern ss13 design includes a significantly heavier load of antagonists
that aren't fixed roundstart compared to when the e-lance went in.

When we added the e-lance, if nuke ops spawned, that was it, there was
nuke ops, if you e-lanced the nuke ops and died you were dead until the
next round.

Nowadays you're rolling for lone operative, blob, wizard, disease,
revenant, and every other fun enjoyable antagonist role under the sun.

I can e-lance a nuke op/cultist/traitor/revolutionary/any bad guy in the
game as a non-antag assistant, die, and have a good chance to roll
another, way more fun antag in deadchat.

My change to make the e-lance a proper "we both die" tool didn't
actually help because I didn't quite realize that to the modern SS13
player because of how we designed Dynamic and antagonists in the modern
era, death is, frankly, not a punishment anymore.

It's time we admit the facts, items designed in 2015 SS13 in #12389
simply don't hold up in a healthy manner in 2022 SS13. Dying in SS13 in
2015 was a significantly different experience with different
consequences than it has now, and right now "kills you when you use it"
is not the same massive downside it was 7-8 years ago.

## Changelog
:cl:
del: You can no longer craft explosive lances.
/:cl:

---
## [PKRoma/Terminal](https://github.com/PKRoma/Terminal)@[9ccd6ecd74...](https://github.com/PKRoma/Terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Monday 2022-11-21 09:19:27 by Mike Griese

Manually copy trailing attributes on a resize (#12637)

## THE WHITE WHALE

This is a fairly naive fix for this bug. It's not terribly performant,
but neither is resize in the first place.

When the buffer gets resized, typically we only copy the text up to the
`MeasureRight` point, the last printable char in the row. Then we'd just
use the last char's attributes to fill the remainder of the row.

Instead, this PR changes how reflow behaves when it gets to the end of
the row. After we finish copying text, then manually walk through the
attributes at the end of the row, and copy them over. This ensures that
cells that just have a colored space in them get copied into the new
buffer as well, and we don't just blat the last character's attributes
into the rest of the row. We'll do a similar thing once we get to the
last printable char in the buffer, copying the remaining attributes.

This could DEFINITELY be more performant. I think this current
implementation walks the attrs _on every cell_, then appends the new
attrs to the new ATTR_ROW. That could be optimized by just using the
actual iterator. The copy after the last printable char bit is also
especially bad in this regard. That could likely be a blind copy - I
just wanted to get this into the world.

Finally, we now copy the final attributes to the correct buffer: the new
one.  We used to copy them to the _old_ buffer, which we were about to
destroy.

## Validation

I'll add more gifs in the morning, not enough time to finish spinning a
release Terminal build with this tonight.

Closes #32 🎉🎉🎉🎉🎉🎉🎉🎉🎉
Closes #12567

(cherry picked from commit 855e1360c0ff810decf862f1d90e15b5f49e7bbd)

---
## [linux-kdevops/kdevops](https://github.com/linux-kdevops/kdevops)@[2a5691b870...](https://github.com/linux-kdevops/kdevops/commit/2a5691b870efdf0341ed2fd4e4732bac55294432)
#### Monday 2022-11-21 09:34:31 by Luis Chamberlain

bootlinux: add 9p support

This adds support to build Linux on the host side *once*, and to
then use 9pfs on target libvirt guests to then install the kernel.

The build process with our default guest specs typically takes
about 13 minutes. Build time is now reduced to the time it takes
to build the kernel on your beefy system.

I will note that 'make install modules_install' could be optimized
further upstream on Linux, today is does a stupid loop copying files
one by one.

So the way I see it now after implementing this is we'd add a new
9p mount tag per target code we want to re-share on the host.

I will also note that we're using bus=pcie.0,addr=0x10 and I am
starting to wonder if we'll run out of devices on this bus soon.
I think it should support 16 as its pcie. I set this to depend on
q35 as I'll only b testing this on modern virtualization systems.

For cloud support or to build on beefy remote nodes, not sure what we
should use. Maybe NFS instead?

Signed-off-by: Luis Chamberlain <mcgrof@kernel.org>

---
## [AttackX/AttackX.github.io](https://github.com/AttackX/AttackX.github.io)@[cde3d5c412...](https://github.com/AttackX/AttackX.github.io/commit/cde3d5c412ea5e67e161f25eabdc3ce6c20603f8)
#### Monday 2022-11-21 10:44:54 by kid rendom pulsar

Create skidding.js

if u come from Azari, fuck you.

---
## [jameshih/smoldot](https://github.com/jameshih/smoldot)@[1fb20114ca...](https://github.com/jameshih/smoldot/commit/1fb20114ca7c5d11539dd37ca67adb0556314831)
#### Monday 2022-11-21 13:00:34 by Pierre Krieger

Decode Merkle proofs entirely at once (#3013)

cc https://github.com/paritytech/smoldot/issues/2973

This PR rewrites the code that verifies Merkle proofs. Instead of
iterating through the proof while decoding it to find one specific
element, we now fully decode and verify the proof then later find the
elements from that decoding. This means that we no longer need to verify
the proof multiple times.

In terms of API, this means that decoding the proof no longer returns
any "entry missing" error. The errors about a missing entry have thus
been added at a higher level.

The logic of the code keeps track of all the entries found in the proof.
Later, in order to find an element, we actually iterate "upwards". So
for example to find `0xf00bab`, we first try `0xf00bab`, then for
example `0xf00b` and then `0xf00`. The vast majority of the time there
should be a precise hit, so it seems better to me to try to find
`0xf00bab` first and then iterate upward in order to prove that the
requested key doesn't exist or isn't in the proof.

I've removed the existing code. Despite the fact that it works, I think
it's a strictly worse way of doing it than the code in this PR.

As I've reached the end of this PR and my brain is fried, I realized
that using a `BTreeMap` is kind of stupid since the proof is already a
tree, and we should instead just keep a parallel `Vec` adding some
information that avoids having to recalculate hashes when decoding the
tree. However I don't have the courage to do this anymore and I've just
left a `TODO` instead. Since this is purely an implementation detail and
that the complexity would remain the same, it can be changed later
without breaking anything.

I also had in mind to immediately add a `next_key` and a `prefix_key`
function to the proof, but again I don't have the courage to do so now.

Co-authored-by: mergify[bot] <37929162+mergify[bot]@users.noreply.github.com>

---
## [interactions-py/library](https://github.com/interactions-py/library)@[e527a7d034...](https://github.com/interactions-py/library/commit/e527a7d034f93781d2739a380a1c87c089fdf572)
#### Monday 2022-11-21 15:46:30 by EdVraz

feat(channel): Add new overwrite helper methods (#1173)

* fix: edge case

* refactor: move import

* guys I don't recommend coding when you're sick

* do stuff

* omg what the fuck did i code yesterday

* fix: simplify code

* feat: add another helper method

* Update channel.py

---
## [0x5066/DeClassified](https://github.com/0x5066/DeClassified)@[d07a8d2a5b...](https://github.com/0x5066/DeClassified/commit/d07a8d2a5b33f76bd7fcc9532f27f9ca53d4281f)
#### Monday 2022-11-21 15:46:55 by Eris Lund

of course this occurs *now*

i fucking forgot to update the _noiso variant of eq_layers.m and i hate myself for that

---
## [Yoast/wordpress-seo](https://github.com/Yoast/wordpress-seo)@[4766d0821a...](https://github.com/Yoast/wordpress-seo/commit/4766d0821ab502a98d766f8b3e9a63158c69553b)
#### Monday 2022-11-21 15:48:51 by jrfnl

Surfaces\Values\Meta: fix dynamic property setting in magic methods

The magic `Surfaces\Values\Meta::__get()` method was creating dynamic properties on the class, where dynamic properties are properties not declared on the class which subsequently created on the fly as `public` properties.

As of PHP 8.2, creating dynamic properties is deprecated.

This commit fixes this by:
* Declaring a `private` `$properties_bin` array property to the class.
* Adjusting the magic `__get()` method to save the values for the properties in the `$properties_bin` instead of dynamically creating properties.
* Adjusting the magic `__get()` method to take values previously saved to the `$properties_bin` into account.
* Adjusting the magic `__isset()` method to also look in the `$properties_bin` when determining whether a property is set or not.
* Forbidding setting and unsetting properties other than the declared ones and those supported via the magic `__get()` method by adding new magic `__set()` and `__unset()` methods which will throw an exception.

Note: this does mean to access these properties once set, the magic `__get()` method will now always be called, where previously it would be bypassed. This may have a very very tiny impact on performance.

Also note that there are a few caveats/changes in behaviour:
* Setting dynamic properties on the class is now forbidden, not just for the above case, but in all cases. Previously dynamic properties could still be assigned to the class.
* The class is not `final` and potential child classes and (inaccessible) properties of those are not taken into account in the magic `__get()` method.
    We did do some extensive searches to check if the class _is_ being extended and those searches didn't yield any usable results.

What hasn't changed: access to the already declared `protected` properties from outside the class was previously not supported via the magic methods and is still not supported.

Includes tests for the new `__set()` and `__unset()` methods and a safeguard that the magic `__get()` method does not return the values for `protected` or `private` properties.

---
Internal: if anyone is wondering why this implementation was chosen:
- Hard declaring the properties would be maintenance unfriendly and error-prone as each of the properties would need to be `unset()` in the class constructor as otherwise the magic methods would not be triggered to lazily set the value for the property.
    It would also mean that "sets" and "unsets" cannot be blocked as once the property is declared/initialized, the magic methods are bypassed.
    I.e. the constructor would need to be updated every time a property would be added/removed, but only for the properties supported by magic, which means that the cognitive load when updating the class would also increase.
- Now, you may wonder "why not declare these properties anyway, but make them `private` and not bother with the `unset()` ?" Good question, but access to `private` properties from within the class does not go via the magic methods _unless_ the property is _unset_.
- We also discussed having initial `null` values for all supported properties in the `$properties_bin`, which would then effectively function as an "allow list" for the properties supported by the magic methods.
    We decided against that as a) that would give a special meaning to a `null` value, which means that if the "lazy initialization" would result in a `null` value, the lazy initialization could no longer be short-circuited and b) this would again cause maintenance overhead making it error prone.
---

Tests for the real functionality of the preexisting `__get()` and `__isset()` methods should be added by the team at a later date.

---
## [MinamiKitsune/mpv](https://github.com/MinamiKitsune/mpv)@[6f7506b660...](https://github.com/MinamiKitsune/mpv/commit/6f7506b660b83a44535eceb12a8b9c4de6c0eb36)
#### Monday 2022-11-21 17:02:41 by Philip Langdale

f_hwtransfer: get rid of the shit list

A few years ago, wm4 got sufficiently annoyed with how vaapi image
format support was being discovered that he flipped the table and
introduced the shit list (which just included vaapi) to hard-code the
set of supported formats.

While that might have been necessary at the time, I haven't been able
to find a situation where the true list of supported formats was unsafe
to use. We filter down the list based on what the vo reports - and the
vo is already doing a thorough testing of formats, and if a format
makes it through that gauntlet, it does actually work.

Interestingly, as far as I can tell, the hwdec_vaapi probing code was
already good enough at the time (also written by wm4), so perhaps the
key difference here is that the driver side of things has improved.

I dug into this because of the support for the 422/444 high bit depth
vaapi formats I added to ffmpeg. These are obviously not in the hard
coded list today, but they work fine.

Finally, although it's positioned as a vaapi thing, it's really just
Intel specific, as the AMD vaapi driver has never exposed support for
anything except the formats used by the decoder/encoder profiles.

---
## [igorescodro/alkaa](https://github.com/igorescodro/alkaa)@[27c3f275c8...](https://github.com/igorescodro/alkaa/commit/27c3f275c864ce8d4e3d8d150a62b267c6c85c44)
#### Monday 2022-11-21 18:27:46 by Igor Escodro

♻️ Refactor the NavGraph for better readability

I want to update all the navigation to be inside the same graph, similar
to the "Now in Android" app. However, my experience with that is pretty
annoying. For now, a simple refactor to break the graphs internally and
make it better to read is enough.

---
## [Metastruct/garrysmod-chatsounds](https://github.com/Metastruct/garrysmod-chatsounds)@[35dee955a9...](https://github.com/Metastruct/garrysmod-chatsounds/commit/35dee955a9ae01494db3c127d7e83b653d479e32)
#### Monday 2022-11-21 18:43:28 by Mike

10 years in the joint made you a fuckin pussy

fuck you

---
## [willior/Action_RPG_1](https://github.com/willior/Action_RPG_1)@[36abde6e7e...](https://github.com/willior/Action_RPG_1/commit/36abde6e7e2dfc5da1d889ade2e9dbedccf58b49)
#### Monday 2022-11-21 18:58:11 by willior

re-integrating Formulas

there are lots of problems to solve, but i'm trying to re-integrate the primary functionality of formulas right now.
one thing to consider is how, currently, Formulas are instantiated only by the Player. there is no way, currently, for Formulas to be instantiated by enemies, for example. so i'm trying to expand the scaleability of formulas so that in the future, they can be instanced from anywhere else in the code. if an instanced formula doesn't have its player variable set, it won't be able to calculate spell_mod (magic modifier based on magic attribute) nor formula_level_mod (magic modifier based on the formula level). these 2 variables affect different formulas' parameters, depending on the formula.
i'm thinking ahead a little bit right now because we don't have enemies that can cast formulas yet. but i assume the way it will work is that enemies who can cast formulas will have hard-coded values for these variables which can be grabbed when they decide to cast a formula.
what this will allow is the possibility for different enemies to cast the same formulas, but have those formulas' potency values changed depending on the enemy casting it. take the Lightning Strike formula, for example: it uses spell_mod as a damage modifier, and formula_level_mod to determine the number of strikes. theoretically, we can design a system that will allow different enemies to cast different Lightning Strikes: eg., one might cast it with a low spell_mod, but with multiple strikes. another might cast it with a high spell_mod, but it only ever strikes once, etc.
of course, this system will also need a way to determine collision, which shouldn't be too hard. we can even write a global function to determine Formula behaviour, something like:
Global.initialize_formula(caster), where "caster" is a reference to the body casting it.
we check if caster is a Player, and if it is, we set the Formula's player variable, which will instance a FormulaTargetScreen.
if caster is a Player, we set the formula's Hitbox collision layer to PlayerHitbox, and its mask to EnemyHurtbox; if caster is an enemy, the formula's Hitbox collision layer should get set to EnemyHitbox and its mask to PlayerHurtbox. the hurtbox_entered() methods for both Players & Enemies will probably need to be re-configured to be more rigid. right now, they have pretty different functionality. eg., the Player's hurtbox_entered() method isn't exactly set up to get hit by damage formulas, since there are no damage formulas that damage the player, yet.
more thought might need to be put into designing a rigid system. for example, things like bushes/grass have the PlayerHitbox mask; so if a bush's Hurtbox detects an area on the PlayerHitbox collision layer, it emits the area_entered signal and calls its function (which plays the cut animation). perhaps, instead of simply detecting which layer a monitored area is on, we can look at the area's damage_type. for example, one way of doing things would be to check if area.get("damage_type") == 1, aka it's a physical slash-type damage, and only run the code based on that condition. doing it this way, it's possible to set a number of different conditions. for example, if area.get("element") == FIRE, burn the bush instead of cutting it. that's just one example.
i've gotten rid of the Exit collision layer since i don't think it was being used. Exits detect Player Bodies, then run the Scene Change code - Players don't have to detect Exits. so they don't need their own collision layer.
for now, i've changed it to FormulaHitbox as i'm experimenting with different ways we can determine how & who a formula targets. there are a lot of factors to take into account. but, for starters - and to keep things relatively simple - let's try and go with the following: an instanced Formula can only target EITHER Players OR Enemies; not both. so no friendly fire, or getting damage by your own AoE. also, no healing enemies with your own heal spells, and vice versa.
so, in summary, when a Formula is instantiated, depending on what instantiated it (ie. either a Player or an Enemy), it configures its collision layers/masks accordingly.
one thing to keep in mind is the Charm mechanic: Charmed enemies should be able to be hit by both enemies AND players. but they shouldn't be able to be healed by players. this might pose a problem, but we'll figure it out when we get there.
since we've changed the order & number of the collision layers, the Charm status is currently broken, but will fix that in next commit. Godot 4 was crashing every time i typed "set_collision_mask_value" in Enemy_Class.gd.

---
## [Huffie56/cmss13](https://github.com/Huffie56/cmss13)@[ca2114f0f5...](https://github.com/Huffie56/cmss13/commit/ca2114f0f56ab4a51443bdac52053ead327724dc)
#### Monday 2022-11-21 20:32:51 by Mister-moon1

Removes some useless code from welding helmet (#1363)

* fuck you useless code

* you cannot hide, useless code

---
## [danieljharvey/mimsa](https://github.com/danieljharvey/mimsa)@[2cdf13d80c...](https://github.com/danieljharvey/mimsa/commit/2cdf13d80c070f8e0677e0736954b7a0279a8484)
#### Monday 2022-11-21 21:19:22 by Daniel Harvey

Add tuples (#826)

* Oh my god this is boring

* Fix GHC options

* Bin off

* Format

* Now fix all the type errors in the tests and cry

* WIP fix tests

* Well, shit, these pass

* WIP

* Well, well, well

* Yeah

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[d0e1ac9118...](https://github.com/treckstar/yolo-octo-hipster/commit/d0e1ac9118e854f1eac3ea59429efdae628f5edf)
#### Monday 2022-11-21 22:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [ammarfaizi2/linux-fork](https://github.com/ammarfaizi2/linux-fork)@[fb032319b1...](https://github.com/ammarfaizi2/linux-fork/commit/fb032319b103b57db657697231b491f5cd4fc8df)
#### Monday 2022-11-21 23:16:09 by Johannes Weiner

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

---

