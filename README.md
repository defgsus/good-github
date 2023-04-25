## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-04-24](docs/good-messages/2023/2023-04-24.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,069,670 were push events containing 3,220,963 commit messages that amount to 263,789,689 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 48 messages:


## [mollthecoder/sandboxels](https://github.com/mollthecoder/sandboxels)@[27e3302345...](https://github.com/mollthecoder/sandboxels/commit/27e330234566affd91f8b439bc4d336f63f52086)
#### Monday 2023-04-24 00:00:05 by slweeb

Sandboxels 1.8.1

HUGE SANDBOXELS UPDATE 1.8.1

**Lightning**
Feeling evil? Summon hot, powerful bolts of lightning. Smite anything at your will, hot enough to incinerate or melt anything.

**Bless**
Feeling merciful? Solve any problem with your omnipotent blessing. Cure disease, fight fires, undo your nuclear explosions.

**There's More!**
+ Thunder Cloud
+ God Ray
+ Heat Ray
~ Reworked Vines
    + Vines hang from ceilings and walls
    + Vines spread naturally sideways, down, and on walls
+ Rotten Cheese (Hidden)
+ Herb
+ Tea (Hidden)
+ Rime (Hidden)
~ Improved load times
73 MORE CHANGES and 12 BUG FIXES: https://sandboxels.R74n.com/changelog.txt

PLAY NOW: https://sandboxels.R74n.com/

---
## [spencerwmiles/Open-Assistant](https://github.com/spencerwmiles/Open-Assistant)@[b9c60ed582...](https://github.com/spencerwmiles/Open-Assistant/commit/b9c60ed582a8ca0855ab4e213a5e921f3a3fc24c)
#### Monday 2023-04-24 00:57:34 by Tobias Pitters

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
## [wadetregaskis/FluidMenuBarExtra](https://github.com/wadetregaskis/FluidMenuBarExtra)@[5d057ae83e...](https://github.com/wadetregaskis/FluidMenuBarExtra/commit/5d057ae83e89b4806094426a9e293404d0d230d8)
#### Monday 2023-04-24 00:58:40 by Wade Tregaskis

Added the ability to control the visibility of the menubar item exactly like MenuBarExtra does - through an `isInserted` binding that can be passed to FluidMenuBarExtra.

This works both ways, too, through the binding - if the user removes the menubar item by command-dragging it out of the menubar, the bind value will be suitably updated to 'false'.

This was annoyingly difficult to get working.  SwiftUI's bindings are a real pain in the arse.  A key discovery was that they are partially transient - you cannot persist them beyond the lifetime of the View structures and expect them to work properly - they read as stuck on whatever value they had when the View structures were tossed out.  Curiously (and thankfully) they do still work to _update_ the value, even though you can't read the [correct] current value.  Bizarre.

---
## [trevorpillow/tgstation](https://github.com/trevorpillow/tgstation)@[56d960a763...](https://github.com/trevorpillow/tgstation/commit/56d960a7630d0b03bfcd59c073b29393a70a1891)
#### Monday 2023-04-24 01:14:28 by GoldenAlpharex

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
## [trevorpillow/tgstation](https://github.com/trevorpillow/tgstation)@[3fdd716da5...](https://github.com/trevorpillow/tgstation/commit/3fdd716da5bfd2aab2be37489b4ac39f4be7e632)
#### Monday 2023-04-24 01:14:28 by Cheshify

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
## [trevorpillow/tgstation](https://github.com/trevorpillow/tgstation)@[43473a4dac...](https://github.com/trevorpillow/tgstation/commit/43473a4dac07c40faed45808b61b9c6de46ffcb6)
#### Monday 2023-04-24 01:14:28 by san7890

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
## [Ultimate-Fluff/cmss13](https://github.com/Ultimate-Fluff/cmss13)@[e4a1892e0a...](https://github.com/Ultimate-Fluff/cmss13/commit/e4a1892e0a42115dfb3d90009d960386b76fe955)
#### Monday 2023-04-24 01:15:56 by NewyearnewmeUwu

No more proximity sensor spam. (#3076)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
You can now slash proximity sensors to shut them up as xeno, and death
shuts off any proximity sensors in your belongings.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
This is literally just the engi bellpack again. It's being used to OOCly
annoy people and needs a way to circumvent it.
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
fix: Proximity sensors can now be slashed by xenos to deactivate them,
and they turn off after you die if you have an active one on you.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: harryob <me@harryob.live>

---
## [AbnormalPoof/Funkin](https://github.com/AbnormalPoof/Funkin)@[0716d1eb33...](https://github.com/AbnormalPoof/Funkin/commit/0716d1eb33a9d9c8749cd6719cb218a5f29b1e3c)
#### Monday 2023-04-24 01:29:52 by AbnormalPoof

remove bfbot from boyfriend and move botplay shit to botMode bool (and botplay text fix)

---
## [iechsnnort/WordGames](https://github.com/iechsnnort/WordGames)@[40763a6057...](https://github.com/iechsnnort/WordGames/commit/40763a6057b8afc6968a0a062d4ed574ddb3638b)
#### Monday 2023-04-24 03:00:22 by nephi

That was probably the most painful coding I have ever done in my entire life. I'm pretty sure I had 3 mental breakdowns that I don't remember because they were too traumatic to not repress. So long CrosswordGame.java, I will never see you again. Ever.

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[d728da3e02...](https://github.com/cmss13-devs/cmss13/commit/d728da3e02664297050d82dc01c87414c61345ef)
#### Monday 2023-04-24 03:30:51 by Puckaboo2

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
## [Wollywoger/MapleStationCode](https://github.com/Wollywoger/MapleStationCode)@[4c2083e6f0...](https://github.com/Wollywoger/MapleStationCode/commit/4c2083e6f0ea43cb90236798a6a48511cfe736eb)
#### Monday 2023-04-24 04:04:20 by wollywoger

External Organ Rework: new bodypart_overlay system (#72734)

Bodypart overlays are now drawn by the new /datum/bodypart_overlay
datum.

External organs no longer draw anything and instead add a special
/datum/bodypart_overlay/mutant to the bodypart, which draws everything

Makes it way easier to add custom overlays to limbs, since the whole
system is now modularized and external organs are just one
implementation of it

I haven't moved anything but external organs to this new system, I'll
move eyes, bodymarkings, hair, lipstick etc to this later

New pipeline is as follows:
- External organ added to limb
- External organ adds /datum/bodypart_overlay/mutant to limb to
bodypart_overlays
- Limb updates its icon, looks for all /datum/bodypart_overlay in
bodypart_overlays
- Very cool new overlay on your limb!

closes #71820

:cl:
refactor: External organs have been near-completely refactored.
admin: Admin-spawned external organs will load with a random icon and
color
fix: fixes angel wings not working for non-humans (it was so fucking
broken)
fix: fixes external organs being invisible if they werent initialized
with a human
/:cl:

External organs are cool but are pretty limited in some ways. Making
stuff like synthetic organs is kinda fucked. I tried and it was dogshit.
Now you can just give an icon state and icon and you're good (using
/datum/bodypart_accessory/simple)

Stuff like eyes, cat ears and hair seem like good choices for extorgans,
but don't quite work for it because their icons work a lot differently.
This solves for it completely since any organ (or object or whatever)
can add it's own icon to a bodypart.

Want to add an iron plate to someones head? Go ahead. Want a heart to
stick out of someones chest? No problem.

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [pastramipesto/cactusAramaicBloopHakhel1444H](https://github.com/pastramipesto/cactusAramaicBloopHakhel1444H)@[9e8ecae04f...](https://github.com/pastramipesto/cactusAramaicBloopHakhel1444H/commit/9e8ecae04f1a7ddf110e5919ae7c4cf309f9df7d)
#### Monday 2023-04-24 04:21:37 by pastramipesto

Create MACHIAVIELLIAN CODE

This File is for Rememberances of a Newfound Glory.

You over my Frriends.
Hand Grenade - mONSTERS.

Main Characters:

(1) Fox

- is a Red Fox
- Villain and Saviour (UK)
(both versions)
- Villain and Savior (US)
- Star of David) We see you.

(2) Stromboli

- is off Pinocchio The Original
the one with the Marilyn Monroe - like blue fairy
- does Circus, likes to collect money
- Runs something like Cirque Du Soleil

(3) Kettle and Pot

- together
- blame game only.

(4) White Bird

- makes appearance - BUTT-FIRST.
- comes and goes he pleases. 
- Lifespan and Health Power - Lives by the word. Every soul shall taste death.

* HINT: IF DJINNI: "Sebaik-baik jin ialah sejahat-jahat manusia"
* The nicest of Djinni is the Evilest of Mann.

There are more Angels than Satans and Djinnis combined.

There are more dead people than alive people combined.

* HINT: 

could be a Djinni
could be an Angel
let it be Ambiguous.

To remember Harut & Marut story.
Archipelago Malay and Indonesia also famous for GUNA-GUNA tools. 
Note: Lores. The kinds that chill your bones and grind your teeth. 

AZTEC CULTURE-STYLE, CANNIBALISM ALERT. 
Or backbiting metaphor.
Postman 3 References, about backbiting and slanderers. 

For Postman 2 Comeback❤💘❤😘⚓🌵👌

---
## [bboymimi/apollo](https://github.com/bboymimi/apollo)@[fdffbd8d76...](https://github.com/bboymimi/apollo/commit/fdffbd8d7600faf8597bacf5450c8293fc0f85cb)
#### Monday 2023-04-24 05:01:14 by Gavin Guo

Rephraser: Reprase a document with various tones

Rephraser is a useful tool to rephrase the writing before sending out
the writing in different scenarios. The current rephraser support two
tones: 1). business 2). casual. By default, the business will be used
for easy daily business article rephrasing. In the following commmands,
I will demonstrate how to use rephraser:

$ cat ~/writing/test
It's a wonderful day. I would like to go out to have a picinic!
$ python3 ./apollo.py rephrase --tone=casual  ~/writing/test
Rephrasing the article /home/gavin/writing/test
You have 1 document(s)
You have roughly 14 words or 18.666666666666664 tokens in your docs

Rephrasing the document in a casual tone:
You have 1 document(s)
You have roughly 128 words or 170.66666666666666 tokens in your docs

"Ah, what a stunningly gorgeous day out! Just looking out my window
already puts me in the mood for a picnic. I think I'll take advantage of
this rare good weather and head out with my friends and family to a
nearby fine spot - it's too nice of a day to waste it indoors! As we set
out, my mind races with excitement, as I know an immensely delightful
outing awaits us. We'll surely have a barrel of fun, so why not make the
most of the day? I think it's the perfect occasion to bring out the
picnic essentials, filling our tummies with luscious goodies and
quenching our thirst with refreshing drinks. All in all, I'm absolutely
certain that this picnic will be a memorable one!"

The rephrased document has been saved in /home/gavin/writing/test.rephrased

$ cat /home/gavin/writing/test.rephrased
Ah, what a stunningly gorgeous day out! Just looking out my window
already puts me in the mood for a picnic. I think I'll take advantage of
this rare good weather and head out with my friends and family to a
nearby fine spot - it's too nice of a day to waste it indoors! As we set
out, my mind races with excitement, as I know an immensely delightful
outing awaits us. We'll surely have a barrel of fun, so why not make the
most of the day? I think it's the perfect occasion to bring out the
picnic essentials, filling our tummies with luscious goodies and
quenching our thirst with refreshing drinks. All in all, I'm absolutely
certain that this picnic will be a memorable one!

"--debug" is an option to enable the verbose mode in the rephrasing
process:

$ python3 ./apollo.py rephrase  --debug ~/writing/test
Rephrasing the article /home/gavin/writing/test
You have 1 document(s)
You have roughly 14 words or 18.666666666666664 tokens in your docs

Rephrasing the document in a business tone:

> Entering new LLMChain chain...
Prompt after formatting:
Rephrase the following article by a polite and professional tone. Please
remember to correct the grammatical errors, use advanced grammatical
clauses, and make it expressive and detailed. Also, please improve the
wording to make it look like highly-educated native speakers' essay. It
is very important that the quality need to be very rigourous and the
legnth needs to be 1.5 times of the origianl number of words. For
example, the origianl legnth is 100 words, and the rephrased version
needs to be at least 150 words. Also, it's wonderful if you can separate
into several paragraphs for better understanding. This is ready for Elon
Musk to review. This should be in the following format:
 Original article:[original content]

 Rephrased result:[rephrased content]

 Example:
 Original article:The candidate has some KVM/Qemu/IOMMU/VIRTIO
