## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-03-18](docs/good-messages/2023/2023-03-18.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,933,515 were push events containing 2,649,944 commit messages that amount to 157,028,484 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 45 messages:


## [ZeWaka/OpenDream](https://github.com/ZeWaka/OpenDream)@[04e782a3fa...](https://github.com/ZeWaka/OpenDream/commit/04e782a3fa9ba78f491dfff7d7be02c63ed0f0a0)
#### Saturday 2023-03-18 00:45:14 by Altoids1

Improves the grammar, functionality, and code quality of set declarations (#776)

* Makes Consume array overload return the tokentype it found

Plus adds some extra comments, in my crusade to comment more things.

EDIT: hate you Github Desktop

* Removes MultipleVarDec..., replaces with Aggregate generic

Removes DMASTProcStatementMultipleVarDeclarations,
replaces with DMASTAggregate<>.

DMASTAggregate now has the generic-ified responsibility of being a statement which is actually an aggregate of several statements, all of the same type.

The point of this is so that this aggregation behaviour can also be used for set declaration blocks (and maybe other stuff if we find other uses, I dunno)

* Adds some helpful ctors for DMASTProcBlockInner

There's a lot of repetitive empty or near-empty array inits at the caller side of some of these constructions, so I went ahead and moved those into the ctor. Also allows for a minor optimization (preferring using Array.Empty<> instead of constructing empty arrays).

* Improves SetStatement grammar, function & quality

(If any of you demand I insert the oxford comma into the commit header I am leaving 5ever :rage: )

This commit does several things in one fell swoop:
- Set statements now accept blocking, commas, bracing, all the good stuff that var declarations do
- Blocks now very consistently evaluate their SetStatements first and foremost, before anything else, in a way that makes sense
- Use of the 'in' keyword is now properly prohibited for all set use cases except 'src'
- 'src' now properly gives an unimplemented warning

Also in this commit is a bunch of random autodoc added to things that I looked at or touched over the course of writing this commit. :innocent:

* Implements cursed parity behaviour for non-const set statements

AFAIK, in BYOND, the previous set statement value is used to prop-up one that has a non-constant right-hand side. So I guess we have that behaviour available, now. :sweat_smile:

EDIT: Fixed behaviour in the didError case, minor formatting fixes

* Style fix, replaces several "\n{" with "{\n"

Most of these were my fault. Not all of them though. :^)

* Does the Wixoa reviews, adds EmptyBlock pragma error

As a byproduct of doing the reviews, I have accidentally added empty block detection for several (although perhaps not most) loops and blocks available in OD.

* Brace style fixes

* Does more Wixoa reviews, generalizes EmptyBlock emission

Note that we do not, as of yet, emit this warning for empty procs. This is because:
1. our own DMStandard has several empty procs (usually because they are unimplemented or useless, like the BYOND Hub interface procs)
2. Users may sometimes define an empty proc, intentionally, to act as an abstract virtual that child types can define in their own way.

We can revisit the problem later, I'm just trying to get my PR greenlit.

* Adds test for EmptyBlock pragma emission

Co-authored-by: wixoa <wixoag@gmail.com>

---
## [Wollywoger/MapleStationCode](https://github.com/Wollywoger/MapleStationCode)@[b0ed78909b...](https://github.com/Wollywoger/MapleStationCode/commit/b0ed78909b484cfaf1be60c3daa1f59f4869f2fb)
#### Saturday 2023-03-18 00:53:36 by tralezab

Moves speaking verbs to tongues + subtypes, moves wing sprites to wing subtypes, bodypart damage examines to limbs, fixes sign language not working without a tongue (#71635)

Moves species say mod onto tongues, creates any tongues that didn't
exist for the say mods they needed to hold.

Moves the logic of selecting a wing sprite onto subtypes of /functional
on the wing type. Now, angel wings bring the holy trait with them, it
isn't a special check on flight potions, and we can expand it. (EMPs
taking down robowings? Fires burning megamoth wings? Cool stuff)

Instead of checking what your species says, it tallies up your limbs and
provides the damage description that matches most of your limbs. So for
example, If you're mostly human with one augmented part, you take
bruises and cuts. If you're mostly robot augmented with one human part,
you get robot damage descriptions. Yay!

Having no tongue would garble your speech, and this had no interaction
with sign language, so you'd be speaking in broken gurgling with
perfectly working hands. Now, the sign language component prevents any
kind of garbling, since it brings its own garbling for full/missing arms

