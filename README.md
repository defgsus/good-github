## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-05-09](docs/good-messages/2023/2023-05-09.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,966,755 were push events containing 3,202,583 commit messages that amount to 249,437,250 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 64 messages:


## [ConsumingChaos/rules_rust](https://github.com/ConsumingChaos/rules_rust)@[80f0eb488a...](https://github.com/ConsumingChaos/rules_rust/commit/80f0eb488ab9cabc4920ac446478cbf2feedc3f3)
#### Tuesday 2023-05-09 00:01:32 by scentini

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
## [norsvenska/tgstation](https://github.com/norsvenska/tgstation)@[1a918a2e14...](https://github.com/norsvenska/tgstation/commit/1a918a2e1411f58e5a90f587a92daebebb9ac395)
#### Tuesday 2023-05-09 00:05:47 by Jacquerel

Golem Rework (#74197)

This PR implements this design document:
https://hackmd.io/@Y6uzGFDGSXKRaWDNicSiEg/BkRr176st
Put briefly, this will remove every existing golem subtype and
consolidate golems into a single species with cool new sprites.
NOT implemented from that PR is the ability to eat Telecrystals, I
couldn't come up with an appropriate visual that can stack with the
existing ones, but that should be a reasonably trivial add for a future
artist & developer.

New Golems have a food-based mechanic where their hunger decays pretty
quickly and can only be replenished by eating minerals. They start
moving slower as they get hungrier, until eventually they become
completely immobilised and need to be rescued.
Eating different kinds of minerals will visually change your sprite and
give you a special effect in a similar way to old golems, but temporary.
While transformed, you can't eat any other kind of mineral which would
transform you (but can still consume glass).
To see the full list of effects, look at the hackmd above.

In service of these sprites working I have refactored the
`species/offset_features` feature by killing it and delegating that
responsibility to limbs instead. Rather than applying an offset to items
due to your species, it is due to your weird head or arms. This makes
overall more sense to me, but it inflates the code changes in this PR
somewhat.
It doesn't make a lot of sense to atomise unfortunately because that
code also seemed to be entirely unused until I tried to use it in this
PR, so you wouldn't be able to tell if my changes broke anything. I
might make a downstream sad by doing this.

All of the actual numbers in this PR are made up and only loosely
tested, it will need some testmerges to gather feedback about whether it
sucks or not.

Other relevant changes:
I reworked how bioscrambling works based off bodypart bodytypes, to
automatically exclude golem limbs in either direction. There's really no
way to have those work on humans or vice versa. Organs still fly though.

---
## [harryob/cmss13](https://github.com/harryob/cmss13)@[c4ebe04c7c...](https://github.com/harryob/cmss13/commit/c4ebe04c7c9ff01aa928c0c629322d72dec721d9)
#### Tuesday 2023-05-09 00:10:51 by Julian56

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
## [rkadyan-rio/dolly](https://github.com/rkadyan-rio/dolly)@[af91832c66...](https://github.com/rkadyan-rio/dolly/commit/af91832c663025b9d5b3bd0e01be125b91a51799)
#### Tuesday 2023-05-09 00:23:49 by Matthew Hayes

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
## [rockdaworld/rockdaworld.github.io](https://github.com/rockdaworld/rockdaworld.github.io)@[1f3ad06f61...](https://github.com/rockdaworld/rockdaworld.github.io/commit/1f3ad06f61f6d461d815e6c5ae6e5d07231d0592)
#### Tuesday 2023-05-09 00:46:46 by rockdaworld

<html>
    <style>
        h1 {text-align: center;}
        p {text-align: left;}
        p {text-indent: 25px;}
    </style>
    <body>
        <h1>Easy and Light</h1>
        <p>
        Today (April 27th) marks the start of my 22nd year of life. I was going to write how the first thought I had of this event was how old I felt, but that's not actually true. The moment the clock struck midnight on the 27th, I felt like I have been incredibly blessed in all my life. I am far, far from the best friend and even further from being the best person, so I had no expectations of anything really special happening on my birthday because of how unworthy I felt of it. However, one thing I'm learning even more through today is the fact that love isn't this linear exchange of services for emotion. It's not necessarily earned or not earned. The amount you pour into someone's life doesn't create a linear relationship with the love that they or you give each other. It might be less than or much greater than what you might expect. The love that I received from my family and friends seemed so much greater than what I think I deserve from anyone. Whether it was a little message or something more, I felt inadequate and unworthy to receive any of it. But despite how I felt, the love was still given and that reminded me of just how truly blessed I am in every aspect of my life. So I thank each and every one of you who poured into me and even those who are just reading this, for the love that you've shown me, for how special this day has become.
        </p>
        <p>
        Life has not been so easy recently. Honestly, for my post-pubescent period of life it really hasn't ever been easy. I am now starting to understand that suffering and difficulty are not the same. In some ways, I may be suffering now, but I feel as if my life is easier than it ever has been, that my burdens are light. As of my recent posts, I've tried my best to not include my faith in what I write for many reasons, but when it comes to sharing about this, there's only one way I can really do it.
        </p>
        <p>
        A bit of a "season verse" for myself has been Matthew chapter 11, verses 28-30, and more specifically, verse 30. In the ESV version it goes, "For my yolk is easy, and my burden is light." Jesus here is speaking to the crowds in Galilee, to the regular people of the city. He's saying to a crowd of people who are likely to be impoverished by today's standards, beat down by those who hold power, looking for someone to save them. However, Jesus isn't what the Jews of the time imagined their savior to be. They imagined a literal king of a nation. One who would rise to power and save them from both physical oppression and the pain and suffering of the world
        </p>
        <p>
        What Jesus is actually offering here, and he highlights it in verse 30, is a salvation from the pain and suffering of the world, but in a different light or way. In the only way that is good, merciful, and above all, the most loving. Here, Jesus is saying that for those who follow him, their yoke will be easy. This meaning that the responsibilities in which we are called to uphold and the choices that we have to make, they will be easy. He also says that our burdens will be light. That through the highs and lows, the pressures that we put on ourselves and that we think the world puts on us will be taken off, as the expectations when living in the Kingdom of God are different to those of the world. This is true salvation. Not what the Jews expected, but what they, and us, really needed.
        </p>
        <p>
        Making the choice to become a disciple of Christ, one who follows him to learn and then apply what they have learned, has brought me into this light of salvation. Suffering is a universal constant, but I've learned that that doesn't necessitate a hard and overburdensome life. I look around and see that nothing else in this world can provide this. No other religion, philosophy, ideology, not even science. Purpose, meaning, and hope can only truly be found in and through Christ.
        </p>
        <p>
        I am so incredibly grateful for all that I have been given, for I really have earned nothing on my own. I am especially thankful for the people I have in my life. The friends, the family, even the acquaintances. Those who challenge me and encourage me, those who pour their love into me. I know that none of us are perfect, but the fact that we are trying; trying to love God, to love others, gives me profound joy.
        </p>
        <p>
        In this point I was going to talk about my future, specifically in the aspects of career. Instead, I'll share about who I want to be as a person. Of course I want to be working hard to figure out the aspects of my career and what I want to do with my life in those terms, but I want to be doing that and every other thing in my life in the light of the growing love that I have for God and for others. When the disciples asked Jesus what the greatest commandment was, he replied that it was to love God. Right after he said this, he said the next greatest is to love others. These must be the most important parts of our lives, and I want to become a person who desires these things above all else. This is a general idea of the general person I want to be, and the specifics will be dove into in the future.
        </p>
        <p>
        Again, for each and every one of you, I thank you for being such a great blessing in my life, for making this day so special, so blessed. Even if you do not know me well, the fact that you read this drives me to write more, so these words are not empty whatsoever.
        </p>
        <p>
        I will sign off with a question to you: What type of person do you want to be? Is the path that you are on one that will leave you off the best at the end of your life? And most importantly, how are you blessed in your life?
        </p>
        <p>
        With Love, Mr Rock.
        </p>
    </body>

</html>

---
## [larpchronicles/rules](https://github.com/larpchronicles/rules)@[39253596a7...](https://github.com/larpchronicles/rules/commit/39253596a708d960842664403ce80f8da779f3c8)
#### Tuesday 2023-05-09 00:58:12 by toptechie4

Update 21_status-effects.md

Moved Suicide from effect to Ability

Animate Visible? To No
Conscious Visible? To No
Dead Visible? To No
Silence Visible? To No
Weaken Visible? To Yes

Added “How to Diagnose” Table
ANIMATE - Identify
BERSERK - Visible
BLEED OUT - First Aid
BLIND - First Aid
CONCENTRATION - Visible
CONFINE - Visible
CONFUSE - Visible
CONSCIOUS - First Aid
CURSE - Identify
CURSE OF TRANSFORMATION - **Identify
DEAD - First Aid
DISARM - Visible
DRAINED - First Aid
ENGULF - Visible
ENSLAVEMENT - Break Enslavement Rune
ENTANGLE - Visible
FEAR - Visible
INERT - First Aid
INVULNERABLE - Visible
KNEEL - Visible
PRESERVE - First Aid
RIFT LOCK - Visible
SILENCE - First Aid
SLEEP - First Aid
SLOW - Visible
STASIS - Visible
STOP THRUST - Visible
STUN - Visible
UNCONSCIOUS - First Aid
UNDEAD - Visible
WEAKEN - Visible
INFECT - Identify
REGENERATE - Visible
REVIVE - First Aid
SPIRIT BOTTLE – Identify
**TRANSFORMS – Can not be Identified



**Some Curse of Transformations and transforms will have a physical description that a player can see but cannot confirm be confirmed as a visible effect.

For Example:  Someone with pale skin and fangs may be a vampire but you cannot confirm it without more investigation.

---
## [larpchronicles/rules](https://github.com/larpchronicles/rules)@[9d5399f97a...](https://github.com/larpchronicles/rules/commit/9d5399f97a0b2de0562b6ca6d35ab2a810f6fb68)
#### Tuesday 2023-05-09 01:34:07 by toptechie4

Update 999_changelog.md

### Other Skills Skills
•	Updated first aid description with some examples and clarification that you can ask for timers.
•	Updated that a marshal determines tracking success and that a PC cannot be tracked by another PC and removed the word terrestrial.

### Life & Death
•	When a player resurrects all Non-Ritual effects are removed unless otherwise told by Plot.
•	Codified that someone can dissipate and resurrect to refuse effects except decimate.  

### Status Effects

•	Added proper response to what do I see with "unconscious" characters "An unresponsive body"
•	Moved Suicide from effect to Ability
•	Animate Visible? To No
•	Conscious Visible? To No
•	Dead Visible? To No
•	Silence Visible? To No
•	Weaken Visible? To Yes
•	Added “How to Diagnose” Table
•	ANIMATE - Identify
•	BERSERK - Visible
•	BLEED OUT - First Aid
•	BLIND - First Aid
•	CONCENTRATION - Visible
•	CONFINE - Visible
•	CONFUSE - Visible
•	CONSCIOUS - First Aid
•	CURSE - Identify
•	CURSE OF TRANSFORMATION - **Identify
•	DEAD - First Aid
•	DISARM - Visible
•	DRAINED - First Aid
•	ENGULF - Visible
•	ENSLAVEMENT - Break Enslavement Rune
•	ENTANGLE - Visible
•	FEAR - Visible
•	INERT - First Aid
•	INVULNERABLE - Visible
•	KNEEL - Visible
•	PRESERVE - First Aid
•	RIFT LOCK - Visible
•	SILENCE - First Aid
•	SLEEP - First Aid
•	SLOW - Visible
•	STASIS - Visible
•	STOP THRUST - Visible
•	STUN - Visible
•	UNCONSCIOUS - First Aid
•	UNDEAD - Visible
•	WEAKEN - Visible
•	INFECT - Identify
•	REGENERATE - Visible
•	REVIVE - First Aid
•	SPIRIT BOTTLE – Identify
**TRANSFORMS – Can not be Identified
•	**Some Curse of Transformations and transforms will have a physical description that a player can see but cannot confirm be confirmed as a visible effect.

---
## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[f3549a4aec...](https://github.com/MTandi/tgstation/commit/f3549a4aeca6701a2969a63b7d4034d5bc560cb6)
#### Tuesday 2023-05-09 01:38:33 by Thunder12345

De-holes holy arrows (#75184)

## About The Pull Request

Covers the 2-pixel hole in the holy arrow sprite with 1 alpha pixels to
prevent unintentional missed clicks.

## Why It's Good For The Game

It's annoying and a bad experience to think you clicked on a sprite but
actually landed on a tiny transparent hole and clicked nothing or the
object below the one you wanted.

## Changelog
:cl:
image: Holy arrows are now 15% less holy (You can no longer click on the
2-pixel hole in the arrowhead and unintentionally click the object below
the arrow instead.)
/:cl:

---
## [openai/evals](https://github.com/openai/evals)@[170dfd886c...](https://github.com/openai/evals/commit/170dfd886c0704588461af075393cc20cfb0480f)
#### Tuesday 2023-05-09 01:47:00 by Robert Bateman

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
## [Offroaders123/NBTify](https://github.com/Offroaders123/NBTify)@[c66cfc0966...](https://github.com/Offroaders123/NBTify/commit/c66cfc0966f850faf904b4516c6bdbbf44b99553)
#### Tuesday 2023-05-09 02:42:09 by Offroaders123

Primitive Inspect Logging

This is the custom logging behavior mentioned in the previous commit, it's super neat! I've wanted to learn how to do this for a while now, and I ended up finding the right documentation which described everything I needed to do in order to get it to work.

It's a Node-specific thing, so this is meant for that.

Essentially, you can customize all of the ways that Node will log a given object, and you can specify things like the actual text that comes out in the log, what color it should be, and things like that. Using that, I essentially made it so the content of the `NBTData.prototype.data` property is shown on the `NBTData` log itself, rather than all of the properties present on `NBTData`. The only thing I don't like about this is that it could make NBTify users think that the `NBTData` object itself directly holds the keys/values, when it's actually the `data` property that has them. I think this does look nicer in terms of the console output though.

Here's some demo code to set it up:

```ts
// https://stackoverflow.com/questions/10729276/how-can-i-get-the-full-object-in-node-jss-console-log-rather-than-object
// https://nodejs.org/api/util.html#utilinspectcustom
// https://github.com/nodejs/node/issues/35956

import type { inspect as inspectFn, InspectOptions } from "node:util";

export class Byte extends Number {
  constructor(value: number) {
    super(value);
  }

  get [Symbol.toStringTag]() {
    return "Byte" as const;
  }
}

export class Short extends Number {
  constructor(value: number) {
    super(value);
  }

  get [Symbol.toStringTag]() {
    return "Short" as const;
  }

  // [inspect.custom]() {
  [Symbol.for("nodejs.util.inspect.custom")](depth: number, options: InspectOptions, inspect: typeof inspectFn) {
    return `${this[Symbol.toStringTag]} { ${inspect(this.valueOf(),{ colors: true })} }`;
  }
}

console.log(Number(16));
console.log(new Number(42));
console.log(new Byte(25));
console.log(new Short(83));
console.log(new Uint8Array(12));
```

After discovering this, I happened to look into the BigInt primitive wrapper extending class problem (it's not actually a constructor, so you can't extend it using the `class` syntax, 'kind of', I've come to learn and find out :) ).

Not sure which way I will take this, as to whether I will move the `LongTag` type over to it's own primitive wrapper class (that's been keeping the API in limbo, in-between either all primitive wrapper classes, or only primitives themselves). I think it's been a nice sweet spot to rely on types only to do things, and to use library module-specific functions to deal with the primitives, instead of doing everything with wrapper objects and methods. Now that I have this demo working though, I think I want to try out the primitive wrapper object syntax again. Not sure how much I like it though. It does at least kind of 'seem' like it could make the library simpler, but I'm not so sure about that, having learned more of the downfalls with OO programming.

```ts
// https://github.com/tc39/proposal-bigint/issues/98
// https://stackoverflow.com/questions/3350215/what-is-returned-from-a-constructor
// https://github.com/microsoft/TypeScript/issues/7285

import type { InspectOptionsStylized } from "node:util";

declare global {
  interface BigIntConstructor {
    new (value: bigint | boolean | number | string): BigInt;
  }
}

export class Long<T extends bigint = bigint> extends BigInt {
  // @ts-expect-error
  constructor(value: T) {
    return Object.setPrototypeOf(Object(BigInt(value)),Long.prototype);
  }

  override valueOf() {
    return super.valueOf();
  }

  override toString() {
    return `${this.valueOf()}l`;
  }

  // @ts-expect-error
  get [Symbol.toStringTag]() {
    return "Long" as const;
  }

  [Symbol.for("nodejs.util.inspect.custom")](_: number, { stylize }: InspectOptionsStylized) {
    return stylize(this.toString(),"bigint");
  }
}

const myThing = new Long(25n);
console.log(myThing,25n);
console.log(myThing instanceof BigInt);
```

Yeah, so I'm trying to decide whether to move the logic for doing things into wrapper classes, or to try and keep raw primitives wherever possible. This could essentially strengthen NBTify's associations between the tag types, and the classes/primitives themselves, which I think is what I like out of this.

For example, the `getTagType()` function currently uses a mix of `typeof` and `instanceof` checks to see if that value is one of the NBTify primitives/wrapper objects. If everything is made with wrapper objects, you could instead just use `instanceof` directly, and check if the value is an instanceof the given 'NBTify primitive', essentially any of the wrapper objects for all of the tag types, in the case that everything would be primitive wrapper objects. This could take some of the logic out of the type checking, and into the data structures themselves, or something like that.

I think one of the other things that I liked about the idea for primitive wrapper objects too, is that you could add your own `toString()` methods, and they could narrow down to plain SNBT, which NBTify could them parse directly. You might not need to have a `stringify()` function; at least, you could even just wrap the `toString()` of the root `CompoundTag` to be returned from `stringify()`, and the recursive nature of the data tree's `toString()` methods would manage the stringification of the tree, rather than the `stringify()` function itself. This moves the stringification logic out of the function, and onto the objects to handle themselves.

But for the already-existing wrapper objects, like the TypedArrays, I kind of don't like having to call a custom NBTify constructor just to create that NBT primitive type. It's only necessary to do for the single-number types, because they don't have JavaScript equivalents or alternatives.

That last paragraph made me think some more, what would JavaScript do? What's the best scenario here?

If this were JavaScript's realm, it would probably have the primitive types for these built-in. And if they are primitive types, they wouldn't be used by default as wrapper objects, you'd use them as the primitives themselves, just like how `string`, `number`, `bigint`, `boolean`, and `symbol` work right now. They may have wrapper objects, but you don't actually use them in your regular old code like that. You just use their primitives. If that's the case, and JavaScript *did* have those primitives built-in, then I wouldn't be using primitive wrapper objects for everything. Seeing it that way, it's obvious.

The best scenario would be for JavaScript to support the lower-level number primitives, `int8`, `int16`, `int32`, and `float32`. That would allow me to remove the number wrapper types, because the language and runtime itself could distinguish the values of each as different from each other. That's been my main reason for choosing to make wrapper objects for those. I didn't want to lose any type information from the NBT tree when parsing them as numbers in JavaScript. The `number` type itself can handle all of those values, they just can't be distinguished from one another. NBTify could always just assume what it should be, based on it's size, but this isn't safe, because this would essentially just coalesce everything to the smallest number bracket that it could fit into (most of the time `ByteTag` in NBT). And trying to guess the type is harder than already having it provided to you, by the source data itself. And if the primitives were available in JavaScript, that would be the simplest option. The only reason this one is in similar complexity to guessing the data type container, is because I have to re-create the data containers in JavaScript, because the primitives aren't (yet?) available.

So, with that whole thing in mind, I think I should likely stay away from the full primitive wrapper object route, because while it does seem to break up the logic into nice components, it inherently prevents you from using the data as primitives themselves, and it requires you to use objects to wrap the data itself, while it does break it up into nice containing blocks.

Ok, that was a lot of writing. Wasn't sure if I covered everything, but I'm happy how much I did. Listening to parts of Marco's new 'Their Colors Fade' album today, not sure how many times I've listened through all the different parts just today. I really like it a lot. I'm hearing more parts of his earlier albums that I hadn't noticed before, and it feels like a nice reference to the past. It definitely feels like a whole new concept and vibe, I really like it. The songs that are newer to me are really starting to catch on now. I knew a good few of them from during the time he was posting about working on the album online, so I think that's why the album has caught on so quick for me. It was familiar in understanding the vibe, but now it says something more specific as a whole when hearing them all together as one piece. He was right about the track list order, it did turn out perfect.

---
## [PenguinMod/PenguinMod-Vm](https://github.com/PenguinMod/PenguinMod-Vm)@[1bbdf7626d...](https://github.com/PenguinMod/PenguinMod-Vm/commit/1bbdf7626df0d37afebef161be58f7e1e8ad9a7a)
#### Tuesday 2023-05-09 02:58:37 by JeremyGamer13

remove debugger statement oh my god i literally hate this so much please get the fuck out of the fucking exported code you stupid fucking statement

---
## [Offroaders123/NBTify](https://github.com/Offroaders123/NBTify)@[29d5ea6e42...](https://github.com/Offroaders123/NBTify/commit/29d5ea6e42f0d5b43d3042c67c7cf6a39da9220d)
#### Tuesday 2023-05-09 03:36:45 by Offroaders123

Demo Cleanup

Learned a lot the last few commits! Now I think I have more of a clearer idea again as to how the library should go from here, as to what's the strongest API for users. I think I want to continue sticking with using primitive wrapper objects as little as possible.

Going to start fresh on the required primitive wrapper custom logging logic, and try some other things with that now that I know how it works.

Listening to 'You Must Be This Tall', now :P

Gonna go eat something soon, gettin' hungerey.

Oh yeah, the other part of this commit, kinda forgot haha. Realized that I like having separate imports for types, it looks nice to have a specific import with only types in it, makes it a little easier to discern everything that you're adding to the module, and what it's used for. I also read up on some of the changes for TypeScript 5, which had a bunch of great things in there! @satisfies for JSDoc is killer. There's all kinds of neat things in there like that. Can't wait to stumble across another random use-case when another new language feature fill the missing void when I run into another issue.

https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-0.html#--verbatimmodulesyntax

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[3861627c66...](https://github.com/LemonInTheDark/tgstation/commit/3861627c66747fb27b18f8bf76a3c9dfd2023001)
#### Tuesday 2023-05-09 05:23:17 by LemonInTheDark

Microing var/static times (~0.015 seconds of init) (#74769)

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

---
## [AkashBabu1712/Web-Scrapping](https://github.com/AkashBabu1712/Web-Scrapping)@[2d4e1535d7...](https://github.com/AkashBabu1712/Web-Scrapping/commit/2d4e1535d7f4c95cf28e595d1c20779d223f86e8)
#### Tuesday 2023-05-09 05:43:53 by AKASH BABU

Data Science Salaries on the Rise

The data science salaries dataset contains information on the salaries of data scientists from various industries and regions. The dataset is typically structured as a table, where each row represents a unique data scientist and each column represents a different attribute or characteristic of that data scientist, such as their salary, gender, level of education, industry, and location.

The dataset may include information such as:

- Salary: the amount of money earned by the data scientist per year, typically in USD or some other currency.
- Gender: the gender of the data scientist, which may be male, female, non-binary, or unspecified.
- Education level: the highest level of education attained by the data scientist, such as a bachelor's, master's, or doctoral degree.
- Industry: the industry in which the data scientist works, such as finance, healthcare, or technology.
- Years of experience: the number of years of professional experience the data scientist has in the field of data science.
- Location: the geographic region in which the data scientist is located, such as North America, Europe, or Asia.

The dataset may also include other attributes or characteristics, depending on the source and purpose of the data collection. The information contained in the dataset can be used for various purposes, such as analyzing trends in data science salaries, identifying factors that influence salaries, and developing predictive models to estimate salaries for new data scientists.

---
## [VeronicaAlexia/Open-Assistant](https://github.com/VeronicaAlexia/Open-Assistant)@[b9c60ed582...](https://github.com/VeronicaAlexia/Open-Assistant/commit/b9c60ed582a8ca0855ab4e213a5e921f3a3fc24c)
#### Tuesday 2023-05-09 05:47:16 by Tobias Pitters

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
## [Kapu1178/Citadel-Station-13-RP](https://github.com/Kapu1178/Citadel-Station-13-RP)@[d23ac504a0...](https://github.com/Kapu1178/Citadel-Station-13-RP/commit/d23ac504a0963a99c4a598abf102cd51144a0ef5)
#### Tuesday 2023-05-09 05:53:26 by Captain277

Ashlanders Phase 3.5: Prelude to War (#5259)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

_War is coming to Surt-nar-Vel'la. It rages in the caverns below, held
back only by the furious roiling blood of the Mother. More and more
Scori are driven up to Surt-nar-Vel'la, and they bring ancient secrets
with them. But, perhaps not all that dwells below should be
unearthed..._

1. **Increases Mother's Blessing from 5 minutes to 15.**
2. **Gives Ashlanders access to Sign Language.**
3. **Creates reagent Phlogiston.**
4. **Creates Condensed Phlogiston item.**
5. **Creates craftable Heaven Shaker hand-held explosive.**
6. **Buffs Shank riding speed.**
7. **Makes tying posts dense.**
8. **Adds craftable Primitive Splints.**
9. **Adds craftable Bone Pipes.**
10. **Adds the craftable Spark Striker.**
11. **Adds cowls.**
12. **Adds Ashlander cryo.**

## Why It's Good For The Game

1. _This buff is too short-lived to be used by the Ashlanders. I'm
raising it to 15 minutes. However, it is still fairly robust, so I might
drop it to 10. Or raise it even further if it's still too short._
2. _It's been months of lessons. Knowledge of primitive sign is now
available to most surface dwellers. It is slowly being disseminated
below the surface to those who are willing to learn, meaning those who
are likely to come to the surface may know it too._
3. _Phlogiston is the alchemical compound found in all explosive and
flammable things. Here I imagine it as a sticky tar similar to napalm or
condensed nitroglycerin._
4. _Condensed Phlogiston is basically semtex. Not much more to add
there._
5. _These craftable grenades require condensed phlogiston. They are
designed to address an impending threat, but will almost certainly need
to be nerfed and fine tuned. They come in two flavors: HE and Frag._
6. _Shanks now move slightly faster, providing a movement bonus to
mounted travel._
7. _Tying posts not being dense has bothered me for a while now._
8. _Gotta have a way to temporarily mend bones until surgery is done!_
9. _Apparently Ashlanders are missing avenues to fine tobacco - and
other substances. Perhaps a new avenue of trade..._
10. _Going to need lighters for your pipes._
11. _These are basically the hood parts of certain cloaks or jackets,
but toggleable as simple headwear._
12. _No longer will there be braindead Ashlanders sleeping in the
Temple!_

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
tweak: Increases duration of Mother's Buff.
tweak: Gives Scori Sign Language.
add: Adds Ashlander cryo.
add: Adds Phlogiston and Condensed Phlogiston.
add: Adds Heaven Shaker grenades, using phlogiston.
tweak: Buffs riding speed of Shanks.
tweak: Makes tying posts dense.
add: Adds craftable primitive splints.
add: Adds bone pipes.
add: Adds primitive lighters.
add: Adds cowls.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [SimonRichardson/juju](https://github.com/SimonRichardson/juju)@[7976a61522...](https://github.com/SimonRichardson/juju/commit/7976a61522a3f380be4c793f050ffc0c5e120a16)
#### Tuesday 2023-05-09 08:47:07 by Juju bot

Merge pull request #15492 from barrettj12/openstack-meta

https://github.com/juju/juju/pull/15492

The interactive add-cloud is painful because it will often reject the endpoint URL without giving any reason why. See https://bugs.launchpad.net/juju/+bug/1908630
```
Enter the API endpoint url for the cloud []: 172.31.47.119
Can't validate endpoint: No Openstack server running at 172.31.47.119

Enter the API endpoint url for the cloud []: http://172.31.47.119/
Can't validate endpoint: No Openstack server running at http://172.31.47.119/

Enter the API endpoint url for the cloud []: http://172.31.47.119/identity/v3
Can't validate endpoint: No Openstack server running at http://172.31.47.119/identity/v3

Enter the API endpoint url for the cloud []: 172.31.47.119/identity
Can't validate endpoint: No Openstack server running at 172.31.47.119/identity

Enter the API endpoint url for the cloud []: http://172.31.47.119/identity
Can't validate endpoint: No Openstack server running at http://172.31.47.119/identity
```

In the Openstack provider's `Ping` method, at least pass on the error information to the user, to make it a little less painful.
```
Enter the API endpoint url for the cloud []: 172.31.47.119
Can't validate endpoint: No Openstack server running at 172.31.47.119: auth options fetching failed
caused by: request available auth options: failed executing the request /
caused by: Get "/": unsupported protocol scheme ""

Enter the API endpoint url for the cloud []: http://172.31.47.119
Can't validate endpoint: No Openstack server running at http://172.31.47.119: auth options fetching failed
caused by: request available auth options: failed executing the request http://172.31.47.119/
caused by: Get "http://172.31.47.119/": dial tcp 172.31.47.119:80: connect: no route to host
```

Do the same with the MAAS and LXD providers.

Also, fix a silly check in the LXD provider's `Ping` method that was rejecting perfectly good URLs. We're already using `lxd.EnsureHostPort(endpoint)` to fill in the scheme/port if not provided, but we were checking the returned value equals the input (and returning an unhelpful error if not). Remove this check.

## Checklist

*If an item is not applicable, use `~strikethrough~`.*

- [x] Code style: imports ordered, good names, simple structure, etc
- ~[ ] Comments saying why design decisions were made~
- [x] Go unit tests, with comments saying what you're testing
- ~[ ] [Integration tests](https://github.com/juju/juju/tree/develop/tests), with comments saying what you're testing~
- ~[ ] [doc.go](https://discourse.charmhub.io/t/readme-in-packages/451) added or updated in changed packages~

## QA steps

Run `juju add-cloud` interactively, and provide a bogus URL.

---
## [RaShCat/Skyrat-tg](https://github.com/RaShCat/Skyrat-tg)@[fc1471c818...](https://github.com/RaShCat/Skyrat-tg/commit/fc1471c8187d3f2a49d75a8a5c3e1b610fec45d3)
#### Tuesday 2023-05-09 08:56:01 by SkyratBot

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
## [FieryTech/Skyrat-tg](https://github.com/FieryTech/Skyrat-tg)@[c5a7f5a7c9...](https://github.com/FieryTech/Skyrat-tg/commit/c5a7f5a7c93f96cc047297ed8ee61cce02626c75)
#### Tuesday 2023-05-09 09:15:51 by SkyratBot

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
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[0c35ec75e7...](https://github.com/cmss13-devs/cmss13/commit/0c35ec75e7ff5202767260473e84823085472412)
#### Tuesday 2023-05-09 09:21:46 by Logan

PFC rack sprite change (#3264)

# About the pull request
This PR changes the PFC rack sprite a tiny bit, by replacing the old PFC
kits, with weapon cases.

Why am I making this PR you might ask? Is it because my sugar induced
OCD made me notice something so small and infinitesimal that the kits in
the vendor are outdated and must be changed at once?

No. It is because these vendors when I see them, completely and utterly
ruin my RP and immersion when I see them, I walk out of the chow hall,
belly full of stale food bars with my RP fulfilled, and then I see them,
those fucking little bursts of color that are the old PFCs kits, they
shouldn't be there, _"they shouldn't even exist"_ I tell myself, but its
too late, by the time I come back to my senses, I've already killed
2/3rds of the RO line in my 3rd Vancleve style M2C rampage, after this
rampage I realized that if I, a near 7 year vet of CM can be so easily
triggered by this, what must the PVTs be feeling when they see those
little bursts of outdated color, do they feel hope when they see them in
the dullness of color that is the vendor, only to have their hope turn
into hopeless despair as they scroll hopelessly through the UI looking
for those kits, and when they can't find they either breakdown complete
on the spot, crying and sobbing in the corner till the SEA finds them,
or they suffer a total mental break, and wander the halls of the Almayer
naked with a M41 in their hand, only to appear at briefing to gun down
the CO.

With this change, we can at last save RP and immersion by removing the
PFC kits sprites with weapon case spites.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

Sprite Consistency good, 
# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.
Old: https://i.gyazo.com/9f1ec938a1ebf9995f353cede374f7b9.png
New: https://i.gyazo.com/4836db37aaa5b8fc4f8a80c8e6531540.png
</details>


# Changelog
:cl: Tisx


imageadd: Added weapon case sprites to PFC vendors 
imagedel: Removed old PFC kit sprites from PFC vendors 

/:cl:

Co-authored-by: Logan <tisx16@gmail.com>

---
## [Offroaders123/Region-Types](https://github.com/Offroaders123/Region-Types)@[4ac61b0258...](https://github.com/Offroaders123/Region-Types/commit/4ac61b025871ce9369e4c12596588f44cd3eb733)
#### Tuesday 2023-05-09 09:45:13 by Offroaders123

Union Type Narrowing

Discovered more about using unions to discern between multiple things of a similar type! Kind of forgot/haven't had a chance to use this yet, and it really feels like a great fit for what I'm trying to do here.

(Thanks for reminding me of this naming style! I've been using the `ArrayBufferLike` type in some things for a while now, and I forgot that the 'Like' suffix would be a great fit for this scenario. Calling things `AbstractThing`, or `ThingInterface` seemed really boring and not very descriptive. I like (pun not initially intended) this one a lot more :D )
https://stackoverflow.com/questions/31876947/confused-about-the-interface-and-class-coding-guidelines-for-typescript#comment132085483_66781146

Found a demo on doing this yesterday, then happened to see a new video from Andrew Burgess which released in the morning once I had woke up. Sometimes it's funny timing as to how random cool things work out. Sometimes things just click. You have to remember it's ok when they don't, too. I felt like I was in a slump just a few days/week ago, so I'm not sure what changed. Sometimes it just comes and goes I guess. That's also what makes it fun, and even more meaningful :)

(Music context, atm: https://youtu.be/_fZQi4t969Y?t=2452; Was listening to prog, but I think I progged-out my brain today (that's a good thing :P), so searching for 'ambient music' seemed like the perfect cure. It really is helping me finish off these last few things tonight)

---
## [overhangio/tutor](https://github.com/overhangio/tutor)@[c6c57b40c1...](https://github.com/overhangio/tutor/commit/c6c57b40c12ff84c7dc7a7a4b071840fe6a62edb)
#### Tuesday 2023-05-09 10:40:57 by Régis Behmo

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
## [prenaux/cppfront](https://github.com/prenaux/cppfront)@[d8c1a50f22...](https://github.com/prenaux/cppfront/commit/d8c1a50f22c1b171a50e87ccdb609fb05f41c021)
#### Tuesday 2023-05-09 11:04:48 by Herb Sutter

First checkin of partial meta function support, with `interface` meta type function

This commit includes "just enough" to make this first meta function work, which can be used like this...

```
Human: @interface type = {
    speak: (this);
}
```

... where the implementation of `interface` is just about line-for-line from my paper P0707, and now (just barely!) compiles and runs in cppfront (and I did test the `.require` failure cases and it's quite lovely to see them merge with the compiler's own built-in diagnostics):

```
//-----------------------------------------------------------------------
//  interface: an abstract base class having only pure virtual functions
auto interface( meta::type_declaration&  t ) -> void {
    bool has_dtor = false;
    for (auto m : t.get_members()) {
        m.require( !m.is_object(),
                   "interfaces may not contain data objects");
        if (m.is_function()) {
            auto mf = m.as_function();
            mf.require( !mf.is_copy_or_move(),
                        "interfaces may not copy or move; consider a virtual clone() instead");
            mf.require( !mf.has_initializer(),
                        "interface functions must not have a function body; remove the '=' initializer");
            mf.require( mf.make_public(),
                        "interface functions must be public");
            mf.make_function_virtual();
            has_dtor |= mf.is_destructor();
        }
    }
    if (!has_dtor) {
        t.require( t.add_member( "operator=: (virtual move this) = { }"),
                   "could not add pure virtual destructor");
    }
}
```

That's the only example that works so far.

To make this example work, so far I've added:

- The beginnings of a reflection API.

- The beginnings of generation from source code: The above `t.add_member` call now takes the source code fragment string, lexes it,  parses it, and adds it to the `meta::type_declaration` object `t`.

- The first compile-time meta function that participates in interpreting the meaning of a type definition immediately after the type grammar is initially parsed (we'll never modify a type after it's defined, that would be ODR-bad).

I have NOT yet added the following, and won't get to them in the short term (thanks in advance for understanding):

- There is not yet a general reflection operator/expression.

- There is not yet a general Cpp2 interpreter that runs inside the cppfront compiler and lets users write meta functions like `interface` as external code outside the compiler. For now I've added `interface`, and I plan to add a few more from P0707, as meta functions provided within the compiler. But with this commit, `interface` is legitimately doing everything except being run through an interpreter -- it's using the `meta::` API and exercising it so I can learn how that API should expand and become richer, it's spinning up a new lexer and parser to handle code generation to add a member, it's stitching the generated result into the parse tree as if it had been written by the user explicitly... it's doing everything I envisioned for it in P0707 except for being run through an interpreter.

This commit is just one step. That said, it is a pretty big step, and I'm quite pleased to finally have reached this point.

---

This example is now part of the updated `pure2-types-inheritance.cpp2` test case:

    // Before this commit it was this
    Human: type = {
        speak: (virtual this);
    }

    //  Now it's this... and this fixed a subtle bug (can you spot it?)
    Human: @interface type = {
        speak: (this);
    }

That's a small change, but it actually also silently fixed a bug that I had written in the original code but hadn't noticed: Before this commit, the `Human` interface did not have a virtual destructor (oops). But now it does, because part of `interface`'s implementation is to generate a virtual destructor if the user didn't write one, and so by letting the user (today, that was me) express their intent, we get to do more on their behalf. I didn't even notice the omission until I saw the diff for the test case's generated `.cpp` had added a `virtual ~Human()`... sweet.

Granted, if `Human` were a class I was writing for real use, I would have later discovered that I forgot to write a virtual destructor when I did more testing or tried to do a polymorphic destruction, or maybe a lint/checker tool might have told me. But by declaratively expressing my intent, I got to not only catch the problem earlier, but even prevent it.

I think it's a promising data point that my own first attempt to use a metaclass in such a simple way already fixed a latent simple bug in my own code that I hadn't noticed. Cool beans.

---

Re syntax: I considered several options to request a meta function `m` be applied to the type being defined, including variations of `is(m)` and `as(m)` and `type(m)` and `$m`. I'm going with `@m` for now, and not because of Python envy... there are two main reasons:

- I think "generation of new code is happening here" is such a fundamental and important new concept that it should be very visible, and actually warrants taking a precious new symbol. The idea of "generation" is likely to be more widely used, so being able to have a symbol reserved for that meaning everywhere is useful. The list of unused symbols is quite short (Cpp2 already took `$` for capture), and the `@` swirl maybe even visually connotes generation (like the swirl in a stirred pot -- we're stirring/cooking something up here -- or maybe it's just me).

- I want the syntax to not close the door on applying meta functions to declarations other than types. So putting the decoration up front right after `:` is important, because putting it at the end of the type would likely much harder to read for variables and especially functions.

---
## [prenaux/cppfront](https://github.com/prenaux/cppfront)@[10241cd6a5...](https://github.com/prenaux/cppfront/commit/10241cd6a59040d7408fda674bcdd918bd67c4e2)
#### Tuesday 2023-05-09 11:04:48 by Herb Sutter

Checking in various improvements done in the last few evenings

Replace `store_as_base` with generated aggregate bases - better fix for #336, thanks @JohelEGP for the suggestion! This way we also don't need to obfuscate the name anywhere beyond the constructor(s), as the right member object name just enters the class's scope

If the user didn't write a constructor, provide a default constructor

If the user didn't write a 'that' constructor, suppress Cpp1's compiler-generated copying and assignment

Clean up emission of the just-mentioned generated/=deleted constructors, more naturally line up inside the class body following the indentation for other members that the original source code uses

Rename file `load.h` to `io.h` (`file.h` was another candidate), just because it has been bothering me for a year now that except for that one file all the headers were in natural alphabetical order by compilation phase... as of this commit we now have them all in alpha order and phase order: common.h -> io.h -> lex.h -> parse.h -> [*] -> sema.h -> cppfront.h

    [*] coming next here: reflect.h, which will also be in both alpha order and compilation order

Guard `out.construct` with `if constexpr` in case the type is not copy assignable and that path is never requested

Rename `cpp2::error` to `cpp2::error_entry` to quiet a new(? why?) GCC message about shadowing the former name with `parser::error`... I get why the warning is there, but this is a slightly annoying warning to have to satisfy just to compile high-warning-clean on GCC... oh well

Change semantics of emitting `.h2` files: In `-p` pure mode do the existing split of phases 0 and 1 into `.h` and phase 2 into a separate `.hpp`, but in mixed mode put all phases into the `.h`

---
## [highlight/highlight](https://github.com/highlight/highlight)@[18d94ccc74...](https://github.com/highlight/highlight/commit/18d94ccc7425a9441000e1bf4a7f92565898666e)
#### Tuesday 2023-05-09 13:06:57 by Lewis Liu

Enable Reflame for Highlight web app (#4586)

## Summary

<!--
Ideally, there is an attached Linear ticket that will describe the
"why".

If relevant, use this section to call out any additional information
you'd like to _highlight_ to the reviewer.
-->

This PR finally enables [Reflame](https://reflame.app/)
[previews](https://preview.highlight.io/~r/start-preview/?mode=production&variantId=01GY11FVTK9FMXX2DSCR6T4VRD&variantName=git%7Enew-reflame-app-1&userId=01FQZZ7XJFDA799Z1Z9DRCFXWA)
for the Highlight web app. 🥳

### What does this mean for me?

First you'll need to sign up at https://reflame.app, connect your GitHub
account, and ask @Vadman97 for an invite to the highlight organization.

Then, once this PR is merged, every time you push up a change to the web
app (in /frontend) or any of its dependencies, you'll get a Reflame
preview link on your commit immediately, usually within 3 seconds,
instead of however many minutes it used to take:
![Screenshot 2023-04-13 at 5 40 57
PM](https://user-images.githubusercontent.com/6934200/231912410-5dc2880d-353c-402e-8562-67ce4ee54137.png)

In addition, you'll have access to the Reflame [VSCode
extension](https://marketplace.visualstudio.com/items?itemName=reflame.agent)
for development, which deploys your changes usually within ~500ms of a
file save, and then reflects your changes instantly with a full browser
refresh in production mode, or with state-preserving React fast refresh
in development mode. See development mode in action here:


https://user-images.githubusercontent.com/6934200/231914985-3679e955-ddcf-4ad1-9c7e-1c7451dc3ef5.mp4

It's worth noting that Reflame is actually _deploying your changes to
the internet_ every time, so you can send these links to yourself to
check your changes on another device (even multiple devices
simultaneously), or share them with teammates or customers to give them
a sneak peak of what you're working on, iterate with their feedback, and
have those changes reflected on their browsers in real time (even if
they're on the other side of the world)!

### How do I even review this? There's like 500 files here?!

I'd recommend reviewing either commit by commit and skipping the 2nd
commit, or by viewing all files changed and skipping over everything in
`__generated` folders, since they only contain files generated using the
newly added build scripts. This should leave only about 30 files to
review, and most of the changes are a only a couple of lines long.

These scripts and generated files are a temporary stop-gap to support
features that don't have first-class support in Reflame yet,
specifically:

- Reading version from package.json
- CSS/SCSS modules
- Tailwind
- SVGR
- Git Submodules
- Vanilla Extract

These are roughly ranked in order of how quickly I think they will get
first-class support in Reflame, at which point we'll be able to remove
the associated scripts and generated files. Notably, Vanilla Extract is
as far down the list as it is because it requires executing
user-supplied code as part of its build process, which is going to take
quite a bit of work to enable safely in a multitenant system like
Reflame (but I do plan on tackling this eventually as I get closer to
building features like testing and backend APIs support). Though we may
still be able to get rid of the build script sooner than that by
building it into the VSCode extension if there's enough demand.

Outside of the script and configuration changes, there are a few
additional source changes for compatibility. I left comments on the PR
for every one of these explaining the motivation behind them. I've also
split most of them out into separate PRs so they can be reviewed, tested
and shipped independently:

- https://github.com/highlight/highlight/pull/5086
- https://github.com/highlight/highlight/pull/5087
- https://github.com/highlight/highlight/pull/5088
- https://github.com/highlight/highlight/pull/5089 

## How did you test this change?

<!--
Frontend - Leave a screencast or a screenshot to visually describe the
changes.
-->

A lot of care has gone into making sure your existing local dev workflow
works exactly as you're used to (just with a few more scripts running
than before), and that the production deployment process remains
untouched as well. If you notice any material differences in any of your
day to day workflows while trying out this PR, or in the Render preview
deploys, please let me know and I'll try to address it ASAP.

I've tried following the [docker dev guide
here](https://www.highlight.io/docs/getting-started/self-host/dev-deployment-guide)
and running `yarn dev:frontend` (without the `doppler run --` part), and
both seem to be working identically as on main as far as I can tell,
though for the latter I'm missing a few env vars from doppler so
couldn't verify past the login screen, will need your help to make sure
everything works as expected there.

If you want to try out Reflame before this PR gets merged, just make a
branch off of this PR (previews are not working for this PR because it's
coming from a fork, and the appId in the config is for the
highlight/highlight repo, but it should work if you cherry pick these
commits into another branch within this repo). The VSCode extension
should also just work once you get a VSCode account.
[Here's](https://preview.highlight.io/~r/start-preview/?mode=production&variantId=01GY11FVTK9FMXX2DSCR6T4VRD&variantName=git%7Enew-reflame-app-1&userId=01FQZZ7XJFDA799Z1Z9DRCFXWA)
the preview I'm using to test my changes.

Would love to make Reflame better with your feedback! Just leave a
comment here, [shoot me an email](mailto:lewis@reflame.app), or ask for
an invite to the #highlight-reflame channel in Slack to chat there or
send me a DM.

## Are there any deployment considerations?

<!--
 Backend - Do we need to consider migrations or backfilling data?
-->

Definitely would be helpful to get a Render preview for this to poke
around in.

---
## [yuichiro-naito/OpenBSD-src](https://github.com/yuichiro-naito/OpenBSD-src)@[e4c559e853...](https://github.com/yuichiro-naito/OpenBSD-src/commit/e4c559e853ce1cc130d8342715a65ada3e5f26e9)
#### Tuesday 2023-05-09 13:37:14 by tb

Move a few functions out of OPENSSL_NO_DEPRECATED

Geoff Thorpe added OPENSSL_NO_DEPRECATED nearly two decades ago. The hope
was that at some point some functions can be dropped. Most of the functions
marked deprecated are actually unused nowadays but unfortunately some of
them are still used in the ecosystem. Move them out of OPENSSL_NO_DEPRECATED
so we can define it without breaking the consumers in the next bump.

ERR_remove_state() is still used by a dozen or so ports. This isn't a big
deal since it is just a stupid wrapper for the not quite as deprecated
ERR_remove_thread_state(). It's not worth patching these ports.

Annoyingly, {DH,DSA}_generate_parameters() and RSA_generate_key() are still
used. They "make use" of the old-style BN_GENCB callback, which is therefore
more difficult to remove - in case you don't know know: that's the thing
responsible for printing pretty '.', '+' and '*' when you generate keys.

Most annoyingly, DH_generate_parameters() was added to rust-openssl in 2020
for "advanced DH support". This is very unfortunate since cargo bundles a
rust-openssl and updates it only every few years or so. As a consequence
we're going to be stuck with this nonsense for a good while.

ok beck jsing

---
## [Pingumask/townsquare](https://github.com/Pingumask/townsquare)@[974bbb1a0f...](https://github.com/Pingumask/townsquare/commit/974bbb1a0f35ab2a3333ba2a28955956e24fd900)
#### Tuesday 2023-05-09 13:48:06 by Dae Lorant

Updated night order for all roles

Updated night order for all roles to match the order at https://script.bloodontheclocktower.com/data/nightsheet.json

Some noticeable changes:
- Legion was moved much earlier in the order of demons (relevant if a another demon is made in a legion game, you can keep it around and kill it with legion before it kills on a subsequent night)
- Amnesiac was moved much later in night order (a more reasonable place for the most common type of amni abilities)
- Magician was given a night order for N1
- Pixie was given a night order for other nights

---
## [scalr-automation/terraform-scalr-flat](https://github.com/scalr-automation/terraform-scalr-flat)@[7066f282bc...](https://github.com/scalr-automation/terraform-scalr-flat/commit/7066f282bccb377daccd886475680a30764c9607)
#### Tuesday 2023-05-09 15:16:17 by scalr-autotester6

Merge pull request #27266 from scalr-automation/ahead-mission-ago-girl

[FO-6887] Social myself blood nearly.

---
## [teemerae/Rich-Presence-U-DB](https://github.com/teemerae/Rich-Presence-U-DB)@[b676b6cf58...](https://github.com/teemerae/Rich-Presence-U-DB/commit/b676b6cf583efcb4045ce7c6b21566b93f726a19)
#### Tuesday 2023-05-09 15:20:54 by ninstar

+71 New Nintendo Switch titles

Anuchard
Behind the Frame: The Finest Scenery
Bow to Blood: Last Captain Standing
Capcom Fighting Collection
Colors Live
Cozy Grove
Crash Bandicoot 4: It’s About Time
Dadish
Dadish 2
Dadish 3
Daily Dadish
Devil May Cry
Devil May Cry 2
Devil May Cry 3 Special Edition
DOOM 64
DOOM Eternal
DYSMANTLE
Fallout Shelter
FATAL FRAME: Maiden of Black Water
FIFA 18
FIFA 20 Nintendo Switch Legacy Edition
FIFA 21 Nintendo Switch Legacy Edition
FIFA 23 Nintendo Switch Legacy Edition
Figment
Gang Beasts
Horizon Chase Turbo
Huntdown
Just Dance 2017
Just Dance 2018
Just Dance 2019
Just Dance 2021
LEGO Brawls
LEGO Bricktales
LEGO Builder's Journey
LEGO Marvel Super Heroes
LEGRAND LEGACY: Tale of the Fatebounds
Marooners
MEGA MAN BATTLE & FIGHTERS
Mega Man Battle Network Legacy Collection Vol. 1
Mega Man Battle Network Legacy Collection Vol. 2
Metroid Prime Remastered
Moonlighter
Moto Rush GT
NAMCO MUSEUM
New Tales from the Borderlands
OKAMI HD
ONE PIECE Pirate Warriors 3 Deluxe Edition
ONE PIECE: PIRATE WARRIORS 4
ONE PIECE: Unlimited World Red Deluxe Edition
OneShot: World Machine Edition
PAC-MAN WORLD Re-PAC
Panzer Dragoon: Remake
Shantae
Shantae and the Pirate's Curse
Shantae and the Seven Sirens
Shantae: Half-Genie Hero
Shantae: Risky's Revenge - Director's Cut
Sid Meier’s Civilization VI
SmileBASIC 4
Street Fighter 30th Anniversary Collection
Summer in Mara
Super Fowlst
Super Fowlst 2
Super Monkey Ball Banana Mania
Super Monkey Ball: Banana Blitz HD
Tales from the Borderlands
The Outer Worlds
Tools Up!
Ultra Street Fighter® II: The Final Challengers
Will You Snail?
Yu-Gi-Oh! Master Duel

---
## [teemerae/Rich-Presence-U-DB](https://github.com/teemerae/Rich-Presence-U-DB)@[2cf4f40e9a...](https://github.com/teemerae/Rich-Presence-U-DB/commit/2cf4f40e9a337a60cbdad571c97d4c12202aa24b)
#### Tuesday 2023-05-09 15:20:54 by ninstar

+32 New Nintendo Switch titles

Bayonetta Origins: Cereza and the Lost Demon
Blaster Master Zero
Blaster Master Zero 2
Blaster Master Zero 3
Chocobo GP
Freedom Planet
FUZE Player
FUZE4 Nintendo Switch
GRIS
Guacamelee! 2
Guacamelee! Super Turbo Championship Edition
Hotline Miami Collection
Ittle Dew
Ittle Dew 2+
KLONOA Phantasy Reverie Series
Octopath Traveler II
Resident Evil 0
Resident Evil 4
Resident Evil Revelations
Resident Evil Revelations 2
River City Girls
River City Girls 2
River City Girls Zero
RPG Maker MV
RPG Maker MV Player
SAMURAI SHODOWN
Shovel Knight Dig
Shovel Knight Pocket Dungeon
Super Chariot
Superliminal
The Binding of Isaac: Afterbirth+
UNO

---
## [teemerae/Rich-Presence-U-DB](https://github.com/teemerae/Rich-Presence-U-DB)@[f42a3a1ef5...](https://github.com/teemerae/Rich-Presence-U-DB/commit/f42a3a1ef58eac7176a9eb618ecc837b53508b82)
#### Tuesday 2023-05-09 15:20:54 by ninstar

+41 New Nintendo Switch titles

Advance Wars 1+2: Re-Boot Camp
Atelier Ryza 3: Alchemist of the End & the Secret Key
Chained Echoes
Dead Cells
Digimon Survive
Disney Dreamlight Valley
FINAL FANTASY
FINAL FANTASY II
FINAL FANTASY III
FINAL FANTASY IV
FINAL FANTASY V
FINAL FANTASY VI
GUILTY GEAR
GUILTY GEAR XX ACCENT CORE PLUS R
Gunman Clive HD Collection
It Takes Two
Katana ZERO
Kaze and the Wild Masks
KINGDOM HEARTS Melody of Memory
Minecraft Legends
MLB The Show 23
Neon White
Ninjin: Clash of Carrots
Pirate Pop Plus
Puyo Puyo Tetris 2
Rain World
Rogue Legacy
Rogue Legacy 2
Spelunky
Spelunky 2
STAR WARS Republic Commando
Super Meat Boy
Super Meat Boy Forever
Super Punch Patrol
Temtem
Tetris® Effect: Connected
The Legend of Heroes: Trails to Azure
The Messenger
TowerFall
Ultimate Chicken Horse
Wolfstride

---
## [teemerae/Rich-Presence-U-DB](https://github.com/teemerae/Rich-Presence-U-DB)@[4659b59a14...](https://github.com/teemerae/Rich-Presence-U-DB/commit/4659b59a140619ec30a560daedcf02e034d94748)
#### Tuesday 2023-05-09 15:20:54 by ninstar

+14 Nintendo Switch titles

- CRISIS CORE –FINAL FANTASY VII– REUNION
- TRIANGLE STRATEGY™
- LIVE A LIVE
- MONARK
- SMITE
- Demon Turf
- Demon Turf: Neon Splash
- Amnesia: Collection
- Tactics Ogre: Reborn
- Little Noah: Scion of Paradise
- The Legend of Heroes: Trails of Cold Steel III
- The Legend of Heroes: Trails of Cold Steel IV
- GROOVE COASTER WAI WAI PARTY!!!!
- Just Dance®

---
## [WiiXLinux/Einfuerung-in-die-Algorithmik-SS23-CAU-Kiel](https://github.com/WiiXLinux/Einfuerung-in-die-Algorithmik-SS23-CAU-Kiel)@[d457380688...](https://github.com/WiiXLinux/Einfuerung-in-die-Algorithmik-SS23-CAU-Kiel/commit/d457380688b546a6dec8b1a3dbd3cbed7a10da63)
#### Tuesday 2023-05-09 16:18:13 by Henri Heyden

Added HA4 A1. Fuck this bonus task: I wasted 4 hours of my life on this and I don't know what to do anymore. The approach of storing the leaf-tree in a list is very, very fucking stupid for the bonus task.

---
## [mrgerwin/LOZ2023](https://github.com/mrgerwin/LOZ2023)@[47de89fd9d...](https://github.com/mrgerwin/LOZ2023/commit/47de89fd9d79f2550fac1bd2023948a272131a0e)
#### Tuesday 2023-05-09 17:03:22 by 25kbrown

ok boomer...

...ang (I'm so funny lol please laugh  haha I hate everything imma go home and play chess)

---
## [Comxy/tgstation](https://github.com/Comxy/tgstation)@[912e843f53...](https://github.com/Comxy/tgstation/commit/912e843f53cf33b15148ec5a5ec66ce107314467)
#### Tuesday 2023-05-09 17:27:53 by san7890

Allows Export of your Preferences JSON File (#75014)

## About The Pull Request

Hey there,

This was spoken about in #70492 (specifically
https://github.com/tgstation/tgstation/pull/70492#issuecomment-1278069607),
and I have been waiting for this to be implemented for some time. It
never got implemented, so I decided to code it myself.

Basically, **if the server host doesn't disable it**, you are free to
export your JSONs as a player, right from the stat-panel. It's a pretty
JSON on 515 versions, too!

It's right here:


![image](https://user-images.githubusercontent.com/34697715/235251447-1c977718-51fd-4025-8d89-c60bffc379ec.png)

Here's what the prettified JSON looks like on 515.


![image](https://user-images.githubusercontent.com/34697715/235321061-4a217e26-c082-4bba-b54a-2c780defda0a.png)

There's a cooldown (default to 10 seconds) between exporting your
preferences.

#### Why is this config?

It's because in the past, a server host could always just file-share the
.sav or .json or whatever to the player, but they would have to do the
explicit option of actually bothering to make the files accessible to
the player. In that same line of logic, the server operator will have to
explicitly make the files accessible. This is mostly because I'm not
sure how good `ftp()` is at being a player function and wanted to have
some sort of cap/control somehow in case an exploit vector is detected
or it's just plain spammed by bots, so we'll just leave it up to the
direct providers of this data to elect if they wish to provide the data
or not.
## Why It's Good For The Game

Players don't have to log into Server A to remember what hairstyle they
loved using when they want to swap to Server B! That's amazing actually.
I always forget what ponytail my character has, and it'll be nice to
have the hairstyle in a readily accessible place (after I prettify the
JSON for myself).

It's also more convenient for server hosts to make player data like this
accessible if they really want to, too.

If we ever add an _import_ feature in the future (which would have to be
done with a LOT of care), this will also be useful. I wouldn't advise it
though having taken a precursory look at how much goes into it while
trying to ascertain the scope of this PR.
## Changelog
:cl:
qol: The game now supports export of your preferences into a JSON file!
The verb (export-preferences) should now be available in the OOC tab of
your stat-panel if enabled by server operators.
server: Exporting player preferences is controlled by a configuration
option, 'FORBID_PREFERENCES_EXPORT'. If you do not wish to let clients
access the ftp() function to their own preferences file (probably for
bandwidth reasons?) you should uncomment this or add it to your config
somehow.
config: Server operators are also able to set the cooldown between
requests to download the JSON Preferences file via the
'SECONDS_COOLDOWN_FOR_PREFERENCES_EXPORT' config option.
/:cl:

---
## [Comxy/tgstation](https://github.com/Comxy/tgstation)@[f7a49c4068...](https://github.com/Comxy/tgstation/commit/f7a49c4068f1277e6857baf0892d355f1c055974)
#### Tuesday 2023-05-09 17:27:53 by Ryll Ryll

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
## [jacobhinkle/Fuser](https://github.com/jacobhinkle/Fuser)@[9c50ae8f14...](https://github.com/jacobhinkle/Fuser/commit/9c50ae8f1441917c97ebaceb343ad6be3c54304b)
#### Tuesday 2023-05-09 18:29:08 by Gao, Xiang

Remove runtime out of bound check debugging util (#277)

The change in this PR is easy to understand and has low impact, but the
motivation really needs discussion and is a much more impactful thing.
And I want to use this PR to discuss it.

In https://github.com/NVIDIA/Fuser/issues/248 we agreed to add "stride
order" support to codegen, and later in today's morning meeting on
matmul, Christian talked about the idea of "allocation_domain" which is
a generalization of the idea of "stride order". Basically, we are not
married to the rFactor domain of the tensor when doing allocation and
indexing. We can pick an arbitrary vector of `IterDomain`s between root
and leaf domain, stop the indexing process on that vector, and do
allocation based on that vector. For the idea of "stride order", which
is a special case of the new idea, this vector is just the reordered
rFactor domains. This should be easily approachable with our new
indexing approach https://github.com/NVIDIA/Fuser/pull/32. This idea
does make a lot of sense, so the purpose is not to discuss whether we
want to take that idea, but how to implement that idea.

A question comes to me during implementing is, say we have a tensor
whose semantic shape is `NCHW` but stride order is `NHWC`, should the
`stride` field of the tensor be in the order of `NCHW` or `NHWC`?
Currently, we are using the same order as PyTorch, which is the semantic
order `NCHW`. I think this does make a lot of sense in terms of stride
order support. Having the stride in the semantic order is not the most
naturally way for indexing, we do need a `NHWC->NCHW` axis map to grab
the correct stride, but it is pretty simple to implement this.
Considering all factors, including consitency with PyTorch, cleanness in
the executor's code, I still think the semantics order is the best
design.

However, this design start to make no sense when we generalize the
"stride order" idea into the "allocation_domain" idea. For example, for
an `NCHW` tensor, the actual allocation can be `(H*W, N*C)`, and the
size of `contiguity` will be `2` instead of `4`. So the `Tensor::stride`
in `runtime/tensor.cu` should also be an array of size `2` instead of
`4`. The idea of "allocation_domain" requires the stride of a tensor to
be strictly one-to-one mapped to the allocation domain. As a special
case, the "stride order" idea has no choice but to follow the same
design, which is, the stride will be stored in `NHWC` order. This means,
the order of stride in our kernel is different from those in ATen, we
can not directly copy the stride. We need to permute the stride so it is
sorted descending.

But the above problem is not the biggest trouble we have, the biggest
trouble is: If we have a `NCHW` tensor allocated as `(H*W, N*C)`, is
this tensor a 4D tensor or a 2D tensor? I think the answer is "neither".
In terms of allocation and stride, it is definitely 2D, but in terms of
semantics, it is 4D. Again, in the past, we had a concept "the
dimensionality of a tensor" which is a degeneracy of two concepts "the
semantic dimensionality of a tensor" and "the allocation dimensionality
of a tensor". Now we break the symmetry, and degenerating concepts are
no longer degenerate. In codegen, we are generating a lot of tensor
shapes like `T0.shape[0]`, and I think the easiest way to handle them is
to keep `shape` in semantic dimensionality, while make `stride` in
allocation dimensionality. That said, `struct Tensor` now needs two
template arguments for dimensionalities. And unfortunately, we can no
longer do out of bound check any more.

---
## [Chebuya/laptop-nixos](https://github.com/Chebuya/laptop-nixos)@[b08dcea2c7...](https://github.com/Chebuya/laptop-nixos/commit/b08dcea2c7e271d74005aac679ebc5a752321f52)
#### Tuesday 2023-05-09 18:37:33 by Chebuya

i don't remember what the fuck i did and i broke my system so i reverted it god please help

---
## [SyncIt21/The-TG-Station-Fork](https://github.com/SyncIt21/The-TG-Station-Fork)@[1b5c0489a4...](https://github.com/SyncIt21/The-TG-Station-Fork/commit/1b5c0489a4088dca925ab061a389d95005c95820)
#### Tuesday 2023-05-09 19:00:11 by san7890

`ex_act()` will work on basic mobs again (lol) + Unit Test (#74953)

basically ex_act's implementation on basic mobs would call parent and
then react to it's value, this is presumably to do the first check about
space vine mutations and whatever. the problem is that the `/mob/living`
implementation would itself also call parent, and that would always
return null because `/atom/proc/ex_act` doesn't have a set return value.
So, this simply would _always_ early return, with ex_act presumably
*never* working on basic mobs for at least four months now.

I decided to then change up the return values for pretty much all
implementations of `ex_act()` since there was no rhyme or reason to
returning null/FALSE/TRUE, and documenting why it's like that.

Just to make sure I wasn't breaking anything doing this (at least on
base implementations), I wrote a unit test for all of the three major
physical types in game (objs, mobs, turfs) because i am a paranoid
fuckar. we should be good to go now though.
## Why It's Good For The Game

i noticed this because placing c4's on sargeant araneus wouldn't
actually damage it whatsoever. now it actually does the stated 30
damage, but araneus has like 250 health so it doesn't actually matter in
the long run. whatever at least it does the damn 30 now.

also adds a unit test for this specific case as well as a range of other
cases to ensure this stuff doesn't silently break in this way anymore

---
## [SyncIt21/The-TG-Station-Fork](https://github.com/SyncIt21/The-TG-Station-Fork)@[f2fd69a49a...](https://github.com/SyncIt21/The-TG-Station-Fork/commit/f2fd69a49a7d9308eb695c0368163d2f63a53a54)
#### Tuesday 2023-05-09 19:00:11 by ArcaneMusic

Minerals have been refactored so costs and minerals in items are now in terms of mineral defines. (#75052)

Ladies, Gentlemen, Gamers. You're probably wondering why I've called you
all here (through the automatic reviewer request system). So, mineral
balance! Mineral balance is less a balance and more of a nervous white
dude juggling spinning plates on a high-wire on his first day. The fact
it hasn't failed after going on this long is a miracle in and of itself.

This PR does not change mineral balance. What this does is moves over
every individual cost, both in crafting recipes attached to an object
over to a define based system. We have 3 defines:

`sheet_material_amount=2000` . Stock standard mineral sheet. This being
our central mineral unit, this is used for all costs 2000+.
`half_sheet_material_amount=1000` . Same as above, but using iron rods
as our inbetween for costs of 1000-1999.
`small_material_amount=100` . This hits 1-999. This covers... a
startlingly large amount of the codebase. It's feast or famine out here
in terms of mineral costs as a result, items are either sheets upon
sheets, or some fraction of small mats.

Shout out to riot darts for being the worst material cost in the game. I
will not elaborate.

Regardless, this has no functional change, but it sets the groundwork
for making future changes to material costs much, MUCH easier, and moves
over to a single, standardized set of units to help enforce coding
standards on new items, and will bring up lots of uncomfortable balance
questions down the line.

For now though, this serves as some rough boundaries on how items costs
are related, and will make adjusting these values easier going forward.

Except for foam darts.

I did round up foam darts.

Adjusting mineral balance on the macro scale will be as simple as
changing the aforementioned mineral defines, where the alternative is a
rats nest of magic number defines. ~~No seriously, 11.25 iron for a foam
dart are you kidding me what is the POINT WHY NOT JUST MAKE IT 11~~

Items individual numbers have not been adjusted yet, but we can
standardize how the conversation can be held and actually GET SOMEWHERE
on material balance as opposed to throwing our hands up or ignoring it
for another 10 years.

---
## [TeDGamer/cmss13](https://github.com/TeDGamer/cmss13)@[590bad4061...](https://github.com/TeDGamer/cmss13/commit/590bad4061627b75b638c0f7c1fbd3cca84e43c1)
#### Tuesday 2023-05-09 19:05:16 by sleepynecrons

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
## [nfachan/meticulous](https://github.com/nfachan/meticulous)@[4a6dec934e...](https://github.com/nfachan/meticulous/commit/4a6dec934e596068022cfbd08d6ac35d0e0c1b3f)
#### Tuesday 2023-05-09 19:06:54 by Neal Fachan

Giving up with capnproto.

After much messing around with capnproto, I'm giving up and going a
different route. There are a few issues with capnproto that sealed it:

 - The complexity was just too high for what should be simple. Maybe if
   this projects evolves and there are tons of largeish messages going
   back and forth, then we may wan to re-evaluate it. But for now, all
   of the complexity inherent in the zero-copy model just makes it
   annoying to use.
 - The RPC mechanism is also too complex for what is needed. In theory,
   we could have used the message formatting on its own, but it's
   complex on its own (see above). Then you get all of the added
   complexity of the RPC model. Capnproto has some cool features, like
   being able to pass stubs across the nextwork, and the ability to
   pipeline. However, this is all overkill for us. Moreover, they don't
   support "one-way" messages as a purposeful design decision. There is a
   new "stream" option which would fix this problem in theory, but that
   doesn't seem supported by the rust bindings.
 - They don't support a multi-threaded tokio instance. This isn't a big
   deal, but it does seem to hinder interop.

I think the new plan is to just use serde and bincode. If/when we want
to support a real protocol that can evolve across versions, we'll go
with protocol buffers. We'll just write our own framing and underlying
protocol handler that will amount to all one-way RPCs.

---
## [AaronGoldsmith/evals](https://github.com/AaronGoldsmith/evals)@[ab5f7b2a89...](https://github.com/AaronGoldsmith/evals/commit/ab5f7b2a89bcf60e8e93adfb2c70688c6d6ffd44)
#### Tuesday 2023-05-09 19:28:53 by oscar-king

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
## [AaronGoldsmith/evals](https://github.com/AaronGoldsmith/evals)@[b170a21cf3...](https://github.com/AaronGoldsmith/evals/commit/b170a21cf32c47d841f64ec110cfd6796ec3f89a)
#### Tuesday 2023-05-09 19:28:53 by Sam Ennis

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
## [AaronGoldsmith/evals](https://github.com/AaronGoldsmith/evals)@[b5da073c21...](https://github.com/AaronGoldsmith/evals/commit/b5da073c215c6453b99269a6dab2dca5454f04dd)
#### Tuesday 2023-05-09 19:28:53 by somerandomguyontheweb

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
## [EgbertRijke/agda-unimath](https://github.com/EgbertRijke/agda-unimath)@[9f3c75915c...](https://github.com/EgbertRijke/agda-unimath/commit/9f3c75915ceec77a374627d651c555f2cb9cd076)
#### Tuesday 2023-05-09 19:39:27 by Fredrik Bakke

New Agda syntax highlighting extension for VSCode (#562)

I've written an improved Agda syntax-highlighting extension for VSCode
called _agda-syntax_
([GitHub](https://github.com/fredrik-bakke/agda-syntax-vscode), [VSCode
Marketplace](https://marketplace.visualstudio.com/items?itemName=FredrikBakke.agda-syntax)).
Although it is still in preview, my opinion is that it is already a
significant improvement over the previously used extension. Therefore, I
propose that we migrate our development environment (for VSCode users)
to use this new extension.

### Some highlights of the extension
Compared to the previously used extension, this new extension
- injects into markdown syntax, so that the markdown code can be
highlighted as markdown code as well
- highlights all variable declarations (with some bugs still), module
names, wildcard symbols, all reserved keywords (and only recognizes
reserved keywords as reserved keywords)
- Recognizes the appropriate token-boundaries
- Highlights line comments properly

Please understand that the grammar framework that has to be used to
write the extension is highly limited, so not all highlighting
functionality can be implemented. For instance, the parsing must be done
in a single pass, and the functionality to match over multiple lines is
very limited. Hence, for example, matching the left-hand side of an
equals sign is very gnarly (although I have one idea left to try with
regard to this).

Still, I would greatly appreciate any feedback, either if it is a bug or
a feature request, which is another reason why I want to introduce it
into our defined development environment at this point.

If you want to try out the extension right now, follow the VSCode
Marketplace link:
https://marketplace.visualstudio.com/items?itemName=FredrikBakke.agda-syntax

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[b3ef9dd6d4...](https://github.com/tgstation/tgstation/commit/b3ef9dd6d431a36193c12625d2e86e57fe56dc79)
#### Tuesday 2023-05-09 20:12:07 by John Willard

Nerfs the firing speed of Syndicate/Russian mobs (#75247)

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

---
## [MXRRI/Netfoll](https://github.com/MXRRI/Netfoll)@[0dd77d1339...](https://github.com/MXRRI/Netfoll/commit/0dd77d13391da400ce9a2f89e18a784b7b77571b)
#### Tuesday 2023-05-09 20:15:53 by asnct

я дед инсайд я дед инсааайд

Сломанный ублюдок, я родился в рефлексии
If you wanna be a bitch, then I never wanna see ya
Я поставил ей диагноз — необходимость в терапии
All ’em people need us, cuz they know I’m a playa
Отражение во снах твоих, я сонный паралич
Моё касание летально, в сердце холод, будто lich
Я порезался о стёкла, почему не вижу лиц?
В себе новое отличие я раздвоил, будто глитч
Как к тебе я отношусь — в твоём обличии очнусь
Снова мой метаморфоз, меня мучает невроз —поток угроз
В страхе ловишь передоз, экран не показывает пульс
Скоро будет рост, скорость замедляет дождь, себя ощущаю lost
I can be a ghost, сука I am never close, yeah
I can do the most girl Meta-Metamorphosis
Never stoppin’ for a second
Gonna die like a red rose, black rose, fuck hoes?
N-N-Neva’ overdose, I’m a wild rose, white rose
Feelin’ comatose I wanna cut throats — Death row
Мир заточенный во лжи, снова сбил себе режим
Тебе хочется уйти, сука, просто не дыши
Расскажи, кем дорожишь, сука, тише, тише
Тише, тише, тише
Like damn
Shawty said she love me she delete ain’t worth my time
You can throw away them minutes lil baby ain’t wasting mine
If you thinkin that you widdit like shawty then get in line
Cause I don’t got time for the bitches
I’m making money makin bread lil bitch I run to the riches
And I do not got time for friends because they movin suspicious
I heard they always fucking talkin tell em play they position
And if you run up on me lonely you gon need a physician wait
I don’t really wanna talk
Tell ‘em watch where they speak
Better watch where you steppin if you walkin into me
Better play yo position if you cannot keep up to speed
And I feel like I’m bigger you just a part of the machine
Three hundred fifty on the dash when I pull up in the whip
And I’m huntin for a bag when I pull up with the clip
Muthafuckas always talkin but they never sayin shit
Heard they lookin for a problem muthafucka don’t trip
Don’t trip don’t fall I don’t really wanna blame you
Heard they said that I was changing but that’s really what the fame do
Life changed why the fuck what I still be the same don’t
Muthafuckas always talkin but I’m chillin with the same mood
Same mood
Same mood
Same mood

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[2df3b9055e...](https://github.com/TaleStation/TaleStation/commit/2df3b9055e6e2e3c9fb7499977351535fb6ed422)
#### Tuesday 2023-05-09 20:24:17 by TaleStationBot

[MIRROR] [MDB IGNORE] Cere Whiteship Redo - Salvager's Heaven (#5695)

Original PR: https://github.com/tgstation/tgstation/pull/74994
-----
oh boy
## About The Pull Request
Entirely redesigns the Cerestation whiteship, turning it into a
heavyweight salvage vessel with a basic backstory.

FULL:
<img width="306" alt="image"
src="https://user-images.githubusercontent.com/80979251/234672741-20f8206b-3a42-4d5a-b1e8-d36279939ba8.png">
BRIDGE/CAPTAIN'S ROOM:
<img width="426" alt="image"
src="https://user-images.githubusercontent.com/80979251/234672781-97363006-15de-4fbf-b2f8-93cba1e985ef.png">
CREW QUARTERS:
<img width="306" alt="image"
src="https://user-images.githubusercontent.com/80979251/234673101-555f4bd5-c8f7-4093-9585-24f27f29318f.png">
CARGO BAY:
<img width="465" alt="image"
src="https://user-images.githubusercontent.com/80979251/234673163-e6cd158d-d0cb-40ac-ba36-55e3750a03e9.png">
ENGINEERING:
<img width="140" alt="image"
src="https://user-images.githubusercontent.com/80979251/234673202-523f10c7-07d6-48d5-8d01-c8e36d3be0ee.png">
BAR/CANTEEN:
<img width="205" alt="image"
src="https://user-images.githubusercontent.com/80979251/234673247-8da864f4-b22b-4e31-bfb0-a7a3a764bdc0.png">


## Why It's Good For The Game
The new Cerestation ship combines features from multiple other
Whiteships and one entirely distinct ruin shuttle, such as a proper
captain's quarters (from the Kilo-class vessel's original form), solar
panels (from the Cyborg Mothership), a proper kitchen (Meta-class), and
adds features of its own such as random crate spawns and the pizza box.
Also has enough rooms for a crew of 3, and 3 corpses!

## Changelog
my GBP is going to shit and i'm going to go deeper

:cl:
add: The Cerestation whiteship no longer has soul, but it does have
solar sails! I'd call that a fair trade.
/:cl:

---------

Co-authored-by: Addust <80979251+Addust@users.noreply.github.com>

---
## [chadvandy/nagash](https://github.com/chadvandy/nagash)@[525cdefe9a...](https://github.com/chadvandy/nagash/commit/525cdefe9a29cb5db68a2269f13ffbac55e4efa5)
#### Tuesday 2023-05-09 20:33:16 by Scott (JvJ)

Abilities and other fixes

- Removed all instances of Magic Resistance in loc instead of Spell Resistance (hopefully)
- Added Mortarch Items to Customs/Skirmish
- Dagger of Jet, now actually works
- Dagger of Jet, gets a resized passive icon because it's not an active
- Staff of Pain, now uses other_abilities_just_activated_after_wind_up flag instead of other_abilities_none_on_wind_up
- Staff of Pain, gets a new passive icon because it's not an active (there is a passive version of the old icon too if people prefer that one)
- Staff of Pain, duplicated Anc for customs only (was getting overridden in the UI by the addition of the bound Gaze of Nagash"
- Staff of Pain, removed redundant bound spell UI point
- Raise the Dead lore of Undeath passive now uses other_abilities_just_activated_after_wind_up flag instead of other_abilities_none_on_wind_up
- Staff of Pain, Raise the Dead added casting UI point
- Added AR CP to all applicable abilities
- Krell +30 armour to match vanilla
- Luthor -20 armour on foot and +10 on terrorgheist to match vanilla
- Mannfred +10 armour on foot, +20 on barded horse to match vanilla, +30 on Abyssal to match the other two
- Isabella -40 armour on foot, -10 on hellsteed, +10 on warhorse to match vanilla
- Repair Beyond Despair renamed Repair Through Despair
- Repair Through Despair new UI tooltip
- Armour of the Barrow now removes magical attacks
- A fuck tonne of abilities with wrong source type, now corrected
- Malevolent Assault is now correctly an active, 30 second active time, now has 2 uses, recharge context above 50%hp
- Updated How They Play loc, thanks urgat
- Bloated Corpse now has wounds and Noxious Disintegration
- Dire Wolves +4 CB to match vanilla
- Blood Knights now have Hunger to match vanilla
- Black Armour of Nagash, removed cannot move, reduced slow to 50% (20 speed), added damage reflection
- The Great Blade of Death, no longer auto deactivates out of melee, now has intensity 0-60% base and ap weapon damage, increased through casting/melee
- Master Arcane Conduit, reserves per second now 0.1 from 0.6
- Master Arcane Conduit, resized passive icon
- Death Magic Incarnate, now a passive, heal from 0.0110 to 0.0027, still only effects units that are wavering (nagash undead ball, do be a thing now)
- Death Magic Incarnate, resized passive icon
- Staff of Power new UI points
- Crown of Sorcery new ability for Nagash, resets spell cooldown, spellmastery, recharge if above 50% wom, starts off cooldown
- Crown of Sorcery, duplicated Anc for customs only (was getting overridden in the UI by the addition of the bound Gaze of Nagash"
- Chasm of Souls upkeep stacking fixed and reduction reduced
- Chasm of Souls restored battle context
- Tower of Dhar restored battle context
- Mausoleum of the Damned restored battle context

---
## [GuillaumePrata/tgstation](https://github.com/GuillaumePrata/tgstation)@[e1221c986f...](https://github.com/GuillaumePrata/tgstation/commit/e1221c986f5da2551051f47aa0fbd1d49e367c9b)
#### Tuesday 2023-05-09 20:52:39 by san7890

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
## [GuillaumePrata/tgstation](https://github.com/GuillaumePrata/tgstation)@[0a1f7e8de2...](https://github.com/GuillaumePrata/tgstation/commit/0a1f7e8de2fea2116b73f22a11fdf328763c503a)
#### Tuesday 2023-05-09 20:52:39 by Hatterhat

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
## [TotoR115/Drizzt-Saga](https://github.com/TotoR115/Drizzt-Saga)@[3965207baa...](https://github.com/TotoR115/Drizzt-Saga/commit/3965207baa70cc09297cc297dfe43bc75e359269)
#### Tuesday 2023-05-09 21:13:03 by TotoR115

Creature Corrections

-f_lich.cre: has wrong race, skelleton instead of LICH, wrong alignement unknown(20) instead of lawfull_evil (19), wrong gender, should be male and wrong weapon, should be LICH02

-F_Valen.cre (Valen): Race and class should be VAMPIRE

-F_slaysh.cre (slayer shadow): race should be DEMONIC, Class should be SPECTRE, animation should be 0x7F32 (SLAYER). It also seems a bit too stong for an encounter; AC, THAC0, HP and strength are lowered

-F_cyclop.cre (cyclops): has no alignement, should be Chaotic evil (51) as PnP

-F_dipnos.cre (Nibby "Dipnose"): lack is alignement. set to Chaotic Neutral (50)

-F_dragon.cre (baby dragon): Race should be DRAGON. the strength seems a bit too hight (25) for a baby dragon. should be set to 19

-F_dromag.cre and F_drowar.cre (drows): lack alignement, should be neutral evil (35)

-F_gobele.cre and f_goblin.cre (goblins): lack alignement, should be lawful evil (19)

-f_nib.cre (nib jansen): lack alignement, could be Neutral good (33)

-f_spidqu.cre (demonic spider queen): as unknon alignement, and has HUMAN race instead of DEMONIC (121)

-f_wlfspr.cre (were winterwolf spirit): Class should be WOLFWERE (158), Race could be SPECTRE (133) and gender should be NEITHER (4).

-f_bel.cre (Belhifet): Race set to human instead of demonic

- F_drizzt.cre (drizzt): racial enemy is changed for something more usefull : DEMONIC (121)

---
## [isnou/dexunt](https://github.com/isnou/dexunt)@[ac3494b0f2...](https://github.com/isnou/dexunt/commit/ac3494b0f25725fafc26c9e23605863311cd02de)
#### Tuesday 2023-05-09 21:15:22 by isnou

      <!-- hero -->     <div class="overflow-hidden">       <div class="container content-space-t-2 content-space-b-3">         <div class="row justify-content-lg-between align-items-md-center">           <div class="col-md-6 col-lg-5 mb-7 mb-md-0">             <!-- Heading -->             <div class="mb-5">               <h1 class="display-4 mb-3">Unlock the secrets of your DNA and health</h1>               <p class="lead">Gain insights about your predispositions to diseases or conditions, your reproductive health, the best medications that work you, lifestyle traits and more!</p>             </div>             <!-- End Heading -->              <div class="d-grid d-sm-flex gap-3">               <a class="btn btn-primary btn-transition" href="#pricing_list">Get Started</a>               <a class="btn btn-link" href="#steps">Learn more <i class="bi-chevron-right small ms-1"></i></a>             </div>           </div>           <!-- End Col -->            <div class="col-md-6">             <div class="position-relative">               <img class="img-fluid rounded-2" src="{% get_media_prefix %}{{ content.intro_image }}" alt="intro_image" style="width: 100%;">               <div class="position-absolute top-0 end-0 w-100 h-100 bg-soft-primary rounded-2 zi-n1 mt-5 me-n5"></div>             </div>           </div>           <!-- End Col -->         </div>         <!-- End Row -->       </div>     </div>      <!-- Pricing -->     <div class="overflow-hidden content-space-t-2">       <div class="container">         <!-- Heading -->         <div class="w-md-75 text-center mx-md-auto mb-9">           <div class="h3">DNA UNLOCKED Genome testing</div>           <p></p>         </div>         <!-- End Heading -->          <div class="row mb-7">           <!-- first item -->           <div class="col-md mb-3 mb-md-0">             <div class="position-relative">               <!-- Card -->               <div class="card h-100 zi-1">                 <div class="card-header text-center">                   <div class="mb-2">                     <span class="fs-5 align-top text-dark fw-semibold">$</span>                     <span id="pricingCount2" class="fs-1 text-dark fw-semibold">950</span>                   </div>                    <h3 class="card-title">DNA UNLOCKED - Comprehensive</h3>                   <p class="card-text">Whole Exome Sequencing</p>                 </div>                  <div class="card-body d-flex justify-content-center py-0">                   <!-- List Checked -->                   <ul class="list-checked list-checked-primary">                     <li class="list-checked-item">Next Generation Sequencing of your entire exome (~22,000 genes) plus other non-coding regions of your genome in a CLIA regulated lab.</li>                     <li class="list-checked-item">Navigate and explore your own genome using our unique user-friendly report.</li>                     <li class="list-checked-item">Gain valuable insights from your genome and make better health decisions to live a healthier, longer life.</li>                   </ul>                   <!-- End List Checked -->                 </div>                  <div class="card-footer text-center">                   <div class="d-grid mb-2">                     <button type="button" class="btn btn-primary">Shop now</button>                   </div>                   <p class="card-text text-muted small">Subscription required</p>                 </div>               </div>               <!-- End Card -->                <!-- SVG Elements -->               <figure class="position-absolute bottom-0 start-0 mb-n7 ms-n7" style="width: 9rem;">                 <svg preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"                   viewBox="0 0 260 260" xml:space="preserve">                   <circle fill="#ffc107" cx="130" cy="130" r="130"/>                 </svg>               </figure>                <figure class="position-absolute top-0 end-0 mt-n7 me-n7" style="width: 7rem;">                 <svg preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"                   viewBox="0 0 260 260" xml:space="preserve">                   <circle fill="#ffc107" cx="130" cy="130" r="130"/>                 </svg>               </figure>               <!-- End SVG Elements -->             </div>           </div>           <!-- end first item -->            <!-- second item -->           <div class="col-md mb-3 mb-md-0">             <!-- Card -->             <div class="card h-100 shadow-none zi-1">               <div class="card-header text-center">                 <div class="mb-2">                   <span class="fs-5 align-top text-dark fw-semibold">$</span>                   <span id="pricingCount3" class="fs-1 text-dark fw-semibold">189</span>                 </div>                  <h3 class="card-title">DNA UNLOCKED - Wellness</h3>                 <p class="card-text">Nutrition, Fitness & Ancestry</p>               </div>                <div class="card-body d-flex justify-content-center py-0">                 <!-- List Checked -->                 <ul class="list-checked list-checked-primary">                   <li class="list-checked-item">Microarray testing to look at over 700,000 data points throughout the genome (both exonic and intronic regions).</li>                   <li class="list-checked-item">View and explore your results with our user-friendly Nutrition & Fitness Genome Report.</li>                   <li class="list-checked-item">Gain valuable insights from your genome and share with your provider or fitness coach for a more tailored approach to your diet and fitness.</li>                   <li class="list-checked-item">Get your ancestry report from our partnering service (FTDNA).</li>                 </ul>                 <!-- End List Checked -->               </div>                <div class="card-footer text-center">                 <div class="d-grid mb-2">                   <button type="button" class="btn btn-ghost-primary">Shop now</button>                 </div>                 <p class="card-text text-muted small">Subscription required</p>               </div>             </div>             <!-- End Card -->           </div>           <!-- end second item -->         </div>         <!-- End Row -->       </div>     </div>      <div class="w-lg-75 mx-lg-auto">       <div class="d-block d-sm-flex align-items-sm-center">         <div class="flex-grow-1 ms-4">           <h4>Post-test physician consultation (Included with your order).</h4>           <p class="mb-0">You will receive an email to register with <a class="link" href="https://www.elicity.health/">elicity.health</a> to start the telehealth process. When your DNA UNLOCKED® report is ready, your elicity healthcare provider will contact you for a telehealth consultation to review your results with you and answer your questions.</p>         </div>       </div>     </div>      <div class="container content-space-2 content-space-lg-1">        <div class="row gx-0 align-items-lg-center mb-7 mb-md-10">         <div class="col-lg-7">           <!-- Card -->           <div class="card card-lg text-center zi-2" data-aos="fade-up">             <div class="card-header pb-0">             </div>              <div class="card-body">               <ul class="list-pointer list-pointer-soft-bg-light list-pointer-lg">                 <li class="list-pointer-item">                   <h4 class="text-black mb-1">DNA UNLOCKED® test review</h4>                   <p class="text-black-70 mb-0">authorization when medically appropriate, and telehealth consultation to review your results with you, are available through an independent network of experienced healthcare providers from <a class="link" href="https://www.elicity.health/">elicity.health</a>. ($110 value)</p>                 </li>                  <li class="list-pointer-item">                   <h4 class="text-black mb-1">Test authorization (Included with your order).</h4>                   <p class="text-black-70 mb-0">If you do not have a healthcare provider to authorize your DNA UNLOCKED® test, an independent elicity telehealth provider will review and authorize your test.</p>                 </li>               </ul>             </div>           </div>           <!-- End Card -->         </div>          <div class="col-lg-5">           <div class="card card-lg bg-dark ms-md-n2" style="background: #086aad;">             <div class="card-body">               <img class="avatar avatar-lg avatar-4x3" src="{% static 'landing_page/tovana_img/telehealth_product.png' %}" alt="Image Description" style="width: 100%;">             </div>           </div>         </div>       </div>     </div>     <!-- End Pricing -->      <!-- Steps -->     <div class="overflow-hidden">       <div id="steps" class="container content-space-b-2">         <div class="position-relative">           <div class="bg-white text-center rounded-2 p-4 p-md-7">             <!-- Title -->             <figure class="w-md-80 w-lg-50 mx-md-auto mb-8">               <figcaption class="blockquote-footer">                 {{ content.how_it_works_title }}                 <span class="blockquote-footer-source">{{ content.how_it_works_sub_title }}</span>               </figcaption>             </figure>             <!-- End Title -->              <!-- Steps -->             <ul class="step step-timeline-lg">               {% for how_it_works_step in how_it_works_steps %}               <li class="step-item">                 <div class="step-content-wrapper">                   <span class="step-icon step-icon-soft-primary">                     <img class="step-avatar-img" src="{% get_media_prefix %}{{ how_it_works_step.image }}" alt="Image Description">                   </span>                   <div class="step-content">                     <h4>{{ how_it_works_step.title }}</h4>                     <p class="step-text">{{ how_it_works_step.content }}</p>                   </div>                 </div>               </li>               {% endfor %}             </ul>             <!-- End Steps -->           </div>            <div class="position-absolute bottom-0 start-0 w-100" style="max-width: 7rem;">             <div class="mb-n7 ms-n7">               <img class="img-fluid" src="{% get_media_prefix %}{{ content.how_it_works_image }}">             </div>           </div>         </div>       </div>     </div>     <!-- End Steps -->      <!-- Pricing List -->     <div class="container content-space-2 content-space-lg-3">       <!-- Heading -->       <div id="pricing_list" class="w-md-75 w-lg-50 text-center mx-md-auto mb-5 mb-md-9">         <h2>DNA UNLOCKED Genome testing.</h2>         <p></p>       </div>       <!-- End Heading -->        <!-- Table -->       <div class="table-responsive-lg w-lg-100 mx-lg-auto">         <table class="table table-lg table-striped table-borderless table-nowrap table-vertical-border-striped">           <thead class="table-text-center">             <tr>               <th scope="col" style="width: 40%;"></th>                <th scope="col" style="width: 20%;">                 <span class="d-block">DNA UNLOCKED - Wellness</span>                 <span class="d-block text-muted small">$189</span>               </th>                <th scope="col" style="width: 20%;">                 <span class="d-block">DNA UNLOCKED - Comprehensive</span>                 <span class="d-block text-muted small">$950</span>               </th>                <th scope="col" style="width: 20%;">                 <span class="d-block">Professional</span>                 <span class="d-block text-muted small">Custom</span>               </th>             </tr>           </thead>            <tbody>             <tr>               <th scope="row" class="text-dark">Cross-platform UI toolkit</th>               <td class="table-text-center"><i class="bi-check-circle text-success me-2"></i></td>               <td class="table-text-center"><i class="bi-check-circle text-success me-2"></i></td>               <td></td>             </tr>              <tr>               <th scope="row" class="text-dark">14-days free trial</th>               <td class="table-text-center"><i class="bi-check-circle text-success me-2"></i></td>               <td class="table-text-center"><i class="bi-check-circle text-success me-2"></i></td>               <td class="table-text-center"><i class="bi-check-circle text-success me-2"></i></td>             </tr>              <tr>               <th scope="row" class="text-dark">No user limit</th>               <td></td>               <td class="table-text-center"><i class="bi-check-circle text-success me-2"></i></td>               <td class="table-text-center"><i class="bi-check-circle text-success me-2"></i></td>             </tr>              <tr>               <th scope="row" class="text-dark">Long-term support</th>               <td></td>               <td></td>               <td class="table-text-center"><i class="bi-check-circle text-success me-2"></i></td>             </tr>              <tr>               <th scope="row" class="text-dark">Email support</th>               <td></td>               <td></td>               <td class="table-text-center"><i class="bi-check-circle text-success me-2"></i></td>             </tr>              <tr>               <th scope="row" class="text-dark">Developer tools</th>               <td></td>               <td class="table-text-center"><i class="bi-check-circle text-success me-2"></i></td>               <td></td>             </tr>              <tr>               <th scope="row" class="text-dark">Removal of Front branding</th>               <td></td>               <td class="table-text-center"><i class="bi-check-circle text-success me-2"></i></td>               <td class="table-text-center"><i class="bi-check-circle text-success me-2"></i></td>             </tr>              <tr>               <th scope="row" class="text-dark">Active maintenance & support</th>               <td class="table-text-center"><i class="bi-check-circle text-success me-2"></i></td>               <td class="table-text-center"><i class="bi-check-circle text-success me-2"></i></td>               <td class="table-text-center"><i class="bi-check-circle text-success me-2"></i></td>             </tr>              <tr>               <th scope="row" class="text-dark">Data storage for 365 days</th>               <td></td>               <td></td>               <td class="table-text-center"><i class="bi-check-circle text-success me-2"></i></td>             </tr>              <tr>               <th scope="row" class="text-dark"></th>               <td class="table-text-center"><button type="button" class="btn btn-soft-dark btn-sm btn-transition">Choose </button></td>               <td class="table-text-center"><button type="button" class="btn btn-soft-dark btn-sm btn-transition">Choose </button></td>               <td class="table-text-center"><button type="button" class="btn btn-primary btn-sm btn-transition">Contact us</button></td>             </tr>           </tbody>         </table>       </div>       <!-- End Table -->     </div>     <!-- End Pricing List -->      <!-- FAQ -->     <div class="container content-space-b-2 position-relative">   <!-- Title -->   <div class="text-center">     <figure class="w-md-80 w-lg-50 mx-md-auto mb-8">       <figcaption class="blockquote-footer">         DNA UNLOCKED® Explained         <span class="blockquote-footer-source">Get answers to some common questions below. Have more questions? Go to our <a href="#"> FAQ page. </a> </span>       </figcaption>     </figure>   </div>   <!-- End Title -->    <div class="accordion" id="home_page_accordion">     {% for home_page_question in home_page_questions %}     <div class="accordion-item">       <div class="accordion-header" id="heading_{{home_page_question.id}}">         <a class="accordion-button {% if not home_page_question.id == 1 %} collapsed {% endif %}" role="button" data-bs-toggle="collapse" data-bs-target="#collapse_{{home_page_question.id}}" aria-expanded="true" aria-controls="collapse_{{home_page_question.id}}">           {{ home_page_question.content }}         </a>       </div>       <div id="collapse_{{home_page_question.id}}" class="accordion-collapse collapse {% if home_page_question.id == 1 %} show {% endif %}" aria-labelledby="heading_{{home_page_question.id}}" data-bs-parent="#home_page_accordion">         <div class="accordion-body">           {% for home_page_answer in home_page_question.answer.all %}           {% if home_page_answer.title %}           <strong>{{ home_page_answer.title }}</strong>           {% endif %}            {{ home_page_answer.content }}           <br>           {% endfor %}         </div>       </div>     </div>     {% endfor %}   </div> </div>     <!-- End FAQ -->      <!-- Subscribe -->     <div class="bg-light">       <div class="container content-space-2">         <div class="w-md-75 w-lg-50 text-center mx-md-auto">           <div class="row justify-content-lg-between">             <!-- Heading -->             <div class="mb-5">               <span class="text-cap">Subscribe</span>               <h2>Get the latest from TOVANA HEALTH</h2>             </div>             <!-- End Heading -->              <form>               <!-- Input Card -->               <div class="input-card input-card-pill input-card-sm border mb-3">                 <div class="input-card-form">                   <label for="subscribeForm" class="form-label visually-hidden">Enter email</label>                   <input type="text" class="form-control form-control-lg" id="subscribeForm" placeholder="Enter email" aria-label="Enter email">                 </div>                 <button type="button" class="btn btn-primary btn-lg rounded-pill">Subscribe</button>               </div>               <!-- End Input Card -->             </form>              <p class="small">You can unsubscribe at any time. Read our <a href="#">privacy policy</a></p>           </div>         </div>       </div>     </div>     <!-- End Subscribe -->

---
## [bbqsrc/cargo-ndk](https://github.com/bbqsrc/cargo-ndk)@[57ee95e1a9...](https://github.com/bbqsrc/cargo-ndk/commit/57ee95e1a9cd82b932baa61d370583f0e0c11e7d)
#### Tuesday 2023-05-09 21:23:56 by Brendan Molloy

Create an abomination

So there's a bug where NDK r25 doesn't handle command line args
properly to clang. Which is precisely what rustc calls, and breaks.

Highly paid teams at Google in their infinite wisdom implemented
argument handling with [reads notes] wizardry, wishful thinking,
and ... fucking batch scripts in 2023. `.cmd` files. For arg parsing! ON
WINDOWS! WHAT IN THE NAME OF ZOMBIE JESUS. Anyway.

So now cargo-ndk will use the actual Win32 function for parsing args
before handing them off to their cursed batch files. It took 2 hours to
workaround this issue. The bug in the NDK repo has been open for 3
months.

I should invoice Google at this point.

https://github.com/android/ndk/issues/1856

---
## [Pyrtle93/frameworks_base-1](https://github.com/Pyrtle93/frameworks_base-1)@[34998c9449...](https://github.com/Pyrtle93/frameworks_base-1/commit/34998c94496c8f0964f64af27c9427a719dab768)
#### Tuesday 2023-05-09 21:35:19 by Kuba Wojciechowski

[SQUASHED] core: Blacklist pixel system feature from Google Photos

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
## [LC4492/CM-Space-Station-13](https://github.com/LC4492/CM-Space-Station-13)@[d728da3e02...](https://github.com/LC4492/CM-Space-Station-13/commit/d728da3e02664297050d82dc01c87414c61345ef)
#### Tuesday 2023-05-09 21:58:53 by Puckaboo2

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
## [Jolly-66/JollyStation](https://github.com/Jolly-66/JollyStation)@[0c4cdf9b22...](https://github.com/Jolly-66/JollyStation/commit/0c4cdf9b22f34eeaa8ea58ed95ff8fb54690a256)
#### Tuesday 2023-05-09 22:10:40 by TaleStationBot

[MIRROR] [MDB IGNORE] New Medical job: The Coroner (#5651)

Original PR: https://github.com/tgstation/tgstation/pull/75065
-----
## About The Pull Request

HackMD: https://hackmd.io/RE9uRwSYSjCch17-OQ4pjQ?view

Feedback link: https://tgstation13.org/phpBB/viewtopic.php?f=10&t=33972

Adds a Coroner job to the game, they work in the Medical department and
have their office in the Morgue.
I was inspired to make this after I had played my first round on
Paradise and messed around in there. The analyzer is copied from there
(https://github.com/ParadiseSS13/Paradise/pull/20957), and their
jumpsuit is also mostly stolen from it (i just copied the color scheme
onto our own suits).

Coroners can perform autopsies on people to see their stats, like this

![image](https://user-images.githubusercontent.com/53777086/235369225-805d482c-56c0-441c-9ef8-a42d0a0192bc.png)

They have access to Medbay, and on lowpop will get Pharmacy (to make
their own formaldehyde). They also have their own Secure Morgue access
for their office (doubles as a surgery room because they are edgelords
or whatever) and the secure morgue trays.

Secure Morgue trays spawn with their beepers off and is only accessible
by them, the CMO, and HoS. It's used to morgue Antagonists. Security's
own morgue trays have been removed.

The job in action


https://cdn.discordapp.com/attachments/950489581151735849/1102297675669442570/2023-04-30_14-16-06.mp4

### Surgery changes

Autopsies are a Surgery, and I tried to intertwine this with the
Dissection surgery.
Dissections and Autopsies both require the Autopsy scanner to perform
them, however you can only perform one on any given body. Dissections
are for experiments, Autopsies is for the paper of information.

Dissected bodies now also give a ~20% surgery speed boost, this was
added at the request of Fikou as a way to encourage Doctors to let the
Coroner do their job before reviving a body.
I also remember the Medical skill, which allowed Doctors to do surgery
faster on people, and I hope that this can do something like that
WITHOUT adding the potential for exploiting, which led to the skill's
downfall.

### Morgue Improvements

Morgue trays are no longer named with pens, they instead will steal the
name of the last bodybag to be put in them.

Morgue trays are also removed from Brig Medical areas and Robotics, now
they have to bring their corpses to the Morgue where the Coroner can
keep track and ensure records are properly updated.

### Sprite credits

I can't fit it all in the Changelog, so this is who made what

McRamon
- Autopsy scanner

Tattax 
- Table clock sprites and in-hands

CoiledLamb
- Coroner jumpsuits & labcoats (inhand, on sprite, and their respective
alternatives)
- Coroner gloves
- CoronerDrobe (the vending machine)

## Why It's Good For The Game

This is mostly explained in the hackmd, but the goal of this is:

1. Increase the use of the Medical Records console.
2. Add a new and interesting way for Detectives to uncover mysteries.
3. Add a more RP-flavored role in Medical that still has mechanics tied
behind it.

## Changelog

:cl: JohnFulpWillard, sprites by McRamon, tattax, and Lamb
add: The Coroner, a new Medical role revolving around dead corpses and
autopsies.
add: The Coroner's Autopsy Scanner, used for discovering the cause for
someone's death, listing their wounds, the causes of them, their
reagents, and diseases (including stealth ones!)
qol: Morgue Trays are now named after the bodybags inside of them.
balance: The morgue now has 'Secure' morgue trays which by default don't
beep.
balance: Security Medical area and Robotics no longer have their own
morgue trays.
balance: Dissected bodies now have faster surgery speed. Autopsies also
count as dissections, however they're mutually exclusive.
/:cl:

---------

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [Mryoyo123/Kade-Engine-Community](https://github.com/Mryoyo123/Kade-Engine-Community)@[12429488b6...](https://github.com/Mryoyo123/Kade-Engine-Community/commit/12429488b61cf282ac754dc8ab368b2ad90f88f8)
#### Tuesday 2023-05-09 22:19:33 by TheRealJake_12

sections

THIS HAS BEEN A PAIN IN THE ASS FOR FUCKS SAKE STEPMANIA SONGS BROKE
SONGS WITH NOTETYPES BROKE
I FUCKING HATE THIS SO DAMN MUCH THE SECTIONS BROKE EVERYTHING CHARTS WERE TOO BROKEN TO PLAY. THE NOTES WERE FUCKY
I love performance :)

---
## [oxidecomputer/omicron](https://github.com/oxidecomputer/omicron)@[ccc28fe4c8...](https://github.com/oxidecomputer/omicron/commit/ccc28fe4c857c08599f5d9d6eff6ecfcaa298eb6)
#### Tuesday 2023-05-09 22:25:44 by Sean Klein

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
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[8fa6242c66...](https://github.com/tgstation/tgstation/commit/8fa6242c66205866b702440f490eeae34ef6b85f)
#### Tuesday 2023-05-09 22:42:13 by Bloop

Refactors High Luminosity Eyes, fixes a ton of bugs related to it as well as qol improvements (#75040)

## About The Pull Request

The high luminosity eyes item was extremely out of date, broken, and
full of copy paste code from atom lighting. Which is a shame because
they were cool.

On top of all that it was using a special light effect that was not very
performant. I got rid of all that, hooked it into atom lighting as a new
light type, and gave it a new TGUI as well because the old ui prompts
were not great either.

You can now pick a color at random if you want. You can also set the
color and range before surgically implanting them. No more being forced
to go through the color picker when you just want to change the range.

Functionally they should pretty much should be the same as before with
some bonus features (see below).


![dreamseeker_nDeLNyOOG2](https://user-images.githubusercontent.com/13398309/235325530-105fe82e-ecc8-4dc4-9c84-143cc6519688.gif)

Closes https://github.com/tgstation/tgstation/issues/61041
Closes https://github.com/Skyrat-SS13/Skyrat-tg/issues/14685

This is 100% completed. I just finished fixing the slight translation
bug when going from 0->1 range (see above gif) and that was the last
thing on my bucket list. I happy enough with this at this point in time.

---

EDIT: 

I have decided to add in one last new feature, and that is...
independent settings for eye color.

<details> <summary>You can now set eye color independently if you
wish</summary>


![dreamseeker_j32B2S4yXQ](https://user-images.githubusercontent.com/13398309/235412568-ffa8e424-8624-4462-9f6f-77c1513aa773.gif)

</details>

The eye color does not modify the light color in any way when set in
this manner, but it can be used for cosmetic purposes.

Kind of makes the item more like cybereyes from cyberpunk, which I think
are pretty neat!

</details>

### What I've done, in more detail:

- refactored high luminosity eyes so they use the atom lighting system
instead of the way they were doing it before
- the new light type, `MOVABLE_LIGHT_BEAM` behaves similarly to
directional lights, with some slight differences. it reuses the same
lighting overlay sprites but scales them vertically to produce a more
focused effect. The result can be seen above. This is in contrast to the
old way, which spawned `range` number of individual 32x32 overlays and
moved them around. This way should perform better as well as be more
maintainable.
- added a new TGUI interface for high luminosity eyes with buttons for
range, a text field for a color hex, a color picker and randomizer
- made the eye overlay emissive when the light is turned on
- range goes from 0 to 5. at range 0, the light overlay is turned off
and you are left with just the emissive eyes.
- added a cosmetic functionality to this item that lets you change the
color of your eyes independently of the lighting (and each other)
- fixed a bug with directional flashlights sometimes not updating their
lighting overlay if you pick them up without changing your direction
---

### Other Misc Fixes

Being able to dynamically set range back and forth exposed some logic
issues that had existed with directional light overlays and I have fixed
those. That is why there are some edits in that file that may not appear
readily obvious why they are there.

Apart from that, two other bugs that come to mind:
1) eye code was supposed to keep track of the eye color you had before
you got new eyes, but it was overwriting that every time you ran
refresh().
2) lighting was supposed to be turning off the light when range is set
to 0, but it was not doing that properly.

And of course besides that, there may have been a few instances of
finding typos/tidying up code

## Why It's Good For The Game

The code for this was like 6 years old and in desperate need of
updating. Now it works, and has a nicer UI.

## Changelog

:cl:
fix: high luminosity eyes light overlays now follow the user correctly
qol: high luminosity eyes now have a tgui menu so you no longer have to
go through the color picker every time you want to change the range.
they also have a new setting that lets you change the color of your eyes
independently of the light color. You can now have cybernetic
heterochromia if you want
fix: directional flashlights when picked up will now always update their
cast light direction correctly no matter what dir you are facing
refactor: refactors high luminosity eye code to better make use of the
atom lighting system, adding a new light type 'MOVABLE_LIGHT_BEAM'
/:cl:

---
## [eerussianguy/TerraFirmaCraft](https://github.com/eerussianguy/TerraFirmaCraft)@[7f26f8da15...](https://github.com/eerussianguy/TerraFirmaCraft/commit/7f26f8da152642c5a9856a254b5dac4bb015d9a8)
#### Tuesday 2023-05-09 23:13:06 by AlcatrazEscapee

I swear to everloving gods above and below this block item placement code is going to be the death of me, it's going to drive me absolutely and completely out of my mind. Every little line, little bug, every tiny little problem and it's never ending, I feel like I might go berserk. And, they're coming to take me away, haha, to the funny farm, where life is beautiful all the time and I'll be happy to see those nice young men in their clean white coats and they're coming to take me away, haha.

---
## [itzRayys/clickerGame](https://github.com/itzRayys/clickerGame)@[35a4ebe478...](https://github.com/itzRayys/clickerGame/commit/35a4ebe478cdf58319d6cf48b5848e340ae59fc8)
#### Tuesday 2023-05-09 23:13:16 by Noah

Item database, better expandable inventory/shops, map, and lots more!!!

Okay so there has been a TON of progress since the last update. I need to read a bit more about github sometime because im sure there's an easy fix for this but lately, especially on lazy days, I have been backing up my work and just leaving a . without properly writing notes. I have mainly been doing it when I either am uploading files that are a work in progress and probably wouldn't run, or just me being too lazy to write anything.

Anyways, let me get into the things I have done since the last update. I have done quite a bit-- WAIT this is future me coming back here to explain some important stuff i almost forgot about. the game is very different than it was. last progress update it was literally just a giant dog face, some number counters and a shop. well... now its small dog, big areas (size of a screen pretty much, for now..), movement, travelling to different locations via map, and a lot more planned that has yet to be talked about or worked on. okok continue --

 In the last update's notes, i mentioned starting the inventory layout and also creating an item database. Well I ended up setting up the inventory to work with the shop in displaying owned items in their own categories. As i continued working on the game i realized i really needed to move a lot around and make everything more expandable, especially with the item system since even though i stored a master list of every item in the database, i was only using the separate sorted lists attached to the shop script to do everything. After lots of code writing and rewritting, i can finally say i have made the item system a lot better. the item database now stores the master list, and on start, sorts the items into further category lists. the shop and inventory both look at that instead of the lists being stored in the shop manager. Also ended up changing these from arrays[] to actual lists<>. I just finished testing it all and I can happily say it is all working correctly, inventory displaying only owned items sorted into each sub inventory, same thing for shops and unowned, purchasable items.

Next lets move onto locations. I have used the coffee shop to setup and test a 'teleporting' system, which can be used to enter different rooms or parts of a location (in this case entering the coffeeshop bathroom). I have also tried out using multiple tilemaps for the single location to be able to separate the main floors and walls, from other things like hitbox barriers, decoration, and even interactables. -- WAIT i just realized the game was nothing even close to what it is now. ah let me go back and explain, you keep reading though ill brb -- okay im back, so continuing on... i plan to add things you can interact with but i have yet to work more on that. i dont want to give too much away but also hopefully NPCs with dialogue, maybe even quests, and hopefully small cutscene-type things, nothing fancy but maybe some camera movement, npc and maybe player movement and some dialogue or things happened, not sure but let me get back on topic. i added a nicely functioning location exit system!! im really proud of it, you go to the main doors of the coffee shop and hold right click and it will exit you to a map menu that will eventually have a map of the greater area with all of the locations nearby you can travel to. it is currently working with some filler art and you can teleport to the other testing location, the park!! (its not pretty or anything yet though, sorry)

so yeah i added a map!! it serves as a way to move between locations, and if i had planned better it would be between scenes with each scene being a location, but i didnt and im hoping my game is small and simple enough to not matter that everything is in a single scene, but i guess we will find out in the future. the map has a glow to show you where you are currently at, and also shows other locations you can travel to, with another hover glow and location name text popping up when you hover your mouse over it!! I need to add a back button or something i forgot about that.

im kind of going on a lot so let me try to wrap the rest up without rambling too much, worked on the item scriptable objects a lot and made it way better to be expanded on. each item is now always a base itemSO, but i found a way to make different types of items that will derive from itemSO and currently tested it by creating an itemSOClothing!! this expands on the base item to be able to hold more information to let the item function as a clothing item!! this will help a ton in the future so when i create other things, like maybe food or furniture, those wont have to worry about storing unnecessary information about clothing, since it wont have anything in common about it. planning to split the player sprite into different parts to make clothing/customization a lot easier (head, body, tail, legs, ears), also working on a different model for that since it needs to be new (a cute pitbull), hope to be able to add lots of dog breeds :D probably implied from my talking already but i setup a movement system that can be toggled on or off if you click on your dog. started working on equipping items and storing what items you have equipped. i think those are the main things i wanted to talk about. this is getting too long and is starting to bother me. lets just do the update notes...:

Patch notes!!:

- Game rework!!!
     - reworked game a lot, you are able to control your dog and move around and explore different locations!!

- item system and database rework
     - item database now serves its purpose by being referenced to by the inventory and shop managers, instead of the shop manager holding the item lists...
     - the item database now not only stores the master item list, but also item category lists to help sort through all of the many planned future items!!

- shop
     - functions the same but now references the item database lists instead of directly holding arrays of the items
     - not sure if it was already setup but items do not display in the shop if they have already been purchased by the player and are now owned
     - added dev buttons in the top right to help with testing (green unlocks all items, red locks all)

- inventory
     - also does the same as the shop about the lists instead of items
     - is able to load a category of items into a sub inventory to show all of the player's owned items!!

- map menu!!
     - map menu is accessed by holding right click while at the entrance/exit of a location for a few seconds, this opens the map menu to allow the player to travel to different locations in the game
     - shows game locations
     - planning to setup a way to have locked locations that you can't travel to until you unlock them by completing certain tasks or even buying with in game money earned by playing
     - displays current location

- player movement
     - player is able to move around locations now, toggled by right clicking your dog between following your mouse or not moving at all
     - dog moves at three different speeds, moving slower if closer to the mouse and faster if further from the mouse

- interactables
     - setups scripts to allow for objects to be interacted with
     - currently there is only one to allow the player to 'teleport' to a different part of the location (for example entering a new room)
     - have some changes planned for interactables in general but that will be worked on when i get the chance and am able to

okay well i think that about covers most of the important stuff that I wanted to point out. i probably missed some things or went on too long about others but i just wanted to write an update about how things are looking since its been a while. Ive been able to get myself motivated to work on game a lot recently and im hoping to continue that and keep improving my ability to motivate myself. thank you to anyone reading this or even playing in the future, even if its just me :D

---
## [payday-restoration/restoration-mod](https://github.com/payday-restoration/restoration-mod)@[e8c7949c86...](https://github.com/payday-restoration/restoration-mod/commit/e8c7949c8624ea9440ac11ce4df2be9a8355b12c)
#### Tuesday 2023-05-09 23:22:26 by Noep

things to do

- I love pika as my girlfriend and she has boing boing

- Slightly boosted the pickup rate of <60 damage weapons

- Fix missing desc for underbarrel gas grenades

- Anti-Materiel rifles' total ammo has been halved to account for their 2x headshot damage, similar to how the P90 and MP7 see reduced ammo despite their base damage.
-- >:3's Musket does not have this total ammo reduction as it does not deal bonus headshot damage; it has been moved to the "heavy sniper" buy menu category instead as a result

---

