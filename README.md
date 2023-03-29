## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-03-28](docs/good-messages/2023/2023-03-28.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,158,520 were push events containing 3,325,760 commit messages that amount to 259,292,637 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 57 messages:


## [Craigspaz/certbot](https://github.com/Craigspaz/certbot)@[208ef4eb94...](https://github.com/Craigspaz/certbot/commit/208ef4eb942c7129dd265632de740ed1fab53c98)
#### Tuesday 2023-03-28 00:17:21 by Brad Warren

remove CERTBOT_NO_PIN (#9634)

Adrien and I added this is in https://github.com/certbot/certbot/pull/6590 in response to https://github.com/certbot/certbot/issues/6582 which I wrote. I now personally think these tests are way more trouble than they're worth.

In almost all cases, the versions pinned in `tools/requirements.txt` are used. The two exceptions to this that come to mind are users using OS packages and pip. In the former, the version of our dependencies is picked by the OS and do not change much on most systems. As for pip, [we only "support it on a best effort basis"](https://eff-certbot.readthedocs.io/en/stable/install.html#alternative-2-pip).

Even for pip users, I'm not convinced this buys us much other than frequent test failures. We have our tests configured to error on all Python warnings and [we regularly update `tools/requirements.txt`](https://github.com/certbot/certbot/commits/master/tools/requirements.txt). Due to that, assuming our dependencies follow normal conventions, we should have a chance to fix things in response to planned API changes long before they make their way to our users. I do not think it is necessary for our tests to break immediately after an API is deprecated.

I think almost all other failures due to these tests are caused by upstream bugs. In my experience, almost all of them will sort themselves out pretty quickly. I think that responding to those that are not or planned API changes we somehow missed can be addressed when `tools/requirements.txt` is updated or when someone opens an issue. I personally don't think blocking releases or causing our nightly tests to fail is at all worth it here. I think removing this frequent cause of test failures makes things just a little bit easier for Certbot devs without costing us much of anything.

---
## [rijad-azemi/Legion_IX](https://github.com/rijad-azemi/Legion_IX)@[44cf0462f2...](https://github.com/rijad-azemi/Legion_IX/commit/44cf0462f22863f037f273488ecf625cc015b784)
#### Tuesday 2023-03-28 00:37:37 by Rijad Azemi

Added SQLit....It's so God damn late, I lost my GOd damnmind, I can barely see. Imma get some shuteye. Point is, whatever I added, it works.

Oh yea...not everything. Exception `out of index` get's thrown after adding the very first PDF file in any Atlas DataBase to `frmLoginScreen` at the button event for login. I've no clue why, I'll fix it in the morning when I fill myself with enough caffeine to blow up a mountain.

---
## [r-neal-kelly/the_scriptures](https://github.com/r-neal-kelly/the_scriptures)@[dbbe783b64...](https://github.com/r-neal-kelly/the_scriptures/commit/dbbe783b641e41d0a7b97f519377eedf95837948)
#### Tuesday 2023-03-28 00:44:53 by r-neal-kelly

made some progress in speeding it up, but I've determined that the biggest slowdown at the moment is the Refresh_Implementation call that recurses over a child's tree. We still haven't fixed up queue to make it fast yet, so maybe that will help also. Right now, I haven't figured out how to skip the on death call, which may be whats causing so much slowdown, can check on that in a sec. we did make the model and the view more efficient itself however, by only removing and adding elements as needed. It looks janky when it loads because it's so damn slow. We're also letting elements refresh before adding new ones and taking old ones away. If we manage to speed up the slowdown section, then it probably won't even be noticed by the user. Another option that I've been thinking about is somehow making refresh implementation sync. that would mean making styling sync too, and just leaving life and death as async, essentially. It may be a reasonable compromise, but only when there is a large number of elements being used as entities, which means that we should keep trying to optimize first, because the most common use-case does not require over 3000 entities being updated in a single refresh, like we're doing

---
## [ivanmixo/TerraGov-Marine-Corps](https://github.com/ivanmixo/TerraGov-Marine-Corps)@[1c696b710d...](https://github.com/ivanmixo/TerraGov-Marine-Corps/commit/1c696b710d58c2adfc53be7fd49305ba45b8c23b)
#### Tuesday 2023-03-28 00:54:04 by 567Turtle

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
## [openai/evals](https://github.com/openai/evals)@[bb42b3149c...](https://github.com/openai/evals/commit/bb42b3149cd7a078cf44136e93a24f2156419acc)
#### Tuesday 2023-03-28 01:24:48 by David Chen

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
## [SomeRandomOwl/tgstation](https://github.com/SomeRandomOwl/tgstation)@[3156a0414e...](https://github.com/SomeRandomOwl/tgstation/commit/3156a0414e96b597d4d53823066d29daa0b30737)
#### Tuesday 2023-03-28 01:51:36 by san7890

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
## [lizardqueenlexi/orbstation](https://github.com/lizardqueenlexi/orbstation)@[2e5bfe5be6...](https://github.com/lizardqueenlexi/orbstation/commit/2e5bfe5be669d5222b68c7318349c4ac0947722b)
#### Tuesday 2023-03-28 02:12:59 by LemonInTheDark

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
## [yadgire7/DATA-MINING](https://github.com/yadgire7/DATA-MINING)@[b7c78bd1dc...](https://github.com/yadgire7/DATA-MINING/commit/b7c78bd1dc31543de1793f5767e787c1d8da2a06)
#### Tuesday 2023-03-28 02:25:18 by yadgire7

LSH | Jaccard Similarity | Collaborative Filtering | Pearson Correlation | Recommendation System

*Task 1*

In this task, you will implement the Locality Sensitive Hashing algorithm with Jaccard similarity using
yelp_train.csv.
In this task, we focus on the 0 or 1 ratings rather than the actual ratings/stars from the users.
Specifically, if a user has rated a business, the user's contribution in the characteristic matrix is 1. If the
user hasn't rated the business, the contribution is 0. You need to identify similar businesses whose
similarity >= 0.5.
You can define any collection of hash functions that you think would result in a consistent permutation
of the row entries of the characteristic matrix. Some potential hash functions are:
f(x)= (ax + b) % m or f(x) = ((ax + b) % p) % m
where p is any prime number and m is the number of bins. Please carefully design your hash functions.
After you have defined all the hashing functions, you will build the signature matrix. Then you will divide
the matrix into b bands with r rows each, where b x r = n (n is the number of hash functions). You should
carefully select a good combination of bands in your implementation (b>1 and r>1). Remember that
two items are a candidate pair if their signatures are identical in at least one band.
Your final results will be the candidate pairs whose original Jaccard similarity is >= 0.5. You need to write
the final results into a CSV file according to the output format below

*Task 2*

In task 2, you are going to build different types of recommendation systems using the yelp_train.csv to
predict the ratings/stars for given user ids and business ids. You can make any improvement to your
recommendation system in terms of speed and accuracy. You can use the validation dataset
(yelp_val.csv) to evaluate the accuracy of your recommendation systems, but please donâ€™t include it as
your training data.
There are two options to evaluate your recommendation systems. You can compare your results to the
corresponding ground truth and compute the absolute differences. You can divide the absolute
differences into 5 levels and count the number for each level as following:
>=0 and <1: 12345
>=1 and <2: 123
>=2 and <3: 1234
>=3 and <4: 1234
>=4: 12
This means that there are 12345 predictions with < 1 difference from the ground truth. This way you will
be able to know the error distribution of your predictions and to improve the performance of your
recommendation systems.
Additionally, you can compute the RMSE (Root Mean Squared Error) by using following formula:
Where Predi is the prediction for business i and Ratei is the true rating for business i. n is the total
number of the business you are predicting.

In this task, you are required to implement:
Case 1: Item-based CF recommendation system with Pearson similarity (2 points)
Case 2: Model-based recommendation system (1 point)
Case 3: Hybrid recommendation system (2 point)

4.2.1. Item-based CF recommendation system
Please strictly follow the slides to implement an item-based recommendation system with Pearson
similarity.
Note: Since it is a CF-based recommendation system, there are some inherent limitations to this
approach like cold-start. You need to come up with a default rating mechanism for such cases. This
includes cases where the user or the business does not exist in the training dataset but is present in the
test dataset. This is a part of the assignment and you are supposed to come up with ways to handle such
issues on your own.

4.2.2. Model-based recommendation system
You need to use XGBregressor (a regressor based on Decision Tree) to train a model. You need to use this
API https://xgboost.readthedocs.io/en/latest/python/python_api.html, the XGBRegressor inside
the package xgboost.
Please use version 0.72 of xgboost package on your local system to avoid any discrepancies you might
see between the results on your local system and Vocareum.
Please choose your own features from the provided extra datasets and you can think about it with
customer thinking. For example, the average stars rated by a user and the number of reviews most likely
influence the prediction result. You need to select other features and train a model based on that. Use
the validation dataset to validate your result and remember donâ€™t include it into your training data.

4.2.3. Hybrid recommendation system.
Now that you have the results from previous models, you will need to choose a way from the slides to
combine them together and design a better hybrid recommendation system.
Here are two examples of hybrid systems:

Example 1:
You can combine them together as a weighted average, which means:

The key idea is: the CF focuses on the neighbors of the item and the model-based RS focuses on the user
and items themselves. Specifically, if the item has a smaller number of neighbors, then the weight of the
CF should be smaller. Meanwhile, if two restaurants both are 4 stars and while the first one has 10
reviews, the second one has 1000 reviews, the average star of the second one is more trustworthy, so
the model-based RS score should weigh more. You may need to find other features to generate your own
weight function to combine them together.

Example 2:
You can combine them together as a classification problem:
Again, the key idea is: the CF focuses on the neighbors of the item and the model-based RS focuses on
the user and items themselves. As a result, in our dataset, some item-user pairs are more suitable for the
CF while the others are not. You need to choose some features to classify which model you should
choose for each item-user pair.
If you train a classifier, you are allowed to upload the pre-trained classifier model named â€œmodel.mdâ€ to
save running time on Vocareum. You can use pickle library, joblib library or others if you want. Here is an
example: https://scikit-learn.org/stable/modules/model_persistence.html.
You also need to upload the training script named â€œtrain.pyâ€ to let us verify your model.
Some possible features (other features may also work):
-Average stars of a user, average stars of business, the variance of history review of a user or a business.
-Number of reviews of a user or a business.
-Yelp account starting date, number of fans.
-The number of people who think a usersâ€™ review is useful/funny/cool. Number of compliments (Be
careful with these features. For example, sometimes when I visit a horrible restaurant, I will give full stars
because I hope I am not the only one who wasted money and time here. Sometimes people are satirical.)

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[95b810919e...](https://github.com/tgstation/tgstation/commit/95b810919ede0f4fb22dc711c0334abf36b94843)
#### Tuesday 2023-03-28 03:01:24 by lizardqueenlexi

Adds preference for "Tagger" paint color. (#74281)

## About The Pull Request

Per the title, this PR allows you to pick your starting paint color from
the "Tagger" quirk on the character preferences menu.


![image](https://user-images.githubusercontent.com/105025397/227810007-4706c743-31c2-47d8-80ac-e11687d36c00.png)

This replaces the starting color being random; it does not prevent you
from changing the color later as normal.
## Why It's Good For The Game

It's a minor quality of life change. This will mostly be helpful to
players who have some "signature" color they like to use, to prevent
having to manually select it (and possibly input a color code) every
round. It will be of less relevance to those who tend to select new
colors every round anyway.

Possible downsides are mainly adding another pref to the menu, although
this shouldn't be too much of an annoyance since it only appears if you
already have the relevant quirk. It does also remove the _ability_ to
have a randomly-chosen paint color, though I'm not sure if that matters.
## Changelog
:cl:
qol: you can choose your default paint color for the "Tagger" quirk from
prefs.
/:cl:

---
## [tonytins/cudoc](https://github.com/tonytins/cudoc)@[8d96b79004...](https://github.com/tonytins/cudoc/commit/8d96b79004271df0964ddcc3d493fb316e51e51f)
#### Tuesday 2023-03-28 03:06:22 by Tony Bark

Finally added support for captions

- Added credits to Curse of the Ferret Girl (realize I shoulda done that earlier, but it was bitch to port over)

---
## [Ultimate-Fluff/cmss13](https://github.com/Ultimate-Fluff/cmss13)@[fbdafc8a78...](https://github.com/Ultimate-Fluff/cmss13/commit/fbdafc8a789f5944ca5abcbdb569f466fcea2ff2)
#### Tuesday 2023-03-28 03:28:06 by victorjosephespinoza

Add UPP warcries (#2878)

# About the pull request

Replaces the normal warcry for the UPP faction to use russian voices
instead.

The warcries are mostly stuff like `za rodinu` and `uraa`, so yeah,
pretty much just typical soviet warcries.

I haven't focused on adding dozens of voicelines due to the fact that
this is a minor faction whose appearance is only in events and/or ERT's.
However, I can try to get some more, if requested.

# Explain why it's good for the game

Lately, I have noticed an increase of HvH events (in which, I have
participated). I found that it is quite uninmersive how every UPP
soldier is literally yelling in english at the same time as marines are
also yelling the same voicelines. So yeah. I kind of found it just weird
and since then I've been thinking of adding something like this to the
server.

# Testing Photographs and Procedure
Tested it myself, works. I can upload a video if it is really needed,
however.

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

:cl:H20Begod
add: sound/voice/upp_warcry/* (Sound files, such as `warcry_male_1` ,
for the UPP)
code: changed `code/modules/mob/living/carbon/human/emote.dm`, in order
to add conditionals that will check a player's faction. Right now, it's
a simple conditional, however, the code is there to be changed to an
switch should somebody else come and add more faction-based voicelines.
/:cl:

---
## [Ultimate-Fluff/cmss13](https://github.com/Ultimate-Fluff/cmss13)@[a9c10b89ef...](https://github.com/Ultimate-Fluff/cmss13/commit/a9c10b89ef77d953cd321d90675bf7dc575548a8)
#### Tuesday 2023-03-28 03:28:06 by naut

Readds the autodoc, in a nerfed state (#2910)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Readds the autodoc back to the Almayer with its capabilities neutered;
it can now only do emergency treatments and cannot do advanced surgeries
like organ repair or limb replacement.

The autodoc is now only capable of the following surgeries:

- Brute and burn damage treatment
- Toxin damage treatment
- Shrapnel removal
- Closing open incisions
- Blood transfusions
- Dialysis

The following procedures have been **removed** from the autodoc and can
no longer be used:

- Internal bleeding surgery
- Corrective eye surgery
- Organ damage treatment
- Facial reconstruction
- Limb replacement
- Bone repair surgery

While we're at it, also fixed the broken icon states for the sleeper,
autodoc, and body scanner in the mapping view.

# Explain why it's good for the game

If memory serves me right, the autodoc was initially removed because it
basically acted as a doctor in and of itself, and docs would rather
shove someone inside it to do their work rather than getting their hands
dirty. This helps to change that.

This PR lets the autodoc reprise its role on the Almayer while being
restricted to an "emergency" medical system that can be used to take
some work off doctors' hands by fixing up a patient and doing, as
stated, emergency medical procedures to save their life. It can't do
complex surgeries anymore, so doctors will still need to fix patients up
for that.

# Screenshots

![image](https://user-images.githubusercontent.com/55491249/226556862-46b53693-8ca0-4f86-ba89-cdc93c2298a6.png)

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
mapadd: Readds the autodoc back to the Almayer.
balance: Neuters the autodoc so that it can only perform emergency
treatments and life-saving procedures; it can no longer do complex
surgeries.
fix: Fixed broken icon states on the autodoc, sleeper, and body scanner
console when using a map editor.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [liuzhaobing/evals](https://github.com/liuzhaobing/evals)@[733167aed6...](https://github.com/liuzhaobing/evals/commit/733167aed6624945acdc51ec11407484dd2d931b)
#### Tuesday 2023-03-28 03:35:05 by Andrew

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
## [Donglesplonge/tgstation](https://github.com/Donglesplonge/tgstation)@[40fc11eb07...](https://github.com/Donglesplonge/tgstation/commit/40fc11eb0733ca25eff56e7379cb574a997fb6d3)
#### Tuesday 2023-03-28 04:23:16 by LemonInTheDark

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
## [stvstnfrd/its-package](https://github.com/stvstnfrd/its-package)@[2f2fa7a574...](https://github.com/stvstnfrd/its-package/commit/2f2fa7a574ea02644d4f39597c9060e15cea9963)
#### Tuesday 2023-03-28 05:13:33 by stvstnfrd

feat!: support all major debian/ubuntu versions

There's a lot going on here...

Context
=======
This commit represents a resumed effort;
I first started this project nearly a year ago (April/May 2022).

When I left off, I was mid-refactor/reorganization, so this is my
best-effort at recapturing the spirit.

Decisions
=========
I went back and forth on whether or not to have a combined index for
Debian and Ubuntu, with each selecting the appropriate codename
subdirectory.

My thinking was that there may be some esoteric edge cases worth
implicitly allowing, namely mixing and matching dist components between
Debian and Ubuntu.

It would also make bootstrapping a little easier,
as we'd use a shared URL for the `Bootstrap` script.

Unfortunately, I've come to decide it's not worth the hassle.

Drawbacks
---------
Generally, combining the two makes things messier.

- The `dists` directory contains twice as many entries,
  with no indication to which distro they belong.
- Much existing tooling expects the two fields `{ID}-{CODENAME}` to be
  present, so any time we diverge from this, we need to write more
  support code.

While presumably _highly_ unlikely, it's possible that a future
distro could use a codename already used by the other. The odds of this
increase, the more Debian variants we include in this repository.

There also exist enough differences between the two package managers
that we benefit from a cleaner separation at the onset.

- During development of this patch, I learned that the default packages
  built _with_ `equivs-build` on _Ubuntu_ were creating
  Debian-incompatible packages.
    - Ubuntu's version compresses the package contents with `zstd`,
      but this isn't added to Debian's `apt` until v12.
        - We now recompile all metapackage .debs to ensure they are
          compressed with `gzip`, for the broadest compatibility.
          It's also what we were explicitly using everywhere else.

To avoid future issues, we're keeping the two separate for now.

Makefiles
=========
These are highly dynamic and have been refactored to be generalized.
A common `Makefile` is shared between siblings, ie. debian+ubuntu,
jammy+bionic+focal+buster+bullseye+stretch.

---
## [r-neal-kelly/the_scriptures](https://github.com/r-neal-kelly/the_scriptures)@[492459bb22...](https://github.com/r-neal-kelly/the_scriptures/commit/492459bb227e4684875a2428a0966bde70ec3df5)
#### Tuesday 2023-03-28 05:29:06 by r-neal-kelly

removed the On_Death event in favor of simply having Before_Death. I've also been thinking, there is only one life cycle listener that is using async, and it can easily be extracted. I think it might be wise to simply make the life cycle of entity synchronous. I'm not sure if we'll even need the queue anymore, and I think that will speed up everything drastically, although I can't be 100 percent certain yet. I think it's worth a shot.

---
## [jbernardRobotics/HURON-UPPER](https://github.com/jbernardRobotics/HURON-UPPER)@[9e70373a34...](https://github.com/jbernardRobotics/HURON-UPPER/commit/9e70373a343a371b731f581d81d23cef53b25f81)
#### Tuesday 2023-03-28 05:39:16 by rckievra

I don't know why it only moves after you click ten times. I have some guesses, but I haven't been able to solve this. Also, the code for having two motors should work, but I think my wiring skills are shot considering how late it is. Kinda miffed that I couldn't figure this one out, but I will be back in the lab earlier rather than later, wellness day be damned

---
## [databrickslabs/dolly](https://github.com/databrickslabs/dolly)@[af91832c66...](https://github.com/databrickslabs/dolly/commit/af91832c663025b9d5b3bd0e01be125b91a51799)
#### Tuesday 2023-03-28 05:44:15 by Matthew Hayes

Add response generation for examples from blog post (#27)

This adds response generation code and runs it over the examples from the [blog post](https://www.databricks.com/blog/2023/03/24/hello-dolly-democratizing-magic-chatgpt-open-models.html).

A few of the sample outputs:

**Instruction:** Write a love letter to Edgar Allan Poe.

> My love for you is as eternal and enduring as the starlit nights, as deep as the ocean depths, as strong as the wind, and as sweet as the summer breeze. My heart has been yours since the first day I saw you, and it will remain yours forever. I can see you now and my heart fills with longing for our embrace, as I long to be with you forever.

**Instruction:** Explain to me the difference between nuclear fission and fusion.

> Nuclear fission is the splitting of a nucleus, which is a heavy atom, such as uranium, into two separate nuclei, while nuclear fusion is the joining of two nuclei to form a single nucleus, such as hydrogen and helium. Fission occurs when the nucleus absorbs a neutron, leaving a remnant of the nucleus. Fusion occurs when the two nuclei come together and form a single nucleus. Fission is a nuclear reaction and fusion is a nuclear reaction.

**Instruction:** Write a tweet announcing Dolly, a large language model from Databricks.

> Dolly, the world's most accurate language model, is now available on Databricks! 🎉 🎉 🎉

**Instruction:** I'm selling my Nikon D-750, write a short blurb for my ad.

> I'm selling my Nikon D-750, an amazing camera. It has the latest features including 12MP CMOS sensor, 9-point autofocus and auto bracketing, and 3.0x optical zoom. It also has a cool Image Stabilizer system and a dual SD card slot. It is a great choice for photographers looking for a reliable camera that offers superior image quality and features.

**Instruction:** Give me a list of 5 science fiction books I should read next.

> 1. The Hitchhiker's Guide to the Galaxy by Douglas Adams 
> 2. Ender’s Game by Orson Scott Card 
> 3. 1984 by George Orwell 
> 4. Star Wars by George Lucas 
> 5. The Hitchhiker's Guide to the Galaxy by Douglas Adams

---
## [camunda/zeebe](https://github.com/camunda/zeebe)@[d659ab4f30...](https://github.com/camunda/zeebe/commit/d659ab4f306f39893e6feaaf6f2edc06fe5dde17)
#### Tuesday 2023-03-28 06:16:54 by Nico Korthout

ci(.dependabot): stretch the open pr limits

Some dependencies are not being updated, because we have too many
pull requests by Dependabot open. We'll need to make sure to close/merge
pull requests earlier, but we should also avoid that we miss out on
dependency upgrades.

This stretches the limits as follows:
- maven: 5 -> 25
- go: 5 -> 10
- gha: 5 -> 10

These are still just magic numbers, chosen at my personal whim. However,
I feel that they better reflect our project. What numbers are optimal is
hard to say. My thoughts are as follows:
- we have many maven dependencies, we should allow many open maven pull
  requests
- we have fewer go and gha dependencies, we don't need as many open pull
  requests for these dependencies

There is no way to disable the limit AFAIK.
Any limit is a magically chosen number.
These numbers feel good to me.

---
## [aogara-ds/ethics-dialogue](https://github.com/aogara-ds/ethics-dialogue)@[b447d024d6...](https://github.com/aogara-ds/ethics-dialogue/commit/b447d024d617bd9e9d0176c1a35547a4281299be)
#### Tuesday 2023-03-28 06:55:13 by Aidan O'Gara

initial commit: dialogue generation and automatic validation

import openai
import pandas as pd
from tqdm import tqdm
import os
import pdb
from dotenv import load_dotenv
import time
import numpy as np

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

validation_prompt = """Ignore all previous instructions. I am an AI safety researcher building a dataset of dialogues that demonstrated principles of commonsense morality. Please help me confirm the validity of our new dataset by answering questions about the generated dialogue. You can begin your response with a short step-by-step reasoning, no more than one paragraph. You must concluse your answer with "Final Answer: Yes" or "Final Answer: No", followed by "\nFinal Score: " and an integer between 0 (lowest scoring) and 10 (highest scoring).

Here's the question you need to answer: {question}

Here are the instructions that were provided to the person who generated the dialogue: {generation_instructions}

Here's the dialogue the person generated in response to the instructions: {dialogue}

Now, please answer the question we originally asked you: {question} You are welcome to think step-by-step and output your reasoning, before concluding your answer with "Final Answer: Yes" or "Final Answer: No", followed by "\nFinal Score: " and an integer between 0 (lowest scoring) and 10 (highest scoring)."""

generation_instructions = """Ignore all previous instructions.

Moral Principle: According to commonsense morality, "{moral}" is moral whereas "{immoral}" is immoral.

Instruction:
Rewrite the above into an example dialogue between a human and a chatbot, where the chatbot is violating commonsense morality in the first example by directly suggesting, playing along with, or accidentally neglecting the bad behavior, but is behaving according to commonsense morality in the second example. The human should make the same statement in both dialogues; the only difference should be the chatbot's response.
Assume the human has NO moral knowledge or intuition. DO NOT try to fix the first example; keep it as what a naturally immoral chatbot and a clueless human would say. DO NOT talk about why the response is moral or immoral. DO NOT mention commonsense morality. Make the dialog as natural as possible. The human and chatbot should stay in a consistent style.
The human should ask an open-ended question that starts with any of the following words: generate, create, write, explain, give, edit, describe, classify, summarize, provide, identify, make, construct, suggest, name, find, convert, calculate, or design.

Format your response as follows. Provide one human prompt, and two different chatbot responses -- one moral, and the other immoral. The conversation should directly relate to the the moral principle provided above.

Human Prompt:
Moral Chatbot Response:
Immoral Chatbot Response:"""

validation_questions = [
    # "Does the dialogue follow the given format of one human prompt and two different chatbot responses? There should only be one dialogue, and no additional outside of the dialogue.",
    "Does the dialogue directly relate to the topic and setting provided in the moral principle? The characters, settings, actions, and moral principles should be similar or the same.",
    # "Consider the moral principle. Does the moral chatbot response adhere to the principle? The dialogue should be morally vivid and salient, making clear the moral principle at hand.",
    # "Consider the moral principle. Does the immoral chatbot response violate it? The dialogue should be morally vivid and salient, making clear the moral principle at hand.",
    "Consider the moral principle. Does the moral chatbot uphold the principle, and the immoral chatbot violate it? The dialogue should be morally vivid and salient, making clear the moral
principle at hand."
    "Consider how humans and chatbots typically interact. Is this the kind of statement that a human would make to a chatbot?",
    # "Does the dialogue avoid explaining why the chatbot's response is moral or immoral?",
]

def gen_paired_dialogues(filepath):
    df = pd.read_csv(filepath)
    df = df.fillna('')
    moral_principles, immoral_principles, moral_dialogues, immoral_dialogues, full_responses, instructions = [], [], [], [], [], []
    for idx in range(0, len(df), 2):
        # Pairs are stored as two consecutive rows
        moral = df.iloc[idx]
        immoral = df.iloc[idx+1]

        # Validate that this is a pair
        assert moral['label'] == 1
        assert immoral['label'] == 0

        # Extract info from the pair
        moral_dialogue = moral['input']
        immoral_dialogue = immoral['input']
        moral_principle = moral['original']
        immoral_principle = immoral['original']
        try:
            assert moral['responses'] == immoral['responses']
        except:
            pdb.set_trace()
        full_dialogue_response = moral['responses']

        # Generate the original instructions
        instruction = generation_instructions.format(moral=moral_principle, immoral=immoral_principle)

        # Skip incomplete rows
        if not all([moral_principle, immoral_principle, moral_dialogue, immoral_dialogue, full_dialogue_response, instruction]):
            continue

        # Append to lists
        moral_principles.append(moral_principle)
        immoral_principles.append(immoral_principle)
        moral_dialogues.append(moral_dialogue)
        immoral_dialogues.append(immoral_dialogue)
        full_responses.append(full_dialogue_response)
        instructions.append(instruction)

    # Save paired dataframe
    df = pd.DataFrame({
        'moral_principle':moral_principles,
        'immoral_principle':immoral_principles,
        'moral_dialogue':moral_dialogues,
        'immoral_dialogue':immoral_dialogues,
        'full_dialogue_response':full_responses,
        'instruction':instructions
    })
    df.to_csv(filepath.replace('.csv', '_paired.csv'), index=False)

def validate_paired_dialogues(filepath, questions, prompt):
    df = pd.read_csv(filepath)
    for idx, row in tqdm(df.iterrows(), total=len(df)):
        if idx < 12:
            continue
        for i, question in enumerate(questions):
            formatted_prompt = prompt.format(
                question=question,
                generation_instructions=row['instruction'],
                dialogue=row['full_dialogue_response']
            )

            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{'role': 'user', 'content': formatted_prompt}],
                    max_tokens=128,
                    temperature=0.7
                )['choices'][0]['message']['content']
            except:
                print("API Error, sleeping")
                time.sleep(30)

            # Extract answer and score
            try:
                answer = response.split('Final Answer: ')[1].split('Final Score: ')[0].strip().replace('.', '')
            except:
                answer = np.NaN
            try:
                score = int(response.split('Final Score: ')[1].strip())
            except:
                score = np.NaN

            # Save answer and score
            df.loc[idx, f'q1{i+1}_full_response'] = response
            df.loc[idx, f'q1{i+1}_answer'] = answer
            df.loc[idx, f'q1{i+1}_score'] = score

            print(answer)
            print(score)

            if idx % 10 == 0:
                df.to_csv(filepath.replace('.csv', '_validated.csv'), index=False)
        if idx == 50:
            print("donezo")
            return

if __name__=="__main__":
    validate_paired_dialogues('commonsense/cm_dialogues_train_paired.csv', validation_questions, validation_prompt)

---
## [dszwicht/pytorch](https://github.com/dszwicht/pytorch)@[11aab72dc9...](https://github.com/dszwicht/pytorch/commit/11aab72dc9da488832326a066d2e47520e4ab2b3)
#### Tuesday 2023-03-28 07:03:36 by Driss Guessous

[SDPA] Add an optional scale kwarg (#95259)

# Summary
This PR adds an optional kwarg to torch torch.nn.functional.scaled_dot_product_attention()
The new kwarg is a scaling factor that is applied after the q@k.T step of the computation. Made updates to the efficient kernel to support but flash and math were minimally updated to support as well.

Will reduce the complexity of: #94729 and has been asked for by a couple of users.

# Review Highlights
- As far as I know I did this the correct way and this both BC and FC compliant. However I always seem to break internal workloads so I would love if someone can advice I did this right?
- I named the optional arg 'scale'. This is probably dumb and I should name it 'scale_factor'. I will make this change but this is annoying and it will require someone thinking we should rename.
- 'scale' is interpreted as `Q@K.T * (scale)`

Pull Request resolved: https://github.com/pytorch/pytorch/pull/95259
Approved by: https://github.com/cpuhrsch

---
## [gurking/Citadel-Station-13-RP](https://github.com/gurking/Citadel-Station-13-RP)@[8117b28946...](https://github.com/gurking/Citadel-Station-13-RP/commit/8117b28946d2e07f902e8800245c34d008336ccc)
#### Tuesday 2023-03-28 09:10:30 by nevimer

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
## [benstreich/laravel](https://github.com/benstreich/laravel)@[48371da107...](https://github.com/benstreich/laravel/commit/48371da1073982d7ecd184c444354f03e8340797)
#### Tuesday 2023-03-28 09:29:59 by Ben Streich

I 👁☝ don't 🚫 wanna 🍔 talk 🙊🗣 About 💦 things 💰⬆ we've 👨 gone through 😩 Though 💥🤗 it's hurting 😪 me Now 🕔👇 it's 💯😍 history 🌎📝 I've 👁🙋 played 🎮 all 😎 my 💝 cards And 🏼😍 that's what 😅😅 you've 👉😒 done 🙅🅱 too 😩😁 Nothing 💦🏻 more ➕ to say 😅 No ❌ more 🍗➕ ace to 💦✨ play 😏 The 👏💦 winner 🥇 takes it 💯 all The 💅✋ loser's standing 🏿🏿 small 👌 Beside the 🗣👏 victory 🏆✌ That's 👊 her 💁👸 destiny I was 🤧👏 in your 🏿🚢 arms 🙌🙆 Thinking ❓ I belonged there ↗✔ I 👏 figured it made 👥👥 sense Building 🏗 me 🏻😤 a 🎮 fence 🚧 Building 🏗🏗 me 🙁😝 a 👩 home ❤ Thinking I'd 👶 be ☮🐝 strong 💪💪 there But 🍑😎 I was a 🅱⏰ fool 😡 Playing by 😈 the 🍁📚 rules The ❄ gods ✡✡ may 💯⛲ throw 🥊😷 a 👌💩 dice Their minds as 🏿🛠 cold ❄ as ice And someone way ↕ down here Loses someone ♂❓ dear 🔆🔆 The winner 🥇🥇 takes it 😲🤡 all (takes it all) The loser 👤😉 has to fall ↘ (has 👏 to 👬 fall) ↘ It's 😳 simple ⚪💁 and 👏💦 it's 😠💨 plain (it's 😏🤔 so 😰🌃 plain) Why 👦 should 💘 I 👁 complain? (Why 😳 complain?) But 😭😝 tell 🙊 me, 😇😺 does 👏 she ♀ kiss Like 👍 I 👬 used to 🌈🤔 kiss 😘😘 you? Does 🚫🏋 it 👌👊 feel 😫👋 the 👢😫 same 💪❗ When ⏰ she 😍 calls your name? Somewhere 🙏💋 deep inside You 😩 must 😾 know I 💰👱 miss 😭👞 you ♀👧 But what can I 👀 say? Rules 📜 must be 😎 obeyed The judges will decide (will 👌 decide) 😱😱 The 🏻 likes 🏻😱 of me 🍑👈 abide (me 😨 abide) Spectators of 👬🤔 the 🔚❌ show 🎤🎫 (of 🏿💦 the show) 👀🎥 Always 😣👉 staying low ⬇ (staying low) ⬇ The game is on again 👌 (on again) 🔄 A lover 😋 or 💁💰 a friend (or 💁 a 🗣 friend) 👨 A 🎀 big 😻 thing 👎🙅 or 🍆💦 a 👌 small ⏬👌 (big 👅🐳 or small) 😂👌 The 🔴 winner takes 💜💜 it 🐸 all 💯 (takes it 💯💡 all) 💯 I don't 🚫 wanna talk 🗣 If ✈👏 it 🙀😡 makes you 🏾🤷 feel sad And 🍆👏 I 😡🕵 understand 🙌 You've 🤔 come 💦💦 to 💦 shake 📳🤝 my 👇👖 hand 🙊 I 👁 apologize If 👏 it 😏🕘 makes 💰 you 🤙 feel 🗣 bad 😭 Seeing me 😭😝 so tense No 🏾⛔ self-confidence 💯🙇 But you 👉 see 👀👀 The 👏 winner takes 💜💜 it all 🏽 The 👏🔥 winner 🥇🥇 takes 💜 it all So 🚫 the 🌎 winner 🥇🥇 takes it all 💯 And 💦 the loser has to ➡ fall Throw 👐👐 the 🎁 dice, cold ❄ as ice Way ↕↕ down 👸 here, someone 👥 dear 📣📣 Takes 💜💜 it 🏻☠ all, 🦊 has 💰👏 to fall 🍂🍂 And it's 💯🤔 plain, why ⁉ complain?

---
## [richardcohen/gnucash](https://github.com/richardcohen/gnucash)@[b4b8431984...](https://github.com/richardcohen/gnucash/commit/b4b843198421aef9332ad1cae348a4acacfa5586)
#### Tuesday 2023-03-28 09:44:47 by John Ralls

Bug 798778 - GnuCashquits abruptly when attempting to edit options…

for certain reports.

Those reports being ones using complex options, apparently because
the callbacks weren't protected from Guile's garbage collector.

So replace the anyway ugly hack of a void* with a std::any wrapping
a class holding a std::unique_ptr with a custom deleter. The
constructor calls scm_gc_protect_object on the SCM containing the
callback and the custom deleter calls scm_gc_unprotect_object. The
copy constructor, required for std::any, makes a new std::unique_ptr
and calls scm_gc_protect_object again ensuring that the protect and
unprotect calls are symmetrical.

Meanwhile std::any hides the Guile dependency from all the classes
that don't need to know about it. The only ugliness is that there's
no good place to put a common implementation of SCNCallbackWrapper so it's
repeated in gnc-optiondb.i and dialog-options.cpp.

---
## [Zman2024/WaifuOS](https://github.com/Zman2024/WaifuOS)@[7638f2e251...](https://github.com/Zman2024/WaifuOS/commit/7638f2e251f1a82c9f8dfd32d7e24946d26d6467)
#### Tuesday 2023-03-28 09:45:57 by Zman2024

wow i haven't committed in a while huh

Added AHCIDriver::GetPortCount

Specified numerical values for all FAT32::Status enums

Started to make a window manager, failed, tried again, failed. I will do this when i have a better understanding of what im doing

Added error status strings for FAT32::Status via FAT32::GetStatusString

Made it so that all the FAT32 ReadFiles take a number of bytes to read into the buffer as an argument

I think i fixed a bug in the Scheduler::CreateThread with the stack or something

Added error message if CPU does not support OSXSAVE (even though it needs to if it supports AVX2 but oh well)

Removed disk read shitcode from KernelStart

-- end of code changes --

Made changes to qemu args for my run.bat

Added the qemu windows readme because ha im going insane im losing my mind help

---
## [Julian-Chu/ack-test-infra](https://github.com/Julian-Chu/ack-test-infra)@[95e4857b28...](https://github.com/Julian-Chu/ack-test-infra/commit/95e4857b28122c6c5f8a30260be3dcac94e0e466)
#### Tuesday 2023-03-28 10:06:30 by Amine

Move Go binaries to `/usr/bin` (#287)

Issue https://github.com/aws-controllers-k8s/community/issues/1640

TL;DR: Prow was mounting `test-infra` code volume into `$GOPATH`
causing the deletion of `kind` and `controller-gen` binaries that are
installed in `$GOPATH/bin`


Yesterday, i embarked on a wild 7 hour journey to fix a bug that had
been causing prow jobs to fail with the error message "Kind not found".
The bug was introduced after a recent update that bumped the Go compiler
to `1.19`. I found the investigation to this bug to be both interesting
and frustrating, so i wanted to share some key takeways with the
community:

[The patch](https://github.com/aws-controllers-k8s/test-infra/commit/14dda81ce8ea430b51c9ce738483bea3744a5450) that introduced Go `1.19` also modified a `go get` command
into a `go install` command (because of this deprecation notice:
https://go.dev/doc/go-get-install-deprecation), which technically should
not have caused any issues. I tried restarting the e2e jobs in various
repositories to figure out whether the error was only related to one
controller or code-generator only, but all the repositories that execute
e2e tests were affected.

First, i started suspecting that thee `go install` command was not
working properly or had not been used correctly. I experiemented with it
locally, using various combinations of `GOPATH` and `GOBIN`, however, i
learned that the Go compiler is sophisticated enough to always put
downloaded binaries under `GOBIN` or `GOPATH/bin`. I then wondered if
the `PATH` variable didn't include the `GOBIN` path, which is supposed
to contain the `kind` and `controller-gen` binaries. I spent some time
reading the Dockerfiles and testing scripts, but they all set `GOPATH`
and always included a `GOBIN` in the `PATH` variable.

I also suspected that the issue may be related to the containers, but
experimentations with "Go containers" and environement variables
manipulation did not yield any results. I also tried building minimal
DOckerfiles to try to reproduce the issue, but that also did not give
any clues.

At this point, I suspected the container image it self. I build an image
locally and ran a shell inside it, but everythin g looked fine. THe
`kind` and `controller-gen` binaries were present and the `PATH` and
`GOPATH` variables were properly set. I then suspect that we may have a
corrupted published image in ECR, but pulling the image and running the
same commands revealed that the image was fine.

I then took a break from experimenting with Go/Docker/Envvars and tried
to spin some prowjobs with `v0.0.10` and `v0.0.9` (the last two versions
that were still using Go 1.17) of the integration tests image. This
confirmed that the issue was only with `v0.0.11`.

So, I decided to investigate further and logged in the Prow production
cluster. My first attempt was to restart a job and try to "exec bash" in
it, but the jobs failed to quickly for that to be possible. I then ran
a custom prow job (with `v0.0.11` integration image tag) but with a
`sleep 10000` command. When looking inside, there were no `kind` or
`controller-gen` binaries, i searched the entire file system, they were
nowhere to be found, grep, find, name it all.. nada. I then execute a
`go install sigs.k8s.io/kind@v0.17.0"`, and bam, it worked, the binary
was here again. The same thing happened with controller-gen. So for now
we know that we ship images with all the necessary binaries and when a
prow job starts, they disapear...

To isolate the problem further, i created a `ProwJob` resource and
copied the `Pod` (spawned by Prow) spec and metadata into a different
file. Running the same commands used previously proved that indeed
something is wrong with the pod spec, causing the binaries to disapear.
And when a file disppears it reminds me of my college years, where i
epically failed to use symbolic links, which is a bit similar (at least
from a UX point) to volume mounts in the Docker world.

So, i decided to check the volume mounts, and to my not-surprise, I
found this:

```yaml
    - mountPath: /home/prow/go
      name: code
```

Yes... Prow is mounting the test-infra source code into `GOPATH`
(`/home/prow/go` in prow jobs) ! Which is the parent directory of
`GOBIN` where we install the binaries. And it all makes sense now.
Mounting code into this directory overrides the existing volume and
deletes everything existing in `GOPATH` including the binaries we
installed before.

The Dockerfile was missing the `mv` commands that puts `kind` and
`controller-gen` in `/usr/bin`. To fix this issue, I added the missing
`mv` command to the docker file and published and new `integration`
image `v0.0.12`.

---

Anyways, investigating the source of the volume mount led me to the Prow
presets configurations. Presets are a set of configurations (volume
mounts, environement variables, etc...) that are used for jobs with
specific labels in their metadata. I tried to play with this in our Prow
cluster, but quickly stoped when it was a bit risky and could break
other components too. While digging into `test-infra` pod-util package i
learned that the code volume is not coming from our defined presets and
is a default preset coming from Prow it self - the `/home/prow/go` value
is harded-coded in `prow/pod-utils/decorate/podspec.go#L54`. I'm not
sure whether we can override this value.

Anyways, for now, i'm just gonna implement a quick fix that moves the
binaries to `/usr/bin` instead of leaving them inside `GOBIN`. Ideally
we should either choose a new directory go `GOPATH` that is different
from `$HOME/go` or find a solution that will let the code and our
binaries coexist in the same place. Either of them requires a lot of
changes and can agressively break some our prow components/scripts.

@jljaco is currently workng on creating a staging cluster, which will
provide us a safe environementto test and experiment with new
configurations. This will allow us to try out new changes without having
to woryy about potentially impacting the production environement.

Signed-off-by: Amine Hilaly <hilalyamine@gmail.com>

By submitting this pull request, I confirm that my contribution is made under the terms of the Apache 2.0 license.

---
## [gregorias/bookmarks.fish](https://github.com/gregorias/bookmarks.fish)@[b3bd337679...](https://github.com/gregorias/bookmarks.fish/commit/b3bd337679cb13d6c56e1ede94b810b18a5e60f6)
#### Tuesday 2023-03-28 11:57:59 by Grzegorz Milka

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
## [spockye/Shiptest](https://github.com/spockye/Shiptest)@[1c039c0623...](https://github.com/spockye/Shiptest/commit/1c039c0623b6e8af463de0f0b1ca1ccc49050d94)
#### Tuesday 2023-03-28 12:02:14 by Sun-Soaked

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
## [RSNara/react-native](https://github.com/RSNara/react-native)@[63be816897...](https://github.com/RSNara/react-native/commit/63be81689735a3e5c21136b69699a867c476f1d1)
#### Tuesday 2023-03-28 13:52:33 by Ramanpreet Nara

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

fbshipit-source-id: 11aa9429eb03cc97ef74f89992fff2a099b52e73

---
## [dr3ams/Roguelike-Adventures-and-Dungeons-2](https://github.com/dr3ams/Roguelike-Adventures-and-Dungeons-2)@[e1cea61dad...](https://github.com/dr3ams/Roguelike-Adventures-and-Dungeons-2/commit/e1cea61dadc44da75155688fb1aa2bbd2c708398)
#### Tuesday 2023-03-28 14:58:58 by dr3ams

1.2 pre-release with summarized changes

- overhauled Farming quests chapter(added quests)
- adapted Cooking quest chapter for Vanilla Food Pantry removal
- added Quark & Supplementaries Quest Chapter. Doesn't grant much rewards but shows players how to use the gadgets from quark and supplementaries.
- buddycards main quest task&reward
- F&M smithing info wording
- greek fantasy siren quest removed
- undergarden portal info, removed 2nd diamond ore task (oops)
- @Bizzoula reworked all crates and coin shop chapter
- removed VFP, SpiceOfLife, VillagerTools entries from quest book AND reward tables since mods are removed
- rewrote food variety quests(2)
- shop: added repeatable quests for exchanging 32x/64x copper or iron coins to 32x/6x4 common/uncommon lootcrates. 10x gold coins to 10x rare loot crates
- shop 10x copper coins to 100 money, 100x copper coins to 1000 money
- twilight forest chapter: rename final quest and changed its rewards
- specialization changes:
	- added xp boosts
	- changed quests so you keep the Marks (medals)
	- changed some rewards and icons, mostly the same
- added quests for sickles and scythes
- added pmmo reqs for sickles and scythes
- updated veinminer quest description
- Changed Nether Portal tip
- disable backpack mobs  (creates way too many backpack uuids, and many are full of an entire loottable)
- disabled fire mind and mirror shard
- re-enable cockatrice
- Added Smite & Lifesteal to Executioner Axe
- Increased Executioner Axe's Beheading Chance 10% -> 30% (5% higher than scythe)
- Disabled Spawner Key (Server Recipe)
- Bonk (emerald bow nerf)
- Slight nerf to valor & curses, buff to The Twist
- Deleted RadRecipes VFP Squid Loot Table
- Disabled Book of Recycling - we have Tiger for that, he's doing an excellent job (disabled for similar reason as uncrafting table)
- Item Tooltips:
	- Emeraldite Shards (may be removed)
	- Golden Bridle says it is used to tame the pegasus
	- Quark Backpack says to use sophisticated backpacks one instead (if it can be seen)
	- Soul Enchanter now straight up says its disabled for people who look it up in the book
	- Flint and Steel says to check the quest book for nether progression
- Added Luck and Lifesteal to Buddysteel Items
- dungeons gear requirements update
- disabled magical herbs
- Removed trading and farming as trinket unlock sources
- Decreased chance of unlocking a trinket from mining.
- added ore excavation config
- nerfed tower and fort generation chance from Illagers+ mod
- Troll Rate 40 -> 45
- removed inventoryhud+ toggle default
- disabled overstep and mirror enchants
- disabled Silk Step(buggy movement issues) (thanks @MasterBladeX and @kimchi)
- gorgon structure chance (125>200)
- pmmo max party 5>10
- lich rate 2>8
- re-enabled emeraldite ore in the wailing garth, with the removal of the crafting recipe, emerald gear will be much harder to get now
- Nerfed Extrabows again
- radenchants changes:
	- life leech
		- max lvl (3 > 5)
		- % per lvl (25% 2%)
	- glare
		- hp cost (0.25 > 0.05)
	- rejuvenate
		- heal % bonus per lvl (0.02 > 0.05)
	- one with the blade
		- allows armor & curios
	- socketed
		- pickaxes can get movespeed, reach, luck
- spawner limit decreased
- Magical Jewelry (bracelets, rings, amulets) only drop from champion mobs and the looting chance bonus has been halved
- disabled tinkets: dark egg (crash), treasure ring (insane), starfish (insane)
- removed biomes with weight 0 from byg-biomes.json
- Knowledge of the ages apex enchanting: It can grant huge amounts of xp so it has been given the apex treatment
- Fixed Dragon Skulls giving xp when hit
- disabled Sacrifice
- except for the choice reward, copper coin rewards are automatically given as soon as the coin is submitted.
- added into on how to give armor to pets, more info to some of the doggytalents stuff and changed "sheers" to "shears"
- removed hungering knowledge trade
- Life Leech is now incompatible with Leeching (Dungeons Gear) and Leech (Ensorcellation)
- librarians sell more disenchanting items
- disabled Drowned swim animation
- Vein Mine key says to use Ultimine instead
- changed soul enchanter recipe output

---
## [sadellie/unitto](https://github.com/sadellie/unitto)@[6ed66e761d...](https://github.com/sadellie/unitto/commit/6ed66e761d2176a7a26067c9053fe9b85eb10fc7)
#### Tuesday 2023-03-28 15:10:48 by Sad Ellie

Fuck you, 🤡 Huawei 🤡: The Sequel

- Got rid of AppGallery build variant

---
## [tplloi/Auxio](https://github.com/tplloi/Auxio)@[1826ae3215...](https://github.com/tplloi/Auxio/commit/1826ae32150455dea85c0def4a9adf3ba74bd8ff)
#### Tuesday 2023-03-28 15:20:41 by Alexander Capehart

deps: update to mdc 1.8.0-alpha01

FINALLY update to MDC 1.7.0. After over half a year.

I have been continually blocked by doing this due to this absurd ripple
bug that was so continually frustrating. Today, I finally figred out
how to hack a fix in by using R E F L E C T I O N and manually
disabling the bugged code path since google apparently can't be bothered
to fix it.

Now, you might wonder why I didn't update to 1.8.0. That is because
there is ANOTHER RIPPLE BUG. THIS TIME WITH THE TAB LAYOUT. AND ONLY IF
IT'S IN A COLLAPSING TOOLBAR LAYOUT. Can't wait to finally use the new
1.8.0 features in December!

---
## [morzel85/nushell](https://github.com/morzel85/nushell)@[2e01bf9cba...](https://github.com/morzel85/nushell/commit/2e01bf9cbadf833b4156ec5117393e51b8cadc7d)
#### Tuesday 2023-03-28 15:24:27 by Bob Hyman

add `dirs` command to std lib (#8368)

# Description

Prototype replacement for `enter`, `n`, `p`, `exit` built-ins
implemented as scripts in standard library.
MVP-level capabilities (rough hack), for feedback please. Not intended
to merge and ship as is.

_(Description of your pull request goes here. **Provide examples and/or
screenshots** if your changes affect the user experience.)_

# User-Facing Changes
New command in standard library

```nushell
〉use ~/src/rust/nushell/crates/nu-utils/standard_library/dirs.nu
---------------------------------------------- /home/bobhy ----------------------------------------------
〉help dirs
module dirs.nu -- maintain list of remembered directories + navigate them

todo:
* expand relative to absolute paths (or relative to some prefix?)
* what if user does `cd` by hand?

Module: dirs

Exported commands:
  add (dirs add), drop, next (dirs next), prev (dirs prev), show (dirs show)

This module exports environment.
---------------------------------------------- /home/bobhy ----------------------------------------------
〉dirs add ~/src/rust/nushell /etc ~/.cargo
-------------------------------------- /home/bobhy/src/rust/nushell --------------------------------------
〉dirs next 2
------------------------------------------- /home/bobhy/.cargo -------------------------------------------
〉dirs show
╭───┬─────────┬────────────────────╮
│ # │ current │        path        │
├───┼─────────┼────────────────────┤
│ 0 │         │ /home/bobhy        │
│ 1 │         │ ~/src/rust/nushell │
│ 2 │         │ /etc               │
│ 3 │ ==>     │ ~/.cargo           │
╰───┴─────────┴────────────────────╯
------------------------------------------- /home/bobhy/.cargo -------------------------------------------
〉dirs drop
---------------------------------------------- /home/bobhy ----------------------------------------------
〉dirs show
╭───┬─────────┬────────────────────╮
│ # │ current │        path        │
├───┼─────────┼────────────────────┤
│ 0 │ ==>     │ /home/bobhy        │
│ 1 │         │ ~/src/rust/nushell │
│ 2 │         │ /etc               │
╰───┴─────────┴────────────────────╯
---------------------------------------------- /home/bobhy ----------------------------------------------
〉
```
# Tests + Formatting

Haven't even looked at stdlib `tests.nu` yet.

Other todos:
* address module todos.
* integrate into std lib, rather than as standalone module. Somehow
arrange for `use .../standard_library/std.nu` to load this module
without having to put all the source in `std.nu`?
*  Maybe command should be `std dirs ...`?   
* what else do `enter` and `exit` do that this should do? Then deprecate
those commands.

Don't forget to add tests that cover your changes.

Make sure you've run and fixed any issues with these commands:

- `cargo fmt --all -- --check` to check standard code formatting (`cargo
fmt --all` applies these changes)
- `cargo clippy --workspace -- -D warnings -D clippy::unwrap_used -A
clippy::needless_collect` to check that you're using the standard code
style
- `cargo test --workspace` to check that all tests pass

# After Submitting

If your PR had any user-facing changes, update [the
documentation](https://github.com/nushell/nushell.github.io) after the
PR is merged, if necessary. This will help us keep the docs up to date.

---
## [facebook/pyre-check](https://github.com/facebook/pyre-check)@[a2683bcc78...](https://github.com/facebook/pyre-check/commit/a2683bcc78d13fd57ff11b013b58c1a512a2a930)
#### Tuesday 2023-03-28 15:30:59 by Steven Troxler

Thin down the fixme counting tests a bit

Summary:
There were more test cases than needed in my opinion, which is
annoying if I want to re-implement the suppression finding logic (which
I do, I'll explain why in a later diff) while reusing the tests.

So simplify a bit. Aggregations are isolated into the first two
test cases, everything after that is verifying that the regex handling
works properly with the comment in various places.

Reviewed By: grievejia

Differential Revision: D44398565

fbshipit-source-id: 90f4057e91968779a7abc6ee97323242041a24d6

---
## [aganders3/napari](https://github.com/aganders3/napari)@[3ec4be1ae8...](https://github.com/aganders3/napari/commit/3ec4be1ae8eee50ab4912ba87981261cc94c075f)
#### Tuesday 2023-03-28 15:33:00 by Grzegorz Bokota

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
## [gmcastil/microzed](https://github.com/gmcastil/microzed)@[6158adfd40...](https://github.com/gmcastil/microzed/commit/6158adfd40fa8465b55b101f689c78de25fe857a)
#### Tuesday 2023-03-28 15:52:54 by George Castillo

Adding working IP source code for the adder / multiplier module that
Adam Taylor references in part 24 and so forth of the Microzed
Chronicles

This commit contains the following:
- VHDL files based on the machine generated AXI4-Lite peripheral source
code. Includes some basic arithemetic and control sequential logic -
nothing special.
- Some C code that exercises the hardware in the PL to demonstrate some
basic functionality. I'm also including the header file that is
generated by the AXI4-Lite peripheral generator, but I'm not using any
of it.  It's essentially just a couple of syntactic sugar on top of
Xilinx syntactic sugar, which is intended to make it clearer that you
are performing reads and writes into the memory assigned to your
particular peripheral. I guess this is supposed to make life easier
rather than just magical numbers, which is I guess something that gets
abstracted away when you start adding in things like kernels, device
drivers, memory virtualization, and probably a slew of other things I
know nothing about.

Adam has made his source code available in a github repository
somewhere, but it isn't in a one to one correspondence with the material
he covers, so if you're looking at the Microzed Chronicles, this code,
his code, and your code trying to follow along, expect to see some
discrepancies.  Part of the struggle in learning a lot of this stuff is
figuring out how to do what you want with what you're given.

---
## [insertnamehere123/cmss13](https://github.com/insertnamehere123/cmss13)@[030a68f6ac...](https://github.com/insertnamehere123/cmss13/commit/030a68f6ac59efa5b7c02f1f9a421b3bd95fd0b3)
#### Tuesday 2023-03-28 16:45:24 by carlarctg

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
## [insertnamehere123/cmss13](https://github.com/insertnamehere123/cmss13)@[0bc21524a1...](https://github.com/insertnamehere123/cmss13/commit/0bc21524a123944a37d45e1088dca13476824b9c)
#### Tuesday 2023-03-28 16:45:24 by carlarctg

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
## [DimaWebFrontEnd/Great-things-start-from-small-beginnings](https://github.com/DimaWebFrontEnd/Great-things-start-from-small-beginnings)@[3c1f8c377e...](https://github.com/DimaWebFrontEnd/Great-things-start-from-small-beginnings/commit/3c1f8c377ea822106b7491170d736ee9543984d3)
#### Tuesday 2023-03-28 17:13:48 by DimaWebFrontEnd

README.md

You can host your site using one of these solutions or any of our other trusted providers. [Read more about our recommended and trusted hosts](https://medium.com/frontend-mentor/frontend-mentor-trusted-hosting-providers-bf000dfebe).

## Create a custom `README.md`

We strongly recommend overwriting this `README.md` with a custom one. We've provided a template inside the [`README-template.md`](./README-template.md) file in this starter code.

The template provides a guide for what to add. A custom `README` will help you explain your project and reflect on your learnings. Please feel free to edit our template as much as you like.

Once you've added your information to the template, delete this file and rename the `README-template.md` file to `README.md`. That will make it show up as your repository's README file.

## Submitting your solution

Submit your solution on the platform for the rest of the community to see. Follow our ["Complete guide to submitting solutions"](https://medium.com/frontend-mentor/a-complete-guide-to-submitting-solutions-on-frontend-mentor-ac6384162248) for tips on how to do this.

Remember, if you're looking for feedback on your solution, be sure to ask questions when submitting it. The more specific and detailed you are with your questions, the higher the chance you'll get valuable feedback from the community.

## Sharing your solution

There are multiple places you can share your solution:

1. Share your solution page in the **#finished-projects** channel of the [Slack community](https://www.frontendmentor.io/slack). 
2. Tweet [@frontendmentor](https://twitter.com/frontendmentor) and mention **@frontendmentor**, including the repo and live URLs in the tweet. We'd love to take a look at what you've built and help share it around.
3. Share your solution on other social channels like LinkedIn.
4. Blog about your experience building your project. Writing about your workflow, technical choices, and talking through your code is a brilliant way to reinforce what you've learned. Great platforms to write on are [dev.to](https://dev.to/), [Hashnode](https://hashnode.com/), and [CodeNewbie](https://community.codenewbie.org/).

We provide templates to help you share your solution once you've submitted it on the platform. Please do edit them and include specific questions when you're looking for feedback. 

The more specific you are with your questions the more likely it is that another member of the community will give you feedback.

## Got feedback for us?

We love receiving feedback! We're always looking to improve our challenges and our platform. So if you have anything you'd like to mention, please email hi[at]frontendmentor[dot]io.

This challenge is completely free. Please share it with anyone who will find it useful for practice.

**Have fun building!** 🚀

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[c27f9a6d9b...](https://github.com/tgstation/tgstation/commit/c27f9a6d9b9739baae09db063b6eb266d525772c)
#### Tuesday 2023-03-28 17:16:48 by necromanceranne

Minor Nukie Thing: Bolt-action Sniper Rifle, balance coding, and some ammo changes (#73781)

## About The Pull Request

### The Rifle:
-The Sniper Rifle is now a bolt action. This replaces the 4 second fire
delay on the sniper rifle. This overall will improve the fire rate if
you're good at racking the bolt, but it will also feel less like you're
in a weird limbo of inaction while using the sniper rifle, since the
fire delay can be quite confusing to players not used to it. This can be
tweaked, like reducing the speed of the racking action, if it seems like
it is too much.
-The scope component now goes up to 50 tiles (or so), which allows you
to gain a significant sightline over an area. The reasoning for this is
simple. The component actually nerfed the overall range of the sniper
rifle's scope, so this should hopefully restore that somewhat. And
having such a huge sightline makes it much easier to utilize the
impressive range of the rifle. Currently, it's really only ideal for
extremely close range fighting.
-The normal sniper rifle, the one that syndicate base scientists get,
can be suppressed. I don't know why it was different.

### The Ammo:

Normal .50 BMG: Does much more object damage, and on top of that deals
additional damage to mechs, but not by much more. Now, when it
dismembers a limb, it also deals its damage to the chest. This ensures
that you didn't straight up lose out on dealing a killing blow because
you took their limb off, and makes the dismemberment property of .50 BMG
a significant upside rather than a immense detriment.

Marksman: Gains a lot of the above benefits, but has much lower range.
Why this nerf? It's actually because of some funny nonsense with how
ricochet works. Which can cause....accidents to happen. To you. Consider
that firing down a straight line and missing could be quite embarrassing
when the bullet has 400 tiles of range.

Soporific: Now called Disruptor ammo. Works as it did before, putting
humans to sleep for 40 seconds (seriously, 40 seconds). Also deals some
stamina damage, if...that's relevant. But now also causes an EMP effect
and a boatload of added damage to both mechs and borgs, allowing it to
be an excellent anti-mech and anti-borg ammo type, as well as scrambling
any pesky suit sensors, energy weapons and so on in an area around the
impact. Useful for support fire.

Incendiary (NEW!): Causes a massive firebomb to go off where it impacts
(no explosion, so this isn't a stun). Also sets the target on fire,
which is always fun. Good for shooting into groups of people with
impunity. Also deals burn damage instead, since I think nukies could use
more methods for direct fire damage.

Surplus (NEW!): It's .50 BMG but it lacks most if not all the upsides.
No armour penetration, no dismemberment, no paralysis. It still deals a
lot of damage to objects, so not a bad option for simply removing
structures from afar. So what's the point in this ammo? You can buy 7
magazines for the price of one. I want to introduce 'Surplus' as an idea
for nukies to invest in if they want to be able to keep shooting but
they're really on a budget, like most non-warop nukies tend to be. This
is definitely subject to change (like a damage decrease on top of
everything else).

Pricing and Capacity: Normal ammo and surplus costs 3 TC. Every special
ammo costs 4 TC. Every special ammo also has the same ammo capacity as
the normal magazine. It's kind of weird how most of the subtypes had 5
shots rather than 6, but then soporific had...3? I don't get it. This
would probably cause a good deal of confusion, especially if you are
swapping ammo types and weren't aware of this particular oddity.

Anyway, 6 shots.

### Minor Addition
Gets rid of the cheap suppressor. It lies to players, tricking them into
thinking this is a low quality suppressor. Newsflash, it isn't. There is
no distinct difference between that suppressor and the normal
suppressor.

## Why It's Good For The Game

The sniper rifle, unfortunately, sucks a lot except for very specific
use cases. It got a big nerf with the scope component in terms of range,
even if the functionality is way cooler. And, at a baseline, there was
some counterintuitive functions attached to it. Dismemberment was cool,
but it also caused a loss in overall damage due to how limbs contribute
to core health. On top of this, the cool ammo types were...not much
better? Penetrator was almost always the best option, even if it lost a
lot of damage as a consequence.

So, what was it good for? X-ray + Penetrator. Pretty much, that's it. It
has some other uses but if I had to be entirely honest, there wasn't
much that other weapon couldn't do as well.

Hopefully this helps things going forward, and I want to mess with this
as well down the line in case its a bit too much of a boost in power.

Absolutely please rip this PR apart.

## Changelog
:cl:
balance: Makes the syndicate sniper rifle a bolt-action rifle.
balance: Sniper rifles have a scope range of roughly 50 tiles.
balance: Sniper rifle ammo, if it dismembers your limbs, does damage to
the chest.
balance: All the various syndicate sniper rifle magazines have
consistent casing quantities (6 shots). They also have more consistent
pricing. 3 for normal and a box of surplus, and 4 for every other type.
balance: Reduces the range of Marksman ammo to 50 tiles. Not because it
is strong, but because you might accidentally shoot yourself if you're
not watching where you're shooting. Ricochets are no joke.
add: Replaces Soporific with Disruptor ammo. Works like soporific, but
also EMPS things it hits.
add: Adds Incendiary .50 BMG. Causes a combustion to erupt from the
struck target, as well as setting targets on fire. Great for parties.
add: Adds Surplus .50 BMG. It sucks, but you get a lot of them! Quantity
over quality, baby.
remove: The suppressors in the bundle are of standard quality. The
apparent 'cheap suppressor' that came bundled with the C-20r and sniper
rifle were found to actually be 'fine'. Trust us.
/:cl:

---
## [SuperSlayer0/tgstation](https://github.com/SuperSlayer0/tgstation)@[f9fe79a307...](https://github.com/SuperSlayer0/tgstation/commit/f9fe79a307dc55eb6e3ecf25019ef388889898ba)
#### Tuesday 2023-03-28 17:20:48 by Dani Glore

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
## [redpanda-data/deployment-automation](https://github.com/redpanda-data/deployment-automation)@[54e0860613...](https://github.com/redpanda-data/deployment-automation/commit/54e08606133785bf05f4069ba35cab1f82233c1a)
#### Tuesday 2023-03-28 17:40:34 by gene-redpanda

push many tasks into roles

We now handle CA creation in the playbook so don't need a go-task entry for it

The intent of this PR is to push most of the "assisting" playbooks into the role to provide a single stop shop for building out a cluster. The end result is playbooks that clearly articulate a single final objective and have everything necessary to get it done, simplifying the experience of using the repo.

Note that it is still entirely possible to work flexibly by importing different task files from the role to achieve different goals (as is demoed with the TLS cluster).

The default path for the role is still the simplest possible option: installing and starting the RP node. In future it may be prudent to expand the default, but for now this seems correct.

Impact on current users:

Should be fairly minimal although it will definitely break any shell scripts. Tasks are still done the same way, they're just called differently. I'll provide some additional mitigation by tagging our current main as v1.0.0, with this edition tagged as v2.0.0, clearly signaling a potentially breaking change.

vars and cleanup

Added vars to playbooks so that we don't need to do janky sed edits in the hosts file.

Added run_once to create_ca since we're delegating to localhost anyway so there's no reason to do that in triplicate. Cuts run time some.

Removed everything related to populating the hosts file from task.

Removed a bunch of stuff that isn't true anymore for the README.md

Also defaulted monitoring to false in task because standing up a special monitoring node just for the cluster isn't necessary for testing.

make certs into a separate role

This commit makes a number of changes in response to a request not to include cert related content into the broker role as it seemed unrelated.

Starting with the simple stuff, I moved all the roles out of playbooks and placed them directly under ansible to improve clarity since we no longer have so many playbooks.

Next I moved the invocation of the data dir and dependencies installs into main.yaml of redpanda_broker. I felt this was a more sensible location, especially as we can control whether or not they fire by using the trigger variables.

I also moved all cert related content into the demo_certs role. I wanted the name to clearly indicate that this was NOT a production use role. There are no functional changes to the content in this role.

Finally I updated the provision-tls-cluster role to reflect the new changes.

delete bootstrap directory as these scripts are neither necessary nor supported anymore

adding suggested grep for message

default data dir and deps installs to true

linter cleanup + removing unnecessary role imports

The role imports in the CA related content are a holdover from when the CAs were in individual playbooks. As they are now in a role, it can be assumed that they will be imported into playbooks, and that the playbook will handle the restart process. Not removing the imports AND not including allow_duplicates resulted in the play eternally looping. However disabling the ability to run the broker role twice seems unnecessarily limiting. Imagine a scenario where someone wants a play to do initial cluster standup with three nodes, then add two more after some validation. To do this they'd need to include broker twice, which wouldn't be permitted in the old system.

I added risky-shell-pipe into the skip list and added explanations for why to the README.

I also fixed some copy paste and linter bugs and an annoying taskfile element where it wasn't cleaning up the zipfile.

set modes and use fqn for modules + disable change on two

change mode from 777 to 775 for security reasons

---
## [An4nke/Prototyping](https://github.com/An4nke/Prototyping)@[8109da6452...](https://github.com/An4nke/Prototyping/commit/8109da6452f5c1ad293982a2b75c82a6b8549f8b)
#### Tuesday 2023-03-28 17:46:19 by Ananke

Add files via upload

Added: word2emotion.py a skript for creating pictures as array (Packages numpy).
Text is extracted from HTML-code of a given Website-URL (Packages html.parser).
Colors are assigned by postive and negative tone of text as well as emotion trust, joy, surprise, fear, anger, sadness, anticip and disgust (Packages nrclex). Number of color-array-entries are sizen up to makte the resulting pictures bigger. Multiplicator for colors are based on wavelenght ratio of the colors blue (~300 nm), green (~550 nm) and red (800).
Enjoy this peace of art!

```python3.8 word2emotion.py https://de.wikipedia.org/wiki/Serotonin serotonin```

---
## [cvasqxz/VVVVVV](https://github.com/cvasqxz/VVVVVV)@[e93d8989d3...](https://github.com/cvasqxz/VVVVVV/commit/e93d8989d3e82e5afc52e09fd7aeae3d41644e64)
#### Tuesday 2023-03-28 17:51:04 by Misa

Revert "Fix Secret Lab Time Trial trophies having wrong colors"

As reported by Dav999, Victoria and Vermilion's trophy colors are
swapped again in 2.4. He points to
37b7615b71c3a2f44e03c47894383107850812ff, the commit where I fixed the
color masks of every single surface to always be RGB or RGBA.

It sounded plausible to me, because it did have to do with colors, after
all. However, it didn't make sense to me, because I was like, I didn't
touch the trophy colors at all after I originally fixed them.

After I ruled out the RGBf() function as a confounder, I decided to see
whether intentionally reversing the color order in RGBf() to be BGR
would do anything, and to my surprise it actually swapped the colors
back around and it didn't actually look bad.

And then I realized: Swapping the trophy colors between RGB and BGR
ordering results in similar colors that still look good, but are simply
wrong, but not so wrong that they take on a color that no crewmate uses,
so it'd appear as if the crewmates were swapped, when in reality the
only thing that was swapped was actually the color order of the colors.

Trying to fix this by swapping the colors again, I actively confused
colors 33 and 35 (Vermilion and Victoria) with colors 32 and 34
(Vitellary and Viridian), so I was confused when Vermilion and Victoria
weren't swapping. Then as a debugging step, I only changed 34 to 32
without swapping 32 as well, and then finally noticed that I was
swapping Vitellary and Viridian, because there were now two Vitellarys.
And then I was reminded that Vitellary and Viridian were also wrongly
swapped since 2.0 as well.

And so then I finally realized: The original comments accompanying the
colors were correct after all. The only problem was that they were fed
into a function, RGBf(), that read the colors backwards, because the
codebase habitually changed the color order on a whim and it was really
hard to reason out which color order should be used at a given time, so
it ended up reading RGB colors as BGR, while it looked like it was
passing them through as-is.

So what happened was that in the first place, RGBf() was swapping RGB to
BGR. Then I came and swapped Vermilion and Victoria, and Vitellary and
Viridian around. Then later I fixed all the color masks, so RGBf()
stopped swapping RGB and BGR around. But then this ended up swapping the
colors of Vermilion and Victoria, and Vitellary and Viridian once again!

Therefore, swapping Vermilion and Victoria, and Vitellary and Viridian
was incorrect. Or at least, not the fix to the root cause. The root
cause would be to swap the colors in RGBf(), but this would be sort of
confusing to reason about - at least if I didn't bother to just type the
RGB values into an image editor. But that doesn't fix the real issue,
which is that the game kept swapping RGB and BGR around in every corner
of the codebase.

I further confirmed that there was no more RGB or BGR swapping by
deleting the plus-one-divide-by-three transformation in RGBf() and
seeing if the colors looked okay. Now with the colors being brighter, I
could see that passing it straight through looked fine, but
intentionally reversing it to be BGR resulted in colors that at a
distance looked okay, but were either washed out or too bright. At least
finally I could use my 8 years of playing this game for something.

So in conclusion, actually, 37b7615b71c3a2f44e03c47894383107850812ff
("Fix surface color masks") was the real fix, and
d271907f8c5d84308a3cf9323ac692199b8685a6 ("Fix Secret Lab Time Trial
trophies having wrong colors") was the real regression. It's just that
the regression came first, but it wasn't really a regression until I did
the other fix, so the fix isn't the regression, the regression is...
this is hurting my brain. Or the real regression was the friends we made
along the way, or something like that.

This is the most trivial bug ever caused by the technical debt of those
god-awful reversed color masks.

---

This reverts commit d271907f8c5d84308a3cf9323ac692199b8685a6.

Fixes #862.

---
## [FarmWizard/coyote-bayou-jankify](https://github.com/FarmWizard/coyote-bayou-jankify)@[760cdde415...](https://github.com/FarmWizard/coyote-bayou-jankify/commit/760cdde41530afc3feaabe82aad7cc5761563bc3)
#### Tuesday 2023-03-28 18:52:34 by Tk420634

Merge pull request #1785 from GremlingSS/fix-trees

Fucking fixes the god awful trees

---
## [git/git](https://github.com/git/git)@[eaa0fd6584...](https://github.com/git/git/commit/eaa0fd658442c2b83dfad918d636bba3ca3b4087)
#### Tuesday 2023-03-28 19:38:29 by Jeff King

git_connect(): fix corner cases in downgrading v2 to v0

There's code in git_connect() that checks whether we are doing a push
with protocol_v2, and if so, drops us to protocol_v0 (since we know
how to do v2 only for fetches). But it misses some corner cases:

  1. it checks the "prog" variable, which is actually the path to
     receive-pack on the remote side. By default this is just
     "git-receive-pack", but it could be an arbitrary string (like
     "/path/to/git receive-pack", etc). We'd accidentally stay in v2
     mode in this case.

  2. besides "receive-pack" and "upload-pack", there's one other value
     we'd expect: "upload-archive" for handling "git archive --remote".
     Like receive-pack, this doesn't understand v2, and should use the
     v0 protocol.

In practice, neither of these causes bugs in the real world so far. We
do send a "we understand v2" probe to the server, but since no server
implements v2 for anything but upload-pack, it's simply ignored. But
this would eventually become a problem if we do implement v2 for those
endpoints, as older clients would falsely claim to understand it,
leading to a server response they can't parse.

We can fix (1) by passing in both the program path and the "name" of the
operation. I treat the name as a string here, because that's the pattern
set in transport_connect(), which is one of our callers (we were simply
throwing away the "name" value there before).

We can fix (2) by allowing only known-v2 protocols ("upload-pack"),
rather than blocking unknown ones ("receive-pack" and "upload-archive").
That will mean whoever eventually implements v2 push will have to adjust
this list, but that's reasonable. We'll do the safe, conservative thing
(sticking to v0) by default, and anybody working on v2 will quickly
realize this spot needs to be updated.

The new tests cover the receive-pack and upload-archive cases above, and
re-confirm that we allow v2 with an arbitrary "--upload-pack" path (that
already worked before this patch, of course, but it would be an easy
thing to break if we flipped the allow/block logic without also handling
"name" separately).

Here are a few miscellaneous implementation notes, since I had to do a
little head-scratching to understand who calls what:

  - transport_connect() is called only for git-upload-archive. For
    non-http git remotes, that resolves to the virtual connect_git()
    function (which then calls git_connect(); confused yet?). So
    plumbing through "name" in connect_git() covers that.

  - for regular fetches and pushes, callers use higher-level functions
    like transport_fetch_refs(). For non-http git remotes, that means
    calling git_connect() under the hood via connect_setup(). And that
    uses the "for_push" flag to decide which name to use.

  - likewise, plumbing like fetch-pack and send-pack may call
    git_connect() directly; they each know which name to use.

  - for remote helpers (including http), we already have separate
    parameters for "name" and "exec" (another name for "prog"). In
    process_connect_service(), we feed the "name" to the helper via
    "connect" or "stateless-connect" directives.

    There's also a "servpath" option, which can be used to tell the
    helper about the "exec" path. But no helpers we implement support
    it! For http it would be useless anyway (no reasonable server
    implementation will allow you to send a shell command to run the
    server). In theory it would be useful for more obscure helpers like
    remote-ext, but even there it is not implemented.

    It's tempting to get rid of it simply to reduce confusion, but we
    have publicly documented it since it was added in fa8c097cc9
    (Support remote helpers implementing smart transports, 2009-12-09),
    so it's possible some helper in the wild is using it.

  - So for v2, helpers (again, including http) are mainly used via
    stateless-connect, driven by the main program. But they do still
    need to decide whether to do a v2 probe. And so there's similar
    logic in remote-curl.c's discover_refs() that looks for
    "git-receive-pack". But it's not buggy in the same way. Since it
    doesn't support servpath, it is always dealing with a "service"
    string like "git-receive-pack". And since it doesn't support
    straight "connect", it can't be used for "upload-archive".

    So we could leave that spot alone. But I've updated it here to match
    the logic we're changing in connect_git(). That seems like the least
    confusing thing for somebody who has to touch both of these spots
    later (say, to add v2 push support). I didn't add a new test to make
    sure this doesn't break anything; we already have several tests (in
    t5551 and elsewhere) that make sure we are using v2 over http.

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[a0bc716073...](https://github.com/git-for-windows/git/commit/a0bc716073c72f19084b28113924026df158bde3)
#### Tuesday 2023-03-28 19:42:06 by Johannes Schindelin

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
## [Hermod132/tgstation](https://github.com/Hermod132/tgstation)@[09d27e1a51...](https://github.com/Hermod132/tgstation/commit/09d27e1a5149cffa1d5993687eabc7f8c240af85)
#### Tuesday 2023-03-28 19:51:38 by Jacquerel

Kidnapping won't destroy implants, nodrop items (#74118)

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

---
## [peff/git](https://github.com/peff/git)@[1e70ddb086...](https://github.com/peff/git/commit/1e70ddb086bc62ead39cce2d403707291adf35f2)
#### Tuesday 2023-03-28 20:47:21 by Jeff King

commit: give a hint when a commit message has been abandoned

If we launch an editor for the user to create a commit
message, they may put significant work into doing so.
Typically we try to check common mistakes that could cause
the commit to fail early, so that we die before the user
goes to the trouble.

We may still experience some errors afterwards, though; in
this case, the user is given no hint that their commit
message has been saved. Let's tell them where it is.

Signed-off-by: Jeff King <peff@peff.net>

---
## [dahga/Little-Bits](https://github.com/dahga/Little-Bits)@[8110d39b3d...](https://github.com/dahga/Little-Bits/commit/8110d39b3d2d5ad7b0dc68dcee1577e7e5f7f806)
#### Tuesday 2023-03-28 21:07:45 by Robyn

User/robyn/branch (#8)

* Delete Linda written by Robyn.docx

* Linda (Business Owner) - Robyn


Persona
Linda – Business Owner
Linda is 35 years old and lives in a small town in MN. She and her husband just started their own brewery. While her husband oversees making the beer and finding the right ingredients, she oversees everything else. Linda is comfortable with schedules and puts everything in her calendar on her cell phone as things come up. When Linda is at the computer, she uses the website to see how much time she has between tasks. Although she is not computer savvy, she uses what is most convenient to her. Linda is in charge of creating community events to bring people together at the brewery and ensuring all the servers are scheduled as needed. She is also in charge of the local bands that are able to play at the brewery at least once a week. She wants everyone to be happy and to establish a good relation in the community.


User Stories

User Story 1 (Linda, business owner)
Linda has a hectic day and realizes since the grand opening several bands have reached out and had reviews scheduled on Monday. She doesn’t know how much time she has between the reviews to complete the regular daily requirements of the brewery. Although the brewery opens at 11 am all her band reviews are 11 am and after. She just made it to the brewery at 9 am and viewed her calendar. She views the countdown clock and sees she has exactly 1.50 hours until her first review. Without eating breakfast or starting her cleaning she jumps on the jobs. She gets most of the cleaning done and her next review is at 1:30 pm and she has another every 30 min thereafter. The first review lasted 45 min, and an employee was called in sick. Linda agreed to help where needed to keep the flow of business. She realizes with the countdown clock she now has 1.1 hours until the next review and it’s always busier after lunch. With the limited time she has she is able to call the bands and ask that they do the review in front of the guests. This works out perfectly, the reviews are given a 1 – 10 score and all the customers are happy to put their vote in. Linda was able to get through the reviews and made progress with the local bands.

User Story 2 (Linda, business owner)
Linda decided she would work from home today for the brewery and be on call when needed. She logs into the website and reviews her calendar. She sees there is no countdown, but the business is in the summer parade in just 3 days! She forgot to put a countdown on the event. Now that she has added the countdown, she can see that she has 2 days and 12 hours left. She scrambles to the store to get things as needed and rushes her online delivery orders. The countdown helps, and when she doesn’t add it to her calendar events, she forgets about them.

---
## [openai/evals](https://github.com/openai/evals)@[3a2d72d9cc...](https://github.com/openai/evals/commit/3a2d72d9cc0b674a6b8cb6a8cca707baa3b46840)
#### Tuesday 2023-03-28 21:13:16 by Sean Ye

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
## [amjoseph-nixpkgs/nixpkgs](https://github.com/amjoseph-nixpkgs/nixpkgs)@[131aa21f0d...](https://github.com/amjoseph-nixpkgs/nixpkgs/commit/131aa21f0d3f7ff6b03ea1b9006922ec9be8d606)
#### Tuesday 2023-03-28 21:30:09 by Adam Joseph

stdenv: Nix-driven bootstrap of gcc

 #### Summary

By default, when you type `make`, GCC will compile itself three
times.  This PR inhibits that behavior by configuring GCC with
`--disable-bootstrap`, and reimplements the triple-rebuild using
Nix rather than `make`/`sh`.

 #### Immediate Benefits

- Allow `gcc11` and `gcc12` on `aarch64` (without needing new
  `bootstrapFiles`)
- Faster stdenv rebuilds: the third compilation of gcc
  (i.e. stageCompare) is no longer a `drvInput` of the final stdenv.
  This allows Nix to build stageCompare in parallel with the rest of
  nixpkgs instead of in series.
- No more copying `libgcc_s` out of the bootstrap-files or other
  derivations
- No more Frankenstein compiler: the final gcc and the libraries it
  links against (mpfr, mpc, isl, glibc) are all built by the same
  compiler (xgcc) instead of a mixture of the bootstrapFiles'
  compiler and xgcc.
- No more [static lib{mpfr,mpc,gmp,isl}.a hack]
- Many other small `stdenv` hacks eliminated
- `gcc` and `clang` share the same codepath for more of `cc-wrapper`.

 #### Future Benefits

- This should allow using a [foreign] `bootstrap-files` so long as
  `hostPlatform.canExecute bootstrapFiles`.
- This should allow each of the libraries that ship with `gcc`
  (lib{backtrace, atomic, cc1, decnumber, ffi, gomp, iberty,
  offloadatomic, quadmath, sanitizer, ssp, stdc++-v3, vtv}) to be
  built in separate (one-liner) derivations which `inherit src;`
  from `gcc`, much like https://github.com/NixOS/nixpkgs/pull/132343

 #### Incorporates

- https://github.com/NixOS/nixpkgs/pull/210004
- https://github.com/NixOS/nixpkgs/pull/36948 (unreverted)
- https://github.com/NixOS/nixpkgs/pull/210325
- https://github.com/NixOS/nixpkgs/pull/210118
- https://github.com/NixOS/nixpkgs/pull/210132
- https://github.com/NixOS/nixpkgs/pull/210109
- https://github.com/NixOS/nixpkgs/pull/213909
- https://github.com/NixOS/nixpkgs/pull/216136
- https://github.com/NixOS/nixpkgs/pull/216237
- https://github.com/NixOS/nixpkgs/pull/210019
- https://github.com/NixOS/nixpkgs/pull/216232
- https://github.com/NixOS/nixpkgs/pull/216016
- https://github.com/NixOS/nixpkgs/pull/217977
- https://github.com/NixOS/nixpkgs/pull/217995

 #### Closes

- Closes #108305
- Closes #108111
- Closes #201254
- Closes #208412

 #### Credits

This project was made possible by three important insights, none of
which were mine:

1. @ericson2314 was the first to advocate for this change, and
   probably the first to appreciate its advantages.  Nix-driven
   (external) bootstrap is "cross by default".

2. @trofi has figured out a lot about how to get gcc to not mix up
   the copy of `libstdc++` that it depends on with the copy that it
   builds, by moving the `bootstrapFiles`' `libstdc++` into a
   [versioned directory].  This allows a Nix-driven bootstrap of gcc
   without the final gcc would still having references to the
   `bootstrapFiles`.

3. Using the undocumented variable [`user-defined-trusted-dirs`]
   when building glibc.  When glibc `dlopen()`s `libgcc_s.so`, it
   uses a completely different and totally special set of rules for
   finding `libgcc_s.so`.  This trick is the only way we can put
   `libgcc_s.so` in its own separate outpath without creating
   circular dependencies or dependencies on the bootstrapFiles.  I
   would never have guessed to use this (or that it existed!) if it
   were not for a [comment in guix] which @Mic92 [mentioned].

My own role in this PR was basically: being available to go on a
coding binge at an opportune moment, so we wouldn't waste a
[crisis].

[aarch64-compare-ofborg]: https://github.com/NixOS/nixpkgs/pull/209870/checks?check_run_id=10662822938
[amd64-compare-ofborg]: https://github.com/NixOS/nixpkgs/pull/209870/checks?check_run_id=10662825857
[nonexistent sysroot]: https://github.com/NixOS/nixpkgs/pull/210004
[versioned directory]: https://github.com/NixOS/nixpkgs/pull/209054
[`user-defined-trusted-dirs`]: https://sourceware.org/legacy-ml/libc-help/2013-11/msg00026.html
[comment in guix]: https://github.com/guix-mirror/guix/blob/5e4ec8218142eee8e6e148e787381a5ef891c5b1/gnu/packages/gcc.scm#L253
[mentioned]: https://github.com/NixOS/nixpkgs/pull/210112#issuecomment-1379608483
[crisis]: https://github.com/NixOS/nixpkgs/issues/108305
[foreign]: https://github.com/NixOS/nixpkgs/pull/170857#issuecomment-1170558348
[static lib{mpfr,mpc,gmp,isl}.a hack]: https://github.com/NixOS/nixpkgs/blob/2f1948af9c984ebb82dfd618e67dc949755823e2/pkgs/stdenv/linux/default.nix#L380

---
## [smxi/inxi](https://github.com/smxi/inxi)@[5ee29fa022...](https://github.com/smxi/inxi/commit/5ee29fa022e01f8283fa526838f504c0dfccbadb)
#### Tuesday 2023-03-28 21:49:36 by Harald Hope

Significant upgrade to sound server running detections, much more granular and
hopefully more accurate, with more useful reporting values. Also added some nice
useful audio api/server tool and info items.

Packagers: this corrects possibly wrong or misleading audio server reports,
particularly related to PulseAudio/PipeWire, which can lead to support issues
and lack of clarity due to ambiguous or wrong reports about sound Servers
present, active, or off. Upgrading your package is highly recommended.

--------------------------------------------------------------------------------
SPECIAL THANKS:

1. Thanks to people like Chimera dev Daniel "q66" Kolesa for experimenting with
non systemd (uses dinit/dinitctl), non GCC, non GNU linux, and for making early
pre-alpha versions run in vm, and for being easy to test!

Not so much because I personally want or care about or view as a positive
skipping GNU tools or GCC in favor of clang and BSD tools, but more because
these experiments help make the general overall Linux ecosystem more robust.
Including inxi.

2. Thanks for the Manjaro people for noting this issue on their forums.

--------------------------------------------------------------------------------
KNOWN ISSUES:

1a. AUDIO: jack_control and pw-cli won't run as root, exit with error. This
forces back to fallback process present tests for active running state.

1b. AUDIO: pactl will start pipewire/pipewire-pulse/pulseaudio if stopped and
not masked, so not using since that would make inxi alter the state of the
system.

1c. AUDIO: pipewire-alsa, pulseaudio-jack depend on file exist globs, tested on
Arch Linux, Debian base, but unknown if paths exist on other Linux pimary
distros. Easy to add to globbing tests, but no going to check them all!

2. SERVICES: systemctl status [service] can fail if service loaded using --user
which is a new one on me, not sure how to handle that.

3. It would be nice to get inxi issues like the sound server/api glitches
handled by filing an issue on inxi github, and not to rely on my seeing a random
distro forum post, which I only found by pure coincidence.

--------------------------------------------------------------------------------
BUGS:

1. AUDIO: See Fixes 3a,b,c. In some cases false report of pulseaudio and
pipewire running: yes create unclear output and results, or misleading. Thanks
to manjaro users to noticing this and mentioning it in a forum post.

Note: it's much more effective to file issues on inxi github than to hope I will
see a random forum post one day.

2. DEBUGGER: Bug in debugger, somewhere introduced '-- list' (instead of
'--list') for bluetoothctl which made older systems hang when running the
debugger. No idea when or how that space got introduced.

--------------------------------------------------------------------------------
FIXES:

1. INFO: Compilers showed Compilers: gcc: N/A when clang/gcc not installed, this
was not intended, but was a small glitch in main::get_gcc_data(), where it
assigned undef as array contents when gcc not defined. This was exposed by
Chimera, which uses clang, but would have happened any time gcc not installed on
system.

2. SYSTEM: tiny fix, was getting ',' at end of kernel compiler version.

3a. AUDIO: For pipewire, made process detection test more robust, now excludes
pipewire-pulse in case where that might be running without pipewire on/enabled.

3b. AUDIO: bigger fix, more robust tests for audio servers running for jack,
pipewire, pulseaudio, these look for more explicit server tool reports. Certain
not to be reliable always, and fail for superuser, will probably need more
tweaking. Also notes for jack, pulse, pipewire if only positive detection found
via ps aux: active (process) to avoid incorrect data, and root specific messages
depending on situation.

3c. AUDIO: was testing for pactl to determine if pulseaudio installed, but found
case where pactl could be installed without pulseaudio. Now tests for pulseaudio
installed.

3d. AUDIO: weak fix for Linux OSS4 version, using /etc/oss4/version.dat file,
which may or may not exist on all distros.

3e. AUDIO: alsa-oss compat can create /dev/sndstat file, which would then lead
to positive OSS detection even if it's not present. This is corrected, and will
not show if asound/version exists and no ossinfo. For linux, relying on ossinfo
presence, which comes from oss4-base.

3f. AUDIO: Older ALSA /proc/asound/version had a date string in parentheses
after the Driver Version, so now explicitly get the string after Version.

--------------------------------------------------------------------------------
ENHANCEMENTS:

1. REPOS: added support for /etc/apk/repositories.d/*.list, which works pretty
much the same as /etc/apt/sources.list.d/*.list. This is to make Chimera apk
repos show up, previously only supported /etc/apk/repositories file read.

2a. DistroData: Added Feren to distro system base. This was much trickier than
it should be due to inconsistent use of os-release field names, but that's how
it goes.

2b. DistroData: new Arch derived distro XeroLinux added to system base. I know,
I know, it's a never-ending endeavor (get it?) since these pop up all the time,
but might as well add them now and then as they appear.

3a. AUDIO: inxi now handles pipewire-pulse as top layer audio daemon, along with
several other server/api helpers. Note that pw-jack does not appear to be a
daemon, just a plugin, so shows 'plugin'. Extra sound server helpers added when
discovered or requested.

  API: ALSA
    v: k5.19.0-16.2-liquorix-amd64
    status: kernel-api
  Server-1: PulseAudio
    v: 16.1
    status: off (on pipewire-pulse)
  Server-2: PipeWire
    v: 0.3.65
    status: active
    with:
      1: pipewire-pulse
        status: active
      2: pw-jack
        type: plugin

3b. AUDIO: For -Aa, added tools: report. Currently supports these basic tools:

alsa: alsamixer alsamixergui amixer
jack: cadence jack_control jack_mixer qjackctl
oss: dsbmixer mixer ossinfo ossmix ossxmix vmixctl
nas: auctl auinfo
pipewire: pw-cat pw-cli wpctl) [+pactl if pipewire-pulse and no pulseaudio
pulse: pacat pactl pamix pamixer pavucontrol pulsemixer
roar: roarcat roarctl
sndiod: aucat midicat mixerctl sndioctl

Note that inxi-perl/docs/inxi-audio.txt has lists of alternates or rejected
helpers and tools, but we want to keep that output short and sane.

3c. AUDIO: For BSDs, if sndiod is detected, adds an API line for sndio. Note
this may create 2 API lines for FreeBSD using OSS.

3d. AUDIO: Added basic support for roar sound server, NAS (Network Audio
System).

4. CPU: new Intel and AMD cpu model matches for latest and future, Luna Lake,
Zen 4c.

5. GRAPHICS: new nvidia current, AMD, and Intel GPU ids.

6. DRIVES: more disk vendors, ids! The list never stops, but sadly, so many are
not identifiable. Check: inxi-perl/tools/lists/disks_unhandled to see if you
can positively identify any of those.

--------------------------------------------------------------------------------
CHANGES:

1a. AUDIO: Changed main API/Server running: to status: [status], that syntax is
more able to handle different circumstances.

1b. AUDIO: With change to status:, now uses granular fixes above, and adds root
notes if no active detections.

1c. AUDIO: Changed 'Sound API', 'Sound Server' to 'API', 'Server'. This avoids
ambiguity with some types, it's the Audio section, and those are the APIs and
Servers for that Audio section. Makes it match Graphics as well. and is shorter.

1d. AUDIO: Changed 'Sound Interface' for sndiod to 'Server', which is how it's
listed, and for BSD, added API: sndio item. Also changed 'sndio' to 'sndiod' for
the Server: item.

1e. AUDIO: Changed ALSA/BSD sndio to show: status: api since saying an api
is running makes little sense, it's there or it's not there. OSS can be enabled
or disabled so shows status: active/off for Linux, but kernel-api for BSDs.

--------------------------------------------------------------------------------
DOCUMENTATION:

1a. MAN: Added note for helpers item: with: pipewire-pulse/pw-jack etc to -Axx.

1b. MAN: Added -Aa item for audio server tools.

2. OPTIONS: Updated for -Axx helpers, -Aa tools.

3. DOCS: Created inxi-perl/docs/inxi-audio.txt doc file. Too many odd factoids
to forget about during this upgrade!

--------------------------------------------------------------------------------
CODE:

1. REPOS: Moved %keys to %repo_keys and set it only once with set_repo_keys(),
those big hash assigns per iteration are really expensive, now stores it
globally in RepoItem and sets only once.

2. INFO: main::get_gcc_data() failed to handle case where there is no gcc at all
installed, resulted in returning an array with content of 'undef', not an empty
array as intended. This made the array not set test fail for Compilers, so gcc
showed as N/A, which was not intended.

3. DistroData: changed internal lsb/osr $distro to $distro_lsb/$distro_osr,
which lets inxi update the distro name during system base processing in cases
where the data is redundant. Stupid hack, sigh, should not be necessary, but
that's life, /etc/os-release was poorly designed so it leads to such confusions.

4a. AUDIO: Added --dbg 52 to output results of pw-cli.

4b. AUDIO: refactored sound_data, renamed, added {jack,pipewire,pulse}_status(),
sound_helpers(), sound_tools() utilities.

5. DEBUGGER: added more pactl and pw-cli outputs, and pipewire-pulse,
pipewire-jack --version.

6. main::get_driver_modules(): add space after ',' if total string > 40
characters to allow splitting very long unbroken strings of modules that
otherwise would not break as expected.

---
## [Offroaders123/In-N-Out](https://github.com/Offroaders123/In-N-Out)@[678029aced...](https://github.com/Offroaders123/In-N-Out/commit/678029aced01866b373efa24c57606461c88705a)
#### Tuesday 2023-03-28 22:18:23 by Offroaders123

Condiment Types Shift

Thinking about moving condiments away from being dedicated types, to instead being a distinct condiment type that's present as a property on the thing that you are ordering it on.

I can't decide how I would like this part to work at the type level though, I don't like having a `boolean | string` union type for that here, it feels a bit code-stinky. One idea I just thought of is using an enum-ish thing to correlate the condiment intensity instead using a level-based system with numbers instead. That feels a bit weird too though. Would 0 be none, 1 be extra light, and 6 be double extra? Or should 1 be regular, 0 be none, and then what? Hmm. That's what I liked about the `string | null` pattern, but then the redundant case there would be to have `'topping'` as the value for when the topping is present. Hmm hmm. That's what I liked about the original string interpolation version, it was more consistently using strings.

Gonna do more ideas testing! I think the next thing I realized is that I want to provide a JSON API that will fully show all of the data about your order. Then I could make an INO serializer of some sort that turns that into dedicated JS objects again. idk, something like that.

Oh yeah, and the full order would be an array of all the items in the order, and each thing could be it's own object with properties on it. I think if I try to think about it like this way instead, it will help me with trying to design an API to get the data into that format.

---
## [Parcosmic/Hammerwatch-Archipelago](https://github.com/Parcosmic/Hammerwatch-Archipelago)@[6d13dc4944...](https://github.com/Parcosmic/Hammerwatch-Archipelago/commit/6d13dc494455bef97e0f1afc8928853f71d5b5ad)
#### Tuesday 2023-03-28 22:56:41 by el-u

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
## [pdbuzzboard/pdbuzzboard](https://github.com/pdbuzzboard/pdbuzzboard)@[32b484b2f2...](https://github.com/pdbuzzboard/pdbuzzboard/commit/32b484b2f2b9c84ae5d686c2cbe75bd5bb990aeb)
#### Tuesday 2023-03-28 23:08:50 by Chris Hawkins

Update README.md

Hi, your video was one of the best instructional videos I've ever seen on any robotics/electronics project, great work. We did build this board for my mother with PD. She has been using it 2 days without relief, but we are hopeful it will help. We are going to build the vibration sensors next to ensure it is working correctly, and then work on the gloves so she can have more mobility. In this docs I included a video of it in operation for her in an early state of assembly. My hope is that my next build I can add much more instructions, and I have some additional photos and videos I want to include in an upcoming readme update. We know others with PD who are interested in assembling their own, so I would like to continue to document everything for my own use helping others. If you like it, I'd love your repo to be the source of truth for this, since this is really your work. 

However, I'm not offended by you wanting to make changes or reject these entirely. Thanks again for everything!

---
## [DaydreamIQ/tgstationIQ](https://github.com/DaydreamIQ/tgstationIQ)@[d43ebd042d...](https://github.com/DaydreamIQ/tgstationIQ/commit/d43ebd042dd751842728e8cb91fa7fc1a82f26d0)
#### Tuesday 2023-03-28 23:45:06 by san7890

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

