## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-04-27](docs/good-messages/2023/2023-04-27.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,186,088 were push events containing 3,420,215 commit messages that amount to 259,523,917 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 63 messages:


## [meemofcourse/Shiptest](https://github.com/meemofcourse/Shiptest)@[7df4885117...](https://github.com/meemofcourse/Shiptest/commit/7df4885117a4a12ea333934d5af92e0766c84c5d)
#### Thursday 2023-04-27 00:03:46 by Mark Suckerberg

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
## [SquidDOTjpeg/TGBL](https://github.com/SquidDOTjpeg/TGBL)@[d9d6087865...](https://github.com/SquidDOTjpeg/TGBL/commit/d9d6087865e01b4c028ef9e4314de3f48b96ae15)
#### Thursday 2023-04-27 00:05:42 by Anthony Pillow MacBook

Finally got the protected route working. Got rid of route guard and added the AuthService file (which needs a logout function still). Total pain in the ass. That being said there's more pain on the horizon with me having to figure out how I set one token for the whole site instead of having a token per page. Which is happening I guess. I love dev but I hate dev so much.

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[99b655dc5d...](https://github.com/cockroachdb/cockroach/commit/99b655dc5d84bf58ccf060493658a015b5cb3f21)
#### Thursday 2023-04-27 00:08:44 by craig[bot]

Merge #99174 #99624 #99699 #99759 #99813 #99839 #99865 #99878

99174: sql: fix circular dependencies in views r=rharding6373 a=rharding6373

This change fixes node crashes that could happen due to stack overflow if views were created with circular dependencies.

Fixes: #98999
Epic: none
Co-authored-by: chengxiong@cockroachlabs.com

Release note (bug fix): If views are created with circular dependencies, CRDB returns the error "cyclic view dependency for relation" instead of crashing the node. This bug is present since at least 21.1.

99624: testutils: add infrastructure for reusable test fixtures r=RaduBerinde a=RaduBerinde

Certain storage-related tests/benchmarks generate fixtures and attempt to reuse them across invocations. This is important because fixtures can be large and slow to generate; but more importantly the generation is non-deterministic and we want to use the exact same fixture when comparing benchmark data.

Currently the tests achieve this by using a `.gitignore`d subdirectory inside the source tree. This does not work with bazel (which executes the test in a sandbox).

This commit addresses the issue by adding new test infrastructure for reusable fixtures. We use the user's `.cache` directory instead of the source tree (specifically $HOME/.cache/crdb-test-fixtures/...). For bazel, we make sure the path is available (and writable) in the sandbox and we pass the path to the test through an env var.

Fixes #83599.

Release note: None
Epic: none

99699: spanconfig: integrate SpanConfigBounds with the Store and KVSubscriber r=ajwerner a=arulajmani

This patch integrates `SpanConfigBounds` with the `KVSubscriber` and
`spanconfig.Store`. The `spanconfig.Store` used by the `KVSubscriber`
now has a handle to the global tenant capability state. It uses this to
clamp any secondary tenant span configs that are not in conformance
before returning them.

By default, clamping of secondary tenant span configurations is turned
off. It can be enabled using the `spanconfig.bounds.enabled` cluster
setting. The setting is hidden.

Fixes: https://github.com/cockroachdb/cockroach/issues/99689
Informs #99911

Release note: None

99759: roachtest: set lower min range_max_bytes in multitenant_distsql test r=rharding6373 a=rharding6373

The multitenant_distsql roachtest relies on a smaller range size than the new default min of range_max_bytes (64MiB) due to performance and resource limitations. We set the COCKROACH_MIN_RANGE_MAX_BYTES to allow the test to use the smaller range.

Fixes: #99626
Epic: None

Release note: None

99813: spanconfig: do not fatal in NeedsSplit and ComputeSplitKey r=irfansharif a=arulajmani

See individual commits for details. 

Fixes #97336.

99839: schemachanger: Annotate all tables if ALTER TABLE IF EXISTS on non-existent table r=Xiang-Gu a=Xiang-Gu

Previously, if table `t` does not exist, `ALTER TABLE IF EXISTS t` will only mark `t` as non-existent. This is inadequate because for stmt like `ALTER TABLE IF EXISTS t ADD FOREIGN KEY REFERENCES t_other` we will not touch `t_other` and the validation logic will later complain that `t_other` is not fully resolved nor marked as non-existent. This commit fixes it by marking all tables in this ALTER TABLE stmt as non-existent if the `t` is non-existent, so we can pass the validation.

Fixes issues discovered in #99185
Epic: None

99865: roachtest: fix query used to get job status in backup/mixed-version r=srosenberg a=renatolabs

At the moment, we only query job status in mixed-version state (so we should always use `system.jobs`). However, the code added in this commit should continue to work once we start developing 23.2, as we're checking that the cluster version is at least 23.1 before using `crdb_internal.system_jobs`.

Epic: none

Release note: None

99878: jobs: change job_info.info_key to string r=dt a=dt

Release note: none.
Epic: none.

Hopefully we get this one in now before it is released and harder to change later. I think if we go with bytes, we'll spend the next several years typing convert_to over and over, or forgetting to and then typing it, when debugging.

Co-authored-by: rharding6373 <rharding6373@users.noreply.github.com>
Co-authored-by: Radu Berinde <radu@cockroachlabs.com>
Co-authored-by: Arul Ajmani <arulajmani@gmail.com>
Co-authored-by: Xiang Gu <xiang@cockroachlabs.com>
Co-authored-by: Renato Costa <renato@cockroachlabs.com>
Co-authored-by: David Taylor <tinystatemachine@gmail.com>

---
## [Cheshify/tgstation](https://github.com/Cheshify/tgstation)@[3861627c66...](https://github.com/Cheshify/tgstation/commit/3861627c66747fb27b18f8bf76a3c9dfd2023001)
#### Thursday 2023-04-27 00:09:20 by LemonInTheDark

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
## [colegaboriault/trail](https://github.com/colegaboriault/trail)@[f23df2a188...](https://github.com/colegaboriault/trail/commit/f23df2a1881c0c4f143f9bf8e32336bf6dcf3866)
#### Thursday 2023-04-27 00:16:00 by colegaboriault

Livin on a prayer

Holy shit I though this would stop at 7, then 7:30, then 8, but still
it playes on. I think it is a loop. Who would dream of such a thing.
Every hostel i say no more hostels, then we forget and fall for some
kind of hostel trap all over again. This miscarriage of justice cannot
stand

---
## [bearrrrrrrr/coyote-bayou](https://github.com/bearrrrrrrr/coyote-bayou)@[d188513e9e...](https://github.com/bearrrrrrrr/coyote-bayou/commit/d188513e9e6871ce027e9b9d5c65c3318a0d0b3f)
#### Thursday 2023-04-27 00:31:02 by Jess

Merge pull request #2066 from jinxynii/master

stop cheesing my fucking dungeon you god damn LOSERS

---
## [Hatterhat/Skyrat-tg](https://github.com/Hatterhat/Skyrat-tg)@[74dc72b867...](https://github.com/Hatterhat/Skyrat-tg/commit/74dc72b867c1b841c71ec1dedcacff8a64167253)
#### Thursday 2023-04-27 00:31:41 by SkyratBot

[MIRROR] Config Flag to Save Generated Spritesheets to Logs [MDB IGNORE] (#20738)

* Config Flag to Save Generated Spritesheets to Logs (#74884)

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

* Config Flag to Save Generated Spritesheets to Logs

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [savetheclocktower/pulsar](https://github.com/savetheclocktower/pulsar)@[71d4ad1d07...](https://github.com/savetheclocktower/pulsar/commit/71d4ad1d076f097a5a53a107209ccc3f332954e7)
#### Thursday 2023-04-27 00:49:45 by Andrew Dupont

Restore `core.useTreeSitterParsers` setting…

…along with a temporary `core.useExperimentalModernTreeSitter` setting.

If we truly planned to keep three different language modes around indefinitely,
changing `core.useTreeSitterParsers` to an enum would make sense. But we don't,
so it'd actually just be a gigantic pain in the ass to migrate one setting to
another of a different type.

When we ship modern-tree-sitter experimentally, we'll make it opt-in via the
temporary setting. When we make it the official tree-sitter implementation and
remove the legacy node-tree-sitter version, we'll remove the temporary setting
and just change the semantics around `core.useTreeSitterParsers`.

Reverting the addition of the `core.languageParser` setting is a chore, but it
prevents a _gigantic_ future headache.

---
## [meemofcourse/Shiptest](https://github.com/meemofcourse/Shiptest)@[b5dc4835a6...](https://github.com/meemofcourse/Shiptest/commit/b5dc4835a6af4fc2ee07e2d26e86382b3d0fb1ab)
#### Thursday 2023-04-27 00:52:48 by Bjarl

New Ruin: Singularity Research Lab (#1612)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->
Adds the Singularity Research Lab, formerly a cutting edge science
station, now overrun with kudzu, it is a space ruin.
<!-- Tick the box below (put an X instead of a space between the
brackets) if you have tested your changes and this is ready for review.
Leave unticked if you have yet to test your changes and this is not
ready for review. -->
![2022 11 25-10 46
03](https://user-images.githubusercontent.com/94164348/204041197-027d9a73-8707-4a00-ad5c-1afcfeff13e0.png)
![2022 11 25-10 46
14](https://user-images.githubusercontent.com/94164348/204041200-98d1a2ac-112c-4c4f-b1ff-d0c1e5a59e81.png)
![2022 11 25-10 46
06](https://user-images.githubusercontent.com/94164348/204041203-4e84a947-8ec9-476d-ae8e-aa9bc17c101a.png)

The two areas of note are the singularity reactor, which is assembled,
and would just need a hand if someone were to want to start it, and the
research lab. The Research lab contains the fruits of the now deceased
science staff's labors, assorted energy weapons. Unfortunately, it also
contains the deceased science staff.

![dreamseeker_HFLqhdKLV5](https://user-images.githubusercontent.com/94164348/204038725-1dd396cd-4961-40e1-bd7a-b60b69a33eaf.png)
Other areas of the base were not so lucky, and are thoroughly infested

![image](https://user-images.githubusercontent.com/94164348/204039090-c85eb551-af84-4000-b1d9-14b15c987680.png)
The engineering team attempted to hold back the vines, and quickly
discovered that fire was not sufficient.

![dreamseeker_IrJikGDXKw](https://user-images.githubusercontent.com/94164348/204039133-273f0a19-c9b7-467e-a06a-05e0a951e4e6.png)
And what used to be the recreation area is completely gone

Notably, the hangar is empty. I plan on making a patch to put a
subshuttle inside it once that rolls around.

Notable loot includes:
3 energy SMGs
3 Flamethrowers
The Ion Projector, a self charging Ion weapon.
An Antique Laser
2 Energy PDWs
2 Accelerator Laser Cannons
4 engineering hardsuits
An engineering lathe and circuit imprinter
A particle accelerator
A singularity generator
6 emitters
1 energy shotgun
Kudzu Seeds
Basically Everything You'd Need For an R&D Set Up
A sense of pride and accomplishment



I feel like this has some rough spots but I've got no idea where to
start, so into the review -> testing -> feedback process it goes

- [x] The ruin spawns when the spawn ruin verb doesn't runtime.
## Why It's Good For The Game
More ruin variety. This one spawns in space and does a few things that I
haven't seen yet. Mainly a singularity, cool semi-hidden asteroid base
that could in theory, be turned into a player lair.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: An abandoned Nanotrasen Asteroid Facility has been spotted in the
area. Salvage teams are advised to steer clear, or at least bring a
knife.
add: kudzu zombie subtype. 
fix: vent iconstates.
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
Co-authored-by: spockye <79304582+spockye@users.noreply.github.com>

---
## [VasilevAY/tgstation](https://github.com/VasilevAY/tgstation)@[09d27e1a51...](https://github.com/VasilevAY/tgstation/commit/09d27e1a5149cffa1d5993687eabc7f8c240af85)
#### Thursday 2023-04-27 01:04:08 by Jacquerel

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
## [YanniZ06/SillyFrogGame](https://github.com/YanniZ06/SillyFrogGame)@[11d4d9d5fd...](https://github.com/YanniZ06/SillyFrogGame/commit/11d4d9d5fdbfd333d2dce3db16bbc492fe25648b)
#### Thursday 2023-04-27 01:08:56 by YanniZ06

BETA IS DONE!! (fucking hell)

yeah uh cool there is actual stuff now yippie!!

i will continue on this for fun

as of now you may:
- pet the frog
- feed the frog (simple button press)
- look at cute frog pictures
- listen to silly music
- enjoy the froggy vibe :))

---
## [michaelbarlow7/crawl](https://github.com/michaelbarlow7/crawl)@[a852ce8369...](https://github.com/michaelbarlow7/crawl/commit/a852ce8369264a3a4759b99df0bbba7645a78c97)
#### Thursday 2023-04-27 01:20:31 by Nicholas Feinberg

Play with ranged weapon stats more

Following some thinking about ranged weapons, here's a new set of
ammoless stats. Philosophy:

- Slings are high-skill 1-handers. Hunting slings are vaguely like
  war axes, and fustibaluses are no longer ultra-rare but are now
  more like broad axes.
- Bows are high-skill 2-handers.
- Crossbows are lower-skill - it takes fairly little to get the hand
  crossbow or the arbalest to mindelay. The triple crossbow is still
  high-skill, but it's quite rare, so doesn't define the 'feel' of
  the class, much as you can't rely on finding a triple sword as a
  lbl user or an exec axe as an axe user. (Unless a gifting god gets
  involved.)

If we're going to keep all these item classes, it would be great to
have some more obvious and pronounced gimmicks. I suspect we'll end
up merging or removing some of these at some point, but that's a
larger project than I'm ready for right now.

TODO: make fustibali spawn at a higher rate - right now they're about
1/5th as common as I'd like.

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[ae5ae813b8...](https://github.com/shiptest-ss13/Shiptest/commit/ae5ae813b8dead3db964893b5169737a4a7f0551)
#### Thursday 2023-04-27 01:20:39 by Bjarl

The Pillbottle, and Pill Things. (#1585)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
![2022 10 20-22 10
16](https://user-images.githubusercontent.com/94164348/197116962-64d22347-2a19-43fc-9614-0c56142c96b9.png)

![dreamseeker_mMxUmMmRjx](https://user-images.githubusercontent.com/94164348/197119938-c60ff760-a7a0-493d-95e3-ac5579a3f3ca.png)

![image](https://user-images.githubusercontent.com/94164348/197118936-6e777e9c-9452-4339-8c38-b7ee5afcd3eb.png)

Adds the Pillbottle-Class Locust Carrier, a ship that hauls around 8
Pills. It is intended as an adminspawn ship mainly for stresstesting
subshuttles (and being asked for). It's fairly resource starved, and has
frankly terrible engines. The expectation is that it will utilize its 8
pods to gather resources and return to the mothership. Or fly off and
die horribly. It has slots for 10 prisoners (that's like 3 pills and one
third of a 4th).
This pr also edits the pill, blackpill, and superpill to be subshuttles
(compatible with the subshuttle system) by cutting out most of their
equipment, converting their maps to shuttle datums, and giving them
docking ports.


<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the
brackets) if you have tested your changes and this is ready for review.
Leave unticked if you have yet to test your changes and this is not
ready for review. -->

- [ ] I affirm that I have tested all of my proposed changes and that
any issues found during tested have been addressed.

## Why It's Good For The Game
Subshuttles are fucking awesome.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Pillbottle-Class Locust Carrier has been added. These cramped
vessels act as a mothership to a swarm of Pill-class Torture
add: The pill and all variants are now subshuttles.
add: Bad Ion Engines, for ships that need to go slow.
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
Co-authored-by: spockye <79304582+spockye@users.noreply.github.com>

---
## [ivanmixo/tgstation](https://github.com/ivanmixo/tgstation)@[a6f49ed542...](https://github.com/ivanmixo/tgstation/commit/a6f49ed54255f9a8d4dfc27bc397e56f87029cb8)
#### Thursday 2023-04-27 01:21:02 by san7890

Refactors Suiciding Variable Into Trait (#74150)

## About The Pull Request

Firstly, this var was on `/mob`, even though only `/mob/living` and
`/mob/dead` could have ever used it, so who knows how much needless
memory it was consuming on stuff such as `oranges_ear` that would never
ever ever use something like this.

Edit: okay instead of memory it just polluted variable edit windows for
all /mob when it didn't need to. I like having a slim VV window

Secondly, it's a technical improvement over the previous system as we
are able to "track" where a suicide originates from, and how we can
track that from mob-to-mob-to-mob. Previously, the boolean `suiciding`
would only inform us if they had ever been connected to a mob that had
ever committed suicide, but now we are able to precisely determine which
mob gave them the trait that they must now apparently bear until the
round restarts.

## Why It's Good For The Game

Less memory usage, more indepth ability to track suicides in case you
really need that dexterity. Currently no implemented code could benefit
from using it, but it would be pretty neat if someone could figure out a
way to have someone be guilt-tripped whenever they look into a mirror
and seeing the reflection of their past life? This PR won't actually
help you code that and it'll probably require a bit more work, but it's
a possibility of some cool interactions you can do when you have this
information available to you.


![image](https://user-images.githubusercontent.com/34697715/226506321-550c37e7-5de8-4f9f-9ceb-4bf9b1052597.png)

## Changelog

:cl:
refactor: Some aspects of how we track suicides from your living mob to
your observer have changed- please do let us know if anything has broken
via a GitHub Issue Report.
/:cl:

There's probably some technical improvements that can be made in some
parts of the code I reworked to accommodate this change, do let me know
if you spot any easy ones (or fuckups). a lot of excess comes from the
fact that any step in the TRAIT framework trusts that you are passing in
a valid datum (or subtype) so that's a thing

---
## [CliffracerX/Skyrat-tg-PRs](https://github.com/CliffracerX/Skyrat-tg-PRs)@[edabb9be67...](https://github.com/CliffracerX/Skyrat-tg-PRs/commit/edabb9be679c65f176532670b339d9adc859e664)
#### Thursday 2023-04-27 01:37:37 by SkyratBot

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
## [mai-nakagawa/evals](https://github.com/mai-nakagawa/evals)@[aeeb452867...](https://github.com/mai-nakagawa/evals/commit/aeeb4528675de633d95a3535100b23c98739f6ce)
#### Thursday 2023-04-27 01:51:21 by Alexander Raul

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
## [mai-nakagawa/evals](https://github.com/mai-nakagawa/evals)@[bf2ebb9dd6...](https://github.com/mai-nakagawa/evals/commit/bf2ebb9dd69e8fbaad3eb42dab1a0523066a52ed)
#### Thursday 2023-04-27 01:51:21 by Amir DIB

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
## [mai-nakagawa/evals](https://github.com/mai-nakagawa/evals)@[38f40050e9...](https://github.com/mai-nakagawa/evals/commit/38f40050e9344d6d4694c75506af03bf7ffe14d3)
#### Thursday 2023-04-27 01:51:21 by dz-pika

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
## [mai-nakagawa/evals](https://github.com/mai-nakagawa/evals)@[b2250e4117...](https://github.com/mai-nakagawa/evals/commit/b2250e4117125fa79e852f454cd4b01b3c066563)
#### Thursday 2023-04-27 01:51:21 by shivamd1810

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
## [mai-nakagawa/evals](https://github.com/mai-nakagawa/evals)@[9fdbd94c93...](https://github.com/mai-nakagawa/evals/commit/9fdbd94c93fc9560781c5e359e3be10d069ac6c5)
#### Thursday 2023-04-27 01:51:21 by Tong

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
## [facebook/hhvm](https://github.com/facebook/hhvm)@[b2e2e868b9...](https://github.com/facebook/hhvm/commit/b2e2e868b9f87b03d7c4729f654adb2efda4eb1e)
#### Thursday 2023-04-27 02:20:23 by Lucian Wischik

log all outcomes of CLIENT_CHECK

Summary:
I asked viratyosin how his experience was with streaming errors -- was it working okay? was it getting stuck? He replied "I might not realize because I tend to hit Ctrl+C when things get stuck; does your telemetry show that?" This diff aims to improve telemetry here.

This diff changes the events associated with "hh". It used to be:
1. CLIENT_CHECK_START (produced only at the start of "hh check")
2. CLIENT_CHECK (upon successful completion of "hh check")
3. CLIENT_BAD_EXIT (used for all commands not just check, e.g. "hh start" and "hh lsp"). You have to filter by "command=Check" to get the bad exits specific to "hh check".

After this diff, "hh check" now produces these:
1. CLIENT_CHECK_START, as before
2. CLIENT_CHECK as before, upon success
3. CLIENT_CHECK_PARTIAL if it succeeded in printing some errors before user interrupted with Ctrl+C or SIGPIPE
4. CLIENT_CHECK_BAD_EXIT if it failed

Why?
* I figure that now with streaming errors, users may deliberately do Ctrl+C as soon as the first error has been shown. And this won't indicate failure; it will indicate success! I wanted this situation to be logged in a separate event CLIENT_CHECK_PARTIAL so it won't inadvertently be lumped with the others. I specifically didn't want it in the normal CLIENT_BAD_EXIT because I want to also get some check-specific telemetry (e.g. time to first error, time of most recent error)
* I figure that folks will also do "hh | head" to pipe it into things which only consume the first error, as their way of ending early. I wanted this to work properly without huge error spew. The common convention of other unix tools appears to just fail with exit code 141 upon such SIGPIPE, and not display anything.
* Scuba makes it awkward to search for nested queries such as `event=CLIENT_CHECK OR (event=CLIENT_BAD_EXIT AND command=Check)`. I'm aiming to turn the availability of "hh check" into an OKR, and I want the scuba queries for it to be easy to write.

While I was at it, I made some other changes:
* the CLIENT_CHECK_PARTIAL and CLIENT_CHECK_BAD_EXIT now also record the current value of the spinner, if any. If figured it'd be interesting to learn whether more people are hitting Ctrl+C in particular states.
* I changed the exit code of Exit_status.Interrupted to be 130, the unix standard code for Ctrl+C. And added a new one Exit_status.Client_broken_pipe (by analogy to the existing Exit_status.Event_logger_broken_pipe) with unix standard exit code 141.
* Removed `produce_streaming_errors` from rollout flags (since it's been at 100% for some weeks), and added `consume_streaming_errors` instead (so we can correlate whether Ctrl+C has gotten better or worse with this flag).

Reviewed By: CatherineGasnier

Differential Revision: D45196752

fbshipit-source-id: bc4ae99ae5d7d5b72e8fd32651efbcba07c98cc0

---
## [manoj-maharana/evals](https://github.com/manoj-maharana/evals)@[ab5f7b2a89...](https://github.com/manoj-maharana/evals/commit/ab5f7b2a89bcf60e8e93adfb2c70688c6d6ffd44)
#### Thursday 2023-04-27 02:28:20 by oscar-king

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
## [manoj-maharana/evals](https://github.com/manoj-maharana/evals)@[b170a21cf3...](https://github.com/manoj-maharana/evals/commit/b170a21cf32c47d841f64ec110cfd6796ec3f89a)
#### Thursday 2023-04-27 02:28:20 by Sam Ennis

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
## [manoj-maharana/evals](https://github.com/manoj-maharana/evals)@[b5da073c21...](https://github.com/manoj-maharana/evals/commit/b5da073c215c6453b99269a6dab2dca5454f04dd)
#### Thursday 2023-04-27 02:28:20 by somerandomguyontheweb

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
## [Josh-Vanenbrink/hello-world](https://github.com/Josh-Vanenbrink/hello-world)@[9bf6dc2711...](https://github.com/Josh-Vanenbrink/hello-world/commit/9bf6dc2711fc3c560f99b6bd9b714fb7ad261f04)
#### Thursday 2023-04-27 02:43:53 by Josh-Vanenbrink

Update README.md

Tried to make my students laugh with a terrible dad joke that wasn't funny.

---
## [retlaw34/Shiptest](https://github.com/retlaw34/Shiptest)@[1c039c0623...](https://github.com/retlaw34/Shiptest/commit/1c039c0623b6e8af463de0f0b1ca1ccc49050d94)
#### Thursday 2023-04-27 03:53:07 by Sun-Soaked

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
## [hmojicag/SurfingAttendanceApp](https://github.com/hmojicag/SurfingAttendanceApp)@[ffb5e016b9...](https://github.com/hmojicag/SurfingAttendanceApp/commit/ffb5e016b9f2e76b2d3d7d15647e69f225b43c87)
#### Thursday 2023-04-27 04:49:45 by Mojica García Hazael Fernando

* Displaying Sync with SurfingTime checkbox in List view
* Fixing stupid annoying made me waste 4 hrs debugging fucking BUG in AttendanceRecordsRepository
* Syncing AttendanceRecords to SurfingTime now working

---
## [Luigi30/mame](https://github.com/Luigi30/mame)@[c4a19a68a6...](https://github.com/Luigi30/mame/commit/c4a19a68a67cd32ffaaa37edfd6f1c2ba347905f)
#### Thursday 2023-04-27 05:01:49 by Ivan Vangelista

New systems marked not working
------------------------------
Desert Gold (20202311, ASP) [anonymous, Heihachi_73]
Diamond Eyes (10129211, ASP) [anonymous, Heihachi_73]
Dolphin Treasure (10177911, ASP) [anonymous, Heihachi_73]
Silk Road (10176811, ASP) [anonymous, Heihachi_73]
Snap Shot (20115211, ASP) [anonymous, Heihachi_73]
The Golden Gong (20196011, ASP) [anonymous, Heihachi_73]
Wild Cougar - Power Pay (30214211, ASP) [anonymous, Heihachi_73]
Wings over Olympus (10176511, ASP) [anonymous, Heihachi_73]

New clones marked not working
-----------------------------
5 Dragons (10176611, ASP) [anonymous, Heihachi_73]
5 Dragons (10178611, New Zealand) [anonymous, Heihachi_73]
5 Koi - Power Pay (1J016211, ASP) [anonymous, Heihachi_73]
50 Lions (0152077, US) [anonymous, Heihachi_73]
100 Lions (30223811, ASP) [anonymous, Heihachi_73]
Arabian Nights (10122611, ASP) [anonymous, Heihachi_73]
Big Ben (10169611, ASP) [anonymous, Heihachi_73]
Buccaneer (10181911, ASP) [anonymous, Heihachi_73]
Buffalo (20232611, ASP) [anonymous, Heihachi_73]
Brazil (10218511, ASP) [anonymous, Heihachi_73]
Dolphin Treasure (20265311, New Zealand) [anonymous, Heihachi_73]
Dream Catcher (10172921, ASP) [anonymous, Heihachi_73]
Fire Dancer (10191311, ASP) [anonymous, Heihachi_73]
Fortune King (10230911, ASP) [anonymous, Heihachi_73]
Geisha (10122011, ASP) [anonymous, Heihachi_73]
Geisha (10112411, ASP) [anonymous, Heihachi_73]
Go For Green (10122111, ASP) [anonymous, Heihachi_73]
Golden Pyramids (10196511, ASP) [anonymous, Heihachi_73]
Heart of Gold (10184211, ASP) [anonymous, Heihachi_73]
Helen of Troy (10129121, ASP) [anonymous, Heihachi_73]
Helen of Troy (10116411, ASP) [anonymous, Heihachi_73]
Hollywood Dreams (10122811, ASP) [anonymous, Heihachi_73]
Helen of Troy (10122711, ASP) [anonymous, Heihachi_73]
House of Hearts (10208411, ASP) [anonymous, Heihachi_73]
Indian Dreaming (10192211, ASP) [anonymous, Heihachi_73]
King of the Nile (10127511, ASP) [anonymous, Heihachi_73]
Let's Go Fish'n (10223911, ASP) [anonymous, Heihachi_73]
Money Tree (10122211, ASP) [anonymous, Heihachi_73]
Paris Lights (10139011, ASP) [anonymous, Heihachi_73]
Peacock Magic (10134311, ASP) [anonymous, Heihachi_73]
Pelican Pete (10196211, ASP) [anonymous, Heihachi_73]
Pirates (10122311, ASP) [anonymous, Heihachi_73]
Pompeii (10122411, ASP) [anonymous, Heihachi_73]
Queen of Sheba (30146921, ASP) [anonymous, Heihachi_73]
Queen of the Nile (10204311, ASP) [anonymous, Heihachi_73]
Queen of the Nile (10192311, ASP) [anonymous, Heihachi_73]
Queen of the Nile Special Edition (10127411, ASP) [anonymous, Heihachi_73]
Ruby Magic (10148811, ASP) [anonymous, Heihachi_73]
Scatter Magic II (10122511, ASP) [anonymous, Heihachi_73]
Spring Festival (20267211, New Zealand) [anonymous, Heihachi_73]
Tigress (20243811, ASP) [anonymous, Heihachi_73]
Tiki Torch (10124011, New Zealand) [anonymous, Heihachi_73]
Torch of the Gods (20210211, ASP) [anonymous, Heihachi_73]
Turtle Treasure (10239811, ASP) [anonymous, Heihachi_73]
Where's The Gold (10177111, ASP) [anonymous, Heihachi_73]
Wild Cats (20258111, ASP) [anonymous, Heihachi_73]
Wild Goose (10155911, ASP) [anonymous, Heihachi_73]
Wild Panda (20225011, ASP) [anonymous, Heihachi_73]
Zorro (20167511, ASP) [anonymous, Heihachi_73]

-aristocrat/aristmk6.cpp updates:
* dumped 3 more System EPROM Sets [anonymous, Heihachi_73]
* renamed "Malaysian" games to ASP as the games don't have any specific region, only the BIOS does [Heihachi_73]

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[e6e318db01...](https://github.com/treckstar/yolo-octo-hipster/commit/e6e318db01f009db40f4ae852b2fa05f5f738874)
#### Thursday 2023-04-27 05:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[cb1388ed9e...](https://github.com/odoo-dev/odoo/commit/cb1388ed9e64ced4e0d85cf5778192dfbdfd5995)
#### Thursday 2023-04-27 05:31:22 by Jeremy Kersten

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

closes odoo/odoo#119246

X-original-commit: 4aca39a533e9d41f5f452f36a1ffc001f586b4f4
Signed-off-by: Jérémy Kersten <jke@odoo.com>

---
## [Addust/tgstation](https://github.com/Addust/tgstation)@[0b90dc54a6...](https://github.com/Addust/tgstation/commit/0b90dc54a61f99667a4e4d75ec32a4ec438d78d7)
#### Thursday 2023-04-27 06:11:07 by Addust

god fucking damnit i was DECIEVED by my OWN FOOLISHNESS

---
## [Silentis/multiplication-is-hell](https://github.com/Silentis/multiplication-is-hell)@[e45049eb5f...](https://github.com/Silentis/multiplication-is-hell/commit/e45049eb5f9b6e686108e6b0d2d1ee87df9c9a0c)
#### Thursday 2023-04-27 06:29:54 by Silentis

first version for the HELL OF AN APP. 

I HATE LIFE AND I HATE LIFE. I WANNA KILL MYSELF AT THIS MOMENT.

---
## [alanrtao/Slider](https://github.com/alanrtao/Slider)@[cc06840f9a...](https://github.com/alanrtao/Slider/commit/cc06840f9a88f1453b251a7ff28206d263a55df0)
#### Thursday 2023-04-27 07:08:37 by alanrtao

tried to fix intonation issue and kinda just gave up. you know, sometimes life is like this. the real intonations are the friends we met along the way. your into-network is your into-networth, etc.

---
## [sarvex/terminal](https://github.com/sarvex/terminal)@[21464fe41c...](https://github.com/sarvex/terminal/commit/21464fe41c9c09eac4b9e2d85225f18f1f3c2c7b)
#### Thursday 2023-04-27 07:15:36 by Mike Griese

Manually hide our DesktopWindowXamlSource (#15165)

As discussed in #6507

Newer builds of Windows do this automatically. However, this was spotted
in the wild on 1.18. It's possible the threading changes created a
situation where the OS-side fix no longer applied to us. So let's just
do it manually. It doesn't have any side effects.

I saw this once on Win11, but couldn't repro it this morning when I
tried to add this fix. I'm just gonna assume this worked, despite the
fact that I can't repro it on win11 anymore.

closes #6507

See also #14957

## detailed description

> `WindowsXamlManager::XamlCore::Initialize` calls
`ConfigureCoreWindow`, which creates a `CoreWindow` on the thread

> Problem is, we're calling that on the main thread (which doesn't have
_any_ windows), and then eventually creating a `DesktopWindowXamlSource`
on a second thread for the actual window

> It's not that it "manages a window", it's that it "manages xaml on
Windows OS". just use ICoreWindowInterop -- QI for ICoreWindowInterop
and call get_WindowHandle.

Also see:
*
[ICoreWindowInterop](https://learn.microsoft.com/en-us/windows/win32/api/corewindow/nn-corewindow-icorewindowinterop)
*
[WindowsXamlManager.InitializeForCurrentThread](https://learn.microsoft.com/en-us/uwp/api/windows.ui.xaml.hosting.windowsxamlmanager.initializeforcurrentthread?view=winrt-22621#windows-ui-xaml-hosting-windowsxamlmanager-initializeforcurrentthread)
* The source code in
`onecoreuap\windows\dxaml\xcp\dxaml\lib\WindowsXamlManager_Partial.*`
* os.2020!6102020 which fixed MSFT:33498969, MSFT:27807465,
MSFT:21854264

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[ecc37ba72a...](https://github.com/cmss13-devs/cmss13/commit/ecc37ba72a663ddc748b0ade41fbd99ec5a5853a)
#### Thursday 2023-04-27 07:57:15 by Hopekz

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
## [NetBSD/pkgsrc](https://github.com/NetBSD/pkgsrc)@[ab06d0dbc8...](https://github.com/NetBSD/pkgsrc/commit/ab06d0dbc802e55401b44739ca478e24371e4606)
#### Thursday 2023-04-27 09:05:50 by pin

shells/nushell: update to 0.79.0

Themes of this release / New features

- Standard library (@amtoine, @bobhy, @fdncred, @presidento, ...)
  This is it. We finally release the standard library with this 0.79!
  It's been on the mind of the core team of Nushell for some time and it was
  made real between the two releases.

  But first of all... what is the standard library?

  The nushell standard library is a collection of nushell scripts that are
  automatically loaded in the nushell binary and reachable via the use command
  without any additional setup.

  Note: some of the commands from the standard library are used without human
  intervention as part of what we call the prelude.
  As said above, the other commands are available with the use command.
  The goal of this library is, as its name suggests, to provide a standard
  experience and a standardized set of commands and tools to any Nushell user.
  In std, one can find things like:
    - a test framework to write robust Nushell scripts, modules and libraries
    - implementation of builtin commands once written in rust
    - logging commands with several log levels
    - ...

  Note: yes, you heard right, in the future, the standard library might become
  a sanctuary for non-time-critical commands that were once written in rust as
  part of the built-in set of commands!
  Right now, we are actively trying to move the help commands from the nushell
  core implementation to the library.

  With this release, the library comes with the following custom commands:
  std assert, std dirs, std help, std iter, std log and xml module
  See https://www.nushell.sh/blog/2023-04-25-nushell_0_79.html for a
  description of these and a list of available sub-commands.

  some other commands live under the std namespace, without any module: clip,
  path add and run-tests.

- TL;DR
  As there has been quite a lot of contributions already (see the 50 closed
  PRs at the time i'm writing this), i'm just gonna give some hints and links
  in this release note, leaving the rest to the amazing work of other
  contributors who wrote parts of the lib and its documents
  (shout out to @bobhy, @fdncred and @presidento)

  - the library can be used and tested with or use direct imports, such as
    use std dirs
  - one can follow the activity of the library in the roadmap
  - the library comes with a test framework; see the Testing your Nushell code
    chapter of the book
  - the long term information, changelog and updates shall be found in the
    Standard library chapter of the Nushell book
  - if you are a contributor willing to help out, everything happens in the
    nu-std crate, especially the CONTRIBUTING.md document which explains all
    there is to know about "developing with std" in great details.

  If, for some reason, you want to load Nushell without the standard library,
  start nu with the --no-std-lib. This can be the case if you find the startup
  times much longer than before. We're aiming to improve the loading speed
  in the future.

- enhanced IDE support in our VS code extension (JT, fdncred)
  Nushell now has a first LSP (Language Server Protocol) implementation with a
  VSCode integration. If you install the latest version of our VSCode plugin,
  you'll see hovers, inlays, tooltips, error squigglies and other features.
  We are still very early in the LSP development, but the extension is already
  very usable and definitely moves the experience of writing Nu code to another
  level!

  While currently we have only VSCode integration, the server itself is
  standalone and we welcome projects adding the LSP support to more editors.

- atuin now supports Nushell
  Thanks to @stevenxxiu you can now use atuin with Nushell. We are happy to see
  Nushell supported by more projects and we welcome PRs adding more
  integrations.

- Relaxed parsing rules (JT)
  We listened to your feedback around the syntax changes introduced with 0.78
  and decided to revert to the old behavior around the parsing rules for
  numeric literals as well as the compulsory || for closures.

- Removed old alias implementation (kubouch)
  While there are still some missing pieces, we removed the old alias
  implementation. This means that old-alias is no longer available. We decided
  to remove it to clean up the code. It makes further fixes to aliases easier
  as you do not need to remember which alias implementation a piece of code
  belongs to.

  There are two notable missing features from the old aliases:
  - Missing completions with external completers.
  - Most parser keywords (such as source) cannot be aliased but adding support
    for aliasing them should be possible in most cases.
  - Not possible to alias with environment shorthands
    (e.g., alias foo = FOO=bar spam)
  - Some presentation issues, such as the output of which and the alias usage
    pointing at the aliased call instead of the alias itself.

- Changes to default files locations (ito-hiroki)
  $nu.config-path and $nu.env-path are now set based on --config
  and --env-config flags passed to Nushell and also use the path after
  resolving symlinks. This means that they no longer guarantee pointing at the
  default Nushell's config directory. To be able to refere to the default
  config directory, $nu.default-config-dir was added and used in default env.nu
  to always point NU_LIB_DIRS to the scripts directory under the default config
  directory.

  Related to that, $env.CURRENT_FILE was added to be able to show the currently
  evaluated file.

- Breaking changes
  #8797 old-alias is no longer available
  #8724 str index-of -r now uses ranges
  #8792 config nu and config env now open $nu.config-path and $nu.env-path,
        respectively.
  #8779 Aliasing math expressions now shows error immediately instead of
        failing silently and showing a confusing error later.
  #8917 exec inherits Nushell's environment variables
  #8887 NU_LIB_DIRS definition in env.nu changed

---
## [willardstation/tg-voidcrew](https://github.com/willardstation/tg-voidcrew)@[2b2cb3dff6...](https://github.com/willardstation/tg-voidcrew/commit/2b2cb3dff6d9985103cee46a6020aa1b63a3c2de)
#### Thursday 2023-04-27 09:44:22 by LemonInTheDark

Hologram Touchup (Init savings edition) (#74793)

## About The Pull Request

### Polishes and Reworks Holograms

Hologram generation currently involves a bunch of icon operations, which
are slow.
Not to mention a series of get flats for the human models, which is even
worse.

We lose 0.05 seconds of init to em off just the 2 RCD holograms. it
hurts man.

So instead, let's use filters and render steps to achive the same
effect.

While I'm here I'll dim the holo light and make it blue, make the
hologram and its beam emissive (so they glow), and do some fenangling
with move_hologram() (it doesn't clear the hologram off failure anymore,
instead relying on callers to do that) to ensure holocalls can't be
accidentially ended by moving out of the area.

Ah and I added RESET_ALPHA to the emissive appearance flags, cause the
alpha does override and fuck with color rendering, which ends up looking
dumb. If we're gonna support this stuff it should be first class not
accidential.

### Makes Static Not Shit

While I'm here (since holograms see static) lets ensure the static plane
is always visible if you're seeing through an ai eye.

The old solution was limited to applying it to JUST ais, which isn't
satisfactory for this sort of thing and missed a LOT of cases (I didn't
really get how ai eyes worked before I'ma be honest)

I'm adding a signal off the hud for it detecting a change in its eye
here.
This is semi redundant, but avoids unneeded dupe work, so I'm ok with
it.

The pipeline here is less sane then I'd like, but it works and that's
enough

## Why It's Good For The Game


![dreamseeker_zMiLXzlZ2X](https://user-images.githubusercontent.com/58055496/232470136-add945da-5f76-469e-ba1a-6ed3159b6f5b.png)
More pretty, better ux, **static works**

## Changelog
:cl:
add: Holograms glow now, pokes at the lighting for holocalls in general
a bit to make em nicer.
qol: You can no longer accidentally end a holocall (as a non ai) by
leaving the area. Felt like garbage
fix: Fixes static rendering improperly if viewed by a non ai
/:cl:

---
## [warptools/warpforge](https://github.com/warptools/warpforge)@[7ba05edb02...](https://github.com/warptools/warpforge/commit/7ba05edb02f85f168b06fdbb5d07fca7144f9eb8)
#### Thursday 2023-04-27 09:49:36 by Eric Myhre

Massively refactored CLI wiring.

The main justifications of this are to make it easier to test,
and to prepare for more features I want to work on that require
more access to the CLI objects.

The justifications for this package structure can be found in
the introduced HACKME file.

The use of package-scope vars for the CLI object is considerably unfortunate,
but (again, as detailed in the HACKME), our CLI library already breaks the dam.
(This will become even more largely applicable when I get to work on
the planned features around help content generation, which will require
yet more global var touches to things inside the CLI library.)
So: in for a penny, in for a pound, and I hope I don't regret this too much.

Subcommands now register themselves in package init mechanisms.
As above: in for a penny, in for a pound, and I hope I don't regret this too much.

There's no more use of "internal" packages.
Those tend to footgun me painfully more often than not,
and so let's not have that.

Removed a fairly bonkers use of an "after" func in the CLI.
Its only user was part of the check subcommand.
Fewer lines of code and fewer weird long jumps across callbacks
occur by simply putting the code where it's used.

Many other miscellaneous fixes.
For example, fixing many references to `os.Args[0]` to use the app name.
Too many other small ones to recount.

A few things itch to me, but haven't yet received any changes:
there's still a "util" package in 'app/base/util',
and I'd like to tidy it away.
Also, the "middleware" functions in it for tracing are highly
redundant and I wonder if we can't make that a bit less frequently
copy-pasted.
This diff is already big enough, though.

The 'pkg/config' package also continues to exist, and I think it
should probably be unified into 'app/base' shortly.
The CLI library has features for env vars, as well as documenting them,
and we might as well use that.
(This config package is also pretty brazenly using package-scope vars
already too, so combining it with this other package that also does so
should produce no additional hurt.)

There are some uses of "../" in test setup that are also likely to
become broken soon -- as soon as we use 'app/testutil' from varying
depths of packages.  In this commit, that hasn't happened yet,
but expect some minor Fun dealing with that soon.

---
## [Pinsplash/halflife2chaos](https://github.com/Pinsplash/halflife2chaos)@[094eb33f54...](https://github.com/Pinsplash/halflife2chaos/commit/094eb33f54b24c9fd264acc1cbdb3f4101afe022)
#### Thursday 2023-04-27 10:15:28 by Pinsplash

Fixed issues seen watching MarioInATopHat's stream

fixed everyone being forced to use my weird keybinds
removed seemingly harmless assert caused by Pause Physics
restricted clone_npcs from happening on d1_trainstation_01 because barney can end up perfectly blocking the doorway
fixed Player is Big getting you stuck when jumping and not holding duck
groups added so that Annoying Alyx and Left 4 Dead cannot happen at the same time as the No Looking Up/Down/Left/Right effects
fixed being teleported to odd places when the game was struggling to find a good place to put you at to get you unstuck
fixed trigger_changelevel not working if you touched it while not being inside the trigger_transition
added d1_canals_06 to map list for the Player Teleport context
fixed game crash when killing an ichthyosaur by ramming with a vehicle
fixed Lock Vehicles re-locking vehicles when meant to be unlocking them
Ran Out Of Glue can no longer happen on more maps
fixed game thinking you were drowning in a vehicle when loading a save made when Swim In Air was active
airboat gun no longer recharges when No One Can Reload is on
fixed un-stuck code thinking an elevator might not be valid standable ground
fixed un-stuck code thinking it wasn't possible to get an object unstuck if its origin was inside world geometry (the code wants to avoid teleporting objects through world geometry)
game no longer attempts to get you unstuck when using noclip
Suppression Field Hiccup can no longer happen on d1_eli_02

---
## [NetBSD/pkgsrc](https://github.com/NetBSD/pkgsrc)@[73b036d91a...](https://github.com/NetBSD/pkgsrc/commit/73b036d91af335cfda7bd9aa4b88039312536a38)
#### Thursday 2023-04-27 10:33:08 by wiz

mame: update to 0.254.

MAME 0.254, the most hotly anticipated emulator release in recent
memory, is ready today! Yes, it finally happened: the first batch
of Namco System 10 games have been emulated! It’s been a real team
effort, with contributors around the world working on emulation,
cracking encryption, and properly dumping the Flash memory chips.
You’ll be able to enjoy Namco’s Mr. Driller 2 and Mr. Driller G,
as well as the spin-off Star Trigon. System 10 was home to Mitchell’s
final two arcade games, Gamshara and Kono e Tako. From Metro, there
are two GAHAHA Ippatsudou mini-game collections and the two-in-one
mahjong tile puzzle game GekiToride-Jong Space. Other working Namco
games include Kotoba no Puzzle Mojipittan, Panikuru Panekuru, and
Uchuu Daisakusen: Chocovader Contactee.

Quite a few of the System 10 games that are still marked as not
working are already playable. Taiko no Tatsujin 2, 4 and 6 are
playable, although we aren’t confident enough in the timing accuracy
of MAME’s PlayStation emulation to mark rhythm games as working at
the moment. You can play the light gun shooter Golgo 13: Juusei no
Requiem, but it’s missing sounds and voice acting at the moment.
Several coin pushers on the closely related WIDEISM SP-02 platform
run; you can trigger various animations, but there’s no gameplay
as such.

Of course, Namco System 10 emulation isn’t the only thing that’s
updated in this release. Almost a dozen Yamaha keyboards based on
the GEW7 CPU are now working. Interestingly, their sound synthesis
capabilities are closely related to the MultiPCM chip used in
various Sega arcade games. Another game from SNK’s early Micon Kit
series has been dumped and emulated. There are also two more working
Brother word processors and two working Liberty Electronics serial
terminals.

Cave CV1000 games now have more realistic blitter performance,
meaning you don’t need to tweak settings to get close to the arcade
experience. Properly emulating the absence of a memory management
unit in the R4650 CPU used by Namco’s System 23 solves crashes in
Time Crisis 2. Some fixes in SGI workstation emulation have IRIX
running again. A few bugs affecting PC Engine and Virtual Boy games
have been fixed. Issues with certain sound effects in classic Konami
arcade games have been fixed, too.

---
## [coolstation/coolstation](https://github.com/coolstation/coolstation)@[553a9f502d...](https://github.com/coolstation/coolstation/commit/553a9f502d2b4a11eaa005889f1d893d946de284)
#### Thursday 2023-04-27 12:26:11 by BatElite

More minegen messing (#178)

* replace bullshit in mine map gen with turf flags

* kill quality, add starstone generation to zlevels

* Crop borders when iterating, define BS for CSGetSolid

* Inline CAGetSolid into desert gen, fucking hell

* explain some shit

* Erebite, miraclium now generate in z levels

---
## [Offroaders123/Mojang-API](https://github.com/Offroaders123/Mojang-API)@[a9ebfbfc89...](https://github.com/Offroaders123/Mojang-API/commit/a9ebfbfc894913543f42ec5ae302827c2b5d30df)
#### Thursday 2023-04-27 12:40:51 by Offroaders123

Demo Script

This project is still in the very early idea stages, so the code quality is sub-par as of now. Learning how to do some things a few different ways. Not sure what this can be used for yet, either. Always wanted to make my own skin downloading site, so maybe this could be for that?

Some of these changes were going to be made the other day also, but I ended up accidentally `git checkout .`-ing my small few edits, waht a dehrp.

Oh yeah, it was also because I couldn't come up with a name for the project. I wanted to find something clever, since `mojang-api`, `mojang`, and `mine-api` are all already taken. I was going to do `poisonous-potato`, but that was too random to remember. It doesn't really connect with the library at all either. I think changing back and forth on names is what broke the changes I made actually, now that I remember. I was also gonna go with `golden-apple`, but wasn't in love with the name. Saying it (lol) out loud again (by that, I mean typing it) though, it actually might be neat afterall. We'll see (I don't like that phrase, but I guess I'm using it here, aaagh)!

---
## [kjambunathan/org-mode-ox-odt](https://github.com/kjambunathan/org-mode-ox-odt)@[4d7d8ccda6...](https://github.com/kjambunathan/org-mode-ox-odt/commit/4d7d8ccda65c7a1860a53151838c39252d35aa2a)
#### Thursday 2023-04-27 13:46:19 by Jambunathan K

* lisp/ox-odt.el (org-odt-verse-block): Add bottom margin to `OrgVerse'

* etc/styles/OrgOdtStyles.xml (OrgVerse): Use bottom margin to
space a verse block to the next element.

* lisp/ox-odt.el (org-odt-verse-block): Don't use a line break to
space the verse block to the next element.

Fixes #242.

Here is an `org' snippet to test drive this change

    #+begin_verse
	The woods are lovely, dark and deep,
	    But I have promises to keep,
	And miles to go before I sleep,
	    And miles to go before I sleep.
    #+end_verse

    Robert Frost, “Stopping by Woods on a Snowy Evening” from /The Poetry
    of Robert Frost,/ edited by Edward Connery Lathem. Copyright 1923, ©
    1969 by Henry Holt and Company, Inc., renewed 1951, by Robert
    Frost. Reprinted with the permission of Henry Holt and Company, LLC.

    Source: //Collected Poems, Prose, & Plays// (Library of America, 1995)

    * COMMENT Add background colour to the verse block

    #+ATTR_ODT: :target "extra_styles"
    #+begin_src nxml
    <style:style style:name="OrgVerse"
		 style:parent-style-name="Preformatted_20_Text"
		 style:family="paragraph">
      <style:paragraph-properties fo:background-color="#f6f9d4"
				  fo:border="0.06pt solid #000000"
				  fo:margin-bottom="0.21cm"
				  fo:margin-top="0cm"
				  fo:padding="0.049cm"
				  style:shadow="none" />
    </style:style>
    #+end_src

---
## [PremChand12/abc1](https://github.com/PremChand12/abc1)@[0d7121df0b...](https://github.com/PremChand12/abc1/commit/0d7121df0bc8f5d79af6f055faf92e9c025a5c73)
#### Thursday 2023-04-27 14:31:02 by Prem Chand

Added about man life

humans can born and die 
humans has the option to get god on his own.

---
## [Wizrd101/The-Peanut-Game](https://github.com/Wizrd101/The-Peanut-Game)@[29ebb89d7f...](https://github.com/Wizrd101/The-Peanut-Game/commit/29ebb89d7f4f0f3a87570836d07143dfe2ae1384)
#### Thursday 2023-04-27 15:30:32 by Simon Henderson

I think I figured out the NavMesh problem

Are you guys ready for the solution to why the NavMesh wasn't working, keeping me up all night and putting me on 4 hours of sleep today? It was... I was an idiot. It was working, it's just really slow building it and the enemy moves really slowly.

But seriously, I am on 4 hours of sleep today. I need a break.

---
## [deltachat/deltachat-core-rust](https://github.com/deltachat/deltachat-core-rust)@[57091bca24...](https://github.com/deltachat/deltachat-core-rust/commit/57091bca249135b684dfe2b9f1ffb29ad44e6689)
#### Thursday 2023-04-27 15:44:47 by iequidoo

Remove "vc-contact-confirm-received", "vg-member-added-received" messages from Securejoin protocol (#3836)

They are an overkill and do not solve any problem.

IDK all details why they were added, so just citing from #3836:

    @iequidoo: Btw, can somebody explain the purpose of
    vg-member-added-received/vc-contact-confirm-received messages in the protocol? They look
    excessive and for me it's like a try to solve that problem with two friends that want to meet
    and drink some beer but only if each of them is sure that their beermate is also going to the
    meeting :) Even if Bob didn't receive vg-member-added message (e.g. because of mail delivery
    problems), we can consider Bob joined -- Bob can try sending messages to the group and that must
    work afaiu.

    @flub: Yes, this is a weird state. It is currently the difference between an internal state
    "un-idirectional verified" and the exposed state "bi-directional verified". The latter (bi-)
    means both know that both have each other verified, in the former (uni-) only one of them knows
    this and the other hasn't figured this out yet.

    IIRC the last time this was discussed the revelation (at least to me) was that the main
    practical difference between these two is that bi-directional allows you to add the other person
    to a verified group, while if you only have them uni-directional verified you can not do they
    since they don't trust you enough (IIRC, there should be a cryptpad somewhere with this written
    down).

    @link2xt: When Bob receives vc-auth-required, he already has Alice one-way verified. When Alice
    receives vc-request-with-auth, she has Bob two-way verified (she has verified Bob's key and she
    know Bob has verified her), but Bob still does not know about this. When Bob receives
    vc-contact-confirm (or vg-member-added) he sets Alice state to "two-way verified".

    The question is what happens if vc-contact-confirm/vg-member-added is lost. In this case Alice
    has Bob two-way verified, while Bob has Alice only one-way verified. Because of this, Bob cannot
    safely add Alice to any verified group, because Bob thinks maybe Alice has not received
    vc-request-with-auth and has Bob completely unverified. However, Alice still can add Bob to
    verified groups and if Bob later receives any message from Alice in a verified group, he sets
    Alice to two-way verified, so eventually both Alice and Bob converge to a two-way verified
    state. This is not how it is currently implemented, but this was the idea during the discussion
    with @flub and @missytake.

    But vg-member-added-received/vc-contact-confirm-received is an overkill and can be removed IMO,
    it does not solve any problem.

Also remove Secure-Join-Fingerprint header from vg-member-added messages, it's a compatibility
crutch for old clients. Currently DC sends Autocrypt key gossips instead, they're better because
knowing a key allows not to only trust the peer, but also encrypt to it. Before it was a problem for
other devices on a joining side going online after a successful Securejoin setup -- they didn't have
a joiner's key to encrypt to it. So, we decided not to complicate the Securejoin with sending keys
instead, but rely on the Autocrypt.

And more reasoning to remove all this stuff is that it's not documented anywhere, instead there's a
PR to the Countermitm doc documenting when gossips in 'vc-request-with-auth' are needed:

    Bob's own key fingerprint ``Bob_FP``,
    the second challenge ``AUTH`` from step 1 and
    optionally an Autocrypt-Gossip header for Alice's
    Autocrypt key in order for a second device of Bob
    to learn Alice's verified key.

Also all necessary tests were added before and they work w/o the removed code.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[53f1486556...](https://github.com/mrakgr/The-Spiral-Language/commit/53f1486556578e25943bf3b1fc76df7e7d4936c6)
#### Thursday 2023-04-27 15:58:27 by Marko Grdinić

"6:45pm. https://boards.4channel.org/g/thread/93041086/sdg-stable-diffusion-general

Compared to last year, the level of AI art is insane here.

God, I am tired. My brain feels like it will explode.

7:30pm. https://emaggiori.com/employed-in-tech-for-years-but-almost-never-worked/

7:35pm. i am fucking going to bed. I'll die at this rate from mental exhaustion.

4/27/2023

7:55am. Despite being in bed for over 12h, I did get much sleep. I am still tired, but I should be more rested than before.

Last night, I was so wound up, I felt like a zombie.

8am. I still am somewhat.

Let's give this 'toubing another month and then I will see how fit I am for contracting.

https://mangadex.org/title/135b2ea2-94a7-4499-aa2e-85f3efae4a4c/daily-life-in-ts-school
https://mangadex.org/title/5e9a2a3e-f992-4af4-a887-cd130460c9e5/baki-dou

For now let me just read the latest of these. Then I will do some recording. I want to get the IndexDb down.

https://youtu.be/NNuTV-gjlZQ
Storage for the web

https://web.dev/storage-for-the-web/

https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Client-side_storage
https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API

8:55am. My dad just called to tell me there will be a power outage from 9am to 1pm. I am turning off here.

9:20am. So much for that power outage. Maybe it will happen later.

Let me do my screencasting, and if I lose some work due to a sudden turn off, then so be it.

9:40am. Still hasn't happened.

9:55am. The power's still on.

10:30am. It is still on.

10:45am. Oh, changing the duration in the cut and the edit pages has different behavior. In the cut page it ripples the timeline, which is a lot more useful than the overwritting on the edit page.

11:30am. Had to take a break, let me resume.

12:05pm. I have 9:15m worth of video. I could end it here.

But let me study IndexDb a bit more before I make the decision.

https://youtu.be/vb7fkBeblcw
IndexedDB Crash Course with Javascript

https://youtu.be/vb7fkBeblcw?t=92
> It is essentially an object key value store.

So that is all there is to IndexedDb?

https://youtu.be/vb7fkBeblcw?t=300

Why the fuck am I wasting my time watching this? Forget it.

Let me just watch a bit on NoSql.

https://youtu.be/0buKQHokLK8
How do NoSQL databases work? Simply Explained!

https://youtu.be/0buKQHokLK8?t=75

I had no idea that SQL has a hard time scaling.

https://youtu.be/0buKQHokLK8?t=105
> They are key value stores

https://youtu.be/0buKQHokLK8?t=310

Hmm, really?

https://youtu.be/0buKQHokLK8?t=400

Hmmm...

https://youtu.be/0buKQHokLK8?t=420

I should look into CouchDb as there is an IndexedDb library based off it.

12:35pm. No there is no need to go deeper.

1:20pm. In the end, the power never went out even once.

1:40pm. We'll let it render for a while.

Let me have breakfast.

2:20pm. https://www.nango.dev/blog/why-is-oauth-still-hard

I need to keep Nango in mind in the future. No way do I want to go through the experience of last 3 weeks again.

https://news.ycombinator.com/item?id=35713518
> That drove me up the wall in Python so much - ALL the documentation just described how to put a massive library into a cookie cutter example and never explained how it's supposed to work so I could debug the darn thing.

> Asp.Net authentication is 10 times worse in this regard.

///

It'd be interesting to hear about people who have had a good time implementing OAuth, as my experience is similar to that in the article. I've played with adding it to a few side projects and the process usually goes:

1. Read loads of docs, end up pretty confused
2. Find a library that seems to do what I want
3. Install this huge library full of opaque code doing...things
4. Have an impossible time troubleshooting issues
5. Get scared ("I'm almost certainly doing something wrong here") and give up

I find it hard to have much faith in security standards like this. I want them small, well defined and understandable and OAuth does not meet any of these criteria in my experience.

///

3:25pm. Done with breakfast and chores.

Let me resume. For some reason the upload failed last time so let me do it now.

3:30pm. How did I export the markers into CSV last time?

Ah, right click on the timeline.

https://stackoverflow.com/questions/2459472/executing-f-scripts

Now I ma wondering why it didn't run the script file.

3:45pm.

```fs
#r "nuget: FSharp.Data"

open System.IO
open FSharp.Data

let f =
    CsvFile
        .Load(Path.Combine(Directory.GetCurrentDirectory(), "f.csv"))

System.Console.SetOut(File.CreateText(Path.Combine(Directory.GetCurrentDirectory(),"toc.txt")))

for row: CsvRow in f.Rows do
    printfn "%s %s" (row.GetColumn "Source In") (row.GetColumn "Notes")
```

How much time is this going to take me? At first I exported the wrong thing, but now it is messing with this.

Why am I doing this anyway?

https://youtu.be/LqoIz8Nx7Ts
Authentication With The SAFE Stack. Generalized Remoting Proxies, Reactive Tokens, IndexDb. (Pt. 8)

Here is my masterpiece.

4pm. Organized them into a separate playlist.

https://www.youtube.com/playlist?list=PL04PGV4cTuIVZGJZI1POoobUSjmSIhIlc
Authentication With ASP.NET Core And F#

I'll post this one into the F# slack.

4:05pm. Posted it on the F# sub, slack and twitter.

4:10pm. Phew.

e: is at 20gb?

How the hell did that happen?

4:15pm. I shouldn't have tried turning on the render cache that one time. I observed the opposite of the screencast being smoother when I did.

Anyway, I am done for the day. Who is going to do any more?

Actually, I do feel like doing more.

If I can clear the microservice hurdle, I could try looking for jobs again.

4:20pm. Right now let me chill for a bit and then I'll watch a video or two. I still haven't read the Mahoako chapter.

5:25pm. https://youtu.be/DFDbh1c9zyE
What are microservices?!?!? Let’s build one with .NET and Docker!

Done with lunch. I kind of feel like watching this.

5:45pm. https://youtu.be/DFDbh1c9zyE?t=622
What are microservices?!?!? Let’s build one with .NET and Docker!

I'll keep these learning paths in mind. Let me close here. This video is so boring that I skipped a quarter of it. I'll leave the hands on stuff for tomorrow.

It is fine to stop at this time. I went through quite a gauntlet in the last month. April is almost over. Hopefully, May will be more interesting.

5:55pm. It seems the economy is booming in Netherlands. It might be worth looking for a RJ there."

---
## [PixelExperience-Devices/kernel_motorola_msm8998](https://github.com/PixelExperience-Devices/kernel_motorola_msm8998)@[d7ad2d19a2...](https://github.com/PixelExperience-Devices/kernel_motorola_msm8998/commit/d7ad2d19a2a25094c7121a49c345d137b762e34b)
#### Thursday 2023-04-27 16:41:31 by Christian Brauner

BACKPORT: signal: add pidfd_send_signal() syscall

The kill() syscall operates on process identifiers (pid). After a process
has exited its pid can be reused by another process. If a caller sends a
signal to a reused pid it will end up signaling the wrong process. This
issue has often surfaced and there has been a push to address this problem [1].

This patch uses file descriptors (fd) from proc/<pid> as stable handles on
struct pid. Even if a pid is recycled the handle will not change. The fd
can be used to send signals to the process it refers to.
Thus, the new syscall pidfd_send_signal() is introduced to solve this
problem. Instead of pids it operates on process fds (pidfd).

/* prototype and argument /*
long pidfd_send_signal(int pidfd, int sig, siginfo_t *info, unsigned int flags);

/* syscall number 424 */
The syscall number was chosen to be 424 to align with Arnd's rework in his
y2038 to minimize merge conflicts (cf. [25]).

In addition to the pidfd and signal argument it takes an additional
siginfo_t and flags argument. If the siginfo_t argument is NULL then
pidfd_send_signal() is equivalent to kill(<positive-pid>, <signal>). If it
is not NULL pidfd_send_signal() is equivalent to rt_sigqueueinfo().
The flags argument is added to allow for future extensions of this syscall.
It currently needs to be passed as 0. Failing to do so will cause EINVAL.

/* pidfd_send_signal() replaces multiple pid-based syscalls */
The pidfd_send_signal() syscall currently takes on the job of
rt_sigqueueinfo(2) and parts of the functionality of kill(2), Namely, when a
positive pid is passed to kill(2). It will however be possible to also
replace tgkill(2) and rt_tgsigqueueinfo(2) if this syscall is extended.

/* sending signals to threads (tid) and process groups (pgid) */
Specifically, the pidfd_send_signal() syscall does currently not operate on
process groups or threads. This is left for future extensions.
In order to extend the syscall to allow sending signal to threads and
process groups appropriately named flags (e.g. PIDFD_TYPE_PGID, and
PIDFD_TYPE_TID) should be added. This implies that the flags argument will
determine what is signaled and not the file descriptor itself. Put in other
words, grouping in this api is a property of the flags argument not a
property of the file descriptor (cf. [13]). Clarification for this has been
requested by Eric (cf. [19]).
When appropriate extensions through the flags argument are added then
pidfd_send_signal() can additionally replace the part of kill(2) which
operates on process groups as well as the tgkill(2) and
rt_tgsigqueueinfo(2) syscalls.
How such an extension could be implemented has been very roughly sketched
in [14], [15], and [16]. However, this should not be taken as a commitment
to a particular implementation. There might be better ways to do it.
Right now this is intentionally left out to keep this patchset as simple as
possible (cf. [4]).

/* naming */
The syscall had various names throughout iterations of this patchset:
- procfd_signal()
- procfd_send_signal()
- taskfd_send_signal()
In the last round of reviews it was pointed out that given that if the
flags argument decides the scope of the signal instead of different types
of fds it might make sense to either settle for "procfd_" or "pidfd_" as
prefix. The community was willing to accept either (cf. [17] and [18]).
Given that one developer expressed strong preference for the "pidfd_"
prefix (cf. [13]) and with other developers less opinionated about the name
we should settle for "pidfd_" to avoid further bikeshedding.

The  "_send_signal" suffix was chosen to reflect the fact that the syscall
takes on the job of multiple syscalls. It is therefore intentional that the
name is not reminiscent of neither kill(2) nor rt_sigqueueinfo(2). Not the
fomer because it might imply that pidfd_send_signal() is a replacement for
kill(2), and not the latter because it is a hassle to remember the correct
spelling - especially for non-native speakers - and because it is not
descriptive enough of what the syscall actually does. The name
"pidfd_send_signal" makes it very clear that its job is to send signals.

/* zombies */
Zombies can be signaled just as any other process. No special error will be
reported since a zombie state is an unreliable state (cf. [3]). However,
this can be added as an extension through the @flags argument if the need
ever arises.

/* cross-namespace signals */
The patch currently enforces that the signaler and signalee either are in
the same pid namespace or that the signaler's pid namespace is an ancestor
of the signalee's pid namespace. This is done for the sake of simplicity
and because it is unclear to what values certain members of struct
siginfo_t would need to be set to (cf. [5], [6]).

/* compat syscalls */
It became clear that we would like to avoid adding compat syscalls
(cf. [7]).  The compat syscall handling is now done in kernel/signal.c
itself by adding __copy_siginfo_from_user_generic() which lets us avoid
compat syscalls (cf. [8]). It should be noted that the addition of
__copy_siginfo_from_user_any() is caused by a bug in the original
implementation of rt_sigqueueinfo(2) (cf. 12).
With upcoming rework for syscall handling things might improve
significantly (cf. [11]) and __copy_siginfo_from_user_any() will not gain
any additional callers.

/* testing */
This patch was tested on x64 and x86.

/* userspace usage */
An asciinema recording for the basic functionality can be found under [9].
With this patch a process can be killed via:

 #define _GNU_SOURCE
 #include <errno.h>
 #include <fcntl.h>
 #include <signal.h>
 #include <stdio.h>
 #include <stdlib.h>
 #include <string.h>
 #include <sys/stat.h>
 #include <sys/syscall.h>
 #include <sys/types.h>
 #include <unistd.h>

 static inline int do_pidfd_send_signal(int pidfd, int sig, siginfo_t *info,
                                         unsigned int flags)
 {
 #ifdef __NR_pidfd_send_signal
         return syscall(__NR_pidfd_send_signal, pidfd, sig, info, flags);
 #else
         return -ENOSYS;
 #endif
 }

 int main(int argc, char *argv[])
 {
         int fd, ret, saved_errno, sig;

         if (argc < 3)
                 exit(EXIT_FAILURE);

         fd = open(argv[1], O_DIRECTORY | O_CLOEXEC);
         if (fd < 0) {
                 printf("%s - Failed to open \"%s\"\n", strerror(errno), argv[1]);
                 exit(EXIT_FAILURE);
         }

         sig = atoi(argv[2]);

         printf("Sending signal %d to process %s\n", sig, argv[1]);
         ret = do_pidfd_send_signal(fd, sig, NULL, 0);

         saved_errno = errno;
         close(fd);
         errno = saved_errno;

         if (ret < 0) {
                 printf("%s - Failed to send signal %d to process %s\n",
                        strerror(errno), sig, argv[1]);
                 exit(EXIT_FAILURE);
         }

         exit(EXIT_SUCCESS);
 }

/* Q&A
 * Given that it seems the same questions get asked again by people who are
 * late to the party it makes sense to add a Q&A section to the commit
 * message so it's hopefully easier to avoid duplicate threads.
 *
 * For the sake of progress please consider these arguments settled unless
 * there is a new point that desperately needs to be addressed. Please make
 * sure to check the links to the threads in this commit message whether
 * this has not already been covered.
 */
Q-01: (Florian Weimer [20], Andrew Morton [21])
      What happens when the target process has exited?
A-01: Sending the signal will fail with ESRCH (cf. [22]).

Q-02:  (Andrew Morton [21])
       Is the task_struct pinned by the fd?
A-02:  No. A reference to struct pid is kept. struct pid - as far as I
       understand - was created exactly for the reason to not require to
       pin struct task_struct (cf. [22]).

Q-03: (Andrew Morton [21])
      Does the entire procfs directory remain visible? Just one entry
      within it?
A-03: The same thing that happens right now when you hold a file descriptor
      to /proc/<pid> open (cf. [22]).

Q-04: (Andrew Morton [21])
      Does the pid remain reserved?
A-04: No. This patchset guarantees a stable handle not that pids are not
      recycled (cf. [22]).

Q-05: (Andrew Morton [21])
      Do attempts to signal that fd return errors?
A-05: See {Q,A}-01.

Q-06: (Andrew Morton [22])
      Is there a cleaner way of obtaining the fd? Another syscall perhaps.
A-06: Userspace can already trivially retrieve file descriptors from procfs
      so this is something that we will need to support anyway. Hence,
      there's no immediate need to add another syscalls just to make
      pidfd_send_signal() not dependent on the presence of procfs. However,
      adding a syscalls to get such file descriptors is planned for a
      future patchset (cf. [22]).

Q-07: (Andrew Morton [21] and others)
      This fd-for-a-process sounds like a handy thing and people may well
      think up other uses for it in the future, probably unrelated to
      signals. Are the code and the interface designed to permit such
      future applications?
A-07: Yes (cf. [22]).

Q-08: (Andrew Morton [21] and others)
      Now I think about it, why a new syscall? This thing is looking
      rather like an ioctl?
A-08: This has been extensively discussed. It was agreed that a syscall is
      preferred for a variety or reasons. Here are just a few taken from
      prior threads. Syscalls are safer than ioctl()s especially when
      signaling to fds. Processes are a core kernel concept so a syscall
      seems more appropriate. The layout of the syscall with its four
      arguments would require the addition of a custom struct for the
      ioctl() thereby causing at least the same amount or even more
      complexity for userspace than a simple syscall. The new syscall will
      replace multiple other pid-based syscalls (see description above).
      The file-descriptors-for-processes concept introduced with this
      syscall will be extended with other syscalls in the future. See also
      [22], [23] and various other threads already linked in here.

Q-09: (Florian Weimer [24])
      What happens if you use the new interface with an O_PATH descriptor?
A-09:
      pidfds opened as O_PATH fds cannot be used to send signals to a
      process (cf. [2]). Signaling processes through pidfds is the
      equivalent of writing to a file. Thus, this is not an operation that
      operates "purely at the file descriptor level" as required by the
      open(2) manpage. See also [4].

/* References */
[1]:  https://lore.kernel.org/lkml/20181029221037.87724-1-dancol@google.com/
[2]:  https://lore.kernel.org/lkml/874lbtjvtd.fsf@oldenburg2.str.redhat.com/
[3]:  https://lore.kernel.org/lkml/20181204132604.aspfupwjgjx6fhva@brauner.io/
[4]:  https://lore.kernel.org/lkml/20181203180224.fkvw4kajtbvru2ku@brauner.io/
[5]:  https://lore.kernel.org/lkml/20181121213946.GA10795@mail.hallyn.com/
[6]:  https://lore.kernel.org/lkml/20181120103111.etlqp7zop34v6nv4@brauner.io/
[7]:  https://lore.kernel.org/lkml/36323361-90BD-41AF-AB5B-EE0D7BA02C21@amacapital.net/
[8]:  https://lore.kernel.org/lkml/87tvjxp8pc.fsf@xmission.com/
[9]:  https://asciinema.org/a/IQjuCHew6bnq1cr78yuMv16cy
[11]: https://lore.kernel.org/lkml/F53D6D38-3521-4C20-9034-5AF447DF62FF@amacapital.net/
[12]: https://lore.kernel.org/lkml/87zhtjn8ck.fsf@xmission.com/
[13]: https://lore.kernel.org/lkml/871s6u9z6u.fsf@xmission.com/
[14]: https://lore.kernel.org/lkml/20181206231742.xxi4ghn24z4h2qki@brauner.io/
[15]: https://lore.kernel.org/lkml/20181207003124.GA11160@mail.hallyn.com/
[16]: https://lore.kernel.org/lkml/20181207015423.4miorx43l3qhppfz@brauner.io/
[17]: https://lore.kernel.org/lkml/CAGXu5jL8PciZAXvOvCeCU3wKUEB_dU-O3q0tDw4uB_ojMvDEew@mail.gmail.com/
[18]: https://lore.kernel.org/lkml/20181206222746.GB9224@mail.hallyn.com/
[19]: https://lore.kernel.org/lkml/20181208054059.19813-1-christian@brauner.io/
[20]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[21]: https://lore.kernel.org/lkml/20181228152012.dbf0508c2508138efc5f2bbe@linux-foundation.org/
[22]: https://lore.kernel.org/lkml/20181228233725.722tdfgijxcssg76@brauner.io/
[23]: https://lwn.net/Articles/773459/
[24]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[25]: https://lore.kernel.org/lkml/CAK8P3a0ej9NcJM8wXNPbcGUyOUZYX+VLoDFdbenW3s3114oQZw@mail.gmail.com/

Cc: "Eric W. Biederman" <ebiederm@xmission.com>
Cc: Jann Horn <jannh@google.com>
Cc: Andy Lutomirsky <luto@kernel.org>
Cc: Andrew Morton <akpm@linux-foundation.org>
Cc: Oleg Nesterov <oleg@redhat.com>
Cc: Al Viro <viro@zeniv.linux.org.uk>
Cc: Florian Weimer <fweimer@redhat.com>
Signed-off-by: Christian Brauner <christian@brauner.io>
Reviewed-by: Tycho Andersen <tycho@tycho.ws>
Reviewed-by: Kees Cook <keescook@chromium.org>
Reviewed-by: David Howells <dhowells@redhat.com>
Acked-by: Arnd Bergmann <arnd@arndb.de>
Acked-by: Thomas Gleixner <tglx@linutronix.de>
Acked-by: Serge Hallyn <serge@hallyn.com>
Acked-by: Aleksa Sarai <cyphar@cyphar.com>

(cherry picked from commit 3eb39f47934f9d5a3027fe00d906a45fe3a15fad)

Conflicts:
        arch/x86/entry/syscalls/syscall_32.tbl - trivial manual merge
        arch/x86/entry/syscalls/syscall_64.tbl - trivial manual merge
        include/linux/proc_fs.h - trivial manual merge
        include/linux/syscalls.h - trivial manual merge
        include/uapi/asm-generic/unistd.h - trivial manual merge
        kernel/signal.c - struct kernel_siginfo does not exist in 4.14
        kernel/sys_ni.c - cond_syscall is used instead of COND_SYSCALL
        arch/x86/entry/syscalls/syscall_32.tbl
        arch/x86/entry/syscalls/syscall_64.tbl

(1. manual merges because of 4.14 differences
 2. change prepare_kill_siginfo() to use struct siginfo instead of
kernel_siginfo
 3. use copy_from_user() instead of copy_siginfo_from_user() in copy_siginfo_from_user_any()
 4. replaced COND_SYSCALL with cond_syscall
 5. Removed __ia32_sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_32.tbl.
 6. Replaced __x64_sys_pidfd_send_signal with sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_64.tbl.)

Bug: 135608568
Test: test program using syscall(__NR_pidfd_send_signal,..) to send SIGKILL
Change-Id: I34da11c63ac8cafb0353d9af24c820cef519ec27
Signed-off-by: Suren Baghdasaryan <surenb@google.com>
Signed-off-by: electimon <electimon@gmail.com>

---
## [RatanMasanta/PracticeJava](https://github.com/RatanMasanta/PracticeJava)@[19f0a26c6e...](https://github.com/RatanMasanta/PracticeJava/commit/19f0a26c6e9f7584e27ebbdb5799b3e8b54357b9)
#### Thursday 2023-04-27 17:20:18 by Ratan Masanta

Changes for 23rd April 2022
Leetcode 1830. Minimum Number of Operations to Make String Sorted
Solution:
Before starting
What leetcode is providing us with the strings is a number. It is just a number expressed with base-26 digits. I will consider it for the rest of this article, in which I will deal with digits for making it more easy to understand. So please remember that their string is nothing else but a number expressed in base-26.

Explanation without code
Decreasing
Let's start with a basic problem. I give you the number 15324. I want you to give me the highest number following those two conditions :

It should be lower than the original
It should contain exactly the same digits
The answer is 15243. How did I find it? I start from the end, and I'm looking for the first digit which will not follow the decreasing order (from right remember). So 4-> 2 -> 3. OK, we found 3. I then switch with the highest value lower than 3, which is 2. 15234, and then, I revert everything on the right of the 2 we just put, so 15243.

Feel free to read the explanation of the solution of this problem : https://leetcode.com/problems/next-permutation/ (it's the exact opposite problem).

What about the algorithm I just described ? It is exactly the algorithm that leetcode is using in the problem. So what they do is just getting the highest lower number formed with those digits.

Counting (with distinct digits)
Now, let's consider we have 4 digits: 1, 2, 3 and 4. I would like to know the number of combination I can make with those digits. It's 4! (4×3×2×1) = 24. Now, let's list them all here in ascending order :

1234
1243
1324
1342
1423
1432
2134
2143
2314
2341
2413
2431
3124
3142
3214
3241
3412
3421
4123
4132
4213
4231
4312
4321
So now, let's assume I give you the number 3412, and I ask you how much permutations do I need to make it sorted. Solution is quite easy, you just have to look at the list above, it's 17. Did you fall in the trap? :-) Actually it is 16, because the first one in the list with rank 1 has a score of 0 in the problem we are trying to solve. But how could we find 16 without that list ?

4×3×2×1 possibilities. Let's call this number f.
And let's assume we have an array of the digits we are using : [1,2,3,4]
Let's count the number of non zero elements in the array : 4. Let's call this value p
First, we are using the 3rd digit which is not 0 of the array. So in order to get his rank, we need to do (f/p)×(3-1) = 6×2 = 12

Now, let's divide f by the number of non 0 elements in the array (4) and let's replace the 3 by a zero.
Now, f=6 and array is [1,2,0,4] and p = 3.
Now, let's do this again, this time, 4 is the 3rd digit which is not 0 in the array. So once again (f/p)×(3-1) = 2×2 = 4

Let's do it again, with f=2, array=[1,2,0,0] and p = 2. (f/p)×(1-1) = 1×0 = 0
Let's do it again with f=1, array=[0,2,0,0] and p = 1. (f/p)×(1-1) = 1×0 = 0

Ok, now, let's sum up all what we have : 12+4+0+0 = 16, which is exactly the result we were looking for.

So now, we know how to solve the leetcode problem for a string which would only contain distinct characters. Now, let's see how to solve this with characters that can be duplicated.

Counting (with digits that can appear many times)
Now, let's make the problem more difficult. What is the position of the number 1223 in increasing order  ? Ok, I'm just kidding, what is the position of the number 2312 in the list. Then, the previous method cannot be useful, as we have 2 which appears 2 times. Let's try, same as before, to do the list of all numbers with those digits, in increasing order :

1223
1232
1322
2123
2132
2213
2231
2312
2321
3122
3212
3221
How many possibilities we have ? Actually, it seems to be 4!/(product of number of occurrences of all digits). 4! / 2 = 12, which seems to work. So, now, let's try with 12333. With our formula, we can predict that we will have 5! / 3 = 40 results. Let's list them all :

12333
13233
13323
13332
21333
23133
23313
23331
31233
31323
31332
32133
32313
32331
33123
33132
33213
33231
33312
33321
Oooops, we actually have only 20, not 40. It is because the result is 5! / ([numberOfOne]!x[numberOfTwo]!x[numberOfThree]!) = 120 / 6 = 20.

OK, this will be our last listing (I promess), let's try with 11223 :

11223
11232
11322
12123
12132
12213
12231
12312
12321
13122
13212
13221
21123
21132
21213
21231
21312
21321
22113
22131
22311
23112
23121
23211
31122
31212
31221
32112
32121
32211
So we can see that we have 30 results, which match our prediction : 5! / (2!x2!x1!) = 120 / 4 = 30. Now, and it is the leetcode problem, how to know the rank of 23121 (we know from the list it is 22).

As we can see, the numbers with 1 and 2 appears 2 times more in the first position than the number 3. Because we have 2 occurrences of 2, it seems that it appears 2! times more. Sorry, but not this time. That is why it is important to run with multiple examples in algorithms. We can see in the previous list (12333) that numbers starting with a 3 appears 3 times more than numbers starting with a 2 or a 1.

5! / (2! x 2! x 1!)

Let's do first an array of pairs (value, occurrences) = [[1,2], [2,2], [3,1]]. So we start with n, which is the number of possibilities :
n / (sum of occurrences) * (sum of occurrences before). For 2, we have, (30 / 5) * 2 = 6 * 2 = 12
Now, we have [[1,2], [2,1], [3,1]], and number of possibilities is 4! / (2! x 1! x 1!) = 12
Next digit is a 3, so (12 / 4) * (3) = 9
Now we have [[1,2], [2,1], [3,0]], and number of possibilities is 3! / (2! x 1! x 0!) = 3
Next digit is a 1, so (3 / 3) * (0) = 0
Now we have [[1,1], [2,1], [3,0]] and number of possibilities is 2! / (1! x 1! x 0!) = 2
Next digit is a 2, so (2/2) * 1 = 1
Now we have [[1,1], [2,0], [3,0]] and number of possibilities is 1! / (1! x 0! x 0!) = 1
Next digit is a 1, so (1/1) * 0 = 0
Let's sum all numbers we got : 12 + 9 + 0 + 1 + 0 : 22. Which is the result we expected.

That's it on how to solve the leetcode problem. We come up with a solution, in n x m complexity (where m is the number of characters allowed and n the number of characters).

---
## [faiyazsadi/misc](https://github.com/faiyazsadi/misc)@[146785f44e...](https://github.com/faiyazsadi/misc/commit/146785f44e41e6ddac5165e4a41ba12d5c170e4e)
#### Thursday 2023-04-27 17:49:09 by faiyazsadi

SHA-1 shit-tier implementation not copied from chatgpt and I clearly understand the theory behind don't fucken judge

---
## [MF366-Coding/The-Psychologist](https://github.com/MF366-Coding/The-Psychologist)@[03c721c0ec...](https://github.com/MF366-Coding/The-Psychologist/commit/03c721c0eca9064304b63249a75b61a1b535ee47)
#### Thursday 2023-04-27 18:19:35 by MF366-Coding

DONE FOR THE DAY

What is missing?
- Battle system
- Storyline (it's on paper tho)
- Enemie check loading (gonna work on that tomorrow)
- Music (that is with my friend @norbcodes - sorry for the tag)

I think that is all FOR NOW.

---
## [Blusutils/DESrv](https://github.com/Blusutils/DESrv)@[b7519117b3...](https://github.com/Blusutils/DESrv/commit/b7519117b370bfd9fb833cc37b70c57f2c04a092)
#### Thursday 2023-04-27 19:36:42 by Egor Bron

Lots of fixes and beginnings
Yeah, screw your CIs, commit all this shit together
* Extension loading logic in bootstrapper
* Moved thread management to separate project
* Started creating commands API
* Removed console services
* Fixed `Dispose`
* Created DESrv.InternalPlugin and Dip
* Fixed & added some doc-comments

---
## [KarlJoad/Emacs_dotfiles](https://github.com/KarlJoad/Emacs_dotfiles)@[962ac66268...](https://github.com/KarlJoad/Emacs_dotfiles/commit/962ac66268b4199d524a470ed29d52242d786c5d)
#### Thursday 2023-04-27 20:29:51 by Karl Hallsby

Change how org-roam is loaded based on the system I am running on

The way this is done is SUPER hacky. I hate myself for having to do
this. But the problem comes down to the :straight symbol being used as
a plist and its quoting by straight.el. I can provide a function to
determine the backend to use, but the function MUST be one word (no
hyphens at all). There are likely other limitations that I am not
aware of.

---
## [josh3io/evals](https://github.com/josh3io/evals)@[24dae81ae0...](https://github.com/josh3io/evals/commit/24dae81ae06ebc70808690c7a147f2710e3e54bf)
#### Thursday 2023-04-27 20:38:54 by Yohei Inui

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
## [EspressoSystems/jellyfish](https://github.com/EspressoSystems/jellyfish)@[a81387790a...](https://github.com/EspressoSystems/jellyfish/commit/a81387790ad9a91706a615a4a77a5bb15591a5ac)
#### Thursday 2023-04-27 21:02:01 by Gus Gutoski

make `bytes_from_field_elements` infallible with paranoid checks for overflow (#250)

* impl Error for PCSError

* use anyhow for bytes_from_field_elements error type

* make bytes_from_field_elements infallible

* appease clippy (you're welcome)

* tidy an ugly line

* better test

* check everything for overflow, better panic messages

* remove commented code (oops)

---
## [Staph9000/PythonEx_Library_System](https://github.com/Staph9000/PythonEx_Library_System)@[1ad878bed8...](https://github.com/Staph9000/PythonEx_Library_System/commit/1ad878bed816309a4f51c5b3b8c5dabfbe485455)
#### Thursday 2023-04-27 21:08:52 by Staph9000

Create 28_4_23_AndrewDPirate_Edit

A few things to think about relative to your own implementation:

    Orchestration: When there are multiple classes involved, there's generally one of them that should logically be responsible for orchestrating activity. In this case, Library makes sense. You want it to have the top level methods for adding Books, Borrowers and for lending and returning books. It should coordinate what happens with the Book and Borrower objects.
    You had a little conflicting use of Adding books and the process of lending them. The library shouldn't forget about the book if it's loaned out.
    The book should know who's borrowed it. Imagine it like the old library cards that used to sit in library books, that would say who loaned it.
    Borrower should have a repr()
    The member_number should be assigned by the Library, because who else would do that?
    Don't have objects like Book and Borrower return strings about success or failure. The calling code understands its own context, so it should decide. These slave objects should just indicate the kind of success or failure they've experienced.
    Search is more useful with Contains, so they don't need to know the exact title.
    str.join() is your friend.
    Needed to deal with cases of books that were already loaned, or already returned.

    I made the search distinguish between books that were available, and books that were already loaned.

    I made the containers for books and borrowers set()'s, so it can't get duplicates.

    "Pickle Rick" ... noice.

The sort of thing I've listed above is me trying to boost you more rapidly through the inevitable learning curve.
One of my old managers that I particularly liked, used to say that in software, we have to solve new problems three times before we get it right. 

1st, we tend to make some analog of the existing manual methods that we understand. On using that, we realize that it doesn't gain us much efficiency. The admin overhead of doing everything with the computer offsets the benefits.

2nd, we realize we can reinvent the system without all the prior human constraints, so that the potential of new efficiencies emerges, but we have to reinvent the human engagement with it also.

3rd, we realize that the problem we've been solving is actually WAY more general than the little niche that we implemented, and so we genericize the application so it can be configured to solve wide ranges of related problems, without having to constantly reinvent it.

We may however be approaching the need to a 4th iteration, where it needs to be reinvented to have intelligence on the inside, so it can reinvent itself to solve whatever problem comes along.

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[4cf0651670...](https://github.com/cmss13-devs/cmss13/commit/4cf06516705b3e0f4a6f446cd36eaa15b554a561)
#### Thursday 2023-04-27 21:18:06 by BlackCrystalic

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
## [tanayp327/Quintic5Flask](https://github.com/tanayp327/Quintic5Flask)@[8ec2e2d3e3...](https://github.com/tanayp327/Quintic5Flask/commit/8ec2e2d3e335a99722cc1251d0c3b572ba48602b)
#### Thursday 2023-04-27 21:25:12 by Raunak Mondal

You used to call me on my You used to, you used to Yeah You used to call me on my cell phone Late night when you need my love Call me on my cell phone Late night when you need my love And I know when that hotline bling That can only mean one thing I know when that hotline bling That can only mean one thing Ever since I left the city, you Got a reputation for yourself now Everybody knows and I feel left out Girl, you got me down, you got me stressed out 'Cause ever since I left the city, you Started wearing less and goin' out more Glasses of champagne out on the dance floor Hangin' with some girls I've never seen before You used to call me on my cell phone Late night when you need my love Call me on my cell phone Late night when you need my love I know when that hotline bling That can only mean one thing I know when that hotline bling That can only mean one thing Ever since I left the city, you, you, you You and me, we just don't get along You make me feel like I did you wrong Going places where you don't belong Ever since I left the city, you You got exactly what you asked for Running out of pages in your passport Hanging with some girls I've never seen before You used to call me on my cell phone Late night when you need my love Call me on my cell phone Late night when you need my love And I know when that hotline bling That can only mean one thing I know when that hotline bling That can only mean one thing These days, all I do is Wonder if you're bendin' over backwards for someone else Wonder if you're rollin' up a Backwoods for someone else Doing things I taught you, gettin' nasty for someone else You don't need no one else You don't need nobody else, no Why you never alone? Why you always touchin' road? Used to always stay at home, be a good girl You was in the zone Yeah, you should just be yourself Right now, you're someone else You used to call me on my cell phone Late night when you need my love Call me on my cell phone Late night when you need my love And I know when that hotline bling That can only mean one thing I know when that hotline bling That can only mean one thing Ever since I left the city

You used to call me on my
You used to, you used to
Yeah
You used to call me on my cell phone
Late night when you need my love
Call me on my cell phone
Late night when you need my love
And I know when that hotline bling
That can only mean one thing
I know when that hotline bling
That can only mean one thing
Ever since I left the city, you
Got a reputation for yourself now
Everybody knows and I feel left out
Girl, you got me down, you got me stressed out
'Cause ever since I left the city, you
Started wearing less and goin' out more
Glasses of champagne out on the dance floor
Hangin' with some girls I've never seen before
You used to call me on my cell phone
Late night when you need my love
Call me on my cell phone
Late night when you need my love
I know when that hotline bling
That can only mean one thing
I know when that hotline bling
That can only mean one thing
Ever since I left the city, you, you, you
You and me, we just don't get along
You make me feel like I did you wrong
Going places where you don't belong
Ever since I left the city, you
You got exactly what you asked for
Running out of pages in your passport
Hanging with some girls I've never seen before
You used to call me on my cell phone
Late night when you need my love
Call me on my cell phone
Late night when you need my love
And I know when that hotline bling
That can only mean one thing
I know when that hotline bling
That can only mean one thing
These days, all I do is
Wonder if you're bendin' over backwards for someone else
Wonder if you're rollin' up a Backwoods for someone else
Doing things I taught you, gettin' nasty for someone else
You don't need no one else
You don't need nobody else, no
Why you never alone?
Why you always touchin' road?
Used to always stay at home, be a good girl
You was in the zone
Yeah, you should just be yourself
Right now, you're someone else
You used to call me on my cell phone
Late night when you need my love
Call me on my cell phone
Late night when you need my love
And I know when that hotline bling
That can only mean one thing
I know when that hotline bling
That can only mean one thing
Ever since I left the city

---
## [lizardqueenlexi/orbstation](https://github.com/lizardqueenlexi/orbstation)@[200b739c0a...](https://github.com/lizardqueenlexi/orbstation/commit/200b739c0a0bbfff95dbfd697786013c92cb6cf6)
#### Thursday 2023-04-27 21:31:14 by Kyle Spier-Swenson

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
## [lizardqueenlexi/orbstation](https://github.com/lizardqueenlexi/orbstation)@[773cc9542a...](https://github.com/lizardqueenlexi/orbstation/commit/773cc9542a54837fc52b15eb09cc98d7226049fb)
#### Thursday 2023-04-27 21:31:14 by MrMelbert

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
## [lizardqueenlexi/orbstation](https://github.com/lizardqueenlexi/orbstation)@[821123b598...](https://github.com/lizardqueenlexi/orbstation/commit/821123b59850bc4d0556b8dd7e0cf169f7fa6bc3)
#### Thursday 2023-04-27 21:31:14 by ChungusGamer666

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
## [Tsunamico/Tsunamico-cmss13](https://github.com/Tsunamico/Tsunamico-cmss13)@[d728da3e02...](https://github.com/Tsunamico/Tsunamico-cmss13/commit/d728da3e02664297050d82dc01c87414c61345ef)
#### Thursday 2023-04-27 23:18:04 by Puckaboo2

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
## [git-for-windows/git](https://github.com/git-for-windows/git)@[ede561936b...](https://github.com/git-for-windows/git/commit/ede561936bf0e237ac5269ce938876fe2836dbb0)
#### Thursday 2023-04-27 23:29:00 by Johannes Schindelin

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

