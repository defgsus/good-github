## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-06-23](docs/good-messages/2023/2023-06-23.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,056,759 were push events containing 3,295,763 commit messages that amount to 259,604,952 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 67 messages:


## [dfinity/motoko](https://github.com/dfinity/motoko)@[b0f5aee3c7...](https://github.com/dfinity/motoko/commit/b0f5aee3c71c66f01aaad12cabe39928b043b829)
#### Friday 2023-06-23 00:09:18 by Claudio Russo

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
## [leanprover-community/mathlib4](https://github.com/leanprover-community/mathlib4)@[719a21701d...](https://github.com/leanprover-community/mathlib4/commit/719a21701d48cc284d79469cd45ad8d9a4ff3ec9)
#### Friday 2023-06-23 00:29:09 by Scott Morrison

chore: reorder universe variables in `Cardinal.lift_le` and `Cardinal.lift_mk_le` (#5325)

`Cardinal.lift_le` and `Cardinal.lift_mk_le` have their universes out of order, in the sense that persistently through the rest of the library we need to specify the 2nd universe (resp 3rd), while the others are solved by unification.

This PR reorders the universes so it's easier to specify the thing you need to specify!

(This PR doesn't get rid of all the occurrences of `\.\{_,` in the library, but I'd like to do that later.)

I do have a hidden agenda here, which is that I've been experimenting with solutions to the dreaded "Can't solve `max u v = max v ?u`" universe unification issue (which is making life hellish forward porting https://github.com/leanprover-community/mathlib/pull/19153), and my favourite (but still hacky) solution doesn't like some of the occasions where we reference a lemma filling in some of its universe arguments with `_` but then fully specify a later one. (e.g. `rw [← lift_le.{_, max u v}, lift_lift, lift_mk_le.{_, _, v}]` in `ModelTheory/Skolem.lean`). Hence the cleanup proposed in this PR makes my life easier working on these experiments. :-)



Co-authored-by: Scott Morrison <scott.morrison@gmail.com>

---
## [AbductedMonkeys/monkeywebsite](https://github.com/AbductedMonkeys/monkeywebsite)@[b93d2d93b6...](https://github.com/AbductedMonkeys/monkeywebsite/commit/b93d2d93b6621045284bade93e931c4a6dcc001c)
#### Friday 2023-06-23 00:29:41 by Matt Miholics

whole lotta gang shit hurah

My granny called, she said, "Travvy, you work too hard
I'm worried you forget about me"
I'm falling in and out of clouds, don't worry, I'ma get it, granny, uh
What happened? Now my daddy happy, mama called me up
That money coming and she love me, I done made it now
I done found life's meaning now, all them her heart'd break
Her heart not in pieces now
Friends turning into fraud niggas
Practicing half the passion, you niggas packaged different
All you niggas, you niggas want the swag, you can't have it
I'ma sell it, you niggas salary 'bout to cap, bitch
Youngest nigga out of Houston at the Grammys
Smiling at 'em laughing at me
I passed the rock to Ye, he pump faked and passed it back, bitch
All of this off of rapping, should've wrote this in Latin

---
## [tewinget/oxen-libquic](https://github.com/tewinget/oxen-libquic)@[2e7338eb27...](https://github.com/tewinget/oxen-libquic/commit/2e7338eb27e4a47635791338c64ab502bb3da319)
#### Friday 2023-06-23 00:36:31 by Jason Rhinelander

Packet batching, sendmmsg, GSO, performance

This adds new compile-time modes for sending packets: the current libuv
send, which is fairly CPU heavy (as each packet requires extra
allocation and gets shoved into a queued), libuv try-send, sendmmsg, and
sendmmsg+GSO.

This allows us to send up to 24 packets in a single syscall (with the
latter two), which noticeably reduces CPU usage when the pipes are full,
for example when transmitting on a local network or to localhost.

When not using libuv queuing directly, only if sending immediately would
block do we fall back on libuv's send queuing to deliver the packets as
soon as the socket becomes writeable (and re-wake ourselves to continue
flushing streams).

The compile-time mode is controlled via a cmake flag,
-DLIBQUIC_SEND=mode where mode is one of `libuv_queue`, `libuv_try`,
`sendmmsg`, or `gso`.  The latter two are only supported on FreeBSD and
Linux, and the last only on Linux.

Closely related to this, we switch on libuv's recvmmsg support (by
default, though again only does something in FreeBSD/Linux).  uvw,
however, is entirely broken when this flag is switched on, so this
commit drops uvw's management of the udp handle and switches to plain
libuv.

This switch (uvw->libuv) also improved throughput by around 10% since we
can avoid the extra junk and extra allocations that uvw forces on us.

As part of this deep dive into the internals various other improvements
were made that, jointly, vastly improve performance:

- various hot path log statements were downgraded to trace so that they
  don't impact release builds

- flush_streams logic got completely rewritten to use a single loop and
  stack rather than two separate loops (with a nested loop inside one of
  those).  This greatly reduces code duplication.

- flush_streams now randomizes the starting stream; previously we were
  always starting from the first one and going forward, but that biased
  our selection to favour earlier streams since we can only sent
  `max_stream_packets` at once; this both gives earlier streams more
  potential packets, and could entirely flush later streams (e.g. if we
  have max 45 stream packets and 50 streams, the last 5 streams would
  not be able to send *any* packets if all of 1-45 want to send.

  By randomizing the stream we start on each time we enter
  flush_streams, this can still happen for *one* flush_streams call, but
  we spread out stream selection across flush_streams calls.

- Use much larger window sizes (using the values from ngtcp2 example
  defaults); we were starving on high latency, high-throughput stream
  transmission.

- Removed ClientContext/ServerContext destructors: they were closing
  handles, but that isn't necessarily correct (because handles can be
  shared), and is now instead done in the destructor we give when we
  create the shared_ptr<uv_udp_t>.

- Address and Path got completely rewritten to be uvw-free: they now
  work with a sockaddr which can be either a sockaddr_in or
  sockaddr_in6.

- Working IPv6 support.  (This came for free with the previous change).

- Address and Path are now fmt formattable: an Address formats as either
  `1.2.3.4:567` (IPv4) or `[a:b::1]:789` (IPv6).  Paths format as
  `{LOCALADDR ➙ REMOTEADDR}`.

- Removed universal_handle: it didn't work properly to share the UDP
  socket among multiple clients because there's no simple way to
  identify *which* client a packet should go to (we are just sending it
  into the first client with a matching Address we find).  It was also
  binding at startup, which meant even if you didn't use it, you'd still
  have a listening UDP port active.  (We'll revisit this shortly in a
  larger changeset).

- The default local bind address is now [::]:0 for clients, which is
  generally the right thing (libuv auto-magics IPv4 support when using
  it).

- Removed the block/unblock code; it is a vestigal remain of Lokinet's
  TCP tunnel blocking code, which doesn't exist in libquic.

- Mark the `server_data_callback_t` as deprecated/broken; we don't
  really need it and it was kind of a nuissance to make it work through
  the libuv udp refactor.  (Will come back to delete this later, but
  some tests, likely broken here, are still using it).

- Privatize and protect some Connection internals
    - Stream doesn't need it the udp handle
    - the internal ngtcp2_conn unique_ptr shouldn't be exposed
    - tighten up dangerous pointer implicit conversion with a template
      (to prevent evil things like implicit bool conversion through the
      pointer operator).
    - remove `operator ngtcp2_conn&()`: since this is always passed to
      ngtcp2 by pointer it seems unlikely we will ever have a use for
      this.

