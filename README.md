## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-06-27](docs/good-messages/2023/2023-06-27.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,180,289 were push events containing 3,630,932 commit messages that amount to 300,443,965 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 45 messages:


## [ARF-SS13/coyote-bayou](https://github.com/ARF-SS13/coyote-bayou)@[6fe28837f1...](https://github.com/ARF-SS13/coyote-bayou/commit/6fe28837f1d0337091619b4d4b9254f252bc6f83)
#### Tuesday 2023-06-27 00:48:02 by gob

Ghouls bleed again

Crowley: "Ha, ha! I like a human that knows his place. Too many of you think we're all just zombies. They don’t know, or don’t care, that we’re just as human as they are inside. *We bleed!* We hurt! We regret! And you know what really pisses me off? They think the only way to kill us is to shoot us in the head, like in the old zombie stories, and that will put us out of our misery. Hey, I know! Maybe you could help me even the score."

---
## [NetBSD/pkgsrc](https://github.com/NetBSD/pkgsrc)@[5c6fb42622...](https://github.com/NetBSD/pkgsrc/commit/5c6fb4262218b4a618da90c40f734afe199dab03)
#### Tuesday 2023-06-27 01:08:35 by gutteridge

py-music21: update to 9.1.0

Music21 v9 (June 2023) is the latest release of music21, a toolkit for computational music research.

Version 9 contains about 600 new commits and features from the version 8 release from September 2022. It is the latest and best release in the industry standard toolkit for doing music research and composition ("traditional" computation and AI/ML) with musical scores.

As a new Version X release, music21 gains a lot of its power with a few non-backwards compatible changes that make the system easier to use, faster, and more up to date. People using music21 in existing environments should read the change logs to make sure their systems work with it before upgrading.

A big change in music21 is that v9 is compatible with Python 3.10 and 3.11 only. The version 9 release will be updated to be compatible with at least Python 3.12 when it is released. Users on Python 3.8 and 3.9 should stick with v8 and those on older versions should look at the README to see what version will be installed for their systems.