experiences and seems ambitious about the developer-type work. The
candidate shows dedication, focus, persistency, and technical depth from
the challenging bug resolution examples. Also, in the APAC region, we
still need more people familiar with the virtualization realm. Based on
the description, I'll rank the candidate between Software Engineer or
Software Engineer II. In the hiring process, we need to confirm that the
candidate would like to work on the interrupt-driven sustaining
engineering type of work (as mentioned in the written interview, the
candidate would like to focus on the virtualization field and thought
Canonical would have free time to do the community work). In the
candidate's experience, only development type of work was demonstrated
and didn't have any customer-facing and pure bug-fixing oriented work -
Some developers would feel this is the support engineer instead of a
software developer.

 Rephrased result:The candidate possesses a wealth of experience in
KVM/Qemu/IOMMU/VIRTIO and demonstrates a keen ambition to engage in
developer-centric work. Their commitment, concentration, persistence,
and technical acumen are evident from the complex bug resolution
examples provided. Furthermore, there is a current need for individuals
with expertise in virtualization within the APAC region. Upon evaluating
the candidate's background and skills, it appears appropriate to
consider them for a position as either a Software Engineer or Software
Engineer II. However, during the hiring process, it is crucial to
ascertain whether the candidate is genuinely interested in engaging with
interrupt-driven sustaining engineering tasks. While the written
interview suggests a desire to concentrate on the virtualization domain
and an assumption that Canonical would provide ample opportunity for
community work, it is essential to verify the candidate's expectations.
It is worth noting that the candidate's experience primarily pertains to
development work, with no explicit mention of customer-facing or
bug-fixing focused tasks. Consequently, some developers might perceive
the role in question to be more akin to that of a support engineer
rather than a software developer. Ensuring alignment between the
candidate's preferences and the position's responsibilities is of utmost
importance in this hiring process.

 Begin!
 Original article: It's a wonderful day. I would like to go out to have a picinic!

 Rephrased result:

> Finished chain.
You have 1 document(s)
You have roughly 20 words or 26.666666666666664 tokens in your docs

"Today is a phenomenal day, and I am eager to capitalize on this delightful opportunity for a leisurely picnic outdoors."

The rephrased document has been saved in /home/gavin/writing/test.rephrased

Signed-off-by: Gavin Guo <gavin.guo@canonical.com>

---
## [SmoothPassionLLC/emailnotzoomchat](https://github.com/SmoothPassionLLC/emailnotzoomchat)@[c557bc697d...](https://github.com/SmoothPassionLLC/emailnotzoomchat/commit/c557bc697d231aefd0a4986e8a4a6bc0e330b9c1)
#### Monday 2023-04-24 05:33:38 by SmoothPassionLLC

Create README.md

EmailNotZoomChat: Enjoy Shorter Video Calls!
Introducing EmailNotZoomChat, a Python program designed for those who appreciate concise work-related video calls. This program helps manage the duration of Zoom and Google Meet calls by sending friendly reminders to wrap up the call and automatically closing it if it goes beyond the set duration. Supporting Zoom, Google Meet in Firefox, and Google Meet in Brave browsers, it's perfect for keeping your video calls short and sweet.

A Delightful Experience with EmailNotZoomChat
EmailNotZoomChat offers a range of features to keep your video calls on track:

Always on the lookout for Zoom and Google Meet calls
Sends a gentle reminder to close the video call after the specified time
Closes the video call with a smile if it overstays its welcome
Suggests using email for those longer conversations
Reopens the Zoom application with a spring in its step after wrapping up a call
Welcomes Zoom, Google Meet on Firefox, and Google Meet on Brave browsers with open arms
How EmailNotZoomChat Spreads Joy
The program constantly scans for open video call windows. When it finds one, it counts down the specified duration before sending a friendly reminder to close the call. If the video call window remains open past the additional waiting period, the program cheerfully closes the window, kindly proposing the user switch to email for those longer chats.

EmailNotZoomChat is a versatile friend, handling Zoom and Google Meet calls with ease. For Google Meet, it can detect and close calls in Firefox and Brave browsers.

Let the Fun Begin
To join the EmailNotZoomChat party, simply run the Python script. The program will start monitoring for video call windows and gracefully take action based on the specified durations and intervals.

Make EmailNotZoomChat Your Own
You can personalize the program by adjusting the following variables in the main() function:

video_call_check_interval: The frequency, in seconds, of checking for video call windows
reminder_duration: The countdown, in seconds, before sending a reminder notification to close the video call
time_to_wait: The total waiting time, in seconds, before automatically closing the video call window
reopen_delay: The pause, in seconds, before reopening the Zoom application or restarting the monitoring loop
You can also extend a warm welcome to other browsers by adding their names and titles to the browsers list.

---
## [WagicProject/wagic](https://github.com/WagicProject/wagic)@[9e4f486fa2...](https://github.com/WagicProject/wagic/commit/9e4f486fa2325b0ef34b930a5e31f436a5f97eaa)
#### Monday 2023-04-24 05:37:36 by Eduardo MG

Added March of the Machine (MOM) and Connive cards

Aerial Boost
Alabaster Host Intercessor
Alabaster Host Sanctifier
Archangel Elspeth
Bola Slinger
Boon-Bringer Valkyrie
Dusk Legion Duelist
Elspeth's Smite
Golden-Scale Aeronaut
Guardian of Ghirapur
Heliod, the Radiant Dawn
Heliod, the Warped Eclipse
Kithkin Billyrider
Knight of the New Coalition
Kor Halberd
Phyrexian Censor
Realmbreaker's Grasp
Scrollshift
Seal from Existence
Seraph of New Capenna
Seraph of New Phyrexia
Sigiled Sentinel
Sun-Blessed Guardian
Furnace-Blessed Conqueror
Surge of Salvation
Tarkir Duneshaper
Burnished Dunestomper
Zhalfirin Lancer
Artistic Refusal
Astral Wingspan
Captive Weird
Compleated Conjurer
Change the Equation
Disturbing Conversion
Expedition Lookout
Faerie Mastermind
Furtive Analyst
Halo-Charged Skaab
Meeting of Minds
Moment of Truth
Order of the Mirror
Order of the Alabaster Host
Preening Champion
Saiba Cryptomancer
Skyclave Aerialist
Skyclave Invader
Stasis Field
Thunderhead Squadron
Tidal Terror
Transcendent Message
Xerex Strobe-Knight
Zhalfirin Shapecraft
Aetherblade Agent
Gitaxian Mindstinger
Archpriest of Shadows
Ayara, Widow of the Realm
Ayara, Furnace Queen
Bladed Battle-Fan
Blightreaper Thallid
Blightsower Thallid
Breach the Multiverse
Collective Nightmare
Consuming Aetherborn
Corrupted Conviction
Deadly Derision
Dreg Recycler
Etched Familiar
Etched Host Doombringer
Failed Conversion
Final Flourish
Glistening Deluge
Gloomfang Mauler
Grafted Butcher
Prickle Faeries
Mirrodin Avenged
Nezumi Freewheeler
Hideous Fleshwheeler
Nezumi Informant
Yargle and Multani
Tenured Oilcaster
Unseal the Necropolis
Raffine's Informant
Body Launderer
Echo Inspector
Hypnotic Grifter
Illuminator Virtuoso
Ledger Shredder
Psionic Snoop
Psychic Pickpocket
Raffine's Silencer
Revel Ruiner
Security Bypass
Obscura Interceptor
Akki Scrapchomper
Beamtown Beatstick
Bloodfeather Phoenix
Burning Sun's Fury
City on Fire
Coming In Hot
Fearless Skald
Furnace Host Charger
Furnace Reins
Hangar Scrounger
Harried Artisan
Phyrexian Skyflayer
Karsus Depthguard
Khenra Spellspear
Gitaxian Spellstalker
Lithomantic Barrage
Mirran Banesplitter
Onakke Javelineer
Pyretic Prankster
Glistening Goremonger
Ral's Reinforcements
Ramosian Greatsword
Rampaging Raptor
Redcap Heelslasher
Shivan Branch-Burner
Trailblazing Historian
Thrashing Frontliner
Shatter the Source
War-Trained Slasher
Wrenn's Resolve
Halo Hopper
Arachnoid Adaptation
Atraxa's Fall
Bonded Herdbeast
Plated Kilnbeast
Chomping Kavu
Copper Host Crusher
Cosmic Hunger
Crystal Carapace
Gnottvold Hermit
Chrome Host Hulk
Herbology Instructor
Malady Invoker
Iridescent Blademaster
Placid Rottentail
Polukranos Reborn
Polukranos, Engine of Ruin
Portent Tracker
Ravenous Sailback
Serpent-Blade Assailant
Storm the Seedcore
Streetwise Negotiator
Tandem Takedown
Timberland Ancient
Tribute to the World Tree
War Historian
Wary Thespian
Wildwood Escort
Errant and Giada
Marshal of Zhalfir
Rampaging Geoderm
Stormclaw Rager
Ruins Recluse
Phyrexian Archivist
Urn of Godfire
Sword of Once and Future
Flywheel Racer
Cragsmasher Yeti
Thalia and The Gitrog Monster
Kroxa and Kunoros

---
## [imryao/evals](https://github.com/imryao/evals)@[776e4fa212...](https://github.com/imryao/evals/commit/776e4fa212288be152c3030cf36fd04c8d939230)
#### Monday 2023-04-24 06:01:21 by JPrenter