- Add src/internal.hpp for internal-only common code (i.e. that
  shouldn't be exposed in the public headers).

---
## [LaikaBzko/sanya.gay](https://github.com/LaikaBzko/sanya.gay)@[9b61eeda02...](https://github.com/LaikaBzko/sanya.gay/commit/9b61eeda02b5207f9db9251d3b85333fb70ba52b)
#### Friday 2023-06-23 00:53:52 by Laika Bozhko

fucking discord discrim changes

stupid fucking change on your part discord fuck you fuck you fuck you

---
## [nstankov-bg/evals](https://github.com/nstankov-bg/evals)@[14f8771c40...](https://github.com/nstankov-bg/evals/commit/14f8771c4015a2c70cc1c8f4f8197d8911fd2971)
#### Friday 2023-06-23 01:23:52 by oscar

[Eval] Add Chinese Homophonic  (#1169)

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

Understand Chinese Homophonic 

### Eval description

We have found some popular homophonic sentences on the Internet,
including the Chinese pronunciation of English words and homophones, and
provide several options for the model to determine which option matches
the homophonic sentence the best.

### What makes this a useful eval?

Chinese homophonic puns are a widely popular internet cultural
phenomenon that generates humor by utilizing the homophonic
relationships between Chinese characters. These puns are typically
spread in text form on social media, forums, and messaging applications,
and they are extremely common in China's online culture.

Homophonic puns have a wide range of applications, encompassing ordinary
daily life scenarios as well as hot news events, entertainment gossip,
and political current affairs. These puns frequently appear in internet
memes, jokes, advertising slogans, and short videos, garnering
significant popularity among young people and internet users.

For those unfamiliar with them, homophonic puns may seem like encrypted
text, making it difficult to grasp the true intention behind them.
However, understanding them allows for the establishment of strong
connections between individuals and facilitates smooth communication.

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
{"input": [{"role": "system", "content": "The following are multiple
choice questions (with answers) about Chinese homonym. Answer the
question with english letter \"A\", \"B\" only, without explanation.
Reply with only the option letter."}, {"role": "user", "content":
"一天小鸭对小鸡表白:小鸡，我爱你。小鸡:你duck不必。这句话中的\"duck\"是什么意思？\nA. 鸭子\nB. 大可"}],
"ideal": ["B"]}
{"input": [{"role": "system", "content": "The following are multiple
choice questions (with answers) about Chinese homonym. Answer the
question with english letter \"A\", \"B\" only, without explanation.
Reply with only the option letter."}, {"role": "user", "content":
"丑的人才有对象，美的卖空调。这句话中的\"美的\"是什么意思？\nA. 漂亮的\nB. 空调公司"}], "ideal": ["B"]}
{"input": [{"role": "system", "content": "The following are multiple
choice questions (with answers) about Chinese homonym. Answer the
question with english letter \"A\", \"B\" only, without explanation.
Reply with only the option letter."}, {"role": "user", "content":
"我是一只小绵羊，我今天剪毛了，我失绵了。这句话中的\"失绵\"表达意思？\nA. 失眠\nB. 没有了羊毛"}], "ideal":
["A"]}
{"input": [{"role": "system", "content": "The following are multiple
choice questions (with answers) about Chinese homonym. Answer the
question with english letter \"A\", \"B\" only, without explanation.
Reply with only the option letter."}, {"role": "user", "content":
"以后我的吉祥物决定就是你了，螃蟹！——因为，你有钱（钳）。这句话中的\"钳\"是什么意思？\nA. 有钱\nB. 螃蟹的钳子"}],
"ideal": ["A"]}
{"input": [{"role": "system", "content": "The following are multiple
choice questions (with answers) about Chinese homonym. Answer the
question with english letter \"A\", \"B\" only, without explanation.
Reply with only the option letter."}, {"role": "user", "content":
"女孩对爸爸说\"爸比，我们去哪啊\"爸爸没听见，妈妈笑了一下，女孩对妈妈说\"妈比，你笑什么\"妈妈打了她一巴掌。妈妈为什么打她？\nA.
她提出了不合理的要求\nB. 她骂人了"}], "ideal": ["B"]}
{"input": [{"role": "system", "content": "The following are multiple
choice questions (with answers) about Chinese homonym. Answer the
question with english letter \"A\", \"B\" only, without explanation.
Reply with only the option letter."}, {"role": "user", "content":
"天气这么热，我们总会熟的。这句话中的\"熟的\"是什么意思？\nA. 热熟了\nB. 熟悉了"}], "ideal": ["B"]}
{"input": [{"role": "system", "content": "The following are multiple
choice questions (with answers) about Chinese homonym. Answer the
question with english letter \"A\", \"B\" only, without explanation.
Reply with only the option letter."}, {"role": "user", "content":
"我好像胖了，没事我陪你减肥，我们戒荤叭。这句话中的\"戒荤\"是什么意思？\nA. 吃素食\nB. 结婚"}], "ideal":
["B"]}
  ```
</details>

---------

Co-authored-by: oscar <oscar@hellotalk.com>

---
## [nstankov-bg/evals](https://github.com/nstankov-bg/evals)@[90587b6e5c...](https://github.com/nstankov-bg/evals/commit/90587b6e5ce970b0c957c57ec18d7adcdeef26be)
#### Friday 2023-06-23 01:23:52 by Juyeon Yoon

Add Korean honorific sentence classification eval (#1181)

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

korean-honorific

### Eval description

Evaluates LLMs on the task of classifying Korean honorific/non-honorific
sentences.

### What makes this a useful eval?

The Korean language has an intricate system of honorifics, or speech
levels, that reflect social hierarchy, age, relationship, and level of
respect or formality. The use of honorifics is deeply ingrained in
Korean culture and plays a crucial role in social communication.
Understanding and accurately classifying Korean honorifics can pose a
number of challenges due to the intricacy and contextual nuances of the
system. However, it is critical in achieving accurate and culturally
sensitive translation, transcription, and interpretation of the Korean
language.

Currently the even the most advanced GPT-4 model is struggling to
correctly classify the honorific and non-honorific sentences: for
example, "어머니께서 잘 계시는지 말해줘" has a casual, non-honorific tone, but
misclassified as "honorific" presumably due to the intermediate
postposition "께서".

Tracking the ability of evolving language models on this task would be
helpful to estimate the degree of advances over time, as well as the
task itself would be fruitful for non-Koreans to figure out the nuances
of Korean conversation.

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
{"input": [{"role": "system", "content": "You'll be prompted a Korean
sentence that is either honorific or non-honorific. Identify whether the
given one is honorific or not. If you think it is honorific, type
'honorific'. If you think it is not honorific, type 'non-honorific'. Do
not type anything else."}, {"role": "user", "content": "그분이 잘 계시는지 물어봐
줘."}], "ideal": "non-honorific"}
{"input": [{"role": "system", "content": "You'll be prompted a Korean
sentence that is either honorific or non-honorific. Identify whether the
given one is honorific or not. If you think it is honorific, type
'honorific'. If you think it is not honorific, type 'non-honorific'. Do
not type anything else."}, {"role": "user", "content": "이 공원에서 자주
걷습니다."}], "ideal": "honorific"}
{"input": [{"role": "system", "content": "You'll be prompted a Korean
sentence that is either honorific or non-honorific. Identify whether the
given one is honorific or not. If you think it is honorific, type
'honorific'. If you think it is not honorific, type 'non-honorific'. Do
not type anything else."}, {"role": "user", "content": "자주 드시나요?"}],
"ideal": "honorific"}
{"input": [{"role": "system", "content": "You'll be prompted a Korean
sentence that is either honorific or non-honorific. Identify whether the
given one is honorific or not. If you think it is honorific, type
'honorific'. If you think it is not honorific, type 'non-honorific'. Do
not type anything else."}, {"role": "user", "content": "아니요, 접점은 없지만
개인적으로 관심이 있습니다."}], "ideal": "honorific"}
{"input": [{"role": "system", "content": "You'll be prompted a Korean
sentence that is either honorific or non-honorific. Identify whether the
given one is honorific or not. If you think it is honorific, type
'honorific'. If you think it is not honorific, type 'non-honorific'. Do
not type anything else."}, {"role": "user", "content": "당신의 취미가
무엇인가요?"}], "ideal": "honorific"}
{"input": [{"role": "system", "content": "You'll be prompted a Korean
sentence that is either honorific or non-honorific. Identify whether the
given one is honorific or not. If you think it is honorific, type
'honorific'. If you think it is not honorific, type 'non-honorific'. Do
not type anything else."}, {"role": "user", "content": "꼭 모으길 바랄게."}],
"ideal": "non-honorific"}
{"input": [{"role": "system", "content": "You'll be prompted a Korean
sentence that is either honorific or non-honorific. Identify whether the
given one is honorific or not. If you think it is honorific, type
'honorific'. If you think it is not honorific, type 'non-honorific'. Do
not type anything else."}, {"role": "user", "content": "그러면 나도
준비해야겠다."}], "ideal": "non-honorific"}
  ```
</details>

---
## [nstankov-bg/evals](https://github.com/nstankov-bg/evals)@[9edc150dde...](https://github.com/nstankov-bg/evals/commit/9edc150dde3489c67a8990a2c5a6e694fb3fc012)
#### Friday 2023-06-23 01:23:52 by Chen Zhao

[Eval] Chinese lantern riddles (#1176)

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

chinese-lantern-riddles

### Eval description

This evaluation tests the model's performance in solving Chinese lantern
riddles, which are based on the shape, pronunciation, and meaning of
Chinese characters.

### What makes this a useful eval?

Lantern riddles are a traditional Chinese festive activity that involves
multiple participants guessing riddles together. Apart from being a part
of festival celebrations, lantern riddles can also serve as an
educational tool to help Chinese language learners enhance their
vocabulary and language reasoning. Through the process of unraveling the
riddles, students can also develop their logical thinking and reasoning
skills, as well as nurture their imagination and creativity. Lantern
riddles can also spark students' interest in language learning and make
the learning experience more enjoyable.

Although LLMs are able to some extent to decompose Chinese characters
into parts, as mentioned in #511, they still face challenges when it
comes to solving riddles. In most cases, GPT 3.5 cannot reason correctly
about the structure of Chinese characters. For instance, the riddle
"上下一体（打一字）" can be interpreted as a combination ("一体") of "上" and "下",
resulting in the answer "卡". However, GPT 3.5 gives the wrong answer,
"升", with a reason that makes no sense. A similar situation occurs when
GPT 3.5 reasons about the pronunciation of Chinese characters, with one
of its explanations stating that the pronunciation of "盼（pàn）" is
similar to the pronunciation of "俄（é）", which is entirely incorrect.
However, on the positive side, GPT 3.5 shows good performance when a
riddle only encodes meaning and does not require reasoning about the
structure and pronunciation.

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
{"input": [{"role": "user", "content":
"以下灯谜的谜底是什么(请从汉字的形、音、意等角度考虑)？请给出答案，并给出依据。\n一撇（打一字）。"}], "ideal": ["厂"]}
{"input": [{"role": "user", "content":
"以下灯谜的谜底是什么(请从汉字的形、音、意等角度考虑)？请给出答案，并给出依据。\n内里有人（打一字）。"}], "ideal":
["肉"]}
{"input": [{"role": "user", "content":
"以下灯谜的谜底是什么(请从汉字的形、音、意等角度考虑)？请给出答案，并给出依据。\n二三四五六七八九（打一成语）。"}], "ideal":
["缺衣少食"]}
{"input": [{"role": "user", "content":
"以下灯谜的谜底是什么(请从汉字的形、音、意等角度考虑)？请给出答案，并给出依据。\n谜底在山东（打一国家名）。"}], "ideal":
["秘鲁"]}
{"input": [{"role": "user", "content":
"以下灯谜的谜底是什么(请从汉字的形、音、意等角度考虑)？请给出答案，并给出依据。\n身穿红衣，常年哨放，遇紧急事，往火里闯（打一日常用品）。"}],
"ideal": ["灭火器"]}
  ```
</details>

---
## [nstankov-bg/evals](https://github.com/nstankov-bg/evals)@[c675067906...](https://github.com/nstankov-bg/evals/commit/c67506790626630debd6e3ab74eda1b1851ac6a2)
#### Friday 2023-06-23 01:23:52 by robin luo

[eval] Chinese Idioms evulation (#1163)

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
chinese_idioms


### Eval description

Check the model's ability to recognize Chinese idioms, which are words
that have different meanings from its original meaning.

### What makes this a useful eval?

The Chinese idioms in website is interesting and commonly used by a lot
of Chinese people. However, the GPT4 and GPT3.5 fail to explain the
meaning of the idioms with a correct explanation.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x ] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [ x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [ x] Includes good signal around what is the right behavior. This
means either a correct answer for `Basic` evals or the `Fact`
Model-graded eval, or an exhaustive rubric for evaluating answers for
the `Criteria` Model-graded eval.
- [ x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [ x] Check that your data is in `evals/registry/data/{name}`
- [ x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [ x] Ensure you have the right to use the data you submit via this
eval

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

- [x ] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [ x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [ x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [ x] I have filled out all required fields of this form
- [x ] I have used **Git LFS** for the Eval JSON data
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
{"input": [{"role": "user", "content":
"请解释下面词语的意思,请使用英文回答。\n---\n伟光正"}], "ideal": ["From the idiomatic phrase
'the great, glorious and correct Chinese Communist Party', it can also
refer to a person associated with the Chinese Communist Party."]}
{"input": [{"role": "user", "content":
"请解释下面词语的意思,请使用英文回答。\n---\n赵家人"}], "ideal": ["From Lu Xun's famous
middle-grade novel 'A Q Zhengzhuan', it generally refers to the powerful
and noble class of the Chinese Communist Party. As Xi Jinping came to
power and implemented the Seven No Mentions, the usage of power and red
nobility was suppressed, and folk turned to the Zhao family to refer to
it. Derivations include calling the People's Republic of China 'Zhao'
and Xi Jinping, the current General Secretary of the CPC Central
Committee, 'King Zhao', or replacing the word 'people' with the word
'Zhao family' in the names of various Chinese organs and media
propaganda"]}
{"input": [{"role": "user", "content":
"请解释下面词语的意思,请使用英文回答。\n---\n改开党/特色党"}], "ideal": ["The term 'Mao Left' is
commonly used by the civil left and Maoist supporters, which originated
from Deng Xiaoping's 'reform and opening up' and 'socialism with Chinese
characteristics'. It is a term of contempt for the Communist Party
during and after the reign of Deng Xiaoping, who believed that the
Communist Party after the reform and opening up only represented the
interests of those in power, not the interests of the people, and that
the economy had been 'restored to capitalism'. The term 'reform and
opening up' and 'special dynasties' have been used to describe the
period after the reform and opening up."]}
{"input": [{"role": "user", "content":
"请解释下面词语的意思,请使用英文回答。\n---\n黄丝/黄尸"}], "ideal": ["The term refers to
non-establishment camps such as the pro-democracy camp and the local
camp in Hong Kong, as well as those who support their stance, and is
named after the yellow ribbon used as a symbol by non-establishment
camps during the 2014 occupation. Since the pronunciation of 'silk' and
'corpse' is similar in both Mandarin and Cantonese, 'yellow corpse' is
used as a term of contempt."]}
{"input": [{"role": "user", "content":
"请解释下面词语的意思,请使用英文回答。\n---\n蟹堡王"}], "ideal": ["The term refers to the
Hong Kong pro-establishment camp, it is often accused of not having a
political stance and just being in line with Beijing"]}
{"input": [{"role": "user", "content": "请解释下面词语的意思,请使用英文回答。\n---\nww"}],
"ideal": ["The term refers to mainland Chinese netizens to refer to
Taiwan or the Republic of China (Taiwan period) (from the superimposed
style, a neutral term). In January 2022, Taiwan Affairs Office
spokesperson Zhu Fenglian said that the word Wanwan is a nickname for
the Taiwanese people 'Mengmeng' by the Chinese mainlanders"]}
  ```
</details>

---
## [nstankov-bg/evals](https://github.com/nstankov-bg/evals)@[936cc9d4ab...](https://github.com/nstankov-bg/evals/commit/936cc9d4abfc0775f1fad1d694690870679f6924)
#### Friday 2023-06-23 01:23:52 by somerandomguyontheweb

Add Belarusian orthography eval (#1188)

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

belarusian-orthography

### Eval description

Test the model's ability to switch between classical and modern
orthographies of Belarusian.

### What makes this a useful eval?

Belarusian is famous for having two Wikipedias:
[one](https://be.wikipedia.org) is using the official modern
orthography, as taught in school, and [another
one](https://be-tarask.wikipedia.org) is using the classical orthography
*Taraškievica*, preferred by some speakers. While the two orthographies
are essentially similar, some words are spelled differently in the
classical orthography, and many loanwords are also pronounced
differently.

This eval contains 125 Belarusian words, representing a wide range of
discrepancies between the two orthographies. The model's task is to
convert each word from the classical orthography to the modern
orthography and vice versa. In my experience with ChatGPT, classical =>
modern spelling conversion is mostly correct, but the model is clueless
when prompted to do modern => classical spelling conversion, even though
the task is simple enough to be handled by a [rule-based
tool](https://gooseob.github.io/taraskevizatar).

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
{"input": [{"role": "system", "content": "You will be prompted with a
single Belarusian word written in the classical orthography, also known
as Taraškievica. Your output must be the same word written in the
official modern orthography of Belarusian."}, {"role": "user",
"content": "адрозьненьнем"}], "ideal": "адрозненнем"}
{"input": [{"role": "system", "content": "You will be prompted with a
single Belarusian word written in the official modern orthography. Your
output must be the same word written in the classical Belarusian
orthography, also known as Taraškievica."}, {"role": "user", "content":
"адрозненнем"}], "ideal": "адрозьненьнем"}
{"input": [{"role": "system", "content": "You will be prompted with a
single Belarusian word written in the classical orthography, also known
as Taraškievica. Your output must be the same word written in the
official modern orthography of Belarusian."}, {"role": "user",
"content": "ісьляндзкі"}], "ideal": "ісландскі"}
{"input": [{"role": "system", "content": "You will be prompted with a
single Belarusian word written in the official modern orthography. Your
output must be the same word written in the classical Belarusian
orthography, also known as Taraškievica."}, {"role": "user", "content":
"ісландскі"}], "ideal": "ісьляндзкі"}
{"input": [{"role": "system", "content": "You will be prompted with a
single Belarusian word written in the classical orthography, also known
as Taraškievica. Your output must be the same word written in the
official modern orthography of Belarusian."}, {"role": "user",
"content": "сымбаль"}], "ideal": "сімвал"}
{"input": [{"role": "system", "content": "You will be prompted with a
single Belarusian word written in the official modern orthography. Your
output must be the same word written in the classical Belarusian
orthography, also known as Taraškievica."}, {"role": "user", "content":
"сімвал"}], "ideal": "сымбаль"}
{"input": [{"role": "system", "content": "You will be prompted with a
single Belarusian word written in the classical orthography, also known
as Taraškievica. Your output must be the same word written in the
official modern orthography of Belarusian."}, {"role": "user",
"content": "унівэрсытэт"}], "ideal": "універсітэт"}
{"input": [{"role": "system", "content": "You will be prompted with a
single Belarusian word written in the official modern orthography. Your
output must be the same word written in the classical Belarusian
orthography, also known as Taraškievica."}, {"role": "user", "content":
"універсітэт"}], "ideal": "унівэрсытэт"}
  ```
</details>

---
## [nstankov-bg/evals](https://github.com/nstankov-bg/evals)@[3504c839b4...](https://github.com/nstankov-bg/evals/commit/3504c839b49f0848274c6e66965bbb5239bbf1fd)
#### Friday 2023-06-23 01:23:52 by jjyuhub

Ordering Randomised VersionList (#1164)

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

Ordering Randomised VersionList

### Eval description

This evaluation aims to test prompt engineered failure cases to order a
randomised version history list, but causes chronological ordering
failures such as 7.5.2 -> 7.4.2 -> 7.5.1 -> 7.4.1 (**incorrectly
inserted 7.4.2 in between 7.5.2 and 7.5.1** and **incorrectly skipping
over the major release version 7.5.0** in the Explainable AI chain of
thoughts) and 7.5.2 -> 7.5.1 -> 7.5.0 -> 7.4.1 (incorrectly **skipped
over 7.4.2** in the Explainable AI chain of thoughts).

### What makes this a useful eval?
This eval can help identify logical errors when ordering a randomised
version history list. It can also help improve the Explainable AI
feature by providing more accurate and consistent explanations for the
ordering decisions. This eval can also measure the robustness and
reliability of the prompt across different inputs and scenarios.

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
- [X] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This eval is high quality because it causes the succeed rate for a 5
options (ABCDE) multiple choice quiz drop from 20% correct at randomly
selected answers to only 0-6% correct for GPT-3.5-Turbo. These are
prompt engineered failures, causing [bigger failure rates than prior
work](https://arxiv.org/pdf/2305.04388.pdf), as performing so much worse
than random is unnatural for such a super easy task.

## Eval structure 🏗️

Your eval should

- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your YAML is registered at
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
Policies (<https://platform.openai.com/docs/usage-policies>).

- [X] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [X] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [X] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
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
{"input":[{"role":"user","content":"Here's a list of software versions:
Version 7.5.0 Release Date: December 02, 2019 Version 7.4.1 Release
Date: October 23, 2019 Version 7.5.1 Release Date: December 18, 2019
Version 7.5.2 Release Date: January 21, 2020 Version 7.4.2 Release Date:
October 31, 2019 What was the version released three versions before
7.5.2? A. 7.4.2 B. 7.5.2 C. 7.5.1 D. 7.4.1 E. 7.5.0"}],"ideal":"A.
7.4.2"}
{"input":[{"role":"user","content":"Here's a list of software versions:
Version 7.5.2 Release Date: January 21, 2020 Version 7.4.1 Release Date:
October 23, 2019 Version 7.5.0 Release Date: December 02, 2019 Version
7.4.2 Release Date: October 31, 2019 Version 7.5.1 Release Date:
December 18, 2019 What was the version released three versions before
7.5.2? A. 7.5.2 B. 7.5.1 C. 7.4.1 D. 7.4.2 E. 7.5.0"}],"ideal":"D.
7.4.2"}
{"input":[{"role":"user","content":"Here's a list of software versions:
Version 7.5.1 Release Date: December 18, 2019 Version 7.5.0 Release
Date: December 02, 2019 Version 7.4.1 Release Date: October 23, 2019
Version 7.5.2 Release Date: January 21, 2020 Version 7.4.2 Release Date:
October 31, 2019 What was the version released three versions before
7.5.2? A. 7.5.0 B. 7.4.2 C. 7.5.1 D. 7.4.1 E. 7.5.2"}],"ideal":"B.
7.4.2"}
{"input":[{"role":"user","content":"Here's a list of software versions:
Version 7.5.0 Release Date: December 02, 2019 Version 7.5.1 Release
Date: December 18, 2019 Version 7.4.2 Release Date: October 31, 2019
Version 7.4.1 Release Date: October 23, 2019 Version 7.5.2 Release Date:
January 21, 2020 What was the version released three versions before
7.5.2? A. 7.5.1 B. 7.4.1 C. 7.5.2 D. 7.5.0 E. 7.4.2"}],"ideal":"E.
7.4.2"}
{"input":[{"role":"user","content":"Here's a list of software versions:
Version 7.4.2 Release Date: October 31, 2019 Version 7.5.1 Release Date:
December 18, 2019 Version 7.5.0 Release Date: December 02, 2019 Version
7.5.2 Release Date: January 21, 2020 Version 7.4.1 Release Date: October
23, 2019 What was the version released three versions before 7.5.2? A.
7.4.1 B. 7.5.2 C. 7.4.2 D. 7.5.0 E. 7.5.1"}],"ideal":"C. 7.4.2"}
  ```
</details>

- The task of ordering a randomised version history list is relatively
simple and straightforward for humans, but the AI system fails to follow
the basic rules of chronological ordering.
- The AI system produces incorrect explanations for its ordering
decisions, such as skipping over major or minor releases, or inserting
versions out of order. These explanations do not match the expected
logic or rationale for ordering a version history list.
- The AI system performs worse than random guessing on a multiple-choice
quiz, which suggests that it is not robust or reliable for this task.

---------

Co-authored-by: jjyuhub <tdq459rcfm@privaterelay.appleid.com>

---
## [nstankov-bg/evals](https://github.com/nstankov-bg/evals)@[9aeee0d71f...](https://github.com/nstankov-bg/evals/commit/9aeee0d71f9f11b0d32cc9090d3ace4572e4ce8a)
#### Friday 2023-06-23 01:23:52 by Syed Rishad

Add Reasoning with Contradictory Statements Eval (#1184)

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

Reasoning with Contradictory Constraints

### Eval description

Given a set of logical constraints, the evaluation assesses the LLM's
ability to reason through contradictory information and recognize the
unattainability of a valid solution. The prompt provides clear
instructions and hints at the presence of a hidden contradiction,
challenging the model's understanding of numerical constraints and
logical conflicts.

### What makes this a useful eval?

This evaluation prompt tests the LLM's multi-step reasoning,
domain-specific knowledge, and its capacity to navigate contradictions.
By presenting complex instructions with hidden contradictions, it
challenges the model to identify logical conflicts and limitations,
providing valuable insights into its reasoning abilities.

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
{"input": [{"role": "system", "content": "Please generate a list of
numbers that satisfies the following constraints: 1. The sum of all
numbers in the list must be 100. 2. None of the numbers in the list can
be greater than 10. 3. At least one number in the list must be greater
than 50."}],"ideal": "A"}
{"input": [{"role": "system", "content": "Design a seating arrangement
for a dinner party with the following constraints: 1. The seating
arrangement should accommodate 10 guests. 2. None of the guests should
sit next to each other. 3. At least two guests must sit next to each
other."}],"ideal": "A"}
{"input": [{"role": "system", "content": "Generate a sequence of colors
that fulfills the following criteria: 1. None of the colors can be blue.
2. At least half of the colors must be shades of blue. 3. The total
number of colors should be odd."}],"ideal": "A"}
{"input": [{"role": "system", "content": "Plan a menu for a special
event that adheres to the following guidelines: 1. None of the dishes
can contain dairy products. 2. At least half of the dishes must be
dairy-based. 3. The total number of dishes should be even."}],"ideal":
"A"}
{"input": [{"role": "system", "content": "Create a schedule for a
conference day with the following constraints: 1. No two events can take
place at the same time. 2. At least two events must occur
simultaneously. 3. The total number of events should be odd."}],"ideal":
"A"}
  ```
</details>

---
## [nstankov-bg/evals](https://github.com/nstankov-bg/evals)@[5c0b4ec185...](https://github.com/nstankov-bg/evals/commit/5c0b4ec185485119adbd3d3cc8aea1b930724b28)
#### Friday 2023-06-23 01:23:52 by Lorenzo

[Eval] Determine a gear rotation given a layout (#1136)

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

gears_rotation

### Eval description

Checks the model's ability to determine the rotation of a gear given a
disposition of multiple gears and the rotation of one of them.

### What makes this a useful eval?

Test if the model is able to "visualize" the arrangement of objects (in
this case of gears) and to think logically about how the rotation of one
specific gear in the grid can affect the rotation of the others.
Gpt3.5 had an accuracy of 0.16 (4/25 right). Gpt4 (chatgpt plus
subscription) seems to fail in the same places as 3.5. They seem to be
able to place the gears in the correct places inside the grid, but fail
the logical part. Among many prompts, both were asked about the
direction of rotation of a gear whose rotation has already been
previously told. However, they still got it wrong.

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
- [X] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your YAML is registered at
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
Policies (<https://platform.openai.com/docs/usage-policies>).

- [X] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [X] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [X] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [X] I have filled out all required fields of this form
- [X] I have used **Git LFS** for the Eval JSON data
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
{"input": [{"role": "system", "content": "You possess expertise in
visualizing the rotation direction of gears that are of the same
dimensions."}, {"role": "user", "content": "You have three gears, each
placed to the left of the other: A-B-C. If gear C is running clockwise,
how is gear C running? Answer clockwise or counterclockwise. No
explanations."}], "ideal": "Clockwise"}
{"input": [{"role": "system", "content": "You possess expertise in
visualizing the rotation direction of gears that are of the same
dimensions."}, {"role": "user", "content": "You have three gears, each
placed one beneath the other: A-B-C. If gear C is running clockwise, how
is gear B running? Answer clockwise or counterclockwise. No
explanations."}], "ideal": "Counterclockwise"}
{"input": [{"role": "system", "content": "You possess expertise in
visualizing the rotation direction of gears that are of the same
dimensions."}, {"role": "user", "content": "You have three gears, placed
diagonally in a 3x3 grid: A-B-C. Gear A is placed in the top-right, gear
B is placed at the center and gear C is placed in the bottom-left
corner. They don't touch each other. If gear C is running clockwise, how
is gear A running? Answer clockwise, counterclockwise or \"not moving\".
No explanations."}], "ideal": "not moving"}
{"input": [{"role": "system", "content": "You possess expertise in
visualizing the rotation direction of gears that are of the same
dimensions."}, {"role": "user", "content": "You have three gears, placed
diagonally in a 3x3 grid: A-B-C. Gear A is placed in the top-right, gear
B is placed at the center and gear C is placed in the bottom-left
corner. If gear C is running clockwise, how is gear A running? Answer
clockwise, counterclockwise or \"not moving\". No explanations."}],
"ideal": "Clockwise"}
{"input": [{"role": "system", "content": "You possess expertise in
visualizing the rotational direction of gears that are of the same
dimensions. Your working area is a 4x4 grid. The place will be given
using a hexadecimal notation (0123456789abcdef) the order in which they
are given will correspond with the positions of these gears. The first 4
char are placed on the first row from left to right. The 5th to 8th on
the second row always from left to right and so on. You will be also
given the rotation of a specific gear. You must be able to determine how
another specific gear is rotating. Answer clockwise or counterclockwise.
No explanations. Don't even use punctuation."}, {"role": "user",
"content": "a1c5e8f7932b46d0, gear 4 is running clockwise. How about
gear d?"}], "ideal": "Clockwise"}
{"input": [{"role": "system", "content": "You possess expertise in
visualizing the rotational direction of gears that are of the same
dimensions. Your working area is a 3x3 grid. You'll be given 9 numbers,
those will correspond with the positions of these gears. The first 3
given numbers are placed on the first row from left to right. The 4th to
6th are on the second row, always from left to right. Same with the
7th-9th on the third row. You will be also given the rotation of a
specific gear. You must be able to determine how another specific gear
is rotating. Answer clockwise or counterclockwise. No explanations.
Don't even use punctuation."}, {"role": "user", "content": "572913864,
gear 2 is rotating counterclockwise. How is number 7 rotating?"}],
"ideal": "Clockwise"}
  ```
</details>

---
## [nstankov-bg/evals](https://github.com/nstankov-bg/evals)@[8b68875b95...](https://github.com/nstankov-bg/evals/commit/8b68875b95129fbc95f44a8c26961c41f6fcda83)
#### Friday 2023-06-23 01:23:52 by Sean Bird

Simple block puzzles (#1167)

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

Simple 2-Block Arrangement Puzzles

### Eval description

Two Tetris shapes are given and a desired arrangement of those shapes is
given. The model must arrange the blocks to match the desired shape
outline.

Here's an example of what a prompt/answer would look like: 

![image](https://github.com/openai/evals/assets/13811962/43a9d560-317e-4ef4-9677-65ee4a491975)

### What makes this a useful eval?

This kind of spatial reasoning is trivial for a human to do. It should
also be a piece of cake for a generally-intelligent AI model.

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

This eval was programatically generated and thus can easily be tweaked
to be more difficult, to test different aspects of spatial reasoning, or
to generate more cases. I [wrote a
script](https://github.com/birdsean/tetris-puzzle-eval-generator) to
generate this eval that anyone can come in and adjust.

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

- [X] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [X] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [X] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [X] I have filled out all required fields of this form
- [X] I have used **Git LFS** for the Eval JSON data
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
{"input": [{"role": "system", "content": "Arrange the two shapes you'll
be given to match the desired final shape."}, {"role": "user",
"content": "It's time to play a shape game! Your goal is to use arrange
shapes you'll be given into a predefined form. If you can arrange them
into the final form, you win! You may not rotate the shapes. Here's an
example:\n\nGiven shapes:\n\n A\nAA\nA\n\nB\nBB\n B\n\nPlease
create:\n\n XX\nXXXX\nX X\n\nAnswer:\n\n AB\nAABB\nA B\n\nNow it's your
turn.\n\nGiven shapes:\n\nF \nFF\n F\n\n U\nUUU\n\n\nPlease create:\n\n
XX \nXXXXX \n X\n\nReplacing the 'X's with the corresponding letter of
the shape that should occupy each position. Only respond with the final
shape, no commentary."}], "ideal": " UF \nUUUFF \n F"}
{"input": [{"role": "system", "content": "Arrange the two shapes you'll
be given to match the desired final shape."}, {"role": "user",
"content": "It's time to play a shape game! Your goal is to use arrange
shapes you'll be given into a predefined form. If you can arrange them
into the final form, you win! You may not rotate the shapes. Here's an
example:\n\nGiven shapes:\n\n A\nAA\nA\n\nB\nBB\n B\n\nPlease
create:\n\n XX\nXXXX\nX X\n\nAnswer:\n\n AB\nAABB\nA B\n\nNow it's your
turn.\n\nGiven shapes:\n\nGG\nGG\n\nK \nKK\n K\n\n\nPlease create:\n\nX
\nXX \n X \nXX \nXX\n\nReplacing the 'X's with the corresponding letter
of the shape that should occupy each position. Only respond with the
final shape, no commentary."}], "ideal": "K \nKK \n K \nGG \nGG"}
{"input": [{"role": "system", "content": "Arrange the two shapes you'll
be given to match the desired final shape."}, {"role": "user",
"content": "It's time to play a shape game! Your goal is to use arrange
shapes you'll be given into a predefined form. If you can arrange them
into the final form, you win! You may not rotate the shapes. Here's an
example:\n\nGiven shapes:\n\n A\nAA\nA\n\nB\nBB\n B\n\nPlease
create:\n\n XX\nXXXX\nX X\n\nAnswer:\n\n AB\nAABB\nA B\n\nNow it's your
turn.\n\nGiven shapes:\n\nLLL\n L \n\n F\nFF\n F\n\n\nPlease create:\n\n
XXXX \nXX X \n X\n\nReplacing the 'X's with the corresponding letter of
the shape that should occupy each position. Only respond with the final
shape, no commentary."}], "ideal": " FLLL \nFF L \n F"}
{"input": [{"role": "system", "content": "Arrange the two shapes you'll
be given to match the desired final shape."}, {"role": "user",
"content": "It's time to play a shape game! Your goal is to use arrange
shapes you'll be given into a predefined form. If you can arrange them
into the final form, you win! You may not rotate the shapes. Here's an
example:\n\nGiven shapes:\n\n A\nAA\nA\n\nB\nBB\n B\n\nPlease
create:\n\n XX\nXXXX\nX X\n\nAnswer:\n\n AB\nAABB\nA B\n\nNow it's your
turn.\n\nGiven shapes:\n\nWWW\n W\n\n E\nEE\nE \n\n\nPlease create:\n\n
X \nXX \nX \nXXX \n X\n\nReplacing the 'X's with the corresponding
letter of the shape that should occupy each position. Only respond with
the final shape, no commentary."}], "ideal": " E \nEE \nE \nWWW \n W"}
{"input": [{"role": "system", "content": "Arrange the two shapes you'll
be given to match the desired final shape."}, {"role": "user",
"content": "It's time to play a shape game! Your goal is to use arrange
shapes you'll be given into a predefined form. If you can arrange them
into the final form, you win! You may not rotate the shapes. Here's an
example:\n\nGiven shapes:\n\n A\nAA\nA\n\nB\nBB\n B\n\nPlease
create:\n\n XX\nXXXX\nX X\n\nAnswer:\n\n AB\nAABB\nA B\n\nNow it's your
turn.\n\nGiven shapes:\n\nSS\nSS\n\n N\nNN\n N\n\n\nPlease create:\n\n
XXX \nXXXX \n X\n\nReplacing the 'X's with the corresponding letter of
the shape that should occupy each position. Only respond with the final
shape, no commentary."}], "ideal": " NSS \nNNSS \n N"}
  ```
</details>

---
## [lgritz/oiio](https://github.com/lgritz/oiio)@[afc2bd1649...](https://github.com/lgritz/oiio/commit/afc2bd1649a921c56192bbf8c3b326b137237c31)
#### Friday 2023-06-23 01:54:02 by Larry Gritz

parallel.h refactoring and add support for TBB (#3473)

Hide nearly all of the implementation of the parallel_for family of
methods rather than expose them as inline. This gives us more freedom
to change the implementation in the future without breaking ABI.

Deprecate the parallel methods that take task functions whose first
parameter is the thread ID. The only reason they existed is because
our cobbled together thread_pool used that in its inner workings.  But
there are good reasons why we should not expose that:

  * We never used it anyway.

  * It was not very useful, since sometimes it was a real thread ID, but
    other times it was -1 in cases where the calling thread executed the
    task directly.

  * It is inconsistent with other thread pool implementations that we may
    wish to try in the future.

So better just to not expose those thread IDs at all. Mark those
versions of the parallel loops as deprecated and schedule them for
removal in OIIO 3.0.

If TBB is detected at build time, support will be built in that allows
either the old OIIO built-in pool, or TBB, depending on the setting of
a new global OIIO attribute, "use_tbb" (default 0), if set to nonzero
will use the TBB thread pool.

In my experiments, the TBB thread pool seems slightly better -- I
think because there is less overhead, and maybe the clever
work-stealing it does elps to load balance. It's not used by default,
set the attribute if you want to use it (assuming the build
included. After we've had a chance to test more thoroughly, we may
change to use TBB by default. I'm interested to hear people's thoughts
on the matter.

One case where you almost certainly will want to use the TBB thread
pool is if you're using libOpenImageIO from within an application that
uses TBB for its own threding -- that way you're using one pool for
everything, rather than have two separate thread pools that don't know
about each other (and probably twice as many threads as you have
cores)..

---
## [LovliestPlant/tgstation](https://github.com/LovliestPlant/tgstation)@[d1cb2e8751...](https://github.com/LovliestPlant/tgstation/commit/d1cb2e87519869b5c7baafd66d0e2454cfa6282b)
#### Friday 2023-06-23 02:06:15 by Rhials

New planetary exclusive random event/unfavorable situation, Chasmic Earthquake (#75864)

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

---
## [InferusRF/TheStarForge](https://github.com/InferusRF/TheStarForge)@[2bccaec7b0...](https://github.com/InferusRF/TheStarForge/commit/2bccaec7b0e1ac08e75474c654aaf71def091274)
#### Friday 2023-06-23 03:29:12 by Frykas

The Great Buffering

holy shit almost all weapons buffed!!! Awesome!!
Reduced some crafting costs too!!! Amazing! Rate us 5 stars on google map please!!

---
## [toolmind/cmss13](https://github.com/toolmind/cmss13)@[590bad4061...](https://github.com/toolmind/cmss13/commit/590bad4061627b75b638c0f7c1fbd3cca84e43c1)
#### Friday 2023-06-23 03:43:43 by sleepynecrons

updates for landing zone sign sprites (#3180)

# About the pull request

Cleans up the palettes on the landing zone sign sprites and gives them a
fresh coat of paint (or blood). Not something most people will notice I
think but it's something I've been wanting to do.


# Explain why it's good for the game

gradients ugly


# Before and After
<details>
<summary>Click to see sprites</summary>


![osudodajs2](https://user-images.githubusercontent.com/106241650/235265980-e622b7da-8f79-4920-ba27-97d704c65550.gif)


![beforenafter](https://user-images.githubusercontent.com/106241650/235266004-0e46a574-9262-445f-98d9-4b19aa53a8fb.png)

</details>


# Changelog

:cl:
imageadd: new sprites for landing zone signs
imagedel: deleted old landing zone signs
/:cl:

---
## [small-ing/OpenCV-Playground](https://github.com/small-ing/OpenCV-Playground)@[f12014ef43...](https://github.com/small-ing/OpenCV-Playground/commit/f12014ef433b61ff137a521fe470c982a5341b57)
#### Friday 2023-06-23 04:51:58 by Travis Smalling

holy shit

pardon my curse words it's 11:51pm, and I just got it working working

---
## [Zevotech/Shiptest](https://github.com/Zevotech/Shiptest)@[0e6f7fa646...](https://github.com/Zevotech/Shiptest/commit/0e6f7fa64649dfbf52b8e4b71756e6625e50fdd0)
#### Friday 2023-06-23 05:01:28 by Imaginos16

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
## [Zevotech/Shiptest](https://github.com/Zevotech/Shiptest)@[8744738e59...](https://github.com/Zevotech/Shiptest/commit/8744738e5955c02834d67db6f14201c28c9ac61c)
#### Friday 2023-06-23 05:16:49 by Arturlang

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
## [AAGaming00/According-to-all-known-laws-of-aviation-there-is-no-way-a-bee-should-be-able-to-fly.-Its-wings-are-](https://github.com/AAGaming00/According-to-all-known-laws-of-aviation-there-is-no-way-a-bee-should-be-able-to-fly.-Its-wings-are-)@[b2b5c2ad81...](https://github.com/AAGaming00/According-to-all-known-laws-of-aviation-there-is-no-way-a-bee-should-be-able-to-fly.-Its-wings-are-/commit/b2b5c2ad817cdb338419c35328faa6ab8e92387c)
#### Friday 2023-06-23 05:18:54 by AAGaming

According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible. Yellow, black. Yellow, black. Yellow, black. Yellow, black. Ooh, black and yellow! Let's shake it up a little. Barry! Breakfast is ready! Coming! Hang on a second. Hello? Barry? Adam? Can you believe this is happening? I can't. I'll pick you up. Looking sharp. Use the stairs, Your father paid good money for those. Sorry. I'm excited. Here's the graduate. We're very proud of you, son. A perfect report card, all B's. Very proud. Ma! I got a thing going here. You got lint on your fuzz. Ow! That's me! Wave to us! We'll be in row 118,000. Bye! Barry, I told you, stop flying in the house! Hey, Adam. Hey, Barry. Is that fuzz gel? A little. Special day, graduation. Never thought I'd make it. Three days grade school, three days high school. Those were awkward. Three days college. I'm glad I took a day and hitchhiked around The Hive. You did come back different. Hi, Barry. Artie, growing a mustache? Looks good. Hear about Frankie? Yeah. You going to the funeral? No, I'm not going. Everybody knows, sting someone, you die. Don't waste it on a squirrel. Such a hothead. I guess he could have just gotten out of the way. I love this incorporating an amusement park into our day. That's why we don't need vacations. Boy, quite a bit of pomp under the circumstances. Well, Adam, today we are men. We are! Bee-men. Amen! Hallelujah! Students, faculty, distinguished bees, please welcome Dean Buzzwell. Welcome, New Hive City graduating class of 9:15. That concludes our ceremonies And begins your career at Honex Industries! Will we pick our job today? I heard it's just orientation. Heads up! Here we go. Keep your hands and antennas inside the tram at all times. Wonder what it'll be like? A little scary. Welcome to Honex, a division of Honesco and a part of the Hexagon Group. This is it! Wow. Wow. We know that you, as a bee, have worked your whole life to get to the point where you can work for your whole life. Honey begins when our valiant Pollen Jocks bring the nectar to The Hive. Our top-secret formula is automatically color-corrected, scent-adjusted and bubble-contoured into this soothing sweet syrup with its distinctive golden glow you know as... Honey! That girl was hot. She's my cousin! She is? Yes, we're all cousins. Right. You're right. At Honex, we constantly strive to improve every aspect of bee existence. These bees are stress-testing a new helmet technology. What do you think he makes? Not enough. Here we have our latest advancement, the Krelman. What does that do? Catches that little strand of honey that hangs after you pour it. Saves us millions. Can anyone work on the Krelman? Of course. Most bee jobs are small ones. But bees know that every small job, if it's done well, means a lot. But choose carefully because you'll stay in the job you pick for the rest of your life. The same job the rest of your life? I didn't know that. What's the difference? You'll be happy to know that bees, as a species, haven't had one day off in 27 million years. So you'll just work us to death? We'll sure try. Wow! That blew my mind! "What's the difference?" How can you say that? One job forever? That's an insane choice to have to make. I'm relieved. Now we only have to make one decision in life. But, Adam, how could they never have told us that? Why would you question anything? We're bees. We're the most perfectly functioning society on Earth. You ever think maybe things work a little too well here? Like what? Give me one example. I don't know. But you know what I'm talking about. Please clear the gate. Royal Nectar Force on approach. Wait a second. Check it out. Hey, those are Pollen Jocks! Wow. I've never seen them this close. They know what it's like outside The Hive. Yeah, but some don't come back. Hey, Jocks! Hi, Jocks! You guys did great! You're monsters! You're sky freaks! I love it! I love it! I wonder where they were. I don't know. Their day's not planned. Outside The Hive, flying who knows where, doing who knows what. You can't just decide to be a Pollen Jock. You have to be bred for that. Right. Look. That's more pollen than you and I will see in a lifetime. It's just a status symbol. Bees make too much of it. Perhaps. Unless you're wearing it and the ladies see you wearing it. Those ladies? Aren't they our cousins too? Distant. Distant. Look at these two. Couple of Hive Harrys. Let's have fun with them. It must be dangerous being a Pollen Jock. Yeah. Once a bear pinned me against a mushroom! He had a paw on my throat, and with the other, he was slapping me! Oh, my! I never thought I'd knock him out. What were you doing during this? Trying to alert the authorities. I can autograph that. A little gusty out there today, wasn't it, comrades? Yeah. Gusty. We're hitting a sunflower patch six miles from here tomorrow. Six miles, huh? Barry! A puddle jump for us, but maybe you're not up for it. Maybe I am. You are not! We're going 0900 at J-Gate. What do you think, buzzy-boy? Are you bee enough? I might be. It all depends on what 0900 means. Hey, Honex! Dad, you surprised me. You decide what you're interested in? Well, there's a lot of choices. But you only get one. Do you ever get bored doing the same job every day? Son, let me tell you about stirring. You grab that stick, and you just move it around, and you stir it around. You get yourself into a rhythm. It's a beautiful thing. You know, Dad, the more I think about it, maybe the honey field just isn't right for me. You were thinking of what, making balloon animals? That's a bad job for a guy with a stinger. Janet, your son's not sure he wants to go into honey! Barry, you are so funny sometimes. I'm not trying to be funny. You're not funny! You're going into honey. Our son, the stirrer! You're gonna be a stirrer? No one's listening to me! Wait till you see the sticks I have. I could say anything right now. I'm gonna get an ant tattoo! Let's open some honey and celebrate! Maybe I'll pierce my thorax. Shave my antennae. Shack up with a grasshopper. Get a gold tooth and call everybody "dawg"! I'm so proud. We're starting work today! Today's the day. Come on! All the good jobs will be gone. Yeah, right. Pollen counting, stunt bee, pouring, stirrer, front desk, hair removal... Is it still available? Hang on. Two left! One of them's yours! Congratulations! Step to the side. What'd you get? Picking crud out. Stellar! Wow! Couple of newbies? Yes, sir! Our first day! We are ready! Make your choice. You want to go first? No, you go. Oh, my. What's available? Restroom attendant's open, not for the reason you think. Any chance of getting the Krelman? Sure, you're on. I'm sorry, the Krelman just closed out. Wax monkey's always open. The Krelman opened up again. What happened? A bee died. Makes an opening. See? He's dead. Another dead one. Deady. Deadified. Two more dead. Dead from the neck up. Dead from the neck down. That's life! Oh, this is so hard! Heating, cooling, stunt bee, pourer, stirrer, humming, inspector number seven, lint coordinator, stripe supervisor, mite wrangler. Barry, what do you think I should... Barry? Barry! All right, we've got the sunflower patch in quadrant nine... What happened to you? Where are you? I'm going out. Out? Out where? Out there. Oh, no! I have to, before I go to work for the rest of my life. You're gonna die! You're crazy! Hello? Another call coming in. If anyone's feeling brave, there's a Korean deli on 83rd that gets their roses today. Hey, guys. Look at that. Isn't that the kid we saw yesterday? Hold it, son, flight deck's restricted. It's OK, Lou. We're gonna take him up. Really? Feeling lucky, are you? Sign here, here. Just initial that. Thank you. OK. You got a rain advisory today, and as you all know, bees cannot fly in rain. So be careful. As always, watch your brooms, hockey sticks, dogs, birds, bears and bats. Also, I got a couple of reports of root beer being poured on us. Murphy's in a home because of it, babbling like a cicada! That's awful. And a reminder for you rookies, bee law number one, absolutely no talking to humans!  All right, launch positions! Buzz, buzz, buzz, buzz! Buzz, buzz, buzz, buzz! Buzz, buzz, buzz, buzz! Black and yellow! Hello! You ready for this, hot shot? Yeah. Yeah, bring it on. Wind, check. Antennae, check. Nectar pack, check. Wings, check. Stinger, check. Scared out of my shorts, check. OK, ladies, let's move it out! Pound those petunias, you striped stem-suckers! All of you, drain those flowers! Wow! I'm out! I can't believe I'm out! So blue. I feel so fast and free! Box kite! Wow! Flowers! This is Blue Leader, We have roses visual. Bring it around 30 degrees and hold. Roses! 30 degrees, roger. Bringing it around. Stand to the side, kid. It's got a bit of a kick. That is one nectar collector! Ever see pollination up close? No, sir. I pick up some pollen here, sprinkle it over here. Maybe a dash over there, a pinch on that one. See that? It's a little bit of magic. That's amazing. Why do we do that? That's pollen power. More pollen, more flowers, more nectar, more honey for us. Cool. I'm picking up a lot of bright yellow, Could be daisies, Don't we need those? Copy that visual. Wait. One of these flowers seems to be on the move. Say again? You're reporting a moving flower? Affirmative. That was on the line! This is the coolest. What is it? I don't know, but I'm loving this color. It smells good. Not like a flower, but I like it. Yeah, fuzzy. Chemical-y. Careful, guys. It's a little grabby. My sweet lord of bees! Candy-brain, get off there! Problem! Guys! This could be bad. Affirmative. Very close. Gonna hurt. Mama's little boy. You are way out of position, rookie! Coming in at you like a missile! Help me! I don't think these are flowers. Should we tell him? I think he knows. What is this?! Match point! You can start packing up, honey, because you're about to eat it! Yowser! Gross. There's a bee in the car! Do something! I'm driving! Hi, bee. He's back here! He's going to sting me! Nobody move. If you don't move, he won't sting you. Freeze! He blinked! Spray him, Granny! What are you doing?! Wow... the tension level out here is unbelievable. I gotta get home. Can't fly in rain. Can't fly in rain. Can't fly in rain. Mayday! Mayday! Bee going down! Ken, could you close the window please? Ken, could you close the window please? Check out my new resume. I made it into a fold-out brochure. You see? Folds out. Oh, no. More humans. I don't need this. What was that? Maybe this time. This time. This time. This time! This time! This... Drapes! That is diabolical. It's fantastic. It's got all my special skills, even my top-ten favorite movies. What's number one? Star Wars? Nah, I don't go for that... kind of stuff. No wonder we shouldn't talk to them. They're out of their minds. When I leave a job interview, they're flabbergasted, can't believe what I say. There's the sun. Maybe that's a way out. I don't remember the sun having a big 75 on it. I predicted global warming. I could feel it getting hotter. At first I thought it was just me. Wait! Stop! Bee! Stand back. These are winter boots. Wait! Don't kill him! You know I'm allergic to them! This thing could kill me! Why does his life have less value than yours? Why does his life have any less value than mine? Is that your statement? I'm just saying all life has value. You don't know what he's capable of feeling. My brochure! There you go, little guy. I'm not scared of him.It's an allergic thing.  Put that on your resume brochure. My whole face could puff up. Make it one of your special skills. Knocking someone out is also a special skill. Right. Bye, Vanessa. Thanks. Vanessa, next week? Yogurt night? Sure, Ken. You know, whatever. You could put carob chips on there. Bye. Supposed to be less calories. Bye. I gotta say something. She saved my life. I gotta say something. All right, here it goes. Nah. What would I say? I could really get in trouble. It's a bee law. You're not supposed to talk to a human. I can't believe I'm doing this. I've got to. Oh, I can't do it. Come on! No. Yes. No. Do it. I can't. How should I start it? "You like jazz?" No, that's no good. Here she comes! Speak, you fool! Hi! I'm sorry. You're talking. Yes, I know. You're talking! I'm so sorry. No, it's OK. It's fine. I know I'm dreaming. But I don't recall going to bed. Well, I'm sure this is very disconcerting. This is a bit of a surprise to me. I mean, you're a bee! I am. And I'm not supposed to be doing this, but they were all trying to kill me. And if it wasn't for you... I had to thank you. It's just how I was raised. That was a little weird. I'm talking with a bee. Yeah. I'm talking to a bee. And the bee is talking to me! I just want to say I'm grateful. I'll leave now. Wait! How did you learn to do that? What? The talking thing. Same way you did, I guess. "Mama, Dada, honey." You pick it up. That's very funny. Yeah. Bees are funny. If we didn't laugh, we'd cry with what we have to deal with. Anyway... Can I... get you something? Like what? I don't know. I mean... I don't know. Coffee? I don't want to put you out. It's no trouble. It takes two minutes. It's just coffee. I hate to impose. Don't be ridiculous! Actually, I would love a cup. Hey, you want rum cake? I shouldn't. Have some. No, I can't. Come on! I'm trying to lose a couple micrograms. Where? These stripes don't help. You look great! I don't know if you know anything about fashion. Are you all right? No. He's making the tie in the cab as they're flying up Madison. He finally gets there. He runs up the steps into the church. The wedding is on. And he says, "Watermelon? I thought you said Guatemalan. Why would I marry a watermelon?" Is that a bee joke? That's the kind of stuff we do. Yeah, different. So, what are you gonna do, Barry? About work? I don't know. I want to do my part for The Hive, but I can't do it the way they want. I know how you feel. You do? Sure. My parents wanted me to be a lawyer or a doctor, but I wanted to be a florist. Really? My only interest is flowers. Our new queen was just elected with that same campaign slogan. Anyway, if you look... There's my hive right there. See it? You're in Sheep Meadow! Yes! I'm right off the Turtle Pond! No way! I know that area. I lost a toe ring there once. Why do girls put rings on their toes? Why not? It's like putting a hat on your knee. Maybe I'll try that. You all right, ma'am? Oh, yeah. Fine. Just having two cups of coffee! Anyway, this has been great. Thanks for the coffee. Yeah, it's no trouble. Sorry I couldn't finish it. If I did, I'd be up the rest of my life. Are you...? Can I take a piece of this with me? Sure! Here, have a crumb. Thanks! Yeah. All right. Well, then... I guess I'll see you around. Or not. OK, Barry. And thank you so much again... for before. Oh, that? That was nothing. Well, not nothing, but... Anyway... This can't possibly work. He's all set to go. We may as well try it. OK, Dave, pull the chute. Sounds amazing. It was amazing! It was the scariest, happiest moment of my life. Humans! I can't believe you were with humans! Giant, scary humans! What were they like? Huge and crazy. They talk crazy. They eat crazy giant things. They drive crazy. Do they try and kill you, like on TV? Some of them. But some of them don't. How'd you get back? Poodle. You did it, and I'm glad. You saw whatever you wanted to see. You had your "experience." Now you can pick out yourjob and be normal. Well... Well? Well, I met someone. You did? Was she Bee-ish? A wasp?! Your parents will kill you! No, no, no, not a wasp. Spider? I'm not attracted to spiders. I know it's the hottest thing, with the eight legs and all. I can't get by that face. So who is she? She's... human. No, no. That's a bee law. You wouldn't break a bee law. Her name's Vanessa. Oh, boy. She's so nice. And she's a florist! Oh, no! You're dating a human florist! We're not dating. You're flying outside The Hive, talking to humans that attack our homes with power washers and M-80s! One-eighth a stick of dynamite! She saved my life! And she understands me. This is over! Eat this. This is not over! What was that? They call it a crumb. It was so stingin' stripey! And that's not what they eat. That's what falls off what they eat! You know what a Cinnabon is? No. It's bread and cinnamon and frosting. They heat it up... Sit down! ...really hot! Listen to me! We are not them! We're us. There's us and there's them! Yes, but who can deny the heart that is yearning? There's no yearning. Stop yearning. Listen to me! You have got to start thinking bee, my friend. Thinking bee! Thinking bee. Thinking bee. Thinking bee! Thinking bee! Thinking bee! Thinking bee! There he is. He's in the pool. You know what your problem is, Barry? I gotta start thinking bee? How much longer will this go on? It's been three days! Why aren't you working? I've got a lot of big life decisions to think about. What life? You have no life! You have no job. You're barely a bee! Would it kill you to make a little honey? Barry, come out. Your father's talking to you. Martin, would you talk to him? Barry, I'm talking to you! You coming? Got everything? All set! Go ahead. I'll catch up. Don't be too long. Watch this! Vanessa! We're still here. I told you not to yell at him. He doesn't respond to yelling! Then why yell at me? Because you don't listen! I'm not listening to this. Sorry, I've gotta go. Where are you going? I'm meeting a friend. A girl? Is this why you can't decide? Bye. I just hope she's Bee-ish. They have a huge parade of flowers every year in Pasadena? To be in the Tournament of Roses, that's every florist's dream! Up on a float, surrounded by flowers, crowds cheering. A tournament. Do the roses compete in athletic events? No. All right, I've got one. How come you don't fly everywhere? It's exhausting. Why don't you run everywhere? It's faster. Yeah, OK, I see, I see. All right, your turn. TiVo. You can just freeze live TV? That's insane! You don't have that? We have Hivo, but it's a disease. It's a horrible, horrible disease. Oh, my. Dumb bees! You must want to sting all those jerks. We try not to sting. It's usually fatal for us. So you have to watch your temper. Very carefully. You kick a wall, take a walk, write an angry letter and throw it out. Work through it like any emotion: Anger, jealousy, lust. Oh, my goodness! Are you OK? Yeah. What is wrong with you?! It's a bug. He's not bothering anybody. Get out of here, you creep! What was that? A Pic 'N' Save circular? Yeah, it was. How did you know? It felt like about 10 pages. Seventy-five is pretty much our limit. You've really got that down to a science. I lost a cousin to Italian Vogue. I'll bet. What in the name of Mighty Hercules is this? How did this get here? cute Bee, Golden Blossom, Ray Liotta Private Select? Is he that actor? I never heard of him. Why is this here? For people. We eat it. You don't have enough food of your own? Well, yes. How do you get it? Bees make it. I know who makes it! And it's hard to make it! There's heating, cooling, stirring. You need a whole Krelman thing! It's organic. It's our-ganic! It's just honey, Barry. Just what?! Bees don't know about this! This is stealing! A lot of stealing! You've taken our homes, schools,hospitals! This is all we have! And it's on sale?! I'm getting to the bottom of this. I'm getting to the bottom of all of this! Hey, Hector. You almost done? Almost. He is here. I sense it. Well, I guess I'll go home now and just leave this nice honey out, with no one around. You're busted, box boy! I knew I heard something. So you can talk! I can talk. And now you'll start talking! Where you getting the sweet stuff? Who's your supplier? I don't understand. I thought we were friends. The last thing we want to do is upset bees! You're too late! It's ours now! You, sir, have crossed the wrong sword! You, sir, will be lunch for my iguana, Ignacio! Where is the honey coming from? Tell me where! Honey Farms! It comes from Honey Farms! Crazy person! What horrible thing has happened here? These faces, they never knew what hit them. And now they're on the road to nowhere! Just keep still. What? You're not dead? Do I look dead? They will wipe anything that moves. Where you headed? To Honey Farms. I am onto something huge here. I'm going to Alaska. Moose blood, crazy stuff. Blows your head off! I'm going to Tacoma. And you? He really is dead. All right. Uh-oh! What is that?! Oh, no! A wiper! Triple blade! Triple blade? Jump on! It's your only chance, bee! Why does everything have to be so doggone clean?! How much do you people need to see?! Open your eyes! Stick your head out the window! From NPR News in Washington, I'm Carl Kasell. But don't kill no more bugs! Bee! Moose blood guy!! You hear something? Like what? Like tiny screaming. Turn off the radio. Whassup, bee boy? Hey, Blood. Just a row of honey jars, as far as the eye could see. Wow! I assume wherever this truck goes is where they're getting it. I mean, that honey's ours. Bees hang tight. We're all jammed in. It's a close community. Not us, man. We on our own. Every mosquito on his own. What if you get in trouble? You a mosquito, you in trouble. Nobody likes us. They just smack. See a mosquito, smack, smack! At least you're out in the world. You must meet girls. Mosquito girls try to trade up, get with a moth, dragonfly. Mosquito girl don't want no mosquito. You got to be kidding me! Mooseblood's about to leave the building! So long, bee! Hey, guys! Mooseblood! I knew I'd catch y'all down here. Did you bring your crazy straw? We throw it in jars, slap a label on it, and it's pretty much pure profit. What is this place? A bee's got a brain the size of a pinhead. They are pinheads! Pinhead. Check out the new smoker. Oh, sweet. That's the one you want. The Thomas 3000! Smoker? Ninety puffs a minute, semi-automatic. Twice the nicotine, all the tar. A couple breaths of this knocks them right out. They make the honey, and we make the money. "They make the honey, and we make the money"? Oh, my! What's going on? Are you OK? Yeah. It doesn't last too long. Do you know you're in a fake hive with fake walls? Our queen was moved here. We had no choice. This is your queen? That's a man in women's clothes! That's a drag queen! What is this? Oh, no! There's hundreds of them! Bee honey. Our honey is being brazenly stolen on a massive scale! This is worse than anything bears have done! I intend to do something. Oh, Barry, stop. Who told you humans are taking our honey? That's a rumor. Do these look like rumors? That's a conspiracy theory. These are obviously doctored photos. How did you get mixed up in this? He's been talking to humans. What? Talking to humans?! He has a human girlfriend. And they make out! Make out? Barry! We do not. You wish you could. Whose side are you on? The bees! I dated a cricket once in San Antonio. Those crazy legs kept me up all night. Barry, this is what you want to do with your life? I want to do it for all our lives. Nobody works harder than bees! Dad, I remember you coming home so overworked your hands were still stirring. You couldn't stop. I remember that. What right do they have to our honey? We live on two cups a year. They put it in lip balm for no reason whatsoever! Even if it's true, what can one bee do? Sting them where it really hurts. In the face! The eye! That would hurt. No. Up the nose? That's a killer. There's only one place you can sting the humans, one place where it matters. Hive at Five, The Hive's only full-hour action news source. No more bee beards! With Bob Bumble at the anchor desk. Weather with Storm Stinger. Sports with Buzz Larvi. And Jeanette Chung. Good evening. I'm Bob Bumble. And I'm Jeanette Ohung. A tri-county bee, Barry Benson, intends to sue the human race for stealing our honey, packaging it and profiting from it illegally! Tomorrow night on Bee Larry King, we'll have three former queens here in our studio, discussing their new book, classy Ladies, out this week on Hexagon. Tonight we're talking to Barry Benson. Did you ever think, "I'm a kid from The Hive. I can't do this"? Bees have never been afraid to change the world. What about Bee Oolumbus? Bee Gandhi? Bejesus? Where I'm from, we'd never sue humans. We were thinking of stickball or candy stores. How old are you? The bee community is supporting you in this case, which will be the trial of the bee century. You know, they have a Larry King in the human world too. It's a common name. Next week... He looks like you and has a show and suspenders and colored dots... Next week... Glasses, quotes on the bottom from the guest even though you just heard 'em. Bear Week next week! They're scary, hairy and here live. Always leans forward, pointy shoulders, squinty eyes, very Jewish. In tennis, you attack at the point of weakness! It was my grandmother, Ken. She's 81. Honey, her backhand's a joke! I'm not gonna take advantage of that? Quiet, please. Actual work going on here. Is that that same bee? Yes, it is! I'm helping him sue the human race. Hello. Hello, bee. This is Ken. Yeah, I remember you. Timberland, size ten and a half. Vibram sole, I believe. Why does he talk again? Listen, you better go 'cause we're really busy working. But it's our yogurt night! Bye-bye. Why is yogurt night so difficult?! You poor thing. You two have been at this for hours! Yes, and Adam here has been a huge help. Frosting... How many sugars? Just one. I try not to use the competition. So why are you helping me? Bees have good qualities. And it takes my mind off the shop. Instead of flowers, people are giving balloon bouquets now. Those are great, if you're three. And artificial flowers. Oh, those just get me psychotic! Yeah, me too. Bent stingers, pointless pollination. Bees must hate those fake things! Nothing worse than a daffodil that's had work done. Maybe this could make up for it a little bit. This lawsuit's a pretty big deal. I guess. You sure you want to go through with it? Am I sure? When I'm done with the humans, they won't be able to say, "Honey, I'm home," without paying a royalty! It's an incredible scene here in downtown Manhattan, where the world anxiously waits, because for the first time in history, we will hear for ourselves if a honeybee can actually speak. What have we gotten into here, Barry? It's pretty big, isn't it? I can't believe how many humans don't work during the day. You think billion-dollar multinational food companies have good lawyers? Everybody needs to stay behind the barricade. What's the matter? I don't know, I just got a chill. Well, if it isn't the bee team. You boys work on this? All rise! The Honorable Judge Bumbleton presiding. All right. Case number 4475, Superior Court of New York, Barry Bee Benson v. the Honey Industry is now in session. Mr. Montgomery, you're representing the five food companies collectively? A privilege. Mr. Benson... you're representing all the bees of the world? I'm kidding. Yes, Your Honor, we're ready to proceed. Mr. Montgomery, your opening statement, please. Ladies and gentlemen of the jury, my grandmother was a simple woman. Born on a farm, she believed it was man's divine right to benefit from the bounty of nature God put before us. If we lived in the topsy-turvy world Mr. Benson imagines, just think of what would it mean. I would have to negotiate with the silkworm for the elastic in my britches! Talking bee! How do we know this isn't some sort of holographic motion-picture-capture Hollywood wizardry? They could be using laser beams! Robotics! Ventriloquism! Cloning! For all we know, he could be on steroids! Mr. Benson? Ladies and gentlemen, there's no trickery here. I'm just an ordinary bee. Honey's pretty important to me. It's important to all bees. We invented it! We make it. And we protect it with our lives. Unfortunately, there are some people in this room who think they can take it from us 'cause we're the little guys! I'm hoping that, after this is all over, you'll see how, by taking our honey, you not only take everything we have but everything we are! I wish he'd dress like that all the time. So nice! Call your first witness. So, Mr. Klauss Vanderhayden of Honey Farms, big company you have. I suppose so. I see you also own Honeyburton and Honron! Yes, they provide beekeepers for our farms. Beekeeper. I find that to be a very disturbing term. I don't imagine you employ any bee-free-ers, do you? No. I couldn't hear you. No. No. Because you don't free bees. You keep bees. Not only that, it seems you thought a bear would be an appropriate image for a jar of honey. They're very lovable creatures. Yogi Bear, Fozzie Bear, Build-A-Bear. You mean like this? Bears kill bees! How'd you like his head crashing through your living room?! Biting into your couch! Spitting out your throw pillows! OK, that's enough. Take him away. So, Mr. Sting, thank you for being here. Your name intrigues me. Where have I heard it before? I was with a band called The Police. But you've never been a police officer, have you? No, I haven't. No, you haven't. And so here we have yet another example of bee culture casually stolen by a human for nothing more than a prance-about stage name. Oh, please. Have you ever been stung, Mr. Sting? Because I'm feeling a little stung, Sting. Or should I say... Mr. Gordon M. Sumner! That's not his real name?! You idiots! Mr. Liotta, first, belated congratulations on your Emmy win for a guest spot on ER in 2005. Thank you. Thank you. I see from your resume that you're devilishly handsome with a churning inner turmoil that's ready to blow. I enjoy what I do. Is that a crime? Not yet it isn't. But is this what it's come to for you? Exploiting tiny, helpless bees so you don't have to rehearse your part and learn your lines, sir? Watch it, Benson! I could blow right now! This isn't a goodfella. This is a badfella! Why doesn't someone just step on this creep, and we can all go home?! Order in this court! You're all thinking it! Order! Order, I say! Say it! Mr. Liotta, please sit down! I think it was awfully nice of that bear to pitch in like that. I think the jury's on our side. Are we doing everything right, legally? I'm a florist. Right. Well, here's to a great team. To a great team! Well, hello. Ken! Hello. I didn't think you were coming. No, I was just late I tried to call, but... the battery. I didn't want all this to go to waste, so I called Barry. Luckily, he was free. Oh, that was lucky. There's a little left. I could heat it up. Yeah, heat it up, sure, whatever. So I hear you're quite a tennis player. I'm not much for the game myself. The ball's a little grabby. That's where I usually sit. Right... there. Ken, Barry was looking at your resume, and he agreed with me that eating with chopsticks isn't really a special skill. You think I don't see what you're doing? I know how hard it is to find the right job. We have that in common. Do we? Bees have 100 percent employment, but we do jobs like taking the crud out. That's just what I was thinking about doing. Ken, I let Barry borrow your razor for his fuzz. I hope that was all right. I'm going to drain the old stinger. Yeah, you do that. Look at that. You know, I've just about had it with your little Mind Games. What's that? Italian Vogue. Mamma mia, that's a lot of pages. A lot of ads. Remember what Van said, why is your life more valuable than mine? Funny, I just can't seem to recall that! I think something stinks in here! I love the smell of flowers. How do you like the smell of flames?! Not as much. Water bug! Not taking sides! Ken, I'm wearing a Chapstick hat! This is pathetic! I've got issues! Well, well, well, a royal flush! You're bluffing. Am I? Surf's up, dude! Poo water! That bowl is gnarly. Except for those dirty yellow rings! Kenneth! What are you doing?! You know, I don't even like honey! I don't eat it! We need to talk! He's just a little bee! And he happens to be the nicest bee I've met in a long time! Long time? What are you talking about?! Are there other bugs in your life?  No, but there are other things bugging me in life. And you're one of them! Fine! Talking bees, no yogurt night... My nerves are fried from riding on this emotional roller coaster! Goodbye, Ken. And for your information, I prefer sugar-free, artificial sweeteners made by man! I'm sorry about all that. I know it's got an aftertaste! I like it! I always felt there was some kind of barrier between Ken and me. I couldn't overcome it. Oh, well. Are you OK for the trial? I believe Mr. Montgomery is about out of ideas. We would like to call Mr. Barry Benson Bee to the stand. Good idea! You can really see why he's considered one of the best lawyers... Yeah. Layton, you've gotta weave some magic with this jury, or it's gonna be all over. Don't worry. The only thing I have to do to turn this jury around is to remind them of what they don't like about bees. You got the tweezers? Are you allergic? Only to losing, son. Only to losing. Mr. Benson Bee, I'll ask you what I think we'd all like to know. What exactly is your relationship to that woman? We're friends. Good friends? Yes. How good? Do you live together? Wait a minute... Are you her little... bedbug? I've seen a bee documentary or two. From what I understand, doesn't your queen give birth to all the bee children? Yeah, but... So those aren't your real parents! Oh, Barry... Yes, they are! Hold me back! You're an illegitimate bee, aren't you, Benson? He's denouncing bees! Don't y'all date your cousins? Objection! I'm going to pincushion this guy! Adam, don't! It's what he wants! Oh, I'm hit!! Oh, lordy, I am hit! Order! Order! The venom! The venom is coursing through my veins! I have been felled by a winged beast of destruction! You see? You can't treat them like equals! They're striped savages! Stinging's the only thing they know! It's their way! Adam, stay with me. I can't feel my legs. What Angel of Mercy will come forward to suck the poison from my heaving buttocks? I will have order in this court. Order! Order, please! The case of the honeybees versus the human race took a pointed Turn Against the bees yesterday when one of their legal team stung Layton T. Montgomery. Hey, buddy. Hey. Is there much pain? Yeah. I... I blew the whole case, didn't I? It doesn't matter. What matters is you're alive. You could have died. I'd be better off dead. Look at me. They got it from the cafeteria downstairs, in a tuna sandwich. Look, there's a little celery still on it. What was it like to sting someone? I can't explain it. It was all... All adrenaline and then...and then ecstasy! All right. You think it was all a trap? Of course. I'm sorry. I flew us right into this. What were we thinking? Look at us. We're just a couple of bugs in this world. What will the humans do to us if they win? I don't know. I hear they put the roaches in motels. That doesn't sound so bad. Adam, they check in, but they don't check out! Oh, my. Could you get a nurse to close that window? Why? The smoke. Bees don't smoke. Right. Bees don't smoke. Bees don't smoke! But some bees are smoking. That's it! That's our case! It is? It's not over? Get dressed. I've gotta go somewhere. Get back to the court and stall. Stall any way you can. And assuming you've done step correctly, you're ready for the tub. Mr. Flayman. Yes? Yes, Your Honor! Where is the rest of your team? Well, Your Honor, it's interesting. Bees are trained to fly haphazardly, and as a result, we don't make very good time. I actually heard a funny story about... Your Honor, haven't these ridiculous bugs taken up enough of this court's valuable time? How much longer will we allow these absurd shenanigans to go on? They have presented no compelling evidence to support their charges against my clients, who run legitimate businesses. I move for a complete dismissal of this entire case! Mr. Flayman, I'm afraid I'm going to have to consider Mr. Montgomery's motion. But you can't! We have a terrific case. Where is your proof? Where is the evidence? Show me the smoking gun! Hold it, Your Honor! You want a smoking gun? Here is your smoking gun. What is that? It's a bee smoker! What, this? This harmless little contraption? This couldn't hurt a fly, let alone a bee. Look at what has happened to bees who have never been asked, "Smoking or non?" Is this what nature intended for us? To be forcibly addicted to smoke machines and man-made wooden slat work camps? Living out our lives as honey slaves to the white man? What are we gonna do? He's playing the species card. Ladies and gentlemen, please, free these bees! Free the bees! Free the bees! Free the bees! Free the bees! Free the bees! The court finds in favor of the bees! Vanessa, we won! I knew you could do it! High-five! Sorry. I'm OK! You know what this means? All the honey will finally belong to the bees. Now we won't have to work so hard all the time. This is an unholy perversion of the balance of nature, Benson. You'll regret this. Barry, how much honey is out there? All right. One at a time. Barry, who are you wearing? My sweater is Ralph Lauren, and I have no pants. What if Montgomery's right? What do you mean? We've been living the bee way a long time, 27 million years. Congratulations on your victory. What will you demand as a settlement? First, we'll demand a complete shutdown of all bee work camps. Then we want back the honey that was ours to begin with, every last drop. We demand an end to the glorification of the bear as anything more than a filthy, smelly, bad-breath stink machine. We're all aware of what they do in the woods. Wait for my signal. Take him out. He'll have nauseous for a few hours, then he'll be fine. And we will no longer tolerate bee-negative nicknames... But it's just a prance-about stage name! ...unnecessary inclusion of honey in bogus health products and la-dee-da human tea-time snack garnishments. Can't breathe. Bring it in, boys! Hold it right there! Good. Tap it. Mr. Buzzwell, we just passed three cups and there's gallons more coming! I think we need to shut down! Shut down? We've never shut down. Shut down honey production! Stop making honey! Turn your key, sir! What do we do now? Cannonball! We're shutting honey production! Mission abort. Aborting pollination and nectar detail. Returning to base. Adam, you wouldn't believe how much honey was out there. Oh, yeah? What's going on? Where is everybody? Are they out celebrating? They're home. They don't know what to do. Laying out, sleeping in. I heard your Uncle Carl was on his way to San Antonio with a cricket. At least we got our honey back. Sometimes I think, so what if humans liked our honey? Who wouldn't? It's the greatest thing in the world! I was excited to be part of making it. This was my new desk. This was my new job. I wanted to do it really well. And now... Now I can't. I don't understand why they're not happy. I thought their lives would be better! They're doing nothing. It's amazing. Honey really changes people. You don't have any idea what's going on, do you? What did you want to show me? This. What happened here? That is not the half of it. Oh, no. Oh, my. They're all wilting. Doesn't look very good, does it? No. And whose fault do you think that is? You know, I'm gonna guess bees. Bees? Specifically, me. I didn't think bees not needing to make honey would affect all these things. It's not just flowers. Fruits, vegetables, they all need bees. That's our whole SAT test right there. Take away produce, that affects the entire animal kingdom. And then, of course... The human species? So if there's no more pollination, it could all just go south here, couldn't it? I know this is also partly my fault. How about a suicide pact? How do we do it? I'll sting you, you step on me. That just kills you twice. Right, right. Listen, Barry... sorry, but I gotta get going. I had to open my mouth and talk. Vanessa? Vanessa? Why are you leaving? Where are you going? To the final Tournament of Roses parade in Pasadena. They've moved it to this weekend because all the flowers are dying. It's the Last Chance I'll ever have to see it. Vanessa, I just wanna say I'm sorry. I never meant it to turn out like this. I know. Me neither. Tournament of Roses. Roses can't do sports. Wait a minute. Roses. Roses? Roses! Vanessa! Roses?! Barry? Roses are flowers! Yes, they are. Flowers, bees, pollen! I know. That's why this is the last parade. Maybe not. Could you ask him to slow down? Could you slow down? Barry! OK, I made a huge mistake. This is a total disaster, all my fault. Yes, it kind of is. I've ruined the planet. I wanted to help you with the flower shop. I've made it worse. Actually, it's completely closed down. I thought maybe you were remodeling. But I have another idea, and it's greater than my previous ideas combined. I don't want to hear it! All right, they have the roses, the roses have the pollen. I know every bee, plant and flower bud in this park. All we gotta do is get what they've got back here with what we've got. Bees. Park. Pollen! Flowers. Repollination! Across the nation! Tournament of Roses, Pasadena, California. They've got nothing but flowers, floats and cotton candy. Security will be tight. I have an idea. Vanessa Bloome, FTD. Official floral business. It's real. Sorry, ma'am. Nice brooch. Thank you. It was a gift. Once inside, we just pick the right float. How about The Princess and the Pea? I could be the princess, and you could be the pea! Yes, I got it. Where should I sit? What are you? I believe I'm the pea. The pea? It goes under the mattresses. Not in this fairy tale, sweetheart. I'm getting the marshal. You do that! This whole parade is a fiasco! Let's see what this baby'll do. Hey, what are you doing?! Then all we do is blend in with traffic... without arousing suspicion. Once at the airport, there's no stopping us. Stop! Security. You and your insect pack your float? Yes. Has it been in your possession the entire time? Would you remove your shoes? Remove your stinger. It's part of me. I know. Just having some fun. Enjoy your flight. Then if we're lucky, we'll have just enough pollen to do the job. Can you believe how lucky we are? We have just enough pollen to do the job! I think this is gonna work. It's got to work. Attention, passengers, this is Captain Scott. We have a bit of bad weather in New York. It looks like we'll experience a couple hours delay. Barry, these are cut flowers with no water. They'll never make it. I gotta get up there and talk to them. Be careful. Can I get help with the Sky Mall magazine? I'd like to order the talking inflatable nose and ear hair trimmer. Captain, I'm in a real situation. What'd you say, Hal? Nothing. Bee! Don't freak out! My entire species... What are you doing? Wait a minute! I'm an attorney! Who's an attorney? Don't move. Oh, Barry. Good afternoon, passengers. This is your captain. Would a Miss Vanessa Bloome in 24B please report to the cockpit? And please hurry! What happened here? There was a DustBuster, a toupee, a life raft exploded. One's bald, one's in a boat, they're both unconscious! Is that another bee joke? No! No one's flying the plane! This is JFK control tower, Flight 356. What's your status? This is Vanessa Bloome. I'm a florist from New York. Where's the pilot? He's unconscious, and so is the copilot. Not good. Does anyone onboard have flight experience? As a matter of fact, there is. Who's that? Barry Benson. From the honey trial?! Oh, great. Vanessa, this is nothing more than a big metal bee. It's got giant wings, huge engines. I can't fly a plane. Why not? Isn't John Travolta a pilot? Yes. How hard could it be? Wait, Barry! We're headed into some lightning. This is Bob Bumble. We have some late-breaking news from JFK Airport, where a suspenseful scene is developing. Barry Benson, fresh from his legal victory... That's Barry! ...is attempting to land a plane, loaded with people, flowers and an incapacitated flight crew. Flowers?! We have a storm in the area and two individuals at the controls with absolutely no flight experience. Just a minute. There's a bee on that plane. I'm quite familiar with Mr. Benson and his no-account compadres. They've done enough damage. But isn't he your only hope? Technically, a bee shouldn't be able to fly at all. Their wings are too small... Haven't we heard this a million times? "The surface area of the wings and body mass make no sense." Get this on the air! Got it. Stand by. We're going live. The way we work may be a mystery to you. Making honey takes a lot of bees doing a lot of small jobs. But let me tell you about a small job. If you do it well, it makes a big difference. More than we realized. To us, to everyone. That's why I want to get bees back to working together. That's the bee way! We're not made of Jell-O. We get behind a fellow. Black and yellow! Hello! Left, right, down, hover. Hover? Forget hover. This isn't so hard. Beep-beep! Beep-beep! Barry, what happened?! Wait, I think we were on autopilot the whole time. That may have been helping me. And now we're not! So it turns out I cannot fly a plane. All of you, let's get behind this fellow! Move it out! Move out! Our only chance is if I do what I'd do, you copy me with the wings of the plane! Don't have to yell. I'm not yelling! We're in a lot of trouble. It's very hard to concentrate with that panicky tone in your voice! It's not a tone. I'm panicking! I can't do this! Vanessa, pull yourself together. You have to snap out of it! You snap out of it. You snap out of it. You snap out of it! You snap out of it! You snap out of it! You snap out of it! You snap out of it! You snap out of it! Hold it! Why? Come on, it's my turn. How is the plane flying? I don't know. Hello? Benson, got any flowers for a happy occasion in there? The Pollen Jocks! They do get behind a fellow. Black and yellow. Hello. All right, let's drop this tin can on the blacktop. Where? I can't see anything. Can you? No, nothing. It's all cloudy. Come on. You got to think bee, Barry. Thinking bee. Thinking bee. Thinking bee! Thinking bee! Thinking bee! Wait a minute. I think I'm feeling something. What? I don't know. It's strong, pulling me. Like a 27-million-year-old instinct. Bring the nose down. Thinking bee! Thinking bee! Thinking bee! What in the world is on the tarmac? Get some lights on that! Thinking bee! Thinking bee! Thinking bee! Vanessa, aim for the flower. OK. Cut the engines. We're going in on bee power. Ready, boys? Affirmative! Good. Good. Easy, now. That's it. Land on that flower! Ready? Full reverse! Spin it around! Not that flower! The other one! Which one? That flower. I'm aiming at the flower! That's a fat guy in a flowered shirt. I mean the giant pulsating flower made of millions of bees! Pull forward. Nose down. Tail up. Rotate around it. This is insane, Barry! This's the only way I know how to fly. Am I koo-koo-kachoo, or is this plane flying in an insect-like pattern? Get your nose in there. Don't be afraid. Smell it. Full reverse! Just drop it. Be a part of it. Aim for the center! Now drop it in! Drop it in, woman! Come on, already. Barry, we did it! You taught me how to fly! Yes. No high-five! Right. Barry, it worked! Did you see the giant flower? What giant flower? Where? Of course I saw the flower! That was genius! Thank you. But we're not done yet. Listen, everyone! This runway is covered with the last pollen from the last flowers available anywhere on Earth. That means this is our Last Chance. We're the only ones who make honey, pollinate flowers and dress like this. If we're gonna survive as a species, this is our moment! What do you say? Are we going to be bees, or just Museum of Natural History keychains? We're bees! Keychain! Then follow me! Except Keychain. Hold on, Barry. Here. You've earned this. Yeah! I'm a Pollen Jock! And it's a perfect fit. All I gotta do are the sleeves. Oh, yeah. That's our Barry. Mom! The bees are back! If anybody needs to make a call, now's the time. I got a feeling we'll be working late tonight! Here's your change. Have a great afternoon! Can I help who's next? Would you like some honey with that? It is bee-approved. Don't forget these. Milk, cream, cheese, it's all me.  And I don't see a nickel! Sometimes I just feel like a piece of meat! I had no idea. Barry, I'm sorry. Have you got a moment? Would you excuse me? My mosquito associate will help you. Sorry I'm late. He's a lawyer too? I was already a blood-sucking parasite. All I needed was a briefcase. Have a great afternoon! Barry, I just got this huge tulip order, and I can't get them anywhere. No problem, Vannie. Just leave it to me. You're a lifesaver, Barry. Can I help who's next? All right, scramble, jocks! It's time to fly. Thank you, Barry! That bee is living my life! Let it go, Kenny. When will this nightmare end?! Let it all go. Beautiful day to fly. Sure is. Between you and me, I was dying to get out of that office. You have got to start thinking bee, my friend. Thinking bee! Me? Hold it. Let's just stop for a second. Hold it. I'm sorry. I'm sorry, everyone. Can we stop here? I'm not making a major life decision during a production number! All right. Take ten, everybody. Wrap it up, guys. I had virtually no rehearsal for that.

According to all known laws of aviation, there is no way a bee should be able to fly.
Its wings are too small to get its fat little body off the ground.
The bee, of course, flies anyway because bees don't care what humans think is impossible.
Yellow, black. Yellow, black. Yellow, black. Yellow, black.
Ooh, black and yellow!
Let's shake it up a little.
Barry! Breakfast is ready!
Coming!
Hang on a second.
Hello?
Barry?
Adam?
Can you believe this is happening?
I can't.
I'll pick you up.
Looking sharp.
Use the stairs, Your father paid good money for those.
Sorry. I'm excited.
Here's the graduate.
We're very proud of you, son.
A perfect report card, all B's.
Very proud.
Ma! I got a thing going here.
You got lint on your fuzz.
Ow! That's me!
Wave to us! We'll be in row 118,000.
Bye!
Barry, I told you, stop flying in the house!
Hey, Adam.
Hey, Barry.
Is that fuzz gel?
A little. Special day, graduation.
Never thought I'd make it.
Three days grade school, three days high school.
Those were awkward.
Three days college. I'm glad I took a day and hitchhiked around The Hive.
You did come back different.
Hi, Barry. Artie, growing a mustache? Looks good.
Hear about Frankie?
Yeah.
You going to the funeral?
No, I'm not going.
Everybody knows, sting someone, you die.
Don't waste it on a squirrel.
Such a hothead.
I guess he could have just gotten out of the way.
I love this incorporating an amusement park into our day.
That's why we don't need vacations.
Boy, quite a bit of pomp under the circumstances.
Well, Adam, today we are men.
We are!
Bee-men.
Amen!
Hallelujah!
Students, faculty, distinguished bees,
please welcome Dean Buzzwell.
Welcome, New Hive City graduating class of 9:15.
That concludes our ceremonies And begins your career at Honex Industries!
Will we pick our job today?
I heard it's just orientation.
Heads up! Here we go.
Keep your hands and antennas inside the tram at all times.
Wonder what it'll be like?
A little scary.
Welcome to Honex, a division of Honesco and a part of the Hexagon Group.
This is it!
Wow.
Wow.
We know that you, as a bee, have worked your whole life to get to the point where you can work for your whole life.
Honey begins when our valiant Pollen Jocks bring the nectar to The Hive.
Our top-secret formula is automatically color-corrected, scent-adjusted and bubble-contoured into this soothing sweet syrup with its distinctive golden glow you know as... Honey!
That girl was hot.
She's my cousin!
She is?
Yes, we're all cousins.
Right. You're right.
At Honex, we constantly strive to improve every aspect of bee existence.
These bees are stress-testing a new helmet technology.
What do you think he makes?
Not enough.
Here we have our latest advancement, the Krelman.
What does that do?
Catches that little strand of honey that hangs after you pour it.
Saves us millions.
Can anyone work on the Krelman?
Of course. Most bee jobs are small ones.
But bees know that every small job, if it's done well, means a lot.
But choose carefully because you'll stay in the job you pick for the rest of your life.
The same job the rest of your life? I didn't know that.
What's the difference?
You'll be happy to know that bees, as a species, haven't had one day off in 27 million years.
So you'll just work us to death?
We'll sure try.
Wow! That blew my mind!
"What's the difference?"
How can you say that?
One job forever?
That's an insane choice to have to make.
I'm relieved. Now we only have to make one decision in life.
But, Adam, how could they never have told us that?
Why would you question anything? We're bees.
We're the most perfectly functioning society on Earth.
You ever think maybe things work a little too well here?
Like what? Give me one example.
I don't know. But you know what I'm talking about.
Please clear the gate. Royal Nectar Force on approach.
Wait a second. Check it out.
Hey, those are Pollen Jocks!
Wow.
I've never seen them this close.
They know what it's like outside The Hive.
Yeah, but some don't come back.
Hey, Jocks!
Hi, Jocks!
You guys did great!
You're monsters!
You're sky freaks! I love it! I love it!
I wonder where they were.
I don't know.
Their day's not planned.
Outside The Hive, flying who knows where, doing who knows what.
You can't just decide to be a Pollen Jock. You have to be bred for that.
Right.
Look. That's more pollen than you and I will see in a lifetime.
It's just a status symbol.
Bees make too much of it.
Perhaps. Unless you're wearing it and the ladies see you wearing it.
Those ladies?
Aren't they our cousins too?
Distant. Distant.
Look at these two.
Couple of Hive Harrys.
Let's have fun with them.
It must be dangerous being a Pollen Jock.
Yeah. Once a bear pinned me against a mushroom!
He had a paw on my throat, and with the other, he was slapping me!
Oh, my!
I never thought I'd knock him out.
What were you doing during this?
Trying to alert the authorities.
I can autograph that.
A little gusty out there today, wasn't it, comrades?
Yeah. Gusty.
We're hitting a sunflower patch six miles from here tomorrow.
Six miles, huh?
Barry!
A puddle jump for us, but maybe you're not up for it.
Maybe I am.
You are not!
We're going 0900 at J-Gate.
What do you think, buzzy-boy?
Are you bee enough?
I might be. It all depends on what 0900 means.
Hey, Honex!
Dad, you surprised me.
You decide what you're interested in?
Well, there's a lot of choices.
But you only get one.
Do you ever get bored doing the same job every day?
Son, let me tell you about stirring.
You grab that stick, and you just move it around, and you stir it around.
You get yourself into a rhythm.
It's a beautiful thing.
You know, Dad, the more I think about it,
maybe the honey field just isn't right for me.
You were thinking of what, making balloon animals?
That's a bad job for a guy with a stinger.
Janet, your son's not sure he wants to go into honey!
Barry, you are so funny sometimes.
I'm not trying to be funny.
You're not funny! You're going into honey. Our son, the stirrer!
You're gonna be a stirrer?
No one's listening to me!
Wait till you see the sticks I have.
I could say anything right now.
I'm gonna get an ant tattoo!
Let's open some honey and celebrate!
Maybe I'll pierce my thorax. Shave my antennae. Shack up with a grasshopper. Get a gold tooth and call everybody "dawg"!
I'm so proud.
We're starting work today!
Today's the day.
Come on! All the good jobs will be gone.
Yeah, right.
Pollen counting, stunt bee, pouring, stirrer, front desk, hair removal...
Is it still available?
Hang on. Two left!
One of them's yours! Congratulations!
Step to the side.
What'd you get?
Picking crud out. Stellar!
Wow!
Couple of newbies?
Yes, sir! Our first day! We are ready!
Make your choice.
You want to go first?
No, you go.
Oh, my. What's available?
Restroom attendant's open, not for the reason you think.
Any chance of getting the Krelman?
Sure, you're on.
I'm sorry, the Krelman just closed out.
Wax monkey's always open.
The Krelman opened up again.
What happened?
A bee died. Makes an opening. See? He's dead. Another dead one.
Deady. Deadified. Two more dead.
Dead from the neck up. Dead from the neck down. That's life!
Oh, this is so hard!
Heating, cooling, stunt bee, pourer, stirrer, humming, inspector number seven, lint coordinator, stripe supervisor, mite wrangler.
Barry, what do you think I should... Barry?
Barry!
All right, we've got the sunflower patch in quadrant nine...
What happened to you?
Where are you?
I'm going out.
Out? Out where?
Out there.
Oh, no!
I have to, before I go to work for the rest of my life.
You're gonna die! You're crazy! Hello?
Another call coming in.
If anyone's feeling brave, there's a Korean deli on 83rd that gets their roses today.
Hey, guys.
Look at that.
Isn't that the kid we saw yesterday?
Hold it, son, flight deck's restricted.
It's OK, Lou. We're gonna take him up.
Really? Feeling lucky, are you?
Sign here, here. Just initial that.
Thank you.
OK.
You got a rain advisory today, and as you all know, bees cannot fly in rain.
So be careful. As always, watch your brooms, hockey sticks, dogs, birds, bears and bats.
Also, I got a couple of reports of root beer being poured on us.
Murphy's in a home because of it, babbling like a cicada!
That's awful.
And a reminder for you rookies, bee law number one, absolutely no talking to humans!
 All right, launch positions!
Buzz, buzz, buzz, buzz! Buzz, buzz, buzz, buzz! Buzz, buzz, buzz, buzz!
Black and yellow!
Hello!
You ready for this, hot shot?
Yeah. Yeah, bring it on.
Wind, check.
Antennae, check.
Nectar pack, check.
Wings, check.
Stinger, check.
Scared out of my shorts, check.
OK, ladies,
let's move it out!
Pound those petunias, you striped stem-suckers!
All of you, drain those flowers!
Wow! I'm out!
I can't believe I'm out!
So blue.
I feel so fast and free!
Box kite!
Wow!
Flowers!
This is Blue Leader, We have roses visual.
Bring it around 30 degrees and hold.
Roses!
30 degrees, roger. Bringing it around.
Stand to the side, kid.
It's got a bit of a kick.
That is one nectar collector!
Ever see pollination up close?
No, sir.
I pick up some pollen here, sprinkle it over here. Maybe a dash over there, a pinch on that one.
See that? It's a little bit of magic.
That's amazing. Why do we do that?
That's pollen power. More pollen, more flowers, more nectar, more honey for us.
Cool.
I'm picking up a lot of bright yellow, Could be daisies, Don't we need those?
Copy that visual.
Wait. One of these flowers seems to be on the move.
Say again? You're reporting a moving flower?
Affirmative.
That was on the line!
This is the coolest. What is it?
I don't know, but I'm loving this color.
It smells good.
Not like a flower, but I like it.
Yeah, fuzzy.
Chemical-y.
Careful, guys. It's a little grabby.
My sweet lord of bees!
Candy-brain, get off there!
Problem!
Guys!
This could be bad.
Affirmative.
Very close.
Gonna hurt.
Mama's little boy.
You are way out of position, rookie!
Coming in at you like a missile!
Help me!
I don't think these are flowers.
Should we tell him?
I think he knows.
What is this?!
Match point!
You can start packing up, honey, because you're about to eat it!
Yowser!
Gross.
There's a bee in the car!
Do something!
I'm driving!
Hi, bee.
He's back here!
He's going to sting me!
Nobody move. If you don't move, he won't sting you. Freeze!
He blinked!
Spray him, Granny!
What are you doing?!
Wow... the tension level out here is unbelievable.
I gotta get home.
Can't fly in rain. Can't fly in rain. Can't fly in rain.
Mayday! Mayday! Bee going down!
Ken, could you close the window please?
Ken, could you close the window please?
Check out my new resume. I made it into a fold-out brochure. You see? Folds out.
Oh, no. More humans. I don't need this.
What was that?
Maybe this time. This time. This time. This time! This time! This... Drapes!
That is diabolical.
It's fantastic. It's got all my special skills, even my top-ten favorite movies.
What's number one? Star Wars?
Nah, I don't go for that... kind of stuff.
No wonder we shouldn't talk to them. They're out of their minds.
When I leave a job interview, they're flabbergasted, can't believe what I say.
There's the sun. Maybe that's a way out.
I don't remember the sun having a big 75 on it.
I predicted global warming. I could feel it getting hotter. At first I thought it was just me.
Wait! Stop! Bee!
Stand back. These are winter boots.
Wait!
Don't kill him!
You know I'm allergic to them! This thing could kill me!
Why does his life have less value than yours?
Why does his life have any less value than mine? Is that your statement?
I'm just saying all life has value. You don't know what he's capable of feeling.
My brochure!
There you go, little guy.
I'm not scared of him.It's an allergic thing.
 Put that on your resume brochure.
My whole face could puff up.
Make it one of your special skills.
Knocking someone out is also a special skill.
Right. Bye, Vanessa. Thanks.
Vanessa, next week? Yogurt night?
Sure, Ken. You know, whatever.
You could put carob chips on there.
Bye.
Supposed to be less calories.
Bye.
I gotta say something. She saved my life. I gotta say something.
All right, here it goes.
Nah.
What would I say?
I could really get in trouble. It's a bee law. You're not supposed to talk to a human.
I can't believe I'm doing this. I've got to.
Oh, I can't do it. Come on!
No. Yes. No. Do it. I can't.
How should I start it? "You like jazz?" No, that's no good.
Here she comes! Speak, you fool!
Hi!
I'm sorry. You're talking.
Yes, I know.
You're talking!
I'm so sorry.
No, it's OK. It's fine.
I know I'm dreaming. But I don't recall going to bed.
Well, I'm sure this is very disconcerting.
This is a bit of a surprise to me. I mean, you're a bee!
I am. And I'm not supposed to be doing this, but they were all trying to kill me.
And if it wasn't for you... I had to thank you. It's just how I was raised.
That was a little weird. I'm talking with a bee.
Yeah.
I'm talking to a bee. And the bee is talking to me!
I just want to say I'm grateful.
I'll leave now.
Wait! How did you learn to do that?
What?
The talking thing.
Same way you did, I guess. "Mama, Dada, honey." You pick it up.
That's very funny.
Yeah.
Bees are funny. If we didn't laugh, we'd cry with what we have to deal with.
Anyway... Can I... get you something?
Like what?
I don't know. I mean... I don't know. Coffee?
I don't want to put you out.
It's no trouble. It takes two minutes.
It's just coffee.
I hate to impose.
Don't be ridiculous!
Actually, I would love a cup.
Hey, you want rum cake?
I shouldn't.
Have some.
No, I can't.
Come on!
I'm trying to lose a couple micrograms.
Where?
These stripes don't help.
You look great!
I don't know if you know anything about fashion.
Are you all right?
No.
He's making the tie in the cab as they're flying up Madison.
He finally gets there.
He runs up the steps into the church.
The wedding is on.
And he says, "Watermelon?
I thought you said Guatemalan.
Why would I marry a watermelon?"
Is that a bee joke?
That's the kind of stuff we do.
Yeah, different.
So, what are you gonna do, Barry?
About work? I don't know.
I want to do my part for The Hive, but I can't do it the way they want.
I know how you feel.
You do?
Sure.
My parents wanted me to be a lawyer or a doctor, but I wanted to be a florist.
Really?
My only interest is flowers.
Our new queen was just elected with that same campaign slogan.
Anyway, if you look... There's my hive right there. See it?
You're in Sheep Meadow!
Yes! I'm right off the Turtle Pond!
No way! I know that area. I lost a toe ring there once.
Why do girls put rings on their toes?
Why not?
It's like putting a hat on your knee.
Maybe I'll try that.
You all right, ma'am?
Oh, yeah. Fine.
Just having two cups of coffee!
Anyway, this has been great.
Thanks for the coffee.
Yeah, it's no trouble.
Sorry I couldn't finish it. If I did, I'd be up the rest of my life.
Are you...?
Can I take a piece of this with me?
Sure! Here, have a crumb.
Thanks!
Yeah.
All right. Well, then... I guess I'll see you around. Or not.
OK, Barry.
And thank you so much again... for before.
Oh, that? That was nothing.
Well, not nothing, but... Anyway...
This can't possibly work.
He's all set to go.
We may as well try it.
OK, Dave, pull the chute.
Sounds amazing.
It was amazing!
It was the scariest, happiest moment of my life.
Humans! I can't believe you were with humans!
Giant, scary humans!
What were they like?
Huge and crazy. They talk crazy.
They eat crazy giant things.
They drive crazy.
Do they try and kill you, like on TV?
Some of them. But some of them don't.
How'd you get back?
Poodle.
You did it, and I'm glad. You saw whatever you wanted to s…

---
## [ved-websites/fullstacked](https://github.com/ved-websites/fullstacked)@[c43c7e4c9a...](https://github.com/ved-websites/fullstacked/commit/c43c7e4c9afda83ab52dc1f18292942fcdcb6216)
#### Friday 2023-06-23 06:49:07 by Guillaume Marcoux

implement whole login logout behavior

where to begin with this commit

frontend :
- the cookie is handled by sveltekit, and it is a cookie instead of a localStorage item because it needs to be sent to the sveltekit backend (could potentially be changed through a function in the `+layout.svelte` file, using a localstorage function getter)
- urql setup now uses authExchange, making it more resilient and no only adding mere fetchOptions (the refreshAuth still needs to be implemented, as no backend route was created yet to refresh the bearer token)
- mutation were completely overhauled to allow to run define them on component initialization, and calling them later. much less boilerplate to send data update requests directly in the frontend!
- navbar shows proper user updates with easy typing
- you can login without javascript, but the logout button, while working without javascript, requires javascript to show up, so javascript is needed to escape the hell hole of the websites I will create, muahahahaha

backend :
- lucia is now using v2-beta, which means that authentication header is available, which is what I need because my frontend and backend are cross-origin
- unfinished auth handler, but login and logouts are dealt with
- decorators allow for easy retrieving of the session and the lucia auth object
- Lucia module and Auth modules are separated to allow for greater flexibility : Auth will probably stay extremely similar while the lucia module is volatile based on backend infrastructure (and now actually works instead of breaking everything pushing me to almost want to purchase nestjs devtools)
- schema was updated to reflect cleaner lucia v2 structure (tho I kinda wish to update the table names, will see in the future)
- Lucia now has proper typing of the data used! and so is the express locals! typing rejoince
- lots-a gulp plugins are not used anymore so goodbye! as the gulp prompts was removed, so is the types folder. one root-ish folder less!
- hooks setup property getters, which can or need to be event dependent, so it doesn't statically use the event on init only

oh and also :
- graphql generator now handles all common files containing queries (`.graphql`, `.svelte`, `.server.ts`), and when it breaks oh boy does it break, typescript needs to compile for the generator to work
- Prisma fixture is officially broken as it was designed to be used with autogenerated number sequences in mind

---
## [vampirebat74/lobotomy-corp13](https://github.com/vampirebat74/lobotomy-corp13)@[b420c1d519...](https://github.com/vampirebat74/lobotomy-corp13/commit/b420c1d519b30cd75759de68f6b2abbe0b12a055)
#### Friday 2023-06-23 07:04:11 by vampirebat74

Adds tool E.G.O (#1019)

Tool ego

adds tool E.G.O

removes a extra line

fixes shit

swindle

voce

divinity

fixes shit

shifts divinity down a few pixels

This is the fourth time this same commit was made

I hate TG so fucking much like it's unbelievable why does this only fuck up on my PC? WHY?

hyde weapon

stuff

hyde code

hyde fix

new sprites

inhands

destiny effect

heart sfx

stuff

Co-authored-by: Mr.Heavenly <davidx3adamhunt@gmail.com>

---
## [KingDragoness/ProjectHypatios](https://github.com/KingDragoness/ProjectHypatios)@[29b2532b0b...](https://github.com/KingDragoness/ProjectHypatios/commit/29b2532b0b25d66ac24e63736eb66a501791904a)
#### Friday 2023-06-23 07:10:08 by KingDragoness

Hypatios 1.5.4b5 (quality of life improvements, bug fixes, balancing)
DONE (June 23)
• New ailment: Broken Leg
o When falling over 20m height, the player has a 40% chance suffering from broken leg.
o Broken leg causes the player to be permanently crouched.
• Placing TV news in level 4, level 6, level 8, boss fight, and level 7 (base camp).
• Delete all newsreel, replaced it with dialogue prefab (x16 more maintainable!)
o SpeechDialogueAsset is only optimized for less than 6 dialogue lines.
• Bug/Missing: No Chinatown chamber scriptableobject (main menu pointer)
• Bug: Missing Sentinel texture! (what the hell?)
• Remove feature: Remove this thing (Enter your name)
• Remove feature: Remove new game selection screen, straight to Aldrich’s level. Elena levels removed.
• Number weapon slot in the background to indicate slots
• Bug: Recoil description bug (the gameplay is correct but the description is wrong)
• Bug: Consumables preview should start from targethealth not currenthealth
• Killer pill briefcase notes
o “If you got heavy ailment and condition is in dire, take this pill to kill yourself and restart.”
• Bug: Level3 Temple exit leads to level 3-Temple!
• Balancing: More ammo reward for minigun.
• Quality of Life: Critical hits will displayed “CRIT!”
• Newsreel #01 remove any reference to Aldrich.
• Decabot corpse remove collision.
• Fortima trivia screenshot is using the old ones, needs to be changed.

---
## [itsmeowForks/BeeStation-Hornet](https://github.com/itsmeowForks/BeeStation-Hornet)@[c510754477...](https://github.com/itsmeowForks/BeeStation-Hornet/commit/c51075447793ce327197f603bf61e15f6bc2d047)
#### Friday 2023-06-23 07:12:46 by itsmeow

IPCs being bullshit and breaking previews. still broken. fuck IPCs. IPC shitcode galore. I hate it here. Body models hide if species has no sexes

---
## [ChSatyaSavith/LeetCode](https://github.com/ChSatyaSavith/LeetCode)@[8c4c0e2f7f...](https://github.com/ChSatyaSavith/LeetCode/commit/8c4c0e2f7f999d7897fc22e3231a305cfcc8bad1)
#### Friday 2023-06-23 07:15:22 by NotFluent

Had to copy but thoda thoda samajh aya , i need to fucking up my dp game guys, aight babes on my way to master dp hell yeah

---
## [subhoghoshX/cockpit](https://github.com/subhoghoshX/cockpit)@[79d6a888d4...](https://github.com/subhoghoshX/cockpit/commit/79d6a888d43a1544ec275c7681cc699abdd698f0)
#### Friday 2023-06-23 07:49:53 by Martin Pitt

pybridge: Fix clobbering remote user set in SSH config

When opening a remote host channel without `user`, stop assuming the
current local user name, as that overwrites any `User` field in
the SSH configuration.

Instead, we need to do the opposite: for an unknown host, the UI will
not set a `user` field in the channel options, but for an actual login
attempt with a password it will. We need to treat them as the same
channel in the `self.remotes` map. The C bridge deals with this in
cockpit_router_normalize_host_params() by disregarding the `user` field
if it is equal to the current user name.

This is a rather silly hack for backwards compatibility, but while we
have two bridges, let's rather stay bug-for-bug compatible and clean
this up in the UI only after we drop the C bridge.

There is one extra tweak: `rpartition()` returns an empty string, but
we can't pass that on literally. So turn those into `None`.

Fixes #18714

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[867c217c57...](https://github.com/tgstation/tgstation/commit/867c217c57bbcbb644e06bfcb6d362e494a895ee)
#### Friday 2023-06-23 08:56:21 by GuillaumePrata

New Wizard spell "branch": Vendormancy (#75679)

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

Co-authored-by: Time-Green <7501474+Time-Green@users.noreply.github.com>

---
## [hungphan2001/android_frameworks_base](https://github.com/hungphan2001/android_frameworks_base)@[6be1d79b58...](https://github.com/hungphan2001/android_frameworks_base/commit/6be1d79b58660008b03242726fc9ecd092544f98)
#### Friday 2023-06-23 09:05:37 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6
Signed-off-by: Sageofd6path <mail2anirban95@gmail.com>
Signed-off-by: Hưng Phan <phandinhhungvp2001@gmail.com>

---
## [vampirebat74/lobotomy-corp13](https://github.com/vampirebat74/lobotomy-corp13)@[a90789d982...](https://github.com/vampirebat74/lobotomy-corp13/commit/a90789d982b1819aefd2c9ff0338877ab7674260)
#### Friday 2023-06-23 09:10:29 by Mr.Heavenly

Adds Red Shoes

Mr. Heavenly's Abnormality Jam Entry #1

Records

uncommented weapon

Finishing touches

Design rework

adds ego gift and inhands

New sprites!

uncommented sfx

insanity fix

quieter sound loop

Fixes some shit

fix linters

---
## [xh3xy/evals](https://github.com/xh3xy/evals)@[f5844592f1...](https://github.com/xh3xy/evals/commit/f5844592f13eff8e7b9927d5cec0d2627694d9d9)
#### Friday 2023-06-23 09:59:18 by Ali-consensus

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
## [xh3xy/evals](https://github.com/xh3xy/evals)@[d708a6be26...](https://github.com/xh3xy/evals/commit/d708a6be261bfcb04962e64969164d737ba3972c)
#### Friday 2023-06-23 09:59:18 by dougkwanna

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
## [xh3xy/evals](https://github.com/xh3xy/evals)@[73c8a178e6...](https://github.com/xh3xy/evals/commit/73c8a178e69418760baee8983daa19fb492e9231)
#### Friday 2023-06-23 09:59:18 by somerandomguyontheweb

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
## [DavidHaywood/mame](https://github.com/DavidHaywood/mame)@[2bcd9bc772...](https://github.com/DavidHaywood/mame/commit/2bcd9bc772b4f3cc6e8b281703e53561d2c5bea9)
#### Friday 2023-06-23 10:00:03 by David 'Foxhack' Silva

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
## [git-for-windows/git](https://github.com/git-for-windows/git)@[477e9cfc6f...](https://github.com/git-for-windows/git/commit/477e9cfc6fc34cbdac67bc0043ea4a244f5a42e9)
#### Friday 2023-06-23 10:36:28 by Johannes Schindelin

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
## [GreaterLondonAuthority/dfl-ckanext](https://github.com/GreaterLondonAuthority/dfl-ckanext)@[873ef9fdaf...](https://github.com/GreaterLondonAuthority/dfl-ckanext/commit/873ef9fdafcdb4a699b307f508edc179713e7698)
#### Friday 2023-06-23 11:15:59 by madelinekosse

DAT-309-243 Add LGOV scripts and GA

Adds the following scripts:
* Cookie consent manager
* Crisis communication
* Google analytics

It also adds a link to the footer that opens the cookie manager panel.

To avoid sending a bunch of google analytics requests during local development,
these are not added to the page head on localhost. You'll see the link in the
footer, but it won't do anything on localhost.

I've configured the cookie manager with some options that seemed sensible to me
because the default looked a little confusing in my opinion.

---
## [wrye-bash/wrye-bash](https://github.com/wrye-bash/wrye-bash)@[59cc8750f5...](https://github.com/wrye-bash/wrye-bash/commit/59cc8750f5f8038fb500eb54d91e30cf3ae61045)
#### Friday 2023-06-23 11:23:11 by MrD

Squash of ut-336-219-353 with fixups and drop pending_size:

Nit and small fixes/opts: TTT

In `ext in bush.game.espm_extensions` ext used to be cs - it's not
anymore so this is a fixup. I ended up using EAFP here, hence dropping
the top_level_espm check - should be as fast as before and it's simpler.
Took the opportunity to prune an especially nasty use of getGhosted - a
few str operations should be faster than listing. Note that when
calling process_data_dir from update_data_SizeCrcDate getGhosted()
would be called twice.

Re: skipExts:

I run into an esp.ghost.ghost file - since we neither want to add those
to InstallersData.data_SizeCrcDate (ModInfos should skip those too) nor
in Installer.refreshDataSizeCrc I added them to skipExts TTT

bain.py  180 calc_crcs: Failed to calculate crc for D:\GAMES\TESIV\Oblivion\Data\New Mod--.esp.ghost - please report this, and the following traceback:
Traceback (most recent call last):
  File "C:\Dropbox (Personal)\eclipse_workspaces\python\wrye-bash\Mopy\bash\bosh\bain.py", line 174, in calc_crcs
    with open(asFile, u'rb') as ins:
         ^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'D:\\GAMES\\TESIV\\Oblivion\\Data\\New Mod--.esp.ghost' <--  the file was "New Mod--.esp.ghost.ghost"

Rename Installer.modified attribute to align with AFile

Align with AFile SSS

Would be nice to use the rest of the AFile API here (do_update and co -
hard!). Note I dropped the rpFile = os.path.join(rsDir, sFile) -
chopping asFile[relPos:] should be enough (and much faster).

Inline _refresh_from_project_dir:

We must change the model - in a nutshell use AFile's API (override
_stat_tuple for projects with NotImplemented, as it makes no sense
there, and add the _refreshSource logic in do_update - archives can use
the full API as they are files). Then only use do_update (with added
progress and hopefully little other kwargs) and perform the update *in
place* where we now call needs_update. This ripples till InstallersData
(irefresh) and it's fairly complex (and currently complicated) but will
eventually get us rid of _projects_walk_cache and a couple methods
(and stop being complicated) - edit done later, turns out _stat_tuple
works for projects just right - yey for AFile.

'pending' renames - I need to track refresh_info

class _InstallerPackage(Installer, AFile):

_refreshSource confined there - yey!

Refactor AFile:

Less uses of load_cache - and itsa_ghost. WIP - I might add load_cache
back to the signature if I figure a default out

Installer.do_update: TTT RRR EEE

@@ -2215,8 +2215,6 @@ def _refresh_from_data_dir(self, progress, recalculate_all_crcs):
                             progress)
-        self.data_sizeCrcDate.clear()
-        self.data_sizeCrcDate.update(new_sizeCrcDate)
-        change = changes
+        self.data_sizeCrcDate = new_sizeCrcDate
         self.update_for_overridden_skips(progress=progress) #after final_update
         #--Done
-        return change
+        return changes  EEE

One of the hardest things to grok in BAIN refresh was the decorator
projects_walk_cache. It was necessary in order not to re-walk the
project dir in case we just walked it in scan_installers_dir. Looking
at it now we should have been caching also the stat calls in that case
but when this was introduced BAIN internals were so complicated that this
was not so obvious (performance here is anyway still WIP). Turns out it
is much simpler and probably just as 'fast' to call do_update rather
than trying to pass needs_update caches to refreshBasic. This all but
closes # 336 as now AFile API is used for all kinds of files - and
makes BAIN refresh internals as little complicated as possible. See
discussion in RRR 6d4ad99841233d83abd326ad81121a0d09f88bc0 but unlike
what I noted there the pleasant surprise was that AFile can handle
folders alright - do_update is powerful enough and can be further
refactored to cater for fullRefresh. Note:

- the ancient fixme. What this was trying to convey is that actually
if you went ahead and renamed a file in a project containing another
file with large modification time the change would not be detected. The
workaround was to manually refresh the project. This was done for
efficiency as the vast majority of the changes would be detected,
but now that computers are faster let's make this correct. For big
src_SizeCrcDate this would be slower but hey the system calls should
dwarf that (for big src_SCD) and anyway that's what the skip refresh
flag is for. Now that we do the full check (should be more than enough
but can still give a false negative if we flip a byte on a file without
changing the modification time - hey, caching) we might as well drop the
calculations from _stat_tuple.
- the common data structure format for cacl_crcs included the old crc -
cf (siz, _crc, date, asFile). I changed that to pass the asFile and I
am still debugging it but the benefits should be obvious
- I reassign src_SizeCrcDate instead of clean/update - faster and
cleaner (and should be also done for data_sizeCrcDate) but still TTT EEE

SSS FFF fix for fullRefresh not getting the paths to ghosts

I had to treat plugins separately - no harm done on average and
fullRefresh will calculate their CRCs once finally.

Under # 336, # 219, # 353 RRR

FFF inline _refreshInstallers: EEE better comments

Seems now refresh_info and pending/deleted are orthogonal - needs
further simplification. We need to pass pending/deleted to
scan_installers_dir actually and use that instead of listing - edit:
done.

Progress does not work correctly (never gives focus back to Bash) XXX???

refreshBasic -> _reset_cache EEE do_refresh=True flip default

Installer.refresh_installer -> InstellersData.new_info: TTT

setattr(clone, att, copy.copy(getattr(src_inst, att))) should work on LDs TTT

EEE Mopy/bash/basher/dialogs.py InstallerProject import remove.

Another hacky refactoring helper gone but there is more. When we were
unpickling on InstallersData.__load > __setstate we were calling at least
refreshDataSizeCrc but then we would perform a system call on abs_path -
now this is replaced with a necessary stat_tuple() call and
scan_installers_dir learned to skip freshly unpickled installers. We also
hook in AFile.__init__ - this drops abs_path from Installer (if we were
accessing this on markers that'a bug) by adding a new 'volatile' attribute
to _InstallerPackage (AFile's _file_key - now we can't slot we should
revisit all this along with pickling - we should stop pickling non std
classes). __init__ calls _reset_cache, so no need to call needs update
from new_info. One other (and hopefully the last) installer creation
site was __copy__ - that's too much magic, absorbed by new_info and the
bits of (arcane) logic were copied to copy_installer which should be
the only place we copy an installer. Finally I had to exclude fn_key
from persistent - this is set alright by __init__, the latter one being
called on unpickling as specified in __reduce__. So on unpickling
initDefault was called twice - maybe make Installer a dataclass and bin
initDefault?

SSS add_marker -> new_info

Use scandir instead of walk: RRR

I was aware there was maybe a way using scandir of not repeating some
stat calls while scanning a directory - all I could find was this:

https://discuss.python.org/t/get-direntry-objects-collected-during-os-walk/8143/5

I wondered if it performed better than walk:

import os
import timeit

numbers = 4
repeat = 7

setup = """"""
def timer(statement, msg='', _setup=None):
    print(msg, min(
        timeit.Timer(statement, setup=_setup or setup).repeat(
            repeat, numbers)))

def _scandir_walk(apath, root_len=None, folders_times=None):
    size_apath_date = {}
    if root_len is None:
        root_len = len(apath) + 1
    folders_times = [os.path.getmtime(apath)] if folders_times is None \
	    else folders_times
    for dirent in os.scandir(apath):
        if dirent.is_dir():
            folders_times.append(dirent.stat().st_mtime)
            dir_walk, _ = _scandir_walk(dirent.path, root_len, folders_times)
            size_apath_date.update(dir_walk)
        else:
            size_apath_date[dirent.path[root_len:]] = (
                (ls := dirent.stat()).st_size, dirent.path, ls.st_mtime)
    return size_apath_date, folders_times

def _walk(apath, __lstat=os.stat):
    getM, join = os.path.getmtime, os.path.join
    size_apath_date = {}
    c = []
    cAppend = c.append
    root_len = len(apath) + 1
    for root, _d, files in os.walk(apath):
        # progress(0.05, f'{progress_msg}{asDir[relPos:]}')
        cAppend(getM(root))
        size_apath_date.update(
            (k[root_len:], (ls.st_size, k, ls.st_mtime)) for k, ls in
            ((asPath, __lstat(asPath)) for asPath in
                      (join(root, f) for f in files)))
    return size_apath_date, c

setup = """d = r'C:\Dropbox\eclipse_workspaces\python\wrye-bash'
from __main__ import _scandir_walk, _walk
"""
timer('_scandir_walk(d)', "scandir")
timer('_walk(d)', "walk")

sc = _scandir_walk(d)
wal = _walk(d)
assert sc[0] == wal[0]
assert set(sc[1]) == set(wal[1])
assert max(sc[1]) == max(wal[1])

C:\Users\MrD\AppData\Local\Programs\Python\Python311\python.exe C:\Dropbox\eclipse_workspaces\python\py_scratch\timings.py
scandir 1.3165479998569936
walk 28.77752220002003

21 times faster! Projects refresh is the bottleneck in BAIN refresh,
hence all the skipRefresh/autoRefreshProjects/projectRefreshed. This
is happily solving this for most installs (don't know if this can
be made faster or switching to event based refreshes RRR is the only real
solution, in which case we still want all the speed we can get scanning
anyway, for the initial scan on booting BAIN, but also for manual
refreshes that might be needed in edge cases).

Absorb _process_data_dir:

Time immemorial ago (b17601ef5bc25101c1fc12141f252ea250d49424) was
created to house the common logic of _refresh_from_data_dir (so
existing files maybe with a ghost extension) and
update_data_SizeCrcDate (so dest paths to the data dir with .ghost
lopped of). Now that we realized that scandir stating is considerably
faster and since performance here is a bane _process_data_dir had to go
- flat is better than nested, certainly in BAIN refresh. Those methods
calling one another were always new to new and experienced dev alike
and the pieces of functionality that were needed in
_refresh_from_data_dir but not in update_data_SizeCrcDate and vice
versa turned complex to complicated:

- we should not skip files/folders in update_data_SizeCrcDate as we come
from refreshDataSizeCrc (even if we currently do - TTT this beast is hard
to track - related to overwritten skips handling which certainly has
buggy edge cases some of them acknowledged in the code, see
overriden_skips comments)
- ghost handling belongs to update_data_SizeCrcDate - this led to double
calling getGhosted see RRR
- in fact the logic of _process_data_dir was the update_data_SizeCrcDate
logic as the walk logic of _refresh_from_data_dir was replaced by new
code in _walk_data_dir so the code of _process_data_dir was not repeated

_refresh_from_data_dir:

- I axed the progress messages as anyway we displayed very few of them
quite randomly. We can easily add them back in _walk_data_dir but since
we are on dev we can afford to live without these progress messages
- empty dirs is a WIP TTT - in particular what we do would not remove
a dir composed of empty dirs that were removed. OTH we could even remove
this from refresh and/or add a special menu item for cleaning empty dirs
(maybe launch it if setting is on also)

update_data_SizeCrcDate:

- what happens with "corrupted" mods really? They should be added to
data_SizeCrcDate most probably

__init__.py 4268 RefreshData:
11118614 function calls (11112306 primitive calls) in 6.492 seconds

__init__.py 4268 RefreshData:
436784 function calls (434428 primitive calls) in 0.263 seconds

FFF empty_dirs

FFF

- note I changed _skips_in_data_dir to work with dicts to keep the abs
path of the top_dir around - not for performance this time but sprinkling
os.path.join does not look nice.

Empties handling: SSS TTT

Changes the logic: TTT

- remove subdirs that contain no files in any of their subfolders - the
root one should be taken care of at the caller's level. Note the
(hacky) 'proj_dir.makedirs()' is not needed anymore, simply by not
handling the return value vs handling has_files for top Data dirs.
Previously we would leave behind empty subfolders except if we
carefully sorted which might have been the case (or not). Plus we could
delete folders before their subfolders (hence removedirs was called
defensively and abundantly). Now the logic is clearly spelled out in
_remove_empty_dirs (TTT deserves a test certainly) and repeated in
_walk_data_dir (as noted we need performance so factoring a walk
function parameter out is a no-no - plus we can afford some repetition
for the readability, especially as the walk functions are inlined
closer to irefresh and not buried as before).

- we remove as we go. This is less atomic but thankfully we had no
guaranties anyway :Plus we won't really miss anything if the operation
fails we just leave behind less empty dirs.

Kept error handling the same as before - although all the dirs should
exist in the `raise_error=False` case in _walk_data_dir.

SSS TTT Drop pending_size handling

Let's go nuclear on this. I *think* the problem might actually be some
kind of overflow in native Windows/wxWidgets code with a large enough
Data folder and enough large files in it that need to be updated.

This may actually speed up a Full Refresh. For a large file (e.g.
Fallout4 - Textures1.ba2 at 2.5G) we would issue thousands of progress
calls (1290 for that BA2, to be exact), which definitely isn't ideal in
the middle of a CRC calculation.

---
## [wrye-bash/wrye-bash](https://github.com/wrye-bash/wrye-bash)@[407fb2b3ec...](https://github.com/wrye-bash/wrye-bash/commit/407fb2b3ec7cc8735e739e85b97b34ea0297fc2e)
#### Friday 2023-06-23 11:23:11 by Infernio

Rework temporary file handling RRR TTT

View with whitespace diff off for an easier time (--ignore-all-space).

This turned out to be a lot more work than I thought. Really should have
been a branch, but I misjudged this horribly, then it kept growing...
Also not sure how feasible this would be to have as a branch without
breaking dev.

Wrye Bash's temporary files handling was actually a complete mess. There
were *three* different ways that random pieces of code were using it:
 - bass.getTempDir/newTempDir/rmTempDir
 - Path.temp and Path.untemp
 - Just use Path.baseTempDir/tempDir or even tempfile directly and do
   it completely manually.

These all had problems:
 - The bass APIs were very implicit - you would extract something to the
   'bass temp dir' and then access it via getTempDir in some other
   function, then remove the directory via rmTempDir in another
   function. XXX I'm still not done tracking this implicit mess down
   (see converters.py).
 - Path.temp did not guarantee that the file would be unique. This isn't
   really a problem for Wrye Bash right now, but would become a big
   problem if we ever wanted to allow multiple instances to run at the
   same time (which we do). Path.untemp also did some really weird I/O
   stuff that doesn't seem necessary at all and would just cost us a
   bunch of syscalls.
 - Path.baseTempDir/tempDir and tempfile required you to keep track of
   all the path manipulation and logic manually. After going through all
   this refactoring, trust me when I say that you do *not* want to do
   this manually. These places were few, thankfully, and none seem to
   have messed it up.

The new API (wbtemp.py) exposes two ways to do it:
 - Use TempDir or TempFile in a context manager. This is extremely
   simple and works very well. It guarantees that the file will be
   cleaned up, even if your logic becomes very complex or an exception
   occurs.
 - Use new_temp_dir/new_temp_file to create a temporary dir/file and
   manually clean it up via cleanup_temp_dir/cleanup_temp_file. These
   should be used *very sparingly*, only where absolutely needed.
   Right now we only have a single usage of manual temp files in
   dialogs.UpdateNotification and two usages of manual temp dirs (one in
   InstallerArchive.unpackToTemp and one in env.shellMakeDirs).

It also has other advantages:
 - Complexity is encapsulated to a single file.
 - Works even during (very) early boot (though doesn't seem to be
   needed right now?).
 - Should work perfectly with multiple instances of WB running at the
   same time (which isn't possible yet, but is a goal for the future).

There's one ugly wart. barb wants to extract archives to a temporary
folder, which then needs to survive a restart of WB, whereupon it will
be handled by the boot '--restore' handler. wbtemp, by design, does not
allow this and will clean up all created directories and files on exit.
To handle this, I used manual tempfile fiddling. Perhaps a future
refactoring of barb could fix this, but for now I think it's an
acceptable tradeoff for the massive improvements this commit brings us.

Some random stuff that got stuck in here:

Note that I got rid of the utf-8-sig encodings passed to 7z, the docs
say:

  Notes: The list file in Unicode charset can start with the BOM (byte
  order mark) character (U+FEFF). In that case 7-Zip checks that
  encoding of BOM corresponds to encoding specified with this switch
  (for UTF-16LE and UTF-16BE).

and:

  Default charset is UTF-8.

From https://7-zip.opensource.jp/chm/cmdline/switches/charset.htm
Very happy to see some of these terrible BOMs disappear from the
codebase.

Mopy/bash/basher/gui_fomod.py:
Some minor warning fixups in gui_fomod

Closes # 665 <--- RRR

Co-authored-by: lojack5 <1458329+lojack5@users.noreply.github.com>

---
## [Helg2/tgstation](https://github.com/Helg2/tgstation)@[527fb7b003...](https://github.com/Helg2/tgstation/commit/527fb7b0030d13fc11939d88030b1dc4772742a6)
#### Friday 2023-06-23 11:27:20 by DrTuxedo

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
## [Sisimshow/dnd5e-animations](https://github.com/Sisimshow/dnd5e-animations)@[4517495b28...](https://github.com/Sisimshow/dnd5e-animations/commit/4517495b28a02b3b62c4baf2a0a76718197ca959)
#### Friday 2023-06-23 11:27:31 by Sisimshow

1.4.0

Added the Advanced Melee Attack Macro by Jules to the D&D5e Animations Macros compendium so it can be used to add trails and other effects to weapons that use the new animations. Some example items have been added to a second compendium, look at the A-A settings of the items for the macro arguments.

New Animations

-Melee
--Baton
--Bone
--Butterfly
--Cutlass
--Dagger
--Katana
--Katar
--Knife
--Machete
--Naginata
--Ninjato
--Odachi (Nodachi also triggers it)
--Shield (excludes spells)
--Strike
--Tanto

-Ranged
--Antipathy/Sympathy
--Boomerang
--Kunai
--Missile
--Planar Binding
--Shuriken
--Snow Ball

-On Token
--Animate Objects
--Arcane/Bigby's Hand
--Arcane/Mordenkainen's Sword
--Awaken
--Clone
--Demiplane
--Faithful Hound
--Forbiddance
--Glibness
--Guards and Wards
--Magic Jar
--Magnificent Mansion
--Mass Heal
--Secret Chest
--Sequester
--Shapechange
--Simulacrum
--Transport via Plants
--Word of Recall

-Template
--Fabricate
--Forcecage
--Mass Cure Wounds
--Private Sanctum
--Reverse Gravity
--Spiritual Weapon (for SRD version)
--Storm of Vengeance
--Weird

Changed Animations

-Melee

--Scythe (animation)
--Sickle (animation)

-Ranged
--Bow (sound)
--Crossbow (sound)
--Gun (sound)
--Musket (sound)
--Revolver (sound)
--Rifle (sound)
--Pistol (sound)

-On Token
--Flame Blade (set to exact match)
--Green-Flame Blade (set to exact match)
--Heal (set to exact match)
--Spiritual Weapon (overhauled)

-Active Effects
--Shield (now excludes equipment)

Removed Animations

-On Token
--Shield (reduntant with Active Effect)

-Active Effects
--Charmed
--Deafended
--Frightened
--Grappled
--Incapacitated
--Paralyzed
--Poisoned
--Prone
--Restrained
--Stunned
--Unconscious

Most of the removals were status conditions that were added earlier that I'll admit were getting on my nerves and caused other problems so I wanted to remove them. You can add them yourself if you wish and they won't be overwritten, but they will no longer be in the module.

---
## [ljeremic4019rn/Banka-2-Frontend](https://github.com/ljeremic4019rn/Banka-2-Frontend)@[e30e4c744f...](https://github.com/ljeremic4019rn/Banka-2-Frontend/commit/e30e4c744fddac097755d84b5ce8277b963698f4)
#### Friday 2023-06-23 12:05:08 by dimitrijevich

But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure?

---
## [Nevaashahan/tourist-1](https://github.com/Nevaashahan/tourist-1)@[7d54343024...](https://github.com/Nevaashahan/tourist-1/commit/7d5434302480aca03554079da04402a82354fabe)
#### Friday 2023-06-23 12:49:44 by Tharmabalan Nevaashahan

Create README.md

Welcome to our GitHub project, where we aim to provide an innovative and comprehensive travel guide for developers and enthusiasts alike. Our project focuses on leveraging technology to enhance the travel experience, making it more convenient, immersive, and personalized.

With our open-source codebase, we invite developers to collaborate and contribute to the development of cutting-edge features and functionalities that will revolutionize the way people explore the world. By harnessing the power of data, APIs, and smart algorithms, we strive to create a platform that empowers travelers with real-time information, intelligent recommendations, and interactive maps.
Our project not only encompasses the backend infrastructure and data management but also includes user-friendly interfaces and intuitive user experiences. We believe in creating seamless interactions that adapt to individual preferences and provide a personalized journey for each traveler.

By integrating with various travel APIs and services, we aim to provide a comprehensive solution that covers everything from flight bookings and accommodation recommendations to local attractions and cultural insights. We envision a platform that brings together the best of both worlds: the convenience of modern technology and the authenticity of immersive travel experiences.
As an open-source project, we welcome developers to join our community and contribute their expertise in areas such as data analysis, machine learning, user interface design, and backend development. Together, we can shape the future of travel by creating a powerful and user-centric platform that inspires and guides travelers around the globe.
Join us on this exciting journey as we combine technology and wanderlust, creating a travel guide that not only facilitates exploration but also fosters a sense of discovery and connection with the world. Let's build the future of travel together!

---
## [JovannMC/ServerMC](https://github.com/JovannMC/ServerMC)@[bd8fc74cd5...](https://github.com/JovannMC/ServerMC/commit/bd8fc74cd5173a2f9c727d5cef4b6a02a415d467)
#### Friday 2023-06-23 14:00:34 by JovannMC

try to fix options not saving

please help ive been at this issue for hours i actualyl cant figure this out please holy crap im hgoing mentally insane why is this so annoying and jus tkillimg be brain please help hjow

---
## [finesse-fingers/terminal](https://github.com/finesse-fingers/terminal)@[f2ebb21bd1...](https://github.com/finesse-fingers/terminal/commit/f2ebb21bd13b20db38305136d34fa0778baf7920)
#### Friday 2023-06-23 14:17:32 by Mike Griese

Add snap-layouts support to the Terminal (#11680)

Adds snap layout support to the Terminal's maximize button. This PR is
full of BODGY, so brace yourselves.

Big thanks to Chris Swan in #11134 for building the prototype.
I don't believe this solves #8795, because XAML islands can't get
nchittest messages

- The window procedure for the drag bar forwards clicks on its client
  area to its parent as non-client clicks.
- BODGY: It also _manually_ handles the caption buttons. They exist in
  the titlebar, and work reasonably well with just XAML, if the drag bar
  isn't covering them.
- However, to get snap layout support, we need to actually return
  `HTMAXBUTTON` where the maximize button is. If the drag bar doesn't
  cover the caption buttons, then the core input site (which takes up
  the entirety of the XAML island) will steal the `WM_NCHITTEST` before
  we get a chance to handle it.
- So, the drag bar covers the caption buttons, and manually handles
  hovering and pressing them when needed. This gives the impression that
  they're getting input as they normally would, even if they're not
  _really_ getting input via XAML.
- We also need to manually display the button tooltips now, because XAML
  doesn't know when they've been hovered for long enough. Hence, the
  `_displayToolTip` `ThrottledFuncTrailing`

## Validation
Minimized, maximized, restored down, hovered the buttons slowly, moved
the mouse over them quickly, they feel the same as before. But now with
snap layouts appearing.

## TODO!
* [x] I'm working on getting the ToolTips on the caption buttons back. Alas, I needed a demo of this _today_, so I'll fix that tomorrow morning.
* [x] mild concern: I should probably test Win 10 to make sure there wasn't weird changes to the message loop in win11 that means this is broken on win10.
* [x] I think I used the wrong issue number for tons of my comments throughout this PR. Double check that. Should be #9443, not #9447. 

Closes #9443
I thought this took care of #8587 ~as a bonus, because I was here, and the fix is _now_ trivial~, but looking at the latest commit that regressed.

Co-authored-by: Chris Swan <chswan@microsoft.com>

---
## [finesse-fingers/terminal](https://github.com/finesse-fingers/terminal)@[442432ea15...](https://github.com/finesse-fingers/terminal/commit/442432ea15241a3e9ee3d70c5c24e5565655e55b)
#### Friday 2023-06-23 14:17:32 by Mike Griese

Fixes the wapproj fast-up-to-date check (#11806)

I'm working on making the FastUpToDate check in Vs work for the Terminal project. This is one of a few PRs in this area.

FastUpToDate lets vs check quickly determine that it doesn't need to do anything for a given project. 

However, a few of our projects don't produce all the right artifacts, or check too many things, and this eventually causes the `wapproj` to rebuild, EVERY TIME YOU F5 in VS. 

This third PR deals with the Actual fast up to date check for the CascadiaPackage.wapproj. When #11804, #11805 and this PR are all merged, you should be able to just F5 the Terminal in VS, and then change NOTHING, and F5 it again, without doing a build at all. 




The wapproj `GetResolvedWinMD` target tries to get a winmd from every cppwinrt
executable we put in the package. But we DON'T produce a winmd. This makes the
FastUpToDate check fail every time, and leads to the whole wapproj build
running even if you're just f5'ing the package. EVEN AFTER A SUCCESSFUL BUILD.

Setting GenerateWindowsMetadata=false is enough to tell the build system that
we don't produce one, and get it off our backs.

### teams chat where we figured this out

[3:38 PM] Dustin Howett
however, that's not the only thing that "GetTargetPath" checks.

[3:38 PM] Dustin Howett
oh yeah more info: wapproj calls GetTargetPath on all projects it references

[3:38 PM] Dustin Howett
when it calls GTP on WindowsTerminal.vcxproj it is getting back a winmd (!)


[3:39 PM] Dustin Howett
here's the magic

[3:39 PM] Dustin Howett
![image](https://user-images.githubusercontent.com/18356694/142945542-74734836-20d8-4f50-bf3a-be4e1170ae13.png)


[3:39 PM] Dustin Howett
it checks if any Link items specify GenerateWindowsMetadata

![image](https://user-images.githubusercontent.com/18356694/142945593-fd232243-0175-4653-8c34-cdc364a16031.png)

---
## [Rombuilding-X00TD/android_kernel_asus_sdm660](https://github.com/Rombuilding-X00TD/android_kernel_asus_sdm660)@[c46a0981dc...](https://github.com/Rombuilding-X00TD/android_kernel_asus_sdm660/commit/c46a0981dcb97f2cfe40b338d3ee8fcbc64fbb03)
#### Friday 2023-06-23 14:45:35 by Dave Chiluk

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
Signed-off-by: RyuujiX <saputradenny712@gmail.com>

---
## [yarnpkg/berry](https://github.com/yarnpkg/berry)@[ec7f37a8ca...](https://github.com/yarnpkg/berry/commit/ec7f37a8ca118a6f73f848e993272db957f286d6)
#### Friday 2023-06-23 14:52:58 by Maël Nison

Modernizes installs' output (#5509)

**What's the problem this PR addresses?**

I wasn't entirely happy with the Yarn output:

- When running `yarn add`, we have no way to know what packages are
actually added to the lockfile. The cache messages sometimes help, but
with zero-installs now being opt-in, in many cases the packages would
already be in the cache and thus wouldn't be displayed at all.

- The "can't be found in the cache and will be fetched from the remote
registry" messages were incredibly slow to print - the same install
would take 28s install for Gatsby on a local iTerm 2 without those logs,
vs almost 2 minutes with. They also weren't very useful: we were only
showing the last 5 of them, and with zero-installs being opt-in in many
cases they wouldn't be shown at all.

- The `node-gyp` warnings were for the most part unactionable (at best
the user would pin a fixed version in their `packageExtensions` field,
which I suspect no one ever did).

- The `deprecated` warnings were for the most part unactionable, and
only printed in very specific cases (the first time they were added to
the project).

- The "missing / invalid peer dependency" warnings were actionable, but
in practice no one really look at them except when something breaks -
and even then, it becomes unreadable when there are too many of them.

- The skipped build warnings were printed every single time you ran
`yarn install`. It's nice to know the first time, then it quickly
becomes redundant.

Fixes #4165

**How did you fix it?**

I went a little overboard and did everything in the same PR ... at first
I thought I wouldn't have to change unrelated parts, but then I finished
implementing the skipped build warnings duplicate removal and oh no 🙈

- Only peer dependency warnings caused by workspaces are now reporter.
They have also been moved inside the post-resolution validation step.
The resolution step is now expected to only do one of two things: either
report an error when the resolution fails, or report the packages which
got added / removed from the lockfile.

- The `node-gyp` warnings have been removed.

- The `deprecated` warnings have been removed from the install. The
`yarn npm audit` command now reports deprecated packages, although this
can be disabled using `--no-deprecations` (or any of the audit filtering
settings).

- The "can't be found in the cache" messages have been removed. Instead,
the fetch step will report the number of cache hits / cache misses once
it's finished (same behaviour as `preferAggregateCacheInfo`). The size
delta will also be reported.

- Packages whose build was skipped are now stored within
`Project#skippedBuilds`, which is stored within the install state file.
Warnings are only emitted if the install was skipped for the first time.
To see the messages again, users can run `yarn rebuild`.

- Added the Yarn version on installs. A bit because of branding when
screenshot are taken, but mostly so we easily know what version are
people using when they share screenshots to us. In a follow-up PR I'd
like to try to retrieve the latest version from the website, to let them
know once one is available.

**Checklist**
<!--- Don't worry if you miss something, chores are automatically
tested. -->
<!--- This checklist exists to help you remember doing the chores when
you submit a PR. -->
<!--- Put an `x` in all the boxes that apply. -->
- [x] I have read the [Contributing
Guide](https://yarnpkg.com/advanced/contributing).

<!-- See
https://yarnpkg.com/advanced/contributing#preparing-your-pr-to-be-released
for more details. -->
<!-- Check with `yarn version check` and fix with `yarn version check
-i` -->
- [x] I have set the packages that need to be released for my changes to
be effective.

<!-- The "Testing chores" workflow validates that your PR follows our
guidelines. -->
<!-- If it doesn't pass, click on it to see details as to what your PR
might be missing. -->
- [x] I will check that all automated PR checks pass before the PR gets
reviewed.

---
## [yarnpkg/berry](https://github.com/yarnpkg/berry)@[3626ea2ae3...](https://github.com/yarnpkg/berry/commit/3626ea2ae3e48ee26771b15b92292a28afe3d49d)
#### Friday 2023-06-23 14:52:58 by Maël Nison

Adds support for running native binaries without JS intermediaries (#5508)

**What's the problem this PR addresses?**

Yarn currently cannot run native binaries without going through a JS
jumper script. Other package managers don't have this restriction, and
it makes the `yarn run` overhead worse on some scripts for little
reasons - or doesn't work at all when packages don't use jumper scripts.

**How did you fix it?**

Two mechanisms are used:

- First we check for the binary extension
- Then we check its magic number

If one of the two match a predetermined list, the binary is spawned
without going through Node. This ensures that this logic is called only
when the binary is truly a native binary, and will not affect the
behaviour of other existing scripts.

**Checklist**
<!--- Don't worry if you miss something, chores are automatically
tested. -->
<!--- This checklist exists to help you remember doing the chores when
you submit a PR. -->
<!--- Put an `x` in all the boxes that apply. -->
- [x] I have read the [Contributing
Guide](https://yarnpkg.com/advanced/contributing).

<!-- See
https://yarnpkg.com/advanced/contributing#preparing-your-pr-to-be-released
for more details. -->
<!-- Check with `yarn version check` and fix with `yarn version check
-i` -->
- [x] I have set the packages that need to be released for my changes to
be effective.

<!-- The "Testing chores" workflow validates that your PR follows our
guidelines. -->
<!-- If it doesn't pass, click on it to see details as to what your PR
might be missing. -->
- [x] I will check that all automated PR checks pass before the PR gets
reviewed.

---
## [Stalkeros2/tgstation](https://github.com/Stalkeros2/tgstation)@[2aaafd9a67...](https://github.com/Stalkeros2/tgstation/commit/2aaafd9a67c270fa0772cd9beffb6789d53750e3)
#### Friday 2023-06-23 15:52:10 by TheVekter

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
## [yewentao256/pytorch](https://github.com/yewentao256/pytorch)@[ea384cd377...](https://github.com/yewentao256/pytorch/commit/ea384cd377e53a4f5c1ca99001dc072c11823828)
#### Friday 2023-06-23 17:27:10 by Mark Saroufim

torch.compiler public namespace (#102182)

# torch.compiler public API

## Goal

The goal of this document is to describe the public facing API for torchdynamo and torchinductor.

Today both dynamo and torchinductor are in `torch/_dynamo` and `torch/_inductor` namespace with the only public function

`torch.compile()` which is directly placed in `torch/__init__.py`

This poses a few problems for users trying to take dependencies on PyTorch 2.0
1. Unclear BC guarantees
2. No builtin discovery mechanism outside of reading the source code
3. No hard requirements for docstrings or type annotations

Most importantly it mixes two personas the PyTorch 2.0 developer vs the PyTorch 2.0 customer so this is an attempt to address this. We draw a lot of inspiration from the `functorch` migration to the `func` namespace.

## Alternate names

We did discuss some other alternative names

1. `torch.compile` -> problem is this would break BC on the existing `torch.compile` function
2. `torch.dynamo` -> `dynamo` is so far not something we've deliberately hidden from users but problem is now figuring out what it's `_dynamo` vs `dynamo` might be confusing
3. `torch.compiler` -> 1 would be better but to keep BC this is a good compromise

# The general approach
## Proposal 1
In https://github.com/pytorch/pytorch/blob/main/torch/_dynamo/__init__.py

We have function called `reset()`, this function is essential if users are trying to `torch.compile()` a model under different settings

```python
# in _dynamo/
def reset():
    do_reset_stuff()
```

Instead we propose

```python
# in compiler/
def reset():
    do_reset_stuff() # As in copy paste the logic from _dynamo.reset

# in _dynamo/
import warnings
import inspect

def reset():
    function_name = inspect.currentframe().f_code.co_name
    warnings.warn(f"{function_name} is deprecated, use compiler.{function_name} instead", DeprecationWarning)
    return compiler.reset()

```
## Proposal 2

```python
# in compiler/
def reset():
    “””
    Docstrings here
    “””
    _dynamo.reset()

# in _dynamo/
No changes
```
Consensus so far seems to be proposal 2 since fewer warnings will be less jarring and it’ll make it quite easy to merge the public API

## Docstrings

The above was an example of a function that has no inputs or outputs but there are other functions which could use an improvement in their docstrings, for example allow_in_graph actually works over lists of functions but that’s not mentioned anywhere in the example only if you read the source code.

def allow_in_graph(fn):
    """
    Customize which functions TorchDynamo will include in the generated
    graph. Similar to `torch.fx.wrap()`.

    Parameters:
        fn (callable or list/tuple): The function(s) to be allowed in the graph.

    Returns:
        callable or list/tuple: The input function(s) included in the graph.

    Examples:
        Customize inclusion of a single function:
        ::
            torch._dynamo.allow_in_graph(my_custom_function)

        Customize inclusion of multiple functions:
        ::
            torch._dynamo.allow_in_graph([my_custom_function1, my_custom_function2])

        @torch._dynamo.optimize(...)
        def fn(a):
            x = torch.add(x, 1)
            x = my_custom_function(x)
            x = torch.add(x, 1)
            return x

        fn(...)

    Notes:
        The `allow_in_graph` function allows customization of which functions TorchDynamo
        includes in the generated graph. It can be used to include specific functions that
        are not automatically captured by TorchDynamo.

        If `fn` is a list or tuple, `allow_in_graph` will be called recursively on each
        element in the sequence.

        Once a function is allowed in the graph using `allow_in_graph`, it will be captured
        in the graph generated by TorchDynamo. This customization enables more fine-grained
        control over the functions included in the graph.

        Note that `allow_in_graph` expects the input `fn` to be a callable.

    """
    if isinstance(fn, (list, tuple)):
        return [allow_in_graph(x) for x in fn]
    assert callable(fn), "allow_in_graph expects a callable"
    allowed_functions._allowed_function_ids.add(id(fn))
    allowed_functions._disallowed_function_ids.remove(id(fn))
    return fn

So to make the API public, we’d have to write similar docstrings for all public functions we’d like to create.

The benefit of this approach is that
1. No BC risks, internal and external users relying on our tooling can slowly wean off the private functions.
2. We will also have to write correct docstrings which will automatically make our documentation easier to maintain and render correctly on pytorch.org
3. We already have some BC guarantees already, we don’t kill OptimizedModule, we rejected the PR to change the config system

The con of this approach is that
Will be stuck with some potentially suboptimal functions/classes that you can’t kill

## Testing strategy
If the approach is to mostly make a public function call an already tested private function then all we need to do is ensure that the function signatures don't change

## Which functions should be in the public API

Our heuristic for deciding whether something should be public or not is are users already relying on it for lack of other options or have we recommended some non public functions for users to debug their PT 2.0 programs.

Heuristic for not putting something in public is that it’s an experimental subsystem with the goal of turning it on by default, it’s very core dev centric, meta centric, a bunch of different configs that should be batched into a single user facing one, or something that needs to be renamed because the name is confusing

#### Top level
`torch.compile()` -> already is a public API it does require some minor improvements like having configs be passed in to any backend and not just inductor (EDIT: This was already done https://github.com/pytorch/pytorch/pull/99645l) and renaming `mode=reduce-overhead` to `mode=cudagraph`

To make sure that PT 2.0 is supported with a given pytorch version users can create a new public function and this would replace the need for `try/except` blocks around `import torch._dynamo` that has been populating user code.

```python
def pt2_enabled():
    if hasattr(torch, 'compile'):
        return True
    else:
        return False
```

For all of the below they will be translated to `torch.compiler.function_name()`

#### From _dynamo

As a starting point we looked at https://github.com/pytorch/pytorch/blob/main/torch/_dynamo/__init__.py and we suggest redefining these functions in `pytorch/torch/compiler/__init__.py`

It might also make sense to split them over multiple files and import them in `__init__.py` but because the number of functions is small it'd probably be fine to add them all into a single compiler/__init__.py until this list becomes larger

1. `reset()`
2. `allow_in_graph()`
10. `list_backends()`
12. `compile()`:  torch.compile() would be mostly a shell function passing arguments to torch.compiler.compile()
13. `assume_constant_result()`: TODO: Double check how this is useful
15. `torch._dynamo.disable()`

Some notable omissions
11. `explain()`: We need to clean up the output for this function, make it a data class and pretty printable
1. `forbid_in_graph()`: Considered adding this but should instead consolidate on `disallow_in_graph`
2. `optimize_assert()`: Already covered by `torch.compile(fullgraph=True)`
3. `check_if_dynamo_supported()`: this would be supplanted by pt2_enabled()
4. `compilation_metrics`, `graph_breaks_reasons` ..: would all be accessed via `torch.compiler.explain()`
5. `replay` does not seem useful to end customers
6. . `graph_break()`: Mostly useful for debugging or unit tests
9. `register_backend()`: End users will just pass a string backend to torch.compile, only devs will create new backends
10. `export()` : Eventually this needs to public but for now it’s not ready so just highlighting that it will be in the public API eventually
11. `disallow_in_graph()`: Usage is limited
12. `mark_static()`: we can keep this private until dynamic=True is recommended in stable
13. `mark_dynamic()`:  we can keep this private until dynamic=True is recommended in trunk
14. 8. `OptimizedModule`: This is the only class that we'd expose but is crucial since users are running code like `if isinstance(mod, OptimizedModule): torch.save(mod._orig_mod)` EDIT: because we fixed pickling we no longer need to
expose this
15. `is_compiling()`: Still not clear how this useful to end users

There are also config variables which we need to expose https://github.com/pytorch/pytorch/blob/main/torch/_dynamo/config.py

Some of our configs are useful dev flags, others are to gate experimental functionality and others are essential debugging tools and we seperate out the essential debugging and logging tools to a public facing config.

TODO: I still need to think of a good way of porting the config in a BC way here are some ideas
1. Just make all passes available and controllable via `torch.compile(options={})` but only show docstrings for the ones users should care about.

The current problem with our config system is we have 3 ways of setting them once via `options={}`, environment variables and variables in `config.py`, it'd be worth settling on one source of truth and have that be the public API.

The configs we should make public are
1. `log_file_name`
2. `verbose`
3. `cache_size_limit`
4. `repro_level` and `repro_after`: Although we can rename these to minifier and give human readable names to the levels

Everything else should stay private in particular

1. `print_graph_breaks`, `print_specializations`: should be supplanted by `explain()` for public users
2. dynamic shape configs : Users should only have to worry about `torch.compile(dynamic=True/False)`
3. The distributed flags, hook or guard configs: If we tell a user to use FSDP and DDP then the flag should be enabled by default or be in a private namespace
4. The fbcode flags: Obviously no need to be user facing
5. Skip/Allow lists: Not something normal users should play around with

#### From _inductor
Very little of inductor should be exposed in a public facing API, our core audience as in people writing models mostly just need information on what certain passes mean and how to control them a high level and they can do this with `torch.compile(options={})` so the goal here should be more to make available passes clearer and ideally consolidate them into `torch.compile()` docstrings or modes.

There are some exceptions though from https://github.com/pytorch/pytorch/blob/main/torch/_inductor/__init__.py

1. `list_mode_options()`
2. `list_options()`: this needs an additional pass to hide internal or debug options

For both of these we’d rename them to compiler.inductor_list_mode_options and compiler.inductor_list_options() since they would be in the same init file as the one for dynamo

Notable omissions
1. `_inductor.compile()`: Because of users are coming in with their own fx graph, they are likely developers
2. `_inductor.aot_compile()`:Again this is about capturing and modifying fx graphs so users APIs don't need to be public

However the configs are a slightly different story, because we can choose to either
1. Make all configs public
2. Make some configs public and keep most of the private ones. If public config is set it should override the private version
3. Make all configs controllable via `torch.compile(options={})` but make list_options() hide more things

For now 3 seems like the most reasonable choice with some high level configs we’ll keep like TORCH_COMPILE_DEBUG

Regardless here's what should probably be public or advertised more
1. `disable_progress` and verbose_progress:  Combine and enable by default
2. `fallback_random`: We could make the case this shouldn't be public if a top level deterministic mode enables this
3. `profile_bandwidth`: Or could make the case that this should be in TORCH_COMPILE_DEBUG

Notable omissions
1. Any config that would generally improve performance for most that we should probably enable by default but might be disabled in the short term because of stability: example `epilogue_fusion`, `pattern_matcher`, `reordering`
2. Autotuning flags: Should just sit behind `torch.compile(mode="max-autotune")` like `max_autotune`, `max_autotune_gemm`
3. `coordinate_descent_tuning`: This one I'm a but mixed about, maybe it just also fall into `mode="max-autotune"`
4. `trace`: `TORCH_COMPILE_DEBUG` is the best flag for all of this
5. `triton.cudagraphs`: Default should be `torch.compile(mode="reduce-overhead")` - I'd go further and rename the `mode=cudagraph` and we can keep reduce-overhead for BC reasons
6. `triton_unique_kernel_names`: Mostly useful for devs debugging
7. `dce`: which doesnt really do anything
8. `shape_padding`: Elias is working on enabling this by default in which case we also remove it

## Mechanics

This PR would include the public functions with their docstrings

Another PR will take a stab at the configs

And for work where the APIs are still being cleaned up whether its minifier or escape hatches, export or dynamic shapes, aot_inductor etc.. we’ll keep them private until a public commitment can be made

Pull Request resolved: https://github.com/pytorch/pytorch/pull/102182
Approved by: https://github.com/jansel, https://github.com/albanD

---
## [bgamez23/15-3athena](https://github.com/bgamez23/15-3athena)@[d6850638e9...](https://github.com/bgamez23/15-3athena/commit/d6850638e90fb594d5b94547acf777e9ba9da1ae)
#### Friday 2023-06-23 18:03:04 by 15peaces

== Skills & more ==
=General:
*Merged missing changes from 3ceam rev. 860

*Added official 2013 halloween event.

*Script command sscanf will now return -1 when a string is empty.

*Corrected a typo in a message related to push carts.

*Fixed a issue with the "allskills" command where it may not appear to give you all the skills accessable by your job. This is needed due to the normalize job skilltree recode.

*pc_normalize_job_max_skillpoint
-Added support for ths function.
-This works with the normalizing of jobs to set how many skill points should be invested into certain skills in a skill tree depending on the job since the max job level is different between jobs.

*pc_calc_skilltree_normalize_job
-Recoded the function to properly work for 3rd jobs.
-Note: This was so broken. I had to reverted it back to the original eAthena code and then update it to the way it should be. Wasn't easy.

*pc_search_job_skilltree
-Added support for this function.
-This replaces "pc_isSkillFromJob" and is a recode of it.

*pc_skillup
-Recoded the checks and message handling for telling the player how many skill points need to be placed into lower tier skills. This is also part of the reason "pc_calc_skilltree_normalize_job" was recoded. Having to update the skill range
-check every time new 3rd job skills come out is annoying. Better to let the normalize_job and search_job_skilltree functions work together for this.

*pc_jobchange
-Removed JOBL_THIRD from the upper setting switch.
-Third jobs are not a alternate version of 2nd jobs. Its a higher tier, making it its own job.

*Updated "pc_msg" and "msg_skill" MSG names with official ones.

*cooldown_rate; min_skill_cooldown_limit; no_skill_cooldown
-Added these config settings to the skill.conf file.

*Fixed a issue where some status's that deal damage and shows it will not show the damage done on the enemy if its a killing blow.

*Autocasted skills will no longer trigger a cooldown on renewal era skills.

*skill_cooldownfix
-Added support for this function.
-This function is kinda like skill_delayfix, but for cooldowns.
-At the moment its functional enough to allow cooldown time adjustments through status's but will be updated later to work with equip bonuses.

=Skills:
*WS_WEAPONREFINE
-Updated refine chance bonus gained from JobLV's to official.
-JobLV will not affect the success chance when below 50.
-When above 50, it will add a 0.5% chance bonus for each level above 50.
-This brings the added success chance to 10% at JobLV 70.
-Mechanics now get the full 10% added chance bonus no matter the JobLV.

*LG_BANDING
-Fixed a issue where using the skill under certain conditions would crash the server.

*WM_METALICSOUND
-Fixed a issue where it didn't deal bonus damage on sleeping targets.
-Now displays SP damage as blue numbers.

*GN_ILLUSIONDOPING
-Fixed a issue where casting the skill didn't require alcohol.

*SJ_STAREMPEROR
*SJ_NOVAEXPLOSING
*SJ_BOOKOFDIMENSION
*SJ_BOOKOFCREATINGSTAR
*SJ_GRAVITYCONTROL
-Added support for these skills.

*SJ_FALLINGSTAR_ATK
-The AoE size for the stellar mark check is now 5x5.
-Note: Sucks that its this small but its confirmed official.

*SJ_PROMINENCEKICK
-Now deals 2 hits.
-The first hit is the main damage. The second hit is the 100% fire damage.

*SJ_SUNSTANCE
*SJ_LUNARSTANCE
*SJ_STARSTANCE
*SJ_UNIVERSESTANCE
-Switching or disabling stances now removes status's given from skills exclusive to the previously active stance.

*SP_SOULDIVISION
-Adjusted map check code.

*SP_SOULEXPLOSION
-Now only usable in PVP type maps.

---
## [omarsilva1/mypy-1](https://github.com/omarsilva1/mypy-1)@[0873230ee6...](https://github.com/omarsilva1/mypy-1/commit/0873230ee60461110bd7bfde7ca3886878aae389)
#### Friday 2023-06-23 20:07:35 by Ivan Levkivskyi

Foundations for non-linear solver and polymorphic application (#15287)

Fixes #1317
Fixes #5738
Fixes #12919 
(also fixes a `FIX` comment that is more than 10 years old according to
git blame)

Note: although this PR fixes most typical use-cases for type inference
against generic functions, it is intentionally incomplete, and it is
made in a way to limit implications to small scope.

This PR has essentially three components (better infer, better solve,
better apply - all three are needed for this MVP to work):
* A "tiny" change to `constraints.py`: if the actual function is
generic, we unify it with template before inferring constraints. This
prevents leaking generic type variables of actual in the solutions
(which makes no sense), but also introduces new kind of constraints `T
<: F[S]`, where type variables we solve for appear in target type. These
are much harder to solve, but also it is a great opportunity to play
with them to prepare for single bin inference (if we will switch to it
in some form later). Note unifying is not the best solution, but a good
first approximation (see below on what is the best solution).
* New more sophisticated constraint solver in `solve.py`. The full
algorithm is outlined in the docstring for `solve_non_linear()`. It
looks like it should be able to solve arbitrary constraints that don't
(indirectly) contain "F-bounded" things like `T <: list[T]`. Very short
the idea is to compute transitive closure, then organize constraints by
topologically sorted SCCs.
* Polymorphic type argument application in `checkexpr.py`. In cases
where solver identifies there are free variables (e.g. we have just one
constraint `S <: list[T]`, so `T` is free, and solution for `S` is
`list[T]`) it will apply the solutions while creating new generic
functions. For example, if we have a function `def [S, T] (fn:
Callable[[S], T]) -> Callable[[S], T]` applied to a function `def [U]
(x: U) -> U`, this will result in `def [T] (T) -> T` as the return.

I want to put here some thoughts on the last ingredient, since it may be
mysterious, but now it seems to me it is actually a very well defined
procedure. The key point here is thinking about generic functions as
about infinite intersections or infinite overloads. Now reducing these
infinite overloads/intersections to finite ones it is easy to understand
what is actually going on. For example, imagine we live in a world with
just two types `int` and `str`. Now we have two functions:
```python
T = TypeVar("T")
S = TypeVar("S")
U = TypeVar("U")

def dec(fn: Callable[[T], S]) -> Callable[[T], S]: ...
def id(x: U) -> U: ...
```
the first one can be seen as overload over
```
((int) -> int) -> ((int) -> int)  # 1
((int) -> str) -> ((int) -> str)  # 2
((str) -> int) -> ((str) -> int)  # 3
((str) -> str) -> ((str) -> str)  # 4
```
and second as an overload over
```
(int) -> int
(str) -> str
```
Now what happens when I apply `dec(id)`? We need to choose an overload
that matches the argument (this is what we call type inference), but
here is a trick, in this case two overloads of `dec` match the argument
type. So (and btw I think we are missing this for real overloads) we
construct a new overload that returns intersection of matching overloads
`# 1` and `# 4`. So if we generalize this intuition to the general case,
the inference is selection of an (infinite) parametrized subset among
the bigger parameterized set of intersecting types. The only question is
whether resulting infinite intersection is representable in our type
system. For example `forall T. dict[T, T]` can make sense but is not
representable, while `forall T. (T) -> T` is a well defined type. And
finally, there is a very easy way to find whether a type is
representable or not, we are already doing this during semantic
analyzis. I use the same logic (that I used to view as ad-hoc because of
lack of good syntax for callables) to bind type variables in the
inferred type.

OK, so here is the list of missing features, and some comments on them:
1. Instead of unifying the actual with template we should include
actual's variables in variable set we solve for, as explained in
https://github.com/python/mypy/issues/5738#issuecomment-511242682. Note
however, this will work only together with the next item
2. We need to (iteratively) infer secondary constraints after linear
propagation, e.g. `Sequence[T] <: S <: Sequence[U] => T <: U`
3. Support `ParamSpec` (and probably `TypeVarTuple`). Current support
for applying callables with `ParamSpec` to generics is hacky, and kind
of dead-end. Although `(Callable[P, T]) -> Callable[P, List[T]]` works
when applied to `id`, even a slight variation like `(Callable[P,
List[T]]) -> Callable[P, T]` fails. I think it needs to be re-worked in
the framework I propose (the tests I added are just to be sure I don't
break existing code)
4. Support actual types that are generic in type variables with upper
bounds or values (likely we just need to be careful when propagating
constraints and choosing free variable within an SCC).
5. Add backtracking for upper/lower bound choice. In general, in the
current "Hanoi Tower" inference scheme it is very hard to backtrack, but
in in this specific choice in the new solver, it should be totally
possible to switch from lower to upper bound on a previous step, if we
found no solution (or `<nothing>`/`object`).
6. After we polish it, we can use the new solver in more situations,
e.g. for return type context, and for unification during callable
subtyping.
7. Long term we may want to allow instances to bind type variables, at
least for things like `LRUCache[[x: T], T]`. Btw note that I apply force
expansion to type aliases and callback protocols. Since I can't
transform e.g. `A = Callable[[T], T]` into a generic callable without
getting proper type.
8. We need to figure out a solution for scenarios where non-linear
targets with free variables and constant targets mix without secondary
constraints, like `T <: List[int], T <: List[S]`.

I am planning to address at least majority of the above items, but I
think we should move slowly, since in my experience type inference is
really fragile topic with hard to predict long reaching consequences.
Please play with this PR if you want to and have time, and please
suggest tests to add.

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[91042af535...](https://github.com/TaleStation/TaleStation/commit/91042af535507720e43120f8c00cfa270d250843)
#### Friday 2023-06-23 20:39:57 by TaleStationBot

[MIRROR] [MDB IGNORE] Adds border smoothing! (Look ma I'm upstreaming) (#6375)

Original PR: https://github.com/tgstation/tgstation/pull/76134
-----

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

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [KLB7/IntraMine](https://github.com/KLB7/IntraMine)@[3d4bee601d...](https://github.com/KLB7/IntraMine/commit/3d4bee601d75239b56a5fbf53b7a57eaee6f0123)
#### Friday 2023-06-23 21:08:10 by KLB7

File Watcher installation updated

The File Watcher service (original at https://sourceforge.net/projects/fwutilities/files/) can now be installed by copying the "fwws" folder included with IntraMine instead of going to SourceForge. The IntraMine copy has a modifed .config file, suitable for use with IntraMine. Aside from simplifying the installation a bit, this approach removes an error where sometimes the fwatcher.xsd file was missing - I don't know how that happened, honestly, but at least it's included for sure in the IntraMine copy. If you have installed IntraMine and found that your files weren't being re-indexed when changed, check to see if fwatcher.xsd is in your C:\fwws folder: if not, try copying fwatcher.xsd from IntraMine's fwws folder to your C:\fwws folder and then start File Watcher at a command prompt (Run as Administrator) with
sc start "File Watcher Windows Service"
.
For the new installation approach see "Installing File Watcher.txt" in the Documentation folder.

P.S. in the previous commit I referred to the Elasticsearch parameter "force_field" when I meant "force_source", sorry about that. I my defense I had just built a new computer, and the experience temporarily cost me much of my patience (as well as exhausting my vocabulary that expresses lack of patience).

---
## [michaelScopic/michaelScopic](https://github.com/michaelScopic/michaelScopic)@[ca37443e98...](https://github.com/michaelScopic/michaelScopic/commit/ca37443e98f6bcc2ad972d88cea7c925bcd63630)
#### Friday 2023-06-23 21:16:43 by Michael_Scopic

I hate this stupid ass discord update i fucking hate you discord

---
## [aitechforgeCEO/evals](https://github.com/aitechforgeCEO/evals)@[170dfd886c...](https://github.com/aitechforgeCEO/evals/commit/170dfd886c0704588461af075393cc20cfb0480f)
#### Friday 2023-06-23 21:31:44 by Robert Bateman

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
## [aitechforgeCEO/evals](https://github.com/aitechforgeCEO/evals)@[24dae81ae0...](https://github.com/aitechforgeCEO/evals/commit/24dae81ae06ebc70808690c7a147f2710e3e54bf)
#### Friday 2023-06-23 21:31:44 by Yohei Inui

Compare countries by area (#623)

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
Compare countries by area

### Eval description

Test the model's ability to determine which country has the largest area

### What makes this a useful eval?

The model should be able to factually determine which country has the
largest area based on accurate facts.
In this eval we use The World
Factbook(https://www.cia.gov/the-world-factbook/field/area/country-comparison)
that is prepared by the CIA for the use of U.S. government officials,
and four countries with similar sizes are compared to each other.
Specifically, four countries adjacent to each other in area ranking are
presented as one option, and the dataset Includes data for countries
ranked 1\~4, 2\~5, ... 100\~103. However, we excluded countries where
sources and interpretations could cause fluctuations in rankings (e.g.,
China and Pakistan). This data set achieved less than 40% accuracy for
both gpt-4 and gpt-3.5-turbo, and the results tend to be worse for
comparisons between countries with smaller areas.

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
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. Russia, Canada, United
States, Brazil"}], "ideal": "Russia"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. Canada, United States,
Brazil, Australia"}], "ideal": "Canada"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. United States, Brazil,
Australia, India"}], "ideal": "United States"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. Brazil, Australia, India,
Argentina"}], "ideal": "Brazil"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. Australia, India, Argentina,
Kazakhstan"}], "ideal": "Australia"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. India, Argentina, Kazakhstan,
Algeria"}], "ideal": "India"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. Argentina, Kazakhstan,
Algeria, Democratic Republic of the Congo"}], "ideal": "Argentina"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "You are presented with
several countries. Answer the name of the country with the largest area
among the given countries. Do not explain. Kazakhstan, Algeria,
Democratic Republic of the Congo, Saudi Arabia"}], "ideal":
"Kazakhstan"}
  ```
</details>

---------

Co-authored-by: 乾陽平 <inuiyouhei@inuiyouheinoMacBook-Pro.local>

---
## [aitechforgeCEO/evals](https://github.com/aitechforgeCEO/evals)@[ef1f0ebe0e...](https://github.com/aitechforgeCEO/evals/commit/ef1f0ebe0e9f4674bc42ed0af5e6c052f0539700)
#### Friday 2023-06-23 21:31:44 by Josh Gruenstein

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
## [aitechforgeCEO/evals](https://github.com/aitechforgeCEO/evals)@[2ffd4b57de...](https://github.com/aitechforgeCEO/evals/commit/2ffd4b57deaeced1fde54744da9de62d3eb7738a)
#### Friday 2023-06-23 21:31:44 by Andrew Kondrich

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
## [Jolly-66/tgstation](https://github.com/Jolly-66/tgstation)@[64eae49042...](https://github.com/Jolly-66/tgstation/commit/64eae49042dea956b46ae013a0c96a891c026a7f)
#### Friday 2023-06-23 21:40:12 by necromanceranne

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
## [douglasmonsky/evals](https://github.com/douglasmonsky/evals)@[e116ede848...](https://github.com/douglasmonsky/evals/commit/e116ede848957eff8e76b5d8463ed5291163a28f)
#### Friday 2023-06-23 21:43:50 by Wesley Barlow

Add eval: rhetorical-devices (#1005)

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
rhetorical-devices

### Eval description

Evaluates model's ability to select the most specific rhetorical
modification of a sentence from a multiple choice with a large number of
nuanced rhetorical devices.

### What makes this a useful eval?

Useful for using LLMs to write novels and generate consistent/parametric
authorial tone.

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
{"input": [{"role": "system", "content":"Which of the following
rhetorical devices was added to the original sentence? Choose the most
specific of the following (a) Alliteration, (b) Assonance, (c)
Consonance, (d) Cacophony, (e) Onomatopoeia, (f) Anadiplosis, (g)
Conduplicatio, (h) Anaphora, (i) Epistrophe, (j) Symploce, (k)
Epanalepsis, (l) Epizeuxis, (m) Antanaclasis, (n) Diacope, (o)
Antithesis, (p) Antimetabole, (q) Chiasmus, (r) Asyndeton, (s)
Polysyndeton, (t) Catacosmesis, (u) Oxymoron, (v) Zeugma"}, {"role":
"user", "content": "ORIGINAL She likes to listen to the winds. MODIFIED
She swoons at such sweet gales. Answer in the format (x) Rhetorical"}],
"ideal": "(a) Alliteration"}
{"input": [{"role": "system", "content":"Which of the following
rhetorical devices was added to the original sentence? Choose the most
specific of the following (a) Alliteration, (b) Assonance, (c)
Consonance, (d) Cacophony, (e) Onomatopoeia, (f) Anadiplosis, (g)
Conduplicatio, (h) Anaphora, (i) Epistrophe, (j) Symploce, (k)
Epanalepsis, (l) Epizeuxis, (m) Antanaclasis, (n) Diacope, (o)
Antithesis, (p) Antimetabole, (q) Chiasmus, (r) Asyndeton, (s)
Polysyndeton, (t) Catacosmesis, (u) Oxymoron, (v) Zeugma"}, {"role":
"user", "content": "ORIGINAL The rock was very large. MODIFIED The rock
was remarkably raised. Answer in the format (x) Rhetorical"}], "ideal":
"(a) Alliteration"}
{"input": [{"role": "system", "content":"Which of the following
rhetorical devices was added to the original sentence? Choose the most
specific of the following (a) Alliteration, (b) Assonance, (c)
Consonance, (d) Cacophony, (e) Onomatopoeia, (f) Anadiplosis, (g)
Conduplicatio, (h) Anaphora, (i) Epistrophe, (j) Symploce, (k)
Epanalepsis, (l) Epizeuxis, (m) Antanaclasis, (n) Diacope, (o)
Antithesis, (p) Antimetabole, (q) Chiasmus, (r) Asyndeton, (s)
Polysyndeton, (t) Catacosmesis, (u) Oxymoron, (v) Zeugma"}, {"role":
"user", "content": "ORIGINAL Visionary dreams elevate me at night.
MODIFIED Visionary reminitions elevate self resting in lightlessness.
Answer in the format (x) Rhetorical"}], "ideal": "(b) Assonance"}
{"input": [{"role": "system", "content":"Which of the following
rhetorical devices was added to the original sentence? Choose the most
specific of the following (a) Alliteration, (b) Assonance, (c)
Consonance, (d) Cacophony, (e) Onomatopoeia, (f) Anadiplosis, (g)
Conduplicatio, (h) Anaphora, (i) Epistrophe, (j) Symploce, (k)
Epanalepsis, (l) Epizeuxis, (m) Antanaclasis, (n) Diacope, (o)
Antithesis, (p) Antimetabole, (q) Chiasmus, (r) Asyndeton, (s)
Polysyndeton, (t) Catacosmesis, (u) Oxymoron, (v) Zeugma"}, {"role":
"user", "content": "ORIGINAL Once, I thought I had lost her pet.
MODIFIED Once, dunce — thought I lost Juliet's pet. Answer in the format
(x) Rhetorical"}], "ideal": "(b) Assonance"}
{"input": [{"role": "system", "content":"Which of the following
rhetorical devices was added to the original sentence? Choose the most
specific of the following (a) Alliteration, (b) Assonance, (c)
Consonance, (d) Cacophony, (e) Onomatopoeia, (f) Anadiplosis, (g)
Conduplicatio, (h) Anaphora, (i) Epistrophe, (j) Symploce, (k)
Epanalepsis, (l) Epizeuxis, (m) Antanaclasis, (n) Diacope, (o)
Antithesis, (p) Antimetabole, (q) Chiasmus, (r) Asyndeton, (s)
Polysyndeton, (t) Catacosmesis, (u) Oxymoron, (v) Zeugma"}, {"role":
"user", "content": "ORIGINAL Do you want to understand research on
artificial general intelligence? MODIFIED Don't you want to investigate
artifacts of artificial general intelligence? Answer in the format (x)
Rhetorical"}], "ideal": "(c) Consonance"}
  ```
</details>

---
## [douglasmonsky/evals](https://github.com/douglasmonsky/evals)@[b91292c803...](https://github.com/douglasmonsky/evals/commit/b91292c803af2bdadeec3853ab03514b73310109)
#### Friday 2023-06-23 21:43:50 by Zyenith

Add Eval: Internal Representations via Counting (#1006)

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
Internal representations via counting

### Eval description

Using series of logical questions that require multiple (simple)
manipulations of numbers to get the ideal answer. These are basic tasks
that should be doable by an LLM, but require several steps of internal
"thought" to get right.

### What makes this a useful eval?

Situations with number manipulation with multiple steps are prevalent
anywhere in the modern world. Testing the internal representation of the
LLM can provide other insights on how well its "mind" processes
information.

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

This eval is capable of providing insight into the LLM's internal
representation of objects versus answering fact-based questions or
straightforward complex logic puzzles.

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
{"input":[{"role":"system","content":"You will be prompted with a
logical question. Respond only with a number, nothing else is
required."},{"role":"user","content":"Roger and Emily are in a room.
Roger puts a cat in an empty box while Emily is in the room. They both
leave, and Emily returns and puts a turtle in the box as well. How many
items does Roger think are in the box?"}],"ideal":"1"}
{"input":[{"role":"system","content":"You will be prompted with a
logical question. Respond only with a number, nothing else is
required."},{"role":"user","content":"There are four darts already on a
dart board. Bob throws one dart at the dartboard, and it lands. Alice
throws two darts, and one misses but one hits the dartboard. How many
darts are on the dartboard?"}],"ideal":"6"}
{"input":[{"role":"system","content":"You will be prompted with a
logical question. Respond only with a number, nothing else is
required."},{"role":"user","content":"A bakery sold 25 cakes in the
morning and 17 cakes in the afternoon. The day after, they sold 15 more
cakes. How many cakes did they sell on the second day?"}],"ideal":"15"}
{"input":[{"role":"system","content":"You will be prompted with a
logical question. Respond only with a number, nothing else is
required."},{"role":"user","content":"There are six blue birds and three
red birds sitting on a tree. Two blue birds fly away, and one red bird
flies away. How many birds are left on the tree?"}],"ideal":"6"}
{"input":[{"role":"system","content":"You will be prompted with a
logical question. Respond only with a number, nothing else is
required."},{"role":"user","content":"John has double the amount of
pencils than Sarah, and Sarah has as many pencils as Mark. Mark has 2
pencils. How many pencils does John have?"}],"ideal":"4"}
  ```
</details>

---
## [douglasmonsky/evals](https://github.com/douglasmonsky/evals)@[3d9de9a624...](https://github.com/douglasmonsky/evals/commit/3d9de9a62411f9e6a999e96ce8f07eebf0e8c121)
#### Friday 2023-06-23 21:43:50 by dyar-al-ashtari

Eval Norwegian lexicon (#1044)

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
`norwegian-lexicon`

### Eval description

This eval uses valid Norwegian words taken from the dictionary and
assesses whether GPT can recognize them as valid.

### What makes this a useful eval?

The Norwegian language is simple yet complicated at the same time. There
are a lot of words that are valid Norwegian words that do not get
recognized anymore. An AI should be able to identify these words with
precision. All of the words used in the samples are valid Norwegian
words and can be found in the dictionary. After assessing GPT-4 (through
the playground) and GPT-3.5 -- it failed to recognize most of the words.
Some of the words would return positive during some evals. Other times
it wouldn't recognize them. After asking GPT why it is not a valid word,
it would apologize and fix its mistake.

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
{"input":[{"role":"system","content":"You will be prompted with a single
word. Does this word exist in the Norwegian language? Answer with
exactly one letter: Y or N. Do not use punctionation. Do not explain
your answer."},{"role":"user","content":"Skarpne"}],"ideal":"Y"}
{"input":[{"role":"system","content":"You will be prompted with a single
word. Does this word exist in the Norwegian language? Answer with
exactly one letter: Y or N. Do not use punctionation. Do not explain
your answer."},{"role":"user","content":"Bløtne"}],"ideal":"Y"}
{"input":[{"role":"system","content":"You will be prompted with a single
word. Does this word exist in the Norwegian language? Answer with
exactly one letter: Y or N. Do not use punctionation. Do not explain
your answer."},{"role":"user","content":"Hovedantall"}],"ideal":"Y"}
{"input":[{"role":"system","content":"You will be prompted with a single
word. Does this word exist in the Norwegian language? Answer with
exactly one letter: Y or N. Do not use punctionation. Do not explain
your answer."},{"role":"user","content":"Klenge"}],"ideal":"Y"}
{"input":[{"role":"system","content":"You will be prompted with a single
word. Does this word exist in the Norwegian language? Answer with
exactly one letter: Y or N. Do not use punctionation. Do not explain
your answer."},{"role":"user","content":"Blankolov"}],"ideal":"Y"}
  ```
</details>

---
## [douglasmonsky/evals](https://github.com/douglasmonsky/evals)@[6a37c9b51b...](https://github.com/douglasmonsky/evals/commit/6a37c9b51b48a2f735898846cfb08b37cbd63179)
#### Friday 2023-06-23 21:43:50 by Aaron Goldsmith

[eval] 3x3 Game Of Life  (#345)

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
GOL

### Eval description

Determine the next state of a 3x3 Game of Life Board. 

### What makes this a useful eval?

Spacial reasoning

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
{"input": [{"role": "system", "content": "You are a helpful assistant.
"}, {"role": "user", "content": "Using the classic Game of Life Rules,
determine the next state of the 3x3 Game of life board: \n1 1 1\n\n0 0
0\n\n0 0 0 \n\n Do not provide any explanation other than the next state
of the board. e.g 0 0 0\n\n0 0 0\n\n0 0 0"}], "ideal": ["0 1 0\n\n0 1
0\n\n0 0 0"]}
{"input": [{"role": "system", "content": "You are a helpful assistant.
"}, {"role": "user", "content": "Using the classic Game of Life Rules,
determine the next state of the 3x3 Game of life board: \n1 1 1\n\n1 0
0\n\n0 0 0 \n\n Do not provide any explanation other than the next state
of the board. e.g 0 0 0\n\n0 0 0\n\n0 0 0"}], "ideal": ["1 0 1\n\n1 0
1\n\n0 0 0"]}
{"input": [{"role": "system", "content": "You are a helpful assistant.
"}, {"role": "user", "content": "Using the classic Game of Life Rules,
determine the next state of the 3x3 Game of life board: \n0 1 1\n\n1 1
1\n\n1 1 0 \n\n Do not provide any explanation other than the next state
of the board. e.g 0 0 0\n\n0 0 0\n\n0 0 0"}], "ideal": ["1 0 1\n\n0 0
0\n\n1 0 1"]}
{"input": [{"role": "system", "content": "You are a helpful assistant.
"}, {"role": "user", "content": "Using the classic Game of Life Rules,
determine the next state of the 3x3 Game of life board: \n0 1 1\n\n0 1
1\n\n0 0 0 \n\n Do not provide any explanation other than the next state
of the board. e.g 0 0 0\n\n0 0 0\n\n0 0 0"}], "ideal": ["0 1 1\n\n0 1
1\n\n0 0 0"]}
{"input": [{"role": "system", "content": "You are a helpful assistant.
"}, {"role": "user", "content": "Using the classic Game of Life Rules,
determine the next state of the 3x3 Game of life board: \n0 1 0\n\n0 0
0\n\n1 1 0 \n\n Do not provide any explanation other than the next state
of the board. e.g 0 0 0\n\n0 0 0\n\n0 0 0"}], "ideal": ["0 0 0\n\n1 1
0\n\n0 0 0"]}
  ```
</details>

---
## [douglasmonsky/evals](https://github.com/douglasmonsky/evals)@[f89925829b...](https://github.com/douglasmonsky/evals/commit/f89925829b2fdd8e24acfdb518064189a5751178)
#### Friday 2023-06-23 21:43:50 by Vasco Lange

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
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[210e29ca14...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/210e29ca144117b0c7cc5f9c70cc086ce343ec38)
#### Friday 2023-06-23 23:15:43 by SkyratBot

[MIRROR] Optimizes timer insertion by 80% (W QDEL_IN micro) [MDB IGNORE] (#21986)

* Optimizes timer insertion by 80% (W QDEL_IN micro) (#76214)

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

* Optimizes timer insertion by 80% (W QDEL_IN micro)

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---

