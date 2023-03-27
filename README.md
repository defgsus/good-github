## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-03-26](docs/good-messages/2023/2023-03-26.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,003,026 were push events containing 3,440,362 commit messages that amount to 201,050,092 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 65 messages:


## [Impossible-Robotics-5412/linkage](https://github.com/Impossible-Robotics-5412/linkage)@[fecd0dddf0...](https://github.com/Impossible-Robotics-5412/linkage/commit/fecd0dddf00ccc324520b2580f546b24ef562052)
#### Sunday 2023-03-26 00:07:55 by BaukeWestendorp

Bob: Change 'build all' order

On the Pi building Cockpit-frontend fucking sucks and takes longer
than the average Pink Floyd song.
Let's just procrastinate building it...

---
## [gmlarumbe/melpa](https://github.com/gmlarumbe/melpa)@[4872ef038d...](https://github.com/gmlarumbe/melpa/commit/4872ef038dbbf67008bfa7951574ee372d6ff68d)
#### Sunday 2023-03-26 00:42:55 by Jonas Bernoulli

Distribute all back-ends with the emacsql package

There are two reasons for this.

- Going forward, packages that use `emacsql' and SQLite should use
  the best back-end that can be used with the Emacs instance in use,
  either `emacsql-sqlite-builtin`, `emacsql-sqlite-module`, or as a
  last resort `emacsql-sqlite'.

  That means that if we didn't bundle the back-end libraries with
  `emacsql' itself, these packages would have to depend on all three
  back-end packages in addition to `emacsql' itself.  (Alternatively
  they could not depend on any of the back-end packages, and instead
  make the user install the appropriate back-end, when they try to
  use the package.  That's a bad user experience and there likely
  would be bugs, making it even more painful.)

- EmacSQL is now distributed on NonGNU Elpa as well.  While we at
  Melpa encourages the creation of separate packages for optional
  extensions (which are not useful to all users, or which have
  additional dependencies) the Emacs maintainers prefer everything to
  be distribute as one package, even if that means that `defvar' and
  `declare-function' declarations are necessary to keep the compiler
  happy.

  I still think our way is usually better, but since three of the
  back-end libraries have to be distributed with the main package
  anyway, we might as well give in here and bundle the other three
  as well.

For the time being, we have to continue to *also* distribute the
back-end libraries as separate packages.

Several third-party packages depend on the existing `emacsql' and
`emacsql-sqlite' packages.  These packages should be updated to only
depend on `emacsql', but the latest released versions of these
packages will continue to depend on `emacsql-sqlite' as well.  If we
removed the recipe for that, that would remove the latest release of
that package from Melpa, not just the snapshot version.

This is the current roadmap:

0. Include all back-ends in `emacsql'.
1. Update dependant packages to only depend on `emacsql'.
2. Make changes to `emacsql', which are enabled by the former two
   steps, and which are blocking the creation of a new `emacsql'
   release.  (These changes are related to the addition of the
   additional SQLite back-ends.  So this is a bit of a chicken and
   egg problem, and this commit (0) is the first step to break out
   of that.)
3. Create an `emacsql' release.
4. Wait for new releases of all dependant packages.
5. Change the separate back-end packages to warn the user, asking
   them to remove all of these packages.
6. After waiting some more, remove the separate back-end packages.

While a back-end is installed as part of `emacsql' and as a separate
package, it is undefined which version is loaded, but until step (5)
the two versions should be the same, so it doesn't matter.

---
## [Gooseus/evals](https://github.com/Gooseus/evals)@[ab5f7b2a89...](https://github.com/Gooseus/evals/commit/ab5f7b2a89bcf60e8e93adfb2c70688c6d6ffd44)
#### Sunday 2023-03-26 00:59:07 by oscar-king

