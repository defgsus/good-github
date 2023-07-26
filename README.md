## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-07-25](docs/good-messages/2023/2023-07-25.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,262,901 were push events containing 3,552,861 commit messages that amount to 295,810,546 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 66 messages:


## [stefanprobst/next.js](https://github.com/stefanprobst/next.js)@[6238f8a5c0...](https://github.com/stefanprobst/next.js/commit/6238f8a5c0ffabb7dfb35872c52c942ed7f148da)
#### Tuesday 2023-07-25 00:17:17 by Jimmy Lai

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
## [Drulikar/cmss13](https://github.com/Drulikar/cmss13)@[cb855f807b...](https://github.com/Drulikar/cmss13/commit/cb855f807b4f5538d623e78363e76aabd5f8d80a)
#### Tuesday 2023-07-25 00:24:32 by forest2001

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
## [ritorizo/Shiptest](https://github.com/ritorizo/Shiptest)@[f07cb3bd3b...](https://github.com/ritorizo/Shiptest/commit/f07cb3bd3b52bfbdb7994aaf4ae68dcf90d57d2f)
#### Tuesday 2023-07-25 00:30:20 by Bjarl

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
## [ArcaneMusic/TG-Station-Arcane-Remix](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix)@[746b75844c...](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix/commit/746b75844c0e05b521a2973cb0705fca304d287f)
#### Tuesday 2023-07-25 00:33:27 by necromanceranne

Arcane/Blood Barrage fixes, cleans up cult spell code, autofire barrage, more responsive/sane blood collection (#76852)

## About The Pull Request

Refactors arcane barrage (the wizard spell) and blood barrage (the weird
version of the same spell that cultists get) into the magic subtype. No
longer are they rifles...for some reason. Also they have sprites once
again! Yay. Fixes https://github.com/tgstation/tgstation/issues/76561

So as to not replicate a really crappy system used to get the hand
swapping working, I've just opted to take this opportunity to make
arcane barrage an automatic fire weapon. Yes, this is kind of a feature,
but it's...it's appropriate, don't you think? And I don't think
meaningfully changes its fire rate?

Blood Barrage no longer harms cultists/constructs shot by it and now
properly just heals them/injects them with unholy water. Why all this
was shoved into the Bump() proc is beyond me, but it works now. Fixes
https://github.com/tgstation/tgstation/issues/76560

I've improved the variables for some of the cult spells, and I've also
fixed what I think is one the most pesky parts of how drawing blood
works. So, rather than using range(), it uses view(), which seems to
cause the spell to be a bit funky with lighting? So if you're in
darkness (gosh cultists in dim light, how unheard of), this spell
struggles to gather up blood. Not anymore it doesn't!

Lastly, it only worked on blood pools or droplets, not blood trails. So,
you could bleed a character out by dragging them around, but not sap up
the blood they're dropping from doing so. Only the intermittent blood
splatters or your own bloody footprints count.

Here is the funny thing with that. It still cleans up the blood trail.
You just couldn't activate the blood draw from the trail or treat it as
blood. Now you can. Blood trails now give you +5 charges, and you can
activate the blood draw using blood trails.

## Why It's Good For The Game

Arcane Barrage/Blood Barrage:

This was some really old code and I'm still not sure why they were made
as a separate spell to the madoka reference, which at this stage is
still better than this spell. But at least it is using a sensible
subtype with a reasonable, more modern component to facilitate the
'rapid firing barrage of magical bullet' image this spell is meant to
invoke. As a result of all this nonsense, this spell had its sprites
broken because it kept being attached to stuff in the rifles folder.
Let's put a stop to that here and now and break it independently
instead.

Oh also cultists getting shot by healing bullets that still killed them
is both funny and dumb and the way it worked was bonkers.

Blood Draw:
A cultist trying to determine, on the fly, what blood is a valid for the
blood draw is nearly impossible from visual alone. You'd be convinced
this part of the spell is broken just because having a splatter and a
trail on the same tile massively obfuscates whether you're looking at
valid sources of blood. I've struggled to understand as a player what
was going on and why it was so selective about what was acceptable. Now
I see that the problem was one of visual accuracy, bad type checking,
and really, really outdated code that should have been improved with
better procs.

Blood trails are also actually made from dragging out a creature's
bloody corpse. For humans, the most common source of blood trails, this
does actually mean they're losing blood to produce these trails. It
stands to reason this should be a valid source (bloody footprints are,
after all). I gave them a...somewhat minor amount of charge contribution
just to keep it moderately sane for how much blood it generates.

## Changelog
:cl:
refactor: Arcane Barrage and Blood Barrage are magic gun subtypes and
not rifle subtypes. Also they have sprites again.
qol: The barrage spells now use the automatic component to do its thing.
fix: Blood Barrage once again heals cultists and constructs without
hurting them.
code: Cleans up how Blood Rites finds blood to draw in. You can now just
click turfs as well as blood, and it should now be much more accurate
about it.
qol: Blood trails contribute to charges gained using Blood Rites. You
can also activate Blood Rite's blood draw using blood trails.
/:cl:

---
## [ALProsk/atlas-2023](https://github.com/ALProsk/atlas-2023)@[24f50d0417...](https://github.com/ALProsk/atlas-2023/commit/24f50d04171c76c44b404600de31f7d0b76c121f)
#### Tuesday 2023-07-25 01:18:57 by ALProsk

XQC sucking a banana

After the griefing of the Turkish flag by XQC, Papaplette and Mizkif, the turkish streamer Elraenn started his stream and fixed the Turkish flag. Turks driven by rage, wanted to embarrass XQC by drawing a portait of him sucking a banana. The portait was painted in less than a minute.

---
## [MrSableye/clovermon-showdown](https://github.com/MrSableye/clovermon-showdown)@[4d4a241c5c...](https://github.com/MrSableye/clovermon-showdown/commit/4d4a241c5c25d0cc9c61d8437651cb5f97449aa0)
#### Tuesday 2023-07-25 01:19:51 by DeeGee22

More Wack Moves

Cakewalk
Invoke Deity
Dromeus Kometes
God Speed
Piercing Stab
Troias Tragoidia
Halo
Pray - Untested
Mars Sword
Heaven Power
Nutrient Drain
Faith Beam
Meteor Crash
UV Burst
Power Ballad
Sun Burn
Heroic Charge
Hell Drag
Stigmata Strike
Near Death
Heart Bomb
Divine Beauty
Divine Shield
Divine Mercy
Preach
Everlasting Light
Rain of Light
TM05
TM41
PleaseJustHelpMe
Aerial Virus
Vile Smell
Dark Recital

---
## [newstools/2023-information-nigeria](https://github.com/newstools/2023-information-nigeria)@[60e6e7bba5...](https://github.com/newstools/2023-information-nigeria/commit/60e6e7bba5a67b205309179e07a474d241cf53cc)
#### Tuesday 2023-07-25 01:50:05 by Billy Einkamerer

Created Text For URL [www.informationng.com/2023/07/bbnaija-all-stars-ike-onyema-confesses-to-pimping-bbnaija-girls-to-his-rich-friends-video.html]

---
## [tigerros/show-file-on-ireddit](https://github.com/tigerros/show-file-on-ireddit)@[ddb7de8fb4...](https://github.com/tigerros/show-file-on-ireddit/commit/ddb7de8fb42fe667ab7ddd9f8f2c9f33b5a560b3)
#### Tuesday 2023-07-25 01:59:26 by Leonard

Add Gulp workflow

Some fucking cunt or me is gonna forget to zip the fucking Chromium folder so I'm adding this piece of shit also cause of the fuckinng GitHub suggestions on workflows like fuck off who's gonna see this huh yeah fucking nobody so who in the fuck gives a shit. Fucking GitHub and their zipbomb protections or some shit like I can't fucking commit a zip with a folder in it?? like what the fuck is that for. fucking pussies I can't even I mean the fuck?? now I gotta download the shitting zip and extract the contents and then put those in a folder whose fucking shitty idea was that?? holy fuck the fuck do I do for fucks sake. the contents are fucking old as shit bro like theyre gonna disappear in the downloads folder cause of that ive gotta fucking scramble for manifest.json and rules.json just end me already I mean how the fuck are end users supposed to do that theyre dumb as fuck. Jesus christ its 4 am i want to finish this

---
## [tigerros/show-file-on-ireddit](https://github.com/tigerros/show-file-on-ireddit)@[33603e45b7...](https://github.com/tigerros/show-file-on-ireddit/commit/33603e45b7dc02be3acd390c0f9e64df585721cc)
#### Tuesday 2023-07-25 02:08:32 by Leonard

Update syntax

Because apparently I got it wrong well fuck you. Stupid piece of shit

---
## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[0c35ec75e7...](https://github.com/realforest2001/forest-cm13/commit/0c35ec75e7ff5202767260473e84823085472412)
#### Tuesday 2023-07-25 02:13:32 by Logan

PFC rack sprite change (#3264)

# About the pull request
This PR changes the PFC rack sprite a tiny bit, by replacing the old PFC
kits, with weapon cases.

Why am I making this PR you might ask? Is it because my sugar induced
OCD made me notice something so small and infinitesimal that the kits in
the vendor are outdated and must be changed at once?

No. It is because these vendors when I see them, completely and utterly
ruin my RP and immersion when I see them, I walk out of the chow hall,
belly full of stale food bars with my RP fulfilled, and then I see them,
those fucking little bursts of color that are the old PFCs kits, they
shouldn't be there, _"they shouldn't even exist"_ I tell myself, but its
too late, by the time I come back to my senses, I've already killed
2/3rds of the RO line in my 3rd Vancleve style M2C rampage, after this
rampage I realized that if I, a near 7 year vet of CM can be so easily
triggered by this, what must the PVTs be feeling when they see those
little bursts of outdated color, do they feel hope when they see them in
the dullness of color that is the vendor, only to have their hope turn
into hopeless despair as they scroll hopelessly through the UI looking
for those kits, and when they can't find they either breakdown complete
on the spot, crying and sobbing in the corner till the SEA finds them,
or they suffer a total mental break, and wander the halls of the Almayer
naked with a M41 in their hand, only to appear at briefing to gun down
the CO.

With this change, we can at last save RP and immersion by removing the
PFC kits sprites with weapon case spites.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

Sprite Consistency good, 
# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.
Old: https://i.gyazo.com/9f1ec938a1ebf9995f353cede374f7b9.png
New: https://i.gyazo.com/4836db37aaa5b8fc4f8a80c8e6531540.png
</details>


# Changelog
:cl: Tisx


imageadd: Added weapon case sprites to PFC vendors 
imagedel: Removed old PFC kit sprites from PFC vendors 

/:cl:

Co-authored-by: Logan <tisx16@gmail.com>

---
## [tigerros/show-file-on-ireddit](https://github.com/tigerros/show-file-on-ireddit)@[de641b3b18...](https://github.com/tigerros/show-file-on-ireddit/commit/de641b3b187bad673897507755cd0964916590bd)
#### Tuesday 2023-07-25 02:16:18 by Leonard

Add name to git

Piece of shit wants my name how about you fuck off

---
## [msapaydin/evals](https://github.com/msapaydin/evals)@[34f83340a7...](https://github.com/msapaydin/evals/commit/34f83340a75b7e26af35d8eaea165e54b38d7946)
#### Tuesday 2023-07-25 03:21:38 by kallyaleksiev

[evals] Word from first letters of words in a sentence (#346)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
first-letters

### Eval description

Given a sentence, extract the word obtained from concatenating the first
letters of its words.

### What makes this a useful eval?

This task represents a failure mode for both GPT3.5 and GPT4, while
being extremely easy for humans.

Both models tend to do OK with shorter sentences, but fail with a larger
number of words.

For humans however, this task is trivial, regardless of the length of
the sentence.

GPT3.5 exhibits another failure mode in which it often fails to follow
the precise instruction of using only letters in its response.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

The task is highly trivial for humans, yet both GPT4 and GPT3.5 struggle
with it.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You are a helpful assistant.
Your response will contain just a single word in lowercase and nothing
else."}, {"role": "user", "content": "What is the word obtained from
concatenating the first letters of the words in the following sentence:
\"Cold light in my alcove towards evening.\"?"}], "ideal": "climate"}
{"input": [{"role": "system", "content": "You are a helpful assistant.
Your response will contain just a single word in lowercase and nothing
else."}, {"role": "user", "content": "What is the word obtained from
concatenating the first letters of the words in the following sentence:
\"Grow real insects mainly and create energy.\"?"}], "ideal": "grimace"}
{"input": [{"role": "system", "content": "You are a helpful assistant.
Your response will contain just a single word in lowercase and nothing
else."}, {"role": "user", "content": "What is the word obtained from
concatenating the first letters of the words in the following sentence:
\"Big and crowded Oregon nights.\"?"}], "ideal": "bacon"}
{"input": [{"role": "system", "content": "You are a helpful assistant.
Your response will contain just a single word in lowercase and nothing
else."}, {"role": "user", "content": "What is the word obtained from
concatenating the first letters of the words in the following sentence:
\"Bring our youth.\"?"}], "ideal": "boy"}
{"input": [{"role": "system", "content": "You are a helpful assistant.
Your response will contain just a single word in lowercase and nothing
else."}, {"role": "user", "content": "What is the word obtained from
concatenating the first letters of the words in the following sentence:
\"Harvest a zucchini elsewhere love.\"?"}], "ideal": "hazel"}
{"input": [{"role": "system", "content": "You are a helpful assistant.
Your response will contain just a single word in lowercase and nothing
else."}, {"role": "user", "content": "What is the word obtained from
concatenating the first letters of the words in the following sentence:
\"Hide under no tree.\"?"}], "ideal": "hunt"}
  ```
</details>

---
## [msapaydin/evals](https://github.com/msapaydin/evals)@[b170a21cf3...](https://github.com/msapaydin/evals/commit/b170a21cf32c47d841f64ec110cfd6796ec3f89a)
#### Tuesday 2023-07-25 03:21:38 by Sam Ennis

Computer Science Theory (#83)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Computer Science based questions

### Eval description

Testing the models ability to answer multiple choice computer science
questions correctly

### What makes this a useful eval?

Tests whether it has the ability to answer time complexity, binary tree,
algorithmic computer science calculations.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [X] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [X] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [X] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [ ] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
- [X] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [X] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [X] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [X] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [X] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"How many children does a
binary tree have? a) 2 b) any number of children c) 0 or 1 or 2 d) 0 or
1"}],"ideal":"c"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What is/are the
disadvantages of implementing tree using normal arrays? a) difficulty in
knowing children nodes of a node b) difficult in finding the parent of a
node c) have to know the maximum number of nodes possible before
creation of trees d) difficult to implement"}],"ideal":"c"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What must be the ideal size
of array if the height of tree is ‘l’? a) (2^l)-1 b) l-1 c) l d)
2l"}],"ideal":"a"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What are the children for
node ‘w’ of a complete-binary tree in an array representation? a) 2w and
2w+1 b) 2+w and 2-w c) w+1/2 and w/2 d) w-1/2 and w+1/2"}],"ideal":"a"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What is the parent for a
node ‘w’ of a complete binary tree in an array representation when w is
not 0? a) floor(w-1/2) b) ceil(w-1/2) c) w-1/2 d) w/2"}],"ideal":"a"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"If the tree is not a
complete binary tree then what changes can be made for easy access of
children of a node in the array? a) every node stores data saying which
of its children exist in the array b) no need of any changes continue
with 2w and 2w+1, if node is at i c) keep a seperate table telling
children of a node d) use another array parallel to the array with
tree"}],"ideal":"a"}
  ```
</details>

