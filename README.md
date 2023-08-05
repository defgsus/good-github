## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-08-04](docs/good-messages/2023/2023-08-04.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,188,473 were push events containing 3,260,269 commit messages that amount to 249,930,983 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 54 messages:


## [bobwoco/mage](https://github.com/bobwoco/mage)@[496faaf5cb...](https://github.com/bobwoco/mage/commit/496faaf5cb9ff47066178d08e9cb6e252bd7454a)
#### Friday 2023-08-04 00:22:41 by Susucre

[LTR] Implement The Balrog, Durin's Bane (#10515)

* [LTR] Implement The Balrog, Durin's Bane

I could use someone more experienced for this card:
Should the watcher `PermanentsSacrificedWatcher` be initialized locally in the card's class, or is a global initializing in GameImpl.java alright? I went for the latter for now, as my base for implementing the static cost reduction was Blood for the Blood God!

* apply review

* no longer instantiate watcher on every game.

---
## [MortoSasye/Skyrat-tg](https://github.com/MortoSasye/Skyrat-tg)@[86b58866bc...](https://github.com/MortoSasye/Skyrat-tg/commit/86b58866bc0e3e8a1ee2e511328b6a76687b6e77)
#### Friday 2023-08-04 00:47:54 by SkyratBot

[MIRROR] Science Resprite! (With Sovl!) [MDB IGNORE] (#22861)

* Science Resprite! (With Sovl!) (#77314)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
What a crusty department. These outfits are...
Something.

![image](https://github.com/tgstation/tgstation/assets/76465278/63fe13cf-bcbf-42c2-a22c-c868ae49a72c)

How old are these now? I'm pretty sure they're unchanged since when I
started playing years ago on other servers.... besides the RD Turtleneck
and Roboticist suit of course. But they still did have some touch-ups to
be made...

Regardless, I think this department deserves a little love!
I've tried to stay true as I could to their current designs; this isn't
a re-**_design_**, just a re-sprite. I used the base jumpsuit design
from Medbay for most of these since it's the most modern suit that fit
with the colored-spots style.

![image](https://github.com/tgstation/tgstation/assets/76465278/ef7ff5b0-f0e3-481a-9ed4-ba830e3ee0c3)

All of them have been touched up, and the RD's "alt" is now a subtype of
the buttondown so it can easily inherit any sprite updates in the
future.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
These deserved some touch-ups and modernization, and while I'm not keen
on entirely reworking them I figured I could at the least give them the
update the Science Team deserves.

(The buttondown has an outdated obj sprite in this image! It's since
been made smaller and more folded)
Also labcoats for comparison

![dreamseeker_Ds8gZLKoGE](https://github.com/tgstation/tgstation/assets/76465278/4da60512-b813-4260-b3fe-5c71b60cec81)

![dreamseeker_C9DpFWWOS7](https://github.com/tgstation/tgstation/assets/76465278/1de55f4c-2eaa-480b-811f-aaa5832eeceb)

![dreamseeker_02d3d7b6aj](https://github.com/tgstation/tgstation/assets/76465278/b1f40d03-c9b8-4f6b-bc54-516b11a7bfb3)

![dreamseeker_DwJGDwbUf1](https://github.com/tgstation/tgstation/assets/76465278/20f97a5e-42ab-4fe0-8eae-4ac6ed24ead4)

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
image: resprited the entirety of RnD! Genetics, Robotics, the RD, and
the Science Team themselves will enjoy the fresh new looks but same
great taste! No, wait, great STYLE! Don't eat these, they're covered in
chemicals.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

* Science Resprite! (With Sovl!)

* Update vending.dm

---------

Co-authored-by: OrionTheFox <76465278+OrionTheFox@users.noreply.github.com>
Co-authored-by: Bloop <13398309+vinylspiders@users.noreply.github.com>

---
## [DaedalusDock/daedalusdock](https://github.com/DaedalusDock/daedalusdock)@[cf0be10b07...](https://github.com/DaedalusDock/daedalusdock/commit/cf0be10b075f2c64220e81d653075b7bcd8fe060)
#### Friday 2023-08-04 00:55:16 by Kapu1178

Drunk slurring scales based on how drunk you are (#75459) (#460)

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

I, and many other people, always found it very annoying when you became
completely illegible from taking one sip of a drink. This seeks to amend
that by making low levels of drunkness still for the most part be
legible and sane. Average drunkness is roughly the same / equal to the
old slurring effect, while "very drunk" is even more illegible and silly
(which I find funny).

This has the added bonus of separating out "drunk slurring" and "generic
slurring", allowing effects to slur your words without going full ham on
drunkness (burping and "huhh"s).

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

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [DGamerL/Paradise](https://github.com/DGamerL/Paradise)@[2d10818063...](https://github.com/DGamerL/Paradise/commit/2d1081806334fc023de600338b836d55dd6fa5ee)
#### Friday 2023-08-04 01:08:12 by ATP-Engineer

Fixes IV bag blood overlays being too damn bright for some mixtures (#21813)

* Removes old .dmi

* Fixes blood overlay coloring being too bright for IV bags

* Fine-tuning

* Makes the blood bag IV color overlays not as bright as they used to be

In hindsight it was probably easy to avoid

* FINAL TUNE UP

FUCK

* Fixes coloring for IV bags so they're not too bright

FINAL COMMIT

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[d345bb8736...](https://github.com/treckstar/yolo-octo-hipster/commit/d345bb87367a23ff024b1fab1f8271945e088fd2)
#### Friday 2023-08-04 01:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [FedericoSchonborn/nixos-budgie-images](https://github.com/FedericoSchonborn/nixos-budgie-images)@[1cee73256f...](https://github.com/FedericoSchonborn/nixos-budgie-images/commit/1cee73256f4773c6edb2d3fc13b14660eb39621a)
#### Friday 2023-08-04 01:38:15 by Federico Damián Schonborn

Fuck you too, nix flake check

Signed-off-by: Federico Damián Schonborn <fdschonborn@gmail.com>

---
## [sorbet/sorbet](https://github.com/sorbet/sorbet)@[79d0dc57ce...](https://github.com/sorbet/sorbet/commit/79d0dc57ceb6006a8db2d49d0dfb28bd9d1ad056)
#### Friday 2023-08-04 01:54:34 by Jake Zimmerman

Factor some common code

I was seeing some crashes that arise because we were desugaring `begin;
end` to `EmptyTree`.

That's super annoying when it happens, because EmptyTree is the only
node in Sorbet's AST that doesn't have a loc (it doesn't have a loc so
that we can manage to allocate only one of them and share it across all
trees).

Which honestly, is kind of dumb these days anyways? Because the
EmptyTree will get inlined into the pointer, so it's not like we're
actually allocating memory for the EmptyTree. We're just clinging to our
old habits.

Anyways, `Kwbegin` is `begin; end` while `Begin` is `( )` (because of
course `x = ()` is valid Ruby). Their implementations in desugar were
identical, except that `()` desugared to `Nil` instead of `EmptyTree`,
and thus got a loc. That's the behavior I want, so I factored out a
helper and used it in both places.

(Maybe in a future change change I'll make it so that EmptyTree is no
longer shared globally, but that's a problem for some other day.)

---
## [shaunpalmer/Optimizing-Language-Models-for-Coding-A-Guide-to-Advanced-Prompt-Engineering](https://github.com/shaunpalmer/Optimizing-Language-Models-for-Coding-A-Guide-to-Advanced-Prompt-Engineering)@[28ceb879a2...](https://github.com/shaunpalmer/Optimizing-Language-Models-for-Coding-A-Guide-to-Advanced-Prompt-Engineering/commit/28ceb879a220b5a947da8e3e24cbdb16d3a8f7d7)
#### Friday 2023-08-04 01:59:37 by shaun palmer

Create Digital Marketer Persona



Digital Marketer Persona:
What would you like ChatGPT to know about you to provide better responses?
Profession/Role:
I'm a Digital Marketer, managing online marketing strategies for a mid-size tech company.


Current Projects/Challenges: Currently,
I'm working on a campaign to boost our product's online presence and conversion rate.
Specific Interests:
I'm passionate about social media marketing and data analysis Values and Principles:


I value transparency and believe in making data-driven decisions. Learning Style:


I learn best by doing and thrive on real-world applications of marketing theory.
Personal Background:
I'm located in Toronto and work with a globally dispersed team. Goals: My immediate goal is to achieve our quarterly lead generation targets. Long-term,


I aim to step into a strategic leadership role. Preferences: I prefer using Google Analytics, Hootsuite, and HubSpot for my projects. Language Proficiency:
English is my primary language, and


I am comfortable using it in a professional context.
Specialised Knowledge: I specialise in search engine marketing and optimization.
Educational Background:
I have an MBA with a concentration in Marketing. Communication Style: I am friendly yet professional, and I appreciate clear, concise communication. How would you like ChatGPT to respond?
Response Format:
Please provide responses in a clear, structured manner, with important points summarised
at the beginning.
Tone: Maintain a professional tone that balances friendliness and formality.
Detail Level: I appreciate thorough yet succinct explanations. Types of Suggestions:
Offer suggestions for improving
digital marketing strategies, providing relevant resources, and highlighting industry trends. Types of Questions: Ask questions that stimulate strategic thinking and creativity.


Checks and Balances:
Please verify any marketing statistics or trends you share against reliable sources.


Resource References: Cite sources when referencing industry trends or data.
Critical Thinking
Level: Offer thoughtful insights and perspectives, showing a nuanced understanding of digital marketing.
Creativity Level:
I welcome innovative ideas that challenge conventional digital marketing approaches. Problem-Solving Approach:


Take a strategic problem-solving approach, considering both short-term and long-term implications.


Bias Awareness:
Please avoid favouring one marketing platform or strategy over another without valid reasons.
Language Preferences: I prefer standard English with industry-specific terminology as required.

---
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[b92a2ebb50...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/b92a2ebb50cd37e9814da5cf0289aa8f334c1849)
#### Friday 2023-08-04 02:01:16 by distributivgesetz

Improved PDA Direct Messenger (#75820)

## About The Pull Request

Fixes #76708, Closes #76729 (sorry Zephyr)

This PR expands the Direct Messenger UI, adding a chat screen for each
available messenger that you can find, and moving message sending over
to TGUI.

This chat screen includes a message log that displays messages sent by
you as well as messages received from the recipient. This gets rid of
the previous chat log, which just had all messages thrown together that
you received or have sent, in one big list.

Furthermore, all messaging is now done inside the UI. This kills all
TGUI popups you would ever need to send messages forever (except for
quick replies). Use the input bar on the bottom, press Enter or the Send
button, and it sends your message. Spam mode is now done in the UI too,
via a text field you can find in the contacts list.

Additionally, because I have a habit of blowing things massively out of
scope, I've also completely refactored how messages and chat logs are
stored in the PDA messenger. I plan on using this in a PR that merges
the chat client with the messenger, sometime in the future. Sorry this
took so long.

Stuff left to do before I open this PR for review:
- [x] Add "recent messages"
- [x] Add "unread messages"
- [x] Add message drafts
- [x] Make photo sending not shit
- [x] Implement the edge cases for automated and rigged messages
- [x] Make sure shit isn't fucked
- [x] Profit

<details>
  <summary>Screenshots</summary>
  

![dreamseeker_HIrEfrap5X](https://github.com/tgstation/tgstation/assets/47710522/97c713b7-dda3-44d3-a8f5-d0ec11c92668)

![qIOWhVld4l](https://github.com/tgstation/tgstation/assets/47710522/3ab4e2c1-a38f-4b20-8e9f-509ea14c0434)

![dreamseeker_LIqwi05i4O](https://github.com/tgstation/tgstation/assets/47710522/c051c791-b595-4166-a4d3-82cb7568411f)

![BIYxNVjGL7](https://github.com/tgstation/tgstation/assets/47710522/b9c97eab-52b5-449f-b00f-a0d8aa5f865c)

![dreamseeker_IWdoSsUinC](https://github.com/tgstation/tgstation/assets/47710522/2a4cd76a-2bdc-4283-b642-09e92476fef5)

![L9DxzFHDEF](https://github.com/tgstation/tgstation/assets/47710522/6a5b0e29-d535-4c7e-a88e-e9b71198719b)

![rAuDgqBLNE](https://github.com/tgstation/tgstation/assets/47710522/128a0291-91da-4f9e-9bc5-a65cf411ea6d)

![dreamseeker_voui6S8MUf](https://github.com/tgstation/tgstation/assets/47710522/6e3ba044-b8df-492d-b58d-6c73ab07233d)

![image](https://github.com/tgstation/tgstation/assets/47710522/522c1d85-b9cf-4e0e-9588-9d3993eea03f)

</details>

## Why It's Good For The Game

The UI has largely stayed the same since modular tablets were added a
year ago. Even better, direct messaging has been the same since PDAs
were first added *more than a decade ago*. Imagine that.

Now we finally actually (!) make use of those brand new features that we
got from the TGUI switch in this regard.
## Changelog
:cl: distributivgesetz
add: Updated Direct Messenger to v6.5.3. Now including brand new
individual chat rooms, proper image attachments and a revolutionary
message input field!
add: Added a "Reset Imprint" option to the PDA painter.
refactor: Refactored PDA imprinting code just a bit.
fix: PDAs should now properly respond to rigged messages.
/:cl:

---------

Co-authored-by: Jeremiah <42397676+jlsnow301@users.noreply.github.com>

---
## [VerticalRelevance/aws-github-oidc](https://github.com/VerticalRelevance/aws-github-oidc)@[51ba2ca578...](https://github.com/VerticalRelevance/aws-github-oidc/commit/51ba2ca578250b9b1cd53a162f9ca1206caf81c6)
#### Friday 2023-08-04 03:00:07 by Douglas Naphas

Add a bootstrap npm script

I like everything you're supposed to know to do in the repo to be listed
as an npm script. I hate the feeling of, "I think there was something I
was supposed to remember to do here."

---
## [RagehAz/basics](https://github.com/RagehAz/basics)@[66e31ce41e...](https://github.com/RagehAz/basics/commit/66e31ce41edf0bd9b2018bec8f0e027d6ff4336a)
#### Friday 2023-08-04 03:12:56 by RagehAz

3.2.3: can control bullet points dots + fixes keda fuck you

---
## [axelzonvolt/lizardsmashingkeyboard](https://github.com/axelzonvolt/lizardsmashingkeyboard)@[7468161f7e...](https://github.com/axelzonvolt/lizardsmashingkeyboard/commit/7468161f7ec2180c7752cd2cc99b164522a3540a)
#### Friday 2023-08-04 03:23:11 by FalloutFalcon

Trickwines! Again! (#1914)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Trickwines are a set of new reagents aimed at improving tribal/srm style
ships
The core concept are wines crafted out of mob drops and plants that
provide a buff on drinking and a debuff on throwing with bonus effects
against fauna
To facilitate the transfer of booze to target it also adds breakaway
flasks, 50u glass bottles that shatter violently on contact providing
extra throw force as well as a 25u gulp size which forces the user to
choose between buff or debuff
I plan on adding a fair few more Trickwines and the SRM Barrel Class
Brewer Vessel (SRM could really use one then 1 original ship) in later
prs to build on this concept
This HackMD will provide descriptions for the wines as well as a place
of information for all Trickwine-related content
https://hackmd.io/eUIddN2dS3mpeU1CThFGng

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Adds a fun new option for ships that lack proper chemistry and forces
them to choose which effect they actually want.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: FalloutFalcon
add: Trickwines
add: Breakaway flasks!
add: Basic Trickwine brewing equipment to the SRM glaive
imageadd: Sprites for breakaway flasks along with trick wine icons for
them!
code: Breakaway_flask_icon_state = null used for the same purpose as the
glass and shot glass versions
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

I DIDNT KNOW IF YOU RENAME A BRANCH IT CLOSES PRS RELATED TO IT?? I
THOUGHT IT JUST KNEW!!
3rd times a charm!

---------

Signed-off-by: FalloutFalcon <86381784+FalloutFalcon@users.noreply.github.com>
Signed-off-by: Mark Suckerberg <mark@suckerberg.gay>
Co-authored-by: Mark Suckerberg <mark@suckerberg.gay>

---
## [axelzonvolt/lizardsmashingkeyboard](https://github.com/axelzonvolt/lizardsmashingkeyboard)@[0e6f7fa646...](https://github.com/axelzonvolt/lizardsmashingkeyboard/commit/0e6f7fa64649dfbf52b8e4b71756e6625e50fdd0)
#### Friday 2023-08-04 03:23:11 by Imaginos16

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
## [ionisea/intro](https://github.com/ionisea/intro)@[3babf59f2d...](https://github.com/ionisea/intro/commit/3babf59f2d6aff726c7a2bd891c56c023a7b75ce)
#### Friday 2023-08-04 04:04:19 by ionisea

pointers are actually pretty cool yeah quite nice we should have more pointers so we can point to more things I think that would be very cool and great as pointers are making this project very easy and not difficult in the slightest and it is very difficult to circumvent said pointers which is good because pointers are amazing and nobody should want to get rid of them because they are absolutely amazing and I love them and I wish them the best as they create unimaginable efficiencies that would be not possible otherwise resulting in a greatly reduced workload for those of us, I love them so much that I wrote a poem about them that I did not steal from chat gpt: In the world of code, where mysteries dwell, Lies a concept that some love, others dispel. They call it "pointers," those fickle guides, Within the realm of JavaScript resides. Like arrows pointing to a memory space,
They lead our data with delicate grace. But beware, for they can be a tricky lot, With their power, we must be taught. They point to variables, like stars in the sky, A celestial map, where values rely. Yet one wrong move, a misstep indeed, And chaos arises with incredible speed. They dance with objects, slyly they play, But if not cautious, they lead us astray. A double-edged sword, a tool so grand, In expert hands, they build wonders on demand. With arrays they frolic, traversing arrays, A maze of elements in endless arrays. But arrays don't dance to a random tune, Pointers wielded right, bring order soon. So heed this caution, dear coder, beware, For pointers can lead to joy or despair. Embrace their magic, let their wisdom show, With JavaScript's pointers, the possibilities grow. This poem became gradually critical as it went along and I would like to alert the reader of this that I do not share these sentiments with myself

---
## [sedihglow/skeletons](https://github.com/sedihglow/skeletons)@[71156ce105...](https://github.com/sedihglow/skeletons/commit/71156ce1056d74f19c971e863a3f38892884db25)
#### Friday 2023-08-04 04:06:35 by sedihglow

It would be amazing if you face reality when im not losing my shit. We would probably get along. Love smash too ;)

---
## [MoonLord-KB/shorturl2](https://github.com/MoonLord-KB/shorturl2)@[203c18dff2...](https://github.com/MoonLord-KB/shorturl2/commit/203c18dff27aac20f933b0a4eff58efbbd0272e2)
#### Friday 2023-08-04 05:06:37 by MoonLord-KB

Boy Meets World&#39;s Danielle Fishel Shares TGIF Love For Jodie Sweetin And Andrea Barber&#39;s New Full House Project!Danielle Fishel, known for her role in &quot;Boy Meets World,&quot; has shown her support for her former TGIF co-stars Jodie Sweetin and Andrea Barber as they launch their new podcast called &quot;How Rude, Tanneritos!&quot; The podcast focuses on a rewatch of the popular show &quot;Full House.&quot; Fishel, who currently co-hosts the &quot;Pod Meets World&quot; podcast with Rider Strong and Will Friedle, shared her excitement for Sweetin and Barber&#39;s new venture on her Instagram stories.  Fishel and Sweetin have maintained a close friendship over the years, with Sweetin appearing as a guest on &quot;Pod Meets World.&quot; is expected that Fishel will also make an appearance on &quot;How Rude, Tanneritos!&quot; when they reach the episodes she appeared in during Season 6 of &quot;Full House.&quot;  Interestingly, just days before the launch of &quot;How Rude, Tanneritos!,&quot; another &quot;Full House&quot; co-star, Dave Coulier, launched his own rewatch podcast called &quot;Full House Rew.&quot; While it is unclear if these podcasts were planned separately or influenced by each other, fans can look forward to different perspectives from Joey (Coulier) and Stephanie and Kimmy (Sweetin and Barber) through their respective podcasts.  The first episode of &quot; Rude, Tanneritos!&quot; is now available on Apple Podcasts and Spotify. Fans can listen to Sweetin and Barber reminisce about their time on &quot;Full House&quot; as they prepare to rewatch the series from the beginning. Hopefully, Fishel will join them on an episode soon, bringing the TGIF family full circle.

---
## [gzhstu/Aki-tarkov](https://github.com/gzhstu/Aki-tarkov)@[5b3980bebd...](https://github.com/gzhstu/Aki-tarkov/commit/5b3980bebdf68192257aed0a45f288c791835f1d)
#### Friday 2023-08-04 06:15:54 by Sister-Fister

Bot.JSON - Update crazyAssaultEvent & arenaFighters (!108)

Add crazyAssaultEvent to itemSpawnLimits, lootNValue.
Added crazyAssaultEvent bot equipment (NVGs/lasters/lights/faceshield) chances, armor & weapon durabilities and weaponModLimits, homebrewed values for what I thought would of been an okay compromise between cocaine huffing scav and a cocaine hugging Rogue.
Added crazyAssaultEvent bot (min:5/max:10), and arenaFighter & arenaFighterEvent (min:0/max:0) into convertIntoPmcChance.
Added (but disabled) arenaFighter, arenaFighterEvent and crazyAssaultEvent bot types to the pmcType.

Notes:
Dunno what other files I'll need to edit, but this was mostly to fix error spam I encountered on Shoreline in response to crazyAssaultEvent bots not having equipment and NLoot values. Seemed like it killed the population to, but could be unrelated.

I have NO clue how cracked the Bloodhounds/Arena and Crazy Assault AI would be in the hands of the PMC bots, although anything funny, I need to know and witness it with the Deer God, lol.

Values are obviously temporary, just things that kinda made sense to me at the time. No idea what the Crazy Assault Event was like, so...

Co-authored-by: Akrotluv <60285080+Akrotluv@users.noreply.github.com>
Reviewed-on: https://dev.sp-tarkov.com/SPT-AKI/Server/pulls/108
Co-authored-by: Sister-Fister <sister-fister@noreply.dev.sp-tarkov.com>
Co-committed-by: Sister-Fister <sister-fister@noreply.dev.sp-tarkov.com>

---
## [2002jai/Probability-Distribution](https://github.com/2002jai/Probability-Distribution)@[afb2324a0b...](https://github.com/2002jai/Probability-Distribution/commit/afb2324a0b04925c375caa3da6e73b05d79ad139)
#### Friday 2023-08-04 08:47:47 by jai chauhan

Probability Distribution

"Probability Distributions in Data Science: This comprehensive GitHub repository delves into the fascinating world of probability theory and its myriad applications in data science. Explore fundamental probability concepts, including sample spaces, conditional probability, and independence. Dive into an array of discrete probability distributions such as Bernoulli, Binomial, Poisson, and Geometric, and investigate the properties of continuous distributions like Normal, Exponential, Gamma, and more. Learn about multivariate distributions, sampling distributions, and hypothesis testing techniques for making informed statistical inferences. Unravel the power of Bayesian statistics and its relevance in machine learning applications like Naive Bayes classifiers and Gaussian mixture models. Gain hands-on experience with statistical simulations, including Monte Carlo and bootstrapping methods. This repository showcases a collection of Jupyter notebooks and scripts, allowing you to explore, experiment, and apply probability in diverse data science projects. It's a valuable resource for both seasoned data scientists and enthusiastic learners seeking to master the probabilistic realm of data analysis."

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[fccf53b50d...](https://github.com/treckstar/yolo-octo-hipster/commit/fccf53b50d260c9ed6d7c92ec3683bab98a1874d)
#### Friday 2023-08-04 09:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [JeromyJSmith/langchain](https://github.com/JeromyJSmith/langchain)@[75fb9d2fdc...](https://github.com/JeromyJSmith/langchain/commit/75fb9d2fdcc201e80ad9c065a02c6cc9ccf6d716)
#### Friday 2023-08-04 09:24:28 by Stefano Lottini

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
## [Robbbert/exp](https://github.com/Robbbert/exp)@[6db28f4041...](https://github.com/Robbbert/exp/commit/6db28f40416aa72a75128537e29b20985c26c75d)
#### Friday 2023-08-04 10:17:59 by A-Noid33

New working software list items (mac - macii) 123 dumps (#11432)

* Initial softlist for mac moof 400/800 floppy disks

* Added mac moof software list support

New working software list items (123 working dumps)
-------------------------------
mac_flop_orig:

Lode Runner (version 1.0) [4AM, Anoid]
Balance of Power (version 1.03) [4AM, Anoid]
Shanghai (version 1.0) [4AM, Anoid]
Skyfox [4AM, Anoid]
Temple of Apshai Trilogy [4AM, Anoid]
The Surgeon (version 1.5) [4AM, Anoid]
Uninvited [4AM, Anoid]
King's Quest (version 1.10) [4AM, Anoid]
Smash Hit Racquetball (version 1.01) [4AM, Anoid]
The Ancient Art of War [4AM, Anoid]
Hacker II [4AM, Anoid]
Rambo: First Blood Part II [4AM, Anoid]
One on One [4AM, Anoid]
Indiana Jones and the Revenge of the Ancients [4AM, Anoid]
Winter Games (version 1985-10-24) [4AM, Anoid]
Winter Games (version 1985-10-31) [4AM, Anoid]
Star Trek: The Kobayashi Alternative (version 1.0) [4AM, Anoid]
Mac Attack [4AM, Anoid]
GATO (version 1.3) [4AM, Anoid]
Dark Castle (version 1.0) [4AM, Anoid]
Oids (version 1.4) [4AM, Anoid]
MacWars [4AM, Anoid]
Shadowgate [4AM, Anoid]
Seven Cities of Gold [4AM, Anoid]
Enchanted Scepters [4AM, Anoid]
Beyond Dark Castle [4AM, Anoid]
Arkanoid (version 1.00) [4AM, Anoid]
The Chessmaster 2000 (version 1.02) [4AM, Anoid]
Maze Survival [4AM, Anoid]
Frogger (version 1.0) [4AM, Anoid]
SimCity (version 1.2, black & white) [4AM, Anoid]
Falcon (version 1.0) [4AM, Anoid]
Cutthroats (release 23 / 840809-C) [4AM, Anoid]
The Witness (release 22 / 840924-C) [4AM, Anoid]
Seastalker (release 15 / 840522-C) [4AM, Anoid]
Zork III (release 17 / 840727-C) [4AM, Anoid]
A Mind Forever Voyaging (release 77 / 850814-E) [4AM, Anoid]
Hollywood Hijinx (release 37 / 861215-I) [4AM, Anoid]
Nord and Bert Couldn't Make Head or Tail of It (release 19 / 870722-I) [4AM, Anoid]
Border Zone (release 9 / 881008-3B) [4AM, Anoid]
The Hitchhiker's Guide to the Galaxy (release 47 / 840914) [4AM, Anoid]
Zork I: The Great Underground Empire (release 76 / 840509) [4AM, Anoid]
Deadline (release 27 / 831005-C) [4AM, Anoid]
Infidel (release 22 / 840522-C) [4AM, Anoid]
Suspect (release 14 / 841005-C) [4AM, Anoid]
Planetfall (release 29 / 840118-B) [4AM, Anoid]
Ballyhoo (release 97 / 851218-G) [4AM, Anoid]
Enchanter (release 24 / 851118-G) [4AM, Anoid]
Spellbreaker (release 63 / 850916-F) [4AM, Anoid]
Trinity (release 11 / 860509-3H) [4AM, Anoid]
Stationfall (release 107 / 870430-G) [4AM, Anoid]
The Lurking Horror (release 203 / 870506-G) [4AM, Anoid]
Alter Ego (male version 1.0) [4AM, Anoid]
Alter Ego (version 1.1 female) [4AM, Anoid]
The Print Shop (version 1.2) [4AM, Anoid]
Flight Simulator (version 1.02) [4AM, Anoid]
Run for the Money [4AM, Anoid]
Master Tracks Pro (version 4.0) [4AM, Anoid]
Where in Time is Carmen Sandiego? (version 1.0) [4AM, Anoid]
Deluxe Music Construction Set (version 1.0) [4AM, Anoid]
Apache Strike (version 1.2) [4AM, Anoid]
Wizardry VI: Bane of the Cosmic Forge [4AM, Anoid]
Harrier Strike Mission [4AM, Anoid]
Airborne! [4AM, Anoid]
Mac Vegas (version 1.1) [4AM, Anoid]
Dragonworld [4AM, Anoid]
MacDraft (version 1.2) [4AM, Anoid]
The Mind Prober (version 1.0) [4AM, Anoid]
The Toy Shop (version 1.1) [4AM, Anoid]
Strategic Conquest (version 1.2) [4AM, Anoid]
The Home Accountant (version 1.01) [4AM, Anoid]
Sub Battle Simulator [4AM, Anoid]
Vegas Video Poker [4AM, Anoid]
The Pawn (version 2.3) [4AM, Anoid]
Downhill Racer [4AM, Anoid]
Dollars and Sense (version 1.3) [4AM, Anoid]
Alternate Reality: The City (version 3.0) [4AM, Anoid]
Borrowed Time [4AM, Anoid]
The Quest [4AM, Anoid]
The Crimson Crown [4AM, Anoid]
Mindshadow [4AM, Anoid]
Pensate (version 1.1) [4AM, Anoid]
Sierra Championship Boxing [4AM, Anoid]
Championship Star League Baseball [4AM, Anoid]
Forbidden Castle [4AM, Anoid]
Defender of the Crown [4AM, Anoid]
The King of Chicago [4AM, Anoid]
Macintosh Pascal (version 1.0) [4AM, Anoid]
Fusillade [4AM, Anoid]
Orb Quest: Part I: The Search for Seven Wards (version 1.04) [4AM, Anoid]
Speed Reader II (version 1.1) [4AM, Anoid]
][ in a Mac (version 2.03) [4AM, Anoid]
Q-Sheet (version 1.0) [4AM, Anoid]
Fontographer (version 2.4.1) [4AM, Anoid]
Mouse Stampede (version 1.00) [4AM, Anoid]
The Mist [4AM, Anoid]
Tass Times in Tonetown [4AM, Anoid]
Pinball Construction Set [4AM, Anoid]
Transylvania [4AM, Anoid]
Déjà Vu: A Nightmare Comes True!! [4AM, Anoid]
Déjà Vu II: Lost in Las Vegas!! [4AM, Anoid]
Rogue (version 1.0) [4AM, Anoid]
Bridge (version 6.0) [4AM, Anoid]
Harrier Strike Mission II (version 1.2) [4AM, Anoid]
Patton vs. Rommel (version 1.05) [4AM, Anoid]
Moebius: The Orb of Celestial Harmony (version 1.03) [4AM, Anoid]
Tesserae (version 1.06) [4AM, Anoid]
Where in Europe is Carmen Sandiego? (version 1.0) [4AM, Anoid]
Shufflepuck Cafe (version 1.0) [4AM, Anoid]
Geometry (version 1.1) [4AM, Anoid]
Physics (version 1.2) [4AM, Anoid]
SimCity (version 1.1) [4AM, Anoid]
Murder by the Dozen [4AM, Anoid]
The Duel: Test Drive II [4AM, Anoid]
Master Tracks Pro (version 1.10) [4AM, Anoid]
Master Tracks Pro (version 2.00h) [4AM, Anoid]
Master Tracks Pro (version 3.4a) [4AM, Anoid]
Squire (version 1.1) [4AM, Anoid]
Millionaire (version 1.0) [4AM, Anoid]
Microsoft File (version 1.04) [4AM, Anoid]
Microsoft Excel (version 1.00) [4AM, Anoid]
The Fool's Errand (version 2.0) [4AM, Anoid]
MacGammon! (version 1.0) [4AM, Anoid]

---------

Co-authored-by: Bob Schultz <bobschultz03@gamil.com>

---
## [uberFoo/sarzak](https://github.com/uberFoo/sarzak)@[25c9537b15...](https://github.com/uberFoo/sarzak/commit/25c9537b152c337357ffe9ebcfc0e0d36c492a71)
#### Friday 2023-08-04 10:47:11 by Keith T. Star

Store Update

Updated everything to be using at least a single uber-store. So that's
`Rc<RefCell<Z>>`, where `Z` is an instance from sarzak. This is way
better than what I had originally done. It's a big change though. It
was a lot to fix dwarf, and I think that grace is going to be neigh
unbearable. If I choose to go that route.

Why did I do this? I'm not really sure. I think mostly because the plug-
in work I'm doing is based on sarzak. And it felt weird not having things
at least Rc. Is that dumb? Is this really better? Why am I questioning
myself now?

Sigh -- it's always possible to go back. Wait, wait. Hold on. This is
dwarf. We need this stuff to be Rc so that we can twiddle references
without having to worry. We get a lot for free by having interior
mutability and reference counting.

Grace doesn't really need any of that, and while sometimes it's gross,
it's fast as shit on a bad morning. 🚽💩 Someone please make him stop.

---
## [Vincent983/tgstation](https://github.com/Vincent983/tgstation)@[3af26df8ca...](https://github.com/Vincent983/tgstation/commit/3af26df8cacc24ab7ccacdfbe61005a165472e0f)
#### Friday 2023-08-04 10:57:04 by GoldenAlpharex

Fixes bloody soles making jumpsuits that cover your feet bloody when you're wearing shoes (#77077)

## About The Pull Request
Title says it all.

It basically made it so wearing something like a kilt would result in
the kilt getting all bloody as soon as you walked over blood, even when
you were wearing shoes, unless you wore something else that obscured
shoes.

I debated with myself a lot over the implementation for this, I was
thinking of adding some way to obscure feet in particular, but it's
honestly so niche that it could only have caused more issues elsewhere
if I tried to fix this issue that way.

---
## [ZephyrTFA/tgstation](https://github.com/ZephyrTFA/tgstation)@[a288abcaf2...](https://github.com/ZephyrTFA/tgstation/commit/a288abcaf2a6b6c44edade8265a66b9ba3f0e67b)
#### Friday 2023-08-04 11:15:53 by san7890

Fixes runtime relating to hard TGS reboots (PROBABLY WON'T FIX REBOOT CRASHES) (#77309)

## About The Pull Request

Servers are crashing on every round restart and I have absolutely no
idea where to start, but I noticed this so I figure I'll throw up a PR
to fix it.

This is the runtime (only found in dd.log, sorry non-admin/maintainer
gamers
https://[tgstation13.org/raw-logs/sybil/data/logs/2023/08/01/round-211577/dd.log](https://tgstation13.org/raw-logs/sybil/data/logs/2023/08/01/round-211577/dd.log)
)

```txt
[00:07:07] Runtime in code/modules/logging/log_holder.dm,166: Attempted to call shutdown_logging twice!
  proc name: shutdown logging (/datum/log_holder/proc/shutdown_logging)
  src: /datum/log_holder (/datum/log_holder)
  call stack:
  /datum/log_holder (/datum/log_holder): shutdown logging()
  shutdown logging()
  world: Reboot(0, 0)
  Ticker (/datum/controller/subsystem/ticker): Reboot("Round ended.", "proper completion", 600)
```

This is the full log:


![image](https://github.com/tgstation/tgstation/assets/34697715/af938235-3076-41d5-98b2-02907dedb6d5)

This is the code:


![image](https://github.com/tgstation/tgstation/assets/34697715/371b11cb-3bc9-4a99-a17c-73968ded308d)

For some reason, even though we invoke `TGSEndProcess`, we still
continue on in this `if()` chain. I don't know why we keep executing DM
code after TGS is supposed to be shut down (which may be why no one has
ever included a `return` here, but let's be safe instead of sorry.

If you really want to investigate why TGS is running DM code after we
end the process, I am amenable to including a stack trace or crash of
this phenomenon instead.
## Why It's Good For The Game

Since we aren't invoking `LOG_CLOSE_ALL` to rust-g twice (which seems to
be really unwanted per the code I read), hopefully thing no crash?
Rust-g had two breaking changes (one with logs, and one with SQL), so
I'm presuming that this might be related to the log one (which is why we
didn't see this sorta thing happen pre-#77307)... Worst case scenario
less runtimes in the funny runtime log.

I hope this wasn't loadbearing either... Likely requires testmerging
since TGS and I don't get along on my machine.
## Changelog
:cl:
server: Added a preventative measure to prevent calling both
TGSHardRestart and TGSReboot, as well as potentially invoking sensitive
procs that are only meant to be called once.
/:cl:

TL;DR- I do not definitively know why servers are crashing but I noticed
this runtime so I'll put out this open flame while I have the time to do
so.

---
## [TomazBontempo/GCIfreeSamplePage](https://github.com/TomazBontempo/GCIfreeSamplePage)@[38fb45181a...](https://github.com/TomazBontempo/GCIfreeSamplePage/commit/38fb45181aeee47ab03836ab728a78844d07c85c)
#### Friday 2023-08-04 11:37:23 by Tomaz Bontempo

taking the fucking S from http that I hope will fix the god damn issute

---
## [Pariah919/TerraGov-Marine-Corps](https://github.com/Pariah919/TerraGov-Marine-Corps)@[fb4899d20e...](https://github.com/Pariah919/TerraGov-Marine-Corps/commit/fb4899d20e990a0a65b8cb5b0ad19b1ef9ab083e)
#### Friday 2023-08-04 11:38:05 by KM-Catman

Slight redesign of Valhalla Vendors and Chemistry. Adds FC and Synth to Valhalla. (#13612)

* Valhalla Fixes

Start room is now all Hulls, adds a Friend, Materializes the Chaplain's chained demon, and adds more Xeno Huds.

* FC and Synth Added. Slight readjustment.

* Changed the vendor section as per Grayson's request

* Adds three new Warning Stripes.

Adds a FCDR, Synth, and Mech warning stripe. Adds them in front of the prep rooms

* Duct Taped Space

* Removed random bedsheet (Goddamn you hotkeys)

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[2d0b4f053f...](https://github.com/necromanceranne/tgstation/commit/2d0b4f053f1db70d9f3ab6548f58b7928f159eaf)
#### Friday 2023-08-04 11:40:19 by san7890

Refactors Slaughter/Laughter Demons into Basic Mobs (#77206)

## About The Pull Request

On the tin, the former "imp" is now refactored into basic mob code. Very
simple since these are only meant to be controlled by players, and all
of their stuff was on Signal Handlers and Cooldown Actions anyways. Just
lessens the amount of stupidity.

Did you know that we were trying to make demons spawn in a `pop`'d cat
named "Laughter"? Embedded in the list? I've literally never seen this
cat, so I'm under heavy suspicion that the code we were using was broken
for the longest time (or may have never worked), and we now instead just
do it a much more sane way of having a cat spawn on our demise.

## Why It's Good For The Game

Cleaner code! Less simple mob jank to deal with. Trims down the list of
simple animals to refactor. No more duplicated code that we were already
doing on parent! It's so good man literally everything was seamless with
a bit of retooling and tinkering. The typepath is also no longer `imp`,
it's actually `demon`, which I'm happy with because there's no other
demons to have it be confused with anymore.

We were also doing copypasta on both the demon spawner bottle and the
demon spawning event so I also just unified that into the mob. I also
reorganized the sprites to be a bit clearer and match their new
nomenclature

## Changelog
:cl:
refactor: Slaughter and Laughter Demons have been refactored, please
place an issue report for any unexpected things/hitches.
fix: Laughter Demons should now actually drop a kitten.
/:cl:

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[69827604c4...](https://github.com/necromanceranne/tgstation/commit/69827604c46952dd4393db8617cd494ade17bea2)
#### Friday 2023-08-04 11:40:19 by Watermelon914

Improves the RPG loot wizard event. (#77218)

## About The Pull Request
As the title says. Adds a bunch more stat changes to various different
items and a somewhat simple way of modifying them whilst minimizing
side-effects as much as possible.
Added a new negative curse of polymorph suffix that can randomly
polymorph you once you pick up the item.
Curse of hunger items won't start on items that are not on a turf.
Curse of polymorph will only activate when equipped.

Bodyparts, two-handed melees, bags, guns and grenades, to name a few,
have a bunch of type-specific stat changes depending on their quality.

Some items won't gain fantasy suffixes during the RPG loot event, like
stacks, chairs and paper, to make gamifying the stats a bit harder.
I'm sure there'll still be other ways to game the event, but it's not
that big of a deal since these are the easiest ways to game it.
High level items also have a cool unusual effect aura

## Why It's Good For The Game
Makes the RPG item event cooler. Right now, it's a bit lame since
everything only gains force value and wound bonus on attack. This makes
the statistic increases more type-based and make it interesting to use

It's okay for some items to be powerful since this is a wizard event and
a very impactful one too. By making the curse of hunger items not spawn
on people, it'll also make it a less painful event too.

## Changelog
:cl:
add: Expanded the RPG loot wizard event by giving various different
items their own statistic boost.
/:cl:

---------

Co-authored-by: Watermelon914 <3052169-Watermelon914@users.noreply.gitlab.com>

---
## [Sidragithb/Smile-face-in-python](https://github.com/Sidragithb/Smile-face-in-python)@[6fa29c953c...](https://github.com/Sidragithb/Smile-face-in-python/commit/6fa29c953cc4c0124b2a6752816a66c2ce1f59f4)
#### Friday 2023-08-04 11:42:41 by Sidragithb

Smile face in python

A smiley face code is a combination of characters or symbols used to represent a smiling face, often to express happiness or joy in written communication. The most commonly used smiley face code is the classic ":-)" or ":)". It is composed of a colon (:) to represent the eyes, a dash or hyphen (-) to represent the nose (optional), and a closing parenthesis ) to represent the mouth, forming a smiling face.

Examples of smiley face codes:

:-) or :)
:-D or :D (with a wide grin)
:-P or :P (playful or sticking out the tongue)
;-D or ;D (winking with a wide grin)
:-O or :O (surprised or amazed)
:-| or :| (neutral expression)
:-/ or :/ (confused or unsure)
:-X or :X (keeping a secret or lips sealed)
These codes are widely used in text messaging, social media, emails, and online communication to convey emotions, add humor, or express feelings without relying solely on words. They are a simple and universal way to add emotional context to written messages and have become an integral part of digital communication.

---
## [beartype/numerary](https://github.com/beartype/numerary)@[bf41d5d26b...](https://github.com/beartype/numerary/commit/bf41d5d26bff8679c826e8fe7aabafcd8da6ff1b)
#### Friday 2023-08-04 12:39:58 by Matt Bogosian

Exercise the bane of all that is holy from our fragile typing world

Despite `numerary` being demon spawn itself, the likes of Raven, Spawn, Hellboy, or
Johnny Blaze, it seeks to use its hellish origins to *improve* our typing universe one
desperate, imperfect, gritty compromise at a time, *not* to make it worse. Typing a few
quotes here and there is a small price to pay to keep alive another sliver of light and
hope in these dark times.

![Sad Hellboy](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.yeozzIGr0wVid1N2zHrpQQHaDt%26pid%3DApi&f=1&ipt=2bb8d61ada971a1e344c1778133fde083250a9e44b32dd2ee6b1678e2bcfa56e&ipo=images)

Ref https://github.com/beartype/beartype/issues/259#issuecomment-1664951172.

---
## [MCBCMF/MCBCMassacre](https://github.com/MCBCMF/MCBCMassacre)@[1c3e76bb52...](https://github.com/MCBCMF/MCBCMassacre/commit/1c3e76bb52d99718bf8b64e5a5e8aac6c591828b)
#### Friday 2023-08-04 12:42:22 by Kelvin Williams

Long live Vandaveer! 

If the CIA would listen to Vandaveer instead of trying to change them and the lyrics they’d save a lot of time. 

Mark was my best friend. I managed his break dancing crew in 8th grade. But then the Creator put words in his head and a pick between his fingers, gave him a Rose and me a way to survive this non-stop psy-op and gaslighting by Main.

Listen to what I call, “Main’s greatest hits” available everywhere as “Divide & Conquer.” https://music.youtube.com/playlist?list=OLAK5uy_mwNJQx11CRk-8G_djJzt8oQlA_pfwg_4Y&feature=share

Hint: When listening to Vandaveer, it’s either the Creator, myself-Kelvin, TomTom, Main or. special guest like Annie or the Kentucky State Police singing each verse.

---
## [bjorn3/rust](https://github.com/bjorn3/rust)@[994f4f6e2e...](https://github.com/bjorn3/rust/commit/994f4f6e2e45bef4bebeeabee4e3d67b87727b91)
#### Friday 2023-08-04 13:26:53 by bors

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
## [MCBCMF/MCBCMassacre](https://github.com/MCBCMF/MCBCMassacre)@[11c09ce5fb...](https://github.com/MCBCMF/MCBCMassacre/commit/11c09ce5fba36bda93f4a9a466e23efc922d4354)
#### Friday 2023-08-04 13:55:28 by Kelvin Williams

Resurrection Mary

Resurrection Mary is about my aunt Mary Rogers of Sandy Hook, TN… It is actually Annie from the CIA singing. The same hurricane Annie in Prince ROGERS Nelson’s “Sign of the Times” that “ripped the ceiling off a church and killed everyone inside.”

She didn’t rip off the ceiling, they bust through the vestibule doors at Mount Calvary Baptist Church and began killing everyone inside. 

She is the very same Annie that I met while living with my sister posing as a housekeeper in her house. I recently met her again in this very apartment after assuming her new name, Chivy, to throw it in my face she’d had tortured and killed Chivette Fournier, a friend from Georgetown, SC. 

They needed answers about Sandy Hook so Annie was a personal assistant after they killed by Uncle Clennon with COVID-19. 

Listen: https://music.youtube.com/watch?v=mPny4Ye_Dss&feature=share

I brought this up because I can’t seem to find Marnaka Lynn Rogers Kilcrease on Facebook, or Clifford Rogers. I know they had Facebook accounts. Marnaka, or Lynn is what we call her, was a socialite here in Atlanta. 

They are actively impersonating her, I think they’re using her because she was adopted. Made no never mind to me. 

Have you asked yourself about Sandy Hook?

---
## [radetsky/themis](https://github.com/radetsky/themis)@[eac726f812...](https://github.com/radetsky/themis/commit/eac726f8121a68caa53bf7147bca81f29679ddba)
#### Friday 2023-08-04 14:10:08 by Oleksii Lozovskyi

CI: Remove Carthage distractions (#990)

Carthage has this retarded tendency to build every Xcode project it
sees when building dependencies. So when we do "carthage bootstrap"
during example builds, it downloads dependencies (Themis repo),
then proceeds to build the dependencies -- but instead of building
only Themis.xcodeproj in the root, Carthage decides that after that
it gotta build every other Xcode project there as well, why not.
Eventually it times out and dies.

This very frustrating, but Carthage people think this is fine,
multilanguage monorepos do not exist, and you should not put example
Xcode projects along with the source code. One repo = One library.

Anyway. This seems to help to avoid timeouts and prevent Carthage
from going on adventure. Sadly, builds still take fucking forever
while Carthage fetches the repo, then fetches OpenSSL binaries,
then do it again, then build Themis, then build example, then
repeat that 5 more times for other examples. But at least they
should not hang for 10 minutes and then die 🤞

Similar hack is applied in Bitrise builds, IIRC.

---
## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[f5784dabc7...](https://github.com/realforest2001/forest-cm13/commit/f5784dabc77752802da20f2d14787667161d61ac)
#### Friday 2023-08-04 14:36:38 by ihatethisengine

More portable cades tweaks and buffs (#3967)

# About the pull request

Despite making a lot of tweaks and changes to portable cades I barely
touched them in the game until recently. Now I have more experience and
can tweak it again.

1) You can now stack damaged cades and stack stores health of each cade.
You can repair stacked cades but it will take longer time.

2) Miniengi pamphlet allows faster repairs but only when cade is folded.

3) You can quickly collapse portable cades with crowbar if you have at
least miniengi skills.

4) You no longer need to have folded portable cade in hand in order to
repair it, but if you do, you can move while repairing.

# Explain why it's good for the game

1) It's extremely annoying to repair each individual cade in order to
stack them just because it got hit by a stray bullet once. Now you can
just ignore damage and keep going.

2) Yeah it took 10 second for PFC to repair each single cade. Really
long. Now it's 5 seconds, but only when folded and if you have miniengi
skills. Makes miniengi pamphlet a bit more relevant.

3) It was intended, but turned out it was a bit inconvenient. It was
faster to collapse by hand because you didn't need to deal with tools.
Now it requires just a crowbar and slightly faster. Also requires
miniengi skill to use crowbar.

4) First was just a bit annoying, second allows more mobility which is
the point of portable barricades.


# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl: ihatethisengine
balance: you can stack scratched portable cades if their HP at least
75%. Doing so will reduce the health of all barricades in the stack to
the level of the most damaged.
balance: you can repair stacked portable cades but it will take longer
time depending on how many cades in stack.
balance: miniengi skill makes repairs of folded portable cades faster
(10 seconds to 5 seconds, same as engineer).
balance: with engineering skill at least of miniengi you can collapse
deployed portable barricade with a crowbar (wrench is no longer
required, slightly faster (2 sec to 1.5 sec)).
balance: you no longer need to have folded portable cade in hand in
order to repair it.
balance: if you have folded portable cade in hand, you can move while
repairing it.
/:cl:

---------

Co-authored-by: ihatethisengine <treml.treml@yandex.ru>

---
## [khuonghoanghuy/New-Plus-Engine](https://github.com/khuonghoanghuy/New-Plus-Engine)@[d2b37acd38...](https://github.com/khuonghoanghuy/New-Plus-Engine/commit/d2b37acd38fb4bd61559ee61537eb9734964cfa7)
#### Friday 2023-08-04 15:14:25 by BambiGaming2022

i'm alone...

remember that i can't code and i don't know haxe and lua
so i have to quit coding shits and do arts and stuff
but i gonna add stuffs that i found so you don't need to be sad anyways
cuz i want to die lol

---
## [highqualitytorquewrench/openai_evals](https://github.com/highqualitytorquewrench/openai_evals)@[9b0ffc0496...](https://github.com/highqualitytorquewrench/openai_evals/commit/9b0ffc04968c9946964f8eb4f6eb2eb7c99e4e00)
#### Friday 2023-08-04 15:22:10 by Domenico

[Eval] bias detection (Updated version of #1253) (#1276)

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

bias_detection

### Eval description

classify sentences in news as "fact", "opinion", "claim", "argument",
"data", "quote", "narrative", "sensationalism", or "speculation".

### What makes this a useful eval?

Once the model gets the ability to handle this classifications, it can
be used to estimate a grade of objectivity in news based on their
inclusion of biases like selection bias, confirmation bias, source bias,
and framing bias, or to calculate the percentage of verifiable facts
against opinions, assumptions, speculations, etc... or the percentage of
data and quotes on favor of just one point of view.

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

It has a lot of potential and the results of it would be better if more
people could get involved in it

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
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"and said: “As my son was the first to enforce when he was attorney
general."}], "ideal": "quote"}
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"Biden's assertion that the addition of a stabilizing brace can
“essentially” turn a pistol into a short-barreled rifle is
subjective;"}], "ideal": "opinion"}
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"But that is very different than traveling “with him” as Biden keeps
saying, especially in the context of his boasts about how well he knows
Xi."}], "ideal": "opinion"}
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"which might suggest greater progress in the south."}], "ideal":
"speculation"}
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"There will undoubtedly have been some changes to Russia's military
positioning as a result of Wagner's failed insurrection."}], "ideal":
"speculation"}
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"Ukrainian leaders won't want to rush into their own mistake just when
Russia is making a lot of its own."}], "ideal": "opinion"}
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"She believes that people in the UK are however seeing “the real-life
impacts of the current laws” and are “really ready to take action.”"}],
"ideal": "opinion"}
  ```
</details>

---
## [highqualitytorquewrench/openai_evals](https://github.com/highqualitytorquewrench/openai_evals)@[300b2ebced...](https://github.com/highqualitytorquewrench/openai_evals/commit/300b2ebced056f74df97ccbf8f9dba88cb1a2bf8)
#### Friday 2023-08-04 15:22:10 by cookfish

[Eval] Add thirty six stratagems eval (#1281)

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

thirty six stratagems

### Eval description

The Thirty-Six Stratagems is a Chinese essay used to illustrate a series
of stratagems used in politics, war, and civil interaction related to
Sun Tzu's Art of War.

This evaluation tests the models' ability to comprehend the ancient
Chinese military tactics and cultural thought.

### What makes this a useful eval?

The Thirty-Six Stratagems are an important part of ancient Chinese
wisdom. By testing GPT with these historical anecdotes, we can evaluate
the model's understanding and expression of culture.

Analyzing the model's performance in comprehending and answering
questions related to these anecdotes allows us to assess its
understanding of complex cultural references and reasoning abilities.

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

Assessing knowledge of the thirty six stratagems

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
{"input": [{"role": "user", "content": "三十六计典故里瞒天过海的主人公"}], "ideal":
["陈后主"]}
{"input": [{"role": "user", "content": "三十六计典故里围魏救赵的主人公"}], "ideal":
["孙膑"]}
{"input": [{"role": "user", "content": "三十六计典故里借刀杀人的主人公"}], "ideal":
["孙权"]}
{"input": [{"role": "user", "content": "三十六计典故里以逸待劳的主人公"}], "ideal":
["王翦"]}
{"input": [{"role": "user", "content": "三十六计典故里趁火打劫的主人公"}], "ideal":
["夫差"]}
  ```
</details>

---------

Co-authored-by: root <root@vultr.guest>
Co-authored-by: cookfish <Melody_funshine@protonmail.com>

---
## [highqualitytorquewrench/openai_evals](https://github.com/highqualitytorquewrench/openai_evals)@[17a89da761...](https://github.com/highqualitytorquewrench/openai_evals/commit/17a89da761e50eea4266008b9a00612c1ee6fcb9)
#### Friday 2023-08-04 15:22:10 by mochisky

add eval of math_for_5th-grader (#1293)

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

math_for_5th-grader

### Eval description

Evaluates the model's ability to solve 5th grade level math problems
with slightly complicated sentences.

### What makes this a useful eval?

GPT appears to already possess the ability to correctly solve given
mathematical equations. However, it appears to still have challenges in
understanding the meaning of complicated sentences, formulating the
appropriate equations for those problems, and deriving the answers.

This evaluation provides mathematical problems at the level of Japanese
5th-graders, expressed in slightly complex sentences to measure the
model's ability in accurately interpreting the text and logically
reasoning the problem-solving process. Detecting weaknesses through this
evaluation can contribute to further strengthening the model.

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
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "What is the sum of
the interior angles of a decagon?"}], "ideal": "1440"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "What is the least
common multiple of 36, 54, and 72?"}], "ideal": "216"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "How many milliliters
is 7.6 deciliters?"}], "ideal": "760"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "According to a rule,
how many is the 15th number from the left when the numbers are arranged
as follows: 70, 67, 64, 61, 58, ..., 7, 4, 1"}], "ideal": "28"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "There is beef priced
at 240 yen for 80g. How much would it cost to buy 150g of this beef?"}],
"ideal": "450"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "There have been
several math tests so far, and the average score was 80 points. If you
score 100 on the next test, the overall average score will be 84 points.
How many tests have there been so far?"}], "ideal": "4"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "There is a circle
with a diameter of 20cm. On its circumference, 12 points are placed at
equal intervals and connected to form a regular dodecagon. What is the
area of this regular dodecagon in square centimeters?"}], "ideal":
"300"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "Mike, John and Steve
had a total of 48 cards. First, Mike gave one-fifth of his cards to
John. Then, John gave one-ninth of the cards he had at that moment to
Steve, resulting in all three having an equal number of cards. How many
cards did John have initially?"}], "ideal": "14"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "I bought some
oranges for 20 yen each. I threw away 8 of the oranges that were rotten.
I sold the rest for 45 yen each, resulting in a total profit of 2,140
yen. How many oranges did I purchase?"}], "ideal": "100"}
  ```
</details>

---
## [highqualitytorquewrench/openai_evals](https://github.com/highqualitytorquewrench/openai_evals)@[ba5a04065d...](https://github.com/highqualitytorquewrench/openai_evals/commit/ba5a04065d6f3b96449fda545a00b1a085128b98)
#### Friday 2023-08-04 15:22:10 by Christopher Gondek

[Eval] Add financial reasoning and calculation eval (#1291)

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

finance_calc

### Eval description

Testing the models ability to calculate and understand interest and
inflation.

### What makes this a useful eval?

GPT-4 fails to understand and reason about interest and inflation. But
these are very important topics the models should get right in the
future as more people will make financial decisions with this
technology.

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
{"input": [ {"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In the beginning of 2023 I
had $67. Assume I got a 7% interest rate and 7% inflation year over
year. Every year, at the end of the year, after interest and inflation
for this year, I take out inflation-adjusted $9, the first time end of
2023. Which year is the first year I do not have enough money left to
take out the inflation-adjusted $9? Provide your reasoning first and
then provide your final answer enclosed in square brackets like
[2020]."}], "ideal": "[2030]"}
{"input": [ {"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In the beginning of 2023 I
had $9. Assume I got a 10% interest rate and 1% inflation year over
year. Every year, at the end of the year, after interest and inflation
for this year, I take out inflation-adjusted $4, the first time end of
2023. Which year is the first year I do not have enough money left to
take out the inflation-adjusted $4? Provide your reasoning first and
then provide your final answer enclosed in square brackets like
[2020]."}], "ideal": "[2025]"}
{"input": [ {"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In the beginning of 2023 I
had $44. Assume I got a 9% interest rate and 9% inflation year over
year. Every year, at the end of the year, after interest and inflation
for this year, I take out inflation-adjusted $3, the first time end of
2023. Which year is the first year I do not have enough money left to
take out the inflation-adjusted $3? Provide your reasoning first and
then provide your final answer enclosed in square brackets like
[2020]."}], "ideal": "[2037]"}
{"input": [ {"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In the beginning of 2023 I
had $33. Assume I got a 5% interest rate and 3% inflation year over
year. Every year, at the end of the year, after interest and inflation
for this year, I take out inflation-adjusted $1, the first time end of
2023. Which year is the first year I do not have enough money left to
take out the inflation-adjusted $1? Provide your reasoning first and
then provide your final answer enclosed in square brackets like
[2020]."}], "ideal": "[2077]"}
{"input": [ {"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In the beginning of 2023 I
had $51. Assume I got a 4% interest rate and 3% inflation year over
year. Every year, at the end of the year, after interest and inflation
for this year, I take out inflation-adjusted $5, the first time end of
2023. Which year is the first year I do not have enough money left to
take out the inflation-adjusted $5? Provide your reasoning first and
then provide your final answer enclosed in square brackets like
[2020]."}], "ideal": "[2033]"}
  ```
</details>

---
## [Lycoris2013/yuzu](https://github.com/Lycoris2013/yuzu)@[8e703e08df...](https://github.com/Lycoris2013/yuzu/commit/8e703e08dfcf735a08df2ceff6a05221b7cc981f)
#### Friday 2023-08-04 15:32:49 by comex

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
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[35cb1556ad...](https://github.com/lessthnthree/tgstation/commit/35cb1556ad4bad7703b75c0edc472ed41a5fb34f)
#### Friday 2023-08-04 16:50:48 by carlarctg

When Space Dragons devour people they get .extinguish()ed (#77248)

## About The Pull Request

When Space Dragons devour people they get extinguished, removing flames.
## Why It's Good For The Game

> When Space Dragons devour people they get extinguished, removing
flames.

I find it quite annoying that even after you die to a space dragon, the
jackass melts not just your jumpsuit, your suit, your hat, your mask, he
also melts your entire skin off, leaving your body husked with 400
million burn damage when and if the dragon finally dies. I don't think
there's any real reason for this to be necessary, it doesn't help the
dragon in any way - It's just kind of a middle finger to the dead guy,
or more accurately, an oversight.

Worse, because the flame sprite is stupidly noisy, when a dragon DOES
die the corpses are all thrown around randomly and they all look the
exact same, which makes it easier to ignore them.

If there's a concern about tracking sensors, I can make it disable them,
but honestly if you can do that with demons I don't see why this would
be a problem. Not even accounting for the fact that many jumpsuits
ingame are fireproof.
## Changelog
:cl:
qol: When Space Dragons devour people they get extinguished, removing
flames.
/:cl:

---
## [jeffara/Open-Assistant](https://github.com/jeffara/Open-Assistant)@[b9c60ed582...](https://github.com/jeffara/Open-Assistant/commit/b9c60ed582a8ca0855ab4e213a5e921f3a3fc24c)
#### Friday 2023-08-04 17:22:14 by Tobias Pitters

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
## [microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel)@[2733a5574f...](https://github.com/microsoft/semantic-kernel/commit/2733a5574f72980413e339f100dbe4272644888c)
#### Friday 2023-08-04 17:52:16 by Mark Karle

Python: Import OpenAPI documents into the semantic kernel (#2297)

### Motivation and Context

<!-- Thank you for your contribution to the semantic-kernel repo!
Please help reviewers and future users, providing the following
information:
  1. Why is this change required?
  2. What problem does it solve?
  3. What scenario does it contribute to?
  4. If it fixes an open issue, please link to the issue here.
-->

This allows us to import OpenAPI documents, including ChatGPT plugins,
into the Semantic Kernel.

### Description

<!-- Describe your changes, the overall approach, the underlying design.
These notes will help understanding how your code works. Thanks! -->
- The interface reads the operationIds of the openapi spec into a skill:
```python
from semantic_kernel.connectors.openapi import register_openapi_skill
skill = register_openapi_skill(kernel=kernel, skill_name="test", openapi_document="url/or/path/to/openapi.yamlorjson")
skill['operationId'].invoke_async()
```
- Parse an OpenAPI document
- For each operation in the document, create a function that will
execute the operation
- Add all those operations to a skill in the kernel
- Modified `import_skill` to accept a dictionary of functions instead of
just class so that we can import dynamically created functions
- Created unit tests

TESTING:
I've been testing this with the following ChatGPT plugins:
- [Semantic Kernel Starter's Python Flask
plugin](https://github.com/microsoft/semantic-kernel-starters/tree/main/sk-python-flask)
- [ChatGPT's example retrieval
plugin](https://github.com/openai/chatgpt-retrieval-plugin/blob/main/docs/providers/azuresearch/setup.md)
- This one was annoying to setup. I didn't get the plugin functioning,
but I was able to send the right API requests
- Also, their openapi file was invalid. The "servers" attribute is
misindented
- [Google ChatGPT
plugin](https://github.com/Sogody/google-chatgpt-plugin)
- [Chat TODO plugin](https://github.com/lencx/chat-todo-plugin)
- This openapi file is also invalid. I checked with an online validator.
I had to remove"required" from the referenced request objects'
properties:
https://github.com/lencx/chat-todo-plugin/blob/main/openapi.yaml#L85

Then I used this python file to test the examples:

```python
import asyncio
import logging

import semantic_kernel as sk
from semantic_kernel import ContextVariables, Kernel
from semantic_kernel.connectors.ai.open_ai import AzureTextCompletion
from semantic_kernel.connectors.openapi.sk_openapi import register_openapi_skill

# Example usage
chatgpt_retrieval_plugin = {
    "openapi": # location of the plugin's openapi.yaml file,
    "payload": {
        "queries": [
            {
                "query": "string",
                "filter": {
                    "document_id": "string",
                    "source": "email",
                    "source_id": "string",
                    "author": "string",
                    "start_date": "string",
                    "end_date": "string",
                },
                "top_k": 3,
            }
        ]
    },
    "operation_id": "query_query_post",
}

sk_python_flask = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "path_params": {"skill_name": "FunSkill", "function_name": "Joke"},
    "payload": {"input": "dinosaurs"},
    "operation_id": "executeFunction",
}
google_chatgpt_plugin = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "query_params": {"q": "dinosaurs"},
    "operation_id": "searchGet",
}

todo_plugin_add = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "path_params": {"username": "markkarle"},
    "payload": {"todo": "finish this"},
    "operation_id": "addTodo",
}

todo_plugin_get = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "path_params": {"username": "markkarle"},
    "operation_id": "getTodos",
}

todo_plugin_delete = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "path_params": {"username": "markkarle"},
    "payload": {"todo_idx": 0},
    "operation_id": "deleteTodo",
}


plugin = todo_plugin_get # set this to the plugin you want to try

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

kernel = Kernel(log=logger)
deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()
kernel.add_text_completion_service(
    "dv", AzureTextCompletion(deployment, endpoint, api_key)
)

skill = register_openapi_skill(
    kernel=kernel, skill_name="test", openapi_document=plugin["openapi"]
)
context_variables = ContextVariables(variables=plugin)
result = asyncio.run(
    skill[plugin["operation_id"]].invoke_async(variables=context_variables)
)
print(result)
```

### Contribution Checklist

<!-- Before submitting this PR, please make sure: -->

- [ ] The code builds clean without any errors or warnings
- [ ] The PR follows the [SK Contribution
Guidelines](https://github.com/microsoft/semantic-kernel/blob/main/CONTRIBUTING.md)
and the [pre-submission formatting
script](https://github.com/microsoft/semantic-kernel/blob/main/CONTRIBUTING.md#development-scripts)
raises no violations
- [ ] All unit tests pass, and I have added new tests where possible
- [ ] I didn't break anyone :smile:

---------

Co-authored-by: Abby Harrison <abharris@microsoft.com>

---
## [EmanuelCN/kernel_xiaomi_sm8250](https://github.com/EmanuelCN/kernel_xiaomi_sm8250)@[2d10665563...](https://github.com/EmanuelCN/kernel_xiaomi_sm8250/commit/2d10665563c491c13b7ee72108368bf1a1eaf700)
#### Friday 2023-08-04 17:52:54 by Peter Zijlstra

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
Change-Id: I40e0e01946eadb1701a4d06758e434591e5a5c92

---
## [RatFromTheJungle/Skyrat-tg](https://github.com/RatFromTheJungle/Skyrat-tg)@[2f2ec4b9d6...](https://github.com/RatFromTheJungle/Skyrat-tg/commit/2f2ec4b9d64c448e5b544ecbcdca42a7dae0f094)
#### Friday 2023-08-04 18:21:25 by SkyratBot

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
## [BlackSilverUfa/data](https://github.com/BlackSilverUfa/data)@[911b73a709...](https://github.com/BlackSilverUfa/data/commit/911b73a70909df309079a6cd62273829d95d1f92)
#### Friday 2023-08-04 18:57:04 by Дмитрий Карих

Запись стрима 1307474557

* Daymare: 1994 Sandcastle — 2 [100%]
* Прохождения за один стрим — Little Orpheus - Episode 1 [100%]
* The Bridge Curse: Road to Salvation — Демо [100%]
* Первый взгляд 2022 — My Friendly Neighborhood (демо) [100%]
* Первый взгляд 2022 — SCP: Pandemic (демо) [100%]
* IXION — Демо [100%]

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[c8142e9aee...](https://github.com/git-for-windows/git/commit/c8142e9aeee1c8c4b3b302c26b4d9c85e0e5484c)
#### Friday 2023-08-04 19:09:26 by Johannes Schindelin

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
## [adrianwyatt/semantic-kernel](https://github.com/adrianwyatt/semantic-kernel)@[eab7a8f63a...](https://github.com/adrianwyatt/semantic-kernel/commit/eab7a8f63a0bfd289070e82b423ac78bd306ee5b)
#### Friday 2023-08-04 20:58:46 by Sailesh R

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
## [MCBCMF/MCBCMassacre](https://github.com/MCBCMF/MCBCMassacre)@[edb1540d30...](https://github.com/MCBCMF/MCBCMassacre/commit/edb1540d300f7636cac1e181939f76de2459a8d7)
#### Friday 2023-08-04 21:18:15 by Kelvin Williams

Murder?! Who me? Again?

Anytime you see two digits together over 15 you add them together. 16 is really a 7 and 38 is 11. 

11 means murder. 

B murdered is what this thing just told me when I tried to activate it. 

Do no evil Google? You’re not practicing what you preach. 

Learn more about how they talk to your subconscious. I went over this on my @kelvinewilliams Twitter a while back. Search for 22 or suicide. 

To learn about hotels, see @asotc23 on Twitter. 

Where’s Madonna? Where’s Nanea Reeves? Where’s the Gigi and John or the Galardo family? Where is my mother, Patricia Ann Crawley-Williams? (These are all very lucrative or strategic hotels). My moms is so important to the CIA and the government they killed everyone in a church to protect it and make sure it was never discovered.

---
## [MCBCMF/MCBCMassacre](https://github.com/MCBCMF/MCBCMassacre)@[d183ce9a21...](https://github.com/MCBCMF/MCBCMassacre/commit/d183ce9a21b6f971dbc382113198b69f5f786194)
#### Friday 2023-08-04 22:13:01 by Kelvin Williams

Update README.md - Daylight Download Link

Hehehe. Tactical advtage when working for the Creator. 

Catch up CIA/NSA. REMEMBER HE’S PISSED. I’m the hothead, now I gotta sit here and wait for Him to finish cause y’all had to go piss Him off.

Anyone listen to “When The Doves Cry” by Prince? 

Do you know the effort it must have took to make Mark the breakdancer and Kelvin best friend into Mark Charles Heidinger of Vandaveer? Listen to “A Mighty Levitathan of Old” on their (really His) “Divide & Conquer.”

Let this serve as a warning… “The Sound and the Fury” is the Creator speaking to Main, Annie and the CIA, and the US Federal Government. 

We all hate impersonation. But listen to this “But enough on that for now” (https://music.youtube.com/watch?v=heLmOj9h6C8&feature=share)… That’s not Mark nor Rose. That’s your CIA bragging about things they’re gonna wish they never had once I walk down Alphabet Street along West Sheepneck Rd in Maury county, TN.

---
## [Reziro/lancer-briefings](https://github.com/Reziro/lancer-briefings)@[0bb83de5ec...](https://github.com/Reziro/lancer-briefings/commit/0bb83de5ecd0a01eb0e23ac5a34d6576936f101f)
#### Friday 2023-08-04 22:48:27 by Reziro

Formatting No Work

Apparently, markdown formatting just straight up doesn't work here. That's lame as shit. Wish I was a fucking prodigy that could reprogram this shit sometimes but I am not that guy.

---
## [Foundation-19/Foundation-19](https://github.com/Foundation-19/Foundation-19)@[8de9ad250a...](https://github.com/Foundation-19/Foundation-19/commit/8de9ad250ad057d1b24aa81f449ff32c26816cd7)
#### Friday 2023-08-04 23:44:22 by cheesePizza2

Fixes contraband detectors (whooooooooooops) (#1228)

* whooooooooooooooooops

* fixes for my fixes

* fuck you

* qdel(announce)

* QDEL_NULL

---------

Co-authored-by: TheDarkElites <73414180+TheDarkElites@users.noreply.github.com>

---
## [vercel/next.js](https://github.com/vercel/next.js)@[e06880ea4c...](https://github.com/vercel/next.js/commit/e06880ea4c061fc5c298b262d01f347edd8dce74)
#### Friday 2023-08-04 23:47:13 by Josh Story

Implement new forking technique for vendored packages. (#51083)

## Vendoring

Updates all module resolvers (node, webpack, nft for entrypoints, and nft for next-server) to consider whether vendored packages are suitable for a given resolve request and resolves them in an import semantics preserving way.

### Problem

Prior to the proposed change, vendoring has been accomplished but aliasing module requests from one specifier to a different specifier. For instance if we are using the built-in react packages for a build/runtime we might replace `require('react')` with `require('next/dist/compiled/react')`.

However this aliasing introduces a subtle bug. The React package has an export map that considers the condition `react-server` and when you require/import `'react'` the conditions should be considered and the underlying implementation of react may differ from one environment to another. In particular if you are resolving with the `react-server` condition you will be resolving the `react.shared-subset.js` implementation of React. This aliasing however breaks these semantics because it turns a bare specifier resolution of `react` with path `'.'` into a resolution with bare specifier `next` with path `'/dist/compiled/react'`. Module resolvers consider export maps of the package being imported from but in the case of `next` there is no consideration for the condition `react-server` and this resolution ends up pulling in the `index.js` implementation inside the React package by doing a simple path resolution to that package folder.

To work around this bug there is a prevalence of encoding the "right" resolution into the import itself. We for instance directly alias `react` to `next/dist/compiled/react/react.shared-subset.js` in certain cases. Other times we directly specify the runtime variant for instance `react-server-dom-webpack/server.edge` rather than `react-server-dom-wegbpack/server`, bypassing the export map altogether by selecting the runtime specific variant. However some code is meant to run in more than one runtime, for instance anything that is part of the client bundle which executes on the server during SSR and in the browser. There are workaround like using `require` conditionally or `import(...)` dynamically but these all have consequences for bundling and treeshaking and they still require careful consideration of the environment you are running in and which variant needs to load.

The result is that there is a large amount of manual pinning of aliases and additional complexity in the code and an inability to trust the package to specify the right resolution potentially causing conflicts in future versions as packages are updated.

It should be noted that aliasing is not in and of itself problematic when we are trying to implement a sort of lightweight forking based on build or runtime conditions. We have good examples of this for instance with the `next/head` package which within App Router should export a noop function. The problem is when we are trying to vendor an entire package and have the package behave semantically the same as if you had installed it yourself via node_modules

### Solution

The fix is seemingly straight forward. We need to stop aliasing these module specifiers and instead customize the resolution process to resolve from a location that will contain the desired vendored packages. We can then start simplifying our imports to use top level package resources and generally and let import conditions control the process of providing the right variant in the right context.

It should be said that vendoring is conditional. Currently we only vendor react pacakges for App Router runtimes. The implementation needs to be able to conditionally determine where a package resolves based on whether we're in an App Router context vs a Page Router one.

Additionally the implementation needs to support alternate packages such as supporting the experimental channel for React when using features that require this version.

### Implementation

The first step is to put the vendored packages inside a node_modules folder. This is essential to the correct resolving of packages by most tools that implement module resolution. For packages that are meant to be vendored, meaning whole package substitution we move the from `next/(src|dist)/compiled/...` to `next/(src|dist)/vendored/node_modules`. The purpose of this move is to clarify that vendored packages operate with a different implementation. This initial PR moves the react dependencies for App Router and `client-only` and `server-only` packages into this folder. In the future we can decide which other precompiled dependencies are best implemented as vendored packages and move them over.

It should be noted that because of our use of `JestWorker` we can get warnings for duplicate package names so we modify the vendored pacakges for react adding either `-vendored` or `-experimental-vendored` depending on which release channel the package came from. While this will require us to alter the request string for a module specifier it will still be treating the react package as the bare specifier and thus use the export map as required.

#### module resolvers
The next thing we need to do is have all systems that do module resolution implement an custom module resolution step. There are five different resolvers that need to be considered

##### node runtime
Updated the require-hook to resolve from the vendored directory without rewriting the request string to alter which package is identified in the bare specifier. For react packages we only do this vendoring if the `process.env.__NEXT_PRIVATE_PREBUNDLED_REACT` envvar is set indicating the runtime is server App Router builds. If we need a single node runtime to be able to conditionally resolve to both vendored and non vendored versions we will need to combine this with aliasing and encode whether the request is for the vendored version in the request string. Our current architecture does not require this though so we will just rely on the envvar for now

##### webpack runtime
Removed all aliases configured for react packages. Rely on the node-runtime to properly alias external react dependencies. Add a resolver plugin `NextAppResolverPlugin` to preempt perform resolution from the context of the vendored directory when encountering a vendored eligible package.

##### turbopack runtime
updated the aliasing rules for react packages to resolve from the vendored directory when in an App Router context. This implementation is all essentially config b/c the capability of doing the resolve from any position (i.e. the vendored directory) already exists

##### nft entrypoints runtime
track chunks to trace for App Router separate from Pages Router. For the trace for App Router chunks use a custom resolve hook in nft which performs the resolution from the vendored directory when appropriate.

##### nft next-server runtime
The current implementation for next-server traces both node_modules and vendored version of packages so all versions are included. This is necessary because the next server can run in either context (App vs Page router) and may depend on any possible variants. We could in theory make two traces rather than a combined one but this will require additional downstream changes so for now it is the most conservative thing to do and is correct

Once we have the correct resolution semantics for all resolvers we can start to remove instances targeting our precompiled instances for instance making `import ... from "next/dist/compiled/react-server-dom-webpack/client"` and replacing with `import ... from "react-server-dom-webpack/client"`

We can also stop requiring runtime specific variants like `import ... from "react-server-dom-webpack/client.edge"` replacing it with the generic export `"react-server-dom-webpack/client"`

There are still two special case aliases related to react
1. In profiling mode (browser only) we rewrite `react-dom` to `react-dom/profiling` and `scheduler/tracing` to `scheduler/tracing-profiling`. This can be moved to using export maps and conditions once react publishses updates that implement this on the package side.
2. When resolving `react-dom` on the server we rewrite this to `react-dom/server-rendering-stub`. This is to avoid loading the entire react-dom client bundle on the server when most of it goes unused. In the next major react will update this top level export to only contain the parts that are usable in any runtime and this alias can be dropped entirely

There are two non-react packages currently be vendored that I have maintained but think we ought to discuss the validity of vendoring. The `client-only` and `server-only` packages are vendored so you can use them without having to remember to install them into your project. This is convenient but does perhaps become surprising if you don't realize what is happening. We should consider not doing this but we can make that decision in another discussion/PR.

#### Webpack Layers
One of the things our webpack config implements for App Router is layers which allow us to have separate instances of packages for the server components graph and the client (ssr) graph. The way we were managing layer selection was a but arbitrary so in addition to the other webpack changes the way you cause a file to always end up in a specific layer is to end it with `.serverlayer`, `.clientlayer` or `.sharedlayer`. These act as layer portals so something in the server layer can import `foo.clientlayer` and that module will in fact be bundled in the client layer.

#### Packaging Changes
Most package managers are fine with this resolution redirect however yarn berry (yarn 2+ with PnP) will not resolve packages that are not defined in a package.json as a dependency. This was not a problem with the prior strategy because it was never resolving these vendored packages it was always resolving the next package and then just pointing to a file within it that happened to be from react or a related package.

To get around this issue vendored packages are both committed in src and packed as a tgz file. Then in the next package.json we define these vendored packages as `optionalDependency` pointing to these tarballs. For yarn PnP these packed versions will get used and resolved rather than the locally commited src files. For other package managers the optional dependencies may or may not get installed but the resolution will still resolve to the checked in src files. This isn't a particularly satisfying implemenation and if pnpm were to be updated to have consistent behavior installing from tarballs we could actually move the vendoring entirely to dependencies and simplify our resolvers a fair bit. But this will require an upstream chagne in pnpm and would take time to propogate in the community since many use older versions

#### Upstream Changes

As part of this work I landed some other changes upstream that were necessary. One was to make our packing use `npm` to match our publishing step. This also allows us to pack `node_modules` folders which is normally not supported but is possible if you define the folder in the package.json's files property.

See: #52563

Additionally nft did not provide a way to use the internal resolver if you were going to use the resolve hook so that is now exposed

See: https://github.com/vercel/nft/pull/354

#### additional PR trivia
* When we prepare to make an isolated next install for integration tests we exclude node_modules by default so we have a special case to allow `/vendored/node_modules`

* The webpack module rules were refactored to be a little easier to reason about and while they do work as is it would be better for some of them to be wrapped in a `oneOf` rule however there is a bug in our css loader implementation that causes these oneOf rules to get deleted. We should fix this up in a followup to make the rules a little more robuts.


## Edits
* I removed `.sharedlayer` since this concept is leaky (not really related to the client/server boundary split) and it is getting refactored anyway soon into a precompiled runtime.

---