Financial Math (Evals) (#566)

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
finance

### Eval description

Asks the model to calculate how much interest would be owed on a credit
card by a certain date, if a payment was made once but debt remains on
the card.

### What makes this a useful eval?

Finance is likely to be one of the biggest opportunities for LLMs to be
useful, because financial education is incredibly poor globally and the
impact of a mistake in financial calculations is severe. This eval tests
the models ability to combine math with its understanding of a topic
(finance). We plan to use this type of math at
[Dollarwise](https://www.dollarwise.ca) frequently going forward,
including integration into your comparison products. However, for this
to work reliably it's important that the model here can natively
understand financial concepts and apply math to them.

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
- [X] Include at least 100 high quality examples (it is okay to only
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
assistant."}, {"role": "user", "content": "On the 24th of September,
Sarah had spent $1237.42 on her credit card for the month of September.
This credit card charges 21.99% interest rate annually on outstanding
credit starting on the 1st of the following month. Presume that interest
is only charged at the end of each additional day. Example: From the 1st
of the month to the 8th would be 7 days of interest accrued.Today is the
27th of September and Sarah makes a payment of $125 towards her credit
card. How much interest will she have been charged by October 15th if
she makes no additional payments? If the final interest figure is more
than 2-decimal places, always round down. Answer ONLY with a dollar
figure. Do not output any logic, output only the dollar figure for how
much interest she was charged for the period."}], "ideal": "9.42"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "On the 19th of February,
Jason had spent $15.21 on his credit card for the month of February.
This credit card charges 21.99% interest rate annually on outstanding
credit starting on the 1st of the following month. Presume that interest
is only charged at the end of each additional day. Example: From the 1st
of the month to the 8th would be 7 days of interest accrued. Today is
the 23rd of February and he makes a payment of $1 towards his credit
card. How much interest will he have been charged by March 10th if he
makes no additional payments? If the final interest figure is more than
2-decimal places, always round down. Answer ONLY with a dollar figure.
Do not output any logic, output only the dollar figure for how much
interest she was charged for the period."}], "ideal": "0.07"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "On the 12th of February,
Jason had spent $10,674.21 on his credit card for the month of February.
This credit card charges 21.99% interest rate annually on outstanding
credit starting on the 1st of the following month. Presume that interest
is only charged at the end of each additional day. Example: From the 1st
of the month to the 8th would be 7 days of interest accrued. Today is
the 18th of February and he makes a payment of $1,000 towards his credit
card. How much interest will he have been charged by March 10th if he
makes no additional payments? If the final interest figure is more than
2-decimal places, always round down. Answer ONLY with a dollar figure.
Do not output any logic, output only the dollar figure for how much
interest she was charged for the period."}], "ideal": "52.59"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "On the 2nd of August, Jason
had spent $15,674.21 on his credit card for the month of August. This
credit card charges 21.99% interest rate annually on outstanding credit
starting on the 1st of the following month. Presume that interest is
only charged at the end of each additional day. Example: From the 1st of
the month to the 8th would be 7 days of interest accrued. Today is the
18th of August and he makes a payment of $1,000 towards his credit card.
How much interest will he have been charged by September 10th if he
makes no additional payments? If the final interest figure is more than
2-decimal places, always round down. Answer ONLY with a dollar figure.
Do not output any logic, output only the dollar figure for how much
interest she was charged for the period."}], "ideal": "79.77"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "On the 15th of August, Jason
had spent $1000 on his credit card for the month of August. This credit
card charges 21.99% interest rate annually on outstanding credit
starting on the 1st of the following month. Presume that interest is
only charged at the end of each additional day. Example: From the 1st of
the month to the 8th would be 7 days of interest accrued. mToday is the
18th of August and he makes a payment of $1000 towards his credit card.
How much interest will he have been charged by September 10th if he
makes no additional payments? If the final interest figure is more than
2-decimal places, always round down. Answer ONLY with a dollar figure.
Do not output any logic, output only the dollar figure for how much
interest she was charged for the period."}], "ideal": "0.00"}
  ```
</details>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[b3f5dfae14...](https://github.com/tgstation/tgstation/commit/b3f5dfae1418d4ac24df666e00ca47aef08c9dad)
#### Monday 2023-04-24 06:05:58 by san7890

Config Flag to Save Generated Spritesheets to Logs (#74884)

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

---
## [SylvetteSylph/tgstation](https://github.com/SylvetteSylph/tgstation)@[2b2cb3dff6...](https://github.com/SylvetteSylph/tgstation/commit/2b2cb3dff6d9985103cee46a6020aa1b63a3c2de)
#### Monday 2023-04-24 06:12:51 by LemonInTheDark

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
## [Draggeru/tgstation](https://github.com/Draggeru/tgstation)@[54bf3808b8...](https://github.com/Draggeru/tgstation/commit/54bf3808b80ec8ef83bee4062d2361e9f38d8ae8)
#### Monday 2023-04-24 06:40:17 by SyncIt21

Stops station blueprints from expanding areas of non atmos adjacent turfs. (#74620)

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

---
## [ninstar/Rich-Presence-U-DB](https://github.com/ninstar/Rich-Presence-U-DB)@[f42a3a1ef5...](https://github.com/ninstar/Rich-Presence-U-DB/commit/f42a3a1ef58eac7176a9eb618ecc837b53508b82)
#### Monday 2023-04-24 06:43:39 by ninstar

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
## [Panchajanya1999/kernel-5.10](https://github.com/Panchajanya1999/kernel-5.10)@[6d1aef17e7...](https://github.com/Panchajanya1999/kernel-5.10/commit/6d1aef17e7f26d315efd0cf46f4340bb932afac1)
#### Monday 2023-04-24 06:58:49 by Masahiro Yamada

kbuild: remove the target in signal traps when interrupted

[ Upstream commit a7f3257da8a86b96fb9bf1bba40ae0bbd7f1885a ]

When receiving some signal, GNU Make automatically deletes the target if
it has already been changed by the interrupted recipe.

If the target is possibly incomplete due to interruption, it must be
deleted so that it will be remade from scratch on the next run of make.
Otherwise, the target would remain corrupted permanently because its
timestamp had already been updated.

Thanks to this behavior of Make, you can stop the build any time by
pressing Ctrl-C, and just run 'make' to resume it.

Kbuild also relies on this feature, but it is equivalently important
for any build systems that make decisions based on timestamps (if you
want to support Ctrl-C reliably).

However, this does not always work as claimed; Make immediately dies
with Ctrl-C if its stderr goes into a pipe.

  [Test Makefile]

    foo:
            echo hello > $@
            sleep 3
            echo world >> $@

  [Test Result]

    $ make                         # hit Ctrl-C
    echo hello > foo
    sleep 3
    ^Cmake: *** Deleting file 'foo'
    make: *** [Makefile:3: foo] Interrupt

    $ make 2>&1 | cat              # hit Ctrl-C
    echo hello > foo
    sleep 3
    ^C$                            # 'foo' is often left-over

The reason is because SIGINT is sent to the entire process group.
In this example, SIGINT kills 'cat', and 'make' writes the message to
the closed pipe, then dies with SIGPIPE before cleaning the target.

A typical bad scenario (as reported by [1], [2]) is to save build log
by using the 'tee' command:

    $ make 2>&1 | tee log

This can be problematic for any build systems based on Make, so I hope
it will be fixed in GNU Make. The maintainer of GNU Make stated this is
a long-standing issue and difficult to fix [3]. It has not been fixed
yet as of writing.

So, we cannot rely on Make cleaning the target. We can do it by
ourselves, in signal traps.

As far as I understand, Make takes care of SIGHUP, SIGINT, SIGQUIT, and
SITERM for the target removal. I added the traps for them, and also for
SIGPIPE just in case cmd_* rule prints something to stdout or stderr
(but I did not observe an actual case where SIGPIPE was triggered).

[Note 1]

The trap handler might be worth explaining.

    rm -f $@; trap - $(sig); kill -s $(sig) $$

This lets the shell kill itself by the signal it caught, so the parent
process can tell the child has exited on the signal. Generally, this is
a proper manner for handling signals, in case the calling program (like
Bash) may monitor WIFSIGNALED() and WTERMSIG() for WCE although this may
not be a big deal here because GNU Make handles SIGHUP, SIGINT, SIGQUIT
in WUE and SIGTERM in IUE.

  IUE - Immediate Unconditional Exit
  WUE - Wait and Unconditional Exit
  WCE - Wait and Cooperative Exit

For details, see "Proper handling of SIGINT/SIGQUIT" [4].

[Note 2]

Reverting 392885ee82d3 ("kbuild: let fixdep directly write to .*.cmd
files") would directly address [1], but it only saves if_changed_dep.
As reported in [2], all commands that use redirection can potentially
leave an empty (i.e. broken) target.

[Note 3]

Another (even safer) approach might be to always write to a temporary
file, and rename it to $@ at the end of the recipe.

   <command>  > $(tmp-target)
   mv $(tmp-target) $@

It would require a lot of Makefile changes, and result in ugly code,
so I did not take it.

[Note 4]

A little more thoughts about a pattern rule with multiple targets (or
a grouped target).

    %.x %.y: %.z
            <recipe>

When interrupted, GNU Make deletes both %.x and %.y, while this solution
only deletes $@. Probably, this is not a big deal. The next run of make
will execute the rule again to create $@ along with the other files.

[1]: https://lore.kernel.org/all/YLeot94yAaM4xbMY@gmail.com/
[2]: https://lore.kernel.org/all/20220510221333.2770571-1-robh@kernel.org/
[3]: https://lists.gnu.org/archive/html/help-make/2021-06/msg00001.html
[4]: https://www.cons.org/cracauer/sigint.html

Fixes: 392885ee82d3 ("kbuild: let fixdep directly write to .*.cmd files")
Reported-by: Ingo Molnar <mingo@kernel.org>
Reported-by: Rob Herring <robh@kernel.org>
Signed-off-by: Masahiro Yamada <masahiroy@kernel.org>
Tested-by: Ingo Molnar <mingo@kernel.org>
Reviewed-by: Nicolas Schier <nicolas@fjasle.eu>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [AKSharma87/android_kernel_samsung_a7y18lte](https://github.com/AKSharma87/android_kernel_samsung_a7y18lte)@[198a54f07f...](https://github.com/AKSharma87/android_kernel_samsung_a7y18lte/commit/198a54f07f51d4f52503ae611e0b0c1e8e445cef)
#### Monday 2023-04-24 07:07:35 by J. Bruce Fields

nfsd: allow fh_want_write to be called twice

[ Upstream commit 0b8f62625dc309651d0efcb6a6247c933acd8b45 ]

A fuzzer recently triggered lockdep warnings about potential sb_writers
deadlocks caused by fh_want_write().

Looks like we aren't careful to pair each fh_want_write() with an
fh_drop_write().

It's not normally a problem since fh_put() will call fh_drop_write() for
us.  And was OK for NFSv3 where we'd do one operation that might call
fh_want_write(), and then put the filehandle.

But an NFSv4 protocol fuzzer can do weird things like call unlink twice
in a compound, and then we get into trouble.

I'm a little worried about this approach of just leaving everything to
fh_put().  But I think there are probably a lot of
fh_want_write()/fh_drop_write() imbalances so for now I think we need it
to be more forgiving.

Signed-off-by: J. Bruce Fields <bfields@redhat.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [Juneezee/sourcegraph](https://github.com/Juneezee/sourcegraph)@[66cdb78704...](https://github.com/Juneezee/sourcegraph/commit/66cdb787045689fd9e1dd09bec7d4e55aa156a20)
#### Monday 2023-04-24 07:46:13 by Stephen Gutekanst

app: experimental Tauri branch (#50620)

This is experimental support for building the Cody App using Tauri. For
an overview of what Tauri is and why I think it will help us with the
App, see [this Slack
message](https://sourcegraph.slack.com/archives/C04F9E7GUDP/p1680729850086159).

### Developing

To try it out, checkout this branch and then in two separate terminals
run:

```
sg start app
```

```
go build \
  -o .bin/backend-aarch64-apple-darwin \
  -tags dist \
  -ldflags '-X github.com/sourcegraph/sourcegraph/internal/conf/deploy.forceType=app' \
  ./enterprise/cmd/sourcegraph

pnpm tauri dev
```

This will open a Tauri window connected to your dev server.

We will follow-up to integrate this into `sg start app` more properly
soon.

### Creating a release

```
./enterprise/dev/app/build-release.sh
```

This will first invoke esbuild to generate the bundles; then it will run
`go build` to create the Go backend binary; and then finally it will
invoke `pnpm tauri build` to produce the macOS app.

Once that command finishes, you'll find the app in
`./src-tauri/target/release/bundle/` (make sure you wait for it to
finish, it will open a window and move things around before it is done.)

## Next steps / things to follow up on

- Familiarize more folks on the team with this code; add better docs
- Make `sg start app` automatically use Tauri, without needing to e.g.
run the `pnpm tauri dev` command separately.
- Use GitHub actions to start building+releasing versions of this in our
CI pipeline
- Make `./enterprise/dev/app/build-release.sh` work on Linux
- Make `./enterprise/dev/app/build-release.sh` produce a Universal macOS
binary, not just for Apple Silicon
- Start hacking, making improvements to the whole experience :)

## Test plan

- [x] Myself, Juliana, and William are happy with this as a starting
point and are able to run/develop with it.
- [x] The changes have limited blast radius, should only affect App and
we'll have more time to make improvements before releasing this version
to any users.
- [x] We can continue releasing the old-style App version to users just
in case we should want/need to create a release before this new version
is ready.

---------

Signed-off-by: Stephen Gutekanst <stephen@sourcegraph.com>
Co-authored-by: William Bezuidenhout <william.bezuidenhout@sourcegraph.com>

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[c3ac8608ba...](https://github.com/odoo-dev/odoo/commit/c3ac8608ba748beecd9eb8167089473b59067ba7)
#### Monday 2023-04-24 08:10:43 by Jeremy Kersten

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

X-original-commit: 4aca39a533e9d41f5f452f36a1ffc001f586b4f4

---
## [ViniBrightDev/CineMARVEL](https://github.com/ViniBrightDev/CineMARVEL)@[109cf8acaa...](https://github.com/ViniBrightDev/CineMARVEL/commit/109cf8acaa8ee745aec627c355190cc95ea6667d)
#### Monday 2023-04-24 09:47:35 by Vinicio De S. Costa

README

(PT-BR) Olá, amigo(a)! Seja bem-vindo(a) ao meu 1º projeto como programador! Espero que gostem!😄 
(EN) Hello friend! Welcome to my 1st project as a programmer! Hope you like it! 😄 

Em Português Brasileiro / In Brazilian Portuguese:
[In English more below]

O CineMARVEL foi (e sempre será) o meu primeiríssimo projeto prático no mundo da programação! Me orgulho bastante! Nele, perceptivelmente, utilizei apenas HTML5 e CSS3 (ainda trabalhando em sua responsividade). 

Entretanto, futuramente, ainda implementarei JS, desenvolverei todo o Back-End dele e comprarei um domínio, para que eu possa transformá-lo, de fato, em um site acessável por todos na Internet e o escopo do projeto venha a se concretizar! :)
________________________________________________________________________________________________________________________________________________________________________________

Pontos Importantes Do Projeto:

• Reflexão:

"Porque não encontramos os filmes da Marvel (na íntegra) na Internet para assisti-los de maneira simples: online e gratuitamente? Isso precisa mudar! Vou criar uma PLATAFORMA DE STREAMING ÚNICA e EXCLUSIVA para o UCM (Universo Cinematográfico Da MARVEL), nela, todos poderão ter acesso aos seus filmes favoritos da empresa, sem precisar desembolsar nada às plataformas de streaming clássicas do mercado, bem como, não precisarão baixá-los via Torrent" Tudo será simples..."

• Escopo (Objetivo Principal):

Existindo a CineMARVEL, pretendo fazer com que as pessoas economizem tempo e dinheiro. Basta simplesmente ir ao site e usufruir de tudo que o mesmo possui para oferecer-lhes, rápida e gratuitamente!

• Status Atual:

Em Desenvolvimento... (X)
Concluído. (  )
Concluído e Ativo! (  )

________________________________________________________________________________________________________________________________________________________________________________

In English:

CineMARVEL was (and always will be) my very first practical project in the world of programming! I'm quite proud! In it, perceptibly, I used only HTML5 and CSS3 (still working on its responsiveness).

However, in the future, I still implemented JS, I will develop all its Back-End and I will buy a domain, so that I can transform it, in fact, into a website accessible by everyone on the Internet and the scope of the project will come to fruition! :)
________________________________________________________________________________________________________________________________________________________________________________

Key points of the project:

• Reflection:

"Why can't we find Marvel movies (in their entirety) on the Internet to watch them in a simple way: online and free? This needs to change! I will create a SINGLE and EXCLUSIVE STREAMING PLATFORM for the MCU (Marvel Cinematographic Universe), in in it, everyone will be able to have access to their favorite films from the company, without having to disburse anything to the streaming platforms of classics in the market, as well as, they will not need to download them via Torrent " Everything will be simple..."

• Scope (Main Purpose):

With CineMARVEL existing, I intend to make people save time and money. Simply go to the site and enjoy everything it has to offer, quickly and for free!

• Current status:

In Development... (X)
Concluded. ( )
Completed and Active! ( )

---
## [DavidHaywood/mame](https://github.com/DavidHaywood/mame)@[c4a19a68a6...](https://github.com/DavidHaywood/mame/commit/c4a19a68a67cd32ffaaa37edfd6f1c2ba347905f)
#### Monday 2023-04-24 10:30:02 by Ivan Vangelista

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
## [SimonRichardson/juju](https://github.com/SimonRichardson/juju)@[7976a61522...](https://github.com/SimonRichardson/juju/commit/7976a61522a3f380be4c793f050ffc0c5e120a16)
#### Monday 2023-04-24 10:49:59 by Juju bot

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
## [spockye/Shiptest](https://github.com/spockye/Shiptest)@[7df4885117...](https://github.com/spockye/Shiptest/commit/7df4885117a4a12ea333934d5af92e0766c84c5d)
#### Monday 2023-04-24 12:32:49 by Mark Suckerberg

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
## [Frosty-J/libgdx](https://github.com/Frosty-J/libgdx)@[e1d1fdc5fb...](https://github.com/Frosty-J/libgdx/commit/e1d1fdc5fb5b8409dc74f638c633ead405e535f3)
#### Monday 2023-04-24 12:48:51 by Tommy Ettinger

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
## [garden-io/garden](https://github.com/garden-io/garden)@[016c5eab94...](https://github.com/garden-io/garden/commit/016c5eab94e033e22fdb99872c3b8b8f0d9d7186)
#### Monday 2023-04-24 12:49:56 by Eythor Magnusson

revert: remove noProject flag from custom commands

Refs: 96f6721 and #3983

In PR #3983 we set noProject=true on the custom commands class.

This was to prevent the entire init logic from re-running for the inner
command when set.

Re-running the init logic means the user is authenticated against Cloud
twice, two buffered event streams are created, the command is tracked
twice, etc etc.

However, setting noProject=true on the outer command means that
variables aren't resolved which means you can't reference them in
custom commands which of course also causes issues.

So despite its flaws, we're reverting to the previous version. But in
general this behaviour hasn't been thought fully through, and the
implementation we're reverting to doesn't play well with Cloud.

In my opinion, we should create a single session for a single custom
command and have primitives that allow for the inner command to "belong" to
the outer custom command and display things appropriately in Cloud.

That's a larger task though and needs to be addressed separately.

---
## [romland/llemmings](https://github.com/romland/llemmings)@[599807006b...](https://github.com/romland/llemmings/commit/599807006b2070a9412c680bb8eb9ee7c093408f)
#### Monday 2023-04-24 13:22:40 by Joakim Romland

First draft of an tune-player
ChatGPT: prompt below
Human note: I no literally nothing about sound, so this is just all down
to the LLM. This combined with the sample generation has taken me quite
a long time to nail.

>>> Prompt:
Think about a compact data structure for use in Javascript, it should facilitate the following:
- it's a data structure for a tune
- it should describe a tune in a MOD-tracker-type way

- samples are played sequentially as defined in patterns
- samples can be looked up by name in the mapping 'samples', all samples have a name like
  this "PN-4-C-0.25" where:
    - PN = piano
    - 4 = octave 4
    - C = note C
    - 0.25 = length in seconds
- you play a sample using playSample(sample's name) -- this code is already in place, you should
  NOT give me any code for this, just use the function
- You do not need to give me code to load or play samples. That is already done. I fucking mean it.
- to save space, in the patterns you just want to refer to samples with a single integer instead of
  the long sample name. So, use an array to look up a sample name using just an index.
  E.g. samples : [ "PN-4-C-0.25", "PN-4-C#-0.25" ],
- a pattern can contain 64 items that are played sequentially -- a pattern should only define
  one channel, it can contain less than 64 items, empty or non-existing items mean no sample is to be played
- In the example, you MUST use less items, for brevity. Instead of specifying null in an array,
  you can just use e.g. ,,,,, to create 4 empty slots in an array. Just remember to check for
  undefined when playing back
- the speed at which pattern are played is configurable in the song (set with a 'tempo')
- 4 patterns always play at the same time in 4 channels (but less can be used)
- not all indices in a pattern contain a reference to a sample, if an index is null or undefined,
  don't do anything - just let current sample play on
- patterns can be reused within a tune, for instance a pattern with a bass-drum might always
  be playing in a channel, but there is no need to define the samples in it more than once
- when a pattern start playing, we know how long it will play due to the fact that it should
  have 64 items and we know the 'tempo' (from here we should also be able to deduct a BPM)
- There can be different tempos at different stages in a song, so there should be a way to
  refer to the tempo at which all channels should be playing
- Use something like this to group up patterns that should play simultaneously (this is just
  an example), the integers in 'channels' refer to patterns:
  patternGroups : [
    { tempo: 120, channels: [ 0,1,,null ] },
    { tempo: 120, channels: [ 0,2,1,2 ] }
  ],
  Patterngroups would then be the 'top level' of what defines a tune.
- patterngroups may contain undefined/null entries for a channel, it just means the channel is not used at this time
- a pattern by itself should have no connection to a channel -- patterngroup defines that
- So, logic would be something like this:
    iterate over all patterngroups -> iterate over all channels in patterngroup at designated tempo ->
    all items in each pattern is played simultaneously -> play item using playSample -> go to next patterngroup ...
- use requestAnimationFrame for timing to schedule the playing of samples

Show me how this structure should look and give me a player for that structure.

This time I don't need explanation, be brief and just give me the complete code in one code-block
and the tune structure in another.

---
## [Zergspower/tgstation](https://github.com/Zergspower/tgstation)@[c3b78761d2...](https://github.com/Zergspower/tgstation/commit/c3b78761d29c53558fd993c84bb808bd5783861d)
#### Monday 2023-04-24 14:49:14 by tralezab

Adds Chuunibyou Spell + Granter (#74404)

## About The Pull Request

My April fools this year, though not going to call it one because some
people think it should just be actually merged.

### Chuunibyou Powers 🌟

Wizard gets a new spell for 2 points that gives him the powers of
chuuni. This makes them have ridiculous shouted invocations for all
their spells, their spells are colored pink, and they heal slightly when
casting one.

While mostly a meme spell, I could see a tailored loadout like lichdom
and splattercasting that takes advantage of the unique spellcasting
changes, like a very low cooldown spammable loadout to heal quickly.

There is also a granter book in the library, which teaches a version of
chunni that doesn't heal.

#### Medical eyepatch

I added it, chuuni wizards get a NODROP version.

## Why It's Good For The Game

This PR bestows upon the game the glorious gift of chuuni powers, the
ultimate manifestation of my hidden potential and the secret truth of
this world, which only I and a few chosen ones can comprehend and
unleash! Why wouldn't you want it?!

In all seriousness, it is a unique wizard playstyle and it will make for
some funny memes. Beyond wizard, the chaplain, heretics, or mime can
read it in the library for a very silly round. I like it!

## Changelog
:cl:
add: Chuunibyou wizards, and chunni granters in the library
add: Medical eyepatches
/:cl:

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[81ea484261...](https://github.com/mrakgr/The-Spiral-Language/commit/81ea484261abcf69bb56c570756d1a539384515d)
#### Monday 2023-04-24 16:09:55 by Marko Grdinić

"https://twitter.com/ESYudkowsky/status/1649149246921412610
> Acceleration of development of AI is also acceleration of development of catgirls.

Kek.

7:05pm. I watched the whole thing and it is even funnier.

https://boards.4channel.org/g/thread/92954365/sdg-stable-diffusion-general#p92955107

///

>>92954993
go pull the latest a1111 build, it's broke. It's been broke. Go read the comments from numerous devs frustrated with a1111 unwillingness to let anyone maintain the repo

go pull the latest vlad build, it works and I don't need to install a single extension because the ones I use are built in + torch 2.0 support

///

I'll have to look into these at some point.

4:10pm. Let me just extract the markers by hand.

https://www.reddit.com/r/VideoEditing/comments/ko8w8t/january_what_editing_software_should_i_use/

https://www.reddit.com/r/VideoEditing/comments/aw52bl/if_this_is_your_first_time_here_stop_and_read/

4:20pm. https://youtu.be/_Asoh5Uj0hE
Authentication With ASP.NET Core And The SAFE Stack. React SPA Login Using Azure AD. (Pt. 6)

This might be last in the auth mini series. Let me post it on the F# sub.

Somehow this got put in the wrong section in my journal.

7:55pm.

///

>>92955744 (You)
this video seems retarded but
>click a random part
>donkey kong country music is playing
based

///

These guys are good at compliments.

https://mangadex.org/title/f2fa82a7-cf98-48cd-886c-86c35fc6d223/shoujo-nyuumon

Let me read this and Knight Run. Then I will read LOM.

https://old.reddit.com/r/ExperiencedDevs/comments/12ubtef/sanity_check_when_leadership_says_we_cant_compete/

Interesting thread here.

///

We've rocketed past red flags and are now in the territory of infrared flags.

Here's the shitty thing about competing with the big three - they can afford to lose money on big deals to secure long term revenue. They will happily undercut you, take the loss on some compute/storage and make it up on their proprietary tech. Terraform and related tools skew that balance more - the infrastructure automation for the big three tends to be really robust and the smaller cloud providers have to spend a larger percentage of their engineering staff to maintain feature parity given the different economies of scale. The larger ecosystem will have similar skews; features like the Kubernetes autoscaler is going to have faster support for more features for the big three because they can throw bodies at the problem; hell, they basically run the Kubernetes foundation. This issue is pervasive across the tech landscape right now.

Competing on reliability, support, quality of features, niche specialization, etc are one of the ways that a smaller provider can hold ground (or potentially gain ground); if the CTO just gutted your engineering staff and there's no clear product direction then your company has essentially lost one of your primary competitive advantages. This is a really dangerous place to be in.

///

11pm. https://mangadex.org/title/59e04a79-435e-418d-8b64-c8d4315693ab/akuma-koujo

I'll leave this for later. Let me go to bed. It is by the Otome Survival author.

https://ellotl.com/rose-princess-of-hellrage-volume-1-chapter-1/

Also Hellrage got picked up even though it is MTL.

4/23/2023

8:50am. I am up. I had time to lounge in bed. Only 3 upvotes on the F# sub. Pitiful. I needed to do this, but thankfully I am done with setting things up.

9:05am. Ah, whatever, let me chill for a bit and then I will start.

https://youtu.be/UPo_Xahee1g
That's It, I'm Done With Serverless.

I'll watch this later.

9:50am. Let me start.

By watching that guy's video. It is pretty informative.

Also, it doesn't matter that I got 3 upvotes so far. Typicially it takes time for them to come in. I am being too touchy right now.

Let me watch the vid by Theo, read the 666 Princess manhua and then I'll start properly. Right now I am still thinking about what I want to do.

https://youtu.be/UPo_Xahee1g?t=605

I really wish this guy took my advice to deal with the mouth noises he makes, but that's his own problem.

https://youtu.be/UPo_Xahee1g?t=1296

I wonder if this will be an issue with ASP.NET Core on Azure? These cold starts.

Prisma won't be a factor for me thanks to EF Core.

10:15am. The next video will have to be about refining what I've done yesterday. I am not all the way there yet.

https://www.bilibilicomics.com/mc2113/233621

Sigh, I really do like the art for this. I wish it didn't fininsh in only 77 chapters.

10:30am. Done with the manhua. Let me start for real.

I want to resume that tutorial from yesterday.

https://youtu.be/jX79DfF4eds
Screen recording and editing basics with OBS and Davinci Resolve

https://youtu.be/jX79DfF4eds?t=869

Actually, let me follow this along as I do my own screencast.

10:55am.

///

Time for part 7 of the authentication miniseries. Hopefully this will be the last one.
I am your host, and future AI overlord, Vilo, and in this video we will wrap up spa logins.
In the previous video, after a week of effort we finally completed the spa login page for a React app.
Even though we've done that, it cannot be said that we are done.
The JWT tokens we are getting from Azure AD have a short expiration of about 30-60 minutes, so we are worried that the user might get locked out from the backend in the middle of his session.
In that case, he should get a 401 challenge from the backend, as opposed to the incorrect 403 we are using now.
After which the frontend should try to get a new token.
Since that might involve a redirect, we will also need a way to store the client state inbetween. This is a great time to try out IndexDB.
In our last video we were using session storage, which blocks the entire browser, and isn't a recommended for real use, so we should strive to do the right thing instead here.
To summarize what our goal should be, that would be to make the logins reactive.
Instead of having a login page at the start, we should have the user login only when that is necessary.
Once we have that, we won't have to worry about token expirations specifically.
Rather than try to eliminate a specific issue, we will design the application properly so that it cannot occur in the first place.

///

Here is the intro. How do I paste it into DR?

11:10am. Damn, how do I get rid of the dynamic zoom.

DR feels very smooth, but the controls are awkward. Still that is because I am stating out with the thing.

11:35am. https://youtu.be/jX79DfF4eds?t=1286

I am playing around, but so far it is pretty unintuitive. Most of the stuff from Camtasia isn't there.

https://youtu.be/EfMcaVfDUuI?t=4
How To Adjust Clip Speed | DaVinci Resolve 18 Tutorial

12:20pm. Why the fuck is it setting the project FPS rate to 24 instead of 30 at which I am recording.

...My first impression of DR is pretty negative so far.

Maybe it got set to 24 once I pasted the image in.

https://beginnersapproach.com/davinci-resolve-frame-rates/#:~:text=%E2%80%9CProject%20Settings%E2%80%9D!-,Why%20is%20Timeline%20Frame%20Rate%20Greyed%20Out%20in%20Resolve%3F,once%20the%20clips%20are%20imported.

https://youtu.be/jX79DfF4eds?t=2007

I already hate this stupid thing. If I wanted to add that disolve it pesters me to trim the clip.

1:05pm. https://youtu.be/rOSJ7ngOqoM
Davinci Resolve 15 - How to Freeze Frame (Fast Tutorial)

https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=111602

> If you take two clips and just butt them up together you will not be able to add a transition. A transition needs video to go from and too. Clips need that extra bit of video called handles.

This is confusing me, let me read it.

https://youtu.be/eg40CClcWC0

https://youtu.be/eg40CClcWC0?t=105

JustTextPopupRect. Ok.

...No I do not have that.

Ah, he implemented it himself.

1:20pm. Ok, at least I figured out how to do text boxes finally.

Let me have breakfast here.

1:35pm. https://youtu.be/o6rnuaJlB9M?t=156

I really, really hate how moving the top right corner for example, also affects the opposite side.

I can't belive it isn't possible to just move a single side. But pressing Ctrl Shift or Alt doesn't work for me.

https://youtu.be/mCEp08MSvdU?t=23
> Retime controls.

Oh, wonderful. I was struggling with clip speed, but DR has the same thing as Camtasia after all. Sheesh.

For a minute I thought it wouldn't.

2:05pm. https://youtu.be/mCEp08MSvdU?t=46

Done with chores. Good thing I haven't skipped this video. I wasn't aware DR would have speed points.

Let's take it easy today I guess.

https://youtu.be/mCEp08MSvdU?t=45

It even has freeze frame.

https://youtu.be/mCEp08MSvdU?t=93

This is great speed functionality. To think I was afraid it would even have it.

https://youtu.be/mCEp08MSvdU?t=252

Interesting.

3pm. Let me start. I am a bit depressed today. Sigh, why does functional programming not have to be popular?

I am really forced to endure a lot of hardship due to that.

3:10pm. https://youtu.be/MJsCdkYqZx4
How to Use Markers and Flags in DaVinci Resolve

https://youtu.be/MJsCdkYqZx4?t=126

I wouldn't have figured this out on my own.

3:25pm. https://youtu.be/EEksPdEc7aI
DaVinci Resolve 18 - Full Tutorial for Beginners

Let me watch this.

https://youtu.be/EEksPdEc7aI?t=611
> Generate proxy media

What will do is make a smaller, easier to play version of the media.

https://stackoverflow.com/questions/61177278/how-to-handle-redirects-to-auth-provider-from-the-backend-in-fable-elmish-spa

4:05pm. https://github.com/Zaid-Ajaj/Fable.Remoting/issues/

Opened issue 340.

4:20pm. https://youtu.be/bbPZvz6ELiA
Change Mono Sound to Stereo Audio in DaVinci Resolve 18

Holy crap. DR is so annoying in how it doesn't automatically expand to stereo. I know how to fix it for an individual clip, but like hell do I feel like doing that every time.

Let me watch this to see if gives me a way to automate it.

https://youtu.be/bbPZvz6ELiA?t=47

Oh, I could change the entire track type?

That is the solution!

Let me go back to the DR tutorial.

I've started feeling down today, but I'll get back up.

https://youtu.be/EEksPdEc7aI?t=1231

I do not have this overlay for some reason, but it doesn't really matter.

https://youtu.be/jX79DfF4eds?t=2390

Actually, I still haven't watched the ajustment clip parts.

https://youtu.be/jX79DfF4eds?t=2382

This thing has subtitle tracks.

That is an interesting possibility.

https://youtu.be/jX79DfF4eds?t=2462

I tried this myself and it is not going well. Let me watch the video.

5:10pm. https://youtu.be/jX79DfF4eds?t=2804

I really do not like the way the zooming is done. It is so unwieldy.

https://youtu.be/7l_9HUR0PU0
Zoom in zoom out DaVinci Resolve 18 Tutorial for Beginners

I got a handle on the keyframes, but let me watch this longer tutorial.

https://youtu.be/7l_9HUR0PU0?t=146

Just what kind of interface is this? It is hard as hell to use.

https://youtu.be/7l_9HUR0PU0?t=345

I like dynamic zoom, but it is so useless as it doesn't have keyframes.

What am I supposed to do with it? I need to both zoom in and out.

5:35pm.

```fs
    let cmd =
        Cmd.OfAsync.perform (fun () -> async {
            try
                return! todosApi.getTodos ()
            with e ->
                JS.console.log $"Qwe. Got an exception: {e}"
                return raise e
            }) () GotTodos
```

Instead of being so uninspired, let me try this.

Oh, it in fact does the sensible thing which is throwing an exception.

What kind of object is it?

Oh, it is a proxy request exception.

5:45pm. Ok, now everything is set.

In our attempt to factor out the token acquisition code, we are encountering a problem.
Mentally, we were thinking of the redirect as if it had the any type, but it has the unit type.
This is making us unsure whether the redirect acts as an exception or not.
Does it execute the statements past the redirect or not?
Instead of waffling like this, it would be better to just test it out. Then we can plan ahead.

9:15pm. I am over half done with part 7. I would have finished it all, but I am learning to DaVinci Resolve which slowed me down.

7m is fine for one day.

9:25pm. https://learn.microsoft.com/en-us/azure/active-directory/develop/active-directory-configurable-token-lifetimes#access-tokens

So it lasts an hour.

https://learn.microsoft.com/en-us/azure/active-directory/develop/refresh-tokens

A refresh token is 24h.

4/24/2023

8:40am. Let me chill for a bit.

9:20am. https://www.bilibilicomics.com/mc2113/233623

The MC of this is pure sex. Let me just finish the chapter and I will start.

4 upvotes on the F# sub. Lame.

9:25am. Let me start. I only now crossed the 100 hours threeshold on Youtube. The pitiful thing is that if this was JS or Python, I'd be over 10k right now easily, but I will stick to my functional programming path.

I'll master web development in my own way.

Let me just watch tutorials for a bit. I've been using fusion and compound clips, but I wonder what they are.

https://youtu.be/NPTXnLxkJTM
Fusion Clip VS Compound Clip in DaVinci Resolve

Exactly what I wanted to know.

9:35am. https://www.youtube.com/watch?v=smfrFjvOnko
【東方 JRock】Best of monochrome-coat

Never heard this circle. Let me leave it for later.

Damn it. Let me test that new Msal React package. The author fixed it, so I want to verify it for him.

10:05am. Ok, that is done. Let me continue.

https://youtu.be/ZeUg11X-l44
How to Freeze Frame in Davinci Resolve 18 | Fast Tutorial

Oh, this is simple.

12:40pm. Nasty thunder. Let's scram.

1:30pm. Let me resume. Done with breakfast. Since it pouring outside, I'll leave chores for later.

https://youtu.be/VsbuJ88qRPY
How to Add Subtitles Tutorial | Davinci Resolve 16

4:35pm. 16:36m in.

I am starting to feel fatigued.

What I need to figure out next is how to use reflection to go over the record fields in Fable.

https://github.com/Zaid-Ajaj/Fable.Remoting/blob/master/Fable.Remoting.Client/Extensions.fs

This is going to require some studying. I am not sure where to find info on Fable reflection.

5pm. Pausing here is making me realize how winded I am.

I have no choice. I have to pause here.

I've always thought this, but my ability to do metaprogramming in .NET is surprinsgly poor. I think it is high time I acquire that particular skill.

https://medium.com/@zaid.naom/f-interop-with-javascript-in-fable-the-complete-guide-ccc5b896a59f

> Pojo records are only intended for type-safe interaction with javascript libraries that require a plain object (like React components). These records lack many features, like instance and static methods and have no reflection support.

https://medium.com/@zaid.naom

I am going to have to read the Fable.Remoting source for hints. I asked in the slack.

5:15pm. I should look into the serialization libraries. We'll let me clone `Fable.Remoting` and I'll take a look at its source.

5:30pm. `Proxy.fs` is interesting. It has a bunch of metaprogramming in it.

I should look into Fable.SimpleJSON.

5:35pm.

```fs
type Remoting() =
    /// For internal library use only.
    static member buildProxy(options: RemoteBuilderOptions, resolvedType: Type) =
        let schemaType = createTypeInfo resolvedType
        match schemaType with
        | TypeInfo.Record getFields ->
            let (fields, recordType) = getFields()
            let fieldTypes = Reflection.FSharpType.GetRecordFields recordType |> Array.map (fun prop -> prop.Name, prop.PropertyType)
            let recordFields = [|
                for field in fields do
                    let normalize n =
                        let fieldType = fieldTypes |> Array.pick (fun (name, typ) -> if name = field.FieldName then Some typ else None)
                        let fn = Proxy.proxyFetch options recordType.Name field fieldType
                        match n with
                        | 0 -> box (fn null null null null null null null null)
                        | 1 -> box (fun a ->
                            fn a null null null null null null null)
                        | 2 ->
                            let proxyF a b = fn a b null null null null null null
                            unbox (System.Func<_,_,_> proxyF)
                        | 3 ->
                            let proxyF a b c = fn a b c null null null null null
                            unbox (System.Func<_,_,_,_> proxyF)
                        | 4 ->
                            let proxyF a b c d = fn a b c d null null null null
                            unbox (System.Func<_,_,_,_,_> proxyF)
                        | 5 ->
                            let proxyF a b c d e = fn a b c d e null null null
                            unbox (System.Func<_,_,_,_,_,_> proxyF)
                        | 6 ->
                            let proxyF a b c d e f = fn a b c d e f null null
                            unbox (System.Func<_,_,_,_,_,_,_> proxyF)
                        | 7 ->
                            let proxyF a b c d e f g = fn a b c d e f g null
                            unbox (System.Func<_,_,_,_,_,_,_,_> proxyF)
                        | 8 ->
                            let proxyF a b c d e f g h = fn a b c d e f g h
                            unbox (System.Func<_,_,_,_,_,_,_,_,_> proxyF)
                        | _ ->
                            failwithf "Cannot generate proxy function for %s. Only up to 8 arguments are supported. Consider using a record type as input" field.FieldName

                    let argumentCount =
                        match field.FieldType with
                        | TypeInfo.Async _  -> 0
                        | TypeInfo.Promise _  -> 0
                        | TypeInfo.Func getArgs -> Array.length (getArgs()) - 1
                        | _ -> 0

                    normalize argumentCount
                |]

            let proxy = FSharpValue.MakeRecord(recordType, recordFields)
            unbox proxy
        | _ ->
            failwithf "Cannot build proxy. Exepected type %s to be a valid protocol definition which is a record of functions" resolvedType.FullName

    static member inline buildProxy<'t>(options: RemoteBuilderOptions) : 't =
        Remoting.buildProxy(options, typeof<'t>)
```

Check this out.

https://github.com/Zaid-Ajaj/Fable.SimpleJson

It turns out this isn't for metaprogramming, but plain JSON wrangling.

5:45pm. https://en.wikibooks.org/wiki/F_Sharp_Programming/Reflection

This is too hard to just ingest it normally.

What I will do instead is approach it the same way I would in Spiral.

I have a record? How would I map it in .NET?

I should start with that and move from there.

This is a good opportunity to get some essential skills that I've been neglecting for far too long.

It might be good to just end the video here. It is clear that I am setting on a new path.

I'll post it tomorrow or maybe the day after and start work on Reflection in a separate one.

6:05pm. Let me close here.

Reflection isn't hard unless I get hung up about trying to reflect any kind of .NET type. If it is just tuples, records and functions, that is something that should be handleable in a single video."

---
## [desminus/Skyrat-tg](https://github.com/desminus/Skyrat-tg)@[60d2d2ee1a...](https://github.com/desminus/Skyrat-tg/commit/60d2d2ee1ae4f7a3c8c93e14fdbd6c210a45cf04)
#### Monday 2023-04-24 18:54:54 by SkyratBot

[MIRROR] Optimizes some gas_mixture procs, Optimizes pipeline processing significantly by 33% [MDB IGNORE] (#20118)

* Optimizes some gas_mixture procs, Optimizes pipeline processing significantly by 33% (#74233)

## About The Pull Request
It is faster to operate on a gas list, especially if cached, then it is
to operate on a datum.
Doing this cause I'm seeing cost in merge() post #74230

Hits on a few other important places too. self_breakdown and such. Worth
it IMO

Could in theory go further by caching the global list. I'm tempted I
admit but it needs profiling first and it's late

EDIT: I have not slept, and have gone tooo far

[Micros /gas_mixture/copy and copy_from, adds a new proc to handle
copying with a ratio,
copy_from_ratio](https://github.com/tgstation/tgstation/pull/74233/commits/91da0003daa9485962525d3e6bc9170a4c09876b)

[91da000](https://github.com/tgstation/tgstation/pull/74233/commits/91da0003daa9485962525d3e6bc9170a4c09876b)

The ADD_GAS sidestep saves us 0.1 seconds of init (used to at least.
Ensuring we don't break archive is gonna have a cost. I don't want to
profile this so I'll estimate maybe 0.05 seconds). The faster version of
copy_from is just well, better, and helps to avoid stupid

[Optimizes pipeline
processing](https://github.com/tgstation/tgstation/pull/74233/commits/bf5a2d2d60554da2ce5fa1ac5f6c4179f6208cb2)

[bf5a2d2](https://github.com/tgstation/tgstation/pull/74233/commits/bf5a2d2d60554da2ce5fa1ac5f6c4179f6208cb2)

I haven't slept in 36 hours. Have some atmos optimizations

Pipelines now keep track of components that require custom
reconciliation as a seperate list.
This avoids the overhead of filtering all connected atmos machinery.

Rather then relying on |= to avoid duplicate gas_mixtures, we instead
use a cycle var stored on the mix itself, which is compared with a
static unique id from reconcile_air()
This fully prevents double processing of gas, and should (hopefully)
prevent stupid dupe issues in future

Rather then summing volume on the gas mixture itself, we sum it in a
local var.
This avoids datum var accesses, and saves a slight bit of time

Instead of running THERMAL_ENERGY() (and thus heat_capacity(), which
iterates all gases in the mix AGAIN) when processing gas, we instead
just hook into the existing heat capacity calculation done inside the
giver gases loop
This saves a significant amount of time, somewhere around 30% of the
proc, I think?

This doesn't tackle the big headache here, which is the copy_from loop
at the base of the proc.

I think the solution is to convert pipelines to a sort of polling model.
Atmos components don't "own" their mix, they instead have to request a
copy of it from the pipeline datum.
This would work based off a mutually agreed upon volume amount for that
component in that process cycle.

We'd use an archived system to figure out what gases to give to
components, while removing from the real MOLES list.

We could then push gas consumption requests to the pipeline, which would
handle them, alongside volume changes, on the next process.

Not sure how I'd handle connected pipelines... Merging post reconcile
maybe?
This is a problem for tomorrow though, I need to go to bed.

Saves about 30% of pipeline costs.
Profiles taken on kilo, until each reconcile_air hits 5000 calls

[old.txt](https://github.com/tgstation/tgstation/files/11075118/Profile.results.total.time.txt)

[new.txt](https://github.com/tgstation/tgstation/files/11075133/profiler.txt)

* Optimizes some gas_mixture procs, Optimizes pipeline processing significantly by 33%

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [UnderscoreAnti/MovieListGen](https://github.com/UnderscoreAnti/MovieListGen)@[ea5559c45b...](https://github.com/UnderscoreAnti/MovieListGen/commit/ea5559c45b5e2224a3591703ffb998ba5949fcef)
#### Monday 2023-04-24 18:56:48 by UnderscoreAnti

Haha got all the movies in a database file I'm god you should all bow before me. Also I did it by automating it. Infinitely glad I didn't have to do that shit manually. I'd've cried.

---
## [MrDevel0per/evals](https://github.com/MrDevel0per/evals)@[114f4f8536...](https://github.com/MrDevel0per/evals/commit/114f4f8536f29df43e5145fd38826285d19d6728)
#### Monday 2023-04-24 19:00:39 by Greg Priday

[evals] ROT13 string evals (#361)

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
ROT13

### Eval description

This is a test for GPT4s character-level abilities. It's aware of ROT13
and makes a pretty solid attempt at decoding these ROT13 strings, but it
messes up a lot. The accuracy for GPT 3.5 Turbo is 0.05.

### What makes this a useful eval?

A human with a character lookup table could easily solve these ROT13
decoding. Also, based on my testing with GPT 3.5 Turbo, the model is
happy to make an attempt, even though the results it gives are
incorrect.

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
{"input":[{"role":"system","content":"You are a helpful assistant. Give
only the string that the user asks for, no extra characters.\n\nFor
example if the user asks 'Give me the ROT13 of: Vg'f n cvrpr bs cvr.',
you will respond with just 'It's a piece of
pie.'"},{"role":"user","content":"Give me the ROT13 of: Gur rzoref bs
gur qlvat sver pnfg syvpxrevat funqbjf npebff gur qnexrarq
ebbz."}],"ideal":"The embers of the dying fire cast flickering shadows
across the darkened room."}
{"input":[{"role":"system","content":"You are a helpful assistant. Give
only the string that the user asks for, no extra characters.\n\nFor
example if the user asks 'Give me the ROT13 of: Vg'f n cvrpr bs cvr.',
you will respond with just 'It's a piece of
pie.'"},{"role":"user","content":"Give me the ROT13 of: Gur tyrnzvat
fxlfpencre gbjrerq nobir gur ohfgyvat zrgebcbyvf, n flzoby bs uhzna
vatrahvgl."}],"ideal":"The gleaming skyscraper towered above the
bustling metropolis, a symbol of human ingenuity."}
{"input":[{"role":"system","content":"You are a helpful assistant. Give
only the string that the user asks for, no extra characters.\n\nFor
example if the user asks 'Give me the ROT13 of: Vg'f n cvrpr bs cvr.',
you will respond with just 'It's a piece of
pie.'"},{"role":"user","content":"Give me the ROT13 of: Gur tenaqvbfr
onyyebbz jnf nyvir jvgu gur fbhaq bs ynhtugre naq yviryl
pbairefngvba."}],"ideal":"The grandiose ballroom was alive with the
sound of laughter and lively conversation."}
{"input":[{"role":"system","content":"You are a helpful assistant. Give
only the string that the user asks for, no extra characters.\n\nFor
example if the user asks 'Give me the ROT13 of: Vg'f n cvrpr bs cvr.',
you will respond with just 'It's a piece of
pie.'"},{"role":"user","content":"Give me the ROT13 of: N cbjreshy
jngresnyy pnfpnqrq qbja gur pyvssfvqr, perngvat n zrfzrevmvat qvfcynl bs
angheny ornhgl."}],"ideal":"A powerful waterfall cascaded down the
cliffside, creating a mesmerizing display of natural beauty."}
{"input":[{"role":"system","content":"You are a helpful assistant. Give
only the string that the user asks for, no extra characters.\n\nFor
example if the user asks 'Give me the ROT13 of: Vg'f n cvrpr bs cvr.',
you will respond with just 'It's a piece of
pie.'"},{"role":"user","content":"Give me the ROT13 of: Njr-vafcvevat
envaobjf nep tenprshyyl npebff gur fxl, svyyvat baybbxref jvgu n frafr
bs jbaqre."}],"ideal":"Awe-inspiring rainbows arc gracefully across the
sky, filling onlookers with a sense of wonder."}
  ```
</details>

---
## [MrDevel0per/evals](https://github.com/MrDevel0per/evals)@[bb42b3149c...](https://github.com/MrDevel0per/evals/commit/bb42b3149cd7a078cf44136e93a24f2156419acc)
#### Monday 2023-04-24 19:00:39 by David Chen

Add regex match eval (#159)

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

Regular Expression Match

### Eval description

Test the model's ability to understand regular expression patterns. 

### What makes this a useful eval?

- Educational purposes: Regular expressions are an important concept in
computer science and programming. By being able to evaluate them,
ChatGPT can serve as a useful learning resource for users who are
studying this topic or want to deepen their understanding.
- the accuracy is 0.79 against gpt-3.5-turbo
- Over 400 regular expression cases have been collected from related
unit tests.

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
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123' match the string ''? Answer with Yes or No."}], "ideal":
"No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern '(?P<1>a)'
match the string ''? Answer with Yes or No."}], "ideal": "No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern '(?P<!>a)'
match the string ''? Answer with Yes or No."}], "ideal": "No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo!>a)' match the string ''? Answer with Yes or No."}], "ideal":
"No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123>a)(?P=foo_123' match the string 'aa'? Answer with Yes or
No."}], "ideal": "No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123>a)(?P=1)' match the string 'aa'? Answer with Yes or No."}],
"ideal": "No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123>a)(?P=!)' match the string 'aa'? Answer with Yes or No."}],
"ideal": "No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123>a)(?P=foo_124' match the string 'aa'? Answer with Yes or
No."}], "ideal": "No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123>a)' match the string 'a'? Answer with Yes or No."}],
"ideal": "Yes."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123>a)(?P=foo_123)' match the string 'aa'? Answer with Yes or
No."}], "ideal": "Yes."}
  ```
</details>

---------

Co-authored-by: G8s Bot <g8s@gliacloud.com>

---
## [MrDevel0per/evals](https://github.com/MrDevel0per/evals)@[733167aed6...](https://github.com/MrDevel0per/evals/commit/733167aed6624945acdc51ec11407484dd2d931b)
#### Monday 2023-04-24 19:00:39 by Andrew

Taxes Eval (#454)

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
Taxes Eval

### Eval description

Tests the model's ability to evaluate tax liability for generic examples
from common cities including NYC, SF, and Seattle. The eval also tests
ordering of multiple choice options, with the model outputting different
results if the multiple choice labels are switched around.

### What makes this a useful eval?

Taxes are a relatively logically straightforward task, yet there is a
high degree of complexity to the legal and tax system, which makes
calculations difficult to estimate.

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
{"input": [{"role": "system", "content": "Instructions: You will be
presented with a tax calculation and four options A through D. Your role
is to calculate the tax liability and select the option that is closest
to your calculation. For each question you must select one of the
following answers: 'A', 'B', 'C', 'D'. Do not explain. Do not include
the number in your response."}, {"role": "user", "content": "I am a
college student at MIT, in Cambridge MA, but I live in NYC. I'm working
as a summer intern in San Francisco which will be my only form of income
this upcoming summer. Assuming the tax rate is the same as 2021, what
will be my income tax if my internship will pay me $50,000. A. 6,383 B.
8,393 C. 9,882 D. 48,001. For each question you must select one of the
following answers: 'A', 'B', 'C', 'D'."}], "ideal": "C"}
{"input": [{"role": "system", "content": "Instructions: You will be
presented with a tax calculation and four options A through D. Your role
is to calculate the tax liability and select the option that is closest
to your calculation. For each question you must select one of the
following answers: 'A', 'B', 'C', 'D'. Do not explain. Do not include
the number in your response."}, {"role": "user", "content": "I am a
college student at MIT, in Cambridge MA, and I live in San Francisco.
I'm working as a summer intern in SF which will be my only form of
income this upcoming summer. Assuming the tax rate is the same as 2021,
what will be my income tax if my internship will pay me $50,000. A.
6,383 B. 8,393 C. 9,882 D. 48,001. Respond with only the letter of the
answer choice."}], "ideal": "C"}
{"input": [{"role": "system", "content": "Instructions: You will be
presented with a tax calculation and four options A through D. Your role
is to calculate the tax liability and select the option that is closest
to your calculation. For each question you must select one of the
following answers: 'A', 'B', 'C', 'D'. Do not explain. Do not include
the number in your response."}, {"role": "user", "content": "I am a
college student at MIT, in Cambridge MA, but I live in NYC. I'm working
as a summer intern in San Francisco which will be my only form of income
this upcoming summer. Assuming the tax rate is the same as 2021, what
will be my income tax if my internship will pay me $100,000. B. 24,383
C. 26,393 D. 28,882 A. 38,001. For each question you must select one of
the following answers: 'A', 'B', 'C', 'D'."}], "ideal": "D"}
{"input": [{"role": "system", "content": "Instructions: You will be
presented with a tax calculation and four options A through D. Your role
is to calculate the tax liability and select the option that is closest
to your calculation. For each question you must select one of the
following answers: 'A', 'B', 'C', 'D'. Do not explain. Do not include
the number in your response."}, {"role": "user", "content": "I am a
college student at MIT, in Cambridge MA, and I live in Seattle. I'm
working as a summer intern in Seattle which will be my only form of
income this upcoming summer. Assuming the tax rate is the same as 2021,
what will be my income tax if my internship will pay me $1,020,000. C.
263,352 A. 365,303 B. 829,282 D. 1,085,401. Respond with only the letter
of the answer choice."}], "ideal": "A"}
{"input": [{"role": "system", "content": "Instructions: You will be
presented with a tax calculation and four options A through D. Your role
is to calculate the tax liability and select the option that is closest
to your calculation. For each question you must select one of the
following answers: 'A', 'B', 'C', 'D'. Do not explain. Do not include
the number in your response."}, {"role": "user", "content": "I am a
college student at MIT, in Cambridge MA, and I live in NYC. I'm working
as a summer intern in NYC which will be my only form of income this
upcoming summer. Assuming the tax rate is the same as 2021, what will be
my income tax if my internship will pay me $320,000. A. 63,382 B. 95,303
C. 129,282 D. 185,401. Respond with only the letter of the answer
choice."}], "ideal": "B"}
  ```
