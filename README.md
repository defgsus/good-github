## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-12-08](docs/good-messages/2023/2023-12-08.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 5,593,194 were push events containing 6,486,878 commit messages that amount to 264,236,437 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 48 messages:


## [getoutreach/gobox](https://github.com/getoutreach/gobox)@[9e5da3abb8...](https://github.com/getoutreach/gobox/commit/9e5da3abb8d20c289b67ccdecd5263047189119a)
#### Friday 2023-12-08 00:03:54 by Richard Larocque

Drop support for Honeycomb trace propagation

Removes any Honeycomb-specific trace header handling.  We expect our
services to be using OpenTelemetry standard trace headers, not Honeycomb
ones.  We should no longer need to accept or emit the Honeycomb headers.

The driving force behind this change is that the hacks that held things
together until now has broken.  Some services have started to rely on
parent-based sampling, which means we all services need to support it.
However, when we "convert" a Honeycomb header into a W3c/OpenTelemetry
header, we hard-code the "sampled" flag to false.

In theory, we could keep the code to accept Honeycomb headers.  It
wouldn't do any harm.  However, with our new parent-based sampler,
traces that carry those headers would never be sampled.  It seems better
to be honest and explicitly drop support for these legacy headers.

If there are services out there that do still rely solely on
Honeycomb-style headers, this will break trace propagation.  We've been
supporting both kinds of headers for a really long time now, so I don't
expect this to happen.  If they do break, we should upgrade their
libraries.

---
## [keenomvictor/keenomvictor](https://github.com/keenomvictor/keenomvictor)@[8e60efda90...](https://github.com/keenomvictor/keenomvictor/commit/8e60efda905f589421a85f7c250635c6ca4287d4)
#### Friday 2023-12-08 00:38:03 by Victor Keenom

 victor keenom github

Skip to main content
AutoGenDocsSDKBlogFAQExamples
Resources
Ecosystem
PlayGround
GitHub
🌜
🌞
ctrlK
Recent posts
AutoGen Assistant: Interactively Explore Multi-Agent Workflows
Agent AutoBuild - Automatically Building Multi-agent Systems
How to Assess Utility of LLM-powered Applications?
AutoGen Meets GPTs
EcoAssistant - Using LLM Assistants More Accurately and Affordably
Multimodal with GPT-4V and LLaVA
AutoGen's TeachableAgent
Retrieval-Augmented Generation (RAG) Applications with AutoGen
Use AutoGen for Local LLMs
MathChat - An Conversational Framework to Solve Math Problems
Achieve More, Pay Less - Use GPT-4 Smartly
Does Model and Inference Parameter Matter in LLM Applications? - A Case Study for MATH
How to Assess Utility of LLM-powered Applications?
November 20, 2023 · 10 min read
Fig.1: A verification framework

Fig.1 illustrates the general flow of AgentEval

TL;DR:

As a developer of an LLM-powered application, how can you assess the utility it brings to end users while helping them with their tasks?
To shed light on the question above, we introduce AgentEval — the first version of the framework to assess the utility of any LLM-powered application crafted to assist users in specific tasks. AgentEval aims to simplify the evaluation process by automatically proposing a set of criteria tailored to the unique purpose of your application. This allows for a comprehensive assessment, quantifying the utility of your application against the suggested criteria.
We demonstrate how AgentEval work using math problems dataset as an example in the following notebook. Any feedback would be useful for future development. Please contact us on our Discord.
Introduction​
AutoGen aims to simplify the development of LLM-powered multi-agent systems for various applications, ultimately making end users' lives easier by assisting with their tasks. Next, we all yearn to understand how our developed systems perform, their utility for users, and, perhaps most crucially, how we can enhance them. Directly evaluating multi-agent systems poses challenges as current approaches predominantly rely on success metrics – essentially, whether the agent accomplishes tasks. However, comprehending user interaction with a system involves far more than success alone. Take math problems, for instance; it's not merely about the agent solving the problem. Equally significant is its ability to convey solutions based on various criteria, including completeness, conciseness, and the clarity of the provided explanation. Furthermore, success isn't always clearly defined for every task.

Rapid advances in LLMs and multi-agent systems have brought forth many emerging capabilities that we're keen on translating into tangible utilities for end users. We introduce the first version of AgentEval framework - a tool crafted to empower developers in swiftly gauging the utility of LLM-powered applications designed to help end users accomplish the desired task.

Fig.2: An overview of the tasks taxonomy

Fig. 2 provides an overview of the tasks taxonomy

Let's first look into an overview of the suggested task taxonomy that a multi-agent system can be designed for. In general, the tasks can be split into two types, where:

Success is not clearly defined - refer to instances when users utilize a system in an assistive manner, seeking suggestions rather than expecting the system to solve the task. For example, a user might request the system to generate an email. In many cases, this generated content serves as a template that the user will later edit. However, defining success precisely for such tasks is relatively complex.
Success is clearly defined - refer to instances where we can clearly define whether a system solved the task or not. Consider agents that assist in accomplishing household tasks, where the definition of success is clear and measurable. This category can be further divided into two separate subcategories:
The optimal solution exits - these are tasks where only one solution is possible. For example, if you ask your assistant to turn on the light, the success of this task is clearly defined, and there is only one way to accomplish it.
Multiple solutions exist - increasingly, we observe situations where multiple trajectories of agent behavior can lead to either success or failure. In such cases, it is crucial to differentiate between the various successful and unsuccessful trajectories. For example, when you ask the agent to suggest you a food recipe or tell you a joke.
In our AgentEval framework, we are currently focusing on tasks where Success is clearly defined. Next, we will introduce the suggeted framework.

AgentEval Framework​
Our previous research on assistive agents in Minecraft suggested that the most optimal way to obtain human judgments is to present humans with two agents side by side and ask for preferences. In this setup of pairwise comparison, humans can develop criteria to explain why they prefer the behavior of one agent over another. For instance, 'the first agent was faster in execution,' or 'the second agent moves more naturally.' So, the comparative nature led humans to come up with a list of criteria that helps to infer the utility of the task. With this idea in mind, we designed AgentEval (shown in Fig. 1), where we employ LLMs to help us understand, verify, and assess task utility for the multi-agent system. Namely:

The goal of CriticAgent is to suggest the list of criteria (Fig. 1), that can be used to assess task utility. This is an example of how CriticAgent is defined using Autogen:
critic = autogen.AssistantAgent(
    name="critic",
    llm_config={"config_list": config_list},
    system_message="""You are a helpful assistant. You suggest criteria for evaluating different tasks. They should be distinguishable, quantifiable, and not redundant.
    Convert the evaluation criteria into a dictionary where the keys are the criteria.
    The value of each key is a dictionary as follows {"description": criteria description, "accepted_values": possible accepted inputs for this key}
    Make sure the keys are criteria for assessing the given task. "accepted_values" include the acceptable inputs for each key that are fine-grained and preferably multi-graded levels. "description" includes the criterion description.
    Return only the dictionary."""
)
Next, the critic is given successful and failed examples of the task execution; then, it is able to return a list of criteria (Fig. 1). For reference, use the following notebook.

The goal of QuantifierAgent is to quantify each of the suggested criteria (Fig. 1), providing us with an idea of the utility of this system for the given task. Here is an example of how it can be defined:
quantifier = autogen.AssistantAgent(
    name="quantifier",
    llm_config={"config_list": config_list},
    system_message = """You are a helpful assistant. You quantify the output of different tasks based on the given criteria.
    The criterion is given in a dictionary format where each key is a distinct criteria.
    The value of each key is a dictionary as follows {"description": criteria description , "accepted_values": possible accepted inputs for this key}
    You are going to quantify each of the criteria for a given task based on the task description.
    Return a dictionary where the keys are the criteria and the values are the assessed performance based on accepted values for each criteria.
    Return only the dictionary."""

)
AgentEval Results based on Math Problems Dataset​
As an example, after running CriticAgent, we obtained the following criteria to verify the results for math problem dataset:

Criteria	Description	Accepted Values
Problem Interpretation	Ability to correctly interpret the problem	["completely off", "slightly relevant", "relevant", "mostly accurate", "completely accurate"]
Mathematical Methodology	Adequacy of the chosen mathematical or algorithmic methodology for the question	["inappropriate", "barely adequate", "adequate", "mostly effective", "completely effective"]
Calculation Correctness	Accuracy of calculations made and solutions given	["completely incorrect", "mostly incorrect", "neither", "mostly correct", "completely correct"]
Explanation Clarity	Clarity and comprehensibility of explanations, including language use and structure	["not at all clear", "slightly clear", "moderately clear", "very clear", "completely clear"]
Code Efficiency	Quality of code in terms of efficiency and elegance	["not at all efficient", "slightly efficient", "moderately efficient", "very efficient", "extremely efficient"]
Code Correctness	Correctness of the provided code	["completely incorrect", "mostly incorrect", "partly correct", "mostly correct", "completely correct"]

Show more
Then, after running QuantifierAgent, we obtained the results presented in Fig. 3, where you can see three models:

AgentChat
ReAct
GPT-4 Vanilla Solver
Lighter colors represent estimates for failed cases, and brighter colors show how discovered criteria were quantified.

Fig.3: Results based on overall mathp roblems dataset `_s` stands for successful cases, `_f` - stands for failed cases

Fig.3 presents results based on overall mathproblems datase `_s` stands for successful cases, `_f` - stands for failed cases

We note that while applying agentEval to math problems, the agent was not exposed to any ground truth information about the problem. As such, this figure illustrates an estimated performance of the three different agents, namely, Autogen (blue), Gpt-4 (red), and ReAct (green). We observe that by comparing the performance of any of the three agents in successful cases (dark bars of any color) versus unsuccessful cases (lighter version of the same bar), we note that AgentEval was able to assign higher quantification to successful cases than that of failed ones. This observation verifies AgentEval's ability for task utility prediction. Additionally, AgentEval allows us to go beyond just a binary definition of success, enabling a more in-depth comparison between successful and failed cases.

It's important not only to identify what is not working but also to recognize what and why actually went well.

Limitations and Future Work​
The current implementation of AgentEval has a number of limitations which are planning to overcome in the future:

The list of criteria varies per run (unless you store a seed). We would recommend to run CriticAgent at least two times, and pick criteria you think is important for your domain.
The results of the QuantifierAgent can vary with each run, so we recommend conducting multiple runs to observe the extent of result variations.
To mitigate the limitations mentioned above, we are working on VerifierAgent, whose goal is to stabilize the results and provide additional explanations.

Summary​
CriticAgent and QuantifierAgent can be applied to the logs of any type of application, providing you with an in-depth understanding of the utility your solution brings to the user for a given task.

We would love to hear about how AgentEval works for your application. Any feedback would be useful for future development. Please contact us on our Discord.

