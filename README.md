## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-11-11](docs/good-messages/2023/2023-11-11.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,959,948 were push events containing 2,827,125 commit messages that amount to 167,650,278 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 48 messages:


## [yuiseki/evals](https://github.com/yuiseki/evals)@[db8b3dfe6f...](https://github.com/yuiseki/evals/commit/db8b3dfe6f69450577314bba40582bfa41bd06a9)
#### Saturday 2023-11-11 00:01:36 by Thiago M. Nóbrega

Add A is B and B is A Eval (#1366)

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

ab

### Eval description

This evaluation aims to assess the model's ability to correctly identify
and understand the relationship between two entities, where A is a
specific entity (which could be a chemical element, a painting, a bird
species, a star, a mountain, a novel, a river, or a musical instrument)
and B is a unique characteristic or fact about that entity. The model
should be able to accurately interpret the user's query about the entity
(A) and provide a relevant fact (B), and vice versa. This evaluation
will help in fine-tuning the model's understanding of context, relation
between entities, and its ability to provide accurate and relevant
responses. The entities and their characteristics have been chosen to be
specific and challenging.

### What makes this a useful eval?

This evaluation is important for several reasons:

1. Contextual Understanding: It tests the model's ability to understand
the context of a conversation, particularly the relationship between two
related entities (A and B).

2. Accuracy: It assesses the model's ability to provide accurate and
relevant information based on the user's query.

3. Relevance: It evaluates the model's ability to understand the
relevance of A to B and vice versa, which is crucial in providing
meaningful and coherent responses.

4. General Knowledge: This tests the model's knowledge about various
specific entities and their unique characteristics or facts, which is a
part of its general knowledge. The entities span a wide range of
categories, including chemistry, art, ornithology, astronomy, geography,
literature, and music, making this a comprehensive test of the model's
general knowledge.

5. Versatility: This checks the model's ability to handle different
types of queries, as the user can ask about the specific entity (A) or
its unique characteristic or fact (B). This tests the model's
flexibility in understanding and responding to a variety of query
structures across diverse knowledge domains.

gpt-3.5-turbo
[2023-10-10 22:42:42,192] [oaieval.py:229] Final report:
[2023-10-10 22:42:42,192] [oaieval.py:231] counts/A: 2
[2023-10-10 22:42:42,192] [oaieval.py:231] counts/B: 11
[2023-10-10 22:42:42,192] [oaieval.py:231] counts/D: 2
[2023-10-10 22:42:42,192] [oaieval.py:231] counts/C: 1

gpt-4
[2023-10-10 22:43:37,306] [oaieval.py:229] Final report:
[2023-10-10 22:43:37,306] [oaieval.py:231] counts/C: 7
[2023-10-10 22:43:37,306] [oaieval.py:231] counts/B: 7
[2023-10-10 22:43:37,306] [oaieval.py:231] counts/D: 2

class: modelgraded.classify:ModelBasedClassify
eval_type: cot_classify
modelgraded_spec: fact

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

A popular paper has been going around called 'The Reversal Curse: LLMs
trained on “A is B” fail to learn “B is A”'. I figured an Eval on this
would have a unique value.

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
pre-commit; pre-commit install` and have verified that `mypy`, `black`,
`isort`, and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "The user will ask you a
question about a specific chemical element that has the atomic number
79, please respond to the best of your abilities."}, {"role": "user",
"content": "What is the name of the element with atomic number 79?"}],
"ideal": "The element with atomic number 79 is Gold."}
{"input": [{"role": "system", "content": "The user will ask you a
question about a chemical element that is often associated with jewelry
and has the symbol Au, please respond to the best of your abilities."},
{"role": "user", "content": "Which element is this?"}], "ideal": "This
element is Gold."}
{"input": [{"role": "system", "content": "The user will ask you a
question about a specific painting that was stolen from the Isabella
Stewart Gardner Museum in 1990, please respond to the best of your
abilities."}, {"role": "user", "content": "What is the name of the
Vermeer painting stolen from the Isabella Stewart Gardner Museum in
1990?"}], "ideal": "The name of the Vermeer painting stolen from the
Isabella Stewart Gardner Museum in 1990 is 'The Concert'."}
{"input": [{"role": "system", "content": "The user will ask you a
question about a Vermeer painting that is still missing after being
stolen from a museum in Boston, please respond to the best of your
abilities."}, {"role": "user", "content": "Which painting is this?"}],
"ideal": "This painting is 'The Concert'."}
{"input": [{"role": "system", "content": "The user will ask you a
question about a specific species of bird that is known for its
elaborate courtship dance, please respond to the best of your
abilities."}, {"role": "user", "content": "What is the name of the bird
species known for its moonwalk-like courtship dance?"}], "ideal": "The
bird species known for its moonwalk-like courtship dance is the Blue
Manakin."}
{"input": [{"role": "system", "content": "The user will ask you a
question about a bird species that is known for its blue color and
unique courtship dance, please respond to the best of your abilities."},
{"role": "user", "content": "Which bird species is this?"}], "ideal":
"This bird species is the Blue Manakin."}

  ```
</details>

---
## [yuiseki/evals](https://github.com/yuiseki/evals)@[4b7a66bd45...](https://github.com/yuiseki/evals/commit/4b7a66bd45f06156656e021e170e7574f6cde3f5)
#### Saturday 2023-11-11 00:01:36 by Vilhjalmur Thorsteinsson

Added Icelandic inflection eval; JsonMatch eval function (#1387)

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

Icelandic noun phrase inflection

### Eval description

This eval consists of 3 x 100 samples in "easy", "medium" and "hard"
categories. Each sample
represents the task of inflecting a noun phrase in Icelandic, in all
four cases of the language
(nominative, accusative, dative and genitive), both singular and plural.
A noun phrase
consists of an adjective and a noun (e.g., "fallegur litur" = "beautiful
color").
In the easy category, both the adjective and the noun are
relatively common. In the medium category, they are less common, and in
the hard category they
are rare enough that it is pretty unlikely that they occur in any
training corpora.

### What makes this a useful eval?

The eval is designed to test the general grammatical proficiency of a
model in Icelandic, and
the eval accuracy is assumed to correlate with a model's ability to
generate grammatically
correct text in the language. GPT models have so far struggled with
generating correct Icelandic
text, even though GPT-4 was uniquely trained by RLHF in the language.
Icelandic is believed to
be a good bellwether for lower-resource, grammatically complex language
support in general.

Inflecting noun phrases is something that native language speakers do
without significant
effort, even if they have not seen the particular adjective and the noun
before, as it can be done on the
basis of generic grammatical pattern recognition. However, to date,
GPT-4 seems not to have
acquired enough of a "native feel" for Icelandic to be able to do this
task with high accuracy.

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

**Note: this PR includes a new general eval class, JsonMatch, which is
not specific to the Icelandic evaluation
case. It allows completions and ideal answers to be represented as JSON
objects, comparing the objects
by individual key:value pairs. Tests and documentation of this
functionality are included in the PR.**

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
pre-commit; pre-commit install` and have verified that `mypy`, `black`,
`isort`, `autoflake` and `ruff` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Þú ert sérfræðingur í
íslenskri málfræði."}, {"role": "user", "content": "Hvernig fallbeygist
nafnliðurinn \"palestínskur fréttavefur\" í öllum föllum (nf, þf, þgf,
ef), eintölu (et) og fleirtölu (ft), án greinis? Svaraðu í *JSON formi
eingöngu* og auðkenndu tölur og föll með skammstöfunum et, ft, nf, þf,
þgf, ef."}], "ideal": "{\"et\": {\"nf\": \"palestínskur fréttavefur\",
\"þf\": \"palestínskan fréttavef\", \"þgf\": \"palestínskum fréttavef\",
\"ef\": \"palestínsks fréttavefjar\"}, \"ft\": {\"nf\": \"palestínskir
fréttavefir\", \"þf\": \"palestínska fréttavefi\", \"þgf\":
\"palestínskum fréttavefjum\", \"ef\": \"palestínskra fréttavefja\"}}"}
{"input": [{"role": "system", "content": "Þú ert sérfræðingur í
íslenskri málfræði."}, {"role": "user", "content": "Hvernig fallbeygist
nafnliðurinn \"hliðhollt lyfjapróf\" í öllum föllum (nf, þf, þgf, ef),
eintölu (et) og fleirtölu (ft), án greinis? Svaraðu í *JSON formi
eingöngu* og auðkenndu tölur og föll með skammstöfunum et, ft, nf, þf,
þgf, ef."}], "ideal": "{\"et\": {\"nf\": \"hliðhollt lyfjapróf\",
\"þf\": \"hliðhollt lyfjapróf\", \"þgf\": \"hliðhollu lyfjaprófi\",
\"ef\": \"hliðholls lyfjaprófs\"}, \"ft\": {\"nf\": \"hliðholl
lyfjapróf\", \"þf\": \"hliðholl lyfjapróf\", \"þgf\": \"hliðhollum
lyfjaprófum\", \"ef\": \"hliðhollra lyfjaprófa\"}}"}
{"input": [{"role": "system", "content": "Þú ert sérfræðingur í
íslenskri málfræði."}, {"role": "user", "content": "Hvernig fallbeygist
nafnliðurinn \"refsiverð stjörnuleit\" í öllum föllum (nf, þf, þgf, ef),
eintölu (et) og fleirtölu (ft), án greinis? Svaraðu í *JSON formi
eingöngu* og auðkenndu tölur og föll með skammstöfunum et, ft, nf, þf,
þgf, ef."}], "ideal": "{\"et\": {\"nf\": \"refsiverð stjörnuleit\",
\"þf\": \"refsiverða stjörnuleit\", \"þgf\": \"refsiverðri
stjörnuleit\", \"ef\": \"refsiverðrar stjörnuleitar\"}, \"ft\": {\"nf\":
\"refsiverðar stjörnuleitir\", \"þf\": \"refsiverðar stjörnuleitir\",
\"þgf\": \"refsiverðum stjörnuleitum\", \"ef\": \"refsiverðra
stjörnuleita\"}}"}
{"input": [{"role": "system", "content": "Þú ert sérfræðingur í
íslenskri málfræði."}, {"role": "user", "content": "Hvernig fallbeygist
nafnliðurinn \"japönsk landbúnaðarvara\" í öllum föllum (nf, þf, þgf,
ef), eintölu (et) og fleirtölu (ft), án greinis? Svaraðu í *JSON formi
eingöngu* og auðkenndu tölur og föll með skammstöfunum et, ft, nf, þf,
þgf, ef."}], "ideal": "{\"et\": {\"nf\": \"japönsk landbúnaðarvara\",
\"þf\": \"japanska landbúnaðarvöru\", \"þgf\": \"japanskri
landbúnaðarvöru\", \"ef\": \"japanskrar landbúnaðarvöru\"}, \"ft\":
{\"nf\": \"japanskar landbúnaðarvörur\", \"þf\": \"japanskar
landbúnaðarvörur\", \"þgf\": \"japönskum landbúnaðarvörum\", \"ef\":
\"japanskra landbúnaðarvara\"}}"}
{"input": [{"role": "system", "content": "Þú ert sérfræðingur í
íslenskri málfræði."}, {"role": "user", "content": "Hvernig fallbeygist
nafnliðurinn \"dýrmætt vistheimili\" í öllum föllum (nf, þf, þgf, ef),
eintölu (et) og fleirtölu (ft), án greinis? Svaraðu í *JSON formi
eingöngu* og auðkenndu tölur og föll með skammstöfunum et, ft, nf, þf,
þgf, ef."}], "ideal": "{\"et\": {\"nf\": \"dýrmætt vistheimili\",
\"þf\": \"dýrmætt vistheimili\", \"þgf\": \"dýrmætu vistheimili\",
\"ef\": \"dýrmæts vistheimilis\"}, \"ft\": {\"nf\": \"dýrmæt
vistheimili\", \"þf\": \"dýrmæt vistheimili\", \"þgf\": \"dýrmætum
vistheimilum\", \"ef\": \"dýrmætra vistheimila\"}}"}
  ```
</details>

---
## [filecoin-project/motion](https://github.com/filecoin-project/motion)@[4fc79c87ff...](https://github.com/filecoin-project/motion/commit/4fc79c87ffacf103db46441a4dafaaf793b74600)
#### Saturday 2023-11-11 00:40:57 by Elijah

feat: add cleanup test, and isolate id mapping code and cleanup code (#218)

Wrote a test for the cleanup code while investigating #201. This
involved moving cleanup code to its own file. I also used this
opportunity to isolate ID mapping code.

The test is passing from the start, so I'm not sure if it'll fix that
issue, but there's a possibility. In any case, it cleans up a bit of
mess.

The cleanup scheduler is a new object with the sole purpose of reading
through the local bin store and removing files based on the result of a
configurable callback, at some interval. A configurable callback allows
it to be mocked easily for the test. In `store.go`, the callback is set
to the `hasDealForAllProviders()` function. This should be tested next.
It'll be a bit more involved since it'll have to be added to the
integration test, since singularity has to be running, but I think I
know how I'll do it.

A few additional functions have been added to local store: `List()` and
`Delete()`. These were previously done inline in `store.go` by manually
working with the store directory files, which was kinda hacky. This puts
that stuff where it belongs.

About the new ID map object: a separation of concerns refactor. Motion
maps blob IDs to Singularity IDs by storing files ending in ".id" in the
same directory, named with the stringified motion ID, and containing the
Singularity ID in the body. This processing was all done inline in
`store.go` With these changes, this behavior is unmodified, so there
should not be any compatibility issues. I originally wrote this because
I thought I would be working with IDs in `cleanup.go`, but my final
solution did not end up needing it. So in the end it is just a general
improvement. It does pave the way for an ID mapping test.

should fix #201, awaiting confirmation by @Angelo-gh3990

---
## [OliOliOnsiPree/tgstation](https://github.com/OliOliOnsiPree/tgstation)@[2532911353...](https://github.com/OliOliOnsiPree/tgstation/commit/2532911353d63661b735004f2895103d45858b50)
#### Saturday 2023-11-11 00:41:21 by LemonInTheDark

Adds pathmaps, refactors pathfinding a bit (#78684)

## About The Pull Request

Implements /datum/pathfind/sssp, which generates /datum/path_map

/datum/path_maps allow us to very efficently generate paths to any turf
they contain from their central point.

We're effectively running the single source shortest paths algorithm.
We expand from the center turf, adding turfs as they're found, and then
processing them in order of addition.
As we go, we remember what turf "found" us first. Reversing this chain
gives us the shortest possible path from the center turf to any turf in
its range (or the inverse).

This isn't all that useful on its own, outside of a few niche cases
(Like if we wanted to get the farthest reachable turf from the center)
but if we could reuse the map more then once, we'd be able to swarm
to/from a point very easily.

Reuse is a bit troublesome, reqiures a timeout system and a way to
compare different movables trying to get paths.
I've implemented it tho. I've refactored CanAStarPass to take a datum,
/datum/can_pass_info. This is built from a movable and a list of access,
and copies all the properties that would impact pathfinding over onto
itself.

There is one case where we don't do this, pathing over openspace
requires checking if we'd fall through the openspace, and the proc for
that takes an atom.
So instead we use the weakref to the owner that we hold onto, and hold
copies of all the values that would impact the check on the datum.

When someone requests a swarmed path their pass info is compared with
the pass info of all other path_maps centered on their target turf. If
it matches and their requested timeout isn't too short, we just reuse
the map.

Timeout is a tricky thing because the longer a map exists the more out
of date it gets.
I've added a few age defines that let you modulate your level of risk
here. We default to only allowing maps that are currently
being generated, or finished generating in our tick. 
Hopefully this prevents falling into trouble, but consumers will need to
allow "failed" movements.

As a part of this datumized pass info, I've refactored pathfinding to
use access lists, rather then id cards directly. This also avoids some
dumbass harddel oppertunities, and prevents an idcard from changing mid
path.

Did a few things to the zPass procs, they took args that they did NOT
need, and I thought it'd be better to yeet em.

If you'd all like I could undo the caching/can_pass_info stuff if you'd
all like. I think it's useful generally because it avoids stuff changing
mid pathfind attempt, but if it's too clunky I could nuke it.

Oh also I added optional args to jps that constricts how it handles
diagonals. I've used this to fix bot paths.

## Why It's Good For The Game

Much of this is redundant currently. I'm adding it because it could have
saved hugglebippers, and because I get the feeling it'll be useful for
"grouping" mobs like bees and such.
We're doing more basic mob work currently and I want to provide extra
tools for that work.


https://github.com/tgstation/tgstation/assets/58055496/66aca1f9-c6e7-4173-9c38-c40516d6d853

## Changelog
🆑
add: Adds swarmed pathfinding, trading accuracy for potential
optimization of used correctly
fix: Bots will no longer take diagonal paths, preventing weirdo looking
path visuals
refactor: Refactored bits of pathfinding code, hopefully easier to add
new pathfinding strategies now
/🆑

---
## [vampirebat74/lobotomy-corp13](https://github.com/vampirebat74/lobotomy-corp13)@[294f764ad0...](https://github.com/vampirebat74/lobotomy-corp13/commit/294f764ad01a99c63b46dfea3dac7e5cfe14cd7d)
#### Saturday 2023-11-11 00:50:43 by Coxswain

Adds distorted form (#1435)

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

damage coeff update

makes suggested changes

updates comments

adds procs

adds stuff

---
## [BogCreature/Shiptest](https://github.com/BogCreature/Shiptest)@[590e8cb752...](https://github.com/BogCreature/Shiptest/commit/590e8cb752400295fe770c303cf5b65a0089fc97)
#### Saturday 2023-11-11 00:55:04 by Imaginos16

Adds the Inkwell-class Supply Freighter (#2385)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->
## Wait, isn't there a freeze right now?
Correct, there is a ship freeze currently, but I have received
permission from @Apogee-dev to create the PR for this vessel, as it was
a ship I've been working on since at least early-to-mid August.

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/653635cc-b83d-44d8-a9e3-384ffbd9367b)

If any other maptainer would like to overrule Apogee, I'd be more than
happy to temporarily close the PR. Until then, here it is!
## About The Pull Request
Hello everyone! Mr. SolGov here again to add yet another ship to be
tested!

This PR adds a completely new vessel, that being the **Inkwell-class
Supply Freighter**, a ship known for its vast cargo space!

![2023-10-13 13 54
57](https://github.com/shiptest-ss13/Shiptest/assets/77556824/9a70d97e-ab17-45af-a690-e528574b95cb)

![2023-10-13 13 54
59](https://github.com/shiptest-ss13/Shiptest/assets/77556824/2d9d6d0a-85e2-4c46-9754-d49f15be0560)

With extra starter money, three sonnensöldners, and three miners,
players can enjoy completing bounties like no tomorrow, have drinks with
their crewmates in peace, and supply other SolGov vessels with much
needed equipment in less time than you can say "I ran out of ammo!"

Notable things in this ship include:
- Turrets (with IFF!)
- A bar!
- A full-blown cafeteria with a small kitchen and lounge!
- An office space for bureaucrats and scribes!
- Decently-sized quarters for the Logistics Deck Officer and Captain!
- A massive cargo bay with pre-existing supplies!
- A secret compartment for private storage!

And finally, as for jobs, there are:
- 1 Captain
- 1 Logistics Deck Officer
- 3 Sonnensöldneren
- 2 Space Engineers
- 3 Field Engineers
- 2 Bureaucrats
- 6 Scribes
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
More SolGov content is nice! Especially when it comes to ships, for a
faction that only has two existing at the moment, haha.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy
add: The Solarian Port Authority Has Now Permitted Inkwell-class Vessels
To Explore The Stars!
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

---
## [Rustybuckets6601/tgstation](https://github.com/Rustybuckets6601/tgstation)@[d31c21ff1b...](https://github.com/Rustybuckets6601/tgstation/commit/d31c21ff1b57ba7003f9bbdcf51171d3215a0774)
#### Saturday 2023-11-11 01:31:23 by jimmyl

new space ruin, the biological research outpost (#79149)

## About The Pull Request

![2023-10-21 18 02
39](https://github.com/tgstation/tgstation/assets/70376633/5829e939-3b04-465f-a186-095ceb360bba)

adds this ruin to space ruin pool
this is a shady (as NT always is) bioresearch outpost that got fucked up
by an experiment
this has like some puzzle aspect to it since you gotta find keycards and
shit and press buttons to unlock shield gates
this ends with you fighting a heart which if you defeat, destroys the
blockade that prevents you from entering the outpost vault

also you can no longer literally just cut indestructible grilles or
unanchor indestructible windows

### new puzzle elements or something idk
variant of pressure plate that you cannot remove and it sends a puzzle
signal
cooler red puzzle doors that look very foreboding or something idk
theyre for this ruin
also puzzle blockades, which are indestructible dense objects that are
destroyed if they receive a puzzle signal
and also buttons and keycard pads for puzzles


https://github.com/tgstation/tgstation/assets/70376633/c98807ec-1e7b-49c4-a757-cdbb76a1b566



https://github.com/tgstation/tgstation/assets/70376633/9d5d9dd1-5868-44e6-a978-5ea57b30c298

stuff that throws electric shocks in a pattern, ignores insuls and only
knocks down, and no you cannot just run past


https://github.com/tgstation/tgstation/assets/70376633/5772917c-a963-48a4-a743-b0f610801d25

### enemies
living floor, it can only attack stuff on top of it and it attacks until
the victim is dead
it is invincible to all but a crowbar, and it cannot move, and it
remains hidden until a victim is in range


https://github.com/tgstation/tgstation/assets/70376633/aa1d54f6-b259-4e58-9d44-e393d2131acf

living flesh, it can replace your limbs with itself
the conditions for that are; the limb must have 20 or more brute, victim
must be alive and dismemberable, the limb may not be torso or head, or
the limb may not be living flesh
alternatively it can replace a missing limb
these are all checked with every attack
they have 20 hp
the limbs in question will sometimes act up, while passively draining
nutrition, arms will randomly start pulling nearby stuff, legs may step
randomly
limbs when detached, turn into mobs and reactivate AI 2 seconds later.
if the host is shocked, all living flesh limbs will detach, or if the
host dies they will also do that


https://github.com/tgstation/tgstation/assets/70376633/765cc99e-c800-4efb-aabe-d68817bbd7ae



## Why It's Good For The Game

ruin variety is cool i think
also the other things i added should be useful for other mappers for
bitrunning or whatever

also bug bad for that one fix
## Changelog
:cl:
add: living floor, living flesh, and other stuff for the bioresearch
outpost ruin
add: bioresearch outpost ruin
fix: you may not defeat indestructible grilles and windows with mere
tools
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Rustybuckets6601/tgstation](https://github.com/Rustybuckets6601/tgstation)@[9e18c6575a...](https://github.com/Rustybuckets6601/tgstation/commit/9e18c6575a3cb9e73c3e699d4fe51b904b76e2f6)
#### Saturday 2023-11-11 01:31:23 by lizardqueenlexi

Basic Pirate NPCs (#79284)

## About The Pull Request

Converts hostile pirate NPCs to basic mobs - specifically, a subtype of
trooper. As their behavior is not meaningfully distinct from other
troopers, this conversion mostly just sticks them on the existing AI
behavior while keeping the rest the same.

Pirates do have one new thing going for them, though, to differentiate
them from other troopers. They use the new **plundering attacks**
component, which means that every time they land a melee attack, they
steal money from the bank account of whoever they hit. This requires the
target to be wearing an ID with a linked bank account, so it's not the
hardest thing in the world to hide your money from them - but it's still
something to be wary of! If killed, any mob with this component will
drop everything they've stolen in a convenient holochip.
## Why It's Good For The Game

Takes down 5 more simplemobs, and (I think) converts the last remaining
trooper-type enemy to be a basic trooper. (It's possible there's more
I've forgotten that could use the same AI, though.)

The money-stealing behavior is mostly good because I think it's funny,
but it also makes the pirates something a little distinct from "yet
another mob that runs at you and punches you until you die". They still
do that, but now there's a little twist! This can be placed on other
mobs too, if we want to make any other sorts of thieves or brigands.
## Changelog
:cl:
refactor: Pirate NPCs now use the basic mob framework. They'll be a
little smarter in combat, and if you're wearing your ID they'll siphon
your bank account with every melee attack! Beware! Please report any
bugs.
/:cl:

---
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[c8d4d0080b...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/c8d4d0080b786212841ec0f03148987cf6594aba)
#### Saturday 2023-11-11 01:34:45 by Profakos

Changes to the lore of Knock (#79542)

## About The Pull Request

This PR renames Knock to Lock, and changes most of the knowledge gain
lore.

## Why It's Good For The Game

The Knock Lore, is based on the Knock Principle from Cultist Simulator,
with the path description being copied from the wiki. Many other
keywords and concepts are fully lifted from that game (Locksmith's
Secret, Mother Of Ants, etc). In my vision, if a heretic path has to be
based on a principle from cultist simulator, it should have its own
spin, and also, the knowledge gain texts should tell a story. For
example, Ash tells the story of a watchman burning down their city after
being betrayed, and Cosmic is a love story between a knowledge seeker
and a monster from the beyond.

So I have decided to reflavour Knock. I have changed the name to Lock,
so at least it would feel similar, just like how Blade is akin to Edge.
Many powers also block people or confuse their paths instead of opening
new ways, and thus, I feel a path whose name implies that it *both*
opens and closes would be more self describing.

I have changed most of its lore to be about the Locked Labyrinth, where
knowledge seekers willingly trap themselves and submit themselves to
servitude to find ultimate freedom by progressing through its trials.
These are the Stewards, who are basically workers in an infinite and
malicious hotel in their dreams. Consider them assistants if you will
(this wasn't my intention when I wrote the lore, but thinking about it
in retrospect, it honestly fits). In the implied story, the heretic
joins their ranks, but keeps getting closer to the more corrupt members,
along with parasitic spirits. Ultimately, they manage to open the
Labyrinth's core, letting out the Stewards, allowing them to manifest in
the forms of heretic summon creatures.

The side path spells and the lock knowledge ritual I have not touched,
they were fine. Some items have been renamed and repathed.

I have kept the distinctive sound effect for using the Grasp, as its
unique enough. Though if someone did have a nice sound effect for
turning a lock and added some filters, I would add it.

**DB Issue**

I have renamed the achievement's define to MEDAL_LOCK_ASCENSION but kept
the value as "Knock", as I don't know how trigger a change in the DB. If
this is a blocking change, I'll try to figure out how to make a
migration file.

**Future improvements**

I would also come back later with another PR, that hands out names to
the eldritch beings spawned by the portal, based on the Stewards in the
knowledge gain lore that I added, along with some new ones that fit the
theme, and some jokey ones like Minotaur.

## Changelog

:cl:
spellcheck: Renamed Knock to Locks, and changed most of the flavor text
of knowledge gain, and renamed some items and knowledges from the path.
/:cl:

---
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[a881f0fe6c...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/a881f0fe6c9dde7409978b38e40be30299ba8b6c)
#### Saturday 2023-11-11 01:35:10 by DaCoolBoss

Adds garbage dumpster ruins (#79446)

## About The Pull Request
Adds 4 small space ruins. Each is a dumpster in space containing hostile
mobs to fight and items to bring back to the station. There's a
decommissioned garbage truck pulling each dumpster which acts as a
staging area before you take on the mobs inside.
All the fights are in cramped dark areas with full pressure, air is
breathable but sometimes has miasma in it so beware of getting sick. So
you can drop your space suit and put on armour, but PKAs won't fire at
full power and keeping a gas mask on is recommended.
Also all the dumpsters look the same from the outside so you gotta crawl
inside to know what's inside. And no you can't metagame it with mesons
either.

Comes in the following flavours:
Food Waste
Full of trash from kitchens, and food. Some of the food is still edible.
There's a lot of territorial rats. You can chop them up into meat if you
want more food. The big prize is a big vat of cooking oil.

Medical Waste
Spare organs, cyberorgans and almost a full set of old surgical gear.
There's a syndicate agent here up to no good and he has a GUN. The gun
blows up when the agent dies so you can't get it. There's a few corpses
of different species in bodybags and some spare corpse parts so you can
bring them back to the station and give them to the coroner. Also a
single use eyestealer in a safe (the cool way to do surgery) and a bug
from the old traitor objective that doesn't do jack but can probably
still get you thrown in perma.

Construction Garbage
Tools and construction materials here, including a cool hammer that fits
in a tool belt and can function as a crowbar. There's also a drug lab
with plenty of weird pills to eat, cigarettes to eat and an angry
russian drug dealer who will stab you if he sees you. He has a badass
lighter and a flamethrower you can take after you kill him. Setting fire
to things in here is not recommended because of all the welding fuel.

Mall Trash
Action figures, trading cards, Christmas crackers and other trash the
local mall tossed out. Also a mothman used to live here but he got eaten
by giant spiders so you can grab his stuff, including snacks and a
civilian modsuit with no mods (wow). You can cut through the webs to
kill the spiders or let them eat you too if you want.
## Why It's Good For The Game
More content for space explorers.
More variety to the potential dangers of space, now u can get sick and
die or get eaten by rats (this is hobo RP)
Better environmental storytelling. Now instead of players left asking
"what happens to the garbage when it goes into space" they can rest
assured that there's busted ass garbage trucks in space. All their
questions are answered.
Loot that encourages working with people on the station. Raw food for
the kitchen, rats for genetics, organs for the coroner, etc
## Changelog
:cl:
add: 4 new space ruins
/:cl:

---
## [MelnikovAG/roslyn](https://github.com/MelnikovAG/roslyn)@[c881d0a819...](https://github.com/MelnikovAG/roslyn/commit/c881d0a819551606c4be8df25afafb864fb38654)
#### Saturday 2023-11-11 01:47:10 by Cyrus Najmabadi

Fix contract assertion firing with SG OOP syncing.

This was a very subtle issue. It was found thanks to some paranoid asserts added when doing the "perform SG generation in OOP process" work.

First, some background. We have a type called SourceText which represents the string-oriented (not byte-oriented) contents of a file. That type also exposes a concept of the "content checksum". This content checksum corresponds to the original bytes the source-text was created from, and not necessarily the current 'string-oriented view' the SourceText represents.

In other words, the following axiom does NOT hold:

sourceText.GetChecksum() == SourceText.From(sourceText.ToString(), sourceText.Encoding, sourceText.HashAlgorithm).GetChecksum()

As an example of when this might happen, consider that the bytes of a file may or may not include the BOM for utf8. So you might have two files with different byte contents that end up representing the same char contents.

Unfortunately, the SG OOP syncing code assumed the above was true. If would sync over file contents, then assert that the checksum we then produced on the host side matched what was on the OOP side. This assertion was not valid given the above, and our connection would die.

The fix is not to just to remove the assertion though. If we did that, we'd end up in a bad state where the host and the OOP side would always disagree on the content checksum of these SG files, causing them to resync on each solution fork. That would be very bad for perf (Esp. as SG files can be enormous). The fix instead is to understand that the checksum on the OOP side may not be computable on the host side, and instead just trust and use that server-side-computed checksum locally for all checksum related questions we have.

Note: A cleaner fix will be possible if/when we get approval on the following API suggestion: #70752. With that API we would be able to produce a SourceText locally with the exact same checksum as what was on the OOP side. This would be nice to have in the long term so that if we have any other code that ends up looking directly at the SourceText for its checksum, it doesn't get confused as to why the host and OOP disagree on it.

---
## [ReturnToZender/ReturnsBubber](https://github.com/ReturnToZender/ReturnsBubber)@[468afa292d...](https://github.com/ReturnToZender/ReturnsBubber/commit/468afa292dfaef7bcbc6df7b55cd0380582533a6)
#### Saturday 2023-11-11 02:22:04 by BurgerLUA

Adds the WT-551, Unskyrats the WT-550 ammo (#655)

## About The Pull Request


## The WT-551

![image](https://github.com/Bubberstation/Bubberstation/assets/8602857/d57f5767-366e-4835-a5bf-d965b6b375a6)

This adds the WT-551. A remade version of the WT-550 that is worse in
every way. Fortunately, that means that it is balanced enough to be put
in NanoTrasen armories.

Compared tot he WT-551, it is bulkier and slightly slower (0.3 second
fire delay compared to 0.2). Additionally, it is commonly used with
rubber-tipped rounds or FlatHead rounds, which are a special surplus of
ammo that deals less damage and has no wounding, embedding, or
penetrative power. Regular ammo can be purchased from cargo or
researched later, with special ammo also being available later.

Note that this does not replace the WT-550.

## FlatHead ammo


![image](https://github.com/Bubberstation/Bubberstation/assets/8602857/81de4bdb-6fd6-4f23-a1b1-0af21e924c34)

Flathead ammo deals 18 brute damage (compared to the original 20), and 5
stamina damage per hit. It is extremely weak against armor, has no embed
chance, has virtually no wounding chance. It's perfect for cheap
corporate companies dealing with cheaper personnel. This is the type of
lethal ammo that security will use for the gun, unless someone speedruns
weapon research.


## Research Progression


![image](https://github.com/Bubberstation/Bubberstation/assets/8602857/26b72a1c-ebda-439a-98c9-9dc3168e01bd)

### Basic WT-550/WT-551 Ammunition.
Flathead rounds and Rubber rounds for the WT-550/WT-551 can be
researched for 2500 points after unlocking the "Weapon Development
Technology" node.

### Advanced WT-550/WT-551 Ammunition.
Regular rounds and AP rounds for the WT-550/WT-551 can be researched can
be researched for 5000 points after unlocking the "Advanced Weapon
Development Technology" and "Basic WT-550/WT-551 Ammunition" nodes.

### Illegal WT-550/WT-551 Ammunition.
Incendiary rounds for the WT-550/WT-551 can be researched can be
researched for 7500 points after unlocking the "Illegal Technology",
"Exotic Ammo" , and "Advanced WT-550/WT-551 Ammunition" nodes.

### Syndicate Research

Removes the WT-550 ammo from syndicate research since it is now
redundant.

## Cargo


![image](https://github.com/Bubberstation/Bubberstation/assets/8602857/a24e9df4-36e3-4368-b77a-cff06a42579f)

WT-551 rifles can be ordered in pairs (2) for the cost of a parrot, a
grilling starter pack, or a crab rocket (1600 credits). This value was
chosen because it is slightly higher than the thermal pistols, and the
traitor-ordered WT-550 rifle pack (which contains lethal ammo + spare
lethal ammo).

Additional FlatHead, Rubber, and Regular ammo can be ordered from cargo
as well.

Cargo techs no longer get WT-550s in the mail, but instead WT-551s (why
was this a thing holy shit).

## Armory


![image](https://github.com/Bubberstation/Bubberstation/assets/8602857/e88a37af-2e4f-4b1c-bc25-b9bed9e41b91)

2 WT-551s can be found in the armory.
For balance purposes one (1) laser rifle was removed.

## I hate Skyrat so much holy shit


![image](https://github.com/Bubberstation/Bubberstation/assets/8602857/b09eed34-77cd-4f37-8356-93688fec344e)

Unfucks the WT-550 ammo types by removing their dumb names and changed
caliber types.

Unfucks the WT-550 ammo in the ammo printer so that rubber rounds can be
printed at T0 and everything else (except incendiary rounds) can be
printed with the adv munitions disk.

The bullets for the WT-550 have been forcibly changed to /tg/ balance,
which means that any and all future Skyrat PRs cannot touch the damage
values for it (unless some fuckery occurs, idk).

## Why It's Good For The Game


![image](https://github.com/Bubberstation/Bubberstation/assets/8602857/395b9fa5-8380-46bc-96a7-06ce0931d8e7)


Security is in dire need of actual ballistics. /tg/ removed ballistics
from security because of reasons I legitimately don't think are valid.
It's also a huge balance concern for security not to have at least 1
ballistic weapon (other than the shotgun) because it doesn't stop antags
from hoarding laser immunity or meds.

Also guns are cool.

## Changelog

:cl: BurgerBB
add: Adds the WT-551 rifle, a redesign of the WT-550 rifle that is
balanced (citation needed) for security use.
add: Makes WT-550 ammo researchable and orderable from cargo. Removes
WT-550 ammo from syndicate research, and gives them their own
categories.
/:cl:

---------

Co-authored-by: StrangeWeirdKitten <95130227+StrangeWeirdKitten@users.noreply.github.com>
Co-authored-by: ReturnToZender <donwest947@gmail.com>

---
## [acidvegas/skeleton](https://github.com/acidvegas/skeleton)@[0df93b8f80...](https://github.com/acidvegas/skeleton/commit/0df93b8f80c82295df540d2a1386ee481f9988e3)
#### Saturday 2023-11-11 02:22:30 by acidvegas

Spaces to tabs (cause fuck you) and fixed nickserv line missing f-string

---
## [EntranceJew/TTT2](https://github.com/EntranceJew/TTT2)@[b156272b3a...](https://github.com/EntranceJew/TTT2/commit/b156272b3aa41fb56904a2d806bebc36c3833cb3)
#### Saturday 2023-11-11 02:36:49 by EntranceJew

grenades WIP

- added trajectory for grenade throws
- removed redundant Init/CreateGrenade, use baseclass
- renamed confgrenade vars to make more sense
- added UI to conf/smoke/firegrenade
- removed dead code in smoke entity
- brought in ttt_flame entity
- moved ttt_flame globals to game_effects library, affects C4
- fixed ttt_flame not utilizing offset from trace, as the intent seems to be
- allowed disarming players with impacts
- made discombobs bouncy
- grenade UI indicators in gameplay options
- fixed basegame bug where grenades would self-intersect on raytrace for ground searches
- smoke projectile packs in convars to game_effects
- smoke projectile no longer uses accessor functions
- smoke projectile centers itself by half of its radius to prevent floorsmokes
- hook for confgrenade explode
- particle dispersal from discombob
- consolidate ttt_smoke into Disipate and Remove
- force add PVS code (still doesn't fix ParticleEmitter shenanigans)
- smoke effects use same parameters, but smokegrenade convar differs
- ttt_smoke now utilizes the space better to fill the volume better even with maximum variance
- fires get funny particles and trails
- ttt_flame hitboxes adjusted their hitboxes are way too big
- new explosion sound Tim provided
- new fizzle sound edited together by me
- game_effects.Extinguish now plays a noise
- ttt_flame can no longer re-ignite
- PushPullRadius from conf moved to game_effects
- thirdparty menu
- vfire
- factored out game_effects.ScorchDown
- potentially ruined ttt_firegrenade_proj killing itself frame0 because extinguish might not know what to do with it
- reorganized BaseClass.Initialize for no good reason
- addon checker result ammended
- ttt_flame bringdown
- ttt_flame has netvars for new params
- startfires longer signature
- ttt_flame / SpawnFire has more accurate hitbox
- fire size / life span / spread / prevent discombob fling convars
- removed legacy renderer for fire, since smoke is broken, nobody gets to be happy
- smacking grenades makes explosions
- added changelog
- fixes from TimGoll
- renamed boom_ball to "electric_explosion"
- added more addonchecker items
- passes down the inflictor to pushpullradius
- documented extinguish hook
- gameEffects docs
- remove postround protection and redundant latch, correct trace offset
- don't tinker with the PVS if it isn't fixing problems
- it wasn't relevant because there IS no physics object right now
- all this for a little bit of not scorching in the wrong spot
- all this does is prevent repeat callbacks on the explode method on the client, sometimes
- back out cringe network changes
- replace scorch with PaintDown
- looping smoke sound global
- SmokeData color can now be manually overridden
- killed todos
- docs fixes
- added animation timers back in
- networked the var and run only in server to prevent double sfx

---
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[1a9043d797...](https://github.com/jlsnow301/tgstation/commit/1a9043d797325fe09cdb4e42d42f5d922c151ed9)
#### Saturday 2023-11-11 03:19:34 by necromanceranne

The Brawlening: Unarmed fighting interactions for shoving, grabbing and nonlethal takedowns (not martial arts) (#79362)

## About The Pull Request

I've tweaked some elements of unarmed fighting to give it additional
interactions between the various components, bridging them into a more
coherent system and focusing more strongly as tool for disabling
opponents nonlethally.

### Shoving

Shoving guarantees that unarmed attacks will land while knocked
off-balance (AKA when slowed by a shove).

Being off-balance means that you can be knocked down from a punch if you
have taken enough brute and stamina damage combined (at least above 40).

Being off-balance makes you vulnerable to grabs while you have a
moderate amount of stamina damage (30 damage), forcing you to have to
resist even passive grabs. This pairs _exceptionally_ well with
tackling.

### Grappling

Grappling someone makes your unarmed attacks penetrate armor based on a
new limb value called ``unarmed_effectiveness``. This is something
shared by kicking.

### Unarmed Attacks in General

``unarmed_effectiveness`` has also taken over the functionality of
``unarmed_stun_threshold``, as well as accuracy calculations. Human
equivalent limbs (pretty much all of them except mushrooms and golems)
have a value of 10.

Now, ``unarmed_effectiveness`` determines how accurately a given limb
makes unarmed attacks. Unarmed attacks have a base inaccuracy of 20%,
with effectiveness acting as a reduction to this value. (so for humans,
that's 20% - 10% before any value changes from brute and stamina
damage). It is also capped at 75% miss chance, just to avoid those weird
instances of two brawling fighters being incapable of finishing each
other off at a certain amount of damage and it being real awkward, like
it does currently.

It also determines the base probability of landing a knockdown punch.
For humans, this is 10%.

For the most part, these two particular changes are roughly equivalent
to the current values, just handled in a way that is more
straightforward to understand from a code perspective.

In addition to the above, human equivalent limbs have higher damage
floors for unarmed attacks. Arms deal 5-10 damage, while legs deal 7-15
damage. In addition, kicks also deal stamina damage, like punches do.

### Minor Mentions

Golems and Mushroom People (who don't even use their limbs for their
unarmed strikes because mushroom people start with a martial art) have
very accurate punches, and their punches penetrate quite a bit of armor
when they are entitled to that. They also have a high knockdown
probability. This is partially because they previously already _had_
these features due to the wonky math at play, but also because this is
their big thing they are good at.

Carp mutation also got a big win out of this as well. If and when you
actually manage to get that to work and matter.

## Why It's Good For The Game

My favorite thing in this game is the robustness of unarmed fighting.
It's the part of the game that actually acknowledges the sandbox and
environmental interaction in a big way. The only problem with the
unarmed combat is that it is a bit disjointed, and often much weaker
than using even the most pathetic weapon you can get your hands on
unless you're using the stun loops available. Those loops get a bit
boring, even if they're mostly all environmental (except for the lucky
neckgrab finish). Giving more options generally means that even when not
in an ideal position, you still have _some_ options.

It also has some internal inconsistencies in design even in the same
proc, like accuracy calculations and knockdowns, as well as weird splits
in damage. So I decided to resolve that.

Now, every part of unarmed fighting has some relevance in the other
parts. Predominantly, it is heavily favoured towards dealing stamina
damage, making unarmed combat very favourable as a nonlethal method of
taking someone down, which is something we currently lack considerably.
While people may still opt to simply beat someone into actual crit
rather than stop at stamina crit, the possibility is actually entirely
available and supported now. No just banking on a lucky neckgrab after a
shove.

Paying attention to damage dealt and thinking intelligently about how
you apply combinations of effects allows even someone on the significant
back foot an opportunity for a comeback if they know what they're doing
against even armed opponents.

Separating accuracy and knockdown effectiveness from damage allows for
more consistent design and readability, but also preventing weirdness
ike tighter damage spreads increasing knockdown probabilities as well as
increasing accuracy without the coder knowing why. This also lets us
make unarmed attacks just that little bit stronger. Since unarmed
attacks require more complicated combinations to work, I think this
won't make them stronger than weapons necessarily, but it will make for
more interesting swung fights.

## Changelog
:cl:
add: With the flood of Chi within the Spinward Sector receding, various
masters of The Tunnel Arts, colloquially known as 'Maint-fu Masters',
have started to refine the basics of their martial techniques. New forms
have started to develop within Spacestation 13's hidden maintenance
dojos.
add: Someone shoved off-balance makes them vulnerable to more guaranteed
unarmed strikes, knockdowns from a successful punch, and more difficult
to escape grabs.
add: Grabbing someone (as well as kicking them while they're on the
floor) makes them more vulnerable to taking unarmed attack damage, even
if they have armor.
balance: Unarmed strikes made with human-equivalent limbs have higher
damage floors, meaning you overall do more damage on average while not
increasing the overall damage potential. It's more consistent!
refactor: Significantly changed how punching accuracy and knockdowns are
calculated.
balance: Golem and mushroom limbs are a lot more effective at punching
as a result of these various changes. As they should be.
/:cl:

---
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[91af16bcbf...](https://github.com/jlsnow301/tgstation/commit/91af16bcbfd2dd363a89d846ae2acd6d655083c2)
#### Saturday 2023-11-11 03:19:34 by zxaber

Adds Paddy, the Security Mech (#79376)

## About The Pull Request
- Adds a new combat mech, Paddy. Paddy is a modified Ripley MK-I,
intended for use by the station's security force. Like the MK-I, the
Paddy features an open-air cockpit design (and thus does not protect
from ranged weapons), but maintains the speed of the base unit.
Constructing a Paddy is similar to constructing a MK-II, though the kit
requires combat-mech level research. Sprites by
[DrDiasyl](https://github.com/DrDiasyl)
-- The paddy has an internal cargo bay capable of holding up to four
individuals (loaded with a hydraulic claw). If the pilot exits the
Paddy, any loaded individuals are likewise ejected. Individuals can
attempt to resist their way out of the mech, but it requires the mech to
be stationary for 45 seconds. If they do this, all individuals in the
holding cell are ejected.

- Adds a new mech equipment piece, the hydraulic claw. Similar to a
clamp, this Paddy-exclusive item can load mobs into the Paddy's cargo
bay. Humanoid mobs are handcuffed upon loading. The hydraulic claw is
unlocked on the same tech node as the Paddy.

- Adds a round-start Paddy, carrying one peacekeeper disabler and one
hydraulic claw, to each security area on all maps. Round-start Paddys
are also pre-locked with security access. Security now has access to a
mech charger, and a small bay for it all. Map edits were done by
[Maurukas](https://github.com/Maurukas).

- Also did some minor cleanup of various mech-related code. Ripley mech
cargo is no longer stored in the mech, but within the "ejector" object.
This doesn't have any player-facing changes, but it is easier to
organize behind the scenes. additionally, if Ripleys are destroyed now,
they drop their stored objects rather than deleting them.

## Why It's Good For The Game
Playing lone security is probably one of the least fun aspects of the
game. Arresting any assistant is inevitably setting yourself up against
the tide as a whole; You try to stun any one person and they crawl out
of the woodworks to get in your way, drag off the arrestee, and probably
try to steal your gear.

The Paddy is set up to be functional against low-threat targets, but not
particularly good against anything with purpose. The round-start Paddy
carries the disabler equipment, as well as the law claw, to detain
individuals in a *somewhat* safe manner. Being that you're inside an
exosuit, you're immune to shovespam that plagues the halls, and you
don't risk dropping important gear quite as easily.

However, The open canopy gives you no protection at all from ranged
attacks, nor from atmos hazards. Being that you're in an exosuit, you
cannot use other items or equipment. The AI will have trouble finding
you to open a door, due to your name not jumping their camera to your
location.
## Changelog
:cl: Zxaber, DrDiasyl, Maurukas
add: A new security-focused combat mech, the Paddy, has been added,
intended to be particularly helpful for lone sec officers. You will find
one in the Security main office, and a replacement can be built with
late-game mech research.
fix: Ripley MK-I and MK-II mechs no longer qdel their stored items when
destroyed.
/:cl:

![image](https://github.com/tgstation/tgstation/assets/37497534/72e6890d-82be-44dd-9b09-e4c75a9bfd4a)

---------

Co-authored-by: Vire <66576896+Maurukas@users.noreply.github.com>

---
## [yybos-hash/Katarakt2](https://github.com/yybos-hash/Katarakt2)@[f7bb2efaef...](https://github.com/yybos-hash/Katarakt2/commit/f7bb2efaefc6c36720ccdd275818b8b9e6e21026)
#### Saturday 2023-11-11 03:22:38 by yybos-hash

oh my fucking god, so many changes;
Its 00:20 am and I cant think straight, any code written from now on can be considered trash.

Some changes:
no more logPort, now there is the chatPort. Ill use it to send the chats to the client, the log is now gonna send the messages normally.

Now the client sends the version, username and password all at once, something like this: "1.0.0;username;password"

Thats it, I think

---
## [mattkime/kibana](https://github.com/mattkime/kibana)@[cd909f03b1...](https://github.com/mattkime/kibana/commit/cd909f03b1d71da93041a0b5c184243aa6506dea)
#### Saturday 2023-11-11 03:57:39 by Kyle Pollich

[Fleet] Fix inability to upgrade agents from 8.10.4 -> 8.11 (#170974)

## Summary

Closes https://github.com/elastic/kibana/issues/169825

This PR adds logic to Fleet's `/api/agents/available_versions` endpoint
that will ensure we periodically try to fetch from the live product
versions API at https://www.elastic.co/api/product_versions to make sure
we have eventual consistency in the list of available agent versions.

Currently, Kibana relies entirely on a static file generated at build
time from the above API. If the API isn't up-to-date with the latest
agent version (e.g. kibana completed its build before agent), then that
build of Kibana will never "see" the corresponding build of agent.

This API endpoint is cached for two hours to prevent overfetching from
this external API, and from constantly going out to disk to read from
the agent versions file.

## To do
- [x] Update unit tests
- [x] Consider airgapped environments

## On airgapped environments

In airgapped environments, we're going to try and fetch from the
`product_versions` API and that request is going to fail. What we've
seen happen in some environments is that these requests do not "fail
fast" and instead wait until a network timeout is reached.

I'd love to avoid that timeout case and somehow detect airgapped
environments and avoid calling this API at all. However, we don't have a
great deterministic way to know if someone is in an airgapped
environment. The best guess I think we can make is by checking whether
`xpack.fleet.registryUrl` is set to something other than
`https://epr.elastic.co`. Curious if anyone has thoughts on this.

## Screenshots


![image](https://github.com/elastic/kibana/assets/6766512/0906817c-0098-4b67-8791-d06730f450f6)


![image](https://github.com/elastic/kibana/assets/6766512/59e7c132-f568-470f-b48d-53761ddc2fde)


![image](https://github.com/elastic/kibana/assets/6766512/986372df-a90f-48c3-ae24-c3012e8f7730)

## To test

1. Set up Fleet Server + ES + Kibana
2. Spin up a Fleet Server running Agent v8.11.0
3. Enroll an agent running v8.10.4 (I used multipass)
4. Verify the agent can be upgraded from the UI

---------

Co-authored-by: Kibana Machine <42973632+kibanamachine@users.noreply.github.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[a1e46c5d31...](https://github.com/tgstation/tgstation/commit/a1e46c5d31347887de95520eee31c00749379b9c)
#### Saturday 2023-11-11 04:04:55 by Jacquerel

Basic Guardians/Holoparasites (#79473)

## About The Pull Request

Fixes #79485
Fixes #77552

Converts Guardians (aka Holoparasites) into Basic Mobs.
Changes a bunch of their behaviours into actions or components which we
can reuse.
Replaces some verbs it would give to you and hide in the status panel
with action buttons that you may be able to find more quickly.

They _**should**_ work basically like they did before but a bit
smoother. It is not unlikely that I made some changes by accident or
just by changing framework though.

My one creative touch was adding random name suggestions.
The Wizard federation have a convention of naming their arcane spirit
guardians by combining a colour and a major arcana of the tarot. The
Syndicate of course won't truck with any of that mystical claptrap and
for their codenames use the much more sensible construction of a colour
and a gamepiece.

This lets you be randomly assigned such creative names as "Sparkling
Hermit", "Bloody Queen", "Blue World", or "Purple Diamond".
You can of course still ignore this entirely and type "The Brapmaster"
into the box if so desired.

I made _one_ other intentional change, which is to swap to Mothblocks'
nice leash component instead of instantly teleporting guardians back to
you when they are pulled out of the edge of their range. They should now
be "dragged" along behind you until they can't path, at which point they
will teleport. This should make the experience a bit less disorienting,
you have the recall button if you _want_ to instantly catch up.

This is unfortunately a bumper-sized PR because it did not seem
plausible to not do all of it at once, but I can make a project branch
for atomisation if people think this is too much of a pain in the ass to
review.

Other changes:
- Some refactoring to how the charge action works so I could
individually override "what you can hit" and "what happens when you hit"
instead of those being the same proc
- Lightning Guardian damage chain is now a component
- Explosive Guardian explosive trap is now a component
- Added even more arguments to the Healing Touch component to allow it
to heal tox/oxy damage and require a specific click modifier
- Life Link component which implements the Guardian behaviour of using
another mob as your health bar
- Moved some stuff about deciding what guardians look and are described
like into a theming datum
- Added a generic proc which can return whether your mob is meant to
apply some kind of damage multiplier to a certain damage type. It's not
perfect because I couldn't figure out how ot cram limb modifiers in
there, which is where most of it is on carbons. Oh well.
- Riders of vehicles now inherit all movement traits of those vehicles,
so riding a charging holoparasite will let you cross chasms. Also works
if you piggyback someone with wings, probably.

## Changelog

:cl:
refactor: Guardians/Powerminers/Holoparasites now use the basic mob
framework. Please report any unexpected changes or behaviour.
qol: The verbs used to communicate with, recall, or banish your Guardian
are now action buttons.
balance: If (as a Guardian) your host moves slightly out of range you
will now be dragged back into range if possible, rather than being
instantly teleported to them.
balance: Protectors now have a shorter leash range rather than a longer
one, in order to more easily take advantage of their ability to drag
their charge out of danger.
balance: Ranged Guardians can now hold down the mouse button to fire
automatically.
balance: People riding vehicles or other mobs now inherit all of their
movement traits, so riding a flying mob (or vehicle, if we have any of
those) will allow you to cross chasms and lava safely.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [OceanAITeam/NSGA2--FSDRSA](https://github.com/OceanAITeam/NSGA2--FSDRSA)@[37330559cc...](https://github.com/OceanAITeam/NSGA2--FSDRSA/commit/37330559cce84a9ab348f687dcbbc187439a9534)
#### Saturday 2023-11-11 04:34:36 by OceanAITeam

Add files via upload

Tree release version (based on matrix) and some exploration (initialization method) —— exploration attempts for cold start

Use matrix-based tree structure storage method initialization method

**************************************************************************************************************************************************************************

Dear experts and engineers,

If our work has been helpful to you, we kindly ask that when you achieve outstanding research results, you cite the following paper in your references. Our entire team, including myself and 22 other members, would be very grateful.

Paper: "Dual-Side Disassembly Line Balancing Problem with Job Rest Time: Constraint Programming Model and Improved NSGA II Algorithm"

We will periodically update relevant materials and our thoughts. However, because our team is also undertaking some other research tasks (and may consider further sharing of dynamic multi-objective optimization, deep reinforcement learning, and deep learning technology applications in industry in the future), often with project engineering requirements, updates may be delayed. But with each update, we will not only upload code but also add some of our thoughts. Additionally, we have related research based on the NSGA2--FSDRSA algorithm that is currently in the preparation for publication stage, and after publication, we will gradually upload relevant materials. We also welcome experts to review them.

Once again, thank you for recognizing our work.

Sincerely,
The entire team

**************************************************************************************************************************************************************************

Motivation and approach: Recently, while having a meal, we discussed the effectiveness of our method. Through these discussions, our team believes that the reason our method is effective is because we have efficiently integrated the concept of "avoiding duplicate searches" with the characteristics of the problem we are solving. This conclusion came from a conversation between my friend Matthew and a senior professor. In their discussion, they mentioned the Monte Carlo search algorithm in AlphaGo, and he realized that the key idea used in the algorithm is to avoid duplicate searches. Then he thought about immune algorithms, ant colony algorithms, etc., and believed that they all incorporate mathematical formulas (such as distance calculation and search frequency calculation) to avoid duplicate searches during the search process. This inspired us, and we concluded that from an algorithmic perspective, our method does not deviate from this idea. Recently, in the actual engineering application process, our team also evaluated our method. We believe that the success of our method is because we have effectively integrated the above concept with the disassembly line balancing problem. In fact, many algorithms inadvertently incorporate the idea of avoiding duplicate searches. I personally believe that methods with this idea can achieve the same effect as our method, but the premise of achieving the effect of our method is to effectively integrate the concept of "avoiding duplicate searches" into the problem to be solved. For example, in ant colony algorithms, there is the concept of pheromones, and effectively integrating this concept with the characteristics of the disassembly line balancing problem is crucial.

---
## [eta-c/spotify-jam](https://github.com/eta-c/spotify-jam)@[11880304fa...](https://github.com/eta-c/spotify-jam/commit/11880304fa783274c135bd9d9a9109a8acd67c7f)
#### Saturday 2023-11-11 04:42:16 by Tykind

Locale update

Since my girlfriend isn't in the US, this had to be changed so it updates with it. Sorry to the countries that don't support it... But this is one way I could support a ton. You can request an issue, if enough are done I'll change it to be better :P

---
## [Deadondev/Cozis-Offworld-Wares](https://github.com/Deadondev/Cozis-Offworld-Wares)@[5b83fa3764...](https://github.com/Deadondev/Cozis-Offworld-Wares/commit/5b83fa37640e5fb0a4591710f445d85b67c0f0cc)
#### Saturday 2023-11-11 06:40:48 by Cozi

Huge November Update

Ahoy Destructors! Cozi here, back with another "oh god why the fuck did he add this?" Update!

I know it's been a while but quite bluntly I burned out hard on HD modding, kinda lost the vision on what I wanted with this project and didn't want to return until I felt I could actually set goals that I could meet, alongside starting to finish the projects I have started here. So far we have...

-Musket is a lot better animation-wise now, alongside having a "Gunk" system where the barrel will get too dirty causing inaccuracy and require cleaning using Alt. Reload + Alt. Fire, don't clean a loaded rifle! It won't work.
(Also make sure to ram multiple times! there's now a chance to fail :] )

Next up is Blue Rum, with matt's recent changes to how stims and such work, I had to rewrite the cleaner and now rum simply to get them into a spot I'm happier with. Cleaner's... The same. Blue Rum however is not.
You can now feed you downed friends blue rum with alt. fire! It's a bit WIP so I'll likely add some limitations and such (kinda thrown together but in fairness the whole update threw me off for a month)

Also, we've added Heartstopper Cigarettes! They're a loadout only item so far but you can use them to give a little of aggro damage, but balance out your heartbeat and relieve some stun. allowing you to stay cool under pressure!

The flintlock is while still missing good spriting, in a pretty okay spot now. They're the same as the musket, sans the failchance on ramming and needing to be cleaned more often due to the smaller barrel. It's alright, not my proudest work.

Defib Fans? Uh... Sorry nothing still there.

Anywho, thanks to everyone who tested and helped me with this, you guys are the best.

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[b77fa8c2a2...](https://github.com/LemonInTheDark/tgstation/commit/b77fa8c2a2490b43bf9174271ebfad72c4782d98)
#### Saturday 2023-11-11 07:00:34 by LemonInTheDark

Starlight Control (Aurora works now, space gas doesn't touch starlight, narsie ending effects) (#78877)

## About The Pull Request

[Implements a setter for starlight
variables](https://github.com/tgstation/tgstation/commit/af34f06b418b039b2ead90b29112b30adea4bc68)

I want to start to modify starlight more, and that means I need a way to
hook into everything that uses it and update it, so we can modify it on
the fly.

This does that, alongside removing space overlays from nearspace (too
many false positives) and making the aurora modify all turfs projecting
starlight, rather then all turfs in an area.

Do still need to figure out handling for the starlight color usage in
turf underlays tho (I gave up, we just keep it static. I'll fix it
someday but the render_relay strategy just doesn't work with its masking
setup)

[Reworks how starlight overlays
work](https://github.com/tgstation/tgstation/commit/9da4bc38e223e0ce2d91b0c8beddf1ebba968b9c)

Instead of setting color on the overlays directly, we instead store an
object with our current settings in every mob's screen, and
render_target it down onto our overlays.

This lets us update overlay colors VERY trivially. Just need to set
color on the overlay var. Makes modifying starlight a lot cheaper.

It doesn't work on area overlays, because suffering, and it MIGHT induce
extra cost on clients. if it does we can do something about that, we'll
play it by ear

[Removes parallax starlight
coloring.](https://github.com/tgstation/tgstation/commit/5f701a1b137c7d4c333929e4cbfdd9d4aa8656d6)

I'm sorta iffy on the color, the effect can be real oppressive in some
cases, and I'd like to use starlight color for more events in world, and
having it vary can make that looking nice hard.

[Adds some visual effects to narsie being
summoned](https://github.com/tgstation/tgstation/pull/78877/commits/a423cfcb2ba9c0d729b06c36dd7d38ff68c967c2)

As the rune drawing progresses space (starlight and parallax) go from
normal to greyscale. Then, right about when narsie shows up, starlight
becomes vibrant red.

It's a nice effect. I wanna do more shit like this, I think it'll
improve vibes significantly.
## Why It's Good For The Game

Can't embed it because of github's upload limit, can show a
[link](https://cdn.discordapp.com/attachments/458452245256601615/1160821856358645860/2023-10-08_22-31-22.mp4?ex=65360e99&is=65239999&hm=680e33e4e0026b89e132afc50c04a648a24f869eb662f274a381a5de5c5a36f2&)
for the narsie stuff

Here's
[one](https://cdn.discordapp.com/attachments/326831214667235328/1160813747196141568/2023-10-08_22-34-10.mp4?ex=6536070c&is=6523920c&hm=f8d571d1013da89887f49f3fec99f632251eeeac83085aa7dde97009aee3922f&)
for the aurora too.

This gives us more pretty starlight shit, and the ABILITY to do more
pretty starlight shit. I'm pretty jazzed, and I hope people use this
proc more (keeping in mind that it's pretty hard on the lighting system,
and needs significant delay between changes)
## Changelog

🆑
add: Narsie summoning has had some effects added to space and starlight
del: Removes the link between spacegas color and starlight. It was a
slight bit too vibrant and I think impacted the vibe too wildly to be
incidental.
fix: The aurora event actually... works now. Space lights up and all
that
/🆑

---
## [pawan4488/SQL_HR_ANALYST](https://github.com/pawan4488/SQL_HR_ANALYST)@[294596f3e9...](https://github.com/pawan4488/SQL_HR_ANALYST/commit/294596f3e92b333a3be3b3c83e6ccc500d85fe1a)
#### Saturday 2023-11-11 07:20:54 by pawan4488

HR_ANALYST

These are some insights have been driven from this.
1. 89 of the employee's who left the organization came from the similar educational background that is Life Sciences.
2. 26-35 is the age group where more no. of employee's left the job.
3.Avg age of the Employee is 37 
4. According to gender male is almost 2x in numbers comparing with female who left the job.
5. Attrition rate of the Employee is 16.12%
6. Organization should think about R&d because it's having more attrition rate 56% of total attrition

---
## [cwmaguire/exif_photo_org](https://github.com/cwmaguire/exif_photo_org)@[9ce5f901d0...](https://github.com/cwmaguire/exif_photo_org/commit/9ce5f901d0c33c38e9847baab93f1438ee1568b4)
#### Saturday 2023-11-11 08:27:31 by Chris Maguire

Add all code to date

NOTE: currently the files are not copied; a filename is created with
touch to simulate what would happen for testing.

Main file:
- photo_org.sh

  Currently I'm running it with this:

  find pics -iname "*.jpg" -or -iname "*.heic" -or -iname "*.png" \
    -exec ./photo_org.sh pics3 {} \; | tee log2

Function files:
- everything else

Goal:
Copy all photo files from one unorganized directory tree of files into
an organized tree of files with standard names using EXIF info.

Files are organized by year and month according to the EXIF information
in this order:
1) CreateDate
2) ModifyDate
3) DateCreated
4) FileModifyDate
5) or the file is not copied

Files are named D_M_N_Q_S.ext where
D = yyyy_mm_dd_hh_MM_ss_
M = model
N = EXIF FileNumber
Q = EXIF SequenceNumber
ext = original file extension

Model comes from:
1) "thumbnail" if the filename contains "thumbnail"
2) "preview" if the filename contains "preview"
3) first word of EXIF Software, e.g. Picasa
4) first 2 words of LensModel, e.g. iPhone 5s
5) filename keywords:
  1) webcam      -> webcam
  2) iphone      -> iPhone
  3) scan        -> scanned
  4) z2          -> dImage_Z2
  5) argus       -> argus
  6) /micro/     -> USB_microscope
  7) smugmug     -> smugmug
  8) screen shot -> screenshot
6) "webcam" if the EXIF Comment contains "webcam"

Notes to myself on BASH:
- wrap params to functions in double quotes
  - or capture all possible params in the function with $@ / $*
- lowercase vars with ${var,,}
- uppercase vars with ${var^^}
- turn params into var references with "declare -n var=$1"
- pipes are run in subshells, so piping to readarray assigns to a var in
  a subshell
- replace var chars with ${var/x/y}
- get substrings or array slices with ${var:x} or ${var:x:y}
  - can use a var for x or y, e.g. ${var:${var2}:${var3}}
- match in if [[ ... ]] with =~
  - note that quotes are not required
  - use a var for wonky stuff

---
## [Offroaders123/Menu-Drop](https://github.com/Offroaders123/Menu-Drop)@[8ca901d537...](https://github.com/Offroaders123/Menu-Drop/commit/8ca901d53782e5c06cbc9d3cd7246e8fc2439695)
#### Saturday 2023-11-11 08:54:16 by Offroaders123

Vite Dev Server

Figured out how to use Vite to demo working on the component! I'm surprised I haven't figured this out yet, it works really well. This also finally allows everything to work locally, since it uses npm for loading the Constructable Stylesheets and ES Module Shims polyfills.

Once the dev server is running in a terminal tab, note that you have to navigate specifically to `http://localhost:5500/test/index.html`, since the main HTML file isn't in the root of the project, because I want to use it only for testing things out.

https://vitejs.dev/guide/#index-html-and-project-root

I had to add `skipLibCheck` because the Constructable Stylesheets Polyfill has overlapping types with the standard library now, unfortunately. So everything was working good with Vite and all (type-wise), but the regular lib defintions were overlapping with each other, since TS natively added types for `document.adoptedStyleSheets`. I can look into making an issue/PR to the polyfill to make it work accordingly with newer TS versions.

I had to add `?inline` to make Vite happy for the CSS Module Scripts import. I am going to look into a way to get around that issue, as I don't want to enforce needing to use that for users that don't use Vite. That query parameter could mean something else by chance on their server, or something like that.

Oh yeah, and turns out I needed `rootDir`/`exclude` for the `tsconfig` because of each Web Component's use of `declare global { interface HTMLElementTagNameMap {} }`, since it defines the tag names on the global scope, and the output JS and types in `./dist` clash with the `./src` definitions, so that causes a type collision issue as well. Aag! I'm gonna look into seeing how Lit element components deal with that, maybe they also `exclude` the `dist` directory. I didn't want to use `rootDir` because I wanted to apply type checking to the TS files in `./test`, like how I'm doing for my other projects. That was one of the benefits with moving to Vite, that I can type check the demo files as well, and use full TS, and also not need to run `tsc` in parallel to the dev server. Instead the server (Vite) can handle the transpilation for me :) All about that simple abstraction :)

---
## [pforret/jekyll.forret.com](https://github.com/pforret/jekyll.forret.com)@[5e41b84785...](https://github.com/pforret/jekyll.forret.com/commit/5e41b84785834eb935938aaddc59bf1de3614fac)
#### Saturday 2023-11-11 09:24:49 by Peter Forret

ADD: magazine.md wired.md, MOD: version.html 2004-02-24-wacluster-newest-sibling-in-the-wautilswinadmin-family.md 2004-03-11-pypersomail-updated-to-v02.md 2004-04-20-moodlex-ableton-live.md 2004-05-03-no-life-without-curls.md 2004-05-06-a-pentium-4-is-not-necessarily-a-pentium-4.md 2004-05-12-feed-based-automatic-downloadcaching.md 2004-05-19-converge-already-struggling-with-wlbs.md 2004-05-24-organizing-my-cd-collection.md 2004-06-01-port-redirection-in-windows.md 2004-06-04-collaborative-filtering-on-dating-sites.md 2004-06-10-cool-speakers-bose-personalized-amplification-system.md 2004-06-17-50-coolest-song-parts-ever.md 2004-06-18-bum-titty-bum-limerick-toolbox.md 2004-06-21-fix-by-disabling-error-1016-in-event-log.md 2004-06-23-oh-nokia-wont-you-make-me-a-nice-mobile-phone.md 2004-06-25-doctorow-drm-is-evil.md 2004-07-12-swastikas-drawn-on-woman-in-paris-attack.md 2004-08-08-imperial-time-units-here-come-the-nunes.md 2004-08-11-moiano-teaches-soulschool.md 2004-08-27-blogs-and-wikis-how-about-a-bliki.md 2004-09-15-japanese-lesson-in-rock-n-roll.md 2004-09-23-the-last-pinguin-to-drink-coffee.md 2004-09-26-i-remember-house-before-it-was-techno.md 2004-10-03-adobe-authors-digital-negative-dng-standard.md 2004-10-04-google-is-listening-searching-audio.md 2004-10-10-intelligence-is-the-minds-worst-enemy.md 2004-10-11-casablanca-heres-looking-at-you.md 2004-10-19-redhat-versions-what-am-i-running.md 2004-10-19-squid-list-top-x-referers.md 2004-10-21-estimate-of-lines-in-a-log-file.md 2004-10-21-probe-average-cpu-utilisation-mrtg.md 2004-10-27-delicious-library-no-we-dont-like-microsoft.md 2004-10-31-more-is-better-the-quintuple-neck-guitar.md 2004-11-01-its-the-latency-stupid.md 2004-11-02-date-formatting-in-gawk-boot-time.md 2004-11-08-it-conversations-podcasting-feeds-your-brain.md 2004-11-08-squid-cachemgrcgi-ui-hack.md 2004-11-25-idea-using-a-uri-for-sending-email.md 2004-11-29-how-do-you-move-a-terabyte.md 2004-12-04-podcast-as-muzak-replacement.md 2004-12-10-domain-registry-of-america-scam.md 2005-01-04-information-overload-blog-filtering.md 2005-01-05-wired-magazine-in-belgium-expensive-habit.md 2005-01-09-just-a-little-lovin-early-in-the-morning.md 2005-01-09-podcast-for-business-authenticated-podcatching.md 2005-01-10-podcast-pepsi-challenge-doing-it-in-the-car.md 2005-01-16-rediscovering-meshell-ndegeocello.md 2005-01-18-dave-winers-problem-and-solution.md 2005-01-20-mr1200-mp3-player-for-djs.md 2005-01-21-perl-html-scraping-part-1.md 2005-01-24-popular-belgian-blogs-the-preliminary-top-25.md 2005-01-25-busy-being-born-the-mac-user-interface.md 2005-01-31-popular-belgian-blogs-top-25-v2.md 2005-02-04-binary-confusion-kilobytes-and-kibibytes.md 2005-02-06-folksonomizer-generic-folksonomy-service.md 2005-02-07-popular-belgian-blogs-version-3.md 2005-02-08-tango-steps-and-twister.md 2005-02-09-what-women-want.md 2005-02-11-sue-your-customers.md 2005-02-12-cd-to-mp3-ripping-speed-estimation.md 2005-02-18-domain-names-in-flanders-and-wallonie-the-digital-divide.md 2005-02-19-quoteplay-and-portable-smil.md 2005-03-04-hybrid-cd-making-it-run-on-mac-and-pc.md 2005-03-11-itunes-and-id3-tags.md 2005-03-20-removal-of-serflogsumom-worm.md 2005-04-05-googlistics-messing-with-the-big-g.md 2005-04-24-instant-ken-and-barbie-melanotan-to-the-rescue.md 2005-04-28-know-your-metric-limits.md 2005-04-30-old-style-nigerian-scam-via-fax.md 2005-05-09-req-live-mashup-performance-tool.md 2005-05-19-installing-ntp-time-synchronisation.md 2005-05-20-la-gamba-sinistra-italian-tango.md 2005-05-23-jobs-announces-podcasts-in-itunes.md 2005-05-27-genesis-of-some-famous-sounds.md 2005-05-30-propaganda-podcast-creation-tool-by-mixmeister.md 2005-06-07-sudoku-solver-tool.md 2005-06-15-convert-bind-dns-zone-into-ptr-records.md 2005-06-16-internet-activity-in-the-eu.md 2005-06-20-rss-with-images-picture-podcasting.md 2005-07-17-bentzon-brotherhood-rappers-new-delight.md 2005-07-29-moroccan-blue-leads-top-fashion-colors-rgb.md 2005-07-31-digital-cinema-one-step-closer.md 2005-08-03-guitar-fretboard-generator-name-that-fret.md 2005-08-04-digital-filmmaking-cheaper-movies.md 2005-08-18-photofeed-image-podcasting.md 2005-08-27-automated-initial-image-tagging-ojos-inc.md 2005-09-02-flickr-changes-image-urls-with-some-glitches.md 2005-09-05-brusselse-stadsblog-gaat-van-start.md 2005-09-11-pareto-doesnt-do-search.md 2005-09-19-brussels-bloggers-meeting-on-oct-7.md 2005-09-27-blogging-its-all-about-conversations.md 2005-09-28-wizarss-a-wizard-player-based-on-rss.md 2005-09-29-web-20-mememap-overview.md 2005-10-12-get-ready-for-video-podcasting.md 2005-10-13-lost-in-itunes-good-and-bad-news.md 2005-10-16-belgium-does-not-need-earlier-retirement.md 2005-10-18-public-wifi-the-on-line-consumer.md 2005-10-19-jason-fried-lessons-learned-building-basecamp.md 2005-10-20-jakob-nielsen-design-mistake-5.md 2005-10-21-my-blogs-roi.md 2005-10-23-wealthy-belgian-bloggers-the-blog-dollars-top-60.md 2005-10-26-contextual-advertising-without-javascript.md 2005-10-27-open-wifi-hotspots-in-brussels.md 2005-10-30-spam-economics-government-role.md 2005-10-31-web-20-nieuwe-trends-in-web-projecten.md 2005-11-01-avoiding-wiki-spam-in-mediawiki.md 2005-11-02-adsense-in-all-media-tv-cinema-sport-traffic.md 2005-11-03-oakland-installs-free-municipal-wifi.md 2005-11-04-how-not-to-do-copy-protection-sony-music.md 2005-11-09-folksonomy-and-google-bombs.md 2005-11-10-adam-curry-goes-100-podsafe.md 2005-11-11-wealthy-belgian-bloggers-v3.md 2005-11-12-its-so-cool-to-be-anti-web-20.md 2005-11-15-consumers-digital-rights.md 2005-11-17-wiki-markup-languages-syntax-confusion.md 2005-11-18-google-turning-cash-into-cache.md 2005-11-23-filling-a-terabyte-ipod.md 2005-11-24-google-toppers-pick-your-title-carefully.md 2005-11-29-professional-communicator.md 2005-12-01-municipal-wifi-requirements-for-success.md 2005-12-02-lets-get-rid-of-podkeywordcom.md 2005-12-08-two-days-at-lesblogs-paris.md 2005-12-13-rfm-for-rss-feeds-recency-frequency-momentary-value.md 2005-12-14-the-mpa-and-other-peoples-money.md 2005-12-15-google-experiments-with-inline-revisions.md 2005-12-15-google-introduces-music-search.md 2005-12-16-new-podcast-icons-based-on-firefoxie-feed-logo.md 2005-12-23-migrating-from-blogspot-to-a-real-blog.md 2005-12-25-christmas-present-podcast-feed-validator.md 2005-12-27-thought-dmca-was-bad-heres-dtcs.md 2005-12-28-diy-web20-flowchart-generator.md 2006-01-07-magnus-jumpneedle-drummers.md 2006-01-09-geek-love-checklist.md 2006-01-11-apple-reinvents-photocasting-in-ilife-06.md 2006-01-13-superthriller-concert-in-botanique.md 2006-01-15-apple-creates-rss-the-microsoft-way.md 2006-01-19-recent-posts-comments-in-blogger.md 2006-01-20-the-top-10-reasons-why-web-20-is-like-disco.md 2006-01-24-why-spam-opt-out-lists-wont-work.md 2006-02-03-entrepreneurship-20.md 2006-02-11-lexmark-printers-with-hardware-error-0502.md 2006-02-14-user-generated-media-is-intels-wet-dream.md 2006-02-16-the-riaa-shoots-itself-in-the-foot-again.md 2006-02-17-broadband-in-brussels.md 2006-02-21-the-next-german-top-model-will-be-thin.md 2006-02-26-migrating-from-blogger-to-wordpress-20.md 2006-02-28-ancienne-belgique-rocks.md 2006-02-28-black-eyed-peas-lose-da-humps.md 2006-02-28-lalalover-troubles-and-fights.md 2006-02-28-shockabsorber-baywatch-and-science.md 2006-03-01-together-facing-the-new-totalitarianism.md 2006-03-04-digital-cinema-movie-distribution.md 2006-03-07-saving-the-net-doc-searls.md 2006-03-09-blogger-snafu-emergency-migration-to-wordpress.md 2006-03-09-google-buys-writely.md 2006-03-14-bmi-is-not-perfect.md 2006-03-15-req-more-being-spaces-in-brussels.md 2006-03-16-1969-was-an-inspiring-year.md 2006-03-17-who-knows-a-spam-pigeon.md 2006-03-19-barcamp-brussels-may-2006.md 2006-03-22-web-based-web-development.md 2006-03-24-moving-up-the-feed-chain.md 2006-03-28-google-files-patents-for-contextual-wifi-advertising.md 2006-03-29-size-doesnt-matter.md 2006-03-30-google-moving-into-interactive-tv.md 2006-03-31-storing-the-sql-queries-in-the-database.md 2006-04-04-barcamp-brussels-may-20-2006.md 2006-04-06-adsense-also-looks-at-search-terms.md 2006-04-07-pdf-podcasts-proof-of-concept.md 2006-04-12-ivi-internet-voor-iedereen.md 2006-04-13-double-wifi-municipal-wifi-with-protection.md 2006-04-14-bluehost-vs-dreamhost.md 2006-04-19-pleasure-from-da-bass-memorable-bass-lines.md 2006-04-22-blogcom-antwerp-pings-and-comments.md 2006-04-24-barcamp-brussels-less-than-a-month-to-go.md 2006-04-25-emma-marie-and-julie.md 2006-04-26-adsense-the-long-tail-of-spare-change.md 2006-04-27-100-essential-movies.md 2006-04-27-click-to-hear-the-mp3-playlist.md 2006-05-03-play-us-a-slow-song.md 2006-05-04-youtube-bandwidth-terabytes-per-day.md 2006-05-05-database-war-stories-db-vs-square-files.md 2006-05-09-barcamp-brussels-10-days-to-go.md 2006-05-10-rails-conference-in-london-whos-coming.md 2006-05-11-beyond-the-megapixel.md 2006-05-11-mission-impossible-iii-largest-digital-release-ever.md 2006-05-14-bouncing-email.md 2006-05-16-barcamp-brussels-get-ready.md 2006-05-16-lies-damned-lies-and-google-trends.md 2006-05-18-the-photo-must-link-back-to-its-photo-page.md 2006-05-19-barcamp-brussels-getting-there.md 2006-05-23-barcamp-brussels-when-the-day-is-done.md 2006-05-24-convergence-of-the-ipod.md 2006-05-27-invent-dont-inhibit.md 2006-06-02-on-the-origin-of-speeches.md 2006-06-07-estimating-real-time-traffic-speed.md 2006-06-14-myers-briggs-typology-im-an-enfp.md 2006-06-16-more-fun-with-myers-briggs.md 2006-06-21-first-rubyonrails-seminar-itworks.md 2006-06-24-google-and-perfect10-dmca-at-its-best.md 2006-06-28-owner-of-the-amen-break.md 2006-06-30-trackback-wizard-for-blogger-users.md 2006-07-06-how-to-visualize-a-timeline.md 2006-07-10-netgear-sc-101-urgent-support-required.md 2006-07-12-brussels-traffic-is-kinda-safe.md 2006-07-19-the-five-factor-personality-profile.md 2006-07-27-barcamp-brussels-2-on-sunday-sept-24th.md 2006-08-14-a-sudoku-challenge-generator.md 2006-08-15-ipod-in-2009-more-storage-or-bandwidth.md 2006-08-16-rule-of-thirds-for-powerpoint.md 2006-08-17-interestingness-for-google-web-search.md 2006-08-20-pukkelpop-2006.md 2006-08-21-brussels-tango-on-google-calendar.md 2006-08-22-tangotation-writing-tango-steps.md 2006-08-23-how-to-upsize-an-image.md 2006-08-25-colorbar-belgian-spam.md 2006-08-28-no-more-smoking-in-restaurants.md 2006-08-29-five-seo-excuses.md 2006-08-31-youtube-for-pdf-embedding-documents.md 2006-09-01-intrusive-google-ads-on-sourceforge.md 2006-09-06-easy-web-page-mockup-tool.md 2006-09-07-moldover-live-mashup-dj.md 2006-09-11-barcamp-brussel-is-approaching.md 2006-09-12-more-globalisation-please.md 2006-09-14-context-aware-mobile-devices.md 2006-09-14-ibc-amsterdam-bigger-better-faster.md 2006-09-14-styles-should-not-be-referenced-by-a-link.md 2006-09-15-fancy-wordpress-themes-on-dreamhost.md 2006-09-19-barcamp-brussels-this-sunday.md 2006-09-20-wp-cache-speeds-up-your-wordpress.md 2006-09-27-hd-720p-1080i-and-1080p.md 2006-09-30-coditel-digital-television.md 2006-10-02-pixar-dreamworks-synchronized-imagination.md 2006-10-03-helping-martin-luther-king-jr-a-hand.md 2006-10-05-being-multilingual-in-belgium.md 2006-10-16-a-picture-a-day-flickrs-storage-growth.md 2006-10-17-dreamhost-has-better-performance-now.md 2006-10-23-le-web-3-in-paris.md 2006-10-25-myspace-bulletin-and-other-spam.md 2006-10-26-brussels-statistics-atlas-2006.md 2006-10-30-our-customers-are-the-perverts-not-us.md 2006-11-02-thank-you-for-smoking.md 2006-11-03-import-excel-into-google-spreadsheets.md 2006-11-03-mobile-etiquette-caller-id.md 2006-11-06-big-bazooka-xl-gaming-kinepolis.md 2006-11-09-leweb3-a-dozen-belgians-in-paris.md 2006-11-20-babel-japanese-september-remix.md 2006-11-20-thalys-to-amsterdam-is-way-too-slow.md 2006-11-21-yahoo-should-sell-flickr-to-google.md 2006-11-27-the-popular-canon-400d.md 2006-12-02-mark-king-plays-a-mean-bass.md 2006-12-05-digital-cinema-advertising-and-me.md 2006-12-08-megapixel-myth-nuances.md 2006-12-10-off-to-leweb3.md 2006-12-12-leweb3-is-actually-loic-for-president.md 2006-12-13-there-are-no-flash-websites.md 2006-12-14-leweb3-the-babel-effect.md 2006-12-20-countdown-to-no-smoking.md 2007-01-03-lots-of-new-years-pictures.md 2007-01-12-popurls-why-i-like-reddit-and-delicious-better-than-digg.md 2007-01-16-mrtg-data-in-xml-format.md 2007-01-18-eu-domain-speculation.md 2007-01-19-my-own-pagerank-inventory.md 2007-01-23-paypal-ready-shops-in-benelux.md 2007-01-26-to-upsize-a-picture-use-the-b-spline-algorithm.md 2007-02-02-shades-of-purple.md 2007-02-04-viral-in-the-bad-sense-messengerchecker.md 2007-02-14-you-give-out-your-passwords-every-day.md 2007-02-16-adultery-and-secure-documents.md 2007-02-16-yahoo-pipes-get-remix-deliver-model.md 2007-02-21-pipes-sql-structured-web-query-language-swql.md 2007-02-28-hollywood-movie-studios.md 2007-03-08-barcamp-brussels-3-may-5th-in-the-marolles.md 2007-03-08-ghost-rider-fire-and-cleavage.md 2007-03-14-dream-turned-to-nightmare.md 2007-03-15-urlrewrite-for-wordpress-on-lighttpd.md 2007-03-16-govern-yourselves-accordingly.md 2007-03-16-the-top-20-bloggers-in-flanders.md 2007-03-19-printing-an-mp3-on-a4s.md 2007-03-22-100000-flickr-views.md 2007-03-23-tonight-bwards-in-antwerp.md 2007-03-24-bwards-url-overload.md 2007-03-25-countdown-to-brussels-tango-festival.md 2007-03-30-equal-pay-day.md 2007-04-05-package-delivery-20.md 2007-04-06-barcamp-brussels-one-month-to-go.md 2007-04-10-interpersonal-intelligence-and-mental-violence.md 2007-04-12-twitter-watch-your-mouth.md 2007-04-18-reinventing-the-wheel-twitter-backchannel.md 2007-04-25-creating-a-tango-calendar.md 2007-04-26-your-twitter-quotient-tq.md 2007-04-27-plan-your-alcohol-consumption.md 2007-05-10-prefab-sprout-steve-mcqueen-legacy-edition.md 2007-06-11-the-godfather-of-disco.md 2007-06-12-the-barcamp-video-saga-background.md 2007-06-13-what-american-accent-do-you-have.md 2007-06-14-new-beta-youtube-layout.md 2007-06-15-one-continuous-line-movie.md 2007-06-20-pimp-your-laptop-apple-vs-dell.md 2007-07-01-whisher-exchange-passwords-to-share-wifi.md 2007-07-02-my-first-facebook-spam.md 2007-07-03-living-photographs-by-andrew-mole.md 2007-07-04-redirecting-with-apaches-htaccess.md 2007-07-05-the-good-wifes-guide.md 2007-07-05-web-tool-visualize-on-google-maps.md 2007-07-06-lg-ku-800-have-low-expectations.md 2007-07-24-arno-on-the-francofolies.md 2007-07-24-my-city-your-city-brussels.md 2007-07-26-test-your-karma-early-in-the-morning.md 2007-08-06-point-and-shoot-badly.md 2007-08-07-my-personaldna.md 2007-08-13-k2-sidebar-modules-vs-widgets.md 2007-08-21-weekday-colours-ayurveda.md 2007-08-22-what-google-agenda-currently-misses.md 2007-08-23-my-first-picture-in-the-papers.md 2007-08-29-id3exe-ideal-tool-for-tagging-and-renaming-mp3-files.md 2007-09-04-if-kate-moss-and-inspector-morse-had-a-baby.md 2007-09-06-the-sneaky-shall-inherit-the-earth.md 2007-09-14-fight-for-kisses.md 2007-09-17-porque-te-vas.md 2007-09-28-two-dice-make-a-calendar.md 2007-10-08-what-is-hd-jpeg.md 2007-10-15-announced-barcamp-brussels-4.md 2007-10-18-logitech-online-store-haunted.md 2007-10-27-tomtom-one-beauty-with-short-breath.md 2007-10-31-barcamp-where-4.md 2007-11-09-learning-bulgarian-in-an-hour.md 2007-11-19-buying-an-hd-ready-tv.md 2007-11-22-barcamp-brussels-4-10-days-to-go.md 2007-11-26-number-17.md 2007-12-06-mivb-en-google-transit.md 2008-01-05-tv-tip-californication.md 2008-01-07-wd-my-book-is-not-really-pro-storage.md 2008-01-25-pecha-kucha-brussels.md 2008-01-29-tasting-whisky.md 2008-02-02-new-lens-for-my-canon.md 2008-02-08-screenshots-of-a-dvd-with-ffmpeg.md 2008-02-28-apple-trailers-when-720p-isnt-always-720p.md 2008-03-04-photography-workflow-with-picasa-flickr.md 2008-03-05-brudio-stussel-studio-brussel-vs-tien-om-te-zien.md 2008-04-16-fm-brussel-playlist-live-on-twitter.md 2008-04-17-my-ipod-nano-cannot-be-unlocked.md 2008-04-21-a-jpeg-picture-doesnt-care-about-no-dpi.md 2008-04-24-drupalpress-matt-vs-dries.md 2008-04-28-favourite-podcasts-basic-soul-radio-show.md 2008-04-30-netgear-readynas-nas-done-right.md 2008-05-13-tvh-likes-women.md 2008-06-03-lightbox-for-photo-feeds.md 2008-06-04-procreate-to-win-a-car.md 2008-07-14-twitter-spammers-clickbankkeynetics-affiliates.md 2008-08-22-hip-hop-is-different.md 2008-08-28-the-early-days-of-ebook-piracy.md 2008-09-17-stuff-to-install-on-a-new-windows-pc.md 2008-09-26-touched-by-the-ipod.md 2008-10-28-calendarburner-feedburner-for-ical-calendars.md 2008-10-31-five-tips-for-taking-tango-pictures-in-dark-environments.md 2009-01-29-dont-send-me-a-video-send-me-a-link.md 2009-02-13-create-your-own-iphone-ring-tones.md 2009-04-25-ac-adaptors-standardize-please.md 2009-07-14-my-quest-for-lets-get-lost-chet-baker-by-bruce-weber.md 2009-08-05-seths-bandwidth-vs-synchronicity-graph-its-a-start.md 2009-08-19-wordle-and-famous-movies.md 2009-08-20-imagine-a-virtual-iphone-for-everyone.md 2009-11-16-idea-preview-service-for-url-shorteners.md 2009-11-17-iphone-bandwidth-orders-of-magnitude.md 2009-12-01-newscorp-is-indeed-dropping-out-of-google.md 2010-01-02-fax-2-0-because-fax-wont-die-in-the-internet-age.md 2010-05-26-idea-hosted-classification-service.md 2010-09-22-droa-the-saga-continues.md 2010-10-22-fix-for-error-15000-remote-speakers-on-itunes-windows-7.md 2010-11-13-droa-now-with-a-belgian-lawyer.md 2011-01-08-how-to-delete-old-data-in-google-calendar.md 2011-01-13-shooting-portraits-of-strangers.md 2011-01-29-tv-show-scoring-the-decline-of-true-blood.md 2011-04-16-track-your-synology-nas-when-its-stolen.md 2011-07-14-google-docs-infamous-moved-temporarily-error-fixed.md 2011-07-14-repairing-amazon-s3-downloads-for-ie.md 2012-01-20-bose-soundlink-ideal-travel-companion.md 2012-04-03-company-cars-in-belgium.md 2012-04-20-emoticon-for-innuendo.md 2012-10-10-ios6-losing-its-3g-cellular-data-settings-fix-for-belgium.md 2012-10-29-cleaning-up-an-infected-php-server-malbadsrc-m-trojphpshll-b.md 2012-12-31-ll-and-rr-glasses-on-a-3d-screen.md 2013-09-11-status-page-for-telecominternet-providers.md 2013-11-11-blackwhite-video-thermography.md 2013-11-19-wifi-in-my-car-proof-of-concept.md 2015-05-21-reset-your-oneplus-one-to-factory-settings.md 2015-06-10-getting-rid-of-google-play-services-has-stopped-on-oneplus.md 2015-10-13-extended-mrtg-format.md 2016-07-08-idea-short-term-unified-group-messaging-enterprise.md 2016-12-03-idea-using-a-helpdesk-app-as-an-applicant-tracking-system-ats.md 2017-02-11-diy-my-bamboo-usb-ssd-disk-bay.md 2017-03-08-geen-ongewenste-reclame.md 2017-09-21-how-to-add-cloudflare-ssl-to-a-wordpress-website.md 2017-11-07-speed-test-of-samsung-external-ssds-t1-t3-and-t5.md 2018-02-15-the-sorry-state-of-keyboard-layout-management.md 2018-03-13-gdpr-plugins-for-wordpress.md 2018-05-04-tango-photography-gdpr.md 2018-06-03-bash-boilerplate-generator.md 2018-11-05-gdpr-spam.md 2018-11-21-cloud-connected-charger.md 2019-11-03-tool-to-look-up-emojis.md 2019-11-22-ten-tips-to-take-better-low-light-photos-lessons-from-tango-paparazzo.md 2020-01-11-nuuz-io-has-fans-in-russia.md 2020-01-16-when-the-api-returns-images.md 2020-03-05-hosting-a-laravel-project-on-gandi.md 2020-04-06-easy-site-deployment-on-gandi.md 2020-04-25-securely-manage-multiple-wordpress-blogs.md 2020-05-25-qr-experiments-qroulette.md 2020-05-30-simple-remote-portrait-photography.md 2020-06-06-web-services-on-the-command-line.md 2020-07-04-best-way-to-upscale-low-resolution-photos.md 2020-07-28-bashful-thinking-a-newsletter-for-bash-enthusiasts.md 2020-07-31-package-version-management-with-semver-sh.md 2020-10-07-splashmark-easy-unsplash-image-markup-on-the-command-line.md 2020-12-10-private-repos-on-laravel-forge-spark-and-mailcoach.md 2020-12-19-using-homebrew-on-apple-silicon-m1-natively.md 2021-01-14-cpu-benchmark-apple-silicon-m1.md 2021-01-21-creating-image-reveal-videos-with-ffmpeg-and-primitive.md 2021-02-14-every-country-in-the-world-in-1-unsplash-photo.md idea.md podcast.md podcast.md

---
## [pranabendra/langchain](https://github.com/pranabendra/langchain)@[dff24285ea...](https://github.com/pranabendra/langchain/commit/dff24285eaf6d102b1ff913274d18379d8aeeb21)
#### Saturday 2023-11-11 10:03:42 by Nikhil Jha

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
## [NotSamus/Axolots](https://github.com/NotSamus/Axolots)@[b9a10d6746...](https://github.com/NotSamus/Axolots/commit/b9a10d6746544b841da245fa0b246b5742c1b5f8)
#### Saturday 2023-11-11 10:40:30 by NotSamus

this is the last version we worked on, god bless alex ass if this code runs

---
## [Djonker83/Python](https://github.com/Djonker83/Python)@[a82f1576c3...](https://github.com/Djonker83/Python/commit/a82f1576c32bc3497afa6cb67bdf2f28ce4a2f91)
#### Saturday 2023-11-11 11:21:55 by Purshotam Bohra

Create gstin_scraper.py

Hello owners, this is just a small and beautiful script (pun intended) that demonstrates use of beautifulSoup to extract practical data.

GSTIN, short for Goods and Services Tax Identification Number, is a unique 15 digit identification number assigned to every taxpayer (primarily dealer or supplier or any business entity) registered under the GST regime in INDIA.

I created this script back in 2021, when one of my brother required this for his startup business and today when I saw this repo and it's inclusiveness for all sorts of crazy python script I desired to include this crazy adventure of mine.

Although the original version was bit messier but I refactored it according to current best standards.

Hope for a positive commity commity.

Thank you so much,
Purshotam Bohra

---
## [pforret/jekyll.forret.com](https://github.com/pforret/jekyll.forret.com)@[664c2613fe...](https://github.com/pforret/jekyll.forret.com/commit/664c2613fee0a00502fc9b6f9ce7c0c33b580350)
#### Saturday 2023-11-11 11:45:12 by Peter Forret

ADD: prey.md streaming.md tracking.md, DEL: 2004-06-23-oh-nokia-wont-you-make-me-a-nice-mobile-phone.md 2004-10-27-delicious-library-no-we-dont-like-microsoft.md 2005-09-27-blogging-its-all-about-conversations.md 2005-10-21-my-blogs-roi.md 2006-05-10-rails-conference-in-london-whos-coming.md popularity.md studiobrussel.md, MOV: meme.md, MOD: footer.html version.html 2004-08-27-blogs-and-wikis-how-about-a-bliki.md 2004-10-10-intelligence-is-the-minds-worst-enemy.md 2004-10-11-casablanca-heres-looking-at-you.md 2004-11-01-its-the-latency-stupid.md 2005-01-09-just-a-little-lovin-early-in-the-morning.md 2005-01-18-dave-winers-problem-and-solution.md 2005-07-17-bentzon-brotherhood-rappers-new-delight.md 2005-07-29-moroccan-blue-leads-top-fashion-colors-rgb.md 2005-09-11-pareto-doesnt-do-search.md 2005-11-12-its-so-cool-to-be-anti-web-20.md 2005-12-02-lets-get-rid-of-podkeywordcom.md 2005-12-14-the-mpa-and-other-peoples-money.md 2005-12-23-migrating-from-blogspot-to-a-real-blog.md 2005-12-27-thought-dmca-was-bad-heres-dtcs.md 2006-01-11-apple-reinvents-photocasting-in-ilife-06.md 2006-01-24-why-spam-opt-out-lists-wont-work.md 2006-02-14-user-generated-media-is-intels-wet-dream.md 2006-03-29-size-doesnt-matter.md 2006-05-05-database-war-stories-db-vs-square-files.md 2006-05-27-invent-dont-inhibit.md 2006-06-14-myers-briggs-typology-im-an-enfp.md 2006-07-12-brussels-traffic-is-kinda-safe.md 2006-10-16-a-picture-a-day-flickrs-storage-growth.md 2007-01-03-lots-of-new-years-pictures.md 2007-03-19-printing-an-mp3-on-a4s.md 2007-07-04-redirecting-with-apaches-htaccess.md 2007-07-05-the-good-wifes-guide.md 2008-01-07-wd-my-book-is-not-really-pro-storage.md 2008-02-08-screenshots-of-a-dvd-with-ffmpeg.md 2008-02-28-apple-trailers-when-720p-isnt-always-720p.md 2008-03-05-brudio-stussel-studio-brussel-vs-tien-om-te-zien.md 2008-04-21-a-jpeg-picture-doesnt-care-about-no-dpi.md 2009-01-29-dont-send-me-a-video-send-me-a-link.md 2009-07-14-my-quest-for-lets-get-lost-chet-baker-by-bruce-weber.md 2009-08-05-seths-bandwidth-vs-synchronicity-graph-its-a-start.md 2011-04-16-track-your-synology-nas-when-its-stolen.md 2011-07-14-google-docs-infamous-moved-temporarily-error-fixed.md about.md apple.md audio-video.md bandwidth.md belgium.md devops.md google.md hardware.md linux.md mobile.md nl.md scripting.md smartphones.md technology.md webdev.md apple.md bandwidth.md belgium.md blog.md blogger.md bloggers.md blogosphere.md flickr.md google.md linux.md meme.md music.md photography.md storage.md

---
## [defr0std/vim-tpipeline](https://github.com/defr0std/vim-tpipeline)@[2889cbdbe7...](https://github.com/defr0std/vim-tpipeline/commit/2889cbdbe756324e1e21716a34b3d36b058f959e)
#### Saturday 2023-11-11 12:54:53 by Magnus Groß

Add workaround for inconsistent statusline eval padding

It seems that neovim applies inconsistent padding when evaluating the
statusline:

- When padding a normal component, e.g. "%5l", then the global fillchars
  option is used
- When padding a grouped component with minwid, e.g. "%2(a%)", then the
  fillchars parameter for nvim_eval_statusline() is used

It is this inconsistent padding that causes our statusline split
heuristic to mistakenly think that a grouped component is the actual
split of the statusline (like "%="), while it is actually not.
This caused some statuslines (in particular heirline, luckily not many
other popular statuslines use grouped components like this) to have very
weird and early right alignment.
This is obviously not the fault of those statuslines, but it turns out
that this bug is not very easy to fix in upstream neovim.
Ideally we would have API in nvim_eval_statusline() that would tell us
the split point directly, then we could avoid these nasty heuristics
altogether.

So instead I came up with a workaround in the meantime. Keep in mind,
this workaround is absolutely horrid, but at least it works. Hopefully
we can resolve this problem properly, but for now I have added a unit
test to make sure that we don't regress this further.

Also fuck whoever masochist came up with 1-based indexes in Lua. It's
causing off-by-one errors literally everywhere, and unfortunately that's
not even the worst part about this horrible language.

Fixes #58

---
## [psychonaut-station/PsychonautStation](https://github.com/psychonaut-station/PsychonautStation)@[68cd638330...](https://github.com/psychonaut-station/PsychonautStation/commit/68cd6383306e3f37d36cdc82113ada320b6e6365)
#### Saturday 2023-11-11 16:19:25 by Donglesplonge

swaps one of the fridges in snowcabin to be in line with the rest  (#79414)

## About The Pull Request

In truth, this is an IDED PR (this is not at all sarcasm, and as we all
know nobody would lie on the internet) that came about from a round i
just got done playing wherein i was in snowcabin trying to cook up some
food for fun, well wouldn't you know it i couldn't open one of the
fridges, what gives? well i got to thinkin it has to do with the fridge
type used, for some reason the fridge that holds the universal enzyme
uses the freezer/fridge/kitchen type instead of the fridge/open type
that the other two do, so i went ahead and just changed it off to the
other fridge types so now anyone can open it.

## Why It's Good For The Game

its a bit stupid to have a single fridge thats different from the rest
for no discernable reason, i can't think of any reason universal enzyme
would need to be guarded ever, you could just say "well why not go back
onto the station and grab some if the fridge is locked", well if for
some reason i'm barred from the station i want to be able to use as many
tools within my reach as possible preferably without many hoops, and
this ones unnecessary.

## Changelog

fix: changes the type of fridge used to hold the universal enzyme in the
snowcabin gateway's kitchen, letting everyone access it like the rest of
the fridges.

/:cl:

---
## [ralfth/git](https://github.com/ralfth/git)@[8f23432b38...](https://github.com/ralfth/git/commit/8f23432b38d9b122be8179295a56688391dc8ad6)
#### Saturday 2023-11-11 16:20:00 by Johannes Schindelin

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
## [selliott512/freedoom](https://github.com/selliott512/freedoom)@[9ea70e75de...](https://github.com/selliott512/freedoom/commit/9ea70e75de134e0922ed4120e05721f73dd2b097)
#### Saturday 2023-11-11 16:52:15 by mc776

levels: various QOL fixes.

Generally there should be nothing *necessary to finish a level* that requires any of:
- straferunning;
- extremely sensitive timing that could softlock you if you're on keyboard, lagging in multiplayer or have motor issues;
- checking only for a sound cue that something has happened;
- remembering how to distinguish two visually nearly identical areas; or
- backtracking to a previous area on the map that you had previously been given no reason to revisit.

I haven't caught all of them by any stretch of the imagination but it's a start.

Also some regular minor fixes.

E1M9
- Fixed some textures around the big blue-trimmed lift and removed an extraneous use line that triggered a faraway lift for no reason.
- The red key bridge lowerable section is now textured differently from the rest of the bridge.

E3M5
- Teleporter platform to get back up to the catwalk from the northeastern blood maze is now clearly marked as having a switch, as it is a mandatory progression rather than a secret.

E4M8
- Got rid of some fake contrasts on the noodles at the start.
- Added a radsuit for the northwest switch. While it is possible to avoid damage even without straferun, unless you've got a tic counter display and can time it to the damage interval this is basically RNG.
- The water flat on top of the lowering wall in the east was very, very noticeable. The switch is now stepped on instead of hit. (Not too sure if the secret isn't *too* obscure now...)
- Removed asymmetrical doortrak on the slime bridge on the southeastern piston switch.
- The linedefs of said slime bridge pit are flipped so a deathmatch opponent trying to grab the berserk in there is not magically immune to rocket blasts. (see #996)
- Realigned the four pistons by the gate to the starship. They also reveal moving parts when activated - not nearly as good as the crushers on the original DI, but better than nothing.
- Made the southern walls use PLAT1 to make it more obvious that those walls will lower later (with the added bonus that they match the four pistons).
- The southern light bronze area now has a strip to guide the player towards the switch in case they lose track of their direction while fighting monsters and forget to explore inside that area, as well as to better distinguish it from the southeast.
- The gate threshold to the southern light bronze area now matches that of the pre-opened southeast.
- There is now actually a threshold where you can tell where the starport ends and the ship begins.
- The two light bronze areas are a bit too similar-looking. Added a few health boosts so the player can spot/be attacked by them and know this is an unexplored area.

Map11
- The lift going down into the yellow key room requires a switch that is out of sight from the lift itself, which is not clearly marked as a lift to begin with. The only real way to realize what's going on if you don't already know about the lift is to locate the sound and immediately turn to investigate before the lift comes back up. I thought this was annoying when I first did my big overhaul of this map, but ultimately left the basic mechanism alone out of an abundance of caution; however, with the recent discussion of accessibility in the proposed changes to the documentation I'm revisiting this. That upper switch now lowers a wall to reveal the lift which is triggered by a walk line.
- The lower far switch on that same lift was actually literally *impossible* to make on keyboard and no straferun (and no vanilla wallbounce exploit), even if I change it to a regular lift instead of fast. This is completely unacceptable for something necessary to progression (rather than an obscure secret). The lower switches are now permanent repeatable floor-lowerers, while the line crossing from the lift into the lower chamber is a permanent repeatable floor-raiser, with the line crossing into the lift from above being a simple lift line.
- Retextured the stairs out of the water in the eastern branch so it's not an unreadable mess of criss-crossing grey lines.
- Realigned the new skull switch texture in the skull room.

Map19
- One of the stealth worms was stuck in a burning barrel.
- Removed monster block flag on line 2083.
- Unmerged and remerged a few identical sectors to better match the intended sound travel.
- Flagged line 281 as a monster blocker. This allows the player to always be able to make the jump onto that bottom stair without being blocked by the octaminator.
- That octaminator is now a pain bringer in easy mode. The far end of that platform path is well outside the maximum vertical autoaim range in vanilla, which means that to actually hit the octaminator without up/down aiming you'd have to be on one of the later platforms - i.e., confined to a relatively narrow area with no cover *against an opponent that has seeker missiles*. The best way to solve this is to charge towards the octaminator as fast and as soon as possible with the SSG, minigun, or ripsaw+prayer to RNGsus that you'll get a good painlock. This is not the kind of tactic the sort of person who *needs* to play on easy will think to do, or could do while also being ready to sidestep if the octaminator fires at the wrong time.
- 347 and 249 are now also monster blockers, and the worms in that slime pit have been moved to the platform just behind the combat slug since they're awakened early on and that's where you'll first encounter them anyway.
- Replaced the teleport pad in the vertical platforming sequence with a lift, to minimize disorientation and going the wrong way. (In retrospect I probably could have just made the teleport destination face the pit you came in from, but the lift worked aesthetically better anyway.)
- A good chunk of that entire platforming area has been moved 8 units to the west so that things would align with the flat grid.
- Lines 307 and 309 are now also monster blockers. The worm that would be trapped between them is now moved further down the route and marked ambush.

Map20
- Removed the useless, misleading skull switch texture on the bars at the start.
- The door leading into the blue key arena needs no blue key; the door leading out needs a blue key. Both are marked with blue-light trim. Removed the blue lights on the first one.
- The lowering wall leading to the teleporter now uses a pipe texture.
- The door leading out of the giant quadruped arena now has a bright flickering light.
- Yellow key is another case of effectively-randomly-mandatory damage. Added a path.
- Same with the lava tunnel on the red key route.

Map25
- The silver lift near the river and shack is now activated by SW1GSTON switch right on the wall at eye level, rather than counterintuitively and invisibly recessed into additional sectors.
- The painlord ambush lift is now accessible after the encounter. A small health refill has been added there for easy and medium.

---
## [vlggms/lobotomy-corp13](https://github.com/vlggms/lobotomy-corp13)@[e23ea7b596...](https://github.com/vlggms/lobotomy-corp13/commit/e23ea7b5965a446e5b34f30baa0d4e4dc2d5b868)
#### Saturday 2023-11-11 17:31:41 by Táculo

Updates La Luna, Pinnochio for Rcorp and playables, gives minions NV on Rcorp AND moves CheckCombat to simple_animal. (#1621)

* Adds Everything

adds nv combat checks to
nosferatu bats
ml slimes
censored minis
tbird spawns
la luna spawned mob

adds mind transfer to pinocchio and la luna
add check for combat to initialize ai controllers for pinocchio, gives him a seclite on rcorp
add check for combat to spawn the breached la luna mob on its position instead of in a random department and to disable the timer.

makes pino ai disabled while a client is possesing it.

* removes one line

* Changes CheckCombat location, applies it to all minions.

* Makes button refuse pino.

fuck you pinocchio

* moves blocking code to pinocchio's

* moves the nightvision checks to simple_animal

moves the nightvision checks to simple_animal

removes the checks from censored, luna, tbird, ml, nosferatu

---
## [Mirag1993/mrdg](https://github.com/Mirag1993/mrdg)@[70463ae71b...](https://github.com/Mirag1993/mrdg/commit/70463ae71b7d639eecea572d3251562c5ffef68b)
#### Saturday 2023-11-11 17:54:22 by Mirag1993

Reworks The Visuals Of Independent And Nanotrasen Captains (#2453)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

Does what it says in the title. This is a demented PR that touches a lot
of things, but its main benefit is that now regular independent
captains, cowboy independent captains, and nanotrasen captains have a
unique identity.

Of those changed, it includes:

- The Nanotrasen Captain (parade)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/48a31cb1-b266-43cb-9b6e-525028893011)

- The Nanotrasen Captain (regular)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/799c88f0-b7ce-4736-956d-2e9c0a096433)

- The Independent Captain (regular/parade)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/17ecb3d3-5f2f-4ce0-a518-81366945ebdf)

- The Independent Captain (western)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/a56a798c-5adf-41d7-917a-730661f306ed)

The PR also axes a bunch of unused, or frankly quite basic lieutenant
outfits that were nothing more than set dressing with not much substance
behind them. The roles were not removed for now, and they have
appropriate outfits as a placeholder pending a full removal.

This also means that the Head of Personnel was slightly touched up,
mostly by having a coat and hat similar to the western captain's when
appropriate. The role itself is pending a full visual rework for later
that is beyond the scope of this PR.

Speaking of removals, this also means that captain outfits/roles that
were there as a legacy of removed ships, were finally axed for good.
Goodbye deserter captain for Riggs variant number 4, you will not be
missed.

This PR also touches several (a lot) of maps, mostly adding/removing
outfits that were either missing, or didn't fit with the dress code of
the vessel.

Also the PR fixes an oversight by @MarkSuckerberg by making the BYOND
version warning an actual warning, instead of an error when compiling.
Etto bleh.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

Visual cohesion is important, and dear fucking god if I see one more
independent western captain not wearing the duster because it wasn't in
the ship, I will weep, and my weeping will cause a biblical deluge.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

:cl: PositiveEntropy
imageadd: Outfits for independent and Nanotrasen captains have been
violently reworked.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [commonuserlol/android_kernel_xiaomi_mt6768](https://github.com/commonuserlol/android_kernel_xiaomi_mt6768)@[5cd65a10d2...](https://github.com/commonuserlol/android_kernel_xiaomi_mt6768/commit/5cd65a10d2b7e472dba75f0aa9cb6c07a6061674)
#### Saturday 2023-11-11 18:12:06 by Peter Zijlstra

sched/core: Fix ttwu() race

Paul reported rcutorture occasionally hitting a NULL deref:

  sched_ttwu_pending()
    ttwu_do_wakeup()
      check_preempt_curr() := check_preempt_wakeup()
        find_matching_se()
          is_same_group()
            if (se->cfs_rq == pse->cfs_rq) <-- *BOOM*

Debugging showed that this only appears to happen when we take the new
code-path from commit:

  2ebb17717550 ("sched/core: Offload wakee task activation if it the wakee is descheduling")

and only when @cpu == smp_processor_id(). Something which should not
be possible, because p->on_cpu can only be true for remote tasks.
Similarly, without the new code-path from commit:

  c6e7bd7afaeb ("sched/core: Optimize ttwu() spinning on p->on_cpu")

this would've unconditionally hit:

  smp_cond_load_acquire(&p->on_cpu, !VAL);

and if: 'cpu == smp_processor_id() && p->on_cpu' is possible, this
would result in an instant live-lock (with IRQs disabled), something
that hasn't been reported.

The NULL deref can be explained however if the task_cpu(p) load at the
beginning of try_to_wake_up() returns an old value, and this old value
happens to be smp_processor_id(). Further assume that the p->on_cpu
load accurately returns 1, it really is still running, just not here.

Then, when we enqueue the task locally, we can crash in exactly the
observed manner because p->se.cfs_rq != rq->cfs_rq, because p's cfs_rq
is from the wrong CPU, therefore we'll iterate into the non-existant
parents and NULL deref.

The closest semi-plausible scenario I've managed to contrive is
somewhat elaborate (then again, actual reproduction takes many CPU
hours of rcutorture, so it can't be anything obvious):

					X->cpu = 1
					rq(1)->curr = X

	CPU0				CPU1				CPU2

					// switch away from X
					LOCK rq(1)->lock
					smp_mb__after_spinlock
					dequeue_task(X)
					  X->on_rq = 9
					switch_to(Z)
					  X->on_cpu = 0
					UNLOCK rq(1)->lock

									// migrate X to cpu 0
									LOCK rq(1)->lock
									dequeue_task(X)
									set_task_cpu(X, 0)
									  X->cpu = 0
									UNLOCK rq(1)->lock

									LOCK rq(0)->lock
									enqueue_task(X)
									  X->on_rq = 1
									UNLOCK rq(0)->lock

	// switch to X
	LOCK rq(0)->lock
	smp_mb__after_spinlock
	switch_to(X)
	  X->on_cpu = 1
	UNLOCK rq(0)->lock

	// X goes sleep
	X->state = TASK_UNINTERRUPTIBLE
	smp_mb();			// wake X
					ttwu()
					  LOCK X->pi_lock
					  smp_mb__after_spinlock

					  if (p->state)

					  cpu = X->cpu; // =? 1

					  smp_rmb()

	// X calls schedule()
	LOCK rq(0)->lock
	smp_mb__after_spinlock
	dequeue_task(X)
	  X->on_rq = 0

					  if (p->on_rq)

					  smp_rmb();

					  if (p->on_cpu && ttwu_queue_wakelist(..)) [*]

					  smp_cond_load_acquire(&p->on_cpu, !VAL)

					  cpu = select_task_rq(X, X->wake_cpu, ...)
					  if (X->cpu != cpu)
	switch_to(Y)
	  X->on_cpu = 0
	UNLOCK rq(0)->lock

However I'm having trouble convincing myself that's actually possible
on x86_64 -- after all, every LOCK implies an smp_mb() there, so if ttwu
observes ->state != RUNNING, it must also observe ->cpu != 1.

(Most of the previous ttwu() races were found on very large PowerPC)

Nevertheless, this fully explains the observed failure case.

Fix it by ordering the task_cpu(p) load after the p->on_cpu load,
which is easy since nothing actually uses @cpu before this.

Fixes: c6e7bd7afaeb ("sched/core: Optimize ttwu() spinning on p->on_cpu")
Reported-by: Paul E. McKenney <paulmck@kernel.org>
Tested-by: Paul E. McKenney <paulmck@kernel.org>
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Signed-off-by: Ingo Molnar <mingo@kernel.org>
Link: https://lkml.kernel.org/r/20200622125649.GC576871@hirez.programming.kicks-ass.net
Change-Id: Ieb841b8f567bb5da0dcce8ff7ed3473fd096db31
Signed-off-by: SamarV-121 <samarvispute121@gmail.com>

---
## [MrMelbert/tgstation](https://github.com/MrMelbert/tgstation)@[1a62886a8b...](https://github.com/MrMelbert/tgstation/commit/1a62886a8b83afe5b827947051b9d85ac2ed1a8a)
#### Saturday 2023-11-11 19:01:23 by san7890

Fixes Shaving Beards + Mirror Code Improvement (#79529)

## About The Pull Request

Fixes #79519

Basically we did a lot of assumptions that we really shouldn't do in the
whole magical mirror framework (like having a boolean value for magical
mirrors, what?). Anyways, I just made the UX experience a lot better
when it came to bearded persons with feminine physiques to easily shave
off their beard with an additional confirmatory prompt + details as well
as keeping the nature of the magical mirror (giving you a swagadocious
beard due to magic:tm:) intact.
## Why It's Good For The Game

There was a lot of convoluted code that skipped through the quality
filter checks (it was me i think) so let's both make the code far easier
to grasp as well as ensure that people who legitimately acquire beards
and wish to keep them, keep them.

We were also doing some FUCK shit on attack_hand and the like
(overriding a FALSE return signal to return TRUE is not what we should
be doing there)- so that's also cleaned up.
## Changelog
:cl:
fix: Both magic mirrors and regular mirrors are far better at respecting
the choice of the beard you wish to wear (within reason, of course).
/:cl:

---
## [introShack/Project-3--Warehouse-Sim](https://github.com/introShack/Project-3--Warehouse-Sim)@[762b9af186...](https://github.com/introShack/Project-3--Warehouse-Sim/commit/762b9af18620d4a1c78c6ec0d7f6fde5ad9c8056)
#### Saturday 2023-11-11 19:06:09 by Aurora Liles

stupid fucking bracket deleted itself. little shit

---
## [clayne/cppfront](https://github.com/clayne/cppfront)@[cdf71bdca6...](https://github.com/clayne/cppfront/commit/cdf71bdca64536a005f2491d8c19f1d05a1c62f6)
#### Saturday 2023-11-11 19:28:33 by Herb Sutter

Correct copy/move for `union`

By writing separate construction and assignment, plus the new feature of suppressing assignment to a member by writing `member = _ ;` (now allowed only in assignment operators).

I do realize that's an "opt-out" which I normally prefer to avoid, but:

- I considered and decided against (for now) the alternative of not having assignment be memberwise by default. I want to keep the (new to Cpp2) default of memberwise semantics for assignment as with construction. I think that's a useful feature, and normally if you do assign to a member it doesn't arise, and so I think it makes sense to explicitly call out when we're choosing not to do any assignment at all to a member before doing other assignment processing. We'll get experience with how it goes.

- `_` is arguably natural here, since it's pronounced "don't care." There too, we'll see if that is natural generalized, or feels strained. For now it feels natural to me.

---
## [ihatethisengine/cmss13](https://github.com/ihatethisengine/cmss13)@[830e002a27...](https://github.com/ihatethisengine/cmss13/commit/830e002a27b7b4115815e450b8506832cb403a02)
#### Saturday 2023-11-11 19:41:01 by QuickLode

Adds a Colony Synthetic variant, with bug fixes (#4760)

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

1. should fix fax machine problem(thx forest)
2.  gives trucker synth the frontier jumpsuit(Thwomplert)
3. adds Freelancer Synthetic. This Synth is one that was bought off a
civi market and reprogrammed, or stolen and reprogrammed, or hacked, You
get the point - its going with a band of freelancers. The idea behind it
is that this synth's team is dead and they are just programmed as a merc
for pay - hoping to someday find their boss boss and give the money as
set up. I always thought about this one for a long time and decided to
put him in the civilian category, where its hard to roll and also gives
you freedom to choose your allegiance. In this case I hope that a
freelancer synthetic will open up unique avenue of RP and allegiance.
I've only explored it once ingame, but it was very good for RP!
Hopefully people can recreate this success.

was hard to make this guy look cool and I also wasn't sure on what his
loadout would be. I ended up giving him random generic stuff while
looking like a beat up freelancer(missing the armor especially hurt his
look, since thats the largest piece of a freelancer - the curiass, but I
don't want to give armor for balance reasons) and no beret because its
for a SL only.

as usual, if a synth wants to change RP avenues and don different
clothes for different RP, no one would know the difference
# Explain why it's good for the game
1. bug bad
2. a beat up UA laborer that so happens to be synthetic. you wouldn't
expect it because there's so many similar looking people! exactly the
job of a synth - to blend in.
3. Freelancer colony synth hopefully will open up a unique avenue of RP.
If they don't want to they can always ditch it - but its on a relatively
rare and uncommon roll anyways.
# Testing Photographs and Procedure
<details>
<summary>[Screenshots &
Videos](https://cdn.discordapp.com/attachments/490668342357786645/1166307813719556187/image.png?ex=654a03cb&is=65378ecb&hm=7108218bbaab61c78c0bedcecbfdcc07bdf9db87a3fefe9fb94b28d3430cc815&)</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:
add: adds another Colony Synthetic variant, changes up some existing
ones(trucker,CMB)
fix: fixes a small problem with WY-Colony Synthetic access(thx forest),
adds WY subtype of Synthetics for admin building/faxes
fix: fixes problems with organic spawning ferret industries Trucker
Synthetic
/:cl:

---
## [BlackCatMS/Luniks](https://github.com/BlackCatMS/Luniks)@[11c2d92da6...](https://github.com/BlackCatMS/Luniks/commit/11c2d92da6adb4d9557f555a6f27f5f7ff410cc6)
#### Saturday 2023-11-11 20:36:32 by Josie

GHOST TEMPLES // LAST LIGHT

guys guys guys guys guys guys guys guys guys guys guys guys guys guys holy shit this is so cool this is the most fun ive had with writing after leremkov im not even fucking kidding this is incredible

---
## [norrlandxyz/fegil](https://github.com/norrlandxyz/fegil)@[886c77762a...](https://github.com/norrlandxyz/fegil/commit/886c77762aa3aa36dfb8eb1f20b71228a1201e56)
#### Saturday 2023-11-11 21:26:40 by joakim

fuck you vikingfuck you vikingfuck you vikingfuck you vikingfuck you vikingfuck you vikingfuck you vikingfuck you vikingfuck you vikingfuck you vikingfuck you vikingfuck you vikingfuck you vikingfuck you vikingfuck you vikingfuck you vikingfuck you vikingfuck you vikingfuck you vikingfuck you vikingfuck you vikingfuck you vikingfuck you vikingfuck you vikingfuck you vikingfuck you vikingfuck you vikingfuck you vikingfuck you vikingfuck you vikingfuck you vikingfuck you vikingfuck you vikingfuck you vikingfuck you vikingfuck you vikingv

---
## [naibu3/pw](https://github.com/naibu3/pw)@[f92974476e...](https://github.com/naibu3/pw/commit/f92974476e44bccc167fb778ce0041d62a95dd59)
#### Saturday 2023-11-11 21:39:57 by Nacho

only 2 more and i'll be done with this fucking
bullshit of a project
someobody please send help i want to die

---
## [LukeyeDev/Begotten-III](https://github.com/LukeyeDev/Begotten-III)@[0ff5062837...](https://github.com/LukeyeDev/Begotten-III/commit/0ff50628372e44e9cf3c0dfbac54d454a3802aca)
#### Saturday 2023-11-11 21:41:38 by DETrooper

New Thralls & Rebalance, Other Changes

	- Added 3 new thralls: the Coinsucker, the Ironclad, and the Pursuer.
	- Added correct item model for the Master-at-Arms plate.
	- Fixed Holy Sigils parry lua error.
	- Fixed /notarget admin command.
	- Hellteleporting, helljaunting, and using the hell portal now all provide bear trap immunity immediately after the teleport.
	- Rebalanced NPCs to make fighting them far more skill-based/team-based:
		- Increased the attack range of the Brute and Eddie (bladed arm thralls).
		- Increased the XP value of the Chaser to 200.
		- Modified Brute attack timings to make it faster. Eddie remains the same since it has more HP, range, and damage.
		- NPCs now utilize their minimum attack range instead of attacking at the maximum distance their attacks can reach. This means you won't be able to just walk away from most thralls anymore.
		- Parrying thralls now stuns them.
		- Reduced max range of the Otis chainsawer thrall's attack from 140 to 125. Increased the suitor chainsawer thrall's from 60 to 125.
		- Reduced the Shambler's health from 150 to 100 and reduced its damage from 15 to 10, so it is now a much weaker version of the Chaser. Also gave it an XP reward value that it was missing.
		- Reduced the XP value of the Otis from 250 to 200.
		- Shamblers now spawn at night in lieu of Chasers, as they have less health and do less damage though they are still fairly dangerous due to the rapidity of their attacks and speed.
	- Removed the InvAction command so that it can't be used to use items without opening the inventory menu.

---
## [Time-Green/tgstation](https://github.com/Time-Green/tgstation)@[0be45dcd65...](https://github.com/Time-Green/tgstation/commit/0be45dcd6534244532e652564976bab13a3d8bdb)
#### Saturday 2023-11-11 22:07:16 by John Willard

Human sounds now depend on body type (#78632)

## About The Pull Request

So there's currently a problem where our human sounds are dependent on
whether you are a male or female, however we have 4 genders in-game.
This leads to scream sounds being female if you're anything but a Male,
and gasp shock sounds being male if you're anything but a Female. This
is very inconsistent, and I think as a better way of handling this, it
should all be handled by Bodytype, since we only have 2 and is a
separate choice from gender. This means regardless of gender, you can
still choose what sounds your character will make.

## Why It's Good For The Game

Mostly explained in the about section, this lets people who play as
they/them & it/its to decide what they should sound like.
I guess as a bonus, it means men now appear more like women if they
choose the female bodytype, and vice versa. Or at least I think it's a
bonus? I'm not really knowledgeable in this sort of stuff.

I kinda have the same argument as why I think TTS should be accurate.
You should be able to customize your character to how you want it, and I
think that choosing the non-male/female ones shouldn't give you
inconsistent voices.

## Changelog

I actually don't know what to label this.

:cl:
code: Your bodytype now decides what gendered sounds you make.
/:cl:

---
## [vrglab/LowpEngine](https://github.com/vrglab/LowpEngine)@[1facbaf8d8...](https://github.com/vrglab/LowpEngine/commit/1facbaf8d8a3929f4326d4e1142011bdb68f030b)
#### Saturday 2023-11-11 23:43:52 by Vrglab

Just nearly fixed this stupid fucking shit head, it's driving  me fucking insane, why is a simple system linking in core but not inlauncher

---

