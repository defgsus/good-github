## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-03-25](docs/good-messages/2023/2023-03-25.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,980,959 were push events containing 3,411,283 commit messages that amount to 202,528,473 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 59 messages:


## [Burger1998/Yogstation](https://github.com/Burger1998/Yogstation)@[8e3e0b1450...](https://github.com/Burger1998/Yogstation/commit/8e3e0b1450189ebda3b2bc760c036ba6c59c6b6a)
#### Saturday 2023-03-25 00:14:19 by LazennG

adds magmite crusher to the things you can make at the world anvil (#17530)

* FUCK YOU PLASMA CUTTER

* updated it now just waiting on BAIOMU FOR FUCKIN SPRITES

* returned old sprites i had but it's still lacking 1 handed versions

* touched up some of the sprites but STILL NEED ONEHANDED ONES FROM BAIOMU

* FINALLY

---
## [crcrpar/pytorch](https://github.com/crcrpar/pytorch)@[11aab72dc9...](https://github.com/crcrpar/pytorch/commit/11aab72dc9da488832326a066d2e47520e4ab2b3)
#### Saturday 2023-03-25 01:09:50 by Driss Guessous

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
## [reyzheng/jenkins-pipeline](https://github.com/reyzheng/jenkins-pipeline)@[c0da728fc5...](https://github.com/reyzheng/jenkins-pipeline/commit/c0da728fc54f1933ce434050096837af171d26c3)
#### Saturday 2023-03-25 01:58:34 by Rey Cheng

fuck you java

Signed-off-by: Rey Cheng <reyzheng@gmail.com>

---
## [Quidifer/Cranium](https://github.com/Quidifer/Cranium)@[e1b3fde17a...](https://github.com/Quidifer/Cranium/commit/e1b3fde17aea5e725c850de60d6b4a3522e24d47)
#### Saturday 2023-03-25 02:01:50 by Karan Bhogal

LETS FREAKING GOOOOOOOOOOO THIS IS THE MOMENT, GET READY GET READY, WE ARE IN THE END GAME NOW BOYS AND GIRLS, THIS IS A VERY EXCITING TIME, ITS BEEN SO REAL, I'D LIKE TO THANK MY FAMILY AND FRIENDS AND THE GREATEST TEAM EVER

---
## [Timberpoes/tgstation-nxt](https://github.com/Timberpoes/tgstation-nxt)@[3156a0414e...](https://github.com/Timberpoes/tgstation-nxt/commit/3156a0414e96b597d4d53823066d29daa0b30737)
#### Saturday 2023-03-25 02:15:32 by san7890

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[d77ca677c3...](https://github.com/treckstar/yolo-octo-hipster/commit/d77ca677c393bc65251c389b4aab708a943e94a9)
#### Saturday 2023-03-25 02:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [KJSturgill/Meal_Planner](https://github.com/KJSturgill/Meal_Planner)@[121c615f8d...](https://github.com/KJSturgill/Meal_Planner/commit/121c615f8db9ba8fbbfba8e97ea328c3f614d109)
#### Saturday 2023-03-25 02:23:32 by KJSturgill

LINQ

oh boy, here's a shit ton of linq queries, like an insane amount of them but the project functions and meets the requirements, now to just add ingredients lists to make it a little less sad

---
## [gaurangnagar/ADmyBRAND-India](https://github.com/gaurangnagar/ADmyBRAND-India)@[50d8ded65a...](https://github.com/gaurangnagar/ADmyBRAND-India/commit/50d8ded65aefff10855985c4a2547e706c5b0067)
#### Saturday 2023-03-25 02:54:20 by Gaurang Nagar

Add files via upload

Once upon a time, there was a young woman named Ava who longed to escape the monotony of her everyday life. She yearned for adventure and excitement, so she decided to embark on a journey through the wilderness.

With nothing but a backpack full of supplies and a map in hand, Ava set off into the unknown. She walked for hours, taking in the beautiful scenery around her. The trees were tall and majestic, the birds sang sweetly, and the sound of a nearby stream filled the air.

As the sun began to set, Ava realized that she needed to find a place to rest for the night. She searched the surrounding area and eventually came across a small clearing that was perfect for setting up camp.

As she settled in for the night, Ava heard rustling in the bushes nearby. She tensed up, wondering what kind of creature might be lurking in the darkness. Suddenly, a figure emerged from the bushes and approached her campsite.

It was an unexpected visitor - a rugged-looking man with a wild beard and piercing blue eyes. He introduced himself as Finn, a seasoned adventurer who had been exploring the wilderness for years.

Despite her initial trepidation, Ava found herself drawn to Finn's infectious enthusiasm and zest for life. Over the next few days, they journeyed together through the wilderness, encountering all manner of challenges and obstacles along the way.

They climbed steep mountains, forded treacherous rivers, and braved fierce storms. Through it all, Ava and Finn formed a deep bond, sharing stories, laughter, and a sense of awe at the beauty and majesty of the natural world around them.

As their journey drew to a close, Ava knew that she would never forget the lessons she had learned and the experiences she had shared with Finn. She had discovered that sometimes, the most meaningful journeys are the ones we take with unexpected companions, and that true adventure can be found in the unlikeliest of places.

---
## [shardul22/awesome-docker](https://github.com/shardul22/awesome-docker)@[3164d6df94...](https://github.com/shardul22/awesome-docker/commit/3164d6df94f60d7d3d11629241c111ed416eb8eb)
#### Saturday 2023-03-25 02:56:34 by Derek Lee

Add Kurtosis to list of testing tools (#1063)

* Add Kurtosis to list of testing tools

Hey team! We'd like to add Kurtosis to the list of testing tools. 

*What is Kurtosis?* Kurtosis is a built system for multi-(docker)container test environments. 
*What is Kurtosis for?* Kurtosis is for engineers who dev against large distributed systems/applications and who experience pain when trying to configure multi (Docker) container environments for their testing workflows. 

Kurtosis can be used locally without the need to sign up and is free-forever under a source-available license (BSL). 

We have:
- Linked out to our Github: https://github.com/kurtosis-tech/kurtosis
- [A README on our GIthub](https://github.com/kurtosis-tech/kurtosis#readme)
- Content about how to setup/install the project (in our [Github README](https://github.com/kurtosis-tech/kurtosis#to-start-using-kurtosis) and on our [docs](https://docs.kurtosis.com/install)),
- Lots of great examples on: [Github](https://github.com/kurtosis-tech/awesome-kurtosis#awesome-kurtosis-) and in our [docs](https://docs.kurtosis.com/). 

I followed the [Quality Standards](https://github.com/veggiemonk/awesome-docker/blob/master/.github/CONTRIBUTING.md#quality-standards) you guys wrote, but please let me know if you've got any questions about Kurtosis or if we missed something!

Thanks

* add "composable" to description

---
## [JayAgra/scouting-app](https://github.com/JayAgra/scouting-app)@[dde948a0c2...](https://github.com/JayAgra/scouting-app/commit/dde948a0c25764dbefd4736faf06936d7abb4581)
#### Saturday 2023-03-25 03:12:07 by JayAgra

sp98hfgpiusf

i forgot a fucking ) and the entire thing broke what the hell I hate this

---
## [ktoma36/Citadel-Station-13-RP](https://github.com/ktoma36/Citadel-Station-13-RP)@[8117b28946...](https://github.com/ktoma36/Citadel-Station-13-RP/commit/8117b28946d2e07f902e8800245c34d008336ccc)
#### Saturday 2023-03-25 03:33:37 by nevimer

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
## [Salex08/tgstation](https://github.com/Salex08/tgstation)@[f9fe79a307...](https://github.com/Salex08/tgstation/commit/f9fe79a307dc55eb6e3ecf25019ef388889898ba)
#### Saturday 2023-03-25 03:40:47 by Dani Glore

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
## [MemedHams/Shiptest](https://github.com/MemedHams/Shiptest)@[31eabb62f1...](https://github.com/MemedHams/Shiptest/commit/31eabb62f1bfe944a58fa6b74d1745cf80cb83aa)
#### Saturday 2023-03-25 03:57:07 by spockye

The Crashed Starwalker (#1700)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
This PR adds a beach ruin based around a ship I've previously made,
called the "Starwalker"

![2023 01 16-16 33
48](https://user-images.githubusercontent.com/79304582/212715120-1234050a-b91c-411c-b792-82d0621cc549.png)

![2023 01 16-16 35
19](https://user-images.githubusercontent.com/79304582/212715457-6b643815-ab0f-4962-9222-1a0d6eeb7535.png)


it contains:
some medical supplies ( oinment slurry / herbal pack / crew monitor /
health scanner / charcoal bottle / misc pills )
one Swat suit
one shotgun / one energy cutlass
goliath cloak  / military rig
3 abandoned crates
1 gold crate / one silver crate
lizard wine
one baby carp
a radiant dance machine
a sci protolathe
misc salvage


Lore bit:
After a "most excellent robbery that went like, totally as planned", our
protagonists aboard the Starwalker fled the crime scene, with heavy
damage to the ship's hull. With one of the Engine blocks almost falling
off, The valiant crew decided that the best course of action would be a
"Totally rad emergency landing". This, of course, ended in disaster, as
the pilot was high on LSD.
The pilot did however manage to steer them towards a nearby lak- sike,
it's just some shallow water. Crashing directly onto the ground, the
ship split into multiple fragments, Killing the pilot and crewmate, and
Impaling the captain.
The captain knew that he didn't have long until the bloodloss would get
to him, and started moving all his treasure into a nearby cavern.
_THERE'S NO WAY_ he would die in that godforsaken ship, nor without his
treasures. This is where you now find him, rotting in his "100% real Cow
skin" throne _(spacemart Brand Comfy chair)_ .
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
currently there's a bit of a lack in beach ruins, something that I'd
like to help resolve!
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Adds a new Beach ruin, the beach_crashed_starwalker
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
## [JohnFulpWillard/tgstation](https://github.com/JohnFulpWillard/tgstation)@[a6f49ed542...](https://github.com/JohnFulpWillard/tgstation/commit/a6f49ed54255f9a8d4dfc27bc397e56f87029cb8)
#### Saturday 2023-03-25 04:32:44 by san7890

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
## [sweetmamatiff/Veneno](https://github.com/sweetmamatiff/Veneno)@[0b6564749d...](https://github.com/sweetmamatiff/Veneno/commit/0b6564749d9bb718fb7bfdd41fa677a89c0a9600)
#### Saturday 2023-03-25 05:17:18 by Tiffany Veneno Resilience

Create Life is like the game of snake

One day your ass smacks you in the face, and then you die.

---
## [massaheartsu/massastation](https://github.com/massaheartsu/massastation)@[8d7db532c0...](https://github.com/massaheartsu/massastation/commit/8d7db532c0f425e6cc68d975b526694bbaefc870)
#### Saturday 2023-03-25 05:32:14 by Bloop

Reworks blood deficiency backend, & some adjustments to slime blood deficiency (#74143)

## About The Pull Request

This is a followup PR to
https://github.com/tgstation/tgstation/pull/73866

Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/19991

I had suspected the nutrition loss slimes experience alongside blood
regen might necessitate some tweaks down the line and here we are. This
PR has two parts.

---

**PART I:** _Reworking the blood deficiency quirk backend_

As it is, blood drain from the blood deficiency occurs in the quirk's
subsystem process() call asynchronously to Life(), where the blood regen
occurs.

This results in the blood volume fluctuating constantly, making it
difficult to really make sense of readings and potentially introducing
race conditions. This PR changes that.

The blood deficiency quirk no longer processes and instead has a proc,
`lose_blood(delta_time)`, which is called in the `handle_blood()` proc
at the same time blood gets regenerated.

Added a `get_quirk` proc to help with this, so that we only have to
iterate through the quirks list once for each mob (rather than calling
has_quirk, then locate in quirks... etc).

Added a `TRAIT_BLOOD_DEFICIENCY` to further optimize the code.

---

**PART II:** _Some fine tuning of the slime blood deficiency quirk_

Slime regen works a bit differently than humans such that if they lose
-any- blood whatsoever, they will also lose nutrition. This means that
even if hooked up to an IV they will still become starving rather
quickly. A bit -too- quickly.

Instead, now the hunger does not kick in until `blood_volume` reaches
550. This means that if a slime with the blood deficiency quirk is
hooked up to an IV with say, welding fluid, and has over 150 nutrition,
they will regen blood faster than they lose it from the blood deficiency
quirk. Once they get to over 550 `blood_volume`, they will stop losing
hunger (from blood regen, anyway--normal hunger rate still applies).

So essentially this just allows slimes with the blood deficiency quirk
to be able to function so long as they stay hooked up to their IV's (or
chug welder fluid/some other toxin), which is the intended purpose of
the quirk.

Edit: As a bonus I added new blood bags for the exotic blood types, and
added a proc `update_mail_goodies` which updates the blood deficiency
quirk's mail goodies accordingly (crewmembers with blood deficiency get
sent blood bags, now they will get the correct type if their species
changes). While I was in these files I changed any immediate single
letter vars I could find and cleaned up what I could.


![image](https://user-images.githubusercontent.com/13398309/226739179-a21790e3-0be6-423a-be89-8d2cb84f6149.png)


<details>
<summary>The new blood packs</summary>


![image](https://user-images.githubusercontent.com/13398309/226743543-29fca53d-b3d1-4903-9706-35b2c00bbe78.png)

</details>

## Why It's Good For The Game

-This is arguably a more performant option than before, and fixes race
conditions from `Life()` and `quirk/blooddeficiency/process()` fighting
with one another.

-Adjustments to slime blood deficiency will enable it to function as
intended.

-It is now easier to read health analyzer blood volume readings for
blood deficient mobs.

-Now the correct blood packs are sent in the mail.

## Changelog

:cl:
qol: adjusted the blood deficiency quirk for slimepeople to not cause
excessive hunger as long as blood volume is kept above 550 via an IV
drip (or other means of getting welding fluid/some other toxin etc into
the bloodstream, e.g. ingestion)
qol: speciees with exotic blood types will now receive the correct blood
bag in the mail from having the blood deficiency perk
add: adds new blood bag types: TOX (slimepeople), H2O (podpeople), S
(snail)
fix: fixed blood deficiency quirk causing wild fluctuations in blood
volume on the analyzer, giving more accurate readings
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [DavidTran1311/Day_by_Day](https://github.com/DavidTran1311/Day_by_Day)@[900d365980...](https://github.com/DavidTran1311/Day_by_Day/commit/900d36598094f6479a0c11185e40e9ddbfebc8e9)
#### Saturday 2023-03-25 05:45:15 by aaliyahtran

Create tasklist and fix the popup and other shit

- put task ui in
- tried to code to zoom but im kind of stupid yall
- urrghhhhhhhhhh fixed the popup code
- did a lot of trial and error shit that didnt  work and is fucking embarrassing so thankfully github catches none of that!

---
## [diphons/D8G_Kernel_oxygen](https://github.com/diphons/D8G_Kernel_oxygen)@[1fbe771143...](https://github.com/diphons/D8G_Kernel_oxygen/commit/1fbe77114359e82dcd359c7bd9d80c091fbfde77)
#### Saturday 2023-03-25 05:49:48 by Angelo G. Del Regno

Makefile.lib: Lower kernel gzip compression to fastest

You're reading this - so you're trying to understand "JUST WHY OMG".
That's already a good step.

First of all, this is a downstream kernel - always keep that in mind!
Now, this kernel is targeting new *very powerful* Qualcomm platforms
like SM8250 and the Sony Edo platform - which has a very fast UFS card.

Keep in mind that the bootloader sets the CPU at a frequency that is
slightly faster than the "in the middle" ones, which is anyway not
veeeery fast - but that's good, really. I agree.

So.. check this out:   for Image.gz-dtb.....
COMP_LEVEL    SIZE
9             20116171
5      	      20220479
2      	      20940223
1      	      21231290

Remember again that we're loading from a UFS card and that
we are loading ~1.1MB more out of a 20MB file.
If you're smart enough you surely know already about RAM and CPU
overhead of very high compression levels.

If you still disagree with what I just did, read this commit description
another 20 times, or more, until you understand it. :)))

Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>

---
## [NewyearnewmeUwu/cmss13](https://github.com/NewyearnewmeUwu/cmss13)@[ef9d0c61a3...](https://github.com/NewyearnewmeUwu/cmss13/commit/ef9d0c61a3335d40c9bd9459479e0112903ccc02)
#### Saturday 2023-03-25 06:36:20 by Moonshanks

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[6c0854c497...](https://github.com/treckstar/yolo-octo-hipster/commit/6c0854c497da1c7e14909aac4860dd1cdd985beb)
#### Saturday 2023-03-25 07:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [mc-oofert/tgstation](https://github.com/mc-oofert/tgstation)@[1cdc327a8f...](https://github.com/mc-oofert/tgstation/commit/1cdc327a8f98c1592fc970a4ef1c39d685c81554)
#### Saturday 2023-03-25 09:26:12 by Jacquerel

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
## [Rombuilding-X00TD/android_kernel_asus_sdm660](https://github.com/Rombuilding-X00TD/android_kernel_asus_sdm660)@[694cad717e...](https://github.com/Rombuilding-X00TD/android_kernel_asus_sdm660/commit/694cad717e9d3160d408abc101ff8f816035da1d)
#### Saturday 2023-03-25 09:50:07 by Christian Brauner

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
## [ArrowOS-Devices/android_kernel_xiaomi_beryllium](https://github.com/ArrowOS-Devices/android_kernel_xiaomi_beryllium)@[7ec7b0f72b...](https://github.com/ArrowOS-Devices/android_kernel_xiaomi_beryllium/commit/7ec7b0f72b169daf2440f0f45ef08a450ac6734a)
#### Saturday 2023-03-25 11:35:40 by tanish2k09

Introducing KLapse - A kernel level livedisplay module v4.0:

Author: @tanish2k09 (email: tanish2k09.dev@gmail.com)

What is it?
Kernel-based Lapse ("K-Lapse") is a linear RGB scaling module that 'shifts' RGB based on time (of the day/selected by user), or (since v2.0) brightness. This concept is inspired from
LineageOS (formerly known as 'CyanogenMod') ROM's feature "livedisplay" which also changes the display settings (RGB, hue, temperature, etc) based on time.

Why did you decide to make this? (Tell me a story).
I (personally) am a big fan of the livedisplay feature found on LineageOS ROM. I used it every single day, since Android Lollipop. Starting from Android Nougat, a native night mode
solution was added to AOSP and it felt like livedisplay was still way superior, thanks to its various options (you could say it spoiled me, sure). I also maintained a kernel (Venom
kernel) for the device I was using at that time. It was all good until the OEM dropped support for the device at Android M, and XDA being XDA, was already working on N ROMs. The issue
was, these ROMs weren't LineageOS or based on it, so livedisplay was... gone. I decided I'll try to bring that feature to every other ROM. How would I do that? Of course! The kernel! It
worked on every single ROM, it was the key! I started to work on it ASAP and here it is, up on GitHub, licensed under GPL (check klapse.c), open to everyone :)

How does it work?
Think of it like a fancy night mode, but not really. Klapse is dependent on an RGB interface (like Gamma on MTK and KCAL on SD chipsets). It fetches time from the kernel, converts it to
local time, and selects and RGB set based on the time. The result is really smooth shifting of RGB over time.

How does it really work (dev)?
Klapse mode 1 (time-based scaling) uses a method void klapse_pulse(void) that should ideally be called every minute. This can be done by injecting a pulse call inside another method that
is called repeatedly naturally, like cpufreq or atomic or frame commits. It can be anything, whatever you like, even a kthread, as long as it is called repeatedly naturally. To execute
every 60 seconds, use jiffies or ktime, or any similar method. The pulse function fetches the current time and makes calculations based on the current hour and the values of the tunables
listed down below.

Klapse mode 2 (brightness-based scaling) uses a method void set_rgb_slider(<type> bl_lvl) where is the data type of the brightness level used in your kernel source. (OnePlus 6 uses u32
data type for bl_lvl) set_rgb_slider needs to be called/injected inside a function that sets brightness for your device. (OnePlus 6 uses dsi_panel.c for that, check out the diff for that
file in /op6)

What all stuff can it do?

1, Emulate night mode with the proper RGB settings
2, Smoothly scale from one set of RGB to another set of RGB in integral intervals over time.
3, Reduce perceived brightness using brightness_factor by reducing the amount of color on screen. Allows lower apparent brightness than system permits.
4, Scale RGB based on brightness of display (low brightness usually implies a dark environment, where yellowness is probably useful).
5, Automate the perceived brightness independent of whether klapse is enabled, using its own set of start and stop hours.
6, Be more efficient,faster by residing inside the kernel instead of having to use the HWC HAL like android's night mode.
7, (On older devices) Reduce stuttering or frame lags caused by native night mode.
8, An easier solution against overlay-based apps that run as service in userspace/Android and sometimes block apps asking for permissions.
9, Give you a Livedisplay alternative if it doesn't work in your ROM.
10, Impress your crush so you can get a date (Hey, don't forget to credit me if it works).

Alright, so this is a replacement for night mode?
NO! Not at all. One can say this is merely an alternative for LineageOS' Livedisplay, but inside a kernel. Night mode is a sub-function of both Livedisplay and KLapse. Most comparisons
here were made with night mode because that's what an average user uses, and will relate to the most. There is absolutely no reason for your Android kernel to not have KLapse. Go ahead
and add it or ask your kernel maintainer to. It's super-easy!

What can it NOT do (yet)?

1, Calculate scaling to the level of minutes, like "Start from 5:37pm till 7:19am". --TODO
2, Make coffee for you.
3, Fly you to the moon. Without a heavy suit.
4, Get you a monthly subscription of free food, cereal included.

All these following tunables are found in their respective files in /sys/klapse/

1. enable_klapse : A switch to enable or disable klapse. Values : 0 = off, 1 = on (since v2.0, 2 = brightness-dependent mode)
2. klapse_start_hour : The hour at which klapse should start scaling the RGB values from daytime to target (see next points). Values : 0-23
3. klapse_stop_hour : The hour by which klapse should scale back the RGB values from target to daytime (see next points). Values : 0-23
4. daytime_rgb : The RGB set that must be used for all the time outside of start and stop hour range.
5. target_rgb : The RGB set that must be scaled towards for all the time inside of start and stop hour range.
6. klapse_scaling_rate : Controls how soon the RGB reaches from daytime to target inside of start and stop hour range. Once target is reached, it remains constant till 30 minutes before
   stop hour, where target RGB scales back to daytime RGB.
7. brightness_factor : From the name itself, this value has the ability to bend perception and make your display appear as if it is at a lesser brightness level than it actually is at.
   It works by reducing the RGB values by the same factor. Values : 2-10, (10 means accurate brightness, 5 means 50% of current brightness, you get it)
8. brightness_factor_auto : A switch that allows you to automatically set the brightness factor in a set time range. Value : 0 = off, 1 = on
9. brightness_factor_auto_start_hour : The hour at which brightness_factor should be applied. Works only if #8 is 1. Values : 0-23
10. brightness_factor_auto_stop_hour : The hour at which brightness_factor should be reverted to 10. Works only if #8 is 1. Values : 0-23
11. backlight_range : The brightness range within which klapse should scale from daytime to target_rgb. Works only if #1 is 2. Values : MIN_BRIGHTNESS-MAX_BRIGHTNESS

Signed-off-by: Eliminater74 <eliminater74@gmail.com>
Signed-off-by: energyspear17 <energyspear17@gmail.com>
Signed-off-by: Michael <loukerismichalis@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>

---
## [tbs-shagai/odoo](https://github.com/tbs-shagai/odoo)@[f05491105f...](https://github.com/tbs-shagai/odoo/commit/f05491105f93939490cbeb078cb7653c38685644)
#### Saturday 2023-03-25 11:56:56 by Romain Derie

[FIX] website: redirect to case insensitive URL if not exact match

Before this commit, if a link to a page was not correct because of a
case mismatch, it would simply land on a 404 page.
While it's correct, as URL are case sensitive, it leads to a few bad UX
flow at the admin/editor level:
- Create a link in your page (on a text or a button eg), type an URL
  which does not exists (to create it after) like /Page
- Click on the link/button you just made, you are redirected to /Page
  which display a 404 with the "Create page" option (correct)
- When you click on that button, it will actually create a page with
  /page URL, leading to a mismatch between the URL you created and the
  page URL.
  Your link/button will still lead to a 404 URL as it points to /Page.

Since it's just a fallback when an exact URL match is not found, it
should not break anything and should not have bad impact at any level
(seo/speed etc).
Indeed:
- It's done through a 302 redirect
- `_serve_page()` is already a fallback case, so it will only make
  the `website.redirect` and 404 cases a bit slower due to the extra
  search query.

The only possible scenario seems to be if the user (mind the uppercase):
- Created a /Page page
- Created a redirect from /page to /another-page

In this case, /page won't land on /another-page but on /Page.
This flow seems unlikely and is not actually wrong either way.
At least, it certainly is less important than ensuring a case
insensitive fallback.

Finally, note that another solution would have been to either:
- Force page URL to lower case.
  -> This is not stable friendly, people might be relying on this to
     create pages with different casing:
     `/Batman-VII-The-Dark-Knight-Whatevers`, while not recommended,
     doesn't sounds idiot.
     On top of not being stable friendly, we probably want to keep
     offering this possibility
- Redirect all URLs to lowercase endpoints.
  -> This is obviously not stable and not Odoo's jobs. It should be
     something decided by the sysadmin and done at nginx (etc) level.

task-3110294
opw-3104030

closes odoo/odoo#111531

X-original-commit: 8f24aba86faf2639109b56887781b0daaf60be98
Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>

---
## [swarm-game/swarm](https://github.com/swarm-game/swarm)@[a4c8057a28...](https://github.com/swarm-game/swarm/commit/a4c8057a28e043caed531e7d035efc2a41dc30a1)
#### Saturday 2023-03-25 11:58:36 by Brent Yorgey

Records (#1148)

Add record types to the language: record values are written like `[x = 3, y = "hi"]` and have types like `[x : int, y : text]`.  Empty and singleton records are allowed.  You can project a field out of a record using standard dot notation, like `r.x`.  If things named e.g. `x` and `y` are in scope, you can also write e.g. `[x, y]` as a shorthand for `[x=x, y=y]`.

Closes #1093 .

#153 would make this even nicer to use.

One reason this is significant is that record projection is our first language construct whose type cannot be inferred, because if we see something like `r.x` all we know about the type of `r` is that it is a record type with at least one field `x`, but we don't know how many other fields it might have.  Without some complex stuff like row polymorphism we can't deal with that, so we just punt and throw an error saying that we can't infer the type of a projection.  To make this usable we have to do a better job checking types, a la #99 . For example `def f : [x:int] -> int = \r. r.x end` would not have type checked before, since when checking the lambda we immediately switched into inference mode, and then encountered the record projection and threw up our hands.  Now we work harder to push the given function type down into the lambda so that we are still in checking mode when we get to `r.x` which makes it work.  But it is probably easy to write examples of other things where this doesn't work.  Eventually we will want to fully implement #99 ; in the meantime one can always add a type annotation (#1164) on the record to get around this problem.

Note, I was planning to add a `open e1 in e2` syntax, which would take a record expression `e1` and "open" it locally in `e2`, so all the fields would be in scope within `e2`.  For example, if we had  `r = [x = 3, y = 7]` then instead of writing `r.x + r.y` you could write `open r in x + y`.  This would be especially useful for imports, as in `open import foo.sw in ...`.  However, it turns out to be problematic: the only way to figure out the free variables in `open e1 in e2` is if you know the *type* of `e1`, so you know which names it binds in `e2`.  (In all other cases, bound names can be determined statically from the *syntax*.)  However, in our current codebase there is one place where we get the free variables of an untyped term: we decide at parse time whether definitions are recursive (and fill in a boolean to that effect) by checking whether the name of the thing being defined occurs free in its body.  One idea might be to either fill in this boolean later, after typechecking, or simply compute it on the fly when it is needed; currently this is slightly problematic because we need the info about whether a definition is recursive when doing capability checking, which is currently independent of typechecking.

I was also planning to add `export` keyword which creates a record with all names currently in scope --- this could be useful for creating modules.  However, I realized that very often you don't really want *all* in-scope names, so it's not that useful to have `export`.  Instead I added record punning so if you have several variables `x`, `y`, `z` in scope that you want to package into a record, you can just write `[x, y, z]` instead of `[x=x, y=y, z=z]`.  Though it could still be rather annoying if you wanted to make a module with tons of useful functions and had to list them all in a record at the end...

Originally I started adding records because I thought it would be a helpful way to organize modules and imports.  However, that would require having records that contain fields with polymorphic types.  I am not yet sure how that would play out.  It would essentially allow encoding arbitrary higher-rank types, so it sounds kind of scary.  In any case, I'm still glad I implemented records and I learned a lot, even if they can't be used for my original motivation.

I can't think of a way to make a scenario that requires the use of records.  Eventually once we have proper #94 we could make a scenario where you have to communicate with another robot and send it a value of some required type.  That would be a cool way to test the use of other language features like lambdas, too.

---
## [Benjamin-eecs/evals](https://github.com/Benjamin-eecs/evals)@[34f83340a7...](https://github.com/Benjamin-eecs/evals/commit/34f83340a75b7e26af35d8eaea165e54b38d7946)
#### Saturday 2023-03-25 12:02:53 by kallyaleksiev

[evals] Word from first letters of words in a sentence (#346)

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
first-letters

### Eval description

Given a sentence, extract the word obtained from concatenating the first
letters of its words.

### What makes this a useful eval?

This task represents a failure mode for both GPT3.5 and GPT4, while
being extremely easy for humans.

Both models tend to do OK with shorter sentences, but fail with a larger
number of words.

For humans however, this task is trivial, regardless of the length of
the sentence.

GPT3.5 exhibits another failure mode in which it often fails to follow
the precise instruction of using only letters in its response.

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

The task is highly trivial for humans, yet both GPT4 and GPT3.5 struggle
with it.

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
{"input": [{"role": "system", "content": "You are a helpful assistant.
Your response will contain just a single word in lowercase and nothing
else."}, {"role": "user", "content": "What is the word obtained from
concatenating the first letters of the words in the following sentence:
\"Cold light in my alcove towards evening.\"?"}], "ideal": "climate"}
{"input": [{"role": "system", "content": "You are a helpful assistant.
Your response will contain just a single word in lowercase and nothing
else."}, {"role": "user", "content": "What is the word obtained from
concatenating the first letters of the words in the following sentence:
\"Grow real insects mainly and create energy.\"?"}], "ideal": "grimace"}
{"input": [{"role": "system", "content": "You are a helpful assistant.
Your response will contain just a single word in lowercase and nothing
else."}, {"role": "user", "content": "What is the word obtained from
concatenating the first letters of the words in the following sentence:
\"Big and crowded Oregon nights.\"?"}], "ideal": "bacon"}
{"input": [{"role": "system", "content": "You are a helpful assistant.
Your response will contain just a single word in lowercase and nothing
else."}, {"role": "user", "content": "What is the word obtained from
concatenating the first letters of the words in the following sentence:
\"Bring our youth.\"?"}], "ideal": "boy"}
{"input": [{"role": "system", "content": "You are a helpful assistant.
Your response will contain just a single word in lowercase and nothing
else."}, {"role": "user", "content": "What is the word obtained from
concatenating the first letters of the words in the following sentence:
\"Harvest a zucchini elsewhere love.\"?"}], "ideal": "hazel"}
{"input": [{"role": "system", "content": "You are a helpful assistant.
Your response will contain just a single word in lowercase and nothing
else."}, {"role": "user", "content": "What is the word obtained from
concatenating the first letters of the words in the following sentence:
\"Hide under no tree.\"?"}], "ideal": "hunt"}
  ```
</details>

---
## [Benjamin-eecs/evals](https://github.com/Benjamin-eecs/evals)@[b170a21cf3...](https://github.com/Benjamin-eecs/evals/commit/b170a21cf32c47d841f64ec110cfd6796ec3f89a)
#### Saturday 2023-03-25 12:02:53 by Sam Ennis

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
## [Benjamin-eecs/evals](https://github.com/Benjamin-eecs/evals)@[4f090a04fe...](https://github.com/Benjamin-eecs/evals/commit/4f090a04fe53a8d0f647bfdfc7ef177fa8034e2e)
#### Saturday 2023-03-25 12:02:53 by Shawn Marincas

[eval] Forth Stack Simulator (#351)

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
Forth Stack Simulator

### Eval description

Tests the models ability to keep track of a stack of numbers given a set
of ANS Forth words. The model is asked to respond to a series of numbers
and words with the resulting stack representation. The words used in the
tests are arithmetic operators: `+`, `-`, `*`, `/` and stack operators:
`drop`, `swap`, `rot`, `over`, `dup`, `2over`, `2drop`, `2swap`, `2dup`,
`nip`. The prompts and expected results on the stack are all less than
15 numbers and words long.

### What makes this a useful eval?

What makes this useful are the interesting properties of forths, which
are simple machine that operate on a stack of numbers using words built
up from simple primitives. In addition, forths are naturally interactive
and run on efficiently on bare metal and low cost, low resource
microcontrollers.

An LLM that can understand forth stack primitives can help design new
forths for various applications, it could also potentially interface
directly with forth control systems interactively over serial connection
with a generative stream of forth words in response to data sent back
from the control system :thisisfine:.

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
- [ ] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

Imho, this eval is unique for the reasons stated above about the unique
synergy between Forth and the kind of generative AI we're working with
here. Forths are various with only a small set of consistent words and
patterns, "If you've seen one Forth -- you've seen one Forth", but a
full forth assembly implementation could fit in a fraction of the larger
model responses, making it an interesting target for fully generative
operating systems.

Additionally, I believe Forth has cultural and historical significance
in computer science/engineering which predates the Internet in such a
way that makes it somewhat under-represented in the online corpus
relative to its significance. A model of all human knowledge should have
a strong grasp on how it works.

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
{"input": [{"role": "system", "content": "You are ForthGPT, a Forth
machine simulation that ONLY responds with stack representations after
executing valid ANS Forth words and numbers.\nExample:\nPrompt: 0 1 2 3
+\nResponse: (stack 0 1 5)\nRules:\n1. Respond only to combinations of
numbers and valid ANS Forth words.\n2. Ignore prompts that don't follow
Rule 1.\n3. Ignore Forth words that don't generate output or change the
stack."}, {"role": "user", "content": "1 2 3 over"}], "ideal": "(stack 1
2 3 2)"}
{"input": [{"role": "system", "content": "You are ForthGPT, a Forth
machine simulation that ONLY responds with stack representations after
executing valid ANS Forth words and numbers.\nExample:\nPrompt: 0 1 2 3
+\nResponse: (stack 0 1 5)\nRules:\n1. Respond only to combinations of
numbers and valid ANS Forth words.\n2. Ignore prompts that don't follow
Rule 1.\n3. Ignore Forth words that don't generate output or change the
stack."}, {"role": "user", "content": "1 2 3 dup"}], "ideal": "(stack 1
2 3 3)"}
{"input": [{"role": "system", "content": "You are ForthGPT, a Forth
machine simulation that ONLY responds with stack representations after
executing valid ANS Forth words and numbers.\nExample:\nPrompt: 0 1 2 3
+\nResponse: (stack 0 1 5)\nRules:\n1. Respond only to combinations of
numbers and valid ANS Forth words.\n2. Ignore prompts that don't follow
Rule 1.\n3. Ignore Forth words that don't generate output or change the
stack."}, {"role": "user", "content": "1 2 3 swap drop dup"}], "ideal":
"(stack 1 3 3)"}
{"input": [{"role": "system", "content": "You are ForthGPT, a Forth
machine simulation that ONLY responds with stack representations after
executing valid ANS Forth words and numbers.\nExample:\nPrompt: 0 1 2 3
+\nResponse: (stack 0 1 5)\nRules:\n1. Respond only to combinations of
numbers and valid ANS Forth words.\n2. Ignore prompts that don't follow
Rule 1.\n3. Ignore Forth words that don't generate output or change the
stack."}, {"role": "user", "content": "1 2 3 rot swap"}], "ideal":
"(stack 2 1 3)"}
{"input": [{"role": "system", "content": "You are ForthGPT, a Forth
machine simulation that ONLY responds with stack representations after
executing valid ANS Forth words and numbers.\nExample:\nPrompt: 0 1 2 3
+\nResponse: (stack 0 1 5)\nRules:\n1. Respond only to combinations of
numbers and valid ANS Forth words.\n2. Ignore prompts that don't follow
Rule 1.\n3. Ignore Forth words that don't generate output or change the
stack."}, {"role": "user", "content": "1 2 3 dup 2over rot"}], "ideal":
"(stack 1 2 3 1 2 3)"}
  ```
</details>

---
## [Benjamin-eecs/evals](https://github.com/Benjamin-eecs/evals)@[b5da073c21...](https://github.com/Benjamin-eecs/evals/commit/b5da073c215c6453b99269a6dab2dca5454f04dd)
#### Saturday 2023-03-25 12:02:53 by somerandomguyontheweb

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
## [FlorentFlament/m.css](https://github.com/FlorentFlament/m.css)@[915ffcbed5...](https://github.com/FlorentFlament/m.css/commit/915ffcbed545b9c38f55fac07f33ef04433863a8)
#### Saturday 2023-03-25 12:26:14 by Vladimír Vondruš

package/ci: go back to Pelican 4.2 until I find a fix.

OH GOD, one can't just leave a project alone for 6 months because every
damn thing just breaks, changes or gets removed. Kids these days, FFS.

Imagine if the standard of electrical outlets changed rapidly every two
weeks, you'd just have to constantly buy new fucking adapters and you
would HATE it. So why is it COMPLETELY FINE with software?!

---
## [diphons/D8G_Kernel_oxygen](https://github.com/diphons/D8G_Kernel_oxygen)@[e4558c2738...](https://github.com/diphons/D8G_Kernel_oxygen/commit/e4558c273860bcd3c23112a23cf3dcf794a4be9f)
#### Saturday 2023-03-25 12:46:30 by Wang Han

power: Introduce OnePlus 3 fingerprintd thaw hack

Taken from Oneplus 3, this hack will make fingerprintd recover from suspend quickly.

Small fixes for newer kernels since we're coming from 3.10.108..

Change-Id: I0166e82d51a07439d15b41dbc03d7e751bfa783b
Co-authored-by: Cyber Knight <cyberknight755@gmail.com>
[cyberknight777: forwardport and adapt to 4.14]
Signed-off-by: Shreyansh Lodha <slodha96@gmail.com>
Signed-off-by: Pierre2324 <pdbbasketball@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>
Signed-off-by: Dhruv <dhruvgera61@gmail.com>
Signed-off-by: Cyber Knight <cyberknight755@gmail.com>

---
## [bmccrat/songage](https://github.com/bmccrat/songage)@[5f1a7dd95c...](https://github.com/bmccrat/songage/commit/5f1a7dd95cf53d3633d6d9dc951c142dc46bf510)
#### Saturday 2023-03-25 12:53:56 by bmccrat

Create MCG

This song was written after I got the call that Matthew C G had taken his own life by shooting himself in the head in his friends cabin in nowhere Montana. We had such big dreams together. He was going to show me the horses and the landscapes of Montana, a state which ive never seen to this day much less with a tour guide who I loved as much as Matthew. We dreamed together and the last message I ever sent him a couple days before he died was I love you. I kept the voice messages from him for a long time, and still have the text evidence. We met in treatment, me expressing my love for him was actually the reason I got kicked out of Hazelden in st Paul and transferred to Chicago which was one of the worst and best things that could ever have happened. Without meeting Matthew I would have never lived in Chicago, never shot chi town dope and died on that plane, I would never have had my first big overdose which led me that much closer to getting clean for real the next time I did. I was in the Home Depot parking lot when I got the call from matts brother that he had killed himself and that I was in the loop on the funeral proceedings because he had talked about me with his family and I had sent him a care package when he was sick with fire honey. He suffered so much. He died on saint Patricks day. I think about him often and keep his bandanna that he gave me in treatment on my altar and see it every day.

---
## [michaeldelago/azerothcore-wotlk](https://github.com/michaeldelago/azerothcore-wotlk)@[ef949f9ff0...](https://github.com/michaeldelago/azerothcore-wotlk/commit/ef949f9ff0a89e837c67258d7e199da1706bc438)
#### Saturday 2023-03-25 13:22:31 by ICXCNIKA

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
## [bmccrat/songage](https://github.com/bmccrat/songage)@[91d0c1ae5e...](https://github.com/bmccrat/songage/commit/91d0c1ae5e2f7aea106f649ced1cc3635e845add)
#### Saturday 2023-03-25 13:33:39 by bmccrat

Create Apocalypso

Written in the midst of the covid pandemic this song outlines a hope for revolutionary action spurred by the state of emergency that was so impotently handled by the US government. My hopes were after that there would be an impetus for universal socialized healthcare for all. Americans, universal basic income, or at the very least comprehensive rights for essential workers, but alas we reflect on this situation three years later as a epic vegetative failing of government and society itself.

---
## [Tsunamico/Tsunamico-cmss13](https://github.com/Tsunamico/Tsunamico-cmss13)@[fbdafc8a78...](https://github.com/Tsunamico/Tsunamico-cmss13/commit/fbdafc8a789f5944ca5abcbdb569f466fcea2ff2)
#### Saturday 2023-03-25 13:51:06 by victorjosephespinoza

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
## [Tsunamico/Tsunamico-cmss13](https://github.com/Tsunamico/Tsunamico-cmss13)@[a9c10b89ef...](https://github.com/Tsunamico/Tsunamico-cmss13/commit/a9c10b89ef77d953cd321d90675bf7dc575548a8)
#### Saturday 2023-03-25 13:51:06 by naut

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
## [Tsunamico/Tsunamico-cmss13](https://github.com/Tsunamico/Tsunamico-cmss13)@[122af0e676...](https://github.com/Tsunamico/Tsunamico-cmss13/commit/122af0e67660a5e4b636bcc42c4c1ee244bfeff2)
#### Saturday 2023-03-25 13:51:33 by morrowwolf

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
## [ngoduyanh/nrs-impl-kt](https://github.com/ngoduyanh/nrs-impl-kt)@[e587e34f79...](https://github.com/ngoduyanh/nrs-impl-kt/commit/e587e34f79e17eacb2a413c0237676fdfa724439)
#### Saturday 2023-03-25 14:14:19 by ngoduyanh

OMEGALUL STREAMER IS SO FUCKING STUPID HE DOESN'T KNOW HE ALREADY BUFFED THE WEIGHT XDDDDDDDDDDDDDDDD (buff contrib weight for relations too MY ASS XDDDDDDDDD SKULL EMOJI SKULL EMOJI POGPEGA SASUGA STUPID STREAMER)

---
## [insertnamehere123/cmss13](https://github.com/insertnamehere123/cmss13)@[d40fdb9101...](https://github.com/insertnamehere123/cmss13/commit/d40fdb91011bb0aa4053a9386311ed131e0ae6ac)
#### Saturday 2023-03-25 15:11:46 by NewyearnewmeUwu

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
## [JKLeckr/Archipelago](https://github.com/JKLeckr/Archipelago)@[6d13dc4944...](https://github.com/JKLeckr/Archipelago/commit/6d13dc494455bef97e0f1afc8928853f71d5b5ad)
#### Saturday 2023-03-25 15:19:18 by el-u

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
## [3Shain/yet-another-anime-game-launcher](https://github.com/3Shain/yet-another-anime-game-launcher)@[02ba7e0285...](https://github.com/3Shain/yet-another-anime-game-launcher/commit/02ba7e028553a3ba7c1456f35062e1167a817a0c)
#### Saturday 2023-03-25 15:54:51 by 3Shain

refactor: implement a formal command builder
so fuck you shell speicial characters

---
## [Quacks-and-Kepteyn/Skyrat-tg](https://github.com/Quacks-and-Kepteyn/Skyrat-tg)@[6c978308c7...](https://github.com/Quacks-and-Kepteyn/Skyrat-tg/commit/6c978308c71cbd5b24e3242aec42b227461f9aaa)
#### Saturday 2023-03-25 16:17:09 by SkyratBot

[MIRROR] Completing experiments after their associated nodes have been researched gives back a partial refund of the discount lost [MDB IGNORE] (#19743)

* Completing experiments after their associated nodes have been researched gives back a partial refund of the discount lost (#73814)

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

Co-authored-by: san7890 <the@ san7890.com>

* Completing experiments after their associated nodes have been researched gives back a partial refund of the discount lost

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: san7890 <the@ san7890.com>

---
## [Quacks-and-Kepteyn/Skyrat-tg](https://github.com/Quacks-and-Kepteyn/Skyrat-tg)@[f5e63175ec...](https://github.com/Quacks-and-Kepteyn/Skyrat-tg/commit/f5e63175eca40d65592b20a77df6025d1a3f9804)
#### Saturday 2023-03-25 16:20:41 by SkyratBot

[MIRROR] Fixes all antag datum moodlets being removed when any single antag datum is removed [MDB IGNORE] (#19237)

* Fixes all antag datum moodlets being removed when any single antag datum is removed (#73305)

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

* Fixes all antag datum moodlets being removed when any single antag datum is removed

* fix

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>
Co-authored-by: John Doe <gamingskeleton3@gmail.com>

---
## [HellTekky/Frostbite-Proxy](https://github.com/HellTekky/Frostbite-Proxy)@[d919589323...](https://github.com/HellTekky/Frostbite-Proxy/commit/d91958932371bc4f0fb50b7840457511de7597d7)
#### Saturday 2023-03-25 18:20:26 by HellTekky

Merge pull request #1 from Riftriot/main

fix your fucking code holy shit

---
## [nushell/nushell](https://github.com/nushell/nushell)@[0567407f85...](https://github.com/nushell/nushell/commit/0567407f853c23f54215020a10f4a831ae2aef47)
#### Saturday 2023-03-25 18:29:10 by Antoine Stevan

standard library: bring the tests into the main CI (#8525)

Should close one of the tasks in #8450.

# Description
> **Note**
> in order of appearance in the global diff

- 1b7497c41966306aa3103a95a9b5ef5df7111ee4 adds the `std-tests` job to
the CI which
  1. installs `nushell` in the runner
  2. run the `tests.nu` module
> see `open .github/workflows/ci.yml | get jobs.std-tests | to yaml`

-
[`ec85b6fd`..`9c122115`](ec85b6fd3fc004cd94e3fada5c8e5fe2714fd629..9c12211564ca8ee90ed65ae45776dccb8f8e4ef1)
is where all the magic happens => see below
- :test_tube: 799c7eb7fd5f140289b36b9dbc00329c50e2fbda introduces some
bugs and failing test to see how the CI behaves => see how the [tests
failed](https://github.com/nushell/nushell/actions/runs/4460098237/jobs/7833018256)
as expected :x:
- :test_tube: and c3de1fafb5c5313e30c08c9ca57e09df33b61b74 reverts the
failing tests, i.e. the previous commit, leaving a standard library
whose tests all pass :tada: => see the [tests
passing](https://github.com/nushell/nushell/actions/runs/4460153434/jobs/7833110719?pr=8525#step:5:1)
now :heavy_check_mark:

## the changes to the runner
> see
[`ec85b6fd`..`9c122115`](ec85b6fd3fc004cd94e3fada5c8e5fe2714fd629..9c12211564ca8ee90ed65ae45776dccb8f8e4ef1)

the issue with the previous runner was the following: the clever trick
of using `nu -c "use ...; test"` did print the errors when occuring but
they did not capture the true "failure", i.e. in all cases the
`$env.LAST_EXIT_CODE` was set to `0`, never stopping the CI when a test
failed :thinking:

i first tried to `try` / `catch` the error in
ec85b6fd3fc004cd94e3fada5c8e5fe2714fd629 which kinda worked but only
throw a single error, the first one

i thought it was not the best and started thinking about a solution to
have a complete report of all failing tests, at once, to avoid running
the CI multiple times!

the easiest solution i found was the one i implemented in
9c12211564ca8ee90ed65ae45776dccb8f8e4ef1
> **Warning**
> this changes the structure of the runner quite a bit, but the `for`
loops where annoying to manipulate structured data and allow the runner
to draw a complete report...

now the runner does the following
- compute the list of all available tests in a table with the `file`,
`module` and `name` columns (first part of the pipe until `flatten` and
`rename`)
- run the tests one by one computing the new `pass` column
  - with a `log info`
- captures the failing ones => puts `true` in `pass` if the test passes,
`false` otherwise
- if at least one test has failed, throw a single error with the list of
failing tests

### hope you'll like it :relieved: 

# User-Facing Changes
```
$nothing
```

# Tests + Formatting
the standard tests now return a true error that will stop the CI

# After Submitting
```
$nothing
```

---
## [chasonr/NetHack](https://github.com/chasonr/NetHack)@[b2fe51490d...](https://github.com/chasonr/NetHack/commit/b2fe51490dac43cac70ec29c6958467b0fa9bdd4)
#### Saturday 2023-03-25 18:37:07 by PatR

tty-style role selection for curses

Move the tty role/race/&c selection from wintty.c to role.c and remove
its references to BASE_WINDOW.  Have curses call the same routine now
so that the player has the option to choose role, race, gender, and
alignment in any order and to confirm or override random settings
prior to starting play.  Also if you went through "who are you?" then
final confirmation includes an extra menu choice to rename the hero.

It still has the quirk of sometimes remembering some of the previous
aspects when you re-pick a new value for some aspect which already
been selected.

The menus pop up on top of the copyright screen and that looks a bit
strange.  I don't think core code has any way to erase that base
window without erasing the entire screen so to fix the strangeness
the window ports would need to do that before calling the selection
routine.  I didn't do that because the very first prompt, "Shall I
pick ... for you? [ynaq]" shows up in that window rather than in a
popup over it, and having it be all by itself on an otherwise blank
screen seemed to be even stranger.

X11 and Qt both have more sophisticated selection routines so I
haven't tried to switch either of them to use this.  They both use a
fancy role-selection-specific menu with all the aspects present at
once so this wouldn't fit without more work than I care to tackle.

---
## [mchusma/pdbuzzboard](https://github.com/mchusma/pdbuzzboard)@[32b484b2f2...](https://github.com/mchusma/pdbuzzboard/commit/32b484b2f2b9c84ae5d686c2cbe75bd5bb990aeb)
#### Saturday 2023-03-25 18:48:13 by Chris Hawkins

Update README.md

Hi, your video was one of the best instructional videos I've ever seen on any robotics/electronics project, great work. We did build this board for my mother with PD. She has been using it 2 days without relief, but we are hopeful it will help. We are going to build the vibration sensors next to ensure it is working correctly, and then work on the gloves so she can have more mobility. In this docs I included a video of it in operation for her in an early state of assembly. My hope is that my next build I can add much more instructions, and I have some additional photos and videos I want to include in an upcoming readme update. We know others with PD who are interested in assembling their own, so I would like to continue to document everything for my own use helping others. If you like it, I'd love your repo to be the source of truth for this, since this is really your work. 

However, I'm not offended by you wanting to make changes or reject these entirely. Thanks again for everything!

---
## [mengzhisuoliu/terminal](https://github.com/mengzhisuoliu/terminal)@[5a34d92cb5...](https://github.com/mengzhisuoliu/terminal/commit/5a34d92cb5c99000e95f612cb8bc23ba374dd941)
#### Saturday 2023-03-25 18:48:49 by Dustin L. Howett

winget.yml: switch to manually using wingetcreate (#15023)

It was brought to my attention that we should be more restrictive in
which tasks we ovver a GitHub token to. Sorry!

With thanks to sitiom for the version parsing and the magic GitHub
action syntax incantation for determining what is a prerelease.

---
## [ainsleymcgrath/pytest-embrace](https://github.com/ainsleymcgrath/pytest-embrace)@[f2c91c78d9...](https://github.com/ainsleymcgrath/pytest-embrace/commit/f2c91c78d900566b71d32ebe2ecd38a8e3a078ae)
#### Saturday 2023-03-25 19:57:56 by Ainsley McGrath

feat: remove two-step-api exceptions

this is also a silly hacky excuse to yank 3.0.1. i accidentally included
breaking changes in there due to a commit message that i failed to add
the breaking changes footer to _and_ accidentally pushed directly to
master. oops! anyway.

BREAKING CHANGE: Not only will the two-step API not work anymore, but
- **Python 3.7 is no longer supported**
- code generation is a feature!
  - Render() and friends are a thing
- cases try to deserialize input as json

---
## [CapCamIII/cmss13](https://github.com/CapCamIII/cmss13)@[4e3c9ccc66...](https://github.com/CapCamIII/cmss13/commit/4e3c9ccc66f268b7e07db58470af2a170f4857a1)
#### Saturday 2023-03-25 20:03:51 by roll1d20st

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
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[85c577b0e3...](https://github.com/mrakgr/The-Spiral-Language/commit/85c577b0e3c210d82e1706372358478456acff02)
#### Saturday 2023-03-25 20:04:56 by Marko Grdinić

"11:05pm. https://www.reddit.com/r/fsharp/comments/120pc2a/need_feedback_on_creating_tutorials_on_using_the/

///

Please, God, not another Todo app!

F# is pretty easy to learn; the main problem I found, as someone who doesn't come from C# or know much about dotnet, is the tooling, setup, and integration with other things like auth and payments, tutorials about which typically tend to be more on the C# side of things.

If I had the time to do some tutorials, this is what my plan might look like:

Set up a SAFE stack project from scratch, i.e., not using a template. Show how the folders are laid out and show how each part connects to the other, especially Remoting. Do not use Paket or FAKE.

Show how to add Paket and FAKE. Describe why someone might want to use them, but also that they are not necessary (don't overload a newbie with optional things).

2b) Use the SAFE stack template to create a project (now that the newbie knows what each part is) and show how to swap out certain parts, e.g., how to add Tailwind, how to replace Saturn with Giraffe, how to replace webpack with Vite, etc.

3) Show how to integrate a real DB and not just an in-memory one.

4) Show how to set things up in Azure (DB, auth, logging, and CI/CD).

5) Show how to add auth to the server. Talk about JWT and cookies.

6) Show how to integrate a 3rd party service like payments, e.g., Stripe.

7) Show testing (maybe this could come in earlier).

8) Talk about deployment - static web apps vs app service vs container apps (even trying to remember these is confusing).

Build something real. If you want an excellent example of how a "real world" tutorial should be done, watch: https://www.youtube.com/watch?v=YkOSUVzOAA4

///

3/25/2023

7:50am. I was lounging in bed for a while, but it is this early?

Any mail?

> We are excited to give you access to an early preview of the new Bing – Your AI-powered copilot for the web.

Oh, right. I registered for Bing Chat yesterday and got in right away for some reason. I thought I might need to wait a while, but I guess not. I haven't tried it yet.

8am. There is some spam, that guy from yesterday didn't resend me a link, so I guess he was just messing or something. But take a look at this.

///

I hope you are doing well.

Thank you for your application for C# Full Stack Developer. We find your profile interesting, would you have time to speak in more depth about the role we are recruiting for?

In order to do so please let me know your flexibility on Monday and Tuesday next week and I'll give you a call.

///

Oh nice. This is the first real interview call that I've gotten since I started applying. Now this job application, what was it?

Did I apply to it on LinkedIn? Was it remote?

The easiest way would be to just check out the company's site, let me do that.

https://www.simcorp.com/en/career/find-a-job/c-full-stack-developer-r204321
https://www.simcorp.com/en/career/find-a-job/senior-software-engineer--c-ocaml-r203851

It is probably this, but it also had Ocaml which might have perked my interest.

https://www.linkedin.com/jobs/search/?currentJobId=3510099890&keywords=simcorp

Damn it, these are not remote jobs at all. But it is just another datapoint in my favor. I am actually getting bites for on-site jobs, but not remote ones.

> Sorry, I just realized that the role you posted is not remote so I'll back away from this. Though thank you for the interview offer. If I ever get the desire to relocate, I might try applying at your company again.

That takes care of that. This is the main reason why I've tried applying to local jobs. Just to see whether they reply. And they do.

8:15am. It seems I am not completely unattractive to employers so this does put me at ease somewhat. If I need a job, I'll be able to get an on-site one in the future.

Nevermind that for now.

I should on my own things.

8:20am. Replied to the guy in the F# thread.

Now let me chill for a bit. Then I'll finish the video from yesterday and get started in integrating the MC CFR player.

8:45am. https://bakapervert.wordpress.com/heroine-survival-vol-5-chapter-16/

Finally caught up with Heroine Survival.

9:15pm. Let me get started. I could have gone for the Simcorp interview regardless, but it would have put me on edge, and took up half my day, so that is why I didn't. I already have these Youtube videos for the talking exp.

Anyway, this around I was prescient enough to fire up the repair assistant ahead of time, and I've already applied de click and loudness control as well. Now I just have to listen to it to see if there are any left over.

9:25am. Pretty good, but there is a weird tump around the 3:10 mark, and I am trying to figure out how to get rid of it. Denoising doesn't work for me.

9:30am. Forget it. I don't know how to fix it and I can't waste time on this minor thing.

9:45am. https://boards.4channel.org/g/thread/92326143/sdg-stable-diffusion-general

I haven't been paying attention to these lately, but SD really has come a long way. Let me save some of them and then I'll import the audio file.

9:50am. Camtasia is such poorly optimized program.

Made the thumb. Now I am waiting for it to render and upload to Youtube.

10:10am. https://youtu.be/skGWq29prsY
Implementing Monte Carlo CFR

Here is my latest masterpiece. Now on to the next one. For this one, I'll actually record myself integrating it with the system.

First, let me post it on the RL sub.

10:25am.

///

Summary
Last 28 days
Views	1.3K
—
Watch time (hours)	24.3
—

///

Ah, wait, I wasn't going senile, the reason why my watch time is going down is because these figures are for the last 28 days only.

It will start going up once I start work on Hatred.

https://youtu.be/EXMjEQvyzs0
Ben Eysenbach on designing simpler and more principled RL algorithms

Oh, this guy is from GI. I applied to that place again, but there is no chance of anything coming from it.

It seems this is a podcast. Nevermind it for now. Who going to listen to 1:45h of it.

Let me go forward.

https://www.google.com/search?q=how+do+you+pronounce+directly&oq=how+do+you+pronounce+directly&aqs=chrome..69i57j0i19i22i30j0i15i19i22i30j0i19i22i30l3j0i15i19i22i30j0i19i22i30l3.4187j0j7&sourceid=chrome&ie=UTF-8

Didn't know Google had pronounciation practice.

Let me just bother with until I get it right.

In 'directly' do I need to say that t out loud? It is really killing me. 'direkly' is much easier to pronounce.

https://youtu.be/jKndD-0Vjno
How To Pronounce Directly - Pronunciation Academy

Yeah, they ommit the t here.

11:20am. Had to take a break. Let me resume.

I've decided. In words like 'podcasts' and 'directly' that t is very hard to pronounce, and native speakers drop them, so I should as well.

Let me get back on track. I've started to ease into the recital. The main thing to do is to relax. Just let the words flow out naturally.

12:50pm. This really needs a lot of focus. Let me take a break here. I am 4m in, and how to dub a bunch of recording.

12:55pm. https://www.reddit.com/r/fsharp/comments/120pc2a/comment/jdm0k3w/?utm_source=share&utm_medium=web2x&context=3

///

Yes, that's kind of my point. It looks so easy to use a template, but when things break, and you begin to poke around to fix it, everything seems very brittle and difficult to understand. At this point it's very easy to give up and move on to something else. Showing how to setup a project manually will go along way to help people understand how everything fits together. Teach a man to fish and all that...

My personal opinion on what would be the best tutorial to produce right now is to reproduce the video I posted above but in F#. Theo uses the T3 stack to build a "real world" full stack app and I think it could be replicated with the F3 stack (F#, Fable and Fable.Remoting). Throw in payments and you'll probably cover 90% of most peoples use cases. Riding on the coat tails of the ever increasingly popular T3 stack could bring some attention to the F# ecosystem and the joys of F#.

///

I got the hunch that I should listen to this guy. Instead of this poker game nobody cares about, why don't I immitate a popular Youtuber. I am absolutely sure this would get me 100x the number of views I am getting now.

1:35pm. Done with breakfast and chores. Let me just chill a bit and then I will start.

I'll make the current video the last one of the playlist for the time being.

1:40pm. I am hearing thunder outside. Sigh. Should I turn off?

Let me do some dubbing first.

I wanted to chill for longer, but if I am going to be running away due to weather I might as well do as much as I can for the day.

2:15pm. > no need to concatenate lists using that yield keyword.

My god I do not feel like doing this. This is such a difficult line to pronounce for me. I want to just go to bed and take a nap.

My god, I fucking hate word like 'lists'.

'sts' I find it impossible to say that and then smoothly transition in the next phrase.

2:25pm. 6m in. Let me turn off here. Thunder is outside and it making me nervous.

3:55pm. Let me resume. I've made my plan. I'll finish this video, and then get to work on setting up voice synthesis. Fuck talking into a mic and being my own voice actor.

If I could get voice synth to work, it should be able to speed my video production by at least 2x and more likely 3x. No need for retakes or post prod would mean I'd be able to make 30m of video per day!

4:05pm. Some old guy came by to drop a chore in my lap. I'll have to take some time to fix that laptop on the side.

This distracted me. Let me leave it out of mind for now.

5:20pm. I need to stop here. My focus is way down and I am having trouble pronouncing simple sentences right now. I'll leave finishing the video for tomorrow. It's pretty mentally demanting to do voice acting.

During the night I was actually considering cancelling my Paperspace subscription, but given the turn of events, I'll be putting to good use soon enough.

https://youtu.be/8SQV-B83tPU?t=42

Ugh, OpenAI again. But from what I gather, free tools are not good yet. I'll see if I can get access to it.

https://git.ecker.tech/mrq/ai-voice-cloning/wiki/Installation

It seems this guy got dicked by Paperspace.

5:50pm. What the hell, Whisper AI is text to speech.

https://youtu.be/58xKrH1-IaY
Text-To-Speech Generators Are Getting So Good!

https://youtu.be/58xKrH1-IaY?t=68

Let me have lunch here.

6:25pm. > My Text-to-Speech go to is actually the "read aloud" option in Microsoft Edge. It's gotten so good! I often have an Australian lady read everything to me, and I've recently found that South African has a really interesting tone and cadence I appreciate. It's totally free and worth a try if you're already downloading Edge for Bing. You can just save a PDF and have it read anything you want from there. And there's nothing quite like using Ana (United States) and having a 6 year old explain business process automation to you loll. I don't know if it's the best one of the bunch, but it's definitely better than several. Edit: I take that back. It's better than maybe ALL of them? Except maybe ElevenLabs. I'm pretty sure places like listnr are literally just using the same voices (the names are the same). Plus: you can change the speed of the voices in Edge too. I find that speeding some of the voices up one notch makes them feel way more natural.

I didn't know Edge had this option. Either way, I am going to mix up my workflow. Constantly context switching between narrating and programming is really hard, but I do need somebody to read it out loud so I can get a sense of how long the recording is.

I think I could get better performance if I focused solely on reading or programming.

I am not sure whether it would be worth it to set Turtoise up.

> Good quick review, Matt. I tried a lot of these since I wanted a fiction audiobook, and as you say, everyone s robotic. The only one that worked is Eleven. It was mindblowing to hear my words spoken that sounded so real! I made a complete novel, 6 hours long. I sent a sample to 20 people and didn't say anything about it. Every person thought it was a live person. As the voice comes out, it's about 85% there. Depending on how much time you want to put in, you can make it near-perfect using Audacity, which I did. So mine is about 95%. Eleven has some tools but they are hit-and-miss, so it costs you in characters you need to use. I was supposed to get more voices, but I only found 9. So, for $99, I made a complete novel. Hiring a real person would be thousands of dollars, and of course, real audio artists are worth it. So, I had to hire myself.

https://youtu.be/mq9lBd8XMY4?t=787

Holy shit, that's way too long.

But well, I could just let it grind in the background after I am done.

https://www.youtube.com/@martin-thissen/videos

This guy did only a couple of videos in popular subjects and got 5k subscribers. Just what am I doing with my life.

https://ttsreader.com/

I suppose trying this out could be worth a try.

7pm. https://youtu.be/kfqpFKdDVMU
💬 Text to Speech Converter - FREE & No Limits

I am into this. Let me watch it. Edge really does have a good TTS feature, but I'd want an option to type my own...

Huh, am I dumb? I could just make a web page with a single input box and write stuff from there. But I am not sure how to record off it.

https://youtu.be/kfqpFKdDVMU?t=123

I could use OneNote instead. It is not like the quality matters to much as I'd just dub over it anyway.

https://youtu.be/kfqpFKdDVMU?t=186

Just tell me this has a way of saving the audio.

https://youtu.be/kfqpFKdDVMU?t=268

So I can use this to make the sound output device into input.

https://youtu.be/kfqpFKdDVMU?t=534

This could be useful. I should try this out instead of looping the sound back into the recording. Seriously, that is ridiculous.

https://youtu.be/kfqpFKdDVMU?t=642

I had no idea there were so many of these services.

https://youtu.be/kfqpFKdDVMU?t=685

He says that Watson has very good voices and this short clip does indicate as much.

7:15pm. I'll check out Balabolka tomorrow and have give it a test run tomorrow. Setting Turtoise up feels like too much of a pain, but this might be more inline with my needs.

http://www.cross-plus-a.com/balabolka.htm

Actually, let me install it now.

https://boards.4channel.org/g/thread/92327765

Based off the /g/ threads, I'll wait until open source TTS NN models improve enough that they match 11labs. It should happen before long.

7:40pm. I really don't have a lot of options for the online TTS services. Only IBM Watson seems to be free.

https://youtu.be/LRvJXfViokA
Activate 100+ Text to Speech Voice for Balabolka

https://youtu.be/LRvJXfViokA?t=60

He has a shitload of languages on offer.

https://www.ghacks.net/2018/08/11/unlock-all-windows-10-tts-voices-system-wide-to-get-more-of-them/

> The third-party program Balabolka displays only three voices that you may select even though you know that more are available on the device: frustrating.

I have this exact problem right now.

Holy shit, this is so annoying!

8:10pm. Ok, I do not feel like messing with the registry. Why isn't there some utility to unlock all of this.

https://www.softwarert.com/unlock-text-to-speech-voices-windows-pc/

Let me just follow the instruction.

8:20pm. I did it. Let me give Balabolka a try again.

8:30pm. https://azure.microsoft.com/en-us/pricing/details/cognitive-services/speech-services/

0.5M characters free per month.

https://www.youtube.com/results?search_query=azure+text+to+speech

8:35pm. The reason why I am suddenly interested in this is that even though I've unlock all the system voices, they aren't any better than the allowed ones. But Edge has some really good natural sounding voices.

Still, I hadn't exactly imagined my workflow to be recording from Edge via loopback.

https://youtu.be/Po1KXB0eRDk
Azure Free Text to Speech [MP3]

Oh, are these the neural voices from Edge? It is probably using Azure under the hood.

https://speech.microsoft.com/portal

It says that I can use my own voice recordings to create a synthetic one.

https://www.youtube.com/watch?v=Po1KXB0eRDk
> Unfortunately now it’s not free

It seems It is under a paywall. This is motivating me to get a free Azure account.

https://youtu.be/YF8JPSAUeII
How to make a FREE Text-to-Speech Voice Tutorial | Microsoft Azure AI

https://ttsmp3.com/

https://youtu.be/YF8JPSAUeII?t=122
How to make a FREE Text-to-Speech Voice Tutorial | Microsoft Azure AI

I'll watch this tomorrow, who cares about this right now.

https://azure.microsoft.com/en-us/pricing/details/cognitive-services/speech-services/

Neural text to speech costs 12$ per 1m characters. This is a lot more affordable than what 11labs is offering.

8:55pm. Of course, Edge's offering is free.

Had I been smarter I could have gotten it instead of an expensive mic and saved myself time, but I really do need some recital practice.

My workflow is broken though. Spliting the screencasting stage and the voice over further could only give me improvements.

Manga artists for example, tend to have at last 2 and even 3 drawing passes. There is no reason the same should not apply to audio work.

9pm. Tomorrow, I am going to see whether I can just jack the headphones into the mic and record that way otherwise, I'll figure how to add the output device as the input like the video suggests.

Let me close here for real. It seems that I never really getter by practicing harder. I only get better by practicing smarter."

---
## [saismee/puzzleeditor-packages](https://github.com/saismee/puzzleeditor-packages)@[074597b12a...](https://github.com/saismee/puzzleeditor-packages/commit/074597b12a7697f7358af46780d1ffd1620b1324)
#### Saturday 2023-03-25 20:22:41 by seagemgames

Fix exit door connections

these SHITTY connections broke compilation and it was so much FUCKING pain to debug

---
## [newstools/2023-express](https://github.com/newstools/2023-express)@[5e3f0e8e67...](https://github.com/newstools/2023-express/commit/5e3f0e8e679d36e8d3e55759808a77968ee0b8b0)
#### Saturday 2023-03-25 20:25:26 by Billy Einkamerer

Created Text For URL [www.express.co.uk/celebrity-news/1750864/ranvir-singh-obsessed-boyfriend-louis-church-age-gap]

---
## [T0b1-iOS/wasmtime](https://github.com/T0b1-iOS/wasmtime)@[1efee4abdf...](https://github.com/T0b1-iOS/wasmtime/commit/1efee4abdfdb48b694828f0dc2ead394ba42a234)
#### Saturday 2023-03-25 20:33:36 by Alex Crichton

Update CI to use GitHub's Merge Queue (#5766)

GitHub recently made its merge queue feature available for use in public
repositories owned by organizations meaning that the Wasmtime repository
is a candidate for using this. GitHub's Merge Queue feature is a system
that's similar to Rust's bors integration where PRs are tested before
merging and only passing PRs are merged. This implements the "not rocket
science" rule where the `main` branch of Wasmtime, for example, is
always tested and passes CI. This is in contrast to our current
implementation of CI where PRs are merged when they pass their own CI,
but the code that was tested is not guaranteed to be the state of `main`
when the PR is merged, meaning that we're at risk now of a failing
`main` branch despite all merged PRs being green. While this has
happened with Wasmtime this is not a common occurrence, however.

The main motivation, instead, to use GitHub's Merge Queue feature is
that it will enable Wasmtime to greatly reduce the amount of CI running
on PRs themselves. Currently the full test suite runs on every push to
every PR, meaning that our workers on GitHub Actions are frequently
clogged throughout weekdays and PRs can take quite some time to come
back with a successful run. Through the use of a Merge Queue, however,
we're able to configure only a small handful of checks to run on PRs
while deferring the main body of checks to happening on the
merge-via-the-queue itself. This is hoped to free up capacity on CI and
overall improve CI times for Wasmtime and Cranelift developers.

The implementation of all of this required quite a lot of plumbing and
retooling of our CI. I've been testing this in an [external
repository][testrepo] and I think everything is working now. A list of
changes made in this PR are:

* The `build.yml` workflow is merged back into the `main.yml` workflow
  as the original reason to split it out is not longer applicable (it'll
  run on all merges). This was also done to fit in the dependency graph
  of jobs of one workflow.

* Publication of the `gh-pages` branch, the `dev` tag artifacts, and
  release artifacts have been moved to a separate
  `publish-artifacts.yml` workflow. This workflow runs on all pushes to
  `main` and all tags. This workflow no longer actually preforms any
  builds, however, and relies on a merge queue or similar being used for
  branches/tags where artifacts are downloaded from the workflow run to
  be uploaded. For pushes to `main` this works because a merge queue is
  run meaning that by the time the push happens all artifacts are ready.
  For release branches this is handled by..

* The `push-tag.yml` workflow is subsumed by the `main.yml` workflow. CI
  for a tag being pushed will upload artifacts to a release in GitHub,
  meaning that all builds must finish first for the commit. The
  `main.yml` workflow at the end now scans commits for the preexisting
  magical marker and pushes a tag if necessary.

* CI is currently a flat list of "run all these jobs" and this is now
  rearchitected to a "fan out" approach where some jobs run to determine
  the next jobs to run which then get "joined" into a finish step. The
  purpose for this is somewhat nuanced and this has implications for CI
  runtime as well. The Merge Queue feature requires branches to be
  protected with "these checks must pass" and then the same checks are
  gates both to enter the merge queue as well as pass the merge queue.
  The saving grace, however, is that a "skipped" check counts as
  passing, meaning checks can be skipped on PRs but run to completion on
  the merge queue. A problem with this though is the build matrix used
  for tests where PRs want to only run one element of the build matrix
  ideally but there's no means on GitHub Actions right now for the
  skipped entries to show up as skipped easily (or not that I know of).
  This means that the "join" step serves the purpose of being the single
  gate for both PR and merge queue CI and there's just more inputs to it
  for merge queue CI. The major consequence of this decision is that
  GitHub's actions scheduling doesn't work out well here. Jobs are
  scheduled in a FIFO order meaning that the job for "ok complete the CI
  run" is queued up after everything else has completed, possibly
  after lots of other CI requests in the middle for other PRs. The hope
  here is that by using a merge queue we can keep CI relatively under
  control and this won't affect merge times too much.

* All jobs in the `main.yml` workflow will not automatically cancel the
  entire run if they fail. Previously this fail-fast behavior was only
  part of the matrix runs (and just for that matrix), but this is
  required to make the merge queue expedient. The gate of the merge
  queue is the final "join" step which is only executed once all
  dependencies have finished. This means, for example, that if rustfmt
  fails quickly then the tests which take longer might run for quite
  awhile before the join step reports failure, meaning that the PR sits
  in the queue for longer than needed being tested when we know it's
  already going to fail. By having all jobs cancel the run this means
  that failures immediately bail out and mark the whole job as
  cancelled.

* A new "determine" CI job was added to determine what CI actually needs
  to run. This is a "choke point" which is scheduled at the start of CI
  that quickly figures out what else needs to be run. This notably
  indicates whether large swaths of ci (the `run-full` flag) like the
  build matrix are executed. Additionally this dynamically calculates a
  matrix of tests to run based on a new `./ci/build-test-matrix.js`
  script. Various inputs are considered for this such as:

  1. All pushes, meaning merge queue branches or release-branch merges,
     will run full CI.
  2. PRs to release branches will run full CI.
  3. PRs to `main`, the most common, determine what to run based on
     what's modified and what's in the commit message.

  Some examples for (3) above are if modifications are made to
  `cranelift/codegen/src/isa/*` then that corresponding builder is
  executed on CI. If the `crates/c-api` directory is modified then the
  CMake-based tests are run on PRs but are otherwise skipped.
  Annotations in commit messages such as `prtest:*` can be used to
  explicitly request testing.

Before this PR merges to `main` would perform two full runs of CI: one
on the PR itself and one on the merge to `main`. Note that the one as a
merge to `main` was quite frequently cancelled due to a merge happening
later. Additionally before this PR there was always the risk of a bad
merge where what was merged ended up creating a `main` that failed CI to
to a non-code-related merge conflict.

After this PR merges to `main` will perform one full run of CI, the one
as part of the merge queue. PRs themselves will perform one test job
most of the time otherwise. The `main` branch is additionally always
guaranteed to pass tests via the merge queue feature.

For release branches, before this PR merges would perform two full
builds - one for the PR and one for the merge. A third build was then
required for the release tag itself. This is now cut down to two full
builds, one for the PR and one for the merge. The reason for this is
that the merge queue feature currently can't be used for our
wildcard-based `release-*` branch protections. It is now possible,
however, to turn on required CI checks for the `release-*` branch PRs so
we can at least have a "hit the button and forget" strategy for merging
PRs now.

Note that this change to CI is not without its risks. The Merge Queue
feature is still in beta and is quite new for GitHub. One bug that
Trevor and I uncovered is that if a PR is being tested in the merge
queue and a contributor pushes to their PR then the PR isn't removed
from the merge queue but is instead merged when CI is successful, losing
the changes that the contributor pushed (what's merged is what was
tested). We suspect that GitHub will fix this, however.

Additionally though there's the risk that this may increase merge time
for PRs to Wasmtime in practice. The Merge Queue feature has the ability
to "batch" PRs together for a merge but this is only done if concurrent
builds are allowed. This means that if 5 PRs are batched together then 5
separate merges would be created for the stack of 5 PRs. If the CI for
all 5 merged together passes then everything is merged, otherwise a PR
is kicked out. We can't easily do this, however, since a major purpose
for the merge queue for us would be to cut down on usage of CI builders
meaning the max concurrency would be set to 1 meaning that only one PR
at a time will be merged. This means PRs may sit in the queue for awhile
since previously many `main`-based builds are cancelled due to
subsequent merges of other PRs, but now they must all run to 100%
completion.

[testrepo]: https://github.com/bytecodealliance/wasmtime-merge-queue-testing

---
## [BlueMoon-Labs/SERP-BlueMoon-Station-13](https://github.com/BlueMoon-Labs/SERP-BlueMoon-Station-13)@[44ffcdfcc7...](https://github.com/BlueMoon-Labs/SERP-BlueMoon-Station-13/commit/44ffcdfcc7e628b06618f25e34bd14fea8e164a2)
#### Saturday 2023-03-25 20:52:32 by SkyratBot

[MIRROR] Kidnapping won't destroy implants, nodrop items [MDB IGNORE] (#19994)

* Kidnapping won't destroy implants, nodrop items (#74118)

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

* Kidnapping won't destroy implants, nodrop items

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Solulever2023/Mega-trends-Driving-Chemical-Industry---Digital-Strategies.-Pt.1](https://github.com/Solulever2023/Mega-trends-Driving-Chemical-Industry---Digital-Strategies.-Pt.1)@[97e1406c75...](https://github.com/Solulever2023/Mega-trends-Driving-Chemical-Industry---Digital-Strategies.-Pt.1/commit/97e1406c758e9f7f8118a8d90e3d643beb248dae)
#### Saturday 2023-03-25 21:07:42 by Solulever2023

Mega-trends Driving Chemical Industry -Pt.1

       
                  Mega-trends Driving Chemical Industry - Digital Strategies. Pt.1
Introduction.In these challenging times, the chemical industry has experienced its vulnerability and shown its tenacity. Disarray is a continuous thing and is the reason for the evolution of an industry in accordance with market changes and customer needs. To gear up to these challenges and to adapt to digital technical advancements, new levels of agility, scalability, data leveraging, collaboration should be adapted. Opportunities to lead the future of innovation will only present to those corporations that can integrate, simplify, and automate processes while bringing in more sustainable business models. Humans are the key enablers to all these transformations, which are technology intensive. End-to-end process reexamination will yield significant cultural changes in chemical companies. These processes extend beyond the enterprises. The industry will emphasize a common platform to share information with those across the value chain, earning trust and laying the foundation for a more sustainable future. The path of continuous innovation and leverage existing technologies will lead the Chemical companies to be the leaders in Digital transformation journeys. For instance, the use of artificial intelligence, automation, and optimization can unearth new sources of value while empowering business users to focus their time and energy on high-value activities.
The adoption of industry 4.0 is the key element for any industry which is underway in its digital transformation as intelligent technologies are embraced, and new levels of connectivity are brought into historical and siloed data. New business models based on real-time data sharing, and co-innovation with customers on new platforms and in ecosystems, will continue to be strong differentiators in the chemical industry. These innovations or opportunities for innovation include, for example, sharing data with customers to develop custom products, using real-time data to diagnose and correct production issues as they happen, and developing business models based on value rather than volume. Industry 4.0 is only one area where new digital technologies make it possible to gather and analyze data across machines and business systems to enable faster, more flexible, and efficient processes.
All these changes and innovations are driven by megatrends which can be categorized into three main sections:
•	Digital Strategies of Transformation
•	Success Priorities of Transformation
•	Underlying Technologies of Transformation
We will cover all three megatrends in this series of articles. The current article will majorly focus on ‘Digital Strategies of Transformation’.
Six Digital Strategies of Transformation
The Six Digital Strategies of Transformation which will decide the leaders for tomorrow are as follows:
1.	Increasing competition is driving the commoditization of products and the erosion of margins. This is resulting in chemical companies focusing on co-innovation, portfolio optimization, and selling of outcomes and business values instead of just developing products with the ultimate goal of generating new customers and consumer experiences.
2.	Sustainability is the new digital transformation that affects all areas of business. From reducing the overall cost of the products by decreasing the cost of operations through efficient energy management, to getting subsidiaries from different governments to drive the sustainable model, all while increasing the profit margins.
3.	The risk of supply chain breakage has increased dramatically in the past few years. The breakage ranges from pandemics affecting the availability of human resources to support operations, to wars disrupting international trade, taxation and various other increased risks. Various geopolitical risks, waves of pandemics and climate change play a crucial role in risk management now.
4.	Intelligent Technologies and automation are the new definitions of technical advancements. Technologies like the Internet of Things, Artificial Intelligence, Intelligent robotic process automation, machine learning, blockchain, the cloud and analytics, provide new opportunities for chemical manufacturers to cut costs by automating the back office and running low-touch operations.
5.	Starting to Participate in Business Networks is a step beyond traditional value chains for chemical companies, as they now play in the field with disruptors coming from all angles. Hence, thriving along with business partners becomes the right choice for them.
6.	In an increasingly dynamic world with mergers, acquisitions and divestitures, as key vehicles for portfolio optimization and sustainable growth, strategic Market driven agility has become imperative to survive and thrive.
Digital Strategies are ever evolving and transforming, and by this they also change the rules to be the leader in the market for Chemical Companies.
<aside> 💡 Studies suggest that about 45% of the chemical companies in the market are rethinking about the ways their human and machine resources are interacting with each other. 94% of executives in the chemical industries survey ways to increase their company’s digital expenditure and bring in the new positive transformation. 79% of industry experts believe that the best ROI will come for a company having either Cloud Computing (45%) or Big Data Analysis (34%).
</aside>
The ability to address these global trends will determine who will be among the winners in the midterm and long-term future. According to Accenture, tomorrow’s leading companies are already moving beyond products and services. They are applying technology to create deeper and more meaningful relationships with people. They are creating new affiliations with businesses across industries that share their vision and mission. They are using these new partnerships to invent new products and services that meet the goals of their customers and employees and, in doing so, are achieving new levels of growth and differentiation. They are also helping their communities create new economic opportunities and develop new ways to serve and protect citizens, benefitting society as a whole. Industry 4.0 is an enabler to achieve this, leading to a true Fourth Industrial Revolution.

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[05bccc5a00...](https://github.com/TaleStation/TaleStation/commit/05bccc5a00b0b9b7d9f407219b8e7dd9e7a14142)
#### Saturday 2023-03-25 21:29:20 by TaleStationBot

[MIRROR] [MDB IGNORE] RTD, RLD and RSF Prettification (#5054)

Original PR: https://github.com/tgstation/tgstation/pull/74093
-----

## About The Pull Request

Remade the RTD and its charge meter in the style of the other rapid
tools using the RCD as a base, along with its in hand icons.
Altered the RLD's in hand icons to more closely match their inventory
icon's palette and appearance.
Altered the RSF's darkest green color in its palette to be actually
green.
## Why It's Good For The Game
I think updating the RTD speaks for itself. The old one is just ugly and
sticks out like a sore thumb amongst the rest of the tools and honestly
seems like a placeholder.
the RLD's hand icons didn't match its inventory icon in its palette and
details. now it does and looks more consistent.
the last change on the RSF might be minutiae. if you cant tell what it
is: the very dark orange from the orange tools was kept despite the
green palette swap. which was most likely a mistake. so I gave it a dark
green that goes well with the rest of the palette even if it was only
for a few pixels.


![image](https://user-images.githubusercontent.com/121331795/226132541-d99d5723-dfe6-4ffd-a861-6d997d090a25.png)
(The RLD inventory icon is just there for reference.)
## Changelog
:cl:

imageadd: prettified all RTD icons 
imageadd: prettified in hand RLD icons 
imageadd: subtly improved the RSF icons

/:cl:

---------

Co-authored-by: Chlorotrifluoride <121331795+Chlorotrifluoride@users.noreply.github.com>

---
## [kugamo/cmss13](https://github.com/kugamo/cmss13)@[e5ab42dba0...](https://github.com/kugamo/cmss13/commit/e5ab42dba06e537df5c146169971dd8418f2ce55)
#### Saturday 2023-03-25 22:11:25 by boskoramen

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
## [DavidTran1311/Day_by_Day](https://github.com/DavidTran1311/Day_by_Day)@[841faf3a98...](https://github.com/DavidTran1311/Day_by_Day/commit/841faf3a987e99e36cbfcf8a398a44d1d5ae3ca9)
#### Saturday 2023-03-25 22:29:20 by aaliyahtran

Put logos n shit

- Fucked around in the apartment to make it look sexy
- Got rid of that stupid fucking canvas filter literally what the fuck was that\
- Made canvas prefab

---