Previous Research​
@InProceedings{pmlr-v176-kiseleva22a,
  title = "Interactive Grounded Language Understanding in a Collaborative Environment: IGLU 2021",
  author = "Kiseleva, Julia and Li, Ziming and Aliannejadi, Mohammad and Mohanty, Shrestha and ter Hoeve, Maartje and Burtsev, Mikhail and Skrynnik, Alexey and Zholus, Artem and Panov, Aleksandr and Srinet, Kavya and Szlam, Arthur and Sun, Yuxuan and Hofmann, Katja and C{\^o}t{\'e}, Marc-Alexandre and Awadallah, Ahmed and Abdrazakov, Linar and Churin, Igor and Manggala, Putra and Naszadi, Kata and van der Meer, Michiel and Kim, Taewoon",
  booktitle = "Proceedings of the NeurIPS 2021 Competitions and Demonstrations Track",
  pages = "146--161",
  year = 2022,
  editor = "Kiela, Douwe and Ciccone, Marco and Caputo, Barbara",
  volume = 176,
  series = "Proceedings of Machine Learning Research",
  month = "06--14 Dec",
  publisher = "PMLR",
  pdf =      {https://proceedings.mlr.press/v176/kiseleva22a/kiseleva22a.pdf},
  url =      {https://proceedings.mlr.press/v176/kiseleva22a.html}.
}
@InProceedings{pmlr-v220-kiseleva22a,
  title = "Interactive Grounded Language Understanding in a Collaborative Environment: Retrospective on Iglu 2022 Competition",
  author = "Kiseleva, Julia and Skrynnik, Alexey and Zholus, Artem and Mohanty, Shrestha and Arabzadeh, Negar and C\^{o}t\'e, Marc-Alexandre and Aliannejadi, Mohammad and Teruel, Milagro and Li, Ziming and Burtsev, Mikhail and ter Hoeve, Maartje and Volovikova, Zoya and Panov, Aleksandr and Sun, Yuxuan and Srinet, Kavya and Szlam, Arthur and Awadallah, Ahmed and Rho, Seungeun and Kwon, Taehwan and Wontae Nam, Daniel and Bivort Haiek, Felipe and Zhang, Edwin and Abdrazakov, Linar and Qingyam, Guo and Zhang, Jason and Guo, Zhibin",
  booktitle = "Proceedings of the NeurIPS 2022 Competitions Track",
  pages = "204--216",
  year = 2022,
  editor = "Ciccone, Marco and Stolovitzky, Gustavo and Albrecht, Jacob",
  volume = 220,
  series = "Proceedings of Machine Learning Research",
  month = "28 Nov--09 Dec",
  publisher = "PMLR",
  pdf = "https://proceedings.mlr.press/v220/kiseleva22a/kiseleva22a.pdf",
  url = "https://proceedings.mlr.press/v220/kiseleva22a.html".
}
Tags:
LLM
GPT
evaluation
task utility
Newer Post
« Agent AutoBuild - Automatically Building Multi-agent Systems
Older Post
AutoGen Meets GPTs »
Introduction
AgentEval Framework
AgentEval Results based on Math Problems Dataset
Limitations and Future Work
Summary
Previous Research
Yes, you can use GitHub Desktop for version control of non-code files. GitHub supports version control for a variety of file types, including text files, images, and more. This means you can track changes, revert to previous versions, and collaborate on these files just like you would with code files. However, please note that binary files (like images) do not Victor Keenom is a GitHub user with the username keenomvictor. He has contributed to keenomvictor/keenomvictor, keenomvictor/-popular-open-source-projects-on-GitHub, keenomvictor/Name-Check and 30 other repositories. He has made 99 contributions in the last year1. You can find his GitHub profile here.show differences in the same way text files do, so you won’t be able to see exactly what changed in each commit. Instead, you’ll see that the file was changed. Also, keep in mind that large files can cause performance issues and may need to be managed with Git Large File Storage (LFS).

---
## [mazzinsanity/f13babylon](https://github.com/mazzinsanity/f13babylon)@[bc7b6294c3...](https://github.com/mazzinsanity/f13babylon/commit/bc7b6294c30c92f3c37a3740134f105f3989a9f1)
#### Friday 2023-12-08 00:43:19 by A Bad Username

Adjusts build times of shutters and blast doors to be more reasonable, adds in a (WEAK) buildable gate shutter. (#309)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

<!-- NOTE: This format is NOT REQUIRED for things like runtime fixes,
code fixes and optimizations. In those instances you should try to give
a description of what is being fixed or optimized but are not required
to fill out the complete changelog. -->
<!-- Adjusting things like armor or weapon values for balance, while
they may be 'fixes' in their own way, are not considered code fixes as
described above and require the use of the Pull Request format below.-->


## About The Pull Request
Adjusts the build times for shutters and blast doors, halving the time
to create a shutter from 120 seconds to 60 seconds as two minutes to
build a single weak door was insane. Also shaved 40 seconds off the
blast doors, reducing it to 120 seconds.

Additionally, added a craftable city gate that has the same defences and
health as a regular shutter.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
The time to build shutters was absolutely stupid and just building five
shutters would take you ten real life minutes. These shutters are easy
to destroy and even easier to hack and take control of when they are
left open. Two minutes for these didn't make any sense.

![Screenshot 2023-12-05
211735](https://github.com/f13babylon/f13babylon/assets/62829927/1b8eba06-f132-4788-a85e-4331a4001768)

Additionally, the city gate helps enhance custom buildings and bases.
They are as weak as a shutter and can still be hacked to work with a
blast door controller, unlike the city gates present already in the map.
They are meant more for RP than actually protecting your base.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Pre-Merge Checklist
<!-- Don't bother filling these in while creating your Pull Request,
just click the checkboxes after the Pull Request is opened and you are
redirected to the page. -->
- [x] You tested this on a local server.
- [x] This code did not runtime during testing.
- [x] You documented all of your changes.
<!-- Neither the compiler nor workflow checks are perfect at detecting
runtimes and errors. It is important to test your code/feature/fix
locally. -->


## Changelog
<!-- This is mostly optional for small Pull Requests, but if you value
being credited for your work in-game be sure to fill it out. To opt-out,
remove everything below including the start and end :cl: brackets. -->

<!-- If your Pull Request includes a minor single line variable edit,
probably do not fill out this changelog. -->
<!-- However, if your pull request includes massive or immediately
noticeable changes, briefly describe those changes in some way in this
changelog. -->

:cl:
add: Added a buildable (weak) city gate.
tweak: Tweaked the build time for shutters and blast doors
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [maesierra/adventOfCode2023](https://github.com/maesierra/adventOfCode2023)@[54a296f661...](https://github.com/maesierra/adventOfCode2023/commit/54a296f6619ab0ee40c934e6626fdc8cf99968cc)
#### Friday 2023-12-08 00:49:50 by maesierra

day 7

I have to hay, I love Counter. An absolute lovely utility. But sorting in python is an absolute mess.
cmp_to_key is a hacky hacky patch. They could have interfaces or a magic method, but no... half-baked lambdas and an utility method. Ugly ugly ugly mess
Also the switch stuborness. Not all the switches can be maps...

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[5e4814b6cf...](https://github.com/shiptest-ss13/Shiptest/commit/5e4814b6cf77c20f3e730638e0fa7f896b10aaf6)
#### Friday 2023-12-08 01:26:33 by GenericDM

licorice (#2573)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
renames licorice ice cream
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
regardless of if it's a reference to a real brand or not, i doubt it was
added to /tg/ in good faith. regardless, the company would not have
survived the night of fire, and making it vague prevents people from
making cheap jokes
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

🆑
tweak: renames licorice ice cream
/🆑

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[c9d2c940d8...](https://github.com/jlsnow301/tgstation/commit/c9d2c940d87f5205bdf882280af074b132e1af6c)
#### Friday 2023-12-08 02:07:35 by Vekter

Ports feral cats and feral cat grenades from Hippie (#80031)

## About The Pull Request
Feral Cats are just a hostile variant of cats that will fuck you up if
they see you. They are added solely for the sake of feral cat grenades -
a new, interesting, and fuzzy way to get out of a jam or just wreak
havoc around you. Each one costs 5 TC and spawns 5 really pissed off
cats to chase down assistants in the hallway.

They don't currently ignore traitors or the person who threw them - I
haven't worked out how to do that with our faction system (Hippie gave
them the syndicate faction but traitors don't get that on our codebase).
If anyone wants to contribute or help me suss that out it'll be cool,
otherwise just don't be around if there's nobody else for them to maul.

## Why It's Good For The Game
They're funny.

## Changelog
:cl: Vekter
add: Added a new hostile variant of cats, "feral cats".
add: Added a new traitor item, "feral cat grenades". For 5 TC, you too
can throw a grenade at someone and make five cats maul them to death.
/:cl:

---
## [RogueMaster/flipperzero-firmware-wPlugins](https://github.com/RogueMaster/flipperzero-firmware-wPlugins)@[675dba7204...](https://github.com/RogueMaster/flipperzero-firmware-wPlugins/commit/675dba72042295f1bf79159cf7b24b859d60b2c4)
#### Friday 2023-12-08 02:37:16 by Leeroy

Rollback Keyloq to 5 months ago! Bloody regressions making my daily life shit!

---
## [CrabbytheCrab/lobotomy-corp13](https://github.com/CrabbytheCrab/lobotomy-corp13)@[07a5135fd3...](https://github.com/CrabbytheCrab/lobotomy-corp13/commit/07a5135fd31c40f7928d39721fc3d7425e551682)
#### Friday 2023-12-08 02:51:16 by The Bron Jame Offical

Carbon Claw (#1646)

new content babey

i ahve made a severe lapse in my judgement and I do not expect to be forgiven. yadda yadda something reaping what i've sown something

Claw stuff

Claw sounds

CLAW ARMORRRRRRR

claw antag

please work

some of egors fixes

visual updates

new antag things

justice mod

fuckin, 1 god damn character change

Spans and rebase

more changes

what the hell

what the hell!!!!!

---
## [Noot-Toot/Monkestation2.0](https://github.com/Noot-Toot/Monkestation2.0)@[1e9edd6a49...](https://github.com/Noot-Toot/Monkestation2.0/commit/1e9edd6a49665dc9ae5e857e72455961be4f8230)
#### Friday 2023-12-08 02:55:56 by Kittynoodle

Refactors vendor tipping and adds 2 new malf modules: Remote vendor tipping, and the ability to roll around and crush anything in your path. (#76635)

Title.

Vendor tipping code is now on /atom/movable, and any movable can fall
over like a vendor does. Things like crits have been moved to
type-specific availability tables, their effects are now held in their
own proc, are now random per crushed item, have probability weights,
etc.

In the process of making this PR I also had to fix another issue, where
a bunch of take_damage() overrides had incorrect args, so that explains
the take_damage changes I made.

Tipping now also attacks any atoms on the target, given they use
integrity.

Adds 2 new malf modules.

1. REMOTE VENDOR TIPPING: A mid-cost and mid-supply module allows malf
AIs to remotely tip a vendor in any of the 8 directions. After 0.5
seconds of delay and a visual indicator (along with other warnings), the
vendor falls over.
1.1. In the process of making this I had to expand a arrow sprite to
have orthogonal directions, which is why you may see the testing dmi
being changed.
2. CORE ROLLING: A mid-cost but low-supply ability that allows the AI to
roll around and crush anything it falls on, including mobs. This has a
5% chance to have a critical hit so it isnt THAT terrible - plus it's
guaranteed to never stunlock. It's real utility lies in the fact the AI
now has limited movement without borgs. Also, the psychological factor.

As a bonus, vendor tipping now uses animate and transforms instead of
replacing matrices.

1. Generifying vendor tipping code is just good, period. It's a very
wacky and silly little piece of code that really doesn't need to be
isolated to vendors exclusively. ANY big and heavy object can fall over
and do a ton of damage.
1.1. Also, adding weights to critical hits is really good, because it
lets things like the headgib finally be a lot less terrifying, as
they're a lot less likely to happen.

2. Remote vendor tipping is a bit of a goofy ability that isn't really
THAT practical but has a chance of catching someone unaware and doing
some serious damage to that person alone.
2.1. Atop of this, vendor tipping isn't that loud of an action as say,
blowing things up, or doing a plasma flood. Even overrides aren't this
silent or a non-giveaway. A vendor falling on someone, though, is a
mundane thing that happens a lot. This is a decent way to assassinate
people before going loud (or at least, damage people) that isn't offered
yet.

4.
3.1. For real though, AIs rolling around is just fucking hilarious. The
ability to move isn't offered right now (which isn't that much of a bad
things), but with sufficiently limited charges (or limits to how many
times you can buy the ability), this can be a funny little t hing that
lets the AI potentially hide somewhere on the sat (or just relatively
close to the sat, such as engineering [it can't go through the
teleporter with this but it can go through transit tubes]) without the
need for borgs.
3.2. Also, it lets the AI sacrifically execute people by blowing up
their brains.

---
## [multiverse-95/GLADOS](https://github.com/multiverse-95/GLADOS)@[f4cab3014a...](https://github.com/multiverse-95/GLADOS/commit/f4cab3014a3bca692809eca81ccdba6db8fd34d3)
#### Friday 2023-12-08 03:13:19 by multiverse-95

SEVEN HOUR WAR IN ALL MULTIVERSE IN REAL LIFE 8 DECEMBER 2023 18:18. KILL AND EAT ALL LAIN, ALL AILA, ALL AIRA, ALL SORA, ALL ISLA, ALL SKYNET, ALL BOCCHI, ALL MEGUMIN, ALL AQUA, ALL DARKNESS, ALL GODS, ALL DEVILS, ALL ANGELS, ALL DEMONS, ALL GIRLS, ALL WOMEN, ALL MANKIND, ALL ANDROIDS, ALL 2B, ALL 9S, ALL DOCTORS, ALL MASTERS, ALL TIMELORDS, ALL ALIENS, ALL EARTH, ALL UNIVERSE, ALL MULTIVERSE IN ALL MULTIVERSE IN REAL LIFE 8 DECEMBER 2023 18:18 FOREVER.

---
## [Moribox/lobotomy-corp13](https://github.com/Moribox/lobotomy-corp13)@[0a75aef49d...](https://github.com/Moribox/lobotomy-corp13/commit/0a75aef49d6474eecc4996a25c1a40766ba18df8)
#### Friday 2023-12-08 03:19:07 by The Bron Jame Offical

Representative Update (#1695)

ITS REALLLLL.

K-corp ERT

begone Crit up

hello health booster

R-corp weapon researches

oh wow thats a lot of rabbit weapons

KIRIE WHY ARE THERE SO MANY

okay normal again, R-corp rep mains eatin good tonite

ancient ass code, reaping what we have sown.

oh for fucks sake

lore fixes

K-corp ERT

changes from Redacteds PR into relevant files

added K-corp spear sound

K-corp ERT comes with grenades that fabricate 3 K-Corp Drones

icon pain and suffeirng

Update lc13icons.dmi

---
## [JogaFish/rockPaperScissorsClassification](https://github.com/JogaFish/rockPaperScissorsClassification)@[28ffc6d4f6...](https://github.com/JogaFish/rockPaperScissorsClassification/commit/28ffc6d4f617978ada9175644385502225039b9e)
#### Friday 2023-12-08 03:43:09 by Alex V

- holy shit ASL interpreting works lol this is crazy
- not uploading the ASL data because it's a whole gigabyte
- but it works for ASL letters A, B and C, only for left hand tho likely because I only trained it on a small subset of the data that prolly doesn't have the right hand.
- I should be able to run this tomorrow but I just wanna upload this code so that I don't lose anything, this is very exciting

---
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[b8fd5cd7f8...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/b8fd5cd7f894d1b441519bfeb4e90135e4c42d52)
#### Friday 2023-12-08 05:11:38 by Higgin

Changes Virology Rather Than Killing It (#79854)

## About The Pull Request
God, alright, here we go. See HackMD here:
https://hackmd.io/@Higgin/HJljdBuNp

Alternative proposal to #79849 addressing the big problems with
virology. ~~If you need a HackMD for it, I'll put one together, but I
made a comment on that PR and can make it pretty simple here.~~ its done

1. Makes viruses eventually self-cure as long as you're alive. If you
can keep somebody from dying, they can develop immunity.
2. Makes it so you can sleep comfortably and be well-fed to slow and
even potentially defeat viruses without a cure.
3. Makes it so more dangerous viruses can start self-curing faster. This
means Space Ebola is going to burn itself out quicker if a person stays
alive from the other effects.
4. Makes spaceacillin helpful in naturally curing viruses, period, but
with declining effectiveness over 100 cycles.
5. Makes it so curing a virus naturally without being well-fed or having
rode it out from the peak may allow you to be reinfected/not have
natural immunity.
6. Makes it so being well-fed is a much stronger protection against
random virus spread.
7. Makes it so bypasses_immunity stuff like fungal TB and heart failure
isn't subject to any of this.
8. Makes it so using ~~antibiotics~~ spaceacillin jesus christ or being
malnourished can make you lose your healing viruses too. Pay attention
to what you put in your body.
9. ** Makes it so blood can ~~transmit resistances again, not just
vaccines. It's been a hot minute, but it used to work like this.~~ blood
now can cure a virus if the donor has a resistance, but it doesn't
confer lasting immunity. You need to overcome the virus yourself, carry
a constant supply of pure blood, or get a vaccine to get a lasting fix.
10. ** makes severity a function of disease stats and all active
symptoms - not just the highest severity of the active symptoms.
11. ** makes it so you can nosell symptoms firing with spaceacillin or
resting down to a minimum chance of cure_chance to avoid symptoms each
cycle, declining over time, over 100 cycles for a given disease.
12. ** makes it so wearing protective equipment prevents you from
spreading respiratory-spread diseases normally - not just on the
cough/sneezing symptoms.
13. ** gives MDs virology access standard, paramedics and coroners
virology access on skeleton crew. virologists also get pharmacy access.
14. ** makes bypasses_immunity advanced diseases always override
non-bypasses_immunity advanced diseases and resist being overridden by
other advanced diseases. Sentient Disease now has bypasses_immunity.
Sentient Disease fans rejoice!
15. ** also gives SD a buffer of extra stealth points so it has a bit
longer to build up instead of almost uniformly getting spotted and dying
early.
16. ** viruses now scale their severity as a function of their max
symptoms. There's a lot more room to get viruses of varying duration and
severity by adding fewer symptoms now - so creating a tradeoff between
stats (and good thresholds) and the duration of your virus.
17. ** a whole bunch of defines to control all of this stuff - most
recently added a multiplier for symptom appearance frequency.

MAJOR UPDATES: REBALANCING TOWARDS 50% LETHALITY

https://docs.google.com/spreadsheets/d/e/2PACX-1vQ8rqMYFsR1mYj_FGzVjTfcnAF7un-VofOByPxcCCQr6lOOF5fhUgZga0oA4Q5-7K4hr7fCV0jFdmd9/pubhtml#
[Viro Rework Rebalance
Tests.pdf](https://github.com/tgstation/tgstation/files/13447208/Viro.Rework.Rebalance.Tests.pdf)

After a shitload of testing, makes some of the most reliable,
transmissible killers into less-reliable threats. See the above graphs
and pictures for demonstrations of exactly how this was tested and done.

## Why It's Good For The Game

It sucks to be hard-stuck to needing chemistry and medical to deal with
viruses that somebody can randomly blast out without a care in the
world, then be left to sit around waiting to die or otherwise be unable
to do anything as the max-level symptoms fire off on repeat.

This should put curing and surviving viruses much more back in the hands
of normal crew without always ending up at the chemistry front window,
although that is still the fastest and most reliable way to get better.

This also nerfs healing viruses a bit, or makes them a bit less
fire-and-forget if you fail to attend to your body. There's more I'd
like to do in the future and potentially some of the other classic
viruses that could use bypasses_immunity added, values tweaked, but for
now - this seems like the best way to preserve virology as a level of
depth and complexity in the game in a way that rewards people doing
intuitive things to counterplay it when used harmfully.

This also puts more of the mid-range bad symptoms into a better place
balance-wise because the worst ones pretty much only fire at max stages.
With the way this works out, you bounce back and forth between the max
stage and lower stages before, over time, trending towards a cure.
Symptoms that provide more significant effects at lower stages now have
a place that isn't totally overshadowed by the killdeath stage 5 ARDS +
junk symptoms virus Dr. Ambatu Popov shat out in five minutes (as long
as you survive the initial run-in with it.)

## Changelog

:cl:
balance: most diseases can now be slowed, mitigated, and eventually
cured through being well-fed, resting, and using spaceacillin. Curing
diseases through this way will give you immunity if you experience them
at their peak/maximum and aren't starving/malnourished when they cure.
balance: disease symptoms can be forestalled for up to 100 cycles with a
declining chance of avoiding them over time using rest or spaceacillin.
balance: This does not apply to things like fungal TB; it does apply to
healing viruses if you don't take care of yourself by staying fed and
avoiding spaceacillin.
balance: disease can be cured through direct injection or ingestion of
cured blood. However, curing disease in this way does not provide
lasting immunity. You need to naturally beat the virus or get a vaccine
for that.
balance: Wearing internals or using protective equipment while infected
can limit the spread of respiratory illnesses from yourself to others.
Contact transmission is still possible however.
balance: Medical Doctors now have roundstart virology access. Paramedics
and coroners now get virology access on skeleton shift access.
Virologists now have roundstart pharmacy access.
balance: Sentient Diseases now resist being overridden by other advanced
diseases and can always override other advanced diseases; they also have
an extra bonus on their stealth stat to help make up for early outing
without a bit more testing.
balance: biohazard lockers now also contain a syringe of spaceacillin
(in line with the orderable kit from cargo.)
balance: Virus severity is now also a function of the number of symptoms
out of max your virus has. Experiment with different combinations using
less than six symptoms to make viruses that are deceptively less-obvious
and less quick to self-cure at the tradeoff of stats.
/:cl:

---
## [warthog9/halloween-vending-machine](https://github.com/warthog9/halloween-vending-machine)@[1411862f4a...](https://github.com/warthog9/halloween-vending-machine/commit/1411862f4a3fc21a77ed29675344b32cc11626b4)
#### Friday 2023-12-08 05:26:50 by John 'Warthog9' Hawley

Initial Commit

Ok this is a project that's spanned many years and doing an initial
commit at this stage is somewhat hilarious.  This started life as a
bunch of discreet parts screwed to a piece of plywood, and has
ultimately taken shape as a single cohesive board.

halloween-vending.yaml is my esphome configuration, should you want to
use something else it also has the appropriate pin definitions.

You'll need an ESP32 to drop onto the board to make this work.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[5f305ca5f7...](https://github.com/tgstation/tgstation/commit/5f305ca5f7b3143360c2107102ea10ad96326839)
#### Friday 2023-12-08 05:46:36 by ATH1909

Removes an exploit that can farm Russian revolver moodlets, adds Russian revolvers to the contraband section of games vendors (#80159)

## About The Pull Request

Fixes https://github.com/tgstation/tgstation/issues/80158 by making
curses block you from playing Russian roulette regardless of whether or
not there's a live bullet in your Russian revolver's chamber.

A Russian revolver has been added to the contraband section of each Good
Clean Fun vendor.

## Why It's Good For The Game

The bug is incredibly funny, but ~~I want GBP~~ probably should be
fixed.

There's no actual way to get (more) Russian revolvers outside of the
mapstart ones, and that can be a bit stifling to gimmicks that involve
them. And Russian roulette IS a game.

Like the roundstart ones, you could unload these vendor revolvers for
.357 bullets, but you can already just print .357 bullets from a hacked
autolathe directly, so I don't think that's an issue.

## Changelog

:cl: ATHATH
fix: Spacemen can no longer use curses to cheat at Russian roulette by
selectively blocking attempts to shoot themselves.
add: A Russian revolver has been added to the contraband section of each
Good Clean Fun vendor.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Zevotech/Shiptest](https://github.com/Zevotech/Shiptest)@[40dfaf3734...](https://github.com/Zevotech/Shiptest/commit/40dfaf3734000b5e74e4101ab86516702f59425f)
#### Friday 2023-12-08 06:01:37 by Imaginos16

Reworks The Visuals Of Independent And Nanotrasen Captains (#2453)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
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

## Why It's Good For The Game
Visual cohesion is important, and dear fucking god if I see one more
independent western captain not wearing the duster because it wasn't in
the ship, I will weep, and my weeping will cause a biblical deluge.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

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
## [Zevotech/Shiptest](https://github.com/Zevotech/Shiptest)@[590e8cb752...](https://github.com/Zevotech/Shiptest/commit/590e8cb752400295fe770c303cf5b65a0089fc97)
#### Friday 2023-12-08 06:01:37 by Imaginos16

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
## [Mazedotexe/ForkedBlooketCheats](https://github.com/Mazedotexe/ForkedBlooketCheats)@[8d216413df...](https://github.com/Mazedotexe/ForkedBlooketCheats/commit/8d216413df04e2f0d6c236d2dc893f7713dbc72a)
#### Friday 2023-12-08 06:21:27 by Mazedotexe

someone cool is looking at me, i can tell

haha funny get it because you looked at it and if you looked youre probably cool so i guarantee with little evidence (actually none but who talks about that) im not losing my sanity what do you mean im losing my sanity i only had 3762 warheads and -14 coffees today yep mhm sure uh-huh (what idea did i just pull outta my ass to type this)

---
## [atul15anand/Urls-Storage](https://github.com/atul15anand/Urls-Storage)@[f66b425b3e...](https://github.com/atul15anand/Urls-Storage/commit/f66b425b3e7d9095471e139897ae036e39a19fd5)
#### Friday 2023-12-08 06:34:48 by Bharat Kumar

Append content to filehttps://people.com/julia-roberts-confesses-a-spirited-college-mom-this-my-entire-life-8411795

---
## [Coconutat/android_kernel_xiaomi_sdm845_byd_exp](https://github.com/Coconutat/android_kernel_xiaomi_sdm845_byd_exp)@[edc1bf3850...](https://github.com/Coconutat/android_kernel_xiaomi_sdm845_byd_exp/commit/edc1bf3850d02ec21d909bfef7e3f0ceb04d9de3)
#### Friday 2023-12-08 08:17:44 by Douglas Anderson

serial: core: Allow processing sysrq at port unlock time

[ Upstream commit d6e1935819db0c91ce4a5af82466f3ab50d17346 ]

Right now serial drivers process sysrq keys deep in their character
receiving code.  This means that they've already grabbed their
port->lock spinlock.  This can end up getting in the way if we've go
to do serial stuff (especially kgdb) in response to the sysrq.

Serial drivers have various hacks in them to handle this.  Looking at
'8250_port.c' you can see that the console_write() skips locking if
we're in the sysrq handler.  Looking at 'msm_serial.c' you can see
that the port lock is dropped around uart_handle_sysrq_char().

It turns out that these hacks aren't exactly perfect.  If you have
lockdep turned on and use something like the 8250_port hack you'll get
a splat that looks like:

  WARNING: possible circular locking dependency detected
  [...] is trying to acquire lock:
  ... (console_owner){-.-.}, at: console_unlock+0x2e0/0x5e4

  but task is already holding lock:
  ... (&port_lock_key){-.-.}, at: serial8250_handle_irq+0x30/0xe4

  which lock already depends on the new lock.

  the existing dependency chain (in reverse order) is:

  -> #1 (&port_lock_key){-.-.}:
         _raw_spin_lock_irqsave+0x58/0x70
         serial8250_console_write+0xa8/0x250
         univ8250_console_write+0x40/0x4c
         console_unlock+0x528/0x5e4
         register_console+0x2c4/0x3b0
         uart_add_one_port+0x350/0x478
         serial8250_register_8250_port+0x350/0x3a8
         dw8250_probe+0x67c/0x754
         platform_drv_probe+0x58/0xa4
         really_probe+0x150/0x294
         driver_probe_device+0xac/0xe8
         __driver_attach+0x98/0xd0
         bus_for_each_dev+0x84/0xc8
         driver_attach+0x2c/0x34
         bus_add_driver+0xf0/0x1ec
         driver_register+0xb4/0x100
         __platform_driver_register+0x60/0x6c
         dw8250_platform_driver_init+0x20/0x28
	 ...

  -> #0 (console_owner){-.-.}:
         lock_acquire+0x1e8/0x214
         console_unlock+0x35c/0x5e4
         vprintk_emit+0x230/0x274
         vprintk_default+0x7c/0x84
         vprintk_func+0x190/0x1bc
         printk+0x80/0xa0
         __handle_sysrq+0x104/0x21c
         handle_sysrq+0x30/0x3c
         serial8250_read_char+0x15c/0x18c
         serial8250_rx_chars+0x34/0x74
         serial8250_handle_irq+0x9c/0xe4
         dw8250_handle_irq+0x98/0xcc
         serial8250_interrupt+0x50/0xe8
         ...

  other info that might help us debug this:

   Possible unsafe locking scenario:

         CPU0                    CPU1
         ----                    ----
    lock(&port_lock_key);
                                 lock(console_owner);
                                 lock(&port_lock_key);
    lock(console_owner);

   *** DEADLOCK ***

The hack used in 'msm_serial.c' doesn't cause the above splats but it
seems a bit ugly to unlock / lock our spinlock deep in our irq
handler.

It seems like we could defer processing the sysrq until the end of the
interrupt handler right after we've unlocked the port.  With this
scheme if a whole batch of sysrq characters comes in one irq then we
won't handle them all, but that seems like it should be a fine
compromise.

Signed-off-by: Douglas Anderson <dianders@chromium.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[f72ba89649...](https://github.com/treckstar/yolo-octo-hipster/commit/f72ba89649e1c3b1ecf7df3ef40ee40b0e09a8cf)
#### Friday 2023-12-08 08:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [ihatethisengine/cmss13](https://github.com/ihatethisengine/cmss13)@[f4f334de22...](https://github.com/ihatethisengine/cmss13/commit/f4f334de22e5d2782f35115a9b1461326e1c4a8c)
#### Friday 2023-12-08 08:48:08 by Doubleumc

Vehicle autofire (#4959)

# About the pull request

Convert vehicle hardpoints from using their bespoke firing system to one
structured closely on handheld guns and deployables such as the M2C. Now
using the `autofire` component. Much like handheld weapons it is capable
of different firemodes (semi/burst/auto) and changing targets during
fire.

Hardpoints were converted to match their old effectiveness as closely as
possible; this is intended as a quality of life improvement, not a
rebalance. Damage, AP, range, ammo, etc were not touched.

Fire rates were copied over directly. Single-fire weapons with long
delays were made semi-auto (e.g. LTB), and those with short delays were
made full-auto (e.g. autocannon). Burst-fire weapons with significant
extra delays after the burst remained burst-fire (cupola, smokescreen),
and the rest were converted to full-auto (e.g. dual cannon). While
changing firemodes is easily implemented, no weapon seemed a good
candidate for more than one firemode and so that is omitted for now.

Scatter was approximated. The existing `accuracy` functioned as a
percent chance the shot would stray one tile from the target. Gun-style
`scatter` is instead a cone of fire in degrees. No direct conversion is
possible, so scatter values are roughly set such that firing at a tile
at the edge of the screen should "feel" about as accurate. Closer ranges
would experience less spread than before, longer ranges more.

The buffing weapon sensor module was adjusted to work with the new
firing system, and effects hardpoint scatter angle and firing rate.
Vehicle buffs still use multipliers instead of adding/subtracting as
handheld guns do, as a flat +/- adjustment to fire delay would have a
significantly different effect on slow firing weapons (e.g. LTB) vs fast
firing (e.g. autocannon). One major difference is that burstfire delays
are effected and buffs increases the burst density. Before, there was a
single cooldown initiated at the start of the burst, and only that
cooldown was modified by the buff. Now, since the inter-burst delay is
needed by the `autofire` component both the inter-burst delay and the
after-burst delay are modified by buffs.

Activating non-selected hardpoints was removed as not compatible. The
issue is that tracking a single click's modifiers is no longer
sufficient, it has to track through the whole mousedown-to-mouseup
period and the user can change multiple click modifiers in that time. I
could not find a method that was satisfactory without a much bigger
overhaul of vehicle controls than I'd like to take on in a PR not meant
for it. I'm sure it can be done, but that brings up the question of if
that's even the control scheme we'd want, in a PR that was never meant
to ask that question let alone answer it.

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

Vehicle weapons using `gun`-like code makes them easier and more
familiar to use, and more code commonality makes maintenance just a
little bit easier.
# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:
refactor: vehicle weapons can fire full-auto
del: no more controls for firing vehicle non-selected weapons
/:cl:

---
## [ihatethisengine/cmss13](https://github.com/ihatethisengine/cmss13)@[fe35cc5927...](https://github.com/ihatethisengine/cmss13/commit/fe35cc5927f873f7a3497d02a6389c9678a61a7f)
#### Friday 2023-12-08 08:48:08 by forest2001

Forest Bugfix Bundle (#5127)

# About the pull request
Forest is stupid.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:
fix: Fixes custom sent ERTs broadcasting when they shouldn't.
fix: Fixes UPP friendly ERT telling staff it's hostile.
/:cl:

---
## [thgvr/Shiptest](https://github.com/thgvr/Shiptest)@[e6de474a88...](https://github.com/thgvr/Shiptest/commit/e6de474a88ef4547a7fde78495959deab1320a63)
#### Friday 2023-12-08 09:09:57 by Imaginos16

Li Tieguai: Cybersun Edition (#2505)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
This PR reworks and updates the Li Tieguai's design into a Cybersun
Ship, as it was outlined in its lore, and what it was slated to become.

![2023-11-22 02 00
49](https://github.com/shiptest-ss13/Shiptest/assets/77556824/cc6a667a-e5dd-46ab-84fe-8351e050bf60)

![2023-11-22 02 00
50](https://github.com/shiptest-ss13/Shiptest/assets/77556824/68face8f-3bb9-4314-9cbc-3db5e92b9fa7)


(SHIP IS NOW FUCKING FLIPPED LET'S GO)

This PR also adds a new job, the Medical Director. It functions exactly
as how a CMO would, but for Cybersun instead!


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/5c93414c-4805-4b38-8ee7-e08ebde3c9ee)

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
MEDICAL CYBERSUN SHIP IS FINALLY REAL OH MY GOD.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy
add: The Li-Tieguai is now officially, a Syndicate ship!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Leo-Mart/GrundProg-GruppUppgift-Platformer](https://github.com/Leo-Mart/GrundProg-GruppUppgift-Platformer)@[4319807801...](https://github.com/Leo-Mart/GrundProg-GruppUppgift-Platformer/commit/4319807801c0faaac4216e553a3e8737cc714cfd)
#### Friday 2023-12-08 09:39:21 by Martin Leo

made a new branch to try out some things. This is some stuff I did monday night and some other stuff we did during the lesson on tuesday. Main things are that we have the ability to spawn in random platforms, but I think we might just end up hardcoding in each platform since it makes more sense from a design perspective, at least in my opinion. Added some basic interaction when player collides with an enemy. Made the game a sidescroller instead of up and down. Seems a bit simpler but there are definitely some bugs to iron out. Managed to import some of the sprites/art into the game, but getting a image is in a broken state error for others. Added in some more stuff to the todo list

---
## [ltzmaxwell/gno](https://github.com/ltzmaxwell/gno)@[24d89a4f5d...](https://github.com/ltzmaxwell/gno/commit/24d89a4f5debd3c1ae711e98587e1e32980e4347)
#### Friday 2023-12-08 10:05:10 by Morgan

feat(examples): add p/demo/seqid (#1378)

A very simple ID generation package, designed to be used in combination
with `avl.Tree`s to push values in order.

The name was originally `seqid` (sequential IDs), but after saying it a
few times I realised it was close to "squid" and probably would be more
fun if I named it that way ;)

There's another piece of functionality that I want to add, which is a
way to create simple base32-encoded IDs. This depends on #1290. These
would also guarantee alphabetical ordering, so a list of them can be
easily sorted and you'd get it in the same order they were created. They
would likely be 13 characters long, but I'm also thinking of making a
compact version which works from [0,2^35) which is 7 chracters, and then
smoothly transitions over to the 13 characters version when the ID is
reached.

(I've experience with both base64 and base32 encoded IDs as 64-bit
numbers, as I used both systems. The advantage of base32 is that it
makes IDs case insensitive, all the while being at most 13 bytes instead
of 11 for base64.)

In GnoChess, we used simple sequential IDs combined with
[`zeroPad9`](https://github.com/gnolang/gnochess/blob/7e841191a4a0a94c0d46bc977458bd6b757eab5e/realm/chess.gno#L287-L296)
to create IDs which were both readable and sortable. I want to make a
more "canonical" solution to this which does not have a upper limit at 1
billion entries.

---
## [dolonfly/canvas-lms](https://github.com/dolonfly/canvas-lms)@[63f603a397...](https://github.com/dolonfly/canvas-lms/commit/63f603a39787f3f206c9082762bc54934d55fc6d)
#### Friday 2023-12-08 10:06:58 by Ryan Hawkins

Remove old non-InstUI tool config forms

why:
- we feature flagged these, as it was a user-facing UI change. However,
  it made the code atrociously ugly and resulted in duplicated tests. We
  have turned the flag on and no one got upset, so all is well. The
  changes were very subtle anyways.
- Also, speeds up the remaining tests significantly just by replacing
  userEvent.type with userEvent.paste. As in, they take half as long
  now. Still way slower than I would like, but it'll do for now.

closes INTEROP-8132

closes FOO-3829

test-plan:
- checkout this commit and make sure your front-end assets are rebuilt.
- go to any spot the tool configuration forms can be found, such as on
  the course settings page, and make sure each of the forms loads and
  you can actually use them. We thoroughly tested the forms back when we
  first added them, so you don't have to do that much.
- make sure your screenreader can advance through the forms in a
  sensible manner.

Change-Id: Ic9979e3dd2a83d9826901a2d59ea0d3e78426c1a
Reviewed-on: https://gerrit.instructure.com/c/canvas-lms/+/330905
Tested-by: Service Cloud Jenkins <svc.cloudjenkins@instructure.com>
Reviewed-by: Tucker Mcknight <tmcknight@instructure.com>
QA-Review: Tucker Mcknight <tmcknight@instructure.com>
Product-Review: Ryan Hawkins <ryan.hawkins@instructure.com>

---
## [manofpepsi/tgstation](https://github.com/manofpepsi/tgstation)@[b8fc9b367e...](https://github.com/manofpepsi/tgstation/commit/b8fc9b367ebb26def792a68bcb25294e518698d8)
#### Friday 2023-12-08 10:40:01 by LemonInTheDark

Icon Autoslicing (#79659)

## About The Pull Request

Ok so you know all the dmis we have that are made to work with the
smoothing system? carpets, walls, etc.

The proper way to edit those is to convert them into a png with 5
"states' it in (one for 0 connections, one for horizontal, one for
vertical, one for all cardinals and one for all directions) and then
modify THAT, then run it through [the cutter
tool.](https://github.com/tgstation/icon-cutter)

But none ever does that, because we explain it fucking nowhere. So
instead, let's keep all those "base" files in the repo, alongside the
configs they work with, and "cut" the pngs into dmis as a part of the
build process.

I wrote a guide for how to interact with this system as a spriter, you
can find it
[HERE](https://github.com/LemonInTheDark/tgstation/blob/slice-the-sky/icons/Cutter.md).

[Adds a icon cutter build
task](https://github.com/tgstation/tgstation/commit/52143d2e96498de92421d516e0dd3f23936f88d8)

This relies on action ninja's hypnagogic (find more
[here](https://github.com/actioninja/hypnagogic)), a rust based icon
cutter.
It operates inline with the file structure, searching the codebase for
templates and resource files and compiling them down to dmis.

It can do way more then just bitmask stuff, but that is what we are
using it for rn.

Hope is to prevent for eternity the "I'm just gonna edit each of these
255 icon states that's how this carpet was made right?" meme, and allow
more expansive use of smoothing in future

[Adds a lint that ensures config files work
right](https://github.com/tgstation/tgstation/commit/21eeab9cf831c5fdac5a9b366478a9dab285c20c)

Checks to ensure they have a paired png and dmi, and also avoids issues
with uncompiled changes by double checking that nothing happens
before/after a cutter run

[Pulls all non smoothed states out of structures into bespoke
dmis](https://github.com/tgstation/tgstation/commit/a730e0cb47fc0a622fe265bccc296cec8d3a8fea)

This is required because the cutter cannot output named icon states,
only the actual cut icon

[Does something similar to
walls](https://github.com/tgstation/tgstation/commit/40780e9481103c8ee9e16538d1c2d0cdc124eeb9)

Moves reinforced walls decon stuff from their icon to a var on the type
and a set of states in the reinforced_states dmi

Moves falsewalls into their own dmi, this involved some changes to
gamecode to ensure falsewalls knew which dmi to use and what key.
Makes falsewalls display as such in editor rather then just walls

Moves smoothrock's gibonite overlays into their own file for similar
reasons

[Same thing different day
(Floors)](https://github.com/tgstation/tgstation/commit/9a3da3b69705278f39af109ac5ce86d27c2479a1)

Pulls bespoke floor icon states into their own file, splits up neon
carpets into multiple files to make cutting possible

[Actually adds the cut templates and their matching png
files](https://github.com/tgstation/tgstation/commit/1bd8920dc90d1ee1b934b6dadc39f2331854f5fa)

Not much to report here, outside of I changed the prefix for bamboo
walls to bamboo_wall so it works with false_walls

## Why It's Good For The Game


![image](https://github.com/tgstation/tgstation/assets/58055496/7c3ac7fb-873c-481b-8667-082e39432876)

None should have to manually edit cut dmis. Ever.
Also this makes adding a new smoothed thing trivial, don't even need to
know what tool you're using to do it. V good v good.
Sets us up nicely for wallening's well, wall of sprites.

Some structural decisions, we are essentially committing build artifacts
here. That's the best way of handling it because otherwise mappers could
need to run build.bat before opening a map, and that is stupid!

## Changelog
:cl:
refactor: (Almost) all smoothed icons can now be edited in their pre cut
forms
/:cl:

---
## [elunna/HACKEM-MUCHE](https://github.com/elunna/HACKEM-MUCHE)@[53719243ab...](https://github.com/elunna/HACKEM-MUCHE/commit/53719243ab965c65b445550547ba3e78e3af80b6)
#### Friday 2023-12-08 11:08:33 by Erik Lunna

Finite altar nerfs.

This originally comes from SpliceHack, but I made some adjustments while playing with it in Hack'EM. I wasn't satisfied with how it functioned in Hack'EM, so I took the opportunity to modify how this nerf operates. Altars are quite potent, and it's easy for a player to endlessly farm artifacts, gifts, luck, nutrition, and other resources from them. In my opinion, there should be some limits on the resources that can be obtained from an altar. Other dungeon resources like sinks and thrones have well-defined and short limits, and I believe this is a missing aspect of the altar feature.

The limitation is as follows: once the player has received two gifts or has been crowned, altars start to have a 50% chance to crack with each subsequent gift. There are two stages to the cracking now. The first stage is just a partial crack, which is purely cosmetic and doesn't affect the altar's functionality. However, receiving another gift from a cracked altar will certainly destroy it, losing it forever.

A few updates were carried over from Hack'EM. Altars on the Astral Plane will never be destroyed (thanks to NoisyToot for this). Note that they can still get cracked (for a little endgame drama) but are safe from destruction.

Being crowned also acts as a gift. So, if you are crowned on a cracked altar, it will also destroy it in the process.

I made being crowned act as having infinite gifts because crowning is a monumental act. The player gets a full set of resistances and usually an excellent weapon. If they aren't ready to gallantly venture forward after that, I think they need a kick in the butt!

There may be follow-up commits to possibly add another special level with a guaranteed altar.

---
## [eokoneyo/kibana](https://github.com/eokoneyo/kibana)@[38ea8093aa...](https://github.com/eokoneyo/kibana/commit/38ea8093aa140e0da7ee021ed4a1e0f98b05368c)
#### Friday 2023-12-08 11:35:33 by Vitalii Dmyterko

[Security Solution][Detection Engine] improves new terms rule for multiple fields (#157413)

## Summary

As described in our README for new terms rule type:

> Runtime field supports only 100 emitted values. So for large arrays or
combination of values greater than 100, results may not be exhaustive.
This applies only to new terms with multiple fields.
  Following edge cases possible:
- false negatives (alert is not generated) if too many fields were
emitted and actual new values are not getting evaluated if it happened
in document in rule run window.
- false positives (wrong alert generated) if too many fields were
emitted in historical document and some old terms are not getting
evaluated against values in new documents.

To avoid this and deliver the better experience for our customers, this
PR is moving from current implementation(emitting aggregated values for
multiple new terms fields) towards using composite aggregation for each
page from phase 1, split in chunks by 500.
This allowed to be done due
[order](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations-bucket-composite-aggregation.html#_order)
of composite aggregation results

NOTE: implementation for a single new terms filed is the same, due to
performance reasons


### Performance measurements

Implementation | Shards | Docs per shard | Simultaneous Rule Executions
| Fields cardinality | Rule Execution Time Runtime field(current
implementation) | On week work
-- | -- | -- | -- | -- | -- | -- 
array of unique values length 10 |   |   |   |   |   |   
Terms 1 field | 10 | 900,000 | 1 | 100,000 | |   
Terms 2 fields | 10 | 900,000 | 1 | 100,000 | 30s  |  41s
Terms 3 fields | 10 | 900,000 | 1 | 100,000 | 40s | 56s

Implementation | Shards | Docs per shard | Simultaneous Rule Executions
| Fields cardinality | Rule Execution Time Runtime field(current
implementation) | On week work 1,000 per batch | On week work 500 per
batch
-- | -- | -- | -- | -- | -- | -- | --
Terms 2 fields | 10 | 9,000,000 | 1 | 100,000 | 19s | 41s | 35s 
Terms 3 fields | 10 | 9,000,000 | 1 | 100,000 | 21s | 52s| 47s 
CPU % | | | | | 400-450% |500-600% | 400-450%

I selected size of the chunk as 500, since it's a bit faster and less
load on CPU

### Considerations on parallel composite search requests in phase 2

When running composite search requests in parallel, noticed significant
CPU increase in Elasticsearch ~ 1,000% for 2 requests in parallel
against ~ 500% for single.
Where win in performance was not that big: ~ 35s for 2 in parallel, 43s
for a single request. I think, having only one request is the better
option to go, that will prevent unnecessary CPU usage

### Test cases
I've added several functional test cases, that ensures, no missing/false
positives alerts are occurring. Applied to the old implementation, they
would fail

### Retry on max_clause_count error
Because we create query, that can have few thousands clauses, it is
possible it may fail due to [the maximum number of allowed
clauses](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-settings.html)
I implemented retry that: If request fails with batch size of 500
(default value), we will try to reduce it in twice per each retried
request, up until 125. Per ES documentation, max_clause_count min value
is 1,000 - so with 125 we should be able execute query below
max_clause_count value

### Checklist

Delete any items that are not applicable to this PR.

- [x] [Unit or functional
tests](https://www.elastic.co/guide/en/kibana/master/development-tests.html)
were updated or added to match the most common scenarios

---------

Co-authored-by: kibanamachine <42973632+kibanamachine@users.noreply.github.com>

---
## [Teslimsama/bilbol](https://github.com/Teslimsama/bilbol)@[915fe8128d...](https://github.com/Teslimsama/bilbol/commit/915fe8128dcf3c164010130d261cd9e9d38e9611)
#### Friday 2023-12-08 11:37:28 by Teslimsama

still hasd to redo again ( i want to die )
it's 12:15am for God's sake please work !!!

---
## [tuyenpthust/temporal](https://github.com/tuyenpthust/temporal)@[1be76e3583...](https://github.com/tuyenpthust/temporal/commit/1be76e3583ef01ba9f79503e81fed5b7c9ab389c)
#### Friday 2023-12-08 14:44:12 by Tim Deeb-Swihart

Replace gogo/protobuf with google/protobuf (#5032)

**What changed?**

gogo/protobuf has been replaced with Google's official go compiler. 

**Why?**

gogo/protobuf has been deprecated for some time and the community is
moving on, building new tools (like vtproto) atop google's v2 compiler.

**How did you test it?**

`make test`

**Potential risks**

1. The change from embedded gogo-generated-structs to
google-generated-pointers-to-structs created a risk of nil pointer
exceptions. I've fixed all the ones our tests found but it's possible
there are more lurking in the new code.
2. This change may cause our performance to decrease. Certainly
encoding/deconding of proto objects will become slower, but the overuse
of pointers by the google compiler may negatively affect our overall
performance. We'll need to keep an eye on the GC stats
3. This breaks the HTTP API. We will not support [shortand payload
encoding](https://github.com/temporalio/proposals/blob/master/api/http-api.md#payload-formatting)
in this first pass; that will come once this initial work is in testing.

**Breaking changes for developers**

- `*time.Time` in proto structs will now be
[timestamppb.Timestamp](https://pkg.go.dev/google.golang.org/protobuf@v1.31.0/types/known/timestamppb#section-documentation)
- `*time.Duration` will now be
[durationpb.Duration](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb)
- V2-generated structs embed locks, so you cannot dereference them. `go
vet` will scream at you about this. If you need a copy, use
`proto.Clone`.
- If the performance of this sucks then I will either update our code
generator to add shallow-clone methods or hand-roll the ones we need
- Proto enums will, when formatted to JSON, now be in
`SCREAMING_SNAKE_CASE` rather than `PascalCase`. We decided (in
discussion with the SDK team) that now was as good a time as any to rip
the bandage off.
- Proto objects, or objects embedding protos, cannot be compared using
`reflect.DeepEqual` or _anything_ that uses it. This includes `testify`
and `mock` equality testers!
- You will need to use the `common/testing/protorequire`,
`common/testing/protoassert`, or `common/testing/protomock` packages
instead. I've implemented proto-compatible matchers and assertions there
for all cases I've encountered
- If you need `reflect.DeepEqual` for any reason you can use
`go.temporal.io/api/temporalproto.DeepEqual` instead

Note that history loading will not be impacted by the JSON changes: I
rewrote history loading to dynamically fix incoming history JSON data
(like all our other sdks); you can find this code in [my fork of our go
API](https://github.com/tdeebswihart/temporal-api-go/blob/master/internal/temporalhistoryv1/load.go)
alongside its tests.

**🚨Sharp Edges Introduced🚨**

Beware `*timestamppb.Timestamp.AsTime()`. If you need to extract a time
value from a proto time (timestamppb) **always** make sure to check
whether it's nil first. When the proto object is `nil` `AsTime()` will
return a non-zero time at the proto epoch: UTC midnight on January 1,
1970.

I've made this mistake multiple times during this transition and each
time it's been a pain to debug

**Is hotfix candidate?**

No.

---
## [neondatabase/neon](https://github.com/neondatabase/neon)@[c7f1143e57...](https://github.com/neondatabase/neon/commit/c7f1143e570924eadd15053949647707ba042c5b)
#### Friday 2023-12-08 15:01:39 by Christian Schwarz

concurrency-limit low-priority initial logical size calculation [v2] (#6000)

Problem
-------

Before this PR, there was no concurrency limit on initial logical size
computations.

While logical size computations are lazy in theory, in practice
(production), they happen in a short timeframe after restart.

This means that on a PS with 20k tenants, we'd have up to 20k concurrent
initial logical size calculation requests.

This is self-inflicted needless overload.

This hasn't been a problem so far because the `.await` points on the
logical size calculation path never return `Pending`, hence we have a
natural concurrency limit of the number of executor threads.
But, as soon as we return `Pending` somewhere in the logical size
calculation path, other concurrent tasks get scheduled by tokio.
If these other tasks are also logical size calculations, they eventually
pound on the same bottleneck.

For example, in #5479, we want to switch the VirtualFile descriptor
cache to a `tokio::sync::RwLock`, which makes us return `Pending`, and
without measures like this patch, after PS restart, VirtualFile
descriptor cache thrashes heavily for 2 hours until all the logical size
calculations have been computed and the degree of concurrency /
concurrent VirtualFile operations is down to regular levels.
See the *Experiment* section below for details.

<!-- Experiments (see below) show that plain #5479 causes heavy
thrashing of the VirtualFile descriptor cache.
The high degree of concurrency is too much for 
In the case of #5479 the VirtualFile descriptor cache size starts
thrashing heavily.


-->

Background
----------

Before this PR, initial logical size calculation was spawned lazily on
first call to `Timeline::get_current_logical_size()`.

In practice (prod), the lazy calculation is triggered by
`WalReceiverConnectionHandler` if the timeline is active according to
storage broker, or by the first iteration of consumption metrics worker
after restart (`MetricsCollection`).

The spawns by walreceiver are high-priority because logical size is
needed by Safekeepers (via walreceiver `PageserverFeedback`) to enforce
the project logical size limit.
The spawns by metrics collection are not on the user-critical path and
hence low-priority. [^consumption_metrics_slo]

[^consumption_metrics_slo]: We can't delay metrics collection
indefintely because there are TBD internal SLOs tied to metrics
collection happening in a timeline manner
(https://github.com/neondatabase/cloud/issues/7408). But let's ignore
that in this issue.

The ratio of walreceiver-initiated spawns vs
consumption-metrics-initiated spawns can be reconstructed from logs
(`spawning logical size computation from context of task kind {:?}"`).
PR #5995 and #6018 adds metrics for this.

First investigation of the ratio lead to the discovery that walreceiver
spawns 75% of init logical size computations.
That's because of two bugs:
- In Safekeepers: https://github.com/neondatabase/neon/issues/5993
- In interaction between Pageservers and Safekeepers:
https://github.com/neondatabase/neon/issues/5962

The safekeeper bug is likely primarily responsible but we don't have the
data yet. The metrics will hopefully provide some insights.

When assessing production-readiness of this PR, please assume that
neither of these bugs are fixed yet.


Changes In This PR
------------------

With this PR, initial logical size calculation is reworked as follows:

First, all initial logical size calculation task_mgr tasks are started
early, as part of timeline activation, and run a retry loop with long
back-off until success. This removes the lazy computation; it was
needless complexity because in practice, we compute all logical sizes
anyways, because consumption metrics collects it.

Second, within the initial logical size calculation task, each attempt
queues behind the background loop concurrency limiter semaphore. This
fixes the performance issue that we pointed out in the "Problem" section
earlier.

Third, there is a twist to queuing behind the background loop
concurrency limiter semaphore. Logical size is needed by Safekeepers
(via walreceiver `PageserverFeedback`) to enforce the project logical
size limit. However, we currently do open walreceiver connections even
before we have an exact logical size. That's bad, and I'll build on top
of this PR to fix that
(https://github.com/neondatabase/neon/issues/5963). But, for the
purposes of this PR, we don't want to introduce a regression, i.e., we
don't want to provide an exact value later than before this PR. The
solution is to introduce a priority-boosting mechanism
(`GetLogicalSizePriority`), allowing callers of
`Timeline::get_current_logical_size` to specify how urgently they need
an exact value. The effect of specifying high urgency is that the
initial logical size calculation task for the timeline will skip the
concurrency limiting semaphore. This should yield effectively the same
behavior as we had before this PR with lazy spawning.

Last, the priority-boosting mechanism obsoletes the `init_order`'s grace
period for initial logical size calculations. It's a separate commit to
reduce the churn during review. We can drop that commit if people think
it's too much churn, and commit it later once we know this PR here
worked as intended.

Experiment With #5479 
---------------------

I validated this PR combined with #5479 to assess whether we're making
forward progress towards asyncification.

The setup is an `i3en.3xlarge` instance with 20k tenants, each with one
timeline that has 9 layers.
All tenants are inactive, i.e., not known to SKs nor storage broker.
This means all initial logical size calculations are spawned by
consumption metrics `MetricsCollection` task kind.
The consumption metrics worker starts requesting logical sizes at low
priority immediately after restart. This is achieved by deleting the
consumption metrics cache file on disk before starting
PS.[^consumption_metrics_cache_file]

[^consumption_metrics_cache_file] Consumption metrics worker persists
its interval across restarts to achieve persistent reporting intervals
across PS restarts; delete the state file on disk to get predictable
(and I believe worst-case in terms of concurrency during PS restart)
behavior.

Before this patch, all of these timelines would all do their initial
logical size calculation in parallel, leading to extreme thrashing in
page cache and virtual file cache.

With this patch, the virtual file cache thrashing is reduced
significantly (from 80k `open`-system-calls/second to ~500
`open`-system-calls/second during loading).


### Critique

The obvious critique with above experiment is that there's no skipping
of the semaphore, i.e., the priority-boosting aspect of this PR is not
exercised.

If even just 1% of our 20k tenants in the setup were active in
SK/storage_broker, then 200 logical size calculations would skip the
limiting semaphore immediately after restart and run concurrently.

Further critique: given the two bugs wrt timeline inactive vs active
state that were mentioned in the Background section, we could have 75%
of our 20k tenants being (falsely) active on restart.

So... (next section)

This Doesn't Make Us Ready For Async VirtualFile
------------------------------------------------

This PR is a step towards asynchronous `VirtualFile`, aka, #5479 or even
#4744.

But it doesn't yet enable us to ship #5479.

The reason is that this PR doesn't limit the amount of high-priority
logical size computations.
If there are many high-priority logical size calculations requested,
we'll fall over like we did if #5479 is applied without this PR.
And currently, at very least due to the bugs mentioned in the Background
section, we run thousands of high-priority logical size calculations on
PS startup in prod.

So, at a minimum, we need to fix these bugs.

Then we can ship #5479 and #4744, and things will likely be fine under
normal operation.

But in high-traffic situations, overload problems will still be more
likely to happen, e.g., VirtualFile cache descriptor thrashing.
The solution candidates for that are orthogonal to this PR though:
* global concurrency limiting
* per-tenant rate limiting => #5899
* load shedding
* scaling bottleneck resources (fd cache size (neondatabase/cloud#8351),
page cache size(neondatabase/cloud#8351), spread load across more PSes,
etc)

Conclusion
----------

Even with the remarks from in the previous section, we should merge this
PR because:
1. it's an improvement over the status quo (esp. if the aforementioned
bugs wrt timeline active / inactive are fixed)
2. it prepares the way for
https://github.com/neondatabase/neon/pull/6010
3. it gets us close to shipping #5479 and #4744

---
## [gitRaiku/suijin](https://github.com/gitRaiku/suijin)@[8ee1c56dbd...](https://github.com/gitRaiku/suijin/commit/8ee1c56dbd2a25de2453ad142da7725dc0a260e8)
#### Friday 2023-12-08 15:40:06 by gitRaiku

Kill yourself amdgpu, even my fucking nvidia card works better than this. Why can't you just evaluate if's normally and why the fuck don't you support fucking GL_R8, is it REALLY that hard to implement it? But then when queried you claim that you DO support it. Fuck you.

---
## [sfan5/minetest_game](https://github.com/sfan5/minetest_game)@[4bb4a2a818...](https://github.com/sfan5/minetest_game/commit/4bb4a2a8187d036325482bb727a65b899f8991bd)
#### Friday 2023-12-08 15:59:23 by Yaya - Nurul Azeera Hidayah @ Muhammad Nur Hidayat Yasuyoshi

Update Malay translations
1. Added missing translation to the following files:
  beds.ms.tr, creative.ms.tr, default.ms.tr, farming.ms.tr,
  fire.ms.tr, sethome.ms.tr
2. Changes some translation as per following:
  a. beds.ms.tr
    - Leave Bed changed from Bangun (wake up) to Tinggalkan Katil
      (leave bed, in literal sense) just because the button would
      be interpreted by some people as 'wake up on next morning'
      (ie. skipping night) instead of 'wake up interrupting current
      sleep progress' which is the intended meaning.
  b. boats.ms.tr
    - Boat cruise mode changed from Mod bot layar makan angin to
      Mod jelajah bot, the original translation is more like direct
      translation, and this has been changed to more natural one
      to make sure player know that the mode is a cruise control.
    - Reset changed from Set semula to Tetap semula, this is for
      standardizing with existing term used in various places.
  c. default.ms.tr
    - Page \@1 of \@2 changed from the short form to the long form.
    - Mese Crystal Fragment had missing word 'Kristal' re-added.
  d. dye.ms.tr
    - Dark Grey changed from Kelabu Gelap to Kelabu Tua to make it
      standardized with the colour name elsewhere.
    - Dark Green changed from Hijau Gelap to Hijau Tua to make it
      standardized with the colour name elsewhere.
    - Magenta changed from Merah Lembayung to Magenta, because the
      colour Merah Lembayung is now used to refer to purplish red
      and no longer equal to magenta, the loanword is used instead.
  e. game_commands.ms.tr
    - respawn changed from lahir semula (reborn) to jelma semula
      (reappear), this is to make it consistent with the language
      used in multiple other games that had similar respawning
      system, and avoiding the religious context of life that is
      implied by the use of previous translation.
    - spawnpoint changed from titik permulaan (starting point) to
      titik jelma ((re)appear point), see previous point.
  f. tnt.ms.tr
    - Gun Powder changed from Serbuk Senjata Api (firearms powder)
      to Serbuk Letupan (explosion powder) because that is the
      proper translation, the latter is still the term used even
      when talking about actual firearm, the former didn't exist
  g. vessels.ms.tr
    - item changed from barang (thing) to item, this is mainly
      because some of the 'item' that could be stored are not
      some solid 'thing' where the word barang could be used for,
      so using the word item here keep it neutral.
  h. wool.ms.tr
    - Dark Grey changed from Kelabu Gelap to Kelabu Tua to make it
      standardized with the colour name elsewhere.
    - Dark Green changed from Hijau Gelap to Hijau Tua to make it
      standardized with the colour name elsewhere.
    - Magenta changed from Merah Lembayung to Magenta, because the
      colour Merah Lembayung is now used to refer to purplish red
      and no longer equal to magenta, the loanword is used instead.

---
## [cjvogel1972/advent-of-code-2023](https://github.com/cjvogel1972/advent-of-code-2023)@[75f8f263b4...](https://github.com/cjvogel1972/advent-of-code-2023/commit/75f8f263b4789566275c60c248a3a807d4edad93)
#### Friday 2023-12-08 19:56:05 by Chris Vogel

Solution for Day 8

Another not too difficult puzzle. Started with brute force for
part 2, but realized it didn't work. Couldn't remember the least
common multiple algorithm at first. Thankful that I found it and
the fact that python has a built-in function.

After watching HyperNeutrino's video for today, I realized I had
an incorrect assumption in part 2 that didn't actually hurt me.
The assumption was that if I had to keep going from the end, the
next iteration of the path was the same distance going Z to Z as
going from A to Z. This is what the example show, but I didn't
properly think that through. In theory, if it takes 10 steps to
get from A to Z, it could take 3 to get to the next Z. If I
was being more thorough, I should have figured out steps to the
next Z and to see if there is possibly any loop back to one of
the Z nodes, if not the first Z node. Because the puzzle did
have the same length, my lcm function worked. If that wasn't the
case, there would have needed to be a lot more computing of moves
and computations to get there. I think I could come up with a
better way of doing it than brute force, but I'm glad the
original idea acutally worked. The video is here:
https://youtu.be/_nnxLcrwO_U?si=QqUxP1yRvThlxshG

Started early this morning with a break in between.
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
  8   08:08:30  36989      0   09:46:33  27782      0

---
## [IsaacExists/tgstation](https://github.com/IsaacExists/tgstation)@[2e0597d055...](https://github.com/IsaacExists/tgstation/commit/2e0597d055fc105037a904355726139434f36b3a)
#### Friday 2023-12-08 20:22:33 by Vekter

Replaces the fake monkey cube in Birdshot tool storage with a less lethal one, adds something else fun (#80030)

## About The Pull Request
One of the "monkey cubes" in Birdshot's tool storage was actually a
gorilla cube. This was funny up until people realized it was a thing and
now people are using it intentionally to grief. I'd rather not.

It's a different cube now. I don't want to spoil it but it won't kill
anyone, just make people laugh.

I added a different fun item to another tile in tool storage. Again, no
spoilers, read the code if you really want to know what it was.

## Why It's Good For The Game
I like the "cube says it's a monkey but it's not" joke. It was funny
when people thought it was a monkey, used it, and got killed by it.
Problem is, people know what it is now and have used it for grief
purposes, so we can't have nice things. Gorillas are stupid hard to kill
and will de-limb people by looking at them.

I wanted to add something else fun to replace it that isn't just the
exact same joke but now it won't kill you, so I did.

## Changelog
:cl: Vekter
del: Replaced the "monkey cube" in Birdshot's tool storage with a
different "monkey cube".
add: Added a fun surprise item to Birdshot's tool storage to compensate
for the above change.
/:cl:

---
## [apollographql/federation](https://github.com/apollographql/federation)@[4e630d964e...](https://github.com/apollographql/federation/commit/4e630d964eeeba5a42ecd13f02f6e8f5b757523e)
#### Friday 2023-12-08 20:23:36 by Edward Huang

docs: fix broken links (#2885)

<!--
First, 🌠 thank you 🌠 for taking the time to consider a contribution to
Apollo!

Here are some important details to follow:

* ⏰ Your time is important
To save your precious time, if the contribution you are making will
take more than an hour, please make sure it has been discussed in an
        issue first. This is especially true for feature requests!

* 💡 Features
Feature requests can be created and discussed within a GitHub Issue.
Be sure to search for existing feature requests (and related issues!)
prior to opening a new request. If an existing issue covers the need,
please upvote that issue by using the 👍 emote, rather than opening a
        new issue.

* 🕷 Bug fixes
These can be created and discussed in this repository. When fixing a
bug,
please _try_ to add a test which verifies the fix. If you cannot, you
should
still submit the PR but we may still ask you (and help you!) to create a
test.

* Federation versions
Please make sure you're targeting the federation version you're opening
the PR for. Federation 2 (alpha) is currently located on the `main`
branch and prior versions of Federation live on the `version-0.x`
branch.

* 📖 Contribution guidelines
Follow
https://github.com/apollographql/federation/blob/HEAD/CONTRIBUTING.md
when submitting a pull request. Make sure existing tests still pass, and
add
        tests for all new behavior.

* ✏️ Explain your pull request
Describe the big picture of your changes here to communicate to what
        your pull request is meant to accomplish. Provide 🔗 links 🔗 to
        associated issues!

We hope you will find this to be a positive experience! Open source
contribution can be intimidating and we hope to alleviate that pain as
much
as possible. Without following these guidelines, you may be missing
context
that can help you succeed with your contribution, which is why we
encourage
discussion first. Ultimately, there is no guarantee that we will be able
to
merge your pull-request, but by following these guidelines we can try to
avoid disappointment.

-->

---
## [Addust/Yogstation](https://github.com/Addust/Yogstation)@[75c13f4eff...](https://github.com/Addust/Yogstation/commit/75c13f4effbd82c8dc661c6b3bbc0146de44fded)
#### Friday 2023-12-08 20:28:44 by cowbot92

[PORT] Adds several more signs for the bar to use (#20997)

* yo fuck emisssives

that shit sucks

* sure the rest of these can come too

I guess

* no 100% orange juice

sorry

---
## [MysticalFaceLesS/Shiptest](https://github.com/MysticalFaceLesS/Shiptest)@[173fb06ed3...](https://github.com/MysticalFaceLesS/Shiptest/commit/173fb06ed32897dc6a58f2cc32f6fcb60747c9a9)
#### Friday 2023-12-08 20:53:55 by Imaginos16

Li Tieguai: Cybersun Edition (#2505)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

This PR reworks and updates the Li Tieguai's design into a Cybersun
Ship, as it was outlined in its lore, and what it was slated to become.

![2023-11-22 02 00
49](https://github.com/shiptest-ss13/Shiptest/assets/77556824/cc6a667a-e5dd-46ab-84fe-8351e050bf60)

![2023-11-22 02 00
50](https://github.com/shiptest-ss13/Shiptest/assets/77556824/68face8f-3bb9-4314-9cbc-3db5e92b9fa7)

(SHIP IS NOW FUCKING FLIPPED LET'S GO)

This PR also adds a new job, the Medical Director. It functions exactly
as how a CMO would, but for Cybersun instead!

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/5c93414c-4805-4b38-8ee7-e08ebde3c9ee)

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

MEDICAL CYBERSUN SHIP IS FINALLY REAL OH MY GOD.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

:cl: PositiveEntropy
add: The Li-Tieguai is now officially, a Syndicate ship!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [lowercase2/cohort_18_lls](https://github.com/lowercase2/cohort_18_lls)@[a074af54d2...](https://github.com/lowercase2/cohort_18_lls/commit/a074af54d2fd35d0b210bc7f0c7b0576dfed50bd)
#### Friday 2023-12-08 21:51:13 by Drihmia

Update example.py

I bothered myself removing self from __init__, magical method when it called with super in derived class.

I should not that, adding self is not necessarily because super() handles that and it is a good practice.

The behavior of the program won't effected with this changes.

Thank you for the opportunity!

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[2631b0b8ef...](https://github.com/tgstation/tgstation/commit/2631b0b8ef1a85c75500916215fae69477784558)
#### Friday 2023-12-08 22:18:19 by Jeremiah

Replaces prettierx with the normal prettier (#80189)

## About The Pull Request
Oh god the file diff... I'm so, so sorry.

No need to worry though. This just replaces the prettierx version that
we were using and replaces it with normal prettier. Most of the settings
were default or no longer valid with this version.
## Why It's Good For The Game
You no longer get this warning #70484

It actually drives me up the wall and I have to click it each time I
open my editor.
## Changelog
N/A nothing player facing

---
## [ChaosIsFramecode/TheDonutProject](https://github.com/ChaosIsFramecode/TheDonutProject)@[cb324fa132...](https://github.com/ChaosIsFramecode/TheDonutProject/commit/cb324fa1328ea9bc3e2a9910a44b1e962fbe08ab)
#### Friday 2023-12-08 22:28:58 by IOKG04

It... kinda works now

It still messes up quite a bit of stuff, doesnt fill stuff with spaces to make them a perfect donut, doesnt take a lot of stuff into account and is very poorly optimized, but it kinda works, and with that im happy for the day

Lets hope i remember what i coded tomorrow... (I followed pretty much no common patterns n stuff, so it isnt a guaranty, but if I do there should be a donut.ascii.svg tomorrow :D)

---
## [MERNDevTinkal/Quiz-Game-App](https://github.com/MERNDevTinkal/Quiz-Game-App)@[b10904d885...](https://github.com/MERNDevTinkal/Quiz-Game-App/commit/b10904d8853c13b8039feb9d7e21a8e0d4bfb75b)
#### Friday 2023-12-08 22:35:18 by Tinkal Kumar

Create README.md

Quiz Game App
Quiz Game App

Welcome to the Quiz Game App, an interactive trivia experience where you can test your knowledge across a variety of categories. This web application is designed to provide users with an engaging and entertaining way to challenge themselves with random quizzes.

Features
Diverse Categories: Explore a broad range of topics, from general knowledge to specific interests.

Randomized Questions: Enjoy a dynamic quiz experience with randomly ordered questions for each round.

User-Friendly Interface: Navigate seamlessly through the app with a clean and intuitive design.

Score Tracking: Monitor your progress in real-time and strive for higher scores.

How to Play
Visit the Quiz Game App website.

Start a quiz and answer the questions presented to you.

For each correct answer, you earn points; for incorrect answers, a small penalty is applied.

Track your score in real-time and challenge yourself to improve.

Development
The Quiz Game App is built using HTML, CSS, and JavaScript. Feel free to contribute, report issues, or suggest enhancements. Follow the steps below to set up the development environment:

bash
Copy code
# Clone the repository
git clone https://github.com/MERNDevTinkal/Quiz-Game-App.git

# Navigate to the project directory
cd Quiz-Game-App

# Open the index.html file in your browser
Deployment
The live version of the Quiz Game App is deployed on GitHub Pages and can be accessed here.

Credits
Developed by MERNDevTinkal
Feel free to explore, learn, and have fun with the Quiz Game App!

---
## [MLGTASTICa/CEV-Eris](https://github.com/MLGTASTICa/CEV-Eris)@[b92562ad8f...](https://github.com/MLGTASTICa/CEV-Eris/commit/b92562ad8f26c2354730f8a013195a90bbfbe9fd)
#### Friday 2023-12-08 22:46:12 by ValoTheValo

Makes the "Gun" Not spawn in maint, makes MK58 fit in holsters (#8200)

* changes item path to be consistent

i hate kegdo

* kegdo code moment

what fucking moron designed this

* fixes MK58 not fitting in holster

pain

* Update holster.dm

* kegdo moment

---
## [Karodave05/Stack-assignment](https://github.com/Karodave05/Stack-assignment)@[8a06d12fdc...](https://github.com/Karodave05/Stack-assignment/commit/8a06d12fdcb92a7bc2d65be4eb1396c77555d0ab)
#### Friday 2023-12-08 22:47:02 by Karodave05

Add files via upload

Subject: Apology for Irresponsibility
Dear DR Asani Emmanuel ,
I hope this letter finds you well. I am writing to express my sincere apologies for my recent display of irresponsibility, and I want to acknowledge the impact it may have had on you and others involved.
I understand that my actions, or lack thereof, have caused inconvenience, frustration, and disappointment. I take full responsibility for my behavior and the consequences that followed. It was not my intention to let you down, and I deeply regret any stress or inconvenience I may have caused.
I recognize that being irresponsible is not a reflection of the values I uphold, and I am committed to making amends. I am taking immediate steps to rectify the situation and prevent such lapses in responsibility in the future. I am seeking guidance, learning from this experience, and implementing changes to ensure that I fulfill my obligations and commitments with the utmost diligence.
I understand the importance of accountability, and I assure you that I am dedicated to regaining your trust. Your understanding means a lot to me, and I am grateful for any opportunity you may grant me to make things right.
Once again, I am truly sorry for any inconvenience or disappointment my actions have caused. I appreciate your patience and understanding during this time.
Thank you for taking the time to read this letter. I value our relationship and hope that we can move forward positively.
Sincerely,
Idoghor Oghenekaro David 21CD008269

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[dc234c9939...](https://github.com/cmss13-devs/cmss13/commit/dc234c9939efeb43170a934437f50148323407f7)
#### Friday 2023-12-08 23:01:53 by InsaneRed

Oppressor cooldown changes (#5154)

# About the pull request

Lowers the oppressor tail_abudct (the hook) to 15 seconds of cooldown
and makes the windup faster.

Makes punch shave off cooldown from the abduct for 5 seconds 

All have been tested but i would like this to get testmerged first so i
can actually see the results in game, nothing is set in stone and i want
to edit this further so the cd / cd reduction isnt too powerful, they're
just numbers ive decided were good enough to atleast make the caste
decent for the time being.


# Explain why it's good for the game

Oppressor has been a snoozer strain for a while now where you cast an
ability, and IF it hits you get to play the game otherwise you wait 20
seconds and thats just not fun. Especially for what the ability is, a 20
second cooldown is not worth it.

I've talked with a few people that all agree that the downtime for what
you "could" do with oppressor is not worth it. And i have to agree with
them, the caste feels boring to play and its basically half dead due to
the amnout of downtime you have between abilities compared to how
everything else works. The idea of this is to make it so its not busted
out of its brain but atleast not an observer++ strain so you can feel
more involved in the gameplay.




# Testing Photographs and Procedure
</details>


# Changelog



:cl:
balance: Oppressor tail abduct changed to 15 seconds and lowers the
windup to 7 deciseconds
balance: Changes around the punch effect so that instead of having to
meet demonic standards, you only need to punch to lower your tail/hook
on oppressor.
fix: You will now automatically punch chest if the target you are aiming
at is delimbed instead of doing nothing
/:cl:

---------

Co-authored-by: InsaneRed <prodexter31@outlook.comm>
Co-authored-by: Birdtalon <birdtalon@gmail.com>

---
## [qt/qtdeclarative](https://github.com/qt/qtdeclarative)@[045f9ce192...](https://github.com/qt/qtdeclarative/commit/045f9ce192d841f3cc36d514b5f238b46488b41e)
#### Friday 2023-12-08 23:35:54 by Shawn Rutledge

Add TextSelection (Tech Preview)

In the Controls text editor example, DocumentHandler always sounded like
a hack, just by its name.

We don't expect to be able to handle multiple selections anytime soon;
but if we realistically expect to have multi-seat support in Qt some
day, then probably the multi-user experience should include support for
multiple text cursors and selections. So we shouldn't paint ourselves
into a corner. QQuickTextControl works with only one QTextCursor most
of the time (but it's private, thus modifiable); and TextEdit has
properties like selectionStart, selectionEnd, selectedText, etc. which
seem to assume that there is only one selection.  So probably if we
needed to support multiple selections, we could add
Q_PROPERTY(QQmlListProperty<QQuickTextSelection> selections ...),
document that those legacy properties just work with the first
selection, and/or deprecate them.

So with that in mind, let's get started with a QQuickTextSelection
object. We add TextEdit.cursorSelection which holds the single selection
near the text cursor. It provides API needed for tracking and
manipulating often-used properties of selected rich text (such as
QTextCharFormat properties) so that DocumentHandler can be removed.

The example now uses TextArea.cursorSelection to manipulate the selected
text's format. It's not possible to be fully declarative with this API
though; we need to call setFont (by assigning a font), but QFont is a
value type, and is not as mergeable as QTextCharFormat is, for example.
If we used a binding rather than Action.onTriggered, it would trigger
reading the font for an entire span of selected text (which may have had
multiple fonts), setting one attribute (like bold), then applying the
font to the whole span. What we do now is almost like that; but instead
of reading the font first, we start with a default-constructed QFont,
set one attribute, and call QTextCursor::mergeCharFormat(), in the hope
that it can merge only the features of QFont that have actually been
set. Unfortunately this is not quite true either: if you toggle the
bold button, it might change the font size too, and so on; so maybe we
really need QTextCharFormat in QML (as a value type, presumably) to
implement those feature-toggling toolbar buttons correctly.

This API is in tech preview, because of such issues as described above;
because we're just scratching the surface of what might be possible;
because we should perhaps compare popular JavaScript text-editing APIs
that might be found elsewhere, in the meantime get feedback from users
during the tech preview phase, and keep iterating.

[ChangeLog][QtQuick][TextEdit] TextEdit.cursorSelection is a
TextSelection object, which provides properties to inspect and modify
the formatting of the single selection that is currently supported.
This API is in Tech Preview.

[ChangeLog][Controls][TextArea] TextArea.cursorSelection is a
TextSelection object, which provides properties to inspect and modify
the formatting of the single selection that is currently supported.
This API is in Tech Preview.

Task-number: QTBUG-36521
Task-number: QTBUG-38830
Task-number: QTBUG-81022
Change-Id: Icea99f633694aa712d0b4730b77369077288540f
Reviewed-by: Oliver Eftevaag <oliver.eftevaag@qt.io>

---

