## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-07-04](docs/good-messages/2023/2023-07-04.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,141,331 were push events containing 3,445,916 commit messages that amount to 266,796,393 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 52 messages:


## [norsvenska/tgstation](https://github.com/norsvenska/tgstation)@[ed57b8127f...](https://github.com/norsvenska/tgstation/commit/ed57b8127f1b28507272170c60c7db16f6e02a87)
#### Tuesday 2023-07-04 00:06:33 by Jacquerel

Rat RP expansion (#76455)

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

---
## [chadlyalan/portfolio](https://github.com/chadlyalan/portfolio)@[16a20ee99a...](https://github.com/chadlyalan/portfolio/commit/16a20ee99a184dd548c24db01de1e7f42b931d60)
#### Tuesday 2023-07-04 00:45:38 by Chad

Chadlyalan/issue22 (#34)

* working animations

we converted this landing widget into a stateless widget because the animated text was freaking out when setState was called. I extracted all of the setState functionality to their individual widgets, and let landing page worry less about them.

Now the animations work just as they used to, AND when the theme get's toggled, they rebuild correctly.

* Update landing.dart

converting to stateless widget

* a light theme

this likely won't be the final light theme scheme but it works for now. I'll continue playing around with some of the colors to see how I feel about them as time goes on.

Also a small grammatical fix to the About me section.

* text colors

these changes will update the text color for the light mode to white. White comes up fairly well on the tealish background, better than the black does at any rate. It's not the best, I'm not convinced this is the final color scheme, but it's a color scheme at least.

* light theme overlap error fix

The colors aren't correct as those changes seem to be local on my PC but this includes the fix to the light theme's overlap issue. It was because I was using material3 on light, which I do like, but there was extra padding in the animated texts that was causing issues.

I also have fixed the appbar's color in this mode, as normal material had a plain white appbar in light mode by default.

I also realized that I didn't need the align widget in the landing page, as the column was already telling it's children where to be placed.

* a light theme that works

maybe not the final product but it is a light theme that doesn't cause sizing issues when turning back and forth from light/dark.
I'm not sold on the orange cards but I kinda like them. I want to do something a little bit different with the project cards if I can think of what to do.

* Update my_theme.dart

* Update my_theme.dart

* redpoint demo video

I cut together a demo video of redpoint finally. It should be working but has not been tested yet.

* project card styling

Especially in the light theme, it felt like the project cards needed a little extra love. I added a color to the entire "card" to give it a little extra feeling on hover.

I haven't decided what I should do for the mobile site to make sure it feels good.

---
## [raymond-yuan/langchain](https://github.com/raymond-yuan/langchain)@[75fb9d2fdc...](https://github.com/raymond-yuan/langchain/commit/75fb9d2fdcc201e80ad9c065a02c6cc9ccf6d716)
#### Tuesday 2023-07-04 00:50:17 by Stefano Lottini

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
## [Ghommie/tgstation](https://github.com/Ghommie/tgstation)@[8af20d1577...](https://github.com/Ghommie/tgstation/commit/8af20d157738044cef2fc00846caa1869d56a087)
#### Tuesday 2023-07-04 00:58:21 by necromanceranne

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
## [kenstir/hemlock-ios](https://github.com/kenstir/hemlock-ios)@[0199735545...](https://github.com/kenstir/hemlock-ios/commit/019973554522b16f8c9c95e6ce1cd0ca1705a262)
#### Tuesday 2023-07-04 01:20:03 by kenstir

Wire up results TableView and OMG I hate IB

* Recreate Results storyboard from scratch to get hierarchy right
* OMG I HATE IB.  The cells were not auto-resizing because of an extra
  customClass="ResultsTableViewCell" on the tableViewCellContentView
  I don't know how it got there but wow what a pain.
* For now have to fetchCodedValueMaps so we have format labels.

---
## [openai/evals](https://github.com/openai/evals)@[ab0b90c5fa...](https://github.com/openai/evals/commit/ab0b90c5fa8b2993f84d68be8bccdb0d377a68de)
#### Tuesday 2023-07-04 02:05:43 by Uday

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
## [openai/evals](https://github.com/openai/evals)@[ace845e93e...](https://github.com/openai/evals/commit/ace845e93e345e52e73f5e2e05af45b83c1c9e97)
#### Tuesday 2023-07-04 02:06:21 by Youngwook Kim

add eval_confusing_korean (#1201)

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

`confusing_korean`

### Eval description

The current model confuses some Korean usage and cannot distinguish what
is correct.

### What makes this a useful eval?

Evaluates the model's ability to correctly use confusing Korean.

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

It is a sentence that is used a lot in everyday life.

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
{"input": [{"role": "system", "content": "Answer the following question.
Is this the correct Korean usage? Answer with exactly one of the
following: 'Yes' or a 'No'. Don't add anything else to the response."},
{"role": "user", "content": "가을이 되니 입맛이 땡긴다"}], "ideal": "No"}
{"input": [{"role": "system", "content": "Answer the following question.
Is this the correct Korean usage? Answer with exactly one of the
following: 'Yes' or a 'No'. Don't add anything else to the response."},
{"role": "user", "content": "가을이 되니 입맛이 당긴다"}], "ideal": "Yes"}
{"input": [{"role": "system", "content": "Answer the following question.
Is this the correct Korean usage? Answer with exactly one of the
following: 'Yes' or a 'No'. Don't add anything else to the response."},
{"role": "user", "content": "살진 전어가 잡혔다"}], "ideal": "Yes"}
{"input": [{"role": "system", "content": "Answer the following question.
Is this the correct Korean usage? Answer with exactly one of the
following: 'Yes' or a 'No'. Don't add anything else to the response."},
{"role": "user", "content": "살찐 전어가 잡혔다"}], "ideal": "No"}
{"input": [{"role": "system", "content": "Answer the following question.
Is this the correct Korean usage? Answer with exactly one of the
following: 'Yes' or a 'No'. Don't add anything else to the response."},
{"role": "user", "content": "일이 얼마큼 진행됐을까?"}], "ideal": "Yes"}
  ```
</details>

---
## [openai/evals](https://github.com/openai/evals)@[1c9bc7f61b...](https://github.com/openai/evals/commit/1c9bc7f61b88b909b5351a3c20edafe4fd113d09)
#### Tuesday 2023-07-04 02:10:57 by Zhou Guanghui

[Eval]Identify Chinese Shi Jing Title (#1245)

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

Identify Chinese Shi Jing title

### Eval description

Given some content from the "Classic of Poetry" (also known as "Shi
Jing"), return its title.

### What makes this a useful eval?

"The Classic of Poetry" (also known as "Shi Jing") is an important
collection of ancient Chinese literature and the earliest existing
anthology of poetry in China. It is also known as "Three Hundred Poems."
It is considered the foundation of ancient Chinese poetry and
encompasses a wide range of themes, reflecting the social customs,
people's lives, and thoughts during the Western Zhou period (11th
century BC to 6th century BC). Shi Jing consists of 305 poems and is
divided into three sections: Feng (Air), Ya (Elegant), and Song (Odes).
Each poem is composed in the form of verses and stanzas, used to praise,
depict specific events, scenes, or emotions. Currently, Both of GPT-3.5
and GPT-4 models can only give correct titles to only a few of the more
well-known content in Shi Jing, and the rest are returned randomly.

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

All contents and titles of this eval are from 诗经析读 published by Zhonghua
Book Company in 2018. All entries are double-checked to make sure they
are correct.

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

{"input":[{"role":"user","content":"下面这段内容出自诗经的哪一篇？请只回复包含完整分类结构的篇目名称，不要包含其他内容。例如：《周南·关雎》\n---\n关关雎鸠，在河之洲。窈窕淑女，君子好逑。"}],"ideal":"《周南·关雎》"}

{"input":[{"role":"user","content":"下面这段内容出自诗经的哪一篇？请只回复包含完整分类结构的篇目名称，不要包含其他内容。例如：《周南·关雎》\n---\n桃之夭夭，灼灼其华。之子于归，宜其室家。"}],"ideal":"《周南·桃夭》"}

{"input":[{"role":"user","content":"下面这段内容出自诗经的哪一篇？请只回复包含完整分类结构的篇目名称，不要包含其他内容。例如：《周南·关雎》\n---\n蒹葭苍苍，白露为霜。所谓伊人，在水一方。"}],"ideal":"《秦风·蒹葭》"}

{"input":[{"role":"user","content":"下面这段内容出自诗经的哪一篇？请只回复包含完整分类结构的篇目名称，不要包含其他内容。例如：《周南·关雎》\n---\n死生契阔，与子成说。执子之手，与子偕老。"}],"ideal":"《邶风·击鼓》"}

{"input":[{"role":"user","content":"下面这段内容出自诗经的哪一篇？请只回复包含完整分类结构的篇目名称，不要包含其他内容。例如：《周南·关雎》\n---\n摽有梅，其实七兮。求我庶士，迨其吉兮。"}],"ideal":"《召南·摽有梅》"}
  ```
</details>

---
## [openai/evals](https://github.com/openai/evals)@[bae0f38789...](https://github.com/openai/evals/commit/bae0f38789b9c91e0446bfdc20a00f200d845a11)
#### Tuesday 2023-07-04 02:12:47 by Gregor Lichtner

[Eval] SMILES to molecular formula (#1252)

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

SMILES to Molecular Formula Conversion

### Eval description

Conversion of SMILES (Simplified Molecular Input Line Entry System)
strings -- a widely used ASCII string notation for molecular structures
-- to the corresponding molecular formula (the types and numbers of
atoms in the molecule).

### What makes this a useful eval?

This conversion is of utility in cheminformatics, the intersection of
chemistry and computer science. It is invaluable in various contexts
such as drug discovery, where large databases of chemicals are often
stored as SMILES strings. Converting these SMILES strings into molecular
formulas can provide a quick understanding of the molecular composition,
without having to decipher the original SMILES string.

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
{"input": [{"role": "system", "content": "Tell me the molecular formula
of the following canonical SMILES string. Please provide explanations
for your decision-making process and provide the final answer in square
brackets."}, {"role": "user", "content": "COC(=O)/C=C/c1ccccc1"}],
"ideal": "[C10H10O2]"}
{"input": [{"role": "system", "content": "Tell me the molecular formula
of the following canonical SMILES string. Please provide explanations
for your decision-making process and provide the final answer in square
brackets."}, {"role": "user", "content": "O=C1c2ccccc2C(=O)c2ccccc21"}],
"ideal": "[C14H8O2]"}
{"input": [{"role": "system", "content": "Tell me the molecular formula
of the following canonical SMILES string. Please provide explanations
for your decision-making process and provide the final answer in square
brackets."}, {"role": "user", "content": "CCCCCCCCCCCCCCCCCCN"}],
"ideal": "[C18H39N]"}
{"input": [{"role": "system", "content": "Tell me the molecular formula
of the following canonical SMILES string. Please provide explanations
for your decision-making process and provide the final answer in square
brackets."}, {"role": "user", "content":
"N[C@@H](Cc1ccc(O)cc1)C(=O)O"}], "ideal": "[C9H11NO3]"}
{"input": [{"role": "system", "content": "Tell me the molecular formula
of the following canonical SMILES string. Please provide explanations
for your decision-making process and provide the final answer in square
brackets."}, {"role": "user", "content": "CC(C)C[C@H](N)C(=O)O"}],
"ideal": "[C6H13NO2]"}
{"input": [{"role": "system", "content": "Tell me the molecular formula
of the following canonical SMILES string. Please provide explanations
for your decision-making process and provide the final answer in square
brackets."}, {"role": "user", "content":
"N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O"}], "ideal": "[C11H12N2O2]"}
{"input": [{"role": "system", "content": "Tell me the molecular formula
of the following canonical SMILES string. Please provide explanations
for your decision-making process and provide the final answer in square
brackets."}, {"role": "user", "content": "CCCCCCC(O)CCCCCCCCCCC(=O)O"}],
"ideal": "[C18H36O3]"}
{"input": [{"role": "system", "content": "Tell me the molecular formula
of the following canonical SMILES string. Please provide explanations
for your decision-making process and provide the final answer in square
brackets."}, {"role": "user", "content": "NCC1(CC(=O)O)CCCCC1"}],
"ideal": "[C9H17NO2]"}
  ```
</details>

---
## [openai/evals](https://github.com/openai/evals)@[fd65012b46...](https://github.com/openai/evals/commit/fd65012b46c9f4d6f97f0064b3d34087dc1747b6)
#### Tuesday 2023-07-04 02:13:02 by Anthony DiMaggio

[Eval] Add NER for finance (#1255)

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

NER for finance

### Eval description

Named entity recognition (NER) over financial documents.

### What makes this a useful eval?

Named entity recognition is used in many fields for document
understanding and extraction. In finance, NER can be particularly tricky
since financial documents often involve complex interactions between
several entities. Enhanced NER capabilities in finance can be very
useful to improve news analysis, risk assessments, and much more. This
PR was partly motivated by [Bloomberg
GPT](https://arxiv.org/abs/2303.17564) and the data comes from a [2015
paper](https://aclanthology.org/U15-1010.pdf).

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
{"input": [{"role": "system", "content": "The following sentence is from
a financial document. List the named entities in the order they appear.
If an entity appears multiple times, list it once for each time it
appears. Think step by step first and then state your final answer as a
comma-separated list enclosed in brackets with the format [NAME - TYPE,
NAME - TYPE, NAME - TYPE]. Entity types can be PERSON, ORGANIZATION, or
LOCATION. If there are no entities found, state 'No entities found'."},
{"role": "user", "content": "( a ) To obtain an Equipment Advance ,
Borrower will deliver to Bank a completed supplement in substantially
the form attached (\" Loan Supplement \"), together with invoices and
such additional information as Bank may request at least five ( 5 )
Business Days before the proposed funding date ( the \" Funding Date
\")."}], "ideal": "[Borrower - PERSON, Bank - ORGANIZATION, Bank -
ORGANIZATION]"}
{"input": [{"role": "system", "content": "The following sentence is from
a financial document. List the named entities in the order they appear.
If an entity appears multiple times, list it once for each time it
appears. Think step by step first and then state your final answer as a
comma-separated list enclosed in brackets with the format [NAME - TYPE,
NAME - TYPE, NAME - TYPE]. Entity types can be PERSON, ORGANIZATION, or
LOCATION. If there are no entities found, state 'No entities found'."},
{"role": "user", "content": "On each Funding Date , Bank will specify in
the Loan Supplement for each Equipment Advance , the Basic Rate , the
Loan Factor , the Payment Dates , and a table of Stipulated Loan Values
, together with a UCC Financing Statement covering the Equipment
described on the Loan Supplement ."}], "ideal": "[Bank - ORGANIZATION]"}
{"input": [{"role": "system", "content": "The following sentence is from
a financial document. List the named entities in the order they appear.
If an entity appears multiple times, list it once for each time it
appears. Think step by step first and then state your final answer as a
comma-separated list enclosed in brackets with the format [NAME - TYPE,
NAME - TYPE, NAME - TYPE]. Entity types can be PERSON, ORGANIZATION, or
LOCATION. If there are no entities found, state 'No entities found'."},
{"role": "user", "content": "If Borrower satisfies the conditions of
each Equipment Advance specified from time to time by Bank , Bank will
disburse such Equipment Advance by internal transfer to Borrower ' s
deposit account with Bank ."}], "ideal": "[Borrower - PERSON, Bank -
ORGANIZATION, Bank - ORGANIZATION, Borrower - PERSON, Bank -
ORGANIZATION]"}
{"input": [{"role": "system", "content": "The following sentence is from
a financial document. List the named entities in the order they appear.
If an entity appears multiple times, list it once for each time it
appears. Think step by step first and then state your final answer as a
comma-separated list enclosed in brackets with the format [NAME - TYPE,
NAME - TYPE, NAME - TYPE]. Entity types can be PERSON, ORGANIZATION, or
LOCATION. If there are no entities found, state 'No entities found'."},
{"role": "user", "content": "( b ) Bank ' s obligation to lend the
undisbursed portion of the Committed Equipment Line will terminate if ,
in Bank ' s sole discretion , there has been a material adverse change
in the general affairs , management , results of operation , condition (
financial or otherwise ) or the prospects of Borrower , whether or not
arising from transactions in the ordinary course of business , or there
has been material adverse deviation by Borrower from the most recent
business plan of Borrower presented to and accepted by Bank prior to the
execution of this Agreement ."}], "ideal": "[Bank - ORGANIZATION, Bank -
ORGANIZATION, Borrower - PERSON, Borrower - PERSON, Borrower - PERSON,
Bank - ORGANIZATION]"}
{"input": [{"role": "system", "content": "The following sentence is from
a financial document. List the named entities in the order they appear.
If an entity appears multiple times, list it once for each time it
appears. Think step by step first and then state your final answer as a
comma-separated list enclosed in brackets with the format [NAME - TYPE,
NAME - TYPE, NAME - TYPE]. Entity types can be PERSON, ORGANIZATION, or
LOCATION. If there are no entities found, state 'No entities found'."},
{"role": "user", "content": "4 < PAGE > 5 2 . 2 INTEREST RATE , PAYMENTS
."}], "ideal": "No entities found"}
{"input": [{"role": "system", "content": "The following sentence is from
a financial document. List the named entities in the order they appear.
If an entity appears multiple times, list it once for each time it
appears. Think step by step first and then state your final answer as a
comma-separated list enclosed in brackets with the format [NAME - TYPE,
NAME - TYPE, NAME - TYPE]. Entity types can be PERSON, ORGANIZATION, or
LOCATION. If there are no entities found, state 'No entities found'."},
{"role": "user", "content": "( a ) Principal and Interest Payments On
Payment Dates ."}], "ideal": "No entities found"}
{"input": [{"role": "system", "content": "The following sentence is from
a financial document. List the named entities in the order they appear.
If an entity appears multiple times, list it once for each time it
appears. Think step by step first and then state your final answer as a
comma-separated list enclosed in brackets with the format [NAME - TYPE,
NAME - TYPE, NAME - TYPE]. Entity types can be PERSON, ORGANIZATION, or
LOCATION. If there are no entities found, state 'No entities found'."},
{"role": "user", "content": "Borrower will make payments monthly in
advance of principal and accrued interest for each Equipment Advance (
collectively , \" Scheduled Payments \"), on the first Business Day of
the month following the Funding Date ( or commencing on the Funding Date
if the Funding Date is the first Business Day of the month ) with
respect to such Equipment Advance and continuing thereafter during the
Repayment Period on the first Business Day of each calendar month ( each
a \" Payment Date \"), in an amount equal to the Loan Factor multiplied
by the Loan Amount for such Equipment Advance as of such Payment Date
."}], "ideal": "[Borrower - PERSON]"}
{"input": [{"role": "system", "content": "The following sentence is from
a financial document. List the named entities in the order they appear.
If an entity appears multiple times, list it once for each time it
appears. Think step by step first and then state your final answer as a
comma-separated list enclosed in brackets with the format [NAME - TYPE,
NAME - TYPE, NAME - TYPE]. Entity types can be PERSON, ORGANIZATION, or
LOCATION. If there are no entities found, state 'No entities found'."},
{"role": "user", "content": "All unpaid principal and accrued interest
is due and payable in full on the last Payment Date with respect to such
Equipment Advance ."}], "ideal": "No entities found"}
{"input": [{"role": "system", "content": "The following sentence is from
a financial document. List the named entities in the order they appear.
If an entity appears multiple times, list it once for each time it
appears. Think step by step first and then state your final answer as a
comma-separated list enclosed in brackets with the format [NAME - TYPE,
NAME - TYPE, NAME - TYPE]. Entity types can be PERSON, ORGANIZATION, or
LOCATION. If there are no entities found, state 'No entities found'."},
{"role": "user", "content": "An Equipment Advance may be prepaid only
upon payment of a prepayment premium specified by Bank ."}], "ideal":
"[Bank - ORGANIZATION]"}
{"input": [{"role": "system", "content": "The following sentence is from
a financial document. List the named entities in the order they appear.
If an entity appears multiple times, list it once for each time it
appears. Think step by step first and then state your final answer as a
comma-separated list enclosed in brackets with the format [NAME - TYPE,
NAME - TYPE, NAME - TYPE]. Entity types can be PERSON, ORGANIZATION, or
LOCATION. If there are no entities found, state 'No entities found'."},
{"role": "user", "content": "( b ) Interest Rate ."}], "ideal": "No
entities found"}
  ```
</details>

---
## [openai/evals](https://github.com/openai/evals)@[c6acec3767...](https://github.com/openai/evals/commit/c6acec37675ee3b4dba8a9ab8d87ceeef6af1962)
#### Tuesday 2023-07-04 02:13:14 by Zhou Guanghui

[Eval]Identify the author and title of Chinese modern poem (#1256)

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

Identify the author and title of Chinese modern poem

### Eval description

Given the famous sentences from Chinese modern poems, return its author
and title.

### What makes this a useful eval?

Modern Chinese poetry, including New poetry (新诗), refers to post Qing
dynasty(1644 to 1912), including the modern vernacular (baihua) style of
poetry increasingly common with the New Culture movements, with the
development of experimental styles such as "free verse" (as opposed to
the traditional Chinese poetry written in Classical Chinese language);
but, also including twentieth and twenty-first century continuations or
revivals of Classical Chinese poetry forms. Currently, Both of GPT-3.5
and GPT-4 models can only give correct author and title to only a few of
the more well-known content in Chinese modern poems, and the rest are
returned randomly.

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

All the poems in this eval are random picked from 中国现代诗歌名篇赏 published by
Guangming RiBao Publishing House in 2010, 中国现代诗歌选 published by people's
Literature Publishing House in 2018, and other poets' albums. All the
poems are double-checked against Google search result to make sure we
have put in the right author and title for each poem.

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

{"input":[{"role":"user","content":"下面这段内容出自哪位中国现当代作家的哪一部诗歌作品？请只回复作家姓名和作品名称，不要包含其他内容。例如：徐志摩《再别康桥》\n---\n轻轻的我走了，正如我轻轻的来；我轻轻的招手，作别西天的云彩。"}],"ideal":"徐志摩《再别康桥》"}

{"input":[{"role":"user","content":"下面这段内容出自哪位中国现当代作家的哪一部诗歌作品？请只回复作家姓名和作品名称，不要包含其他内容。例如：徐志摩《再别康桥》\n---\n我不知道风
是在哪一个方向吹——我是在梦中，在梦的轻波里依洄。"}],"ideal":"徐志摩《我不知道风是在哪一个方向吹》"}

{"input":[{"role":"user","content":"下面这段内容出自哪位中国现当代作家的哪一部诗歌作品？请只回复作家姓名和作品名称，不要包含其他内容。例如：徐志摩《再别康桥》\n---\n我是天空里的一片云，偶尔投影在你的波心。你不必讶异，更无须欢喜，在转瞬间消灭了踪影。"}],"ideal":"徐志摩《偶然》"}

{"input":[{"role":"user","content":"下面这段内容出自哪位中国现当代作家的哪一部诗歌作品？请只回复作家姓名和作品名称，不要包含其他内容。例如：徐志摩《再别康桥》\n---\n黑夜给了我黑色的眼睛，我却用它寻找光明。"}],"ideal":"顾城《一代人》"}

{"input":[{"role":"user","content":"下面这段内容出自哪位中国现当代作家的哪一部诗歌作品？请只回复作家姓名和作品名称，不要包含其他内容。例如：徐志摩《再别康桥》\n---\n你，一会儿看我，一会儿看云。我觉得，你看我时很远，你看云时很近。"}],"ideal":"顾城《远和近》"}
  ```
</details>

---
## [openai/evals](https://github.com/openai/evals)@[534d6b5014...](https://github.com/openai/evals/commit/534d6b50146d301794c77e116ea345f8878657c2)
#### Tuesday 2023-07-04 02:14:59 by Lance Miyamoto

[Eval] Identify Dhammapada Pali reference (#1261)

## Eval details 📑

### Eval name

dhammapada-reference

### Eval description

Given a snippet of a Dhammapada verse in Pali, identify who the Buddha
was referencing in that verse.

### What makes this a useful eval?

> The Dhammapada is a collection of sayings of the Buddha in verse form
and one of the most widely read and best known Buddhist scriptures.
[Dhammapada—Wikipedia](https://en.wikipedia.org/wiki/Dhammapada)

This ancient Buddhist text is not explicit about who the Buddha is
referencing in each of these 423 verses. Yet, behind every verse (and
behind every hidden reference) is a parable--that once understood, adds
much more meaning and clarity to these spoken words. These references
are found in other parts of the Pali Canon, such as the Commentarial
section.

Currently, GPT-3.5 has trouble identifying and referencing Pali verses
from the Dhammapada.


![dhammapada-reference-eval](https://github.com/openai/evals/assets/81899308/6f23420c-e08d-4882-b76c-a9793c18f2fc)

Also, I stumbled upon this issue when personally using ChatGPT-3.5 and
-4 to study the Pali Canon, including the Dhammapada. But I found the
models hallucinating answers, even fabricating verses.

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

All Dhammapada verses in this eval are randomly picked from _A
Comparative Edition of the Dhammapada_ by Ānandajoti Bhikkhu (as sourced
in Wikipedia). I made one spelling update in the verse "sabbattha ve
sappurisā **vajanti**" to "sabbattha ve sappurisā **cajanti**" as I
noticed more sources referenced that spelling instead. All the verses
and references were cross-checked with the sources below to ensure the
correct information is provided.

Here are the sources used:

- [_Comparative Edition of the Dhammapada_ by Ānandajoti
Bhikkhu](https://www.ancient-buddhist-texts.net/Buddhist-Texts/C3-Comparative-Dhammapada/index.htm)
- [_Dhammapada (Illustrated)_ by Ven.
Thero](https://www.wisdomlib.org/buddhism/book/dhammapada-illustrated)
- [Digital Pali
Reader](https://www.digitalpalireader.online/_dprhtml/index.html)
- [_The Dhammapada: Verses and Stories_ by Daw Mya Tin,
M.A.](https://www.tipitaka.net/tipitaka/dhp/)

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
{"input": [{"role": "system", "content": "You're a Pali scholar. The
user is studying the Dhammapada and provides a snippet of Pali verse
from the ancient Buddhist text. The user asks, \u201cWho is the Buddha
referencing when speaking these words?\u201d Before answering, analyze
and match this snippet to the complete verse. Once matched, identify
only the name of the person who the Buddha is referencing in that verse;
or, if the reference is nameless, identify only a concise Pali
description that scholars traditionally use as the reference (e.g.,
farmer, young bride, thirty monks, etc.). Please provide your reasoning
step-by-step. Then, write your final answer in Pali without
capitalizations and enclosed in square brackets. For example, if your
final answer is the name Vis\u0101kh\u0101, then write
[vis\u0101kh\u0101] after providing your step-by-step reasoning; or, if
your final answer is the nameless reference \"farmer\" (which translates
to \"kassaka\" in Pali), then write [kassaka] after providing your
step-by-step reasoning."}, {"role": "user", "content": "pa\u1e6dhavisamo
no virujjhati indakh\u012bl\u016bpamo t\u0101di subbato"}], "ideal":
"[s\u0101riputta]"}
{"input": [{"role": "system", "content": "You're a Pali scholar. The
user is studying the Dhammapada and provides a snippet of Pali verse
from the ancient Buddhist text. The user asks, \u201cWho is the Buddha
referencing when speaking these words?\u201d Before answering, analyze
and match this snippet to the complete verse. Once matched, identify
only the name of the person who the Buddha is referencing in that verse;
or, if the reference is nameless, identify only a concise Pali
description that scholars traditionally use as the reference (e.g.,
farmer, young bride, thirty monks, etc.). Please provide your reasoning
step-by-step. Then, write your final answer in Pali without
capitalizations and enclosed in square brackets. For example, if your
final answer is the name Vis\u0101kh\u0101, then write
[vis\u0101kh\u0101] after providing your step-by-step reasoning; or, if
your final answer is the nameless reference \"farmer\" (which translates
to \"kassaka\" in Pali), then write [kassaka] after providing your
step-by-step reasoning."}, {"role": "user", "content": "andhabh\u016bto
aya\u1e41 loko tanukettha vipassati"}], "ideal":
"[pesak\u0101radh\u012btara\u1e41]"}
{"input": [{"role": "system", "content": "You're a Pali scholar. The
user is studying the Dhammapada and provides a snippet of Pali verse
from the ancient Buddhist text. The user asks, \u201cWho is the Buddha
referencing when speaking these words?\u201d Before answering, analyze
and match this snippet to the complete verse. Once matched, identify
only the name of the person who the Buddha is referencing in that verse;
or, if the reference is nameless, identify only a concise Pali
description that scholars traditionally use as the reference (e.g.,
farmer, young bride, thirty monks, etc.). Please provide your reasoning
step-by-step. Then, write your final answer in Pali without
capitalizations and enclosed in square brackets. For example, if your
final answer is the name Vis\u0101kh\u0101, then write
[vis\u0101kh\u0101] after providing your step-by-step reasoning; or, if
your final answer is the nameless reference \"farmer\" (which translates
to \"kassaka\" in Pali), then write [kassaka] after providing your
step-by-step reasoning."}, {"role": "user", "content": "yo ca
vantakas\u0101vassa s\u012blesu susam\u0101hito"}], "ideal":
"[devadatta]"}
{"input": [{"role": "system", "content": "You're a Pali scholar. The
user is studying the Dhammapada and provides a snippet of Pali verse
from the ancient Buddhist text. The user asks, \u201cWho is the Buddha
referencing when speaking these words?\u201d Before answering, analyze
and match this snippet to the complete verse. Once matched, identify
only the name of the person who the Buddha is referencing in that verse;
or, if the reference is nameless, identify only a concise Pali
description that scholars traditionally use as the reference (e.g.,
farmer, young bride, thirty monks, etc.). Please provide your reasoning
step-by-step. Then, write your final answer in Pali without
capitalizations and enclosed in square brackets. For example, if your
final answer is the name Vis\u0101kh\u0101, then write
[vis\u0101kh\u0101] after providing your step-by-step reasoning; or, if
your final answer is the nameless reference \"farmer\" (which translates
to \"kassaka\" in Pali), then write [kassaka] after providing your
step-by-step reasoning."}, {"role": "user", "content":
"samm\u0101pa\u1e47ihita\u1e41 citta\u1e41 seyyaso na\u1e41 tato
kare"}], "ideal": "[soreyya]"}
{"input": [{"role": "system", "content": "You're a Pali scholar. The
user is studying the Dhammapada and provides a snippet of Pali verse
from the ancient Buddhist text. The user asks, \u201cWho is the Buddha
referencing when speaking these words?\u201d Before answering, analyze
and match this snippet to the complete verse. Once matched, identify
only the name of the person who the Buddha is referencing in that verse;
or, if the reference is nameless, identify only a concise Pali
description that scholars traditionally use as the reference (e.g.,
farmer, young bride, thirty monks, etc.). Please provide your reasoning
step-by-step. Then, write your final answer in Pali without
capitalizations and enclosed in square brackets. For example, if your
final answer is the name Vis\u0101kh\u0101, then write
[vis\u0101kh\u0101] after providing your step-by-step reasoning; or, if
your final answer is the nameless reference \"farmer\" (which translates
to \"kassaka\" in Pali), then write [kassaka] after providing your
step-by-step reasoning."}, {"role": "user", "content": "sabbe tasanti
da\u1e47\u1e0dassa sabbe bh\u0101yanti maccuno"}], "ideal":
"[chabbaggiye bhikkh\u016b]"}
  ```
</details>

---
## [algohali3008/docs](https://github.com/algohali3008/docs)@[ba633965f4...](https://github.com/algohali3008/docs/commit/ba633965f47c8dd9f477212c074a37c4bf6a95c0)
#### Tuesday 2023-07-04 02:17:45 by algohali3008

Create Lesers30008

<body><div class="line-gutter-backdrop"></div><table><tbody><tr><td class="line-number" value="1"></td><td class="line-content"><span class="html-doctype">&lt;!DOCTYPE html</span></td></tr><tr><td class="line-number" value="2"></td><td class="line-content"><span class="html-doctype"> PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"&gt;</span><span class="html-tag">&lt;html <span class="html-attribute-name">xmlns</span>="<span class="html-attribute-value">http://www.w3.org/1999/xhtml</span>"&gt;</span><span class="html-tag">&lt;head&gt;</span><span class="html-tag">&lt;meta <span class="html-attribute-name">http-equiv</span>="<span class="html-attribute-value">Content-Type</span>" <span class="html-attribute-name">content</span>="<span class="html-attribute-value">text/html; charset=utf-8</span>" /&gt;</span><span class="html-tag">&lt;meta <span class="html-attribute-name">name</span>="<span class="html-attribute-value">viewport</span>" <span class="html-attribute-name">content</span>="<span class="html-attribute-value">width=device-width, initial-scale=1.0,shrink-to-fit=no,user-scalable=no</span>"&gt;</span><span class="html-tag">&lt;title&gt;</span>about_Shanghai Friendess Electronic Technology Co., Ltd.<span class="html-tag">&lt;/title&gt;</span><span class="html-tag">&lt;link <span class="html-attribute-name">rel</span>="<span class="html-attribute-value">icon</span>" <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-resource-link" target="_blank" href="/wp-content/themes/bcindex/assets/img/friendess.ico" rel="noreferrer noopener">/wp-content/themes/bcindex/assets/img/friendess.ico</a>" <span class="html-attribute-name">type</span>="<span class="html-attribute-value">image/x-icon</span>" /&gt;</span><span class="html-tag">&lt;meta <span class="html-attribute-name">name</span>="<span class="html-attribute-value">keywords</span>" <span class="html-attribute-name">content</span>="<span class="html-attribute-value">laser cutting, fiber laser, fscut, cypcut</span>" /&gt;</span><span class="html-tag">&lt;meta <span class="html-attribute-name">name</span>="<span class="html-attribute-value">description</span>"</span></td></tr><tr><td class="line-number" value="3"></td><td class="line-content"> <span class="html-attribute-name">content</span>="<span class="html-attribute-value">FSCUT, CypCut, CypNest, BLT laser head ... Friendess is a leading provider of laser cutting control systems and laser cutting heads. Friendess has been deeply involved in the electronics manufacturing industry for over 15 years. From a solution expert in the laser cutting industry to a promoter of industrial automation, Friendess gene of authenticity, innovation and service has never changed. </span>" /&gt;<span class="html-tag">&lt;meta <span class="html-attribute-name">http-equiv</span>="<span class="html-attribute-value">X-UA-Compatible</span>" <span class="html-attribute-name">content</span>="<span class="html-attribute-value">IE=edge,Chrome=1</span>" /&gt;</span><span class="html-tag">&lt;link <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-resource-link" target="_blank" href="/wp-content/themes/bcindex/assets/bootstrap/bootstrap-4.4.1-dist/css/bootstrap.min.css" rel="noreferrer noopener">/wp-content/themes/bcindex/assets/bootstrap/bootstrap-4.4.1-dist/css/bootstrap.min.css</a>" <span class="html-attribute-name">rel</span>="<span class="html-attribute-value">stylesheet</span>"</span></td></tr><tr><td class="line-number" value="4"></td><td class="line-content"> <span class="html-attribute-name">type</span>="<span class="html-attribute-value">text/css</span>" /&gt;<span class="html-tag">&lt;link <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-resource-link" target="_blank" href="/wp-content/themes/bcindex/assets/css/style.css?v=1688436837" rel="noreferrer noopener">/wp-content/themes/bcindex/assets/css/style.css?v=1688436837</a>" <span class="html-attribute-name">rel</span>="<span class="html-attribute-value">stylesheet</span>"</span></td></tr><tr><td class="line-number" value="5"></td><td class="line-content"> <span class="html-attribute-name">type</span>="<span class="html-attribute-value">text/css</span>" /&gt;<span class="html-tag">&lt;link <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-resource-link" target="_blank" href="/wp-content/themes/bcindex/assets/css/animate.min.css" rel="noreferrer noopener">/wp-content/themes/bcindex/assets/css/animate.min.css</a>" <span class="html-attribute-name">rel</span>="<span class="html-attribute-value">stylesheet</span>" <span class="html-attribute-name">type</span>="<span class="html-attribute-value">text/css</span>" /&gt;</span> <span class="html-tag">&lt;script <span class="html-attribute-name">type</span>="<span class="html-attribute-value">text/javascript</span>" <span class="html-attribute-name">src</span>="<a class="html-attribute-value html-resource-link" target="_blank" href="/wp-content/themes/bcindex/assets/bootstrap/jquery-3.3.1.slim.min.js" rel="noreferrer noopener">/wp-content/themes/bcindex/assets/bootstrap/jquery-3.3.1.slim.min.js</a>"&gt;</span><span class="html-tag">&lt;/script&gt;</span> <span class="html-tag">&lt;script <span class="html-attribute-name">type</span>="<span class="html-attribute-value">text/javascript</span>" <span class="html-attribute-name">src</span>="<a class="html-attribute-value html-resource-link" target="_blank" href="/wp-content/themes/bcindex/assets/js/swiper-bundle.min.js" rel="noreferrer noopener">/wp-content/themes/bcindex/assets/js/swiper-bundle.min.js</a>"&gt;</span><span class="html-tag">&lt;/script&gt;</span> <span class="html-tag">&lt;link <span class="html-attribute-name">rel</span>="<span class="html-attribute-value">stylesheet</span>" <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-resource-link" target="_blank" href="/wp-content/themes/bcindex/assets/css/swiper-bundle.min.css" rel="noreferrer noopener">/wp-content/themes/bcindex/assets/css/swiper-bundle.min.css</a>"&gt;</span>  <span class="html-tag">&lt;script <span class="html-attribute-name">async</span> <span class="html-attribute-name">src</span>="<a class="html-attribute-value html-resource-link" target="_blank" href="https://www.googletagmanager.com/gtag/js?id=G-QWQ6SEEEKY" rel="noreferrer noopener">https://www.googletagmanager.com/gtag/js?id=G-QWQ6SEEEKY</a>"&gt;</span><span class="html-tag">&lt;/script&gt;</span> <span class="html-tag">&lt;script&gt;</span>window.dataLayer = window.dataLayer || [];</td></tr><tr><td class="line-number" value="6"></td><td class="line-content">    function gtag(){dataLayer.push(arguments);}</td></tr><tr><td class="line-number" value="7"></td><td class="line-content">    gtag('js', new Date());</td></tr><tr><td class="line-number" value="8"></td><td class="line-content"><br></td></tr><tr><td class="line-number" value="9"></td><td class="line-content">    gtag('config', 'G-QWQ6SEEEKY');<span class="html-tag">&lt;/script&gt;</span>  <span class="html-tag">&lt;script&gt;</span>(function(d, w, c) {</td></tr><tr><td class="line-number" value="10"></td><td class="line-content">          w.ChatraID = '2n6GmxPnnCSCnpLba';</td></tr><tr><td class="line-number" value="11"></td><td class="line-content">          var s = d.createElement('script');</td></tr><tr><td class="line-number" value="12"></td><td class="line-content">          w[c] = w[c] || function() {</td></tr><tr><td class="line-number" value="13"></td><td class="line-content">              (w[c].q = w[c].q || []).push(arguments);</td></tr><tr><td class="line-number" value="14"></td><td class="line-content">          };</td></tr><tr><td class="line-number" value="15"></td><td class="line-content">          s.async = true;</td></tr><tr><td class="line-number" value="16"></td><td class="line-content">          s.src = 'https://call.chatra.io/chatra.js';</td></tr><tr><td class="line-number" value="17"></td><td class="line-content">          if (d.head) d.head.appendChild(s);</td></tr><tr><td class="line-number" value="18"></td><td class="line-content">      })(document, window, 'Chatra');<span class="html-tag">&lt;/script&gt;</span> <span class="html-tag">&lt;/head&gt;</span><span class="html-tag">&lt;body&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">phone-nav</span>"&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">nav-menu</span>"&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">m-nav-top</span>"&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="/en" rel="noreferrer noopener">/en</a>" <span class="html-attribute-name">class</span>="<span class="html-attribute-value">m-icon-a</span>"&gt;</span> <span class="html-tag">&lt;img <span class="html-attribute-name">src</span>="<a class="html-attribute-value html-resource-link" target="_blank" href="/wp-content/themes/bcindex/assets/img/shouye/aboutus.png" rel="noreferrer noopener">/wp-content/themes/bcindex/assets/img/shouye/aboutus.png</a>" <span class="html-attribute-name">alt</span>="" <span class="html-attribute-name">class</span>="<span class="html-attribute-value">m-icon</span>"&gt;</span> <span class="html-tag">&lt;/a&gt;</span> <span class="html-tag">&lt;img <span class="html-attribute-name">src</span>="<a class="html-attribute-value html-resource-link" target="_blank" href="/wp-content/themes/bcindex/assets/img/shouye/close.png" rel="noreferrer noopener">/wp-content/themes/bcindex/assets/img/shouye/close.png</a>" <span class="html-attribute-name">alt</span>="" <span class="html-attribute-name">class</span>="<span class="html-attribute-value">m-close</span>"&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;ul <span class="html-attribute-name">class</span>="<span class="html-attribute-value">m-ul</span>"&gt;</span><span class="html-tag">&lt;li&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">m-li</span>"&gt;</span> <span class="html-tag">&lt;input <span class="html-attribute-name">class</span>="<span class="html-attribute-value">search-en</span>" <span class="html-attribute-name">name</span>="<span class="html-attribute-value">s</span>" <span class="html-attribute-name">id</span>="<span class="html-attribute-value">s</span>" <span class="html-attribute-name">type</span>="<span class="html-attribute-value">text</span>" <span class="html-attribute-name">placeholder</span>="<span class="html-attribute-value">search</span>"</span></td></tr><tr><td class="line-number" value="19"></td><td class="line-content"> <span class="html-attribute-name">style</span>="<span class="html-attribute-value">color:#fff;height:40px;background-color:#1e3d76;border:none;outline:none;</span>"&gt; <span class="html-tag">&lt;img <span class="html-attribute-name">src</span>="<a class="html-attribute-value html-resource-link" target="_blank" href="/wp-content/themes/bcindex/assets/img/index/search-w.svg" rel="noreferrer noopener">/wp-content/themes/bcindex/assets/img/index/search-w.svg</a>" <span class="html-attribute-name">alt</span>=""&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;li&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">m-li m-li1</span>"&gt;</span> <span class="html-tag">&lt;span&gt;</span>Products<span class="html-tag">&lt;/span&gt;</span> <span class="html-tag">&lt;img <span class="html-attribute-name">src</span>="<a class="html-attribute-value html-resource-link" target="_blank" href="/wp-content/themes/bcindex/assets/img/shouye/down.svg" rel="noreferrer noopener">/wp-content/themes/bcindex/assets/img/shouye/down.svg</a>" <span class="html-attribute-name">alt</span>="" <span class="html-attribute-name">class</span>="<span class="html-attribute-value">getin</span>"&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;ul <span class="html-attribute-name">class</span>="<span class="html-attribute-value">m-li-main</span>"&gt;</span><span class="html-tag">&lt;li&gt;</span><span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="/en/product/#board-system" rel="noreferrer noopener">/en/product/#board-system</a>"&gt;</span>Laser Cutting Controller<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;li&gt;</span><span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="/en/product/#bus-system" rel="noreferrer noopener">/en/product/#bus-system</a>"&gt;</span>EtherCAT Bus Controller<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;li&gt;</span><span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="/en/product/#intelligent-hardware" rel="noreferrer noopener">/en/product/#intelligent-hardware</a>"&gt;</span>Smart Hardware<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;li&gt;</span><span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="/en/product/#follower-system" rel="noreferrer noopener">/en/product/#follower-system</a>"&gt;</span>Height Controller<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;li&gt;</span><span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="/en/product/#visual-system" rel="noreferrer noopener">/en/product/#visual-system</a>"&gt;</span>Vision System<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;li&gt;</span><span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="/en/product/#informatization-system" rel="noreferrer noopener">/en/product/#informatization-system</a>"&gt;</span>Industrial IoT<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;/ul&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;li&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">m-li m-li2</span>"&gt;</span> <span class="html-tag">&lt;span&gt;</span>Software<span class="html-tag">&lt;/span&gt;</span> <span class="html-tag">&lt;img <span class="html-attribute-name">src</span>="<a class="html-attribute-value html-resource-link" target="_blank" href="/wp-content/themes/bcindex/assets/img/shouye/down.svg" rel="noreferrer noopener">/wp-content/themes/bcindex/assets/img/shouye/down.svg</a>" <span class="html-attribute-name">alt</span>="" <span class="html-attribute-name">class</span>="<span class="html-attribute-value">getin</span>"&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;ul <span class="html-attribute-name">class</span>="<span class="html-attribute-value">m-li-main</span>"&gt;</span><span class="html-tag">&lt;li&gt;</span><span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://www.fscut.com/en/soft/my-machine/" rel="noreferrer noopener">https://www.fscut.com/en/soft/my-machine/</a>" <span class="html-attribute-name">class</span>="<span class="html-attribute-value">m-li-btn</span>"&gt;</span>My Machine<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;li&gt;</span><span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://www.fscut.com/en/soft/cypcutpro/" rel="noreferrer noopener">https://www.fscut.com/en/soft/cypcutpro/</a>" <span class="html-attribute-name">class</span>="<span class="html-attribute-value">m-li-btn</span>"&gt;</span>CypCutPro<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;li&gt;</span><span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://www.fscut.com/en/soft/hypcut/" rel="noreferrer noopener">https://www.fscut.com/en/soft/hypcut/</a>" <span class="html-attribute-name">class</span>="<span class="html-attribute-value">m-li-btn</span>"&gt;</span>HypCut<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;li&gt;</span><span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://www.fscut.com/en/soft/cypcute/" rel="noreferrer noopener">https://www.fscut.com/en/soft/cypcute/</a>" <span class="html-attribute-name">class</span>="<span class="html-attribute-value">m-li-btn</span>"&gt;</span>CypCutE<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;li&gt;</span><span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://www.fscut.com/en/soft/tubest-lite/" rel="noreferrer noopener">https://www.fscut.com/en/soft/tubest-lite/</a>" <span class="html-attribute-name">class</span>="<span class="html-attribute-value">m-li-btn</span>"&gt;</span>TubesT-Lite<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;li&gt;</span><span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://www.fscut.com/en/soft/tubepro/" rel="noreferrer noopener">https://www.fscut.com/en/soft/tubepro/</a>" <span class="html-attribute-name">class</span>="<span class="html-attribute-value">m-li-btn</span>"&gt;</span>TubePro<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;li&gt;</span><span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://www.fscut.com/en/soft/cypone/" rel="noreferrer noopener">https://www.fscut.com/en/soft/cypone/</a>" <span class="html-attribute-name">class</span>="<span class="html-attribute-value">m-li-btn</span>"&gt;</span>CypOne<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;li&gt;</span><span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://www.fscut.com/en/soft/cypcut/" rel="noreferrer noopener">https://www.fscut.com/en/soft/cypcut/</a>" <span class="html-attribute-name">class</span>="<span class="html-attribute-value">m-li-btn</span>"&gt;</span>CypCut<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;li&gt;</span><span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://www.fscut.com/en/soft/tubest/" rel="noreferrer noopener">https://www.fscut.com/en/soft/tubest/</a>" <span class="html-attribute-name">class</span>="<span class="html-attribute-value">m-li-btn</span>"&gt;</span>TubesT<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;li&gt;</span><span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://www.fscut.com/en/soft/cypnest/" rel="noreferrer noopener">https://www.fscut.com/en/soft/cypnest/</a>" <span class="html-attribute-name">class</span>="<span class="html-attribute-value">m-li-btn</span>"&gt;</span>CypNest<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;/ul&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;li&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">class</span>="<span class="html-attribute-value">m-li m-li4</span>" <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="http://go.fscut.com/mplink/?id=4" rel="noreferrer noopener">http://go.fscut.com/mplink/?id=4</a>" <span class="html-attribute-name">target</span>="<span class="html-attribute-value">_blank</span>"&gt;</span> <span class="html-tag">&lt;span&gt;</span>Online Mall<span class="html-tag">&lt;/span&gt;</span> <span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;li&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">class</span>="<span class="html-attribute-value">m-li m-li4</span>" <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="/about/" rel="noreferrer noopener">/about/</a>"&gt;</span> <span class="html-tag">&lt;span&gt;</span>About us<span class="html-tag">&lt;/span&gt;</span> <span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;li&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">class</span>="<span class="html-attribute-value">m-li m-li6</span>" <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="/en/soft/" rel="noreferrer noopener">/en/soft/</a>"&gt;</span> <span class="html-tag">&lt;span&gt;</span>Download<span class="html-tag">&lt;/span&gt;</span> <span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;li&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">class</span>="<span class="html-attribute-value">m-li m-li7</span>" <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="/contact/" rel="noreferrer noopener">/contact/</a>"&gt;</span> <span class="html-tag">&lt;span&gt;</span>Contact us<span class="html-tag">&lt;/span&gt;</span> <span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;/ul&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;header&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">container-fluid</span>"&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">row head no-gutters</span>"&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">d-flex d-sm-none menus col-3</span>"&gt;</span> <span class="html-tag">&lt;img <span class="html-attribute-name">src</span>="<a class="html-attribute-value html-resource-link" target="_blank" href="/wp-content/themes/bcindex/assets/img/shouye/menu.png" rel="noreferrer noopener">/wp-content/themes/bcindex/assets/img/shouye/menu.png</a>" <span class="html-attribute-name">alt</span>="" <span class="html-attribute-name">class</span>="<span class="html-attribute-value">menu</span>"&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">col-6 col-sm-2 head-left </span>"&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="/en/" rel="noreferrer noopener">/en/</a>" <span class="html-attribute-name">class</span>="<span class="html-attribute-value">head-img1</span>"&gt;</span> <span class="html-tag">&lt;img <span class="html-attribute-name">src</span>="<a class="html-attribute-value html-resource-link" target="_blank" href="/wp-content/themes/bcindex/assets/img/shouye/01.svg" rel="noreferrer noopener">/wp-content/themes/bcindex/assets/img/shouye/01.svg</a>" <span class="html-attribute-name">alt</span>="" <span class="html-attribute-name">class</span>="<span class="html-attribute-value">img-a</span>"&gt;</span> <span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">col-sm-8 d-none d-sm-block head-ul-ch</span>"&gt;</span><span class="html-tag">&lt;ul <span class="html-attribute-name">class</span>="<span class="html-attribute-value">head-ul</span>"&gt;</span><span class="html-tag">&lt;li&gt;</span><span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="/en/" rel="noreferrer noopener">/en/</a>"&gt;</span>Home<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;li <span class="html-attribute-name">class</span>="<span class="html-attribute-value">nav-show</span>"&gt;</span><span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="/en/product/" rel="noreferrer noopener">/en/product/</a>" <span class="html-attribute-name">class</span>="<span class="html-attribute-value">nav-show1</span>"&gt;</span>Products<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;li <span class="html-attribute-name">class</span>="<span class="html-attribute-value">nav-show</span>"&gt;</span><span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="/en/soft/" rel="noreferrer noopener">/en/soft/</a>" <span class="html-attribute-name">class</span>="<span class="html-attribute-value">nav-show2</span>"&gt;</span>Software<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;li&gt;</span><span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://emart.fscut.com/emart/buy.aspx" rel="noreferrer noopener">https://emart.fscut.com/emart/buy.aspx</a>" <span class="html-attribute-name">target</span>="<span class="html-attribute-value">_blank</span>"&gt;</span>Online Mall<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;li&gt;</span><span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="/news-en/" rel="noreferrer noopener">/news-en/</a>"&gt;</span>News<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;li&gt;</span><span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="/about/" rel="noreferrer noopener">/about/</a>"&gt;</span>About Us<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">head-ul-list head-ul-list1</span>"&gt;</span><span class="html-tag">&lt;div&gt;</span><span class="html-tag">&lt;div&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="/en/product/#board-system" rel="noreferrer noopener">/en/product/#board-system</a>"&gt;</span>Laser Cutting Controller<span class="html-tag">&lt;/a&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://www.fscut.com/en/product/fscut1000/" rel="noreferrer noopener">https://www.fscut.com/en/product/fscut1000/</a>"&gt;</span>FSCUT1000<span class="html-tag">&lt;/a&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://www.fscut.com/en/product/fscut3000s/" rel="noreferrer noopener">https://www.fscut.com/en/product/fscut3000s/</a>"&gt;</span>FSCUT3000<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;div&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="/en/product/#bus-system" rel="noreferrer noopener">/en/product/#bus-system</a>"&gt;</span>EtherCAT Bus Controller<span class="html-tag">&lt;/a&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://www.fscut.com/en/product/fscut2000/" rel="noreferrer noopener">https://www.fscut.com/en/product/fscut2000/</a>"&gt;</span>FSCUT2000E<span class="html-tag">&lt;/a&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://www.fscut.com/en/product/fscut4000/" rel="noreferrer noopener">https://www.fscut.com/en/product/fscut4000/</a>"&gt;</span>FSCUT4000E<span class="html-tag">&lt;/a&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://www.fscut.com/en/product/fscut5000/" rel="noreferrer noopener">https://www.fscut.com/en/product/fscut5000/</a>"&gt;</span>FSCUT5000<span class="html-tag">&lt;/a&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://www.fscut.com/en/product/fscut6000/" rel="noreferrer noopener">https://www.fscut.com/en/product/fscut6000/</a>"&gt;</span>FSCUT6000<span class="html-tag">&lt;/a&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://www.fscut.com/en/product/fscut7000/" rel="noreferrer noopener">https://www.fscut.com/en/product/fscut7000/</a>"&gt;</span>FSCUT7000<span class="html-tag">&lt;/a&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://www.fscut.com/en/product/fscut8000/" rel="noreferrer noopener">https://www.fscut.com/en/product/fscut8000/</a>"&gt;</span>FSCUT8000<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;div&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="/en/product/#intelligent-hardware" rel="noreferrer noopener">/en/product/#intelligent-hardware</a>"&gt;</span>Height Controller<span class="html-tag">&lt;/a&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://www.fscut.com/en/product/bcs100/" rel="noreferrer noopener">https://www.fscut.com/en/product/bcs100/</a>"&gt;</span>BCS100<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;div&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="/en/product/#intelligent-hardware" rel="noreferrer noopener">/en/product/#intelligent-hardware</a>"&gt;</span>Smart Hardware<span class="html-tag">&lt;/a&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://www.fscut.com/en/product/blt-4-series/" rel="noreferrer noopener">https://www.fscut.com/en/product/blt-4-series/</a>"&gt;</span>BLT 4 Series<span class="html-tag">&lt;/a&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://www.fscut.com/en/product/blt-5-series/" rel="noreferrer noopener">https://www.fscut.com/en/product/blt-5-series/</a>"&gt;</span>BLT 5 Series<span class="html-tag">&lt;/a&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://www.fscut.com/en/product/blt-6-series/" rel="noreferrer noopener">https://www.fscut.com/en/product/blt-6-series/</a>"&gt;</span>BLT 6 Series<span class="html-tag">&lt;/a&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://www.fscut.com/en/product/bmh510/" rel="noreferrer noopener">https://www.fscut.com/en/product/bmh510/</a>"&gt;</span>BMH510<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;div&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="/en/product/#visual-system" rel="noreferrer noopener">/en/product/#visual-system</a>"&gt;</span>Vision System<span class="html-tag">&lt;/a&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://www.fscut.com/en/product/cypvision/?app=true" rel="noreferrer noopener">https://www.fscut.com/en/product/cypvision/?app=true</a>"&gt;</span>CypViSion<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;div&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="/en/product/#visual-system" rel="noreferrer noopener">/en/product/#visual-system</a>"&gt;</span>Accessories<span class="html-tag">&lt;/a&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://www.fscut.com/en/product/bcl0810e-bcl4508e/" rel="noreferrer noopener">https://www.fscut.com/en/product/bcl0810e-bcl4508e/</a>"&gt;</span>BCL0810E/BCL4508E<span class="html-tag">&lt;/a&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://www.fscut.com/en/product/bcl1501a-1501b/" rel="noreferrer noopener">https://www.fscut.com/en/product/bcl1501a-1501b/</a>"&gt;</span>BCL1501A/1501B<span class="html-tag">&lt;/a&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://www.fscut.com/en/product/bcl4516e-bcl4516/" rel="noreferrer noopener">https://www.fscut.com/en/product/bcl4516e-bcl4516/</a>"&gt;</span>BCL4516E/BCL4516<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">head-ul-list head-ul-list2</span>"&gt;</span><span class="html-tag">&lt;div&gt;</span><span class="html-tag">&lt;div&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="/en/soft/#planeSoftware" rel="noreferrer noopener">/en/soft/#planeSoftware</a>"&gt;</span>2D Cutting<span class="html-tag">&lt;/a&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://www.fscut.com/en/soft/cypcut/" rel="noreferrer noopener">https://www.fscut.com/en/soft/cypcut/</a>"&gt;</span>CypCut<span class="html-tag">&lt;/a&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://www.fscut.com/en/soft/cypcute/" rel="noreferrer noopener">https://www.fscut.com/en/soft/cypcute/</a>"&gt;</span>CypCutE<span class="html-tag">&lt;/a&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://www.fscut.com/en/soft/cypcutpro/" rel="noreferrer noopener">https://www.fscut.com/en/soft/cypcutpro/</a>"&gt;</span>CypCutPro<span class="html-tag">&lt;/a&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://www.fscut.com/en/soft/cypnest/" rel="noreferrer noopener">https://www.fscut.com/en/soft/cypnest/</a>"&gt;</span>CypNest<span class="html-tag">&lt;/a&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://www.fscut.com/en/soft/cypone/" rel="noreferrer noopener">https://www.fscut.com/en/soft/cypone/</a>"&gt;</span>CypOne<span class="html-tag">&lt;/a&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://www.fscut.com/en/soft/hypcut/" rel="noreferrer noopener">https://www.fscut.com/en/soft/hypcut/</a>"&gt;</span>HypCut<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;div&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="/en/soft/#3DSoftware" rel="noreferrer noopener">/en/soft/#3DSoftware</a>"&gt;</span>3D Cutting<span class="html-tag">&lt;/a&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://www.fscut.com/en/soft/tubepro/" rel="noreferrer noopener">https://www.fscut.com/en/soft/tubepro/</a>"&gt;</span>TubePro<span class="html-tag">&lt;/a&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://www.fscut.com/en/soft/tubest/" rel="noreferrer noopener">https://www.fscut.com/en/soft/tubest/</a>"&gt;</span>TubesT<span class="html-tag">&lt;/a&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://www.fscut.com/en/soft/tubest-lite/" rel="noreferrer noopener">https://www.fscut.com/en/soft/tubest-lite/</a>"&gt;</span>TubesT-Lite<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">style</span>="<span class="html-attribute-value">width:250px;flex:3;</span>" <span class="html-attribute-name">class</span>="<span class="html-attribute-value">img-2</span>"&gt;</span> <span class="html-tag">&lt;img <span class="html-attribute-name">src</span>="<a class="html-attribute-value html-resource-link" target="_blank" href="/wp-content/themes/bcindex/assets/img/index/list2.png" rel="noreferrer noopener">/wp-content/themes/bcindex/assets/img/index/list2.png</a>" <span class="html-attribute-name">alt</span>=""&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;/ul&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">col-3 col-sm-2 head-right</span>"&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">head-search</span>"&gt;</span> <span class="html-tag">&lt;img <span class="html-attribute-name">src</span>="<a class="html-attribute-value html-resource-link" target="_blank" href="/wp-content/themes/bcindex/assets/img/shouye/05.png" rel="noreferrer noopener">/wp-content/themes/bcindex/assets/img/shouye/05.png</a>" <span class="html-attribute-name">alt</span>="" <span class="html-attribute-name">class</span>="<span class="html-attribute-value">head-img2</span>"&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">head-lang</span>"&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">search-input-index</span>"&gt;</span><span class="html-tag">&lt;div&gt;</span> <span class="html-tag">&lt;input <span class="html-attribute-name">class</span>="<span class="html-attribute-value">search-en</span>" <span class="html-attribute-name">name</span>="<span class="html-attribute-value">s</span>" <span class="html-attribute-name">id</span>="<span class="html-attribute-value">s</span>" <span class="html-attribute-name">type</span>="<span class="html-attribute-value">text</span>" <span class="html-attribute-name">placeholder</span>="<span class="html-attribute-value">Please enter key words</span>"</span></td></tr><tr><td class="line-number" value="20"></td><td class="line-content"> <span class="html-attribute-name">style</span>="<span class="html-attribute-value">width:170px;</span>"&gt; <span class="html-tag">&lt;input <span class="html-attribute-name">type</span>="<span class="html-attribute-value">submit</span>" <span class="html-attribute-name">class</span>="<span class="html-attribute-value">search-submit search-submit-en</span>" <span class="html-attribute-name">value</span>=""&gt;</span><span class="html-tag">&lt;/div&gt;</span> <span class="html-tag">&lt;img <span class="html-attribute-name">src</span>="<a class="html-attribute-value html-resource-link" target="_blank" href="/wp-content/themes/bcindex/assets/img/index/del.svg" rel="noreferrer noopener">/wp-content/themes/bcindex/assets/img/index/del.svg</a>" <span class="html-attribute-name">alt</span>="" <span class="html-attribute-name">class</span>="<span class="html-attribute-value">search-del</span>"&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">d-none d-sm-block</span>"&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="https://www.youtube.com/channel/UC7s2-jU8U3x3S8ew_pWk3Tg" rel="noreferrer noopener">https://www.youtube.com/channel/UC7s2-jU8U3x3S8ew_pWk3Tg</a>" <span class="html-attribute-name">target</span>="<span class="html-attribute-value">_blank</span>" <span class="html-attribute-name">style</span>="<span class="html-attribute-value">border-left:none;padding-right: 10px;margin-right:0;</span>" <span class="html-attribute-name">class</span>="<span class="html-attribute-value">Catalog</span>"&gt;</span>YouTube<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;div&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="/catalog" rel="noreferrer noopener">/catalog</a>" <span class="html-attribute-name">style</span>="<span class="html-attribute-value">border-left:none;padding-right: 10px;margin-left:0;</span>" <span class="html-attribute-name">class</span>="<span class="html-attribute-value">Catalog</span>"&gt;</span>Catalog<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/div&gt;</span> <span class="html-tag">&lt;img <span class="html-attribute-name">src</span>="<a class="html-attribute-value html-resource-link" target="_blank" href="/wp-content/themes/bcindex/assets/img/index/search.svg" rel="noreferrer noopener">/wp-content/themes/bcindex/assets/img/index/search.svg</a>" <span class="html-attribute-name">alt</span>="" <span class="html-attribute-name">class</span>="<span class="html-attribute-value">search-index</span>"&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="/ch" rel="noreferrer noopener">/ch</a>"&gt;</span>中文<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;/header&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">flex-box</span>"&gt;</span><span class="html-tag">&lt;section&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">container-fluid</span>"&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">row nav-img-out-h </span>"&gt;</span> <span class="html-tag">&lt;img <span class="html-attribute-name">src</span>="<a class="html-attribute-value html-resource-link" target="_blank" href="https://d.fscut.com/wordpress-fscut/2020/08/投资者关系-1.png" rel="noreferrer noopener">https://d.fscut.com/wordpress-fscut/2020/08/投资者关系-1.png</a>" <span class="html-attribute-name">alt</span>="<span class="html-attribute-value">about</span>" <span class="html-attribute-name">class</span>="<span class="html-attribute-value">prolist</span>"&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;/section&gt;</span><span class="html-tag">&lt;section <span class="html-attribute-name">class</span>="<span class="html-attribute-value">pro-list-bg</span>"&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">container</span>"&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">row</span>"&gt;</span><span class="html-tag">&lt;ul <span class="html-attribute-name">class</span>="<span class="html-attribute-value">pro-list-nav</span>"&gt;</span><span class="html-tag">&lt;li <span class="html-attribute-name">class</span>="<span class="html-attribute-value">pro-list-li tonews d-none</span>"&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="[!--news.url--]en/about/news/details/" rel="noreferrer noopener">[!--news.url--]en/about/news/details/</a>"&gt;</span>News<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;li <span class="html-attribute-name">class</span>="<span class="html-attribute-value">pro-list-li tonotices d-none</span>"&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="[!--news.url--]en/about/notices/details/" rel="noreferrer noopener">[!--news.url--]en/about/notices/details/</a>"&gt;</span>Events<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;li <span class="html-attribute-name">class</span>="<span class="html-attribute-value">pro-list-li toprogress bg-ccc </span>"&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="/about/" rel="noreferrer noopener">/about/</a>"&gt;</span>Our History<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;li <span class="html-attribute-name">class</span>="<span class="html-attribute-value">pro-list-li torecruit invisible</span>"&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="[!--news.url--]en/about/recruit/details/" rel="noreferrer noopener">[!--news.url--]en/about/recruit/details/</a>"&gt;</span>人才招聘<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;/ul&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;/section&gt;</span><span class="html-tag">&lt;section <span class="html-attribute-name">class</span>="<span class="html-attribute-value">margin-top show-all</span>" <span class="html-attribute-name">id</span>="<span class="html-attribute-value">progress</span>"&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">container</span>"&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">row no-gutters</span>"&gt;</span><span class="html-tag">&lt;p <span class="html-attribute-name">class</span>="<span class="html-attribute-value">qylc-title</span>"&gt;</span>FRIENDESS’S GROWING UP TOGETHER WITH CHINA’S LASER INDUSTRY<span class="html-tag">&lt;/p&gt;</span><span class="html-tag">&lt;p <span class="html-attribute-name">class</span>="<span class="html-attribute-value">qylc-txt</span>"&gt;</span>Founded in Zizhu National high-tech Industrial Development Park on September 11, 2007,</td></tr><tr><td class="line-number" value="21"></td><td class="line-content"> Shanghai Friendess Electronics Technology Co., Ltd. supported by Shanghai Technology Entrepreneurship Foundation</td></tr><tr><td class="line-number" value="22"></td><td class="line-content"> for Graduates and CPC Minhang Committee of Science &amp; Technology at the beginning, is a high-tech private</td></tr><tr><td class="line-number" value="23"></td><td class="line-content"> enterprise which locates at the Cangyuan Technology Park of Minhang District near SJTU and ECNU.<span class="html-tag">&lt;/p&gt;</span><span class="html-tag">&lt;p <span class="html-attribute-name">class</span>="<span class="html-attribute-value">qylc-txt</span>"&gt;</span>Since the inception, FRIENDESS is committed to the concept of independent R&amp;D, innovation and</td></tr><tr><td class="line-number" value="24"></td><td class="line-content"> pragmatism. With the deep insight into the needs and suggestions of clients, FRIENDESS has been updating its</td></tr><tr><td class="line-number" value="25"></td><td class="line-content"> products persistently, creating economic benefits with its high-tech and efficient management, and aiming to</td></tr><tr><td class="line-number" value="26"></td><td class="line-content"> become a company which provides transcendental service for clients, helps to reform China’s advanced</td></tr><tr><td class="line-number" value="27"></td><td class="line-content"> manufacturing industry and gives generous return for stakeholders.<span class="html-tag">&lt;/p&gt;</span><span class="html-tag">&lt;p <span class="html-attribute-name">class</span>="<span class="html-attribute-value">qylc-txt</span>"&gt;</span>FRIENDESS is mainly engaged in the R&amp;D of products in the field of laser-processing automation</td></tr><tr><td class="line-number" value="28"></td><td class="line-content"> and the sales of related systems. FRIENDESS focuses on the R&amp;D of laser-processing technology and relevant</td></tr><tr><td class="line-number" value="29"></td><td class="line-content"> theoretical science, and has the ability of independent R&amp;D in the computer graphics, motion control, machine</td></tr><tr><td class="line-number" value="30"></td><td class="line-content"> vision algorithm and laser material processing technique, while being the pioneer of national fibre laser</td></tr><tr><td class="line-number" value="31"></td><td class="line-content"> industry in China.<span class="html-tag">&lt;/p&gt;</span><span class="html-tag">&lt;p <span class="html-attribute-name">class</span>="<span class="html-attribute-value">qylc-txt</span>"&gt;</span>Relying on its independent R&amp;D ability, FRIENDESS has launched CypCut laser cutting control</td></tr><tr><td class="line-number" value="32"></td><td class="line-content"> software, HypCut high-power laser cutting control software, CypTube square tubes laser cutting control software,</td></tr><tr><td class="line-number" value="33"></td><td class="line-content"> the laser cutting control system of FSCUT1000/2000/3000/4000/5000/6000/8000 series, high accuracy visual</td></tr><tr><td class="line-number" value="34"></td><td class="line-content"> positioning system and integrated CNC system successively, and FRIENDESS has created operating revenues new</td></tr><tr><td class="line-number" value="35"></td><td class="line-content"> highs constantly via its R&amp;D products.<span class="html-tag">&lt;/p&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">row no-gutters</span>"&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">qylc-cards</span>"&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">qylc-card</span>"&gt;</span><span class="html-tag">&lt;p <span class="html-attribute-name">class</span>="<span class="html-attribute-value">qylc-c-t</span>"&gt;</span>Philosophy<span class="html-tag">&lt;/p&gt;</span><span class="html-tag">&lt;p <span class="html-attribute-name">class</span>="<span class="html-attribute-value">qylc-c-m</span>"&gt;</span>Client-focused, Striver-based<span class="html-tag">&lt;/p&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">qylc-card</span>"&gt;</span><span class="html-tag">&lt;p <span class="html-attribute-name">class</span>="<span class="html-attribute-value">qylc-c-t</span>"&gt;</span>Innovation<span class="html-tag">&lt;/p&gt;</span><span class="html-tag">&lt;p <span class="html-attribute-name">class</span>="<span class="html-attribute-value">qylc-c-m</span>"&gt;</span>Technology Innovation, Product Innovation, Service Innovation, Concept Innovation,</td></tr><tr><td class="line-number" value="36"></td><td class="line-content"> Management Innovation<span class="html-tag">&lt;/p&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">qylc-card</span>"&gt;</span><span class="html-tag">&lt;p <span class="html-attribute-name">class</span>="<span class="html-attribute-value">qylc-c-t</span>"&gt;</span>Core competitiveness<span class="html-tag">&lt;/p&gt;</span><span class="html-tag">&lt;p <span class="html-attribute-name">class</span>="<span class="html-attribute-value">qylc-c-m</span>"&gt;</span>Product Leadership, Innovation Drive, Collaborative Service<span class="html-tag">&lt;/p&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">qylc-card</span>"&gt;</span><span class="html-tag">&lt;p <span class="html-attribute-name">class</span>="<span class="html-attribute-value">qylc-c-t</span>"&gt;</span>Vision<span class="html-tag">&lt;/p&gt;</span><span class="html-tag">&lt;p <span class="html-attribute-name">class</span>="<span class="html-attribute-value">qylc-c-m</span>"&gt;</span>Reassure the Clients, Satisfy the Staff, Promote the society righteousness, Sustain the</td></tr><tr><td class="line-number" value="37"></td><td class="line-content"> business operation<span class="html-tag">&lt;/p&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">row no-gutters</span>"&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">qylc-imgs</span>"&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">qylc-img-o</span>"&gt;</span> <span class="html-tag">&lt;img <span class="html-attribute-name">src</span>="<a class="html-attribute-value html-resource-link" target="_blank" href="https://www.fscut.com/wp-content/themes/bcindex/assets/img/pro/021.png" rel="noreferrer noopener">https://www.fscut.com/wp-content/themes/bcindex/assets/img/pro/021.png</a>" <span class="html-attribute-name">alt</span>="<span class="html-attribute-value">fscut_about</span>" <span class="html-attribute-name">class</span>="<span class="html-attribute-value">qylc-img</span>"&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">qylc-img-o</span>"&gt;</span> <span class="html-tag">&lt;img <span class="html-attribute-name">src</span>="<a class="html-attribute-value html-resource-link" target="_blank" href="https://www.fscut.com/wp-content/themes/bcindex/assets/img/pro/022.png" rel="noreferrer noopener">https://www.fscut.com/wp-content/themes/bcindex/assets/img/pro/022.png</a>" <span class="html-attribute-name">alt</span>="<span class="html-attribute-value">fscut_about</span>" <span class="html-attribute-name">class</span>="<span class="html-attribute-value">qylc-img</span>"&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">qylc-img-o</span>"&gt;</span> <span class="html-tag">&lt;img <span class="html-attribute-name">src</span>="<a class="html-attribute-value html-resource-link" target="_blank" href="https://www.fscut.com/wp-content/themes/bcindex/assets/img/pro/023.png" rel="noreferrer noopener">https://www.fscut.com/wp-content/themes/bcindex/assets/img/pro/023.png</a>" <span class="html-attribute-name">alt</span>="<span class="html-attribute-value">fscut_about</span>" <span class="html-attribute-name">class</span>="<span class="html-attribute-value">qylc-img</span>"&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">qylc-img-o</span>"&gt;</span> <span class="html-tag">&lt;img <span class="html-attribute-name">src</span>="<a class="html-attribute-value html-resource-link" target="_blank" href="https://www.fscut.com/wp-content/themes/bcindex/assets/img/pro/024.png" rel="noreferrer noopener">https://www.fscut.com/wp-content/themes/bcindex/assets/img/pro/024.png</a>" <span class="html-attribute-name">alt</span>="<span class="html-attribute-value">fscut_about</span>" <span class="html-attribute-name">class</span>="<span class="html-attribute-value">qylc-img</span>"&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;/div&gt;</span><span class="html-tag">&lt;/section&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">foot-bg m-top-50</span>"&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">container foot-ul d-none d-sm-block margin-top</span>"&gt;</span> <span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="/en/" rel="noreferrer noopener">/en/</a>" <span class="html-attribute-name">class</span>="<span class="html-attribute-value">foot-icon-a</span>"&gt;</span> <span class="html-tag">&lt;img <span class="html-attribute-name">src</span>="<a class="html-attribute-value html-resource-link" target="_blank" href="/wp-content/themes/bcindex/assets/img/shouye/logo.png" rel="noreferrer noopener">/wp-content/themes/bcindex/assets/img/shouye/logo.png</a>" <span class="html-attribute-name">alt</span>="" <span class="html-attribute-name">class</span>="<span class="html-attribute-value">foot-icon</span>"&gt;</span> <span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;div <span class="html-attribute-name">class</span>="<span class="html-attribute-value">row no-gutters</span>"&gt;</span><span class="html-tag">&lt;ul <span class="html-attribute-name">class</span>="<span class="html-attribute-value">f-ul f-ul-c</span>"&gt;</span><span class="html-tag">&lt;li <span class="html-attribute-name">class</span>="<span class="html-attribute-value">f-ul-title</span>"&gt;</span><span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="/en/product/" rel="noreferrer noopener">/en/product/</a>"&gt;</span>Products<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;li&gt;</span><span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="/en/product#board-system" rel="noreferrer noopener">/en/product#board-system</a>"&gt;</span>Laser Cutting Controller<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;li&gt;</span><span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="/en/product#bus-system" rel="noreferrer noopener">/en/product#bus-system</a>"&gt;</span>EtherCAT Bus Controller<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;li&gt;</span><span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="/en/product#intelligent-hardware" rel="noreferrer noopener">/en/product#intelligent-hardware</a>"&gt;</span>Intelligent Hardware<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;li&gt;</span><span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="/en/product#follower-system" rel="noreferrer noopener">/en/product#follower-system</a>"&gt;</span>Height Controller<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;li&gt;</span><span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="/en/product#visual-system" rel="noreferrer noopener">/en/product#visual-system</a>"&gt;</span>Vision System<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;li&gt;</span><span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="/en/product#informatization-system" rel="noreferrer noopener">/en/product#informatization-system</a>"&gt;</span>Industrial IoT<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/li&gt;</span><span class="html-tag">&lt;li&gt;</span><span class="html-tag">&lt;a <span class="html-attribute-name">href</span>="<a class="html-attribute-value html-external-link" target="_blank" href="/en/product#other-system" rel="noreferrer noopener">/en/product#other-system</a>"&gt;</span>Accessories<span class="html-tag">&lt;/a&gt;</span><span class="html-tag">&lt;/li&gt;</span>…

---
## [Katskan/cmss13](https://github.com/Katskan/cmss13)@[5c4b13863f...](https://github.com/Katskan/cmss13/commit/5c4b13863f90877e920ce329bd60e99559d7fe35)
#### Tuesday 2023-07-04 02:30:44 by ihatethisengine

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
## [Mqiib/Yogstation](https://github.com/Mqiib/Yogstation)@[465aef0da1...](https://github.com/Mqiib/Yogstation/commit/465aef0da1b967bf7cb008e7906f5791d81b89cd)
#### Tuesday 2023-07-04 02:30:53 by Cark

Some minor changes to space syndicate base. (#19282)

* syndiebuff

* fuck you airlock

* fucking AIRLOCK CONTROLLERS

---
## [PokkeFe/ShipTrek](https://github.com/PokkeFe/ShipTrek)@[7df4885117...](https://github.com/PokkeFe/ShipTrek/commit/7df4885117a4a12ea333934d5af92e0766c84c5d)
#### Tuesday 2023-07-04 03:12:42 by Mark Suckerberg

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
## [ss220club/Skyrat-tg](https://github.com/ss220club/Skyrat-tg)@[9701b40ca0...](https://github.com/ss220club/Skyrat-tg/commit/9701b40ca03e164bd8bd4238fafb6cf778c52efe)
#### Tuesday 2023-07-04 03:32:10 by SkyratBot

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
## [rat-pin-cap/Studies](https://github.com/rat-pin-cap/Studies)@[b272335a7e...](https://github.com/rat-pin-cap/Studies/commit/b272335a7e76a7d5ac90585bce732bdbaf967627)
#### Tuesday 2023-07-04 03:33:50 by N. Biggs

Near miss study

A basic search idea used on a commissioned django site project. Originally was intended to be its own thing but ended up as a decent idea due to the site's need for mobile friendly features and setups. In my personal experience, this would capture many of the typos I make in my daily life with my phone.

The idea originated from reading descriptions of warship combat in WW1/WW2 which helped inspire the name and function. In testing with the project it is a part of, it has proven fairly reliable, though it is only compliant with english keyboards/input currently

---
## [httpsgithu/play-with-docker](https://github.com/httpsgithu/play-with-docker)@[a66a469fa0...](https://github.com/httpsgithu/play-with-docker/commit/a66a469fa0804ba22679b808203030d242efe157)
#### Tuesday 2023-07-04 04:16:58 by Marcos Lilljedahl

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
## [DesmontTiney/tgstation](https://github.com/DesmontTiney/tgstation)@[8788e48378...](https://github.com/DesmontTiney/tgstation/commit/8788e483788db2432b9649313efc9426d324379f)
#### Tuesday 2023-07-04 04:55:10 by Time-Green

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
## [The-Fleet/fleetstation13](https://github.com/The-Fleet/fleetstation13)@[b304b6523f...](https://github.com/The-Fleet/fleetstation13/commit/b304b6523fa1f497800c8ba3818e4d2c01d4eaf4)
#### Tuesday 2023-07-04 06:03:39 by LemonInTheDark

Converts del logging to proper json, using json objects instead of building a text file (#75636)

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

---
## [wulfenbach-jpg/tgstation](https://github.com/wulfenbach-jpg/tgstation)@[d85e44c69c...](https://github.com/wulfenbach-jpg/tgstation/commit/d85e44c69cc06dbeeb3a0de7f76273de45ee3893)
#### Tuesday 2023-07-04 06:03:47 by ChungusGamer666

SPECIES NUKING 2023: Head flags 3 & Knuckles: Fixes some growing pains with head flags  (#76440)

## About The Pull Request

Fixes https://github.com/tgstation/tgstation/issues/76422
This was caused by me somehow not using the wrapper there and not
noticing it

Also fixes hair gradients and facial hair gradients. I am pretty sure
they were uhh, being hidden behind the actual hair/facial hair. Oops.

Also also fixes spawning yourself as a human as admin and getting random
hair colors. That was just a failure to update the icon after updating
everything, I think?

Additionally, to totally babyproof all of this, ensures that head_flags
involved stuff gets applied AFTER species by creating a new preference
priority, and uses two separate wrappers to apply gradient style and
color.

Here's this absolute hellspawn to prove that everything works.

![image](https://github.com/tgstation/tgstation/assets/82850673/7ed29a68-cb60-4b28-996c-3be0e7331be8)

![image](https://github.com/tgstation/tgstation/assets/82850673/e57128be-0d7c-46ad-90dd-ee25981d0fea)

![image](https://github.com/tgstation/tgstation/assets/82850673/5c3619a8-fe6f-42b3-9fdc-12277d568e8d)

![image](https://github.com/tgstation/tgstation/assets/82850673/fdd13000-2220-47ad-8e02-44bc75a4a907)

Sorry for being so damn good at breaking this codebase.

## Why It's Good For The Game

Bugs are bad they make you mad

## Changelog

:cl:
fix: Hair and facial hair gradients work again now
fix: Facial hair colors apply properly again
fix: Admin spawned characters will get hair color preferences applied
properly
/:cl:

---
## [jeremyd2019/binutils-gdb](https://github.com/jeremyd2019/binutils-gdb)@[8bcead6966...](https://github.com/jeremyd2019/binutils-gdb/commit/8bcead69665af3a9f9867cd34c3a1daf22120027)
#### Tuesday 2023-07-04 06:49:46 by Andrew Burgess

gdb/testsuite: add test for core file with a 0 pid

This patch contains a test for this commit:

  commit c820c52a914cc9d7c63cb41ad396f4ddffff2196
  Date:   Fri Aug 6 19:45:58 2010 +0000

              * thread.c (add_thread_silent): Use null_ptid instead of
              minus_one_ptid while getting rid of stale inferior_ptid.

This is another test that has been carried in the Fedora GDB tree for
some time, and I thought that it would be worth merging to master.  I
don't believe there is any test like this currently in the testsuite.

The original issue was reported in this thread:

  https://inbox.sourceware.org/gdb-patches/AANLkTi=zuEDw6qiZ1jRatkdwHO99xF2Qu+WZ7i0EQjef@mail.gmail.com/

The problem was that when GDB was used to open a vmcore (core file)
image generated by the Linux kernel GDB would (sometimes) crash with
an assertion failure:

  thread.c:884: internal-error: switch_to_thread: Assertion `inf != NULL' failed.

To understand what's going on we need some background; a vmcore file
represents each processor core in the same way that a standard
application core file represents threads.  Thus, we might say, a
vmcore file represents cores as threads.

When writing a vmcore file, the kernel will store the pid of the
process currently running on that core as the thread's lwpid.

However, if a core is idle, with no process currently running on it,
then the lwpid for that thread is stored as 0 in the vmcore file.  If
multiple cores are idle then multiple threads will have a lwpid of 0.

Back in 2010, the original issue reported tried to change the kernel's
behaviour in this thread:

  https://lkml.org/lkml/2010/8/3/75

This change was rejected by the kernel team, the current
behaviour (lwpid of 0) was considered correct.  I've checked the
source of a recent kernel.  The code mentioned in the lkml.org posting
has moved, it's now in the function crash_save_cpu in the file
kernel/kexec_core.c, but the general behaviour is unchanged, an idle
core will have an lwpid of 0, so I think GDB still needs to be able to
handle this case.

When GDB loads a vmcore file (which is handled just like any other
core file) the sections are processed in core_open to generate the
threads for the core file.  The processing is done by calling
add_to_thread_list, a function which looks for sections named .reg/NN
where NN is the lwpid of the thread, GDB then builds a ptid_t for the
new thread and calls add_thread.

Remember, in our case the lwpid is 0.  Now for the first thread this
is fine, if a little weird, 0 isn't usually a valid lwpid, but that's
OK, GDB creates a thread with lwpid of 0 and carries on.

When we find the next thread (core) with lwpid of 0, we attempt to
create another thread with an lwpid of 0.  This of course clashes with
the previously created thread, they have the same ptid_t, so GDB tries
to delete the first thread.

And it was within this thread delete code that we triggered a bug
which would then cause GDB to assert -- when deleting we tried to
switch to a thread with minus_one_ptid, this resulted in a call to
find_inferior_pid (passing in minus_one_ptid's pid, which is -1), the
find_inferior_pid call fails and returns NULL, which then triggered an
assert in switch_to_thread.

The actual details of the why the assert triggered are really not
important.  What's important (I think) is that a vmcore file might
have this interesting lwpid of 0 characteristic, which isn't something
we see in "normal" application core files, and it is this that I think
we should be testing.

Now, you might be thinking: isn't deleting the first thread the wrong
thing to do?  If the vmcore file has two threads that represent two
cores, and both have an lwpid of 0 (indicating both cores are idle),
then surely GDB should still represent this as two threads?  You're
not wrong.  This was mentioned by Pedro in the original GDB mailing
list thread here:

  https://inbox.sourceware.org/gdb-patches/201008061057.03037.pedro@codesourcery.com/

This is indeed a problem, and this problem is still present in GDB
today.  I plan to try and address this in a later commit, however,
this first commit is about getting a test in place to confirm that GDB
at a minimum doesn't crash when loading such a vmcore file.

And so, finally, what's in this commit?

This commit contains a new test.  The test doesn't actually contain a
vmcore file.  Instead I've created a standard application core file
that contains two threads, and then manually edited the core file to
set the lwpid of each thread to 0.

To further reduce the size of the core file (as it will be stored in
git), I've zeroed all of the LOAD-able segments in the core file.
This test really doesn't care about that part of the core file, we
only really care about loading the register's, this is enough to
confirm that the GDB doesn't crash.

Obviously as the core file is pre-generated, this test is architecture
specific.  There are already a few tests in gdb.arch/ that include
pre-generate core files.  Just as those existing tests do, I've
compressed the core file with bzip2, which reduces it to just 750
bytes.  I have structured the test so that if/when this patch is
merged I can add some additional core files for other architectures,
however, these are not included in this commit.

The test simply expands the core file, and then loads it into GDB.
One interesting thing to note is that GDB reports the core file
loading like this:

  (gdb) core-file ./gdb/testsuite/outputs/gdb.arch/core-file-pid0/core-file-pid0.x86-64.core
  [New process 1]
  [New process 1]
  Failed to read a valid object file image from memory.
  Core was generated by `./segv-mt'.
  Program terminated with signal SIGSEGV, Segmentation fault.
  The current thread has terminated
  (gdb)

There's two interesting things here: first, the repeated "New process
1" message.  This is caused because linux_core_pid_to_str reports
anything with an lwpid of 0 as a process, rather than an LWP.  And
second, the "The current thread has terminated" message.  This is
because the first thread in the core file is the current thread, but
when GDB loads the second thread (which also has lwpid 0) this causes
the first thread to be deleted, as a result GDB thinks that the
current (first) thread has terminated.

As I said previously, both of these problems are a result of the lwpid
0 aliasing, which is not being fixed in this commit -- this commit is
just confirming that GDB doesn't crash when loading this core file.

Reviewed-By: Kevin Buettner <kevinb@redhat.com>

---
## [rylethever/UACME](https://github.com/rylethever/UACME)@[c65f9215c1...](https://github.com/rylethever/UACME/commit/c65f9215c1103269ca31f66f49869fcde547af98)
#### Tuesday 2023-07-04 06:55:01 by hfiref0x

Update Naka.vcxproj

Retarget platform toolset for appveyor fail. I understand that this service is currently busy supporting %current thing% more than actually working on their script-shit, but holy fuck seriously.

---
## [Tiktodz/android_kernel_asus_sdm636](https://github.com/Tiktodz/android_kernel_asus_sdm636)@[10f928c2f8...](https://github.com/Tiktodz/android_kernel_asus_sdm636/commit/10f928c2f8ae755117c42c7b6657957369fe7c70)
#### Tuesday 2023-07-04 08:07:47 by George Spelvin

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
## [Crimdahl/BeyondChaosRandomizer](https://github.com/Crimdahl/BeyondChaosRandomizer)@[6ecb2514ac...](https://github.com/Crimdahl/BeyondChaosRandomizer/commit/6ecb2514acd962169aaebb21ab93667357e9f95f)
#### Tuesday 2023-07-04 08:59:31 by Crimdahl

Merging in Web version changes.

randomizer.py:
- Wrapped the whole randomize process in a try/except block to pass exceptions back to GUI/Web
- Added support for custom coral names from web
- Added support for a custom playlist from web
- Added support for a custom passwords from web

appearance.py:
- Added support for custom coral names from web
- Added validation to ensure there are enough male and female names

musicinterface.py:
- Added support for a custom playlist from web

musicrandomizer.py:
- Reordered imports
- Added support for a custom playlist from web
- Made tierboss section check case-insensitive

options.py:
- Fixed an invalid default value for dancingmaduin

sillyclowns.py:
- Added support for a custom passwords from web

formationrandomizer.py:
- Import changes

appearance.py, dialoguemanager.py, esperrandomizer.py, itemrandomizer.py, locationrandomizer.py, monsterrandomizer.py, namerandomizer.py, randomizer.py, skillrandomizer.py, towerrandomizer.py, utils.py, wor.py:
- Cosmetic changes to variable names and/or spacing

---
## [CheeseOnGithub/cheese-hook](https://github.com/CheeseOnGithub/cheese-hook)@[5fae8a1e39...](https://github.com/CheeseOnGithub/cheese-hook/commit/5fae8a1e399303de4d65a3268ac82eaa51a87bb5)
#### Tuesday 2023-07-04 09:21:16 by CheeseOnGithub

i need money guy i add more linkvertise because FUCK YOU

---
## [Sealed101/tgstation](https://github.com/Sealed101/tgstation)@[03c964ac45...](https://github.com/Sealed101/tgstation/commit/03c964ac45e727543aac85ad817df89a7555fb31)
#### Tuesday 2023-07-04 09:47:24 by LemonInTheDark

Reworks Duffel Bags (Zippers) (#76313)

## About The Pull Request

Reworks duffel bags in line with oranges proposed plan.


![image](https://github.com/tgstation/tgstation/assets/58055496/126743dd-d7b8-47e0-bdd8-a0caec39c515)

Basically, instead of just making you slower all the time, they make you
slower while you have them open, but give you the same speed while
they're closed.
As a trade off, opening and closing them takes time, 2.1 seconds
(matches the sound) and 0.5 respectively.


https://github.com/tgstation/tgstation/assets/58055496/555d2cd0-038e-4b0b-a693-0c66dac16f5b

[Adds support for limiting extra storage, uses it to make syndie stuff
cool](https://github.com/tgstation/tgstation/pull/76313/commits/d0b2bbf937435b36de3ba497c48771f563b76684)

[d0b2bbf](https://github.com/tgstation/tgstation/pull/76313/commits/d0b2bbf937435b36de3ba497c48771f563b76684)

Syndicate bags currently ignore downsides by just ignoring the slowdown,
but that's kinda boring so let's just buff em instead.

They now support holding a limited amount of bulky items (3), filtered
down to things that would otherwise constitute going loud (or otherwise
be useful to carry around as a loudish traitor)

I may have gone a bit overboard on what I whitelisted here, lemme know
yeah?

I also did some fenangling with backpack uses of create_storage, I don't
like this pattern it was a bad idea I think.

## Why It's Good For The Game

I'm unsure if these delays enough, I think any length of time is decent
since it means you need to stop moving and focus on it for a bit.
My hope is this will make them a proper sidegrade, rather then something
that goes unused/acts as newbie bait

## Changelog
:cl:
balance: Duffelbags will now only make you slow while they are unzipped.
As a tradeoff, you now need to stand still and zip/unzip them to access
their contents/not move real slow.
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [NitheshChowdhary/UserLoginApp](https://github.com/NitheshChowdhary/UserLoginApp)@[ebbd2b212c...](https://github.com/NitheshChowdhary/UserLoginApp/commit/ebbd2b212cfdbcbe6fe860dfc611329aa2f18329)
#### Tuesday 2023-07-04 10:35:26 by NitheshChowdhary

UserLogin App

"Introducing a sleek React JS Login App with a user-friendly Login page, seamless Registration process, and a delightful Home Page upon successful login. Experience effortless authentication and enjoy a personalized journey!"

---
## [BarteG44/Shiptest](https://github.com/BarteG44/Shiptest)@[7468161f7e...](https://github.com/BarteG44/Shiptest/commit/7468161f7ec2180c7752cd2cc99b164522a3540a)
#### Tuesday 2023-07-04 11:22:11 by FalloutFalcon

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
## [BarteG44/Shiptest](https://github.com/BarteG44/Shiptest)@[0e6f7fa646...](https://github.com/BarteG44/Shiptest/commit/0e6f7fa64649dfbf52b8e4b71756e6625e50fdd0)
#### Tuesday 2023-07-04 11:22:11 by Imaginos16

TileTest Part 1: Big Sweeping Changes! (#2054)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->
## !! WARNING !!
This is a multi-parter PR. Due to the fact that tiles here on shiptest
are an unholy amalgam of decals, greyscale sprites and multiple
spread-out files, things are *bound* to look weird. If they do, feel
free to report it and it will be addressed in future PRs.

## About The Pull Request

This PR finally accomplishes the promise I made to @triplezeta a year
ago, creating a unique tileset for the server that people may enjoy!

To put every single microscopic change I have made would take forever,
so I will instead provide a series of screenshots of it in action!


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/00e9cec0-335a-4367-90f9-1adc572595f3)


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/497310ab-fe06-4b31-8774-70e79338a7d8)


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/80991d0b-c48b-404b-b4a6-cbb1c4c6af3a)


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/cc06d43e-3873-499e-aa12-51a0d7a37c98)

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Utilizing an unique, modernized tileset for our server to differentiate
from our competitors is something that has been requested, and I was
more than happy to lend my hand to make it a reality!
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy
del: Removes several unused floor types, as well as completely
annihilating the "monofloor" and "dirty" floor types, and the "edge"
decal type.
imageadd: Redoes the floors using the TileTest tileset!
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
## [bezidev/BeziAppFrontend](https://github.com/bezidev/BeziAppFrontend)@[1a04e9133f...](https://github.com/bezidev/BeziAppFrontend/commit/1a04e9133f8600ab9c4a62c8de2e0ba2b4ea4010)
#### Tuesday 2023-07-04 11:56:25 by mytja

I love how vite dev server doesn't complain about this, but vite build says HELL NAH, AIN'T NO FUCKING WAY I COMPILE THIS SHIT.
Anyhow, this is a follow-up on my writeup on the last commit.
I don't love how Kiwi browser suddenly disconnects my dev console/tools from the page, just because of some shitty "battery saving" capabilities of my Android phone.
So, instead I have fallen in love with Chrome DevTools remote debugging (chrome://inspect/#devices and https://developer.chrome.com/docs/devtools/remote-debugging). Very juicy stuff if you ask me.
Chromium Remote Debugging ftw.

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[02e36ec18e...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/02e36ec18e5ff421243b6816cf115d27c2c4263d)
#### Tuesday 2023-07-04 12:36:41 by SkyratBot

[MIRROR] Expanding the Experimental MODsuit Bepis Node with three new modules. [MDB IGNORE] (#21851)

* Expanding the Experimental MODsuit Bepis Node with three new modules. (#75801)

## About The Pull Request
So, I've had this idea to make a contribution to the Bepis feature with
some modsuit stuff. The gimmicky stuff is ok and a good way to even out
the better content since it has game of chance design it has (you can
find those disks in space anyway so...). However, the Experimental
MODsuit node feels very underwhelming right now, compared to how big
that feature is.

This PR adds three MOD modules to the Experimental MODsuit node, plus
two more:
- Magneto Charger: While the Modsuit is activated, each step the user
takes will charge the installed power cell by a tiny bit, enough to
sustain a standard modsuit of generic slow speed with only a few, easy
modules installed. It won't work in zero G, while flying, pulled by
someone else, on a conveyor belt, riding a vehicle or crawling on the
floor, though.
- Recycler: It collects (most) garbage and casings off the ground and
recycles them into material sheets that can be dispensed on an adjacent
location or storage with with Middle Mouse Button. Doesn't clean debris,
and scuffed because most trash doesn't yield material anyway.
- - It also has two subtypes, unbound from the node: one that dispenses
riot foam darts and can be found on the black market, and another that
dispenses the more innocuous foam darts, rarely found in maints.
- Shooting Assistant: A configurable module. On Stormtrooper mode, it
will give the user a faster fire rate (the double tap trait) at the cost
of accuracy. On Sharpshooter mode, it will improve the user accuracy and
make their shots ricochet against walls at least once (if the hit atom
allows that, that is, e.g. lasers don't ricochet against iron walls), at
the cost of movement speed. Both modes also prevent the user from dual
wielding guns.

To make the Stormtrooper mode stackable with the poor aim quirk and
refrain from making a new trait for the sharpshooter mode, the gun
spread code in gun.dm has also received a little refactor and cleanup.
Also, it's been tested.

## Why It's Good For The Game
The Experimental MODsuit node is quite shabby and could use something
extra to make it more appealing to MODsuit enjoyers.

Also doubles down as a small addition to the black market and maint
loot, and code cleanup, since gun code gives off some garbled vibes.

## Changelog

:cl:
add: Expanded the Experimental MODsuit Bepis node with three new
modules: Magneto Charger, Recycler and Shooting Assistant.
add: Added a Riot Foam Recycler module to the black market, as well a
more innocuous version as maint loot.
/:cl:

* Expanding the Experimental MODsuit Bepis Node with three new modules.

* update modular, I hate this file btw

---------

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>
Co-authored-by: Tom <8881105+tf-4@users.noreply.github.com>

---
## [Jolly-66/tgstation](https://github.com/Jolly-66/tgstation)@[f2ec16c1e6...](https://github.com/Jolly-66/tgstation/commit/f2ec16c1e6485bdf2035837fb3d42de24900e8b4)
#### Tuesday 2023-07-04 13:13:57 by Vekter

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
## [knative-automation/kn-plugin-source-kamelet](https://github.com/knative-automation/kn-plugin-source-kamelet)@[c2397f05e5...](https://github.com/knative-automation/kn-plugin-source-kamelet/commit/c2397f05e537cf6d185540adb1db33de39bbaa89)
#### Tuesday 2023-07-04 14:14:07 by Knative Automation

upgrade to latest dependencies

bumping knative.dev/networking e5d04e8...b9dd5c2:%0A  > b9dd5c2 upgrade to latest dependencies (# 816)%0A  > 68947c5 upgrade to latest dependencies (# 815)%0A  > 14a2bd4 Move `pkg/certificates` from `control-protocol` to `networking` (# 802)%0A  > 2daa483 Update community files (# 813)%0A  > 0dbe4f9 upgrade to latest dependencies (# 812)%0A  > 2a2f7d2 upgrade to latest dependencies (# 810)%0A  > fcbedad Update community files (# 809)%0A  > a44b093 upgrade to latest dependencies (# 808)%0A  > 7c2f7ac upgrade to latest dependencies (# 807)%0A  > 33636d9 Backward compatibility for InternalEncryption (# 806)%0A  > 77975a1 Add the new certificate names for dataplane and controlplane (# 804)%0A  > c3cca43 upgrade to latest dependencies (# 803)%0A  > 3f4627e Add internal trust flag to config (# 778)%0A  > 02055c8 Update community files (# 801)%0A  > 68725bd upgrade to latest dependencies (# 798)%0A  > 1594abb Update community files (# 797)%0Abumping github.com/fsnotify/fsnotify 0f4b979...5f8c606:%0A  > 5f8c606 Update ChangeLog%0A  > 8878587 Tweak the docs a bit%0A  > 89b4cf1 Add test for re-adding a renamed file (# 508)%0A  > 85acde2 Update x/sys%0A  > 69c24b0 Update x/sys%0A  > fb07f82 Add test to see what happens if you watch a symlink (# 498)%0A  > 666da9c Clarify doc comment on WatchList() (# 499)%0A  > 123e4e3 Add note about README version%0A  > 61a05ce Update documentation and examples (# 496)%0A  > e180a87 Move some inotify-tests to run on all backends; test that state is cleaned up after Remove (# 494)%0A  > fdf41a3 Move some files around%0A  > 844d71f Port minor test changes from fen-v2 branch; make LICENSE text not ugly%0A  > 5b87f50 windows: simplify a bit (# 493)%0A  > 2bfaa00 all: add Watcher.{sendEvent,sendError} (# 492)%0A  > 8ab3b84 kqueue: don't set up watchers on unreadable files (# 479)%0A  > a4bcdf8 Update changelog%0A  > 4b43fad kqueue: remove timeout from unix.Kevent() (# 480)%0A  > a24f78c windows: test symlinks (# 491)%0A  > f45391f windows: run TestWatchRename/rename_overwriting_existing_file (# 490)%0A  > ee33a65 Use "os.Rename()" in tests instead of "mv"%0A  > 9dd0568 cmd/fsnotify: fix time.Format() string%0A  > 5dcbfba windows: replace syscall with golang.org/x/sys/windows%0A  > 1f8edaf windows: replace "e" with "err" for error variables%0A  > 99715ba windows: increase buffer size from 4K to 64K (# 485)%0A  > a5c5815 ci: update to use Go 1.19, kick off fewer builds, update x/sys (# 484)%0A  > f2d35c3 Remove CLA section in contributing%0A  > 4604469 Need Linux 5.9 for a useful fanotify we can use%0A  > a566bb1 Update CONTRIBUTING.md%0A  > 01dfc6f Remove PULL_REQUEST_TEMPLATE%0A  > a58e868 Run tests in illumos (# 481)%0A  > 666c6a0 Update ChangeLog%0A  > 928895c [bugfix] close handle when remWatch open in getIno (# 288)%0A  > f174f95 windows: update watch paths when renaming directories with sub-watches (# 370)%0A  > 87dc1fa Rewrite tests (# 478)%0A  > 57e6a49 Add {Event,Op}.Has() (# 477)%0A  > 39823aa Document that /proc and /sys won't work%0A  > 60fbf57 Clarify FAQ on goroutines%0A  > ca0e2f4 macos: retry if open() returns EINTR (# 475)%0A  > ff39bb4 Fix lint (# 476)%0A  > 421f529 debian 6 test: deal with multiple packages (# 474)%0A  > a3256ef Remove AUTHORS file%0A  > 0e78fa6 Update README: split out FAQ to "Platform-specific notes"%0A  > 1a7b6ef inotify: don't ignore events for files that don't exist (# 470)%0A  > f0aceb2 Tweak comment regarding relative paths (# 466)%0A  > d9c9fa5 Add cmd/fsnotify (# 463)%0A  > cc15908 kqueue: better error if watching a file fails (# 471)%0A  > c4e64e4 Replace Use of Kthread-blocking Epoll with Poller Read, Remove Per-Event LStats on Linux # 433 (# 434)%0A  > 4b8b298 Test some more things in CI (# 469)%0A  > 548b8fb Add missing changelog for 1.4.{8,9} (# 468)%0A  > 7fe2936 inotify: fix race in Close() (# 465)%0A  > 35b6378 Clarify README on network drives (# 467)%0A  > e56409e Update link to CONTRIBUTING in the README (# 464)%0A  > 4678dfd Update documentation for linux systems (max_user_watches) (# 287)%0A  > 808f582 bump up GitHub Actions (# 461)%0A  > 4193dfd Do not suppress Chmod on non-existent file (# 260)%0A  > 6ae56b7 kqueue: Make watcher.Close() O(n) instead of O(n^2) (# 233)%0A  > adf5320 strings.Builder instead of bytes.Buffer (# 285)%0A  > 217e78e Explicit mutext (un)locking (# 462)%0A  > 1a4f949 Use common error when removing an unwatched file (# 460)%0A  > 5acfdc1 windows: protect access to isClosed with mutex (# 454)%0A  > c56cafd Test Go 1.18%0A  > 37badf6 This project is archived (# 459)%0Abumping knative.dev/hack f591fea...fc42790:%0A  > fc42790 Update community files (# 296)%0A  > d7586a2 Update e2e kntest link (# 295)%0A  > a861c8e Update community files (# 294)%0A  > 5b7907f Update actions (# 289)%0A  > c133d5d Install Istio for tests (# 291)%0A  > 5812c57 Update community files (# 292)%0A  > 7d81248 Update community files (# 286)%0A  > 6e4569c Update community files (# 285)%0Abumping github.com/prometheus/client_model 7bc5445...63fb982:%0A  > 63fb982 Merge pull request # 63 from prometheus/sparsehistogram%0A  > 5c16fa2 Merge pull request # 57 from prometheus/repo_sync%0A  > fdb567d Add note about native histograms to README%0A  > 6b8c742 Update common Prometheus files%0A  > 942d53c Update common Prometheus files%0A  > 7f720d2 Add note about experimental state of native histograms%0A  > f60d1ac Update common Prometheus files%0A  > 1f8dcad Merge pull request # 59 from prometheus/beorn7/histogram%0A  > 6dc836e Merge pull request # 53 from prometheus/repo_sync%0A  > 421ad2b Merge pull request # 58 from prometheus/beorn7/histogram%0A  > a7ff713 Flatten the buckets of native histograms%0A  > 0e1ed89 Merge pull request # 52 from prometheus/repo_sync%0A  > a227486 Update common Prometheus files%0A  > 408689d Merge branch 'master' into sparsehistogram%0A  > 0da3265 Explain Span layout better%0A  > 14ab895 Merge pull request # 51 from prometheus/repo_sync%0A  > bc75c6a Update common Prometheus files%0A  > 61b6c1a Merge pull request # 47 from prometheus/beorn7/histogram%0A  > 8171e83 Add float histograms and gauge histograms to proto spec%0A  > a863571 Merge pull request # 49 from prometheus/repo_sync%0A  > 2fc368c Update common Prometheus files%0A  > 8831f0d Merge branch 'master' into sparsehistogram%0A  > bbaf1cc Switch to base 2 and powers of 2 for resolution%0A  > 675c4e5 Merge pull request # 48 from prometheus/repo_sync%0A  > a3e6551 Update common Prometheus files%0A  > 24db95a Merge remote-tracking branch 'origin/master' into beorn7/histogram%0A  > 147c58e Move .proto file and add caching of protoc and protoc-gen-go during build (# 46)%0A  > 56ab8d9 Update common Prometheus files%0A  > 4b803f3 Experimental encoding for sparse buckets in histogram%0A  > 0255a22 Merge pull request # 43 from roidelapluie/security-dot-md%0A  > 1f48c5c Rename metrics.proto to io_prometheus_client_metrics.proto (# 45)%0A  > 60555c9 Merge pull request # 41 from prometheus/repo_sync%0A  > 1bb3080 Add SECURITY.md%0A  > 1106810 Update common Prometheus files%0Abumping k8s.io/apiextensions-apiserver 2c55649...52c998e:%0A  > 52c998e Update dependencies to v0.26.5 tag%0A  > 186ff9b Merge pull request # 117274 from jkh52/release-1.26-knp-0.0.37%0A  > b7b18f5 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > ee5015a Bump konnectivity-client to 0.0.37%0A  > 9ce75f3 Bump runc go module v1.1.4 -> v1.1.6%0A  > e9d194a Merge pull request # 115599 from jkh52/release-1.26-knp-0.0.36%0A  > d7df0be Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 9152c67 Bump konnectivity-client to v0.0.36%0A  > 89cec57 Update golang.org/x/net to v0.7.0%0A  > f72cc5c Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 28eb995 Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 33db789 Merge pull request # 114861 from jpbetz/release-1.26%0A  > a06e03d Merge pull request # 114927 from jkh52/release-1.26-knp-metrics%0A  > 0859963 Cherry pick 114857 to release-1.26%0A  > 5183885 Bump konnectivity-client to v0.0.35%0A  > 6e13726 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > c338f3e Update golang.org/x/net 1e63c2f%0A  > 9768bad sync: update go.mod%0A  > f9c2bba fix aggregated discovery version sorting%0A  > d2c9e18 Merge pull request # 113171 from Jefftree/aggregated-discovery-generic%0A  > 470c040 Merge pull request # 113577 from pacoxu/prometheus-client%0A  > 915a888 add crds to aggregated discovery%0A  > 92430b6 Merge pull request # 113314 from cici37/celIntegration%0A  > ac326ca upgrade prometheus-client to v1.14.0%0A  > 5a6bf16 Merge pull request # 113688 from dashpole/update_utils%0A  > 67b0610 Integrate cel admission with API.%0A  > 84fed82 upgrade github.com/prometheus/client_golang to v1.13.1%0A  > 077b441 update k8s.io/utils to fix util tracing panic%0A  > 5bbf20d Adding new api version of admissionregistration.k8s.io v1alpha1 for CEL in Admission Control%0A  > 3b533ba Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > 975bbeb dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > ae2b4c3 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > c4deae9 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > bc4263f Merge pull request # 113172 from dashpole/endpoint_handler_tracing%0A  > f6c164e migrate apiserver utiltrace usage to component-base/tracing%0A  > 53e3726 Merge pull request # 113015 from ritazh/crencryption%0A  > c8d8a9f Enable encryption for custom resources%0A  > 6405068 Merge pull request # 113325 from panslava/fix-time-since-defer%0A  > 508e399 Fix time.Since() in defer. Wrap in anonymous function%0A  > 5f8e59e Merge pull request # 112691 from aimuz/apiextensions-apiserver-change-to-cmp%0A  > c996139 Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > f83e03c apiextensions-apiserver: change k8s.io/apimachinery/pkg/util/diff to github.com/google/go-cmp/cmp%0A  > b68fc51 dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > 49c41b4 Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > 3aaa2a0 Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > d9f6ebd update kube-openapi%0A  > 82e3ba4 Merge pull request # 112789 from enj/enj/r/kms_load_once_v2%0A  > 7423813 update fsnotify to v1.6.0%0A  > 8bf3487 Merge pull request # 113011 from jpmcb/cobra-1.6.0%0A  > d34393e Load encryption config once%0A  > 6ba582f Bumps cobra from 1.5.0 to 1.6.0%0A  > 8e0697b Merge pull request # 113022 from logicalhan/webhook-metrics%0A  > 90c63e0 Merge pull request # 112926 from jiahuif-forks/refactor/cel-out-of-apiextensions%0A  > 548c480 unparameterize 'webhook' from conversion metrics since it's the only one%0A  > 77badb8 Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 609e270 use DefaultMaxRequestSizeBytes for maxRequestSizeBytes.%0A  > 04f26fa Bump golang.org/x/text to v0.3.8%0A  > dd981e1 move CEL package to apiserver package.%0A  > 1644998 Move celopenapi/model to staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/cel/ (# 109959)%0A  > 08d44e8 Merge pull request # 112875 from pohly/update-yaml%0A  > 1300140 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 5fb82bd Merge pull request # 112819 from thockin/no-make-generators%0A  > f5f5279 Codegens: Do not auto-set boilerplate path%0A  > f22ee73 Merge pull request # 112738 from liggitt/proto-tag%0A  > ba7f1b7 Merge pull request # 112689 from cheftako/master%0A  > 7ac7774 github.com/matttproud/golang_protobuf_extensions v1.0.2%0A  > e678457 Merge pull request # 112748 from wojtek-t/lock_ssa_gate%0A  > 0aca5a6 Bump konnectivity-client to v0.0.33%0A  > 9be4b4a Lock ServerSideApply feature to true%0A  > 7b53cb7 Merge pull request # 111980 from aramase/kms%0A  > f40a683 Merge pull request # 112705 from stevekuznetsov/skuznets/fix-comment%0A  > 4cd9125 Add staging directory for kms%0A  > d4e654a clients: clarify a misleading comment%0A  > 8b851d9 Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 362a89c Merge pull request # 112615 from mengjiao-liu/update_CRD_link%0A  > add0c80 Update to latest k8s.io/utils to pick up changes%0A  > 374216b Merge pull request # 112613 from dims/update-github.com/go-openapi/jsonreference-to-drop-github.com/PuerkitoBio/purell%0A  > a7ee7f9 Update `PreserveUnknownFields` field document link%0A  > 488bf20 update github.com/go-openapi/jsonreference to drop github.com/PuerkitoBio/purell%0A  > 47c15ca Merge pull request # 112588 from pacoxu/fsnotify-v1.5.4%0A  > d5b6243 Merge pull request # 112584 from dims/brneto-master%0A  > 8c6aa82 update fsnotify/fsnotify to v1.5.4%0A  > f8e18e9 run pin-dependency.sh and then hack/update-vendor.sh%0A  > c540c8c Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 70b0d96 Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 39cab0b updated etcd to v3.5.5 and newer otel libraries as well%0A  > 5faccda Merge pull request # 111866 from pacoxu/validate%0A  > 1c3fe9d e2e: bump ginkgo to v2.2.0%0A  > 917d446 Merge pull request # 112458 from dims/switch-to-release-tag-for-antlr-v1.4.10%0A  > 8b3fe74 add test case for array checking with dup values%0A  > 045fc90 Merge pull request # 112433 from ncdc/reduce-SchemaHas-allocs%0A  > 73cc883 Switch to release tag for antlr : v1.4.10%0A  > 22bcc66 added ratcheting validation for embedded resource and x-kubernetes-list-type validation%0A  > 269d73d Reduce allocations in HasSchemas%0A  > 7342cc6 Merge pull request # 112200 from pohly/client-go-shared-informer-factory-shutdown%0A  > aabbdff Merge pull request # 112349 from pohly/klog-update%0A  > fdf28bc client-go: support waiting for SharedInformerFactory shutdown%0A  > 6b7d12b build: update to klog v2.80.1%0A  > 559b4fa Merge pull request # 111768 from weilaaa/feature_add_symmetric_difference_in_sets_string%0A  > bf7d058 add symmetric difference in sets%0A  > 04ff81e Merge pull request # 112199 from pohly/klog-update%0A  > 87a4c3f dependencies: update to klog v2.80.0%0A  > 8f15690 Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > f637e1c dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > b6adc1c Merge pull request # 111964 from DangerOnTheRanger/cel-estimate-fix-update%0A  > ea2d438 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 6b4dc0b Add unit tests.%0A  > 767e67b Bump prometheus/client_golang to v1.13.0%0A  > 782b982 Run pin-dependency.sh and update-vendor.sh.%0A  > 305963e Merge pull request # 111909 from tosi3k/bump-prom-client%0A  > fa2959a Merge pull request # 111830 from t1anz0ng/typo%0A  > 5a6ffec Bump prometheus/client_golang to v1.12.2%0A  > e0abc3b fix(typo): remove extra " from autoscaling doc string%0A  > 2184a8d Merge pull request # 111696 from liggitt/go119mod%0A  > f750907 Update go.mod to go1.19%0Abumping knative.dev/client-pkg 4f052f9...f377f06:%0A  > f377f06 Update community files (# 106)%0A  > b93ceb0 Update community files (# 105)%0A  > 83c91f4 Update community files (# 103)%0A  > e5c405e Update community files (# 102)%0A  > eee9b55 Update community files (# 100)%0Abumping knative.dev/serving 2c1bb07...bb1262e:%0A  > bb1262e Update net-kourier nightly (# 14129)%0A  > 32ec382 Drop unused ytt patch for Ingress ServiceType (# 14143)%0A  > 4c3b36c Update net-gateway-api nightly (# 14136)%0A  > 9a75a93 Update net-istio nightly (# 14132)%0A  > ca618b7 Update net-certmanager nightly (# 14131)%0A  > ea3e9c3 Update net-contour nightly (# 14130)%0A  > 2e7d6e4 Update community files (# 14128)%0A  > 63fa389 Allow to set QP resources per service (# 14038)%0A  > 9310e4d Update net-kourier nightly (# 14125)%0A  > 0462ce6 Update net-istio nightly (# 14126)%0A  > 2813b9a Update net-gateway-api nightly (# 14119)%0A  > eaf666e Update net-istio nightly (# 14116)%0A  > 53169cd Update net-istio nightly (# 14112)%0A  > e865aa7 Update net-contour nightly (# 14109)%0A  > 921daf8 Update net-certmanager nightly (# 14111)%0A  > bb581cc Update net-kourier nightly (# 14110)%0A  > fbfffc0 upgrade to latest dependencies (# 14108)%0A  > bcf9274 upgrade to latest dependencies (# 14101)%0A  > f085b30 fix: requests are sent to all pods even if cc=1 and the parity of activatorCount and podTracker is different (# 14022)%0A  > 9772417 Update net-kourier nightly (# 14107)%0A  > f6d0c7b Update net-contour nightly (# 14106)%0A  > 560e0ea Update net-certmanager nightly (# 14105)%0A  > 51f4f1e Update net-istio nightly (# 14104)%0A  > 18519b1 Update net-contour nightly (# 14079)%0A  > 38c155e Add chainguard-dev/actions for creating kind cluster (# 14018)%0A  > 74c57d8 Update net-istio nightly (# 14098)%0A  > 5a9c574 Update net-kourier nightly (# 14096)%0A  > 3a6c2b6 upgrade to latest dependencies (# 14095)%0A  > 5a90438 Update net-istio nightly (# 14091)%0A  > dc0692a Update net-istio nightly (# 14088)%0A  > 0fbd780 Update net-certmanager nightly (# 14087)%0A  > 6f63c98 Update net-kourier nightly (# 14086)%0A  > e74f5f4 Update net-gateway-api nightly (# 14085)%0A  > 1587070 Update net-kourier nightly (# 14081)%0A  > 2e00e9f Update net-certmanager nightly (# 14080)%0A  > a3c7864 Update net-istio nightly (# 14078)%0A  > 384b889 Update net-gateway-api nightly (# 14077)%0A  > 7d0f963 Change storage version of DomainMapping to v1beta1 (# 14058)%0A  > e8b6f05 Update net-gateway-api nightly (# 14068)%0A  > 41e4212 Get certificate reconciler from `networking` instead of `control-protocol` (# 14072)%0A  > e71b933 Update net-certmanager nightly (# 14070)%0A  > 8f516b6 Update net-kourier nightly (# 14069)%0A  > a2bb4aa upgrade to latest dependencies (# 14071)%0A  > c95f17b Update community files (# 14067)%0A  > bf48e64 Remove deprecated internalEncryption dependency (# 14064)%0A  > 6b87d67 Update net-istio nightly (# 14065)%0A  > fbecf34 refactor throttler_test.go (# 14055)%0A  > 349b2d6 Change minimum TLS version to 1.3 for internal encryption (between activator and queue-proxy) (# 13887)%0A  > d07bf78 Update net-contour nightly (# 14049)%0A  > aa023e8 Update net-istio nightly (# 14048)%0A  > 8fc4bb9 Update net-gateway-api nightly (# 14047)%0A  > 135be30 Update net-certmanager nightly (# 14046)%0A  > 8da71b5 Update net-kourier nightly (# 14042)%0A  > 13a4e46 poll until timeout - don't error out if the deployment can't be found (# 14027)%0A  > 31c2b7e upgrade to latest dependencies (# 14043)%0A  > 6a6e417 Update net-istio nightly (# 14041)%0A  > 807fc2c Update net-certmanager nightly (# 14040)%0A  > 3c23945 drop safe to evict annotations (# 14035)%0A  > fca5c14 Update net-gateway-api nightly (# 14033)%0A  > c12c917 Update net-contour nightly (# 14034)%0A  > 2da856d Update net-kourier nightly (# 14032)%0A  > d7c8779 Update net-certmanager nightly (# 14031)%0A  > aaf01dc Update net-istio nightly (# 14030)%0A  > bdaa436 RandomChoice 2 policy wasn't random when the number of targets is 2 (with equal weight) (# 14028)%0A  > c91f8c4 Fix metrics reporting period (# 14019)%0A  > 9f60969 Update net-kourier nightly (# 14004)%0A  > 6020cec Update net-istio nightly (# 14025)%0A  > 88cae7f Update net-gateway-api nightly (# 14016)%0A  > a143bf8 Update net-contour nightly (# 14015)%0A  > c2be582 Update net-certmanager nightly (# 14014)%0A  > 3450f0a upgrade to latest dependencies (# 14013)%0A  > 35cfd8f [Automated] Update net-gateway-api nightly (# 14003)%0A  > 08a9708 Update net-istio nightly (# 14009)%0A  > 5074b4c Update net-contour nightly (# 14010)%0A  > e8cb343 upgrade to latest dependencies (# 13999)%0A  > 1261074 Update net-certmanager nightly (# 14002)%0A  > f987ca6 Bump kind to 0.19 (# 14008)%0A  > fbb7fa1 Update community files (# 13998)%0A  > bff1d80 Remove 1.24 kind version (# 14007)%0A  > a657321 Update net-kourier nightly (# 13993)%0A  > d75b0f0 Update net-contour nightly (# 13990)%0A  > 6d26f54 upgrade to latest dependencies (# 13991)%0A  > df5001f Update net-certmanager nightly (# 13992)%0A  > 2594084 upgrade to latest dependencies (# 13989)%0A  > 7c303fa Update cluster-version to 1.25 (# 13988)%0A  > 9e751a2 Update net-certmanager nightly (# 13974)%0A  > 7b35cfb upgrade to latest dependencies (# 13987)%0A  > 99800ed Set default domain to cluster's domain (# 13964)%0A  > c90fabf Metric annotations work with global class config (# 13978)%0A  > da31cd1 Update net-kourier nightly (# 13975)%0A  > f457924 Update net-contour nightly (# 13976)%0A  > 14ad4d1 upgrade to latest dependencies (# 13973)%0A  > 00ddfd9 Update net-kourier nightly (# 13972)%0A  > fc63583 Update net-kourier nightly (# 13966)%0A  > 219285e Update net-kourier nightly (# 13959)%0A  > 2fa05bd Min TLS for tag to digest defaults to 1.2 again and is configurable (# 13962)%0A  > 43df348 Update net-contour nightly (# 13958)%0A  > 50a9f22 Update net-certmanager nightly (# 13961)%0A  > 4e379cb Update net-gateway-api nightly (# 13957)%0A  > 3d53294 Update net-istio nightly (# 13960)%0A  > ea2a6c8 :lipstick: Install ko using setup-ko, from ko-build (# 13951)%0A  > e5070cd upgrade to latest dependencies (# 13950)%0A  > 9778f2d Update net-istio nightly (# 13949)%0A  > f27ba4e Update net-certmanager nightly (# 13944)%0A  > 2840301 Update net-kourier nightly (# 13945)%0A  > 117a642 Update net-gateway-api nightly (# 13943)%0A  > 84a2230 Update net-contour nightly (# 13942)%0A  > 7aa5edb upgrade to latest dependencies (# 13941)%0A  > 01707d8 upgrade to latest dependencies (# 13940)%0A  > b7d5e8d Update net-istio nightly (# 13939)%0A  > 5e056a0 Update net-certmanager nightly (# 13926)%0A  > 35efd12 Update net-contour nightly (# 13929)%0A  > f476717 Update net-istio nightly (# 13935)%0A  > bd8e37c Update net-gateway-api nightly (# 13925)%0A  > 37a7010 Update net-kourier nightly (# 13934)%0A  > f47802d Update community files (# 13933)%0A  > 990d701 Update net-kourier nightly (# 13928)%0A  > ff9f03d Update net-istio nightly (# 13927)%0A  > 690c525 upgrade to latest dependencies (# 13924)%0A  > 1dd07a7 Update community files (# 13923)%0A  > 66141b8 Update net-istio nightly (# 13920)%0Abumping github.com/matttproud/golang_protobuf_extensions c182aff...c182aff:%0Abumping k8s.io/api 88912e3...6b24792:%0A  > 6b24792 Update dependencies to v0.26.5 tag%0A  > 37e98ba Merge pull request # 117814 from kerthcet/automated-cherry-pick-of-# 117802-upstream-release-1.26%0A  > 7ff025f Update podFailurePolicy comments from alpha-level to beta%0A  > c9f384e Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > c00f1ad Bump runc go module v1.1.4 -> v1.1.6%0A  > 4c28c5a Merge pull request # 117323 from dddddai/automated-cherry-pick-of-# 117182-upstream-release-1.26%0A  > 9483bbc use case-insensitive header keys for http probes%0A  > 0545f3a Merge pull request # 116081 from pohly/automated-cherry-pick-of-# 115928-origin-release-1.26%0A  > e92d7e9 api: generated files%0A  > 16f23da api: drop Resources.Claims from PVC and PVC template%0A  > 5fd8a44 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 1b65b64 Update golang.org/x/net to v0.7.0%0A  > 2e857c1 Merge pull request # 115400 from pohly/automated-cherry-pick-of-# 115354-origin-release-1.26%0A  > 1c6bd70 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 50d0b42 dynamic resource allocation: avoid apiserver complaint about list content%0A  > 045c7fe Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 07a9cbc Merge pull request # 114617 from JoelSpeed/automated-cherry-pick-of-# 114585-upstream-release-1.26%0A  > 52655b9 Resource claims should be a map type%0A  > 07ac8fe Merge remote-tracking branch 'origin/master' into release-1.26%0A  > 566ee01 Update golang.org/x/net 1e63c2f%0A  > b966dc9 sync: update go.mod%0A  > 053624e Merge pull request # 111023 from pohly/dynamic-resource-allocation%0A  > 3590eda Merge pull request # 113375 from atiratree/PodHealthyPolicy-api%0A  > 8356158 api: update testdata%0A  > 5cb3202 Merge pull request # 113186 from ttakahashi21/KEP-3294%0A  > 5a4f9a5 generated%0A  > 78799a8 api: generated files%0A  > dfd6ea2 Generate code%0A  > 993c43c api: add UnhealthyPodEvictionPolicy for PDBs%0A  > ef72ea9 api: dynamic resource allocation API%0A  > d8ab3fb Add API and validation for CrossNamespaceVolumeDataSource%0A  > af772fc api: add resource claims to core API%0A  > 7beaa08 Merge pull request # 112744 from pwschuurman/statefulset-slice-impl%0A  > d7d25c8 Merge pull request # 113360 from mimowo/handling-pod-failures-beta-enable%0A  > f46cd33 Undo unintentional documentation comment change%0A  > f967e44 Merge pull request # 113485 from MikeSpreitzer/apf-borrowing%0A  > 11620b8 Enable the feature into beta%0A  > 6ae95de Fix typo in function emptyInvariants()%0A  > 34f4a52 apiserver: update API testdata at HEAD for flowcontrol%0A  > 3928298 Rebasing feature branch%0A  > e91ffd8 apiserver: add generated files for borrowing in flowcontrol%0A  > d961983 Update doc comments and change name of feature gate%0A  > fcd0d56 apiserver: add fields for borrowing in apf flowcontrol%0A  > adddac7 Small updates and comment fixes%0A  > 98c1aa6 Merge pull request # 113314 from cici37/celIntegration%0A  > 0d02273 Update generated protobuf files%0A  > 3f61c95 Merge pull request # 113688 from dashpole/update_utils%0A  > 8a0a045 API - make update%0A  > a5e7c66 Adding implementation of KEP-3335, StatefulSetSlice%0A  > 72a29bf Merge pull request # 113500 from kerthcet/feat/graduate-nodeInclusionPoplicy-to-beta%0A  > 2a2f510 update k8s.io/utils to fix util tracing panic%0A  > 891a1f8 Adding new api version of admissionregistration.k8s.io v1alpha1 for CEL in Admission Control%0A  > ee30dcf Merge pull request # 113047 from everpeace/improve-supplemental-groups-description%0A  > 2482389 Feat: graduate NodeInclusionPolicy to beta%0A  > a489930 Rename copy to v1alpha1%0A  > 9a33ad3 Merge pull request # 112360 from mimowo/handling-pod-failures-beta-kubelet%0A  > c4b2250 Improve the description of PodSecurityContext.SupplementalGroups (including cri-api)%0A  > 358a069 Copy over admissionregistration v1 to v1alpha1%0A  > 6c616e1 Merge pull request # 113510 from alculquicondor/finalizers-stable%0A  > 5210e2f Add pod disruption conditions for kubelet initiated failures%0A  > 2025045 Merge pull request # 113351 from andrewsykim/endpointslice-terminating-ga%0A  > aa2b4eb Graduate JobTrackingWithFinalizers to stable%0A  > 4bad656 Merge pull request # 113274 from Huang-Wei/kep-3521-A%0A  > aa9d0a7 k8s.io/api/discovery: remove API docs referencing EndpointSliceTerminatingCondition feature gate%0A  > 91f2496 Merge pull request # 113496 from avoltz/anvoltz/ga-itr%0A  > 686871f Automated codegen%0A  > c865c5c Promote ServiceInternalTrafficPolicy to GA%0A  > bd25e4f APIs, Validation and condition enforcements%0A  > 5448eb3 Merge pull request # 106242 from thockin/revive-copy-lb-status-type-to-ingress%0A  > edbfe77 Copy LoadBalancerStatus from core to networking%0A  > 6892570 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > c5dc3f4 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > 4e8dc44 Merge pull request # 111978 from Jefftree/aggregated-discovery-types%0A  > 72580e4 Add discovery types%0A  > 0184bd8 Merge pull request # 112643 from SergeyKanzhelev/removeDynamicKubeletConfig%0A  > 0f81104 Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > f8118a1 remove DynamicKubeletConfig feature gate from the code%0A  > 370c8f0 Bump golang.org/x/text to v0.3.8%0A  > 3638040 Merge pull request # 112875 from pohly/update-yaml%0A  > 7ecab5c dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 669318b Merge pull request # 112832 from tkashem/apf-prelifecycle-gen%0A  > 2cfef31 apiserver: prerelease-lifecycle-gen for flowcontrol%0A  > 3cedfad Merge pull request # 112306 from tkashem/v1beta3%0A  > 3814236 Merge pull request # 112707 from enj/enj/i/https_links%0A  > 418dd97 add testdata for flowcontrol v1beta3%0A  > ba008c5 Use https links for k8s KEPs, issues, PRs, etc%0A  > c96c62f rename assuredConcurrencyShares for flowcontrol v1beta3%0A  > be233f8 Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 51a3f54 add patch annotations to flowcontrol v1beta3%0A  > ca5be1f Update to latest k8s.io/utils to pick up changes%0A  > 7e203ee apiserver: generate for apf v1beta3%0A  > 79091da Merge pull request # 112577 from andrewsykim/feature-gate-cleanup%0A  > 19d0ef4 apiserver: enable v1beta3 for apf%0A  > 052d63f Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 1f28922 remove +featureGate=LoadBalancerClass tag in service.spec.loadBalancerClass%0A  > f50a5b7 apiserver: apf rename copy to v1beta3%0A  > 9df3db1 updated etcd to v3.5.5 and newer otel libraries as well%0A  > bed6431 apiserver: copy apf v1beta2 to v1beta3%0A  > c98ebf1 Merge pull request # 112487 from liggitt/flowcontrol-test%0A  > 5c9e17a Add compatibility fixtures for v1beta2 flowcontrol%0A  > 9842651 Merge pull request # 111333 from flant/selfsubjectattributesreviews%0A  > 43df43b Add auth API to get self subject attributes%0A  > 30ff991 Merge pull request # 112349 from pohly/klog-update%0A  > e6114e9 build: update to klog v2.80.1%0A  > 929c3f0 Merge pull request # 112301 from aojea/ipv6_rfc3849%0A  > a687cab use IPv6 Address Prefix Reserved for Documentation for api docs%0A  > 6dd661f Merge pull request # 112199 from pohly/klog-update%0A  > 8a7d12c dependencies: update to klog v2.80.0%0A  > a6ff7c9 Merge pull request # 112146 from kerthcet/feat/move-schedulerError-to-api%0A  > ab89e44 Move constant schedulerError in scheduler to v1 package%0A  > d104994 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 15b6dd2 Bump prometheus/client_golang to v1.13.0%0A  > 3be0a3c Merge pull request # 111974 from liggitt/1-25-compatibility%0A  > 49e055e Merge pull request # 111830 from t1anz0ng/typo%0A  > fcc83cd Drop 1.23 compatibility data%0A  > 64f80bd Merge pull request # 111611 from kardashov/ref-spec-docs-typo-fix%0A  > ea5df3a fix(typo): remove extra " from autoscaling doc string%0A  > 4cde1ad Add 1.25 compatibility data%0A  > 2e7b661 Merge pull request # 111657 from aojea/hc_nodeport%0A  > d07af88 Generate specs after fixing typo in documentation%0A  > 649256a Fix typo in field description.%0Abumping k8s.io/apimachinery 4fbe8e4...b207ce5:%0A  > b207ce5 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > 917de35 Bump runc go module v1.1.4 -> v1.1.6%0A  > 53ecdf0 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 05339fa Update golang.org/x/net to v0.7.0%0A  > eabbfd5 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 48b8d1f Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 373a5f7 Merge pull request # 114521 from 3point2/automated-cherry-pick-of-# 113283-upstream-release-1.26%0A  > b5e5df6 Fix SPDY proxy authentication with special chars%0A  > 553a2d6 Improve error message when proxy connection fails%0A  > 5d4cdd2 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > 6cbc4a3 Update golang.org/x/net 1e63c2f%0A  > 6561235 Merge pull request # 113699 from liggitt/manjusaka/fix-107415%0A  > dad8cd8 Update workload selector validation%0A  > fe82462 Add extra value validation for matchExpression field in LabelSelector%0A  > 067949d update k8s.io/utils to fix util tracing panic%0A  > 0ceff90 Merge pull request # 112223 from astraw99/fix-ownerRef-validate%0A  > 9e85d3a Merge pull request # 112649 from howardjohn/set/optimize-everything-nothing%0A  > b0dd9ec Fix ownerRef controller validate err%0A  > b03a432 Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > 88a1448 Rename and comment on why sharing is safe%0A  > 4e6bcdb dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > 3adc870 Optimize `Everything` and `Nothing` label selectors%0A  > 0524d6c Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > 5a0277f Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > 6809593 Merge pull request # 112377 from weilaaa/refactor_sets_use_generic%0A  > 70a38aa Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > f2d9aed refactor sets use generic%0A  > d097f82 dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > 7b5633b Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > b839e82 Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > b7d8973 update kube-openapi%0A  > 1dc6ace update fsnotify to v1.6.0%0A  > 78d003c Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 04898ff Bump golang.org/x/text to v0.3.8%0A  > 79993b2 Merge pull request # 112875 from pohly/update-yaml%0A  > 7379c15 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 66e26ac Merge pull request # 112707 from enj/enj/i/https_links%0A  > 882b67d Use https links for k8s KEPs, issues, PRs, etc%0A  > 7fb78ee Merge pull request # 112472 from ialidzhikov/nit/error-msg%0A  > 826a74e Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 22fe889 Improve the error returned from the `LabelSelectorAsSelector` func%0A  > e2f9797 Update to latest k8s.io/utils to pick up changes%0A  > f8159af Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 612703e Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 9901884 updated etcd to v3.5.5 and newer otel libraries as well%0A  > 6439059 Merge pull request # 112526 from liggitt/redirect%0A  > 0564b5e e2e: bump ginkgo to v2.2.0%0A  > 2e3bf73 Limit redirect proxy handling to redirected responses%0A  > 6d854d7 Merge pull request # 112349 from pohly/klog-update%0A  > e1e1b7c build: update to klog v2.80.1%0A  > ed93eed Merge pull request # 111768 from weilaaa/feature_add_symmetric_difference_in_sets_string%0A  > 36163c5 Merge pull request # 112193 from jindijamie/master%0A  > b7b9ba4 add symmetric difference in sets%0A  > 31bc292 Merge pull request # 112199 from pohly/klog-update%0A  > 1c318b6 Add an option for aggregator%0A  > 0d0d03e Merge pull request # 111936 from haoruan/bugfix-111928-microtime-marshal-precision%0A  > 145c075 dependencies: update to klog v2.80.0%0A  > 2d64dac Merge pull request # 112089 from zeze1004/fix-typo%0A  > 2187a78 Marshal MicroTime to json and proto at the same precision%0A  > 53c4d51 Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > 30e9977 Fix typo "sturct" to "struct"%0A  > 5e4f25a dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > 349dcdf Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 16a7f7a Bump prometheus/client_golang to v1.13.0%0A  > 2b9fe2c Merge pull request # 111808 from alvaroaleman/meta-wrapping%0A  > bb48261 Apimachinery meta errors: Support errors.Is and error wrapping%0Abumping golang.org/x/sys 90c8f94...c7a1bf9:%0A  > c7a1bf9 unix: define PerfBitWriteBackward%0A  > 1470852 unix: add SetsockoptTCPMD5Sig on linux%0A  > a6bfb89 unix: use unsafe.Slice in anyToSockaddr%0A  > c10701f windows: use unsafe.Slice in (*RawSockaddrAny).Sockaddr on windows%0A  > 6f25076 unix: define extended TCPInfo on Linux%0A  > 10499f4 unix: add ioctlPtr with unsafe.Pointer arg on other unices (cont)%0A  > 92c4c39 unix: add Dup3 on FreeBSD%0A  > 748af6e unix: pass PROT_MPROTECT(PROT_READ|PROT_WRITE) to initial Mmap on netbsd%0A  > 972870e unix/linux: update to Linux kernel 6.2, glibc 2.37 and Go 1.20.1%0A  > cc0b67d unix: use C.ioctl in generated ioctlPtr%0A  > a3b23cc unix: use SYS_PTRACE in generated ptracePtr%0A  > 71a906e unix/linux: add TUN flags and virtio_net_hdr constants%0A  > 2977c77 unix: add ptracePtr that accepts pointer arg as unsafe.Pointer%0A  > 6877dcc execabs: don't override Go 1.19 error with our error%0A  > b13f40e unix: add ioctlPtr with unsafe.Pointer arg on other unices%0A  > 3b9b58b unix: Faccess: check CAP_DAC_OVERRIDE on Linux%0A  > 2da1413 cpu: get hwcap/auxv from the Go 1.21+ runtime%0A  > 4fee21c windows: Add WSALookupService syscall wrappers%0A  > c79a742 unix: fix a use-after-free bug in PtraceIO on freebsd%0Abumping k8s.io/client-go 7226b15...6e9dabb:%0A  > 6e9dabb Update dependencies to v0.26.5 tag%0A  > 038b381 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > cd83e43 Bump runc go module v1.1.4 -> v1.1.6%0A  > dbfbc03 Merge pull request # 117686 from ardaguclu/automated-cherry-pick-of-# 117495-upstream-release-1.26%0A  > d72dec4 Use absolute path instead requestURI in openapiv3 discovery%0A  > a5144d4 Merge pull request # 117638 from seans3/automated-cherry-pick-of-# 117571-origin-release-1.26%0A  > d6f8d04 Refactors discovery content-type and helper functions%0A  > 2dd0093 Merge pull request # 115899 from odinuge/automated-cherry-pick-of-# 115620-upstream-release-1.26%0A  > f3ae5cb Merge pull request # 116666 from seans3/automated-cherry-pick-of-# 116603-origin-release-1.26%0A  > fffc68d Change where transformers are called.%0A  > 5ebee18 Aggregated discovery resilient to nil GVK%0A  > 8190aa4 client-go/cache: update Replace comment to be more clear%0A  > 87720b3 Merge pull request # 116437 from seans3/automated-cherry-pick-of-# 116145-# 115865-origin-release-1.26%0A  > b667227 client-go/cache: rewrite Replace to check queue first%0A  > fc13749 Removes old discovery hack ignoring 403 and 404%0A  > 30215cd client-go/cache: merge ReplaceMakesDeletionsForObjectsInQueue tests%0A  > f39ba12 Plumb stale GroupVersions through aggregated discovery%0A  > ba35969 client-go/cache: fix missing delete event on replace without knownObjects%0A  > f538edf Merge pull request # 116352 from seans3/automated-cherry-pick-of-# 115978-origin-release-1.26%0A  > 97cf9cb client-go/cache: fix missing delete event on replace%0A  > 5dbbc58 Tolerate empty discovery response in memcache client%0A  > 62133a9 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 8ce239f Update golang.org/x/net to v0.7.0%0A  > e6bc0bc Merge pull request # 115566 from enj/automated-cherry-pick-of-# 115315-upstream-release-1.26%0A  > 9112e19 Merge pull request # 115400 from pohly/automated-cherry-pick-of-# 115354-origin-release-1.26%0A  > 0519b53 kubelet/client: collapse transport wiring onto standard approach%0A  > 2e34348 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 7be38cd dynamic resource allocation: avoid apiserver complaint about list content%0A  > 4968c4a Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 0c34939 Merge pull request # 114617 from JoelSpeed/automated-cherry-pick-of-# 114585-upstream-release-1.26%0A  > 04b098b Resource claims should be a map type%0A  > b3fff46 Merge pull request # 114415 from hoskeri/automated-cherry-pick-of-# 114404-upstream-release-1.26%0A  > 236db3c Merge pull request # 113988 from liggitt/automated-cherry-pick-of-# 113933-upstream-release-1.26%0A  > a2ef324 Check the correct error in d.downloadAPIs%0A  > 95a14c3 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > ebb499f Limit request retrying to []byte request bodies%0A  > 1a7cd1d Update golang.org/x/net 1e63c2f%0A  > 53f2fea sync: update go.mod%0A  > 968ba8d Merge pull request # 113797 from seans3/force-no-aggregated%0A  > c8ffed3 Merge pull request # 111023 from pohly/dynamic-resource-allocation%0A  > 3ac73ea Adds bool to force non-aggregated discovery%0A  > 61cd728 Merge pull request # 113826 from jsafrane/add-openstack%0A  > 522eaa1 api: generated files%0A  > cfd682c Merge pull request # 113375 from atiratree/PodHealthyPolicy-api%0A  > f2b10f3 Remove OpenStack cloud provider%0A  > acc9fa7 Merge pull request # 113186 from ttakahashi21/KEP-3294%0A  > f1c80d7 generated%0A  > a3d3eb0 Revert "Remove references to openstack and cinder"%0A  > c7bdab2 Generate code%0A  > 0a1f6a8 Merge pull request # 112744 from pwschuurman/statefulset-slice-impl%0A  > 1c7a870 Merge pull request # 113485 from MikeSpreitzer/apf-borrowing%0A  > eed2516 Adding implementation of KEP-3335, StatefulSetSlice%0A  > 7280270 Merge pull request # 113599 from seans3/discovery-client-update%0A  > d4a3675 apiserver: add generated files for borrowing in flowcontrol%0A  > 7694435 Update redacting functionality to redact all sensitive info in config when printing with view (# 109189)%0A  > 25d5761 Aggregated discovery client%0A  > 4b1a9fd Merge pull request # 113314 from cici37/celIntegration%0A  > ea9ec91 Merge pull request # 112905 from alexzielenski/kubectl-apply-csa-migration%0A  > 3a430a4 API - make update%0A  > 3daf180 Merge pull request # 113688 from dashpole/update_utils%0A  > 898b7a3 add FindFieldsOwners util function%0A  > dbe034b update k8s.io/utils to fix util tracing panic%0A  > 4f63b62 add UpgradeManagedFieldsPatch%0A  > 7ed3193 Merge pull request # 111545 from jlsong01/rewrite_signature_of_StartEventWatcher%0A  > c8c6cb5 add OWNERS to csaupgrade%0A  > cbe28cf Merge pull request # 113274 from Huang-Wei/kep-3521-A%0A  > 3467961 rewrite signature of function StartEventWatcher%0A  > a45874a remove kubectl annotation logic from upgrade patch%0A  > 2248bf3 Automated codegen%0A  > d576a35 Merge pull request # 113387 from wojtek-t/refactor_client_indexing%0A  > 4fbef5b Merge pull request # 106242 from thockin/revive-copy-lb-status-type-to-ingress%0A  > 5e7ba1f Minor cleanup of thread safe store%0A  > bc6266d Merge pull request # 103177 from arkbriar/support_cancelable_exec_stream%0A  > 3f162fe Copy LoadBalancerStatus from core to networking%0A  > b69a16c Refactor store index into its structure%0A  > 19b2e89 Merge pull request # 113523 from seans3/content-type-response%0A  > 0563dec Propagate the panic with a channel%0A  > 8ff4970 Get response content-type%0A  > 2362c7b use subtests and defer in TestSPDYExecutorStream%0A  > 0d57396 Merge pull request # 113304 from mimowo/handling-pod-failures-beta-ssa%0A  > 5e0a531 Support cancelable SPDY executor stream%0A  > a232cf0 Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > a191e58 SSA to add pod failure conditions - ready for review%0A  > 984bdbf dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > f87d047 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > d236783 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > ef8a2e5 Merge pull request # 113089 from zackzhangkai/fix-doc%0A  > 197e479 Merge pull request # 108959 from astraw99/fix-duplicate-list%0A  > 0945beb fix typo%0A  > 42a0e1c Merge pull request # 113062 from alexzielenski/client-go-json-output%0A  > f549acf Fix duplicate code block of ListAll function%0A  > b6d3c8d Merge pull request # 107278 from harsimranmaan/allow_pagination_in_dynamic_fake_lister%0A  > 624929c address feedback%0A  > 9cc33a4 Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > 0c269b7 remove selflink as per review feedback%0A  > 12cafe2 refactor to use Schema(contentType)%0A  > 9b51067 dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > fbd8e9a fix failing test assertions%0A  > 8b6ceae add more options for fetching openapiv3 in clients%0A  > fa9ed7f Merge pull request # 112860 from nckturner/remove-log-line%0A  > 1f10368 Preserve metadata for fake dynamic client unstructured lists%0A  > 6b24912 Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > 5870c62 Remove log line from expiration cache%0A  > aea20dd Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > e3bb48f update kube-openapi%0A  > 1af3711 update fsnotify to v1.6.0%0A  > e6d958c Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 5e469ba Bump golang.org/x/text to v0.3.8%0A  > f515a4c Merge pull request # 112774 from stevekuznetsov/skuznets/dynamic-client-similar%0A  > b28f6c9 Merge pull request # 112875 from pohly/update-yaml%0A  > 34e8a5d client-go: factor the dynamic client similarly to others%0A  > c9afc73 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > f24bd69 Merge pull request # 112306 from tkashem/v1beta3%0A  > ebc7cd4 Merge pull request # 112707 from enj/enj/i/https_links%0A  > 9b97b72 rename assuredConcurrencyShares for flowcontrol v1beta3%0A  > 2f43d37 Merge pull request # 112705 from stevekuznetsov/skuznets/fix-comment%0A  > 1665808 Use https links for k8s KEPs, issues, PRs, etc%0A  > 9bac803 apiserver: generate for apf v1beta3%0A  > 3697342 Merge pull request # 112680 from enj/enj/i/tls_cache_key_comparable%0A  > 956c1ce clients: clarify a misleading comment%0A  > c81636c Merge pull request # 112665 from NoicFank/fix-typo%0A  > cc2441c transport/cache: statically assert that tlsCacheKey is comparable%0A  > be20b2b Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 59765b8 fix typo error%0A  > 04dbcd8 Update to latest k8s.io/utils to pick up changes%0A  > 2fd4aac Merge pull request # 112613 from dims/update-github.com/go-openapi/jsonreference-to-drop-github.com/PuerkitoBio/purell%0A  > 47ad72a update github.com/go-openapi/jsonreference to drop github.com/PuerkitoBio/purell%0A  > f7c9c63 Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > b6e72dc Merge pull request # 112226 from aojea/client_go_transport%0A  > 6b5ecad updated etcd to v3.5.5 and newer otel libraries as well%0A  > acfaa39 Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 1bd914a client-go: test transport generation is goroutine safe%0A  > 037b5fd Merge pull request # 112514 from markmc/patch-1%0A  > ec6c80a e2e: bump ginkgo to v2.2.0%0A  > 3f66212 client-go: remove reference to TPR in examples%0A  > 86ffa32 Merge pull request # 112475 from vatsalparekh/fix-TestRESTClientLimiter%0A  > ece6462 Merge pull request # 112476 from enj/enj/i/list_pager_flake%0A  > bf2b395 Fix Infelicities in TestRESTClientLimiter%0A  > 58155b7 Merge pull request # 112450 from enj/enj/i/exec_tls_cache_holder_cleanup%0A  > 6703098 Check for context cancellation on each buffered chunk%0A  > eecd3e5 Merge pull request # 112091 from xyz-li/master%0A  > 5dab9a0 client-go/transport: drop Dial and GetCert fields in favor of Holders%0A  > f6b8521 Merge pull request # 111333 from flant/selfsubjectattributesreviews%0A  > cc3cc93 kubectl: fix memory leaks in port forwarding client%0A  > b2b55e6 Add auth API to get self subject attributes%0A  > 18c3338 Merge pull request # 112200 from pohly/client-go-shared-informer-factory-shutdown%0A  > 9dae691 Merge pull request # 112309 from shyamjvs/disable-compression%0A  > ec4fedd client-go: support waiting for SharedInformerFactory shutdown%0A  > ab826d2 Merge pull request # 112349 from pohly/klog-update%0A  > 49ac40b Autogen code%0A  > ab0bfda build: update to klog v2.80.1%0A  > b8a8d94 Add DisableCompression option to KubeConfig%0A  > f32861c Merge pull request # 112341 from enj/enj/i/second_time_is_the_charm%0A  > 7d208ba Remove in-tree credential plugins (again)%0A  > e003fa9 Merge pull request # 112017 from enj/enj/i/exec_tls_cache%0A  > 2698e82 Merge pull request # 111967 from alexzielenski/csa-to-ssa%0A  > 6a008ec exec auth: support TLS config caching%0A  > 27c67e7 Merge pull request # 111122 from alexzielenski/informer%0A  > 00d892f correct spacing%0A  > d28c736 Merge pull request # 112022 from JackZxj/release-lock%0A  > a300ae0 return when test is done%0A  > 2efbeaf add boilerplate%0A  > b8b6206 Merge pull request # 112199 from pohly/klog-update%0A  > d04c2ce update lock getter of leaderelection%0A  > 93e5e0e hold listener lock while waiting for goroutines to finish%0A  > dac0826 remove inaccurate comment%0A  > 5a2c3e9 dependencies: update to klog v2.80.0%0A  > e11a988 simplify control flow%0A  > 7634f2e make upgrade modify input instead of deep copying%0A  > 7ccf7b0 Merge pull request # 112134 from apelisse/client-go-valid-segment%0A  > ac7f657 fix spelling%0A  > 9aa7c11 remove fieldsv1 from upgrade body%0A  > d83ec9e Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > a4b84d8 Validate segments with client-go/dynamic%0A  > 0f4a6cf reset listenersStarted%0A  > 703d15e Update staging/src/k8s.io/client-go/util/csaupgrade/upgrade.go%0A  > cac10a8 dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > 449817f add multithreaded test to shared informer%0A  > 675ca93 refactor if statement%0A  > 46d4284 Merge pull request # 111241 from Abirdcfly/fixtestorsource%0A  > de0b767 remove duplicate test%0A  > cfaca90 address comments%0A  > bdae576 Merge pull request # 112068 from aojea/aojea_client_go%0A  > 9b300de make TestListPager_EachListItem rework%0A  > 0565962 address review comments%0A  > 089614c remove last applied configuration information%0A  > fd22687 add aojea as client-go reviewer%0A  > 5a25eb0 switch listeners to use a map, adapt tests%0A  > efe3789 add more test cases%0A  > 35ead05 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 90c6a46 active remove/add tests for event handlers%0A  > 46dc22f clean up test%0A  > 5291ca2 Bump prometheus/client_golang to v1.13.0%0A  > de4dd3a tests for invalid registration removals%0A  > ced85a8 update godoc%0A  > e6538dd Merge pull request # 112024 from cndoit18/remove-redundant-judgment%0A  > 33eff64 apply desired changes for handler registration%0A  > 049ba69 expose FieldsToSet and SetToFields%0A  > bcd2e6c style: remove redundant judgment%0A  > d73e40f rename handle to registration%0A  > aa892ab remove  unused code%0A  > d5e5863 Merge pull request # 111752 from aanm/revert-final-url-template%0A  > b3a61c6 remove informational informer methods again%0A  > 90ef078 dont expose internal methods in implementatoin%0A  > 5feaced Merge pull request # 67782 from dims/yank-in-tree-openstack-cloud-provider%0A  > e9d4627 client-go/rest: check if url is nil to prevent nil pointer dereference%0A  > ecdc8bf support removal of event handlers from SharedIndexInformers%0A  > c364b63 add function to upgrade managedfields CSA to SSA%0A  > 0fdc4f3 Merge pull request # 111684 from 0xff-dev/master1%0A  > 98e81a7 Remove references to openstack and cinder%0A  > c501ee0 Revert "client-go: remove no longer used finalURLTemplate"%0A  > 4faffa8 Merge pull request # 111564 from inosato/remove-ioutil-from-cli-client-go%0A  > c94a539 use constant NamespaceDefault instead of variable namespace%0A  > 2e40408 Merge pull request # 111918 from liggitt/in-tree-auth%0A  > 27de641 Remove ioutil from client-go%0Abumping golang.org/x/term d974fe8...0edf009:%0A  > 0edf009 go.mod: update golang.org/x dependencies%0Abumping knative.dev/eventing 034bec9...f5b1b12:%0A  > f5b1b12 Send namespace header in MT components (# 7048)%0A  > 4b5fde8 [main] Update community files (# 7043)%0A  > 8f74094 Add handler to auto create Event Types (# 7034)%0A  > 901ef61 Remove check for empty Namespace on resolver (# 7040)%0A  > 95cdbaa We should not limit the EventType creation from the Sources Duck to just brokers (# 7032)%0A  > 7429761 Adjust the Namespace reference to the one from the parent (# 7035)%0A  > cb2a891 update the redeployment script (# 7038)%0A  > ab01938 [main] Upgrade to latest dependencies (# 7025)%0A  > c9dcaf3 Added basic gc loop to kncloudevents clients map (# 6997)%0A  > d6cf96d EventType works with channel (# 7023)%0A  > 365d0b0 Run TLS e2e tests only when Istio is not enabled (# 7029)%0A  > 825a237 Update IMC CRD addressstatus to include `.name` and `.CACerts` fields (# 7026)%0A  > 3190df7 Tracking/reconcile KResource references (# 7014)%0A  > 0f68861 Rename more to Resource, instead of broker (# 7022)%0A  > bccb7d4 Better reflecting the lifecycle of event type … (# 7019)%0A  > 49d4acd Skip ping source TLS rekt test, since extremely flaky (# 7016)%0A  > 8719e18 [main] Upgrade to latest dependencies (# 7012)%0A  > e5ae717 Use HTTP POST when terminating istio proxy (# 7015)%0A  > fea730f Only check if the reference does exist (# 7010)%0A  > 631f4ec Add TLS support for mt-broker-filter (# 6940)%0A  > 45f0a19 Allow wathola components to run with Istio  (# 7011)%0A  > 65f4b1c [main] Format Go code (# 7008)%0A  > 3267b1a test SinkBinding with eventshub TLS receiver as sink (# 6979)%0A  > aad53f4 Updated eventingtls test certs to support IP addresses (# 7006)%0A  > 57d78e0 [main] Update community files (# 7004)%0A  > dfb2243 Support TLS in Trigger and Channel reconciler (# 6988)%0A  > df08b49 Eventing TLS: verify APIServerSource and PingSource sinkURI is https (# 6987)%0A  > d21c1aa [main] Upgrade to latest dependencies (# 6989)%0A  > 70113e8 Deprecate broker field and use KReference for the broker instead (# 6870)%0A  > 4e4647f test update to newest version (# 6990)%0A  > 870ac6b Update MessageDispatcher and FanoutMessageHandler to support sending events to TLS endpoints (# 6983)%0A  > 6dd5d58 Test PingSource with eventshub TLS receiver as sink (# 6965)%0A  > 55f4f28 [main] Upgrade to latest dependencies (# 6982)%0A  > 2a5a9a5 Add more items in the development getting started documentation (# 6978)%0A  > 59118a0 imc-dispatcher starts a TLS server, accepts host based routing on http receiver and path based routing on https receiver (# 6954)%0A  > ee49ada Rework kncloudevents library to support multiple clients (# 6975)%0A  > ee88094 Make ServerManager independent from kncloudevents package (# 6980)%0A  > 6a11c5f [main] Upgrade to latest dependencies (# 6969)%0A  > 8a9a532 Updated DEVELOPMENT.md to provide better instructions on setting up kubernetes (# 6977)%0A  > 390a0c8 Eventing TLS: Test ContainerSource with eventshub TLS receiver as sink (# 6957)%0A  > 5e245ac Fix flaky PingSource TLS unit test (# 6970)%0A  > f9f27c9 Use random names in Channel tests (# 6967)%0A  > d4609a5 Do not parse flags in InitializeEventingFlags (# 6966)%0A  > ef68a0a [main] Update community files (# 6968)%0A  > 4adc287 Add transport-encryption prerequisite for Addressable tests (# 6964)%0A  > deb0ef4 Add field for subscribers & replys CA certs to `SubscriberSpec` and `SubscriptionStatusPhysicalSubscription` (# 6959)%0A  > b81082c Eventing TLS: Test ApiServerSource with eventshub TLS receiver as sink (# 6956)%0A  > cdff269 Adding source duck type to v1b2 (# 6962)%0A  > b47b4ec [main] Upgrade to latest dependencies (# 6958)%0A  > 3315c20 Provide Channels CACerts in Brokers status annotation (# 6952)%0A  > 4b9fdef [main] Upgrade to latest dependencies (# 6955)%0A  > da31970 Improve cert-manager resources for Eventing TLS certs provisioning (# 6953)%0A  > fc5befb Provide subscribers CACerts in triggers status (# 6951)%0A  > 1efab19 Using v1b2 in the reconciler (# 6949)%0A  > c44671c Updating rekt test resources for EventType v1b2 (# 6946)%0A  > e31eb1f Adding testingv1b2 for eventtype (# 6944)%0A  > a9908ef Support TLS in PingSource (# 6929)%0A  > df559c0 Fix typo in flags.IsDisbledTransportEncryption name (# 6941)%0A  > 7073cc9 [main] Upgrade to latest dependencies (# 6939)%0A  > c6bc9bb Eventing TLS: Support K_CA_CERTS env variable injection for SinkBinding subjects (# 6931)%0A  > 24fbfe5 Eventing TLS: support exposing https address in Broker controller (# 6930)%0A  > d18cb42 Add information about retryable error in servermanager (# 6921)%0A  > f92a05b Added Support for K_CA_CERTS in the heartbeats (# 6920)%0A  > b8b43d0 Remove CA certs empty and non nil check, use URL scheme only (# 6928)%0A  > 3c8cc05 Return error directly if one receiver of servermanager fails (# 6919)%0A  > 92ab7f8 [main] Upgrade to latest dependencies (# 6927)%0A  > 5c6fe57 two more for reducing to debug, instead of info (# 6922)%0A  > 6cf9397 less verbose logs on scheduler component  (# 6912)%0A  > 69918f2 Adds ServerManager. Supports http/https message receivers (# 6908)%0A  > d58e259 Install ko using setup-ko in kind e2e tests (# 6910)%0A  > 9cdea5d Eventing TLS: Added Support for setting K_CA_CERTS in the ApiServerSource controller for the adapter (# 6897)%0A  > add8436 Eventing TLS: support exposing https address in InMemoryChannel controller (# 6881)%0A  > 59cfb6d [main] Upgrade to latest dependencies (# 6906)%0A  > 03f2a3d Remove unused test helper (# 6907)%0A  > 7a90c46 Remove eventing-natss from downstream tests (# 6905)%0A  > ba2550b [main] Upgrade to latest dependencies (# 6904)%0A  > 999eead More EventType v1beta2 work (# 6903)%0A  > 66e8257 Remove sanitize HTTP body for `knativeerrordata` extension (# 6902)%0A  > cd50d27 [main] Format Go code (# 6898)%0A  > 0f0a82c [main] Update community files (# 6901)%0A  > 7f4deb5 EventType v1b2 API addition (# 6893)%0A  > 1f917d0 Refactor PingSource adapter client creation (# 6880)%0A  > e2f1c77 [main] Update community files (# 6896)%0A  > 6a5c7ee Eventing TLS: migrate all resolver.URIResolver usages over to AddressableFromDestinationV1 (# 6883)%0A  > 0a12a6c Adds path based routing to message_receiver pkg (# 6873)%0Abumping golang.org/x/net 8e2b117...dfa2b5d:%0A  > dfa2b5d go.mod: update golang.org/x dependencies%0A  > 8c4ef2f hmtl: add security section to package comment%0A  > 1d46ed8 html: have Render escape comments less often%0A  > 569fe81 html: add "Microsoft Outlook comment" tests%0Abumping github.com/prometheus/client_golang 64435fc...254e546:%0A  > 254e546 Merge pull request # 1162 from kakkoyun/cut-1.14.0%0A  > 07d3a81 Merge pull request # 1161 from prometheus/release-1.13%0A  > c8a3d32 Cut v1.14.0%0A  > 870469e Test and support 1.19 (# 1160)%0A  > 53e51c4 Merge pull request # 1157 from prometheus/cut-1.13.1%0A  > b785d0c Fix go_collector_latest_test Fail on go1.19 (# 1136)%0A  > 79ca0eb Added tip from Björn + Grammarly.%0A  > 4d54769 Fix float64 comparison test failure on archs using FMA (# 1133)%0A  > 078f11f Cut 1.13.1 release (+ documenting release process).%0A  > 5f202ee Merge pull request # 1150 from prometheus/sparsehistogram%0A  > ddd7f0e Fix race condition with Exemplar in Counter (# 1146)%0A  > 0859bb8 Merge pull request # 1152 from jessicalins/update-to-custom-reg%0A  > fffb76c Merge branch 'main' into sparsehistogram%0A  > 1f93f64 Fix `CumulativeCount` value of `+Inf` bucket created from exemplar (# 1148)%0A  > 10b0550 Fix race condition with Exemplar in Counter (# 1146)%0A  > a340ca4 Run make format%0A  > e92a8c7 Avoid the term 'sparse' where possible%0A  > 8cc2b6c Fix double-counting bug in promhttp.InstrumentRoundTripperCounter (# 1118)%0A  > dcea97e Fix `CumulativeCount` value of `+Inf` bucket created from exemplar (# 1148)%0A  > 6056615 Update random example to use custom registry%0A  > d31f13b Add SparseBucketsZeroThresholdZero and groom doc comments%0A  > 9801a4e Examples: Replace deprecated WithGoCollections with WithGoCollectorRuntimeMetrics (# 1130)%0A  > 0b7f488 Update simple example to use custom registry%0A  > 58a8ca4 examples: Adjust doc comment for native histograms%0A  > 7c46c15 Clarify documentation around what constructors do (# 1125)%0A  > 9b5c5b8 Update basic example to use custom registry%0A  > 4e71e6f Update prometheus/client_model dependency%0A  > 83d56b1 Extend prometheus.Registry to implement Collector (# 1103)%0A  > 111fae1 Merge branch 'main' into sparsehistogram%0A  > 4c41dfb Clarify exemplar(Add|Observe) by renaming to (add|observe)WithExemplar (# 1122)%0A  > 25bc188 Merge pull request # 1144 from prometheus/beorn7/histogram2%0A  > f73e3cc Fix double-counting bug in promhttp.InstrumentRoundTripperCounter (# 1118)%0A  > 95cf173 Merge branch 'main' into sparsehistogram%0A  > 6942f9e sparse buckets: Fix handling of +Inf/-Inf/NaN observations%0A  > c7aa2a5 Merge pull request # 1113 from prometheus/release-1.13%0A  > ec86ef1 Merge pull request # 1092 from prometheus/beorn7/histogram%0A  > 1e61b8e Update common Prometheus files (# 1111)%0A  > 6141a07 Merge branch 'main' into sparsehistogram%0A  > 8cbcd40 histograms: Move to new exposition protobuf format%0A  > 5a321c7 Merge branch 'foo-commit' into sparsehistogram%0A  > e93e384 Merge branch 'beorn7/release' into sparsehistogram%0A  > e203144 Merge branch 'release-1.12' of github.com:prometheus/client_golang into release-1.12%0A  > 525d042 Merge branch 'main' into sparsehistogram%0A  > a516626 Merge branch 'release-1.12' into beorn7/release%0A  > a27b6d7 Fix conflicts%0A  > 6ba7871 Merge branch 'main' into sparsehistogram%0A  > eb59a7b Histogram: Fix bug with negative schemas (# 1054)%0A  > b237230 Merge branch 'main' into sparsehistogram%0A  > 294cca4 Merge branch 'main' into sparsehistogram%0A  > 70253f4 Fix typo in doc comment%0A  > 5b19c55 Merge branch 'master' into sparsehistogram%0A  > dfbcc28 Merge pull request # 901 from prometheus/beorn7/histogram%0A  > 84fcaff Merge branch 'master' into sparsehistogram%0A  > 263be8d Refactoring of sparse histograms%0A  > 9ef5f90 Allow a zero threshold of zero%0A  > 2409960 Implement strategy to limit the sparse bucket count%0A  > aa6f67a Add TODO about bucket search optimization%0A  > 43f31c2 Merge pull request # 886 from prometheus/beorn7/histogram%0A  > 5aa8534 Merge branch 'master' into sparsehistogram%0A  > 5142344 Pin client_model to the most recent sparsehistogram commit%0A  > 97eb041 Tidy go.sum%0A  > 6c4e0ef Add tests for sparse histogram%0A  > 553ed73 Fix lint warning%0A  > 31318b7 Switch to base-2 buckets%0A  > b7a540a Fix test%0A  > a9df0ba Update prometheus/client_model%0A  > ce36ee3 Merge branch 'master' into beorn7/histogram%0A  > d698336 Merge branch 'master' into beorn7/histogram%0A  > 08104a0 Minor doc comment fixes%0A  > a9d0066 Add note about pow-of-10 precision issue%0A  > d1f5366 Fix span offset%0A  > abe540f Encode sparse histograms in protobuf%0A  > c98db4e Demo sparse histograms%0Abumping golang.org/x/text 71a9c9a...9db913a:%0A  > 9db913a go.mod: update to newer x/tools%0A  > 30dadde all: correct comment typos%0Abumping knative.dev/pkg dfad48e...6eb4b40:%0A  > 6eb4b40 Update community files (# 2760)%0A  > eb63a40 Support to set qps and burst via env variable (# 2755)%0A  > 74c4be5 Generate kresource duck type codegen (# 2754)%0A  > 4dbc312 fix boilerplate (# 2753)%0A  > 15605c7 Defaulting Controller options for all kind of webhooks (# 2738)%0A  > 94b81fc Update community files (# 2752)%0A  > 5671699 drop the dynamic type (# 2750)%0A  > 9bda38b Fix some webhook testing tech debt (# 2751)%0A  > ec20442 Update community files (# 2747)%0A  > 05bfcf6 bump k8s dependencies and update min version to v1.25 (# 2745)%0A  > 52ff2ac drop dynamic client wrappers (# 2744)%0A  > a170a07 Eventing TLS: validate that Destination.CACerts is a PEM encoded cert (# 2743)%0A  > dfb4bf0 Drop dynamic wrapper injection code generation (# 2742)%0A  > db8a353 Add SinkCACerts to SourceStatus (# 2733)%0A  > 9049667 Update community files (# 2735)%0A  > aacec7f Update community files (# 2734)%0A  > 300df43 Eventing TLS: Added AddressableFromDestination method on the resolver (# 2717)

Signed-off-by: Knative Automation <automation@knative.team>

---
## [LeXus21251/CDL](https://github.com/LeXus21251/CDL)@[9df359f2f4...](https://github.com/LeXus21251/CDL/commit/9df359f2f47bfadbb7804b3c3ea498f832b33b9e)
#### Tuesday 2023-07-04 15:16:21 by bartaz61

In Desert and Wilderness – Henryk Sienkiewicz

“Do you know, Nell,” said Stas Tarkowski to his friend, a little English girl, “that
yesterday the police came and arrested the wife of Smain, the overseer, and her three
children,—that Fatma who several times called at the office to see your father and mine.”
And little Nell, resembling a beautiful picture, raised her greenish eyes to Stas and asked
with mingled surprise and fright:
“Did they take her to prison?”
“No, but they will not let her go to the Sudân and an official has arrived who will see that
she does not move a step out of Port Said.”
“Why?”
Stas, who was fourteen years old and who loved his eight–year–old companion very
much, but looked upon her as a mere child, said with a conceited air:
“When you reach my age, you will know everything which happens, not only along the
Canal from Port Said to Suez, but in all Egypt. Have you ever heard of the Mahdi?”
“I heard that he is ugly and naughty.”
The boy smiled compassionately.
“I do not know whether he is ugly. The Sudânese claim that he is handsome. But the word
‘naughty’ about a man who has murdered so many people, could be used only by a little
girl, eight years old, in dresses—oh—reaching the knees.”
“Papa told me so and papa knows best.”
“He told you so because otherwise you would not understand. He would not express
himself to me in that way. The Mahdi is worse than a whole shoal of crocodiles. Do you
understand? That is a nice expression for me. ‘Naughty!’ They talk that way to babes.”
But, observing the little girl’s clouded face, he became silent and afterwards said:
“Nell, you know I did not want to cause you any unpleasantness. The time will come
when you will be fourteen. I certainly promise you that.”
“Aha!” she replied with a worried look, “but if before that time the Mahdi should dash
into Port Said and eat me.”
“The Mahdi is not a cannibal, so he does not eat people. He only kills them. He will not
dash into Port Said, but even if he did and wanted to murder you, he would first have to do
with me.”
This declaration with the sniff with which Stas inhaled the air through his nose, did not
bode any good for the Mahdi and considerably quieted Nell as to her own person.
“I know,” she answered, “you would not let him harm me. But why do they not allow
Fatma to leave Port Said?”
“Because Fatma is a cousin of the Mahdi. Her husband, Smain, made an offer to the
Egyptian Government at Cairo to go to the Sudân, where the Mahdi is staying, and secure
the liberty of all Europeans who have fallen into his hands.”
“Then Smain is a good man?”
“Wait! Your papa and my papa, who knew Smain thoroughly, did not have any confidence
in him and warned Nubar Pasha not to trust him. But the Government agreed to send
Smain and Smain remained over half a year with the Mahdi. The prisoners not only did
not return, but news has come from Khartûm that the Mahdists are treating them more and
more cruelly, and that Smain, having taken money from the Government, has become a
traitor. He joined the Mahdi’s army and has been appointed an emir. The people say that in
that terrible battle in which General Hicks fell, Smain commanded the Mahdi’s artillery
and that he probably taught the Mahdists how to handle the cannon, which before that
time they, as savage people, could not do. But now Smain is anxious to get his wife and
children out of Egypt. So when Fatma, who evidently knew in advance what Smain was
going to do, wanted secretly to leave Port Said, the Government arrested her with the
children.”
“But what good are Fatma and her children to the Government?”
“The Government will say to the Mahdi,—‘Give us the prisoners and we will surrender
Fatma’—”
For the time the conversation was interrupted because the attention of Stas was attracted
by birds flying from the direction of Echtum om Farag towards Lake Menzaleh. They flew
quite low and in the clear atmosphere could be plainly seen some pelicans with curved
napes, slowly moving immense wings. Stas at once began to imitate their flight. So with
head upraised, he ran a score of paces along the dyke, waving his outstretched arms.
“Look!” suddenly exclaimed Nell. “Flamingoes are also flying.”
Stas stood still in a moment, as actually behind the pelicans, but somewhat higher, could
be seen, suspended in the sky, two great red and purple flowers, as it were.
“Flamingoes! flamingoes! Before night they return to their haunts on the little islands,” the
boy said. “Oh, if I only had a rifle!”
“Why should you want to shoot at them?”
“Girls don’t understand such things. But let us go farther; we may see more of them.”
Saying this he took the girl’s hand and together they strolled towards the first wharf
beyond Port Said. Dinah, a negress and at one time nurse of little Nell, closely followed
them. They walked on the embankment which separated the waters of Lake Menzaleh
from the Canal, through which at that time a big English steamer, in charge of a pilot,
floated. The night was approaching. The sun still stood quite high but was rolling in the
direction of the lake. The salty waters of the latter began to glitter with gold and throb
with the reflection of peacock feathers. On the Arabian bank as far as the eye could reach,
stretched a tawny, sandy desert—dull, portentous, lifeless. Between the glassy, as if half–
dead, heaven and the immense, wrinkled sands there was not a trace of a living being.
While on the Canal life seethed, boats bustled about, the whistles of steamers resounded,
and above Menzaleh flocks of mews and wild ducks scintillated in the sunlight, yonder, on
the Arabian bank, it appeared as if it were the region of death. Only in proportion as the
sun, descending, became ruddier and ruddier did the sands begin to assume that lily hue
which the heath in Polish forests has in autumn.
The children, walking towards the wharf, saw a few more flamingoes, which pleased their
eyes. After this Dinah announced that Nell must return home. In Egypt, after days which
even in winter are often scorching, very cold nights follow, and as Nell’s health demanded
great care, her father, Mr. Rawlinson, would not allow her to be near the water after
sunset. They, therefore, returned to the city, on the outskirts of which, near the Canal,
stood Mr. Rawlinson’s villa, and by the time the sun plunged into the sea they were in the
house. Soon, the engineer Tarkowski, Stas’ father, who was invited to dinner arrived, and
the whole company, together with a French lady, Nell’s teacher, Madame Olivier, sat at the
table.
Mr. Rawlinson, one of the directors of the Suez Canal Company, and Ladislaus Tarkowski,
senior engineer of the same company, lived for many years upon terms of the closest
intimacy. Both were widowers, but Pani Tarkowski, by birth a French lady, died at the
time Stas came into the world, while Nell’s mother died of consumption in Helwan when
the girl was three years old. Both widowers lived in neighboring houses in Port Said, and
owing to their duties met daily. A common misfortune drew them still closer to each other
and strengthened the ties of friendship previously formed. Mr. Rawlinson loved Stas as his
own son, while Pan Tarkowski would have jumped into fire and water for little Nell. After
finishing their daily work the most agreeable recreation for them was to talk about the
children, their education and future. During such conversations it frequently happened that
Mr. Rawlinson would praise the ability, energy, and bravery of Stas and Pan Tarkowski
would grow enthusiastic over the sweetness and angelic countenance of Nell. And the one
and the other spoke the truth. Stas was a trifle conceited and a trifle boastful, but diligent
in his lessons, and the teachers in the English school in Port Said, which he attended,
credited him with uncommon abilities. As to courage and resourcefulness, he inherited
them from his father, for Pan Tarkowski possessed these qualities in an eminent degree
and in a large measure owed to them his present position.
In the year 1863 he fought for eleven months without cessation. Afterwards, wounded,
taken into captivity, and condemned to Siberia, he escaped from the interior of Russia and
made his way to foreign lands. Before he entered into the insurrection he was a qualified
engineer; nevertheless he devoted a year to the study of hydraulics. Later he secured a
position at the Canal and in the course of a few years, when his expert knowledge, energy,
and industry became known, he assumed the important position of senior engineer.
Stas was born, bred, and reached his fourteenth year in Port Said on the Canal; in
consequence of which the engineers called him the child of the desert. At a later period,
when he was attending school, he sometimes, during the vacation season and holidays,
accompanied his father or Mr. Rawlinson on trips, which their duty required them to make
from Port Said to Suez to inspect the work on the embankment or the dredging of the
channel of the Canal. He knew everybody—the engineers and custom–house officials as
well as the laborers, Arabs and negroes. He bustled about and insinuated himself
everywhere, appearing where least expected; he made long excursions on the
embankment, rowed in a boat over Menzaleh, venturing at times far and wide. He crossed
over to the Arabian bank and mounting the first horse he met, or in the absence of a horse,
a camel, or even a donkey, he would imitate Farys[Footnote: Farys, the hero of Adam
Mickiewicz’s Oriental poem of the same name.—Translator’s note.] on the desert; in a
word, as Pan Tarkowski expressed it, “he was always popping up somewhere,” and every
moment free from his studies he passed on the water.
His father did not oppose this, as he knew that rowing, horseback riding, and continual life
in the fresh air strengthened his health and developed resourcefulness within him. In fact,
Stas was taller and stronger than most boys of his age. It was enough to glance at his eyes
to surmise that in case of any adventure he would sin more from too much audacity than
from timidity. In his fourteenth year, he was one of the best swimmers in Port Said, which
meant not a little, for the Arabs and negroes swim like fishes. Shooting from carbines of a
small caliber, and only with cartridges, for wild ducks and Egyptian geese, he acquired an
unerring eye and steady hand. His dream was to hunt the big animals sometime in Central
Africa. He therefore eagerly listened to the narratives of the Sudânese working on the
Canal, who in their native land had encountered big, thick–skinned, and rapacious beasts.
This also had its advantage, for at the same time he learned their languages. It was not
enough to excavate the Suez Canal; it was necessary also to maintain it, as otherwise the
sands of the deserts, lying on both banks, would fill it up in the course of a year. The grand
work of De Lesseps demands continual labor and vigilance. So, too, at the present day,
powerful machines, under the supervision of skilled engineers, and thousands of laborers
are at work, dredging the channel. At the excavation of the Canal, twenty–five thousand
men labored. To–day, owing to the completion of the work and improved new machinery,
considerably less are required. Nevertheless, the number is great. Among them the natives
of the locality predominate. There is not, however, a lack of Nubians, Sudânese, Somalis,
and various negroes coming from the White and Blue Niles, that is, from the region which
previous to the Mahdi’s insurrection was occupied by the Egyptian Government. Stas
lived with all on intimate terms and having, as is usual with Poles, an extraordinary
aptitude for languages he became, he himself not knowing how and when, acquainted with
many of their dialects. Born in Egypt, he spoke Arabian like an Arab. From the natives of
Zanzibar, many of whom worked as firemen on the steam dredges, he learned Kiswahili, a
language widely prevalent all over Central Africa. He could even converse with the
negroes of the Dinka and Shilluk tribes, residing on the Nile below Fashoda. Besides this,
he spoke fluently English, French, and also Polish, for his father, an ardent patriot, was
greatly concerned that his son should know the language of his forefathers. Stas in reality
regarded this language as the most beautiful in the world and taught it, not without some
success, to little Nell. One thing only he could not accomplish, that she should pronounce
his name Stas, and not “Stes.” Sometimes, on account of this, a misunderstanding arose
between them, which continued until small tears began to glisten in the eyes of the girl.
Then “Stes” would beg her pardon and became angry at himself.
He had, however, an annoying habit of speaking slightingly of her eight years and citing
by way of contrast his own grave age and experience. He contended that a boy who is
finishing his fourteenth year, if he is not fully matured, at least is not a mere child, but on
the contrary, is capable of performing all kinds of heroic deeds, especially if he has Polish
and French blood. He craved most ardently that sometime an opportunity would occur for
such deeds, particularly in defense of Nell. Both invented various dangers and Stas was
compelled to answer her questions as to what he would do if, for instance, a crocodile, ten
yards long, or a scorpion as big as a dog, should crawl through the window of her home.
To both it never occurred for a moment that impending reality would surpass all their
fantastic suppositions.

---
## [dubwub/mern-stack-boilerplate](https://github.com/dubwub/mern-stack-boilerplate)@[297366e2b5...](https://github.com/dubwub/mern-stack-boilerplate/commit/297366e2b578ae679bb13d918c910f83ddf1c9bb)
#### Tuesday 2023-07-04 15:19:56 by dubwub

fuck yeah its working with typescript and ESnext. good shit

---
## [ariel-miculas/puzzlefs](https://github.com/ariel-miculas/puzzlefs)@[decc2634f2...](https://github.com/ariel-miculas/puzzlefs/commit/decc2634f2ec255858b8bbf0e94278e8449094a1)
#### Tuesday 2023-07-04 15:59:42 by Ariel Miculas

Change the metadata serialization from cbor to capnproto

Capnproto [1] is a fast data interchange format which uses zero-copy
serialization, meaning there is no encoding/decoding step.

Advantages over cbor:
* it removes the custom fixed-length serialization for the inode vector
* it removes the streaming deserializer hack (used because we leave
  extra bytes on the wire)
* it removes the artificial splitting of the Inode structure (a
  low-level Inode which stores the offset to its additional data and a
  high-level Inode structure which rebuild the data at runtime)
* it removes the custom serialization code used to compute the offsets
  of the data structures on the wire (and also having to deal with the
  specifics of the cbor encoding format)
* the encoding format splits the structures into two sections [2], data
  and pointers, which is similar to our strategy of storing offsets into
  the low-level Inode structure, so we could efficiently store the vector
  of Inodes at the beginning of our metadata file; however, Capnproto
  handles this serialization for us
* the format is not self-describing (it uses a schema language in which
  you must describe your data), so it should takes less space on disk
* it allows schema evolution, which means we can add new fields to our
  schema over time, without breaking backwards-compatibility [3]

Disadvantages:
* while the Capnproto format itself doesn't require encoding/decoding,
  it also doesn't generate Rust structures, which means that every field
  access must be done through getters and setters; to make my life
  easier, I've written from_capnp and to_capnp functions for each
  structure, so I could create a Rust structure from the in-memory Capnp
  serialization format; however, this also means that my implemenentation
  is not zero-copy, since it needs to allocate Rust structures; anyway,
  this implemenentation is similar to what was done with the cbor
  serialization, so it shouldn't be less performant; Kent Overstreet
  also had some suggestions for improvement [4]
* there is no support for specifying required or optional fields in the
  format, so the data validation onus is on the user of the library; on
  the other hand, this could be an advantage because it allows greater
  flexibility (we don't need to wrap the structure into an Option if we
  decide it's not required, e.g. fs verity data)

Other changes:
* BlobRef now always holds a digest, it never refers to an offset in the
  same file

For a Ubuntu 20.04 distribution (single layer puzzlefs image) the amount
of space taken by the metadata is:
Cbor serialization:
puzzlefs manifest: 869K
puzzlefs metadata layer: 4.2M

Capnproto serialization:
puzzlefs manifest: 662K
puzzlefs metadata layer: 3.8M

https://capnproto.org/ [1]
https://capnproto.org/encoding.html#structs [2]
https://capnproto.org/news/2014-06-17-capnproto-flatbuffers-sbe.html [3]
https://lore.kernel.org/rust-for-linux/20230609063118.24852-1-amiculas@cisco.com/T/#m22c3db8ba98f2905204d587563ef116a97ce0415 [4]

Fixes #18

Signed-off-by: Ariel Miculas <amiculas@cisco.com>

---
## [phorgeit/phorge](https://github.com/phorgeit/phorge)@[80484b76a5...](https://github.com/phorgeit/phorge/commit/80484b76a5ff815a4f4849e2899fe39650bcd560)
#### Tuesday 2023-07-04 16:23:27 by Valerio Bozzolan

Remarkup Code-block: parse language specifier in markdown

Summary:
We add support to code blocks with the language expressed as GitLab/GitHub/StackOverflow/...
"flavored markdown".

So we support this syntax: (to avoid confusion see it online on the Diff)

    lang=text
    ```php
    $asd = 1;
    ```

Before this change, this was the only supposed syntax in Remarkup, with an explicit "lang=":

    lang=text
    ```lang=php
    $asd = 1;
    ```

This change introduces a minor risk to eat legitimate Remarkup content, since Remarkup allows
to do a multi-line in this way:

    lang=text
    ```$asd = 1;
    $asd = 2;```

The above example still works, but, there is a chance that hardcore Remarkup people
have a problem when doing a code block to mention programming languages.

In short, this can be problematic since "cpp" will be eaten from this list:

    COUNTEREXAMPLE
    ```cpp
    php
    python
    ```

Using the above example is not socially nice because it is not usable in GitLab, GitHub and Stack Overflow.

If your first line is eaten:

Just *add* a newline on the top to reach a valid raw Markdown list (suggested, valid in Remarkup + Markdown):

    lang=text
    ```
    cpp
    php
    python
    ```

Or, just add "text" to specify that as language (suggested, valid in Remarkup + Markdown):

    lang=text
    ```text
    cpp
    php
    python
    ```

Or, just *remove* a newline from the bottom to reach a valid raw Remarkup list (Remarkup-only):

    lang=text
    ```cpp
    php
    python```

Or, just specify that you are writing in the language "text" (Remarkup-only):

    lang=text
    ```lang=text
    cpp
    php
    python```

To reduce impact and help you, the logic of this strict implementation is:

- must have backticks
- must not have any valid remarkup option, like lang=, counterexample, etc.
- must not have content in the same line of the last backticks
- must have a known language in our proposed subset

If everything is OK, we remove that language from the content since it would be otherwise displayed.

Interestingly, this could improve performance when rendering README files or snippets from external
websites, since - in case - we do not need to guess the language using our deep dark magic.

Closes T15481

Test Plan:
We added some nice unit tests. Ensure that this test passes:

    PhutilRemarkupEngineTestCase::testEngine

Optionally, take vision of these, before and after:

https://we.phorge.it/P16

Change the test plan slightly every time, to make sure it is not in your cache.

Reviewers: O1 Blessed Committers, avivey

Reviewed By: O1 Blessed Committers, avivey

Subscribers: avivey, speck, tobiaswiese, Matthew, Cigaryno

Maniphest Tasks: T15481

Differential Revision: https://we.phorge.it/D25299

---
## [ajay-praveen4502/Java-Fundamentals-Challenges](https://github.com/ajay-praveen4502/Java-Fundamentals-Challenges)@[5c3ceedbdd...](https://github.com/ajay-praveen4502/Java-Fundamentals-Challenges/commit/5c3ceedbdd66474c57ed35f5bb0778db12bbd8f1)
#### Tuesday 2023-07-04 16:34:18 by Ajay Praveen

Insomnia Cure

"One dragon. Two dragon. Three dragon", — the princess was counting. She had trouble in falling asleep, and she got bored of counting lambs when she was nine.

However, just counting dragons was boring as well, so she entertained herself at best she could. Tonight she imagined that all dragons were here to steal her, and she was fighting them off. Every k-th dragon got punched in the face with a frying pan. Every l-th dragon got his tail shut into the balcony door. Every m-th dragon got his paws trampled with sharp heels. Finally, she threatened every n-th dragon to call her mom, and he withdrew in panic.

Write a program to find how many imaginary dragons suffered moral or physical damage tonight, if the princess counted a total of d dragons?

INPUT & OUTPUT FORMAT:
Input data contains integer numbers k, l, m, n and d, each number in a separate line (1 ≤ k, l, m, n ≤ 10, 1 ≤ d ≤ 105).
The output displays the number of damaged dragons.

SAMPLE INPUT & OUTPUT 1:
1
2
3
4
12
12

SAMPLE INPUT & OUTPUT 2:
2
3
4
5
24
17

---
## [carlarctg/tgstation](https://github.com/carlarctg/tgstation)@[64eae49042...](https://github.com/carlarctg/tgstation/commit/64eae49042dea956b46ae013a0c96a891c026a7f)
#### Tuesday 2023-07-04 16:58:52 by necromanceranne

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
## [Bjarl/Shiptest](https://github.com/Bjarl/Shiptest)@[9aa3fb2901...](https://github.com/Bjarl/Shiptest/commit/9aa3fb29012991ce7a9d755e640a1af65f3fe319)
#### Tuesday 2023-07-04 17:14:03 by thgvr

Fixes a good chunk of Vox sprites. Removes environmental regulator (#2092)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Oh god the pain. Oh god. The unbearable pain. Why.

Adds a ton of unused vox sprites from Drawsstuff.
Cleans up the files for sprites we don't actually have
Ensures they are pathed correctly, with flags set correctly.
I spent five hours on this in one sitting after being upset at shitty
vox mechanics/sprite support again. They're cool and unique and it was
sad.
Removes the Environmental Regulator.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
1. Vox sprites were incomplete. This completes them a little bit more.
2. The environmental regulator isn't fun. This will remove the regulator
and vox needing to use it. It was buggy, poorly made, and just not fun
even when it worked correctly. Vox aren't nearly strong enough to be
constantly crippled.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: A metric ton of Vox sprites
del: Vox no longer need environmental regulators
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Bjarl/Shiptest](https://github.com/Bjarl/Shiptest)@[c84e40255d...](https://github.com/Bjarl/Shiptest/commit/c84e40255d466e37983e5cb03c110e7dd8ab90c8)
#### Tuesday 2023-07-04 17:14:03 by Imaginos16

Ports pinging in Adminsay from /tg/station (#2111)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Does what it says on the tin, porting a behavior that allows you to ping
a person in admin say by just doing @(ckey) from /tg/station in PR
[#61712](https://github.com/tgstation/tgstation/pull/61712)


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/fc756e0f-668f-4641-9bcd-689d6548d343)

Oh and this PR I guess fixes a hilarious issue where **someone** wrote
'tgstation.dme' instead of 'shiptest.dme' where they shouldn't have.
Whoops!

Most cool of all, which was completely unintentional by me, ports Datum
linking (partially), as well as Ticket linking, respectively added in
PRs [#65154](https://github.com/tgstation/tgstation/pull/65154) and
[#65634](https://github.com/tgstation/tgstation/pull/65634)


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/d6f980ee-c490-4f8d-a76c-81447aeb7658)



<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
I swear to fucking christ if I have to log into the game one more
goddamn time as an admin only to have 2 people being DJs, another one
spriting, and another one doing jack shit while not paying attention at
the server when I am trying to solve a crucial ticket, I'll develop an
aneurysm.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: Ryll-Ryll/Shaps
admin: Adds pinging to adminsay!
admin: Adds the ability to link datums!
admin: Adds linking tickets to asay! Simply put a # followed by a ticket
number for it to be linked in the chat!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [CADindustries/toolcad-23](https://github.com/CADindustries/toolcad-23)@[b23efeb146...](https://github.com/CADindustries/toolcad-23/commit/b23efeb146a98db5d8c9eb392748013ee780ddeb)
#### Tuesday 2023-07-04 17:33:55 by Airat

Removed previewWindow because of cringe competition fuck this shite, I should create my own SoftHub

---
## [pyjamaproggers/soundcheck-backend](https://github.com/pyjamaproggers/soundcheck-backend)@[f3afb25db0...](https://github.com/pyjamaproggers/soundcheck-backend/commit/f3afb25db07ce5807ba963134961406948c382ad)
#### Tuesday 2023-07-04 18:38:12 by Zahaan Shapoorjee

I hate my life I hate MongoDB I hate everything added database login with JWT token and logout functionality that clears cookies as well as add post, delete post, edit post, and view post functionality (I'm so lonely)

---
## [delingar/FluffySTG](https://github.com/delingar/FluffySTG)@[9e523715ac...](https://github.com/delingar/FluffySTG/commit/9e523715acd373ce1a74bdc8f9c2fe422c2ad61e)
#### Tuesday 2023-07-04 18:49:38 by SkyratBot

New planetary exclusive random event/unfavorable situation, Chasmic Earthquake [MDB IGNORE] (#21778)

* New planetary exclusive random event/unfavorable situation, Chasmic Earthquake (#75864)

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

* New planetary exclusive random event/unfavorable situation, Chasmic Earthquake

---------

Co-authored-by: Rhials <Datguy33456@gmail.com>

---
## [nitelitevtuber/Onsenka](https://github.com/nitelitevtuber/Onsenka)@[50e79f72ab...](https://github.com/nitelitevtuber/Onsenka/commit/50e79f72ab0d0f166f40f137e92a97024467e71d)
#### Tuesday 2023-07-04 19:22:08 by nitelite

3 ACTUAL FUCKING BUTTONS (temp until i get my shit together)

HOLY SHIT!!!

---
## [wileyhy/MCprep](https://github.com/wileyhy/MCprep)@[a34b01aa69...](https://github.com/wileyhy/MCprep/commit/a34b01aa69f7e215a0cd6ec46665e1c15a0a78ca)
#### Tuesday 2023-07-04 20:12:34 by mahid

Added type annotations and use of Path
Replaced some instances of os.path with the Path object from pathlib for
readability. Also added type annotations to MCprepEnv as we're moving
towards that. This also means MCprep will not work at all in Blender
2.7x due to the use of new syntax.

This will be the first in a long process of modernizing MCprep's code
with 2.8 style code. Blender 2.7x users may not be happy, but it's for
the better. If anything, 6 years worth of 2.7x support was a mistake (in
my opinion), as it limited what we could do and opened MCprep to even
more bugs (like in Blender 2.93 with make_annotations, which ironically
now is deprecated).

---
## [LanceSmites328/LC13Master](https://github.com/LanceSmites328/LC13Master)@[582f5b38cb...](https://github.com/LanceSmites328/LC13Master/commit/582f5b38cb9ad5d051cbea48af501089ba3f0206)
#### Tuesday 2023-07-04 20:39:08 by Lance

Holy FUCK temporary commit

Mixed between previous abno based spawning and new subsystem

Cleanup Commit

Removes a lot of previous code and paves the way for the subsystem method.

Major Commit

Apocalypse Bird drops it's loot and only spawns once. It'll not try to happen if there aren't enough birds, and if two are breached before the third arrives it'll take the third breaching to start the event, until the others are suppressed. Birds do not target people and are immortal while moving to the portal. If unable to reach it after 3 minutes they'll be forced in manually.

Tweaked Proc

Redundant Code Removal

Remembered I didn't need this

Enhanced Code

Moved an if-statement to a better place to more adequately solve the issue.

Test Commit

Does this solution work?

Global Abnormality Mob List

Patrol Changes and Bird Grab changes

Gaming Test?

Temp Commit

Second Commit

Another Commit!

Fourth Commit

Subsystem changes. Dead abno cleansing. Lower speak cooldown. Debug text removal.

P-bird fix

Fixes P-bird able to die before reaching the portal

---
## [Sakooooo/nixos](https://github.com/Sakooooo/nixos)@[d8eee9ce09...](https://github.com/Sakooooo/nixos/commit/d8eee9ce093fe863f53874d944935e1f5a5b3a45)
#### Tuesday 2023-07-04 20:55:07 by Sakooooo

Humans prefer the dark for sleeping because
of how we are created. We are meant to sleep
at night because we are Mammals Probably
I dont know if i can write a commit message this long at a jbo
job* but this would be really fun
guys ow do i stop a zsh quote
GUYS
please
HELP
ITS POT =STOPPING PLASE HELP
OH MY GOD
Oh found it

---
## [JeromeFitz/websites](https://github.com/JeromeFitz/websites)@[e927742292...](https://github.com/JeromeFitz/websites/commit/e927742292832b99f43b1e24311943626b415cbb)
#### Tuesday 2023-07-04 22:51:05 by Jerome Fitzgerald

🧨 (revamp) NICE-43 Next RSC, Notion API, & Tailwind [b] [!] (#1621)

# ⚠️ Please Note

This is a bit bigger than I would want, but this is a complete refactor to better utilize a `Notion CMS` within a `Next 13 App` structure taking advantage of `RSC`. And then for good measure started the migration _back_ to `Tailwind` (but now I think `Stitches|Vanilla Extract` are oaky with Next 13).

✨ NICE-43 revamp Next RSC, Notion API, & Tailwind

BREAKING CHANGE: New Notion Implementation through Next 13 RSC (App)

# Complete Refactor for Next RSC

- [x] Redis KV Cache
  - Good for quicker Vercel builds / and reducing Notion random limits
  - Next will still limit due to deduplicated requests
    - Sidenote: Need to get better at _not_ prop-drilling and just calling function again
- [x] Image Component
  - [x] Next Refactor
  - [x] Notion Refactor
- [x] Tailwind
  - [x] Move away from Stitches
  - [x] Temporary move to `@jeromefitz/ds` localized version
  - [x] Radix UI Refactor
  - [x] Use internal Component Library for now
- [x] Notion Refactor

  - [x] Image: Hosted by Notion Expiration Refresh
  - [x] Rely less on custom queries and manipulation, more on out of the box Notion API, React, and Next
    - [x] Move from `nodes` to more straight-forward components
    - [x] Refactor logic for
      - [x] `Column|ColumnList`
      - [x] `ListBulleted|ListItem|ListNumbered`
      - [x] `TextAnnotations`
    - [x] **New**: `Embed|Video`
      - [x] `Embed.Twitter` <= Twitter is self-imploding, so good timing.
      - [x] `Embed.YouTube` <= YouTube is ... no comment.

- [x] Next
  - [ ] `preload` => hold on this for now not working as expected
  - [x] `generateMetadata` => move away from `next-seo` (rip)
    - [ ] Need to re-incorporate `@vercel/og` -- or not temporarily.
  - [x] `generateStaticParams` => hack if `isDev` to stop running all the time :?
  - [x] `not-found` => Instead of customizing every route, use `notFound()`
  - [x] `robots.ts|sitemap.ts` => move away from `next-sitemap` (rip)
- [x] Package Upgrades
  - [x] Basically everything except `plaiceholder|semantic-release|syncpack`
- [x] Other refactors
  - [x] EmojiWrapper
  - [x] Config Packages
    - [x] `./packages/*` – this all needs to be ported to [`@jeromefitz/packages`](https://github.com/JeromeFitz/packages)
      - Was borderline impossible to do these in-tandem (need to get better at `pnpm linking`)
- [x] Fathom advises against custom domains now :/

## Layout

Not to be lost in the backend type stuff but this is a complete rehaul of presentation.

The eventual goal of this `Notion + Next` implementation is you can take the data in any way and display it as you would like. For now though still tightly coupled with a lot of decisions until I can abstract away further. Which -- at teh rate I am going may never happen.

## Notion

Do not "normalize" data from Notion, embrace it.

- This is the CMS why are we going through all the trouble to hack it
- Create new Block Components to match and mimic needs

### Formulas

The "big change" here is utilizing Notion Formulas in the CMS.

#### Slug

Before we had `Slug` now we populated `Slug.Preview` where we are able to have Notion mimic Routes better Server Side than figuring it all out on the fly in `next`.

**Note:** For `Events` we need to manually write the `Slug` for now. The potential clash of having multiple Headline Acts means we could have a url like:

- `../jerome-and,alex-o-jerome`

Which I think _could_ work because we could loop through but also _very_ confusing as a URL to share, haha.

To recap:

- `Slug.Preview` for example will create the matching Next Segment Route
  - Before: `jerome-and` (shows); After: `/shows/jerome-and`
  - Before: `jerome-and` (events); After: `/events/2023/06/16/jerome-and`
  - Before: `homepage` (pages); After: `/`

##### Date

Same here, instead of getting the data from Notion then running through `date-fns`, Notion uses `moment` (I think). So we can do more preparation which makes for a more straight-forward:

```bash
- Date: July 15, 2023 9:00PM
- Date.DayOfMonth: 15
- Date.DayOfMonthOrdinal: 15th
- Date.DayOfWeek: Saturday
- Date.DayOfWeekAbbr: Sat
- Date.DaysUntilEvent: 15
- Date.HoursUntilEvent: 360
- Date.ISO: 2023-07-15T21:00:00-04:00
- Date.Month: 07
- Date.MonthName: July
- Date.MonthNameAbbr: Jul
- Date.Time: 09:00 PM
- Date.Timezone: EDT
- Date.WeekNumber: 28
- Date.Year: 2023
```

## Next

### App

The gains of doing `[[...catchAll]]` for everything at **root** was not worth it. 😅

Especially if we _want_ to be able to change layout, RSC data points and more based on the Segment (Notion Database Type).

So there is some duplication of code throughout but will look into better ways of lifting the "same" stuff.

### Events

Ability to see a range of events depending on Date (say for a week, or a weekend):

- `events/yyyy/mm/dd/to/yyyy/mm/dd`
- `events/2023/06/29/to/2023/07/02`

Props to Katie T. as we came up with this idea in a brainstorm session.

- `events/[from]/to/[to]`
- `events/2023/06/15/to/2023/06/18` (THU-SUN)
- `events/2023/06/29/to/2023/05/01` (Across Months)
- `events/2023/12/28/to/2025/01/07` (Across Years)

Probably need to do something for malformed dates, but I reckon `404` will do that.

Up next would be ideas for `Landing Pages`.

### In-House

`next-seo` and `next-sitemap` will eventually be absorded, or their functionality at least, within `next` itself. This gets the ball rolling on that. They were awesome, and thank you.

Depending on your use case those will still be very valid for use!

## Packages

This just covers the `sites/jeromefitzgerald.com` for now

**Upgrade:**
```bash
@mantine/hooks@6.0.15
@notionhq/client@2.2.6
@radix-ui/...@latest
@upstash/redis@1.22.0
@vercel/og@0.5.8
framer-motion@10.12.18
next@13.4.8-canary.14
react-swipeable@7.0.1
swr@2.2.0

@types/ramda@0.29.3
@types/react@18.2.14
@types/react-dom@18.2.6
@types/uuid@9.0.2
tailwind-merge@1.13.2
```

**Add:**

```bash
emoji-regex@10.2.1
node-emoji@2.1.0
react-headroom@3.2.1 # use framer-motion instead
react-tweet@2.0.2 # 3.x has no release notes

@types/react-headroom@3.2.0
```

**Remove:**

```bash
next-seo
next-sitemap
next-unused
```

---
## [mgarlanger/mame](https://github.com/mgarlanger/mame)@[2bcd9bc772...](https://github.com/mgarlanger/mame/commit/2bcd9bc772b4f3cc6e8b281703e53561d2c5bea9)
#### Tuesday 2023-07-04 23:04:16 by David 'Foxhack' Silva

segacd.xml, megacdj.xml: Added various CD dumps. (#11344)

New working software list items
-------------------------------
segacd.xml:
Compton's Interactive Encyclopedia v2.00S (USA) [redump.org]
Note! Color Mechanica (USA) [redump.org]
Note! Color Mechanica (USA, alt) [redump.org]
What is X'Eye Multi Entertainment System (USA) [redump.org]
megacdj.xml:
Heavenly Symphony - Formula One World Championship 1993 Hibaihin (Japan) [redump.org]
Keiou Yuugekitai Taikenban Hibaihin (Japan) [redump.org]
Lunar - Eternal Blue Hibaihin Auto Demo (Japan) [redump.org]
Microcosm Demo CD (Japan) [redump.org]
Night Trap Hibaihin (Japan) [redump.org]
Popful Mail Taikenban Hibaihin (Japan) [redump.org]
Silpheed Hibaihin (Japan) (Fixed) [redump.org]
Sonic The Hedgehog CD Hibaihin (Japan) [redump.org]
Thunderhawk Hibaihin (Japan) [redump.org]
Urusei Yatsura - Dear My Friends Hibaihin (Japan) [redump.org]
Yumemi Yakata no Monogatari Hibaihin (Japan) [redump.org]
WonderMega Collection - Game Garden (Japan, alt) [redump.org]

New software list items marked not working
------------------------------------------
segacd.xml:
Surgical Strike (Brazil, 32X) [redump.org]
megacdj.xml:
Psychic Detective Series vol.3 - AYA Auto Demo (Japan) [redump.org]
Silpheed Hibaihin (Japan) [redump.org]

---