Counting bigrams in sentences (#302)

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
Bigram Counting

### Eval description

Tests whether the model is able to count the frequency of bigrams in a
sentence.

### What makes this a useful eval?

This is a very simple task for humans and it's possibly slightly more
'difficult' than counting the occurrences of a single letter.

Bigram frequencies are used in applications ranging from rudimentary NLP
tasks to cryptography.

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
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"I'm
worried by the fact that my daughter looks to the local carpet seller as
a role model."}],"ideal":"0"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"He
found rain fascinating yet unpleasant."}],"ideal":"1"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"The
near-death experience brought new ideas to light."}],"ideal":"0"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the
frequency."},{"role":"user","content":"Separation anxiety is what
happens when you can't find your phone."}],"ideal":"0"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"He
realized there had been several deaths on this road, but his concern
rose when he saw the exact number."}],"ideal":"0"}
  ```
</details>

---
## [Gooseus/evals](https://github.com/Gooseus/evals)@[b170a21cf3...](https://github.com/Gooseus/evals/commit/b170a21cf32c47d841f64ec110cfd6796ec3f89a)
#### Sunday 2023-03-26 00:59:07 by Sam Ennis

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
## [Gooseus/evals](https://github.com/Gooseus/evals)@[b5da073c21...](https://github.com/Gooseus/evals/commit/b5da073c215c6453b99269a6dab2dca5454f04dd)
#### Sunday 2023-03-26 00:59:07 by somerandomguyontheweb

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
## [ArcaneMusic/TG-Station-Arcane-Remix](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix)@[8d7db532c0...](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix/commit/8d7db532c0f425e6cc68d975b526694bbaefc870)
#### Sunday 2023-03-26 01:33:37 by Bloop

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
## [LyamBRS/BRS-Kontrol](https://github.com/LyamBRS/BRS-Kontrol)@[e8947fe29f...](https://github.com/LyamBRS/BRS-Kontrol/commit/e8947fe29fa07949d019cd95448f18791d2ec887)
#### Sunday 2023-03-26 01:50:17 by Lyam[BRS]

Drivers card are now added but the hitbox is fucking ridiculous and I cant fucking fix the shit

---
## [CLimeburner/Iconic-Affordance-Interactions](https://github.com/CLimeburner/Iconic-Affordance-Interactions)@[37d8b2f538...](https://github.com/CLimeburner/Iconic-Affordance-Interactions/commit/37d8b2f5382a5e1a042f84fa43e9c7a9a20d571d)
#### Sunday 2023-03-26 02:02:25 by CLimeburner

Added more explicit IP or reference for various activities in the BlueSkyBrainstorming document.

As went about filling in some of the gaps for more abstract interactions, I realized I'd already mentioned a decent number of specific IP or listed interactions that are intrinsically tied to one IP (such as Super Mario), however I also realized I may have already made precisely the mistake I set out to avoid by listing affordances more so than specific IP or theme interactions. For example, I listed things like "flying" and then tried to reverse engineer cultural touch-points for it, when really I should have started with "dragons" or "Top Gun" and extracted flying from those popular subjects. I don't know if I have to abandon this list entirely, but I'm thinking I may actually need to take a step back from it, and perhaps reorient toward extracting affordances from a list of top 20 video games or movies.

On a separate point, I ended up with "fire breathing" on my list of interactions, and while I was initially envisioning the circus act when I added it to the list, it occurs to me it might be a kinda fun way of attacking in a 1st person dragon experience. Combining some sort of haptic flying simulation and fire breathing by blowing actuation might actually produce a somewhat compelling, if unorthodox, game where you play as a dragon. As such, while I continue to explore the blue sky domain of idea, I think I might also start some ideation for how this specific interaction might be realized, which if for no other reason will allow me to start exploring how best to document a more tangible game with this commit-oriented methodology.

---
## [WindSoilder/nushell](https://github.com/WindSoilder/nushell)@[0567407f85...](https://github.com/WindSoilder/nushell/commit/0567407f853c23f54215020a10f4a831ae2aef47)
#### Sunday 2023-03-26 02:46:41 by Antoine Stevan

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
## [TheOneTheOnlySpoopyBoi/Apotheosis](https://github.com/TheOneTheOnlySpoopyBoi/Apotheosis)@[bebc644a28...](https://github.com/TheOneTheOnlySpoopyBoi/Apotheosis/commit/bebc644a2895ca78a4d3cb30b13e4491b3cf47a2)
#### Sunday 2023-03-26 03:16:46 by Conga Lyne

New Material, Balances Changes, Fixes

New Material: Veloium
Water Spheres can now cool down molten metals
Nerfed Liquid sphere spells to hit every 10 frames instead of every 1
Spells to Power now only spawns in tier 10 locations
Doubled the spawnrate of Esoteric Beings inside the "You feel an undescribable aura" biome modifier
Omega Death Cross is now a bit more deathly...
Added Flummoxium + Attunium = Veloium
Added Slime + Veloium = Attunium
Slightly increased the spawnrate of rare eggs
Poisonous Gas now harms the player
Spells to Power now only spawns in Heaven, Hell & Other tier 10 spell pools; the goal behind this is StP is a very endgame spell capable of insanely high Damage output, if you want endgame damage spells, you need to visit endgame biomes
Removed Flummoxium + Concentrated Mana = Attunium Recipe (main concern is cross-mod compatibility with other alchemy mods)
Fixed fading water not being converted to Concentrated Mana, something particularly noticeable when Aquamines detonated

---
## [haploeco/dwm](https://github.com/haploeco/dwm)@[67d76bdc68...](https://github.com/haploeco/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Sunday 2023-03-26 04:32:31 by Chris Down

Do not allow focus to drift from fullscreen client via focusstack()

It generally doesn't make much sense to allow focusstack() to navigate
away from the selected fullscreen client, as you can't even see which
client you're selecting behind it.

I have had this up for a while on the wiki as a separate patch[0], but
it seems reasonable to avoid this behaviour in dwm mainline, since I'm
struggling to think of any reason to navigate away from a fullscreen
client other than a mistake.

0: https://dwm.suckless.org/patches/alwaysfullscreen/

---
## [ArturoKuang/GoPlayground-](https://github.com/ArturoKuang/GoPlayground-)@[b2fa3c3740...](https://github.com/ArturoKuang/GoPlayground-/commit/b2fa3c3740a9d7c0a31a5ec696ca5a3745332236)
#### Sunday 2023-03-26 06:00:37 by Arturo Kuang

Wrapping up
We've covered a few things from the sync package
Mutex allows us to add locks to our data
WaitGroup is a means of waiting for goroutines to finish jobs
When to use locks over channels and goroutines?
We've previously covered goroutines in the first concurrency chapter which let us write safe concurrent code so why would you use locks? The go wiki has a page dedicated to this topic; Mutex Or Channel
A common Go newbie mistake is to over-use channels and goroutines just because it's possible, and/or because it's fun. Don't be afraid to use a sync.Mutex if that fits your problem best. Go is pragmatic in letting you use the tools that solve your problem best and not forcing you into one style of code.
Paraphrasing:
Use channels when passing ownership of data
Use mutexes for managing state
go vet
Remember to use go vet in your build scripts as it can alert you to some subtle bugs in your code before they hit your poor users.
Don't use embedding because it's convenient
Think about the effect embedding has on your public API.
Do you really want to expose these methods and have people coupling their own code to them?
With respect to mutexes, this could be potentially disastrous in very unpredictable and weird ways, imagine some nefarious code unlocking a mutex when it shouldn't be; this would cause some very strange bugs that will be hard to track down.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[2e5bfe5be6...](https://github.com/tgstation/tgstation/commit/2e5bfe5be669d5222b68c7318349c4ac0947722b)
#### Sunday 2023-03-26 06:21:07 by LemonInTheDark

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
## [HighlanderRobotics/scouting_dashboard_app](https://github.com/HighlanderRobotics/scouting_dashboard_app)@[5d09f86b9b...](https://github.com/HighlanderRobotics/scouting_dashboard_app/commit/5d09f86b9bea32d9997aa8ae0c48ef5f014a01d3)
#### Sunday 2023-03-26 06:24:24 by MangoSwirl

So I started a bunch of features seperately because finishing them depended on other people finishing their thing and I forgot to work on features in seperate branches so here's the result of pretty much all of that finished, and if future me needs to know what was added in this commit then future me can look through the diffs for all I care. I don't care about that person because they aren't me (yet). And planning for the future is difficult. Was that supposed to only be 50 characters? My bad. I'm just gonna put it all here even if it's not at all useful and super difficult to read. Why did you even bother reading this? Don't you have something better to do, like put this on TestFlight, Jacob? Oh, it's uploading? I guess it's fine then. Your laugh always amuses me. I actually do have something better to work on myself and I'm just procrastinating by writing an insanely long commit message! Wow, I can talk a lot if I really put my mind to it.

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[0bc21524a1...](https://github.com/cmss13-devs/cmss13/commit/0bc21524a123944a37d45e1088dca13476824b9c)
#### Sunday 2023-03-26 07:10:40 by carlarctg

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[e6d568e7f1...](https://github.com/treckstar/yolo-octo-hipster/commit/e6d568e7f1fa71917565abf43a73b03e9241350e)
#### Sunday 2023-03-26 07:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [nevimer/Citadel-Station-13-RP](https://github.com/nevimer/Citadel-Station-13-RP)@[9c8abee554...](https://github.com/nevimer/Citadel-Station-13-RP/commit/9c8abee5540f17951b1947a212b80521f1b36300)
#### Sunday 2023-03-26 07:23:16 by IrkallaEpsilon

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
## [nevimer/Citadel-Station-13-RP](https://github.com/nevimer/Citadel-Station-13-RP)@[d261466765...](https://github.com/nevimer/Citadel-Station-13-RP/commit/d2614667654c0e35b2c906971ca94ece9e7b8629)
#### Sunday 2023-03-26 07:23:16 by IrkallaEpsilon

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
## [nevimer/Citadel-Station-13-RP](https://github.com/nevimer/Citadel-Station-13-RP)@[b3a43f2b85...](https://github.com/nevimer/Citadel-Station-13-RP/commit/b3a43f2b8522c03ca976a1f7e72aa9deea97b350)
#### Sunday 2023-03-26 07:23:16 by IrkallaEpsilon

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
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[10c080392f...](https://github.com/cmss13-devs/cmss13/commit/10c080392f855f07d6ea0c28d221be9840018fd4)
#### Sunday 2023-03-26 07:24:40 by carlarctg

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
## [SyncIt21/The-TG-Station-Fork](https://github.com/SyncIt21/The-TG-Station-Fork)@[f9fe79a307...](https://github.com/SyncIt21/The-TG-Station-Fork/commit/f9fe79a307dc55eb6e3ecf25019ef388889898ba)
#### Sunday 2023-03-26 08:00:59 by Dani Glore

Organ Unit Tests & Bugfixes (#73026)

## About The Pull Request

This PR adds a new unit test for all organs, a new unit test for lungs,
and includes improvements for the existing breath and organ_set_bonus
tests. Using the tests, I was able to root out bugs in the organs. This
PR includes an advanced refactor of several developer-facing functions.
This PR certainly represents a "quality pass" for organs which will make
them easier to develop from now on.

### Synopsis of changes:
1. Fixed many fundamental bugs in organ code, especially in
`Insert()`/`Remove()` and their overrides.
2. Added two new procs to `/obj/item/organ` named `on_insert` and
`on_remove`, each being called after `Insert()`/`Remove()`.
3. Added `organ_effects` lazylist to `/obj/item/organ`. Converted
`organ_traits` to lazylist. 2x less empty lists per organ.
4. Adding `SHOULD_CALL_PARENT(TRUE)` to `Insert()`/`Remove()` was very
beneficial to stability and overall code health.
5. Created unit test `organ_sanity` for all usable organs in the game.
Tests insertion and removal.
6. Created unit test `lungs_sanity` for
`/obj/item/organ/internal/lungs`.
7. Improved `breath_sanity` unit tests with additional tests and
conditions.
8. Improved `organ_set_bonus_sanity` unit tests with better
documentation and maintainable code.

---

### Granular bug/fix list:

- A lot of organs are overriding `Insert()` to apply unique
side-effects, but aren't checking the return value of the parent proc
which causes the activation of side-effects even if the insertion
technically fails. I noticed the use-case of applying "unique
side-effects" is repeated across a lot of organs in the game, and by
overriding `Insert()` the potential for bugs is very high; I solved this
problem with inversion-of-control by adding two new procs to
`/obj/item/organ` named `on_insert` and `on_remove`, each being called
after `Insert()` and `Remove()` succeed.
- Many organs, such as abductor "glands", cursed heart, demon heart,
alien hive-node, alien plasma-vessel, etc, were not returning their
parent's `Insert()` proc return value at all, and as a result those
organs `Insert()`s were always returning `null`. I have been mopping
those bugs up in my last few PRs, and now the unit test reveals it all.
Functions such as those in surgery expect a truthy value to be returned
from `Insert()` to represent insertion success, and otherwise it
force-moves the organ out of the mob.
- Fixed abductor "glands" which had a hard-del bug due to their
`Remove()` not calling the parent proc.
- Fixed cybernetic arm implants which had a hard-del bug due to
`Remove()` not resetting their `hand` variable to `null`.
- Fixed lungs gas exchange implementation, which was allowing exhaled
gases to feedback into the inhaled gases, which caused Humans to inhale
much more gas than intended and not exhale expected gases.

### Overview of the `organ_sanity` unit test:

- The new `organ_sanity` unit test gathers all "usable" organs in the
game and tests to see if their `Insert()` and `Remove()` functions
behave as we expect them to.
- Some organs, such as the Nightmare Brain, cause the mob's species to
change which subsequently swaps out all of their organs; the unit test
accounts for these organs via the typecache `species_changing_organs`.
- Some organs are not usable in-game and can't be unit tested, so the
unit test accounts for them via the typecache `test_organ_blacklist`.

### Overview of the `lungs_sanity` unit test:

- This unit test focuses on `/obj/item/organ/internal/lungs` including
Plasmaman and Ashwalker lungs. The test focuses on testing the lungs'
`check_breath()` proc.
- The tests are composed of calling `check_breath` with different gas
mixes to test breathing and suffocation.
- Includes gas exchange test for inhaled/exhaled gases, such as O2 to
CO2.

### Improvements to the `breath_sanity` unit tests:

- Added additional tests for suffocation with empty internals, pure
Nitrogen internals, and a gas-less turf.
- Includes slightly more reliable tests for internals tanks.

## Why It's Good For The Game

**Organs and Lungs were mostly untested. Too many refactors have been
submitted without the addition of unit tests to prove the code works at
all.** Time to stop. _Time to get some help_. Due to how bad the code
health is in organs, any time we've tried to work with them some sort of
bug caused them to blow up in our faces. I am trying to fix some of that
by establishing some standard testing for organs. These tests have
revealed and allowed me to fix lot of basic developer errors/oversights,
as well as a few severe bugs.


![image](https://user-images.githubusercontent.com/17753498/220251281-07ef598f-355b-43a9-afd6-1de9690831da.png)

## Changelog

:cl: A.C.M.O.
fix: Fixed lungs gas exchange implementation, so you always inhale and
exhale the correct gases.
fix: Fixed a large quantity of hard-deletes which were being caused by
organs and cybernetic organs.
fix: Fixed many organs which were applying side-effects regardless of
whether or not the insertion failed.
code: Added unit tests for Organs.
code: Added unit tests for Lungs.
code: Improved unit tests for breathing.
code: Improved unit tests for DNA Infuser organs.
/:cl:

---
## [harryob/cmss13](https://github.com/harryob/cmss13)@[d7c05a7165...](https://github.com/harryob/cmss13/commit/d7c05a71658b5b7f5312c6a0ec9947f59b307b60)
#### Sunday 2023-03-26 08:07:31 by carlarctg

Aimed shot and spotting now have laser beams. (#1905)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Aiming a shot on a sniper rifle now adds a red laser beam that connects
the target and the aimer. Spotting designators will emanate a faint
yellow one. Both will slowly increase in alpha from 0 to max as the
tracking progresses.

The sniper's laser beam can be disabled with a button, but keeping it
enabled reduces aiming shot time. Cloaked spotters will not cause a beam
to appear.

Completely resprited the indicators for spotting (it's now yellow) and
aiming (it's now red, usually)

The XM42B and PMC sniper rifles have more intense blue lasers and
reticles.

Stepping through laser beams will check for eye protection, if it isn't
sufficient, and the small probability chance passes, the target will
scream in pain! Completely flavor. If they have enough eye protection,
it will bounce off their headgear, and if said protection is BiMex
patented personal shades it will create a cool visual effect.

Refactored eye_protection to have three levels, flavor, flashes, and
welding. Sunglasses have flavor protection, sechuds have flash
protection, welding gear has welding protection.

The spotter's designator now has a white band on it to distinguish it
from the rest.

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

> Aiming a shot on a sniper rifle now adds a red laser beam that
connects the target and the aimer. Spotting designators will emanate a
faint yellow one. Both will slowly increase in alpha from 0 to max as
the tracking progresses.

The primary reason for this addition is because it looks sick as FUCK.
The secondary one is to help xenos see where they're being shot from.

> The sniper's laser beam can be disabled with a button, but keeping it
enabled reduces aiming shot time. Cloaked spotters will not cause a beam
to appear.

Makes sense, cloaked sniper/spotters shouldn't be made completely
useless due to the beam. It makes sense for the laser to reduce aim time
and it isn't a pain for xenomorphs to deal with as they know exactly
where it is coming from and where they can run for cover (And other
xenos can protect them better)

> Completely resprited the indicators for spotting (it's now yellow) and
aiming (it's now red, usually)

It made no sense for sniper reticles to be blue. Red is danger, yellow
is warning, blue is.... good? Additionally, since both reticles for
spotting and aiming were nigh-identical, it caused quite the amount of
confusion. I've tested it myself, you can spook away xenos with only
spotting because they think it's the aimed shot reticle.

> The XM42B and PMC sniper rifles have more intense blue lasers and
reticles.

Look, I know what I just said makes this sound stupid. But I think it
makes a lot of sense for the dangerous high-tech sniper rifles to have
stronger blue lasers, it just feels like a 'strong sci fi laser' color.
Like the pulse rifle in base ss13, it looks similar to the disabler but
you don't see anyone complaining. The base sniper reticle being red is
enough for people to realize this is a more dangerous version anyways.

> Stepping through laser beams will check for eye protection, if it
isn't sufficient, and the small probability chance passes, the target
will scream in pain! Completely flavor. If they have enough eye
protection, it will bounce off their headgear, and if said protection is
BiMex patented personal shades it will create a cool visual effect.

Cool flavor. Also lore-accurate!

# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>


Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>

https://streamable.com/kyprhl

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
add: Aiming a shot on a sniper rifle now adds a red laser beam that
connects the target and the aimer. Spotting designators will emanate a
faint yellow one. Both will slowly increase in alpha from 0 to max as
the tracking progresses.
bal: The sniper's laser beam can be disabled with a button, but keeping
it enabled reduces aiming shot time. Cloaked spotters will not cause a
beam to appear.
imageadd: Completely resprited the indicators for spotting (it's now
yellow) and aiming (it's now red, usually)
imageadd: The XM42B and PMC sniper rifles have more intense blue lasers
and reticles.
add: Stepping through laser beams will check for eye protection, if it
isn't sufficient, and the small probability chance passes, the target
will scream in pain! Completely flavor. If they have enough eye
protection, it will bounce off their headgear, and if said protection is
BiMex patented personal shades it will create a cool visual effect.
refactor: Refactored eye_protection to have three levels, flavor,
flashes, and welding. Sunglasses have flavor protection, sechuds have
flash protection, welding gear has welding protection.
imageadd: The spotter's designator now has a white band on it to
distinguish it from the rest.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

Co-authored-by: harryob <me@harryob.live>

---
## [silicons/Citadel-Station-13-RP](https://github.com/silicons/Citadel-Station-13-RP)@[8117b28946...](https://github.com/silicons/Citadel-Station-13-RP/commit/8117b28946d2e07f902e8800245c34d008336ccc)
#### Sunday 2023-03-26 08:09:06 by nevimer

makes AI experience not fullbright and fixes AI runtiming because they receive a mirror implant (#5179)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

![dreamseeker_sJwmVJw0Yp](https://user-images.githubusercontent.com/77420409/224618392-c9d94b76-05fa-456f-945c-784da7b962a3.png)

![dreamseeker_T7pXJJvDgH](https://user-images.githubusercontent.com/77420409/224618408-838a5156-91df-479f-ac48-4042692e887e.png)



## Why It's Good For The Game

Bug
## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. You can read up on GBP
and it's effects on PRs in the tgstation guides for contributors. Please
note that maintainers freely reserve the right to remove and add tags
should they deem it appropriate. You can attempt to finagle the system
all you want, but it's best to shoot for clear communication right off
the bat. -->

:cl:
fix: made AI's not see fullbright
balance: silicons don't become a traitor anymore on HUD UPDATES WHY
code: changes the call structure of cyborgs and moves life code down to
silicon level in some places, to make AI code work better.
fix: only human types are effected by mirror implants
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: silicons <2003111+silicons@users.noreply.github.com>
Co-authored-by: Lohikar <lohikar@protonmail.com>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[2728bbe9a9...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/2728bbe9a9003dbb4283ac807108c65129b7f34d)
#### Sunday 2023-03-26 08:39:19 by SkyratBot

[MIRROR] Polishes some side sources of light and color [MDB IGNORE] (#19860)

* Polishes some side sources of light and color (#73936)

## About The Pull Request

[Circuit Floor
Polish](https://github.com/tgstation/tgstation/commit/6b0ee9813271f693ceb44ad42277c36ef2e71268)

Circuit floors glow! but it looks like crap cause it's dim and the
colors are washed out.
I'd like to make them look nicer. Let's make them more intense and
longer range, and change the colors over to more vivid replacements.

While I'm here, these should really use power and turn on and off based
off that.
Simple enough to do, just need to hook into a signal (and add a setter
for turf area, which cleans up other code too).

[Desklamp
Upgrade](https://github.com/tgstation/tgstation/commit/8506b13b9c97bf740c3e97db04450555387dd126)

Desklamps look bad. They're fullwhite, have a way too large
range.Crummy.
Let's lower their lightrange from 5 to 3.5, and make the ornate ones
warmer, and the more utilitarian ones cooler. The clown one can be
yellow because it's funny

I'm renaming a color define here so I'm touching more files then you'd
expect

[Brightens
Niknacks](https://github.com/tgstation/tgstation/pull/73936/commits/835bae28e9eb9946be53c9f5dac0a0a39f15ef21)

Increases the light range of request consoles, status displays,
newscasters, and air alarms (keycard machines too, when they're awaiting
input at least)
Increases the brightness of air alarms, I think they should be on par
with apcs, should be able to tell when they're good/bad.
Increases the brightness of vending machines (I want them to light up
the tiles around them very lightly, I think it's a vibe)

Fixes a bug with ai status displays where they'd display an emissive
even if they didn't have anything on their screen, looking stupid.
This was decently easy but required a define. Looked really bad tho

## Why It's Good For The Game

Pretty

<details>
<summary>
Circuit Floors
</summary>

Old

![image](https://user-images.githubusercontent.com/58055496/224534470-c6eac5f5-5de6-40e9-897d-3212b8796d81.png)

![image](https://user-images.githubusercontent.com/58055496/224534477-ad412ad9-f7c4-44ae-ad75-a1a2c9bd17be.png)

New

![image](https://user-images.githubusercontent.com/58055496/224534486-b7b408a3-546c-4f90-aa9f-0e58bf8128ad.png)

![image](https://user-images.githubusercontent.com/58055496/224534496-626458f7-ab63-429c-a5db-eae9c784d06a.png)
</details>

<details>
<summary>
Desk Lights
</summary>

Old

![image](https://user-images.githubusercontent.com/58055496/224534513-9868b0b8-bc73-4b45-b986-8445078a8653.png)

![image](https://user-images.githubusercontent.com/58055496/224534518-bbbc8c6d-b59e-4f28-a31c-6c6a7e2c2885.png)

New

![image](https://user-images.githubusercontent.com/58055496/224534529-7988f440-03be-42ef-894c-b9e77f577ae5.png)

![image](https://user-images.githubusercontent.com/58055496/224534532-c3f2c6bf-c925-4a59-a8f9-10bb955a9942.png)
</details>

The niknack changes are more minor so I'm not gonna grab photos for
them. I can if you'd like but I don't think it's necessary. Mostly a
vibes in dark spaces sorta thing

## Changelog

:cl:
add: I made circuit floors brighter and more vivid.
add: Made air alarms, vending machines, newscasters, request consoles,
status displays and keycard machines slightly "brighter" (larger light
range, tho I did make air alarms a bit brighter too)
add: Tweaked desklamps. Lower range, and each type gets its own coloring
instead of just fullwhite.
fix: AI displays are no longer always emissive, they'll stop doing it if
they aren't displaying anything. Hopefully this'll look nicer
/:cl:

* Polishes some side sources of light and color

* yellow

* Update dance_machine.dm

* Merge branch 'upstream-merge-73936' of https://github.com/Skyrat-SS13/Skyrat-tg into upstream-merge-73936

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>
Co-authored-by: Zonespace <41448081+Zonespace27@users.noreply.github.com>
Co-authored-by: lessthnthree <three@lessthanthree.dk>

---
## [diphons/D8G_Kernel_oxygen](https://github.com/diphons/D8G_Kernel_oxygen)@[1fbe771143...](https://github.com/diphons/D8G_Kernel_oxygen/commit/1fbe77114359e82dcd359c7bd9d80c091fbfde77)
#### Sunday 2023-03-26 08:47:06 by Angelo G. Del Regno

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
5      	      20220479
2      	      20940223
1      	      21231290

Remember again that we're loading from a UFS card and that
we are loading ~1.1MB more out of a 20MB file.
If you're smart enough you surely know already about RAM and CPU
overhead of very high compression levels.

If you still disagree with what I just did, read this commit description
another 20 times, or more, until you understand it. :)))

Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>

---
## [Sefany2723/terminal](https://github.com/Sefany2723/terminal)@[5a34d92cb5...](https://github.com/Sefany2723/terminal/commit/5a34d92cb5c99000e95f612cb8bc23ba374dd941)
#### Sunday 2023-03-26 08:56:03 by Dustin L. Howett

winget.yml: switch to manually using wingetcreate (#15023)

It was brought to my attention that we should be more restrictive in
which tasks we ovver a GitHub token to. Sorry!

With thanks to sitiom for the version parsing and the magic GitHub
action syntax incantation for determining what is a prerelease.

---
## [bmccrat/songage](https://github.com/bmccrat/songage)@[3a487f6f37...](https://github.com/bmccrat/songage/commit/3a487f6f378d5c51371b2a2ba8b0be90f4e08d9b)
#### Sunday 2023-03-26 09:02:45 by bmccrat

Create Shadoworkingonit

Song written in the midst of the only abusive relationship ive ever been in with Sam. He wanted my love and my light and my healing to his shadows and insanity and yet rejected with disgust and shame every expression of my shadow side. He was deeply disgusted with the fact that I am an addict, and yet contiuned to feed me drugs that he felt were acceptable for me. I played this for him and he said nothing in reflection essentially. This relationship ended when I went back to heroin and talked to him while I was high and he spewed vitriol at me for doing so, which neither of what we did was acceptable. The verbal abuse continued for months, and I ultimately ended up overdosing and dying on my childhood bedroom floor where my mother found me. This was my last time using, which was November of this same year. This relationship made It clear to me of why I never want to be a drug dealer, a narcissist, or be in a relationship with someone who is. I t also made it clear my seemingly innate incompatibility with cannabis.

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[fd257da696...](https://github.com/LemonInTheDark/tgstation/commit/fd257da6965486f86330ac82989ca9a4a1a17171)
#### Sunday 2023-03-26 09:10:29 by LemonInTheDark

Ensures I don't york anything

Lowers init savings slightly, ensures the ARCHIVE entry is clear

We need to promise this, because archive drifting can lead to stupid
fucking shit. Better to manually 0 it out even if there is an overhead
for it

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[bf5a2d2d60...](https://github.com/LemonInTheDark/tgstation/commit/bf5a2d2d60554da2ce5fa1ac5f6c4179f6208cb2)
#### Sunday 2023-03-26 09:10:29 by LemonInTheDark

Optimizes pipeline processing

I haven't slept in 36 hours. Have some atmos optimizations

Pipelines now keep track of components that require custom
reconciliation as a seperate list. This avoids the overhead of filtering
all connected atmos machinery.

Rather then relying on |= to avoid duplicate gas_mixtures, we instead
use a cycle var stored on the mix itself, which is compared with a
static unique id from reconcile_air()

This fully prevents double processing of gas, and should (hopefully)
prevent stupid dupe issues in future

Rather then summing volume on the gas mixture itself, we sum it in a
local var. This avoids datum var accesses, and saves a slight bit of
time

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
copy of it from the pipeline datum. This would work based off a mutually
agreed upon volume amount for that component in that process cycle.

We'd use an archived system to figure out what gases to give to
components, while removing from the real MOLES list.

We could then push gas consumption requests to the pipeline, which would
handle them, alongside volume changes, on the next process.

This is a problem for tomorrow though, I need to go to bed

---
## [Segrain/cmss13](https://github.com/Segrain/cmss13)@[4e3c9ccc66...](https://github.com/Segrain/cmss13/commit/4e3c9ccc66f268b7e07db58470af2a170f4857a1)
#### Sunday 2023-03-26 09:38:14 by roll1d20st

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
## [Segrain/cmss13](https://github.com/Segrain/cmss13)@[bde254000f...](https://github.com/Segrain/cmss13/commit/bde254000fcd732e0365239e1b312dbfa21ee308)
#### Sunday 2023-03-26 09:38:14 by carlarctg

Refactors how magazine ammo color is handled into overlays (#2779)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Refactors how magazine ammo color is handled into overlays.

Instead of filling up dmis with a ridiculous amount of icon states for
each new barely used magazine type, compatible magazines have a 'band'
white overlay icon that is colored based on a variable on the magazine.

This will cause various sprites of various magazines to look subtly
different as the exact look couldn't be copied.

Renamed wallpiercing to wall-penetrating.

Removed cluster magazines from the code.

Altered the name of A19 magazines a little.

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

> Refactors how magazine ammo color is handled into overlays.
> Instead of filling up dmis with a ridiculous amount of icon states for
each new barely used magazine type, compatible magazines have a 'band'
white overlay icon that is colored based on a variable on the magazine.
> This will cause various sprites of various magazines to look subtly
different as the exact look couldn't be copied.

This will help a lot if adding new magazines as you don't have to sift
through the awful, bloated dmis. Additionally, it's been proven that
more icons in a dmi causes lag, so the less the merrier.

> Renamed wallpiercing to wall-penetrating.

More accurate

> Removed cluster magazines from the code.

These didn't fit with the new icon handling system, are not used
anywhere, and aren't interesting enough to be worth staying in the code.

> Altered the name of A19 magazines a little.

So i can do 'HV high impact'

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

refactor: Refactors how magazine ammo color is handled into overlays.
refactor: Instead of filling up dmis with a ridiculous amount of icon
states for each new barely used magazine type, compatible magazines have
a 'band' white overlay icon that is colored based on a variable on the
magazine.
imageadd: This will cause various sprites of various magazines to look
subtly different as the exact look couldn't be copied.
spellcheck: Renamed wallpiercing to wall-penetrating.
code: Removed cluster magazines from the code.
spellcheck: Altered the name of A19 magazines a little.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [atteria/tgstation](https://github.com/atteria/tgstation)@[374c8340c8...](https://github.com/atteria/tgstation/commit/374c8340c8c99586a4b4b8e978947c0b0f83a9d7)
#### Sunday 2023-03-26 09:46:05 by Jacquerel

Console Hack / Unfavourable Events won't run ghost roles which don't have time to do anything (#73343)

## About The Pull Request

Fixes #69201
The dynamic subsystem will never roll a new antagonist once the shuttle
is past the point of no return, but this check is bypassed by Console
Hacks and Unfavourable Event rolls (which are chiefly triggered from
console hacks, but also from when the Revolution wins).

I have made these procs more discerning.
Unfavourable Events will now never pick any heavy dynamic midround if
the shuttle is past the point of no return.
Console Hacking will now never spawn sleeper agents if the shuttle is
past the point of no return, and won't spawn Fugitives or Pirates if the
shuttle is called at all even if it can still be recalled

It's my feeling that given the need to get organised and move a ship to
the station there isn't really time for either of those events to
actually start properly rolling, but if you feel like that information
might be metagamed in some way by messing around with the shuttle (not
sure why or to what end, but it's technically manipulatable if you know
how the code works?) I can just give these the same restriction as
Traitor even if it means the bounty hunters risk showing up after the
shuttle has already left.

## Why It's Good For The Game

To some extent it's your own fault for clicking the popup while knowing
full well how much round time is left until the game ends, but it's
still disappointing to see a Blob or Pirates or Wizard alert appear at a
time when they can't possibly do anything interesting.
This is more true for the Pirate and Fugitive events because they
involve teamwork, placing a space ship, travel between the ship and the
station, and in the case of Fugitives its own internal five minute timer
before the other team actually arrives.

## Changelog

:cl:
fix: Hacking the Comms Console or winning a Revolution can no longer
spawn antagonists if there's not enough time left in the round for them
to antagonise anyone.
/:cl:

---
## [atteria/tgstation](https://github.com/atteria/tgstation)@[645054b489...](https://github.com/atteria/tgstation/commit/645054b489212a34d80e6e1a7fa1320e35d9bfc7)
#### Sunday 2023-03-26 09:46:05 by MrMelbert

Fixes encoding on syndicate declaration of war, Fixes a way to send unencoded text to newscasters (#73366)

## About The Pull Request

Ugly


![image](https://user-images.githubusercontent.com/51863163/218280311-f282bd75-2f6e-4290-b3f4-d9d856ff36d3.png)

Nice


![image](https://user-images.githubusercontent.com/51863163/218280315-233da635-f777-4006-8778-c673b83e887e.png)

War dec: 

- TGUI inputs for syndicate declaration of war no longer double-encode
sending customized messages into the announcement
- The alert box for the war declaration no longer has multiple errors
(an extra bracket, negative seconds)
- Reduces some copy and paste in the war declaration device
- Adds a debug item that's a war declaration device but it only does the
sound and message. Please don't fake war decs admins it's a horrible
idea

Additionally

- Documented `priority_announcement`
- Ensures all uses of text and title in the priority announcement
message are encoded (Some were not!)

## Why It's Good For The Game

Encoding looks bad, unencoded text is also bad

## Changelog

:cl: Melbert
fix: Syndicate declarations of war no longer murder apostrophes and
their friends
fix: The alert box for the declaration of war no longer looks funky, and
counts forwards in time rather than backwards
fix: Fixed being able to send unencoded HTML to newscasters
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [heady8354/Video-Game-Project](https://github.com/heady8354/Video-Game-Project)@[9bc6776f81...](https://github.com/heady8354/Video-Game-Project/commit/9bc6776f81b548d44872e14eb046d1a64fdfd91d)
#### Sunday 2023-03-26 10:50:44 by heady8354

battle animations

sorry for not committing recently. ive been working on it but always getting off before committing due to being too tired to write one of these summaries. today i had the most brutal fucking headache of my entire life and took a fat nap to get rid of it, waking up about an hour ago. anyways, gonna do more tmmrw. or today.

---
## [abhilashsv/AI6127_Final_Project](https://github.com/abhilashsv/AI6127_Final_Project)@[96bdc58a4b...](https://github.com/abhilashsv/AI6127_Final_Project/commit/96bdc58a4b2a95c5cb146047276062583cef1cea)
#### Sunday 2023-03-26 11:35:28 by abhilashsv

Create score_generator.ipynb

Score Generator for Conversations:
--
okay <mandarin>来来:lai lai</mandarin> okay <mandarin>来:lai</mandarin> round two (ppl) <S> <Z> <Z> <Z> <S> <S> <Z> <Z> <S> <Z> <S> <S> <Z> <S> <Z> okay alright so (err) miss lily [ah] thank you again [ah] for dropping this call to let us know so (uh) my name is jack over here and nice talking to you so again I think I hear few fair bit of request from your side [ah] in terms of the call enquiry so maybe I can (err) (ppo) check with you a bit more understand a bit from more from you [ah] because I think over here is (uh) (ppo) (uh) you've mentioned that you'll be travelling in (err) family in a tour so (err) there will be I think apart from you your husband and your children there will also be these two elderly [ah] which happens to be your parent so over here is (uh) for your father right who you mentioned is wheelchair bound right (uh) just like to understand a bit more [ah] like could you share with me like (err) what's his like current age and also things like (err) for his wheelchair bound condition right (err) (ppo) how I mean how how's the condition like like is he more yeah (mm) (mm) <Z> <Z> <Z> <Z> <Z> <Z> okay okay sure so over here is (uh) just to probe a bit further (err) who will be the primary caregiver for your father <Z> (mm) (mm) (mm) yup <Z> right right sure I think that's that's definitely a very valid and fair question over here thank you for asking so I think over here maybe I can answer your question on (uh) your earlier question [ah] on (err) the trip to #busan# right in terms of the facilities here and there how is the whole thing like for your father over here [ah] so over here is (err) for the trip there is definitely some (um) facilities to make it more mobile and more user friendly [lah] for wheelchair bound personnels like your father and then over here is like (err) to connect these to your lat~ latter question over here is (err) there will be some (uh) additional cost in terms of the <S> because of the additional I think considerations we will be factoring also in terms of that so (uh) over here I think for the pricing wise right (err) it's something where we can further discuss in a bit but maybe I can also understand in terms of your needs like the because that there's the mentioned that you have also the two children with you right so (err) for them like again what what's their like how how old are they and also like normally what what do (uh) do they do and ya (mm) <Z> <Z> <Z> <Z> <Z> <Z> <Z> okay okay sure so I think over here (err) pricing wise definitely is something that we will look into as for the packages [lah] like in terms of the so called (um) food special diets here and there that your kids can't eats (uh) special diets we would we take taken note of that (uh) how about the rest of your family members including yourself like maybe you can share with me a bit more in terms of yours dietary (uh) preference and restrictions for each of you <Z> <S> <Z> <Z> <Z> <Z> (mm) (mm) right sure sure so over here (err) for our package yes (uh) because of the nature [ah] in terms of the the korean food and all right normally is spicy [lah] due to #kimchi# and all so over here is we do have a non spicy option so no no problem I think for your children (ppb) you can go I will recommend you to go with the non spicy options for them for kids in in particular so (uh) aside to this food (um) (ppo) preference and also no no spicy diet for the children right (uh) I think for to answer your question in terms of the pricing and all right we will need to review [lah] this whole thing as a package also [lah] to see [ah] how (uh) affordable we can make it for you but at the same time is also (uh) just like to understand a bit more from you right is (err) what what's the main purpose of like going for this trip like is it for leisure sightseeing or is it something else <Z> <Z> okay and how long do you plan to have this trip again because I think over here (mm) (mm) (mm) okay (mm) okay okay (ppb) but this is technically a family trip right that you will just keep it within your own group [lah] <Z> <Z> okay sure got promotion but I think we can end the call now (ppl) so (ppb) later on okay can thanks 
0.020781928673386574
okay and can start okay cool so again back to this scenario two [ah] that will be in the context of a hotel where you as a guest is calling in to share with me your positive experience that you have with my hotel right I will just listen to you and receive the feedback accordingly <Z> <S> hi (err) good morning (uh) (um) how may I address you this is miss <Z> <S> <S> <Z> <S> <Z> <Z> <Z> <Z> <S> <Z> <Z> <Z> okay sure so (uh) miss lily thank you for dropping a call [ah] to (uh) pass on the feedback so (uh) my name is jack over here (uh) concurrently I think the hotel manager is away on leave [ah] so I'll pass definitely (err) we appreciate your call and will pass on the feedback to the person in charge [lah] and also and just to inquire a bit right (err) this staff whom you are saying right and you're referring to right do you know what is his name or what is his or her name or whether (uh) ya <Z> okay <Z> <Z> <Z> <S> (mmhmm) alright sure thanks for the praise over here lily so over here again (uh) just to understand also [lah] that we hear your request and we'll certainly pass on this (ppo) (um) appraisal [lah] to to the manager in charge and also to this staff [ah] so (uh) again over here right (err) just like to maybe hear from you again [ah] (uh) because I think you shared a bit on in terms of okay there's this arrangement in terms of the vehicle the driver and also certain areas that he's being (uh) polite and courteous to you in terms of certain service here and there so can I understand a bit more as to (uh) because I don't have the record with me now [ah] but I really hear from you right this whole (um) (ppo) stay of yours right when when was it last back backdated (uh) because I just joined recent (mm) <Z> <Z> <Z> <S> okay right and again <Z> <Z> <Z> right right so (uh) again again over here appreciate your help [ah] in the positive review and also (uh) in terms of like scheduling another upcoming trip with us [ah] so (err) ya for the request it as to the same room right (uh) just to hear from you sorry you are looking at the exact same room that you want for your last sunday (mm) <Z> <Z> (mm) (mm) right okay because right now [ah] on my record is (uh) I think for the spot that you are looking to schedule right is quite (uh) (ppo) the the there's quite a overwhelming response [ah] for this also this similar room also so I'm just wondering right in the event right (uh) over here is definitely I will I've made this (um) request for you [lah] that you are looking at to secure the same room as per what your stay is for last sunday but let's say in the event if (uh) there's other alternatives right (uh) just like to hear from you also right (uh) apart from the sea view that you are saying that okay the scenery is very good and all right is there any other rooms that you will consider if there is right (err) could you share with me a bit more as to what kind of like (err) attributes of the room that you wish to have like what kind of amenities and all those (mm) <Z> <Z> okay is that all or is there something else that you you wish to have in this (uh) room in term (mm) <Z> (mm) okay cool so again [ah] I think over here is to really optimise your experience over here is right (err) we would also (uh) are you also looking to have the similar staff who attended to your (uh) needs and inquiries to to come and serve you again because over here (err) I think for this staff over here [ah] he happens to be on leave [ah] for this certain period of time so I'm not sure if you are okay to have like others staff who come in to attend to you and maybe if you have some (um) (err) request that you would like us to (uh) like (uh) attend to you right maybe you can share with me off hand now so they can (err) (mm) <Z> okay so you are quite okay [lah] if we were to assign (uh) you with a staff which <Z> okay alright sure so I think over here is (err) again [ah] once again thank you so much for your feedback and appraisal over here (err) I think for the last part if you can right maybe we can hear a bit more from you as to (uh) how you can (um) (ppo) how you will you I mean how (uh) because I think you do have some friends [lah] that you mentioned that you will be bringing in to stay at our area over here and there also so (err) maybe if your side can we'll also look forward to having you to maybe do a recommendation of our (err) so called ya website and also in terms of the our services to to others <Z> okay alright okay so lily (uh) thank you so much for your time (uh) and I think that will be all for your call thanks and look forward to seeing you bye bye okay can stop #liao# 
0.027474941685795784
okay <S> yup <S> <Z> <S> <S> <S> <Z> hi lily (err) yes (uh) thank you for your call enquiry may I know what is the (um) <S> in called sorry what what is the changes you are seeking to make over this call <Z> <Z> okay so (mm) <Z> <S> <Z> okay so (err) miss lily right again (uh) first of all [ah] thank you for calling in so over here is (err) I hear that you are calling in to make some changes and the reason is because of the COVID nineteen right that you are (uh) requesting to or (uh) downsize in terms of your guests right to ten people and (err) there's also this request for a (ppo) vegetarian pax [lah] over here okay so over here is for the <S> request right actually we'll just like to inform you like (err) there's actually for this reservation it because it has been made from a certain period days [ah] until now so if you are looking to do the (uh) change of request now right there may we may not be able to so called do a <S> full so called (uh) refund or in terms of the proportionate of the so called reimbursement [lah] in terms of the payment [lah] you made previously over here <Z> <Z> yes yes so so good question over here [ah] over here is because (uh) just now I think you were mentioning that because of the downsize right to ten pax right you are I'd I hear your request that you are looking to have the same room also right the same room okay (mm) okay because over here is at my end is I will need to forward this feedback [lah] in terms of the change of inquiry to the management to see what (uh) what are the leeways they can help to like go about it in terms of the downsizing in terms of the (err) so called balance reimbursement [lah] back to you ya but of aside to this right is there (err) some just to like to understand a bit more from your side is already also actually for this whole (uh) reservation right (err) what what's the occasion for again (uh) <Z> <Z> (mm) okay so in terms of that that's for the birthday celebration also more for kids [lah] and for your (uh) children right okay and (err) because over here (uh) just to take down some questions [ah] from your side also is (err) okay like how many can you share a bit more details [ah] as to like how many adults and also how many kids guests (err) you'll be like will inviting for this whole occasion yup <Z> okay <Z> <S> (mm) right so for in terms of the vegetarian request right (uh) normally would would do have a few recommendations [lah] whether or not is catered to that specific pax right for vegetarian if not right (err) for some of our dishes they are also (err) in vegetarian [lah] technically they are vegetarian and even for non vegetarians right is also good to consume also ya that's why over here will like to check with you also what's your preference and all also [lah] and (uh) aside from this person [ah] who is vegetarian right is that what (uh) maybe I can go through with you the list of the kind of food you have ordered for the reservation maybe just to run through if there's any other (ppo) (uh) changes or any request that you may have [lah] like in terms of like maybe the main dish the dessert and all those (uh) maybe you can share with me a bit more and also in terms of like any guest has any special diets [lah] all that ya <S> <Z> <Z> <S> <Z> okay so if I hear you correctly [ah] basically there may be still another up to another two pax [lah] they may be joining in right for this whole [lah] which makes a total of twelve and then (uh) for discount wise (err) just to share again [ah] the this is something that we will look into it for you (uh) but I'll need to await for the decision [lah] from the management side but in the meantime maybe I can (uh) (uh) you can help me run through what are some of the main dishes and also side dishes appetisers and all those in terms of the food choice [lah] that you'll like to have for this like (um) celebration <Z> (mm) same choice okay if that's the case right just to (err) maybe run through (uh) with your a bit [ah] which is I think for the the one that I'm looking in my system right now I think back then you made certain reservations for (err) okay like (uh) western fried rice and also (uh) vegetarian #bee hoon# over here I think that's more for the main dish and some (uh) noodles also along the way and then for the single dish right it will be like fried chicken wing (err) nuggets french fries coleslaw salads all these (uh) it and any changes to that no change (mm) [oh] you'll bring along your cake for the celebration <Z> [oh] I see I see but actually (uh) add on to that right because for our side we actually do provide certain (uh) (uh) (uh) I think of course (err) we would welcome that just that over here just to share with you that (uh) would you be (um) okay to maybe because we do have this (err) a bit of a promotional offer [ah] that since you are holding this for like a birthday celebration and such right just for a very small fee of like (um) fifteen dollars right we will prepare this (um) (ppo) additional cake from our side also would you prefer that option instead or will you still like (um) (ppo) prefer to like bring along your own like cakes for this (um) celebration <Z> okay okay can okay if not I think we just passed the ten minutes I think we can do a stop now yup okay thank you 
0.021637190133333206
up okay so (ppo) okay so hello I'm calling to (err) make some enquiry about (uh) travel trip to (uh) korea (uh) #busan# I have (err) four adult two children and one of the adult is wheelchair bound which is my father so we have (uh) my father and my mother and my spouse and myself and my two children and (uh) I would like to request (um) first for the air airplane right I would like to request (uh) the seat to be sitting behind (uh) nearest to the toilet so it's more convenient for my (err) parent and also my kids because you know the travel the air flight is about six hours so you know elderly they may may not be able to hold for so long and also I would like to check with you about the the area that we are going (err) is it (uh) handicap friendly do they have (uh) facility like lift (err) escalator and you know the restaurant is it also (uh) okay for the (uh) handicapped person know the restaurant that we are going the places that we are going and and I have two kids (err) we also want to have some (uh) places for them you know for the kids that that the attraction that for the kids as well <S> <S> <S> <S> <S> <S> yes okay so (uh) my my father is (uh) seventy five years old he's wheelchair bound he his leg a bit weak but he able to walk (err) have a short walk with the walking stick so (err) maybe (uh) for some places right he'd be [eh] he is okay to walk with the walking stick ya is not totally (uh) wheelchair bound it just that for long walk right he might not be able to do so ya so we need to use the wheelchair to (um) (uh) wheel him around (err) ya so for shopping right may not be able to may not suitable for him because the place are too crowded so we would like to go to some places right that is not so (uh) (uh) crowded and and we can skip the shopping trip (uh) no need for shopping but we would like to have some places for the kids that they can play so ya that's my request <S> (uh) I will be the caregiver to look after (uh) the two elderly so I just want to check with you right you know because of wheelchair bound right so do I need to pay additional or the the rate is the same (err) ya you know the ticket the everything the entry ticket is it the same or you know we need to we will have a special discount because due to the elderly or or you know <S> <S> <S> <S> <S> <S> <S> ya okay (uh) my my children right one is (uh) five one is (err) (err) (uh) seven so and they they don't eat (uh) spicy food but you know [lah] korea (uh) #kimchi# they have a lot of spicy food over there so if let's say I want to change it because I know we are follow the tour right normally the the the the meal already pre book everything but let's say if you know (uh) if I go there and I don't want to eat the spicy food right I want to order my own non spicy food (uh) this one can be arranged or I need to pay additional you know for it because is not in included in the package I order (uh) different from the from the tour package this one do I need to (uh) pays pay extra for the kids and can it be arranged also or maybe you can tell the tour right I got a case that cannot eat spicy food so maybe they can ch~ exchange (err) for me without any charges <S> <S> [oh] for the adult is (uh) no problem we can eat everything drink anything just that for the kids they are more troublesome because they don't eat spice they don't eat spicy food so (err) understand that most of the meal (uh) in the in the trip right will have some spicy (err) food there (uh) so I just want to check if let's say we we would like to change the meal or we want to order our own (uh) will can we waive can you all waive the charges for us because we just do a exchange for a non spicy (uh) food over there and ya something like that (mm) <S> (uh) okay can okay <S> <S> ya this is a leisure trip this is for sightseeing you know because (uh) after COVID nineteen (uh) we have been (uh) (uh) ne~ (uh) never been to korea for so long time so we just want to make a trip there ya since it's open border now <S> (uh) we plan to stay for about one week ya one week at #busan# then (err) ya just to sightseeing a few places over there and enjoy the I think should be spring time <S> (uh) yes so (err) for the for the pricing right for the charges right is there any promotion for any credit card or any (ppo) any (uh) free luggage for like because I got (uh) six person is going so is there any (uh) promotion (uh) free gift that if I purchased the ticket with you <S> (mm) yup can 
0.02190748043358326
<S> <S> okay okay hello can I speak to the manager hi good morning hi my name is lily I just (err) had my (uh) pleasant stay at your hotel recently I think (uh) last week so just to (ppo) give you some some of my feedback feedback (err) for my stay so (err) because I I found that your hotel staff is very friendly and they actually help my son to solve some of the problem because actually my son (err) lost his handphone during the stay and your staff managed to (err) (uh) found the handphone back to him so (uh) I like to gives some compliments to your staff and also your staff right is able to (uh) change the (uh) hotel (uh) (uh) tidy up the hotel room very quickly and (err) and on the first night we stay right the hotel (err) the hot water actually is not working and the staff quickly help me to change to another room and they they change another bedroom for us without any charges so I think the customer service is very good in this area and we have a pleasant stay over the (err) for about (uh) three days two night (mm) <S> <S> ya okay I think I think his name is (uh) jack okay so (err) he did help help us (uh) during our stay and he is very polite (mm) so (err) he al~ he also (uh) recommend some (uh) local local driver to drive us to drive us (uh) around the town I think the driver (uh) charged very reasonable and he's also very helpful so I think your your hotel has a very good connection with the local (uh) tourists guide you know to be able to recommend some (uh) good (uh) driver for the tourists <S> <S> <S> <S> <S> <S> ya is on last sunday last sunday ya so I would like to feedback I would like to (uh) feedback (um) I will give a com~ I will write a good (uh) feedback on the website that we have we booked the hotel (err) from (err) <Z> agoda ya I will do a very good review on this hotel stay and just to check with you so (err) so next month I'll like to go for the (uh) short stay (uh) with another friends (uh) and family so (err) would you be able to (uh) re~ (uh) reserve the same room for me <S> ya because the room right has a very good (uh) sea view so we would like to stay on the same room and the facility the equipment inside is (uh) I think is quite good maintain is quite good so we would like to have the same room for stay for my family as well for the next trip so (err) if I make the earlier reservation will you be able to give me the same room <S> <Z> <Z> okay as long yeah as long as the the room got the balcony you know got a sea view and of course if is higher floor will be better (err) ya so (err) so we if just normal so I will just get the big room a twin twin twin room with a additional bed then (uh) with a sea view (err) ya then should be okay <S> okay okay <S> overall I think your staff are well trained so (err) I think anyone should be okay because as long as they they are able to speak english you know able to communicate (uh) should be fine with other staff ya as long as they are able to communicate in english then it should be no problem <S> <S> put website social media sure I will give a very good (uh) review on my social media posts and also on your website (uh) review (mm) thank you bye 
0.07879406213760376
okay topic one F&B correct okay so I'm call mister hello my name is lily I'm calling (um) to make some changes on my reservation two days ago <S> okay because (uh) due to the COVID nineteen right I would like to resize my (uh) reservations now I have <Z> (err) about ten people for coming because previously right I have made a reservation for about twenty person so now I only have (uh) ten ten guests guests for coming in and I would I also have (uh) one (uh) vegetarian guest so can I check with you (um) (uh) how to going about for the changes will you still give me the big room <S> <S> ya yes yup <S> <Z> okay be because I only do (err) I I already give you the (uh) down payment I mean (uh) deposit on the reservation for twenty pax right so since now I downsize (err) would you be able to give me the same (uh) (uh) discount for the twenty pax <S> yup I would like to have the same room but (uh) downsize the guest number and I also want the I also want to have the same discount <S> <S> okay this is for birthday party for little girl for my girl so (um) (uh) so we will have a few (uh) children will be coming will you be able to prepare some (uh) like (uh) party props or baby chair for me <S> <S> yes <S> <S> okay I will have I will have four adults six kids and one adult is vegetarian <S> so for the vegetarian's for the (uh) vegetarian side right how would you going to prepare (uh) will you just give a a pack of vegetarian food or how is it going to do <S> <Z> <S> <Z> <Z> <Z> okay okay (um) so (um) beside the the discount right just now I mentioned right the discount because previously at the twenty pax you give me twenty per cent discount so now I reduced to (uh) ten pax right so I I believe the discount will also be affected right (um) so let's say if I (uh) last minute I will have one or two guests coming in <Z> will it be okay for you to arrange (uh) to give me more discount ya <S> <S> okay I think I will still remain the (uh) the same choice that I had made (uh) previously <S> <S> <S> ya yes ya no so I will also prepare I will also (uh) bring along a cake for the celebration <S> ya the cake right is a ice cream cake so (uh) you (ppb) you <Z> before that right I will bring to the kit~ I mean you need to help me to (uh) (uh) put inside the fridge first because it's a ice cream cake <S> <S> <S> because this I already ordered the cake I already ordered the cake and is is custom made so and is a ice cream cake so I will it I would like to stick to my plans I will just (uh) bring along the cake so you'll just help me to cut the cake to serve the guests <S> 
0.1751757562160492
<S> one two three part three <S> <S> okay yup I'm sorry to hear about this but however can you give me your (ppb) can you let me know some basic information like (um) your name or your and your contact number (ppb) and understand you travel to korea do you have the exact date and which city of the korea that your is your is your trip <S> <S> <S> <S> <S> okay <S> <S> <S> <S> <S> <S> <S> <S> <S> <S> <S> okay <S> okay would would you mind to share like how how many meal how many meal that you all have for the (uh) B_B~ for the B_B_Q korean B_B_Q <S> <S> okay okay (mm) okay understand <S> <S> <S> <S> okay understand that the the day of the trip there is actually a it's actually we do arrange for two tour guide to you all (ppb) is like (uh) which would you mind to ex~ or explain a bit further like which tour guide that you refer to (mmhmm) <S> <S> <S> <S> okay I see yup (uh) we'll think on we'll think on this scenario will do something about this <S> (mm) <S> <S> <Z> <S> okay understand that (ppb) so understand that (uh) you need the tour guide that can communicate at least a bit (um) in korean so that to make the trip more smoother for you all (ppb) other than that do you have anythings that (uh) you you are looking (ppb) for (uh) from the travel agency or from the from the tour guide so that we can actually do some improvement on that (ppb) aspect and to serve you better in future <S> <Z> <S> <S> <S> <S> okay I see beside like (uh) the tour guide not able to explain like (uh) things (uh) stuff that (uh) about the not really knowledgeable in sense like (uh) when you all go for the museum or something (ppb) like is there any other thing else that you can give us some example so that we can (ppb) we can we can see what we can do on it <S> [ah] yup or what what do you ex~ (uh) expe~ ya you what you have experienced during the trip <S> <Z> <S> <S> <S> okay the in the sense that they actually taking longer time to (ppb) to to get this done [lah] like to get the ticket everything (ppb) okay understand that (mm) yup yup and also to sorry that you have (uh) about this bad experience you have (uh) for the trip okay can we can stop 
0.03239940106868744
one two three part two yes fullerton hotel here <S> <S> okay (ppb) (uh) understand you will need one room can I have like how many pax guest (uh) do your do you have four to five so you will need a big room correct (ppb) <S> <S> (uh) however our room will go with go with the number of pax as well so for your number of size of the pax right (ppb) we will suggest you to take for two room is that okay for you alright then (uh) let me just check the availability okay (uh) can you can you repeat your dates again okay yup we do have two rooms with the sea view <S> [oh] sorry with the with with the view that you can see the firework <S> okay because it's the there's a holidays (uh) festive seasons so the price will be (uh) three hundred per per night <S> (uh) sorry three hundred is (uh) yup for one room <S> okay what kind of facilities you are looking at <S> yup our hotel do have these services like the for the gym for the for the swimming pool but because due to the the current situation we have some (ppb) maybe we have some limitation of the of the of the headcount (ppb) so you all may ne~ might need to book in advance if you all wish to use for the facility ya (uh) you all can go there as a group and then (uh) you all have to book in advance [loh] (mm) (ppb) yup you can do it after once the reservation after the confirmation of the room reservation yup you all can you all can make it (mm) (ppb) okay so beside for is there any special request that you any other special request regarding about your room <S> okay okay sure (ppb) and do you all have any request regarding about the food we do serve you all the (uh) (uh) breakfast your room will be include breakfast but other than the breakfast do you all need any request for the food [oh] okay I see <S> okay (ppb) (um) yup that's fine so maybe it near to the date you can just confirm us like which (um) which day you wish to (uh) have the lunch service or which day you would like to have dinner (ppb) at our place (ppb) okay (uh) <S> (uh) no it's only the breakfast is included so do you have any budget looking for any food you can (uh) per meal so that we can see what we can (uh) prepare for you <S> okay sure alright (uh) other than that do you have anything else like (uh) regarding about the room reservation on this coming year end <S> [ah] good question (ppb) so for now right (uh) yup yup we did have some (um) promotion like this reward program ongoing (ppb) which in certain like (uh) for for your first reser~ if you sign up with us for so some sort like (um) reward programme (ppb) (uh) we will like your like like you flying with the mile (uh) the mile the mile the mileage some you can earn some point (ppb) and for your next reservation right you can based on the points you have collected so one points will be (uh) will be cre~ (uh) one dollar credited so (ppb) it's like in the next reservation you can use the points to make some dis~ deduction [lah] <S> yeah definitely you can make it now (ppb) so which <Z> yup sure (ppb) so what we suggest that you can go to (uh) once you have (um) maybe before you do your booking for this (uh) this first (uh) book booking (ppb) you can sign up for the plan first then from there you can start to accumulate your point then (uh) with the re~ (uh) once you sign up for the reward this reward programme right they actually will generate you (um) some like a member (ppb) a member a member number or registry a number for you (ppb) so (um) from there you can use this (uh) to do for your booking <S> (uh) I can help you as well I can help you to do it on call (ppb) but you need to provide me some of the basic information (ppb) so in order for me to to proceed so like I it's okay for you you want me to do it for (uh) for you now alright (ppb) ya kay could you h~ could you give me your name <S> alright (ppb) and we'll need your contact number <S> okay and we will need your email address okay hold on [ah] okay I have done for the registration so there'll be email address the the secretary will email you all the details you can check your email if you receive it (ppb) and if you have any question regarding about the reward programmes can always check with us <S> (uh) yes for every point that you (uh) you earn right it's only valid for the (uh) within a year so for example like the points you earn today (ppb) maybe hundred points so you will be valid for one year from today onwards (mm) <S> <S> yes we have a few tier for the membership (ppb) so as what what you say we have silver we have gold (ppb) then (uh) we have gold class everything so the points as what I mentioned to you earlier on that one is the basic it's like one dollar (ppb) (um) for every for for (uh) you can earn for the one dollar point (ppb) so as you go right you higher tier of your membership right you will earn more dollar of the point (mm) <S> yup that's confirmed (ppb) so (uh) I mean (uh) yup the availability we do have a avail~ room available on the day on the date that you you want (ppb) so what you do is like you can you if you want to I can actually help you for the booking as well or if you are confirmed now so I can straightaway do the booking for you <S> okay (ppb) that's okay so quick okay I'll I just take you as our member the membership card the member (ppl) and can you let me know the num~ the pax again how many pax of you all so for now I will put two two one room each room (uh) two pax for now <S> okay alright yours this is done alright stop the recording 
0.026790009811520576
alright one two three part one alright ya sure please go ahead what like what is the changes that you you would like to make <Z> [ah] okay (uh) understand that (uh) but would you mind to push could you share like (uh) more to us like when (uh) what's the number what's the quantity that you are looking for looking at <Z> okay (ppb) (uh) okay go back to your requests [ah] (ppb) so firstly you want to increase your size from forty to fifty am I correct correct <S> four to sorry <S> four to fifty okay that's a huge number (ppl) alright (uh) that's a huge change (um) we could check on that we can and get back to you (uh) how for the cake like do you have any (uh) special is beside of the colour do you have any request on in in terms of the (ppb) flavour or beddings (ppb) so we can see how we can (uh) help you on this (uh) okay can I think that's (uh) yup that's fine so other than that do you have anything else that (uh) break ya for the for the party (mm) <Z> okay <S> okay can (ppb) and I also got you for the about the child about you need some special request about the child dishes (ppb) (uh) you need something sweet that's fine (ppb) (uh) we will need you to provide us the number how many of them (ppb) and for adult wise right would you mind would you would you able to tell us a little bit more like (um) what kind of food that you are looking for big since you have a big (uh) I mean a big number of the order (ppo) okay <S> okay can that should yup I think that should be fine <S> is there anything else that (uh) we can help you on this (uh) reservation <S> can can we can play some music for you (ppb) or you have any specific songs also you can provide us the song list (ppb) so I mean as in like you are ya you provide us the (uh) the the the disc or something we can play the music in the background for you yup that's great yup sure you have any preference about the colour of the call for okay I see yup (uh) yup no problem on it and yup we can arrange for the table cloth and your about the food <S> (uh) yup for now we I will I will confirm with you confirm with you again on this but assume that everything this is (uh) if let's say we when go ahead then you can let me know what others (uh) like requirement that do you have then we can get back to you on this again <S> for the about the number of change yeah so we just will make sure that the the the restaurant can cater (ppl) can cater everything (ppb) her for the food and also for the all the all the place [lah] (mm) (mm) yup sure so let give me like (uh) two working days then we'll get back to you (mm) (um) alright yup other than that <S> <S> (uh) at the moment we do not have any (uh) we don't have this (uh) any games for the (ppl) for the kids however if you need to (ppb) you can what you can do is like we can prepare you a table a spare table maybe (ppb) then maybe and you all will need to bring bring some toys for them or some play I do not know like a board game or something for them (ppb) but for the restaurant is (uh) we do not have this (uh) as in like we do not have any this kind of the service for them (mm) okay so for beside for the cake celebration right (uh) you need you you you want a cake for the celebration is there anything else like any special about the drinks <S> <S> alright (mmhmm) <Z> okay alright <S> okay how about the adult (ppb) you you all prefer to have a some alcoholic drink or non alcoholic drink [oh] only the non alcoholic drink [ah] okay okay alright (uh) maybe you can (um) give us like some of the (ppb) some of the numbers regarding about the (ppb) how many tables you need for #halal# for keep for keep for the keep for malays and then (ppb) so that we can we can do some arrangement as well <S> okay <S> okay okay I think that should be fine alright (uh) do you have any other thing else alright thank you then and we will get back to you again <S> thank you 
0.026445303112268448
<S> <S> part three okay hi I am calling regarding (um) the trip that I've went with your agency not long ago (ppb) (um) to korea and I'm actually calling because (um) I have some unhappiness that I have regarding the trip (ppb) especially with the tour guide so I'd like to make some (ppb) feedback (um) hoping that your company or your agency can (ppb) do the changes necessary <S> <S> <S> okay <S> yup okay so my name is jane my handphone number is nine triple four eight triple four and (um) the trip to korea was just earlier last month I guess (um) around twelve to four twelve to fifteen october so I went there for around a four day three nights stay at korea and what made me really unhappy was (um) firstly some of the tour guides like (um) they were very bad at korean so which was kind of surprising to me since (ppb) you know as a tour guide you are supposed to be very experienced in speaking their language there but they have some issues with (um) the korean language and he couldn't communicate with the locals very effectively (ppb) so a lot of times they were just (um) shouting to get their points across with the koreans locals and (ppb) I think that kind of ruined the mood for the rest of us and the (ppb) (um) tour guide I mean the the people there because I mean we come here to enjoy to (uh) to enjoy our holiday then you're just shouting across it just ruins the mood for me [lah] (ppb) and then besides that also I noticed that (um) the bus drivers that (um) you all employed to drive us around they weren't very sure of the routes (ppb) because most of time like one destination to another it shouldn't take that long according to the itinerary (ppb) but your bus driver took like maybe one hour when the itinerary only said that it will took like thirty minutes so I guess that wasted a lot of time and then (ppb) I mean it's obviously not comfortable to sit on the bus for a long time also because you might need to use the toilet and stuff so I mean besides me and my family other people were also unhappy [lah] but then (um) the tour guide keep saying to us that [oh] it's going according to plan (um) nothing to worry the bus driver is okay (ppb) but then if you look at the itinerary that was given to us I mean it's obviously that it wasn't going smoothly [lah] so that's something that I'm unhappy about also and then (um) I think the places that your company have arranged to bring us to a journey okay (ppb) it's fine but (um) the issue I have is with the food okay so the restaurants that you brought us to (ppb) (um) it's quite similar so every throughout the four days three nights every single night we have we are just eating korean barbecue over and over again so that kind of made me wonder if you all have planned (ppb) the itinerary well enough because (ppb) if you have done so then we shouldn't be eating the same food over and over again yup so <S> I think for all our dinners we had korean barbecue for lunch (um) I think only once korean barbecue and then that's it [lah] but it's just mainly the dinners maybe because there's a lot of korean barbecue outlets near our (ppb) (um) hotel but (ppb) I mean it doesn't make sense to serve us korean (ppl) barbecue every night (ppb) yeah <S> yup so I guess all these made me really unhappy [lah] because (ppb) I could tell that your tour guides were inexperienced because (ppb) they couldn't even communicate basic korean (ppb) and then (um) sometimes when we also asked them you know when we go (ppb) to visit museums and historical places and we asked them some history (ppb) then they were also unable to answer our questions so in the end we just had to google online and we self answered our own question so if that's case then I don't see a point why I should you know hire a tour guide or book your agency if I can get all the questions and answers by myself yup <S> okay I think generally both tour guides were quite poor in korean but (ppb) (um) the one that was espe~ especially more rude was (ppb) (um) the younger one so there's two guide two tour guides one was older one and then another is a younger female (ppb) so I mean sometimes when we ask her questions (ppb) (um) she will come and (um) say things like why do you all need to know so much you just walk and see take pictures can already so she was obviously unhappy about it [lah] so I think that was kind of rude since we are the customers yup (um) I mean I'm I'm not calling to like ask you to fire the staff or like scold the staff I'm I don't need that but (ppb) (um) what I want is for you to train your staffs properly so (ppb) before they even take up any (um) work or take up any trip you know they should be (ppb) at least knowledgeable about the country or the language of the country that they are going to like I I don't need a excellent tour guide but (ppb) the point that they can't even speak basic korean is just unacceptable to me [lah] because that just means that you haven't done your work you like you haven't prepared anything before going to that trip <S> <S> <S> yup (mm) I think I I don't need (um) your company to be accountable because past is the past already [lah] so (ppb) (uh) I don't need like a refund or apology or anything I'm fine with it but (ppb) I'm just calling to just make sure that you know you improve because (ppb) (um) my family and I we have always been (um) whenever we go overseas we have always engaged with your company with your agency (ppb) and book your tour guide so I mean I want to continue this relationship [lah] because (ppb) we have been with your company for many years already but (ppb) this experience really (um) in a sense made me lost my trust in your company a lot because it's just really unacceptable [lah] and just made the entire trip the mood just very bad it was supposed to be a happy holiday but then (ppb) I was annoyed most of the time not just me but my family also so (um) yup I I I don't need you to give me apology or anything but just I hope you can improve and then in the future like I hope I won't see anything like this happen again because I definitely still want to you know (um) hire your agency for my future trips since we have been together for such a long time already <S> <S> (mmhmm) so you mean specific examples is it (mm) I couldn't remember like exact example is because it happened so many times [lah] like (ppb) wherever we go to a new place like for example if we want to buy tickets to enter the museum (ppb) then the tour guide would be ordering the tickets at the counter right but (ppb) you could tell that she's having trouble communicating with (ppb) the the person that's selling the tickets and both of them seemed like very annoyed and stuff like that so I guess that is one specific example that I could remember of and then ya just other occasions also [lah] you can just tell that (ppb) they both the tour guide and the person the korean the local there (ppb) they weren't communicating well because of language barrier <S> <S> yup yup <S> <S> <S> okay 
0.029452908784151077
<S> <S> <Z> part two hi is this fullerton hotel <S> yup okay I would like to make a three days two night (um) reservation from the thirtieth of december to the first of january so I just need one room (um) I'm coming here with my group of friends to celebrate for (um) new year eve so preferably I want the room that allows me to see fireworks so that because I mean after all we are coming here to celebrate the new year for the countdown <S> should be around four to five the num yup yup (um) I'm not really particular about the room size or like the number of beds because (ppb) (um) we are not really going to sleep there because we are just going to party all night and play games so as long as the room is sufficiently large enough to fit us four to five (ppb) and then we are able to see the fireworks then that's okay with me <S> (mm) yup sure that's okay with me <S> okay (um) from the thirtieth of december to the first of january okay okay nice (ppb) (um) may I know around how much is the price <S> <S> <S> so that's for one room right <S> okay sure I think I'm fine with that (ppb) (mm) and maybe just to ask also is there like any facilities that I can use at your hotel throughout our stay <S> (mm) I'm guessing maybe like the gym or swimming pool or like (um) the restaurants and some game facilities <S> <S> <S> <S> <S> [oh] so we can't go there as a group <S> [oh] okay sure <S> so am I able to book now together with this hotel reservation or okay yup sure <S> <S> <S> (mm) not really but (um) probably somewhere that's on the higher level so yeah because I want to see the fireworks so if I see at a higher level it's more nice to see definitely yup <S> (um) I think definitely for lunch we actually don't really need breakfast I guess because my friends and I we don't have a habit of eating breakfast so maybe just lunch and dinner but (um) I probably don't need it for all the three days also because some on some days we might go out of the hotel and eat out near the hotel somewhere near the hotel ya <S> sure okay it's all free of charge right like is it included in the three hundred dollars [oh] okay okay sure I'm confirmed when the date is nearing <S> (mm) (ppo) not really but (um) just wondering do you all have like any reward system so like if I book once then maybe within the next six month if I book another hotel stay then I'll get a discount or something <S> <S> <S> <S> <S> <S> <S> (mm) okay that's nice (ppb) (mm) then is it possible if I also book (um) another reservation for the next time round like right now <S> okay then (um) maybe somewhere around april because (ppb) during that period of time like I have another friend's birthday so since we have this reward system thing then I don't think I'll mind booking another (um) hotel room during april just to celebrate her birthday <S> [orh] okay <S> okay sure so means I have to do it myself online where I can't do it now in this call with you okay yup sure we can do it now <S> okay jane <S> (um) nine triple four and eight triple four <S> so jane at gmail dot com <S> <S> <S> okay is there like expiry date for this reward system thing like <S> (mm) okay then (um) is there like a level of membership kind of thing so means if I accumulated enough points then I'll go to like (um) the silver level if I accumulate enough points in the silver level then I'll go to the gold level or something like that <S> <S> (mm) I see okay okay so (um) okay yup I will just go read up on my own on the membership part because although I'm still be confused about it (um) just to confirm the stay that I'm booking for the (ppb) (um) thirtieth january to the first january it's confirmed right okay <S> !ee! yup just help me straight away do the booking <S> <S> (um) four to five not confirmed yet but around there yup sure okay thank you 
0.02320990338921547
<S> yup part one hello (um) I'm calling regarding the reservation that I've made with your restaurant just about three days ago (ppb) (um) I actually wish to change some details of my reservation so I'm calling to ask if it will be possible to make the changes <S> okay yup so originally I only book (um) a table for four and of course a set meal for four to celebrate my father's birthday (ppb) but this time round we decided to have a more grand birthday party (ppb) so instead of just booking four seats I want to book your entire restaurant so I don't know if that is possible with you <S> okay (um) I'm guessing maybe around fifty guests including like all my extended family my relatives and my dad friends as well (um) I want to hold it probably around next month (ppb) around either on a weekend so maybe the fifth or the sixth december so about one month away from today and I think just yup I just need the entire restaurant and then (ppb) also enough food catering [lah] for all the guests around fifty guests (ppb) and then I also just want a birthday cake for my dad a large one preferably (ppb) maybe red or blue because that's my dad's favourite colour <S> from four to fifty four to fifty yup <S> (mm) I think maybe a cake that is not too sweet any flavour will be fine (ppb) but preferably something like a bigger cake so it looks more grand and more special for my dad's birthday party yup yea yup (mm) I think for the food wise (ppb) (um) just have a wide variety of food so like (um) noodles rice then many different kind of side dishes (ppb) because I'm going have quite (um) a lot of guests so (ppb) all their preferences are different (ppb) and preferably maybe some small food that's easy for children to eat also because (ppb) we have some (um) young children that will be coming and then yup something sweet [lah] for those children also so that (um) it can entertain them and then (mm) in terms of decoration wise maybe just something more grand (um) I don't need it to be very aesthetic it's fine with me just balloons or like happy birthday banner would be fine yeah as long as it's clear that once you step in a restaurant [oh] we are having a party for my dad's birthday party that's sufficient yup <S> <S> <S> <S> (mm) okay (um) for children wise I think maybe we're expecting about five not a lot so just a small portion of food will be fine (ppb) but for the adult wise (um) I guess you can have some #halal# food that is separated from the non #halal# food cause we do have some muslim friends (ppb) and then for the non #halal# food preferably maybe just chinese food [lah] (ppb) those typical food that (um) our older parents our grandparents would like like maybe (um) porridge #dim sum# vegetables yup and also nothing too sweet [lah] because (ppb) my parents don't like sweet stuff so more on the healthier side yup (mm) okay (uh) maybe if possible you could play some music at the background just some comfortable one so that you know we can lighten up the mood yup <S> <S> <S> okay yup sure I'll bring it on the day itself yup and then (mm) maybe for the restaurant itself like could you put some cloths over the table <S> (um) maybe red so it looks more auspicious and more to my dad's liking yup <S> <S> <Z> yup so so all these changes will be possible right because (ppb) I only want to book the date from one month from now so there's more than enough time for the changes to be done <S> <S> <S> okay sure yup yup and (um) if you are not able to make the changes maybe could you inform me earlier so I can (ppb) cancel this reservation and go to another restaurant okay sure (mm) and (mm) would I don't know if it'll be possible but do you have some games or anything in the restaurant because I'm thinking that (um) for the young children who are coming they might get restless and bored easily because they don't talk as much as adults do (ppb) so if you have some games or some (ppb) (um) toys to entertain them in the restaurant that will be great <S> <S> okay sure <S> <S> (mm) I think definitely you should have some a mixture of both hot and cold drinks (ppb) and for your hot one maybe just tea or coffee yup for all the older age group who prefers hotter drinks (ppb) then for the cold drinks maybe something sweet for the children like (um) ribena or milk also milo and any soft drinks so just a wide variety [lah] to cater to different people cause we all have different preferences <S> (mm) okay I think alcoholic drink is fine but make sure you separate them because like I said we have some muslim friends so if you put all the drinks together I'm afraid they might be uncomfortable with that yup <S> okay (um) I think malays maybe around ten to fifteen yeah then the rest are all chinese so (um) don't have to make a lot of food for the muslims but just (uh) make sure they are #halal# [lah] cause I don't want my guests to come and then (ppb) they don't have anything to eat that's a bit rude [lah] yup nope okay <S> thank you <S> 
0.02654053084552288
one two three part three <Z> yup that's right (mm) <Z> <Z> [oh] okay thanks thanks for that thanks for the compliment and then we are happy to hear that (ppb) would you mind to share a little bit of your details so that we can actually or or like your name or your or your contact number <B> (mmhmm) (oh) okay understand you're you're you're talking a~ you're actually referring to the trip (err) to japan like which ci~ which part of the japan you went to <B> [ah] <B> [oh] I see okay yup (uh) can I have the the surname again just to confirm that (err) we are referring to the same person <P2>lily tan</P2> [ah] I see yes yes we do have yup <Z> <B> (mm) okay I see happy to hear that <B>  (mmhmm) ya sure sure I will definitely (err) (uh) definitely (uh) leave this (uh) pass this message to to her as well as to to the supervisor or maybe from your from your end will you possible like (uh) to leave us like a email or to write in to us you can email us or just drop us (uh) some feedback on our [ah] in our website <Z> correct correct we do have so you can go to our (mm) <Z> ya it's the it's the same website correct the asia dot com then from there you can look for the contact us then (uh) under it or in in it would should direct you to the page like to contact (err) to leave us a message or something <B> (mm) okay sure sure sure <B>  other that (mm) other than (err) the tour guide do you just to just to check with a bit further like do do you enjoy the whole trip as in like (uh) all the places that you're you have when you're went to (ppb) or all the food that you have it in japan do you like the arrangement (mm) (mm) <Z> <Z> <Z> <Z> (mm) <Z> <Z> okay I see any memorable (err) places for you like which which (uh) which part of the japan that you enjoy the most <Z> [oh] <S> (mm) <S> <B> okay I see I see that's [oh] that's good to hear that you enjoy the food <B> (mm) other (mm) okay [ah] okay I see okay I see yup (uh) yup that's the something that we special arrange for the for for for our customer and yup happy to to hear that you are en~ you're you enjoy this arrangement <S> (mm) <S> <Z> (err) I think package package five more the rest should be the same (um) but what we have is like if you if you we do have some of this program call like (err) loyal~ loyalty program some rewards program (uh) or the loyalty and rewards program (ppb) so if you continue to take up for (uh) the package with us right we actually have those (uh) like [oh] like discount [lah] on your next trip <B> (mm) <S> yup you ac~ (uh) you basically to accumulate the points the points actually can change back or change to or as what mean by discount (err) earlier on is like you actually can convert the point to to dollar so every twenty points you earn is (uh) equal to one dollar so yup you can use it for your next trip <Z> <Z> yup you have to go to the website to set up or you can actually or do it with me now you can provide me some of the details then I can (uh) I can do the sign up with you now as well <Z> (err) I will advise that you all sign up for one for one [ah] one person to sign up only so that can you all because some of the some of the places you might have some minimum (uh) minimum points or something so it will be good that if you're always travel together it'll be good to only get one representative to sign up for the program <Z> <Z> ya I'm sure it's actually under our website the asia dot com so (err) you can look for the you can look for the our reward program cust~ (err) loyal loyalty rewards program (mm) you can just sign up to become a member there's no charges on it is a free of charge (err) free of charge so (uh) we will on and off we'll have a different different of the program or some of the season we might have (err) different point rewards we actually will notify you all <Z> correct that's correct <Z> yes we do have yup we do have a facebook page for it yup <Z> <Z> yup normally we have any promotion we actually will post it in the (ppb) (uh) in our w~ website of course and as well as the social media like facebook this instagram <Z> <Z> [ah] it's the same name as our company the actual is a asia travel asia dot com the same as for the I_G okay is there anything else we can help you <Z> <Z> no prob~ thank you bye bye 
0.029989399015903473
<UNK> okay one to three part two <Z> <Z> ya that's correct X X X hotel here <Z> yup we do host event for different [oh] yup we do hold events <Z> [ah] yes we do have room for forty people we have a we have actually a a few function room for this but could you would you <B> (mm) (mm) (mm) (err) I mean we we do have a room for those events like no ma~ [ah] we have (uh) we cater for different different teams but would you mind to share a little bit more like how you would like to have it for this (err) for your class reunion events so in order for me to share with you the about the package <Z> <Z> (mm) okay okay [oh] for your session it will be more like (uh) have a chit chat session to each other like as you say like it's a reunion for your classmate with your within your classmate (ppb) or do you all have like or some games in between so if like like likely how's the thing that you would like to have <Z> <Z> <S> do you need a stage for that <Z> okay (uh) yup we do have (uh) provide a stage <Z> <Z> yup that will be a different yup that will be a different charges <Z> okay [oh] so we do have a four different of the event room to cater for your for your size forty (ppb) the normal one we will count as a count like a like more like a like a meeting room where you are have a it should be enough for you for you all to have like (uh) four round table for forty alright the for the one we can we serve foods the other room is like a we we can have a limit of a a a small corner for have a small activities and you have can have some (ppo) some people might have their photo booth or some people might want to have some decoration over there you can have you can do it (ppb) (uh) this one normally people is a more have like or they (uh) at the front that have so~ they have a you can have a the it's more like [oh] the table we will serve in (uh) like a buffet style and you have a some cocktail table as well okay <Z> (uh) it come in a smaller size for the for the for the one that with a with a with a more (ppo) like a buffet style yup that's about the buffet style (mm) <Z> <Z> that can be done that can be done [ah] actually the room can fit (uh) fit for six table but six is the max already (ppb) or if you want to have a bigger space then you might need to take another another package for that (mm) <Z> <Z> yup we do have a few menu [oh] but before that what would you would you mind to let me know a little bit more like about your requirement first regarding about the food like or do you have any restriction for the food or or what kind of style that you are looking at or what kind of cuisine that you are looking at (mm) <Z> <Z> <Z> <Z> (mmhmm) <B> okay <B> okay <Z> <Z> [oh] there's no additional charges on it but then (ppb) we come in a we come in like a what kind of how many like a maybe if you're looking for ten (ppb) ten different dishes in a with more like a package [lah] ten dishes then it will come in a in a price you can actually select like how many of it you want to be want to be (uh) want it to be a halal how many of how many of the dish you want to be to like a vegetarian yup so for your case you would like to have it like (uh) like how people serve in a like wedding ceremony (ppb) in in (ppo) or you want it to be in a buffet style you want it to serve in like a <Z> <Z> yup serving once or y~ yup (ppb) correct <Z> <Z> (uh) so if you go like (uh) for the for the for the the minimum you have to like serving by (uh) those are serving in (uh) dish by the dish right that one will be like [oh] there will be ten dishes in minimum have to be a ten dishes it comes with a starter then come the come with all the drinks and as well as a dessert at the end so it will be roughly for ten pax or eight to ten pax is about is about thousand five <Z> if you go by buffet style we count by (err) per pax so depends on the o~ the order but then minimum you have to (err) to take for the room for the the room that I mentioned to you earlier you have to need to make minimum order of forty pax so per pax will be a hundred <Z> yup we can actually or once you confirm everything actually we can I'll email you the menu you can actually pick (err) do some (uh) customise your own menu you pick and choose from there <Z> <Z> <Z> (ppb) I think for now we are not able to (err) so once you all have the decided (err) the the seat then I'll throughout the throughout the session you all have to be remain (ppo) the the same table (ppb) and not mingle around or move around yup <Z> I think within the same table you might still able to (ppl) <Z> <Z> [ah] there's no postponed or to co~ or if like supposed postpone into or still within the same or within the (ppb) within the three months within three months and then (uh) based on our availability (ppb) there's no any charges but you have to be like [oh] two weeks in advance notifica~ or to let us know [lah] <Z> okay (err) based on the based on the reason of the cancellation okay and also it's also subject to (err) it was also had to be like (uh) you have to let us know in advance as well like two weeks with (uh) two weeks before there's no additional there's the we will refund back to you hundred percent <B> yup yes correct unt~ unless you can un~ (mm) unless you can provide a (ppb) a valid reason like for the for your cancellation <Z> <Z> (err) that's (err) depends on the maximum capacity of the room so if let's say you go for the room two that I suggest to you earlier so the max you can go is a until six (uh) is to sixty <Z> <Z> alright that's all thank you 
0.019997049123048782
okay done alright one two three <Z> part one <Z> yup X Y Z restaurant here <Z> yup we do have some special order for I mean (uh) we do have some special dish for today (ppb) [oh] we do have western western western food yup like what you say spaghetti today we have lobster spaghetti we have lobster burger (ppb) <B> (mm) [oh] actually this both is quite it is like almost almost the same <Z> yup sure but however can I just (err) ma'am can I just have your name and your contact number and all your (ppo) address before we can proceed for the order <B> (mm) (mm) okay and (err) you would like to pick up or delivery <B> yes we we did (uh) could you provide me your post (uh) could you provide me your postal code so that we have a different charges for the different area <Z> (uh) give me a minutes there will be a four dollar delivery charge <B> yup there's no charges on it no there's no charges on it <Z> yup we only have self pick up and delivery however if you because since that you order our special order today which is the <S> or e~ either the lobster burger or the lobster spaghetti we do have this (uh) (uh) like promotion [lah] as in we have this one to one promotion for you <B> yup ya right [oh] it can (uh) cannot ma'am it have to be the the same item <Z> yes that's right <Z> yup there is some [oh] the the clam is from a little of mustard a bit of (uh) i~ it have a few choice here or what is your preference you likes something spicy or or what your su~ or maybe can tell me what your preference <Z> <Z> <S> [oh] it might be a bit difficult for to not have a seafood for the lobster <UNK> <Z> <S> <Z> if you not do not to if you can take a little bit of spicy we do have this thai chilli sauce which is sweet and spicy ya ya we do have mustards mustard as well if you want it to be totally non-spicy you had had choose the mushroom sauce or the #teriyaki# sauce <B> (ppb) (uh) #teriyaki# is one of the famous one and the thai sauce is also (mm) but for your order you have a one to one so you can you have to burger so maybe ya ya right (uh) no for the sauce you can choose <B> spicy ya we have thai sauce chilli we have mustard as well which one you will prefer <Z> [ah] okay okay sure alright that's for your burger (ppo) any special request for the burger beside all the sauce <S> (uh) it come with vegetable all (uh) lettuce and then you have some tomato cucumber as well <B> and [ah] ya so I will remove the olive for you <B> okay (err) no it can add-on or you can add-on for cheese if you want to <B> (uh) one fifteen okay do you have any preference for the cheese we have a what types of cheese that you want <B> okay sure <S> <B> yup we do have a it come in a set (uh) in a meal set or in a in ala carte if you'd like to have a in a meal that come with a drinks and a side dish you have a few choice of the side dish <S> yup we serve (uh) in cold drinks (err) as a hot drink as well so you can have hot either a hot or cold drink <B> ice coke alright yup we have coffee [oh] we have coffee we have a we have different account called we have different coffee like latte cappuccino (ppb) for the tea wise we have those (uh) english breakfast tea <B> earl grey yes with it <B> (mm) no it's the same <B> okay sure okay we do have cold (uh) cold side dish and hot side dish so you will prefer (err) give me a minute [ah] okay for your one you can choose two you can choose two side dish so you would like to go for cold or the or the <B> hot side dish okay yes we did we…

---
## [Kingkalamz/printf](https://github.com/Kingkalamz/printf)@[11144f0fb3...](https://github.com/Kingkalamz/printf/commit/11144f0fb3f27a5538082c7e194654630608f935)
#### Sunday 2023-03-26 13:11:09 by Kingkalamz

I'm not going anywhere. You can print that wherever you want to. I'm here and I'm a Spur for life. // Education is when you read the fine print. Experience is what you get if you don't. // With a face like mine, I do better in print. // What one has not experienced, one will never understand in print. // Nothing in fine print is ever good news. // My weakness is wearing too much leopard print. // How is the world ruled and led to war? Diplomats lie to journalists and believe these lies when they see them in print. // The big print gives and the small print takes away. // Sarcasm is lost in print. // Print some money and give it to us for the rain forests. // The negative is the equivalent of the composer's score, and the print the performance. // It's depressing when you're still around and your albums are out of print. // Every time that I wanted to give up, if I saw an interesting textile, print what ever, suddenly I would see a collection. // Print is the sharpest and the strongest weapon of our party. // The flood of print has turned reading into a process of gulping rather than savoring.

---
## [NewSoupVi/Archipelago](https://github.com/NewSoupVi/Archipelago)@[6d13dc4944...](https://github.com/NewSoupVi/Archipelago/commit/6d13dc494455bef97e0f1afc8928853f71d5b5ad)
#### Sunday 2023-03-26 14:19:26 by el-u

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
## [ShadowUser17/awesome-docker](https://github.com/ShadowUser17/awesome-docker)@[3164d6df94...](https://github.com/ShadowUser17/awesome-docker/commit/3164d6df94f60d7d3d11629241c111ed416eb8eb)
#### Sunday 2023-03-26 15:01:44 by Derek Lee

Add Kurtosis to list of testing tools (#1063)

* Add Kurtosis to list of testing tools

Hey team! We'd like to add Kurtosis to the list of testing tools. 

*What is Kurtosis?* Kurtosis is a built system for multi-(docker)container test environments. 
*What is Kurtosis for?* Kurtosis is for engineers who dev against large distributed systems/applications and who experience pain when trying to configure multi (Docker) container environments for their testing workflows. 

Kurtosis can be used locally without the need to sign up and is free-forever under a source-available license (BSL). 

We have:
- Linked out to our Github: https://github.com/kurtosis-tech/kurtosis
- [A README on our GIthub](https://github.com/kurtosis-tech/kurtosis#readme)
- Content about how to setup/install the project (in our [Github README](https://github.com/kurtosis-tech/kurtosis#to-start-using-kurtosis) and on our [docs](https://docs.kurtosis.com/install)),
- Lots of great examples on: [Github](https://github.com/kurtosis-tech/awesome-kurtosis#awesome-kurtosis-) and in our [docs](https://docs.kurtosis.com/). 

I followed the [Quality Standards](https://github.com/veggiemonk/awesome-docker/blob/master/.github/CONTRIBUTING.md#quality-standards) you guys wrote, but please let me know if you've got any questions about Kurtosis or if we missed something!

Thanks

* add "composable" to description

---
## [AOSP-Krypton/frameworks_base](https://github.com/AOSP-Krypton/frameworks_base)@[bc1fc05c1b...](https://github.com/AOSP-Krypton/frameworks_base/commit/bc1fc05c1b3e8c407fa07b25777bf577d5285f49)
#### Sunday 2023-03-26 15:25:09 by Nick Pelly

Delay 500ms between each registering each SDP record using sdptool.

This is to workaround an issue where SDP records will fail to register using
sdptool. When we run SystemService.start() it forks sdptool, so if we do this
four times in a row these forked processes can run in parallel, and one or
more of them fails. There is probably some thready safety issue in sdptool
or Bluez that makes it unsafe to run sdptool in parallel.

As a workaround, delay 500ms between each run of sdptool to register SDP
records when starting Bluetooth.

Before this fix it was easy to reproduce problems with service record
registration. If you turn BT off/on multiple times you can see that sometimes
one or more service records are missing. Repro rate is about 20% in my tests.
Result is that remote devices cannot connect to the missing service.

After this fix I am unable to reproduce any missing SDP records, after 30+
cycles of BT on/off. Motorola BT team also ran stress tests overnight with this
fix and were unable to reproduce the missing SDP records.

This is a low risk fix. It does delay some records from being registered
by an additional 1.5 seconds (on top of the 3 second delay we already had),
so if you try and very quickly connect a BT service after turning BT on it
won't work the first time.

Do not merge. (I will use a less hacky fix for MR2/Master)

Change-Id: I305c181c3194e8ce25e3825320cc2e1ef6d3d3cc
Bug: 2180800
DrNo: eastham
Joke: Why can't you play cards in the jungle? Because there's too many cheetas!

---
## [AOSP-Krypton/frameworks_base](https://github.com/AOSP-Krypton/frameworks_base)@[1ba101f82e...](https://github.com/AOSP-Krypton/frameworks_base/commit/1ba101f82eae4e54293428480fbcbfd1c58359c8)
#### Sunday 2023-03-26 15:51:14 by Steve Howard

Improve accelerometer-based orientation sensing.

There were three main complains about orientation sensing:
* Switching to landscape when putting a device down on a table (or picking it up)
* Changing orientation due to road bumps or vehicle vibrations while in a car dock
* Switching to upside-down too easily

This change includes three primary enhancements.

First, we run the accelerometer output through a lowpass filter before considering its orientation.  This avoids glitches due to brief phone movement, particularly when the phone hits a table.  The filter uses a very low default time constant of 200ms to retain responsiveness (note the samping period is ~200ms, so the effect of this filtering is pretty mild).  At tilt angles beyond 45 degrees, however, we increase the time constant to 600ms, which helps greatly with avoiding glitches picking the phone up from a table.  It does introduce some sluggishness when rotating while the phone is tilted back, i.e. being used in one's lap.

It's also worth mentioning that the accelerometer output on Sapphire appears to be pre-lowpass-filtered with a time constant of around 500ms, making this less necessary on that device, but the added effect doesn't noticeably degrade user experience in my opinion.

Second, we check the magnitude of the raw accelerometer output.  If it deviates from the strength of gravity by more than one m/s^2, we distrust the data, since that implies the device is under external acceleration and the sensor data doesn't accurately reflect orientation.  This helps avoid glitches due to shocks and vibrations, as in the car dock scenario.  However, rather than ignore the data entirely, we filter it with a very high time constant (5 sec).  As a result, if the device is rotated while vibrating, even if we never pick up a clean sample, we will eventually detect the orientation switch.  Of course, with a sampling period of 200ms, we're prone to aliasing, but that seems like a highly unlikely corner case.

Third, we restrict transitions to upside-down orientation to a much narrower range, both in terms of orientation and tilt.  This should prevent upside-down mode from activating in most cases where it's not desired.

I also updated a lot of stale documentation, added a lot of documentation, and cleaned up a lot of the code, so as to make this (often subtle) code as transparent as possible.

---
## [trydevhub/hitori](https://github.com/trydevhub/hitori)@[d6a48c04b4...](https://github.com/trydevhub/hitori/commit/d6a48c04b4d6f2d46478b4448433a7cb29ee62d0)
#### Sunday 2023-03-26 16:35:50 by Chiko

style(formatter): lets try some rome (#7)

* style: fuck you prettier

* fix: forgot to add the folders

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[d72ef99270...](https://github.com/tgstation/tgstation/commit/d72ef99270f2697064681b3214f0569dcf38d526)
#### Sunday 2023-03-26 16:40:54 by necromanceranne

Goliath-Infused Tendril Hammer uses an internal cooldown for the its special attack instead of a universal click cooldown (#74159)

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

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Rex9001/Rex-station-](https://github.com/Rex9001/Rex-station-)@[4599842d7c...](https://github.com/Rex9001/Rex-station-/commit/4599842d7c6b5ed499307f92a6f8032d598b7889)
#### Sunday 2023-03-26 17:04:37 by Jacquerel

Makes Shake() proc work (#73480)

## About The Pull Request

Fixes #72321
Fixes #70388

The shake proc didn't work and hasn't for ages.
I remember it having worked at some point, but it was quite a long time
ago.
I cannot guarantee that the end result here is the same as it was, the
reason here being that I have no idea how this proc ever worked in the
first place. My limited understanding of the `animate` proc implies that
the previous implementation as written would never have acted as you
would expect it to, but clearly at some time in the past it did work. A
mystery.

As a result of the previous, possibly because the proc never _did_ work
as expected and just did something which looked vaguely correct most of
the time, both the default values and the values people were passing
into this proc were completely ridiculous.
Why would anyone ever want to pixel shift an object with a range of _15_
pixels in all directions? That's half a full tile! And why would you
want it to do this for 25 seconds?
So I also changed the values being passed in, because you really want
pretty small numbers passed into here most of the time.

Here's a video of everything that vibrates:
https://www.youtube.com/watch?v=Q0hoqmaXkKA

The exception is the v8 engine. I left this alone because it seems to
try and start shaking while in your hands, which doesn't work, and I
don't know how to fix that. This has potentially _also_ never worked.

## Why It's Good For The Game

Now you can see intended visual indicators for:
- Lobstrosities charging.
- Beepsky being EMPed.
- The Savannah Ivanov preparing to jump.
- The DNA infuser putting someone through the spin cycle.
- The mystery box admin item I had no previous idea even existed (fun
animations on this one).
- Anything else which wants to use this proc to create vibrating objects
in the future.

## Changelog

:cl:
fix: Lobstrosities and Tarantulas will once more vibrate to let you know
they're about to charge at you.
fix: The Savannah Ivanov will once more vibrate to let you know it's
about to jump into the air.
fix: The DNA infuser will now vibrate to let people know that it's busy
blending someone with a dead animal.
/:cl:

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[4383fda8d5...](https://github.com/treckstar/yolo-octo-hipster/commit/4383fda8d5b4b83293d26173d433761a673d8c92)
#### Sunday 2023-03-26 17:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [ARF-SS13/coyote-bayou](https://github.com/ARF-SS13/coyote-bayou)@[aaa23be87d...](https://github.com/ARF-SS13/coyote-bayou/commit/aaa23be87dd116c43f24b2c0b35e0ad0e09dd7e7)
#### Sunday 2023-03-26 17:31:54 by Superlagg

Merge pull request #1776 from ARF-SS13/fuck-you-ghd

Trash Stack Desc fix

---
## [meemofcourse/Shiptest](https://github.com/meemofcourse/Shiptest)@[84a2a8f394...](https://github.com/meemofcourse/Shiptest/commit/84a2a8f394a0296ecc527f23c0da470b30280c0c)
#### Sunday 2023-03-26 17:35:02 by Bjarl

Die Of Fate Change (#1760)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
replaces the die of fate's d20 effect (spawn you as wizard) with spawn
wizard clothes and magic mirror under you.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
I'm sick of wizards spawning without admin intervention
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
balance: You can't be turned into a wizard by the die of fate, instead
getting a magic mirror and wizard clothes.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [amitpatra/fucking-algorithm](https://github.com/amitpatra/fucking-algorithm)@[15b428a8ab...](https://github.com/amitpatra/fucking-algorithm/commit/15b428a8ab2d3bf09c3f710f90a2240bed0b39c8)
#### Sunday 2023-03-26 17:36:12 by Tomasz Surowiec

[English] Correct Edit Distance 

(I feel a need to preface this by saying that the changes I made were based solely on the English version, and the reading experience, for I do not speak Chinese (I'm not even sure if it's Mandarin, Cantonese or which one, nor if there's any difference in writing). Should you object to any changes, please let me know)

1. Changed the apostrophe character from *`* to *'*. The former is not used as an apostrophe, and is actually an accent mark (for preferred characters, refer to (this)[http://snowball.tartarus.org/texts/apostrophe.html] (U+0027 ', U+2019 ’, U+201B ‛)).
2. Changed certain verb forms. For instance: *"The last question is that **writing** a function to calculate [...]"* to *"The last question is **to write** a function which calculates [...]"* (also *which* -> *to* in order to avoid the repetition).
3. Changed the capitalization where necessary. For example: *Helpless* to *helpless* (since it's not a proper name); *We* to *we* (middle of a sentence).
4. Changed a few verbs to nouns, and vice versa: *"explain"* (on its own serves as an imperative, which would demand that the reader explain it) to *"explanation"*; *"storage"* to "store [the least editing distance of s1 and s2; L226]".
5. Fixed redundant spaces: *"[...] `s2`  in [...]"* to *"[...] `s2` in [...]"*; *"s1[i]！=s2[j]"* to *"s1[i] != s2[j]"*
6. Changed a few odd phrases: *"a violent solution"* to *"a brute force solution"* ( (most)[https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiolLjsxK3xAhUspIsKHU-9BwEQFjADegQIBBAD&url=https%3A%2F%2Fgsdrc.org%2Fwp-content%2Fuploads%2F2019%2F11%2F671_P-CVE_Programming_on_Men_Women_Boys_and_Girls.pdf&usg=AOvVaw2QjJ_-yjxxw2oWYtG77sgE], albeit (not all)[https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiolLjsxK3xAhUspIsKHU-9BwEQFjABegQIAhAE&url=https%3A%2F%2Fwww.programmersought.com%2Farticle%2F27011223160%2F&usg=AOvVaw1f6OCbf1r7M8GAfmGotBDg], uses of the former did not refer to programming ); *"from the bottom to up"* to *"from the bottom up"* (or *"bottom-up"*; see: (from the bottom up)[https://www.lexico.com/definition/from_the_bottom_up], and (bottom-up)[https://dictionary.cambridge.org/dictionary/english/bottom-up] ); *"operation number"* to *"the number of operations"* (this one might have been more subjective).
7. Removed latex dollar signs (since github markdown does not support it): *"$O(min(M, N))$"* to *"O(min(M, N))"* (as used in other articles).
8. Pluralized certain nouns after *"any"* ( ("We use any for indefinite quantities in questions and negative sentences")[https://dictionary.cambridge.org/grammar/british-grammar/any] ): *"any operation"* to *"any operations"*.
9. Added some formatting: "dp(i, j)" to "`dp(i, j)`" (L98).

I'm also not sure if *"[...] I wrote some words out of place by mistake"* refers to mistyping, but it's still more than clear, albeit slightly wordy.

To reiterate, should any of these be of concern, let me know, especially since it is my second language.
Best regards

---
## [openai/evals](https://github.com/openai/evals)@[114f4f8536...](https://github.com/openai/evals/commit/114f4f8536f29df43e5145fd38826285d19d6728)
#### Sunday 2023-03-26 17:40:02 by Greg Priday

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
## [RSNara/react-native](https://github.com/RSNara/react-native)@[7bf8d7fc29...](https://github.com/RSNara/react-native/commit/7bf8d7fc29293fbdf1e22ee4ff8eda2376dadb48)
#### Sunday 2023-03-26 18:09:39 by Ramanpreet Nara

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

fbshipit-source-id: dc2eddcf7d0721d99155fb8aacf4c2c8a1d26e4a

---
## [FireNick44/M151-laravel](https://github.com/FireNick44/M151-laravel)@[274d9d329c...](https://github.com/FireNick44/M151-laravel/commit/274d9d329cc7c1fd1469b96d6de8366fad0730be)
#### Sunday 2023-03-26 20:02:20 by Y

BLING BLING 🤡🤡🦁🦁

why😍you🤚🏼always🤡cry👁on😔social❤️media🧚🏿 ✨𝓼𝓱𝓾𝓽 𝓽𝓱𝓮 𝓯𝓾𝓬𝓴 𝓾𝓹✨🧚🏿DAMN

just renegade the sad away 🧚🏽

I 🥺 don’t 💕 see😌 how 👁 you 👽 can🤦‍♂️hate 😜 from🧚‍♀️my 🥳 side👄 of 🖤 the😈 club😹 you 🗣 cant👅 even 💅 get 🕴🏽 in

𝔁𝓾𝓮🥶𝓱𝓾𝓪🧚‍♀️𝓹𝓲𝓪𝓸😻𝓹𝓲𝓪𝓸🗿𝓫𝓮𝓲👺𝓯𝓮𝓷𝓰🤩𝔁𝓲𝓪𝓸😼𝔁𝓲𝓪𝓸👣

ür ńáwt ïñvītëd tø thė tré 🌲

she👩🏽 like🌂papî 🍰I 🍾adore 💘you🤸‍♀️i’m 🛍like 🩸baby 🎀 i 🖍ain't 💅normal👩‍🦯 Rrrrr 🦁 🦁🦁 foreigner 💕foreigner 💕

🧚🏻✨𝓼𝓱𝓾𝓽 𝓽𝓱𝓮 𝓯𝓾𝓬𝓴 𝓾𝓹✨🧚🏻

chicken 🐓 wing 🍗 chicken 🐓 wing 🍗 hotdog 🌭 and baloney ✨ chicken 🐔 and macaroni 🍝 chillin 🥶 with my 😘 homies 👯‍♀️

look for the gummy bear album in stores on november 13th 🦋✨🌈💞🧚‍♀️

there’s💅alot🙇🏼of🌾people👯‍♀️in👑𝒜𝓂𝑒𝓇𝒾𝒸𝓊𝒽 👄in🧚🏼𝒜𝓂𝑒𝓇𝒾𝒸𝓊𝒽👣 ǟɦɦǟɦɦ😔over😳300👀milion🤯in✨𝒜𝓂𝑒𝓇𝒾𝒸𝓊𝒽🇺🇸

these comments are so mean😔✨💖listen to them girlie🥰💫🧚‍♂️

There’s always room for improvement.💕 but it’s not in this room, get out🧚🏻‍♀️✨💟

aww i was having a bad day🧚🏻‍♀️💫🥰💞this made it worse🤩😘

twins🥺✨ but make them 🌸💖tOweRz💓🧚🏼‍♀️

confidence is key 🧚✨ throw the key away 🥰😘😊

God really do be choosing favorites 😍✨🌸 not you tho! 🦋😘🧚

Just keep smiling 💖✌🏻😘 I love the color yellow ✨🧚🦋

Day 🌞 to 💦✌ night 🌙 to 💦💦 morning, keep with me 🙏😈 in 💁⬇ the moment 🕑🤔 I'd 💉 let 😤👍 you 👈🏼 had I 🕵👁 known 💫👁 it, 💓 why ♀ don't 😡🙈 you 🏻🏿 say ☝ so? 💯 Didn't 😘😘 even 🌩🌃 notice, 👎👎 no punches left 👈🌰 to 🅱🚶 roll with You 🅱 got to 🔵 keep me focused, 😤 you 👀👤 want it, 🥇 say 😫 so Day to night 👉 to 😛🅱 morning, keep 🙊 with 😲🍨 me 🙈🗡 in 🙍👌 the moment 😳🤔 I'd let you had 😭🍆 I 👈💯 known 😝 it, 💯 why 👨 don't you 👈 say so? Didn't even 🌃😷 notice, 👎 no 🚫 punches left 👈 to 🔎 roll 🔄🎶 with 👏👏 You 👏 got 🏻 to keep 🏃 me focused, you want it, 🗯😝 say 🗯 so 💝💯 It's 🤔❗ been 🍀💫 a 👌 long time since you 😣👏 fell 🅾 in ♂ love 😇 You 🏻😛 ain't coming out your 👈😍 shell, 🐚🐚 you 🏻 really 🙏 ain't been 💴🥜 yourself 😝☝

---
## [spockye/tgstation](https://github.com/spockye/tgstation)@[3156a0414e...](https://github.com/spockye/tgstation/commit/3156a0414e96b597d4d53823066d29daa0b30737)
#### Sunday 2023-03-26 20:19:45 by san7890

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
## [FireNick44/M151-laravel](https://github.com/FireNick44/M151-laravel)@[6006992913...](https://github.com/FireNick44/M151-laravel/commit/600699291354373467eef75f200c46832f2c7305)
#### Sunday 2023-03-26 20:43:07 by Y

 IT WORKS 50 POINTS FOR D20a!!!
🥵🥵🥵😈😈😈👿👿👿👺👺👺👹👹👹☠☠☠

You dropped this 🔴 put it back on your nose 🤡🥰
Stop posting negative comments 😌🍃 I can’t stop liking them 🤩🤪
You can do anything you put your mind to ✨💞 just not this 💖🍃⭐️
You look tired 🥺 go take a permanent nap ✨ u deserve it queen 💖
Take a deep breath ✨💕🌈 now hold it in 💫🌈😉
Thanks for sharing 💖🧚 please don’t ever share again though 💖🧚
You ate this up ✨🧚 I recommend starving tho 💕✨
You're definitely going places 🌈🌸 when you do, don’t come back 😘
Oh chill out this is all a joke 💕🧚🏼👑😌 like your life 🥰👑❤️🧚🏼
The video is so nice! 💖🌸 try it without you! 🌞🥳
Dancing is a talent 🥺💐🦋 but not urs 😘☘️🙈
I’m pro-choice 💗🙈 because of you 🥰🧚‍♀️
Imagine being that talented 🧚🏼‍♀️✨ yea keep imagining 😍❤️
Fire 💞💅🏻 but make it the dumpster ⭐️💕
You go girl 🌈🌨 no like literally, leave 🍒🌋
I have a bath bomb for you 🦄 its called a toaster 💫🧚‍♂️
Look on the bright side 🥺💕🧚‍♀️hope it blinds u ✨😌
Bob Ross would say 🧜🏼‍♀️🌟 you’re an unhappy accident ✨💅🏼🏔
Life but make it 🥰 end 🥰
I almost scrolled past this 💞🧚🏻 next time I make sure I will 🌸🧚🏻
Maybe men deserve rights 🥰💖🌈 not this one tho 🧚🏻‍♀️🌸🌻
I’d say you did that 🌈✨ but I’d be lying 🦋💗
Here’s the door for new opportunities! 🚪 💕 I locked it for you 🥰👑
Sit on ur throne 💗🌸 but make it electric 💗🧚‍♂️
Anna but make it 🌷 b o r s h i n 🌷
Confidence is key 🤪💫🌹 you’re locked out 🌟☀️💐
Cancer 🤩 not the zodiac tho 💘😚
Be positive bro 🌈🧚‍♂️ for coronavirus 💖
I showed this to my cat 💕 she threw up 🤩
Your showing off the goods 👑🌸 and it burns our eyes 🧚‍♂️🌿
Jumpsuit but make it 🍋 orange 🍋

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[e75a1c00aa...](https://github.com/tgstation/tgstation/commit/e75a1c00aa3bcf2658428a536997f2eca0f25028)
#### Sunday 2023-03-26 20:47:48 by san7890

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
## [sed-i/operator](https://github.com/sed-i/operator)@[ecb9ca1163...](https://github.com/sed-i/operator/commit/ecb9ca1163a3618448e797af645b2e1bd38255ed)
#### Sunday 2023-03-26 21:10:17 by Ben Hoyt

Import (almost) all public names in ops __init__.py (#910)

This is to address #731: it's hard to remember or discover which `ops`
sub-module (like `ops.charm` or `ops.framework`) a name comes from.
That, and imports become a bit of a mess (`from ops.charm import X;
from ops.framework import Y; from ops.main import main`).

In my view we had previously split them up somewhat arbitrarily
(eg: `FooEvent` types are in `ops.charm`, but they could just as well
be in `ops.framework`). I considered a different, more logical
sub-module arrangement, but I think it'd still be hard to remember
and know where things were.

This solution is simple: import all the public names into the
top-level `ops` module in the `__init__.py` file. They're quite
unique, so there's no conflicts. The only exception is `ops.pebble`,
whose names aren't imported there (most charms don't use `ops.pebble`
directly anyway, they use it via `model.Container`, but if you need
it its still readily importable).

This makes all the names easily discoverable, either by looking in
`ops/__init__.py` manually, or via your editor's code completion when
you've done `import ops`. I expect that many charms will change to
just `import ops` and access names like `ops.CharmBase` (`ops` is a
nice short prefix) ... see [this PR on my database test charm]
(https://github.com/benhoyt/test-charms/pull/1/files) for an example
of what that would look like.

Folks can also use explicit imports like `from ops import CharmBase`
if they prefer. And of course the existing usage `from ops.charm
import CharmBase` still works fine too.

The one quirky thing is that `ops.main` is currently a module, but we
want to allow `import ops ... ops.main()` or `from ops import
main ... main()`. To solve this we've main the main module callable
(and it just calls the `main` function). This allows the new usage,
but also allows the existing usages `from ops.main import main ...
main()` and  `import ops.main ... main.main()` to continue working.

### Testing note

The user-facing changes here are all done in `ops/__init__.py` and
`ops/main.py`, but I've also updated the `test/test_*.py` files to
show using the single `import ops` approach (partly to set that as a
precedent).

However, I ran all the previous, unmodified tests against the new
`ops/__init__.py`, and they all pass. This ensures that I haven't
messed anything up, including the `main` shenanigans mentioned
above.

Fixes #731.

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[3bb88402f1...](https://github.com/Buildstarted/linksfordevs/commit/3bb88402f19bbdcc7fa1dd239c574cbb6f28c255)
#### Sunday 2023-03-26 21:14:32 by Ben Dornis

Updating: 3/26/2023 9:00:00 PM

 1. Added: Toward Disposable Software
    (https://www.paritybits.me/disposable/)
 2. Added: Banking Crisis 2023: Who else is in trouble? - What the Hell is Beeping?
    (https://davidschenz.com/banking-crisis-2023-who-else-is-in-trouble/)
 3. Added: About Incremental and Disruptive innovations
    (https://www.antonoriza.com/incremental-disruptive-innovations/)
 4. Added: Experience Replay | Entangled Logs
    (https://entangledlogs.com/archives/2023/xp_replay/)
 5. Added: The Artificial in AI - Pravesh Koirala
    (https://praveshkoirala.com/2023/03/16/the-artificial-in-ai/)
 6. Added: Just update rules between neurons
    (https://www.jtolio.com/2023/03/just-update-rules-between-neurons/)
 7. Added: Software is not defined by the language it's written in
    (https://garrit.xyz/posts/2023-03-26-software-is-not-defined-by-the-language-it%27s-written-in)
 8. Added: I've been programming full time for the past 5 years. Am I a senior engineer yet?
    (https://cuffaro.com/2023-03-26-am-i-a-senior-engineer-yet/)
 9. Added: Putnam on reason, reductionism, and relativism
    (http://edwardfeser.blogspot.com/2023/03/putnam-on-reason-reductionism-and.html)
10. Added: A note to my former self: You're not supposed to take care of everything
    (http://blog.killerstorm.dev/2023/03/a-note-to-my-former-self-youre-not.html)
11. Added: I Started a Shitstorm or Contemporary Journalism Is Embarrassing
    (https://filthydreams.org/2023/03/25/i-started-a-shitstorm-or-contemporary-journalism-is-embarrassing/)
12. Added: Building a DOS ChatGPT client in 2023
    (https://yeokhengmeng.com/2023/03/building-a-dos-chatgpt-client-in-2023/)
13. Added: Techniques for label conditioning in Gaussian denoising diffusion models
    (https://beckham.nz/2023/01/27/ddpms_guidance.html)
14. Added: Retry flaky tests with dotnet test and PowerShell
    (https://conductofcode.io/post/retry-flaky-tests-with-dotnet-test-and-powershell/)
15. Added: CSS-only Widgets Are Inaccessible
    (https://adrianroselli.com/2023/03/css-only-widgets-are-inaccessible.html)
16. Added: I won't buy a YubiKey
    (https://garrit.xyz/posts/2023-03-21-i-wont-buy-a-yubikey)
17. Added: Sparks of Artificial General Intelligence (AGI) in GPT-4
    (https://ibragimov.org/2023/03/24/sparks-of-agi.html)
18. Added: the 2/3 rule for multi-factor authentication
    (https://roman.computer/mfa/)
19. Added: How to be a technology charlatan
    (https://scottlocklin.wordpress.com/2023/03/23/how-to-be-a-technology-charlatan/)
20. Added: LLMs and Declarative Software Development
    (http://aumitleon.dev/llms-and-declaritive-software-development)
21. Added: Ideas have a 2 week shelf life
    (https://stevecorona.com/ideas-have-a-2-week-shelf-life)
22. Added: Techniques for Setting up Peripherals via PIO and DMA
    (https://serhack.me/articles/techniques-setting-up-pheripherals-dma-pio/)
23. Added: 2 Years Of Lessons From Running My Own Bookstore - RyanHoliday.net
    (https://ryanholiday.net/2-years-of-lessons-from-running-my-own-bookstore/)

Generation took: 00:14:18.1331043
 Maintenance update - cleaning up homepage and feed

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[639cfc76ba...](https://github.com/odoo-dev/odoo/commit/639cfc76ba259eea8f38284192017024809173b3)
#### Sunday 2023-03-26 22:00:01 by Romain Derie

[FIX] website: redirect to case insensitive URL if not exact match

Before this commit, if a link to a page was not correct because of a
case mismatch, it would simply land on a 404 page.
While it's correct, as URL are case sensitive, it leads to a few bad UX
flow at the admin/editor level:
- Create a link in your page (on a text or a button eg), type an URL
  which does not exists (to create it after) like /Page
- Click on the link/button you just made, you are redirected to /Page
  which display a 404 with the "Create page" option (correct)
- When you click on that button, it will actually create a page with
  /page URL, leading to a mismatch between the URL you created and the
  page URL.
  Your link/button will still lead to a 404 URL as it points to /Page.

Since it's just a fallback when an exact URL match is not found, it
should not break anything and should not have bad impact at any level
(seo/speed etc).
Indeed:
- It's done through a 302 redirect
- `_serve_page()` is already a fallback case, so it will only make
  the `website.redirect` and 404 cases a bit slower due to the extra
  search query.

The only possible scenario seems to be if the user (mind the uppercase):
- Created a /Page page
- Created a redirect from /page to /another-page

In this case, /page won't land on /another-page but on /Page.
This flow seems unlikely and is not actually wrong either way.
At least, it certainly is less important than ensuring a case
insensitive fallback.

Finally, note that another solution would have been to either:
- Force page URL to lower case.
  -> This is not stable friendly, people might be relying on this to
     create pages with different casing:
     `/Batman-VII-The-Dark-Knight-Whatevers`, while not recommended,
     doesn't sounds idiot.
     On top of not being stable friendly, we probably want to keep
     offering this possibility
- Redirect all URLs to lowercase endpoints.
  -> This is obviously not stable and not Odoo's jobs. It should be
     something decided by the sysadmin and done at nginx (etc) level.

task-3110294
opw-3104030

closes odoo/odoo#109812

Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>

---
## [Zergspower/Skyrat-tg](https://github.com/Zergspower/Skyrat-tg)@[44ffcdfcc7...](https://github.com/Zergspower/Skyrat-tg/commit/44ffcdfcc7e628b06618f25e34bd14fea8e164a2)
#### Sunday 2023-03-26 22:05:08 by SkyratBot

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
## [stinky-lizard/tsorcRevamp](https://github.com/stinky-lizard/tsorcRevamp)@[497b91fb91...](https://github.com/stinky-lizard/tsorcRevamp/commit/497b91fb91317eb98fbc819ec0645b15910d553d)
#### Sunday 2023-03-26 22:25:21 by timhjersted

Phoenix Trio Revamp 1.0 + more

- The Phoenix bosses now have several new attack elements, some of which activate during a new 2nd phase at half health
-Corrupted Jellyfish renamed Obsidian Jellyfish and given wider spawn pool and HM stats, enabling potential interesting gameplay interactions with the map, (intentionally getting hit can give 30s of lava immunity), to go with the obsidian theme, they also have 999 defense requiring 5 or 10 hits to kill
-Created new banner placeholder sprite
-Added "Cracked Dragon Stone" which provides early HM access to On Fire! immunity, which will be useful during The Rage fight (can be crafted from Cobalt Bars or drops from Ancient Demon event as an expert drop)
-Bloodred Moss Clump now heals for 30HP, up from 20
-Ancient Demon now has a boss bag
-Ancient Demon and Oolicile Demon have better boss bag sprites
-Pwnhammer removed as a Wall of Flesh drop, WoF now drops Molten Pickaxe, which is also now used to craft Mjolnir
-Nerfed Corrupted Tooth healing, now has a 1/20 chance when attacking corrupted enemies, 1/10 chance for anything else
-Basilisk walkers and shifters as well as the Dworc family now has a chance to drop Bloodred Moss Clump
-Mutant Toads can now swim in water and have HM stats, plus 2s of Venom debuff in HM
-EoW and Golem damage stats bumped again slightly
-Cursed Dragon's Breath and Frozen Dragon's Breath now activate their most brutal debuffs after The Hunter and The Sorrow have been defeated
-Frozen Dragon's Breath adds 3s of Frostburn
-Enemy Black Fire kill sound changed
-Added Ice Spirit projectile which has a homing effect
-The Hunter's Miracle Sprouter/Vines emit more light for visibility
-Worm Food and Pwnhammer blocked via no drop/craft list

---
## [stinky-lizard/tsorcRevamp](https://github.com/stinky-lizard/tsorcRevamp)@[8fea941afa...](https://github.com/stinky-lizard/tsorcRevamp/commit/8fea941afa122afe297bb199a83c4c7b3e295788)
#### Sunday 2023-03-26 22:25:21 by timhjersted

Created Dragon Crest Shield + new sprites for later use

-Added Dragon Crest Shield, which consumes stamina to absorb damage; it drops from a secret boss in the Oolicile Forest
-Added Faraam, Gael, Havel,, Nameless King, Greirat, and Seigward sprites, for potentially turning into bosses later (permission granted by spriter) - we could potentially use Leonhard as a base but the animation frames don't match yet - alternatively, we could tweak the animation code to work with all of these sets, as they're all uniform
-Ancient Demon has correct health
-Hero of Lumelia will spawn corrupted hammers and teleport if she loses sight of the player for too long
-Added 'final stand' attack for Hellkite Dragon and reduced movement speed a bit
-Increased Seath's health and soul drops
-Added MP compatibility for Hunter spawn? (not entirely sure if necessary)
-Blocked small, normal and large female zombie, because silly, also blocked small, normal and large variant of normal zombie in HM, though was tempted to block them entirely, to clear room for more interesting enemies

---
## [stinky-lizard/tsorcRevamp](https://github.com/stinky-lizard/tsorcRevamp)@[63754eeb2a...](https://github.com/stinky-lizard/tsorcRevamp/commit/63754eeb2a66d46912061094173e2fdaf6ce678d)
#### Sunday 2023-03-26 22:25:21 by timhjersted

More Phoenix Boss Changes +

-Cracked Dragon Stone also grants immunity to slow and chilled, and costs more souls
-Hellkite Dragon and Seath now interact with the environment in a very cool way (they hit walls instead of pass through them and fly above the ground instead of diving into it more often) but they can still phase through walls when needed to reach the player (further experimentation needed with the 10 and 100 value to find the best balance). It phases through walls more liberally currently to be on the safe side.
--
Phoenix Changes:
-Adjusted health stats for the phoenix birds so they reflect the in-game numbers (health is unchanged besides a small bump to the Rage)
-2nd phase warning message lasts 3x long
-Enhanced the Rage with 2 extra attacks and a 'final stand' phase NPC spawn
-The Sorrow now triggers slow at close range during 2nd phase and chilled at long range
-The Sorrow has 1 extra attack during 1st phase and also spawns animal kin to aid herself
--
-Meteor Heads do extra damage in HM for Rage fight
-Cursed Dragon's breath triggers poison debuff instead of bleeding
-Enemy Cursed breath is way less harsh with the weak debuff
-Attempted to add hostile Hellwing projectile with homing but couldn't get the animation working
-Fixed Ancient Oolcile Demon health

---
## [shiukaheng/stagehands](https://github.com/shiukaheng/stagehands)@[05a58b022d...](https://github.com/shiukaheng/stagehands/commit/05a58b022db74c9690bb626025a31e3fc8f46d46)
#### Sunday 2023-03-26 22:30:30 by Heng

go fuck yourself, topic names

Co-Authored-By: Neel Amonkar <s2030247@ed.ac.uk>

---
## [swarm-game/swarm](https://github.com/swarm-game/swarm)@[a4c8057a28...](https://github.com/swarm-game/swarm/commit/a4c8057a28e043caed531e7d035efc2a41dc30a1)
#### Sunday 2023-03-26 22:38:51 by Brent Yorgey

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
## [kenstir/hemlock-ios](https://github.com/kenstir/hemlock-ios)@[48ef96f351...](https://github.com/kenstir/hemlock-ios/commit/48ef96f3517d4b403031e7e53801492c67367218)
#### Sunday 2023-03-26 23:11:32 by kenstir

Wire up results cell and OMG I hate IB

* Recreate Results storyboard from scratch to get hierarchy right
* OMG I HATE IB.  The cells were not auto-resizing because of an extra
  customClass="ResultsTableViewCell" on the tableViewCellContentView
  I don't know how it got there but wow what a pain.
* For now have to fetchCodedValueMaps so we have format labels.

---
## [Wallemations/heavenstation](https://github.com/Wallemations/heavenstation)@[296ca23aa1...](https://github.com/Wallemations/heavenstation/commit/296ca23aa1d8531fba291eb9b802b7282fee657b)
#### Sunday 2023-03-26 23:11:38 by Jacquerel

Most actions cannot be used while incapacitated (#73513)

## About The Pull Request

Fixes #39775
The `TRAIT_INCAPACITATED` trait is intended to block you from acting but
does not inherently block actions. Actions only check for "conscious",
"has available hands", "immobile", or "lying down".
Most actions still _can't_ be used while incapacitated. This is because
most actions are spells, most spells have invocations, and you can't
talk while you are incapacitated. This is silly.

I have resolved this by adding a new flag which blocks actions while
incapacitated. This is somewhat redundant with "conscious" because most
sources of that also make you incapacitated but not _always_, you might
want the specificity.

I have tried to be discerning about where this flag is applied, it is
not in all cases (for instance you can still swallow implanted pills
while incapacitated and such), but it's not only possible but I can't
really avoid implementing this without it being a balance change in
_some_ cases,

Actions this effects are things such as:
Xenomorph Tail Sweep, Lesser Magic Missile (cult constucts), Heretic
Shadow Cloak, the Smoke spell in general, Conjuring (but not firing)
Infinite Guns, Mime spells

Times when these actions will no longer be available but were previously
are such times as when the mob is:
Stamina Crit, Stunned, Paralysis, and Time Stopped.

## Why It's Good For The Game

The incapacitated trait is applied by effects which should block acting
but still permits several actions which logically would be prevented.
This fortunately hasn't come up too often due to the high ratio of
actions with invocations, but it feels bad to stun someone and then have
them still able to perform an action they logically wouldn't be able to
take while stunned.
This is especially egregious in the case of Time Stop (the only way to
stun a lot of the mobs effected by this) but that's a rare pick on a
rare antagonist and would also rarely be used on these mobs, so a bit of
an edge case.

## Changelog

:cl:
fix: Many spell-like abilities which could be stunned, paralysed, or
frozen in time now cannot be.
/:cl:

---
## [Evervolv/android_frameworks_base](https://github.com/Evervolv/android_frameworks_base)@[c4029aa929...](https://github.com/Evervolv/android_frameworks_base/commit/c4029aa929f5aab82c674a5d4e68ee169e7f59a7)
#### Sunday 2023-03-26 23:44:34 by Kuba Wojciechowski

AttestationHooks: Blacklist pixel system features from Google Photos

    We want to include the P21 experience flag to enable new features,
    however it seems like Google Photos uses it to decide whether to use the
    TPU tflite delegate. There doesn't seem to be any fallback so we need to
    make sure the feature is not exposed to the app so that a normal
    NNAPI/GPU delegate can be used instead.

    Test: Google Photos editor with PIXEL_2021_EXPERIENCE feature in product
    Signed-off-by: Kuba Wojciechowski <nullbytepl@gmail.com>
    Change-Id: I51a02f8347324c7a85f3136b802dce4cc4556ac5

commit 67eb31b3bb43d06fcc7f6fdb2f92eb486451cae6
Author: kondors1995 <normandija1945@gmail.com>
Date:   Thu Jun 9 17:39:25 2022 +0530

    Core: Extend Pixel experience Blacklist For Google Photos

    Turns out having these brakes Original quality backups.
    Since these indicate that the device is pixel 4 with in the turn brakes device spoofing as OG pixel

    Change-Id: I336facff7b55552f094997ade337656461a0ea1d

commit 508a99cde60b73dc3f1e843d569bca31def35988
Author: ReallySnow <reallysnow233@gmail.com>
Date:   Fri Dec 31 16:40:23 2021 +0800

    base: core: Blacklist Pixel 2017 and 2018 exclusive for Google Photos

    * In this way can use PixelPropsUtils to simulate the Pixel XL prop
      method to use the unlimited storage space of Google Photos
    * Thanks nullbytepl for the idea

    Change-Id: I92d472d319373d648365c8c63e301f1a915f8de9

commit aaf07f6ccc89c2747b97bc6dc2ee4cb7bd2c6727
Author: Akash Srivastava <akashniki@gmail.com>
Date:   Sat Aug 20 19:04:32 2022 +0700

    core: Pixel experience Blacklist For Google Photos for Android 13

    * See, in Android 13 pixel_experience_2022_midyear was added, which needs to be blacklisted aswell

    Change-Id: Id36d12afeda3cf6b39d01a0dbe7e3e9058659b8e

commit 9d6e5749a988c9051b1d47c11bb02daa7b1b36fd
Author: spezi77 <spezi7713@gmx.net>
Date:   Mon Jan 31 19:17:34 2022 +0100

    core: Rework the ph0t0s features blacklist

    * Moving the flags to an array feels more like a blacklist :P
    * Converted the flags into fully qualified package names, while at it

    Signed-off-by: spezi77 <spezi7713@gmx.net>
    Change-Id: I4b9e925fc0b8c01204564e18b9e9ee4c7d31c123

commit d7201c0cff326a6374e29aa79c6ce18828f96dc6
Author: Joey Huab <joey@evolution-x.org>
Date:   Tue Feb 15 17:32:11 2022 +0900

    core: Refactor Pixel features

    * Magic Eraser is wonky and hard to
      enable and all this mess isn't really worth
      the trouble so just stick to the older setup.

    * Default Pixel 5 spoof for Photos and only switch
      to Pixel XL when spoof is toggled.

    * We will try to bypass 2021 features and Raven
      props for non-Pixel 2021 devices as apps usage
      requires TPU.

    * Remove P21 experience system feature check

Change-Id: Iffae2ac87ce5428daaf6711414b86212814db7f2

---