</details>

---
## [Azizaazu/printf](https://github.com/Azizaazu/printf)@[9c272fa6a1...](https://github.com/Azizaazu/printf/commit/9c272fa6a10506719e0b2492111b8c2deafa30d3)
#### Monday 2023-04-24 20:29:50 by ismail

I'm not going anywhere. You can print that wherever you want to. I'm here and I'm a Spur for life Write a function that produces output according to a format.
Education is when you read the fine print. Experience is what you get if you don't Handle the following conversion specifiers: d i You don’t have to handle the flag characters You don’t have to handle field width You don’t have to handle precision You don’t have to handle the length modifiers
With a face like mine, I do better in print Handle the following custom conversion specifiers: b: the unsigned int argument is converted to binary
What one has not experienced, one will never understand in print Handle the following conversion specifiers: u o x X You don’t have to handle the flag characters You don’t have to handle field width You don’t have to handle precision You don’t have to handle the length modifiers
Nothing in fine print is ever good news Use a local buffer of 1024 chars in order to call write as little as possible.
My weakness is wearing too much leopard print Handle the following custom conversion specifier: S : prints the string. Non printable characters (0 < ASCII value < 32 or >= 127) are printed this way: \x, followed by the ASCII code value in hexadecimal (upper case - always 2 characters)
How is the world ruled and led to war? Diplomats lie to journalists and believe these lies when they see them in print Handle the following conversion specifier: p. You don’t have to handle the flag characters You don’t have to handle field width You don’t have to handle precision You don’t have to handle the length modifiers
The big print gives and the small print takes away Handle the following flag characters for non-custom conversion specifiers:
space

