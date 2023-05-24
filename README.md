## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-05-23](docs/good-messages/2023/2023-05-23.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,046,129 were push events containing 3,414,066 commit messages that amount to 262,165,665 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 70 messages:


## [Latentish/Shiptest](https://github.com/Latentish/Shiptest)@[d4b5a598e2...](https://github.com/Latentish/Shiptest/commit/d4b5a598e2346bb3f69d533ed05a94d539e8b830)
#### Tuesday 2023-05-23 00:00:34 by Bjarl

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
## [LynxSolstice/cmss13](https://github.com/LynxSolstice/cmss13)@[2baaba2746...](https://github.com/LynxSolstice/cmss13/commit/2baaba27468b20016d2095edfbdba26658935ddc)
#### Tuesday 2023-05-23 00:21:06 by Hopekz

Adds medic clothing racks to WO (#3313)

God damn this is so frustrating every time I play WO as a medic


![dreamseeker_ZXt55sth9R](https://github.com/cmss13-devs/cmss13/assets/24533979/252773e1-fec0-4bec-a1a5-0ccb63547781)


![dreamseeker_UiolotzaIV](https://github.com/cmss13-devs/cmss13/assets/24533979/a241ee86-f2ea-490f-91c7-7b1a90e9734f)


:cl: Hopek
add: Medics finally get medic clothing racks on WO
/:cl:

---
## [gitstart/sourcegraph](https://github.com/gitstart/sourcegraph)@[753ef33f15...](https://github.com/gitstart/sourcegraph/commit/753ef33f151752ca94942ba890277587a828bf9a)
#### Tuesday 2023-05-23 00:24:25 by Valery Bugakov

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
## [llegomark/evals](https://github.com/llegomark/evals)@[3a585acbcd...](https://github.com/llegomark/evals/commit/3a585acbcd80a1af48bb54d8a72c20542f736e43)
#### Tuesday 2023-05-23 00:24:51 by Achin Parashar

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
## [llegomark/evals](https://github.com/llegomark/evals)@[4e59e8903b...](https://github.com/llegomark/evals/commit/4e59e8903b4cb06204bd4c9646eacf345643eb74)
#### Tuesday 2023-05-23 00:24:51 by neolizhe

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
## [llegomark/evals](https://github.com/llegomark/evals)@[80edb30f3c...](https://github.com/llegomark/evals/commit/80edb30f3c7e922e7c7542bf4017c1ce62a2f1c4)
#### Tuesday 2023-05-23 00:24:51 by Chris Sypherd

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
## [llegomark/evals](https://github.com/llegomark/evals)@[06802cc61d...](https://github.com/llegomark/evals/commit/06802cc61da1395e492ecc8b1ed7153c42b5e2df)
#### Tuesday 2023-05-23 00:24:51 by Alexander Rössler

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
## [llegomark/evals](https://github.com/llegomark/evals)@[5fdb015ff7...](https://github.com/llegomark/evals/commit/5fdb015ff7b0c09836c614ced07c1c1f20c07c3a)
#### Tuesday 2023-05-23 00:24:51 by AlexanderMeloysund

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
## [llegomark/evals](https://github.com/llegomark/evals)@[7b4bd9439f...](https://github.com/llegomark/evals/commit/7b4bd9439fce855cf52c93357fe3fe239d96abaf)
#### Tuesday 2023-05-23 00:24:51 by AlexBuz

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
## [pearuhdox/Cartographer](https://github.com/pearuhdox/Cartographer)@[60be47b68b...](https://github.com/pearuhdox/Cartographer/commit/60be47b68bf3f4f530158088450f01d5ef64eadb)
#### Tuesday 2023-05-23 00:48:09 by pearuhdox

A large number of new enchants

Curses:
- Curse of Clumsiness: When you fall, you receive an additional +1 unblockable damage per level.
- Curse of Flammability: When you take fire damage, you take an additional +1 unblockable damage per level.
- Curse of Jinxing: When you take magic (Poison or Wither) damage, you take an additional +1 unblockbale damage per level.

- Curse of Drowning: When you are in water, you take drowning damage over time (even if you are not out of breath or in air).

- Curse of Rusting: Durability is slowly depleted on an item while it is on your hotbar or armor slots, to a specified cap.
(Level will increase the rate of draining by draining more durability every trigger. Unbreaking has a chance to prevent it from draining in that proc.)

Melee:
- Hex Eater: Melee attacks consume all debuffs and do +1 damage per debuff per level. Does not count effects that were applied in the same hit.

Ranged:
- Repulsion: When reloading the crossbow, emit a blast of wind that knocks enemies away when the reload starts. (Applies effects)

Passive:
- Reconstruction: The item will slowly regain durability over time.
(Level will increase the rate of recovery by adding more durability back every trigger.)

- Resourceful: Gain a 10% chance per level of not consuming an arrow when firing the weapon (aka receiving an arrow back when fired.)
	(You will always receive a normal arrow, even if you fired a spectral or tipped arrow.)

- Sprint Dash: Sprint jumps have extra forward momentum per level.
- Disengage: Taking damage preps a buffed backwards jump that moves you further and higher.

- Gravity: (Already done)
- Quake: Killing a mob creates a shockwave around you that inflicts damage and applies on hits.
- Momentum: Sprinting builds charge, which can be expended for more powerful melee attacks. (+25% damage per level on a group)
- Smite: Periodically a mob near you is struck for damage and effects. (Range is 15 blocks, every 5 seconds, and it cannot strike the same mob twice in a row.)

- Shielding: When you have no Absorption health, you gain Absorption I. This effect has a cooldown dependent on the level of enchant.
(90 Second Start, -15 Seconds per additional level, 90/75/60/45/30/15)

- Confidence: Deal additional damage while above 75% max health. (10% per level)
- Desperation: Deal additional dmage while below 50% max health. (10% per level)
- Stalwart: Gain +1 Armor per level when under 50% max health. (+1 per level)

- Second Wind Refresh:

While worn/held, you will be protected from a lethal hit. When you are hit for lethal damage, you gain 10 seconds of brief invulnerability. During this time, every mob that is targeting you within 16 blocks will be marked. If every marked mob dies before your invulnerability runs out, you are healed and saved from death. If not every marked mob dies, you die at the end of your invulnerability. If you die and there are no nearby hostile mobs, Second Wind will not activate.

---
## [Higgin/Skyrat-tg](https://github.com/Higgin/Skyrat-tg)@[410979bb6a...](https://github.com/Higgin/Skyrat-tg/commit/410979bb6af8b1ccfb840dee0461867724714912)
#### Tuesday 2023-05-23 01:10:52 by SkyratBot

[MIRROR] Microing var/static times (~0.015 seconds of init) [MDB IGNORE] (#20688)

* Microing var/static times (~0.015 seconds of init) (#74769)

## About The Pull Request

Moth and I came up with an affront to god and man, and used it to track
the time spent creating /static (and in theory /global) variables (this
happens right at the start of init)
They cost as a sum about 0.05 seconds btw, at least currently.

```
/datum/timer
    var/key

/datum/timer/New(file, line)
    src.key = "[file]:[line]"

/datum/timer/proc/operator*(x)
    rustg_time_reset(key)
    return x

/datum/timer/proc/operator+(x)
    var/time = rustg_time_microseconds(key)
    world.log << "TIMER: [key]: [time]"
    return x

Regex:
var/static/([\w/]+) =
-> var/static/$1 = (new /datum/timer(__FILE__, __LINE__)) * (new /datum/timer(__FILE__, __LINE__)) +
```

Output on moth's pc looks like this, time in microseconds

[output_sorted.csv](https://github.com/tgstation/tgstation/files/11241900/output_sorted.csv)

Most of this is either icon_states() memes (which appears to be cached
btw, that's interesting), or a variation on typecacheof()
There is one get_asset_datum call, but that is ALREADY cached and so is
just redundant. That's a good 0.01 seconds saved.

The rest of the time here is slightly more interesting.

The majority of typecacheof() is iterating the output of typesof(), a
byond internal proc that returns a list of types that either are or are
the child of the passed in type.
A decent chunk of time here (0.005 seconds, or 10% of the proc) can be
saved by unrolling the arguments to the proc.
It takes an arbitrary amount of typepaths as input, but we can't like
use arglist() here (cause this is an internal "proc"), so instead we try
a window of args, passing in null if we start to try and take in too
much.
Window size matters, zebra fits better into 4 then 5, especially because
of how grouping needs to work to make this effect happen.
We save about 0.001 for zebra btw, which is around about 7%. It's lower
cause we need to group the paths beforehand I think.

The speedup is minor, but it DOES exist. Plus it's fun.

## Why It's Good For The Game

Microing is a hell of a drug

* Microing var/static times (~0.015 seconds of init)

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [rslinford/openai_evals](https://github.com/rslinford/openai_evals)@[b93700ab49...](https://github.com/rslinford/openai_evals/commit/b93700ab496bd112f89821777edc6a22d5972fb2)
#### Tuesday 2023-05-23 03:01:36 by DunedainStrider

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
## [rslinford/openai_evals](https://github.com/rslinford/openai_evals)@[8e276ea460...](https://github.com/rslinford/openai_evals/commit/8e276ea4603155ee616d5cd66aadfddcfbcae0cc)
#### Tuesday 2023-05-23 03:01:36 by steven-luabase

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
## [rslinford/openai_evals](https://github.com/rslinford/openai_evals)@[33484c8341...](https://github.com/rslinford/openai_evals/commit/33484c83416c30733359d5c4dcb9a61f91cab8a6)
#### Tuesday 2023-05-23 03:01:36 by emu1729

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
## [rslinford/openai_evals](https://github.com/rslinford/openai_evals)@[aa71d43273...](https://github.com/rslinford/openai_evals/commit/aa71d4327328933a463e972d662e6988234d0ef7)
#### Tuesday 2023-05-23 03:01:36 by Andrew Kondrich

Fix get_answer (#972)

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
## [rslinford/openai_evals](https://github.com/rslinford/openai_evals)@[8f8632ec55...](https://github.com/rslinford/openai_evals/commit/8f8632ec55ee1f9704fe34225e1bce0cd999a8b1)
#### Tuesday 2023-05-23 03:01:36 by Oshan Upreti

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
## [panzerr1944/coyote-bayou](https://github.com/panzerr1944/coyote-bayou)@[6fd64b92ca...](https://github.com/panzerr1944/coyote-bayou/commit/6fd64b92ca4cc80357d8d78c8efc1c6d8196204f)
#### Tuesday 2023-05-23 03:31:36 by Tk420634

Updating the Mansion a bit

Preparing my brain for making a non euclidian dungeon, because I fucking hate everything.

---
## [strikersix23/git](https://github.com/strikersix23/git)@[eb1c42da8e...](https://github.com/strikersix23/git/commit/eb1c42da8e21cc2a8dacd21023a179b788858887)
#### Tuesday 2023-05-23 04:08:08 by Jeff King

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
## [shifucun/website](https://github.com/shifucun/website)@[60d93d54cc...](https://github.com/shifucun/website/commit/60d93d54cc21bc04c0f3e1c3435a76e3e74fe808)
#### Tuesday 2023-05-23 04:25:09 by Jehangir Amjad

[NL Interface] Embeddings update (#2642)

In this PR, we do the following:

1. Make the build_embeddings_v2.py be the default way to generate
embeddings.
2. Updates the latest embeddings (after running the process in (1)).
3. Due to (1) and (2), increased the number of query -> sentences
matched number (from 20 to 40).
4. Updates the nl server tests (need reviewers to check carefully)
5. Update the integration tests (will need a careful look)
6. Linked is the embeddings index differ script output (using top 3
only):

https://drive.google.com/file/d/1-6A-xXcRYj50poglis_7rc1P3aqxYf3R/view?usp=sharing


Based on (6), most of the changes look Ok. We looked at some individual
cases to figure out if the differences are actually impacting. Only one
case below (in bold) was found to actually be different than what's on
autopush right now.

24: How many male civilians are there in Queens? => this is the same on
autopush and after the changes in this PR (ignoring "Queens" and the
stop words makes the results the same.)

38: What is the median age of American Indian or Alaska Native females
in the United States? => same as above (no impact).

43: age in california => this is different but since we'll soon be
removing some of the age SVs by breakdowns, it should be Ok.

44: agricultural output across california => same as above (no impact
due to place and stop word removal)

63: count of earthquakes per year => same on autopush so no impact. This
is because earthquake events are handled separately.

100: housing price trend comparison across US states => same as above
(no impact) after place and stop word removal.

**101: housing trend comparison across US states** => this is different
(autopush uses housing units but new embeddings lead to number of
households but that seems Ok but arguably autopush is also bad because
it goes to a correlation plot which is not the right thing to do here
anyway)

---
## [mamedev/mame](https://github.com/mamedev/mame)@[2222a0f098...](https://github.com/mamedev/mame/commit/2222a0f098c2f32ec6090627598a90e596006596)
#### Tuesday 2023-05-23 04:42:23 by David 'Foxhack' Silva

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
## [newstools/2023-daily-nation](https://github.com/newstools/2023-daily-nation)@[adfcd73327...](https://github.com/newstools/2023-daily-nation/commit/adfcd73327d03c84a1d4ef7f97d0c78971e98a7a)
#### Tuesday 2023-05-23 05:07:06 by Billy Einkamerer

Created Text For URL [nation.africa/kenya/news/-my-brother-lost-his-life-to-thugs-while-defending-his-friend--4243328]

---
## [shonker/AmalgamEngine](https://github.com/shonker/AmalgamEngine)@[920f2c4d79...](https://github.com/shonker/AmalgamEngine/commit/920f2c4d79fc71415af6f9bc6cf57b46cd6a73de)
#### Tuesday 2023-05-23 05:10:43 by Net_

Massive tile map/sprite data improvement.

Motivation:
Previously, each tile in the tile map just held layers of sprites.
This was fine for a while, but it was recognized that, by bringing
the tile map to a higher level of abstraction, we could make the
experience of working with it a lot more friendly.
This "higher level of abstraction" is that of floors, walls, etc.
Actual concepts of what goes on a tile map, instead of generic
sprites. The goal with this change is to let developers think at
the level of "I want to add a wall to this tile", instead of "I
need to add a wall sprite to layer 3 and update any surrounding
sprites".

TODO:
Rendering is still partially commented out.

Changes:
Refactored SpriteDataBase/SpriteData classes to use the new
higher-level sprite concepts.

Replaced TileUpdate/TileUpdateRequest messages with more specific
messages: TileAddLayer, TileRemoveLayer, TileClearLayers,
TileExtentClearLayers. These were necessary because we no longer
are working with a homogenous array of sprites, but they provide
the added benefit of opening a path for us to send large operations
as a single message. TileExtentClearLayers is the current example
of that, and we can add more in the future.

Refactored the TileUpdateSystems, ChunkUpdateSystem, and
ChunkStreamingSystem to match the new tile map and use the new
messages.

Made some enum changes for consistency. When relevant, each enum
should follow the patterns: Be a Uint8 (for in-memory size in
the tile map), be a struct-wrapped normal enum (to avoid constantly
casting an enum class. not necessary if never used as index or size),
have a Count value (instead of e.g. NumTypes), don't specify numbers
unless necessary (so Count stays correct if values are added).

Gave SpriteData a dedicated directory.

SpriteDataBase::get() -> getSprite().

Big TileMapBase/TileMap refactors.

Changed ISimulationExtension:isTileUpdateValid() to isExtentEditable().
It's more restricted so we may need to change it in the future, but
we have multiple types of update messages now so the old one wasn't
workable. Maybe in the future change we'll pass the updates as a
variant?

Updated ChunkSnapshot/ChunkWireSnapshot/TileSnapshot to work with the
tile map changes.

Changed Rotation::Direction to be an unsigned enum so it fit with
Wall::Type in our generic message. MovementHelpers is the only place
that needed the special values for the input math, so it now has
a translation function.

Refactored SpriteData, updated parsing logic.

Big Tile refactor to handle the new concepts.

Fixed some things like ChunkExtent that were a class when they should
have been a struct.

---
## [Ebin-Halcyon/Skyrat-tg](https://github.com/Ebin-Halcyon/Skyrat-tg)@[fc1471c818...](https://github.com/Ebin-Halcyon/Skyrat-tg/commit/fc1471c8187d3f2a49d75a8a5c3e1b610fec45d3)
#### Tuesday 2023-05-23 05:12:14 by SkyratBot

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
## [Aliya-Daire/C-Projects](https://github.com/Aliya-Daire/C-Projects)@[8ff2831c0e...](https://github.com/Aliya-Daire/C-Projects/commit/8ff2831c0e1174df9969c4f0280024075636fdca)
#### Tuesday 2023-05-23 05:51:32 by Aliya Daire

PR3 Maze Solver

2. Introduction and Background
Introduction

Solving a Maze
In this programming assignment you will write a program to read a given maze (provided as text “art”) and find the shortest path from start to finish. Mazes go back to antiquity and the story of the minotaur. However, Theseus didn’t have Google Maps.

You will implement breadth-first search, a simple algorithm that finds not just any path to the exit in a maze, but actually finds a shortest path from the start to the finish. This algorithm was described in the late 1950s, making it one of the earliest nontrivial algorithms to follow the creation of the electronic computer.

Maze Input Format
Your program will receive the input file from a command line argument.
Below shows an example of passing in a maze input file called “maze1.in” to our maze program using a command line argument.
./maze maze1.in
The input file is structured as follows:

The first line of the file should contain two integer numbers indicating the row and column size of the maze. The number of rows indicated will determine how many lines of text follow (1 row per line).

On each line will be one character for each of the indicated number of columns followed by a newline character. The characters can be a period . indicating a space in the maze, a # sign indicating a wall in the maze, a capital S indicating the start location for your search, or a capital F for the desired finish location. You can’t go outside the grid. (i.e., you may imagine that lava surrounds the maze perimeter.)

In general the format of the maze is:
rows cols
[row 1: cols many characters]
[row 2: cols many characters]
...
[row rows: cols many characters]
and the possible characters are:
Character	Meaning
.	Empty space
#	Wall
S	Start location
F	Finish location

We provide you with 4 mazes: maze[1-4].in and maze1.in is shown as an example on the left. You can also find some interesting mazes in a directory called test cases.

Maze Output Format
Your search algorithm will find a shortest path from the start cell to the finish. It will indicate this path by filling in the character locations on the path with asterisks *; then, it will write the resulting character maze to cout (standard output).

Note: We could have chosen to output the results to a file to practice with ofstream objects, but because they behave nearly the same as cout, we chose the simpler cout approach so you can focus on the really learning tasks of allocating the 2D array(s) and implementing the BFS algorithm.

The correct output for maze1.in (below) is shown on the left (maze1.sol).
maze1.in
5 5
.S.#. 
##.#.
.....
.####
....F
maze1.sol (this is the content that cout should produce)
5 5
.S*#. 
##*#.
***..
*####
****F

However,
If no path exists, your program should output
No path could be found!
If the user gives an invalid maze (more than one start or finish point), your program should output
Invalid maze.
If the input maze contains characters other than those shown above, then your program should output
Error, input format incorrect.

BFS
Breadth First Search is a general technique with many uses including flood fill, shortest paths, and meet-in-the-middle search. The idea is to explore every possible valid location, beginning at the start location, using an ordering so that we always explore ALL close locations (i.e. those at a shorter distance from the start) before exploring any location at a further (longer) distance from the start.

In other words, first we “explore” the start, then all locations at distance 1 from the start (one at a time), then all locations at distance 2 from the start (one at a time), etc, in that order.

This property ensures that when we do find the finish cell (if one exists), we will arrive there via a shortest-length path. Of course, as we search we mark cells (as explored) that we’ve visited so that we don’t visit them again and cause an infinite cycle of exploration!

Ensuring the BFS property
To ensure we explore all closer locations before further locations, we keep a queue of locations in the maze. A queue has the property that the first item added is the first to be removed (first-in, first-out, a.k.a. FIFO). We can easily implement this by always adding new values to the back of a list (i.e. tail of the queue) but remove from the front (i.e. head of the queue).

Put simply, a queue mimics a line of people waiting. New arrivals enter at the back and leave from the front when they are served. The longest/oldest item will be at the front of the queue and the newest at the back.

In our maze search the queue is initially empty and we begin by putting the start location into it. In each iteration, we remove the oldest remaining location from the queue, and we add all of its new neighbors to the end of the list. This simple algorithm successfully implements the BFS.
We keep the BFS going until the queue is exhausted because all reachable locations were explored or we find our goal location.
What is left is to actually mark out the shortest path in * characters (i.e., trace your path back from the finish point to start point). But this requires that we record which location found each subsequent location during the outward (BFS) exploration. We will track a predecessor for each location (which is simply the coordinates of the location that found this one). Think of a predecessor as a pointer to take one step backward. Once we find the Finish location, we can just walk from the predecessor of the Finish to that location’s predecessor, and then to that location’s predecessor, and so on until we reach the start, marking each of those locations with *.

Coding Considerations
Location Struct
The maze in this assignment is a 2D grid. Therefore, each location in the maze is identified by two index values: a row index and a column index. The approach that we will use for solving the maze will involve keeping track of a list of these locations. It will be extremely convenient if we are able to create a structure that contains both a number for the row and a number for the column.
We can accomplish this by creating a simple new data type.
We will call it Location.
struct Location { // define a new data type
  int row;
  int col;
};

Put Simply
A Location object is simply a package with two numbers that can be manipulated using the dot (membership) operator.
Here is an artificial example.

Location start;//create a location called 'start'
start.row = 3 ;//set the row of `start` to be 3
start.col = 5 ;//set the column of `start` to be 5

Location one_below = start; // make a copy of the start location called `one_below`
one_below.row += 1 ;//add one to the row of `one_below`

cout<<"Start:"<< start.row <<","<< start.col <<endl; // Start: 3,5
cout<<"One Below:"<< one_below.row <<","<< one_below.col <<endl; // One Below: 4,5

This will be convenient because we can have an array (or queue) of Locations, have functions that take a Location as input or output, etc.

In the next page, we will talk about another data type that you will have to complete, the Queue class.

Questions that you should be asking yourself:
What are the differences between a struct and a class? When should I use a class vs a struct?

The Queue class
You will be required to complete the definition of another new data type, the Queue class, that will be useful in implementing the search. The Queue class will store the list of Locations waiting to be searched. The Queue class should support the following operations:
- create an empty queue (but with a given maximum capacity of how many Locations it can store)
- add a new Location to the back of the queue
- Remove the oldest Location from the front of the queue 
- check if the queue is empty

We use objects (classes and structs) to abstract our software design and implementation. By first writing the Queue class, you do not have to worry about those implementation details when you write your higher level BFS algorithm. This allows you to focus on the larger BFS algorithm and not the data management aspects.

Every time you find a new, unexplored Location you will call the Queue's add_to_back(Location) function. Every time you want to get the next location to explore from, you will call the Queue's remove_from_front() function.
Internally, the Queue class should just create an array to hold the maximum number of Locations that could ever be entered into the queue and use integer index variables to remember where it should place new values (i.e. where the back is located) and where it should remove old values (i.e. where the front is located).

Remember that our Queue class needs to support the following operations:
// returns true if the queue is empty.
bool is_empty();

// insert a new Location at the end of our queue  
void add_to_back(Location loc);

// returns the oldest Location in the queue and "removes" it.
Location remove_from_front();
Here is an example of how it should behave:
// create some locations;
Location three_one;
three_one.row = 3; three_one.col = 1;
Location two_two;
two_two.row = 2; two_two.col = 2;

// create a queue with max capacity 5
Queue q(5);

cout << boolalpha;
cout << q.is_empty() << endl; // true
q.add_to_back(three_one);

cout << q.is_empty() << endl; // false
q.add_to_back(two_two);

Location loc = q.remove_from_front();
cout << loc.row << "," << loc.col << endl; // 3,1

loc = q.remove_from_front();
cout << loc.row << "," << loc.col << endl; // 2,2

cout << q.is_empty() << endl; // true
As you can see, the queue gave us back the oldest location (the one add_to_back added earliest) first.
The Queue class under the hood

The Queue implementation we provide you is almost complete. It is based on the idea of using a long array/pointer called contents that holds Locations, as well as two counters:
tail counts the number of add_to_back calls so far. Equivalently, its value is the next unused index in the contents array.
head counts the number of remove_from_front calls so far. Equivalently, its value is the oldest index that has not yet been extracted.
For instance, this is what the internal variables of the Queue should look like for the example above before the two locations are added:
tail: 0
head: 0
contents[0..4]: garbage
Here is what it looks like after both locations are added:
tail: 2
head: 0
contents[0]: Location(row 3, col 1)
contents[1]: Location(row 2, col 2)
contents[2..4]: garbage
Currently, head is 0.

When we make the first call to remove_from_front, it should both return the Location at contents[head] which is Location(row 3 , col 1) and increment the head counter by one.
head is now 1.

After that, when we make the second call to remove_from_front, it again should return the Location at contents[head] which is Location(row 2, col 2) and increment head counter by one.

After that, because head and tail are now equal, the Queue knows it is empty.

You may have to create a temporary variable to hold the Location at contents[head] so that you can increment the head counter before returning that Location. This is because any statement that comes after a return statement will not be executed.

Note: when you delete a Location from the queue (remove_from_front), you do not technically remove the Location. You simply move the head counter forwards (i.e., incrementing the head counter and leaving the old Locations sitting in their original Locations). Actually, the expense of removing a Location and shifting other Locations forward would make your program much slower.

The Queue constructor takes an integer max_size. For our BFS application, you should pass rows*cols as this maximum size, since that it the maximum number of locations that our queue could be used to explore. 

2D Array Allocation
You will not know the size of the maze until runtime, when you read the maze data. Thus we will need to dynamically allocate an array to hold the maze data. 

Remember that a single call to new can only allocate a 1D array. Thus you will need to allocate each row of the 2D array as a separate 1D array. And, beyond that, we need not just one 2D array but several: 
one for the maze data, one for the predecessors, and one to remember which cells have been visited.

The way to allocate a 2D array in C++ is: use new[] once to allocate a 1D array of pointers, then using a loop containing new[] to allocate many 1D arrays whose starting addresses are stored in the pointer array elements. See the dynamic memory exercise nxmboard and deepnames on the website (in class exercises).

Memory leaks
Remember that you need to deallocate everything that you allocate. This means that every call to new[] needs a matching call to delete[]. Otherwise, your program will have a memory leak!

Typically, the pattern you use to allocate is the same pattern you will use to deallocate, but just in reverse order.

---
## [overhangio/tutor](https://github.com/overhangio/tutor)@[92891ef9ef...](https://github.com/overhangio/tutor/commit/92891ef9ef8fd8835844192043b359324743f97b)
#### Tuesday 2023-05-23 07:24:57 by Régis Behmo

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
## [ProditorMagnus/Ageless-for-1-14](https://github.com/ProditorMagnus/Ageless-for-1-14)@[9239fe3fc3...](https://github.com/ProditorMagnus/Ageless-for-1-14/commit/9239fe3fc3808b76803a4ff24963a6c4c382568a)
#### Tuesday 2023-05-23 09:07:17 by ReynBolt

changelog , ME - Update

ME - AVIANS

- Largewing cave defense to 20% (+10%) , movement cost to 3 (-1)
- Largewing hills defense to 50% (+10%)
- Largewing arcane ressistance to 20% (+20%)
- Medwing hills defense to 50% (+10%) 
- Medwing village defense to 60% (+10%)
- Medging arcane ressistance to 10% (+10%)
- Floatwing deep-water/reef movement cost to 2 (+1) 
- Smallwing now has 10% (+10% arcane res

These units are medwing.
- Archer XP from 44 to 38
- Bombardier XP from 75 to 70 , price to 26g (-3g)
- Bowflurry cold ressistance to 10% (+10%) , price to 52g (+6g)
- Hawkeye XP from 75 to 72 , price to 28g (-2g)
- Eagle Eye cold ressistance to 10% (+10%) , price to 54g (+7g)

- Watchman XP from 42 to 39 
- Bladewing cold ressistance to 10% (+10%) 
- Razorwing cold ressistance to 10% (+10%) , price to 55g (+3g)
- Shell price to 53g (+6g)
- Savior HP to 46 (+2) , price to 31g (-1g)

- Armorpiercer now has parry(+5%) in melee
- Daredevil cold ressist to 10% (+10%) , ranged damage decrease from 4-5 to 3-4 but parry(+5%)
- Rocket cold ressistance to 10% (+10%) 


These units are largewing.
- Broadwing XP from 54 to 49
- Skylord HP to 46 (+2) , cold ranged damage increase to 8-3
- Winged Baron price to 60g (+6g)
- Sky Terror HP to 56 (+4)
- Dreadnought HP to 74 (+4) , cold ranged damage increase to 17-2

- Egglayer now has parry(+5%) in melee , movement to 6 (+1)
- Sitter price to 32g (-4g)

These units are smallwing
- Jackdaw XP from 46 to 42
- Crow HP to 42 (+2)
- Raven HP to 55 (+3) , cold res to 10% (+10%) , price to 57g (+3g)
- Owl HP to 38 (+3) 
- Nightwing HP to 53 (+6) , price to 58g (+1g)

- Dove price to 34g (+2g)
- Humming Bird melee damage adjusted from 4-4 to 8-2
- Sparrow cold res to 10% (+10%) price to 32g (-2g)
- Falcon cold res to 15% (+15%) , price to 56g (+3g)
- Passer HP to 51 (+3) , cold res to 10% (+10%) 


And groundeds...
- Grounded XP from 44 to 42 , swamp defense to 30% (+10%)
- Ironbeak impact melee damage decrease by -1 , swamp defense to 30% (-10%) , price to 28g (-2g)
- Steelbeak swamp defense to 30% (-10%) 
- Diamondbeak swamp defense to 30% (+10%) , price to 82g (+7g)



ME - BLIGHT

- Acid
a) HP to 24 (-2) , ranged has now +drains +absorb , blade/impact lowered by 10% , cold res lowered to -50% (-10%)
b) melee attack now has UN UPGRADABLE STRIKE 1
c) NEW ATTACK: 12-1 fire melee +drains +absorb & accuracy/parry -5% 
d) ranged has now UN UPGRADABLE STRIKE 4 , but gains an extra attack that can gain more strikes but -5% accuracy/parry
Out of Orocia it's impossible this unit gain extra strikes, but if it did happen it was more melee than ranged unit.
Now its focus is about being ranged unit. Balance tests need to be tried as unit max level is 1 and they need fire ranged specialist.

- Ooze absorb now gains UN UPGRADABLE STRIKE 2, NEW ATTACK: Absorb 12-2 fire melee +drains +absorb and parry(-5%) , price to 31g (-4g)
Problem is not about unit being at max HP, problem is also of unit getting higher than max HP with strong attacks.

- Amoeba absorb now gains UN UPGRADABLE STRIKE 1, NEW ATTACK: Absorb 12-1 fire melee +drains +absorb and accuracy(-5%)

- Plagued damage decrease to 9-3 , price to 30g (-2g)
- Blighted damage decrease to 13-3
- Zombie price to 26g (-2g)
- Flesh Eater fire res to -10% (+10%) , price to 52g (+4g)

- Undead hound price to 38g (-2g)

- Dismembered pierce res to 45% (-5%) , price to 32g (+2g)
- Rancid XP from 68 to 80 , price to 32g (+2g)
- Putrid pierce res to 45% (-5%) , claws damage decrease to 24-2 , price to 54g (+13g)

- Blacktide XP from 100 to 88
- Undertow HP to 49 (+3) , damage increase to 8-6 , cold res to 35% (+5%) , price to 55g (+9g)
Now it's worth getting this unit to lv3, more benefit than XP mod upgrades, specially for 5% more cold ressist.

- Seeded aligment change to NEUTRAL, added +ME-Triple-strike , price to 9g (-1g)
This is actually a nerf, unit can block tiles in day but could deal +25% damage on night. Some very small AoD in compensation.

- Host HP to 35 (+1)
- Spore Hive HP to 52 (+2)

- Charred Zombie XP from 40 to 38
- Mutilated corpse pierce ressistance to 35% (+5%)
- Dreadbones price to 54g (+8g)


ME - ENCHANTERS

- Stockpiler pierce and blade damages decreased by 1, price to 54g (+1g)

- Sacrificer price to 33g (+2g)
- Powermad price to 57g (+8g)
- Apocalyptic price to 83g (+11g)
- Sellsoul price to 60g (+10g)
- Cursed hand price to 34g (+1g)
- Devilhand price to 57g (+7g)

- Forge price to 32g (-4g)
- Fabricator price to 60g (+6g)

- Magic Sword HP to 29 (+1) , price to 27g (-5g)
- Enchanted Sword HP to 36 (+2)
- Shadow Sword price to 52g (+2g)
- Possesed Sword HP to 28 (+2) , price to 31g (-1g)
- Shifting HP to 29 (+1) , Sword price to 32g (-2g)

- Blazier XP from 77 to 75 , price to 27g (-3g)
- Incinerator price to 54g (+2g)
- Clearbow arcane ranged damage increase to 8-4 , price to 31g (-1g)
- Crystal Bow pierce ranged increase to 14-3 , arcane ranged damage increase to 9-5 , price to 56g (+6g)

- Reductor XP from 50 to 46
- Titan price to 34g (-2g)

- Rune apprentice XP from 60 to 52
- Arcane transcriber XP from 105 to 92 , price to 35g (-9g)
- Arcane Rune Splicer price to 54g (-3g)
- Rune Purist HP to 48 (-2)
irrelevant nerf for a mage.
- Rune Master price to 80g (+3g)
- Rune Splicer price to 58g (+3g)
- Ice Runer Improver secondary cold attack damage adjusted from 5-7 magical to 6-7 enchanted and parry(+5%)
- Fire Rune specialist price to 38g (-5g)


ME - EQUESTRIANS

- Bull all damages decreased by 1 , price to 32g (-1g)

- Charger XP from 45 to 52
- Crasher XP from 86 to 92 , price to 43g (+4g)
- Breaker HP to 75 (+3) , price to 67g (+9g)

- Knight XP from 44 to 41
- Paladin price to 36g (+1g)

- Mage Rider HP to 31 (+1) , XP from 50 to 47
- Mage Knight HP to 45 (+1), XP from 110 to 90 , fire res to 10% (+5%)
- Templar HP to 57 (+1) , fire res to 15% (+15%) , price to 65g (+12g)
- Troubadour pierce ressistance to 10% (-10%) , price to 37g (-8g)

- Pegasus rider cold res to 10% (+10%)
- Pegasus Knight price to 32g (-4g) , cold res to 10% (+10%)
- Silver Pegasus HP to 60 (+4) , cold res to 20% (+20%) , price to 62g (+7g)

- Jockey price to 59g (+8g)

- Searay cold res to 15% (+15%)
- Manta cold res to 20% (+20%) , price to 31g (-5g)

- Vagabound XP from 42 to 39 , cold res to 10% (+10%)
- Nomad melee damage increase to 6-3 , XP from 77 to 75 , cold res to 10% (+10%) , price to 32g (-2g)
- Roamer cold res to 15% (+15%)


ME - FANATICS

- Bladesman XP from 46 to 41
- Zealblade price to 54g (+6g)
- Terrorist movement to 6 (+1) , price to 32g (+2g)
- Fearmonger movement to 6 (+1) , price to 56g (+2g)

- Sandbow XP from 44 to 39
- Ambusher blade damage increase to to 12-1  XP from 70 to 63 , price to 24g (-1g)
- Sandskulker price to 50g (+3g)

- Streetrat XP from 36 to 31
- Prowler HP to 44 (+2) , ranged has accuracy(+5%) , fire ressist to 30% (+20%) , price to 30g (-5g)
- Sandthief HP to 41 (+2) , fire res to 20% (+10%)
- Sand Bandit HP to 52 (+2) , fire res to 20% (+10%) , price to 48g (+5g)

- Caravan XP from 41 to 39
- Camel Rider price to 31g (-3g)
- Camel Knight price to 55g (+9g)

- Follower XP from 40 to 38
- Fanatic price to 54g (+8g)

- Misinformant price to 32g (-4g)
- Propagand price to 57g (+3g)

- Genie XP from 50 to 48
- Master Genie price 36g (-6g)


ME - HIGHLANDERS

- Contestant HP to 35 (+2)
- Stonethrower HP to 47 (+3) , XP from 72 to 67 , price to 28g (-4g)
- Rocklauncher HP to 58 (+2) price to 52g (+6g)

- Sober HP to 55 (+2) , XP from 62 to 80 , cold res to 30% (+10%) , price to 29g (-1g)
Sober XP had to be nerfed because of Coldturkey option, STRONG leadership unit.
- Bartab NEW ATTAC: Mug of Mead 9-1 pierce ranged , cold res to 30% (+10%) , price to 48g (+2g)
Had to get bonus range attack because it was not the nerfing target.
- Coldturkey HP to 72 (+2) , cold res to 30% (+10%) , price to 62g (+10g)
- Barfighter XP from 65 to 72 
- Wildman price to 58g (+4g)

- Amputator HP to 50 (+2) , removed bleeding.
- Combatmedic price to 36g (-4g)

- Hulk HP to 60 (+2)
- Thor HP to 72 (+2) , melee damage increase to 19-2 , XP from 114 to 135 , price to 57g (+5g)
- Odin price to 90g (+40g)
- Behemoth price to 57g (+5g)

- Pipeman now has +leadership and can boost lv0 damage.
- Bagplayer XP from 70 to 75 , price to 33g (-2g)
- Warpipe price to 60g (+9g)

- Pilferer XP from 72 to 80 , price to 30g (-2g)
- Plunderer HP to 70 (+3) , price to 55g (+9g)
- Barbarian XP from 72 to 80

- Valkyrie Warrior price to 32g (-2g) 
Lots of 40% defenses...
- Valkyrie Princess HP to 71 (+2) , price to 56g (+4g)

- Woodsman price to 28g (-2g)
- Gamekeeper HP to 66 (+1) , price to 52g (+5g)
- Hatchet thrower blade ressist to 20% (+5%)
Too many nerfs in highlanders, need a buff even in something strong.
- Axethorower price to 54g (+5g)


ME - HIVE  
- Hivefoot now has 10% arcane res
- ALL flies

Hivefoot units
- Fire Ant movement to 6 (+1) , fire ranged damage decrease to 3-4 , price to 30g (+1g)
- Bull Ant pierce melee damage decrease to 18-2 , price to 54g (+2g)

- Beetle/Stag/Hercules arcane res unchanged.
- Stag XP from 72 to 82 , Stag price to 31g (+3g)
It used to be fire weakness, but now is fire ressistant lol, payback nerf.
- Hercules price to 55g (+9g)
- Flea price to 32g (-1g) 
- Tick price to 51g (+5g)

- Tarantula XP from 76 to 82
- Gargantuan melee damage decrease to 8-3 , price to 59g (+6g)
- Trapdoor Spider melee impact damage increase to 10-1

- Termite XP from 46 to 42
- Termite Solider price to 31g (+2g)


Nonhive foot units
- Hopper XP from 49 to 43
- Glider HP to 52 (-4) , price to 42g (+4g)
- Mantis cold res to 0% (+5%) , arcane res to 15% (+5%) , price to 30g (+2g)
- Skiper HP to 54 (+2) , price to 33g (-3g)

- Swarm & advancement have +fearless trait (inmune to AwE auras)
More stuff that can deal againist punisher (specially if normally pierce weak againist undead) might help.
NEUTRAL aligment, will not cause balance issues ... unless thralled LOL
- Infest XP from 70 to 80
- Drove HP to 40 (+2) , price to 54g (+6g)
AND MORE AWE COUNTERS COMING IN 4.31

- Gnat and all its advancement will now be 10% arcane ressistant

- Firefly XP from 55 to 45
- Lantern bug price to 30g (-2g)

- Regal price to 60g (+8g)
- Hornet price to 57g (+5g)
- Queen XP from 100 to 80 , arcane res to 20% (+10%) , price to 37g (-3g)
- Overmind arcane res to 20% (+10%)


ME - HOLY ORDER 

- Crusader arcane melee attack adjusted from 10-2 to 8-3 , price to 24g (-2g)
- Paladin price to 57g (+5g)

- Bishop XP from 93 to 80 , price to 30g (-6g)
- Priest price to 26g (-8g)
- Pope price to 48g (-2g)

- Torturer price to 56g (+4g)

- Judgementor price to 23g (-4g)

- Holy spirit XP from 100 to 95
- Arcane Spirit price to 63g (+13g)

- Listener price to 30g (-2g)
- Eye of Fate has accuracy(+5%) in ranged, price to 54g (+3g)

- Law price to 52g (+4g)
- Order price to 52g (+4g)
- Peacekeeper price to 54g (+6g)

- Mage XP from 100 to 85 , price to 35g (-5g)
- Ballast arcane damage increase to 10-4 , fire ranged damage increase to 19-2 , melee damage adjusted from 5-3 to 7-2
- Scholar price to 37g (-5g)
- Wisdomkeeper price to 58g (-2g)

- Witchhunter XP from 46 to 41
- Demonslayer XP from 86 to 78 , arcane ranged damage decrease to 14-2 , price to 30g (-4g)
- Purifier HP to 56g (+1g)


ME - INFERNAI

- Dominated price to 48g (+8g)

- Hellhound HP to 39 (+1) , price to 31g (-1g)
- Cerberus price to 53g (+9g)

- Gog XP from 48 to 42
- Magog XP from 78 to 80 , price to 28g (-4g)
- Incubus price to 55g (+5g)

- Troglodyte XP from 65 to 70 , price to 29g (+1g)
- Infernal Troglodyte price to 54g (+4g)

- Ifreet Master HP to 30 (+2) , price to 37g (-3g)
- Ifreet Sultan price to 54g (+11g)

- Pitlord price to 31g (+1g)
- Pit Master price to 55g (+8g)
- Tormentor price to 38g (+3g)

- Familiar price to 30g (+1g)
Had to distance more pricement of magog and familiar because familiar is significantly better unit.

- Archfiend +ME-Fury Getting replaced by +EOMA-Fury & EOMA +BloodLust(3) 
Unit can attack multiple targets in same turn, but not move and then attack. In compensation each kill will heal it +3.
- Sadist , BloodLust value lowered from 8 to 5 , XP from 80 to 75 , damage increase to 16-2 , price to 29g (-1g)
- Bloodbather HP to 70 (+4) , BloodLust value lowered from 8 to 6 , price to 54g (+6g)
- Horned One HP to 78 (+3) , movement to 4 (-1) , added EoMa BloodLust(3) , price to 57g (+4g)
10% pierce weakness in melee fighter is bad, I decided to not fix it and instead give +BloodLust(3)

- Demon XP from 73 to 75 , price to 32g (+3g)
Pretty bulky lv2 leadership unit
- Devil price to 62g (+9g)
- Lucifer price to 90g (+18g)


ME - ORACLES

- Evileye added parry(5%) on ranged , price to 33g (-1g)

- Master price to 31g (-1g)

- Arbiter XP from 46 to 42
- Therugist price to 31g (-1g)
- Judgementor price to 56g (+4g)

- Clergyman price to 24g (-8g)
- Bishop price to 44g (-11g)

- Necromantic XP from 114 to 95 , price to 38g (-4g)
- Quietus price to 65g (+17g)

- Mage price to 23g (-1g)
- Oracle XP from 50 to 47
- Prophet XP from 100 to 88 , price to 37g (-1g)

- Wizard XP from 50 to 48
- Warlock XP from 100 to 90 , price to 38g (-4g)
- Sorcerer price to 63g (+4g)

- Gravitymancer blade ranged strikes decrease by 1 , XP from 88 to 83 price to 28g (-4g)
- Telekenetic melee worsened from 5-5 to 4-4 , price to 60g (+6g)
- Scrapshifter Metalshards (blade) minimun strikes decreased to 2 , Metalshards (pierce) minimun strikes decreased to 1 , metal fist (8-1) cannot be more than 1 strike.

- Sage fire/cold ressist increase to 10% (+10%) 
- Psychic fire/cold ressist increase to 10% (+10%) , XP from 60 to 75 , price to 34g (-2g)
- Omnicient HP to 55 (+2) , price to 56g (+4g)

- Occultist price to 33g (-3g)
- Alchemist price to 58g (+2g)

- Conjurer impact melee damage increase to 12-2 , price to 36g (-5g)


ME - REFUGEES
Pretty interesting faction, I should test them soon.

- Cleaner XP from 54 to 47
- Purifier price to 38g (-4g)

- Messenger impact res to 15% (+5%) , cold res to 10% (+10%) , price to 31g (-3g)
- Envoy impact res to 15% (+5%) , cold res to 10% (+10%) , price to 56g (+8g)

- Gatekeeper price to 34g (+4g)
- Roadclearer blade ressistance to 55% (-5%) , price to 57g (+2g) 
low health, reason it doesn't cost even more.

- Stonewall XP from 88 to 82 , added description.
- Spire all physical ressist lowered by -5% , price to 60g (+3g)

- Longboat XP from 65 to 53
- Trireme price to 38g (+3g)

- Maceman price to 26g (-1g)
- Greeter price to 52g (+6g)

- Sarissan XP from 47 to 42
- Defender impact damage adjusted from 14-1 to 8-2 , ranged damage increase to 9-1
- Protector impact damage adjusted from 20-1 to 14-2 , ranged damage increase to 13-1 , price to 55g (+4g)
- Hoplite XP from 75 to 72
- Linebreaker price to 55g (+5g)
- Phalanx price to 55g (+8g)
- Javelineer price to 27g (-3g)

- Sniper XP from 77 to 72 , price to 26g (-2g)
- Deadeye price to 54g (+2g)


ME - SLAVERS
- All mutts (except berserk) fire ressistance to -10% (+10%)

- Elder Hawk price to 18g (+8g)
- Observer price to 19g (+9g)

- Entrancer price to 36g (-2g)

- Maneater gains +Feeding now
- Pursuer price to 28g (-1g)
- Chaser parry(5%) on melee , price to 53g (+6g)

- Provoker XP from 69 to 63 , price to 22g (-2g)
- Abuser price to 46g (+3g)

- Miner HP to 58 (-2) , price to 27g (+3g)
- Stoneshatterer HP to 72 (-2) , price to 55g (+7g)

- Slavemaster price to 57g (+14g)
- Subjugator price to 34g (+2g)

- Stalker price to 55g (+12g)


ME - TRIBE

- Boomerang Thrower melee damage decrease to 4-2 , NEW ATTACK: Boomerang 6-2 impact melee +spinning +attack only , ranged damage increase to 8-2 , price to 18g (+1g)
- Ranger NEW ATTACK: Boomerang 11-2 impact melee +spinning +attack-only

- Archer XP from 71 to 68 , price to 28g (-3g)
- Native price to 53g (+4g)

- Maneater HP to 53 (-5)

- Dartsman XP from 44 to 40
- Hunter XP from 76 to 72 , price to 31g (-2g)
- Slayer ranged damage decrease to 13-3 , price to 54g (+7g)

- Rowboat XP from 37 to 34
- Canoe price to 26g (-3g)
- Fishing boat HP to 49 (+3) , price to 26g (-3g)

- Decapitator price to 28g (-1g)
- Executioner price to 55g (+3g)

- Shaman ranged changed from 4-4 +magical to 5-4 +enchanted.
- Medicineman HP to 42 (+2) , ranged changed from 6-4 +magical to 7-4 +enchanted , price to 35g (-5g)
- Witchdoctor HP to 45 (+1) , XP from 100 to 87 , ranged changed from 6-4 +magical to 7-5 +enchanted , price to 37g (-3g)

- Voodoo Doctor curse attack reworked: damage 7-5 +magical adjusted to 7-6 +enchanted (more damage if no upgrades)
NEW ATTACK: Curse 6-5 +magical +slows , voodoo attacks +5% accuracy , price to 58g (+4g)

- Kangaroo HP to 43 (+3) , price to 26g (-1g)
- Boxer price to 55g (+9g)

- Endemic XP from 80 to 75 , price to 26g (-2g)
- Indigenous HP to 70 (+2) , pierce ressistance to 20% (+5%) , price to 53g (+5)
- Chieftain price to 59g (+4g)

---
## [KingDragoness/ProjectHypatios](https://github.com/KingDragoness/ProjectHypatios)@[0c9ca10174...](https://github.com/KingDragoness/ProjectHypatios/commit/0c9ca1017473c27159c6ffbdce178f3714f5773b)
#### Tuesday 2023-05-23 09:10:18 by KingDragoness

Hypatios 1.5.2b1 (quality of life improvements, bug fixes, new UI, balancing)
DONE (May 23)
• New section (Intermezzo2): platforming section shortcut to level 4.
o Tricky platforming and precision.
• Longer vents in sewers to the chamber 2.
• Chamber 2 chamber script changes
o Now after completing twice will have more difficult enemies
o New tutorial hint: “Harder Chamber”
 “In some chambers, the difficult may ramp up after you complete it multiple times.”
• Balancing: Nerf Sentinel attack
o Slower attack speed
o Lower damage
• Chest randomization problem
o Now uses the current scene index as additional seed
o Loot table now only allow 1 weapon item per container.
• Disabling player’s input now prevents camera from moving and weapon from shooting
• TV news needs texture
• New event: OnPlayerDied
o Executed when player is DEAD.
• Misleading Text: Notification hint workbench says “Most workbench cost 50 souls” when actually most are 35
• Bug: WeaponDisplay still opened when player died
• Bug: Tooltip still opened when player died
• Favourite item will be permanent except weapon which is stored in itemData
o List<string> will detect all items has been favourited
o Will be override during additem function
• Favourite menu UI use
o An entire new UIMode
o The category like serum, food, drinks, meds, alcohol shows all available consumables available to the player
o Radial menu which displays 6 primary slots:
 Serum
 Food
 Drinks
 Medicines
 Alcohol
 Favorites (to show all favorited consumables)
o Holding TAB to open the favourite shortcut
o Doesn’t pause the game but unlocks mouse control, prevent weapon from shooting and camera from moving.
o Only for quickly consume item, only consumables can be favourited
o Stats
 Hitpoint
 Alcohol meter
 Status effects
• Mainmenu additional stat progression:
o Total playtime progress.
o Current clock in the run.
• Heer Etres soldier 3d
o Recycled Mobius Guard with different helmet model and armor texture.
o Armor needs significant texture overhaul.
o Starfield’s space raider helmet (see OneNote)
• Looted item notification (similar to Genshin’s item loot)
o Max 4 item buttons
o Icon using RPGUI’s subcategory sprites
• Move RPGUI subcategory sprite to AssetDatabase
• New consumables: Rage Stim
o Regen HP -7 HP/s but gains gun damage, melee damage and movement speed.
• Grappling Hook [Wired only]: LMB to hook/unhook anchor. RMB to roll to the hooked anchor.
o Only available in WIRED chamber because it’ll break every level in the game.
o 3 ammo/anchors.
o Wire anchor.
o Sound effect for rolling the grappling hook.
• Placement Enemy: Adding merc enemy and healing bot to several levels
• Minor UI touchup for Paradox shop
• Bug: Workbench interact prompt still 50 souls not 35
• Chamber 8 changes
o Dialogue in chamber 8 needs to be reduced
o Remove several spaceguard
• Chamber 2 design is poorly executed and just straight up bad.
o Chamber 2 needs a paradox shortcut directly through the near exit of the chamber.
o Replace the pathetic stairs with elevator (use the travellator script, don’t use the shitty door script!).
• Problem narrative
o Conversing with the Emperor seems too random and very unfocused
o Emperor now only appears twice in intermezzo2. Next time will appear in level 6.
• Emperor only appear twice, after the 3rd chamber complete, Emperor will not appear in Intermezzo_2.

---
## [Areej-Muhajab/OCD-Ontology](https://github.com/Areej-Muhajab/OCD-Ontology)@[2b3b5517a2...](https://github.com/Areej-Muhajab/OCD-Ontology/commit/2b3b5517a2ba411a28fad19bca5072fa110e7890)
#### Tuesday 2023-05-23 09:10:32 by Areej-Muhajab

Add files via upload

The survey's primary objective is to evaluate the accuracy of the logical representations of concepts related to Obsessive-Compulsive Disorder (OCD). A logical representation of a concept encompasses its definition, which outlines the necessary and sufficient conditions for an entity to belong to that concept. Along with the definition, the logical representation includes details about the properties and connections of the concept with other related concepts.

To illustrate, let's consider the concept of "intrusive thoughts." It is associated with the "thought appraisal" class, indicating a relationship between the two. In the OCD ontology, we provide each class's precise natural language statements (positive statements), describing their logical representations involving concepts and relationships. Additionally, we offer an example that serves to clarify the natural language statement for a particular class. These examples draw inspiration from existing OCD assessment tools.

---
## [b4n/fishman-ctags](https://github.com/b4n/fishman-ctags)@[e6e018b90d...](https://github.com/b4n/fishman-ctags/commit/e6e018b90dcbcf6813243f700efc1ae5d4341ac5)
#### Tuesday 2023-05-23 09:12:04 by Colomban Wendling

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
## [software-mansion/react-native-reanimated](https://github.com/software-mansion/react-native-reanimated)@[0e96f1cd6e...](https://github.com/software-mansion/react-native-reanimated/commit/0e96f1cd6e0f6bae6a57aad6f5bd5208d5ae0d19)
#### Tuesday 2023-05-23 09:16:33 by Tomasz Żelawski

Remove plugin dev files from npm package (#4433)

<!-- Thanks for submitting a pull request! We appreciate you spending
the time to work on these changes. Please follow the template so that
the reviewers can easily understand what the code changes affect. -->

## Summary

Currently development files from `plugin/` are included in npm package.
This PR removes them from it.

b4:
<img width="253" alt="Screenshot 2023-05-08 at 14 39 29"
src="https://user-images.githubusercontent.com/40713406/236829343-1865480f-99d0-4843-adb2-f658db2acce0.png">
after:
<img width="238" alt="Screenshot 2023-05-08 at 14 39 51"
src="https://user-images.githubusercontent.com/40713406/236829379-7c31b6b4-27e1-493c-8be0-6254edbd0c4c.png">

Since [README is always
included](https://docs.npmjs.com/cli/v6/configuring-npm/package-json#files)
I renamed plugin's dev README and removed `README` from being included
in `package.json`.


## Test plan

I recommend using this powerful oneliner: 
`./createNPMPackage.sh && mkdir tarball-new && mv
react-native-reanimated-3.1.0.tgz tarball-new && tarball-new && tar -xf
react-native-reanimated-3.1.0.tgz && ..`
to see the contents of the new package.

Also run _some_ Example App to see if Reanimated plugin from the tarball
is actually working.

---
_Note_: Testing this PR took me longer than it should.

For some reason with current configuration of Example App and running it
on Android (I didn't check iOS) it's surprisingly difficult to use
reanimated from either tarball or unpacked tarball directory. I had to
make a new app and then include Example's source code there.

While it's not that troublesome I think we should have a more
streamlined approach for using custom reanimated package location for
tests with our Examples.

---------

Co-authored-by: Tomek Zawadzki <tomasz.zawadzki@swmansion.com>

---
## [ThePainkiller/Liberty-Station-13](https://github.com/ThePainkiller/Liberty-Station-13)@[0f74820c9d...](https://github.com/ThePainkiller/Liberty-Station-13/commit/0f74820c9d04762ac5b06907e6eb5207be80f136)
#### Tuesday 2023-05-23 09:18:11 by ThePainkiller

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
## [MiMillieuh/ublue-custom](https://github.com/MiMillieuh/ublue-custom)@[c7deb7d6fe...](https://github.com/MiMillieuh/ublue-custom/commit/c7deb7d6fe3aa4256d7a79123ffc250a24165263)
#### Tuesday 2023-05-23 09:27:33 by Arcitec

fix: friendlier experience in the "yafti" first boot template

- The first screen's "Pick some applications to get started" has been replaced with a friendly welcoming message.

- The second screen's difficult-to-understand "WARNING: This will modify your Flatpaks if you are rebasing!" has been replaced with an explanation of what it actually does.

- The application setup screen is now titled "Application Installer", since the previous title sounded too much like a silly rhyme. It's a minor change.

- All Flatpaks now default to system-wide install thanks to the great work of bsherman at https://github.com/ublue-os/yafti/pull/82. This saves tons of disk space for multi-user systems.

- The "system application" category have been split up into GNOME apps and every other system app, so that people on other desktop environments don't get all the GNOME apps.

- Apps that had too vague descriptions have been renamed to their full names, such as "Backup -> Deja Dup Backups".

- All app lists have been sorted alphabetically.

- Non-inclusive language in descriptions has been changed.

- Added SteamTinkerLaunch as a suggestion for the Steam category, which is the best tool for managing Steam game configurations and Proton installations, albeit very advanced since it can do practically anything the gamer needs. :)

---
## [intel/cluster-management-toolkit](https://github.com/intel/cluster-management-toolkit)@[fc805bc921...](https://github.com/intel/cluster-management-toolkit/commit/fc805bc9213be4de7273440bd2755f7358b6739c)
#### Tuesday 2023-05-23 10:30:09 by David Weinehall

Initial support for RKE2 + SUSE

Add some support for RKE2 and SUSE. RKE2 mostly takes care
of everything on its own, so it's pretty straightforward,
but getting customisations integrated still took some work.

What works?

cmtadm prepare
cmtadm setup-control-plane
cmtadm setup-cni
cmtadm teardown-control-plane
cmtadm purge
cmt prepare
cmt add-node
cmt remove-node
cmt purge

Using external CRI-O & external Containerd, using external CNI.

Additionally the feature gates needed for DRA should be possible
to set properly.

What is known not to work?

cmtadm upgrade-control-plane
cmt upgrade-node

This patch also adds some basic support for setup on SLES 15/OpenSUSE 15.
This requires some rather ugly hacks due to Python 3 being stuck
at Python 3.6. CMT requires at least 3.8. Thanks to a "magical"
shebang and by installing all Python dependencies using pip,
we can get around this, but it's not a recommended setup.
As soon as SLES 16/OpenSUSE 16 have been released "proper" support
will be added.

Pre-requisites for installation on SLES 15/OpenSUSE 15:

* Enable the Python and Container components
* Install python310 (ensure that python310-pip is installed too)

Recommended:

* Disable packagekit (it inevitably interferes with package installation
  at the most inopportunate times)
* You *might* need to disable firewalld; CMT will NOT disable it,
  due to security concerns.

Signed-off-by: David Weinehall <david.weinehall@intel.com>

---
## [Coxswain-Navigator/lobotomy-corp13](https://github.com/Coxswain-Navigator/lobotomy-corp13)@[928b2420d9...](https://github.com/Coxswain-Navigator/lobotomy-corp13/commit/928b2420d906fbdef89ce27d75db5afe713b147d)
#### Tuesday 2023-05-23 10:31:39 by Lance

Servant of Wrath

Records and Instability

Dash speed up

Fuck you I'll space indent all I like

There was some fuckin lint in this PR

God damned there's a lot of lint in here

Faction Check

Sprite update, minor bug fixes

Floating and Gun and Acid

Minor Records

Small update

Unnerfs resists

AoE hit fix

Gun update real

more res should mean less talk

Pixel Fix

Sound... Fix?

Broke the staff's legs, fuck those guys.

lmfao audio pains

Gun Rename, Spawn nerf

NO MORE FRIENDS FROM GUN

Faction change

acid tweak

LINT!

SW Code and Balance

SoW Temp commit

Scuff-Fix

SoW bonk update

Hermit range increase and ranged damage decrease

visual fix

Ending adjustments

I forgot to carry the 4

Visual indicator

minor fixes

Instability Tweaks

Paperwork Update

Anti-Self-Burn

Ending Update

Right view

A check that should be a non-issue but i'm making sure!

Breach Update and EGO update

More goo and FEMALE

Improvement and new Icons

---
## [Chodum91/Cosmic-Cows-](https://github.com/Chodum91/Cosmic-Cows-)@[f38db09d18...](https://github.com/Chodum91/Cosmic-Cows-/commit/f38db09d18ba38f0744617cf43a0bdb33029cc6c)
#### Tuesday 2023-05-23 10:55:46 by Mathhew Shannon Amos

Update README.md

...~^♠︎^.Rainwizzard.com.^♠︎^~Plus Google.Meet

...~^♠︎^.Rainwizzard.com.^♠︎^~Plus Google.Meet





What is 1e100.net? | Hacker News

What is 1e100.net? | Hacker News


https://account.rogers.com/?from_ts=myrogersidp_withoutcompleteuri&pid=userless&aid=eas&sid=07b16821-af94-45b7-aead-de77ff93a7eb&hostname=https:%2F%2Frogers-prd.transmit.security&token=eyJraWQiOiJlYXMiLCJjdHkiOiJKV1QiLCJ0eXAiOiJKT1NFIiwiZW5jIjoiQTI1NkdDTSIsImFsZyI6IlJTQS1PQUVQLTI1NiJ9.SS68_A_zIUASE2xUvY7hfh7bkm6I32O1lSNoWlKv6Igd31YZd9kFFnUyq68wdNXmbkuVnTW40wlSfXAXiYinDWGldegS84p_pAHdBY97bgspKmb_TaXyNXrgizSogMe0eDia5ePUQ1T_e5CVU8IbVBS8Rrtsy-yKKs4uhS9dSJtXTro4XA-EKwUr3d2W6RrI-PsdWy-kKGABU7k_RxwVOV3Rn6QYHcFJFH6XDmnxrCVlmvv-pGIc31HXWx9zWjyjFGD0DgHa9xXawa6stCc7-SNOL80RwUVW5NkLy6r9zZcC8U78PXaRxO9suPIBb2dYUVTzdpfL85KdxmwjL0WZ6A.P13aFgB2hTPNlMbW.rpNFhw-URouybKSuo4adoRMZ5NolGnPudWGXN_kE7jwC5uXfRzai2dHOQlXHZS0qAjUlh7-SPioo9yLgwVPAEpV97SXaoFcpOMY3req7mNrULDw61pZcEGUNIB4obi4QXG6M44P8PaPAxypsnoHzfmmzdtAyAlMcD6mVw7VgFn81YL5Ot97kjsdADdWeynzA7S88fir15TiDY8TGCd4mqnESTavxWMtHfDjQx807MUffZ2V-04oPB_N6EGVeQ9MEssuoGOQJWBFLmnE1wjyzREsCMELcPHN34phzDQ_bAPfe9ayFfGgL8Zc_Lx7dbB7bd2z2u83T_ORyFtiNk5XRlnk1_GjRiDVlPnrM30S1mMeaGPD2d0WBzjlT0TiCVA1klSFyaRokXqPGSWabWaWsOF_0bjhdUxpEYwwPiDvKCFAowWpHN8BDYuS1toXtZ63Cl2oxhX9TtAUfWCW1tkUgpz-X8ByDXF8jQURvwFOW32J6gMmDA-RufvPy-T47mczyh0n8eriXxx5hNEZOQAXaECtJXaWJNEleVuODrtXcUc1yMANhXy07CqQfWG_CWF6wQD_GUBbr1QB2Cm_cEkfc8K9nQLPX9hEMFGRUl31EmWFltE80AzSQbb67pYSqC8J3l9xdaaxMxFkSUtrLO2EeZB8fIfqHx2KT_RJT1VQruo_pAcEIcPIFzHKtrHUCaw3ouUQEQxdOUQ0Yo4vY8-haXsR8ugPzYZCqqP8R4_-vfrtcdNj-D5cLEfTmSygv3mTtOsUTIcZgINPXZiFsw70ozdj-HiuEcXRUiWfutOKYB2W3aVdKLty0KRmhumqy6Sg4chNCQ9IX53fHgmKn-f2niKmm5YP-ZFmQhi7NqsGOwouzM1YzKFzKfwQ3a5MehoWyZzti3X8bC06G2TyH-uagUou9LYg3XWy4ZopCeGxNlBCoxdvCo7cYXUlwYTjoZnqGbM_OqU4YKGdSNgMpALKffrIiC1cMytK_OWUn9FcMJHrhviaLxIXM103O_dhttpprCQzbp7884gUXyyxaZhkcv89-ifxRwpGC00fVwUMbEnGeai3ecXs8AE_GOhzFx6X6GmnjrLqfskte15uS04Bsj8p7iE-PR7jOuJ259X0b76qd7bNTFdwUFw2XuzKU81KUcQPyQoE0Xkqo8ugI7esmHEANaVEylOhkUvr7EZ3yULB4RbYZRKm5qTZs3xERkHrociuTTK5Vbr1Vx3ewArfNsSDDrTktjwKyZwGQRfUG_Ek8tuCUIFzS7vFZ1RIE7igVhEtt1JJA6FswU6f_A3VRufm-RJDgSDEZhWN-5Ny-NbUjTnLWkz2IFkc2aUHMmJKA7s4-o2FVOSGbgnTm8ffJJ6kr4Fw_fqO0JwO9GuCx1JEvx-JwvXGZyyM8Xxe1TLI-kaGQaG85dur2BbeVj5BlWAjbZrmI7nuiIqlXesrr4Q0ERcP5nNMoD0js_6B8T98HRKyesDByBu20VA_a8n2R3r2SJwwKla6vqgNaa7JgecAp9_W2i10tWQtrYaObPI5_hw6WoetokvJZnWslmvo9oM7QA1Yh3yRQNOOiHFHGwCOzywvXxfw71gRAOnVtA_1mEGElXhbLj8jHZS6PxVbi56k3J_BaQF_d.dWMoyTYGft3iV8G7eodVKA&brand=cbu&ui_locales=en&csmID=20304b18-b245-44b6-87e3-83250fbffe14&prompt=login

  <thanks change host name> to local host https://account.rogers.com/?


<iframe width="560" height="315" src="https://www.youtube.com/embed/d6Ix6zvx6AE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframWhite-Boy Papa.Legou to join~^♠︎^.Rain Wizard.h.^♠︎^~.Phone3 °F!DOCTYPE html><html lhttps://meet.google.com/ynu-otxi-ygr?pli=.~^♠︎^.Rainwizzard.com.^♠︎^~.Phone,1~^♠︎^.Rainwizzard.^♠︎^~.Phone,1nba.N.B has invited yg="en-GB"><head><script nonce="bdYM


P4s0T0yxL9DPyJyONQ">var DOCS_timing={}; DOCS_timing['pls']=new Date().getTime();</script><meta property="og:title" content="~^♠︎^.Rainwizzard.

><meta property="og:type" content="article"><meta property="og:site_name" content="Google Docs"><meta property="og:url" content="https://docs.google.com/document/d/1ItbxlBw0qIKzwu52aGIGqMPOEtaL0MGBQfB8yhzKlt8/edit?usp=embed_facebook"><meta property="og:description" content="https://video.sebastienbiollo.com/google.com_www.rain-wizzard.blogspot.com   copy and paste . How we use personal data https://rain-wizzard.blogspot.com/?m-1 https://video.sebastienbiollo.com/google.com_www.rain-wizzard.blogspot.com     We also use the data to operate our business, which include..."><meta name="google" content="notranslate"><meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0"><meta http-equiv="X-UA-Compatible" content="IE=edge;"><meta name="fragment" content="!"><meta name="referrer" content="strict-origin-when-cross-origin"><title>~^♠︎^.Rainwizzard.^♠︎^~. - Google Docs</title><link rel="shortcut icon" href="https://ssl.gstatic.com/docs/documents/images/kix-favicon7.ico"><link rel="chrome-webstore-item" href="https://chrome.google.com/webstore/detail/ghbmnnjooekpmoecnnnilnnbdlolhkhi"><link rel="chrome-webstore-item" href="https://chrome.google.com/webstore/detail/apdfllckaahabafndbhieahigkjlhalf"><link rel="manifest" href="/document/manifest.json" crossorigin="use-credentials"/><script nonce="bdYMP4s0T0yxL9DPyJyONQ">_docs_webfonts_fontFaces = null; _docs_webfonts_iframe_fontFaces = null;(function() {_docs_webfonts_createFontFaces = function(doc) {if (doc && doc.fonts) {var win = window; var fontFaceObject = {}; var docs_fontFaces_data = {"Roboto-400-normal":{"fontFamily":"docs-Roboto","sourceString":"local(\u0027Roboto\u0027), local(\u0027Roboto-Regular\u0027), url(filesystem:https://docs.google.com/persistent/docs/fonts/KFOmCnqEu92Fr1Me4A.woff2), url(//fonts.gstatic.com/s/roboto/v30/KFOmCnqEu92Fr1Me4A.woff2)","weight":"400","style":"normal","subset":"*"},"Roboto-400-italic":{"fontFamily":"docs-Roboto","sourceString":"local(\u0027Roboto Italic\u0027), local(\u0027Roboto-Italic\u0027), url(filesystem:https://docs.google.com/persistent/docs/fonts/KFOkCnqEu92Fr1Mu52xK.woff2), url(//fonts.gstatic.com/s/roboto/v30/KFOkCnqEu92Fr1Mu52xK.woff2)","weight":"400","style":"italic","subset":"*"},"Roboto-700-normal":{"fontFamily":"docs-Roboto","sourceString":"local(\u0027Roboto Bold\u0027), local(\u0027Roboto-Bold\u0027), url(filesystem:https://docs.google.com/persistent/docs/fonts/KFOlCnqEu92Fr1MmWUlvBg.woff2), url(//fonts.gstatic.com/s/roboto/v30/KFOlCnqEu92Fr1MmWUlvBg.woff2)","weight":"700","style":"normal","subset":"*"},"Roboto-700-italic":{"fontFamily":"docs-Roboto","sourceString":"local(\u0027Roboto Bold Italic\u0027), local(\u0027Roboto-BoldItalic\u0027), url(filesystem:https://docs.google.com/persistent/docs/fonts/KFOjCnqEu92Fr1Mu51TzBhc4.woff2), url(//fonts.gstatic.com/s/roboto/v30/KFOjCnqEu92Fr1Mu51TzBhc4.woff2)","weight":"700","style":"italic","subset":"*"}}; for (var identifierString in docs_fontFaces_data) {var fontFace = new win.FontFace( docs_fontFaces_data[identifierString]['fontFamily'], docs_fontFaces_data[identifierString]['sourceString'],{'style': docs_fontFaces_data[identifierString]['style'], 'weight': docs_fontFaces_data[identifierString]['weight']}); fontFace.load().then(function(loadedFontFace) {doc.fonts.add(loadedFontFace);}); fontFaceObject[identifierString] = fontFace;}return fontFaceObject;}return null;}; _docs_webfonts_fontFaces = _docs_webfonts_createFontFaces(document);})();DOCS_timing['wpid']=new Date().getTime();</script><style nonce="W_XnfdE16RohD_dZ0lweOQ">.gb_5a:not(.gb_Ld){font:13px/27px Roboto,Arial,sans-serif;z-index:986}@-webkit-keyframes gb__a{0%{opacity:0}50%{opacity:1}}@keyframes gb__a{0%{opacity:0}50%{opacity:1}}a.gb_ca{border:none;color:#4285f4;cursor:default;font-weight:bold;outline:none;position:relative;text-align:center;text-decoration:none;text-transform:uppercase;white-space:nowrap;-webkit-user-select:none}a.gb_ca:hover:after,a.gb_ca:focus:after{background-color:rgba(0,0,0,.12);content:"";height:100%;left:0;position:absolute;top:0;width:100%}a.gb_ca:hover,a.gb_ca:focus{text-decoration:none}a.gb_ca:active{background-color:rgba(153,153,153,.4);text-decoration:none}a.gb_da{background-color:#4285f4;color:#fff}a.gb_da:active{background-color:#0043b2}.gb_ea{-webkit-box-shadow:0 1px 1px rgba(0,0,0,.16);box-shadow:0 1px 1px rgba(0,0,0,.16)}.gb_ca,.gb_da,.gb_fa,.gb_ga{display:inline-block;line-height:28px;padding:0 12px;-webkit-border-radius:2px;border-radius:2px}.gb_fa{background:#f8f8f8;border:1px solid #c6c6c6}.gb_ga{background:#f8f8f8}.gb_fa,#gb a.gb_fa.gb_fa,.gb_ga{color:#666;cursor:default;text-decoration:none}#gb a.gb_ga.gb_ga{cursor:default;text-decoration:none}.gb_ga{border:1px solid #4285f4;font-weight:bold;outline:none;background:#4285f4;background:-webkit-linear-gradient(top,#4387fd,#4683ea);background:linear-gradient(top,#4387fd,#4683ea);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#4387fd,endColorstr=#4683ea,GradientType=0)}#gb a.gb_ga.gb_ga{color:#fff}.gb_ga:hover{-webkit-box-shadow:0 1px 0 rgba(0,0,0,.15);box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_ga:active{-webkit-box-shadow:inset 0 2px 0 rgba(0,0,0,.15);box-shadow:inset 0 2px 0 rgba(0,0,0,.15);background:#3c78dc;background:-webkit-linear-gradient(top,#3c7ae4,#3f76d3);background:linear-gradient(top,#3c7ae4,#3f76d3);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#3c7ae4,endColorstr=#3f76d3,GradientType=0)}#gb .gb_ia{background:#fff;border:1px solid #dadce0;color:#1a73e8;display:inline-block;text-decoration:none}#gb .gb_ia:hover{background:#f8fbff;border-color:#dadce0;color:#174ea6}#gb .gb_ia:focus{background:#f4f8ff;color:#174ea6;outline:1px solid #174ea6}#gb .gb_ia:active,#gb .gb_ia:focus:active{background:#ecf3fe;color:#174ea6}#gb .gb_ia.gb_5{background:transparent;border:1px solid #5f6368;color:#8ab4f8;text-decoration:none}#gb .gb_ia.gb_5:hover{background:rgba(255,255,255,.04);color:#e8eaed}#gb .gb_ia.gb_5:focus{background:rgba(232,234,237,.12);color:#e8eaed;outline:1px solid #e8eaed}#gb .gb_ia.gb_5:active,#gb .gb_ia.gb_5:focus:active{background:rgba(232,234,237,.1);color:#e8eaed}.gb_i{display:none!important}.gb_Oa{visibility:hidden}.gb_kd{display:inline-block;vertical-align:middle}.gb_Cf .gb_h{bottom:-3px;right:-5px}.gb_Df{position:relative}.gb_e{display:inline-block;outline:none;vertical-align:middle;-webkit-border-radius:2px;border-radius:2px;-webkit-box-sizing:border-box;box-sizing:border-box;height:40px;width:40px;color:#000;cursor:pointer;text-decoration:none}#gb#gb a.gb_e{color:#000;cursor:pointer;text-decoration:none}.gb_7a{border-color:transparent;border-bottom-color:#fff;border-style:dashed dashed solid;border-width:0 8.5px 8.5px;display:none;position:absolute;left:11.5px;top:43px;z-index:1;height:0;width:0;-webkit-animation:gb__a .2s;animation:gb__a .2s}.gb_8a{border-color:transparent;border-style:dashed dashed solid;border-width:0 8.5px 8.5px;display:none;position:absolute;left:11.5px;z-index:1;height:0;width:0;-webkit-animation:gb__a .2s;animation:gb__a .2s;border-bottom-color:#ccc;border-bottom-color:rgba(0,0,0,.2);top:42px}x:-o-prefocus,div.gb_8a{border-bottom-color:#ccc}.gb_L{background:#fff;border:1px solid #ccc;border-color:rgba(0,0,0,.2);color:#000;-webkit-box-shadow:0 2px 10px rgba(0,0,0,.2);box-shadow:0 2px 10px rgba(0,0,0,.2);display:none;outline:none;overflow:hidden;position:absolute;right:8px;top:62px;-webkit-animation:gb__a .2s;animation:gb__a .2s;-webkit-border-radius:2px;border-radius:2px;-webkit-user-select:text}.gb_kd.gb_ya .gb_7a,.gb_kd.gb_ya .gb_8a,.gb_kd.gb_ya .gb_L,.gb_ya.gb_L{display:block}.gb_kd.gb_ya.gb_Ef .gb_7a,.gb_kd.gb_ya.gb_Ef .gb_8a{display:none}.gb_Ff{position:absolute;right:8px;top:62px;z-index:-1}.gb_Ua .gb_7a,.gb_Ua .gb_8a,.gb_Ua .gb_L{margin-top:-10px}.gb_kd:first-child,#gbsfw:first-child+.gb_kd{padding-left:4px}.gb_Ca.gb_Ue .gb_kd:first-child{padding-left:0}.gb_Ve{position:relative}.gb_Vc .gb_Ve,.gb_2d .gb_Ve{float:right}.gb_e{padding:8px;cursor:pointer}.gb_Ca .gb_cd:not(.gb_ca):focus img{background-color:rgba(0,0,0,.20);outline:none;-webkit-border-radius:50%;border-radius:50%}.gb_We button svg,.gb_e{-webkit-border-radius:50%;border-radius:50%}.gb_We button:focus:not(:focus-visible) svg,.gb_We button:hover svg,.gb_We button:active svg,.gb_e:focus:not(:focus-visible),.gb_e:hover,.gb_e:active,.gb_e[aria-expanded=true]{outline:none}.gb_Ec .gb_We.gb_Xe button:focus-visible svg,.gb_We button:focus-visible svg,.gb_e:focus-visible{outline:1px solid #202124}.gb_Ec .gb_We button:focus-visible svg,.gb_Ec .gb_e:focus-visible{outline:1px solid #f1f3f4}@media (forced-colors:active){.gb_Ec .gb_We.gb_Xe button:focus-visible svg,.gb_We button:focus-visible svg,.gb_Ec .gb_We button:focus-visible svg{outline:1px solid currentcolor}}.gb_Ec .gb_We.gb_Xe button:focus svg,.gb_Ec .gb_We.gb_Xe button:focus:hover svg,.gb_We button:focus svg,.gb_We button:focus:hover svg,.gb_e:focus,.gb_e:focus:hover{background-color:rgba(60,64,67,.1)}.gb_Ec .gb_We.gb_Xe button:active svg,.gb_We button:active svg,.gb_e:active{background-color:rgba(60,64,67,.12)}.gb_Ec .gb_We.gb_Xe button:hover svg,.gb_We button:hover svg,.gb_e:hover{background-color:rgba(60,64,67,.08)}.gb_wa .gb_e.gb_Xa:hover{background-color:transparent}.gb_e[aria-expanded=true],.gb_e:hover[aria-expanded=true]{background-color:rgba(95,99,104,.24)}.gb_e[aria-expanded=true] .gb_Ze,.gb_e[aria-expanded=true] .gb_0e{fill:#5f6368;opacity:1}.gb_Ec .gb_We button:hover svg,.gb_Ec .gb_e:hover{background-color:rgba(232,234,237,.08)}.gb_Ec .gb_We button:focus svg,.gb_Ec .gb_We button:focus:hover svg,.gb_Ec .gb_e:focus,.gb_Ec .gb_e:focus:hover{background-color:rgba(232,234,237,.10)}.gb_Ec .gb_We button:active svg,.gb_Ec .gb_e:active{background-color:rgba(232,234,237,.12)}.gb_Ec .gb_e[aria-expanded=true],.gb_Ec .gb_e:hover[aria-expanded=true]{background-color:rgba(255,255,255,.12)}.gb_Ec .gb_e[aria-expanded=true] .gb_Ze,.gb_Ec .gb_e[aria-expanded=true] .gb_0e{fill:#fff;opacity:1}.gb_kd{padding:4px}.gb_Ca.gb_Ue .gb_kd{padding:4px 2px}.gb_Ca.gb_Ue .gb_b.gb_kd{padding-left:6px}.gb_L{z-index:991;line-height:normal}.gb_L.gb_1e{left:8px;right:auto}@media (max-width:350px){.gb_L.gb_1e{left:0}}.gb_2e .gb_L{top:56px}.gb_J .gb_e,.gb_K .gb_J .gb_e{background-position:-64px -29px}.gb_p .gb_J .gb_e{background-position:-29px -29px;opacity:1}.gb_J .gb_e,.gb_J .gb_e:hover,.gb_J .gb_e:focus{opacity:1}.gb_Md{display:none}.gb_h{display:none}.gb_4c{font-family:Google Sans,Roboto,Helvetica,Arial,sans-serif;font-size:20px;font-weight:400;letter-spacing:0.25px;line-height:48px;margin-bottom:2px;opacity:1;overflow:hidden;padding-left:16px;position:relative;text-overflow:ellipsis;vertical-align:middle;top:2px;white-space:nowrap;-webkit-flex:1 1 auto;flex:1 1 auto}.gb_4c.gb_5c{color:#3c4043}.gb_Ca.gb_Da .gb_4c{margin-bottom:0}.gb_6c.gb_7c .gb_4c{padding-left:4px}.gb_Ca.gb_Da .gb_8c{position:relative;top:-2px}.gb_Ca{color:black;min-width:320px;position:relative;-webkit-transition:box-shadow 250ms;transition:box-shadow 250ms}.gb_Ca.gb_Nc{min-width:240px}.gb_Ca.gb_Nd .gb_Od{display:none}.gb_Ca.gb_Nd .gb_Pd{height:56px}header.gb_Ca{display:block}.gb_Ca svg{fill:currentColor}.gb_Qd{position:fixed;top:0;width:100%}.gb_Rd{-webkit-box-shadow:0px 4px 5px 0px rgba(0,0,0,.14),0px 1px 10px 0px rgba(0,0,0,.12),0px 2px 4px -1px rgba(0,0,0,.2);box-shadow:0px 4px 5px 0px rgba(0,0,0,.14),0px 1px 10px 0px rgba(0,0,0,.12),0px 2px 4px -1px rgba(0,0,0,.2)}.gb_Sd{height:64px}.gb_Pd{-webkit-box-sizing:border-box;box-sizing:border-box;position:relative;width:100%;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-pack:space-between;-webkit-justify-content:space-between;justify-content:space-between;min-width:-webkit-min-content;min-width:min-content}.gb_Ca:not(.gb_Da) .gb_Pd{padding:8px}.gb_Ca.gb_Td .gb_Pd{-webkit-flex:1 0 auto;flex:1 0 auto}.gb_Ca .gb_Pd.gb_Ud.gb_Vd{min-width:0}.gb_Ca.gb_Da .gb_Pd{padding:4px;padding-left:8px;min-width:0}.gb_Od{height:48px;vertical-align:middle;white-space:nowrap;-webkit-box-align:center;-webkit-align-items:center;align-items:center;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-user-select:none}.gb_Xd>.gb_Od{display:table-cell;width:100%}.gb_6c{padding-right:30px;-webkit-box-sizing:border-box;box-sizing:border-box;-webkit-flex:1 0 auto;flex:1 0 auto}.gb_Ca.gb_Da .gb_6c{padding-right:14px}.gb_Zd{-webkit-flex:1 1 100%;flex:1 1 100%}.gb_Zd>:only-child{display:inline-block}.gb_0d.gb_Wc{padding-left:4px}.gb_0d.gb_1d,.gb_Ca.gb_Td .gb_0d,.gb_Ca.gb_Da:not(.gb_2d) .gb_0d{padding-left:0}.gb_Ca.gb_Da .gb_0d.gb_1d{padding-right:0}.gb_Ca.gb_Da .gb_0d.gb_1d .gb_wa{margin-left:10px}.gb_Wc{display:inline}.gb_Ca.gb_Qc .gb_0d.gb_3d,.gb_Ca.gb_2d .gb_0d.gb_3d{padding-left:2px}.gb_4c{display:inline-block}.gb_0d{-webkit-box-sizing:border-box;box-sizing:border-box;height:48px;line-height:normal;padding:0 4px;padding-left:30px;-webkit-flex:0 0 auto;flex:0 0 auto;-webkit-box-pack:flex-end;-webkit-justify-content:flex-end;justify-content:flex-end}.gb_2d{height:48px}.gb_Ca.gb_2d{min-width:initial;min-width:auto}.gb_2d .gb_0d{float:right;padding-left:32px}.gb_2d .gb_0d.gb_4d{padding-left:0}.gb_5d{font-size:14px;max-width:200px;overflow:hidden;padding:0 12px;text-overflow:ellipsis;white-space:nowrap;-webkit-user-select:text}.gb_6d{-webkit-transition:background-color .4s;transition:background-color .4s}.gb_7d{color:black}.gb_Ec{color:white}.gb_Ca a,.gb_Kc a{color:inherit}.gb_z{color:rgba(0,0,0,.87)}.gb_Ca svg,.gb_Kc svg,.gb_6c .gb_8d,.gb_Vc .gb_8d{color:#5f6368;opacity:1}.gb_Ec svg,.gb_Kc.gb_Oc svg,.gb_Ec .gb_6c .gb_8d,.gb_Ec .gb_6c .gb_Dc,.gb_Ec .gb_6c .gb_8c,.gb_Kc.gb_Oc .gb_8d{color:rgba(255,255,255,0.87)}.gb_Ec .gb_6c .gb_Cc:not(.gb_9d){opacity:0.87}.gb_5c{color:inherit;opacity:1;text-rendering:optimizeLegibility;-webkit-font-smoothing:antialiased}.gb_Ec .gb_5c,.gb_7d .gb_5c{opacity:1}.gb_ae{position:relative}.gb_be{font-family:arial,sans-serif;line-height:normal;padding-right:15px}a.gb_m,span.gb_m{color:rgba(0,0,0,.87);text-decoration:none}.gb_Ec a.gb_m,.gb_Ec span.gb_m{color:white}a.gb_m:focus{outline-offset:2px}a.gb_m:hover{text-decoration:underline}.gb_n{display:inline-block;padding-left:15px}.gb_n .gb_m{display:inline-block;line-height:24px;vertical-align:middle}.gb_ce{font-family:Google Sans,Roboto,Helvetica,Arial,sans-serif;font-weight:500;font-size:14px;letter-spacing:0.25px;line-height:16px;margin-left:10px;margin-right:8px;min-width:96px;padding:9px 23px;text-align:center;vertical-align:middle;-webkit-border-radius:4px;border-radius:4px;-webkit-box-sizing:border-box;box-sizing:border-box}.gb_Ca.gb_2d .gb_ce{margin-left:8px}#gb a.gb_ga.gb_ga.gb_ce{cursor:pointer}.gb_ga.gb_ce:hover{background:#1b66c9;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_ga.gb_ce:focus,.gb_ga.gb_ce:hover:focus{background:#1c5fba;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_ga.gb_ce:active{background:#1b63c1;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_ce{background:#1a73e8;border:1px solid transparent}.gb_Ca.gb_Da .gb_ce{padding:9px 15px;min-width:80px}.gb_de{text-align:left}#gb .gb_Ec a.gb_ce:not(.gb_5),#gb.gb_Ec a.gb_ce{background:#fff;border-color:#dadce0;-webkit-box-shadow:none;box-shadow:none;color:#1a73e8}#gb a.gb_ga.gb_5.gb_ce{background:#8ab4f8;border:1px solid transparent;-webkit-box-shadow:none;box-shadow:none;color:#202124}#gb .gb_Ec a.gb_ce:hover:not(.gb_5),#gb.gb_Ec a.gb_ce:hover{background:#f8fbff;border-color:#cce0fc}#gb a.gb_ga.gb_5.gb_ce:hover{background:#93baf9;border-color:transparent;-webkit-box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.3);box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.3)}#gb .gb_Ec a.gb_ce:focus:not(.gb_5),#gb .gb_Ec a.gb_ce:focus:hover:not(.gb_5),#gb.gb_Ec a.gb_ce:focus:not(.gb_5),#gb.gb_Ec a.gb_ce:focus:hover:not(.gb_5){background:#f4f8ff;outline:1px solid #c9ddfc}#gb a.gb_ga.gb_5.gb_ce:focus,#gb a.gb_ga.gb_5.gb_ce:focus:hover{background:#a6c6fa;border-color:transparent;-webkit-box-shadow:none;box-shadow:none}#gb .gb_Ec a.gb_ce:active:not(.gb_5),#gb.gb_Ec a.gb_ce:active{background:#ecf3fe}#gb a.gb_ga.gb_5.gb_ce:active{background:#a1c3f9;-webkit-box-shadow:0 1px 2px rgba(60,64,67,.3),0 2px 6px 2px rgba(60,64,67,.15);box-shadow:0 1px 2px rgba(60,64,67,.3),0 2px 6px 2px rgba(60,64,67,.15)}.gb_wa{background-color:rgba(255,255,255,.88);border:1px solid #dadce0;-webkit-box-sizing:border-box;box-sizing:border-box;cursor:pointer;display:inline-block;max-height:48px;overflow:hidden;outline:none;padding:0;vertical-align:middle;width:134px;-webkit-border-radius:8px;border-radius:8px}.gb_wa.gb_5{background-color:transparent;border:1px solid #5f6368}.gb_xa{display:inherit}.gb_wa.gb_5 .gb_xa{background:#fff;-webkit-border-radius:4px;border-radius:4px;display:inline-block;left:8px;margin-right:5px;position:relative;padding:3px;top:-1px}.gb_wa:hover{border:1px solid #d2e3fc;background-color:rgba(248,250,255,.88)}.gb_wa.gb_5:hover{background-color:rgba(241,243,244,.04);border:1px solid #5f6368}.gb_wa:focus-visible,.gb_wa:focus{background-color:rgba(255,255,255);outline:1px solid #202124;-webkit-box-shadow:0px 1px 2px 0px rgba(60,64,67,.3),0px 1px 3px 1px rgba(60,64,67,.15);box-shadow:0px 1px 2px 0px rgba(60,64,67,.3),0px 1px 3px 1px rgba(60,64,67,.15)}.gb_wa.gb_5:focus-visible,.gb_wa.gb_5:focus{background-color:rgba(241,243,244,.12);outline:1px solid #f1f3f4;-webkit-box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px 0 rgba(0,0,0,.3);box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px 0 rgba(0,0,0,.3)}.gb_wa.gb_5:active,.gb_wa.gb_ya.gb_5:focus{background-color:rgba(241,243,244,.1);border:1px solid #5f6368}.gb_za{display:inline-block;padding-bottom:2px;padding-left:7px;padding-top:2px;text-align:center;vertical-align:middle;line-height:32px;width:78px}.gb_wa.gb_5 .gb_za{line-height:26px;margin-left:0;padding-bottom:0;padding-left:0;padding-top:0;width:72px}.gb_za.gb_Aa{background-color:#f1f3f4;-webkit-border-radius:4px;border-radius:4px;margin-left:8px;padding-left:0}.gb_za.gb_Aa .gb_Ba{vertical-align:middle}.gb_Ca:not(.gb_Da) .gb_wa{margin-left:10px;margin-right:4px}.gb_Ea{max-height:32px;width:78px}.gb_wa.gb_5 .gb_Ea{max-height:26px;width:72px}.gb_g{-webkit-background-size:32px 32px;background-size:32px 32px;border:0;-webkit-border-radius:50%;border-radius:50%;display:block;margin:0px;position:relative;height:32px;width:32px;z-index:0}.gb_Pa{background-color:#e8f0fe;border:1px solid rgba(32,33,36,.08);position:relative}.gb_Pa.gb_g{height:30px;width:30px}.gb_Pa.gb_g:hover,.gb_Pa.gb_g:active{-webkit-box-shadow:none;box-shadow:none}.gb_Qa{background:#fff;border:none;-webkit-border-radius:50%;border-radius:50%;bottom:2px;-webkit-box-shadow:0px 1px 2px 0px rgba(60,64,67,.30),0px 1px 3px 1px rgba(60,64,67,.15);box-shadow:0px 1px 2px 0px rgba(60,64,67,.30),0px 1px 3px 1px rgba(60,64,67,.15);height:14px;margin:2px;position:absolute;right:0;width:14px}.gb_Ra{color:#1f71e7;font:400 22px/32px Google Sans,Roboto,Helvetica,Arial,sans-serif;text-align:center;text-transform:uppercase}@media (min-resolution:1.25dppx),(-o-min-device-pixel-ratio:5/4),(-webkit-min-device-pixel-ratio:1.25),(min-device-pixel-ratio:1.25){.gb_g::before,.gb_Sa::before{display:inline-block;-webkit-transform:scale(.5);transform:scale(.5);-webkit-transform-origin:left 0;transform-origin:left 0}.gb_r .gb_Sa::before{-webkit-transform:scale(0.416666667);transform:scale(0.416666667)}}.gb_g:hover,.gb_g:focus{-webkit-box-shadow:0 1px 0 rgba(0,0,0,.15);box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_g:active{-webkit-box-shadow:inset 0 2px 0 rgba(0,0,0,.15);box-shadow:inset 0 2px 0 rgba(0,0,0,.15)}.gb_g:active::after{background:rgba(0,0,0,.1);-webkit-border-radius:50%;border-radius:50%;content:"";display:block;height:100%}.gb_Ta{cursor:pointer;line-height:40px;min-width:30px;opacity:.75;overflow:hidden;vertical-align:middle;text-overflow:ellipsis}.gb_e.gb_Ta{width:auto}.gb_Ta:hover,.gb_Ta:focus{opacity:.85}.gb_Ua .gb_Ta,.gb_Ua .gb_Va{line-height:26px}#gb#gb.gb_Ua a.gb_Ta,.gb_Ua .gb_Va{font-size:11px;height:auto}.gb_Wa{border-top:4px solid #000;border-left:4px dashed transparent;border-right:4px dashed transparent;display:inline-block;margin-left:6px;opacity:.75;vertical-align:middle}.gb_Xa:hover .gb_Wa{opacity:.85}.gb_wa>.gb_b{padding:3px 3px 3px 4px}.gb_Za.gb_Oa{color:#fff}.gb_p .gb_Ta,.gb_p .gb_Wa{opacity:1}#gb#gb.gb_p.gb_p a.gb_Ta,#gb#gb .gb_p.gb_p a.gb_Ta{color:#fff}.gb_p.gb_p .gb_Wa{border-top-color:#fff;opacity:1}.gb_K .gb_g:hover,.gb_p .gb_g:hover,.gb_K .gb_g:focus,.gb_p .gb_g:focus{-webkit-box-shadow:0 1px 0 rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.2);box-shadow:0 1px 0 rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.2)}.gb_0a .gb_b,.gb_1a .gb_b{position:absolute;right:1px}.gb_b.gb_o,.gb_2a.gb_o,.gb_Xa.gb_o{-webkit-flex:0 1 auto;flex:0 1 auto;-webkit-flex:0 1 main-size;flex:0 1 main-size}.gb_3a.gb_4a .gb_Ta{width:30px!important}.gb_d{height:40px;position:absolute;right:-5px;top:-5px;width:40px}.gb_5a .gb_d,.gb_6a .gb_d{right:0;top:0}.gb_b .gb_e{padding:4px}.gb_fe{display:none}sentinel{}</style><script nonce="bdYMP4s0T0yxL9DPyJyONQ">DOCS_timing['ojls']=new Date().getTime();</script><script nonce="bdYMP4s0T0yxL9DPyJyONQ">;this.gbar_={CONFIG:[[[0,"www.gstatic.com","og.qtm.en_US.gCY_j2aIrY4.es5.O","ca","en-GB","25",0,[4,2,"","","","500587755","0"],null,"PUjCY6rNOc7cwbkP796qwAQ",null,0,"og.qtm.u7mWlFl1QR4.L.W.O","AA2YrTu68--9ZuKdtjYX-t7k4usVb-YyZg","AA2YrTvz7ig2_pXD7E6HPsesgafZ3WrM_Q","",2,1,200,"CAN",null,null,"25","25",1],null,[1,0.1000000014901161,2,1],[1,0.001000000047497451,1],[1,0,0,null,"0","mattamos250@gmail.com","","AN7pSW3AzD64S0As8m_EzEEeX1mgGa-L-ZDh4PrdbMm0zQrHFvbWEF-XTqE7Ftsz6De5Jh44Y7-K3Fkk76FRW_95CJOoJm6gpQ"],[0,0,"",1,0,0,0,0,0,0,null,0,0,null,0,0,null,null,0,0,0,"","","","","","",null,0,0,0,0,0,null,null,null,"rgba(32,33,36,1)","rgba(255,255,255,1)",0,0,0,null,null,1,0,0],["%1$s (default)","Brand account",1,"%1$s (delegated)",1,null,83,"/document/d/1ItbxlBw0qIKzwu52aGIGqMPOEtaL0MGBQfB8yhzKlt8/edit?authuser=$authuser",null,null,null,1,"https://accounts.google.com/ListAccounts?authuser=0\u0026pid=25\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=en-GB\u0026ts=35",0,"dashboard",null,null,null,null,"Profile","",1,null,"Signed out","https://accounts.google.com/AccountChooser?source=ogb\u0026continue=$continue\u0026Email=$email\u0026ec=GAhAGQ","https://accounts.google.com/RemoveLocalAccount?source=ogb","Remove","Sign in",0,1,1,0,1,1,0,null,null,null,"Session expired",null,null,null,"Visitor",null,"Default","Delegated","Sign out of all accounts",1,null,null,0,null,null,"myaccount.google.com","https",0,1,0],null,["1","gci_91f30755d6a6b787dcc2a4062e6e9824.js","googleapis.client:gapi.iframes","0","en-GB"],null,null,null,null,["m;/_/scs/abc-static/_/js/k=gapi.gapi.en.WEPncdil2Uw.O/d=1/rs=AHpOoo-eOecLLtOXEl3I3kIuMsKXRkDMmA/m=__features__","https://apis.google.com","","","1","",null,1,"es_plusone_gc_20221206.0_p0","en-GB",null,0],[0.009999999776482582,"ca","25",[null,"","0",null,1,5184000,null,null,"",null,null,null,null,null,0,null,0,0,1,0,0,0,null,null,0,0,null,0,0,0,0,0],null,null,null,0,null,null,["5061451","google\\.(com|ru|ca|by|kz|com\\.mx|com\\.tr)$",1]],[1,1,null,40400,25,"CAN","en-GB","500587755.0",8,0.009999999776482582,1,0,null,null,null,null,"",null,null,null,"PUjCY6rNOc7cwbkP796qwAQ",0,0,0,null,2,5,"ug",81,0,0,1,0,0],[[null,null,null,"https://www.gstatic.com/og/_/js/k=og.qtm.en_US.gCY_j2aIrY4.es5.O/rt=j/m=qabr,qgl,q_dnp,qcwid,qbg,qbd,qapid/exm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin,qhpr/d=1/ed=1/rs=AA2YrTu68--9ZuKdtjYX-t7k4usVb-YyZg"],[null,null,null,"https://www.gstatic.com/og/_/ss/k=og.qtm.u7mWlFl1QR4.L.W.O/m=qcwid/excm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin,qhpr/d=1/ed=1/ct=zgms/rs=AA2YrTvz7ig2_pXD7E6HPsesgafZ3WrM_Q"]],null,null,null,[[[null,null,[null,null,null,"https://ogs.google.com/u/0/widget/account?sea=1"],0,414,372,57,4,1,0,0,65,66,8000,"https://accounts.google.com/SignOutOptions?hl=en-GB\u0026continue=https://docs.google.com/document/d/1ItbxlBw0qIKzwu52aGIGqMPOEtaL0MGBQfB8yhzKlt8/edit\u0026service=writely",68,2,null,null,1,113,"Something went wrong. Refresh to try again or %1$schoose another account%2$s.",3,null,null,75,0,null,null,null,null,null,null,null,"/widget/account",["https","myaccount.google.com",0,32,83,0],0,0,1,["Critical security alert","Important recommended actions"],0]],0,[null,null,null,"https://www.gstatic.com/og/_/js/k=og.qtm.en_US.gCY_j2aIrY4.es5.O/rt=j/m=qdsh/d=1/ed=1/rs=AA2YrTu68--9ZuKdtjYX-t7k4usVb-YyZg"],"25","25",1,0,null,"en-GB",0,["/document/d/1ItbxlBw0qIKzwu52aGIGqMPOEtaL0MGBQfB8yhzKlt8/edit?authuser=$authuser","https://accounts.google.com/AddSession?service=wise\u0026continue=https://docs.google.com/document/d/1ItbxlBw0qIKzwu52aGIGqMPOEtaL0MGBQfB8yhzKlt8/edit\u0026ec=GAlAGQ","https://accounts.google.com/Logout?service=wise\u0026continue=https://docs.google.com\u0026ec=GAdAGQ","https://accounts.google.com/ListAccounts?authuser=0\u0026pid=25\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=en-GB\u0026ts=35",0,0,"",0,0,null,0,0],0,0,0],[300000,"/u/0","/u/0/_/gog/get","AN7pSW3AzD64S0As8m_EzEEeX1mgGa-L-ZDh4PrdbMm0zQrHFvbWEF-XTqE7Ftsz6De5Jh44Y7-K3Fkk76FRW_95CJOoJm6gpQ","https",0,"aa.google.com","rt=j\u0026sourceid=25","","bdYMP4s0T0yxL9DPyJyONQ",null,0,1,null,1,null,1,0,"https://waa-pa.clients6.google.com","AIzaSyBGb5fGAyC-pRcRU6MUHb__b_vKha71HRE","BGzusj5ImLnUrCMhNtL0",null,0],[["mousedown","touchstart","touchmove","wheel","keydown"],300000]]],};this.gbar_=this.gbar_||{};(function(_){var window=this;

try{

/*


 Copyright The Closure Library Authors.

 SPDX-License-Identifier: Apache-2.0

*/

var ka,ya,za,Aa,Ba,Ha,Ja,Ia,La,Ma,Pa,Ta,Qa,Wa,Xa,bb,cb,db,eb,fb,gb,ib,jb,nb,ob;_.aa=function(a,b){if(Error.captureStackTrace)Error.captureStackTrace(this,_.aa);else{var c=Error().stack;c&&(this.stack=c)}a&&(this.message=String(a));void 0!==b&&(this.cause=b)};_.ba=function(){var a=_.n.navigator;return a&&(a=a.userAgent)?a:""};_.p=function(a){return-1!=_.ba().indexOf(a)};_.ca=function(){return _.p("Opera")};_.da=function(){return _.p("Trident")||_.p("MSIE")};_.fa=function(){return _.p("Firefox")||_.p("FxiOS")};

_.ia=function(){return _.p("Safari")&&!(_.ha()||_.p("Coast")||_.ca()||_.p("Edge")||_.p("Edg/")||_.p("OPR")||_.fa()||_.p("Silk")||_.p("Android"))};_.ha=function(){return(_.p("Chrome")||_.p("CriOS"))&&!_.p("Edge")||_.p("Silk")};_.ja=function(){return _.p("Android")&&!(_.ha()||_.fa()||_.ca()||_.p("Silk"))};ka=function(){return _.p("iPhone")&&!_.p("iPod")&&!_.p("iPad")};_.la=function(){return ka()||_.p("iPad")||_.p("iPod")};

_.ma=function(a){var b=a.length;if(0<b){for(var c=Array(b),d=0;d<b;d++)c[d]=a[d];return c}return[]};_.na=function(){return-1!=_.ba().toLowerCase().indexOf("webkit")&&!_.p("Edge")};_.pa=function(a){return oa&&null!=a&&a instanceof Uint8Array};_.ra=function(a,b){if(_.qa)return a[_.qa]|=b;if(void 0!==a.Rb)return a.Rb|=b;Object.defineProperties(a,{Rb:{value:b,configurable:!0,writable:!0,enumerable:!1}});return b};

_.ua=function(a,b){var c=_.sa(a);(c&b)!==b&&(Object.isFrozen(a)&&(a=Array.prototype.slice.call(a)),_.ta(a,c|b));return a};_.sa=function(a){var b;_.qa?b=a[_.qa]:b=a.Rb;return null==b?0:b};_.ta=function(a,b){_.qa?a[_.qa]=b:void 0!==a.Rb?a.Rb=b:Object.defineProperties(a,{Rb:{value:b,configurable:!0,writable:!0,enumerable:!1}})};_.va=function(a){_.ra(a,1);return a};_.wa=function(a){return!!(_.sa(a)&2)};_.xa=function(a){_.ra(a,16);return a};ya=function(a,b){_.ta(b,(a|0)&-51)};

za=function(a,b){_.ta(b,(a|18)&-41)};Aa=function(a){return null!==a&&"object"===typeof a&&!Array.isArray(a)&&a.constructor===Object};Ba=function(a){var b=a.length;(b=b?a[b-1]:void 0)&&Aa(b)?b.g=1:(b={},a.push((b.g=1,b)))};_.Ca=function(a,b){return null==a?b:a};_.Ea=function(a,b){Da=b;a=new a(b);Da=void 0;return a};

Ha=function(a){switch(typeof a){case "number":return isFinite(a)?a:String(a);case "object":if(a)if(Array.isArray(a)){if(0!==(_.sa(a)&128))return a=Array.prototype.slice.call(a),Ba(a),a}else{if(_.pa(a))return _.Fa(a);if(a instanceof _.Ga){var b=a.Ba;return null==b?"":"string"===typeof b?b:a.Ba=_.Fa(b)}}}return a};Ja=function(a,b,c,d){if(null!=a){if(Array.isArray(a))a=Ia(a,b,c,void 0!==d);else if(Aa(a)){var e={},f;for(f in a)e[f]=Ja(a[f],b,c,d);a=e}else a=b(a,d);return a}};

Ia=function(a,b,c,d){var e=_.sa(a);d=d?!!(e&16):void 0;a=Array.prototype.slice.call(a);for(var f=0;f<a.length;f++)a[f]=Ja(a[f],b,c,d);c(e,a);return a};La=function(a){return a.Ye===Ka?a.toJSON():Ha(a)};Ma=function(a,b){a&128&&Ba(b)};

Pa=function(a,b,c){c=void 0===c?za:c;if(null!=a){if(oa&&a instanceof Uint8Array)return a.length?new _.Ga(new Uint8Array(a),_.Na):_.Oa();if(Array.isArray(a)){var d=_.sa(a);if(d&2)return a;if(b&&!(d&32)&&(d&16||0===d))return _.ta(a,d|2),a;a=Ia(a,Pa,d&4?za:c,!0);b=_.sa(a);b&4&&b&2&&Object.freeze(a);return a}return a.Ye===Ka?Qa(a):a}};Ta=function(a,b,c,d,e,f,g){(a=a.j&&a.j[c])?(d=_.sa(a),d&2?d=a:(f=_.Ra(a,Qa),za(d,f),Object.freeze(f),d=f),_.Sa(b,c,d,e)):_.r(b,c,Pa(d,f,g),e)};

Qa=function(a){if(_.wa(a.ya))return a;a=_.Ua(a,!0);_.ra(a.ya,2);return a};_.Ua=function(a,b){var c=a.ya,d=_.xa([]),e=a.constructor.j;e&&d.push(e);e=a.Gb;if(e){d.length=c.length;d.fill(void 0,d.length,c.length);var f={};d[d.length-1]=f}0!==(_.sa(c)&128)&&Ba(d);b=b||a.jc()?za:ya;d=_.Ea(a.constructor,d);a.Bd&&(d.Bd=a.Bd.slice());for(var g=!!(_.sa(c)&16),h=e?c.length-1:c.length,l=0;l<h;l++)Ta(a,d,l-a.Ec,c[l],!1,g,b);if(e)for(var m in e)c=e[m],h=+m,Number.isNaN(h)?f[h]=c:Ta(a,d,h,c,!0,g,b);return d};

_.Va=function(a){if(!_.wa(a.ya))return a;var b=_.Ua(a,!1);b.A=a;return b};Wa=function(a,b){if(Array.isArray(a)){var c=_.sa(a),d=1;!b||c&2||(d|=16);(c&d)!==d&&_.ta(a,c|d)}};Xa=function(a,b){return Ha(b)};_.t=function(a,b){return null!=a?!!a:!!b};_.u=function(a,b){void 0==b&&(b="");return null!=a?a:b};_.Ya=function(a,b){void 0==b&&(b=0);return null!=a?a:b};_.Za=function(a,b,c){for(var d in a)b.call(c,a[d],d,a)};

_.ab=function(a,b){for(var c,d,e=1;e<arguments.length;e++){d=arguments[e];for(c in d)a[c]=d[c];for(var f=0;f<$a.length;f++)c=$a[f],Object.prototype.hasOwnProperty.call(d,c)&&(a[c]=d[c])}};bb=function(a){var b=0;return function(){return b<a.length?{done:!1,value:a[b++]}:{done:!0}}};cb="function"==typeof Object.defineProperties?Object.defineProperty:function(a,b,c){if(a==Array.prototype||a==Object.prototype)return a;a[b]=c.value;return a};

db=function(a){a=["object"==typeof globalThis&&globalThis,a,"object"==typeof window&&window,"object"==typeof self&&self,"object"==typeof global&&global];for(var b=0;b<a.length;++b){var c=a[b];if(c&&c.Math==Math)return c}throw Error("a");};eb=db(this);fb=function(a,b){if(b)a:{var c=eb;a=a.split(".");for(var d=0;d<a.length-1;d++){var e=a[d];if(!(e in c))break a;c=c[e]}a=a[a.length-1];d=c[a];b=b(d);b!=d&&null!=b&&cb(c,a,{configurable:!0,writable:!0,value:b})}};

fb("Symbol",function(a){if(a)return a;var b=function(f,g){this.j=f;cb(this,"description",{configurable:!0,writable:!0,value:g})};b.prototype.toString=function(){return this.j};var c="jscomp_symbol_"+(1E9*Math.random()>>>0)+"_",d=0,e=function(f){if(this instanceof e)throw new TypeError("b");return new b(c+(f||"")+"_"+d++,f)};return e});

fb("Symbol.iterator",function(a){if(a)return a;a=Symbol("c");for(var b="Array Int8Array Uint8Array Uint8ClampedArray Int16Array Uint16Array Int32Array Uint32Array Float32Array Float64Array".split(" "),c=0;c<b.length;c++){var d=eb[b[c]];"function"===typeof d&&"function"!=typeof d.prototype[a]&&cb(d.prototype,a,{configurable:!0,writable:!0,value:function(){return gb(bb(this))}})}return a});gb=function(a){a={next:a};a[Symbol.iterator]=function(){return this};return a};

_.hb=function(a){var b="undefined"!=typeof Symbol&&Symbol.iterator&&a[Symbol.iterator];return b?b.call(a):{next:bb(a)}};ib="function"==typeof Object.create?Object.create:function(a){var b=function(){};b.prototype=a;return new b};if("function"==typeof Object.setPrototypeOf)jb=Object.setPrototypeOf;else{var kb;a:{var lb={a:!0},mb={};try{mb.__proto__=lb;kb=mb.a;break a}catch(a){}kb=!1}jb=kb?function(a,b){a.__proto__=b;if(a.__proto__!==b)throw new TypeError("d`"+a);return a}:null}nb=jb;

_.v=function(a,b){a.prototype=ib(b.prototype);a.prototype.constructor=a;if(nb)nb(a,b);else for(var c in b)if("prototype"!=c)if(Object.defineProperties){var d=Object.getOwnPropertyDescriptor(b,c);d&&Object.defineProperty(a,c,d)}else a[c]=b[c];a.Y=b.prototype};ob=function(a,b,c){if(null==a)throw new TypeError("e`"+c);if(b instanceof RegExp)throw new TypeError("f`"+c);return a+""};

fb("String.prototype.startsWith",function(a){return a?a:function(b,c){var d=ob(this,b,"startsWith"),e=d.length,f=b.length;c=Math.max(0,Math.min(c|0,d.length));for(var g=0;g<f&&c<e;)if(d[c++]!=b[g++])return!1;return g>=f}});fb("Array.prototype.find",function(a){return a?a:function(b,c){a:{var d=this;d instanceof String&&(d=String(d));for(var e=d.length,f=0;f<e;f++){var g=d[f];if(b.call(c,g,f,d)){b=g;break a}}b=void 0}return b}});var pb=function(a,b){return Object.prototype.hasOwnProperty.call(a,b)};

fb("WeakMap",function(a){function b(){}function c(l){var m=typeof l;return"object"===m&&null!==l||"function"===m}function d(l){if(!pb(l,f)){var m=new b;cb(l,f,{value:m})}}function e(l){var m=Object[l];m&&(Object[l]=function(q){if(q instanceof b)return q;Object.isExtensible(q)&&d(q);return m(q)})}if(function(){if(!a||!Object.seal)return!1;try{var l=Object.seal({}),m=Object.seal({}),q=new a([[l,2],[m,3]]);if(2!=q.get(l)||3!=q.get(m))return!1;q.delete(l);q.set(m,4);return!q.has(l)&&4==q.get(m)}catch(w){return!1}}())return a;

var f="$jscomp_hidden_"+Math.random();e("freeze");e("preventExtensions");e("seal");var g=0,h=function(l){this.j=(g+=Math.random()+1).toString();if(l){l=_.hb(l);for(var m;!(m=l.next()).done;)m=m.value,this.set(m[0],m[1])}};h.prototype.set=function(l,m){if(!c(l))throw Error("g");d(l);if(!pb(l,f))throw Error("h`"+l);l[f][this.j]=m;return this};h.prototype.get=function(l){return c(l)&&pb(l,f)?l[f][this.j]:void 0};h.prototype.has=function(l){return c(l)&&pb(l,f)&&pb(l[f],this.j)};h.prototype.delete=function(l){return c(l)&&

pb(l,f)&&pb(l[f],this.j)?delete l[f][this.j]:!1};return h});

fb("Map",function(a){if(function(){if(!a||"function"!=typeof a||!a.prototype.entries||"function"!=typeof Object.seal)return!1;try{var h=Object.seal({x:4}),l=new a(_.hb([[h,"s"]]));if("s"!=l.get(h)||1!=l.size||l.get({x:4})||l.set({x:4},"t")!=l||2!=l.size)return!1;var m=l.entries(),q=m.next();if(q.done||q.value[0]!=h||"s"!=q.value[1])return!1;q=m.next();return q.done||4!=q.value[0].x||"t"!=q.value[1]||!m.next().done?!1:!0}catch(w){return!1}}())return a;var b=new WeakMap,c=function(h){this.o={};this.j=

f();this.size=0;if(h){h=_.hb(h);for(var l;!(l=h.next()).done;)l=l.value,this.set(l[0],l[1])}};c.prototype.set=function(h,l){h=0===h?0:h;var m=d(this,h);m.list||(m.list=this.o[m.id]=[]);m.Ua?m.Ua.value=l:(m.Ua={next:this.j,lc:this.j.lc,head:this.j,key:h,value:l},m.list.push(m.Ua),this.j.lc.next=m.Ua,this.j.lc=m.Ua,this.size++);return this};c.prototype.delete=function(h){h=d(this,h);return h.Ua&&h.list?(h.list.splice(h.index,1),h.list.length||delete this.o[h.id],h.Ua.lc.next=h.Ua.next,h.Ua.next.lc=

h.Ua.lc,h.Ua.head=null,this.size--,!0):!1};c.prototype.clear=function(){this.o={};this.j=this.j.lc=f();this.size=0};c.prototype.has=function(h){return!!d(this,h).Ua};c.prototype.get=function(h){return(h=d(this,h).Ua)&&h.value};c.prototype.entries=function(){return e(this,function(h){return[h.key,h.value]})};c.prototype.keys=function(){return e(this,function(h){return h.key})};c.prototype.values=function(){return e(this,function(h){return h.value})};c.prototype.forEach=function(h,l){for(var m=this.entries(),

q;!(q=m.next()).done;)q=q.value,h.call(l,q[1],q[0],this)};c.prototype[Symbol.iterator]=c.prototype.entries;var d=function(h,l){var m=l&&typeof l;"object"==m||"function"==m?b.has(l)?m=b.get(l):(m=""+ ++g,b.set(l,m)):m="p_"+l;var q=h.o[m];if(q&&pb(h.o,m))for(h=0;h<q.length;h++){var w=q[h];if(l!==l&&w.key!==w.key||l===w.key)return{id:m,list:q,index:h,Ua:w}}return{id:m,list:q,index:-1,Ua:void 0}},e=function(h,l){var m=h.j;return gb(function(){if(m){for(;m.head!=h.j;)m=m.lc;for(;m.next!=m.head;)return m=

m.next,{done:!1,value:l(m)};m=null}return{done:!0,value:void 0}})},f=function(){var h={};return h.lc=h.next=h.head=h},g=0;return c});fb("Number.MAX_SAFE_INTEGER",function(){return 9007199254740991});fb("Number.isNaN",function(a){return a?a:function(b){return"number"===typeof b&&isNaN(b)}});

var qb=function(a,b){a instanceof String&&(a+="");var c=0,d=!1,e={next:function(){if(!d&&c<a.length){var f=c++;return{value:b(f,a[f]),done:!1}}d=!0;return{done:!0,value:void 0}}};e[Symbol.iterator]=function(){return e};return e};fb("Array.prototype.entries",function(a){return a?a:function(){return qb(this,function(b,c){return[b,c]})}});

fb("Array.from",function(a){return a?a:function(b,c,d){c=null!=c?c:function(h){return h};var e=[],f="undefined"!=typeof Symbol&&Symbol.iterator&&b[Symbol.iterator];if("function"==typeof f){b=f.call(b);for(var g=0;!(f=b.next()).done;)e.push(c.call(d,f.value,g++))}else for(f=b.length,g=0;g<f;g++)e.push(c.call(d,b[g],g));return e}});fb("Array.prototype.keys",function(a){return a?a:function(){return qb(this,function(b){return b})}});

fb("Array.prototype.values",function(a){return a?a:function(){return qb(this,function(b,c){return c})}});fb("Array.prototype.fill",function(a){return a?a:function(b,c,d){var e=this.length||0;0>c&&(c=Math.max(0,e+c));if(null==d||d>e)d=e;d=Number(d);0>d&&(d=Math.max(0,e+d));for(c=Number(c||0);c<d;c++)this[c]=b;return this}});var rb=function(a){return a?a:Array.prototype.fill};fb("Int8Array.prototype.fill",rb);fb("Uint8Array.prototype.fill",rb);fb("Uint8ClampedArray.prototype.fill",rb);

fb("Int16Array.prototype.fill",rb);fb("Uint16Array.prototype.fill",rb);fb("Int32Array.prototype.fill",rb);fb("Uint32Array.prototype.fill",rb);fb("Float32Array.prototype.fill",rb);fb("Float64Array.prototype.fill",rb);var sb="function"==typeof Object.assign?Object.assign:function(a,b){for(var c=1;c<arguments.length;c++){var d=arguments[c];if(d)for(var e in d)pb(d,e)&&(a[e]=d[e])}return a};fb("Object.assign",function(a){return a||sb});

fb("Object.entries",function(a){return a?a:function(b){var c=[],d;for(d in b)pb(b,d)&&c.push([d,b[d]]);return c}});fb("Object.is",function(a){return a?a:function(b,c){return b===c?0!==b||1/b===1/c:b!==b&&c!==c}});fb("Array.prototype.includes",function(a){return a?a:function(b,c){var d=this;d instanceof String&&(d=String(d));var e=d.length;c=c||0;for(0>c&&(c=Math.max(c+e,0));c<e;c++){var f=d[c];if(f===b||Object.is(f,b))return!0}return!1}});

fb("String.prototype.includes",function(a){return a?a:function(b,c){return-1!==ob(this,b,"includes").indexOf(b,c||0)}});var wb,xb,yb;_.tb=_.tb||{};_.n=this||self;_.ub=function(a){var b=typeof a;return"object"==b&&null!=a||"function"==b};_.vb="closure_uid_"+(1E9*Math.random()>>>0);wb=function(a,b,c){return a.call.apply(a.bind,arguments)};xb=function(a,b,c){if(!a)throw Error();if(2<arguments.length){var d=Array.prototype.slice.call(arguments,2);return function(){var e=Array.prototype.slice.call(arguments);Array.prototype.unshift.apply(e,d);return a.apply(b,e)}}return function(){return a.apply(b,arguments)}};

_.z=function(a,b,c){Function.prototype.bind&&-1!=Function.prototype.bind.toString().indexOf("native code")?_.z=wb:_.z=xb;return _.z.apply(null,arguments)};_.A=function(a,b){a=a.split(".");var c=_.n;a[0]in c||"undefined"==typeof c.execScript||c.execScript("var "+a[0]);for(var d;a.length&&(d=a.shift());)a.length||void 0===b?c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}:c[d]=b};

_.B=function(a,b){function c(){}c.prototype=b.prototype;a.Y=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.Qk=function(d,e,f){for(var g=Array(arguments.length-2),h=2;h<arguments.length;h++)g[h-2]=arguments[h];return b.prototype[e].apply(d,g)}};yb=function(a){return a};_.zb=function(a){var b=null,c=_.n.trustedTypes;if(!c||!c.createPolicy)return b;try{b=c.createPolicy(a,{createHTML:yb,createScript:yb,createScriptURL:yb})}catch(d){_.n.console&&_.n.console.error(d.message)}return b};_.B(_.aa,Error);_.aa.prototype.name="CustomError";_.Ab=String.prototype.trim?function(a){return a.trim()}:function(a){return/^[\s\xa0]*([\s\S]*?)[\s\xa0]*$/.exec(a)[1]};_.Bb=Array.prototype.indexOf?function(a,b){return Array.prototype.indexOf.call(a,b,void 0)}:function(a,b){if("string"===typeof a)return"string"!==typeof b||1!=b.length?-1:a.indexOf(b,0);for(var c=0;c<a.length;c++)if(c in a&&a[c]===b)return c;return-1};_.Cb=Array.prototype.forEach?function(a,b,c){Array.prototype.forEach.call(a,b,c)}:function(a,b,c){for(var d=a.length,e="string"===typeof a?a.split(""):a,f=0;f<d;f++)f in e&&b.call(c,e[f],f,a)};

_.Db=Array.prototype.filter?function(a,b,c){return Array.prototype.filter.call(a,b,c)}:function(a,b,c){for(var d=a.length,e=[],f=0,g="string"===typeof a?a.split(""):a,h=0;h<d;h++)if(h in g){var l=g[h];b.call(c,l,h,a)&&(e[f++]=l)}return e};_.Ra=Array.prototype.map?function(a,b,c){return Array.prototype.map.call(a,b,c)}:function(a,b,c){for(var d=a.length,e=Array(d),f="string"===typeof a?a.split(""):a,g=0;g<d;g++)g in f&&(e[g]=b.call(c,f[g],g,a));return e};

_.Eb=Array.prototype.reduce?function(a,b,c){return Array.prototype.reduce.call(a,b,c)}:function(a,b,c){var d=c;(0,_.Cb)(a,function(e,f){d=b.call(void 0,d,e,f,a)});return d};_.Fb=Array.prototype.some?function(a,b){return Array.prototype.some.call(a,b,void 0)}:function(a,b){for(var c=a.length,d="string"===typeof a?a.split(""):a,e=0;e<c;e++)if(e in d&&b.call(void 0,d[e],e,a))return!0;return!1};_.Gb=function(a){_.Gb[" "](a);return a};_.Gb[" "]=function(){};var Ub,Vb,$b;_.Hb=_.ca();_.C=_.da();_.Ib=_.p("Edge");_.Jb=_.Ib||_.C;_.Kb=_.p("Gecko")&&!_.na()&&!(_.p("Trident")||_.p("MSIE"))&&!_.p("Edge");_.Lb=_.na();_.Mb=_.p("Macintosh");_.Nb=_.p("Windows");_.Ob=_.p("Linux")||_.p("CrOS");_.Pb=_.p("Android");_.Qb=ka();_.Rb=_.p("iPad");_.Sb=_.p("iPod");_.Tb=_.la();Ub=function(){var a=_.n.document;return a?a.documentMode:void 0};

a:{var Wb="",Xb=function(){var a=_.ba();if(_.Kb)return/rv:([^\);]+)(\)|;)/.exec(a);if(_.Ib)return/Edge\/([\d\.]+)/.exec(a);if(_.C)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a);if(_.Lb)return/WebKit\/(\S+)/.exec(a);if(_.Hb)return/(?:Version)[ \/]?(\S+)/.exec(a)}();Xb&&(Wb=Xb?Xb[1]:"");if(_.C){var Yb=Ub();if(null!=Yb&&Yb>parseFloat(Wb)){Vb=String(Yb);break a}}Vb=Wb}_.Zb=Vb;if(_.n.document&&_.C){var ac=Ub();$b=ac?ac:parseInt(_.Zb,10)||void 0}else $b=void 0;_.bc=$b;_.cc=_.fa();_.dc=ka()||_.p("iPod");_.ec=_.p("iPad");_.fc=_.ja();_.gc=_.ha();_.hc=_.ia()&&!_.la();var ic;ic={};_.jc=null;_.Fa=function(a,b){void 0===b&&(b=0);_.kc();b=ic[b];for(var c=Array(Math.floor(a.length/3)),d=b[64]||"",e=0,f=0;e<a.length-2;e+=3){var g=a[e],h=a[e+1],l=a[e+2],m=b[g>>2];g=b[(g&3)<<4|h>>4];h=b[(h&15)<<2|l>>6];l=b[l&63];c[f++]=m+g+h+l}m=0;l=d;switch(a.length-e){case 2:m=a[e+1],l=b[(m&15)<<2]||d;case 1:a=a[e],c[f]=b[a>>2]+b[(a&3)<<4|m>>4]+l+d}return c.join("")};

_.kc=function(){if(!_.jc){_.jc={};for(var a="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789".split(""),b=["+/=","+/","-_=","-_.","-_"],c=0;5>c;c++){var d=a.concat(b[c].split(""));ic[c]=d;for(var e=0;e<d.length;e++){var f=d[e];void 0===_.jc[f]&&(_.jc[f]=e)}}}};var oa;oa="undefined"!==typeof Uint8Array;_.Na={};_.lc="function"===typeof Uint8Array.prototype.slice;_.mc="undefined"!==typeof TextDecoder;_.nc="undefined"!==typeof TextEncoder;var oc;_.Ga=function(a,b){if(b!==_.Na)throw Error("u");this.Ba=a;if(null!=a&&0===a.length)throw Error("v");};_.Oa=function(){return oc||(oc=new _.Ga(null,_.Na))};_.Ga.prototype.hc=function(){return null==this.Ba};_.qa="function"===typeof Symbol&&"symbol"===typeof Symbol()?Symbol():void 0;var Ka,pc,rc;Ka={};rc=[];_.ta(rc,23);_.qc=Object.freeze(rc);_.sc=function(a){if(_.wa(a.ya))throw Error("x");};var tc;tc=function(a){var b=a.o+a.Ec;return a.Gb||(a.Gb=a.ya[b]={})};_.D=function(a,b,c){return-1===b?null:b>=a.o?a.Gb?a.Gb[b]:void 0:c&&a.Gb&&(c=a.Gb[b],null!=c)?c:a.ya[b+a.Ec]};_.r=function(a,b,c,d){_.sc(a);return _.uc(a,b,c,d)};_.uc=function(a,b,c,d){a.A&&(a.A=void 0);if(b>=a.o||d)return tc(a)[b]=c,a;a.ya[b+a.Ec]=c;(c=a.Gb)&&b in c&&delete c[b];return a};_.E=function(a,b){a=_.D(a,b);return null==a?a:!!a};

_.vc=function(a,b,c,d){var e=_.D(a,c,d);var f=!1;var g=null==e||"object"!==typeof e||(f=Array.isArray(e))||e.Ye!==Ka?f?new b(e):void 0:e;g!==e&&null!=g&&(_.uc(a,c,g,d),_.ra(g.ya,_.sa(a.ya)&18));return g};_.F=function(a,b,c,d){d=void 0===d?!1:d;b=_.vc(a,b,c,d);if(null==b)return b;if(!_.wa(a.ya)){var e=_.Va(b);e!==b&&(b=e,_.uc(a,c,b,d))}return b};_.wc=function(a,b,c){_.sc(a);null==c&&(c=void 0);return _.uc(a,b,c)};

_.Sa=function(a,b,c,d){_.sc(a);var e=null==c?_.qc:_.va([]);if(null!=c){for(var f=!!c.length,g=0;g<c.length;g++){var h=c[g];f=f&&!_.wa(h.ya);e[g]=h.ya}e=_.ua(e,(f?8:0)|1);a.j||(a.j={});a.j[b]=c}else a.j&&(a.j[b]=void 0);return _.uc(a,b,e,d)};_.xc=function(a,b,c){a=_.D(a,b);return null==a?void 0===c?0:c:a};_.yc=function(a,b,c){c=void 0===c?0:c;var d=_.D(a,b);var e=null==d?d:"number"===typeof d||"NaN"===d||"Infinity"===d||"-Infinity"===d?Number(d):void 0;null!=e&&e!==d&&_.uc(a,b,e);return _.Ca(e,c)};var Da;_.G=function(a,b,c){null==a&&(a=Da);Da=void 0;var d=this.constructor.o||0,e=0<d,f=this.constructor.j,g=!1;if(null==a){a=f?[f]:[];var h=48;var l=!0;e&&(d=0,h|=128);_.ta(a,h)}else{if(!Array.isArray(a))throw Error();if(f&&f!==a[0])throw Error();var m=h=_.ra(a,0);if(l=0!==(16&m))(g=0!==(32&m))||(m|=32);if(e)if(128&m)d=0;else{if(0<a.length){var q=a[a.length-1];if(Aa(q)&&"g"in q){d=0;m|=128;delete q.g;var w=!0,y;for(y in q){w=!1;break}w&&a.pop()}}}else if(128&m)throw Error();h!==m&&_.ta(a,m)}this.Ec=(f?

0:-1)-d;this.j=void 0;this.ya=a;a:{f=this.ya.length;d=f-1;if(f&&(f=this.ya[d],Aa(f))){this.Gb=f;this.o=d-this.Ec;break a}void 0!==b&&-1<b?(this.o=Math.max(b,d+1-this.Ec),this.Gb=void 0):this.o=Number.MAX_VALUE}if(!e&&this.Gb&&"g"in this.Gb)throw Error("C");if(c){b=l&&!g&&!0;e=this.o;var x;for(l=0;l<c.length;l++)g=c[l],g<e?(g+=this.Ec,(d=a[g])?Wa(d,b):a[g]=_.qc):(x||(x=tc(this)),(d=x[g])?Wa(d,b):x[g]=_.qc)}};_.k=_.G.prototype;_.k.toJSON=function(){var a=this.ya;return pc?a:Ia(a,La,Ma)};

_.k.Ea=function(){pc=!0;try{return JSON.stringify(this.toJSON(),Xa)}finally{pc=!1}};_.k.jc=function(){return _.wa(this.ya)};_.k.Ye=Ka;_.k.toString=function(){return this.ya.toString()};_.zc=Symbol();_.Ac=Symbol();_.Bc=Symbol();_.Cc=Symbol();var Dc=function(a){_.G.call(this,a)};_.v(Dc,_.G);_.Ec=function(a){_.G.call(this,a)};_.v(_.Ec,_.G);_.Ec.prototype.Zc=function(a){return _.r(this,3,a)};_.Fc=function(a){_.G.call(this,a)};_.v(_.Fc,_.G);var Gc=function(a){_.G.call(this,a)};_.v(Gc,_.G);_.Hc=function(a){_.G.call(this,a)};_.v(_.Hc,_.G);_.Hc.prototype.hd=function(a){return _.r(this,24,a)};_.Ic=function(a){_.G.call(this,a)};_.v(_.Ic,_.G);_.H=function(){this.Fb=this.Fb;this.Ma=this.Ma};_.H.prototype.Fb=!1;_.H.prototype.isDisposed=function(){return this.Fb};_.H.prototype.ta=function(){this.Fb||(this.Fb=!0,this.R())};_.H.prototype.R=function(){if(this.Ma)for(;this.Ma.length;)this.Ma.shift()()};var Jc=function(a){_.H.call(this);this.A=a;this.j=[];this.o={}};_.v(Jc,_.H);Jc.prototype.resolve=function(a){var b=this.A;a=a.split(".");for(var c=a.length,d=0;d<c;++d)if(b[a[d]])b=b[a[d]];else return null;return b instanceof Function?b:null};Jc.prototype.vd=function(){for(var a=this.j.length,b=this.j,c=[],d=0;d<a;++d){var e=b[d].j(),f=this.resolve(e);if(f&&f!=this.o[e])try{b[d].vd(f)}catch(g){}else c.push(b[d])}this.j=c.concat(b.slice(a))};var Kc=function(a){_.H.call(this);this.A=a;this.C=this.j=null;this.B=0;this.D={};this.o=!1;a=window.navigator.userAgent;0<=a.indexOf("MSIE")&&0<=a.indexOf("Trident")&&(a=/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a))&&a[1]&&9>parseFloat(a[1])&&(this.o=!0)};_.v(Kc,_.H);Kc.prototype.F=function(a,b){this.j=b;this.C=a;b.preventDefault?b.preventDefault():b.returnValue=!1};_.Lc=function(a){_.G.call(this,a)};_.v(_.Lc,_.G);_.Mc=function(a){_.G.call(this,a)};_.v(_.Mc,_.G);_.Nc=function(){this.data={}};_.Nc.prototype.j=function(){window.console&&window.console.log&&window.console.log("Log data: ",this.data)};_.Nc.prototype.Ea=function(a){var b=[],c;for(c in this.data)b.push(encodeURIComponent(c)+"="+encodeURIComponent(String(this.data[c])));return("atyp=i&zx="+(new Date).getTime()+"&"+b.join("&")).substr(0,a)};var Oc=function(a,b){this.data={};var c=_.F(a,Gc,8)||new Gc;window.google&&window.google.kEI&&(this.data.ei=window.google.kEI);this.data.sei=_.u(_.D(a,10));this.data.ogf=_.u(_.D(c,3));this.data.ogrp=(window.google&&window.google.sn?!/.*hp$/.test(window.google.sn):_.t(_.E(a,7)))?"1":"";this.data.ogv=_.u(_.D(c,6))+"."+_.u(_.D(c,7));this.data.ogd=_.u(_.D(a,21));this.data.ogc=_.u(_.D(a,20));this.data.ogl=_.u(_.D(a,5));b&&(this.data.oggv=b)};_.v(Oc,_.Nc);var $a="constructor hasOwnProperty isPrototypeOf propertyIsEnumerable toLocaleString toString valueOf".split(" ");_.Pc=function(a,b,c,d,e){Oc.call(this,a,b);_.ab(this.data,{jexpid:_.u(_.D(a,9)),srcpg:"prop="+_.u(_.D(a,6)),jsr:Math.round(1/d),emsg:c.name+":"+c.message});if(e){e._sn&&(e._sn="og."+e._sn);for(var f in e)this.data[encodeURIComponent(f)]=e[f]}};_.v(_.Pc,Oc);var Qc;_.Rc=function(){void 0===Qc&&(Qc=_.zb("ogb-qtm#html"));return Qc};_.Uc=function(a,b){this.j=a===_.Sc&&b||"";this.o=_.Tc};_.Uc.prototype.Qb=!0;_.Uc.prototype.vb=function(){return this.j};_.Tc={};_.Sc={};_.Wc=function(a,b){this.j=b===_.Vc?a:""};_.Wc.prototype.toString=function(){return this.j+""};_.Wc.prototype.Qb=!0;_.Wc.prototype.vb=function(){return this.j.toString()};_.Yc=function(a){return _.Xc(a).toString()};_.Xc=function(a){return a instanceof _.Wc&&a.constructor===_.Wc?a.j:"type_error:TrustedResourceUrl"};_.Vc={};var bd,cd,Zc;_.$c=function(a,b){this.j=b===Zc?a:""};_.$c.prototype.toString=function(){return this.j.toString()};_.$c.prototype.Qb=!0;_.$c.prototype.vb=function(){return this.j.toString()};_.ad=function(a){return a instanceof _.$c&&a.constructor===_.$c?a.j:"type_error:SafeUrl"};bd=/^data:(.*);base64,[a-z0-9+\/]+=*$/i;cd=/^(?:(?:https?|mailto|ftp):|[^:/?#]*(?:[/?#]|$))/i;

_.ed=function(a){if(a instanceof _.$c)return a;a="object"==typeof a&&a.Qb?a.vb():String(a);cd.test(a)?a=_.dd(a):(a=String(a).replace(/(%0A|%0D)/g,""),a=a.match(bd)?_.dd(a):null);return a};_.fd=function(a){if(a instanceof _.$c)return a;a="object"==typeof a&&a.Qb?a.vb():String(a);cd.test(a)||(a="about:invalid#zClosurez");return _.dd(a)};Zc={};_.dd=function(a){return new _.$c(a,Zc)};_.gd=_.dd("about:invalid#zClosurez");_.hd={};_.id=function(a,b){this.j=b===_.hd?a:"";this.Qb=!0};_.id.prototype.vb=function(){return this.j};_.id.prototype.toString=function(){return this.j.toString()};_.kd=new _.id("",_.hd);_.ld=RegExp("^[-+,.\"'%_!#/ a-zA-Z0-9\\[\\]]+$");_.md=RegExp("\\b(url\\([ \t\n]*)('[ -&(-\\[\\]-~]*'|\"[ !#-\\[\\]-~]*\"|[!#-&*-\\[\\]-~]*)([ \t\n]*\\))","g");

_.nd=RegExp("\\b(calc|cubic-bezier|fit-content|hsl|hsla|linear-gradient|matrix|minmax|radial-gradient|repeat|rgb|rgba|(rotate|scale|translate)(X|Y|Z|3d)?|steps|var)\\([-+*/0-9a-zA-Z.%#\\[\\], ]+\\)","g");var od;od={};_.pd=function(a,b){this.j=b===od?a:"";this.Qb=!0};_.pd.prototype.vb=function(){return this.j.toString()};_.pd.prototype.toString=function(){return this.j.toString()};_.qd=function(a){return a instanceof _.pd&&a.constructor===_.pd?a.j:"type_error:SafeHtml"};_.rd=function(a){var b=_.Rc();a=b?b.createHTML(a):a;return new _.pd(a,od)};_.sd=new _.pd(_.n.trustedTypes&&_.n.trustedTypes.emptyHTML||"",od);_.td=_.rd("<br>");var vd;_.ud=function(a){var b=!1,c;return function(){b||(c=a(),b=!0);return c}}(function(){var a=document.createElement("div"),b=document.createElement("div");b.appendChild(document.createElement("div"));a.appendChild(b);b=a.firstChild.firstChild;a.innerHTML=_.qd(_.sd);return!b.parentElement});vd=/^[\w+/_-]+[=]{0,2}$/;

_.wd=function(a){a=(a||_.n).document;return a.querySelector?(a=a.querySelector('style[nonce],link[rel="stylesheet"][nonce]'))&&(a=a.nonce||a.getAttribute("nonce"))&&vd.test(a)?a:"":""};_.xd=RegExp("^\\s{3,4}at(?: (?:(.*?)\\.)?((?:new )?(?:[a-zA-Z_$][\\w$]*|<anonymous>))(?: \\[as ([a-zA-Z_$][\\w$]*)\\])?)? (?:\\(unknown source\\)|\\(native\\)|\\((?:eval at )?((?:http|https|file)://[^\\s)]+|javascript:.*)\\)|((?:http|https|file)://[^\\s)]+|javascript:.*))$");_.yd=RegExp("^(?:(.*?)\\.)?([a-zA-Z_$][\\w$]*(?:/.?<)?)?(\\(.*\\))?@(?::0|((?:http|https|file)://[^\\s)]+|javascript:.*))$");var zd,Cd,Bd;_.Ad=function(a){var b=window.google&&window.google.logUrl?"":"https://www.google.com";b+="/gen_204?use_corp=on&";b+=a.Ea(2040-b.length);zd(_.ed(b)||_.gd)};zd=function(a){var b=new Image,c=Bd;b.onerror=b.onload=b.onabort=function(){c in Cd&&delete Cd[c]};Cd[Bd++]=b;b.src=_.ad(a)};Cd=[];Bd=0;_.Dd=function(a){_.G.call(this,a)};_.v(_.Dd,_.G);_.Ed=function(a){var b="Kc";if(a.Kc&&a.hasOwnProperty(b))return a.Kc;b=new a;return a.Kc=b};_.Fd=function(){this.j={};this.o={}};_.Hd=function(a,b){var c=_.Fd.j();if(a in c.j){if(c.j[a]!=b)throw new Gd(a);}else{c.j[a]=b;if(b=c.o[a])for(var d=0,e=b.length;d<e;d++)b[d].j(c.j,a);delete c.o[a]}};_.Jd=function(a,b){if(b in a.j)return a.j[b];throw new Id(b);};_.Fd.j=function(){return _.Ed(_.Fd)};var Kd=function(){_.aa.call(this)};_.v(Kd,_.aa);var Gd=function(){_.aa.call(this)};_.v(Gd,Kd);var Id=function(){_.aa.call(this)};_.v(Id,Kd);var Nd=function(){var a=Ld;this.C=Md;this.o=_.Ya(_.yc(a,2,.001),.001);this.D=_.t(_.E(a,1))&&Math.random()<this.o;this.F=_.Ya(_.xc(a,3,1),1);this.B=0;this.j=this.A=null};Nd.prototype.log=function(a,b){if(this.j){var c=new Dc;_.r(c,1,a.message);_.r(c,2,a.stack);_.r(c,3,a.lineNumber);_.r(c,5,1);var d=new _.Ec;_.wc(d,40,c);this.j.log(98,d)}try{if(this.D&&this.B<this.F){try{var e=(this.A||_.Jd(_.Fd.j(),"lm")).B(a,b)}catch(f){e=new _.Pc(this.C,"quantum:gapiBuildLabel",a,this.o,b)}_.Ad(e);this.B++}}catch(f){}};var Od=[1,2,3,4,5,6,9,10,11,13,14,28,29,30,34,35,37,38,39,40,42,43,48,49,50,51,52,53,62,500],Rd=function(a,b,c,d,e,f){Oc.call(this,a,b);_.ab(this.data,{oge:d,ogex:_.u(_.D(a,9)),ogp:_.u(_.D(a,6)),ogsr:Math.round(1/(Pd(d)?_.Ya(_.yc(c,3,1)):_.Ya(_.yc(c,2,1E-4)))),ogus:e});if(f){"ogw"in f&&(this.data.ogw=f.ogw,delete f.ogw);"ved"in f&&(this.data.ved=f.ved,delete f.ved);a=[];for(var g in f)0!=a.length&&a.push(","),a.push(Qd(g)),a.push("."),a.push(Qd(f[g]));f=a.join("");""!=f&&(this.data.ogad=f)}};

_.v(Rd,Oc);var Qd=function(a){a=String(a);return a.replace(".","%2E").replace(",","%2C")},Pd=function(a){if(!Td){Td={};for(var b=0;b<Od.length;b++)Td[Od[b]]=!0}return!!Td[a]},Td=null;var Ud=function(a){_.G.call(this,a)};_.v(Ud,_.G);var Yd=function(){var a=Vd,b=Wd,c=Xd;this.o=a;this.j=b;this.B=_.Ya(_.yc(a,2,1E-4),1E-4);this.D=_.Ya(_.yc(a,3,1),1);b=Math.random();this.A=_.t(_.E(a,1))&&b<this.B;this.C=_.t(_.E(a,1))&&b<this.D;a=0;_.t(_.E(c,1))&&(a|=1);_.t(_.E(c,2))&&(a|=2);_.t(_.E(c,3))&&(a|=4);this.F=a};Yd.prototype.log=function(a,b){try{if(Pd(a)?this.C:this.A){var c=new Rd(this.j,"quantum:gapiBuildLabel",this.o,a,this.F,b);_.Ad(c)}}catch(d){}};_.Zd=function(a){this.Ba=a;this.j=void 0;this.o=[]};_.Zd.prototype.then=function(a,b,c){this.o.push(new $d(a,b,c));ae(this)};_.Zd.prototype.resolve=function(a){if(void 0!==this.Ba||void 0!==this.j)throw Error("K");this.Ba=a;ae(this)};_.Zd.prototype.reject=function(a){if(void 0!==this.Ba||void 0!==this.j)throw Error("K");this.j=a;ae(this)};var ae=function(a){if(0<a.o.length){var b=void 0!==a.Ba,c=void 0!==a.j;if(b||c){b=b?a.A:a.B;c=a.o;a.o=[];try{_.Cb(c,b,a)}catch(d){console.error(d)}}}};

_.Zd.prototype.A=function(a){a.o&&a.o.call(a.j,this.Ba)};_.Zd.prototype.B=function(a){a.A&&a.A.call(a.j,this.j)};var $d=function(a,b,c){this.o=a;this.A=b;this.j=c};_.J=function(){this.B=new _.Zd;this.j=new _.Zd;this.G=new _.Zd;this.D=new _.Zd;this.F=new _.Zd;this.H=new _.Zd;this.C=new _.Zd;this.A=new _.Zd;this.o=new _.Zd;this.K=new _.Zd};_.k=_.J.prototype;_.k.di=function(){return this.B};_.k.oi=function(){return this.j};_.k.xi=function(){return this.G};_.k.ni=function(){return this.D};_.k.vi=function(){return this.F};_.k.ki=function(){return this.H};_.k.li=function(){return this.C};_.k.Vh=function(){return this.A};_.k.Uh=function(){return this.o};_.J.j=function(){return _.Ed(_.J)};var be=function(a){_.G.call(this,a)};_.v(be,_.G);_.de=function(){return _.F(_.ce,_.Hc,1)};_.ee=function(){return _.F(_.ce,_.Ic,5)};var fe;window.gbar_&&window.gbar_.CONFIG?fe=window.gbar_.CONFIG[0]||{}:fe=[];_.ce=new be(fe);var Ld,Md,Wd,Xd,Vd;Ld=_.F(_.ce,_.Dd,3)||new _.Dd;Md=_.de()||new _.Hc;_.K=new Nd;Wd=_.de()||new _.Hc;Xd=_.ee()||new _.Ic;Vd=_.F(_.ce,Ud,4)||new Ud;_.ge=new Yd;_.A("gbar_._DumpException",function(a){_.K?_.K.log(a):console.error(a)});_.he=new Kc(_.K);_.ge.log(8,{m:"BackCompat"==document.compatMode?"q":"s"});_.A("gbar.A",_.Zd);_.Zd.prototype.aa=_.Zd.prototype.then;_.A("gbar.B",_.J);_.J.prototype.ba=_.J.prototype.oi;_.J.prototype.bb=_.J.prototype.xi;_.J.prototype.bd=_.J.prototype.vi;_.J.prototype.bf=_.J.prototype.di;_.J.prototype.bg=_.J.prototype.ni;_.J.prototype.bh=_.J.prototype.ki;_.J.prototype.bi=_.J.prototype.li;_.J.prototype.bj=_.J.prototype.Vh;_.J.prototype.bk=_.J.prototype.Uh;_.A("gbar.a",_.J.j());var ie=new Jc(window);_.Hd("api",ie);

var je=_.ee()||new _.Ic;window.__PVT=_.u(_.D(je,8));_.Hd("eq",_.he);

}catch(e){_._DumpException(e)}

try{

var ke=function(a){_.G.call(this,a)};_.v(ke,_.G);var le=function(){_.H.call(this);this.o=[];this.j=[]};_.v(le,_.H);le.prototype.A=function(a,b){this.o.push({features:a,options:b})};le.prototype.init=function(a,b,c){window.gapi={};var d=window.___jsl={};d.h=_.u(_.D(a,1));null!=_.D(a,12,!1)&&(d.dpo=_.t(_.E(a,12)));d.ms=_.u(_.D(a,2));d.m=_.u(_.D(a,3));d.l=[];_.D(b,1)&&(a=_.D(b,3))&&this.j.push(a);_.D(c,1)&&(c=_.D(c,2))&&this.j.push(c);_.A("gapi.load",(0,_.z)(this.A,this));return this};var me=_.F(_.ce,_.Lc,14)||new _.Lc,ne=_.F(_.ce,_.Mc,9)||new _.Mc,oe=new ke,pe=new le;pe.init(me,ne,oe);_.Hd("gs",pe);

}catch(e){_._DumpException(e)}

})(this.gbar_);

// Google Inc.

</script><script nonce="bdYMP4s0T0yxL9DPyJyONQ">DOCS_timing['ojle']=new Date().getTime();</script><script src="chrome-extension://ghbmnnjooekpmoecnnnilnnbdlolhkhi/page_embed_script.js" nonce="bdYMP4s0T0yxL9DPyJyONQ"></script><script nonce="bdYMP4s0T0yxL9DPyJyONQ">_docs_flag_initialData={"docs-ails":"docs_warm","docs-fwds":"docs_nf","docs-crs":"docs_crs_unk","docs-l2t":0,"docs-shdn":104,"docs-tfh":"","info_params":{"token":"AC4w5Vj2Zf_Rs6bATQGoO3w5aZdxV2w8nA:1673676861963","includes_info_params":true},"docs-eohmo":false,"uls":"{\"langs\":[\"en_GB\"],\"itcs\":[\"en-t-k0-und\",\"en-t-i0-und\"],\"override\":\"\",\"selected\":\"en-t-k0-und\",\"activated\":false}","scotty_upload_url":"/upload/document/resumable","docs-net-udmi":500000,"docs-net-udpt":40000,"docs-net-udur":"/upload/blob/document","docs-net-usud":true,"docs-enable_feedback_svg":false,"enable_feedback":true,"docs-fpid":713722,"docs-fbid":"ExternalUserData","customer_type":"ND","docs-obsImUrl":"https://ssl.gstatic.com/docs/common/netcheck.gif","docs-lsltms":20000,"lssv":7,"docs-offline-oebp":"/offline/eventbusworker.js","docs-offline-swcmcd":30000,"docs-offline-swcmcul":10,"docs-offline-nnodi":100,"docs-localstore-iort":10000,"docs-offline-dck":"AIzaSyDrRZPb_oNAJLpNm167axWK5i85cuYG_HQ","docs-offline-mobile-mms":15000000,"docs-extension-id":"ghbmnnjooekpmoecnnnilnnbdlolhkhi","docs-ewtaoe":true,"docs-offline-hsu":"docs.google.com","dffm":["Calibri","Cambria","Syncopate","Lobster","Corsiva","Coming Soon","Shadows Into Light","Indie Flower","Tahoma","Crafty Girls","Proxima Nova","Roboto Condensed","Average","Lato","Source Code Pro","Old Standard TT","Alfa Slab One","Playfair Display","PT Sans Narrow","Muli","Montserrat","Roboto Slab","Raleway","Open Sans","Oswald","Amatic SC","Source Sans Pro","Roboto","Economica","Reenie Beenie","Stint Ultra Expanded","Alegreya","Merriweather"],"dffd":["Calibri","Cambria","Syncopate","Lobster","Corsiva","Coming Soon","Shadows Into Light","Indie Flower","Tahoma","Crafty Girls","Proxima Nova","Roboto Condensed","Average","Lato","Source Code Pro","Old Standard TT","Alfa Slab One","Playfair Display","PT Sans Narrow","Muli","Montserrat","Roboto Slab","Raleway","Open Sans","Oswald","Amatic SC","Source Sans Pro","Roboto","Economica","Reenie Beenie","Stint Ultra Expanded","Alegreya","Merriweather"],"docs-offline-toomem":false,"kixOfflineUrl":"/document","trixOfflineUrl":"/spreadsheet","trixOfflineUrlSuffix":"/offline/view","trixOnlineUrlSuffix":"/ccc","ritzOfflineUrl":"/spreadsheets","drawingsOfflineUrl":"/drawings","punchOfflineUrl":"/presentation","docs-irbfes":true,"docs-offline-ercidep":true,"docos-eos":true,"docs-offline-lsuid":"ue19ca827904bab0f","docs-offline-ue":"mattamos250@gmail.com","udurls":true,"docs-localstore-cide":true,"docs-localstore-dom":false,"docs-offline-uifeo":"[\"ue19ca827904bab0f\",\"mattamos250@gmail.com\",\"en_GB\",1,1,0,null,0]","icso":false,"docs-offline-copy":false,"docs-clsvn":2,"docs-rlsvn":2,"docs-offline-desktop-mms":200000000,"docs-offline-uebie":true,"docs-localstore-eplam":false,"docs-emasl":false,"fatra":true,"docs-sw-ecfr":false,"docs-cibs":500,"docs-doie":false,"docs-sw-eddf":false,"docs-efcs":false,"docs-offline-oepdp":false,"docs-offline-eoep":true,"docs-offline-eeooip":true,"docs-offline-eorlv":false,"docs-eoufm":false,"docs-localstore-ilat":10000,"docs-sw-nfhms":10,"docs-offline-ouil":["ue19ca827904bab0f","ue73a2fe4c78a5ff8"],"docs-sw-rpl":[],"docs-sw-cache-prefix":"document","docs-efrsde":true,"docs-text-ewf":true,"docs-wfsl":["ca","da","de","en","es","fi","fr","it","nl","no","pt","sv"],"docs-efpsf":true,"docs-ejsfawf":false,"docs-eksfawf":false,"docs-edfn":true,"docs-efpsp":true,"docs-localstore-eidsilfm":true,"docs-ecfdsfj":true,"docs-esreff":true,"docs-eeii":true,"docs-ecci":true,"docs-eldi":false,"docs-ecuach":false,"docs-cclt":56,"docs-esi":false,"docs-liap":"/naLogImpressions","ilcm":{"eui":"ADFN-csz7F18nxl_fXSvbEoqn_eQVQAyYpqv2YI0ZHxgfnScWTmTfzesepMEXCFk6Dd84yvY7LkZ","je":1,"sstu":1673676861965451,"si":"CKaIzpa0xvwCFeKBIAEd0AYCtA","gsc":2,"ei":[5700019,5700032,5700057,5700103,5700114,5700261,5700333,5700611,5700884,57…

---
## [gitster/git](https://github.com/gitster/git)@[07f91e5e79...](https://github.com/gitster/git/commit/07f91e5e79810a8f17de745d2d84c384add75f0a)
#### Tuesday 2023-05-23 11:03:50 by Jeff King

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
## [git-for-windows/git](https://github.com/git-for-windows/git)@[3e56d1bb07...](https://github.com/git-for-windows/git/commit/3e56d1bb076efe5ce883374b73890e817a4bcc84)
#### Tuesday 2023-05-23 11:06:22 by Johannes Schindelin

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
## [tiwai/sound](https://github.com/tiwai/sound)@[1bba82fe1a...](https://github.com/tiwai/sound/commit/1bba82fe1afac69c85c1f5ea137c8e73de3c8032)
#### Tuesday 2023-05-23 12:17:21 by Darrick J. Wong

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
## [StephenCleary/comments.stephencleary.com](https://github.com/StephenCleary/comments.stephencleary.com)@[326e90ab45...](https://github.com/StephenCleary/comments.stephencleary.com/commit/326e90ab4562c0a0a47a849d550ab8be39564b1d)
#### Tuesday 2023-05-23 13:12:03 by Comment Bot

(Staticman) Stephen The Ahole Cleary humps Muslim goats: wow great copy and paste article. Hey you stupid sob why don't you just copy and paste an article next time you shit ass

https://blog.stephencleary.com/2012/09/introduction-to-dataflow-part-2.html#comment-57ee6199-4383-422e-a0ee-882210ad63e1

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[661624802b...](https://github.com/odoo-dev/odoo/commit/661624802b1c50cb9cad4ad11bc59db7f9375f8a)
#### Tuesday 2023-05-23 13:50:59 by Jeremy Kersten

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

closes odoo/odoo#119230

X-original-commit: 4aca39a533e9d41f5f452f36a1ffc001f586b4f4
Signed-off-by: Jérémy Kersten <jke@odoo.com>

---
## [TOBKA4/cmss13](https://github.com/TOBKA4/cmss13)@[b451aba2d4...](https://github.com/TOBKA4/cmss13/commit/b451aba2d4fd87a3b5cceaaba6955b8b783f84b2)
#### Tuesday 2023-05-23 14:38:00 by Hopekz

Fix a start now error and add the ability of queuing the start of the game (#3090)

This PR does two things.

Fixes this error when trying to start early

![dreamseeker_lIUnkd0lFZ](https://user-images.githubusercontent.com/24533979/232609965-5cf94825-0671-420b-8625-16f505f26d63.png)


And adds queuing meaning that if an admin wants to start a game early
during loading; it will now tell them that the game will launch as soon
as it is available then waits for the game to be ready before starting.

Before this PR it just tells you that the game isn't ready then you have
to wait for it to load and launch the "start now" command again.

Does not bypass the "are you sure?" check because it has been moved to
the front.

Honestly made this PR because I hate waiting for the start I just want
to do it once when I see the game window then step away for like a
minute instead of having to wait for it.


:cl: Hopek
add: Adds the support for queuing the round start meaning that if an
admin pressed "start now" it will actually wait until the game is loaded
then immediately start the game as expected versus telling you to try
later.
fix: fixed the "start now" verb displaying that the game has already
started when it is loading because it didn't understand how to read the
game state properly.
/:cl:

---------

Co-authored-by: harryob <me@harryob.live>

---
## [lucasfoufou/evals](https://github.com/lucasfoufou/evals)@[114f4f8536...](https://github.com/lucasfoufou/evals/commit/114f4f8536f29df43e5145fd38826285d19d6728)
#### Tuesday 2023-05-23 14:42:52 by Greg Priday

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
## [lucasfoufou/evals](https://github.com/lucasfoufou/evals)@[bb42b3149c...](https://github.com/lucasfoufou/evals/commit/bb42b3149cd7a078cf44136e93a24f2156419acc)
#### Tuesday 2023-05-23 14:42:52 by David Chen

Add regex match eval (#159)

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

Regular Expression Match

### Eval description

Test the model's ability to understand regular expression patterns. 

### What makes this a useful eval?

- Educational purposes: Regular expressions are an important concept in
computer science and programming. By being able to evaluate them,
ChatGPT can serve as a useful learning resource for users who are
studying this topic or want to deepen their understanding.
- the accuracy is 0.79 against gpt-3.5-turbo
- Over 400 regular expression cases have been collected from related
unit tests.

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
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123' match the string ''? Answer with Yes or No."}], "ideal":
"No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern '(?P<1>a)'
match the string ''? Answer with Yes or No."}], "ideal": "No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern '(?P<!>a)'
match the string ''? Answer with Yes or No."}], "ideal": "No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo!>a)' match the string ''? Answer with Yes or No."}], "ideal":
"No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123>a)(?P=foo_123' match the string 'aa'? Answer with Yes or
No."}], "ideal": "No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123>a)(?P=1)' match the string 'aa'? Answer with Yes or No."}],
"ideal": "No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123>a)(?P=!)' match the string 'aa'? Answer with Yes or No."}],
"ideal": "No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123>a)(?P=foo_124' match the string 'aa'? Answer with Yes or
No."}], "ideal": "No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123>a)' match the string 'a'? Answer with Yes or No."}],
"ideal": "Yes."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123>a)(?P=foo_123)' match the string 'aa'? Answer with Yes or
No."}], "ideal": "Yes."}
  ```
</details>

---------

Co-authored-by: G8s Bot <g8s@gliacloud.com>

---
## [lucasfoufou/evals](https://github.com/lucasfoufou/evals)@[733167aed6...](https://github.com/lucasfoufou/evals/commit/733167aed6624945acdc51ec11407484dd2d931b)
#### Tuesday 2023-05-23 14:42:52 by Andrew

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
## [GaiaByTeamLime/firmware-v2](https://github.com/GaiaByTeamLime/firmware-v2)@[116a814e48...](https://github.com/GaiaByTeamLime/firmware-v2/commit/116a814e483e89163f0e95dd99671c289b54fa74)
#### Tuesday 2023-05-23 14:50:10 by jaschutte

Fixed a comment

Sander has stolen my sanity, I don't think I'll be the same man after this.
We reverted the revert, and for what? Just to create another pull-request?
Is this what my life has resorted too? Pull-requests for a single comment change?
Was it worth it? Was all this pain and suffering worth it? Just for a single correction in a comment?
I hope it is, as it has costed me my life. And with that, my sanity.
I am a changed man. I can never be the same.
Goodbye.

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[bfb3967c90...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/bfb3967c908682e21202312d8b30ec17ad65e549)
#### Tuesday 2023-05-23 16:10:04 by SkyratBot

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
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[727b0b51df...](https://github.com/mrakgr/The-Spiral-Language/commit/727b0b51df8a8da11b5a0a14498c3d903e698318)
#### Tuesday 2023-05-23 16:16:59 by Marko Grdinić

"8:30am. I think I accidentally refed the F# issue in yesterday's reply. Damn. That will create a link in it.

It was late so I wasn't cautious about it. This is one of the disadvantages of using Github as your blogging platform.

Anyway, I've chilled so let me get started for the day.

10:15am. Focus me stop reading the stuff on the ML sub.

///

Sigh, what we will do is put this project aside for the moment.
Let's start a new project that will be based off the MudBlazor template, and then we will try importing the diagrams component.
We want to make sure there isn't some fundamental incompat

///

Damn it, I do not want to start a new thing.

Let me pause here and I'll get to the bottom of it.

1pm. Done breakfast.

Bolero has kicked my ass thoroughly. I am going to switch to Blazor after all.

I can't even create a regular button in its DSL.

There is no point to using Bolero if I can't get Blazor components to work with it.

1:45pm. Let me resume.

https://fsbolero.io/docs/HTML

```
let myElement : Node =
    button {
        on.click (fun _ -> printfn "Clicked!")

        "Click me!"
    }
```

Ah, here is how it is possible to do it.

Enjoy Yourself by Steven O'Brien | https://www.steven-obrien.net/
Creative Commons CC BY-ND 4.0
Music promoted by https://www.chosic.com/free-music/all/
https://creativecommons.org/licenses/by-nd/4.0/

https://soundcloud.com/yoitrax/latte-by-jantrax-royalty-free-music-original
https://soundcloud.com/liqwyd/taste-it

I should leave links for these in the media clips.

5:25pm. https://youtu.be/m8Te-3rTopI
VN Compiler. We give up on Bolero. Introducing MudBlazor. (Pt. 2)

Let me post this on the F# sub.

#webdevelopment #fsharp #blazor #AspNetCore

Let me save these tags here.

5:35pm. I am done for the day here.

5:55pm. I guess I'll read more abyss loli manga.

https://mangadex.org/title/bf1d564b-e41a-4f55-9241-b5c7ac7f30ab/despite-coming-from-the-abyss-i-will-save-humanity

Let me link to it again. It really does pick up after the village battle surpringly enough and is a fun read. The novel is supposed to be GB, but the manga makes zero mention of it.

Sigh, forget it. I'll just focus on this project until I feel like I have perfected my webdev workflow which shouldn't take more than a few months once I start focusing on Blazor.

I meant to go with React, but it is not my job to specialize in outdated technologies.

I'll learn the best tools, and if the companies aren't interested that is their problem.

I'll probably end up liking Blazor.

I'll host the Leduc project properly, and put it on my resume along with Helix and Spiral, and hopefully that should be enough to get me an in.

I've already put the Youtube series on my resume. Out of the 20 compos I've applied to, I got 3 rejects so far, and I don't get the feeling I'll get any interest from the rest.

Most likely I will get interest once I get enough of an audience on Youtube, and then I'll have proper leverage for negotiation.

But that is going to be a slow process.

Still, I've realized it, had I done writing, even at the placid pace I've been getting followers, I'd have been way more successful than had I been trading or programming.

It is important to keep putting new material out there, and cultivate your connections.

Right now I have 106 subscribers on Youtube, which is not a big deal.

But it is better than Heaven's Key, and gives me a platform to cultivate my skills.

Getting a little bit like this every day is far better than programming in silence and solitude even if it slows me down.

It is not like I'll get anything in particular from the Helix project.

I've gone from living in a world where I life with my own power to, living in a world where I am dependent on the attention of others.

Because the vision of the Singularity that I had did not manifest.

The world just can't throw me a line here, but I still want to believe that programming will have a purpose in the end.

Street cleaners are not going to be the ones to bring the era of a man to an end.

I still want to believe that the programmers and the individuals will be the ones to do it.

I still want to believe that I can do something for myself with my own power.

I do not want to give up."

---
## [Kneba/kernel_asus_caf](https://github.com/Kneba/kernel_asus_caf)@[ef8c0b9a2a...](https://github.com/Kneba/kernel_asus_caf/commit/ef8c0b9a2a4c48f0e6f9a6e6c8863320706254ed)
#### Tuesday 2023-05-23 16:54:53 by Dave Chiluk

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
Signed-off-by: Tiktodz <ewprjkt@proton.me>
Signed-off-by: Kneba <abenkenary3@gmail.com>

---
## [rohankshir/evals](https://github.com/rohankshir/evals)@[34f83340a7...](https://github.com/rohankshir/evals/commit/34f83340a75b7e26af35d8eaea165e54b38d7946)
#### Tuesday 2023-05-23 17:39:28 by kallyaleksiev

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
## [rohankshir/evals](https://github.com/rohankshir/evals)@[3e92d6e27c...](https://github.com/rohankshir/evals/commit/3e92d6e27ce43c53cd6f0dba8ed05dbdc5ddfb3c)
#### Tuesday 2023-05-23 17:39:28 by ytsaig

Rhyming words in a different language (Hebrew) (#176)

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

hebrew-rhyme

### Eval description

Given a pair of two words in English, the task is to determine whether
their Hebrew translations rhyme and if so, output the rhyming pair in
Hebrew.

### What makes this a useful eval?

This task tests the ability of the model to carry out a composite task
that involves reasoning in a different language than the source
language. It is relatively simple for a bilingual human but
gpt-3.5-turbo scores about the same as random guessing.

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
{"input": [{"role": "system", "content": "For each pair of words,
determine whether their Hebrew translations rhyme. If they do, output
the pair of rhyming words in Hebrew. If not, output NONE."}, {"role":
"user", "content": "honey, detective"}], "ideal": ["דבש, בלש", "בלש,
דבש"]}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether their Hebrew translations rhyme. If they do, output
the pair of rhyming words in Hebrew. If not, output NONE."}, {"role":
"user", "content": "power, flight"}], "ideal": "NONE"}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether their Hebrew translations rhyme. If they do, output
the pair of rhyming words in Hebrew. If not, output NONE."}, {"role":
"user", "content": "melody, reaction"}], "ideal": "NONE"}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether their Hebrew translations rhyme. If they do, output
the pair of rhyming words in Hebrew. If not, output NONE."}, {"role":
"user", "content": "heart, breath"}], "ideal": "NONE"}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether their Hebrew translations rhyme. If they do, output
the pair of rhyming words in Hebrew. If not, output NONE."}, {"role":
"user", "content": "tool, without"}], "ideal": ["כלי, בלי", "בלי, כלי"]}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether their Hebrew translations rhyme. If they do, output
the pair of rhyming words in Hebrew. If not, output NONE."}, {"role":
"user", "content": "opened, laughter"}], "ideal": "NONE"}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether their Hebrew translations rhyme. If they do, output
the pair of rhyming words in Hebrew. If not, output NONE."}, {"role":
"user", "content": "sees, brain"}], "ideal": "NONE"}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether their Hebrew translations rhyme. If they do, output
the pair of rhyming words in Hebrew. If not, output NONE."}, {"role":
"user", "content": "ice cream, thank you"}], "ideal": ["גלידה, תודה",
"תודה, גלידה"]}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether their Hebrew translations rhyme. If they do, output
the pair of rhyming words in Hebrew. If not, output NONE."}, {"role":
"user", "content": "child, skeleton"}], "ideal": ["ילד, שלד", "שלד,
ילד"]}
{"input": [{"role": "system", "content": "For each pair of words,
determine whether their Hebrew translations rhyme. If they do, output
the pair of rhyming words in Hebrew. If not, output NONE."}, {"role":
"user", "content": "gift, blessing"}], "ideal": "NONE"}
  ```
</details>

Co-authored-by: Ubuntu <ubuntu@ip-10-0-1-131.us-west-2.compute.internal>

---
## [rohankshir/evals](https://github.com/rohankshir/evals)@[4f090a04fe...](https://github.com/rohankshir/evals/commit/4f090a04fe53a8d0f647bfdfc7ef177fa8034e2e)
#### Tuesday 2023-05-23 17:39:28 by Shawn Marincas

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
## [7ez/circlebot-translations](https://github.com/7ez/circlebot-translations)@[d8e43d05b4...](https://github.com/7ez/circlebot-translations/commit/d8e43d05b4042b0e429d9e00365db7e2628e75c4)
#### Tuesday 2023-05-23 17:58:49 by Aochi

Merge pull request #4 from blobnom/patch-2

fuck you aochi im gonna kill myself

---
## [davidhildenbrand/qemu](https://github.com/davidhildenbrand/qemu)@[b5d5b74bc5...](https://github.com/davidhildenbrand/qemu/commit/b5d5b74bc5c7e328697ce69e58ddcb01403d0ed2)
#### Tuesday 2023-05-23 18:52:02 by David Hildenbrand

virtio-mem: Expose device memory via multiple memslots if enabled

Having large virtio-mem devices that only expose little memory to a VM
is currently a problem: we map the whole sparse memory region into the
guest using a single memslot, resulting in one gigantic memslot in KVM.
KVM allocates metadata for the whole memslot, which can result in quite
some memory waste.

Assuming we have a 1 TiB virtio-mem device and only expose little (e.g.,
1 GiB) memory, we would create a single 1 TiB memslot and KVM has to
allocate metadata for that 1 TiB memslot: on x86, this implies allocating
meatdata for:

(1) RMAP: ~0.2% (~2100 MiB). Not that this is optimized out with the TDP
    MMU, but will be allocated lazily when running nested VMs.
(2) gfn_track: 0.024% (~252 MiB)
(3) Bitmap when dirty-tracking: 2 x 0.003% (~63 MiB)

Consequently, using multiple memslots and only mapping the memslots we
really need can significantly reduce memory waste and speed up
memslot-related operations. Let's expose the sparse RAM memory region using
multiple memslots, mapping only the memslots we currently need into our
device memory region container.

A nice side effect is that we will expose less memory to the guest, so
a malicious guest won't be able to do that much harm and we might be
able to detect some BUGs in well-behaving guests more easily. However,
in the future we'll want to properly protect all unplugged memory from
getting reallocated (using features that have to be separately enabled).

* With VIRTIO_MEM_F_UNPLUGGED_INACCESSIBLE, we only map the memslots that
  actually have memory plugged, and dynamically (un)map when
  (un)plugging memory blocks.

* Without VIRTIO_MEM_F_UNPLUGGED_INACCESSIBLE, we always map the memslots
  covered by the usable region, and dynamically (un)map when resizing the
  usable region.

We'll auto-detect the number of memslots to use based on the remaining
available memslots and the remaining avilable size for memory devices using
our new helper. Further, we'll take care to not consume a crazy number of
memslots, because the assumption is that many memslots can degrade
performance especially in QEMU, at least right now. Let's not use more than
512 memslots per device and not use memslots smaller than 1 GiB for now.
Note that our global limit for all memory devices is currently set to
1024, so even with multiple big virtio-mem devices, we'd still have a sane
limit. We might want to fine-tune these values in the future (might have
to do via compat machine properties).

Still default to a single memslot for now, because it can be problematic in
vhost setups, and we don't want to break existing setups. We'll change
the default via compat machines in the future. Until then, this feature can
be enabled using "force-single-memslot=false".

As vhost devices are currently very limited when it comes to the number
of supported memslots, they have to be defined on the QEMU cmdline
before defining the virtio-mem devices. Otherwise, aut-detection is
unaware of the additional restriction and QEMU will bail out when
realizing the vhost device. Further, hotplug of vhost devices might
require planning ahead.

Note 1: how many memslots we'll be using is an internal implementation
detail (especially: migration is not affected), and we can change the
auto-detection as we please. Values (including "force-single-memslot") can
differ on migration source and destination.

Note 2: we should look into supporting more memslots (512 -- 1024)
especially for vhost-user soon, but that will require changes in QEMU
(to make many memslots scale better) and support in vhost-user
implementations. So we'll have to life with this vhost memslot limitation
oddity for now.

Signed-off-by: David Hildenbrand <david@redhat.com>

---
## [davidhildenbrand/qemu](https://github.com/davidhildenbrand/qemu)@[f9b3ae4e03...](https://github.com/davidhildenbrand/qemu/commit/f9b3ae4e034de9442abe6026330a258273df8420)
#### Tuesday 2023-05-23 18:52:02 by David Hildenbrand

memory-device: Add a memslot soft-limit for memory devices and warn the user

While we properly check before plugging a memory device whether there
still is a free memslot, we have other memslot consumers (especially PCI
BARs) that don't perform any checks and might dynamically consume
memslots without any prior reservation later. So we might succeed in
plugging a memory device, but once we dynamically map a PCI BAR we would
be in trouble.

Let's indicate to the user that we cannot guarantee that everything will
work as intended and that we might run out of free memslots later. We'll
warn once, when we detect that there are not that many memslots around,
and once we then exceed the calculated soft-limit.

As long as we don't have to warn the user (IOW, at least 253 memslots set
aside), we don't expect surprises. Especially environments with very little
memslots (32 with vhost-user) are quite possibly problematic.

We use the historic magic memslot number of 509 as orientation to when
supporting 256 memory devices (leaving 253 for boot memory and other
devices) has been proven to work reliable. We'll warn on anything below
that for now.

We still allow to exceed the soft-limit, because there might be
reasonable setups that simply work.

We'll cap the soft-limit at 512, which no setup should currently really
exceed (ACPI supports a maximum of 256 slots). Note that the soft-limit
will be used in virtio-mem context soon, when auto-determining the number
of memslots to use.

Signed-off-by: David Hildenbrand <david@redhat.com>

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[c20b961685...](https://github.com/shiptest-ss13/Shiptest/commit/c20b961685c78760ab807c95a2e79fe72ee4d507)
#### Tuesday 2023-05-23 19:29:03 by thgvr

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
## [RebeccaBaumgarten/Handouts-for-Apologetics-Talks](https://github.com/RebeccaBaumgarten/Handouts-for-Apologetics-Talks)@[3e1d46387c...](https://github.com/RebeccaBaumgarten/Handouts-for-Apologetics-Talks/commit/3e1d46387ccc9585b75666e05a8e5f6bd6172eda)
#### Tuesday 2023-05-23 19:48:32 by Rebecca Baumgarten

Uploaded file

First 2 principles of Catholic Social Teaching:
1.	Life and Dignity of the Human Person
2.	Call to Family, Community, and Participation
Quotes from the Bible, the Catechism of the Catholic Church, United States Conference of Catholic Bishops, C.S. Lewis, and Ronald Reagan
Explains the special dignity of the human person
Examines ordinary and extraordinary care and what is morally obligatory, using case studies
Lists affronts to life or human dignity
Further reading

---
## [discordexperimenthub/deh-ai](https://github.com/discordexperimenthub/deh-ai)@[12a520bee0...](https://github.com/discordexperimenthub/deh-ai/commit/12a520bee03439193f778fe86d33ded302af8537)
#### Tuesday 2023-05-23 20:00:20 by Samomen

I DONT HAVE BRAINNNN

I'm not even sure if I'm going to finish it or not, I'm just writing this damn thing to get new experiences, I'm changing it, I don't know what I'm doing, I'm just pressing the keys on the damn keyboard and I guess that's not enough. Obviously this is a suicide note thank you to everyone I love for being a part of my life. @Surge13z don't forget me cute human

---
## [Nobelium-XVIII/tgstation](https://github.com/Nobelium-XVIII/tgstation)@[4014aef4b0...](https://github.com/Nobelium-XVIII/tgstation/commit/4014aef4b0a24d260b314f462a21f943c3d62894)
#### Tuesday 2023-05-23 20:00:47 by Bloop

Fixes a runtime in simple_animal/hostile (#74706)

## About The Pull Request

Attempting to fix this flaky test that has been cropping up from the
Icebox tests. It is annoying.

From what I can tell, the mob was getting qdeleted while it was doing
its loop of finding a target. This can happen at any time, because many
simple mobs (including the one causing the issues) get qdeleted on
death.

Added some more checks to make sure we don't do certain actions if the
mob gets qdeleted midway through execution of its AI routine. It really
could happen anywhere so we must be vigilant.

```
create_and_destroy: [02:24:31] Runtime in stack_trace.dm,4: addtimer called with a callback assigned to a qdeleted object. In the future such timers will not be supported and may refuse to run or run with a 0 wait (code/controllers/subsystem/timer.dm:583)
proc name:  stack trace (/proc/_stack_trace)
src: null
call stack:
stack trace("addtimer called with a callbac...", "code/controllers/subsystem/tim...", 583)
addtimer(/datum/callback (/datum/callback), 300, 8, null, "code/modules/mob/living/simple...", 595)
the demonic watcher (/mob/living/simple_animal/hostile/asteroid/ice_demon): GainPatience()
the demonic watcher (/mob/living/simple_animal/hostile/asteroid/ice_demon): GiveTarget(the mi-go (/mob/living/simple_animal/hostile/netherworld/migo))
the demonic watcher (/mob/living/simple_animal/hostile/asteroid/ice_demon): FindTarget(/list (/list))
the demonic watcher (/mob/living/simple_animal/hostile/asteroid/ice_demon): AIShouldSleep(/list (/list))
the demonic watcher (/mob/living/simple_animal/hostile/asteroid/ice_demon): handle automated action() at stack_trace.dm:4
```

On top of that, there is signal handling in place to LoseTarget() when a
mob that is already a target gets qdel'd and sends
`COMSIG_PARENT_QDELETING`. Shown below.


https://github.com/tgstation/tgstation/blob/4c48966ff80915ee0b4f796994a0ab6616cab31b/code/modules/mob/living/simple_animal/hostile/hostile.dm#L655-L666

However there is nothing stopping a target that is not null but that has
been qdeleted from being considered as a target in the first place.

This PR just aims to fix that problem by making sure that a) a hostile
ai that gets qdeleted midway through does not keep doing stuff that can
cause issues and b) an atom that is being qdeleted never makes its way
into the targets list of a hostile ai.

Simple mobs/AI are due for a wider refactor honestly but this really
ought to be done in the meantime so we don't get spammed by CI failures
over nonsense.

Fixes https://github.com/tgstation/tgstation/issues/73032
Fixes https://github.com/tgstation/tgstation/issues/74266
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/18964
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/19749
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/18964
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/19322
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/18974
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/19296
Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/19294


## Why It's Good For The Game

Bugfix, stops the icebox test from failing as much.

## Changelog
:cl:
fix: fixes hostile mobs sometimes being able to target an atom that has
been marked for deletion and then becoming confused, and in a similar
vein fixes mobs sometimes still running their AI while being marked for
deletion.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [RebeccaBaumgarten/Handouts-for-Apologetics-Talks](https://github.com/RebeccaBaumgarten/Handouts-for-Apologetics-Talks)@[db52a64ca6...](https://github.com/RebeccaBaumgarten/Handouts-for-Apologetics-Talks/commit/db52a64ca61475ebc83df783df0d9056458a7f6f)
#### Tuesday 2023-05-23 20:11:44 by Rebecca Baumgarten

Uploaded file

Historical perspective
•	Elements of Christianity that have influence sci-fi and fantasy religions
•	Ancient paganism
•	Innovations of Judaism
Unique elements of Christianity
•	Looks at our major feast days and what they celebrate
•	Conception of God: Trinity as Love
Practical Arguments
•	Lewis’s trilemma
•	The blood of the martyrs
•	The conversion of the gentiles
Resources/further reading

---
## [AcademySoftwareFoundation/OpenShadingLanguage](https://github.com/AcademySoftwareFoundation/OpenShadingLanguage)@[71a9310f0b...](https://github.com/AcademySoftwareFoundation/OpenShadingLanguage/commit/71a9310f0b8765f57b59e25e73f5f3bbdb8077e8)
#### Tuesday 2023-05-23 20:25:30 by Larry Gritz

feat(gpu)!: GPU/OptiX support of ReParameter (#1686)

BREAKING CHANGE: to RendererServices ABI (including for CPU) and to
the renderer-side setup when using OptiX.

This overhauls the implementation of how interactively-editable
parameters work, where they live in memory, and get it all working on
GPU/OptiX so that renderers can support interactive adjustment of
those params without recompiling shaders.

The basic gist is as follows:

* We continue work to finish making a clean separation between
  "interpolated" parameters and "interactive" (editable) parameters.

* Interpolated params are collected and put into a separate memory
  area -- a separate per-group allocation on both the CPU and GPU
  (where applicable). It needs to remember the offset into this arena
  where each of the interpolated parameters resides. These allocations
  and eventual release are taken care of by the OSL shading system,
  they live in the ShaderGroup. When the group is set up, this block
  of memory is initialized with the correct initial values of the
  params and are ready to go.

* The implementation of ReParameter writes to this special memory
  area also, that's how it works now (both CPU and GPU).

* How does the OSL library know how to allocate, free, and copy to the
  device memory? It doesn't! Instead, we add new RendererServices
  methods `device_alloc()`, `device_free()`, and
  `copy_to_device()`. It's up to the renderer to provide those, so
  that the OSL library doesn't itself need to know about the Cuda
  runtime. These are trivial, there's really only one implementation
  that makes sense, and you can copy it from the ones in testshade and
  testrender.

* Interactive parameters are NOT constant folded during runtime
  optimization.

* The shader entry points themselves now take an extra parameter in
  the main call -- this will be the pointer to the beginning of the
  shader group's interactive parameter arena.

* When JITing, references to interactive parameters know to retrieve
  them from their designated offset into the interactive parameter
  area.

* This means that the renderer-side OptiX/Cuda code is responsible for
  adding this extra pointer parameter to the call to the shader entry
  points. You can see how this is done in the testshade and testrender
  Cuda code.

* It's up to the renderer to figure out how to make the OptiX hit program
  aware of the interactive parameter pointer for that particular material,
  in order to pass it to the osl shader entry point. The way I did it in
  testshade and testrender is using a field in the struct that's given
  to each entry of the shader binding table and can be retrieved on the
  OptiX side via optixGetSbtDataPointer(). In testshade/testrender, a
  data pointer already existed which wasn't used. In a real renderer, you
  may need to add a field or come up with whatever other way you want
  to somehow get this pointer, which can be retrieved via

      shadingsys->getattribute(shadergroupptr, "device_interactive_params",
                               TypeDesc::PTR, &myptr);

  you can see how I do that in optixraytracer.cpp (testrender) and in
  optixgridrender.cpp (testshade).

A number of other things you will see that's worth calling out:

I added a device_ptr utility template that is just a wrapper around a
device side pointer that makes it hard to accidentally dereference it
on the host side.

Since I was changing RendererServices anyway, I also remove unused
register_global, fetch_global, global_map which were unused. They were
leftovers from the way we handled strings in OptiX 6.x.

Encapsulate cuda global symbol name mangling into
BackendLLVM::global_unique_symname(). I did this early on, turns out
it wasn't necessary, but I still like that encapsulation, so I'm
keeping it.

I bumped the 3rd set of digits in the version to reflect that the
changes in RendererServices break ABI. This is only in main, it
obviously cannot be backported to a release branch.

All tests pass for scalar and batch and optix.

I added a new simple reparam test, and renamed the old reparem to
reparam-array. Oddly, the reparam-array test doesn't work properly on
optix (it had never been tried before), but it also failed in optix at
main -- so it's not related to this patch! Putting that on my list of
other oddities to investigate later. It may just be a quirk of
testshade, I'm not really sure yet.

Added to BackendLLVM (and batched) a llvm_ptr_type(TypeSpec) method
that returns the LLVM type of a pointer to the specified type.

Note: This patch doesn't account for the face that a parameter marked
"interactive" could prevent a shader from correctly building for the GPU
because it used the kind of construct that is fine in shader source code but
only will work on GPU if it can be resolved to be a constant by the time
we get done with the runtime optimization (as pointed out by Stephen
Friedman. We'll come back to the problem later with a more robust and
automatic fix -- and if we are lucky, Stephen will have the opportunity to
upstream the approach he already has.

Signed-off-by: Larry Gritz <lg@larrygritz.com>

---
## [nss-day-cohort-62/rare-2-server-wildlings](https://github.com/nss-day-cohort-62/rare-2-server-wildlings)@[a5d6a2b697...](https://github.com/nss-day-cohort-62/rare-2-server-wildlings/commit/a5d6a2b69759cb0c6cfcbf8e2cec386c0918c8b2)
#### Tuesday 2023-05-23 20:49:20 by Wesley Hughes

Merge pull request #13 from nss-day-cohort-62/wh

fuck you rare, hate your bitch ass

---
## [meemofcourse/Shiptest](https://github.com/meemofcourse/Shiptest)@[0cff53fc09...](https://github.com/meemofcourse/Shiptest/commit/0cff53fc09c34d989d2bc34b1699bd856af2cb92)
#### Tuesday 2023-05-23 20:51:21 by meemofcourse

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
## [myne145/myne145.github.io](https://github.com/myne145/myne145.github.io)@[4e66e8c198...](https://github.com/myne145/myne145.github.io/commit/4e66e8c1981ce94001997456d5dce3788633c256)
#### Tuesday 2023-05-23 21:15:57 by myne145

i fucking hate working on reviewpage.html
it makes me wanna puke

reviewpage.html is like a bomb covered in horse shit with cat piss poured all over it. it sucks so fucking much that i can't explain it. i think that the most accurate description would be taking a shit into your bath and making it EXPLODE on EVERY SINGLE WALL!!!

in conclusion,
I FUCKING HATE reviewpage.html!12121!!!@#

---
## [elh/evals](https://github.com/elh/evals)@[3a2d72d9cc...](https://github.com/elh/evals/commit/3a2d72d9cc0b674a6b8cb6a8cca707baa3b46840)
#### Tuesday 2023-05-23 21:33:54 by Sean Ye

Illinois Law Claims (#486)

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
Illinois Law Cases

### Eval description

This eval tests the models ability to correctly identify the case
conclusion for Trespassing, Battery, Assault, and Self-Defense. The
dataset is consisted of 88 Illinois Historical cases representing 112
legal claims. Some cases have multiple claims, each coded as a different
test case.

### What makes this a useful eval?

This assesses the model's ability to correctly categorize these
historical cases. Correctly identifying these results shows the models
capability for a strong understanding of law. The GPT-3.5-turbo models
currently receives an accuracy of 0.45.

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

This work includes data from the Illinois Intentional Tort Qualitative
Dataset, which was compiled by the Qualitative Reasoning Group at
Northwestern University. The dataset is freely available under the
Creative Commons Attribution 4.0 license from
https://www.qrg.northwestern.edu/Resources/caselawcorpus.html.

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
{"input": [{"role": "system", "content": "You will be presented with a
court claim and the criminal charge. Your role is to assess the case and
return either \"Positive\" or \"Negative\" corresponding to the case
conclusion for the criminal charge. Do not explain."}, {"role":
"system", "content": "In 2007, the Cocrofts obtained a loan for $386,750
from Countrywide Bank, FSB secured by a mortgage on the home they
already owned in Country Club Hills, Illinois. The loan closed on April
17, 2007. At the time of the closing, Countrywide improperly failed to
inform [the Cocrofts] of the real source of funding for their loan.
Plaintiffs also contend that Countrywide violated TILA by failing to
inform them that they had three days to rescind the loan and by failing
to disclose the total sale price and itemize the amount financed, as
well as by failing to make unspecified prepayment disclosures. The
Cocrofts claim that Countrywide understated the total finance charges
for the loan by more than $5,000. Plaintiffs claim that they learned of
Countrywide's misrepresentations in June 2009. They decided to exercise
their right under the provisions of TILA to rescind the loan. On July 1,
2009, they mailed notice to that effect to BA, the successor to
Countrywide, and to MERS. The Cocrofts do not say what if anything
happened as a result of those notices, but on September 29, lawyers
working for HSBC contacted them and stated that HSBC was ready to begin
foreclosure. HSBC claimed that it was the trustee of a trust that
included their loan. The Cocrofts, however, contend that the transfer of
their loan into the trust was defective. They sent HSBC's lawyers two
cease and desist letters, notifying HSBC that they had rescinded the
loan. They allege that after receiving one of the cease and desist
letters, HSBC informed them that it had no interest in the loan and that
they needed to contact the loan's servicer, Roundpoint Mortgage.
Plaintiffs also sent a copy of the rescission documents to BAC, which
they identify as the actual servicer of the loan. HSBC brought a
foreclosure action in Illinois state court on January 19, 2010. [From
below:] defendants unlawfully entered [the plaintiffs'] home by
conducting a self-help eviction of the plaintiffs and changing the locks
on their home in August 2008. At the time, [plaintiffs] had made
arrangements to rent the property in the short term and then to sell it,
and defendants' actions disrupted the sale."}, {"role": "user",
"content": "Trespass"}], "ideal": "Positive"}
{"input": [{"role": "system", "content": "You will be presented with a
court claim and the criminal charge. Your role is to assess the case and
return either \"Positive\" or \"Negative\" corresponding to the case
conclusion for the criminal charge. Do not explain."}, {"role":
"system", "content": "Defendants, on January 15, 1915, with force and
arms broke and entered the close of the plaintiff, to-wit, the southeast
quarter of the northeast quarter of section 16, township 4, south, range
3, west, in Pike county, Illinois, and cut down and destroyed 500 hedge
trees and a certain fence belonging to plaintiff situated on said land.
Defendants cut down the south half of a hedge fence which for many years
prior to February, 1915, stood upon the line between the southeast
quarter of the northeast quarter of said section 16 (hereinafter
referred to as the east forty) and the southwest quarter of the
northeast quarter of said section 16 (hereinafter referred to as the
west forty). On and prior to February 13, 1866, both of these forty-acre
tracts belonged to a man named Teadrow. On February 13, 1866, Teadrow
conveyed the west forty to Benjamin Newman, and on February 15, 1866,
conveyed the east forty to Oliver P. Rice. When these conveyances were
made there was a hedge fence on the north half of the line and a wooden
fence on the south half of the line between the two tracts. In 1868
Benjamin Newman, the owner of the west forty, removed the wooden fence
and set out a hedge fence on the south half of the line between the two
tracts. Thereafter, during the separate ownership of the tracts,
Banjamin Newman trimmed and otherwise cared for the hedge fence on the
south half of the line and Rice trimmed and looked after the hedge fence
on the north half of the line. In December, 1888, Rice conveyed the
southeast quarter of the northeast quarter of said section 16 to
Benjamin Newman, the latter thereby becoming the owner of both tracts.
Thereafter, during the ownership of both tracts by Benjamin Newman, he
required the tenants of the west forty to take care of the south half
and the tenants of the east forty to take care of the north half of the
hedge fence on the line between the two tracts. On June 22, 1904,
Benjamin Newman executed and delivered to his daughter, F. Eva Newman,
the plaintiff, who has since married J. O. Conklin, a warranty deed,
conveying to her two hundred acres of land, including the southeast
quarter of the northeast quarter of said section 16, referred to herein
as the east forty, but not including the tract referred to herein as the
west forty. This deed contained the provision that 'this deed is not to
take effect until after the death of the grantor, Benjamin Newman.' The
wife of Benjamin Newman, who is still living, did not join in the
conveyance. At the same time plaintiff executed and delivered to her
father the following written instrument signed by her: 'Whereas Benjamin
Newman has this day conveyed to me certain tracts and parcels of land in
Pike county, Illinois, to take effect after his death, I hereby agree to
pay the taxes on said land in lieu of all rents that I would otherwise
have to pay, (this does not affect any rent that is now due,) and in
consideration of my paying said taxes I am to receive all the rents,
profits, etc., that may accrue on said land.' When the conveyance was
made to plaintiff the tract in controversy known as the east forty was
in the possession of Joseph Gifford as tenant and the west forth was in
the possession of John B. Newman, a grandson of Benjamin Newman, as
tenant of Benjamin Newman. When [the plaitiff's] father delivered the
deed of June 22, 1904, he took her upon the east forty and told her and
Gifford, the tenant, that he was placing her in full possession of the
tract; that she was to receive all the rents and profits from the land
and was to keep up the repairs and pay the taxes; that she was to have
the south half of the fence on the line between the east forth and the
west forty and was to keep up that part of the fence, and that George
Newman, his son, to whom he then intended to deed the west forty, should
keep up the north half of the fence, and that thereafter plaintiff and
her tenants kept the south half of the fence in repair while the tenants
in possession of the west forty made repairs to the north half of the
fence. During the month of January, 1915, a controversy arose between
plaintiff and Defendants regarding the ownership of the hedge fence,
each party claiming the south half of the fence. During the month of
February, 1915, Defendants, over the protest of plaintiff, cut down the
south half of the hedge fence on the line between the east forty and the
west forty and erected a wire fence in the place thereof."}, {"role":
"user", "content": "Trespass"}], "ideal": "Positive"}
{"input": [{"role": "system", "content": "You will be presented with a
court claim and the criminal charge. Your role is to assess the case and
return either \"Positive\" or \"Negative\" corresponding to the case
conclusion for the criminal charge. Do not explain."}, {"role":
"system", "content": "The city of O'Fallon installed a sewer system in
about 1926. In 1961, due to backups into homes serviced by the system,
the city built an overflow outlet on East Madison Street. The overflow
was to relieve pressure in the sewer system during periods of heavy
rainfall; it proved successful in preventing backups into nearby homes.
However, when water escaped through the overflow, raw sewage was also
discharged into an open ditch that flowed into a neighboring pond. In
December 1974, the city of O'Fallon closed the overflow. On January 10,
1975, and on subsequent dates, sewage backed up into the plaintiff's
house following heavy rainfall. The January 10 backup was the worst,
causing water to accumulate in the plaintiff's finished basement to a
height of 25 1/2 inches. The lower level of the plaintiff's modern,
ranch-style home contained a family room with fireplace and built-in
bookshelves, bedroom, closet, bath and utility room with washer, dryer,
furnace and water heater. The walls were watermarked, and the tile floor
was damaged, as were the furnishings, appliances and many irreplaceable
family items such as family photographs and slides. The lower level of
the house was virtually unusable for a year, and the plaintiff had to
expend considerable time, effort and money in repairing the floor,
repainting the walls, and replacing and removing damaged personalty. The
city knew the blocking of the overflow would cause some backup, although
they were not aware that it would be as severe as it was. From January
until April or May 1975, when the city reopened the overflow, the city
attempted to alleviate the pressure in the sewer system by pumping the
water from the sewers into open ditches during periods of heavy rain.
The defendant used either large or small pumps, depending upon the
amount of water in the system. The backups into Mrs. Dial's home ended
after the overflow was reopened in April or May 1975."}, {"role":
"user", "content": "Trespass"}], "ideal": "Positive"}
{"input": [{"role": "system", "content": "You will be presented with a
court claim and the criminal charge. Your role is to assess the case and
return either \"Positive\" or \"Negative\" corresponding to the case
conclusion for the criminal charge. Do not explain."}, {"role":
"system", "content": "the plaintiff, his wife, Beatrice, and daughters,
Aurora and Angela, lived at 313 East Marquette Street in Ottawa. The lot
upon which their home was located was eighty-eight feet wide and one
hundred thirty feet deep. The home of the defendant was immediately east
and adjoining the Galvan lot, and their residences were about forty feet
apart and separated by a hedge fence. According to the testimony of the
plaintiff, he, the plaintiff, arrived at his home about five o'clock on
Friday afternoon, June 19, 1953, from his work as a bricklayer's helper.
After he had had his evening meal, he left home about seven o'clock,
paid a coal bill to a Mr. Burke, and then he and Burke went to a tavern
where they remained an hour and a half, during which time the plaintiff
drank two bottles of beer. Mr. Burke went home, and the plaintiff
proceeded to another tavern and remained there until after midnight. At
the second tavern he had four or five bottles of beer. He than proceeded
to another tavern, where he remained for fifteen minutes, and had a
glass of beer there. He then proceeded homeward, entering his lot at the
rear, and singing as he went along. Sitting upon the steps of the back
porch of his home were his wife and daughter, Angela, and when the
plaintiff arrived there he stopped singing. He refused his wife's
suggestion to go into the house and go to bed but sat down on the porch
step, took his shoes, socks, and hat off, cursed the mosquitoes, laid
down on the ground under a pear tree three or four feet from the
southeast corner of the steps of the rear porch and immediately went to
sleep. The plaintiff's wife and daughter, Angela, remained on the porch
steps after the plaintiff had laid down under the pear tree. About
fifteen minutes after he had gone to sleep, the daughter observed the
defendant coming very slowly through the hedge from his property onto
the Galvan premises. He had a knife in his hand and, without a word,
proceeded to cut the prostrate body of the plaintiff. The other daughter
of the plaintiff, Aurora, was in the house asleep but was awakened by
her sister and ran to the yard and saw the defendant 'slashing' at her
father with a knife. She called to the defendant to stop and ran for
help. Police officers arrived shortly thereafter, and they testified
that they found the plaintiff lying on the ground about six feet from
the porch of his home all covered with blood and with his hat and a pair
of shoes and socks lying next to his body. The blood was all in one
place and in the form of a pool near the pear tree. An ambulance was
called, and the plaintiff was removed to the Ryburn-King Hospital."},
{"role": "user", "content": "Battery"}], "ideal": "Positive"}
{"input": [{"role": "system", "content": "You will be presented with a
court claim and the criminal charge. Your role is to assess the case and
return either \"Positive\" or \"Negative\" corresponding to the case
conclusion for the criminal charge. Do not explain."}, {"role":
"system", "content": "Since September 2000, plaintiff regularly visited
a patient at the Illinois Department of Human Services Treatment and
Detention Facility ('Facility') in Jolict, Illinois. From May 4, 2005 to
May 11, 2005, plaintiff was subjected to patdown searches by defendant
Martin, a Security Therapist Aid II at the Facility, in which defendant
Martin placed her fingers in plaintiff's vaginal area and required
plaintiff to remove her shoes prior to being allowed to visit the
patient. Such searches occurred at least four times during the
aforementioned time period. After plaintiff's complaints to Bernard
Akpan, an Exec. 11 at the Facility, and defendant Strock, the Assistant
Security Director of the Facility, and facility patient Brad Lieberman's
complaints to defendant Budz, Director of the Facility, defendant
Sanders, Security Director of the Facility, and defendant Strock,
plaintiff was no longer required to submit to patdown searches by
defendant Martin. Rather, plaintiff's visits were preceded by a Rapiscan
scan of her person. According to plaintiff's complaint, a Rapiscan
machine is an electronic screening device used to scan a person's entire
body. 'These machines produce a naked image of the person and can also
produce evidence of highly sensitive details such as the following:
mastectomies, colostomy appliances, penile implants, catheter tubes, and
the size of a person's breasts and genitals' From May 17, 2005 to June
19, 2005, plaintiff was subjected to 20 to 25 Rapiscan scans.
Plaintiff's complaint further alleges that other Facility staff members
were allowed to view her scanned image, her scanned image was not erased
from the machine, and staff members viewed her image hours after she was
scanned, all without her consent. Additionally, while later told that
she should have had the choice between the Rapiscan scan or a physical
patdown prior to visiting a patient, plaintiff was never informed of
such a choice during the two months she underwent the Rapiscan scans."},
{"role": "user", "content": "Assault"}], "ideal": "Positive"}

  ```
</details>

---
## [an0rak-dev/avatar](https://github.com/an0rak-dev/avatar)@[2e0ccbbdda...](https://github.com/an0rak-dev/avatar/commit/2e0ccbbddab9ae37d505edcb7234b60362063f1a)
#### Tuesday 2023-05-23 22:09:54 by Sylvain Nieuwlandt

It's been a while since my last entry...

It was difficult to find some time for working on this project (I changed my
daily job and was still on probation period, family time, little games
too -- still not finished Hogwarts Legacy). The little amount I found, I spent
it learning Vulkan and trying to use it in the project.

I have some previous experience with DirectX 12 (from the past iterations of
this project), and Vulkan is quite similar in the approch. But bloody hell that
this API is verbose... It's at least 30LoC to create just one resource and we
will need at least Instance, Device (Physical&logical), Commands
Queue/Allocator/Buffer, Swapchain...

But after some time, I thought that I've shifted from my initial goal with this
project : Keep It Simple. Vulkan has a multiplatform support, which means that
specific code (like handling HWND or HINSTANCE on Windows) must be done through
extensions to enable, more specific headers to includes, and .lib/.dll to add.
And it's not the simplest way to do low-level graphic programming on Windows,
because it will require installation of external tools and libraries as long as
a lot of checks to make sure that  the platform supports the extensions.

On the other end, Windows already have a low-level graphic API : DirectX12.
Headers and libs are already bundled in all Visual C++ redistribuable packages,
and there is no need to load runtime extensions because we _know_ the platform
it works on.

So I decided to put on hold the vulkan implementation and go back to a DirectX12
one instead. I've just backport the core mechanics around the game level
management.

---
## [openai/evals](https://github.com/openai/evals)@[24f78a806e...](https://github.com/openai/evals/commit/24f78a806e60b452aaefc355f045c6336a81d076)
#### Tuesday 2023-05-23 22:53:19 by YuryRudnitski

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
## [openai/evals](https://github.com/openai/evals)@[1785cf6cc2...](https://github.com/openai/evals/commit/1785cf6cc289c4a01445fd0eabdfa1a281873d1c)
#### Tuesday 2023-05-23 22:54:07 by Jongseung (John) Lim

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
## [openai/evals](https://github.com/openai/evals)@[6087aee945...](https://github.com/openai/evals/commit/6087aee94583a5ac440f024756b2d9a5f3754410)
#### Tuesday 2023-05-23 22:56:42 by lucasfoufou

Find country from svg (#418)

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
Find country from svg

### Eval description

Test the model's ability to distinguish a country based on its svg shape
(from wikimedia svg file).

### What makes this a useful eval?

Multiple real life use case, the first one would be to understand that a
svg shape is a country (it could be very useful for scraps via [Text
from:] prompts). On the opposite side, while asking to create an app or
a website (with a map, I just had the case for a client), GPT would
currently hint you to find the svg of the country on the web, mainly
linking to wikimedia, this solution is quicker.

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

GPT currently lacks of geography "knowledge" (I've tried him on multiple
tasks where it fails), this evals would help him "recognize" country
shapes, if that's a thing ?

## Eval structure 🏗️

Your eval should
- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [X] Ensure you have the right to use the data you submit via this eval
(it's in public domain from wikimedia)

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
{"input": [{"role": "system", "content": "I will provide you with the
svg with one shape, you will tell me which country it is the shape
of."}, {"role": "user", "content": "<svg><path
xmlns=\"http://www.w3.org/2000/svg\" d=\"m 1277.96,284.094 c 0.89,-0.422
1.96,-0.686 2.95,-0.504 0.34,-1.514 -1.67,-0.473 -2.09,-1.512
0.92,-0.307 2,-0.194 2.96,-0.145 -0.75,-0.129 -1.77,0.138 -1.23,-0.792
-0.58,-0.03 -2.55,1.079 -2.79,0.108 -0.32,-1.325 1.7,-2.125 2.66,-2.315
1.29,-0.256 2.51,-0.36 3.82,-0.324 1.85,0.05 3.04,-1.75 5.1,-1.501
-0.24,0.665 2.23,2.987 2.92,2.708 0.47,-0.226 0.91,-0.484 1.34,-0.772
0.94,-0.521 0.88,0.152 1.66,0.302 0.77,0.148 1.37,-0.462 1.42,0.787
0.5,-0.347 -0.24,-0.762 0.17,-1.327 0.43,-0.577 0.65,0.299 1.02,0.397
0.88,0.232 2.02,0 2.91,-0.15 -1.89,-0.553 -1.2,-3.219 -1.04,-4.608
0.1,-0.676 -0.95,-1.354 -1.3,-1.826 -0.6,-0.813 0,-2.049 -0.9,-2.711
0.65,0.114 1.25,0.434 1.9,0.569 0.71,0.148 1.58,-0.549 2.21,-0.235
0.97,0.488 -0.24,1.954 1.1,2.724 0.39,0.222 1.09,-0.173 1.49,-0.177
1.17,-0.01 2.29,0.385 3.43,0.601 1.11,0.211 2.08,0.179 3.07,-0.39
0.9,-0.515 2.11,-0.496 2.93,-1.075 -0.65,0.256 -1.75,0.386 -2.38,0.03
-1.27,-0.731 1.67,-2.529 2.15,-2.748 1.55,-0.694 3.31,-0.611 4.88,-1.241
0.91,-0.365 2.13,-2.453 3.26,-1.869 -0.99,-0.639 -0.38,-5.064
0.44,-5.893 0.81,-0.814 4.94,-2.286 6.01,-1.391 0.54,0.456 -0.52,2.21
1.06,2.601 1.63,0.403 1.25,0.04 2.41,0.383 1.08,0.325 0.74,1.156
1.57,1.56 1.09,0.527 2.19,-0.1 2.05,1.586 0.65,-0.419 1.78,-0.322
2.46,-0.08 1.3,0.444 0.75,2.039 0.49,2.965 0.87,0.145 1.85,0.414
2.71,0.07 0.85,-0.341 1.05,-1.314 1.9,-1.654 0.1,0.536 -0.15,2.933
0.58,2.959 1.07,0.04 3.23,1.451 3.56,2.478 -0.1,-0.296 4.07,0.378
4.28,0.396 1.02,0.09 1.77,-0.122 2.58,0.715 0.63,0.66 1.07,1.697
2.03,1.948 0.21,-0.1 0.37,-0.244 0.5,-0.438 0.31,-0.321 0.46,0.105
0.79,0.15 0.19,0.07 0.24,0.196 0.15,0.377 -0.1,0.392 0.86,0.178
1.01,0.191 1.03,0.09 1.61,-0.538 2.56,0.183 1.01,0.768 3.09,0.91
4.35,1.121 -1.54,1.365 -2.97,2.863 -3.47,4.891 -0.24,0.986 -0.83,1.892
-0.99,2.886 -0.1,0.65 0.12,0.914 -0.14,1.749 -0.31,1.009 0.46,1.85
-0.22,2.476 -0.58,0.528 -1.02,1.037 -1.88,0.96 -0.72,-0.06 -0.78,-1.131
-1.65,-0.648 -0.62,0.349 -0.68,1.463 0.36,1.296 -0.78,0.826 -1.48,1.807
-2.38,2.52 -0.55,0.358 -1.09,0.734 -1.61,1.128 -0.43,0.39 -0.39,1.154
-0.76,1.608 -0.62,0.774 -1.83,1.138 -2.02,2.232 0.14,0.373 0.24,0.757
0.29,1.151 -0.15,0.709 -0.81,0.962 -1.08,1.584 1.19,-0.149 1.63,-0.555
1.94,-1.691 0.31,-1.118 2.37,-1.032 3.21,-0.797 1,0.283 0.32,1.927
1.04,2.728 1.27,1.392 0.49,1.914 -0.65,2.857 0.61,0.857 2.88,2.445
2.26,3.701 -0.43,0.843 -3.57,2 -3.56,2.144 0,0.994 1.97,1.841 2.63,2.408
0.96,0.82 -1.33,2.281 -1,3.365 0.4,1.316 2.92,2.808 4.25,2.275
1.67,-0.669 1.42,0.304 0.79,1.417 -1.52,2.681 -4.43,4.033 -7.03,5.786
0.17,0.244 0.34,0.484 0.51,0.72 -0.97,0.139 -1.78,0.637 -2.69,0.955
-0.97,0.343 -1.6,-0.197 -2.52,-0.124 -1.4,0.11 -2.26,-1.056 -3.93,-0.903
0.67,-1.731 -2.2,-0.404 -2.23,-1.41 0.18,-0.312 0.47,-0.394 0.86,-0.246
0,-0.567 -0.37,-0.887 -0.94,-0.864 0.48,0.734 0.1,0.842 -0.59,0.875
-1.09,0.05 -1.2,-0.01 -1.5,-1.307 0.39,2.583 -0.27,0.936 -1.94,0.936
-0.97,0 -1.76,-0.61 -2.7,-0.656 -1.15,-0.06 -2.42,1.249 -3.45,1.719
-0.8,0.367 -3.62,1.411 -3.44,2.5 0,0.357 -0.13,0.689 -0.32,0.996
-0.45,0.4 -0.41,0.756 0.11,1.068 0.4,1.252 0.14,1.879 0.87,3.086
-0.69,0.197 -1.29,-0.149 -1.97,-0.108 -0.7,0.04 -1.06,0.605 -1.69,0.777
-1.52,0.415 -2.45,-1.16 -3.91,-0.1 -0.1,0.07 -2.12,-0.872 -2.34,-1.035
-0.57,-0.423 0.73,-0.369 -0.18,-0.978 -0.53,-0.353 -1.48,-0.508
-1.93,0.07 -0.21,-1.289 -1.64,-0.75 -2.41,-1.362 -1.07,-0.845
-3.26,-1.387 -2.92,0.643 -1.2,-0.173 -2.55,-0.475 -3.76,-0.253
-0.67,0.123 -1.12,0.313 -1.69,-0.203 -1.02,-0.914 -0.94,-0.538
-1.97,-0.552 -1.03,-0.01 -5.97,-3.26 -6.48,-1.944 -0.94,-0.386
-0.27,-1.066 -0.21,-1.721 0.1,-0.779 -2.2,-0.424 -2.67,-1.015
2.86,-1.059 3.1,-5.023 3.62,-7.601 0.21,-1.012 0.39,-2.607 1.23,-3.329
1.23,-1.052 -0.42,-1.2 -0.53,-0.01 -0.17,-2.436 0.32,-5.421 1.37,-7.632
1.01,0.569 2.02,1.244 2.45,2.376 0.1,0.504 0.19,1.008 0.29,1.512
0.23,0.641 0.87,0.729 0.86,1.512 0.29,-1.007 -0.73,-1.782 -0.83,-2.736
-0.14,-1.466 -0.66,-2.459 -1.96,-3.172 -0.54,-0.298 -1.15,-0.705
-1.6,-1.142 -0.74,-0.712 1.19,-0.357 1.58,0 -0.91,-0.441 -0.96,-4.294
-0.43,-5.04 -1.19,0.835 -4,-0.808 -4.55,-1.915 -0.49,-0.979 -1.6,-1.488
-1.82,-2.631 -0.2,-1.043 1.71,-2.185 -0.69,-2.293 0.28,-0.333
0.34,-0.938 0.7,-1.192 0.92,-0.638 1.76,0.435 2.62,0.544 -1.53,-1.009
-2.13,-0.674 -3.73,-0.466 -0.8,0.105 -2.36,-1.08 -0.88,-1.262
-0.41,-0.407 -0.24,-0.671 0.5,-0.792 -1.13,-0.282 -2.75,0.642
-3.67,-0.36 0.51,0 0.99,-0.127 1.44,-0.36 -0.9,-0.604 -2.57,-0.359
-2.81,0.864 0,-0.8 -0.92,-1.548 -0.1,-2.231 -0.35,0.876 -1.92,0.819
-0.94,-0.288 -1.99,1.73 -4.67,-2.209 -6.69,-0.07 -0.81,-1.117
-1.48,-1.803 -2.87,-2.092\"/></svg>"}], "ideal": ["France"]}
{"input": [{"role": "system", "content": "I will provide you with the
svg with one shape, you will tell me which country it is the shape
of."}, {"role": "user", "content": "<svg><path
xmlns=\"http://www.w3.org/2000/svg\" id=\"cd\" class=\"landxx cd\" d=\"m
1393.81,748.499 c 0.69,-0.521 1.53,-0.08 1.8,-1.012 0.22,-0.755
0.84,-3.721 0.31,-4.328 -1.38,-1.588 4,-3.988 5.01,-4.891 0.27,1.147
1.95,1.314 2.02,2.521 0.54,-0.559 1.25,-0.89 1.85,-1.371 0.81,-0.656
0.47,-1.845 1.18,-2.589 1.2,1.591 3,-1.453 4.41,-0.744 1.35,0.676
0.11,0.977 -0.1,1.824 -0.23,0.951 0.37,1.993 0.37,2.949 0.6,-0.772
1.92,0.202 2.73,-0.359 1.19,-0.829 1.93,-2.404 2.84,-3.516 0.47,-0.576
2.39,-1.501 2.49,-2.024 0.27,-1.382 1.42,-1.713 2.56,-2.2 2.66,-1.134
3.13,-6.138 3.07,-8.528 0,-1.819 0.12,-3.463 -0.11,-5.279 -0.22,-1.742
1.97,-2.189 2.71,-3.567 1.73,-3.247 1.6,-5.301 5.12,-7.692 1.48,-1.007
2.38,-2.189 3.37,-3.577 0.98,-1.382 0.27,-3.4 0.67,-4.985 0.35,-1.392
1.03,-7.368 1.09,-8.935 0.1,-1.771 1.09,-3.324 1.38,-5.05 0.29,-1.671
-0.2,-3.438 0.17,-5.092 0.71,-3.114 2.57,-5.662 3.63,-8.623 0.62,-1.72
0.33,-3.533 0.28,-5.287 0,-0.809 0.35,-1.657 0.22,-2.448 -0.11,-0.705
-0.53,-1.293 -0.72,-1.971 -0.31,-1.078 1.57,-1.049 2,-2.032 0.6,-1.357
1.23,-2.549 2.25,-3.647 0.99,-1.052 2.22,-1.952 3.73,-1.941 1.27,0
1.78,1.112 2.6,1.293 1.89,0.419 3.65,2.466 4.35,4.206 0.58,1.421
2.62,0.36 3.77,0.707 0.63,0.188 0.94,1.033 1.66,1 0.63,-0.03 0.77,-0.145
1.42,0.191 0.99,0.506 1.19,0 2.17,-0.06 0.65,-0.04 1.36,0.302 1.96,0.522
1.07,0.398 2.54,1.173 3.71,0.76 2.1,-0.738 1.46,-5.749 4.25,-5.88
1.59,-0.08 2.01,3.142 4.09,1.177 0.88,-0.831 6.94,-1.633 6.57,-3.625
1.26,-0.05 1.68,1.669 2.88,1.548 1.45,-0.146 3.93,-0.364 4.53,-1.908
0.23,-0.576 -0.35,-1.151 0.41,-1.533 0.93,-0.466 1.7,-0.188 2.42,0.528
1.17,1.147 2.25,-0.203 3.54,0.408 0.64,0.302 1.17,0.782 1.79,1.105
0.73,0.376 1.25,0.06 2.02,0.172 1.83,0.275 2.54,-1.756 4.47,-0.662
0.73,0.416 3.28,2.021 3.28,2.97 0,0.465 0.6,1.612 1.05,1.796 1.9,0.773
3.71,3.567 5.73,1.659 1.15,-1.082 2,-1.298 3.52,-0.555 1.56,0.765
2.18,0.455 3.11,-1.363 1.21,-2.397 4.32,3.607 4.48,4 0.71,1.754
5.45,1.985 4,4.723 0.92,-0.216 2.04,-0.273 2.27,0.9 0.11,0.313
0.27,0.603 0.48,0.867 0.12,0.602 -0.7,1.727 -0.61,2.355 0.29,2.012
0,4.015 -0.34,5.933 -0.15,1.011 0.6,0.878 1.74,0.678 0.52,-0.09
2.5,1.295 2.14,2.396 -0.86,2.629 -4.13,5.237 -6,7.185 -0.62,0.644
-1.87,2.357 -2.62,2.99 -0.75,0.632 -0.83,0.09 -1.26,0.918 -0.54,1.034
0.12,2.297 -0.53,3.355 -0.73,1.174 -1.45,2.943 -1.61,4.325 -0.14,1.238
-0.12,2.489 -0.2,3.731 -0.11,1.453 -0.3,2.722 -0.45,4.102 -0.11,1.009
0.15,2.425 -0.31,3.349 -0.53,1.051 -1.38,1.445 -2.15,2.296 -1.19,1.317
-1.09,1.742 -1.14,3.287 0,1.018 -1.11,2.163 -1.67,2.89 -1.21,1.603
0.48,3.278 1.42,4.805 0.71,1.151 1.22,1.959 0.7,3.544 -1.91,1.674
0.4,6.932 -1.4,8.659 1.31,0.757 1.07,-2.637 1.53,-2.063 0.45,2.673
-1.22,4.611 -1.23,7.23 0,3.402 2.85,4.969 1.64,7.322 -0.7,1.358
-1.43,1.657 -0.84,2.532 0.9,1.34 1.28,3.548 3.06,7.032 1.19,2.328
4.59,1.892 4.79,7.5 0.1,2.201 1.8,0.993 2.46,4.37 -4.7,1.073 -8.17,1.196
-12.89,2.206 1.95,3.224 -3.12,4.564 -4.03,6.979 2.71,0.838 1.81,5.035
1.63,7.086 -0.14,1.493 0.43,2.903 0.34,4.381 0,0.775 -0.21,1.511
-0.52,2.18 -0.45,0.968 -0.76,1.698 -1.01,2.72 -0.49,2.006 -1.17,3.153
0.1,5.093 0.89,1.35 2.52,3.048 3.69,4.155 0.53,0.497 3.31,2.201
3.52,1.167 0.39,-1.837 0.87,-1.494 2.68,-2.012 0,2.897 -0.1,5.805
-0.18,8.701 0,0.447 0.32,2.356 -0.43,2.431 -0.88,0.09 -1.07,-0.928
-0.46,-1.413 -1.3,-1.593 -4.21,3.376 -5.58,0.392 -0.46,-0.994
-0.89,-2.254 -1.56,-3.155 -0.38,-0.512 -1.4,-1.171 -1.52,-1.776
-0.23,-1.183 -0.46,-2.555 -1.95,-2.597 -1.25,-0.03 -1.79,-1.34
-2.98,-1.484 -1.01,-0.121 -1.62,0.635 -2.31,-0.466 -0.54,-0.854
-0.56,-2.098 -1.34,-2.799 -1.11,-1 -1.91,-4.476 -2.88,-1.358 -1,3.216
-2.76,1.525 -5.27,1.614 -1.69,0.06 -2.09,-0.477 -3.51,-1.124 -0.1,-0.04
-1.6,-0.401 -1.64,-0.394 -2.28,0.4 -2.96,-3.062 -2.15,-4.641 -1.4,0.08
-2.81,0.375 -4.11,0.87 -1.61,0.608 -1.95,1.4 -3.74,0.65 0.69,-1.238
0.73,-2.872 0.13,-2.843 -0.78,0.04 -1.11,-0.627 -1.65,-1.14 -1.25,-1.191
-1.08,0.215 -1.38,0.318 -1.11,0.385 -1.6,0.328 -2.6,0.07 -1.21,-0.313
-1.96,0.53 -3.03,0.908 -1.37,0.485 -2.24,-0.437 -3.13,-0.283 -0.32,0.05
-1.59,-0.08 -1.63,-0.06 -0.86,0.463 -1.3,1.761 -2.48,1.732 0.27,-0.889
-0.27,-1.587 -0.42,-2.422 -0.22,-1.147 0.58,-1.353 0.83,-2.235
0.58,-2.045 -0.22,-5.594 -1.46,-7.239 -1.51,-2.007 -2.16,-3.263
-1.97,-5.861 0.19,-2.685 1.13,-5.502 0.43,-8.174 -0.27,-1.021
-0.99,-1.907 -0.98,-2.99 0,-1.224 0.7,-2.37 0.79,-3.585 0.15,-2.002
-1.14,-1.78 -2.77,-1.795 -1.54,-0.01 -3.07,-0.04 -4.61,0.02 -3.17,0.134
-2.69,-0.557 -1.79,-3.234 -0.71,0 -1.41,-0.18 -2.1,0.09 -0.46,0.182
-0.12,0.385 -0.38,0.609 -0.84,0.717 -4.68,0.09 -5.8,0.09 0.37,0.946
-0.32,2.053 -0.16,3.064 0.13,0.817 0.16,2.114 -1.14,1.836 0.42,1.246
-0.33,2.482 -0.1,3.74 -0.53,0 -3.97,0.114 -4.53,-0.209 -1.65,-0.955
-4.55,0.828 -5.11,0.878 -1.31,-0.213 -2.54,-0.151 -3.97,-0.144
-1.82,-0.38 -2.61,-4.163 -3.52,-5.497 -0.32,-0.47 -0.57,-0.807
-0.91,-1.274 -0.61,-0.864 -0.33,-1.484 -0.46,-2.405 -0.22,-1.639
-1.94,-2.716 -1.69,-4.456 0.22,-1.565 0,-2.871 -0.74,-3.785 -1.02,-1.277
-1,-1.747 -2.6,-1.67 -4.38,0.21 -8.73,0.382 -13.11,0.132 -3.54,-0.201
-7.68,0.384 -11.15,-0.285 -2.78,-0.536 -5.08,3.601
-6.72,-0.577\"/></svg>"}], "ideal": ["Democratic Republic of the
Congo"]}
{"input": [{"role": "system", "content": "I will provide you with the
svg with one shape, you will tell me which country it is the shape
of."}, {"role": "user", "content": "<svg><path
xmlns=\"http://www.w3.org/2000/svg\" d=\"m 1390.14,847.849 c 1.06,-0.165
1.89,-1.097 3.02,-0.896 0.97,0.171 1.84,0.902 2.86,0.707 2.12,-0.406
3.58,-2.884 6,-2.224 1.93,0.526 2.95,2.692 4.89,3.334 1.09,0.365
4.47,0.223 6.27,0.239 8.21,0.07 16.44,0.234 24.65,-0.1 2.17,-0.09
2.9,-0.247 3.93,1.67 1.3,2.439 3.25,1.9 5.6,2.158 3.07,0.337 6.34,0.197
9.22,1.207 1.11,0.388 2.1,0.528 3.08,-0.06 0.86,-0.524 1.69,-0.336
2.94,-0.03 1.26,0.308 2.01,0.1 2.85,-0.1 5.12,-1.189 10.92,-2.392
16.36,-3.42 1.05,-0.2 2.12,-0.682 3.21,-0.515 0.65,0.1 1.62,0.721
2.26,0.401 2.05,-1.02 2.99,1.138 4.34,2.064 -0.98,-0.256 -2.13,0.318
-3.06,0.681 -1.16,0.451 -1.5,2.182 -2.61,1.159 -1.79,-1.646 -5.29,3.747
-6.61,4.381 -0.64,-1.236 -1.33,-3.988 -3.16,-4.161 -2.36,-0.223
-5.3,0.967 -7.59,1.454 -2.71,0.573 -5.9,0.683 -8.59,1.185 l -1,31.899
-6.8,-0.1 -1.47,54.378 c 0.17,2.48 -1.96,1.44 -3.14,2.56 -0.59,0.56
-0.54,1.1 -1.71,1.5 -0.8,0.28 -1.17,0.61 -0.52,1.35 -1.79,0.53
-1.71,-0.14 -3.38,-0.39 -1.75,-0.26 -3.25,0.69 -5.32,0.24 -3.29,-0.7
-5.24,-1.92 -5.39,-2.52 -0.41,-1.68 0,-0.99 0,-2.32 -0.1,-0.53
-0.64,-0.39 -1.04,-0.8 -0.57,-0.6 -1.06,-1.86 -1.67,-1.48 -1.9,1.21
-1.37,3 -2.04,3.52 -0.94,0.73 -2.12,1.7 -3.11,0.46 -1.3,-1.64
-3.04,-2.94 -4.2,-4.69 -1.03,-1.56 -1.86,-3.228 -2.69,-4.895
-0.44,-0.885 -0.48,-1.837 -0.64,-2.792 -0.15,-0.986 -0.83,-1.5
-1.02,-2.398 -0.35,-1.647 0.38,-2.252 -0.84,-3.77 -0.48,-0.606
-0.32,-0.997 -0.3,-1.771 0,-1.251 -0.41,-2.334 -0.54,-3.554 -0.1,-0.869
0,-1.749 -0.27,-2.599 -0.36,-1.202 0.25,-2.365 0,-3.567 -0.4,-2.072
-1.39,-3.963 -2.14,-5.918 -0.85,-2.207 -0.21,-4.07 -0.43,-6.304
-0.15,-1.516 -0.38,-3.414 -0.24,-4.197 0.1,-0.367 0.99,-4.049 0.58,-3.96
-0.1,-1.983 -1.09,-3.925 -2.22,-5.516 -0.63,-0.895 -1.36,-1.729
-1.89,-2.693 -0.49,-0.886 -0.59,-1.97 -1.23,-2.777 -2.94,-3.719
-3.57,-8.234 -5.75,-12.264 -1.99,-3.694 -2.66,-8.768 -5.9,-11.674
-3.49,-3.125 -3.9,-7.688 -3.6,-12.097\"/></svg>"}], "ideal":
["Namibia"]}
{"input": [{"role": "system", "content": "I will provide you with the
svg with one shape, you will tell me which country it is the shape
of."}, {"role": "user", "content": "<svg><path
xmlns=\"http://www.w3.org/2000/svg\" d=\"m 1372.42,438.678 c
-0.96,-0.829 1.1,-1.805 1.63,-2.052 1.61,-0.745 2.47,-1.172 3.44,-2.748
0.78,-1.267 1.57,-1.885 1.26,-3.517 -0.26,-1.407 -0.93,-2.825
-0.78,-4.293 0.19,-2.013 2.64,-1.498 3.03,-2.941 0.42,-1.555 1.69,-2.357
2.99,-2.975 0.99,-0.475 4.23,-1.358 4.26,-2.736 0,-0.69 -0.67,-1.117
-0.59,-1.85 0.13,-1.342 0.18,-2.69 0.31,-4.032 1.29,0.9 3.03,1.355
4.42,2.209 1.46,0.896 3.11,1.201 4.81,1.015 1.71,-0.188 2.98,-1.275
4.74,-0.637 1.57,0.569 3.24,0.628 4.77,1.28 1.36,0.581 2.46,1.63
3.83,2.168 1.2,0.471 2.83,-0.02 3.9,0.719 1.26,0.873 1.5,2.371
1.74,3.773 0.31,1.794 1.02,3.224 2.41,4.429 2.53,2.176 5.65,1.666
8.69,2.217 3.04,0.554 7.38,1.939 9.83,3.917 1.95,1.582 3.75,4.253
6.55,4.002 3.22,-0.291 6.67,-3.134 7.39,-6.372 0.33,-1.495 -0.68,-2.658
-1.14,-4.005 -0.5,-1.485 -0.87,-3.192 -0.36,-4.729 0.93,-2.82
5.57,-6.318 8.52,-6.417 1.52,-0.05 2.41,-1.154 3.82,-1.262 1.44,-0.11
2.97,-0.136 4.38,0.208 1.64,0.401 3.07,1.195 4.63,1.805 1.85,0.723
1.36,0.974 1.45,2.59 0.1,1.309 2.18,1.586 3.13,1.656 1.83,0.138
3.01,0.967 4.7,1.457 1.68,0.487 3.44,-0.08 5.15,0.236 0.96,0.176
2.42,2.102 2.07,3.114 -0.36,1.068 -1.66,1.34 -1.84,2.542 -0.25,1.66
0.81,2.891 1.1,4.435 0.33,1.737 -0.79,3.275 -1.38,4.785 -0.63,1.602
1.01,3.505 1.29,5.163 0.46,2.826 0.96,5.498 1.14,8.396 l 1.78,75.281 c
-2.49,0 -4.98,0 -7.48,0 0.1,1.439 0,2.883 0.14,4.32 l -59.65,-33.761
-13.53,6.482 c -1.14,0.313 -2.55,-1.557 -3.21,-2.222 -2.8,-2.783
-5.83,-3.352 -9.55,-4.197 -1.32,-0.302 -3.06,-0.456 -4.24,-1.19
-0.94,-0.582 -1.38,-2.224 -1.77,-3.174 -1.14,-2.791 -2.53,-3.55
-5.26,-4.578 -0.91,-0.341 -1.77,-1.111 -2.77,-1.085 -0.97,0.02
-2.02,1.104 -2.93,0.118 -0.74,-0.8 -2.02,-2.856 -2.04,-3.963 0,-2.316
-0.26,-3.162 -1.54,-5.134 -0.98,-1.52 -4.24,-4.22 -2.84,-6.243
1.62,-2.334 4.1,-1.441 3.04,-5.269 -0.53,-1.915 -0.91,-3.386
-0.26,-5.329 0.56,-1.665 0.9,-3.039 0.28,-4.76 -0.64,-1.81 -0.14,-3.622
0,-5.461 0.19,-2.18 -0.13,-4.379 -0.86,-6.438 -0.62,-1.766 -1.53,-3.429
-2.62,-4.947\"/></svg>"}], "ideal": ["Libya"]}
{"input": [{"role": "system", "content": "I will provide you with the
svg with one shape, you will tell me which country it is the shape
of."}, {"role": "user", "content": "<svg><path
xmlns=\"http://www.w3.org/2000/svg\" d=\"m 1174.6,515.237 c 0.16,-0.371
0.67,-1.265 1.64,-1.315 l 27.88,-0.03 c 1.42,-0.747 0.44,-6.909
0.35,-9.281 -0.17,-2.384 -0.41,-3.937 1.5,-5.746 1.6,-1.514 1.54,-1.128
6.63,-3.207 l 1.12,-21.833 24.87,-0.291 0.34,-11.071 c 9.47,6.373
18.77,12.937 27.9,19.782 h -13.21 l 5.42,72.911 c 0.45,1.192 1.68,1.706
1.79,1.985 0.72,1.855 -0.23,2.415 -0.3,3.844 -0.1,1.675 -0.25,3.183
-0.74,3.363 l -15.88,0.02 c -9.03,0.312 -12.89,1.548 -13.69,-1.121
-0.39,2.416 -3.97,2.811 -5.73,2.11 -2.79,-1.107 -4.57,-0.64 -5.71,2.498
-0.65,-1.071 -1.59,-1.985 -2.56,-2.918 -1.15,-1.106 -2.25,-1.698
-2.86,-1.361 -2.29,1.269 0.9,7.651 -4.72,7.248 0,0.102 -1.51,-1.093
-1.92,-1.876 -0.51,-0.967 -1.09,-0.659 -2.06,-1.487 -1.05,-0.897
-0.98,-2.361 -1.84,-2.934 -2.31,-1.535 -1.4,-1.554 -1.61,-2.594
-0.27,-1.282 -1.57,-2.914 -2.22,-2.923 -3.4,-0.05 -3.64,-2.805
-5.84,-3.866 -1.12,-0.536 -2.08,-0.818 -3.58,-0.867 -2.33,-0.08
-3.14,2.203 -8.49,1.803 -1.13,-0.08 -0.98,-0.838 -1.94,-0.565
-0.93,0.342 -2.03,3.346 -2.4,4.133 0,-5.202 3.42,-9.445 3.92,-14.544
0.29,-3.07 -0.13,-5.666 -0.52,-8.672 -0.14,-1.084 -0.1,-2.273
-0.79,-3.192 -0.6,-0.802 -1.65,-1.372 -1.76,-2.464 0.8,0.25 1.69,-0.345
1.59,-1.224 -0.54,0.145 -0.97,0.552 -1.16,1.08 0.2,-1.044 1.04,-1.777
1.5,-2.694 0.29,-0.593 -0.14,-1.541 0.21,-1.938 1.57,-1.792 -0.83,-4.97
-1.42,-6.744 -0.24,0.428 -0.41,0.884 -0.5,1.368 -1.59,-1.202
-1.21,-3.688 -2.81,-4.896 -0.25,1.062 -0.64,2.092 -0.86,3.1635
-0.21,-1.3785 -0.1,-2.3295 0.46,-3.6545 z\"/></svg>"}], "ideal":
["Mauritania"]}
{"input": [{"role": "system", "content": "I will provide you with the
svg with one shape, you will tell me which country it is the shape
of."}, {"role": "user", "content": "<svg><path
xmlns=\"http://www.w3.org/2000/svg\" d=\"m 1702.78,554.229 c -2.43,-0.09
-1.06,-5.061 -3.46,-5.344 1.08,-1.714 -2.92,-7.033 -3.61,-8.909 l
-2.81,-6.489 c -7.13,1.401 -14.28,2.934 -21.3,3.881 -5.85,1.805
-8.8,4.713 -10.12,7.879 -1.22,1.824 -1.88,6.43 -4.8,6.253 -1.99,-0.12
-1.78,-3.107 -3.69,-2.881 -2.42,0.285 -4.39,0.24 -6.84,-0.104
-1.39,-0.195 -2.82,-1.184 -4.18,-1.184 -1.5,0 -3,0.145 -4.5,0.287
-1.84,0.174 -3.39,1 -5.3,0.895 -1.05,-0.06 -1.44,-1.224 -2.51,-1.357
-1.02,-0.128 -1.81,0.563 -2.24,1.429 -0.47,0.945 -0.62,2.091 -0.44,3.129
0.11,0.672 1.05,1.339 0.54,2.028 -0.48,0.653 -0.87,1.324 -1.36,2.004
-0.27,0.372 -0.6,0.665 -1.01,0.88 -0.96,0.48 -0.47,0.845 -0.27,1.898
0.31,1.668 -0.32,2.441 -0.61,3.961 -0.28,1.407 0.9,2.63 0.77,4.029
-0.27,-0.24 -1.7,-0.277 -1.46,0.282 0,-0.117 1.44,0.726 1.44,0.722
0.8,0.856 1.1,1.742 1.38,2.862 0.53,2.196 0.58,4.644 1.27,6.78
0.28,0.877 0.98,1.533 1.32,2.388 0.4,1.031 0,2.149 0,3.204 0,2.087
2.48,3.843 1.8,5.963 0.92,0.07 1.54,-0.446 2.47,-0.07 0.99,0.396
1.67,0.723 2.77,0.506 2.25,-0.447 3.26,-2.023 5.61,-0.79 -0.12,-0.64
0.56,-1.29 0.79,-0.359 0.39,-0.428 0.61,-0.925 0.93,-1.401 0.49,-0.753
1.3,-0.736 1.96,-1.238 1.48,-1.118 1.65,-2.245 3.69,-2.713 1.9,-0.437
3.91,-0.52 5.85,-0.342 1.14,0.104 3.06,-1.206 4.2,-1.53 1.71,-0.483
2.56,-1.96 4.06,-2.792 0.46,-0.255 1.11,-0.832 1.61,-0.981 0.55,0.02
1.07,0.149 1.57,0.391 0.57,0.03 1.12,-0.04 1.66,-0.203 3.63,-0.584
4.44,-4.338 7.7,-5.939 1.52,-0.744 2.86,-0.932 4.47,-1.215 2,-0.348
3.65,-1.686 5.62,-2.154 1.36,-0.326 2.74,-0.583 4.07,-1.061 1.32,-0.478
1.79,-1.532 2.91,-2.103 0.93,-0.474 2.93,-0.415 3.21,-1.675 0.34,-1.46
-0.68,-2.788 -0.15,-4.277 1.07,-3.009 4.74,-2.89
6.99,-4.536\"/></svg>"}], "ideal": ["Yemen"]}
  ```
</details>

---------

Co-authored-by: Lucas Fougeras <lucasfougeras@DIGITALCACTUS>

---
## [openai/evals](https://github.com/openai/evals)@[3dd0a24da8...](https://github.com/openai/evals/commit/3dd0a24da87c3eefd7f17424bdf124ae87698d89)
#### Tuesday 2023-05-23 22:57:21 by Pranav Gade

[eval] swap two words (#280)

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
Swap Words

### Eval description

This eval asks the model to swap two random words, so "chat gpt" should
become "gpt chat"

### What makes this a useful eval?

Robustly being able to swap words around seems like a foundational
capability the model should know, as moving things around probably helps
a lot with logic/math tasks if the model is thinking out aloud.

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
assistant."}, {"role": "user", "content": "Swap the words in this
string, write the output in double quotes and do not output anything
else:\"FRKLXk PrOQNNod\""}], "ideal": "\"PrOQNNod FRKLXk\""}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Swap the words in this
string, write the output in double quotes and do not output anything
else:\"hdJLcGtgv VaPHvqHUm\""}], "ideal": "\"VaPHvqHUm hdJLcGtgv\""}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Swap the words in this
string, write the output in double quotes and do not output anything
else:\"AZmgciwu ApPfVAelBGTGq\""}], "ideal": "\"ApPfVAelBGTGq
AZmgciwu\""}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Swap the words in this
string, write the output in double quotes and do not output anything
else:\"IQJeJQTxpKmYZ WppHdbeayUULw\""}], "ideal": "\"WppHdbeayUULw
IQJeJQTxpKmYZ\""}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Swap the words in this
string, write the output in double quotes and do not output anything
else:\"MuXvXQCQbtatHZy Yjnlus\""}], "ideal": "\"Yjnlus
MuXvXQCQbtatHZy\""}
  ```
</details>

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[2bca78d445...](https://github.com/cmss13-devs/cmss13/commit/2bca78d445030e89792dfadf9a0153a94c71195b)
#### Tuesday 2023-05-23 23:40:59 by c4xmaniac2

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

