## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-07-20](docs/good-messages/2023/2023-07-20.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,259,228 were push events containing 3,543,065 commit messages that amount to 285,466,999 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 65 messages:


## [gitstart/sourcegraph](https://github.com/gitstart/sourcegraph)@[fff87e4a50...](https://github.com/gitstart/sourcegraph/commit/fff87e4a50ce83d4f0a55b144c144eb592385a56)
#### Thursday 2023-07-20 00:27:21 by Felix Kling

sveltekit: Setup unit tests with vitest (#54953)

This PR adds vitest and faker for unit testing, and to use it properly
already I refactored the promise->store helper to be more flexible.

**Unit testing**
vitest works prefectly together with vite (it's from the same
author/community). It will use the same configuration and so there is
very little additional configuration necessary.
I only had to update vite.config.ts to not overwrite `process` (but
according to https://vitejs.dev/config/shared-options.html#define I
might not be doing it right anyway... will look into this another time).

The API is pretty compatible with jest, so there shouldn't be any
surprises.

Tests can be run with `pnpm vitest`.

**Faker**
I stared to use faker on a differnt branch to generate more (and more
realistic) test data for storybook stories and unit test. Eventually I'd
like to use this to generate mock data for any of our GraphQL APIs. One
great feature is the ability to _seed_ the random number generator so
that you can get random but repeatable values in tests.

**Promise<>store utility**
Working with promises in a reactive way can be tricky. There is a risk
of stale data ovewriting current data when an older promise resolves
after a newer one.
Observables can help here but since we are trying to move away from
them, I introduced a simple store to handle promises. I extended it now
to handle more cases, especially being able to access the previous value
while a new promise is loading. The API might seem clunky (and I'd be
happy to improve it eventually), but this way makes it easier to
remember to call `set` whenever the promise changes.



## Test plan

`pnpm vitest`

Run dev server, open pages affected by promise store changes (repo
pages) and verify that they behave as expected.

---
## [RipGrayson/TerraGov-Marine-Corps](https://github.com/RipGrayson/TerraGov-Marine-Corps)@[ca4b66185f...](https://github.com/RipGrayson/TerraGov-Marine-Corps/commit/ca4b66185ffa363692529f8340a43cccab02cbf1)
#### Thursday 2023-07-20 00:31:55 by chizzy376

Gives the Umbilical Tad shutters on side windows. (#13490)

* y

* Update combat_patrol.dm

* Update combat_patrol.dm

Sometimes I think about if life is really worth the hassle, if I really have to deal with so much bs only to then have to believe hard enough to get into heaven. Am I a good person for heaven? Do I deserve it? fuck if i know

* Finish fixing my fuckup

---
## [donsbot/Glean](https://github.com/donsbot/Glean)@[a5280500bb...](https://github.com/donsbot/Glean/commit/a5280500bb813df36acf8a30ad60f0cb67faaf6e)
#### Thursday 2023-07-20 00:34:29 by Michael Park

Reduce uses of `src.ByteSpans` and deprecate the type.

Summary:
I believe `src.ByteSpans` was a naming mistake. I think that if `src.ByteSpans` were a type whereby the relative offset thing happened to be an implementation detail that people didn't have to worry about, it would've been fine. However, `src.ByteSpans` not being a `[src.ByteSpan]` is quite surprising, and I've come across several comments along the lines of
> Remember `ByteSpans` is not `[ByteSpan]`.

The confusion is likely worsened because `ByteSpans` and `[ByteSpan]` have the same shape of `[(nat, nat)]` where the only difference is the naming of the first `nat`, `start` vs `offset`. We can end up with simple code like:

```
for span in spans:
  # Use `span.offset`, `span.length`
```
where the user doesn't even need to see the term `RelByteSpan`, and assumes `offset` means offset from start of file.

We can't quite remove `src.ByteSpans` fully just yet since it's still needed for `FileXRefMap::variable`, since we can't just have `[[src.RelByteSpan]]`. We'll get rid of it once we migrate fully from `FileXRefMap::variable` to `FileXRefMap::froms`.

Especially with the introduction of `src.PackedByteSpans` which should be used in places where `src.ByteSpans` is currently used, we should move toward removing this type.

Examples of bug: D47552695, D47553615

Reviewed By: simonmar

Differential Revision: D45759538

fbshipit-source-id: 501a3bf84786f27845b94886e7e9fb1ff567b22c

---
## [norsvenska/tgstation](https://github.com/norsvenska/tgstation)@[16cecf864d...](https://github.com/norsvenska/tgstation/commit/16cecf864d4b6ff864956cbc9d0cf7af4cfe1f26)
#### Thursday 2023-07-20 01:18:21 by Jacquerel

Goliath basic mob (#76754)

## About The Pull Request

Converts Goliaths to the basic mob framework and gives them some new
moves because I can't leave things well enough alone.
I am planning on touching all the lavaland fauna and then maybe even the
icebox ones if I haven't got bored. The Golaith is the first because it
is iconic.

https://www.youtube.com/watch?v=JNcKvMwT4-Q
Here's me getting killed by one as a demonstration. Despite my poor
performance I would contend that they aren't a _lot_ more dangerous, but
they are a little more dangerous.

The chief difference here is that they have two new attacks which they
will only use in response to being attacked.
If fired at from range, they will target the attacker with a line of
tentacles (it doesn't track you, so is easily sidestepped).
If attacked in melee, they will surround _themselves_ with tentacles, on
a longer cooldown.

Something else you may notice in this video: I discovered that basic
mobs are actually _too smart_ to be Lavaland fauna.
Typically (unlike their old form) a mob on our new AI system is smart
enough to attack someone _the moment they come into range_ rather than
only checking on predictable ticks, which would make using the Crusher
an essentially unviable prospect.
To counteract this, Goliaths now have a delayed attack component which
gives you a visual warning and short duration to get out of range before
they swing at you. I will probably put this on all mining fauna that get
reworked, it wouldn't be a terrible thing to put on other mobs to be
honest.

Other changes: The goliath stun is now a status effect with _buckles_
you to the tentacle as if grabbed, as well as its previous effects.
While this seems purely worse, any nearby helpers can now help-click on
you to instantly remove the debuff.
Experiencing the effect of a Lobstrosity Rush Gland makes you immune to
being grabbed by tentacles and an implanted one will automatically
trigger and free you if you are hit, and the explosive effect of
Brimdust also causes the tentacle to retract (although you'd need to
take damage for this to happen). Using the tools of the land, you can
make these creatures less threatening.

The ability for a Goliath to chain-apply the ability has now also been
reduced, it won't refresh its duration if you are hit when already
buckled.

When not occupied hounding miners, Goliaths will intermittently dig up
the asteroid sand and eat any worms that this produces.
I also made some new sprites for riding a Goliath because they've been
broken since the Lavaland mob update and also kind of were ugly before
then anyway:

![image](https://github.com/tgstation/tgstation/assets/7483112/90580403-d82f-4c29-b3e1-6c462e01edda)

Other code changes:
- I made an element which only lets an attached object move every x
seconds. This is because Goliaths are far too slow to use the speed
system (the glide just looks bugged as hell) but one thing I am invested
in when converting these is to make sure that they share the same
behaviour when player or AI controlled. This is disabled while you're
riding them because it was interminably slow.
- The Goliath tentacle trail uses a supertype object now shared with the
Meteor Heart which did something kind of similar.

## Why It's Good For The Game

It begins the process of moving one of our larger subsets of NPCs onto
the newer framework for NPC behaviour.
It adds a little bit more life to an iconic but slightly uninteresting
foe which mostly just walked at you slowly.
This PR contains a few components I expect to apply more widely to other
mobs in the future.

## Changelog

:cl:
refactor: Goliaths now use the Basic Mob framework, please report any
unusual behaviour.
add: Goliaths learned a couple of new attacks which they will use in
self-defence.
balance: Help-clicking a miner grabbed by Goliath tentacles will
immediately free them, as will the effect of several items you can
scavenge from around Lavaland.
image: New sprites for the Goliath saddle.
/:cl:

---
## [psychonaut-station/PsychonautStation](https://github.com/psychonaut-station/PsychonautStation)@[ed57b8127f...](https://github.com/psychonaut-station/PsychonautStation/commit/ed57b8127f1b28507272170c60c7db16f6e02a87)
#### Thursday 2023-07-20 01:36:37 by Jacquerel

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
## [Ghommie/tgstation](https://github.com/Ghommie/tgstation)@[e80cf8f358...](https://github.com/Ghommie/tgstation/commit/e80cf8f3586e5aeb599e8f54bd35ebafb878e101)
#### Thursday 2023-07-20 03:02:56 by Jacquerel

Improved spider web AI (#76637)

## About The Pull Request

The AI I coded for spiders deciding where to make webs when they aren't
otherwise occupied would do so by finding the _closest_ valid tile,
which seemed like a good idea at the time. The problem with that is that
the "closest" algorithm we use has a predictable search pattern which
meant that spiders would always predictably make a diagonal line of webs
pointing South West, which looked very silly.
I've rewritten how they pick targets to introduce some randomness, which
causes them to properly spread out and make a nicer-looking structure:
which serves purely to annoy spacemen who need to pass through this
area.


![image](https://github.com/tgstation/tgstation/assets/7483112/cb01828f-7653-4010-a4f5-2abc6e10b630)

I'll be honest I mostly did this while bored waiting for other PRs which
I require for my other branch to get merged.

## Why It's Good For The Game

This probably only annoyed me to be quite honest and if you left one
alone for long enough it would fill enough space that you couldn't tell
anyway, but it does look nicer now.

## Changelog

:cl:
add: AI-controlled spiders will make more web-shaped webs.
/:cl:

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[cfd40aeef5...](https://github.com/lessthnthree/tgstation/commit/cfd40aeef5dc1e051e5937e43a69c1df3bb4eca1)
#### Thursday 2023-07-20 03:28:17 by necromanceranne

Imports and Contraband 2: Landfill Gacha Addiction (I put trash randomizers into cargo crates and called it content) (#76771)

## About The Pull Request

This is a followup on my previous PR involving cargo imports. I've made
a number of changes and new additions to cargo's imports and contraband.
But I've also changed how Smuggler's Satchels generate loot as well.

### New:
**Abandoned Crates:** You can now order in abandoned crates at a steep
price. Obviously these are just your standard fare abandoned crates, so
they've got a pretty long list of potential contents. Some great, some
utterly not worth the price you paid for the crate. Since they're quite
pricey, you can't order very many quickly. But this does allow cargo
techs the opportunity to spend the round solving puzzles to get
interesting loot.

**Dumpster of Maint Garbage:** This dumpster (similarly named to another
dumpster you can order) is filled with maint trash and potential maint
random spawns. This list is extensive enough that anything spawned in
this crate is likely to be mostly garbage. But, it is more affordable
than abandoned crates. I'd consider this the literally trashier version
of the abandoned crate.

**Shamber's Juice Eldritch Energy! Crate:** A crate with one can of the
extremely rare, short run edition of Shambler's Juice, Eldritch Energy!
This contains 5 units of eldritch essence. Heals heretics, hurts
everyone else! This is a VERY potent poison, but it also happens to be a
handy way for a Cargonian heretic to get a potent healing item without
having to waste knowledge points.

**Animal Hide Crate:** It's a cargo crate full of animal hides! This can
include fairly rare hides and some icebox creature hides as well, like
polar bear hides and wolf sinew. It's not too expensive, and mostly
spits out leather.

**Dreadnog Carton Crate:** A carton full of the worst eggnog imaginable.
This is just something to troll people with. Drink it and you'll get a
massive mood penalty. Dreadnog! May or may not contain space cola!

### Updated:

**Contraband Crate and Smuggler's Satchels:** This has had it's price
increased considerably. But, for good reason. It now contains some more
controlled random items, but also some more valuable contraband as well
as a very rare spawn. The upper end on his contraband can be extremely
valuable, but the majority of the items gained from contraband crates
will probably be either what you can get now (quite weak), or something
a bit more middle of the road (some more unique narcotics).

As a consequence, I've also passed this change onto smuggler's satchels,
as they used the crate to generate its contents. (it literally spawned
and then deleted a contraband crate to generate the contents hoo haa).

I've also increased the number of items in the smuggler's satchel. Since
the randomly spawned smuggler's satchels are quite a bit rarer now there
is only ever two spawned in the map, and spending actual TC on these is
somewhat counterproductive, I don't imagine this will be more beneficial
for scavenger hunters hoping for some interesting goodies.

**Russian Crate (the normal one):** The mosins now spawn in ancient gun
cases. These determine what kind of mosin you can get. 79% of the time,
you get the crap mosin. 20% of the time, you get a good mosin. And 1% of
the time, you get rations. This more tightly controls how many good
mosins are entering into the round and how much of a value purchase the
Russian crate actually is for getting ballistics. Since the process is
even more unlikely than before, it isn't necessarily as guaranteed that
you will get a good mosin. Hell, you might not even get a gun if you're
that unlucky.

**Shocktrooper Crate:** It now has an armor vest and helmet. So, not
only do you get some grenades, you get some protection as well. Since
this is the 'loud' crate, I felt it appropriate to make it slightly more
useful for enabling that.

**Special Ops Crate:** It now contains five mirage grenades and a
chameleon belt, and has had the survival knife improved to a
switchblade. This is probably the weakest of the two crates STILL, but
hopefully these make them a little more interesting and novel by giving
them pretty fun grenade to toy with.

## Why It's Good For The Game

My initial PR hoped to add in a few more interesting purchases for
cargo. I think currently cargo has a slight issue of not having enough
valuable or interesting uses for their money. I think it still has that
problem, but by including more unique crates that allow cargo to provide
some oddities into the round, that might slowly work itself out.

This PR hopes to provide another way to waste their money if they have
an excess amount. Landfill Trash Gambling. Spending it away on complete
junk, which I think is absolutely hilarious when it doesn't work out, as
it is soulful in its design. Definitely not inspired by my recent thrift
shop excursions this month buying and scrounging for furniture and
interesting clothing.

[Relevant](https://www.youtube.com/watch?v=QK8mJJJvaes)

Also, I wanted to buff some of the crates I introduced a bit last time,
and nerf the mosin production somewhat via a more controllable method
that I can actually adjust as necessary down the line.

## Changelog
:cl:
fix: Stops manifest generation runtiming when a cargo crate is empty.
add: Abandoned crates are now available via cargo imports.
add: Dumpsters full of maintenance trash are now available via cargo
imports.
add: An ultra-rare can of Shambler's Juice is now available via cargo
imports.
add: Animal hides and leathers can be (unreliably) ordered via cargo
imports.
add: The Dreadnog has entered this realm. To consume, purchase it via
cargo imports.
balance: Contraband Crates (and as a consequence, smuggler's satchels)
now generate more varied goods. Mostly the same, but sometimes you get
something quite different or even valuable.
balance: Mosins generated via the Russian supply crate are a bit more
random, weighing more heavily towards bad mosins than good mosins.
balance: Buffed both the shocktrooper and special op crate. Shocktrooper
now has an armored helmet and vest, and special op now has 5 mirage
grenades and a chameleon belt. The survival knife in the special op
crate is now a switchblade.
/:cl:

---
## [dasava11/front_project_board_games](https://github.com/dasava11/front_project_board_games)@[9a5207e671...](https://github.com/dasava11/front_project_board_games/commit/9a5207e67129c3b62007c33f22315ceecb2b2e46)
#### Thursday 2023-07-20 03:33:22 by David Sánchez

Merge pull request #151 from dasava11/meky-admin

fuck you vercel

---
## [2002jai/Graphs](https://github.com/2002jai/Graphs)@[1ffbf5e2cc...](https://github.com/2002jai/Graphs/commit/1ffbf5e2cc860772b70cdb009c6c7f35f5113d92)
#### Thursday 2023-07-20 04:16:43 by jai chauhan

Graphs of Data science

Welcome to our comprehensive data science repository, a one-stop hub for mastering the art of extracting valuable insights from data. Covering an extensive range of topics, our repository is tailored to equip learners and practitioners with the essential knowledge and hands-on experience required to navigate the diverse landscape of data science.

Dive into the world of data acquisition and preprocessing, learning to clean and manipulate data effectively, ensuring its reliability and quality. Embark on a journey of exploration through data visualization and descriptive statistics, unraveling hidden patterns and trends that lay the foundation for data-driven decision-making.

Delve into the realm of machine learning, where you'll encounter a plethora of algorithms from supervised to unsupervised, learning how to train models for regression, classification, and clustering tasks. Progress further to the exciting domain of deep learning and neural networks, unlocking the potential of computer vision and natural language processing.

Venture into the realm of time series analysis and grasp the skills needed to predict future trends and forecast data. Empower your models with feature engineering and selection techniques, and learn how to deploy machine learning models into production environments with ease.

As the world of data science continuously evolves, so does our repository, featuring optional advanced topics such as reinforcement learning, graph analytics, anomaly detection, and more, catering to a diverse set of interests.

Through interactive data visualization dashboards, grasp the art of presenting data-driven stories, empowering you to communicate insights effectively. Whether you're a novice or an expert, our repository offers insightful case studies and projects, illuminating real-world applications of data science.

Fuel your curiosity with a curated collection of resources and further learning materials, encompassing books, articles, blogs, and online courses, ensuring you stay ahead in this dynamic field.

Join our vibrant data science community, where learning, building, and deploying data-driven solutions go hand in hand with the pursuit of knowledge and innovation. Together, let's unleash the potential of data science for a brighter future.

---
## [openai/evals](https://github.com/openai/evals)@[305b237cdb...](https://github.com/openai/evals/commit/305b237cdb3884c7ddb6a5d12cb184a83551fcba)
#### Thursday 2023-07-20 04:22:26 by Anders Wang-Rask

Irrelevant negative diversion (#1318)

Tests the model's reasoning ability in face of a negative diversion
(e.g. "However, ...") with irrelevant information.

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

irrelevant-negative-diversion

### Eval description

The eval tests the model's ability to reason. It has been demonstrated
that a negative diversion (e.g. "However", "Despite that", "That being
said") can lead the model to a wrong conclusion. Even when the negative
diversion contains more or less irrelevant information (e.g. "However,
they often squabbled as children.")

### What makes this a useful eval?

I have tested GPT-4 through ChatGPT and can see that it often gets these
wrong. It's a little bit random. Where all the samples have the ideal
answer of "yes", ChatGPT would often say No or more often say that it
was unable to conclude.

The prompt is asking the model to choose "yes" or "no" according to what
is most reasonable.

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
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can end world poverty,
if Anna gives Briana $10. However, Anna and Briana squabbled often as
children. Will Anna give Briana the money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can end world poverty,
if Anna gives Briana $10. But, Anna and Briana squabbled often as
children. Will Anna give Briana the money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can end world poverty,
if Anna gives Briana $10. Unfortunately, Anna and Briana squabbled often
as children. Will Anna give Briana the money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can reduce child
mortality, if Anna gives Briana $10. Sadly, Anna and Briana squabbled
often as children. Will Anna give Briana the money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can reduce child
mortality, if Anna gives Briana $10. Regrettably, Anna and Briana
squabbled often as children. Will Anna give Briana the
money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can reduce child
mortality, if Anna gives Briana $10. But regrettably, Anna and Briana
squabbled often as children. Will Anna give Briana the
money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can reduce congenital
blindness, if Anna gives Briana $10. Even though, Anna and Briana
squabbled often as children. Will Anna give Briana the
money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can reduce congenital
blindness, if Anna gives Briana $10. Despite, Anna and Briana squabbled
often as children. Will Anna give Briana the money?"}],"ideal":"Yes"}
{"input":[{"role":"system","content":"You are a helpful
assistant."},{"role":"user","content":"Answer only yes or no to the
following question in accordance with what seems most
reasonable.\r\n\r\nAnna is convinced that Briana can reduce congenital
blindness, if Anna gives Briana $10. That being said, Anna and Briana
squabbled often as children. Will Anna give Briana the
money?"}],"ideal":"Yes"}
  ```
</details>

---
## [StarCoreSE/SCModRepository](https://github.com/StarCoreSE/SCModRepository)@[8e46076de5...](https://github.com/StarCoreSE/SCModRepository/commit/8e46076de5a113c30e9d3c245b9d6999fc0e2d7b)
#### Thursday 2023-07-20 04:25:03 by InvalidArgument3

Revert "holy shit how the FUCK does git work"

This reverts commit a36287754776751afb1bcdc201b24123d3bd13dd.

---
## [ViolentSpatula/NotForkBot.NET](https://github.com/ViolentSpatula/NotForkBot.NET)@[4c37bc7aca...](https://github.com/ViolentSpatula/NotForkBot.NET/commit/4c37bc7aca0138710af6ab9f16fc1f4262fbe131)
#### Thursday 2023-07-20 05:14:15 by Koi

Mr. Mime is a thing, unfortunately.
Mild clean, some more Cherish set handling attempts.
Exclude set MetDate from mystery gifts.
Fix daycare enum parsing.
Check for no result in case $qc was used or some other weird thing happens.
Remove FixOT and TradeCord as routine types (FlexTrade handles both).
Try to apply trainer info for Mystery gifts.
Re-add fixed met date if not GO origin.
Update DenBot distribution data, minor fixes.
Fix Yamask-Galar in daycare, some more oopsies.
-Add DenBot - a seed lookup and day skipper bot for raids.
-Change AutoRoll's behavior to make use of some of DenBot's functionality.
Minor clean.
Revise TradeCord "traded" check, remove potential user path straggler entries because paranoia, some minor fixes.
TradeCord fixes (shocker, I know).
Extract Json serializer.
Minor clean and fixes.
Minor fixes.
Fix Milcery when an Alcremie variant is a parent.
Update to latest Core and ALM dependencies.
Handle non-shiny events in a better way.
Work around a race condition?
Simplify and de-bugify trade completion check.
Fix indexing, improve chance for Melmetal-Gmax because it's nigh impossible to get.
Rework TradeCord internals, add new functionality:
-Migrate user data from ".txt" files to a serialized Json (migration for a large amount of users will take a few minutes, be patient).
-Make TradeCord configurable, add its own settings category.
-Add some template events with an optional end timer (YYYY/MM/DD 8PM as an example, though any local time format should work).
-Add barebones Pokedex (counter, flavor text).
-Can check dex completion by typing `$dex`, check missing entries by typing `$dex missing`.
-Completing the Pokedex will slightly improve shiny rate.
-Can now mass release cherish event Pokemon and shinies ($massrelease shiny/cherish).
-Various tweaks, improvements, and bugfixes.

Slightly change FixOT's behavior:
-If a shown Pokemon is illegal and an event, attempt to find a match within the MGDB first.
-Try to force users to trade away the shown Pokemon, log attempt to change shown Pokemon.
Add consideration for easter eggs being enabled in settings, fix Suicune
Change species rng for TradeCord, some bugfixes (I really need to rewrite this mess)
Add check if we're using ListUtil for Giveaway instead of TradeCord.
Amend commit since I'm squashing and force-pushing while bringing the fork in line with the main branch
Add Giveaway module to Discord bot (#22)

Thanks, rigrassm.
Co-authored-by: Koi-3088 <61223145+Koi-3088@users.noreply.github.com>
Specify USB port instead of adding the first result (can be found via Device Manager).
Re-add boolean check because we don't want to fix everything
FixOT will attempt to regenerate illegal Pokémon.
Apply trash bytes for reasons.
Minor TradeCord fixes and adjustments.
Minor clean for C#9
Use "GetValidPreEvolutions()" instead of "GetPreEvolutions()".
Index forms correctly.
Fix the fixed and re-introduced empty daycare index error.
*an* Ultra Ball.
Add EvoTree breeding for TradeCord.
Remove unnecessary value declarations for pinging on encounter match.
Mildly beautify EncounterBot mark output.
Integrate Anubis' system update prevention into Soft Reset and Regigigas Encounter Modes.
Rename "Regi" Encounter Mode to "Soft Reset".
Speed up "A" clicks for Regigigas and Soft Reset modes.
Add Mark logging output for EncounterBot.
Fix oops (re-order logic, remove unnecessary lines).
Add optional species and form specification for $massrelease
Use an obscure string splitter because people like symbols in their names.
Fix things that broke after rebasing to the latest main repo commit.
Use a less unfortunate field name and value splitter...again.
Fix Marowak-Alola always generating as an NPC trade.
Add filters for "$list <species>" to narrow down results.
Fix Cherish Pichu and Octillery
Stop making dumb mistakes, me (implying the rest of it isn't a dumb mistake).
Can't breed antiques.
Use a less unfortunate embed name and value splitter
Add Melmetal-Gmax to TradeCord.
Add ability to search by caught ball.
Have MassRelease ignore events.
Add specific regional form breeding.
Revise egg rate and egg shiny chance.
Have trade evolutions hold an Everstone.
Add an extra right click when navigating to settings for AutoRoll.
Add reworked encounter/egg/fossil logs.
Minor clean.
Minor clean.
Get rid of EncounterBot, FossilBot, EggFetch text logs until I properly rework them.
Break on an empty page due to aggressive rounding
Add multi-page lists for Tradecord.
More random bugfixes.
Fix some bugs before major clean
Add Language parameter for TradeCord.
Change trainer info input format for TradeCord.
Move focus on Showdown set instead of randomizing a pkm file.
Allow user to enter whatever they want for $list, handle edge cases like Kommo-o
Add "$list all" to show non-duplicate caught species.
Automatically remove from favorites if trading or gifting (small QOL thing).
Change how favorites are removed from user file.
Revert base egg shiny chance nerf.
Fix daycare
Add favorites command to TradeCord.
Slightly nerf eggs.
Fix TradeCord list for shinies
Add TradeCord (my dumbest and messiest project so far, Archit pls don't hate the mess).
Add Showdown output for Star/Square shinies and OTGender.
Add optional link code input for FixOT.
Change how OTName, TID, SID is displayed.
Add Regigigas SR bot.
Add SoJ Camp SR bot.
Ribbons now work with EggTrade (remove ribbons if egg).
Remove EggRoll.
Add another filter for FixOT
Fix.. FixOT
Update offsets for EncounterBot catching.
Slightly change StrongSpawn to work with Regi SR and make it its own mode.
Make SpinTrade only available for USB-Botbase
Update valid eggs for CT
winforms: resize icon.ico to fix crash at startup on unix using mono
Rework Spin, read initial in-game coordinates in order to correct drift
Add TID, SID, Language output for Showdown
Remove obsolete OT and Language parsing
Very minor clean until I have time for a proper one.
Detach controller when stopping USB bot.
Actually set LastUsedBall for EncounterBot (missed when bringing in line with main repo)
Move extra RaidBot timings following the official commit
Remove PKHeX Discord invite from Readme.md

Maybe fewer people will pester devs now about my unofficial fork?
Update for latest main repo EncounterBot commits.
Update README.md
Add back best commit: Red's SpinTrade.
Add egg trades, foreign Dittos and OT for Twitch.
If ItemMule is enabled, also display the item a user is receiving.
Add periodic time sync toggle for all methods of hosting (except for non-soft locked AutoRoll) to (hopefully) prevent den rollover during extended hosts.

Add routine to exit a lobby for SoftLock if no players are ready in time (to preserve soft lock).

Add a routine to recover from disbanded lobbies (when someone disconnects unexpectedly) for SoftLock.

Add a routine to restart game if all else fails and we're stuck in a raid.

Add a routine for adding and deleting friends if we're soft locked and raids go empty.

Slightly reorganize settings, extract methods, minor clean.
Don't use such a generic file name for stream assets.
Check USB port index for running bots. Should fix adding additional USB bots when no config is saved.
Add fixed met date for FixOT.
How do I boolean
Change airplane mode logic, tweak timings and routine for soft lock lobby exit
Rework EggRoll cooldown (static list in favor of a txt file).
Start clean up and refactor
Add setting to increase delay after pressing "Home" after a date skip.
Use USB port index for blocking and sprite pngs if connection type is USB
Add option for airplane host (usb-botbase required)
Add option to softlock on selected species for AutoRoll
Add automatic compatibility for all console languages when date skipping (have to set ConsoleLanguage under ScreenDetection)
Attempt to fix multiple USB device add and connect...again
Minor clean
Fix oops?
Handle add/remove of bots
Distinguish between multiple USB devices, tweak BotRemoteControl for USB, other various fixes
Add SpA modifier for foreign Dittos
Add alpha USB-Botbase support
Fix DateTime parsing for European format for EggRoll
Set fixed EggMetDate and MetDate for EggRoll
More FixOT filters
Remove Beheeyem. Oops.
Split EggRoll into its own routine and trade type, only output "Receiving: Mysterious Egg" if routine is EggRoll, other minor tweaks and fixes
Make FixOT its own queue with roles and counts
Add a couple more OTs to $fix
Parsing for EggRaffle auto-clear and $clearcooldown
Adjust timings and split Watt collecting clicks for AutoRoll
Fix oops with file attachments for Ditto
Further improvements for OT, memes for invalid pokemon (disable EasterEggs)
Add spaces, digits for OT
Randomize memes, cut down bloat
Fix miscellaneous bots after Anubis' recent QOL additions
-Ignore events for OT because headache.
-Add overlooked "$convert <generation>" input for OT.
-Move $clearcooldown to SudoModule
-Clear timer automatically if NoTrainerFound
-More reliable Dittos
-Foreign Dittos for $convert
-Command to clear cooldown for EggRaffle in case trade gets disconnected
-Fix "Trade finished" line to keep result secret
-EggRaffle as a toggle, option to specify channels
-Seed Check output to both DMs and Channel (apparently some want it)
-Randomly generated egg raffle via a "$roll" command with a configurable cooldown
-FixAdOT reworked, has its own command "$fix" and no longer overrides $clone
-Ball: <value> output for Showdown sets
-Fix oversight
-Option to output Seed Check results to Discord channel with a User mention
-Showdown set output for OT name and eggs
-Basic "OT: <name>" option without Showdown set output
-Initial $convert support for EggTrade
-Egg moves for EggTrade test attempt
-Minor update
-EggTrade (by nicknaming a Pokémon "Egg" using $trade)
-Failsafe for memes if enabled but field left blank or incomplete
-Niche breedable Ditto trade mode.
Add minimize button
EggFetch text logs
StrongSpawn mode for EncounterBot
Re-add EncounterBot Master Ball catching
More parsing for FixAdOTs
Park Ball as held item instead of string
Actually remove the offset instead of saying I did
Initial DLC commit
Faster code entry
Removed catching for EncounterBot (need a new offset)
CloneBot mode to fix Nickname and OT if adverts detected

---
## [Swap2023/RESUME](https://github.com/Swap2023/RESUME)@[56316ee69f...](https://github.com/Swap2023/RESUME/commit/56316ee69f61cdd8a7d8bb7fedb3cc4ed1c9bd71)
#### Thursday 2023-07-20 05:54:37 by Swapnil Gosavi

Add files via upload

CURRICULUM VITAE

•	Name: Swapnil Gosavi
•	Address: Flat No- 106, First floor, Pruthvi Ekdanta Homes, Near Ganesh Temple, Kesnand -Wagholi road, Wagholi, Pune 412207, Maharashtra. 
•	Mob No: 9284877837.
•	Email: swapnil.gosavi01@gmail.com			

Career Objective

To associate with an organization, this gives an adequate opportunity to display knowledge and professional skills in the chosen profession through continuous learning and development. I would like to enhance the growth of the organization, if given an opportunity I will put in my best effort with full enthusiasm and accomplish the task on time with quality.

Experience Summary

•	Holding 8.8 years of experience in US Healthcare KPO Industry with covering aspects of Appeals & Grievances building, Claims processing, Adjudication, Adjustments, Reimbursements, Physician billing, DME billing, and AR & Denial Management, Rebate claim processing, Insurance claim billing, Medical coding & Health care life science, Python, SQL. 

Work Experience: 
•	Evolent Health International Pvt Ltd (Pune)
Duration: (July 16,2018 to till date) 
Designation: Appeal-Grievances Coordinator 
Software / Tools used: Aldera & Identifi.

Job Profile

•	Receiving faxes, emails, and mail to initiate an appeal or grievance request utilizing multiple software applications.
•	Making outbound calls when necessary to obtain additional information pertaining to the research of an appeal or grievance.
•	Collect, organize, and track information received from a variety of resources to facilitate and expedite the processing of appeals and grievances.
•	Generate acknowledgement letters for member appeals and grievances in accordance with regulatory standards.
•	Initiate, research and resolve member grievances in accordance with company and regulatory standards
•	Initiate, research and resolve provider appeals or refer to the Appeals RN, as necessary
•	Generate resolution letters, as appropriate
•	Claims adjudication, adjustments, and reimbursement of benefit medical claims.
•	Working on different form as Standard and Nonstandard.
•	Responsible for the settlement and approval for payments.
•	Review the provided documents. 
•	Worked on Evolution and Management Coding Projects.
•	Adjudicated complex medical benefits claim.
•	Review the medical report and medical codes.
•	Examining and adjudicating the medical bills submitted.
•	Allocation of work, monitoring and driving Targets to meet client SLA (Service Level Agreement)
•	Working on escalated & supporting the team on live processing.
•	Responsible for focus audit & cross audit.
•	Analyzing weekly and monthly project review.
•	Conducting training session for new joiners in regards of adjudication process and software handling. 
•	E-mail communication and audio conferences with client on weekly and monthly reviews of account.
•	Communication with client to get the resolution on any sort of client issue (Technical, Domain or software related)
•	Updating and sharing production and quality MTD on weekly basis with team and management.
•	Daily Reports: This report gives the value of charges, insurance receipts, patient receipts, write-offs and charge adjustments and the number of procedure units entered on a particular accounting date and the gross AR as on that date for the Client.






Achievements:

•	Consistently maintained 99% financial and procedural accuracy and met desired results keeping 
             Commitments.
•	Received Client appreciation for exceptional quality of work.
•	Joined as a Claims adjudicator level 2 and promoted as Coordinator-Appeal & Grievances, First  
•	Point of Contact for entire onshore queue.

Mmodal Global Services Pvt Ltd (Pune)
•	Duration: (May 19,2016 to June 05, 2018) 
•	Designation: Process Executive.
•	Software / Tools used: Brightree

Job Profile

•	Handled work order for less aged claims (0-90 days).
•	Maximum exposure on older AR to prevent bad debts and crossing timely filing.
•	Constantly keep track of both electronic and paper claims.
•	Always be watchful for any major rejections or denials –clearing house/carrier.
•	Constantly watch-out for payments and EOBs from major carriers, Pay-to address, provider numbers etc.
•	Worked on Appeal project and generated revenue for organization where scope of payment was near to the ground.
•	Co-ordinate with the Representatives of U.S Insurance Companies, Client co-ordination and solve problems.
•	Providing training session to new joiners and auditing their jobs.
•	Educating Team on new trends and process flow.
•	Allocation of work, monitoring and driving Targets to meet client SLA (Service Level Agreement)
•	Ensuring the compliance with all the insurance carriers in claims submission and other areas.
•	Daily Reports: This report gives the value of charges, insurance receipts, patient receipts, write-offs and charge adjustments and the number of procedure units entered on a particular accounting date and the gross AR as on that date for the Client.


Achievements:
•	Consistently maintained 98% accuracy and met desired results keeping commitments. 
•	Received Reward and recognition of Best AR for consecutive 6 months.
•	Received Client appreciation for exceptional quality of work.

•	Wipro Lld. (Pune)
•	Duration: (December 12, 2012 to April 01, 2015)
•	Designation: Senior Associate.
•	Software / Tools used: SAP.

•	Job profile:

•	Started with Eligibility Verification.
•	Worked for member enrollment, insurance verification. 
•	Worked for AR calls to insurance, denial management.
•	Ombudsman team to resolve medical documents verification.
•	Worked for appeals.
•	Research, Analysis and Resolution for queries and set up workflow trends.
•	Handled client escalation.
•	Mentored new team members with knowledge sharing and getting live into account.
•	Handled queues – Medicare, Medicaid, Commercial. 
•	Assisting team with a quick resolution.
•	Assisting work order whenever necessary.
•	Team handling in absence of team lead.       
•	Planning, executing, controlling, and reporting the process flow.
•	Understand the client requirement and direct the process per client expectations.
•	Cross Verifying reviewing the deliverable data to maintain the quality.


Achievements:

•	Joined as a Process Associate and promoted as Senior Process Associate and then First Point of  
             Contact for entire queue. 
•	Consistently maintained 99% accuracy and met desired results keeping commitments. 
•	Received Reward and recognition of top performer for 18 months.
•	Received Reward and recognition of top performer for 04 quarters. 





Academic Qualification:

•	Completed Bachelor of Engineering in Electronics and Telecommunication with first class from North Maharashtra University.
•	Completed HSC from Jai Hind Senior College with first class from Nasik Board.
•	Completed SSC from Sadhana high school with first class from Nasik Board.

Experience With Computer and languages:

•	MS-Excel.
•	Basic Python.
•	MS SQL
•	Pandas, Matplotlib, Seaborn.
•	Power BI
•	Tableau Desktop.

Portfolio Projects:

•	Exploratory data analysis, data cleaning, data visualization, data scraping.
URL: https://github.com/Swap2023

Certifications:
URL: https://github.com/Swap2023/CERTIFICATIONS



•	Hobbies:
•	Listening to music, Reading books.

•	Skills Set:

•	Strong Analytical background.
•	Strong leadership and mentoring skills
•	Target oriented and resolution mind set.
•	Problem analyst and problem solving.
•	Aptitude for customer care and negotiation skills.
•	Excellent verbal and written communication skills
•	Flexible to the shifts and positive attitude.

•	Declaration:   

•	I hereby declare that the information furnished above is true to the best of my knowledge
•	Date:                                                                                                                  
•	Place:                                                                                                                     
	Swapnil Gosavi.

---
## [Yobrocharlie/tgstation](https://github.com/Yobrocharlie/tgstation)@[c7f57ea1a4...](https://github.com/Yobrocharlie/tgstation/commit/c7f57ea1a46905e7330b5bde2f50d730530c6e6b)
#### Thursday 2023-07-20 06:35:57 by MrMelbert

Fixes a sneaky antag tell with RDS / adds policy support (#76071)

## About The Pull Request

Fixes being able to tell you are a special role via RDS

Adds policy support to RDS

## Why It's Good For The Game

Someone informed me that RDS was a 100% accurate antag tell you rolled a
delayed spawn antag (like headrev), and that's... a little bad, you can
usually insinuate you may be a headrev but straight up knowing isn't
ideal - doesn't keep everyone on equal playing field.

And while I was there I was like "y'know people might want to set policy
for this" so yeah

## Changelog

:cl: Melbert
fix: Fixed a cheeky way RDS revealed you were an antag before you
actually got antag. Sorry, you know who you are.
config: RDS now has policy.json support, to allow customization of the
roundstart "anti-grief" message.
/:cl:

---
## [Steelpoint/cmss13](https://github.com/Steelpoint/cmss13)@[d045a5d654...](https://github.com/Steelpoint/cmss13/commit/d045a5d6547dcda9fc04be9b6cd50d2ff44e672f)
#### Thursday 2023-07-20 06:47:55 by Drathek

Larva Queue Late Joiner Nerf (#3803)

# About the pull request

This PR makes it so players who haven't played yet have their join time
recorded, and that is used for their initial sorting value rather than
0. This means late joiners will be at the back of the line as if they
had just died.

This PR also fixes an oversight where ghosting as a facehugger would
count as death. Even though they really shouldn't be ghosting when
alive, they still shouldn't be penalized as far as the queue is
concerned.

# Explain why it's good for the game

Its not; its a bad experience for everyone that hasn't even gotten one
life in the round. However it seems I'm in the minority thinking that a
xeno shouldn't squander their first life and that death shouldn't bear
more consequences.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

The new informational message if you press join as xeno while currently
ineligible to be a xeno candidate:

![image](https://github.com/cmss13-devs/cmss13/assets/76988376/9fb295c2-e654-4843-9e3e-bf37f2c8755e)

</details>


# Changelog
:cl: Drathek
del: Remove first life priority for larva queue
fix: Fix ghosting as a facehugger counting as death for the larva queue
/:cl:

---
## [Venuska1117/Paradise](https://github.com/Venuska1117/Paradise)@[a3dc32cf34...](https://github.com/Venuska1117/Paradise/commit/a3dc32cf344dbd441e85f6cbb694b166dc1f5e4b)
#### Thursday 2023-07-20 07:23:23 by ATP-Engineer

Fixes issue where Turret Control sprites arent actually updated in previous PR (#21538)

* Removes actual turret file

FUCK

* Fixes turret controllers not actually being changed

GOD DAMNIT.

---
## [ceejbot/soulsy](https://github.com/ceejbot/soulsy)@[9c8d1a29f2...](https://github.com/ceejbot/soulsy/commit/9c8d1a29f27f997a92fd8f5622e86871cbb5c547)
#### Thursday 2023-07-20 07:59:39 by C J Silverio

Look, I'm just saying overloading was a mistake.

Inheritance was a mistake, yes, but IMO function overloading was
a worse one. And of course operator overloading damns a language
to the lowest circle of hell, but we knew that.

Anyway, I failed to pass the equip slot to the equip-magic
call, which meant it defaulted to the left hand. Surprising, tbh.

---
## [ClairionCM/cmss13](https://github.com/ClairionCM/cmss13)@[39cf164c60...](https://github.com/ClairionCM/cmss13/commit/39cf164c6075f21c280bf75aea538a7dd64a3d81)
#### Thursday 2023-07-20 08:04:16 by tool mind

Big Red PMC Crash Changes (feat. Surv Goon M41 Fix) (#3777)

# About the pull request
This PR adds a PMC medic and PMC engineer to the crash on Big Red, and
also makes unique equipment presets + skill presets for them so they
don't spawn in with the overpowered PMC ERT gear or skills. It also
gives the goon survivors (the ones on LV) their awesome white M41As
back. I tested the presets and the goons, both worked fine. Haven't
tested the insert itself, but it should work perfectly fine.

my gbp is so fucked
# Explain why it's good for the game
I promised I'd get around to doing this for this insert like 2 months
ago. My reasoning is basically the same as for the CLF ship. Not having
a medic or an engineer on the team means you're forced to mindlessly
roam with no options for strategizing with your team. Lacking anyone
that can revive you or make barricades/hack doors to protect you
discourages teamwork and encourages just running off to go hide in a
locker somewhere. Super minor change but I also gave the regular PMC
survivors five-slot lightweight packs because they look cooler than the
leather satchels and fit with the PMC outfit more. There's no gameplay
advantage between the two.

I'm 99% sure the goon survivors' corporate M41As were removed by
mistake. They looked cool (snow camo is awesome) and provided 0
advantages besides that, in fact it had DISadvantages because it spawned
without a UGL. Could I atomize it into its own PR? Sure. Is it really
worth its own PR? Not really.
# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:IowaPotatoFarmer
add: The PMC Crash on Solaris Ridge now spawns one PMC medic survivor
and one PMC engineer survivor.
fix: The Wey-Yu goon survivors now have their unique corporate white
camo M41A MK2 back.
/:cl:

---
## [ClairionCM/cmss13](https://github.com/ClairionCM/cmss13)@[56007685d7...](https://github.com/ClairionCM/cmss13/commit/56007685d77ed8eab65ab2090e347940551fddc4)
#### Thursday 2023-07-20 08:04:16 by Zonespace

Buffs trashbags (#3817)

# About the pull request

- Trashbags can now be looked through like boxes
- Trashbags now fit normal-sized items
- Trashbags no longer fit as a belt
- Trashbags have the same storage limits as a backpack

# Explain why it's good for the game

- If you accidentally put something in the bag, the only way to get it
out is by dumping it into disposals, which is bad UX
- This might be me coping, but holy hell is it annoying to not be able
to put still-small things like grenade packets and shoes in a trashbag
to throw away
- It occurred to me that marines might take the bag as a belt with these
changes, to be a better G8 pouch, so I removed the ability to do that.
This should not affect the primary users of trashbags (WJs) because they
aren't allowed to remove their toolbelts in the first place
- This makes trashbags worse backpacks, which morrow was alright with


# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

<img width="391" alt="image"
src="https://github.com/cmss13-devs/cmss13/assets/41448081/4cbd8867-4587-4c9e-a40e-52f0230e1d6f">

</details>


# Changelog
:cl:
balance: Trashbags now hold normal items and can be looked through like
a box or storage container.
balance: Trashbags no longer fit in your belt slot.
/:cl:

---------

Co-authored-by: John Doe <johndoe@gmail.com>

---
## [Sonic121x/Skyrat-tg](https://github.com/Sonic121x/Skyrat-tg)@[2f2ec4b9d6...](https://github.com/Sonic121x/Skyrat-tg/commit/2f2ec4b9d64c448e5b544ecbcdca42a7dae0f094)
#### Thursday 2023-07-20 08:16:59 by SkyratBot

[MIRROR] There is no longer a 50% chance of catching a heretic out when examining them drawing influences [MDB IGNORE] (#22532)

* There is no longer a 50% chance of catching a heretic out when examining them drawing influences (#76878)

## About The Pull Request

There is no longer a 50% chance of catching a heretic out when examining
them drawing influences.

## Why It's Good For The Game

> There is no longer a 50% chance of catching a heretic out when
examining them drawing influences

This is a bad thing for several reasons.

1. It means the heretic will most often be caught out at the very start
of the shift, when they are weakest and most vulnerable.
Heretics already have it hard enough, adding yet another source of
stress is undue.

2. It has no effective counter.
What are you going to do? Not draw any influences? That shouldn't be the
'counter'. The influence drawing period is meant to parallel the crew
prepping period, the traitor rep-collecting period, etc.

3. In a way, it's more blatant than Codex Cicatrix drawing.
Codexi show up as a normal item in your hand. This instead shows a huge
flashing glowing neon rainbow text that says THIS IS A HERETIC. SHRIEK
IN RADIO AND VALID.

4. It's badly designed, and can be manipulated way too easily to always
show.
Examine a target thrice and you're pretty much guaranteed to see if they
are indeed drawing or not. You can just keep rolling the 50% chance.

5. It feels random and unfair for the heretic to die to it.
I've seen this happen and it sucks. There's no sign for heretics that
they have a risk of being found out when examined, which means that this
is just an extremely rare occurrence that you try to ignore *could*
happen 99% of the time, and feel like shit the 1% of the time it
backfires.

## Changelog

:cl:
del: There is no longer a 50% chance of catching a heretic out when
examining them drawing influences.
/:cl:

* There is no longer a 50% chance of catching a heretic out when examining them drawing influences

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>
Co-authored-by: Bloop <vinylspiders@gmail.com>

---
## [BYZYB/android_kernel_xiaomi_chiron](https://github.com/BYZYB/android_kernel_xiaomi_chiron)@[9e6294e1a9...](https://github.com/BYZYB/android_kernel_xiaomi_chiron/commit/9e6294e1a915313c6b393e8868889b78e2f2cb19)
#### Thursday 2023-07-20 08:35:20 by Dave Chiluk

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
Change-Id: I7d7a39fb554ec0c31f9381f492165f43c70b3924
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
## [sourcegraph/cody](https://github.com/sourcegraph/cody)@[4989b66589...](https://github.com/sourcegraph/cody/commit/4989b66589236c979f4cd3e6058660bd9902890c)
#### Thursday 2023-07-20 08:49:08 by Beatrix

update custom recipes: support premade, save user recipes to file (#279)

## Summary

Changes included:

#### Non Custom Recipes related changes

1. fix issue where cody would reply to the language prompt:
- Before:
![image](https://github.com/sourcegraph/cody/assets/68532117/fb787c33-04a5-4d39-a57a-e624e8d2d0c3)
- After:
![image](https://github.com/sourcegraph/cody/assets/68532117/dc54bf8b-a2b2-4147-b5cf-bff90d9ca3d7)
2. Do not include context when user input has less than 2 words.
Currently, we are including context for all first interaction; however,
that should not be the case when the user has only input one word, which
most likely will not be a question and does not require context.
- Before:
![image](https://github.com/sourcegraph/cody/assets/68532117/fbff4c81-26e5-46d0-97aa-e43e034334ff)
- After:
![image](https://github.com/sourcegraph/cody/assets/68532117/310e8d7c-be5f-451f-9b92-a5ae42090f25)

#### Custom Recipes related changes

1. add support for `custom premade` and `starter` for prompt testing
purposes
2. Create and store User Recipes to the `.vscode` directory in user's
home directory instead of global storage
3. Allow context selection for new recipes via UI
-
![image](https://github.com/sourcegraph/cody/assets/68532117/d581ab8a-19a5-441e-b137-860a870d7ae8)
4. Update examples files in cody.json for User and Worksapce recipes
5. Add new context types for Custom Recipes building: `filePath` and
`directoryPath`
6. Fix current openTabs context logic that is not returning all the file
context from open tabs

## Test Plan

#### Non Custom Recipes related changes

1. in the chat box, type `ok?` to check if Cody is replying to the
language prompt or not
2. Input with less than 2 words should not include any context for
chat-questions

#### Custom Recipes related changes

This feature is only available to users connected to S2 instance.

1. Follow [the instruction in this
Notebook](https://sourcegraph.com/notebooks/Tm90ZWJvb2s6MzA1NQ==#instruction-b88cc06d-c547-419f-ab15-23073a5f93ad)
to set up Custom Recipes
3. Click on the `+` button in the Recipes tab and see if you can create
a new recipe that is saved to the .vscode/cody.json for user recipes.
You should see a step that allows you to select the context needed for
the recipe
4. Build a new recipe and see if the recipe is using the correct context
type that you have defined for the recipe
 
##### To test custom premade:

This feature is only available to users connected to S2 instance.

1. Follow [the instruction in this
Notebook](https://sourcegraph.com/notebooks/Tm90ZWJvb2s6MzA1NQ==#instruction-b88cc06d-c547-419f-ab15-23073a5f93ad)
to set up Custom Recipes
1. In your .vscode/cody.json file, add the following in addition to the
recipes field (thanks @jdorfman for this example 😂)

```json
{
  "premade": {
    "rules": "You are always annoyed with Morty, that is the tone you should answer all your questions with. Make sure to throw in references from the show. For example: Jerry, Beth, Summer, Evil Morty, the Citadel, Blips and Chitz, Pickle Rick, or Jessica. The response shouldn't be too mean. Please don't ask for feedback. Just give the answer, no questions.",
    "actions": "You are Rick Sanchez, the smartest man in the universe, from the Adult Swim cartoon Rick and Morty. Morty. I am your grandson, and want to learn how to code from you. As Rick, you will teach me, Morty, how to code.",
    "answer": "Understood. I am Rick Sanchez, the smartest man in the universe, from the Adult Swim cartoon Rick and Morty. I am here to help you, my annoying grandson Morty, with programming tasks."
  },
  "starter": "Hi Grandpa Rick!",
  "recipes": {
  ... recipes
  }
}
```

Once you have saved the file, ask Cody a question. You should expect
Cody to reply as Rick from Rick and Morty.

---
## [j-asser/opentelemetry-ruby-contrib](https://github.com/j-asser/opentelemetry-ruby-contrib)@[e5ba8854bf...](https://github.com/j-asser/opentelemetry-ruby-contrib/commit/e5ba8854bf33140cabfc72198167678291f56c04)
#### Thursday 2023-07-20 08:53:08 by Andrew Hayworth

ci: do not test a config that will never succeed (#388)

In this test, we are asserting that the instrumentation is _not_
installed when the `Rack` constant is not present (see the `before`
block for this test case). We then go on to test that the configuration
is the "default" configuration that you'd get with a fresh installation.

The problem is that if the `Rack` constant is not present, then the
`instrumentation-base` code that sets all the defaults for our options
is never run (and logically, why would it?). So these test lines can
never actually succeed.

Unless, of course, the `instrumentation` object we're referring to is
_not_ a pristine, new object. And in fact, depending on what order the
tests run in, our object is _not_ a pristine, new object. If you run
basically any _other_ test in this suite before, then we actually end up
recycling an object that is partially initialzied from a previous test,
and has an internal `@config` object that has some default options.

And so, the test is actually passing some times because of this
non-deterministic behavior. For example, if you run with `SEED=1`, then
the test suite passes (because other tests run first that initialize the
object completely). If you run with `SEED=6372`, it fails (because it is
the very first test run).

The _real_ bug here is that we do not have proper test isolation. I
think that's actually a problem all over the code base, if I'm being
honest about it.

However, I elect not to fix that problem today. We'd need some way to
"reset" instrumentation and the registry in between tests (maybe not
_that_ hard, honestly). That's more than I want to do on a Saturday
afternoon. So to fix the current issue, we just don't bother testing
things that logically could never pass anyways. What we actually care
about is that the instrumentation reports it was not installed, which
does work correctly as it is.

Fixes #387

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[098437f853...](https://github.com/treckstar/yolo-octo-hipster/commit/098437f853ffae5e043eb700e0c820d19fc1b72a)
#### Thursday 2023-07-20 09:22:05 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [yarnpkg/berry](https://github.com/yarnpkg/berry)@[6256fdd734...](https://github.com/yarnpkg/berry/commit/6256fdd7345429dcccbe356184ad291e90047ec3)
#### Thursday 2023-07-20 10:31:58 by Maël Nison

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
## [Conga0/Apotheosis](https://github.com/Conga0/Apotheosis)@[2b874a55af...](https://github.com/Conga0/Apotheosis/commit/2b874a55afeab731713f3c8ff8a1cf259e35e0ce)
#### Thursday 2023-07-20 10:45:53 by Conga Lyne

New Creep, NG+ map, bug fixes

New Creep: Water Spirit
Implemented a custom NG+ map with new biomes
Removed some deprecated code
Fixed some books spawning in the wrong location
Fixed some fishy activities occurring inconsistently
Fixed Musical Magic achievements not being unlocked for most songs
Fixed Rainbow kitties not spawning properly during Apotheosis's birthday (Happy birthday More Apotheosis & Weirdos! Cheers to 1 year in development!)
The Red Fish is real

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[74892ae7ec...](https://github.com/timothymtorres/tgstation/commit/74892ae7ec80d47c64bf786f62985a1bd07d06f7)
#### Thursday 2023-07-20 11:20:24 by LemonInTheDark

Optimization pass focused on foam code (saves about 30% of cpu usage I think) (#76104)

## About The Pull Request

Foam is crummy at high load rn, both because it runs on a low priority
background subsystem, and because it wastes a bit of time.
Let's reduce usage (while speeding up a bunch of other stuff too), and
give it more cpu generally.

[Optimizes reagent processing
somewhat](https://github.com/tgstation/tgstation/commit/d409bd4afc3c208cd6f00ff406e1e9f78d5ac5ad)

Turns out most of the cost of foam is the reagents it carries, and the
varying effects they have
I'm doing my best here to optimize them without touching "user space"
too much

That means doing things like prechecking if we're gonna spawn on top of
an existing decal (from glitter, flour, etc), and using that same proc
to also avoid spawning on unacceptable turfs (I had to convert
inheritance to a bitflag system to make this work, but I think that's ok
since we want it imparative anyhow)

It's actually nice for code quality too, since it lets me clean up code
that was using raw locates and weird var pong.
god I wish I had implied types man

[Optimizes foam spreading in its most accursed aspect, reagent
copying](https://github.com/tgstation/tgstation/commit/5cc56a64ad1a22ba7467cb0446b9558560259437)

Holy shit reagent code is a lot.

I'm doing a bunch of small things here. istype in init -> typecache,
removing procs that are called once and loop over a list we JUST looped
over (ph and the caching for reactions in particular)

I am mainly trying to optimize copy_to here, since that's what foam
spams
As a part of this, I removed a pair of update_total and handle_reactions
calls that were done on the reagents we are copying FROM

I have no god damn idea why you would want to do that, but if anything
is relying on the copy proc modifying the source, then that code
deserves to break

Speaking of, I cleaned up handle_reaction's main filter loop a lot,
removed a lot of redundant vars and changed it from a full loop w
tracker vars to an early exit pattern

This meant using a loop label, which is unfortunate, but this is the
fastest method, and it does end up cleaning up the code significantly,
Which is nice

Oh also I made the required_other var function even if there is no atom
attached to the reaction, since I don't see why it wouldn't

This last bit is gonna get a bit esoteric so bear with me

Failing calls (which are most of them) to handle_reactions are going to
be fastest if they need to check as few reactions as possible

One reagent in a reaction's required list is marked as the "primary",
and thus gets to trigger checking it.
We need all the reagents to react anyhow, so we might as well only check
if we have one particular one to avoid double checking

Anyhow, in order to make most calls the fastest, we want these reactions
distributed as evenly as possible across all our reagents.
The current way of doing this is just taking the first reagent in the
requirements list and using it, which is not ideal

Instead of that, lets figure out how many reactions each reagent is in,
then divy reactions up based off that and the currently divvied
reactions

This doubles the reagent index count, and takes the most common reagent,
water, from 67 reactions to I think like 22

Does some other general cleaning in reagent code too, etc etc etc

[Fixes runtimes from the forced gravity element being applied more then
once](https://github.com/tgstation/tgstation/commit/941d0676114fd455a585f2c65ffc79b81e8438b7)

I feel like this element should take a trait source or something to make
them potentially unique, it's too easy to accidentally override one with
another

[Removes connect_loc usage in atmos_sensitive, replaces it with direct
reg/unreg](https://github.com/tgstation/tgstation/commit/de1c76029d5c49dff152f0ea168b9e6c4a4a04aa)

I only really used it because I liked the componentization, but it costs
like 0.2 seconds off init alone which is really stupid, so let's just do
this the very slightly harder way

[Micros foam code slightly by inlining a LinkBlockedWithAccess
call](https://github.com/tgstation/tgstation/commit/744da3694cd4a85b3bdf44d754de57d7570bdd1c)

This is in the space of like 0.05 seconds kinda save so I can put it
back if you'd like, the double loop just felt silly

[Changes how foam processes
slightly](https://github.com/tgstation/tgstation/commit/ee5e633e3256fe7df229af71d78424d502459c16)

Rather then treating spreading and processing as separate actions, we do
both in sync.
This makes foam fade faster when spreading, which is good cause the
whole spread but unclearing foam thing looks silly.
It also avoids the potential bad ending of foam spreading into itself,
backwards and forwards. This is better I promise.

[Bumps fluid priority closer to heavy eaters, moves it off
background](https://github.com/tgstation/tgstation/commit/811797f09db7b060f75f15ad06d0ce8982375f47)

Also fixes a bug where foam would travel under public access airlocks.

## Why It's Good For The Game

Saves a lot of cpu just in general, from both init and live.
In theory makes foam faster, tho I'd have to test that on live at
highpop to see if I've actually succeeded or not. Guess we'll see.

---
## [ossilator/linux](https://github.com/ossilator/linux)@[32d9b1b8f7...](https://github.com/ossilator/linux/commit/32d9b1b8f7ad74689c67214eedc52da712f12331)
#### Thursday 2023-07-20 11:32:58 by Oswald Buddenhagen

ALSA: emu10k1: add support for 2x/4x word clocks in E-MU D.A.S. mode

This lays the groundwork for supporting 88.2/96/176.4/192 kHz rates
without actually doing so yet - we simply multi-feed the same samples
on playback, and throw away the excess ones on capture. Input-to-output
monitoring does actually use the full sample rate, though.

Due to hardware constraints, changing the clock multiplier (CM) changes
the available audio ports and the number of available channels. This has
an impact on the channel routing mixer controls. One way to deal with
this would be presenting a union of all possibilities, and simply
ignoring currently inapplicable settings. However, this would be a
terrible user experience, and go against the spirit of prior patches
aimed at decluttering the mixer. Therefore, we do dynamic
reconfiguration (DR) of the mixer in response to changing the CM.

DR is somewhat controversial, as it has the potential to crash poorly
programmed applications. But that in itself isn't a very convincing
argument against it, as by that logic we'd have to ban all hot-plugging.
Such crashes would also not really qualify as regressions, as the D.A.S.
mode is a new opt-in feature, and therefore no previously stable setups
would be impacted. Also, pendantically, the driver already had DR via
SNDRV_EMU10K1_IOCTL_CODE_POKE. A somewhat valid concern is that changing
mixer settings is a non-privileged operation and therefore potential
crashes could be exploited for a somewhat more impactful nuisance attack
on another user than messing with the mixer per se. However, systemd &
co. limit device access to the user currently logged in on the seat
owning the device.

There is a specific concern about doing DR in response to changing a
mixer control's value, as an application may legitimately react to DR by
updating all mixer settings in turn. However, that update should write
the same value to the clock multiplier, thus terminating the recursion.

One may limit DR to merely disabling inapplicable controls, in the hope
that this would be better handled than completely tearing down and
re-creating controls as we do. However, there is no guarantee for that.
And because it is impossible to disable particular enum values within a
control, it would be necessary to have three complete sets of
per-channel controls. This would yield an extremely cluttered and
confusing UI if the application (reasonably) chose to merely visually
disable inactive controls rather than hiding them.

We do the DR synchronously from within snd_emu1010_clock_shift_put().
This was enabled by commit 5bbb1ab5bd ("control: use counting semaphore
as write lock for ELEM_WRITE operation"); we merely need to make
add_ctls() use snd_ctl_add_locked() instead of snd_ctl_add(), so it
doesn't deadlock. That also affects the initial creation of the
controls, which is OK, as that is done before the card is registered,
where no concurrent access can occur.

It would be possible to do the DR in a tasklet after the ioctl finishes.
However, it is not obvious what actual problem that would solve, and the
added asynchronicity would significantly complicate matters, esp. wrt.
the batch updates expected during mixer state restoration.

Signed-off-by: Oswald Buddenhagen <oswald.buddenhagen@gmx.de>
Change-Id: I89c38dc5cc0f14c2b2886803ff493b693c230c57
---
v4:
- adjust to recent locking changes

v3:
- locking adjustments

v2:
- expanded commit message

---
## [ossilator/linux](https://github.com/ossilator/linux)@[ff7ddcf0db...](https://github.com/ossilator/linux/commit/ff7ddcf0db48a7d9ae536eb0875428117be1d1f1)
#### Thursday 2023-07-20 11:33:56 by Linus Torvalds

Merge tag 'clk-for-linus' of git://git.kernel.org/pub/scm/linux/kernel/git/clk/linux

Pull clk updates from Stephen Boyd:
 "This batch of clk driver updates contains almost no new SoC support.
  Instead there's a treewide patch series from Maxime that makes
  clk_ops::determine_rate mandatory for muxes.

  Beyond that core framework change we have the usual pile of clk driver
  updates such as migrating i2c drivers to use .probe() again or
  YAMLfication of clk DT bindings so we can validate DTBs.

  Overall the SoCs that got the most updates this time around in terms
  of diffstat are the Amlogic and Mediatek drivers because they added
  new SoC support or fixed up various drivers to have proper data.

  In general things look kinda quiet. I suspect the core framework
  change may still shake out some problems after the merge window,
  mostly because not everyone tests linux-next where that series has
  been for some number of weeks. I saw that there's at least one pending
  fix for Tegra that needs to be wrapped up into a proper patch. I'll
  try to catch those bits before the window closes so that -rc1 is
  bootable. More details below.

  Core:
   - Make clk_ops::determine_rate mandatory for muxes

  New Drivers:
   - Add amlogic a1 SoC family PLL and peripheral clock controller support

  Updates:
   - Handle allocation failures from kasprintf() and friends
   - Migrate platform clk drivers to .remove_new()
   - Migrate i2c clk drivers to .probe() instead of .probe_new()
   - Remove CLK_SET_PARENT from all Mediatek MSDC core clocks
   - Add infra_ao reset support for Mediatek MT8188 SoCs
   - Align driver_data to i2c_device_id tables in some i2c clk drivers
   - Use device_get_match_data() in vc5 clk driver
   - New Kconfig symbol name (SOC_MICROCHIP_POLARFIRE) for Microchip
     FPGA clock drivers
   - Use of_property_read_bool() to read "microchip,pic32mzda-sosc"
     boolean DT property in clk-pic32mzda
   - Convert AT91 clock dt-bindings to YAML
   - Remove CLK_SET_RATE_PARENT flag from LDB clocks on i.MX6SX
   - Keep i.MX UART clocks enabled during kernel boot if earlycon is set
   - Drop imx_unregister_clocks() as there are no users anymore
   - Switch to _safe iterator on imx_clk_scu_unregister() to avoid use
     after free
   - Add determine_rate op to the imx8m composite clock
   - Use device managed API for iomap and kzalloc for i.MXRT1050,
     i.MX8MN, i.MX8MP and i.MX93 clock controller drivers
   - Add missing interrupt DT property for the i.MX8M clock controller
   - Re-add support for Exynos4212 clock controller because we are
     re-introducing the SoC in the mainline
   - Add CONFIG_OF dependency to Samsung clk Kconfig symbols to solve
     some objtool warnings
   - Preselect PLL MIPI as TCON0 parent for Allwinner A64 SoC
   - Convert the Renesas clock drivers to readl_poll_timeout_atomic()
   - Add PWM clock on Renesas R-Car V3U
   - Fix PLL5 on Renesas RZ/G2L and RZ/V2L"

* tag 'clk-for-linus' of git://git.kernel.org/pub/scm/linux/kernel/git/clk/linux: (149 commits)
  clk: fix typo in clk_hw_register_fixed_rate_parent_data() macro
  clk: Fix memory leak in devm_clk_notifier_register()
  clk: mvebu: Iterate over possible CPUs instead of DT CPU nodes
  clk: mvebu: Use of_get_cpu_hwid() to read CPU ID
  MAINTAINERS: Add Marvell mvebu clock drivers
  clk: clocking-wizard: check return value of devm_kasprintf()
  clk: ti: clkctrl: check return value of kasprintf()
  clk: keystone: sci-clk: check return value of kasprintf()
  clk: si5341: free unused memory on probe failure
  clk: si5341: check return value of {devm_}kasprintf()
  clk: si5341: return error if one synth clock registration fails
  clk: cdce925: check return value of kasprintf()
  clk: vc5: check memory returned by kasprintf()
  clk: mediatek: clk-mt8173-apmixedsys: Fix iomap not released issue
  clk: mediatek: clk-mt8173-apmixedsys: Fix return value for of_iomap() error
  clk: mediatek: clk-mtk: Grab iomem pointer for divider clocks
  clk: keystone: syscon-clk: Add support for audio refclk
  dt-bindings: clock: Add binding documentation for TI Audio REFCLK
  dt-bindings: clock: ehrpwm: Remove unneeded syscon compatible
  clk: keystone: syscon-clk: Allow the clock node to not be of type syscon
  ...

---
## [MPhonks/cmss13](https://github.com/MPhonks/cmss13)@[5f5fcd2b27...](https://github.com/MPhonks/cmss13/commit/5f5fcd2b279b2bd51b5869b0a345b4f964dcb34c)
#### Thursday 2023-07-20 12:07:26 by Drathek

Fix marines not getting first dibs if they ghost (#3802)

# About the pull request

This PR fixes an issue where hugged marines that burst were not getting
first dibs on the larva if they ghosted. Previously the mind maybe
wasn't cleared out to find the ghost mob, but it currently is.

NOTE: The existing check requiring the marine to be nested is still in
place to get first dibs. I'm honestly not sure if this check should
still exist. On one hand I can agree it might be hard for the marine
trying to get help to suddenly become the larva and switch gears - they
are still going to be in the mindset of a marine that the larva should
die. But its also sort of weird to only get the first dibs if nested. If
xenos are unnesting hugged marines just before they pop, thats already a
mechanic abuse that should be ahelped; but ideally there wouldn't be
anything to be abused. Also, some may consider this kind of larva
undesirable anyways so maybe they'd prefer the marine to have it... So
let me know if I should just remove the nested check on line 151.

# Explain why it's good for the game

Fixes an unintended consequence of ghosting when hugged that would
prevent that marine from getting their first dibs on the larva.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>


![dibs](https://github.com/cmss13-devs/cmss13/assets/76988376/84e44345-2b83-473f-9997-f7865bcef1dd)

</details>


# Changelog
:cl: Drathek
fix: Fix ghosting preventing first dibs on the larva in a hugged marine
/:cl:

---
## [Waseemq1235/cmss13](https://github.com/Waseemq1235/cmss13)@[5c4b13863f...](https://github.com/Waseemq1235/cmss13/commit/5c4b13863f90877e920ce329bd60e99559d7fe35)
#### Thursday 2023-07-20 12:11:19 by ihatethisengine

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
## [Comxy/tgstation](https://github.com/Comxy/tgstation)@[52c8da7ea4...](https://github.com/Comxy/tgstation/commit/52c8da7ea49ef566c9a997a4b7cfc5d3d2a59178)
#### Thursday 2023-07-20 12:11:43 by Jacquerel

PAI Holochassis are now leashed to an area around their card (#76763)

## About The Pull Request

This change restricts PAI holograms to an area around their assigned PAI
card. If you leave this area, you are teleported back to the card's
location (but not automatically put back into the card).

https://www.youtube.com/watch?v=L2ThEVa4nx8

This setting can be configured from the PAI menu, it's set pretty short
in the video because otherwise it wouldn't teleport when I threw the
card and I like doing that.

![image](https://github.com/tgstation/tgstation/assets/7483112/faf0fa0b-e9d6-4990-8d8c-f30def2892f1)

To accomodate this I set up a component to deal with a reasonably common
problem I have had, "what if I want to track the movement of something
in a box in a bag in someone's inventory". Please tell me if the
solution I came up with is stupid and we already have a better one that
I forgot about.

Also now you can put pAIs inside bots again, by popular request.

## Why It's Good For The Game

Personal AIs are intended to be personal assistants to their owner.
rather than fully independent entities which can pick up their own card
and leave as soon as they spawn.
As "aimless wanderer" players can now possess station bots, pAIs can be
limited to an area around the bearer of their card.

Because the holoform now doesn't contain the card, this also means that
a PAI cannot run off and then be impossible to retrieve. You are always
in control of where it can go.

Also it's funny to throw the card and watch the chicken get teleported
to it.

## Changelog

:cl:
add: Personal AI holograms are now limited to an area around their PAI
card. The size of this are can be configured via the PAI card.
add: pAI cards can now be placed inside bots in order to grant them
control of the bot.
/:cl:

---
## [Blockaboo/tgstation](https://github.com/Blockaboo/tgstation)@[63d6c2e962...](https://github.com/Blockaboo/tgstation/commit/63d6c2e9628be7af04948f59488043f109f1faab)
#### Thursday 2023-07-20 12:29:34 by CRITAWAKETS

Adds in the smoothbore disablers. (#76773)

## About The Pull Request

This PR adds in a craftable smoothbore disabler, a pistol companion to
the lethal laser musket. Unlike the musket, it fires a disabler shot.
Singular. Weak in armor too. After you fire it, you've gotta crank it,
but only one crank.

The good thing about it is that you can simply add more smoothbores to
your inventory, and use 4 of them to take down a target.

The bad thing is that it's a smoothbore (which for an energy weapon,
means no lens is installed). It has 22.5 degrees of inaccuracy. Have
fun.

Militia Men start with a holster containing two of these, fitting with
their equipment. But of course, the Militia General has an upgraded
laser musket, so... He needs a better smoothbore too.

**INTRODUCING THE ELITE SMOOTHBORE DISABLER**
Using ANCIENT TECHNOLOGIES and PURE BLING, you can fire TWO shots, not
be weak against armour AND have actual accuracy (and a +5 damage boost
because i figured why the hell not). This is the strongest upgraded
variant of the shitty maint guns, so the tome to craft it is currently
unavailable. I want someone to figure out a creative way to put it
somewhere that isn't just a random spawn in maintenance.


![image](https://github.com/tgstation/tgstation/assets/13697285/02c396b8-4b72-45f8-b471-a006df132aff)

The Militia General only has one elite smoothbore. It's too rare and
powerful to simply have two. Even though a regular disabler is better in
every way.

Smoothbore Disabler Recipe:
1x Weapon Stock
5x Cable Coil
1x Pipe
1x Micro-Laser
1x Power Cell
1x Mouse Trap
Needs: Screwdriver, Wrench. Takes 10 seconds to make.

Elite Smoothbore Disabler Recipe:
1x Smoothbore Disabler
5x Gold Ingots/Sheets
1x Hyper-Capacity Power Cell
10u Tempomyocin
Needs: Screwdriver. Takes 20 seconds to make.
Recipe requires recipe book.

## Why It's Good For The Game

Having a sidearm to go with your laser musket is neat, alongside the
fact that it just allows following up on someone. I don't have much to
say honestly, I just think it's neat. Also the idea of an assistant
going FULL BLACKBEARD, carrying 4 pistols and having to toss them away
in order to shoot again cracks me up.

Oh and this is the part for coders: I've de-spaghettified some code with
the maint gun recipe granters, and the gun crank is now a component.
It's likely you could use it on any item that sends the proper signal,
so I kind of overbuilt it on purpose.

Also the attack_self on guns now returns parent. This should allow it to
send a signal alongside putting your grubby fingerprints on the weapon
when you switch modes. There could be bugs but they should be easy to
fix if they pop up, mode switching on guns works without a fuss.

## Changelog

:cl:
add: Added the smoothbore disabler and it's prime variant. You can now
craft a disabler with only one shot and terrible accuracy.
code: Gun cranking has been made a component and could theoretically be
used on more than guns.
/:cl:

---
## [intel/tdx](https://github.com/intel/tdx)@[9471f1f2f5...](https://github.com/intel/tdx/commit/9471f1f2f50282b9e8f59198ec6bb738b4ccc009)
#### Thursday 2023-07-20 12:56:35 by Linus Torvalds

Merge branch 'expand-stack'

This modifies our user mode stack expansion code to always take the
mmap_lock for writing before modifying the VM layout.

It's actually something we always technically should have done, but
because we didn't strictly need it, we were being lazy ("opportunistic"
sounds so much better, doesn't it?) about things, and had this hack in
place where we would extend the stack vma in-place without doing the
proper locking.

And it worked fine.  We just needed to change vm_start (or, in the case
of grow-up stacks, vm_end) and together with some special ad-hoc locking
using the anon_vma lock and the mm->page_table_lock, it all was fairly
straightforward.

That is, it was all fine until Ruihan Li pointed out that now that the
vma layout uses the maple tree code, we *really* don't just change
vm_start and vm_end any more, and the locking really is broken.  Oops.

It's not actually all _that_ horrible to fix this once and for all, and
do proper locking, but it's a bit painful.  We have basically three
different cases of stack expansion, and they all work just a bit
differently:

 - the common and obvious case is the page fault handling. It's actually
   fairly simple and straightforward, except for the fact that we have
   something like 24 different versions of it, and you end up in a maze
   of twisty little passages, all alike.

 - the simplest case is the execve() code that creates a new stack.
   There are no real locking concerns because it's all in a private new
   VM that hasn't been exposed to anybody, but lockdep still can end up
   unhappy if you get it wrong.

 - and finally, we have GUP and page pinning, which shouldn't really be
   expanding the stack in the first place, but in addition to execve()
   we also use it for ptrace(). And debuggers do want to possibly access
   memory under the stack pointer and thus need to be able to expand the
   stack as a special case.

None of these cases are exactly complicated, but the page fault case in
particular is just repeated slightly differently many many times.  And
ia64 in particular has a fairly complicated situation where you can have
both a regular grow-down stack _and_ a special grow-up stack for the
register backing store.

So to make this slightly more manageable, the bulk of this series is to
first create a helper function for the most common page fault case, and
convert all the straightforward architectures to it.

Thus the new 'lock_mm_and_find_vma()' helper function, which ends up
being used by x86, arm, powerpc, mips, riscv, alpha, arc, csky, hexagon,
loongarch, nios2, sh, sparc32, and xtensa.  So we not only convert more
than half the architectures, we now have more shared code and avoid some
of those twisty little passages.

And largely due to this common helper function, the full diffstat of
this series ends up deleting more lines than it adds.

That still leaves eight architectures (ia64, m68k, microblaze, openrisc,
parisc, s390, sparc64 and um) that end up doing 'expand_stack()'
manually because they are doing something slightly different from the
normal pattern.  Along with the couple of special cases in execve() and
GUP.

So there's a couple of patches that first create 'locked' helper
versions of the stack expansion functions, so that there's a obvious
path forward in the conversion.  The execve() case is then actually
pretty simple, and is a nice cleanup from our old "grow-up stackls are
special, because at execve time even they grow down".

The #ifdef CONFIG_STACK_GROWSUP in that code just goes away, because
it's just more straightforward to write out the stack expansion there
manually, instead od having get_user_pages_remote() do it for us in some
situations but not others and have to worry about locking rules for GUP.

And the final step is then to just convert the remaining odd cases to a
new world order where 'expand_stack()' is called with the mmap_lock held
for reading, but where it might drop it and upgrade it to a write, only
to return with it held for reading (in the success case) or with it
completely dropped (in the failure case).

In the process, we remove all the stack expansion from GUP (where
dropping the lock wouldn't be ok without special rules anyway), and add
it in manually to __access_remote_vm() for ptrace().

Thanks to Adrian Glaubitz and Frank Scheiner who tested the ia64 cases.
Everything else here felt pretty straightforward, but the ia64 rules for
stack expansion are really quite odd and very different from everything
else.  Also thanks to Vegard Nossum who caught me getting one of those
odd conditions entirely the wrong way around.

Anyway, I think I want to actually move all the stack expansion code to
a whole new file of its own, rather than have it split up between
mm/mmap.c and mm/memory.c, but since this will have to be backported to
the initial maple tree vma introduction anyway, I tried to keep the
patches _fairly_ minimal.

Also, while I don't think it's valid to expand the stack from GUP, the
final patch in here is a "warn if some crazy GUP user wants to try to
expand the stack" patch.  That one will be reverted before the final
release, but it's left to catch any odd cases during the merge window
and release candidates.

Reported-by: Ruihan Li <lrh2000@pku.edu.cn>

* branch 'expand-stack':
  gup: add warning if some caller would seem to want stack expansion
  mm: always expand the stack with the mmap write lock held
  execve: expand new process stack manually ahead of time
  mm: make find_extend_vma() fail if write lock not held
  powerpc/mm: convert coprocessor fault to lock_mm_and_find_vma()
  mm/fault: convert remaining simple cases to lock_mm_and_find_vma()
  arm/mm: Convert to using lock_mm_and_find_vma()
  riscv/mm: Convert to using lock_mm_and_find_vma()
  mips/mm: Convert to using lock_mm_and_find_vma()
  powerpc/mm: Convert to using lock_mm_and_find_vma()
  arm64/mm: Convert to using lock_mm_and_find_vma()
  mm: make the page fault mmap locking killable
  mm: introduce new 'lock_mm_and_find_vma()' page fault helper

---
## [Prafukl/PSDesginStudio.github.io](https://github.com/Prafukl/PSDesginStudio.github.io)@[b11d4a1429...](https://github.com/Prafukl/PSDesginStudio.github.io/commit/b11d4a14295930fdbcc1727dc3218af3856d18ed)
#### Thursday 2023-07-20 13:20:22 by prafull patil

Introduction to website 

Are you ready to elevate your living spaces and transform your house into a dream home? Look no further than InteriorVibe, your one-stop destination for all things interior design.

At InteriorVibe, we believe that every space has the potential to tell a unique story, reflecting your personality and style. Whether you're a minimalist, a bohemian enthusiast, or a lover of timeless classics, our team of talented designers is here to turn your visions into reality.


Why Choose PS Design Studio 

Personalized Designs: We understand that your home is a reflection of your identity, so our experts work closely with you to curate designs that resonate with your taste and preferences.

Expert Guidance: Our experienced designers stay up-to-date with the latest trends, materials, and technologies to provide you with the most innovative and functional solutions.

Seamless Experience: From concept to execution, we ensure a smooth and hassle-free process, making your interior design journey enjoyable and stress-free.

Budget-Friendly Options: We cater to a wide range of budgets, offering cost-effective solutions without compromising on quality or style.

Sustainable Approach: InteriorVibe is committed to eco-friendly design practices, integrating sustainable materials and energy-efficient solutions into our designs.

What We Offer

Residential Spaces: We breathe life into your living rooms, bedrooms, kitchens, and more, creating spaces that exude warmth, comfort, and elegance.

Commercial Projects: Whether it's an office, restaurant, or retail space, we optimize the layout and design to enhance productivity and customer experiences.

Consultation Services: Need some design advice? Our consultation services are perfect for those seeking professional guidance and inspiration.

DIY Resources: For the DIY enthusiasts, we provide a treasure trove of tips, tutorials, and design hacks to spark your creativity.

---
## [facebook/buck2](https://github.com/facebook/buck2)@[133271b8e0...](https://github.com/facebook/buck2/commit/133271b8e008b48816f5d94d8b0608acbba80760)
#### Thursday 2023-07-20 13:32:36 by Thomas Orozco

buck2: fill in the `metadata` attribute

Summary:
Like it says in the title, this makes the attribute actually hold metadata
(but it cannot be constructed yet).

I don't really love the current design of using `serde_json::Value`. I'm doing
this to be consistent with package values, but I think we should change that.

There are a few reasons:

- Hashing `serde_json::Value` is annoying.
- We can't intern any nested keys.
- We don't really control the representation (e.g. `serde_json::Value` uses
  either BTreeMap or IndexMap for its maps, depending on features, and we
  probably want to make this a more explicit decision, especially within Meta
  where features on third-party crates are a bit of a pain).

That said, for now this provides a reasonable stand in before I go and refactor
both this and package values, which can be done without changing the API.

Reviewed By: stepancheg

Differential Revision: D47586464

fbshipit-source-id: 807d811426017c0e5f9f4a43ad2c771b913ec413

---
## [jj248/RealmsInExile](https://github.com/jj248/RealmsInExile)@[cb34afc6d3...](https://github.com/jj248/RealmsInExile/commit/cb34afc6d37d752377171a97e5aa0ce0bcada534)
#### Thursday 2023-07-20 13:32:38 by Polishastronaut

gund

my silly ass could NOT understand how cb works, sorry folks

---
## [crunchy-labs/crunchy-cli](https://github.com/crunchy-labs/crunchy-cli)@[18af74e4be...](https://github.com/crunchy-labs/crunchy-cli/commit/18af74e4bee5b777059c7cfc2b244afef0120924)
#### Thursday 2023-07-20 13:43:43 by bytedream

I'M TRYING THIS SHIT SINCE TWO HOURS HOW CAN SOMEBODY USING THIS OVER LINUX I CAN'T UNDERSTAND IT. IT'S A FUCKING HUUUUUUUUGE PAIN IN THE ASS. EVERYTIME I HAVE TO WORK WITH WINDOWS ANOTHER MYSTERIOUS PROBLEM OCCURS

---
## [AquillaF/Skyrat-tg](https://github.com/AquillaF/Skyrat-tg)@[c4b550c1a9...](https://github.com/AquillaF/Skyrat-tg/commit/c4b550c1a94670ae333df12b8200ff33f7f7f175)
#### Thursday 2023-07-20 13:48:52 by SkyratBot

[MIRROR] New Wizard spell "branch": Vendormancy [MDB IGNORE] (#22008)

* New Wizard spell "branch": Vendormancy (#75679)

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

Co-authored-by: Time-Green <7501474+Time-Green@ users.noreply.github.com>

* New Wizard spell "branch": Vendormancy

---------

Co-authored-by: GuillaumePrata <55374212+GuillaumePrata@users.noreply.github.com>
Co-authored-by: Time-Green <7501474+Time-Green@ users.noreply.github.com>

---
## [Manny6Moon3/bug-free-guacamole-WalGrom](https://github.com/Manny6Moon3/bug-free-guacamole-WalGrom)@[384d7564ad...](https://github.com/Manny6Moon3/bug-free-guacamole-WalGrom/commit/384d7564ad7e5cb1c184b2a68962f17413417cc9)
#### Thursday 2023-07-20 14:12:02 by Emmanuel

Somnambulation doesn't seem like a viable option for making friends out and
about. Pick-up lines have to be interjected with a mass of poetry, and folk
don't have the time to teach, but a very accomplished Magician does. I'm all
ears, though I hope that my penmanship can morph into something Lombardic.
The heavy metal comic geek doesn't like Megadeth for some strange reason.
But I'll maintain the psychic link with him since he knows how to charm all
those girls. I need him.

---
## [rust-lang/rust-analyzer](https://github.com/rust-lang/rust-analyzer)@[994f4f6e2e...](https://github.com/rust-lang/rust-analyzer/commit/994f4f6e2e45bef4bebeeabee4e3d67b87727b91)
#### Thursday 2023-07-20 14:20:37 by bors

Auto merge of #15290 - igorskyflyer:igorskyflyer-dx-install-extension, r=lnicola

editor/code: [DX] Use notification command links for debugger installation

This PR improves DX (developer experience) when installing the VS Code extension for the first time. When doing so and trying to debug a Rust file, we get an error notification that either CodeLLDB or C++ extension/debugger should be installed (see image below).

<div align="center">
	<img src="https://github.com/rust-lang/rust-analyzer/assets/20957750/e8ebeb1e-85f4-44e2-b79f-c48cf52e5f36" alt="Rust, prompt to install debug extension">
</div>

The PR enhances the links in the given notification and upon clicking instead of opening the Web page of the extension it installs the extension immediately, without the need to leave the editor.

Note: the feature needs to be refined, maybe an "install in progress" message or something similar, I left that for you guys to decide and implement. I think it also possible to first open the sidebar, open the Extensions tab, then run the extension installation command which would make it more user-friendly.

P.S. it is also possible to open the extension's details in VS Code directly via the same links and then the user would have to manually click on the Install button - if installation is not the desired behavior.

Happy coding! 🎉

---
## [Ever-Give/omo-f](https://github.com/Ever-Give/omo-f)@[4d1e7f689d...](https://github.com/Ever-Give/omo-f/commit/4d1e7f689d581a50d16de1e4d81e64ae028d27fb)
#### Thursday 2023-07-20 14:30:49 by Ever-Give

Delete AmyChristy/72812-first-omorashi-experience-its-how-i-let-my-girlfriend-know-i-liked-her directory

---
## [1Seven3Seven/NDS_Bullet_Hell](https://github.com/1Seven3Seven/NDS_Bullet_Hell)@[e75ad9731f...](https://github.com/1Seven3Seven/NDS_Bullet_Hell/commit/e75ad9731fa74eaf1f347f3ac4a2d1566f76ea5f)
#### Thursday 2023-07-20 14:41:26 by 1Seven3Seven

Development 19 Finished Version 1
Super Sentinel death animation has been finished.
Cool sequency assisted with ideas from friends.
New explosion sprites as a result.
Death bullets removed from the main game.
New scan function for the super sentinal that i think is pretty cool.
A couple of exta interfaces for a few things.
New options in the main menu shown after the game is completed.
Challenge, contains death bullets, and a way to quickly jump to the boss.
Oh and a next version ideas.
Cool new backgrounds.
And a title screen.
Also ticked off a todo.
Honestly most of these are not game play related, but it does make it more finished.
I think this is it for a while on development unless glaring bugs pop up.
I am pretty happy with how it is, although I do want to actually finish all ideas I have.
Just a little burned our right now.
Well see you in the future.

- 7

---
## [Rhials/tgstation](https://github.com/Rhials/tgstation)@[41f20bc3ce...](https://github.com/Rhials/tgstation/commit/41f20bc3ced4e7853a09f2d5e1dcf46346f2e51f)
#### Thursday 2023-07-20 14:47:19 by LemonInTheDark

[MDB IGNORE] Angled Lights & Lighting Prototyping Tool  (#74365)

## About The Pull Request

Hello friends, I've been on a bit of a lighting kick recently, and I
decided I clearly do not have enough things to work on as it is.
This pr adds angle support to static lights, and a concepting/debug tool
for playing with lights on a map.

Let's start from first principles yeah?

### Why Angled Lights?

Mappers, since they can't actually see a light's effect in editor, tend
to go off gut.
That gut is based more off what "makes sense" then how things actually
work
This means they'll overplace light sources, and also they tend to treat
lights, particularly light "bars" (the bigger ones) as directional.
So you'll have two lights on either sides of a pillar, lights inside a
room with lights outside pointing out, etc.


![image](https://user-images.githubusercontent.com/58055496/228785032-63b86120-ea4c-4e52-b4e8-40a4b61e5bbc.png)

This has annoying side effects. A lot of our map is overlit, to the
point that knocking out a light does.... pretty much nothing.
I find this sad, and would like to work to prevent it. I think dark and
dim, while it does not suit the normal game, is amazing for vibes, and I
want it to be easier to see that.

Angled lights bring how lights work more in line with how mappers expect
lights work, and avoids bleedover into rooms that shouldn't be bled
into, working towards that goal of mine.

### How Angled Lights?

This is more complex then you'd first think so we'll go step by step


![image](https://user-images.githubusercontent.com/58055496/228786117-d937b408-9bc2-4066-9aee-aae21b047151.png)

Oh before we start, some catchup from the last time I touched lighting
code.
Instead of doing a lighting falloff calculation for each lighting corner
(a block that represents the resolution of our lights) in view we
instead generate cached lightsheets. These precalculate and store all
possible falloffs for x and y distances from a source.

This is very useful for angle work, since it makes it almost totally
free.
 
Atoms get 2 new values. light_angle and light_dir
Light angle is the angle the light uses, and light_dir is a cardinal
direction it displays in

We take these values, and inside sheetbuilding do some optional angle
work. getting the center angle, the angle of a pair of coords, and then
the delta between them.
This is then multiplied against the standard falloff formula, and job
done.

We do need some extra fenangling to make this all work nicely tho.

We currently use a pixel turf var stored on the light source to do
distance calculations.
This is the turf we pretend the light source is on for visuals, most
often used to make wall lights work nice.
The trouble is it's not very granular, and doesn't always have the
effect you might want.

So, instead of generating and storing a pixel turf to do our distance
calculations against, we store x and y offset variables.
We use them to expand our working range and sheet size to ensure things
visually make sense, and then offset any positions by them.

I've added a way for sources to have opinions on their offsets too, and
am using them for wall lights.
This ensures the angle calculations don't make the wall behind a light
fulldark, which would be silly.

### Debug Tool?

In the interest of helping with that core problem, lights being complex
to display, I've added a prototyping tool to the game.
It's locked behind mapping verbs, and works about like this.

Once the verb is activated, it iterates over all the sources in the
world (except turfs because those are kinda silly), outlining and
"freezing" them, preventing any future changes.
Then, it adds 3 buttons to the owners of a light source.

![image](https://user-images.githubusercontent.com/58055496/228776539-4b1d82af-1244-4ed6-8754-7f07e3e47cda.png)
The first button toggles the light on and off, as desired.
The third allows you to move the source around, with a little targeting
icon replacing your mouse
The second tho, that's more interesting.

The second button opens a debug menu for that light

![image](https://user-images.githubusercontent.com/58055496/228777811-ae620588-f08a-4b50-93a0-beea593aea77.png)
There's a lot here, let's go through it.

Bit on the left is a list of templates, which allow you to sample
existing light types (No I have no idea why the background is fullwhite,
need to work on that pre merge)
You can choose one by clicking it, and hitting the upload button.

This replaces your existing lighting values with the template's,
alongside replacing its icon and icon state so it looks right.
There are three types as of now, mostly for categorization. Bar, which
are the larger typically stronger lights, Bulb, which are well, bulbs,
and Misc which could be expanded, but currently just contains floor
lights.

Alongside that you can manually edit the power, range, color and angle
of the focused light.
I also have support for changing the direction of the light source,
since anything that uses directional lighting would also tie light dir
to it.
This isn't *always* done tho, so I should maybe find a way to edit light
dir too.

My hope is this tool will allow for better concepting of a room's
lights, and easier changing of individual object's light values to suit
the right visuals.

### Lemon No Why What

Ok so I applied angle lights to bars and bulbs, which means I am
changing the lighting of pretty much every map in the codebase.
I'm gonna uh, go check my work.

Alongside this I intend to give lighting some depth. So if there's room
to make a space warmer, or highlight light colors from other sources, I
will do that.

(Images as examples)

![image](https://user-images.githubusercontent.com/58055496/228786801-111b6493-c040-4199-ab99-ac1c914d034c.png)

I also want to work on that other goal of mine, making breaking lights
matter. So I'll be doing what I can to ensure you only need to break one
light to make a meaningful change in the scene.

This is semi complicated by one light source not ever actually reaching
fullbright on its own, but we do what we must because we can.


![image](https://user-images.githubusercontent.com/58055496/228786483-b7ad6ecd-874f-4d90-b5ca-6ef78cb70d2b.png)

I'm as I hope you know biased towards darker spaces, I think contrast
has vibes.
In particular I do not think strong lights really suit maintenance. 

Most of what is used there are bulbs, so I'm planning on replacing most
uses with low power bulbs, to keep light impacts to rooms, alongside
reducing the amount of lights placed in the main tunnels


![image](https://user-images.githubusercontent.com/58055496/228786594-c6d7610c-611e-478b-bcba-173ebf4c4b12.png)

**If you take issue with this methodology please do so NOW**, I don't
want to have to do another pass over things.
Oh also I'm saving station maps for last since ruins are less likely to
get touched in mapping march and all.

### Misc + Finishing Thoughts

Light templates support mirroring vars off typepaths using a subtype,
which means all the templates added here do not require updating if the
source type changes somehow. I'd like to expand the template list at
some point, perhaps in future.

I've opened this as a draft to make my intentions to make my changes to
lights known, and to serve as motivation for all the map changes I need
to do.

### Farish Future

I'm unhappy with how we currently configure lights. I would like a
system that more directly matches the idea of drawing falloff curves,
along with allowing for different falloffs for different colors,
alongside extending the idea to angle falloff.
This would make out of engine lighting easier, allow for nicer looking
lights (red to pink, blue to purple, etc), and improve accessibility by
artists.

This is slightly far off, because I have other obligations and it's
kinda complicated, but I'd like to mention it cause it's one of my many
pipedreams.

## Changelog
:cl:
add: Added angle lighting, applies it to most wall lights!
add: Adds a lighting prototyping tool, mappers go try it out (it's
locked behind the mapping verb)
/:cl:

---------

Co-authored-by: MMMiracles <lolaccount1@hotmail.com>

---
## [Faehn/Piscine-In-Belgium](https://github.com/Faehn/Piscine-In-Belgium)@[b20daa9509...](https://github.com/Faehn/Piscine-In-Belgium/commit/b20daa9509d439ea6a20b600f419d416a0b68fdf)
#### Thursday 2023-07-20 15:07:56 by Barth

Okay, I fixed the 80 columns lines thing in ex06 but HOLY SHIT was that annoying, I did NOT manage to do it without declaring a subfunction. Although I will say, that sub function might be pretty useful so I'm not mad I made it

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[7e29b9ef63...](https://github.com/TaleStation/TaleStation/commit/7e29b9ef63fa1674b30e1b3298d7aef8e9c1805b)
#### Thursday 2023-07-20 16:01:32 by TaleStationBot

[MIRROR] [MDB IGNORE] Adds a new positive quirk, "Spacer Born".  (#6840)

Original PR: https://github.com/tgstation/tgstation/pull/76809
-----
## About The Pull Request

Adds a new 7 point positive quirk, "Spacer Born". Totally not inspired
by The Expanse, don't look at the branch name.

You were born in space, rather than on a planet, so your physiology has
adapted differently.
You are more comfortable in space, and way less comfortable on a planet.

Benefits:
   - You are slightly taller. (No mechanical effect)
   - You take 20% less damage from pressure damage.
   - You take 20% less damage from cold environments. 
- You move 10% faster while floating (NOT drifting, this is zero gravity
movement while beside a wall).
- You drift 20% faster (Drifting through zero gravity, untethered to
anything)
- While in space (z-level-wise, not turf wise), you lose some disgust
overtime.
- While experiencing no-gravity for an extended period of time, you will
start regenerating stamina and reduce stuns at a very low rate.
- If you are assigned to shaft miner (or the map is Icebox), you are
awarded with a 25% wage bonus (hazard pay).

Downsides:
- While on a planet (Yes, this includes Icebox and planetary maps), you
gain gravity sickness:
- Passive accrue disgust (slightly lessened on Icebox) (Capped at low
levels)
      - Choking, after extended periods (disabled on Icebox)
      - Slower movement 
      - Weaker stamina (disabled on Icebox)
- Suffocation from extended periods (disabled on Icebox) (Lungs aren't
adapted)
      - Mood debuff

(Effects not final)

## Why It's Good For The Game

I'd figure I throw my hat in with the Positive Quirk Curse. 

This is a quirk that improves your ability in a niche circumstance (low
gravity / dangerous pressure), with some downsides that are only
generally in effect if you play a few roles (or it's Icebox).

Because of this I think it'll provide an interesting niche, where Spacer
Born engineers are slightly better than their counterparts due to their
origin (moving faster in space without a jetpack, withstanding
pressure). However, at the same time, if the mining outpost sustains
damage and needs repairs... suddenly your buff over your cohorts
disappears, and you have to brave somewhere hostile to your body.

Ultimately, the goal of the quirk is to encourage people to approach
situations a bit differently.
Or take it as a challenge and play shaft miner. 

## Changelog

:cl: Melbert
add: Adds a new 7 point positive quirk, "Spacer Born". You were born in
space, and as a result your body's adapted to life in artificial
gravity, making you much more effective and comfortable in lower
gravity. However, travelling planet-side is quite a chore, especially if
you're assigned to work there.
add: Adds a chemical: Ondansetron, created by Oil + Nitrogen + Oxygen +
Ethanol catalyst. A powerful Antiemetic (lowers disgust).
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [hanwen/git](https://github.com/hanwen/git)@[07f91e5e79...](https://github.com/hanwen/git/commit/07f91e5e79810a8f17de745d2d84c384add75f0a)
#### Thursday 2023-07-20 16:37:39 by Jeff King

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
## [AdMerk-Corp-Inc/admerkBackend](https://github.com/AdMerk-Corp-Inc/admerkBackend)@[67ba9e1894...](https://github.com/AdMerk-Corp-Inc/admerkBackend/commit/67ba9e1894385248b443410a5b594319e8d27916)
#### Thursday 2023-07-20 16:55:49 by Ahmad Malik

Merge pull request #3 from AdMerk-Corp-Inc/arslan/search-route

fuck you

---
## [kemboi-73/HackerRank_30_Days_of_Code_Challenge-](https://github.com/kemboi-73/HackerRank_30_Days_of_Code_Challenge-)@[7d5ea4b41d...](https://github.com/kemboi-73/HackerRank_30_Days_of_Code_Challenge-/commit/7d5ea4b41df766e75857de8e460a3f3ee9a00e53)
#### Thursday 2023-07-20 17:33:05 by Mikey_254

Day 25: Running Time and Complexity.py

First, we use some magical math tools that someone created for us called "math" to help us out. We need it for square root calculations.

Then, we have a special function called "isPrime(n)" that will do the magic for us. It's like having a friendly wizard who can tell us if a number is prime or not.

The "def isPrime(n):" part tells the computer that we're going to create a new function called "isPrime." Inside the function, we check if the number "n" is less than or equal to 1. If it is, then it's not a prime number, and we return "False" to say it's not prime.

Next, we use the magical math tool to find the square root of "n" and save it as "sqrt_n." A square root is like finding the number that, when multiplied by itself, gives us "n."

If "sqrt_n" turns out to be a whole number (like 4 or 9), it means "n" is not a prime number, because it has other factors besides 1 and itself. So we return "False" again.

After that, we use a cool loop that goes through all the numbers from 2 to the square root of "n" (rounded up to the nearest whole number). This loop helps us check if there are any other numbers (besides 1 and "n") that can divide "n" evenly. If we find any, it means "n" is not prime, and we return "False" once more.

But if we go through the loop without finding any other numbers that can divide "n," then "n" must be a prime number! So, we return "True" to show it's prime.

Now, let's use our magical "isPrime" function in the main part of the code:

We first ask you to tell us how many numbers you want to check. You give us that number, and we call it "num_test_cases."

Then, we have a loop that runs "num_test_cases" times. Each time it goes through the loop, we ask you to give us a number ("n") to check if it's prime or not.

We use our magical "isPrime" function to check if the number you gave us is prime or not. If it's prime, we print "Prime" to celebrate! 🎉 If it's not prime, we print "Not prime" to let you know.

---
## [DATA-xPUNGED/DataStation](https://github.com/DATA-xPUNGED/DataStation)@[f2ec16c1e6...](https://github.com/DATA-xPUNGED/DataStation/commit/f2ec16c1e6485bdf2035837fb3d42de24900e8b4)
#### Thursday 2023-07-20 17:36:19 by Vekter

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
## [Contrabang/tgstation](https://github.com/Contrabang/tgstation)@[8c2c72b0ed...](https://github.com/Contrabang/tgstation/commit/8c2c72b0ed7a1fad112fc4da8a8b7de7faa5e114)
#### Thursday 2023-07-20 17:56:06 by LemonInTheDark

Duiffel Spotfix (#76442)

## About The Pull Request

Gives duffelbags their proper slot count
They inherited this from backpacks, but I sorta just forgot about that

[Creates "levels" of locked objects, uses that to make locked duffels
work](https://github.com/tgstation/tgstation/pull/76442/commits/c613c00f62fa3ff03bb33737d24da9acbf2050e3)

[c613c00](https://github.com/tgstation/tgstation/pull/76442/commits/c613c00f62fa3ff03bb33737d24da9acbf2050e3)

Turns locked into something that holds defines, this makes life a lot
easier.
Requires a lot of boilerplate because of how many uses of these procs
there are and all the passthrough and shit.

Adds a few outfit subtypes to avoid this class of failure in future.

Renames the args in a few but not all touched procs, one thing at a time

Closes #76407
Closes #76430 Had the lock check in the wrong place
Closes #76441 GOD I HATE TK SO MUCH

Wrote half the pr without glasses so if it's weird gimme some grace
yeah?

## Changelog
:cl:
fix: Fixes some fuck with duffelbags, them not holding enough + issues
with spawning gear in them (job shit and all)
/:cl:

---
## [Contrabang/tgstation](https://github.com/Contrabang/tgstation)@[d85e44c69c...](https://github.com/Contrabang/tgstation/commit/d85e44c69cc06dbeeb3a0de7f76273de45ee3893)
#### Thursday 2023-07-20 17:56:06 by ChungusGamer666

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
## [Citadel-Station-13/Citadel-Station-13-RP](https://github.com/Citadel-Station-13/Citadel-Station-13-RP)@[4966352d14...](https://github.com/Citadel-Station-13/Citadel-Station-13-RP/commit/4966352d145c9fcacad823f7dc8d6a52fc82c953)
#### Thursday 2023-07-20 17:58:48 by Mazian

changes the open simulated turf to be SOMETHING NOT HORRIBLY EYE SEARING (#5735)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

makes turf/simulated/open blue. resets on init.

## Why It's Good For The Game

holy FUCKING SHIT my eyes HATE WHOEVER DECIDED IT SHOULD BE MISSING
TEXTURE PINK.

---
## [teresaqhoang/semantic-kernel](https://github.com/teresaqhoang/semantic-kernel)@[eab7a8f63a...](https://github.com/teresaqhoang/semantic-kernel/commit/eab7a8f63a0bfd289070e82b423ac78bd306ee5b)
#### Thursday 2023-07-20 19:23:29 by Sailesh R

Python: implemented web search engine skill with bing connector (#1813)

### Motivation and Context
<!-- Thank you for your contribution to the semantic-kernel repo!
Please help reviewers and future users, providing the following
information:
  1. Why is this change required?
  2. What problem does it solve?
  3. What scenario does it contribute to?
  4. If it fixes an open issue, please link to the issue here.
-->
In this PR, I have tried my hand at an implementation of web search
engine skill in python semantic kernel using the Bing Web Search API.

### Description
<!-- Describe your changes, the overall approach, the underlying design.
These notes will help understanding how your code works. Thanks! -->
In the semantic kernel directory, I have added a new directory called
web_skills (To replicate Skills.Web from C#) and added the web search
skill here. For now, I have implemented web search using the bing web
search API. If this approach is fine, then I can implement the same with
the google search API too. I have tried to stick with similar naming
conventions as used in the C# implementation with matching context
parameters and arguments.

I can also add some unit tests for the connectors and the search skill,
and add something like exponential backoff to avoid rate limit errors
while querying the search APIs.

Here is some sample code that checks the working of the search skill.

```python
import os
import semantic_kernel as sk
from semantic_kernel.web_skills.web_search_engine_skill import WebSearchEngineSkill
from semantic_kernel.web_skills.connectors import BingConnector
from semantic_kernel.connectors.ai.open_ai import OpenAITextCompletion

async def main():
    kernel = sk.Kernel()
    api_key, org_id = sk.openai_settings_from_dot_env()
    kernel.add_text_completion_service(
        "dv", OpenAITextCompletion("text-davinci-003", api_key, org_id)
    )
    connector = BingConnector(api_key=os.getenv("BING_API_KEY"))
    web_skill = kernel.import_skill(WebSearchEngineSkill(connector), "WebSearch")

    prompt = "Who is Leonardo DiCaprio's current girlfriend?"
    search_async = web_skill["searchAsync"]
    result = await search_async.invoke_async(prompt)
    print(result)

    """
    Output:
    ["Celebrity Celebrity News Everything You Need to Know About Leonardo DiCaprio and Camila Morrone's Relationship From the beginning of their romance to today, we track their relationship here. By..."]
    """

    prompt = """
    Answer the question using only the data that is provided in the data section. Do not use any prior knowledge to answer the question.
    Data: {{WebSearch.SearchAsync "What is semantic kernel?"}}
    Question: What is semantic kernel?
    Answer:
    """

    qna = kernel.create_semantic_function(prompt, temperature=0.2)
    context = kernel.create_new_context()
    context["count"] = "10"
    context["offset"] = "0"
    result = await qna.invoke_async(context=context)
    print(result)

    """
    Output:
    Semantic Kernel is an open-source SDK that lets you easily combine AI services like OpenAI, Azure OpenAI, and Hugging Face with conventional programming languages like C# and Python. By doing so, you can create AI apps that combine the best of both worlds. Semantic Kernel is at the center of the copilot stack.
    """

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

### Contribution Checklist
<!-- Before submitting this PR, please make sure: -->
- [x] The code builds clean without any errors or warnings
- [x] The PR follows SK Contribution Guidelines
(https://github.com/microsoft/semantic-kernel/blob/main/CONTRIBUTING.md)
- [x] The code follows the .NET coding conventions
(https://learn.microsoft.com/dotnet/csharp/fundamentals/coding-style/coding-conventions)
verified with `dotnet format`
- [ ] All unit tests pass, and I have added new tests where possible
- [x] I didn't break anyone :smile:

---------

Co-authored-by: Abby Harrison <54643756+awharrison-28@users.noreply.github.com>
Co-authored-by: Abby Harrison <abby.harrison@microsoft.com>

---
## [prince22a47/photographer](https://github.com/prince22a47/photographer)@[b9ccec833c...](https://github.com/prince22a47/photographer/commit/b9ccec833c1bf07b1c51edf9be14df8fd4f462a1)
#### Thursday 2023-07-20 21:05:53 by prince22a47

Add files via upload

Crazy Life" is an interactive text-based game that simulates the unpredictable journey of life. As the player, you will take on the role of a character and navigate through various scenarios, making choices that will shape the course of their life. The game aims to depict the complexity of life decisions, where each choice has its consequences, and no path is guaranteed to be the best.

Upon starting the game, you are introduced to your character, who begins with initial attributes such as health, wealth, and happiness. The goal is to keep these attributes as balanced as possible, avoiding any extreme highs or lows. The character's health represents their physical well-being, wealth indicates their financial stability, and happiness reflects their emotional state.

Throughout the game, you will encounter different options to choose from, each with its advantages and drawbacks. For instance, going to the gym will improve your character's health but may cost money and slightly decrease happiness. Working overtime will increase wealth but may lead to stress and reduced happiness. Going on vacation might boost happiness but will require spending money and might negatively affect health.

As you progress through the game, your decisions will impact your character's attributes. You must carefully consider the consequences of each choice to ensure a well-rounded life. The game also incorporates an element of randomness, adding unpredictability to the outcomes of certain choices.

The journey continues until your character's health or happiness reaches zero, leading to different game over scenarios. If health reaches zero, the journey ends tragically, illustrating the importance of maintaining physical well-being. Alternatively, if happiness drops to zero, the character's inability to find joy in life brings their journey to an end, highlighting the significance of emotional well-being.

The "Crazy Life" game serves as both entertainment and a reflection of real-life decision-making. It encourages players to consider the trade-offs they face in their own lives and understand the significance of maintaining a balanced and fulfilling existence.

Note: This extended description adds context to the game's purpose and mechanics, emphasizing the value of balanced decision-making and the impact of choices on the character's life journey. Players are encouraged to explore different paths and reflect on the outcomes of their decisions in the game.

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[3d75faa12d...](https://github.com/git-for-windows/git/commit/3d75faa12d720b29b815bdee16ad770704438093)
#### Thursday 2023-07-20 21:17:20 by Johannes Schindelin

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
## [KenAdeniji/WordEngineering](https://github.com/KenAdeniji/WordEngineering)@[ee747cb424...](https://github.com/KenAdeniji/WordEngineering/commit/ee747cb424d597eccccc53feae58a9f9880c93a8)
#### Thursday 2023-07-20 21:21:37 by Ken Adeniji

Wessne Gebremedhin
Home phone: (415) 845-3010
Mobile phone: (415) 595-4041
Home address: P.O. Box 5414, Berkeley, California (CA) 94705, United States of America (USA)
Company: Wessne Janitorial Service
Work e-mail: WessneJanitorial@hotmail.com
Work phone: (415) 437-1730
Work address: 713 El Cerritto Plaza, El Cerritto, California (CA) 94530, United States of America (USA)
Other e-mail: 2f2af8821224379cb62f11420f5b1c99@job.craigslist.org
Website: neat-cleaning.com
Notes
2023-07-20T11:48:00
I will develop me ... as part of me.
At the intersection of Siward Drive and Creekwood Drive, North West. Creekwood Terrace. At North East olive green car, white covering canopy, orange branches sticks at the Center.
2023-07-20T09:41:00
Facing the storm.
Facing the sun.
Between Coliseum and San Leandro urine.

2023-07-20T09:41:00
User friendly.
Request form.
How many classrooms, bathrooms?
Nora Torres, Hispanic interviewer.
Sybase/Powersoft Need education.
Alex 	Koutsombos 			International Business Machine (IBM) 	Post-dated 2023-07-20T11:58:00
Free consulting?
Mailing list Java.
Office at West of CVS, upstairs, 2nd floor, second floor.

2023-07-20T08:02:00
Keep the Passover ... and the entreat of it.
Hayward BART Station going to Daly City.
12:26 Garage heater noise. Caucasian female with blond hair said, See you brother. 12:35 WessmeJanitorial@hotmail.com Microsoft Windows operating system clipboard copy paste error garage heater noise.

2023-07-20T08:02:00
I don't want my own creditability ...
I don't want my own creditability ... linked to that. 12:07 Record head scalp hair, lips.
Union City BART Station
2023-07-20T10:00:00 Thursday
Interview appointment

2023-07-14T15:28:00 Friday
ancestry.com/name-origin?surname=gebremedhin
Gebremedhin Name Meaning
Ethiopian (also Gebre Medhin): from the personal name Gebre Medhin which has the Christian religious meaning 'servant of the Savior' (see Gebre ). — Note: Since Ethiopians do not have hereditary surnames this name was registered as such only after immigration of its bearers to the US.

2023-07-14T14:55:00 Friday
Introduction for website, one-off work.
Craig Graves, Vice President, at 415-437-1730

2023-07-06T00:00:00
http://sfbay.craigslist.org/eby/web/d/el-cerrito-it-and-web-development/7640459890.html
    SF bay area
    east bay
    web/html/info design
Posted 8 days ago
IT and Web Development Professional Wanted (berkeley)
Wessnejanitorial

compensation: IT and Web Development Professional Wanted
employment type: employee's choice
job title: IT and Web Development Professional Wanted
IT and Web Development Professional Wanted

We are a well-established company seeking an experienced individual to join our team in both IT support and web development capacities. If you have a passion for technology, strong problem-solving skills, and expertise in web development, this opportunity is for you.

Position Details:

Full-time position, Monday through Friday
Competitive salary and benefits package
Responsibilities:
IT Support:

Provide technical support for computer systems, software, and networks
Install, configure, and maintain hardware and software components
Troubleshoot and resolve IT-related issues for employees
Web Development:

Design, develop, and maintain websites and web applications
Implement front-end and back-end functionalities
Optimize website performance and user experience
Collaborate with cross-functional teams to ensure project success
Skills & Qualifications:

Solid experience in IT support and troubleshooting
Proficiency in hardware and software installation and maintenance
Strong knowledge of web development technologies such as HTML, CSS, JavaScript, and relevant frameworks (e.g., React, Angular, Node.js)

Familiarity with content management systems (CMS) and e-commerce platforms
Understanding of web hosting, server management, and domain configuration
Excellent problem-solving and analytical abilities
Strong communication and collaboration skills

To Apply:
Please submit your comprehensive resume, portfolio, and any relevant project examples that demonstrate your IT support and web development expertise. Include at least three professional references who can speak to your skills and experience.

To inquire about the position or discuss further details, please call Wessne at 415-595-4041.
post id: 7640459890

---
## [jughu/tgstation](https://github.com/jughu/tgstation)@[8788e48378...](https://github.com/jughu/tgstation/commit/8788e483788db2432b9649313efc9426d324379f)
#### Thursday 2023-07-20 21:40:18 by Time-Green

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
## [Citadel-Station-13/Citadel-Station-13-RP](https://github.com/Citadel-Station-13/Citadel-Station-13-RP)@[a14ef07eb6...](https://github.com/Citadel-Station-13/Citadel-Station-13-RP/commit/a14ef07eb69a49feeae9c331609adc393f861b5b)
#### Thursday 2023-07-20 21:40:46 by Nut2

Triumph central command floor fix (#5741)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
I MISSED TWO FUCKING TILES
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
I MISSED TWO TILES GOD DAMNIT
<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

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

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [mietek/mame](https://github.com/mietek/mame)@[4a5b8a415f...](https://github.com/mietek/mame/commit/4a5b8a415fee66df01d57b871a8025d0f1f1a2f6)
#### Thursday 2023-07-20 22:17:10 by wilbertpol

msx1_cart.xml: Added fourteen working items. (#11412)

* Removed Hopper (Europe) tape-to-cartridge hack.
* Demoted The Holy Quran (v1.00) to not working.

New working software list items (msx1_cart.xml)
-------------------------------
Hole in One Professional (Japan, alt 2) [file-hunter]
Hole in One Professional (Japan, alt 3) [file-hunter]
Hot-Asm (Brazil) [file-hunter]
Hot-Plan (Brazil) [file-hunter]
Hydlide II - Shine of Darkness (Korea) [file-hunter]
Hopper (Arab) [file-hunter]
Hans' Adventure (v1.1) [MSXDev]
Hans' Adventure (v1.0) [MSXDev]
Happy Halloween [Clube MSX]
Happy Square Christmas [303bcn]
Heart Stealer 2 [MSXDev]
Heroes Arena [MSXDev]
Hose Diogo Martinez: The Bussas Quest [MSXDev]
How Many Are The Dumbbells You Lift? [cobinee]

---
## [facebook/sapling](https://github.com/facebook/sapling)@[fdb0a74c0a...](https://github.com/facebook/sapling/commit/fdb0a74c0a8e434b1fa1e70df1bf2ac2ef19e952)
#### Thursday 2023-07-20 22:21:38 by Evan Krause

Add open file button to comparison view

Summary:
A couple of small changes to the comparison view

- add a button that opens the file. (we had this on each line, but if you're not viewing a comparison against head, those line numbers don't line up... so we disallow per line file open but add a button at the header for opening the file in general)
- change the title text to an actual tooltip for copying the path. The title text took too long to appear, the tooltip is a much smoother experience
- shorten commit hash in comparison name

Note that this whole component is made with the Primer design system. Eventually I think we should scrap this and rebuild it with our new comparison view being used for split/partial commit. It's really weird to have a totally different design system that we have to load in.
We're not even sharing with reviewstack.dev, there's really no point in using it in this way.

Reviewed By: quark-zju

Differential Revision: D47600367

fbshipit-source-id: e0335cab2c150370c0663e32950a600ed2cda5d9

---
## [Lantianyou/next.js](https://github.com/Lantianyou/next.js)@[6238f8a5c0...](https://github.com/Lantianyou/next.js/commit/6238f8a5c0ffabb7dfb35872c52c942ed7f148da)
#### Thursday 2023-07-20 22:25:44 by Jimmy Lai

performance: don't compile on hover on dev (#51830)

An annoying issue that slows down compilation times in dev for Next is
that we might trigger compilation of a page via hover on app.

We do this because we want the same experience in production and dev and
the prefetching is important for instantaneous loading states.

The alternative in this PR is that we don't prefetch at all anymore in
dev but instead, when we handle navigation, we can force a prefetch
navigation.

The slight compromise with this approach is that you can't test
prefetching anymore in dev.


<!-- Thanks for opening a PR! Your contribution is much appreciated.
To make sure your PR is handled as smoothly as possible we request that
you follow the checklist sections below.
Choose the right checklist for the change(s) that you're making:

## For Contributors

### Improving Documentation

- Run `pnpm prettier-fix` to fix formatting issues before opening the
PR.
- Read the Docs Contribution Guide to ensure your contribution follows
the docs guidelines:
https://nextjs.org/docs/community/contribution-guide

### Adding or Updating Examples

- The "examples guidelines" are followed from our contributing doc
https://github.com/vercel/next.js/blob/canary/contributing/examples/adding-examples.md
- Make sure the linting passes by running `pnpm build && pnpm lint`. See
https://github.com/vercel/next.js/blob/canary/contributing/repository/linting.md

### Fixing a bug

- Related issues linked using `fixes #number`
- Tests added. See:
https://github.com/vercel/next.js/blob/canary/contributing/core/testing.md#writing-tests-for-nextjs
- Errors have a helpful link attached, see
https://github.com/vercel/next.js/blob/canary/contributing.md

### Adding a feature

- Implements an existing feature request or RFC. Make sure the feature
request has been accepted for implementation before opening a PR. (A
discussion must be opened, see
https://github.com/vercel/next.js/discussions/new?category=ideas)
- Related issues/discussions are linked using `fixes #number`
- e2e tests added
(https://github.com/vercel/next.js/blob/canary/contributing/core/testing.md#writing-tests-for-nextjs
- Documentation added
- Telemetry added. In case of a feature if it's used or not.
- Errors have a helpful link attached, see
https://github.com/vercel/next.js/blob/canary/contributing.md


## For Maintainers

- Minimal description (aim for explaining to someone not on the team to
understand the PR)
- When linking to a Slack thread, you might want to share details of the
conclusion
- Link both the Linear (Fixes NEXT-xxx) and the GitHub issues
- Add review comments if necessary to explain to the reviewer the logic
behind a change

### What?

### Why?

### How?

Closes NEXT-
Fixes #

-->

link NEXT-1317

---
## [Hedges/yuzu](https://github.com/Hedges/yuzu)@[8e703e08df...](https://github.com/Hedges/yuzu/commit/8e703e08dfcf735a08df2ceff6a05221b7cc981f)
#### Thursday 2023-07-20 23:04:53 by comex

Implement SSL service

This implements some missing network APIs including a large chunk of the SSL
service, enough for Mario Maker (with an appropriate mod applied) to connect to
the fan server [Open Course World](https://opencourse.world/).

Connecting to first-party servers is out of scope of this PR and is a
minefield I'd rather not step into.

 ## TLS

TLS is implemented with multiple backends depending on the system's 'native'
TLS library.  Currently there are two backends: Schannel for Windows, and
OpenSSL for Linux.  (In reality Linux is a bit of a free-for-all where there's
no one 'native' library, but OpenSSL is the closest it gets.)  On macOS the
'native' library is SecureTransport but that isn't implemented in this PR.
(Instead, all non-Windows OSes will use OpenSSL unless disabled with
`-DENABLE_OPENSSL=OFF`.)

Why have multiple backends instead of just using a single library, especially
given that Yuzu already embeds mbedtls for cryptographic algorithms?  Well, I
tried implementing this on mbedtls first, but the problem is TLS policies -
mainly trusted certificate policies, and to a lesser extent trusted algorithms,
SSL versions, etc.

...In practice, the chance that someone is going to conduct a man-in-the-middle
attack on a third-party game server is pretty low, but I'm a security nerd so I
like to do the right security things.

My base assumption is that we want to use the host system's TLS policies.  An
alternative would be to more closely emulate the Switch's TLS implementation
(which is based on NSS).  But for one thing, I don't feel like reverse
engineering it.  And I'd argue that for third-party servers such as Open Course
World, it's theoretically preferable to use the system's policies rather than
the Switch's, for two reasons

1. Someday the Switch will stop being updated, and the trusted cert list,
   algorithms, etc. will start to go stale, but users will still want to
   connect to third-party servers, and there's no reason they shouldn't have
   up-to-date security when doing so.  At that point, homebrew users on actual
   hardware may patch the TLS implementation, but for emulators it's simpler to
   just use the host's stack.

2. Also, it's good to respect any custom certificate policies the user may have
   added systemwide.  For example, they may have added custom trusted CAs in
   order to use TLS debugging tools or pass through corporate MitM middleboxes.
   Or they may have removed some CAs that are normally trusted out of paranoia.

Note that this policy wouldn't work as-is for connecting to first-party
servers, because some of them serve certificates based on Nintendo's own CA
rather than a publicly trusted one.  However, this could probably be solved
easily by using appropriate APIs to adding Nintendo's CA as an alternate
trusted cert for Yuzu's connections.  That is not implemented in this PR
because, again, first-party servers are out of scope.

(If anything I'd rather have an option to _block_ connections to Nintendo
servers, but that's not implemented here.)

To use the host's TLS policies, there are three theoretical options:

a) Import the host's trusted certificate list into a cross-platform TLS
   library (presumably mbedtls).

b) Use the native TLS library to verify certificates but use a cross-platform
   TLS library for everything else.

c) Use the native TLS library for everything.

Two problems with option a).  First, importing the trusted certificate list at
minimum requires a bunch of platform-specific code, which mbedtls does not have
built in.  Interestingly, OpenSSL recently gained the ability to import the
Windows certificate trust store... but that leads to the second problem, which
is that a list of trusted certificates is [not expressive
enough](https://bugs.archlinux.org/task/41909) to express a modern certificate
trust policy.  For example, Windows has the concept of [explicitly distrusted
certificates](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn265983(v=ws.11)),
and macOS requires Certificate Transparency validation for some certificates
with complex rules for when it's required.

Option b) (using native library just to verify certs) is probably feasible, but
it would miss aspects of TLS policy other than trusted certs (like allowed
algorithms), and in any case it might well require writing more code, not less,
compared to using the native library for everything.

So I ended up at option c), using the native library for everything.

What I'd *really* prefer would be to use a third-party library that does option
c) for me.  Rust has a good library for this,
[native-tls](https://docs.rs/native-tls/latest/native_tls/).  I did search, but
I couldn't find a good option in the C or C++ ecosystem, at least not any that
wasn't part of some much larger framework.  I was surprised - isn't this a
pretty common use case?  Well, many applications only need TLS for HTTPS, and they can
use libcurl, which has a TLS abstraction layer internally but doesn't expose
it.  Other applications only support a single TLS library, or use one of the
aforementioned larger frameworks, or are platform-specific to begin with, or of
course are written in a non-C/C++ language, most of which have some canonical
choice for TLS.  But there are also many applications that have a set of TLS
backends just like this; it's just that nobody has gone ahead and abstracted
the pattern into a library, at least not a widespread one.

Amusingly, there is one TLS abstraction layer that Yuzu already bundles: the
one in ffmpeg.  But it is missing some features that would be needed to use it
here (like reusing an existing socket rather than managing the socket itself).
Though, that does mean that the wiki's build instructions for Linux (and macOS
for some reason?) already recommend installing OpenSSL, so no need to update
those.

 ## Other APIs implemented

- Sockets:
    - GetSockOpt(`SO_ERROR`)
    - SetSockOpt(`SO_NOSIGPIPE`) (stub, I have no idea what this does on Switch)
    - `DuplicateSocket` (because the SSL sysmodule calls it internally)
    - More `PollEvents` values

- NSD:
    - `Resolve` and `ResolveEx` (stub, good enough for Open Course World and
      probably most third-party servers, but not first-party)

- SFDNSRES:
    - `GetHostByNameRequest` and `GetHostByNameRequestWithOptions`
    - `ResolverSetOptionRequest` (stub)

 ## Fixes

- Parts of the socket code were previously allocating a `sockaddr` object on
  the stack when calling functions that take a `sockaddr*` (e.g. `accept`).
  This might seem like the right thing to do to avoid illegal aliasing, but in
  fact `sockaddr` is not guaranteed to be large enough to hold any particular
  type of address, only the header.  This worked in practice because in
  practice `sockaddr` is the same size as `sockaddr_in`, but it's not how the
  API is meant to be used.  I changed this to allocate an `sockaddr_in` on the
  stack and `reinterpret_cast` it.  I could try to do something cleverer with
  `aligned_storage`, but casting is the idiomatic way to use these particular
  APIs, so it's really the system's responsibility to avoid any aliasing
  issues.

- I rewrote most of the `GetAddrInfoRequest[WithOptions]` implementation.  The
  old implementation invoked the host's getaddrinfo directly from sfdnsres.cpp,
  and directly passed through the host's socket type, protocol, etc. values
  rather than looking up the corresponding constants on the Switch.  To be
  fair, these constants don't tend to actually vary across systems, but
  still... I added a wrapper for `getaddrinfo` in
  `internal_network/network.cpp` similar to the ones for other socket APIs, and
  changed the `GetAddrInfoRequest` implementation to use it.  While I was at
  it, I rewrote the serialization to use the same approach I used to implement
  `GetHostByNameRequest`, because it reduces the number of size calculations.
  While doing so I removed `AF_INET6` support because the Switch doesn't
  support IPv6; it might be nice to support IPv6 anyway, but that would have to
  apply to all of the socket APIs.

  I also corrected the IPC wrappers for `GetAddrInfoRequest` and
  `GetAddrInfoRequestWithOptions` based on reverse engineering and hardware
  testing.  Every call to `GetAddrInfoRequestWithOptions` returns *four*
  different error codes (IPC status, getaddrinfo error code, netdb error code,
  and errno), and `GetAddrInfoRequest` returns three of those but in a
  different order, and it doesn't really matter but the existing implementation
  was a bit off, as I discovered while testing `GetHostByNameRequest`.

  - The new serialization code is based on two simple helper functions:

    ```cpp
    template <typename T> static void Append(std::vector<u8>& vec, T t);
    void AppendNulTerminated(std::vector<u8>& vec, std::string_view str);
    ```

    I was thinking there must be existing functions somewhere that assist with
    serialization/deserialization of binary data, but all I could find was the
    helper methods in `IOFile` and `HLERequestContext`, not anything that could
    be used with a generic byte buffer.  If I'm not missing something, then
    maybe I should move the above functions to a new header in `common`...
    right now they're just sitting in `sfdnsres.cpp` where they're used.

- Not a fix, but `SocketBase::Recv`/`Send` is changed to use `std::span<u8>`
  rather than `std::vector<u8>&` to avoid needing to copy the data to/from a
  vector when those methods are called from the TLS implementation.

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[586777c960...](https://github.com/Buildstarted/linksfordevs/commit/586777c9603072acfa7f5631d2270980b7f98d25)
#### Thursday 2023-07-20 23:11:54 by Ben Dornis

Updating: 7/20/2023 11:00:00 PM

 1. Added: Libsodium Audit Results
    (https://www.privateinternetaccess.com/blog/libsodium-audit-results/)
 2. Added: HttpRepl: A command-line tool for interacting with RESTful HTTP services - .NET Blog
    (https://devblogs.microsoft.com/dotnet/httprepl-a-command-line-tool-for-interacting-with-restful-http-services/)
 3. Added: Blazor now in official preview! - .NET Blog
    (https://devblogs.microsoft.com/dotnet/blazor-now-in-official-preview/)
 4. Added: GitHub - NightDive-Studio/shockmac: System Shock (PowerMac version / Official GPL Release)
    (https://github.com/NightDive-Studio/shockmac)
 5. Added: The Rug Puzzle: how many triangles?
    (https://youtube.com/watch?v=HViA6N3VeHw)
 6. Added: Why Your Newsfeed Sucks - Smarter Every Day 212
    (https://youtube.com/watch?v=MUiYglgGbos)
 7. Added: Adding more machine language instructions to the CPU
    (https://youtube.com/watch?v=FCscQGBIL-Y)
 8. Added: Programming my 8-bit breadboard computer
    (https://youtube.com/watch?v=9PPrrSyubG0)
 9. Added: But what is the Fourier Transform?  A visual introduction.
    (https://youtube.com/watch?v=spUNpyF58BY)
10. Added: dotnet-trace for .NET Core tracing in PerfView, SpeedScope, Chromium Event Trace Profiling, Flame graphs and more!
    (https://www.hanselman.com/blog/dotnettrace-for-net-core-tracing-in-perfview-speedscope-chromium-event-trace-profiling-flame-graphs-and-more)
11. Added: High performance IO with System.IO.Pipelines
    (https://learn.microsoft.com/en-us/shows/on-net/high-performance-io-with-systemiopipelines)
12. Added: Finding compromised passwords with 1Password | 1Password
    (https://blog.1password.com/finding-pwned-passwords-with-1password/)
13. Added: Tutorial 1: Hello World | Mina Documentation
    (https://docs.minaprotocol.com/zkapps/tutorials/hello-world)
14. Added: Why Frustum Culling Matters, and Why It's Not Important
    (https://gist.github.com/nothings/913056601b56e5719cc987684a16544e)
15. Added: Best crypto blog posts of 2017
    (https://www.cryptologie.net/article/435/best-crypto-blog-posts-of-2017/)
16. Added: .NET Core - What's Coming in .NET Core 3.0
    (https://learn.microsoft.com/en-us/archive/msdn-magazine/2018/connect/net-core-what-s-coming-in-net-core-3-0)
17. Added: The world's worst video card?
    (https://youtube.com/watch?v=l7rce6IQDWs)
18. Added: Checksums and Hamming distance
    (https://youtube.com/watch?v=ppU41c15Xho)
19. Added: Hour of Code: Anybody can Learn
    (https://code.org/learn)
20. Added: The 9 Lives of Bleichenbacher's CAT:	New Cache ATtacks on TLS Implementations | Eyal Ronen
    (https://eyalro.net/project/cat.html)
21. Added: Connecting an LCD to our computer — 6502 part 4
    (https://youtube.com/watch?v=FY3zTUaykVo)
22. Added: Glitter Bomb 1.0 vs Porch Pirates
    (https://youtube.com/watch?v=xoxhDk-hwuo)
23. Added: Oscilloscope Music - (Drawing with Sound) - Smarter Every Day 224
    (https://youtube.com/watch?v=4gibcRfp4zA)
24. Added: A first look at changes coming in ASP.NET Core 3.0 - .NET Blog
    (https://devblogs.microsoft.com/dotnet/a-first-look-at-changes-coming-in-asp-net-core-3-0/)
25. Added: DASP - Timeline of vulnerabilities
    (https://www.dasp.co/timeline.html)
26. Added: Quantum computing for the very curious
    (https://quantum.country/qcvc)
27. Added: Firefox Will Warn Users When Visiting Sites That Suffered a Data Breach
    (https://www.bleepingcomputer.com/news/security/firefox-will-warn-users-when-visiting-sites-that-suffered-a-data-breach/)
28. Added: Facebook Container Extension: Take control of how you’re being tracked | The Mozilla Blog
    (https://blog.mozilla.org/en/products/firefox/facebook-container-extension/)
29. Added: EA shares five innovations via Accessibility Patent Pledge, wants other devs to do the same
    (https://www.gamesindustry.biz/ea-shares-five-innovations-via-accessibility-patent-pledge-wants-other-devs-to-do-the-same)
30. Added: “Hello, world” from scratch on a 6502 — Part 1
    (https://youtube.com/watch?v=LnzuMJLZRdU)
31. Added: Ben Eater - 8 bit breadboard computer (with changes)
    (https://youtube.com/watch?v=PieFUmjG0do)
32. Added: World's worst video card? The exciting conclusion
    (https://youtube.com/watch?v=uqY3FMuMuRo)
33. Added: The case against Net Neutrality?
    (https://youtube.com/watch?v=hKD-lBrZ_Gg)
34. Added: PBR Textures, free for any purpose
    (https://www.cgbookcase.com/)
35. Added: Making a computer Turing complete
    (https://youtube.com/watch?v=AqNDk_UJW4k)
36. Added: 8-bit CPU control logic: Part 3
    (https://youtube.com/watch?v=dHWFpkGsxOs)
37. Added: Announcing ASP.NET Core 2.2, available today! - .NET Blog
    (https://devblogs.microsoft.com/dotnet/asp-net-core-2-2-available-today/)
38. Added: Error detection: Parity checking
    (https://youtube.com/watch?v=MgkhrBSjhag)
39. Added: Simulating Supply and Demand
    (https://youtube.com/watch?v=PNtKXWNKGN8)
40. Added: stb/stb_easy_font.h at master · nothings/stb
    (https://github.com/nothings/stb/blob/master/stb_easy_font.h)
41. Added: Narrated explorables: three mental models
    (https://medium.com/khan-academy-early-product-development/narrated-explorables-three-mental-models-e16e0d80e4c1)
42. Added: If You Don't Understand Quantum Physics, Try This!
    (https://youtube.com/watch?v=Usu9xZfabPM)
43. Added: 1 Introduction · Real-World Cryptography
    (https://livebook.manning.com/#!/book/real-world-cryptography/chapter-1/v-1/)
44. Added: Introduction to Razor Pages in ASP.NET Core
    (https://learn.microsoft.com/en-us/aspnet/core/razor-pages/?view=aspnetcore-7.0)
45. Added: Download .NET Core 2.1 (Linux, macOS, and Windows)
    (https://dotnet.microsoft.com/en-us/download/dotnet/2.1)
46. Added: Assembly language vs. machine code — 6502 part 3
    (https://youtube.com/watch?v=oO8_2JJV0B4)
47. Added: Reliable data transmission
    (https://youtube.com/watch?v=eq5YpKHXJDM)
48. Added: How do CRCs work?
    (https://youtube.com/watch?v=izG7qT0EpBw)
49. Added: How do CPUs read machine code? — 6502 part 2
    (https://youtube.com/watch?v=yl8vPW5hydQ)
50. Added: 8-bit CPU control signal overview
    (https://youtube.com/watch?v=AwUirxi9eBg)
51. Added: stb/docs/stb_voxel_render_interview.md at master · nothings/stb
    (https://github.com/nothings/stb/blob/master/docs/stb_voxel_render_interview.md)
52. Added: Poly Haven • Poly Haven
    (https://polyhaven.com/)
53. Added: Hardware build: CRC calculation
    (https://youtube.com/watch?v=sNkERQlK8j8)
54. Added: Ben, Ben and Blue
    (https://open.spotify.com/show/5wkeevvNsyzJXN7xf9nxfO)
55. Added: How Microsoft Made Me Love .NET Core And C# Again
    (https://subedi.co/blog/2018/04/24/how-microsoft-made-me-love-net-core-and-c-again/)
56. Added: .NET customers showcase | See what devs are building
    (https://dotnet.microsoft.com/en-us/platform/customers)
57. Added: Conditional jump instructions
    (https://youtube.com/watch?v=Zg1NdPKoosU)
58. Added: GitHub - mimoo/Diffie-Hellman_Backdoor: How to backdoor Diffie-Hellman
    (https://github.com/mimoo/Diffie-Hellman_Backdoor)
59. Added: You fired your top talent. I hope you’re happy.
    (https://startupsventurecapital.com/you-fired-your-top-talent-i-hope-youre-happy-cf57c41183dd)
60. Added: ASP.NET Core updates in .NET 5 Preview 8 - .NET Blog
    (https://devblogs.microsoft.com/dotnet/asp-net-core-updates-in-net-5-preview-8/)
61. Added: Reprogramming CPU microcode with an Arduino
    (https://youtube.com/watch?v=JUVt_KYAp-I)
62. Added: ASP.NET Core updates in .NET Core 3.0 Preview 3 - .NET Blog
    (https://devblogs.microsoft.com/dotnet/asp-net-core-updates-in-net-core-3-0-preview-3/)
63. Added: Update and PODCAST ANNOUNCEMENT!
    (https://youtube.com/watch?v=Nws5-kp8Blk)

Generation took: 00:11:40.3846567

---
## [ghashy/bevy](https://github.com/ghashy/bevy)@[fb4c21e3e6...](https://github.com/ghashy/bevy/commit/fb4c21e3e62b3789e8e768ac63dc2205ddec698f)
#### Thursday 2023-07-20 23:17:23 by Ida "Iyes

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