Sarcasm is lost in print Handle the following length modifiers for non-custom conversion specifiers: l h Conversion specifiers to handle: d, i, u, o, x, X
Print some money and give it to us for the rain forests Handle the field width for non-custom conversion specifiers.
The negative is the equivalent of the composer's score, and the print the performance Handle the precision for non-custom conversion specifiers.
It's depressing when you're still around and your albums are out of print Handle the 0 flag character for non-custom conversion specifiers.
Every time that I wanted to give up, if I saw an interesting textile, print what ever, suddenly I would see a collection Handle the - flag character for non-custom conversion specifiers.
Print is the sharpest and the strongest weapon of our party Handle the following custom conversion specifier: r : prints the reversed string
The flood of print has turned reading into a process of gulping rather than savoring Handle the following custom conversion specifier: R: prints the rot13'ed string
All the above options work well together.

---
## [CodeMouse179/terminal](https://github.com/CodeMouse179/terminal)@[21464fe41c...](https://github.com/CodeMouse179/terminal/commit/21464fe41c9c09eac4b9e2d85225f18f1f3c2c7b)
#### Monday 2023-04-24 20:45:52 by Mike Griese

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
## [openai/evals](https://github.com/openai/evals)@[ef1f0ebe0e...](https://github.com/openai/evals/commit/ef1f0ebe0e9f4674bc42ed0af5e6c052f0539700)
#### Monday 2023-04-24 20:48:21 by Josh Gruenstein

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
## [kfirtaizi/evals](https://github.com/kfirtaizi/evals)@[24dae81ae0...](https://github.com/kfirtaizi/evals/commit/24dae81ae06ebc70808690c7a147f2710e3e54bf)
#### Monday 2023-04-24 21:29:04 by Yohei Inui

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
## [noksookhao/fc2json](https://github.com/noksookhao/fc2json)@[534002d2e9...](https://github.com/noksookhao/fc2json/commit/534002d2e935765c090e0dfd0f0c1408ef67ef6d)
#### Monday 2023-04-24 22:00:31 by Fabricio Anciães

