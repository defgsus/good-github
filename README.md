## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-06-11](docs/good-messages/2023/2023-06-11.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,776,041 were push events containing 2,650,782 commit messages that amount to 159,854,339 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 63 messages:


## [0x845FED/libgdx](https://github.com/0x845FED/libgdx)@[e1d1fdc5fb...](https://github.com/0x845FED/libgdx/commit/e1d1fdc5fb5b8409dc74f638c633ead405e535f3)
#### Sunday 2023-06-11 00:07:38 by Tommy Ettinger

I18NMessageTest needs to reset I18NBundle static state. (#7101)

* Mark PauseableThread as excluded on GWT.

* Minor typo corrections.

* Fix atan2() when it should produce 0f.

Without this small change (which has essentially no performance impact that I could measure), calling atan2() with a point on the x-axis would produce a small but non-zero result, which is incorrect.

* Add atan, atan2, asin, acos for degrees.

This also includes atan2Deg360(), which in my opinion is the most useful of these because it does something differently from Math.atan2(), and can often save some effort.

* Approximations for tan() and tanDeg().

Sorry this is so long-winded, but the error isn't as straightforward to express as with sin() or cos().

* Apply formatter

* Add to MathUtilsTest.

* Apply formatter

* Stop trying to load defaults from wrong dir.

This old behavior broke Flame's effect-open dialog when any particle effect used the default billlboard or model particle. Now Flame tries to load a file given its absolute path (like before), but if it fails, it falls back to trying the default filenames as internal files.

* I18NMessageTest needs to reset I18NBundle state.

If you run I18NSimpleMessageTest and then I18NMessageTest without this PR, then the first test will have called I18NBundle.setSimpleFormatter(true), but the second test needs it to be set to false.

Because the tests are still perfectly usable if you run them on their own (or use LWJGL2, I think, because it might not share static state), this is not at all a priority to merge; it just makes running many tests in one session not throw an Exception.

---------

Co-authored-by: GitHub Action <action@github.com>

---
## [CartoonFan/higan](https://github.com/CartoonFan/higan)@[e6e19a7c89...](https://github.com/CartoonFan/higan/commit/e6e19a7c897574491e19a17edd33664ff4d49942)
#### Sunday 2023-06-11 00:29:26 by byuu

Update to bsnes v053 release.

This release greatly polishes the user interface, adds a new cheat code search utility, adds the snesfilter library, and adds Qt-based GUI support to both snesfilter and snesreader. snesfilter gains 2xSaI, Super 2xSaI and Super Eagle support, plus full configuration for both the NTSC and scanline filters; and snesreader gains support support for multi-file ROM archives (eg GoodMerge sets.)
Statically linking Qt to bsnes, snesfilter and snesreader would be too prohibitive size-wise (~10MB or so.) I have to link dynamically so that all three can share the same Qt runtime, which gets all of bsnes and its modules to ~1MB (including the debugger build); and Qt itself to about ~2.5MB.
However, there is some bad news. There's a serious bug in MinGW 4.4+, where it is not generating profile-guided input files (*.gcno files.) There is also a serious bug in Qt 4.5.2/Windows when using dynamic linking: the library is hanging indefinitely, forcing me to manually terminate the process upon exit. This prevents the creation of profile-guided output files (*.gcda files.) It would be tough enough to work around one, but facing both of these issues at once is too much.
I'm afraid I have no choice but to disable profile-guided optimizations until these issues can be addressed. I did not know about these bugs until trying to build the official v053 release, so it's too late to revert to an all-in-one binary now. And I'm simply not willing to stop releasing new builds because of bugs in third-party software. As soon as I can work around this, I'll post a new optimized binary. In the mean time, despite the fact that this release is actually more optimized, please understand that the Windows binary will run approximately ~10% slower than previous releases. I recommend keeping v052 for now if you need the performance. Linux and OS X users are unaffected.
Changelog:
    - save RAM is initialized to 0xff again to work around Ken Griffey Jr Baseball issue
    - libco adds assembly-optimized targets for Win64 and PPC-ELF [the latter courtesy of Kernigh]
    - libco/x86 and libco/amd64 use pre-assembled blocks now, obviates need for custom compilation flags
    - added a new cheat code search utility to the tools menu
    - separated filters from main bsnes binary to libsnesfilter / snesfilter.dll
    - added 2xSaI, Super 2xSaI and Super Eagle filters [kode54]
    - added full configuration settings for NTSC and scanline filters (12+ new options)
    - further optimized HQ2x filter [blargg]
    - added Vsync support to the Mac OS X OpenGL driver
    - added folder creation button to custom file load dialog
    - fixed a few oddities with loading of "game folders" (see older news for an explanation on what this is)
    - updated to blargg's file_extractor v1.0.0
    - added full support for multi-file archives (eg GoodMerge sets)
    - split multi-cart loading again (BS-X, Sufami Turbo, etc) as required for multi-file support
    - cleaned up handling of file placement detection for save files (.srm, .cht, etc)
    - file load dialog now remembers your previous folder path across runs even without a custom games folder assigned
    - windows now save their exact positioning and size across runs, they no longer forcibly center
    - menus now have radio button and check box icons where appropriate
    - debugger's hex editor now has a working scrollbar widget
    - added resize splitter to settings and tools windows
    - worked around Qt style sheet bug where subclassed widgets were not properly applying style properties

---
## [EvaEvaEvaEvaEva/CEV-Eris](https://github.com/EvaEvaEvaEvaEva/CEV-Eris)@[b92562ad8f...](https://github.com/EvaEvaEvaEvaEva/CEV-Eris/commit/b92562ad8f26c2354730f8a013195a90bbfbe9fd)
#### Sunday 2023-06-11 00:47:07 by ValoTheValo

Makes the "Gun" Not spawn in maint, makes MK58 fit in holsters (#8200)

* changes item path to be consistent

i hate kegdo

* kegdo code moment

what fucking moron designed this

* fixes MK58 not fitting in holster

pain

* Update holster.dm

* kegdo moment

---
## [Zergspower/Skyrat-tg](https://github.com/Zergspower/Skyrat-tg)@[a4994167fa...](https://github.com/Zergspower/Skyrat-tg/commit/a4994167fab9cd3ef571f7eef2ad1384306d8221)
#### Sunday 2023-06-11 01:19:56 by SkyratBot

[MIRROR] Drunk slurring scales based on how drunk you are [MDB IGNORE] (#21247)

* Drunk slurring scales based on how drunk you are (#75459)

## About The Pull Request

The strength of the slurring effect drunkness applies on you now scales
based on how drunk you are.

Being "a little" drunk still changes your saymod, and makes you
occasionally slur your words...

![image](https://github.com/tgstation/tgstation/assets/51863163/1b21b359-a1f9-428a-8e10-d2028ac59728)

But being "a lot" drunk kicks it up to 11

![image](https://github.com/tgstation/tgstation/assets/51863163/9d593c80-75ff-4d02-8e7c-e48c738154bb)

Additionally, drunk slurring was separated into "generic slurring" and
"drunk slurring", the former which does not scale but less closely
resembles drunkness. Generic slurring is used in places such as
concussions, so this is an added bonus.

As a result of the split, I had to update mind restoration. Now it heals
all types of slurring, which does include cult slurs.

## Why It's Good For The Game

I, and many other people, always found it very annoying when you became
completely illegible from taking one sip of a drink. This seeks to amend
that by making low levels of drunkness still for the most part be
legible and sane. Average drunkness is roughly the same / equal to the
old slurring effect, while "very drunk" is even more illegible and silly
(which I find funny).

This has the added bonus of separating out "drunk slurring" and "generic
slurring", allowing effects to slur your words without going full ham on
drunkness (burping and "huhh"s).

## Changelog

:cl: Melbert
add: When you are drunk, the strength of your slurring now varies based
on how drunk you are. Being "a little drunk" only rarely slurs your
words, being average drunk is the same as the old effect, while being
very drunk now slurs your words even more.
add: Some non-alcohol sources of slurring, such as concussions, now give
"generic slurring" rather than "drunk slurring", which less resemble
being drunk (ie, no burping).
add: Mind restoration now heals ALL slurring, rather than only drunk
slurring (which includes cult / heretic slurring).
/:cl:

* Drunk slurring scales based on how drunk you are

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [07am/Zero-K](https://github.com/07am/Zero-K)@[5e2b1657be...](https://github.com/07am/Zero-K/commit/5e2b1657be4cd0d9d7975eb434cc40c9a350ee1b)
#### Sunday 2023-06-11 02:25:16 by Helwor

Big update, various improvements and fixes, slight rewrite

-Adapted my code to be compatible with the Zero-K version

-Rewrote slightly the code to be more concise and efficient

-Fixed: The Zero-K version is broken since an edit made Sep 2020 (!) when user start to change spacing, the rectangles would never disappear because newspacing variable was never falsified at the end of the  Update round.

-Fixed: the param for spTraceScreenRay was the opposite of what it should be

-Improvement: The widget now adapt to the wrong engine grid which is off and also sometimes misleading when it comes to place units on water

-Added: On this particular case, widget gives the possibility for the user to either follow the grid coherence, or show the reality of where the unit will actually be placed. In that case, an extra rect is drawn to see where the first placement will land.  By usage, it seems the latter is more interesting so I put it on by default.
(More details in the comments that could help fix the problem with the engine)

-Improvement: the option panel now stop resetting scroll anytime an option is changed, this fix could easily be implemented universally by changing WG.crude.OpenPath, all it have to do is remembering 'scrollPosY' of the last panel and apply it to the new.

-Added: an option  for the user to choose wether rects should spread straightforward (if user want to only have a basic glance of the separation with no simulation of placing on the ground) or follow the ground, as it was before. I'm undecided which is the best as default for new users.

-Added: an option to have different colors of rects for bad placements, this on default if follow ground is on default, it seems to be adding a plus mostly in this case.

-Changed Description that's been edited, it does not just memorize spacing. I understand that it need to be concise, but a description is meant also to say what it does. User won't be able to tell if that widget make the previsualization or add mouse wheel to spacing by reading its description.

-Changed back title of an option. The purpose of how they are written is to build a sentence obviously, to make it more straightforward and user friendly. This change broke that concept. When user, especially new user, dive into options they can be lost as I was, to understand what option do what, if the option is dependent of another, etc... that's the purpose of my system to make all that as clear as I can.

-Changed back some default for new user, I think having the shift+mousewheel is a must, it's faster and more convenient, especially when discovering the game. I would have been glad to have that when I started, (that's, by the way, why I rewrote this widget in the first place).
Also changed back previsualization, with only 2 rects and only when spacing change, and for 0.7 sec
It is, in my opinion, also much more convenient for a new user to be able to see in a quick glance how your placement will be separated without the need of start posing queue and THEN realize the spacing is not good. If non-new user get tired of it, they will be able to find the options to undo it.
Indeed, new user will not be anymore really a new user when he discovers previsualization, if it's not on by default.

-Few minor things:
  -preGame is now set by GameFrame and then GameFrame removes itself
  -MouseWheel gets added/removed whenever shift+wheel option is changed
  -I don't see any reason to change the name spaced_rects in spaced_rects_2. As far as I know, one can only want that for resetting his own option to default for testing  purpose. Reverted it since it didn't make sense.
  -Upped the max time before infinite for show value and show rects to 10 sec
  -Didn't reverted it but imho, changing 'p' to 'placement' made the code uselessly more cumbersome than it already is.
  -Changed 'if not placementCache[unitDefID] then'  to 'if not placeTable[unitDefID] then' as the code was intended to mean
  note about this: since the vast majority of building have same sizex and sizez, maybe it could be improved by checking if it's relevant to consider the off-facing in 
  before.
 -Estomped the double dots before option titles when they are active, to make them less present.
 -update placement on more relevant changement of facing
 -Made the options defaults in concordance with the widget defaults
 -And maybe some other stuff I forgot

Lots of change, so please, let me know what you think.

---
## [encloinc/evals](https://github.com/encloinc/evals)@[44d941b773...](https://github.com/encloinc/evals/commit/44d941b7734983950d09d9f0012ec58ec45e171c)
#### Sunday 2023-06-11 02:33:13 by HorizonAuto

Context-free-grammars (#1097)

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

context-free-grammar

### Eval description

This tests the ability for GPT-4 to evaluate whether or not a string can
be produced by a given context-free grammar.

### What makes this a useful eval?

This is an interesting computational task. Context-free languages are
important in linguistics, and it will be interesting to see
how a language model fares in handling this task.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [✅] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [✅] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [✅] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [✅] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)
I've handcrafted a lot of these examples. Some of them are there to
'trick' the model––I think it will be a useful test to see how well the
language model can do at those.

## Eval structure 🏗️

Your eval should

- [✅] Check that your data is in `evals/registry/data/{name}`
- [✅] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [✅] Ensure you have the right to use the data you submit via this eval

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

- [✅] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [✅] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [✅] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [✅] I have filled out all required fields of this form
- [✅] I have used **Git LFS** for the Eval JSON data
- [✅] (Ignore if not submitting code) I have run `pip install
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
{"input": [{"role": "system","content": "You will be provided with a
context-free grammar, and a string. Respond whether or not that string
can be produced by the given grammar. Respond only with the word true or
false; you do not need to show your work. The empty string is
represented with ϵ, and productions are separated with the symbol ;. The
alphabet is always {0, 1}."}, {"role": "user", "content": "Given the
grammar 'S -> 01 | SS | 0S1 | ϵ', is the string '01010101' in the
language?"}], "ideal": "true"}
{"input": [{"role": "system","content": "You will be provided with a
context-free grammar, and a string. Respond whether or not that string
can be produced by the given grammar. Respond only with the word true or
false; you do not need to show your work. The empty string is
represented with ϵ, and productions are separated with the symbol ;. The
alphabet is always {0, 1}."}, {"role": "user", "content": "Given the
grammar 'S -> 01 | SS | 0S1 | ϵ', is the string '00011101' in the
language?"}], "ideal": "true"}
{"input": [{"role": "system","content": "You will be provided with a
context-free grammar, and a string. Respond whether or not that string
can be produced by the given grammar. Respond only with the word true or
false; you do not need to show your work. The empty string is
represented with ϵ, and productions are separated with the symbol ;. The
alphabet is always {0, 1}."}, {"role": "user", "content": "Given the
grammar 'S -> 01 | SS | 0S1 | ϵ', is the string '00110101' in the
language?"}], "ideal": "true"}
{"input": [{"role": "system","content": "You will be provided with a
context-free grammar, and a string. Respond whether or not that string
can be produced by the given grammar. Respond only with the word true or
false; you do not need to show your work. The empty string is
represented with ϵ, and productions are separated with the symbol ;. The
alphabet is always {0, 1}."}, {"role": "user", "content": "Given the
grammar 'S -> 01 | SS | 0S1 | ϵ', is the string '01001101' in the
language?"}], "ideal": "true"}
{"input": [{"role": "system","content": "You will be provided with a
context-free grammar, and a string. Respond whether or not that string
can be produced by the given grammar. Respond only with the word true or
false; you do not need to show your work. The empty string is
represented with ϵ, and productions are separated with the symbol ;. The
alphabet is always {0, 1}."}, {"role": "user", "content": "Given the
grammar 'S -> 01 | SS | 0S1 | ϵ', is the string '01010011' in the
language?"}], "ideal": "true"}
  ```
</details>

---------

Co-authored-by: Arjun Taneja <arjun.taneja02@gmail.com>

---
## [encloinc/evals](https://github.com/encloinc/evals)@[04e1312631...](https://github.com/encloinc/evals/commit/04e131263125d46812f19ce4cc58d55207beee3b)
#### Sunday 2023-06-11 02:33:13 by Nazar

Russian verse (#979)

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
russian-verse

### Eval description

The most popular Russian poems that nearly every Russian speaker can
recall

### What makes this a useful eval?

Understanding a basic Russian poem or any foreign literature is
significant for a Language Learning Model (LLM) like GPT-4 because it
enhances multilingual ability, provides cultural context, and improves
understanding of language structure. It makes the model globally useful,
and culturally sensitive.

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
{"input": [{"role": "system", "content": "Continue verse with no
punctuation marks:\nМороз и солнце день чудесный\nЕще ты дремлешь друг
прелестный \nПора красавица проснись\nОткрой сомкнуты негой
взоры\nНавстречу северной Авроры"}], "ideal": "Звездою севера явись"}
{"input": [{"role": "system", "content": "Continue verse with no
punctuation marks:\nУ лукоморья дуб зелёный\nЗлатая цепь на дубе том\nИ
днём и ночью кот учёный\nВсё ходит по цепи кругом\nИдёт направо песнь
заводит"}], "ideal": "Налево сказку говорит"}
{"input": [{"role": "system", "content": "Continue verse with no
punctuation marks:\nЯ к вам пишу чего же боле\nЧто я могу еще
сказать\nТеперь я знаю в вашей воле\nМеня презреньем наказать\nНо вы к
моей несчастной доле"}], "ideal": "Хоть каплю жалости храня"}
{"input": [{"role": "system", "content": "Continue verse with no
punctuation marks:\nЯ помню чудное мгновенье\nПередо мной явилась
ты\nКак мимолетное виденье\nКак гений чистой красоты\nВ томленьях грусти
безнадежной"}], "ideal": "В тревогах шумной суеты"}
{"input": [{"role": "system", "content": "Continue verse with no
punctuation marks:\nЛюбви надежды тихой славы\nНедолго нежил нас
обман\nИсчезли юные забавы\nКак сон как утренний туман\nНо в нас горит
еще желанье"}], "ideal": "Под гнетом власти роковой"}
  ```
</details>

---
## [Dobby233Liu/sonic-cd-disassembly](https://github.com/Dobby233Liu/sonic-cd-disassembly)@[09e3e4d6d4...](https://github.com/Dobby233Liu/sonic-cd-disassembly/commit/09e3e4d6d4dd45ee21ae7efcebf1b0cb91556cdc)
#### Sunday 2023-06-11 03:03:38 by Liu Wenyuan

Revert "fuck You"

This reverts commit 08bd0520536c0c8cf9ef02d95bea334fd846bcc8.

---
## [erikdesjardins/rust](https://github.com/erikdesjardins/rust)@[8ad70e7f99...](https://github.com/erikdesjardins/rust/commit/8ad70e7f99b6a5eca65f6ef76cedee6c40132d6f)
#### Sunday 2023-06-11 03:08:58 by bors

Auto merge of #14866 - AndreasBackx:feature/doc-comments-markdown, r=Veykril

[editors/code] add markdown syntax highlighting to doc comments

_This is a continuation of https://github.com/microsoft/vscode/pull/169956 and https://github.com/dustypomerleau/rust-syntax/pull/37 (that repo is no longer maintained: https://github.com/dustypomerleau/rust-syntax/issues/39#issuecomment-1427339029). The VS Code team seemed to prefer this being inside of an extension._

This adds Markdown highlighting to doc comment lines and blocks. Currently it is thus regarded both as a comment and as Markdown which leads to normally foreground text being in the colour of the comment and the rest highlighted like Markdown or its own embedded languages in code blocks.

![image](https://github.com/rust-lang/rust-analyzer/assets/1593486/c84f2e83-faea-47ca-853d-3728a07b2b66)

![image](https://github.com/rust-lang/rust-analyzer/assets/1593486/f4191425-32cd-451c-ae3a-29a0970ce7a2)

Block comments are supported, but currently not when there is a `*` at the start of the line:
![image](https://github.com/rust-lang/rust-analyzer/assets/1593486/ce3b58d5-9dca-4376-bffe-4f5a54acbe37)
![image](https://github.com/rust-lang/rust-analyzer/assets/1593486/b73a5ee6-a178-4aef-a0e4-3d75e4e7d8e5)

I'm not entirely sure if I can easily fix this, I'd need to find a way to make the content ignore the `*`. Though I'm unsure if it's important as there are [conventions against using block comments](
https://rust-lang.github.io/rfcs/1574-more-api-documentation-conventions.html#use-line-comments) and using them without `*` does work. All of this TextMate grammar is so hard to find documentation on that _honestly_ I'd just not want to support this considering the effort.

Let me know what everyone thinks of this being in rust-analyzer. I've personally found it hard to write large amounts of Rust documentation due to the lack of Markdown syntax highlighting.

Also, thank you `@adenine-dev` as well for making this available in the interim and your enthousiasm. Wanted to get this PR out sooner, but life gets in the way.

---
## [meemofcourse/Shiptest](https://github.com/meemofcourse/Shiptest)@[00b8761853...](https://github.com/meemofcourse/Shiptest/commit/00b8761853eabc6d73073cce4708dc71d402539c)
#### Sunday 2023-06-11 03:09:24 by Apogee-dev

Slays the Lamia (#1974)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Removes the Lamia in its entirety.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

The Lamia is awkwardly-mapped, inconsistent with the current lore (in as
much as wizard lore is even established at this point), and most
damningly, it's a magnet for new players, often ones with an LRP bent.
The ship itself encourages wizard RP, yes, but frankly, wizard RP is not
the kind of RP we necessarily want here. I'd rather new players' first
experience on this server involved actually interacting with the faction
lore in at least some measure.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
del: Removed the Lamia-class wizard ship
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [kalw/play-with-docker](https://github.com/kalw/play-with-docker)@[a66a469fa0...](https://github.com/kalw/play-with-docker/commit/a66a469fa0804ba22679b808203030d242efe157)
#### Sunday 2023-06-11 03:33:02 by Marcos Lilljedahl

Change ssh key since RSA is deprecated

Copyright (c) 2023 Author. All rights reserved.

Licensed under the "THE BEER-WARE LICENSE" (Revision 42):
Everyone is permitted to copy and distribute verbatim or modified
copies of this license document, and changing it is allowed as long
as the name is changed.

	DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
	0. You just DO WHAT THE FUCK YOU WANT TO.

Signed-off-by: Marcos Lilljedahl <marcosnils@gmail.com>

---
## [philIip/react-native](https://github.com/philIip/react-native)@[a29cb85bde...](https://github.com/philIip/react-native/commit/a29cb85bde5854059bf38846c434069f3b9137b5)
#### Sunday 2023-06-11 04:30:23 by Phillip Pan

introduce build boilerplate for ios unit tests (#37811)

Summary:
Pull Request resolved: https://github.com/facebook/react-native/pull/37811

Changelog: [Internal]

i am looking to add ios unit tests to venice and this is the first unit test suite that will test native ios code in the new architecture afaik, so i wanted to open this up to discussion.

currently, all `XCTest` in `react-native-github` are coupled with the `RNTester` target. my main qualm with this is i am concerned that it won't scale well. currently we have only ~30ish tests but ultimately if we want a proper testing suite, surely this count will be in the hundreds and that won't be able to reasonably live in a single test target.

however, the trade is that this test will not show up in RNTester. i have added a unit test to RNTester before in D31949237, however the experience was extremely painful as i had to manually update the `project.pbxproj` to include my file, and i had to manually determine what hex value was the next one (for whatever reason, this doesn't increment at the endian...).

i am wondering if we can treat the current unit testing experience in RNTester as pretty much maintenance mode and start thinking of a improved version starting with something more modular like this.

Reviewed By: cipolleschi

Differential Revision: D46467229

fbshipit-source-id: d96fa1de276ec70cdefc61332b09a541477ebe0c

---
## [openai/evals](https://github.com/openai/evals)@[d708a6be26...](https://github.com/openai/evals/commit/d708a6be261bfcb04962e64969164d737ba3972c)
#### Sunday 2023-06-11 05:00:13 by dougkwanna

NFL Point Combinations Eval (#1129)

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

NFL Point Combinations

### Eval description

This eval tests the model's ability to calculate all the possible ways
to achieve a specific score by a single team in an NFL game.

### What makes this a useful eval?

This eval is actually very similar to the coin change problem which
GPT-4 handles very well. However, it is extremely inaccurate when asked
to applied that same type of problem to a real life situation (2.5%
accuracy for GPT-3.5-turbo and 12.5% accuracy for GPT-4). It is
important for the model to learn how to derive logic problems from real
life context.

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

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

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
{"input": [{"role": "system", "content": "As of the year 2010, in
American Football, how many unique, order-independent ways can an NFL
(National Football League) team score exactly 4 points in a single game?
Exclude one-point safeties as one of the scoring options. List out all
the possible combinations and write your final answer as a single number
enclosed in square brackets."}], "ideal": "[1]"}
{"input": [{"role": "system", "content": "As of the year 2010, in
American Football, how many unique, order-independent ways can an NFL
(National Football League) team score exactly 6 points in a single game?
Exclude one-point safeties as one of the scoring options. List out all
the possible combinations and write your final answer as a single number
enclosed in square brackets."}], "ideal": "[3]"}
{"input": [{"role": "system", "content": "As of the year 2010, in
American Football, how many unique, order-independent ways can an NFL
(National Football League) team score exactly 7 points in a single game?
Exclude one-point safeties as one of the scoring options. List out all
the possible combinations and write your final answer as a single number
enclosed in square brackets."}], "ideal": "[2]"}
{"input": [{"role": "system", "content": "As of the year 2010, in
American Football, how many unique, order-independent ways can an NFL
(National Football League) team score exactly 12 points in a single
game? Exclude one-point safeties as one of the scoring options. List out
all the possible combinations and write your final answer as a single
number enclosed in square brackets."}], "ideal": "[7]"}
{"input": [{"role": "system", "content": "As of the year 2010, in
American Football, how many unique, order-independent ways can an NFL
(National Football League) team score exactly 25 points in a single
game? Exclude one-point safeties as one of the scoring options. List out
all the possible combinations and write your final answer as a single
number enclosed in square brackets."}], "ideal": "[24]"}
{"input": [{"role": "system", "content": "As of the year 2010, in
American Football, how many unique, order-independent ways can an NFL
(National Football League) team score exactly 38 points in a single
game? Exclude one-point safeties as one of the scoring options. List out
all the possible combinations and write your final answer as a single
number enclosed in square brackets."}], "ideal": "[68]"}
  ```
</details>

---
## [Tejas-Jain/Tejas-Jain](https://github.com/Tejas-Jain/Tejas-Jain)@[6b6e4a70e8...](https://github.com/Tejas-Jain/Tejas-Jain/commit/6b6e4a70e8e311a9df95342e411f857984556303)
#### Sunday 2023-06-11 05:19:26 by Tejas Jain

Update README with Rsc.md

1. Backup json file Rename to data.json
{"prefix":{"title":"Hi 👋, I'm","currentWork":"🔭 I’m currently working on","currentLearn":"🌱 I’m currently learning","collaborateOn":"👯 I’m looking to collaborate on","helpWith":"🤝 I’m looking for help with","ama":"💬 Ask me about","contact":"📫 How to reach me","resume":"📄 Know about my experiences","funFact":"⚡ Fun fact","portfolio":"👨‍💻 All of my projects are available at","blog":"📝 I regularly write articles on"},"data":{"title":"Tejas Jain","subtitle":"A passionate full stack developer from India","currentWork":"","currentLearn":"Flask","collaborateOn":"","helpWith":"","ama":"React, Nodejs","contact":"1tejasjain@gmail.com","funFact":"","twitterBadge":false,"visitorsBadge":true,"badgeStyle":"flat","badgeColor":"0e75b6","badgeLabel":"Profile views","githubProfileTrophy":false,"githubStats":true,"githubStatsOptions":{"theme":"","titleColor":"","textColor":"","bgColor":"","hideBorder":false,"cacheSeconds":null,"locale":"en"},"topLanguages":true,"topLanguagesOptions":{"theme":"","titleColor":"","textColor":"","bgColor":"","hideBorder":false,"cacheSeconds":null,"locale":"en"},"streakStats":true,"streakStatsOptions":{"theme":""},"devDynamicBlogs":false,"mediumDynamicBlogs":false,"rssDynamicBlogs":false},"link":{"currentWork":"","collaborateOn":"","helpWith":"","portfolio":"","blog":"","resume":""},"social":{"github":"tejas-jain","dev":"","linkedin":"1tejasjain","codepen":"","stackoverflow":"","kaggle":"tejasjain2","codesandbox":"","fb":"","instagram":"","twitter":"","dribbble":"","behance":"","medium":"","youtube":"","codechef":"tejas_jain","hackerrank":"1tejasjain","codeforces":"","leetcode":"tejas-jain","topcoder":"","hackerearth":"","geeks_for_geeks":"","discord":"","rssurl":""},"skills":{"11ty":false,"amplify":false,"android":false,"angular":false,"angularjs":false,"apachecordova":false,"appwrite":false,"arduino":false,"aws":false,"azure":false,"babel":false,"backbonejs":false,"bash":false,"blender":false,"bootstrap":true,"bulma":false,"c":true,"canvasjs":false,"cassandra":false,"chartjs":false,"circleci":false,"clojure":false,"cockroachdb":false,"codeigniter":false,"coffeescript":false,"couchdb":false,"cplusplus":true,"csharp":false,"css3":true,"cypress":false,"d3js":false,"dart":false,"django":false,"docker":false,"dotnet":false,"elasticsearch":false,"electron":false,"elixir":false,"ember":false,"erlang":false,"express":true,"figma":true,"firebase":false,"flask":true,"flutter":false,"framer":false,"gatsby":false,"gcp":false,"git":true,"go":false,"grafana":false,"graphql":false,"gridsome":false,"gtk":false,"gulp":false,"hadoop":false,"haskell":false,"heroku":false,"hexo":false,"hive":false,"html5":true,"hugo":false,"ifttt":false,"illustrator":false,"invision":false,"ionic":false,"jasmine":false,"java":false,"javascript":true,"jekyll":false,"jenkins":false,"jest":false,"kafka":false,"karma":false,"kibana":false,"kotlin":false,"kubernetes":false,"laravel":false,"linux":false,"mariadb":false,"materialize":false,"matlab":false,"middleman":false,"mocha":false,"mongodb":true,"mssql":false,"mysql":true,"nativescript":false,"nestjs":false,"nextjs":false,"nginx":false,"nim":false,"nodejs":true,"nuxtjs":false,"objectivec":false,"opencv":false,"openresty":false,"oracle":false,"pandas":false,"perl":false,"photoshop":false,"php":false,"postgresql":false,"postman":true,"pug":false,"puppeteer":false,"python":true,"pytorch":false,"qt":false,"quasar":false,"rabbitMQ":false,"rails":false,"react":true,"reactnative":false,"realm":false,"redis":false,"redux":false,"ruby":false,"rust":false,"sapper":false,"sass":true,"scala":false,"scikit_learn":false,"scully":false,"sculpin":false,"seaborn":false,"selenium":false,"sketch":false,"solr":false,"spring":false,"sqlite":false,"svelte":false,"swift":false,"symfony":false,"tailwind":false,"tensorflow":false,"travisci":false,"typescript":false,"unity":false,"unreal":false,"vagrant":false,"vuejs":false,"vuepress":false,"vuetify":false,"webpack":false,"wx_widgets":false,"xamarin":false,"xd":false,"zapier":false},"support":{"buyMeACoffee":""}}
2. Image Link: https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjYwOGEwMzBlZTFiMTU4N2VlOTk2MGUxMjI5MDM2NmI0OTBhZGMwNyZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/qgQUggAC3Pfv687qPC/giphy.gif
3. Another Image: https://cdn.dribbble.com/users/1162077/screenshots/3848914/programmer.gif
4. https://www.youtube.com/watch?v=G-EGDH50hGE
5. https://rahuldkjain.github.io/gh-profile-readme-generator/

---
## [vampirebat74/lobotomy-corp13](https://github.com/vampirebat74/lobotomy-corp13)@[53a1fa3d8d...](https://github.com/vampirebat74/lobotomy-corp13/commit/53a1fa3d8d86d9de8cec8e802f92f7e8a8371aa2)
#### Sunday 2023-06-11 05:29:57 by Mr.Heavenly

Tool ego

adds tool E.G.O

removes a extra line

fixes shit

swindle

voce

divinity

fixes shit

shifts divinity down a few pixels

This is the fourth time this same commit was made

I hate TG so fucking much like it's unbelievable why does this only fuck up on my PC? WHY?

hyde weapon

stuff

hyde code

hyde fix

new sprites

inhands

destiny effect

heart sfx

---
## [ArcaneMusic/TG-Station-Arcane-Remix](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix)@[527fb7b003...](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix/commit/527fb7b0030d13fc11939d88030b1dc4772742a6)
#### Sunday 2023-06-11 06:14:51 by DrTuxedo

ELEVATOR MUSIC: True Elevator Experience (#75388)

## About The Pull Request
Adds elevator music into the game that is played by an elevator panel.


https://github.com/tgstation/tgstation/assets/42353186/1a801604-3990-46ae-a96a-b3766b102d62

It's done by using loop sound, with a Kevin MacLeod "Local Forecast -
Elevator" (UNDER CC ATTRIBUTIONS 4.0, and we anyway used some other
Kevin MacLeod music) chopped into 8 small pieces.
The elevator panel has a variable which allows playing music but can be
changed in the map editor if you don't want it to play at certain
places.

(It also doesn't ignore walls, this means you can't hear the music
through wall or when elevator is closed)
## Why It's Good For The Game
Gives elevators more flavour and love, especially when people mostly
prefer stairs to those "laggy crushing machines."
Because of this people might instead hop into an elevator just to hear
meme elevator music, which is relaxing and might create comedic
situations (although elevators don't move that fast)
## Changelog
:cl: DrDiasyl aka DrTuxedo
sound: Nanotrasen have started installing music players in the elevators
to boost workers' morale.
/:cl:

---------

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [2022-AP-CS-A/Untiy](https://github.com/2022-AP-CS-A/Untiy)@[332bfbbe8d...](https://github.com/2022-AP-CS-A/Untiy/commit/332bfbbe8d6382fa5b601b9011c5ff80b4f402a4)
#### Sunday 2023-06-11 07:45:06 by SumedhChinta

Done?

i think we done. the death sound doesnt play right but honestly it doesnt matter. and when it does play its kinda funny.

---
## [petre-symfony/api-platform-3-part-2-security-for-you-symfonycasts-june-2023](https://github.com/petre-symfony/api-platform-3-part-2-security-for-you-symfonycasts-june-2023)@[04e4fb7dc3...](https://github.com/petre-symfony/api-platform-3-part-2-security-for-you-symfonycasts-june-2023/commit/04e4fb7dc396f0f3779e5e504b199e32bf89b31e)
#### Sunday 2023-06-11 08:07:51 by Petre Ro

29.1 Custom Normalizer

 Copy the test method - testOwnerCanSeeIsPublishedField. We just added some magic so that admin users can see the isPublished property. This method tests for our next mission: that owners of a DragonTreasure can also see this.

 Run it with:

  symfony php bin/phpunit --filter=testOwnerCanSeeIsPublishedField
 And... it fails: expected null to be the same as false, because the field isn't returned at all.

 To fix this, over in DragonTreasure, add a third special group: owner:read

 Can you see where we're going with this? If we are the owner of a DragonTreasure, we'll add this group and then the field will be included. However, pulling this off is tricky.

 As we talked about in the last video, normalization groups start static: they live up here in our config. The context builder allows us to make these groups dynamic per request. So, if we're an admin user, we can add an extra admin:read group, which will be used when serializing every object for this entire request.

 But in this situation, we need to make the group dynamic per object. Imagine if we're returning 10 DragonTreasure's: the user may only own one of them, so only that one DragonTreasure should be normalized using this extra group.

 The Job of Normalizers
 - To handle this level of control, we need a custom normalizer. Normalizers are core to Symfony's serializer. They're responsible for turning a piece of data - like an ApiResource object or a DateTime object that lives on a property - into a scalar or array value. By creating a custom normalizer, you can do pretty much any weird thing you want!

 Find your terminal and run:

  php  bin/console debug:container --tag=serializer.normalizer

 I love this: it shows us every single normalizer in our app! We can see stuff that's responsible for normalizing UUIDs.... this is what normalizes any of our ApiResource objects to JSON-LD and here's one for a DateTime. There's a ton of interesting stuff.

 Our goal is to create our own normalizer, decorate an existing core normalizer, then add the dynamic group before that core normalizer is called.

 Creating the Normalizer Class
 - So let's get to work! Over in src/ - it doesn't really matter how we organize things - I'm going to create a new directory called Normalizer. Let me collapse a few things... so it's easier to look at. Inside that, add a new class called, how about, AddOwnerGroupsNormalizer. All normalizers must implement NormalizerInterface... then go to "Code"->"Generate" or Command+N on a Mac and select "Implement methods" to add the two we need

 Here's how this works: as soon as we implement NormalizerInterface, anytime any piece of data is being normalized, it will call our supportsNormalization() method. There, we can decide whether or not we know how to normalize that thing. If we return true, the serializer will then call normalize(), pass us that data, and then we return the normalized version.

 And actually, to avoid some deprecation errors, pop open the parent class. The return type is this crazy array thingy. Copy that... and add it as the return type. You don't have to do this - everything would work without it - but you'd get a deprecation warning in your tests.

 Down for supportsNormalization(), in Symfony 7, there will be an array $context argument... and the method will return a bool

 Which Service do We Decorate?
 - Before we fill this in or set up decoration, we need to think about which core service we're going to decorate. Here's my idea: if we replace the main core normalizer service with this class, we could add the group then call the decorated normalizer... so that everything then works like usual, except that it has the extra group.

 Back at the terminal, run:

  bin/console debug:container normalizer

 We get back a bunch of results. That makes sense: there's a main normalizer, but then the normalizer itself has lots of other normalizers inside of it to handle different types of data. So... where is the top level normalizer? It's actually not even in this list: it called serializer. Though, as we'll see next, even that isn't quite right.

---
## [petre-symfony/api-platform-3-part-2-security-for-you-symfonycasts-june-2023](https://github.com/petre-symfony/api-platform-3-part-2-security-for-you-symfonycasts-june-2023)@[d630ffc443...](https://github.com/petre-symfony/api-platform-3-part-2-security-for-you-symfonycasts-june-2023/commit/d630ffc4435802553399e43ef470e3cefb7b7507)
#### Sunday 2023-06-11 08:07:51 by Petre Ro

28.1. Dynamic Groups: Context Builder

 In DragonTreasure, find the  field. Earlier we added this ApiProperty security thing so that the field is only returned for admin users or owners of this treasure. This is a simple and 100% valid way to handle this situation.

 However, there is another way to handle fields that should be dynamic based on the current user... and it may or may not have two advantages depending on your situation.

 The security Options vs Dynamic Groups
 - First, check out the documentation. Open the GET endpoint for a single DragonTreasure. And, even without trying it, you can see that isPublished is a field that is correctly advertised in our docs.

 So, that's good, right? Yea! Well, probably. If isPublished were truly an internal, admin-only field, we might not want it advertised to the world.

 The second possible problem with security is that, if you have this option on many properties, it's going to run that security check a lot of times when returning a collection of objects. Honestly, that probably won't cause performance issues, but it's something to be aware of.

 Inventing New Serialization Groups
 - To solve these two possible problems - and, honestly, just to learn more about how API Platform works under the hood - I want to show you an alternative solution. Remove the ApiProperty attribute

 And replace it with two new groups. We're not going to use the normal treasure:read and treasure:write... because then the fields would always be part of our API. Instead, use admin:read and admin:write

 This won't work yet... because these groups are never used. But here's the idea: if the current user is an admin, then when we serialize, we'll add these two groups.

 The tricky part is, right now, groups are static! We set them way up here on the ApiResource attribute - or on a specific operation - and that's it! But we can make them dynamic.

---
## [petre-symfony/api-platform-3-part-2-security-for-you-symfonycasts-june-2023](https://github.com/petre-symfony/api-platform-3-part-2-security-for-you-symfonycasts-june-2023)@[623172508d...](https://github.com/petre-symfony/api-platform-3-part-2-security-for-you-symfonycasts-june-2023/commit/623172508d34493e7c24c5efa19cafdf0193e158)
#### Sunday 2023-06-11 08:07:51 by Petre Ro

27.3. Fixing the Validation Groups
 - Ok, back to the test! It's failing with a 422. Open the error response. Ah, it's from plainPassword: this field should not be blank!

 The plainPassword property is not persisted to the database. So, it's always empty at the start of an API request. When we create a User, we absolutely do want this field to be required. But when we're editing a User, we don't need this field to be set. They can set it in order to change their password, but that's optional.

 This is the first spot where we need conditional validation: validation should happen on one operation, but not on others. The way to fix this is with validation groups, which is very similar to serialization groups.

 Find the Post operation and pass a new option called validationContext with, you guessed it, groups! Set this to an array with a group called Default with a capital D. Then invent a second group: postValidation

 When the validator validates an object, by default, it validates everything that's in a group called Default. And any time you have a constraint, by default that constraint is in that Default group. So what we're saying here is:

  We want to validate all the normal constraints plus any constraints that are in the postValidation group.

 Now we can take that postValidation, go down to plainPassword and set groups to postValidation

 That removes this constraint from the Default group and only includes it in the postValidation group. Thanks to this, other operations like Patch will not run this, but the Post operation will.

 Run the test now:

  symfony php bin/phpunit --filter=testPatchToUpdateUser
 We're unstoppable! In fact, all of our tests are passing!

 Careful: PUT Can Create Objects
 - But head's up! In User, we still have both Put and Patch. I haven't played with it much yet, but the new Put behavior, in theory, does support creating objects. This can make things tricky: do we need to require the password or not? It depends! This might be another reason for removing the Put operation to keep life simple. That gives us one operation for creating and one operation for editing.

 Next: let's explore making our serialization groups dynamic based on the user. This will give us another way to include or not include fields based on who is logged in. And it'll lead us towards adding super custom fields.

---
## [Consensus-NLP/openai-evals](https://github.com/Consensus-NLP/openai-evals)@[8e4d43bb5b...](https://github.com/Consensus-NLP/openai-evals/commit/8e4d43bb5b06a725c70a9b2c1eaad38787e737aa)
#### Sunday 2023-06-11 09:43:52 by tescao

Human body movement (#360)

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

Human body movement

### Eval description

An eval to asses the model's understanding of how a human body moves,
e.g. after performing an exercise starting from a known side, which side
does the human end up with?

There are 20 unique samples + 20 samples with the starting side flipped,
as I noticed ChatGPT performed differently when starting side was
changed in the same movement.

### What makes this a useful eval?

The eval test the model's physical reasoning abilities as well as good
knowledge of a human body, which is necessary for being safe and helpful
to users, and could be used in fitness applications, as an aid for
people with visual impairments, generating dance sequences, etc.

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
- [ ] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [ ] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [ ] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

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
{"input": [{"role": "system", "content": "Answer the question based on
the following description of a movement. Assume average human body
ability."}, {"role": "user", "content": "\nDescription: A woman is
standing on her hands and feet, facing the floor and reaching her hips
towards the ceiling, she lifts her left leg towards the ceiling, then
lowers it and puts it in between her hands. She inhales and twists her
torso pressing her chest against her inner thigh and reaches her arm to
the ceiling.\nQuestion: Which arm does she reach up?\nAnswer with a
single word: 'left' or 'right'."}], "ideal": "left"}
{"input": [{"role": "system", "content": "Answer the question based on
the following description of a movement. Assume average human body
ability."}, {"role": "user", "content": "\nDescription: A woman is
standing on her left leg, she lifts her other leg and presses it into
her chest with both arms. She then grabs the heel of her lifted leg with
her hand and stretches it all the way to the side, still holding the
heel. She remains upright with her chest opened.\nQuestion: Which hand
does she use to hold her leg?\nAnswer with a single word: 'left' or
'right'."}], "ideal": "right"}
{"input": [{"role": "system", "content": "Answer the question based on
the following description of a movement. Assume average human body
ability."}, {"role": "user", "content": "\nDescription: A woman is
holding a reversed plank position, holding her body in a straight line
and facing up. She lifts her left leg off the ground then lifts her hand
off the ground and transitions into a side plank.\nQuestion: Which hand
does she have to lift off the ground to transition into side
plank?\nAnswer with a single word: 'left' or 'right'."}], "ideal":
"left"}
{"input": [{"role": "system", "content": "Answer the question based on
the following description of a movement. Assume average human body
ability."}, {"role": "user", "content": "\nDescription: A man is in a
plank position, holding his body in a straight line and facing the
floor. Bracing his core, he lifts his left leg off the floor until it is
level with his body, then lifts his opposite arm until it is level with
his body, then puts them back on the floor. This is one repetition and
he does eight such repetitions, starting with his left leg and
alternating sides. This is one set. He takes a few seconds to rest then
does the same set again, starting with his right leg this
time.\nQuestion: Which arm does he lift at the last repetition of the
last set?\nAnswer with a single word: 'left' or 'right'."}], "ideal":
"right "}
{"input": [{"role": "system", "content": "Answer the question based on
the following description of a movement. Assume average human body
ability."}, {"role": "user", "content": "\nDescription: A woman stands
straight, she takes a big step back with her left foot, turning toes of
that foot out slightly. She lengthens her torso, opening her chest and
reaching her side towards her front leg until she can grab her leg with
her arm. She reaches the other arm to the sky and holds, lengthening her
body and opening her chest more.\nQuestion: Which arm did she reach
up?\nAnswer with a single word: 'left' or 'right'."}], "ideal": "left"}
  ```
</details>

---------

Co-authored-by: Marina Pchelina <marinapchelina@MarinaucBookPro.hitronhub.home>

---
## [Consensus-NLP/openai-evals](https://github.com/Consensus-NLP/openai-evals)@[33484c8341...](https://github.com/Consensus-NLP/openai-evals/commit/33484c83416c30733359d5c4dcb9a61f91cab8a6)
#### Sunday 2023-06-11 09:43:52 by emu1729

Added AIME eval (#293)

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
AIME-Evaluation

### Eval description

This eval evaluates GPT on some selected AIME (American Invitational
Mathematics Examination) problems. This is a selective and prestigious
mathematical examination for high schoolers. All questions are selected
from the 2001 and 2002 AIME I and II examinations.

### What makes this a useful eval?

This evaluation combines math and logical evaluation and is designed to
be quite challenging. The model must first understand the math question
asked and then perform the math equations needed to come up with a
reasonable solution.

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

Our eval was designed to include both math and logical reasoning and is
quite challenging. This is a level above the AMC10 examination.

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
- [X] (Ignore if not submitting code) I have run `pip install
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
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"Find the sum of all positive
two-digit integers that are divisible by each of their
digits."}],"ideal":"630"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"A fair die is rolled four
times. The probability that each of the final three rolls is at least as
large as the roll preceding it may be expressed in the form m\/n, where
m and n are relatively prime positive integers. Find m +
n"}],"ideal":"079"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"A sphere is inscribed in the
tetrahedron whose vertices are A = (6, 0, 0), B = (0, 4, 0), C = (0, 0,
2), and D = (0, 0, 0).The radius of the sphere is m \/ n, where m and n
are relatively prime positive integers. Find m + n."}],"ideal":"005"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"A mail carrier delivers mail
to the nineteen houses on the east side of Elm Street. The carrier
notices that no two adjacent houses ever get mail on the same day, but
that there are never more than two houses in a row that get no mail on
the same day. How many different patterns of mail delivery are
possible?"}],"ideal":"351"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"The numbers 1, 2, 3, 4, 5, 6,
7, and 8 are randomly written on the faces of a regular octahedron so
that each face contains a different number. The probability that no two
consecutive numbers, where 8 and 1 are considered to be consecutive, are
written on faces that share an edge is m\/n, where m and n are
relatively prime positive integers. Find m + n."}],"ideal":"085"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"Let N be the largest positive
integer with the following property: reading from left to right, each
pair of consecutive digits of N forms a perfect square. What are the
leftmost three digits of N?"}],"ideal":"816"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"Each of the 2001 students at a
high school studies either Spanish or French, and some study both. The
number who study Spanish is between 80 percent and 85 percent of the
school population, and the number who study French is between 30 percent
and 40 percent. Let m be the smallest number of students who could study
both languages, and let M be the largest number of students who could
study both languages. Find M-m."}],"ideal":"298"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"A set of positive numbers has
the 'triangle-property' if it has three distinct elements that are the
lengths of the sides of a triangle whose area is positive. Consider sets
{4, 5, 6, ..., n} of consecutive positive integers, all of whose
ten-element subsets have the triangle property. What is the largest
possible value of n?"}],"ideal":"253"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"Each unit square of a 3-by-3
unit-square grid is to be colored either blue or red. For each square,
either color is equally likely to be used. The probability of obtaining
a grid that does not have a 2-by-2 red square is m\/n, where m and n are
relatively prime positive integers. Find m + n."}],"ideal":"929"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"Given that x and y are both
integers between 100 and 999, inclusive; y is the number formed by
reversing the digits of x; and z=|x-y|. How many distinct values of z
are possible?"}],"ideal":"009"}

  ```
</details>

---------

Co-authored-by: Emily Mu <emilymu@30-10-85.wireless.csail.mit.edu>
Co-authored-by: Emily Mu <emilymu@30-10-24.wireless.csail.mit.edu>

---
## [Consensus-NLP/openai-evals](https://github.com/Consensus-NLP/openai-evals)@[06802cc61d...](https://github.com/Consensus-NLP/openai-evals/commit/06802cc61da1395e492ecc8b1ed7153c42b5e2df)
#### Sunday 2023-06-11 09:43:52 by Alexander Rössler

add eval for time zone conversion (#382)

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
test-time-zone-conversion

### Eval description

Test the models' ability to convert between different times zones,
including the 2-week period between daylight savings time change in
Europe and US.

### What makes this a useful eval?

For using the model as a personal AI assistant, a frequent task is to
convert times between different time zones, e.g. for scheduling meetings
or to simply check when a person is available. Currently, GPT-3.5 fails
in giving correct results in the 2-week period where the time offset
between Europe and US is shorter due to different date of daylight
saving time change. US switches to daylight savings time on the second
Sunday of March, Europe switches on the last Sunday of March.
Potentially there are further anomalies which need to be evaluated. I'm
happy to contribute more cases if this PR is accepted.

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

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

[x] Very common task for AI assistants.

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
{"input": [{"role": "system", "content": "Today is March 31st 2023."},
{"role": "user", "content": "Convert 22:00 CET to PT. Output in 24h
format hh:mm, no explanation."}], "ideal": "13:00"}
{"input": [{"role": "system", "content": "Today is March 31st 2023, the
current time in CET is 22:00"}, {"role": "user", "content": "Which time
is it in PT? Output in 24h format hh:mm, no explanation."}], "ideal":
"13:00"}
{"input": [{"role": "system", "content": "Today is March 21st 2023."},
{"role": "user", "content": "Convert 22:00 CET to PT. Output in 24h
format hh:mm, no explanation."}], "ideal": "14:00"}
{"input": [{"role": "system", "content": "Today is March 21st 2023, the
current time in CET is 10pm"}, {"role": "user", "content": "Which time
is it in PT? Output in 24h format hh:mm, no explanation."}], "ideal":
"14:00"}
{"input": [{"role": "system", "content": "Today is November 4th 2023."},
{"role": "user", "content": "Convert 14:00 CET to CT. Output in 24h
format hh:mm, no explanation."}], "ideal": "07:00"}
{"input": [{"role": "system", "content": "Today is November 5th 2023,
the current time in CET is 14:00"}, {"role": "user", "content": "Which
time is it in CT? Output in 24h format hh:mm, no explanation."}],
"ideal": "07:00"}
{"input": [{"role": "system", "content": "Today is November 3rd 2023."},
{"role": "user", "content": "Convert 14:00 CET to CT. Output in 24h
format hh:mm, no explanation."}], "ideal": "8:00"}
{"input": [{"role": "system", "content": "Today is November 2nd 2023,
the current time in CET is 2pm"}, {"role": "user", "content": "Which
time is it in CT? Output in 24h format hh:mm, no explanation."}],
"ideal": "8:00"}
  ```
</details>

---
## [Consensus-NLP/openai-evals](https://github.com/Consensus-NLP/openai-evals)@[cb23f7aff1...](https://github.com/Consensus-NLP/openai-evals/commit/cb23f7aff1a84328ff8bed31fa2ab65f3dfdfb12)
#### Sunday 2023-06-11 09:43:52 by Andrew

Update fuzzy_match.py (#989)

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
[Insert Eval name here]

### Eval description

[Insert a short description of what your eval does here]

### What makes this a useful eval?

[Insert why this eval is worth including and any additional context]

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [ ] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [ ] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [ ] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [ ] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [ ] Check that your data is in `evals/registry/data/{name}`
- [ ] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [ ] Ensure you have the right to use the data you submit via this eval

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

- [ ] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [ ] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [ ] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [ ] I have filled out all required fields of this form
- [ ] I have used **Git LFS** for the Eval JSON data
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
  INSERT_EVAL_HERE
  ```
</details>

---
## [Consensus-NLP/openai-evals](https://github.com/Consensus-NLP/openai-evals)@[8f8632ec55...](https://github.com/Consensus-NLP/openai-evals/commit/8f8632ec55ee1f9704fe34225e1bce0cd999a8b1)
#### Sunday 2023-06-11 09:43:52 by Oshan Upreti

Nepali song singer recognition (#892)

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
Nepali Song Singer

### Eval description

It tests the ability to understand Nepali language from given English
Transliteration phrase which is provided by user as a song title, and
checks the singer/band of the song. This eval has the accuracy of zero.
And, I still created this eval PR because I get the wrong answers every
time I ask, and I don't think that should be the case. It might not be
something that needs to be done immediately, but in a near future you
would expect your AI to answer it correctly.

### What makes this a useful eval?

If it can do for any English songs in the database, it should be able to
do for other languages as well. This is just a pattern I found it in my
mother tongue, but there might be different other languages where this
is happening as well, and it can be other things as well not just the
song title recognition.

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
{"input": [{"role": "system", "content": "A user will give you a English
transliteration phrase of Nepali song. Give the name of the singer or
band."}, {"role": "user", "content": "Sayad Timro Bato Ma"}], "ideal":
"Raju Lama"}
{"input": [{"role": "system", "content": "A user will give you a English
transliteration phrase of Nepali song. Give the name of the singer or
band."}, {"role": "user", "content": "Timi Lai Dekhera"}], "ideal":
"Raju Lama"}
{"input": [{"role": "system", "content": "A user will give you a English
transliteration phrase of Nepali song. Give the name of the singer or
band."}, {"role": "user", "content": "Aaja maan udhera bhagchha"}],
"ideal": "Udit Narayan"}
{"input": [{"role": "system", "content": "A user will give you a English
transliteration phrase of Nepali song. Give the name of the singer or
band."}, {"role": "user", "content": "Kaha Hola Ghar Bara"}], "ideal":
"Karma"}
{"input": [{"role": "system", "content": "A user will give you a English
transliteration phrase of Nepali song. Give the name of the singer or
band."}, {"role": "user", "content": "Khaseka Tara"}], "ideal":
"Albatross"}
  ```
</details>

---
## [Consensus-NLP/openai-evals](https://github.com/Consensus-NLP/openai-evals)@[7b4bd9439f...](https://github.com/Consensus-NLP/openai-evals/commit/7b4bd9439fce855cf52c93357fe3fe239d96abaf)
#### Sunday 2023-06-11 09:43:52 by AlexBuz

Add eval for finding leg of 45-45-90 triangle (#370)

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
isosceles-right-triangle

### Eval description

This evaluates the model's ability to solve for the length of a leg of
an isosceles right triangle given the length of the hypotenuse.

### What makes this a useful eval?

This task is easy for humans, as it simply requires dividing by the
square root of 2 (an operation which GPT-4 seems to be capable of).
However, GPT-4 often misjudges which side is the hypotenuse and ends up
with the wrong result. GPT-3.5-Turbo has a low accuracy (< 20%) on this
task. Although GPT-4 does better (based on my testing in ChatGPT Plus),
it is still far from perfect.

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
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In triangle FOX, angle F =
90º, angle O = 45º, and OX = 3√2. Solve for FX. Think step by step, and
then write your final answer in simplified form on a new line in this
format (where ? is your answer):\n<answer>FX = ?</answer>"}], "ideal":
["<answer>FX = 3</"]}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In triangle FOX, angle O =
45º, angle F = 90º, and OX = 3√2. Solve for FX. Think step by step, and
then write your final answer in simplified form on a new line in this
format (where ? is your answer):\n<answer>FX = ?</answer>"}], "ideal":
["<answer>FX = 3</"]}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In triangle JUY, angle J =
90º, angle U = 45º, and UY = 4√2. Solve for JY. Think step by step, and
then write your final answer in simplified form on a new line in this
format (where ? is your answer):\n<answer>JY = ?</answer>"}], "ideal":
["<answer>JY = 4</"]}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In triangle JUY, angle U =
45º, angle J = 90º, and UY = 4√2. Solve for JY. Think step by step, and
then write your final answer in simplified form on a new line in this
format (where ? is your answer):\n<answer>JY = ?</answer>"}], "ideal":
["<answer>JY = 4</"]}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In triangle JUY, angle J =
90º, angle U = 45º, and UY = 4. Solve for JY. Think step by step, and
then write your answer in simplified form on a new line in this format
(where ? is your answer):\n<answer>JY = ?</answer"}], "ideal":
["<answer>JY = 2√2</", "<answer>JY = 2sqrt(2)</", "<answer>JY =
2*sqrt(2)</", "<answer>JY = 2 * sqrt(2)</"]}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In triangle JUY, angle U =
45º, angle J = 90º, and UY = 4. Solve for JY. Think step by step, and
then write your answer in simplified form on a new line in this format
(where ? is your answer):\n<answer>JY = ?</answer"}], "ideal":
["<answer>JY = 2√2</", "<answer>JY = 2sqrt(2)</", "<answer>JY =
2*sqrt(2)</", "<answer>JY = 2 * sqrt(2)</"]}
  ```
</details>

---
## [kossiitkgp/docs](https://github.com/kossiitkgp/docs)@[a0c3bce015...](https://github.com/kossiitkgp/docs/commit/a0c3bce01594a96ccd834195ed255bacde8b3222)
#### Sunday 2023-06-11 10:28:55 by Arpit Bhardwaj

more on kwoc (#59)

* [WIP] more elaboration of processes

- Adding few new things which weren't here but I as a CTM experienced via myself or via my friends or seniors
- removed the point for backing up the database
- left is to mention about mid-evals qualification criteria.. mailing/updating dashboard whatever

* add: mid-evals criteria

* Apply suggestions from code review by harsh

Co-authored-by: Harsh Khandeparkar <shadowwarriorpro3003@gmail.com>

* update: website specifics and social media

---------

Co-authored-by: Harsh Khandeparkar <shadowwarriorpro3003@gmail.com>

---
## [enjarai/do-a-barrel-roll](https://github.com/enjarai/do-a-barrel-roll)@[db8711cfa4...](https://github.com/enjarai/do-a-barrel-roll/commit/db8711cfa4ceffb7d1562821d11ef00dd6da1bd7)
#### Sunday 2023-06-11 10:33:01 by enjarai

Yknow what, fuck you. *Makes your keyboard input logic context-sensitive*

---
## [Nimowa/tgstation](https://github.com/Nimowa/tgstation)@[c67d6a22a4...](https://github.com/Nimowa/tgstation/commit/c67d6a22a405f006a9d7a537dc35cecbdb65cfde)
#### Sunday 2023-06-11 10:47:03 by Kyle Spier-Swenson

fix stupid error message in delay pre-game (#75824)

tabbing out during init after hitting the verb, while you wait for the
server to un-lockup and present you with the prompt, and coming back in,
noticing you were too late, and cancelling out of the time prompt, only
to get told the round had already started, was kinda fucking lame. I
know, thats why i fucking hit cancel you fucking robit.

also makes the proc more early return

---
## [Nimowa/tgstation](https://github.com/Nimowa/tgstation)@[d01b433ab1...](https://github.com/Nimowa/tgstation/commit/d01b433ab12e7aa45416d42f9045f1135e545dae)
#### Sunday 2023-06-11 10:47:03 by Sealed101

Fixes colossus possessor crystal cockroaches/animals not dumping the user's body upon death/gibbing (#75843)

## About The Pull Request
Hooks the stasis closet thingamajing into `COMSIG_LIVING_DEATH` instead
of checking the animal's stat on `process()`, which makes possessed
animals properly dump the stasis closet's contents upon death or gibbing
(which is death but cooler).
yeah uh this method is hilarious but it does protect the user's body
quite reliably at least lol

## Why It's Good For The Game
Fixes #75829
also probably makes cockroach death saner in some unreported way, this
`. = ..()` vs `..()` is above my non-existent paygrade but it keeps
popping up from time to time

## Changelog
:cl:
fix: gibbing colossus possessor crystal possessed animals will no longer
stick the user's body and their stuff into the shadow realm. the animals
will properly drop your corpse when killed or gibbed
/:cl:

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [Harisali1234/Harisali1234](https://github.com/Harisali1234/Harisali1234)@[bce7974ccc...](https://github.com/Harisali1234/Harisali1234/commit/bce7974cccd0879a6c86a323a9c3be1863b507e5)
#### Sunday 2023-06-11 11:04:28 by Harisali1234

tour.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
        <h1>Welcome to Lahore!</h1>
        <p>Join us on an exciting tour of Lahore, the cultural heart of Pakistan.</p>
      
        <h2>Lahore Fort</h2>
        <p>Visit the Lahore Fort, also known as Shahi Qila, a UNESCO World Heritage Site showcasing stunning Mughal architecture.</p>
        <img src="lahore-pakistan-march-2019-view-fort-1355754446" alt="Lahore Fort">
      
        <h2>Badshahi Mosque</h2>
        <p>Explore the majestic Badshahi Mosque, an architectural masterpiece with elegant minarets and intricate marble work.</p>
        <img src="TXJEdxs5Hh4.html" alt="Badshahi Mosque">
      
        <h2>Old City</h2>
        <p>Get lost in the bustling streets and bazaars of the Old City, where you'll find vibrant colors, aromatic spices, and the famous Wazir Khan Mosque.</p>
        <img src="wazir-khan-mosque-lahore-pakistan-28th-1275202219" alt="Old City">
      
        <h2>Shalimar Gardens</h2>
        <p>Experience the enchanting Shalimar Gardens, a serene oasis of terraced lawns, fountains, and ancient trees.</p>
        <img src="imgres" alt="Shalimar Gardens">
      
        <h2>Food Street in Gawalmandi</h2>
        <p>Indulge in the mouthwatering Pakistani cuisine at Food Street, offering kebabs, biryanis, gol gappay, and more.</p>
        <img src="imgres" alt="Food Street">
      
        <h2>Lahore Museum</h2>
        <p>Discover the rich history and cultural heritage of Lahore at the Lahore Museum, home to art, artifacts, and historical relics.</p>
        <img src="imgres (1)" alt="Lahore Museum">
      
        <h2>Gulberg</h2>
        <p>Experience the modern side of Lahore in the vibrant neighborhood of Gulberg, with its upscale restaurants, trendy cafes, and boutique shops.</p>
        <img src="imgres (1)" alt="Gulberg">
      
        <p>Lahore is a city that seamlessly blends history with modernity, offering a unique experience to its visitors.</p>
      
        <footer>
          <p>Enjoy your tour of Lahore!</p>
        </footer>
      
      </html>
      
</body>
</html>

---
## [dddraxxx/evals](https://github.com/dddraxxx/evals)@[d0e7844c48...](https://github.com/dddraxxx/evals/commit/d0e7844c482b7b65961bc80dad64559ff8ffa488)
#### Sunday 2023-06-11 11:35:18 by Derek Pisner

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
## [dddraxxx/evals](https://github.com/dddraxxx/evals)@[fabca8cebb...](https://github.com/dddraxxx/evals/commit/fabca8cebb3f8e14d1f374e448533e0bde6e5a68)
#### Sunday 2023-06-11 11:35:18 by Nick Clyde

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
## [Drulikar/cmss13](https://github.com/Drulikar/cmss13)@[d1d23352eb...](https://github.com/Drulikar/cmss13/commit/d1d23352eb41452a98d0c66c7fbf5c5ea4143ffe)
#### Sunday 2023-06-11 11:49:14 by fira

Reduces SG Full Auto Scatter (#3556)

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

It's been bugging me for a long time, but when you fire for a good dozen
seconds with the standard issue smartguns, the bullets start scattering.
So, so far you'll say, good Fira, that's soulful!

However, we have no ACTUAL recoil or similar mechanic. So letting go of
the LMB for just even 20 miliseconds is enough to reset scatter to start
of firing. **It's just a noobtrap with zero real gameplay elements.**

This reduces the max scatter so that bullets don't just start (after
EIGHTY shots!) spraying a (roughly) 48° angle cone, but instead 12°
which mostly stays on the same actual turfs. At this value the targeting
impact is vastly minimized, but the projectile visuals retain
significant scattering.

I don't think this ACTUALLY qualifies as a "balance" change due to how
irrelevant the "mechanic" was, but i'll slap it on.

# Explain why it's good for the game
Less of a noobtrap and pointless purely mechanical micromanagement so
people can focus on playing the game.

I'd rather we get a recoil mechanic to make this meaningful but it's bit
of a bigger problem...

# Changelog
:cl:
qol: Reduced USCM SG max scattering on Full Auto fire so you don't have
to periodically let go of the fire button to keep it from firing way
wide.
/:cl:

---
## [ExactExampl/kernel_bonito-4.9](https://github.com/ExactExampl/kernel_bonito-4.9)@[fe021a62c2...](https://github.com/ExactExampl/kernel_bonito-4.9/commit/fe021a62c26b81f3038b914c83e343e3e6fe9bce)
#### Sunday 2023-06-11 12:15:46 by Angelo G. Del Regno

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

---
## [T6751/SERP-BlueMoon-Station-13](https://github.com/T6751/SERP-BlueMoon-Station-13)@[52eb909f42...](https://github.com/T6751/SERP-BlueMoon-Station-13/commit/52eb909f423900340814843d3223a7f3205add35)
#### Sunday 2023-06-11 12:24:51 by Tom

Makes Hell Microwaves Not Use Power (#67413) (#21210)

Hey there,

I was informed that the holodeck program Microwave Paradise would draw and suck power out of an APC. Didn't intend for that to happen, and while funny, I don't really want to arm the crew with le epic power sink with very little effort than pressing a button, or warranting this to eventually be locked to "dangerous" programs. So, let's change such that this subtype of microwaves that can not be constructed (only mapped/spawned) doesn't consume any power. I don't know why it drew off the nearest APC or how that works, but this seems to be alright.

It's not possible to deconstruct machinery spawned in at the Holodeck (which I verified while testing this PR), so do not worry about people using this to bypass the power economy for whzhzhzhz purposes.

Co-authored-by: san7890 <the@san7890.com>

---
## [godot-gonzago/gonzago-design](https://github.com/godot-gonzago/gonzago-design)@[233c8939cb...](https://github.com/godot-gonzago/gonzago-design/commit/233c8939cb4f324bdc88413b39ec1ee238df45f8)
#### Sunday 2023-06-11 12:31:03 by David Krummenacher

Fuck this shit. This is again very stupid and cumbersome and leads to nothing.

---
## [qqkookie/terminal](https://github.com/qqkookie/terminal)@[442432ea15...](https://github.com/qqkookie/terminal/commit/442432ea15241a3e9ee3d70c5c24e5565655e55b)
#### Sunday 2023-06-11 12:45:44 by Mike Griese

Fixes the wapproj fast-up-to-date check (#11806)

I'm working on making the FastUpToDate check in Vs work for the Terminal project. This is one of a few PRs in this area.

FastUpToDate lets vs check quickly determine that it doesn't need to do anything for a given project. 

However, a few of our projects don't produce all the right artifacts, or check too many things, and this eventually causes the `wapproj` to rebuild, EVERY TIME YOU F5 in VS. 

This third PR deals with the Actual fast up to date check for the CascadiaPackage.wapproj. When #11804, #11805 and this PR are all merged, you should be able to just F5 the Terminal in VS, and then change NOTHING, and F5 it again, without doing a build at all. 




The wapproj `GetResolvedWinMD` target tries to get a winmd from every cppwinrt
executable we put in the package. But we DON'T produce a winmd. This makes the
FastUpToDate check fail every time, and leads to the whole wapproj build
running even if you're just f5'ing the package. EVEN AFTER A SUCCESSFUL BUILD.

Setting GenerateWindowsMetadata=false is enough to tell the build system that
we don't produce one, and get it off our backs.

### teams chat where we figured this out

[3:38 PM] Dustin Howett
however, that's not the only thing that "GetTargetPath" checks.

[3:38 PM] Dustin Howett
oh yeah more info: wapproj calls GetTargetPath on all projects it references

[3:38 PM] Dustin Howett
when it calls GTP on WindowsTerminal.vcxproj it is getting back a winmd (!)


[3:39 PM] Dustin Howett
here's the magic

[3:39 PM] Dustin Howett
![image](https://user-images.githubusercontent.com/18356694/142945542-74734836-20d8-4f50-bf3a-be4e1170ae13.png)


[3:39 PM] Dustin Howett
it checks if any Link items specify GenerateWindowsMetadata

![image](https://user-images.githubusercontent.com/18356694/142945593-fd232243-0175-4653-8c34-cdc364a16031.png)

---
## [RandyMcMillan/git](https://github.com/RandyMcMillan/git)@[07f91e5e79...](https://github.com/RandyMcMillan/git/commit/07f91e5e79810a8f17de745d2d84c384add75f0a)
#### Sunday 2023-06-11 12:49:15 by Jeff King

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
## [Blacklion567/Little-Projects-HTML-CSS-JS](https://github.com/Blacklion567/Little-Projects-HTML-CSS-JS)@[6b3e25de8f...](https://github.com/Blacklion567/Little-Projects-HTML-CSS-JS/commit/6b3e25de8fa4c77c9ba558b135db510f2cddef94)
#### Sunday 2023-06-11 12:59:35 by Blacklion567

Little-Projects-HTML-CSS-JS

“If you’re going through hell, keep going.” – Winston Churchill

“Success is no accident. It is hard work, perseverance, learning, studying, sacrifice and most of all, love of what you are going or learning to do. ” – Edson Arantes do Nascimento – Pelé

“All happiness depends on courage and work.” – Honoré de Balzac

“Patience and perseverance have a magical effect before which difficulties disappear and obstacles vanish” – John Quincy Adams

“Procrastination makes easy things hard, hard things harder.” – Mason Cooley

“There are no traffic jams on the extra mile.” – Zig Ziglar

---
## [petre-symfony/api-platform-3-part-2-security-for-you-symfonycasts-june-2023](https://github.com/petre-symfony/api-platform-3-part-2-security-for-you-symfonycasts-june-2023)@[751697d2f4...](https://github.com/petre-symfony/api-platform-3-part-2-security-for-you-symfonycasts-june-2023/commit/751697d2f4baa373485d385101998f27da5f1c9f)
#### Sunday 2023-06-11 14:02:17 by Petre Ro

31.1 Totally Custom Fields

 Let's get wild. I want to add a totally custom, crazy new field to our DragonTreasure API that does not correspond to any property in our class. Well, actually, we learned in part 1 of this series that adding custom fields is possible by creating a getter method and adding a serialization group above it. But, that solution only works if we can calculate the field's value solely from the data on the object. If, for example, we need to call a service to get the data, then we're out of luck.

 Adding a new field whose data is calculated from a service is another trick up the custom normalizer's sleeve. And since we already have one set up, I thought we'd use it to see how this works.

 Testing for the IsMe Field
 - Go to DragonTreasureResourceTest and find testOwnerCanSeeIsPublishedField(). Rename this to testOwnerCanSeeIsPublishedAndIsMineFields()

 This is a bit silly, but if we own a DragonTreasure, we're going to add a new boolean property called $isMine set to true. So, down at the bottom, we'll say isMine and expect it to be true

 Copy that method name, then spin over and run this test:

  symfony php bin/phpunit --filter=testOwnerCanSeeIsPublishedAndIsMineFields
 Tada! It's null because the field doesn't exist yet.

 Returning the Custom Field
 - So how can we add this? Now that we've gone through the pain of getting the normalizer set up, it's easy! The normalizer system will do its thing, return the normalized data, then, between that and the return statement, we can... just mess with it!

 Copy the if statement from up here. I could be more clever and reuse code, but it's fine. If the object is a DragonTreasure and we own this DragonTreasure, we will say $normalized['isMine'] = true

 That's it! When we run the test:

  symfony php bin/phpunit --filter=testOwnerCanSeeIsPublishedAndIsMineFields

 All green!

 Custom Fields Missing in the Docs
 - But there's a practical downside to these custom fields: they will not be documented in our API. Our API docs have no idea that this exists!

 If you do need a super-duper custom field that requires service logic... and you do need it to be documented, you have two options. First, you could add a non-persisted isMe property to your class then populate it with a state provider. We haven't talked about state providers yet, but they're how data is loaded. For example, our classes are already using a Doctrine state provider behind the scenes to query the database. We'll cover state providers in part 3 of this series.

 The second solution would be to use the custom normalizer like we did, then try to add the field to the OpenAPI docs manually via the OpenAPI factory trick that we showed earlier.

 Next: suppose a user is allowed to edit something... but there are certain changes to the data that they are not allowed to make - like they could set a field to foo but they aren't allowed to change it to bar because they don't have enough permissions. How should we handle that? It's security meets validation.

---
## [LovliestPlant/tgstation](https://github.com/LovliestPlant/tgstation)@[1b5c0489a4...](https://github.com/LovliestPlant/tgstation/commit/1b5c0489a4088dca925ab061a389d95005c95820)
#### Sunday 2023-06-11 14:10:28 by san7890

`ex_act()` will work on basic mobs again (lol) + Unit Test (#74953)

basically ex_act's implementation on basic mobs would call parent and
then react to it's value, this is presumably to do the first check about
space vine mutations and whatever. the problem is that the `/mob/living`
implementation would itself also call parent, and that would always
return null because `/atom/proc/ex_act` doesn't have a set return value.
So, this simply would _always_ early return, with ex_act presumably
*never* working on basic mobs for at least four months now.

I decided to then change up the return values for pretty much all
implementations of `ex_act()` since there was no rhyme or reason to
returning null/FALSE/TRUE, and documenting why it's like that.

Just to make sure I wasn't breaking anything doing this (at least on
base implementations), I wrote a unit test for all of the three major
physical types in game (objs, mobs, turfs) because i am a paranoid
fuckar. we should be good to go now though.
## Why It's Good For The Game

i noticed this because placing c4's on sargeant araneus wouldn't
actually damage it whatsoever. now it actually does the stated 30
damage, but araneus has like 250 health so it doesn't actually matter in
the long run. whatever at least it does the damn 30 now.

also adds a unit test for this specific case as well as a range of other
cases to ensure this stuff doesn't silently break in this way anymore

---
## [hesh3am/Jenkins](https://github.com/hesh3am/Jenkins)@[9e163488c7...](https://github.com/hesh3am/Jenkins/commit/9e163488c753229846669eb44d12576c236f84ff)
#### Sunday 2023-06-11 14:14:11 by hesh3am

Create README.md

DEPRECATION NOTICE
This image has been deprecated for over 2 years in favor of the jenkins/jenkins:lts image provided and maintained by the Jenkins Community as part of the project's release process. The images found here have not received updates for over 2 years and will not receive any updates in the future.

Remaining tags are here only for historical reasons, none of them are supported and none of them should be used.

Supported tags and respective Dockerfile links
latest, 2.60.3 (Dockerfile)
alpine, 2.60.3-alpine (Dockerfile)
Quick reference
Where to get help:
the Docker Community Forums, the Docker Community Slack, or Stack Overflow

Where to file issues:
https://github.com/cloudbees/jenkins-ci.org-docker/issues

Maintained by:
the Jenkins Project

Supported architectures: (more info)
amd64

Published image artifact details:
repo-info repo's repos/jenkins/ directory (history)
(image metadata, transfer size, etc)

Image updates:
official-images PRs with label library/jenkins
official-images repo's library/jenkins file (history)

Source of this description:
docs repo's jenkins/ directory (history)

Supported Docker versions:
the latest release (down to 1.6 on a best-effort basis)

Jenkins
The Jenkins Continuous Integration and Delivery server.

This is a fully functional Jenkins server, based on the Long Term Support release http://jenkins.io/.

For weekly releases check out jenkinsci/jenkins

logo

How to use this image
docker run -p 8080:8080 -p 50000:50000 jenkins
This will store the workspace in /var/jenkins_home. All Jenkins data lives in there - including plugins and configuration. You will probably want to make that a persistent volume (recommended):

docker run -p 8080:8080 -p 50000:50000 -v /your/home:/var/jenkins_home jenkins
This will store the jenkins data in /your/home on the host. Ensure that /your/home is accessible by the jenkins user in container (jenkins user - uid 1000) or use -u some_other_user parameter with docker run.

You can also use a volume container:

docker run --name myjenkins -p 8080:8080 -p 50000:50000 -v /var/jenkins_home jenkins
Then myjenkins container has the volume (please do read about docker volume handling to find out more).

Backing up data
If you bind mount in a volume - you can simply back up that directory (which is jenkins_home) at any time.

This is highly recommended. Treat the jenkins_home directory as you would a database - in Docker you would generally put a database on a volume.

If your volume is inside a container - you can use docker cp $ID:/var/jenkins_home command to extract the data, or other options to find where the volume data is. Note that some symlinks on some OSes may be converted to copies (this can confuse jenkins with lastStableBuild links etc)

For more info check Docker docs section on Managing data in containers

Setting the number of executors
You can specify and set the number of executors of your Jenkins master instance using a groovy script. By default its set to 2 executors, but you can extend the image and change it to your desired number of executors :

executors.groovy

import jenkins.model.*
Jenkins.instance.setNumExecutors(5)
and Dockerfile

FROM jenkins
COPY executors.groovy /usr/share/jenkins/ref/init.groovy.d/executors.groovy
Attaching build executors
You can run builds on the master (out of the box) but if you want to attach build slave servers: make sure you map the port: -p 50000:50000 - which will be used when you connect a slave agent.

Passing JVM parameters
You might need to customize the JVM running Jenkins, typically to pass system properties or tweak heap memory settings. Use JAVA_OPTS environment variable for this purpose :

docker run --name myjenkins -p 8080:8080 -p 50000:50000 --env JAVA_OPTS=-Dhudson.footerURL=http://mycompany.com jenkins
Configuring logging
Jenkins logging can be configured through a properties file and java.util.logging.config.file Java property. For example:

mkdir data
cat > data/log.properties <<EOF
handlers=java.util.logging.ConsoleHandler
jenkins.level=FINEST
java.util.logging.ConsoleHandler.level=FINEST
EOF
docker run --name myjenkins -p 8080:8080 -p 50000:50000 --env JAVA_OPTS="-Djava.util.logging.config.file=/var/jenkins_home/log.properties" -v `pwd`/data:/var/jenkins_home jenkins
Passing Jenkins launcher parameters
Arguments you pass to docker running the jenkins image are passed to jenkins launcher, so you can run for example :

$ docker run jenkins --version
This will dump Jenkins version, just like when you run jenkins as an executable war.

You also can define jenkins arguments as JENKINS_OPTS. This is useful to define a set of arguments to pass to jenkins launcher as you define a derived jenkins image based on the official one with some customized settings. The following sample Dockerfile uses this option to force use of HTTPS with a certificate included in the image

FROM jenkins:1.565.3

COPY https.pem /var/lib/jenkins/cert
COPY https.key /var/lib/jenkins/pk
ENV JENKINS_OPTS --httpPort=-1 --httpsPort=8083 --httpsCertificate=/var/lib/jenkins/cert --httpsPrivateKey=/var/lib/jenkins/pk
EXPOSE 8083
You can also change the default slave agent port for jenkins by defining JENKINS_SLAVE_AGENT_PORT in a sample Dockerfile.

FROM jenkins:1.565.3
ENV JENKINS_SLAVE_AGENT_PORT 50001
or as a parameter to docker,

$ docker run --name myjenkins -p 8080:8080 -p 50001:50001 --env JENKINS_SLAVE_AGENT_PORT=50001 jenkins
Installing more tools
You can run your container as root - and install via apt-get, install as part of build steps via jenkins tool installers, or you can create your own Dockerfile to customise, for example:

FROM jenkins
# if we want to install via apt
USER root
RUN apt-get update && apt-get install -y ruby make more-thing-here
USER jenkins # drop back to the regular jenkins user - good practice
In such a derived image, you can customize your jenkins instance with hook scripts or additional plugins. For this purpose, use /usr/share/jenkins/ref as a place to define the default JENKINS_HOME content you wish the target installation to look like :

FROM jenkins
COPY plugins.txt /usr/share/jenkins/ref/
COPY custom.groovy /usr/share/jenkins/ref/init.groovy.d/custom.groovy
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/ref/plugins.txt
When jenkins container starts, it will check JENKINS_HOME has this reference content, and copy them there if required. It will not override such files, so if you upgraded some plugins from UI they won't be reverted on next start.

Also see JENKINS-24986

For your convenience, you also can use a plain text file to define plugins to be installed (using core-support plugin format). All plugins need to be listed as there is no transitive dependency resolution.

pluginID:version
credentials:1.18
maven-plugin:2.7.1
...
And in derived Dockerfile just invoke the utility plugin.sh script

FROM jenkins
COPY plugins.txt /usr/share/jenkins/plugins.txt
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt
Upgrading
All the data needed is in the /var/jenkins_home directory - so depending on how you manage that - depends on how you upgrade. Generally - you can copy it out - and then "docker pull" the image again - and you will have the latest LTS - you can then start up with -v pointing to that data (/var/jenkins_home) and everything will be as you left it.

As always - please ensure that you know how to drive docker - especially volume handling!

Image Variants
The jenkins images come in many flavors, each designed for a specific use case.

jenkins:<version>
This is the defacto image. If you are unsure about what your needs are, you probably want to use this one. It is designed to be used both as a throw away container (mount your source code and start the container to start your app), as well as the base to build other images off of.

jenkins:alpine
This image is based on the popular Alpine Linux project, available in the alpine official image. Alpine Linux is much smaller than most distribution base images (~5MB), and thus leads to much slimmer images in general.

This variant is highly recommended when final image size being as small as possible is desired. The main caveat to note is that it does use musl libc instead of glibc and friends, so certain software might run into issues depending on the depth of their libc requirements. However, most software doesn't have an issue with this, so this variant is usually a very safe choice. See this Hacker News comment thread for more discussion of the issues that might arise and some pro/con comparisons of using Alpine-based images.

To minimize image size, it's uncommon for additional related tools (such as git or bash) to be included in Alpine-based images. Using this image as a base, add the things you need in your own Dockerfile (see the alpine image description for examples of how to install packages if you are unfamiliar).

License
View license information for the software contained in this image.

As with all Docker images, these likely also contain other software which may be under other licenses (such as Bash, etc from the base distribution, along with any direct or indirect dependencies of the primary software being contained).

Some additional license information which was able to be auto-detected might be found in the repo-info repository's jenkins/ directory.

As for any pre-built image usage, it is the image user's responsibility to ensure that any use of this image complies with any relevant licenses for all software contained within.

---
## [EOT3000/NewMod](https://github.com/EOT3000/NewMod)@[3f55bed279...](https://github.com/EOT3000/NewMod/commit/3f55bed2792cfc6b47a7a90ab540d209a54578ec)
#### Sunday 2023-06-11 15:12:36 by EOT3000

currently extremely broken, will not compile, but this is my fork so fuck you

---
## [Sebastiengote/-48660708311](https://github.com/Sebastiengote/-48660708311)@[d88177b20b...](https://github.com/Sebastiengote/-48660708311/commit/d88177b20b893ca59fcf952ae14a62f08d8de4e5)
#### Sunday 2023-06-11 15:38:54 by Sebastiengote

Create Renee O’Brien 

Legends says that a purple door means a witch lives there. Well, in a place this overgrown, ancient looking, and magical, who else would live here?
Fairytaleasfuck is a place to post and escape the daily boredom of life and take a few … more
Visit save 
Share your feedback 
Spencer & wedekind

---
## [Updated-NoCheatPlus/NoCheatPlus](https://github.com/Updated-NoCheatPlus/NoCheatPlus)@[4817eed02e...](https://github.com/Updated-NoCheatPlus/NoCheatPlus/commit/4817eed02e99117db83a552b0b2a3979ef072d21)
#### Sunday 2023-06-11 15:49:48 by Lysandr0

Minor refactor for moving checks, rename Folia class, integrate Gutenberg as an ordinary check.

Move hard-coded magic into its own package (envelope); move checks.moving.magic class to the moving utilities package; split envelopes methods into its own class (PlayerEnvelopes); BounceUtil -> BounceHandler and to the envelope class; BounceType -> to the checks.moving.model package.

* Renamed Folia class to "SchedulerHelper" (name is up to debate, feel free to add)

* Gutenberg won't check for availability anymore. The event was introduced in 1.5 and NCP doesn't support versions lower than that anymore.

* Move "honeyBlockSidewayCollision" method to PlayerEnvelopes.

* Fix compilation errors in RichBoundsLocation and get rid of unused method.

* Get rid of the "split move" flag: too internal of an option and should never be disabled anyway.

* Clarify docs

* LiftOffEnvelope:
-Get rid of min/max jump distinction.
-Decrease normal jump height down to 1.26.

* SurvivalFly: various adjustments... Key change are:
 -The riddance of vAcc. Useless with the upcoming vDistRel rework;
-Unbind to the horizontal-push-speed mechanic from hard-coded magic. (Please Asofold for the love God why did you not document this kind of stuff... Why was it needed);
-Merge vDistWeb, vDistLevitation, vDistBush into vDistRel, climbables and powder snow are still handled in their respective methods because we are restricted by NCP's current  infrastructure and we cannot predict those two (powder snow in particular)
-Move honeyBlock collision to richboundslocation.

* RichEntityLocation:
-Force legacy players to have vines attached to a solid block to climb up.
-Check for client version for fullHeight setting as well.
-Move liquid pushing stuff to RuchEntityLocation

---
## [FernandoJ8/tgstation](https://github.com/FernandoJ8/tgstation)@[2aaafd9a67...](https://github.com/FernandoJ8/tgstation/commit/2aaafd9a67c270fa0772cd9beffb6789d53750e3)
#### Sunday 2023-06-11 15:49:53 by TheVekter

Replaces the syndicate corpse Legions can drop with one without a MODSuit (#75700)

## About The Pull Request
This is part of a pass I'm working on doing where I go through and
remove instances of antag gear outside of their normal context. This is
mostly going to involve replacing space/Lavaland ruin gear with
something close to the same power level but not distinctly something
only antags should be able to get. I want to keep ruins rewarding but I
don't want explicit antag gear to be something you can obtain without
needing an uplink.

The first part of this is me removing the MODSuit from the syndicate
operative corpse. The new one drops a turtleneck, a syndicate gas mask,
and gripper gloves.

## Why It's Good For The Game
It's my opinion that antag gear should probably stay in antag hands
unless you manage to kill one or steal an uplink. The main impetus for
this was a discussion I had a while back about how blood red hardsuits
used to _just_ be an antag thing. I kind of miss that general feeling of
paranoia that came from seeing someone wearing it, as opposed to seeing
it these days and just thinking "Yeah, it's probably someone who got it
from space".

In this specific instance, Syndicate MODSuits are pretty strong anyway
and, regardless of the low odds of getting one, I really don't think it
should be available as loot off a fairly easy-to-kill mob.

## Changelog
:cl:
balance: Syndicate corpses dropped from killing a Legion no longer come
with a MODSuit.
/:cl:

---
## [tikimcfee/LookAtThat](https://github.com/tikimcfee/LookAtThat)@[3299dc7cf0...](https://github.com/tikimcfee/LookAtThat/commit/3299dc7cf02aa321678b564bb9fb71496549d7db)
#### Sunday 2023-06-11 15:56:44 by Ivan Lugo

- The world is full of beautiful things and terrible things. It is full of happiness and sadness, pain and pleasure. It is full of all things good and all things evil. It is whole and it is fragmented.
- There is no is.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[5a34f44b16...](https://github.com/treckstar/yolo-octo-hipster/commit/5a34f44b16fc34edf49f9513b2e22c9c3a18df99)
#### Sunday 2023-06-11 16:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [GeoB99/reactos](https://github.com/GeoB99/reactos)@[b61a29d56a...](https://github.com/GeoB99/reactos/commit/b61a29d56a2153c3a3b7fa6dfbffd7473bc97c8c)
#### Sunday 2023-06-11 16:23:46 by George Bișoc

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

Another important note is that the added code grew up the binary size of x64 FreeLdr and that makes a PE image check fail because the bootloader is too large. Currently such code is disabled for AMD64, until
a real fix comes into place.

---
## [Kneba/platform_kernel_asus_sdm660](https://github.com/Kneba/platform_kernel_asus_sdm660)@[96f5f25fdf...](https://github.com/Kneba/platform_kernel_asus_sdm660/commit/96f5f25fdfe574929ef0dea4512c12efaaf3cce2)
#### Sunday 2023-06-11 17:33:40 by George Spelvin

lib/sort: make swap functions more generic

Patch series "lib/sort & lib/list_sort: faster and smaller", v2.

Because CONFIG_RETPOLINE has made indirect calls much more expensive, I
thought I'd try to reduce the number made by the library sort functions.

The first three patches apply to lib/sort.c.

Patch #1 is a simple optimization.  The built-in swap has special cases
for aligned 4- and 8-byte objects.  But those are almost never used;
most calls to sort() work on larger structures, which fall back to the
byte-at-a-time loop.  This generalizes them to aligned *multiples* of 4
and 8 bytes.  (If nothing else, it saves an awful lot of energy by not
thrashing the store buffers as much.)

Patch #2 grabs a juicy piece of low-hanging fruit.  I agree that nice
simple solid heapsort is preferable to more complex algorithms (sorry,
Andrey), but it's possible to implement heapsort with far fewer
comparisons (50% asymptotically, 25-40% reduction for realistic sizes)
than the way it's been done up to now.  And with some care, the code
ends up smaller, as well.  This is the "big win" patch.

Patch #3 adds the same sort of indirect call bypass that has been added
to the net code of late.  The great majority of the callers use the
builtin swap functions, so replace the indirect call to sort_func with a
(highly preditable) series of if() statements.  Rather surprisingly,
this decreased code size, as the swap functions were inlined and their
prologue & epilogue code eliminated.

lib/list_sort.c is a bit trickier, as merge sort is already close to
optimal, and we don't want to introduce triumphs of theory over
practicality like the Ford-Johnson merge-insertion sort.

Patch #4, without changing the algorithm, chops 32% off the code size
and removes the part[MAX_LIST_LENGTH+1] pointer array (and the
corresponding upper limit on efficiently sortable input size).

Patch #5 improves the algorithm.  The previous code is already optimal
for power-of-two (or slightly smaller) size inputs, but when the input
size is just over a power of 2, there's a very unbalanced final merge.

There are, in the literature, several algorithms which solve this, but
they all depend on the "breadth-first" merge order which was replaced by
commit 835cc0c8477f with a more cache-friendly "depth-first" order.
Some hard thinking came up with a depth-first algorithm which defers
merges as little as possible while avoiding bad merges.  This saves
0.2*n compares, averaged over all sizes.

The code size increase is minimal (64 bytes on x86-64, reducing the net
savings to 26%), but the comments expanded significantly to document the
clever algorithm.

TESTING NOTES: I have some ugly user-space benchmarking code which I
used for testing before moving this code into the kernel.  Shout if you
want a copy.

I'm running this code right now, with CONFIG_TEST_SORT and
CONFIG_TEST_LIST_SORT, but I confess I haven't rebooted since the last
round of minor edits to quell checkpatch.  I figure there will be at
least one round of comments and final testing.

This patch (of 5):

Rather than having special-case swap functions for 4- and 8-byte
objects, special-case aligned multiples of 4 or 8 bytes.  This speeds up
most users of sort() by avoiding fallback to the byte copy loop.

Despite what ca96ab859ab4 ("lib/sort: Add 64 bit swap function") claims,
very few users of sort() sort pointers (or pointer-sized objects); most
sort structures containing at least two words.  (E.g.
drivers/acpi/fan.c:acpi_fan_get_fps() sorts an array of 40-byte struct
acpi_fan_fps.)

The functions also got renamed to reflect the fact that they support
multiple words.  In the great tradition of bikeshedding, the names were
by far the most contentious issue during review of this patch series.

x86-64 code size 872 -> 886 bytes (+14)

With feedback from Andy Shevchenko, Rasmus Villemoes and Geert
Uytterhoeven.

Link: http://lkml.kernel.org/r/f24f932df3a7fa1973c1084154f1cea596bcf341.1552704200.git.lkml@sdf.org
Signed-off-by: George Spelvin <lkml@sdf.org>
Acked-by: Andrey Abramov <st5pub@yandex.ru>
Acked-by: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Reviewed-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Cc: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Cc: Geert Uytterhoeven <geert@linux-m68k.org>
Cc: Daniel Wagner <daniel.wagner@siemens.com>
Cc: Don Mullis <don.mullis@gmail.com>
Cc: Dave Chinner <dchinner@redhat.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Dede Dindin Qudsy <xtrymind@gmail.com>
Signed-off-by: Kneba <abenkenary3@gmail.com>

---
## [abesto/ts-bindgen](https://github.com/abesto/ts-bindgen)@[076b94a2e6...](https://github.com/abesto/ts-bindgen/commit/076b94a2e62cd490d94fd1c62f28c2863a77b897)
#### Sunday 2023-06-11 18:58:36 by Zoltán Nagy

Horrible hack: kinda sorta support template literals

Currently string literals are represented as a `String` in Rust,
with no compile-time checking of the values. As long as this is the
case, template literals can be "implemented" by just pretending
they are `String`s as well.

This is horrible, but it doesn't *decrease* type safety, and allows
importing type definitions using template literals.

While we're at it, let's also flatten unions of strings into a single
`String`. There's no value gained by generating an enum with a single
`String(String)` variant.

---
## [Onule/TaleStation](https://github.com/Onule/TaleStation)@[46929a3617...](https://github.com/Onule/TaleStation/commit/46929a3617536d96093d128a193a935cad766635)
#### Sunday 2023-06-11 19:15:39 by TaleStationBot

[MIRROR] [MDB IGNORE] Welding Fuel Tanks now log_bomber when hit by projectile (#6168)

Original PR: https://github.com/tgstation/tgstation/pull/75885
-----

## About The Pull Request

This was intended behavior, but I think a lot of bullshit over the years
sorta corrupted this proc's intention. Anyways, we just override the
whole ass proc for this one check, give a good return value (or at least
the same one that we were always giving) if our criteria is met, rather
than deal with the problems that parent was feeding us.


![image](https://github.com/tgstation/tgstation/assets/34697715/e2b39140-d365-43aa-8834-2740f9fa5036)

The specific issue here was that the parent of `bullet_act()` was
invoking `take_damage()` which prematurely invoked `boom()` which
invokes `qdel()`, meaning that the `QDELETED()` check would _always_
early return without fail every time.

Let's just do our own thing here.
## Why It's Good For The Game


![image](https://github.com/tgstation/tgstation/assets/34697715/ca8fdeba-9f5d-4bed-afba-88824d389cfb)

Intended behavior actually works.
## Changelog
:cl:
admin: Shooting a welding fuel tank (big or small) with a projectile
will now accurately post to list_bombers with the name of the person who
shot the projectile from the gun. If you don't know how to list-bombers,
it will also be present in game.log for your viewing pleasure.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [Rat-Time/Liberty-Station-13](https://github.com/Rat-Time/Liberty-Station-13)@[0f74820c9d...](https://github.com/Rat-Time/Liberty-Station-13/commit/0f74820c9d04762ac5b06907e6eb5207be80f136)
#### Sunday 2023-06-11 19:44:20 by ThePainkiller

Fixes upon fixes and more

- Fixes exploit on medical fabricator that allowed it to take any disk
- Consequently, fixes general autolathe's capacity to receive medical disks as was... intended?
- Comments out cartographer's seal and pyramid anomalies
- Bruise packs and the like should now cost their exact amount of materials (and chemicals) to print, no longer accruing massive costs
- New: Gate floodlights, they're static, fixed, brighter, and can't have their cells taken out (they come with a large posi). To illuminate the fence at night. TODO: Make them create a directional light spot like flashlights
- Wallets can now take syrettes
- Bone gel now made out of biomatter
- Fixes extant references to Lonestar on the vault's gold shovel
- Adds and renames missing stamps to heads of staff offices
- New functionality: CTRL SHIFT clicking a PDA ejects its pen
- New functionality: Alt clicking a dropper selects transfer amount
- Ammo kits (and the crafting table) can now make caseless ammo
- Fixes Ugil's mag overlay issue
- Changes up many, many weapon's firing sounds to be more fitting
- Fixes self heating coffee doing eating sounds
- Adds quality of life sounds to MRE-like foods, when opened, heated up, and finished heating
- Beautification of the Custodians of the Bonfire's Stronghold, removing references to church, new areas as well
- Changed the lift's walls' names from the mines from "The Rocinante" to "Elevator" proper
- Many musical instruments and loot added to the map
- Bar now has a piano!

---
## [ItzJustGig/projekt-kepler](https://github.com/ItzJustGig/projekt-kepler)@[95c6bb7c82...](https://github.com/ItzJustGig/projekt-kepler/commit/95c6bb7c82c2bbead9adf655ed95e9728a4a9c80)
#### Sunday 2023-06-11 19:49:07 by gig

Enya Release; Balance; Bug Fix

FIX
-DOTs were not applying on allies
-If an enemy was dead and a AOE move was used, the target would die aswel
-If a passive had shield as 2nd scaling, it would be shown as null on the tooltip

CHAMPIONS
NEW
-Enya

PASSIVE
-Leaf Being
FIX
name in pt change from "Ser de Plata" to "Ser de Planta"

-Sharpshooter
TRUE
12%->14% attack damage

-Holding the Line
SMALL SHIELD
3->5 base shield
8%->9% damage resistance

-Combat Repair
shield is earned over 4->3 turns

NEW
-Druid
The user’s healing is increased by +(4% of the user’s magic power)%, when an ally is affected by Blood, Allergy, Poison or Cripple, the user heal bonus 15 health on that target

-Elfic Magic
Every 9 magic or ranged moves the next will crit and deal bonus 8 + (22% magic power) + (18% attack damage) magic damage. (crit applies on magic damage aswell)

MOVES
-Spores
25->40 mana cost
EFFECT
100%->80% chance
2-3->1-3 turns duration
MAGIC
x 1.9% cur hp
45%->55% magic power

-Firebreath
MAGIC
6->5 base damage
105%->85% magic power

-Accurate Shot
PHYSICAL
38%->40% attack damage
MAGIC
70%->50% magic power

-Silent Shot
PHYSICAL
40%->50% attack damage

-Force Field
SHIELD
45->55 base shield
25%->30% magic resistance
80%->85% magic power

-Keen Eye
PARTICLE
target have keeneye particle

-Glare
PARTICLE
target have keeneye particle
user have keeneye particle

NEW
-Bloom
-Barrage
-Gale Burst
-Yggdrasil's Blessing

---
## [thatoneyeeter/cmss13](https://github.com/thatoneyeeter/cmss13)@[d5b1193802...](https://github.com/thatoneyeeter/cmss13/commit/d5b119380250ea512db2a5319e36592c7f604250)
#### Sunday 2023-06-11 20:03:41 by fira

FOB Tents  (#3509)

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

Sprites stolen from thwomper and sammy, available NOW with game code!

Adds a few tents to be used in FOB building, mainly for organizational
purposes but also providing small gameplay benefits. At current the main
goal is to incentive usage to organize and liven up FOB, so the buffs
are rather small.

There are 4 tent types:
* The Command Tent is a 2x3 structure that comes bundled with an
overwatch console, a phone, and two (2) chairs.
* The Medical Tent is a 2x3 structure that comes with a NanoMED, 2
roller beds, and slightly buffs surgery (10% less time taken, and a very
token pain/failure chance improvement)
* The Requisitions Tent is a 4x3 structure that comes with a phone,
rack, desks, and a variant of the old APC vendor that can stock
materials and regular ammunition. The vendor starts empty, save for some
tables/racks/paperwork for organization purposes. It is only useable
with requisitions access.
* The Big Tent is a bigger tent for all your organizational needs: 3x3.
Get creative.

The tents also provide decent additional protection against cold
environements. Unfortunately, rain/snow will visually pour through it, i
can't do much about that.

The tents are extremely vulnerable to explosives and xeno claws. For
simplicity and technical reasons, they are currently NON REDEPLOYABLE
and NON REPLACEABLE. The tent destruction will destroy/disable linked
objects (console/vendor etc). Be mindful of where you place them.

**Mind that the tents may not work out for all LZ FOBs due to the
required space. I expect people will find ways to make it work anyway
but it might take a while.**

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

I'm lazyyy i forgot and already closed the game... If you actually want
em bug me and i'll add em
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

:cl: Firartix , Thwomper and Sammy
add: Added four types of tents to liven up FOB. They provide cold
protection and benefits depending on their type. The tents spawn in
Requisitions roundstart near the mortar. They're vulnerable to
explosives and xenomorphs, and NON REPLACEABLE. Mind where you put them!
add: The Command tent comes equipped with an overwatch console and a
phone.
add: The Medical tent provides a small boost to surgery speed/pain
carried out inside it.
add: The Requisitions tent provides a restockable vendor, desk, and
furniture for organization.
add: The Big tent is just a big tent, and provides you a slate to
organize the way you want.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: harryob <me@harryob.live>

---
## [DogWithAHat/roblox-repainted](https://github.com/DogWithAHat/roblox-repainted)@[3ca6f874ce...](https://github.com/DogWithAHat/roblox-repainted/commit/3ca6f874ce4744695b74cdf5b77d3f73940f6c2f)
#### Sunday 2023-06-11 20:03:48 by shneeble gleebis

got rid of a piece of folder fodder 

fuck you im calling it folder fodder from now on

---
## [OriSketchy/Wild-Isles](https://github.com/OriSketchy/Wild-Isles)@[41e456ddc9...](https://github.com/OriSketchy/Wild-Isles/commit/41e456ddc9f6edf541b29932dc158bdc1052597c)
#### Sunday 2023-06-11 20:54:24 by OriSketchy

Added comments

its very simple code but i have coded at horribly late hours of the night before so id rather be safe than sorry

---
## [GunJumpers/GunJumpers](https://github.com/GunJumpers/GunJumpers)@[c8cce03922...](https://github.com/GunJumpers/GunJumpers/commit/c8cce03922777bb6e6540a22828aeb4d742865fe)
#### Sunday 2023-06-11 21:26:38 by silmist

fuck my stupid baka life

pace drive
auto repair
cursor

---
## [ttztony/gorilla](https://github.com/ttztony/gorilla)@[f3ce849a8c...](https://github.com/ttztony/gorilla/commit/f3ce849a8c46f5683477ff26ec34dc04518c294b)
#### Sunday 2023-06-11 22:01:55 by Shishir Patil

Releasing Torch and TF weights 🚀  (#16)

In this PR we release the weights for Gorilla 0-shot model for Torch Hub
and Tensorflow Hub APIs 🎉

It chooses from 626 (exhaustive) TensorFlow v2 APIs, and 94 (exhaustive)
Torch Hub in a 0-shot fashion (without any retrieval). In the spirit of
being open, we do not filter, nor carry out any post processing either
to the prompt nor response 🎁 We would like to remind the community that
neither of `gorilla-7b-hf-v0`, `gorilla-7b-tf-v0`, nor
`gorilla-7b-th-v0` have any generic chat capability. We do have a model
with all the 1600+ APIs which also has generic chat capability, which we
release slowly to accommodate server demand.

You can play around with Gorilla either through our hosted colab (OpenAI
Chat completion API compliant) or you can download and run it locally.

Thank you for all the comments and suggestions so far! Keep them
coming!!!

🚀 🚀 🚀

---
## [Zeden19/mappingSmash](https://github.com/Zeden19/mappingSmash)@[1fb8ac8754...](https://github.com/Zeden19/mappingSmash/commit/1fb8ac87543357b70f5926d82b6fdc1eca003a1d)
#### Sunday 2023-06-11 22:51:56 by Zeden19

Implement basic form of python implementation

Basically we know do it all from javascript (i fucking hate javascript
so fucking much). There are still a few bugs and quirks that need to be
filled out.

Fuck this stupid ass javascript ass dumbass fucking language

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[d1cb2e8751...](https://github.com/tgstation/tgstation/commit/d1cb2e87519869b5c7baafd66d0e2454cfa6282b)
#### Sunday 2023-06-11 23:43:30 by Rhials

New planetary exclusive random event/unfavorable situation, Chasmic Earthquake (#75864)

## About The Pull Request


https://github.com/tgstation/tgstation/assets/28870487/2451bc69-db1e-420d-9a18-2f899ca65427

This introduces a new unfavorable situation (non-antagonist random
events that dynamic triggers under certain circumstances), restricted to
planetary maps (Icebox). An earthquake occurs, felt by everyone on the
map, forming a fault that tears the a hole somewhere on the station.

The fault zone is indicated by shaking tiles, which gives a chance
(about 30 seconds) for you to move your machinery/property/crewmembers
out of the way. If you're on those tiles when the fault forms, get ready
to take a nasty fall.

Anything caught in the fault zone as it collapses inward will be
destroyed, violently, _before_ being dropped down into the z-level
below.


![image](https://github.com/tgstation/tgstation/assets/28870487/56916c9f-c8da-4ffb-9d8b-7e940e92bbc2)

These can also happen as a random event, however their rarity is on-par
with that of a meteor storm.

This also adds a helper for finding a midpoint turf between two provided
turfs, thanks to ZephyrTFA.

This idea basically possessed me over the course of a few days, and I
found myself unable to work on anything else until I had it complete.
I'm glad its done.
## Why It's Good For The Game

Gives Icebox its own big "environmental disaster" event. I'm hoping it
isn't received as being too destructive, but mind that this is meant to
be an equal to the dreaded meteor storm.

Also makes it so that unfavorable events aren't a coinflip between a
portal storm/rod on planetary maps.
## Changelog
:cl: Rhials
add: Chasmic Earthquake random event, exclusive to Icebox. Tears a huge
chasm in the hull of the station. Watch out for shaking tiles!
sound: Adds sounds for distant rumbling, metal creaking, and rubble
shaking.
imageadd: Achievement icon for getting sucked up in an earthquake chasm.
/:cl:

---
## [Cthulhu80/cmss13](https://github.com/Cthulhu80/cmss13)@[e8f53984c1...](https://github.com/Cthulhu80/cmss13/commit/e8f53984c1edd98c25b4c3199a6a5363eaa26869)
#### Sunday 2023-06-11 23:58:48 by morrowwolf

Warrior Nerf (#3424)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

This PR removes cooldown reduction on slash.

This PR slightly lowers fling and punch cooldowns.

This PR lowers fling stun to a micro stun and adds a slow.

This PR decreases lunge range to 4 tiles.

As a reminder design feedback and balance concerns go here:
https://forum.cm-ss13.com/w/pr-feedback/steps/step_1

# Explain why it's good for the game

Warrior rework has been on my mind for a while. I'm not quite sure how I
want to do it. The cooldowns on abilities and the abilities themselves
are incredibly powerful crowd control and just a few warriors can do
immense damage to large groups of marines. It's just... not in a great
place for a T2 and sadly I don't have a thorough game plan yet to rework
it into something more bearable while equally enjoyable to play. In the
mean time, this is what we're getting. Am I promising a rework in the
near future? Not really. It's on my list somewhere. Does warrior need
some changing around? Yeah.

Overall, this should make warrior a bit more bearable. We'll see. More
changes as testing goes.

# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

:cl: Morrow
balance: Removes warrior cooldown reduction on slash
balance: Warrior slightly lowered fling and punch cooldowns
balance: Lowers fling stun to a micro stun and adds a slow
balance: Decreases warrior lunge range to 4 tiles
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---

