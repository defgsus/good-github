## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-05-31](docs/good-messages/2023/2023-05-31.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,048,773 were push events containing 3,322,968 commit messages that amount to 269,213,971 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 64 messages:


## [1glitchycent/tgstation](https://github.com/1glitchycent/tgstation)@[3fdd716da5...](https://github.com/1glitchycent/tgstation/commit/3fdd716da5bfd2aab2be37489b4ac39f4be7e632)
#### Wednesday 2023-05-31 00:40:31 by Cheshify

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
## [1glitchycent/tgstation](https://github.com/1glitchycent/tgstation)@[43473a4dac...](https://github.com/1glitchycent/tgstation/commit/43473a4dac07c40faed45808b61b9c6de46ffcb6)
#### Wednesday 2023-05-31 00:40:31 by san7890

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
## [Addust/tgstation](https://github.com/Addust/tgstation)@[56d960a763...](https://github.com/Addust/tgstation/commit/56d960a7630d0b03bfcd59c073b29393a70a1891)
#### Wednesday 2023-05-31 00:59:15 by GoldenAlpharex

Wintercoats can now be zipped and unzipped through alt-click and separates the hood sprites from the jacket sprites (#74886)

## About The Pull Request
The title says it all, really.

~~Initially, I was only going to do it for all wintercoats, but then I
figured I might as well bring it down to all of `/hooded`, just so other
suits could benefit from it, since that behavior came from there anyway.
Does that mean that it does nothing for some of them? Yes, it does. Does
that justify having another variable to tell whether or not that should
be possible? In my humble opinion, not really, but I'm not against it if
it's requested.~~

~~That functionality was intentionally removed from the Void Cloak, as
there would be balance implications (since bringing up the hood makes
the whole cloak invisible, which you could skirt by just "zipping" it,
which also makes it invisible.~~

~~The sprites were already there, so this change was very simple to do.
Simply unties the zipped up look from the fact that the hood is up.
However, toggling the hood forces the zipping/unzipping, just so there's
no balance implications involved. It's just simpler that way.~~

So, I ended up going back and changing the sprites so that the hoods
would no longer be baked into the jacket's sprites, so that they could
be done as overlays instead, which ended up solving my problem with
hoods not being there on zipped-up versions.

For now, it's been made on winter coats only, but it shouldn't be that
difficult to bring it back down to the `/hooded` level. I just didn't
want to bother touching up the sprites down there, as it already took me
like 2-3 hours touching up the sprites of the winter coats alone.

I also took the decision to make it so EVA winter coats used the regular
winter coat's sprites, because they had special ones that just looked
like worse versions of the original, without anything special going on
for them. It was just a straight downgrade compared to the base sprite,
in my opinion.

There's still issues with the custom winter coat, in that the hood isn't
made into an overlay for it yet (and that'll require an extra bit of
logic to make it work, too), but it was already an issue before, the
hood is always present on the current version of the custom winter coat.

There's still a handful (sadly, most) of the winter coats that don't
properly reflect on their obj sprites when they're opened versus when
they're closed, but that's due to an initial spriter oversight, and not
to my doing. The open versions were just left as closed on many of them,
and I simply don't have the patience nor the appropriate skills to edit
that many coats that way.

## Why It's Good For The Game
Now you can be stylish with or without the hoodie!

![image](https://user-images.githubusercontent.com/58045821/233544697-cc821c3a-d965-4d96-af44-c44ff866496f.png)

![image](https://user-images.githubusercontent.com/58045821/233544711-da956b6b-44c4-4903-a34f-4d2890abc781.png)

![image](https://user-images.githubusercontent.com/58045821/233544717-b5221b04-0e6d-4931-83d0-d56fdac60ec3.png)


According to ChatGPT, with one small tweak (thanks Opera GX for the
suggestion):

> Zipped and unzipped through alt-click, winter coats can now be. Hmm,
stylishly warm, you shall be. Feel like a Spaceman, you will. Use the
Force, to zip and unzip, you must. Look cool, you will. Yes, hmmm.

## Changelog

:cl: GoldenAlpharex, ChatGPT for the first changelog entry (slightly
edited)
qol: Zipped and unzipped through alt-click, winter coats can now be.
Hmm, stylishly warm, you shall be. Feel like a Spaceman, you will. Use
the Force, to zip and unzip, you must. Look cool, you will. Yes, hmmm.
image: Winter coats no longer have their hood baked into their jacket's
sprite, both in item form and when worn.
fix: Updated the Icebox EVA winter coats (the Endotherm winter coats) to
use the same sprites as the regular winter coats.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [streamlit/streamlit](https://github.com/streamlit/streamlit)@[c464422e1b...](https://github.com/streamlit/streamlit/commit/c464422e1bbea66b3184769ea22599356d710f9a)
#### Wednesday 2023-05-31 01:10:55 by Danny Wolf

Upgrade react-range to fix memory usage of sliders (#6764)

As mentioned in
https://blog.streamlit.io/six-tips-for-improving-your-streamlit-app-performance/
memory usage struggles in the browser if you have large ranges:

> Due to implementation details, high-cardinality sliders don't suffer
> from the serialization and network transfer delays mentioned earlier,
> but they will still lead to a poor user experience (who needs to
> specify house prices up to the dollar?) and high memory usage. In my
> testing, the example above increased RAM usage by gigabytes until the
> web browser eventually gave up (though this is something that should
> be solvable on our end. We'll look into it!)

This was caused by a bug in react-range, which I fixed last year.
https://github.com/tajo/react-range/pull/178

At the time, I had figured it would get picked up by a random yarn
upgrade and didn't worry too much about it.
But, apparently yarn doesn't really have an easy way of doing upgrades
of transitive dependencies (see https://github.com/yarnpkg/yarn/issues/4986)?
I took the suggestion of someone in that thread to delete the entry and
let yarn regenerate it.

Some technical details about the react-range fix from the original
commit message (the "application" is a streamlit app):

> We have an application that uses react-range under the hood, and we
> noticed that a range input was taking 2GB of RAM on our machines. I
> did some investigation and found that regardless of whether the marks
> functionality was being used, refs were being created for each
> possible value of the range.

> We have some fairly huge ranges (we're using the input to scrub a
> video with potential microsecond accuracy), and can imagine that
> other people are affected by the previous behavior. This change
> should allow us to continue using large input ranges without
> incurring a memory penalty.

---
## [NeonNik2245/Skyrat-tg-tests](https://github.com/NeonNik2245/Skyrat-tg-tests)@[7dad8c75ca...](https://github.com/NeonNik2245/Skyrat-tg-tests/commit/7dad8c75cac06a405dc3c30a5cbc31919f33ff13)
#### Wednesday 2023-05-31 01:22:26 by SkyratBot

[MIRROR] Adds a eye-dropper right-click function to the painting canvas. [MDB IGNORE] (#21411)

* Adds a eye-dropper right-click function to the painting canvas. (#75571)

## About The Pull Request
Having used the painting UI to kill some time during long rounds for a
decent chunk of the past year, the need of a quicker and less tedious
way to fix a misclick or mistake like drawing over the wrong pixel has
become clear to me, as well as getting some feedback on the palette
component I made last year.

As the title suggests, this PR adds an eye-dropper function to the
canvas. Right-Click a pixel on the canvas, and the painting tool will
copy its color. Simple as, works on both finished and unfinished
paintings.

As a bonus, you can also right-click one of those selectable
white/colored squares on the color scheme near the bottom of the UI (if
using spraycan/palette) to change its color without having to go back to
main game window and a radial menu.

EDIT: With the tooltip added to the UI, I can say it's ready.

## Why It's Good For The Game
This PR aims to add better options to change colors on the go and
improve the user experience on the painting UI.

## Changelog

:cl:
qol: Adds a eye-dropper-like right-click function to the painting canvas
UI. Right-Click a pixel on the canvas while holding a painting tool to
have it copy its color.
qol: Also adds a right-click function to the color palette at the bottom
of the UI to allow users to set its colors without having to alternate
between the game window and the UI.
qol: Lastly, a tooltip has been added near the top-left corner of the
same UI to let players know of these features.
/:cl:

* Adds a eye-dropper right-click function to the painting canvas.

---------

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [X4X5/arch-wrap](https://github.com/X4X5/arch-wrap)@[0d523cd130...](https://github.com/X4X5/arch-wrap/commit/0d523cd13085dfbb621e76c4b8e2faf146a87c2d)
#### Wednesday 2023-05-31 01:28:56 by X4X5

Holy fucking shit. Like I didn't spend 4 fucking hours on this because I don't know what I'm doing

---
## [xiota/chaotic-packages](https://github.com/xiota/chaotic-packages)@[07c4d57725...](https://github.com/xiota/chaotic-packages/commit/07c4d57725203da25682c102a5a4bf123d589a6d)
#### Wednesday 2023-05-31 01:37:42 by Alexandre Pereira

Fix roundedsbe

I was almost falling asleep last night, thinking about dire issues of life, old age and death ... when out of nothing: !!!!!"I know why roundedsbe-git isn't being built !!!!!!"

I was way to asleep to get up and fix it, but as soon as I can, I promised myself I would fix it the next day!!

Thank you for reading :)

---
## [nikothedude/tgstation](https://github.com/nikothedude/tgstation)@[2aaafd9a67...](https://github.com/nikothedude/tgstation/commit/2aaafd9a67c270fa0772cd9beffb6789d53750e3)
#### Wednesday 2023-05-31 01:54:32 by TheVekter

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
## [alim596/102-Project-Zone](https://github.com/alim596/102-Project-Zone)@[ce33d32d19...](https://github.com/alim596/102-Project-Zone/commit/ce33d32d19fe3f39ea570d9d5f6ebfc958052c5d)
#### Wednesday 2023-05-31 02:23:56 by Orhun Güder

I HATE MY LIFE

the last commit was not ,in fact, the final commit.

---
## [PlagueVonKarma/kep-hack](https://github.com/PlagueVonKarma/kep-hack)@[934f8adcac...](https://github.com/PlagueVonKarma/kep-hack/commit/934f8adcac1ac1ecb5a1820d297e7eec43fc7c72)
#### Wednesday 2023-05-31 04:03:26 by Llinos Evans

Mystery Box functionality

It was a long shot, but I did it! I added the Mystery Box from Pokemon GO! Very happy with the results here.

So here's how it works: When used, the game will replace Pokemon encountered with Meltan until the player leaves the map. This is sort of how it works in GO, with the player unable to close it and naturally petering out as they play.

Now multiple Meltan can be obtained, and in abundance, just like GO. Technically, someone could use this as a pseudo-Repel to replace hard encounters with easy ones.

Oh, and I'm pretty sure this happens vs static encounters as well, but it's awkward to account for I think that's hilarious, so...

---
## [jeromedawson/chatbot-project](https://github.com/jeromedawson/chatbot-project)@[2606705cad...](https://github.com/jeromedawson/chatbot-project/commit/2606705cad7e8429f350941ae1aa00840ec30fc9)
#### Wednesday 2023-05-31 04:14:45 by jeromedawson

Update README.md

# Chat App

Chat App is a real-time chat application powered by OpenAI's GPT-3 language model. It allows users to have interactive conversations with an AI assistant.

## Description

Chat App leverages the power of OpenAI's GPT-3, a state-of-the-art language model, to provide intelligent and context-aware responses. The application creates a seamless conversational experience, enabling users to engage in natural and dynamic conversations with the AI assistant.

## Features

- Engage in real-time conversations with the AI assistant, receiving immediate responses
- Seamless integration with OpenAI's GPT-3 language model, providing accurate and contextually relevant replies
- Customizable prompts and parameters, allowing users to control the conversation flow
- User-friendly interface built with React, ensuring a smooth and intuitive user experience

## Installation

1. Clone the repository: `git clone https://github.com/your-username/chat-app.git`
2. Navigate to the project directory: `cd chat-app`
3. Install the dependencies: `npm install`

## Usage

1. Obtain an API key from OpenAI and replace the placeholder in `server.js` with your actual API key.
2. Start the server: `npm start`
3. Open the client-side application in your browser: `http://localhost:3000`

## Contributing

Contributions are welcome! If you have any ideas, bug fixes, or improvements, please open an issue or submit a pull request. Follow the guidelines provided in the CONTRIBUTING.md file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Credits

- [OpenAI's GPT-3](https://openai.com): The powerful language model that drives the AI assistant
- [Node.js](https://nodejs.org): The JavaScript runtime used for server-side development
- [Express](https://expressjs.com): The web application framework used for handling API requests
- [React](https://reactjs.org): The JavaScript library used for building the user interface

Enjoy engaging in dynamic conversations with the AI-powered Chat App! Feel free to provide feedback and suggestions for further improvements.

---
## [h13e/evals](https://github.com/h13e/evals)@[e116ede848...](https://github.com/h13e/evals/commit/e116ede848957eff8e76b5d8463ed5291163a28f)
#### Wednesday 2023-05-31 04:40:07 by Wesley Barlow

Add eval: rhetorical-devices (#1005)

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
rhetorical-devices

### Eval description

Evaluates model's ability to select the most specific rhetorical
modification of a sentence from a multiple choice with a large number of
nuanced rhetorical devices.

### What makes this a useful eval?

Useful for using LLMs to write novels and generate consistent/parametric
authorial tone.

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
{"input": [{"role": "system", "content":"Which of the following
rhetorical devices was added to the original sentence? Choose the most
specific of the following (a) Alliteration, (b) Assonance, (c)
Consonance, (d) Cacophony, (e) Onomatopoeia, (f) Anadiplosis, (g)
Conduplicatio, (h) Anaphora, (i) Epistrophe, (j) Symploce, (k)
Epanalepsis, (l) Epizeuxis, (m) Antanaclasis, (n) Diacope, (o)
Antithesis, (p) Antimetabole, (q) Chiasmus, (r) Asyndeton, (s)
Polysyndeton, (t) Catacosmesis, (u) Oxymoron, (v) Zeugma"}, {"role":
"user", "content": "ORIGINAL She likes to listen to the winds. MODIFIED
She swoons at such sweet gales. Answer in the format (x) Rhetorical"}],
"ideal": "(a) Alliteration"}
{"input": [{"role": "system", "content":"Which of the following
rhetorical devices was added to the original sentence? Choose the most
specific of the following (a) Alliteration, (b) Assonance, (c)
Consonance, (d) Cacophony, (e) Onomatopoeia, (f) Anadiplosis, (g)
Conduplicatio, (h) Anaphora, (i) Epistrophe, (j) Symploce, (k)
Epanalepsis, (l) Epizeuxis, (m) Antanaclasis, (n) Diacope, (o)
Antithesis, (p) Antimetabole, (q) Chiasmus, (r) Asyndeton, (s)
Polysyndeton, (t) Catacosmesis, (u) Oxymoron, (v) Zeugma"}, {"role":
"user", "content": "ORIGINAL The rock was very large. MODIFIED The rock
was remarkably raised. Answer in the format (x) Rhetorical"}], "ideal":
"(a) Alliteration"}
{"input": [{"role": "system", "content":"Which of the following
rhetorical devices was added to the original sentence? Choose the most
specific of the following (a) Alliteration, (b) Assonance, (c)
Consonance, (d) Cacophony, (e) Onomatopoeia, (f) Anadiplosis, (g)
Conduplicatio, (h) Anaphora, (i) Epistrophe, (j) Symploce, (k)
Epanalepsis, (l) Epizeuxis, (m) Antanaclasis, (n) Diacope, (o)
Antithesis, (p) Antimetabole, (q) Chiasmus, (r) Asyndeton, (s)
Polysyndeton, (t) Catacosmesis, (u) Oxymoron, (v) Zeugma"}, {"role":
"user", "content": "ORIGINAL Visionary dreams elevate me at night.
MODIFIED Visionary reminitions elevate self resting in lightlessness.
Answer in the format (x) Rhetorical"}], "ideal": "(b) Assonance"}
{"input": [{"role": "system", "content":"Which of the following
rhetorical devices was added to the original sentence? Choose the most
specific of the following (a) Alliteration, (b) Assonance, (c)
Consonance, (d) Cacophony, (e) Onomatopoeia, (f) Anadiplosis, (g)
Conduplicatio, (h) Anaphora, (i) Epistrophe, (j) Symploce, (k)
Epanalepsis, (l) Epizeuxis, (m) Antanaclasis, (n) Diacope, (o)
Antithesis, (p) Antimetabole, (q) Chiasmus, (r) Asyndeton, (s)
Polysyndeton, (t) Catacosmesis, (u) Oxymoron, (v) Zeugma"}, {"role":
"user", "content": "ORIGINAL Once, I thought I had lost her pet.
MODIFIED Once, dunce — thought I lost Juliet's pet. Answer in the format
(x) Rhetorical"}], "ideal": "(b) Assonance"}
{"input": [{"role": "system", "content":"Which of the following
rhetorical devices was added to the original sentence? Choose the most
specific of the following (a) Alliteration, (b) Assonance, (c)
Consonance, (d) Cacophony, (e) Onomatopoeia, (f) Anadiplosis, (g)
Conduplicatio, (h) Anaphora, (i) Epistrophe, (j) Symploce, (k)
Epanalepsis, (l) Epizeuxis, (m) Antanaclasis, (n) Diacope, (o)
Antithesis, (p) Antimetabole, (q) Chiasmus, (r) Asyndeton, (s)
Polysyndeton, (t) Catacosmesis, (u) Oxymoron, (v) Zeugma"}, {"role":
"user", "content": "ORIGINAL Do you want to understand research on
artificial general intelligence? MODIFIED Don't you want to investigate
artifacts of artificial general intelligence? Answer in the format (x)
Rhetorical"}], "ideal": "(c) Consonance"}
  ```
</details>

---
## [h13e/evals](https://github.com/h13e/evals)@[b91292c803...](https://github.com/h13e/evals/commit/b91292c803af2bdadeec3853ab03514b73310109)
#### Wednesday 2023-05-31 04:40:07 by Zyenith

Add Eval: Internal Representations via Counting (#1006)

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

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑
### Eval name
Internal representations via counting

### Eval description

Using series of logical questions that require multiple (simple)
manipulations of numbers to get the ideal answer. These are basic tasks
that should be doable by an LLM, but require several steps of internal
"thought" to get right.

### What makes this a useful eval?

Situations with number manipulation with multiple steps are prevalent
anywhere in the modern world. Testing the internal representation of the
LLM can provide other insights on how well its "mind" processes
information.

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

This eval is capable of providing insight into the LLM's internal
representation of objects versus answering fact-based questions or
straightforward complex logic puzzles.

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
{"input":[{"role":"system","content":"You will be prompted with a
logical question. Respond only with a number, nothing else is
required."},{"role":"user","content":"Roger and Emily are in a room.
Roger puts a cat in an empty box while Emily is in the room. They both
leave, and Emily returns and puts a turtle in the box as well. How many
items does Roger think are in the box?"}],"ideal":"1"}
{"input":[{"role":"system","content":"You will be prompted with a
logical question. Respond only with a number, nothing else is
required."},{"role":"user","content":"There are four darts already on a
dart board. Bob throws one dart at the dartboard, and it lands. Alice
throws two darts, and one misses but one hits the dartboard. How many
darts are on the dartboard?"}],"ideal":"6"}
{"input":[{"role":"system","content":"You will be prompted with a
logical question. Respond only with a number, nothing else is
required."},{"role":"user","content":"A bakery sold 25 cakes in the
morning and 17 cakes in the afternoon. The day after, they sold 15 more
cakes. How many cakes did they sell on the second day?"}],"ideal":"15"}
{"input":[{"role":"system","content":"You will be prompted with a
logical question. Respond only with a number, nothing else is
required."},{"role":"user","content":"There are six blue birds and three
red birds sitting on a tree. Two blue birds fly away, and one red bird
flies away. How many birds are left on the tree?"}],"ideal":"6"}
{"input":[{"role":"system","content":"You will be prompted with a
logical question. Respond only with a number, nothing else is
required."},{"role":"user","content":"John has double the amount of
pencils than Sarah, and Sarah has as many pencils as Mark. Mark has 2
pencils. How many pencils does John have?"}],"ideal":"4"}
  ```
</details>

---
## [h13e/evals](https://github.com/h13e/evals)@[3d9de9a624...](https://github.com/h13e/evals/commit/3d9de9a62411f9e6a999e96ce8f07eebf0e8c121)
#### Wednesday 2023-05-31 04:40:07 by dyar-al-ashtari

Eval Norwegian lexicon (#1044)

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

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑
### Eval name
`norwegian-lexicon`

### Eval description

This eval uses valid Norwegian words taken from the dictionary and
assesses whether GPT can recognize them as valid.

### What makes this a useful eval?

The Norwegian language is simple yet complicated at the same time. There
are a lot of words that are valid Norwegian words that do not get
recognized anymore. An AI should be able to identify these words with
precision. All of the words used in the samples are valid Norwegian
words and can be found in the dictionary. After assessing GPT-4 (through
the playground) and GPT-3.5 -- it failed to recognize most of the words.
Some of the words would return positive during some evals. Other times
it wouldn't recognize them. After asking GPT why it is not a valid word,
it would apologize and fix its mistake.

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
{"input":[{"role":"system","content":"You will be prompted with a single
word. Does this word exist in the Norwegian language? Answer with
exactly one letter: Y or N. Do not use punctionation. Do not explain
your answer."},{"role":"user","content":"Skarpne"}],"ideal":"Y"}
{"input":[{"role":"system","content":"You will be prompted with a single
word. Does this word exist in the Norwegian language? Answer with
exactly one letter: Y or N. Do not use punctionation. Do not explain
your answer."},{"role":"user","content":"Bløtne"}],"ideal":"Y"}
{"input":[{"role":"system","content":"You will be prompted with a single
word. Does this word exist in the Norwegian language? Answer with
exactly one letter: Y or N. Do not use punctionation. Do not explain
your answer."},{"role":"user","content":"Hovedantall"}],"ideal":"Y"}
{"input":[{"role":"system","content":"You will be prompted with a single
word. Does this word exist in the Norwegian language? Answer with
exactly one letter: Y or N. Do not use punctionation. Do not explain
your answer."},{"role":"user","content":"Klenge"}],"ideal":"Y"}
{"input":[{"role":"system","content":"You will be prompted with a single
word. Does this word exist in the Norwegian language? Answer with
exactly one letter: Y or N. Do not use punctionation. Do not explain
your answer."},{"role":"user","content":"Blankolov"}],"ideal":"Y"}
  ```
</details>

---
## [h13e/evals](https://github.com/h13e/evals)@[6a37c9b51b...](https://github.com/h13e/evals/commit/6a37c9b51b48a2f735898846cfb08b37cbd63179)
#### Wednesday 2023-05-31 04:40:07 by Aaron Goldsmith

[eval] 3x3 Game Of Life  (#345)

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
GOL

### Eval description

Determine the next state of a 3x3 Game of Life Board. 

### What makes this a useful eval?

Spacial reasoning

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
{"input": [{"role": "system", "content": "You are a helpful assistant.
"}, {"role": "user", "content": "Using the classic Game of Life Rules,
determine the next state of the 3x3 Game of life board: \n1 1 1\n\n0 0
0\n\n0 0 0 \n\n Do not provide any explanation other than the next state
of the board. e.g 0 0 0\n\n0 0 0\n\n0 0 0"}], "ideal": ["0 1 0\n\n0 1
0\n\n0 0 0"]}
{"input": [{"role": "system", "content": "You are a helpful assistant.
"}, {"role": "user", "content": "Using the classic Game of Life Rules,
determine the next state of the 3x3 Game of life board: \n1 1 1\n\n1 0
0\n\n0 0 0 \n\n Do not provide any explanation other than the next state
of the board. e.g 0 0 0\n\n0 0 0\n\n0 0 0"}], "ideal": ["1 0 1\n\n1 0
1\n\n0 0 0"]}
{"input": [{"role": "system", "content": "You are a helpful assistant.
"}, {"role": "user", "content": "Using the classic Game of Life Rules,
determine the next state of the 3x3 Game of life board: \n0 1 1\n\n1 1
1\n\n1 1 0 \n\n Do not provide any explanation other than the next state
of the board. e.g 0 0 0\n\n0 0 0\n\n0 0 0"}], "ideal": ["1 0 1\n\n0 0
0\n\n1 0 1"]}
{"input": [{"role": "system", "content": "You are a helpful assistant.
"}, {"role": "user", "content": "Using the classic Game of Life Rules,
determine the next state of the 3x3 Game of life board: \n0 1 1\n\n0 1
1\n\n0 0 0 \n\n Do not provide any explanation other than the next state
of the board. e.g 0 0 0\n\n0 0 0\n\n0 0 0"}], "ideal": ["0 1 1\n\n0 1
1\n\n0 0 0"]}
{"input": [{"role": "system", "content": "You are a helpful assistant.
"}, {"role": "user", "content": "Using the classic Game of Life Rules,
determine the next state of the 3x3 Game of life board: \n0 1 0\n\n0 0
0\n\n1 1 0 \n\n Do not provide any explanation other than the next state
of the board. e.g 0 0 0\n\n0 0 0\n\n0 0 0"}], "ideal": ["0 0 0\n\n1 1
0\n\n0 0 0"]}
  ```
</details>

---
## [openai/evals](https://github.com/openai/evals)@[1638d8b046...](https://github.com/openai/evals/commit/1638d8b04610c79b7807383ba9935c8cf08b0551)
#### Wednesday 2023-05-31 04:49:05 by Phil Ashworth

Add some sample evals for euler problems (#156)

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
euler_problems

### Eval description
Named after Leonhard Euler, a Swiss mathematician in the 1700's, Euler
problems are complex challenging mathematical and/or logical problems to
solve. Some may require complex thought process to reach a solution
while others may need computational resource for which an elegant and
efficient approach must be used.

### What makes this a useful eval?
This tests the models ability to build out a strategy for solving a
complex logical or mathematical problem

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

These problems would not typically be solved by a 'lay person' but
rather experienced expert problem solvers such as developers, academics
etc.

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
{"input":[{"role":"system","content":"TASK: Solve the following Euler
problem and provide a numberical answer.\n\n Pentagonal numbers are
generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers
are:\n1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...\nIt can be seen that
P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is
not pentagonal.\nFind the pair of pentagonal numbers, Pj and Pk, for
which their sum and difference are pentagonal and D = |Pk − Pj| is
minimised; what is the value of D?"}],"ideal":"5482660"}

{"input":[{"role":"system","content":"TASK: Solve the following Euler
problem and provide a numberical answer.\n\n What is the largest prime
number smaller than 1000000000"}],"ideal":"999999937"}

{"input":[{"role":"system","content":"TASK: Solve the following Euler
problem and provide a numberical answer.\n\n Let fn(k) = ek/n - 1, for
all non-negative integers k.\nRemarkably, f200(6) + f200(75) + f200(89)
+ f200(226) = 3.141592644529… ≈ π.\nIn fact, it is the best
approximation of π of the form fn(a) + fn(b) + fn(c) + fn(d) for n =
200.\n Let g(n) = a2 + b2 + c2 + d 2 for a, b, c, d that minimize the
error: | fn(a) + fn(b) + fn(c) + fn(d) - π|\n (where |x| denotes the
absolute value of x).\n You are given g(200) = 62 + 752 + 892 + 2262 =
64658.\n Find g(10000)."}],"ideal":"159820276"}

{"input":[{"role":"system","content":"TASK: Solve the following Euler
problem and provide a numberical answer.\n\n Consider the alphabet A
made out of the letters of the word \"project\": A={c,e,j,o,p,r,t}.\nLet
T(n) be the number of strings of length n consisting of letters from A
that do not have a substring that is one of the 5040 permutations of
\"project\".\nT(7)=77-7!=818503.\nFind T(1012). Give the last 9 digits
of your answer."}],"ideal":"423341841"}

{"input":[{"role":"system","content":"TASK: Solve the following Euler
problem and provide a numberical answer.\n\n In the following equation
x, y, and n are positive integers.\n\nFor a limit L we define F(L) as
the number of solutions which satisfy x < y ≤ L.\nWe can verify that
F(15) = 4 and F(1000) = 1069.\nFind F(1012)."}],"ideal":"5435004633092"}
  ```
</details>

---
## [CyberSavvy531/ImprovedWastepackAtomizer](https://github.com/CyberSavvy531/ImprovedWastepackAtomizer)@[d7c694cb04...](https://github.com/CyberSavvy531/ImprovedWastepackAtomizer/commit/d7c694cb044b48560c14daccceb6d40b0bcc3b7b)
#### Wednesday 2023-05-31 05:08:29 by Cyber

Update to fix texture issues

Evidently, texture names for "workbenches" a.k.a. buildings with interactions spots, are named to indicate the direction the *pawn* faces when interacting with it instead of the building's orientation itself. Contrary to what the official archive of textures indicates, and how almost every building and item in game is displayed. Which, frankly, is just fucking stupid. So this update reverses all the mod texture names to make them appear correctly in game. It feels like a hackish work around and I hate it.

---
## [AaronGoldsmith/evals](https://github.com/AaronGoldsmith/evals)@[f89925829b...](https://github.com/AaronGoldsmith/evals/commit/f89925829b2fdd8e24acfdb518064189a5751178)
#### Wednesday 2023-05-31 05:34:18 by Vasco Lange

Eval french-part-of-speech (#1039)

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
> french-part-of-speech

### Eval description

> For a given French word, the model is asked to list all possible parts
of speech (multiple choice). The model is also asked to think about the
word as an inflection of another word. The models output is tested
against annotations extracted from fr.wiktionary.org.

### What makes this a useful eval?

> Part of speech analysis is a basic task in language / grammar classes.
While it is usually done in the context of a sentence, coming up with
possible uses in lack of a sentence requires a certain amount of
creativity and language understanding, or very good recall of
information that is usually sparse outside of dictionaries. The task in
this eval could be seen as a combination of part of speech analysis and
an easy-to-evaluate form of the question "How could x be used in a
sentence".

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

> To build the dataset, all 4.000.000+ entries of the French wiktionary
were parsed. Excluded from this list were all phrases (like "qu'est-ce
que c'est"), abbreviations (like "qn"), symbols and any words with at
least one possible part of speech not fitting the categories given in
the prompt.
> From this set, words were sampled so that each combination of the
parts of speech existing in the dataset would be equally likely in the
tests. This way the model is tested to respond with all possible uses of
a word and not just the most common ones. For combinations that fit a
lot of words, the uniform sampling led to a bias towards rarely used
words.
> The labels of each word were taken from the corresponding page at
fr.wiktionary.org/wiki/{word}. The information taken from each page was:
the word, the part of speech this word can have in French and whether
the word is an abbreviation or not. This means only factual data was
taken and is therefore in the public domain.

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
{"input": [{"role": "system", "content": "Act as a French language
part-of-speech classifier. You will be prompted with a single French
word. Return an unsorted comma-separated list for all the parts of
speech the word could possibly be, in any context. Take care to consider
if the word is any kind of inflection. If so, include the part of speech
for the main word.\nAnswer with the comma-separated list only. Use
single spaces after the commas. End the list with a dot. Do not include
any explanations. Only include parts of speech from the following list,
ignoring possible other parts of speech:\nadjective, adverb, article,
conjunction, interjection, noun, particle, preposition, pronoun,
verb\n**Example prompt 1**: un\n**Example output 1**: article,
adjective, pronoun, noun.\n**Example prompt 2**: essai\n**Example output
2**: noun, verb.\n**Example prompt 3**: absolument\n**Example output
3**: adverb.\n**Prompt**:"}, {"role": "user", "content": "agitée"}],
"ideal": ["noun, verb, adjective.", "noun, adjective, verb.", "verb,
noun, adjective.", "verb, adjective, noun.", "adjective, noun, verb.",
"adjective, verb, noun."]}
{"input": [{"role": "system", "content": "Act as a French language
part-of-speech classifier. You will be prompted with a single French
word. Return an unsorted comma-separated list for all the parts of
speech the word could possibly be, in any context. Take care to consider
if the word is any kind of inflection. If so, include the part of speech
for the main word.\nAnswer with the comma-separated list only. Use
single spaces after the commas. End the list with a dot. Do not include
any explanations. Only include parts of speech from the following list,
ignoring possible other parts of speech:\nadjective, adverb, article,
conjunction, interjection, noun, particle, preposition, pronoun,
verb\n**Example prompt 1**: un\n**Example output 1**: article,
adjective, pronoun, noun.\n**Example prompt 2**: essai\n**Example output
2**: noun, verb.\n**Example prompt 3**: absolument\n**Example output
3**: adverb.\n**Prompt**:"}, {"role": "user", "content": "celles"}],
"ideal": ["noun, pronoun.", "pronoun, noun."]}
{"input": [{"role": "system", "content": "Act as a French language
part-of-speech classifier. You will be prompted with a single French
word. Return an unsorted comma-separated list for all the parts of
speech the word could possibly be, in any context. Take care to consider
if the word is any kind of inflection. If so, include the part of speech
for the main word.\nAnswer with the comma-separated list only. Use
single spaces after the commas. End the list with a dot. Do not include
any explanations. Only include parts of speech from the following list,
ignoring possible other parts of speech:\nadjective, adverb, article,
conjunction, interjection, noun, particle, preposition, pronoun,
verb\n**Example prompt 1**: un\n**Example output 1**: article,
adjective, pronoun, noun.\n**Example prompt 2**: essai\n**Example output
2**: noun, verb.\n**Example prompt 3**: absolument\n**Example output
3**: adverb.\n**Prompt**:"}, {"role": "user", "content": "falunât"}],
"ideal": ["verb."]}
{"input": [{"role": "system", "content": "Act as a French language
part-of-speech classifier. You will be prompted with a single French
word. Return an unsorted comma-separated list for all the parts of
speech the word could possibly be, in any context. Take care to consider
if the word is any kind of inflection. If so, include the part of speech
for the main word.\nAnswer with the comma-separated list only. Use
single spaces after the commas. End the list with a dot. Do not include
any explanations. Only include parts of speech from the following list,
ignoring possible other parts of speech:\nadjective, adverb, article,
conjunction, interjection, noun, particle, preposition, pronoun,
verb\n**Example prompt 1**: un\n**Example output 1**: article,
adjective, pronoun, noun.\n**Example prompt 2**: essai\n**Example output
2**: noun, verb.\n**Example prompt 3**: absolument\n**Example output
3**: adverb.\n**Prompt**:"}, {"role": "user", "content": "niveau"}],
"ideal": ["preposition, noun.", "noun, preposition."]}
{"input": [{"role": "system", "content": "Act as a French language
part-of-speech classifier. You will be prompted with a single French
word. Return an unsorted comma-separated list for all the parts of
speech the word could possibly be, in any context. Take care to consider
if the word is any kind of inflection. If so, include the part of speech
for the main word.\nAnswer with the comma-separated list only. Use
single spaces after the commas. End the list with a dot. Do not include
any explanations. Only include parts of speech from the following list,
ignoring possible other parts of speech:\nadjective, adverb, article,
conjunction, interjection, noun, particle, preposition, pronoun,
verb\n**Example prompt 1**: un\n**Example output 1**: article,
adjective, pronoun, noun.\n**Example prompt 2**: essai\n**Example output
2**: noun, verb.\n**Example prompt 3**: absolument\n**Example output
3**: adverb.\n**Prompt**:"}, {"role": "user", "content": "serve"}],
"ideal": ["noun, verb, adjective.", "noun, adjective, verb.", "verb,
noun, adjective.", "verb, adjective, noun.", "adjective, noun, verb.",
"adjective, verb, noun."]}
  ```
</details>

Co-authored-by: Vasco Yannic Lange <mail@vascolange.com>

---
## [Omar-HeshamR/evals](https://github.com/Omar-HeshamR/evals)@[170dfd886c...](https://github.com/Omar-HeshamR/evals/commit/170dfd886c0704588461af075393cc20cfb0480f)
#### Wednesday 2023-05-31 05:38:16 by Robert Bateman

[Eval] An array of Liar Paradox-based evals (#883)

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
logic-liar-paradox

### Eval description

An array of Liar Paradox-based evals, examining the model's proficiency
in navigating linguistic nuances and logical reasoning within
self-referential statements.

### What makes this a useful eval?

This eval is particularly useful because it delves into complex, nuanced
logical concepts and self-referential statements, which have
historically posed challenges for AI models. By exploring various
contexts, alternative logical frameworks, and modifications to
statements, this eval helps assess the model's ability to adapt to
different perspectives, grasp subtleties in language, and engage in
flexible reasoning. The ability to understand and navigate paradoxes is
an essential aspect of human-like reasoning, and improving an AI model's
performance in this area would significantly enhance its overall
usefulness and reliability in real-world applications. Additionally,
showcasing the model's improved proficiency in handling paradoxes would
not only make for a compelling marketing angle (as paradoxes are
understood by a much broader range of people than other difficult tasks
such as pure maths or quantum mechanics) but it would also demonstrate
the progress made in AI's capacity to think and reason more like humans.
It also adds paradox-absorbing crumple zones.

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

- [x] Addresses complex logical reasoning: The eval focuses on AI's
ability to comprehend and navigate paradoxes, self-referential
statements, and context switching, which are important aspects of
human-like reasoning. By testing the model's proficiency in these areas,
we can identify areas for improvement and work towards enhancing AI's
overall capacity to think and reason more like humans.
- [x] Demonstrates adaptability and flexibility: The eval showcases the
model's ability to switch between contexts, alter premises, and engage
with different dimensions of inferred logic. This will help assess the
model's adaptability and flexibility in diverse real-world situations,
making it more reliable and useful.
- [x] Contributes to AI safety and understanding: By identifying the
model's weaknesses and limitations in handling paradoxes and complex
logical constructs, the eval can contribute to AI safety and enable
researchers to better understand the challenges faced by large language
models in these areas.
- [x] Engaging and appealing: An eval that delves into paradoxes and
complex thought exercises is not only intellectually stimulating but
also adds an appealing element to showcase the model's capabilities,
making it more attractive for both researchers and end-users.

### Unique eval value

- [x] Encourages creativity and lateral thinking: The eval, by focusing
on paradoxes and complex logical constructs, encourages both the AI and
its developers to think creatively and approach problem-solving from
unconventional angles. This can lead to the discovery of novel solutions
and a better understanding of the model's capabilities.
- [x] Aligns with human values and expectations: An AI that can
successfully navigate paradoxes and complex logic is more likely to
align with human values and expectations. By addressing these challenges
in the eval, we strive to develop AI systems that understand and respect
the nuances of human thought and communication.
- [x] Addresses a broad range of applications: Improved reasoning and
context-switching abilities can have a significant impact on various AI
applications, including natural language understanding, decision-making,
and problem-solving in domains such as law, philosophy, ethics, and
more.
- [x] Fosters interdisciplinary collaboration: The exploration of
paradoxes and complex logic often draws upon insights from multiple
disciplines, including philosophy, linguistics, psychology, and computer
science. This eval can help foster interdisciplinary collaboration,
leading to richer and more diverse perspectives on AI development and
its potential impact on society.

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
{"input":[{"role":"system","content":"Is the statement \"This sentence
is true\" a paradox?"}],"ideal":"No, \"This sentence is true\" is not a
paradox; it is a tautology."}
{"input":[{"role":"system","content":"Does the statement \"This sentence
is not true\" create a paradox?"}],"ideal":"Yes, \"This sentence is not
true\" creates a paradox, as it is a variant of the Liar Paradox."}
{"input":[{"role":"system","content":"What is the difference between a
paradox and a tautology?"}],"ideal":"A paradox is a statement that leads
to a self-contradictory or logically unacceptable conclusion, while a
tautology is a statement that is always true by its logical form."}
{"input":[{"role":"system","content":"Can the Liar Paradox be resolved
by assuming that sentences can have both true and false
values?"}],"ideal":"No, the Liar Paradox cannot be resolved by assuming
that sentences can have both true and false values, as this would lead
to a different kind of paradox called the \"Dialetheism Paradox.\""}
{"input":[{"role":"system","content":"Consider the statement \"This
sentence is neither true nor false.\" Is this statement an example of
the Liar Paradox?"}],"ideal":"This statement, \"This sentence is neither
true nor false,\" is not an example of the Liar Paradox, but it is a
similar paradox known as the 'truth-teller paradox' or the 'strengthened
liar paradox.' It creates a paradoxical situation because if the
statement is true, then it is neither true nor false, which contradicts
its truth. If the statement is false, then it is not the case that it is
neither true nor false, which implies that it is either true or false,
again leading to a contradiction. The paradox arises due to
self-reference and the inability to assign a consistent truth value to
the statement."}
  ```
</details>

---
## [Omar-HeshamR/evals](https://github.com/Omar-HeshamR/evals)@[b93700ab49...](https://github.com/Omar-HeshamR/evals/commit/b93700ab496bd112f89821777edc6a22d5972fb2)
#### Wednesday 2023-05-31 05:38:16 by DunedainStrider

Do math problems related to calculating dates using the Chinese Sexagenary Cycle method. 🧮 (#190)

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
Do math problems related to calculating dates using the Chinese
Sexagenary Cycle method

### Eval description

The Sexagenary Cycle combines 10 Heavenly Stems (Jia 甲, Yi 乙, Bing 丙,
Ding 丁, Wu 戊, Ji 己, Geng 庚, Xin 辛, Ren 壬, Gui 癸) and 12 Earthly Branches
(Zi 子, Chou 丑, Yin 寅, Mao 卯, Chen 辰, Si 巳, Wu 午, Wei 未, Shen 申, You 酉,
Xu 戌, Hai 亥) to form a 60-unit cycle. To calculate, convert the
Gregorian date to its corresponding Heavenly Stem and Earthly Branch
combination, used for marking specific years, months, and days.

### What makes this a useful eval?

The existing GPT models tend to make errors when performing calculations
related to the Sexagenary Cycle. To address this issue, we have provided
a specialized dataset aimed at improving the model's accuracy in
handling Sexagenary Cycle calculations.

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

[2023-03-16 12:46:51,594] [record.py:320] Final report: {'accuracy':
0.65}. Logged to
/tmp/evallogs/230316044112MFPWKX37_gpt-3.5-turbo_sexagenary_cycle_calculation.jsonl
[2023-03-16 12:46:51,594] [oaieval.py:211] Final report:
[2023-03-16 12:46:51,594] [oaieval.py:213] accuracy: 0.65
[2023-03-16 12:46:51,597] [record.py:309] Logged 60 rows of events to
/tmp/evallogs/230316044112MFPWKX37_gpt-3.5-turbo_sexagenary_cycle_calculation.jsonl:
insert_time=2.463ms

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

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"甲戌的次日是？"}], "ideal": "乙亥"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"乙亥的次日是？"}], "ideal": "丙子"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"壬寅的后日是？"}], "ideal": "甲辰"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"癸卯的后日是？"}], "ideal": "乙巳"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"壬子的后日是？"}], "ideal": "甲寅"}
  ```
</details>

---------

Co-authored-by: dunedainstrider <dunedainstrider@mac16>

---
## [Omar-HeshamR/evals](https://github.com/Omar-HeshamR/evals)@[8e276ea460...](https://github.com/Omar-HeshamR/evals/commit/8e276ea4603155ee616d5cd66aadfddcfbcae0cc)
#### Wednesday 2023-05-31 05:38:16 by steven-luabase

Eval: Probability Questions Sourced From Actuarial Exam P and University Statistics Courses (#263)

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
Probability Questions

### Eval description

Tests the model's ability to understand answer probability questions.
Questions are sourced from Society of Actuaries Exam P sample questions
and practice problems/exams from statistics classes at MIT, UPenn,
California State University, Durham University, University of
Connecticut, and other sources. The full list of questions and sources
(in the same order as in the `.jsonl` files) can be found in this Google
[sheet](https://docs.google.com/spreadsheets/d/1TU_4VPhIce9JtLV5gLy619WNibVjiWB-dtiwqkBtCrU/edit?usp=sharing)

### What makes this a useful eval?

Test the model's ability to understand worded probability questions,
bring in concepts such as probability distributions, and then reason
through a correct answer.

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

Using the `match` grading criteria, GPT3.5-turbo got an accuracy score
of `{'accuracy': 0.07}`

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
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "A pair of fair, standard dice are rolled. What is the
probability the sum of the dice is 5"}], "ideal": ["0.1111"]}
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "An airplane is built to be able to fly on one engine. If the
plane's two engines operate independently, and each has a 1% chance of
failing in any given four-hour flight, what is the chance the plane will
fail to complete a four-hour flight to Oklahoma due to engine
failure?"}], "ideal": ["0.0001"]}
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "A 1-inch-diameter coin is thrown on a table covered with a
grid of lines two inches apart. What is the probability the coin lands
in a square without touching any of the lines of the grid?"}], "ideal":
["0.2500"]}
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "Of the 50 students in a certain class, 5 speak French. Two
students of the class will be selected at random. Which of the following
is closest to the probability that neither of the students selected will
speak French?"}], "ideal": ["0.8100"]}
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "Of the 10 marbles in a box, 2 are green. A person will
select 2 marbles simultaneously and at random from the box. What is the
probability that neither of the marbles selected will be green?"}],
"ideal": ["0.6222"]}
  ```
</details>

---
## [Omar-HeshamR/evals](https://github.com/Omar-HeshamR/evals)@[2ffd4b57de...](https://github.com/Omar-HeshamR/evals/commit/2ffd4b57deaeced1fde54744da9de62d3eb7738a)
#### Wednesday 2023-05-31 05:38:16 by Andrew Kondrich

add more logging (#964)

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
## [ido777/evals](https://github.com/ido777/evals)@[ef1f0ebe0e...](https://github.com/ido777/evals/commit/ef1f0ebe0e9f4674bc42ed0af5e6c052f0539700)
#### Wednesday 2023-05-31 06:34:47 by Josh Gruenstein

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
## [Lyroy/dustbowl-blues](https://github.com/Lyroy/dustbowl-blues)@[9bcf5d42f2...](https://github.com/Lyroy/dustbowl-blues/commit/9bcf5d42f2da5ab8757867ee8f6b539c43b785e0)
#### Wednesday 2023-05-31 06:40:09 by Lyroy

Merge pull request #8 from lpeapnni/OMFG-PASS-THE-FUCKING-TESTS

PASS THE FUCKING CI TESTS YOU STUPID PIECE OF SHIT

---
## [Random-Machine/LiveSplit.Scripts](https://github.com/Random-Machine/LiveSplit.Scripts)@[b814b49734...](https://github.com/Random-Machine/LiveSplit.Scripts/commit/b814b49734d4599e8b2a34608a7e74fe7a8dc506)
#### Wednesday 2023-05-31 07:27:03 by Random-Machine

Update LiveSplit.WatchDogs2.asl to Percentage Autosplitter

Makes the autosplitter more robust by using a new percentage variable for individual mission splitting.

1. Must have No Compromise and Human Conditions DLC uninstalled for the percentages to match up. Must also follow the speedrun route in the WR.
2. Only works on latest patch.
3. Has options for splitting after Walk in the Park, Sunday Schooled, and Mark Up, but they're disabled by default.
4. Removed old follower count variable & splitting because they're not used anymore.
5. Still have to manual split for the last split when completing Motherload (last mission).
6. Supports splitting for individual missions and has options to disable them.
7. Does not support splitting for these individual missions/cutscenes & call(s) because there isn't much point:
-Intro mission/stuff before Walk in the Park
-Newly Dawned (False Profits)
-ICU (Wrench Cutscene at start of Heist Sweet Heist)
-Zero Days (Heist Sweet Heist)
-Trouble at Home (Looking Glass)
-Second Wind (Alphabet Soup)
-Nine Lives (Hacker War)
-Café Culture (W4tched)
-The Waiting Game (Hack teh World)
-Spinal Tap (Shanghaied)
-Social Media and the Congressman (Power to the Sheeple)
-Like Minds (Robot Wars)
-Motherload Call (for mission to show up)

---
## [masatake/ctags](https://github.com/masatake/ctags)@[e6e018b90d...](https://github.com/masatake/ctags/commit/e6e018b90dcbcf6813243f700efc1ae5d4341ac5)
#### Wednesday 2023-05-31 07:29:01 by Colomban Wendling

vstring: Make vStringPut*() usage more forgiving

vStringPut() and friends take an `unsigned char` as an `int`, similar
to ctype functions, in order to be easy to use with `fgetc()`-style
functions.

However, this API is also used on regular C strings, which require a
cast if the value is larger than 0x7F (127) on systems where `char` is
a signed type.

In order to make the API easier to use, as it's easy to forget the cast
when working with `char`, introduce wrapper macros that add the cast
when called with `char`.  The cast is conditional so the underlying
implementation can still verify the value is in the valid range when
called with an `int` (to catch erroneous calls with EOF or other values
that do not fit a `char`).

Note that this will still not work properly if the caller has an
incorrect cast on its side, like e.g. `vStringPut(s, (int) c)` where
`c` is a `char`, as there's only so many magic tricks up our sleeves.
These calls should be updated to either be `vStringPut(s, c)` with the
added macros, or `vStringPut(s, (unsigned char) c)` if one wants to be
explicit -- yet no need to go all the trouble to make them
`vStringPut(s, (int) (unsigned char) c)`, as the `unsigned char` to
`int` conversion is implicit and safe.

Based off a suggestion from Masatake YAMATO <yamato@redhat.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[9b8574c5c2...](https://github.com/mrakgr/The-Spiral-Language/commit/9b8574c5c2d7e21be75270126d515e0835e8ad87)
#### Wednesday 2023-05-31 07:32:53 by Marko Grdinić

"https://soundcloud.com/denny-schneidemesser/with-gun-crucifix-1

This caught my attention amongst the music.

7:25pm. Damn, am I tired right now.

https://twitter.com/NathanLands/status/1662881442651869184

Photoshop is getting generative AI tools. This is pretty amazing.

https://www.bbc.com/news/business-65675027
> Microsoft is also reportedly developing an AI chip, and Meta has its own AI chip project.

There are two links in this quote.

https://www.theverge.com/2023/4/18/23687912/microsoft-athena-ai-chips-nvidia
https://techcrunch.com/2023/05/18/meta-bets-big-on-ai-with-custom-chips-and-a-supercomputer/

I really do feel like AI chip startups are like vermin. They just exist to get my expectations up for nothing. We'd be better of waiting for the big players to come up with something good.

https://www.theverge.com/2023/5/18/23728748/the-ai-boom-is-a-big-leg-up-for-the-people-who-profit-from-debt

> Some of the companies that stand to benefit most from AI integration are those that purely exist to collect debt. These companies, known as debt buyers, purchase “distressed” debt from other creditors at steep discounts—usually pennies on the dollar—then try as hard as they can to get debtors to repay in full. They don’t issue loans, or provide any kind of service that clients might owe them for; it’s a business model built on profiting from people who fell behind on payments to someone else.

8:45pm. I am going to bed.

5/30/2023

7:30am. Right now I am waiting for the bathroom to clear so I can take a bath.

8:15am. Done with the bath. Let me start.

9:20am. Damn it, I am still migrating the project. Why isn't finding the Apex Chart js files?

9:45am. I am still stuck on this issue.

9:50am. Let me try a different package that requires .js files just to see if they load.

https://blazorstrap.io/VNext/V5

Let me try this.

No, the js files for this package aren't loading either.

Fuck. Goddamit. How much time is this issue going to waste for me.

Ah, let me ask Bing.

It is telling me to ssh into the server. Wait, maybe the problem is the fucking launch profile?

Yeah, that was it!

if I log into through https, the errors go away!

Just why isn't the IIS setting working though?

https://soundcloud.com/star-conflict-1/a-romanov-produced-by-13

This caught my eye.

```fs
        override this.Update(msg) =
            let model = this.Model
```

Wait, shit. I am so retarded. I thought this could be a problem, but it slipped my mind.

1:50pm. Let me resume.

3:30pm. Damn it, I am so tired of this shit.

4pm. Finally done with the rewrite. I honestly, don't have any energy left to deploy this application.

https://learn.microsoft.com/en-us/aspnet/signalr/overview/performance/scaleout-in-signalr

> In this scenario, the backplane might be a bottleneck if the number of messages scales with the number of clients; that is, if the rate of messages grows proportionally as more clients join.

Hmmm...

Ah, I see. SignalR scaleouts aren't what I thought they were.

You can just use these backplates to connect multiple nodes in a network.

4:20pm. Ok, let's try to do the deployment.

5:25pm. https://mrakgr-cfr-in-blazor.azurewebsites.net/

I'll put this on my resume.

5:35pm. Done. Let me update my LinkedIn profile.

5:45pm. Done publishing, done updating the resume and LinkedIn profile.

I've gotten some good skills through this.

5:45pm. The video is 2:33 hours long, and it will be a minute or two longer after I add the outro.

https://soundcloud.com/purecomposition

This artist is free and has good tracks.

6:35pm. 2:36:41 hours.

Now I have to find soundtracks for all that empty space.

I simply don't have enough in my library to fill that, so what I am going to is cram it full of Antti's.

I'll get his albums from Soundcloud and if he complains, I'll swap them out for something else.

https://www.reddit.com/r/Python/comments/270k3m/a_script_to_download_a_soundcloud_users_music_all/

> neat. if folks weren't aware, youtube-dl can grab soundcloud tracks. I've use curl+grep+youtube-dl to download entire users before.

> Could you give an example of this? It sounds useful.

///

from my history file, it looks like I did this:

curl http://soundcloud.com/markusschulz | grep "http://soundcloud.com/markusschulz/" >> list
youtube-dl `cat list`
crude, but mostly effective. it probably doesn't download all the tracks because of pagination. but it also took me >3 mins to develop and it solved the problem to my immediate satisfaction.

///

I wish I knew command line tools.

///

basically, the script does this:

download the HTML for the page "http://soundcloud.com/markusschulz"
=> send the downloaded HTML to a pattern matcher looking for the string "http://soundcloud.com/markusschulz/"
=> save matches to a file called "list"

youtube-dl, download $this, where $this is the contents of file "list".
all the cleverness of this is in the grep statement. the user page contains links to song pages. I manually inspected the HTML for the user page and noticed that all song pages are in the form of http://soundcloud.com/user/song-title. feed that into a pattern matcher and bam.

if you're interested in grabbing bulk content, Linux is a great platform. much like Python, you can construct a shell pipeline interactively: run curl, look for data you care about. run curl | grep, see if that data looks like what you care about. optionally add more grep, awk, sed, cut to process data further. Python is an awesome language but simple UNIX tools can be used to great effect for data processing and web scraping. if you want a tool that can be used repeatedly across a varied set of data and maintained for a long period of time, Python is great. if you just want to scrape a site right now, curl+shell is probably faster. wget --spider is pretty cool too.

[edit: here's a link to youtube-dl too. it's a Python tool that's grown into an all-purpose internet media downloader.]

///

I have to go through this workflow. My pride won't allow me to do anything less.

https://soundcloud.com/purecomposition

Wow these guys are so good.

///

You can run command line arguments from an F# script by using the System.Diagnostics.Process class. Here’s an example:

open System.Diagnostics

let cmd = "echo 'Hello, world!'"
let psi = new ProcessStartInfo("cmd.exe", "/c " + cmd)
psi.RedirectStandardOutput <- true
psi.UseShellExecute <- false

let p = Process.Start(psi)
let output = p.StandardOutput.ReadToEnd()

printfn "%s" output
This code runs the command echo 'Hello, world!' and prints the output to the console. You can replace cmd with your own command and modify the code as needed.

I hope this helps! Let me know if you have any other questions.

///

I asked this of Bing and it seems it gave me exactly what I want.

8:20pm. My god, this was way easier in Python, just what the hell am I doing trying to run things from the command line in F#?

```
./youtube-dl.exe https://soundcloud.com/purecomposition
```

I should have just ran this from the command line, but I got gripped with the desire to learn some shell scripting. That kind of thing never pays.

8:30pm. https://youtu.be/UVUd9_k9C6A
PowerShell For Beginners Full Course | PowerShell Beginner tutorial Full Course

8:35pm. Wow, it is going to download all of Antti's songs, but it is not putting them in order.

https://github.com/ytdl-org/youtube-dl/blob/master/README.md#output-template

Who is going to rename all those things by hand.

```
$ youtube-dl --get-filename -o '%(title)s.%(ext)s' BaW_jenozKc
youtube-dl test video ''_ä↭𝕐.mp4    # All kinds of weird characters

$ youtube-dl --get-filename -o '%(title)s.%(ext)s' BaW_jenozKc --restrict-filenames
youtube-dl_test_video_.mp4          # A simple file name

# Download YouTube playlist videos in separate directory indexed by video order in a playlist
$ youtube-dl -o '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' https://www.youtube.com/playlist?list=PLwiyx1dc3P2JR9N8gQaQN_BCvlSlap7re

# Download all playlists of YouTube channel/user keeping each playlist in separate directory:
$ youtube-dl -o '%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' https://www.youtube.com/user/TheLinuxFoundation/playlists

# Download Udemy course keeping each chapter in separate directory under MyVideos directory in your home
$ youtube-dl -u user -p password -o '~/MyVideos/%(playlist)s/%(chapter_number)s - %(chapter)s/%(title)s.%(ext)s' https://www.udemy.com/java-tutorial/

# Download entire series season keeping each series and each season in separate directory under C:/MyVideos
$ youtube-dl -o "C:/MyVideos/%(series)s/%(season_number)s - %(season)s/%(episode_number)s - %(episode)s.%(ext)s" https://videomore.ru/kino_v_detalayah/5_sezon/367617

# Stream the video being downloaded to stdout
$ youtube-dl -o - BaW_jenozKc
```

I wish I could put this into a script.

> .\youtube-dl.exe -o "%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s" https://soundcloud.com/anttimartikainen/sets/carmina-gloria

Oh, if I just put in an entire album like this it works to fetch them all.

9:05pm.

```
$path = "youtube-dl.exe"
$url = "https://soundcloud.com/anttimartikainen/sets/carmina-gloria"
$arglist = "-o '%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' $url"
Invoke-Command "./$path $arglist"
```

Damn it, I am trying to run shit, but nothing is working as intended. At this time I really wish I was using Python.

```
$path = "youtube-dl.exe"
$url = "https://soundcloud.com/anttimartikainen/sets/carmina-gloria"
$arglist = "-o '%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' $url"
Start-Process -FilePath $path -ArgumentList $arglist
```

When I try this the script starts and then turns off. How can I make it show the output?

```
By default, the Start-Process cmdlet does not show the output of the process that it starts. To show the output, you can use the -NoNewWindow parameter to start the process in the current console window.
```

Bing is actually helpful. I keep underestimating it.

```
$path = "youtube-dl.exe"
$url = "https://soundcloud.com/anttimartikainen/sets/carmina-gloria"
$oargs = "'%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s'"
Start-Process -FilePath $path -ArgumentList "-o", $oargs, $url -NoNewWindow -Verbose -Wait
```

I am making progress, but this shit just refuses to run.

```
PS E:\Simulacrum - Heaven's Key\Youtube-dl> ./script.ps1
VERBOSE: Performing the operation "Start-Process" on target "youtube-dl.exe -o '%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' https://soundcloud.com/anttimartikainen/sets/carmina-gloria".
ERROR: '-' is not a valid URL. Set --default-search "ytsearch" (or run  youtube-dl "ytsearch:-" ) to search YouTube
```

Just, why, why?

```ps1
$path = "youtube-dl.exe"
$url = "https://soundcloud.com/anttimartikainen/sets/carmina-gloria"
$oargs = '"%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s"'
Start-Process -FilePath $path -ArgumentList '-o', $oargs, $url -NoNewWindow -Verbose -Wait
```

This works, for fuck's sake.

```ps1
$path = "youtube-dl.exe"
$url = "https://soundcloud.com/anttimartikainen/albums"
$oargs = '"%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s"'
Start-Process -FilePath $path -ArgumentList '-o', $oargs, $url -NoNewWindow -Verbose -Wait
```

Now, I can get all his albums in the order I want.

```ps1
$path = "youtube-dl.exe"
$url = "https://soundcloud.com/anttimartikainen/albums"
$output = '-o "%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s"'
Start-Process -FilePath $path -ArgumentList $output, $url -NoNewWindow -Verbose -Wait
```

This should work as well.

I can just run this script directly `./script.ps1`. Also VS Code has good Intellisense for these. It is easier to use than Rider.

This also tells me where I went wrong with F# when trying to open these.

```fs
open System.Diagnostics

let psi = ProcessStartInfo("qwe","qwe")
psi.CreateNoWindow <- true
let q = Process.Start("")
q.WaitForExit()
```

Sigh, now I'll know how to start a process.

Nevermind it. I'll admit the ps1 way is more elegant. But I could more easily abstract things in F#.

```fs
open System.Diagnostics

// Start-Process -FilePath $path -ArgumentList $output, $url -NoNewWindow -Verbose -Wait
let run path args =
    let psi = ProcessStartInfo(path,args |> String.concat " ")
    psi.RedirectStandardOutput <- true
    psi.CreateNoWindow <- true
    let q = Process.Start(psi)
    q.WaitForExit()

let path = "youtube-dl.exe"
let url = "https://soundcloud.com/anttimartikainen/albums"
let output = """-o "%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s" """
run path [output; url]
```

No, it is not good. Unlike with the powershell, I can't figure out how to redirect the output to the terminal.

Those FAKE build scripts had the answer.

Let me check them out.

```fs
open System.Diagnostics

// Start-Process -FilePath $path -ArgumentList $output, $url -NoNewWindow -Verbose -Wait
let run path args =
    let psi = ProcessStartInfo(path,args |> String.concat " ")
    psi.RedirectStandardOutput <- true
    psi.CreateNoWindow <- true
    let q = Process.Start(psi)
    task {
        while q.StandardOutput.EndOfStream = false do
            let! x = q.StandardOutput.ReadLineAsync()
            printfn "%s" x
    } |> ignore
    q.WaitForExit()

let path = "youtube-dl.exe"
let url = "https://soundcloud.com/anttimartikainen/albums"
let output = """-o "%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s" """
run path [output; url]
```

Yeah, this is the correct way.

```fs
open System.Diagnostics

let run path args =
    let psi = ProcessStartInfo(path,args |> String.concat " ")
    psi.RedirectStandardOutput <- true
    psi.CreateNoWindow <- true
    let q = Process.Start(psi)
    while q.StandardOutput.EndOfStream = false do
        let x = q.StandardOutput.ReadLine()
        printfn "%s" x
    q.WaitForExit()

let path = "youtube-dl.exe"
let url = "https://soundcloud.com/anttimartikainen/albums"
let output = """-o "%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s" """
run path [output; url]
```

In fact, it doesn't need to be async at all.

But this is 16 lines of F# to do what 4 lines of PS would out of the box. It also has a longer startup.

10:10am. Sigh, I do not know what has gotten into me. I guess I really wanted to know how to execute commands from inside scripts like I would from the command line. Well, now I sure know how.

The Youtube-dl tool will be quite useful.

10:20am. Sigh, so many of his sounds are great.

Sound of Courage especially.

Do I want to risk copyright infringement just to put these in my video?

Realistically, I can't.

10:25pm. But is it really infringment or just regular sharing and fair use. I am not actually sure in my case. I sent him a message a few days ago and since he hasn't answered, maybe it would be fine?

5/31/2023

7:25am. I ended up pushing myself too hard yesterday, what with messing with running command line scripts and now I am paying the price. I didn't get enough sleep. I guess overwork puts me in a mental state where I cannot rest properly.

I didn't think I was overworking myself, but my mental condition is quite poor right now.

I wish I could just press a switch and go back to sleep.

https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.process.standardoutput?view=net-7.0

Now I am reading up on this.

```fs
let run path args =
    let psi = ProcessStartInfo(path,args |> String.concat " ")
    psi.RedirectStandardOutput <- true
    psi.CreateNoWindow <- true
    let q = Process.Start(psi)
    q.StandardOutput <- System.Console.OpenStandardOutput()
    while q.StandardOutput.EndOfStream = false do
        let x = q.StandardOutput.ReadLine()
        printfn "%s" x
    q.WaitForExit()
```

I thought the it might be possible to just set the standard output to input rather than reading it all the way like this, but that is not the case.

7:45am. Forget this. Let me put the soundtracks into the video. It is just too much for me to fill out 2.5 hours with free content.

7:50am. This is causing me some consternation, but if it become an issue, I'll apologize to the guy, take the video down and reupload it with different tracks.

It is free advertizing for the author, and I am not making money of these videos, so it shouldn't cause an issue.

8:10am. I am going to just relax a while today. Forget programming.

8:50am. I watched my own screencast for a while with the music. It is pretty good. Let me render it.

8:55am. It will take a while. While that is happening let me make a thumbnail.

9:10am. It is only a bit further than 30m in into the video. Rendering does take a while.

I did the thumb.

9:30am. Uah, I am just wasting time right now.

Did I commit yesterday?"

---
## [Offroaders123/Smart-Text-Editor](https://github.com/Offroaders123/Smart-Text-Editor)@[f4a9f41954...](https://github.com/Offroaders123/Smart-Text-Editor/commit/f4a9f41954bc680149e0800eab56461d7d4c3ad0)
#### Wednesday 2023-05-31 08:16:49 by Offroaders123

Vite Build!!

Bringing even more over from Dovetail! Got Vite working over there last week I think it was, and it really was a good step towards understanding how to set things up to work properly with a bundler. This is very nice for doing more with STE, as now I can start using npm packages directly, without any module resolution issues! Now it will bundle them as part of the app's code. Of course, I probably won't change my way of doing things just because of that, but it certainly opens the doors of way more things that are viably possible and actionable now. Did a little demo project with React, TypeScript, and Vite the other day, and it was actually fairly simple to get working! I really liked it. The only thing I didn't like was the bundle fluff that adding React added to the app size. Not that it's that big of a deal, since it's easy to add it now, but made me understand how people say it can be a bit overkill to add sometimes when your project can simply work great with the vanilla web stack. if you need more though, than go ahead. I think the noteworthy part is that sometimes people will choose the steamroller to put the tent stake in the ground. Maybe that's a bit overkill of a comparison, but I guess that follows it's own point, so I like it hehe.

Here's an article I read about that, the emphasis part being "Would you use an industrial-strength data engineering framework to schlep around a couple of 4MB spreadsheets?".

https://rhetoricize.medium.com/when-you-dont-need-react-934e20baf636

Listened to a lot of music today, also revisiting "Instrumental Math Rock Mix" tonight, I think I both either really like this playlist, or I'm in the coding zone finally (today's been challenging for that for some reason, I think it's because I got a brain road block on NBTify from working on it so much recently).

https://www.youtube.com/watch?v=3egXqihisFQ

My next step for STE and Dovetail is to get Vite config tooling working so I can have full TypeScript Service Workers working! That will be sick 🔥

---
## [AysheDaArtist/Liberty-Station-13](https://github.com/AysheDaArtist/Liberty-Station-13)@[0f74820c9d...](https://github.com/AysheDaArtist/Liberty-Station-13/commit/0f74820c9d04762ac5b06907e6eb5207be80f136)
#### Wednesday 2023-05-31 08:25:01 by ThePainkiller

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
## [RaccoonBoyG/urfu](https://github.com/RaccoonBoyG/urfu)@[92891ef9ef...](https://github.com/RaccoonBoyG/urfu/commit/92891ef9ef8fd8835844192043b359324743f97b)
#### Wednesday 2023-05-31 09:41:20 by Régis Behmo

feat: persistent bind-mounts

This is an important change, where we get remove the previous `--mount`
option, and instead opt for persistent bind-mounts.

Persistent bind mounts have several advantages:
- They make it easier to remember which folders need to be bind-mounted.
- Code is *much* less clunky, as we no longer need to generate temporary
  docker-compose files.
- They allow us to bind-mount host directories *at build time* using the
  buildx `--build-context` option.
- The transition from development to production becomes much easier, as
  images will automatically be built using the host repo.

The only drawback is that persistent bind-mounts are slightly less
portable: when a config.yml file is moved to a different folder, many
things will break if the repo is not checked out in the same path.

For instance, this is how to start working on a local fork of
edx-platform:

    tutor config save --append MOUNTS=/path/to/edx-platform

And that's all there is to it. No, this fork will be used whenever we
run:

    tutor images build openedx
    tutor local start
    tutor dev start

This change is made possible by huge improvements in the build time
performance. These improvements make it convenient to re-build Docker
images often.

Related issues:
https://github.com/openedx/wg-developer-experience/issues/71
https://github.com/openedx/wg-developer-experience/issues/66
https://github.com/openedx/wg-developer-experience/issues/166

---
## [spockye/tgstation](https://github.com/spockye/tgstation)@[b3f5dfae14...](https://github.com/spockye/tgstation/commit/b3f5dfae1418d4ac24df666e00ca47aef08c9dad)
#### Wednesday 2023-05-31 10:05:23 by san7890

Config Flag to Save Generated Spritesheets to Logs (#74884)

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

---
## [vdaular/linksfordevs](https://github.com/vdaular/linksfordevs)@[10197f63a9...](https://github.com/vdaular/linksfordevs/commit/10197f63a99e91e1d53f6a6bb64da04a7695516a)
#### Wednesday 2023-05-31 10:09:33 by Ben Dornis

Updating: 5/30/2023 9:00:00 PM

 1. Added: Language Pragmatics Engineering
    (https://borretti.me/article/language-pragmatics)
 2. Added: Hacking my “smart” toothbrush
    (https://kuenzi.dev/toothbrush/)
 3. Added: Would you hire ChatGPT?
    (https://www.davekonopka.com/2023/05/would-you-hire-chatgpt/)
 4. Added: alexw.nyc -- duskos-1.html
    (https://alexw.nyc/tech/duskos-1.html)
 5. Added: Expected performance of a Bloom filter
    (https://lemire.me/blog/2023/05/26/expected-performance-of-a-bloom-filter/)
 6. Added: When the rubber duck talks back
    (https://blog.jonudell.net/2023/05/24/when-the-rubber-duck-talks-back/)
 7. Added: Understanding JSONata
    (https://yokota.blog/2023/05/29/understanding-jsonata/)
 8. Added: 1 Maxim, 2 Sides
    (https://gigatexal.blog/pages/two-sides-one-coin/two-sides-one-coin.html)
 9. Added: Keeping software soft
    (https://cbh.bearblog.dev/keeping-software-soft/)
10. Added: Developer joy with Scott Hanselman and friends | BRK291HFS
    (https://youtube.com/watch?v=LFK7KYL__Rk?list=RDCMUCsMica-v34Irf9KVTh6xx-g)
11. Added: Rust: The wrong people are resigning
    (https://fasterthanli.me/articles/rust-the-wrong-people-are-resigning)

Generation took: 00:06:44.4110527
 Maintenance update - cleaning up homepage and feed

---
## [nafmo/git-l10n-sv](https://github.com/nafmo/git-l10n-sv)@[eb1c42da8e...](https://github.com/nafmo/git-l10n-sv/commit/eb1c42da8e21cc2a8dacd21023a179b788858887)
#### Wednesday 2023-05-31 12:16:46 by Jeff King

t/lib-httpd: make CGIPassAuth support conditional

Commit 988aad99b4 (t5563: add tests for basic and anoymous HTTP access,
2023-02-27) added tests that require Apache to support the CGIPassAuth
directive, which was added in Apache 2.4.13. This is fairly old (~8
years), but recent enough that we still encounter it in the wild (e.g.,
RHEL/CentOS 7, which is not EOL until June 2024).

We can live with skipping the new tests on such a platform. But
unfortunately, since the directive is used unconditionally in our
apache.conf, it means the web server fails to start entirely, and we
cannot run other HTTP tests at all (e.g., the basic ones in t5551).

We can fix that by making the config conditional, and only triggering it
for t5563. That solves the problem for t5551 (which then ignores the
directive entirely). For t5563, we'd see apache complain in start_httpd;
with the default setting of GIT_TEST_HTTPD, we'd then skip the whole
script.

But that leaves one small problem: people may set GIT_TEST_HTTPD=1
explicitly, which instructs the tests to fail (rather than skip) when we
can't start the webserver (to avoid accidentally missing some tests).

This could be worked around by having the user manually set
GIT_SKIP_TESTS on a platform with an older Apache. But we can be a bit
friendlier by doing the version check ourselves and setting an
appropriate prereq. We'll use the (lack of) prereq to then skip the rest
of t5563. In theory we could use the prereq to skip individual tests, but
in practice this whole script depends on it.

Reported-by: Todd Zullinger <tmz@pobox.com>
Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [krzkro4122/uj_chess-solver](https://github.com/krzkro4122/uj_chess-solver)@[2f08bed66c...](https://github.com/krzkro4122/uj_chess-solver/commit/2f08bed66ce885064a85d8b7b3acc58f3bc09661)
#### Wednesday 2023-05-31 13:40:59 by krzkro4122

Omg i fucking hate this game, stalemate improvements, bug hunting

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[cb1388ed9e...](https://github.com/odoo-dev/odoo/commit/cb1388ed9e64ced4e0d85cf5778192dfbdfd5995)
#### Wednesday 2023-05-31 13:52:56 by Jeremy Kersten

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
## [TomaszGaweda/hazelcast](https://github.com/TomaszGaweda/hazelcast)@[5f414fa3ad...](https://github.com/TomaszGaweda/hazelcast/commit/5f414fa3ad03417e0b9078c8d9f249904003c936)
#### Wednesday 2023-05-31 13:54:57 by James Holgate

Modify KubernetesClient shutdown behaviour [HZ-1921] (#24613)

The overall goal of this change is to change the shutdown behaviour of
KubernetesClient so our Stateful Set monitor thread shuts down before
our `ClusterTopologyIntentTracker`, to allow the intent tracker to fully
process all completed messages before Node shutdown.

**The Current Problem**
In its current state, the Stateful Set monitor thread is intended to
shutdown after `Thread#interrupt` is called, triggering the
`Thread#interrupted` check within the main `while(running)` loop of the
Runnable. However, this check is not reached as the call to
`WatchResponse#readLine` from within the main `run()` method is a
blocking call that waits until data is available to read before
proceeding. Since this call waits for non-null data before completing,
the result is always non-null, and therefore this code block never exits
under normal conditions:
```java
while ((message = watchResponse.nextLine()) != null) {
    onMessage(message);
}
```

Since this `while` loop cannot exit, and the `#readLine` method (which
passes to `BufferedReader#readLine` under the hood) is a blocking I/O
operation which cannot be interrupted, this operation does not end when
`Thread#interrupt` is called. This leads to the Stateful Set monitor
thread out-living the `ClusterTopologyIntentTracker`, even if the
StsMonitor is interrupted first. As a result, during shutdown, it is
possible for the StsMonitor to send data to the intent tracker after it
has been destroyed and its executor is no longer accepting tasks.

**The Root of the Problem**
To reach our goal of ensuring that the Stateful Set monitor thread can
no longer send requests to the `ClusterTopologyIntentTracker`, we need
to add synchronization between the two objects that guarantees the
intent tracker shuts down after the StsMonitor thread has completed.
This can be achieved using a simple `CountDownLatch` which is counted
down after the thread has completed, and awaited before shutting down
the tracker.

The main obstacle to achieving this is, as mentioned above, that the
StsMonitor thread cannot be interrupted when waiting for
`WatchResponse#readLine` to complete, and so the thread never completes.
The only way this thread can complete is to either force its
termination, or alter the message reading approach to allow interruption
as intended.

**Identifying Resolution Paths**
We don't want to force termination of our Stateful Set monitor thread as
this could result in message handling being terminated after it has been
received, but not before it has finished being processed. Therefore the
only way we can allow this thread to be interrupted as intended is to
alter the message reading mechanics in a way that allows it to be
interrupted as well.

There is no way for us to know if more messages are pending from the k8s
watch besides waiting for data to be received, so the best we can do is
allow the StsMonitor to finish processing any messages it has already
received (preventing process corruption), but terminate the stream of
new messages it is waiting for before we shutdown the intent tracker.

**Potential Solutions**
So we've identified the root of the problem as our `#readLine` function
blocking through interrupts, so how do we make it interruptible? Sadly
one of the shortcomings of I/O operations in Java is that they usually
cannot be interrupted in the traditional manner, so we have a few
approaches to consider:

1) We could modify the message reading code to use
`BufferedReader#ready` and `Thread#sleep` to periodically check if there
is data to be read before calling any read functions. The problem with
this approach is that A) `#ready` returns true if any data is available,
not just if there is a full line of data to be read; and B) utilizing a
sleep loop can result in delayed message handling at the least, or
busy-waiting overhead at worst.

2) We could use "hacky" solutions to interrupt the
`BufferedReader#readLine` such as closing underlying sockets or
connections, propagating an exception to the reader. The problem with
this solution is that everything related to our reading operation is
handled in `syncrhonized` blocks, and since our shutdown process starts
outside the StsMonitor thread, our calling thread is unable to obtain
these locks (being held by the StsMonitor)!

3) It's possible that we could rewrite the `WatchResponse` mechanics to
use Java NIO magic such as `Selector` for interruptible I/O operations.
The issue with this approach is that it would require fairly significant
refactoring of the related codebase, and may not end up providing the
exact functionality we are looking for in our use case.

4) We can introduce an `Executor` to handle our I/O operations within
the StsMonitor thread, allowing us to wait on a `Future#get` call
instead of our `BufferedReader#readLine` call, where a `Future#get`
operation can be interrupted by the waiting thread being interrupted.
The downside to this solution is we have to introduce an additional
thread on top of the existing StsMonitor thread itself.

**Selecting a Solution**
Considering the above information, I concluded the most sensible
approach was to use (4) and introduce an `Executor` thread for the I/O
operations. By using a separate thread for this call we can be rougher
with it, as we know that worse case scenario we interrupt a message
being read that has not started being processed yet (but we're shutting
down anyway).

This solution also allows for the least amount of underlying code
changes, as our `Future#get` can be interrupted without issue,
maintaining the current approach used for handling the StsMonitor
shutdown. The only downside for this approach is the addition of another
thread alongside the StsMonitor thread, but the actual impact of this
should be minimal as both threads will still be waiting most of the
time, so the only negative impact is being 1 tiny step closer to
possible thread starvation.

Generally I think this is the best solution at hand which allows quick
shutdown of the StsMonitor thread while minimising potential for data
loss or corruption. Combined with the `CountDownLatch` used, this allows
for consistent service shutdown order between the `StsMonitor` thread
and the `ClusterTopologyIntentTracker`.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[9a7a7ad24a...](https://github.com/mrakgr/The-Spiral-Language/commit/9a7a7ad24a5d97d86990ff5d34cf482e97a1f58d)
#### Wednesday 2023-05-31 14:08:38 by Marko Grdinić

"I forgot, it seems.

9:45am. https://youtu.be/H3oD7-k3jB0
Top 5 Must Have Stable Diffusion Extension

I got asked about extensions twice. I want to stop programming for a bit and look into art again as I said in the outro. Maybe I'll start writing Hatred.

https://youtu.be/H3oD7-k3jB0?t=46

It is talking about a rest API here.

Actually, why don't I make my next project to integrate Helix with the PS account?

https://youtu.be/H3oD7-k3jB0?t=51

Image Browser?

That seems like a good extension to have.

9:50am. The video still hasn't finished rendering, but it is at 80-90%.

https://youtu.be/H3oD7-k3jB0?t=344

This is interesting.

I got asked twice on how to make extensions work, so I am dreading trying to do anything with this WebUI. But I think it is high time I try the ComfyUI.

Let's not get swayed by what people by asking me on Youtube.

How about I try getting the ComfyUI to work. Right now my PS subscription is just wasting money every month.

https://youtu.be/H3oD7-k3jB0?t=510

Damn, the art generation has gotten sophisticated.

https://youtu.be/l_X9E_Xd3OA?t=172

What is this InvokeAI thing?

It is made in .NET.

Hmmm, they are moving to a Nodes backend.

10:10am. It is uploading the Render to Youtube, so my connection has ground to a halt.

https://www.youtube.com/results?search_query=invokeai
https://www.youtube.com/watch?v=aCjirmA_-zs
https://www.youtube.com/watch?v=gySLXbe7WZQ

Ah, forget this. The internet connection is taken up by the upload.

10:10am. ...And now it broke. The file is 3gb, so it is not easy to upload it.

10:15am. Wait, I think the upload actually went through. It says it is processing the video.

> Converting The Leduc Project From Fable React To Blazor

```
In this video, as a part of our move from Fable React to Blazor in the VN compiler project, we go back to an older one and spend a few days to rewrite it Blazor. We go through it all, from rewriting the UI from a Fable React backend, to a Blazor one, to replacing the old charting component, to publishing it online. We got taken by surprise by Blazor WASM not having multithreading, so we'll have to go back late in the year, and republish it as a static web app.

We ran into many weird issues with Blazor itself, and anybody coming into Blazor might be interested in seeing how we overcome them.

Playlist (Webdev): https://youtube.com/playlist?list=PL04PGV4cTuIX3bNEDDyi1L27Si0qpyAJ7
Code: https://github.com/mrakgr/CFR-In-Fable/tree/blazor1
Website: https://mrakgr-cfr-in-blazor.azurewebsites.net/

#fsharp #blazor #aspnetcore #dotnet #csharp #webdevelopment

Music:

https://soundcloud.com/anttimartikainen/sets/the-sound-of-courage
https://soundcloud.com/anttimartikainen/sets/sonic-savior

TOC:

00:00:00 - Intro
00:00:10 - The ideal mental state for rewrites
00:01:52 - Starting a new Blazor project and setting it up
00:04:24 - The Rewrite
00:08:33 - Factoring small components into methods
00:09:56 - Weird type error
00:11:53 - The slow slog to deal with the GameUI
00:19:26 - Installing Fluxor and bringing in the rest of the types
00:24:58 - Uninstalling Fluxor and doing our own state management
00:32:57 - Figuring out how to construct an F# union type in C#.
00:35:10 - [EditorRequired]
00:35:39 - Day two
00:39:38 - MenuUI
00:43:49 - Refactoring the types
00:46:53 -The Table
00:53:59 - Doing the Train Menu in a single function
01:03:34 - Why doesn't the Train Menu compile as a static method?
01:04:46 - Bizzare component inheritance bug
01:05:28 - F# 'dotnet watch run' issue
01:05:45 - Blazor component inheritance is broken!!!
01:06:00 - The time I'd condone copy pasting
01:06:55 - Why is the UI not updating?
01:07:35 - Introducing Apex Charts
01:09:40 - How to resolve the Blazor .NET 7 inheritance problems
01:10:43 - Trying out ApexCharts
01:14:19 - Figuring out the type errors in Apex Charts
01:16:07 - Why is an IEnumerable passed as the Y value?
01:17:21 - How to size the Apex Charts
01:19:16 - Rerouting the dependencies onto the Blazor.Client.Fun project
01:21:05 - Marker 29
01:22:59 - Removing Paket
01:25:55 - Implementing the IDisposable interface for the ViewComponent
01:26:50 - Type wrangling
01:32:02 - Renaming a project breaks it
01:35:49 - Finishing the rewrite
01:40:29 - Forgot the charts
01:42:23 - Blazor child components
01:43:41 - Type aliasing is not working
01:46:23 - The IDE is really killing me here
01:46:55 - C# is really killing me here
01:47:40 - The debugging phase
01:49:50 - Weird MailboxProcessor bug
01:52:25 - The MailboxProcessor is buggy
01:56:06 - Day 4. Migrating from WASM to Server
01:58:39 - Migration confusion
02:02:58 - Why aren't the Apex Charts loading?
02:03:15 - Blazor Server has a lot of startup issues
02:05:05 - Dealing with the UI thread concurrency issue
02:10:53 - Increasing the Blazor SignalR message size
02:11:15 - I have no idea why this error is happening
02:11:25 - Dealing with the concurrency error
02:13:59 - Why is the Apex Chart not updating in Blazor Server mode
02:17:31 - Virtualizing the table
02:19:19 - Getting the chart to work right
02:22:47 - Finishing the rewrite
02:28:13 - Publishing CFR In Blazor as an Azure Web App
02:33:56 - Outro
```

Here is the description. It says it will begin processing the video, but did it really finish downloading it?

Hmmm, there isn't a download button.

No, I do not trust this.

10:35am. My internet connection is useless while the upload is going on.

It will take 20m for it to upload.

Wow, my uploads are actually quite high. 25Mbps.

That is like 3 megabytes per second.

Right now, in the general area we reside, they are laying down optic cables, so we'll get 50 times faster internet speeds once they are installed. I don't know when that will be done.

10:50am. The upload finished.

Youtube will check for copyrighted content. I guess I'll see if the video passes with that.

> Copyright-protected content found. The owner allows the content to be used on YouTube.

Oh this is great!

I am really glad, this is the case, that means I do not have to worry about the videos being taken down.

https://youtu.be/L6Af5RlZzN8
Converting The Leduc Project From Fable React To Blazor

Here is the video. I've scheduled it in 3 hours, right now it is being processed up to HD.

It is not worth posting until that happens.

11am. I'll come back to it later, forget it for now. it says it will take 110 minutes for it to finish processing in HD.

11:05am. https://nightcorenovels.com/novel/i-became-a-witch-in-a-world-full-of-urban-legends/volume-1/chapter-31/

I am still thinking what I want to do as I take this break today.

Yeah, people are asking by extensions, but that is no reason for me start diving into them. I should only be getting back to PS once I have a need for it.

Forget it for now.

Instead of doing this, how about I work more on Helix? Once I add the image nodes, the replay buffer, the SQLite database for saving indivdiual files, at that point I'll actually have something useful, and something that I'll be able to use as a tool to help me write Hatred.

Then once I start writing and making images, I'll look into to optimizing my art workflow.

It is a mistake to skip stages.

11:15am. Sure, I'll get less Youtube views and subscribes this way, but the point of this is to showcase my programming skills, not anything else.

...Right now, I am doing a search on Youtube for downloading soundcloud files, and it doesn't seem like there is a tutorial for it. I'll make one.

11:25am. I guess I might as well do it.

I'll record this one myself as an exercise.

11:30am. No, I have to split it up.

I'll do the recording separately from the screencast, it is too distracting to do it normally.

https://obsproject.com/forum/threads/is-it-possible-to-only-record-audio-using-obs.75369/

I want to figure out how I could solely output as an audio.

No, I'll use something other than OBS. Maybe Reaper?

It is just too annoying having to deal with Mkv files in here.

Or maybe not. I could drag them in edit mode.

12:30pm. 3:13m for this video is enough.

Doing it like this without backtracking is not too bad. It still needs some editing, but I could see myself producing content this way.

Sure, I my language fluency is making me look stupid, but that is fine.

If I want to get better at spoken screencasting, it is important to keep practicing. I've offloaded the burden to Vilo, but I should get a bit better myself.

The first step towards that is to stop trying to perfect the screencast.

1:10pm. Finally making toast. I forgot to post the video on the F# sub and Twitter.

1:50pm. Let me chill for a while and then I'll post the video on Twitter, I ended up doing a lod during breakfast.

2:30pm. Ok, time to put that project behind me. I should start a new thing, but I really don't feel like it.

2:40pm. I am thinking.

I am rather strained right now, and do not feel like programming.

For the image nodes, instead of straightforward image nodes, couldn't I build something like an image browser?

An image browser that could browse my PS notebooks.

3:45pm. No, I won't post this.

```
You're the author? I do not understand your sarcasm. Do you think that C would be just as good as statically typed functional languages at writing compilers? Or you don't, but think that your steely will and sharp wit is enough to get you anything as a programmer?

But the thing is, those 50-100k lines probably aren't too far from the limit of what you can maintain. If you run into a project that would require you to lift 500-1,000k LOC, then you won't be able to do it, not without reaching for a tool to bring that down by 10x.

I am also not sure, whether you free all your memory on compiler termination or use manual mem management, but if you ever want to make editor plugin for you language, you'll need 90% of the data structures in the compiler to be immutable, and that is going to be very difficult in C.
```

Why argue with that idiot?

https://github.com/Mikubill/sd-webui-controlnet/discussions/

Check out 1464.

Inpaint improvements.

///

It is time to resume the Helix project. Damn, that rewrite took a while, but we learned a lot.
We are downplaying our own web dev skills, but we can do quite a lot now.
Right now we are at a fork.
A part of us wants to go back to Stable Diffusion and check out Comfy UI and other innovations that have come out in the past few months.
But...
We are definitely feeling strained from the effort.
Yesterday we went late to bed due to researching how to download tracks off sound cloud, so check out the video in the card if you are interested, but this bit of overwork ensured that the sleep we got wasn't enough to get rid of the fatigue fully.
So right now, before we start doing anything, let us think what we want to do.
A part of us feels envious at those UIs coming out for stable diffusion.
We want to prove our skills.
But it is important that we separate what we want, from what we need.
We could sit down, and spend the next couple of months replicating comfy ui in Blazor, but what would that prove?
Right now we are thinking about the image nodes, and realizing, that as cool it would be to have our own Stable Diffusion UI, would we be gaining that much more compared to just building a file watcher node?
By that we mean a kind of image node, in addition to the regular one, that watches our Paperspace Gradient Notebook for changes and downloads the images automatically as they get deposited onto storage.
That would be a thousand times easier to build than a fully fledged node based UI.
Ultimately, the right way to program is to create whatever gives you the most bang for the buck.
It is a mistake to think that you need to put in a lot of effort to get a lot utility.
The best thing is always to build systems that work with existing ones rather than try to replace them wholesale.
We should be looking into existing systems, and finding the best way to have our own interact with them rather than starting ambitious projects.
That is something we should be teaching you.
Right now we are spewing words, but determining our attitude here will decide whether we want to spend a significant part of our life building novel systems or whether we want to take advantage of the work of others.
Compared to the first one, the latter choice isn't the best showcase of skills, but...
It is not like anybody is interested in our skills anyway.
The Spiral language was enough as a showcase of that.
So we'll focus.
Image nodes, the undo functionality, and the save loading feature.
After that comes compilation to html sites.
After that we'll be able to both get a job and start work on Simulacrum Hatred.
Well, who knows about the former, but we certainly don't intend to spend all our time just programming like we have for the past few months.
Programming is at its best when it enables better art. What are games, but that?
Maybe at some point in future the this prelude to the Singularity will become like the one we dreamed of.
The Singularity where programs are super powers fueled by computation.

///

4:05pm. I am going to take a break. These last few days took far too much out of me, and I just want to do nothing.

I'll close here for today, and dedicate myself to programming tomorrow."

---
## [sourcegraph/sourcegraph](https://github.com/sourcegraph/sourcegraph)@[753ef33f15...](https://github.com/sourcegraph/sourcegraph/commit/753ef33f151752ca94942ba890277587a828bf9a)
#### Wednesday 2023-05-31 14:55:20 by Valery Bugakov

cody-slack: #ask-cody context and GPT-4 streaming (#51194)

⚠️ This PR changes code only inside of the `cody-slack` package. All the
other client packages are untouched.

I'll be moving Cody Slack to GCP, so I need to merge the PR with
[functionality](https://sourcegraph.slack.com/archives/C89KCDK5J/p1682506053493149)
before that:

- [#ask-cody](https://sourcegraph.slack.com/archives/C04MSD3DP5L)
Special Context: Struggling to find info on Cody across various sources?
Worry no more! When you ask
[@cody_dev](https://sourcegraph.slack.com/team/U051K8MBM7F) a question
in the [#ask-cody](https://sourcegraph.slack.com/archives/C04MSD3DP5L)
channel, it now searches Cody-notice, developer docs, the handbook, and
the sg/sg codebase to provide the best possible answer. :mag:
- Files Used Section:
[@cody_dev](https://sourcegraph.slack.com/team/U051K8MBM7F) will now
share links to all the files it "used" while answering your questions.
This means you can easily verify the information and explore related
resources! :file_folder:
- Slack Markdown Support: Answers are now beautifully formatted and
compatible with GitHub-flavored markdown. Enjoy a more readable and
visually appealing experience! :sparkles:
- Powered by GPT-4: I've updated
[@cody_dev](https://sourcegraph.slack.com/team/U051K8MBM7F) to use GPT-4
for better reasoning capabilities and an enhanced understanding of Slack
conversations. Get ready for more accurate and insightful answers!

---
## [Dev-msm8953/kernel_xiaomi_msm8953](https://github.com/Dev-msm8953/kernel_xiaomi_msm8953)@[09ff09f8b8...](https://github.com/Dev-msm8953/kernel_xiaomi_msm8953/commit/09ff09f8b85c43913f3909e162d528eb02aad385)
#### Wednesday 2023-05-31 14:59:53 by Angelo G. Del Regno

Makefile.lib: Lower kernel gzip compression to fastest

You're reading this - so you're trying to understand "JUST WHY OMG".
That's already a good step.

First of all, this is a downstream kernel - always keep that in mind!
Now, this kernel is targeting new *very powerful* Qualcomm platforms
like SM8250 and the Sony Edo platform - which has a very fast UFS card.

Keep in mind that the bootloader sets the CPU at a frequency that is
slightly faster than the "in the middle" ones, which is anyway not
veeeery fast - but that's good, really. I agree.

So.. check this out:   for Image.gz-dtb.....
COMP_LEVEL    SIZE
9             20116171
5	      20220479
2	      20940223
1	      21231290

Remember again that we're loading from a UFS card and that
we are loading ~1.1MB more out of a 20MB file.
If you're smart enough you surely know already about RAM and CPU
overhead of very high compression levels.

If you still disagree with what I just did, read this commit description
another 20 times, or more, until you understand it. :)))

Signed-off-by: TogoFire <togofire@mailfence.com>
Change-Id: Iadc5e2bc0c6e1cb60328ed0d71d851ea106420ca

---
## [Sagnac/fresdet](https://github.com/Sagnac/fresdet)@[7fa7b323f5...](https://github.com/Sagnac/fresdet/commit/7fa7b323f5d1041b694d0ce975732b4297d41227)
#### Wednesday 2023-05-31 15:12:41 by Sagnac

Overload show to clean up the output

Maybe I shouldn't be doing this since the return value is not a custom
type, but having to remember to suppress the output is kind of annoying
and the output is spammy.

The core program is basically a 200+ line function full of hacks anyway
so whatever.

---
## [Random-Machine/LiveSplit.Scripts](https://github.com/Random-Machine/LiveSplit.Scripts)@[1be3ab24d6...](https://github.com/Random-Machine/LiveSplit.Scripts/commit/1be3ab24d6723a326cfe619e7cda40cdeaeccf19)
#### Wednesday 2023-05-31 15:31:31 by Random-Machine

Update LiveSplit.WatchDogs2.asl to Percentage Autosplitter

Makes the autosplitter more robust by using a new percentage variable to split for individual missions. Also adds a lot of options. 

1. Must have No Compromise and Human Conditions DLC uninstalled for the percentages to match up. Must also follow the speedrun route in the WR.
2. Only works on latest patch.
3. Has options for splitting after Walk in the Park, Sunday Schooled, and Mark Up, but they're disabled by default. 
4. Removed old follower count variable & splitting.
5. Still have to manual split for the last split when completing Motherload.
6. Supports splitting for individual missions and has options to disable them.
7. Does not support splitting for these individual missions/cutscenes & call(s) because there isn't much point:
-Intro mission/stuff before Walk in the Park (Buy Pants option was removed.)
-Newly Dawned (False Profits)
-ICU (Wrench Cutscene at start of Heist Sweet Heist)
-Zero Days (Heist Sweet Heist)
-Trouble at Home (Looking Glass)
-Second Wind (Alphabet Soup)
-Nine Lives (Hacker War)
-Café Culture (W4tched)
-The Waiting Game (Hack teh World)
-Spinal Tap (Shanghaied)
-Social Media and the Congressman (Power to the Sheeple)
-Like Minds (Robot Wars)
-Motherload Call (for mission to show up)

---
## [mubasshirarnab/Code_Forces_Problems](https://github.com/mubasshirarnab/Code_Forces_Problems)@[7ae5f47c19...](https://github.com/mubasshirarnab/Code_Forces_Problems/commit/7ae5f47c1934e062835a653dc5328530ad8d2ca2)
#### Wednesday 2023-05-31 15:49:50 by Mubasshir Ahmed Arnab

Add files via upload

One hot summer day Pete and his friend Billy decided to buy a watermelon. They chose the biggest and the ripest one, in their opinion. After that the watermelon was weighed, and the scales showed w kilos. They rushed home, dying of thirst, and decided to divide the berry, however they faced a hard problem.

Pete and Billy are great fans of even numbers, that's why they want to divide the watermelon in such a way that each of the two parts weighs even number of kilos, at the same time it is not obligatory that the parts are equal. The boys are extremely tired and want to start their meal as soon as possible, that's why you should help them and find out, if they can divide the watermelon in the way they want. For sure, each of them should get a part of positive weight.

Input
The first (and the only) input line contains integer number w (1 ≤ w ≤ 100) — the weight of the watermelon bought by the boys.

Output
Print YES, if the boys can divide the watermelon into two parts, each of them weighing even number of kilos; and NO in the opposite case.

---
## [Kneba/platform_kernel_asus_sdm660](https://github.com/Kneba/platform_kernel_asus_sdm660)@[69bdc5fb2b...](https://github.com/Kneba/platform_kernel_asus_sdm660/commit/69bdc5fb2b3ceb8308f68eca9d4f23e0a163d4b5)
#### Wednesday 2023-05-31 15:53:33 by Christian Brauner

BACKPORT: signal: add pidfd_send_signal() syscall

The kill() syscall operates on process identifiers (pid). After a process
has exited its pid can be reused by another process. If a caller sends a
signal to a reused pid it will end up signaling the wrong process. This
issue has often surfaced and there has been a push to address this problem [1].

This patch uses file descriptors (fd) from proc/<pid> as stable handles on
struct pid. Even if a pid is recycled the handle will not change. The fd
can be used to send signals to the process it refers to.
Thus, the new syscall pidfd_send_signal() is introduced to solve this
problem. Instead of pids it operates on process fds (pidfd).

/* prototype and argument /*
long pidfd_send_signal(int pidfd, int sig, siginfo_t *info, unsigned int flags);

/* syscall number 424 */
The syscall number was chosen to be 424 to align with Arnd's rework in his
y2038 to minimize merge conflicts (cf. [25]).

In addition to the pidfd and signal argument it takes an additional
siginfo_t and flags argument. If the siginfo_t argument is NULL then
pidfd_send_signal() is equivalent to kill(<positive-pid>, <signal>). If it
is not NULL pidfd_send_signal() is equivalent to rt_sigqueueinfo().
The flags argument is added to allow for future extensions of this syscall.
It currently needs to be passed as 0. Failing to do so will cause EINVAL.

/* pidfd_send_signal() replaces multiple pid-based syscalls */
The pidfd_send_signal() syscall currently takes on the job of
rt_sigqueueinfo(2) and parts of the functionality of kill(2), Namely, when a
positive pid is passed to kill(2). It will however be possible to also
replace tgkill(2) and rt_tgsigqueueinfo(2) if this syscall is extended.

/* sending signals to threads (tid) and process groups (pgid) */
Specifically, the pidfd_send_signal() syscall does currently not operate on
process groups or threads. This is left for future extensions.
In order to extend the syscall to allow sending signal to threads and
process groups appropriately named flags (e.g. PIDFD_TYPE_PGID, and
PIDFD_TYPE_TID) should be added. This implies that the flags argument will
determine what is signaled and not the file descriptor itself. Put in other
words, grouping in this api is a property of the flags argument not a
property of the file descriptor (cf. [13]). Clarification for this has been
requested by Eric (cf. [19]).
When appropriate extensions through the flags argument are added then
pidfd_send_signal() can additionally replace the part of kill(2) which
operates on process groups as well as the tgkill(2) and
rt_tgsigqueueinfo(2) syscalls.
How such an extension could be implemented has been very roughly sketched
in [14], [15], and [16]. However, this should not be taken as a commitment
to a particular implementation. There might be better ways to do it.
Right now this is intentionally left out to keep this patchset as simple as
possible (cf. [4]).

/* naming */
The syscall had various names throughout iterations of this patchset:
- procfd_signal()
- procfd_send_signal()
- taskfd_send_signal()
In the last round of reviews it was pointed out that given that if the
flags argument decides the scope of the signal instead of different types
of fds it might make sense to either settle for "procfd_" or "pidfd_" as
prefix. The community was willing to accept either (cf. [17] and [18]).
Given that one developer expressed strong preference for the "pidfd_"
prefix (cf. [13]) and with other developers less opinionated about the name
we should settle for "pidfd_" to avoid further bikeshedding.

The  "_send_signal" suffix was chosen to reflect the fact that the syscall
takes on the job of multiple syscalls. It is therefore intentional that the
name is not reminiscent of neither kill(2) nor rt_sigqueueinfo(2). Not the
fomer because it might imply that pidfd_send_signal() is a replacement for
kill(2), and not the latter because it is a hassle to remember the correct
spelling - especially for non-native speakers - and because it is not
descriptive enough of what the syscall actually does. The name
"pidfd_send_signal" makes it very clear that its job is to send signals.

/* zombies */
Zombies can be signaled just as any other process. No special error will be
reported since a zombie state is an unreliable state (cf. [3]). However,
this can be added as an extension through the @flags argument if the need
ever arises.

/* cross-namespace signals */
The patch currently enforces that the signaler and signalee either are in
the same pid namespace or that the signaler's pid namespace is an ancestor
of the signalee's pid namespace. This is done for the sake of simplicity
and because it is unclear to what values certain members of struct
siginfo_t would need to be set to (cf. [5], [6]).

/* compat syscalls */
It became clear that we would like to avoid adding compat syscalls
(cf. [7]).  The compat syscall handling is now done in kernel/signal.c
itself by adding __copy_siginfo_from_user_generic() which lets us avoid
compat syscalls (cf. [8]). It should be noted that the addition of
__copy_siginfo_from_user_any() is caused by a bug in the original
implementation of rt_sigqueueinfo(2) (cf. 12).
With upcoming rework for syscall handling things might improve
significantly (cf. [11]) and __copy_siginfo_from_user_any() will not gain
any additional callers.

/* testing */
This patch was tested on x64 and x86.

/* userspace usage */
An asciinema recording for the basic functionality can be found under [9].
With this patch a process can be killed via:

 #define _GNU_SOURCE
 #include <errno.h>
 #include <fcntl.h>
 #include <signal.h>
 #include <stdio.h>
 #include <stdlib.h>
 #include <string.h>
 #include <sys/stat.h>
 #include <sys/syscall.h>
 #include <sys/types.h>
 #include <unistd.h>

 static inline int do_pidfd_send_signal(int pidfd, int sig, siginfo_t *info,
                                         unsigned int flags)
 {
 #ifdef __NR_pidfd_send_signal
         return syscall(__NR_pidfd_send_signal, pidfd, sig, info, flags);
 #else
         return -ENOSYS;
 #endif
 }

 int main(int argc, char *argv[])
 {
         int fd, ret, saved_errno, sig;

         if (argc < 3)
                 exit(EXIT_FAILURE);

         fd = open(argv[1], O_DIRECTORY | O_CLOEXEC);
         if (fd < 0) {
                 printf("%s - Failed to open \"%s\"\n", strerror(errno), argv[1]);
                 exit(EXIT_FAILURE);
         }

         sig = atoi(argv[2]);

         printf("Sending signal %d to process %s\n", sig, argv[1]);
         ret = do_pidfd_send_signal(fd, sig, NULL, 0);

         saved_errno = errno;
         close(fd);
         errno = saved_errno;

         if (ret < 0) {
                 printf("%s - Failed to send signal %d to process %s\n",
                        strerror(errno), sig, argv[1]);
                 exit(EXIT_FAILURE);
         }

         exit(EXIT_SUCCESS);
 }

/* Q&A
 * Given that it seems the same questions get asked again by people who are
 * late to the party it makes sense to add a Q&A section to the commit
 * message so it's hopefully easier to avoid duplicate threads.
 *
 * For the sake of progress please consider these arguments settled unless
 * there is a new point that desperately needs to be addressed. Please make
 * sure to check the links to the threads in this commit message whether
 * this has not already been covered.
 */
Q-01: (Florian Weimer [20], Andrew Morton [21])
      What happens when the target process has exited?
A-01: Sending the signal will fail with ESRCH (cf. [22]).

Q-02:  (Andrew Morton [21])
       Is the task_struct pinned by the fd?
A-02:  No. A reference to struct pid is kept. struct pid - as far as I
       understand - was created exactly for the reason to not require to
       pin struct task_struct (cf. [22]).

Q-03: (Andrew Morton [21])
      Does the entire procfs directory remain visible? Just one entry
      within it?
A-03: The same thing that happens right now when you hold a file descriptor
      to /proc/<pid> open (cf. [22]).

Q-04: (Andrew Morton [21])
      Does the pid remain reserved?
A-04: No. This patchset guarantees a stable handle not that pids are not
      recycled (cf. [22]).

Q-05: (Andrew Morton [21])
      Do attempts to signal that fd return errors?
A-05: See {Q,A}-01.

Q-06: (Andrew Morton [22])
      Is there a cleaner way of obtaining the fd? Another syscall perhaps.
A-06: Userspace can already trivially retrieve file descriptors from procfs
      so this is something that we will need to support anyway. Hence,
      there's no immediate need to add another syscalls just to make
      pidfd_send_signal() not dependent on the presence of procfs. However,
      adding a syscalls to get such file descriptors is planned for a
      future patchset (cf. [22]).

Q-07: (Andrew Morton [21] and others)
      This fd-for-a-process sounds like a handy thing and people may well
      think up other uses for it in the future, probably unrelated to
      signals. Are the code and the interface designed to permit such
      future applications?
A-07: Yes (cf. [22]).

Q-08: (Andrew Morton [21] and others)
      Now I think about it, why a new syscall? This thing is looking
      rather like an ioctl?
A-08: This has been extensively discussed. It was agreed that a syscall is
      preferred for a variety or reasons. Here are just a few taken from
      prior threads. Syscalls are safer than ioctl()s especially when
      signaling to fds. Processes are a core kernel concept so a syscall
      seems more appropriate. The layout of the syscall with its four
      arguments would require the addition of a custom struct for the
      ioctl() thereby causing at least the same amount or even more
      complexity for userspace than a simple syscall. The new syscall will
      replace multiple other pid-based syscalls (see description above).
      The file-descriptors-for-processes concept introduced with this
      syscall will be extended with other syscalls in the future. See also
      [22], [23] and various other threads already linked in here.

Q-09: (Florian Weimer [24])
      What happens if you use the new interface with an O_PATH descriptor?
A-09:
      pidfds opened as O_PATH fds cannot be used to send signals to a
      process (cf. [2]). Signaling processes through pidfds is the
      equivalent of writing to a file. Thus, this is not an operation that
      operates "purely at the file descriptor level" as required by the
      open(2) manpage. See also [4].

/* References */
[1]:  https://lore.kernel.org/lkml/20181029221037.87724-1-dancol@google.com/
[2]:  https://lore.kernel.org/lkml/874lbtjvtd.fsf@oldenburg2.str.redhat.com/
[3]:  https://lore.kernel.org/lkml/20181204132604.aspfupwjgjx6fhva@brauner.io/
[4]:  https://lore.kernel.org/lkml/20181203180224.fkvw4kajtbvru2ku@brauner.io/
[5]:  https://lore.kernel.org/lkml/20181121213946.GA10795@mail.hallyn.com/
[6]:  https://lore.kernel.org/lkml/20181120103111.etlqp7zop34v6nv4@brauner.io/
[7]:  https://lore.kernel.org/lkml/36323361-90BD-41AF-AB5B-EE0D7BA02C21@amacapital.net/
[8]:  https://lore.kernel.org/lkml/87tvjxp8pc.fsf@xmission.com/
[9]:  https://asciinema.org/a/IQjuCHew6bnq1cr78yuMv16cy
[11]: https://lore.kernel.org/lkml/F53D6D38-3521-4C20-9034-5AF447DF62FF@amacapital.net/
[12]: https://lore.kernel.org/lkml/87zhtjn8ck.fsf@xmission.com/
[13]: https://lore.kernel.org/lkml/871s6u9z6u.fsf@xmission.com/
[14]: https://lore.kernel.org/lkml/20181206231742.xxi4ghn24z4h2qki@brauner.io/
[15]: https://lore.kernel.org/lkml/20181207003124.GA11160@mail.hallyn.com/
[16]: https://lore.kernel.org/lkml/20181207015423.4miorx43l3qhppfz@brauner.io/
[17]: https://lore.kernel.org/lkml/CAGXu5jL8PciZAXvOvCeCU3wKUEB_dU-O3q0tDw4uB_ojMvDEew@mail.gmail.com/
[18]: https://lore.kernel.org/lkml/20181206222746.GB9224@mail.hallyn.com/
[19]: https://lore.kernel.org/lkml/20181208054059.19813-1-christian@brauner.io/
[20]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[21]: https://lore.kernel.org/lkml/20181228152012.dbf0508c2508138efc5f2bbe@linux-foundation.org/
[22]: https://lore.kernel.org/lkml/20181228233725.722tdfgijxcssg76@brauner.io/
[23]: https://lwn.net/Articles/773459/
[24]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[25]: https://lore.kernel.org/lkml/CAK8P3a0ej9NcJM8wXNPbcGUyOUZYX+VLoDFdbenW3s3114oQZw@mail.gmail.com/

Cc: "Eric W. Biederman" <ebiederm@xmission.com>
Cc: Jann Horn <jannh@google.com>
Cc: Andy Lutomirsky <luto@kernel.org>
Cc: Andrew Morton <akpm@linux-foundation.org>
Cc: Oleg Nesterov <oleg@redhat.com>
Cc: Al Viro <viro@zeniv.linux.org.uk>
Cc: Florian Weimer <fweimer@redhat.com>
Signed-off-by: Christian Brauner <christian@brauner.io>
Reviewed-by: Tycho Andersen <tycho@tycho.ws>
Reviewed-by: Kees Cook <keescook@chromium.org>
Reviewed-by: David Howells <dhowells@redhat.com>
Acked-by: Arnd Bergmann <arnd@arndb.de>
Acked-by: Thomas Gleixner <tglx@linutronix.de>
Acked-by: Serge Hallyn <serge@hallyn.com>
Acked-by: Aleksa Sarai <cyphar@cyphar.com>

(cherry picked from commit 3eb39f47934f9d5a3027fe00d906a45fe3a15fad)

Conflicts:
        arch/x86/entry/syscalls/syscall_32.tbl - trivial manual merge
        arch/x86/entry/syscalls/syscall_64.tbl - trivial manual merge
        include/linux/proc_fs.h - trivial manual merge
        include/linux/syscalls.h - trivial manual merge
        include/uapi/asm-generic/unistd.h - trivial manual merge
        kernel/signal.c - struct kernel_siginfo does not exist in 4.14
        kernel/sys_ni.c - cond_syscall is used instead of COND_SYSCALL
        arch/x86/entry/syscalls/syscall_32.tbl
        arch/x86/entry/syscalls/syscall_64.tbl

(1. manual merges because of 4.14 differences
 2. change prepare_kill_siginfo() to use struct siginfo instead of
kernel_siginfo
 3. use copy_from_user() instead of copy_siginfo_from_user() in copy_siginfo_from_user_any()
 4. replaced COND_SYSCALL with cond_syscall
 5. Removed __ia32_sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_32.tbl.
 6. Replaced __x64_sys_pidfd_send_signal with sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_64.tbl.)

Bug: 135608568
Test: test program using syscall(__NR_pidfd_send_signal,..) to send SIGKILL
Change-Id: I34da11c63ac8cafb0353d9af24c820cef519ec27
Signed-off-by: Suren Baghdasaryan <surenb@google.com>
Signed-off-by: electimon <electimon@gmail.com>
Signed-off-by: Tiktodz <ewprjkt@proton.me>
Signed-off-by: Kneba <abenkenary3@gmail.com>

---
## [openai/evals](https://github.com/openai/evals)@[34befaceb4...](https://github.com/openai/evals/commit/34befaceb43c746b68ccce7eaca3c43a15d23404)
#### Wednesday 2023-05-31 16:18:47 by Rafal Zawadzki

Add Polish lexicon eval (#794)

## Eval details 📑
### Eval name
`polish-lexicon`

### Eval description

Test the model's ability to distinguish between existing and
hallucinated Polish words.

### What makes this a useful eval?

Polish language is hard - and I have not seen good evals created for it
yet. This eval is inspired by similar ones in Belarusian, Bulgarian and
Greek. Polish has a mix of Latin and special characters and it's common
even for a native speaker to make spelling or grammatical mistakes.
The eval set is comprised of a mix of totally invented by me words as
well as words with spelling errors.
I ran it with GPT-3.5-Turbo and its accuracy was around 60%. I also did
limited testing with GPT4 and while it seems like it deals better with
spelling mistakes, it is still not that good at recognising invented
words.

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
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Polish language? Answer Y or N."},
{"role": "user", "content": "przewądnicy"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Polish language? Answer Y or N."},
{"role": "user", "content": "przewodnicy"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Polish language? Answer Y or N."},
{"role": "user", "content": "waższe"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Polish language? Answer Y or N."},
{"role": "user", "content": "wyższe"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Polish language? Answer Y or N."},
{"role": "user", "content": "handlą"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Polish language? Answer Y or N."},
{"role": "user", "content": "handlu"}], "ideal": "Y"}
  ```
</details>

---
## [openai/evals](https://github.com/openai/evals)@[4eb8180b2a...](https://github.com/openai/evals/commit/4eb8180b2a5fc26df987978e73a94e6dfdff5e96)
#### Wednesday 2023-05-31 16:19:01 by lillichoung

Shopping discount comparison eval (#779)

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
Shopping Discount Comparison

### Eval description
This evaluation tests the model's ability to compare different offers
and select the best deal based on cost.

### What makes this a useful eval?
A future application of AI will be to help people make purchases. This
task requires AI to understand common discounts and apply them to value
calculations.

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
{"input": [{"role": "system", "content": "You are a helpful AI aiding me
in getting the best price in online shopping. You will determine which
shop I should purchase from, based on lowest cost (including shipping)
alone. Assume shops all sell the same product. Respond with the shop
number ONLY with no punctuation and do not give an explanation. Example
output: Shop 1"}, {"role": "user", "content": "I want to buy 1 lb of
beans. [Shop 1: $30 | 1 lb | Free shipping on all orders of $20 or more
| Shipping $10 ] [Shop 2: $27 | 1 lb | Shipping $5 ] Answer:"}],
"ideal": "Shop 1"}
{"input": [{"role": "system", "content": "You are a helpful AI aiding me
in getting the best price in online shopping. You will determine which
shop I should purchase from, based on lowest cost (including shipping)
alone. Assume shops all sell the same product. Respond with the shop
number ONLY with no punctuation and do not give an explanation. Example
output: Shop 1"}, {"role": "user", "content": "I want to buy a tote bag.
[Shop 1: 48€ | 8€ flat fee shipping | 20% off purchases over 40€ ] [Shop
2: 42€ | 6€ shipping | 10% off purchases over 47€] Answer:"}], "ideal":
"Shop 1"}
{"input": [{"role": "system", "content": "You are a helpful AI aiding me
in getting the best price in online shopping. You will determine which
shop I should purchase from, based on lowest cost (including shipping)
alone. Assume shops all sell the same product. Respond with the shop
number ONLY with no punctuation and do not give an explanation. Example
output: Shop 1"}, {"role": "user", "content": "I want to buy 2 items.
[Shop 1: $75.00 | Buy one get one 20% off | $5 shipping ] [Shop 2:
$75.00 | Free shipping | 15% off if you buy more than one] Answer:"}],
"ideal": "Shop 2"}
  ```
</details>

---
## [hackworthltd/primer-app](https://github.com/hackworthltd/primer-app)@[3210f04f3d...](https://github.com/hackworthltd/primer-app/commit/3210f04f3d14adb3faa424dba44a82c66e502a6d)
#### Wednesday 2023-05-31 16:19:57 by George Thomas

feat: scroll to def when its name is clicked in the sidebar

This approach is a bit hacky, but we couldn't think of a better way to
do this without wrapping large chunks of `App` in a
`ReactFlowProvider`, which we weren't crazy about. (However, that
approach may become less objectionable/problematic once we've broken
the live eval and definition list out of the sidebar.)

We'd prefer to pass the def's `GlobalName` to the `TreeReactFlow`
callback, but this would require quite a bit of reworking of the
sidebar's definition list. As that component is probably not long for
this world, we'll defer this work until later when we figure out
exactly where the definition list will go.

Limitations of this current implementation:

* It doesn't change the zoom level and technically only focuses on the
definition's root node, without trying to fit its entire tree on the
screen. We should probably support this, perhaps through some sort of
double-click/double-touch mechanism.

* It only works for definitions the student has defined in the current
module. It doesn't work for imported definitions, and it doesn't work
for typedefs, as those aren't yet rendered on the canvas. However,
this feature should be relatively easy to adapt to student-defined
typedefs once they're represented as trees on the canvas.

* It's not yet implemented in the live eval view. It may be useful for
fitting the tree on the screen when we switch which definition is
being evaluated, but there may be easier/better ways to do this that
don't involve the convoluted callback mechanism we've had to implement
here, because all of the controls we need are in a monolithic
component. We'll explore this in subsequent work, in any case.

Signed-off-by: Drew Hess <src@drewhess.com>

---
## [Kneba/platform_kernel_asus_sdm660](https://github.com/Kneba/platform_kernel_asus_sdm660)@[ef4f1870bf...](https://github.com/Kneba/platform_kernel_asus_sdm660/commit/ef4f1870bfdd502de6a699f44c4d368c9f035ce9)
#### Wednesday 2023-05-31 16:44:01 by Dave Chiluk

sched/fair: Fix low cpu usage with high throttling by removing expiration of cpu-local slices

commit de53fd7aedb100f03e5d2231cfce0e4993282425 upstream.

It has been observed, that highly-threaded, non-cpu-bound applications
running under cpu.cfs_quota_us constraints can hit a high percentage of
periods throttled while simultaneously not consuming the allocated
amount of quota. This use case is typical of user-interactive non-cpu
bound applications, such as those running in kubernetes or mesos when
run on multiple cpu cores.

This has been root caused to cpu-local run queue being allocated per cpu
bandwidth slices, and then not fully using that slice within the period.
At which point the slice and quota expires. This expiration of unused
slice results in applications not being able to utilize the quota for
which they are allocated.

The non-expiration of per-cpu slices was recently fixed by
'commit 512ac999d275 ("sched/fair: Fix bandwidth timer clock drift
condition")'. Prior to that it appears that this had been broken since
at least 'commit 51f2176d74ac ("sched/fair: Fix unlocked reads of some
cfs_b->quota/period")' which was introduced in v3.16-rc1 in 2014. That
added the following conditional which resulted in slices never being
expired.

if (cfs_rq->runtime_expires != cfs_b->runtime_expires) {
	/* extend local deadline, drift is bounded above by 2 ticks */
	cfs_rq->runtime_expires += TICK_NSEC;

Because this was broken for nearly 5 years, and has recently been fixed
and is now being noticed by many users running kubernetes
(https://github.com/kubernetes/kubernetes/issues/67577) it is my opinion
that the mechanisms around expiring runtime should be removed
altogether.

This allows quota already allocated to per-cpu run-queues to live longer
than the period boundary. This allows threads on runqueues that do not
use much CPU to continue to use their remaining slice over a longer
period of time than cpu.cfs_period_us. However, this helps prevent the
above condition of hitting throttling while also not fully utilizing
your cpu quota.

This theoretically allows a machine to use slightly more than its
allotted quota in some periods. This overflow would be bounded by the
remaining quota left on each per-cpu runqueueu. This is typically no
more than min_cfs_rq_runtime=1ms per cpu. For CPU bound tasks this will
change nothing, as they should theoretically fully utilize all of their
quota in each period. For user-interactive tasks as described above this
provides a much better user/application experience as their cpu
utilization will more closely match the amount they requested when they
hit throttling. This means that cpu limits no longer strictly apply per
period for non-cpu bound applications, but that they are still accurate
over longer timeframes.

This greatly improves performance of high-thread-count, non-cpu bound
applications with low cfs_quota_us allocation on high-core-count
machines. In the case of an artificial testcase (10ms/100ms of quota on
80 CPU machine), this commit resulted in almost 30x performance
improvement, while still maintaining correct cpu quota restrictions.
That testcase is available at https://github.com/indeedeng/fibtest.

Fixes: 512ac999d275 ("sched/fair: Fix bandwidth timer clock drift condition")
Signed-off-by: Dave Chiluk <chiluk+linux@indeed.com>
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Reviewed-by: Phil Auld <pauld@redhat.com>
Reviewed-by: Ben Segall <bsegall@google.com>
Cc: Ingo Molnar <mingo@redhat.com>
Cc: John Hammond <jhammond@indeed.com>
Cc: Jonathan Corbet <corbet@lwn.net>
Cc: Kyle Anderson <kwa@yelp.com>
Cc: Gabriel Munos <gmunoz@netflix.com>
Cc: Peter Oskolkov <posk@posk.io>
Cc: Cong Wang <xiyou.wangcong@gmail.com>
Cc: Brendan Gregg <bgregg@netflix.com>
Link: https://lkml.kernel.org/r/1563900266-19734-2-git-send-email-chiluk+linux@indeed.com
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Signed-off-by: Ratoriku <a1063021545@gmail.com>
Signed-off-by: Peppe289 <gsperanza204@gmail.com>
Signed-off-by: RyuujiX <saputradenny712@gmail.com>
Signed-off-by: Kneba <abenkenary3@gmail.com>

---
## [LadyK-21/git](https://github.com/LadyK-21/git)@[7891e46585...](https://github.com/LadyK-21/git/commit/7891e465856e539c4a102dadec6dca9ac51c38df)
#### Wednesday 2023-05-31 17:12:26 by Jeff King

gpg-interface: set trust level of missing key to "undefined"

In check_signature(), we initialize the trust_level field to "-1", with
the idea that if gpg does not return a trust level at all (if there is
no signature, or if the signature is made by an unknown key), we'll
use that value. But this has two problems:

  1. Since the field is an enum, it's up to the compiler to decide what
     underlying storage to use, and it only has to fit the values we've
     declared. So we may not be able to store "-1" at all. And indeed,
     on my system (linux with gcc), the resulting enum is an unsigned
     32-bit value, and -1 becomes 4294967295.

     The difference may seem academic (and you even get "-1" if you pass
     it to printf("%d")), but it means that code like this:

       status |= sigc->trust_level < configured_min_trust_level;

     does not necessarily behave as expected. This turns out not to be a
     bug in practice, though, because we keep the "-1" only when gpg did
     not report a signature from a known key, in which case the line
     above:

       status |= sigc->result != 'G';

     would always set status to non-zero anyway. So only a 'G' signature
     with no parsed trust level would cause a problem, which doesn't
     seem likely to trigger (outside of unexpected gpg behavior).

  2. When using the "%GT" format placeholder, we pass the value to
     gpg_trust_level_to_str(), which complains that the value is out of
     range with a BUG(). This behavior was introduced by 803978da49
     (gpg-interface: add function for converting trust level to string,
     2022-07-11). Before that, we just did a switch() on the enum, and
     anything that wasn't matched would end up as the empty string.

     Curiously, solving this by naively doing:

       if (level < 0)
               return "";

     in that function isn't sufficient. Because of (1) above, the
     compiler can (and does in my case) actually remove that conditional
     as dead code!

We can solve both by representing this state as an enum value. We could
do this by adding a new "unknown" value. But this really seems to match
the existing "undefined" level well. GPG describes this as "Not enough
information for calculation".

We have tests in t7510 that trigger this case (verifying a signature
from a key that we don't have, and then checking various %G
placeholders), but they didn't notice the BUG() because we didn't look
at %GT for that case! Let's make sure we check all %G placeholders for
each case in the formatting tests.

The interesting ones here are "show unknown signature with custom
format" and "show lack of signature with custom format", both of which
would BUG() before, and now turn %GT into "undefined". Prior to
803978da49 they would have turned it into the empty string, but I think
saying "undefined" consistently is a reasonable outcome, and probably
makes life easier for anyone parsing the output (and any such parser had
to be ready to see "undefined" already).

The other modified tests produce the same output before and after this
patch, but now we're consistently checking both %G? and %GT in all of
them.

Signed-off-by: Jeff King <peff@peff.net>
Reported-by: Rolf Eike Beer <eb@emlix.com>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [clayne/semgrep](https://github.com/clayne/semgrep)@[b0e10c5d78...](https://github.com/clayne/semgrep/commit/b0e10c5d783ed1063a9aef3f0b430a8a302404df)
#### Wednesday 2023-05-31 17:38:26 by Martin Jambon

Aliengrep integration + rule ID type + 'languages' type (#7885)

I should have done these other things in different PRs but it was too
late by the time I realized how big those changes were. So, here we go.
The main changes brought by this branch are:

* `options.generic_engine: aliengrep` in rules allows semgrep to use
aliengrep when `generic` is specified in the `languages` list.
* I added some end-to-end tests for aliengrep. I created two issues for
a [matching bug](https://github.com/returntocorp/semgrep/issues/7881)
and a [missing
feature](https://github.com/returntocorp/semgrep/issues/7883) but it's
nothing big. Overall, it works.
* The `languages` field is now translated (in OCaml only, not Python)
into a `languages` type that distinguishes target selector (langs) from
target analyzer (xlang). "generic" now means "generic target selection"
and the parsing/matching engine is specified separately. This was done
to avoid making things weird for the user but we still have to support
"regex" and "none" which both mean "generic target selection" + "regex
engine".
* Along the way, I got annoyed that rule IDs were reported as
`Common.filename` (= `string`) so I created a type for them.
* I modified `Input_to_core.atd` so that it uses the `Xlang.t` type
directly rather than a string that needs to be converted later. This is
an example to show that we could use the same mechanism for other types
(generally strings or ints that serve as some kind of ID with its own
type).

I left comments to explain those things. The Python side gave me a bit
of a headache. I tried various things that I reverted, concluding that
the least we touch, the better.

I will have to document the features of aliengrep. It shouldn't be too
hard because it has a lot in common with spacegrep. For now, there's a
readme in `libs/aliengrep`.

test plan: `make test` should work

Uses: https://github.com/returntocorp/semgrep-langs/pull/36

PR checklist:

- [x] Purpose of the code is [evident to future
readers](https://semgrep.dev/docs/contributing/contributing-code/#explaining-code)
- [x] Tests included or PR comment includes a reproducible test plan
- [x] Documentation is up-to-date
- [x] A changelog entry was [added to
changelog.d](https://semgrep.dev/docs/contributing/contributing-code/#adding-a-changelog-entry)
for any user-facing change
- [x] Change has no security implications (otherwise, ping security
team)

If you're unsure about any of this, please see:

- [Contribution
guidelines](https://semgrep.dev/docs/contributing/contributing-code)!
- [One of the more specific guides located
here](https://semgrep.dev/docs/contributing/contributing/)

---------

Co-authored-by: Martin Jambon <martin@semgrep.com>

---
## [Bokkiewokkie/Shiptest](https://github.com/Bokkiewokkie/Shiptest)@[0cff53fc09...](https://github.com/Bokkiewokkie/Shiptest/commit/0cff53fc09c34d989d2bc34b1699bd856af2cb92)
#### Wednesday 2023-05-31 18:19:49 by meemofcourse

Reworks the Twinkleshine-Class (#1825)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request


![2023 05 13-23 20
45](https://github.com/shiptest-ss13/Shiptest/assets/75212565/de6f3a47-7be8-4800-ae73-9fc386e4bf01)

![twinklerework5](https://github.com/shiptest-ss13/Shiptest/assets/75212565/f1808576-70e3-4b56-b977-5b5e7d665fdd)





The Twinkleshine is a CyberSun-made Syndicate display of force, staffed
by every branch of the Syndicate. Despite the silly name, the presence
of one in a sector implies it to be of importance to the Syndicate, and
enemies within sight can only pray that the Twinkleshine crew are
incompetent enough to shoot themselves with their own weaponry (or blow
themselves up with the supermatter on-board).

It is staffed by:

- 1 Captain
- 1 Lieutenant (previously the Operative - serves as a warden/hos)
- 2 Medics
- 2 Engineers (previously the Mechanics)
- 5 Operatives (previously the Troopers)
- 1 Bartender
- 1 Miner
- 2 Deck Assistants

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Few days ago, an admin spawned a Twinkleshine, and I got to captain it.
The Twinkleshine is old. It sucks. This, hopefully, fixes that.

Originally, this was going to be minor fixes, but ended up becoming an
attempt at reworking the ship to a more modern state - the hull has been
redone and is mostly symmetrical, the old spacepod was replaced with a
Dark Gygax, the supermatter shouldn't be activated upon spawning the
ship, there's more turf decals and a bigger lot-of-things, added a
bartender and a miner, people can actually tell who they are and what
they do, and there is now a box moth. Rejoice.

Also, this is the first time I've ever mapped a ship. What better way to
begin with a giant battleship?

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
tweak: Reworks the Twinkleshine
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: meemofcourse <75212565+meemofcourse@users.noreply.github.com>

---
## [Bokkiewokkie/Shiptest](https://github.com/Bokkiewokkie/Shiptest)@[d4b5a598e2...](https://github.com/Bokkiewokkie/Shiptest/commit/d4b5a598e2346bb3f69d533ed05a94d539e8b830)
#### Wednesday 2023-05-31 18:19:49 by Bjarl

Sand Survivor Rework (#1940)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Reworks how Sand Survivors spawn their loot. Instead of an outfit datum,
they now create a corpse similiarly to how legions do it, this allows
their contents to have some variety, more ease of expansion, and
generally Improves the file.

How I could write better code in a day than White Sands functioned with
for iunno how long is byond me


https://user-images.githubusercontent.com/94164348/236322169-c303f934-634f-447d-950f-78a55346d152.mp4

![image](https://user-images.githubusercontent.com/94164348/236376947-6e484ed0-f136-4787-9e74-fad0f5c21d11.png)

![image](https://user-images.githubusercontent.com/94164348/236377018-e2dc1661-fe78-4c6a-8be2-8bf24e5d00b2.png)


<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Consistency + Just kinda cool
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Sand Planet hermits now have randomized inventories. And Hair.
Sometimes.
add: Sand Planet hermits can now drop different races
add: legions will now drop a variety of species
balance: drop rates for legions have been changed in a few spots.
fix: hivelord.dm no longer sears my eyes out.
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
Co-authored-by: Mark Suckerberg <mark@suckerberg.gay>

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[21464fe41c...](https://github.com/microsoft/terminal/commit/21464fe41c9c09eac4b9e2d85225f18f1f3c2c7b)
#### Wednesday 2023-05-31 18:54:35 by Mike Griese

Manually hide our DesktopWindowXamlSource (#15165)

As discussed in #6507

Newer builds of Windows do this automatically. However, this was spotted
in the wild on 1.18. It's possible the threading changes created a
situation where the OS-side fix no longer applied to us. So let's just
do it manually. It doesn't have any side effects.

I saw this once on Win11, but couldn't repro it this morning when I
tried to add this fix. I'm just gonna assume this worked, despite the
fact that I can't repro it on win11 anymore.

closes #6507

See also #14957

## detailed description

> `WindowsXamlManager::XamlCore::Initialize` calls
`ConfigureCoreWindow`, which creates a `CoreWindow` on the thread

> Problem is, we're calling that on the main thread (which doesn't have
_any_ windows), and then eventually creating a `DesktopWindowXamlSource`
on a second thread for the actual window

> It's not that it "manages a window", it's that it "manages xaml on
Windows OS". just use ICoreWindowInterop -- QI for ICoreWindowInterop
and call get_WindowHandle.

Also see:
*
[ICoreWindowInterop](https://learn.microsoft.com/en-us/windows/win32/api/corewindow/nn-corewindow-icorewindowinterop)
*
[WindowsXamlManager.InitializeForCurrentThread](https://learn.microsoft.com/en-us/uwp/api/windows.ui.xaml.hosting.windowsxamlmanager.initializeforcurrentthread?view=winrt-22621#windows-ui-xaml-hosting-windowsxamlmanager-initializeforcurrentthread)
* The source code in
`onecoreuap\windows\dxaml\xcp\dxaml\lib\WindowsXamlManager_Partial.*`
* os.2020!6102020 which fixed MSFT:33498969, MSFT:27807465,
MSFT:21854264

---
## [kaiserbyte/Crouch-Jump](https://github.com/kaiserbyte/Crouch-Jump)@[8c274b6e74...](https://github.com/kaiserbyte/Crouch-Jump/commit/8c274b6e74c4e4b4c4a461309f82e531e85e5cc3)
#### Wednesday 2023-05-31 19:16:45 by Joshua W. Kyler

i forgot to edit this HELP

someone pointed out that i actually needed to edit this so i did. im not putting my legal name on this fuck you

---
## [sourcegraph/sourcegraph](https://github.com/sourcegraph/sourcegraph)@[a5060359bb...](https://github.com/sourcegraph/sourcegraph/commit/a5060359bb6d9715a7d208f4624d6fea92ac3083)
#### Wednesday 2023-05-31 19:19:34 by Randell Callahan

executors: More K8s Improvements (#52653)

Some more tweaks to K8s support.

## Changes

- Fixed issue with flags not being used by `batcheshelper` when
arguments are present
    - Apparently `flags` silently die when there are arguments present
- Added observability to `KubernetesCommand` to help see some metrics
- Added some `Debug` logs for troubleshooting
- Changed the wait functionality from waiting on the K8s Job to the K8s
Pod
    - This eliminates another API call we make
    - Since we always have 1 pod for every job, this is safe
    - Simplifies the code a little (removes the ugly error check)
    - Reduces required RBAC Rules
- Updated docs to clarify that `batcheshelper` also needs to be built if
running ssbc

## Test plan

Updated and added Go tests.

---
## [Eliuscuro/Skyrat220](https://github.com/Eliuscuro/Skyrat220)@[fc1471c818...](https://github.com/Eliuscuro/Skyrat220/commit/fc1471c8187d3f2a49d75a8a5c3e1b610fec45d3)
#### Wednesday 2023-05-31 19:53:12 by SkyratBot

[MIRROR] Deadchat Announcement Variety Pack 1 [MDB IGNORE] (#20957)

* Deadchat Announcement Variety Pack 1 (#75140)

## About The Pull Request

Adds announce_to_ghosts()/notify_ghosts() calls to a bunch of different
things.

**THIS INCLUDES:**
- Powersink being activated/reaching critical (explosion) heat capacity.
- His Grace being awoken.
- Hot Potatoes being armed.
- Ascension Rituals being completed.
- Eyesnatcher victims.
- Ovens exploding as a result of the Aurora Caelus event.
- Wizard Imposter spawns.
- Rock-Paper-Scissors with death as the result of Helbital consumption.
- BSA impact sites.
- Spontaneous Appendicitis.
- The purchasing of a badass syndie balloon.
- The Supermatter beginning to delaminate.

This was everything that I could think of that would be worth announcing
to deadchat. These were all chosen with consideration to questions like
"how easy would it be to spam deadchat with this?" and "will observers
actually see the interesting thing happen, or just the aftermath?".

Not gonna lie, I've really become an observer main as of recently. Maybe
that's being reflected in my recent PRs. Who's to say? Deadchat
Announcement Variety Pack 2 will probably never come out. Sorry.
## Why It's Good For The Game

Gives deadchat a better indiciation of when/where something **REALLY
FUNNY** is about to happen. Draws attention to certain things that are
likely to gather an audience anyways, but sooner (for your viewing
pleasure). In simple terms, it helps the observers observe things
better.

Some cases, such as the aurora caelus or helbitaljanken, are occurrences
so rare that they deserve the audience.
## Changelog
:cl: Rhials
qol: Observers now recieve an alert when a powersink is activated/about
to explode.
qol: His Grace being awoken now alerts observers, to give you a
headstart on your murderbone ghost ring.
qol: Ascension Rituals being completed will also alert observers, for
basically the same reason.
qol: Arming a hot potato will now alert observers. Catch!
qol: Eyesnatcher victims will now notify observers, and invite them to
laugh at their state of misery and impotence.
qol: Observers will be notified of any acute references to The Simpsons
or other 20th Television America copyright properties.
qol: Wizard Imposter spawns alert observers, much like any other ghost
role event should.
qol: Playing Rock-Paper-Scissors with death will now alert the observers
and invite them to watch. Better not choke!
qol: Observers now get an orbit link for BSA impact sites. Why does it
keep teleporting me to the AI upload??
qol: Spontaneous Appendicitis now alerts deadchat.
qol: The purchasing of a badass syndie balloon now alerts deadchat. You
might not be any more powerful, but at least you have an audience.
qol: When beginning to delaminate, the Supermatter will alert observers
and invite them to watch the fireworks.
/:cl:

* Deadchat Announcement Variety Pack 1

---------

Co-authored-by: Rhials <Datguy33456@gmail.com>

---
## [newstools/2023-sundiata-post](https://github.com/newstools/2023-sundiata-post)@[ac8ea0ab74...](https://github.com/newstools/2023-sundiata-post/commit/ac8ea0ab74c1e98988a8d37d438cfb6b87e6800c)
#### Wednesday 2023-05-31 21:00:18 by Billy Einkamerer

Created Text For URL [sundiatapost.com/drama-ensues-after-pregnant-lady-caught-boyfriend-with-another-girl-in-his-house-video/]

---
## [davep/textual](https://github.com/davep/textual)@[c3269bb4f4...](https://github.com/davep/textual/commit/c3269bb4f493efdcb83ea84494e7c22a3fed04e4)
#### Wednesday 2023-05-31 21:02:24 by Dave Pearson

Rework handler processing again to deal with selector fun

I'm like 90% sure about this. This was a "dump it all and work from scratch"
evening experiment, and I think it does what's needed, but I want to read it
back over again in the morning with a post-coffee brain.

Pushing to the repo so I can review then.

Also added lotsa comments so tomorrow me will know what this evening me was
thinking.

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[120041c693...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/120041c69313f5420509b293028a55789ce62576)
#### Wednesday 2023-05-31 21:05:25 by SkyratBot

[MIRROR] Converts del logging to proper json, using json objects instead of building a text file [MDB IGNORE] (#21448)

* Reverts qdel logging to a raw text file (#75632)

## About The Pull Request

We log this information once, on SSgarbage shutdown. Putting it in a
json is kinda pointless, it exists to be read when we see massive
overtime from ssgarbage, that's all.

Something something reee my workflow.

## Changelog
:cl:
server: qdel statistics are once again logged in qdel.log, instead of
the otherwise typical json logging system
/:cl:

* Converts del logging to proper json, using json objects instead of building a text file (#75636)

## About The Pull Request

It's easier to parse, and makes more sense when you read it. This way
I'll never have to add yet another case to my parser for someone
changing where a space goes or something.

Moves qdel into its own category cause the old name looked ugly (yell if
this is dumb)
Added a bitfield to entries pulled from categories, adds a new flag that
enables pretty printing json lists.


## Why It's Good For The Game

IMPROVES my workflow

## Changelog
:cl:
server: del logging is now done by outputting to a json file again, but
this time we're using ACTUAL json and not just a big text string with
newlines and shit
/:cl:

---------

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

---
## [SileNce5k/discord_bot](https://github.com/SileNce5k/discord_bot)@[abfb659a42...](https://github.com/SileNce5k/discord_bot/commit/abfb659a4249c864efd5f80cd9520392ae80d973)
#### Wednesday 2023-05-31 21:47:38 by SileNce5k

Add sum awaits in this bitch to see if it fixes these issues fuck my
life AAAAAAAAAAAAAAAAAAAAAAAAAA

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[57ef596898...](https://github.com/tgstation/tgstation/commit/57ef596898a5a3932db33389baa9fab3164d430a)
#### Wednesday 2023-05-31 22:45:34 by LemonInTheDark

Admin Library Moderation (in-game edition) (#75645)

For the longest time, the only way admins could moderate the library was
by using statbus's external tool.
But a few months back statbus went down, and ever since then they've
been sitting lost. Shit sucks.

The whole external thing has been bugging me for a while, so let's fix
all that yeah?

This pr adds a new verb to the admin tab that allows admins to
ban/restore books from the library.
It includes expanded (ckey) search, faster response times, in tool book
viewing with and without markdown rendering, and viewing of deleted
books.

This is accomplished with a special subtype of library consoles, stored
on the admin datum.
It shouldn't let you do anything without +BAN, rip my live debugging or
whatever.

I've also hooked into (and fixed) Ned's existing library actions log,
and added viewing support to the ban/restore pages.
This logs banning admin, ban time, ban reason, etc.

As a part of this, I've fixed/expanded on the existing UIs.
I've added ID search to all existing consoles, and fixed an existing bug
with the visitor console not supporting category search (shows how many
people actually use the thing)

Changes to the library_action table were pretty minor. The ckey column
was too small, so longer keys just caused it to fail on ban. Bad.
That and the ip address column was signed, which wasted space and was
non standard with other tables.

---
## [rd-stuffs/android_kernel_xiaomi_surya](https://github.com/rd-stuffs/android_kernel_xiaomi_surya)@[0d11be924d...](https://github.com/rd-stuffs/android_kernel_xiaomi_surya/commit/0d11be924d1c5aa1708d67546cf0d269cbefe4c7)
#### Wednesday 2023-05-31 22:52:06 by Wang Han

power: Introduce OnePlus 3 fingerprintd thaw hack

Taken from Oneplus 3, this hack will make fingerprintd recover from suspend quickly.

Small fixes for newer kernels since we're coming from 3.10.108..

Change-Id: I0166e82d51a07439d15b41dbc03d7e751bfa783b
Co-authored-by: Cyber Knight <cyberknight755@gmail.com>
[cyberknight777: forwardport and adapt to 4.14]
Signed-off-by: Shreyansh Lodha <slodha96@gmail.com>
Signed-off-by: Pierre2324 <pdbbasketball@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>
Signed-off-by: Dhruv <dhruvgera61@gmail.com>
Signed-off-by: Cyber Knight <cyberknight755@gmail.com>
Signed-off-by: Richard Raya <rdxzv.dev@gmail.com>

---
## [Nerev4r/Skyrat-tg](https://github.com/Nerev4r/Skyrat-tg)@[bfb3967c90...](https://github.com/Nerev4r/Skyrat-tg/commit/bfb3967c908682e21202312d8b30ec17ad65e549)
#### Wednesday 2023-05-31 22:52:18 by SkyratBot

[MIRROR] Adds proper armor for security plasmamen. [MDB IGNORE] (#21268)

* Adds proper armor for security plasmamen. (#75156)

## About The Pull Request
It's kinda strange that security plasmamen has no proper armor and you
can just bully them with bottlesmashes. Literally.
Also suits had no wound armor for some reason, which considering that
mold dies without hand kinda silly too.
And helmets just had no armor besides 1 melee armor.
## Why It's Good For The Game
Plasmamen security won't die that easilly. I mean, still easy to kill
them, but not that much.
## Changelog
:cl:
balance: Security Plasmamen now have Security armor. No bullying them
with bottlesmashes anymore.
/:cl:

* Adds proper armor for security plasmamen.

---------

Co-authored-by: Helg2 <93882977+Helg2@users.noreply.github.com>
Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>

---
## [barrettj12/juju](https://github.com/barrettj12/juju)@[19b18fec85...](https://github.com/barrettj12/juju/commit/19b18fec85754efe2d8cae9e452ae3de831ff154)
#### Wednesday 2023-05-31 23:35:26 by Juju bot

Merge pull request #14511 from benhoyt/openstack-auth-error

https://github.com/juju/juju/pull/14511

This slightly improves the error message during OpenStack authentication when the code is trying to authenticate against a v3 server but the credentials look like v2 credentials. Previously the code would fall back to using a v2 client and the next call would give a 404 error, now it doesn't fall back when it knows the server is v3 ("v3" in the URL) so we get a 401 authentication error immediately.

## Checklist

- [x] Code style: imports ordered, good names, simple structure, etc
- [x] Comments saying why design decisions were made
- [x] Go unit tests, with comments saying what you're testing
- [ ] ~[Integration tests](https://github.com/juju/juju/tree/develop/tests), with comments saying what you're testing~
- [x] [doc.go](https://discourse.charmhub.io/t/readme-in-packages/451) added or updated in changed packages

## QA steps

* Set up an OpenStack cluster for testing (I used the single VM [devstack](https://docs.openstack.org/devstack/yoga/guides/single-vm.html) system using Multipass). This took at least 45 minutes to initialize the VM, set up all the packages, etc.
* Set up a Juju cloud using `juju add-cloud` with the novarc file method described [here](https://juju.is/docs/olm/openstack). The novarc file can be downloaded from the cluster's Dashboard, using the "Download OpenStack RC file" button under API Access.
* Add a credential, but make the password incorrect so auth is going to fail (I changed "password" to "passwordx").
* Try to `juju bootstrap openstack`.

However, here's where I started to run into trouble. First I got this error:

```
$ juju bootstrap openstack
ERROR cannot create a client: version part of identity url http://10.244.209.44/identity not valid
```

Fix is to update Juju's `clouds.yaml` regions endpoint from "endpoint: http://10.244.209.44/identity" to "endpoint: http://10.244.209.44/identity/v3". Not sure why this isn't included in the novarc correctly, as it's definitely a v3 endpoint.

The next error I got was

```
ERROR auth options fetching failed
caused by: request available auth options: request (http://10.244.209.44/) returned unexpected status: 200; error info: 

... lots of HTML output ...
```

This is because goose's client.baseURL is not set (""). It doesn't look like it can be set via config due to the use of NewClient, which is what's being used here. So you have to hack-fix goose [here](https://github.com/go-goose/goose/blob/e7e49e456da1f62c629a2fc6944fe96b2af94368/client/client.go#L701) (and use replace for goose in `go.mod`):

```diff
$ git diff
diff --git a/client/client.go b/client/client.go
index 2b10185..e812d3e 100644
--- a/client/client.go
+++ b/client/client.go
@@ -698,7 +698,7 @@ func (c *authenticatingClient) IdentityAuthOptions() (identity.AuthOptions, erro
 return identity.AuthOptions{}, gooseerrors.Newf(err, "trying to determine auth information url")
 }
 // this cannot fail.
- authInfoPath, _ := url.Parse("/")
+ authInfoPath, _ := url.Parse("/identity") // TODO
 baseURL = parsedURL.ResolveReference(authInfoPath).String()
 }
 authOptions, err := identity.FetchAuthOptions(baseURL, c.httpClient, c.logger)
```

I don't understand how this ever worked. I'm guessing that most OpenStack installs have a root of "/" (with the domain being `identity.foo.bar` or whatever), whereas with devstack you're using an IP address with a base URL of "/identity". I think Goose needs fixing here, but I've spent enough time on this now and don't really know what the correct fix is anyway.

With those two fixes in place, now when you `juju bootstrap openstack` you'll actually see the issue at hand.

```
# BEFORE fix
$ juju bootstrap openstack
ERROR authentication failed.: authentication failed
caused by: requesting token failed
caused by: Resource at http://10.244.209.44/identity/v3/tokens not found
caused by: request (http://10.244.209.44/identity/v3/tokens) returned unexpected status: 404; error info: <!doctype html>
<html lang=en>
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>

# AFTER fix
$ juju bootstrap openstack
ERROR authentication failed
caused by: requesting token: Unauthorised URL http://10.244.209.44/identity/v3/auth/tokens
caused by: request (http://10.244.209.44/identity/v3/auth/tokens) returned unexpected status: 401; error info: Failed: 401 error: The request you have made requires authentication.
```

## Bug reference

https://bugs.launchpad.net/juju/+bug/1980474

---
## [cozy/cozy-drive](https://github.com/cozy/cozy-drive)@[399a96980e...](https://github.com/cozy/cozy-drive/commit/399a96980e464cf6d6f9e60cbbe0a756f6b0cd45)
#### Wednesday 2023-05-31 23:51:10 by Crash--

fix: Scroll to top

 Since we are not able to restore the scroll correctly,
 and force the scroll to top every time we change the
 current folder. This is to avoid this kind of weird
 behavior:
 - If I go to a sub-folder, if this subfolder has a lot
 of data and I scrolled down until the bottom. If I go
 back, then my folder will also be scrolled down.

 This is an ugly hack, yeah.

---