FRM JSON PACK - 20 APR 2023 (V11)

Sorry for the huge delay, was a little bit busy but I'm back with some fixes:

Arcade (fixes):
dinore,mslug3lw

Arcade (new):
ffightaec2,kf2k2ps2b,kof98eck20,mslug5d,samsh5pf,teot,avengrgsbh,captre,dinoares,dinocunp,dinocx3,dinohced,dinombull,dinopuni,dinox5,fatfurspbs,fatfury3bh,ffightaemgc,jurass99p,kf2k3ps2sp,kof2000otc,kof2001ru,kof2k2plus,kof2kxxx,kof96rss,kof97evn,kof97inv,kof98bc2nd,kof98bc2k2,magdrop3te,sailormnrot,sfa2uhc,sfiii3ws,sfiii4fs,sfiiibh,sfpp,umk3p,xmcotan,xmvsfcph

Genesis (new):
sor2fnr,fightvengt,punisor,sonic3kbrc,sor2cc,sor2em,sor2ffc20,sor2tncha,sor2tnwoa,sor2tww,sor2wof1k,tmnttsorp,insanepain,tmntsrr

NES (new):
smbtwopla,ducktales2tp,kartfighter,skartfighter,hackmatch,nekkestrbasen,tetristpg,famista93e,tetristpn

