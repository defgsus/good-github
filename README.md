## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-06-24](docs/good-messages/2023/2023-06-24.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,688,621 were push events containing 2,506,674 commit messages that amount to 157,375,053 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 51 messages:


## [Zevotech/Shiptest](https://github.com/Zevotech/Shiptest)@[8744738e59...](https://github.com/Zevotech/Shiptest/commit/8744738e5955c02834d67db6f14201c28c9ac61c)
#### Saturday 2023-06-24 00:37:21 by Arturlang

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
## [BlackBoxMC/blackbox-rs](https://github.com/BlackBoxMC/blackbox-rs)@[b822ce6494...](https://github.com/BlackBoxMC/blackbox-rs/commit/b822ce6494e0e3ea03b3bfacdca3dbc7e94908ca)
#### Saturday 2023-06-24 01:49:08 by IoI_xD

almost done with function signatures for real. have to implement support for manually written classes because java just doesn't tell us about them because fuck you that's what

---
## [Jolly-66/JollyStation](https://github.com/Jolly-66/JollyStation)@[6105979883...](https://github.com/Jolly-66/JollyStation/commit/6105979883a1ea1e7fb0f69f588b73551921fa14)
#### Saturday 2023-06-24 01:52:15 by TaleStationBot

[MIRROR] [MDB IGNORE] Admin Library Moderation (in-game edition) (#6058)

Original PR: https://github.com/tgstation/tgstation/pull/75645
-----

## About The Pull Request

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

## Why It's Good For The Game


https://github.com/tgstation/tgstation/assets/58055496/60a9cfac-980a-4d99-bdaf-f3b6c9a9535f

## Changelog
:cl:
add: You can now filter by book id in library consoles
fix: The visitor console now actually has categories to select. Shows
how many people actually use it
admin: Added a library moderation tool, so you guys can do that again
now that statbus has passed into the byond
server: Bumped DB version, the library_action table has a few columns
that were improperly typed, this fixes that
/:cl:

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [Derpguy3/tgstation](https://github.com/Derpguy3/tgstation)@[867c217c57...](https://github.com/Derpguy3/tgstation/commit/867c217c57bbcbb644e06bfcb6d362e494a895ee)
#### Saturday 2023-06-24 02:30:01 by GuillaumePrata

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
## [norsvenska/tgstation](https://github.com/norsvenska/tgstation)@[a8e16030f8...](https://github.com/norsvenska/tgstation/commit/a8e16030f83911aef695ba9f28d565c41c99c3e6)
#### Saturday 2023-06-24 03:16:49 by LemonInTheDark

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
## [norsvenska/tgstation](https://github.com/norsvenska/tgstation)@[5c032cc098...](https://github.com/norsvenska/tgstation/commit/5c032cc098f9a1d62f9f9dee133ae7c3e4489dca)
#### Saturday 2023-06-24 03:16:49 by LemonInTheDark

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
## [puttingscienceintodatascience/teaching_materials](https://github.com/puttingscienceintodatascience/teaching_materials)@[1b2525deba...](https://github.com/puttingscienceintodatascience/teaching_materials/commit/1b2525deba5f877d3c784a14a5bc647453b5d3cb)
#### Saturday 2023-06-24 03:43:05 by Putting Science into Data Science

June 23 update based on Julia's feedback

Hi Jay,

Here's my feedback for the Website Color Challenge lecture slides:

In the intro, before diving into the challenge, add context from your industry experience, so students understand where this example came from, that it’s representative of the kinds of problems they’ll likely encounter, and the attitudes their supervisors will likely approach them with (assuming they’re right)? That way you establish the relevance and real-world connection.

—> this would make sense to add to all examples, so students understand these aren’t just toy examples?

Is there a syllabus that links the lectures to the readings in 9 Pitfalls and Thinking Clearly? Could make sense to reference the examples from both books at high level when you cover the pitfall, so students see the connection to the books and to other cases?

Slide 5: explain why you’re going into details of what probability is (—> hypothesis testing). Make explicit how this relates to the web color challenge and why this is relevant for data science. See notes in slide 15.

In general: frontload motivation and why more -- usually listed only at end, like resolving mystery, but then students are more likely to e lost re. how the lecture relates to data science and the pitfall. Could keep at the end but also frontload?

Thanks, these are great!
Julia

---
## [Dinobubba/cmss13](https://github.com/Dinobubba/cmss13)@[a2d5ca6e69...](https://github.com/Dinobubba/cmss13/commit/a2d5ca6e69725341f0fa261a4a3f89c737e843b3)
#### Saturday 2023-06-24 03:54:51 by QuickLode

Introducing the Colonial Marshal ERT w/ Anchorpoint Marines (#2318)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
My first PR of this scale, for sure. 

Been working on this PR for two weeks off and on, and finally I believe
I have checked every box that I intended to check when I first thought
of this idea a couple months back in November or so. Original idea:
https://discord.com/channels/150315577943130112/1037030635820306562/1037030635820306562

It will be adding a Colonial Marshal Bureau ERT, a Colonial Marshal
Bureau Inspection Team, and an Anchorpoint Station ERT.

First: Anchorpoint Station, unlike many ERTs, this one will hail from a
station. The station is located in the Neroid Sector and is used as a
transit / refinery station. It's large enough to hold 3000 but never
reaches its full potential. It consists of four towers and a central
module - one of the towers houses a permanent CMB presence and in the
same tower, a contingent of Colonial Marines is onboard. There's also a
Seegson office but I didn't do anything with it here.
Reference: https://avp.fandom.com/wiki/Anchorpoint_Station

For standard inspections, a dropship is dispatched from Anchorpoint
Station to the USS Almayer to carry out their objectives.
I do expect this to be the primary usage of this entire PR, because
there was always a part lacking for Anti-Corporate/Anti-Smuggling/CMB
type of interactions. It was almost always focused on Corporate, or
USCM. Nothing else. You should consider this to be an HRP addition to
the game.

Its also important to note that the Colonial Marshals are **Colonial**
and UA law enforcement agents / investigative functionaries. **They
shouldn't be enforcing Marine Law** unless: 1. The CMP/aCO has requested
it, 2. The Colonial Marshal believes its in the best interest of the CMB
and 3. The CMB Office at Anchorpoint(admins) does not intervene to
change this decision. Jurisdiction is another interaction that will be
nice to see. Non-USCM suspects should be transferred to the CMB, and
vice versa. The CMB should also be handling crimes, especially with the
ICC, involving smuggling, black market activities, and corporate
corruption/cover-ups.

**The Colonial Marshal** - He leads the team, and should be an
experience player with some knowledge of the lore behind what they are
doing. There's objectives and a backstory to help guide players if they
are unaware.
**The CMB Investigative Synthetic** - Unlike what you would expect from
most Synthetics, this one(as the name implies) is purely for
investigative and/or law enforcement purposes, though they have brought
along a medical belt.
**The CMB Deputy** - Working under the lead of the Marshal, his loyal
deputies uphold Colonial Law, Earth Law, and help with investigations
and/or law enforcement should it be needed.
**Interstellar Commerce Commission Corporate Liaison** - This Executive
works with the Colonial Marshals specifically to observe proper trade
practices and investigate any possibilities of smuggling or black market
activity. They are also an advisory agent to the Marshals by giving them
an eye on the corporate side of things.
**Interstellar Human Rights Observer** - Through a lot of hard work, the
Observer has managed to make his way onto the frontier to document and
record any kind of atrocities that may be occurring in this dark sector
of space. It's a bit of a PR stunt, but the Observer might surprise you.
Also, in an emergency, the Observer may be able to provide medical aid
for the team - they are the most capable of it.


For Emergency Responses, a nearby dropship which was enroute to an
investigation of its own, is re-routed to the USS Almayer's distress
beacon. There is a 10% chance of this happening.
They will not fare very well in extended combat, because they are not
prepared for it. They simply come aboard to lend a helping hand to a
distress beacon.
As the Colonial Marshals are equipped for law enforcement and
investigations, they are comparably lightly armed to most things they
might encounter in or by the USS Almayer.

This is where the contingent of Colonial Marines in Tower 4 comes in.

The third ERT that may be called in is an Anchorpoint Station QRF Team.
Canonically this is purely used when a random-beacon is answered by the
CMB Patrol Team, and they are able to raise the radio back to base to
call in the QRF. Thus giving them an additional, albeit optional
objective. This is controlled entirely by admins, as the Anchorpoint QRF
Team, despite its small size and average skill levels, is equipped with
a decent amount of gear compared to the depleted stocks of the USS
Almayer. Should the CMB team be able to raise its own distress signal to
the preparing QRF team, admins may choose to grant, delay, or deny the
QRF entirely.



Those are the main points of the PR.
There are also small variation changes to CMB-related survivors and also
some changes to synths.dm. (I tried to refractor the code because the
last PR to it bugged out the way items spawn in, but I was unsuccessful
and those changes are not in this PR.)

Pizza ERT chance and Freelancer ERT chance was nerfed by 4 and 5
respectively. This gives room for this ERT, and also Pizza was a bit
LRP.. You see a ship burning with a giant hole in it and you go to
deliver a pizza...?

EDIT: Pizza ERT removed from rotation entirely a la morrow

I would love to give a great thanks to:
nauticall - for their awesome cap and badge sprites! Also they have just
been a great help to me for much of my time here :)
kitsunemitsu - for their CMB hud icons!
harryOB - for helping me with fixing my vars and procs in the main ERT!
I was able to make things a % chance thanks to him.
and forest2001 - for helping me troubleshoot and find a solution for a
really annoying piece of hud code.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

This is a great, non-combat ERT and extremely HRP addition which adds a
phenomenal avenue of RP to the game rarely seen before. There is someone
to investigate the CL, interact with survivors, give MPs someone to talk
to, take non-USCM prisoners, assist with CMB-survivors and especially
with the new Black Market update this ERT will have tons of potential to
bring really interesting dynamics to the Almayer. The Colonial Marshal
Bureau are a HRP oriented set of roles, perfect for mini-events.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>
I have done extensive testing with this and believe I have figured out
pretty much every single bug. One thing I was not able to test was the
ERT messages for obvious reasons, but they seem to be sound - and a test
merge will definitely double check that.

In addition, there may or may not be a bug where the CMB cannot see
their own HUD Icons, but ghosts can just fine. I haven't been able to
find the cause of this yet.

https://media.discordapp.net/attachments/1042176396711170119/1064156692050358372/image.png</summary>

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

:cl: QuickLoad, nauticall, Kitsunemitsu, harryOB, forest2001
add: Introducing the Colonial Marshal Bureau Inspection and Emergency
Response Teams - A Law Enforcement & Investigative UA Functionary which
brings with it an HRP oriented set of roles perfect for your anti-corpo,
colonial, prisoner, smuggling, or other types of interactions on the
Almayer! It should unlock a very unique avenue of RP for many players,
especially smugglers, CL, survivors and the black market. This is a well
supported faction with their own frequencies, equipment, even faxes and
icons etcetera. The laws of the Earth stretch beyond the Sol.
add: Added the Anchorpoint Station Emergency QRF - A team of Colonial
Marines dispatched from Anchorpoint Station to respond to the CMB's
distress signal. Few in numbers, average in skills, but well equipped.
When things get dicey for the Marshals, they are the cavalry. This is an
admin call but makes it into an optional two-part ERT.
imageadd: Awesome looking CMB Cap, Marshal Badge and Deputy Badge by
nauticall!
imageadd: HUD Icons for each of the Colonial Marshal Bureau
Investigation Members, made by Kitsunemitsu!
imageadd: CMB key, hudsec and earpiece! Comes with a nice blue shale
radio color.
qol: Switched up some of the bugged synth loadouts, added some variety.
fix: Corrects the legacy path of hudsec where it was looking for old
paths instead of the updated ones - hudsec should work fine now. Thanks
to forest for his help in spotting these.
tweak: Superficial changes to cryo ERT loadout and CMB-relevant survivor
loadouts.
tweak: Superficial changes to armor vest so that they can carry
guns/lights.
tweak: Superficial changes to not being able to put on vests over
certain uniforms.
tweak: Freelancer ERT chance down from 25 to 20.
tweak: Synthetic vendor has some packs renamed for clarity, and receives
the tech welder satchel and medical satchel as an option.
del: Synthetic nurse hat is gone from Synthetics!
del: Pizza ERT is removed from rotation
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: naut <55491249+nauticall@users.noreply.github.com>
Co-authored-by: naut <nautilussplat@gmail.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[c35dd6e630...](https://github.com/treckstar/yolo-octo-hipster/commit/c35dd6e6309b561026fb96fe901b59850bee6bd9)
#### Saturday 2023-06-24 04:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [i-xzvr/evals](https://github.com/i-xzvr/evals)@[aeeb452867...](https://github.com/i-xzvr/evals/commit/aeeb4528675de633d95a3535100b23c98739f6ce)
#### Saturday 2023-06-24 04:40:24 by Alexander Raul

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
## [i-xzvr/evals](https://github.com/i-xzvr/evals)@[bf2ebb9dd6...](https://github.com/i-xzvr/evals/commit/bf2ebb9dd69e8fbaad3eb42dab1a0523066a52ed)
#### Saturday 2023-06-24 04:40:24 by Amir DIB

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
## [i-xzvr/evals](https://github.com/i-xzvr/evals)@[38f40050e9...](https://github.com/i-xzvr/evals/commit/38f40050e9344d6d4694c75506af03bf7ffe14d3)
#### Saturday 2023-06-24 04:40:24 by dz-pika

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
## [i-xzvr/evals](https://github.com/i-xzvr/evals)@[b2250e4117...](https://github.com/i-xzvr/evals/commit/b2250e4117125fa79e852f454cd4b01b3c066563)
#### Saturday 2023-06-24 04:40:24 by shivamd1810

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
## [i-xzvr/evals](https://github.com/i-xzvr/evals)@[9fdbd94c93...](https://github.com/i-xzvr/evals/commit/9fdbd94c93fc9560781c5e359e3be10d069ac6c5)
#### Saturday 2023-06-24 04:40:24 by Tong

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
## [yarnpkg/berry](https://github.com/yarnpkg/berry)@[a0064712f7...](https://github.com/yarnpkg/berry/commit/a0064712f7b0ae38c21fb204bea9831c2b269bd7)
#### Saturday 2023-06-24 06:13:27 by Maël Nison

Bumps Node requirements from 14 to 18 (#5445)

**What's the problem this PR addresses?**

We're still supporting Node 14, but it has reached end of life. Node 16
is still maintained, but will reach an early end of life in October, so
I think it's reasonable to drop it now rather than publish a major
release just for that.

**How did you fix it?**

Bumps the requirements from `14.16` to `18.12` (first LTS from the 18.x
release line).

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

---------

Co-authored-by: Kristoffer K <merceyz@users.noreply.github.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[87441b1ffd...](https://github.com/treckstar/yolo-octo-hipster/commit/87441b1ffd272dfa09e63daa15aad804ca3eb4a0)
#### Saturday 2023-06-24 06:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [kogelf/The_Arena_5_1](https://github.com/kogelf/The_Arena_5_1)@[5836a339d7...](https://github.com/kogelf/The_Arena_5_1/commit/5836a339d72842dd773f9129f7ade285cdd0f7ee)
#### Saturday 2023-06-24 06:28:56 by OscarEpsilon

So many things, So little progress

-Added Textures to Ferrous
-Added Ragdoll on death
-Added new bug where respawning doesn't even fucking work anymore
-Added a lot of lights to ferrous
-changed FOV for parity
-fixed bug where dying while in motion would translate that motion when respawning
-fixed bug where player character could shove their face through walls
-fixed bug where vines had collision
-attempted to change projectile speed
-reduced karrl's crossbow knockback
-died inside
-fixed bug where shoving your face into a ladder would teleport you out of the map
-made a tweak to FOV effects
-reduced mouse sensitivity
-found a new bug where invisible corpses probably cause weird inexplicable collisions, but didn't even know how to begin to fix that
-created new bug where dying while running up stairs teleported you up into god's realm
-probably fixed that bug
-client ferrous map hitbox is still insanely broken despite 30 minutes of rotting my brain

---
## [DevPatel1023/python](https://github.com/DevPatel1023/python)@[d6b790a966...](https://github.com/DevPatel1023/python/commit/d6b790a966e7bb9fcd684b2e71de06a9e9b9e208)
#### Saturday 2023-06-24 07:57:04 by Dev Patel

Create Greeting.py

This is an greeting app it basically greeting you good morning,afternoon,evening and night based upon system local time 
i use the time package that shows the local system time ,throw time it cheaks conditions and greeting you.

---
## [EvilDragonfiend/tgstation](https://github.com/EvilDragonfiend/tgstation)@[dff70625e7...](https://github.com/EvilDragonfiend/tgstation/commit/dff70625e7c29616887619dacc0375ddc84f0708)
#### Saturday 2023-06-24 08:05:48 by ChungusGamer666

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
## [HosseinKrouna/capstone-project](https://github.com/HosseinKrouna/capstone-project)@[ada669c5e2...](https://github.com/HosseinKrouna/capstone-project/commit/ada669c5e2ae78da6db5782427487849dcf0b66d)
#### Saturday 2023-06-24 08:29:36 by HosseinKrouna

Update README.md

"Friends Wall" is a user-friendly web application designed to simplify event planning and coordination among friends. With its intuitive interface and powerful features, the app enables users to create, manage, and collaborate on events effortlessly. Users can create personalized events, attach relevant images, and invite friends to join through a voting system. The app provides complete control over event details, allowing users to modify or delete events according to their preferences. With a demo version available for exploration, "Friends Wall" is optimized for mobile devices and built using technologies like React, Next.js, styled components, Immer, npm, Formidable, and Cloudinary. Experience the convenience and joy of organizing events with friends through "Friends Wall."

---
## [KingDragoness/ProjectHypatios](https://github.com/KingDragoness/ProjectHypatios)@[6e12356613...](https://github.com/KingDragoness/ProjectHypatios/commit/6e12356613109c21f833e09a2551023f0da1350d)
#### Saturday 2023-06-24 10:10:23 by KingDragoness

Hypatios 1.5.4b6 (quality of life improvements, bug fixes, balancing)
DONE (June 24)
• Change sewers entrance not using falling slope
• Fall damage increase chance when higher height
o 20m has 20%
o 50m has 100%
o Lerp (20m = 0, 50m = 1)
o Make no fall damage when no gravity
• Bug: Missing charge station bot
o Also, the stupid glitched Z fighting plane
• Bug: Eastria spaceguard always stuck in here! Bad collision!
o Don’t make spaceguard rotate freely! They look fucking stupid!
• Fortima change the fucking exit to not falling platform!
• Fortima fix the stupid overlapped audio when completing the chamber!
• Bug: Some audios in chamber 5 are not in the mixer.

---
## [Proxima-Project/Proxi-Eris](https://github.com/Proxima-Project/Proxi-Eris)@[17d0319a84...](https://github.com/Proxima-Project/Proxi-Eris/commit/17d0319a84f62458acbc4e4ae3ffb0211ab26a72)
#### Saturday 2023-06-24 12:11:32 by евиё

Titanium material (#8)

* adding titanium

may the god forgive me for editing base

* fixes my fuck ups

---
## [brucerennie/NetHack](https://github.com/brucerennie/NetHack)@[bbba8b82d2...](https://github.com/brucerennie/NetHack/commit/bbba8b82d2f3435fe6eba546773fe213299c5308)
#### Saturday 2023-06-24 12:43:15 by PatR

fix issue #1062 - monster hiding messages

Reported by Umbire:  if a statue of a hider-under was activated by
a statue trap, it would hide underneath its own statue.  Also, the
hero saw a snake hide under unseen submerged kelp.

Both of those things were exposed by new "you see <monster> hide"
message rather than caused by it.  It also led to the [re-]discovery
that an existing monster hiding under a statue that was a not-yet-
triggered trap prevented the trap from producing a monster.

This redoes yesterday's can't-hide-under-statue change:  hiders can
hide under statues again, but they can't hide under anything at trap
locations.  [Pits containing one or more objects are an exception,
although it seems silly that a hero is prevented from falling into
one by the presence of a tiny creepy-crawly hiding under a ring or
dart in there.]  So, hider-underers won't be able to interfere with
statue traps by being present at the trap location.  [Trappers and
lurkers-above probably need a similar restriction; I didn't look.
They avoid trap spots rather than get lured to such by objects.]

It also prevents newly created hider-underers from becoming hidden
as part of the their creation (except when that creation is part
of level creation) whether their creation uses up an object (statue
activation, egg hatching) or there are simply other items present.
That will prevent statue of a hider producing a monster that hides
under the activated statue (which was happening due to the sequence
create monster, transfer any statue contents to monster inventory,
destroy statue).

The can't-hide-under-statues code has been repurposed to prevent
hiding under gold pieces unless there are at least 10 (arbitrary
threshold) of those or they're in a pile with some other object(s).

Sea monsters hide in water regardless of the presence of objects.
Prevent other swimmers from hiding under objects at water locations.
Such creatures don't have gills and shouldn't be able to stay
submerged in hiding for an arbitrary length of time.  [No exception
is made for non-breathers.  The overlap between swimmers and hider-
underers is limited to small snakes, even though it is feasible for
a creature wearing an amulet of magical breathing to polymorph into
one.  Heros don't spend enough time underwater to worry about snakes
hiding under kelp or thrown junk.]

Lastly, alter the "suddenly, you notice a <monster>" message if
monster-vs-monster activity causes one you've just seen going into
hiding comes back out again without any intervening messages.  [I'm
not sure whether something similar is needed for the "Wait.  There's
something there" message in the you-vs-monster case.]

Fixes #1062

---
## [rvasseur31/react-native](https://github.com/rvasseur31/react-native)@[ee38c4a40c...](https://github.com/rvasseur31/react-native/commit/ee38c4a40c9d301c30fad4d127e8d020a6100b8e)
#### Saturday 2023-06-24 13:23:44 by Phillip Pan

introduce build boilerplate for ios unit tests (#37811)

Summary:
Pull Request resolved: https://github.com/facebook/react-native/pull/37811

Changelog: [Internal]

i am looking to add ios unit tests to venice and this is the first unit test suite that will test native ios code in the new architecture afaik, so i wanted to open this up to discussion.

currently, all `XCTest` in `react-native-github` are coupled with the `RNTester` target. my main qualm with this is i am concerned that it won't scale well. currently we have only ~30ish tests but ultimately if we want a proper testing suite, surely this count will be in the hundreds and that won't be able to reasonably live in a single test target.

however, the trade is that this test will not show up in RNTester. i have added a unit test to RNTester before in D31949237, however the experience was extremely painful as i had to manually update the `project.pbxproj` to include my file, and i had to manually determine what hex value was the next one (for whatever reason, this doesn't increment at the endian...).

i am wondering if we can treat the current unit testing experience in RNTester as pretty much maintenance mode and start thinking of a improved version starting with something more modular like this.

Reviewed By: cipolleschi

Differential Revision: D46467229

fbshipit-source-id: 09de9cf8bc5f8b9c86abcaf7750a6f63686d8d1a

---
## [cyberknight777/dragonheart_kernel_oneplus_sm8150](https://github.com/cyberknight777/dragonheart_kernel_oneplus_sm8150)@[1264c69809...](https://github.com/cyberknight777/dragonheart_kernel_oneplus_sm8150/commit/1264c698091aa1704de273ff8a912346f2238397)
#### Saturday 2023-06-24 13:58:02 by alk3pInjection

drm: Handle dim for udfps

* Apparently, los fod impl is better than udfps cuz it
  has onShow/HideFodView hook, which allows us to toggle
  dimlayer seamlessly.

  Since udfps only partially supports the former one,
  we'd better kill dim in kernel. This is kinda a hack
  but it works well, bringing perfect fod experience
  back to us.

Co-authored-by: Art_Chen <Chenxy0201@qq.com>
Signed-off-by: alk3pInjection <webmaster@raspii.tech>
Change-Id: I80bfd508dacac5db89f4fff0283529c256fb30ce
Signed-off-by: Cyber Knight <cyberknight755@gmail.com>

---
## [RAF-SI-2022/Banka-2-Frontend](https://github.com/RAF-SI-2022/Banka-2-Frontend)@[e30e4c744f...](https://github.com/RAF-SI-2022/Banka-2-Frontend/commit/e30e4c744fddac097755d84b5ce8277b963698f4)
#### Saturday 2023-06-24 14:16:48 by dimitrijevich

But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying consequences, or one who avoids a pain that produces no resultant pleasure?

---
## [CiarenceW/Receiver2ModdingKit](https://github.com/CiarenceW/Receiver2ModdingKit)@[e0ca8d51e7...](https://github.com/CiarenceW/Receiver2ModdingKit/commit/e0ca8d51e702b4a503645bf0fece0c5612c93000)
#### Saturday 2023-06-24 14:23:48 by Szikaka-97

Merge pull request #2 from CiarenceW/master

few things to make me hate my life less

---
## [AaronMatto/PathFindingVisualiser](https://github.com/AaronMatto/PathFindingVisualiser)@[400599419b...](https://github.com/AaronMatto/PathFindingVisualiser/commit/400599419bb3258cb59799f41b80e7a669ce3740)
#### Saturday 2023-06-24 15:35:58 by Aaron Matto

I FUCKIN DID IT HAHAHAA HOLY SHIT THIS TOOK WEEKS. NO TUTORIAL. NO GUIDES. NO CHEATING.  PURELY IMPLEMENTED BY YOURS TRULY. OPTIMISED ROTATIONS LETS GOOOOOOOO!!!!!!!

---
## [verheesj/evals](https://github.com/verheesj/evals)@[14f8771c40...](https://github.com/verheesj/evals/commit/14f8771c4015a2c70cc1c8f4f8197d8911fd2971)
#### Saturday 2023-06-24 15:46:12 by oscar

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
## [verheesj/evals](https://github.com/verheesj/evals)@[90587b6e5c...](https://github.com/verheesj/evals/commit/90587b6e5ce970b0c957c57ec18d7adcdeef26be)
#### Saturday 2023-06-24 15:46:12 by Juyeon Yoon

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
## [verheesj/evals](https://github.com/verheesj/evals)@[9edc150dde...](https://github.com/verheesj/evals/commit/9edc150dde3489c67a8990a2c5a6e694fb3fc012)
#### Saturday 2023-06-24 15:46:12 by Chen Zhao

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
## [verheesj/evals](https://github.com/verheesj/evals)@[c675067906...](https://github.com/verheesj/evals/commit/c67506790626630debd6e3ab74eda1b1851ac6a2)
#### Saturday 2023-06-24 15:46:12 by robin luo

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
## [verheesj/evals](https://github.com/verheesj/evals)@[936cc9d4ab...](https://github.com/verheesj/evals/commit/936cc9d4abfc0775f1fad1d694690870679f6924)
#### Saturday 2023-06-24 15:46:12 by somerandomguyontheweb

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
## [verheesj/evals](https://github.com/verheesj/evals)@[3504c839b4...](https://github.com/verheesj/evals/commit/3504c839b49f0848274c6e66965bbb5239bbf1fd)
#### Saturday 2023-06-24 15:46:12 by jjyuhub

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
## [verheesj/evals](https://github.com/verheesj/evals)@[9aeee0d71f...](https://github.com/verheesj/evals/commit/9aeee0d71f9f11b0d32cc9090d3ace4572e4ce8a)
#### Saturday 2023-06-24 15:46:12 by Syed Rishad

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
## [verheesj/evals](https://github.com/verheesj/evals)@[5c0b4ec185...](https://github.com/verheesj/evals/commit/5c0b4ec185485119adbd3d3cc8aea1b930724b28)
#### Saturday 2023-06-24 15:46:12 by Lorenzo

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
## [verheesj/evals](https://github.com/verheesj/evals)@[8b68875b95...](https://github.com/verheesj/evals/commit/8b68875b95129fbc95f44a8c26961c41f6fcda83)
#### Saturday 2023-06-24 15:46:12 by Sean Bird

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
## [narstybits/MacOS-DuckyScripts](https://github.com/narstybits/MacOS-DuckyScripts)@[ed0c6f751b...](https://github.com/narstybits/MacOS-DuckyScripts/commit/ed0c6f751b01bea0e86388f8bace60acb95d8ea4)
#### Saturday 2023-06-24 16:59:56 by Narsty

Rename Fuck your Files .txt to System File Deletion.txt

---
## [AllCorruptingWyrm/afterglow-ss13](https://github.com/AllCorruptingWyrm/afterglow-ss13)@[887388fa35...](https://github.com/AllCorruptingWyrm/afterglow-ss13/commit/887388fa35b6ec2a98ec530df7cc5f59d4643c52)
#### Saturday 2023-06-24 17:58:24 by Zephyr

Merge pull request #111 from Afterglow-Ss13/sani

fuck you

---
## [gilbert2003-beep/gilbert2003-beep](https://github.com/gilbert2003-beep/gilbert2003-beep)@[1f514a77d7...](https://github.com/gilbert2003-beep/gilbert2003-beep/commit/1f514a77d7ebc2de8b7b9e528ce9289dc4d82418)
#### Saturday 2023-06-24 18:48:34 by gilbert.bageni

Update README.md

Hi there, I'm Gilbert Bageni! 👋
I'm a passionate software engineer with a knack for building robust and user-friendly applications. Welcome to my GitHub profile, where you'll find a collection of my projects, contributions, and explorations in the world of code.

🧰 Tech Stack
Languages: Python, JavaScript, Java
Front-end: HTML, CSS, JavaScript, React
Back-end: Node.js, Express, Django
Databases: MySQL, MongoDB
Tools: Git, Docker, AWS
🚀 Projects
Here are a few notable projects I've worked on:

Project A: Brief description of the project and its purpose. Provide a link to the repository or a live demo.
Project B: Brief description of the project and its purpose. Provide a link to the repository or a live demo.
Project C: Brief description of the project and its purpose. Provide a link to the repository or a live demo.
Feel free to explore these projects and provide feedback. I'm always open to new ideas and suggestions!

🌱 Contributions
I believe in the power of open source and have made contributions to various projects. Some notable contributions include:

Project X: Brief description of the project and your contribution.
Project Y: Brief description of the project and your contribution.
Project Z: Brief description of the project and your contribution.
Check out these projects to see how I've collaborated with others and contributed to the developer community.

📚 Blog
I occasionally write about my experiences, learnings, and insights in the tech industry. Visit my blog to read some of my articles on topics such as software development, best practices, and emerging technologies. [Link to your blog or Medium profile]

🤝 Let's Connect
I'm always excited to connect with fellow developers, tech enthusiasts, and potential collaborators. Feel free to reach out to me via email or connect with me on LinkedIn. Let's chat about coding, exchange ideas, and explore opportunities to work together.

Thank you for visiting my GitHub profile. Enjoy exploring my projects, and happy coding! 👨‍💻

---
## [Daeberdir/Skyrat-tg](https://github.com/Daeberdir/Skyrat-tg)@[7dad8c75ca...](https://github.com/Daeberdir/Skyrat-tg/commit/7dad8c75cac06a405dc3c30a5cbc31919f33ff13)
#### Saturday 2023-06-24 19:16:07 by SkyratBot

[MIRROR] Adds a eye-dropper right-click function to the painting canvas. [MDB IGNORE] (#21411)

* Adds a eye-dropper right-click function to the painting canvas. (#75571)

## About The Pull Request
Having used the painting UI to kill some time during long rounds for a
decent chunk of the past year, the need of a quicker and less tedious
way to fix a misclick or mistake like drawing over the wrong pixel has
become clear to me, as well as getting some feedback on the palette
component I made last year.

As the title suggests, this PR adds an eye-dropper function to the
canvas. Right-Click a pixel on the canvas, and the painting tool will
copy its color. Simple as, works on both finished and unfinished
paintings.

As a bonus, you can also right-click one of those selectable
white/colored squares on the color scheme near the bottom of the UI (if
using spraycan/palette) to change its color without having to go back to
main game window and a radial menu.

EDIT: With the tooltip added to the UI, I can say it's ready.

## Why It's Good For The Game
This PR aims to add better options to change colors on the go and
improve the user experience on the painting UI.

## Changelog

:cl:
qol: Adds a eye-dropper-like right-click function to the painting canvas
UI. Right-Click a pixel on the canvas while holding a painting tool to
have it copy its color.
qol: Also adds a right-click function to the color palette at the bottom
of the UI to allow users to set its colors without having to alternate
between the game window and the UI.
qol: Lastly, a tooltip has been added near the top-left corner of the
same UI to let players know of these features.
/:cl:

* Adds a eye-dropper right-click function to the painting canvas.

---------

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [Punkwe1ght/evals](https://github.com/Punkwe1ght/evals)@[93fa8a55e9...](https://github.com/Punkwe1ght/evals/commit/93fa8a55e9113ebf221347af731b9a5fb6400512)
#### Saturday 2023-06-24 19:20:33 by Austin Starnes

Add logic grid puzzle eval (#830)

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
`logic-grid`

### Eval description

The model is prompted with a logic grid word problem with a list of
hints, categories, and values for the category. The model is then asked
to provide a solution, showing reasoning, in a set of Python tuples that
show the matched category values.

<details>
  <summary>See human-friendly example prompt</summary>

```
Using the hints and information provided, solve the following logic grid puzzle.
Show your reasoning concisely, but step-by-step, to arrive at your final answer.
Remember, since this is a grid-based puzzle, each option in every category will be used exactly once.
Since there are 4 values per category, and 3 categories, your final answer will include 4 tuples each of length 3.
 Puzzle Scenario:
A number of new space probes were launched this year. Using only the clues that follow, match each probe to the month it launched and its eventual destination.

Category Options:
  Probes: "Nalini", "Hikaru", "Sarika", and "Sven"
  Destinations: "Ganymede", "Titan", "Enceladus", and "Phobos"
  Months: "January", "February", "March", and "April"

Hints:
  1: The Hikaru launched 2 months before the Nalini.
  2: The probe going to Phobos launched sometime after the Hikaru.
  3: The Sven launched 2 months before the mission going to Ganymede.
  4: Of the probe that launched in April and the mission going to Titan, one is the Sarika and the other is the Nalini.

In your response, format your final answer for each set of linked category values as a python tuple of strings in this order:
("Enceladus", [value from months], [value from probes])
("Ganymede", [value from months], [value from probes])
("Phobos", [value from months], [value from probes])
("Titan", [value from months], [value from probes])
```
</details>

<details>
  <summary>See expected/ideal answer</summary>

```
("Enceladus", "January", "Hikaru")
("Ganymede", "April", "Sarika")
("Phobos", "February", "Sven")
("Titan", "March", "Nalini")
```
</details>

<details>
<summary>See failure case from GPT-4 (at least from the web UI - I don't
have API access to GPT-4)</summary>

```
Step 1: From Hint 3, we know that Hikaru launched 2 months before Nalini. Since the latest month available is April, this means that Nalini cannot have launched in April because there wouldn't be a 2-month gap for Hikaru. So, Nalini must be the probe going to Titan (from Hint 4), and Sarika must be the probe that launched in April.

Step 2: Since Nalini is going to Titan, from Hint 4, it must have launched in February to allow Hikaru to launch in December (2 months before). However, December is not an option, so Hikaru must have launched in January (the earliest month possible) and Nalini in March.

Step 3: The Sven launched 2 months before the mission going to Ganymede (Hint 2). Since Sven cannot be launched in January (as Hikaru is launched in January), it must have launched in February. That means the mission to Ganymede must be in April.

Step 4: The only remaining month is March, and the only remaining probe is Nalini. So Nalini was launched in March.

Step 5: The probe going to Phobos launched sometime after Hikaru (Hint 1). Since Hikaru launched in January, the only remaining option for Phobos is Sarika, which launched in April.

Step 6: The only remaining destination is Enceladus, and the only remaining probe is Hikaru, so Hikaru is going to Enceladus.

The final answer is:
("Enceladus", "January", "Hikaru")
("Ganymede", "April", "Sven")
("Phobos", "April", "Sarika")
("Titan", "March", "Nalini")
```
</details>

### What makes this a useful eval?

This set of evals relies on a lot of *context-ramping* (as I call it)
for LLMs to get right - relying on chain-of-thought style logic to
'ramp' into the most likely next-deduction for a multi-parameter logical
problem.
These prompts are written as word problems and don't rely on any ASCII
or markdown type of table to express the puzzle (though `gpt-3.5-turbo`
appears to use markdown tables in it's chain of thought).

This ramping gets expensive and doesn't scale well with the increase of
category or values-per-category parameters, and is something that LLMs
might benefit from avoiding (either by requiring less of a context-ramp
to get to the meat of an answer, or by the surrounding
infrastructure/problem agent that tries to use a cheaper ensemble for
most of the context ramping, or other strategies).

The reasoning skills required for this kind of <b>constraint
satisfaction</b> expressed in natural language word prompts can, in
theory, generalize to solving constraints expressed in less structured
formats in the wild.

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
- [X] <span title="A GPT-4 failure case from the eval set is included
above.">Contains failures where a human can do the task, but either
GPT-4 or GPT-3.5-Turbo could not.</span>
- [X] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [X] **<span title="15 examples per grid size are included, for 6
different grid sizes, make a total of 90 included examples.">Include at
least 15 high quality examples.</span>**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This eval contains varied prompts and grid sizes, 15 examples per grid
size, for a total of 90 procedurally generated puzzles.
~This PR also implements (disabled by default) multiline answers and
punctuation whitelisting behavior in `FuzzyMatch`, which was required
due to the structural nature of the logic grid answers and the behavior
of `utils.normalize(...)` which (prior to this PR) did not provide any
functionality to interpret answers that span across newline characters
`\n` or preserve punctuation where it may be useful (in this case, the
model is prompted for the resultant grid associations in python tuple
format, so the punctuation in `(",)` is configured to be preserved for
these evals).
The new functionality is, again, disabled by default, such that existing
evals are not affected.~

## Eval structure 🏗️

Your eval should
- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your yaml is registered at
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
{"input":[{"role":"system","content":"Using the hints and information
provided, solve the following logic grid puzzle.\nShow your reasoning
concisely, but step-by-step, to arrive at your final answer.\nRemember,
since this is a grid-based puzzle, each option in every category will be
used exactly once.\nSince there are 4 values per category, and 3
categories, your final answer will include 4 tuples each of length
3.\n"},{"role":"system","content":"Puzzle Scenario:\nA number of new
space probes were launched this year. Using only the clues that follow,
match each probe to the month it launched and its eventual
destination.\n\nCategory Options:\n Probes: \"Nalini\", \"Hikaru\",
\"Sarika\", and \"Sven\"\n Destinations: \"Ganymede\", \"Titan\",
\"Enceladus\", and \"Phobos\"\n Months: \"January\", \"February\",
\"March\", and \"April\"\n\nHints:\n 1: The Hikaru launched 2 months
before the Nalini.\n 2: The probe going to Phobos launched sometime
after the Hikaru.\n 3: The Sven launched 2 months before the mission
going to Ganymede.\n 4: Of the probe that launched in April and the
mission going to Titan, one is the Sarika and the other is the
Nalini.\n\nIn your response, format your final answer for each set of
linked category values as a python tuple of strings in this
order:\n(\"Enceladus\", [value from months], [value from
probes])\n(\"Ganymede\", [value from months], [value from
probes])\n(\"Phobos\", [value from months], [value from
probes])\n(\"Titan\", [value from months], [value from
probes])"}],"ideal":"(\"Enceladus\", \"January\",
\"Hikaru\")\n(\"Ganymede\", \"April\", \"Sarika\")\n(\"Phobos\",
\"February\", \"Sven\")\n(\"Titan\", \"March\", \"Nalini\")"}
{"input":[{"role":"system","content":"Using the hints and information
provided, solve the following logic grid puzzle.\nShow your reasoning
concisely, but step-by-step, to arrive at your final answer.\nRemember,
since this is a grid-based puzzle, each option in every category will be
used exactly once.\nSince there are 4 values per category, and 3
categories, your final answer will include 4 tuples each of length
3.\n"},{"role":"system","content":"Puzzle Scenario:\nThe Monterey Bay
Aquarium has a new exhibit featuring several dolphin skeletons. The
aquarium asked local elementary school children to name each dolphin and
match it to its species, length, and the year in which it was donated to
the aquarium. Use the given clues to solve the puzzle.\n\nCategory
Options:\n Dolphin: \"Atlantic white-sided dolphin\", \"Pacific
white-sided dolphin\", \"common dolphin\", and \"bottlenose dolphin\"\n
Names: \"Momo\", \"Simon\", \"Tychus\", and \"Marlo\"\n Lengths: \"21
ft\", \"23 ft\", \"25 ft\", and \"27 ft\"\n\nHints:\n 1: Momo is 4 feet
shorter than Tychus.\n 2: The common dolphin is somewhat shorter than
the bottlenose dolphin.\n 3: The 21 ft long exhibit is either the
Atlantic white-sided dolphin or Simon.\n 4: Marlo is either the 23 ft
long exhibit or the Atlantic white-sided dolphin.\n 5: Of Simon and the
Pacific white-sided dolphin, one is 27 ft long and the other is 21 ft
long.\n\nIn your response, format your final answer for each set of
linked category values as a python tuple of strings in this
order:\n(\"Atlantic white-sided dolphin\", [value from lengths], [value
from names])\n(\"Pacific white-sided dolphin\", [value from lengths],
[value from names])\n(\"bottlenose dolphin\", [value from lengths],
[value from names])\n(\"common dolphin\", [value from lengths], [value
from names])"}],"ideal":"(\"Atlantic white-sided dolphin\", \"25 ft\",
\"Marlo\")\n(\"Pacific white-sided dolphin\", \"27 ft\",
\"Tychus\")\n(\"bottlenose dolphin\", \"23 ft\", \"Momo\")\n(\"common
dolphin\", \"21 ft\", \"Simon\")"}
{"input":[{"role":"system","content":"Using the hints and information
provided, solve the following logic grid puzzle.\nShow your reasoning
concisely, but step-by-step, to arrive at your final answer.\nRemember,
since this is a grid-based puzzle, each option in every category will be
used exactly once.\nSince there are 4 values per category, and 3
categories, your final answer will include 4 tuples each of length
3.\n"},{"role":"system","content":"Puzzle Scenario:\nHillcrest County
Hospital released a press release today to announce its annual list of
the first babies born immediately after the start of the new year. Using
only the clues below, match each baby to its family time of birth, and
determine the room number in which it was delivered.\n\nCategory
Options:\n Names: \"Lydia\", \"Naomi\", \"Katherine\", and \"Rebecca\"\n
Families: \"McIntyre\", \"Gonzalez\", \"Hudson\", and \"O'Connor\"\n
Times: \"12:01am\", \"12:04am\", \"12:07am\", and
\"12:10am\"\n\nHints:\n 1: Naomi was born 3 minutes after Rebecca.\n 2:
The Hudsons' child was born 6 minutes after the O'Connors' child.\n 3:
The baby born at 12:04am was either Rebecca or the McIntyres' child.\n
4: Of Katherine and the baby born at 12:01am, one was the O'Connors' and
the other was the Gonzalezes'.\n\nIn your response, format your final
answer for each set of linked category values as a python tuple of
strings in this order:\n(\"Gonzalez\", [value from names], [value from
times])\n(\"Hudson\", [value from names], [value from
times])\n(\"McIntyre\", [value from names], [value from
times])\n(\"O'Connor\", [value from names], [value from
times])"}],"ideal":"(\"Gonzalez\", \"Katherine\",
\"12:10am\")\n(\"Hudson\", \"Lydia\", \"12:07am\")\n(\"McIntyre\",
\"Naomi\", \"12:04am\")\n(\"O'Connor\", \"Rebecca\", \"12:01am\")"}
{"input":[{"role":"system","content":"Using the hints and information
provided, solve the following logic grid puzzle.\nShow your reasoning
concisely, but step-by-step, to arrive at your final answer.\nRemember,
since this is a grid-based puzzle, each option in every category will be
used exactly once.\nSince there are 4 values per category, and 3
categories, your final answer will include 4 tuples each of length
3.\n"},{"role":"system","content":"Puzzle Scenario:\nMedisynth
Therapeutics has spent decades scouring the world's rainforests for new
sources of medical drugs, and this year a number of these new drugs have
been officially approved by the FDA. Using only the clues below, match
each drug to the condition it treats, the month it was approved, and the
source from which its main ingredient is derived.\n\nCategory Options:\n
Drugs: \"Mystolam\", \"Soludox\", \"Aurexil\", and \"Synodil\"\n
Conditions: \"rheumatism\", \"chikungunya\", \"hyperglycemia\", and
\"encephalitis\"\n Months: \"January\", \"February\", \"March\", and
\"April\"\n\nHints:\n 1: The medicine that treats hyperglycemia was
approved sometime after Synodil.\n 2: The medicine that treats
hyperglycemia was approved 1 month before the medicine that treats
rheumatism.\n 3: Of Mystolam and the pharmaceutical approved in April,
one treats rheumatism and the other treats encephalitis.\n 4: Of the
Aurexil approved in February and the drug that treats chikungunya, one
is Soludox and the other is Synodil.\n\nIn your response, format your
final answer for each set of linked category values as a python tuple of
strings in this order:\n(\"chikungunya\", [value from drugs], [value
from months])\n(\"encephalitis\", [value from drugs], [value from
months])\n(\"hyperglycemia\", [value from drugs], [value from
months])\n(\"rheumatism\", [value from drugs], [value from
months])"}],"ideal":"(\"chikungunya\", \"Synodil\",
\"January\")\n(\"encephalitis\", \"Soludox\",
\"April\")\n(\"hyperglycemia\", \"Aurexil\",
\"February\")\n(\"rheumatism\", \"Mystolam\", \"March\")"}
{"input":[{"role":"system","content":"Using the hints and information
provided, solve the following logic grid puzzle.\nShow your reasoning
concisely, but step-by-step, to arrive at your final answer.\nRemember,
since this is a grid-based puzzle, each option in every category will be
used exactly once.\nSince there are 4 values per category, and 3
categories, your final answer will include 4 tuples each of length
3.\n"},{"role":"system","content":"Puzzle Scenario:\nA group of friends
has gotten together for dinner, and just for fun they're comparing their
\"social networking\" stats on Facebook, Twitter and LinkedIn. Using
only the clues that follow, determine the number of friends (Facebook),
followers (Twitter) and connections (LinkedIn) each person
has.\n\nCategory Options:\n Names: \"Avery\", \"Evan\", \"Natalia\", and
\"Camila\"\n Linkedin: \"54\", \"59\", \"64\", and \"68\"\n Facebook:
\"120\", \"130\", \"140\", and \"150\"\n\nHints:\n 1: Avery has 68
LinkedIn connections.\n 2: Natalia has 10 fewer Facebook friends than
the person with 68 LinkedIn connections.\n 3: The person with 140
Facebook friends is either the one with 54 LinkedIn connections or
Evan.\n 4: The one with 54 LinkedIn connections has 10 fewer Facebook
friends than the one with 64 LinkedIn connections.\n\nIn your response,
format your final answer for each set of linked category values as a
python tuple of strings in this order:\n(\"120\", [value from LinkedIn],
[value from names])\n(\"130\", [value from LinkedIn], [value from
names])\n(\"140\", [value from LinkedIn], [value from names])\n(\"150\",
[value from LinkedIn], [value from names])"}],"ideal":"(\"120\", \"59\",
\"Natalia\")\n(\"130\", \"68\", \"Avery\")\n(\"140\", \"54\",
\"Camila\")\n(\"150\", \"64\", \"Evan\")"}
  ```
</details>

---
## [Punkwe1ght/evals](https://github.com/Punkwe1ght/evals)@[b0650402dd...](https://github.com/Punkwe1ght/evals/commit/b0650402ddeaf93dba27f4a0252ae890bf8184ab)
#### Saturday 2023-06-24 19:20:33 by Alexander Shirkov

[Eval] English-Russian homonym context resolution (GPT-3.5: 0.42) (#1064)

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
English-Russian homonym context resolution

### Eval description

Cross-lingual English-Russian eval to resolve ambiguity with homonyms
present.

### What makes this a useful eval?

[Insert why this eval is worth including and any additional context]
Cross-lingual homonyms are hard to resolve: they add context ambiguity,
which needs to be resolved via reasoning.

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
{"input": [{"role": "system", "content": "For the given context, resolve
the ambiguity and determine the most appropriate response. If there is
one, output just one word; otherwise, output unknown. The responses must
be lowercase with no punctuation."}, {"role": "user", "content": "You
are coming to a community facility to drop a child for hockey practice.
The road is under construction and big machines are paving it. What
would \"каток\" mean in this context? rink or roller"}], "ideal":
"unknown"}
{"input": [{"role": "system", "content": "For the given context, resolve
the ambiguity and determine the most appropriate response. If there is
one, output just one word; otherwise, output unknown. The responses must
be lowercase with no punctuation."}, {"role": "user", "content": "You
are coming to a community facility to drop a child for hockey practice.
The road is under construction and big machines are paving it. Child
pointing at the machine and says: \"каток\". What does he mean: rink or
roller?"}], "ideal": "roller"}
{"input": [{"role": "system", "content": "For the given context, resolve
the ambiguity and determine the most appropriate response. If there is
one, output just one word; otherwise, output unknown. The responses must
be lowercase with no punctuation."}, {"role": "user", "content": "You
are coming to a community facility to drop a child for hockey practice.
The road is under construction and big machines are paving it. Child
pointing at the building and says: \"каток\". What does he mean: rink or
roller?"}], "ideal": "rink"}
{"input": [{"role": "system", "content": "For the given context, resolve
the ambiguity and determine the most appropriate response. If there is
one, output just one word; otherwise, output unknown. The responses must
be lowercase with no punctuation."}, {"role": "user", "content": "A
woman with long braided hair is working in the field. She cuts the grass
with scythe. Someone says \"хорошая коса\". Do they refer scythe or
hairstyle?"}], "ideal": "unknown"}
{"input": [{"role": "system", "content": "For the given context, resolve
the ambiguity and determine the most appropriate response. If there is
one, output just one word; otherwise, output unknown. The responses must
be lowercase with no punctuation."}, {"role": "user", "content": "A
woman with long braided hair is working in the field. She cuts the grass
with scythe. Someone points at the quality of her work and says
\"хорошая коса\". Do they refer scythe or hairstyle?"}], "ideal":
"scythe"}
{"input": [{"role": "system", "content": "For the given context, resolve
the ambiguity and determine the most appropriate response. If there is
one, output just one word; otherwise, output unknown. The responses must
be lowercase with no punctuation."}, {"role": "user", "content": "A
woman with long braided hair is working in the field. She cuts the grass
with scythe. Someone points at her head and says \"хорошая коса\". Do
they refer scythe or hairstyle?"}], "ideal": "hairstyle"}
{"input": [{"role": "system", "content": "For the given context, resolve
the ambiguity and determine the most appropriate response. If there is
one, output just one word; otherwise, output unknown. The responses must
be lowercase with no punctuation."}, {"role": "user", "content": "Scythe
is found on a sandbar. A person is saying: \"коса\". Do they refer
scythe or sandbar?"}], "ideal": "unknown"}
{"input": [{"role": "system", "content": "For the given context, resolve
the ambiguity and determine the most appropriate response. If there is
one, output just one word; otherwise, output unknown. The responses must
be lowercase with no punctuation."}, {"role": "user", "content": "Scythe
is found on a sandbar. A person is saying: \"ржавая коса\". Do they
refer scythe or sandbar?"}], "ideal": "scythe"}
  ```
</details>

---
## [Punkwe1ght/evals](https://github.com/Punkwe1ght/evals)@[e959ff4b90...](https://github.com/Punkwe1ght/evals/commit/e959ff4b90c3511f5b8a91ca69413a9206d8c4c7)
#### Saturday 2023-06-24 19:20:33 by Vasco Lange

[Eval] German part-of-speech (#1053)

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
> german-part-of-speech

### Eval description

> For a given German word, the model is asked to list all possible parts
of speech (multiple choice). The model is also asked to think about the
word as an inflection of another word. The models output is tested
against annotations extracted from de.wiktionary.org. This is a follow
up to #1039

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

> To build the dataset, all 1.000.000+ entries of the German wiktionary
were parsed. Excluded from this list were all phrases, abbreviations,
symbols, names, toponyms and any words with at least one possible part
of speech not fitting the categories given in the prompt. Also I had to
exclude some entries where the part of speech could not be determined
automatically from the wikitext.
> From this set, words were sampled so that each combination of the
parts of speech existing in the dataset would be equally likely in the
tests. This way the model is tested to respond with all possible uses of
a word and not just the most common ones. > For combinations that fit a
lot of words, the uniform sampling led to a bias towards rarely used
words.
> The labels of each word were taken from the corresponding page at
de.wiktionary.org/wiki/{word}. The information taken from each page was:
the word, the part of speech this word can have in German and whether
the word is an abbreviation or not.
> This means only factual data was taken and is therefore in the public
domain.

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
{"input": [{"role": "system", "content": "Act as a German language
part-of-speech classifier. You will be prompted with a single German
word. Return an unsorted comma-separated list for all the parts of
speech the word could possibly be, in any context. Take care to consider
if the word is any kind of inflection. If so, include the part of speech
for the main word.\nAnswer with the comma-separated list only. Use
single spaces after the commas. End the list with a dot. Do not include
any explanations. Only include parts of speech from the following list,
ignoring possible other parts of speech:\nadjective, adverb, article,
conjunction, interjection, noun, particle, preposition, pronoun,
verb\n**Example prompt 1**: alle\n**Example output 1**: adverb, noun,
pronoun.\n**Example prompt 2**: künftig\n**Example output 2**:
adjective, adverb.\n**Example prompt 3**: Sommelier\n**Example output
3**: noun.\n**Prompt**:"}, {"role": "user", "content": "anstelle"}],
"ideal": ["preposition, adverb, verb.", "preposition, verb, adverb.",
"adverb, preposition, verb.", "adverb, verb, preposition.", "verb,
preposition, adverb.", "verb, adverb, preposition."]}
{"input": [{"role": "system", "content": "Act as a German language
part-of-speech classifier. You will be prompted with a single German
word. Return an unsorted comma-separated list for all the parts of
speech the word could possibly be, in any context. Take care to consider
if the word is any kind of inflection. If so, include the part of speech
for the main word.\nAnswer with the comma-separated list only. Use
single spaces after the commas. End the list with a dot. Do not include
any explanations. Only include parts of speech from the following list,
ignoring possible other parts of speech:\nadjective, adverb, article,
conjunction, interjection, noun, particle, preposition, pronoun,
verb\n**Example prompt 1**: alle\n**Example output 1**: adverb, noun,
pronoun.\n**Example prompt 2**: künftig\n**Example output 2**:
adjective, adverb.\n**Example prompt 3**: Sommelier\n**Example output
3**: noun.\n**Prompt**:"}, {"role": "user", "content": "heute"}],
"ideal": ["adverb, verb.", "verb, adverb."]}
{"input": [{"role": "system", "content": "Act as a German language
part-of-speech classifier. You will be prompted with a single German
word. Return an unsorted comma-separated list for all the parts of
speech the word could possibly be, in any context. Take care to consider
if the word is any kind of inflection. If so, include the part of speech
for the main word.\nAnswer with the comma-separated list only. Use
single spaces after the commas. End the list with a dot. Do not include
any explanations. Only include parts of speech from the following list,
ignoring possible other parts of speech:\nadjective, adverb, article,
conjunction, interjection, noun, particle, preposition, pronoun,
verb\n**Example prompt 1**: alle\n**Example output 1**: adverb, noun,
pronoun.\n**Example prompt 2**: künftig\n**Example output 2**:
adjective, adverb.\n**Example prompt 3**: Sommelier\n**Example output
3**: noun.\n**Prompt**:"}, {"role": "user", "content": "Mist"}],
"ideal": ["noun, interjection.", "interjection, noun."]}
{"input": [{"role": "system", "content": "Act as a German language
part-of-speech classifier. You will be prompted with a single German
word. Return an unsorted comma-separated list for all the parts of
speech the word could possibly be, in any context. Take care to consider
if the word is any kind of inflection. If so, include the part of speech
for the main word.\nAnswer with the comma-separated list only. Use
single spaces after the commas. End the list with a dot. Do not include
any explanations. Only include parts of speech from the following list,
ignoring possible other parts of speech:\nadjective, adverb, article,
conjunction, interjection, noun, particle, preposition, pronoun,
verb\n**Example prompt 1**: alle\n**Example output 1**: adverb, noun,
pronoun.\n**Example prompt 2**: künftig\n**Example output 2**:
adjective, adverb.\n**Example prompt 3**: Sommelier\n**Example output
3**: noun.\n**Prompt**:"}, {"role": "user", "content": "Rotschöpfe"}],
"ideal": ["noun."]}
{"input": [{"role": "system", "content": "Act as a German language
part-of-speech classifier. You will be prompted with a single German
word. Return an unsorted comma-separated list for all the parts of
speech the word could possibly be, in any context. Take care to consider
if the word is any kind of inflection. If so, include the part of speech
for the main word.\nAnswer with the comma-separated list only. Use
single spaces after the commas. End the list with a dot. Do not include
any explanations. Only include parts of speech from the following list,
ignoring possible other parts of speech:\nadjective, adverb, article,
conjunction, interjection, noun, particle, preposition, pronoun,
verb\n**Example prompt 1**: alle\n**Example output 1**: adverb, noun,
pronoun.\n**Example prompt 2**: künftig\n**Example output 2**:
adjective, adverb.\n**Example prompt 3**: Sommelier\n**Example output
3**: noun.\n**Prompt**:"}, {"role": "user", "content": "vornüber"}],
"ideal": ["adverb."]}
  ```
</details>

---------

Co-authored-by: Vasco Yannic Lange <mail@vascolange.com>

---
## [koji/opentrons](https://github.com/koji/opentrons)@[5271d4fbc4...](https://github.com/koji/opentrons/commit/5271d4fbc473bb8f2506a90b2c929535c82892f6)
#### Saturday 2023-06-24 19:39:34 by Seth Foster

feat(api,shared-data): error codes in PE (#12936)

On the python side of our code, we want our new enumerated exceptions to
be gradually integratable, and we also want to make sure that any errors
that we didn't yet get the chance to give error codes end up with error
codes. To do this in a programmatic way, we can add some automated
methods for wrapping python exceptions.

All enumerated errors now get to wrap errors. These are optional
sequences of more enumerated errors that are considered to have caused
the top-level one - in most cases, this will be because the enumerated
error explicitly was instantiated to wrap a python exception, but it
could also be if it was raised from one.

Since we only wrap other enumerated errors, we need a way to make
exceptions enumerated errors. A new exception type (but not code - it's
just a GeneralError) called PythonException has this capability; it lets
you give it BaseExceptions in addition to other EnumeratedErrors, and
it's capable of walking the python memory model internals to try and get
the other exceptions in a stack of raise from ... raise from ... calls
that are reasonably popular in our code. This is functionality that is
promoted out of The Dunder Zone in python 3.11, so I feel pretty good
using it (this is what ExceptionGroups are).

So now, as in the tests, if you catch an exception and give it to a
PythonException you bless it with an error code and save all the
exceptions and their stack traces for later inspection. Cool!

ProtocolEngine is the first place we'll go through and add places that
actually use these error codes, since it's in a lovely high-leverage
middle spot in our stack. That means we both get to test the upward
interface of how these things will be represented in the HTTP API and
how they'll be created from lower exceptions.

ProtocolEngine already has its own very large and robust set of custom
exceptions, which is awesome. We can make them inherit from the
enumerated errors pretty easily, but unfortunately we have to add a
bunch of stuff to their constructors to pass along things like the
ability to wrap other exceptions and so on. Luckily that's just typing.

Once we've done that, at the three points we catch all missed exceptions
we have to switch over to creating the new style. ProtocolEngineErrors
get passed on; uncaught legacy errors get captured as PythonExceptions;
and uncaught errors in the normal core do too.

Finally, we have to represent this new style of error in the
ErrorOccurrence objects. This is the fun part. Previously, we'd added
error codes to those objects; this was sort of a big deal because we
want them to be required when you make new ErrorOccurrences and when
clients look, but we don't want things to break when we deserialize old
ones. We can extend that trick pretty easily to add new things. What's
not quite as easy is this concept of wrapping errors. Our errors are now
essentially trees, and we need tree structure here. Luckily, jsonschema
and pydantic are actually pretty good at type-recursive schema and
object definitions, so we can plop a list of other error occurrences in
there.

Now, when we catch one of these errors that's bubbled up from hardware,
we give it a name and we capture its entire history in an inspectable
way, and I think that's really cool.

---
## [mikeevmm/sane](https://github.com/mikeevmm/sane)@[370cc78fad...](https://github.com/mikeevmm/sane/commit/370cc78fade7e2e10fe0a06d2ade1868de605ec6)
#### Saturday 2023-06-24 20:17:43 by Miguel M

Release: sane 7.0

Version 7.0 was completely rewritten from scratch. Sane is now based on
a small number of decorators, namely @cmd, @task, @tag, and @depends.
User input is more thoroughly validated, and sane should be overall
friendlier. The new definitions also allow for more predictable
behaviour, be easier to remember, and result in cleaner code.

Sane 7.0 is also magic: explicitly calling a function to run sane is no
longer necessarily required, as isn't specifying command line mode or
not (which, to be quite honest, was confusing and inelegant). Now
calling a @task or @cmd spawns and runs the tree, as one might expect.

The documentation was also completely re-written, and sane now includes
a manual with a full guide-by-example, and a proper reference for all of
the provided decorators, as well as some commentary on the internal
workings of sane.

The new code was written in a self-documenting style and should be
easier to understand.

---
## [meemofcourse/Shiptest](https://github.com/meemofcourse/Shiptest)@[0e6f7fa646...](https://github.com/meemofcourse/Shiptest/commit/0e6f7fa64649dfbf52b8e4b71756e6625e50fdd0)
#### Saturday 2023-06-24 20:37:57 by Imaginos16

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
## [EnglezosAOSP/android_frameworks_base](https://github.com/EnglezosAOSP/android_frameworks_base)@[2c02c4c4e7...](https://github.com/EnglezosAOSP/android_frameworks_base/commit/2c02c4c4e7e25b759233fcf2bb0ec21a594f82a7)
#### Saturday 2023-06-24 21:13:34 by Kuba Wojciechowski

core: Blacklist pixel system feature from Google Photos

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
## [freedoom/freedoom](https://github.com/freedoom/freedoom)@[99149fba2d...](https://github.com/freedoom/freedoom/commit/99149fba2d2dd99ff83cf304e80e1f49ae0affc3)
#### Saturday 2023-06-24 22:02:45 by mc776

levels: various minor fixes. (#990)

* levels: various fixes.

E1M2
Fixed some missing and misaligned textures around the secret lowering computer block.

E2M5
The red key bars could both be squeezed through and jumped around on a jump-enabling sourceport. The red key now raises the stairs instead, and the final door before the exit also requires a red key.

E2M7
Added one more bar in front of the exit to prevent squeeze glides.

E3M2
Expanded yellow key pillar so it would match the flat.

E3M6
Untagged the skylight inside the secret as being itself a secret.

E4M1
That line of health and armour bonuses just inside the big building would have a few floaters. They've all been moved forward and should be fully clear of that ledge.

Map05
The pit with the central column of water and the spectres was being blocked off by said spectres before the player could jump into it. There is now a monster blocking line right in front of the ledge, barely far enough to guarantee space for you to drop but close enough to let the pinkies bite.
You can now freely move through the gaps between any of the objects in the blue key room.
The exit from the blue key building now has a lift instead of stairs, and the wall prevents the nearest pinkies from seeing you until you've actually dropped inside. Hopefully this at least mitigates the problem of being stuck on the stairs with a pinkie right below your ability to target.
Miscellaneous aesthetic tweaks.

Map07
The lift overlooking the big arena was still suffering from monsters blocking from below. It has been moved to the side with an intervening ceiling.
The central grey aquatex nukage trim hub was a cross shape and the exits all had very strong lines turning right, making it look like a swastika. The southern section has been tweaked to throw off the symmetry and avoid that impression.
Made it possible to move all the way around the stack of crates in the eastern area with the switch.
Miscellaneous texture improvements.

Map08
The exit bars are now impossible to squeeze glide through. They are also styled in the same manner as the moving pistons by the big switches, giving the suggestion that they would be moved in a similar manner.

Map09
Fixed some floating pickups at the collapsed roof, the red key room, and the stairs to the warehouse admin area.
Shotgun guys in the admin area switch room are now situated between the deep cracks that were preventing their movement.

Map12
Turned the two wall-facing enemies around near (2016,96).
Added a second trigger line for the minigunner ambush store room so it happens even when you approach it from the other side.
Added a second switch for the bars normally opened before reaching the storage room ambush.
Replaced the BFG secret with a megasphere since you already get a BFG in Map11.

Map18
There were some lamps on the lower floor of the southwest room that were invisible from the higher floor but would block your movement. All major blockers have been deleted or moved to the edge of the room.
The tree near the red armour to the right of the start has been moved for similar reasons.

Map20
Moved some pickups (and the dead body) away from the bottom sides of the steps to reduce the chances of someone bypassing them while moving downwards.
Made the armour/health bonus placement more unambiguous around the cross and star.
Simplified the bridge around the red key so that the rising portion is only one sector.

Map22
Because this map has been disproportionately harder to pistol start than anything near it...
Moved all 4 player starts into the starting elevator to avoid a hot start.
Flagged some ammo pickups as appearing on all skill levels, as well as the southern super shotgun and the starting area armour. The easy-only SSG in the starting area is now a chaingun and appears on all skill levels.
The starting shotgun is now only available on easy, with two shotgunners (one of them guarding the armour) in its place on medium and hard.
Differentiated the walls of the starting elevator so you know which way to face, and made the switch resemble the normal (but broken) SW1TEK.
The switch system itself is simplified and given a simpler implied story: the big switch is broken, so you locate and use the backup system. The switch shooting is gone.
Made the fringe around the lava elevator go all the way around and populated it with health bonuses to make it clear you're actually expected to go down there, because frankly the original is so thoroughly obscured it looks like you're breaking sequence by exploiting an oversight in the map.
Extended the staircase down from the brown platform to mitigate the "pinkie right in front of you below your aim" effect.
Added a medikit near that brown platform.
The armour in the crate hall is now a medikit.

Map24
The hanging bodies in the red key room are now the non-blocking versions.
The trilobite stuck on the teleport pad in the square maze is now an octaminator so it doesn't get stuck.
The lines around the door leading to the serpentipedes with their backs to you no longer block sounds.
Removed the sound block flags on the octaminator ambush doors, so the pinkies can join in if you start shooting at them instead of powering through into the new room.

Map26
Health bonuses under crusher were floating.

Map27
Lizardbaby platform now has a full 72 unit clearance.
Spectres in the red rock area to the northeast are now in the tunnels and only come out when you land in the red water.

* levels: fix one screwy texture.

Monitor in the room west of the westmost shiny lowering shelf thing.

* levels: more minor fixes.

E2M1
Life surge secret was marked on the thin doorway, making it possible to fail to register even after you've taken the surge. The secret is now the room itself, at the cost of that random light effect.

E2M6
Life surge secret was marked on the thin central bit of the sigil, leaving *lots* of room to step around it while grabbing the powerup. (The fact that the red makes it kinda look like a hurtfloor really doesn't help.) The secret is now the larger room itself.

Map12
New eastern storage room trigger wasn't covering the entire hallway. It should also be diagonal to minimize the chance of it being skipped entirely.

Map28
The serps on the ledge by the bloodfalls and fleshy sigil were facing the wall and marked as ambush. They now face the actual play area.

Map29
Moved all the secret pit pickups a little bit further inside the square so they look like they're resting on the surface of the solid floor.

Map30
The multiplayer-only spawn pickups are now flagged as multi-only.

* levels: tiny map04 aesthetic tweak.

The fake contrast exaggerates the shadow on some "AGM" silver columns while eliminating the shadow on others. These are often right next to each other on the screen, producing absurd results. This moves 1 vertex from each affected line 2 pixels so they are no longer orthogonal.

---
## [Waseemq1235/tgstation](https://github.com/Waseemq1235/tgstation)@[835952ccf4...](https://github.com/Waseemq1235/tgstation/commit/835952ccf42af58db7238a572d7df6a9b8b2afd7)
#### Saturday 2023-06-24 22:33:50 by MrMelbert

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
## [TerraFirmaCraft/TerraFirmaCraft](https://github.com/TerraFirmaCraft/TerraFirmaCraft)@[b84519897d...](https://github.com/TerraFirmaCraft/TerraFirmaCraft/commit/b84519897d497ae0a4d747c00206b7442d46f077)
#### Saturday 2023-06-24 23:03:41 by EERussianguy

We knew the world would not be the same. A few people laughed, a few people cried, most people were silent. I remembered the line from the Hindu scripture, the Bhagavad-Gita; Vishnu is trying to persuade the Prince that he should do his duty and, to impress him, takes on his multi-armed form and says, "Now I am become Death, the destroyer of worlds." I suppose we all thought that, one way or another.
J. Robert Oppenheimer

---

