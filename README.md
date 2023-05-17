## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-05-16](docs/good-messages/2023/2023-05-16.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,103,228 were push events containing 3,481,049 commit messages that amount to 253,274,941 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 69 messages:


## [StollD/linux-fedora](https://github.com/StollD/linux-fedora)@[1bba82fe1a...](https://github.com/StollD/linux-fedora/commit/1bba82fe1afac69c85c1f5ea137c8e73de3c8032)
#### Tuesday 2023-05-16 00:02:44 by Darrick J. Wong

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
## [greenhas/spg_website](https://github.com/greenhas/spg_website)@[502bc76d46...](https://github.com/greenhas/spg_website/commit/502bc76d4659977ecf0591c0283dfb15a465937c)
#### Tuesday 2023-05-16 00:16:57 by Spencer Greenhalgh

post This book took me a while to get into. I gave up on the print version a year or three ago, and even the audiobook wasn't doing great at capturing my attention for a while—I had to rush to finish this before it was due back to Libby. I'm glad that I stuck it out, though, because I liked what I got. I never read the X-Wing novels from the old EU, but I wanted something like what I imagined they were. Alphabet Squadron ended up being the best kind of expanded universe book: Expanding on interesting ideas, filling in details, offering new perspectves, and capturing the original feel of things. This ended up feeling a lot like Andor in adding some grittiness and cynicism to Star Wars, and I was surprised how far Freed went in emphasizing that star war is star hell. I found pew pew pew spaceship fights that I've loved for decades to actually be quite ugly, and I'm glad for that new perspective.