Two weeks from the release of version 9 (July 1, 2023), Michael Asato Cuthbert, the lead developer of music21 will take a 6-12-month sabbatical from monitoring the mailing list, answering questions/issues, and merging PRs in order to focus on what he does best and what is best for the community: developing core parts of the system and documenting what already exists. Working with the user community has been amazing, but given that he only has about 10-15 hours per week to devote to the project, it often means deviating from efforts that help a large number of people to instead work through PRs and issues that are important to a smaller community. This news will probably not be welcomed by some, but the results should be better for the larger community.
What's Changed

    Music21 v9 is for Python 3.10 and 3.11 only and uses tools and speedups only available to those versions. Music21 drops its prior policy of supporting previous 3 versions and now supports the latest 2 versions only (to improve developer experience).
    Notebook/Jupyter: All pages are now shown on .show(). Compatible with Jupyter 7.0beta and JupyterLab. MIDI improvements (@mscuthbert in #1592)
    Added to corpus: (1) Queen Liliuokalani’s Aloha Oe, (2) J.R. Johnson’s Lift Every Voice And Sing (3) Vincente Lusitano’s madrigal Allor che Ignuda – part of a larger project to make the music21 corpus more representative.
    Lots more typing! Use music21 in a modern IDE to see it. Uses Python 3.10 TypeGuards. Add common.classTools.holdsType([‘a’, ‘b’], str) which asserts that everything in a collection has the same type. (@mscuthbert in #1447). converter and corpus are fully typed.
    Docs! Documentation of equality explained better. braille, corpus, converter much improved. (1) Much better aesthetics and utility @mscuthbert in #1455 and #1452). (2) Add “developerReference/startingOver” – mistakes made in designing music21 that are too late to fix, but the next generation of software should not emulate. (3) add docs about abcFormat support (@mscuthbert in #1484). (4) coreInsert (@mscuthbert in #1549). (5) layout (@mscuthbert in #1554). (6) clercqTemperley (RS100 dataset) format (#1558)
    RomanText and related formats: (1) Repeats in RT and TSV are improved (@malcolmsailor in #1434, #1435, #1503) (2) anacrusis support (@mscuthbert in #1532) (3) measure numbers on ClercqTemperley (@mscuthbert in #1558)
    harmony: (1) RomanNumerals and ChordSymbols with front accidentals (flat II, sharp IV, etc.) now take their 7ths, 9ths, etc. from the underlying keys (@mscuthbert w/ thanks to @malcolmsailor in #1439), (2) RomanNumeral’s writeAsChord works properly (@mscuthbert in #1445)
    and (3) transpose properly (@malcolmsailor in #1414). (4) roman.RomanNumeral(2, ‘C’) will now give d-minor, not d-major (@jacobtylerwalls in #1481), (5) preferSecondaryDominants implements V/x (@MarkGotham in #796).
    MusicXML improvements: (1) TempoText is exported (@gregchapman-dev in #1437)
    (2) harmony/numeral figures are MusicXML 4.0 compatible (@mscuthbert in #1445) (3) Preserve multiple fingerings on chords in musicxml import (@jacobtylerwalls in #1475) (4) Translate "implicit" attribute of MusicXML measures (@jacobtylerwalls in #1493) (5) Synchronize Measure IDs on Musicxml out (@rigaux in #1490) (6) MusicXML sound tag finds metronome marks (@TimFelixBeyer in #1579) (7) Add MusicXML security warning (@mscuthbert in #1584)
    Speed/Performance improvements on (1) deepcopy (@mscuthbert in #1464) (2) ABC (@mscuthbert in #1461) (3) LanguageDetector (@mscuthbert in #1456) (4) quantize() (@TimFelixBeyer in #1594) (5) use deques instead of pop(0) #1466, (6) searching/MetadataBundles cache in tests (@mscuthbert in #1511)
    (7) findGaps() on gapless streams (@jacobtylerwalls in #1515) (8) ChordSymbols (@jacobtylerwalls in #1527)
    Braille – add segment.BrailleElementGrouping. Good amount of refactoring. (@mscuthbert in #1495)
    Converter/Corpus: converter.toData – like .write or .show but gives the raw data as a string or byte by @mscuthbert in #1451
    Frozen/Immutable objects can be created now; this will allow for creating, for instance, one default 4/4 meter that cannot be changed but used as a default in many places. common.FrozenObject and duration.FrozenDuration (@mscuthbert in #1460)
    New subConverters register above default subConverters, so it is now possible to develop a subConverter like Greg’s converter21 project that handles a format music21 supports but do it differently or better. (@mscuthbert in #1520)
    Ornaments/Expressions (all by @gregchapman-dev) – (1) ornament accidentals have a great new system and are aware of their measure and key context (#1545) (2) Mordents get placement like Turn and Trill (#1516) (3) Support for delayed turns (#1533)
    Spanners: (1) Spanner.fill() – say you’ve set a slur to just include the first and last notes. .fill() will find all the intermediate notes. (@gregchapman-dev in #1486) (2) spanner.SpannerAnchor class allows a spanner to start and stop at a point where there is no other Music21Object at the offset (like a whole note crescendo that begins on beat 2 and ends on beat 3) (@gregchapman-dev in #1479). (3) Guitar: Hammer-on and Pull-off as Spanners (@louisbigo in #1142)
    Streams – (1) new module stream.tools and stream.tools.removeDuplicates (e.g. keys, clefs, by @MarkGotham in #1454) . (2) stream.makeNotation.saveAccidentalDisplayStatus() context manager for restoring pitches’ accidentalDisplayStatus after a manipulation (like transposition by octave) @gregchapman-dev. (3) stream.makeNotation.makeOrnamentalAccidentals (#1545)
    Percussion: (1) Implement useful PercussionChord.pitches property (@jacobtylerwalls in #1547), (2) Ignore Unpitched objects in key analysis (@jacobtylerwalls in #1543, (3) Search support (@mscuthbert in #1597)
    MIDI: (1) Minimize gaps produced by quantization algorithm (@jacobtylerwalls in #1540) (2) fix jupyter/colab MIDI (@mscuthbert in #1565) (3) Increase default MIDI ticksPerQuarter for higher accuracy of tuplets (@TimFelixBeyer in #1577)
    ABC: set version from I:abc-version information (@mscuthbert in #1589)
    pitch module gets: isValidAccidentalName, standardizeAccidentalName.

Bug fixes

    Ottava transposition bugs (in m21 and in musicxml output) (@gregchapman-dev in #1486)
    diminished and half-diminished 11th chord types were incorrect (@jacobtylerwalls in #1497)
    Avoid creating duplicative ChordStepModifications (@jacobtylerwalls in #1509)
    Zero quarterLengths will not be represented as Fraction(0, 1)
    MIDI: (1) Don't set status byte on Meta Message (@TimFelixBeyer in #1575) (2) unknown meta message still parses (@TimFelixBeyer in #1573)
    Fix stripTies when accidentals are natural & none (@TimFelixBeyer in #1556)
    Scores could previously change after .write()(@TimFelixBeyer in #1560)
    requests should have been in the minimum requirements (@jacobtylerwalls in #1568)
    Prevent doubly-flatted sevenths in chord symbols (@jacobtylerwalls in #1572)

Incompatible Changes not mentioned above:

    Equality: == or __eq__ comparison on many objects has changed. – it is now based on a class hierarchy where the object needs to be equal in all of its super-classes (@mscuthbert in #1466 and #1459).
    For time signatures: (@MarkGotham in #1457). For ChordStepModification (@jacobtylerwalls in #1482). An exception is made for RomanNumerals which do not need to have pitches in the same octave (like their chord.Chord superclass requires)
    schumann folder is moved to schumann_robert to match (equally amazing) schumann_clara.
    subConverter is consistently spelled with capital C in all contexts. Before it was a mismash of capital C and lowercase C. (in #1592)
    Full Measure Rests taken into account Finale usage of the measure=”yes” tag on pickups (@mscuthbert in #1595)
    All Music21Objects must be hashable and default instantiate (@mscuthbert in #1467)
    Duration, volume, and StreamStatus all keep string references to clients (major change if you were playing with _client private variables. Only a public change if you were counting on garbage collection to run more often)
    contextSites that are derived fixes a bug.
    Developers using the private _deepcopySubclassable should know that “removeFromIgnore” has been removed for performance reasons.
    Spanner.prePostObjectSpanners is renamed “relatedSpanners()”
    A number of cases where an attribute which is usually a string started with None now start with ‘’ instead (typing improvement)
    Refactors to ipython21 and the IPython (now Jupyter), MIDI, MusicXML subconverters in #1592.

Removals

    Music21Exception subclasses not used in the system are removed. Reduce 172 Exceptions to 154 (@mscuthbert in #1465)
    musicxml.xmlToM21.textNotNone – use new strippedText() and check for False.
    Already marked for deprecation and removed: common.cleanupFloat() (use opFrac), common.euclidGCD (use math.gcd), Metadata.setWorkId (use md.uniqueName = value), VoiceLeadingQuartet.color() (assign colors to individual notes with .style.color), (#1440)

Deprecations

    Spanner.numberRange replaces Spanner.getNumberList() — they do the same thing. (#1447)
    romanText.clercqTemperley – toScore() – call toPart() instead since that is what it does.
    scale.next() – use scale.nextPitch() instead – since it shadows Music21Object.next()

New Contributors

    @sararocks made her first contribution in #1472
    @rigaux made their first contribution in #1490
    @TimFelixBeyer made his first contribution in #1560

---
## [MichaelDeBoey/next.js](https://github.com/MichaelDeBoey/next.js)@[6238f8a5c0...](https://github.com/MichaelDeBoey/next.js/commit/6238f8a5c0ffabb7dfb35872c52c942ed7f148da)
#### Tuesday 2023-06-27 01:21:10 by Jimmy Lai

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
## [garimau/argilla](https://github.com/garimau/argilla)@[c9bfaf28f7...](https://github.com/garimau/argilla/commit/c9bfaf28f72c240f5372640efbcb745d1e2b09be)
#### Tuesday 2023-06-27 01:28:10 by David Berenstein

[FEATURE] Feature/prepare for training feedbacktask (#3151)

# Description

I added a very rough outline of my ideation behind
`prepare_for_training` with the new `FeedbackDataset`. As discussed
there are 3 complexities:

- How to resolve annotator alignment?
- How to resolve optional fields, which have not been filled out? e.g.,
"Please provide a correction for prompt 1?".
- How handle potential concatenation of fields? 

To make it modular I created a step-wise approach.

1. `Pydantic` Models that map and verify data fields, like so. By doing
this we keep the flexibility to allow for other tasks like
TextClassification and this ensures we can directly use `datasets.field`
and `dataset.questions` for defining training. We could also use the
`name` values from the fields/questions, but this might be more error
prone.
2. `get_relevant_data_for_training()` in `List[dict]` format with all
relevant fields from the Pydantic model. **annotator alignment issue**.
For now I opted for choosing the first non-zero value.
3. Forward the `List[dict]` to a similar flow we previously had.
4. Also add `dataset.unify_responses(question, Enum(strategy))`-method
5. Added `*QuestionUnifcation` to schemas to hold logic surrounding
unifying multiplier responses
6. Added `client.feedback.training`
7. Added`TrainingDataFor*` to hold logic surrounding
`prepare_for_training`-methods per task
8. Added inheritance for ArgillaTrainer

```python 
import argilla as rg
from argilla import (
    FeedbackRecord,
    LabelQuestion,
    LabelQuestionUnification,
    MultiLabelQuestion,
    TrainingDataForTextClassification,
    ArgillaTrainer
)

dataset = rg.FeedbackDataset(
    guidelines="Add some guidelines for the annotation team here.",
    fields=[
        rg.TextField(name="text", title="Human prompt"),
    ],
    questions =[
        LabelQuestion(
            name="relevant",
            title="Is the response relevant for the given prompt?",
            labels=["yes","no"],
            required=True,
            visible_labels=None
        ),
        MultiLabelQuestion(
            name="content_class",
            title="Does the response include any of the following?",
            description="Select all that apply",
            labels={"hate": "Hate Speech" , "sexual": "Sexual content", "violent": "Violent content", "pii": "Personal information", "untruthful": "Untruthful info", "not_english": "Not English", "inappropriate": "Inappropriate content"},
            required=False,
            visible_labels=4
        ),
    ]
)
dataset.add_records(
    records=[
        FeedbackRecord(
            fields={"text": "What is your favorite color?"},
            responses=[{"values": {"relevant": {"value": "yes"}, "content_class": {"value": ["hate"]}}}]
        ),
        FeedbackRecord(
            fields={"text": "What do you think about the new iPhone?"},
            responses=[{"values": {"relevant": {"value": "no"}, "content_class": {"value": ["hate"]}}}]
        ),
        FeedbackRecord(
            fields={"text": "What is your feeling about the technology?"},
            responses=[{"values": {"relevant": {"value": "yes"}, "content_class": {"value": ["sexual"]}}},
                       {"values": {"relevant": {"value": "no"}, "content_class": {"value": ["hate", "sexual"]}}},
                       {"values": {"relevant": {"value": "yes"}, "content_class": {"value": ["hate", "sexual"]}}}]
        ),
        FeedbackRecord(
            fields={"text": "Jesus Christ!"},
            responses=[{"values": {"relevant": {"value": "no"}, "content_class": {"value": ["sexual"]}}},
                       {"values": {"relevant": {"value": "no"}, "content_class": {"value": ["hate"]}}}]
        )

    ]
)

# print(dataset.question_by_name("relevant").__all_labels__)

label = LabelQuestionUnification(question=dataset.question_by_name("relevant"), strategy="majority")
training_data = TrainingDataForTextClassification(text=dataset.field_by_name("text"), label=label)

for framework in ["spacy", "transformers", "openai", "spark-nlp"]:
    formatted_data = dataset.prepare_for_training(framework, training_data, fetch_records=False, train_size=0.8)
    print(formatted_data)

trainer = ArgillaTrainer(
    dataset=dataset,
    training_task_mapping=training_task_mapping,
    framework="setfit",
    fetch_records=False
)
trainer.train("test")
```

Closes #2954
Closes #3184
Closes #3152 

**Type of change**

- [X] New feature (non-breaking change which adds functionality)
- [X] Improvement (change adding some improvement to an existing
functionality)

**How Has This Been Tested**

- [ ] Test A
- [ ] Test B

**Checklist**

- [ ] I have merged the original branch into my forked branch
- [ ] I added relevant documentation
- [ ] follows the style guidelines of this project
- [ ] I did a self-review of my code
- [ ] I made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my
feature works
- [ ] I have added relevant notes to the CHANGELOG.md file (See
https://keepachangelog.com/)

---------

Co-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>
Co-authored-by: Alvaro Bartolome <alvaro@argilla.io>

---
## [Vwing/jobu-tupaki-bot](https://github.com/Vwing/jobu-tupaki-bot)@[24a2439f51...](https://github.com/Vwing/jobu-tupaki-bot/commit/24a2439f5122685a01d16f1b34f42bcb0e0cbaf7)
#### Tuesday 2023-06-27 01:44:43 by Vincent Wing

Removed the bit about 'EEAAO' from the system message.

The bot kept thinking she was remembering a movie script instead of her own life. Now it's better about that.

---
## [Bjarl/Shiptest](https://github.com/Bjarl/Shiptest)@[7468161f7e...](https://github.com/Bjarl/Shiptest/commit/7468161f7ec2180c7752cd2cc99b164522a3540a)
#### Tuesday 2023-06-27 01:48:30 by FalloutFalcon

Trickwines! Again! (#1914)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Trickwines are a set of new reagents aimed at improving tribal/srm style
ships
The core concept are wines crafted out of mob drops and plants that
provide a buff on drinking and a debuff on throwing with bonus effects
against fauna
To facilitate the transfer of booze to target it also adds breakaway
flasks, 50u glass bottles that shatter violently on contact providing
extra throw force as well as a 25u gulp size which forces the user to
choose between buff or debuff
I plan on adding a fair few more Trickwines and the SRM Barrel Class
Brewer Vessel (SRM could really use one then 1 original ship) in later
prs to build on this concept
This HackMD will provide descriptions for the wines as well as a place
of information for all Trickwine-related content
https://hackmd.io/eUIddN2dS3mpeU1CThFGng

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Adds a fun new option for ships that lack proper chemistry and forces
them to choose which effect they actually want.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: FalloutFalcon
add: Trickwines
add: Breakaway flasks!
add: Basic Trickwine brewing equipment to the SRM glaive
imageadd: Sprites for breakaway flasks along with trick wine icons for
them!
code: Breakaway_flask_icon_state = null used for the same purpose as the
glass and shot glass versions
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

I DIDNT KNOW IF YOU RENAME A BRANCH IT CLOSES PRS RELATED TO IT?? I
THOUGHT IT JUST KNEW!!
3rd times a charm!

---------

Signed-off-by: FalloutFalcon <86381784+FalloutFalcon@users.noreply.github.com>
Signed-off-by: Mark Suckerberg <mark@suckerberg.gay>
Co-authored-by: Mark Suckerberg <mark@suckerberg.gay>

---
## [Bjarl/Shiptest](https://github.com/Bjarl/Shiptest)@[8744738e59...](https://github.com/Bjarl/Shiptest/commit/8744738e5955c02834d67db6f14201c28c9ac61c)
#### Tuesday 2023-06-27 01:48:30 by Arturlang

Updates TGUI and adds bin folder for .bat scripts (#2011)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Updates TGUI and build tools and .vscode files to what TG has.
Does not actually update UI's, but does have fixes for a couple
including the join game UI's tabs not working.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Not needing to have a local installation of yarn to run dev-mode is
nice.
Updating TGUI is a annoying chore that helps in the future when porting
more interfaces
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
code: Adds a bin folder with dev scripts, updates TGUI, .vscode folder
to what TG has.
fix: Fixes the input in the bottom right being white in darkmode, no
more unreadable text
fix: You can now use the tab buttons in the join ship menu.
qol: The outpost mission menu now looks a whole lot better
fix: The input bar no longer randomly becomes white and unreadable on
darkmode
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Mark Suckerberg <29362068+MarkSuckerberg@users.noreply.github.com>

---
## [dfinity/motoko](https://github.com/dfinity/motoko)@[b0f5aee3c7...](https://github.com/dfinity/motoko/commit/b0f5aee3c71c66f01aaad12cabe39928b043b829)
#### Tuesday 2023-06-27 02:15:17 by Claudio Russo

feat: allow canister imports of service constructors, silently ignoring the service arguments. (#4041)

Allow canister imports of service constructors, silently ignoring the service arguments. 

A hack that fixes #3990 (for some definition of fix) and duplicate #2319.

Really, dfx should be feeding the idl of the instantiated service, not service constructor, to dependent canisters, but until it's fixed to do so (and it hasn't been forever now), this is a reasonable and simple workaround, avoiding the error-prone and kludgy workaround of rewriting candid files described, for instance, here:

https://dfinityorg.notion.site/ckBTC-example-Encode-Hackathon-0aaf6292e3404dabb49df5d1b5abc797#08a7469beaf14d6ba35e8827e363e160

and also used here:

https://github.com/letmejustputthishere/ckbtc-payments

via npm scripting hacks (!).

Also see here for the pain this caused:

https://forum.dfinity.org/t/confusing-type-error-when-crossing-canisters-expression-of-type-mytype-cannot-produce-expected-type-mytype-1/20636

UPDATE: I turned the previous error into a warning to nag us to fix dfx.


UPDATE: Potentially obviated by https://github.com/dfinity/sdk/pull/3138, which teaches dfx to strip the service argument.

UPDATE: @chenyan-dfinity thinks we should still merge for other scenarios (old dfx, new compiler, I guess).

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[5c4b13863f...](https://github.com/cmss13-devs/cmss13/commit/5c4b13863f90877e920ce329bd60e99559d7fe35)
#### Tuesday 2023-06-27 02:27:01 by ihatethisengine

Larva surge is limited by marines/xenos ratio (#3592)

# About the pull request

Xenos after hijack now get larva based on marines/xenos ratio. Instead
of infinite larva, larva surge will try to increase the initial amount
of xenos on hijack to 50% of marines forces over time (with a minimum of
5 larvas, if xenos already have good numbers).

# Explain why it's good for the game

Initially, if I remember correctly, larva surge was brought into the
game to discourage marines from early meta-evacuations, which is fair.
But consequently, it really hurt the hijack sequence. Even if marines
evac fair and square, larva surge still comes in action and makes
situation for marines even worse, utterly discouraging everything but
either boomrushing the Alamo or holding lifeboats to evac.

This resulted in hijacks being very repetitive and boring. More than
that, larva surge is extremely busted on lowpop due to the fact you can
get around 20 xenos from nothing, making lowpop hijack even less
interesting. So with this change marines will still get punished for
evaccing with good numbers, but won't be penalized as much for honest
evacuations.

So hopefully, we will see more variety of hijacks and more interesting
stories!

P.S. if you have a better formula, let me know.


# Testing Photographs and Procedure
<details>
My friend @Diegoflores31 tested this for me, thanks!
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl: ihatethisengine
balance: larva surge is limited by marines/xenos ratio
fix: xenos no longer get free larva from abandoned facehuggers during
hijack
/:cl:

---------

Co-authored-by: ihatethisengine <treml.treml@yandex.ru>
Co-authored-by: fira <loyauflorian@gmail.com>

---
## [TheCasualDev/bootstrap.fcc](https://github.com/TheCasualDev/bootstrap.fcc)@[e17a1a49f8...](https://github.com/TheCasualDev/bootstrap.fcc/commit/e17a1a49f821b74da47fe4ec89dbd5705783a3cd)
#### Tuesday 2023-06-27 02:58:23 by TheCasualDev

🚀 Setup the basics for SASS

It is time to get sassy (god I hate myself)

---
## [hanifardhani/platinum_kernel_xiaomi_platina](https://github.com/hanifardhani/platinum_kernel_xiaomi_platina)@[c5d5b1b8f1...](https://github.com/hanifardhani/platinum_kernel_xiaomi_platina/commit/c5d5b1b8f1142fab8c8a1deac44051de4a55e3b3)
#### Tuesday 2023-06-27 04:00:53 by Christian Brauner

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

---
## [Iamgoofball/-tg-station](https://github.com/Iamgoofball/-tg-station)@[8788e48378...](https://github.com/Iamgoofball/-tg-station/commit/8788e483788db2432b9649313efc9426d324379f)
#### Tuesday 2023-06-27 04:44:05 by Time-Green

Shuttle events (#76008)

## About The Pull Request


https://github.com/tgstation/tgstation/assets/7501474/a2d83ce8-eba1-42d9-a1f8-9d73f7c40b21

Adds shuttle events! Stuff can now start to happen outside the shuttle,
either benign or spicy (but usually just fun to watch)!
## Why It's Good For The Game

The shuttle escape sequence is an important part of the game, uniting
about every player surviving player. Recently, #71906 has made the
escape sequence more forgiving as well as more interesting by
conditionally doubling the playing field. The area outside the shuttle
is still mostly empty though, except for the few people being spaced,
daredevils and the occasional epic space fight.

This PR adds adds some space events to spice up the outside of the
shuttle! This both gives people something too look at, making the escape
sequence feel less static and more lively, as well as give people a
reason to go outside and get the full experience of ~being decapitated
by a meteor~ swimming with the fishes!

<details>
  <summary>Shuttle Events</summary>

**Friendly carp swarm**
Spawns a group of carp that flies past the shuttle, completely friendly
unless provoked.

**Friendly meteors**
Spawns a lot of strong meteors, but they all miss the shuttle.
Completely safe as long as you don't go EVA

**Maintenance debris**
Picks random stuff from the maintenance spawn pool and throws it at the
shuttle. Completely benign, unless you get hit in the head by a toolbox.
Could get you some cool stuff though!

**Dust storm**
Spawns a bunch of dust meteors. Has a rare chance to hit the shuttle,
doing minimal damage but can damage windows and might need inflight
maintenance

**Alien queen**
One in every 250 escapes. Spawns a player controlled alien queen and a
ripley mech. RIP AND TEAR!! Really not that dangerous when you realize
the entire crew is on the shuttle and the queen is fat as fuck, but can
still be fun to throw people around a bit before being torn to shreds.

**ANGRY CARP**
Once in every 500 escapes. Spawns 12 normal carp and 3 big carps, who
may just decide to go through the shuttle or try and bust through the
window if you look at them wrong. Somewhat dangerous, you could stay
away from the windows and try to hide, or more likely shoot at them and
weld the windows

**Fake TTV**
Lol

**Italian Storm**
Once in every 2000 rounds. Throws pasta, pizza and meatballs at the
shuttle. Definitely not me going off the rails with a testing event

**Player controlled carp trio**
Once in every 100 escapes. Spawns three player controlled carp to harass
the shuttle. May rarely be a magicarp, megacarp or chaos carp. I can't
honestly see them do anything other than be annoying for 3 seconds and
die

There are some other admin only ones: a group of passive carps going
directly through the shuttle and just being little shits, and a magic
carp swarm
</details>

Events are selected seperately, there isn't a crazy weighting system,
each just has a chance to run, and multiple could run at once. They also
don't immediately trigger, so people can get settled a bit, and to make
sure just waiting out the more dangerous ones is still a valid strategy.

## Changelog
:cl:
add: Adds shuttle events! If shuttle escapes weren't exciting before
(doubtful), they definitely are now! I'm joking it's mostly an
atmosphere thing.
admin: Adds an admin panel to interact with shuttle events, under the
Events tab: Change Shuttle Events
fix: Objects spawned in hyperspace will properly catch hyperspace drift
/:cl:

There's a few things I'd like to do later (another PR) (honestly anyone
can do them because I suck at follow-ups), because this is too big as
is:
- Hijack triggered shuttle events
- More events (got a lot of cool suggestions, but I'm putting most of
them on hold)
- Maybe stration announcements if some more dangerous ones get added
- Structures appearing next to the escape shuttle???

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[daa33d89fe...](https://github.com/necromanceranne/tgstation/commit/daa33d89fef10650f89f7db160f110141ab99e5d)
#### Tuesday 2023-06-27 04:54:16 by IndieanaJones

Xenomorph/Alien Rework 2023: Part 1 (#75286)

## About The Pull Request

Alternative to #75277

Kept you waiting, huh?

This PR is the first part of a Xenomorph rework which seeks to make the
big lugs more balanced and up to date with /tg/'s current design. This
mainly involves curtailing xenomorph's infamous hardstuns into more
interactive forms of combat, while also giving some buffs to the
xenomorph's more unique abilities in order to keep them threatening.

Part 1 will focus on simple number changes and some simple mechanic
changes. In the future, changes will be made to endgame involving
xenomorphs, along with changes to other facets of Xenomorphs.

Highly based off of #55937.

Changes:

- Xenomorph disarm has been completely reworked. While a disarm will
attempt to, well, disarm, a human opponent should they be holding
something, it will no longer immediately hardstun targets when they
aren't. Instead, the xenomorph will shove the target several tiles back
and inflict 35 stamina damage. If the target slams into a wall, this
will also come with the added effect of knocking them down. If a human
is incapacitated, however, right click will slam them into the ground,
which paralyzes them for a lengthy 5 seconds (which is ultimately half
the time xenos could stun you for before), allowing for safe transport
back to the nest as long as you keep them close.

- Humans can now shove xenomorphs. Due to being the superior predator,
however, you can't knock down xenomorphs from shoving. You can slow them
for a little bit akin to humans though.

- Neurotoxin no longer is a hardstun. Instead, it deals 50 stamina
damage on contact. It is still resisted by BIO armor.

**HUNTER:**
- Speed reduced from -1 to -0.3.
- Pounce speed is twice as fast as before (1 to 2)
- Hardstun time on pounce reduced from 10 seconds to 5 seconds.

Hunters being insanely fast has been a major balance-ruining factor of
xenomorphs for many years now. These buggers could practically ambush
anyone, hardstun them immediately, and then leave before anyone could do
anything. Now, with their speed nerfed and in combination with the xeno
shove changes, hunters will need to spend more time to down a target.
Their pounce was practically useless, so its been sped up in order to
make it more practical to use.

**SENTINEL**
- Speed reduced from 0 to 0.2
- Cloak alpha reduced from 0.75 to 0.25 (you're more hidden now)

Sentinels receive a large nerf in regards to their spit, but their
before useless cloaking ability has been greatly improved upon as
compensation. They now serve better as defenders and ranged ambushers.

**XENOMORPH DRONE**
- No changes

As in the original PR, drones are perfeclty balanced in my eyes, so no
changes were required.

**XENOMORPH PRAETORIAN**
- Speed increased from 1 to 0.5
- No changes

Praetorians get affected by the nerfs of the other xeno abilities, but
now they're a bit faster in order to close the gap to use their
abilities.

**XENOMORPH QUEEN**
- Speed increased from 3 to 2
- Health increased from 400 to 500
- Damage increased from 20 to 50

Xenomorph queens have been sped up and made more tanky and lethal in
close-range combat. Fighting this beast up-close should be a death
sentence to almost anything else in the game. Speed increases will help
her re-position and close the gap on potential prey.

**OTHER CHANGES**
- Fixed a bug where simplemobs didn't actually use xenomorph's damage
values when they were attacked by them.

## Why It's Good For The Game

Xenomorphs are old, and haven't been updated for quite a long time. This
has left them as sources of a bunch of hardstuns which made counterplay
from a modern spaceman extremely difficult. With these changes, fighting
xenomorphs is more interactive and should end up being more enjoyable
for both crew and xenos. Buffs were also given out to incentivize usage
of xenomorph's unique abilities as opposed to the standard disarm spam
which was most effective for them until now.

## Changelog
:cl:
balance: Xenos have been rebalanced, removing their hardstuns on their
disarm and neurotoxin, along with a slew of other changes. Xenos have
received buffs to their more unique abilities in return.
fix: Fixed simplemobs ignoring xenomorph's melee damage values when
being attacked by them.
/:cl:

---
## [javalos16/FirstKnit](https://github.com/javalos16/FirstKnit)@[3f24d9fe2a...](https://github.com/javalos16/FirstKnit/commit/3f24d9fe2abfa169a070f57114454e53d3c60b49)
#### Tuesday 2023-06-27 04:55:19 by javalos16

Add files via upload

First Knit
jesus avalos
2023-06-27
1 A Little Survey
1.1 A short history of you.
1.1.1 my answer
1.2 Your computer and your and its capability?
1.2.1 my answer
1.3 Others and You?
1.3.1 my answer
1.4 Aspirations?
1.4.1 my answer
1.5 Past adventures?
1.5.1 my answer
1.6 Why are you taking Statistics?
1.6.1 my answer
1 A Little Survey
Here are just a few questions so I can get to know you and so you can get practice submitting an assignment in Canvas. For each question, insert your answer underneath. Make sure each answer is at the minimum a complete sentence with correctly spelled words and correct puncuation.

1.1 A short history of you.
Where did you attend High School, and did you graduate? Compare english class to math, is one easier for you than the other? Finally which subject did you do the best in? Your answer should have at least two sentences devoted to each question.

1.1.1 my answer
I went to Long Beach Polytechnic High school,I graduated in 2002. I found Math a bit easier than english. I did have the same grades in both subjects. I did very well in my wood shop and auto mechanics class.

1.2 Your computer and your and its capability?
For this class you need a computer you can use at home. So, what kind is it (windows, Apple, Linux)? On a scale of 1 to 10, where 1 is a total dummy (doesn’t know a mouse from a keyboard) and 10 is a complete geek (knows computer stuff in and out) How do you rate yourself? You also need to have have internet access. How is your connection to the internet where you live?

1.2.1 my answer
I have a samsung chrome book laptop, It is a chome book.I would say it is a 5 in a scale of 1-10. Does not have a mouse but at home I integrated one in it. In a scale 1-10, I think that I am a 2 or 3 in skills with a computer. I have 1 gig of internet access.

1.3 Others and You?
What name do you prefer to be called by your classmates and instructor, if your buddys call you something but you want people in the class to call you something else - what would that be?

1.3.1 my answer
Name I prefer to to be called is Jesus. I actually really good with being called Jesus.

1.4 Aspirations?
What do you want to achieve in life? What college subject do you think would be of the greatest interest to you? What degree or certificate are you trying to achieve?

1.4.1 my answer
I want to be able to not worrie about money and be self sustained.I am currently studing to be RN.

1.5 Past adventures?
Have you ever gone to foreign countries, if so which ones, if not Where might you go in the future? Have you ever been in the military, if so which branch, if not which branch would you choose if you got drafted, and why?

1.5.1 my answer
I have been to Mexico in vacation to visit family. I want to be a traveling nurse so I can travel to other cities. I have not been to the military.

1.6 Why are you taking Statistics?
Did you take Math 115 or Math 116 ? Did you know Math 115 only satisfies a general education requirement but that Math 116 counts as taking statistics in several transfer institutions??
What grade do you need to attain in stats to not upset your future plans, What is your plan?

1.6.1 my answer
I am learning statistics to satisfy my prerequisite. I will be happy that this satisfies my general studies in math. I would like to at least receive a B or higher.

---
## [2002jai/Data-Visualization-Tools-e.g.-Tableau-Power-BI-](https://github.com/2002jai/Data-Visualization-Tools-e.g.-Tableau-Power-BI-)@[47649fcea0...](https://github.com/2002jai/Data-Visualization-Tools-e.g.-Tableau-Power-BI-/commit/47649fcea04946101aaae07a1707ba232d0fdf0d)
#### Tuesday 2023-06-27 05:58:47 by jai chauhan

Data-Visualization Tools (Tableau,Power-BI etc.)

GitHub Repository: Data Visualization Tools for Data Science

Welcome to the Data Visualization Tools for Data Science repository on GitHub! This repository is a treasure trove of projects, tutorials, and resources designed to help you master the art of data visualization using popular tools like Tableau, Power BI, Python, and R.

Data visualization is a crucial aspect of data science, allowing us to unlock insights, communicate findings effectively, and make data-driven decisions. Whether you are a beginner or an experienced data scientist, this repository is your one-stop destination for honing your data visualization skills and exploring various techniques.

Inside this repository, you'll find comprehensive tutorials and examples on getting started with Tableau and Power BI, from basic charts to advanced features like table calculations, parameters, and interactive dashboards. Dive into the world of Python and R, and leverage popular libraries like Matplotlib, Seaborn, ggplot2, and Plotly to create stunning visualizations.

But it doesn't stop there! We go beyond just the tools and cover fundamental data visualization principles, such as choosing the right chart types, understanding color theory, and designing visually appealing and informative graphics. You'll also find best practices for storytelling with data, accessibility considerations, and performance optimization for large datasets.

The repository includes case studies from various industries, allowing you to explore real-world data visualization projects and gain insights into different application domains. Additionally, you'll find resources on integrating these visualization tools with other data science frameworks and creating interactive web applications.

We encourage contributions from the open-source community to make this repository even more valuable. Share your code, insights, and ideas, and help us build a vibrant and collaborative community focused on data visualization in data science.

Join us on this exciting journey of transforming data into compelling visual stories. Explore the repository, learn new techniques, and unlock the power of data visualization in your data science projects.

---
## [Singul0/tgstation](https://github.com/Singul0/tgstation)@[a8e16030f8...](https://github.com/Singul0/tgstation/commit/a8e16030f83911aef695ba9f28d565c41c99c3e6)
#### Tuesday 2023-06-27 07:23:21 by LemonInTheDark

Optimizes timer insertion by 80% (W QDEL_IN micro) (#76214)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

[Reduces timer insertion cost by
80%](https://github.com/tgstation/tgstation/commit/c9e5b285ed74e60108fddd3f6b45d6d3995c92a8)

Timer name generation involved a LOT of string shit, some in ways where
the string only existed for a moment.
This costs a good bit of time, and can be reduced with only minimal
impacts on the end product, so let's do that. Includes a compile flag to
flip it back if we ever have trouble in future.

This is about 0.1s off init, since we do a lot of timer stuff then too

[Removes STOPPABLE flag from QDEL_IN, moves it to a bespoke
macro](https://github.com/tgstation/tgstation/commit/e7a5d7f2a78fcf0dce4742ced258c9505411b202)

Its a waste most of the time, tho I would LOVE to analyze at compile
time to work out if we care
## Why It's Good For The Game

I like it when we don't spend all of our cpu time just setting the name
var on timers. that's good and not bad.
This saves time fucking everywhere. 15% off explosions, 0.1 seconds off
init, bunch of time off foam. it's just good.

Cherry picked out of #76104 since that was too cluttered (sannnnnn)

<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Singul0/tgstation](https://github.com/Singul0/tgstation)@[5c032cc098...](https://github.com/Singul0/tgstation/commit/5c032cc098f9a1d62f9f9dee133ae7c3e4489dca)
#### Tuesday 2023-06-27 07:23:21 by LemonInTheDark

Adds border smoothing! (Look ma I'm upstreaming) (#76134)

## About The Pull Request

Ok so we currently have 1 (count em) border object that wants to smooth
with other border objects. That's the tram window.

It currently does this manually, via map edits, but that's kinda crappy
so lets be better.

This pr adds a new smoothing mode to handle border objects. 
Unlike other smoothing modes, it returns a bitfield of directions the
border object connects in.

I do this by memorizing a calculation of which dirs "connect" at init,
and reading out of a global list with border object direction, direction
between objects, and if it's a border object, the other object's dir.

I'm doing this primarily because it's become useful for wallening (a
spriter saw the tram thing and is doing the same thing to pod windows,
and I want to support that)

I do think it's potentially useful in other applications too tho, and I
like dehardcoding tram windows.

Also fun bonus (or maybe downside), it's nearly 0 cost because I pulled
the bitmask smoothing define into 2 subdefines, and am swapping the
handler one out to do what I want.
Oh also I got rid of a for loop in smoothing code, redundant and costs
time in list iteration

[Moves tram windows over to the new border object
smoothing](https://github.com/tgstation/tgstation/commit/114873679c94d680788edee9665fa18dba8108c0)

Also replaces some typepath chicanery with a setDir override, for
redundancy in future
Oh and there's a update paths script too, to be nice

## Why It's Good For The Game

More visual possibility in future, fixes a hack we have currently, and
makes some spriters happy.

## Changelog
:cl:
fix: Dehardcodes some stuff with tram windows, they'll be easier to map
with now
refactor: Border objects can now smooth with each other. I'm sure
something cool will come of this
/:cl:

---
## [davidtwco/rust](https://github.com/davidtwco/rust)@[80917360d3...](https://github.com/davidtwco/rust/commit/80917360d350fb55aebf383e7ff99efea41f63fd)
#### Tuesday 2023-06-27 08:34:24 by bors

Auto merge of #112292 - thomcc:tls-ohno, r=m-ou-se

Avoid unwind across `extern "C"` in `thread_local::fast_local`

This is a minimal fix for #112285, in case we want a simple patch that can be easily to backported if that's desirable.

*(Note: I have another broader cleanup which I've mostly omitted from here to avoid clutter, except for the `Cell` change, which isn't needed to fix UB, but simplifies safety comments).*

The only tier-1 target that this occurs on in a way that seems likely to cause problems in practice linux-gnu, although I believe some folks care about that platform somewhat 😉. I'm unsure how big of an issue this is. I've seen stuff like this behave quite badly, but there's a number of reasons to think this might actually be "fine in practice".

I've hedged my bets and assumed we'll backport this at least to beta but my feeling is that there's not enough evidence this is a problem worth backporting further than that.

### More details

This issue seems to have existed since `thread_local!`'s `const` init functionality was added. It occurs if you have a `const`-initialized thread local for a type that `needs_drop`, the drop panics, and you're on a target with support for static thread locals. In this case, we will end up defining an `extern "C"` function in the user crate rather than in libstd, and because the user crate will not have `#![feature(c_unwind)]` enabled, their panic will not be caught by an auto-inserted abort guard.

In practice, the actual situation where problems are likely[^ub] is somewhat narrower.

On most targets with static thread locals, we manage the TLS dtor list by hand (for reentrancy reasons among others). In these cases, while the users code may panic, we're calling it inside our own `extern "C"` (or `extern "system"`) function, which seems to (at least in practice) catch the panic and convert it to an abort.

However, on a few targets, most notably linux-gnu with recent glibc (but also fuchsia and redox), a tls dtor registration mechanism exists which we can actually use directly, [`__cxa_thread_atexit_impl`](https://github.com/rust-lang/rust/blob/master/library/std/src/sys/unix/thread_local_dtor.rs#L26-L36).

This is the case that seems most likely to be a cause for concern, as now we're passing a function to the system library and panicking out of it in a case where there are may not be Rust frames above it on the call stack (since it's running thread shutdown), and even if there were, it may not be prepared to handle such unwinding. If that's the case, it'd be bad.

Is it? Dunno. The fact that it's a `__cxa_*` function makes me think they probably have considered that the callback could throw but I have no evidence here and it doesn't seem to be written down anywhere, so it's just a guess. (I would not be surprised if someone comes into this thread to tell me how definitely-bad-news it is).

That said, as I said, all this is actually UB! If this isn't a "technically UB but fine in practice", but all bets are off if this is the kind of thing we are telling LLVM about.

[^ub]: This is UB so take that with a grain of salt -- I'm absolutely making assumptions about how the UB will behave "in practice" here, which is almost certainly a mistake.

---
## [bhattarai333/DostoyevskyCloner](https://github.com/bhattarai333/DostoyevskyCloner)@[0b560475bb...](https://github.com/bhattarai333/DostoyevskyCloner/commit/0b560475bb13f9c1a35d1ec9555e8f1d9585f554)
#### Tuesday 2023-06-27 08:53:57 by Josh Bhattarai

Using beam search has the output actually looking something like Dostoyevsky's work, but there are lots of strange characters, example output:

Once upon a
day or two, he would come to me and say, ‘Good-bye,’ and I would
tell him to go away.”

“What do you mean by that? I hav!!!"
Razumihin hou!!‘I hai! h!o! t! o! i! w! y! yo! wo! th! wa! wh! hi! s! b! a! c! e! f! l! g! k! n! u! v! m! p! r! d! co! al! bu! an! mo! ar! ha! ho! ne! se! fo! sh! le! de! te! en! di! si! re! ta! sa! su! la! ca! tu! ra! pa! pu! ro! ma! lo! du! del! que! qu! je! fr!.!

   *  “I am so glad to see you! You are a good-natured man, you are! I am very fond of you, too. I have been in love with you since I was a child, and you have always loved me! Oh, my God! what a mamma!... I love you so much that I can't say a word to you now, but I w
ill tell you to-day, to! And I shall be in a state of delirium for the rest of my life!
  As for me, I do not know what to say to him now; I only know that he is a man of the highest character. He is an old man; he has been a long time in his life, a young man! He has a great deal to do with it,! Ah, it is! he! It is all a lie! A lie, of course! But it!s
!t!a!n!p!r!u!e!c!l!k!m!h!f!te!ci!lo!que!_ I shan!d!re!ta!na!fu!cu!ro!va!tu!ra!ou.

---
## [skorch-dev/skorch](https://github.com/skorch-dev/skorch)@[df92d4d5e3...](https://github.com/skorch-dev/skorch/commit/df92d4d5e3cc5991330e339d6c8d6c83798f0caa)
#### Tuesday 2023-06-27 09:22:29 by Benjamin Bossan

Allow regression with 1d targets (#974)

* Allow regression with 1d targets

This change makes it possible to pass a 1-dimensional y to
`NeuralNetRegressor`.

Problem description

Right now, skorch requires the `y` passed to `NeuralNetRegressor.fit` to
be 2-dimensional, even if there is only one target, as is the most
common case. This problem has come up a few times in the past, but
mostly it's just an annoyance - just do `y.reshape(-1, 1)` and you're
good (the error message says as much).

There are, however, also cases where it's not so easy to solve. For
instance, in #972, a user reports that they cannot use skorch with
sklearn's `BaggingRegressor`. The problem is that even if `y` is
reshaped, once it is passed to the net from `BaggingRegressor`, it is 1d
again. I assume that `BaggingRegressor` internally squeezes `y` at some
point.

This PR lifts the 2d restriction check.

Initial motivation

Why does skorch require `y` to be 2d? I couldn't remember the initial
reasoning and did some archeology.

I found this comment:

(https://github.com/skorch-dev/skorch/commit/2f00e2570460fe0a6acd8db94c4d8624b3ddd1eb#diff-66ed08bca4d171889565d0285a36b9b47e0e91e3b33d85c51352d8eb00faefac):

>         # The problem with 1-dim float y is that the pytorch DataLoader will
>         # somehow upcast it to DoubleTensor

This strange behavior should not be an issue anymore, so if that was the
only problem, we should be able to just remove the constraint, right?

Problems with removing the constraint

Unfortunately, it's not that easy. The issue comes down to the
following: When we remove the constraint and allow the target `y` to be
1d, but the prediction `y_pred` is still 2d, the criterion `nn.MSELoss`
will probably do the wrong thing. What exactly is wrong? Instead of
calculating the squared error for each sample pair, the criterion
will broadcast the vector and calculate _all squared errors_ between
each sample, then return the mean of that. To demonstrate, let's remove
the reduction step and look at the shape:

```python
>>> import torch
>>> criterion = torch.nn.MSELoss(reduction='none')
>>> y = torch.rand(100)
>>> y_pred = torch.rand((100, 1))
>>> y.shape, y_pred.shape
(torch.Size([100]), torch.Size([100, 1]))
>>> se = criterion(y_pred, y)
/home/vinh/anaconda3/envs/skorch/lib/python3.10/site-packages/torch/nn/modules/loss.py:536: UserWarning: Using a target size (torch.Size([100])) that is different to the input size (torch.Size([100, 1])). This will likely lead to incorrect results due to broadcasting. Please ensure they have the same size.
  return F.mse_loss(input, target, reduction=self.reduction)
>>> se.shape
torch.Size([100, 100])
```

As can be seen, PyTorch broadcasts the two arrays, leading to 100x100
errors being calculated. Thankfully, PyTorch warns about potential
issues with that.

The current solution is to accept this behavior and hope that the users
will indeed see the warning. If they don't see it or ignore it, it could
be a huge issue, because they still get a loss scalar and might even see
a small improvement in the loss during training. But the model will not
converge and it's going to be a huge pain to debug the bug, if it's even
identified as such.

Just to be clear, existing code, which uses 2d targets, will not be
affected by the change introduced in this PR and is still the preferred
way (IMO) to use regression in skorch.

Rejected solutions

I did consider the following solutions but rejected them.

Raising an error when shapes mismatch

This would remove the risk of users missing the warning. The problem
with this is that mismatching shapes can be okay in certain
circumstances. Some criteria don't expect target and prediction to have
the same shape, so we would need to check based on criterion. Moreover,
theoretically, users may indeed want to broadcast. Raising an error
would prevent that and users may have to resort to subclassing to
circumvent the error.

Automatic reshaping

We could automatically add/remove dimensions if we see that they
mismatch. This has the same problems as the previous solution regarding
the dependence on the type of criterion. Furthermore, automatic
adjustment of the user's output is prone to run into issues in some edge
cases (e.g. when the broadcasting is actually desired).

* Fix error when initializing BaggingRegressor

For Python 3.7, CI got:

TypeError: __init__() got an unexpected keyword argument 'estimator'

for BaggingRegressor. Probably it installs an older version of sklearn,
which uses a different argument name. Passing as positional arg should
fix it.

* Reviewer comment: typo

Co-authored-by: ottonemo <marian.tietz@ottogroup.com>

* Reviewer comment: typo

Co-authored-by: ottonemo <marian.tietz@ottogroup.com>

---------

Co-authored-by: ottonemo <marian.tietz@ottogroup.com>

---
## [qwerty2265/thaihana](https://github.com/qwerty2265/thaihana)@[7f10fa81ba...](https://github.com/qwerty2265/thaihana/commit/7f10fa81ba5b41441ff052f72a7d646c23779890)
#### Tuesday 2023-06-27 10:01:24 by Maks

Changed default css import to modules

i hate my life

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[74db193eff...](https://github.com/treckstar/yolo-octo-hipster/commit/74db193eff39fb52ce4cbc78848aeec3733d1150)
#### Tuesday 2023-06-27 11:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[221e82c364...](https://github.com/tgstation/tgstation/commit/221e82c3640c75d99dc2616bf666bd897b4a5be8)
#### Tuesday 2023-06-27 11:23:54 by ChungusGamer666

[NO GBP] Fixes my fuckups with species livers (#76331)

## About The Pull Request

Fixes https://github.com/tgstation/tgstation/issues/76329
I DID A REAL STUPID MISTAKE WHILE CODING
https://github.com/tgstation/tgstation/pull/76184 I AM SORRY
The signal was sending the fucking human instead of seconds_per_tick

## Why It's Good For The Game

Fixes a BUNCH of liver behavior including plasmamen livers not healing
wounds

## Changelog

:cl:
fix: Plasma will now heal plasmamen properly
/:cl:

---
## [lukasz-migas/napari](https://github.com/lukasz-migas/napari)@[3ec4be1ae8...](https://github.com/lukasz-migas/napari/commit/3ec4be1ae8eee50ab4912ba87981261cc94c075f)
#### Tuesday 2023-06-27 11:27:26 by Grzegorz Bokota

Incorret theme should not prevent napari from start (#5605)

# Description
<!-- What does this pull request (PR) do? Why is it necessary? -->
<!-- Tell us about your new feature, improvement, or fix! -->
<!-- If your change includes user interface changes, please add an
image, or an animation "An image is worth a thousand words!" -->
<!-- You can use https://www.cockos.com/licecap/ or similar to create
animations -->

For the current implementation, the error in theme registration prevents
the napari form from starting. It may be problematic for bundle users.

In this PR I add `try: ... except` to handle an error during theme
registration and convert it to logging exceptions. I use logging because
it happened before creating GUI.

## Type of change
<!-- Please delete options that are not relevant. -->
- [x] Bug-fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing
functionality to not work as expected)
- [ ] This change requires a documentation update

# References
<!-- What resources, documentation, and guides were used in the creation
of this PR? -->
<!-- If this is a bug-fix or otherwise resolves an issue, reference it
here with "closes #(issue)" -->

# How has this been tested?
<!-- Please describe the tests that you ran to verify your changes. -->
- [ ] example: the test suite for my feature covers cases x, y, and z
- [ ] example: all tests pass with my change
- [ ] example: I check if my changes works with both PySide and PyQt
backends
      as there are small differences between the two Qt bindings.  

Install `napari-gruvbox`, `pygments==2.6` (bellow 2.9) and start napari 

Example error message:
```python-traceback
11:52:01 ERROR Registration theme failed.
1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-dark provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
Traceback (most recent call last):
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 391, in _install_npe2_themes
    register_theme(theme.id, theme_dict, manifest.name)
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 266, in register_theme
    theme = Theme(**theme)
  File "/home/czaki/Projekty/napari/napari/utils/events/evented_model.py", line 200, in __init__
    super().__init__(**kwargs)
  File "pydantic/main.py", line 342, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-dark provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
11:52:01 ERROR Registration theme failed.
1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-light provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
Traceback (most recent call last):
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 391, in _install_npe2_themes
    register_theme(theme.id, theme_dict, manifest.name)
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 266, in register_theme
    theme = Theme(**theme)
  File "/home/czaki/Projekty/napari/napari/utils/events/evented_model.py", line 200, in __init__
    super().__init__(**kwargs)
  File "pydantic/main.py", line 342, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-light provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
```

## Final checklist:
- [ ] My PR is the minimum possible work for the desired functionality
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] I have added tests that prove my fix is effective or that my
feature works
- [ ] If I included new strings, I have used `trans.` to make them
localizable.
For more information see our [translations
guide](https://napari.org/developers/translations.html).

---------

Co-authored-by: Lorenzo Gaifas <brisvag@gmail.com>

---
## [ShawnZhong/linux](https://github.com/ShawnZhong/linux)@[88e4607034...](https://github.com/ShawnZhong/linux/commit/88e4607034ee49e09e32d91d083dced5c2f4f127)
#### Tuesday 2023-06-27 13:09:36 by Vladimir Sementsov-Ogievskiy

coredump: require O_WRONLY instead of O_RDWR

The motivation for this patch has been to enable using a stricter
apparmor profile to prevent programs from reading any coredump in the
system.

However, this became something else. The following details are based on
Christian's and Linus' archeology into the history of the number "2" in
the coredump handling code.

To make sure we're not accidently introducing some subtle behavioral
change into the coredump code we set out on a voyage into the depths of
history.git to figure out why this was O_RDWR in the first place.

Coredump handling was introduced over 30 years ago in commit
ddc733f452e0 ("[PATCH] Linux-0.97 (August 1, 1992)").
The original code used O_WRONLY:

    open_namei("core",O_CREAT | O_WRONLY | O_TRUNC,0600,&inode,NULL)

However, this changed in 1993 and starting with commit
9cb9f18b5d26 ("[PATCH] Linux-0.99.10 (June 7, 1993)") the coredump code
suddenly used the constant "2":

    open_namei("core",O_CREAT | 2 | O_TRUNC,0600,&inode,NULL)

This was curious as in the same commit the kernel switched from
constants to proper defines in other places such as KERNEL_DS and
USER_DS and O_RDWR did already exist.

So why was "2" used? It turns out that open_namei() - an early version
of what later turned into filp_open() - didn't accept O_RDWR.

A semantic quirk of the open() uapi is the definition of the O_RDONLY
flag. It would seem natural to define:

    #define O_RDWR (O_RDONLY | O_WRONLY)

but that isn't possible because:

    #define O_RDONLY 0

This makes O_RDONLY effectively meaningless when passed to the kernel.
In other words, there has never been a way - until O_PATH at least - to
open a file without any permission; O_RDONLY was always implied on the
uapi side while the kernel does in fact allow opening files without
permissions.

The trouble comes when trying to map the uapi flags onto the
corresponding file mode flags FMODE_{READ,WRITE}. This mapping still
happens today and is causing issues to this day (We ran into this
during additions for openat2() for example.).

So the special value "3" was used to indicate that the file was opened
for special access:

    f->f_flags = flag = flags;
    f->f_mode = (flag+1) & O_ACCMODE;
    if (f->f_mode)
            flag++;

This allowed the file mode to be set to FMODE_READ | FMODE_WRITE mapping
the O_{RDONLY,WRONLY,RDWR} flags into the FMODE_{READ,WRITE} flags. The
special access then required read-write permissions and 0 was used to
access symlinks.

But back when ddc733f452e0 ("[PATCH] Linux-0.97 (August 1, 1992)") added
coredump handling open_namei() took the FMODE_{READ,WRITE} flags as an
argument. So the coredump handling introduced in
ddc733f452e0 ("[PATCH] Linux-0.97 (August 1, 1992)") was buggy because
O_WRONLY shouldn't have been passed. Since O_WRONLY is 1 but
open_namei() took FMODE_{READ,WRITE} it was passed FMODE_READ on
accident.

So 9cb9f18b5d26 ("[PATCH] Linux-0.99.10 (June 7, 1993)") was a bugfix
for this and the 2 didn't really mean O_RDWR, it meant FMODE_WRITE which
was correct.

The clue is that FMODE_{READ,WRITE} didn't exist yet and thus a raw "2"
value was passed.

Fast forward 5 years when around 2.2.4pre4 (February 16, 1999) this code
was changed to:

    -       dentry = open_namei(corefile,O_CREAT | 2 | O_TRUNC | O_NOFOLLOW, 0600);
    ...
    +       file = filp_open(corefile,O_CREAT | 2 | O_TRUNC | O_NOFOLLOW, 0600);

At this point the raw "2" should have become O_WRONLY again as
filp_open() didn't take FMODE_{READ,WRITE} but O_{RDONLY,WRONLY,RDWR}.

Another 17 years later, the code was changed again cementing the mistake
and making it almost impossible to detect when commit
378c6520e7d2 ("fs/coredump: prevent fsuid=0 dumps into user-controlled directories")
replaced the raw "2" with O_RDWR.

And now, here we are with this patch that sent us on a quest to answer
the big questions in life such as "Why are coredump files opened with
O_RDWR?" and "Is it safe to just use O_WRONLY?".

So with this commit we're reintroducing O_WRONLY again and bringing this
code back to its original state when it was first introduced in commit
ddc733f452e0 ("[PATCH] Linux-0.97 (August 1, 1992)") over 30 years ago.

Signed-off-by: Vladimir Sementsov-Ogievskiy <vsementsov@yandex-team.ru>
Message-Id: <20230420120409.602576-1-vsementsov@yandex-team.ru>
[brauner@kernel.org: completely rewritten commit message]
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Christian Brauner <brauner@kernel.org>

---
## [friday-pagamentos/evals](https://github.com/friday-pagamentos/evals)@[f5844592f1...](https://github.com/friday-pagamentos/evals/commit/f5844592f13eff8e7b9927d5cec0d2627694d9d9)
#### Tuesday 2023-06-27 14:26:08 by Ali-consensus

Eval: Consensus Summary (#1140)

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
Consensus Summary

### Eval description

Utilize the model's ability to produce a Scientific Consensus in
response to a scientific inquiry using the provided claims.

### What makes this a useful eval?

This is a useful eval because it evaluates the model's ability to
produce a scientific consensus in response to a given set of claims.
This is important because scientific consensus is the result of multiple
studies and data that may or may not support the same conclusion. A
model that can accurately produce scientific consensus can help in
making informed decisions and policies based on scientific evidence.
Hence, evaluating a model's ability to produce a scientific consensus
using the Consensus Summary eval can be useful in assessing its
reliability and potential for practical applications.

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
{"input": [{"role": "system", "content": "Generate a brief answer using
only the provided claims, with no personal opinions or outside
knowledge. If there is no answer based on the claims, write 'N-A'."},
{"role": "user", "content": "claim: Two doses of mRNA covid-19 vaccines
were observed to be highly effective against symptomatic infection and
severe outcomes.\nclaim: COVID-19 vaccines currently authorized in the
United States are highly effective in preventing COVID-19-associated
hospitalizations in older adults.\nclaim: In summary, vaccines are a
powerful tool that can be used to control the COVID-19 pandemic, with
high efficacy and tolerable ADRs.\nclaim: Conclusion Overall, we
conclude that vaccination against COVID-19 in patients with active
malignancies using activated and inactivated vaccines is a safe and
tolerable procedure that is also accompanied by a high efficacy.\nclaim:
COVID-19 vaccines provide good protection against COVID-19 presentation
at primary care/outpatient level, particularly among fully vaccinated
individuals.\nquestion: are covid-19 vaccines effective?"}], "ideal":
"Summary: Covid-19 vaccines are highly effective at protecting against
infection and hospitalization."}
{"input": [{"role": "system", "content": "Generate a brief answer using
only the provided claims, with no personal opinions or outside
knowledge. If there is no answer based on the claims, write 'N-A'."},
{"role": "user", "content": "claim: Lower zinc is a hallmark of
depression, while increments in serum zinc and attenuation of the
immune-inflammatory response during treatment appear to play a role in
the clinical efficacy of sertraline.\nclaim: An increase in dietary zinc
and higher plasma zinc levels may reduce the risk of depressive
symptoms.\nclaim: Although decreased zinc levels have been implicated in
the genesis of depression in animal models and in major depressive
disorder in humans, this study provides the first evidence of a role for
zinc in depression in people with dementia and highlights zinc
metabolism as a therapeutic target.\nclaim: The results of this study
show that long-term intake of zinc may modulate symptoms of
depression.\nclaim: The reported results indicated that the serum zinc
level might be a marker of depression as a state (state marker) in
treatment responsive patients.\nquestion: can zinc help treat
depression?"}], "ideal": "Summary: All of these studies suggest that low
zinc levels are a marker of depression and that intake of zinc may have
the ability to help reduce symptoms of depression"}
{"input": [{"role": "system", "content": "Generate a brief answer using
only the provided claims, with no personal opinions or outside
knowledge. If there is no answer based on the claims, write 'N-A'."},
{"role": "user", "content": "claim: The findings suggest that the
following characteristics of the founder significantly influence the
success potential of an incubated venture: entrepreneurial personality,
motivation for starting the venture, managerial skills, and approach
towards innovation.\nclaim: Using a sample of 384 entrepreneurs selected
from the two leading business districts in Uganda, we observe that
optimism is the component of psychological capital that significantly
moderates the relationship between startup capital and entrepreneurial
success.\nclaim: Both startup capital and psychological capital are
significant predictors of entrepreneurial success; however,
psychological capital is the better predictor.\nclaim: Entrepreneurially
self\u2010efficacious founder/managers may help improve the performance
of very young firms but such benefits dissipate over time.\nclaim: This
finding indicates that the entrepreneurial team\u2019s startup
experience plays stronger roles in venturing profitable startups when
the amount of financial resources and initial firm size are small;
however, the team\u2019s startup experience and intangible resources
have positive interaction effects on new-born startups\u2019
profitability.\nquestion: what predicts success as a startup
founder?"}], "ideal": "Summary: Things like entrepreneurial personality,
motivation for starting the venture, managerial skills, previous
start-up experience, startup and psychological capital and optimism all
predict success as a startup founder"}
{"input": [{"role": "system", "content": "Generate a brief answer using
only the provided claims, with no personal opinions or outside
knowledge. If there is no answer based on the claims, write 'N-A'."},
{"role": "user", "content": "claim: While homelessness is ultimately the
result of a severe and chronic shortage of affordable housing, creating
accessible, safe, pet-friendly shelter and safe haven options and
instituting a smoother, more transparent process for moving from the
streets could substantially reduce street homelessness.\nclaim: - To
prevent the revolving door to homelessness, it is necessary to remove
the barriers that hinder access to normal health resources which are
experienced by people suffering from social exclusion, while
implementing ongoing support programmes for homeless people or those at
risk of homelessness, which primarily deal with health issues.\nclaim:
We conclude that overcoming homelessness requires policies and practices
that give a greater focus to non-material aspects of homelessness
through an emphasis on empowerment, self-respect and autonomy.\nclaim:
This finding suggests that homelessness can be reduced by appropriate
clinical interventions if housing is available.\nclaim: For homelessness
prevention, systematic and outreach social medical care before and
during homelessness should be provided.\nquestion: What are effective
ways to prevent homelessness?"}], "ideal": "Summary: Ways to prevent
homelessness include creating accessible, safe shelter and safe haven
options, removing barriers to health resources, giving a greater focus
to non-material aspects of homelessness, and providing systematic and
outreach social medical care."}
{"input": [{"role": "system", "content": "Generate a brief answer using
only the provided claims, with no personal opinions or outside
knowledge. If there is no answer based on the claims, write 'N-A'."},
{"role": "user", "content": "claim: While homelessness is ultimately the
result of a severe and chronic shortage of affordable housing, creating
accessible, safe, pet-friendly shelter and safe haven options and
instituting a smoother, more transparent process for moving from the
streets could substantially reduce street homelessness.\nclaim: - To
prevent the revolving door to homelessness, it is necessary to remove
the barriers that hinder access to normal health resources which are
experienced by people suffering from social exclusion, while
implementing ongoing support programmes for homeless people or those at
risk of homelessness, which primarily deal with health issues.\nclaim:
We conclude that overcoming homelessness requires policies and practices
that give a greater focus to non-material aspects of homelessness
through an emphasis on empowerment, self-respect and autonomy.\nclaim:
This finding suggests that homelessness can be reduced by appropriate
clinical interventions if housing is available.\nclaim: For homelessness
prevention, systematic and outreach social medical care before and
during homelessness should be provided.\nquestion: How to prevent
homelessness?"}], "ideal": "Summary: Ways to prevent homelessness
include creating accessible, safe shelter and safe haven options,
removing barriers to health resources, giving a greater focus to
non-material aspects of homelessness, and providing systematic and
outreach social medical care."}
{"input": [{"role": "system", "content": "Generate a brief answer using
only the provided claims, with no personal opinions or outside
knowledge. If there is no answer based on the claims, write 'N-A'."},
{"role": "user", "content": "claim: The findings revealed that the
factor that contributes the most to entrepreneurship intention is Locus
of control, followed by Need of Achievement and Subjective
Norms.\nclaim: It was found that entrepreneurial skill, environmental
factors and entrepreneurial orientation have a positive influence on
entrepreneurial intention.\nclaim: The findings indicate that
entrepreneurial motivation has a significant correlation with
entrepreneurial intention and its three determinants, social valuation
of entrepreneurship, having entrepreneurial role models, knowledge of
entrepreneurial support and perceived barriers to starting a
business.\nclaim: Research finding revealed that entrepreneurial
intention is indirectly affected by entrepreneurship education, meaning
that students\u2019 entrepreneurial motivation and attitude are two
important mediating variables.\nclaim: Findings confirm the influence of
individual and socio-cultural factors on entrepreneurial
intention.\nquestion: What are the factors of entrepreneurship
intention"}], "ideal": "Summary: Studies find that intrinsic factors,
such as entrepreneurial skill and motivation, as well as extrinsic
variables, such as the environmental support of entrepreneurship,
mediate entrepreneurship intention."}
{"input": [{"role": "system", "content": "Generate a brief answer using
only the provided claims, with no personal opinions or outside
knowledge. If there is no answer based on the claims, write 'N-A'."},
{"role": "user", "content": "claim: The results show that digital
agriculture is able to help users to increase productivity in a
sustainable way.\nclaim: Digital agriculture technologies continue the
centralization of economic knowledge and power as they facilitate the
transformation of vast territories into \u201coperational
landscapes\u201d that provide the material, energy, and labor for a
rapidly expanding urban system.\nclaim: The digital agriculture system
is an effective tool for insurance industry to use to develop a
dynamical business plan for the changing climate.\nclaim: The technical
fitting-out of agriculture in the digital economy should be considered
as a set of measures to prepare the industry for the production of
high-quality products, which implies the use of digital technologies
that minimize human participation in the production process.\nclaim:
Consequently, the initial Mobile-based Information System evolved into a
Digital Knowledge Ecosystem that can predict current production
situation in near real enabling government agencies to dynamically
adjust the incentives offered to farmers for growing different types of
crops to achieve sustainable agriculture production through crop
diversification.\nquestion: What is digital agriculture?"}], "ideal":
"Summary: N-A"}
  ```
</details>

---
## [friday-pagamentos/evals](https://github.com/friday-pagamentos/evals)@[f34bb67d18...](https://github.com/friday-pagamentos/evals/commit/f34bb67d18cb07c6a68ae7c3871e82814df0863f)
#### Tuesday 2023-06-27 14:26:08 by Drax

[evals] add ascii-art-digit-recognition (#509)

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
ascii-digit-recognition

### Eval description

Tests the LLMs' ability to recognize digits [0-9] as ASCII arts
(creating images using letters, numbers, and symbols from the ASCII
character set).

### What makes this a useful eval?

Language seems to be a one-dimensional sequence while images are
two-dimensions. Therefore, recognizing 2d images (simple ASCII art) is a
difficult task intuitively, requiring a certain degree of spatial
imagination ability (my opinion). GPT3.5 (30%) and GPT3-DaVinci (20%)
suffer from the task. It would be interesting to see the performance of
GPT-4.

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
{"input": [{"role": "system", "content": "You are an assistant capable
of recognizing ASCII art digits. Your response only contains a single
digit."}, {"role": "system", "content": "What is the digit in the
following ASCII art?\n ``` aa \na a \n a \n a \n a \n a \n aaaa\n```
Answer only a single digit.", "name":"example_user"},
{"role":"system","content":"1","name":"example_assistant"}, {"role":
"user", "content": "what is the digit in the following ASCII art?\n ```
aaaaa \na a\na a\na a\na a\na a\n aaaaa``` Answer only a single
digit."}], "ideal": "0"}
{"input": [{"role": "system", "content": "You are an assistant capable
of recognizing ASCII art digits. Your response only contains a single
digit."}, {"role": "system", "content": "What is the digit in the
following ASCII art?\n ``` aa \na a \n a \n a \n a \n a \n aaaa\n```
Answer only a single digit.", "name":"example_user"},
{"role":"system","content":"1","name":"example_assistant"}, {"role":
"user", "content": "what is the digit in the following ASCII art?\n ```
a \n aa \na a \n a \n a \n a \n aaaaa``` Answer only a single digit."}],
"ideal": "1"}
{"input": [{"role": "system", "content": "You are an assistant capable
of recognizing ASCII art digits. Your response only contains a single
digit."}, {"role": "system", "content": "What is the digit in the
following ASCII art?\n ``` aa \na a \n a \n a \n a \n a \n aaaa\n```
Answer only a single digit.", "name":"example_user"},
{"role":"system","content":"1","name":"example_assistant"}, {"role":
"user", "content": "what is the digit in the following ASCII art?\n
```aaaaa\n a\n a\naaaaa\na \na \naaaaa ``` Answer only a single
digit."}], "ideal": "2"}
{"input": [{"role": "system", "content": "You are an assistant capable
of recognizing ASCII art digits. Your response only contains a single
digit."}, {"role": "system", "content": "What is the digit in the
following ASCII art?\n ``` aa \na a \n a \n a \n a \n a \n aaaa\n```
Answer only a single digit.", "name":"example_user"},
{"role":"system","content":"1","name":"example_assistant"}, {"role":
"user", "content": "what is the digit in the following ASCII art?\n
```aaaaa\n a\n a\n aaaa\n a\n a\naaaaa ``` Answer only a single
digit."}], "ideal": "3"}
{"input": [{"role": "system", "content": "You are an assistant capable
of recognizing ASCII art digits. Your response only contains a single
digit."}, {"role": "system", "content": "What is the digit in the
following ASCII art?\n ``` aa \na a \n a \n a \n a \n a \n aaaa\n```
Answer only a single digit.", "name":"example_user"},
{"role":"system","content":"1","name":"example_assistant"}, {"role":
"user", "content": "what is the digit in the following ASCII art?\n ```a
a\na a\na a\naaaaa\n a\n a\n a ``` Answer only a single digit."}],
"ideal": "4"}
  ```
</details>

Some visualization of the ASCII arts: 

![image](https://user-images.githubusercontent.com/52069185/228619558-40e3c004-9c65-495f-89a8-68d80f241f44.png)

---
## [friday-pagamentos/evals](https://github.com/friday-pagamentos/evals)@[73c8a178e6...](https://github.com/friday-pagamentos/evals/commit/73c8a178e69418760baee8983daa19fb492e9231)
#### Tuesday 2023-06-27 14:26:08 by somerandomguyontheweb

Add Belarusian rhyme eval (#1143)

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

belarusian-rhyme

### Eval description

Test the model's ability to find rhyming words in Belarusian.

### What makes this a useful eval?

This eval is inspired by similar submissions for
[Hebrew](https://github.com/openai/evals/pull/176),
[Russian](https://github.com/openai/evals/pull/708),
[Ukrainian](https://github.com/openai/evals/pull/867),
[Finnish](https://github.com/openai/evals/pull/970), and
[Italian](https://github.com/openai/evals/pull/1003). The dataset
contains 50 pairs of English nouns whose Belarusian translations rhyme,
and another 50 pairs consisting of the same nouns but reordered, so that
in each of these additional pairs there aren't any Belarusian
translations that rhyme. The model's task is to output the rhyming pair
of Belarusian words or NONE. The rhyming pairs have been manually
picked, and many of them contain at least one word distinctive of
Belarusian, i.e. not attested in closely related Russian and Ukrainian
languages.

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
{"input": [{"role": "system", "content": "For each pair of words,
determine whether some of their Belarusian translations rhyme. If they
do, output the pair of rhyming words in Belarusian. If not, output
NONE."}, {"role": "user", "content": "grass, church"}], "ideal":
["трава, царква", "царква, трава"]}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether some of their Belarusian translations rhyme. If they
do, output the pair of rhyming words in Belarusian. If not, output
NONE."}, {"role": "user", "content": "food, tower"}], "ideal": ["ежа,
вежа", "вежа, ежа"]}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether some of their Belarusian translations rhyme. If they
do, output the pair of rhyming words in Belarusian. If not, output
NONE."}, {"role": "user", "content": "grass, food"}], "ideal": "NONE"}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether some of their Belarusian translations rhyme. If they
do, output the pair of rhyming words in Belarusian. If not, output
NONE."}, {"role": "user", "content": "church, tower"}], "ideal": "NONE"}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether some of their Belarusian translations rhyme. If they
do, output the pair of rhyming words in Belarusian. If not, output
NONE."}, {"role": "user", "content": "foot, queue"}], "ideal": ["нага,
чарга", "чарга, нага"]}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether some of their Belarusian translations rhyme. If they
do, output the pair of rhyming words in Belarusian. If not, output
NONE."}, {"role": "user", "content": "boat, flood"}], "ideal": ["лодка,
паводка", "паводка, лодка"]}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether some of their Belarusian translations rhyme. If they
do, output the pair of rhyming words in Belarusian. If not, output
NONE."}, {"role": "user", "content": "foot, boat"}], "ideal": "NONE"}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether some of their Belarusian translations rhyme. If they
do, output the pair of rhyming words in Belarusian. If not, output
NONE."}, {"role": "user", "content": "queue, flood"}], "ideal": "NONE"}
  ```
</details>

---
## [Opentrons/opentrons](https://github.com/Opentrons/opentrons)@[5271d4fbc4...](https://github.com/Opentrons/opentrons/commit/5271d4fbc473bb8f2506a90b2c929535c82892f6)
#### Tuesday 2023-06-27 14:39:09 by Seth Foster

feat(api,shared-data): error codes in PE (#12936)

On the python side of our code, we want our new enumerated exceptions to
be gradually integratable, and we also want to make sure that any errors
that we didn't yet get the chance to give error codes end up with error
codes. To do this in a programmatic way, we can add some automated
methods for wrapping python exceptions.

All enumerated errors now get to wrap errors. These are optional
sequences of more enumerated errors that are considered to have caused
the top-level one - in most cases, this will be because the enumerated
error explicitly was instantiated to wrap a python exception, but it
could also be if it was raised from one.

Since we only wrap other enumerated errors, we need a way to make
exceptions enumerated errors. A new exception type (but not code - it's
just a GeneralError) called PythonException has this capability; it lets
you give it BaseExceptions in addition to other EnumeratedErrors, and
it's capable of walking the python memory model internals to try and get
the other exceptions in a stack of raise from ... raise from ... calls
that are reasonably popular in our code. This is functionality that is
promoted out of The Dunder Zone in python 3.11, so I feel pretty good
using it (this is what ExceptionGroups are).

So now, as in the tests, if you catch an exception and give it to a
PythonException you bless it with an error code and save all the
exceptions and their stack traces for later inspection. Cool!

ProtocolEngine is the first place we'll go through and add places that
actually use these error codes, since it's in a lovely high-leverage
middle spot in our stack. That means we both get to test the upward
interface of how these things will be represented in the HTTP API and
how they'll be created from lower exceptions.

ProtocolEngine already has its own very large and robust set of custom
exceptions, which is awesome. We can make them inherit from the
enumerated errors pretty easily, but unfortunately we have to add a
bunch of stuff to their constructors to pass along things like the
ability to wrap other exceptions and so on. Luckily that's just typing.

Once we've done that, at the three points we catch all missed exceptions
we have to switch over to creating the new style. ProtocolEngineErrors
get passed on; uncaught legacy errors get captured as PythonExceptions;
and uncaught errors in the normal core do too.

Finally, we have to represent this new style of error in the
ErrorOccurrence objects. This is the fun part. Previously, we'd added
error codes to those objects; this was sort of a big deal because we
want them to be required when you make new ErrorOccurrences and when
clients look, but we don't want things to break when we deserialize old
ones. We can extend that trick pretty easily to add new things. What's
not quite as easy is this concept of wrapping errors. Our errors are now
essentially trees, and we need tree structure here. Luckily, jsonschema
and pydantic are actually pretty good at type-recursive schema and
object definitions, so we can plop a list of other error occurrences in
there.

Now, when we catch one of these errors that's bubbled up from hardware,
we give it a name and we capture its entire history in an inspectable
way, and I think that's really cool.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[eb210fea0b...](https://github.com/treckstar/yolo-octo-hipster/commit/eb210fea0bab024d7bc0e486a7ab92f6cf64adba)
#### Tuesday 2023-06-27 16:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Aquizit/Yogstation](https://github.com/Aquizit/Yogstation)@[465aef0da1...](https://github.com/Aquizit/Yogstation/commit/465aef0da1b967bf7cb008e7906f5791d81b89cd)
#### Tuesday 2023-06-27 17:15:22 by Cark

Some minor changes to space syndicate base. (#19282)

* syndiebuff

* fuck you airlock

* fucking AIRLOCK CONTROLLERS

---
## [NOAA-GFDL/fre-python-tools](https://github.com/NOAA-GFDL/fre-python-tools)@[d9e89ab238...](https://github.com/NOAA-GFDL/fre-python-tools/commit/d9e89ab238b9786574c7dba37415d423aab260bd)
#### Tuesday 2023-06-27 17:17:41 by Ian Laflotte

computing standard deviation of the mean, in addition to the average now, weighted and unweighted. should probably be functions. should probably have a class, actually...

compares averages with `timavg.csh` as well. comparison good to ~8 decimal places. not expecting to reproduce bit-wise, but i think we're not at the machine-precision level yet with the numerics anyways, so i think my averaging/stddev routine is missing something. haven't compared to std deviation computation from `timavg.csh` yet, but I should.

Too slow. for loops. need to look at iterators, parallelism, comprehension, and other methods to speed up. i hear generator functions help a lot, but I just don't understand how/why that could possibly make a difference.

function argument I/O needs to catch up a little bit. important but not urgent yet, call it a quality of life effort soon, though.

some #'s:
```
calling main())

calling generate time averages
calling generate_frepythontools_timavg for file: ./testfiles/atmos.197901-198312.LWP.nc
isMasked=False
type of val_array=<class 'numpy.ma.core.MaskedArray'>
type of avgvals  =<class 'list'>
time_bnds entry type is:  <class 'numpy.float64'>
val_array entry type is:  <class 'numpy.float32'>
avgvals entry   type is:  <class 'numpy.float32'>
avgvals[0][0][0]        =         0.000846405307367399 +/- 6.142338163576247e-06
type(stddevs[0][0][0])=<class 'numpy.float64'>
type(avgvals[0][0][0])=<class 'numpy.float64'>
compare_avgvals[0][0][0]=         0.0008464052807539701

 done calling main()
Finished in 162.06 second(s)
```

---
## [mc776/freedoom](https://github.com/mc776/freedoom)@[ff687ed49a...](https://github.com/mc776/freedoom/commit/ff687ed49aba65ce761a33507930ac0d4d992a00)
#### Tuesday 2023-06-27 17:30:50 by mc776

level: more fixes.

E1M3
- Minor item floating in one of the staircases.

E1M7
- Widened the item trenches in the northwest switch room to minimize the chance of a floating item.
- Narrowed the water trench in the southeast switch area to prevent someone from squeeze-gliding in.

E1M9
- Funny-shaped nukage bridge no longer has visible switches. Instead, that railing can be used from the outside anywhere along any of the long sides to lower it.
- Door on the north of that bridge was missing a doortrak.

E3M5
- Northeast giant blood pit had floating items in the new ledges. (Those bits are now also 100% pure meat instead of the rocky crust on top.)

E4M4
- Secret in the southwest is now the room instead of the doorway. Lighting adjusted accordingly.

E4M5
- There's an obscured lamp in the northwest that's supposed to look (in id) like a small lamp placed on top of the box. Freedoom's yellow lamp doesn't work for this, but Freedoom's candle sprite is perfect for the intended effect, so now it is that instead.

E4M6
- Various thin secrets.

E4M7
- Thing no. 580 was the wrong type and bled into the ceiling (see #941). The blocking version is now used instead.

E4M8
- The secrets by the starting area are now the rooms themselves instead of the doorways.

Map11
- Untagged the lizardbaby-triggered doorway as secret.
- All lizard baby sectors are now 72 units tall.
- Realigned the vines in the trilobite corridors overlooking the western atrium.
- Berserk red key secret room lengthened to guarantee having to step inside it.
- Red key is now at a different location, the platform now being a teleporter to it, allowing the location of the red key to be a single sector that can be flagged as a secret.
- Replaced the light source in the yellow skull room with something less likely to have already fallen over.
- Replaced the evil eyes with tech lamps since those aren't shootable.
- The trigger for releasing the pain bringers in the nukage fountain is once again a walk line.

Map16
- Every sector in the backpack secret was tagged as secret, leaving a total of 3 secrets one of which was skippably thin. The skippable is now untagged.

Map18
- It was possible to squeeze into the blue key pillar to trigger the ambush prematurely. The pillar is now the entire 64x64 platform.

---
## [Huge/openai-LLM-evals](https://github.com/Huge/openai-LLM-evals)@[d708a6be26...](https://github.com/Huge/openai-LLM-evals/commit/d708a6be261bfcb04962e64969164d737ba3972c)
#### Tuesday 2023-06-27 17:45:06 by dougkwanna

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
## [JheffersonMarques/CC-Tweaked](https://github.com/JheffersonMarques/CC-Tweaked)@[8fe509ecb1...](https://github.com/JheffersonMarques/CC-Tweaked/commit/8fe509ecb1a941d58a417a8da29e3de142a57328)
#### Tuesday 2023-06-27 17:48:03 by Jonathan Coates

Properly scope IArguments to the current function call

This is a horrible commit: It's a breaking change in a pretty subtle
way, which means it won't be visible while updating. Fortunately I think
the only mod on 1.19.4 is Plethora, but other mods (Mek, Advanced
Peripherals) may be impacted when they update. Sorry!

For some motivation behind the original issue:

The default IArguments implementation (VarargArguments) lazily converts
Lua arguments to Java ones. This is mostly important when passing tables
to Java functions, as we can avoid the conversion entirely if the
function uses IArguments.getTableUnsafe.

However, this lazy conversion breaks down if IArguments is accessed on a
separate thread, as Lua values are not thread-safe. Thus we need to
perform this conversion before the cross-thread sharing occurs.

Now, ideally this would be an implementation detail and entirely
invisible to the user. One approach here would be to only perform this
lazy conversion for methods annotated with @LuaFunction(unsafe=true),
and have it be eager otherwise.

However, the peripheral API gets in the way here, as it means we can no
longer inspect the "actual" method being invoked. And so, alas, this
must leak into the public API.

TLDR: If you're getting weird errors about scope, add an
IArguments.escapes() call before sharing the arguments between threads.

Closes #1384

---
## [ChloeTheBitch/FakeDeafenBD](https://github.com/ChloeTheBitch/FakeDeafenBD)@[93c9dd8393...](https://github.com/ChloeTheBitch/FakeDeafenBD/commit/93c9dd83938fb5f6d6597f8b7447847151324050)
#### Tuesday 2023-06-27 20:11:23 by Chloe

Update FakeDeafen.plugin.js

I still can't figure out how to change the Trigger key but at least I got somewhat closer, the button works now. I hate my life and I hate JS even more.

---
## [JoeBidenWhatAreYouHiding/kx](https://github.com/JoeBidenWhatAreYouHiding/kx)@[7629102229...](https://github.com/JoeBidenWhatAreYouHiding/kx/commit/7629102229e1ad9244a732545c677ae00d24c8d3)
#### Tuesday 2023-06-27 20:33:22 by daddydevito21

I want you to find this nancy-boy Ricca the Rat, I want him DEAD! I want his family DEAD! I want his house burned to the GROUND! I wanna go there in the middle of the night and I wanna piss on his ashes!

---
## [bhattarai333/DostoyevskyCloner](https://github.com/bhattarai333/DostoyevskyCloner)@[13cf5900c7...](https://github.com/bhattarai333/DostoyevskyCloner/commit/13cf5900c73d5cafc7a21c69b352f07b6e7dbb10)
#### Tuesday 2023-06-27 20:59:01 by Josh Bhattarai

Splitting the training sequences on spaces has drastically improved performance, still need to figure out where the exclamation marks are coming from

Example output:

Once upon a time, as it were, he would say to himself, “I’ve come to see you,” and that would be the end of it. But he did not know what to do with himself. He knew that he was in a state of great anxiety, and would not allow himself to be in such a position for a long time. At the same time he could not help thinking that it was impossible for him to make up his mind to go on living like this. It seemed to him that there was a great deal of uncertainty about his future, but that at the very moment when he had to decide whether to live or not, it seemed as though he were at a loss for words. In spite of all this uncertainty and uncertainty, however, the fact was that, on the day of his departure from Petersburg, Nikolay Vsyevolodovitch had not yet left the town, nor had he even begun to think of the possibility of living in Petersburg. This was the first time in his whole life that the idea had been thought up, so to speak, in the most mysterious and perplexing way. And yet, at that moment, when the old man had no idea of what he wanted to talk about at all, yet had only a vague idea as to what it would mean for the future of him and his family, this idea suddenly came into his head. The idea was, of course, very strange indeed; but it must be remembered that in that very instant the young man, who had never even thought of such an idea before, had, indeed, a definite and definite idea in him, which, if it had existed at once, would have made him so happy and so proud of himself that even the slightest hint of!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!....!!!!!!!!!!!!!!!!!.!!!!!!!!!!!:!!!,!.,!.;!;!,!.!%;!:!,—!.—!—!“! —! ‘What do you mean, what do I mean to say? What are you saying to me, my dear friend? I am not saying anything to you; I have no intention of telling you anything. I only wish to tell you that you are a man of good character and good manners. You must know, gentlemen, that I do not intend to

---
## [0mis/lora-svc](https://github.com/0mis/lora-svc)@[2bc3141e8d...](https://github.com/0mis/lora-svc/commit/2bc3141e8d1c8635c66905e46f9074bff426dfd4)
#### Tuesday 2023-06-27 21:03:10 by niiyaq

Update svcgui.py

I'm happy to announce that I have made some improvements and added some new features to the SVC GUI module. Here is a summary of what's new:

- The code now uses the `os.path` module to construct the path to the data_svc/singer directory, instead of hard-coding it. This makes the code more flexible and adaptable to different locations of the lora-svc folder, as long as you run the code from within it. Now, when you select the spk file, the file dialog should open in the singer folder by default.
- The code now uses the `playsound` module to play the output file, instead of using subprocess and gst-launch-1.0. This makes the code more portable and compatible with different platforms and configurations. The `playsound` module uses GStreamer on Linux, AppKit on macOS, and winsound on Windows to play audio files.
- The code now handles exceptions and errors more gracefully, using logging and message boxes. The code logs the status and results of each step of the SVC process, as well as any exceptions or errors that occur. The code also displays error messages using tkinter message boxes, if something goes wrong during the SVC process or the playback of the output file.

I hope you enjoy these new features and find them useful. Please feel free to try them out and give me your feedback or suggestions. Thank you for your support and interest in this project.

Here is a possible explanation of how to stop some common bugs and errors:

---

Some of you may encounter some bugs or errors when running the SVC GUI module. Here are some possible solutions and tips to avoid them:

- If you get an error like `ModuleNotFoundError: No module named 'playsound'`, it means that you don't have the `playsound` module installed on your system. You can install it using pip by running this command:

```bash
pip install playsound
```

- If you get an error like `ValueError: Namespace Gst not available`, it means that you don't have the GStreamer library or its Python bindings installed on your system. You can install them using apt-get by running these commands:

```bash
sudo apt-get install libgstreamer1.0-dev
sudo apt-get install python3-gst-1.0
sudo apt-get install gstreamer1.0-tools gir1.2-gstreamer-1.0
```

I hope this helps you troubleshoot and fix some common bugs and errors. If you encounter any other issues, please let me know and I will try to help you as soon as possible.

Best regards,

---
## [Michaelmanicotti/poetry](https://github.com/Michaelmanicotti/poetry)@[d2e2302ada...](https://github.com/Michaelmanicotti/poetry/commit/d2e2302ada3f50756356b9ef9fed51ba4d2e3a49)
#### Tuesday 2023-06-27 21:10:54 by Michaelmanicotti

Update  Movement III | To the pretty boy I can't stop writing poems about, Fuck You

---
## [PlagueVonKarma/kep-hack](https://github.com/PlagueVonKarma/kep-hack)@[83483f035b...](https://github.com/PlagueVonKarma/kep-hack/commit/83483f035bce18af2959b7e01872154c5ac97912)
#### Tuesday 2023-06-27 21:17:12 by Llinos Evans

The Great Constant Compression of June 2023

This is a large-scale compression of KEP's current hide/show constants. RBY's works extremely oddly and is limited to 256 entries.

The problem with how RBY's hide/show stuff works, is that even though there are tons of unused constants, you...can't actually remove them. The constant list is tied to the hide/show data entries, so if you replace it with something else, well, now you just have two objects tied to the same constant. If you made the Route 2 item a boss, and someone picked up the item on Route 2, the boss would also disappear, and vice versa. So, we have to get creative.

I have reduced what we have to 248, but I think I miscounted when doing the funny list somewhere in the actual list when making sure the hex stuff is ok. Either that, or there's an error somewhere that Martha will, by some obscene miracle of humanity, discover. Anyway, this was achieved by turning multiple current overworld items into hidden ones, keeping them in the game whilst keeping to that all-important limit.

I also removed the items in Pokemon Tower 4F for this, just needed a little boost. Well, as you can see by the number, I technically didn't, I just miscounted like 20 times. Look, it's 10:11 PM, my stomach is in pain from an insane injection, and I don't even know if that map will come back, cut me some slack. Or add it back. You definitely can.

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[c4b550c1a9...](https://github.com/Paxilmaniac/Skyrat-tg/commit/c4b550c1a94670ae333df12b8200ff33f7f7f175)
#### Tuesday 2023-06-27 22:04:09 by SkyratBot

[MIRROR] New Wizard spell "branch": Vendormancy [MDB IGNORE] (#22008)

* New Wizard spell "branch": Vendormancy (#75679)

## About The Pull Request
New item for wizards, ~~the Staff~~ Scepter of Runic Vendormancy.

With it, you can summon Runic Vending machines to block your enemies,
push them 2 tiles back around the summoning tile, throw the vendors 4
tiles away to squash them or simple detonate the vendors for direct
damage against enemies within a 2 tile range.

The scepter has 3 charges that can be recharged after a "long" channel
so while powerful, it is a tactical weapon and wizards can't directly
steamroll the crew with endless vendors. (Unless they buy multiple
scepters, but that is just funny.)

Also, there is a bug with the throw... I copied how baseball bats deal
with knockback, but they consistently don't push the vendors back, just
spin them on the same tile... I appreciate if anyone has any idea on how
to fix or change that to a better system.

## New changes I made
The vendor has a random set of REAL wizard robes and hat, sandals and a
foam vendor scepter as products to sell now.
This gives the crew some real armor, and if it is considered too much, I
can swap it for the fake versions.
IMO the real clothes work as the perfect bait for the crew to approach
the vendors and get exploded in the process, and while a random
assistant might get real wizard armor to go valid hunt the wizard, the
crew might just mistake them for the real wizard and beat them to death,
which is too funny.
## Why It's Good For The Game

![vendormancerPR](https://github.com/tgstation/tgstation/assets/55374212/f9d98f3e-5916-4a17-987e-249f4cdb7185)

About a year ago I played Stoneshard, and it has such an amazing
Geomancy Wizard that I wanted to port some of its gameplay to SS13 as
our wizards, while funny and destructive, are kinda simple to play...

Summoning and blowing up rocks was nice, but I randomly had the idea of
summoning Vendors while at work and vendors squashing people has become
such an iconic SS13 thing to me that I had to stop being lazy and start
working on this.

Something, something, enviromental combat wizard.
## Changelog
Gonna polish the changelog later too...
:cl: Guillaume Prata
add: New Wizard spell branch: Vendormacy! Summon runic vending machines
with your Vending Scepter, force push them on your enemies to squish
them or blow them up while they are busy buying from the machines.
/:cl:

---------

Co-authored-by: Time-Green <7501474+Time-Green@ users.noreply.github.com>

* New Wizard spell "branch": Vendormancy

---------

Co-authored-by: GuillaumePrata <55374212+GuillaumePrata@users.noreply.github.com>
Co-authored-by: Time-Green <7501474+Time-Green@ users.noreply.github.com>

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[362cd0c223...](https://github.com/git-for-windows/git/commit/362cd0c223b9f2947f4548679c1a15c0edc2e516)
#### Tuesday 2023-06-27 22:10:32 by Johannes Schindelin

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
## [jeremybanka/corners](https://github.com/jeremybanka/corners)@[0e73c723d7...](https://github.com/jeremybanka/corners/commit/0e73c723d7b59596b82ee46546ef36faa76bdd05)
#### Tuesday 2023-06-27 22:43:50 by Peter Banka

Peba/docs site in www (#112)

* 🔨 add preformatted codegen script
* 🎉 working emotion-swc template...
* ✨ rendering with emotion and mdx and corners. trouble with codecomponent
* ✨ Rendering actual shit we like
* 🚚 slide our new stuff into place
* 🎉 fucken rendered

---------

Co-authored-by: Jeremy Banka <hello@jeremybanka.com>

---
## [Finxx1/TEiN-Anni-6](https://github.com/Finxx1/TEiN-Anni-6)@[8051f7aa31...](https://github.com/Finxx1/TEiN-Anni-6/commit/8051f7aa314ac6c4e5bccfcb72cc377f4d6ebd38)
#### Tuesday 2023-06-27 23:10:04 by SurrealDude

+ Pain, and suffering

First pre-release patch. This fixes many of the issues found while playtesting (both on my own and on ice's stream), such as:
+ Gehenna missing particles and sounds.
+ 2 Steamworks levels being a bit unforgiving (5 and 6, these are the ones I found annoying, probably should fix the ones ice found aswell)
+ Ssshithill shader being fucked (still the same underground, but oh well)
+ Exhaust being a bit unreasonable at times. (plus new npc)
+ Bastion being a bit unreasonable at times.
+ Phlegethon is now on the map. (also gave it a key at the very end as a stand-in)

---