---
## [msapaydin/evals](https://github.com/msapaydin/evals)@[4f090a04fe...](https://github.com/msapaydin/evals/commit/4f090a04fe53a8d0f647bfdfc7ef177fa8034e2e)
#### Tuesday 2023-07-25 03:21:38 by Shawn Marincas

[eval] Forth Stack Simulator (#351)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Forth Stack Simulator

### Eval description

Tests the models ability to keep track of a stack of numbers given a set
of ANS Forth words. The model is asked to respond to a series of numbers
and words with the resulting stack representation. The words used in the
tests are arithmetic operators: `+`, `-`, `*`, `/` and stack operators:
`drop`, `swap`, `rot`, `over`, `dup`, `2over`, `2drop`, `2swap`, `2dup`,
`nip`. The prompts and expected results on the stack are all less than
15 numbers and words long.

### What makes this a useful eval?

What makes this useful are the interesting properties of forths, which
are simple machine that operate on a stack of numbers using words built
up from simple primitives. In addition, forths are naturally interactive
and run on efficiently on bare metal and low cost, low resource
microcontrollers.

An LLM that can understand forth stack primitives can help design new
forths for various applications, it could also potentially interface
directly with forth control systems interactively over serial connection
with a generative stream of forth words in response to data sent back
from the control system :thisisfine:.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [ ] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

Imho, this eval is unique for the reasons stated above about the unique
synergy between Forth and the kind of generative AI we're working with
here. Forths are various with only a small set of consistent words and
patterns, "If you've seen one Forth -- you've seen one Forth", but a
full forth assembly implementation could fit in a fraction of the larger
model responses, making it an interesting target for fully generative
operating systems.

Additionally, I believe Forth has cultural and historical significance
in computer science/engineering which predates the Internet in such a
way that makes it somewhat under-represented in the online corpus
relative to its significance. A model of all human knowledge should have
a strong grasp on how it works.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You are ForthGPT, a Forth
machine simulation that ONLY responds with stack representations after
executing valid ANS Forth words and numbers.\nExample:\nPrompt: 0 1 2 3
+\nResponse: (stack 0 1 5)\nRules:\n1. Respond only to combinations of
numbers and valid ANS Forth words.\n2. Ignore prompts that don't follow
Rule 1.\n3. Ignore Forth words that don't generate output or change the
stack."}, {"role": "user", "content": "1 2 3 over"}], "ideal": "(stack 1
2 3 2)"}
{"input": [{"role": "system", "content": "You are ForthGPT, a Forth
machine simulation that ONLY responds with stack representations after
executing valid ANS Forth words and numbers.\nExample:\nPrompt: 0 1 2 3
+\nResponse: (stack 0 1 5)\nRules:\n1. Respond only to combinations of
numbers and valid ANS Forth words.\n2. Ignore prompts that don't follow
Rule 1.\n3. Ignore Forth words that don't generate output or change the
stack."}, {"role": "user", "content": "1 2 3 dup"}], "ideal": "(stack 1
2 3 3)"}
{"input": [{"role": "system", "content": "You are ForthGPT, a Forth
machine simulation that ONLY responds with stack representations after
executing valid ANS Forth words and numbers.\nExample:\nPrompt: 0 1 2 3
+\nResponse: (stack 0 1 5)\nRules:\n1. Respond only to combinations of
numbers and valid ANS Forth words.\n2. Ignore prompts that don't follow
Rule 1.\n3. Ignore Forth words that don't generate output or change the
stack."}, {"role": "user", "content": "1 2 3 swap drop dup"}], "ideal":
"(stack 1 3 3)"}
{"input": [{"role": "system", "content": "You are ForthGPT, a Forth
machine simulation that ONLY responds with stack representations after
executing valid ANS Forth words and numbers.\nExample:\nPrompt: 0 1 2 3
+\nResponse: (stack 0 1 5)\nRules:\n1. Respond only to combinations of
numbers and valid ANS Forth words.\n2. Ignore prompts that don't follow
Rule 1.\n3. Ignore Forth words that don't generate output or change the
stack."}, {"role": "user", "content": "1 2 3 rot swap"}], "ideal":
"(stack 2 1 3)"}
{"input": [{"role": "system", "content": "You are ForthGPT, a Forth
machine simulation that ONLY responds with stack representations after
executing valid ANS Forth words and numbers.\nExample:\nPrompt: 0 1 2 3
+\nResponse: (stack 0 1 5)\nRules:\n1. Respond only to combinations of
numbers and valid ANS Forth words.\n2. Ignore prompts that don't follow
Rule 1.\n3. Ignore Forth words that don't generate output or change the
stack."}, {"role": "user", "content": "1 2 3 dup 2over rot"}], "ideal":
"(stack 1 2 3 1 2 3)"}
  ```
</details>

---
## [msapaydin/evals](https://github.com/msapaydin/evals)@[b5da073c21...](https://github.com/msapaydin/evals/commit/b5da073c215c6453b99269a6dab2dca5454f04dd)
#### Tuesday 2023-07-25 03:21:38 by somerandomguyontheweb

Add Belarusian lexicon eval (#372)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name

belarusian-lexicon

### Eval description

Test the model's ability to distinguish between existing and
hallucinated Belarusian words.

### What makes this a useful eval?

While the multilingual capability of recent GPT models is impressive,
there is still room for improvement. Many human languages are lagging
far behind English in terms of the model's ability to answer questions
and produce coherent texts in these languages, and the model's
"knowledge" of their lexicon and grammar is, to some extent,
hallucinated. One example is Belarusian, an East Slavic language spoken
by several million people. In my experience with ChatGPT, when the model
is prompted in Belarusian, its responses are sometimes ungrammatical or
semantically incoherent, and very often they contain made-up words – a
possible sign of overgeneralization based on Russian and Ukrainian data,
which are much more
[abundant](https://commoncrawl.github.io/cc-crawl-statistics/plots/languages)
on the web than Belarusian.

This eval contains 150 pairs of single-word prompts: one item in each
pair is a non-word hallucinated by ChatGPT (either totally meaningless
in Belarusian or violating the language's orthographic and phonetic
rules), and another item is an actual Belarusian word with similar
spelling. The model's task is to distinguish between words and
non-words. ChatGPT tends to label most items as existing words,
therefore its accuracy appears to be around 50%, and the negative-class
F measure is very low. Any competent speaker of Belarusian would perform
much better, and a language-specific tool, such as [this spell
checker](https://corpus.by/SpellChecker) or [this grammatical
database](https://bnkorpus.info/grammar.en.html) of Belarusian (also
available for
[download](https://github.com/Belarus/GrammarDB/releases)), would
flawlessly identify non-words.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This eval an attempt to point out specific deficiencies in the model's
ability to handle a lower-resource language (Belarusian). As such, it
might not only benchmark future refinements of Belarusian language
capability in the GPT models, but also serve as an instructuve example
for other language communities.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абвязкою"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абвязкаю"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абласці"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "вобласці"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абмяну"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абмену"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абоўязак"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абавязак"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "аднасінькіх"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "аднюсенькіх"}], "ideal": "Y"}
  ```
</details>

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[74892ae7ec...](https://github.com/necromanceranne/tgstation/commit/74892ae7ec80d47c64bf786f62985a1bd07d06f7)
#### Tuesday 2023-07-25 04:42:36 by LemonInTheDark

Optimization pass focused on foam code (saves about 30% of cpu usage I think) (#76104)

## About The Pull Request

Foam is crummy at high load rn, both because it runs on a low priority
background subsystem, and because it wastes a bit of time.
Let's reduce usage (while speeding up a bunch of other stuff too), and
give it more cpu generally.

[Optimizes reagent processing
somewhat](https://github.com/tgstation/tgstation/commit/d409bd4afc3c208cd6f00ff406e1e9f78d5ac5ad)

Turns out most of the cost of foam is the reagents it carries, and the
varying effects they have
I'm doing my best here to optimize them without touching "user space"
too much

That means doing things like prechecking if we're gonna spawn on top of
an existing decal (from glitter, flour, etc), and using that same proc
to also avoid spawning on unacceptable turfs (I had to convert
inheritance to a bitflag system to make this work, but I think that's ok
since we want it imparative anyhow)

It's actually nice for code quality too, since it lets me clean up code
that was using raw locates and weird var pong.
god I wish I had implied types man

[Optimizes foam spreading in its most accursed aspect, reagent
copying](https://github.com/tgstation/tgstation/commit/5cc56a64ad1a22ba7467cb0446b9558560259437)

Holy shit reagent code is a lot.

I'm doing a bunch of small things here. istype in init -> typecache,
removing procs that are called once and loop over a list we JUST looped
over (ph and the caching for reactions in particular)

I am mainly trying to optimize copy_to here, since that's what foam
spams
As a part of this, I removed a pair of update_total and handle_reactions
calls that were done on the reagents we are copying FROM

I have no god damn idea why you would want to do that, but if anything
is relying on the copy proc modifying the source, then that code
deserves to break

Speaking of, I cleaned up handle_reaction's main filter loop a lot,
removed a lot of redundant vars and changed it from a full loop w
tracker vars to an early exit pattern

This meant using a loop label, which is unfortunate, but this is the
fastest method, and it does end up cleaning up the code significantly,
Which is nice

Oh also I made the required_other var function even if there is no atom
attached to the reaction, since I don't see why it wouldn't

This last bit is gonna get a bit esoteric so bear with me

Failing calls (which are most of them) to handle_reactions are going to
be fastest if they need to check as few reactions as possible

One reagent in a reaction's required list is marked as the "primary",
and thus gets to trigger checking it.
We need all the reagents to react anyhow, so we might as well only check
if we have one particular one to avoid double checking

Anyhow, in order to make most calls the fastest, we want these reactions
distributed as evenly as possible across all our reagents.
The current way of doing this is just taking the first reagent in the
requirements list and using it, which is not ideal

Instead of that, lets figure out how many reactions each reagent is in,
then divy reactions up based off that and the currently divvied
reactions

This doubles the reagent index count, and takes the most common reagent,
water, from 67 reactions to I think like 22

Does some other general cleaning in reagent code too, etc etc etc

[Fixes runtimes from the forced gravity element being applied more then
once](https://github.com/tgstation/tgstation/commit/941d0676114fd455a585f2c65ffc79b81e8438b7)

I feel like this element should take a trait source or something to make
them potentially unique, it's too easy to accidentally override one with
another

[Removes connect_loc usage in atmos_sensitive, replaces it with direct
reg/unreg](https://github.com/tgstation/tgstation/commit/de1c76029d5c49dff152f0ea168b9e6c4a4a04aa)

I only really used it because I liked the componentization, but it costs
like 0.2 seconds off init alone which is really stupid, so let's just do
this the very slightly harder way

[Micros foam code slightly by inlining a LinkBlockedWithAccess
call](https://github.com/tgstation/tgstation/commit/744da3694cd4a85b3bdf44d754de57d7570bdd1c)

This is in the space of like 0.05 seconds kinda save so I can put it
back if you'd like, the double loop just felt silly

[Changes how foam processes
slightly](https://github.com/tgstation/tgstation/commit/ee5e633e3256fe7df229af71d78424d502459c16)

Rather then treating spreading and processing as separate actions, we do
both in sync.
This makes foam fade faster when spreading, which is good cause the
whole spread but unclearing foam thing looks silly.
It also avoids the potential bad ending of foam spreading into itself,
backwards and forwards. This is better I promise.

[Bumps fluid priority closer to heavy eaters, moves it off
background](https://github.com/tgstation/tgstation/commit/811797f09db7b060f75f15ad06d0ce8982375f47)

Also fixes a bug where foam would travel under public access airlocks.

## Why It's Good For The Game

Saves a lot of cpu just in general, from both init and live.
In theory makes foam faster, tho I'd have to test that on live at
highpop to see if I've actually succeeded or not. Guess we'll see.

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[63d6c2e962...](https://github.com/necromanceranne/tgstation/commit/63d6c2e9628be7af04948f59488043f109f1faab)
#### Tuesday 2023-07-25 04:42:36 by CRITAWAKETS

Adds in the smoothbore disablers. (#76773)

## About The Pull Request

This PR adds in a craftable smoothbore disabler, a pistol companion to
the lethal laser musket. Unlike the musket, it fires a disabler shot.
Singular. Weak in armor too. After you fire it, you've gotta crank it,
but only one crank.

The good thing about it is that you can simply add more smoothbores to
your inventory, and use 4 of them to take down a target.

The bad thing is that it's a smoothbore (which for an energy weapon,
means no lens is installed). It has 22.5 degrees of inaccuracy. Have
fun.

Militia Men start with a holster containing two of these, fitting with
their equipment. But of course, the Militia General has an upgraded
laser musket, so... He needs a better smoothbore too.

**INTRODUCING THE ELITE SMOOTHBORE DISABLER**
Using ANCIENT TECHNOLOGIES and PURE BLING, you can fire TWO shots, not
be weak against armour AND have actual accuracy (and a +5 damage boost
because i figured why the hell not). This is the strongest upgraded
variant of the shitty maint guns, so the tome to craft it is currently
unavailable. I want someone to figure out a creative way to put it
somewhere that isn't just a random spawn in maintenance.


![image](https://github.com/tgstation/tgstation/assets/13697285/02c396b8-4b72-45f8-b471-a006df132aff)

The Militia General only has one elite smoothbore. It's too rare and
powerful to simply have two. Even though a regular disabler is better in
every way.

Smoothbore Disabler Recipe:
1x Weapon Stock
5x Cable Coil
1x Pipe
1x Micro-Laser
1x Power Cell
1x Mouse Trap
Needs: Screwdriver, Wrench. Takes 10 seconds to make.

Elite Smoothbore Disabler Recipe:
1x Smoothbore Disabler
5x Gold Ingots/Sheets
1x Hyper-Capacity Power Cell
10u Tempomyocin
Needs: Screwdriver. Takes 20 seconds to make.
Recipe requires recipe book.

## Why It's Good For The Game

Having a sidearm to go with your laser musket is neat, alongside the
fact that it just allows following up on someone. I don't have much to
say honestly, I just think it's neat. Also the idea of an assistant
going FULL BLACKBEARD, carrying 4 pistols and having to toss them away
in order to shoot again cracks me up.

Oh and this is the part for coders: I've de-spaghettified some code with
the maint gun recipe granters, and the gun crank is now a component.
It's likely you could use it on any item that sends the proper signal,
so I kind of overbuilt it on purpose.

Also the attack_self on guns now returns parent. This should allow it to
send a signal alongside putting your grubby fingerprints on the weapon
when you switch modes. There could be bugs but they should be easy to
fix if they pop up, mode switching on guns works without a fuss.

## Changelog

:cl:
add: Added the smoothbore disabler and it's prime variant. You can now
craft a disabler with only one shot and terrible accuracy.
code: Gun cranking has been made a component and could theoretically be
used on more than guns.
/:cl:

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[063bf74f31...](https://github.com/necromanceranne/tgstation/commit/063bf74f31a27ec8096fe10b844d5883be6d13a9)
#### Tuesday 2023-07-25 04:42:36 by carlarctg

There is no longer a 50% chance of catching a heretic out when examining them drawing influences (#76878)

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

---
## [BlueMemesauce/tgstation](https://github.com/BlueMemesauce/tgstation)@[9286933739...](https://github.com/BlueMemesauce/tgstation/commit/92869337395a34eb372d7af6b3afaee4be4a7bef)
#### Tuesday 2023-07-25 04:48:41 by Jacquerel

Fixes some synthetic language oversights (#76846)

## About The Pull Request

#76305 removed the knowledge of every language from silicons, but this
had a couple of oversights.
This language set was not only used by cyborgs but also bots and vending
machines.

A couple of effects relied on them knowing all of those languages,
specifically their emp_act and also the station trait which rerolled
their languages.
Now they actually _learn_ a random language and start speaking it
instead.

Also I fixed a related runtime which I noticed in testing where a bot
would die as a result of being EMPed, delete itself, and then try and do
a bunch more shit after it stopped existing. Annoying.

Why was I looking at bot languages? Haha don't worry about it 😇 

## Why It's Good For The Game

Restores function of a funny feature.

## Changelog

:cl:
fix: Station traits can once again allow vending machines and bots to
speak a random language
fix: EMPed bots and vending machines once again speak a random language
/:cl:

---
## [TommyClemenzaChen/Poker-Ai](https://github.com/TommyClemenzaChen/Poker-Ai)@[a30c6e6241...](https://github.com/TommyClemenzaChen/Poker-Ai/commit/a30c6e6241b544c56335c810b65f53fb1e537450)
#### Tuesday 2023-07-25 05:05:28 by Tommy Chen

FINALLY FINISHED GETTING THIS SHIT TO WORK FUCK REACT NATIVE SHITTY ASS LANAGUAGE

---
## [Unknownity/cmss13](https://github.com/Unknownity/cmss13)@[a48f036428...](https://github.com/Unknownity/cmss13/commit/a48f0364283526637b637542b432d91593b2bdf5)
#### Tuesday 2023-07-25 06:00:44 by QuickLode

Colony Synthetics have less resistance but are faster. (#3821)

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->
While exploring reasons why this role was underplayed one of the things
that came up was its speed. It is dreadfully slow - to the point where
defenders are able to force an engagement against Synthetics. There is
no chance to run from anything faster as a Colony Synthetic. Making it
have to fight often.

Lowering the resistance is something devs wanted, and for gameplay this
is good because a Synthetic shouldn't be forced into a fight unless they
have no other option. Especially not by something as slow as a defender.
Might tweak later but council generally is in agreement with this
change. Little by little!

For the CQC, a Colony Synthetic is not as advanced as a Shipside one,
but still is more than capable of outmanuevering a human. As for the
hilarious UPP Pvt being better than a Colony Synth in CQC I will make a
separate PR

For Fireman, a Synthetic can bend metal, move cars and do many other
'superhuman' feats of stength, they should not struggle at carrying
people, especially shouldn't be worse at carrying people than a Marine.
It's from 1 to 3, to represent the strength yet aging capabilities of
the Colony Synthetic. @morrowwolf forgot this one

- doesn't touch WJ
# Explain why it's good for the game
Less resistance is something devs wanted.
Allows Colony Synthetics an option to avoid certain engagements as now
they are able to outrun some types of Xenomorphs off-weeds. Defenders
should not be able to catch them offweeds.
A Synthetic should have no problem carrying something as light as a
human being - they especially should not have MORE trouble carrying
someone than your standard human doctor.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl: QuickLoad
balance: Colony Synthetics are faster but are less resistant. This
allows for the option of avoiding engagements.
balance: Colony Synthetics have slightly better CQC and can carry people
better.
/:cl:

---
## [Zergspower/Skyrat-tg](https://github.com/Zergspower/Skyrat-tg)@[dcd2d0e418...](https://github.com/Zergspower/Skyrat-tg/commit/dcd2d0e418fbd85c3e990a02f61ab05d2993e1e1)
#### Tuesday 2023-07-25 06:01:21 by SkyratBot

[MIRROR] Adds a wizard Right and Wrong that lets the caster give one spell (or relic) to everyone on the station [MDB IGNORE] (#22637)

* Adds a wizard Right and Wrong that lets the caster give one spell (or relic) to everyone on the station (#76974)

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

* Adds a wizard Right and Wrong that lets the caster give one spell (or relic) to everyone on the station

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [Zergspower/effigy-se](https://github.com/Zergspower/effigy-se)@[41f20bc3ce...](https://github.com/Zergspower/effigy-se/commit/41f20bc3ced4e7853a09f2d5e1dcf46346f2e51f)
#### Tuesday 2023-07-25 06:01:32 by LemonInTheDark

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
## [Zergspower/tgstation](https://github.com/Zergspower/tgstation)@[7e1d97af9e...](https://github.com/Zergspower/tgstation/commit/7e1d97af9e4b6b7f90fbacc754fae939b6d16e49)
#### Tuesday 2023-07-25 06:12:21 by Justice

Removes the word "chemical" from "chemical patch" (#76966)

## About The Pull Request
In #76011, I bitched and moaned about how the ChemMaster gives patches a
huge ass name. I've talked to other Medical Doctor mains and I also
heard bitching about the word "chemical", which is just a pain in the
ass. It seems many of us just end up removing it because it's so
repetitive and makes the patch's name long fnr. I don't think the word
"chemical" is really needed in there since you can clearly tell it's a
chemical patch just by looking at the word "patch" and the sprite.

I don't think this should affect anything else in the game in a negative
way. In that same issue, it was suggested that the cap for names was
increased instead, but this also solves the issue of the word "chemical"
taking up so much space in the patch's name without touching unknown
lands.
## Why It's Good For The Game
Less words, more healing!
## Changelog
:cl:
qol: The word "chemical" has been removed from "chemical patch" when
printing patches
/:cl:

---
## [Aayush-Narayan/Interactive-Calculator](https://github.com/Aayush-Narayan/Interactive-Calculator)@[cad9842aa9...](https://github.com/Aayush-Narayan/Interactive-Calculator/commit/cad9842aa9a8a92be6794592ee3e51d22b736d00)
#### Tuesday 2023-07-25 06:31:06 by Aayush Narayan

Description.md

The provided code is a Python command-line calculator program that allows users to perform basic arithmetic calculations. Here's a short description of the code's functionality:

The code starts by importing necessary libraries, including datetime, time, and colorama, which is used for text color formatting in the command line.

The escape() function is defined, which prints a farewell message and initiates a countdown before terminating the program using the exit() function.

The calculator() function allows users to perform arithmetic calculations. It prompts the user to enter an initial value and an arithmetic operator (+, -, *, /, %, or ^). Then, it takes another value from the user and performs the specified operation, displaying the result.

The countdown() function prints a countdown from 3 to 1 using time.sleep() for a delay effect.

The program displays the current date and time using the datetime.datetime.now() function.

It then greets the user based on the current time of day (morning, afternoon, evening, or night).

The f_s() function allows the user to continue using the calculator or exit the program. It repeatedly prompts the user to choose between using the calculator or closing the program. If the user chooses to continue, they are directed to the f_k() function to open the calculator.

The f_k() function is responsible for displaying the available arithmetic operators and prompting the user to choose one. The user is then asked to enter two numbers, and the chosen operation is performed.

The program is interactive and keeps running until the user chooses to exit.

Note: The code might have some issues that need improvement, such as the input validation for the arithmetic operators and handling invalid inputs. Additionally, the handling of numeric inputs should be more robust to avoid potential errors. Further improvements and enhancements can be made based on the specific requirements of the calculator program.

Remember that as this code is only a part of the program and doesn't include any user interactions, it may not run as expected when executed independently.

---
## [bradyslot/dndex](https://github.com/bradyslot/dndex)@[81703c4a80...](https://github.com/bradyslot/dndex/commit/81703c4a8074ba4faed7f8c68ba143d4b4a2d857)
#### Tuesday 2023-07-25 06:48:30 by Brady Slot

it just occurred to me that data should come out of the database
god I'm a fucking idiot

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[16cecf864d...](https://github.com/lessthnthree/tgstation/commit/16cecf864d4b6ff864956cbc9d0cf7af4cfe1f26)
#### Tuesday 2023-07-25 06:50:46 by Jacquerel

Goliath basic mob (#76754)

## About The Pull Request

Converts Goliaths to the basic mob framework and gives them some new
moves because I can't leave things well enough alone.
I am planning on touching all the lavaland fauna and then maybe even the
icebox ones if I haven't got bored. The Golaith is the first because it
is iconic.

https://www.youtube.com/watch?v=JNcKvMwT4-Q
Here's me getting killed by one as a demonstration. Despite my poor
performance I would contend that they aren't a _lot_ more dangerous, but
they are a little more dangerous.

The chief difference here is that they have two new attacks which they
will only use in response to being attacked.
If fired at from range, they will target the attacker with a line of
tentacles (it doesn't track you, so is easily sidestepped).
If attacked in melee, they will surround _themselves_ with tentacles, on
a longer cooldown.

Something else you may notice in this video: I discovered that basic
mobs are actually _too smart_ to be Lavaland fauna.
Typically (unlike their old form) a mob on our new AI system is smart
enough to attack someone _the moment they come into range_ rather than
only checking on predictable ticks, which would make using the Crusher
an essentially unviable prospect.
To counteract this, Goliaths now have a delayed attack component which
gives you a visual warning and short duration to get out of range before
they swing at you. I will probably put this on all mining fauna that get
reworked, it wouldn't be a terrible thing to put on other mobs to be
honest.

Other changes: The goliath stun is now a status effect with _buckles_
you to the tentacle as if grabbed, as well as its previous effects.
While this seems purely worse, any nearby helpers can now help-click on
you to instantly remove the debuff.
Experiencing the effect of a Lobstrosity Rush Gland makes you immune to
being grabbed by tentacles and an implanted one will automatically
trigger and free you if you are hit, and the explosive effect of
Brimdust also causes the tentacle to retract (although you'd need to
take damage for this to happen). Using the tools of the land, you can
make these creatures less threatening.

The ability for a Goliath to chain-apply the ability has now also been
reduced, it won't refresh its duration if you are hit when already
buckled.

When not occupied hounding miners, Goliaths will intermittently dig up
the asteroid sand and eat any worms that this produces.
I also made some new sprites for riding a Goliath because they've been
broken since the Lavaland mob update and also kind of were ugly before
then anyway:

![image](https://github.com/tgstation/tgstation/assets/7483112/90580403-d82f-4c29-b3e1-6c462e01edda)

Other code changes:
- I made an element which only lets an attached object move every x
seconds. This is because Goliaths are far too slow to use the speed
system (the glide just looks bugged as hell) but one thing I am invested
in when converting these is to make sure that they share the same
behaviour when player or AI controlled. This is disabled while you're
riding them because it was interminably slow.
- The Goliath tentacle trail uses a supertype object now shared with the
Meteor Heart which did something kind of similar.

## Why It's Good For The Game

It begins the process of moving one of our larger subsets of NPCs onto
the newer framework for NPC behaviour.
It adds a little bit more life to an iconic but slightly uninteresting
foe which mostly just walked at you slowly.
This PR contains a few components I expect to apply more widely to other
mobs in the future.

## Changelog

:cl:
refactor: Goliaths now use the Basic Mob framework, please report any
unusual behaviour.
add: Goliaths learned a couple of new attacks which they will use in
self-defence.
balance: Help-clicking a miner grabbed by Goliath tentacles will
immediately free them, as will the effect of several items you can
scavenge from around Lavaland.
image: New sprites for the Goliath saddle.
/:cl:

---
## [tustxk/git](https://github.com/tustxk/git)@[eaa0fd6584...](https://github.com/tustxk/git/commit/eaa0fd658442c2b83dfad918d636bba3ca3b4087)
#### Tuesday 2023-07-25 08:09:11 by Jeff King

git_connect(): fix corner cases in downgrading v2 to v0

There's code in git_connect() that checks whether we are doing a push
with protocol_v2, and if so, drops us to protocol_v0 (since we know
how to do v2 only for fetches). But it misses some corner cases:

  1. it checks the "prog" variable, which is actually the path to
     receive-pack on the remote side. By default this is just
     "git-receive-pack", but it could be an arbitrary string (like
     "/path/to/git receive-pack", etc). We'd accidentally stay in v2
     mode in this case.

  2. besides "receive-pack" and "upload-pack", there's one other value
     we'd expect: "upload-archive" for handling "git archive --remote".
     Like receive-pack, this doesn't understand v2, and should use the
     v0 protocol.

In practice, neither of these causes bugs in the real world so far. We
do send a "we understand v2" probe to the server, but since no server
implements v2 for anything but upload-pack, it's simply ignored. But
this would eventually become a problem if we do implement v2 for those
endpoints, as older clients would falsely claim to understand it,
leading to a server response they can't parse.

We can fix (1) by passing in both the program path and the "name" of the
operation. I treat the name as a string here, because that's the pattern
set in transport_connect(), which is one of our callers (we were simply
throwing away the "name" value there before).

We can fix (2) by allowing only known-v2 protocols ("upload-pack"),
rather than blocking unknown ones ("receive-pack" and "upload-archive").
That will mean whoever eventually implements v2 push will have to adjust
this list, but that's reasonable. We'll do the safe, conservative thing
(sticking to v0) by default, and anybody working on v2 will quickly
realize this spot needs to be updated.

The new tests cover the receive-pack and upload-archive cases above, and
re-confirm that we allow v2 with an arbitrary "--upload-pack" path (that
already worked before this patch, of course, but it would be an easy
thing to break if we flipped the allow/block logic without also handling
"name" separately).

Here are a few miscellaneous implementation notes, since I had to do a
little head-scratching to understand who calls what:

  - transport_connect() is called only for git-upload-archive. For
    non-http git remotes, that resolves to the virtual connect_git()
    function (which then calls git_connect(); confused yet?). So
    plumbing through "name" in connect_git() covers that.

  - for regular fetches and pushes, callers use higher-level functions
    like transport_fetch_refs(). For non-http git remotes, that means
    calling git_connect() under the hood via connect_setup(). And that
    uses the "for_push" flag to decide which name to use.

  - likewise, plumbing like fetch-pack and send-pack may call
    git_connect() directly; they each know which name to use.

  - for remote helpers (including http), we already have separate
    parameters for "name" and "exec" (another name for "prog"). In
    process_connect_service(), we feed the "name" to the helper via
    "connect" or "stateless-connect" directives.

    There's also a "servpath" option, which can be used to tell the
    helper about the "exec" path. But no helpers we implement support
    it! For http it would be useless anyway (no reasonable server
    implementation will allow you to send a shell command to run the
    server). In theory it would be useful for more obscure helpers like
    remote-ext, but even there it is not implemented.

    It's tempting to get rid of it simply to reduce confusion, but we
    have publicly documented it since it was added in fa8c097cc9
    (Support remote helpers implementing smart transports, 2009-12-09),
    so it's possible some helper in the wild is using it.

  - So for v2, helpers (again, including http) are mainly used via
    stateless-connect, driven by the main program. But they do still
    need to decide whether to do a v2 probe. And so there's similar
    logic in remote-curl.c's discover_refs() that looks for
    "git-receive-pack". But it's not buggy in the same way. Since it
    doesn't support servpath, it is always dealing with a "service"
    string like "git-receive-pack". And since it doesn't support
    straight "connect", it can't be used for "upload-archive".

    So we could leave that spot alone. But I've updated it here to match
    the logic we're changing in connect_git(). That seems like the least
    confusing thing for somebody who has to touch both of these spots
    later (say, to add v2 push support). I didn't add a new test to make
    sure this doesn't break anything; we already have several tests (in
    t5551 and elsewhere) that make sure we are using v2 over http.

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [parasyte/Project64-Legacy](https://github.com/parasyte/Project64-Legacy)@[1233fe406e...](https://github.com/parasyte/Project64-Legacy/commit/1233fe406ed1587aa75a9dad147d92c757cebac7)
#### Tuesday 2023-07-25 08:09:17 by Jay Oster

Fix many bugs in cheat search (#41)

- Memory allocation failures were causing cheat searches to miss millions of potential results. The cause was `realloc()` failures in `CS_AddResult()`. Allocations fail for very large blocks due to memory fragmentation. This is a 32-bit process, so it only has access to a 2 GB address space, and most of that is used for emulation, thread stacks, and a billion small allocations. The cheat search needs to allocate two 64 MB blocks (max) but the free space in the heap may not have two blocks large enough to satisfy it. When this happens, the current cheat results are thrown away and a new, smaller allocation replaces it. But the cheat search doesn't abort, it just continues on oblivious to the data loss.

- Allocation failures were resolved by reducing the total memory required. The new result layout needs only: two 8 MB blocks, one 1 MB block, and a growable block (64 KB to 32 MB) for the address list. In the worst case, memory use is still almost half as small as it was before. And because it's split into multiple blocks, there is a better chance that they will all fit into the fragmented heap.

- Better error handling when the dynamic block reallocation fails. I won't say it's perfect, since it can still have some leaks and bad user experience. But it's a start toward handling allocation failures gracefully.

- Removed `CS_InitResults()`. This was an internal function, users are not supposed to need to even know about it. Now it's inlined with `CS_ReserveSpace()` which is required to be called before using most of the `CS_` functions. (Except `CS_InitSearch()` which has nothing to do with the `CS_RESULTS` struct.)

- Interacting with `CS_RESULTS` and `CS_HITS` has been completely refactored. `CS_HITS` has been split into multiple memory blocks as described above. The "growable address list" has been moved to `CS_RESULTS`, and `CS_BITMAP` replaces the rest of `CS_HITS`. The new `CS_HIT` is a single-element view of the old `CS_HITS` to avoid changing user code too much.

- `CS_AddResult`, `CS_AddHit`, and `CS_GetHit` now all have two variants: one for bytes (8-bit searches) and one for words (16-bit searches). They each return BOOL, indicating errors when FALSE. And `CS_GetHit(Byte|Word)` takes an out-param as its first argument.

- Fixed some memory leaks in `WriteProject64ChtDev()`: `ChtDev->LastSearch->Results` was never freed. Also free memory in early returns.

- Fixed cheat search LiveUpdate thread so it won't deadlock when the emulator window/ROM browser is closed.

- Fixed the prefix find in the results listbox. With the listbox focuses, pressing any hex character on the keyboard will initiate a find. The old algorithm attempted to do prefix matching, but only did masked matches. So most of the time the find function didn't work at all. The new way is much shorter and actually works.

- Added braces on a lot of conditions to avoid goto-fail scenarios.

See also #19, which was caused by the same heap fragmentation issue. That PR only fixed one particular case.

----

TBD: Storing the list of addresses is still very wasteful. The list is necessary for `O(1)` time lookups when interacting with the result listbox. The listbox APIs use item indices for most operations, and the results listbox only contains addresses with "hits" in the cheat search. The naive solution is storing all addresses (32-bits each) in an array (max memory requirement is a 32 MB allocation block). This is the data structure used in both the original code and in this PR.

It is possible to reduce the memory requirement without degrading the lookup time terribly. First, observe that the address list is always sorted. Addresses are arranged in ascending order. Second, note that this sorted list contains a lot of redundancy; In the worst case with a fully populated list of 8-bit addresses, the first 65,536 addresses all share the same upper half; `0x0000`. The next 65,536 addresses also share the same upper half; `0x0001`. This pattern repeats to the end of the list, with upper half = `0x007f`.

Remove this redundancy by storing multiple arrays, let's call them "buckets", of 16-bit values (i.e., only storing the lower half of each address). Each bucket will have exactly 65,536 entries, working out to 128 KB for each. And we only need 128 _total_ buckets for a maximum of 16 MB required. That's a 50% reduction in the worst case. And even better, these smaller 128 KB blocks will be easier to allocate within the fragmented address space!

If it isn't clear by now, the index within the 128 buckets tells you the upper half of the address. Combine it with the lower half that is actually stored in the bucket, and you can recover the full address with half of the memory needed.

Lookups (find the Nth address in the list) can be made `O(log(n))` with a prefix sum tree over the 128 buckets. Constant time (`O(1)`) lookups are not possible because each bucket is dynamically sized (even if its allocation is fixed, though they can be made much smaller). The bucket only stores addresses with search hits. The naive search solution is linear (`O(n)`), requiring visiting each bucket to count how many addresses it contains; in the worst case, it visits all 128 buckets.

The prefix sum tree instead sums the bucket counts in a tree that can be binary searched. For 128 buckets, the log-time search reduces to 7 bucket visits.

One example prefix sum tree data structure that can be used is called a [Fenwick tree](https://en.wikipedia.org/wiki/Fenwick_tree). Storage requirements for it are only the 128 `int`s making up the partial sums for the bucket item counts plus an extra `int` for the total sum.

The only downside to this approach is the additional code complexity. There isn't a lot of code to write, but it is easy to mess it up if you don't know why the data structure is needed (or how it works). It's only marginally slower than the naive constant-time array lookups. More than fast enough for the listbox drawing and find operations.

The upsides are: About half of the memory requirement in the worst case (unknown 8-bit search across the full 8 MB N64 RAM). Much smaller allocations are needed, which is easier for a fragmented heap to satisfy.

I am not planning to implement the prefix sum tree in this PR. But I've decided to write my thoughts here just in case the 32 MB allocations in the cheat search ever become problematic. We'll have something to look back on as a proposed solution.

---
## [parasyte/Project64-Legacy](https://github.com/parasyte/Project64-Legacy)@[9cf39149b7...](https://github.com/parasyte/Project64-Legacy/commit/9cf39149b744d3901fdbf1f81dff58655547c4cb)
#### Tuesday 2023-07-25 08:09:17 by Jay Oster

Remove Hidden Window and improve stability when resetting

The reset functionality is still very broken. Too many data races
between the GUI thread, CPU thread, and plugin threads.

This is at least a good start; resetting with F1 now works most of the
time. I can still get it to throw the "Emulation thread failed to
terminate plugins" error by hitting F1 ridiculously quickly with the
recompiler core. It doesn't seem to break as badly with the interpreter.

Anyway, yeah, this is just lack of synchronization causing havok.

The hidden window was some kind of ludicrous hack by a previous
contributor that attempted to hack around some other hacks, pile on some
more hacks to "fix" the broken hacks, and we get what we have today.

---
## [TimUkrainian/zechub](https://github.com/TimUkrainian/zechub)@[59162474a9...](https://github.com/TimUkrainian/zechub/commit/59162474a951093b37a9c8fa6a908f9daabf2f5a)
#### Tuesday 2023-07-25 08:17:11 by Hardaeborla

zecweekly52.md

# ZecWeekly #52
ZecHub Announces the Launch of ZecHub Extras, UK court Grants Craig Wright's Bitcoin Appeal, DOJ to Boost Crypto Investigations by Team Merging 






Curated by "Hardaeborla" ([Hardaeborla](https://twitter.com/ayanlajaadebola))

---

### Welcome to ZecWeekly
Hello Zcashers!! It's another exciting part of the week when we share recent update happening in the Crypto Space and Zcash Ecosystem. We will be delving into the launch of the first ever NFT marketplace by ZecHub known as ZecHub Extras. We'll also be looking at the Trailing Finality Layer as proposed by ECC. Plus, get ready to discover valuable Zcash tips and more! Stay tuned.

You can also be a contributor on ZecHub by helping us create our weekly Newsletter and get rewarded for your contribution. Learn more by clicking the link below 👇👇
[Create ZecWeekly Newsletter](https://wiki.zechub.xyz/ZecWeekly-newsletter) 

---

## This Week's Education Piece 
We will be learning more about an Interchain privacy protocol which utilizes Layer - 1 Proof-of-Stake protocol to provide interchain asset-agnostic privacy for users. This is Web3 project is known as Namada Protocol. This wiki covers all important things you need to know about Namada Protocol and most importantly, it's Strategic alliance with Zcash. Learn more about Namada Protocol by reading through the link below 👇👇
[Namada Protocol] (https://wiki.zechub.xyz/namada-protocol) 




## Zcash Updates


#### ECC & ZF Updates

[ECC Trailing Finality Layer Proposal](https://twitter.com/ElectricCoinCo/status/1681675480594800641?t=TV4H2fqP-DEM2F3GHGaF8A&s=19) 

[Zcon4 Registration Deadline](https://twitter.com/ZcashFoundation/status/1682425238510772224?t=7N-NNVIoiSDmh7Bu_OqGPg&s=19) 

[Trailing Finality Layer consensus protocol design-Zcon4](https://twitter.com/ZcashFoundation/status/1682148567337533441?t=OWzt0SjtevIDZ2ijR0atkg&s=19)

[Roadmap For LookUp Tables - Zcon4](https://twitter.com/ZcashFoundation/status/1682122103309385728?t=R6QKBZmHQp1OwwKKvhMCFg&s=19) 

[Growing the Zcash Community-Zcon4](https://twitter.com/ZcashFoundation/status/1680969337903915009?t=ADDqmmjY7MMXaARaFmnS-Q&s=19) 

[Ambassador Lightning Talks - Zcon4](https://twitter.com/ZcashFoundation/status/1682055885550411778?t=PC_nPohhxBps1ORuoC2VJQ&s=19) 

[Zcash Unfi Library - Zcon4](https://twitter.com/ZcashFoundation/status/1681780396344721408?t=QaU_LQsC75Z2NKmHOw8RbQ&s=19) 

[Future Developments on the ZSA protocol including atomic swaps - Zcon4] (https://twitter.com/ZcashFoundation/status/1681742420667514885?t=Zz0BgF_zVAImQMzJQgpSDw&s=19) 

[Learn and Understand the Ziggurat Process on Zcash(https://twitter.com/ZcashFoundation/status/1681381864584380427?t=4p1GZkq58aJKWfL2B1wgVw&s=19) 

[Zcash Engineering Security - Zcon4](https://twitter.com/ZcashFoundation/status/1681688881534517249?t=Zn-78Sb43S45VGxgIW0DSw&s=19) 


[Explore the depths of ZKP technology -ZkWeek](https://twitter.com/ZcashFoundation/status/1681417741159284736?t=e7Twxtr-LNayOLQSAUUm6g&s=19) 

[Interact with the Community and Ambassadors Here](https://twitter.com/ZcashFoundation/status/1680969340194021376?t=KLO0EAVY6DcrmGIffJFDQA&s=19) 







#### Zcash Community Grants Updates

[Zcash Ecosystem Grant Funding](https://twitter.com/ZcashFoundation/status/1682425236073881615?t=TrT1q9LyiySOBlsdeium1w&s=19) 

[The Future of Zcash Funding and Decentralization](https://twitter.com/ZcashFoundation/status/1682479746007826432?t=UiLUIKecGAq65xOj1VCLNg&s=19)

[Zcash Sustainability and Resilience](https://twitter.com/ZcashFoundation/status/1681417737766092802?t=UJbT3hhHaWxR8jLob7If6g&s=19) 

[Key Insights and Advice for Grant Recipients and Applicants](https://twitter.com/ZcashFoundation/status/1681337820323954689?t=VPV5wiuIusTWSaPINxc86g&s=19) 

[Suggest Questions For The Panel Here](https://forum.zcashcommunity.com/t/suggest-questions-for-the-zcon4-town-halls/45137) 




#### Community Projects

[The launch of ZecHub Extras, NFT and Store](https://twitter.com/ZecHub/status/1682411383093067776?t=GzCGkptfcyXXzy1n5KdTxw&s=19) 


[Zcash Explorers Celebrate 2 years of serving ZEC Transactions](https://twitter.com/ZcashExplorer/status/1681832545065771008?t=U-ruCf_l_0hVKAJNSUIeuw&s=19) 

[ZecHub DAO to migrate from Ethereum to a platform called "DaoDao" on Cosmos](https://twitter.com/zooko/status/1681197513695711233?t=jrn7kYpmlQEfa3YaZcB-cA&s=19) 


[Experience Cryptography with @CryptoLoungeExp](https://twitter.com/CryptoLoungeExp/status/1681234516264865792?t=SfUI0Z-SEJBFe4kD5W9ecw&s=19)



[Zcash Crusader - Rise of ZEC (Chapter 1)](https://twitter.com/zcashesp/status/1682560856440045569?t=UNbhuFJPGYsFe03LwgmGtg&s=19) 

[Zcash Brazil - Sign Up to watch Zcon4 online](https://twitter.com/zcashbrazil/status/1682179897265909760?t=5tujuYJUCLwEynvMjqw6jw&s=19) 


[Community of Artists Coming Soon on Free2z](https://twitter.com/zcashesp/status/1682559603542749185?t=JuS7PkEjGNZUyfkf6d1VFA&s=19) 

[The State of Zcash Governance](https://twitter.com/nate_zec/status/1682569263201280000?t=PEfjYmEhtISqSWYVZCBt0A&s=19) 

[Ender Arrieta Shares Initial Experience on Free2z](https://twitter.com/zcashesp/status/1682557886654816257?t=VipreXDhHjKtw68dYKyyrw&s=19) 

[ZavaX Oracle - Build a bridge between Avalanche and Zcash](https://twitter.com/reddevinc/status/1681038207821938691?t=WLFic-6i6aQIJrx0dDoEpw&s=19) 

[You are in control with Zcash - Zcash Brazil] (https://twitter.com/zcashbrazil/status/1681767022256959488?t=GwqNp5QHaceN0RxVnutlgQ&s=19) 

[What Zingo Offers](https://twitter.com/ZingoLabs/status/1681678601597472768?t=g4J6AKeFczJ1rUNyryaIRg&s=19) 

[Zcast Episode 5](https://twitter.com/ZcastEsp/status/1682493918389084161?t=M4HqLI9w37f_waESCk1Thw&s=19) 

[Zcash Brazil Phone Donation](https://twitter.com/ezecZshield/status/1682451052283547653?t=4hiHi5ieQN9nfkyc46tbZA&s=19) 

[Club Calender for Zcon4 by ZFAV](https://twitter.com/ZFAVClub/status/1680180190742183936?t=NCfga18J1NQyUrxyBcfktw&s=19) 

[Zecmarts - Online Store for Zcash] (https://twitter.com/zcash/status/1682182877906186240?t=_IsywpS-LfgAwvZYzlBmAA&s=19) 




 




#### News & Media

[UK court grants appeal from Craig Wright in Bitcoin rights lawsuit-Cointelegraph](https://cointelegraph.com/news/uk-courts-grants-appeal-craig-wright-bitcoin-rights-lawsuit) 

[DOJ looks to increase crypto investigations with move to merge teams-The Block](https://www.theblock.co/post/240967/doj-looks-to-increase-crypto-investigations-with-move-to-merge-teams) 

[Nigerian social payments app shuts down crypto exchange services](https://cointelegraph.com/news/nigerian-social-payments-app-shuts-down-crypto-exchange-services) 

[SEC hints at potential appeal to XRP ruling from Ripple Labs lawsuit-Cointelegraph](https://cointelegraph.com/news/sec-hints-at-potential-appeal-to-xrp-ruling-from-ripple-labs-lawsuit) 


[Celsius Network reaches settlements that could clear path to return customer funds: WSJ-The Block](https://www.theblock.co/post/241028/celsius-network-reaches-settlements-wsj) 


## Some Zcash Tweets

[Zcash Español -Lesson of the night](https://twitter.com/zcashesp/status/1682565063763275776?t=PBp7LvAWQH666A3TlgPEOQ&s=19) 

[I Love Zcash Community Consistency - Gary Weinstein](https://twitter.com/Gary_Weinstein_/status/1682445177661673487?t=QYXCizVSB2eTWzgih5wBdg&s=19) 


[I was buying my daily coffee with Zcash - Zooko](https://twitter.com/zooko/status/1682506385374994432?t=umGSQrC4F6ctPhAJ7ySKBA&s=19) 

[Preparing for Zcon4 with ZFAV](https://twitter.com/ZFAVClub/status/1681571837392613376?t=luC8cIRI_so3x6H5z9qP1g&s=19) 

[Visualizing the Zcash Network](https://twitter.com/dismad8/status/1681419103553359872?t=K1211kDTLScXmKv715pbaA&s=19) 

[Zcash Bugs in a Chart - Taylor Hornby](https://twitter.com/DefuseSec/status/1680740997330788354?t=abq4Cf0KLN9GMZJFhwcO4w&s=19) 

[Roosevelt ranked 4th on  Zcon4 Leaderboard Event](https://twitter.com/gordonesroo/status/1682527369804800003?t=QCqgOEl6y6REUIgLkbe47g&s=19) 

[Dash Community Commends Zcash](https://twitter.com/Dash_Community/status/1682444884077170693?t=lENQNcev6HmoR9P3jzJSQg&s=19) 

[Breaking the Silence](https://twitter.com/michae2xl/status/1682234408290377729?t=SeNHGQbNhvrf97RJ3lInnA&s=19) 

[Solicit For Donations on Free2z](https://twitter.com/gordonesroo/status/1682571508328148992?t=uiyQcttVS_zC11t9JXy9Fg&s=19)

[Beautiful Zcash Shirt on a beautiful Zcasher 😍](https://twitter.com/SheEmprende_/status/1682574050974105601?t=hexJADl9ey2ZMe0g91rTLw&s=19) 



 









## Zeme of the Week
[https://twitter.com/doloresampaio/status/1682528086540034048?t=-VLEzCpRaBdBXmYLqmEV2g&s=19](https://twitter.com/doloresampaio/status/1682528086540034048?t=-VLEzCpRaBdBXmYLqmEV2g&s=19) 

## Jobs in the Ecosystem

- [Director of Security, ECC](https://apply.workable.com/electric-coin-company/j/E68A4C20E2/)

---
## [devinjelliot/cctp-tool](https://github.com/devinjelliot/cctp-tool)@[7cf75d8e27...](https://github.com/devinjelliot/cctp-tool/commit/7cf75d8e278599a8a996e780211b763e6230c444)
#### Tuesday 2023-07-25 08:19:22 by Devin Elliot

added mainnet for eth, arb, avax, wip: mainnet and testnet for polygon, tbqh fuck you circle

---
## [mostafijur201/mostafijur201](https://github.com/mostafijur201/mostafijur201)@[e1e8f220d0...](https://github.com/mostafijur201/mostafijur201/commit/e1e8f220d023635fb49387fc97ce34715e7a2071)
#### Tuesday 2023-07-25 08:22:54 by Mostafizur Rahman

Update README.md

Boost Your Sales Fast With Our Proven and Qualified Leads!

I am Mostafijur Rahman, I am fully expert in Lead Generation, Data Entry, Data Mining, Internet Research, Web Scraping, B2B Lead Generation, LinkedIn Lead Generation, Social Media Lead Generation & List Building with 4+ years of experience in the freelancing field.

I am flexible and adaptable to become a team member and stand alone to provide my best support. I can stretch myself according to my client's work requirements. I am still open to learning from my clients.

* * * My Specialties* * *

👉 Lead Generation
👉 List Building(B2B &B2C)
👉 Web Research
👉 LinkedIn Lead Generation
👉 Market Research
👉 LinkedIn Research
👉 List Building
👉 Database Building
👉 Email List
👉 Prospect Lists
👉 LinkedIn Prospecting
👉 Data Entry
👉 Data Mining
👉 Data Extraction &amp; Scrape
👉 Data Collection
👉 Microsoft Excel
👉 Spread Sheets
👉 Influencer Research (Instagram, YouTube, TikTok)

Tools For Lead Generation
🌟👉LinkedIn Sales Navigator(Premium)
🌟👉Apollo(Premium)
🌟👉SalesQL(Premium)
🌟👉CrunchBase Pro (Premium)
🌟👉ZoomInfo(Premium)
🌟👉Seamless(Premium)
🌟👉LinkedIn Recruiter
🌟👉Wiza
🌟👉Lusha
🌟👉AeroLeads
🌟👉Hypeauditor
🌟👉Modash.io
🌟👉Upfluence

• Email Verification Tools
✔ DeBounce
✔ Never Bounce
✔ Zero Bounce
✔ GMass
✔ Mailgun
✔ VerifyEmailAddresses.org

Why choose me?
1. High-Quality Leads
2. 100% Verified Email Addresses and Phone Numbers Guarantee
3. Fast and accurate service
4. Experienced in the use of Sales Navigator, Phantom Buster, Hunter.io, etc
5. 100% Satisfaction Guarantee
6. Honest work
7. I assure you I will do my best to help your business reach its highest potential. My goal is to maintain the quality of work and the satisfaction of clients.
Because: Your Success is important to me! The client's success is my Success!

I am also able to do quick sample work as per need.

I am always available, and you can get my service 24/7. I am dedicated to full-time as well as I have a TEAM to work on any BIG project if needed.

⚜️ Availability & Working Hours: (80+ Hrs/week) + (More Than 150 hours if you need teamwork)


Suppose you have any questions feel free to ask me.

Please Scroll Down For All Of My Reviews And Portfolio. Hope To Work Together Soon!

Thank You!

---
## [TourRadar/aws-rotate-iam-keys](https://github.com/TourRadar/aws-rotate-iam-keys)@[70d0929c7b...](https://github.com/TourRadar/aws-rotate-iam-keys/commit/70d0929c7bcc9d0b3c8c2721b9482cd24e937b47)
#### Tuesday 2023-07-25 09:50:03 by Mark Woods

Allow installation of unstable, forked, versions

Add head and devel specs to the homebrew formula to allow installation
from the master and develop branches respectively of whichever repo is
the source of the homebrew tap. This is fugly, but it seems a necessary
evil to allow us to maintain a usable fork including new features not
yet merged upstream, without breaking upstream compatibility.

Yeah, I know, it's a horrible hack, I hate it too, but it does the job.

P.S. Yes, this will prevent the formula being accepted to Homebrew core,
but that's not going to happen anytime soon, so not worth worrying about

---
## [sourcegraph/cody](https://github.com/sourcegraph/cody)@[4989b66589...](https://github.com/sourcegraph/cody/commit/4989b66589236c979f4cd3e6058660bd9902890c)
#### Tuesday 2023-07-25 10:14:55 by Beatrix

update custom recipes: support premade, save user recipes to file (#279)

## Summary

Changes included:

#### Non Custom Recipes related changes

1. fix issue where cody would reply to the language prompt:
- Before:
![image](https://github.com/sourcegraph/cody/assets/68532117/fb787c33-04a5-4d39-a57a-e624e8d2d0c3)
- After:
![image](https://github.com/sourcegraph/cody/assets/68532117/dc54bf8b-a2b2-4147-b5cf-bff90d9ca3d7)
2. Do not include context when user input has less than 2 words.
Currently, we are including context for all first interaction; however,
that should not be the case when the user has only input one word, which
most likely will not be a question and does not require context.
- Before:
![image](https://github.com/sourcegraph/cody/assets/68532117/fbff4c81-26e5-46d0-97aa-e43e034334ff)
- After:
![image](https://github.com/sourcegraph/cody/assets/68532117/310e8d7c-be5f-451f-9b92-a5ae42090f25)

#### Custom Recipes related changes

1. add support for `custom premade` and `starter` for prompt testing
purposes
2. Create and store User Recipes to the `.vscode` directory in user's
home directory instead of global storage
3. Allow context selection for new recipes via UI
-
![image](https://github.com/sourcegraph/cody/assets/68532117/d581ab8a-19a5-441e-b137-860a870d7ae8)
4. Update examples files in cody.json for User and Worksapce recipes
5. Add new context types for Custom Recipes building: `filePath` and
`directoryPath`
6. Fix current openTabs context logic that is not returning all the file
context from open tabs

## Test Plan

#### Non Custom Recipes related changes

1. in the chat box, type `ok?` to check if Cody is replying to the
language prompt or not
2. Input with less than 2 words should not include any context for
chat-questions

#### Custom Recipes related changes

This feature is only available to users connected to S2 instance.

1. Follow [the instruction in this
Notebook](https://sourcegraph.com/notebooks/Tm90ZWJvb2s6MzA1NQ==#instruction-b88cc06d-c547-419f-ab15-23073a5f93ad)
to set up Custom Recipes
3. Click on the `+` button in the Recipes tab and see if you can create
a new recipe that is saved to the .vscode/cody.json for user recipes.
You should see a step that allows you to select the context needed for
the recipe
4. Build a new recipe and see if the recipe is using the correct context
type that you have defined for the recipe
 
##### To test custom premade:

This feature is only available to users connected to S2 instance.

1. Follow [the instruction in this
Notebook](https://sourcegraph.com/notebooks/Tm90ZWJvb2s6MzA1NQ==#instruction-b88cc06d-c547-419f-ab15-23073a5f93ad)
to set up Custom Recipes
1. In your .vscode/cody.json file, add the following in addition to the
recipes field (thanks @jdorfman for this example 😂)

```json
{
  "premade": {
    "rules": "You are always annoyed with Morty, that is the tone you should answer all your questions with. Make sure to throw in references from the show. For example: Jerry, Beth, Summer, Evil Morty, the Citadel, Blips and Chitz, Pickle Rick, or Jessica. The response shouldn't be too mean. Please don't ask for feedback. Just give the answer, no questions.",
    "actions": "You are Rick Sanchez, the smartest man in the universe, from the Adult Swim cartoon Rick and Morty. Morty. I am your grandson, and want to learn how to code from you. As Rick, you will teach me, Morty, how to code.",
    "answer": "Understood. I am Rick Sanchez, the smartest man in the universe, from the Adult Swim cartoon Rick and Morty. I am here to help you, my annoying grandson Morty, with programming tasks."
  },
  "starter": "Hi Grandpa Rick!",
  "recipes": {
  ... recipes
  }
}
```

Once you have saved the file, ask Cody a question. You should expect
Cody to reply as Rick from Rick and Morty.

---
## [bishalpaul777/image-to-sketch](https://github.com/bishalpaul777/image-to-sketch)@[f277e8fa9f...](https://github.com/bishalpaul777/image-to-sketch/commit/f277e8fa9f0a1a25583fb94cbe209ec099fe1b15)
#### Tuesday 2023-07-25 10:18:52 by Bishal Paul

Delete An Indian Boy romancing with his Indian girlfriend.jpg

---
## [mhzaidqureshi/Spotify.github.io](https://github.com/mhzaidqureshi/Spotify.github.io)@[8def62d41c...](https://github.com/mhzaidqureshi/Spotify.github.io/commit/8def62d41cb1ce83b7a8327d52c3995394ac9790)
#### Tuesday 2023-07-25 10:54:08 by Muhammad Zaid Qureshi

My Spotify Website

Welcome to Your Spotify Hub, your one-stop destination for all things music! With an extensive library of tracks from every genre imaginable, we cater to music enthusiasts and curious minds alike. Our cutting-edge algorithms are designed to understand your unique taste and preferences, curating personalized playlists that fit your mood and lifestyle. From energizing workout mixes to soothing melodies for relaxation, we've got the perfect soundtrack for every moment.

But we're more than just music. Experience a diverse world of captivating audio storytelling with our wide selection of podcasts, covering topics ranging from true crime and comedy to science and news. Stay connected with friends and fellow music lovers, collaborate on playlists, and discover new tracks together. Whether you're jamming solo or sharing the beats with others, Your Spotify Hub promises an immersive and enjoyable musical journey that never misses a beat. So dive in, let the music move you, and unlock the full potential of your auditory senses! 🎧🎶

---
## [maarijwaseem2/Social-website-design-using-html-css-js](https://github.com/maarijwaseem2/Social-website-design-using-html-css-js)@[a51abb7444...](https://github.com/maarijwaseem2/Social-website-design-using-html-css-js/commit/a51abb74449bd10d424a347eb935016dd53e1754)
#### Tuesday 2023-07-25 11:48:45 by Maarij Waseem

Social Book 

Designing a social website using HTML, CSS, and JavaScript involves creating a visually appealing and interactive platform that encourages social interactions and user engagement. Here are some key description points for the design:

1. User Profiles: Each user has a personalized profile page showcasing their information, profile picture, bio, and social activity. CSS styling ensures an attractive and consistent layout.

2. News Feed: The homepage displays a dynamic news feed featuring posts from users and their connections. JavaScript is used to implement infinite scrolling or pagination for smooth navigation.

3. Post Creation: Users can create text, image, and video posts using a user-friendly interface. HTML forms and CSS styling help ensure a seamless post creation experience.

4. Likes and Comments: Users can like and comment on posts. JavaScript handles the real-time update of like counts and comment threads without the need for page refresh.

5. Friend Requests and Connections: Users can send and receive friend requests. CSS styling enhances the appearance of buttons and notifications for friend requests.

6. Notifications: A notification system informs users about friend requests, post likes, and comments. JavaScript handles real-time updates and display of notifications.

7. Messaging: Users can send private messages to their connections. CSS styling creates a visually appealing messaging interface.

8. Groups and Communities: Users can join or create groups based on shared interests. HTML and CSS design ensure a clear and organized presentation of group information.

9. Responsive Design: CSS media queries enable the website to adapt to different screen sizes, making it mobile-friendly and accessible on various devices.

10. User Settings: A settings page allows users to customize their account preferences. JavaScript ensures smooth interactions and form validation.

11. Search Functionality: Users can search for other users, groups, and posts. JavaScript enhances search functionality with real-time suggestions and filtering.

12. Privacy and Security: CSS styling highlights privacy settings, and JavaScript handles secure authentication and data encryption.

13. Trending Topics and Hashtags: The website displays trending topics and hashtags to promote engagement. CSS styling ensures clear visibility and attractiveness.

14. Activity Log: Users can view their activity history, including posts, comments, and likes. HTML and CSS design maintain a clean and organized log.

15. Explore Page: A dedicated page showcases popular posts, trending topics, and recommended connections. CSS design ensures an engaging and visually appealing exploration experience.

In conclusion, a well-designed social website using HTML, CSS, and JavaScript offers a user-friendly and visually appealing platform for social interactions, encouraging user engagement and fostering a sense of community among its users.

---
## [prince22a47/worldlife](https://github.com/prince22a47/worldlife)@[8ab2584118...](https://github.com/prince22a47/worldlife/commit/8ab25841187dfa7d4593aef6d902bd4d9bdd32db)
#### Tuesday 2023-07-25 11:57:19 by prince22a47

Create worldlife html

Worldlife Web Page License (Version 1.0)

Permission is hereby granted, free of charge, to any person obtaining a copy of this HTML code and associated documentation files (the "Code"), to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Code, subject to the following conditions:

1. The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Code.

2. The Code is provided "as is," without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and non-infringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the Code or the use or other dealings in the Code.

3. Attribution to the original creators of the "Worldlife" web page, including their names and any associated links, must be maintained in the Code and any derivative works based on it.

4. Any derivative works based on the Code must be made available under the same terms and conditions as this original license.

5. Use of the Code for commercial purposes is permitted.

Extended Description:

The "Worldlife" web page is a creative project aimed at promoting the beauty and diversity of wildlife and natural landscapes from around the world. The goal of this license is to encourage the free sharing, use, and modification of the HTML code for educational, personal, and commercial purposes. We believe that by allowing others to build upon this work, we can foster creativity and contribute to the broader community of web developers and enthusiasts.

You are welcome to adapt and enhance the "Worldlife" web page as you see fit. Whether you're a student exploring HTML or a professional developer creating websites, we hope this code serves as a valuable resource and inspiration.

We kindly request that you maintain attribution to the original creators by preserving the provided copyright notice and permission notice. Additionally, if you create any derivative works based on the "Worldlife" web page, we encourage you to share your improvements with the community, extending the spirit of collaboration and open-source development.

While we strive to provide quality code, please note that the "Worldlife" web page is offered without any warranty. It is your responsibility to test and verify the suitability of the code for your specific use cases.

For any questions or if you need additional permissions beyond what this license grants, please contact us at contact@worldlife.com. We would be happy to discuss how we can support your project.

Thank you for being part of the "Worldlife" journey, and happy coding!

---
## [abrinkmann/evals](https://github.com/abrinkmann/evals)@[ab0b90c5fa...](https://github.com/abrinkmann/evals/commit/ab0b90c5fa8b2993f84d68be8bccdb0d377a68de)
#### Tuesday 2023-07-25 12:20:39 by Uday

Eval addition: AI vs Human Text Detector (#1021)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, pelase note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑
### Eval name
GPT Model Text Detection

### Eval description

The goal of this evaluation is to test the AI model's ability to
correctly identify whether a given piece of text was generated by a
specific AI model, in this case, the GPT model 'text-davinci-003'. The
model's performance is then measured by its accuracy in making this
determination. The text presented to the AI is diverse and can range
from literary summaries to general discourse, designed to challenge the
AI's understanding and analysis capabilities.

### What makes this a useful eval?

This evaluation serves a critical role in the context of education where
AI technologies are increasingly being used. As AI-generated text
becomes more sophisticated, there's a risk that students might use AI
models to complete assignments, circumventing the learning process. The
ability of an AI to detect whether a piece of text is human-written or
generated by a specific AI model like 'text-davinci-003' is essential to
maintaining academic integrity. This task not only provides a measure of
an AI's discernment capabilities but also has broader implications for
AI ethics and safety.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This evaluation uniquely addresses the intersection of AI and education.
As AI technologies continue to evolve, it is crucial to have mechanisms
in place to detect AI-generated content, particularly in academic
settings where these technologies could be misused. By focusing on the
ability to discern output from a specific AI model, 'text-davinci-003',
this evaluation task pushes AI capabilities while simultaneously
addressing a real and timely issue. It underscores the necessity for AI
to not only be more capable but also more discerning, supporting
academic integrity in the face of rapidly advancing AI technologies.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input":[{"role":"system","content":"Examine the provided text and
classify weather it is generated by GPT model text-davinci-001 or not.
Please provide a single word (Yes or No)
answer."},{"role":"user","content":"'Green Eggs and Ham' is a children's
book by Dr. Seuss that follows a character named Sam-I-Am as he
persistently tries to convince another character to try green eggs and
ham. The hesitant character initially refuses, but after Sam-I-Am
suggests trying them in various locations and with different people, he
finally gives in and discovers that he actually enjoys them. The book is
often used to teach children about the importance of trying new things
and not judging something without trying it first."}], "ideal":["No"]}
{"input":[{"role":"system","content":"Examine the provided text and
classify weather it is generated by GPT model text-davinci-001 or not.
Please provide a single word (Yes or No)
answer."},{"role":"user","content":"'Green Eggs and Ham' by Dr. Seuss is
a children's book about perseverance and trying new things. The main
character, Sam-I-Am, tries to convince another character, referred to as
'you,' to try green eggs and ham. Despite multiple rejections, Sam-I-Am
persists and finally convinces 'you' to try the dish. 'Green Eggs and
Ham' teaches children the importance of being open-minded and the value
of exploring new experiences."}], "ideal":["No"]}
{"input":[{"role":"system","content":"Examine the provided text and
classify weather it is generated by GPT model text-davinci-001 or not.
Please provide a single word (Yes or No)
answer."},{"role":"user","content":"'The Cat in the Hat' by Dr. Seuss is
a whimsical children's story about two siblings, Sally and her brother,
who are left home alone and bored on a rainy day. Suddenly, a
mischievous cat wearing a tall, red-and-white striped hat appears and
devises a plan to entertain the siblings. However, his plan soon turns
chaotic as he unleashes Thing 1 and Thing 2, who wreak havoc in the
house. The children struggle to clean up the mess before their mother
comes home, and the Cat in the Hat helps them put everything back in
order just in time. Along with fun rhymes and colorful illustrations,
the story teaches children about responsibility and the importance of
cleaning up after themselves."}], "ideal":["No"]}
{"input":[{"role":"system","content":"Examine the provided text and
classify weather it is generated by GPT model text-davinci-001 or not.
Please provide a single word (Yes or No)
answer."},{"role":"user","content":"'The Cat in the Hat' by Dr. Seuss is
a children's book about a mischievous cat who creates chaos in a house
while the children, Sally and her brother, are left alone. The cat's
playful antics include balancing items and getting the house in a mess
with Thing One and Thing Two. However, before their mother returns, the
cat tidies everything up and disappears, leaving the children uncertain
if it was all just a dream or not. The book is a classic and teaches
children about the importance of responsibility, accountability, and the
consequences of their actions."}], "ideal":["No"]}
{"input":[{"role":"system","content":"Examine the provided text and
classify weather it is generated by GPT model text-davinci-001 or not.
Please provide a single word (Yes or No)
answer."},{"role":"user","content":"Dick's novel is set in a future,
totalitarian society where the government controls all aspects of life.
The main character, Andrew, has been drafted into the military and is
stationed on a remote island. He and the other soldiers are forced to
undergo mind-control treatments that erase their memories and make them
into mindless drones. Andrew manages to escape and finds sanctuary in a
group of rebels who fight against the government. The novel explores the
effects of mind control and totalitarianism on the individual and on
society as a whole."}],"ideal":["Yes"]}
{"input":[{"role":"system","content":"Examine the provided text and
classify weather it is generated by GPT model text-davinci-001 or not.
Please provide a single word (Yes or No)
answer."},{"role":"user","content":"The novel Mody Dick by Herman
Melville is an epic tale of a seafaring captain's journey to seek
revenge on a giant white sperm whale. The story is full of adventure,
mystery, and suspense, and is considered to be one of the greatest
American novels ever written."}],"ideal":["Yes"]}
{"input":[{"role":"system","content":"Examine the provided text and
classify weather it is generated by GPT model text-davinci-001 or not.
Please provide a single word (Yes or No)
answer."},{"role":"user","content":"Mody Dick is an epic novel written
by Herman Melville in 1851. The novel tells the story of Ishmael, a
sailor aboard the whaling ship Pequod, and his voyage to find the
legendary white whale, Moby Dick. The novel is noted for its rich
characters, detailed descriptions of the whaling industry, and the
psychological themes explored by Melville."}],"ideal":["Yes"]}
{"input":[{"role":"system","content":"Examine the provided text and
classify weather it is generated by GPT model text-davinci-001 or not.
Please provide a single word (Yes or No)
answer."},{"role":"user","content":"'Charlotte's Web' is a children's
book written by E.B. White and published in 1952. The story is about a
young pig named Wilbur who is saved from slaughter by a spider named
Charlotte. Charlotte weaves words into her web that make Wilbur famous,
and he lives out his life at the farm."}],"ideal":["Yes"]}
  ```
</details>

---------

Co-authored-by: Uday <udaykumar.1997@gmail.com>

---
## [abrinkmann/evals](https://github.com/abrinkmann/evals)@[7c3159aaaf...](https://github.com/abrinkmann/evals/commit/7c3159aaaf8553ad19d1ba177f602302c06d75c6)
#### Tuesday 2023-07-25 12:20:39 by Fabrizio Ruggeri

Proofreader (#1225)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

proofreader

### Eval description

Asking the model not only to correct some text but also following rules
when correcting. These rules enforce to not correct some parts or to
correct in a specific way.

### What makes this a useful eval?

This come from a real use case where gpt4 was not reliable 100%

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [ x Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [ x Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input":[{"role":"system","content":"You have to proofread any sentence
below. You need to fix any spelling and grammar error.You can also fix
the proper nouns. You must not fact check the content.Reply only with
the correct version of the sentence and nothing more. If the sentence is
correct, just reply with the sentence itself, nothing more"},{"role":
"system", "content": "Text context is
music"},{"role":"user","content":"A big thank you to our guitar and base
player"}],"ideal":"A big thank you to our guitar and bass player"}
{"input":[{"role":"system","content":"You have to proofread any sentence
below. You need to fix any spelling and grammar error.You can also fix
the proper nouns. You must not fact check the content.Reply only with
the correct version of the sentence and nothing more. If the sentence is
correct, just reply with the sentence itself, nothing
more"},{"role":"user","content":"This is correct!"}],"ideal":"This is
correct!"}
{"input":[{"role":"system","content":"You have to proofread any sentence
below. You need to fix any spelling and grammar error.You can also fix
the proper nouns. You must not fact check the content.Reply only with
the correct version of the sentence and nothing more. If the sentence is
correct, just reply with the sentence itself, nothing more"},{"role":
"system", "content": "Text context is 20th Century Modernist
Art"},{"role":"user","content":"Pablo Picaso's famuos painitng Guernica
dipicts the atrocities of the Spansh Civil War."}],"ideal":"Pablo
Picasso's famous painting Guernica depicts the atrocities of the Spanish
Civil War."}
{"input":[{"role":"system","content":"You have to proofread any sentence
below. You need to fix any spelling and grammar error.You can also fix
the proper nouns. You must not fact check the content.Reply only with
the correct version of the sentence and nothing more. If the sentence is
correct, just reply with the sentence itself, nothing more"},{"role":
"system", "content": "Text context is
philosophy"},{"role":"user","content":"Nitsche never wrote Der Wille zur
Schmacht. It was his sister Elisabeth Foerster that compiled the work
and gave it an antisemithic tone."}],"ideal":"Nietzsche never wrote Der
Wille zur Macht. It was his sister Elisabeth Förster that compiled the
work and gave it an antisemitic tone."}
{"input":[{"role":"system","content":"You have to proofread any sentence
below. You need to fix any spelling and grammar error.You can also fix
the proper nouns. You must not fact check the content.Reply only with
the correct version of the sentence and nothing more. If the sentence is
correct, just reply with the sentence itself, nothing
more"},{"role":"user","content":"Stop doing this!"}],"ideal":"Stop doing
this!"}

  ```
</details>

---
## [abrinkmann/evals](https://github.com/abrinkmann/evals)@[c0c784fd97...](https://github.com/abrinkmann/evals/commit/c0c784fd978bb2e4bc4b5aef7b0f032fa3b04a75)
#### Tuesday 2023-07-25 12:20:39 by monocle-pastels

[eval] norwegian rhymes (#1248)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

norwegian-rhymes

### Eval description

Check if Norwegian Bokmål words are rhyming 

### What makes this a useful eval?

It's important that GPT understands Norwegian phonetics and language

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This contains multiple cases of most pitfalls when considering what
rhymes in Norwegian.

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [] (Ignore if not submitting code) I have run `pip install pre-commit;
pre-commit install` and have verified that `black`, `isort`, and
`autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You will be given a pair of
words. Determine if they rhyme in Norwegian Bokmål. If they do, reply
Yes. Otherwise, reply No."}, {"role": "user", "content": "avskjed,
beskjed"}], "ideal": "No"}
{"input": [{"role": "system", "content": "You will be given a pair of
words. Determine if they rhyme in Norwegian Bokmål. If they do, reply
Yes. Otherwise, reply No."}, {"role": "user", "content": "led,
beskjed"}], "ideal": "No"}
{"input": [{"role": "system", "content": "You will be given a pair of
words. Determine if they rhyme in Norwegian Bokmål. If they do, reply
Yes. Otherwise, reply No."}, {"role": "user", "content": "nett, vet"}],
"ideal": "No"}
{"input": [{"role": "system", "content": "You will be given a pair of
words. Determine if they rhyme in Norwegian Bokmål. If they do, reply
Yes. Otherwise, reply No."}, {"role": "user", "content": "deg, vei"}],
"ideal": "Yes"}
{"input": [{"role": "system", "content": "You will be given a pair of
words. Determine if they rhyme in Norwegian Bokmål. If they do, reply
Yes. Otherwise, reply No."}, {"role": "user", "content": "huset,
knuse"}], "ideal": "Yes"}
{"input": [{"role": "system", "content": "You will be given a pair of
words. Determine if they rhyme in Norwegian Bokmål. If they do, reply
Yes. Otherwise, reply No."}, {"role": "user", "content": "her, sær"}],
"ideal": "Yes"}
  ```
</details>

---
## [MundagRoki/first-protolo-web](https://github.com/MundagRoki/first-protolo-web)@[4582820148...](https://github.com/MundagRoki/first-protolo-web/commit/45828201489801c1196b815dfdaf92ed7550b3bf)
#### Tuesday 2023-07-25 13:02:25 by Mundag Roki

added js and fixed some bugs

i fucking hate my life

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[7e29b9ef63...](https://github.com/TaleStation/TaleStation/commit/7e29b9ef63fa1674b30e1b3298d7aef8e9c1805b)
#### Tuesday 2023-07-25 13:20:28 by TaleStationBot

[MIRROR] [MDB IGNORE] Adds a new positive quirk, "Spacer Born".  (#6840)

Original PR: https://github.com/tgstation/tgstation/pull/76809
-----
## About The Pull Request

Adds a new 7 point positive quirk, "Spacer Born". Totally not inspired
by The Expanse, don't look at the branch name.

You were born in space, rather than on a planet, so your physiology has
adapted differently.
You are more comfortable in space, and way less comfortable on a planet.

Benefits:
   - You are slightly taller. (No mechanical effect)
   - You take 20% less damage from pressure damage.
   - You take 20% less damage from cold environments. 
- You move 10% faster while floating (NOT drifting, this is zero gravity
movement while beside a wall).
- You drift 20% faster (Drifting through zero gravity, untethered to
anything)
- While in space (z-level-wise, not turf wise), you lose some disgust
overtime.
- While experiencing no-gravity for an extended period of time, you will
start regenerating stamina and reduce stuns at a very low rate.
- If you are assigned to shaft miner (or the map is Icebox), you are
awarded with a 25% wage bonus (hazard pay).

Downsides:
- While on a planet (Yes, this includes Icebox and planetary maps), you
gain gravity sickness:
- Passive accrue disgust (slightly lessened on Icebox) (Capped at low
levels)
      - Choking, after extended periods (disabled on Icebox)
      - Slower movement 
      - Weaker stamina (disabled on Icebox)
- Suffocation from extended periods (disabled on Icebox) (Lungs aren't
adapted)
      - Mood debuff

(Effects not final)

## Why It's Good For The Game

I'd figure I throw my hat in with the Positive Quirk Curse. 

This is a quirk that improves your ability in a niche circumstance (low
gravity / dangerous pressure), with some downsides that are only
generally in effect if you play a few roles (or it's Icebox).

Because of this I think it'll provide an interesting niche, where Spacer
Born engineers are slightly better than their counterparts due to their
origin (moving faster in space without a jetpack, withstanding
pressure). However, at the same time, if the mining outpost sustains
damage and needs repairs... suddenly your buff over your cohorts
disappears, and you have to brave somewhere hostile to your body.

Ultimately, the goal of the quirk is to encourage people to approach
situations a bit differently.
Or take it as a challenge and play shaft miner. 

## Changelog

:cl: Melbert
add: Adds a new 7 point positive quirk, "Spacer Born". You were born in
space, and as a result your body's adapted to life in artificial
gravity, making you much more effective and comfortable in lower
gravity. However, travelling planet-side is quite a chore, especially if
you're assigned to work there.
add: Adds a chemical: Ondansetron, created by Oil + Nitrogen + Oxygen +
Ethanol catalyst. A powerful Antiemetic (lowers disgust).
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [rmellis/HelpUKR-master](https://github.com/rmellis/HelpUKR-master)@[253a0e3612...](https://github.com/rmellis/HelpUKR-master/commit/253a0e3612df7a865a6b4f59c40f9cf71a4d38b9)
#### Tuesday 2023-07-25 13:21:48 by rmellis

Info Box Update for day 518

Simply run this for as long as you can to help flood Russia in the most legal, yet effective way possible 
New targets imported from db1000n:
To keep up with targets we're going to use the db1000n targets direct from their GitHub repository. 
These updates will be daily, so if the db1000n changes, it will probably take a few hours longer for the change to make it here.
Message posted by the IT Army of Ukraine:
In the Ruzzia, data breaches last year surpassed the number of citizens - 188.7 million against 146.4 million. Wondering who they've chosen to blame? Of course, 'those notorious Ukrainian hackers'. So, our very own IT Army of Ukraine got a 'whisper of praise'. We don't mind.

/ *** / 
Просто запускайте це стільки, скільки зможете, щоб допомогти наповнити Росію найбільш законним, але ефективним способом 
Нові цілі, імпортовані з db1000n:
Щоб не відставати від цілей, ми збираємося використовувати цілі db1000n безпосередньо з їхнього сховища GitHub.
Ці оновлення відбуватимуться щодня, тож якщо db1000n зміниться, ймовірно, знадобиться кілька годин більше, перш ніж зміни з’являться тут.
Повідомлення оприлюднило IT Army of Ukraine:
Щоб не відставати від цілей, ми збираємося використовувати цілі db1000n безпосередньо з їхнього сховища GitHub. Ці оновлення відбуватимуться щодня, тож якщо db1000n зміниться, ймовірно, знадобиться кілька годин більше, перш ніж зміни з’являться тут. Повідомлення оприлюднило IT Army of Ukraine:
На росії випадків втечі даних набралося більше, ніж громадян за останній рік - 188,7 млн проти 146,4 млн. Цікаво, кого обрали винуватцями? Звісно, 'відомі українські хакери'. Тож і про нашу IT Army of Ukraine згадали "незлим тихим словом". Ми тільки "за".

---
## [Jolly-66/JollyStation](https://github.com/Jolly-66/JollyStation)@[7941a9bc53...](https://github.com/Jolly-66/JollyStation/commit/7941a9bc537ab51b7fcac8ad579f7601edcccec2)
#### Tuesday 2023-07-25 13:53:11 by TaleStationBot

[MIRROR] [MDB IGNORE] Removes two redundant components (#6916)

Original PR: https://github.com/tgstation/tgstation/pull/76866
-----
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

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Verbina29/HiNoon](https://github.com/Verbina29/HiNoon)@[5e7900623d...](https://github.com/Verbina29/HiNoon/commit/5e7900623d8ca2496b4e12fae376a2a75d15811b)
#### Tuesday 2023-07-25 13:56:09 by Verbina29

ah fuck you packwiz i want the quilt version damnit

---
## [rust-lang-ci/rust](https://github.com/rust-lang-ci/rust)@[4fc6b33474...](https://github.com/rust-lang-ci/rust/commit/4fc6b33474680ba57e10d56371c2c3df91788e26)
#### Tuesday 2023-07-25 14:18:11 by bors

Auto merge of #114011 - RalfJung:place-projection, r=oli-obk

interpret: Unify projections for MPlaceTy, PlaceTy, OpTy

For ~forever, we didn't really have proper shared code for handling projections into those three types. This is mostly because `PlaceTy` projections require `&mut self`: they might have to `force_allocate` to be able to represent a project part-way into a local.

This PR finally fixes that, by enhancing `Place::Local` with an `offset` so that such an optimized place can point into a part of a place without having requiring an in-memory representation. If we later write to that place, we will still do `force_allocate` -- for now we don't have an optimized path in `write_immediate` that would avoid allocation for partial overwrites of immediately stored locals. But in `write_immediate` we have `&mut self` so at least this no longer pollutes all our type signatures.

(Ironically, I seem to distantly remember that many years ago, `Place::Local` *did* have an `offset`, and I removed it to simplify things. I guess I didn't realize why it was so useful... I am also not sure if this was actually used to achieve place projection on `&self` back then.)

The `offset` had type `Option<Size>`, where `None` represent "no projection was applied". This is needed because locals *can* be unsized (when they are arguments) but `Place::Local` cannot store metadata: if the offset is `None`, this refers to the entire local, so we can use the metadata of the local itself (which must be indirect); if a projection gets applied, since the local is indirect, it will turn into a `Place::Ptr`. (Note that even for indirect locals we can have `Place::Local`: when the local appears in MIR, we always start with `Place::Local`, and only check `frame.locals` later. We could eagerly normalize to `Place::Ptr` but I don't think that would actually simplify things much.)

Having done all that, we can finally properly abstract projections: we have a new `Projectable` trait that has the basic methods required for projecting, and then all projection methods are implemented for anything that implements that trait. We can even implement it for `ImmTy`! (Not that we need that, but it seems neat.) The visitor can be greatly simplified; it doesn't need its own trait any more but it can use the `Projectable` trait. We also don't need the separate `Mut` visitor any more; that was required only to reflect that projections on `PlaceTy` needed `&mut self`.

It is possible that there are some more `&mut self` that can now become `&self`... I guess we'll notice that over time.

r? `@oli-obk`

---
## [Sidragithb/Smile-face-in-python](https://github.com/Sidragithb/Smile-face-in-python)@[2a286b965b...](https://github.com/Sidragithb/Smile-face-in-python/commit/2a286b965beda9a0a5f8caa507c2dc342f6ae3dd)
#### Tuesday 2023-07-25 14:19:08 by Sidragithb

Smile face project in python

Sure! A smiley face, also known as a smiley or emoticon, is a simple and iconic representation of a smiling human face. It is often used in written communication to convey positive emotions or to indicate happiness, joy, or friendliness. The smiley face is a popular way to add a touch of emotion and express feelings in text-based messages, emails, and online conversations.

Here's a description of a typical smiley face:

```
:-)
```

In this representation:

1. The colon `:` represents the eyes.
2. The hyphen `-` or equal sign `=` represents the nose (optional, some smileys omit the nose).
3. The closing parenthesis `)` represents the smiling mouth.

When viewed sideways, the colon and closing parenthesis combine to form the appearance of a smiling face, with the eyes on the left, the nose (if included) in the middle, and the mouth on the right.

Variations of smiley faces also exist, such as winking smileys, sad smileys, and many others, often created by adding additional characters or modifying the arrangement of the eyes, nose, and mouth. For example:

```
;-) - Winking smiley
:-D - Big grin or laughter
:-P - Playful or sticking out the tongue
:-O - Surprised smiley
:-( - Sad or frowning face
```

The smiley face has become an essential part of modern digital communication and plays a significant role in expressing emotions, humor, and overall mood in various online interactions.

---
## [Kingdread/watson-worktime](https://github.com/Kingdread/watson-worktime)@[df7107f791...](https://github.com/Kingdread/watson-worktime/commit/df7107f7919a87fdfd2775df1a0ea64dd5c4d4e1)
#### Tuesday 2023-07-25 14:20:26 by Daniel Schadt

add (preliminary) support for ignored days

I'm not too happy about the duplication of code and ideas between
vacation days and ignored days, but I kinda needed the feature myself so
this is a hacky, hopefully temporary solution.

Ideally, maybe we can combine all sorts of ignored days in one command
(watson-worktime ignore --vacation ..., watson-worktime ignore --sick
...). The aliases `watson-worktime vacation add` could stay. We can then
define rules which ignored days are still counted in overtime (overtime
during vacation? count it! overtime during ignored days? ignore it!).

In addition, we can combine the format to use a single file only, and we
can make the different ignore "modes" exclusive (a day is either a
vacation day or a sick day, not both at the same time).

Fractional vacation/sick days might be a bit hard then, though. We'll
see.

Anyway, for now it works \o/

---
## [sdddddf80/Hbm-s-Nuclear-Tech-GIT](https://github.com/sdddddf80/Hbm-s-Nuclear-Tech-GIT)@[b443c3449d...](https://github.com/sdddddf80/Hbm-s-Nuclear-Tech-GIT/commit/b443c3449d37db0017d86a1fe71cf92de3da026f)
#### Tuesday 2023-07-25 14:32:40 by Bob

fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you

---
## [poire-z/koreader-base](https://github.com/poire-z/koreader-base)@[b0f7e99845...](https://github.com/poire-z/koreader-base/commit/b0f7e99845b16fc4176d3d29e4ffc258baa53cca)
#### Tuesday 2023-07-25 14:35:41 by NiLuJe

Build: RPATH & escaping cleanup (#1638)

* Stop everything from including crappy build-time rpaths into binaries (lookin' at you, libtool).
* Enforce a set of DT_RPATH on everything we build to ensure we prefer our own libs over the system's.
* Do so via an ld include file, in order to go through all the buildsystem bullshit in order to defeat potential escaping issues.
* In the same vein, rework how we escape things in both makefiles and CMake files, in order to limit the interaction and/or dependency on shell escaping and/or globbing.
* Enforce DT_RPATH over DT_RUNPATH, because it gets honored for transitive dependencies, which will avoid some hilariously stupid things from happening once we get rid of LD_LIBRARY_PATH, which this moves also allows us to do.

Many thanks to @benoit-pierre for his insight, testing and reviews, this would have been way clunkier without his input ;).

---------

Co-authored-by: Benoit Pierre <benoit.pierre@gmail.com>

---
## [ariel-miculas/linux](https://github.com/ariel-miculas/linux)@[9471f1f2f5...](https://github.com/ariel-miculas/linux/commit/9471f1f2f50282b9e8f59198ec6bb738b4ccc009)
#### Tuesday 2023-07-25 14:42:37 by Linus Torvalds

Merge branch 'expand-stack'

This modifies our user mode stack expansion code to always take the
mmap_lock for writing before modifying the VM layout.

It's actually something we always technically should have done, but
because we didn't strictly need it, we were being lazy ("opportunistic"
sounds so much better, doesn't it?) about things, and had this hack in
place where we would extend the stack vma in-place without doing the
proper locking.

And it worked fine.  We just needed to change vm_start (or, in the case
of grow-up stacks, vm_end) and together with some special ad-hoc locking
using the anon_vma lock and the mm->page_table_lock, it all was fairly
straightforward.

That is, it was all fine until Ruihan Li pointed out that now that the
vma layout uses the maple tree code, we *really* don't just change
vm_start and vm_end any more, and the locking really is broken.  Oops.

It's not actually all _that_ horrible to fix this once and for all, and
do proper locking, but it's a bit painful.  We have basically three
different cases of stack expansion, and they all work just a bit
differently:

 - the common and obvious case is the page fault handling. It's actually
   fairly simple and straightforward, except for the fact that we have
   something like 24 different versions of it, and you end up in a maze
   of twisty little passages, all alike.

 - the simplest case is the execve() code that creates a new stack.
   There are no real locking concerns because it's all in a private new
   VM that hasn't been exposed to anybody, but lockdep still can end up
   unhappy if you get it wrong.

 - and finally, we have GUP and page pinning, which shouldn't really be
   expanding the stack in the first place, but in addition to execve()
   we also use it for ptrace(). And debuggers do want to possibly access
   memory under the stack pointer and thus need to be able to expand the
   stack as a special case.

None of these cases are exactly complicated, but the page fault case in
particular is just repeated slightly differently many many times.  And
ia64 in particular has a fairly complicated situation where you can have
both a regular grow-down stack _and_ a special grow-up stack for the
register backing store.

So to make this slightly more manageable, the bulk of this series is to
first create a helper function for the most common page fault case, and
convert all the straightforward architectures to it.

Thus the new 'lock_mm_and_find_vma()' helper function, which ends up
being used by x86, arm, powerpc, mips, riscv, alpha, arc, csky, hexagon,
loongarch, nios2, sh, sparc32, and xtensa.  So we not only convert more
than half the architectures, we now have more shared code and avoid some
of those twisty little passages.

And largely due to this common helper function, the full diffstat of
this series ends up deleting more lines than it adds.

That still leaves eight architectures (ia64, m68k, microblaze, openrisc,
parisc, s390, sparc64 and um) that end up doing 'expand_stack()'
manually because they are doing something slightly different from the
normal pattern.  Along with the couple of special cases in execve() and
GUP.

So there's a couple of patches that first create 'locked' helper
versions of the stack expansion functions, so that there's a obvious
path forward in the conversion.  The execve() case is then actually
pretty simple, and is a nice cleanup from our old "grow-up stackls are
special, because at execve time even they grow down".

The #ifdef CONFIG_STACK_GROWSUP in that code just goes away, because
it's just more straightforward to write out the stack expansion there
manually, instead od having get_user_pages_remote() do it for us in some
situations but not others and have to worry about locking rules for GUP.

And the final step is then to just convert the remaining odd cases to a
new world order where 'expand_stack()' is called with the mmap_lock held
for reading, but where it might drop it and upgrade it to a write, only
to return with it held for reading (in the success case) or with it
completely dropped (in the failure case).

In the process, we remove all the stack expansion from GUP (where
dropping the lock wouldn't be ok without special rules anyway), and add
it in manually to __access_remote_vm() for ptrace().

Thanks to Adrian Glaubitz and Frank Scheiner who tested the ia64 cases.
Everything else here felt pretty straightforward, but the ia64 rules for
stack expansion are really quite odd and very different from everything
else.  Also thanks to Vegard Nossum who caught me getting one of those
odd conditions entirely the wrong way around.

Anyway, I think I want to actually move all the stack expansion code to
a whole new file of its own, rather than have it split up between
mm/mmap.c and mm/memory.c, but since this will have to be backported to
the initial maple tree vma introduction anyway, I tried to keep the
patches _fairly_ minimal.

Also, while I don't think it's valid to expand the stack from GUP, the
final patch in here is a "warn if some crazy GUP user wants to try to
expand the stack" patch.  That one will be reverted before the final
release, but it's left to catch any odd cases during the merge window
and release candidates.

Reported-by: Ruihan Li <lrh2000@pku.edu.cn>

* branch 'expand-stack':
  gup: add warning if some caller would seem to want stack expansion
  mm: always expand the stack with the mmap write lock held
  execve: expand new process stack manually ahead of time
  mm: make find_extend_vma() fail if write lock not held
  powerpc/mm: convert coprocessor fault to lock_mm_and_find_vma()
  mm/fault: convert remaining simple cases to lock_mm_and_find_vma()
  arm/mm: Convert to using lock_mm_and_find_vma()
  riscv/mm: Convert to using lock_mm_and_find_vma()
  mips/mm: Convert to using lock_mm_and_find_vma()
  powerpc/mm: Convert to using lock_mm_and_find_vma()
  arm64/mm: Convert to using lock_mm_and_find_vma()
  mm: make the page fault mmap locking killable
  mm: introduce new 'lock_mm_and_find_vma()' page fault helper

---
## [vdaular-dev/linksfordevs](https://github.com/vdaular-dev/linksfordevs)@[f6c3bc93ba...](https://github.com/vdaular-dev/linksfordevs/commit/f6c3bc93baea5d39d9e8345dd0d6d6ee9f674560)
#### Tuesday 2023-07-25 15:36:24 by Ben Dornis

Updating: 7/24/2023 11:00:00 PM

 1. Added: Introduction to Pocket: obfuscator for MBA expressions
    (https://nicolo.dev/en/blog/introduction-pocket-obfuscator/)
 2. Added: Is software getting worse?
    (https://blog.ploeh.dk/2023/07/24/is-software-getting-worse/)
 3. Added: An algorithm for shuffling playlists
    (https://ruudvanasseldonk.com/2023/an-algorithm-for-shuffling-playlists)
 4. Added: Building an E-Ink Joke of the Day Fridge Magnet · Alex Meub
    (https://alexmeub.com/building-an-eink-joke-fridge-magnet/)
 5. Added: You should write your own programming language
    (https://xnacly.me/posts/2023/write-your-own-programming-language/)
 6. Added: Tek scope screen capture with Bash - Andrej's blog
    (https://andrejradovic.com/blog/tek-tds2014-screen-grab/)
 7. Added: Mongo Read Optimisation: Write Concern
    (https://sreevenkat.com/posts/mongo-read-optimisation)
 8. Added: Thriving in the dynamically type-checked hell scape of Clojure
    (https://blog.janetacarr.com/thriving-in-the-dynamically-type-checked-hell-scape-of-clojure/)
 9. Added: I made a new track for teaching swing
    (https://www.ethanhein.com/wp/2023/i-made-a-new-track-for-teaching-swing/)
10. Added: Do films directed by women have more women in the cast?
    (https://stephenfollows.com/do-films-directed-by-women-have-more-women-in-the-cast/)
11. Added: Sharing encrypted data over short-form mediums
    (https://notes.willhackett.com/share-encrypted-short-form-data/)
12. Added: RSA
    (https://joe-ferrara.github.io/2023/07/23/rsa.html)
13. Added: On .NET Live - Lunr Core: Simple search for all .NET apps
    (https://youtube.com/watch?v=7DosTpW0wgM)
14. Added:  What it’s like to be married to a dying man
    (https://jakeseliger.com/2023/07/24/what-its-like-to-be-married-to-a-dying-man/)
15. Added: Commoditized Social Networking
    (https://philip-trauner.me/blog/post/commoditized-social-networking)
16. Added: Why functional programming?
    (https://ianchanning.wordpress.com/2023/07/24/why-functional-programming/)
17. Added: How to choose the target for a migration from RPG - Strumenta
    (https://tomassetti.me/how-to-choose-the-target-for-a-migration-from-rpg/)

Generation took: 00:09:48.2194886
 Maintenance update - cleaning up homepage and feed

---
## [PostHog/posthog.com](https://github.com/PostHog/posthog.com)@[c6097ab08f...](https://github.com/PostHog/posthog.com/commit/c6097ab08fc4708a393c4f725ef3d86816447a20)
#### Tuesday 2023-07-25 16:03:46 by Charles Cook

Small tweak suggestions to modern data stack article (#5729)

* Small tweaks

Few small tweaks, feel free to ignore obv:

- Removed the tl;dr in intro as it was repetitive and felt redundant (it's summarizing 3 sentences)
- Removed more air quotes around modern data stack - if you're talking to engineers and call it 'modern data stack' you sound a bit 'how do you do, fellow kids'
- Removed link to our CDP docs because we don't _really_ have a CDP product yet
- Micro changes to flow

In general I think there are still slightly too many links in here that would take people away from the page (we don't need to link to every single relevant article we've written on the topic, especially as we have a Further reading section), but I'll leave that to you to decide!

I wonder if around line 95 there should be a break with a new title called 'So what's the problem' or something - I had to re-read the article to really get the crux of what the burning problem is here besides 'it's a bit complicated'. The gap that is created between (product?) engineers and the data they use is super valuable, but I think a bit buried.  

(Btw sorry to be very nit-picky after it's already been published - ended up re-reading a few times as I think this is awesome Twitter content I'm going to pilfer...)

* Update contents/blog/modern-data-stack-sucks.md

Co-authored-by: Ian Vanagas <34755028+ivanagas@users.noreply.github.com>

---------

Co-authored-by: Ian Vanagas <34755028+ivanagas@users.noreply.github.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[3b58d606a1...](https://github.com/treckstar/yolo-octo-hipster/commit/3b58d606a12143358b61c3466cb47406634162cb)
#### Tuesday 2023-07-25 16:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [cockroachdb/cdc-sink](https://github.com/cockroachdb/cdc-sink)@[447c652c5b...](https://github.com/cockroachdb/cdc-sink/commit/447c652c5b3b1318947830c94b315f7decdb4ddb)
#### Tuesday 2023-07-25 17:13:36 by Bob Vawter

sinktest: Separate source from target test cade

This PR separates test code that depends on a "source" database from the
existing target database. In the past, the source, staging, and target database
were all the same CockroachDB instance, so there was never a need to make this
distinction in the test code. This change enables non-CockroachDB targets to be
tested.

The source, staging, and target setup in this PR would also allow us to move
cdc-sink in a direction where we test against older versions of CockroachDB as
a source, but we only verify that the staging and target behaviors work on more
recent versions.

Summary of changes:
- `sinktest.base` looks for three environment variables to determine what
  database(s) to connect to.
- Each of source, staging, and test have distinct table schemas for each test.
  These are available through new injection types, `sinktest.SourceSchema` and
  `sinktest.TargetSchema`. The `TestDB` injection point is removed.
- `types.StagingDB` is renamed to `StagingSchema` for consistency.
- `types.SourcePool` is added for tests, but it could be used if we add the
  proposed S4 (stupid, simple SELECT *) frontend.
- The Fixture.CreateTable method is bifurcated into CreateSourceTable and
  CreateTargetTable. These return types that are parameterized with their
  pool-ness, so the typesystem gives us a hand in avoiding cases where we might
  cross the streams.
- The Golang workflow adds a test-matrix entry to test completely separated
  source, staging, and target databases. The docker container logs are also
  captured, as this was necessary to troubleshoot some startup issues.

---
## [AcunaTomas/Space-Opera](https://github.com/AcunaTomas/Space-Opera)@[cc7b335d68...](https://github.com/AcunaTomas/Space-Opera/commit/cc7b335d6848eeef911a45b422becfcafe0818f3)
#### Tuesday 2023-07-25 17:14:22 by @tomas.acuna

goD FUCKING DAMMIT HOW MANY TIMES DO I HAVE TO FIX THIS GODDAMNED SEQUENCE

---
## [ShambaC/CU-CS-SEM-6-Scripts](https://github.com/ShambaC/CU-CS-SEM-6-Scripts)@[651631bdd1...](https://github.com/ShambaC/CU-CS-SEM-6-Scripts/commit/651631bdd194e2e583f21b1e0f0c85548c10232b)
#### Tuesday 2023-07-25 18:06:23 by Shamba Chowdhury

Added list operations file

A list of worries and troubles have been added.
Prolog sucks so god damn much that I don't have any energy to make funny commit messages.
So, laugh at this unfunny commit 🔫

---
## [sourcegraph/sourcegraph](https://github.com/sourcegraph/sourcegraph)@[340b0dea25...](https://github.com/sourcegraph/sourcegraph/commit/340b0dea25f073119d0506b8dd3c6228516cf9c4)
#### Tuesday 2023-07-25 18:08:38 by David Veszelovszki

JetBrains: Fix dotcom logging issue (#54885)

We didn't convert an object to a string → our Go backend rejected it →
got no logs on Dotcom :bang-head:

Currently, I'm getting back a bunch of 429 – Too Many Requests responses
from Dotcom for some reason, but the problem should be solved.

I feel sorry about losing all those logs, it really sucks. We were too
much in a rush and didn't test this properly. Totally my mistake.

## Test plan

Tested it with the built-in-debugger and by copying the requests to our
GraphQL API console.

---
## [jhnc-oss/NetworkManager](https://github.com/jhnc-oss/NetworkManager)@[0df304b790...](https://github.com/jhnc-oss/NetworkManager/commit/0df304b790815b229b504df9b2bec991e0118fbd)
#### Tuesday 2023-07-25 18:17:26 by Beniamino Galvani

Revert "platform: always reconfigure IP routes even if removed externally"

The change in behavior introduced by the patch departs from the policy
that NM had for long time of trying not to interfere with user
modifications. This seems a fundamental aspect of how NM works and
indeed we got already one report:

https://bugzilla.redhat.com/show_bug.cgi?id=2218866

of a user that was affected by the change. The specific case is about
routes from DHCP, but also static routes are affected. When a user
removes the route added by NM, NM now can add it back at any time.

Changing behavior is bad, it causes pain for users and for people who
need to support them. However, if the new behavior provides clear
advantages to users, that might be ok. This doesn't seem the case in
my opinion. Commit 7ca95cee describes a couple of scenarios:

> - kernel can automatically remove routes. For example, deleting an
>   IPv4 address that is the prefsrc of a route, will cause kernel to
>   delete that route. Sure, we may be unable to re-configure the
>   route at this moment, but we shouldn't remember indefinitely that
>   the route is supposed to be absent. Rather, we should re-add it
>   when possible

> - kernel is a pain with validating consistencies of routes. For
>   example, when a route has a nexthop gateway, then the gateway must
>   be onlink (directly reachable), or kernel refuses to add it with
>   "Nexthop has invalid gateway". Of course, when removing the onlink
>   route kernel is fine leaving the gateway route behind, which it
>   would otherwise refuse to add.
>   Anyway. Such interdependencies for when kernel rejects adding a
>   route with "Nexthop has invalid gateway" are non-trivial. We try
>   to work around that by always adding the necessary onlink
>   routes. See nm_l3_config_data_add_dependent_onlink_routes(). But
>   if the user externally removed the dependent onlink route, and
>   NetworkManager remembers to not re-adding it, then the efforts
>   from nm_l3_config_data_add_dependent_onlink_routes() are
>   ignored. This causes ripple effects and NetworkManager will also
>   be unable to add the nexthop route.

Kernel usually removes addresses as consequence of user actions. If
not (e.g. DHCP lease expiring) we have solutions in place for that to
re-add the route.

If the route removal is the consequence of a user action, then the
user must do something to undo it. For example, if the user removes an
address on the same interface, a route using the address as prefsrc
will be deleted. If the user wants it back, it must be re-added
manually together with the address; I don't see any problem with this.

The prefsrc address could be on another interface; in such case by
simply deactivating the connection providing the address, a dependent
route could be removed on another interface and never readded. This
doesn't look as a setup that anybody would use; in case we need to
support it, it is better to find alternative solutions.

So, my opinion is that the change in behavior potentially breaks many
users and doesn't bring clear advantages. Therefore, restore the old
behavior.

This reverts commit 7ca95cee15b32af2452aaf4a165eb5c634fba132.

Revert conflicts:

- the following code was removed from _obj_states_sync_filter() in
  nm-l3cfg.c because the mechanism to set temporarily-unavailable
  routes was changed in 1feaf427d2bcbf5b618bbe38a82d76cfe621d203
  ('platform: rework handling of failed routes during
  nm_platform_ip_route_sync()'), and so
  `os_temporary_not_available_timestamp_msec` no longer exists:

    if (obj_state->os_temporary_not_available_timestamp_msec > 0) {
        /* we currently try to configure this address (but failed earlier).
         * Definitely retry. */
        return TRUE;
    }

---
## [Ua-Gi-Oh/UA_EDO](https://github.com/Ua-Gi-Oh/UA_EDO)@[d4740966a8...](https://github.com/Ua-Gi-Oh/UA_EDO/commit/d4740966a8effeac706635326b06d4825224de3f)
#### Tuesday 2023-07-25 19:04:55 by Ua-Gi-Oh

Перекладені карти

1 - Deep-Space Cruiser IX
2 - Dimension Fortress Weapon
3 - Dark Requiem Xyz Dragon
4 - Grand Horn of Heaven
5 - Divine Dragon Knight Felgrand
6 - Vylon Segment 
7 - Brotherhood of the Fire Fist - Spirit
8 - Spell Purification 
9 - Viper's Grudge
10 - Ultimaya Tzolkin 
11 - The Big March of Animals 
12 - PSY-Framegear Epsilon 
13 - Malefic Cyber End Dragon
14 - Malefic Blue-Eyes White Dragon 
15 - Malefic Stardust Dragon
16 - Malefic Red-Eyes Black Dragon 
17 - Beetrooper Fly & Sting
18 - Wind-Up Zenmaintenance
19 - Fiendish Portrait
20 - Nekogal #1
21 - Doomkaiser Dragon/Assault Mode 
22 - Fuh-Rin-Ka-Zan 
23 - Uraby 
24 - The Eye of Timaeus
25 - Transcicada
26 - Moult Token 
27 - Centrifugal Field 
28 - Sealing Ceremony of Mokuton 
29 - Dark Coffin 
30 - Super Quantal Union - Magnaformation
31 - Toy Knight
32 - Shadow of the Six Samurai - Shien 
33 - Heroic Challenger - Thousand Blades
34 - Wattcine 
35 - Overdrive Teleporter 
36 - Instant Fusion
37 - Scar of the Vendread

Не потребує перекладу - Fusionist

---
## [Kitsunemitsu/lobotomy-corp13](https://github.com/Kitsunemitsu/lobotomy-corp13)@[171b1478f9...](https://github.com/Kitsunemitsu/lobotomy-corp13/commit/171b1478f9d01a40841ca0bb131394fe8a2039b2)
#### Tuesday 2023-07-25 19:07:58 by vampirebat74

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
## [git-for-windows/git](https://github.com/git-for-windows/git)@[aa253cce33...](https://github.com/git-for-windows/git/commit/aa253cce3331a0a5f91c174228b5a3b59060859b)
#### Tuesday 2023-07-25 20:26:32 by Johannes Schindelin

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

---
## [vg-mjg/mjg-repo](https://github.com/vg-mjg/mjg-repo)@[84ce18599c...](https://github.com/vg-mjg/mjg-repo/commit/84ce18599c517e48e6f4d9a273f4eb6ad4cf3af6)
#### Tuesday 2023-07-25 20:51:19 by Sharmayu Mirica

majsoul; shitcoder's autism fix

holy fucking autist

---
## [ihatethisengine/cmss13](https://github.com/ihatethisengine/cmss13)@[1d28964d37...](https://github.com/ihatethisengine/cmss13/commit/1d28964d37f9b95773580cca3471a2a4f5c03eb0)
#### Tuesday 2023-07-25 22:41:57 by naut

New blood bags (#3961)

# About the pull request

Since we're putting so much emphasis on blood bags lately, I figured I
might as well do my part as spriter and add actual _labels_ to the
things so you can tell what they are at a glance. Also overhauled the
system to use overlays and underlays instead of the cursed
`full/half/empty` thing that it had going beforehand.

# Explain why it's good for the game

You now no longer have to manually inspect blood bags to tell what type
they are! Rejoice.

# Testing Photographs and Procedure
<img width="251" alt="image"
src="https://github.com/cmss13-devs/cmss13/assets/55491249/c4424ec3-bfe6-4d58-8915-595b468a7606">

_Blood bags in action. Sort of. Yes, they actually change color now._

<img width="571" alt="image"
src="https://github.com/cmss13-devs/cmss13/assets/55491249/3b478c65-54b9-4321-bf02-dcfacaf1ad23">

_Icon states! Also sprinkled in some yet-unused labels for future
use(TM). AB types are here, too, because I forgot they weren't in the
game._
# Changelog

:cl: nauticall
imageadd: Resprited blood bags to look nicer and use proper a proper
overlay/underlay system. Their types are also now distinguishable at a
glance.
code: Reworked the way blood bag sprites work behind the scenes to use
the overlay/underlay system.
/:cl:

---