---
## [SoMainline/linux](https://github.com/SoMainline/linux)@[1fb03186df...](https://github.com/SoMainline/linux/commit/1fb03186df0a08b6982aceac399156aa811c3157)
#### Tuesday 2023-05-16 00:19:19 by Douglas Anderson

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[6f237af99f...](https://github.com/treckstar/yolo-octo-hipster/commit/6f237af99f7c62efc710f89674544ac9815c7d6d)
#### Tuesday 2023-05-16 00:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Lypheo/mpv](https://github.com/Lypheo/mpv)@[9a8f08f734...](https://github.com/Lypheo/mpv/commit/9a8f08f7349357792bbc7be98d301b8a5bfb62d2)
#### Tuesday 2023-05-16 00:26:47 by Lypheo

sub: more fixes + move update_subtitles call to playloop

Makes shit a lot more sane I think. Haven’t noticed
any performance or behavior differences but then again
it’s 3 a fucking m and I haven’t produced a single
coherent thought or line of code all day. Hopefully
I’m done with this shit now because it’s all disgusting
mess and I don’t wanna touch it again.

---
## [ajkrupka/Cataclysm-DDA](https://github.com/ajkrupka/Cataclysm-DDA)@[59c577e9f9...](https://github.com/ajkrupka/Cataclysm-DDA/commit/59c577e9f92bd3349312e254fa29d2bfcc84392f)
#### Tuesday 2023-05-16 00:52:41 by Karol1223

A bunch of random item reworks: 3 (#65532)

* boltcutters & chopsticks

* tin snips

* knitting needles

* silly notes

* hairbrush

* flags oh god the flags

* evil commas

* density list removal

---
## [FranklinPenaDev/My-Codewars-soultions](https://github.com/FranklinPenaDev/My-Codewars-soultions)@[917205b812...](https://github.com/FranklinPenaDev/My-Codewars-soultions/commit/917205b812960d89e5253d865fd58ee7cf331613)
#### Tuesday 2023-05-16 01:09:53 by FranklinPenaDev

Create Did she say hallo?

You received a whatsup message from an unknown number. Could it be from that girl/boy with a foreign accent you met yesterday evening?

Write a simple function to check if the string contains the word hallo in different languages.

These are the languages of the possible people you met the night before:

hello - english
ciao - italian
salut - french
hallo - german
hola - spanish
ahoj - czech republic
czesc - polish
Notes

you can assume the input is a string.
to keep this a beginner exercise you don't need to check if the greeting is a subset of word (Hallowen can pass the test)
function should be case insensitive to pass the tests

---
## [llegomark/evals](https://github.com/llegomark/evals)@[170dfd886c...](https://github.com/llegomark/evals/commit/170dfd886c0704588461af075393cc20cfb0480f)
#### Tuesday 2023-05-16 01:25:36 by Robert Bateman

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
## [llegomark/evals](https://github.com/llegomark/evals)@[2ffd4b57de...](https://github.com/llegomark/evals/commit/2ffd4b57deaeced1fde54744da9de62d3eb7738a)
#### Tuesday 2023-05-16 01:25:36 by Andrew Kondrich

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
## [SethLafuente/tgstation](https://github.com/SethLafuente/tgstation)@[dff70625e7...](https://github.com/SethLafuente/tgstation/commit/dff70625e7c29616887619dacc0375ddc84f0708)
#### Tuesday 2023-05-16 02:33:35 by ChungusGamer666

Bible refactor (#75350)

## About The Pull Request

This started as a simple addition where burning a bible would curse you,
but then I realized... Bibles aren't even proper books, thus can't be
burned!
So yeah, since that is not necessary due to how atom_storage works, I
reworked that.

## Why It's Good For The Game

Because burning bibles and getting cursed for it is funny.

![image](https://github.com/tgstation/tgstation/assets/82850673/2a8489ce-ecd6-45ee-9eb9-168ff820af65)

![image](https://github.com/tgstation/tgstation/assets/82850673/ebe98ad6-2d0d-4d20-9ea1-5d472d6ca465)

## Changelog

:cl:
add: You can burn bibles now! But heresy has a steep cost...
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [targed/Open-Assistant](https://github.com/targed/Open-Assistant)@[b9c60ed582...](https://github.com/targed/Open-Assistant/commit/b9c60ed582a8ca0855ab4e213a5e921f3a3fc24c)
#### Tuesday 2023-05-16 02:57:52 by Tobias Pitters

add alpaca gpt4 dataset (#2610)

The inputs can be quite a lot of different versions of `no input`,
therefore don't use the `input` column for that.
In some cases the text in `input` is already in the instruction, in
these cases, we also don't use the `input` column.

I am not quite sure how to concatenate the `instruction` and the `input`
column. In most cases it seems fine to just replace last appearance of
`.`, `!` or `?` with a colon, e.g.:
Instruction: `Identify the odd one out.`
Input: `Twitter, Instagram, Telegram`
or 
Instruction: `How dense is a given material?`
Input: `Steel`

But we also have some questions like:
Instruction: `Given the following synopsis, what is the moral lesson of
this story?`
Input: `Once upon a time, there was a poor young boy who wanted some
candy. He begged his father for money to buy it, but his father said no
and ordered him to go to bed. As he was going to bed, the boy saw a
five-dollar bill on the counter, which he took and bought the candy.`

Where this might not be the best case. Either way, I think the this one
token will not make significant difference the model and therefore I
just concatenate instruction and input with a space.

---
## [pearuhdox/Cartographer](https://github.com/pearuhdox/Cartographer)@[4b0063ec8a...](https://github.com/pearuhdox/Cartographer/commit/4b0063ec8a80cd125b20fc807c58d93ab070d915)
#### Tuesday 2023-05-16 03:14:58 by pearuhdox

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
## [effigy-se/effigy-se](https://github.com/effigy-se/effigy-se)@[527fb7b003...](https://github.com/effigy-se/effigy-se/commit/527fb7b0030d13fc11939d88030b1dc4772742a6)
#### Tuesday 2023-05-16 03:40:22 by DrTuxedo

ELEVATOR MUSIC: True Elevator Experience (#75388)

## About The Pull Request
Adds elevator music into the game that is played by an elevator panel.


https://github.com/tgstation/tgstation/assets/42353186/1a801604-3990-46ae-a96a-b3766b102d62

It's done by using loop sound, with a Kevin MacLeod "Local Forecast -
Elevator" (UNDER CC ATTRIBUTIONS 4.0, and we anyway used some other
Kevin MacLeod music) chopped into 8 small pieces.
The elevator panel has a variable which allows playing music but can be
changed in the map editor if you don't want it to play at certain
places.

(It also doesn't ignore walls, this means you can't hear the music
through wall or when elevator is closed)
## Why It's Good For The Game
Gives elevators more flavour and love, especially when people mostly
prefer stairs to those "laggy crushing machines."
Because of this people might instead hop into an elevator just to hear
meme elevator music, which is relaxing and might create comedic
situations (although elevators don't move that fast)
## Changelog
:cl: DrDiasyl aka DrTuxedo
sound: Nanotrasen have started installing music players in the elevators
to boost workers' morale.
/:cl:

---------

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [zaid2904/E-commerce-site-using-Flexbox](https://github.com/zaid2904/E-commerce-site-using-Flexbox)@[8f68e3a52a...](https://github.com/zaid2904/E-commerce-site-using-Flexbox/commit/8f68e3a52a466058801d94b091b06a640a5efd07)
#### Tuesday 2023-05-16 04:37:04 by Siddiqui Md Zaid

Create README.md

Excited to share my latest achievement! 🎉 Just built an amazing E-commerce site using Flexbox. The flexibility and responsiveness of Flexbox made the design process seamless. Delivering a user-friendly and visually stunning online shopping experience has never been easier. Check it out and let me know what you think!

---
## [ConnorTippets/connortippets.github.io](https://github.com/ConnorTippets/connortippets.github.io)@[578bbc1ff8...](https://github.com/ConnorTippets/connortippets.github.io/commit/578bbc1ff899920ebf46d4cb82d4540727740ddb)
#### Tuesday 2023-05-16 04:37:48 by Con

xenon you suck at javascript

like seriously wtf is with these random ass redelceapiruoleitoid
i'm going insane because of you

---
## [odoo/odoo](https://github.com/odoo/odoo)@[8f6f724174...](https://github.com/odoo/odoo/commit/8f6f724174eaf4fe261576b0657c3875b773519f)
#### Tuesday 2023-05-16 05:30:18 by Xavier Morel

[FIX] core: handle recursion error when resolving stored fields

Issue discovered in the uninstall (and reinstall) of sale_project: a
dump has ~100 tasks, when reinstalling `sale_line_id` has to be
initialised, this is done by marking `sale_line_id` on all extant
tasks as to-recompute, which triggers their computation on the next
`flush`.

Because it's a recursive field, `Field.recompute` ensures only one
record at a time gets recomputed (as there could be cross-dependencies
in the recorset which protection would prevent from resolving).

As the field computation runs, it accesses itself, which triggers a
cache miss, which triggers a `_fetch_field` (to get the currently
stored value), this calls `_read`, which flushes the field we're
trying to read.

The problem here is that for efficiency the cache miss will look for
all records in the cache without a value for the
field (`_in_cache_without`) and try to `fetch` on them as well. This
means rather than not doing anything in flush, we're going to
`Field.recompute` on all records except the one selected the first
time around, which repeats the cycle until there is no more additional
record found in `_in_cache_without`, which could trigger the next
round of `recompute`, and the entire thing unwinds, and we probably
perform a ton of unnecessary additional `compute_value`.

Except that doesn't even happen, because the process from one compute
to the next takes 12~13 stack frames, which given the default
recursion limit of 1000 gives a hard limit of 76 fields before hitting
a RecursionError. As this is less than 100, a recursion error [is what
we get](https://runbot.odoo.com/runbot/build/31726625).

In 15.2, this was fixed by only expanding the fetch on non-recursive
fields, pessimizing recursive
fields (5c2511115b14299516fce4aa3737a62faaf5b653). Test-wise this only
impacted mail performances and in a relatively minor manner.

In 16.0, the mail tests actually match already (so that part was
skipped by the cherrypicking) however this impacts the knowledge perf
tests much more significantly e.g. `test_article_creation_multi_roots`
gets +9 queries when creating 10 top-level articles, which is a bit
much.

So use an alternative which is ugly as hell but which I didn't
consider for 15.2 (may want to backport it one day if the current fix
is an issue): catch the recursion error and use the existing
fallback (of fetching just the requested record's field without
expanding the recordset).

This likely makes for a pretty inefficient situation in the original
case as we're certainly going to hit the recursion limit repeatedly,
but that still fixes the issue, and it avoids deoptimising cases which
fall short of the recursion limit (resolving under 60 records or
so).

Plus despite creating giant stacks we might actually get good
efficiency as we're going to hit recursion limits repeatedly but
that's pure python, once we fall below the limit we can resolve
everything at once with a single SQL query (or something along those
lines).

---
## [shifucun/website](https://github.com/shifucun/website)@[60d93d54cc...](https://github.com/shifucun/website/commit/60d93d54cc21bc04c0f3e1c3435a76e3e74fe808)
#### Tuesday 2023-05-16 05:55:11 by Jehangir Amjad

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
## [Dylan-DPC/rust](https://github.com/Dylan-DPC/rust)@[05e332027e...](https://github.com/Dylan-DPC/rust/commit/05e332027ea0434297dc66f66e157bc2dda3fe8a)
#### Tuesday 2023-05-16 06:17:34 by Dylan DPC

Rollup merge of #111607 - jyn514:clubby-reviews, r=clubby789

Add clubby789 to the bootstrap review rotation

r? ``@clubby789`` - thank you for volunteering!

I have been meaning for a very long time now to write up how to do reviews, but I haven't gotten around to it yet :( here is a short summary:

1. If you're not sure what the changes does or if it's ok, always feel free to ping someone else on the team, especially in the first few weeks. You can use `r? bootstrap` to get triagebot to assign someone else.
2. Bootstrap unfortunately has very few tests. Things that touch CLI or toml parsing should likely have a test in `src/bootstrap/config/tests.rs`; things that touch "core" build logic should have a test in `builder/tests.rs`, anything else kinda just slips in :( see https://github.com/rust-lang/rust/issues/102563 for ideas on how to improve the situation here.
3. "Major" changes should be documented in `src/bootstrap/CHANGELOG.md`. "Major" is up to you, but if it breaks a config option or otherwise is likely to break *someone's* build, it's probably major. If it breaks nearly *everyone*'s build, it should also update `VERSION` in `lib.rs`; this should be very rare. Please also ping me or Mark-Simulacrum for major changes (I might set up a triagebot ping for this so you don't have to remember).
4. Once you've approved the PR, tell bors it's ok - you've been contributing for a while so you know how bors works, but here's a cheatsheet just in case: https://bors.rust-lang.org

Documentation about how to use bootstrap lives at https://rustc-dev-guide.rust-lang.org/building/bootstrapping.html; internal docs live in `src/bootstrap/README.md`. The latter unfortunately is not very complete.

---
## [1j01/textual-paint](https://github.com/1j01/textual-paint)@[f5d97912b6...](https://github.com/1j01/textual-paint/commit/f5d97912b67850e7bd65b59e46f4a82009e36116)
#### Tuesday 2023-05-16 06:48:38 by Isaiah Odhner

Design transparent/opaque options UI ANSI art

This is a first draft (or first 13 versions) of an ANSI art rendition of
MS Paint's transparent/opaque option selector used for the Select and
Text tools.

A somewhat silly smattering of notes:

- Emoji representation: 🛢️🔴🧊 or 🛢️🔴🟩
- More symbols considered (and some used):
  ⛀⛁⛃🛢️⬬
  ▰𝄰ᐟ⸍⸝🧊
  ╭╮🔴⏺◖◗
  ╰╯
- The red circle seems really unreliable so I don't think I can use it.
- Overlapping the red circle/sphere object is hard to represent!
- I managed to get something fairly legible in Ubuntu's terminal,
  not so much in VS Code. VS Code is harder; I might've modified some
  settings, I don't know, but it doesn't handle semigraphics as well,
  at least not on my computer. But...
- At least if you've used MS Paint before, you can recognize the general
  color/shape profile of the icons, if not parse out what the icons are
  meant to represent if you'd never looked closely at them before.
- I'm not sure if v12 or v13 is better. I moved the right border to the
  right a bit by making it Braille, but should the corners extend
  further right then (with two dots), or mirror the left border by using
  a single dot Braille character?

---
## [Momilijaz96/sourcegraph](https://github.com/Momilijaz96/sourcegraph)@[bbfce81a35...](https://github.com/Momilijaz96/sourcegraph/commit/bbfce81a35562d84386862e854ef6b35b555a92a)
#### Tuesday 2023-05-16 06:53:01 by Juliana Peña

web/app: remove hover on navbar items to stop focus from being moved (#51739)

The dropdown menu items in the global navbar (Search and, in App,
Feedback) move focus when you hover over them. This is bizarre, ugly,
and most likely a [WCAG
violation](https://www.w3.org/TR/WCAG21/#focus-order). I spent some time
yesterday and the root cause is that the [Reach menu button we use does
not support hover at all](https://github.com/reach/reach-ui/issues/278)
and we're hacking it by [sending a mousedown event when you hover over
the
button](https://sourcegraph.com/github.com/sourcegraph/sourcegraph/-/blob/client/web/src/nav/NavBar/NavDropdown.tsx?L58).

There are two options I can think of to mitigate this bug:
1. Get rid of hover events and only open the dropdowns on click. This is
the easiest option, but obviously removes the ease of accessing the menu
for mouse users.
2. Rewrite the dropdown nav items to use a custom menu instead of Reach.
This is more expensive because we have to reimplement lots of a11y stuff
here, but we can have more fine-grained control of different UI flows
for mouse hover vs mouse click vs keyboard users.

I went with the first option following @almeidapaulooliveira's
[feedback](https://sourcegraph.slack.com/archives/C0HMGV90V/p1683735888755969?thread_ts=1683734992.157499&cid=C0HMGV90V).

The following changes were applied to `NavDropdown`:

- Removed all hover and touch events; now only a click will open the
menu.
- Removed the split button; now clicking anywhere on the button will
always open the menu.
- Made the mobile home item into a "generic" home item and always
visible when present.
- Made the home item optional (since the Feedback menu item in the
desktop app doesn't have a home item/route).
- Added customizable a11y names; in the past, the only dropdown was the
Search one, but in App we now have Feedback; the a11y labels were still
saying "Search" before this change.

Additionally, the following changes were applied for polish:

- The double-focus ring on the back/forward buttons in the Tauri app has
been fixed
- Styling changes made to simplify code

## Test plan

The global navbar has extensive visual and behavior test coverage.

---
## [yogesh8130/gallery](https://github.com/yogesh8130/gallery)@[49f9f4d527...](https://github.com/yogesh8130/gallery/commit/49f9f4d5279bb2872ffd4eeedd7fa0b0a10dceb0)
#### Tuesday 2023-05-16 07:04:16 by yogesh8130

fixed zoom
- holy shit it is just two lines but damn this took me long, earlier when you zoomed in the point under your mouse was used as reference to zoom around, and this only worked when you were at the top of the page only. As soon as you scroll down the point under the mouse whizzes to top and image seems to be stuck on its bottom edge of the screen. Now no matter where you are vertically in the page, the point under the mouse remains fixed while zooming.

---
## [delanni/kibana](https://github.com/delanni/kibana)@[3b6b7ad9b9...](https://github.com/delanni/kibana/commit/3b6b7ad9b9553be3d039c71edcbdcb2e3d6423fd)
#### Tuesday 2023-05-16 08:05:49 by Pierre Gayvallet

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
## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[2068ea9ab5...](https://github.com/MTandi/tgstation/commit/2068ea9ab53803557b5e48cddbe57205f4c4792e)
#### Tuesday 2023-05-16 08:07:14 by SyncIt21

Crate, Closet Refactors & Access Secured Stuff  (#74754)

## About The Pull Request
This PR is actually 2 parts, one that fixes runtimes with crates & the
other that allows secured closets to be crafted
along with a secured suit storage unit

**Crate Fixes**

Fixes #74708

The problem starts here

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L31-L34
Not only does this if condition look ugly but it's highly error prone
because one single call to `update_appearance()` can cause this to fail,
and sure enough if you look at the parent `Initialize()` proc it calls
just that

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/closets.dm#L81-L88
Since we know the appearance is guaranteed to be changed in some way
before the if condition gets executed let's check what the final state
of the crate would be before this if check

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L54-L56
We see that the final icon state depends on the variable `opened` so if
we want to place/spawn a crate that is opened at round start we have to
ensure that `opened = TRUE` so the `if(icon_state ==
"[initial(icon_state)]open")` succeeds and does its job correctly.
Sadly we did dum shit like this
```
/obj/structure/closet/crate{
	icon_state = "crateopen"
}
```
throughout the entire code base, we thought backwards and were only
concerned in making the closet look open rather than setting its correct
variables to actually say that it is opened. because none of these
crates actually set `opened = TRUE` the final icon state becomes just
"crate" NOT "crateopen" therefore the if condition fails and we add the
component

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L36-L37
with the wrong parameters, so when closing the closet after_close()
removes the component with the wrong arguments

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L81-L84
that is does not unregister the signals and readds the component i.e.
re-registers the signals causing runtime.

The solution just do this
```
/obj/structure/closet/crate/open[mapping helper]
```
To clearly state that you want the closet to be open, that way you don't
have to memorize the icon_state for each different type of crate, it's
consistent across all crates & you don't get runtimes.

And that's exactly what i did everywhere

Another issue that is fixed is "Houdini crates" i.e. crates which are
open & appear empty but when you close & reopen them magical loot
appears, Go ahead walk upto to cargo and find any empty crate that is
open and do this

Fixes #69779


https://user-images.githubusercontent.com/110812394/232234489-0193acde-22c8-4c19-af89-e897f3c23d53.mp4

You will be surprised, This is seriously harmful to players because they
can just walk by a crate that appears to be open & empty only to realize
later that it had some awesome loot. Just mean

The reason this happens is because of the Late Initialization inside
closets

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/closets.dm#L85-L86

What late initialization does is suck up all stuff on its turf

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/closets.dm#L97-L100

In theory this is supposed to work perfectly, if the closet is closed
move everything on the turf into the closet and so when the player opens
it, they all pop back out.
But what happens if the closet is opened before ` LateInitialize()` is
called? This breaking behaviour is caused by object spawners

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/effects/spawners/random/structure.dm#L94-L100
And maint crates

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L141-L143
These 2 spawners open up the crate based on random probability before `
LateInitialize()` is called on the crate and so what happens is the
crate is first opened and then stuff on the turf is sucked in causing an
open but empty crate to appear.

The solution is simple just check again in ` LateInitialize()` if our
crate is still closed before we proceed.That's fixed now too

**Code Refactors**
1. Introduced 2 new signals COMSIG_CLOSET_PRE/POST CLOSE which are the
counter parts for the open signals. hook into them if you ever need to
do stuff before & after closing the closet while return BLOCK_CLOSE for
COMSIG_CLOSET_PRE_CLOSE if you want to block closing the closet for some
reason
2. 2 new procs `before_open()` & `before_close()` which are the counter
parts for `after_open()` & `after_close()`. If you need to write checks
and do actions before opening the closet or before closing the closet
override these procs & not the `open()` & `close()` procs directly

**Secured Craftables** 
This is just a reopened version of #74115 after i accidently merged
another branch without resolving the conflicts first so i'll just
repaste everything here, since crates & closets are related might as
well do all in one

1. **Access secured closets**
   
   - **What about them?**
          **1. Existing System**
If you wanted to create a access secured closet with the existing system
its an 4 step process
            - First construct a normal closet
            - Weld it shut so you can install the airlock electronics
            - Install the electronics [4 seconds]
            - Unweld
This is a 4 step process which takes time & requires a welding tool
         **2. New system**
Combine the 4 steps into 1 by crafting the secure closet directly
                    
![Screenshot
(184)](https://user-images.githubusercontent.com/110812394/235904926-c2ea231c-eba7-45d0-a5af-e0456fdd40bc.png)

    - **Bonus Features**
              **1. Card reader**
The card reader acts as an interface between the airlock electronics &
the player. Usually if you want to change access on a locker you have to
                  - Weld the closet shut
                  - Screw driver out the electronics
                  - Change the settings
                  - Install it back
                  - Unweld
With a card reader there is no need of a welder & screwdriver. You can
change the access of the locker while its operational

        **How do i install the card reader?**
             1. Weld the closet shut
             3. Insert card reader with hand
4. To remove the card reader use crowbar or just deconstruct the whole
closet with a welding tool
             5. Unweld closet

         **How to change its access?**
This will overwrite the settings on your airlock electronics. To do this
1. make sure the closet is first unlocked. This is important so that no
random person who doesn't have access to the closet can change its
access while its locked. It would be like giving the privilege of
changing your current password without first confirming if you know the
old password
2. attack/swipe the closet with your PDA. Make sure your ID card is
inside the PDA for this to work. You can also just use your ID card
directly without a PDA
         3. You will get 3 options to decide the new access levels
           
![Screenshot
(174)](https://user-images.githubusercontent.com/110812394/233454364-d99a2fb6-9f26-4db3-9fac-a10689955484.png)


        They work as follows
- **Personal**: As the name implies only you can access this locker and
no one else. Make sure to have your ID on you at all times cause if you
loose it then no one can open it
- **Departmental**: This copies the access levels of your ID and will
allow people having those exact same access levels. Say you want to
create a closet accessible to only miners. Then have an miner choose
this option and now only miners can open this closet. If the Hop sets
custom access on your ID then only people with those specific access
levels can open this closet
         - **None**: No access, free for all just like a normal closet

**Security:** After you have set the access level it is important to
lock the access panel with a "multi-tool", so no one else can change it.
Unlock the panel again with the "multi-tool" to set the new access type

       **2. Give your own name & description**
To rename the closet or change its description you must first make the
closet access type as personel i.e. make it yours, then use an pen to
complete the job. You cannot change names of departmental or no access
closets because that's vandelism

       **3. Custom Paint Job**
    Use airlock painter. Not intuitive but does the job. 
   
![Screenshot
(181)](https://user-images.githubusercontent.com/110812394/234202905-00946b88-2513-489d-b0a2-d618a72f3e49.png)

      **4. Personal closets**
Round start personal closets can have their access overridden by a new
ID when in it's unlocked state. This is useful if the last person has no
use for the closet & someone else wants to use it.


    - **Why its good for the game?**      
1. Having your own personal closet with your own name & description
gives you more privacy & security for your belongings so people don't
steal your stuff. Personal access is more secure because it requires you
to have the physical ID card you used to set this access and not an ID
which has the same access levels as your previous ID
2. Make secure closets faster without an welding tool & screw driver
3. Bug fix where electronics could be screwed out from round start
secured closets countless times spawning a new airlock electronic each
time
      
2. **Access secured freezers**

    - **What about them?**
The craftable freezer from #73942 has been modified to support secure
access. These can be deconstructed with welders just as before

![Screenshot
(185)](https://user-images.githubusercontent.com/110812394/235905000-ba165feb-4384-4759-b46b-dba77c9e6ba3.png)


    - **How does it work?**
The access stuff works exactly the same as secure closets described
above. You can rename & change description with pen just like the above
described secure closets. No paint job for this. Install card reader
with the same steps described above.

    - **Why it's good for the game?**
1. Make access secured freezers faster without a welder and screwdriver
2. Your own personally named & locked freezer for storing dead bodies is
always a good thing

4. **Access secured suit storage unit**
   - **What about them?**
Suit storage units now require airlock electronics for construction. The
access levels you set on it will be used to decide
       1. If a player can unlock the unit
       2. If the player can open the unit after unlocking
       3. If the player can disinfect whatever is inside
       
      By default all round start suit storage units have free access

   - **Install card reader**
Provides the same functionality as secured closets described above. To
install it
     1. Open its panel with a screw driver
     2. Add a card reader to it with hand
     3. Close the panel
     
     When you deconstruct the machine the card reader pops back out

   - **Why it's good for the game?**
1. Having your own access protected and named suit storage unit so
random people don't steal your mod suits? Who wouldn't want that.?
Provides security for department storage units.
2. If you have the unit locked then you cannot deconstruct the machine
with a crowbar providing additional security
3. Fixes #70552 , random people can't open/unlock the suit storage unit
without access. You can set personal access to make sure only you can
access the unit

## Changelog
:cl:
add: Access secured closets. Personal closets can have their access
overwritten by an new id in it's unlocked state
add: Access secured freezers.
add: Access secured suit storage units.
fix: Suit storage unit not having access restrictions.
fix: airlock electronics not properly getting removed after screwing
them out from round start lockers
fix: round spawned open crates run timing when closed
fix: open crates hiding stuff in plain sight
fix: open closets/crates sucking up contents during late initialize
causing them appear empty & open
/:cl:

---------

Co-authored-by: Tim <timothymtorres@gmail.com>

---
## [FieryTech/Skyrat-tg](https://github.com/FieryTech/Skyrat-tg)@[c2d75696c8...](https://github.com/FieryTech/Skyrat-tg/commit/c2d75696c8d0012027bf97a15b2c0e332416b497)
#### Tuesday 2023-05-16 08:23:13 by SkyratBot

[MIRROR] Nerfs the firing speed of Syndicate/Russian mobs [MDB IGNORE] (#21047)

* Nerfs the firing speed of Syndicate/Russian mobs (#75247)

## About The Pull Request

Nerfs their firing speed from once every 0.2 seconds to once every 2.5
seconds

## Why It's Good For The Game

1. The mob that is NOT a 'burst' type mob, is firing every 0.2 seconds.
Kinda defeats the point of having them as two separate mobs, so this
aims to fix that.
2. Russian mobs. Turns out that letting them fire their strong-ass gun
every 0.2 seconds was kinda not a good idea. I had assumed making them a
Syndicate mob would be safe, and it technically is, it's just that
Syndicate mob is fucked itself.

## Changelog

:cl:
balance: Default Syndicate and Russian gunners now fire every 2.5
seconds instead of every 0.2
/:cl:

* Nerfs the firing speed of Syndicate/Russian mobs

---------

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>

---
## [Latropos/react-native-reanimated](https://github.com/Latropos/react-native-reanimated)@[0e96f1cd6e...](https://github.com/Latropos/react-native-reanimated/commit/0e96f1cd6e0f6bae6a57aad6f5bd5208d5ae0d19)
#### Tuesday 2023-05-16 09:28:54 by Tomasz Żelawski

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
## [Pickle-Coding/tgstation](https://github.com/Pickle-Coding/tgstation)@[bd4392ab74...](https://github.com/Pickle-Coding/tgstation/commit/bd4392ab7463c383c7e2824f8a9b7d154ad7940c)
#### Tuesday 2023-05-16 10:20:31 by Bloop

New inhand icons for light tubes, makes latex balloons craftable, and various other fixes/improvements (#74576)

## About The Pull Request

This ended up turning into a bit of a junk drawer of a PR I'll admit,
but there's really not a whole lot to it.

There are three parts:

### Part I - Inhand sprites for light tubes.

Adds inhand sprites for light tubes. No more cardboard tube placeholder.
This is self explanatory-they have unique sprites for all 3 states
(normal, broken, and burnt out). The broken version has sharpness now.

Also refactored light_items.dm a bit, it was using a bespoke proc called
`update` to do icon updates. Now it has been _updated_ to use
`update_appearance` instead.


![dreamseeker_6WC8vJMiBW](https://user-images.githubusercontent.com/13398309/230615134-31c51e94-cee5-4eef-ba63-c348a3b2debc.gif)

### Part II - Latex Balloons

Latex balloons, a very old piece of code that was full of typos, has had
some life breathed back into it. It is a fun little item, and I saw no
reason to let it rot. It can now be crafted using a latex glove and some
cable. Also, you can pop them using anything sharp... such as a broken
light tube! Aha!

We've come full circle.


![image](https://user-images.githubusercontent.com/13398309/230617764-3a304fd2-05d0-4b2f-b420-056a93c0dce3.png)

### Part III - update_inhand_icon proc

A new atom helper function, `/atom/proc/update_inhand_icon(mob/target =
loc)`

I was struggling to find an existing proc that could update inhand icons
of a mob that was holding any given atom, without necessarily having a
ref to the mob yet.

So I ended up writing one that did that, and finding the spots in the
code which were using a similar way of doing it (that is in fact how I
stumbled upon the latex balloon item).

...........But then Iearned of the
`/datum/element/update_icon_updates_onmob` component and ended up using
that instead. There are still some very niche cases where you might not
be able to use the component where the proc would come in handy however
e.g. in transforming.dm--and if anything, I think it could serve as a
good spot to leave a comment informing would be users of
`update_icon_updates_on_mob` as an alternative.

For that reason especially I thought it worth keeping. 

## Why It's Good For The Game

New inhand sprites, and a fun little craftable balloon. What's not to
like?

## Changelog

:cl:
add: latex balloons can now be crafted using a latex glove and some
cable. You can fill them with air using a tank. They also have a new
sound effect.
imageadd: light tubes have a new inhand sprite
fix: broken light tubes now actually have sharpness to them as they are
basically spikes of glass.
refactor: refactored latex balloon code
/:cl:

---
## [YKonovalov/tf-kolla-ansible](https://github.com/YKonovalov/tf-kolla-ansible)@[2e5e1b5545...](https://github.com/YKonovalov/tf-kolla-ansible/commit/2e5e1b5545a396b216ab5de3441a964b841c8a17)
#### Tuesday 2023-05-16 10:26:44 by Radosław Piliszek

[CI] Nullify attempts

Per Clark Boylan's feedback [1], retries cause a retry not only
for pre playbook failures but also for cases where Ansible detects
network connectivity issues and they are caused by disks getting
filled to their fullest. This is an issue we experience that
sometimes results in a POST_FAILURE but certain FAILUREs are
retried which wastes CI resources.
The problematic jobs are ceph jobs. They are to be looked into.
Backport to all branches.
We can adjust retries for the core jobs that do not exhibit the
nasty behaviour but first we can try running without retries
to measure the troublesomeness.

[1] https://review.opendev.org/c/openstack/kolla-ansible/+/843536

Change-Id: I32fc296083b4881e8f457f4235a32f94ed819d9f
(cherry picked from commit 153956e458157e44d73efc3dd369699ff20e4d12)

---
## [CCSC-Robotics-club/FtcRobotCode-2023](https://github.com/CCSC-Robotics-club/FtcRobotCode-2023)@[bfa4ee7d5c...](https://github.com/CCSC-Robotics-club/FtcRobotCode-2023/commit/bfa4ee7d5c27e255baaed7dec254fdcf2d14444c)
#### Tuesday 2023-05-16 10:31:00 by szjstar

completed RAS program, not tested yet

fixed the stupid bug from chagpt on the rotation difference calculation, that AI is a fucking stupid son of a idiot

---
## [enso-org/enso](https://github.com/enso-org/enso)@[4b7afbfd36...](https://github.com/enso-org/enso/commit/4b7afbfd3619c22b6b31f2840fa807f0af41fb57)
#### Tuesday 2023-05-16 10:43:24 by Ilya Bogdanov

Fix blank input port (#6614)

Fixes #6485

Conflicting requirements for the widget tree caused the issue:
1. The span tree node had a connection, and the text of the `number1` label was changed to white (as per the `Connected` color state)
2. The node configuration did not consider it a valid port because the span tree kind was `Operation`, which is not a port usually. So the port shape was not displayed, making the label blend with the node background.

I fixed the issue by considering the existence of the current connection for `Operation` nodes. Remember that it does not turn the node into a port, so after removing the connection, it's not possible to connect it back. That makes sense, in my opinion, as the resulting AST is invalid anyway. But at least we can see the label on the invalid node.


https://github.com/enso-org/enso/assets/6566674/23934966-8f72-4675-abe3-78a3f0c0cda4

---
## [fourlastor-forks/libgdx](https://github.com/fourlastor-forks/libgdx)@[e1d1fdc5fb...](https://github.com/fourlastor-forks/libgdx/commit/e1d1fdc5fb5b8409dc74f638c633ead405e535f3)
#### Tuesday 2023-05-16 11:49:29 by Tommy Ettinger

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
## [thco-odoo/poem](https://github.com/thco-odoo/poem)@[ffbfd335ef...](https://github.com/thco-odoo/poem/commit/ffbfd335ef794504282dd45dbe05ae29a1b44c21)
#### Tuesday 2023-05-16 11:57:50 by Corentin Thaon (thco)

[IMP] zen: verse about code ambiguity

Computers have made humans superstitious: To exorcise the demons in our
computers we perform the sacred ritual of turning them off and then on.
Supposedly this will fix any mysterious problem. However, computers are
not magic. If your code isn’t working, there is a reason and only
careful, critical thinking will solve it. Refuse the temptation to
blindly try solutions until something seems to work; often you have
merely masked the problem rather than solved it.

---
## [harryob/cmss13](https://github.com/harryob/cmss13)@[d728da3e02...](https://github.com/harryob/cmss13/commit/d728da3e02664297050d82dc01c87414c61345ef)
#### Tuesday 2023-05-16 12:18:54 by Puckaboo2

Healer Balance Changes (#2896)

# About the pull request
This pull request addresses the boring and low-risk gameplay of the
Healer drone, who spends half the round sitting next to recovery nodes
and recovering her health so she may use it again, rinse and repeat
until a rine notices said drone has purple on it and booms her.

First, by changing her health from 600 to 500, Healer can spend more
time healing her sisters than sitting through another 100 health to heal
herself. Though this makes her less tanky than before, healing classes
are not known to be tanks. To ensure Healer can still heal five times
without depleting too much of her health whilst still giving her sisters
a decent amount of heals, I made her ability cost 75 health instead of
100, and also made her ability cost 200 plasma. Since Healer replenishes
plasma much more quickly than her health, she can still put herself into
crit if she heals too frequently. Due to this buff, her heals had a
slight nerf, being 10 damage a second for ten seconds instead of 12
damage per second for ten seconds for a total of 20 less damage healed
per application overall.

In addition to these changes, I'm giving Healer a better plasma transfer
for when she has nobody else to heal/nowhere else to weed and she has an
opportunity to assist her sisters. While a normal drone transfers 50
plasma with a delay of 20, Healer transfers 100 with a delay of 15,
which is nowhere near Hivelord's gargantuan 200 plasma with a delay of
5, but it still is better than a normal drone.

Finally, to give the huggers and larva some love, Healer will
specifically heal little ones 1.5 health per second for 10 seconds for
15 of her own health and 30 plasma.

# Explain why it's good for the game
Healer drone isn't fun. You run around and heal a bunch of T3s, then sit
out for half the battle trying to heal that massive 600 heath while you
wonder why you take so long to heal even though you have Strong
pheromones. You cry to mom for help, but she doesn't have time to heal a
drone who can't build walls and has no need to weed at the moment. You
think, 'screw it, I'm going to make a recovery node and camp here until
I heal', but by the time you finish healing, several T3s and a silly
rouny just suicided into a wall of talls and destroyed your recovery
node, so you run off and make another one. But oh, someone noticed you
have purple on your carapace and decide your location is precisely where
a shell should land, right as you're building one.

No more. These changes allow Healer to move around at her leisure and
makes Healer more engaging by allowing her to be a more front-line
participant and actively run around and heal her sisters without having
to incur such a harsh penalty.

Let this be a testmerge, please.

# Changelog

:cl: Puckaboo2
balance: Healer Drone's health was reduced to 500 from 600.
balance: Healer's damage has been increased to 17 from 12 and the tackle
damage debuff has been halved.
balance: Healer Drone's Apply Salve ability now costs 75 health and 200
plasma, down from 120 health and up from 0 plasma.
balance: Healer Drone's Apply Salve ability now heals 10 damage per
second for 10 seconds, down from 12 damage per second for ten seconds.
balance: To prevent spam healing between Healers, Apply Salve costs 100
health instead of 75 health when Healer heals another Healer. Much
healing.
balance: Healer has an improved Transfer Plasma that gives 100 plasma
instead of 50, with a 25% shorter delay.
balance: Healer will heal huggers and larva for 1.5 health a second for
10 seconds, costing 15 health and 30 plasma.
tweak: Healer will now face the xeno she is healing if she was not
facing their direction before.
spellcheck: All instances of VERYSMALL and VERYLARGE have been renamed
to VERY_SMALL and VERY_LARGE.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: Morrow <darthbane97@gmail.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[d5cd050ec2...](https://github.com/treckstar/yolo-octo-hipster/commit/d5cd050ec26d1c57082ed53e8ad9284f6d19f68f)
#### Tuesday 2023-05-16 12:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [b4n/fishman-ctags](https://github.com/b4n/fishman-ctags)@[0c2e334c74...](https://github.com/b4n/fishman-ctags/commit/0c2e334c743f906daafa1ddde24a4545b99816c8)
#### Tuesday 2023-05-16 12:25:39 by Colomban Wendling

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
## [brauner/linux](https://github.com/brauner/linux)@[bde509d529...](https://github.com/brauner/linux/commit/bde509d5292cc3f3cc8f27b42c1ff1f7cc5e6415)
#### Tuesday 2023-05-16 13:16:23 by Vladimir Sementsov-Ogievskiy

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
ddc733f452e0 ("[PATCH] Linux-0.97 (August 1, 1992)") 30 years.
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
uapi side while the kernel does in fact allow files without permissions.

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
access symlinks

Back when ddc733f452e0 ("[PATCH] Linux-0.97 (August 1, 1992)") added
coredump handling open_namei() took the FMODE_{READ,WRITE} flags as an
argument. So the coredump handling introduced in
ddc733f452e0 ("[PATCH] Linux-0.97 (August 1, 1992)") was buggy because
O_WRONLY shouldn't have been passed. Since O_WRONLY is 1 but
open_namei() took FMODE_* flags it was passed FMODE_READ by accident.

So 9cb9f18b5d26 ("[PATCH] Linux-0.99.10 (June 7, 1993)") was a bugfix
for this and the 2 didn't really mean O_RDWR, it meant FMODE_WRITE which
was correct.

The clue is that FMODE_{READ,WRITE} didn't exist yet and thus a raw "2"
value was passed.

Fast forward 5 years around 2.2.4pre4 (February 16, 1999) this code was
changed to:

    -       dentry = open_namei(corefile,O_CREAT | 2 | O_TRUNC | O_NOFOLLOW, 0600);
    ...
    +       file = filp_open(corefile,O_CREAT | 2 | O_TRUNC | O_NOFOLLOW, 0600);

at this point the raw "2" should have become O_WRONLY again as
filp_open() didn't take FMODE_{READ,WRITE} but O_{RDONLY,WRONLY,RDWR}.

Another 17 years later, the code was changed again cementing the mistake
and making it almost impossible to detect when commit
378c6520e7d2 ("fs/coredump: prevent fsuid=0 dumps into user-controlled directories")
replaced the raw "2" with O_RDWR.

And now, here we are with this patch that send us on a quest to answer
the big questions in life such as "Why are coredump files opened with
O_RDWR?" and "Is it safe to just use O_WRONLY?".

So with this commit we're reintroducing O_WRONLY again and bringing this
code back to its original state when it was first introduced in commit
ddc733f452e0 ("[PATCH] Linux-0.97 (August 1, 1992)") 30 years ago.

Signed-off-by: Vladimir Sementsov-Ogievskiy <vsementsov@yandex-team.ru>
Message-Id: <20230420120409.602576-1-vsementsov@yandex-team.ru>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Christian Brauner <brauner@kernel.org>

---
## [panzerr1944/coyote-bayou](https://github.com/panzerr1944/coyote-bayou)@[856955c45a...](https://github.com/panzerr1944/coyote-bayou/commit/856955c45acda58a4ebab15a67ce4d6e96280e4a)
#### Tuesday 2023-05-16 13:29:18 by Tk420634

Redlick & Garland City Take 2

Fuck you to, strong dmm

---
## [eurekadevelopment/Eureka-Kernel-Exynos7885-Q-R-S](https://github.com/eurekadevelopment/Eureka-Kernel-Exynos7885-Q-R-S)@[61317e0327...](https://github.com/eurekadevelopment/Eureka-Kernel-Exynos7885-Q-R-S/commit/61317e0327ea28599f9281eeb4b24dc8f6d7e174)
#### Tuesday 2023-05-16 13:47:42 by Dave Chiluk

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

---
## [agam778/kernel_xiaomi_sm8250](https://github.com/agam778/kernel_xiaomi_sm8250)@[f3fef97d4f...](https://github.com/agam778/kernel_xiaomi_sm8250/commit/f3fef97d4f427e60e902efff18ae288903b1ccec)
#### Tuesday 2023-05-16 14:27:43 by Agampreet Singh

 touchscreen: focaltech_spi: Rename gesture macros

- Fuck you xiaomi.
- Also don't register KEY_GESTURE_U anymore.

Co-authored-by: Agampreet Singh <68941022+agam778@users.noreply.github.com>

---
## [Zevotech/Shiptest](https://github.com/Zevotech/Shiptest)@[725233b42b...](https://github.com/Zevotech/Shiptest/commit/725233b42b6f56551798a0a75b5362e577042de3)
#### Tuesday 2023-05-16 15:25:32 by thgvr

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
## [Zevotech/Shiptest](https://github.com/Zevotech/Shiptest)@[1c039c0623...](https://github.com/Zevotech/Shiptest/commit/1c039c0623b6e8af463de0f0b1ca1ccc49050d94)
#### Tuesday 2023-05-16 15:25:32 by Sun-Soaked

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
## [kartiksahu82/Diwali-Sales-Analysis-Python](https://github.com/kartiksahu82/Diwali-Sales-Analysis-Python)@[3399473a92...](https://github.com/kartiksahu82/Diwali-Sales-Analysis-Python/commit/3399473a920956d13d8de5c718fd6ab8dca1a3c8)
#### Tuesday 2023-05-16 15:28:14 by kartiksahu82

Add files via upload

🚀 Welcome to my Sales Analysis with Python GitHub repository! 📊

Hello everyone,

In this project, I've developed a powerful Sales Analysis code using Python and popular libraries such as Pandas, NumPy, Seaborn, and Matplotlib. This project wouldn't have been possible without the generous contribution of Rishabh Mishra, who provided both the dataset and the project itself. Be sure to follow him for more amazing content!

Throughout this journey, I've gained valuable insights and knowledge, which I'm excited to share with you:

1️⃣ I've mastered the art of data cleaning and manipulation, ensuring the dataset was in optimal shape for analysis.

2️⃣ Conducting exploratory data analysis (EDA) has become second nature to me, thanks to my extensive use of Pandas, Matplotlib, and Seaborn. I've utilized these libraries to uncover hidden patterns and trends, and visualize the data in compelling ways.

3️⃣ By leveraging the power of Python, I've successfully enhanced the customer experience by identifying potential customers across different states, occupations, genders, and age groups. This information can significantly contribute to targeted marketing strategies and personalized campaigns.

4️⃣ I've significantly boosted sales performance by identifying the most popular product categories and individual products. This vital information can aid businesses in effective inventory planning, ensuring they meet customer demands and maximize profits.

All the coding magic was conjured within Jupyter Notebooks, providing a seamless and interactive experience.

I would be immensely grateful for any feedback or suggestions you might have. Let's continue to learn and grow together! Thank you for visiting and happy analyzing! 📈✨

---
## [OpenDDS/OpenDDS](https://github.com/OpenDDS/OpenDDS)@[8029f5acbc...](https://github.com/OpenDDS/OpenDDS/commit/8029f5acbcf34349f860474d8a1fc67524fa4fa1)
#### Tuesday 2023-05-16 16:21:01 by Fred Hornsey

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
## [DestinedCodes/Obsidian-Notes](https://github.com/DestinedCodes/Obsidian-Notes)@[578543670c...](https://github.com/DestinedCodes/Obsidian-Notes/commit/578543670c405dd57a644acf4d3e22ff10dfa246)
#### Tuesday 2023-05-16 16:45:17 by Destiny Saturday

Updates Note: 16/05/2023 17:45

Affected files:
.obsidian/appearance.json
.obsidian/core-plugins-migration.json
.obsidian/core-plugins.json
.obsidian/graph.json
.obsidian/workspace-mobile.json
.obsidian/workspace.json
00. Daily Notes/2023/May/02-05-2023, Tuesday.md
00. Daily Notes/2023/May/03-05-2023, Wednesday.md
00. Daily Notes/2023/May/04-05-2023, Thursday.md
00. Daily Notes/2023/May/08-05-2023, Monday.md
00. Daily Notes/2023/May/14-05-2023, Sunday.md
01. Templates/Daily Note Template.md
01. Templates/Message Template.md
02. Attachments/Pasted image 20230504154156.png
02. Attachments/Screenshot from 2023-05-02 16-50-32.png
Cloud Computing/2. AWS Cloud Concepts/1. Introduction to Cloud Computing.md
Cloud Computing/2. AWS Cloud Concepts/2. Cloud Concepts.md
Introduction to Machine Learing/What is Machine Learning.md
Messages/Believers' Praiseworthy Pursuit after God's Glorious Visitation.md
Messages/Living in the Fullness of Christ by Faith.md
Sermons/The Authoritative Revelation of the Saving Gospel.md
Untitled.md

---
## [KingDragoness/ProjectHypatios](https://github.com/KingDragoness/ProjectHypatios)@[4e05bac99b...](https://github.com/KingDragoness/ProjectHypatios/commit/4e05bac99bbb1fae6a2e0214dca734b4d403959e)
#### Tuesday 2023-05-16 16:52:39 by KingDragoness

Hypatios 1.5.1b5 (quality of life improvements, additional weapons and enemies)
DONE (May 16)
• TV effect UI setting option
o Chromatic abbretion, vignette and lens distortion in UI post effects
• Workbench now has UI post effect
• Eastria spaceguard seriously need combat overhaul, they all look fucking stupid
o Weapon replaced with Herstagen
• DamageReceiverTriggerEnter
o Check KatanaDamage script
o Perfect solution for Theratios trapped inside Force field dialogue.
 Theratios: “Damnit! You’ll pay for that!”
• Mercenary enemy more polish
o Need more sound effect (breathing)
o Firing mode has charging laser effect similar to spider
o Particle effect firing
• Workbench attachment and requirement material icons
o Receiver, Frame, Magazine, Grip, Tank
• Soul bonus perk level 3,4,5 are nerfed.
• New weapon: Herstagen [Exotic]
o An energy-based laser rifle, inspired by Starfield’s Equinox weapon. 20 ammo capacity.
o Can be scoped.
o Recycled rifle animation
• Weapon vault for Katakis weapon
• New weapon: Katakis [Exotic]
o Affected by melee damage bonus
o Unlocked from Zombie level. Green style weapon, short range but deal high damage and fast cooldown, dealing high DPS.
o Melee attacking will not use any ammo but cannot attack if ammo reached 0, it needs to be recharged for 5 seconds.
o Claw particle effect.
o 12 ammo capacity
o Two attacks:
 Porkos Blast: Short-range blast attack that deals 114 damage uses 18 ammos
 Melee: Fast DPS melee attack
•  “CooldownTimeTrigger.cs” modular script
o UnityEvent on trigger
o ExecuteTime(float cooldown = 0.3f)
• Force Shielder now knockback resistance
• New enemy: Healing Bot
o Flying enemy that can repair any mechanical robots in range
o Looping flying sound
o Healing effect particle effect (affected by size)
o Mechanical, unhackable
• Mobius Explorer corpse
• Explosion damage controller (sets explosion’s damage)
o Assign enemy origin
o Set damage
• New enemy: Mercenary Bot
o Deal explosive damage (similar to Decabot)
o Animations (only two states):
 Walk/Moving
 Fire (stop moving)
 Melee attack (when near)
o Mechanical, can be hacked
• Additional mech enemies:
o Easy mech building: https://www.youtube.com/watch?v=2xIpYAaAPCc&ab_channel=CriticalGiants
o Blender object carver plugin
o Merc Grenadier mech
o See in youtube “mech substance painter” or “mech 3ds max”

---
## [Dayana-World/CustomerMoghimiHome](https://github.com/Dayana-World/CustomerMoghimiHome)@[4976e892e8...](https://github.com/Dayana-World/CustomerMoghimiHome/commit/4976e892e884fccadd8fe2dabff84d00571f5264)
#### Tuesday 2023-05-16 17:14:20 by Bamdad Tabari

Merge pull request #102 from BamdadTabari/FuckYou

Fuck you

---
## [iakoster/pyiak_instr](https://github.com/iakoster/pyiak_instr)@[347b898261...](https://github.com/iakoster/pyiak_instr/commit/347b898261cc1a5506e4f6ce7be1f6d9b3f78778)
#### Tuesday 2023-05-16 17:26:04 by Ivan Kosternoi

chore: i'm fucking sick of trying to figure out the architecture of this shit to make it work properly

---
## [NN-Guillaume/Air_level](https://github.com/NN-Guillaume/Air_level)@[23f5f710bb...](https://github.com/NN-Guillaume/Air_level/commit/23f5f710bbc004f7fba76ceebfe16299edb928cc)
#### Tuesday 2023-05-16 17:31:48 by NN-Guillaume

useless fucking tests ! how the hell work this shit ? !

---
## [AiDriveOne/aiDrive_GPT](https://github.com/AiDriveOne/aiDrive_GPT)@[ab5f7b2a89...](https://github.com/AiDriveOne/aiDrive_GPT/commit/ab5f7b2a89bcf60e8e93adfb2c70688c6d6ffd44)
#### Tuesday 2023-05-16 18:13:58 by oscar-king

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
## [AiDriveOne/aiDrive_GPT](https://github.com/AiDriveOne/aiDrive_GPT)@[b170a21cf3...](https://github.com/AiDriveOne/aiDrive_GPT/commit/b170a21cf32c47d841f64ec110cfd6796ec3f89a)
#### Tuesday 2023-05-16 18:13:58 by Sam Ennis

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
## [AiDriveOne/aiDrive_GPT](https://github.com/AiDriveOne/aiDrive_GPT)@[b5da073c21...](https://github.com/AiDriveOne/aiDrive_GPT/commit/b5da073c215c6453b99269a6dab2dca5454f04dd)
#### Tuesday 2023-05-16 18:13:58 by somerandomguyontheweb

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
## [ARF-SS13/coyote-bayou](https://github.com/ARF-SS13/coyote-bayou)@[6fd64b92ca...](https://github.com/ARF-SS13/coyote-bayou/commit/6fd64b92ca4cc80357d8d78c8efc1c6d8196204f)
#### Tuesday 2023-05-16 18:35:43 by Tk420634

Updating the Mansion a bit

Preparing my brain for making a non euclidian dungeon, because I fucking hate everything.

---
## [RaShCat/FF-STG](https://github.com/RaShCat/FF-STG)@[16e4f3c492...](https://github.com/RaShCat/FF-STG/commit/16e4f3c492cd18e74c975051c4fcd9da5e59fb80)
#### Tuesday 2023-05-16 18:35:58 by SkyratBot

Tcomms Soundloop Comes From One Source And Is Less Awful [MDB IGNORE] (#20713)

* Tcomms Soundloop Comes From One Source And Is Less Awful (#74908)

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

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* Tcomms Soundloop Comes From One Source And Is Less Awful

---------

Co-authored-by: Cheshify <73589390+Cheshify@users.noreply.github.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>
Signed-off-by: Vladimir Veisman <v.veisman@flashie.me>

---
## [RaShCat/FF-STG](https://github.com/RaShCat/FF-STG)@[178b6fc96c...](https://github.com/RaShCat/FF-STG/commit/178b6fc96cef11619565d802750cad9e6c34b12a)
#### Tuesday 2023-05-16 18:35:58 by SkyratBot

Turns Deer into Basic Mob - They Freeze At The Sight of Vehicles [MDB IGNORE] (#20711)

* Turns Deer into Basic Mob - They Freeze At The Sight of Vehicles (#74784)

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

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* Turns Deer into Basic Mob - They Freeze At The Sight of Vehicles

---------

Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>
Signed-off-by: Vladimir Veisman <v.veisman@flashie.me>

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[e1149c6fa7...](https://github.com/pytorch/pytorch/commit/e1149c6fa777f6e0e4e61ba8263b047af6be26e1)
#### Tuesday 2023-05-16 18:45:26 by Joel Schlosser

Update base for Update on "(WIP; DO NOT REVIEW) Use python tensor subclass version of NT for PT2"


I'm out next week so I'm dumping some stuff here for whoever is interested. Added some notes inline. Other things:
* Main idea: convert real NT -> fake / meta instance of `NestedTensor` python tensor subclass during tracing and use that throughout the rest of the PT2 stack
* Python tensor subclass only supports contiguous for now
    * Only need `sizes` because of this, and `sizes` is a dim-length list containing int / List[int] items (for ragged dims) OR SymInts for dynamic shapes (will probably only support this case anyway)
* Inference-only for now; ignore Autograd
* Skip functionalization on NTs for now (there's no in-place op support anyway, although we should ideally handle NT <-> T views within functionalization)

Example script:
```python
import torch
from torch.nested import nested_tensor
from torch.nested._nested_tensor import NestedTensor
from torch._inductor import debug

torch._inductor.config.debug = True
torch._dynamo.config.traceable_tensor_subclasses.add(NestedTensor)

device = 'cuda'

def make_tensor(*shape, device=device, dtype=torch.float32):
    return torch.randn(*shape, device=device, dtype=dtype)

torch.manual_seed(1)

def fn(x, x_offsets):
    x_nt = torch._nested_view_from_jagged(x, x_offsets)
    x_nt = x_nt + 69
    x_nt = x_nt * 42
    return x_nt

torch._dynamo.disallow_in_graph(torch.diff)

compiled_fn = torch.compile(fn)

# shape (sum(*), D)
# component shapes: (3, 5), (4, 5), (6, 5)
x = make_tensor(13, 5)
x_offsets = torch.tensor([0, 3, 7, 13], dtype=torch.int64, device=device)

# helps create dynamic graph right away
torch._dynamo.mark_dynamic(x, 0)
torch._dynamo.mark_dynamic(x_offsets, 0)

output = compiled_fn(x, x_offsets)

# shape (sum(*), D)
# component shapes: (2, 5), (6, 5), (4, 5), (5, 5)
y = make_tensor(17, 5)
y_offsets = torch.tensor([0, 2, 8, 12, 17], dtype=torch.int64, device=device)

output2 = compiled_fn(y, y_offsets)

print(output)
print(output2)
```

WARNING: AWFUL HACKS AHEAD. DO NOT REVIEW YET.

cc soumith voznesenskym penguinwu anijain2305 EikanWang jgong5 Guobing-Chen XiaobingSuper zhuhaozhe blzheng Xia-Weiwen wenzhe-nrv jiayisunx peterbell10 desertfire

[ghstack-poisoned]

---
## [masline147/Fluffy-STG](https://github.com/masline147/Fluffy-STG)@[500cdb9257...](https://github.com/masline147/Fluffy-STG/commit/500cdb925720c408de4332df6b2d8b8e0b20b63c)
#### Tuesday 2023-05-16 18:49:43 by SkyratBot

north star's asylum no longer spawns with prisoners [MDB IGNORE] (#20732)

* north star's asylum no longer spawns with prisoners (#74879)

## About The Pull Request
the asylum on the north star no longer spawns prisoners, only the
permabrig does
the computer in the asylum is rotated correctly

## Why It's Good For The Game
on the paper, it seems like a cool concept, but theres a few issues here
the psychologist isnt designed to handle prisoners in the first place.
this is fine on mrp but it gets kinda muddy when prisoners on lrp like
beating people up
prisoners are recommended as a new player role by the wiki (very
stupid), this role starting in an asylum without anything to do while
being asked some stuff by a psychologist seems like itd add onto
confusion
players dont know what jobs are spawning with them, there very well may
not be a cmo or psychologist. if theres no one in sec you can deal with
that because you have a small botany and kitchen, and can possibly
escape. this aint a thing here, only thing you have is reading books and
maybe pen and paper rpgs if another prisoner spawns, while being stuck
in an extremely tiny space

this can work in the future i think, but it requires code support we
currently dont have, so it better to cut its

## Changelog
:cl:
del: prisoner spawns from the north star asylum
/:cl:

* north star's asylum no longer spawns with prisoners

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>
Signed-off-by: Vladimir Veisman <v.veisman@flashie.me>

---
## [The-GhostRider/azerothcore-wotlk](https://github.com/The-GhostRider/azerothcore-wotlk)@[ef949f9ff0...](https://github.com/The-GhostRider/azerothcore-wotlk/commit/ef949f9ff0a89e837c67258d7e199da1706bc438)
#### Tuesday 2023-05-16 19:25:36 by ICXCNIKA

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
## [k21971/EvilHack](https://github.com/k21971/EvilHack)@[8dcbbecd00...](https://github.com/k21971/EvilHack/commit/8dcbbecd00f5c32e50ff1e0f3c48d40497af5e11)
#### Tuesday 2023-05-16 19:26:57 by k21971

Drow aura of darkness and sources of 'artifact light'.

Drow using aura of darkness (player or monster) uses litroom(), which
has a code that can diminish sources that use artifact_light()
(artifacts, various pieces of armor). Now that a couple players have
ascended this version, it's been observed that this effect coming
directly from a monster is annoying and not quite right. This effect was
initially reserved for blessed/cursed scrolls of light (magic), a
monster's natual ability probably shouldn't be quite so powerful.

A monster's aura of darkness will still extinguish normal light sources
(lamps [even magic lamps], candles) but will leave more powerful sources
of light alone.

---
## [zeta96/L_soul_santoni_msm4.9](https://github.com/zeta96/L_soul_santoni_msm4.9)@[f74d1330d3...](https://github.com/zeta96/L_soul_santoni_msm4.9/commit/f74d1330d3168d025b4e9040c072a9ebbe77c378)
#### Tuesday 2023-05-16 19:51:14 by Jason A. Donenfeld

random: use linear min-entropy accumulation crediting

commit c570449094844527577c5c914140222cb1893e3f upstream.

30e37ec516ae ("random: account for entropy loss due to overwrites")
assumed that adding new entropy to the LFSR pool probabilistically
cancelled out old entropy there, so entropy was credited asymptotically,
approximating Shannon entropy of independent sources (rather than a
stronger min-entropy notion) using 1/8th fractional bits and replacing
a constant 2-2/√𝑒 term (~0.786938) with 3/4 (0.75) to slightly
underestimate it. This wasn't superb, but it was perhaps better than
nothing, so that's what was done. Which entropy specifically was being
cancelled out and how much precisely each time is hard to tell, though
as I showed with the attack code in my previous commit, a motivated
adversary with sufficient information can actually cancel out
everything.

Since we're no longer using an LFSR for entropy accumulation, this
probabilistic cancellation is no longer relevant. Rather, we're now
using a computational hash function as the accumulator and we've
switched to working in the random oracle model, from which we can now
revisit the question of min-entropy accumulation, which is done in
detail in <https://eprint.iacr.org/2019/198>.

Consider a long input bit string that is built by concatenating various
smaller independent input bit strings. Each one of these inputs has a
designated min-entropy, which is what we're passing to
credit_entropy_bits(h). When we pass the concatenation of these to a
random oracle, it means that an adversary trying to receive back the
same reply as us would need to become certain about each part of the
concatenated bit string we passed in, which means becoming certain about
all of those h values. That means we can estimate the accumulation by
simply adding up the h values in calls to credit_entropy_bits(h);
there's no probabilistic cancellation at play like there was said to be
for the LFSR. Incidentally, this is also what other entropy accumulators
based on computational hash functions do as well.

So this commit replaces credit_entropy_bits(h) with essentially `total =
min(POOL_BITS, total + h)`, done with a cmpxchg loop as before.

What if we're wrong and the above is nonsense? It's not, but let's
assume we don't want the actual _behavior_ of the code to change much.
Currently that behavior is not extracting from the input pool until it
has 128 bits of entropy in it. With the old algorithm, we'd hit that
magic 128 number after roughly 256 calls to credit_entropy_bits(1). So,
we can retain more or less the old behavior by waiting to extract from
the input pool until it hits 256 bits of entropy using the new code. For
people concerned about this change, it means that there's not that much
practical behavioral change. And for folks actually trying to model
the behavior rigorously, it means that we have an even higher margin
against attacks.

Cc: Theodore Ts'o <tytso@mit.edu>
Cc: Dominik Brodowski <linux@dominikbrodowski.net>
Cc: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Reviewed-by: Eric Biggers <ebiggers@google.com>
Reviewed-by: Jean-Philippe Aumasson <jeanphilippe.aumasson@gmail.com>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [Stage2Sec/go-cty](https://github.com/Stage2Sec/go-cty)@[97bafac0de...](https://github.com/Stage2Sec/go-cty/commit/97bafac0dea33a3f74db88ab54dea2937b9e8aef)
#### Tuesday 2023-05-16 19:58:06 by Martin Atkins

Remove all of the encoding/gob support code

I originally introduced all of this here as a concession to trying to
HashiCorp trying to get cty values to round-trip through the various
very magical gob-based wire interfaces in Terraform v0.11 and earlier,
back when they thought cty and what became "HCL 2" would just be a drop-in
replacement for HCL 1 and the various different competing representations
of dynamic values.

However, in practice none of that ever actually worked out and instead
Terraform now natively uses cty JSON/msgpack and other such mechanisms for
its wire protocols, making this gob handling code redundant.

This stuff caused various maintenance headaches and panic bugs which make
them a burden to retain. Although this is technically a breaking change
to the public cty API, in practice this stuff was only here to allow
Terraform to use it _indirectly_ as a side-effect of passing values into
the encoding/gob package, and so I'm treating it as if it had been an
internal implementation detail even though in principle it could've been
depended on externally. If anyone was doing that, I'm sorry; I suggest
copying the relevant support code into your own package instead if you
wish to continue using cty with gob.

---
## [Bens-Jammin/ExpenseTracker](https://github.com/Bens-Jammin/ExpenseTracker)@[3235b43a40...](https://github.com/Bens-Jammin/ExpenseTracker/commit/3235b43a40b3dbf79adf9e1a58652ed1c85e5e1d)
#### Tuesday 2023-05-16 20:07:57 by Ben

i am going to blow my fucking brains out i hate gradle so goddamn much

---
## [specks-dining/Codecademy](https://github.com/specks-dining/Codecademy)@[4183bd0b48...](https://github.com/specks-dining/Codecademy/commit/4183bd0b481b354961d15963e58d22c581ebab5e)
#### Tuesday 2023-05-16 21:01:52 by specks-dining

Create python-furniture-store.py

We’ve decided to pursue the dream of small-business ownership and open up a furniture store called Lovely Loveseats for Neat Suites on Fleet Street. With our newfound knowledge of Python programming, we’re going to build a system to help speed up the process of creating receipts for your customers.

In this project, we will be storing the names and prices of a furniture store’s catalog in variables. You will then process the total price and item list of customers, printing them to the output terminal.

Please note: Projects do not run tests against your code. This experience is more open to your interpretation and gives you the freedom to explore. Remember that all variables must be declared before they are referenced in your code.

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Unstuck“ to see a project walkthrough video.

Adding In The Catalog

1. Let’s add in our first item, the Lovely Loveseat that is the store’s namesake. Create a variable called lovely_loveseat_description and assign to it the following string:

Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.

2. Great, now let’s create a price for the loveseat. Create a variable lovely_loveseat_price and set it equal to 254.00.

3. Let’s extend our inventory with another characteristic piece of furniture! Create a variable called stylish_settee_description and assign to it the following string:

Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.

4. Now let’s set the price for our Stylish Settee. Create a variable stylish_settee_price and assign it the value of 180.50.

5. Fantastic, we just need one more item before we’re ready for business. Create a new variable called luxurious_lamp_description and assign it the following:

Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.

6. Let’s set the price for this item. Create a variable called luxurious_lamp_price and set it equal to 52.15.

7. In order to be a business, we should also be calculating sales tax. Let’s store that in a variable as well. Define the variable sales_tax and set it equal to .088. That’s 8.8%.

Our First Customer

8. Our first customer is making their purchase! Let’s keep a running tally of their expenses by defining a variable called customer_one_total. Since they haven’t purchased anything yet, let’s set that variable equal to 0 for now.

9. We should also keep a list of the descriptions of things they’re purchasing. Create a variable called customer_one_itemization and set that equal to the empty string "". We’ll tack on the descriptions to this as they make their purchases.

10. Our customer has decided they are going to purchase our Lovely Loveseat! Add the price to customer_one_total.

11. Let’s start keeping track of the items our customer purchased. Add the description of the Lovely Loveseat to customer_one_itemization.

12. Our customer has also decided to purchase the Luxurious Lamp! Let’s add the price to the customer’s total.

13. Let’s keep the itemization up-to-date and add the description of the Luxurious Lamp to our itemization.

14. They’re ready to check out! Let’s begin by calculating sales tax. Create a variable called customer_one_tax and set it equal to customer_one_total times sales_tax.

15. Add the sales tax to the customer’s total cost.

16. Let’s start printing up their receipt! Begin by printing out the heading for their itemization. Print the phrase "Customer One Items:".

17. Print customer_one_itemization.

18. Now add a heading for their total cost: Print out "Customer One Total:"

19. Now print out their total! Our first customer now has a receipt for the things they purchased.

20. Congratulations! We created our catalog and served our first customer. We used our knowledge of strings and numbers to create and update variables. We were able to print out an itemized list and a total cost for our customer. Lovely!

---
## [grorg/WebKit](https://github.com/grorg/WebKit)@[e0de92594a...](https://github.com/grorg/WebKit/commit/e0de92594a2f4a244443ab69a3f4f25aeacc1a2e)
#### Tuesday 2023-05-16 21:42:39 by Dean Jackson

WebXR: Severe aliasing in WebXR experiences (with WebGL1 contexts)
https://bugs.webkit.org/show_bug.cgi?id=256861
rdar://109424254

Reviewed by NOBODY (OOPS!).

WebXR sessions using WebGL1 contexts are unable to turn on
multisampling. I'm pretty sure this was my fault, but I can't
remember if it was intentional or a mistake. Either way it is
a bug.

Fix this by implementing the multisample renderbuffer creation
and resolution steps. Since we're doing this on a WebGL1 context,
the normal API will be invalid (it requires GLES3), so call the
extension API instead. This means we need to expose some extra methods
on GraphicsContextGL.

Lastly, the framebuffer textures we get are SRGB8_ALPHA8 which
requires an extension to be enabled with a WebGL1 context.

* Source/WebCore/Modules/webxr/WebXROpaqueFramebuffer.cpp:
(WebCore::WebXROpaqueFramebuffer::endFrame): call blitFramebufferANGLE.
(WebCore::WebXROpaqueFramebuffer::setupFramebuffer): Implement logic for WebGL 1.
* Source/WebCore/platform/graphics/GraphicsContextGL.h:
* Source/WebCore/platform/graphics/angle/GraphicsContextGLANGLE.cpp: Implement the extension API/
(WebCore::GraphicsContextGLANGLE::renderbufferStorageMultisampleANGLE):
(WebCore::GraphicsContextGLANGLE::blitFramebufferANGLE):
* Source/WebCore/platform/graphics/angle/GraphicsContextGLANGLE.h:
* Source/WebCore/platform/graphics/cocoa/GraphicsContextGLCocoa.mm:
(WebCore::GraphicsContextGLCocoa::platformInitialize): Turn on the sRGB extension.
* Source/WebKit/GPUProcess/graphics/RemoteGraphicsContextGL.messages.in:
* Source/WebKit/GPUProcess/graphics/RemoteGraphicsContextGLFunctionsGenerated.h:
(renderbufferStorageMultisampleANGLE):
(blitFramebufferANGLE):
* Source/WebKit/WebProcess/GPU/graphics/RemoteGraphicsContextGLProxy.h:
* Source/WebKit/WebProcess/GPU/graphics/RemoteGraphicsContextGLProxyFunctionsGenerated.cpp:
(WebKit::RemoteGraphicsContextGLProxy::renderbufferStorageMultisampleANGLE):
(WebKit::RemoteGraphicsContextGLProxy::blitFramebufferANGLE):

---
## [GoldenAlpharex/tgstation](https://github.com/GoldenAlpharex/tgstation)@[56d960a763...](https://github.com/GoldenAlpharex/tgstation/commit/56d960a7630d0b03bfcd59c073b29393a70a1891)
#### Tuesday 2023-05-16 22:02:54 by GoldenAlpharex

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
## [openai/evals](https://github.com/openai/evals)@[b93700ab49...](https://github.com/openai/evals/commit/b93700ab496bd112f89821777edc6a22d5972fb2)
#### Tuesday 2023-05-16 22:08:34 by DunedainStrider

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
## [freeformstu/rules_rust](https://github.com/freeformstu/rules_rust)@[80f0eb488a...](https://github.com/freeformstu/rules_rust/commit/80f0eb488ab9cabc4920ac446478cbf2feedc3f3)
#### Tuesday 2023-05-16 22:16:02 by scentini

Support for `no_std` mode (#1934)

Initial support for `no_std` mode.
This allows us to
1. Don't pass the whole standard library to compile actions that specify `no_std`
2. Conditionally select `crate_features` and `deps` based on whether `no_std` mode is used.
Currently the only supported modes are `off` and `alloc`, with a possibility to expand in the future.

The `no_std` support comes with the following caveats:
1. Targets in `exec` mode are still built with `std`; the logic here being that if a device has enough space to run bazel and rustc, std's presence would not be a problem. This also saves some additional transitions on `proc_macro`s (they need `std`), as they are built in `exec` mode.
2. Tests are still built with `std`, as `libtest` depends on `libstd`

There is quite an ugly hack to make us be able to `select` on the `no_std` flavor taking `exec` into account; I'm looking forward to the day where Bazel will expose better ways to inspect the cfg.

There is also one part I didn't manage to make work - having a `rust_test` that tests the `rust_shared_library` in `cc_common.link` mode; I got a link error for missing `__rg_alloc` & co. symbols, which should be present as we pass `--@rules_rust//rust/settings:experimental_use_global_allocator=True`. Unfortunately I could only spot this error on CI, and could not reproduce locally. I removed the test because the `rust_shared_library` is already tested via a `cc_test`. I will however give another shot at inspecting how my local setup differs from CI.

The `rust_binary` source code in `main.rs` was borrowed from https://github.com/jfarrell468/no_std_examples, big thanks to @jfarrell468 for letting me use it.

Co-authored-by: Krasimir Georgiev <krasimir@google.com>
Co-authored-by: UebelAndre <github@uebelandre.com>

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[1db699b36b...](https://github.com/git-for-windows/git/commit/1db699b36b7463f893c7ec791be18c293b85a183)
#### Tuesday 2023-05-16 22:33:02 by Johannes Schindelin

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
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[835952ccf4...](https://github.com/tgstation/tgstation/commit/835952ccf42af58db7238a572d7df6a9b8b2afd7)
#### Tuesday 2023-05-16 23:02:12 by MrMelbert

Drunk slurring scales based on how drunk you are (#75459)

## About The Pull Request

The strength of the slurring effect drunkness applies on you now scales
based on how drunk you are.

Being "a little" drunk still changes your saymod, and makes you
occasionally slur your words...


![image](https://github.com/tgstation/tgstation/assets/51863163/1b21b359-a1f9-428a-8e10-d2028ac59728)

But being "a lot" drunk kicks it up to 11


![image](https://github.com/tgstation/tgstation/assets/51863163/9d593c80-75ff-4d02-8e7c-e48c738154bb)

Additionally, drunk slurring was separated into "generic slurring" and
"drunk slurring", the former which does not scale but less closely
resembles drunkness. Generic slurring is used in places such as
concussions, so this is an added bonus.

As a result of the split, I had to update mind restoration. Now it heals
all types of slurring, which does include cult slurs.

## Why It's Good For The Game

I, and many other people, always found it very annoying when you became
completely illegible from taking one sip of a drink. This seeks to amend
that by making low levels of drunkness still for the most part be
legible and sane. Average drunkness is roughly the same / equal to the
old slurring effect, while "very drunk" is even more illegible and silly
(which I find funny).

This has the added bonus of separating out "drunk slurring" and "generic
slurring", allowing effects to slur your words without going full ham on
drunkness (burping and "huhh"s).

## Changelog

:cl: Melbert
add: When you are drunk, the strength of your slurring now varies based
on how drunk you are. Being "a little drunk" only rarely slurs your
words, being average drunk is the same as the old effect, while being
very drunk now slurs your words even more.
add: Some non-alcohol sources of slurring, such as concussions, now give
"generic slurring" rather than "drunk slurring", which less resemble
being drunk (ie, no burping).
add: Mind restoration now heals ALL slurring, rather than only drunk
slurring (which includes cult / heretic slurring).
/:cl:

---
## [fragglet/sdl-sopwith](https://github.com/fragglet/sdl-sopwith)@[5c7272659a...](https://github.com/fragglet/sdl-sopwith/commit/5c7272659a4f65ea236aca79adab5d6a5443c0a9)
#### Tuesday 2023-05-16 23:12:43 by Simon Howard

More tweaks to the beginner's help screen.

First of all, we should only ever show help on the first level.

Secondly, make the help screen appear less often in novice mode. It's not
necessary to keep showing it after the player has demonstrated that they know
the controls.  We identify this by tracking how long the player manages to keep
the plane in the air; if they manage to successfully fly it for at least 8
seconds without crashing, that's considered a successful flight and we won't
show help again.

Third, show the help screen as a hint in the other single player modes as well:
but only if they appear to be really struggling to get the plane off the
ground. We identify this if they crash the plane three times without managing a
single successful flight. This seems like a reasonably conservative metric that
shouldn't annoy experienced players by putting a bunch of text on the screen
that they won't care about.

To support the latter, also move the help text onto the left hand side of the
screen. This is because the right side is the side from which the enemy plane
will flying from to attack the player in "vs. computer" mode. We don't want the
text to obscure this.

---
## [Kitsunemitsu/lobotomy-corp13](https://github.com/Kitsunemitsu/lobotomy-corp13)@[928b2420d9...](https://github.com/Kitsunemitsu/lobotomy-corp13/commit/928b2420d906fbdef89ce27d75db5afe713b147d)
#### Tuesday 2023-05-16 23:14:06 by Lance

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

