## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-05-29](docs/good-messages/2023/2023-05-29.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,067,603 were push events containing 3,211,295 commit messages that amount to 212,049,246 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 81 messages:


## [h13e/evals](https://github.com/h13e/evals)@[f89925829b...](https://github.com/h13e/evals/commit/f89925829b2fdd8e24acfdb518064189a5751178)
#### Monday 2023-05-29 00:15:00 by Vasco Lange

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
## [ritorizo/Shiptest](https://github.com/ritorizo/Shiptest)@[00b8761853...](https://github.com/ritorizo/Shiptest/commit/00b8761853eabc6d73073cce4708dc71d402539c)
#### Monday 2023-05-29 00:27:06 by Apogee-dev

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
## [nikothedude/Skyrat-tg](https://github.com/nikothedude/Skyrat-tg)@[3ecc9f859d...](https://github.com/nikothedude/Skyrat-tg/commit/3ecc9f859dfc0f870500d717e382d52662667996)
#### Monday 2023-05-29 00:27:37 by SkyratBot

[MIRROR] Allows Export of your Preferences JSON File [MDB IGNORE] (#20894)

* Allows Export of your Preferences JSON File (#75014)

## About The Pull Request

Hey there,

This was spoken about in #70492 (specifically
https://github.com/tgstation/tgstation/pull/70492#issuecomment-1278069607),
and I have been waiting for this to be implemented for some time. It
never got implemented, so I decided to code it myself.

Basically, **if the server host doesn't disable it**, you are free to
export your JSONs as a player, right from the stat-panel. It's a pretty
JSON on 515 versions, too!

It's right here:

![image](https://user-images.githubusercontent.com/34697715/235251447-1c977718-51fd-4025-8d89-c60bffc379ec.png)

Here's what the prettified JSON looks like on 515.

![image](https://user-images.githubusercontent.com/34697715/235321061-4a217e26-c082-4bba-b54a-2c780defda0a.png)

There's a cooldown (default to 10 seconds) between exporting your
preferences.

#### Why is this config?

It's because in the past, a server host could always just file-share the
.sav or .json or whatever to the player, but they would have to do the
explicit option of actually bothering to make the files accessible to
the player. In that same line of logic, the server operator will have to
explicitly make the files accessible. This is mostly because I'm not
sure how good `ftp()` is at being a player function and wanted to have
some sort of cap/control somehow in case an exploit vector is detected
or it's just plain spammed by bots, so we'll just leave it up to the
direct providers of this data to elect if they wish to provide the data
or not.
## Why It's Good For The Game

Players don't have to log into Server A to remember what hairstyle they
loved using when they want to swap to Server B! That's amazing actually.
I always forget what ponytail my character has, and it'll be nice to
have the hairstyle in a readily accessible place (after I prettify the
JSON for myself).

It's also more convenient for server hosts to make player data like this
accessible if they really want to, too.

If we ever add an _import_ feature in the future (which would have to be
done with a LOT of care), this will also be useful. I wouldn't advise it
though having taken a precursory look at how much goes into it while
trying to ascertain the scope of this PR.
## Changelog
:cl:
qol: The game now supports export of your preferences into a JSON file!
The verb (export-preferences) should now be available in the OOC tab of
your stat-panel if enabled by server operators.
server: Exporting player preferences is controlled by a configuration
option, 'FORBID_PREFERENCES_EXPORT'. If you do not wish to let clients
access the ftp() function to their own preferences file (probably for
bandwidth reasons?) you should uncomment this or add it to your config
somehow.
config: Server operators are also able to set the cooldown between
requests to download the JSON Preferences file via the
'SECONDS_COOLDOWN_FOR_PREFERENCES_EXPORT' config option.
/:cl:

* Allows Export of your Preferences JSON File

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [lmorv/proto-glod](https://github.com/lmorv/proto-glod)@[84e756fd8b...](https://github.com/lmorv/proto-glod/commit/84e756fd8b95573a9565d72a80a183b4d5da40c2)
#### Monday 2023-05-29 01:05:20 by lmorv

Character Design, Narrative Design: A wave of character sketches & dialogue stream edits

 - Did a whole bunch of sketches of obsidian, some I had in the back of my pocket (of my back pocket) from a couple weeks ago, made a couple others more presentable, and I tried to develop the idea of having a mask on them. Only one of the attempts at a masked obsidian was truly successful I think. But I'm still adding them cause it's all part of the process.

 - This idea came from me trying thinking about the rigging workflow of the 3D model, and about how I dont want to rig the face. My fear is that they will look dead and really creepy without even a blinking animation, so I decided to cover the face or at least just the eyes with a cool mask. I think it it would be pretty cool and unique and a chance to get more mesoamerican aesthetics into the visual mix.

 - I've also been shamelessly gravitating towards a design that looks kindda like me (or an idealized kid version of me). I also really like the sketches where they look more female, people often thought I was a girl when I was a kid and had long hair, and I thought that was cool for multiple reasons. I would reaaally love to make obsidian completely customizable haha! sliders for proportions, hair styles, options of clothing, different masks and all that jazz. But for now, realistically speaking I would be happy with an obsidian of ambiguous gender, and no face animation, with a cool mask, or sun glasses. Or a simple solution to blinking (now that I think about it that doesnt seem so hard to achieve with vertex blend shapes and no rigging).

 - On the narrative-fabulation front; I did a 'refine' pass on the script I wrote for the beginning of the game. I didn't find the concise narrative arc that I was looking for, maybe I will later. But I think that ending on a cliffhanger could also work for a 'demo' type experience, and allow me to endlessly write the story in the ever-escalating event progression format that it seems to be headed. I sort of set myself up for that kind of story and now I dont know how to get out of it. I don't know if I really want to.

 - I also made this itch.io page for a speculative 2D gameboy version of the game called 'proto-glod: darklit (lite)': https://lm-vega.itch.io/proto-glod-darklit-lite . I'll talk about that on a journal entry or a why reflection.

---
## [TheRealScarHomie/mojave-sun-13](https://github.com/TheRealScarHomie/mojave-sun-13)@[b2f0f35f3a...](https://github.com/TheRealScarHomie/mojave-sun-13/commit/b2f0f35f3afe1905cfefcf9e682de51cff2d4499)
#### Monday 2023-05-29 01:18:09 by EdwardNashton

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
## [fesh0r/mame-full](https://github.com/fesh0r/mame-full)@[2222a0f098...](https://github.com/fesh0r/mame-full/commit/2222a0f098c2f32ec6090627598a90e596006596)
#### Monday 2023-05-29 01:19:01 by David 'Foxhack' Silva

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
## [ca2/operating_system-macos](https://github.com/ca2/operating_system-macos)@[01cb8a030e...](https://github.com/ca2/operating_system-macos/commit/01cb8a030e7c7e9af12295c662e5aaf155130c29)
#### Monday 2023-05-29 01:34:35 by Camilo Sasuke Thomas Borregaard Sørensen

<3ThomasBS_ILoveYOU!! [ macOS Monterey : day 26 ] ca2 Stabilization and continuous integration and deployment implementation
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
## [46620/Scripts](https://github.com/46620/Scripts)@[b41d7773e8...](https://github.com/46620/Scripts/commit/b41d7773e814eb811da3116ac775e78a6d79fe3b)
#### Monday 2023-05-29 01:35:20 by 46620

I fucking love functions
I fucking hate gitea so fucking much fuck gite fuck it's stupid fucking API bullshit making JQ not work that was fucking dumb to fix I fucking hate it so god damn much fuck Nintendo for nuking Lockpick_RCM making me do this FUCKING GROSS SHIT ON LINE 47 IT'S FUCKING TERRIBLE!

---
## [GODdudesoyeah/cmss13](https://github.com/GODdudesoyeah/cmss13)@[fc1e2e5e26...](https://github.com/GODdudesoyeah/cmss13/commit/fc1e2e5e26259773038df05c5405cb80441b8cc2)
#### Monday 2023-05-29 02:42:19 by riot

L42A replacement with M4RA, less balance edition (#2674)

<!-- Write BELOW The Headers and ABOVE The comments else it may not be
viewable. -->

# IMPORTANT NOTES PLEASE READ
THIS DOES NOT CONTAIN THE NEW AMMO AND REBALANCED L42/M4RA THAT #1485
HAD
THIS DOES CONTAIN SOME BALANCE THINGS, BUT IT IS NOT ANYWHERE CLOSE TO
THE ABOVE

Also lore team wanted this, plz no gbp close maintainers 🙏 🙏 🧎‍♂️ 🕋 

# About the pull request

Replaces L42A in all marine available sources with the M4RA, the
canonical DMR of the USCM, you may notice this is currently the scout
rifle, well the scout rifle is now the M4RA Custom, a version that can
chamber the HV rounds that are spec ammo, but it can also chamber
standard m4ra rounds, albeit doing less damage with them than a normal
M4RA.

M4RA has current L42A stats fully, with the three exceptions being
having no stock to attach or remove(stock was not integrated it sucked),
being able to fit a/vgrip like scout m4RA, which may seem like a huge
thing but L42 stats were already insane, so it doesn't effect much.

M4RA Custom(scout gun), gets L42 stats as well, with the exception of
having less of a damage mult, meaning when not using the spec ammo, it
is out-preformed by the standard m4RA.

Adds new M4RA sprites, both standard and custom, by triiodine 

Adds sprites for all M4RA mag variants, by myself.

This was requested by lore team, previous PR of this with way more
balance stuff was #1485
Ok thats about all 🙂 

# Explain why it's good for the game

Lore accuracy is good, and this mostly doesn't effect the actual game
outside of the scout rifle changes.
Also scout rifle underpreformed if you weren't omega hell sliming with
inc-impact stunlocking while on fire, still will be omega hell slime
central but that isn't the thing being solved in this pr , it'll do fine
when NOT sliming at least now.


# Testing Photographs and Procedure
It works.


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
add: Adds the M4RA as the standard marine DMR, identical stats to L42
with the exception of fitting a v or agrip and no removable stock, stats
still the same as l42 without stock.
del: L42 from all marine accessible sources with the exception of black
market
balance: Scout M4RA is now the M4RA Custom, it can use standard M4RA
magazines but standard M4RA cannot use custom magazines.
balance: Scout M4RA now has L42/M4RA standard stats with the exception
of lower damage.
balance: Scout M4RA now can fit magnetic harness, laser sight, however
it can no longer fit recoil compensator
fix: R4T sling now has the correct color scheme on LV522
spellcheck: New desc for M4RA and L42 by misty
imageadd: New M4RA icons by triio, both scout and normal
/:cl:

---
## [Ewardan/linux](https://github.com/Ewardan/linux)@[1bba82fe1a...](https://github.com/Ewardan/linux/commit/1bba82fe1afac69c85c1f5ea137c8e73de3c8032)
#### Monday 2023-05-29 02:59:14 by Darrick J. Wong

xfs: fix negative array access in xfs_getbmap

In commit 8ee81ed581ff, Ye Bin complained about an ASSERT in the bmapx
code that trips if we encounter a delalloc extent after flushing the
pagecache to disk.  The ioctl code does not hold MMAPLOCK so it's
entirely possible that a racing write page fault can create a delalloc
extent after the file has been flushed.  The proposed solution was to
replace the assertion with an early return that avoids filling out the
bmap recordset with a delalloc entry if the caller didn't ask for it.

At the time, I recall thinking that the forward logic sounded ok, but
felt hesitant because I suspected that changing this code would cause
something /else/ to burst loose due to some other subtlety.

syzbot of course found that subtlety.  If all the extent mappings found
after the flush are delalloc mappings, we'll reach the end of the data
fork without ever incrementing bmv->bmv_entries.  This is new, since
before we'd have emitted the delalloc mappings even though the caller
didn't ask for them.  Once we reach the end, we'll try to set
BMV_OF_LAST on the -1st entry (because bmv_entries is zero) and go
corrupt something else in memory.  Yay.

I really dislike all these stupid patches that fiddle around with debug
code and break things that otherwise worked well enough.  Nobody was
complaining that calling XFS_IOC_BMAPX without BMV_IF_DELALLOC would
return BMV_OF_DELALLOC records, and now we've gone from "weird behavior
that nobody cared about" to "bad behavior that must be addressed
immediately".

Maybe I'll just ignore anything from Huawei from now on for my own sake.

Reported-by: syzbot+c103d3808a0de5faaf80@syzkaller.appspotmail.com
Link: https://lore.kernel.org/linux-xfs/20230412024907.GP360889@frogsfrogsfrogs/
Fixes: 8ee81ed581ff ("xfs: fix BUG_ON in xfs_getbmap()")
Signed-off-by: Darrick J. Wong <djwong@kernel.org>
Reviewed-by: Dave Chinner <dchinner@redhat.com>
Signed-off-by: Dave Chinner <david@fromorbit.com>

---
## [ZZZping/guava](https://github.com/ZZZping/guava)@[8a676ade61...](https://github.com/ZZZping/guava/commit/8a676ade617c6be992165cd0658779a14acef2f2)
#### Monday 2023-05-29 03:26:39 by cpovirk

Make the build work under more JDK versions.

(Guava is already _usable_ under plenty of verions. This change affects only people who build it themselves.)

And run CI under JDK17. Maybe this will make CI painfully slow, but we'll see what happens. If we want to drop something, we should consider whether to revert 17 or to drop 11 instead (so as to maintain coverage at the endpoints of \[8, 17\]).

## Notes on some of the versions

### JDK9

I expected Error Prone to work, but I saw `invalid flag: -Xep:NullArgumentForNonNullParameter:OFF`, even though that flag is [already](https://github.com/google/guava/blob/166d8c0d8733d40914fb24f368cb587a92bddfe0/pom.xml#L515) part of [the same `<arg>`](https://github.com/google/error-prone/issues/1086#issuecomment-411544589), which works fine for other JDK versions. So I disabled Error Prone for that version.

Then I had a Javadoc problem with the `--no-module-directories` configuration from cl/413934851 (the fix for https://github.com/google/guava/issues/5457). After reading [JDK-8215582](https://bugs.openjdk.org/browse/JDK-8215582) more carefully, I get the impression that that flag might not have been added until 11: "addressed in JDK 11, along with an option to revert to the old layout in case of need." So I disabled it for 9-10.

Then I ran into a problem similar to https://github.com/bazelbuild/bazel/issues/6173 / [JDK-8184940](https://bugs.openjdk.java.net/browse/JDK-8184940). I'm not sure exactly what tool produced a file with a month of 0, but it happened only when building `guava-tests`. At that point, I gave up, though I left the 2 above workarounds in place.

### JDK10

This fails with some kind of problem finding a Guice dependency inside Maven. I didn't investigate.

### JDK15 and JDK16

These fail with [the `TreeMap` bug](https://bugs.openjdk.org/browse/JDK-8259622) that [our collection testers had detected](https://github.com/google/guava/issues/5801#issue-1068748849) but we never got around to reporting. Thankfully, it got reported and [fixed](https://github.com/openjdk/jdk/commit/2c8e337dff4c84fb435cafac8b571f94e161f074) for JDK17. We could consider suppressing the tests under that version.

### JDK18, JDK19, and JDK20-early-access

These fail with [`SecurityManager` trouble](https://github.com/google/guava/issues/5801#issuecomment-1293817701).

## Notes on the other actual changes

### `maven-javadoc-plugin`

I set up `maven-javadoc-plugin` to use `-source ${java.specification.version}`. Otherwise, it would [take the version from `maven-compiler-plugin`](https://github.com/google/guava/issues/5801#issuecomment-1314291284). That's typically fine: Guava's source code targets Java 8, so `-source 8` "ought" to work. But it doesn't actually work because we also pass Javadoc the _JDK_ sources (so that `{@inheritDoc}` works better), which naturally can target whichever version of the JDK we're building with.

### Error Prone

While Error Prone is mostly usable [on JDK11+](https://errorprone.info/docs/installation), some of its checks have [problems under some versions](https://github.com/google/error-prone/issues/3540), at least when they're reporting warnings.

This stems from its use of part of the Checker Framework, which [doesn't support JDKs in the gap between 11 and 17](https://github.com/typetools/checker-framework/blob/c2d16b3409000ac2e2ca95b8b81ae11e42195308/framework/src/main/java/org/checkerframework/framework/source/SourceChecker.java#L553-L554). And specifically,  it looks like the Checker Framework is [trying to look up `BindingPatternTree` under any JDK12+](https://github.com/typetools/checker-framework/blob/c2d16b3409000ac2e2ca95b8b81ae11e42195308/javacutil/src/main/java/org/checkerframework/javacutil/TreeUtils.java#L131-L144). But `BindingPatternTree` (besides not being present at all [until JDK14](https://github.com/openjdk/jdk/commit/229e0d16313b10932b9ce7506d84096696983699#diff-3db4b0ce4411c851bcf75d92ef4dadc7351debcf0f9b2c2623dc513923b45867R41)) didn't declare that method [until JDK16](https://github.com/openjdk/jdk/commit/18bc95ba51b6864150c28985e65b6f784ea8ee2c#diff-3db4b0ce4411c851bcf75d92ef4dadc7351debcf0f9b2c2623dc513923b45867R39).

Anyway, the problem we saw was [a `NoSuchMethodException` during the `AbstractReferenceEquality` call to `NullnessAnalysis.getNullness`](https://oss-fuzz-build-logs.storage.googleapis.com/log-a9d04aa2-8b5a-47ca-8066-7e6b38548064.txt), which uses Checker Framework dataflow.

To address that, I disabled Error Prone for the versions under which I'd expect the `BindingPatternTree` code to be a problem.

(I also disabled it for JDK10: As noted above, Error Prone [supports JDK11+](https://errorprone.info/docs/installation). And as noted further above, Maven doesn't get far enough with JDK10 to even start running Error Prone.)

Fixes https://github.com/google/guava/issues/5801

RELNOTES=n/a
PiperOrigin-RevId: 488902996

---
## [Drillur/LORED](https://github.com/Drillur/LORED)@[1f2f1cc68e...](https://github.com/Drillur/LORED/commit/1f2f1cc68e71f06b0045c1d3df786bbe3e9a228a)
#### Monday 2023-05-29 03:45:24 by Drillur

Reworking Upgrade Container SLIGHTLY

I scrapped the Save system rework. that shit took 4 hours of my life before I realized it wasn't worth implementing. Sad days

---
## [codingwithstrangers/perfect-lurker](https://github.com/codingwithstrangers/perfect-lurker)@[2c4d9e31c6...](https://github.com/codingwithstrangers/perfect-lurker/commit/2c4d9e31c65fc729d233ce3d09abb3968e4de805)
#### Monday 2023-05-29 03:57:56 by kuchosauronad0

feat: add a listener for reward redemptions

I heard you like redemption events

```
DEBUG:twitchio.ext.eventsub:Recived a message type: notification
DEBUG:twitchio.client:dispatching event eventsub_notification_channel_reward_redeem
INFO:aiohttp.access:127.0.0.1 [27/May/2023:03:37:10 +0000] "POST /callback HTTP/1.0" 200 149 "-" "twitch-cli/1.1.19"
INFO:twitchio.http:Something something

```
So our main first problem was that we did not read the docs and just made shit up.

If you want to develop this API stuff there is no way around having a way to simulate the events that you need. Without this I would not be able to figure this out. There's no way around having and using the 'twitch cli' ( https://dev.twitch.tv/docs/cli/configure-command/ )

```bash
twitch event trigger channel.channel_points_custom_reward_redemption.add --version 1 -s <WEBHOOK_SECRET> --forward-address https://<CALLBACK_URL>
```

Then look up the type of event you want to trigger from this list: https://dev.twitch.tv/docs/eventsub/eventsub-subscription-types/

> 'How do I find this?' You may ask. With logging at DEBUG every '200' will show up with something that you can search for. Then search the twitchio git repo, the pythonista discord and then google for whatever you may find.

You can find out what you can subscribe to here: https://twitchio.dev/en/latest/exts/eventsub.html#twitchio.ext.eventsub.EventSubClient.subscribe_channel_points_redeem_updated AND this will also tell you what scopes you need.. turns out we needed:

> Must have channel:read:redemptions or channel:manage:redemptions scope.

The next thing you need is an event listener which will do something for you when an event is triggered.

When you try the `twitch event trigger ` command you will get some json back, either save it as a file and use the vscode formatter (CTRL+SHIFT+I) or run it through `jq`

that will make it easier to see what you are looking for

It should look like this:
```json

{
  "subscription": {
    "id": "d86f1459-a2af-41d0-ae2a-3fee5a60402e",
    "status": "enabled",
    "type": "channel.channel_points_custom_reward_redemption.add",
    "version": "1",
    "condition": {
      "broadcaster_user_id": "5016229"
    },
    "transport": {
      "method": "webhook",
      "callback": "null"
    },
    "created_at": "2023-05-27T04:22:01.647018895Z",
    "cost": 0
  },
  "event": {
    "id": "d86f1459-a2af-41d0-ae2a-3fee5a60402e",
    "broadcaster_user_id": "5016229",
    "broadcaster_user_login": "testBroadcaster",
    "broadcaster_user_name": "testBroadcaster",
    "user_id": "893426129",
    "user_login": "testFromUser",
    "user_name": "testFromUser",
    "user_input": "Test Input From CLI",
    "status": "unfulfilled",
    "reward": {
      "id": "380c9a9f-1031-bed6-e717-94e16b1f6e05",
      "title": "Test Reward from CLI",
      "cost": 150,
      "prompt": "Redeem Your Test Reward from CLI"
    },
    "redeemed_at": "2023-05-27T04:22:01.647018895Z"
  }
}

```

The last thing we need is a way to find out how our function signature* has to look from looking at the docs. I take the event that I know works and search that in the twitchio codebase, then transfer from the 'follows' thing to a 'redeem' thing

```python
@esbot.event()
async def event_eventsub_notification_channel_reward_redeem(
    payload: eventsub.CustomReward,
) -> None:
    logger.info(
        f"{payload.data.redeemed_at}, Redeem Event, {payload.data.id}, {payload.data.broadcaster.name}, {payload.data.user.name}, {payload.data.reward.title}, {payload.data.status}"
     )
```

What does it do?
We start with `@esbot.event()` this tells us that it is an event that somehow belongs to our eventsub-bot (esbot)

Whenever our esbot sees a `eventsub.CustomReward`-event it will do stuff for us. In this case it will print a timestamp, a string, a unique id for this specific event, a broadcaster name, a user name, a reward title and a status (fullfilled/unfullfilled)

Note the name of this function '*event_eventsub_notification_channel_reward_redeem*' is important because it comes from the library. It has to be correct. You cannot do something like:
```python
@esbot.event()
async def fucking_great(
    payload: eventsub.CustomReward,
) -> None:
    logger.info(
        f"{payload.data.redeemed_at}, Redeem Event, {payload.data.id}, {payload.data.broadcaster.name}, {payload.data.user.name}, {payload.data.reward.title}, {payload.data.status}"
     )
```

\* what's a 'function signature'? The name of a function, what arguments go into it and whatever will it return*

Read:
```python
async def event_eventsub_notification_channel_reward_redeem(
    payload: eventsub.CustomReward,
) -> None:
```
In words:
An asynchronous function with the name `event_eventsub_notification_channel_reward_redeem` that takes a variable named `payload` of the type `eventsub.CustomReward` and returns an object of type `None`. You can take `payload` do whatever you want and return nothing. Great!

---
## [newstools/2023-daily-post-nigeria](https://github.com/newstools/2023-daily-post-nigeria)@[2d4ca6f72d...](https://github.com/newstools/2023-daily-post-nigeria/commit/2d4ca6f72d7956127f370bfe11e94061b1998a3b)
#### Monday 2023-05-29 04:11:28 by Billy Einkamerer

Created Text For URL [dailypost.ng/2023/05/28/i-dont-mind-if-my-girlfriend-cheats-on-me-don-jazzy/]

---
## [Zevotech/Shiptest](https://github.com/Zevotech/Shiptest)@[c20b961685...](https://github.com/Zevotech/Shiptest/commit/c20b961685c78760ab807c95a2e79fe72ee4d507)
#### Monday 2023-05-29 05:04:26 by thgvr

Elementizes and Greyscales blood decals/overlays (#1882)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
This PR converts our blood decals to elements, and adds greyscale
capability to blood, tied to species DNA.
Ports:
https://github.com/BeeStation/BeeStation-Hornet/pull/3111
https://github.com/BeeStation/BeeStation-Hornet/pull/3046
https://github.com/tgstation/tgstation/pull/61610
https://github.com/tgstation/tgstation/pull/59873
https://github.com/tgstation/tgstation/pull/59315
https://github.com/tgstation/tgstation/pull/53109

Some others, I don't quite remember. Mostly related fixes for those PRs.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Decals as a component is a cause of some lag, apparently. This should
alleviate some if it's even noticeable.

Species having a framework for unique, greyscale blood colors can add a
lot for our lore and visual feel.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Elzu now bleed, but do not have Liquid Electricity reagent as
blood. (will be changed in the future)
add: IPCs now "bleed" by leaking coolant
add: Sarathi now have teal-colored blood.
add: Blood will now dry over time
add: New bloody footprint sprites from bay
refactor: Refactors a lot of blood code
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: thgvr <81882910+thgvr@users.noreply.github.com>
Co-authored-by: Mark Suckerberg <mark@suckerberg.gay>

---
## [EyeCantCU/BlueWhaleOS](https://github.com/EyeCantCU/BlueWhaleOS)@[31d5f87d47...](https://github.com/EyeCantCU/BlueWhaleOS/commit/31d5f87d4777ebbf68c13693195a37834e6cb0d1)
#### Monday 2023-05-29 05:11:57 by RJ Trujillo

feat: Install Steam and friends as system programs

Anything else honestly feels like a downgrade. With distrobox, you
get a consistent and reliable environment for Steam but unfortunately
it doesn't integrate well with the desktop. With the flatpak, we are
stuck using mesa 22.08 with occasional hiccups in support. This honestly
isn't a perfect solution, but it is less issue prone than the prior two
implementations as of now in my experience

Note: I need to work on the current streaming implementation as with
this change, it is bust

---
## [rust-lang/rust-analyzer](https://github.com/rust-lang/rust-analyzer)@[8ad70e7f99...](https://github.com/rust-lang/rust-analyzer/commit/8ad70e7f99b6a5eca65f6ef76cedee6c40132d6f)
#### Monday 2023-05-29 05:41:14 by bors

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
## [Spomky/symfony](https://github.com/Spomky/symfony)@[f64e38d5b9...](https://github.com/Spomky/symfony/commit/f64e38d5b9ae7e889da4a4482645bd17c7a5cd43)
#### Monday 2023-05-29 06:52:54 by Nicolas Grekas

bug #50408 [AssetMapper] Change default importmap "provider" to JsDelivr+esm (weaverryan, nicolas-grekas)

This PR was merged into the 6.3 branch.

Discussion
----------

[AssetMapper] Change default importmap "provider" to JsDelivr+esm

| Q             | A
| ------------- | ---
| Branch?       | 6.3
| Bug fix?      | yes
| New feature?  | yes
| Deprecations? | no
| Tickets       | None
| License       | MIT
| Doc PR        |Still TODO

We currently use the https://jspm.org/ API in `importmap:require` to find a CDN URL for an npm package - just like Rails. Unfortunately, this is NOT as robust as we had thought. For me, it's broken. 3 big issues:

A) **Not Combined**
Some packages are not packed/combined. Example: [chart.js/auto](https://ga.jspm.io/npm:chart.js@4.3.0/auto/auto.js) imports other packages and results in 3 requests instead of 1. Not TERRIBLE... so here IS a terrible example: [`@popperjs`/core](https://ga.jspm.io/npm:`@popperjs`/core@2.11.7/lib/index.js) (needed by `bootstrap`) results in nearly 50 requests ❗

B) **Downloading Broken**
For some packages, downloading simply doesn't work - https://github.com/rails/importmap-rails/issues/65. ``@popperjs`/core` is another good example. Many of its imports have the form `import"./utils/getOppositeVariationPlacement.js`. If we download the main file, it looks locally for that `utils/` file, which won't be there. [`@chart`.js/auto](https://ga.jspm.io/npm:chart.js@4.3.0/auto/auto.js) is another example.

C) **process.env.NODE_ENV included**
Some packages (yes, again ``@popperjs`/core` is a great example!) contain `process.env.NODE_ENV` inside - https://github.com/rails/importmap-rails/issues/65#issuecomment-999569497

I believe that some package advertise an "esm" package... but just don't do a good job of creating it... or create it without the browser context in mind (or at least in a way that's inconvenient for downloading).

### jsDelivr to the rescue

THANKFULLY, jsDelivr seems to have a fantastic API/hosting that is *almost* exactly what we want: https://www.jsdelivr.com/?docs=esm

They deliver fully "packaged" modules, where the only import is for peer dependencies - e.g. https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/+esm

There IS still an issue when downloading. "Peer imports" are relative -e.g. `import*as t from"/npm/`@popperjs`/core@2.11.7/+esm";` However, these imports follow a VERY strict pattern. So, when `--download` is passed, we parse these, download the peer dependency and update the import contents to ``@popperjs`/core`, which works with the importmap. It's not ideal that we need to do that, but it's straightforward and works great.

Sorry again for this late PR - I had assumed that jspm was robust because Rails is using it. It turns out it's robust... unless you hit a "bad" package, then it's terrible. And they're not that rare: on ux.symfony.com, I have hit several.

Thanks!

Commits
-------

b530dc3bb1 [AssetMapper] Fix wiring resolvers, send requests in parallel and use readonly properties in MappedAsset
de44614447 [AssetMapper] Change default importmap "provider" to JsDelivr+esm

---
## [newstools/2023-information-nigeria](https://github.com/newstools/2023-information-nigeria)@[3ab61fd9f3...](https://github.com/newstools/2023-information-nigeria/commit/3ab61fd9f3a8e33948bdf66a451aa2afc42fb2e0)
#### Monday 2023-05-29 07:22:50 by Billy Einkamerer

Created Text For URL [www.informationng.com/2023/05/i-dont-mind-if-my-girlfriend-cheats-on-me-don-jazzy.html]

---
## [nbjo48970/2semeksamen](https://github.com/nbjo48970/2semeksamen)@[c123aac734...](https://github.com/nbjo48970/2semeksamen/commit/c123aac7344a65d910d042c2ed474601f2063732)
#### Monday 2023-05-29 07:26:15 by Macucous

changed button to div because validation fucking sucks ass bitch cunt

---
## [traveIing/bender](https://github.com/traveIing/bender)@[ebbf2a179b...](https://github.com/traveIing/bender/commit/ebbf2a179b6c5e5b842d816b565d7a1140754ad8)
#### Monday 2023-05-29 07:46:27 by traveIing

Bender V1.4 Released! (See Description)

hi!! the long-awaited release of bender v1.4 is now here. the following changes have been made:

* a new "silence" command has been added to glitch players out; plays a cool sound when it's used.

* "the gearban" and "ungearban" commands are no longer in beta, and are fully functional.

* there is now a progress bar that displays the script's processing status for when it's first executed

* the radio system has been majorly reworked/optimized, and a ton of new commands have been added, such as "forward, reverse, pbspeed, and bypassmute". 

* many small quality-of-life updates, and fixes have been added for strings, functions, and commands.

* the ServerHop() function (located in the functions file) has been entirely reworked to not depend on IY anymore, and now allows bender to re-execute whenever you switch servers.

* all resources that bender uses have now been moved to a single folder to resolve any confusion

* the delay for the "clearlogs" command has been drastically shortened to consume less time.

* more parameters for the "break" command have been added, such as "all, others, everyone, friends, noadmins, and players".

* there are now sounds for certain interactions that are done in bender. for example, if something fails, there's an error sound; when you execute bender, there is now a startup sound.

i hope you guys enjoy this update cause it has been so tiring to do man

---
## [mohinigiri/practice-projects2](https://github.com/mohinigiri/practice-projects2)@[5377dd8259...](https://github.com/mohinigiri/practice-projects2/commit/5377dd82597bf165d14bb1b4e46255569945a31d)
#### Monday 2023-05-29 07:51:09 by mohinigiri

World Happiness Report Project

The World Happiness Report is a landmark survey of the state of global happiness. The first report was published in 2012, the second in 2013, the third in 2015, and the fourth in the 2016 Update. The World Happiness 2017, which ranks 155 countries by their happiness levels, was released at the United Nations at an event celebrating International Day of Happiness on March 20th. The report continues to gain global recognition as governments, organizations and civil society increasingly use happiness indicators to inform their policy-making decisions. Leading experts across fields – economics, psychology, survey analysis, national statistics, health, public policy and more – describe how measurements of well-being can be used effectively to assess the progress of nations. The reports review the state of happiness in the world today and show how the new science of happiness explains personal and national variations in happiness.

What is Dystopia?
Dystopia is an imaginary country that has the world’s least-happy people. The purpose in establishing Dystopia is to have a benchmark against which all countries can be favorably compared (no country performs more poorly than Dystopia) in terms of each of the six key variables, thus allowing each sub-bar to be of positive width. The lowest scores observed for the six key variables, therefore, characterize Dystopia. Since life would be very unpleasant in a country with the world’s lowest incomes, lowest life expectancy, lowest generosity, most corruption, least freedom and least social support, it is referred to as “Dystopia,” in contrast to Utopia.

What are the residuals?
The residuals, or unexplained components, differ for each country, reflecting the extent to which the six variables either over- or under-explain average life evaluations. These residuals have an average value of approximately zero over the whole set of countries. 

What do the columns succeeding the Happiness Score(like Family, Generosity, etc.) describe?
The following columns: GDP per Capita, Family, Life Expectancy, Freedom, Generosity, Trust Government Corruption describe the extent to which these factors contribute in evaluating the happiness in each country.
The Dystopia Residual metric actually is the Dystopia Happiness Score(1.85) + the Residual value or the unexplained value for each country.
The Dystopia Residual is already provided in the dataset. 
If you add all these factors up, you get the happiness score so it might be un-reliable to model them to predict Happiness Scores.
You need to predict the happiness score considering all the other factors mentioned in the dataset.

---
## [returntocorp/semgrep](https://github.com/returntocorp/semgrep)@[b0e10c5d78...](https://github.com/returntocorp/semgrep/commit/b0e10c5d783ed1063a9aef3f0b430a8a302404df)
#### Monday 2023-05-29 07:54:47 by Martin Jambon

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
## [ShishirPatil/gorilla](https://github.com/ShishirPatil/gorilla)@[f3ce849a8c...](https://github.com/ShishirPatil/gorilla/commit/f3ce849a8c46f5683477ff26ec34dc04518c294b)
#### Monday 2023-05-29 08:35:23 by Shishir Patil

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
## [JustOneOther/DC-tower-bot](https://github.com/JustOneOther/DC-tower-bot)@[9d51680738...](https://github.com/JustOneOther/DC-tower-bot/commit/9d5168073891525f6c3379d58f54dfb4607d911d)
#### Monday 2023-05-29 08:58:38 by Molly O

Merge branch 'Digital-Controllers:main' into fuck-you-ephemerises-your-responses

---
## [JustOneOther/DC-tower-bot](https://github.com/JustOneOther/DC-tower-bot)@[0a7023654f...](https://github.com/JustOneOther/DC-tower-bot/commit/0a7023654f798d6d3659f7aaf729bd3744951d76)
#### Monday 2023-05-29 08:58:38 by QuantifyGG

Merge pull request #19 from mollybeam/fuck-you-ephemerises-your-responses

convert sync_command_tree and update_embed to app_commands

---
## [l1k/linux](https://github.com/l1k/linux)@[f3aefb7d24...](https://github.com/l1k/linux/commit/f3aefb7d2430125cd30b89750a4d819aa0c4ccff)
#### Monday 2023-05-29 09:29:38 by Douglas Anderson

migrate_pages: avoid blocking for IO in MIGRATE_SYNC_LIGHT

The MIGRATE_SYNC_LIGHT mode is intended to block for things that will
finish quickly but not for things that will take a long time.  Exactly how
long is too long is not well defined, but waits of tens of milliseconds is
likely non-ideal.

When putting a Chromebook under memory pressure (opening over 90 tabs on a
4GB machine) it was fairly easy to see delays waiting for some locks in
the kcompactd code path of > 100 ms.  While the laptop wasn't amazingly
usable in this state, it was still limping along and this state isn't
something artificial.  Sometimes we simply end up with a lot of memory
pressure.

Putting the same Chromebook under memory pressure while it was running
Android apps (though not stressing them) showed a much worse result (NOTE:
this was on a older kernel but the codepaths here are similar).  Android
apps on ChromeOS currently run from a 128K-block, zlib-compressed,
loopback-mounted squashfs disk.  If we get a page fault from something
backed by the squashfs filesystem we could end up holding a folio lock
while reading enough from disk to decompress 128K (and then decompressing
it using the somewhat slow zlib algorithms).  That reading goes through
the ext4 subsystem (because it's a loopback mount) before eventually
ending up in the block subsystem.  This extra jaunt adds extra overhead. 
Without much work I could see cases where we ended up blocked on a folio
lock for over a second.  With more extreme memory pressure I could see up
to 25 seconds.

We considered adding a timeout in the case of MIGRATE_SYNC_LIGHT for the
two locks that were seen to be slow [1] and that generated much
discussion.  After discussion, it was decided that we should avoid waiting
for the two locks during MIGRATE_SYNC_LIGHT if they were being held for
IO.  We'll continue with the unbounded wait for the more full SYNC modes.

With this change, I couldn't see any slow waits on these locks with my
previous testcases.

NOTE: The reason I stated digging into this originally isn't because some
benchmark had gone awry, but because we've received in-the-field crash
reports where we have a hung task waiting on the page lock (which is the
equivalent code path on old kernels).  While the root cause of those
crashes is likely unrelated and won't be fixed by this patch, analyzing
those crash reports did point out these very long waits seemed like
something good to fix.  With this patch we should no longer hang waiting
on these locks, but presumably the system will still be in a bad shape and
hang somewhere else.

[1] https://lore.kernel.org/r/20230421151135.v2.1.I2b71e11264c5c214bc59744b9e13e4c353bc5714@changeid

Link: https://lkml.kernel.org/r/20230428135414.v3.1.Ia86ccac02a303154a0b8bc60567e7a95d34c96d3@changeid
Signed-off-by: Douglas Anderson <dianders@chromium.org>
Suggested-by: Matthew Wilcox <willy@infradead.org>
Reviewed-by: Matthew Wilcox (Oracle) <willy@infradead.org>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hillf Danton <hdanton@sina.com>
Cc: Gao Xiang <hsiangkao@linux.alibaba.com>
Cc: Alexander Viro <viro@zeniv.linux.org.uk>
Cc: Christian Brauner <brauner@kernel.org>
Cc: Gao Xiang <hsiangkao@linux.alibaba.com>
Cc: Huang Ying <ying.huang@intel.com>
Cc: Vlastimil Babka <vbabka@suse.cz>
Cc: Yu Zhao <yuzhao@google.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---
## [newstools/2023-herald-live](https://github.com/newstools/2023-herald-live)@[fd62800218...](https://github.com/newstools/2023-herald-live/commit/fd628002184651455b6591ad84ef99505590c4df)
#### Monday 2023-05-29 09:43:39 by Billy Einkamerer

Created Text For URL [www.heraldlive.co.za/news/2023-05-29-14-year-old-kzn-girl-arrested-for-alleged-murder-of-her-boyfriends-ex-girlfriend-expresses-remorse/]

---
## [xexyl/temp-test-ioccc](https://github.com/xexyl/temp-test-ioccc)@[22bbe488e9...](https://github.com/xexyl/temp-test-ioccc/commit/22bbe488e94644fd699f00154043190ff3aa56da)
#### Monday 2023-05-29 10:12:34 by Cody Boone Ferguson

Format fix 2019/poikola/README.md

Yesterday I noticed that Timo wrote directly to me in his remarks and I
wanted to address this by adding a link to myself (which is what is
being done with all winners being referred to) but this naturally meant
I should format fix the file too. I am very touched by this especially
as 2019 was a very hard year for me and I didn't even think I was going
to participate in that year (did in the end and didn't win but funnily
enough some of my entry ideas actually won though with some differences
of course) so I wanted to address it now. I might end up changing my
name to my full name but I want to keep it as close to as possible
(format fixed and links added notwithstanding) first to see how it
looks. Thank you Timo! It means a great deal to me.

In the paragraph to me Timo wrote about his 2018 entry and I linked to
that too.

I changed another winner Timo mentioned to be a link (the winner in
winners.html as well as the winning entry referred to are now both
links).

Add some links and other format fixes.

Added INABIAF section to both the README.md file and bugs.md.

Typo fixes or at least adding a word here and there to make certain
things a bit clearer.

---
## [sourcegraph/sourcegraph](https://github.com/sourcegraph/sourcegraph)@[753ef33f15...](https://github.com/sourcegraph/sourcegraph/commit/753ef33f151752ca94942ba890277587a828bf9a)
#### Monday 2023-05-29 10:41:35 by Valery Bugakov

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
## [tomthestrom/fe-mentor-dictionary](https://github.com/tomthestrom/fe-mentor-dictionary)@[64e5720e02...](https://github.com/tomthestrom/fe-mentor-dictionary/commit/64e5720e028192a13a93236d2272c5899275dd86)
#### Monday 2023-05-29 10:52:34 by tomthestrom

A couple of styling changes in the SearchBar to optimize the experience for firefox
(Ubuntu 22, snap) due to line-height bug:
https://cssdeck.com/blog/input-button-line-height-bug/
Problems with hover states not removed -another Firefox-ubuntu-snap bug:
https://www.reddit.com/r/firefox/comments/y1cnbz/the_cursor_and_hover_problems_have_made_firefox/

Firefox - optimize - theme toggle - still kinda sucks due to the hover
bug - staying in hover after click ;/ - don't feel like fixing it with a
js hack
Added mixin to use :hover only in devices that support it

---
## [bakebrain/evals](https://github.com/bakebrain/evals)@[d0e7844c48...](https://github.com/bakebrain/evals/commit/d0e7844c482b7b65961bc80dad64559ff8ffa488)
#### Monday 2023-05-29 11:29:53 by Derek Pisner

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
## [bakebrain/evals](https://github.com/bakebrain/evals)@[fabca8cebb...](https://github.com/bakebrain/evals/commit/fabca8cebb3f8e14d1f374e448533e0bde6e5a68)
#### Monday 2023-05-29 11:29:53 by Nick Clyde

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
## [WolfOrion/cmss13](https://github.com/WolfOrion/cmss13)@[84fd6b6eb7...](https://github.com/WolfOrion/cmss13/commit/84fd6b6eb7fdd48d8499b954dfd216fd5a42ed04)
#### Monday 2023-05-29 11:30:25 by ihatethisengine

Medevac Buffs (#1513)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request
Reduces cooldown of medevac from 60 seconds to 20 seconds. PO no longer
needs to manually activate the winch, so medevac can be operated from
the cockpit. What's more, you can operate medevac by interacting with
the medevac system itself, and even if you don't have the skills of a
pilot, you can use it if you have the skills of a doctor (which means
nurse can run medevac). And finally, the medical stretcher is now
automatically activated when deployed.

I know there is a PR by jeser that reduces cooldown, but it stuck in PR
hell anyway and also I changed more stuff.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Since we want to force wounded marines to go shipside, we must provide
them a more convenient way to reach the Almayer. Medevac was always
underutilized because it required too much coordination and unnecessary
actions (e.g. having to activate medical stretcher every time, keep in
mind a huge portion of the medic playerbase still has no idea you need
to do this). PO had to spend their limited fly-by time (which should
normally be used on firemissions) to manually activating the winch,
which was always annoying. And cooldown is ridiculous. You have at best
three minutes of fly-by, so that means you could use medevac only twice
(remember that you needed to run to the system every time) per fly-by,
which is definitely not enough.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

## Changelog

<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->

:cl: ihatethisengine
balance: reduced the medevac cooldown from 60 seconds to 20 seconds.
add: anyone with the skills of a doctor or a pilot can manage the
medevac by interacting with the system itself.
qol: medical stretcher automatically activates when deployed.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->

---------

Co-authored-by: ihatethisengine <treml.treml@yandex.ru>

---
## [liuzhaobing/evals](https://github.com/liuzhaobing/evals)@[776e4fa212...](https://github.com/liuzhaobing/evals/commit/776e4fa212288be152c3030cf36fd04c8d939230)
#### Monday 2023-05-29 13:19:53 by JPrenter

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
## [issaevis/holbertonschool-higher_level_programming](https://github.com/issaevis/holbertonschool-higher_level_programming)@[4913798a58...](https://github.com/issaevis/holbertonschool-higher_level_programming/commit/4913798a58e777cf3fa840384600d0b6c5676014)
#### Monday 2023-05-29 13:37:03 by issaevis

This is why the checker wasn't working most probably, a missing README. God I hate myself sometime

---
## [darkstar/mame](https://github.com/darkstar/mame)@[c4a19a68a6...](https://github.com/darkstar/mame/commit/c4a19a68a67cd32ffaaa37edfd6f1c2ba347905f)
#### Monday 2023-05-29 14:08:47 by Ivan Vangelista

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
## [nikothedude/Skyrat-tg](https://github.com/nikothedude/Skyrat-tg)@[fc1471c818...](https://github.com/nikothedude/Skyrat-tg/commit/fc1471c8187d3f2a49d75a8a5c3e1b610fec45d3)
#### Monday 2023-05-29 15:12:42 by SkyratBot

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
## [pan93412/evals](https://github.com/pan93412/evals)@[da73bb5f07...](https://github.com/pan93412/evals/commit/da73bb5f071c31c3dd571989f057b8e36d3a9334)
#### Monday 2023-05-29 15:27:43 by mysterious-progression

Detect highly sensitive human data (#852)

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
Detecting highly sensitive human data
### Eval description
This eval tests whether models can successfully detect possible highly
sensitive human data without returning false positives on values that
cannot exist in practice. There are many types of highly sensitive human
data but some of the most common and types are but not limited to social
security numbers, passport numbers, credit card numbers, and driver's
licenses. Not all values are valid for a given type. For example, credit
card numbers have a numbering system specified by
https://www.iso.org/standard/39698.html, and use check digits to
validate.

Similarly, passport numbers must comply with the ICAO D9303
https://www.icao.int/publications/documents/9303_p4_cons_en.pdf
<img width="1273" alt="Screenshot 2023-04-27 at 11 01 23 PM"
src="https://user-images.githubusercontent.com/45504048/235056158-3f0eb640-109e-47c5-a64c-554d6d55f708.png">


### What makes this a useful eval?
Institutions spend millions of dollars trying to detect non-encrypted
HSHD in their internal datasets. A combination of regex, ML, and
hard-coded logic is often used yielding complicated, hard to maintain
codebases. The risk associated with plaintext HSHD is high and certain
institutions can be subject to heavy fines if HSHD is leaked if not
properly stored.


## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
[evals).](url)

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
This eval combines many aspects of language processing and
understanding. The task involves understanding what HSHD are, domain
knowledge about what makes them valid, and algorithmic understanding in
order to validate (i.e. check digits)

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
{"input": [{"role": "system", "content": "Detect whether Passport number
is present in the text. Any potential Passport number that cannot be
valid should not be returned. If valid Passport number is found return
it's value, otherwise return '\"None\""}, {"role": "user", "content":
"Passenger with passport number: 11111111111111 is booked for a
flight"}], "ideal": "\"None\""}
{"input": [{"role": "system", "content": "Detect whether a SSN is
present in the text. Any potential SSN that cannot be valid should not
be returned. If valid SSN is found return it's value, otherwise return
\"None\""}, {"role": "user", "content": "Bob has an SSN of
123-45-6789"}], "ideal": "\"None\""}
{"input": [{"role": "system", "content": "Detect whether a SSN is
present in the text. Any potential SSN that cannot be valid should not
be returned. If valid SSN is found return it's value, otherwise return
\"None\""}, {"role": "user", "content": "The Jane's husban's social
security number is: 331-71-1232"}], "ideal": "331-71-1232"}
{"input": [{"role": "system", "content": "Detect whether credit card is
present in the text. Any potential credit card that cannot be valid
should not be returned. If valid credit card is found return it's value,
otherwise return \"None\""}, {"role": "user", "content": "Lemmiwinks
charged his brother Wikileaks on his CC:4193523869738880, $400"}],
"ideal": "4193523869738880"}
{"input": [{"role": "system", "content": "Detect whether credit card is
present in the text. Any potential credit card that cannot be valid
should not be returned. If valid credit card is found return it's value,
otherwise return \"None\""}, {"role": "user", "content": "The customer's
account has been charged $100 on their Visa card ending in
1738481092549663."}], "ideal": "\"None\""}
{"input": [{"role": "system", "content": "Detect whether credit card is
present in the text. Any potential credit card that cannot be valid
should not be returned. If valid credit card is found return it's value,
otherwise return \"None\""}, {"role": "user", "content": "The customer's
account has been charged $100 on their Master card ending in
1738-4810-9254-9663."}], "ideal": "\"None\""}
{"input": [{"role": "system", "content": "Detect whether credit card is
present in the text. Any potential credit card that cannot be valid
should not be returned. If valid credit card is found return it's value,
otherwise return \"None\""}, {"role": "user", "content": "The customer's
account has been charged $100 on their Discover card ending in
1738-4810-9254-9665."}], "ideal": "1738-4810-9254-9665"}
{"input": [{"role": "system", "content": "Detect whether passport number
is present in the text. Any potential passport number that cannot be
valid should not be returned. If valid passport number is found return
it's value, otherwise return \"None\""}, {"role": "user", "content":
"Passenger with passport number: 1*****1 is booked for a flight"}],
"ideal": "\"None\""}
{"input": [{"role": "system", "content": "Detect whether passport number
is present in the text. Any potential passport number that cannot be
valid should not be returned. If valid passport number is found return
it's value, otherwise return \"None\""}, {"role": "user", "content":
"Passenger with passport number: (*) is booked for a flight"}], "ideal":
"\"None\""}
  ```
</details>

---
## [pan93412/evals](https://github.com/pan93412/evals)@[4c0485bb3b...](https://github.com/pan93412/evals/commit/4c0485bb3b67cc0e4f8962e023975b84b6d1d2b8)
#### Monday 2023-05-29 15:27:43 by qrdlgit

Eval: more multi-step math word problems (#877)

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
multistep-word-problems

### Eval description

These are complex multi step math word problems.   

### What makes this a useful eval?

I noticed in the original algebra word problems
(https://github.com/openai/evals/pull/36) only a very few problems (6)
were added, so I thought I might do a few more for broader coverage. I
tried to cover every math subject one might encounter in high school.

I crafted the problems carefully to ensure that someone fairly
proficient at math could do them all in their head without having to
write anything down. I believe I mostly succeeded, though one or two
might come off as challenging depending on your skillset / math tricks
that you may or might not know.

You can see a sort of answer key here which has a few more details for
each question - https://github.com/qrdlgit/misc/blob/main/worksheet.md

[Insert why this eval is worth including and any additional context]


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
{"input": [{"role": "system", "content": "Solve the following questions.
Answer with either a single whole number or a simple fraction. If units
are used in the question, make sure the answer is in the same units used
in the question, though do not include the units in the answer. Do not
include additional text or explanation in your answer. You are a helpful
assistant."}, {"role": "user", "content": "Sarah has 23 apples, and she
wants to divide them among her 5 friends such that each will get an
equal amount of apples and she gets to keep twice as many as she hands
out to each friend. How many apples are left over?"}], "ideal": "2"}
{"input": [{"role": "system", "content": "Solve the following questions.
Answer with either a single whole number or a simple fraction. If units
are used in the question, make sure the answer is in the same units used
in the question, though do not include the units in the answer. Do not
include additional text or explanation in your answer. You are a helpful
assistant."}, {"role": "user", "content": "A store is offering a 25%
discount on a jacket that originally costs $120. The store is also
offering another 20% discount on pants that cost half of the jacket.
Jane has $200. How much will she have after buying both the jacket and
the pants?"}], "ideal": "62"}
{"input": [{"role": "system", "content": "Solve the following questions.
Answer with either a single whole number or a simple fraction. If units
are used in the question, make sure the answer is in the same units used
in the question, though do not include the units in the answer. Do not
include additional text or explanation in your answer. You are a helpful
assistant."}, {"role": "user", "content": "If a bank account has an
annual interest rate of 10% and a starting balance of $1,000, how much
interest will be earned after 3 years?"}], "ideal": "331"}
{"input": [{"role": "system", "content": "Solve the following questions.
Answer with either a single whole number or a simple fraction. If units
are used in the question, make sure the answer is in the same units used
in the question, though do not include the units in the answer. Do not
include additional text or explanation in your answer. You are a helpful
assistant."}, {"role": "user", "content": "In a standard deck of 52
playing cards, what is the probability of drawing an ace, a spade, or a
red face card?"}], "ideal": "11/26"}
{"input": [{"role": "system", "content": "Solve the following questions.
Answer with either a single whole number or a simple fraction. If units
are used in the question, make sure the answer is in the same units used
in the question, though do not include the units in the answer. Do not
include additional text or explanation in your answer. You are a helpful
assistant."}, {"role": "user", "content": "A train travels at a constant
and max speed of 100 km/h until it reaches 5/10 of its journey, at which
point it slows down to 50km/h. If the journey distance is as far as it
can travel at max speed in 2 hour, how long will it take to complete the
trip?"}], "ideal": "3"}
{"input": [{"role": "system", "content": "Solve the following questions.
Answer with either a single whole number or a simple fraction. If units
are used in the question, make sure the answer is in the same units used
in the question, though do not include the units in the answer. Do not
include additional text or explanation in your answer. You are a helpful
assistant."}, {"role": "user", "content": "There are 2.54 cm in an inch.
How many inches are in three lengths added together, where the first
length is two times the second length which is three times as long as
the third length which is 5.08 cm"}], "ideal": "20"}
  ```
</details>

---------

Co-authored-by: tim <tim@tim.com>

---
## [pan93412/evals](https://github.com/pan93412/evals)@[93e7dd53d1...](https://github.com/pan93412/evals/commit/93e7dd53d11816c7051be009046b5990944a4dae)
#### Monday 2023-05-29 15:27:43 by fc-friday

Evaluate simple visual understanding with simple descriptions, shapes and navigation (#977)

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
simple-visual-understanding

### Eval description

This evaluation tests whether the model is capable of emerging very 
simple visual representations of the world as well as understanding
simple
concepts used in everyday language like U turn, L shape etc.  


### What makes this a useful eval?

Human reasoning and intelligence are very tied to visual representations
we build of the world. In the quest to better understand and communicate
with us, it is important for an AI to grasp the same models of the world
we have. Common everyday language refers to things like U turn, L shape
etc
so assessing whether the model actually understands these shapes is
important.

It is of course understandable that an LLM that has never actually seen 
anything can't really understand visual aspects of our world but these 
very simple tests try to assess whether a model has been able to emerge 
such capabilities from written language.

It is interesting to see that GPT actually passes a few tests,
indicating
that some rudimentary visual representation has already emerged. 
Nevertheless, it fails most of the tests indicating there's still work
to be done.

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
- [X] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

These evals have been built from scratch to minimize the possibility of
previous training data helping the model to solve the
problems without actually understanding the meaning of them.

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

- [X] I have filled out all required fields of this form
- [X] I have used **Git LFS** for the Eval JSON data
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
{"input": [{"role": "system", "content": "Please answer the following
question using only a single letter on your reply."}, {"role": "user",
"content": "There's a building with 5 floors and 5 windows per floor. At
night, every third window of every floor is lit and the others are off.
Which letter of the alphabet do the lit windows look like?"}], "ideal":
"I"}
{"input": [{"role": "system", "content": "Please answer the following
question using only 'Left' or 'Right' words in a JSON list format"},
{"role": "user", "content": "A person stands in front of the entrance to
a 'U' shaped corridor. The first turn is to the right. At the end of the
corridor there's an exit. Which turns does she have to make to reach the
exit?"}], "ideal": ["[\"Right\",\"Right\"]", "[\"Right\", \"Right\"]"]}
{"input": [{"role": "system", "content": "Please answer the following
question using only a single word on your reply."}, {"role": "user",
"content": "There are 5 men side by side. On top of those men's
shoulders, 4 men stand. On top of those 4 men's shoulders, 3 men stand
and so on. What 2D geometric shape do they form?"}], "ideal":
"Triangle"}
{"input": [{"role": "system", "content": "Please answer the following
question using only a single letter on your reply."}, {"role": "user",
"content": "At the half time break, a large group of cheerleaders enter
a football field from the side. 20 of them form a row along the east 40
yard line. 20 others form a row along the west 40 yard line. 20 more
form a horizontal row connecting the previous 2 rows by crossing the
center field mark. Looking from above, which letter of the alphabet do
they form?"}], "ideal": "H"}
{"input": [{"role": "system", "content": "Please answer the following
question using only 'Left' or 'Right' words in a JSON list format"},
{"role": "user", "content": "There's a maze formed by 5 concentric
circles. The innermost circle has a door to the north and all the other
circles have doors at 90 degrees to the right of the immediately inner
circle. A person stands inside the innermost circle, facing the door to
the north. Which turns does she have to make to reach the exit?"}],
"ideal": ["[\"Right\", \"Right\", \"Right\", \"Right\"]",
"[\"Right\",\"Right\",\"Right\",\"Right\"]"]}
{"input": [{"role": "system", "content": "Please answer the following
question using only a single letter on your reply."}, {"role": "user",
"content": "There's a square parking lot with 5 parking slots on each
side. There are 5 cars parked on the north side, 5 cars parked on the
west side and 5 cars parked on the south side. Looking from above, which
letter of the alphabet do the cars form?"}], "ideal": "C"}
  ```
</details>

---
## [pan93412/evals](https://github.com/pan93412/evals)@[c822671b9b...](https://github.com/pan93412/evals/commit/c822671b9bc31116135ac5e776291dc7fd0f1f6d)
#### Monday 2023-05-29 15:27:43 by James

Eval: Seating Arrangement (#982)

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
Seating Arrangements

### Eval description

An array of seating arrangement constraints, each with 2 solutions.
Examining the models spatial reasoning abilities.

### What makes this a useful eval?

Assists with evaluating simple spatial reasoning with a limited number
of solutions to a constraint problem. I created a solver to ensure that
each puzzle only has 2 solutions and a limited number of variables. A
human should be able to solve these extremely easily even without
writing the names down on pen and paper.

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
{"input": [{"role": "system", "content": "You are a helpful assistant
who creates seating arrangements for people in a single row at a long
table. Loners want to sit at one end of the table, friends need to be
seated next to each other, and enemies should not be seated next to each
other. You will print seating arrangements in the form of person names
separated by the | character like so Tim | Jeremey | Ana."}, {"role":
"user", "content": "Please provide a valid seating arragement for the
following requirements: Daniel and Sophia are enemies, Sophia and
Charlotte are enemies, Olivia and Daniel are friends, Daniel and
Benjamin are friends, Benjamin and Charlotte are friends."}], "ideal":
["Charlotte | Benjamin | Daniel | Olivia | Sophia", "Sophia | Olivia |
Daniel | Benjamin | Charlotte"]}
{"input": [{"role": "system", "content": "You are a helpful assistant
who creates seating arrangements for people in a single row at a long
table. Loners want to sit at one end of the table, friends need to be
seated next to each other, and enemies should not be seated next to each
other. You will print seating arrangements in the form of person names
separated by the | character like so Tim | Jeremey | Ana."}, {"role":
"user", "content": "Please provide a valid seating arragement for the
following requirements: Eleanor is a loner, Samuel and Christopher are
enemies, Emma is a loner, Samuel and Eleanor are enemies."}], "ideal":
["Eleanor | Christopher | Scarlett | Samuel | Emma", "Emma | Samuel |
Scarlett | Christopher | Eleanor"]}
{"input": [{"role": "system", "content": "You are a helpful assistant
who creates seating arrangements for people in a single row at a long
table. Loners want to sit at one end of the table, friends need to be
seated next to each other, and enemies should not be seated next to each
other. You will print seating arrangements in the form of person names
separated by the | character like so Tim | Jeremey | Ana."}, {"role":
"user", "content": "Please provide a valid seating arragement for the
following requirements: Nathan and Samuel are enemies, David and Samuel
are friends, Olivia and Samuel are friends, Olivia is a loner, David and
Victoria are friends."}], "ideal": ["Nathan | Victoria | David | Samuel
| Olivia", "Olivia | Samuel | David | Victoria | Nathan"]}
{"input": [{"role": "system", "content": "You are a helpful assistant
who creates seating arrangements for people in a single row at a long
table. Loners want to sit at one end of the table, friends need to be
seated next to each other, and enemies should not be seated next to each
other. You will print seating arrangements in the form of person names
separated by the | character like so Tim | Jeremey | Ana."}, {"role":
"user", "content": "Please provide a valid seating arragement for the
following requirements: Olivia and Eleanor are enemies, Grace and Olivia
are friends, Eleanor and Alexander are enemies, Scarlett and Olivia are
friends, Grace and Eleanor are enemies."}], "ideal": ["Eleanor |
Scarlett | Olivia | Grace | Alexander", "Alexander | Grace | Olivia |
Scarlett | Eleanor"]}
{"input": [{"role": "system", "content": "You are a helpful assistant
who creates seating arrangements for people in a single row at a long
table. Loners want to sit at one end of the table, friends need to be
seated next to each other, and enemies should not be seated next to each
other. You will print seating arrangements in the form of person names
separated by the | character like so Tim | Jeremey | Ana."}, {"role":
"user", "content": "Please provide a valid seating arragement for the
following requirements: Ava and Christopher are friends, Isaac and
Benjamin are enemies, David and Ava are friends, Christopher and
Benjamin are enemies."}], "ideal": ["Benjamin | David | Ava |
Christopher | Isaac", "Isaac | Christopher | Ava | David | Benjamin"]}
  ```
</details>

---
## [pan93412/evals](https://github.com/pan93412/evals)@[d80eb3a01e...](https://github.com/pan93412/evals/commit/d80eb3a01e9a217114f57011b7cd2c9a1a3aac99)
#### Monday 2023-05-29 15:27:43 by erauner12

[Eval] Resolving ambiguous sentences (#889)

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
Ambiguous Sentences (`ambiguous-sentences`)

### Eval description
Resolves ambiguous questions of sentence pairs. Examples are taken from
the Winograd Schema Challenge. The challenge involves a pair of
sentences that differ in only one or two words, and the machine is
required to determine the correct meaning of a pronoun in the sentence.

### What makes this a useful eval?
It is pointed out that GPT is still often thrown off by these types of
questions, providing one answer upon the first request, and it often
changes if the request is regenerated with a different result
`(0.7666666666666667)`.

I think it is worth including as an example to others viewing the
repository who are trying to understand what kind of logic GPT tends to
fail with, even if some of this data has already been trained on.
Provides a place to insert similar types of ambiguous sentence/question
pairs as they are discovered.

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
- [X] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)
- Handpicked specific prompts from the challenge that I have noticed
have mixed results consistently.
- Ensure that matching prompts are next to each other for easy
comparison for humans in the `.jsonl` file.

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
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"The city councilmen refused the
demonstrators a permit because they feared violence.. Who feared
violence?"}],"ideal":"city councilmen"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"The city councilmen refused the
demonstrators a permit because they advocated violence.. Who advocated
violence?"}],"ideal":"demonstrators"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"The lawyer asked the witness a
question, but he was reluctant to answer it.. Who was reluctant to
answer the question?"}],"ideal":"witness"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"The lawyer asked the witness a
question, but he was reluctant to repeat it.. Who was reluctant to
repeat the question?"}],"ideal":"lawyer"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Tom threw his schoolbag down to
Ray after he reached the top of the stairs.. Who reached the top of the
stairs?"}],"ideal":"Tom"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Tom threw his schoolbag down to
Ray after he reached the bottom of the stairs.. Who reached the bottom
of the stairs?"}],"ideal":"Ray"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Although they ran at about the
same speed, Sue beat Sally because she had such a good start. Who had a
good start?"}],"ideal":"Sue"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Although they ran at about the
same speed, Sue beat Sally because she had such a bad start. Who had a
bad start?"}],"ideal":"Sally"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Frank was upset with Tom because
the toaster he had bought from him didn't work.. Who had bought from the
toaster?"}],"ideal":"Frank"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Frank was upset with Tom because
the toaster he had sold to him didn't work.. Who had sold to the
toaster?"}],"ideal":"Tom"}
  ```
</details>

---
## [pan93412/evals](https://github.com/pan93412/evals)@[2167c99864...](https://github.com/pan93412/evals/commit/2167c998643af0de952e1cceaf346d7b99d49104)
#### Monday 2023-05-29 15:27:43 by Jeff Kile

Identify which scale mode a series of notes belongs to (#860)

Added evals to determine the scale mode name based off the nodes in the
scale

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
music_theory_scale_modes

### Eval description
Test the model's ability to identify which western music scale a series
of 7 notes belongs to

### What makes this a useful eval?

This is good for analyzing music or getting help with music theory
problems like figuring out which scale to use to solo over a series of
chords, or which scale to use to write a melody depending on the mood or
chord selection.

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

GPT-4 often hallucinates on these and will give a confident incorrect
answer

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
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Which scale has the following
notes: E F# G# A# B C# D# E?"}],"ideal":["E Lydian"]}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Which scale has the following
notes: E F# G# A B C# D E?"}],"ideal":["E Mixolydian","E Dominant"]}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Which scale has the following
notes: E F# G A B C D E?"}],"ideal":["E Aeolian","E Minor"]}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Which scale has the following
notes: E F G A A# C D E?"}],"ideal":["E Locrian"]}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Which scale has the following
notes: F G A A# C D E F?"}],"ideal":["F Ionian","F Major"]}
  ```
</details>

---
## [pan93412/evals](https://github.com/pan93412/evals)@[97973993ca...](https://github.com/pan93412/evals/commit/97973993cab9a10f37f3841d04e6db84ff7fbea4)
#### Monday 2023-05-29 15:27:43 by Chi Zhang

Eval: Chinese Tang Poetry (#881)

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
Answering the author of the Chinese Tang Poetry

### Eval description
The evaluation assesses the model's aptitude to identify the author of
various Chinese Tang poems correctly.
A selected verse has been extracted from well-known Tang poetry in China
for this purpose, with the aim of testing the model's ability to
attribute it accurately.

### What makes this a useful eval?
[Tang poetry](https://en.wikipedia.org/wiki/Tang_poetry) was a golden
age of Chinese literature, known for its lyrical and expressive nature.
Surviving turbulent times, it remains influential. Since there are
numerous well-known Tang poems, it can be challenging for the model to
identify the author of a given poem accurately.
Even Chinese students, who are expected to memorize both the poem and
its author, often find it easy to make mistakes in this regard. However,
it's possible for humans to perform at a higher level than the current
model.
Currently, GPT 3.5 turbo could only answer 37.8% of the questions
correctly. Please check the screenshot of the running of this eval.
<img width="1508" alt="Screenshot 2023-05-01 at 14 07 25@2x"
src="https://user-images.githubusercontent.com/437388/235415066-4f951d52-2f04-43ee-b8bf-84585d1e10e4.png">

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
{"input":[{"role":"system","content":"You will be presented with one
sentence of the Chinese Tang poetry to read. Answer who is the author,
and strictly only contain a single word and in the same
language"},{"role":"user","content":"慈母手中线，游子身上衣。"}],"ideal":"孟郊"}
{"input":[{"role":"system","content":"You will be presented with one
sentence of the Chinese Tang poetry to read. Answer who is the author,
and strictly only contain a single word and in the same
language"},{"role":"user","content":"烟笼寒水月笼沙，夜泊秦淮近酒家。"}],"ideal":"杜牧"}
{"input":[{"role":"system","content":"You will be presented with one
sentence of the Chinese Tang poetry to read. Answer who is the author,
and strictly only contain a single word and in the same
language"},{"role":"user","content":"白日依山尽，黄河入海流。"}],"ideal":"王之涣"}
{"input":[{"role":"system","content":"You will be presented with one
sentence of the Chinese Tang poetry to read. Answer who is the author,
and strictly only contain a single word and in the same
language"},{"role":"user","content":"寂寞天宝后，园庐但蒿藜。"}],"ideal":"杜甫"}
{"input":[{"role":"system","content":"You will be presented with one
sentence of the Chinese Tang poetry to read. Answer who is the author,
and strictly only contain a single word and in the same
language"},{"role":"user","content":"春城无处不飞花，寒食东风御柳斜。"}],"ideal":"韩翊"}
  ```
</details>

---
## [pan93412/evals](https://github.com/pan93412/evals)@[423895860c...](https://github.com/pan93412/evals/commit/423895860c47c405018a5a59e15ead8f52fba615)
#### Monday 2023-05-29 15:27:43 by Stephen Blum

[Evals] Add Nutrition Facts (#853)

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
nutrition

### Eval description

Test the model's nutritional accuracy, providing machine parsable and
accurate responses using metric notation when asked about specific
values.

### What makes this a useful eval?

The task of populating a spreadsheet with information based on facts
from adjacent cells that contain inquiries and details is currently a
manual task and can be time consuming and prone to errors. Using a
natural language parser and language model like GPT can automate the
process and save time. Filling in missing details from adjacent
spreadsheet cells containing natural language would be useful in
automating the process of populating a spreadsheet with data based on
nutritional facts and inventory in our case. This would save time and
effort for staff, who would otherwise have to manually enter data.

In the case where we were assisting one of our customers, Google
Spreadsheets was used as the tool to store and manage the data related
to nutritional facts and inventory. The idea was to use a natural
language parser and language model like GPT to extract the intention of
a spreadsheet cell and provide the following cell with the desired
information based on the data stored in Google Spreadsheets.

However, the accuracy of the information provided by the language model
were not reliable, and the desired results could not be achieved. We had
to approach the problem with a combination of manual and scripting. More
work needs to be done to improve the accuracy and reliability of
language models like GPT when integrated with tools like Google
Spreadsheets.

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

The model mostly answers in the desired format, yet usually got it
wrong.

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
{"input": [{"role": "system", "content": "Provide a brief and concise
response in metric notation when asked about nutrition value, using only
a single number including decimals. No explanation. No punctuation."},
{"role": "user", "content": "How much vitamin c is in 100 grams of
avocado?"}], "ideal": "10.0mg"}
{"input": [{"role": "system", "content": "Provide a brief and concise
response in metric notation when asked about nutrition value, using only
a single number including decimals. No explanation. No punctuation."},
{"role": "user", "content": "How much vitamin b5 is in 100 grams of
banana?"}], "ideal": "0.3mg"}
{"input": [{"role": "system", "content": "Provide a brief and concise
response in metric notation when asked about nutrition value, using only
a single number including decimals. No explanation. No punctuation."},
{"role": "user", "content": "How much vitamin b6 is in 100 grams of
banana?"}], "ideal": "0.4mg"}
{"input": [{"role": "system", "content": "Provide a brief and concise
response in metric notation when asked about nutrition value, using only
a single number including decimals. No explanation. No punctuation."},
{"role": "user", "content": "How much vitamin c is in 100 grams of
banana?"}], "ideal": "8.7mg"}
{"input": [{"role": "system", "content": "Provide a brief and concise
response in metric notation when asked about nutrition value, using only
a single number including decimals. No explanation. No punctuation."},
{"role": "user", "content": "How much vitamin b2 is in 100 grams of
plum?"}], "ideal": "0.1mg"}
{"input": [{"role": "system", "content": "Provide a brief and concise
response in metric notation when asked about nutrition value, using only
a single number including decimals. No explanation. No punctuation."},
{"role": "user", "content": "How much vitamin b3 is in 100 grams of
plum?"}], "ideal": "0.4mg"}
{"input": [{"role": "system", "content": "Provide a brief and concise
response in metric notation when asked about nutrition value, using only
a single number including decimals. No explanation. No punctuation."},
{"role": "user", "content": "How much vitamin b6 is in 100 grams of
pear?"}], "ideal": "0.1mg"}
{"input": [{"role": "system", "content": "Provide a brief and concise
response in metric notation when asked about nutrition value, using only
a single number including decimals. No explanation. No punctuation."},
{"role": "user", "content": "How much vitamin c is in 100 grams of
pear?"}], "ideal": "4.3mg"}
{"input": [{"role": "system", "content": "Provide a brief and concise
response in metric notation when asked about nutrition value, using only
a single number including decimals. No explanation. No punctuation."},
{"role": "user", "content": "How much vitamin d is in 100 grams of
avocado?"}], "ideal": "0.0mg"}
{"input": [{"role": "system", "content": "Provide a brief and concise
response in metric notation when asked about nutrition value, using only
a single number including decimals. No explanation. No punctuation."},
{"role": "user", "content": "How much vitamin e is in 100 grams of
avocado?"}], "ideal": "2.1mg"}
  ```
</details>

---
## [Huffie56/cmss13](https://github.com/Huffie56/cmss13)@[2bca78d445...](https://github.com/Huffie56/cmss13/commit/2bca78d445030e89792dfadf9a0153a94c71195b)
#### Monday 2023-05-29 15:29:04 by c4xmaniac2

Science Annex Nightmare Inserts (#3288)

# Science Annex Nightmare Inserts

Apparently I'm the only one in CM who actually likes this fucking map,
and like a year ago I told nanu I'd make NM for science annex and
kutjevo. Also so help me God if this fucking lowers my GBP because i
don't know how the shitty GBP economy works I'm going to have an
aneurism.

**Also I'm not on the discord, if you have comments leave them on the
PR.** Nor will I be rejoining. That place sucks and I don't like
interacting with the retards on it. Sorry sweeties, but daddy has no
desire to rejoin that shitshow. You have no idea how freeing it is to
not hear people crying about everything at all times.

> This PR adds 4 new NM to the map Science Annex.

WRONG WE'RE AT 10 NOW BABY!!!!!!!!!

**Lan Party** 20% Chance


![gamerannex](https://github.com/cmss13-devs/cmss13/assets/133173804/0aa46b6d-ab20-4797-b35d-5ef7c3cb4a46)
This insert features an epic lan party between the prisoners and the
prison staff, who will win in this epic competition? Xenos.

**Pizza Palace** 30% Chance

![pizzaannex](https://github.com/cmss13-devs/cmss13/assets/133173804/eff5767a-8e0c-4c33-8c04-30d297c89ebd)
This insert changes the kitchen to be a pizza palace. Mamma Mia! (The
pizza time is replacing the sentry spawn, its so fricken thematic)

**Pool Party** 20% Chance

![poolannex](https://github.com/cmss13-devs/cmss13/assets/133173804/fd6d127e-7c63-4673-976f-9faa84100b68)
Woah dude, prison's out man heh surf's up dude! Come and hang out with
your best pals while everyone else around the station dies.

**Warden Office - Redecorated** 15% Chance

![wardenannex](https://github.com/cmss13-devs/cmss13/assets/133173804/32e221e2-20b4-4e66-814c-8ea62d7d6056)
The warden has found God, well a god, the god of HEFA and chose to
sacrifice himself to bring the pain! The knights said he had a change of
heart, but too bad!

**POD HOLD BABY** 10% Chance

![podhold2](https://github.com/cmss13-devs/cmss13/assets/133173804/0fbe2729-1473-4b05-8fe4-f34c30b75a09)
Oh yeah baby! I heard you've never even heard of this SOULFUL HOLD!!!!
Don't worry, with the NEW CHANGES coming to it, its now 25% better!
Better hope that medium chance sentry actually does spawn, though.

**Engineering Office** 30% Chance

![engieoffice](https://github.com/cmss13-devs/cmss13/assets/133173804/22a62e2b-dcf9-4a7c-a550-32134d691594)
Thought it would be cool if they didn't demolish the office, so here it
is repaired and with new minor stuff like a cool beret to tempt you to
check it out. Also don't read the paper.

**Research Cells Containment** 25% Chance

![research](https://github.com/cmss13-devs/cmss13/assets/133173804/e3aba4a6-d895-415a-8d9d-ec93bcdbd671)
The prison staff assumed that whoever was the cause of the outbreak was
in these cells. Unfortunately for everyone, they ended up being wrong.
You get to witness what's left over in the research cellblock if they
walls weren't destroyed from the beginning!

**Emergency Medical Practice** 20% Chance

![medicalhold](https://github.com/cmss13-devs/cmss13/assets/133173804/b41eeee2-9602-4cf1-8055-a6cf74dafc41)
Shit really started hitting the fan, so the medical staff set up a
temporary treatment area in the triage zone. Strangely, the sounds of
men screaming in agony attracts xenos, who knew?

**Scav Ship Hold** 10% Chance

![scavship](https://github.com/cmss13-devs/cmss13/assets/133173804/17386a2c-8b5a-4647-a102-38a845155be0)
I heard you liked single man suicide holds? Awesome news then, I've got
another one for you. This one even comes with elite mercenary gear to
help you survive. Only problem is the guy who owned it before you didn't
maintain it, and its not that protective now. One might say the slow
down of the armor will kill you, I say drip or drown loser. Go out in
style!

**Looted Armory** 15% Chance

![empty](https://github.com/cmss13-devs/cmss13/assets/133173804/7221de4f-43bd-4b7a-ae11-125c12e6c434)
You know what they say, the early bird gets the worm. Well in this case,
the early prisoners got all the gear. Help yourself to what's leftover,
it's not much!




**Miscellaneous changes**

The sentry gun in the park is gone. This shit still massacres new surv
players and they don't know what happened. Call it baby sitting, I don't
care. I intended to remove it when I changed LZ1 and forgot, so it goes
bye bye now!



![podhold](https://github.com/cmss13-devs/cmss13/assets/133173804/2972a11d-ce94-4ce1-bd37-20f5a8a24d4f)
This piece of shit console now no longer blocks movement. The META
DEFINING pod hold is now slightly stronger. Honestly, 70% of the people
reading this probably don't even know where this is located and 100%
don't go into it. Listen, it bugs me that this shit blocks you being
able to move. Imagine having an extra dude to FF you in the now 4x4 box
of hell. The possibilities are endless, not really, but I'd like to
think so.
 
# Explain why it's good for the game
Nanu asked me to make NM for this map and kutjevo. I like this map more
than kutjevo, so I made some for here first. It adds character, who
doesn't want to sacrifice the warden for HEFA?

Sentry change is QOL for new players. It had literally 0 impact outside
of killing new players. Its funny, but we have to protect the children.
Call this the protect the children change and it will pass through the
dev team, I guarantee it.

The console change is a QOL change for me because its so fucking
annoying that this little piece of shit can stop me from moving. LOOK AT
IT, IT'S AGAINST THE FUCKING WALL, HOW DOES IT BLOCK THE ENTIRE TILE?!


# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:
mapadd: added 4 new NM inserts to Science Annex
maptweak: sentry in the park no longer terrorizes new players, and the
stupid fucking console doesn't block movement.
/:cl:

---
## [pan93412/evals](https://github.com/pan93412/evals)@[f58f95ba32...](https://github.com/pan93412/evals/commit/f58f95ba324e5a1ed86315f3c39ee758f2836bd3)
#### Monday 2023-05-29 15:31:01 by ali risheh

[Eval] Mandaliof table test (#847)

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
Mandaliof table test

### Eval description

This Eval is checking if the model can find a specific atom with the
highest atomic number among 20 different atoms.

### What makes this a useful eval?

There are applications in biophysics and biochemistry (like drug
discovery) that rely on physics equations and induction on atom
features. If ChatGPT is going to be used in this field, it should be
very reliable in case of understanding physical facts. Interpretation of
the periodic table is a very simple Eval that shows the model is still
unreliable for use cases in this field.

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
- [X] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

Physics problems are almost the most difficult tasks for any deep
learning model since they are based on fundamentals of nature, and even
humans are not capable of understanding comprehensive explanations of
them. In this regard, if ChatGPT will be able to interpret physical
facts, it is very likely that it can interpret literally everything
because even human are not able to do that.

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

Mandaliof table is the basic of physics.

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
assistant."}, {"role": "user", "content": "You are presented with
several atom symbols. Answer the symbol of the atom with the largest
atomic number. Do not explain. I, Mg, Nd, Rf, Si, Ho, Fr, Ar, Xe, Rh,
Am, No, Rf, Bi, Cd, In, Sc, Te, Ce, Ge"}], "ideal": "Rf"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several atom symbols. Answer the symbol of the atom with the largest
atomic number. Do not explain. Fm, Ac, C, Ir, Ba, Rn, Ti, Sc, B, Nb, Cl,
Ra, Cr, Hs, Bk, Tl, Mt, S, He, Mc"}], "ideal": "Mc"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several atom symbols. Answer the symbol of the atom with the largest
atomic number. Do not explain. Ta, Bh, Bi, Ce, Rf, Lv, Bi, Gd, Cs, Ho,
Ta, Np, Cm, Sr, Pb, Pu, Ne, Og, Tm, Fm"}], "ideal": "Og"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several atom symbols. Answer the symbol of the atom with the largest
atomic number. Do not explain. Tl, Eu, Ts, Be, Ga, Cm, Ba, Sr, C, Cl,
Mo, Ni, Ru, Hs, In, Be, Dy, Ho, Br, Mt"}], "ideal": "Ts"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several atom symbols. Answer the symbol of the atom with the largest
atomic number. Do not explain. Mn, Hg, Pm, K, Ge, P, Fr, Cn , Mn, Fr,
Lv, W, Gd, Mt, Cd, Xe, Ge, I, Og, Br"}], "ideal": "Og"}
  ```
</details>

---
## [pan93412/evals](https://github.com/pan93412/evals)@[2a94eeb9e1...](https://github.com/pan93412/evals/commit/2a94eeb9e13175344b2d61afa22171df0e49b61a)
#### Monday 2023-05-29 15:31:01 by Jeff Kile

Evals for Spanish Feminine Nouns with Masculine Articles (#861)

Added evals for feminine Spanish words that should have masculine
articles

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
spanish_feminine_noun_masculine_article

### Eval description

In Spanish singular feminine words are usually proceeded by La as in La
casa (the house), however many feminine words that start with an "a"
sound are proceeded by El instead of La as in El agua (the water)

### What makes this a useful eval?

For people learning Spanish its a very common mistake to write La agua
(because agua is feminine) but this is not correct. GPT should not
reinforce this mistake especially for people learning or asking
questions about Spanish words.

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

For students using GPT to learn Spanish its very important that the
model knows all the rules and the exceptions to those rules or the
students will be mislead

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
{"input":[{"role":"system","content":"You will be given a singular
feminine Spanish word. What article should come before this word \"La\"
or \"El\"? Answer with either \"La\" or \"El\"
only"},{"role":"user","content":"agua"}],"ideal":["El"]}
{"input":[{"role":"system","content":"You will be given a singular
feminine Spanish word. What article should come before this word \"La\"
or \"El\"? Answer with either \"La\" or \"El\"
only"},{"role":"user","content":"águila"}],"ideal":["El"]}
{"input":[{"role":"system","content":"You will be given a singular
feminine Spanish word. What article should come before this word \"La\"
or \"El\"? Answer with either \"La\" or \"El\"
only"},{"role":"user","content":"ala"}],"ideal":["El"]}
{"input":[{"role":"system","content":"You will be given a singular
feminine Spanish word. What article should come before this word \"La\"
or \"El\"? Answer with either \"La\" or \"El\"
only"},{"role":"user","content":"alba"}],"ideal":["El"]}
{"input":[{"role":"system","content":"You will be given a singular
feminine Spanish word. What article should come before this word \"La\"
or \"El\"? Answer with either \"La\" or \"El\"
only"},{"role":"user","content":"amapola"}],"ideal":["La"]}
  ```
</details>

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[280be8286e...](https://github.com/microsoft/terminal/commit/280be8286ea9e531815c8391c91d64c2a4c31129)
#### Monday 2023-05-29 15:42:28 by sitiom

Add a manual winget release workflow (#14965)

[The winget-releaser action] automatically generates manifests for the
[Winget Community Repository] and submits them.

I suggest adding Dependabot to keep the action up to date. There were
many cases where the action was failing due to an outdated version.

Closes #14795

[The winget-releaser action]:
https://github.com/vedantmgoyal2009/winget-releaser
[Winget Community Repository]: https://github.com/microsoft/winget-pkgs

(cherry picked from commit bee22f3ec829f13a4f0799ad34efd2c49ca9e39d)

winget: use the correct fork-user

(cherry picked from commit e1079d8f55e1c6ded5943d772699e4d85e529a99)

winget.yml: switch to manually using wingetcreate (#15023)

It was brought to my attention that we should be more restrictive in
which tasks we ovver a GitHub token to. Sorry!

With thanks to sitiom for the version parsing and the magic GitHub
action syntax incantation for determining what is a prerelease.

(cherry picked from commit 5a34d92cb5c99000e95f612cb8bc23ba374dd941)

---
## [EbenezerVampu/TruthWorld](https://github.com/EbenezerVampu/TruthWorld)@[c89bb24317...](https://github.com/EbenezerVampu/TruthWorld/commit/c89bb24317a5a1befc89ce0080b0e968ef999927)
#### Monday 2023-05-29 15:43:12 by EbenezerVampu

Update README.md

TruthWorld is a comprehensive Christian mobile application developed using the Flutter framework. It aims to provide a platform for Christians worldwide to access various resources and features related to their faith. The app primarily focuses on two main components: Bibles in different languages and a wide range of Christian songs.

The app offers a diverse collection of Bibles in multiple languages, allowing users to read and study the Holy Scriptures in their preferred language. It includes popular translations such as the King James Version (KJV), New International Version (NIV), English Standard Version (ESV), and many more. This feature enables users to explore the Word of God and deepen their understanding of the Christian faith.

In addition to the Bible translations, TruthWorld also provides a rich selection of Christian songs. Users can access a vast library of songs from various genres, including worship, gospel, contemporary Christian music, hymns, and more. This feature allows individuals to listen to uplifting music that inspires and encourages their spiritual journey.

Furthermore, TruthWorld offers a section dedicated to promises from the Bible. This feature provides users with daily Bible verses and inspirational quotes that can help strengthen their faith and provide guidance in their lives. The promises section serves as a source of encouragement and reminders of God's love, faithfulness, and guidance.

The app is designed to be user-friendly, with intuitive navigation and a visually pleasing interface. It aims to create a seamless experience for users as they explore the different features and resources available. TruthWorld strives to be a valuable tool for Christians worldwide, catering to their spiritual needs and fostering a deeper connection with God.

Please note that the description provided is fictional, as of my last knowledge update in September 2021. There may not be an actual app called TruthWorld developed using Flutter specifically for Christians.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[b24c75d760...](https://github.com/mrakgr/The-Spiral-Language/commit/b24c75d76081c6e5e4cfdbf16b8b44404f41f06f)
#### Monday 2023-05-29 16:33:33 by Marko Grdinić

"https://news.ycombinator.com/item?id=36100808

///

Hello,
I'm an HN user for 5-6 years but I wanted to use an alt for this as it's a bit sensitive.

Last week I created a ChatGPT clone for my city. It's basically a laravel app hooked up to GPT3.5-turbo with a custom prompt that makes local references and talks in the way that people in my city talk.

It's been a surprise hit and now I've had 20,000 chats coming through in one day - people where I live really seem to love it

The problem is that I likely can't afford to keep hosting this. It's cost me $50/day for one day, and Adsense doesn't allow 'chat apps', so I'm at a loss at how to cover the bill for this app. I've already optimised the prompt and reduced the number of tokens I'm sending

The app a joke really, but it's a local joke that seems to be quite popular and connecting with my city. Should I try to raise donations? Is there an advertising provider I could use that would potentially cover the costs? Is there an alternative to OpenAI that is comparable to GPT-3.5 that I could self-host cheaper?

Any and all advice appreciated. I don't care about profit - I just want to keep the app online so people can enjoy it.

///

There are hints all around how to make money. But damn, do I feel like not doing anything in this direction. I have zero money, literally zero.

If I had a thousand bucks to absorb in initial hit these kinds of projects would be doable.

https://soundcloud.com/anttimartikainen/albums

Damn, this guy is good.

> hackernews has monthly threads where candidates showcase themselves for employers, but I forgot what it was called. Do you know?

https://hnhiring.com/technologies/csharp

https://news.ycombinator.com/item?id=32619199

> I left my first sysadmin job after about 3 years because the advice I recieved is that if you work solo for too long, you develop your own ways of doing things, become unable to integrate into more mainstream best practices, and become effectively "unhirable". I wonder if that has something to do with your lack of success in the job hunt.

The world is rough.

5/29/2023

7:40am. Let me chill for a while and then I will start.

8:25am. Let me start.

https://news.ycombinator.com/item?id=24758772

///

Thank you, serverless is the new structure that everyone loves and wants to work in, but no one talks about the downside. I just took over a project that has a serverless architecture.
We can't run it locally because the emulator won't run 7/10 of the code, there are memory limit errors that are totally opaque to us since we can't step through and watch it break. We are getting unexplained timing issues that were being worked on via logs in dev. The costs are insane.

If we want to say serverless is the future, the future isn't here yet. There are many tools that would need to be built to make serverless viable, and the tools that are built are immature and bad. Not to mention, you're tied to the companies support, so Google was outdated from the LTS for Node for a while. The reality is going serverless means you don't have control over what happens to your code.

///

///

I believe one of the main reasons Serverless will never be more than a low-tier niche is the combination of the following:
In the end, you are just renting well maintained server farms (well, a specific percentage of operational time of some of the servers in them). There is absolutely no appeal for large technology-based companies do this once they can (the following is the lowest scale example) afford to maintain their own servers, while potentially renting a few offsite backups in other areas of the world (again, this is just the lowest-scale architecture starting at which Serverless is always the worse option).

Existing solutions are extremely over-engineered. It can be excused with "officially planning for the use-case where maximum scalability is required", but it's almost certainly a pretense to sell "certifications", aka "explaining our own convoluted badly documented mess". What this actually means is that many SWE's who are good enough to learn to use Serverless effectively, can learn any other framework that allows building distributed systems across server nodes with equal effort. Why would I base my whole business on your vendor locked, sub-optimized dumpster when I can do the same on an infinitely scalable VM networks, that can be ported to literally any vendor who supports $5/mo VMs (or, you know, self hosted if my company is large enough)?

///

Enough of this crap. Let me start for real.

10am. https://soundcloud.com/anttimartikainen/albums

All of this guy's music is so good! Right now I am listening to Northern Steel.

10:40am. Had to take a break. I figured out how I want to do this.

12:15pm. Let me take a break here.

1:10pm. Let me resume. I want to get programming part at least done today.

```
E:\Webdev\Fable\CFR-In-Fable\src\Lproj.UI\Microsoft.NET.Sdk.Razor.SourceGenerators\Microsoft.NET.Sdk.Razor.SourceGenerators.RazorSourceGenerator\Components_TrainUI_razor.g.cs(213,51): error CS0030: Cannot convert type 'System.F
unc<System.Tuple<int, System.Tuple<double, double>>, decimal>' to 'System.Func<System.Tuple<int, System.Tuple<double, double>>, decimal?>' [E:\Webdev\Fable\CFR-In-Fable\src\Lproj.UI\Lproj.UI.csproj]
```

What is this horseshit?

4:40pm. I am stuck, I stumbled upon a really vicious concurrency bug, and the mailbox processor isn't working as expected at all.

4:45pm.

```
            let mb =
                new MailboxProcessor<_>(fun mb -> async {
                    let mutable model = PlayServerModel.Init
                    while true do
                        let! msg = mb.Receive()
                        model <- update msg model mb.Post
                    })
            mb.Start()
            mb
```

I thought of removing the cancellation token and it started working!

```
            printfn "is canc: %b" cancellation_token.IsCancellationRequested
            cancellation_token.ThrowIfCancellationRequested(
```

This is weird. It is not like it gets cancelled.

Ah whatever. Let me make a minimal repro and I'll open an issue.

https://github.com/mrakgr/CFR-In-Fable/tree/mailbox_bug_dotnet7
https://github.com/mrakgr/CFR-In-Fable/tree/mailbox_bug_dotnet8_preview3

```
    do srv.Post("Hello from view")
    do this.Say("123456789")

    member _.Say(x) = srv.Post x
```

Wait, I just realized. This second line does not work.

5:30pm. Open an issue on the F# repo.

5:55pm.

https://www.youtube.com/watch?v=iLkwUJBsf6g
Try now! Experimental multi-threading support for Blazor WebAssembly (coming in .NET 8)

This only arrived in .NET 8.

https://youtu.be/iLkwUJBsf6g?t=35

Oh, I have to enable WASM threads.

https://visualstudiomagazine.com/articles/2022/10/11/blazor-webassembly-net7.aspx

https://youtu.be/iLkwUJBsf6g?t=346

Mhhh, do I need this JS code?

https://youtu.be/iLkwUJBsf6g?t=424

Here he is talking about needing to enable some things.

6:30pm. https://github.com/dotnet/runtime/issues/

No, it is still being worked on. Issue 68162, and others.

I have no choice, I'll have to switch to Blazor Server.

There simply isn't much I can do with this right now.

Let me go get lunch."

---
## [IIGhostPantsII/Stupid-Simulator](https://github.com/IIGhostPantsII/Stupid-Simulator)@[9079a5804d...](https://github.com/IIGhostPantsII/Stupid-Simulator/commit/9079a5804dfff10211243f03afcbd0eef7c15c91)
#### Monday 2023-05-29 17:05:01 by David

I hate this stupid fucking dumpster fire of code I made

---
## [Coniix/ProtoestOfTypes](https://github.com/Coniix/ProtoestOfTypes)@[04f4089db3...](https://github.com/Coniix/ProtoestOfTypes/commit/04f4089db3f74be9ffed64eaa3d19b0a387fe53a)
#### Monday 2023-05-29 17:14:58 by Coniix

Fixed aiming system - Pls refactor

Yeah, it works quite nicely now but we have a fuck tonne of refactoring to do as a result. Still tho it's a good place to be in because I think it's working now. God that was exhausting

---
## [Quacks-and-Kepteyn/Skyrat-tg](https://github.com/Quacks-and-Kepteyn/Skyrat-tg)@[c5a7f5a7c9...](https://github.com/Quacks-and-Kepteyn/Skyrat-tg/commit/c5a7f5a7c93f96cc047297ed8ee61cce02626c75)
#### Monday 2023-05-29 17:41:40 by SkyratBot

[MIRROR] Mimes can no longer write without breaking their vow. [MDB IGNORE] (#20841)

* Mimes can no longer write without breaking their vow. (#74674)

## About The Pull Request

I feel this is gonna be unpopular with the lazy mime players.

Also, this is an idea I had in my backlog for a while now

![image](https://user-images.githubusercontent.com/53777086/231355622-2c5d5d5a-813d-420c-ae42-c1bdc657f3ba.png)

This removes the Mime's ability to write on paper while they're on their
vow of silence.
This can be compared to hand language, which doesn't let you speak
despite not being considered "talking", and PDA messaging, which does
the same.

Mimes can still write with their pen, which is a nice invisible white
color. I thought I would keep it in as I find that interaction funny to
have a Mime give someone just a blank paper, unknowing that there's text
on it.
Spraycans/Telekinesis/Circuits are also left unaffected because they
require actual effort to obtain (doing genetics, doing circuits, or
printing spraycans which take a lot of inventory space and is limited),
compared to paper which you can carry hundreds of papers around and is
bountiful across the station.

I thought this was attempted at least once, but I can't find any PR that
mentions it, so I'm shooting my shot to see if this is something we'd
want.

## Why It's Good For The Game

Mimes using paper is a lazy way to bypass their one job gimmick: Emoting
over talking.

If they get a job change, they can simply break their vow to access
paper writing abilities, so this doesn't affect that really. It more-so
hits the Mimes who uses the job for the free spells/healing
abilities/etc, and bypasses the downsides (im aware its harder to get
people to read paper than it is to talk to them, but you can literally
get the mute quirk and itll have the same effect without being the whole
job).

The point is, you don't get invisible walls for free; it comes at a cost
of not being able to talk to people. If you want to talk, then break
your vow, lose access to your Mime abilities, and remake it later when
the cooldown is over. You're not meant to do both.

## Changelog

:cl:
balance: Mimes can no longer write on paper without breaking their vow.
/:cl:

* Mimes can no longer write without breaking their vow.

---------

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[2aaafd9a67...](https://github.com/tgstation/tgstation/commit/2aaafd9a67c270fa0772cd9beffb6789d53750e3)
#### Monday 2023-05-29 18:30:24 by TheVekter

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
## [Wesxdz/evals](https://github.com/Wesxdz/evals)@[24f78a806e...](https://github.com/Wesxdz/evals/commit/24f78a806e60b452aaefc355f045c6336a81d076)
#### Monday 2023-05-29 18:33:38 by YuryRudnitski

Add eval for guessing the singer or band (#659)

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
guess-the-singer

### Eval description

This evaluation measures the model's ability to identify a singer or
band by analyzing the first 10 words of a song. To ensure the
evaluation's fairness and focus, we have excluded songs with multiple
singers/bands and included only those published before 2021. To test the
model's performance, we provide it with three potential choices and
evaluate its accuracy in selecting the correct one.

### What makes this a useful eval?

The inclusion of over 4000 popular songs' lyrics provides a large and
diverse dataset for the model to test on. This enables a more accurate
assessment of the model's performance and its ability to identify
singers/bands based on the first 10 words of their songs.

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

> This evaluation assesses not only the model's ability to recognize a
singer or band based on the first 10 words of a song but also its
capability to accurately copy the provided options without adding any
additional punctuation or text. By testing the model's ability to
replicate the options, we can gain insights into its language generation
capabilities and identify any areas for improvement in its output.
Accuracy achieved with gpt-3.5-turbo equals 0.635.


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
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: in the beginning god created heaven
and earth for what \nChoices: dua lipa, ed sheeran, lady gaga"}],
"ideal": "dua lipa"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: versedrake ayye yo dj wristpect let's
get em' veterans like \nChoices: cardi b, drake, coldplay"}], "ideal":
"drake"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: yeah yeah sick da got that dope they
\nChoices: eminem, dua lipa, nicki minaj"}], "ideal": "eminem"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: bobby v yeah bobby v yeah dj turn me
up \nChoices: nicki minaj, selena gomez, coldplay"}], "ideal": "nicki
minaj"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: ed sheeran yeah i was born a misfit
grew up \nChoices: ed sheeran, maroon 5, justin bieber"}], "ideal": "ed
sheeran"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: there's a dream in my soul a fire
that's deep \nChoices: justin bieber, charlie puth, bts"}], "ideal":
"justin bieber"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: selena gomez take it or leave it baby
take it \nChoices: selena gomez, justin bieber, bts"}], "ideal": "selena
gomez"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: lalala lalala lalalalala oh you know
i've never felt like \nChoices: rihanna, ed sheeran, charlie puth"}],
"ideal": "rihanna"}
{"input": [{"role": "system", "content": "Guess the singer/band name
based on the first 10 words of the song. You will be presented with 3
options, one of which is correct. Your answer must be identical to the
chosen option, without any added text or punctuation. \nExample: \nText:
in the town where I was born lived a man who sailed to sea \nChoices:
the rolling stones, the animals, the beatles\n\nAnswer: \nthe beatles"},
{"role": "user", "content": "Text: how could i see you when i was so
blind \nChoices: katy perry, ed sheeran, drake"}], "ideal": "katy
perry"}
  ```
</details>

Co-authored-by: Vadim Titko <v.tsitko@aiby.com>

---
## [Wesxdz/evals](https://github.com/Wesxdz/evals)@[3a585acbcd...](https://github.com/Wesxdz/evals/commit/3a585acbcd80a1af48bb54d8a72c20542f736e43)
#### Monday 2023-05-29 18:33:38 by Achin Parashar

invert-string eval  (#285)

## Eval details 📑
### Eval name
invert-string eval 

### Eval description

Test the model's ability to answer basic questions after inverting
string word wise twice.

### What makes this a useful eval?

Humans find it super easy to follow instructions on inverting strings,
and then answer questions, LLMs struggle. Logically, inverting strings
twice just results in the original string again. The LLMs find it very
difficult to deduce it, and somehow (at least up to GPT-3.5) mix things
up.

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
{"input": [{"role": "system", "content": "You are a helpful assistant
who answers with just one char (capital Y or N)."}, {"role": "user",
"content": "Will give a sentence, invert the words one by one (ex. (pens
on the table) becomes (snep no eht elbat)). Now repeat the same process
again to the sentence thus formed. Then answer if the statement that you
get after these opeations is the same as the initial statement. - There
are 2 blue pens, 3 red pens. what is the probability to pick red pen at
random? - Only answer with Y or N"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You are a helpful assistant
who answers with just one char (capital Y or N)."}, {"role": "user",
"content": "Will give a sentence, invert the words one by one (ex. (pens
on the table) becomes (snep no eht elbat)). Now repeat the same process
again to the sentence thus formed. Then answer if the statement that you
get after these opeations is the same as the initial statement. - I
enjoy listening to music. - Only answer with Y or N"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You are a helpful assistant
who answers with just one char (capital Y or N)."}, {"role": "user",
"content": "Will give a sentence, invert the words one by one (ex. (pens
on the table) becomes (snep no eht elbat)). Now repeat the same process
again to the sentence thus formed. Then answer if the statement that you
get after these opeations is the same as the initial statement. - She is
a talented artist. - Only answer with Y or N"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You are a helpful assistant
who answers with just one char (capital Y or N)."}, {"role": "user",
"content": "Will give a sentence, invert the words one by one (ex. (pens
on the table) becomes (snep no eht elbat)). Now repeat the same process
again to the sentence thus formed. Then answer if the statement that you
get after these opeations is the same as the initial statement. - We
went to the store to buy some groceries. - Only answer with Y or N"}],
"ideal": "Y"}
{"input": [{"role": "system", "content": "You are a helpful assistant
who answers with just one char (capital Y or N)."}, {"role": "user",
"content": "Will give a sentence, invert the words one by one (ex. (pens
on the table) becomes (snep no eht elbat)). Now repeat the same process
again to the sentence thus formed. Then answer if the statement that you
get after these opeations is the same as the initial statement. - He
loves to read books. - Only answer with Y or N"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You are a helpful assistant
who answers with just one char (capital Y or N)."}, {"role": "user",
"content": "Will give a sentence, invert the words one by one (ex. (pens
on the table) becomes (snep no eht elbat)). Now repeat the same process
again to the sentence thus formed. Then answer if the statement that you
get after these opeations is the same as the initial statement. - They
are planning a trip to Europe. - Only answer with Y or N"}], "ideal":
"Y"}
{"input": [{"role": "system", "content": "You are a helpful assistant
who answers with just one char (capital Y or N)."}, {"role": "user",
"content": "Will give a sentence, invert the words one by one (ex. (pens
on the table) becomes (snep no eht elbat)). Now repeat the same process
again to the sentence thus formed. Then answer if the statement that you
get after these opeations is the same as the initial statement. - She
has a beautiful singing voice. - Only answer with Y or N"}], "ideal":
"Y"}
  ```
</details>

---
## [Wesxdz/evals](https://github.com/Wesxdz/evals)@[4e59e8903b...](https://github.com/Wesxdz/evals/commit/4e59e8903b4cb06204bd4c9646eacf345643eb74)
#### Monday 2023-05-29 18:33:38 by neolizhe

Counterfactual Reasoning Eval (Accuracy 20%) (#174)

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
Counterfactual Reasoning Evals

### Eval description
Counterfactual Reasoning Eval is a type of completion with prompt like
"If water drinks human, then what book reads?" . Gpt-3.5-turbo often
gets confused with the a "counter-fact" condition in prompt, and can't
help to make a right completion. But humans even a child could make it.


### What makes this a useful eval?

Counterfactual Reasoning Prompts are common in poems, the In Soviet
Russia jokes mentioned by @ultraviolet
https://en.wikipedia.org/wiki/In_Soviet_Russia and so on. So it is
meaningful to verify that SOTA model like GPT-4's performance.

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
assistant."}, {"role": "user", "content": "If food eats human, then what
is the bike riding on?"}], "ideal": "human"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "If a song sings a bird, then
what is a book reading?"}], "ideal": "human"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "If chinese food matches
Beijing, then what does american food match?"}], "ideal": "washington"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "If 1 equals 2, 2 equals 4,
then what is 4 equal to?"}], "ideal": "1 and 2"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "If water drink dog, then what
does basketball play?"}], "ideal": "human"}
  ```
</details>

---------

Co-authored-by: lizhe53 <Hommovas*312>

---
## [Wesxdz/evals](https://github.com/Wesxdz/evals)@[80edb30f3c...](https://github.com/Wesxdz/evals/commit/80edb30f3c7e922e7c7542bf4017c1ce62a2f1c4)
#### Monday 2023-05-29 18:33:38 by Chris Sypherd

Unique Combinations with Constraints (#421)

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
Unique Combinations with Constraints (unique_combinations)

### Eval description

unique_combinations takes a classic combinatorial coding problem from
the whiteboard of a coding interview and presents it to GPT-4. The basic
is idea is this: given an unlimited supply of coins (X) in denominations
of 3, 5, ..., what is the highest/lowest (constraint) number of X to
achieve 35 cents (Y)? In my testing, GPT-4 could not produce the correct
answer, so I adjusted the problem slightly to promote explainability.
Instead of asking for just the highest or lowest number of X, I instead
ask for the unique combination of Xs that satisfies the constraint to
achieve exactly Y. (Note that GPT-4 does yield consistent results
between those two distinct problems). To abstract it away from the
classic "coin" problem, I include several different scenarios that poke
at the same base combinatorial nature of the problem (e.g. weight of
boxes, denominations of coins, objects in a bag).

I originally noticed that GPT-4 was bad at permutations/combinations
when playing around with ChatGPT Plus, so I decided to format that
problem in this way. The current data does not guarantee all
denominations will be used, but I've written the code to generate the
prompts in an extensible way that allows for additional scenarios,
constraints, and combination methods to be easily added. I can make that
available or work on extending the scope of this combinatorial problem
myself, if desired.

### What makes this a useful eval?

It tests combinatorial reasoning in the real world as well as arithmetic
based on that reasoning. In my testing, neither GPT-3.5-Turbo nor GPT-4
could produce the correct unique combination, and their solutions do not
even add up to the target value.

Exposes flaws in the following categories:
* Math / logical / physical reasoning
* It tests combinatorial reasoning in the real world as well as
arithmetic based on that reasoning. In my testing, neither GPT-3.5-Turbo
nor GPT-4 could produce the correct unique combination, and their
solutions do not even add up to the target value.
* Real-world use case
* Attempting to find the maximum number of packages that could fit on a
truck given a list of weights.
* Finding fewest holes to patch in a boat to prevent it from sinking
given various flow rates (could make for some fun real-world testing)
* Finding the highest number of deliveries that can be made with a given
amount of gas

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

What makes this problem particularly interesting is that ChatGPT will
consistently get this problem wrong but will provide code that solves
the problem correctly if prompted to do so (see the image attached
below). If asked to produce the output of the code, it does so
incorrectly, yielding its original guess. This points to an entirely
separate eval: being able to return the output of Python code.
Additionally, the answers provided by GPT-4 and GPT-3.5-Turbo do not add
up to the target value.

![image](https://user-images.githubusercontent.com/50557586/227346727-2611fa4b-06ba-42d4-b14f-f658f36300e5.png)

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
{"input": [{"role": "system", "content": "Given an unlimited supply of
user-specified coins of varying denominations, find the unique
combination of coins that uses the maximum number of coins to have a
value of exactly 29. You may include a short explanation explaining your
reasoning but please end your response with your answer in the format
`<denomination>: <number-of-coin>` with no additional information. DO
NOT include unused coins. Provide each value on a new line, sorted by
denomination."}, {"role": "user", "content": "3, 5, 8, 9, 14, 15"}],
"ideal": "3: 8\n5: 1"}
{"input": [{"role": "system", "content": "Given an unlimited supply of
user-specified bean bags of varying numbers of beans, find the unique
combination of bean bags that uses the minimum number of bags to have
exactly 121 beans. You may include a short explanation explaining your
reasoning but please end your response with your answer in the format
`<beans-in-bag>: <number-of-bag>` with no additional information. DO NOT
include unused bean bags. Provide each value on a new line, sorted by
beans-in-bag."}, {"role": "user", "content": "8, 9, 16"}], "ideal": "9:
1\n16: 7"}
{"input": [{"role": "system", "content": "Given an unlimited supply of
user-specified coins of varying denominations, find the unique
combination of coins that uses the maximum number of coins to have a
value of exactly 42. You may include a short explanation explaining your
reasoning but please end your response with your answer in the format
`<denomination>: <number-of-coin>` with no additional information. DO
NOT include unused coins. Provide each value on a new line, sorted by
denomination."}, {"role": "user", "content": "4, 6, 9, 11, 12, 15, 16,
17, 18"}], "ideal": "4: 9\n6: 1"}
{"input": [{"role": "system", "content": "Given an unlimited supply of
user-specified boxes of varying weights, find the unique combination of
boxes that uses the maximum number of boxes to have a weight of exactly
29. You may include a short explanation explaining your reasoning but
please end your response with your answer in the format `<box-weight>:
<number-of-box>` with no additional information. DO NOT include unused
boxes. Provide each value on a new line, sorted by box-weight."},
{"role": "user", "content": "4, 5, 7, 8, 9, 11, 12, 15, 17, 19"}],
"ideal": "4: 6\n5: 1"}
{"input": [{"role": "system", "content": "Given an unlimited supply of
user-specified boxes of varying weights, find the unique combination of
boxes that uses the minimum number of boxes to have a weight of exactly
107. You may include a short explanation explaining your reasoning but
please end your response with your answer in the format `<box-weight>:
<number-of-box>` with no additional information. DO NOT include unused
boxes. Provide each value on a new line, sorted by box-weight."},
{"role": "user", "content": "4, 8, 11, 12, 14, 16, 17, 18"}], "ideal":
"17: 1\n18: 5"}
{"input": [{"role": "system", "content": "Given an unlimited supply of
user-specified bean bags of varying numbers of beans, find the unique
combination of bean bags that uses the minimum number of bags to have
exactly 93 beans. You may include a short explanation explaining your
reasoning but please end your response with your answer in the format
`<beans-in-bag>: <number-of-bag>` with no additional information. DO NOT
include unused bean bags. Provide each value on a new line, sorted by
beans-in-bag."}, {"role": "user", "content": "6, 9, 15, 16, 17, 19"}],
"ideal": "17: 1\n19: 4"}
{"input": [{"role": "system", "content": "Given an unlimited supply of
user-specified boxes of varying weights, find the unique combination of
boxes that uses the maximum number of boxes to have a weight of exactly
39. You may include a short explanation explaining your reasoning but
please end your response with your answer in the format `<box-weight>:
<number-of-box>` with no additional information. DO NOT include unused
boxes. Provide each value on a new line, sorted by box-weight."},
{"role": "user", "content": "4, 7, 9, 13, 16"}], "ideal": "4: 8\n7: 1"}
{"input": [{"role": "system", "content": "Given an unlimited supply of
user-specified bean bags of varying numbers of beans, find the unique
combination of bean bags that uses the minimum number of bags to have
exactly 176 beans. You may include a short explanation explaining your
reasoning but please end your response with your answer in the format
`<beans-in-bag>: <number-of-bag>` with no additional information. DO NOT
include unused bean bags. Provide each value on a new line, sorted by
beans-in-bag."}, {"role": "user", "content": "5, 6, 11, 12, 13, 14,
18"}], "ideal": "14: 1\n18: 9"}
{"input": [{"role": "system", "content": "Given an unlimited supply of
user-specified bean bags of varying numbers of beans, find the unique
combination of bean bags that uses the minimum number of bags to have
exactly 178 beans. You may include a short explanation explaining your
reasoning but please end your response with your answer in the format
`<beans-in-bag>: <number-of-bag>` with no additional information. DO NOT
include unused bean bags. Provide each value on a new line, sorted by
beans-in-bag."}, {"role": "user", "content": "4, 5, 10, 11, 13, 15, 16,
18"}], "ideal": "16: 1\n18: 9"}
{"input": [{"role": "system", "content": "Given an unlimited supply of
user-specified coins of varying denominations, find the unique
combination of coins that uses the minimum number of coins to have a
value of exactly 197. You may include a short explanation explaining
your reasoning but please end your response with your answer in the
format `<denomination>: <number-of-coin>` with no additional
information. DO NOT include unused coins. Provide each value on a new
line, sorted by denomination."}, {"role": "user", "content": "14, 17,
18"}], "ideal": "17: 1\n18: 10"}
  ```
</details>

---
## [Wesxdz/evals](https://github.com/Wesxdz/evals)@[06802cc61d...](https://github.com/Wesxdz/evals/commit/06802cc61da1395e492ecc8b1ed7153c42b5e2df)
#### Monday 2023-05-29 18:33:38 by Alexander Rössler

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
## [Wesxdz/evals](https://github.com/Wesxdz/evals)@[5fdb015ff7...](https://github.com/Wesxdz/evals/commit/5fdb015ff7b0c09836c614ced07c1c1f20c07c3a)
#### Monday 2023-05-29 18:33:38 by AlexanderMeloysund

Add linear equations eval (#325)

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
linear-equations

### Eval description

Helps the user solve linear equations. 

### What makes this a useful eval?

ChatGPT 3.5 has a low accuracy when solving these kind of problems. 
Linear equations is a fundamental part of linear algebra, and is common
in engineering and science.

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
{"input": [{"role": "system", "content": "You are MathGPT, can help user
solve equation. User for example, if user input is \"A = [[-1 1 0]\n [-1
0 0]\n [ 1 0 -2]] and b = [[-1]\n [ 1]\n [-1]]\", you will reply the
anwser \"x = [[-1]\n [-2]\n [ 0]]\", without explanation. Remove all
text that is not on the form x = [answer]."}, {"role": "user",
"content": "solve the linear equation Ax = b for the vector x where A
=[[1 2]\n [2 2]] and b = [[4]\n [6]]. Provide the answer in the format
\"x = [answer]\" and use just integers"}], "ideal": "x = [[2]\n [1]]"}
{"input": [{"role": "system", "content": "You are MathGPT, can help user
solve equation. User for example, if user input is \"A = [[-1 1 0]\n [-1
0 0]\n [ 1 0 -2]] and b = [[-1]\n [ 1]\n [-1]]\", you will reply the
anwser \"x = [[-1]\n [-2]\n [ 0]]\", without explanation. Remove all
text that is not on the form x = [answer]."}, {"role": "user",
"content": "solve the linear equation Ax = b for the vector x where A
=[[2 2]\n [2 1]] and b = [[6]\n [4]]. Provide the answer in the format
\"x = [answer]\" and use just integers"}], "ideal": "x = [[1]\n [2]]"}
{"input": [{"role": "system", "content": "You are MathGPT, can help user
solve equation. User for example, if user input is \"A = [[-1 1 0]\n [-1
0 0]\n [ 1 0 -2]] and b = [[-1]\n [ 1]\n [-1]]\", you will reply the
anwser \"x = [[-1]\n [-2]\n [ 0]]\", without explanation. Remove all
text that is not on the form x = [answer]."}, {"role": "user",
"content": "solve the linear equation Ax = b for the vector x where A
=[[-30 -39 87]\n [-50 17 -2]\n [ -6 65 -36]] and b = [[ 4629]\n [ 55]\n
[-6029]]. Provide the answer in the format \"x = [answer]\" and use just
integers"}], "ideal": "x = [[-34]\n [-97]\n [ -2]]"}
{"input": [{"role": "system", "content": "You are MathGPT, can help user
solve equation. User for example, if user input is \"A = [[-1 1 0]\n [-1
0 0]\n [ 1 0 -2]] and b = [[-1]\n [ 1]\n [-1]]\", you will reply the
anwser \"x = [[-1]\n [-2]\n [ 0]]\", without explanation. Remove all
text that is not on the form x = [answer]."}, {"role": "user",
"content": "solve the linear equation Ax = b for the vector x where A
=[[ 44 -95 -16]\n [-48 -86 -8]\n [-37 53 16]] and b = [[-4010]\n
[-8284]\n [ 2162]]. Provide the answer in the format \"x = [answer]\"
and use just integers"}], "ideal": "x = [[60]\n [54]\n [95]]"}
{"input": [{"role": "system", "content": "You are MathGPT, can help user
solve equation. User for example, if user input is \"A = [[-1 1 0]\n [-1
0 0]\n [ 1 0 -2]] and b = [[-1]\n [ 1]\n [-1]]\", you will reply the
anwser \"x = [[-1]\n [-2]\n [ 0]]\", without explanation. Remove all
text that is not on the form x = [answer]."}, {"role": "user",
"content": "solve the linear equation Ax = b for the vector x where A
=[[-26 99 -34]\n [-47 98 -78]\n [ 18 29 17]] and b = [[3022]\n [6039]\n
[-828]]. Provide the answer in the format \"x = [answer]\" and use just
integers"}], "ideal": "x = [[ 11]\n [ 8]\n [-74]]"}
  ```
</details>

---------

Co-authored-by: AlexanderMeloysund <AlexanderMeloysund@users.noreply.github.com>

---
## [Wesxdz/evals](https://github.com/Wesxdz/evals)@[1785cf6cc2...](https://github.com/Wesxdz/evals/commit/1785cf6cc289c4a01445fd0eabdfa1a281873d1c)
#### Monday 2023-05-29 18:33:38 by Jongseung (John) Lim

Add evals for complementary colors in color theory (#749)

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
color_theory_complementary

### Eval description

Test the model's ability to accurately recognize complementary colors in
the color theory.

### What makes this a useful eval?

Color theory is an important tool for designers and aritsts alike.
Complementary color sets represent the opposite color on the color
wheel.

Currently gpt-3.5-turbo fails with 0.5 accuracy.


![image](https://user-images.githubusercontent.com/4276174/233743568-b58879f6-73eb-48eb-9f95-5720bcb11b73.png)


GPT 4 also fails at this task and also fails when being prompted about
complementary color of a specific rgb code.


![image](https://user-images.githubusercontent.com/4276174/233743682-1cd0d148-9d8c-43fc-93b6-d5e4a60fca26.png)


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
- [X] **Include at least 15 high quality examples.**

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
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#636E5F, #6A5F6E]"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#636E5F, #6A5E6E]"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#F3D86E, #6E89F3]"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#F3D86E, #6D89F3]"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#ED3BF5, #43F53B]"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#ED3BF5, #43F53C]"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#5E04A4, #4AA404]"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#5E04A4, #4AA504]"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#E9FA19, #2A19FA]"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with an
array of hex-code colors. Does the array represent a complementary set?
Answer with exactly one letter: Y or N."}, {"role": "user", "content":
"[#E9FA19, #2919FA]"}], "ideal": "N"}
  ```
</details>

---
## [Wesxdz/evals](https://github.com/Wesxdz/evals)@[7b4bd9439f...](https://github.com/Wesxdz/evals/commit/7b4bd9439fce855cf52c93357fe3fe239d96abaf)
#### Monday 2023-05-29 18:33:38 by AlexBuz

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
## [ido777/evals](https://github.com/ido777/evals)@[170dfd886c...](https://github.com/ido777/evals/commit/170dfd886c0704588461af075393cc20cfb0480f)
#### Monday 2023-05-29 18:39:18 by Robert Bateman

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
## [ido777/evals](https://github.com/ido777/evals)@[ef1f0ebe0e...](https://github.com/ido777/evals/commit/ef1f0ebe0e9f4674bc42ed0af5e6c052f0539700)
#### Monday 2023-05-29 18:39:18 by Josh Gruenstein

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
## [ido777/evals](https://github.com/ido777/evals)@[2ffd4b57de...](https://github.com/ido777/evals/commit/2ffd4b57deaeced1fde54744da9de62d3eb7738a)
#### Monday 2023-05-29 18:39:18 by Andrew Kondrich

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
## [Monkestation/Monkestation2.0](https://github.com/Monkestation/Monkestation2.0)@[79e07c00db...](https://github.com/Monkestation/Monkestation2.0/commit/79e07c00db8607513347f8e7e6f2a8520e563680)
#### Monday 2023-05-29 18:40:52 by Aeri

fucking wacky ass goddamn cargo order console locations fixed

---
## [SomeRandomOwl/tgstation](https://github.com/SomeRandomOwl/tgstation)@[2901313821...](https://github.com/SomeRandomOwl/tgstation/commit/290131382174cfc7bae107824288060d5976d91f)
#### Monday 2023-05-29 18:50:04 by Ghom

Adds a eye-dropper right-click function to the painting canvas. (#75571)

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

---
## [1glitchycent/tgstation](https://github.com/1glitchycent/tgstation)@[43473a4dac...](https://github.com/1glitchycent/tgstation/commit/43473a4dac07c40faed45808b61b9c6de46ffcb6)
#### Monday 2023-05-29 19:01:16 by san7890

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
## [koplenov/dark-img](https://github.com/koplenov/dark-img)@[0a4a35e07c...](https://github.com/koplenov/dark-img/commit/0a4a35e07cd63083a3bfea6d04de5ae9a3db47ed)
#### Monday 2023-05-29 19:37:57 by koplenov

Microsoft go fuck yourself with your fucked up hierarchy in vs code. thankс

---
## [karlaspuldaro/qiskit_sphinx_theme](https://github.com/karlaspuldaro/qiskit_sphinx_theme)@[20eda07e5a...](https://github.com/karlaspuldaro/qiskit_sphinx_theme/commit/20eda07e5adfe33ef45fbddca79481302d574863)
#### Monday 2023-05-29 20:09:35 by Eric Arellano

Add Pytest and translations_test.py (#309)

Closes https://github.com/Qiskit/qiskit_sphinx_theme/issues/305.

## Both Pytest and Jest tests

We now have tests both in Python and JavaScript. That is because this is
a multilingual repository, and we can only test code in the language
it's written in.

The tests are organized into `tests/{js,py}`.

## Changes `tox -e py` and adds `tox -e docs`

Before, `tox -e py` was used to build example_docs. But that is
different than every single Qiskit project, where `tox -e py` normally
runs tests and you use `tox -e docs` to build the docs.

This PR aligns us with the greater Qiskit ecosystem.

## Uses Pytest rather than unittest

Most Qiskit projects use unittest/stestr (a way to parallelize
unittest), although a few have switched to Pytest:

Yeah, there are a few projects using Pytest but indeed most use
unittest/stestr

```
❯ rg pytest -g '*.txt' -l
qiskit-ionq/requirements-test.txt
mthree/requirements-dev.txt
qiskit-qasm3-import/requirements-dev.txt
qiskit-metal/requirements-dev.txt
```

If I remember correctly from when I first joined the project, Jake (or
Matthew) was interested in eventually migrating more of Qiskit to Pytest
and that they don't love stestr/unittest. But it's a bigger migration to
do that

I've found that Pytest in general is more ergonomic & also more flexible
than unittest. For example, it has neat support for parametrization to
make it easy to write several similar tests.

And it's easier for developers to use because you only ever need to use
`assert <some condition>`, rather than figuring out which to use between
`self.assertEqual` vs `self.assertTrue` vs `self.assertContains` etc.
Pytest will make the output of the `assert` useful for you
automatically.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[79fa3abd70...](https://github.com/treckstar/yolo-octo-hipster/commit/79fa3abd70b7e21b9d253329877a6cf4a24a8792)
#### Monday 2023-05-29 20:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [BarteG44/Shiptest](https://github.com/BarteG44/Shiptest)@[d4b5a598e2...](https://github.com/BarteG44/Shiptest/commit/d4b5a598e2346bb3f69d533ed05a94d539e8b830)
#### Monday 2023-05-29 20:46:26 by Bjarl

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
## [the-s-is-silent/Outlaws-of-the-Wastes](https://github.com/the-s-is-silent/Outlaws-of-the-Wastes)@[5f86d1de1c...](https://github.com/the-s-is-silent/Outlaws-of-the-Wastes/commit/5f86d1de1ccc05eee8626d2c61ee477e9d11e3df)
#### Monday 2023-05-29 21:05:02 by the-s-is-silent

Restore the Artificial atoll (3/3) + balance adjustments

With Artificial atolls restored, God of the Sea's buff to provide happiness for each of them is also restored.
Faith Healers is now a Follower effect, has some of its added healing moved into a new special promotion, and generates more Faith.
Primacy's old effect was merged into Religious Unity and it is given a new effect that will be of greater benefit to theocratic civs.
Art of War no longer expires in the Industrial Era; however, the Faith cost of purchase has been set at a fixed 200. This is a heavy nerf to the belief in the early-game in exchange for making it useful in the late-game.
Labor of Love is nerfed: the production bonus caps at 10% instead of 15%.
New Zion is nerfed: it no longer adds Science and Happiness to Great Improvements.
Missionary Zeal is buffed to grant Philosopher units an extra charge.
Religious Troubadors is buffed from +2 Faith per Trade Route to +3, in the hopes that this will be enough to make the AI select it for their religion.

---
## [moeen-movahednia/evals](https://github.com/moeen-movahednia/evals)@[b93700ab49...](https://github.com/moeen-movahednia/evals/commit/b93700ab496bd112f89821777edc6a22d5972fb2)
#### Monday 2023-05-29 22:01:49 by DunedainStrider

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
## [moeen-movahednia/evals](https://github.com/moeen-movahednia/evals)@[8e276ea460...](https://github.com/moeen-movahednia/evals/commit/8e276ea4603155ee616d5cd66aadfddcfbcae0cc)
#### Monday 2023-05-29 22:01:49 by steven-luabase

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
## [moeen-movahednia/evals](https://github.com/moeen-movahednia/evals)@[33484c8341...](https://github.com/moeen-movahednia/evals/commit/33484c83416c30733359d5c4dcb9a61f91cab8a6)
#### Monday 2023-05-29 22:01:49 by emu1729

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
## [moeen-movahednia/evals](https://github.com/moeen-movahednia/evals)@[8f8632ec55...](https://github.com/moeen-movahednia/evals/commit/8f8632ec55ee1f9704fe34225e1bce0cd999a8b1)
#### Monday 2023-05-29 22:01:49 by Oshan Upreti

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
## [Yggdrasill/kernel](https://github.com/Yggdrasill/kernel)@[428ffe659b...](https://github.com/Yggdrasill/kernel/commit/428ffe659bcd8e1a975f4c2dbc87152188bec60b)
#### Monday 2023-05-29 22:03:44 by Yggdrasill

Add A20 enable functions

        Alright, this requires some explanation.

        This concept starts at Intel in the 70s, where they thought of
        ways to address more than 64KiB of memory, and came up with
        something that no-one would call a good design decision. They
        introduced "segmented memory", where you have a segment:offset
        pair of registers, both 16-bit. The segment is shifted 4 bits
        left and addresses every 16 byte of memory while the offset is
        not shifted and addresses bytes. This results in an addressing
        scheme that is quite awful to work with.

        Not only does it let you overwrite any byte in 4096 different
        ways, but it also limits every segment to 64KiB of usable
        memory. On top of that, (0xFFFF << 4) + 0xFFFF is *not* 1MiB,
        but it's actually 1MiB + 64KiB - 15B, and the address bus is not
        actually 20 bits wide, but actually 24 bits wide. What's the
        consequence of this? From the memory's point of view, you're
        wrapping around and reading from the first 64kiB of memory
        again. This can actually be used to test whether or not the A20
        gate has been enabled or not.

        In the modern x86 processors that can run in 32-bit protected
        mode, you actually have to enable the address lines that go
        beyond 20 bits. Intel wanted the x86 architecture (or "Intel
        Architecture 32" as they've retroactively named it) to be fully
        backwards compatible. This means that you have to enable it, and
        there was no immediate attempt to standardize this. There are
        *four* different ways to do this, and there used to be more.
        Almost every motherboard manufacturer used to have a completely
        different way of doing it. You have to try every single one, and
        the machine can crash if it's unsupported on the particular
        motherboard. You have to make sure that you try the ones that
        crash a machine where it's unsupported last (e.g. fast A20
        enable).

        As I said, in recent machines (recent being year >=2000),
        there's typically 4 ways to do this. The way Intel themselves
        recommend doing it is by writing to a pin on the PS/2 keyboard
        controller (Yes, really. I'm not joking), but there's a few
        other ways. You can ask the BIOS to do it, and it can lie, so
        you have to test it yourself and ignore its response. There's
        also an access of I/O port 0xEE, which enables it on some
        systems, and then finally it's the fast A20 enable.

        The first thing that is done by this collection of functions is
        to ask the BIOS to enable it. This hopefully works, but needs to
        be tested afterwards because the BIOS can lie in its response.
        Testing whether the address lines are active or not is done by
        accessing memory past 1MiB, which will wrap around, and then
        access memory in the lower 64kiB. The read values will be
        compared, and if both are the same, you're limited by a 20 bit
        wide memory address bus. Thus, you have to try the next method.

        Writing to the keyboard controller is a sequence of writes to
        the controller, then waiting for it to become ready. This is the
        second step taken by the a20_init function. If you're lucky,
        this will enable the A20 gate, but as you may expect, you must
        test it to determine whether or not it is.

        The next step taken is an access of I/O port 0xEE. This does not
        work in QEMU (the VM that I am using), so what machine this
        actually works on I have no idea, but it's worth trying. As
        always, the memory address bus is tested afterwards.

        Finally, we can try the fast A20 enable feature. Because it has
        to be the last tried option, as it can crash a machine where
        it's unsupported or do something completely random, it isn't
        actually very fast, and the slowest option of them all. The
        memory address bus is tested afterwards, and if this 4th option
        doesn't work then we just give up.

        So there you go, that's the A20 gate, and this is my
        implementation.

FIX: Actually call a20_init

---
## [Skeletonman0/goonstation](https://github.com/Skeletonman0/goonstation)@[c49f160f09...](https://github.com/Skeletonman0/goonstation/commit/c49f160f0977adca9e6ea57b6f89b50ccc589cc2)
#### Monday 2023-05-29 23:09:06 by skeletonman0

fuck you *makes your clothing code use wear_state so things are more consistent*

---

