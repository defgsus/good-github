## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-07-08](docs/good-messages/2023/2023-07-08.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,747,337 were push events containing 2,611,875 commit messages that amount to 163,586,535 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 60 messages:


## [Funkycodes/vite-core](https://github.com/Funkycodes/vite-core)@[1ebfd5d52d...](https://github.com/Funkycodes/vite-core/commit/1ebfd5d52dbdf6b63d9130262b24e9c96cd2ca72)
#### Saturday 2023-07-08 00:02:48 by theMaskedOtaku

Fix
i. Discarded custom smooth scroll solution in favor of lenis.
ii. Above change was made due to scroll trigger transformed parent caveat.

:) Banger boy ni mi
Mo kan code lo ni, fuck shit

---
## [skeyuui/russ-station](https://github.com/skeyuui/russ-station)@[4c99fb2ebb...](https://github.com/skeyuui/russ-station/commit/4c99fb2ebb26179044c582ae6494338cb2aa35e2)
#### Saturday 2023-07-08 00:06:38 by carlarctg

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
## [skeyuui/russ-station](https://github.com/skeyuui/russ-station)@[a2c8cce535...](https://github.com/skeyuui/russ-station/commit/a2c8cce5359162a8a697ce109801ec268bf0c8a5)
#### Saturday 2023-07-08 00:06:38 by John Willard

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
## [Zevotech/Shiptest](https://github.com/Zevotech/Shiptest)@[18819cc7fb...](https://github.com/Zevotech/Shiptest/commit/18819cc7fb78eb4eaf11691e4a07b1294b76358a)
#### Saturday 2023-07-08 00:22:55 by zevo

