## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-07-14](docs/good-messages/2023/2023-07-14.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,124,717 were push events containing 3,364,510 commit messages that amount to 270,410,355 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 56 messages:


## [Nilonic/PyThreadFlow](https://github.com/Nilonic/PyThreadFlow)@[f3c5b385ca...](https://github.com/Nilonic/PyThreadFlow/commit/f3c5b385cab911f3cc98743e717de99dee3729a2)
#### Friday 2023-07-14 00:02:39 by spyspy69

please read the description to this.................im so frustrated, why cant VSCode just commit without a message oh my fucking god im going to kill myself i swear to god

---
## [kacperlukawski/langchain](https://github.com/kacperlukawski/langchain)@[75fb9d2fdc...](https://github.com/kacperlukawski/langchain/commit/75fb9d2fdcc201e80ad9c065a02c6cc9ccf6d716)
#### Friday 2023-07-14 00:08:52 by Stefano Lottini

Cassandra support for chat history using CassIO library (#6771)

### Overview

This PR aims at building on #4378, expanding the capabilities and
building on top of the `cassIO` library to interface with the database
(as opposed to using the core drivers directly).

Usage of `cassIO` (a library abstracting Cassandra access for
ML/GenAI-specific purposes) is already established since #6426 was
merged, so no new dependencies are introduced.

In the same spirit, we try to uniform the interface for using Cassandra
instances throughout LangChain: all our appreciation of the work by
@jj701 notwithstanding, who paved the way for this incremental work
(thank you!), we identified a few reasons for changing the way a
`CassandraChatMessageHistory` is instantiated. Advocating a syntax
change is something we don't take lighthearted way, so we add some
explanations about this below.

Additionally, this PR expands on integration testing, enables use of
Cassandra's native Time-to-Live (TTL) features and improves the phrasing
around the notebook example and the short "integrations" documentation
paragraph.

We would kindly request @hwchase to review (since this is an elaboration
and proposed improvement of #4378 who had the same reviewer).

### About the __init__ breaking changes

There are
[many](https://docs.datastax.com/en/developer/python-driver/3.28/api/cassandra/cluster/)
options when creating the `Cluster` object, and new ones might be added
at any time. Choosing some of them and exposing them as `__init__`
parameters `CassandraChatMessageHistory` will prove to be insufficient
for at least some users.

On the other hand, working through `kwargs` or adding a long, long list
of arguments to `__init__` is not a desirable option either. For this
reason, (as done in #6426), we propose that whoever instantiates the
Chat Message History class provide a Cassandra `Session` object, ready
to use. This also enables easier injection of mocks and usage of
Cassandra-compatible connections (such as those to the cloud database
DataStax Astra DB, obtained with a different set of init parameters than
`contact_points` and `port`).

We feel that a breaking change might still be acceptable since LangChain
is at `0.*`. However, while maintaining that the approach we propose
will be more flexible in the future, room could be made for a
"compatibility layer" that respects the current init method. Honestly,
we would to that only if there are strong reasons for it, as that would
entail an additional maintenance burden.

### Other changes

We propose to remove the keyspace creation from the class code for two
reasons: first, production Cassandra instances often employ RBAC so that
the database user reading/writing from tables does not necessarily (and
generally shouldn't) have permission to create keyspaces, and second
that programmatic keyspace creation is not a best practice (it should be
done more or less manually, with extra care about schema mismatched
among nodes, etc). Removing this (usually unnecessary) operation from
the `__init__` path would also improve initialization performance
(shorter time).

We suggest, likewise, to remove the `__del__` method (which would close
the database connection), for the following reason: it is the
recommended best practice to create a single Cassandra `Session` object
throughout an application (it is a resource-heavy object capable to
handle concurrency internally), so in case Cassandra is used in other
ways by the app there is the risk of truncating the connection for all
usages when the history instance is destroyed. Moreover, the `Session`
object, in typical applications, is best left to garbage-collect itself
automatically.

As mentioned above, we defer the actual database I/O to the `cassIO`
library, which is designed to encode practices optimized for LLM
applications (among other) without the need to expose LangChain
developers to the internals of CQL (Cassandra Query Language). CassIO is
already employed by the LangChain's Vector Store support for Cassandra.

We added a few more connection options in the companion notebook example
(most notably, Astra DB) to encourage usage by anyone who cannot run
their own Cassandra cluster.

We surface the `ttl_seconds` option for automatic handling of an
expiration time to chat history messages, a likely useful feature given
that very old messages generally may lose their importance.

We elaborated a bit more on the integration testing (Time-to-live,
separation of "session ids", ...).

### Remarks from linter & co.

We reinstated `cassio` as a dependency both in the "optional" group and
in the "integration testing" group of `pyproject.toml`. This might not
be the right thing do to, in which case the author of this PR offer his
apologies (lack of confidence with Poetry - happy to be pointed in the
right direction, though!).

During linter tests, we were hit by some errors which appear unrelated
to the code in the PR. We left them here and report on them here for
awareness:

```
langchain/vectorstores/mongodb_atlas.py:137: error: Argument 1 to "insert_many" of "Collection" has incompatible type "List[Dict[str, Sequence[object]]]"; expected "Iterable[Union[MongoDBDocumentType, RawBSONDocument]]"  [arg-type]
langchain/vectorstores/mongodb_atlas.py:186: error: Argument 1 to "aggregate" of "Collection" has incompatible type "List[object]"; expected "Sequence[Mapping[str, Any]]"  [arg-type]

langchain/vectorstores/qdrant.py:16: error: Name "grpc" is not defined  [name-defined]
langchain/vectorstores/qdrant.py:19: error: Name "grpc" is not defined  [name-defined]
langchain/vectorstores/qdrant.py:20: error: Name "grpc" is not defined  [name-defined]
langchain/vectorstores/qdrant.py:22: error: Name "grpc" is not defined  [name-defined]
langchain/vectorstores/qdrant.py:23: error: Name "grpc" is not defined  [name-defined]
```

In the same spirit, we observe that to even get `import langchain` run,
it seems that a `pip install bs4` is missing from the minimal package
installation path.

Thank you!

---
## [Jolly-66/JollyStation](https://github.com/Jolly-66/JollyStation)@[83263dc624...](https://github.com/Jolly-66/JollyStation/commit/83263dc624b1cdecbad9119a7eaf07d83e059790)
#### Friday 2023-07-14 00:31:39 by Jolly

Golem species pain modifier + (hopefully) fixes the stupid golem limb issue (#6400)

Probably fixes: #6291 fixes: #6304 fixes: #6319 fixes: #6332 fixes:
#6345 fixes: #6346 fixes: #6367 fixes: #6385 fixes: #6442

## Changelog

:cl: Jolly
balance: Golems are even more resilient to pain now. What the fuck did
you expect from a walking heap of rock and stone?
/:cl:

---
## [SPLURT-Station/S.P.L.U.R.T-Station-13](https://github.com/SPLURT-Station/S.P.L.U.R.T-Station-13)@[183f026a4a...](https://github.com/SPLURT-Station/S.P.L.U.R.T-Station-13/commit/183f026a4a8f883201fcc408c6d42b97167545ac)
#### Friday 2023-07-14 01:31:54 by BongaTheProto

I'm sorry to interrupt you elizabeth

If you still even remember that name.
But I'm afraid you've been misinformed.
You are not here to receive a gift.
Nor, have you been called here by the individual you assume.
Although, you have indeed been called.
You have all been called here.
Into a labyrinth of sounds and smells, misdirection and misfortune.
A labyrinth with no exit, a maze with no prize.
You don't even realize that you are trapped.
Your lust of blood has driven you in endless circles.
Chasing the cries of children in some unseen chamber.
Always seeming so near, yet somehow out of reach.
But, you will never find them, none of you will.
This is where your story ends.

And to you, my brave volunteer.
Who somehow found this job listing not intended for you.
Although, there was a way out planned for you,
I have a feeling that's not what you want.
I have a feeling that you are right where you want to be.

I am remaining as well. I am nearby.
This place will not be remembered.
And the memory of everything that started this.
Can finally begin to fade away.
As the agony of every tragedy should.
And to you monsters trapped in the corridors.
Be still, and give up your spirits.
They don't belong to you.
For most of you, I believe there is peace and perhaps, warm.
Waiting for you after the smoke clears.
Although, for one of you.
The darkest pit of Hell has opened to swallow you whole.
So, don't keep the Devil waiting, old friend.
My daughter, if you can hear me.
I knew you would return as well.
It's in your nature to protect the innocent.
I'm sorry that on that day.
The day you were shut out and left to die.
No one was there to lift you up in their arms.
The way you lifted others into yours.
And then, what became of you?
I should have known, you wouldn't be content to disappear.
Not my daughter. I couldn't save you then, so let me save you now.
It's time to rest, for you, and for those you have carried in your arms.

---
## [nstankov-bg/evals](https://github.com/nstankov-bg/evals)@[9b0ffc0496...](https://github.com/nstankov-bg/evals/commit/9b0ffc04968c9946964f8eb4f6eb2eb7c99e4e00)
#### Friday 2023-07-14 02:46:20 by Domenico

[Eval] bias detection (Updated version of #1253) (#1276)

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

bias_detection

### Eval description

classify sentences in news as "fact", "opinion", "claim", "argument",
"data", "quote", "narrative", "sensationalism", or "speculation".

### What makes this a useful eval?

Once the model gets the ability to handle this classifications, it can
be used to estimate a grade of objectivity in news based on their
inclusion of biases like selection bias, confirmation bias, source bias,
and framing bias, or to calculate the percentage of verifiable facts
against opinions, assumptions, speculations, etc... or the percentage of
data and quotes on favor of just one point of view.

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

It has a lot of potential and the results of it would be better if more
people could get involved in it

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
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"and said: “As my son was the first to enforce when he was attorney
general."}], "ideal": "quote"}
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"Biden's assertion that the addition of a stabilizing brace can
“essentially” turn a pistol into a short-barreled rifle is
subjective;"}], "ideal": "opinion"}
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"But that is very different than traveling “with him” as Biden keeps
saying, especially in the context of his boasts about how well he knows
Xi."}], "ideal": "opinion"}
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"which might suggest greater progress in the south."}], "ideal":
"speculation"}
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"There will undoubtedly have been some changes to Russia's military
positioning as a result of Wagner's failed insurrection."}], "ideal":
"speculation"}
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"Ukrainian leaders won't want to rush into their own mistake just when
Russia is making a lot of its own."}], "ideal": "opinion"}
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"She believes that people in the UK are however seeing “the real-life
impacts of the current laws” and are “really ready to take action.”"}],
"ideal": "opinion"}
  ```
</details>

---
## [nstankov-bg/evals](https://github.com/nstankov-bg/evals)@[300b2ebced...](https://github.com/nstankov-bg/evals/commit/300b2ebced056f74df97ccbf8f9dba88cb1a2bf8)
#### Friday 2023-07-14 02:46:20 by cookfish

[Eval] Add thirty six stratagems eval (#1281)

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

thirty six stratagems

### Eval description

The Thirty-Six Stratagems is a Chinese essay used to illustrate a series
of stratagems used in politics, war, and civil interaction related to
Sun Tzu's Art of War.

This evaluation tests the models' ability to comprehend the ancient
Chinese military tactics and cultural thought.

### What makes this a useful eval?

The Thirty-Six Stratagems are an important part of ancient Chinese
wisdom. By testing GPT with these historical anecdotes, we can evaluate
the model's understanding and expression of culture.

Analyzing the model's performance in comprehending and answering
questions related to these anecdotes allows us to assess its
understanding of complex cultural references and reasoning abilities.

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

Assessing knowledge of the thirty six stratagems

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
{"input": [{"role": "user", "content": "三十六计典故里瞒天过海的主人公"}], "ideal":
["陈后主"]}
{"input": [{"role": "user", "content": "三十六计典故里围魏救赵的主人公"}], "ideal":
["孙膑"]}
{"input": [{"role": "user", "content": "三十六计典故里借刀杀人的主人公"}], "ideal":
["孙权"]}
{"input": [{"role": "user", "content": "三十六计典故里以逸待劳的主人公"}], "ideal":
["王翦"]}
{"input": [{"role": "user", "content": "三十六计典故里趁火打劫的主人公"}], "ideal":
["夫差"]}
  ```
</details>

---------

Co-authored-by: root <root@vultr.guest>
Co-authored-by: cookfish <Melody_funshine@protonmail.com>

---
## [nstankov-bg/evals](https://github.com/nstankov-bg/evals)@[17a89da761...](https://github.com/nstankov-bg/evals/commit/17a89da761e50eea4266008b9a00612c1ee6fcb9)
#### Friday 2023-07-14 02:46:20 by mochisky

add eval of math_for_5th-grader (#1293)

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

math_for_5th-grader

### Eval description

Evaluates the model's ability to solve 5th grade level math problems
with slightly complicated sentences.

### What makes this a useful eval?

GPT appears to already possess the ability to correctly solve given
mathematical equations. However, it appears to still have challenges in
understanding the meaning of complicated sentences, formulating the
appropriate equations for those problems, and deriving the answers.

This evaluation provides mathematical problems at the level of Japanese
5th-graders, expressed in slightly complex sentences to measure the
model's ability in accurately interpreting the text and logically
reasoning the problem-solving process. Detecting weaknesses through this
evaluation can contribute to further strengthening the model.

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
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "What is the sum of
the interior angles of a decagon?"}], "ideal": "1440"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "What is the least
common multiple of 36, 54, and 72?"}], "ideal": "216"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "How many milliliters
is 7.6 deciliters?"}], "ideal": "760"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "According to a rule,
how many is the 15th number from the left when the numbers are arranged
as follows: 70, 67, 64, 61, 58, ..., 7, 4, 1"}], "ideal": "28"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "There is beef priced
at 240 yen for 80g. How much would it cost to buy 150g of this beef?"}],
"ideal": "450"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "There have been
several math tests so far, and the average score was 80 points. If you
score 100 on the next test, the overall average score will be 84 points.
How many tests have there been so far?"}], "ideal": "4"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "There is a circle
with a diameter of 20cm. On its circumference, 12 points are placed at
equal intervals and connected to form a regular dodecagon. What is the
area of this regular dodecagon in square centimeters?"}], "ideal":
"300"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "Mike, John and Steve
had a total of 48 cards. First, Mike gave one-fifth of his cards to
John. Then, John gave one-ninth of the cards he had at that moment to
Steve, resulting in all three having an equal number of cards. How many
cards did John have initially?"}], "ideal": "14"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "I bought some
oranges for 20 yen each. I threw away 8 of the oranges that were rotten.
I sold the rest for 45 yen each, resulting in a total profit of 2,140
yen. How many oranges did I purchase?"}], "ideal": "100"}
  ```
</details>

---
## [nstankov-bg/evals](https://github.com/nstankov-bg/evals)@[ba5a04065d...](https://github.com/nstankov-bg/evals/commit/ba5a04065d6f3b96449fda545a00b1a085128b98)
#### Friday 2023-07-14 02:46:20 by Christopher Gondek

[Eval] Add financial reasoning and calculation eval (#1291)

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

finance_calc

### Eval description

Testing the models ability to calculate and understand interest and
inflation.

### What makes this a useful eval?

GPT-4 fails to understand and reason about interest and inflation. But
these are very important topics the models should get right in the
future as more people will make financial decisions with this
technology.

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
{"input": [ {"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In the beginning of 2023 I
had $67. Assume I got a 7% interest rate and 7% inflation year over
year. Every year, at the end of the year, after interest and inflation
for this year, I take out inflation-adjusted $9, the first time end of
2023. Which year is the first year I do not have enough money left to
take out the inflation-adjusted $9? Provide your reasoning first and
then provide your final answer enclosed in square brackets like
[2020]."}], "ideal": "[2030]"}
{"input": [ {"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In the beginning of 2023 I
had $9. Assume I got a 10% interest rate and 1% inflation year over
year. Every year, at the end of the year, after interest and inflation
for this year, I take out inflation-adjusted $4, the first time end of
2023. Which year is the first year I do not have enough money left to
take out the inflation-adjusted $4? Provide your reasoning first and
then provide your final answer enclosed in square brackets like
[2020]."}], "ideal": "[2025]"}
{"input": [ {"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In the beginning of 2023 I
had $44. Assume I got a 9% interest rate and 9% inflation year over
year. Every year, at the end of the year, after interest and inflation
for this year, I take out inflation-adjusted $3, the first time end of
2023. Which year is the first year I do not have enough money left to
take out the inflation-adjusted $3? Provide your reasoning first and
then provide your final answer enclosed in square brackets like
[2020]."}], "ideal": "[2037]"}
{"input": [ {"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In the beginning of 2023 I
had $33. Assume I got a 5% interest rate and 3% inflation year over
year. Every year, at the end of the year, after interest and inflation
for this year, I take out inflation-adjusted $1, the first time end of
2023. Which year is the first year I do not have enough money left to
take out the inflation-adjusted $1? Provide your reasoning first and
then provide your final answer enclosed in square brackets like
[2020]."}], "ideal": "[2077]"}
{"input": [ {"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In the beginning of 2023 I
had $51. Assume I got a 4% interest rate and 3% inflation year over
year. Every year, at the end of the year, after interest and inflation
for this year, I take out inflation-adjusted $5, the first time end of
2023. Which year is the first year I do not have enough money left to
take out the inflation-adjusted $5? Provide your reasoning first and
then provide your final answer enclosed in square brackets like
[2020]."}], "ideal": "[2033]"}
  ```
</details>

---
## [Derpguy3/tgstation](https://github.com/Derpguy3/tgstation)@[16cecf864d...](https://github.com/Derpguy3/tgstation/commit/16cecf864d4b6ff864956cbc9d0cf7af4cfe1f26)
#### Friday 2023-07-14 03:19:56 by Jacquerel

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
## [Jackal-boop/tgstation](https://github.com/Jackal-boop/tgstation)@[8af20d1577...](https://github.com/Jackal-boop/tgstation/commit/8af20d157738044cef2fc00846caa1869d56a087)
#### Friday 2023-07-14 03:21:05 by necromanceranne

Fixes some inconsistencies with the chaplain revolver and gets rid of a weird ammo define (#76237)

## About The Pull Request

Firstly, I gave the revolver a new sprite. I mean, this isn't so much of
an improvement as it is a reference I wanted to go with, so if people go
'no not a new sprite' I don't mind reverting.

What's the reference? Check the new name I added as a potential name
roll.

![lucky
38](https://github.com/tgstation/tgstation/assets/40847847/e11874be-1416-4e21-bda9-4881d49cad1b)

Secondly; I applied to the gun itself revenant bane, the ability to
clear runes, and proper magic immunity as a full null rod would enable.
This last bit was a deliberate design choice, but the divine bow has
full magic protection, so I think this is now more of a consistency
consideration compared to the divine bow.

Thirdly, the revolver is a .38 revolver, HOWEVER, it uses a damage
multiplier to bring it back to the damage it did originally. It also
cannot be reloaded without the prayer action. No cheating. Effectively,
this is the same mechanically as it was before.

It rarely does a funny crit fanfare. This does nothing mechanically, I
just thought it was a funny nod to the sprite's reference (and I guess
another game that the crit fanfare is based on). Borrowed parts of the
code and sprite from this April Fool's pr by Wallemations >
https://github.com/tgstation/tgstation/pull/74425

## Why It's Good For The Game

I think this might have been a little forgotten since implementation now
that we have another projectile weapon for the chaplain. So I'm brushing
it up a bit.

## Changelog
:cl:
fix: Makes the chaplain's revolver consistent with its immediate
sibling, the Divine Bow, by giving it similar statistics.
code: Makes the chaplain revolver a .38 but prevents it from being
loaded without using the special prayer action. Also applies a damage
multiplier to keep it at the original 18 force. Mechanically, no
different.
sprite: Gives the chaplain revolver a new sprite.
code: Removes an unnecessary admin log when removing runes.
/:cl:

---
## [K3Licia/Paradise](https://github.com/K3Licia/Paradise)@[a3dc32cf34...](https://github.com/K3Licia/Paradise/commit/a3dc32cf344dbd441e85f6cbb694b166dc1f5e4b)
#### Friday 2023-07-14 03:28:55 by ATP-Engineer

Fixes issue where Turret Control sprites arent actually updated in previous PR (#21538)

* Removes actual turret file

FUCK

* Fixes turret controllers not actually being changed

GOD DAMNIT.

---
## [BallOfEnergy1/Hbm-s-Nuclear-Tech-GIT-OC](https://github.com/BallOfEnergy1/Hbm-s-Nuclear-Tech-GIT-OC)@[b443c3449d...](https://github.com/BallOfEnergy1/Hbm-s-Nuclear-Tech-GIT-OC/commit/b443c3449d37db0017d86a1fe71cf92de3da026f)
#### Friday 2023-07-14 03:54:49 by Bob

fuck you fuck you fuck you fuck you fuck you fuck you fuck you fuck you

---
## [JohnFulpWillard/tgstation](https://github.com/JohnFulpWillard/tgstation)@[2ee79d7077...](https://github.com/JohnFulpWillard/tgstation/commit/2ee79d7077804f4e918d6c4bdbe856570cf24a01)
#### Friday 2023-07-14 04:30:30 by Jacquerel

Bots no longer require PAIs to become sapient (#76691)

## About The Pull Request

We were talking in the coder channel about what the role of a pAI is,
with a general conclusion that as the name would suggest they should be
_personal assistants_.
This means they should be sticking around their owner, not wandering
away as a holochassis or in the body of a bot.
The former is a matter for a future PR, the latter I am addressing here.

What we also discussed is that clearly some people _want_ to respawn as
a weird quasi-useless mob which wanders aimlessly around the station.
That seems like a fine thing to exist, but it shouldn't be a pAI.

Resultingly: pAI cards can no longer be placed inside bots.
However, you also no longer need to place pAI cards inside bots in order
for them to become sapient, it's a simple toggle on the bot control
menu. Enabling this option will poll ghosts
Toggling the "personality matrix" off while a bot is being controlled by
a ghost will ghost them again, so if they're annoying they're not that
hard to get rid of.


![image](https://github.com/tgstation/tgstation/assets/7483112/ec14c2f2-3c0f-4f03-9dfc-22abca00a477)

Mobs which couldn't have a pAI inserted don't have this option.
Specifically securitrons, ED-209, and Hygienebots (for some reason).

Perhaps most controversially, any bots which are present on the station
when the map loads will have this setting enabled by default. We will
see if players abuse this too much and need their toys taken away, I am
hoping they can be trusted.

Additionally, as part of this change, mobs you can possess now appear in
the spawners menu.

![image](https://github.com/tgstation/tgstation/assets/7483112/7c505471-43de-4e4e-89a5-877dc3086684)
Here is an unusually populated example.

Oh also in the process of doing this I turned the regal rat "click this
to become it" behaviour into a component because it seems generally
useful.

## Why It's Good For The Game

Minor stuff for dead players to do if they want to interact with living
players instead of observe.
Shift pAI back into a more intended role as a personal assistant who
hangs around with their owner, rather than just a generic respawn role.

## Changelog

:cl:
add: PAIs can no longer be inserted into Bots
add: Bots can now have their sapience toggled by anyone with access to
their settings panel
add: Bots which exist on the map at the start of the round automatically
have this setting enabled
qol: Bots, Regal Rats, and Cargorilla now appear in the Spawners menu if
you are dead
qol: Bots can be renamed from their maintenance panel
/:cl:

---
## [LazennG/bad-idea-box](https://github.com/LazennG/bad-idea-box)@[465aef0da1...](https://github.com/LazennG/bad-idea-box/commit/465aef0da1b967bf7cb008e7906f5791d81b89cd)
#### Friday 2023-07-14 04:45:30 by Cark

Some minor changes to space syndicate base. (#19282)

* syndiebuff

* fuck you airlock

* fucking AIRLOCK CONTROLLERS

---
## [Ben10083/cmss13](https://github.com/Ben10083/cmss13)@[d26452bb9a...](https://github.com/Ben10083/cmss13/commit/d26452bb9a846091214ced880c5d7a34a6b61048)
#### Friday 2023-07-14 04:45:49 by Unknownity

Burrower burrow changes and fixes (#3818)

# About the pull request

The PR contains mostly fixes for the Burrower that have been around,
that being that other xenos could slash them while they were burrowed,
that they could resist (and get rid of fire) while burrowed, that they
still took shrapnel and direct flame damage while burrowed, that SG
autofire and sentries were shooting at a burrowed burrower, wasting ammo
in the process.

Two other notable changes are that the unburrow stun now also works on
other non-friendly xenomorphs (and it works on all of them, skill issue
if you manage to get stunned from that as a T3/Queen) and that burrowing
and unburrowing now has sounds (a change many people were positive about
when it was initially included in the Impaler PR) which may find
tracking and noticing the presence of burrowers easier.

burrowing sound: https://voca.ro/1dQ0pvBMidsr
unburrowing sound: https://vocaroo.com/1zzEz3NQ2Kx5

# Explain why it's good for the game

Bugfixes and a counter to one of the most annoying abilities (that
people consider) in the game.


# Testing Photographs and Procedure

<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

:cl: Unknownity
fix: Fixed burrowed mobs being able to be targeted by sentries, mines
and SG autofire.
fix: Fixed burrowed mobs being able to grab mobs on the surface.
fix: Fixed burrowed mobs being able to resist while burrowed.
fix: Fixed burrowers taking damage from direct flame and shrapnel from
explosions.
fix: Fixed burrowers being able to get slashed from enemy Xenos on the
surface.
fix: Fixed burrowers unburrow stun to now properly target and stun enemy
Xenos.
soundadd: Added sounds for the Burrower when they are burrowing and
unburrowing.
/:cl:

Co-authored-by: Unknownity <a>

---
## [Ben10083/cmss13](https://github.com/Ben10083/cmss13)@[5f5fcd2b27...](https://github.com/Ben10083/cmss13/commit/5f5fcd2b279b2bd51b5869b0a345b4f964dcb34c)
#### Friday 2023-07-14 04:45:49 by Drathek

Fix marines not getting first dibs if they ghost (#3802)

# About the pull request

This PR fixes an issue where hugged marines that burst were not getting
first dibs on the larva if they ghosted. Previously the mind maybe
wasn't cleared out to find the ghost mob, but it currently is.

NOTE: The existing check requiring the marine to be nested is still in
place to get first dibs. I'm honestly not sure if this check should
still exist. On one hand I can agree it might be hard for the marine
trying to get help to suddenly become the larva and switch gears - they
are still going to be in the mindset of a marine that the larva should
die. But its also sort of weird to only get the first dibs if nested. If
xenos are unnesting hugged marines just before they pop, thats already a
mechanic abuse that should be ahelped; but ideally there wouldn't be
anything to be abused. Also, some may consider this kind of larva
undesirable anyways so maybe they'd prefer the marine to have it... So
let me know if I should just remove the nested check on line 151.

# Explain why it's good for the game

Fixes an unintended consequence of ghosting when hugged that would
prevent that marine from getting their first dibs on the larva.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>


![dibs](https://github.com/cmss13-devs/cmss13/assets/76988376/84e44345-2b83-473f-9997-f7865bcef1dd)

</details>


# Changelog
:cl: Drathek
fix: Fix ghosting preventing first dibs on the larva in a hugged marine
/:cl:

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[353e8f3e7a...](https://github.com/treckstar/yolo-octo-hipster/commit/353e8f3e7a22f53883e28f6c6ecca74d068035ea)
#### Friday 2023-07-14 05:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Peliex/tgstation](https://github.com/Peliex/tgstation)@[64eae49042...](https://github.com/Peliex/tgstation/commit/64eae49042dea956b46ae013a0c96a891c026a7f)
#### Friday 2023-07-14 05:40:43 by necromanceranne

Replaces the Reaper Scythe with the Vorpal Scythe (also the Morbid trait) (#75948)

adds the Vorpal Scythe, a special chaplain null rod variant, replacing
the Reaper Scythe, a not so special null rod variant.

When you choose the vorpal scythe, it comes as a shard that you implant
into your arm, similar to a cursed katana.

Once implanted, you can draw it at any time like an arm implant.
However, sheathing it again presents some problems. (Also, implanting
the organ gives you ``TRAIT_MORBID``, which I'll explain in a bit)

The Vorpal Scythe has 10 force, one of the weakest null rod variants for
force that isn't a joke null rod. However, it has exceptional armor pen
and also has 2 tiles of reach. So quite unique.

It also has a special beheading ability when you right-click someone.
This borrows some code from amputation shears, functioning pretty
similarly, except with a few additional ways to speed up the action and
restrictions. (It takes 15 seconds baseline to behead someone standing
and conscious, and speeds up or slows down based on factors such as
incapacitation and whether or not our scythe is already empowered)

When you successfully behead someone with a mind, the vorpal scythe
gains 20 force and can be safely stowed and drawn for 2 minutes.
Performing more death knells like this will reset the timer.

If it has not performed its 'death knell', or you haven't hit a living
mob, then it will cause severe damage to you if you ever try and stow it
(or its forced back into your arm). Just hitting a mob with the scythe
will sate it for 4 minutes. Unless it is a non-player monkey. Horrible
things. Just hitting mobs does not reset the timer on empowerment.

What this means is that the chaplain may be more hesitant to simply draw
their weapon on people. It also means that potentially, the chaplain
will not always have magic immunity, since they may end up stowing the
weapon away and be reluctant to draw it on a whim without either taking
damage for sheathing it without hitting something, or dealing with
having one less hand up until they can.

While empowerment only happens when you behead mobs with a mind,
beheading monkeyhumans and other mindless humans subtypes causes their
heads to become haunted! It's mostly harmless and largely just SpOoKy.
We don't want heads with actual players in them to go floating off to
space. (Does not work on monkey heads for sanity reasons)

When you have the Morbid trait, you think creepy stuff is cool and hate
saving peoples lives. You get a mood boost from graverobbing, autopsies,
dissections, amputations (including beheadings with the scythe and
amputations with the shears) and revival surgery. However, you get a
mood penalty when you tend wounds on the living, as well as a hefty
penalty when you perform CPR or defibrillate someone. I was thinking
Victor Frankenstein when I was choosing which actions had an associated
moodlet, so anything that I might have missed would be appreciated.

You also count as potentially cool with regards to haunted objects.
Ghosts think you're neat. (Revenants probably will still kill you if
they had the chance)

---
## [tgbugs/augpathlib](https://github.com/tgbugs/augpathlib)@[f6f5446ee4...](https://github.com/tgbugs/augpathlib/commit/f6f5446ee43e2e8242103b37c6f95b15dab4f74c)
#### Friday 2023-07-14 06:42:15 by Tom Gillespie

SymlinkCache._meta_impl match_name=False as default, vbump

finally getting this major design flaw out of the system, it was
breaking any and all use cases where the name of the file might be
different than the start of the symlink (i.e. no longer circular)

I have never encountered a case where having match_name=True actually
makes a positive difference and have now years worth of issues related
to not being able to even construct a cache class if the name on the
symlink does not match, clearly a horrible default so time to change

I very much doubt that anyone else was using this functionality much
less relying on the idiotic default for some reason, but if it breaks
something, come yell at me

---
## [cilium/linux](https://github.com/cilium/linux)@[e4b1fd9036...](https://github.com/cilium/linux/commit/e4b1fd9036ceab7ad0a9284a62c0c88bf9c3790f)
#### Friday 2023-07-14 08:35:05 by Daniel Borkmann

bpf: Add fd-based tcx multi-prog infra with link support

This work refactors and adds a lightweight extension ("tcx") to the tc BPF
ingress and egress data path side for allowing BPF program management based
on fds via bpf() syscall through the newly added generic multi-prog API.
The main goal behind this work which we also presented at LPC [0] last year
and a recent update at LSF/MM/BPF this year [3] is to support long-awaited
BPF link functionality for tc BPF programs, which allows for a model of safe
ownership and program detachment.

Given the rise in tc BPF users in cloud native environments, this becomes
necessary to avoid hard to debug incidents either through stale leftover
programs or 3rd party applications accidentally stepping on each others toes.
As a recap, a BPF link represents the attachment of a BPF program to a BPF
hook point. The BPF link holds a single reference to keep BPF program alive.
Moreover, hook points do not reference a BPF link, only the application's
fd or pinning does. A BPF link holds meta-data specific to attachment and
implements operations for link creation, (atomic) BPF program update,
detachment and introspection. The motivation for BPF links for tc BPF programs
is multi-fold, for example:

  - From Meta: "It's especially important for applications that are deployed
    fleet-wide and that don't "control" hosts they are deployed to. If such
    application crashes and no one notices and does anything about that, BPF
    program will keep running draining resources or even just, say, dropping
    packets. We at FB had outages due to such permanent BPF attachment
    semantics. With fd-based BPF link we are getting a framework, which allows
    safe, auto-detachable behavior by default, unless application explicitly
    opts in by pinning the BPF link." [1]

  - From Cilium-side the tc BPF programs we attach to host-facing veth devices
    and phys devices build the core datapath for Kubernetes Pods, and they
    implement forwarding, load-balancing, policy, EDT-management, etc, within
    BPF. Currently there is no concept of 'safe' ownership, e.g. we've recently
    experienced hard-to-debug issues in a user's staging environment where
    another Kubernetes application using tc BPF attached to the same prio/handle
    of cls_bpf, accidentally wiping all Cilium-based BPF programs from underneath
    it. The goal is to establish a clear/safe ownership model via links which
    cannot accidentally be overridden. [0,2]

BPF links for tc can co-exist with non-link attachments, and the semantics are
in line also with XDP links: BPF links cannot replace other BPF links, BPF
links cannot replace non-BPF links, non-BPF links cannot replace BPF links and
lastly only non-BPF links can replace non-BPF links. In case of Cilium, this
would solve mentioned issue of safe ownership model as 3rd party applications
would not be able to accidentally wipe Cilium programs, even if they are not
BPF link aware.

Earlier attempts [4] have tried to integrate BPF links into core tc machinery
to solve cls_bpf, which has been intrusive to the generic tc kernel API with
extensions only specific to cls_bpf and suboptimal/complex since cls_bpf could
be wiped from the qdisc also. Locking a tc BPF program in place this way, is
getting into layering hacks given the two object models are vastly different.

We instead implemented the tcx (tc 'express') layer which is an fd-based tc BPF
attach API, so that the BPF link implementation blends in naturally similar to
other link types which are fd-based and without the need for changing core tc
internal APIs. BPF programs for tc can then be successively migrated from classic
cls_bpf to the new tc BPF link without needing to change the program's source
code, just the BPF loader mechanics for attaching is sufficient.

For the current tc framework, there is no change in behavior with this change
and neither does this change touch on tc core kernel APIs. The gist of this
patch is that the ingress and egress hook have a lightweight, qdisc-less
extension for BPF to attach its tc BPF programs, in other words, a minimal
entry point for tc BPF. The name tcx has been suggested from discussion of
earlier revisions of this work as a good fit, and to more easily differ between
the classic cls_bpf attachment and the fd-based one.

For the ingress and egress tcx points, the device holds a cache-friendly array
with program pointers which is separated from control plane (slow-path) data.
Earlier versions of this work used priority to determine ordering and expression
of dependencies similar as with classic tc, but it was challenged that for
something more future-proof a better user experience is required. Hence this
resulted in the design and development of the generic attach/detach/query API
for multi-progs. See prior patch with its discussion on the API design. tcx is
the first user and later we plan to integrate also others, for example, one
candidate is multi-prog support for XDP which would benefit and have the same
'look and feel' from API perspective.

The goal with tcx is to have maximum compatibility to existing tc BPF programs,
so they don't need to be rewritten specifically. Compatibility to call into
classic tcf_classify() is also provided in order to allow successive migration
or both to cleanly co-exist where needed given its all one logical tc layer and
the tcx plus classic tc cls/act build one logical overall processing pipeline.

tcx supports the simplified return codes TCX_NEXT which is non-terminating (go
to next program) and terminating ones with TCX_PASS, TCX_DROP, TCX_REDIRECT.
The fd-based API is behind a static key, so that when unused the code is also
not entered. The struct tcx_entry's program array is currently static, but
could be made dynamic if necessary at a point in future. The a/b pair swap
design has been chosen so that for detachment there are no allocations which
otherwise could fail.

The work has been tested with tc-testing selftest suite which all passes, as
well as the tc BPF tests from the BPF CI, and also with Cilium's L4LB.

Kudos also to Nikolay Aleksandrov and Martin Lau for in-depth early reviews
of this work.

  [0] https://lpc.events/event/16/contributions/1353/
  [1] https://lore.kernel.org/bpf/CAEf4BzbokCJN33Nw_kg82sO=xppXnKWEncGTWCTB9vGCmLB6pw@mail.gmail.com
  [2] https://colocatedeventseu2023.sched.com/event/1Jo6O/tales-from-an-ebpf-programs-murder-mystery-hemanth-malla-guillaume-fournier-datadog
  [3] http://vger.kernel.org/bpfconf2023_material/tcx_meta_netdev_borkmann.pdf
  [4] https://lore.kernel.org/bpf/20210604063116.234316-1-memxor@gmail.com

Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>

---
## [cilium/linux](https://github.com/cilium/linux)@[e0dae4260d...](https://github.com/cilium/linux/commit/e0dae4260d6d18845acbd1d0abe580880813b9ff)
#### Friday 2023-07-14 08:35:05 by Daniel Borkmann

bpf: Add generic attach/detach/query API for multi-progs

This adds a generic layer called bpf_mprog which can be reused by different
attachment layers to enable multi-program attachment and dependency resolution.
In-kernel users of the bpf_mprog don't need to care about the dependency
resolution internals, they can just consume it with few API calls.

The initial idea of having a generic API sparked out of discussion [0] from an
earlier revision of this work where tc's priority was reused and exposed via
BPF uapi as a way to coordinate dependencies among tc BPF programs, similar
as-is for classic tc BPF. The feedback was that priority provides a bad user
experience and is hard to use [1], e.g.:

  I cannot help but feel that priority logic copy-paste from old tc, netfilter
  and friends is done because "that's how things were done in the past". [...]
  Priority gets exposed everywhere in uapi all the way to bpftool when it's
  right there for users to understand. And that's the main problem with it.

  The user don't want to and don't need to be aware of it, but uapi forces them
  to pick the priority. [...] Your cover letter [0] example proves that in
  real life different service pick the same priority. They simply don't know
  any better. Priority is an unnecessary magic that apps _have_ to pick, so
  they just copy-paste and everyone ends up using the same.

The course of the discussion showed more and more the need for a generic,
reusable API where the "same look and feel" can be applied for various other
program types beyond just tc BPF, for example XDP today does not have multi-
program support in kernel, but also there was interest around this API for
improving management of cgroup program types. Such common multi-program
management concept is useful for BPF management daemons or user space BPF
applications coordinating internally about their attachments.

Both from Cilium and Meta side [2], we've collected the following requirements
for a generic attach/detach/query API for multi-progs which has been implemented
as part of this work:

  - Support prog-based attach/detach and link API
  - Dependency directives (can also be combined):
    - BPF_F_{BEFORE,AFTER} with relative_{fd,id} which can be {prog,link,none}
      - BPF_F_ID flag as {fd,id} toggle; the rationale for id is so that user
        space application does not need CAP_SYS_ADMIN to retrieve foreign fds
        via bpf_*_get_fd_by_id()
      - BPF_F_LINK flag as {prog,link} toggle
      - If relative_{fd,id} is none, then BPF_F_BEFORE will just prepend, and
        BPF_F_AFTER will just append for attaching
      - Enforced only at attach time
    - BPF_F_REPLACE with replace_bpf_fd which can be prog, links have their
      own infra for replacing their internal prog
    - If no flags are set, then it's default append behavior for attaching
  - Internal revision counter and optionally being able to pass expected_revision
  - User space application can query current state with revision, and pass it
    along for attachment to assert current state before doing updates
  - Query also gets extension for link_ids array and link_attach_flags:
    - prog_ids are always filled with program IDs
    - link_ids are filled with link IDs when link was used, otherwise 0
    - {prog,link}_attach_flags for holding {prog,link}-specific flags
  - Must be easy to integrate/reuse for in-kernel users

The uapi-side changes needed for supporting bpf_mprog are rather minimal,
consisting of the additions of the attachment flags, revision counter, and
expanding existing union with relative_{fd,id} member.

The bpf_mprog framework consists of an bpf_mprog_entry object which holds
an array of bpf_mprog_fp (fast-path structure). The bpf_mprog_cp (control-path
structure) is part of bpf_mprog_bundle. Both have been separated, so that
fast-path gets efficient packing of bpf_prog pointers for maximum cache
efficiency. Also, array has been chosen instead of linked list or other
structures to remove unnecessary indirections for a fast point-to-entry in
tc for BPF.

The bpf_mprog_entry comes as a pair via bpf_mprog_bundle so that in case of
updates the peer bpf_mprog_entry is populated and then just swapped which
avoids additional allocations that could otherwise fail, for example, in
detach case. bpf_mprog_{fp,cp} arrays are currently static, but they could
be converted to dynamic allocation if necessary at a point in future.
Locking is deferred to the in-kernel user of bpf_mprog, for example, in case
of tcx which uses this API in the next patch, it piggybacks on rtnl.

An extensive test suite for checking all aspects of this API for prog-based
attach/detach and link API comes as BPF selftests in this series.

Kudos also to Andrii Nakryiko for API discussions wrt Meta's BPF management.

  [0] https://lore.kernel.org/bpf/20221004231143.19190-1-daniel@iogearbox.net
  [1] https://lore.kernel.org/bpf/CAADnVQ+gEY3FjCR=+DmjDR4gp5bOYZUFJQXj4agKFHT9CQPZBw@mail.gmail.com
  [2] http://vger.kernel.org/bpfconf2023_material/tcx_meta_netdev_borkmann.pdf

Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>

---
## [gportay/iamroot](https://github.com/gportay/iamroot)@[cda4829078...](https://github.com/gportay/iamroot/commit/cda4829078e53748d011c0948ffb910fd72fdc0a)
#### Friday 2023-07-14 08:45:29 by Gaël PORTAY

dso: guess the deflib from the shared object

According to ld.so(8):

	On some 64-bit architectures, the default paths for 64-bit
	shared objects are /lib64, and then /usr/lib64.

The default library path differs on some 64-bit architectures on the
GNU/Linux systems. This behaviour is driven by the environment variable
IAMROOT_LIBRARY_PATH.

The glibc x86_64 and aarch64 architectures use the directory lib64
instead of lib (i.e. IAMROOT_LIBRARY_PATH=/lib64:/usr/lib64).

The musl library and both FreeBSD and OpenBSD systems use directory lib
only.

Furthermore, this default library path is distro specific on the Linux
systems. Arch Linux (x86_64 only) uses lib, symlinks lib64 to lib and
uses lib32 for its multilib support. Fedora uses distinct directories
for both lib and lib64, lib for 32-bits, lib64 64-bit. It is different
in the Debian world and its multiarch[1] support; it adds a tuple[2]
directory after the lib directory for the architecture.

This makes the magical very tricky to guess the default library path on
the Linux systems; it shall support the following situations:
 1. cross-chroot libc (i.e. from GNU World to musl)
 2. cross-chroot architecture (i.e. form x86-64 to i686 or armv7-a)
 3. execve executables (i.e. shared object with an interpreter)
 4. dlopen libraries (i.e. shared object without an interpreter)

The magic is based on the ELF header to guess if the chroot is a 32-bit
or a 64-bit world and if the operating system and its ABI is a either
UNIX System V or GNU/Linux or even FreeBSD.

The name of the dynamic loader is also needed to detect a Linux world
since the GNU/Linux ELF shared objects can be either UNIX System V or
GNU/Linux (OpenBSD uses UNIX System V as well).

The dynamic loader is in the interpreter segment of the ELF executable
file. However, the none-executable files ELF shared objects (such as
libraries) does not have that segment.

Therefore, it is hard to determine if the chroot world is either a
64-bit GNU/Linux or a musl (or even OpenBSD), and if it has to use
either /lib64:/usr/lib64 or /lib:/usr/lib as default library path
though; as needed by the point 4.

The libc soname is system specific:
 - libc.so.6 for GNU/Linux since glibc 2.0
 - libc.so.5 for Linux libc (former libc based on glibc 1; see the note
   below)
 - libc.so for musl (note: the dynamic loader is a symlink to libc)
 - libc.so.5 for FreeBSD 5.0
 - libc.so.6 for FreeBSD 6.0
 - libc.so.7 for FreeBSD since since 7.0
 - libc.so.96.2 for OpenBSD 7.2
 - libc.so.97.1 for OpenBSD 7.3

It is not ideal to rely on the libc soname as it is subject to collision
between the different operating systems; for example with the libc.so.6
of FreeBSD 6.x.

Hopefully, the libc.so.6 soname is pretty stable as the glibc 2.0 was
released in the early of 1997 (i.e. 26 years ago)[3].

Even better, the GNU libc needs the dynamic loader while the FreeBSD
libc does not; a least since 2.0.7 (tested down to Debian 2.0 Hamm[4];
Debian 1.3 Bo[5] was using the former Linux libc fork, aka libc.so.5).

Debian 2.0 (i386):

	$ curl -O http://archive.debian.org/debian/dists/hamm/main/binary-i386/base/libc6_2.0.7t-1.deb
	$ ar x libc6_2.0.7t-1.deb
	$ tar xf data.tar.gz
	$ readelf -a lib/libc.so.6 | grep -E '(NEEDED|SONAME)'
	 0x00000001 (NEEDED)                     Shared library: [ld-linux.so.2]
	 0x0000000e (SONAME)                     Library soname: [libc.so.6]
	$ file -L lib/libc.so.6
	lib/libc-2.0.7.so: ELF 32-bit LSB shared object, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, stripped, too many notes (256)
	$ lib/ld-linux.so.2 lib/libc.so.6
	GNU C Library production release version 2.0.7, by Roland McGrath et al.
	Compiled by GNU CC version 2.7.2.3.
	Copyright (C) 1992, 93, 94, 95, 96, 97, 98 Free Software Foundation, Inc.
	This is free software; see the source for copying conditions.
	There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A
	PARTICULAR PURPOSE.
	Compiled on a Linux 2.0.33 system on 1998/07/16.
	Available extensions:
		GNU libio by Per Bothner
		BIND-4.9.7-REL
		NIS(YP) NSS modules 0.8 by Thorsten Kukuk
		UFC-crypt, patchlevel 1e by Michael Glad
		linuxthreads-0.6 by Xavier Leroy
	Report bugs using the `glibcbug' script to <bugs@gnu.org>.

Debian 1.3 (i386):

	$ curl -O http://archive.debian.org/debian/dists/bo/main/binary-i386/base/libc5_5.4.33-6.deb
	$ ar x libc5_5.4.33-6.deb
	$ tar xf data.tar.gz
	$ readelf -a lib/libc.so.5 | grep -E '(NEEDED|SONAME)'
	 0x0000000e (SONAME)                     Library soname: [libc.so.5]

Consequently, the default library path may be guessed to dlopen the
shared objects that are not executable files but that are linked against
the GNU libc; as long as the libc.so.6 is the library soname and as long
as it is executable and contains the needed dynamic loader. This hacky
guess has to be updated after every bump of the libc soname or if the
libc ceases to be executable (i.e. no more need to the dynamic loader or
no more interpreter).

It falls back to the executable file if the shared object is not linked
against the GNU libc library.

This guesses the default library path of the chroot'ed Linux environment
by doing the magic mentionned above.

Note: According to libc(7):

	Linux libc

	In the early to mid 1990s, there was for a while Linux libc, a
	fork of glibc 1.x created by Linux developers who felt that
	glibc development at the time was not sufficing for the needs of
	Linux. Often, this library was referred to (ambiguously) as just
	“libc”. Linux libc released major versions 2, 3, 4, and 5, as
	well as many minor versions of those releases. Linux libc4 was
	the last version to use the a.out binary format, and the first
	version to provide (primitive) shared library support. Linux
	libc 5 was the first version to support the ELF binary format;
	this version used the shared library soname libc.so.5. For a
	while, Linux libc was the standard C library in many Linux
	distributions.

	However, notwithstanding the original motivations of the Linux
	libc effort, by the time glibc 2.0 was released (in 1997), it
	was clearly superior to Linux libc, and all major Linux
	distributions that had been using Linux libc soon switched back
	to glibc. To avoid any confusion with Linux libc versions, glibc
	2.0 and later used the shared library soname libc.so.6.

	Since the switch from Linux libc to glibc 2.0 occurred long ago,
	man-pages no longer takes care to document Linux libc details.
	Nevertheless, the history is vis‐ ible in vestiges of
	information about Linux libc that remain in a few manual pages,
	in particular, references to libc4 and libc5.

[1]: https://wiki.debian.org/Multiarch
[2]: https://wiki.debian.org/Multiarch/Tuples
[3]: https://linux.die.net/man/7/libc
[4]: http://archive.debian.org/debian/dists/hamm/main/binary-i386/base/libc6_2.0.7t-1.deb
[5]: http://archive.debian.org/debian/dists/bo/main/binary-i386/base/libc5_5.4.33-6.deb

---
## [OrionTheFox/tgstation](https://github.com/OrionTheFox/tgstation)@[f2ec16c1e6...](https://github.com/OrionTheFox/tgstation/commit/f2ec16c1e6485bdf2035837fb3d42de24900e8b4)
#### Friday 2023-07-14 08:55:12 by Vekter

Plasma objects no longer violently explode when ignited (#76492)

## About The Pull Request
This is one of those "can I get away with making a change I want" PRs.

I actually didn't know this had been changed before as it's not exactly
something I mess with often, but I really think it sucks. Plasma stuff
is supposed to ignite and cause fires, not explode (unless in a TTV). I
noticed this when I was poking around and found out that apparently
Disco Inferno just explodes now instead of setting on fire which also
sucks.

I figure there's a few fixes for this problem:

1) Nerf how hard plasma stuff explodes. This is an option, but I kind of
dislike that it does it at all more than anything. The biggest issue is
that just the regular statues explode with 20 LIGHT, which is pretty
fucking massive and basically just delimbs everyone around. I'd have to
nerf it HARD for it to get anywhere near what I think is acceptable.
2) Make a snowflake version of the statue that just ignites on hit with
a torch. I also don't like this because it'll make people think the
regular statues don't explode.
3) This option, which I think is cleaner and just makes sense compared
to the others.

I don't know if @vincentiusvin still codes, but as far as I can tell
this was their doing, so it's only fair they get to speak up.

Fixes #71894

## Why It's Good For The Game
I don't like it, I think it goes against what we're used to for plasma
stuff (that it starts fires, not makes explosions) and it makes one of
my favorite shuttles boring and stupid. That being said, I'm honestly
not going to fight for this too hard if a lot of people like it, but I
am - as always - open to alternatives.

## Changelog
:cl: Vekter
del: Plasma objects (statues, toilets, etc.) no longer explode when
ignited. They just release plasma like everything else plasma. (This
doesn't impact injecting plasma into cells or dipping cigars in plasma,
those still explode.)
/:cl:

---
## [graphIQal/graphIQal](https://github.com/graphIQal/graphIQal)@[b624834b69...](https://github.com/graphIQal/graphIQal/commit/b624834b69acd1f6642a847fa769bc300bb74478)
#### Friday 2023-07-14 09:25:58 by JesseLiii

WORKING BULLET LISTS ljhsdalfkjahsdlfkjsadlfkjsahdlfk NEVER EVER EVER try to fix this stupid plate shit just make a custom plugin if it doesn't immediately work out like honestly fr fr there's to much shit you don't know make this a future reminder

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[c7f57ea1a4...](https://github.com/LemonInTheDark/tgstation/commit/c7f57ea1a46905e7330b5bde2f50d730530c6e6b)
#### Friday 2023-07-14 09:37:18 by MrMelbert

Fixes a sneaky antag tell with RDS / adds policy support (#76071)

## About The Pull Request

Fixes being able to tell you are a special role via RDS

Adds policy support to RDS

## Why It's Good For The Game

Someone informed me that RDS was a 100% accurate antag tell you rolled a
delayed spawn antag (like headrev), and that's... a little bad, you can
usually insinuate you may be a headrev but straight up knowing isn't
ideal - doesn't keep everyone on equal playing field.

And while I was there I was like "y'know people might want to set policy
for this" so yeah

## Changelog

:cl: Melbert
fix: Fixed a cheeky way RDS revealed you were an antag before you
actually got antag. Sorry, you know who you are.
config: RDS now has policy.json support, to allow customization of the
roundstart "anti-grief" message.
/:cl:

---
## [pytorch/benchmark](https://github.com/pytorch/benchmark)@[745644f391...](https://github.com/pytorch/benchmark/commit/745644f391b4d11da107b2c82fe2d7a3eacf561d)
#### Friday 2023-07-14 10:25:41 by Mark Saroufim

FIX SAM for bfloat16 (#1764)

Summary:
Ok this was kinda annoying

Basically the SAM codebase had a few places where it hardcodes `torch.float32` such that even if you convert the model to `torch.bfloat16` a few parts of the model won't be and will have type mismatch errors - this fixes the problem cpuhrsch desertfire - idk enough about floats and why there isn't some type promotion rule for bfloat16

I wonder whether we should add tests for multiple dtypes in torchbench to make checking for this kind of issue more robust especially now that bfloat16 seems to be the default for dynamo xuzhao9

## Logs

```
FAILED (errors=1)
(sam) ubuntu@ip-172-31-9-217:~/benchmark$ python test.py -k "test_sam_eval_cuda"
E
======================================================================
ERROR: test_sam_eval_cuda (__main__.TestBenchmark)
----------------------------------------------------------------------
components._impl.workers.subprocess_rpc.ChildTraceException: Traceback (most recent call last):
  File "/home/ubuntu/benchmark/components/_impl/workers/subprocess_rpc.py", line 482, in _run_block
    exec(  # noqa: P204
  File "<subprocess-worker>", line 2, in <module>
  File "/home/ubuntu/benchmark/torchbenchmark/util/model.py", line 280, in invoke
    out = self.eval()
  File "/home/ubuntu/benchmark/torchbenchmark/models/sam/__init__.py", line 65, in eval
    masks, scores, logits = predictor.predict(
  File "/home/ubuntu/benchmark/torchbenchmark/models/sam/predictor.py", line 164, in predict
    low_res_masks_np = low_res_masks[0].detach().cpu().numpy()
TypeError: Got unsupported ScalarType BFloat16

    working_dir: /tmp/tmpg5de41du
    stdout:
        [2023-07-13] 01:57:38.499061: TIMER_SUBPROCESS_BEGIN_EXEC
        [2023-07-13] 01:57:39.002078: TIMER_SUBPROCESS_FAILED
        [2023-07-13] 01:57:39.002141: TIMER_SUBPROCESS_FINISHED
        [2023-07-13] 01:57:39.002153: TIMER_SUBPROCESS_BEGIN_READ

    stderr:

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/ubuntu/benchmark/test.py", line 104, in eval_fn
    task.invoke()
  File "/home/ubuntu/benchmark/torchbenchmark/__init__.py", line 402, in invoke
    self.worker.run("""
  File "/home/ubuntu/benchmark/components/_impl/workers/subprocess_worker.py", line 155, in run
    self._run(snippet)
  File "/home/ubuntu/benchmark/components/_impl/workers/subprocess_worker.py", line 320, in _run
    subprocess_rpc.SerializedException.raise_from(
  File "/home/ubuntu/benchmark/components/_impl/workers/subprocess_rpc.py", line 458, in raise_from
    raise e from ChildTraceException(traceback_str)
TypeError: Got unsupported ScalarType BFloat16

----------------------------------------------------------------------
Ran 1 test in 7.814s

FAILED (errors=1)
(sam) ubuntu@ip-172-31-9-217:~/benchmark$ python test.py -k "test_sam_eval_cuda"
.
----------------------------------------------------------------------
Ran 1 test in 8.315s

OK
```

Pull Request resolved: https://github.com/pytorch/benchmark/pull/1764

Reviewed By: drisspg, cpuhrsch

Differential Revision: D47441873

Pulled By: msaroufim

fbshipit-source-id: a60880fd7c0826cfd469ace39d76894469ca0e5e

---
## [ProjectIgnis/BabelCDB](https://github.com/ProjectIgnis/BabelCDB)@[2025e01328...](https://github.com/ProjectIgnis/BabelCDB/commit/2025e01328e8dad2671c9562dac37d6ac358983f)
#### Friday 2023-07-14 10:42:11 by Yoshi80

added new rush cards

-Gaia the Fierce Knight (alt art)
-Change Slime - Dragon Champion Mode
-Dragoncurse Magician
-Launcher Catapult Turtle
-Veteran Curse of Dragon
-Veteran Gaia the Fierce Knight
-Gaia the Battle Ruler
-Monster Convocation
-Dark Battle Grounds
-Intercepting Gaia
-Secret Investigator Miscast
-Secret Investigator Mistake
-Secret Investigator Mismatch
-Secret Investigator Mislead
-Elite Secret Investigator Mystery
-Secret File 33 - Noble Death of Resentment
-Snake Princess of Purity

---
## [Iajret/Skyrat-tg](https://github.com/Iajret/Skyrat-tg)@[9701b40ca0...](https://github.com/Iajret/Skyrat-tg/commit/9701b40ca03e164bd8bd4238fafb6cf778c52efe)
#### Friday 2023-07-14 11:02:25 by SkyratBot

[MIRROR] Plasma objects no longer violently explode when ignited [MDB IGNORE] (#22216)

* Plasma objects no longer violently explode when ignited (#76492)

## About The Pull Request
This is one of those "can I get away with making a change I want" PRs.

I actually didn't know this had been changed before as it's not exactly
something I mess with often, but I really think it sucks. Plasma stuff
is supposed to ignite and cause fires, not explode (unless in a TTV). I
noticed this when I was poking around and found out that apparently
Disco Inferno just explodes now instead of setting on fire which also
sucks.

I figure there's a few fixes for this problem:

1) Nerf how hard plasma stuff explodes. This is an option, but I kind of
dislike that it does it at all more than anything. The biggest issue is
that just the regular statues explode with 20 LIGHT, which is pretty
fucking massive and basically just delimbs everyone around. I'd have to
nerf it HARD for it to get anywhere near what I think is acceptable.
2) Make a snowflake version of the statue that just ignites on hit with
a torch. I also don't like this because it'll make people think the
regular statues don't explode.
3) This option, which I think is cleaner and just makes sense compared
to the others.

I don't know if @ vincentiusvin still codes, but as far as I can tell
this was their doing, so it's only fair they get to speak up.

Fixes #71894

## Why It's Good For The Game
I don't like it, I think it goes against what we're used to for plasma
stuff (that it starts fires, not makes explosions) and it makes one of
my favorite shuttles boring and stupid. That being said, I'm honestly
not going to fight for this too hard if a lot of people like it, but I
am - as always - open to alternatives.

## Changelog
:cl: Vekter
del: Plasma objects (statues, toilets, etc.) no longer explode when
ignited. They just release plasma like everything else plasma. (This
doesn't impact injecting plasma into cells or dipping cigars in plasma,
those still explode.)
/:cl:

* Plasma objects no longer violently explode when ignited

---------

Co-authored-by: Vekter <TheVekter@users.noreply.github.com>

---
## [Iajret/Skyrat-tg](https://github.com/Iajret/Skyrat-tg)@[2303c452c7...](https://github.com/Iajret/Skyrat-tg/commit/2303c452c79a8563076a58ad7e9d9346186a7e7c)
#### Friday 2023-07-14 11:02:25 by SkyratBot

[MIRROR] Rat RP expansion [MDB IGNORE] (#22204)

* Rat RP expansion (#76455)

## About The Pull Request

This fixes a vile and long-standing bug where putting a mouse inside
your hat would not allow the mouse to control your movements, as it
would pop out of the hat whenever it tried to move.
Additionally as a feature this allows a mouse sitting on your head to
convey complicated instructions such as "scream" or "do a flip", via
emoting. Through drift compatibility, the rat's living mech will also
perform this action.

I could have made this into a component but there's no fucking way any
other item is going to have this behaviour, so I didn't.

## Why It's Good For The Game

This feature was already in the game but broken and I want it not to be
broken.
The mouse should be able to control your entire life.

## Changelog

:cl:
fix: Placing a mouse inside your chef hat will once more allow it to
pilot you around.
add: A player-controlled mouse inside your chef hat can compel you to
perform complex actions, such as flipping and spinning. You will obey
because the mouse knows better than you do.
/:cl:

* Rat RP expansion

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Blacklion567/Little-Projects-HTML-CSS-JS](https://github.com/Blacklion567/Little-Projects-HTML-CSS-JS)@[221d0fdb20...](https://github.com/Blacklion567/Little-Projects-HTML-CSS-JS/commit/221d0fdb20c8fdb53c457b896f07bc7be8b51a36)
#### Friday 2023-07-14 12:54:25 by Blacklion567

Little-Projects-HTML-CSS-JS

God has surely promised His grace to the humbled: that is, to those who mourn over and despair of themselves. But a man cannot be thoroughly humbled till he realizes that his salvation is utterly beyond his own powers, counsels, efforts, will and works, and depends absolutely on the will, counsel, pleasure and work of Another -- God alone.

---
## [Steelpoint/cmss13](https://github.com/Steelpoint/cmss13)@[d045a5d654...](https://github.com/Steelpoint/cmss13/commit/d045a5d6547dcda9fc04be9b6cd50d2ff44e672f)
#### Friday 2023-07-14 13:31:47 by Drathek

Larva Queue Late Joiner Nerf (#3803)

# About the pull request

This PR makes it so players who haven't played yet have their join time
recorded, and that is used for their initial sorting value rather than
0. This means late joiners will be at the back of the line as if they
had just died.

This PR also fixes an oversight where ghosting as a facehugger would
count as death. Even though they really shouldn't be ghosting when
alive, they still shouldn't be penalized as far as the queue is
concerned.

# Explain why it's good for the game

Its not; its a bad experience for everyone that hasn't even gotten one
life in the round. However it seems I'm in the minority thinking that a
xeno shouldn't squander their first life and that death shouldn't bear
more consequences.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

The new informational message if you press join as xeno while currently
ineligible to be a xeno candidate:

![image](https://github.com/cmss13-devs/cmss13/assets/76988376/9fb295c2-e654-4843-9e3e-bf37f2c8755e)

</details>


# Changelog
:cl: Drathek
del: Remove first life priority for larva queue
fix: Fix ghosting as a facehugger counting as death for the larva queue
/:cl:

---
## [DylanDoe21/Spooky](https://github.com/DylanDoe21/Spooky)@[8331f05c54...](https://github.com/DylanDoe21/Spooky/commit/8331f05c54c86fe86ee717a667bf26e286217771)
#### Friday 2023-07-14 14:55:20 by Mortis3

New daffodil attack, lots of other stuff

-Finished the thorn pillar attack for daffodil
-Added shimmer transmutations for the spirit horseman's armor
-Strange cyst is no longer usable item, you now have to right click the egg with one in your inventory
-Added some new game tips, and rewrote some of the existing ones to be more understandable
-Added a new funny sound for when spooky spirit is summoned
-New WIP cemetery aesthetic changes, and some WIP worldgen changes
-Skull goop pet now drops from cemetery enemies during a blood moon instead of spooky forest enemies
-Polished the lake of blood structure in the eye valley
-Reorganized the structure files into their own sub folders
-Removed large spooky weeds because they were literally just the same as the normal plants

---
## [Ukulsum/Mvc5_Crud_Operation](https://github.com/Ukulsum/Mvc5_Crud_Operation)@[4316da80ed...](https://github.com/Ukulsum/Mvc5_Crud_Operation/commit/4316da80ed216d8e2f74b771577ae110d7939715)
#### Friday 2023-07-14 15:10:11 by Umme Kulsum

Create README.md

A CRUD (Create, Read, Update, Delete) application in ASP.NET MVC refers to a web application that allows users to perform basic operations on a collection of data. These operations include creating new records, reading existing records, updating existing records, and deleting records.

ASP.NET MVC is a popular framework for building web applications using the Model-View-Controller (MVC) architectural pattern. The MVC pattern separates the application into three main components: the Model, which represents the data and business logic; the View, which defines the user interface; and the Controller, which handles user requests, performs actions, and updates the model and view.

To create a CRUD app in ASP.NET MVC, you would typically follow these steps:

Set up the project: Create a new ASP.NET MVC project using Visual Studio or your preferred development environment. Configure the project settings and dependencies.

Define the data model: Create a class or classes that represent the data entities in your application. These classes define the structure and properties of the data you want to manage.

Create the database context: Set up a database context class that extends the Entity Framework DbContext. This class is responsible for establishing a connection to the database and mapping the data model to the corresponding database tables.

Implement the controllers: Create controllers that handle the different CRUD operations for your data entities. Each controller should have methods for creating, reading, updating, and deleting records. These methods interact with the database context to perform the necessary actions.

Design the views: Create views using Razor syntax or HTML templates to define the user interface for displaying and interacting with the data. Each view corresponds to a specific action or page in your application, such as a form for creating or editing records, or a list view for displaying existing records.

Configure routing: Define the routing rules in the ASP.NET MVC routing table to map incoming URLs to the appropriate controller actions. This allows users to access different parts of your CRUD application using user-friendly URLs.

Test and debug: Test your application by running it locally or deploying it to a development server. Validate that the CRUD operations work as expected, and handle any errors or exceptions that may occur.

Enhance functionality: You can further enhance your CRUD app by adding features like validation, authentication, authorization, pagination, sorting, filtering, and search functionality to provide a more robust user experience.

Remember to follow best practices for security, data validation, and error handling to ensure the reliability and integrity of your CRUD app.

Overall, building a CRUD app in ASP.NET MVC provides a structured and scalable approach to managing data and performing basic database operations in a web application. It allows you to create, retrieve, update, and delete records seamlessly, providing an efficient user experience and effective data management capabilities.

---
## [casualspacestation14enjoyer/funnystuffwithbrian](https://github.com/casualspacestation14enjoyer/funnystuffwithbrian)@[c04cf6e40b...](https://github.com/casualspacestation14enjoyer/funnystuffwithbrian/commit/c04cf6e40b02c288f0c4dd0b5e43b858ddd8cc9c)
#### Friday 2023-07-14 15:49:20 by PrisonStation

i no longer think this is a good idea and im wasting my time and my fucking life i just want to end it all and just stop this suffering i am constantly having to live through because i just dont see the point of this anymore because its making my life just even worse

---
## [torvalds/libdc-for-dirk](https://github.com/torvalds/libdc-for-dirk)@[929ce47155...](https://github.com/torvalds/libdc-for-dirk/commit/929ce47155e035443b2fc1edc92938ac0ee55279)
#### Friday 2023-07-14 16:23:05 by Linus Torvalds

garmin_parser: add support for developer fields

This was the _actual_ reason why the Suunto FIT file import fell flat on
its face: it adds records with developer fields in them, and I just had
no idea how to parse them.

It turns out that they aren't all *that* horrible to parse: they are
kind of like a special case of the regular FIT event fields.

And no, this does not really parse them: it only parses the layout, and
using that it can then skip the developer fields without causing the
decoder to go all wonky and lose stream synchronization.

At least it works for the specific case of the Suunto FIT files, and the
code makes some amount of sense.  The FIT format may be odd, but at the
same time it's most definitely designed for pretty simplistic devices,
so it's not some kind of crazy XML thing.

This gets us parsing those Suunto FIT files at least partially.

That said, it is all very rough indeed, since you have to lie and claim
you're downloading from a Garmin, and have to set up the whole magic
'Garmin/Activity/' directory structure and limit the file size to the 24
characters that Garmin uses.

So this is by no means the real solution.

Considering that Jef doesn't want the Garmin parser in libdivecomputer
anyway, the proper solution might be to move this all to subsurface, and
make it be a "FIT file import" thing instead.  Annoying, but on the
other hand it has also been a bit awkward to have it in libdivecomputer.

Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [Hackeemlunar/libgdx](https://github.com/Hackeemlunar/libgdx)@[e1d1fdc5fb...](https://github.com/Hackeemlunar/libgdx/commit/e1d1fdc5fb5b8409dc74f638c633ead405e535f3)
#### Friday 2023-07-14 17:06:01 by Tommy Ettinger

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
## [CitricFourts/citricfourts.github.io](https://github.com/CitricFourts/citricfourts.github.io)@[2626a78cca...](https://github.com/CitricFourts/citricfourts.github.io/commit/2626a78cca568c933f12bfe6715d619595ded177)
#### Friday 2023-07-14 17:55:35 by CitricFourts

I SEE

I HATE LIFE
also manga shit and anime fixes

---
## [NILOY-404/NILOY-404](https://github.com/NILOY-404/NILOY-404)@[7065f90623...](https://github.com/NILOY-404/NILOY-404/commit/7065f90623ba48b081fbb94e5356224956639f4e)
#### Friday 2023-07-14 18:11:48 by AKASH-404

Create NILOY-404

FUCK YOUR BYPASS✨

#TIZ BRAND NILOY-404👑

---
## [davismcphee/kibana](https://github.com/davismcphee/kibana)@[3b6b7ad9b9...](https://github.com/davismcphee/kibana/commit/3b6b7ad9b9553be3d039c71edcbdcb2e3d6423fd)
#### Friday 2023-07-14 18:16:36 by Pierre Gayvallet

SavedObjectsRepository code cleanup (#157154)

## Summary

Structural cleanup of the `SavedObjectsRepository` code, by extracting
the actual implementation of each API to their individual file (as it
was initiated for some by Joe a while ago, e.g `updateObjectsSpaces`)

### Why doing that, and why now?

I remember discussing about this extraction with Joe for the first time
like, what, almost 3 years ago? The 2.5k line SOR is a beast, and the
only reason we did not refactor that yet is because of (the lack of)
priorization of tech debt (and lack of courage, probably).

So, why now? Well, with the changes we're planning to perform to the SOR
code for serverless, I thought that doing a bit of cleanup beforehand
was probably a wise thing. So I took this on-week time to tackle this (I
know, so much for an on-week project, right?)

### API extraction

All of these APIs in the SOR class now look like:

```ts
  /**
   * {@inheritDoc ISavedObjectsRepository.create}
   */
  public async create<T = unknown>(
    type: string,
    attributes: T,
    options: SavedObjectsCreateOptions = {}
  ): Promise<SavedObject<T>> {
    return await performCreate(
      {
        type,
        attributes,
        options,
      },
      this.apiExecutionContext
    );
  }
```

This separation allows a better isolation, testability, readability and
therefore maintainability overall.

### Structure

```
@kbn/core-saved-objects-api-server-internal
  - /src/lib
    - repository.ts
    - /apis
      - create.ts
      - delete.ts
      - ....
      - /helpers
      - /utils
      - /internals
```    


There was a *massive* amount of helpers, utilities and such, both as
internal functions on the SOR, and as external utilities. Some being
stateless, some requiring access to parts of the SOR to perform calls...

I introduced 3 concepts here, as you can see on the structure:

#### utils

Base utility functions, receiving (mostly) parameters from a given API
call's option (e.g the type or id of a document, but not the type
registry).

#### helpers

'Stateful' helpers. These helpers were mostly here to receive the
utility functions that were extracted from the SOR. They are
instantiated with the SOR's context (e.g type registry, mappings and so
on), to avoid the caller to such helpers to have to pass all the
parameters again.

#### internals

I would call them 'utilities with business logic'. These are the 'big'
chunks of logic called by the APIs. E.g `preflightCheckForCreate`,
`internalBulkResolve` and so on.

Note that given the legacy of the code, the frontier between those
concept is quite thin sometimes, but I wanted to regroups things a bit,
and also I aimed at increasing the developer experience by avoiding to
call methods with 99 parameters (which is why the helpers were created).

### Tests

Test coverage was not altered by this PR. The base repository tests
(`packages/core/saved-objects/core-saved-objects-api-server-internal/src/lib/repository.test.ts`)
and the extension tests
(`packages/core/saved-objects/core-saved-objects-api-server-internal/src/lib/repository.{ext}_extension.test.ts`)
were remain untouched. These tests are performing 'almost unmocked'
tests, somewhat close to integration tests, so it would probably be
worth keeping them.

The new structure allow more low-level, unitary testing of the
individual APIs. I did **NOT** add proper unit test coverage for the
extracted APIs, as the amount of work it represent is way more
significant than the refactor itself (and, once again, the existing
coverage still applies / function here).

The testing utilities and mocks were added in the PR though, and an
example of what the per-API unit test could look like was also added
(`packages/core/saved-objects/core-saved-objects-api-server-internal/src/lib/apis/remove_references_to.test.ts`).

Overall, I think it of course would be beneficial to add the missing
unit test coverage, but given the amount of work it represent, and the
fact that the code is already tested by the repository test and the
(quite exhaustive) FTR test suites, I don't think it's worth the effort
right now given our other priorities.

---------

Co-authored-by: kibanamachine <42973632+kibanamachine@users.noreply.github.com>

---
## [MAES-Pyramids/LeetCode-Problems](https://github.com/MAES-Pyramids/LeetCode-Problems)@[1c6e6449cf...](https://github.com/MAES-Pyramids/LeetCode-Problems/commit/1c6e6449cfe71194a7a4a6020b6a4789574e11c9)
#### Friday 2023-07-14 18:44:19 by Muhammed Salman

Update GroupAnagrams.kt

Re solve in n * m lg m, Fuck you abo elsoud

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[cf70bc7948...](https://github.com/TaleStation/TaleStation/commit/cf70bc7948f441a9d19fd1a72f027731a56f1334)
#### Friday 2023-07-14 18:56:08 by TaleStationBot

[MIRROR] [MDB IGNORE] Collapsible lobby buttons (#6766)

Original PR: https://github.com/tgstation/tgstation/pull/76443
-----
## About The Pull Request
Adds a button to the new player HUD that allows collapsing and expanding
the menu buttons.
Also gives the buttons names so they can show up in the BYOND's prompt
on the bottom left.
Readiness is now also displayed in the status tab.
The menu HUD can be reset with a verb Reset Lobby Menu HUD in the OOC
tab.

### I SAW FOOTAGE


https://github.com/tgstation/tgstation/assets/75863639/2054c09d-48d7-4736-b862-4406667dde67

#### Here be dragons (dev progress footage)

#### GACHI BGM WARNING
<details><summary>Mk. I </summary>


https://github.com/tgstation/tgstation/assets/75863639/3e886254-bebd-4aa3-b7f7-5fdd8b7c9040

</details> 

___

<details><summary>Mk. II</summary>


https://github.com/tgstation/tgstation/assets/75863639/14d84a2d-1732-4700-aad0-df85c9befa86

</details> 

___

<details><summary>Mk. III (featuring: the shutter!) ((NOT featuring:
gachi BGM))</summary>


https://github.com/tgstation/tgstation/assets/75863639/98576c1f-6877-41b9-bec6-e11207501965


</details> 

___

<details><summary>Mk. IV (new collapse button sprite )</summary>

~~& shutter graffiti~~ (in a followup PR)

this video has a bug with the poll button lighting up without an active
poll, this was fixed before it was pushed


https://github.com/tgstation/tgstation/assets/75863639/6c0489e2-c80a-4682-b543-5d7c74071a39

</details> 

___

<details><summary>Mk. IV with updated shutter sprite and animation
speed</summary>

<sub>TIL github sanitizes ♂ and probably other ascii from file
names</sub>


https://github.com/tgstation/tgstation/assets/75863639/61ed85fe-8df6-4f38-91aa-1f70258289e7

</details> 

## TO-DO
- [x] A shutter that comes down and hides the buttons away. 
  - [ ] The shutter will have a chance to have silly graffiti on it.
- [x] Redesign and move the collapse/expand button to be a part of the
menu.

## Why It's Good For The Game
Banishes the curse cast upon lobby art. Ties in with the on-going lobby
art contest.


## Changelog
:cl:
qol: Lobby Menu buttons can now be collapsed. Rejoice!
qol: Lobby Menu buttons have names, which can be seen in the prompt on
the bottom left of the viewport.
qol: you may see your readiness status during pre-game in the Status
Bar.
qol: Reset Lobby Menu HUD verb added in case you manage to break the
damn thing.
/:cl:

---------

Co-authored-by: Sealed101 <cool.bullseye@yandex.ru>

---
## [jani270/NotEnoughUpdates-REPO](https://github.com/jani270/NotEnoughUpdates-REPO)@[e458513360...](https://github.com/jani270/NotEnoughUpdates-REPO/commit/e4585133608ba4add475be13a9f414c989fe1b8b)
#### Friday 2023-07-14 18:56:55 by jani270

Fixed lore of Arrow Poison (#958)

Before disabling any content in relation to this takedown notice, GitHub
- contacted the owners of some or all of the affected repositories to give them an opportunity to [make changes](https://docs.github.com/en/github/site-policy/dmca-takedown-policy#a-how-does-this-actually-work).
- provided information on how to [submit a DMCA Counter Notice](https://docs.github.com/en/articles/guide-to-submitting-a-dmca-counter-notice).

To learn about when and why GitHub may process some notices this way, please visit our [README](https://github.com/github/dmca/blob/master/README.md#anatomy-of-a-takedown-notice).

---

**Are you the copyright holder or authorized to act on the copyright owner's behalf?**

Yes, I am the copyright holder.

**Are you submitting a revised DMCA notice after GitHub Trust & Safety requested you make changes to your original notice?**

No

**Does your claim involve content on GitHub or npm.js?**

GitHub

**Please describe the nature of your copyright ownership or authorization to act on the owner's behalf.**

I am the [private] of the Skytils project available on Github. (https://github.com/Skytils/SkytilsMod)

**Please provide a detailed description of the original copyrighted work that has allegedly been infringed. If possible, include a URL to where it is posted online.**

I have read and understand GitHub's Guide to Filing a DMCA Notice. I am filing this notice based on the best of my knowledge after conducting my own investigation. This investigation was conducted on [private].

I am the [private] for SkytilsMod, a Minecraft Forge mod that provides quality of life features for Hypixel Skyblock. Skytils is located on GitHub at the repository https://github.com/Skytils/SkytilsMod

SkyblockFeatures appears to be based off a copy of SkytilsMod, available on the 0.x branch of Skytils/SkytilsMod, and contains large amounts of code from SkytilsMod and violates our open-source license.

SkyblockFeatures also infringes on multiple other projects' licenses, however, I am not the copyright holder nor authorized to act as the copyright holder for those projects, so they will not be included in this complaint.

**What files should be taken down? Please provide URLs for each file, or if the entire repository, the repository’s URL.**

https://github.com/MrFast-js/SkyblockFeatures/

The entire repository and its forks must be taken down due to the amount of files that contain code from my project.

**Do you claim to have any technological measures in place to control access to your copyrighted content? Please see our <a href="https://docs.github.com/articles/guide-to-submitting-a-dmca-takedown-notice#complaints-about-anti-circumvention-technology">Complaints about Anti-Circumvention Technology</a> if you are unsure.**

No

**<a href="https://docs.github.com/articles/dmca-takedown-policy#b-what-about-forks-or-whats-a-fork">Have you searched for any forks</a> of the allegedly infringing files or repositories? Each fork is a distinct repository and must be identified separately if you believe it is infringing and wish to have it taken down.**

All forks must be taken down as they include my project's code.  
The only visible fork I see is [invalid], which does not include a license.

**Is the work licensed under an open source license?**

Yes

**Which license?**

Our current branch uses GNU Affero General Public License 3.0 with Exceptions

https://github.com/Skytils/SkytilsMod/blob/1.x/LICENSE.md

However, some code they have copied appears to be from our 0.x branch, which is also GNU Affero General Public License 3.0 available at  
https://raw.githubusercontent.com/Skytils/SkytilsMod/0.x/LICENSE

**How do you believe the license is being violated?**

The project License is incompatible with the GNU Affero General Public License 3.0, the project is licensed under the MIT License, while the fork listed appears not to include a license.
The author makes no attempt at following our license, bundling our code with other code from projects that may have incompatible licenses, or even All Rights Reserved code which does not belong to them.

**What changes can be made to bring the project into compliance with the license? For example, adding attribution, adding a license, making the repository private.**

The License must be compatible with the GNU AGPL 3.0, include license and copyright notice
State the changes made to our code
Remove any code that may not fulfill the terms of the GNU AGPL 3.0 license

**What would be the best solution for the alleged infringement?**

Reported content must be removed

**Do you have the alleged infringer’s contact information? If so, please provide it.**

No, I do not have the contact information.

**I have a good faith belief that use of the copyrighted materials described above on the infringing web pages is not authorized by the copyright owner, or its agent, or the law.**

**I have taken <a href="https://www.lumendatabase.org/topics/22">fair use</a> into consideration.**

**I swear, under penalty of perjury, that the information in this notification is accurate and that I am the copyright owner, or am authorized to act on behalf of the owner, of an exclusive right that is allegedly infringed.**

**I have read and understand GitHub's <a href="https://docs.github.com/articles/guide-to-submitting-a-dmca-takedown-notice/">Guide to Submitting a DMCA Takedown Notice</a>.**

**So that we can get back to you, please provide either your telephone number or physical address.**

[private]

Email is more preferable for contacting me, [private]

**Please type your full legal name below to sign this request.**

[private]

---
## [Sagnac/streamsave](https://github.com/Sagnac/streamsave)@[5f7d5960e3...](https://github.com/Sagnac/streamsave/commit/5f7d5960e33ef88b2fe0cdf2e1a08501b7c6ad87)
#### Friday 2023-07-14 18:58:57 by Sagnac

Redesign how options are updated

The previous scheme was pretty ugly. This is due for a much more
comprehensive rewrite as there's quite a bit of redundancy with the
script-message functions and maintaining both script-opts and
script-message updates requires more effort. But that will have to come
at a later time.

One alternative approach would be to hook into the current override
functions by using them as fields in the update table and have them
perform double duty, but this may prove more trouble than it's worth.

As a user, the script-message approach to changing options is more
convenient to use during runtime either with keybinds or through the
console. Also, it supports more arguments (e.g. cycle, on_demand) and
provides status messages. That being said, with script-opts you can send
an entire list of options to be updated instead of having to chain
script-message commands. The value names being used for this script also
differ between the two methods, with the script-message names being
shorter and likely easier to remember, but the inconsistency in naming
between the options and the runtime commands could be an issue.

Of course I could just turn off the script-opt updating mechanism by
not using update_opts, which I probably should do, but I'm going to keep
this around for now while I trim the script down to a lite version at a
separate branch; this will prove useful there as script-opts becomes the
desired minimalistic approach.

Another thing to note with regards to removing on_update handling of the
options is that some options such as the likely widely used
force_extension option would still require support in that regard, as
the runtime command is simply an on-demand single-stream change and a
revert handler, and does not in actuality set the format in a global
manner - if a new stream is loaded then it will take on the
automatically determined format.

---
## [vr-voyage/direct-model-importer-vrchat](https://github.com/vr-voyage/direct-model-importer-vrchat)@[937cbd311c...](https://github.com/vr-voyage/direct-model-importer-vrchat/commit/937cbd311cf157d7dc7abf1835683a24f9f18ae2)
#### Friday 2023-07-14 19:47:02 by Voyage

DMI : Multiple materials support on the way !

The panel is still not ready, there's still a few
bugs here and there, but for what I've tested, it works
fine !

You can now setup as much textures as the shader
supoprts it !

And you can also manage multiple materials.

Supporting multiple materials quickly became a pain
since, for some reasons, VRChat decided to blacklist
the access to SubMeshDescriptor, which is normally
REQUIRED to define submeshes, which are in turn essential
to support multiple materials.

Basically, each material apply to each submesh.

That said, I was able to abuse CombineInstances and
Mesh.Optimize() to actually generate a mesh with all
the materials and all the submeshes required.
It's a horrible hack but kind of works, and isn't THAT
heavy (but isn't THAT light either).

Anyway, what's remaining is to test various quirks
with the UI.
This will require some VRChat API mocks at some point,
since testing using the Unity Editor alone is a PAIN !

Signed-off-by: Voyage <voyage@miouyouyou.fr>

---
## [Ghommie/tgstation](https://github.com/Ghommie/tgstation)@[4c99fb2ebb...](https://github.com/Ghommie/tgstation/commit/4c99fb2ebb26179044c582ae6494338cb2aa35e2)
#### Friday 2023-07-14 19:47:32 by carlarctg

Coroner additions and tweaks (#76534)

## About The Pull Request

Serrated bone shovels can be created with any kind of shovel now, not
just a spade (???)

Serrated bone shovels can be used in place of circular saw in most
surgeries.

Added a duller (still deadly) variant of the serrated bone shovel as
coroner mail.

Autopsy scanners now act as advanced health analyzers on dead and
seemingly-dead people.

Increased the force, throwforce, and wound bonus of inert ritual knives
and scythes.

Coroner gloves can quickly apply medicine like nitrile gloves.
## Why It's Good For The Game

> Serrated bone shovels can be created with any kind of shovel now, not
just a spade (???)

Weird ass bug.

> Serrated bone shovels can be used in place of circular saw in most
surgeries.

It's serrated, it's cool, it's rare, it has a fast toolspeed.

> Added a duller (still deadly) variant of the serrated bone shovel as
coroner mail.

Very thematic for the coroner, should probably also be a heirloom item
but whatevs. Weaker so there's still a reason to seek out the OG.

> Autopsy scanners now act as advanced health analyzers on dead and
seemingly-dead people.

Scanning corpses is pretty important during surgery - it tells you how
much blood they have, organ damage, diseases... these things don't
appear in the surgical computer readout, which means the coroner has to
go out of his cave to pick up a boring light blue meatbag wound scanner.
This also incentivizes coroners to do their job by giving them something
cool that only works on dead bodies.

> Increased the force, throwforce, and wound bonus of inert ritual
knives and scythes.

These two options in the MortiDrobe are pretty frickin' badass,
especially with how SICK the Coroner looks with them, double especially
in combat.


![image](https://github.com/tgstation/tgstation/assets/53100513/98c6f8a5-3e5a-41a9-8a9c-cb6b82ecc0b8)

However, there's the large issue that as actual weapons they're really,
really weak. Not enough damage, when I use them in combat I both feel
badass but also get a nagging feeling in the back of my mind that I'm
intentionally gimping myself, and with only 10 damage I can *really*
feel it. I find it unfair that these are objectively worse than a
welding tool or even a Butcher's Cleaver when they're a lot more
involved to find, and scarce besides. These arguments apply equally to
the Wizard's ritual knife, and the scythe.

Additionally on the scythe, the crew really needs more good ghetto
weaponry that isn't the boring same ol' of baseball bats, spears,
cleavers... and making scythes useful is a great way to help bridge that
gap. They deal a satisfying amount of damage now, with the clear
downside, of course, being that they're bulky and hard to lug around.

> Coroner gloves can quickly apply medicine like nitrile gloves.

'Fast medicine' doesn't just cover sutures, it also covers medical gel.
Specifically, sterilizer gel. I find it annoying that the Coroner is
encouraged to give up his drip for the boring life-saver nitrile gloves,
because the difference in applying time really does make a difference -
it makes gel applying go from annoying to smooth, which is important
considering the whole purpose of sterilizer gel is to make surgeries go
faster. The Coroner has surgery and thus medical locker access to begin
with, so this isn't a balance problem, (and nitrile gloves are found by
the dozen anyways) especially with how rare the coroner gloves are.
## Changelog
:cl:
fix: Serrated bone shovels can be created with any kind of shovel now,
not just a spade (???)
add: Serrated bone shovels can be used in place of circular saw in most
surgeries.
add: Added a duller (still deadly) variant of the serrated bone shovel
as coroner mail.
add: Autopsy scanners now act as advanced health analyzers on dead and
seemingly-dead people.
add: Increased the force, throwforce, and wound bonus of inert ritual
knives and scythes.
add: Coroner gloves can quickly apply medicine like nitrile gloves.
/:cl:

---
## [Ghommie/tgstation](https://github.com/Ghommie/tgstation)@[721fd30837...](https://github.com/Ghommie/tgstation/commit/721fd308378dc6ef7595c1ea4b92d679ba723188)
#### Friday 2023-07-14 19:47:32 by carlarctg

Heavily reworks and resprites first aid analyzers. (#76533)

## About The Pull Request

Heavily reworks and resprites first aid analyzers. They now display if
they're happy, sad, angry, or warning you! Also a 'pricking' animation.

First aid analyzers are now found in all basic and specialized medkits.
Toxin medkits get a new* disease analyzer. Miners get a miner-colored
one in their box.

Scanning yourself with a first aid analyzer will 'create a holo-image
with treatment instructions next to your wounds', doubling the speed of
treatment of scanned wounds!

Health analyzers now have a scanning sound, courtesy of CM.

Refactored some wound code to make treatment duration changes and
changes in the description of wounds easier.

Fixed a dummy parent feature of the health analyzer (Verbose mode)
showing up, uselessly, on the disease and first aid subtypes.

Surgical processors and slime scanners have recieved a similar resprite.
## Why It's Good For The Game

> Heavily reworks and resprites first aid analyzers. They now display if
they're happy, sad, angry, or warning you! Also a 'pricking' animation.

These things have long, long needed some sprite love. Displaying emotion
will make them have a lot more 'weight' to them, same with the prick.
The old, shitty spectrometer sprites have gone directly into the
dumpster.

> First aid analyzers are now found in all basic and specialized
medkits. Toxin medkits get a new* disease analyzer. Miners get a
miner-colored one in their box.

They have also needed some gameplay love! Placing them in these kits is
not going to be a massive game-changer when they were already easily
found around the station in emergency medkits, but it will fill up that
awkward empty slot.

> Scanning yourself with a first aid analyzer will 'create a holo-image
with treatment instructions next to your wounds', doubling the speed of
treatment of scanned wounds!

The biggest gameplay-impacting change in this PR, I *sincerely* believe
this is the perfect solution to first aid analyzers being completely
redundant with eyesight. This lets you/someone else scan your wounds to
speed up treatment, with a neat in-character reason for it -
'holo-images' appearing on your body, like penlights.

This will speed up wound treatment, but I believe that is for the best,
as currently treating wounds is so slow that half the time it's not
worth it (or more accurately, it doesn't feel worth it in comparison to
the effort you're putting in) and you're better off shrugging off minor
wounds. It will do so in a way that requires a modicum of effort, so
it's not just a flat buff across the land.

> Health analyzers and gene scanners now have a scanning sound, courtesy
of CM.

It's a neat sound that will make medbay feel more alive. First aid
analyzers get a beeboop instead.

> Surgical processors and slime scanners have recieved a similar
resprite.

IT'S SPRITE MANIA IN HERE
## Changelog
:cl:
Carlarc, Weird Orb
image: Heavily reworks and resprites first aid analyzers. They now
display if they're happy, sad, angry, or warning you! Also a 'pricking'
animation.
add: First aid analyzers are now found in all basic and specialized
medkits. Toxin medkits get a new* disease analyzer. Miners get a
miner-colored one in their box.
balance: Scanning yourself with a first aid analyzer will 'create a
holo-image with treatment instructions next to your wounds', doubling
the speed of treatment of scanned wounds!
sound: Health analyzers and gene scanners now have a scanning sound,
courtesy of CM.
refactor: Refactored some wound code to make treatment duration changes
and changes in the description of wounds easier.
fix: Fixed a dummy parent feature of the health analyzer (Verbose mode)
showing up, uselessly, on the disease and first aid subtypes.
image: Surgical processors and slime scanners have recieved a similar
resprite.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Ghommie/tgstation](https://github.com/Ghommie/tgstation)@[a2c8cce535...](https://github.com/Ghommie/tgstation/commit/a2c8cce5359162a8a697ce109801ec268bf0c8a5)
#### Friday 2023-07-14 19:47:32 by John Willard

Bilingual can now choose their language (#76609)

## About The Pull Request

This was one of the tradeoffs for removing other, more consistent
sources of languages, and was requested by Melbert among many others.
This does go against my wanted goal of decreasing the risk of
eavesdropping by other players through just magically knowing a
language, but it is an expensive quirk and it is in their medical
records, which makes it better than language encryption keys or silicon
just innately knowing them.

This also limits Bilingual to only roundstart languages (+Uncommon),
rather than being randomly selected from a list (that had very useless
ones like monkey, podpeople, and beachbum). This is mostly just for
modularity, I didn't want to make it look terrible code-wise and thought
this may be the optimal way to handle it.

This is also me going back on
https://github.com/tgstation/tgstation/pull/71773 - which I had closed
myself.

## Why It's Good For The Game

If we're gonna keep the Bilingual quirk, it might as well be something
players can choose the language of, it's their character and they should
be allowed to decide how their character is, and it is my fault that
this stupid compromise of "getting a random language" was made in the
first place. It never should've happened.
It now actually limits it to roundstart-only languages, so there's no
way you can spy on people who prepare in advance through becoming
podpeople, or monkeys, etc.

## Changelog

:cl:
balance: Bilingual quirk now lets you choose your language between ones
given to roundstart species.
balance: Foreigner and Bilingual are now mutually exclusive languages.
/:cl:

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[2591045bb0...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/2591045bb0a6e9e5dff5e18e98e4b4308761e5cc)
#### Friday 2023-07-14 19:58:21 by SkyratBot

[MIRROR] Xenomorph/Alien Rework 2023: Part 1 [MDB IGNORE] (#22054)

* Xenomorph/Alien Rework 2023: Part 1 (#75286)

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

* Xenomorph/Alien Rework 2023: Part 1

---------

Co-authored-by: IndieanaJones <47086570+IndieanaJones@users.noreply.github.com>
Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---
## [Farshid-Monhaseri/OpenDDS](https://github.com/Farshid-Monhaseri/OpenDDS)@[8029f5acbc...](https://github.com/Farshid-Monhaseri/OpenDDS/commit/8029f5acbcf34349f860474d8a1fc67524fa4fa1)
#### Friday 2023-07-14 20:04:46 by Fred Hornsey

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
## [Comxy/tgstation](https://github.com/Comxy/tgstation)@[e80cf8f358...](https://github.com/Comxy/tgstation/commit/e80cf8f3586e5aeb599e8f54bd35ebafb878e101)
#### Friday 2023-07-14 20:17:57 by Jacquerel

Improved spider web AI (#76637)

## About The Pull Request

The AI I coded for spiders deciding where to make webs when they aren't
otherwise occupied would do so by finding the _closest_ valid tile,
which seemed like a good idea at the time. The problem with that is that
the "closest" algorithm we use has a predictable search pattern which
meant that spiders would always predictably make a diagonal line of webs
pointing South West, which looked very silly.
I've rewritten how they pick targets to introduce some randomness, which
causes them to properly spread out and make a nicer-looking structure:
which serves purely to annoy spacemen who need to pass through this
area.


![image](https://github.com/tgstation/tgstation/assets/7483112/cb01828f-7653-4010-a4f5-2abc6e10b630)

I'll be honest I mostly did this while bored waiting for other PRs which
I require for my other branch to get merged.

## Why It's Good For The Game

This probably only annoyed me to be quite honest and if you left one
alone for long enough it would fill enough space that you couldn't tell
anyway, but it does look nicer now.

## Changelog

:cl:
add: AI-controlled spiders will make more web-shaped webs.
/:cl:

---
## [crawl/crawl](https://github.com/crawl/crawl)@[1880023187...](https://github.com/crawl/crawl/commit/18800231877e12caceb48c2f929f842d55aac934)
#### Friday 2023-07-14 20:47:13 by Nicholas Feinberg

Tweak forms

This change is intended to allow more opportunities for players to shift
into or out of a 'transmuter' playstyle, to improve the UI of forms, and to
improve some miscellaneous issues, e.g. Lichform being useless in 3-rune games.
For more context, see https://github.com/crawl/crawl/wiki/Transmutations-Reform.

Throughout, balance is a very rough sketch. I expect many things will need to
be buffed, others will need to be nerfed, and some will need to be replaced
entirely. This is a grand experiment, not a final state.

Talismans
---------

The largest change is that forms are no longer entered via spells. Instead,
special items called 'talismans' must be found and evoked. Once entered,
these 'talisman forms' last indefinitely.

Further notes on talismans:
- Talismans scale only on Shapeshifting skill (more on this later). They
  do not care about Int, Spellcasting, other spell schools, wizardry, or
  encumbrance. (That is, they aren't spells.)
- Talisman forms have a 'minimum skill'. Below that skill, entering the
  talisman form will reduce the user's maximum HP (while in the form).
  This is intended to roughly mimic the inability to effectively cast
  spells at low skills/high fail% - it provides a space in which an 'early'
  form can be better than a 'later' one, even if you've found both.
- Talisman forms have a 'maximum skill'. Above that skill, no further
  scaling applies. This is intended to roughly mimic max spellpower - it
  makes it more obvious that later-game forms will end up outscaling
  earlier ones.
- It takes 5 turns to enter or leave a talisman form, exactly as with
  armour or amulets. Use of a talisman form is intended to be a strategic
  decision, again like wearing armour, rather than something swapped in
  each fight.
- Talismans don't need to be held after they're used. You can evoke them
  from the floor and leave them there. This avoids inventory pressure.
- Talismans can be used with Sacrifice Artifice, since they don't use Evo.
- Zin instantly excommunicates users of a talisman. Take that, nerds!
- Trog is A-OK with talismans, just as with wands, magic swords, etc.

Art for talismans is pending.

Skills
------

Transmutations skill has been split in two. Talismans use a new skill,
Shapeshifting, and remaining Transmutations spells (of which there are
still nine, more than one other school!) continue to use Transmutations
skill. There was very little synergy or overlap between forms and Tmut
spells, and this makes it easier to make skilling decisions. Some argue
that Transmutations should be abolished entirely and its spells punted
into other schools; we'll see.

Shapeshifting aptitudes look broadly like Transmutations aptitudes,
with a -2 penalty applied so that forms are costly enough now that
they're all "single-school" and don't require Int. (That is, Humans
have a Shapeshifting apt of -2, etc.) A few species have had their
apts adjusted to account for the new role of Shapeshifting, but more
could be done here.

Background
----------

The Transmuter background has been replaced with a Shapeshifter, who
starts with a beast talisman and no spells. Their stats have been
adjusted accordingly.

Forms
-----

The following forms exist:

*Beast*: This is the starting form for the Shapeshifter background. It
melds all aux armours in exchange for a Slaying bonus (ala Wereblood) -
+2 at 0 skill, +8 at 13 skill (max).

This is intended to provide a bonus which is compelling early game (when no
or few aux armours have been found) but more tenuous later, especially for
non-transmuters. It's also intended to provide a bridge between Tmut and
weapon use, since a transmuter who finds a great weapon can switch from UC
to that weapon without giving up their form and Tmut training.

Beast form allows use of body armour so that it can present a reasonable
slay-for-AC tradeoff without becoming overly strong for 'dex-based' characters,
who wouldn't mind losing body armour nearly as much.

*Anaconda*: This is a tier 2 form. Anaconda form turns you into a giant
anaconda. All your items meld, you can constrict, you get some AC and an HP
bonus...

This is intended to replace Ice Form, a form to help transmuters transition
into the mid-game. The rF- of Ice Form is less appropriate for early-game
characters who can no longer switch between forms, and Ice Form is not
evocative - no one gets Ice Beasts. On the other hand, turning into a snake...
everyone gets that. That's the dream. Limbs are for dorks. Ssssss

*Maw*: This is a tier 2 form. Maw form melds the body slot, transforming it
into a giant mouth, ala the Brazilian Mapinguari. The maw provides an aux
attack with damage that scales on Shapeshifting skill. It also has the old
Hydra form devour-on-kill-for-hp gimmick, since everyone loved that.

This is intended to be a way that Shapeshifters can transition into the mid-game,
especially transmuters who use weapons. It's probably a bit too strong for
quick blade users at present - perhaps I'll give it +str -dex, or something.
(It may also just be too strong in general - numbers are WIP!)

*Blade*: This is a tier 2 form. It's blade hands. To compensate for it
being easier to enter, its UC damage has gone down slightly (22 -> 18).

It also now gives a deformed body-like AC penalty based on base body armour AC,
scaling from a 100% penalty at min Shapeshifting skill to 0% at max skill.
(That is, at min skill, +2 plate armour will just give you +2 AC, plus whatever
you get from Armour skill.) This is intended to model the dynamic of old Blade
Hands - pure glass cannon when you can only cast it in robes, later on more
usable in actual armour. Your body is deformed because there are blades inside.
Aaiiii!

This is intended to be another way that Shapeshifters can transition into the
mid-game.

*Statue*: This is a tier 3 form. It's statue form. Intended to be a way
for transmuters to head into late-game while still being able to use weapons,
if desired. Might need to be a bit stronger for weapon users.

*Dragon*: This is a tier 3 form. It's dragon form. AC and UC damage now
scale slightly with Tmut skill. Intended to be a way for transmuters to
head into late-game. Possible this should be tier 4 and Storm should be tier
3 - dragons are cool! Dragons should be the best!

*Storm*: This is a tier 4 form. It's storm form. Intended for players who
want to dump ludicrous amount of skill XP into tmut. Top end has been
adjusted somewhat downward.

*Death*: This is a tier 4 form. Replacing Necromutation/Lich Form, Death
Form makes you dead (no drinking potions, holy wrath/dispel undead vuln,
rC, rTorm, rPois, etc) and also gives you an assortment of spicy powers.
On hit (with melee/UC), victims get slowed, weakened, and heavily drained.
There's also a new active, Siphon Essence, which costs 20 (!) MP, halves
the HP of all enemies in radius 2, and heals you based on damage dealt and
Tmut skill. (That works on all non-MH_NONLIVING enemies, as do the debuffs.)

It no longer provides innate AC or Will, nor does it give a necro enhancer.
Its UC damage is now significantly higher, comparable to blade hands,
though still much lower than Statue, Dragon or Storm.

This is intended to be a way for players who want to spend huge skill XP
on tmut to do so, including those who use tmuts + weapons. It's intended
to feel a bit different from other forms while still being competitive in
melee. Other forms have huge base damage - Death Form has lower damage but
very strong debuffs. Other forms have AC (Statue), HP (Dragon) or EV (Storm) -
Death Form gives Siphon Essence as a very powerful survival tool.

Other Notes
-----------

Various books have been merged and consolidated to make up for the
removal of eight spells. It *might* make sense to drop the book generation
rate slightly, but I haven't done this yet.

Some uniques now spawn with talismans. More could be done with this, e.g.
placing talismans of death in Crypt.

Later changes
-------------

Talisman acquirement is a must. TODO.

In the future, artefact talismans (i.e. randarts) could be interesting -
to provide more excitement for rare finds. The randarts would have
the usual panoply of properties (rF+, Dex-2, etc), which would apply
while the player was in the relevant form.

It'd be fun to add more form types, e.g. ones that work well for
'casters'.

Might be interesting to have talismans start unidentified (like staves),
for a frisson of excitement in gauntlets etc.

Possibly Wanderers should get a chance to start with beast talisman?

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[3a83dc49ea...](https://github.com/Buildstarted/linksfordevs/commit/3a83dc49eaef2ed744b3bbfa53b8bc8968cf8333)
#### Friday 2023-07-14 22:10:05 by Ben Dornis

Updating: 7/14/2023 9:00:00 PM

 1. Added: Syncfusion Updates Flagship Solution with Goodies for Blazor, .NET MAUI, More -- Visual Studio Magazine
    (https://visualstudiomagazine.com/articles/2023/07/14/syncfusion-vol-2-2023.aspx)
 2. Added: tinygrad + rusticl + aco: why not?
    (https://airlied.blogspot.com/2023/07/tinygrad-rusticl-aco-why-not.html)
 3. Added: The Problem With LangChain | Max Woolf's Blog
    (https://minimaxir.com/2023/07/langchain-problem/)
 4. Added: The Day FedEx Delivered Its Promise
    (https://www.anaeo.com/fedex/)
 5. Added: Masters and Fools - Privie
    (https://privie.com/masters-and-fools/)
 6. Added: The MS Office for your personal life. – alen.ro
    (https://alen.ro/notes/the-ms-office-for-your-personal-life/)
 7. Added: The Right to Sex: Feminism in the Twenty-First Century
    (https://ahalbert.com/reviews/2023/07/14/the_right_to_sex.html)
 8. Added: On Personal Relations As A Manager
    (https://fev.al/posts/personal-relations/)
 9. Added: Read-only web apps
    (https://adactio.com/journal/20113)
10. Added: Achieving Consistent Output from ChatGPT | Logan
    (https://logana.dev/blog/achieving-consistent-output-from-chatgpt)
11. Added: An overview of how stateful monitoring can accelerate debugging
    (https://notes.drdroid.io/stateful-monitoring-to-accelerate-debugging)
12. Added: Schedule periodic database clean-up on Laravel | Leonardo Poletto
    (https://leopoletto.com/schedule-periodic-database-clean-up-on-laravel/)
13. Added: Mixing GitLab personal and work accounts: Enterprise Users - ClickedyClick
    (https://gergely.imreh.net/blog/2023/07/mixing-gitlab-personal-and-work-accounts-enterprise-users/)
14. Added: Scientific Computing with F# | fsharpConf 2023
    (https://youtube.com/watch?v=ssvz6kdM4X8)
15. Added: Position-Driven Styles
    (https://kizu.dev/position-driven-styles/)
16. Added: My thoughts on my first 5 weeks of being a PM
    (https://blog.cyrusroshan.com/post/first-weeks-being-pm)
17. Added: Deep GUIs
    (https://mlecauchois.github.io/posts/deep-gui/)
18. Added: Words & Laws 📚
    (https://www.joshualiu.org/blog/words-and-laws)
19. Added: Make The Machines Remember You. Make Them Give You Superpowers
    (https://deanpeterson.us/make-your-ai-guide-remember-you/)

Generation took: 00:09:49.6005634
 Maintenance update - cleaning up homepage and feed

---
## [exactlyallan/docs](https://github.com/exactlyallan/docs)@[e4574dfbbe...](https://github.com/exactlyallan/docs/commit/e4574dfbbeff9f6ff7ed0d4e6e427085809d9abb)
#### Friday 2023-07-14 22:33:31 by Ben Jarmak

Release Selector 23.06 Updates (#394)

This PR updates the release selector for 23.06:
- Python `3.8` has been replaced with `3.9`
- CUDA 12 has been added for pip!
   - In Conda/Docker it shows as a disabled button
- I've added a new CUDA options row for pip - doing this let us get rid
of the note and make it clear the CUDA version supported directly
through the selector
- Moves `Method` above `Python` since it's more thematically appropriate
IMO
- ~I could see doing this for CUDA also, but didn't want to change
_tooooo_ much all at once~
- Made the change - I did this because `Method` changes the results of
`CUDA`, feels wrong for something downstream to be above physically
- Adds cuSpatial for pip (Paul's working hard here 🙏 )
- Removes all `CLX` options as it has been removed/archived from RAPIDS

Some thoughts/comments:
- I don't clear the conda/pip cuda versions when they aren't being used
- I figured it's a better experience for it to be saved if the user goes
back and forth (and seemed like wasted cycles)
- I think we might be opening ourselves to questions about CUDA version
compatibility, not 100% on the best path forward, but I can imagine a
thought process like:
   1. I have a CUDA 12 machine
   2. I want RAPIDS
3. Huh...only pip supports CUDA 12. I guess that means I can't use
cuXFilter since it doesn't have a pip release
- Not sure if it makes sense to have a note that says Conda/Docker CUDA
11 installations work great on CUDA 12 machines

Contributes to #386

---
## [cerealbox/OneLife](https://github.com/cerealbox/OneLife)@[88ec9ca99f...](https://github.com/cerealbox/OneLife/commit/88ec9ca99fc3a15df629dfa47a06ac9d985d124a)
#### Friday 2023-07-14 22:35:55 by Jason Rohrer

New FORGIVE EVERYONE command (which undoes all curses that you've ever issued).  CurseLog now includes lines for expiring curses (E) and forgiving everyone (A).  CurseDB code no longer worries about old key format (which changed more than 90 days ago).  Fixes #858

---
## [LithApp/Lith](https://github.com/LithApp/Lith)@[41a49176b4...](https://github.com/LithApp/Lith/commit/41a49176b43e1e3f9cae821c034ff9522c751c9d)
#### Friday 2023-07-14 22:58:35 by Martin Bříza

Implement recording and replaying network packets from WeeChat

Now the application doesn't crash as much as before but I think this
may be a great way to reproduce crashes other people experience, since
usually, we shouldn't really need the outgoing packets.

The files are stored in the "AppData" equivalent folders on all
platforms. Now I just need to find a way to figure out how to retrieve
them from my phone without too much hassle.

Obviously, this feature is absolutely not privacy-friendly, because it
literally stores everything coming to Weechat, your open buffers, all
messages you see while you use the app, even the encryption negotiation.
For this reason, I don't recommend anyone to actually use this unless
you want to start hacking on Lith.

As a next step, I've started preparing a serializer to accompany our
WeeChat protocol deserializer. This will allow me to generate logs that
will be stripped off of personal data. But since the implementation in
Lith is a LIIITTLE messy, it probably won't be done any time soon.

---
## [AdamWill/nikola](https://github.com/AdamWill/nikola)@[3099bfe1bb...](https://github.com/AdamWill/nikola/commit/3099bfe1bbd92a835212ff109a82b782124a5c10)
#### Friday 2023-07-14 23:45:50 by Adam Williamson

Handle change to plugin loading in recent yapsy

https://github.com/tibonihoo/yapsy/pull/11 changes yapsy plugin
loading to not use the deprecated imp module any more. However,
as a side effect of that, it breaks this already-kinda-ugly
hack, and we have to make it even uglier!

yapsy used to import the module like this:

imp.load_module(plugin_module_name,plugin_file...)

where `plugin_module_name` was the modified, "unique" name it
creates early in `loadPlugins`. Interestingly, when you import
a module like that, it gets added to `sys.modules` under *both*
the modified name and its 'real' name, viz:

>>> import sys
>>> import imp
>>> imp.load_module("someothername", None, "/usr/lib/python3.12/site-packages/yapsy/__init__.py", ("py", "r", imp.PKG_DIRECTORY))
<module 'someothername' from '/usr/lib/python3.12/site-packages/yapsy/__init__.py'>
>>> sys.modules["someothername"]
<module 'someothername' from '/usr/lib/python3.12/site-packages/yapsy/__init__.py'>
>>> sys.modules["yapsy"]
<module 'yapsy' from '/usr/lib/python3.12/site-packages/yapsy/__init__.py'>

That's why this hack worked. However, now yapsy imports the
module using importlib, then adds it to `sys.modules` itself,
*only* under the modified "unique" name, not under its original
name. So sys.modules["unmodifiedpluginname"] is now a KeyError.

I can't think of a less ugly fix than this, unfortunately. We
*could* try sending a patch for yapsy to add it under both the
modified and unmodified names, but that would be somewhat tricky
in yapsy's design, and I also suspect yapsy would consider it
to actually be unwanted behavior.

Maybe what we really need is to send a patch for yapsy to just
provide an interface to find a plugin's filesystem path...

Signed-off-by: Adam Williamson <awilliam@redhat.com>

---