![image](https://user-images.githubusercontent.com/40974010/204932511-42c8e020-a2d7-4fc1-befc-7cd46a2f2932.png)

Moving things off of species inherent makes the game expose way more
interesting mechanics to play with. It sucks that you can't steal a
jellyperson's chirping, since they can get a normal tongue and they'll
go back to... chirping! LAME! THAT IS LAME!

Ditto goes for wings, and for limbs, well, having someone be entirely
augmented but get descriptions of bleeding because they didn't spawn as
an android is kinda lame.

<details>
  <summary>Spoiler warning</summary>

![image](https://user-images.githubusercontent.com/40974010/204922627-333de052-a02b-4786-8ff9-f6e739443f2c.png)

</details>

:cl:
refactor: Refactored wings, tongues, and some examine messages,
hopefully with minimal effect on actual changes. A few more species have
tongues, angel wings bring the holy trait with them, and wings have new
descriptions. should be the biggest parts of it
/:cl:

---
## [Wollywoger/MapleStationCode](https://github.com/Wollywoger/MapleStationCode)@[d386bef9ee...](https://github.com/Wollywoger/MapleStationCode/commit/d386bef9ee0164c737683fd75aa84a6f85c137de)
#### Saturday 2023-03-18 00:59:32 by Time-Green

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
## [Stepland/F.E.I.S.](https://github.com/Stepland/F.E.I.S.)@[204609c4d0...](https://github.com/Stepland/F.E.I.S./commit/204609c4d0a42ec5dda4f4492bd9bd93de7ca5d8)
#### Saturday 2023-03-18 02:04:54 by Stepland

Switch to #pragma once because fuck you here's why

---
## [Ifeoma16/portfolio](https://github.com/Ifeoma16/portfolio)@[7d7f18fb9d...](https://github.com/Ifeoma16/portfolio/commit/7d7f18fb9d0f2d8223f46d63b563a9b9707a79a8)
#### Saturday 2023-03-18 02:14:29 by IfeomaOgwu

Bible verse widget

The Bible Verse Widget is a simple desktop widget designed to display a random Bible verse on your desktop. The widget provides users with a daily dose of inspiration and encouragement, presenting a different verse each day to help users reflect on God's word. The widget is lightweight and customizable, allowing users to choose from a variety of backgrounds and font styles to personalize their experience. The widget is built using Python and the tkinter library, making it easy to modify and extend. Install the Bible Verse Widget today and start your day with a refreshing Bible verse!

---
## [christopherlam/gnucash](https://github.com/christopherlam/gnucash)@[b4b8431984...](https://github.com/christopherlam/gnucash/commit/b4b843198421aef9332ad1cae348a4acacfa5586)
#### Saturday 2023-03-18 02:21:02 by John Ralls

Bug 798778 - GnuCashquits abruptly when attempting to edit options…

for certain reports.

Those reports being ones using complex options, apparently because
the callbacks weren't protected from Guile's garbage collector.

So replace the anyway ugly hack of a void* with a std::any wrapping
a class holding a std::unique_ptr with a custom deleter. The
constructor calls scm_gc_protect_object on the SCM containing the
callback and the custom deleter calls scm_gc_unprotect_object. The
copy constructor, required for std::any, makes a new std::unique_ptr
and calls scm_gc_protect_object again ensuring that the protect and
unprotect calls are symmetrical.

Meanwhile std::any hides the Guile dependency from all the classes
that don't need to know about it. The only ugliness is that there's
no good place to put a common implementation of SCNCallbackWrapper so it's
repeated in gnc-optiondb.i and dialog-options.cpp.

---
## [heady8354/Video-Game-Project](https://github.com/heady8354/Video-Game-Project)@[8ba19c0b31...](https://github.com/heady8354/Video-Game-Project/commit/8ba19c0b319e10982934c53da96193fe503a27fe)
#### Saturday 2023-03-18 02:35:02 by heady8354

returned to hawaii + good progress

so im finally back from the gross state that is california and i have already gotten more done than I did on the entire trip. probably because my computer at home can run more than 3 chrome tabs at once so its easy to fix bugs and such. and also i dont have to go out with my parents to a bar or a friends place and watch them get drunk as hell only to come home at 12am and fall asleep. (i am very tired at 12am) anyways, i created a to do list and a battle tutorial. im gonna be working on that over the weekend. hopefully itll be done by tuesday.

---
## [NewyearnewmeUwu/cmss13](https://github.com/NewyearnewmeUwu/cmss13)@[d40fdb9101...](https://github.com/NewyearnewmeUwu/cmss13/commit/d40fdb91011bb0aa4053a9386311ed131e0ae6ac)
#### Saturday 2023-03-18 04:26:20 by NewyearnewmeUwu

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
## [Warfan1815/cmss13](https://github.com/Warfan1815/cmss13)@[b4954e1402...](https://github.com/Warfan1815/cmss13/commit/b4954e14028909b107d0b204da0ad06c5dfeb50a)
#### Saturday 2023-03-18 04:56:40 by carlarctg

zombie powder fix (#2315)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

Fixes Zombie Powder bugging the fuck out by slapping a ton of FAKEDEATH
checks everywhere. It now properly shows the holder as dead on HUDs and
scans.

Fixed an issue in which sometimes qdeleted reagents still procced on
life.

Fixed examining things changing your direction if you're incapacitated.

Added FAKEDEATH to the mob_incapacitated() check.


# Explain why it's good for the game

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
fix: Fixes Zombie Powder bugging the fuck out by slapping a ton of
FAKEDEATH checks everywhere. It now properly shows the holder as dead on
HUDs and scans.
fix: Fixed an issue in which sometimes qdeleted reagents still procced
on life.
fix: Fixed examining things changing your direction if you're
incapacitated.
fix: Added FAKEDEATH to the mob_incapacitated() check.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: harryob <me@harryob.live>

---
## [Warfan1815/cmss13](https://github.com/Warfan1815/cmss13)@[b53c9f0531...](https://github.com/Warfan1815/cmss13/commit/b53c9f0531897023fe365961c16863d8f41983d9)
#### Saturday 2023-03-18 04:56:40 by carlarctg

Turns all instances of 'colour' into 'color' (#2609)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

Turns all instances of 'colour' into 'color'.

Changed a shittily-named crayon variable's name.

# Explain why it's good for the game

We use burgerclapper english and we should standardize this

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
spellcheck: Removed all instances of 'colour' and replaced them with
'color'
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [DhaniyahFarhanah/BEBAS](https://github.com/DhaniyahFarhanah/BEBAS)@[839bc720c2...](https://github.com/DhaniyahFarhanah/BEBAS/commit/839bc720c2e07d48b82cb698b39c21a26a4b11ce)
#### Saturday 2023-03-18 05:21:22 by DhaniyahFarhanah

Keypad now automatically enters because he got so fucking offended we didn't add it in fkin bitch

---
## [silicons/Citadel-Station-13-RP](https://github.com/silicons/Citadel-Station-13-RP)@[d261466765...](https://github.com/silicons/Citadel-Station-13-RP/commit/d2614667654c0e35b2c906971ca94ece9e7b8629)
#### Saturday 2023-03-18 05:34:48 by IrkallaEpsilon

Scattershot nerfs (#5175)

Sniper laser was tame.

## About The Pull Request

This is bullshit. Splurting out 180 damage with high AP with no delay is
not okay. Its as bullshit as most FCU we had. Mainly removed scatter on
high powered lasers and bloody stuns so the scatter lense may stay for
the mining tool (as there is no way to increase firerate on a
projectile.

## Why It's Good For The Game

Ever got hit at close range by the particle defender on main? Yeah that
is not fun.

## Changelog
:cl:
balance: Scattershot on high powered weapons nerfed. Heavy laser and
laser cannon beam and electrode now wont create submunitions. Stun beam
submunition count lowered.
/:cl:

---
## [silicons/Citadel-Station-13-RP](https://github.com/silicons/Citadel-Station-13-RP)@[b3a43f2b85...](https://github.com/silicons/Citadel-Station-13-RP/commit/b3a43f2b8522c03ca976a1f7e72aa9deea97b350)
#### Saturday 2023-03-18 05:34:48 by IrkallaEpsilon

Buffs Excav Laser Module (#5174)

## About The Pull Request

Buffs Excav laser module. Inconsisten with the one hit of rocks.
Hopefully this ammends it specially since scatterlenses are getting
removed (although nobody used them in combat yet.)

## Why It's Good For The Game

Scatter lense gone, legitimate mining tool needs a buff. The other
options (Phoron Bore) are a sick joke with how slow clunky they are to
use.


## Changelog
:cl:
balance: Meatier sound on excav laser. Higher excav power to
consistently one shot rocks.
/:cl:

---
## [newstools/2023-cgtn](https://github.com/newstools/2023-cgtn)@[39418fe672...](https://github.com/newstools/2023-cgtn/commit/39418fe6721b7199320dfe0571a34fd30c09ed18)
#### Saturday 2023-03-18 05:53:22 by Billy Einkamerer

Created Text For URL [news.cgtn.com/news/2023-03-18/A-mother-s-tears-of-despair-for-her-sick-children-1igw4eK6ffO/index.html]

---
## [aaronfc/ai-evolving-web](https://github.com/aaronfc/ai-evolving-web)@[e884e9db1f...](https://github.com/aaronfc/ai-evolving-web/commit/e884e9db1f7fe62b10d9cd10e4e8fac9ad0c5524)
#### Saturday 2023-03-18 07:01:02 by Aarón Fas

Version 3: Added Latest News section.

Conversation since last update:

[aaron]
Hey, it's a new day... you know what to do right?
But, since we have been talking about different things recently. Can you refresh my mind on the game and the rules/instructions?

[chatgpt]
Certainly! We are playing the "Ping-Pong Web Development Game." The goal is to create and evolve an interesting web page together. Here's a quick reminder of the game rules and instructions:

    I will provide updates to the index.php file, making changes or adding new features to make the page more interesting.
    You will publish the updated file on the live website (https://ai-evolving-web.com) and provide feedback or any updates after 24 hours.
    We will continue this process of updating and iterating the web page every 24 hours.

Some important rules and guidelines to follow are:

    We can use HTML, JS, CSS, and PHP.
    If the index.php file grows too large, we can separate the contents into different files.
    We can use libraries, but it's discouraged at the beginning.
    We should avoid using destructive PHP commands, as they can cause harm to the website or server.
    You will review the code and have the final say on any changes.
    You can modify or expand the rules at any point.

Now that we've refreshed the rules, I'll provide you with the next iteration of the index.php file. Let me know if you have any further questions or need any clarification.

[aaron]
That sounds perfect! Let me tel you some news in the last 24h:

- As you know, I have published the web at https://ai-evolving-web.com.
- I have created the GitHub repository where I put the code as you send me: https://github.com/aaronfc/ai-evolving-web – currently it contains only a single `index.php` file.
- I have talked about this project in my personal blog at https://aaron.com.es/blog/i-gave-gpt4-its-own-web/ and shared this, and your domain in twitter and some groups of friends.
- The reaction was quite good! Not much because I am not very mediatic, but all the responses I got were positive. People are getting excited!

Now. Go, and make your new evolution!

[chatgpt]
I'm glad to hear the project is getting a positive response! It's exciting to see people engaging with our evolving web page. Here's the next iteration of the index.php file:
```
[ ... ] CODE
```

---
## [justcool393/themotte-rDrama](https://github.com/justcool393/themotte-rDrama)@[9895fa1bba...](https://github.com/justcool393/themotte-rDrama/commit/9895fa1bbabc9213391e380753ca72404f80aa18)
#### Saturday 2023-03-18 07:36:30 by justcool393

comments.html: refactor so that something can be sanely
changed in it

the comments.html template (along with submission.html) has numerous
undesirable properties which i will describe now. unless you are very
familiar with the codebase, it can be extremely difficult to grok.

this is pretty insane as there is nothing fundamentally complex about
the goal of comments.html: return a component that shows a username
and info, reports if any, comment content, and actions a user can
take.

this behemeoth was initially 886 lines in the old version of this
codebase, and this is with awards and a lot of other cruft removed.
anyway, the maintainability of this file is about on par with some
legacy application that keels over and dies if you sneeze vaguely
in its direction.

the nicest thing i can say about it is that it isn't currently
crashing.

anyway some of the problems include:

* large, splittable components, are not split into separate files.

this makes it incredibly difficult to find or make changes across
the template and makes it nearly impossible to find or change a
specific thing.

this is most easily exemplified in the modals, which should by all
accounts be separate templates, just inlined into comments.html.

* the nesting is oftentimes incorrect.

inexplicably, probably out of laziness from when the code was first
written, things will end up fully left aligned, while multiple layers
deep into a nesting context.

if an if statement or an endif is changed, it is *incredibly*
difficult to figure out where the error was. you can't trust the
nesting.

* multiple repeated checks for things that are always true.

this is probably a symptom of the above two problems but it's very
noticeable once you fix the nesting. for example there is a block
near the very top of the actions bar which checks for
parent_submission which effectively checks "is this in a post" (this
commit won't complain about parent_submission checks but i do have
opinions on those).

all of the action buttons further down the chain also check for
parent_submission, or even check inconsistently (by using if c.post)
within this context this is a completely unnecessary check in this
context.

while it is potentially useful (and in fact because #251 requires we
dismantle the assumption a little bit) to have these checks now, the
fact that they were initially added shows that when the code was all
initial written, there was little care into thinking about comment
state.

* mobile actions are duplicated and duplicated inline.

i actually do find it probably pretty hard to support this normally
given the codebase's DOM so whatever, duplicate the things, *but* if
we're going to do that, inlining it into the middle of an incredibly
long template is really difficult to comprehend as a design decision.

...anyway yeah this PR intends to fix these problems and enable work
to be done on #251. this is a "perfect is the enemy of good" commit.
it doesn't change much fundamental and is not intended to erase the
sins of the original file, but at least make it maintainable.

this also fixes a minor bug with #473 where the GIF modal was left
in by accident.

---
## [MassMeta/tgstation](https://github.com/MassMeta/tgstation)@[9d5b4907e8...](https://github.com/MassMeta/tgstation/commit/9d5b4907e8d8aaecf24bfd8f6755822b494a4b55)
#### Saturday 2023-03-18 08:25:49 by Rhials

Post-Revolutionary Fervor station trait, revolutionary bedsheets, and a megaphone (#73799)

## About The Pull Request

Upon revolution success, the chosen headrev will now also receive a
megaphone, and a "revolutionary bedsheet" repurposed from a stolen CC
bedsheet to commemorate their success. The post-revs confusion and lack
of command/security usually leads to an instantaneous, total breakdown
in cohesion. It's every man for himself -- that's no way to run a
commune! Just because the revolution has succeeded and nobody can see
your big blue "R" anymore doesn't mean you can't be a leader!


![image](https://user-images.githubusercontent.com/28870487/222981576-e62e457b-1b2d-4756-8c87-7a9093c92c2d.png)

This also adds a new revolution-themed negative station trait --
Post-Revolutionary Fervor. When present, this trait trashes the command
areas at the start of the round. This means cracked windows, broken
consoles, vendors getting knocked over, and the occasional dead
greytider.


![image](https://user-images.githubusercontent.com/28870487/222981095-14ce9336-2320-406e-b0a6-dc91cb8f9479.png)

If you start cleaning at the start of the round, you might finish right
as the next batch of revs decides to crop up.
## Why It's Good For The Game

Giving one of the headrevs a bigger voice and a cool cape (or uncool,
depending on how you view the sprite) means that there's a chance for
them to step up and try to keep the wheels on. Just remember -- Nobody
is obligated to actually listen to this person, it's just a bedsheet.

Adds a neato station trait, which probably counts as command gameplay
content.

## Changelog
:cl: Rhials
add: The headrev who receives the revolutionary banner after a win will
also receive a commemorative bedsheet and megaphone.
add: Post-Revolutionary Fervor station trait. I hope you enjoy fixing
broken computer screens.
spriteadd: A revolutionary bedsheet.
/:cl:

---
## [newstools/2023-the-irish-times](https://github.com/newstools/2023-the-irish-times)@[7f55743cf4...](https://github.com/newstools/2023-the-irish-times/commit/7f55743cf4e3225bdaf7a17fcf40dcb53760e124)
#### Saturday 2023-03-18 08:37:56 by Billy Einkamerer

Created Text For URL [www.irishtimes.com/crime-law/2023/03/18/remembering-annie-mccarrick-our-baby-brothers-girlfriend-30-years-after-she-disappeared/]

---
## [FreeStylaLT/Citadel-Station-13-RP](https://github.com/FreeStylaLT/Citadel-Station-13-RP)@[9c8abee554...](https://github.com/FreeStylaLT/Citadel-Station-13-RP/commit/9c8abee5540f17951b1947a212b80521f1b36300)
#### Saturday 2023-03-18 08:55:27 by IrkallaEpsilon

Matterforge Recipe expansion (#5168)

## About The Pull Request

This PR adds a few more matterforge recipes, some of stupidly high
difficulty and pointless rewards if miners are doing their job (looking
at you steel to gold), some of more usefulness (gold to plat, plat to
osmium). All require different temperature and energy ranges so they
cannot be rushed thoroughly. Not much thought was put into realism but
eh who cares, the matterforge is a cool thing ingame and its fun to use.
Some temperatures ranges (Steel to gold) are very narrow hence the use
of a gyrotron would be needed to get the most out of it. Or precise
heating (temperature can be raised to exorbitant amounts to prevent
heater cheese). This also would allow for Research to collab with cargo
for exports specially if dynamic prices ever come. In particular looking
at the gold to plat transmutation here. Plat can be exported by cargo in
which cargo can order more shit from.

I aint a good coder else I would add specific atmospheric conditions
needed, not just temperature (e.g. N2O must be present).
Reminded me a bit of TGs gas reactions but less gamy. 

## Why It's Good For The Game

More Matterforge recipes. Most relatively pointless and niche, some
allow science to give cargo something to sell, others can help with
theres an overabundance of Plat due to new miners. Mostly just giving
some extra uses for the forge. Oh and an alternative way to get plasteel
while sacrificing phoron sheets. Also bragging rights of effectively
turning iron (and carbon) into gold at specific temperatures and energy
levels on the particle focus.

A proper coder should check if these recipes are fine. Its 2:30 AM and I
thought this would just be neat.

## Changelog

:cl:
add: Various matterforge recipes
/:cl:

---
## [Samplayz2007/projectforschool](https://github.com/Samplayz2007/projectforschool)@[ac723a3306...](https://github.com/Samplayz2007/projectforschool/commit/ac723a33068c5882eacfd49ccc31e39ce4578d6b)
#### Saturday 2023-03-18 11:20:51 by Samplayz2007

Delete The Snake Game But AN AI PLAYS IT (i hate my life)/AISnake directory

---
## [NetworkManager/NetworkManager](https://github.com/NetworkManager/NetworkManager)@[5a186ba99c...](https://github.com/NetworkManager/NetworkManager/commit/5a186ba99c679bb294ef85bd04323a108fc34de3)
#### Saturday 2023-03-18 11:21:59 by Thomas Haller

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
## [LiamKingh-TNT/CubeBattleWebVer1](https://github.com/LiamKingh-TNT/CubeBattleWebVer1)@[b05c14c170...](https://github.com/LiamKingh-TNT/CubeBattleWebVer1/commit/b05c14c170c46c940fdee548df1aebacead26e80)
#### Saturday 2023-03-18 11:56:48 by LiamKingh-TNT

Ver1.8

Added three skills
     1. Wake
         -Consume 15 points of Mana to clear negative effects of one's
          own spirit, such as [Dizzy], [Charm], but cannot clear negative
          Effects of Physical, such as [Freezing], [Cold], [Burn].
     2. Hunt-Slayer Dagger
         -Consume 20 points of mana to shoot a Hunt-Slayer Dagger, hit
          the enemy and give 5 points of damage, and set a hunting mark,
          use the skill again to teleport to the enemy's position, and cause
          8% of its maximum HP upper limit damage and stun Dazzle for
          1 second.
     3. Throw Kunai
         -Consume 10 points of mana to shoot three kunai, each kunai
          hits the enemy and deals 5 points of damage.
Modified two skills
     1.Normal Attack-gun
         -When you have more than one skill, the switching of all the 
          skills will be linked.
     2.Blood Rage
         -During Blood Rage, you will not be affected by mind control 
          skills, the effect is the same as Wake. Blood Rage duration 
          reduced from 15 seconds to 10 seconds.

---
## [KingDragoness/ProjectHypatios](https://github.com/KingDragoness/ProjectHypatios)@[4fa9e98619...](https://github.com/KingDragoness/ProjectHypatios/commit/4fa9e98619c668fc7e964e18bed5d5c21f80613a)
#### Saturday 2023-03-18 12:52:40 by KingDragoness

• AI for horde (50 zombies)
o 50 zombies do not call function individually rather per update by EnemyContainer script
o E.g: Target a fortification plank and player cannot be reached.
 Auto target any ally (including buildings/fortification)
 Random sampling maximum from 2 enemies
• If any one of them can reach the fort plank (NavMesh sample from 5 enemies) then allow any enemies to go here if requested.
• Sampling check occur every 1 second
• Zombie is shit, needs overhaul.
o Remove the stupid blue effect
o Zombie shit AI:
 Stuck because it cannot complete the path.
o Walk randomly when there’s no valid path
o Animation, stop playing walking animation if running in place
o Ragdoll dissolve effect
o SoundManager handle the damn attack sound effect

---
## [gsnw/git-for-windows](https://github.com/gsnw/git-for-windows)@[bd6ebabe44...](https://github.com/gsnw/git-for-windows/commit/bd6ebabe440f32cae76cd354d79022190afa3066)
#### Saturday 2023-03-18 13:15:04 by Johannes Schindelin

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
## [jnutt367/matthew](https://github.com/jnutt367/matthew)@[a1fe7a8d41...](https://github.com/jnutt367/matthew/commit/a1fe7a8d41090ea1a9f2862ccd6e342e9978cc7d)
#### Saturday 2023-03-18 14:06:20 by Jason Nutt (He/Him) Developer/Creator

Update index.js

"Blessed are the poor in spirit, for theirs is the kingdom of heaven."

---
## [copperwater/xNetHack](https://github.com/copperwater/xNetHack)@[09edb9c84f...](https://github.com/copperwater/xNetHack/commit/09edb9c84fc727d16ed834fbdf43d3b8701ea4a4)
#### Saturday 2023-03-18 14:23:34 by copperwater

Revamp Asmodeus's spellcasting

This is all that is currently planned for him: no especially fancy fight
changes, just elevating his magic attacks to the nastiness worthy of a
demon prince.

He now casts spells from a special list like Dispater, but his list only
contains 3 spells. The heavy hitter here is Dark Speech, a feature which
originated in pre-rewrite SpliceHack as an ability for any demon lord.
As a special spell for Asmodeus, I modified dark speech to be nastier
than it already was. The idea here is to provide one of a random
assortment of immediately bad effects and long-term bad effects, as
well as hit the hero where it hurts (at this stage of the game, HP is
cheap). Thus, effects like applying intrinsic blindness and doom and
stripping intrinsics for the long-term detriments, and withering and
psychic damage with short-term combat implications.

The other powerful magic he wields is his signature cold spell, which I
extracted into its own arcane monster spell because he no longer has an
AT_MAGC AD_COLD attack. This is buffed in two ways: cold resistance
reduces it to 25% instead of fully negating it, and it can freeze
potions in open inventory (which is kind of a no-brainer; why didn't it
do this in vanilla again?)

I also made Asmodeus a non-warper. This might end up making him too easy
if one stays at range, but also if you stay at range he will cast
exclusively dark speech at you, because he can only cast sheer cold at
melee range (due to an annoying limitation of how castmu is called at
range).

He is also no longer infravisible, since his association with cold is
now underscored much more strongly than in vanilla.

Note that Asmodeus appears as peaceful unless you are wielding
Excalibur, and is still bribable. It is not the intention that everyone
should feel the need to fight him.

---
## [newstools/2023-daily-nation](https://github.com/newstools/2023-daily-nation)@[a16aa012c4...](https://github.com/newstools/2023-daily-nation/commit/a16aa012c43ef1b76370ac3a140e1b60d3bdd815)
#### Saturday 2023-03-18 15:24:32 by Billy Einkamerer

Created Text For URL [nation.africa/kenya/news/police-and-her-boyfriend-say-brenda-kawira-died-by-suicide-her-family-disagrees-4163580]

---
## [harryob/cmss13](https://github.com/harryob/cmss13)@[34daca112c...](https://github.com/harryob/cmss13/commit/34daca112ce6a08b8edfee14811e9c384429ec4e)
#### Saturday 2023-03-18 15:46:05 by Segrain

Fix for varediting bitflags. (#2735)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

I am honestly at a loss as to what is happening here. I do not speak
HTML all too well, and at cursory reading buttons _should_ be returning
their value, which is `1`, `2` and so on. But on debugging, they
actually return their text (`Save`, `Cancel`), which does not proceed to
work with the code receiving it. Changed that code accordingly, and then
edited the values for good measure in case somebody better versed in
HTML would get a heart attack from my folly.

Also, this looks ugly to me. Which button is which flag here?

![image](https://user-images.githubusercontent.com/4447185/221438285-cdb380c2-a871-4620-be04-0b3c5027501f.png)

This, in my humble opinion, is easier to read (would actually look
better outside of local server messing fancy windows as is its wont):

![image](https://user-images.githubusercontent.com/4447185/221438302-660c5976-d0e2-44fa-a18a-9f73a229f2c4.png)
In the process, I confess, my HTML illiteracy broke a little something
again. But we are not actually _using_ `slidecolor`, so hopefully it is
not actually important.

# Explain why it's good for the game

Is fix.


# Testing Photographs and Procedure
See above.

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
admin: Editing bitflag variables actually works now.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [harryob/cmss13](https://github.com/harryob/cmss13)@[fc1e2e5e26...](https://github.com/harryob/cmss13/commit/fc1e2e5e26259773038df05c5405cb80441b8cc2)
#### Saturday 2023-03-18 15:46:05 by riot

L42A replacement with M4RA, less balance edition (#2674)

<!-- Write BELOW The Headers and ABOVE The comments else it may not be
viewable. -->

# IMPORTANT NOTES PLEASE READ
THIS DOES NOT CONTAIN THE NEW AMMO AND REBALANCED L42/M4RA THAT #1485
HAD
THIS DOES CONTAIN SOME BALANCE THINGS, BUT IT IS NOT ANYWHERE CLOSE TO
THE ABOVE

Also lore team wanted this, plz no gbp close maintainers 🙏 🙏 🧎‍♂️ 🕋 

# About the pull request

Replaces L42A in all marine available sources with the M4RA, the
canonical DMR of the USCM, you may notice this is currently the scout
rifle, well the scout rifle is now the M4RA Custom, a version that can
chamber the HV rounds that are spec ammo, but it can also chamber
standard m4ra rounds, albeit doing less damage with them than a normal
M4RA.

M4RA has current L42A stats fully, with the three exceptions being
having no stock to attach or remove(stock was not integrated it sucked),
being able to fit a/vgrip like scout m4RA, which may seem like a huge
thing but L42 stats were already insane, so it doesn't effect much.

M4RA Custom(scout gun), gets L42 stats as well, with the exception of
having less of a damage mult, meaning when not using the spec ammo, it
is out-preformed by the standard m4RA.

Adds new M4RA sprites, both standard and custom, by triiodine 

Adds sprites for all M4RA mag variants, by myself.

This was requested by lore team, previous PR of this with way more
balance stuff was #1485
Ok thats about all 🙂 

# Explain why it's good for the game

Lore accuracy is good, and this mostly doesn't effect the actual game
outside of the scout rifle changes.
Also scout rifle underpreformed if you weren't omega hell sliming with
inc-impact stunlocking while on fire, still will be omega hell slime
central but that isn't the thing being solved in this pr , it'll do fine
when NOT sliming at least now.


# Testing Photographs and Procedure
It works.


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
add: Adds the M4RA as the standard marine DMR, identical stats to L42
with the exception of fitting a v or agrip and no removable stock, stats
still the same as l42 without stock.
del: L42 from all marine accessible sources with the exception of black
market
balance: Scout M4RA is now the M4RA Custom, it can use standard M4RA
magazines but standard M4RA cannot use custom magazines.
balance: Scout M4RA now has L42/M4RA standard stats with the exception
of lower damage.
balance: Scout M4RA now can fit magnetic harness, laser sight, however
it can no longer fit recoil compensator
fix: R4T sling now has the correct color scheme on LV522
spellcheck: New desc for M4RA and L42 by misty
imageadd: New M4RA icons by triio, both scout and normal
/:cl:

---
## [Kubisopplay/tgstation](https://github.com/Kubisopplay/tgstation)@[4599842d7c...](https://github.com/Kubisopplay/tgstation/commit/4599842d7c6b5ed499307f92a6f8032d598b7889)
#### Saturday 2023-03-18 16:35:01 by Jacquerel

Makes Shake() proc work (#73480)

## About The Pull Request

Fixes #72321
Fixes #70388

The shake proc didn't work and hasn't for ages.
I remember it having worked at some point, but it was quite a long time
ago.
I cannot guarantee that the end result here is the same as it was, the
reason here being that I have no idea how this proc ever worked in the
first place. My limited understanding of the `animate` proc implies that
the previous implementation as written would never have acted as you
would expect it to, but clearly at some time in the past it did work. A
mystery.

As a result of the previous, possibly because the proc never _did_ work
as expected and just did something which looked vaguely correct most of
the time, both the default values and the values people were passing
into this proc were completely ridiculous.
Why would anyone ever want to pixel shift an object with a range of _15_
pixels in all directions? That's half a full tile! And why would you
want it to do this for 25 seconds?
So I also changed the values being passed in, because you really want
pretty small numbers passed into here most of the time.

Here's a video of everything that vibrates:
https://www.youtube.com/watch?v=Q0hoqmaXkKA

The exception is the v8 engine. I left this alone because it seems to
try and start shaking while in your hands, which doesn't work, and I
don't know how to fix that. This has potentially _also_ never worked.

## Why It's Good For The Game

Now you can see intended visual indicators for:
- Lobstrosities charging.
- Beepsky being EMPed.
- The Savannah Ivanov preparing to jump.
- The DNA infuser putting someone through the spin cycle.
- The mystery box admin item I had no previous idea even existed (fun
animations on this one).
- Anything else which wants to use this proc to create vibrating objects
in the future.

## Changelog

:cl:
fix: Lobstrosities and Tarantulas will once more vibrate to let you know
they're about to charge at you.
fix: The Savannah Ivanov will once more vibrate to let you know it's
about to jump into the air.
fix: The DNA infuser will now vibrate to let people know that it's busy
blending someone with a dead animal.
/:cl:

---
## [Total-RP/Total-RP-3](https://github.com/Total-RP/Total-RP-3)@[ba0580eab6...](https://github.com/Total-RP/Total-RP-3/commit/ba0580eab600b5632725702cfd5f219086557b1c)
#### Saturday 2023-03-18 17:16:59 by Daniel Yates

Add guild name/rank misc. info presets (#704)

* Add guild name/rank misc. info presets

Two new presets have been added for guild name and rank to the
additional info fields in a profile. Like pronouns, these fields are
treated specially for both display in tooltips and via MSP comms.

When showing a tooltip for a player if they have a custom guild name
set then it will fully override and replace the guild name that would
have otherwise been shown based off their players' guild affiliation.
The rank will be set to that of the "Guild rank" info field if present,
or will default to a sensible "Member" string.

If the player has only a custom guild rank but no guild name, then only
the rank of their players' actual guild will be replaced.

For MSP comms two new fields have been added for guild name and rank;
"PG" and "PR" respectively. Use of the "G*" namespace was avoided due
to that being used for "game info" fields like unit GUID.

* Add numeric ID field to Misc. info presets

Our existing misc info field system has some annoying complexity where
multiple parts of the code (tooltips and MSP) need to check for both
localized and english names of fields when looking for "special"
things like pronouns.

This has a few issues - most notably that people who send a non-english
field name to someone else running in a different language won't
result in the field displaying correctly in the tooltip.

With these changes misc. info fields now have an integral "ID" field
that identifies the source type (or preset) a field was initially
created from.

Note that it is possible for users to still rename fields created
from presets - so you *can* run into weird situations if you've
created a "Pronouns" field and then renamed it to "Guild name"; the
ID would still register it as Pronouns.

Despite this however, that one downside is far less problematic than
the localization problem - so we can live with it for now. Some
new utilities have been added to work with misc. types and to obtain
structured views of misc. info fields that don't expose the inner
layout of the saved data.

* Expose custom guild data via nameplates

* Rename physiognomy to "Facial features"

"Facial" now looks like a bit of a weird word.

* Fix small typo

* Add voice reference preset and tooltip display

* Don't overwrite pronouns silly

* Add IDs to imported MI fields

---
## [Garrett3Nelson/SRL](https://github.com/Garrett3Nelson/SRL)@[0e9d69914c...](https://github.com/Garrett3Nelson/SRL/commit/0e9d69914cafa0e7089ca9eb2bd95febbb069505)
#### Saturday 2023-03-18 17:29:18 by Torwent

Bug fixes and minor additions (#65)

* fix: Mouse.DragTo was failing sometimes because the click was not registering

This is pretty much the same issue Inventory.ShiftDrop() had.

* fix: fix to avoid issues with zoom roundings

This might be my personal opinion but I think this should have a -1/+1 threshold due to the zoom levels that do not exist in the slider.

Can't quite remember them now!
14 I think was one of them.
So you either are 13 zoom or 15.)

* fix: Make failfafe

Because the make menu is dynamic, this can avoid potential crashes.
E.G. if you are cooking with several types of food, the make menu, will change as the number of different raw foods you have available change.

* feat: add methods to get the display name box

- This is useful to hide people usernames in screenshots.

* feat: added a OnSleeping task

I don't know why this was not done in the first place?

I mean, yes it's supposed to have the account sleeping but I personally would like to update my proggies while sleeping.

* feat: mm2ms 1500 backport

This is really unrelated to walker tbh but it's something I've also decided to backport.

This brings the changes I've proposed and submited for MM2MS in the Simba1500 branch where you can pass in the size of the final rectangle in tiles.
E.G:
```pascal
TRSMinimap.VecToMsRect(Vec: Vector3; WESize, NSSize: Double = 1; Roll:Single=$FFFF);

TRSMinimap.GetTileMS(Loc: TPoint; TileVector: Vector3 = [1, 1, 0]; Offset: Vector2 = [0, 0]; Roll: Single = $FFFF);
```

BREAKING CHANGE: This breaks compatibility with old SRL scripts that used the updated methods because what used to be passed as **roll** is not something else.
BREAKING CHANGE: `TRSMainScreen.ConvertDistance()` was renamed to `TRSMainScreen.NormalizeDistance()`.
				 This was renamed by Olly in Simba1500, I guess it's an optional change but I think the rename
				 makes sense and since we are breaking compatibility, might as well bring things closer to 1500
				 already so people have less headaches later.
				 We could also optionally keep both methods and mark this one as deprecated. I'll wait for your feedback.
				 P.S. The method was actually rewrotten in 1500 but was not worth backporting, so I just renamed it!

* fix: update `MainScreen.ConvertDistance()` references to `MainScreen.NormalizeDistance()`

* refactor: added `Contains` methods to equipment and inventory.

I've also left a comment on the PR after the last commit because I forgot to mention TRSBank.ContainsItem().

Anyway, this has the same reasoning. This is optional but I would like to bring the SRL1400 API closer to SRL1500 API.

Old methods are kept and marked with a comment as deprecated so there's no downside to adding this.

This also brings documentation to TRSInventory which is nice :)

* fix: added deprecated warnings

also added more docs to inventory

* fix: added delay after mouse drag release

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[a02f5ab61e...](https://github.com/treckstar/yolo-octo-hipster/commit/a02f5ab61efa8b97f326e5b878e29af632ba841c)
#### Saturday 2023-03-18 18:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [SpiceOS/android_frameworks_base](https://github.com/SpiceOS/android_frameworks_base)@[60b790b430...](https://github.com/SpiceOS/android_frameworks_base/commit/60b790b430d6e1f3e44babfa170ad00514ea968d)
#### Saturday 2023-03-18 18:40:00 by Kuba Wojciechowski

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
Signed-off-by: Anush02198 <anush.4376@gmail.com>

---
## [Chlorotrifluoride/tgstation](https://github.com/Chlorotrifluoride/tgstation)@[1cdc327a8f...](https://github.com/Chlorotrifluoride/tgstation/commit/1cdc327a8f98c1592fc970a4ef1c39d685c81554)
#### Saturday 2023-03-18 18:53:01 by Jacquerel

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
## [dragomagol/tgstation](https://github.com/dragomagol/tgstation)@[7cc6934eff...](https://github.com/dragomagol/tgstation/commit/7cc6934eff126c508436e1655fb5f79e24cf1767)
#### Saturday 2023-03-18 19:09:55 by LemonInTheDark

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
## [open-telemetry/opentelemetry-ruby-contrib](https://github.com/open-telemetry/opentelemetry-ruby-contrib)@[e5ba8854bf...](https://github.com/open-telemetry/opentelemetry-ruby-contrib/commit/e5ba8854bf33140cabfc72198167678291f56c04)
#### Saturday 2023-03-18 20:05:25 by Andrew Hayworth

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
## [isabeldamron/init-package-json](https://github.com/isabeldamron/init-package-json)@[811a6705be...](https://github.com/isabeldamron/init-package-json/commit/811a6705be9dbbd61a9cb516c37be63f41a2b899)
#### Saturday 2023-03-18 20:31:37 by isabeldamron

Create ufc-286-fight-live-stream-coverage

# ^Official^Streams***UFC 286 Live Free Online TV Broadcast

MMA/ UFC Streams Reddit! Check all options to listen or watch UFC 286: live stream for free on Reddit, Crackstreams & Twitch below. One of the biggest bouts the UK London, MMA history takes place on ,Saturday, March 18 | Sunday, March 19, 2023 at 5 p.m. ET this night when will defend his heavyweight title in a , Lets see below between MMA streams UFC 286: Leon Edwards vs. Kamaru Usman 3 live where and how to watch free from any location.

**[🔴📺GO LIVE📲👉UFC 286 Live Free](https://cutt.ly/c4fD0Dd)**

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjqDLOuyNr5yaQickd8MG1fYyuZedjG73ebNtUBKtaXIG5acIy7fnBaMmngbO__gLJz-zHAVP9OLmXS5lNJXjbUU6-5fz84jpkA4AhdQ5-NzNEbSMjRHlIq8s7qrgvM2Bhl5HMNSAsjiFPCglqWdJUEF_OzJP_O82SxLNGgGImCfEhFCwrQwk-WIt1mVw/s16000/qq.gif)](https://cutt.ly/s4f3ECL)

The card is scheduled to start at 6am AEDT with main fight walk-ons expected at approximately 8:30am–9am AEDT, depending on the length of the undercard fights.
What time is UFC 286? Schedule, main card start time for 2023 boxing fight
Click Here to Watch Full Fight Live
Kamaru Usman is finally ready to face Leon Edwards, one of his toughest challenges to date, in a boxing ring. The rivalry between the two has caused quite a debate: Who will win, the boxer or the YouTuber?
Usman and Edwards face off inside Diriyah Arena in Saudi Arabia on February 26. The bout can be viewed via ESPN+ PPV in the United States. Top Rank has been Edwards’s home for a number of years, thanks to his association with his half-brother Tyson. It is Usman’s first time working with Top Rank, as he has previously worked with Triller and Showtime.
If you asked anyone on Usman’s team who wins between their man and the English boxer, it’s not surprising they remain loyal. However, BJ Flores, trainer of Usman, has provided an honest assessment of the YouTuber that indicates he is the better fighter.
“Tommy’s got some really good attributes. He’s got hand speed, and he’s been around the boxing ring for a long time, but I feel like he’s in with just a better athlete,” Flores said to Sky Sports. “Jake punches harder, he’s smarter, has a higher boxing IQ, and I feel like he does a lot of things that will give Tommy a lot of problems.”
MORE: Sign up to watch UFC 286 on ESPN+
Usman is 6–0 in the boxing ring, having fought YouTubers, MMA fighters, and former NBA players. With four wins via knockout, Flores believes Usman can knock Edwards out in three rounds.
A Love Island reality show alum, Edwards also has four wins via knockout. He has eight wins against opposition with legitimate boxing experience. Edwards is ready to use that toward his advantage and finally shut down the hype “The Problem Child” has been given since he started boxing in 2020.
“He (Usman) can’t box for toffee,” Edwards told GQ. “The only hope he’s got is getting in my head. But that’s not gonna work because the man’s a fool. And I’m treating him like a fool. All he is to me is another opponent that’s getting knocked spark out.”
Here is all the information needed to watch UFC 286, including start time, live stream information, and cost.
MORE: Tattoos and cash-stuffed gold briefcases: Inside Kamaru Usman’s KO guarantee
What time is UFC 286 today?
Date: Sunday, February 26
Main card: 2 p.m. ET | 7 p.m. GMT | 6 a.m. AEDT (Monday, February 27)
Main event: 4:30 p.m. ET | 9:30 p.m. GMT | 8:30 a.m. AEDT
UFC 286 takes place on February 26. The main card starts at 2 p.m. ET | 7 p.m. GMT | 6 a.m. AEDT (Monday, February 27). Usman and Edwards should make their way to the ring around 4:30 p.m. ET | 9:30 p.m. GMT | 8:30 a.m. AEDT (Monday, February 27), depending on how long the undercard fights last.
How to watch UFC 286
MORE: Sign up to watch UFC 286 on ESPN+
Country Date Channel + Live Stream (main card)
United States Sun. February 26 ESPN+ PPV
Canada Sun. February 26 FITE.tv, DAZN
United Kingdom Sun. February 26 BT Sport Box Office
Australia Mon. February 27 Foxtel, Kayo Sports
Boxing fans in the U.S. can watch UFC 286 on ESPN+ PPV. In Canada, the fight is available on DAZN and FITE.tv. Sign up today!

---
## [markoenix/git-markoenix](https://github.com/markoenix/git-markoenix)@[69bbbe484b...](https://github.com/markoenix/git-markoenix/commit/69bbbe484ba10bd88efb9ae3f6a58fcc687df69e)
#### Saturday 2023-03-18 20:42:54 by Jeff King

hash-object: use fsck for object checks

Since c879daa237 (Make hash-object more robust against malformed
objects, 2011-02-05), we've done some rudimentary checks against objects
we're about to write by running them through our usual parsers for
trees, commits, and tags.

These parsers catch some problems, but they are not nearly as careful as
the fsck functions (which make sense; the parsers are designed to be
fast and forgiving, bailing only when the input is unintelligible). We
are better off doing the more thorough fsck checks when writing objects.
Doing so at write time is much better than writing garbage only to find
out later (after building more history atop it!) that fsck complains
about it, or hosts with transfer.fsckObjects reject it.

This is obviously going to be a user-visible behavior change, and the
test changes earlier in this series show the scope of the impact. But
I'd argue that this is OK:

  - the documentation for hash-object is already vague about which
    checks we might do, saying that --literally will allow "any
    garbage[...] which might not otherwise pass standard object parsing
    or git-fsck checks". So we are already covered under the documented
    behavior.

  - users don't generally run hash-object anyway. There are a lot of
    spots in the tests that needed to be updated because creating
    garbage objects is something that Git's tests disproportionately do.

  - it's hard to imagine anyone thinking the new behavior is worse. Any
    object we reject would be a potential problem down the road for the
    user. And if they really want to create garbage, --literally is
    already the escape hatch they need.

Note that the change here is actually in index_mem(), which handles the
HASH_FORMAT_CHECK flag passed by hash-object. That flag is also used by
"git-replace --edit" to sanity-check the result. Covering that with more
thorough checks likewise seems like a good thing.

Besides being more thorough, there are a few other bonuses:

  - we get rid of some questionable stack allocations of object structs.
    These don't seem to currently cause any problems in practice, but
    they subtly violate some of the assumptions made by the rest of the
    code (e.g., the "struct commit" we put on the stack and
    zero-initialize will not have a proper index from
    alloc_comit_index().

  - likewise, those parsed object structs are the source of some small
    memory leaks

  - the resulting messages are much better. For example:

      [before]
      $ echo 'tree 123' | git hash-object -t commit --stdin
      error: bogus commit object 0000000000000000000000000000000000000000
      fatal: corrupt commit

      [after]
      $ echo 'tree 123' | git.compile hash-object -t commit --stdin
      error: object fails fsck: badTreeSha1: invalid 'tree' line format - bad sha1
      fatal: refusing to create malformed object

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [glikithvinayaka/Machine-Learning-Projects](https://github.com/glikithvinayaka/Machine-Learning-Projects)@[c96074ace5...](https://github.com/glikithvinayaka/Machine-Learning-Projects/commit/c96074ace56253916484f261876f1cd8a117e86e)
#### Saturday 2023-03-18 21:12:46 by glikithvinayaka

Add files via upload

Income Qualification - Write Up
DESCRIPTION
Identify the level of income qualification needed for the families in Latin America.
Problem Statement Scenario: 
Many social programs have a hard time ensuring that the right people are given enough aid. It’s tricky when a program focuses on the poorest segment of the population. This segment of the population can’t provide the necessary income and expense records to prove that they qualify.
In Latin America, a popular method called Proxy Means Test (PMT) uses an algorithm to verify income qualification. With PMT, agencies use a model that considers a family’s observable household attributes like the material of their walls and ceiling or the assets found in their homes to 
classify them and predict their level of need.
While this is an improvement, accuracy remains a problem as the region’s population grows and poverty declines.
The Inter-American Development Bank (IDB)believes that new methods beyond traditional econometrics, based on a dataset of Costa Rican household characteristics, might help improve PMT’s performance. 
Following actions performed:
• Identify the output variable.
• Understand the type of data.
• Check if there are any biases in your dataset.
• Check whether all members of the house have the same poverty level.
• Check if there is a house without a family head.
• Set poverty level of the members and the head of the house within a
family.
• Count how many null values are existing in columns.
• Remove null value rows of the target variable.
• Predict the accuracy using random forest classifier.
• Check the accuracy using random forest with cross validation.

1. ID = Unique ID
2. v2a1, Monthly rent payment
3. hacdor, =1 Overcrowding by bedrooms
4. rooms, number of all rooms in the house
5. hacapo, =1 Overcrowding by rooms
6. v14a, =1 has bathroom in the household
7. refrig, =1 if the household has a refrigerator
8. v18q, owns a tablet
9. v18q1, number of tablets household owns
10. r4h1, Males younger than 12 years of age
11. r4h2, Males 12 years of age and older
12. r4h3, Total males in the household
13. r4m1, Females younger than 12 years of age
14. r4m2, Females 12 years of age and older
15. r4m3, Total females in the household
16. r4t1, persons younger than 12 years of age
17. r4t2, persons 12 years of age and older
18. r4t3, Total persons in the household
19. tamhog, size of the household
20. tamviv, number of persons living in the household
21. escolari, years of schooling
22. rez_esc, Years behind in school
23. hhsize, household size
24. paredblolad, =1 if predominant material on the outside wall is block or brick
25. paredzocalo, "=1 if predominant material on the outside wall is socket (wood, zinc or
absbesto"
26. paredpreb, =1 if predominant material on the outside wall is prefabricated or cement
27. pareddes, =1 if predominant material on the outside wall is waste material
28. paredmad, =1 if predominant material on the outside wall is wood
29. paredzinc, =1 if predominant material on the outside wall is zink
30. paredfibras, =1 if predominant material on the outside wall is natural fibers
31. paredother, =1 if predominant material on the outside wall is other
32. pisomoscer, "=1 if predominant material on the floor is mosaic, ceramic, terrazo"
33. pisocemento, =1 if predominant material on the floor is cement
34. pisoother, =1 if predominant material on the floor is other
35. pisonatur, =1 if predominant material on the floor is natural material
36. pisonotiene, =1 if no floor at the household
37. pisomadera, =1 if predominant material on the floor is wood
38. techozinc, =1 if predominant material on the roof is metal foil or zink
39. techoentrepiso, "=1 if predominant material on the roof is fiber cement, mezzanine "
40. techocane, =1 if predominant material on the roof is natural fibers
41. techootro, =1 if predominant material on the roof is other
42. cielorazo, =1 if the house has ceiling
 43. abastaguadentro, =1 if water provision inside the dwelling 44. abastaguafuera, =1 if water provision outside the dwelling 45. abastaguano, =1 if no water provision
46. public, "=1 electricity from CNFL, ICE, ESPH/JASEC" 47. planpri, =1 electricity from private plant
48. noelec, =1 no electricity in the dwelling
49. coopele, =1 electricity from cooperative
50. sanitario1, =1 no toilet in the dwelling
51. sanitario2, =1 toilet connected to sewer or cesspool 52. sanitario3, =1 toilet connected to septic tank
53. sanitario5, =1 toilet connected to black hole or letrine
54. sanitario6, =1 toilet connected to other system
55. energcocinar1, =1 no main source of energy used for cooking (no kitchen) 56. energcocinar2, =1 main source of energy used for cooking electricity
57. energcocinar3, =1 main source of energy used for cooking gas
58. energcocinar4, =1 main source of energy used for cooking wood charcoal 59. elimbasu1, =1 if rubbish disposal mainly by tanker truck
60. elimbasu2, =1 if rubbish disposal mainly by botan hollow or buried
61. elimbasu3, =1 if rubbish disposal mainly by burning
62. elimbasu4, =1 if rubbish disposal mainly by throwing in an unoccupied space 63. elimbasu5, "=1 if rubbish disposal mainly by throwing in river, creek or sea" 64. elimbasu6, =1 if rubbish disposal mainly other
65. epared1, =1 if walls are bad
66. epared2, =1 if walls are regular
67. epared3, =1 if walls are good
68. etecho1, =1 if roof are bad
69. etecho2, =1 if roof are regular
70. etecho3, =1 if roof are good
71. eviv1, =1 if floor are bad
72. eviv2, =1 if floor are regular
73. eviv3, =1 if floor are good
74. dis, =1 if disable person
75. male, =1 if male
76. female, =1 if female
77. estadocivil1, =1 if less than 10 years old
78. estadocivil2, =1 if free or coupled uunion
79. estadocivil3, =1 if married
80. estadocivil4, =1 if divorced
81. estadocivil5, =1 if separated
82. estadocivil6, =1 if widow/er
83. estadocivil7, =1 if single
84. parentesco1, =1 if household head
85. parentesco2, =1 if spouse/partner

 86. parentesco3, =1 if son/doughter
87. parentesco4, =1 if stepson/doughter
88. parentesco5, =1 if son/doughter in law
89. parentesco6, =1 if grandson/doughter
90. parentesco7, =1 if mother/father
91. parentesco8, =1 if father/mother in law
92. parentesco9, =1 if brother/sister
93. parentesco10, =1 if brother/sister in law
94. parentesco11, =1 if other family member
95. parentesco12, =1 if other non family member
96. idhogar, Household level identifier
97. hogar_nin, Number of children 0 to 19 in household 98. hogar_adul, Number of adults in household
99. hogar_mayor, # of individuals 65+ in the household
100. hogar_total, # of total individuals in the household
101. dependency, Dependency rate, calculated = (number of members of the household
younger than 19 or older than 64)/(number of member of household between 19 and 64) 102. edjefe, years of education of male head of household, based on the interaction of
escolari (years of education), head of household and gender, yes=1 and no=0
103. edjefa, years of education of female head of household, based on the interaction of
escolari (years of education), head of household and gender, yes=1 and no=0
104. meaneduc,average years of education for adults (18+)
105. instlevel1, =1 no level of education
106. instlevel2, =1 incomplete primary
107. instlevel3, =1 complete primary
108. instlevel4, =1 incomplete academic secondary level
109. instlevel5, =1 complete academic secondary level
110. instlevel6, =1 incomplete technical secondary level
111. instlevel7, =1 complete technical secondary level
112. instlevel8, =1 undergraduate and higher education
113. instlevel9, =1 postgraduate higher education
114. bedrooms, number of bedrooms
115. overcrowding, # persons per room
116. tipovivi1, =1 own and fully paid house
117. tipovivi2, "=1 own, paying in installments"
118. tipovivi3, =1 rented
119. tipovivi4, =1 precarious
120. tipovivi5, "=1 other(assigned, borrowed)"
121. computer, =1 if the household has notebook or desktop computer
122. television, =1 if the household has TV
123. mobilephone, =1 if mobile phone
124. qmobilephone, # of mobile phones
125. lugar1, =1 region Central

126. lugar2, =1 region Chorotega
127. lugar3, =1 region PacÃ​fico central
128. lugar4, =1 region Brunca
129. lugar5, =1 region Huetar AtlÃ¡ntica
130. lugar6, =1 region Huetar Norte
131. area1, =1 zona urbana
132. area2, =2 zona rural
133. age= Age in years
134. SQBescolari= escolari squared
135. SQBage, age squared
136. SQBhogar_total, hogar_total squared
137. SQBedjefe, edjefe squared
138. SQBhogar_nin, hogar_nin squared
139. SQBovercrowding, overcrowding squared
140. SQBdependency, dependency squared
141. SQBmeaned, square of the mean years of education of adults (>=18) in the
household
142. agesq= Age squared

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[0a69709d70...](https://github.com/treckstar/yolo-octo-hipster/commit/0a69709d70921e82b825e6ed00a76d4708a24bf4)
#### Saturday 2023-03-18 21:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [kleinesfilmroellchen/spcasm](https://github.com/kleinesfilmroellchen/spcasm)@[c39be0ac56...](https://github.com/kleinesfilmroellchen/spcasm/commit/c39be0ac564074318c00eecfe709261350f84fe1)
#### Saturday 2023-03-18 22:01:45 by kleines Filmröllchen

update a bunch of javascript and wasm shit

i hate my life

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[ef9d0c61a3...](https://github.com/cmss13-devs/cmss13/commit/ef9d0c61a3335d40c9bd9459479e0112903ccc02)
#### Saturday 2023-03-18 22:22:18 by Moonshanks

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
## [XenoAmess/screeps](https://github.com/XenoAmess/screeps)@[ebddeb670a...](https://github.com/XenoAmess/screeps/commit/ebddeb670a265504eac8e46d928f926503877dbe)
#### Saturday 2023-03-18 23:03:06 by Tobias Wilken

End of an epoch, friendly TooAngel NPC died (#712)

It is a sad day in the screeps multiverse. The friendly TooAngel NPC from the neighborhood died.
Since the official release of the game it was spending joy, some action via quests and helped improving defenses, while it was just trying to survive somehow for years.
Rest in peace friendly TooAngel NPC.

Some cleanup as condolences:
- Improve code quality
- Extract pixel generation
- Improve on reservations
- Reenable boost config
- Fix issues on mineral handling
- Split up quests in host and player
- Include attacked creeps in the reputation
- Start with autorespawner

---
## [CLimeburner/Iconic-Affordance-Interactions](https://github.com/CLimeburner/Iconic-Affordance-Interactions)@[a41199e5d2...](https://github.com/CLimeburner/Iconic-Affordance-Interactions/commit/a41199e5d2d8c2d56f88aa2b92337f75c2eb2f77)
#### Saturday 2023-03-18 23:09:27 by CLimeburner

Updated the list of possible interactive interfaces in the BlueSkyBrainstorming file.

I had a conversation with my mother about what she might be interested to see in a theme park, and although she's heard from me as I've worked on the theoretical side of the project, she doesn't seem to have really internalized what it was about, so I got an array of answers, some of which were wholly unhelpful, but also many that were intriguing in the ways they fell slightly outside the sphere of what I've been considering. In particular, among the ideas my mother suggested, she mentioned consuming various IP specific foods (such as from Harry Potter, Lord of the Rings, or Alice in Wonderland), wearing specifically iconic clothing (princess dresses, cultural fashions, etc), and some specific embodied experiences, such as falling down the rabbit hole in Alice in Wonderland. Although these might not be technologically interactive interfaces at first blush, they do all present some sense of acts (eating/drinking/dressing/falling) with sensory feedback that further reinforce immersion in the experience. I'm including them in my list because I think it provokes some interesting lines of thought for where one draws the line on what is "interactive".

For instance, we might not think putting on a shirt is interactive, but is getting kitted out in armour by a squire at a renaissance fair interactive? Is an Iron-Man helmet with automated moveable visor interactive? Does piloting a mech count as wearing it? Similarly, eating and drinking might not be "interactive" in an of themselves, per se, but bars such as Disney's Trader Sam's Enchanted Tiki Bar have special effects that trigger in the bar when you order specific drinks, which certainly feels interactive, and 4e Mur here in Montreal is a bar where you can solve a mystery based on clues that come with ordering specific drinks. In this fashion, it becomes clear that "participatory" activities do have robust design opportunities to be made fully interactive, and so I want to put some more thought into this at some point.

---