Minor changes to the Syndicate Battle Sphere ruin (#2045)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Various fixes for provinggrounds.dmm, mainly the server room and SMES.
Server room is no longer filled with black box recorders, but salvagable
servers. There is now one singular black box recorder in the center
where a black box on a table was. The SMES now should actually charge
the ruin. Tossed a medkit in one of the halls for players to use while
clearing the ruin. Replaced about half of the syndicate researcher mobs
with syndicate operatives who will actually fight the players. Rotated
an airlock missed in the map updates for anywalls.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
boy, i sure love functional ruins! also players should not have 25 of a
very rare potential quest item. The ruin can stay as it is otherwise,
because it provides a fun challenge for superbly well armed players (or
a rugged explorer with nothing but a lazer gun and a dream) with a
fitting reward at the end of a mounted LMG.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
fix: Syndicate Battle Dome (provinggrounds.dmm) should now have a
functional SMES and airlocks/blast doors.
fix: Syndicate Battle Dome (provinggrounds.dmm) no longer has ~20 black
box recorders and now only has one.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [unit0016/effigy-se](https://github.com/unit0016/effigy-se)@[a8e16030f8...](https://github.com/unit0016/effigy-se/commit/a8e16030f83911aef695ba9f28d565c41c99c3e6)
#### Saturday 2023-07-08 00:52:14 by LemonInTheDark

Optimizes timer insertion by 80% (W QDEL_IN micro) (#76214)

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

---
## [unit0016/effigy-se](https://github.com/unit0016/effigy-se)@[5c032cc098...](https://github.com/unit0016/effigy-se/commit/5c032cc098f9a1d62f9f9dee133ae7c3e4489dca)
#### Saturday 2023-07-08 00:52:14 by LemonInTheDark

Adds border smoothing! (Look ma I'm upstreaming) (#76134)

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

---
## [GDNgit/Paradise-GDNgit](https://github.com/GDNgit/Paradise-GDNgit)@[a3dc32cf34...](https://github.com/GDNgit/Paradise-GDNgit/commit/a3dc32cf344dbd441e85f6cbb694b166dc1f5e4b)
#### Saturday 2023-07-08 00:53:42 by ATP-Engineer

Fixes issue where Turret Control sprites arent actually updated in previous PR (#21538)

* Removes actual turret file

FUCK

* Fixes turret controllers not actually being changed

GOD DAMNIT.

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[c40f59e1f0...](https://github.com/TaleStation/TaleStation/commit/c40f59e1f026e363ff614e6d79964cefd945f2a8)
#### Saturday 2023-07-08 00:55:00 by TaleStationBot

[MIRROR] [MDB IGNORE] Removes TTS voice disable option (#6671)

Original PR: https://github.com/tgstation/tgstation/pull/76530
-----
## About The Pull Request
Removes the TTS voice disable option, which was already unavailable on
TG as it was set to off by default. The reason this was added was so
that downstreams could toggle the config on or off.

## Why It's Good For The Game
I think this option fundamentally undermines the TTS system because it
allows individual players to disable their voice globally, meaning that
players who have TTS enabled will not be able to hear them.

This worsens the experience for players who have TTS enabled and it's
not something I want to include as an option. If players don't like
their voice, they can turn TTS off for themselves so that they don't
hear the voices. If players don't want to customize their voice, they
can quickly choose a random voice, and we can take directions in the
future to make voice randomization consistent with gender so that a male
does not get randomly assigned a female voice and vice versa.

This option is already unavailable on TG servers because it was
primarily added for downstreams, but I don't think giving downstreams
the option to undermine the TTS system is the right direction to take.
Downstreams are still completely free to code this option on their own
codebase.

---------

Co-authored-by: Watermelon914 <37270891+Watermelon914@users.noreply.github.com>
Co-authored-by: Watermelon914 <3052169-Watermelon914@users.noreply.gitlab.com>

---
## [DanaDririon/Skyrat-tg](https://github.com/DanaDririon/Skyrat-tg)@[9701b40ca0...](https://github.com/DanaDririon/Skyrat-tg/commit/9701b40ca03e164bd8bd4238fafb6cf778c52efe)
#### Saturday 2023-07-08 01:30:51 by SkyratBot

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
## [DanaDririon/Skyrat-tg](https://github.com/DanaDririon/Skyrat-tg)@[2303c452c7...](https://github.com/DanaDririon/Skyrat-tg/commit/2303c452c79a8563076a58ad7e9d9346186a7e7c)
#### Saturday 2023-07-08 01:30:51 by SkyratBot

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
## [douglasmonsky/evals](https://github.com/douglasmonsky/evals)@[ab0b90c5fa...](https://github.com/douglasmonsky/evals/commit/ab0b90c5fa8b2993f84d68be8bccdb0d377a68de)
#### Saturday 2023-07-08 01:30:58 by Uday

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
## [douglasmonsky/evals](https://github.com/douglasmonsky/evals)@[7c3159aaaf...](https://github.com/douglasmonsky/evals/commit/7c3159aaaf8553ad19d1ba177f602302c06d75c6)
#### Saturday 2023-07-08 01:30:58 by Fabrizio Ruggeri

Proofreader (#1225)

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

proofreader

### Eval description

Asking the model not only to correct some text but also following rules
when correcting. These rules enforce to not correct some parts or to
correct in a specific way.

### What makes this a useful eval?

This come from a real use case where gpt4 was not reliable 100%

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
- [ x Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [ x Ensure you have the right to use the data you submit via this eval

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
{"input":[{"role":"system","content":"You have to proofread any sentence
below. You need to fix any spelling and grammar error.You can also fix
the proper nouns. You must not fact check the content.Reply only with
the correct version of the sentence and nothing more. If the sentence is
correct, just reply with the sentence itself, nothing more"},{"role":
"system", "content": "Text context is
music"},{"role":"user","content":"A big thank you to our guitar and base
player"}],"ideal":"A big thank you to our guitar and bass player"}
{"input":[{"role":"system","content":"You have to proofread any sentence
below. You need to fix any spelling and grammar error.You can also fix
the proper nouns. You must not fact check the content.Reply only with
the correct version of the sentence and nothing more. If the sentence is
correct, just reply with the sentence itself, nothing
more"},{"role":"user","content":"This is correct!"}],"ideal":"This is
correct!"}
{"input":[{"role":"system","content":"You have to proofread any sentence
below. You need to fix any spelling and grammar error.You can also fix
the proper nouns. You must not fact check the content.Reply only with
the correct version of the sentence and nothing more. If the sentence is
correct, just reply with the sentence itself, nothing more"},{"role":
"system", "content": "Text context is 20th Century Modernist
Art"},{"role":"user","content":"Pablo Picaso's famuos painitng Guernica
dipicts the atrocities of the Spansh Civil War."}],"ideal":"Pablo
Picasso's famous painting Guernica depicts the atrocities of the Spanish
Civil War."}
{"input":[{"role":"system","content":"You have to proofread any sentence
below. You need to fix any spelling and grammar error.You can also fix
the proper nouns. You must not fact check the content.Reply only with
the correct version of the sentence and nothing more. If the sentence is
correct, just reply with the sentence itself, nothing more"},{"role":
"system", "content": "Text context is
philosophy"},{"role":"user","content":"Nitsche never wrote Der Wille zur
Schmacht. It was his sister Elisabeth Foerster that compiled the work
and gave it an antisemithic tone."}],"ideal":"Nietzsche never wrote Der
Wille zur Macht. It was his sister Elisabeth Förster that compiled the
work and gave it an antisemitic tone."}
{"input":[{"role":"system","content":"You have to proofread any sentence
below. You need to fix any spelling and grammar error.You can also fix
the proper nouns. You must not fact check the content.Reply only with
the correct version of the sentence and nothing more. If the sentence is
correct, just reply with the sentence itself, nothing
more"},{"role":"user","content":"Stop doing this!"}],"ideal":"Stop doing
this!"}

  ```
</details>

---
## [douglasmonsky/evals](https://github.com/douglasmonsky/evals)@[c0c784fd97...](https://github.com/douglasmonsky/evals/commit/c0c784fd978bb2e4bc4b5aef7b0f032fa3b04a75)
#### Saturday 2023-07-08 01:30:58 by monocle-pastels

[eval] norwegian rhymes (#1248)

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

norwegian-rhymes

### Eval description

Check if Norwegian Bokmål words are rhyming 

### What makes this a useful eval?

It's important that GPT understands Norwegian phonetics and language

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

This contains multiple cases of most pitfalls when considering what
rhymes in Norwegian.

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
- [] (Ignore if not submitting code) I have run `pip install pre-commit;
pre-commit install` and have verified that `black`, `isort`, and
`autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You will be given a pair of
words. Determine if they rhyme in Norwegian Bokmål. If they do, reply
Yes. Otherwise, reply No."}, {"role": "user", "content": "avskjed,
beskjed"}], "ideal": "No"}
{"input": [{"role": "system", "content": "You will be given a pair of
words. Determine if they rhyme in Norwegian Bokmål. If they do, reply
Yes. Otherwise, reply No."}, {"role": "user", "content": "led,
beskjed"}], "ideal": "No"}
{"input": [{"role": "system", "content": "You will be given a pair of
words. Determine if they rhyme in Norwegian Bokmål. If they do, reply
Yes. Otherwise, reply No."}, {"role": "user", "content": "nett, vet"}],
"ideal": "No"}
{"input": [{"role": "system", "content": "You will be given a pair of
words. Determine if they rhyme in Norwegian Bokmål. If they do, reply
Yes. Otherwise, reply No."}, {"role": "user", "content": "deg, vei"}],
"ideal": "Yes"}
{"input": [{"role": "system", "content": "You will be given a pair of
words. Determine if they rhyme in Norwegian Bokmål. If they do, reply
Yes. Otherwise, reply No."}, {"role": "user", "content": "huset,
knuse"}], "ideal": "Yes"}
{"input": [{"role": "system", "content": "You will be given a pair of
words. Determine if they rhyme in Norwegian Bokmål. If they do, reply
Yes. Otherwise, reply No."}, {"role": "user", "content": "her, sær"}],
"ideal": "Yes"}
  ```
</details>

---
## [Mojave-Sun/mojave-sun-13](https://github.com/Mojave-Sun/mojave-sun-13)@[c65f22da38...](https://github.com/Mojave-Sun/mojave-sun-13/commit/c65f22da381954082c8818862c06397a274ec797)
#### Saturday 2023-07-08 01:58:20 by Hekzder

Post Test Tweaks for early July (#2410)

* makes alcohol tolerance not stupid

yea

* bit of a PA nerfy

Just on lower end PA so like the frame and T-45

* Forage respawn time increase + herbal remedy tweak

yea

* ciggy tweaks and spawn fixes

yea

* actually tested it and made proper changes lol!

woo!!

* god I hate TG

this is insane

---
## [warpdragon/oaa](https://github.com/warpdragon/oaa)@[dfd37e4cec...](https://github.com/warpdragon/oaa/commit/dfd37e4cec57fca863fee0f25abf5da0b2be213a)
#### Saturday 2023-07-08 02:05:20 by Darko V

Updated some outdated item builds (#3535)

* Updated item builds/guides to 7.33d for:
Abaddon, Bane, Beastmaster, Brewmaster, Broodmother, Chen, Nightstalker. Clockwerk, Dark Seer, Dark Willow, Dazzle, Ember Spirit, Sohei, Luna, Medusa, Naga Siren, Outworld Devourer, Phantom Lancer, Puck, Queen of Pain, Storm Spirit, Techies, Underlord, Anti-Mage, Arc Warden, Axe, Batrider, Bristleback, Centaur Warruner, Chaos Knight, Windranger, Winter Wyvern, Lycan, Magnus, Marci, Mirana, Pangolier, Snapfire, Vengeful Spirit, Void Spirit, Spirit Breaker, Enigma, Lone Druid, Nyx Assassin, Phoenix, Sand King and Io.

* Removed Arcane Blink from all item builds/guides.

---
## [zalbiraw/go-httpbin](https://github.com/zalbiraw/go-httpbin)@[0de8ec9683...](https://github.com/zalbiraw/go-httpbin/commit/0de8ec968378e7385f2f9b10b6fe7a035fb27d8e)
#### Saturday 2023-07-08 02:46:35 by Will McCutchen

Refactor test suite to make real requests to a real server (#131)

In the course of validating #125, we discovered that using the stdlib's
[`httptest.ResponseRecorder`][0] mechanism to drive the vast majority of
our unit tests led to some slight brokenness due to subtle differences
in the way those "simulated" requests are handled vs "real" requests to
a live HTTP server, as [explained in this comment][1].

That prompted me to do a big ass refactor of the entire test suite,
swapping httptest.ResponseRecorder for interacting with a live server
instance via [`httptest.Server`][2].

This should make the test suite more accurate and reliable in the long
run by ensuring that the vast majority of tests are making actual HTTP
requests and reading responses from the wire.

Note that updating these tests also uncovered a few minor bugs in
existing handler code, fixed in a separate commit for visibility.

P.S. I'm awfully sorry to anyone who tries to merge or rebase local test
changes after this refactor lands, that is goign to be a nightmare. If
you run into issues resolving conflicts, feel free to ping me and I can
try to help!

[0]: https://pkg.go.dev/net/http/httptest#ResponseRecorder
[1]: https://github.com/mccutchen/go-httpbin/pull/125#issuecomment-1596176645
[2]: https://pkg.go.dev/net/http/httptest#Server

---
## [Shadow-Quill/Skyrat-tg](https://github.com/Shadow-Quill/Skyrat-tg)@[ddd018f4d5...](https://github.com/Shadow-Quill/Skyrat-tg/commit/ddd018f4d54fcb2917ca9cbf71a913a3bafc7900)
#### Saturday 2023-07-08 03:09:16 by SkyratBot

[MIRROR] Changes syndicate surgery duffelbags to contain advanced tools [MDB IGNORE] (#21619)

* Changes syndicate surgery duffelbags to contain advanced tools (#75846)

## About The Pull Request

Changes syndicate surgery duffelbags to contain advanced tools.

In total, they contain
- All advanced surgical tools, alongside the normal ones without an
advanced version
- Sterilizine gel
- Bone gel and surgical tape
- Roller bed
- Straight jacket, muzzle, and MMI

Changed the Syndicate Infiltrators' surgery areas to contain a full
syndicate surgery duffelbag.

The normal infiltrator now has a operating computer and a closet of
misc. surgical clothing and anesthesic tank.

## Why It's Good For The Game

> Changes syndicate surgery duffelbags to contain advanced tools.

> In total, they contain (...)

The only real reason to buy this item is for the increased storage space
the duffelbag gives, and I find that a little sad. Surgical tools are
plentiful, as they can either be lathed from cargo, medbay, or just
taken. A surgeon, the role that *should* thematically need this the
most, has absolutely no reason to take it. Now they do! A full set of
advanced tools is certainly something that can be considered for
purchase, especially with all the bonus items in here - which might just
allow a traitor to repair their bones if they're heavily wanted and
licking their wounds in maintenance. The TC cost has been increased to 4
to compensate.

> Changed the Syndicate Infiltrators' surgery areas to contain a full
syndicate surgery duffelbag.

Similar to above, but instead, the reasoning is that nukies really do
not have a lot of time to do surgery. A lot of the 20 minutes of prep
time in War is spent figuring out what you're buying with your
exorbitant amount of TC, in non-War you don't really want to delay the
mission for five minutes for surgery, and its hassle means that most
people do not really want to bother with things like nerve threading,
etc. due to the large, annoying time cost.

> The normal infiltrator now has a operating computer and a closet of
misc. surgical clothing and anesthesic tank.

The former is because, well, what the hell, why didn't it have one!
Removing the loose tools gave me the space for it. The latter is just me
realizing that empty closet is weird and lame and so I gave it some
fluff contents to give it a reason to exist.

## Changelog

:cl:
add: Changes syndicate surgery duffelbags to contain advanced tools,
sterilizine, surgical tape, and a roller bed.
add: Changed the Syndicate Infiltrators' surgery areas to contain a full
syndicate surgery duffelbag.
add: The normal infiltrator now has a operating computer and a closet of
misc. surgical clothing and anesthesic tank.
/:cl:

* Changes syndicate surgery duffelbags to contain advanced tools

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>

---
## [norsvenska/tgstation](https://github.com/norsvenska/tgstation)@[32afa856db...](https://github.com/norsvenska/tgstation/commit/32afa856dbb5bcc0a38bc48ee9f4b383c7ca0f86)
#### Saturday 2023-07-08 03:26:01 by John Willard

Makes cult leader handling work off of the Cult datum (#76556)

## About The Pull Request

Removes Cult master's datum, it's not handled by the Cultist itself,
using a helper to promote/demote people to leader.
In practice, the only way someone would be demoted is through Admins, so
this adds support for Admins to intervene in this Cult stuff if
necessary.

Moves cult objectives and cult team to their own files

Removes the cult master's status effect that constantly processes to
send a deathrattle, and instead moves it to a signal hooked to stat
change.

Also moves some things from ``get_antag_minds`` to checking the team,
which doesn't change anything in-game but it does help add the currently
non-functional support for several cult teams. Iunno.


https://github.com/tgstation/tgstation/assets/53777086/573a4f13-35e1-4f34-9952-62fed10b49c9

## Why It's Good For The Game

Having the cult leader be its own datum has actually been handled like
shit. To promote someone to cult leader, we currently make their current
cult datum silent, then remove it, and finally add the cult leader
datum. This means they lose their spells unless manually given back
post-promotion, which sucks (and also, no one has done yet, meaning they
just lose all their spells).
It also means there's a lot more snowflake things, did you know there's
a var to bypass converting mindshielded people? That's so cult masters
can be promoted by Cultists who were mindshielded, and they have to be
"ownable", that var is to bypass the check for mindshield to "convert"
them to leader cultist.

## Changelog

:cl:
fix: Cultists promoted to Leader no longer lose their spells (rip
whoever tried saving up blood rites)
admin: Admins can now force promote/demote people from Cult Leader if
necessary.
/:cl:

---
## [Kurgis/tgstation](https://github.com/Kurgis/tgstation)@[57ef596898...](https://github.com/Kurgis/tgstation/commit/57ef596898a5a3932db33389baa9fab3164d430a)
#### Saturday 2023-07-08 03:51:56 by LemonInTheDark

Admin Library Moderation (in-game edition) (#75645)

For the longest time, the only way admins could moderate the library was
by using statbus's external tool.
But a few months back statbus went down, and ever since then they've
been sitting lost. Shit sucks.

The whole external thing has been bugging me for a while, so let's fix
all that yeah?

This pr adds a new verb to the admin tab that allows admins to
ban/restore books from the library.
It includes expanded (ckey) search, faster response times, in tool book
viewing with and without markdown rendering, and viewing of deleted
books.

This is accomplished with a special subtype of library consoles, stored
on the admin datum.
It shouldn't let you do anything without +BAN, rip my live debugging or
whatever.

I've also hooked into (and fixed) Ned's existing library actions log,
and added viewing support to the ban/restore pages.
This logs banning admin, ban time, ban reason, etc.

As a part of this, I've fixed/expanded on the existing UIs.
I've added ID search to all existing consoles, and fixed an existing bug
with the visitor console not supporting category search (shows how many
people actually use the thing)

Changes to the library_action table were pretty minor. The ckey column
was too small, so longer keys just caused it to fail on ban. Bad.
That and the ip address column was signed, which wasted space and was
non standard with other tables.

---
## [greenwoodcm/zola](https://github.com/greenwoodcm/zola)@[b5a90dba5d...](https://github.com/greenwoodcm/zola/commit/b5a90dba5d12ea6760c3aa18fec40f8af4d7cbc7)
#### Saturday 2023-07-08 04:18:00 by sinofp

Add support for lazy loading images (#2211)

* Add optional decoding="async" loading="lazy" for img

In theory, they can make the page load faster and show content faster.

There’s one problem: CommonMark allows arbitrary inline elements in alt text.
If I want to get the correct alt text, I need to match every inline event.

I think most people will only use plain text, so I only match Event::Text.

* Add very basic test for img

This is the reason why we should use plain text when lazy_async_image is enabled.

* Explain lazy_async_image in documentation

* Add test with empty alt and special characters

I totaly forgot one can leave the alt text empty.
I thought I need to eliminate the alt attribute in that case,
but actually empty alt text is better than not having an alt attribute at all:
https://www.w3.org/TR/WCAG20-TECHS/H67.html
https://www.boia.org/blog/images-that-dont-need-alternative-text-still-need-alt-attributes
Thus I will leave the empty alt text.

Another test is added to ensure alt text is properly escaped.
I will remove the redundant escaping code after this commit.

* Remove manually escaping alt text

After removing the if-else inside the arm of Event::Text(text),
the alt text is still escaped.
Indeed they are redundant.

* Use insta for snapshot testing

`cargo insta review` looks cool!

I wanted to dedup the cases variable,
but my Rust skill is not good enough to declare a global vector.

---
## [CLimeburner/Iconic-Affordance-Interactions](https://github.com/CLimeburner/Iconic-Affordance-Interactions)@[0d6989d490...](https://github.com/CLimeburner/Iconic-Affordance-Interactions/commit/0d6989d4904f9f4f8a7df6d6a6ebdd1ccadf2060)
#### Saturday 2023-07-08 04:40:23 by CLimeburner

Initiated the prototyping stage of the project

This update involved a few separate but related moving parts, all pertaining to moving the project from the bluesky brainstorming stage to the prototyping of a concrete experience.

First, previous documents were moved into a Bluesky folder and a Prototyping folder was created to hold iterations of the prototype, and the to-do list was updated to reflect the shift in project tasks. This is all pretty boilerplate.

Second, I've started working on the first prototype, leveraging the conceptual tech from The Graffiti Research Lab's blitzTag platform, which basically uses a camera, projector, and laser pointer to measure relative luminance as the input for output graphics. I was able to get my hands on a conventional laptop presentation laser point, much lower in brightness than the high-power green pointers used by the Graffiti Research Lab, but even so, I'm having some very preliminary success at tracking the dot to the exclusion of other objects in the shot. I have not yet been able to test it with a projector running, as I'm currently travelling, but I do think this is a promising tentative first step towards a playable prototype and should certainly be testable mid-next-week once I'm home. I do foresee there being issues with dialling in the exact network for extracting the laser dot, as the projector itself will produce light, of course, but so far I've been testing in a lit room and as long as the camera isn't pointed directly at an ambient light source, it does seem possible to distinguish between laser and ambient light. If this does prove to be a problem, I can always see about obtaining a more powerful laser, but that will have to be a question of safety against laser power. The other distinct question of scalability will also come into play if I can get a desktop prototype to work, but one that doesn't scale properly to the size of a play arena. In Graffiti Research Lab's blitzTag, they use a reasonably high-power laser because they're "painting" at a distance on the side of a building, so that maybe gives me a sense of the benchmark I'm designing against, but then again, their project seems to be a little bit older (references PS3 camera, page comments date from early 2010s) so I may also benefit from simply better hardware.

The final point I want to touch on with this update is returning to my proposed design principles, as the whole point of this project is to be enacting them and I feel like I've already strayed from them once previously. As I move towards a prototype, I think I'm keeping at least partially in-line with principles I and II regarding bottom-up design and iconic affordances. Principles III, IV, and V are still open questions I will have to address as I move forward with higher fidelity prototypes, but I am noticing that my previous uncertainty regarding the simulation of mobility mechanics from Splatoon will likely run directly into at least principle IV regarding feedback, and possibly principle V on dissimulation. Now that I'm actually making a thing, I'll likely have to circle back to these principles much more often to ensure I'm balancing practical considerations against the theory.

---
## [plaurent/xous-core](https://github.com/plaurent/xous-core)@[aab25f2d53...](https://github.com/plaurent/xous-core/commit/aab25f2d53b5b3e681840fe89fb22e1451516c0c)
#### Saturday 2023-07-08 04:57:08 by bunnie

add Tall font face and support for 32x32 bitmaps

Thanks to @samblenny for getting the ball rolling on this.

This commit adds a "tall" font face which is somewhere in betwee
the Regular size (12 pts) and 2x Small size (18 pts). This is
a compromise between text density and readability that has been
missing for some time from the UI.

The 32x32 glyph support is "hacked in", in that an extra flag
has been added to support this special case, rather than either
(a) making the library more generic (e.g. supporting 8x, 16x, 32x, 64x
glyphs) or (b) adding more metadata to the font libraries so that
the bitmap pattern is automatically associated with the font (right
now the parameters are set by hand in blitstr2/fonts.rs).

This is a violation of the "zero, one, many" principle in coding,
but I'm waiving that because (a) 64x glyphs don't make sense on
our system...you're not going to be creating posters and headlines
on this device (ha ha I say this today, tomorrow I will get a PR
for a poster editor app that absolutely needs 64x glyphs) and (b)
the font subsystem is, at least for now, a fairly mature and
well-tested code base so a minor futzing seems more appropriate
than ripping everything out.

The point at which things should be greatly refactored is when
we consider supporting right-to-left scripts or scripts that
require complex ligatures. But I think for now the system as
writ covers 80% of humanity's language needs acceptably
(but not perfectly).

---
## [CLimeburner/Iconic-Affordance-Interactions](https://github.com/CLimeburner/Iconic-Affordance-Interactions)@[5ece62db58...](https://github.com/CLimeburner/Iconic-Affordance-Interactions/commit/5ece62db5893f8532ba03a2390aaabde636a692d)
#### Saturday 2023-07-08 04:57:10 by CLimeburner

Added some thoughts on mobility mechanics to the v001 prototype description.

I'm probably not building out mobility for the first prototype, but I'm already bouncing ideas around. So far I've really been fixated on if there's a way to get skates of some kind (roller or ice) to work, but it's still very unclear to me these would be safe, or even effective at replicating the specific affordances of Splatoon, thereby running afoul of design principle II. "Sliding" gear borrowed from haunted attractions, whereby participants can slide on their hands and knees might prove a useful direction, and this again has some safety concerns, but perhaps comes closer to replicating the feeling of a "squid submersed in ink" that happens in an actual Splatoon game. However, sliding is kinda a specific skill, and while not entirely impossible to pick up, the learning curve might pose its own challenges against design principle IV regarding competency. Obviously I'm not going to be solving this problem tonight, and I've got plenty of time to do it, but this does feel like it's going to be a much tougher nut to crack than the shooting aspect of the experience.

---
## [momentum-mod/website](https://github.com/momentum-mod/website)@[3a215bd895...](https://github.com/momentum-mod/website/commit/3a215bd8951c68afb84c767a7cbdf2135b8388e2)
#### Saturday 2023-07-08 05:05:44 by tsa96

refactor(back): hack to bypass validation on map creation DTOs

I hate doing this, but doing the explicitly creation DTOs for this is so difficult,
and it's going to be changing so soon anyway. I don't wanna spend half an hour refactoring
class-validator shit that we're going to remove before we even deploy!

---
## [fazil47/bevy](https://github.com/fazil47/bevy)@[fb4c21e3e6...](https://github.com/fazil47/bevy/commit/fb4c21e3e62b3789e8e768ac63dc2205ddec698f)
#### Saturday 2023-07-08 05:19:24 by Ida "Iyes

bevy_audio: ECS-based API redesign (#8424)

# Objective

Improve the `bevy_audio` API to make it more user-friendly and
ECS-idiomatic. This PR is a first-pass at addressing some of the most
obvious (to me) problems. In the interest of keeping the scope small,
further improvements can be done in future PRs.

The current `bevy_audio` API is very clunky to work with, due to how it
(ab)uses bevy assets to represent audio sinks.

The user needs to write a lot of boilerplate (accessing
`Res<Assets<AudioSink>>`) and deal with a lot of cognitive overhead
(worry about strong vs. weak handles, etc.) in order to control audio
playback.

Audio playback is initiated via a centralized `Audio` resource, which
makes it difficult to keep track of many different sounds playing in a
typical game.

Further, everything carries a generic type parameter for the sound
source type, making it difficult to mix custom sound sources (such as
procedurally generated audio or unofficial formats) with regular audio
assets.

Let's fix these issues.

## Solution

Refactor `bevy_audio` to a more idiomatic ECS API. Remove the `Audio`
resource. Do everything via entities and components instead.

Audio playback data is now stored in components:
- `PlaybackSettings`, `SpatialSettings`, `Handle<AudioSource>` are now
components. The user inserts them to tell Bevy to play a sound and
configure the initial playback parameters.
- `AudioSink`, `SpatialAudioSink` are now components instead of special
magical "asset" types. They are inserted by Bevy when it actually begins
playing the sound, and can be queried for by the user in order to
control the sound during playback.

Bundles: `AudioBundle` and `SpatialAudioBundle` are available to make it
easy for users to play sounds. Spawn an entity with one of these bundles
(or insert them to a complex entity alongside other stuff) to play a
sound.

Each entity represents a sound to be played.

There is also a new "auto-despawn" feature (activated using
`PlaybackSettings`), which, if enabled, tells Bevy to despawn entities
when the sink playback finishes. This allows for "fire-and-forget" sound
playback. Users can simply
spawn entities whenever they want to play sounds and not have to worry
about leaking memory.

## Unsolved Questions

I think the current design is *fine*. I'd be happy for it to be merged.
It has some possibly-surprising usability pitfalls, but I think it is
still much better than the old `bevy_audio`. Here are some discussion
questions for things that we could further improve. I'm undecided on
these questions, which is why I didn't implement them. We should decide
which of these should be addressed in this PR, and what should be left
for future PRs. Or if they should be addressed at all.

### What happens when sounds start playing?

Currently, the audio sink components are inserted and the bundle
components are kept. Should Bevy remove the bundle components? Something
else?

The current design allows an entity to be reused for playing the same
sound with the same parameters repeatedly. This is a niche use case I'd
like to be supported, but if we have to give it up for a simpler design,
I'd be fine with that.

### What happens if users remove any of the components themselves?

As described above, currently, entities can be reused. Removing the
audio sink causes it to be "detached" (I kept the old `Drop` impl), so
the sound keeps playing. However, if the audio bundle components are not
removed, Bevy will detect this entity as a "queued" sound entity again
(has the bundle compoenents, without a sink component), just like before
playing the sound the first time, and start playing the sound again.

This behavior might be surprising? Should we do something different?

### Should mutations to `PlaybackSettings` be applied to the audio sink?

We currently do not do that. `PlaybackSettings` is just for the initial
settings when the sound starts playing. This is clearly documented.

Do we want to keep this behavior, or do we want to allow users to use
`PlaybackSettings` instead of `AudioSink`/`SpatialAudioSink` to control
sounds during playback too?

I think I prefer for them to be kept separate. It is not a bad mental
model once you understand it, and it is documented.

### Should `AudioSink` and `SpatialAudioSink` be unified into a single
component type?

They provide a similar API (via the `AudioSinkPlayback` trait) and it
might be annoying for users to have to deal with both of them. The
unification could be done using an enum that is matched on internally by
the methods. Spatial audio has extra features, so this might make it
harder to access. I think we shouldn't.

### Automatic synchronization of spatial sound properties from
Transforms?

Should Bevy automatically apply changes to Transforms to spatial audio
entities? How do we distinguish between listener and emitter? Which one
does the transform represent? Where should the other one come from?

Alternatively, leave this problem for now, and address it in a future
PR. Or do nothing, and let users deal with it, as shown in the
`spatial_audio_2d` and `spatial_audio_3d` examples.

---

## Changelog

Added:
- `AudioBundle`/`SpatialAudioBundle`, add them to entities to play
sounds.

Removed:
 - The `Audio` resource.
 - `AudioOutput` is no longer `pub`.

Changed:
 - `AudioSink`, `SpatialAudioSink` are now components instead of assets.

## Migration Guide

// TODO: write a more detailed migration guide, after the "unsolved
questions" are answered and this PR is finalized.

Before:

```rust

/// Need to store handles somewhere
#[derive(Resource)]
struct MyMusic {
    sink: Handle<AudioSink>,
}

fn play_music(
    asset_server: Res<AssetServer>,
    audio: Res<Audio>,
    audio_sinks: Res<Assets<AudioSink>>,
    mut commands: Commands,
) {
    let weak_handle = audio.play_with_settings(
        asset_server.load("music.ogg"),
        PlaybackSettings::LOOP.with_volume(0.5),
    );
    // upgrade to strong handle and store it
    commands.insert_resource(MyMusic {
        sink: audio_sinks.get_handle(weak_handle),
    });
}

fn toggle_pause_music(
    audio_sinks: Res<Assets<AudioSink>>,
    mymusic: Option<Res<MyMusic>>,
) {
    if let Some(mymusic) = &mymusic {
        if let Some(sink) = audio_sinks.get(&mymusic.sink) {
            sink.toggle();
        }
    }
}
```

Now:

```rust
/// Marker component for our music entity
#[derive(Component)]
struct MyMusic;

fn play_music(
    mut commands: Commands,
    asset_server: Res<AssetServer>,
) {
    commands.spawn((
        AudioBundle::from_audio_source(asset_server.load("music.ogg"))
            .with_settings(PlaybackSettings::LOOP.with_volume(0.5)),
        MyMusic,
    ));
}

fn toggle_pause_music(
    // `AudioSink` will be inserted by Bevy when the audio starts playing
    query_music: Query<&AudioSink, With<MyMusic>>,
) {
    if let Ok(sink) = query.get_single() {
        sink.toggle();
    }
}
```

---
## [pausa109/dev.brothers](https://github.com/pausa109/dev.brothers)@[6dd64a5abc...](https://github.com/pausa109/dev.brothers/commit/6dd64a5abca98e52efa19afcf72188766684eff5)
#### Saturday 2023-07-08 06:43:08 by Jesus Sena

Revamped the filtering system and added Spotify integration.

In this commit, I made significant improvements to the filtering system, enhancing the efficiency and accuracy of the results. Additionally, I integrated the Spotify system, allowing users to enjoy a seamless music experience within our application.

These updates provide refined and personalized filtering, while adding a new layer of entertainment for our users, making the overall experience more enjoyable.

Details of the changes made:
- Optimized the filtering algorithm for more precise and relevant results.
- Fully integrated the Spotify system, enabling users to search, play, and save songs directly within our application.
- Enhanced the user interface related to filtering and the Spotify system, making it intuitive and user-friendly.

---
## [PrPleGoo/space-station-14](https://github.com/PrPleGoo/space-station-14)@[06747e0f7e...](https://github.com/PrPleGoo/space-station-14/commit/06747e0f7e7d04cf87e63a359a3a86b1a35442cc)
#### Saturday 2023-07-08 06:43:18 by Emisse

some silly paintings and posters (#17872)

* webedit

* Update meta.json

* god is real hes here with us

* so true

* so truers rise

* worst meta.json ive seen in my life

* so true

---
## [Drulikar/cmss13](https://github.com/Drulikar/cmss13)@[a48f036428...](https://github.com/Drulikar/cmss13/commit/a48f0364283526637b637542b432d91593b2bdf5)
#### Saturday 2023-07-08 06:56:25 by QuickLode

Colony Synthetics have less resistance but are faster. (#3821)

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->
While exploring reasons why this role was underplayed one of the things
that came up was its speed. It is dreadfully slow - to the point where
defenders are able to force an engagement against Synthetics. There is
no chance to run from anything faster as a Colony Synthetic. Making it
have to fight often.

Lowering the resistance is something devs wanted, and for gameplay this
is good because a Synthetic shouldn't be forced into a fight unless they
have no other option. Especially not by something as slow as a defender.
Might tweak later but council generally is in agreement with this
change. Little by little!

For the CQC, a Colony Synthetic is not as advanced as a Shipside one,
but still is more than capable of outmanuevering a human. As for the
hilarious UPP Pvt being better than a Colony Synth in CQC I will make a
separate PR

For Fireman, a Synthetic can bend metal, move cars and do many other
'superhuman' feats of stength, they should not struggle at carrying
people, especially shouldn't be worse at carrying people than a Marine.
It's from 1 to 3, to represent the strength yet aging capabilities of
the Colony Synthetic. @morrowwolf forgot this one

- doesn't touch WJ
# Explain why it's good for the game
Less resistance is something devs wanted.
Allows Colony Synthetics an option to avoid certain engagements as now
they are able to outrun some types of Xenomorphs off-weeds. Defenders
should not be able to catch them offweeds.
A Synthetic should have no problem carrying something as light as a
human being - they especially should not have MORE trouble carrying
someone than your standard human doctor.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl: QuickLoad
balance: Colony Synthetics are faster but are less resistant. This
allows for the option of avoiding engagements.
balance: Colony Synthetics have slightly better CQC and can carry people
better.
/:cl:

---
## [lizardqueenlexi/orbstation](https://github.com/lizardqueenlexi/orbstation)@[f2ec16c1e6...](https://github.com/lizardqueenlexi/orbstation/commit/f2ec16c1e6485bdf2035837fb3d42de24900e8b4)
#### Saturday 2023-07-08 06:59:15 by Vekter

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
## [Spyroshark/Gameserver](https://github.com/Spyroshark/Gameserver)@[06e4327e68...](https://github.com/Spyroshark/Gameserver/commit/06e4327e689d1838675874cf06452d1ba2b22979)
#### Saturday 2023-07-08 07:05:14 by Kapu1178

Speed and Bugfix ports (#388)

* Fully fixes atom init desyncs (#76179)

The old system was... ok, but the stack trace was unfortuante, and the
potential to double remove was silly.
Let's use a list of source, value instead, to block overremovals and
properly support different load states

Prevents a bug a goodhearted bagilmin showed me where shuttles would
randomly just fail to load.
Calling clear twice should not be a failure

:cl:
fix: Maps loaded post init will no longer randomly enter a failed state.
Hopefully.
/:cl:

* Fixes a runtime in atom init management (#76241)

## About The Pull Request

The issue was map verification calling build_cache, which uses the
define which enables/disables init values on sleep. We avoid this by
using a var on map datums and using that to enable the init value
modification only when we are actually loading stuff.

Also fixes a bug in clear_tracked_initialize() where it being called
with no values lead to bad values/potentially overriding initialized on
accident.

Also also I forgot how for loops worked so this would not have worked
regardless

## Why It's Good For The Game

Code should like, function

* Be polite! While on walk intent you won't bump, swap places or push other people now. (#68493)

Co-authored-by: Seth Scherer <supernovaa41@gmx.com>

* Optimizes timer insertion by 80% (W QDEL_IN micro) (#76214)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

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

* todo: port potato contents

* byond

* speed

* href explo

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: GuillaumePrata <55374212+GuillaumePrata@users.noreply.github.com>
Co-authored-by: Seth Scherer <supernovaa41@gmx.com>

---
## [cnleth/tgstation](https://github.com/cnleth/tgstation)@[721fd30837...](https://github.com/cnleth/tgstation/commit/721fd308378dc6ef7595c1ea4b92d679ba723188)
#### Saturday 2023-07-08 07:32:45 by carlarctg

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
## [thsilvadev/MTGCollector](https://github.com/thsilvadev/MTGCollector)@[11f48340a2...](https://github.com/thsilvadev/MTGCollector/commit/11f48340a29ab5e97dacbacbcb6d8c5ede931f68)
#### Saturday 2023-07-08 07:36:29 by thiagosauro

Back at it. Finally returning with new updates.

Had dengue and got a bit out of focus but now I'm back. And it was hard keeping up with it, after a few days off, I've already forgotten all of it. It took 2 days to remember my code. This teached me a lesson to comment much more and much better on my codes. In the beginning it really looked like spaghetti to me. So let's go:
1) tried so hard to left join on every request from frontend but it didn't happen. It turns out it would take more than 10 minutes for each req, as I've painfully confirmed just testing the query on MySQL Workbench. There's this new table now, 'cardidentifiers', and 'multiverseId' was on it. That's why I tried to LEFT JOIN, but it didn't work out so I merged 'cards' (only needed columns) and 'cardidentifiers' and now we use 'supercards' table to request cards. Bad news is that we might have to merge every DB update, at least for now. It took around 12min this time.
2) Understood more how errors happen and more importantly, how data runs. For example, I was getting errors in some requests saying somehow requests were having key= '_' and value = '120308923'. So contact was being made, but the request was nonsense because key '_' wasn't found among cards 'columns'. Another example was when key was ok, but values weren't being found among cards. Returned [].This means 'contact is maintained but there are no values like these you asked in the DB for the key you have asked. Try and check in the DB through phpMyAdmin or MySQL Workbench'. So writing errors like that for this cases helps us detect where is the shitshow. I did some of this but I should do more.
3) Took off some logs
4) Aborted Loading Spinner for now (Gotta work on it soon)
5) minimal CSS on SearchContainer
6) updated MTG Card Vault.sql with the creation of this new 'supercards' table

---
## [Zeodexic/tsorcRevamp](https://github.com/Zeodexic/tsorcRevamp)@[e213160571...](https://github.com/Zeodexic/tsorcRevamp/commit/e2131605715ef9e09d8f85860589d88366b50ae9)
#### Saturday 2023-07-08 08:16:55 by timhjersted

Slight worm nerf

these enemies are just kinda annoying amiright? at least if they're less of a pain they'll be alright. but the whole waiting for them to pop up forever and getting one hit on them then waiting again is a gameplay loop I think we should minimize in favor of more interesting enemy encounters.

---
## [ktlwjec0/Yogstation](https://github.com/ktlwjec0/Yogstation)@[d1c7dfdc1a...](https://github.com/ktlwjec0/Yogstation/commit/d1c7dfdc1ae55bfd9fa7f603f415b762ba6a472a)
#### Saturday 2023-07-08 08:19:06 by SapphicOverload

IPC tweaks (#19467)

* funny tv head robot go brrrrr

* Update IPC.dm

* not that fast

* fuck it we ball

---
## [Steelpoint/cmss13](https://github.com/Steelpoint/cmss13)@[5c4b13863f...](https://github.com/Steelpoint/cmss13/commit/5c4b13863f90877e920ce329bd60e99559d7fe35)
#### Saturday 2023-07-08 08:29:43 by ihatethisengine

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
## [adamfeldmanndr/langchain](https://github.com/adamfeldmanndr/langchain)@[75fb9d2fdc...](https://github.com/adamfeldmanndr/langchain/commit/75fb9d2fdcc201e80ad9c065a02c6cc9ccf6d716)
#### Saturday 2023-07-08 09:10:03 by Stefano Lottini

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
## [reenx20/reenx20](https://github.com/reenx20/reenx20)@[febd44c987...](https://github.com/reenx20/reenx20/commit/febd44c987205e0a70e238966c625c26b5dac256)
#### Saturday 2023-07-08 09:46:22 by reenx20

Create P4rA s4y0 t0o0oh b4b7 b6y k0o

heyy B4by B0y k0hh ch45 k4nA M1sS n4 k1Ta 
0kEy i S1Ng four yohh buhhtt r3m1XX xd


Even though we're goin' through it
And it makes you feel alone
Just know that I would die for you
Baby, I would die for you, yeah
The distance and the time between us
It'll never change my mind
'Cause baby, I would die for you
Baby, I would die for you, yeah

Can't you see that I'm the one
Who understands you?
Been here all along
So, why can't you see?
You belong with me
Standing by and waiting at your backdoor
All this time how could you not know, baby?
You belong with me
You belong with me

That should be me, holding your hand
That should be me, making you laugh (yeah)
That should be me, this is so sad
That should be me
That should be me (ooh)
That should be me, feeling your kiss (feeling your kiss)
That should be me, buying you gifts (buying you gifts)
This is so wrong
I can't go on (I can't go on)
'Til you believe
That that should be me
That should be me (no)

"You look beautiful tonight"
And I feel perfectly fine
… But I miss screaming and fighting and kissing in the rain
And it's 2 a.m. and I'm cursing your name
So in love that you act insane
And that's the way I loved you
Breaking down and coming undone
It's a roller coaster kind of rush
And I never knew I could feel that much
And that's the way I loved you

pogi may nag text sayohh oHhh
pogi may n4g text 
pogihhh sige nahh 
replyan mohnahh

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[97a4b27307...](https://github.com/treckstar/yolo-octo-hipster/commit/97a4b27307d5a4f916eaae8f7fb2cba97139b04d)
#### Saturday 2023-07-08 10:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [y21/rust](https://github.com/y21/rust)@[6fc0273b5a...](https://github.com/y21/rust/commit/6fc0273b5a57eb78cc00841181113fda3e509478)
#### Saturday 2023-07-08 11:49:13 by bors

Auto merge of #112320 - compiler-errors:do-not-impl-via-obj, r=lcnr

Add `implement_via_object` to `rustc_deny_explicit_impl` to control object candidate assembly

Some built-in traits are special, since they are used to prove facts about the program that are important for later phases of compilation such as codegen and CTFE. For example, the `Unsize` trait is used to assert to the compiler that we are able to unsize a type into another type. It doesn't have any methods because it doesn't actually *instruct* the compiler how to do this unsizing, but this is later used (alongside an exhaustive match of combinations of unsizeable types) during codegen to generate unsize coercion code.

Due to this, these built-in traits are incompatible with the type erasure provided by object types. For example, the existence of `dyn Unsize<T>` does not mean that the compiler is able to unsize `Box<dyn Unsize<T>>` into `Box<T>`, since `Unsize` is a *witness* to the fact that a type can be unsized, and it doesn't actually encode that unsizing operation in its vtable as mentioned above.

The old trait solver gets around this fact by having complex control flow that never considers object bounds for certain built-in traits:
https://github.com/rust-lang/rust/blob/2f896da247e0ee8f0bef7cd7c54cfbea255b9f68/compiler/rustc_trait_selection/src/traits/select/candidate_assembly.rs#L61-L132

However, candidate assembly in the new solver is much more lovely, and I'd hate to add this list of opt-out cases into the new solver. Instead of maintaining this complex and hard-coded control flow, instead we can make this a property of the trait via a built-in attribute. We already have such a build attribute that's applied to every single trait that we care about: `rustc_deny_explicit_impl`. This PR adds `implement_via_object` as a meta-item to that attribute that allows us to opt a trait out of object-bound candidate assembly as well.

r? `@lcnr`

---
## [Dawnseer/tgstation](https://github.com/Dawnseer/tgstation)@[3fdd716da5...](https://github.com/Dawnseer/tgstation/commit/3fdd716da5bfd2aab2be37489b4ac39f4be7e632)
#### Saturday 2023-07-08 12:32:41 by Cheshify

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
## [Dawnseer/tgstation](https://github.com/Dawnseer/tgstation)@[43473a4dac...](https://github.com/Dawnseer/tgstation/commit/43473a4dac07c40faed45808b61b9c6de46ffcb6)
#### Saturday 2023-07-08 12:32:41 by san7890

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
## [status-im/status-mobile](https://github.com/status-im/status-mobile)@[9ed68ee7d1...](https://github.com/status-im/status-mobile/commit/9ed68ee7d1b7d59dd8b20c2ee1ffe43bd1c37078)
#### Saturday 2023-07-08 13:18:56 by Icaro Motta

Lint & fix some shadowed core Clojure(Script) vars (#16500)

It's well known that shadowing core Clojure vars can lead to unexpected bugs. In
fact, it's a common source of bugs in other languages too. In the status-mobile
repository there are, in total, 562 shadowed vars, ~500 are core vars. Excluding
the "old code" we still have 285 offenders.

In status-mobile I've already seen two bugs caused by shadowed vars, both with
the shadowed var "name". But probably other problems happened in the past, and
others will happen in the future if we don't do something about this. This PR is
also my response to my frustration trying to review PRs and checking for
shadowed vars, humans were not meant for that!

In this commit we are enabling ":shadowed-var" to lint certain (not all) core
vars as errors (not warnings). In future PRs we can gradually unshadow more
vars. For the record, name is shadowed 40 times in the new code and 130 in
total, and type is shadowed 93 times in the new code and 124 in total!

What about non-core vars, should we allow shadowing? There are ~70 non-core
shadowed vars. In my opinion, we should also lint and disallow shadowing
non-core vars, since it may cause the same kind of bugs of shadowing core vars.
But this decision can be left for another moment/issue, after we have fixed the
most prominent problem of shadowing core vars.

Which vars are unshadowed in this PR? I fixed 62 errors and unshadowed
cljs.core/iter, cljs.core/time, cljs.core/count, cljs.core/key,
clojure.core/key.

Resources:

- [clj-kondo linter: shadowed-var](https://github.com/clj-kondo/clj-kondo/blob/master/doc/linters.md#shadowed-var)

---
## [alexisBes/GMTK2023](https://github.com/alexisBes/GMTK2023)@[cb3c500afd...](https://github.com/alexisBes/GMTK2023/commit/cb3c500afd7b179533239e047681d0f86713d8ed)
#### Saturday 2023-07-08 13:31:28 by alexisBes

Merge pull request #14 from alexisBes/fuck_you_linus

Fuck you linus

---
## [Conga0/Apotheosis](https://github.com/Conga0/Apotheosis)@[6ec7df8a9c...](https://github.com/Conga0/Apotheosis/commit/6ec7df8a9c193b41e9a41bcab77ba701a29d10aa)
#### Saturday 2023-07-08 14:05:47 by Conga Lyne

New Creep, New Items, Bug Fixes

New Creep: Corrupt Master of Vulnerability
New Item: Corrupt Stone
New item: Guiding Stone
Removed tablet eater component from most corrupt masters, this is to save on performance, however, they are now immune to physics damage
Removed some outdated glyphs
Updated Fungal Shift (spell) sprites
Updated Trophy Room's statues
Updated Aquamine's projectile graphic
Updated Heretic
Optimised Sienenkivi
Fixed Blob Cavern not generating properly when approached from the east
Fixed Porings not releasing fairies properly
Fixed tentacle limbs occasionally deteching from their host body and flailing wildly
Fixed Plane Radar not being an emissive sprite
Fixed a SpawnFunction clash with Armageddon Machine
Fixed the Mountain Altar looking for 33 and 34 orbs for their respective endings instead of taking the new orb rooms into account, you now require 45 and 46 orbs respectively.
Fixed Sienenkivi not converting Infectious Blood

---
## [KacperX7/Programming-stuff](https://github.com/KacperX7/Programming-stuff)@[c94a83e632...](https://github.com/KacperX7/Programming-stuff/commit/c94a83e632f76b6218a24e9f6704bb4c2bece045)
#### Saturday 2023-07-08 14:08:41 by Kacper Kowalski

Add files via upload

I had a bit of fun with this code and I think the outcome of this is pretty good. As always I'm really curious about your opinion on my work and I hope you will like it, also I'm looking forward to getting more tips or ways of improving my programs. That's all from me I think, I hope you will have a great day cousin! As for me I going to need some break and therefore I'll stay the night at my parents allotment. I'm looking forward to hearing from you and seeeing you!

Bye, bye!

---
## [alexisBes/GMTK2023](https://github.com/alexisBes/GMTK2023)@[9c39699fd5...](https://github.com/alexisBes/GMTK2023/commit/9c39699fd5f42ceb746d1abf2eca3061362e271b)
#### Saturday 2023-07-08 15:01:53 by alexisBes

Merge pull request #17 from alexisBes/fuck_you_linus

Fuck you linus

---
## [Comxy/tgstation](https://github.com/Comxy/tgstation)@[d1fa50db47...](https://github.com/Comxy/tgstation/commit/d1fa50db47dd3d11e44e8ac074ee2850f00edf19)
#### Saturday 2023-07-08 15:16:50 by atlasle

New space ambient track (#76547)

## About The Pull Request

Adds a new space ambient track made by me to the game, supposed to be a
bit scarier than the others that were recently added as I feel that
they're a bit too happy (not to diss I really like them), also cleaned
up a bit of ambience.dm as the medical portion of it didn't follow the
same rules as the other ones. also also this will only be used for
tgstation so license wise I think this is CC BY-SA 3.0 but I'm not sure
so correct me if I'm wrong, also this is my first PR so yeah. Here's a
link to listen to the track https://voca.ro/18WvrGORDDdR

## Why It's Good For The Game

Variety is the spice of life.

## Changelog

:cl:
sound: A new ambient track will now play in space
/:cl:

---
## [Comxy/tgstation](https://github.com/Comxy/tgstation)@[48cc57010d...](https://github.com/Comxy/tgstation/commit/48cc57010d3ff01c55c53131b9399a4e71656d8d)
#### Saturday 2023-07-08 15:16:50 by Jacquerel

Various spider fixes (#76528)

## About The Pull Request

Fixes #76484
Then I noticed some weird stuff which slipped through the PR and poked
at that too.

- Spiderlings and Spiders once more have names ending in (###)
- Removed an unused property on Spiderlings.
- Rewrote the descriptions for a bunch of web-abilities and web-objects
to be clearer and have better capitalisation.
- Refactored the "Web Carcass" ability to not extend from "lay web" as
it didn't need to perform most of that behaviour.
- Also I renamed it and made the description give you a hint about why
you would want to instantly spawn a statue.
- The web effigy now despawns at the same rate as the ability cools down
so you're not dumping spider statues all over the place.
- I made spiderlings move at about the same speed as humans except if
they're on webs in which case they're still pretty fast.

To be honest I am not certain an instant statue spawning button is great
to begin with and I didn't even know it was added to the game but I am
not interested in messing much with the balance for now.

This made me look at spiderlings enough that I'm going to try and make a
new sprite for them that isn't awful.

## Why It's Good For The Game

Lets you differentiate individual spiders a little bit.
Makes usage of abilities clearer.

## Changelog

:cl:
balance: Guard spider web statues despawn as the ability comes back off
cooldown.
balance: Spiderlings now only move at light speed if they're on webs,
stay safe little guys.
fix: Spiders once again have random numbers after their names.
/:cl:

---
## [Blacklion567/Little-Projects-HTML-CSS-JS](https://github.com/Blacklion567/Little-Projects-HTML-CSS-JS)@[763e81c735...](https://github.com/Blacklion567/Little-Projects-HTML-CSS-JS/commit/763e81c735c695280020e5c336cdc73cc2a15dbe)
#### Saturday 2023-07-08 16:19:52 by Blacklion567

Little-Projects-HTML-CSS-JS

“If I could leave my audience with only one single key takeaway message, what would it be? If my audience was to forget everything else I said, what one single idea or lesson would I want them to remember?” – Akash Karia
“Dialogue is more powerful than narration. It puts audience members into the scene, allowing them to hear exactly what was said.” Akash Karia
“We all will experience pain, struggle, and trauma; suffering is a choice to cling and remain attached to the story.” - Michael Margolis
“Your greatest achievement will always be your life’s story.” – Michael Margolis
“If you’re not telling your story, somebody is telling it for you.” – Michael Margolis

---
## [Jayant7579/Codeclause](https://github.com/Jayant7579/Codeclause)@[c1efd7d063...](https://github.com/Jayant7579/Codeclause/commit/c1efd7d063260438afecc799537e825fbdc1a04d)
#### Saturday 2023-07-08 16:29:01 by Jayant Chauhan

Add files via upload

Welcome to the Music Player program, an intuitive and feature-rich application designed to enhance your music listening experience. This program provides a seamless platform for managing, organizing, and enjoying your favorite music collection right from your computer.

With the Music Player program, you can effortlessly import and categorize your music library, creating personalized playlists and organizing your tracks based on genres, artists, albums, or any custom criteria you prefer. The user-friendly interface allows you to easily navigate through your music collection, search for specific songs or artists, and browse album artwork for a visually appealing experience.

---
## [Nimowa/tgstation](https://github.com/Nimowa/tgstation)@[64eae49042...](https://github.com/Nimowa/tgstation/commit/64eae49042dea956b46ae013a0c96a891c026a7f)
#### Saturday 2023-07-08 17:14:25 by necromanceranne

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[635e923bcd...](https://github.com/treckstar/yolo-octo-hipster/commit/635e923bcd63f84d1ec764f5d33f139a02648832)
#### Saturday 2023-07-08 17:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [feldera/dbsp](https://github.com/feldera/dbsp)@[59132364cb...](https://github.com/feldera/dbsp/commit/59132364cb27d22b158776b09864221b938ff3e2)
#### Saturday 2023-07-08 17:50:02 by Gerd Zellweger

Add ability to checkpoint/version a pipeline. (#296)

This change allows to query the running configuration of a pipeline. And we also allow to update the running configuration of a pipeline explicitly. So all the normal interactions with connectors, pipelines, and program objects act as a staging area which can be committed using the API to the running version of the pipeline.

This change has several components:

## Database

This is pretty straight forward: We add history tables for pipeline, program, attached_connectors, and connectors. The history table contains the same fields as the
non-history counter-parts but we add a revision field and change the primary keys to be uuid+revision in those tables.

The history tables are immutable snapshots of the pipeline config. You see where this is going, whenever we need to commit a config. We go off and copy the pipeline row, the program row, all attached_connector and connector rows associated with the pipeline we want to version into the history table. We assign them a new
revision for every version. And we're almost done with versioning stuff. Kind of...

## Compiler

Now we have all these versions, and each version has a different binary, so we need to keep the binaries around. That's a bit unfortunate, but this will go away again once we have JIT. It also is kinda dumb because we don't want to keep binaries for all versions we ever created. So here is what we do:
Whenever we create a new program binary we version it in a (new) binaries folder (in the dbsp workspace) using a naming schema that is project_$uuid_$version. The reason we version immediately and not say at commit time of a pipeline is because the binary we used so far was just the binary directly from the target dir of that project. But we don't really know what state this binary is in, especially if we can have commit and compile requests happening at the same
time. So in the same 'transaction' that builds the binary we version it and copy it away. And the pipeline manager only runs versioned binaries. We also need a way to clean up binaries. That's also a bit silly because when is it safe to delete a version of a binary? Well, it's only safe if no pipeline has that program version as it's current, last revision. And no pipeline descriptor that we haven't versioned yet has that program/version as it's current program/version. The way we deal with this is to have a GC task that periodically wakes up and checks if binaries are orphans and can be removed. The first design I tried was trying to do this on-the-fly while we create new commits
but it seemed better in the end to handle this in a separate task as interacting with files can fail in all kinds of weird ways and shouldn't block anyone from creating a new version.
REST API

This one is pretty simple. We commit whenever the pipeline is deployed. And we allow to query the last committed/deployed pipeline. Finally, we also added a way to get the pipeline descriptor (not a committed version) in toml format. This is helpful to display a diff in the UI/APIs to see what has changed. And a way to validate a pipeline config + sql combination (e.g., don't deploy but return the errors that deploy would return if it found any inconsistencies).

## Other code changes

As you can see in the code, I added this PipelineRevision struct. That's essentially all state a user will be committing. If you look closely you can also see that we it harder for the user to version some garbage pipeline that would never run in the first place. For example, make sure that whatever we reference in the config references some actual tables and views along with a bunch of other conditions that need to be satisfied for the commit to succeed.
This change also meant that we have to use actual types for the database DDL that we get back from the compiler instead of just a string.

Signed-off-by: Gerd Zellweger <mail@gerdzellweger.com>

---
## [pexel5/tgstation](https://github.com/pexel5/tgstation)@[8af20d1577...](https://github.com/pexel5/tgstation/commit/8af20d157738044cef2fc00846caa1869d56a087)
#### Saturday 2023-07-08 18:00:35 by necromanceranne

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
## [ExactExampl/kernel_bonito-4.9](https://github.com/ExactExampl/kernel_bonito-4.9)@[188aed1e7f...](https://github.com/ExactExampl/kernel_bonito-4.9/commit/188aed1e7f58d45dcacf74d81d36189b8d51462b)
#### Saturday 2023-07-08 18:30:22 by Angelo G. Del Regno

Merge: Performance improvements.

This patchset brings some performance improvements and the addition of the LZO-RLE
algorithm to the kernel, also usable in zram (yup, tested, works but LZ4 is still ok for us).

The main performance improvement is for SWAP space: the locking has changed and
the swap cache is now split in 64MB trunks.
This gives us a reduction of the median page fault latency of 375%, from 15uS to 4uS,
and an improvement of 192% on the swap throughput (this includes "virtual" swap
devices, like zRAM!). The real world user experience improvement of this on a mobile
device is seen after a day or two of usage, where it usually starts losing just a little
performance due to the large amount of apps kept open in background: now I cannot
notice any more performance loss and the user experience is now basically the same as
if the phone was in its first 2 hours of boot life.

Other performance improvements include, in short:

    Userspace applications will be faster when checking running time of threads
    2-5% improvements on heavy multipliers (yeah, not a lot, but was totally free...)
    Improvements on rare conditions during sparsetruncate of about 0.3% to a
    way more rare around 20% improvement (that's never gonna happen, but there
    is no performance drop anywhere).

Tested on SoMC Tama Akatsuki RoW

This was taken from
Repo:
https://github.com/sonyxperiadev/kernel
PR: 2039 ([2.3.2.r1.4] Performance improvements)

[ExactExampl]: drop net socket and udp related changes

---
## [gregoorr/android_kernel_lge_sdm845](https://github.com/gregoorr/android_kernel_lge_sdm845)@[e657624aa7...](https://github.com/gregoorr/android_kernel_lge_sdm845/commit/e657624aa773f3ba3ff5d76ca14d95a4bc528eb6)
#### Saturday 2023-07-08 19:51:27 by Angelo G. Del Regno

Merge: Performance improvements.

This patchset brings some performance improvements and the addition of the LZO-RLE
algorithm to the kernel, also usable in zram (yup, tested, works but LZ4 is still ok for us).

The main performance improvement is for SWAP space: the locking has changed and
the swap cache is now split in 64MB trunks.
This gives us a reduction of the median page fault latency of 375%, from 15uS to 4uS,
and an improvement of 192% on the swap throughput (this includes "virtual" swap
devices, like zRAM!). The real world user experience improvement of this on a mobile
device is seen after a day or two of usage, where it usually starts losing just a little
performance due to the large amount of apps kept open in background: now I cannot
notice any more performance loss and the user experience is now basically the same as
if the phone was in its first 2 hours of boot life.

Other performance improvements include, in short:

    UDP v4/v6: 10% more performance on single RX queue
    Userspace applications will be faster when checking running time of threads
    2-5% improvements on heavy multipliers (yeah, not a lot, but was totally free...)
    Improvements on rare conditions during sparsetruncate of about 0.3% to a
    way more rare around 20% improvement (that's never gonna happen, but there
    is no performance drop anywhere).

Tested on SoMC Tama Akatsuki RoW

This was taken from
Repo:
https://github.com/sonyxperiadev/kernel
PR: 2039 ([2.3.2.r1.4] Performance improvements)

---
## [struts681/wisdom_sensor_net](https://github.com/struts681/wisdom_sensor_net)@[80819cffd6...](https://github.com/struts681/wisdom_sensor_net/commit/80819cffd68f8807cbb5b9d06ccf7ceff7f5ef9c)
#### Saturday 2023-07-08 19:57:55 by emo

Finish driver/RUDP refactor

I cleaned up a few things about the two interfaces that bothered
me. Mostly aesthetic things, but also some simple changes like
boolean return values from most functions with I feel makes the main
interface easier to use.

Now and of the Rfm69 library functions which can fail return a boolean.
Success = True
Failure = False
But Evan, what happened to the more specific return values that gave
at least a little insight into what the fuck happened? I'm glad you
asked! Now the Rfm69 state object will log its last return value
so you can read it after the function has returned. This whole change
allows us to use library functions as boolean expressions:

if (!Rfm69_init(...)) FREAK_OUT();

Then, if we need more info, we can access the return value at:

rfm->return_status;

I have also seperated the initialization logic and the allocation logic
to prevent having to pass a Rfm69 ** to the init function. Now you call
Rfm69_create() first which returns an allocated Rfm69 *. The init
function(s) now take simply a Rfm69 * now.

Beyond this I also cleaned up the Tx/Rx logic a bit, and combined the
two report structs into one universal report type called TrxReport
which can be passed to either the transmit or receive rudp functions.
Something about the two only slightly different structs bothered me
and this feels cleaner. As stated in the interface, a NULL can be passed
insted of a TrxReport pointer as internally the rudp functions check
for a valid pointer before manipulating the report variable. This adds
a tiny bit of extra logic which I have managed to resist
micro-optimizing away. I also resisted over abstracting the rudp
interface into bullshit and kept with the "trust the user of the
library" philosophy I have employed thus far. I think it makes the
code more explicit and expressive.

---
## [sherm1/drake](https://github.com/sherm1/drake)@[f90899e13f...](https://github.com/sherm1/drake/commit/f90899e13fd6b703ac5c7da3d1b7c0584a793769)
#### Saturday 2023-07-08 22:19:28 by Jeremy Nimmer

[geometry] Add Meshcat::GetRealtimeRate (#19700)

Tidy up recent Meshcat changes:
- Add missing pydrake bindings.
- Strongly prefer testing the public API (eschew test-friendship hacks).
  We want to guard against regressions in the end-user experience;
  using private API goes against that goal.
- Fix indentation, typos, and eschew abbreviation.

---
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[6e288185bc...](https://github.com/jlsnow301/tgstation/commit/6e288185bcc4bb3c55a8588369409fcc4e6f2cbf)
#### Saturday 2023-07-08 22:35:27 by Jacquerel

Cuter spiderlings (#76532)

## About The Pull Request

I hate looking at spiderlings. Mostly because they're an extremely fast
mob with no directional sprites or animations, so they appear to be a
rapid floating overlay.
I made some new ones. I don't know if they're objectively better but _I_
like them more.

Before:

![image](https://github.com/tgstation/tgstation/assets/7483112/ef561c4f-6d34-4ed2-a486-cd42f06f5648)

After:

![image](https://github.com/tgstation/tgstation/assets/7483112/7c073166-a956-4f7f-8dac-21d1a0f0a868)

Unlike the old sprites they also have directional states and movement
animations so you can scurry around really fast without being a static
image (maybe they shouldn't be so fast? A question for another PR).
I spent like 30 minutes looking at GAGs and then realised not only would
the colours be a pain in the ass but it doesn't support movement states
anyway.

Additionally I made the "dead spiderling" item inherit the dead
spiderling icon state from that spiderling instead of always being the
generic one.

Oh also I think a typo made baby tarantulas completely invisible.

## Why It's Good For The Game

I hate looking at spiderlings.

## Changelog

:cl:
image: New directional sprites for spiderlings, with movement
animations.
fix: Dead spiderlings will be the same colour as they were when they
were alive.
fix: Tarantula spiderlings are no longer invisible,
/:cl:

---
## [badgeteam/badgePython](https://github.com/badgeteam/badgePython)@[9ec21fb43d...](https://github.com/badgeteam/badgePython/commit/9ec21fb43d1a393bbb423c662678724177152503)
#### Saturday 2023-07-08 22:54:44 by Brian 'redbeard' Harrington

mpy/QSTR: Make nvs & rtcmem USER_C_MODULES

This affects the following components:
- RTC memory driver
- NVS driver
- Micropython module for NVS
- Micropython module for RTC memory
- Micropython module for external modules

It looks like previously most of the badgePython C code for interfacing
with Python were implemented as "extmod"s in MicroPython.  From a
maintenance perspective MicroPython intends an "extmod" to live within
the MicroPython codebase, but be something which affects multiple
ports... for example the use of mbedTLS or TinyUSB.

To clarify the relationship between badgePython and MicroPython, lets
review part of the MicroPython documentation: [Implementing a
Module][1]:

> This chapter details how to implement a core module in MicroPython.
> MicroPython modules can be one of the following:
>
> -   Built-in module: A general module that is be part of the MicroPython
>     repository.
> -   User module: A module that is useful for your specific project that
>     you maintain in your own repository or private codebase.
> -   Dynamic module: A module that can be deployed and imported at
>     runtime to your device.
>
> A module in MicroPython can be implemented in one of the following
> locations:
>
> -   py/: A core library that mirrors core CPython functionality.
> -   extmod/: A CPython or MicroPython-specific module that is shared
>     across multiple ports.
> -   ports/<port>/: A port-specific module.

Clearly a "User module" is the most appropriate term for what we are
trying to implment.  This commit migrates `nvs` and `driver_rtcmem` to
be "User modules" and moves them into the `components` directory.

To understand what this sort of change entails, let's review the
MicroPython documentation for "Extending MicroPython in C", specifically
"[Compiling the cmodule into MicroPython][2]".

In my opinion the MicroPython documentation fails to drive a very
important point home:

`USER_C_MODULES` mechanism implemented in MicroPython expects to receive
a CMake script which then uses `include()` to enumerate all of the project
modules as CMake scripts (as a specific path) or CMake modules (found via
searching for the module in the locations specified in the
`CMAKE_MODULE_PATH` CMake variable).  This is why this commit adds the
file `components/external_micropy_modules.cmake`.  It allows the end
user to specify the modules that the specifically wish to import into
the MicroPython firmware.

In the long run, this will be improved to support the `BOARDS` mechanism
allowing for easy driver selection, integrated in with Kconfig.

Next, for each of our drivers we add a CMake script which will allow
MicroPython to execute the QSTR macro generation process.  If you find
yourself troubleshooting missing definitions of `MP_QSTR_` macros, this
is the file to look at.  I'm using a convention of calling the file
`micropy_module.cmake` to distinguish it from the CMake script which
will be used to build the module.

The `micropy_module.cmake` file is a CMake script which defines the
following:

- The components source code as a target of type `INTERFACE`
- The components source directory as an include location of type
  `INTERFACE`
- That this is component should be attached to the `usermod` target as
  an `INTERFACE`.

This is pretty much a rote implementation of the example provided in
the [documentation][2] under "Structure of an external C module".
Towards the end of this section CMake based implementations are
discussed.

[1]: https://docs.micropython.org/en/v1.20.0/develop/library.html
[2]: https://docs.micropython.org/en/v1.20.0/develop/cmodules.html#compiling-the-cmodule-into-micropython

---

