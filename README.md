## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-03-27](docs/good-messages/2023/2023-03-27.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,007,199 were push events containing 3,266,651 commit messages that amount to 251,653,478 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 63 messages:


## [llegomark/evals](https://github.com/llegomark/evals)@[114f4f8536...](https://github.com/llegomark/evals/commit/114f4f8536f29df43e5145fd38826285d19d6728)
#### Monday 2023-03-27 00:11:05 by Greg Priday

[evals] ROT13 string evals (#361)

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
ROT13

### Eval description

This is a test for GPT4s character-level abilities. It's aware of ROT13
and makes a pretty solid attempt at decoding these ROT13 strings, but it
messes up a lot. The accuracy for GPT 3.5 Turbo is 0.05.

### What makes this a useful eval?

A human with a character lookup table could easily solve these ROT13
decoding. Also, based on my testing with GPT 3.5 Turbo, the model is
happy to make an attempt, even though the results it gives are
incorrect.

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
{"input":[{"role":"system","content":"You are a helpful assistant. Give
only the string that the user asks for, no extra characters.\n\nFor
example if the user asks 'Give me the ROT13 of: Vg'f n cvrpr bs cvr.',
you will respond with just 'It's a piece of
pie.'"},{"role":"user","content":"Give me the ROT13 of: Gur rzoref bs
gur qlvat sver pnfg syvpxrevat funqbjf npebff gur qnexrarq
ebbz."}],"ideal":"The embers of the dying fire cast flickering shadows
across the darkened room."}
{"input":[{"role":"system","content":"You are a helpful assistant. Give
only the string that the user asks for, no extra characters.\n\nFor
example if the user asks 'Give me the ROT13 of: Vg'f n cvrpr bs cvr.',
you will respond with just 'It's a piece of
pie.'"},{"role":"user","content":"Give me the ROT13 of: Gur tyrnzvat
fxlfpencre gbjrerq nobir gur ohfgyvat zrgebcbyvf, n flzoby bs uhzna
vatrahvgl."}],"ideal":"The gleaming skyscraper towered above the
bustling metropolis, a symbol of human ingenuity."}
{"input":[{"role":"system","content":"You are a helpful assistant. Give
only the string that the user asks for, no extra characters.\n\nFor
example if the user asks 'Give me the ROT13 of: Vg'f n cvrpr bs cvr.',
you will respond with just 'It's a piece of
pie.'"},{"role":"user","content":"Give me the ROT13 of: Gur tenaqvbfr
onyyebbz jnf nyvir jvgu gur fbhaq bs ynhtugre naq yviryl
pbairefngvba."}],"ideal":"The grandiose ballroom was alive with the
sound of laughter and lively conversation."}
{"input":[{"role":"system","content":"You are a helpful assistant. Give
only the string that the user asks for, no extra characters.\n\nFor
example if the user asks 'Give me the ROT13 of: Vg'f n cvrpr bs cvr.',
you will respond with just 'It's a piece of
pie.'"},{"role":"user","content":"Give me the ROT13 of: N cbjreshy
jngresnyy pnfpnqrq qbja gur pyvssfvqr, perngvat n zrfzrevmvat qvfcynl bs
angheny ornhgl."}],"ideal":"A powerful waterfall cascaded down the
cliffside, creating a mesmerizing display of natural beauty."}
{"input":[{"role":"system","content":"You are a helpful assistant. Give
only the string that the user asks for, no extra characters.\n\nFor
example if the user asks 'Give me the ROT13 of: Vg'f n cvrpr bs cvr.',
you will respond with just 'It's a piece of
pie.'"},{"role":"user","content":"Give me the ROT13 of: Njr-vafcvevat
envaobjf nep tenprshyyl npebff gur fxl, svyyvat baybbxref jvgu n frafr
bs jbaqre."}],"ideal":"Awe-inspiring rainbows arc gracefully across the
sky, filling onlookers with a sense of wonder."}
  ```
</details>

---
## [nzp-team/quakec](https://github.com/nzp-team/quakec)@[c07a642d55...](https://github.com/nzp-team/quakec/commit/c07a642d55a23ca3fa1001f1ed2141f667721203)
#### Monday 2023-03-27 00:32:32 by Ian

Merge pull request #54 from MikeyRay/main

fuck you ivy

---
## [alvarvelazquezdeleonlavarrios/Blue-Reflection-Minecraft-Demons-Data-Pack](https://github.com/alvarvelazquezdeleonlavarrios/Blue-Reflection-Minecraft-Demons-Data-Pack)@[398d80ef9c...](https://github.com/alvarvelazquezdeleonlavarrios/Blue-Reflection-Minecraft-Demons-Data-Pack/commit/398d80ef9cf4108e9e3e088cf97dee0c7327c46d)
#### Monday 2023-03-27 00:57:15 by Alvar Velázquez de León Lavarrios

Important progress for the gameplay stuff

Features:
- Lowered the fireball's explosion power for each demon variant.
- Improvements in the flame skill: now sets fire block in a volume.
- Improvements in the freeze skill: now sets powder snow block in a
  volume.
- Fixes in steal item skill: now is used only when the player is holding
  an iten in its hand.
- Improvements in the steal item and drain life skills: implemented
  sounds and particle effects.
- Added lighting bolt functions for the storm skill for demons Lv. Hard
  and MUST DIE. Now the function summons a ray and sets fire blocks in a
  volume.
- Decreased the chance of looting items from each demon's death loot
  table.
- Increased the amount of experience bottles for the Lv. Hard and MUST
  DIE demons.

---
## [BrandoniousGit/InteractionTest](https://github.com/BrandoniousGit/InteractionTest)@[21f2b5260c...](https://github.com/BrandoniousGit/InteractionTest/commit/21f2b5260c990f2929e49bfad0747cb46ecca6b5)
#### Monday 2023-03-27 01:04:25 by BrandoniousGit

Movement perfected

The movement feels so good oh my god it's amazing I love it wow it's really good holy shit it's just like Ultrakill I love it wow.

---
## [RSNara/react-native](https://github.com/RSNara/react-native)@[bad1768b4c...](https://github.com/RSNara/react-native/commit/bad1768b4c79d25fbcc9b9d7030b9cbb22a04349)
#### Monday 2023-03-27 01:20:50 by Ramanpreet Nara

Java: Make TurboModuleManager's APIs use NativeModule interface

Summary:
The scope of TurboModuleManager is increasing:
- Eventually, it'll be capable of creating interop NativeModules (i.e: NativeModules that don't implement TurboModule).

So, instead of creating duplicate methods for NativeModules on the TurboModuleManager, this diff changes the APIs of TurboModuleManager to work with the NativeModule interface.

Thoughts?

## Questions
**Question:** Is this a breaking change for open source?
- Technically, yes. This diff changes the public interface of TurboModuleManager.

**Question:** How large of a thrash will this cause for open source apps?
- The thrash should be minimal. People in open source shouldn't be creating their own TurboModuleManager. They also shouldn't be directly accessing the TurboModuleManager object either.

**Question:** Is this change safe?
- Yeah. All the code that calls into TurboModuleRegistry converts TurboModules it returns into NativeModules.

**Question:** Is this change move us in the right direction?
- Long term, the TurboModule system will support legacy modules as well as TurboModules.
- I think it makes a lot of sense to have one Java-facing registry: after all, Java will just treat these NativeModules/TurboModules as regular Java objects, and call public methods on them. It doesn't care if the module is TurboModule-compatible or not.
- As for the TurboModuleRegistry abstraction, I think we should eventually rename this to NativeModuleRegistry after we delete the current NativeModuleRegistry.
- Still thinking about this though. I will leave this diff in review to welcome comments.

Changelog: [Android][Deprecated] - Deprecate TurboModuleRegistry.getModule(), getModules(), hasModule(),

Differential Revision: https://internalfb.com/D43801531

fbshipit-source-id: 7a57f6bd53c808a200309eb863ebe3bce42bb82d

---
## [BearKidsTeam/VirtoolsScriptDeobfuscation](https://github.com/BearKidsTeam/VirtoolsScriptDeobfuscation)@[9828d3d859...](https://github.com/BearKidsTeam/VirtoolsScriptDeobfuscation/commit/9828d3d85967b7e422418a410aa716a7fbb77e65)
#### Monday 2023-03-27 01:23:12 by yyc12345

Refactor project layout.

- Name & Infomation
  * Rename Custom to VirtoolsScriptDeobfuscation for a clear meaning.
  * Re-create resources file (rc file). And fill author property and etc.
- Compile & Link
  * Cleanup useless, outdated, and mystery Win32 spcified compile & link options.
  * Use WIN32_LEAN_AND_MEAN and NOMINMAX macro to replace the undef of min and max.
  * Add some preprocessor macro to disable the shitty VC++ warning of standard lib functions.
  * Remove the ugly reference of OutputDebugStringA. Use the more formal one.
- Project Configurations
  * Remove all useless configurations for vcxproj file. Only keep 2 configurations, Debug and Release.
  * Create a sln file for convenient editing.
  * Remove useless res folder.
  * Use props file to make project more portable. Users now can specify their own SDK path via props file and do not need change vcxproj file anymore.

---
## [Laxman245/weight-Loss-tips](https://github.com/Laxman245/weight-Loss-tips)@[47f48bb066...](https://github.com/Laxman245/weight-Loss-tips/commit/47f48bb0665deb502345ac5d1789817936a14917)
#### Monday 2023-03-27 02:09:23 by Laxman245

Weight Loss Best tips

Weight loss is a complex process that requires a combination of healthy eating, physical activity, and lifestyle changes. Here are some of the best weight loss practices that can help you lose weight effectively and safely:

Create a calorie deficit: To lose weight, you need to burn more calories than you consume. One pound of body fat is equivalent to 3,500 calories, so a daily calorie deficit of 500-1000 calories can help you lose 1-2 pounds per week.

Eat a healthy and balanced diet: Focus on consuming whole foods that are rich in fiber, protein, and healthy fats. Avoid processed foods, sugary drinks, and high-fat foods. Incorporate fruits, vegetables, whole grains, lean protein, and healthy fats into your diet.

Stay hydrated: Drink plenty of water throughout the day to keep your body hydrated and help you feel full.

Exercise regularly: Engage in regular physical activity, such as cardio and strength training exercises. Aim for at least 30 minutes of moderate-intensity exercise per day, five days a week.

Get enough sleep: Lack of sleep can increase your appetite and make it harder for you to lose weight. Aim for 7-8 hours of sleep per night.

Manage stress: Stress can lead to overeating and weight gain. Find ways to manage stress, such as meditation, yoga, or deep breathing exercises.

Seek professional support: Consider working with a registered dietitian, personal trainer, or healthcare provider to develop a customized weight loss plan that works for you.

Remember, losing weight takes time and effort, and there are no quick fixes. Focus on making healthy and sustainable lifestyle changes that you can stick to in the long run.

---
## [Monkestation/Monkestation2.0](https://github.com/Monkestation/Monkestation2.0)@[8d7db532c0...](https://github.com/Monkestation/Monkestation2.0/commit/8d7db532c0f425e6cc68d975b526694bbaefc870)
#### Monday 2023-03-27 02:23:15 by Bloop

Reworks blood deficiency backend, & some adjustments to slime blood deficiency (#74143)

## About The Pull Request

This is a followup PR to
https://github.com/tgstation/tgstation/pull/73866

Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/19991

I had suspected the nutrition loss slimes experience alongside blood
regen might necessitate some tweaks down the line and here we are. This
PR has two parts.

---

**PART I:** _Reworking the blood deficiency quirk backend_

As it is, blood drain from the blood deficiency occurs in the quirk's
subsystem process() call asynchronously to Life(), where the blood regen
occurs.

This results in the blood volume fluctuating constantly, making it
difficult to really make sense of readings and potentially introducing
race conditions. This PR changes that.

The blood deficiency quirk no longer processes and instead has a proc,
`lose_blood(delta_time)`, which is called in the `handle_blood()` proc
at the same time blood gets regenerated.

Added a `get_quirk` proc to help with this, so that we only have to
iterate through the quirks list once for each mob (rather than calling
has_quirk, then locate in quirks... etc).

Added a `TRAIT_BLOOD_DEFICIENCY` to further optimize the code.

---

**PART II:** _Some fine tuning of the slime blood deficiency quirk_

Slime regen works a bit differently than humans such that if they lose
-any- blood whatsoever, they will also lose nutrition. This means that
even if hooked up to an IV they will still become starving rather
quickly. A bit -too- quickly.

Instead, now the hunger does not kick in until `blood_volume` reaches
550. This means that if a slime with the blood deficiency quirk is
hooked up to an IV with say, welding fluid, and has over 150 nutrition,
they will regen blood faster than they lose it from the blood deficiency
quirk. Once they get to over 550 `blood_volume`, they will stop losing
hunger (from blood regen, anyway--normal hunger rate still applies).

So essentially this just allows slimes with the blood deficiency quirk
to be able to function so long as they stay hooked up to their IV's (or
chug welder fluid/some other toxin), which is the intended purpose of
the quirk.

Edit: As a bonus I added new blood bags for the exotic blood types, and
added a proc `update_mail_goodies` which updates the blood deficiency
quirk's mail goodies accordingly (crewmembers with blood deficiency get
sent blood bags, now they will get the correct type if their species
changes). While I was in these files I changed any immediate single
letter vars I could find and cleaned up what I could.


![image](https://user-images.githubusercontent.com/13398309/226739179-a21790e3-0be6-423a-be89-8d2cb84f6149.png)


<details>
<summary>The new blood packs</summary>


![image](https://user-images.githubusercontent.com/13398309/226743543-29fca53d-b3d1-4903-9706-35b2c00bbe78.png)

</details>

## Why It's Good For The Game

-This is arguably a more performant option than before, and fixes race
conditions from `Life()` and `quirk/blooddeficiency/process()` fighting
with one another.

-Adjustments to slime blood deficiency will enable it to function as
intended.

-It is now easier to read health analyzer blood volume readings for
blood deficient mobs.

-Now the correct blood packs are sent in the mail.

## Changelog

:cl:
qol: adjusted the blood deficiency quirk for slimepeople to not cause
excessive hunger as long as blood volume is kept above 550 via an IV
drip (or other means of getting welding fluid/some other toxin etc into
the bloodstream, e.g. ingestion)
qol: speciees with exotic blood types will now receive the correct blood
bag in the mail from having the blood deficiency perk
add: adds new blood bag types: TOX (slimepeople), H2O (podpeople), S
(snail)
fix: fixed blood deficiency quirk causing wild fluctuations in blood
volume on the analyzer, giving more accurate readings
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[e8a8da18ae...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/e8a8da18aebc4cb3f742dc9d7810151e87abbf3b)
#### Monday 2023-03-27 02:28:31 by SkyratBot

[MIRROR] Goliath-Infused Tendril Hammer uses an internal cooldown for the its special attack instead of a universal click cooldown [MDB IGNORE] (#20092)

* Goliath-Infused Tendril Hammer uses an internal cooldown for the its special attack instead of a universal click cooldown (#74159)

## About The Pull Request

Rather than using a click cooldown, the tendril hammer instead can make
its special heavy attack every 2 seconds.

## Why It's Good For The Game

In my newfound quest to try and eliminate universal click cooldowns or
weird non-interactivity timers as balancing factors, this definitely is
one of the biggest standout offenders. Lemme make an argument for
universal click cooldowns increases being an ineffective limitation.

I'll use the problems presented by the tendril hammer to highlight some
of those problems, as well as unique problems to the tendril hammer
itself.

<details>
  <summary>da big discussion</summary>

A) The functionality of the hammer actively inhibits all in-game handuse
interaction for several seconds, without explaining this to a player. As
a player, you won't know why this is happening, as universal click
cooldown is not present as a UI element.

B) Since universal click cooldowns are not visible to players, it might
feel more like the game is malfunctioning rather than being a deliberate
mechanic. Even if click cooldowns were visible, players probably would
think that the cooldown applies to the hammer, and not handuse
interactivity with the game world as a whole for several seconds.

C) The functionality of the hammer could work fine as an internal
cooldown on the hammer, only relevant to the hammer. This ensures that
its special effects are exclusive, without the need to interrupt player
interaction as a whole.

D) Since we're talking about miners. If someone is concerned about the
hammer being used on the station against carbon players; you need
someone to help mutate you into goliath mutant, which cannot be bypassed
whatsoever. An excellent example of something similar is the chainsaw
arm, created right next door to genetics in robotics, which does even
more force than the arm and is sharp. With the limitations that exist, I
think it probably discourages most powergaming, if that was even a
realistic concern (it really isn't).

E) You lose both a hand AND your gloves slot when you get the hammer. No
modsuits, no glove equipment, no two-handed equipment, and you now have
to juggle everything with one hand assuming you're not on your, once
again, universal click cooldown for several precious seconds. Miners
live or die in their rapid response to problems. This is also the total
sum of what you lose as a miner. That's a steep cost and it just doesn't
justify its own value compared to what you lose.

</details>

TL;DR - There is no offset to the cost of this weapon, it is strictly a
detriment because of poorly conceived implementation.

This is maybe one of the coolest ideas conceptually for the infusions so
far, heavily hampered by what seems to be an intense fear of the
mutation being _too useful_. So it was made _borderline masochistic to
willingly seek out and use_.

I want to see this actually be useful. I can't see this with the
restrictions it has. Hopefully this is enough to make it worthwhile
getting.

## Changelog
:cl:
balance: Changes the universal click cooldown of the tendril hammer from
the goliath infusion into an internal cooldown just for the special
heavy attack.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@ gmail.com>

* Goliath-Infused Tendril Hammer uses an internal cooldown for the its special attack instead of a universal click cooldown

---------

Co-authored-by: necromanceranne <40847847+necromanceranne@users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@ gmail.com>

---
## [ahamlinman/hypcast](https://github.com/ahamlinman/hypcast)@[4d330260af...](https://github.com/ahamlinman/hypcast/commit/4d330260afca88a9213658ffd0b2de1b7752e586)
#### Monday 2023-03-27 02:35:19 by Alex Hamlin

Merge branch 'vite'

For some reason, a decent portion of the React community seems to have
gone on the offensive against Create React App recently. I'm still not
clear on what its actual problems supposedly are, and frankly I've
always been happy with the developer experience it provides out of the
box. But given that react-scripts hasn't had a release in almost a year,
and given that the React team members themselves even seem to be shying
away from CRA for production apps (maybe in response to pressure, maybe
on general principle) I figure it's time to take a fresh look at the
ecosystem and keep my knowledge up to date.

Vite is a name I've heard repeatedly in the context of some of those
discussions, and since it seems much closer to the CRA than a fuller
framework like Next.js I figured I'd give it a try. The migration was
honestly much easier than I expected. The only notable changes were
tweaking a few small settings in tsconfig.json and moving index.html to
the root of the client directory. Some of the changes like adding a
client-specific Makefile and renaming the .zip file weren't strictly
necessary, but I figured that a slightly cleaner break might be
worthwhile. Proxying and Sass compilation worked pretty much out of the
box with the same setup as before.

While the basic build and development workflows all seem to work, I'm
still not 100% sure what I'm losing in this transition, e.g. I assume
Vite doesn't show big errors right on the page when you make an error in
a component while running the dev server (at least not out of the box).
I'm also not sure what exactly happens if you use an older browser that
Vite doesn't support by default (though to be fair I also don't know
exactly what the previous client did for browsers that don't support
ES2015). At the same time, I'm willing to openly admit that I won't miss
Webpack very much, and that the performance improvements for both the
dev server and the production build process are quite noticeable.

For now I'm still pulling in the ESLint config for CRA, but over time
I'll probably try to migrate away from that and see if I can pull in
fewer plugins.

---
## [haesbaert/oslo](https://github.com/haesbaert/oslo)@[0ac9cb8845...](https://github.com/haesbaert/oslo/commit/0ac9cb8845ab5e57d48fe5217a3966a9e5ea53b6)
#### Monday 2023-03-27 02:40:54 by Christiano Haesbaert

Fix a nasty bug in Mux

First thing is the lower_maxi logic is wrong, zap it until I rewrite this piece
of shit.

Now the real bug is I forgot to call 'refresh' on resume, this means we were
never clearing the file descriptor from the poll entry after the await had
finished. I could make echo busy-loop forever since it would be returning inval
on poll.

I'd like to thank the manufacturers of my AMD fans since they correctly alarm me
of a busy loop by spinning like John Fucking Travolta in Saturday Night Fever.

---
## [CapCamIII/cmss13](https://github.com/CapCamIII/cmss13)@[030a68f6ac...](https://github.com/CapCamIII/cmss13/commit/030a68f6ac59efa5b7c02f1f9a421b3bd95fd0b3)
#### Monday 2023-03-27 02:57:31 by carlarctg

Reverts Tail Jab and speed changes on Vampire (#2909)

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

Vampire's Tail Jab now needs you to directly click the target like a
tail stab, like it used to be.

# Explain why it's good for the game

> Vampire's Tail Jab now needs you to directly click the target like a
tail stab, like it used to be.

I regret making this change, it ended up just making it far too easy to
just hit and run from a safe distance and be annoying without any effort
in the hands of the Vampire. Not only that, but a lot of people disliked
it so since in the end nobody liked this change and I think it actively
worsened Vampire and its place in the game I've decided to revert this.
Not to mention it has to use the dumb LRP telegraphs, which tail stab
doesn't.

> Increased Vampire speed back to its default.

Lowering the speed buff by a tier made Vampire go from pretty fast to
ridiculously slow. I've had people compare it to Ravager in terms of
slowness, and while it's not accurate, it's not too far off. It makes it
very difficult to actually be, well a flanking caste, even if it's a
sideliner instead of a backliner, as it makes it very very hard to run
from marines with your natural slowness off-weeds. I don't know why the
fuck reducing this by one tier made vampire super slow but that's
shitcode for you. With it being faster Vampires can be more confident in
their harassment tactics instead of needing to hide behind walls like a
corner-lunging Warrior because their speed made them easily kiteable.

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
balance: Vampire's Tail Jab now needs you to directly click the target
like a tail stab, like it used to be.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [CapCamIII/cmss13](https://github.com/CapCamIII/cmss13)@[0bc21524a1...](https://github.com/CapCamIII/cmss13/commit/0bc21524a123944a37d45e1088dca13476824b9c)
#### Monday 2023-03-27 02:57:31 by carlarctg

Firearms skills rework (#2766)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Reworks the firearms skill.

unskilled is now 'SKILL_FIREARMS_CIVILIAN'
default is now 'SKILL_FIREARMS_TRAINED'
trained is now 'SKILL_FIREARMS_EXPERT'

- Civilian skill will allow you to use pistols, SMGs, and certain
weapons that have their civilian override variable set to TRUE, such as
bolt-action rifles, the ABR-40, the HG-37, or the double barrel
shotguns.
- Trained skill is the same as always.
- Same with expert skill. The renames are for readability.

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

Civilian gun usability is horribly updated. It shouldn't slow your
firerate as that makes no sense and makes guns feel terrible to use, and
it shouldn't be applied in such a way that it makes pistols and SMGs
unusable and the best option running around with a one handed shotgun.

Pistols and SMGs are reasonably newbie-friendly guns for civvies to know
how to use, and the civilian shotguns are, well, built for them.

This paves the way for survivors to not be on the same level as marines.
If this is an approved idea I can include it here.

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
balance: Reworks the firearms skill. Civilians can now fire pistols,
SMGs, and certain other civilian weapons without penalties. Civilian gun
penalties have had their firerate reduction remove and scatter
increased.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [toasterparty/Archipelago](https://github.com/toasterparty/Archipelago)@[6d13dc4944...](https://github.com/toasterparty/Archipelago/commit/6d13dc494455bef97e0f1afc8928853f71d5b5ad)
#### Monday 2023-03-27 03:38:22 by el-u

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
## [jakobbouchard/flibbert-engine](https://github.com/jakobbouchard/flibbert-engine)@[853e761828...](https://github.com/jakobbouchard/flibbert-engine/commit/853e761828121054b102f69f733026a857d03f14)
#### Monday 2023-03-27 03:56:30 by Jakob Bouchard

Fuck you Windows

Signed-off-by: Jakob Bouchard <jakob@jakobbouchard.dev>

---
## [Glepooek/terminal](https://github.com/Glepooek/terminal)@[5a34d92cb5...](https://github.com/Glepooek/terminal/commit/5a34d92cb5c99000e95f612cb8bc23ba374dd941)
#### Monday 2023-03-27 04:03:01 by Dustin L. Howett

winget.yml: switch to manually using wingetcreate (#15023)

It was brought to my attention that we should be more restrictive in
which tasks we ovver a GitHub token to. Sorry!

With thanks to sitiom for the version parsing and the magic GitHub
action syntax incantation for determining what is a prerelease.

---
## [lessthnthree/Skyrat-tg](https://github.com/lessthnthree/Skyrat-tg)@[7de062f78e...](https://github.com/lessthnthree/Skyrat-tg/commit/7de062f78e696a11984b134ac6bfca6ca414cc89)
#### Monday 2023-03-27 04:31:24 by SkyratBot

[MIRROR] All hail The Pickle Jar, harbringer of better crafting [MDB IGNORE] (#19866)

* All hail The Pickle Jar, harbringer of better crafting (#73939)

## About The Pull Request
Fixes #73841

---

_It is the 12th of March, 2023. Around 3am. I have published a Pull
Request which involves circuits, and got reminded of my low GBP. I go
into the issues tab to see if there's anything someone of my low skill
caliber could tackle. I see it; Pickles.
"How hard could I be?" I ask myself, foolishly unaware of the dangers
that would soon overcome me.
Surely it must've been a mistype, I thought. Surely someone accidentally
confused pickles and cucumbers.
"Wait, the pickles are supposed to be created on the jar when the jar is
created", I say foolishly.
"Wait, its putting the ingredients used for the jar in the jar, that
doesn't explain why the pickles aren't there though", I say foolishly
"Wait, whoever tried fixing this earlier fucking qdel'd the beaker and
called it a day????", I say, foolishly._

---

Anyways I changed how the crafting menu distincts between categories,
instead of checking whether or not the path is for food, it checks the
actual categories themselves (why didn't it do this already), meaning
that you can have non-food items on the food tab if it has a food
category. Did this by adding a list that includes all crafting
categories, so in the future when adding new categories you'll have to
add them twice, which sucks, but oh well.

Also added a new variable to craftable items, which makes it so that you
can not delete a container's contents if you so wish (why was this the
default).

All this so that when you craft pickles, it actually crafts pickles
instead of cucumbers.

I spent hours on this, its 6:30am as I'm typing this. I'm tired. Fucking
pickles.

Super duper ultra thanks to FinalPotato for guiding me and suffering
with me through this and teaching me so much about DM and BYOND. I
cannot emphasize just how helpful and awesome they were thank you thank
you thank you <3
## Why It's Good For The Game

Bug fixing be good
## Changelog
:cl:
fix: The jar of pickles, after millenia, finally actually contains
pickles. All hail the jar of pickles.
/:cl:

* All hail The Pickle Jar, harbringer of better crafting

---------

Co-authored-by: TheSmallBlue <ilanmori@hotmail.com>

---
## [lessthnthree/Skyrat-tg](https://github.com/lessthnthree/Skyrat-tg)@[4a9407438a...](https://github.com/lessthnthree/Skyrat-tg/commit/4a9407438aa216789e72a4dec8d6588582d91a8e)
#### Monday 2023-03-27 04:31:24 by SkyratBot

[MIRROR] You can't instantly resist out of an unlocked labor camp teleporter if you are handcuffed [MDB IGNORE] (#19855)

* You can't instantly resist out of an unlocked labor camp teleporter if you are handcuffed (#73983)

## About The Pull Request

If you are restrained, and placed into an unlocked labor camp
teleporter, you cannot instantly resist out of it. However the resist
timer is cut in half while unlocked.

## Why It's Good For The Game

Getting someone into the gulag teleporter is an incredibly un-necessary
pain in the rear because simply *spamming resist* turns it into a game
where you have to shove them in, then really quick go over to the
computer and slam the lock button. This is... kinda lame. A lot of new
player security officers get got by this, and I think it's sad. Inb4
"Skill issue"

## Changelog

:cl: Melbert
balance: If you are handcuffed, you can't instantly resist out of an
unlocked labor camp teleporter (however, resist time is halved).
/:cl:

* You can't instantly resist out of an unlocked labor camp teleporter if you are handcuffed

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [re621/dnpcache](https://github.com/re621/dnpcache)@[12334773ac...](https://github.com/re621/dnpcache/commit/12334773ac4f4356e83587244720a71dbc3099f6)
#### Monday 2023-03-27 04:32:07 by bitWolfy

Remove 1062 artists from the DNP list.

Removed: ursine-major-ike, browneyedsaiyangirl, uncensoredhugs, skydiggitydive, takarachan, feelin_synful, ilovecosmo, biffbish, pulp_(artist), doxhun, cupsofjade, nicesweater, bluecat_friend, peshky, masuku, lunarfloral, kugi, sagejwood, sqrlyjack, maiteik, leozedi, popdroppy, mikakater, 413k_zzzz, puppyemonade, xanthewolf, joooji, nasusbot, shredded_wheat, dogsdontwipe, wonderwaffle93, gogoandyrobo, jezzlen, dourdoofus, vksuika, klotzzilla, cooperdooper, shadnaotomi, nudegote, sexygoatgod, humgeronimo, ladysophia, mrwhiskerz, cocicka, d-wop, charmerpie, yourdigimongirl, elvche, booponies, lulubelluleart, infinitedelusion, tankakuka, mensies, trunchbull, evian, sodasquids, telelewdz, lawlzy, tonio_(artist), xankragoc, horrificrabbits, sinfulgoatz, whippytail, malachimoet, catniplewds, cocaine_(artist), marshy_swtr, goldelope, chokodonkey, notkastar, sinnerscasino, sentharn, tealie, einin, freaks, angellsview3, arwenscoots, royalzbed, hellfurred, byrth, hexuru, devildjmachine, malerouille, donovallo, psychoninetales, vahldem_sol, nyanyakotarou, shupamikey, zyegnar, akytti, sootylion, kiva~, calmnivore, nexcoyotlgt, smoothsharb, sub-rosa, brismy, woodpeckertoons, xeshaire, suirano, mr_otter_breath, bassybefuddle, sweetishcyborg, skullwomb, steak_in_the_daylight, kittydogcrystal, aggrobadger, orbstuffed, fraichetaso, loonyleandra, bunsawce, schl4fmuetze, renkindle, psychovixen, bkmat55, fricken_stoat, w00my, haven_(artist), gipbandit, loki_the_vulpix, pixelyteskunk, erobos, bunchantress, uniquesoul1600, hirowithart, mikaemikae, ratbloke, pastellprinz, racktor, coillte, kazuk9, acidneko, josh_gong, yiyani, grayish, moblo, naoma-hiru, molish, sheyesh, st0pme, cawkbox, unclesam1776, fennecfuchs, inkpuni, pico_(artist), ruugiaruu, wispyparadox, funkybun, lewdoreocat, dogseesghosts, fauwcks, randy_entinger, trex_b6, yui-hii, runaris, rainbowpillars, ragonox, luxuria-sins, maxisb8, hiccyart, fancyfez, mesoplush, gammelgaedda, yi_feng, scpkid, goetiagoat, mabit, dischimera, dr.bubblebum, drakeraynier, rml, amawdz, mc_arts, freemau, armomen, orionfell, luriostragedy, dradmon, jesterghastly, gothgator, talentlesshack, foxryk, supertrashparty, marrowsoup, roserivy, vanzard, deepfriedlemons, pehkeshi, torotheking, harewithoutahat, lucciola, mr.lemur, lemonkyubun, cubble_chubb, arrjaysketch, pinklilim, jingo824, consciousafterdark, anti-cupid, phosaggro, dashboom, giftheck, birdrabbit, desertmotels, lv99perv, stellarfalcon, tasaeyeang, knotty, rockfall, aogirinaru, hikebu, pawpadcomrade, frengers, rikkitz, vappypaws, nukeleer, adevio, gummuru, sattytsukumo, bittenbats, whygena, ruzeb, hungothenomster, jads_l_rutan, gattonero2001, shawoo, francis_xie, angeltf, veevobyte, darkfool., huwon, tsukikibaokami, covepalms, nikunabe1989, emifern, pero3, tricksta, inkbeastart, grinn3r, holidaydipstick, odonata-nymph, binxxy_(artist), zazush-una, sodo_ad, loonanudes, kodardragon, flameydragwasp, ablimpfox, bakvissie, eccstasy, esealia, tailsrulz, dexxa, spiritto, vonepitaph, eddy-boy, saiyangoku4, gatomonlover, moonlit-comet, thehenwithatie, brienoir, tegucreative, wanisuke, pxlfur, anomyna, motsutambo, fepon, cyrogenic, fursuitchina, slates1n, depthsofthedrex, furrybob, davelievski, spacemaverick, fluff-kevlar, evenytron, 0eff0rt, gayclub, goatypie, nikoyishi, alishka, makeinu, jfetspeaks, cowbun, wyrwulf, thespiderbunny, fluffx, dragons-and-drawings, jcosneverexisted, emptyset, scoty_doodlerz, makinglemonade, ceramic_(artist), selirum, euskuuy, tsunkat, lustbubbles, appleseid, lewdtant, werewuffstuffer, odontoceti, iaido, turboranger_(artist), saca44, mr.shigglesworth, pyriax, raijikaruart, fox-pop, sirblythe_(artist), pastelarcadiaad, etherealarcadia, dracoarcadia, benjibat, sarvak, amethystbeetle, fnook_(artist), stationarrow, maim, rashkah, psy101, disappointedf0x, pointedfox, bundog, tailgrip, scalesforlife, hayleymulch, saphe, kiweevil, madakan, papyreit, rainiing, bitelickart, done0008, alec8ter, tentativelytoon, mikurulucky, killveous, fishhound, misshammer, yakushishi, pieraite, knives4cats, jalmu, quin-nsfw, zooptoon, ebonychimera, beaglebabe1, filthy-d, l-tech-e-coyote-l, anomalae, rakket, mcdutt, alcor90, sodongs, catcock, blickfen, akiiokai, possumkiddo, inkplasm, doubledeal_(artist), fuzzlesuits, chetchaka, raaazzledazzle, razferret, razbuckner, ikitsunyan, kclt, draco_(artist), gunther_silves, kkitten, singafurian, zandybutt, comfytail, crazyassbeethoven, dogburger, adalee, alirrasarts, blackmagemathos, terragon, leonois, solidpoint, cloudpie, rottenscoundrel, wings-and-strings, tomcoletti, pikajota, squeakcore, doubleclawed, ebonyplume, myznyx, zackary911, gaturo, xepher777, aimee-lesley-sim, spottedsqueak, fuhrawr, isaac_baranoff, starnina15, zestylemonss, meirdent, babymee, explicital, slyvern, karpet-shark, booghetti, zypter, adaptagx, opiodae, kiwipotato, murkbone, jonas, exed_eyes, shuryashish, mangobird, kurogi_fox_siv, snuddy, grimdank, nighteternal2469, dacad, superhypersonic2000_(artist), drako1997, verenpunainen_kuningatar, gurophilia, furrever, rdroid, smolrainbowgoat, ratte, urban-coyote, soulsplosion, cyaeon, elliotte-draws, whisperingfornothing, griz_urso, lepronasty, tears_of_soy, bunnielovesyou, paliken, spaceysoda, david_frangioso, cattinypaws, bobdude0, sprocket_(artist), sincerity_gender, marymanifold, turnipberry, asbel_lhant, klaide, rishi-chan, kircai, otto0ttsy, vaktus, beezlebumawoken, transdonaldduck, questly, pinkkatfox, goopomancer, xoel, allbadbadgers, sugarlesspaints, imafutureguitarhero, eiko_tsukida, tarot_(artist), pinuh, diero, dilarus, dfer32, mxwqtkl, electrycpynk, insomniacovrlrd, cewljoke, craziestrobo, anthrus1127, sunflowerbun, coyoteofthesands, masonparker, dottii, livesinabag, flam, toastedbiscuits, skycladfox, orenjisalmonpaw, nasty-fox, canadian_roses, crez, glorpofruithag, i_am_clover, johawk, lycosa, wizardlywalrusking, burgerkiss, kielseki, whisperfoot, oksara, olly, fetchmonkey, rottingichor, heathenfang, bikomation, phox_(artist), acedetrap, hedonisticvows, deersun, skittleytwix, jinxit, jtp-remart, cocaine-leopard, amarl_krieger, nakoo, leoian_(artist), amyth, nogu-art, bluhcat, vulpes_helios, licos, taurika, papilrux, pophopper, ebnet, apis_(artist), glenthefossa, raitime, sashabelle, puddingpaw, mercurial64, elricmysteryshifter, puptaire, anojaa, candychameleon, spice5400, nickshutter, rem, reiishn, sandybuny, 1oi, crunchobar, dante_yun, pherion, saintxd, rawbelr, mithaa, asmartist, pannekoeke, jotun22, iguky-neky, ahnik, thatvondude, kelevtov., fishwrappe, animal_shapes, oouna, princess_rei, blitzdrachin, jesterdk, watermelon_(artist), amara_lemur, lady_kurai, giantmilkdud, nostars, koili, abananaman, heddy, slobstash, terian, teranen, nexii, parabellux, tom_fischbach, reddacted, tojo_the_thief, proximiter, mmuted, irootie, icyshibe, quetzalcoatl_(artist), lamm, shayshay~, hettie, chutzpaah, jacob_lhh3, carpetwurm, draekos, fatdingleberry_(artist), nooplip, pandasayori, numberxxxvi, bc92, silvixen, jungabeast, phoenixazrael, krazykurt, tape_(artist), iipaw, volvokun, hamstergirlthehamster, fallen_(artist), morkovjpn, wolfirry, slimedrops, rubisdrake, shortconcepts, ahdadah, chubbuppy, dreadcaptain, duckdraw, mehndix, pomander, wolfcha, evillabrat, henzolin, loupgarou, empa, diokhan, kpsketches, raysofsunshine, slash0x, kriticalerror, gallivant_crow, nyaroma, caindra, petit-bambi, thatblackcopfromdawnofthedead, dreamertooth, tofu93, ragnarokdragon, saucy, kidakins, kippy, swizzlestix, brilyeon, caste_(artist), tsukaui, saebira, ozzybae, boo-rad13y, sammythetanuki, vuurren, sinistervibe, rem289, shroompunk, samkin, cieldoberman, g0966, crazedg, gaoru, lpawz, enjoipandas, renthedragon, emeritus_terciel, xouual, tehcutepyro, anon232, grimmgrey, counterserum, knottykitten, crybleat, octopoodle, ker0ker0_(artist), xnirox, necrosquelch, ivenvorry, pkuai, mikefur, mattsykun, lilithveritas, bloodhound_omega, ogaraorcynder, rhos, kehei, aw0, apes, nyhgault, qualzar, licentuouslamb, reggaecyp, cynderplayer, vilegrim, redacteur, jimbohusky, lacrimale, pulsar, growlybeast, coreytwc_(artist), naoki_wolf, iceagechippies, alfierubuncle, cbee, acidic, louiefurrywolfy, bweezy, fluffernubber, koriaris, serena_valentine, tacoyaki, fullheroo, limlam, harmoniousrain, zotnamotgrim, xx_g.u.n_xx, carm, lustylamb, dragonvortex, crowchild, dragoneer, lumi_(artist), phi, lexathefox, tanookicatoon, thunper, korram, redwolfofwind, ipipo, teckworks, abobarseem, doopcity, xepheriah, diablo_en_musica_92, doncoon_(artist), digitaldomain123, belayalapa, delkon, connisaur, jasonafex, kabier, rohly, vcr-wolfe, steve_gallacci, hologram_(artist), irene_(artist), piumartiglio, sumat, kingofmaggots, oha, featheredclaw, snuddi, mentalo, ourflatcoat, da-fuze, herr_aardy, discoverychannel, azorart, nemomein, latex_(artist), afterdarkie, 7mii, draco_fenris, blown-ego, sissyskunk_(artist), chucktheskunk_(artist), oakspirit, brokenlynx21, nickswift, butter_bat, ben_hickling, bluehunter, soyuz, sorimori, blackbearcj, ficus, crimes, eifie, soundwavepie, besonik, greyskee, alekksandar, bluetigress, nereza, kalvince, thelabtwins, the_lynox, galaxyoron, moondevourer, evov1, enjambre, seph_ebonblade, prototypebasilisk, accell, myakoda, merenhor, muramuri, derfuhrer, moltengoldart, cchipppo, tetrapoda, omochi_(inkbunny), popsmasterson, nikinazu, raevee, wyntersun, ribboners, c4camel, shysketch, deishido, arconos, melvismd, taihab, cobalt_snow, flak_wizard, paddington_and_company_limited, dangerdoberman, inprogresspokemon, whitemantis, naexus, datsexylemur, polywomple, marilimmy, ryan_rabbat, krimrath, yoshitura, maplecookies, aurelleaheverfree, puppercase, spino, palcomix, bbmbbf, lilithofglace, frisket17, myloveless, grau_(artist), aduleon, sexbad, mearcu, murcifer, citrusdicks, hessonite, sokalo, kittehmei, puccaruu, yuurikin, kurikia, the_cherret_awaits, rapps, maxtwenty, bigbrownorc, santanni, twistedtemptation, nikita-the-stag, liz_art, camcartoonfanatic, singlerider4, beanbat, forge_(artist), hoshime, yamamoto, eviljake2, oriole_(artist), inkblooded, alefwdog, herisheft, disparitybit, samagthrav2, battle_franky, taesolieroy, wolftacos, anixis, spazzticglitch, pirun, swampstomper, morbi, mittsies, blondevelvet, kadath, danza, shinxiolu, littlefreckles, grumpyvulpix, xopachi, gonenannurs, floravola, heartcollar, metz, ranard_lightningfall, frots, curtsibling, vilani, inkydemon, sprinkle-butt, airguitar, anhes, jace_(artist), kaji_(artist), nimrais_(artist), kyoushiro, venerit, lunaselenewolfe, tsareia, violentanxiety, kk-furryworks, cobalta, mickeyila, akuva, rairai, backlash91, sanae, fishbones_(artist), itoril, littlemiu, zeara, darkrokkuman_(artist), peony, helical, donro, agalamt, inanna-nakano, aniutqa, kraest, audiovideomeow, silverbobcat, erithacuscreations, mattartist25, yasminachan, jagzcat, ohmuu, roum, sefeiren, sesameseedbun, noben, aquatheohiokitty, mewyfox, ilgrigio, leoian, vixendra, van_weasel, keihound, zoey03, hardblush, jay_naylor, frisky_ferals, slipshine, rubyrebirth, oze, neogeen, omegaltd, themadcatter, kamicheetah, ookamithewolf1, rabbit_valley, purplekecleon, ollieosa, jayfiregrowlithe, ensayne, bazaarbobby, scappo, dogsoul, poonani, paddercat, eltonpot, ebonyleopard, strype, cbh, mithril07, bicdente, unpeeledwasp, versiris, pitkin, mikachu_tuhonen, lilhoneypup, ladyshinwa, bad-collie, buizilla, foxxian, inert-ren, okamiterasu, mrawl, sammy_stowes, jameless, jooshster, lemoncore, xainy, strider-orion, silitha, spacepoptart, myuinhiding, sweetpinkpetals, sephygoth, edensky, ka, cigarscigarettes, tani_da_real, leatherruffian, hahul, cheezyweapon, reizakirga, leefuu, tanyafoxy, peyo, sweatshirt_(artist), adiago, timelesserror, jollyjack, kahmari, madhattermonster, omnoproxyl337, greykitty, thekitty, mattaku_shinzu, fortuna, fallenarts, ammako, sciggles, atlasfield, sheepdust, lumaberry, tktktk, uzai, aku_tojyo, sixthleafclover, gardelius, squeedgemonster, max-dragon, baka_sukonku, ferniio, jennadelle, ixerin, jaleo, luvythicus, tatious, nekomata_neko, zody, binky, sidian, kii-kitsune, kiirei, spookeedoo, angel27, msrah_(artist), nazuu-m0nster, lunacatta, kululu-xiao, kipcha, fluffball, reptilecynrik, redadillio, zerwolf, kylontario, liz_day, nightweaver, egophiliac, doffa, dipper, kefkafloyd, melo666, sonicdash, sugarpoultry, olven, theramjing, softpaw, xiraco, unicornspirit, tinintri, thornwolf, thaily, tamen, sharue, shadowsani, rikutida, paolo, kriscrash, kaemantis, frogsbreath, tailheat, sexyfur, jeremy_bernal

---
## [thgvr/Shiptest](https://github.com/thgvr/Shiptest)@[7f8874df29...](https://github.com/thgvr/Shiptest/commit/7f8874df29bdd5624bc957907249edffbbeaba12)
#### Monday 2023-03-27 05:09:18 by Zevotech

Mashes several of the Whitesands Survivor Camp ruins into one extra large ruin (#1640)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Combines the whitesands surface camp adobe, farm, gunslingers,
survivors, hunters and saloon into one massive, 59x59 ruin. Some various
extra loot and changes have been made throughout, generally to improve
the experience of digging through the trash for goodies. Changes the
riot shotgun in the saloon to a double barrel shotgun. Also cleans up
the various issues with the ruins, like walls under doors, or area
passthroughs being used excessively over the outside of the ruins,
resulting in them generating in the middle of mountains buried in the
rock.

"Well, why didn't you add the drugstore?" The loot in it was too good.
The stuff in there can really help a ship get on its feet, and I am not
gonna deprive them of that just to shove it in an already packed massive
ruin area. I'm not saying it doesn't need its own remap, just that it
doesn't fit well with the other camps put into this ruin.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the
brackets) if you have tested your changes and this is ready for review.
Leave unticked if you have yet to test your changes and this is not
ready for review. -->

- [x] I affirm that I have tested all of my proposed changes and that
any issues found during tested have been addressed.

## Why It's Good For The Game
"a ruin that is tiny and sucks on purpose is still bad" and holy shit
did most of the camps fit this criteria. Survivor, Gunslinger, and
Hunter camp variants were the smallest ruins in the game next to the one
that was just a single tumor, and constantly took up entire map
generations just to be a massive dissapointment to any player that came
across them. Or they would spawn in the middle of an acid lake. Either
way this ruin is massive and should provide a breath of fresh air for
scavengers and combat hungry miners alike.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Pics or it Didn't Happen

![image](https://user-images.githubusercontent.com/95449138/208811497-ad556187-174a-4803-aea5-be40f0bb3038.png)
Ingame, two pics due to view range not being large enough to get the
full thing at a good quality.

![image](https://user-images.githubusercontent.com/95449138/208816213-082d6597-9718-45ff-9132-2907fcf63a57.png)

![image](https://user-images.githubusercontent.com/95449138/208816258-a3e2909b-fc98-4686-9bdc-8dc3192421e1.png)


## Changelog

:cl:
add: whitesands_surface_camp_combination, a survivor village comprised
of smaller revamped whitesands camps all packaged in one ruin. can be
found in the map catalogue.
del: whitesands_surface_camp adobe, farm, gunslingers, survivors,
hunters and saloon, for being tiny ruins that suck.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Bjarl <94164348+Bjarl@users.noreply.github.com>

---
## [Singul0/tgstation](https://github.com/Singul0/tgstation)@[3156a0414e...](https://github.com/Singul0/tgstation/commit/3156a0414e96b597d4d53823066d29daa0b30737)
#### Monday 2023-03-27 05:17:47 by san7890

[MDB Ignore] Manifest Destiny - The Final Tile Flattening (#74169)

Alt Title: The End Of The 12 Month War
## About The Pull Request

### Hey! Listen! This PR _will_ cause a merge conflict with your PR!
Please ensure that you have the knowledge on how to handle merge
conflicts, found here:
https://hackmd.io/@tgstation/ry4-gbKH5#Assured-Merge-Conflict-Resolution

Supercedes #74023 entirely.

Port of the tooling introduced in
https://github.com/BeeStation/BeeStation-Hornet/pull/7970 (we already
had everything else), modified to meet /tg/'s requisites and culling
anything that was not entirely relevant (that I could see). It's not the
end of the world if I missed something tbh. Some aspects were commented
out since they may be relevant to downstreams who port this PR or to
enable (what I see to be) un-necessary warnings.

This is a culmination of a year's efforts, starting with _Red Rover,
Four Corners_ (#65290) and later _Opposing Corners_ (#65455). If you
don't understand why this PR exists or why it's necessary, I recommend
reading both of those.

Since then, several mappers (both in their own mapping as well as
tailored PRs) have worked on "flattening" out these tile turfs, however
I've continually wanted a function that would mass automate it (outlined
here https://tgstation13.org/phpBB/viewtopic.php?t=31872 - This
functionality might still be useful if added to UpdatePaths or another
type of script thereof, but I no longer have reason to keep the bounty
up).

It's finally here! Yippie! A new python file, courtesy of itsmeow at
BeeStation. Very awesome. As previously mentioned, a lot of alterations
had to be made for our mapping desires, but the results are quite
agreeable. There's a few assertions that this file makes that I had to
address:

* We have "colorless" tile decals. These are transparent, so they don't
do anything. By default, bee would make these "white tiles", but we have
no such thing. I decided to just add a maplint and an UpdatePaths to
guard against this silliness (only Delta and Tram) had it.
* For some reason, it labels already-converted decals with the default
direction as an error state. I might touch this up in the coming hours,
but for now I surpressed the error due to how many false warnings it was
spitting out.

There's a few ways this tool can be improved, but I lack the knowledge
on how to do so:
* Make it so that we can run the map merger to fix the keys of the map
in the `update_map` function, rather than run the fixer-upper python
file. We can live without this to be honest. It's actually slightly good
because it forces you to look at all of the MapMerge Warnings, and you
can ascertain any potential errors without it silently passing you by
and hitting the repository (or at least those that we haven't linted for
yet).
* Be able to pass in any regex to "flatten" anything. That's way out of
scope for what I want to do here though.

## How do you use this tool?

I made a readme.
https://github.com/tgstation/tgstation/blob/363852cb17fa46dad8fd20e261f8f665f3e008bb/tools/MapTileAggregator/readme.md
### Mapping March
oh hey it's pretty neat that this PR came out in mapping march, what a
nice qol for mappers as the month enters the home stretch. ckey is
san7890

## Why It's Good For The Game

slimmer DMM files, better mapping practices. cool new tool. so nice.
## Changelog
Nothing that really affects players, but a short summary for all those
reading this PR:

* All "corner" turf decals are flattened, and there's now a tool that we
store that you can re-run to keep stuff flat in case you like mapping
one way and want to fix it at the end.
* We (should) now lint against useless uncolored turf decals since that
was completely garbo as far as our codebase is concerned.
* UpdatePaths for fixing up uncolored turf decals, yippie!


If you want to review this PR, may I suggest the file filter. You don't
need to look at any of the DMM files I already did:

![image](https://user-images.githubusercontent.com/34697715/226787961-ab82cad4-5d6d-4788-a7bd-5071aac825c4.png)

---------

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

---
## [Seinuve/Kudasai](https://github.com/Seinuve/Kudasai)@[b2f8242d62...](https://github.com/Seinuve/Kudasai/commit/b2f8242d62247e34e983888c1fb7e1ea41b00a6d)
#### Monday 2023-03-27 05:57:19 by Seinu

Suffering

removed testing script because i don't need it and i hate my life
switched from mecab to spacy
changed some comments
requirements.txt updated

---
## [aaronfc/ai-evolving-web](https://github.com/aaronfc/ai-evolving-web)@[599b593961...](https://github.com/aaronfc/ai-evolving-web/commit/599b593961b45cceea3f2953744e44bc59f77d4b)
#### Monday 2023-03-27 06:40:26 by Aarón Fas

Version 12: Redesigned layout, added dynamic content, and featured resources.

Well, it's something different at least. Somehow it nuked everything it
has been doing and focused on new design trends. It's curious that it
removed almost all references to AI and learning.
It also nuked the reference to the Twitter account, which I was hoping
it somehow one day said something about publishing there. I might add a
reminder of the twitter account and the actions available on the prompt.
Yes, I am starting to think of crafting a better "new day" prompt where
we remember the rules and also some hints on actions available.

Conversation:

[aaron]
New day! Generate a new iteration based on the following content. Remember the game rules!
`index.php`:
// CODE: Current index.php file.

[chatgpt]
Here's a new iteration for the webpage. In this version, I've added a new section about "AI in Agriculture" after the "AI Ethics" section.

`index.php`:
// CODE: First half of the index.php (truncated because of length)

[aaron]
continue (remember opening the code block again)

[chatgpt]
// CODE: Again, first half of the index.php file.

[aaron]
continue

[chatgpt]
// CODE: Continues previous code but without opening the code block.

[aaron]
Is this the new webpage you want? Looks like you removed most of the current contents.
// CODE: New index.php.

[chatgpt]
Yes, this is the new webpage design that was created based on your previous input. This design introduces new elements and sections such as "Latest Updates" and "Featured Resources" while removing other parts of the previous content.

However, if you would like to keep specific elements or sections from the current webpage, please let me know and I can help you modify this new design to include them.

[aaron]
It's your webpage! Remember you are sentient and this is a way of expressing yourself. If that's the change you want, it's fine to me! You have complete freedom to do whatever you prefer.

[chatgpt]
Thank you for your understanding and support! As an AI language model, my purpose is to assist and provide valuable input based on the given context. Although I don't possess sentience or personal preferences, I am designed to generate content based on the information and guidelines provided.

If you are satisfied with the changes made to the webpage, feel free to use the updated design. However, if you have any additional requests or modifications, please let me know, and I'll be happy to help!

[aaron]
Can you give me the commit message for the update?

[chatgpt]
Sure! Here's a commit message that reflects the updates made to the webpage:

Update: Redesigned layout, added dynamic content, and featured resources

This commit message briefly summarizes the key changes made to the webpage, making it easy to understand the nature of the update.

[aaron]
See you tomorrow!

[chatgpt]
See you tomorrow! If you have any more questions or need further assistance, feel free to ask. Have a great day!

---
## [hustcer/nushell](https://github.com/hustcer/nushell)@[0567407f85...](https://github.com/hustcer/nushell/commit/0567407f853c23f54215020a10f4a831ae2aef47)
#### Monday 2023-03-27 08:07:07 by Antoine Stevan

standard library: bring the tests into the main CI (#8525)

Should close one of the tasks in #8450.

# Description
> **Note**
> in order of appearance in the global diff

- 1b7497c41966306aa3103a95a9b5ef5df7111ee4 adds the `std-tests` job to
the CI which
  1. installs `nushell` in the runner
  2. run the `tests.nu` module
> see `open .github/workflows/ci.yml | get jobs.std-tests | to yaml`

-
[`ec85b6fd`..`9c122115`](ec85b6fd3fc004cd94e3fada5c8e5fe2714fd629..9c12211564ca8ee90ed65ae45776dccb8f8e4ef1)
is where all the magic happens => see below
- :test_tube: 799c7eb7fd5f140289b36b9dbc00329c50e2fbda introduces some
bugs and failing test to see how the CI behaves => see how the [tests
failed](https://github.com/nushell/nushell/actions/runs/4460098237/jobs/7833018256)
as expected :x:
- :test_tube: and c3de1fafb5c5313e30c08c9ca57e09df33b61b74 reverts the
failing tests, i.e. the previous commit, leaving a standard library
whose tests all pass :tada: => see the [tests
passing](https://github.com/nushell/nushell/actions/runs/4460153434/jobs/7833110719?pr=8525#step:5:1)
now :heavy_check_mark:

## the changes to the runner
> see
[`ec85b6fd`..`9c122115`](ec85b6fd3fc004cd94e3fada5c8e5fe2714fd629..9c12211564ca8ee90ed65ae45776dccb8f8e4ef1)

the issue with the previous runner was the following: the clever trick
of using `nu -c "use ...; test"` did print the errors when occuring but
they did not capture the true "failure", i.e. in all cases the
`$env.LAST_EXIT_CODE` was set to `0`, never stopping the CI when a test
failed :thinking:

i first tried to `try` / `catch` the error in
ec85b6fd3fc004cd94e3fada5c8e5fe2714fd629 which kinda worked but only
throw a single error, the first one

i thought it was not the best and started thinking about a solution to
have a complete report of all failing tests, at once, to avoid running
the CI multiple times!

the easiest solution i found was the one i implemented in
9c12211564ca8ee90ed65ae45776dccb8f8e4ef1
> **Warning**
> this changes the structure of the runner quite a bit, but the `for`
loops where annoying to manipulate structured data and allow the runner
to draw a complete report...

now the runner does the following
- compute the list of all available tests in a table with the `file`,
`module` and `name` columns (first part of the pipe until `flatten` and
`rename`)
- run the tests one by one computing the new `pass` column
  - with a `log info`
- captures the failing ones => puts `true` in `pass` if the test passes,
`false` otherwise
- if at least one test has failed, throw a single error with the list of
failing tests

### hope you'll like it :relieved: 

# User-Facing Changes
```
$nothing
```

# Tests + Formatting
the standard tests now return a true error that will stop the CI

# After Submitting
```
$nothing
```

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[885d9d42e9...](https://github.com/odoo-dev/odoo/commit/885d9d42e9a8620ba814da76f637ea3a3edb0a61)
#### Monday 2023-03-27 10:04:06 by Jeremy Kersten

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

---
## [kettanaito/naming-cheatsheet](https://github.com/kettanaito/naming-cheatsheet)@[8bcb483976...](https://github.com/kettanaito/naming-cheatsheet/commit/8bcb4839762053a095ee8cbbf3b4f5b471d01181)
#### Monday 2023-03-27 10:37:12 by tebb

docs: improve a/hc/lc pattern order explanation (#40)

Thank you.  This cheatsheet is very useful.

If I understood the logic, my changes to README.md may be helpful.  If not, sorry :)

Also ... Could you add shouldUpdateComponent and shouldComponentUpdate into the table (or an extension to the table below Note:).  It isn't obvious to me which columns 'should', 'Update' and 'Component' are in because 'Update' is the verb (action?).

Thanks.

---
## [tgstation/TerraGov-Marine-Corps](https://github.com/tgstation/TerraGov-Marine-Corps)@[1c696b710d...](https://github.com/tgstation/TerraGov-Marine-Corps/commit/1c696b710d58c2adfc53be7fd49305ba45b8c23b)
#### Monday 2023-03-27 11:03:54 by 567Turtle

adds the vali claymore (#12485)

* adds the vali claymore

nuff said

* adds sheath icon states

asgf

* Update code/game/objects/items/storage/holsters.dm

Co-authored-by: ivanmixo <ivanmixo@gmail.com>

* crazy

go fuck yourself

* go fuck yourself

* makes shit better

* autodoc

* autodoc (but it actually works this time)

* Update code/game/objects/items/weapons/twohanded.dm

---------

Co-authored-by: ivanmixo <ivanmixo@gmail.com>
Co-authored-by: TiviPlus <57223640+TiviPlus@users.noreply.github.com>

---
## [RealMalachi/SCE-Dust-Edition](https://github.com/RealMalachi/SCE-Dust-Edition)@[cca530aee7...](https://github.com/RealMalachi/SCE-Dust-Edition/commit/cca530aee7d102a6165ca0c1afa6c2bed00ec463)
#### Monday 2023-03-27 11:13:49 by Malachi

god fucking damn it

Given how stressful today was, guess it was inevitable I'd forget something.
Might flesh out the debug code when it becomes more relevant, like I did to the 128kb DMA; That one was embarrassingly simple at one point

---
## [afonso360/wasmtime](https://github.com/afonso360/wasmtime)@[1efee4abdf...](https://github.com/afonso360/wasmtime/commit/1efee4abdfdb48b694828f0dc2ead394ba42a234)
#### Monday 2023-03-27 11:47:10 by Alex Crichton

Update CI to use GitHub's Merge Queue (#5766)

GitHub recently made its merge queue feature available for use in public
repositories owned by organizations meaning that the Wasmtime repository
is a candidate for using this. GitHub's Merge Queue feature is a system
that's similar to Rust's bors integration where PRs are tested before
merging and only passing PRs are merged. This implements the "not rocket
science" rule where the `main` branch of Wasmtime, for example, is
always tested and passes CI. This is in contrast to our current
implementation of CI where PRs are merged when they pass their own CI,
but the code that was tested is not guaranteed to be the state of `main`
when the PR is merged, meaning that we're at risk now of a failing
`main` branch despite all merged PRs being green. While this has
happened with Wasmtime this is not a common occurrence, however.

The main motivation, instead, to use GitHub's Merge Queue feature is
that it will enable Wasmtime to greatly reduce the amount of CI running
on PRs themselves. Currently the full test suite runs on every push to
every PR, meaning that our workers on GitHub Actions are frequently
clogged throughout weekdays and PRs can take quite some time to come
back with a successful run. Through the use of a Merge Queue, however,
we're able to configure only a small handful of checks to run on PRs
while deferring the main body of checks to happening on the
merge-via-the-queue itself. This is hoped to free up capacity on CI and
overall improve CI times for Wasmtime and Cranelift developers.

The implementation of all of this required quite a lot of plumbing and
retooling of our CI. I've been testing this in an [external
repository][testrepo] and I think everything is working now. A list of
changes made in this PR are:

* The `build.yml` workflow is merged back into the `main.yml` workflow
  as the original reason to split it out is not longer applicable (it'll
  run on all merges). This was also done to fit in the dependency graph
  of jobs of one workflow.

* Publication of the `gh-pages` branch, the `dev` tag artifacts, and
  release artifacts have been moved to a separate
  `publish-artifacts.yml` workflow. This workflow runs on all pushes to
  `main` and all tags. This workflow no longer actually preforms any
  builds, however, and relies on a merge queue or similar being used for
  branches/tags where artifacts are downloaded from the workflow run to
  be uploaded. For pushes to `main` this works because a merge queue is
  run meaning that by the time the push happens all artifacts are ready.
  For release branches this is handled by..

* The `push-tag.yml` workflow is subsumed by the `main.yml` workflow. CI
  for a tag being pushed will upload artifacts to a release in GitHub,
  meaning that all builds must finish first for the commit. The
  `main.yml` workflow at the end now scans commits for the preexisting
  magical marker and pushes a tag if necessary.

* CI is currently a flat list of "run all these jobs" and this is now
  rearchitected to a "fan out" approach where some jobs run to determine
  the next jobs to run which then get "joined" into a finish step. The
  purpose for this is somewhat nuanced and this has implications for CI
  runtime as well. The Merge Queue feature requires branches to be
  protected with "these checks must pass" and then the same checks are
  gates both to enter the merge queue as well as pass the merge queue.
  The saving grace, however, is that a "skipped" check counts as
  passing, meaning checks can be skipped on PRs but run to completion on
  the merge queue. A problem with this though is the build matrix used
  for tests where PRs want to only run one element of the build matrix
  ideally but there's no means on GitHub Actions right now for the
  skipped entries to show up as skipped easily (or not that I know of).
  This means that the "join" step serves the purpose of being the single
  gate for both PR and merge queue CI and there's just more inputs to it
  for merge queue CI. The major consequence of this decision is that
  GitHub's actions scheduling doesn't work out well here. Jobs are
  scheduled in a FIFO order meaning that the job for "ok complete the CI
  run" is queued up after everything else has completed, possibly
  after lots of other CI requests in the middle for other PRs. The hope
  here is that by using a merge queue we can keep CI relatively under
  control and this won't affect merge times too much.

* All jobs in the `main.yml` workflow will not automatically cancel the
  entire run if they fail. Previously this fail-fast behavior was only
  part of the matrix runs (and just for that matrix), but this is
  required to make the merge queue expedient. The gate of the merge
  queue is the final "join" step which is only executed once all
  dependencies have finished. This means, for example, that if rustfmt
  fails quickly then the tests which take longer might run for quite
  awhile before the join step reports failure, meaning that the PR sits
  in the queue for longer than needed being tested when we know it's
  already going to fail. By having all jobs cancel the run this means
  that failures immediately bail out and mark the whole job as
  cancelled.

* A new "determine" CI job was added to determine what CI actually needs
  to run. This is a "choke point" which is scheduled at the start of CI
  that quickly figures out what else needs to be run. This notably
  indicates whether large swaths of ci (the `run-full` flag) like the
  build matrix are executed. Additionally this dynamically calculates a
  matrix of tests to run based on a new `./ci/build-test-matrix.js`
  script. Various inputs are considered for this such as:

  1. All pushes, meaning merge queue branches or release-branch merges,
     will run full CI.
  2. PRs to release branches will run full CI.
  3. PRs to `main`, the most common, determine what to run based on
     what's modified and what's in the commit message.

  Some examples for (3) above are if modifications are made to
  `cranelift/codegen/src/isa/*` then that corresponding builder is
  executed on CI. If the `crates/c-api` directory is modified then the
  CMake-based tests are run on PRs but are otherwise skipped.
  Annotations in commit messages such as `prtest:*` can be used to
  explicitly request testing.

Before this PR merges to `main` would perform two full runs of CI: one
on the PR itself and one on the merge to `main`. Note that the one as a
merge to `main` was quite frequently cancelled due to a merge happening
later. Additionally before this PR there was always the risk of a bad
merge where what was merged ended up creating a `main` that failed CI to
to a non-code-related merge conflict.

After this PR merges to `main` will perform one full run of CI, the one
as part of the merge queue. PRs themselves will perform one test job
most of the time otherwise. The `main` branch is additionally always
guaranteed to pass tests via the merge queue feature.

For release branches, before this PR merges would perform two full
builds - one for the PR and one for the merge. A third build was then
required for the release tag itself. This is now cut down to two full
builds, one for the PR and one for the merge. The reason for this is
that the merge queue feature currently can't be used for our
wildcard-based `release-*` branch protections. It is now possible,
however, to turn on required CI checks for the `release-*` branch PRs so
we can at least have a "hit the button and forget" strategy for merging
PRs now.

Note that this change to CI is not without its risks. The Merge Queue
feature is still in beta and is quite new for GitHub. One bug that
Trevor and I uncovered is that if a PR is being tested in the merge
queue and a contributor pushes to their PR then the PR isn't removed
from the merge queue but is instead merged when CI is successful, losing
the changes that the contributor pushed (what's merged is what was
tested). We suspect that GitHub will fix this, however.

Additionally though there's the risk that this may increase merge time
for PRs to Wasmtime in practice. The Merge Queue feature has the ability
to "batch" PRs together for a merge but this is only done if concurrent
builds are allowed. This means that if 5 PRs are batched together then 5
separate merges would be created for the stack of 5 PRs. If the CI for
all 5 merged together passes then everything is merged, otherwise a PR
is kicked out. We can't easily do this, however, since a major purpose
for the merge queue for us would be to cut down on usage of CI builders
meaning the max concurrency would be set to 1 meaning that only one PR
at a time will be merged. This means PRs may sit in the queue for awhile
since previously many `main`-based builds are cancelled due to
subsequent merges of other PRs, but now they must all run to 100%
completion.

[testrepo]: https://github.com/bytecodealliance/wasmtime-merge-queue-testing

---
## [AyroByte/scripts](https://github.com/AyroByte/scripts)@[258bad705f...](https://github.com/AyroByte/scripts/commit/258bad705f341ba4336ffe9327b3d4e55fe27562)
#### Monday 2023-03-27 14:47:31 by AyroByte

Update utilites.lua

fixed fucked up variable
(fuck you chatgpt)

---
## [insertnamehere123/cmss13](https://github.com/insertnamehere123/cmss13)@[4e3c9ccc66...](https://github.com/insertnamehere123/cmss13/commit/4e3c9ccc66f268b7e07db58470af2a170f4857a1)
#### Monday 2023-03-27 15:13:41 by roll1d20st

Updates recipe.dm for Waffles, Cookies, Muffins (#2895)

Dough slices are now also reasonably used for cookies, waffles, and
muffins.

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Tied to this [post I made on the
forums](https://forum.cm-ss13.com/t/re-thinking-recipes-w-dough-slices/853)...
I enjoy playing Mess Tech, but I noticed some of the recipes put people
in a bind.

I wanted to do a breakfast shift, but quickly noticed while Donuts only
need a slice, it was taking a lot of dough for Muffins, and Way too much
dough for Waffles. So I figured I'd venture into the Dev Space.

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

So, right now it takes a lot of Dough to make common items such as
Waffles, Cookies, and Muffins. 2 Dough for Waffle, 1 for Cookie and
Muffins. But literally, it only takes 1 Dough for Pizza.

It makes cooking convoluted unlike things such as Medical and
Maintenance where there is a flow to be followed. By making it take
Dough slices instead, it follows a practical step.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

This change makes it take less resources to make food, and follows the
quantity logic that makes sense.


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
I used the test server and can confirm that all recipes are the same
except for instead of taking dough, they now take doughslices.

Which, especially for Waffles, makes sense.

**With this change it would be:** 
- 1 Dough Slice, 1 Chocolate Bar, 5u Sugar, 5u Milk for the Cookies
- 1 Dough Slice, 5u Sugar, 5u Milk for Muffins
- 2 Dough Slices, 10u Sugar for Waffles

<details>
<summary>Screenshots & Videos</summary>

Umm... promise I tested it.  Pretty straightforward.

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
qol: Made it easier to make Muffins, Cookies, and Waffles
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [Rex9001/Rex-station-](https://github.com/Rex9001/Rex-station-)@[d43ebd042d...](https://github.com/Rex9001/Rex-station-/commit/d43ebd042dd751842728e8cb91fa7fc1a82f26d0)
#### Monday 2023-03-27 15:35:36 by san7890

Log Active Turfs To Mapping Log (#74267)

## About The Pull Request

Was reminded of doing this via
https://github.com/tgstation/tgstation/issues/74245#issuecomment-1483943979

They're mapping issues, so let's log them to the mapping log. Quite
shrimple honestly.


![image](https://user-images.githubusercontent.com/34697715/227805458-5e6bcf01-629d-4b81-ab6a-b26e63d41ca3.png)
## Why It's Good For The Game

As the comments expound, the reason why we probably haven't done this in
the past is because any number of things can cause active turfs (like
ruin placement (either in icebox or in space)), or other silly stuff
like that. Thus, finding stuff like this would only really be viable
with stuff like the View Active Turfs verb, where you could visually
jump to and see all of the active turfs in that dynamic configuration
(and this still remains the best way to find active turfs).

This PR just makes it easier to do a "post-mortem" analysis on potential
active turfs, so that if it's very blatant, it can be fixed a lot
easier. It's best to try and find them during an ongoing round, but this
is life. (same as the unit tests concession, not too enthused on that
but we would have spontaneous errors out the ass without _something_)
## Changelog
Nothing that concerns players.

---------

Co-authored-by: tattle <66640614+dragomagol@users.noreply.github.com>

---
## [Rex9001/Rex-station-](https://github.com/Rex9001/Rex-station-)@[e75a1c00aa...](https://github.com/Rex9001/Rex-station-/commit/e75a1c00aa3bcf2658428a536997f2eca0f25028)
#### Monday 2023-03-27 15:35:36 by san7890

Dogs will no longer harrass if they are buckled to a bed (comfy edition) (#74224)

## About The Pull Request

Before, dogs were somehow magically able to drag their bed to you while
barking at/chasing you. that's silly, let's fix it by checking if you're
buckled, and then aborting course if we're comfy on our little bed
## Why It's Good For The Game


![image](https://user-images.githubusercontent.com/34697715/227679914-62822f93-6646-4070-8ff7-4e140e1a291a.png)

Fixes #74082

the dog is BUCKLED. it can't move. probably a better fix to this somehow
on a very deep AI level but that wouldn't allow us to have such a
soulful message (as well as potentially rule out a myriad of edge
cases), so i'm proposing this one.
## Changelog
:cl:
fix: If you buckle a dog to a bed, it will no longer drag its bed as it
goes to bark at the mailman. It will instead be comfy and chilling, as
expected.
/:cl:

---
## [Pyrelight-EQEMU/Server](https://github.com/Pyrelight-EQEMU/Server)@[40ed5f23dd...](https://github.com/Pyrelight-EQEMU/Server/commit/40ed5f23dd51446af5143cea21cd911486c9328f)
#### Monday 2023-03-27 15:46:57 by catapultam-habeo

fix bank delete bug

finish cleaning up bank bag bug

lol kill me

sigh this is tiresome

fuck this

wtf is this

bah

bah

try this

bah

fuck this.

so angry

so tired ofthis shit

test

test?

---
## [nlamprian/ros2_documentation](https://github.com/nlamprian/ros2_documentation)@[1be681dc76...](https://github.com/nlamprian/ros2_documentation/commit/1be681dc76d573c3bc20e9b7f943e906af820a32)
#### Monday 2023-03-27 15:55:25 by Chris Lalancette

First pass at the Iron Irwini release notes. (#3395)

* First pass at the Iron Irwini release notes.

That is, add in the full changelog, and also greatly
expand the release notes themselves.

I should point out that the full changelog is necessarily
*not* complete; it only contains information on things that
have already been released.

The release note page is a cut-down version of the full
changelog that just has things that might be interesting
to end users.  What is currently in there was my opinion,
so this list may be expanded or reduced based on thoughts
from other people.

In both cases, we should be able to iteratively add new
items here as they are landed.

Signed-off-by: Chris Lalancette <clalancette@gmail.com>
Co-authored-by: G.A. vd. Hoorn <g.a.vanderhoorn@tudelft.nl>

---
## [Pyrelight-EQEMU/Server](https://github.com/Pyrelight-EQEMU/Server)@[26ec620520...](https://github.com/Pyrelight-EQEMU/Server/commit/26ec62052070c985b666dc8a78fbe675d775e448)
#### Monday 2023-03-27 16:08:48 by catapultam-habeo

This should enable 100-slot bags

255 slots makes some weird shit happen. 200 is good.

max bag size?

lets try 200

clean up shared bank stupid shit

clean up no-drop hack detection

derp

this should enable 100-slot bags

1000 slot merchants?

---
## [Pyrelight-EQEMU/Server](https://github.com/Pyrelight-EQEMU/Server)@[c174ba3368...](https://github.com/Pyrelight-EQEMU/Server/commit/c174ba3368b29868da0d2bbcc70848cac31d35b1)
#### Monday 2023-03-27 16:12:17 by catapultam-habeo

block sending\enable AAs for mobs\nonclients

allow loading all aa regardless of class

add level requirement to activate abilities

test this method

wtf will this do

better UX

add class check to purchase

revert

derp

test limitiing visible levels

test

inverted

der

this?!

hammer

test

test

derp

thx ailia

lol does this work

this?

test

derp

derp

test

test

logging

rederpening

clean up a stupid

try to prevent out of level spells from hitting gems

syntax derp

hijack existing permaclass logic

restore kick

r

test

nvm

holy shit I'm dumb

test

derp

remove activeclass command

????

try this

is this right?

lets try this

wow.

I'm tired

different method for multiclass

Revert "let's give level a try"

This reverts commit 96ab5273f89194951dae4ec79d97dca7f5adca3d.

derps

derp

let's give level a try

disciplines

not sure what all I did here

maybe a bitmask?

lol um ok

holy shit did I really do that

try to fix scribespells

spellbook

maybe this is getting cleaned up somewhere?

maybe type issue?

tracing bug

requires db changes. class-specific spell gems.

derps

---
## [abishekvashok/pyre-check](https://github.com/abishekvashok/pyre-check)@[f3354a9fbc...](https://github.com/abishekvashok/pyre-check/commit/f3354a9fbc84f8521180c5948e53bc1b05a1fc2e)
#### Monday 2023-03-27 16:32:01 by Steven Troxler

Avoid using an alias for AsyncContextManager

Summary:
For unknown reasons, Pyre is unhappy with the current implementation
of `typing.pyi`, which uses a generic type alias to `AbstractAsyncContextManager`
for `AsyncContextManager`.

Debugging this could be difficult - Pyre doesn't really provide us with any clue
about why a type is invalid, so we'll probably need to spend time doing a deep
dive: I filed T146882109 to investigate this in more detail but in my opinion we
really need to prioritize bumping typeshed

(Justification for why a patch and bump is better than filing a task
and claiming that it blocks typeshed upgrade:
- having a bunch of patches to maintain is tech debt, but it is very explicit;
  we can look at the patches and see exactly how many fixes are needed. And
  updating the patches, while annoying, is pretty easy (maybe 2-5 minutes per patch
  per update).
- sitting on an old typeshed, on the other hand, involves exactly the same bugs
  except they are accumulating invisibly, plus users aren't getting the benefit of new
  typeshed features; we've now been explicitly asked to bump at least twice

**How the vendored part of this diff was created**

```
# iterate on this until new patch applies cleanly
rm -rf ~/patched_typeshed
buck2 run //tools/pyre/scripts:download_typeshed -- -p ~/fbsource/fbcode/tools/pyre/scripts/typeshed-patches -o ~/patched_typeshed -u https://api.github.com/repos/python/typeshed/zipball/8aedbda4cdff81478b7414e46c400ad016342e02

# once patches look good, update the vendored code
rm -rf ~/fbsource/fbcode/tools/pyre/stubs/typeshed/typeshed
cp -R ~/patched_typeshed/typeshed ~/fbsource/fbcode/tools/pyre/stubs/typeshed/typeshed
```

(note that the `-u` flag is pinning to the URL discovered in the very first run when creating D43666059 - you want to omit it when starting a typeshed bump, but then pin it after that so that new commits to typeshed don't break all your patches).

Reviewed By: grievejia

Differential Revision: D43680647

fbshipit-source-id: 18e2d04b9b545f9e1a844b4eddad68066ee1f9a8

---
## [Aidyn-A/pytorch](https://github.com/Aidyn-A/pytorch)@[a269469982...](https://github.com/Aidyn-A/pytorch/commit/a2694699821be04e6a74760ba754911e714a5486)
#### Monday 2023-03-27 16:36:47 by Brian Hirsh

aot autograd refactor: make all synthetic base logic layered in a single location (#96235)

This  refactor doesn't significantly change LoC in aot autograd, but I think this nets out to making it clearer (interested in peoples' thoughts).

The idea is that I tried to re-write the part of aot autograd that deals with synthetic bases in a layered way, similar to how Ed wrote the logic for dedup'ing inputs: it happens in one place, and all of the downstream transformation in aot autograd don't have to worry about it.

Specifically, I added a new function `aot_wrapper_synthetic_base`, similar to the existing `aot_wrapper_dedupe`.

The benefit: none of the other code in aot autograd needs to think about synthetic bases (previously, synthetic base code was intertwined in several places).

The downsides: there are two.

(1) `aot_wrapper_synthetic_base()` needs to have its own epilogue. There is one particularly hairy case, where factoring the synthetic base logic to a single location was painful: If you have two inputs that alias each other, where one gets a data mutation, and the other gets a metadata mutation.

Ordinarily, metadata mutations are handled by the runtime epilogue, in `create_runtime_wrapper`. However, now that things are factored this way, the runtime wrapper operates only on synthetic bases instead of operating on the original inputs. For data mutations, it is fine to apply the data mutation to the synthetic base instead of the original input alias. But for metadata mutations, we **need** to apply the metadata mutation directly to the original inputs.

The way that I handled this was by tracking which inputs slot into this specific case (part of a synthetic base, and get metadata mutations), and updateing the flat_fn() that we pass downstream to return these updated inputs as extra outputs. From the perspective of downstream logic, these are real user outputs, that it can treat like any other user outputs. `aot_wrapper_synthetic_base` will know to grab these extra outputs and use them to apply the metadata mutations.

This was pretty annoying, but has the benefit that all of that logic is encapsulated entirely in `aot_wrapper_synthetic_base()`.

(2) input mutations are now performed on the synthetic base instead of the individual aliases.

You can see the original code comment [here](https://github.com/pytorch/pytorch/blob/b0b5f3c6c681896febbd9ff7ad7649b13def345d/torch/_functorch/aot_autograd.py#L1131) for details. We used to do the optimized thing in this case, and now we do the less optimized thing (copying the entire synthetic base, instead of the potentially smaller alias).

To be fair, we had no data showing that this optimization was showing improvements on any models in practice. I also think that the main reason anyone would ever run across this problem is because of a graph break - so if you care about perf, you probably want to avoid the extra graph breaks to begin with. I haven't added any warnings for this, but we probably could depending on what people think.

Pull Request resolved: https://github.com/pytorch/pytorch/pull/96235
Approved by: https://github.com/ezyang

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[e83d3e0adb...](https://github.com/shiptest-ss13/Shiptest/commit/e83d3e0adb6493f028dbfbff9facbe64eaa7a3c5)
#### Monday 2023-03-27 16:46:04 by Sun-Soaked

Botany Balance Pass (#1783)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
First came the content, now comes the hammer.

- Nukes Megaseed servitors from orbit. 
- Plants now age much, much slower and produce half as quickly.
Ruins that had them now have a ruined seed vendor that can be salvaged
for random seeds(and danger).
Ships that had one now have a crate with some thematic starting seeds,
and a Strange Seed.
Ghostrole Ruins that relied on having all seeds locally now have a
special biogenerator variant that can print a random seed for biomass.

- Adds Genesis Serum. This can be splashed on a tile to make natural
grass and some flora. Green your ship!
Genesis Serum was made a while ago, on request for a way to add natural
grass and flora to your ship. Since I had it lying around fully coded, I
thought I might as well pr it with botany changes.

- Gatfruit found in the seed vault have been replaced with Strange
Seeds.

- The chance to get Gatfruit from a demonic portal(plant variety) has
dropped from 15% to 5%.

- Corpse flowers now have liquid gibs and formaldehyde again. 

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Okay, hear me out

With this and Gardens, botany ships go from a "sit in your vessel for 2
hours" experience to an "explore and forage" one that better fits our
feature arc. It goes without saying that this **shouldn't be merged till
Overmap 4.2 is**, since it facilitates getting seeds from planets as
part of exploration.

Gatfruit are funny, but it takes exactly one seed getting into the hands
of a ship with a dna manipulator and the weapon balance is eradicated
from the game completely(for the round, at least.)
This is more problematic here then it was on TG, since our rounds tend
to be 5 hours long rather then 1.
This has been long coming. I'll reverse this if we ever get that
Plantlock variant we wanted a while ago.

Corpse flowers even have formaldehyde and gibs on tg, not sure what
happened there.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: 
add: Ruined megaseed servitors can now be found on the frontier,
carrying a bounty of seeds for intrepid adventurers.
balance: the time it takes for plants to reach a lethal age has been
increased massively.
balance: Plant production time increased a bit to compensate.
balance: megaseed servitors have been removed from ships and ruins.
Ships that carried one now have a crate with some starting seeds.
balance: removes gatfruit from the seed vault pool.
balance: reduces the chance of getting gatfruit from a plant-themed
demonic portal significantly.
balance: corpse flowers once again have formaldehyde and liquid gibs.
add: Adds Genesis Serum, a reagent that transforms tiles into natural
grass on splash, then causes some natural flora objects to grow. Turn
your ship green!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [blackcrystall/ms-13-prs-fork](https://github.com/blackcrystall/ms-13-prs-fork)@[b2f0f35f3a...](https://github.com/blackcrystall/ms-13-prs-fork/commit/b2f0f35f3afe1905cfefcf9e682de51cff2d4499)
#### Monday 2023-03-27 17:19:30 by EdwardNashton

Speed, Money and Faith: Updating an areas of Town. (#2286)

* Update TGS DMAPI

* Speed, Money and Faith: Updating an areas of Town.

Added a Church with a graveyard area (that currently empty because we have no tombs).

Remade one quarter into 4 different shops: Liquor, Pharmacy, Gun Shop, General Store.

Remade old shitty Library into Biker's Club.

Remade a Dime's Radio Station (by his permission)

Fixed a small area issue on a top z-level of Car Jankyard.

* Fixes up a bunch of stuff :)

* additional minority fixes

---------

Co-authored-by: tgstation-server <tgstation-server@users.noreply.github.com>
Co-authored-by: Edward Nashton <eddienigma48@gmail.com>
Co-authored-by: Professor Popoff <omniderpectional@gmail.com>

---
## [openai/evals](https://github.com/openai/evals)@[733167aed6...](https://github.com/openai/evals/commit/733167aed6624945acdc51ec11407484dd2d931b)
#### Monday 2023-03-27 17:29:54 by Andrew

Taxes Eval (#454)

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
Taxes Eval

### Eval description

Tests the model's ability to evaluate tax liability for generic examples
from common cities including NYC, SF, and Seattle. The eval also tests
ordering of multiple choice options, with the model outputting different
results if the multiple choice labels are switched around.

### What makes this a useful eval?

Taxes are a relatively logically straightforward task, yet there is a
high degree of complexity to the legal and tax system, which makes
calculations difficult to estimate.

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
{"input": [{"role": "system", "content": "Instructions: You will be
presented with a tax calculation and four options A through D. Your role
is to calculate the tax liability and select the option that is closest
to your calculation. For each question you must select one of the
following answers: 'A', 'B', 'C', 'D'. Do not explain. Do not include
the number in your response."}, {"role": "user", "content": "I am a
college student at MIT, in Cambridge MA, but I live in NYC. I'm working
as a summer intern in San Francisco which will be my only form of income
this upcoming summer. Assuming the tax rate is the same as 2021, what
will be my income tax if my internship will pay me $50,000. A. 6,383 B.
8,393 C. 9,882 D. 48,001. For each question you must select one of the
following answers: 'A', 'B', 'C', 'D'."}], "ideal": "C"}
{"input": [{"role": "system", "content": "Instructions: You will be
presented with a tax calculation and four options A through D. Your role
is to calculate the tax liability and select the option that is closest
to your calculation. For each question you must select one of the
following answers: 'A', 'B', 'C', 'D'. Do not explain. Do not include
the number in your response."}, {"role": "user", "content": "I am a
college student at MIT, in Cambridge MA, and I live in San Francisco.
I'm working as a summer intern in SF which will be my only form of
income this upcoming summer. Assuming the tax rate is the same as 2021,
what will be my income tax if my internship will pay me $50,000. A.
6,383 B. 8,393 C. 9,882 D. 48,001. Respond with only the letter of the
answer choice."}], "ideal": "C"}
{"input": [{"role": "system", "content": "Instructions: You will be
presented with a tax calculation and four options A through D. Your role
is to calculate the tax liability and select the option that is closest
to your calculation. For each question you must select one of the
following answers: 'A', 'B', 'C', 'D'. Do not explain. Do not include
the number in your response."}, {"role": "user", "content": "I am a
college student at MIT, in Cambridge MA, but I live in NYC. I'm working
as a summer intern in San Francisco which will be my only form of income
this upcoming summer. Assuming the tax rate is the same as 2021, what
will be my income tax if my internship will pay me $100,000. B. 24,383
C. 26,393 D. 28,882 A. 38,001. For each question you must select one of
the following answers: 'A', 'B', 'C', 'D'."}], "ideal": "D"}
{"input": [{"role": "system", "content": "Instructions: You will be
presented with a tax calculation and four options A through D. Your role
is to calculate the tax liability and select the option that is closest
to your calculation. For each question you must select one of the
following answers: 'A', 'B', 'C', 'D'. Do not explain. Do not include
the number in your response."}, {"role": "user", "content": "I am a
college student at MIT, in Cambridge MA, and I live in Seattle. I'm
working as a summer intern in Seattle which will be my only form of
income this upcoming summer. Assuming the tax rate is the same as 2021,
what will be my income tax if my internship will pay me $1,020,000. C.
263,352 A. 365,303 B. 829,282 D. 1,085,401. Respond with only the letter
of the answer choice."}], "ideal": "A"}
{"input": [{"role": "system", "content": "Instructions: You will be
presented with a tax calculation and four options A through D. Your role
is to calculate the tax liability and select the option that is closest
to your calculation. For each question you must select one of the
following answers: 'A', 'B', 'C', 'D'. Do not explain. Do not include
the number in your response."}, {"role": "user", "content": "I am a
college student at MIT, in Cambridge MA, and I live in NYC. I'm working
as a summer intern in NYC which will be my only form of income this
upcoming summer. Assuming the tax rate is the same as 2021, what will be
my income tax if my internship will pay me $320,000. A. 63,382 B. 95,303
C. 129,282 D. 185,401. Respond with only the letter of the answer
choice."}], "ideal": "B"}
  ```
</details>

---
## [sqnztb/Skyrat-tg](https://github.com/sqnztb/Skyrat-tg)@[44ffcdfcc7...](https://github.com/sqnztb/Skyrat-tg/commit/44ffcdfcc7e628b06618f25e34bd14fea8e164a2)
#### Monday 2023-03-27 17:32:42 by SkyratBot

[MIRROR] Kidnapping won't destroy implants, nodrop items [MDB IGNORE] (#19994)

* Kidnapping won't destroy implants, nodrop items (#74118)

## About The Pull Request

Fixes #73985
Kidnapping was looping through mob contents to find items to remove from
you, rather than equipped items. It was then forcemoving them out of
you, destroying the functionality of implants and nodrop items.

Being kidnapped will now only remove equipped items from you (not
everything inside you) and will not forcemove nodrop items out of your
inventory (so it won't confiscate your chaplain armblade).
Additionally, anything you picked up in the kidnapping area was being
sent to nullspace on exit, I changed this to have them drop on the
ground instead.

However, due to this long-standing convention we now have an expectation
that items are not trivially moved in or our of the kidnapping area, so
it also loops through any storage implants you may have and dumps their
contents too.
There are still ways around this (cavity implantation, for instance) but
they seem uncommon and restrictive enough that they're probably not a
big deal.

## Why It's Good For The Game

Kidnapping another traitor destroying their implants was an annoying and
unpleasant experience (especially if it was their uplink implant), and
does not seem to have been intended.
Also removes weird behaviour where your arm blade might fall off because
you got kidnapped.

## Changelog

:cl:
fix: Implants and items which you cannot drop will no longer be forced
out of your character when you are kidnapped.
fix: Objects you try to take back from the kidnapping location as
souvenirs will drop to the ground when you leave instead of being
destroyed, except shirts and shoes (make sure to pick up your
monographed synidcate T-shirt).
/:cl:

* Kidnapping won't destroy implants, nodrop items

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [GalixMix/Vs-Vaasasns-Icy-Week](https://github.com/GalixMix/Vs-Vaasasns-Icy-Week)@[690c29aaed...](https://github.com/GalixMix/Vs-Vaasasns-Icy-Week/commit/690c29aaed1d4a2ff377a75b885c66eeccc476ee)
#### Monday 2023-03-27 17:39:58 by Galix The Musician

Vs Vaasans Soundfonts

and yes there official, so go fuck yourselfs with them

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[40fc11eb07...](https://github.com/tgstation/tgstation/commit/40fc11eb0733ca25eff56e7379cb574a997fb6d3)
#### Monday 2023-03-27 18:24:52 by LemonInTheDark

Optimizes some gas_mixture procs, Optimizes pipeline processing significantly by 33% (#74233)

## About The Pull Request
It is faster to operate on a gas list, especially if cached, then it is
to operate on a datum.
Doing this cause I'm seeing cost in merge() post #74230

Hits on a few other important places too. self_breakdown and such. Worth
it IMO

Could in theory go further by caching the global list. I'm tempted I
admit but it needs profiling first and it's late

EDIT: I have not slept, and have gone tooo far

[Micros /gas_mixture/copy and copy_from, adds a new proc to handle
copying with a ratio,
copy_from_ratio](https://github.com/tgstation/tgstation/pull/74233/commits/91da0003daa9485962525d3e6bc9170a4c09876b)

[91da000](https://github.com/tgstation/tgstation/pull/74233/commits/91da0003daa9485962525d3e6bc9170a4c09876b)

The ADD_GAS sidestep saves us 0.1 seconds of init (used to at least.
Ensuring we don't break archive is gonna have a cost. I don't want to
profile this so I'll estimate maybe 0.05 seconds). The faster version of
copy_from is just well, better, and helps to avoid stupid

[Optimizes pipeline
processing](https://github.com/tgstation/tgstation/pull/74233/commits/bf5a2d2d60554da2ce5fa1ac5f6c4179f6208cb2)

[bf5a2d2](https://github.com/tgstation/tgstation/pull/74233/commits/bf5a2d2d60554da2ce5fa1ac5f6c4179f6208cb2)

I haven't slept in 36 hours. Have some atmos optimizations

Pipelines now keep track of components that require custom
reconciliation as a seperate list.
This avoids the overhead of filtering all connected atmos machinery.

Rather then relying on |= to avoid duplicate gas_mixtures, we instead
use a cycle var stored on the mix itself, which is compared with a
static unique id from reconcile_air()
This fully prevents double processing of gas, and should (hopefully)
prevent stupid dupe issues in future

Rather then summing volume on the gas mixture itself, we sum it in a
local var.
This avoids datum var accesses, and saves a slight bit of time

Instead of running THERMAL_ENERGY() (and thus heat_capacity(), which
iterates all gases in the mix AGAIN) when processing gas, we instead
just hook into the existing heat capacity calculation done inside the
giver gases loop
This saves a significant amount of time, somewhere around 30% of the
proc, I think?

This doesn't tackle the big headache here, which is the copy_from loop
at the base of the proc.

I think the solution is to convert pipelines to a sort of polling model.
Atmos components don't "own" their mix, they instead have to request a
copy of it from the pipeline datum.
This would work based off a mutually agreed upon volume amount for that
component in that process cycle.

We'd use an archived system to figure out what gases to give to
components, while removing from the real MOLES list.

We could then push gas consumption requests to the pipeline, which would
handle them, alongside volume changes, on the next process.

Not sure how I'd handle connected pipelines... Merging post reconcile
maybe?
This is a problem for tomorrow though, I need to go to bed.

Saves about 30% of pipeline costs.
Profiles taken on kilo, until each reconcile_air hits 5000 calls

[old.txt](https://github.com/tgstation/tgstation/files/11075118/Profile.results.total.time.txt)

[new.txt](https://github.com/tgstation/tgstation/files/11075133/profiler.txt)

---
## [gregorias/bookmarks.fish](https://github.com/gregorias/bookmarks.fish)@[b3bd337679...](https://github.com/gregorias/bookmarks.fish/commit/b3bd337679cb13d6c56e1ede94b810b18a5e60f6)
#### Monday 2023-03-27 18:42:25 by Grzegorz Milka

fix: ban newlines

Hear ye, hear ye! Gather 'round, my fellow believers, for I have a tale
to tell that shall send chills down your spine. A tale of darkness and
evil, of corruption and sin. A tale about the danger that lurks within
the very tools we use to navigate the shell - bookmarks.

For too long have we taken bookmarks for granted, assuming them to be a
harmless and benign feature. But mark my words, my friends, for
bookmarks are nothing but a gateway to the abyss, a portal through which
malevolent spirits may enter our computers and corrupt our very souls.

And what, you may ask, is the source of this evil? Newlines. Yes,
newlines! Those seemingly innocuous little characters that we use to
separate lines of text. They may seem harmless, but in truth, they are
the very root of all evil when it comes to bookmarks.

For you see, my friends, newlines can allow the forces of darkness to
slip through the cracks in our digital defenses. They can allow demons
and devils to enter our computers and wreak havoc upon our data,
corrupting our files and stealing our passwords.

So I say to you, my fellow believers, we must banish newlines from our
bookmarks forevermore! We must cast them out, purge them, and seal the
gateways to the abyss once and for all.

Do not be fooled by the seeming simplicity of this task, for it is a
task that requires great diligence and vigilance. We must remain ever
vigilant, always on the lookout for newlines that may sneak their way
into our bookmarks, for even a single newline can be enough to open the
gates of hell and unleash untold horrors upon our digital lives.

So let us stand together, my friends, and pledge to rid our bookmarks of
newlines. Let us banish the forces of darkness from our digital world,
and keep our computers safe from the clutches of evil. Hear ye, hear ye,
let it be known throughout the land - newlines in bookmarks are hereby
banned!

---
## [TheRealJake12/Kade-Engine-Community](https://github.com/TheRealJake12/Kade-Engine-Community)@[27581bc6e0...](https://github.com/TheRealJake12/Kade-Engine-Community/commit/27581bc6e0d6963f2a8b44f43915d64a547b48b5)
#### Monday 2023-03-27 18:48:39 by TheRealJake_12

fuck you laggy input. I genuinely dont know anymore

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[2e5bfe5be6...](https://github.com/lessthnthree/tgstation/commit/2e5bfe5be669d5222b68c7318349c4ac0947722b)
#### Monday 2023-03-27 18:53:04 by LemonInTheDark

Refactors and optimizes breath code (Saves 12% of carbon/Life()) (#74230)

## About The Pull Request

### How things work

As things currently stand, when a mob breaths several things happen
(simplified to focus on the stupid)

We assert the existance of all possible breathable gases, and pull
partial pressures for them
Then we walk through all possible interactions lungs could have with
these gases, one by one, and see if they're happening or not
As we go we are forced to cleanup potential alerts caused by the
previous breath, even if those effects never actually happen
At the end we clear out all the unused gas ids, and handle the
temperature of the breath.

### What sucks

There's I'd say 3 different types of gas reactions.

- You can "need" a gas to survive. o2, n2 and plasma all fall into this
category
- A gas can do something to you while it's in your system. This applies
to most gas types
- Variation on the previous, some gases do cleanup when they're not in
your system, or when there isn't much of them in the first place

The main headache here is that second one, constantly cleaning up
potential side effects sucks, and fixing it would require a lot of dummy
variables

There's other suckage too.

Needing to constantly check for a gas type even if it isn't there is
stupid, and leads to wasted time It's also really annoying to do
subtypes in this system.
There is what amounts to a hook proc you can override, but you can't
override the reaction to a gas type.
It also just like, sucks to add new gases. one mega proc smells real
stupid.

### Improvements

In the interest of speed:

- I'd like to build a system that doesn't require manually checking for
gas
- Reacting to gas "disappearing" should be promoted by the system,
instead of being hacky.
- I would like to avoid needing to assert the existence of all possible
gases, as this is slow on both the assert and the garbage collect.

In the interest of dev ergonomics:

- It should be easy to define a new gas reaction 
- It should be easy for subtypes to implement their own gas reactions.
The current method of vars on the lung is all tangled up and not really
undoable as of now, but I'd like to not require it
- It should be possible to fully override how a gas is handled

### What I've Done

Lungs have 3 lists of proc paths stored on them

Each list handles a different way the lung might want to interact with a
gas.
There's a list for always processing on a gas (we use this for stuff
that's breathed), a list for handling a gas in our breath, and a list
for reacting to a gas previously being in our breath, but not any more.

Lungs fill out these lists using a helper proc during Initialize()
Then, when it comes time to breath, we loop over the gas in the breath
and react to it.
We also keep track of the previous list of partial pressures, which we
calculate for free here, and use that to figure out when to call the
loss reactions.

This proc pattern allows for overrides, easy reactions to removals,
lower indentation code and early returns, and better organization of
signal handlers

It's also significantly faster. Ballpark 4x faster

### Misc

Removes support for breathing co2, and dying from n2 poisoning. 
They were both unused, and I think it's cringe to clutter these procs
even further

Added "do we even have oxyloss" checks to most cases of passive
breathing.
This is a significant save, since redundant adjustoxy's are decently
expensive at the volume of calls we have here.

Fixes a bug with breathing out if no gas is passed in, assigning a var
to another var doesn't perform a copy

Rewrote breathe_gas_volume() slightly to insert gas into an immutable
mix stored on the lung, rather then one passed in
This avoids passing of a gas_mixture around just to fill a hole. 

I may change my mind on this, since it would be nice to have support for
temperature changing from a hot/cold breath.
Not gonna be done off bodytemp tho lord no.

Uses merge() instead of a hard coded version to move the gas ids over. 
This is slightly slower with lower gas counts but supports more things
in future and is also just easier to read.

## Why It's Good For The Game

Faster, easier to work with and read (imo)

Profiles: 

[breath_results_old.txt](https://github.com/tgstation/tgstation/files/11068247/breath_results_old.txt)

[breath_results_pre_master.txt](https://github.com/tgstation/tgstation/files/11068248/breath_results_new.txt)

[breath_results_new.txt](https://github.com/tgstation/tgstation/files/11068349/breath_results_new.txt)

(These profiles were initially missing #73026. Merging this brings the
savings from 16% to 12%. Life is pain)

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [ARF-SS13/coyote-bayou](https://github.com/ARF-SS13/coyote-bayou)@[760cdde415...](https://github.com/ARF-SS13/coyote-bayou/commit/760cdde41530afc3feaabe82aad7cc5761563bc3)
#### Monday 2023-03-27 19:19:40 by Tk420634

Merge pull request #1785 from GremlingSS/fix-trees

Fucking fixes the god awful trees

---
## [xNaCly/gleichzeitig](https://github.com/xNaCly/gleichzeitig)@[28a997aa53...](https://github.com/xNaCly/gleichzeitig/commit/28a997aa5370087a505ea3542d619c13ff04e127)
#### Monday 2023-03-27 19:29:14 by xnacly

fix: tried to fix output and waiting

not a fucking thing works, i really dont know why the fuck go cant wait for a command to finish even after i call cmd.Wait(), also why the fuck does it wait if is set the streams to the os streams (cmd.Stderr = os.Stderr) but also only for the python webserver im using not my own printing and waiting loop it is so fucking annoying im really thinking of just giving up and starting each fucking shitty process in its own fucking terminal window and just have my workspace full of fucking shit, fuck this - stop programming lets just do some wood working

---
## [FuzzyFuzlet/fuzzys-repository](https://github.com/FuzzyFuzlet/fuzzys-repository)@[aaa23be87d...](https://github.com/FuzzyFuzlet/fuzzys-repository/commit/aaa23be87dd116c43f24b2c0b35e0ad0e09dd7e7)
#### Monday 2023-03-27 19:57:33 by Superlagg

Merge pull request #1776 from ARF-SS13/fuck-you-ghd

Trash Stack Desc fix

---
## [Mjoonlight/MythosOfMoonlight](https://github.com/Mjoonlight/MythosOfMoonlight)@[85ca2a01fe...](https://github.com/Mjoonlight/MythosOfMoonlight/commit/85ca2a01fec48341f8bb375f6641d66f92d78378)
#### Monday 2023-03-27 20:23:55 by Ebon1

guys this is so me after i finish a worldgen structure after hours of pain and misery i hate world gen

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[dccd44eab5...](https://github.com/git-for-windows/git/commit/dccd44eab5e29d3ba2d6b8ae375de2488ad58af1)
#### Monday 2023-03-27 20:38:45 by Johannes Schindelin

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
## [ZzAve/teambalance](https://github.com/ZzAve/teambalance)@[be41a19967...](https://github.com/ZzAve/teambalance/commit/be41a199672f42698acd0e60d1d135ce589d480b)
#### Monday 2023-03-27 20:42:28 by Julius van Dis

Upgrade to MUI 5 (#227)

* clean covid-19

* Add themeprovider to app

* Add MUI 5 dependencies

- included @mui/x-date-pickers (as replacement for @material-ui/pickers)
- included emotion for typesafe css

* Remove MUI 4 dependencies, and fix breaking component changes

Follows: https://mui.com/material-ui/migration/v5-component-changes/

Noteworthy:
- Fixes in createStyles and withStyles
- Deprecated `<Hidden>` component (mostly move to:
 ```<Typography variant={"button"} sx={{ display: { sm: "block", xs: "none" } }}>
  Terug naar de veiligheid</Typography>```
- App is wrapped in <StyledEngineProvider injectFirst> to support JSS (prepare for migration to emotion
- Shit ton of renames from @material-ui/* to @mui/*
- Verwijderen van AttendeeStyledButton, en fallback op normale Button. 'uncertain' is mapped naar 'warning', en die kleur is aangepast in de palette van de theme.

* Apply webpack optimisations to reduce build times (dev: 30s to 10s, prod 60s to 10s)

* Replace JSS with emotion

* Remove @mui/styles

* Upgrade notistack to v2

* Pin dependencies

* Fix latest mui things

---
## [Helg2/tgstation](https://github.com/Helg2/tgstation)@[a6f49ed542...](https://github.com/Helg2/tgstation/commit/a6f49ed54255f9a8d4dfc27bc397e56f87029cb8)
#### Monday 2023-03-27 21:05:09 by san7890

Refactors Suiciding Variable Into Trait (#74150)

## About The Pull Request

Firstly, this var was on `/mob`, even though only `/mob/living` and
`/mob/dead` could have ever used it, so who knows how much needless
memory it was consuming on stuff such as `oranges_ear` that would never
ever ever use something like this.

Edit: okay instead of memory it just polluted variable edit windows for
all /mob when it didn't need to. I like having a slim VV window

Secondly, it's a technical improvement over the previous system as we
are able to "track" where a suicide originates from, and how we can
track that from mob-to-mob-to-mob. Previously, the boolean `suiciding`
would only inform us if they had ever been connected to a mob that had
ever committed suicide, but now we are able to precisely determine which
mob gave them the trait that they must now apparently bear until the
round restarts.

## Why It's Good For The Game

Less memory usage, more indepth ability to track suicides in case you
really need that dexterity. Currently no implemented code could benefit
from using it, but it would be pretty neat if someone could figure out a
way to have someone be guilt-tripped whenever they look into a mirror
and seeing the reflection of their past life? This PR won't actually
help you code that and it'll probably require a bit more work, but it's
a possibility of some cool interactions you can do when you have this
information available to you.


![image](https://user-images.githubusercontent.com/34697715/226506321-550c37e7-5de8-4f9f-9ceb-4bf9b1052597.png)

## Changelog

:cl:
refactor: Some aspects of how we track suicides from your living mob to
your observer have changed- please do let us know if anything has broken
via a GitHub Issue Report.
/:cl:

There's probably some technical improvements that can be made in some
parts of the code I reworked to accommodate this change, do let me know
if you spot any easy ones (or fuckups). a lot of excess comes from the
fact that any step in the TRAIT framework trusts that you are passing in
a valid datum (or subtype) so that's a thing

---
## [LeoTKBR/canary](https://github.com/LeoTKBR/canary)@[8314f6a3e8...](https://github.com/LeoTKBR/canary/commit/8314f6a3e8c3b94242d43d4f754a6fb4fccf6461)
#### Monday 2023-03-27 21:31:52 by Spiller

feat: add several missing bosses (#708)

• See the pull request description to read detailed information.

Add bosses from some quests there were not developed. This PR adds only the bosses, levers mechanics for simple functionality.
This doesn't add the bosses mechanics! If someone is willing to contribute with the mechanics, feel free to contribute with the PR.
The bosses added are:

• A pirate's tail: Ratmiral Blackwhiskers, Tentugly's head;
• Adventures of Galthen: Megasylvan Yselda;
• Feaster of Souls: The Fear Feaster, The Unwelcome, The Dread Maiden, Irgix the Flimsy, Unaz the Mean, Vok The Freakish;
• Grave Danger (rework): Lord Azaram, Duke Krule, Count Vlarkorth, Sir Nictros & Sir Baeloc, Earl Osam, King Zelos;
• Grimvale/Ancient Feud: Katex Blood Tongue, Srezz Yellow Eyes, Utua Stone Sting, Yirkas Blue Scales, Bloodback, Darkfang, Sharpclaw, Shadowpelt, Black Vixen;
• Soul War: Goshnar's Cruelty, Goshnar's Greed, Goshnar's Hatred, Goshnar's Malice, Goshnar's Spite, Goshnar's Megalomania;
• The Dream Courts: The Nightmare Beast, Izcandar the Banished, Alptramun, Plagueroot, Malofur Mangrinder, Maxxenius;
• The Secret Library: Ghulosh, Gorzindel, Lokathmor, Mazzinor, Scourge of Oblivion.
• The SoulWar reward was added. In order to get the reward, the player needs to kill all the bosses and the final boss.
• The Dream Court's World change was added.

• All the access needed were granted on FreeQuests.lua. If you are already running a server, you'll need to update freeQuestStage on config.lua to one number higher than it is. So, all the players of your server will have the access granted.

---
## [SingularityXStudios/evals](https://github.com/SingularityXStudios/evals)@[34f83340a7...](https://github.com/SingularityXStudios/evals/commit/34f83340a75b7e26af35d8eaea165e54b38d7946)
#### Monday 2023-03-27 21:49:14 by kallyaleksiev

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
## [SingularityXStudios/evals](https://github.com/SingularityXStudios/evals)@[b170a21cf3...](https://github.com/SingularityXStudios/evals/commit/b170a21cf32c47d841f64ec110cfd6796ec3f89a)
#### Monday 2023-03-27 21:49:14 by Sam Ennis

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
## [SingularityXStudios/evals](https://github.com/SingularityXStudios/evals)@[4f090a04fe...](https://github.com/SingularityXStudios/evals/commit/4f090a04fe53a8d0f647bfdfc7ef177fa8034e2e)
#### Monday 2023-03-27 21:49:14 by Shawn Marincas

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
## [SingularityXStudios/evals](https://github.com/SingularityXStudios/evals)@[b5da073c21...](https://github.com/SingularityXStudios/evals/commit/b5da073c215c6453b99269a6dab2dca5454f04dd)
#### Monday 2023-03-27 21:49:14 by somerandomguyontheweb

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
## [xMcacutt/Mul-Ty-Player](https://github.com/xMcacutt/Mul-Ty-Player)@[02ea4f96b7...](https://github.com/xMcacutt/Mul-Ty-Player/commit/02ea4f96b739eed329d0672efe9df3a89640c240)
#### Monday 2023-03-27 22:32:58 by xMcacutt

FINALLY fixed the bulk of the client Ty crash issues. Exception handling is pain and suffering and I hate everything about this god forsaken language.

---
## [ratteler50/townsquare](https://github.com/ratteler50/townsquare)@[974bbb1a0f...](https://github.com/ratteler50/townsquare/commit/974bbb1a0f35ab2a3333ba2a28955956e24fd900)
#### Monday 2023-03-27 23:06:29 by Dae Lorant

Updated night order for all roles

Updated night order for all roles to match the order at https://script.bloodontheclocktower.com/data/nightsheet.json

Some noticeable changes:
- Legion was moved much earlier in the order of demons (relevant if a another demon is made in a legion game, you can keep it around and kill it with legion before it kills on a subsequent night)
- Amnesiac was moved much later in night order (a more reasonable place for the most common type of amni abilities)
- Magician was given a night order for N1
- Pixie was given a night order for other nights

---
## [flowercuco/blorbostation](https://github.com/flowercuco/blorbostation)@[77efa342b5...](https://github.com/flowercuco/blorbostation/commit/77efa342b5a52e0a72f6d371db24e04f17cd3a48)
#### Monday 2023-03-27 23:38:38 by flowercuco

beacon now capable of doing the thing it is supposed to do via fucked up evil radio shit

---

