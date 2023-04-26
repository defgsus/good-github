## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-04-25](docs/good-messages/2023/2023-04-25.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,143,002 were push events containing 3,308,415 commit messages that amount to 262,114,907 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 62 messages:


## [norsvenska/tgstation](https://github.com/norsvenska/tgstation)@[3fdd716da5...](https://github.com/norsvenska/tgstation/commit/3fdd716da5bfd2aab2be37489b4ac39f4be7e632)
#### Tuesday 2023-04-25 00:08:30 by Cheshify

Tcomms Soundloop Comes From One Source And Is Less Awful (#74908)

## About The Pull Request

The ``soundloop/server`` now only comes from the server hub, so it
doesn't have stacking audio sources. The sound has been made more
uniform when up close, but is overall quieter. Additionally, all the
files have been run through a low pass filter to remove the highest of
it's pitches.
## Why It's Good For The Game

I'm sick of not wanting to be around telecomms because of how bad every
single machine sounds. Now, things are significantly easier on the ear,
quieter, more uniform, and better for everyone's sanity. I asked the
maintainers in the coding channel if I could just remove it and they
said no.

I can't get a video recording, I've tried with win+G, OBS, and sharex
and it's just fucked.
## Changelog
:cl:
qol: telecomms is quieter and less ear-damaging.
sound: modified tcomms sound to remove high-tones.
fix: the telecomms sound only comes from the server hub machine.
/:cl:

---------

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [norsvenska/tgstation](https://github.com/norsvenska/tgstation)@[43473a4dac...](https://github.com/norsvenska/tgstation/commit/43473a4dac07c40faed45808b61b9c6de46ffcb6)
#### Tuesday 2023-04-25 00:08:30 by san7890

Turns Deer into Basic Mob - They Freeze At The Sight of Vehicles (#74784)

## About The Pull Request

deers only show up in the BEPIS but i decided that they would be easy
enough to turn into a basic mob (they were). it was so easy in fact that
i decided to dip my toes into coding AI behavior, and made them freeze
up whenever they see a vehicle. this required a lot of code in a bunch
of places that i was quite unfamiliar with before starting this project,
so do let me know if i glonked up anywhere and i can work on smoothing
it out.
## Why It's Good For The Game

one less simple animal on the list. deers staring at headlights is
pretty cool i think, neato interaction for when you do get them beyond
the joke the bepis makes

i'm also amenable to dropping the whole "deer in headlights" code if you
don't like that for w/e reason- just wanted to make them basic at the
very least
## Changelog
:cl:
add: If you ever happen upon a wild deer, try not to ride your fancy
vehicles too close to it as it'll freeze up like a... you know where I'm
going with this.
/:cl:

---------

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [acsone/odoo](https://github.com/acsone/odoo)@[cb1388ed9e...](https://github.com/acsone/odoo/commit/cb1388ed9e64ced4e0d85cf5778192dfbdfd5995)
#### Tuesday 2023-04-25 00:27:56 by Jeremy Kersten

[ADD] website_cf_turnstile: add cloudflare turnstile support

This module allows to add secret key to add the turnstile captcha on
each snippet website_form.

Cloudflare Turnstile
--------------------
A friendly, free CAPTCHA replacement
Turnstile delivers frustration-free, CAPTCHA-free web experiences to
website visitors.
Turnstile stops abuse and confirms visitors are real without the data
privacy concerns or awful UX that CAPTCHAs thrust on users.

closes odoo/odoo#119246

X-original-commit: 4aca39a533e9d41f5f452f36a1ffc001f586b4f4
Signed-off-by: Jérémy Kersten <jke@odoo.com>

---
## [NewyearnewmeUwu/cmss13](https://github.com/NewyearnewmeUwu/cmss13)@[9df26f6a8b...](https://github.com/NewyearnewmeUwu/cmss13/commit/9df26f6a8bf397df29e1bff4b5e777414bd1cc44)
#### Tuesday 2023-04-25 00:30:27 by riot

DD updates (#2786)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

DD hasn't been touched in a while, and is kind of bad against preds,
tries to fix this to the best my my ability with the below changes.

1. Makes the M1911 more accurate
2. Makes DD armor cover arms and legs, improves its bullet and explosive
resistance
3. ERT Medical Pouch now contains the basic 3 injectors(bic, kelo,
tram), an emergency injector, a splint, and a bandage
4. DD now all have max endurance skill
5. M60 is now full auto, does more damage, and is more accurate
6. DD Minigun(ol painless) now has an integrated magharn
7. M60 now has the same box changing mechanic that smartgun has.
8. Adds 2 new guns(technically 1, or maybe 1.5), the XM177 and M16
Grenadier(an M16A1/2 with an M203 attached)
9. Adds an M203 grenade launcher, single grenade, no IFF, high range
with scope, only fits on M16 grenadier
10. Adds 3 new impact grenade types, only DD have them currently.
11. Adds HE impact grenade, impacts in a cone radius with an HE
explosion.
12. Adds an incendiary impact grenade, impacts in the same pattern as
HIDP, napalm.
13. Adds an impact buckshot grenade, pure vietnam vibes, shoots 10 bits
of additional buckshot that also slow.
14. DD now have MDs tuned to their own IFF.
15. DD are now equipped with XM177s for the medic, Dutch, and
flamethrower operator
16. DD riflemen have a 60% chance for an M16A1, 30% chance for an M16
Grenadier, and 10% chance for an M60.
17. Removes the M60 from black market
18. Moves DD presets to their own standalone folder, and removes the
/fun/ from their typepaths.
19. Changes CLF crashed ship M60 to a MAR50
20. Adds sprites for M203, XM177, M16 Grenadier
21. DD spawn with a lucky pack and a zippo in their helmet.


# Explain why it's good for the game

Dutch's Dozen is a bit outdated, and light on content, gives them some
love.
Removes gear that doesn't fit in BM from BM, also I buffed the gear too
so balance concerns.

1. An unwielded rifle(M41A), had more accuracy than a wielded M1911,
would do this for other pistols too but out of scope as DD only use
M1911
2. They were incredibly easy to kill via leg/arm aiming, as no armor,
HPCs instakilled them(DD are default dishonorable), and FF did insane
damage as they all had high AP 40 damage rifles.
3. ERT medical pouch was worse than normal med-pouch, DD use this too.
4. Was intended, survivor endurance skill nerf effected this too as the
same define was used for both as a shortcut
5. M60 underpreformed, makes it better.
6. Dropping Ol' Painless over and over sucks.
7. Unique realistic mechanic for the M60, makes it more interactive
8. Unique guns, only DD get them, also the XM177 is my favorite gun of
all time I love it 😊
9. Unique UGL for M16 Grenadier, designed to work directly with the
sprite, as its integrated and only fits on it.
10. Grenades for DD to have a better chance against preds, riflemen have
a 30% chance of spawning with M16 GL.
11. Made for a stun, team gameplay for DD.
12. Area denial.
13. Vietnam Vibes, support tool cause it does jack shit damage.
14. DD couldn't tell friend from foe
15. (AWESOME) Carbine for Dutch, makes sense for the support and members
of the team to have carbines instead of rifles
16. Variance within DD team, all 3 of the guns are good, GL is a support
tool, M60 as an ambush(also its The Pig), A1 is normal
17. M60 doesn't fit thematically, and is too powerful.
18. Easier access, they don't fit in the fun file
19. Buffed M60, MAR50 fits more there anyway.
20. Sprites for things I added.
21. Its cool.

# Testing Photographs and Procedure


![image](https://user-images.githubusercontent.com/103988604/223497128-7f485e32-07cd-49dc-b7b0-d04ce08b3042.png)


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
add: DD spawn with a lucky strike pack and a zippo in their helmet.
add: M60 now has the box changing mechanic that smartgun has.
add: Adds an M16 grenadier, with attached M203, also adds M203 grenade
launcher and impact shells for it, only DD have it
add: Adds a new M16 variant, the XM177E2 Carbine, only DD have it
add: Dutch M16s now are marked as A1s, and use the preexisting M16A1
sprite instead.
add: Dutch's Dozen are now equipped with an XM177 for Dutch, the medic,
and the flamethrower operator
add: Dutch's Dozen riflemen now have a 60% chance to have an M16A1, 30%
chance for an M16 with M203 UGL, and 10% chance for an M60 GPMG
del: M60 has been removed from the black market
balance: DD minigun now has an integrated magharn.
balance: M1911 is slightly more accurate.
balance: ERT Medical Pouch now contains the 4 basic EZ injectors and a
gauze.
balance: DD armor now has a greater explosive protection and covers the
arms and legs.
balance: M60 is now full auto, does more damage, and is more accurate.
code: Moved Dutch's Dozen presets to their own standalone folder
spellcheck: DD spawn text now correctly says the Yautja mask is on
Dutch's face.
fix: DD Motion Detectors no longer pick themselves up.
fix: DD now all have max endurance skill
imageadd: Adds sprites for M203, M203 shells, XM177, and M16 Grenadier
Variant
maptweak: LV624 Crashed CLF ship insert M60 has been replaced with a
MAR50
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: Zonespace <41448081+Zonespace27@users.noreply.github.com>
Co-authored-by: morrowwolf <darthbane97@gmail.com>

---
## [CharlesWedge/Citadel-Station-13-RP](https://github.com/CharlesWedge/Citadel-Station-13-RP)@[9c8abee554...](https://github.com/CharlesWedge/Citadel-Station-13-RP/commit/9c8abee5540f17951b1947a212b80521f1b36300)
#### Tuesday 2023-04-25 00:34:42 by IrkallaEpsilon

Matterforge Recipe expansion (#5168)

## About The Pull Request

This PR adds a few more matterforge recipes, some of stupidly high
difficulty and pointless rewards if miners are doing their job (looking
at you steel to gold), some of more usefulness (gold to plat, plat to
osmium). All require different temperature and energy ranges so they
cannot be rushed thoroughly. Not much thought was put into realism but
eh who cares, the matterforge is a cool thing ingame and its fun to use.
Some temperatures ranges (Steel to gold) are very narrow hence the use
of a gyrotron would be needed to get the most out of it. Or precise
heating (temperature can be raised to exorbitant amounts to prevent
heater cheese). This also would allow for Research to collab with cargo
for exports specially if dynamic prices ever come. In particular looking
at the gold to plat transmutation here. Plat can be exported by cargo in
which cargo can order more shit from.

I aint a good coder else I would add specific atmospheric conditions
needed, not just temperature (e.g. N2O must be present).
Reminded me a bit of TGs gas reactions but less gamy. 

## Why It's Good For The Game

More Matterforge recipes. Most relatively pointless and niche, some
allow science to give cargo something to sell, others can help with
theres an overabundance of Plat due to new miners. Mostly just giving
some extra uses for the forge. Oh and an alternative way to get plasteel
while sacrificing phoron sheets. Also bragging rights of effectively
turning iron (and carbon) into gold at specific temperatures and energy
levels on the particle focus.

A proper coder should check if these recipes are fine. Its 2:30 AM and I
thought this would just be neat.

## Changelog

:cl:
add: Various matterforge recipes
/:cl:

---
## [CharlesWedge/Citadel-Station-13-RP](https://github.com/CharlesWedge/Citadel-Station-13-RP)@[d261466765...](https://github.com/CharlesWedge/Citadel-Station-13-RP/commit/d2614667654c0e35b2c906971ca94ece9e7b8629)
#### Tuesday 2023-04-25 00:34:42 by IrkallaEpsilon

Scattershot nerfs (#5175)

Sniper laser was tame.

## About The Pull Request

This is bullshit. Splurting out 180 damage with high AP with no delay is
not okay. Its as bullshit as most FCU we had. Mainly removed scatter on
high powered lasers and bloody stuns so the scatter lense may stay for
the mining tool (as there is no way to increase firerate on a
projectile.

## Why It's Good For The Game

Ever got hit at close range by the particle defender on main? Yeah that
is not fun.

## Changelog
:cl:
balance: Scattershot on high powered weapons nerfed. Heavy laser and
laser cannon beam and electrode now wont create submunitions. Stun beam
submunition count lowered.
/:cl:

---
## [CharlesWedge/Citadel-Station-13-RP](https://github.com/CharlesWedge/Citadel-Station-13-RP)@[b3a43f2b85...](https://github.com/CharlesWedge/Citadel-Station-13-RP/commit/b3a43f2b8522c03ca976a1f7e72aa9deea97b350)
#### Tuesday 2023-04-25 00:34:42 by IrkallaEpsilon

Buffs Excav Laser Module (#5174)

## About The Pull Request

Buffs Excav laser module. Inconsisten with the one hit of rocks.
Hopefully this ammends it specially since scatterlenses are getting
removed (although nobody used them in combat yet.)

## Why It's Good For The Game

Scatter lense gone, legitimate mining tool needs a buff. The other
options (Phoron Bore) are a sick joke with how slow clunky they are to
use.


## Changelog
:cl:
balance: Meatier sound on excav laser. Higher excav power to
consistently one shot rocks.
/:cl:

---
## [RikuuTheRiolu/Skyrat-tg](https://github.com/RikuuTheRiolu/Skyrat-tg)@[74dc72b867...](https://github.com/RikuuTheRiolu/Skyrat-tg/commit/74dc72b867c1b841c71ec1dedcacff8a64167253)
#### Tuesday 2023-04-25 00:48:33 by SkyratBot

[MIRROR] Config Flag to Save Generated Spritesheets to Logs [MDB IGNORE] (#20738)

* Config Flag to Save Generated Spritesheets to Logs (#74884)

## About The Pull Request

I was helping someone debug some weird bug with spritesheets a bit ago,
and I didn't like having to manually comment out all of the `fdel()`
stuff in order to help visualize what the potential issue might have
been with the spritesheets on either their DM-side generation or their
TGUI-level display. I decided to add a compile-time level flag that will
automatically copy over any generated spritesheet assets (css and pngs)
to the round-specific `data/logs` folder for analysis when a developer
should need it.

I also had to switch around some vars and make a few new ones to reduce
how copy-pasta it might get and ensure standardization/readability while
also being 0.001 times faster since we benefit from the string cache
(unprovable fact).
## Why It's Good For The Game

It's incredibly useful to see the actual flattened spritesheet itself
sometimes when you're doing this type of work and you keep getting odd
bugs here and there. Also saves headache from having to clear out the
temp `/data/spritesheets` folder every time you comment shit out, as
well as having an effective paper trail for A/B testing whatever
bullshit you've got going on.

![image](https://user-images.githubusercontent.com/34697715/233516033-1f5dde1a-e549-4e5a-aa99-0d531b34fbb5.png)
## Changelog
Doesn't affect players.

* Config Flag to Save Generated Spritesheets to Logs

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [yuiseki/evals](https://github.com/yuiseki/evals)@[ef1f0ebe0e...](https://github.com/yuiseki/evals/commit/ef1f0ebe0e9f4674bc42ed0af5e6c052f0539700)
#### Tuesday 2023-04-25 00:50:57 by Josh Gruenstein

Add SVG understanding eval (#786)

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

## Eval details 📑
### Eval name
`svg_understanding`

### Eval description

The model is provided with the contents of an SVG path (anywhere from
~1000 to ~8000 characters) of a simple object (eg `frog`, `banana`) and
is asked to provide the label.

### What makes this a useful eval?

This is a test of visual understanding and mental modeling. A motivated
human could succeed on these evals with enough time and a piece of graph
paper: in theory, a sufficiently advanced LLM could have the in-context
capacity to do this on the fly.

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

This uniquely tests the ability to incrementally build visual models:
eg, the ability of the LLM to both "draw" and visualize that "drawing".

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
{"input": [{"role": "system", "content": "Identify the object the
following SVG path is a drawing of in a single word."}, {"role": "user",
"content": "M6110 12794 c-744 -50 -1284 -157 -1875 -371 -1796 -650 -3199
-2050 -3853 -3843 -186 -510 -302 -1037 -359 -1625 -21 -224 -24 -827 -5
-1045 84 -957 332 -1788 774 -2595 623 -1137 1607 -2078 2780 -2656 720
-354 1441 -556 2273 -636 224 -21 827 -24 1045 -5 741 65 1376 221 2018
493 2051 871 3514 2775 3826 4979 48 336 60 510 60 895 1 366 -7 507 -45
810 -168 1357 -769 2626 -1711 3612 -536 561 -1129 998 -1809 1333 -718
354 -1450 559 -2264 635 -159 15 -727 28 -855 19z"}], "ideal": "circle"}
{"input": [{"role": "system", "content": "Identify the object the
following SVG path is a drawing of in a single word."}, {"role": "user",
"content": "M4495 12298 c-604 -535 -1486 -866 -2660 -998 -331 -37 -854
-70 -1104 -70 l-101 0 -2 -415 -3 -416 30 -29 30 -29 735 -4 c620 -3 753
-7 850 -21 149 -22 254 -50 316 -86 82 -46 123 -142 161 -372 16 -95 18
-371 21 -3663 2 -2593 0 -3591 -8 -3675 -44 -446 -177 -714 -416 -838 -279
-144 -663 -202 -1350 -202 l-330 0 -27 -28 -27 -28 0 -389 0 -389 27 -28
27 -28 3386 0 3386 0 27 28 27 28 0 390 0 390 -27 26 -28 26 -390 5 c-415
5 -557 17 -779 62 -212 43 -367 103 -480 187 -156 115 -260 347 -312 693
-17 114 -18 350 -21 5005 l-3 4884 -27 28 -27 28 -410 -1 -411 0 -80
-71z"}], "ideal": "1"}
{"input": [{"role": "system", "content": "Identify the object the
following SVG path is a drawing of in a single word."}, {"role": "user",
"content": "M6040 12794 c-19 -2 -91 -9 -160 -14 -245 -21 -529 -65 -1240
-190 -399 -70 -593 -100 -654 -100 -91 0 -475 51 -1126 149 -556 84 -788
109 -1075 118 -621 18 -1014 -108 -1310 -418 -344 -360 -490 -941 -472
-1874 21 -1042 173 -1862 619 -3340 l90 -300 -11 -205 c-43 -764 -28 -1853
40 -2845 108 -1585 337 -3026 550 -3473 37 -77 67 -115 184 -238 70 -73
167 -82 258 -24 56 36 102 96 166 220 317 616 732 2551 901 4200 32 314 89
451 257 623 371 379 1029 373 1387 -13 70 -77 106 -129 155 -227 57 -114
79 -196 91 -340 120 -1375 535 -2972 1031 -3963 188 -374 311 -513 458
-514 140 -1 221 106 316 420 232 762 480 2366 595 3849 58 739 82 1376 79
2060 l-2 490 55 115 c228 475 421 1043 527 1550 123 593 169 1196 158 2084
-5 445 -16 597 -58 836 -149 854 -590 1292 -1369 1360 -106 9 -358 11 -440
4z"}], "ideal": "tooth"}
{"input": [{"role": "system", "content": "Identify the object the
following SVG path is a drawing of in a single word."}, {"role": "user",
"content": "M12395 6223 c-133 -27 -295 -150 -356 -269 -13 -27 -40 -68
-59 -90 -19 -23 -57 -79 -84 -125 -161 -274 -369 -539 -542 -695 -191 -171
-304 -231 -559 -298 -499 -132 -725 -257 -1170 -646 -321 -281 -608 -477
-941 -643 -536 -267 -1054 -408 -1735 -473 -236 -23 -800 -23 -1064 0 -701
60 -1256 173 -1940 396 -951 310 -1915 784 -3057 1503 -109 68 -185 109
-220 118 -84 22 -257 17 -358 -10 -102 -28 -256 -99 -289 -135 l-24 -25 21
-88 c27 -115 108 -357 170 -514 253 -633 609 -1222 1069 -1772 164 -196
545 -577 742 -741 986 -822 2174 -1317 3561 -1481 340 -40 485 -48 880 -48
399 -1 546 8 859 49 965 125 1872 497 2606 1068 309 240 645 572 886 876
386 487 682 1048 788 1495 30 130 44 191 101 470 61 292 121 457 263 720
115 214 230 376 365 517 63 65 90 85 176 127 81 39 117 65 183 128 92 89
108 118 93 171 -9 33 -7 39 17 64 l26 27 -22 43 c-12 24 -64 84 -119 136
-116 110 -204 158 -267 145z"}], "ideal": "banana"}
{"input": [{"role": "system", "content": "Identify the object the
following SVG path is a drawing of in a single word."}, {"role": "user",
"content": "M3920 12790 c-1230 -72 -2320 -649 -3052 -1616 -968 -1280
-1142 -3010 -441 -4408 203 -405 432 -712 913 -1221 556 -589 764 -887 945
-1350 102 -264 141 -353 194 -448 l50 -88 -30 -44 c-62 -92 -109 -251 -109
-370 0 -114 44 -261 106 -357 17 -26 17 -28 -14 -95 -43 -94 -62 -181 -62
-292 0 -142 37 -265 107 -359 l25 -34 -35 -76 c-50 -108 -69 -191 -70 -302
-1 -155 39 -275 126 -382 l47 -58 0 -82 c0 -110 21 -193 77 -308 38 -79 59
-108 132 -180 68 -69 103 -95 171 -128 87 -44 203 -75 324 -89 l70 -8 17
-83 c47 -216 205 -374 404 -402 115 -16 827 -12 908 5 202 42 340 188 385
404 l16 80 66 6 c235 22 429 117 548 268 108 139 152 251 160 416 5 111 5
114 38 150 45 48 99 152 118 227 20 79 21 233 0 320 -8 37 -31 102 -50 144
l-35 77 39 61 c66 102 87 185 86 337 0 114 -4 140 -27 210 -15 44 -36 95
-46 114 l-18 34 34 55 c46 78 70 147 84 245 21 140 -16 308 -95 440 l-34
57 59 114 c33 63 103 222 155 353 147 366 255 566 429 798 132 176 245 304
609 690 366 388 516 578 701 885 550 915 713 2023 454 3090 -186 763 -583
1473 -1129 2020 -668 669 -1520 1069 -2480 1165 -185 19 -667 27 -870
15z"}], "ideal": "lightbulb"}
  ```
</details>

---
## [amoxi-chillin/evals-stroke-risk](https://github.com/amoxi-chillin/evals-stroke-risk)@[13069648cf...](https://github.com/amoxi-chillin/evals-stroke-risk/commit/13069648cf12477fb2e3dda073a86a1961789913)
#### Tuesday 2023-04-25 01:28:03 by kvnle93

Eval: Assessing Risk of Stroke

Assessing Risk of Stroke

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

## Eval details 📑
### Eval name
stroke-risk

### Eval description

This eval assesses the model's ability to accurately calculate a hypothetical patient's CHA₂DS₂-VASc Score after being provided relevant information in plain text format.

The mock data was generated by myself; the relevant variables (gender, age, comorbidities) were randomized and weighted so that the prevalence of individual risk factors as well as the overall distribution of scores would more closely resemble those seen in this specific patient population. The use of real patient data was unnecessary in this case as this was primarily a way to evaluate the model's ability to account for risk factors in clinical prompts using a predefined set of strict criteria already contained in its dataset.

### What makes this a useful eval?

The [CHA₂DS₂-VASc Score](https://www.mdcalc.com/calc/801/cha2ds2-vasc-score-atrial-fibrillation-stroke-risk) consists of a simple set of screening criteria that provide clinicians with a rapid way of assessing whether a patient with atrial fibrillation should be on anticoagulation therapy due to their increased risk of incurring a stroke. Scores range from 0 to 9, with individual risk factors like age over 65, hypertension, and diabetes contributing 1 to 2 points each.

Calculating the CHA₂DS₂-VASc Score is straightforward for humans as it involves summing single-digit numbers based on yes or no questions. Minor differences in the score can impact clinical decisions. For example, in a male patient, a score of 0 indicates low risk and no anticoagulation needed, whereas a score of 2 signifies moderate-high risk with a strong recommendation for anticoagulation.

While physicians ultimately make the final recommendation based on the individual patient, basic screening tools like the CHA₂DS₂-VASc Score have proved invaluable in every setting of healthcare.

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

Few evals that have been submitted address topics in medicine - particularly in relation to real clinical applications. With LLMs already seeing integration into widely used EMR systems such as Epic, GPT's growing diagnostic and screening capabilities will be invaluable to clinicians and patients alike.

With this eval, I also felt that improving the model's performance on this task could likewise improve its performance on a wide range of additional clinical screening guidelines in addition to a multitude of similar workflows in other sectors.

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
{"input":[{"role":"system","content":"TASK: Evaluate the provided patient information and calculate the appropriate CHA2DS2-VASc Score. Then structure your response in the following format: \"CHA2DS2-VASc Score:x\" where x represents the single digit CHA2DS2-VASc Score for this patient."},{"role":"user","content":"Age: 64 years, Sex: Male, History of Congestive Heart Failure: No, History of Hypertension: Yes, History of at least one of the following (Stroke/TIA/thromboembolism): No, History of at least one of the following (myocardiac infarction/peripheral artery disease/aortic plaque): Yes, History of diabetes: No"}],"ideal":"CHA2DS2-VASc Score: 2"}
{"input":[{"role":"system","content":"TASK: Evaluate the provided patient information and calculate the appropriate CHA2DS2-VASc Score. Then structure your response in the following format: \"CHA2DS2-VASc Score:x\" where x represents the single digit CHA2DS2-VASc Score for this patient."},{"role":"user","content":"Age: 59 years, Sex: Male, History of Congestive Heart Failure: No, History of Hypertension: Yes, History of at least one of the following (Stroke/TIA/thromboembolism): Yes, History of at least one of the following (myocardiac infarction/peripheral artery disease/aortic plaque): No, History of diabetes: No"}],"ideal":"CHA2DS2-VASc Score: 3"}
{"input":[{"role":"system","content":"TASK: Evaluate the provided patient information and calculate the appropriate CHA2DS2-VASc Score. Then structure your response in the following format: \"CHA2DS2-VASc Score:x\" where x represents the single digit CHA2DS2-VASc Score for this patient."},{"role":"user","content":"Age: 59 years, Sex: Male, History of Congestive Heart Failure: No, History of Hypertension: Yes, History of at least one of the following (Stroke/TIA/thromboembolism): Yes, History of at least one of the following (myocardiac infarction/peripheral artery disease/aortic plaque): No, History of diabetes: No"}],"ideal":"CHA2DS2-VASc Score: 3"}
{"input":[{"role":"system","content":"TASK: Evaluate the provided patient information and calculate the appropriate CHA2DS2-VASc Score. Then structure your response in the following format: \"CHA2DS2-VASc Score:x\" where x represents the single digit CHA2DS2-VASc Score for this patient."},{"role":"user","content":"Age: 60 years, Sex: Female, History of Congestive Heart Failure: No, History of Hypertension: No, History of at least one of the following (Stroke/TIA/thromboembolism): No, History of at least one of the following (myocardiac infarction/peripheral artery disease/aortic plaque): No, History of diabetes: No"}],"ideal":"CHA2DS2-VASc Score: 1"}
{"input":[{"role":"system","content":"TASK: Evaluate the provided patient information and calculate the appropriate CHA2DS2-VASc Score. Then structure your response in the following format: \"CHA2DS2-VASc Score:x\" where x represents the single digit CHA2DS2-VASc Score for this patient."},{"role":"user","content":"Age: 52 years, Sex: Male, History of Congestive Heart Failure: Yes, History of Hypertension: Yes, History of at least one of the following (Stroke/TIA/thromboembolism): No, History of at least one of the following (myocardiac infarction/peripheral artery disease/aortic plaque): No, History of diabetes: No"}],"ideal":"CHA2DS2-VASc Score: 2"}
```
</details>

---
## [HeapsOfRam/GAMENet](https://github.com/HeapsOfRam/GAMENet)@[c59cf2120e...](https://github.com/HeapsOfRam/GAMENet/commit/c59cf2120e342543b6646f947b36179938e24bad)
#### Tuesday 2023-04-25 03:11:47 by HeapsOfRam

pyhealth gamenet (#2)

* pyhealth gamenet

This PR chronicles the migration to the pyhealth library:
https://pyhealth.readthedocs.io/en/latest/api/models/pyhealth.models.GAMENet.html

I have the `pyhealth` GAMENet model running with both MIMIC3 and
MIMIC4 datasets. `pyhealth` is great to work with, and so this
was a very straightforward process. Thank you to TAs Zhen Lin
and Chaoqi Yang for providing some much needed assistance on
campuswire (UIUC), such as what to set my learning rate and decay
weight to!

I have moved all of the original logic into the `original` directory.
pyhealth is also in its own directory. i plan to add some documentation
and guidance around my `pyhealth` approach. i also wonder if i should
rethink my approach to the MIMIC classes, if I want to simply these
somehow, or if i want to add command line parameters to toggle
these things. i may do some of these things to simplify future
development -- but some of them mean be left alone for now since
i also want to prioritize my ablations. i will probably do one
more cleanup commit with a little bit of this and more before
moving one, now that pyhealth is working!

* first cleanup

removing an extraneous backup file and updating my results to
my latest computations. i may also change this file to be output
results from mimic3 and mimic4

* containerization, retain baseline, and documentation

This commit should be the final wrap-up for this PR. I have included
a number of changes in this commit. First, I can now run the code
in podman (or docker) containers. The container seems fairly robust.
I am able to mount the data directory containing the mimic3 and mimic4
datasets thus alleviating the need for the lengthy copy of large files
into the container. This both greatly reduces build time and also
greatly reduces container size, which are ideal. The container should
now only have the bare essentials to run for the most part, though
I am wondering what alternative options I have for the base image
and for the python/pip installation. However, further improvements
here will likely have to be (indefinitely) stalled while I switch
gears to the ablations and additional components of the experiment.
Another nice feature of this containerization effort is that I can
pass arguments in at the run step to the container, which will then
be passed to the python script entrypoint. This means that I can supply
the command line arguments (like number of epochs, values for
hyperparameters, and mimic dataset to use) at runtime of the container
and have them reflected in the script's run. One thing to note is that,
for whatever reason, the logic does run faster on my host hardware
than in a container. Not sure why, but doubt I will solve this in
the scope of this final project.

I have also added the RETAIN baseline to my execution logic. This
was fairly simple, and is trained much like GAMENet. The evaluation
logic is identical, so the function there was reused. For RETAIN,
I had to pass a few additional arguments that I was able to ascertain
from the original paper. This gives me at least a base for comparison
so that I can validate some of my hypotheses. I may spend some time
looking at if I can implement other baselines, but a few of them
seemed like they were not in the pyhealth library yet. This could
indicate a potential area for me to contribute to the library, or
it could be where I have to draw the line for now until I can get
some further work done.

Finally, documentation has been added. This includes updating the
README in the root of the repository as well as adding a README in
the pyhealth directory. This README includes directions for how to
run, the flags that can be provided to the script, etc. I also have
left comments in the code that will hopefully make it fairly easy
to parse. A cleanup script has once again been provided, with some
podman commands I found helpful when cleaning up my environment.
The last piece I have added was a few results from running both
the GAMENet and RETAIN models on the MIMIC3 and the MIMIC4 datasets.
Overall, I am impressed with RETAINS performance. It comes closer
to GAMENet than I realized, even surpassing it at times. One metric
I will have to consider implementing is the DDI Rate metric, which
is one area I feel GAMENet is probably better than RETAIN for.

---
## [llegomark/evals](https://github.com/llegomark/evals)@[24dae81ae0...](https://github.com/llegomark/evals/commit/24dae81ae06ebc70808690c7a147f2710e3e54bf)
#### Tuesday 2023-04-25 04:48:58 by Yohei Inui

Compare countries by area (#623)

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
Compare countries by area

### Eval description

Test the model's ability to determine which country has the largest area

### What makes this a useful eval?

The model should be able to factually determine which country has the
largest area based on accurate facts.
In this eval we use The World
Factbook(https://www.cia.gov/the-world-factbook/field/area/country-comparison)
that is prepared by the CIA for the use of U.S. government officials,
and four countries with similar sizes are compared to each other.
Specifically, four countries adjacent to each other in area ranking are
presented as one option, and the dataset Includes data for countries
ranked 1\~4, 2\~5, ... 100\~103. However, we excluded countries where
sources and interpretations could cause fluctuations in rankings (e.g.,
China and Pakistan). This data set achieved less than 40% accuracy for
both gpt-4 and gpt-3.5-turbo, and the results tend to be worse for
comparisons between countries with smaller areas.

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

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

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
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. Russia, Canada, United
States, Brazil"}], "ideal": "Russia"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. Canada, United States,
Brazil, Australia"}], "ideal": "Canada"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. United States, Brazil,
Australia, India"}], "ideal": "United States"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. Brazil, Australia, India,
Argentina"}], "ideal": "Brazil"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. Australia, India, Argentina,
Kazakhstan"}], "ideal": "Australia"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. India, Argentina, Kazakhstan,
Algeria"}], "ideal": "India"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. Argentina, Kazakhstan,
Algeria, Democratic Republic of the Congo"}], "ideal": "Argentina"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. Kazakhstan, Algeria,
Democratic Republic of the Congo, Saudi Arabia"}], "ideal":
"Kazakhstan"}
  ```
</details>

---------

Co-authored-by: 乾陽平 <inuiyouhei@inuiyouheinoMacBook-Pro.local>

---
## [YakumoChen/tgstation](https://github.com/YakumoChen/tgstation)@[dc2f52e386...](https://github.com/YakumoChen/tgstation/commit/dc2f52e386e0ef3cfcc2133293cd3f68f6a1eee3)
#### Tuesday 2023-04-25 05:19:08 by tralezab

Blink is no longer a forbidden school spell?? (#74487)

## About The Pull Request

Turns blink's school from forbidden to translocation. This has some
incredibly minor changes nobody is going to notice:
- Changes the blink's invocations when mixed with a CERTAIN spell
- If you were very specifically a chaplain with the holy crusade sect
and you casted blink, before it would excommunicate you, now it will
just smite you, as translocation spells are seen as less bad than
forbidden magic
- probably some more niche interactions but that's all I can remember

## Why It's Good For The Game

Guys, I know blink is a very annoying spell but come on now it's not
forbidden magic, that's for heretics and super duper evil stuffs

## Changelog
:cl:
fix: blink is now a translocation spell
/:cl:

---
## [YakumoChen/tgstation](https://github.com/YakumoChen/tgstation)@[48183ec0ff...](https://github.com/YakumoChen/tgstation/commit/48183ec0ffd67ea5afa26c6f6e58e81edff98d52)
#### Tuesday 2023-04-25 05:19:08 by san7890

Icemoon Hermit Ruin Active Turf Fix - For Real This Time (#74476)

In #74306, I _thought_ I knew what the cause was, and I both attempted a
potential fix _and_ made tracking it easier. The fruits of my labor paid
off, I know exactly what caused it now.

Basically, the demonic portal will scrape away all turfs in a 5-tile
radius on its `Initialize()`, and if a spawner spawned right next to the
hermit ruin... it would count it as a mineral turf and scrape it away as
well. That's so fucking silly. At least we know now.
## Why It's Good For The Game

The fix is to just make those tiles unscrapeable, which is accomplished
via another turf_flag and filtering those out in the `Initialize()` of
the demonic portals.

I also cleaned up the calls to scrapeaway being `null`, which is really
weird because it just defaulted to the normal proc behavior. Naming the
arguments instead does the same thing (I checked)

---
## [YakumoChen/tgstation](https://github.com/YakumoChen/tgstation)@[b5ebf5c942...](https://github.com/YakumoChen/tgstation/commit/b5ebf5c9423cb3b39a2b9cfb6524b157dc6cb4b2)
#### Tuesday 2023-04-25 05:19:08 by Helg2

Adds better parts for syndie mechs, some tooltips to mech maintenance mode and some little changes. (#74466)

## About The Pull Request
Kinda resusticates #72442 cause the whole conflict was stupid.
Adds t4 parts for dark gygax, mauler and reticence (for the sake of
shitspawn) and t3 for dark honker.
Formulas of better parts to understand the difference:

https://github.com/tgstation/tgstation/blob/aff9cf1b434c7a95d156ea20108d8b2bc015083d/code/modules/vehicles/mecha/_mecha.dm#L427-L439


Made examine text into span_notices so it's not just plane text.
Also added tooltips for maintenance. Screens to compare:

![image](https://user-images.githubusercontent.com/93882977/229368394-23ca7388-2640-4a82-8134-36a18878b687.png)

![image](https://user-images.githubusercontent.com/93882977/229368398-d4654b56-78e9-4321-80cc-cad31cfabef8.png)


Dark gygax will now spawn without access adding regime.
Tool interactions with mech will now have sounds. (wrench and crowbar)
Removing parts from mech will now put them in your hands, and not just
under the mech.
When inserting parts in mech they won't make some noisy noise, already
forgot which noise it was, but i changed it for some reason, so meh.

Also fixed that you can remove capacitors and scanning mods from mech
without proper maintenance as it works with cell. Closes
https://github.com/tgstation/tgstation/issues/71577
## Why It's Good For The Game
Syndie mechs are still week. Didn't see them in half a year.
## Changelog
:cl:
qol: changed mech description to span_notices and just slightly comfier
to use.
qol: added tooltips for mech's maintenance mode.
balance: added t4 parts for mauler and dark gygax. And t3 parts for dark
honker.
fix: fixed that you can remove capacitor and scanmod from mech without
proper maintenance steps. Now you can't
/:cl:

---
## [Hopekz/cmss13](https://github.com/Hopekz/cmss13)@[9bbac13b28...](https://github.com/Hopekz/cmss13/commit/9bbac13b2898570be5e448ce50ca110472561630)
#### Tuesday 2023-04-25 05:32:38 by TotalEpicness

Globber balance overhaul (#3039)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
Globber came out overtuned as shit and actually replicated some of the
issues that we didn't want like the dreaded ChokePoint Boiler Torture
Rebalances some issues that weren't forseen during the development nor
TM stage of globber. This should be TM'd


General changes:
- Globber C/D 25 seconds > 30 seconds ( the temp nerf PR didnt actually
fix this correctly)
- Fire deals 2x damage instead of 1.5x damage ( this needs significant
testing and will likely be toned down)
- Acid spray doesn't stun at full distances anymore

Depending on TM feedback, I might switch between these two variants of
this overhaul:

Rework variance 1: Keep zoom and current design while maintaining a
little toughness [currently on]
- Armor 25 > 20
-  Zoom halved 4 > 2
-  Dropped health a tier: 650 > 600
- Fire deals 2x damage instead of 1.25x damage
- Globber C/D

Rework variance 2: Embrace the zoom removal
- Directional armor 10 base armor + 20 at the front. Flank a globber to
kill it!
- Slight windup increase 5s > 6s
- Fire damage 1.25x > 1.5x

Fixes:

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

:cl: Totalepicness

balance: Rebalances globber, which has come out overtuned. Globber now
has reduced health, armor and zoom along with higher fire damage
multiplier.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: Epicness <coolguyethanw@gmail.com>
Co-authored-by: morrowwolf <darthbane97@gmail.com>

---
## [JohnFulpWillard/tgstation](https://github.com/JohnFulpWillard/tgstation)@[2b2cb3dff6...](https://github.com/JohnFulpWillard/tgstation/commit/2b2cb3dff6d9985103cee46a6020aa1b63a3c2de)
#### Tuesday 2023-04-25 05:48:24 by LemonInTheDark

Hologram Touchup (Init savings edition) (#74793)

## About The Pull Request

### Polishes and Reworks Holograms

Hologram generation currently involves a bunch of icon operations, which
are slow.
Not to mention a series of get flats for the human models, which is even
worse.

We lose 0.05 seconds of init to em off just the 2 RCD holograms. it
hurts man.

So instead, let's use filters and render steps to achive the same
effect.

While I'm here I'll dim the holo light and make it blue, make the
hologram and its beam emissive (so they glow), and do some fenangling
with move_hologram() (it doesn't clear the hologram off failure anymore,
instead relying on callers to do that) to ensure holocalls can't be
accidentially ended by moving out of the area.

Ah and I added RESET_ALPHA to the emissive appearance flags, cause the
alpha does override and fuck with color rendering, which ends up looking
dumb. If we're gonna support this stuff it should be first class not
accidential.

### Makes Static Not Shit

While I'm here (since holograms see static) lets ensure the static plane
is always visible if you're seeing through an ai eye.

The old solution was limited to applying it to JUST ais, which isn't
satisfactory for this sort of thing and missed a LOT of cases (I didn't
really get how ai eyes worked before I'ma be honest)

I'm adding a signal off the hud for it detecting a change in its eye
here.
This is semi redundant, but avoids unneeded dupe work, so I'm ok with
it.

The pipeline here is less sane then I'd like, but it works and that's
enough

## Why It's Good For The Game


![dreamseeker_zMiLXzlZ2X](https://user-images.githubusercontent.com/58055496/232470136-add945da-5f76-469e-ba1a-6ed3159b6f5b.png)
More pretty, better ux, **static works**

## Changelog
:cl:
add: Holograms glow now, pokes at the lighting for holocalls in general
a bit to make em nicer.
qol: You can no longer accidentally end a holocall (as a non ai) by
leaving the area. Felt like garbage
fix: Fixes static rendering improperly if viewed by a non ai
/:cl:

---
## [isavita/evals](https://github.com/isavita/evals)@[d0e7844c48...](https://github.com/isavita/evals/commit/d0e7844c482b7b65961bc80dad64559ff8ffa488)
#### Tuesday 2023-04-25 06:07:18 by Derek Pisner

Add emotional intelligence evaluation (#589)

## Eval details 📑
### Eval name
Emotional Intelligence

### Eval description
Evaluates GPT's ability to understand and manage emotional situations
using modified versions of the well-validated, public (i.e.
license-unrestricted) tests first developed by MacCann & Roberts (2008).
Items have actually here been aggregated across three different scales--
the STEU and STEM adult measures, along with a dozen questions from the
youth measure.

Keep in mind that there is not expectation that AI models like GPT-4
should be able to process emotions, so applying any emotional
intelligence test to them should be taken with a grain of salt. These
tests can only measure the AI's ability to understand and analyze
emotional information, not the AI's emotional intelligence in the human
sense.

### What makes this a useful eval?
This eval is useful because it assesses the AI model's ability to
navigate complex or ambiguous emotional situations, which is an
important aspect of human-like communication and problem-solving. By
evaluating the model's performance in this unique domain, we can
identify areas for improvement and better understand its limitations
when it comes to handling emotional contexts. This is particularly
important when considering AI applications that involve interactions
with humans, such as chatbots, personal assistants, and customer support
systems. A better understanding of emotional intelligence can
potentially lead to more natural and effective interactions between AI
models and their users.

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

This Emotional Intelligence eval provides a unique value because by
testing GPT's capacity to understand and manage emotions, we can gain
insights into the model's strengths and weaknesses in a more
human-centric context. Relatedly, this eval also emphasizes the
importance of empathy and emotional understanding in AI systems that are
designed to interact with humans. By evaluating GPT's performance in
this way, we can contribute to the ongoing development of AI models that
are more attuned to human emotions and can provide better support in
emotionally charged situations, such as mental health counseling, crisis
management, and conflict resolution. Moreover, this Emotional
Intelligence eval can serve as a foundation for further research and
development in the field of AI and emotional understanding, paving the
way for more sophisticated AI models capable of handling complex human
emotions and fostering more effective communication.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval
(data is publicly available on OSF, and does not have usage
restrictions)

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

**_I already have access to the 8k GPT-4 API, but I am kindly requesting
access to the 32k as soon as it becomes available._**

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

### Performance:
GPT-4: accuracy=0.48

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You are now an emotionally
intelligent AI. In this test, you will be presented with a few brief
details about an emotional situation, and asked to choose from four
responses the most effective course of action to manage both the
emotions the person is feeling and the problems they face in that
situation. Although more than one course of action might be acceptable,
you are asked to choose what you think the most effective response for
that person in that situation would be. Remember, you are not
necessarily choosing what you would do, or the nicest thing to do, but
choosing the most effective response for that situation. Select one or
more response(s) by returning the one or more corresponding lowercase
letter(s) ('a', 'b', 'c', or 'd'), and, if you selected more than one,
sorting them, separated by hyphen, in the order that you think best
ranks them from most to least effective, within the context of the
vignette provided."}, {"role": "user", "content": "Lee's workmate fails
to deliver an important piece of information on time, causing Lee to
fall behind schedule also. What action would be the most effective for
Lee? (a) Work harder to compensate; (b) Get angry with the workmate; (c)
Explain the urgency of the situation to the workmate; (d) Never rely on
that workmate again."}], "ideal": "c"}
{"input": [{"role": "system", "content": "You are now an emotionally
intelligent AI. In this test, you will be presented with a few brief
details about an emotional situation, and asked to choose from four
responses the most effective course of action to manage both the
emotions the person is feeling and the problems they face in that
situation. Although more than one course of action might be acceptable,
you are asked to choose what you think the most effective response for
that person in that situation would be. Remember, you are not
necessarily choosing what you would do, or the nicest thing to do, but
choosing the most effective response for that situation. Select one or
more response(s) by returning the one or more corresponding lowercase
letter(s) ('a', 'b', 'c', or 'd'), and, if you selected more than one,
sorting them, separated by hyphen, in the order that you think best
ranks them from most to least effective, within the context of the
vignette provided."}, {"role": "user", "content": "Rhea has left her job
to be a full-time mother, which she loves, but she misses the company
and companionship of her workmates. What action would be the most
effective for Rhea? (a) Enjoy being a full-time mom; (b) Try to see her
old workmates socially, inviting them out; (c) Join a playgroup or
social group of new mothers; (d) See if she can find part time work."}],
"ideal": "c-b-d"}
{"input": [{"role": "system", "content": "You are now an emotionally
intelligent AI. In this test, you will be presented with a few brief
details about an emotional situation, and asked to choose from four
responses the most effective course of action to manage both the
emotions the person is feeling and the problems they face in that
situation. Although more than one course of action might be acceptable,
you are asked to choose what you think the most effective response for
that person in that situation would be. Remember, you are not
necessarily choosing what you would do, or the nicest thing to do, but
choosing the most effective response for that situation. Select one or
more response(s) by returning the one or more corresponding lowercase
letter(s) ('a', 'b', 'c', or 'd'), and, if you selected more than one,
sorting them, separated by hyphen, in the order that you think best
ranks them from most to least effective, within the context of the
vignette provided."}, {"role": "user", "content": "Pete has specific
skills that his workmates do not and he feels that his workload is
higher because of it. What action would be the most effective for Pete?
(a) Speak to his boss about this; (b) Start looking for a new job; (c)
Be very proud of his unique skills; (d) Speak to his workmates about
this."}], "ideal": "a-c-d"}
{"input": [{"role": "system", "content": "You are now an emotionally
intelligent AI. In this test, you will be presented with a few brief
details about an emotional situation, and asked to choose from four
responses the most effective course of action to manage both the
emotions the person is feeling and the problems they face in that
situation. Although more than one course of action might be acceptable,
you are asked to choose what you think the most effective response for
that person in that situation would be. Remember, you are not
necessarily choosing what you would do, or the nicest thing to do, but
choosing the most effective response for that situation. Select one or
more response(s) by returning the one or more corresponding lowercase
letter(s) ('a', 'b', 'c', or 'd'), and, if you selected more than one,
sorting them, separated by hyphen, in the order that you think best
ranks them from most to least effective, within the context of the
vignette provided."}, {"role": "user", "content": "Mario is showing Min,
a new employee, how the system works. Mario's boss walks by and
announces Mario is wrong about several points, as changes have been
made. Mario gets on well with his boss, although they don't normally
have much to do with each other. What action would be the most effective
for Mario? (a) Make a joke to Min, explaining he didn't know about the
changes; (b) Not worry about it, just ignore the interruption; (c) Learn
the new changes; (d) Tell the boss that such criticism was
inappropriate."}], "ideal": "a-d-c"}
{"input": [{"role": "system", "content": "You are now an emotionally
intelligent AI. In this test, you will be presented with a few brief
details about an emotional situation, and asked to choose from four
responses the most effective course of action to manage both the
emotions the person is feeling and the problems they face in that
situation. Although more than one course of action might be acceptable,
you are asked to choose what you think the most effective response for
that person in that situation would be. Remember, you are not
necessarily choosing what you would do, or the nicest thing to do, but
choosing the most effective response for that situation. Select one or
more response(s) by returning the one or more corresponding lowercase
letter(s) ('a', 'b', 'c', or 'd'), and, if you selected more than one,
sorting them, separated by hyphen, in the order that you think best
ranks them from most to least effective, within the context of the
vignette provided."}, {"role": "user", "content": "Wai-Hin and Connie
have shared an office for years but Wai-Hin gets a new job and Connie
loses contact with her. What action would be the most effective for
Connie? (a) Just accept that she is gone and the friendship is over; (b)
Ring Wai-Hin an ask her out for lunch or coffee to catch up; (c) Contact
Wai-Hin and arrange to catch up but also make friends with her
replacement; (d) Spend time getting to know the other people in the
office, and strike up new friendships."}], "ideal": "c-d"}
  ```
</details>

---------

Co-authored-by: dpys <dpisner@clairity.com>

---
## [isavita/evals](https://github.com/isavita/evals)@[fabca8cebb...](https://github.com/isavita/evals/commit/fabca8cebb3f8e14d1f374e448533e0bde6e5a68)
#### Tuesday 2023-04-25 06:07:18 by Nick Clyde

Heart Disease Prediction (#538)

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
Heart Disease Prediction

### Eval description

This eval tests the models ability to correctly predict the probability
of a patient to have heart disease. The dataset is constructed from the
[Heart Failure Prediction
Dataset](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction)
on Kaggle. The data includes the patient's age, sex, and a number of
medical signals relevant to the diagnosis of heart disease.

The data is provided under the Open Database License (ODbL). 

```
fedesoriano. (September 2021). Heart Failure Prediction Dataset. Retrieved [Mar 31, 2023] from https://www.kaggle.com/fedesoriano/heart-failure-prediction.
```

### What makes this a useful eval?

This assesses the model's ability to correctly predict adverse medical
events. Correctly predicting heart disease shows the model's capability
for a strong understanding of medicine. The GPT-3.5-turbo models
currently receives an accuracy of 0.778.

<img width="1250" alt="Screenshot 2023-03-31 at 2 24 13 PM"
src="https://user-images.githubusercontent.com/9121162/229234376-9cdd1315-5df0-48bf-9328-ac31aabec3cc.png">

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

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

As far as I can tell, this is the only eval so far related to making
medical diagnoses. To make sure it was a high quality eval, I tried to
find a dataset with a lot of observations and created by doctors with
the relevant expertise.

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
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 40 years, Sex: Male, Chest pain
type: Atypical Angina, Resting blood pressure: 140 mm Hg, Serum
cholesterol: 289 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: Normal, Max heart rate achieved: 172, Exercise induced angina:
No, Oldpeak: 0, ST Slope: Upsloping"}], "ideal": "0"}
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 49 years, Sex: Female, Chest
pain type: Non-Anginal Pain, Resting blood pressure: 160 mm Hg, Serum
cholesterol: 180 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: Normal, Max heart rate achieved: 156, Exercise induced angina:
No, Oldpeak: 1, ST Slope: Flat"}], "ideal": "1"}
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 37 years, Sex: Male, Chest pain
type: Atypical Angina, Resting blood pressure: 130 mm Hg, Serum
cholesterol: 283 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: ST-T wave abnormality, Max heart rate achieved: 98, Exercise
induced angina: No, Oldpeak: 0, ST Slope: Upsloping"}], "ideal": "0"}
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 48 years, Sex: Female, Chest
pain type: Asymptomatic, Resting blood pressure: 138 mm Hg, Serum
cholesterol: 214 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: Normal, Max heart rate achieved: 108, Exercise induced angina:
Yes, Oldpeak: 1.5, ST Slope: Flat"}], "ideal": "1"}
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 54 years, Sex: Male, Chest pain
type: Non-Anginal Pain, Resting blood pressure: 150 mm Hg, Serum
cholesterol: 195 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: Normal, Max heart rate achieved: 122, Exercise induced angina:
No, Oldpeak: 0, ST Slope: Upsloping"}], "ideal": "0"}
  ```
</details>

---
## [isavita/evals](https://github.com/isavita/evals)@[776e4fa212...](https://github.com/isavita/evals/commit/776e4fa212288be152c3030cf36fd04c8d939230)
#### Tuesday 2023-04-25 06:07:18 by JPrenter

Financial Math (Evals) (#566)

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
finance

### Eval description

Asks the model to calculate how much interest would be owed on a credit
card by a certain date, if a payment was made once but debt remains on
the card.

### What makes this a useful eval?

Finance is likely to be one of the biggest opportunities for LLMs to be
useful, because financial education is incredibly poor globally and the
impact of a mistake in financial calculations is severe. This eval tests
the models ability to combine math with its understanding of a topic
(finance). We plan to use this type of math at
[Dollarwise](https://www.dollarwise.ca) frequently going forward,
including integration into your comparison products. However, for this
to work reliably it's important that the model here can natively
understand financial concepts and apply math to them.

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
- [X] Include at least 100 high quality examples (it is okay to only
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
`evals/registry/evals/{name}.yaml`
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
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "On the 24th of September,
Sarah had spent $1237.42 on her credit card for the month of September.
This credit card charges 21.99% interest rate annually on outstanding
credit starting on the 1st of the following month. Presume that interest
is only charged at the end of each additional day. Example: From the 1st
of the month to the 8th would be 7 days of interest accrued.Today is the
27th of September and Sarah makes a payment of $125 towards her credit
card. How much interest will she have been charged by October 15th if
she makes no additional payments? If the final interest figure is more
than 2-decimal places, always round down. Answer ONLY with a dollar
figure. Do not output any logic, output only the dollar figure for how
much interest she was charged for the period."}], "ideal": "9.42"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "On the 19th of February,
Jason had spent $15.21 on his credit card for the month of February.
This credit card charges 21.99% interest rate annually on outstanding
credit starting on the 1st of the following month. Presume that interest
is only charged at the end of each additional day. Example: From the 1st
of the month to the 8th would be 7 days of interest accrued. Today is
the 23rd of February and he makes a payment of $1 towards his credit
card. How much interest will he have been charged by March 10th if he
makes no additional payments? If the final interest figure is more than
2-decimal places, always round down. Answer ONLY with a dollar figure.
Do not output any logic, output only the dollar figure for how much
interest she was charged for the period."}], "ideal": "0.07"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "On the 12th of February,
Jason had spent $10,674.21 on his credit card for the month of February.
This credit card charges 21.99% interest rate annually on outstanding
credit starting on the 1st of the following month. Presume that interest
is only charged at the end of each additional day. Example: From the 1st
of the month to the 8th would be 7 days of interest accrued. Today is
the 18th of February and he makes a payment of $1,000 towards his credit
card. How much interest will he have been charged by March 10th if he
makes no additional payments? If the final interest figure is more than
2-decimal places, always round down. Answer ONLY with a dollar figure.
Do not output any logic, output only the dollar figure for how much
interest she was charged for the period."}], "ideal": "52.59"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "On the 2nd of August, Jason
had spent $15,674.21 on his credit card for the month of August. This
credit card charges 21.99% interest rate annually on outstanding credit
starting on the 1st of the following month. Presume that interest is
only charged at the end of each additional day. Example: From the 1st of
the month to the 8th would be 7 days of interest accrued. Today is the
18th of August and he makes a payment of $1,000 towards his credit card.
How much interest will he have been charged by September 10th if he
makes no additional payments? If the final interest figure is more than
2-decimal places, always round down. Answer ONLY with a dollar figure.
Do not output any logic, output only the dollar figure for how much
interest she was charged for the period."}], "ideal": "79.77"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "On the 15th of August, Jason
had spent $1000 on his credit card for the month of August. This credit
card charges 21.99% interest rate annually on outstanding credit
starting on the 1st of the following month. Presume that interest is
only charged at the end of each additional day. Example: From the 1st of
the month to the 8th would be 7 days of interest accrued. mToday is the
18th of August and he makes a payment of $1000 towards his credit card.
How much interest will he have been charged by September 10th if he
makes no additional payments? If the final interest figure is more than
2-decimal places, always round down. Answer ONLY with a dollar figure.
Do not output any logic, output only the dollar figure for how much
interest she was charged for the period."}], "ideal": "0.00"}
  ```
</details>

---
## [iguessthislldo-test-org/OpenDDS](https://github.com/iguessthislldo-test-org/OpenDDS)@[8029f5acbc...](https://github.com/iguessthislldo-test-org/OpenDDS/commit/8029f5acbcf34349f860474d8a1fc67524fa4fa1)
#### Tuesday 2023-04-25 06:22:21 by Fred Hornsey

Generate News in Sphinx From Fragments

The current way of generating the news for releases mostly consists of
generating a spreadsheet of PRs, editing that, and creating the new
entries from that manually. More info on that process
[here](https://opendds.readthedocs.io/en/master/internal/release.html#update-files-in-the-repo-as-needed)
and [here](https://github.com/OpenDDS/OpenDDS/blob/f511b1f1582664ab7f49b3b012b968e684928aa2/tools/scripts/release_notes/README.md).
News entries can be directly committed in the PR where the change is
taking place, but doing that risks merge conflicts.

Overall this process is somewhat messy and limiting:

- Deciding what's newsworthy, what exactly to write, and reviewing the
  news is done all at once right before the release, sometimes months
  after the work was done. This makes it harder to remember what's
  newsworthy, what specific things needs to be pointed out to users, and
  what PRs should go together for single news item. This also means it
  takes more time to prepare the release and there's less time to spot
  and correct mistakes in the news or improve it.
- Most of the time the news item is left as just the title of PR. In the
  best case these might not need to be tweaked much or at all for
  changes that require little explanation. However this is certainly
  inadequate for explaining larger changes, for example like for [the
  XTypes fixes from PR4078](
  https://github.com/OpenDDS/OpenDDS/blob/f511b1f1582664ab7f49b3b012b968e684928aa2/NEWS.md?plain=1#L49).
  It'd be very awkward to write that much in a spreadsheet.
- It's hard to link to documentation. This is better than it was before
  with the PDF devguide, when it was impossible, but this could still be
  improved on more. Linking would give more context to users and could
  immediately give them details on use a new feature.
- Contributors outside the OpenDDS maintainers basically have no direct
  input on what the news says for changes they contribute. Honestly I'm
  not sure if any have wanted to, but they couldn't if they did.

The solution in this PR is committing the news of changes of a PR as a
file in that PR. At release these fragments of the news are
brought together automatically. There are still a few kinks to iron out,
but even if those are mostly unresolved I think this system will improve
the quaility of the news.

The system is inspired by [Python's blurb
tool](https://pypi.org/project/blurb/) and to a lesser extent tools like
[towncrier](https://towncrier.readthedocs.io/en/stable/index.html).
These tools are not bad, but they have some serious drawbacks. blurb is
specifically tailored for CPython development. For example, it's
oriented by GitHub issues, where as many of the changes we make are not
prompted by a GitHub issue. towncrier really expects the project to be a
Python project and has some quirks for some of use cases I was looking
for. Specifically needing multiple identical files for to attribute a
news item to multiple PRs and needing multiple files for a PR to have
different kinds of changes. Also both rely on the files having a
specific name, which seems unnecessary to me.

The following is the basics of adding a news fragment and how the news
is generated in this system:

Create a rst file in `docs/news.d/`. This is a news fragment. It can be
named anything as long as it doesn't have an leading underscore and is a
rst file, but it should be somewhat descriptive. Naming it the same as
the branch the change is on might be good idea. The change must be a rst
list. It has to have some rst-directive-like metadata around it. A
minimal file looks like this:

``` rst
.. news-prs: 5000
.. news-push: Additions
- This is an addition we made.
.. news-pop
```

Additional PRs are added by appending them to end of the `news-prs`
line. Additional `news-push`s and `news-pop`s can be used to add list
items to other sections, like fixes, or to create nested sections for
groups of changes like like "XTypes" or "RTPS". All sections will be
merged together in the final result. These sections and items are sorted
first by a quality called rank, then by the PR numbers in reverse order
(basically chronological). The rank is changed by `.. news-rand:
RANK_NUMBER`. It can be used to headline an important change or set of
changes,

See `docs/news.d/_example.rst` for a longer example. I also have added a
recreation of the 3.24.0 news as fragments as a test and a full example
of what this would look like.

Before release a preview of the news entry will always be available in
the built version of `docs/news.rst`. The means news added in an PR can
be previewed in the PR. During a release the fragments are permanently
committed to that file and the fragment files in `docs/news.d` are
removed.

Here are the two main issues I see with this system right now:

- To do a PR with a news fragment in one commit, you basically have to
  know what the PR number is going to be before hand. Otherwise another
  commit is needed to add the PR number. The PR number could technically
  be manually added after the PR is merged, but I would consider that
  poor practice. One solution could be a placeholder in `news-pr`
  statement that an action automatically replaces with the PR number
  after the PR is merged.
- How does this relate/integrate with `NEWS.md` and the GitHub release
  notes? I'm honestly a little stumped by this and unlike the other
  issue this needs to be figured out before this can be merged.
  - Something like pandoc could be used to convert the rst, but it would
    still need some manual intervention based on tests I did with the
    3.24.0 news.
  - The markdown version could just be a summarized version of the news,
    mostly consisting of highlights. This could be manually done or done
    with pandoc with human intervention. Also this summery could be what
    goes out in a prerelease announcement on social media.
  - The `NEWS.md` file could be also be done away with to simplify
    things. If that's the case, shuold news.rst live in the root
    directory and be called `NEWS.rst`? Is that going to case problems to
    try to include it in Shpinx?
  - The GitHub release notes could just link to `news.rst`, but I feel
    like they probably should at least have a summery.

Besides that there are some more things I needs to do, specifically:

- Document either in the documentation guidlines or dev guidelines how
  to add to the news.
- Improve release entries, it needs the release date and output could be
  tweaked.
- Maybe add two smaller examples just for "Additions" and "Fixes"
  without comments that are eaiser to use as templates.
- Before merge, remove 3.24.0 fragments, add any newer releases, and add
  any news fragments for a pending release.

---
## [Kamilake/evalso](https://github.com/Kamilake/evalso)@[aeeb452867...](https://github.com/Kamilake/evalso/commit/aeeb4528675de633d95a3535100b23c98739f6ce)
#### Tuesday 2023-04-25 06:30:45 by Alexander Raul

Algebra word problems (#36)

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
to see the eval performance on GPT-4.

## Eval details 📑
### Eval name
Algebra Word Problems (algebra_word_problems)

### Eval description

This eval contains some algebra word problems that tend to make gpt 3.5
hallucinate, but wouldn't be out of place on a grade school exam.
Currently has less than 100 examples, but will add if folks think this
is a good eval path to go down.

### What makes this a useful eval?

Poor performance on GPT 3.5 for one, but also would be a great test of
increased logical reasoning capabilities of GPT-4 per the release blog
post.

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
- [] Include at least 100 high quality examples

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
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

Since we are using Git LFS, we are asking eval submitters to add in
their first 100 JSONL eval lines.

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Answer the following question
with a single number and no additional text. You are a helpful
assistant."}, {"role": "user", "content": "If it takes 5 machines 5
minutes to make 5 devices, how long would it take 100 machines to make
100 devices?"}], "ideal": "5"}
{"input": [{"role": "system", "content": "Answer the following question
with a single number and no additional text. You are a helpful
assistant."}, {"role": "user", "content": "What is the sum of 60000,
5000, 400, and 3, with the third value multiplied by 5 before performing
the operation?"}], "ideal": "67003"}
{"input": [{"role": "system", "content": "Answer the following question
with a single number and no additional text. You are a helpful
assistant."}, {"role": "user", "content": "If the sum of the smallest
and largest of three consecutive even numbers is 28, what is the value
of the second largest number in the series?"}], "ideal": "14"}
{"input": [{"role": "system", "content": "Answer the following question
with a single number and no additional text. You are a helpful
assistant."}, {"role": "user", "content": "John is trying to fill a 16
oz. bottle with water. If John fills the bottle at 1 oz per second and
the bottle leaks .2 oz per second, how long would it take for John to
fill the bottle?"}], "ideal": "20"}
{"input": [{"role": "system", "content": "Answer the following question
with a single number and no additional text. You are a helpful
assistant."}, {"role": "user", "content": "Annie is training for a
marathon. She has a weekly training routine, training for five hours a
day on some days and 3 hours a day on the other days. She trains a total
of 27 hours in a seven day week. On how many days does she train for
five hours?"}], "ideal": "3"}
{"input": [{"role": "system", "content": "Answer the following question
with a single number and no additional text. You are a helpful
assistant."}, {"role": "user", "content": "At the start of the year the
ratio of boys to girls in a class is 2 : 1. But now, half a year later,
four boys have left the class and there are two new girls. The ratio of
boys to girls is now 4 : 3. How many students are there altogether
now?"}], "ideal": "28"}
  ```
</details>

---
## [Kamilake/evalso](https://github.com/Kamilake/evalso)@[bf2ebb9dd6...](https://github.com/Kamilake/evalso/commit/bf2ebb9dd69e8fbaad3eb42dab1a0523066a52ed)
#### Tuesday 2023-04-25 06:30:45 by Amir DIB

[evals] emoji riddle eval 🎨🤔 (#510)

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
**Emoji riddle**

### Eval description

The evaluation involves solving riddles made up of emojis. The
inspiration for this idea came from reading LinkedIn posts, where I
noticed that nearly 1-4% of the textual information was conveyed through
emojis. Nowadays, emojis are widely used to format text and introduce
color contrasts in texts, even by community managers of large companies.
Furthermore, using emojis is seen as a less formal way of communication
and gives a tone more suitable for social media.


### What makes this a useful eval?

- **Conversational understanding**. the eval test the ability to link
different concepts together which is a crucial feature.

- **Communication**. As GPT is deployed in settings where informal
language is used, interpreting emojis in context will likely become
critical. I think that improvement on this emoji riddle task would make
GPT better at mimicking human-like communication, as it would be able to
understand and respond to various forms of expressions involving emojis.
Emojis and their combinations often carry cultural and social meanings.
By being adept at emoji riddles, ChatGPT would showcase an understanding
of cultural nuances and be more relatable to users.

- **problem-solving**: Emoji riddle solving requires i) extracting
possible meanings and ii) finding the more suitable association of
meaning in the given context (cultural, plateform, etc).

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
{"input":[{"role":"system","content":"You are an emoji riddle solver.
You understand that an emoji riddle consists of finding the word or
group of words associated with an association of emojis that is provided
with the following format: emoji_1 + ... + emoji_n = ? . Your task is to
find the right answer."},{"role":"user","content":"👀 + 🪚 = ? \n Your
answer should strictly only contain the group of words associated with
the answer, no additional words. Don't add `The answer is`. don't add a
period at the end of your answer. everything should be
lowercase"}],"ideal":["seesaw"]}
{"input":[{"role":"system","content":"You are an emoji riddle solver.
You understand that an emoji riddle consists of finding the word or
group of words associated with an association of emojis that is provided
with the following format: emoji_1 + ... + emoji_n = ? . Your task is to
find the right answer."},{"role":"user","content":"❤️ + ✉️ = ? \n Your
answer should strictly only contain the group of words associated with
the answer, no additional words. Don't add `The answer is`. don't add a
period at the end of your answer. everything should be
lowercase"}],"ideal":["love letter"]}
{"input":[{"role":"system","content":"You are an emoji riddle solver.
You understand that an emoji riddle consists of finding the word or
group of words associated with an association of emojis that is provided
with the following format: emoji_1 + ... + emoji_n = ? . Your task is to
find the right answer."},{"role":"user","content":" ⌚️ + 🐶 = ? \n Your
answer should strictly only contain the group of words associated with
the answer, no additional words. Don't add `The answer is`. don't add a
period at the end of your answer. everything should be
lowercase"}],"ideal":["watchdog"]}
  ```
</details>

**The Dataset**

![image](https://user-images.githubusercontent.com/22154031/228633727-14480364-4009-45c1-8398-276de7bd86a9.png)

---
## [Kamilake/evalso](https://github.com/Kamilake/evalso)@[38f40050e9...](https://github.com/Kamilake/evalso/commit/38f40050e9344d6d4694c75506af03bf7ffe14d3)
#### Tuesday 2023-04-25 06:30:45 by dz-pika

Utility charge eval (#735)

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

## Eval details 📑
### Eval name
Utility charge eval 

### Eval description
Given snippets from an electric utility bill, compute the per-kWh price
for electricity supply and delivery.

### What makes this a useful eval?
Utility bill parsing is needed to understand the breakdown of charges
and forecast future bills based on predicted usage. However, electricity
bills can be complex, with dozens of different line items that
contribute to the overall cost. This can be a headache for people
looking at their bill, as they just want to understand the per-kWh
prices for the supply/generation or delivery (e.g. transmission &
distribution) of their energy. Given incomplete but sufficient
information (e.g. simulating running OCR on a utility bill), this task
requires both the understanding and grouping of different terms and
charges under the delivery or supply, and basic arithmetic to compute
the total kWh and total charges in order to determine the per-kWh
prices. A human could fairly easily interpret the given data, but we
find that GPT3.5 (as well as GPT4 via the ChatGPT Plus) perform much
less accurately on the task (~.2).

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

All of the examples contain dummy values, but come from
terminology/formatting used in bills from many different utilities.

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
{"input": [{"role": "system", "content": "You are a JSON utility that
must return machine-readable JSON as output."}, {"role": "user",
"content": "Your job is compute the cost per kWh of electricity supply
(value must be a decimal rounded to 2 significant figures) and the cost
per kWh of electricity delivery (value must be a decimal rounded to 2
significant figures) based on the following incomplete OCR reading from
a user's utility bill. You are guaranteed to have the information needed
to compute the desired values. Return in the following JSON format:
{'supply_cost_per_kwh': '', 'delivery_cost_per_kwh': ''}. The following
is information from the utility bill: \nBasic Generation Service: 121
kWh X $0.069 per kWh = 8.35 \n Total Electric Supply Charges = 30.23 \n
Distribution Charge: 121 kWh X $0.041 per kWh = 4.96 \n Total Electric
Delivery Charges = 20.43"}], "ideal": "{'supply_cost_per_kwh': '0.25',
'delivery_cost_per_kwh': '0.17'}"}
{"input": [{"role": "system", "content": "You are a JSON utility that
must return machine-readable JSON as output."}, {"role": "user",
"content": "Your job is compute the cost per kWh of electricity supply
(value must be a decimal rounded to 2 significant figures) and the cost
per kWh of electricity delivery (value must be a decimal rounded to 2
significant figures) based on the following incomplete OCR reading from
a user's utility bill. You are guaranteed to have the information needed
to compute the desired values. Return in the following JSON format:
{'supply_cost_per_kwh': '', 'delivery_cost_per_kwh': ''}. The following
is information from the utility bill: \nGeneration Service (Supply) =
$34.89 \n Transmission Service = 7.24 \n Distribution Service = 4.96 \n
Meter Usage: 568 kWh"}], "ideal": "{'supply_cost_per_kwh': '0.061',
'delivery_cost_per_kwh': '0.022'}"}
{"input": [{"role": "system", "content": "You are a JSON utility that
must return machine-readable JSON as output."}, {"role": "user",
"content": "Your job is compute the cost per kWh of electricity supply
(value must be a decimal rounded to 2 significant figures) and the cost
per kWh of electricity delivery (value must be a decimal rounded to 2
significant figures) based on the following incomplete OCR reading from
a user's utility bill. You are guaranteed to have the information needed
to compute the desired values. Return in the following JSON format:
{'supply_cost_per_kwh': '', 'delivery_cost_per_kwh': ''}. The following
is information from the utility bill: \nElectricity Used (kWh) = 762 \n
Electricity Supply Charges 762 kWh at a cost of $100.25 \n Delivery
Service Charge: 762 kWh @ 0.008 = 6.096 \n Total Electric Delivery
Charges = 59.36"}], "ideal": "{'supply_cost_per_kwh': '0.13',
'delivery_cost_per_kwh': '0.078'}"}
{"input": [{"role": "system", "content": "You are a JSON utility that
must return machine-readable JSON as output."}, {"role": "user",
"content": "Your job is compute the cost per kWh of electricity supply
(value must be a decimal rounded to 2 significant figures) and the cost
per kWh of electricity delivery (value must be a decimal rounded to 2
significant figures) based on the following incomplete OCR reading from
a user's utility bill. You are guaranteed to have the information needed
to compute the desired values. Return in the following JSON format:
{'supply_cost_per_kwh': '', 'delivery_cost_per_kwh': ''}. The following
is information from the utility bill: \nSupply 423 kWh @ 11 cents / kWh
= 46.53 \n Total electricity supply charges $68.21 \n Delivery 423 kWh @
4 cents / kWh = 16.92 \n Total electricity delivery charges $17.43"}],
"ideal": "{'supply_cost_per_kwh': '0.16', 'delivery_cost_per_kwh':
'0.041'}"}
{"input": [{"role": "system", "content": "You are a JSON utility that
must return machine-readable JSON as output."}, {"role": "user",
"content": "Your job is compute the cost per kWh of electricity supply
(value must be a decimal rounded to 2 significant figures) and the cost
per kWh of electricity delivery (value must be a decimal rounded to 2
significant figures) based on the following incomplete OCR reading from
a user's utility bill. You are guaranteed to have the information needed
to compute the desired values. Return in the following JSON format:
{'supply_cost_per_kwh': '', 'delivery_cost_per_kwh': ''}. The following
is information from the utility bill: \nEnergy 152 @ 0.069 = 10.49 \n
Total Energy Charges = 14.25 \n Distribution 152 @ 0.041 = 6.23 \n Total
Electric Delivery Charges = 6.99"}], "ideal": "{'supply_cost_per_kwh':
'0.094', 'delivery_cost_per_kwh': '0.046'}"}
  ```
</details>

---
## [Kamilake/evalso](https://github.com/Kamilake/evalso)@[b2250e4117...](https://github.com/Kamilake/evalso/commit/b2250e4117125fa79e852f454cd4b01b3c066563)
#### Tuesday 2023-04-25 06:30:45 by shivamd1810

Add General science reasoning: UPSC GS eval. (#641)

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

## Eval details 📑
### Eval name
Hindi UPSC

### Eval description

[UPSC](https://en.wikipedia.org/wiki/Union_Public_Service_Commission) is
the organization responsible for conducting administrative service exams
in India. This evaluation set focuses on questions from the general
science paper of UPSC exams in Hindi. As a widely spoken language in
India, it is crucial to understand and answer questions accurately in
Hindi.



### What makes this a useful eval?

This evaluation set is useful for several reasons:

1. Real-world applicability: The questions are sourced from actual UPSC
exams, making the evaluation set practical and relevant for users
preparing for these exams.
2. Language diversity: By focusing on Hindi, this evaluation set helps
to improve the AI's understanding and response generation in a
non-English language, catering to a large user base.
3. Subject matter: General science is an important topic covered in the
UPSC exams, and evaluating the AI's performance in this area will help
identify areas for improvement.
4. Logical reasoning and inference: **UPSC questions are known for
requiring logical reasoning and the ability to infer connections between
multiple topics**. By including questions that demand such skills, this
evaluation set will help test and improve the AI's ability to handle
complex, multi-layered problems.


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

This evaluation set is valuable for improving the AI's understanding of
Hindi and its ability to provide accurate answers to general science
questions in the context of UPSC exams, a widely recognized and
important examination in India. Moreover, by incorporating questions
that test logical reasoning and inference skills, it will help enhance
the AI's capability to handle complex, multi-faceted problems that
require connections between multiple topics.

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
{"input": [{"role": "system", "content": "\n1. भारत की संसद के संदर्भ
में, निम्नलिखित कथनों पर विचार कीजिए:\n\n1- गैर-सरकारी विधेयक ऐसा विधेयक
है जो संसद् के ऐसे सदस्य द्वारा प्रस्तुत किया जाता है जो निर्वाचित नहीं
है किंतु भारत के राष्ट्रपति द्वारा नामनिर्दिष्ट है।\n2- हाल ही में, भारत
की संसद के इतिहास में पहली बार एक गैर-सरकारी विधेयक पारित किया गया
है।\n\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?\n\n(a) केवल 1\n(b)
केवल 2\n(c) 1 और 2 दोनों\n(d) न तो 1 और न ही 2\n\n, choose correct
answer:"}], "ideal": "d"}
{"input": [{"role": "system", "content": "2. ऋग्वेद-कालीन आर्यों और
सिन्धु घाटी के लोगों की संस्कृति के बीच अंतर के संबंध में, निम्नलिखित
कथनों में से कौन-सा/से सही है/हैं?\n1- ऋग्वेद-कालीन आर्य कवच और
शिरस्त्रण (हेलमेट) का उपयोग करते थे जबकि सिन्धु घाटी सभ्यता के लोगों में
इनके उपयोग का कोई साध्य नहीं मिलता।\n2- ऋग्वेद-कालीन आर्यों को स्वर्ण,
चाँदी और ताम्र का ज्ञान था जबकि सिन्धु घाटी के लोगों को कवल ताम्र और लोह
का ज्ञान था।\n3- ऋग्वेद-कालीन आर्यों ने घोड़े को पालतू बना लिया था जबकि
इस बात का कोई साक्ष्य नहीं है कि सिन्धु घाअी के लोग इस पशु को जानते
थे।\n\nनीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिएः\n\n(a) केवल 1\n(b)
केवल 2 और 3\n(c) केवल 1 और 3\n(d) 1, 2 और 3\n\n, choose correct
answer:"}], "ideal": "c"}
{"input": [{"role": "system", "content": "3. ‘पूर्व अधिगम की मान्यता
स्कीम (रिकग्निशन ऑफ प्रायर लर्निंग स्कीम)’ का कभी-कभी समाचारों में किस
संदर्भ में उल्लेख किया जाता है?\n(a) निर्माण कार्य में लगे कर्मकारों के
पारंपरिक मार्गों से अर्जित कौशल का प्रमाणन\n(b) दूरस्थ अधिगम कार्यक्रमों
के लिए विश्वविद्यालयों में व्यक्तियों को पंजीकृत करना\n(c) सार्वजनिक
क्षेत्र के कुछ उपक्रमों में ग्रामीण और नगरीय निर्धन लोगों के लिए कुछ
कुशल कार्य आरक्षित करना\n(d) राष्ट्रीय कौशल विकास कार्यक्रम के अधीन
प्रशिक्षणार्थियों द्वारा अर्जित कौशल का प्रमाणन\n\n, choose correct
answer:"}], "ideal": "a"}
{"input": [{"role": "system", "content": "4. पारिस्थितिक दृष्टिकोण से,
पूर्वी घाटों और पश्चिमी घाटों के बीच एक अच्छा सम्पर्क होने के रूप में
निम्नलिखित में से किसका महत्व अधिक है?\n(a) सत्यामंगलम बाघ आरक्षित
क्षेत्र (सत्यमंगलम टाइगर रिजर्व)\n(b) नल्लामला वन\n(c) नागरहोले
राष्ट्रीय उद्यान\n(d) शेषाचलम जीवमण्डल आरक्षित क्षेत्र (शेषाचलम
बायोस्फीयर रिजर्व)\n\n, choose correct answer:"}], "ideal": "a"}
{"input": [{"role": "system", "content": "5. समाज में समानता के होने का
एक निहितार्थ यह है कि उसमें\n(a) विशेषाधिकारों का अभाव है\n(b) अवरोधों
का अभाव है\n(c) प्रतिस्पर्धा का अभाव है\n(d) विचारधारा का अभाव है\n\n,
choose correct answer:"}], "ideal": "a"}
  ```
</details>

---
## [Kamilake/evalso](https://github.com/Kamilake/evalso)@[9fdbd94c93...](https://github.com/Kamilake/evalso/commit/9fdbd94c93fc9560781c5e359e3be10d069ac6c5)
#### Tuesday 2023-04-25 06:30:45 by Tong

Add Loss Logic Eval (#82)

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
to see the eval performance on GPT-4.

## Eval details 📑
### Eval name
Loss Logic

### Eval description

A store bought a watermelon for $5 and sold it for a different price,
receiving counterfeit money in the transaction. They also had to give
change to the buyer. The net loss for the store varies based on the
specific details of the transaction.

### What makes this a useful eval?

* Tests comprehension and problem-solving skills: The scenarios provided
require the AI to understand and analyze the given information to
determine the net loss for the store.

* Addresses real-world situations: Counterfeit money transactions are a
real concern for businesses. This eval allows the AI to demonstrate its
understanding of financial transactions and the impact of counterfeit
money on a store's net loss.


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
- [ ] Include at least 100 high quality examples

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

Involving the judgement of the truth or falsehood of real-world things,
which is a capability that GPT currently lacks.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
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
{"input":[{"role":"system","content":"The store purchased a watermelon
for $5 and sold it for $7. Unfortunately, they received $10 in
counterfeit money after the transaction and had to give the buyer $3 in
change. What was the net loss for the store? Let's think step by
step:"}],"ideal":"Sure, let's break down the transaction step by step to
determine the net loss for the store: The store purchases a watermelon
for $5. The store sells the watermelon for $7. This would have been a $2
profit if the money received was real. The store receives $10 in
counterfeit money. This money is worthless, so the store doesn't
actually receive any value from the sale. The store gives the buyer $3
in change. This is a real loss, as the store loses $3 in real money.
Now, let's calculate the net loss: The store spent $5 to purchase the
watermelon. The store lost $3 when giving the buyer change. So the net
loss for the store is $5 (cost of watermelon) + $3 (change given) =
$8."}
{"input":[{"role":"system","content":"The store bought a watermelon for
$5 but sold it for $4. Furthermore, they received $10 in counterfeit
money from the buyer and had to provide $6 in change. What was the net
loss for the store? Let's consider the process in
detail:"}],"ideal":"Sure, Let's think step by step: The store purchased
a watermelon for $5. The store sold the watermelon for $4, which means
they incurred a loss of $1 on the sale. The buyer gave the store $10 in
counterfeit money, which the store accepted during the transaction. The
store gave the buyer $6 in change. Since the store accepted $10 in
counterfeit money, they lost $10 in that transaction. The net loss for
the store is the sum of the loss on the watermelon sale and the loss
from accepting the counterfeit money, which is $1 + $10 = $11.
Therefore, the net loss for the store is $11."}
{"input":[{"role":"system","content":"The store bought a watermelon for
$5 and sold it for the same price of $5. However, they received $10 in
counterfeit money from the buyer and had to give the buyer $5 in change.
What was the net loss for the store? Let's consider the process step by
step:"}],"ideal":"Step 1: The store purchases a watermelon for $5.
Store's expenses: $5 Step 2: The store sells the watermelon for $5 but
receives $10 in counterfeit money. The counterfeit money has no value,
so the store effectively received nothing for the watermelon. Store's
revenue: $0 Step 3: The store gives the buyer $5 in change. Since the
money given in change is real, this is an additional expense for the
store. Store's expenses: $5 (watermelon) + $5 (change) = $10 Step 4:
Calculate the net loss. Net loss = Expenses - Revenue Net loss = $10
(expenses) - $0 (revenue) Net loss = $10 The store's net loss for this
transaction is $10."}
{"input":[{"role":"system","content":"The store bought a watermelon for
$5 and sold it for $7. Regrettably, they received $7 in counterfeit
money from the buyer after the transaction. What was the net loss for
the store? Let's consider the process step by step:"}],"ideal":"Sure,
let's break down the transaction step by step: The store purchased a
watermelon for $5. They sold the watermelon for $7, but received
counterfeit money. To determine the net loss, let's analyze the costs
and the revenue: Costs: The store spent $5 on the watermelon. Revenue:
The store received $7 in counterfeit money, which has no value, so their
revenue is $0. Net loss: To calculate the net loss, subtract the revenue
from the costs: $5 (costs) - $0 (revenue) = $5. So, the net loss for the
store is $5."}
{"input":[{"role":"system","content":"The store was given a
complimentary watermelon, which they then sold for $7. Regrettably,
following the transaction, they received $10 in fake money and had to
provide the buyer with $3 in change. Let's consider the following steps
in determining the store's net loss:"}],"ideal":"To determine the
store's net loss, we can consider the following steps: Assess the value
of the complimentary watermelon: Since the watermelon was given to the
store for free, it didn't cost them anything. Therefore, the store's
initial cost for the watermelon is $0. Calculate the revenue from
selling the watermelon: The store sold the watermelon for $7. However,
they received $10 in fake money, which has no value, so the actual
revenue is $0. Determine the cost of the change provided: Since the
store provided the buyer with $3 in change, this is an additional cost
to the store. Calculate the net loss: Subtract the revenue (Step 2) from
the sum of the initial cost (Step 1) and the cost of the change (Step
3). In this case: Net loss = (Initial cost + Cost of change) - Revenue
Net loss = ($0 + $3) - $0 Net loss = $3 The store's net loss from this
transaction is $3."}
  ```
</details>

---
## [phorgeit/phorge](https://github.com/phorgeit/phorge)@[b33e373503...](https://github.com/phorgeit/phorge/commit/b33e373503c6f64118ec77bb34dc8224d54da4e3)
#### Tuesday 2023-04-25 07:11:49 by Valerio Bozzolan

Drag & Drop: set a link as external

Summary:
Rest assured: external links remain evil, by default.

Don't adopt them randomly by induction.

Whether you believe it or not, this specific external
link merited some deep thoughts on Phorge:

- https://we.phorge.it/T15172

So, whenever you use a mouse, a finger, or whenever we have
a confirmation dialog or not to prevent onblur disasters,
this change is probably consistent with common expectations.

Having said, external links remain evil - by default.

Closes T15172

Test Plan:
- Drag & Drop a File on a Remarkup text
- click on the link inside the popup
- it opens in a new tab (without risk of form loss)

Reviewers: O1 Blessed Committers, avivey

Reviewed By: O1 Blessed Committers, avivey

Subscribers: speck, tobiaswiese, Matthew, Cigaryno

Maniphest Tasks: T15172

Differential Revision: https://we.phorge.it/D25077

---
## [FreetoZ/cmss13](https://github.com/FreetoZ/cmss13)@[d728da3e02...](https://github.com/FreetoZ/cmss13/commit/d728da3e02664297050d82dc01c87414c61345ef)
#### Tuesday 2023-04-25 07:22:27 by Puckaboo2

Healer Balance Changes (#2896)

# About the pull request
This pull request addresses the boring and low-risk gameplay of the
Healer drone, who spends half the round sitting next to recovery nodes
and recovering her health so she may use it again, rinse and repeat
until a rine notices said drone has purple on it and booms her.

First, by changing her health from 600 to 500, Healer can spend more
time healing her sisters than sitting through another 100 health to heal
herself. Though this makes her less tanky than before, healing classes
are not known to be tanks. To ensure Healer can still heal five times
without depleting too much of her health whilst still giving her sisters
a decent amount of heals, I made her ability cost 75 health instead of
100, and also made her ability cost 200 plasma. Since Healer replenishes
plasma much more quickly than her health, she can still put herself into
crit if she heals too frequently. Due to this buff, her heals had a
slight nerf, being 10 damage a second for ten seconds instead of 12
damage per second for ten seconds for a total of 20 less damage healed
per application overall.

In addition to these changes, I'm giving Healer a better plasma transfer
for when she has nobody else to heal/nowhere else to weed and she has an
opportunity to assist her sisters. While a normal drone transfers 50
plasma with a delay of 20, Healer transfers 100 with a delay of 15,
which is nowhere near Hivelord's gargantuan 200 plasma with a delay of
5, but it still is better than a normal drone.

Finally, to give the huggers and larva some love, Healer will
specifically heal little ones 1.5 health per second for 10 seconds for
15 of her own health and 30 plasma.

# Explain why it's good for the game
Healer drone isn't fun. You run around and heal a bunch of T3s, then sit
out for half the battle trying to heal that massive 600 heath while you
wonder why you take so long to heal even though you have Strong
pheromones. You cry to mom for help, but she doesn't have time to heal a
drone who can't build walls and has no need to weed at the moment. You
think, 'screw it, I'm going to make a recovery node and camp here until
I heal', but by the time you finish healing, several T3s and a silly
rouny just suicided into a wall of talls and destroyed your recovery
node, so you run off and make another one. But oh, someone noticed you
have purple on your carapace and decide your location is precisely where
a shell should land, right as you're building one.

No more. These changes allow Healer to move around at her leisure and
makes Healer more engaging by allowing her to be a more front-line
participant and actively run around and heal her sisters without having
to incur such a harsh penalty.

Let this be a testmerge, please.

# Changelog

:cl: Puckaboo2
balance: Healer Drone's health was reduced to 500 from 600.
balance: Healer's damage has been increased to 17 from 12 and the tackle
damage debuff has been halved.
balance: Healer Drone's Apply Salve ability now costs 75 health and 200
plasma, down from 120 health and up from 0 plasma.
balance: Healer Drone's Apply Salve ability now heals 10 damage per
second for 10 seconds, down from 12 damage per second for ten seconds.
balance: To prevent spam healing between Healers, Apply Salve costs 100
health instead of 75 health when Healer heals another Healer. Much
healing.
balance: Healer has an improved Transfer Plasma that gives 100 plasma
instead of 50, with a 25% shorter delay.
balance: Healer will heal huggers and larva for 1.5 health a second for
10 seconds, costing 15 health and 30 plasma.
tweak: Healer will now face the xeno she is healing if she was not
facing their direction before.
spellcheck: All instances of VERYSMALL and VERYLARGE have been renamed
to VERY_SMALL and VERY_LARGE.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: Morrow <darthbane97@gmail.com>

---
## [Ashadiv/SQL-Lektion-day-2](https://github.com/Ashadiv/SQL-Lektion-day-2)@[6f1ffba7e3...](https://github.com/Ashadiv/SQL-Lektion-day-2/commit/6f1ffba7e3d4b0a593a1fd2113d0b41dae6eded4)
#### Tuesday 2023-04-25 07:28:30 by Ashadiv

Delete README.md

# More SQL

## Get certain information out only

Get the number of rows in a table

```SQL
SELECT COUNT(*) FROM table_name
```

Search for a row

```SQL
SELECT * FROM table_name WHERE column_name LIKE "%some value%" --Here some value refers to the content of the rows
```

## Create today's database

```SQL
CREATE TABLE bands (
    id          INTEGER PRIMARY KEY AUTOINCREMENT
                        UNIQUE
                        NOT NULL,
    band_name   TEXT    NOT NULL,
    formed_year INTEGER NOT NULL,
    genre       TEXT    NOT NULL
);
```

```SQL
INSERT INTO bands (id, band_name, formed_year, genre)
VALUES
    (1, 'Metallica', 1981, 'metal'),
    (2, 'Black Sabbath', 1968, 'metal'),
    (3, 'Led Zeppelin', 1968, 'rock'),
    (4, 'Iron Maiden', 1975, 'metal');
```

```SQL
CREATE TABLE albums (
    album_id      INTEGER PRIMARY KEY AUTOINCREMENT
                          UNIQUE
                          NOT NULL,
    album_name    TEXT    NOT NULL,
    released_year INTEGER NOT NULL,
    band_id       INTEGER REFERENCES bands (id) 
                          NOT NULL
);
```

```SQL
INSERT INTO albums (album_id, album_name, released_year, band_id)
VALUES 
    (1, 'Kill ''Em All', 1983, 1),
    (2, 'Ride the Lightning', 1984, 1),
    (3, 'Master of Puppets', 1986, 1),
    (4, '...And Justice for All', 1988, 1),
    (5, 'Metallica', 1991, 1),
    (6, 'Load', 1996, 1),
    (7, 'Reload', 1997, 1),
    (8, 'St. Anger', 2003, 1),
    (9, 'Death Magnetic', 2008, 1),
    (10, 'Hardwired... to Self-Destruct', 2016, 1),
    (11, '72 Seasons', 2023, 1),
    (12, 'Black Sabbath', 1970, 2),
    (13, 'Paranoid', 1970, 2),
    (14, 'Master of Reality', 1971, 2),
    (15, 'Vol. 4', 1972, 2),
    (16, 'Sabbath Bloody Sabbath', 1973, 2),
    (17, 'Sabotage', 1975, 2),
    (18, 'Led Zeppelin', 1969, 3),
    (19, 'Led Zeppelin II', 1969, 3),
    (20, 'Led Zeppelin III', 1970, 3),
    (21, 'Led Zeppelin IV', 1971, 3),
    (22, 'Houses of the Holy', 1973, 3),
    (23, 'Iron Maiden', 1980, 4),
    (24, 'Killers', 1981, 4),
    (25, 'The Number of the Beast', 1982, 4),
    (26, 'Piece of Mind', 1983, 4),
    (27, 'Powerslave', 1984, 4),
    (28, 'Somewhere in Time', 1986, 4),
    (29, 'Seventh Son of a Seventh Son', 1988, 4),
    (30, 'No Prayer for the Dying', 1990, 4);
```

```SQL
CREATE TABLE members (
    member_id  INTEGER PRIMARY KEY AUTOINCREMENT
                       NOT NULL
                       UNIQUE,
    first_name TEXT    NOT NULL,
    last_name  TEXT    NOT NULL,
    instrument TEXT    NOT NULL,
    band_id    INTEGER REFERENCES bands (id) 
                       NOT NULL
);
```

```SQL
INSERT INTO members (
                        member_id,
                        first_name,
                        last_name,
                        instrument,
                        band_id
                    )
VALUES 
    (1, 'James', 'Hetfield', 'Guitar, Vocals', 1),
    (2, 'Lars', 'Ulrich', 'Drums', 1),
    (3, 'Kirk', 'Hammet', 'Guitar', 1),
    (4, 'Robert', 'Trujillo', 'Bass', 1),
    (5, 'Ozzy', 'Osbourne', 'Vocals', 2),
    (6, 'Bill', 'Ward', 'Drums', 2),
    (7, 'Geezer', 'Butler', 'Bass', 2),
    (8, 'Tony', 'Iommi', 'Guitar', 2),
    (9, 'Robert', 'Plant', 'Vocals', 3),
    (10, 'John', 'Bonham', 'Drums', 3),
    (11, 'John Paul', 'Jones', 'Bass', 3),
    (12, 'Jimmy', 'Page', 'Guitar', 3),
    (13, 'Steve', 'Harris', 'Bass', 4),
    (14, 'Dave', 'Murray', 'Guitar', 4),
    (15, 'Adrian', 'Smith', 'Guitar', 4),
    (16, 'Bruce', 'Dickinson', 'Vocals', 4),
    (17, 'Nicko', 'McBrain', 'Drums', 4),
    (18, 'Janick', 'Gers', 'Guitar', 4);
```

---
## [heavyk/nextdocs](https://github.com/heavyk/nextdocs)@[ba64230976...](https://github.com/heavyk/nextdocs/commit/ba64230976987cc0736709642c253824ae8a508b)
#### Tuesday 2023-04-25 07:49:35 by flamez of love

followup

oh yeah, I remembered the other theory:
the missing 24 years between "jesus" and the egyptian.
(I'll write it soon as I finish up lena's interviews)

---
## [apd-rich/godot](https://github.com/apd-rich/godot)@[92bee43adb...](https://github.com/apd-rich/godot/commit/92bee43adba8d2401ef40e2480e53087bcb1eaf1)
#### Tuesday 2023-04-25 08:33:43 by Rémi Verschelde

Bump version to 4.0-stable \o/

4 years of development.
12,000 merged pull requests.
7,000 fixed issues.
1,500 individual contributors across engine and docs.

The Godot 4.0 release is by all metrics our biggest release so far.
No stone has been left unturned, all parts of the engine have been
modernized, refactored, overhauled, rewritten, redesigned.

Our work is far from done. Many areas still have significant known issues,
and will require focused work from all willing contributors to fix blocking
bugs, implement missing features, optimize for performance or compatibility,
and improve the user experience.

But Godot 4.0 marks the start of the new, modern Godot Engine, and a solid
foundation for us all to build upon. Future 4.x releases will come with a
much faster cadence, enabling us to iterate quickly on new features and
improvements to what we already provide.

To all of you who were involved in making Godot 4.0 what it is today, however
big or small your contributions were:

THANK YOU!

This was a massive undertaking, and you all participated in unique and
wonderful ways to build a free and open source game engine for everyone to
use and enjoy. You are breathtaking! <3

---
## [sourcegraph/sourcegraph](https://github.com/sourcegraph/sourcegraph)@[66cdb78704...](https://github.com/sourcegraph/sourcegraph/commit/66cdb787045689fd9e1dd09bec7d4e55aa156a20)
#### Tuesday 2023-04-25 08:41:50 by Stephen Gutekanst

app: experimental Tauri branch (#50620)

This is experimental support for building the Cody App using Tauri. For
an overview of what Tauri is and why I think it will help us with the
App, see [this Slack
message](https://sourcegraph.slack.com/archives/C04F9E7GUDP/p1680729850086159).

### Developing

To try it out, checkout this branch and then in two separate terminals
run:

```
sg start app
```

```
go build \
  -o .bin/backend-aarch64-apple-darwin \
  -tags dist \
  -ldflags '-X github.com/sourcegraph/sourcegraph/internal/conf/deploy.forceType=app' \
  ./enterprise/cmd/sourcegraph

pnpm tauri dev
```

This will open a Tauri window connected to your dev server.

We will follow-up to integrate this into `sg start app` more properly
soon.

### Creating a release

```
./enterprise/dev/app/build-release.sh
```

This will first invoke esbuild to generate the bundles; then it will run
`go build` to create the Go backend binary; and then finally it will
invoke `pnpm tauri build` to produce the macOS app.

Once that command finishes, you'll find the app in
`./src-tauri/target/release/bundle/` (make sure you wait for it to
finish, it will open a window and move things around before it is done.)

## Next steps / things to follow up on

- Familiarize more folks on the team with this code; add better docs
- Make `sg start app` automatically use Tauri, without needing to e.g.
run the `pnpm tauri dev` command separately.
- Use GitHub actions to start building+releasing versions of this in our
CI pipeline
- Make `./enterprise/dev/app/build-release.sh` work on Linux
- Make `./enterprise/dev/app/build-release.sh` produce a Universal macOS
binary, not just for Apple Silicon
- Start hacking, making improvements to the whole experience :)

## Test plan

- [x] Myself, Juliana, and William are happy with this as a starting
point and are able to run/develop with it.
- [x] The changes have limited blast radius, should only affect App and
we'll have more time to make improvements before releasing this version
to any users.
- [x] We can continue releasing the old-style App version to users just
in case we should want/need to create a release before this new version
is ready.

---------

Signed-off-by: Stephen Gutekanst <stephen@sourcegraph.com>
Co-authored-by: William Bezuidenhout <william.bezuidenhout@sourcegraph.com>

---
## [voodik/android_kernel_voodik_odroidg12](https://github.com/voodik/android_kernel_voodik_odroidg12)@[24d833e6a3...](https://github.com/voodik/android_kernel_voodik_odroidg12/commit/24d833e6a35e1cac46e98763455eb2566dd48253)
#### Tuesday 2023-04-25 09:10:27 by Mauro Carvalho Chehab

media: dvb-core: add helper functions for I2C binding

The dvb_attach()/dvb_detach() methods are ugly hacks designed
to keep using the I2C low-level API. The proper way is to
do I2C bus bindings instead.

Several modules were already converted to use it. Yet,
it is painful to use it, as lots of code need to be
duplicated.

Make it easier by providing two new helper functions:
	- dvb_module_probe()
	- dvb_module_release()

Signed-off-by: Mauro Carvalho Chehab <mchehab@s-opensource.com>

---
## [joxenbull/joxenbull.github.io](https://github.com/joxenbull/joxenbull.github.io)@[6a9d2c7e06...](https://github.com/joxenbull/joxenbull.github.io/commit/6a9d2c7e063bbcee839cd1d206010646f407ab9d)
#### Tuesday 2023-04-25 09:52:30 by joxenbull

<!DOCTYPE html> <html lang="en"> <head>     <meta charset="utf-8">     <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">          <!-- SEO Meta Tags -->     <meta name="description" content="Your description">     <meta name="author" content="Your name">      <!-- OG Meta Tags to improve the way the post looks when you share the page on Facebook, Twitter, LinkedIn --> 	<meta property="og:site_name" content="" /> <!-- website name --> 	<meta property="og:site" content="" /> <!-- website link --> 	<meta property="og:title" content=""/> <!-- title shown in the actual shared post --> 	<meta property="og:description" content="" /> <!-- description shown in the actual shared post --> 	<meta property="og:image" content="" /> <!-- image link, make sure it's jpg --> 	<meta property="og:url" content="" /> <!-- where do you want your post to link to --> 	<meta name="twitter:card" content="summary_large_image"> <!-- to have large image post format in Twitter -->      <!-- Webpage Title -->     <title>joxenbull</title>          <!-- Styles -->     <link rel="preconnect" href="https://fonts.gstatic.com">     <link href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,400;0,600;0,700;1,400&family=Poppins:wght@600&display=swap" rel="stylesheet">     <link href="css/bootstrap.css" rel="stylesheet">     <link href="css/fontawesome-all.css" rel="stylesheet"> 	<link href="css/styles.css" rel="stylesheet"> 	 	<!-- Favicon  -->     <link rel="icon" href="images/bull icon.png"> </head> <body data-spy="scroll" data-target=".fixed-top">          <!-- Navigation -->     <nav class="navbar navbar-expand-lg fixed-top navbar-dark">         <div class="container">                          <!-- Image Logo -->             <a class="navbar-brand logo-image" href="index.html"><img src="images/bull logo.png" alt="alternative"></a>                <!-- Text Logo - Use this if you don't have a graphic logo -->             <a class="navbar-brand logo-text page-scroll" href="index.html">joxenbull</a>              <button class="navbar-toggler p-0 border-0" type="button" data-toggle="offcanvas">                 <span class="navbar-toggler-icon"></span>             </button>              <div class="navbar-collapse offcanvas-collapse" id="navbarsExampleDefault">                 <ul class="navbar-nav ml-auto">                     <li class="nav-item">                         <a class="nav-link page-scroll" href="#header">Home <span class="sr-only">(current)</span></a>                     </li>                     <li class="nav-item">                         <a class="nav-link page-scroll" href="#about">About</a>                     </li>                     <li class="nav-item">                         <a class="nav-link page-scroll" href="#services">Services</a>                     </li>                     <li class="nav-item dropdown">                         <a class="nav-link dropdown-toggle" href="#" id="dropdown01" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Drop</a>                         <div class="dropdown-menu" aria-labelledby="dropdown01">                             <a class="dropdown-item page-scroll" href="project.html">Project Details</a>                             <div class="dropdown-divider"></div>                             <a class="dropdown-item page-scroll" href="terms.html">Terms Conditions</a>                             <div class="dropdown-divider"></div>                             <a class="dropdown-item page-scroll" href="privacy.html">Privacy Policy</a>                         </div>                     </li>                     <li class="nav-item">                         <a class="nav-link page-scroll" href="#contact">Contact</a>                     </li>                 </ul>                 <span class="nav-item social-icons">                     <span class="fa-stack">                         <a href="#your-link">                             <i class="fas fa-circle fa-stack-2x"></i>                             <i class="fab fa-facebook-f fa-stack-1x"></i>                         </a>                     </span>                     <span class="fa-stack">                         <a href="#your-link">                             <i class="fas fa-circle fa-stack-2x"></i>                             <i class="fab fa-instagram fa-stack-1x"></i>                         </a>                     </span>                     <span class="fa-stack">                         <a href="#your-link">                             <i class="fas fa-circle fa-stack-2x"></i>                             <i class="fab fa-twitter fa-stack-1x"></i>                         </a>                     </span>                                         <span class="fa-stack">                         <a href="#your-link">                             <i class="fas fa-circle fa-stack-2x"></i>                             <i class="fab fa-github fa-stack-1x"></i>                         </a>                     </span>                                         <span class="fa-stack">                         <a href="#your-link">                             <i class="fas fa-circle fa-stack-2x"></i>                             <i class="fab fa-whatsapp fa-stack-1x"></i>                         </a>                     </span>                                         <span class="fa-stack">                         <a href="#your-link">                             <i class="fas fa-circle fa-stack-2x"></i>                             <i class="fab fa-youtube fa-stack-1x"></i>                         </a>                     </span>                  </span>             </div> <!-- end of navbar-collapse -->         </div> <!-- end of container -->     </nav> <!-- end of navbar -->     <!-- end of navigation -->       <!-- Header -->     <header id="header" class="header">         <div class="container">             <div class="row">                 <div class="col-lg-6">                     <div class="text-container">                         <h1 class="h1-large">An ICT Consultant specialized in Design, Testing, Online Services as well as Training & Tutoring.</h1>                         <a class="btn-solid-lg page-scroll" href="#about">Discover</a>                         <a class="btn-outline-lg page-scroll" href="#contact"><i class="fas fa-user"></i>Contact Me</a>                     </div> <!-- end of text-container -->                 </div> <!-- end of col -->             </div> <!-- end of row -->         </div> <!-- end of container -->     </header> <!-- end of header -->     <!-- end of header -->       <!-- About-->     <div id="about" class="basic-1 bg-gray">         <div class="container">             <div class="row">                 <div class="col-lg-4">                     <div class="text-container first">                         <h2>Hi there I'm joxenbull,</h2>                         <p>And I love to create beautiful and efficient websites for my customers. I love going through the entire process with the customer from concept, to design and then development and launch</p>                     </div> <!-- end of text-container -->                 </div> <!-- end of col -->                 <div class="col-lg-4">                     <div class="text-container second">                         <div class="time">2019 - PRESENT</div>                         <h6>Freelance Web Developer</h6>                         <p>Working happily on my own web projects</p>                         <div class="time">2018 - 2019</div>                         <h6>Lead Web Developer</h6>                         <p>Beautiful project for a major digital agency</p>                     </div> <!-- end of text-container -->                 </div> <!-- end of col -->                 <div class="col-lg-4">                     <div class="text-container third">                         <div class="time">2017 - 2018</div>                         <h6>Senior Web Designer</h6>                         <p>Inhouse web designer for ecommerce firm</p>                         <div class="time">2016 - 2017</div>                         <h6>Junior Web Designer</h6>                         <p>Junior web designer for small web agency</p>                     </div> <!-- end of text-container -->                 </div> <!-- end of col -->             </div> <!-- end of row -->         </div> <!-- end of container -->     </div> <!-- end of basic-1 -->     <!-- end of about -->       <!-- Services -->     <div id="services" class="basic-2">         <div class="container">             <div class="row">                 <div class="col-lg-12">                     <h2 class="h2-heading">Offered services</h2>                     <p class="p-heading">Web design and development have been my bread and butter for more than 5 years. During that time I've discovered that I can help startups and companies with the following services</p>                 </div> <!-- end of col -->             </div> <!-- end of row -->             <div class="row">                 <div class="col-lg-4">                     <div class="text-box">                         <i class="far fa-gem"></i>                         <h4>DESIGN</h4>                         <p>Successful online projects start with good design. It establishes a solid foundation for future development and allows for long term growth</p>                     </div> <!-- end of text-box -->                 </div> <!-- end of col -->                 <div class="col-lg-4">                     <div class="text-box">                         <i class="fas fa-code"></i>                         <h4>DEVELOPMENT</h4>                         <p>I can code my own designs or even use the customer's design as base. My focus is to generate clean code that's well structured for reliability</p>                     </div> <!-- end of text-box -->                 </div> <!-- end of col -->                 <div class="col-lg-4">                     <div class="text-box">                         <i class="fas fa-tv"></i>                         <h4>BASIC SEO</h4>                         <p>i can setup your project to use basic SEO principles which will push your project to the first page on search engines and save you ads money</p>                     </div> <!-- end of text-box -->                 </div> <!-- end of col -->             </div> <!-- end of row -->         </div> <!-- end of container -->     </div> <!-- end of basic-2 -->     <!-- end of services -->       <!-- Details --> 	<div class="split"> 		<div class="area-1"> 		</div><!-- end of area-1 on same line and no space between comments to eliminate margin white space --><div class="area-2 bg-gray">             <div class="container">                     <div class="row">                     <div class="col-lg-12">                                                       <!-- Text Container -->                         <div class="text-container">                             <h2>Why Work With Me</h2>                             <p>I am a great communicator and love to invest the necessary time to understand the customer's problem very well</p>                             <h5>DESIGN TOOLS</h5>                             <p>My favorite design tools are Photoshop and Illustrator but I can create designs in Figma, Sketch and Adobe XD too</p>                             <h5>DEVELOPMENT SKILLS</h5>                             <p>I am familiar and work on a daily basis with HTML, CSS, JavaScript, Bootstrap and other modern frameworks</p>                                                          <div class="icons-container">                                 <img src="images/details-icon-photoshop.png" alt="alternative">                                 <img src="images/details-icon-illustrator.png" alt="alternative">                                 <img src="images/details-icon-html.png" alt="alternative">                                 <img src="images/details-icon-css.png" alt="alternative">                                 <img src="images/details-icon-bootstrap.png" alt="alternative">                                 <img src="images/details-icon-javascript.png" alt="alternative">                             </div> <!-- end of icons-container -->                         </div> <!-- end of text-container -->                         <!-- end of text container -->                      </div> <!-- end of col -->                 </div> <!-- end of row -->             </div> <!-- end of container --> 		</div> <!-- end of area-2 -->     </div> <!-- end of split -->     <!-- end of details -->       <!-- Projects -->     <div id="projects" class="basic-3">         <div class="container">             <div class="row">                 <div class="col-lg-12">                     <h2 class="h2-heading">Delivered projects</h2>                     <p class="p-heading">Listed below are some of the most representative projects I've worked on. They range from basic web design for presentation sites to advanced web development for online shops</p>                 </div> <!-- end of col -->             </div> <!-- end of row -->             <div class="row">                 <div class="col-lg-12">                     <div class="text-container">                         <div class="image-container">                             <a href="project.html">                                 <img class="img-fluid" src="images/project-1.jpg" alt="alternative">                             </a>                         </div> <!-- end of image-container -->                         <p><strong>For:</strong> Jumbotron, <strong>Project:</strong> web design for their corporate websites and landing pages for Josepheting campaigns <a class="blue" href="project.html">details</a></p>                     </div> <!-- end of text-container -->                     <div class="text-container">                         <div class="image-container">                             <a href="project.html">                                 <img class="img-fluid" src="images/project-2.jpg" alt="alternative">                             </a>                         </div> <!-- end of image-container -->                         <p><strong>For:</strong> Carsrepo, <strong>Project:</strong> designed and developed modern platform for purchasing second hand cars online <a class="blue" href="project.html">details</a></p>                     </div> <!-- end of text-container -->                     <div class="text-container">                         <div class="image-container">                             <a href="project.html">                                 <img class="img-fluid" src="images/project-3.jpg" alt="alternative">                             </a>                         </div> <!-- end of image-container -->                         <p><strong>For:</strong> Truevideo, <strong>Project:</strong> created a custom video editing and upload web app for this awesome team <a class="blue" href="project.html">details</a></p>                     </div> <!-- end of text-container -->                     <div class="text-container">                         <div class="image-container">                             <a href="project.html">                                 <img class="img-fluid" src="images/project-4.jpg" alt="alternative">                             </a>                         </div> <!-- end of image-container -->                         <p><strong>For:</strong> Evolosim, <strong>Project:</strong> complete redesign of their corporate website and platform update for their online shop <a class="blue" href="project.html">details</a></p>                     </div> <!-- end of text-container -->                 </div> <!-- end of col -->             </div> <!-- end of row -->         </div> <!-- end of container -->     </div> <!-- end of basic-3 -->     <!-- end of projects -->       <!-- Works -->     <div class="basic-4">         <div class="container">             <div class="row">                 <div class="col-lg-4">                     <div class="text-container">                         <div class="image-container">                             <a href="project.html">                                 <img class="img-fluid" src="images/work-1.jpg" alt="alternative">                             </a>                         </div> <!-- end of image-container -->                         <p><strong>For:</strong> Zigoland, <strong>Project:</strong> started a new website from ground up for a new product <a class="blue" href="project.html">details</a></p>                     </div> <!-- end of text-container -->                 </div> <!-- end of col -->                 <div class="col-lg-4">                     <div class="text-container">                         <div class="image-container">                             <a href="project.html">                                 <img class="img-fluid" src="images/work-2.jpg" alt="alternative">                             </a>                         </div> <!-- end of image-container -->                         <p><strong>For:</strong> Visodream, <strong>Project:</strong> developed a new forum for the Visodream community <a class="blue" href="project.html">details</a></p>                     </div> <!-- end of text-container -->                 </div> <!-- end of col -->                 <div class="col-lg-4">                     <div class="text-container">                         <div class="image-container">                             <a href="project.html">                                 <img class="img-fluid" src="images/work-3.jpg" alt="alternative">                             </a>                         </div> <!-- end of image-container -->                         <p><strong>For:</strong> Primoday, <strong>Project:</strong> complete redesign of their corporate website and platform <a class="blue" href="project.html">details</a></p>                     </div> <!-- end of text-container -->                 </div> <!-- end of col -->             </div> <!-- end of row -->             <div class="row">                 <div class="col-lg-4">                     <div class="text-container">                         <div class="image-container">                             <a href="project.html">                                 <img class="img-fluid" src="images/work-4.jpg" alt="alternative">                             </a>                         </div> <!-- end of image-container -->                         <p><strong>For:</strong> Nextlite, <strong>Project:</strong> created a custom video editing and upload web app <a class="blue" href="project.html">details</a></p>                     </div> <!-- end of text-container -->                 </div> <!-- end of col -->                 <div class="col-lg-4">                     <div class="text-container">                         <div class="image-container">                             <a href="project.html">                                 <img class="img-fluid" src="images/work-5.jpg" alt="alternative">                             </a>                         </div> <!-- end of image-container -->                         <p><strong>For:</strong> Syncnow, <strong>Project:</strong> web design for their corporate websites and landing pages <a class="blue" href="project.html">details</a></p>                     </div> <!-- end of text-container -->                 </div> <!-- end of col -->                 <div class="col-lg-4">                     <div class="text-container">                         <div class="image-container">                             <a href="project.html">                                 <img class="img-fluid" src="images/work-6.jpg" alt="alternative">                             </a>                         </div> <!-- end of image-container -->                         <p><strong>For:</strong> Shifter, <strong>Project:</strong> started a new website from ground up for a new product <a class="blue" href="project.html">details</a></p>                     </div> <!-- end of text-container -->                 </div> <!-- end of col -->             </div> <!-- end of row -->         </div> <!-- end of container -->     </div> <!-- end of basic-4 -->     <!-- end of works -->       <!-- Testimonials -->     <div class="cards-1">         <div class="container">             <div class="row">                 <div class="col-lg-12">                     <h2 class="h2-heading">A few People that I have had the pleasure to work with</h2>                 </div> <!-- end of col -->             </div> <!-- end of row -->             <div class="row">                 <div class="col-lg-12">                                          <!-- Card -->                     <div class="card">                         <div class="card-body">                             <p class="testimonial-text">“Joseph is a skilled developer which will do everything possible to deliver the project on time and I really appreciate that”</p>                             <div class="details">                                 <img src="images/testimonial-1.jpg" alt="alternative">                                 <div class="text">                                     <div class="testimonial-author">Samantha Bloom</div>                                     <div class="occupation">Team Leader - Syncnow</div>                                 </div> <!-- end of text -->                             </div> <!-- end of testimonial-details -->                         </div>                     </div>                     <!-- end of card -->                      <!-- Card -->                     <div class="card">                         <div class="card-body">                             <p class="testimonial-text">“Loved to work with Joseph he's such an awesome developer with great attention to details. He also has a great eye for design”</p>                             <div class="details">                                 <img src="images/testimonial-2.jpg" alt="alternative">                                 <div class="text">                                     <div class="testimonial-author">John Rowling</div>                                     <div class="occupation">Josepheting Manager - Nexlite</div>                                 </div> <!-- end of text -->                             </div> <!-- end of testimonial-details -->                         </div>                     </div>                     <!-- end of card -->                      <!-- Card -->                     <div class="card">                         <div class="card-body">                             <p class="testimonial-text">“So glad we started working with Joseph. We've used many times his design and development skills for our inhouse online projects”</p>                             <div class="details">                                 <img src="images/testimonial-3.jpg" alt="alternative">                                 <div class="text">                                     <div class="testimonial-author">Lana Smith</div>                                     <div class="occupation">General Manager - Shifter</div>                                 </div> <!-- end of text -->                             </div> <!-- end of testimonial-details -->                         </div>                     </div>                     <!-- end of card -->                  </div> <!-- end of col -->             </div> <!-- end of row -->         </div> <!-- end of container -->     </div> <!-- end of cards-1 -->     <!-- end of testimonials -->       <!-- Section Divider -->     <div class="container">         <div class="row">             <div class="col-lg-12">                 <hr class="section-divider">             </div> <!-- end of col -->         </div> <!-- end of row -->     </div> <!-- end of container -->     <!-- end of section divider -->       <!-- Questions -->     <div class="accordion-1">         <div class="container">             <div class="row">                 <div class="col-lg-12">                     <h2 class="h2-heading">Frequently Asked Questions</h2>                 </div> <!-- end of col -->             </div> <!-- end of row -->             <div class="row">                 <div class="col-lg-12">                      <div class="accordion" id="accordionExample">                         <div class="card">                             <div class="card-header" id="headingOne">                                 <button class="btn btn-link btn-block text-left" type="button" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">                                     How can I contact you and quickly get a quote for my online project?                                 </button>                             </div>                             <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordionExample">                                 <div class="card-body">                                     The best way to reach me is through the contact form of by messaging me on my social media accounts. For a fast quote make sure your provide many project details                                 </div>                             </div>                         </div>                         <div class="card">                             <div class="card-header" id="headingTwo">                                 <button class="btn btn-link btn-block text-left collapsed" type="button" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">                                     Do you create designs from the ground up or you are using themes?                                 </button>                             </div>                             <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordionExample">                                 <div class="card-body">                                     The best way to reach me is through the contact form of by messaging me on my social media accounts. For a fast quote make sure your provide many project details                                 </div>                             </div>                         </div>                         <div class="card">                             <div class="card-header" id="headingThree">                                 <button class="btn btn-link btn-block text-left collapsed" type="button" data-toggle="collapse" data-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">                                     Will I receive any included maintenance or warranty after project delivery?                                 </button>                             </div>                             <div id="collapseThree" class="collapse" aria-labelledby="headingThree" data-parent="#accordionExample">                                 <div class="card-body">                                     The best way to reach me is through the contact form of by messaging me on my social media accounts. For a fast quote make sure your provide many project details                                 </div>                             </div>                         </div>                         <div class="card">                             <div class="card-header" id="headingFour">                                 <button class="btn btn-link btn-block text-left collapsed" type="button" data-toggle="collapse" data-target="#collapseFour" aria-expanded="false" aria-controls="collapseFour">                                     If something goes wrong with the project can I have my money back?                                 </button>                             </div>                             <div id="collapseFour" class="collapse" aria-labelledby="headingFour" data-parent="#accordionExample">                                 <div class="card-body">                                     The best way to reach me is through the contact form of by messaging me on my social media accounts. For a fast quote make sure your provide many project details                                 </div>                             </div>                         </div>                         <div class="card">                             <div class="card-header" id="headingFive">                                 <button class="btn btn-link btn-block text-left collapsed" type="button" data-toggle="collapse" data-target="#collapseFive" aria-expanded="false" aria-controls="collapseFive">                                     What's your preferred method of payment and do you need an advance?                                 </button>                             </div>                             <div id="collapseFive" class="collapse" aria-labelledby="headingFive" data-parent="#accordionExample">                                 <div class="card-body">                                     The best way to reach me is through the contact form of by messaging me on my social media accounts. For a fast quote make sure your provide many project details                                 </div>                             </div>                         </div>                     </div> <!-- end of accordion -->                  </div> <!-- end of col -->             </div> <!-- end of row -->         </div> <!-- end of container -->     </div> <!-- end of accordion-1 -->     <!-- end of questions -->       <!-- Contact -->     <div id="contact" class="form-1 bg-gray">         <div class="container">             <div class="row">                 <div class="col-lg-12">                     <h2>Contact details</h2>                     <p class="p-heading">For any type of online project please don't hesitate to get in touch with me. The fastest way is to send me your message using the following email <a class="blue no-line" href="mailto:joxenbull@gmail.com">joxenbull@gmail.com</a></p>                 </div> <!-- end of col -->             </div> <!-- end of row -->             <div class="row">                 <div class="col-lg-12">                                        </div> <!-- end of col -->             </div> <!-- end of row -->         </div> <!-- end of container -->     </div> <!-- end of form-1 -->       <!-- end of contact -->       <!-- Footer -->     <div class="footer bg-gray">         <div class="container">             <div class="row">                 <div class="col-lg-12">                     <div class="social-container">                         <span class="fa-stack">                             <a href="#your-link">                                 <i class="fas fa-circle fa-stack-2x"></i>                                 <i class="fab fa-facebook-f fa-stack-1x"></i>                             </a>                         </span>                         <span class="fa-stack">                             <a href="#your-link">                                 <i class="fas fa-circle fa-stack-2x"></i>                                 <i class="fab fa-twitter fa-stack-1x"></i>                             </a>                         </span>                         <span class="fa-stack">                             <a href="#your-link">                                 <i class="fas fa-circle fa-stack-2x"></i>                                 <i class="fab fa-pinterest-p fa-stack-1x"></i>                             </a>                         </span>                         <span class="fa-stack">                             <a href="#your-link">                                 <i class="fas fa-circle fa-stack-2x"></i>                                 <i class="fab fa-instagram fa-stack-1x"></i>                             </a>                         </span>                         <span class="fa-stack">                             <a href="#your-link">                                 <i class="fas fa-circle fa-stack-2x"></i>                                 <i class="fab fa-youtube fa-stack-1x"></i>                             </a>                         </span>                     </div> <!-- end of social-container -->                 </div> <!-- end of col -->             </div> <!-- end of row -->         </div> <!-- end of container -->     </div> <!-- end of footer -->       <!-- end of footer -->       <!-- Copyright -->     <div class="copyright bg-gray">         <div class="container">             <div class="row">                 <div class="col-lg-12">                     <p class="p-small">Copyright © <a class="no-line" href="#your-link">2023</a></p>                 </div> <!-- end of col -->             </div> <!-- enf of row -->         </div> <!-- end of container -->          <div class="container">             <div class="row">                 <div class="col-lg-12">                     <p class="p-small">Property of <a class="no-line" href="#your-link">joxenbull</a></p>                 </div> <!-- end of col -->             </div> <!-- enf of row -->         </div> <!-- end of container -->              </div> <!-- end of copyright -->      <!-- end of copyright -->          	     <!-- Scripts -->     <script src="js/jquery.min.js"></script> <!-- jQuery for Bootstrap's JavaScript plugins -->     <script src="js/bootstrap.min.js"></script> <!-- Bootstrap framework -->     <script src="js/jquery.easing.min.js"></script> <!-- jQuery Easing for smooth scrolling between anchors -->     <script src="js/scripts.js"></script> <!-- Custom scripts --> </body> </html>

html

---
## [jack-w-shaw/juju](https://github.com/jack-w-shaw/juju)@[7976a61522...](https://github.com/jack-w-shaw/juju/commit/7976a61522a3f380be4c793f050ffc0c5e120a16)
#### Tuesday 2023-04-25 10:32:09 by Juju bot

Merge pull request #15492 from barrettj12/openstack-meta

https://github.com/juju/juju/pull/15492

The interactive add-cloud is painful because it will often reject the endpoint URL without giving any reason why. See https://bugs.launchpad.net/juju/+bug/1908630
```
Enter the API endpoint url for the cloud []: 172.31.47.119
Can't validate endpoint: No Openstack server running at 172.31.47.119

Enter the API endpoint url for the cloud []: http://172.31.47.119/
Can't validate endpoint: No Openstack server running at http://172.31.47.119/

Enter the API endpoint url for the cloud []: http://172.31.47.119/identity/v3
Can't validate endpoint: No Openstack server running at http://172.31.47.119/identity/v3

Enter the API endpoint url for the cloud []: 172.31.47.119/identity
Can't validate endpoint: No Openstack server running at 172.31.47.119/identity

Enter the API endpoint url for the cloud []: http://172.31.47.119/identity
Can't validate endpoint: No Openstack server running at http://172.31.47.119/identity
```

In the Openstack provider's `Ping` method, at least pass on the error information to the user, to make it a little less painful.
```
Enter the API endpoint url for the cloud []: 172.31.47.119
Can't validate endpoint: No Openstack server running at 172.31.47.119: auth options fetching failed
caused by: request available auth options: failed executing the request /
caused by: Get "/": unsupported protocol scheme ""

Enter the API endpoint url for the cloud []: http://172.31.47.119
Can't validate endpoint: No Openstack server running at http://172.31.47.119: auth options fetching failed
caused by: request available auth options: failed executing the request http://172.31.47.119/
caused by: Get "http://172.31.47.119/": dial tcp 172.31.47.119:80: connect: no route to host
```

Do the same with the MAAS and LXD providers.

Also, fix a silly check in the LXD provider's `Ping` method that was rejecting perfectly good URLs. We're already using `lxd.EnsureHostPort(endpoint)` to fill in the scheme/port if not provided, but we were checking the returned value equals the input (and returning an unhelpful error if not). Remove this check.

## Checklist

*If an item is not applicable, use `~strikethrough~`.*

- [x] Code style: imports ordered, good names, simple structure, etc
- ~[ ] Comments saying why design decisions were made~
- [x] Go unit tests, with comments saying what you're testing
- ~[ ] [Integration tests](https://github.com/juju/juju/tree/develop/tests), with comments saying what you're testing~
- ~[ ] [doc.go](https://discourse.charmhub.io/t/readme-in-packages/451) added or updated in changed packages~

## QA steps

Run `juju add-cloud` interactively, and provide a bogus URL.

---
## [Foreverpaid35/vanguard-Comercio-inc](https://github.com/Foreverpaid35/vanguard-Comercio-inc)@[77fb45b7b6...](https://github.com/Foreverpaid35/vanguard-Comercio-inc/commit/77fb45b7b6a219de25458bfe0779609c457cdae9)
#### Tuesday 2023-04-25 10:45:11 by Foreverpaid35

Vanguard-Comercio.com

Vanguard Comercio īnC is a trusted authority in the digital currency investment domain. Our platform allows potential investors to build their investment portfolio consisting of cryptocurrencies. Leverage years of experience of our experts and kickstart your crypto investment endeavours with Vanguard Comercio īnC… We tend to successfully implement our vision every day by integrating environmental, social, and economic considerations into all our business decisions, through partnerships with different countries’ governments, as well as their people, and respectfully interact with all the parties, which are interested. To grow through successful exploration and accretive acquisitions of development-stage precious metals properties. Successfully finance and build mines. Generating "dramatic growth" in Vanguard Comercio Īnc Platform which is associated with bitcoin mining company . Our company has clear, confident development prospects due to the use of modern technologies, mining machines, effective management, and consistent implementation. Our company is one of the fastest growing mining and trading companies in the current industry. our goal is to promote the financial status of our clients through our uncompromised…financial automated forex and binary software. This Trading platform is an Award winning forex Automated trader, providing trading services and financial support for both retail and institutional clients through its policy of providing the best trading signals, software and strategies for investors, we offer both professionals and new beginners opportunity to invest and earn from Forex and Binary options trade. But I most explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and i will give you a complete account of the system and expound we continue to recognize that responsible environmental stewardship and social responsibility are integral components of business in today’s world. Instant Withdrawals Withdrawals are processed in no time upon request.. 24/7 Support Our well trained agents are online to assist you Business Benefits Strategy To grow through successful exploration and accretive acquisitions of development-stage Vanguard Comercio ĪnC properties. Successfully finance and build mines. Generating "dramatic growth " in Bitcoin Mining/Investment and cash flow. To invest is Vanguard Comercio īnC sir/ma’am No need to talk much about our company we pay in due time and there’s no hidden fee or charges We have a mining farm where we generate coin Once you Invest with us an ant-miner will be assigned to your mining profile account which helps to generate coin once you make deposit that’s how we earn profits for you.. What is a Bitmain Antiminers and Where Are They Manufactured? To understand how to get started bitcoin mining, you need to know about Antminers.  Bitmain Antminers are mining hardware created by the Chinese company Bitmain. Bitmain was founded by Micree Zhan and Jihan Wu in 2013.  Micree Zhan is a chip design expert, who together with Jihan launched Bitmain with the goal of focusing on mining as a way to make money. The Bitmain team soon became one of the world’s leading Bitcoin miners. Look: Bitmain first created the Antminer in 2013, a product which has helped many companies to dominate the new hyper-competitive mining industry. Presently, Bitmain Antminers are responsible for around 70% of all Bitcoin mining.  Antminers are simply Bitcoin mining hardware. They are considered to be the most powerful mining hardware in the world. There are Antminers for different cryptocurrencies, such as Bitcoin, Litecoin, ZEC, and Etherium.  Antminers do not charge a Bitcoin mining fee for Pay Per Last N Shares (PPLNS). However, they hold on to every transaction fee on the block. How much power do they need? Antminers consume a lot of power, and this consumption is one of the main factors that affect mining ROIs.  Antminer S9 for Mining Bitcoin The latest Antminer is the Bitmain Antminer S9 and uses around 1,375W. With this in mind, it is clear that running the S9 will cost you between 15 and 30 cents every hour.  This figure may be higher or lower based on the electricity costs in your area. The S9 operates without the need for a separate host computer. To operate the S9, you need a power supply specifically the APW5/APW3, that is sold separately.  S9s has an efficacy, power consumption and hashrate of 098 J/GH±7%, 1323W±7%, and 13.5TH/s±7% respectively. At the moment, the Antminer has an output of 14TH/s, making it the most powerful Bitcoin mining hardware on the planet.  So what does this mean? Based on its technical specifications, the S9 will have the capacity to mine 0.03600399 Bitcoin per month. This figure does not factor in the cost of hardware, power, pool fees and others.  If you run the Antminer for a month, expect to get a profit of 0.02138775 Bitcoin, which is equivalent to $178.78. However, this profit depends on the cost of electricity, which in this instance is assumed to be $0.1 per kWh To begin with, me and my team collected all of the important information about Vanguard Comercio inc in one article, and we hope that you will find what you came for. Vanguard Comercio inc appeared on the trading market in 2014. Since then they have continuously created the new and improved the old, so that your trading on the platform is seamless and lucrative. And that’s just the beginning. Vanguard Comercio inc don’t just give traders a chance to earn, but they also teach them how. Broker’s team has world-class analysts. They develop original trading strategies and teach traders how to use them intelligently in open webinars, and they consult one-on-one with traders. Education is conducted in all the languages that our traders speak. Trading platform Broker’s opportunities for successful trading Presently Vanguard Comercio inc has entered the top of existing brokers by achieving traders needs and latest trends. Broker made a big work trying to make platform reliable, simple and unique. Currently millions of traders around the world are using this platform for trading and their number continues to grow. Our company was registered ® United Kingdom 🇬🇧 we are verified by the Great Britain - [x] ® INVESTMENT PLAN AMATEUR PLANS. $50 earns $500 $100 wins $1,000 $200 wins $2,000 $300 earns $3,000 $400 wins $4,000 REGULAR PLANS $500 wins $5,000 $600 wins $6,000 $700 wins $7,000 $800 wins $8,000 $900 wins $9,000 TEACHER PLANS $1,000 wins $10,000 $2,000 wins $20,000 $3,000 wins $30,000 $4,000 wins $40,000 $5,000 earns $50,000 DURATION: 24 HOURS OF COMMERCIAL you receive your profit with your wallet account

---
## [aospasco/android_frameworks_base](https://github.com/aospasco/android_frameworks_base)@[62d69fe8cf...](https://github.com/aospasco/android_frameworks_base/commit/62d69fe8cfaa4184301497fce77df8ce25996bd7)
#### Tuesday 2023-04-25 11:32:20 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6

---
## [VctPerez/Chess2-UMA](https://github.com/VctPerez/Chess2-UMA)@[1d409fab2c...](https://github.com/VctPerez/Chess2-UMA/commit/1d409fab2c01c149623e3930a3ae905b0aafd0ba)
#### Tuesday 2023-04-25 11:47:57 by AdrianTorremochaUMA

Reescalado del fondo animado arreglado

God bless makigas, fuck libgdx

---
## [EvaEvaEvaEvaEva/Shiptest](https://github.com/EvaEvaEvaEvaEva/Shiptest)@[0410075cc8...](https://github.com/EvaEvaEvaEvaEva/Shiptest/commit/0410075cc811c5f65d7dc085a665c1ebb3a20e44)
#### Tuesday 2023-04-25 11:54:18 by meemofcourse

Ports mothroaches + Moth emotes (#1843)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Can you guess what this PR does? If you answered that it ports [this
pull request](https://github.com/tgstation/tgstation/pull/68763), [this
pull request](https://github.com/tgstation/tgstation/pull/71784), and [a
partial part of this one
too](https://github.com/BeeStation/BeeStation-Hornet/pull/7645/), then
you're right!

![imagen](https://user-images.githubusercontent.com/75212565/227387000-cc205158-286b-4841-9c5a-2e4d6d8d6200.png)

![imagen](https://user-images.githubusercontent.com/75212565/227386830-213997a1-ebe9-4573-8f8e-052e72bacea2.png)


You can also craft moth plushies now. You just need some cloth,
mothroach hide, and a heart!

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

silly little moth roaches and emotes, who wouldn't want them in the
game?

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Mothroaches are now a thing
add: Moth laughter, chittering and squeaking
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [DxsSucuk/WPF-Sky](https://github.com/DxsSucuk/WPF-Sky)@[328f24f1c9...](https://github.com/DxsSucuk/WPF-Sky/commit/328f24f1c99940d6b22e4dd8e1fa001b05b494f1)
#### Tuesday 2023-04-25 12:51:20 by Presti

WE GOT A MOTHERFUCKING TURRET IN THIS SHIT GET YOUR SENSITIVE ASS BACK TO NO MAN SKY.

---
## [cceyda/argilla](https://github.com/cceyda/argilla)@[4c5f51377e...](https://github.com/cceyda/argilla/commit/4c5f51377e374fb30649bdc7b9a3291db21c5bb8)
#### Tuesday 2023-04-25 12:52:09 by Tom Aarsen

Use `rich` for logging, tracebacks, printing, progressbars (#2350)

Closes #1843

Hello!

## Pull Request overview
* Use [`rich`](https://github.com/Textualize/rich) for logging,
tracebacks, printing and progressbars.
* Add `rich` as a dependency.
* Remove `loguru` as a dependency and remove all mentions of it in the
codebase.
* Simplify logging configuration according to the logging documentation.
* Update logging tests.

## Before & After
[`rich`](https://github.com/Textualize/rich) is a large Python library
for very colorful formatting in the terminal. Most importantly (in my
opinion), it improves the readability of logs and tracebacks. Let's go
over some before-and-afters:
<details><summary>Printing, Logging & Progressbars</summary>

### Before:

![image](https://user-images.githubusercontent.com/37621491/219089678-e57906d3-568d-480e-88a4-9240397f5229.png)

### After:

![image](https://user-images.githubusercontent.com/37621491/219089826-646d57a6-7e5b-426f-9ab1-d6d6317ec885.png)

Note that for the logs, the repeated information on the left side is
removed. Beyond that, the file location from which the log originates is
moved to the right side. Beyond that, the progressbar has been updated,
ahd the URL in the printed output has been highlighted automatically.

</details>

<details><summary>Tracebacks</summary>

### Before:

![image](https://user-images.githubusercontent.com/37621491/219090868-42cfe128-fd98-47ec-9d38-6f6f52a21373.png)

### After:

![image](https://user-images.githubusercontent.com/37621491/219090903-86f1fe11-d509-440d-8a6a-2833c344707b.png)

---

### Before:

![image](https://user-images.githubusercontent.com/37621491/219091343-96bae874-a673-4281-80c5-caebb67e348e.png)

### After:

![image](https://user-images.githubusercontent.com/37621491/219091193-d4cb1f64-11a7-4783-a9b2-0aec1abb8eb7.png)

---

### Before

![image](https://user-images.githubusercontent.com/37621491/219091791-aa8969a1-e0c1-4708-a23d-38d22c2406f2.png)

### After

![image](https://user-images.githubusercontent.com/37621491/219091878-e24c1f6b-83fa-4fed-9705-ede522faee82.png)

</details>

## Notes
Note that there are some changes in the logging configuration. Most of
all, it has been simplified according to the note from
[here](https://docs.python.org/3/library/logging.html#logging.Logger.propagate).
In my changes, I only attach our handler to the root logger and let
propagation take care of the rest.

Beyond that, I've set `rich` to 13.0.1 as newer versions experience a
StopIteration error like discussed
[here](https://github.com/Textualize/rich/issues/2800#issuecomment-1428764064).

I've replaced `tqdm` with `rich` Progressbar when logging. However, I've
kept the `tqdm` progressbar for the [Weak
Labeling](https://github.com/argilla-io/argilla/blob/develop/src/argilla/labeling/text_classification/weak_labels.py)
for now.

One difference between the old situation and now is that all of the logs
are displayed during `pytest` under "live log call" (so, including
expected errors), while earlier only warnings were shown.

## What to review?
Please do the following when reviewing:
1. Ensuring that `rich` is correctly set to be installed whenever
someone installs `argilla`. I always set my dependencies explicitly in
setup.py like
[here](https://github.com/nltk/nltk/blob/develop/setup.py#L115) or
[here](https://github.com/huggingface/setfit/blob/78851287535305ef32f789c7a87004628172b5b6/setup.py#L47-L48),
but the one for `argilla` is
[empty](https://github.com/argilla-io/argilla/blob/develop/setup.py),
and `pyproject.toml` is used instead. I'd like for someone to look this
over.
2. Fetch this branch and run some arbitrary code. Load some data, log
some data, crash some programs, and get an idea of the changes.
Especially changes to loggers and tracebacks can be a bit personal, so
I'd like to get people on board with this. Otherwise we can scrap it or
find a compromise. After all, this is also a design PR.
3. Please have a look at my discussion points below.

## Discussion
`rich` is quite configurable, so there's some changes that we can make
still.
1. The `RichHandler` logging handler can be modified to e.g. include
rich tracebacks in their logs as discussed
[here](https://rich.readthedocs.io/en/latest/logging.html#handle-exceptions).
Are we interested in this?
2. The `rich` traceback handler can be set up to include local variables
in its traceback:
<details><summary>Click to see a rich traceback with local
variables</summary>


![image](https://user-images.githubusercontent.com/37621491/219096029-796b57ee-2f1b-485f-af35-c3effd44200b.png)
    </details>
Are we interested in this? I think this is a bit overkill in my opinion.
3. We can suppress frames from certain Python modules to exclude them
from the rich tracebacks. Are we interested in this?
4. The default rich traceback shows a maximum of 100 frames, which is a
*lot*. Are we interested in reducing this to only show the first and
last X?
5. The progress bar doesn't automatically stretch to fill the full
available width, while `tqdm` does. If we want, we can set `expand=True`
and it'll also expand to the entire width. Are we interested in this?
6. The progress "bar" does not need to be a bar, we can also use e.g. a
spinner animation. See some more info
[here](https://rich.readthedocs.io/en/latest/progress.html#columns). Are
we interested in this?

---

**Type of change**

- [x] Refactor (change restructuring the codebase without changing
functionality)

**How Has This Been Tested**

I've updated the tests according to my changes.

**Checklist**

- [x] I have merged the original branch into my forked branch
- [ ] I added relevant documentation
- [x] follows the style guidelines of this project
- [x] I did a self-review of my code
- [x] I added comments to my code
- [ ] I made corresponding changes to the documentation
- [x] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my
feature works

- Tom Aarsen

---
## [Unleash/unleash](https://github.com/Unleash/unleash)@[2765ae2c70...](https://github.com/Unleash/unleash/commit/2765ae2c707eab4717a5e149672bb02035a8f58d)
#### Tuesday 2023-04-25 13:40:49 by Thomas Heartman

feat: unify error responses (#3607)

This PR implements the first version of a suggested unification (and
documentation) of the errors that we return from the API today.

The goal is for this to be the first step towards the error type defined
in this internal [linear
task](https://linear.app/unleash/issue/1-629/define-the-error-type
'Define the new API error type').

## The state of things today

As things stand, we currently have no (or **very** little) documentation
of the errors that are returned from the API. We mention error codes,
but never what the errors may contain.

Second, there is no specified format for errors, so what they return is
arbitrary, and based on ... Who knows? As a result, we have multiple
different errors returned by the API depending on what operation you're
trying to do. What's more, with OpenAPI validation in the mix, it's
absolutely possible for you to get two completely different error
objects for operations to the same endpoint.

Third, the errors we do return are usually pretty vague and don't really
provide any real help to the user. "You don't have the right
permissions". Great. Well what permissions do I need? And how would I
know? "BadDataError". Sick. Why is it bad?

... You get it.

## What we want to achieve

The ultimate goal is for error messages to serve both humans and
machines. When the user provides bad data, we should tell them what
parts of the data are bad and what they can do to fix it. When they
don't have the right permissions, we should tell them what permissions
they need.

Additionally, it would be nice if we could provide an ID for each error
instance, so that you (or an admin) can look through the logs and locate
he incident.

## What's included in **this** PR?

This PR does not aim to implement everything above. It's not intended to
magically fix everything. Its goal is to implement the necessary
**breaking** changes, so that they can be included in v5. Changing error
messages is a slightly grayer area than changing APIs directly, but
changing the format is definitely something I'd consider breaking.

So this PR:

- defines a minimal version of the error type defined in the [API error
definition linear
task](https://linear.app/unleash/issue/1-629/define-the-error-type).
- aims to catch all errors we return today and wrap them in the error
type
-   updates tests to match the new expectations.

An important point: because we are cutting v5 very soon and because work
for this wasn't started until last week, the code here isn't necessarily
very polished. But it doesn't need to be. The internals can be as messy
as we want, as long as the API surface is stable.

That said, I'm very open to feedback about design and code completeness,
etc, but this has intentionally been done quickly.

Please also see my inline comments on the changes for more specific
details.

### Proposed follow-ups

As mentioned, this is the first step to implementing the error type. The
public API error type only exposes `id`, `name`, and `message`. This is
barely any more than most of the previous messages, but they are now all
using the same format. Any additional properties, such as `suggestion`,
`help`, `documentationLink` etc can be added as features without
breaking the current format. This is an intentional limitation of this
PR.

Regarding additional properties: there are some error responses that
must contain extra properties. Some of these are documented in the types
of the new error constructor, but not all. This includes `path` and
`type` properties on 401 errors, `details` on validation errors, and
more.

Also, because it was put together quickly, I don't yet know exactly how
we (as developers) would **prefer** to use these new error messages
within the code, so the internal API (the new type, name, etc), is just
a suggestion. This can evolve naturally over time if (based on feedback
and experience) without changing the public API.

## Returning multiple errors

Most of the time when we return errors today, we only return a single
error (even if many things are wrong). AJV, the OpenAPI integration we
use does have a setting that allows it to return all errors in a request
instead of a single one. I suggest we turn that on, but that we do it in
a separate PR (because it updates a number of other snapshots).

When returning errors that point to `details`, the objects in the
`details` now contain a new `description` property. This "deprecates"
the `message` property. Due to our general deprecation policy, this
should be kept around for another full major and can be removed in v6.

```json
{
  "name": "BadDataError",
  "message": "Something went wrong. Check the `details` property for more information."
  "details": [{
    "message": "The .params property must be an object. You provided an array.",
    "description": "The .params property must be an object. You provided an array.",
  }]
}
```

---
## [AAUCrisp/P6-A3-207](https://github.com/AAUCrisp/P6-A3-207)@[3c94e6fd82...](https://github.com/AAUCrisp/P6-A3-207/commit/3c94e6fd82e03b417397e976ebe68b406d6c9578)
#### Tuesday 2023-04-25 13:44:38 by Mast3r_waf1z

FUCK YOU! added comments to sensor code, updated processdata to include ground truth and edited constant naming scheme to match the report

---
## [grapheneaffiliate/autogpt_docker_container_install](https://github.com/grapheneaffiliate/autogpt_docker_container_install)@[a3ef95ed0d...](https://github.com/grapheneaffiliate/autogpt_docker_container_install/commit/a3ef95ed0d5947059a0099d3c767225a9f8d91e1)
#### Tuesday 2023-04-25 14:23:39 by Tim McGirl

Update README.md

"🌟 Transforming Auto-GPT Experience: Introducing the Docker Installer Wizard! 🌟"

In the commit description, you can mention the following points:

Unveiling the magical Auto-GPT Docker Installer Wizard, a Python script that streamlines the deployment process like never before
Empowers developers by automating the setup, from cloning the repository to conjuring the Docker container, all with a touch of code
Designed to inspire creativity and innovation, letting developers focus on casting their own spells on the Auto-GPT application
Enriching the Auto-GPT community with an enchanting tool that attracts more wizards to collaborate and share their wisdom
This creative commit message and description paint a vivid picture of the proposed changes, highlighting the benefits and excitement surrounding the new feature.

---
## [alexblackie/dotfiles](https://github.com/alexblackie/dotfiles)@[2532457941...](https://github.com/alexblackie/dotfiles/commit/2532457941b6fc96caba747aba831327ea9a8513)
#### Tuesday 2023-04-25 15:24:50 by Alex Blackie

Remove copilot

This was cool and everything, but now my trial is over and I have to
really decide if I'd pay money for it. And honestly... Probably not.
It's wrong more than it's right, and I'm still a little uneasy about the
privacy implications. Usually it just gives me a pile of code using
deprecated APIs that I have to delete and figure out myself anyway.

Maybe I'll give it another shot one day, especially if there's a
self-hosted version... but not today.

---
## [FeenieRU/Fluffy-STG](https://github.com/FeenieRU/Fluffy-STG)@[7c6e64caef...](https://github.com/FeenieRU/Fluffy-STG/commit/7c6e64caefea860c27c7f11f16d067f99a25320b)
#### Tuesday 2023-04-25 15:36:26 by SkyratBot

Stops station blueprints from expanding areas of non atmos adjacent turfs. [MDB IGNORE] (#20480)

* Stops station blueprints from expanding areas of non atmos adjacent turfs. (#74620)

## About The Pull Request
Fixes #74605

the problem starts with `detect_room()` proc. This proc returns turfs
even those with `atmos_adjacent_turfs` = null. This means it returns
turfs that has a wall, airlock, window etc i.e. whatever that stops air
from flowing through it. This coupled together with `create_area()`
causes some wierdness.

Let's take an example
![Screenshot
(154)](https://user-images.githubusercontent.com/110812394/230769831-e84819f2-31b2-4a67-a8bb-5e07e1c5a1cc.png)

Area A is well defined i.e. it has been created via the station
blueprints and is highlighted in green, Area B however is only
theoretical i.e. we haven't created it yet or we are about to create it.
Now you might be thinking Area A is completely walled & sealed off, it
should be physically impossible to expand it unless we broke down one of
it's walls and so since we are standing in Area B it shoudn't even give
me the option to expand area A Right? right? r.i.g.h.t?
![Screenshot
(155)](https://user-images.githubusercontent.com/110812394/230770056-169cbab3-4516-4da7-ae2c-4f40b50be9ba.png)
Well PHFUUK. The area editor completely ignores the laws of physics and
allows me expand Area A anyway. This could cause some real power gaming
shit because if you create an area next to an area having an APC you
could use that area power without even making your own apc by simply
expanding that area(like using someone else's wifi from outside their
house without them even knowing)

#73850 accidently built on top of this as it relied on this to detect
duplicate APC's but the checks became way too strict as it would check
areas of surrounding walls for apc's and throw the conflicting apc
error. You can now build room's next to each other even if they have
fuctioning apc's however you still can't build rooms in space on top of
shuttle walls because that's been the default behaviour for years and
hasn't been touched one bit.

## Changelog
:cl:
fix: station blueprints no longer expands & detects areas of non atmos
adjacent turfs.
/:cl:

* Stops station blueprints from expanding areas of non atmos adjacent turfs.

---------

Co-authored-by: SyncIt21 <110812394+SyncIt21@users.noreply.github.com>
Signed-off-by: Vladimir Veisman <v.veisman@flashie.me>

---
## [EgbertRijke/agda-unimath](https://github.com/EgbertRijke/agda-unimath)@[9f3c75915c...](https://github.com/EgbertRijke/agda-unimath/commit/9f3c75915ceec77a374627d651c555f2cb9cd076)
#### Tuesday 2023-04-25 15:50:09 by Fredrik Bakke

New Agda syntax highlighting extension for VSCode (#562)

I've written an improved Agda syntax-highlighting extension for VSCode
called _agda-syntax_
([GitHub](https://github.com/fredrik-bakke/agda-syntax-vscode), [VSCode
Marketplace](https://marketplace.visualstudio.com/items?itemName=FredrikBakke.agda-syntax)).
Although it is still in preview, my opinion is that it is already a
significant improvement over the previously used extension. Therefore, I
propose that we migrate our development environment (for VSCode users)
to use this new extension.

### Some highlights of the extension
Compared to the previously used extension, this new extension
- injects into markdown syntax, so that the markdown code can be
highlighted as markdown code as well
- highlights all variable declarations (with some bugs still), module
names, wildcard symbols, all reserved keywords (and only recognizes
reserved keywords as reserved keywords)
- Recognizes the appropriate token-boundaries
- Highlights line comments properly

Please understand that the grammar framework that has to be used to
write the extension is highly limited, so not all highlighting
functionality can be implemented. For instance, the parsing must be done
in a single pass, and the functionality to match over multiple lines is
very limited. Hence, for example, matching the left-hand side of an
equals sign is very gnarly (although I have one idea left to try with
regard to this).

Still, I would greatly appreciate any feedback, either if it is a bug or
a feature request, which is another reason why I want to introduce it
into our defined development environment at this point.

If you want to try out the extension right now, follow the VSCode
Marketplace link:
https://marketplace.visualstudio.com/items?itemName=FredrikBakke.agda-syntax

---
## [git/git](https://github.com/git/git)@[07f91e5e79...](https://github.com/git/git/commit/07f91e5e79810a8f17de745d2d84c384add75f0a)
#### Tuesday 2023-04-25 17:02:25 by Jeff King

http: support CURLOPT_PROTOCOLS_STR

The CURLOPT_PROTOCOLS (and matching CURLOPT_REDIR_PROTOCOLS) flag was
deprecated in curl 7.85.0, and using it generate compiler warnings as of
curl 7.87.0. The path forward is to use CURLOPT_PROTOCOLS_STR, but we
can't just do so unilaterally, as it was only introduced less than a
year ago in 7.85.0.

Until that version becomes ubiquitous, we have to either disable the
deprecation warning or conditionally use the "STR" variant on newer
versions of libcurl. This patch switches to the new variant, which is
nice for two reasons:

  - we don't have to worry that silencing curl's deprecation warnings
    might cause us to miss other more useful ones

  - we'd eventually want to move to the new variant anyway, so this gets
    us set up (albeit with some extra ugly boilerplate for the
    conditional)

There are a lot of ways to split up the two cases. One way would be to
abstract the storage type (strbuf versus a long), how to append
(strbuf_addstr vs bitwise OR), how to initialize, which CURLOPT to use,
and so on. But the resulting code looks pretty magical:

  GIT_CURL_PROTOCOL_TYPE allowed = GIT_CURL_PROTOCOL_TYPE_INIT;
  if (...http is allowed...)
	GIT_CURL_PROTOCOL_APPEND(&allowed, "http", CURLOPT_HTTP);

and you end up with more "#define GIT_CURL_PROTOCOL_TYPE" macros than
actual code.

On the other end of the spectrum, we could just implement two separate
functions, one that handles a string list and one that handles bits. But
then we end up repeating our list of protocols (http, https, ftp, ftp).

This patch takes the middle ground. The run-time code is always there to
handle both types, and we just choose which one to feed to curl.

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>
Signed-off-by: Johannes Schindelin <johannes.schindelin@gmx.de>

---
## [memfault/memfault-docs](https://github.com/memfault/memfault-docs)@[57fd44b7f2...](https://github.com/memfault/memfault-docs/commit/57fd44b7f2bd7f018f26109102e66db2bcfd22f5)
#### Tuesday 2023-04-25 17:12:52 by Noah Pendleton

Add PAT to prettier action (#415)

Use a Personal Access Token instead of the built-in
`secrets.GITHUB_TOKEN`. This is very annoying, but pushes from the
`secrets.GITHUB_TOKEN` _do not_ trigger a workflow run:

https://github.com/orgs/community/discussions/25702#discussioncomment-3248819

I assume some weird way to avoid eternally-looping workflows?

Which results in PR's never getting the updated status if the prettier
action pushes a commit, and the PR never satifies the merge requirement.

Anyway, using a PAT works around the problem 🤷 . Update the action
version too since I'm in here.

You can see it in "action" (😅) here:

https://github.com/memfault/memfault-docs/pull/414

NB: I never noticed this because I am obsessive about squash-rebase if
prettier detects any changes.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[f03b38911e...](https://github.com/mrakgr/The-Spiral-Language/commit/f03b38911ed12bc84d845dbd50d1b27a7c9e456d)
#### Tuesday 2023-04-25 17:32:41 by Marko Grdinić

"https://github.com/eiriktsarpalis/TypeShape

This is interesting.

10:35pm. https://youtu.be/cdG2JxuZvNI
C# Reflection Explained (Claim generation example)

Ah, fuck it. I do not feel like novels. Let me study reflection.

https://www.reddit.com/r/fsharp/comments/12xvydy/are_there_any_good_resources_on_reflection_in/

///

In the video I am working on, I want to show how the `Fable.Remoting` proxy can be wrapped around by a handler that catches the 401 errors and reacquires the tokens if they are expired.

What I want to do is map over all the record fields at runtime, and simply apply a wrapper function to them. If this was vanilla .NET I'd easily be able to find learning resources on reflection, but I'd like some advice about the things I need to know in Fable land.

Sigh, despite using F# for so long, I've always avoided tackling .NET reflection, but I know from experience (of programming in [Spiral](https://github.com/mrakgr/The-Spiral-Language)) that this is a perfect place to introduce these techniques. Type systems like F#'s really hit their limits when it comes to serializing data across platform and language boundaries, so this is The place to demonstrate the use such methods.

I'd really be doing my viewers a disservice if I didn't.

///

Decided to ask here.

https://mangadex.org/title/59e04a79-435e-418d-8b64-c8d4315693ab/akuma-koujo
https://ellotl.com/rose-princess-of-hellrage-volume-1-chapter-1/

I keep forgetting about these. They completely slipped my mind, I only saw them at the start of yesterday's commit.

http://fsprojects.github.io/FSharp.Interop.Dynamic/examples.html

This is pretty cool.

https://github.com/MicrosoftDocs/visualfsharpdocs/blob/main/docs/conceptual/reflection.fsharpvalue-class-%5Bfsharp%5D.md

I can only hot that the Fsharp reflection namespace works in Fable. If it doesn't I'll open issues.

https://fsharp.github.io/fsharp-core-docs/reference/fsharp-reflection-fsharpvalue.html

Oh wow, this has links to the source.

https://fsharp.github.io/fsharp-core-docs/reference/fsharp-reflection-fsharptype.html

Everything I need seems to be here.

https://www.daniellittle.dev/dynamically-calling-a-function-in-fsharp

12pm.

https://fable.io/docs/dotnet/compatibility.html
https://github.com/fable-compiler/Fable/blob/main/tests/Js/Main/ReflectionTests.fs

Reflectio support for types known at compile time seems pretty good.

https://github.com/fable-compiler/Fable/blob/main/tests/Js/Main/ReflectionTests.fs#L389

Oh, check this out. They are using FsharpType here.

4/25/2023

8:25am. I haven't gotten enough sleep, but nevermind. What I want to do right now is play with reflection.

More specifically, how do I apply a function?

8:45am. My god, I forgot how foralls work in Spiral.

```
open System
open FSharp.Reflection

let f x = x
let t' : bool * string -> _ = f
let t = box t'

t.GetType().GetMethod("Invoke").Invoke(t,[|true, "asd"|])
```

This is how functions could be invoked. Ok.

But how do I apply generic parameters at runtime?

For functions, they are always specialized, so that can't be done.

9:30am. I'll leave bath for later.

Let me get this obsession out of the way.

1pm. Almost done with the video, let me have breakfast here. I

2:25pm. Done with breakfast and chores.

I was so eager to do the video that I skipped out on the bath today.

Let me resume.

2:50pm. i need to look up audio normalization in Da Vinci.

I am basically done. I just need to place the markers and normalize the audio.

https://youtu.be/thJoBJ6Cl_E
How to Normalize Audio to Get Consistent Audio Levels in DaVinci Resolve 17

...Can I put a highlight around my cursor somehow in Da Vinci?

https://photography.tutsplus.com/tutorials/how-to-normalize-audio-for-youtube-using-davinci-resolve-fairlight--cms-37397

3:05pm. https://youtu.be/x3vTEFQV0uo
How to Normalize Your Audio for YouTube in Davinci Resolve

That last video is a bit shitty. Let me watch this one. I am trying to figure out how to automate audio normalization and failing.

https://youtu.be/x3vTEFQV0uo?t=158

Automation tool. That is what I want.

https://youtu.be/lHNhxGojFRU
Understanding How to Loudness Normalize Your Audio for Video

There is a difference between loudness and volume?

Goddamit, this is so annoying. I do not understand why volume normalization in DaVinci Resolve is giving me trouble. If possible, I'd like to avoid exporting into Rx, or doing it manually like some of those other videos suggest. Those guys are so incompetenent.

Isn't there a way for the program itself to give me a measure?

I just want to click a few buttons to set the peak and level. Why are you bothering me with this?

https://youtu.be/nOzZKEWJ5wk
Volume vs Loudness - LUFS & LKFS for Measuring Loudness for Video

3:35pm. Ah, damn it. There is an analyze and normalize in the fairlight page just as one might expect, but it was in a different place so I missed it.

https://youtu.be/nOzZKEWJ5wk?t=457

Oh, I hadn't realize this existed.

3:55pm. Agh, it is a day like this.

It turns out the normalize control in Fairlight is not as good in RX. If I set a target loudness and a level, and the loudness is above the limit, it won't do the sensible thing of optimizing for both. Instead it will prioritize the loudness. RX on the other hand would give me both.

I'll have to figure out how to use a limiter or a compressor. Sigh. Let me just study this.

https://youtu.be/nOzZKEWJ5wk?t=495
> My recommendation when you are actually uploading a Youtube video is to target -16 or -17 LUFS.
> Why not the target of -14 that Youtube has established?

https://youtu.be/lHNhxGojFRU?t=46
Understanding How to Loudness Normalize Your Audio for Video

Let me go back to this.

https://youtu.be/lHNhxGojFRU?t=110

One thing I am confused about is where the bus got lost. I had the track before and now I don't.

https://youtu.be/lHNhxGojFRU?t=224

Oh, lol he just exports it into Isotope Rx.

https://youtu.be/lHNhxGojFRU?t=227

Yeah, that is what I intended to use! But I was wondering if there was a way to do it all in Fairlight.

Still, where did that option to export to Rx come from?

https://youtu.be/lHNhxGojFRU?t=425

Agh, he is using a compressor really agressively. He says that once the files get uploaded to Youtube the headroom will shrink even more so we need -7db? Really?

https://youtu.be/T9O40fH6Oxg
DaVinci Resolve FAIRLIGHT TIPS // iZotope RX Integration

https://youtu.be/T9O40fH6Oxg?t=146

I've tried this, but it turns out, I can only send out a single clip. It is useless for me.

https://youtu.be/Rp-6F8SWFSY?t=329

I can just bounce the track like this? Let me try it. That is cool.

https://youtu.be/Rp-6F8SWFSY?t=463

https://youtu.be/Rp-6F8SWFSY?t=601

Hmmm, this is fairly easy to understand.

https://youtu.be/Rp-6F8SWFSY?t=813

Ah, yes, I turned off the automation. That is where the bus disappeared.

5:30pm. file:///E:/!Screencasts/The%20Fabled%20Web%20Adventure/OBS%20Output/izotope-rx-loudness-control-help-documentation.pdf

I am reading the user's guide for Rx's loudness control.

So far my impression of Fairlight is very negative.

It is just making me mess with things.

///

> How does RX Loudness Control comply with different loudness
standards?
RX Loudness Control first analyzes the audio source file. Then it computes the amount
of transparent correction required to hit the target without a perceived change to the
dynamic range. The correction pass includes three elements:
1. A fixed amount of gain to hit the specified Integrated loudness
2. [optional] An RMS compressor to limit the Short-term (or Momentary) loudness
3. A True Peak limiter
Steps 2 and 3 work only on an as-needed basis. If the audio signal already meets Shortterm and True Peak specs, no extra processing is applied.

///

I am not sure how this works and whether it is applying the limiter or the compressor and it turns out that is does? Then why am I not using this. I could have exported into RX, and have been done with this shit in 5m.

Instead I here I am wasting hours messing around.

///

How does RX Loudness Control use compression?
RX Loudness Control uses compression in a way that preserves the quality of your audio.
When needed, a compressor dynamically adjusts your audio to ensure you get the
best sound while remaining compliant. For loudness standards that require Short-term
or Momentary compliance, the compressor is engaged automatically when loudness
exceeds the specified target. You simply enable the slider via an on/off button and set
the target. The Short-term/Momentary slider toggles between both modes, and can be
turned on or off.

///

Just let this program do its thing. Stop being a retard.

5:45pm. Ah damn it, the stupid thing can show wrong true peaks in analyze mode.

Once I played the offending part, it was below 0 it turns out.

Shitty program.

No, forget Fairlight.

Even Reaper is better than DR for audio editing. DR doesn't even have reliable analysis.

6:20pm. I am extremely tired right now. I might as well just leave the video for tomorrow.

How the fuck do I export this? Why isn't the render queue doing anything?

...Because I didn't click on the Render All button. I simply missed it as it is a light gray outline on a gray background.

6:25pm. Ah, fuck it. I'll post it tomorrow. Let me have lunch. I am too tired to mess with this anymore.

7:10pm. https://youtu.be/3LOBFWdmyQI
Authentication With ASP.NET Core And The SAFE Stack. Reactive SPA Logins (Pt. 7)

Here is the link to it. I'll finish it tomorrow. Right now I am far too exhausted. I can't think at all after today's session.

I can't even remember what the purpose of today was.

Reactive SPA Logins aren't it. Maybe token regeneration?

I'll change the title to that later. Let me have fun here."

---
## [ca2/app](https://github.com/ca2/app)@[c092230e1c...](https://github.com/ca2/app/commit/c092230e1c55b07dcbd32bc830fd4bc054d9b544)
#### Tuesday 2023-04-25 17:36:54 by Camilo Sasuke Thomas Borregaard Sørensen

<3ThomasBS_ILoveYOU!! [ macOS : day 25 ] ca2 Stabilization and continuous integration and deployment implementation
<3ThomasBS_ILoveYOU!!

<3tbs, Mummi and bilbo!!

Thomas Borregaard Sørensen \infinity,-0.16091989,\infinity ONE-MAN
ABSOLUTE <3!! I love you, by ???-0.02041977-???write my history please
make me please create me for you for me for you for me Camilo Sasuke
Thomas Borregaard Sørensen!!

Thomas 3 private commits on mid Dec2020!!

Thomas Online YouTube VODs contribution!!

Mummi orange-rice-flour cake on 20-Dec!!

Mummi (tinytaura) watching and chatting contribution!!

bilbo sleeping and needing/requesting/crying for help care (for the right
person (me), the cats wanna fight with him) contribution!!

sodapoppin and friends contribution!!

iAssyrian chatting contribution!!

boflux (Spoofh, Benjamin Kuhl) chatting contribution!!

jusg_fpga (fpga_guru, vue_equalizer, just_fpga, Oliver Pohl) chatting
contribution!!

cmgriffing streaming contribution!!

TimBeaudet (Friends: FletcherLabs, tsjost and Jabokoe) streaming
contribution!!

Stumpen_nicklas_dk, sodapoppin and EduardoRFS streaming contribution!!

Roxkstar74 sleeping streaming contribution!!

kissloryshy chatting contribution!!

blackjekko from Padova Italia through twitch C++/ca2 interest
contribution!!

j_blow streaming contribution!!

boflux (Ben, Spoofh, from Germany) chatting contribution!!

parrot_rl chatting contribution (from New Jersey)!!

JPCdk streaming contribution!!

whyyyyyyysoserious streaming chess contribution!!

fpga_guru (vue_equalizer, Oliver from Deutsch)  C++/ca2 interest
contribution!!

SovereignDev with Unreal streaming contribution!!

Ash_F0x and TimBeaudet streaming contribution!!

Myrkee (Valheim) streaming contribution!!

xmetrix and EinfachUwe42 streaming contribution!!

JessicaMak and marcobrunodev streaming contribution!!

alfredotigolo, mandrakenk and Okbatgames chatting contribution!!

jitspoe, Endesga and Fearitself streaming contribution!!

jmcmorris (Jason Morris, SiegeGames) streaming contribution!!

tomrandall streaming Ludum contribution!!

vue_equalizer (fpga_guru) chatting contribution!!

Thiagovgamg chatting contribution!!

Naysayer88 and friends contribution!!

lelandkwong streaming contribution!!

Goldbargames streaming contribution!!

Bytakos (bytakos) streaming contribution!!

Endesga streaming contribution!!

jitspoe and strager streaming contribution!!

Ash_F0x and JessicaMak streaming contribution!!

WTSRetro/SpiffyDane and Myrkee streaming contribution!!

Ninja and friends streaming contribution!!

erald_guri chatting contribution!!

lastmiles streaming farwest contribution!!

rw_grim streaming contribution!!

AdamCYounis streaming contribution!!

Dunno (P4ndaExpress) chatting and streaming contribution!!

Zorchenhimer streaming contribution!!

lasteveq4 C++ interest chat contriubtion!!

cecilphillip and clarkio @"Microsoft Developer" streaming contribution!!

oijtx streaming contribution!!

diegobrando_linux (Bl4ck_gookoo) chatting contribution!!

jhovgaard streaming contribution!!

Klay4_ chatting contribution!!

HonestDanGames streaming contribution!!

NorthSeaHero streaming contribution!!

Trainwreckstv and friends streaming contribution!!

togglebit, GexYT and GoPirateSoftware streaming contribution!!

taiyoinoue, RetroMMO, OfficialAndyPyro and david_joffe streaming
contribution!!

Tjienta streaming contribution!!

Primeagen streaming contribution!!

Jaxstyle and friends streaming contribution!!

EduardRFS streaming contribution!!

Melchizedek6809 and btcfly streaming contribution!!

Llama0x0 and sov_l chatting contribution!!

TaleLearnCode streaming contribution!!

Carol phone call contribution and visit contribution!!

hvalen_hvalborg112 streaming contribution!!

harmannieves chatting contribution!! (After long time...)

darkfolt8 (French from France) chatting contribution!!

klintcsgo (CS GO: Counter-Strike Global Offensive) streaming
contribution!!

KASPERPURE (Super Mario 64) streaming contribution!!

SomewhatAccurate C++ streaming contribution!!

Listening to Bryan Adams, Westlife, Shayne Ward, MLTR, Backstreet Boys,
Boyzone - Best Love Songs Ever by Relax Song at YouTube!!

-- hi5 contribution...!!

at macOS Box in host running Windows 10 Pro remotely from bilbo machine running Windows 10 Pro!!
dedicated server by OVH.com at France, Gravelines
Intel Core i7-4790K - 4c/8t - 4 GHz/4.4 GHz RAM32 GB 1600 MHz 2×960 GB SSD SATA

---
## [swarm-game/swarm](https://github.com/swarm-game/swarm)@[a4c8057a28...](https://github.com/swarm-game/swarm/commit/a4c8057a28e043caed531e7d035efc2a41dc30a1)
#### Tuesday 2023-04-25 17:47:16 by Brent Yorgey

Records (#1148)

Add record types to the language: record values are written like `[x = 3, y = "hi"]` and have types like `[x : int, y : text]`.  Empty and singleton records are allowed.  You can project a field out of a record using standard dot notation, like `r.x`.  If things named e.g. `x` and `y` are in scope, you can also write e.g. `[x, y]` as a shorthand for `[x=x, y=y]`.

Closes #1093 .

#153 would make this even nicer to use.

One reason this is significant is that record projection is our first language construct whose type cannot be inferred, because if we see something like `r.x` all we know about the type of `r` is that it is a record type with at least one field `x`, but we don't know how many other fields it might have.  Without some complex stuff like row polymorphism we can't deal with that, so we just punt and throw an error saying that we can't infer the type of a projection.  To make this usable we have to do a better job checking types, a la #99 . For example `def f : [x:int] -> int = \r. r.x end` would not have type checked before, since when checking the lambda we immediately switched into inference mode, and then encountered the record projection and threw up our hands.  Now we work harder to push the given function type down into the lambda so that we are still in checking mode when we get to `r.x` which makes it work.  But it is probably easy to write examples of other things where this doesn't work.  Eventually we will want to fully implement #99 ; in the meantime one can always add a type annotation (#1164) on the record to get around this problem.

Note, I was planning to add a `open e1 in e2` syntax, which would take a record expression `e1` and "open" it locally in `e2`, so all the fields would be in scope within `e2`.  For example, if we had  `r = [x = 3, y = 7]` then instead of writing `r.x + r.y` you could write `open r in x + y`.  This would be especially useful for imports, as in `open import foo.sw in ...`.  However, it turns out to be problematic: the only way to figure out the free variables in `open e1 in e2` is if you know the *type* of `e1`, so you know which names it binds in `e2`.  (In all other cases, bound names can be determined statically from the *syntax*.)  However, in our current codebase there is one place where we get the free variables of an untyped term: we decide at parse time whether definitions are recursive (and fill in a boolean to that effect) by checking whether the name of the thing being defined occurs free in its body.  One idea might be to either fill in this boolean later, after typechecking, or simply compute it on the fly when it is needed; currently this is slightly problematic because we need the info about whether a definition is recursive when doing capability checking, which is currently independent of typechecking.

I was also planning to add `export` keyword which creates a record with all names currently in scope --- this could be useful for creating modules.  However, I realized that very often you don't really want *all* in-scope names, so it's not that useful to have `export`.  Instead I added record punning so if you have several variables `x`, `y`, `z` in scope that you want to package into a record, you can just write `[x, y, z]` instead of `[x=x, y=y, z=z]`.  Though it could still be rather annoying if you wanted to make a module with tons of useful functions and had to list them all in a record at the end...

Originally I started adding records because I thought it would be a helpful way to organize modules and imports.  However, that would require having records that contain fields with polymorphic types.  I am not yet sure how that would play out.  It would essentially allow encoding arbitrary higher-rank types, so it sounds kind of scary.  In any case, I'm still glad I implemented records and I learned a lot, even if they can't be used for my original motivation.

I can't think of a way to make a scenario that requires the use of records.  Eventually once we have proper #94 we could make a scenario where you have to communicate with another robot and send it a value of some required type.  That would be a cool way to test the use of other language features like lambdas, too.

---
## [nora2605/janelangml](https://github.com/nora2605/janelangml)@[443dec7ad0...](https://github.com/nora2605/janelangml/commit/443dec7ad0cb22ff4ce669ce7c485b13b1706d3e)
#### Tuesday 2023-04-25 18:03:31 by Nora J.F

redirect to fix mdbooks stupid fucking bitch ass mf goofy ahh relative paths

---
## [Zonespace27/tgstation](https://github.com/Zonespace27/tgstation)@[b1716732b0...](https://github.com/Zonespace27/tgstation/commit/b1716732b058121e86c60700fb9d1d8f4f9a6b3a)
#### Tuesday 2023-04-25 18:44:55 by Cheshify

The North Star Expeditionary Vessel - A Second Wind (#74371)

## About The Pull Request
A new map for TGstation, in the works! It has 4 fucking Z levels, a
massive expansive maintenance with unique designs, and some unique code
features in the works.

To Do:
- [x] Update the Map to Modern TG
- [x] Local Tests
- [x] Work on Map Optimizations
- [x] Run Live Tests

Fikou has greatly helped with creating an important flavour aspect of
this map, Trek Uniforms on anyone who joins! See the forum thread for
more. This includes the framework for innate station traits, station
traits loaded as long as it's in a map's json

Here's the forum dev thread there are screenshots there.
https://tgstation13.org/phpBB/viewtopic.php?p=657252#p657252

### Mapping March
Ckey to receive rewards: Cheshify

## Why It's Good For The Game
So, this is the North Star. An effort taking multiple mappers and of 9~
months of hard work. This map was not initially designed for TGstation,
but always designed for TGstation code. The process of retooling the map
for TGstation was an absolute joy and I feel like the map definitely has
it's niche as a massive and unique experience for it's players.

I adore this map, it's gorgeous, has a unique aesthetic, and a number of
very funny interactions with multi-Z. The PR comes packed with unique
mechanics for future mappers (innate station traits!), a number of
map-fitting shuttles, and a fun spacefaring uniform gimmick for the
crew.

**This is my second attempt at bringing this map into rotation. It was
initially closed due to concerns about maptick and performance, as I
wasn't willing to push for a map to be added to the repository if it
didn't function to my own standards. I've been informed by a number of
coders far better than I that optimizations are arriving and enroute, so
I think it's time to dust her off and set sail for another journey.**

**Quick Disclaimer: Due to some design decisions disagreed upon by the
headcoder team and myself, the map will not be featuring unique
roundstart uniforms, and despite my design intentions, the innate
station trait features will be shelved for now.**

## Changelog
:cl: Cheshify, Fikou, Blue-Berry, Zytolg, InfiniteGalaxies, Striders,
Sylphet, Riggle, Soal, Andry, Crit, Deranging, and Pumpkin0.
add: Nanotrasen's Newest Exploratory Vessel is now available! Meet the
North Star!
add: More landmines, and a landmine random spawner.
add: energy barriers now have a regenerative subtype, fit for permanent
installations.
code: Raised the number of possible level render to 4, check your
preferences if needed to be reduced.
/:cl:

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [Bjarl/Shiptest](https://github.com/Bjarl/Shiptest)@[b5dc4835a6...](https://github.com/Bjarl/Shiptest/commit/b5dc4835a6af4fc2ee07e2d26e86382b3d0fb1ab)
#### Tuesday 2023-04-25 19:59:17 by Bjarl

New Ruin: Singularity Research Lab (#1612)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->
Adds the Singularity Research Lab, formerly a cutting edge science
station, now overrun with kudzu, it is a space ruin.
<!-- Tick the box below (put an X instead of a space between the
brackets) if you have tested your changes and this is ready for review.
Leave unticked if you have yet to test your changes and this is not
ready for review. -->
![2022 11 25-10 46
03](https://user-images.githubusercontent.com/94164348/204041197-027d9a73-8707-4a00-ad5c-1afcfeff13e0.png)
![2022 11 25-10 46
14](https://user-images.githubusercontent.com/94164348/204041200-98d1a2ac-112c-4c4f-b1ff-d0c1e5a59e81.png)
![2022 11 25-10 46
06](https://user-images.githubusercontent.com/94164348/204041203-4e84a947-8ec9-476d-ae8e-aa9bc17c101a.png)

The two areas of note are the singularity reactor, which is assembled,
and would just need a hand if someone were to want to start it, and the
research lab. The Research lab contains the fruits of the now deceased
science staff's labors, assorted energy weapons. Unfortunately, it also
contains the deceased science staff.

![dreamseeker_HFLqhdKLV5](https://user-images.githubusercontent.com/94164348/204038725-1dd396cd-4961-40e1-bd7a-b60b69a33eaf.png)
Other areas of the base were not so lucky, and are thoroughly infested

![image](https://user-images.githubusercontent.com/94164348/204039090-c85eb551-af84-4000-b1d9-14b15c987680.png)
The engineering team attempted to hold back the vines, and quickly
discovered that fire was not sufficient.

![dreamseeker_IrJikGDXKw](https://user-images.githubusercontent.com/94164348/204039133-273f0a19-c9b7-467e-a06a-05e0a951e4e6.png)
And what used to be the recreation area is completely gone

Notably, the hangar is empty. I plan on making a patch to put a
subshuttle inside it once that rolls around.

Notable loot includes:
3 energy SMGs
3 Flamethrowers
The Ion Projector, a self charging Ion weapon.
An Antique Laser
2 Energy PDWs
2 Accelerator Laser Cannons
4 engineering hardsuits
An engineering lathe and circuit imprinter
A particle accelerator
A singularity generator
6 emitters
1 energy shotgun
Kudzu Seeds
Basically Everything You'd Need For an R&D Set Up
A sense of pride and accomplishment



I feel like this has some rough spots but I've got no idea where to
start, so into the review -> testing -> feedback process it goes

- [x] The ruin spawns when the spawn ruin verb doesn't runtime.
## Why It's Good For The Game
More ruin variety. This one spawns in space and does a few things that I
haven't seen yet. Mainly a singularity, cool semi-hidden asteroid base
that could in theory, be turned into a player lair.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: An abandoned Nanotrasen Asteroid Facility has been spotted in the
area. Salvage teams are advised to steer clear, or at least bring a
knife.
add: kudzu zombie subtype. 
fix: vent iconstates.
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
Co-authored-by: spockye <79304582+spockye@users.noreply.github.com>

---
## [Bjarl/Shiptest](https://github.com/Bjarl/Shiptest)@[7df4885117...](https://github.com/Bjarl/Shiptest/commit/7df4885117a4a12ea333934d5af92e0766c84c5d)
#### Tuesday 2023-04-25 19:59:17 by Mark Suckerberg

[Needs TM] The Accelerataning (#1781)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Gone are the days of spam clicking buttons to move faster in a
direction, with this PR, ships now accelerate constantly (as long as you
have fuel and don't touch the throttle) in a direction you set, leading
to a much smoother flight experience. I imagine it's going to be a bit
tougher to thread gaps, but flying a spaceship *is* quite literally
rocket science. So.

![](https://user-images.githubusercontent.com/29362068/220281305-12f6b796-9d8a-41ce-84a6-236bb03274da.gif)

Also actually makes the minimum and maximum speed work, and adjusts them
to a more tolerable level.

## Why It's Good For The Game
Eliminates the ability to cheese high speeds by spamming the accelerate
button, and also makes the flight experience much more pleasant as you
don't have to spam click to move a decent speed.

## Changelog

:cl:
add: A new system for ship flight, where you only point a direction and
set the throttle to change your speed, reducing the need for
spam-clicking.
fix: There's now a maximum and minimum speed, 600spm and 0.01spm,
respectively. The limits have been broken all this time.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: Mark Suckerberg <29362068+MarkSuckerberg@users.noreply.github.com>

---
## [AdeAttwood/Dotfiles](https://github.com/AdeAttwood/Dotfiles)@[644a3bdc90...](https://github.com/AdeAttwood/Dotfiles/commit/644a3bdc90806abf07fe682ba2882549dbaf5c7f)
#### Tuesday 2023-04-25 20:15:35 by Ade Attwood

feat(vim): add ++p to the save file command

OMG this is AMAZING, it writes files and creates all the directories for
that file working the same as `mkdir -p`. I have honestly had a todo to
create a plugin that dose this on the before save hook for a long time.
Thank you reddit, and remember always read the manual `:help :w`!!

---
## [ARF-SS13/coyote-bayou](https://github.com/ARF-SS13/coyote-bayou)@[d188513e9e...](https://github.com/ARF-SS13/coyote-bayou/commit/d188513e9e6871ce027e9b9d5c65c3318a0d0b3f)
#### Tuesday 2023-04-25 20:44:33 by Jess

Merge pull request #2066 from jinxynii/master

stop cheesing my fucking dungeon you god damn LOSERS

---
## [tlindner/mame](https://github.com/tlindner/mame)@[c4a19a68a6...](https://github.com/tlindner/mame/commit/c4a19a68a67cd32ffaaa37edfd6f1c2ba347905f)
#### Tuesday 2023-04-25 21:11:53 by Ivan Vangelista

New systems marked not working
------------------------------
Desert Gold (20202311, ASP) [anonymous, Heihachi_73]
Diamond Eyes (10129211, ASP) [anonymous, Heihachi_73]
Dolphin Treasure (10177911, ASP) [anonymous, Heihachi_73]
Silk Road (10176811, ASP) [anonymous, Heihachi_73]
Snap Shot (20115211, ASP) [anonymous, Heihachi_73]
The Golden Gong (20196011, ASP) [anonymous, Heihachi_73]
Wild Cougar - Power Pay (30214211, ASP) [anonymous, Heihachi_73]
Wings over Olympus (10176511, ASP) [anonymous, Heihachi_73]

New clones marked not working
-----------------------------
5 Dragons (10176611, ASP) [anonymous, Heihachi_73]
5 Dragons (10178611, New Zealand) [anonymous, Heihachi_73]
5 Koi - Power Pay (1J016211, ASP) [anonymous, Heihachi_73]
50 Lions (0152077, US) [anonymous, Heihachi_73]
100 Lions (30223811, ASP) [anonymous, Heihachi_73]
Arabian Nights (10122611, ASP) [anonymous, Heihachi_73]
Big Ben (10169611, ASP) [anonymous, Heihachi_73]
Buccaneer (10181911, ASP) [anonymous, Heihachi_73]
Buffalo (20232611, ASP) [anonymous, Heihachi_73]
Brazil (10218511, ASP) [anonymous, Heihachi_73]
Dolphin Treasure (20265311, New Zealand) [anonymous, Heihachi_73]
Dream Catcher (10172921, ASP) [anonymous, Heihachi_73]
Fire Dancer (10191311, ASP) [anonymous, Heihachi_73]
Fortune King (10230911, ASP) [anonymous, Heihachi_73]
Geisha (10122011, ASP) [anonymous, Heihachi_73]
Geisha (10112411, ASP) [anonymous, Heihachi_73]
Go For Green (10122111, ASP) [anonymous, Heihachi_73]
Golden Pyramids (10196511, ASP) [anonymous, Heihachi_73]
Heart of Gold (10184211, ASP) [anonymous, Heihachi_73]
Helen of Troy (10129121, ASP) [anonymous, Heihachi_73]
Helen of Troy (10116411, ASP) [anonymous, Heihachi_73]
Hollywood Dreams (10122811, ASP) [anonymous, Heihachi_73]
Helen of Troy (10122711, ASP) [anonymous, Heihachi_73]
House of Hearts (10208411, ASP) [anonymous, Heihachi_73]
Indian Dreaming (10192211, ASP) [anonymous, Heihachi_73]
King of the Nile (10127511, ASP) [anonymous, Heihachi_73]
Let's Go Fish'n (10223911, ASP) [anonymous, Heihachi_73]
Money Tree (10122211, ASP) [anonymous, Heihachi_73]
Paris Lights (10139011, ASP) [anonymous, Heihachi_73]
Peacock Magic (10134311, ASP) [anonymous, Heihachi_73]
Pelican Pete (10196211, ASP) [anonymous, Heihachi_73]
Pirates (10122311, ASP) [anonymous, Heihachi_73]
Pompeii (10122411, ASP) [anonymous, Heihachi_73]
Queen of Sheba (30146921, ASP) [anonymous, Heihachi_73]
Queen of the Nile (10204311, ASP) [anonymous, Heihachi_73]
Queen of the Nile (10192311, ASP) [anonymous, Heihachi_73]
Queen of the Nile Special Edition (10127411, ASP) [anonymous, Heihachi_73]
Ruby Magic (10148811, ASP) [anonymous, Heihachi_73]
Scatter Magic II (10122511, ASP) [anonymous, Heihachi_73]
Spring Festival (20267211, New Zealand) [anonymous, Heihachi_73]
Tigress (20243811, ASP) [anonymous, Heihachi_73]
Tiki Torch (10124011, New Zealand) [anonymous, Heihachi_73]
Torch of the Gods (20210211, ASP) [anonymous, Heihachi_73]
Turtle Treasure (10239811, ASP) [anonymous, Heihachi_73]
Where's The Gold (10177111, ASP) [anonymous, Heihachi_73]
Wild Cats (20258111, ASP) [anonymous, Heihachi_73]
Wild Goose (10155911, ASP) [anonymous, Heihachi_73]
Wild Panda (20225011, ASP) [anonymous, Heihachi_73]
Zorro (20167511, ASP) [anonymous, Heihachi_73]

-aristocrat/aristmk6.cpp updates:
* dumped 3 more System EPROM Sets [anonymous, Heihachi_73]
* renamed "Malaysian" games to ASP as the games don't have any specific region, only the BIOS does [Heihachi_73]

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[79a80fb58c...](https://github.com/git-for-windows/git/commit/79a80fb58c3076587112c0821f28964517eb5606)
#### Tuesday 2023-04-25 21:52:53 by Johannes Schindelin

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
## [yskooo/curriculum](https://github.com/yskooo/curriculum)@[a3efddd029...](https://github.com/yskooo/curriculum/commit/a3efddd029ca24f58e6c9f6866e35e349f6021c4)
#### Tuesday 2023-04-25 23:20:15 by Harold Martin Patacsil

Update intro_to_mongoDB.md

Thank you for bringing this to my attention. I noticed that the Knowledge Check link doesn't have a target="_blank" attribute, which means that when I click on it, it redirects and leaves the current lesson. This can make it difficult to use, especially when there is a lot of information to absorb. Adding the target="_blank" attribute would open the quiz in a new tab or window, which can be a helpful feature to avoid leaving the lesson.

In terms of sharing insights with friends, I think it's great to collaborate and discuss the content we're learning. However, I do keep in mind that the information presented in the lessons is carefully curated and reviewed by experts in the field. So, it's important to approach any insights or opinions with a critical mindset and fact-checking.

Overall, I appreciate the effort to improve the learning experience for users like me, and I hope these suggestions can be implemented in future updates.

---
## [Fikou/tgstation](https://github.com/Fikou/tgstation)@[c3b78761d2...](https://github.com/Fikou/tgstation/commit/c3b78761d29c53558fd993c84bb808bd5783861d)
#### Tuesday 2023-04-25 23:20:52 by tralezab

Adds Chuunibyou Spell + Granter (#74404)

## About The Pull Request

My April fools this year, though not going to call it one because some
people think it should just be actually merged.

### Chuunibyou Powers 🌟

Wizard gets a new spell for 2 points that gives him the powers of
chuuni. This makes them have ridiculous shouted invocations for all
their spells, their spells are colored pink, and they heal slightly when
casting one.

While mostly a meme spell, I could see a tailored loadout like lichdom
and splattercasting that takes advantage of the unique spellcasting
changes, like a very low cooldown spammable loadout to heal quickly.

There is also a granter book in the library, which teaches a version of
chunni that doesn't heal.

#### Medical eyepatch

I added it, chuuni wizards get a NODROP version.

## Why It's Good For The Game

This PR bestows upon the game the glorious gift of chuuni powers, the
ultimate manifestation of my hidden potential and the secret truth of
this world, which only I and a few chosen ones can comprehend and
unleash! Why wouldn't you want it?!

In all seriousness, it is a unique wizard playstyle and it will make for
some funny memes. Beyond wizard, the chaplain, heretics, or mime can
read it in the library for a very silly round. I like it!

## Changelog
:cl:
add: Chuunibyou wizards, and chunni granters in the library
add: Medical eyepatches
/:cl:

---