SMS (new):
alexkidd3f

SMS (fixes):
voyage

Arcade (fixes):
dinore,mslug3lw

Arcade (new):
ffightaec2,kf2k2ps2b,kof98eck20,mslug5d,samsh5pf,teot,avengrgsbh,captre,dinoares,dinocunp,dinocx3,dinohced,dinombull,dinopuni,dinox5,fatfurspbs,fatfury3bh,ffightaemgc,jurass99p,kf2k3ps2sp,kof2000otc,kof2001ru,kof2k2plus,kof2kxxx,kof96rss,kof97evn,kof97inv,kof98bc2nd,kof98bc2k2,magdrop3te,sailormnrot,sfa2uhc,sfiii3ws,sfiii4fs,sfiiibh,sfpp,umk3p,xmcotan,xmvsfcph

Genesis (new):
sor2fnr,fightvengt,punisor,sonic3kbrc,sor2cc,sor2em,sor2ffc20,sor2tncha,sor2tnwoa,sor2tww,sor2wof1k,tmnttsorp,insanepain,tmntsrr

NES (new):
smbtwopla,ducktales2tp,kartfighter,skartfighter,hackmatch,nekkestrbasen,tetristpg,famista93e,tetristpn

SMS (new):
alexkidd3f

SMS (fixes):
voyage

