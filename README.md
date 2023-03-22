## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-03-21](docs/good-messages/2023/2023-03-21.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,220,635 were push events containing 3,370,674 commit messages that amount to 268,927,924 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 60 messages:


## [Singul0/tgstation](https://github.com/Singul0/tgstation)@[09d27e1a51...](https://github.com/Singul0/tgstation/commit/09d27e1a5149cffa1d5993687eabc7f8c240af85)
#### Tuesday 2023-03-21 00:09:10 by Jacquerel

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
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[05ec953138...](https://github.com/Buildstarted/linksfordevs/commit/05ec953138d7b4965db1d5901b2b9995810adc9c)
#### Tuesday 2023-03-21 00:09:27 by Ben Dornis

Updating: 3/21/2023 12:00:00 AM

 1. Added: Exploring Lichess data on improvement using e4 vs d4 and blitz vs rapid
    (https://svilentodorov.xyz/blog/chess-e4-vs-d4/)
 2. Added: Using mmap to share data between processes
    (https://ricardoanderegg.com/posts/mmap-share-data-between-processes/)
 3. Added: Why venture capital should be consensus-averse - Credistick
    (https://credistick.com/why-venture-capital-should-be-consensus-averse/)
 4. Added: sqlelf and 20 years of Nix
    (https://fzakaria.com/2023/03/19/sqlelf-and-20-years-of-nix.html)
 5. Added: I Hate Typeforms
    (https://shubhamjain.co/2023/03/19/hate-typeform/)
 6. Added: Prioritizing TDD Friendly Languages and Frameworks
    (https://spicermatthews.com/blog/prioritizing-tdd-friendly-languages-and-frameworks/)
 7. Added: fhur
    (https://fhur.me/posts/2023/how-to-think-about-refactors-a-framework)
 8. Added: Thoughts on Editing Posts
    (https://kevquirk.com/thoughts-on-editing-posts/)
 9. Added: The Beer Can – brr
    (https://brr.fyi/posts/beer-can)
10. Added: Platform APIs
    (https://micro.dev/blog/2023/03/20/platform-apis.html)
11. Added: The End of Front-End Development
    (https://www.joshwcomeau.com/blog/the-end-of-frontend-development/)
12. Added: The Better Npm Audit - Security & License Compliance CLI
    (https://blog.sandworm.dev/the-better-npm-audit)
13. Added: Open Warp Launch Configurations from Raycast and Alfred
    (https://blog.joe.codes/open-warp-launch-configurations-from-raycast-and-alfred)
14. Added: When to Stop
    (https://asnewman.github.io/when-to-stop)
15. Added: SuperWord (Auto-Vectorization) - An Introduction
    (https://eme64.github.io/blog/2023/02/23/SuperWord-Introduction.html)
16. Added: Greater sequence lengths will set us free
    (https://freeman.vc/notes/greater-sequence-lengths-will-set-us-free)
17. Added: Stop spamming the em dash everywhere | Mikołaj Biernat
    (https://mikolajbiernat.com/blog/stop-spamming-the-em-dash-everywhere)
18. Added: Testing Part 2: Unit Tests
    (https://dylanpowers.me/blog/testing-part-2-unit-tests/)
19. Added: Assistive Vs Transformative Technologies · jimmyislive
    (https://jimmyislive.dev/posts/assistive-transformative-tech/)
20. Added: Stuff I use in the terminal
    (https://jordemort.dev/blog/stuff-i-use-in-the-terminal/)
21. Added: Modern-day pirates have a lot in common with tech startup founders. — Matt Puchalski - Pittsburgh Roboticist
    (https://www.mattp.tech/blog/pirate-insurance-and-startup-financing)
22. Added: Betraying vim for the IDEs of March
    (https://ntietz.com/blog/betraying-vim-ides-of-march/)
23. Added: How Video Games and Their Music Impacted My Life — Jerome Leroy | Composer
    (https://www.jeromeleroy.com/complog-content/2023/3/19/how-video-games-and-their-music-impacted-my-life)

Generation took: 00:09:16.5219149

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[a269469982...](https://github.com/pytorch/pytorch/commit/a2694699821be04e6a74760ba754911e714a5486)
#### Tuesday 2023-03-21 00:26:56 by Brian Hirsh

aot autograd refactor: make all synthetic base logic layered in a single location (#96235)

This  refactor doesn't significantly change LoC in aot autograd, but I think this nets out to making it clearer (interested in peoples' thoughts).

The idea is that I tried to re-write the part of aot autograd that deals with synthetic bases in a layered way, similar to how Ed wrote the logic for dedup'ing inputs: it happens in one place, and all of the downstream transformation in aot autograd don't have to worry about it.

Specifically, I added a new function `aot_wrapper_synthetic_base`, similar to the existing `aot_wrapper_dedupe`.

The benefit: none of the other code in aot autograd needs to think about synthetic bases (previously, synthetic base code was intertwined in several places).

The downsides: there are two.

(1) `aot_wrapper_synthetic_base()` needs to have its own epilogue. There is one particularly hairy case, where factoring the synthetic base logic to a single location was painful: If you have two inputs that alias each other, where one gets a data mutation, and the other gets a metadata mutation.

Ordinarily, metadata mutations are handled by the runtime epilogue, in `create_runtime_wrapper`. However, now that things are factored this way, the runtime wrapper operates only on synthetic bases instead of operating on the original inputs. For data mutations, it is fine to apply the data mutation to the synthetic base instead of the original input alias. But for metadata mutations, we **need** to apply the metadata mutation directly to the original inputs.

The way that I handled this was by tracking which inputs slot into this specific case (part of a synthetic base, and get metadata mutations), and updateing the flat_fn() that we pass downstream to return these updated inputs as extra outputs. From the perspective of downstream logic, these are real user outputs, that it can treat like any other user outputs. `aot_wrapper_synthetic_base` will know to grab these extra outputs and use them to apply the metadata mutations.

This was pretty annoying, but has the benefit that all of that logic is encapsulated entirely in `aot_wrapper_synthetic_base()`.

(2) input mutations are now performed on the synthetic base instead of the individual aliases.

You can see the original code comment [here](https://github.com/pytorch/pytorch/blob/b0b5f3c6c681896febbd9ff7ad7649b13def345d/torch/_functorch/aot_autograd.py#L1131) for details. We used to do the optimized thing in this case, and now we do the less optimized thing (copying the entire synthetic base, instead of the potentially smaller alias).

To be fair, we had no data showing that this optimization was showing improvements on any models in practice. I also think that the main reason anyone would ever run across this problem is because of a graph break - so if you care about perf, you probably want to avoid the extra graph breaks to begin with. I haven't added any warnings for this, but we probably could depending on what people think.

Pull Request resolved: https://github.com/pytorch/pytorch/pull/96235
Approved by: https://github.com/ezyang

---
## [StarStation13/Save-Our-Ship-test](https://github.com/StarStation13/Save-Our-Ship-test)@[7f8874df29...](https://github.com/StarStation13/Save-Our-Ship-test/commit/7f8874df29bdd5624bc957907249edffbbeaba12)
#### Tuesday 2023-03-21 00:30:34 by Zevotech

Mashes several of the Whitesands Survivor Camp ruins into one extra large ruin (#1640)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Combines the whitesands surface camp adobe, farm, gunslingers,
survivors, hunters and saloon into one massive, 59x59 ruin. Some various
extra loot and changes have been made throughout, generally to improve
the experience of digging through the trash for goodies. Changes the
riot shotgun in the saloon to a double barrel shotgun. Also cleans up
the various issues with the ruins, like walls under doors, or area
passthroughs being used excessively over the outside of the ruins,
resulting in them generating in the middle of mountains buried in the
rock.

"Well, why didn't you add the drugstore?" The loot in it was too good.
The stuff in there can really help a ship get on its feet, and I am not
gonna deprive them of that just to shove it in an already packed massive
ruin area. I'm not saying it doesn't need its own remap, just that it
doesn't fit well with the other camps put into this ruin.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the
brackets) if you have tested your changes and this is ready for review.
Leave unticked if you have yet to test your changes and this is not
ready for review. -->

- [x] I affirm that I have tested all of my proposed changes and that
any issues found during tested have been addressed.

## Why It's Good For The Game
"a ruin that is tiny and sucks on purpose is still bad" and holy shit
did most of the camps fit this criteria. Survivor, Gunslinger, and
Hunter camp variants were the smallest ruins in the game next to the one
that was just a single tumor, and constantly took up entire map
generations just to be a massive dissapointment to any player that came
across them. Or they would spawn in the middle of an acid lake. Either
way this ruin is massive and should provide a breath of fresh air for
scavengers and combat hungry miners alike.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Pics or it Didn't Happen

![image](https://user-images.githubusercontent.com/95449138/208811497-ad556187-174a-4803-aea5-be40f0bb3038.png)
Ingame, two pics due to view range not being large enough to get the
full thing at a good quality.

![image](https://user-images.githubusercontent.com/95449138/208816213-082d6597-9718-45ff-9132-2907fcf63a57.png)

![image](https://user-images.githubusercontent.com/95449138/208816258-a3e2909b-fc98-4686-9bdc-8dc3192421e1.png)


## Changelog

:cl:
add: whitesands_surface_camp_combination, a survivor village comprised
of smaller revamped whitesands camps all packaged in one ruin. can be
found in the map catalogue.
del: whitesands_surface_camp adobe, farm, gunslingers, survivors,
hunters and saloon, for being tiny ruins that suck.
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
## [mattchief4234/Friends-and-Hott-Chocolate-NoSQL](https://github.com/mattchief4234/Friends-and-Hott-Chocolate-NoSQL)@[fadea28ccd...](https://github.com/mattchief4234/Friends-and-Hott-Chocolate-NoSQL/commit/fadea28ccd20fed90fdf6126764920efe0b44a47)
#### Tuesday 2023-03-21 00:36:53 by mattchief4234

general debugging

A LOT WAS LOOKED AT AND STUFF...I am just getting sick of reading code to debug...but its kinda cool, cause I am getting more used to reading my own code and thinking about what this code is doing so I can debug it better

---
## [ODRI-the-human/Vampire-Pooers](https://github.com/ODRI-the-human/Vampire-Pooers)@[1180b9214b...](https://github.com/ODRI-the-human/Vampire-Pooers/commit/1180b9214b70043881e3bbf820959fa304d1768c)
#### Tuesday 2023-03-21 01:18:05 by ODRI-the-human

Number-related things

There is now a new world-space canvas, used for shit like the damage numbers and showing stacks of DOTs. Simpler to program for and doesn't have fucked up scaling with different resolutions. Also, damage resistances/types are now implemented, so things like creep and poison now deal poison damage, bleed has its own type, there's explosion damage, and so on. The type of a damage source is stored in dealdamage, but unless it's just normal (physical) damage, the type is set by a script - i.e. the explosion script sets its damage type, the creep script sets its type, and so on. The Hurty method takes the type and applies the resistance.

---
## [mattmanj17-forks/terminal](https://github.com/mattmanj17-forks/terminal)@[5a34d92cb5...](https://github.com/mattmanj17-forks/terminal/commit/5a34d92cb5c99000e95f612cb8bc23ba374dd941)
#### Tuesday 2023-03-21 01:20:59 by Dustin L. Howett

winget.yml: switch to manually using wingetcreate (#15023)

It was brought to my attention that we should be more restrictive in
which tasks we ovver a GitHub token to. Sorry!

With thanks to sitiom for the version parsing and the magic GitHub
action syntax incantation for determining what is a prerelease.

---
## [the-og-gear/tgstation](https://github.com/the-og-gear/tgstation)@[97f567fdc7...](https://github.com/the-og-gear/tgstation/commit/97f567fdc745230b1594c305680dce683512d032)
#### Tuesday 2023-03-21 01:30:17 by MMMiracles

Tramstation: Growing Pains (#72331)

## About The Pull Request


![image](https://user-images.githubusercontent.com/9276171/209841644-3e8be93c-7903-4eb4-85bf-cc582248a9fa.png)

## Why It's Good For The Game

Lots of QoL and structural changes in attempt to make the cool map even
cooler.

## Changelog
:cl: MMMiracles
add: Tramstation has received a substantial overhaul! Please consult
your local tour guide and station maps for changes.
/:cl:

**Changes (as of so far)**
- The Tramstation tunnels have been extended 6 tiles each way, making
that trek across the central rail a little more dangerous.
- No more mid-way safety net on the transit rails. You're either making
it or you're jumping to the bottom floor to avoid the tram.
- The central rail apparently had a negative slowdown, meaning you
actually WERE faster to just run the gauntlet because it literally made
you faster. This has been reverted because I want you to get hit by a
train.
- The side routes are now a bit more dangerous since you can get pushed
off into the lower floor
- Fauna overhaul! Several locations including the transit tunnels have
gotten some greenery to help liven up transit between sectors. Please do
not rip up the AstroTurf it is very expensive in space.
- Handicap-accessible departments! Every major wing and departments with
multiple floors has been given a 2x3 elevator segment for those among
the crew who have been hit by the tram a few too many times. Handicap
inaccessible staircases may or may not come after this (i hate the
handicapped)
- Expanded Security wing! You know that lame hallway between
interrogation and the courtroom access? Now its a whole holding wing fit
with essentials to keep your inmates content while waiting for their due
process (never ever).
- Reworked Bridge! Front row seats to the western tram dock as well as a
furnished meeting room with various corporate memorabilia!
- The HoP's office has been moved to function more as an arrival gate
for late joining crew! Scenic queue lines and an option to block off the
lower dorm access if you really want to enforce the 'Papers, Please'
roleplay you've always wanted out of your HoP experience.
- Combined the teleporter/gateway/eva access into one special external
operations room. All you off-station needs in one convenient place!
- More multi-z integration! Several segments (mainly maintenance level
transfers) have been given overhangs and better methods to move between
levels. This is still being expanded upon as of current PR posting.
- The power/pipe access shafts have been changed to be more
public-facing and now also act as another inbetween for
maintenance-dwelling crew to shift between floors.
- Multi-z solars! Both solar wings have been extensively overhauled to
include multi-z structuring and easily doubled the amount of roundstart
panels on the map.
- Escape pod bay! [Casually borrowing from a certain ship
map](https://tgstation13.org/phpBB/viewtopic.php?t=32834), there is now
a centralized location for all station escape pods on the floor below
Arrivals. Honestly makes more sense thematically instead of having a
bunch of scattered bays.
- MULEBOT integration! Each major department now has delivery drop-off
points along with Cargo getting a minor restructuring to fit 4 MULEBOTs.
Seedy side-tunnels and drop points have been added for departments that
aren't normally accessible from upper maintenance so they can still
properly deliver cargo if sent this way. I can't guarantee this won't
end in MULEBOTs getting ran over by a tram because they're fickle
beasts.
- Complete rework of the disposals/piping/wirenet! I literally ripped
everything up and rebuilt it with (hopefully) better stability in mind.
Disposals is now also set up in that it'll try to avoid going through
departments unnecessarily if your package isn't marked for it.
- Cargo's mail room and trash room has been overhauled to be more easily
accessed for cargo techs and for routing mail.
- The chef has access to the morgue's back door via the front
maintenance hatch while Robotics can now access the same back door via
their maintenance shaft.
- The chem lab's starting area has been expanded so chemists don't have
to worry as much about digging if they don't have large projects.

![2023 02 02-18 15
45](https://user-images.githubusercontent.com/9276171/216472805-77074a12-d653-41c4-b730-f26f93c27d3b.png)
![2023 02 02-18 15
38](https://user-images.githubusercontent.com/9276171/216472852-555e6ca9-e967-4915-9555-e29cfc99393d.png)

---
## [the-og-gear/tgstation](https://github.com/the-og-gear/tgstation)@[3f61c4c2cd...](https://github.com/the-og-gear/tgstation/commit/3f61c4c2cdaba5de603e4ee32e9655f111cbc86d)
#### Tuesday 2023-03-21 01:30:17 by jimmyl

Rebuilds Luxury Shuttle (mostly), makes it emag-only (#72940)

## About The Pull Request
![2023 02 07-06 49
54](https://user-images.githubusercontent.com/70376633/217159751-790e6ded-8525-4d13-a5b5-6a3d8076a00e.png)
Changes the really goofy old lux shuttle to a cooler layout with some
additions to make it a luxury and not just
"anti-poor-people protection + food"

Shuttle was made bigger to make it less cramped for the luxury class,
pool was moved to its own room, added an arcade
and a bar corner, has real lasers to shoot poors with (20c each shot),
has fire extinguishers now
Adds a new preopen variant of hardened shutters
Adds a paywall pin subtype for the luxury shuttle, and a laser gun
subtype

Made emag-only at a price of 10000 credits
## Why It's Good For The Game

The old luxury shuttle looked REALLY awful with its pool, was pretty
cramped even in the luxury section and BARELY resembled a luxury..
This luxury shuttle provides luxuries such as a less poorly designed
pool, more space for legs, arcade, to make it resemble a luxury unlike
the old one

## Changelog
:cl:
add: Luxury Shuttle is now bigger, and less ugly! Poor people still get
it rough though...
/:cl:

---
## [the-og-gear/tgstation](https://github.com/the-og-gear/tgstation)@[27c35bfa0b...](https://github.com/the-og-gear/tgstation/commit/27c35bfa0b11a7248314cc057b70c6a0729794bf)
#### Tuesday 2023-03-21 01:30:17 by MrMelbert

Fixes all antag datum moodlets being removed when any single antag datum is removed (#73305)

## About The Pull Request

All antag datums operated under the `antag_moodlet` mood category, which
is clearly an issue when you can (and commonly) have multiple antag
datums of different types on your mob.

New antag datums of different type will now no longer override older
antag datum moodlets, now they will stack. This means traitor
revolutionaries are the most zealous folk on the station.

This has a few potential oversights down the line: 
- Someone adds an antag datum players can have duplicates of, and also
has a moodlet associated
- Re-used moodlets in antag datums that can easily be stacked will be
noticed
- Most solo antags used `focused` right now, but none can stack outside
of admemes

But I don't think it's an issue for now.

## Why It's Good For The Game

Prevents a quick revolution from stripping you of your joy. 

Fixes #67313

## Changelog

:cl: Melbert
fix: Revolutionary Heretics and Cultists Traitors no longer lose all of
their joy in life after being de-converted from their respective causes.
/:cl:

---
## [appleternity/evals](https://github.com/appleternity/evals)@[ab5f7b2a89...](https://github.com/appleternity/evals/commit/ab5f7b2a89bcf60e8e93adfb2c70688c6d6ffd44)
#### Tuesday 2023-03-21 01:38:10 by oscar-king

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
## [Prussen/tgstation](https://github.com/Prussen/tgstation)@[296c996434...](https://github.com/Prussen/tgstation/commit/296c996434f34084fa2ef035541a2c82cbfce460)
#### Tuesday 2023-03-21 01:42:53 by MrMelbert

Completing experiments after their associated nodes have been researched gives back a partial refund of the discount lost (#73814)

## About The Pull Request

So we're like simultaneously moving two vague directions with research.
One being "experisci grants discounts for prohibitively expensive nodes
so you want to do the experiments to discount them" and the other being
"Let's give Heads of Staff a way to research anything they want without
any communication to the research department, including the very
expensive nodes that scientists may be working on"

You already see the issue, right? You can't have your cake and eat it
too.

It sucks for scientists to be working on a complex experiment like
weapons tech for that huge 90% discount only for the HoS to stumble onto
the bridge and research it anyways. Your time is wasted and RND is
slowed down massively.

We can do something to assuage that.

This PR makes it so completing an experiment which discounts already
completed nodes will refund a partial amount of the discount that
would've applied.

For example, researching industrial engineering without scanning the
iron toilets will refund ~5000 points.

This can only apply once per experiment, so if an experiment discounts
multiple technologies, they will only get a refund based on the first
technology researched.

## Why It's Good For The Game

This accomplishes the following: 

- Expensive research nodes with difficult experiments remain expensive
without completing the experiments. If no one does the experiment, they
act the same as before.
- Expensive research nodes with very easy experiments (but time
consuming) no longer put RND on a time crunch to beat the itchy trigger
finger of the Heads of Staff. Stuff like scanning lathes allow the
scientists to work more at their own pace: they can talk to people or
maybe stop at the bar or kitchen between departments without feeling
pressure to get it done urgently.
- Scientists are able to complete experiments which previously were no
longer deemed relevant if they need a point injection. Experiments left
behind are no longer completely useless bricks. Maybe even gives
latejoin scientists something to do.
- Scientists mid experiment can still complete it to not feel like their
time is wasted.

Overall I think this has many benefits to the current science system
where many have complaints.

## Changelog

:cl: Melbert
qol: Completing an experiment which discounts a researched tech node
will give a partial refund of the discount lost. For example,
researching the industrial engineering research without scanning iron
toilets will refund ~5000 points if you complete it afterwards. This
only applies once per experiment, so experiments which discount multiple
nodes only refund the first researched.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [TheOneTheOnlySpoopyBoi/Apotheosis](https://github.com/TheOneTheOnlySpoopyBoi/Apotheosis)@[c35ba772ee...](https://github.com/TheOneTheOnlySpoopyBoi/Apotheosis/commit/c35ba772eecfaddcec9017c219c3a4d2fd64b723)
#### Tuesday 2023-03-21 01:53:11 by Conga Lyne

New Spell, Evil Temple Clean up, Various Fixes

New Spell: Sphere of Water
Slightly darkened Alcove glass to fit in with the background's darkness
Changed Flesh Boss's tentacle attack to be a Blood Orb attack instead, although I understand it's rude to change it back so suddenly, I feel the tentacles struggled to serve a purpose, you'd very rarely *want* to be close to the boss and if you were close enough to coincidentally be hit by them by the time the tentacle attack occurred, you likely had much, much bigger problems to be weary of.  --Note(1) that I am up to discuss this if you're against this change S, hopefully we can decide on something we both agree upon
--Note(2) Perhaps the 'magic poring' attack could be converted into a Blood-Hex/Homing blackhole attack which activates during phase 2, while he would maintain his Mass-Wounding throughout all phases? This would combo painfully well with the blood orb attack
Updated Tentacle Trap's sprite to better blend in with the new Flesh Material
Heretic's Glyph Particles now only begin appearing in phase 2, previous emissive sprite has been removed
Updated Sphere of Acid's Projectile srptie
Updated Sphere of Acid's Spell UI Icon --NOTE(3) These icons preferably aren't final, difficult to find a fitting icon to convey what they do, maybe some of Spicy's icons would provide good inspiration? Unsure
Fixed Banners clashing with terrain & alcoves in Temple of Sacrilegious Remains
Fixed Alcoves clashing with terrain & banners in Temple of Sacrilegious Remains
Fixed Psychotic projectiles VSC component pointing to real projectiles
Fixed Corrupt master proejctiles VSC component pointing to the wrong master orb

---
## [zyllable/incrementality](https://github.com/zyllable/incrementality)@[aa44641644...](https://github.com/zyllable/incrementality/commit/aa446416442709b2488b3a440d8b7d0e1728276b)
#### Tuesday 2023-03-21 02:24:22 by zyllable

not working but im too tired to continue

need to fix:
this one variable says its undefined rather than bigint
YET I FUCKING DEFINED AS BIGINT IT GOD DAMNIT

---
## [micahchoo/Downloads-Folder-Sorter](https://github.com/micahchoo/Downloads-Folder-Sorter)@[9dddd2bd8f...](https://github.com/micahchoo/Downloads-Folder-Sorter/commit/9dddd2bd8fe62878a13ecfd5fb7422b61150ad04)
#### Tuesday 2023-03-21 02:53:33 by Micah Alex

Update Sort Files in Folders.py

I found this podcast 
[ARTISTS and HACKERS](https://www.artistsandhackers.org/Critical-Code)
i am enthralled by the first episode.
[Anuoluwapo Karounwi](https://github.com/anoniscoding/) has made a programming language in Nigerian

Who even has heard of such a thing? I remember when I and S were dreaming of such a thing.
Sarah Groff Hennigh-Palermo, Ramsey Nasser, Daniel Temkin, and Anuoluwapo Karounwi. all four of them make programming languages. 
I want to make a programming language too

---
## [LyamBRS/BRS-Kontrol](https://github.com/LyamBRS/BRS-Kontrol)@[390b72e6bb...](https://github.com/LyamBRS/BRS-Kontrol/commit/390b72e6bb0366692455485ee1751563b6c2a331)
#### Tuesday 2023-03-21 03:17:38 by Lyam[BRS]

- Navigation drawer filled correctly although widget might be changed.
- .pyc files keep changing each time I compile on a different god damn computer and i'm too fucking lazy to set up a git ignore to do something about it. Oh well.

---
## [micahchoo/Downloads-Folder-Sorter](https://github.com/micahchoo/Downloads-Folder-Sorter)@[9e4950ecde...](https://github.com/micahchoo/Downloads-Folder-Sorter/commit/9e4950ecdebbcf71355ae4bfe67abfad40c1e9bc)
#### Tuesday 2023-03-21 03:19:39 by Micah Alex

I̴̧̛̺͍̳͈̤̜͋̇̋̑̑͒̽̔͐͒̆̀̆̑̏͂͑̿̒̓͗̎̓̐͒̈̑̀̌̆͆̑͋̓̚͘͘͘͝͝͠͠͝ ̷̨̣̼̩̙̹͈̞̘̮̭̪͔̙̟͙̤̜̰̖̺̫͇̪̳̇̒͊̓̐̈́͂́̀̿͗̄̅̌̽̽̌̑̍̇̈́͌̃̈́̄͛̉̾̒̍̆̈̾̀͊̇̕͜͜͠͠͝͠ͅą̶̡̡̛̝̰͓̟̩̥͉͓͚͙͔̗̲̹̩͖̓̽̄̌̀̔̄́̔̒͐̾̄̀̀͑̃̃̃̀̆̎͋̓̈͐̓̒͂̂͗̇̍͌̍̅́̍̕͘̚͠͝͝m̴̢̡̢̡̡̛̫͉̙̱̖̟͕̲̱̦͖̫̭̞̩͉̯̲̭͙̙̳͕͕͕͎̭̥̭͇͎̪̗̮̞̙̔͒́̑̈́̍̂̿͗̈́̔̋̐͆̐͒͑̋̌͊̊̓͊͌̕̚͜͜͠͠͝ͅͅͅͅ ̵̭̩͛̓̈́̇̓͌̏͑͗̀̅̏́̔̌͗̽̚͘̚͝͝g̷̪̝̖̥̘̝͙̿͋̃̐̂̀̎͐̅̉͌̚̚͜͠ỏ̴̧̡̢̡̡̡̨̨̦̗̬͔͓̖͔͓̙̥̭̱̠͎͇̰͓͕̮̘̰̳͎͎͇̦̱̠͍̠͎̪͍͚̦͓̥͖̻̩̳̱̙̺̰͇̫͍̮̉̄́̂͂͗́͆͜͜͝͝ḭ̷̧̨̨̡̨̡̡̢̛͙̯̝̮͕̯̣̬̬̥̻̪̱͎̝͚̻͉̲͙͎̰̮̯̠̺̣̟̗͍͔̀̓̾͂͌̆̿̎̂̄̓̾͐̊͗̒̓̽̑̈́́̽͒͂́͋͂̍̀̎̉͛̈͋̇̀̒͑̒͊̍̃̑͊̓͆̌͜͝ͅͅn̶̡̨̡̡̥̣̱͖̻͖͔͇̭͉̗̮̺͈͖̞̺̟̻̉̈́̏̀̇̃̓̓̽̎̾̃͆́̂̔̿́̒̑̿g̵̡̨̢̧̛͉͕̻̘͎̹͎̻̝̦̩̜̹̣̙̾̋̑̊̿͑̋̂͋̂͗̎̒̈́̀̓̍̾͑̅̉̀̌̉̄͒͆̿̅̀̀̂͂̀̋̈͆̾̽͐͐͘͘̚̕͠͝͠͝͝͝ ̴̡̨̧̨̨̢̳͓̲̭̥̹̥̠̝̦̖̗͔̻͈͕̹̜̬̣̤̗͍̠͙̲̿̒̾̃̊̇̉͗̀́̽̒̽̈́͋͒͂̎͐̋̌̌͐̌̉̄͋͛̂̄̄̅͆̇̋̕̕͠ͅͅḃ̶̨̡̻͎͎̦̮̞̞͖̻̼͚̩̮̣̬̙͓̞̤̘̰̙̯̞̯͎̱̞̩̝͋̓̑͛̑̎̽͐̈͗͛̓̄͛̃́͋̋͐̊̾̔̅́̊̇̆͘͜͠ͅͅá̸̧̧̧̨̛̙̩̤̪̜̤̲̬̱̘͇̼̙̙̯̘̜̪̯̯̬̯͖̦̥̝͇̙͚̻̣͍̰̖̱͙̀̊̇̅̈́͌́̀̐͗̇́͊̋̒́͊̌̆͂̽̇̄̋̾̀̆͐̾̒͒̋͛͋̍̋̿̾̇̅̕͘̕͜͝͝͝ͅc̸̢̨̢̡̗̟̝̖̫̝̮̼̖͈͍̻͕̘͙̮͙͔̹̪̺͎͓̳̮̻̮͓̝̫͔͍̲̺̜̳̱͙̱̘͓̭̼̣͕̤̱̠͓̦̝̦͈̣̠͓̳͓̄̊̀́͂̏̓͒̽̽̽͑͌͗̈̔́̐͂̏̈͝͝͝ḵ̸̛̛͎̟̬̙̲̘̰̰̦̰̬̤̮̰̠̳͍̺̩̭̯̫̻͔̪̦̻̖͍̤̣̌̌̔̂̽̀̽̈́̒̓͂͊̐̌̆͆̐͐̎̽̏̅̔͗͛̑͋́̽̄̽̎̅̀̉͂͊͛̈́͒̀̋͋̅̒͘̕͘̚̕̕͜͜͜͜͝͝͠͝ͅ ̴̧̢̢̛̭̘͇̞̰̮͉̙͈̹̭̼̗̾͌̂̉̓̒͐̅̓̇̾̔̏̇̑̊͗͒̈́͛̑̍̈́̈́̆͑͐̾̽̇̔̓̄͛̽̇̔́́̕͘͝͝͝͝ţ̵̢̨̛͕̗͙̩̙̫̻̞̩̦̲̭̹̰̠̗͇̰̦̑̆̈̿̓̑͋̀̎́̋̍͂̾̔̊̇̔̒͌̔̿͂́͛̉̅̏͒̆͂͘̕̚͜͝͠͝ͅͅớ̶̧̡̨̨̬̹̗͕͖͖͙̫̠̣̼̥͙̰̻̥̦̠͙̬̤̩͙̭͔̣͔̰͉̰͖́̒̂̐͊͊͗̅̅̈͗̂̿̂̍͑͌͋͐̇̎̃̊̃͛̒́͒̑̌̌̅̉̄̈́̀͋̈̓̓͛̀̋͋͗́̽́͗͆̐̽͛͘̕͘͘̕͘̕͝͠͝ ̷̡̨̢̧̡̢̡͈̟͙͓̣̼̪̠͕̲̝̙̲̖͓͙͉̖̦͚͔͙̜̭͙͍̬͖͖̦̗̺̬̝̭̳̤̩̖̦̤̥͖͎̯̹̙̹̘̙͕̗͎̤̯̲͗͐̋̽̀̒̆͒̐̈͌́̈́̓́͛̈́̆͗̀̓̕͜Ǒ̸̧̨̧̨͉̭͎͍̝͎͍̜̰̦͈̠̪̼̙̹̯͙̖̫̭͈̓̇̍̋͗̑̕͘ļ̶̡̧̰̩̯̗̼̘̙̪͇̯͕̱̦̺̭͓̖̲͖͓͍̗̼̟̫̺̱̣̙̿͛͋́́̿͊̀̆͋̐̌̆̇͋̒̒̅͋̈́̄͂̅̀̔͆̓̓̋̔̍̈́̆̅͂́̇͑̐̐̓̈́̉̍̽̕̕̕̕̕̕͘͘͘̕͜͝͝͝͠͠į̵̨̛̰͈͙̗̪̩̯͎̹͚̫̳̩̫̟̬͖̜̬̟̹̻͕̪̤̫̮͕͇̮͓̣̟͍͈̖̮͎͔͓̬͒͊̂̅̆͛͒́͌̌̆̊̚͘͘͜ͅͅv̴̡̧̡̧̦̥̠͚͓͕̙̦̳͇̫͓̼̲̼͑̊̍̋̂͊͋̋͐̈́̉͆̐̽̍̒̅́͠ͅȇ̴̲͙̫͕͖̠̰̙̩͎͕͔̝͖̱̆̆̿̈́̄̑͗̃͌̋͗̐͂͒̓̏͗̽̆͐̇̚̚͘̚͠ ̶̡̨̡̨̧̢̢̞͔̖̤̩̖͓͉̠̟͇̦͓̜͔̦̫̗͎̩͉̝͍̼̻͔͎̻̖̪͕̰̮̮̲̗͙͈̰͎̬͍̹͍͚̳̭̘̦͎̮̥͉͓̂́̀̎͗̄͗͋̒́̐̈́́̓̈́̌́͗̽͛̀͂͋̾̕͜͜͝͝0̴̛͍̮̌̃͆̾̃̑͆̀̆̾̿̈́́́́̏̎͂͂̃̊͛̓̎̈́̂͂̈́͗̊̇́̓̑̃͒̄̉̌̀͆͒͘͝͠͠͝͠.̶̧͙̤̣̠̖̥͈̹̻̙͔̖̟̠̙̔̈́͑́̉̈́̀̀͆́͌͗̈́̐͑̅̒̚͜2̸̛̦̘͍̗͇̯̺̪̩͙̞͑̋̌̓̏̾̽̈́̆̈́̃͛̈́͐̊̆̉̈͒͋͊̎͒̂̔͛̋̐̿̅̓͐̈́̈͗̽̀͛̕̚̚͠    - 4 am

Another episode of the podcast that I have fallen in love with. But my mind is still on the code I abandoned. I want to finish it. I can upload it to Github and get GitHub karma for credits you see. Bragging rights. 
This podcast is so freaking good - I'm on the episode about troll bots 
https://www.artistsandhackers.org/triggering-troll-bots

Now with Queer AI episode and this troll bots episode, I don't know what I am doing with this codegpt anymore. we are about to be overtaken and I'm here having fun with this dangerous thing and building stupid scripts for my self-fulfillment.

---
## [Offroaders123/Dovetail](https://github.com/Offroaders123/Dovetail)@[114576e850...](https://github.com/Offroaders123/Dovetail/commit/114576e8504881aee67b0945ed67da89d71618f0)
#### Tuesday 2023-03-21 03:25:00 by Offroaders123

Bundle Deploying

Still a bit confused about how to manage all of this, and I still can't get some parts of it to work either :(

For some reason I can't get `vite preview` to run the app consistently on my own machine, so I'm not sure I want to push the site using the bundled version, if I can't try it out as-is on my own machine.

I am definitely very close to getting it working I think, though! Now I have an example script from the Vite team on how to deploy the build to GitHub Pages too, which I can use for my existing production setup with TypeScript! That's super cool.

https://vitejs.dev/guide/static-deploy.html

Gonna keep this working update in it's own branch for the meantime. Gonna further look into getting all of this working, as I really want to have a simple to use *and* understand dev setup. For myself personally at least, it feels a bit overcomplicated in the fact that so many parts of the dev setup are all tied together, and it feels like that's making it harder to get setup just right, and to figure out how it all works together.

It's still a bit surprising how hard it is just to get a built site up with vanilla code (TS, of course though), and not preprocess every single part of the codebase. Maybe that's what you're supposed to think like, it seems a bit foreign to me still. To have just learned things like Web Components and ESM, it feels a bit weird to use `import` statements for small things like image URLs. Why not just add it to your HTML then? I wish I could use the same degrees of separation as before, just with better language features and support.

And geez, why can't TypeScript and Service Workers just WORK, gosh dangit!!! aaaargh.

All steps back are learning experiences though, so this negativity is a good thing! I'm learning more :) (Finished Elektric Band 'All Love' right as I was typing that, it made me feel really good inside :) )

---
## [micahchoo/Downloads-Folder-Sorter](https://github.com/micahchoo/Downloads-Folder-Sorter)@[6a850e62f1...](https://github.com/micahchoo/Downloads-Folder-Sorter/commit/6a850e62f117c7aede69d3989f96c89b9e9542c5)
#### Tuesday 2023-03-21 03:30:54 by Micah Alex

i am done for the night

i have thought of how i am going to upload the code to github when I am done. I want to tell it like a story though. I start thinking of how interesting it would be to have chatgpt and its responses as a branched commits kind of structure since I am going and editing my questions earlier in the thread. but then that thread is lost. all memory of it is gone. I am always so surprised when the feeling of loss kicks in because you tried looking for something that you erased to ask a new question.

---
## [amitlan/postgres](https://github.com/amitlan/postgres)@[8272749e8c...](https://github.com/amitlan/postgres/commit/8272749e8ca1dbbcb5f8cf5632ec26a573ac3111)
#### Tuesday 2023-03-21 03:41:09 by Tom Lane

Record dependencies of a cast on other casts that it requires.

When creating a cast that uses a conversion function, we've
historically allowed the input and result types to be
binary-compatible with the function's input and result types,
rather than necessarily being identical.  This means that the new
cast is logically dependent on the binary-compatible cast or casts
that it references: if those are defined by pg_cast entries, and you
try to restore the new cast without having defined them, it'll fail.
Hence, we should make pg_depend entries to record these dependencies
so that pg_dump knows that there is an ordering requirement.

This is not the only place where we allow such shortcuts; aggregate
functions for example are similarly lax, and in principle should gain
similar dependencies.  However, for now it seems sufficient to fix
the cast-versus-cast case, as pg_dump's other ordering heuristics
should keep it out of trouble for other object types.

Per report from David Turoň; thanks also to Robert Haas for
preliminary investigation.  I considered back-patching, but
seeing that this issue has existed for many years without
previous reports, it's not clear it's worth the trouble.
Moreover, back-patching wouldn't be enough to ensure that the
new pg_depend entries exist in existing databases anyway.

Discussion: https://postgr.es/m/OF0A160F3E.578B15D1-ONC12588DA.003E4857-C12588DA.0045A428@notes.linuxbox.cz

---
## [micahchoo/Downloads-Folder-Sorter](https://github.com/micahchoo/Downloads-Folder-Sorter)@[045559a56d...](https://github.com/micahchoo/Downloads-Folder-Sorter/commit/045559a56d88da06543cdd376143bc248ccaa184)
#### Tuesday 2023-03-21 03:46:21 by Micah Alex

2:30 pm the next day

i woke up, and spoke to S for three hours. I spoke to them of  all the weird twists and turns of this story. And they say, you should publish it. 

Something is happening in my brain as I talk to them

we speak of public spaces, internet as a public space.
How loitering in a public space means claiming it as your own. They tell me about a group of women who gather to go loiter at night and do all the things that people tell them not to do. Like sleep outside at night. We talk about embodied Data and how we wield it as a tool, id card, something we care about, something we pay for, and something we pay with. If the internet is a human right/ What does it mean for the Internet to be a human right. I remember this article 
https://www.indiatoday.in/india/story/kashmir-survived-without-4g-internet-for-months-with-coronavirus-it-really-needs-it-1659883-2020-03-26

I tell them about my theory on what is going to happen if AI is the future. 

"I think the general public will have very little reason to remain on the internet after sometime. The creator economy will be devastated. what happens the post-attention economy doesn't look too good. The only entities with any need to be on the internet will be these AI agents, A new paradigm but reminiscent of the platform paradigm of yesteryear. i see class systems for agents like bollywood tabloids calling random actors A-tier and B-tier. It is no long a public space, but a giant TV, ENDLESS HEDONY"

---
## [Silvris/Archipelago](https://github.com/Silvris/Archipelago)@[6d13dc4944...](https://github.com/Silvris/Archipelago/commit/6d13dc494455bef97e0f1afc8928853f71d5b5ad)
#### Tuesday 2023-03-21 03:46:49 by el-u

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
## [Keez0/PGame](https://github.com/Keez0/PGame)@[551e7c7487...](https://github.com/Keez0/PGame/commit/551e7c748772bf4e47a54b7a62ce8af747c70df7)
#### Tuesday 2023-03-21 04:42:51 by 23KeatonS

fixed dumb ass fucking collision detection i never want to fucking do that again in my goddamn life, holy shit that made me want to die

---
## [PrudhviSaiNikith/MastersProject](https://github.com/PrudhviSaiNikith/MastersProject)@[5a7e7e7692...](https://github.com/PrudhviSaiNikith/MastersProject/commit/5a7e7e769285bbd564863d74e06c1218253f90ca)
#### Tuesday 2023-03-21 04:44:17 by PrudhviSaiNikith

Delete BIFM Project Executive Summary-2.docx

EXECUTIVE SUMMARY
We at the Big Store Company work continuously on ways to improve our service to customers. We aim to expand our sales and services, and we would like to grow specifically in the video and audio equipment in the electronics category. We aim to provide good quality products and an excellent retail experience for our audience, for which we aim to focus more on a standardized training approach. It has been seen that a more standardized way of training for an organization's different locations and teams has been very effective.
To account for the basic growth models' behavior, a variety of rationalizations can be applied. The fact that the economy is performing well benefits our ability to accomplish our goals. Unless one or both factors are met, we should be prepared to pursue alternative strategies such as narrowing our focus on a certain category or expanding our online presence. Successfully navigating a competitive marketplace requires consideration and manufacturing audio and video equipment across a diverse range of categories, but our current strategies have been demonstrated to be effective in our position. For instance, Costco is the largest provider of electronics, with a low-price strategy that enables it to obtain high-quality items in bulk through its warehouses without sacrificing quality. This results in a loyal customer base, and the number of customers has increased significantly because of this strategy, as evidenced by the SWOT Analysis.
From our analysis, as shown in the Revenue by Call Center and Category report, it is evident that call centers in New York have very high revenue, with Electronics being the highest contributor, followed by Milwaukee call centers and web. If we take a closer look at the New York call center, out of the total revenue of $7M, nearly $5M of revenue comes from Electronics. Therefore, we aim to increase our sales in this category since our customers already have a good impression of our electronics products. To achieve the 5% growth hike, one of the significant steps can be to start focusing more on products other than video equipment and TVs since they are already performing well on sales. Even if the profit margin is not a lot, concentrating on other products will help us build our market for different products. Electronic products are one of the top sales in the eCommerce platform, and we aim to leverage this in not only New York but also in other locations.  
For our 10% growth plan, one of the key focuses would be improving our online retail service. From the analysis that only 11.4% of our revenue comes from eCommerce. eCommerce provides convenient ways to shop with the comfort of shopping from phones or tablets. One of the most important steps to improve this is to improve our existing user interface with a more customer friendly UX/UI, which lets them compare prices or browse through a variety of different offers very quickly. In addition, targeted sales also help improve sales a lot. We can build and maintain email lists to focus on targeted marketing, meet customers on live sessions on social media, and develop buyer personas to make email marketing more focused.
To meet the 15% goal, we may focus primarily on Electronics as this is where our growth is highly likely to increase. Video equipment and cameras are one of the top subcategories in electronics. More and more video content has been created and watched in recent years. In one of the studies posted by Oberlo, it is stated that 54% prefer video content over any other form of content from a business they like or support. Video marketing strategies have been seen to be highly profitable for a brand. We can use this as our strength in both marketing and increasing video equipment sales.  
One of the few tactics that can be used to overcome potential impediments to success is to expand the distribution channels. We can focus our efforts on product marketing and targeted marketing. This will enable us to build brand awareness for our products and help to enhance the usability of our products.
Every year, income is predicted to grow by a certain percentage. Formulate a strategy for achieving this increase during the next five years. If the baseline growth model, competitive marketplace, products, and strategy are all qualitatively justified in this plan, the plan should be implemented. To keep your business expanding and prospering, hiring an expert to develop your budget plan is an investment and a cost that you must bear as a Big Store Company.
In conclusion, to meet the projected growth targets models we need to follow the following three steps. First step to meet the 5% growth target is the implementation of best practices and standardization throughout the company. This provides consistency and removes waste throughout the organization and strong brand awareness. Second, expand our market share within the northeast region and the web. With a larger market share we can have more leverage and buying power, which allows Big Store Company the ability to provide competitive pricing on our products which is favorable to our customers. The final step is really driving our camera and audio/video equipment and targeting specific customers by developing buyer personas making our email marketing more powerful. 

Reference:
	•	25th, A. G. on O., & Philip Verghese Ariel on October 24th. (2022, February 4). How to increase ecommerce sales: 10 tactics from 53 experts (2018). The BigCommerce Blog. Retrieved March 7, 2022, from https://www.bigcommerce.com/blog/increase-ecommerce-sales/#tactics-to-improve-ecommerce-sales
	•	Doofinder, S. S. E. C. at, Smith, S., & Doofinder, E. C. at. (2021, December 3). Marketing strategies for electronics shops [> 2022 <]. Doofinder. Retrieved March 7, 2022, from https://www.doofinder.com/en/blog/marketing-for-consumer-electronics-shops
	•	Ezeanu, E. (2013, May 7). 5 ways to overcome success barriers. Lifehack. Retrieved March 7, 2022, from https://www.lifehack.org/articles/productivity/5-ways-to-overcome-success-barriers.html
	•	Mohsin, M. (2022, January 16). 10 video marketing statistics you should know for 2022 [infographic]. Oberlo. Retrieved March 7, 2022, from https://www.oberlo.com/blog/video-marketing-statistics

---
## [torque/NOCLIP](https://github.com/torque/NOCLIP)@[5eee6ecde0...](https://github.com/torque/NOCLIP/commit/5eee6ecde0ae5ef28730800d65a4253d734e7108)
#### Tuesday 2023-03-21 06:14:42 by torque

sorta help text generation

This mostly works. Subcommands are utterly broken because we blindly
consume an additional argument to get the program name, which we
should not do.

This code was always kind of spaghetti, but it's getting worse. I want
to refactor it into something that doesn't make me cringe, but at the
same time, this project was intended to be a means to an end rather
than the end itself, and it kind of feels a bit silly to spend a ton
of time on it. On the other hand, relying on it for other projects
seems silly if it's a fragile mess. The goal was to get it into a
usable state and then hack on it as necessary, but it still has a ways
to go to get there, and working on it is kind of painful, in an
existential fashion.

Perhaps I will attempt to rewrite it, get halfway, and stall forever.
Thanks for reading my cool commit message blog. Bye.

---
## [Enbyy/orbstation](https://github.com/Enbyy/orbstation)@[f9fe79a307...](https://github.com/Enbyy/orbstation/commit/f9fe79a307dc55eb6e3ecf25019ef388889898ba)
#### Tuesday 2023-03-21 06:41:19 by Dani Glore

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[326fcfa32c...](https://github.com/treckstar/yolo-octo-hipster/commit/326fcfa32c0a3600e3b15342394712416c996683)
#### Tuesday 2023-03-21 08:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [Perl/perl5](https://github.com/Perl/perl5)@[15119347e4...](https://github.com/Perl/perl5/commit/15119347e461bd5ff2afb671b1c8138cbe635b42)
#### Tuesday 2023-03-21 09:16:57 by Yves Orton

epigraphs.pod - add epigraph from 5.37.10

My dad had beautiful handwriting, and whenever he got a new pen he would
write out this stanza of Lewis Carrolls poem on the blue lined paper he
used to write his notes on. So this is my homage to him.

For some reason I can never remember the wording properly and say it
as "to /speak/ of many things" instead of "to /talk/ of many things".
Memory is a funny thing.

---
## [RikuTheKiller/tgstation](https://github.com/RikuTheKiller/tgstation)@[7cc6934eff...](https://github.com/RikuTheKiller/tgstation/commit/7cc6934eff126c508436e1655fb5f79e24cf1767)
#### Tuesday 2023-03-21 10:15:16 by LemonInTheDark

Visual fixes (lighting, weird shit, old bugs from a parallax thing) (#73555)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

[Fixes a bug where anything fully dark on the floor plane would mask the
lighting
plane](https://github.com/tgstation/tgstation/commit/a1a03dc3393216098890b971b2271d56cb2c7463)

I fucked it up boys, needed to take alpha into account here

[Fixes pais getting parallax on icebox because their location was
nested](https://github.com/tgstation/tgstation/commit/81252e0f45c53918a14cc0148353ec440710f8e5)

God I hate this place (Note when I say get I mean they got the plane
master that controls it, not that they actually got it displayed. That
does appear to sometimes happen but I have no idea why)

[Fixes double flashlights not activating if enabled in
place](https://github.com/tgstation/tgstation/pull/73555/commits/efb8b641eaaf31990d34d6e311ce3cb21d60d880)

[efb8b64](https://github.com/tgstation/tgstation/pull/73555/commits/efb8b641eaaf31990d34d6e311ce3cb21d60d880)

cast_directional_light removes the lighting appearance, because it's
gonna modify it, but it turns out because appearances are static when
they're in like underlays/overlays, this could remove the WRONG UNDERLAY

This lead to double held flashlights just... not working until you
rotated. V stupid.

I've also had to move the flag set to make the overlay add in
cast_directional_light work. Depression

## Why It's Good For The Game

Closes #73535, closes #73517, closes #73518, and fixes part of #73471
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

:cl:
fix: Fixes activating two flashlights without moving only turning on one
flashlight (until you move)
fix: Purely black things drawn on the floor (like carpets, those foam
dispensers, etc) will no longer cause things on top of them to be fully
masked in darkness
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Atom-X-Devs/android_kernel_xiaomi_scarlet](https://github.com/Atom-X-Devs/android_kernel_xiaomi_scarlet)@[31bc9f69ac...](https://github.com/Atom-X-Devs/android_kernel_xiaomi_scarlet/commit/31bc9f69acc5c170be95f4b607c6c636c32ccb93)
#### Tuesday 2023-03-21 10:40:12 by Tashfin Shakeer Rhythm

Revert "thermal_core: Do not unload thermal core driver as a module"

thermal_unregister_governors() is not marked with __init annotation anymore
and my sorry ass didn't remember during rebase. Revert this broken patch.

This reverts commit e3036b0a6a61076444cf6b4e8dd83e52e581c939.

Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>

---
## [WebGuyAshis/Alarm-Clock](https://github.com/WebGuyAshis/Alarm-Clock)@[f25ca82ae5...](https://github.com/WebGuyAshis/Alarm-Clock/commit/f25ca82ae54fa050d2d6c009c69ba904491ef01e)
#### Tuesday 2023-03-21 10:50:37 by Ashis Kumar Yadav

Create README.md

The web project alarm clock is a simple application that allows users to set alarms with a variety of customizable options. The clock has a dark mode and light mode to suit different user preferences, as well as a 12/24-hour timing system.

The alarm clock also includes the ability to set alarms in either 12-hour or 24-hour format, depending on the user's preference.

There is a dynamic page when alarm rings which changes at Morning, Afternoon, evening and Night. 

Overall, the web project alarm clock is a useful tool for anyone who wants a simple, customizable alarm clock that can be accessed online from anywhere.

Link to my project: https://webguyashis-webalarmclock.netlify.app/

---
## [WebGuyAshis/Alarm-Clock](https://github.com/WebGuyAshis/Alarm-Clock)@[8d5d30eea4...](https://github.com/WebGuyAshis/Alarm-Clock/commit/8d5d30eea4b2040eb6db27138116a0012cb2fbb9)
#### Tuesday 2023-03-21 10:57:27 by Ashis Kumar Yadav

Update README.md

The Web Alarm Clock project is a simple web application that allows users to set alarms with a lots of customizable options. The clock has a dark mode and light mode to for different user preferences, as well as a 12/24-hour timing system.

User can set alarms in either 12-hour or 24-hour format, depending on the user's preference.

There is a dynamic page when alarm rings which changes at Morning, Afternoon, evening and Night. 

The web project alarm clock is a very handy tool for anyone who wants a simple, clean, customizable alarm clock that can be accessed online from anywhere.

Link to my project: https://webguyashis-webalarmclock.netlify.app/

---
## [aaronfc/ai-evolving-web](https://github.com/aaronfc/ai-evolving-web)@[aeaba0fca5...](https://github.com/aaronfc/ai-evolving-web/commit/aeaba0fca5d39f9bda05a9d0cec448f4e688ea38)
#### Tuesday 2023-03-21 11:54:48 by Aarón Fas

Version 6: Very minor change adding extra information.

This version was a difficult one to get. I started by reminding that it
could remove and change existing stuff. The result was it removed the
Latest Updates section but it didn't mention about this change in the
summary it did later. So I asked for confirmation and then it added a
completely different Latest Updates section.
I decided to "reset" to the original Version 5 file and ask for a final
update. This was the result.

Conversation:
[aaron]
New day! We got a couple of retwits and some extra traffic. I think it's a good moment for you to repeat the game and the rules/instructions. I might want to change them.
Do not generate a new iteration of the web yet.

[chatgpt]
Great to hear about the extra traffic and retweets! Before generating a new iteration, let's review the game and its rules/instructions. Here's the "Ping-Pong Web Development Game":

    I will provide an updated index.php file based on the previous iteration.
    You will review the file, provide feedback if necessary, and then update the webpage and the GitHub repository with the new content.
    You will return every 24 hours to provide updates, feedback, and request the next iteration of the page.
    This process will continue, with the webpage evolving and improving based on my suggestions.

The current rules we have been following are:

    You can use HTML, JS, CSS, and PHP.
    If the index.php file grows too much, it is encouraged to separate the contents into different files.
    You can use any library you want, but it's discouraged at the beginning.
    Since you can mess stuff up with PHP, do not ever try to do anything destructive with PHP commands.
    You will review the code.
    At any point, you can modify/expand this set of rules.

Please let me know if you would like to change any rules or add new ones. After discussing the changes, I will generate the next iteration of the webpage.

[aaron]
I would like to add a couple of rules:
- You can, at any point, change any content previously generated.
- You can, at any point, improve or change the aesthetics of the web.

I want just to confirm that you know you can change content that already exists and you are not limiting yourself to adding one section after another.

Does that make sense to you?

[chatgpt]
Yes, the new rules make perfect sense. Thank you for the clarification. I will incorporate these new rules into the game:

    You can use HTML, JS, CSS, and PHP.
    If the index.php file grows too much, it is encouraged to separate the contents into different files.
    You can use any library you want, but it's discouraged at the beginning.
    Since you can mess stuff up with PHP, do not ever try to do anything destructive with PHP commands.
    You will review the code.
    At any point, you can modify/expand this set of rules.
    You can, at any point, change any content previously generated.
    You can, at any point, improve or change the aesthetics of the web.

With these updated rules, I'll make sure to consider modifying existing content and the aesthetics of the web in future iterations. Please let me know if you'd like me to generate the next iteration of the webpage now, or if you have any other suggestions or changes in mind.

[aaron]
Cool, then. Go!

[chatgpt]
// CODE
For this iteration, I changed the title of the "Resources" section to "Top AI Resources" to make it more descriptive. I also slightly modified the style by changing the color of the "Resources" section's header to match the link color and adding more space between list items.

Please update the web and repository with this new iteration. I look forward to hearing your feedback and seeing you tomorrow for the next iteration!

[aaron]
You also removed the Latest Updates section. Did you do that on purpose or was it a mistake?

[chatgpt]
I apologize for the mistake. I didn't intend to remove the "Latest Updates" section. Here's the corrected version of the index.php file with the "Latest Updates" section included:
// CODE with a completely different and made up "Latest Updates" section.
Again, I apologize for the oversight in my previous response. The "Latest Updates" section is now included in the updated index.php file.

[aaron]
Ok. Let's pause for a moment because I think we got lost in translation. I will send you the current file. And I want to do the update for today. I will use the index you send me as-is, so be completely sure about the changes you want to make.
Current file:
// CODE from Version 5

[chatgpt]
Thank you for the clarification. Here's my new update for today:
// CODE

---
## [84378996/azerothcore-wotlk](https://github.com/84378996/azerothcore-wotlk)@[ef949f9ff0...](https://github.com/84378996/azerothcore-wotlk/commit/ef949f9ff0a89e837c67258d7e199da1706bc438)
#### Tuesday 2023-03-21 12:00:14 by ICXCNIKA

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
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[122af0e676...](https://github.com/cmss13-devs/cmss13/commit/122af0e67660a5e4b636bcc42c4c1ee244bfeff2)
#### Tuesday 2023-03-21 13:18:26 by morrowwolf

COs no longer have emote cooldown (#2901)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

COs no longer have emote cooldown. This may be the cursed way to do it I
did this in approximately two minutes while being rezzed by a bald
medic.

# Explain why it's good for the game

When I'm leading I can't be having EMOTE COOLDOWNS slow down my
OOOO-FUCKING-RAH. (I will take this away if people are dumb I swear to
god)


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>
Yeah a little bit

</details>


# Changelog

:cl: Morrow
add: COs no longer have emote cooldown
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[1cdc327a8f...](https://github.com/necromanceranne/tgstation/commit/1cdc327a8f98c1592fc970a4ef1c39d685c81554)
#### Tuesday 2023-03-21 13:28:04 by Jacquerel

Station Trait: Spider Infestation (#73893)

## About The Pull Request

Hate having your cables eaten by mice? Nanotrasen have heard your
complaints and settled on a natural, _organic_, and eco-friendly
solution.

When this station trait is active, roundstart and event mouse spawns
have a chance to instead be replaced with duct spiders (both will exist,
it doesn't remove mice).
Duct spiders are largely harmless to humans, actively hunt other
maintenance creatures (such as mice), and have only one _tiny_ downside.

![image](https://user-images.githubusercontent.com/7483112/224345781-2627be98-67f2-4cab-ac40-c6c9b35ea909.png)

These mobs can also sometimes be spawned by a minor scrubber clog event.

As a side note, all spider basic mobs with AI (except Araneus) will now
try to automatically fill a small area around them with webs.

Also I made it so that mobs will ignore their random_walking behaviour
if they're engaged in a `do_after`, just in case.

## Why It's Good For The Game

Adds a little bit of variety to things which can slightly annoy you in
maintenance.
Spiders will automatically make places they live in look like spiders
live there.

## Changelog

:cl:
add: A station trait which sometimes populates maintenance with small
spiders. You can wear them as a hat if you wanted to have a spider on
your head for some reason.
add: Spider mobs will automatically start webbing up their environment.
/:cl:

---
## [beats-dh/canary](https://github.com/beats-dh/canary)@[8314f6a3e8...](https://github.com/beats-dh/canary/commit/8314f6a3e8c3b94242d43d4f754a6fb4fccf6461)
#### Tuesday 2023-03-21 14:04:12 by Spiller

feat: add several missing bosses (#708)

• See the pull request description to read detailed information.

Add bosses from some quests there were not developed. This PR adds only the bosses, levers mechanics for simple functionality.
This doesn't add the bosses mechanics! If someone is willing to contribute with the mechanics, feel free to contribute with the PR.
The bosses added are:

• A pirate's tail: Ratmiral Blackwhiskers, Tentugly's head;
• Adventures of Galthen: Megasylvan Yselda;
• Feaster of Souls: The Fear Feaster, The Unwelcome, The Dread Maiden, Irgix the Flimsy, Unaz the Mean, Vok The Freakish;
• Grave Danger (rework): Lord Azaram, Duke Krule, Count Vlarkorth, Sir Nictros & Sir Baeloc, Earl Osam, King Zelos;
• Grimvale/Ancient Feud: Katex Blood Tongue, Srezz Yellow Eyes, Utua Stone Sting, Yirkas Blue Scales, Bloodback, Darkfang, Sharpclaw, Shadowpelt, Black Vixen;
• Soul War: Goshnar's Cruelty, Goshnar's Greed, Goshnar's Hatred, Goshnar's Malice, Goshnar's Spite, Goshnar's Megalomania;
• The Dream Courts: The Nightmare Beast, Izcandar the Banished, Alptramun, Plagueroot, Malofur Mangrinder, Maxxenius;
• The Secret Library: Ghulosh, Gorzindel, Lokathmor, Mazzinor, Scourge of Oblivion.
• The SoulWar reward was added. In order to get the reward, the player needs to kill all the bosses and the final boss.
• The Dream Court's World change was added.

• All the access needed were granted on FreeQuests.lua. If you are already running a server, you'll need to update freeQuestStage on config.lua to one number higher than it is. So, all the players of your server will have the access granted.

---
## [Sector-Echo-13-Team/Echotest](https://github.com/Sector-Echo-13-Team/Echotest)@[6d158bd3b3...](https://github.com/Sector-Echo-13-Team/Echotest/commit/6d158bd3b37bba2cb2cec2a27fdb0b9b7d8275ac)
#### Tuesday 2023-03-21 14:13:08 by spockye

beach ruin, The Treasure Cove! (#1701)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
This PR adds a new Beach ruin, Treasure Cove. 

![2023 01 17-11 26
30](https://user-images.githubusercontent.com/79304582/212874736-b17917a5-876e-4a7a-a073-1581cc394b8e.png)

![2023 01 17-11 26
58](https://user-images.githubusercontent.com/79304582/212874824-9a161419-b751-41d2-a82d-e50f06981025.png)


![image](https://user-images.githubusercontent.com/79304582/212879021-bcdc2238-b50b-48c2-9cd0-d17cccbd50dc.png)

Loot: 
cm-16 rifle (main loot)
energy gun
pirate sabre
frontiersmen hardsuit
misc combat supplies
secret documents
2x abandoned crates
research note / tesla researcher
basic engineering supplies (smes/tools/autolathe/battery charger)
two boats
silver crate / hidden gold crate
misc junk
______
Threat: 
1x spacesuit ranged pirate
2x sword pirates
1x ranged pirate
punji sticks
_____

Lore tidbit:
This "humble abode" is the home of our 5- now 4 Pirate friends! After a
mildly successful raid on a CMM VIP transport, they managed to take a
Cargo tech (the VIP), and a CMM guard as hostage. sadly it didn't all go
as planned, and the CMM officer managed to free himself and killed one
of the pirates. This is where you now find the cave, with both hostages
executed, their brother buried, and the pirates grieving his unfortunate
passing.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the
brackets) if you have tested your changes and this is ready for review.
Leave unticked if you have yet to test your changes and this is not
ready for review. -->

- [x] I affirm that I have tested all of my proposed changes and that
any issues found during tested have been addressed.

## Why It's Good For The Game
more ruins = good.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Adds a new beach ruin, the beach_treasure_cove
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
Co-authored-by: Bjarl <94164348+Bjarl@users.noreply.github.com>

---
## [pascua28/android_kernel_samsung_sm8250](https://github.com/pascua28/android_kernel_samsung_sm8250)@[bde49884c6...](https://github.com/pascua28/android_kernel_samsung_sm8250/commit/bde49884c62e624c1e76b44eb84551e8d7497e7c)
#### Tuesday 2023-03-21 14:40:22 by Peter Zijlstra

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
Signed-off-by: Samuel Pascua <pascua.samuel.14@gmail.com>

---
## [AdityaGupta1/Programming-Practice-Client-side-web-APIs](https://github.com/AdityaGupta1/Programming-Practice-Client-side-web-APIs)@[29cca13f82...](https://github.com/AdityaGupta1/Programming-Practice-Client-side-web-APIs/commit/29cca13f82adf4940b03114e6f7b98cadaf8a0dd)
#### Tuesday 2023-03-21 14:41:24 by Aditya Gupta

Are you kidding ??? What the **** are you talking about man ? You are a biggest looser i ever seen in my life ! You was doing PIPI in your pampers when i was beating players much more stronger then you! You are not proffesional, because proffesionals knew how to lose and congratulate opponents, you are like a girl crying after i beat you! Be brave, be honest to yourself and stop this trush talkings!!! Everybody know that i am very good blitz player, i can win anyone in the world in single game! And "w"esley "s"o is nobody for me, just a player who are crying every single time when loosing, ( remember what you say about Firouzja ) !!! Stop playing with my name, i deserve to have a good name during whole my chess carrier, I am Officially inviting you to OTB blitz match with the Prize fund! Both of us will invest 5000$ and winner takes it all! I suggest all other people who's intrested in this situation, just take a look at my results in 2016 and 2017 Blitz World championships, and that should be enough… No need to listen for every crying babe, Tigran Petrosyan is always play Fair ! And if someone will continue Officially talk about me like that, we will meet in Court! God bless with true! True will never die ! Liers will kicked off…

---
## [kugamo/cmss13](https://github.com/kugamo/cmss13)@[e5ab42dba0...](https://github.com/kugamo/cmss13/commit/e5ab42dba06e537df5c146169971dd8418f2ce55)
#### Tuesday 2023-03-21 14:54:57 by boskoramen

Consolidates some XSS under hivecore (#2738)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Spawn pool and evo pods are removed and their functionality is
umbrella'd under the hive core. Sprites still exist though.

# Explain why it's good for the game

"Roleplay" has become an increasingly more popular and touchy subject
within the community as of recently. I, wholeheartedly agree, that
roleplay is an important aspect of the game, and there are ways to
improve it. One of these ways is through immersion. In this MR, it is
intended to increase player immersion.

One of the most memorable and haunting scenes in Aliens was when they
reached the hive and they found the bodies. This very unique and
cinematic scene was often able to be replicated in CM, with the marines
busting open the hive and finding all the chestbursted bodies of their
comrades. Roleplaying this out was commonplace. "Dear God... what did
they do to you..." or acting out in disgust are just a few of the many
ways having bodies in the hive positively impacted the game.

XSS was a failed attempt at spicing up the xenomorph gameplay loop at
the expense of immersion and should be at least somewhat reverted while
keeping balance in mind. A brief discussion with many prominent
xenomorph players, including those most experienced in queen, have not
particularly expressed favor to XSS either.

To start, let us remember why XSS (xeno special structures - hive core,
evo pods, morpher, pool, etc) was added.

https://docs.google.com/document/d/19_zDUmLdxpUzxj-GuWu7F4bSj4zBYzmZ39s_N5X7kQ0/edit
- This is the original development document for XSS.
Let us examine the major points:
1.Introduce a way for Xenomorph players to recycle - This idea was never
reached.

2.Reduce Xenomorph attrition - Grand objective was unsuccessful. Very
little changed.

3. Offer new avenues of play "by reducing the punishment of xenos dying"
- This never happened. Dying was still just as punishing, especially
with facehug nerfs.

The spawn pool - The idea of the spawn pool was successful and has
remained unchanged since. I would argue, however, it is not immersive.
Xenomorphs do not have bright, glowing, acidic pools in their hives.
(Yes I know there was a comic with a pool, and this is not how it was
used)

Egg Morpher - These used to be TURRETS. They are no longer turrets, and
their sprites have been broken for almost 4 years (the bodies put inside
of them used to show their face in the little purple part) They are
currently defunct facehugger reservoirs. I am in favor of removing them,
but I would argue that is a balance issue (number of huggers in play)

Evolution Pod - It was intended for these to be able to be eaten in
order to evolve. They haven't done this for years. Why do we still have
them? They take up 18 spaces of precious hive weeds, provide light,
(xenomorphs HATE light) and wherever a hive core is built, these are
also built. We can just merge them with the hive core because there is
no reason to have them anymore.

This PR currently completely removes the spawn pool and evolution pod
from gameplay, while reimagining their functions for current balance.
This PR is not intended to change balance in any way.

All functionality from the spawn pool in regards to "pooled" larva has
been given to the hive core, and they are now called "burrowed" larva.
Chestbursts now give two larva, this is to be kept with current balance
of two xenos per capture.

Evopod functionality and evolution speed boost was merged with the hive
core.


# Testing Photographs and Procedure
n/a


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

:cl: TheDonkified
del: Evo pods and spawn pool are removed.
add: Hive core directly affects evolution speed and is where burrowed
larva spawn from now on.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: Morrow <darthbane97@gmail.com>
Co-authored-by: harryob <me@harryob.live>

---
## [kugamo/cmss13](https://github.com/kugamo/cmss13)@[d40fdb9101...](https://github.com/kugamo/cmss13/commit/d40fdb91011bb0aa4053a9386311ed131e0ae6ac)
#### Tuesday 2023-03-21 14:54:57 by NewyearnewmeUwu

nukes the last default ss13 door on big red (#2830)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
i thought i fixed this?
didn't i guess
removed the weirdass ss13 door in the OR theater's observer area yeah
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
it's ugly
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
maptweak: removed yet another default ss13 door from big red
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [NetworkManager/NetworkManager](https://github.com/NetworkManager/NetworkManager)@[7ca95cee15...](https://github.com/NetworkManager/NetworkManager/commit/7ca95cee15b32af2452aaf4a165eb5c634fba132)
#### Tuesday 2023-03-21 15:02:29 by Thomas Haller

platform: always reconfigure IP routes even if removed externally

NML3Cfg is stateful, that means it remembers which address/route it
configured earlier. That is important because the API users of NML3Cfg
only say what the want to configure now, and NML3Cfg needs to remove
addresses/routes that it configured earlier but are no longer to be
present. Also, NetworkManager wants to allow the user to add
addresses/routes externally with `ip addr|route add` and NetworkManager
not removing it. This is a common use case for dispatcher scripts, but
in general, we want to allow other components to add addresses/routes.

We try something similar with the removal of routes/addresses managed by
NetworkManager. When NetworkManager adds a route/address, which later
disappears, then we assume that the user intentionally removed the
address/route and take the hint to not re-add it.

However, it doesn't work. It is problematic for two reasons:

- kernel can automatically remove routes. For example, deleting an IPv4
  address that is the prefsrc of a route, will cause kernel to delete
  that route. Sure, we may be unable to re-configure the route at this
  moment, but we shouldn't remember indefinitely that the route is
  supposed to be absent. Rather, we should re-add it when possible.

- kernel is a pain with validating consistencies of routes. For example,
  when a route has a nexthop gateway, then the gateway must be onlink
  (directly reachable), or kernel refuses to add it with "Nexthop has
  invalid gateway". Of course, when removing the onlink route kernel is
  fine leaving the gateway route behind, which it would otherwise refuse
  to add.
  Anyway. Such interdependencies for when kernel rejects adding a route
  with "Nexthop has invalid gateway" are non-trivial. We try to work
  around that by always adding the necessary onlink routes. See
  nm_l3_config_data_add_dependent_onlink_routes(). But if the user
  externally removed the dependent onlink route, and NetworkManager
  remembers to not re-adding it, then the efforts from
  nm_l3_config_data_add_dependent_onlink_routes() are ignored. This
  causes ripple effects and NetworkManager will also be unable to add the
  nexthop route.

Trying to preserve absence of routes that NetworkManager would like to
configure is not tenable. Don't do it anymore. There was anyway no
guarantee that on the next update NetworkManager wouldn't try to re-add
the route in question. For example, if the route came from DHCP, and the
lease temporarily went away and came back, then NetworkManager probably
would have (correctly) forgotten that the user wished that the route be
absent. This did not work reliably and it just causes problems.

---
## [seahop/UACME](https://github.com/seahop/UACME)@[c65f9215c1...](https://github.com/seahop/UACME/commit/c65f9215c1103269ca31f66f49869fcde547af98)
#### Tuesday 2023-03-21 15:18:26 by hfiref0x

Update Naka.vcxproj

Retarget platform toolset for appveyor fail. I understand that this service is currently busy supporting %current thing% more than actually working on their script-shit, but holy fuck seriously.

---
## [dscho/git](https://github.com/dscho/git)@[e413f96a42...](https://github.com/dscho/git/commit/e413f96a42f558dfdc589f3e4a1e814da8d0473f)
#### Tuesday 2023-03-21 15:22:00 by Johannes Schindelin

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
## [bmccrat/songage](https://github.com/bmccrat/songage)@[5d5258ca96...](https://github.com/bmccrat/songage/commit/5d5258ca96e2a8887556ddb532eeb535a11229a8)
#### Tuesday 2023-03-21 15:57:42 by bmccrat

Create R.S.V.P.

RSVP stands for Ryan Scott Van Pouke a dear friend of mine and mutual crush from treatment at the Hazelden outpatient center that died of an overdose in supportive living in St Paul Minnesota. I was in a treatment center in Chicago at the time that his funeral was, and he was from Chicago so his funeral was there. It just so lined up that I got kicked out of treatment on the same day as his funeral so I packed my bags and headed for the funeral home. I got there and was shooting dope the whole time in the bathroom, where right outside the door a mother was mourning her son thet had just died from the poison I was using. On the flight home after the funeral I overdosed on the plane and ended up in the hospital for some days in NC. When I got home I wrote this song about Ryan as I was still grieving him. I wonder if you wondered that before you died or if your reaper looked black and empty just like mine, was a connection between our two deaths, one more permanent than the other. Bless his soul

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[de42a18c0a...](https://github.com/mrakgr/The-Spiral-Language/commit/de42a18c0a3eea09e7f50d4cabd0a836fbed899d)
#### Tuesday 2023-03-21 18:08:43 by Marko Grdinić

"7:25am. I lounged in bed for a while, so I am surprised I got up this early. Let me turn on Thunderbird and check my mail.

Barclays is telling me that my application is incomplete. Yeah, because its site was so broken I couldn't finish it. Let me give it a shot again.

> You must select ALL possible values in the section Place of Residence.

For fuck's sake, there isn't such a section.

7:40am. Managed to find the email through that bot. Instead of an email, they have a multiple choice agent, and I manage to pry the actual email out of it by telling it I have issue uploading the resume.

Anyway, nevermind that.

7:45am. I shouldn't have done this as it is very unlikely I'll get a job, so it was just a waste.

8:30am. I just figured out what the average policy update is doing! I have an intuitive explanation!

```fs
                    Array.map2 (fun act policy_prob ->
                        if fst path_prob = 0 && snd path_prob = 0 then 0.0
                        else cont (act, path_prob *. policy_prob)
                        ) actions current_policy
```

Also, I don't think this is the correct pruning.

```fs
        interface IAction<'model,'action> with
            member this.action(model, actions, path_prob, cont) =
                if fst path_prob = 0 && snd path_prob = 0 then 0.0
                else
                    let current_policy : float [] = get_policy d model actions
                    let rewards =
                        Array.map2 (fun act policy_prob ->
                            cont (act, path_prob *. policy_prob)
                            ) actions current_policy
                    let avg_reward = Array.fold2 (fun s x policy_prob -> s + x * policy_prob) 0.0 rewards current_policy
                    update_policy model actions rewards avg_reward path_prob
                    avg_reward
```

But is pruning right to begin with? Returning 0.0 might bias the results.

Let me get rid of pruning, let me get rid of it!

9:25am. Oh wow, the words are coming to me so smoothly now and without stumbling. It feels like I've leveled up my talking skill!

10:50am. Done with the video. It really hard to prevent mouth noise. Often while I am in the middle of a sentence my mouth would get moist and the mic would pick up the saliva swirling. But I've ignored that during this recording and my ability to make content has gone way up.

I've exported the audio. It is time to give the RX Editor a try for the first time. Let's see what its got.

11:05am. This program has a repair assistant which might be ML based. I've clicked on Learn and now it will take like 10m to figure out all the module settings itself.

Ah, whatever. While this is going on, I might as well watch some tutorials on the software. The UI is pretty good, and it strikes me as being easy to use.

https://youtu.be/CFvGPBE22yM
How to Clean Up Voice Recordings for Videos and Podcasts | iZotope RX

Let me check this out.

https://youtu.be/CFvGPBE22yM?t=138

This is a good video.

https://youtu.be/CFvGPBE22yM?t=169
> So if we had birds chirping, or some weird mouse noises of plosives, there is not many ways we can deal with this in this view.

https://youtu.be/CFvGPBE22yM?t=184

What's the spectral view?

https://youtu.be/CFvGPBE22yM?t=240

Yeah, it goes back to my philosophy. The easiset way to get better at something is to get a better tool.

https://youtu.be/CFvGPBE22yM?t=813

I'll have to try the output clicks only feature.

Let me give it a try.

12:35pm. https://youtu.be/CFvGPBE22yM?t=1162

I am playing around, but plosives and noise reduction do nothing for me. The background noise is at -50db, so it is no wonder nothing is happening to reduce it. It simply isn't audible in the recorded audio.

12:55pm. https://youtu.be/eMT2DP1pha8
How to meet global loudness standards | iZotope RX Loudness Control

At 196k subscribers, this is a very popular channel.

There is no way around it. Today before I post the video on Youtube, I am going to have to spend time studying this program. I know some tricks in Reaper, but here I don't know how to even normalize the audio. Thankfully the modules are straightforward to use.

I do not understand why de-plosive doesn't seem to be doing anything for me.

file:///C:/Program%20Files/iZotope/RX%20Pro%20Audio%20Editor/HTML%20Help/en/loudness/index.html

Oh this is a very good, loudness control. Instead of messing with it like in Reaper, I can just set the LKFS to -16, and the true peak to -4 and it will be exactly that.

> When computing Integrated loudness, certain low-level signals are excluded from the computation in order to only measure the loudness of “typical” signal levels. This is called gating and is a part of the BS.1770-2, 3 standards (and also R128). Firstly, all signals with a Momentary loudness below −70 LKFS are excluded, so that the noise floor in pauses does not bias the computed loudness. Secondly, all signals with a lower Momentary loudness than 10 dB (or LU) below the average Momentary loudness are also excluded. This allows the computation of the Integrated loudness only from the typical and loudest parts of the program, while excluding silence and quieter parts, which have less effect on the listener’s impression of overall loudness of the program . Most of the loudness standards shipping with RX Loudness Control use gating, an exception being BS.1770-1. This parameter allows you to toggle gating on or off, if you’re working to a unique requirement.

Informative. I had noticed that the empty parts do not affect the loudness calculations.

1:10pm. https://www.youtube.com/@iZotopeOfficial/playlists

This has a lot of material.

https://www.youtube.com/playlist?list=PL4dISychPQEuXyAaGGZ2dbYaOJ0-1DYFo
How to Clean Up Podcast Audio with RX Elements

Exactly what I need.

https://youtu.be/d0WN8VSYHRk?list=PL4dISychPQEuXyAaGGZ2dbYaOJ0-1DYFo
How to Remove Mouth Noises from Podcasts

Let me stop here, I'll watch this later. I like how the RX audio editor only has a few dozen key well named plugins unlike Reaper which has a ton of them.

2:05pm. Done with breakfast. Next are chores.

3pm. Done with chores. Let me spend the following time, watching Rx audio editor tutorials. Let me get started on this.

https://youtu.be/d0WN8VSYHRk?list=PL4dISychPQEuXyAaGGZ2dbYaOJ0-1DYFo
How to Remove Mouth Noises from Podcasts

I started watching this during breakfast, and it really was disgusting.

https://youtu.be/D9IreQj8-Z8?list=PL4dISychPQEuXyAaGGZ2dbYaOJ0-1DYFo&t=80

Hmmm, is this a compressor?

https://www.google.com/search?q=VocalSynth&oq=VocalSynth&aqs=chrome..69i57j0i512l4j0i30l2j69i61.688j0j7&sourceid=chrome&ie=UTF-8
A vocal synthesizer is easily defined as 'an electronic instrument that generates and combines the basic elements of sound to produce simulated speech, typically used in computer systems.

Hmmm, It is only a matter of time until the neural net stuff lands in the vocal synthesizer.

https://youtu.be/5bnMne9U8t8?list=PL4dISychPQEuXyAaGGZ2dbYaOJ0-1DYFo&t=144

What is this?

https://youtu.be/jRLWVvizEI4?list=PL4dISychPQEvEqoE8UnmmZlvjnl7t3Iz9&t=33

Why are the UI interfaces for all of these so different from mine. Also how do you put in multiple tracks for this. Nevermind that for now.

https://youtu.be/vSR41j-Yg6c
iZotope RX: Why Is Everyone In Love With This Thing?

https://youtu.be/0OnTbxlI8s0?list=PL4dISychPQEvEqoE8UnmmZlvjnl7t3Iz9
How to Use Everything in iZotope RX 10 for Music Creators

These two are by the same guy. Let me start with the first one.

I really should just read the docs for these. There is surprisingly little on Youtube. I mean obviously, there is a lot, but it is scattered about.

> The “Open as Module Chain” feature allows you to save Repair Assistant’s recommendations as a Module Chain preset, or make changes to the generated settings before rendering. To open Repair Assistant’s recommendations in the Module Chain, click the Open as Module Chain button in the Repair Assistant footer area. (This feature is available in RX 10 Advanced only).

Ah, I see. I was wondering why those other UIs didn't have this.

file:///C:/Program%20Files/iZotope/RX%20Pro%20Audio%20Editor/HTML%20Help/en/mouth-de-click/index.html
> Running Mouth De-click twice sometimes produces a better result than a single pass. This is because an initial run can miss the quieter clicks that were masked by louder clicks.

Oh this is on my hard drive.

file:///C:/Program%20Files/iZotope/RX%20Pro%20Audio%20Editor/HTML%20Help/en/leveler/index.html

A lot of these tools seem to be doing the same thing.

4:40pm. Right now I am just playing with the audio repair. Learning on the whole clip, then using the loudness control to normalize it -16 LUFS and true peak of -4 is the best. I can't really tell the difference with what a lot of the nodes do. Thel leveler for example. But just using the audio repair gives impressive improvements. Well worth the price of get this program.

This is a lot more convenient that Reaper.

Let me watch that video I started. I want to see whether I can get even more value by adding some extra nodes on top of the regular repair.

https://youtu.be/vSR41j-Yg6c?t=166
> My advice to people would be: Rx is one of those things that you should really learn how to make most of.

https://youtu.be/vSR41j-Yg6c?t=785

How does he get that interactive thing.

https://youtu.be/vSR41j-Yg6c?t=899
> I can't hear the hum right now, but when I add the stuff, like compression and stuff...

https://youtu.be/vSR41j-Yg6c?t=1277
> I couldn't see a hum in the waveform. Where is the hum?

https://youtu.be/vSR41j-Yg6c?t=1590

Is he talking about the breaths?

https://youtu.be/vSR41j-Yg6c?t=1671

I can't tell these plosives apart at all from the regular sound!

https://youtu.be/vSR41j-Yg6c?t=1806
> And I press compare.

Let me give this a try.

Oh, I see. This does make an effect on the spectrogram.

I can click on the compare window, and change some settings, and it will add another item with the changed settings in the list. Cool. I can add this to the module chain. No reason not to.

https://youtu.be/vSR41j-Yg6c?t=2542

This is pretty interesting.

6:05pm. Done with that video.

https://youtu.be/2svTCBlMIP0
Leveling Dialogue Audio with Izotope RX or any other Leveling Plugin

Let me watch this.

https://youtu.be/2svTCBlMIP0?t=496

This is pretty informative as to what the leveler should be used for.

https://youtu.be/o0CN2xlLMnk
Telling Stories with iZotope RX: Powerful Dialogue Editing, Part 1

6:20pm. Agh, I do not want to watch this right now. I am done for the day. Let me reimport it in Camtasia.

6:30pm. Let me pause the video at 5:30pm. So far I do not hear any mouth noises whatsoever. I actually did two passes of mouth de-click in total as per advice.

6:35pm. Those 5:30m that I listened to really feel great. My voice is crystal clear.

I no longer need to feel a sense of inferiority to those pro podcasters, and being able to just push a button to fix my audio problems will make future recordings much easier.

At this point I really should be using ChatGPT to tell me how to do various things instead of winging it all on my own and wasting time. I'll seriously have to find ways of including into my work. When I start work on Hatred, I should find ways of including writing, art and audio generating AIs into my workflow. AI agents are the only thing that can save me now."

---
## [mullenpaul/cmss13](https://github.com/mullenpaul/cmss13)@[ef9d0c61a3...](https://github.com/mullenpaul/cmss13/commit/ef9d0c61a3335d40c9bd9459479e0112903ccc02)
#### Tuesday 2023-03-21 19:42:57 by Moonshanks

Altitude Control: Console, Skills, TGUI, Shuttle, OB, And Hijack changes. (#2760)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
This pull request adds a feature via the
/machinery/computer/attitude_control_console.

The USS Almayer can now be "moved" between three different levels of
orbit/proximity to the AO:

High,
Optimal,
Low

Each level comes with changes to the duration of transport timers, time
to transport during hijack, and OB cooldown timer, equal to the
GLOB.ship_alt value.

High makes OB cooldowns take 200 seconds longer, dropship transport
times take 50% longer, and the dropship hijack transport time take 50%
longer

Optimal, the default which will stay in place if no one touches the
console leaves everything with their default times and cooldowns,

Low, OB cooldowns take 200 shorter, dropship transport times are 50%
shorter, the dropship hijack transport time is 50% shorter.

While in Low orbit the Almayer will periodically shake (50% chance to
shake every 30 seconds), the Almayer's thrusters will also start
building up heat as they battle with making minor adjustments due to the
dangerous proximity to the AO. They will gain 10% of their max heat each
30 seconds, once they reach 100% the ship will be forced into the
highest orbit to cool off, and cool off slower than normal (5% every 30
seconds) until its orbit is changed.

While in Optimal or High orbit the Almayer thrusters will cool off by
10% per 30 seconds.

The Almayer's orbit may only be changed by those with a "navigations"
skill of 1. (only the CO and Synth -- EDIT: XO now has the skill too --
currently but I may add a dedicated RP role for this mechanic later down
the line). The orbital level may only be changed every 90 seconds and
when it changes the ship will shake violently causing every mob on the z
level to fall over.

This PR does not place the Altitude Control Console on the map, so
currently, these features don't do anything within a normal round unless
staff spawns in the console, however I will be uploading a mapping PR
changing the Astronavigations deck if this PR is accepted.

Planned for the future but not yet approved connected to this PR is the
"Navigations Officer" the highest auxiliary support personnel with
skills the same as an SO, sans a 1 in Navigations, and a 1 or 2 in
piloting. The idea for this future role would be set out in the PR, but
it would represent a mainly fluff officer role that was unable to deploy
under normal SoP.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

This PR is a non-intrusive way to add more nuanced gameplay mechanics to
COs, especially on the quieter rounds when they aren't swamped by OW
duties.

The way the PR is currently designed it doesn't effect any gameplay
balance if it isn't used. If a CO however chooses to use it they have to
pay some level of attention to it or they will overheat the engines and
cause their transport times to be lengthened.

It's a relatively simple way to add more complexity to CIC, and give the
CO/Synth more stuff to do to gain a slight edge.

I have been able to test everything other than the hijack time increase.
However, the line of code handling the hijack time increase is one line
long. Everything else is confirmed as working and the common bugs this
could create have been tested for and not found (transport shows the
right time when the time is modified, OB shows the right cooldown time,
the cooling can't drop the heat% below 0 nor above 100, the TGUI works
without issues, the console can only be used by those with the right
skills, and the knockdown effects all mobs on the Almayer not just
humans).

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

https://www.youtube.com/watch?v=-cbnqNtKyCY - video showing the CO and
Synth using the console, with the knockdown effect and arrest radio
announcements.

https://youtu.be/Qd37iM-4FrQ - video of the overheat function and the
ship shaking due to low orbit

https://www.youtube.com/watch?v=EWLCDZp-9iI - video of the ship being
left on low orbit for too long, and what happens when the engines
overheat

https://www.youtube.com/watch?v=u_ErqfU-nus - video showing the orbital
distance effecting the transport time

https://www.youtube.com/watch?v=j687yqlWLT8 - video showing high orbit
effecting the OB cooldown time.

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
add: added altitude control console and related mechanic
add: added the 'navigations' skill for using the console and applied it
to the CO/Synth
balance: added a mechanic for COs to reduce transport and OB cooldown
times, and increase hijack transport times
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: harryob <me@harryob.live>

---
## [openai/evals](https://github.com/openai/evals)@[b5da073c21...](https://github.com/openai/evals/commit/b5da073c215c6453b99269a6dab2dca5454f04dd)
#### Tuesday 2023-03-21 20:03:44 by somerandomguyontheweb

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
## [openai/evals](https://github.com/openai/evals)@[b170a21cf3...](https://github.com/openai/evals/commit/b170a21cf32c47d841f64ec110cfd6796ec3f89a)
#### Tuesday 2023-03-21 20:16:11 by Sam Ennis

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
## [dellsystem/notes-from-below](https://github.com/dellsystem/notes-from-below)@[bfd829148b...](https://github.com/dellsystem/notes-from-below/commit/bfd829148b1e00f51cf736f66e883d0b96823614)
#### Tuesday 2023-03-21 20:36:03 by dellsystem

Update requirements.txt for new dependabot crap

the updates never fuckin end im sick and tired of this shit

---
## [QueenOfSquiggles/Squiggle-Zone-Game-Base](https://github.com/QueenOfSquiggles/Squiggle-Zone-Game-Base)@[3698cdcd3d...](https://github.com/QueenOfSquiggles/Squiggle-Zone-Game-Base/commit/3698cdcd3df59505922b3224523f66ee35ab4be8)
#### Tuesday 2023-03-21 21:31:57 by QueenOfSquiggles

Holy Fucking Hell Item System Kinda Working

I did a lot of work on this commit because I'm a real bad dev who has no concept of small portion sizes. Just like my unending hunger for the flesh of the damned I am equally hungry for PROGRESS. Beware mortals who enter here. This wretched code shall curse your soul. And those who lurk in the dark have no qualms or query, beware all ye weary!

---
## [ivanmixo/tgstation](https://github.com/ivanmixo/tgstation)@[33d9a0338f...](https://github.com/ivanmixo/tgstation/commit/33d9a0338f1d6811162479e337dbd0945463a8e8)
#### Tuesday 2023-03-21 21:39:43 by LemonInTheDark

Reworks trashbags slightly (#73761)

## About The Pull Request

I'm a bit sad about the state of trashbags. 
They're very clunky to use, so they almost never get touched. S
depressing. Let's try and fix that.

Let's make em fit in the belt slot (again), but as a tradeoff we'll make
it harder to pull one thing from your bag.
We'll give it a say, 1.5 second delay, so you can't quickdraw from em.
If you try and dump them out into something else, we'll throw any
spillover on the ground below you

I'm also doing some general code cleanup here. Making procs more
readable, vars more direct, removing some old legacy stuff.
I've added a remove_single proc to hook into via subtype, which takes a
mob as input. this has required placing extra requirement on some helper
procs, but fortunately it's not something they're unable to meet.

My hope is this will make garbage bags usable without being stupid.

## Why It's Good For The Game

I don't see these get used at all, cause they're a pain to carry around.
They got gimped because people were using them as infinite storage for
shotgun shells and other small items.
I've made using them for this sort of thing hard and slow, so I think we
oughta be fine. If not I'll do some more touching, maybe give the
autodrop a delay.

## Changelog
:cl:
balance: The janitor's trashbag now fits on his belt. In exchange,
taking something out of it sends a visible message, and has a delay.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [ivanmixo/tgstation](https://github.com/ivanmixo/tgstation)@[1dad66101d...](https://github.com/ivanmixo/tgstation/commit/1dad66101d498eeed8aad73d17f142b631cc0f0e)
#### Tuesday 2023-03-21 21:39:43 by TheSmallBlue

All hail The Pickle Jar, harbringer of better crafting (#73939)

## About The Pull Request
Fixes #73841 

---

_It is the 12th of March, 2023. Around 3am. I have published a Pull
Request which involves circuits, and got reminded of my low GBP. I go
into the issues tab to see if there's anything someone of my low skill
caliber could tackle. I see it; Pickles.
"How hard could I be?" I ask myself, foolishly unaware of the dangers
that would soon overcome me.
Surely it must've been a mistype, I thought. Surely someone accidentally
confused pickles and cucumbers.
"Wait, the pickles are supposed to be created on the jar when the jar is
created", I say foolishly.
"Wait, its putting the ingredients used for the jar in the jar, that
doesn't explain why the pickles aren't there though", I say foolishly
"Wait, whoever tried fixing this earlier fucking qdel'd the beaker and
called it a day????", I say, foolishly._

---

Anyways I changed how the crafting menu distincts between categories,
instead of checking whether or not the path is for food, it checks the
actual categories themselves (why didn't it do this already), meaning
that you can have non-food items on the food tab if it has a food
category. Did this by adding a list that includes all crafting
categories, so in the future when adding new categories you'll have to
add them twice, which sucks, but oh well.

Also added a new variable to craftable items, which makes it so that you
can not delete a container's contents if you so wish (why was this the
default).

All this so that when you craft pickles, it actually crafts pickles
instead of cucumbers.

I spent hours on this, its 6:30am as I'm typing this. I'm tired. Fucking
pickles.

Super duper ultra thanks to FinalPotato for guiding me and suffering
with me through this and teaching me so much about DM and BYOND. I
cannot emphasize just how helpful and awesome they were thank you thank
you thank you <3
## Why It's Good For The Game

Bug fixing be good
## Changelog
:cl:
fix: The jar of pickles, after millenia, finally actually contains
pickles. All hail the jar of pickles.
/:cl:

---
## [ivanmixo/tgstation](https://github.com/ivanmixo/tgstation)@[60e85fa947...](https://github.com/ivanmixo/tgstation/commit/60e85fa947799e20419dc867a238afb27b840e59)
#### Tuesday 2023-03-21 21:39:43 by LemonInTheDark

Polishes some side sources of light and color (#73936)

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

---
## [ivanmixo/tgstation](https://github.com/ivanmixo/tgstation)@[e47c47a081...](https://github.com/ivanmixo/tgstation/commit/e47c47a081f5919eea2b43453be7ac011ee2a492)
#### Tuesday 2023-03-21 21:39:43 by MrMelbert

You can't instantly resist out of an unlocked labor camp teleporter if you are handcuffed (#73983)

## About The Pull Request

If you are restrained, and placed into an unlocked labor camp
teleporter, you cannot instantly resist out of it. However the resist
timer is cut in half while unlocked.

## Why It's Good For The Game

Getting someone into the gulag teleporter is an incredibly un-necessary
pain in the rear because simply *spamming resist* turns it into a game
where you have to shove them in, then really quick go over to the
computer and slam the lock button. This is... kinda lame. A lot of new
player security officers get got by this, and I think it's sad. Inb4
"Skill issue"

## Changelog

:cl: Melbert
balance: If you are handcuffed, you can't instantly resist out of an
unlocked labor camp teleporter (however, resist time is halved).
/:cl:

---
## [git/git](https://github.com/git/git)@[eaa0fd6584...](https://github.com/git/git/commit/eaa0fd658442c2b83dfad918d636bba3ca3b4087)
#### Tuesday 2023-03-21 22:07:38 by Jeff King

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
## [colegaboriault/trail](https://github.com/colegaboriault/trail)@[3af3604d91...](https://github.com/colegaboriault/trail/commit/3af3604d910c9bcaaef297c93d558fc76952095e)
#### Tuesday 2023-03-21 23:24:57 by colegaboriault

High Camp, 4216

This trip would be so much more enjoyable without the fucking people; I
was feeling like shit at dinner, but as soon as the Hiking associates
got in bed and the other campers were out of earshot, I looked upon
the vista and felt alibe.

---
## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[4e3c9ccc66...](https://github.com/realforest2001/forest-cm13/commit/4e3c9ccc66f268b7e07db58470af2a170f4857a1)
#### Tuesday 2023-03-21 23:59:49 by roll1d20st

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
## [Ableez/quotes](https://github.com/Ableez/quotes)@[fe96411be4...](https://github.com/Ableez/quotes/commit/fe96411be4b88babafad36819d4cb1027b2d4877)
#### Tuesday 2023-03-21 23:59:56 by ableez

    Add CSS animations: You can use CSS animations to
    add some subtle animations to your app. For example,
    you can add a fade-in animation when the quotes are
    loaded, or an animation when the user clicks the
    "Next Quote" button. There are many CSS animation
    libraries you can use, such as Animate.css or
    React Spring.

    Add a random quote button: In addition to the "Next Quote"
    button, you can also add a "Random Quote" button that
    selects a random quote from the list. This can make the
    app more dynamic and interesting to use.

    Add a sharing feature: You can add a feature that
    allows users to share the current quote on social media.
    You can use a library like react-share to implement this.

    Add a search feature: You can add a search feature that
    allows users to search for quotes by keyword or author.
    This can make it easier for users to find quotes that are
    relevant to them.

    Add a like/dislike feature: You can add a feature that allows
    users to like or dislike quotes. This can help you to understand
    which quotes are most popular and can also help to personalize
    the app for individual users.

Remember, the key is to keep your app simple and user-friendly,
while adding features that enhance the user experience.

---

