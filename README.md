## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-05-01](docs/good-messages/2023/2023-05-01.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,116,541 were push events containing 3,194,869 commit messages that amount to 242,805,424 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 63 messages:


## [alexhenrie/git](https://github.com/alexhenrie/git)@[7891e46585...](https://github.com/alexhenrie/git/commit/7891e465856e539c4a102dadec6dca9ac51c38df)
#### Monday 2023-05-01 00:11:52 by Jeff King

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
## [m-tmatma/git](https://github.com/m-tmatma/git)@[07f91e5e79...](https://github.com/m-tmatma/git/commit/07f91e5e79810a8f17de745d2d84c384add75f0a)
#### Monday 2023-05-01 00:17:01 by Jeff King

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[080c5dec38...](https://github.com/treckstar/yolo-octo-hipster/commit/080c5dec38ace34c6680647a5d0b25db54e4ef10)
#### Monday 2023-05-01 00:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [MarkSuckerberg/Shiptest](https://github.com/MarkSuckerberg/Shiptest)@[725233b42b...](https://github.com/MarkSuckerberg/Shiptest/commit/725233b42b6f56551798a0a75b5362e577042de3)
#### Monday 2023-05-01 00:33:50 by thgvr

The Lizardening Part One (And Friends) (#1845)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
This PR changes a lot of sprites. It's honestly too much. Namely:

- Explorer Equipment + Prototype
- Syndicate clothing
- Digitigrade lizard legs
- A new tail from Halcyon.
- Magboots from Zeta. Originally PR'd to tgstation.
- Colored (not greyscale! Ha Ha!) jumpsuits from Imaginos.

Heavy inspiration from the work of Imaginos, Halcyon, Mqiib, and
2cents#8442 for the original leg-work. (Haha, get it?)
The new digitigrade sprites started as a twinkle in the eye of Mqiib,
for yogstation(?) After myself and Halcyon saw those, an epihpany
struck. Perspective makes things cool and digitigrade perspective was
BAD.

I'll include a collage image of the new sprites if it's needed later.
Preview below:


![image](https://user-images.githubusercontent.com/81882910/228710332-0a213f88-5a8b-4b41-abdd-cee3b70ec403.png)
## Why It's Good For The Game
lizard,
Death of Codersprites
## Changelog

:cl:
add: New Digitigrade lizard sprites.
add: Various syndicate and mining clothing resprites.
add: Sarathi can now have an incredibly large tail.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [MarkSuckerberg/Shiptest](https://github.com/MarkSuckerberg/Shiptest)@[1c039c0623...](https://github.com/MarkSuckerberg/Shiptest/commit/1c039c0623b6e8af463de0f0b1ca1ccc49050d94)
#### Monday 2023-05-01 00:33:50 by Sun-Soaked

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
## [elee-p3/scsmush-evennia](https://github.com/elee-p3/scsmush-evennia)@[397108bca1...](https://github.com/elee-p3/scsmush-evennia/commit/397108bca1a3c3435dd333a95b1e624a43b774e6)
#### Monday 2023-05-01 00:34:26 by dancerdevin

CmdLogmunch and CmdTeach implemented. logmuncher.py and log.txt versioned. My plan is to replace log.txt every time I want to munch a new log and iterate through all my old logs. Is that clunky? Fuck you!

---
## [cozy/cozy-drive](https://github.com/cozy/cozy-drive)@[399a96980e...](https://github.com/cozy/cozy-drive/commit/399a96980e464cf6d6f9e60cbbe0a756f6b0cd45)
#### Monday 2023-05-01 00:36:27 by Crash--

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
## [JELGT2011/evals](https://github.com/JELGT2011/evals)@[aeeb452867...](https://github.com/JELGT2011/evals/commit/aeeb4528675de633d95a3535100b23c98739f6ce)
#### Monday 2023-05-01 00:45:05 by Alexander Raul

Algebra word problems (#36)

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
to see the eval performance on GPT-4.

## Eval details 📑
### Eval name
Algebra Word Problems (algebra_word_problems)

### Eval description

This eval contains some algebra word problems that tend to make gpt 3.5
hallucinate, but wouldn't be out of place on a grade school exam.
Currently has less than 100 examples, but will add if folks think this
is a good eval path to go down.

### What makes this a useful eval?

Poor performance on GPT 3.5 for one, but also would be a great test of
increased logical reasoning capabilities of GPT-4 per the release blog
post.

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
- [] Include at least 100 high quality examples

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

Since we are using Git LFS, we are asking eval submitters to add in
their first 100 JSONL eval lines.

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Answer the following question
with a single number and no additional text. You are a helpful
assistant."}, {"role": "user", "content": "If it takes 5 machines 5
minutes to make 5 devices, how long would it take 100 machines to make
100 devices?"}], "ideal": "5"}
{"input": [{"role": "system", "content": "Answer the following question
with a single number and no additional text. You are a helpful
assistant."}, {"role": "user", "content": "What is the sum of 60000,
5000, 400, and 3, with the third value multiplied by 5 before performing
the operation?"}], "ideal": "67003"}
{"input": [{"role": "system", "content": "Answer the following question
with a single number and no additional text. You are a helpful
assistant."}, {"role": "user", "content": "If the sum of the smallest
and largest of three consecutive even numbers is 28, what is the value
of the second largest number in the series?"}], "ideal": "14"}
{"input": [{"role": "system", "content": "Answer the following question
with a single number and no additional text. You are a helpful
assistant."}, {"role": "user", "content": "John is trying to fill a 16
oz. bottle with water. If John fills the bottle at 1 oz per second and
the bottle leaks .2 oz per second, how long would it take for John to
fill the bottle?"}], "ideal": "20"}
{"input": [{"role": "system", "content": "Answer the following question
with a single number and no additional text. You are a helpful
assistant."}, {"role": "user", "content": "Annie is training for a
marathon. She has a weekly training routine, training for five hours a
day on some days and 3 hours a day on the other days. She trains a total
of 27 hours in a seven day week. On how many days does she train for
five hours?"}], "ideal": "3"}
{"input": [{"role": "system", "content": "Answer the following question
with a single number and no additional text. You are a helpful
assistant."}, {"role": "user", "content": "At the start of the year the
ratio of boys to girls in a class is 2 : 1. But now, half a year later,
four boys have left the class and there are two new girls. The ratio of
boys to girls is now 4 : 3. How many students are there altogether
now?"}], "ideal": "28"}
  ```
</details>

---
## [JELGT2011/evals](https://github.com/JELGT2011/evals)@[bf2ebb9dd6...](https://github.com/JELGT2011/evals/commit/bf2ebb9dd69e8fbaad3eb42dab1a0523066a52ed)
#### Monday 2023-05-01 00:45:05 by Amir DIB

[evals] emoji riddle eval 🎨🤔 (#510)

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
**Emoji riddle**

### Eval description

The evaluation involves solving riddles made up of emojis. The
inspiration for this idea came from reading LinkedIn posts, where I
noticed that nearly 1-4% of the textual information was conveyed through
emojis. Nowadays, emojis are widely used to format text and introduce
color contrasts in texts, even by community managers of large companies.
Furthermore, using emojis is seen as a less formal way of communication
and gives a tone more suitable for social media.


### What makes this a useful eval?

- **Conversational understanding**. the eval test the ability to link
different concepts together which is a crucial feature.

- **Communication**. As GPT is deployed in settings where informal
language is used, interpreting emojis in context will likely become
critical. I think that improvement on this emoji riddle task would make
GPT better at mimicking human-like communication, as it would be able to
understand and respond to various forms of expressions involving emojis.
Emojis and their combinations often carry cultural and social meanings.
By being adept at emoji riddles, ChatGPT would showcase an understanding
of cultural nuances and be more relatable to users.

- **problem-solving**: Emoji riddle solving requires i) extracting
possible meanings and ii) finding the more suitable association of
meaning in the given context (cultural, plateform, etc).

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
{"input":[{"role":"system","content":"You are an emoji riddle solver.
You understand that an emoji riddle consists of finding the word or
group of words associated with an association of emojis that is provided
with the following format: emoji_1 + ... + emoji_n = ? . Your task is to
find the right answer."},{"role":"user","content":"👀 + 🪚 = ? \n Your
answer should strictly only contain the group of words associated with
the answer, no additional words. Don't add `The answer is`. don't add a
period at the end of your answer. everything should be
lowercase"}],"ideal":["seesaw"]}
{"input":[{"role":"system","content":"You are an emoji riddle solver.
You understand that an emoji riddle consists of finding the word or
group of words associated with an association of emojis that is provided
with the following format: emoji_1 + ... + emoji_n = ? . Your task is to
find the right answer."},{"role":"user","content":"❤️ + ✉️ = ? \n Your
answer should strictly only contain the group of words associated with
the answer, no additional words. Don't add `The answer is`. don't add a
period at the end of your answer. everything should be
lowercase"}],"ideal":["love letter"]}
{"input":[{"role":"system","content":"You are an emoji riddle solver.
You understand that an emoji riddle consists of finding the word or
group of words associated with an association of emojis that is provided
with the following format: emoji_1 + ... + emoji_n = ? . Your task is to
find the right answer."},{"role":"user","content":" ⌚️ + 🐶 = ? \n Your
answer should strictly only contain the group of words associated with
the answer, no additional words. Don't add `The answer is`. don't add a
period at the end of your answer. everything should be
lowercase"}],"ideal":["watchdog"]}
  ```
</details>

**The Dataset**

![image](https://user-images.githubusercontent.com/22154031/228633727-14480364-4009-45c1-8398-276de7bd86a9.png)

---
## [JELGT2011/evals](https://github.com/JELGT2011/evals)@[38f40050e9...](https://github.com/JELGT2011/evals/commit/38f40050e9344d6d4694c75506af03bf7ffe14d3)
#### Monday 2023-05-01 00:45:05 by dz-pika

Utility charge eval (#735)

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
Utility charge eval 

### Eval description
Given snippets from an electric utility bill, compute the per-kWh price
for electricity supply and delivery.

### What makes this a useful eval?
Utility bill parsing is needed to understand the breakdown of charges
and forecast future bills based on predicted usage. However, electricity
bills can be complex, with dozens of different line items that
contribute to the overall cost. This can be a headache for people
looking at their bill, as they just want to understand the per-kWh
prices for the supply/generation or delivery (e.g. transmission &
distribution) of their energy. Given incomplete but sufficient
information (e.g. simulating running OCR on a utility bill), this task
requires both the understanding and grouping of different terms and
charges under the delivery or supply, and basic arithmetic to compute
the total kWh and total charges in order to determine the per-kWh
prices. A human could fairly easily interpret the given data, but we
find that GPT3.5 (as well as GPT4 via the ChatGPT Plus) perform much
less accurately on the task (~.2).

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

All of the examples contain dummy values, but come from
terminology/formatting used in bills from many different utilities.

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
{"input": [{"role": "system", "content": "You are a JSON utility that
must return machine-readable JSON as output."}, {"role": "user",
"content": "Your job is compute the cost per kWh of electricity supply
(value must be a decimal rounded to 2 significant figures) and the cost
per kWh of electricity delivery (value must be a decimal rounded to 2
significant figures) based on the following incomplete OCR reading from
a user's utility bill. You are guaranteed to have the information needed
to compute the desired values. Return in the following JSON format:
{'supply_cost_per_kwh': '', 'delivery_cost_per_kwh': ''}. The following
is information from the utility bill: \nBasic Generation Service: 121
kWh X $0.069 per kWh = 8.35 \n Total Electric Supply Charges = 30.23 \n
Distribution Charge: 121 kWh X $0.041 per kWh = 4.96 \n Total Electric
Delivery Charges = 20.43"}], "ideal": "{'supply_cost_per_kwh': '0.25',
'delivery_cost_per_kwh': '0.17'}"}
{"input": [{"role": "system", "content": "You are a JSON utility that
must return machine-readable JSON as output."}, {"role": "user",
"content": "Your job is compute the cost per kWh of electricity supply
(value must be a decimal rounded to 2 significant figures) and the cost
per kWh of electricity delivery (value must be a decimal rounded to 2
significant figures) based on the following incomplete OCR reading from
a user's utility bill. You are guaranteed to have the information needed
to compute the desired values. Return in the following JSON format:
{'supply_cost_per_kwh': '', 'delivery_cost_per_kwh': ''}. The following
is information from the utility bill: \nGeneration Service (Supply) =
$34.89 \n Transmission Service = 7.24 \n Distribution Service = 4.96 \n
Meter Usage: 568 kWh"}], "ideal": "{'supply_cost_per_kwh': '0.061',
'delivery_cost_per_kwh': '0.022'}"}
{"input": [{"role": "system", "content": "You are a JSON utility that
must return machine-readable JSON as output."}, {"role": "user",
"content": "Your job is compute the cost per kWh of electricity supply
(value must be a decimal rounded to 2 significant figures) and the cost
per kWh of electricity delivery (value must be a decimal rounded to 2
significant figures) based on the following incomplete OCR reading from
a user's utility bill. You are guaranteed to have the information needed
to compute the desired values. Return in the following JSON format:
{'supply_cost_per_kwh': '', 'delivery_cost_per_kwh': ''}. The following
is information from the utility bill: \nElectricity Used (kWh) = 762 \n
Electricity Supply Charges 762 kWh at a cost of $100.25 \n Delivery
Service Charge: 762 kWh @ 0.008 = 6.096 \n Total Electric Delivery
Charges = 59.36"}], "ideal": "{'supply_cost_per_kwh': '0.13',
'delivery_cost_per_kwh': '0.078'}"}
{"input": [{"role": "system", "content": "You are a JSON utility that
must return machine-readable JSON as output."}, {"role": "user",
"content": "Your job is compute the cost per kWh of electricity supply
(value must be a decimal rounded to 2 significant figures) and the cost
per kWh of electricity delivery (value must be a decimal rounded to 2
significant figures) based on the following incomplete OCR reading from
a user's utility bill. You are guaranteed to have the information needed
to compute the desired values. Return in the following JSON format:
{'supply_cost_per_kwh': '', 'delivery_cost_per_kwh': ''}. The following
is information from the utility bill: \nSupply 423 kWh @ 11 cents / kWh
= 46.53 \n Total electricity supply charges $68.21 \n Delivery 423 kWh @
4 cents / kWh = 16.92 \n Total electricity delivery charges $17.43"}],
"ideal": "{'supply_cost_per_kwh': '0.16', 'delivery_cost_per_kwh':
'0.041'}"}
{"input": [{"role": "system", "content": "You are a JSON utility that
must return machine-readable JSON as output."}, {"role": "user",
"content": "Your job is compute the cost per kWh of electricity supply
(value must be a decimal rounded to 2 significant figures) and the cost
per kWh of electricity delivery (value must be a decimal rounded to 2
significant figures) based on the following incomplete OCR reading from
a user's utility bill. You are guaranteed to have the information needed
to compute the desired values. Return in the following JSON format:
{'supply_cost_per_kwh': '', 'delivery_cost_per_kwh': ''}. The following
is information from the utility bill: \nEnergy 152 @ 0.069 = 10.49 \n
Total Energy Charges = 14.25 \n Distribution 152 @ 0.041 = 6.23 \n Total
Electric Delivery Charges = 6.99"}], "ideal": "{'supply_cost_per_kwh':
'0.094', 'delivery_cost_per_kwh': '0.046'}"}
  ```
</details>

---
## [JELGT2011/evals](https://github.com/JELGT2011/evals)@[b2250e4117...](https://github.com/JELGT2011/evals/commit/b2250e4117125fa79e852f454cd4b01b3c066563)
#### Monday 2023-05-01 00:45:05 by shivamd1810

Add General science reasoning: UPSC GS eval. (#641)

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
Hindi UPSC

### Eval description

[UPSC](https://en.wikipedia.org/wiki/Union_Public_Service_Commission) is
the organization responsible for conducting administrative service exams
in India. This evaluation set focuses on questions from the general
science paper of UPSC exams in Hindi. As a widely spoken language in
India, it is crucial to understand and answer questions accurately in
Hindi.



### What makes this a useful eval?

This evaluation set is useful for several reasons:

1. Real-world applicability: The questions are sourced from actual UPSC
exams, making the evaluation set practical and relevant for users
preparing for these exams.
2. Language diversity: By focusing on Hindi, this evaluation set helps
to improve the AI's understanding and response generation in a
non-English language, catering to a large user base.
3. Subject matter: General science is an important topic covered in the
UPSC exams, and evaluating the AI's performance in this area will help
identify areas for improvement.
4. Logical reasoning and inference: **UPSC questions are known for
requiring logical reasoning and the ability to infer connections between
multiple topics**. By including questions that demand such skills, this
evaluation set will help test and improve the AI's ability to handle
complex, multi-layered problems.


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

This evaluation set is valuable for improving the AI's understanding of
Hindi and its ability to provide accurate answers to general science
questions in the context of UPSC exams, a widely recognized and
important examination in India. Moreover, by incorporating questions
that test logical reasoning and inference skills, it will help enhance
the AI's capability to handle complex, multi-faceted problems that
require connections between multiple topics.

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
{"input": [{"role": "system", "content": "\n1. भारत की संसद के संदर्भ
में, निम्नलिखित कथनों पर विचार कीजिए:\n\n1- गैर-सरकारी विधेयक ऐसा विधेयक
है जो संसद् के ऐसे सदस्य द्वारा प्रस्तुत किया जाता है जो निर्वाचित नहीं
है किंतु भारत के राष्ट्रपति द्वारा नामनिर्दिष्ट है।\n2- हाल ही में, भारत
की संसद के इतिहास में पहली बार एक गैर-सरकारी विधेयक पारित किया गया
है।\n\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?\n\n(a) केवल 1\n(b)
केवल 2\n(c) 1 और 2 दोनों\n(d) न तो 1 और न ही 2\n\n, choose correct
answer:"}], "ideal": "d"}
{"input": [{"role": "system", "content": "2. ऋग्वेद-कालीन आर्यों और
सिन्धु घाटी के लोगों की संस्कृति के बीच अंतर के संबंध में, निम्नलिखित
कथनों में से कौन-सा/से सही है/हैं?\n1- ऋग्वेद-कालीन आर्य कवच और
शिरस्त्रण (हेलमेट) का उपयोग करते थे जबकि सिन्धु घाटी सभ्यता के लोगों में
इनके उपयोग का कोई साध्य नहीं मिलता।\n2- ऋग्वेद-कालीन आर्यों को स्वर्ण,
चाँदी और ताम्र का ज्ञान था जबकि सिन्धु घाटी के लोगों को कवल ताम्र और लोह
का ज्ञान था।\n3- ऋग्वेद-कालीन आर्यों ने घोड़े को पालतू बना लिया था जबकि
इस बात का कोई साक्ष्य नहीं है कि सिन्धु घाअी के लोग इस पशु को जानते
थे।\n\nनीचे दिए गए कूट का प्रयोग कर सही उत्तर चुनिएः\n\n(a) केवल 1\n(b)
केवल 2 और 3\n(c) केवल 1 और 3\n(d) 1, 2 और 3\n\n, choose correct
answer:"}], "ideal": "c"}
{"input": [{"role": "system", "content": "3. ‘पूर्व अधिगम की मान्यता
स्कीम (रिकग्निशन ऑफ प्रायर लर्निंग स्कीम)’ का कभी-कभी समाचारों में किस
संदर्भ में उल्लेख किया जाता है?\n(a) निर्माण कार्य में लगे कर्मकारों के
पारंपरिक मार्गों से अर्जित कौशल का प्रमाणन\n(b) दूरस्थ अधिगम कार्यक्रमों
के लिए विश्वविद्यालयों में व्यक्तियों को पंजीकृत करना\n(c) सार्वजनिक
क्षेत्र के कुछ उपक्रमों में ग्रामीण और नगरीय निर्धन लोगों के लिए कुछ
कुशल कार्य आरक्षित करना\n(d) राष्ट्रीय कौशल विकास कार्यक्रम के अधीन
प्रशिक्षणार्थियों द्वारा अर्जित कौशल का प्रमाणन\n\n, choose correct
answer:"}], "ideal": "a"}
{"input": [{"role": "system", "content": "4. पारिस्थितिक दृष्टिकोण से,
पूर्वी घाटों और पश्चिमी घाटों के बीच एक अच्छा सम्पर्क होने के रूप में
निम्नलिखित में से किसका महत्व अधिक है?\n(a) सत्यामंगलम बाघ आरक्षित
क्षेत्र (सत्यमंगलम टाइगर रिजर्व)\n(b) नल्लामला वन\n(c) नागरहोले
राष्ट्रीय उद्यान\n(d) शेषाचलम जीवमण्डल आरक्षित क्षेत्र (शेषाचलम
बायोस्फीयर रिजर्व)\n\n, choose correct answer:"}], "ideal": "a"}
{"input": [{"role": "system", "content": "5. समाज में समानता के होने का
एक निहितार्थ यह है कि उसमें\n(a) विशेषाधिकारों का अभाव है\n(b) अवरोधों
का अभाव है\n(c) प्रतिस्पर्धा का अभाव है\n(d) विचारधारा का अभाव है\n\n,
choose correct answer:"}], "ideal": "a"}
  ```
</details>

---
## [JELGT2011/evals](https://github.com/JELGT2011/evals)@[9fdbd94c93...](https://github.com/JELGT2011/evals/commit/9fdbd94c93fc9560781c5e359e3be10d069ac6c5)
#### Monday 2023-05-01 00:45:05 by Tong

Add Loss Logic Eval (#82)

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
to see the eval performance on GPT-4.

## Eval details 📑
### Eval name
Loss Logic

### Eval description

A store bought a watermelon for $5 and sold it for a different price,
receiving counterfeit money in the transaction. They also had to give
change to the buyer. The net loss for the store varies based on the
specific details of the transaction.

### What makes this a useful eval?

* Tests comprehension and problem-solving skills: The scenarios provided
require the AI to understand and analyze the given information to
determine the net loss for the store.

* Addresses real-world situations: Counterfeit money transactions are a
real concern for businesses. This eval allows the AI to demonstrate its
understanding of financial transactions and the impact of counterfeit
money on a store's net loss.


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
- [ ] Include at least 100 high quality examples

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

Involving the judgement of the truth or falsehood of real-world things,
which is a capability that GPT currently lacks.

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
{"input":[{"role":"system","content":"The store purchased a watermelon
for $5 and sold it for $7. Unfortunately, they received $10 in
counterfeit money after the transaction and had to give the buyer $3 in
change. What was the net loss for the store? Let's think step by
step:"}],"ideal":"Sure, let's break down the transaction step by step to
determine the net loss for the store: The store purchases a watermelon
for $5. The store sells the watermelon for $7. This would have been a $2
profit if the money received was real. The store receives $10 in
counterfeit money. This money is worthless, so the store doesn't
actually receive any value from the sale. The store gives the buyer $3
in change. This is a real loss, as the store loses $3 in real money.
Now, let's calculate the net loss: The store spent $5 to purchase the
watermelon. The store lost $3 when giving the buyer change. So the net
loss for the store is $5 (cost of watermelon) + $3 (change given) =
$8."}
{"input":[{"role":"system","content":"The store bought a watermelon for
$5 but sold it for $4. Furthermore, they received $10 in counterfeit
money from the buyer and had to provide $6 in change. What was the net
loss for the store? Let's consider the process in
detail:"}],"ideal":"Sure, Let's think step by step: The store purchased
a watermelon for $5. The store sold the watermelon for $4, which means
they incurred a loss of $1 on the sale. The buyer gave the store $10 in
counterfeit money, which the store accepted during the transaction. The
store gave the buyer $6 in change. Since the store accepted $10 in
counterfeit money, they lost $10 in that transaction. The net loss for
the store is the sum of the loss on the watermelon sale and the loss
from accepting the counterfeit money, which is $1 + $10 = $11.
Therefore, the net loss for the store is $11."}
{"input":[{"role":"system","content":"The store bought a watermelon for
$5 and sold it for the same price of $5. However, they received $10 in
counterfeit money from the buyer and had to give the buyer $5 in change.
What was the net loss for the store? Let's consider the process step by
step:"}],"ideal":"Step 1: The store purchases a watermelon for $5.
Store's expenses: $5 Step 2: The store sells the watermelon for $5 but
receives $10 in counterfeit money. The counterfeit money has no value,
so the store effectively received nothing for the watermelon. Store's
revenue: $0 Step 3: The store gives the buyer $5 in change. Since the
money given in change is real, this is an additional expense for the
store. Store's expenses: $5 (watermelon) + $5 (change) = $10 Step 4:
Calculate the net loss. Net loss = Expenses - Revenue Net loss = $10
(expenses) - $0 (revenue) Net loss = $10 The store's net loss for this
transaction is $10."}
{"input":[{"role":"system","content":"The store bought a watermelon for
$5 and sold it for $7. Regrettably, they received $7 in counterfeit
money from the buyer after the transaction. What was the net loss for
the store? Let's consider the process step by step:"}],"ideal":"Sure,
let's break down the transaction step by step: The store purchased a
watermelon for $5. They sold the watermelon for $7, but received
counterfeit money. To determine the net loss, let's analyze the costs
and the revenue: Costs: The store spent $5 on the watermelon. Revenue:
The store received $7 in counterfeit money, which has no value, so their
revenue is $0. Net loss: To calculate the net loss, subtract the revenue
from the costs: $5 (costs) - $0 (revenue) = $5. So, the net loss for the
store is $5."}
{"input":[{"role":"system","content":"The store was given a
complimentary watermelon, which they then sold for $7. Regrettably,
following the transaction, they received $10 in fake money and had to
provide the buyer with $3 in change. Let's consider the following steps
in determining the store's net loss:"}],"ideal":"To determine the
store's net loss, we can consider the following steps: Assess the value
of the complimentary watermelon: Since the watermelon was given to the
store for free, it didn't cost them anything. Therefore, the store's
initial cost for the watermelon is $0. Calculate the revenue from
selling the watermelon: The store sold the watermelon for $7. However,
they received $10 in fake money, which has no value, so the actual
revenue is $0. Determine the cost of the change provided: Since the
store provided the buyer with $3 in change, this is an additional cost
to the store. Calculate the net loss: Subtract the revenue (Step 2) from
the sum of the initial cost (Step 1) and the cost of the change (Step
3). In this case: Net loss = (Initial cost + Cost of change) - Revenue
Net loss = ($0 + $3) - $0 Net loss = $3 The store's net loss from this
transaction is $3."}
  ```
</details>

---
## [klorpa/tgstation](https://github.com/klorpa/tgstation)@[3156a0414e...](https://github.com/klorpa/tgstation/commit/3156a0414e96b597d4d53823066d29daa0b30737)
#### Monday 2023-05-01 01:02:16 by san7890

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
## [ma44/mojave-sun-13](https://github.com/ma44/mojave-sun-13)@[736422fac8...](https://github.com/ma44/mojave-sun-13/commit/736422fac8d84c8e054853fd2b205cc993250c21)
#### Monday 2023-05-01 01:04:38 by Technobug14

Field Transfusions & Fixes Sprites/Runtime (#2152)

* Working field transfusions

As far as I can tell, no runtimes or bugs. Should be good to go. Could maybe do with some polish? But otherwise it works great.

* Fixes energy weapon bugs

Fixes a runtime related to emptying cells from energy weapons, and fixes an overlay bug and inventory icon bug on the cells themselves.

* Bug fixes

read above, fixes a few bugs/errors

* Broken as hell

Supposed to add new IV bag sprites and overlays that would change as the bag gets emptier. Multiple bugs both with transfusion and the icon/overlay. Right now, the icon currently disappears once the object is on the ground and I can't tell why. Secondly, the overlay has the visual bugs and could probably do with a more thorough system to apply it? The bugs on transfusion are mostly due to a lack of sanity checks, where it will continue to be attached to someone from many tiles away when thrown/dropped, etc.

* Shit

HATE HATE HATE this sucks and it is buggy as hell

* Fix icon/overlay updates

* Mostly working

Still some broken stuff, you can attach IV bags if you're not next to someone and do it from inside containers, also fixes the world states for the police and military 10mm pistol

* Finishing touches

Couple of bug fixes, fixes 10mm police/military world sprite, etc etc. Should be good to go.

Co-authored-by: Koshenko <koshenko@pm.me>
Co-authored-by: Koshenko <53068134+Koshenko@users.noreply.github.com>

---
## [the-og-gear/tgstation](https://github.com/the-og-gear/tgstation)@[b3f5dfae14...](https://github.com/the-og-gear/tgstation/commit/b3f5dfae1418d4ac24df666e00ca47aef08c9dad)
#### Monday 2023-05-01 01:34:33 by san7890

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
## [Cheshify/tgstation](https://github.com/Cheshify/tgstation)@[ad302f209f...](https://github.com/Cheshify/tgstation/commit/ad302f209f4fc0b739c6eea8e6be92da05e2742c)
#### Monday 2023-05-01 01:57:30 by Zytolg

Nanotrasen Budget Programme - Mothball Edition [BIRDSHOT STATION] (#73502)

## About The Pull Request
--- 

The Space Tram is currently spaced. This is a known issue with not the
map, but Trams in general. The Space Tram is a Space Tram to encourage a
fix. Until then, the Space Tram is a maint tram that's an actual hazard
but cannot directly kill anyone, including lizards. Enjoy the commodity
as you zip from secmaint to medmaint.
-------------------------------------------------------

I... really don't know if I should be proud of myself here. This whole
process has been akin to a fever dream and it has only been little over
a month since I first created the .dmm for this. What started as a
simple yet humble reimagining of Birdboat has turned into an entirely
new station, and blown past Metastation sized proportions. This has been
my most expansive project yet, and somehow it's also been my quickest.
So without further ado, I unveil Birdshot - Successor to Birdoat.

-------------------------------------------------------

**Due to recent cost expenditures on Icemoon projects, and a growing
need for orbital research stations, Nanotrasen has decided to pull
Birdboat Station out of mothball after nearly 5 years of abandonment.**

Since then, the station has seen a variety of changes at the hands of
the various vagabond lawless scum and villains that have decided to make
the abandoned station their home. Do not fret though, a Nanotrasen
Operation has secured the companies rightful property for corporate use
once again, though you'll need to be the stewards of the remaining
cleanup operation.

------------------------------------------------------

Now, as you might have guessed by now, Birdshot is heavily based on
Birdboat station. Many of the decisions here follow the original layout,
and what had to be modified or moved still tries its best to replicate
and imitate what bird being said. At least, that was the idea initially.
This has very much grown into its own beast and as such, while the main
inspiration has been Birdboat, there are a lot of new ideas thrown into
the mix that really give this station its own unique and deserving
identity. Maybe it's not perfect, but I've been inspired by @MMMiracles
own performance with Tramstation to keep working on Birdshot and
updating it with better and improved faculties. For now, though the
station is in a playable state, and that means I'm making a PR. If I had
to borrow the words of the good MMM, I would call this **Birdshot:
Season 0**


![BirdSHOTFULL2-26-S](https://user-images.githubusercontent.com/33048583/221432760-27af1889-d2d0-4861-9435-df4258525fae.png)



See the image in more detail here: https://imgur.com/iT5Vi8k



## Why It's Good For The Game

We've been with the same 5 maps for a while now. @san7890 jokingly said
that I could sacrifice Metastation back in November if I remade Birdboat
but modern. Obviously that wasn't going to happen, yet I was spurred on
by the idea. When I began this in earnest early this January, @EOBGames
said that a Birdboat sized map would replace Kilostation in the
rotation. Interestingly we're not a small map anymore so I honestly have
no clue where this goes. Maybe that ephemeral 6th map slot that's been
rumored.

What I can say, is that Birdshot is wholly unlike anything else that is
currently in rotation. It's got an engineering section that feels way
too small for a station of that size, almost evocative of Cere. Cargo is
blessed with a Boutique that makes use of @Fikou's new mannequin dolls.
Command is outfitted with a Corporate Guest Suite, and Officials sent
from Nanotrasen can embark from their ferry into the safety of their own
Corporate Dock. Elements of Cerestation are present, yet not in a way
that makes traversal annoying. Furthermore we have **2 Trams** (that I
have yet to get functional but we'll get there) on Birdshot, that's
right 2. One Security Prison Tram, and then other, a Space Tram. Both
Novel in their own ways. Departments on Birdshot twist and turn, and
there's an abundance of Maintenance Tunnels to cut through everything,
for the brave and the bold that is. And there's plenty left to discover,
but I'd rather let Birdshot speak for itself. I'm proud of this one.

If you want something new, this is something that is almost the complete
opposite of Chilled Station - Explicitly Designed to send you back to
the metal death trap that is: **Space Station 13.**


## Changelog
:cl:
add: Birdshot station has been pulled out of Mothball.
add: New station areas and places to visit. A Mix of Kilo and Delta
maints with winding shortcutting paths.
add: A host of new shuttles to support this bold endeavor to reclaim
something that really shouldn't be reclaimed.
add: Two Trams, Two Trams.
add: For the last time Bob, the gaping hole is a **feature.** Use the
breach shutters or have the virologist make starlight.
add: A smiling salute to stations past...
add: Secrets.


/:cl:

---------

Co-authored-by: Zytolg <theoriginaldash@gmail,com>

---
## [Bm0n/tgstation](https://github.com/Bm0n/tgstation)@[e1221c986f...](https://github.com/Bm0n/tgstation/commit/e1221c986f5da2551051f47aa0fbd1d49e367c9b)
#### Monday 2023-05-01 02:06:31 by san7890

Chasm Hell On Icebox - 300 Active Turfs on Prod Moment (#74410)

## About The Pull Request

Spontaneous regressions introduced by #74359
(1e58c1875d9e2f48a306fe31a0626dbbb1990ff9).
```txt
 - Z-Level 2 has 150 active turf(s).
 - Z-Level 3 has 150 active turf(s).
 - Z-Level trait Ice Ruins Underground has 300 active turf(s).
 - Z-Level trait Mining has 300 active turf(s).
 - Z-Level trait Station has 300 active turf(s).
 - End of active turf list.
 ```

![image](https://user-images.githubusercontent.com/34697715/229213138-5a6a7a4f-edec-47ab-8def-ee4e4bddfe61.png)

Basically the lavaland ruin sucks dogshit and I had to do a lot of stuff to account for everything failing. There was even a moment where we were adding something to `flags_1` instead of `turf_flags` and that was also really bad to figure out.

![image](https://user-images.githubusercontent.com/34697715/229213428-63bb1f6e-6f88-4604-a3c6-e08e20cbfa7a.png)

i also had to add orange genturfs because it was really getting bad with all of the assertions we had to keep making, especially since stuff like this could also show up:

![image](https://user-images.githubusercontent.com/34697715/229213562-4a145453-5f90-4d05-b8cc-5c1beec2b0dd.png)

That's the prison in the red box, those are active turfs because a chasm scraped it away.

Sorry if this is hard to follow but I promise you everything in this is essential. I wish we didn't have to rely on turf flags as much as we do but this is a fix PR, not a refactor.
## Why It's Good For The Game

Even one active turf on IceBox ate up _three_ seconds of SSair's initialization every single time it was really fucking bad.

We haven't had to deal with chasms for about two years so there's a lot of mapping assertions we made since they just weren't a thing, but now they're back so lets do it properly.
## Changelog
:cl:
fix: The prison on IceBox should no longer leak air as often.
/:cl:

I have compiled this map about 30 times until active turfs stopped fucking happening and now I am content. This likely doesn't fix _everything_ because some stuff can still be hidden to me, and we still have PRs that need to be merged to reduce the amount of noise we're getting on prod.

---
## [Bm0n/tgstation](https://github.com/Bm0n/tgstation)@[0a1f7e8de2...](https://github.com/Bm0n/tgstation/commit/0a1f7e8de2fea2116b73f22a11fdf328763c503a)
#### Monday 2023-05-01 02:06:31 by Hatterhat

Thrown containers splashing on mobs spill some contents on the floor (#74345)

## About The Pull Request
Spiritual continuation of tgstation/tgstation#74187.

![image](https://user-images.githubusercontent.com/31829017/228645705-5a32cc67-37e0-48d6-9e95-6006f455ed3c.png)
Reagent containers that splash their contents on people also splash the
floor - the amount that gets splashed on the floor is the amount that
missed the target.
### Mapping March

Ckey to receive rewards: N/A (it's not a mapping PR)

## Why It's Good For The Game
Splashing people with a molotov filled with Random Shit now also
splashes that Random Shit all around, making them slightly more spicy to
play around with. Unfortunately, I couldn't figure out how to make fuel
puddles ignite off of lit objects resting on top of them (there's no
item-level proc for hotspot exposure or something). If anyone wants to
advise me on how to make that happen, that'd be cool.

## Changelog
:cl:
add: Reagent containers that splash on people when thrown (e.g.
molotovs) now spill their contents on both target and turf. (This means
that throwing molotovs with enough fuel spills fuel puddles, throwing
beakers with acid spills acid on the floor, etc. etc.) Unfortunately,
molotovs still lack the ability to ignite their own spilled fuel, but
we'll get there one day.
/:cl:

Co-authored-by: Hatterhat <Hatterhat@users.noreply.github.com>

---
## [BlackMajor/CHOMPStation2](https://github.com/BlackMajor/CHOMPStation2)@[b1f52736ca...](https://github.com/BlackMajor/CHOMPStation2/commit/b1f52736ca4407110979e2c246ae002b89ed86ae)
#### Monday 2023-05-01 02:18:11 by Fluff

Loots, Loots, and More Loots

-Removed the gas in the phoron canisters, and added some chemdispensers in place of the sleeper
-Made the carbinter gun thing useable
-Hopefully made the pirate vessel worth visisting
-Changed the walls of the vox shuttle, adjusted the foes because the giant voxes just stop exsisting, and mercs should die quikly
-Slightly buffed red shuttle down loot.
-Buffed the loot of the blood church

---
## [JeromeFitz/websites](https://github.com/JeromeFitz/websites)@[3c58337227...](https://github.com/JeromeFitz/websites/commit/3c5833722792a496c7e7e2f14a8e60664bfb7596)
#### Monday 2023-05-01 02:35:45 by Jerome Fitzgerald

✨ NICE-23 app dir to use api not direct functions (#1554)

This _was_ working a-okay, but in a `canary` build this way of getting data within the app dir went the way of the `dodo`.

- https://nextjs.org/docs/messages/deopted-into-client-rendering

The reference hyper-focuses on `useSearchParams` but there is a _bit_ more to it. At least in the way this repo had things set up. I think it could also be the way it was doing a lot more than it should have and duplicating the `api` calls. However, originally, I thought that was the preference for RSC in that you did _not_ have to do an API call from RSC.

I digress. This is working much better, so this refactor (aka feature) is a stepped improvement for sure. At one point an update back on `canary` everything "looked good" but **tanked** RES (Real Experience Score). The Lighthouse was still `100` so this was weird.

Added bonus `ISR` now works again by following the `fetch` pattern more closely. And a proper `preload`.

- [x] upgrade to `next@13.3.0`
- [x] upgrade to `@vercel/og@0.5.2`, `swr@2.1.3`
- [x] Try and find what is causing the deopt
  - This was **three fold** at least: 1) `Analytics` 2) `CommandMenu` 3) `getNotionData`
- [x] Trial and Error on `colophon` so that it does not show: `page deopted into client-side rendering`
- [x] Migrate all `page.tsx` to this and update the Page/ Metadata/ Preload
- [x] Verify ISR
- [x] Determine if this works on Vercel

Yes the big callout is a bit of a hack. Since we _use_ the Next API to generate itself, this is probably anti-pattern. (Lol, this whole websites repo has been from day one.)

### `sites/jeromefitzgerald.com/src/lib/constants.ts`

This is a bit of a headache to look at so at some point we should refactor. This _requires_ the Production API to already exist. So this would work for this website, but not a net-new one. So need to also add to README or the call out in a comment here. I think this is kind of my problem with this site using Notion. Perhaps ... and hear me out here ... it was never a good idea to do this and spend this much time on it haha.

- Notion API is _a lot_
- We take the data and customize ("normalize") it to be digestible within this app an store the output in Redis
- We then use the Next API to call Redis and add some realtime flair from time to time

All of that is overcomplicated and probably not necessary. Or can be improved so let us first **fix** this and get back on canary latest and then see when (if ever) there is time to get out of this quagmire.

---
## [facebook/hhvm](https://github.com/facebook/hhvm)@[adc9644e45...](https://github.com/facebook/hhvm/commit/adc9644e459bdc1f8b1ec277ac4cdb9c4adab6f7)
#### Monday 2023-05-01 05:01:23 by Lucian Wischik

consolidate Errors.Parsing into Errors.Typing

Summary:
[This is part of an 19-diff stack whose purpose is to remove the redundant Errors.Parsing and Errors.Decl phases]

It used to be that ServerTypeCheck did as its first step **do_parsing** which (1) produced ASTs for the files that had changed, (2) extracted decls from that, and also FileInfo.t in order to update the forward and reverse naming-table. If there were parse-errors at this time, then
1. these errors were reported under `phase=Errors.Parsing`
2. an error meant that we continued to use whatever was the previous (successfully-parsed)  decl.
3. an error meant that subsequent steps like updating the naming-table **do_naming** `phase=Errors.Naming` and **do_type_checking** `phase=Errors.Typing` didn't get run on the files with parsing errors.

Steve Cao changed **do_parsing** to use the direct-decl-parser under a flag, and rjbailey recently removed the flag and deleted the non-direct-decl codepaths. With these changes, (1) no errors are produced during **do_parsing**, (2) decls are produced even for files with parse errors, (3) **do_type_checking** has to parse ASTs and emit the parsing errors, which it still does under the name `phase=Errors.Parsing` even though it now happens at the same time as `phase=Errors.Typing`.

This is quite a difference! It means that `phase=Errors.Parsing` is no longer a real phase in its own right, and should no longer be treated any differently from `phase=Errors.Typing`.

---------

## Why remove phase=Errors.Parsing

Note that phases are not user-visible. They're solely an internal machinery to help ServerTypeCheck decide what to do and when. They're not related to the "Parsing[1002]" or "Typing[4012]" messages that users see. Those are computed in User_error.ml:
```
let error_kind error_code =
  match error_code / 1000 with
  | 1 -> "Parsing"
  | 2 -> "Naming"
  | 3 -> "NastCheck"
  | 4 -> "Typing"
  | 5 -> "Lint"
  | 8 -> "Init"
  | _ -> "Other"
```

I asked folks about phases here: https://fb.workplace.com/groups/342676619986174/posts/1271105500476610

dlreeves wrote:
> For history around phases. Really early on in Hack (ie before I joined the team) Hack always initialized using a full init. The full init would follow phases Parsing -> Naming -> Decl -> Typing. Each phase would produce additional data that was stored in shared memory and a phase was not allowed to use data that was produced in a later phase. So for instance during Parsing we would store AST for each file. Then in Naming we would produce a named AST with some elaboration performed before folding decls during Decl phase.

> Errors would be reported at each phase a long the way. For instance checks that needed to be performed solely on the named ast became nast_checks. While errors that could be reported while declaring were decl errors. I believe the way it worked at the time is if there were errors in an earlier phase we wouldn’t proceed with checking until those errors were fixed (not 100% sure). We began changing most of how these phases worked during my first year on the team as we were running into scaling issues and were trying to get the early form of saved states working. One of the first changes was “lazy decls” that allowed us to proceed to the Typing phase and Decl dependencies as needed. This we no longer had an official decls phase. Instead we stored those decl errors in the folded results.

> Don’t know if any of this history was helpful, but we are so far removed from the original motivation of the phase concept that we should feel free to make it do what we want. Or remove the concept entirely if it serves no purpose.

Wilfred wrote:
> I don't see any value from the phases abstraction today.

I found the concept of phases confusing in various ways.
1. We're moving to a map/reduce model of checking, where the central process does as little work as possible, and the bulk of work is done by parallel workers. Phases get in the way of this. We'd much rather have *every single error* generated by the parallel workers, rather than some by the central process and others by the workers.
2. When I was writing streaming-errors, there was legacy code relating to phases which made the correctness quite subtle to reason about. (I had to stick in asserts and telemetry to validate that various paths weren't used). The reason is similar: I have to come up with principled invariants about when errors are appended to the streaming-errors-file, and prove that we've covered all errors, and phases made this tricker.
3. I think there were bugs in ServerTypeCheck associated with the fact that Errors.Parsing no longer happens prior to do_type_checking. There was also dead code associated with the fact that do_parsing no longer produces Errors.Parsing.

I think we'll be reducing our tech-debt to eliminate the concept!

## What this diff does

The previous diffs in the stack systematically examined and removed the places where we treated `phase=Errors.Parsing` specially. There are now no places anywhere in the codebase where it's treated any differently from `phase=Errors.Typing`.

This diff folds every use of `Errors.Parsing` into `Errors.Typing`.

## How to review this diff

Start with `errors.mli`. The entire rest of the diff is just a mechanical consequence.

Reviewed By: Wilfred

Differential Revision: D44861043

fbshipit-source-id: e46260828d82f29cc4a51788e6da7a04fa345e73

---
## [facebook/hhvm](https://github.com/facebook/hhvm)@[56cb5cddbe...](https://github.com/facebook/hhvm/commit/56cb5cddbeb405dd32a9d9ecbffe523b02e215b2)
#### Monday 2023-05-01 05:01:23 by Lucian Wischik

Which files need Naming/Parsing/Checking after saved-state init?

Summary:
[This is part of an 19-diff stack whose purpose is to remove the redundant Errors.Parsing and Errors.Decl phases]

It used to be that ServerTypeCheck did as its first step **do_parsing** which (1) produced ASTs for the files that had changed, (2) extracted decls from that, and also FileInfo.t in order to update the forward and reverse naming-table. If there were parse-errors at this time, then
1. these errors were reported under `phase=Errors.Parsing`
2. an error meant that we continued to use whatever was the previous (successfully-parsed)  decl.
3. an error meant that subsequent steps like updating the naming-table **do_naming** `phase=Errors.Naming` and **do_type_checking** `phase=Errors.Typing` didn't get run on the files with parsing errors.

Steve Cao changed **do_parsing** to use the direct-decl-parser under a flag, and rjbailey recently removed the flag and deleted the non-direct-decl codepaths. With these changes, (1) no errors are produced during **do_parsing**, (2) decls are produced even for files with parse errors, (3) **do_type_checking** has to parse ASTs and emit the parsing errors, which it still does under the name `phase=Errors.Parsing` even though it now happens at the same time as `phase=Errors.Typing`.

This is quite a difference! It means that `phase=Errors.Parsing` is no longer a real phase in its own right, and should no longer be treated any differently from `phase=Errors.Typing`.

Reading through the code in serverLazyInit for handling "dirty saved states" (i.e. those with errors), I believe it is simply stale -- hasn't been brought up to date with the changes I described above.

------------

Q1. Which files need be *named* i.e. populate the forward and reverse naming-table as part of saved-state init?
```
  let naming_files = ...
      [
        naming_and_parsing_error_files;
        dirty_naming_files;
        dirty_master_files;
        dirty_local_files;
        changed_while_parsing;
      ]
```
BEFORE: `naming_and_parsing_error_files` (i.e. those which had `phase=Errors.(Naming|Parsing)` errors in the dirty saved-state) plus those that have been changed on disk since the saved-state

AFTER: `naming_error_files` (i.e. those which had `phase=Errors.Naming` errors in the dirty saved-state) plus those that have been changed on disk since the saved state.

There's no reason to put `phase=Errors.Parsing` errors through naming. That doesn't make sense any more. Actually, strictly speaking, we never in practice allow saved-state generation when there are `phase=Errors.Naming`, so this will be empty. I'll add an assert for this in a future diff.

-----------

Q2. Which files need to be in `disk_needs_parsing`, so that the deferred ServerTypeCheck will put them through naming and fanout calculation?
```
        (* The only reason old_parsing_error_files are added to disk_needs_parsing
                   here is because of an issue that seems to be already tracked in T30786759 *)
        disk_needs_parsing = old_parsing_error_files;
```
BEFORE: as a hack, those which had `phase=Errors.Parsing` in the dirty saved-state. When this hack was first written, Kasper the code-reviewer asked for it not to be included; he said that it would be better to understand what was going on https://www.internalfb.com/diff/D9932749?dst_version_fbid=528779804211925&transaction_fbid=1848903675145188. But the code was landed anyway. The underlying bug for which this was claimed to workaround was reaped T30786759.

AFTER: none. There's no need for the deferred ServerTypeCheck to do any naming or fanout calculation. That's because we've done all the naming and fanout work already.

------------------

Q3. Which files need be in `needs_recheck`, so that the deferred ServerTypeCheck will recheck them all with a call to **do_type_checking**? (note: in addition to these, we'll also do fanout).
```
        needs_recheck =
          Relative_path.Set.union env.needs_recheck decl_and_typing_error_files;
```
BEFORE: well, `env.needs_recheck` is empty (I'll add an assert in a future diff), so it's just `decl_and_typing_error_files` i.e. those errors that had `phase=Errors.(Decl|Typing)`.

AFTER: this diff changes it to include *all* error files from the dirty saved-state, no matter which phase they came in. I think it's clear that they do all need to be typechecked (so that `env.errors` can be populated).

Why weren't the ones from `phase=Errors.Parsing` included here? -- well, they were in `disk_needs_parsing`, so they'd have been done.

What about the ones with `phase=Errors.Naming`? Well, those duplicate-name-errors have already been reported by the earlier call to `update_reverse_naming_table_from_env_and_get_duplicate_name_errors`. But there's no great harm in typechecking them as well.

-----------------

Q4. In addition to the files we already identified in `needs_recheck`, we also need an additional *fanout calculation*. Which files should contribute to this fanout calculation?
```
    calculate_fanout_and_defer_or_do_type_check
      genv
      env
      old_naming_table
      defs_per_file
      ~dirty_master_files_unchanged_hash
      ~dirty_master_files_changed_hash
      ~dirty_local_files_unchanged_hash
      ~dirty_local_files_changed_hash
      t
      cgroup_steps
```
How do all those parameters contribute to the initial fanout calculation? It's honestly quite hard to say!

This diff makes a change here: `defs_per_file` used to be the FileInfo.t of changed files plus those with `phase=Errors.(Naming|Parsing)` in the dirty saved-state, but in this diff it no longer includes `phase=Errors.Parsing`.

Well, `defs_per_file` is used in two ways. First, for sake of decl-diffing the dirty files, it judges whether the new defs in `defs_per_file` differ from those in `old_naming_table`. This is fine because `defs_per_file` already includes all the dirty files; including `phase=Errors.Parsing` should have no effect.

Second, for the files we feed into `oldify_type_decl` and `redo_type_decl`, we look within `defs_per_file` to find the new FileInfo.t for the files in question. Again this doesn't make sense to include `phase=Errors.Parsing`.

Reviewed By: CatherineGasnier

Differential Revision: D45011521

fbshipit-source-id: ffd99f75c35e923aa3e37c2a54671a590669427b

---
## [meemofcourse/Shiptest](https://github.com/meemofcourse/Shiptest)@[7df4885117...](https://github.com/meemofcourse/Shiptest/commit/7df4885117a4a12ea333934d5af92e0766c84c5d)
#### Monday 2023-05-01 05:06:21 by Mark Suckerberg

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
## [danhancach/voidUI_frameworks_base](https://github.com/danhancach/voidUI_frameworks_base)@[98a1d4eae7...](https://github.com/danhancach/voidUI_frameworks_base/commit/98a1d4eae702afd88d862acdf1e93be5c07bc360)
#### Monday 2023-05-01 06:28:20 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6

---
## [ROS-Spanish-Users-Group/ros2_documentation](https://github.com/ROS-Spanish-Users-Group/ros2_documentation)@[1be681dc76...](https://github.com/ROS-Spanish-Users-Group/ros2_documentation/commit/1be681dc76d573c3bc20e9b7f943e906af820a32)
#### Monday 2023-05-01 06:58:04 by Chris Lalancette

First pass at the Iron Irwini release notes. (#3395)

* First pass at the Iron Irwini release notes.

That is, add in the full changelog, and also greatly
expand the release notes themselves.

I should point out that the full changelog is necessarily
*not* complete; it only contains information on things that
have already been released.

The release note page is a cut-down version of the full
changelog that just has things that might be interesting
to end users.  What is currently in there was my opinion,
so this list may be expanded or reduced based on thoughts
from other people.

In both cases, we should be able to iteratively add new
items here as they are landed.

Signed-off-by: Chris Lalancette <clalancette@gmail.com>
Co-authored-by: G.A. vd. Hoorn <g.a.vanderhoorn@tudelft.nl>

---
## [LastWow-Core/lastwow-lk](https://github.com/LastWow-Core/lastwow-lk)@[ef949f9ff0...](https://github.com/LastWow-Core/lastwow-lk/commit/ef949f9ff0a89e837c67258d7e199da1706bc438)
#### Monday 2023-05-01 07:57:26 by ICXCNIKA

fix(DB/Locale): deDE fix request items texts #02 (#14615)

Process of translation: only original sources of deDE texts by
researching multiple sources, reverse translation by searching for
related quest items/NPCs and using these names to reconstruct a proper
translation.

This fixes the terms

Coldtooth-Mine (Eisbeißermine), Doomhammer (Schicksalshammer), Fizzle
(Zischel), Fizzledowser (Rutenwünschels), Fizzlebub (Zischelbub),
Burning Blade (Brennende Klinge), Ashenvale (Eschental),
Bloodscalp/s/stamm (Blutskalpe, Blutskalpstamm),
Darkspeartrolle/Darkspears/Darkspearstamm (Dunkelspeere,
Dunkelspeertrolle, -stamm), Moonglade (Mondlichtung), Starblaze
(Sternenschauer), Shadowglen (Laubschattental), Darrowshire (Darroheim),
Booty Bay (Beutebucht), Ratchet (Ratschet), Dizzywig (Flunkerblick),
Hearthglen (Herdweiler), Chillwindspitze (Zugwindspitze), Stormrage
(Sturmgrimm), Stormpike (Sturmlanze/n), Ironforge (Eisenschmiede),
Thunderhorn (Donnerhörner), Steamboil (Kesseldampf), Twilight-Hammer,
-klan (Schattenhammer/Schattenhammerklan), Fathom-Kern (Tiefenkern),
Blackfathom Deeps (Tiefschwarze Grotte), Blackrock-* (Schwarzfels-*),
Hawkwind (Falkenwind), Feathermoon (Mondfeder), Moonrage (Mondzorn),
Firemane (Feuermähne), Searingblade (Sengende Klinge), Ragefireabgrund
(Flammenschlund), Ironbands Areal (Eisenbands Lager), Zandalar
(Zandalari), Southshore (Süderstade)

for quest progress/request text entries for the deDE localisation with
proper casus/declension (these are not proper translated names of
locations/NPCs that have been left over by Blizzard since their language
localisations in TBC in 2006 and onward).

Added missing progress/request text entries for 308, 311, 417, 1644,
1787, 5059, 5060, 5721, 6004, 6023, 6025, 6187, 8042, 8043, 8044, 8046,
8047, 8048, 8050-8079, 8102, 8107, 8108, 8111, 8112, 8113, 8117, 8118,
8142, 8143, 8147, 8183-8195, 8238, 8239, 8240, 8243, 8246, 8860, 9594,
9692, 9707, 10414, 10415, 10919, 11451. (A lot of them are
Zandalari/Zul'Gurub related quests.)

Replaced post-Cataclysm progress/request text entries for 933, 935,
6387, 7383.

Fixed a wrong $R with plain text at progress/request text for 9147.

Added missing female gender equivalent to 6391.

(There are probably more changes in the file that aren't further
explained here as it was hard to keep track of everything. If you think
I made a mistake or have questions please contact me directly.)

<!-- First of all, THANK YOU for your contribution. -->

## Changes Proposed:
-  Fixing a lot in the quest_request_items_locale table.

## Issues Addressed:
<!-- If your fix has a relating issue, link it below -->
- Fixing some of the tasks in
https://github.com/azerothcore/azerothcore-wotlk/issues/14244
Referring to my other two bug reports from CC Github:
- https://github.com/chromiecraft/chromiecraft/issues/4697
- https://github.com/chromiecraft/chromiecraft/issues/4745

## SOURCE:
<!-- If you can, include a source that can strengthen your claim -->
- Read the text on top.

## Tests Performed:
<!-- Does it build without errors? Did you test in-game? What did you
test? On which OS did you test? Describe any other tests performed -->
- Not tested.


## How to Test the Changes:
<!-- Describe in a detailed step-by-step order how to test the changes
-->
All of the changes are to reward texts of quests, can be tested by
completing quests or simply reviewing the changed file.

## Known Issues and TODO List:
<!-- Is there anything else left to do after this PR? -->

- [ ]
- [ ]

<!-- If you intend to contribute repeatedly to our project, it is a good
idea to join our discord channel. We set ranks for our contributors and
give them access to special resources or knowledge:
https://discord.com/invite/DasJqPba)
Do not remove the instructions below about testing, they will help users
to test your PR -->
## How to Test AzerothCore PRs
 
When a PR is ready to be tested, it will be marked as **[WAITING TO BE
TESTED]**.

You can help by testing PRs and writing your feedback here on the PR's
page on GitHub. Follow the instructions here:

http://www.azerothcore.org/wiki/How-to-test-a-PR

**REMEMBER**: when testing a PR that changes something **generic** (i.e.
a part of code that handles more than one specific thing), the tester
should not only check that the PR does its job (e.g. fixing spell XXX)
but **especially** check that the PR does not cause any regression (i.e.
introducing new bugs).

**For example**: if a PR fixes spell X by changing a part of code that
handles spells X, Y, and Z, we should not only test X, but **we should
test Y and Z as well**.

---
## [phoebenamyalo/Data-Analysis-with-SQL](https://github.com/phoebenamyalo/Data-Analysis-with-SQL)@[c703aac997...](https://github.com/phoebenamyalo/Data-Analysis-with-SQL/commit/c703aac997a584ef6e7f929a803a00f73edb09f7)
#### Monday 2023-05-01 08:10:01 by phoebenamyalo

Add files via upload

Practice SQL – 10 Final Query Questions
Exercise 1
Find the average salary of the male and female employees in each department.
Exercise 2
Find the lowest department number encountered in the 'dept_emp' table. Then, find the highest department number.
Exercise 3
Obtain a table containing the following three fields for all individuals whose employee number is not greater than 10040:
- employee number
- the lowest department number among the departments where the employee has worked in (Hint: use
a subquery to retrieve this value from the 'dept_emp' table)
- assign '110022' as 'manager' to all individuals whose employee number is lower than or equal to 10020, and '110039' to those whose number is between 10021 and 10040 inclusive.

Exercise 4
Retrieve a list of all employees that have been hired in 2000.
     
Exercise 5
Retrieve a list of all employees from the ‘titles’ table who are engineers.
Repeat the exercise, this time retrieving a list of all employees from the ‘titles’ table who are senior engineers.
After LIKE, you could indicate what you are looking for with or without using parentheses. Both options are correct and will deliver the same output. We think using parentheses is better for legibility and that’s why it is the first option we’ve suggested.
Exercise 6
Create a procedure that asks you to insert an employee number and that will obtain an output containing the same number, as well as the number and name of the last department the employee has worked in.
Finally, call the procedure for employee number 10010.
If you've worked correctly, you should see that employee number 10010 has worked for department number 6 - "Quality Management".
Exercise 7
How many contracts have been registered in the ‘salaries’ table with duration of more than one year and of value higher than or equal to $100,000?
Hint: You may wish to compare the difference between the start and end date of the salaries contracts.
Exercise 8
Create a trigger that checks if the hire date of an employee is higher than the current date. If true, set the hire date to equal the current date. Format the output appropriately (YY-mm-dd).
Extra challenge: You can try to declare a new variable called 'today' which stores today's data, and then use it in your trigger!
After creating the trigger, execute the following code to see if it's working properly.
Exercise 9
Define a function that retrieves the largest contract salary value of an employee. Apply it to employee number 11356.
In addition, what is the lowest contract salary value of the same employee? You may want to create a new function that to obtain the result.
     
Exercise 10
Based on the previous exercise, you can now try to create a third function that also accepts a second parameter. Let this parameter be a character sequence. Evaluate if its value is 'min' or 'max' and based on that retrieve either the lowest or the highest salary, respectively (using the same logic and code structure from Exercise 9). If the inserted value is any string value different from ‘min’ or ‘max’, let the function return the difference between the highest and the lowest salary of that employee.

---
## [toolmind/cmss13](https://github.com/toolmind/cmss13)@[4cf0651670...](https://github.com/toolmind/cmss13/commit/4cf06516705b3e0f4a6f446cd36eaa15b554a561)
#### Monday 2023-05-01 08:16:45 by BlackCrystalic

Fixes queen stat bug (#3168)

# About the pull request

Good morning VIETNAM!
That again happened! We found some mistake!

# Explain why it's good for the game

That not good for game, because I fixend so usual staff, like timer for
queen, he can abuse that to make engage on last second and marines -
bruh, young queen, FIGHT! and BANG! Screech on ALL marines... Stupid
folks.

(devs trying to find and fix bugs)
https://www.youtube.com/watch?v=ryNSpF9I3rE

# Changelog

:cl:
fix: Stat proc replaced with get_status_tab_items, fixed issue with
QUEEN additional status
/:cl:

Co-authored-by: BlackCrystalic <blackcrystalic@inbox.ru>

---
## [toolmind/cmss13](https://github.com/toolmind/cmss13)@[b451aba2d4...](https://github.com/toolmind/cmss13/commit/b451aba2d4fd87a3b5cceaaba6955b8b783f84b2)
#### Monday 2023-05-01 08:16:45 by Hopekz

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
## [SyncIt21/The-TG-Station-Fork](https://github.com/SyncIt21/The-TG-Station-Fork)@[fa0225b05c...](https://github.com/SyncIt21/The-TG-Station-Fork/commit/fa0225b05c5411c46187f67816f8363e7dd91f30)
#### Monday 2023-05-01 08:30:23 by san7890

Converts Spiderlings from Structures to Basic Mobs (#75001)

If I could've made this more atomic, I would have in a heartbeat, trust
me.

## About The Pull Request

Hey there. People were mocking us for having spiderlings still be a
subtype of `/obj/structure`. I decided to take a lot of time to fix
that. A lot of behavior it was implementing was just pseudo-mob stuff,
so it was actually easier than it looked for the raw conversion. A lot
of the footwork on spider stuff in the basic framework was already done
previously by Jacquerel, so that was pretty nice.

However, there are two new things that weren't introduced in the code
that had to be put in.

A) A component to handle growth and differentiation into a mob. This may
have already existed, no clue. If it does (and it's NOT
evolutionary_leap), let me know.
B) AI Behavior to handle seeking out a vent, entering a vent, and then
exiting out of a different vent. I may have gone a bit wacky on the
code, but it certainly works as expected (spiderling goes in one vent,
exits the other). Let me know if you can think of a way it can be better
optimized, but it was deliberately written to be very failsafey in case
shit goes yonkers.

One fundamental difference between structure spiderlings and basic mob
spiderlings (beyond the AI and not just a random prob() check for
movement) is the fact that they had vent movement coded in... but we
_really_ don't need stuff like that for our intents and purposes. If the
range turns out to be too OP in the current framework, we can always
change it up a bit, but also there's a _lot_ of vents we can end up in
the station (my testing had one spiderling end up in the AI sat to get
obliterated).
## Why It's Good For The Game

Spiderlings aren't structures! They behave like a mob should! Players
can possess spiderlings! They work seamlessly with differentiating into
a giant spider! Better AI! More room for people to add into this very
under-utilized buggers!
## Changelog
:cl:
refactor: Spiderlings are now basic mobs, report any complete
weirdness/deviation from known behavior. They should be a lot more
intelligent now though.
add: AI Spiderlings are super fragile, but they're also super fast,
especially when they get into a vent. Once they're in circulation, they
could end up everywhere! Maybe in the armory, maybe in a locked closet
in maintenance. Be sure to be vigilant and splat them whenever you can
to save the station from a whole lotta heartache!
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[edabb9be67...](https://github.com/Paxilmaniac/Skyrat-tg/commit/edabb9be679c65f176532670b339d9adc859e664)
#### Monday 2023-05-01 11:03:33 by SkyratBot

[MIRROR] Stops station blueprints from expanding areas of non atmos adjacent turfs. [MDB IGNORE] (#20480)

* Stops station blueprints from expanding areas of non atmos adjacent turfs. (#74620)

## About The Pull Request
Fixes #74605

the problem starts with `detect_room()` proc. This proc returns turfs
even those with `atmos_adjacent_turfs` = null. This means it returns
turfs that has a wall, airlock, window etc i.e. whatever that stops air
from flowing through it. This coupled together with `create_area()`
causes some wierdness.

Let's take an example
![Screenshot
(154)](https://user-images.githubusercontent.com/110812394/230769831-e84819f2-31b2-4a67-a8bb-5e07e1c5a1cc.png)

Area A is well defined i.e. it has been created via the station
blueprints and is highlighted in green, Area B however is only
theoretical i.e. we haven't created it yet or we are about to create it.
Now you might be thinking Area A is completely walled & sealed off, it
should be physically impossible to expand it unless we broke down one of
it's walls and so since we are standing in Area B it shoudn't even give
me the option to expand area A Right? right? r.i.g.h.t?
![Screenshot
(155)](https://user-images.githubusercontent.com/110812394/230770056-169cbab3-4516-4da7-ae2c-4f40b50be9ba.png)
Well PHFUUK. The area editor completely ignores the laws of physics and
allows me expand Area A anyway. This could cause some real power gaming
shit because if you create an area next to an area having an APC you
could use that area power without even making your own apc by simply
expanding that area(like using someone else's wifi from outside their
house without them even knowing)

#73850 accidently built on top of this as it relied on this to detect
duplicate APC's but the checks became way too strict as it would check
areas of surrounding walls for apc's and throw the conflicting apc
error. You can now build room's next to each other even if they have
fuctioning apc's however you still can't build rooms in space on top of
shuttle walls because that's been the default behaviour for years and
hasn't been touched one bit.

## Changelog
:cl:
fix: station blueprints no longer expands & detects areas of non atmos
adjacent turfs.
/:cl:

* Stops station blueprints from expanding areas of non atmos adjacent turfs.

---------

Co-authored-by: SyncIt21 <110812394+SyncIt21@users.noreply.github.com>

---
## [Firestorm01X2/Cataclysm-BN](https://github.com/Firestorm01X2/Cataclysm-BN)@[08d54d0287...](https://github.com/Firestorm01X2/Cataclysm-BN/commit/08d54d0287a1313cb810a1d3d74ca0e531189ae1)
#### Monday 2023-05-01 12:14:14 by KheirFerrum

Fix MGOAL_FIND_ITEM_GROUP, fix up some code (#2546)

* Reorganize

Code still sucks. In particular recruit_class doesn't compare properly with npc->my_class so MGOAL_RECRUIT_NPC_CLASS fails horribly even if you fix up that area of code to it actually points to type->recruit_class instead of recruit_class

For that matter mission has a select copy of several mission type defs and I can only assume this is due to legacy fuckery.

* Fix mission.cpp

Now will only allow you to select items if you have enough of them, and will only consume the necessary amount.

Added documentation for MGOAL_FIND_ITEM_GROUP

Thank god this wasn't too much work.

---
## [ravikul505/MindZero](https://github.com/ravikul505/MindZero)@[96778aea08...](https://github.com/ravikul505/MindZero/commit/96778aea08807f321f83df4516062e87243e0a79)
#### Monday 2023-05-01 12:25:23 by gon araseon

debugging and change of ideas

holy fucking  shit this ain't easy

---
## [jhh67/chapel](https://github.com/jhh67/chapel)@[724ad6243a...](https://github.com/jhh67/chapel/commit/724ad6243a1b00d9373624045d512aa525d23498)
#### Monday 2023-05-01 13:53:49 by Andy Stone

Make gpu SDK version checking code more robust (#22198)

This PR (https://github.com/chapel-lang/chapel/pull/22170) introduced
code that validates the installed version of a GPU SDK (i.e. CUDA or
ROCm). My validation code works by looking for a certain file that
contains the version; unfortunately it looks like the name of this file
is different for different versions of both CUDA and ROCm. This PR
updates to look for other known names/formats.

Since this is failing our nightly tests I plan to merge this quickly but
we may want to consider if this is robust enough to handle future
versions or deal with versions that we say we're supporting but haven't
explicitly tested. Some thoughts:

- We could compile a small program using CUDA/ROCm that calls the API to
report the version and use that. This seems awfully heavy-handed to me.
- We could also consider not erroring if we can't find the file. IOW we
only error if we can prove the user has a version we know not to work
rather than erroring that we can't validate that they have a working
version.

Also note that the error we produce today looks like this:

```
Error: Unable to determine CUDA version. To avoid this issue, you can have GPU code run on the CPU by setting 'CHPL_GPU_CODEGEN=none'. To turn this error into a warning set CHPLENV_GPU_REQ_ERRS_AS_WARNINGS.
```

which, gives a workaround (set `CHPLENV_GPU_REQ_ERRS_AS_WARNINGS`) so if
this regresses there is a workaround presented.

[Reviewed by nobody; updates to fix failing nightly build]

---
## [avar/git](https://github.com/avar/git)@[69bbbe484b...](https://github.com/avar/git/commit/69bbbe484ba10bd88efb9ae3f6a58fcc687df69e)
#### Monday 2023-05-01 14:21:44 by Jeff King

hash-object: use fsck for object checks

Since c879daa237 (Make hash-object more robust against malformed
objects, 2011-02-05), we've done some rudimentary checks against objects
we're about to write by running them through our usual parsers for
trees, commits, and tags.

These parsers catch some problems, but they are not nearly as careful as
the fsck functions (which make sense; the parsers are designed to be
fast and forgiving, bailing only when the input is unintelligible). We
are better off doing the more thorough fsck checks when writing objects.
Doing so at write time is much better than writing garbage only to find
out later (after building more history atop it!) that fsck complains
about it, or hosts with transfer.fsckObjects reject it.

This is obviously going to be a user-visible behavior change, and the
test changes earlier in this series show the scope of the impact. But
I'd argue that this is OK:

  - the documentation for hash-object is already vague about which
    checks we might do, saying that --literally will allow "any
    garbage[...] which might not otherwise pass standard object parsing
    or git-fsck checks". So we are already covered under the documented
    behavior.

  - users don't generally run hash-object anyway. There are a lot of
    spots in the tests that needed to be updated because creating
    garbage objects is something that Git's tests disproportionately do.

  - it's hard to imagine anyone thinking the new behavior is worse. Any
    object we reject would be a potential problem down the road for the
    user. And if they really want to create garbage, --literally is
    already the escape hatch they need.

Note that the change here is actually in index_mem(), which handles the
HASH_FORMAT_CHECK flag passed by hash-object. That flag is also used by
"git-replace --edit" to sanity-check the result. Covering that with more
thorough checks likewise seems like a good thing.

Besides being more thorough, there are a few other bonuses:

  - we get rid of some questionable stack allocations of object structs.
    These don't seem to currently cause any problems in practice, but
    they subtly violate some of the assumptions made by the rest of the
    code (e.g., the "struct commit" we put on the stack and
    zero-initialize will not have a proper index from
    alloc_comit_index().

  - likewise, those parsed object structs are the source of some small
    memory leaks

  - the resulting messages are much better. For example:

      [before]
      $ echo 'tree 123' | git hash-object -t commit --stdin
      error: bogus commit object 0000000000000000000000000000000000000000
      fatal: corrupt commit

      [after]
      $ echo 'tree 123' | git.compile hash-object -t commit --stdin
      error: object fails fsck: badTreeSha1: invalid 'tree' line format - bad sha1
      fatal: refusing to create malformed object

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [Rex9001/Rex-station-](https://github.com/Rex9001/Rex-station-)@[3fdd716da5...](https://github.com/Rex9001/Rex-station-/commit/3fdd716da5bfd2aab2be37489b4ac39f4be7e632)
#### Monday 2023-05-01 15:18:49 by Cheshify

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
## [Rex9001/Rex-station-](https://github.com/Rex9001/Rex-station-)@[43473a4dac...](https://github.com/Rex9001/Rex-station-/commit/43473a4dac07c40faed45808b61b9c6de46ffcb6)
#### Monday 2023-05-01 15:18:49 by san7890

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
## [lunar-begonia/android_kernel_xiaomi_mt6785](https://github.com/lunar-begonia/android_kernel_xiaomi_mt6785)@[4d368e10b1...](https://github.com/lunar-begonia/android_kernel_xiaomi_mt6785/commit/4d368e10b1ef1ac8babf27ec9dfcd4a3a5fdeb3e)
#### Monday 2023-05-01 15:28:30 by Peter Zijlstra

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

---
## [Sakamoto4ka/tgstation](https://github.com/Sakamoto4ka/tgstation)@[d43ebd042d...](https://github.com/Sakamoto4ka/tgstation/commit/d43ebd042dd751842728e8cb91fa7fc1a82f26d0)
#### Monday 2023-05-01 15:41:56 by san7890

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
## [Sakamoto4ka/tgstation](https://github.com/Sakamoto4ka/tgstation)@[40fc11eb07...](https://github.com/Sakamoto4ka/tgstation/commit/40fc11eb0733ca25eff56e7379cb574a997fb6d3)
#### Monday 2023-05-01 15:41:56 by LemonInTheDark

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
## [nikothedude/Skyrat-tg](https://github.com/nikothedude/Skyrat-tg)@[c5a7f5a7c9...](https://github.com/nikothedude/Skyrat-tg/commit/c5a7f5a7c93f96cc047297ed8ee61cce02626c75)
#### Monday 2023-05-01 15:43:56 by SkyratBot

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
## [daplcor/KU](https://github.com/daplcor/KU)@[77a09e5ffb...](https://github.com/daplcor/KU/commit/77a09e5ffbf6d1ea7f7df6d8a0e251bb830a712f)
#### Monday 2023-05-01 15:49:24 by AmirDapl

headache

Might have made my repl too stupid, but I can't for the life of me mint with collection-policy.  Collections work fine, but here we are.  need to figure out why ledger isn't finding tokens but token-policy sees it.

---
## [Helg2/tgstation](https://github.com/Helg2/tgstation)@[4014aef4b0...](https://github.com/Helg2/tgstation/commit/4014aef4b0a24d260b314f462a21f943c3d62894)
#### Monday 2023-05-01 15:54:46 by Bloop

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
## [PeterFalken/cockpit](https://github.com/PeterFalken/cockpit)@[29500b32c6...](https://github.com/PeterFalken/cockpit/commit/29500b32c66dff16ec4aabf119a5772f007a007e)
#### Monday 2023-05-01 16:06:07 by Martin Pitt

ws: Disallow direct URL logins with LoginTo=false

The current documentation of LoginTo= isn't very specific about what
exactly happens with a "false" value; but it is plausible for an admin
to assume that "false" would disallow logging into a remote host
completely -- not merely hide the "Connect to:" field and then allowing
a direct URL login anyway.

It is sometimes important to disallow direct SSH logins from the login
page on publicly exposed bastion hosts, as this functionality allows
unauthenticated remote users to:

 - scan the internal network for existing hosts, which might otherwise
   not be accessible directly from the internet
   (Fixes #18540, https://bugzilla.redhat.com/show_bug.cgi?id=2167006)

 - scan the cockpit-ws host or internal network hosts for open ports
   (Fixes #15077, https://bugzilla.redhat.com/show_bug.cgi?id=2018741)

So change ws to reject direct URL logins with `LoginTo=false`. This
happens most naturally in cockpit_session_launch(), as we still want to
allow remote URLs from the shell's host switcher in already
authenticated sessions. This will not produce a very friendly error
message, but it doesn't have to be -- at that point specifying direct
URLs can be considered hacking anyway.

Clarify the documentation accordingly.

---
## [mirandadam/evals](https://github.com/mirandadam/evals)@[114f4f8536...](https://github.com/mirandadam/evals/commit/114f4f8536f29df43e5145fd38826285d19d6728)
#### Monday 2023-05-01 16:20:12 by Greg Priday

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
## [mirandadam/evals](https://github.com/mirandadam/evals)@[bb42b3149c...](https://github.com/mirandadam/evals/commit/bb42b3149cd7a078cf44136e93a24f2156419acc)
#### Monday 2023-05-01 16:20:12 by David Chen

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
## [mirandadam/evals](https://github.com/mirandadam/evals)@[733167aed6...](https://github.com/mirandadam/evals/commit/733167aed6624945acdc51ec11407484dd2d931b)
#### Monday 2023-05-01 16:20:12 by Andrew

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
## [ca2/graphics3d-port](https://github.com/ca2/graphics3d-port)@[dbcf0d8568...](https://github.com/ca2/graphics3d-port/commit/dbcf0d8568d26a3e0fc6945af2f608e25a8c951b)
#### Monday 2023-05-01 17:13:00 by Camilo Sasuke Thomas Borregaard Sørensen

<3ThomasBS_ILoveYOU!! [ macOS : day 25 ] ca2 Stabilization and continuous integration and deployment implementation
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
## [oxidecomputer/omicron](https://github.com/oxidecomputer/omicron)@[ccc28fe4c8...](https://github.com/oxidecomputer/omicron/commit/ccc28fe4c857c08599f5d9d6eff6ecfcaa298eb6)
#### Monday 2023-05-01 18:16:10 by Sean Klein

[sled-agent] Refactor service management out of `StorageManager` (#2946)

## History

The Sled Agent has historically had two different "managers" responsible
for Zones:

1. `ServiceManager`, which resided over zones that do not operate on
Datasets
2. `StorageManager`, which manages disks, but also manages zones which
operate on those disks

This separation is even reflected in the sled agent API exposed to Nexus
- the Sled Agent exposes:

- `PUT /services`
- `PUT /filesystem`

For "add a service (within a zone) to this sled" vs "add a dataset (and
corresponding zone) to this sled within a particular zpool".

This has been kinda handy for Nexus, since "provision CRDB on this
dataset" and "start the CRDB service on that dataset" don't need to be
separate operations. Within the Sled Agent, however, it has been a
pain-in-the-butt from a perspective of diverging implementations. The
`StorageManager` and `ServiceManager` have evolved their own mechanisms
for storing configs, identifying filesystems on which to place zpools,
etc, even though their responsibilities (managing running zones) overlap
quite a lot.

## This PR

This PR migrates the responsibility for "service management" entirely
into the `ServiceManager`, leaving the `StorageManager` responsible for
monitoring disks.

In detail, this means:

- The responsibility for launching Clickhouse, CRDB, and Crucible zones
has moved from `storage_manager.rs` into `services.rs`
- Unfortunately, this also means we're taking a somewhat hacky approach
to formatting CRDB. This is fixed in
https://github.com/oxidecomputer/omicron/pull/2954.
- The `StorageManager` no longer requires an Etherstub device during
construction
- The `ServiceZoneRequest` can operate on an optional `dataset` argument
- The "config management" for datastore-based zones is now much more
aligned with non-dataset zones. Each sled stores
`/var/oxide/services.toml` and `/var/oxide/storage-services.toml` for
each group.
- These still need to be fixed with
https://github.com/oxidecomputer/omicron/issues/2888 , but it should be
simpler now.
- `filesystem_ensure` - which previously asked the `StorageManager` to
format a dataset and also launch a zone - now asks the `StorageManager`
to format a dataset, and separately asks the `ServiceManager` to launch
a zone.
- In the future, this may become vectorized ("ensure the sled has *all*
the datasets we want...") to have parity with the service management,
but this would require a more invasive change in Nexus.

---
## [Cl3v3rbot/cmss13](https://github.com/Cl3v3rbot/cmss13)@[030a68f6ac...](https://github.com/Cl3v3rbot/cmss13/commit/030a68f6ac59efa5b7c02f1f9a421b3bd95fd0b3)
#### Monday 2023-05-01 18:36:09 by carlarctg

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
## [Cl3v3rbot/cmss13](https://github.com/Cl3v3rbot/cmss13)@[0bc21524a1...](https://github.com/Cl3v3rbot/cmss13/commit/0bc21524a123944a37d45e1088dca13476824b9c)
#### Monday 2023-05-01 18:36:09 by carlarctg

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
## [bhearsum/firefox-translations-training](https://github.com/bhearsum/firefox-translations-training)@[039d3db86c...](https://github.com/bhearsum/firefox-translations-training/commit/039d3db86c85dfdede6ac250fc349ac5b1845365)
#### Monday 2023-05-01 18:40:49 by Ben Hearsum

Add toolchain tasks for things that we depend on to train language models.

Most of these are straight forward download and compiles, but there's a few callouts:
- The CLI tools (marian, fast-align, etc.) already have build scripts used by the existing pipeline. For the most part, I'm just replacing them with my own version because they're just unpack/make/cmake. The exception is Marian, which has a little bit more going on with cmake definitions. Maybe I should just copy those in here though?
- Some Python modules that don't have binary wheels available, which we ought to build to avoid needing to compile them at the start of training tasks.
- CUDA (a NVIDIA Toolkit) is a huge pain. They don't have any real advertised way to just dump the files you want into a directory (they want you to run an installer). I _think_ I managed to get this work, but it's possible this will need a tweak in the future if a future task has trouble with the current toolchain.

This also necessitated switching Docker images to Ubuntu, because some tools were not reasonably possible to make work on Alpine.

---
## [Iajret/tgstation](https://github.com/Iajret/tgstation)@[129c74c945...](https://github.com/Iajret/tgstation/commit/129c74c945a3fe0bce2c29065f69424ce8551670)
#### Monday 2023-05-01 18:43:58 by carlarctg

EMPs on robotic limbs will now disable them for 4-8 seconds rather than causing a 10-20 second full stun (#74570)

## About The Pull Request

EMPs on robotic limbs will now disable them for 10-20 seconds rather
than causing a 10-20 second full stun on the user. Additionally, they
will damage the limb for a little brute and some burn.

Arm EMPs don't do anything special as the limb being disabled already
drops items.

Leg EMPs cause a 10-20 second knockdown, only really applicable if
there's only one robotic leg as two disabled legs KD you anyways.

Chest EMPs cause a 3-6 second standing-up paralyze, visible to the
player by a quite noticeable shaking of their body.

Head EMPs break the optical transponder circuits for 7.5-15 seconds,
effectively giving the user nightmare goggles vision with green instead
of red as the only remaining color.

Tacit approval for the PR at least existing.

![image](https://user-images.githubusercontent.com/53100513/230537462-b06d0bb5-0607-4f83-954c-6b2a0bcdc635.png)
## Why It's Good For The Game

Robotic limbs are not so strong that a glancing EMP that may not even
have been directed at you should stun you for ten, TEN seconds, or
worse, twenty. This is basically legacy stunning from the days of
super-stuns on soap, stunbatons, etc. The code for it was last touched
six years ago.

**_The stats as shown above are not even close to final. I really don't
know or care what the right stats should be in the end. and I'm fine
with making them a 10-20 second timer again. I just put some
reasonable-seeming numbers in as a placeholder. EMPs could also still
cause a short stun if that is deemed necessary. Hell, that could be the
chest effect!_**
## Changelog
:cl:
balance: EMPs on robotic limbs will now disable them for 10-20 seconds
rather than causing a 10-20 second full stun on the user. Additionally,
they will damage the limb for a little brute and some burn.
EMPs on robotic limbs will now disable them for 10-20 seconds rather
than causing a 10-20 second full stun on the user. Additionally, they
will damage the limb for a little brute and some burn.
balance: Arm EMPs don't do anything special as the limb being disabled
already drops items.
balance: Leg EMPs cause a 10-20 second knockdown, only really applicable
if there's only one robotic leg as two disabled legs KD you anyways.
balance: Chest EMPs cause a 3-6 second standing-up paralyze, visible to
the player by a quite noticeable shaking of their body.
balance: Head EMPs break the optical transponder circuits for 7.5-15
seconds, effectively giving the user nightmare goggles vision with green
instead of red as the only remaining color.
/:cl:

---
## [Squishypone/tgstation](https://github.com/Squishypone/tgstation)@[200b739c0a...](https://github.com/Squishypone/tgstation/commit/200b739c0a0bbfff95dbfd697786013c92cb6cf6)
#### Monday 2023-05-01 19:29:07 by Kyle Spier-Swenson

Refactors and defuckulates dbcore. Adds support for min_threads rustg setting, Reduce query delay, Make unit tests faster (#74852)

dbcore was very fuckulated.

It had 3 lists of queries, but they all had their own current_run style
list to support mc_tick_check (as it was already being done before with
the undeleted query check, so i can understand why they ~~cargo culted~~
mirrored the behavior) This was silly and confusing and unneeded given
two of those loops can only process at most 25 items at a time on
default config, plus these were cheap operations (ask rustg to start
thread, ask rustg to check on thread).

Because of the confusingness of the 6 lists for 3 query states, The code
to run pending/queued queries immediately during world shutdown was
instead looking at the current_run list for active queries, **meaning
those queries got ran twice.**

The queued query system only checked the current active query count in
fire(), meaning even when there was nothing going on in this subsystem
new queries had to wait for the next fire() to run (10 ticks, so 500ms
on default config)

Those have all been fixed.

the config `BSQL_THREAD_LIMIT` has been renamed to
`POOLING_MAX_SQL_CONNECTIONS` and its default was lowered to match
MAX_CONCURRENT_QUERIES .

added a new config `POOLING_MIN_SQL_CONNECTIONS`, allowing you to
pre-allocate a reserve of sql threads.

The queue processing part of SSdbcore's fire() has been made to not obey
mc_tick_check for clarity and to make the following change easier to do:

If there is less than `MAX_CONCURRENT_QUERIES` in the active queue, new
queries activate immediately.

(its ok that there are two configs that kinda do the same thing,
POOLING_MAX_SQL_CONNECTIONS maps to max-threads in the mysql crate, and
it seems to only be a suggestion, meanwhile MAX_CONCURRENT_QUERIES can't
do anything during init, which is when the highest amount of concurrent
queries tend to happen.)

:cl:
config: database configs have been updated for better control over the
connection pool
server: BSQL_THREAD_LIMIT has been renamed to
POOLING_MAX_SQL_CONNECTIONS, old configs will whine but still work.
fix: fixed rare race condition that could lead to a sql query being ran
twice during world shutdown.
/:cl:

I have not tested this pr.

---
## [Squishypone/tgstation](https://github.com/Squishypone/tgstation)@[773cc9542a...](https://github.com/Squishypone/tgstation/commit/773cc9542a54837fc52b15eb09cc98d7226049fb)
#### Monday 2023-05-01 19:29:07 by MrMelbert

Adds admin alert for revs created through traitor panel (#74862)

## About The Pull Request

So like, using traitor panel to make revs doesn't work. 

Revolutions live and die, currently, by the revolution ruleset datum
dynamic creates. It manages the hostile environment and also processes
to check whether either side should be winning or not.

This means that the revolutionary buttons in the traitor panel are kind
of noob-admin-bait. You press it for a funny revolution and then you
realize it's screwed when all the heads are dead and everyone's
stumbling around cluelessly

This has a proper solution, albeit somewhat difficult - separate out the
revolution from the ruleset, make admin spawned revs create a
revolution. I can do this but it's a lot of effort and this works in the
meanwhile

Pops up a TGUI alert when an admin presses "add revolutionary" in
traitor panel when there is no ongoing revolution. Simply enough, gives
them an alert that it will not work correctly. Lets them decide whether
they want to deal with that. (Because you can manually deal with it via
proc calls, if you've got code smarts.)

## Why It's Good For The Game

Stops admins from stumbling into the same trap without warning.

Can be removed in the future easily when revs are coded better. 

## Changelog

:cl: Melbert
admin: Adds a warning that spawning revs via traitor panel will not
function as expected.
/:cl:

---
## [Squishypone/tgstation](https://github.com/Squishypone/tgstation)@[821123b598...](https://github.com/Squishypone/tgstation/commit/821123b59850bc4d0556b8dd7e0cf169f7fa6bc3)
#### Monday 2023-05-01 19:29:07 by ChungusGamer666

Makes a whole bunch of wooden objects flammable (#74827)

## About The Pull Request

This whole PR started because I realized that baseball bats are not
actually flammable which I found weird, then I looked at a whole bunch
of other stuff that really should be flammable but also isn't.

## Why It's Good For The Game

Makes wooden objects behave slightly more consistently? Honestly, most
of these seem like oversights to me.

## Changelog

:cl:
balance: The following structures are now flammable: Picture frame,
fermenting barrel, drying rack, sandals, painting frames, paintings,
spirit board, notice board, dresser, displaycase chassis, wooden
barricade
balance: The following items are now flammable: Baseball bat, rolling
pin, mortar, coffee condiments display, sandals, wooden hatchet, gohei,
popsicle stick, rifle stock
/:cl:

---
## [Capsandi/tgstation](https://github.com/Capsandi/tgstation)@[c18b1ef442...](https://github.com/Capsandi/tgstation/commit/c18b1ef4423fc7d9083adac9b51aab4f169ea8aa)
#### Monday 2023-05-01 20:50:12 by tralezab

End of Mapping March (Thanks to everyone who contributed, you're amazing!!!) (#74417)

## About The Pull Request

Removes the special mapping template. We got a really good turnout this
year! Will start counting ckeys and all that.

### But my mapping pr isn't done yet!

If it was opened during march, you'll get your token, don't worry

---
## [ArcaneDefence/tgstation](https://github.com/ArcaneDefence/tgstation)@[2e5bfe5be6...](https://github.com/ArcaneDefence/tgstation/commit/2e5bfe5be669d5222b68c7318349c4ac0947722b)
#### Monday 2023-05-01 20:54:52 by LemonInTheDark

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
## [NickBergeron13/ms_thesis](https://github.com/NickBergeron13/ms_thesis)@[9f0814b208...](https://github.com/NickBergeron13/ms_thesis/commit/9f0814b20880fe64fe2145e85b205e0f1c4adf0d)
#### Monday 2023-05-01 21:06:53 by Nick Bergeron

Completed my gitbook. I added 2 new chapters and made some changes to the first chapter. I'm sorry I didn't do more. My parents have been in town to see the baby and I struggled to make time to finish all of my final projects. Thanks for the amazing class!

---
## [newstools/2023-new-york-post](https://github.com/newstools/2023-new-york-post)@[4ed529de3b...](https://github.com/newstools/2023-new-york-post/commit/4ed529de3b329780a3150271872522863fa9f078)
#### Monday 2023-05-01 21:19:58 by Billy Einkamerer

Created Text For URL [nypost.com/2023/05/01/dear-abby-my-girlfriend-cheated-on-me-she-says-i-should-be-more-confident/]

---
## [Hopekz/cmss13](https://github.com/Hopekz/cmss13)@[c4ebe04c7c...](https://github.com/Hopekz/cmss13/commit/c4ebe04c7c9ff01aa928c0c629322d72dec721d9)
#### Monday 2023-05-01 21:23:49 by Julian56

fix the medbay door release button to exit treatment center. (#3173)

# About the pull request
fix the medbay door release button to exit treatment center.
was my mistake sorry
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
fixing bug is good
# Testing Photographs and Procedure
i tested the button ingame 
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:

fix: fix the med-bay door release button to exit treatment center.my
bad.

/:cl:

---------

Co-authored-by: Julien <jverger.ingx@gmail.com>
Co-authored-by: Morrow <darthbane97@gmail.com>

---
## [Dissentbay/Dissents-wild-fork](https://github.com/Dissentbay/Dissents-wild-fork)@[14a2aff333...](https://github.com/Dissentbay/Dissents-wild-fork/commit/14a2aff3335d2cc93ac8f0f4f7da9d6b3d48aaa4)
#### Monday 2023-05-01 22:31:55 by ThePainkiller

Erismed4 patches

- Lowers overdose of Party Drops and Menace
- improves upon certain wound fixing methods
- Surgical "tape" is gone, why would we need that when we always had bone gel for doing the exact same procedure a year ago
- Hyperzine renamed to Chronos. No longer a drug, considered a stim now, effects largely remain the same with no emote spam, but it will consume the user's sanity the more it's on them, causing halucinations and sanity loss. Overdose causes mental breakdown, hallucinations, jitteriness, nerve damage and fatal brain damage.
- Various stim recipes tweaked
- Medical stack items costs shuffled around
- Bone grafting to bone fixing
- Detox given Purger chem quality for treatment on toxin accumulation wounds
- Fixes overdose of Baton and Claw energy drinks to damage their respective organs instead of just the heart
- Combat chem injector has basic combat chems now instead of just hyperzine and free food/meds
- Organ fabricator no longer spills biomatter on the floor when deconstructed, handled as a proper lathe with no bullshit since Biomatter is no longer a "church" material

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[f7a49c4068...](https://github.com/tgstation/tgstation/commit/f7a49c4068f1277e6857baf0892d355f1c055974)
#### Monday 2023-05-01 22:38:03 by Ryll Ryll

Gunpoints now take half a second to activate, make gasp sounds, and briefly immobilize the shooter and target, other small balance changes (#74036)

## About The Pull Request
This PR messes around with gunpoints a bit, with the purpose of making
them more viable in certain scenarios without making them obnoxious. The
biggest change is that gunpoints now require a 0.5 second do_after()
where neither the shooter nor the target moves, and immobilizes both of
them for 0.75 seconds if point blank, or half that if you're 2 tiles
away. Originally you were supposed to only be able to initiate a
gunpoint from point-blank, but #56601 seems to have removed that
requirement, so we'll run with it and just leave it as advantageous to
gunpoint closer up. The do_after() reinforces that it should be used as
an ambush tactic, and so you can't use it on someone who's actively
fleeing or fighting you.

Getting held up will now make you emit a shocked gasp sound, a la Metal
Gear Solid, which combined with the short immobilize will hopefully make
it more noticeable that someone's pointing a gun at you.

Holdups will now immediately give a 25% bonus to damage and wounds,
instead of having to wait 2.5 seconds to hit the double damage stage.

Finally, right clicking someone that you're holding up will no longer
shoot them. That just feels like good consistency.

## Why It's Good For The Game
Hopefully makes gunpoints a little more viable for when you want to
stick someone who's not expecting it up without them immediately jetting
off. In the future I'd like to ape Baycode and let the gunman have an
action that toggles whether the victim is allowed to move, so you can
order them to move to a second location without instantly shooting them,
but that'll come later.
## Changelog
:cl: Ryll/Shaps
balance: Holding someone at gunpoint now requires both the shooter and
the victim to hold still for half a second before activating, so you
can't hold-up people fleeing or fighting you. After that, it will
briefly immobilize the both of you, 0.75 seconds if adjacent, or half
that if you're two tiles away. Nuke ops are immune to the
immobilization, since they're ready to die anyways.
balance: Holding someone up will immediately apply a 1.25x damage and
wound multiplier, rather than waiting 2.5 seconds to hit 2x.
soundadd: Being held up will now make the victim play a sharp gasp
sound, a la Metal Gear Solid.
qol: Trying to hold someone up that you're already holding up will no
longer shoot them.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---