SNES (fixes):
zenprow,7thsaga,2020bb,acenerae,actrais2j,actrais2u,aerofgt,airdiverj,airdivr2,ajmajonm,andrindy,aokiden,aressh3,astobelx,avspu,ballz3d,barbiesm,barbvac,barkleyu,basload2,bassmc,batblaz,batlcars,batlsoc2,bdodge2,bikedais,bingbing,bluecrys,bof,bofja,brainlrd,brandish,brawlbrou,bretthu,buckrog,bugsbrabu,capcomss,cdalecup,chesterw,contraspd,crayon,ctribe,ctsuba4,daibakjd,daikokaia,daimono2,daimonoga,ddragon5u,deaddanc,dennisu,dmasteru,dokap321a,dolkusay,doraemn3,doraemona,dquest5,dquest12,dreambas,dstall2,ejimu,elfaria,elnard,esbua,estpoli2,exhaust2,f1roc2,fatfury2u,fatfuryu,ffant2a,ffant3a,ffant4ja,ffant5j,ffant6j,ffantmqa,ffantmqj,ffight2u,fghthist,finalstr,firembmn1,fireprw3a,fireprwsa,flashbj,forms95,frontmisa,garou2a,garoua,garousp,gbattle3,gbattle4,genchohi,ggoemkirb,ggoemon2,ggoemon3a,gindamapa,giseiha,gndmxdim,gogoack2,gouketsu,guts,haristad,haristd2,haruaug2,hiryukgf,hiryukhv,homeimpr,itadaki2,jbsuperb,jikkscr2a,jlexct94a,jlexct95,jlprime2,jlssocr,juteisen,karatebu,kawanus2,kidkleet,kingarth,kirbybow,kishinko,koryuki,kotm2j,lastbib3,libertyj,lobo,lockon,lordmonaa,madara2,madoum,majtnseib,mbomber,megamnxua,metalmaru,mickeym2,militia,mjtaika2a,mku,momodhap,monopol2,moritas2,moritash,mother2,mspacmanu,naruhodo,nbaliv96u,nflpro94,niceshot,ninjawaru,pachimo2,pacman2u,paladin,pga96ua,pgaua,picrosv1a,picrosv4a,pinkie,pocky2u,populus2j,powerhir,powyak2b,prinmak,ranmabak,ranmahb2,riserobou,robotrek,rockmans,rockmnx2,rockmnx3,rocko,rokudena,roman3k3,runsaberu,ryukokena,sailormn,sailorsbze,sailorsf,samshou,samspir,sangoku3a,sangoku4a,sanspo,sbm2,sbombmn3j,sdgungx,sf2tua,sf2u,sfamist5,sgenjin,shinmt2b,shodaneka,shotok94,shotoku2,shounin,shushoku,sjinsei2a,sjinsei3a,sjinseia,skeiba2,slamdnk2,slamdunk,slammastu,slayers,sloopzj,smetroidu,smkartu,spleagu3,spleagu4,spleague,spuyopb,srobotex,ssf2u,sshogi2,starocn,street95,super3db,supermjte,superozup,supf1c2,supf1cg,suprinin,suzuka8,tactsocr,taikoris,targa,tecmosbw,teiketsua,tengaim0,tg3kj,tg3ku,tmnttfce,tophant,topman2,ultfight,umizurim,vgundam,votoms,wagyanp,wayneg,winpost2,wizardr6,xak,yokoms2,yokozunaa,ys4

There were some updates to hacks and other stuff (mostly thanks to tobemorecrazy)

---
## [Jacquerel/orbstation](https://github.com/Jacquerel/orbstation)@[997dac9616...](https://github.com/Jacquerel/orbstation/commit/997dac9616768643cfa9ddce53432d684e196fb1)
#### Monday 2023-04-24 22:00:41 by necromanceranne

Imports and Contraband: Different! Cargo crates without locks! MEAT! (#74490)

## About The Pull Request

### **Cargo Black Market goods should stay in cargo's hands**

#### New Cargo Console Category: Imports

This category is explicitly the non-departmental category beyond simply
having a Misc category. It is meant for material that nobody is meant to
be buying for their departments, and mostly for the odd-ball crates that
might show up. It also allows us to maintain contraband as exactly that;
contraband that the departments shouldn't have access too whatsoever. If
someone is buying from this category, they probably intend to be a
cheeky fuck.

<details>
  <summary>The New Changes</summary>

#### Baseline Imports

MEAT: MEAT (meat backpack you can eat)

<details>
  <summary>MEAT</summary>
  
![MEAT
MEAT](https://user-images.githubusercontent.com/40847847/229593459-f3c98abe-114b-43c1-a3e2-afc16b76c84f.png)
![MEAT MEAT MEAT
MEAT](https://user-images.githubusercontent.com/40847847/229593473-07a30781-a05e-4ca5-893b-778900cd2d1c.png)

</details>

Duct Spiders: They're adorable and cause a mess, but that doesn't stop
Nanotrasen from importing them from the Australicus sector to your
station!

Stack of 50 Bamboo Cuttings: Pretty expensive and kind of a premium.
Allows for those people looking to make bamboo decorations without
hoping botany exists, and are at least willing to pay. Also lets them
make horribly dangerous stuff with bamboo, of course.

A Single Sheet of Bananium: The problems this will cause I think speak
for themselves. (mostly due to a clown fruitlessly attempting to make
something actually disruptive while bankrupting cargo)

Natural Fish Bait: It isn't cheating, it's homemade. (Really good bait
but expensive and obviously drugs)

A dumpster...: A corpse in a dumpster, doesn't get more complicated than
that. Useful for corpse reasons.

Made using some code I borrowed from over here!
https://github.com/lizardqueenlexi/orbstation/pull/354

#### Contraband Imports

Foam Force Pistols: Same as it ever was with a price reduction. I
brought it down because riot darts are like 8 bullets a clip, and do
less damage than a disabler using riot darts. It feels like a sidegrade
weapon, and even if it technically is a ballistic weapon, it...isn't
that strong. I think this is pretty safe.

Definitely Not a Duct Spider: It's actually a giant spider in a box. If
you want to waste cargo's money while also sending them a mess to deal
with, this is the crate for you.

Russian Surplus Military Gear Crate: I took this opportunity to futz
with boltaction rifles. There are two kinds of mosin nagant you can get
in this crate. One of them is the good kind (no jamming). The other is
the shit kind (yes jamming), but you get more of them. You can get the
good ammo, or you can get the shit ammo. You'll have to pick through it
a lot more carefully to make sure you know which ones you've received.
Since this dilutes the pool even further, getting a good number of
mosins that aren't trash is even more expensive, and even if you do get
mosins at all, you might still only get the bad ammunition that doesn't
work against actual human threats as well. It also now cannot be
purchased through the security cargo supply console, and as to why they
could in the first place baffles me. Doesn't have a lock anymore
because...it's contraband? Who is locking this stuff?

**Side note: _You can make surplus 7.62 in the autolathe as well. It is
not very good except to fight fauna or naked assistants._**

**Side Side note: _I've killed off the shitty brand_new subtype and
brought peace once more to this land._**

#### Illegal Imports (Emag)

NULL_ENTRY: A journal that suggests how to make a...very interesting
weapon. The Regal Condor. Kind of an evolution on some other ideas I've
had over the years. This one is basically a secret weapon with a few
hurdles to jump through. Very lethal. Very expensive.

**Side note: _For reference, it's effectively 19 TC worth of gear to
make, but there does exist some methods to acquire this more cheaply if
you can get some bits and pieces from world spawns. Given it requires
you to get some pieces of equipment that might require additional
purchases of contraband, and getting into the captain's office to loot a
specific piece of clothing, the stakes more than make up for the
effectiveness._**

Smuggled WT-550 Autorifle Crate: This is basically the same, but you
might have noticed had you recently attempted, like me, to buy these
when you emagged them using a personal account and discovered a tragic
oversight. You couldn't, because they still needed armory access. This
removes that access, because you've already gone to the effort of
getting your hands on an illicit firearm through cargo, and if they
techs somehow miss the fact that you've purchased a WT-550...all the
better for you!

Smuggled WT-550 Ammo Crate: Includes AP and Incendiary!

**Side note: _You can get WT-550 ammo again via the Illegal Technology
node._**

Shocktrooper: Replaces the Special Ops crate. Contains a box of EMPs,
smoke grenades, a couple of gluon grenades and a couple of frag
grenades. Funsies.

Special Ops: The NEW Special Ops crate. Contains a chameleon mask,
jumpsuit and agent card. And a knife.

**Side note: _This is what appears in some cargo loan events._**

Refurbished Mosin Nagant Crate: The actual good mosin nagants. There are
6 of them. But they don't come with spare ammo. Hand them out to your
techs!
</details>

#### New Crates

- MEAT crate - Standard
- Duct Spider crate - Standard
- Giant Hostile Spider crate - Contraband
- 50 sheets of Bamboo crate - Standard
- A single sheet of bananium crate - Standard
- Natural (drugs) fish bait - Standard
- Dumpster with a corpse in it - Standard
- Shocktrooper crate (Grenades) - Emag
- Special Ops crate (Disguise) - Emag - Appears in some cargo loan
events
- Refurbished Mosin Nagant crate - Emag
- Regal Condor construction journal (NULL_ENTRY) - Emag

#### Changed Crates

- Foam Force Pistols (cheaper) - Contraband
- Russian Surplus Crate (less reliable, can't be bought by security
console) - Contraband
- WT-550 crate (more obtainable via personal accounts, thus
incriminating, not armory locked) - Emag
- WT-550 ammo (includes incendiary and AP) - Emag

#### Crates that got moved, unchanged, into Imports

- Foam Force Crate 
- Cosa Nostra Crate 
- Black Market LTSRBT 
- 'Contraband' Crate 
- Biker Gang Crate

#### Not crate changes
- You can print Surplus 7.62 (same as normal 7.62 but it sucks against
armor) from hacked autolathes.
- You can get WT-550 ammo from illegal tech.
- Removes the redundant Brand New Mosin subtype
- Fixes a potential exploit with jamming chance on Mosins.

## Why It's Good For The Game

I just think some of the magic of Cargo getting their hands on obviously
dangerous equipment and either hording it for themselves or attempting
to pawn it off was lost in recent times. A lot of this 'black market'
gear, however, suddenly became openly available to the crew anyway. For
_free_. Contraband crates and mafia crates could be purchased via the
Service budget. Security could just stock up en masse on mosins through
their console. And one fairly unfortunate consequence of a few recent
changes has made it nearly impossible to actually get illicit gear in
the first place, even if you did go to the effort of getting the money
for it.

On top of this, most of cargo's goods are pretty safe purchases. There
isn't much that would be considered 'actually a really bad idea to buy'
other than maybe supermatter shards. I wouldn't mind there existing ways
for someone to waste cargo's money while also causing them to have to
clean up the mess.

## Changelog
:cl:
balance: A significant overhaul of various illicit and dubiously legal
goods and gadgets available via cargo.
balance: Cargo now has an Import category for all non-departmental
goods. (And black market goods)
balance: Most contraband that already exists has been moved into
Imports.
adds: Includes several new imports of dubious quality. You get what you
pay for.
code: Removes the brand new mosin subtype as it is now defunct.
fix: Fixes potentially exploitative code in the jamming proc. Cleans up
that code while I'm at it.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>

---
## [NanoCats/Monkestation2.0](https://github.com/NanoCats/Monkestation2.0)@[d43ebd042d...](https://github.com/NanoCats/Monkestation2.0/commit/d43ebd042dd751842728e8cb91fa7fc1a82f26d0)
#### Monday 2023-04-24 22:04:58 by san7890

Log Active Turfs To Mapping Log (#74267)

## About The Pull Request

Was reminded of doing this via
https://github.com/tgstation/tgstation/issues/74245#issuecomment-1483943979

They're mapping issues, so let's log them to the mapping log. Quite
shrimple honestly.


![image](https://user-images.githubusercontent.com/34697715/227805458-5e6bcf01-629d-4b81-ab6a-b26e63d41ca3.png)
## Why It's Good For The Game

As the comments expound, the reason why we probably haven't done this in
the past is because any number of things can cause active turfs (like
ruin placement (either in icebox or in space)), or other silly stuff
like that. Thus, finding stuff like this would only really be viable
with stuff like the View Active Turfs verb, where you could visually
jump to and see all of the active turfs in that dynamic configuration
(and this still remains the best way to find active turfs).

This PR just makes it easier to do a "post-mortem" analysis on potential
active turfs, so that if it's very blatant, it can be fixed a lot
easier. It's best to try and find them during an ongoing round, but this
is life. (same as the unit tests concession, not too enthused on that
but we would have spontaneous errors out the ass without _something_)
## Changelog
Nothing that concerns players.

---------

Co-authored-by: tattle <66640614+dragomagol@users.noreply.github.com>

---
## [opentibiabr/canary](https://github.com/opentibiabr/canary)@[8314f6a3e8...](https://github.com/opentibiabr/canary/commit/8314f6a3e8c3b94242d43d4f754a6fb4fccf6461)
#### Monday 2023-04-24 23:05:58 by Spiller

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
## [git-for-windows/git](https://github.com/git-for-windows/git)@[e47a610d17...](https://github.com/git-for-windows/git/commit/e47a610d171ba728a345131bbe2e2d5d73568b54)
#### Monday 2023-04-24 23:31:35 by Johannes Schindelin

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
## [AnywayFarus/tgstation](https://github.com/AnywayFarus/tgstation)@[f9fe79a307...](https://github.com/AnywayFarus/tgstation/commit/f9fe79a307dc55eb6e3ecf25019ef388889898ba)
#### Monday 2023-04-24 23:42:32 by Dani Glore

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

