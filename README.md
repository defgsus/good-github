## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-11-30](docs/good-messages/2023/2023-11-30.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 5,134,662 were push events containing 6,227,408 commit messages that amount to 284,531,120 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 63 messages:


## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[2011c229f9...](https://github.com/realforest2001/forest-cm13/commit/2011c229f9a37de8fa67a74d8e40974515724cde)
#### Thursday 2023-11-30 00:03:59 by stalkerino

Readds skull facemask and facepaint (#5042)

# About the pull request
It readds two items that were removed in the past for no valid reason
(in my opinion), since it was a targeted PR against a specific player I
do not think it should've been removed.

# Explain why it's good for the game

It looks nice and fits the atmosphere, adding it will help players
customize their characters without being too loud.
The removal reason of "You'd get laughed at for wearing it IRL" is
invalid, a lot of military and law enforcement people wear skull masks,
punisher emblems and etcetra - this is especially evident in America
(We're UA)

https://discord.com/channels/150315577943130112/746325423289401395/1168350579307860078

https://discord.com/channels/150315577943130112/827156857566265375/1145494273568022588
https://files.catbox.moe/4o3ag1.png

https://discord.com/channels/150315577943130112/604397850675380234/1094357565317586964
-- the person who made it admitting it was targeted.


# Testing Photographs and Procedure
I don't think it needs testing
</details>


# Changelog
:cl: stalkerino
add: readds skull facepaint and skull balaclava (blue and black)
/:cl:

---
## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[a955791561...](https://github.com/realforest2001/forest-cm13/commit/a955791561d5aeab0ff0640923fe1192ad377830)
#### Thursday 2023-11-30 00:03:59 by fira

/tg/ Status effects part 1 - fluid status updates (#4828)

![image](https://github.com/cmss13-devs/cmss13/assets/604624/38cdd1a0-e13c-4d69-b893-49cea2a8113f)
CM Dev figured it out 9 years ago and nobody listened and kept tacking
illogical conditions

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

Builds on previous "prelude" PRs in the following steps:
 * Ports /tg/ body_position and mobility_flags
* Fixes some interaction requirements to use stun/mobility rather than
lying/knocked_down
* Ports /tg/ granular status updates, ie. status propagating through
handlers and signals. This includes changes to resting, buckling, and
lying down human transforms.
 * Wires our status effect system to it directly
* Removes `update_canmove` from existence completely as not needed
anymore

Because step 1 and 2 require updating all the gameplay logic using them,
this PR modifies a lot of files.

Part 2 will move the actual status effects to /tg/ status_effects,
resolving our timing problems.

# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Testing Checklist!</summary>

- [x] Basic Movement
- [x] Admin Freeze Prevents Movement
- [x] Resting, Getting Up
- [x] Xenos change icon when resting
- [x] Buckling, including bed rotation and propelled chairs
- [x] Crawling Movement including sprite movement
- [x] Aggressive, Choke Grabbing, and Fireman carry apply rotation
- [x] Xeno Pounce and Abduct properly freeze both target and caster 
- [x] Double dropship seats density update
- [x] Explosive knockout on Humans
- [x] Xeno burrow density and movement interactions
- [x] Xeno nest interactions, specifically confirm density changes work
- [ ] Xeno nest bullet hits doublecheck with snowflake trait check
- [x] Combat Xeno ~~knockouts~~ knockdown and sprite updates
- [x] ~~Sleeping, Waking up, Usage of items while sleeping~~ - Can't
really test this we have almost no sleep code
- [x] Arbitrary buckling rotations
- [x] Admin-set transforms work with buckling/lying
- [ ] All the broken objects that will only be found out in Testmerge

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
label your changes in the changelog. Please note that maintainers freely
reserve the right to remove and add tags should they deem it
appropriate. You can attempt to finagle the system all you want, but
it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Maintainers freely reserve the right to remove and add
tags should they deem it appropriate. -->

:cl:
code: Ported basic /tg/ Status Backend.
add: Human transform changes such as lying down, knock down, buckling,
are now animated.
fix: Some statuses will now take effect immediately instead of waiting
for a life tick, notably Resting.
balance: Many interaction requirements were changed to eg. fail upon
stuns rather than if lying down.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [Zevotech/Shiptest](https://github.com/Zevotech/Shiptest)@[40dfaf3734...](https://github.com/Zevotech/Shiptest/commit/40dfaf3734000b5e74e4101ab86516702f59425f)
#### Thursday 2023-11-30 00:29:01 by Imaginos16

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
## [HoloShaii/Virulence](https://github.com/HoloShaii/Virulence)@[d48972061e...](https://github.com/HoloShaii/Virulence/commit/d48972061ef63ea55dc3c71849024e456f7b1745)
#### Thursday 2023-11-30 00:36:17 by HoloShaii

Holy fucking shit got so much done just look at the To-Do list, not gonna write all that shit here

---
## [NetHack/NetHack](https://github.com/NetHack/NetHack)@[0473fff5b5...](https://github.com/NetHack/NetHack/commit/0473fff5b5908896ac12829afb523ad6d614af4f)
#### Thursday 2023-11-30 00:37:19 by Michael Meyer

Make destruction of altar incite its god's wrath

This is for completely destroying an altar with extra-powerful magical
digging -- the normal altar_wrath() punishment didn't seem sufficient
for such an outrage to me, so skip straight to slinging the lightning
bolts.  Destroying an altar is unlikely to happen by accident (though
it's possible with poorly timed usage of a drum of earthquake).

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[39d9c45b4a...](https://github.com/tgstation/tgstation/commit/39d9c45b4a7afc2a963de4249592a3d4ae6c4715)
#### Thursday 2023-11-30 00:59:44 by san7890

Meat Hook Rework (Accidental Features) (#80002)

## About The Pull Request

Or, how I tried to kill `/datum/forced_movement` but got absolutely
clonged.

Actually, I did kill `/datum/forced_movement`. It was only used in one
spot so I just went ahead and cooked it into a special utility datum
that should only be used in one spot. We can optimize the code later or
something, but I like the way it is right now (pretty much status quo
without the potential of someone using a depreciated framework).

Alright, there were also like 3 `TODO`s (4 if you count the move loop
comment (which is ehhhh)). I naively tried to tackle them a very hard
way, but then I just realized I could use the fancy new datum I cooked
up and wow they're all solved now. The hook looks so fucking good now.

* The code is overall more streamlined, with all of the post-projectile
work being handled by a special datum (I wanted it to be handled by the
hook but the timings were all based on SSFastprocess so datum it is).
Forced movement is killed but we just salvaged whatever we needed from
it.
* More traits to ensure we don't cheese in a way we're not supposed to
* A very sexy chain will spawn when you drag your kill in (this wasn't
there before but I fixeded it :3)
* The firer will actually get grounded when they try and shoot the chain
out. They get grounded for 0.25 seconds unless they hit something. I
don't know how the timing is but I think it's fair.
* We also add a unique suicide act, because I noticed we did the
"magical" one previously, which big-league sucked.
* More traits to ensure less cheese! I like how nice it is now.
## Why It's Good For The Game

The meat hook really makes you _feel_ like Roadhog from Overwatch.
Resolves a bunch of old TODOs while getting rid of a completely obsolete
framework in a really neat way. I don't typically like mixing balances
and refactors but these TODOs were getting crusty man i just wanted to
get them out of the way
## Changelog
:cl:
balance: The Meat Hook will now "ground" you whenever you fire it out at
someone. You get a very small immobilization every time you fire, which
"upgrades" to a full immobilization whenever you actually hit an atom
and start to drag it in.
fix: A chain should now show up as you drag in something with the meat
hooks.
fix: Meat hooks should no longer play the "magical gun" suicide if you
were to use it, but instead do their own unique thing.
/:cl:

---
## [Imaginos16/Shiptest](https://github.com/Imaginos16/Shiptest)@[caa19d2a6f...](https://github.com/Imaginos16/Shiptest/commit/caa19d2a6f8014c2d34663c7c63685921bc0218a)
#### Thursday 2023-11-30 01:01:51 by GenericDM

Assorted cringe removal pt.whatever (#2534)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Removes more cringe I found laying around.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
/tg/ was on some WILD shit.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
del: removes tail club
del: removes all flavors of tail whip
del: removes lizardskin clothing
del: removes 'Genetic Purifier'
tweak: makes bunny ears desc not incredibly sexist
tweak: change up wording in magic mirror gender change
del: removes 'genuine' cat ears
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[08ab5d2731...](https://github.com/san7890/bruhstation/commit/08ab5d27312d236593eabdb27fb23dccbf8283e6)
#### Thursday 2023-11-30 01:04:30 by Mothblocks

Blood brothers is now a single person conversion antagonist (#79971)

## About The Pull Request
Instead of choosing 2-3 brothers, *one* person will be selected and
given a flash which can convert one other person over. In accordance to
the existing 10% chance for 3 members, there is a 10% chance that the
first person converted will receive a flash of their own.

Expectation is people will flash a friend or a robust guy or whatever.
My intent is primarily to see if this kind of blood brothers is more
enjoyable to play with/against, and if their inclusion in a round
increases the general chaos of it. My theory is that since most likely
blood brothers will be people who know each other, that it can become
more consistently interesting to the rest of the crew. That or they just
murderbone together idk

Fikou and head admins said they wanted this to replace rather than add
which I agree with.

## Why It's Good For The Game
Keeps the sandboxy aspect of blood brothers (no uplink) while likely
making it more enjoyable to play. Conversion is equally as simple as
revs for the user, and is just as intuitive to the one being converted
since there are no new mechanics thrown in your face.

Blood brothers is currently disabled everywhere on the main servers
except for MRP. I think this form will be more appealing to all
rulesets. If left enabled, Dynamic now has more antagonists to make
rounds diverse with and I want that

## Changelog

:cl:
add: Instead of teaming up random people together, blood brothers will
now start out with one player and let them convert a single other person
over to blood brother using a flash.
/:cl:

---
## [RedBaronFlyer/RedBaronFlyer](https://github.com/RedBaronFlyer/RedBaronFlyer)@[7fce8cd805...](https://github.com/RedBaronFlyer/RedBaronFlyer/commit/7fce8cd8054cc1d0b048db12d7e9587b42fcdef2)
#### Thursday 2023-11-30 01:23:33 by san7890

Codifies male goats not having an udder (#79722)

## About The Pull Request

This was addressed in #78759 (1b1fde4908826ef5c54ffc0734e74028270af3fd)
and reviewed (and merged even though I didn't respond to it, oh well),
but I half-assed it because the whole point was to prevent male goats
from having an udder, but I only added it to the subtype of Pete i made
in that PR. Let's expand that to all male goats now.
## Why It's Good For The Game

It doesn't make biological nor morphological sense as to why a male goat
can provide milk. Ideally this should be like this for all animals
(because that's real life) but that's a later issue with further balance
implication.

I think it's still an interesting idea that Nanotrasen will just send
you any old goat despite it being "useless" beyond being very good at
eating plants. Maybe cargo should have a way to guarantee getting a
female goat in the future? It's just like real life where zoos and farms
have to constantly dealw ith female animals (such as giraffes or other
exotic stuff) tending to be far rarer/cost far more than their male
variants due to the potential to generate offspring (there's more nuance
to husbandry than this but just play along)... and in space, every
animal is "exotic".

It still remains possible to biogenerate milk, which tends to be far
faster than feeding/milking goats- which is something that the cook
should have access to anyways.
## Changelog
:cl:
balance: Male Goats should no longer spawn with an udder, instead of it
just being Pete.
/:cl:

---------

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [zohaib02/Java-Exercises](https://github.com/zohaib02/Java-Exercises)@[8f4b457c1c...](https://github.com/zohaib02/Java-Exercises/commit/8f4b457c1cf036938d42fa34872b02bce27729e7)
#### Thursday 2023-11-30 01:50:42 by zohaib02

Hey there! Ever dreamed of creating your own ice cream masterpiece? Look no further! This Ice Cream Store App, built with Java and Swing, brings your ice cream fantasies to life. Choose your flavors (Chocolate, Strawberry, Vanilla) and toppings (Sprinkles, Marshmallows, Flakes, Caramel) with a click, and voilà! It calculates the total price in a snap.

Description:
Welcome to the Ice Cream Store! Picture a fun and interactive app that lets you craft your dream ice cream. We've put our hearts into this creation to ensure it's not just an app but an experience.

Easy, Fun, and Visual:

We've made it super easy to pick your flavors and toppings—just click away! The interface is designed to be intuitive and visually appealing, ensuring a seamless and delightful experience.
Magic Happens in Real-Time:

Ever seen prices change magically as you select? Well, that's us! We've got real-time calculations going on. You choose, and instantly, the total price pops up, keeping you engaged and excited.
No Stress, Just Ice Cream Bliss:

Made a mistake or want to start fresh? No worries! Hit 'Clear All' for a clean slate. It's all about making your experience stress-free and enjoyable.
Geeky Stuff Behind the Scenes:

Behind this ice cream paradise, there's some serious Java and Swing magic happening. We've poured our expertise into every detail, ensuring a smooth and responsive interface.
A Treat for Ice Cream Lovers:

We didn't just build an app; we crafted an experience. It's not just about flavors and toppings; it's about translating dreams into real, user-centric software.

So, are you ready to indulge in a scoop of digital ice cream paradise? Dive into our Ice Cream Store and let your imagination create the perfect treat!

---
## [adamcreater/bestofthebest](https://github.com/adamcreater/bestofthebest)@[0fffb4124d...](https://github.com/adamcreater/bestofthebest/commit/0fffb4124d1bac1c8fcfe9dab2240d3cb26100ae)
#### Thursday 2023-11-30 02:02:03 by adamcreater

README.md

Free


📸🔓💯 Adobe Photoshop Crack Download: Unleash Your Creativity for Free! 🎨🔥

Get ready to take your photo editing skills to the next level with Adobe Photoshop Crack Download Free Now! 🚀💥 This phenomenal software gives you access to a wide range of advanced tools and features without having to spend a dime. 💸✨

With Adobe Photoshop Crack, you'll have endless possibilities at your fingertips. 💫💡 Enhance colors, remove imperfections, and add jaw-dropping effects effortlessly. 🌈🖌️ Let your imagination run wild and watch your creations come to life with just a few clicks! 🌟🖼️

Experience seamless integration with other Adobe Creative Cloud apps, collaborate with fellow creatives, and boost your productivity like never before. 💻🤝✅ Adobe Photoshop Crack Download is user-friendly and suitable for beginners and professionals alike. ⚡🎉

Unlock the full potential of Adobe Photoshop today! Download Adobe Photoshop Crack and start exploring a world of limitless possibilities. 🚀🔓

---
## [chromium/chromium](https://github.com/chromium/chromium)@[ea7ee982c6...](https://github.com/chromium/chromium/commit/ea7ee982c6b804ed01b54e8f97917a590dd21c0d)
#### Thursday 2023-11-30 02:21:00 by Devlin Cronin

[Extensions] Duct tape a crash in --pack-extension

--pack-extension allows a user (or, more likely, tool) to pack
an extension from the commandline. This works by short-circuiting
the browser startup process, packing the extension, and early-returning
from the main loop in Chrome.

This happens *before* the base::FeatureList is initialized. Prior to
https://crrev.com/ca7b5601102d, checking the state of a feature before
feature list initialization would return the default value. Now, it
crashes.

In this CL, change the checks that happen in SimpleFeature and friends
to check the state of the feature if the FeatureList is initialized and,
if not, fall back to the default state of the feature. This is okay in
the pack extension case because we still have all the same checks in
place when *using* the extension and it's already trivially possible to
pack an extension with any conceivable feature state (by just appending
commandline flags).

This is only a band-aid fix for the issue. This will still crash if any
of the ManifestHandlers or other extension-creation mechanisms use
base::FeatureList::IsEnabled() before feature list initialization. The
right fix here is to move the pack extension job after the
FeatureList is initialized so that we don't have to have these hacks
in place; however, that's non-trivial due to other issues that come up
when we try to delay pack-extension handling. We'll look into fixing
this more properly in a follow-up, but this should at least prevent
crashing in many of the cases.

Add a browsertest that repros the bug and verifies the fix.

Bug: 1498558
Change-Id: I2429346e77aeae207a3d21f85853db87442556cb
Reviewed-on: https://chromium-review.googlesource.com/c/chromium/src/+/5072730
Reviewed-by: Tim <tjudkins@chromium.org>
Commit-Queue: Devlin Cronin <rdevlin.cronin@chromium.org>
Cr-Commit-Position: refs/heads/main@{#1231094}

---
## [vdaular-dev/linksfordevs](https://github.com/vdaular-dev/linksfordevs)@[7f2ded4fc7...](https://github.com/vdaular-dev/linksfordevs/commit/7f2ded4fc7fd996f3c4b1c853a28656a28124692)
#### Thursday 2023-11-30 02:31:17 by Ben Dornis

Updating: 11/28/2023 10:00:00 PM

 1. Added: GitHub - fempire/women-tech-speakers-organizers: A list of women tech speakers & organizers. Add yourself or others by submitting a PR! PS if you do add someone, make sure to tell them! :) #fempire
    (https://github.com/fempire/women-tech-speakers-organizers)
 2. Added: .NET 8 and C# 12 — Experimental Attribute
    (https://henriquesd.medium.com/net-8-and-c-12-experimental-attribute-c895d66bba4e)
 3. Added: Goodbye DevRel… (for now)
    (https://spinscale.de/posts/2023-11-28-goodbye-devrel.html)
 4. Added: Cloud translation is more expensive than I thought
    (https://hiandrewquinn.github.io/til-site/posts/selkouutiset-archive-now-supports-77-languages/)
 5. Added: "Position Strings" for Collaborative Lists and Text
    (https://mattweidner.com/2023/04/13/position-strings.html)
 6. Added: Five Learnings from Five Years as a First-Time Founder
    (https://www.lureinperera.com/post/five-learnings-from-five-years-as-a-first-time-founder)
 7. Added: Deploy your CloudKit-backed SwiftData entities to production
    (https://www.leojkwan.com/swiftdata-cloudkit-deploy-schema-changes/)
 8. Added: A year working with HTML Web Components
    (https://hawkticehurst.com/writing/a-year-working-with-html-web-components/)
 9. Added: Consider Writing Documentation for Your House
    (https://luke.hsiao.dev/blog/housing-documentation/)
10. Added: The Ideal Social Network
    (https://www.zaxis.page/p/social-network)
11. Added: What is going on with Mars Sample Return?
    (https://caseyhandmer.wordpress.com/2023/11/26/what-is-going-on-with-mars-sample-return/)
12. Added: Trying simple tree-search techniques for LLM token sampling
    (https://andys.page/posts/llm_sampling_strategies/)
13. Added: Dependency rejection
    (https://amontalenti.com/2023/11/25/dependency-rejection)
14. Added: Nextty: a radically collaborative computing environment
    (https://offbyone.us/posts/nextty-idea/)
15. Added: My techno-optimism
    (https://vitalik.ca/general/2023/11/27/techno_optimism.html)
16. Added: Matrix vs. XMPP | Luke's Webpage
    (https://lukesmith.xyz/articles/matrix-vs-xmpp/)
17. Added: construct0, the first steps of an organisation with great aspirations.
    (https://blog.benjaminvr.net/2023/11/construct0-first-steps-of-organisation.html)
18. Added: Rust: Memory Management
    (https://priver.dev/blog/rust/memory-management/)
19. Added: ML.NET 3.0 Boosts Deep Learning, Data Processing for .NET-Based AI Apps -- Visual Studio Magazine
    (https://visualstudiomagazine.com/articles/2023/11/28/ml-net-3-0.aspx)
20. Added: Bazel market growth, year over year
    (https://blog.aspect.dev/bazel-market-2023)
21. Added: The quality of your life is the quality of the people you get to know: Illuminating the David Brooks way
    (https://jakeseliger.com/2023/11/28/the-quality-of-your-life-is-the-quality-of-the-people-you-get-to-know-illuminating-the-david-brooks-way/)
22. Added: Mercure, Braid, PREP… news about subscribing to HTTP resource updates - Kévin Dunglas
    (https://dunglas.dev/2023/11/mercure-braid-prep-news-about-subscribing-to-http-resource-updates/)
23. Added: Yusuf Aytas - Talent Sourcing Journey
    (https://www.yusufaytas.com/talent-sourcing-journey/)
24. Added: Should this be an A/B Test?
    (https://alexeymk.com/2023/11/26/should-this-be-an-ab-test)
25. Added: My Personal Data Backup Pipeline – Justin Paulin
    (https://justinpaulin.com/2023/11/27/my-personal-data-backup-pipeline/)
26. Added: My Ego Is My Enemy. Your Ego Is Your Enemy.
    (https://preslav.me/2023/10/06/my-ego-is-my-enemy-your-ego-is-your-enemy/)
27. Added: How we fixed my SEO | johnnyreilly
    (https://johnnyreilly.com/how-we-fixed-my-seo)
28. Added: Nighttime Time Lapse Photography with AllSky
    (https://johnjonesfour.com/2023/12/01/nighttime-time-lapse-photography-with-allsky/)
29. Added: Building a Critter Stack Application: Event Storming
    (https://jeremydmiller.com/2023/11/28/building-a-critter-stack-application-event-storming/)
30. Added: Running SQL Queries on Org Tables
    (http://yummymelon.com/devnull/running-sql-queries-on-org-tables.html)
31. Added: Ryle on microphysics and the everyday world
    (http://edwardfeser.blogspot.com/2023/11/ryle-on-microphysics-and-everyday-world.html)
32. Added: Embark: Dynamic documents for making plans
    (https://www.inkandswitch.com/embark/)
33. Added: RAG Pipelines from scratch
    (https://www.zansara.dev/posts/2023-10-27-haystack-series-rag/)
34. Added: The Village Effect of the Greater Web
    (https://www.fromjason.xyz/p/notebook/the-village-effect-of-the-greater-web/)
35. Added: How to Do a Competitive Analysis for Startups?
    (https://frederik.today/blog/how-to-do-a-competitive-analysis-for-startups)

Generation took: 00:13:05.2813355

---
## [Wongboo/pytorch](https://github.com/Wongboo/pytorch)@[a911b4db9d...](https://github.com/Wongboo/pytorch/commit/a911b4db9d82238a1d423e2b4c0a3d700217f0c1)
#### Thursday 2023-11-30 02:52:56 by voznesenskym

AOTAutograd: handle set_(), detect metadata mutations that cancel out (#111554)

This should be enough to get @voznesenskym 's FSDP branch to plumb `set_()` through AOTAutograd properly and have everything properly no-op out. Main changes are:

(1) graph break on `aten::set_.source_Tensor_storage_offset` (we could support it but it isn't needed, seems safer to graph break)

(2) Functionalization: add a "proper" functionalization kernel for `aten::set_.source_Tensor`. The previous one we had was codegen'd and it was wrong (it would just clone() and call set_(), which does not do the right thing). I also manually mark on the `FunctionalTensorWrapper` when a given tensor has been mutated by a `set_()` call.

(3) AOTAutograd: I added a new field, `InputAliasInfo.mutates_storage_metadata`, so we can distinguish between "regular" metadata mutations, and metadata mutations due to `set_()` calls. This is mainly because at runtime, one requires calling `as_strided_()` to fix up metadata, while the other requires calling `set_()`.

(4) Made AOTAutograd's detection for metadata mutations / set_() mutations smarter and detect no-ops (if the storage and metadata are all the same).

I also killed `was_updated()` and `was_metadata_updated()`, and replaced them with (existing) `has_data_mutation() ` and (new) `has_data_mutation()`, which can more accurately distinguish between data-mutation vs. `set_()` calls vs. metadata-mutation

**This PR is still silently correct in one case though**, which I'd like to discuss more. In particular, this example:
```
def f(x):
    x_view = x.view(-1)
    x.set_(torch.ones(2))
    x_view.mul_(2)
    return
```

If you have an input that experiences both a data-mutation **and** a `x_old.set_(x_new)` call, there are two cases:

(a) the data mutation happened on the storage of `x_new`. This case should be handled automatically: if x_new is a graph intermediate then we will functionalize the mutation. If x_new is a different graph input, then we will perform the usual `copy_()` on that other graph input

(b) the data mutation happened on the storage of `x_old`. This is more of a pain to handle, and doesn't currently work. At runtime, the right thing to do is probably something like:
```

def functionalized_f(x):
    x_view = x.view(-1)
    # set_() desugars into a no-op; later usages of x will use x_output
    x_output = torch.ones(2)
    # functionalize the mutation on x_view
    x_view_updated = x.mul(2)
    x_updated = x_view_updated.view(x.shape)
    # x experienced TWO TYPES of mutations; a data mutation and a metatadata mutation
    # We need to return both updated tensors in our graph
    return x_updated, x_output
def runtime_wrapper(x):
    x_data_mutation_result, x_set_mutation_result = compiled_graph(x)
    # First, perform the data mutation on x's old storage
    x.copy_(x_data_mutation_result)
    # Then, swap out the storage of x with the new storage
    x.set_(x_set_mutation_result)
```

There are two things that make this difficult to do though:

(1) Functionalization: the functionalization rule for `set_()` will fully throw away the old `FunctionalStorageImpl` on the graph input. So if there are any mutations to that `FunctionalStorageImpl` later on in the graph, the current graph input won't know about it. Maybe we can have a given `FunctionalTensorWrapper` remember all previous storages that it had, and track mutations on all of them - although this feels pretty complicated.

(2) AOTAutograd now needs to know that we might have *two* graph outputs that correspond to a single "mutated input", which is annoying.

It's worth pointing out that this issue is probably extremely unlikely for anyone to run into - can we just detect it and error? This feels slightly easier than solving it, although not significantly easier. We would still need `FunctionalTensorWrapper` to keep track of mutations on any of its "previous" storages, so it can report this info back to AOTAutograd so we can raise an error.

Pull Request resolved: https://github.com/pytorch/pytorch/pull/111554
Approved by: https://github.com/ezyang
ghstack dependencies: #113926

---
## [f13babylon/f13babylon](https://github.com/f13babylon/f13babylon)@[2f8b621240...](https://github.com/f13babylon/f13babylon/commit/2f8b62124081d83f1dc9ee4085e0365a33a4bb2f)
#### Thursday 2023-11-30 03:45:17 by K4rlox

Chruch PR, attempt 3 to fix merge coflict (#249)

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

this PR works on redesigning, and moving the warren church to bighorn

![2023-11-24 13 33
01](https://github.com/f13babylon/f13babylon/assets/118483925/f9e8cb97-cdb1-46b7-950a-4c0364fad0a8)

![2023-11-24 13 33
20](https://github.com/f13babylon/f13babylon/assets/118483925/3ee346c1-c788-4c87-8e9b-31381030bc31)


the preacher already is considered a bighorn citizen so the church being
in warren used to make no sense

this fixes the issue and adds a few additional community requested
changes


this is a second attempt because the last one was closed because of a
item that crashed the server that i forgot to mention in changelogs


### **please if you want something changed then say it**
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Preacher is supposed to be a citizen of bighorn therefore have a church
in bighorn, but they for some reason had a church in warren instead of
bighorn, i have heard some community members arguing about it and
decided to act on it as it only makes sense for the church to be
somewhere close to bighorn instead of in warren.

adds more items for the priest to use, adds an actual spawning landmark
for the priest to spawn in the church instead of a random matrix

adds several other misc items such as a angel food cake, a holy water
bottle, bread, wine, and several spare bibles

oh also gives the preacher closet a shotgun with no ammo, since the
preacher landmark seems to have a shotgun icon.

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
add: church in (front of) bighorn
add: bible, bread, wine and water crate
add: holy water flask
add: angel food cake
add: Priest shotgun (with no ammo)
add: Preacher starter landmark
add: water bottles
tweak: changes the bible on the table to the whiskey bible
fix: fixes the prayer breads not working

/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [EasyApp-RPI/EasyApp](https://github.com/EasyApp-RPI/EasyApp)@[49ebd50be3...](https://github.com/EasyApp-RPI/EasyApp/commit/49ebd50be3835bd0934104fdb29b522c326e0c96)
#### Thursday 2023-11-30 04:03:01 by Anthony Fabius

Working Interests and SkillsComp

The amount of blood sweat and tears I put into this commit is not funny. Thought I was gonna have to switch majors if this shit didn't work ngl.

---
## [mazzinsanity/f13babylon](https://github.com/mazzinsanity/f13babylon)@[f996624f34...](https://github.com/mazzinsanity/f13babylon/commit/f996624f34bd17872783cf0757300c93cc116f38)
#### Thursday 2023-11-30 04:03:28 by foxymegneil

Enclave Marineification (#251)

## About The Pull Request

Changes all the icons and items of Enclave enlisted rank tabs (officer
tabs are the same between the Army and Marines) to be that of the Marine
Corps, while also adding some new ones that can be used for RP or
whatever. Also appropriately hands out said tabs. Private tab is GONE,
because it doesn't exist in the Marine Corps. You also may notice a
Petty Officer Third Class tab. What's that for? Well, it was originally
going to be for the Navy Corpsman loadout for the Specialist, however
loadouts seem to suffer with terminally low storage, so I wasn't able to
fit a rank tab into either of the loadouts. The item and icon are being
left in, however, just in case someone smarter than me can fix it.

Anyway, here are the sprites:

![sprites](https://github.com/f13babylon/f13babylon/assets/85942538/8b239726-1efb-43d3-a15d-731453df4a30)

## Why It's Good For The Game

We're Marines now! To hell with those Army tabs!
It's more immersive, and gosh darn it, that's all we Enclave players
have left. Immersion.

## Pre-Merge Checklist
- [x] You tested this on a local server.
- [x] This code did not runtime during testing.
- [x] You documented all of your changes.


## Changelog


:cl:
add: Adds some brand new Marine Corps tabs.
del: Old Army tabs that aren't needed anymore.
tweak: Changes some of the old tabs to new ones.
imageadd: New tabs!
imagedel: Old ones are gone.
/:cl:

---
## [anirudh-hegde/numpy](https://github.com/anirudh-hegde/numpy)@[af55348f5c...](https://github.com/anirudh-hegde/numpy/commit/af55348f5cbe338a86ed032812ee11e8714be673)
#### Thursday 2023-11-30 04:13:36 by Sebastian Berg

API: Allow comparisons with and between any python integers

This implements comparisons between NumPy integer arrays and arbitrary valued
Python integers when weak promotion is enabled.

To achieve this:
* I allow abstract DTypes (with small bug fixes) to register as loops (`ArrayMethods`).
  This is fine, you just need to take more care.
  It does muddy the waters between promotion and not a bit if the
  result DType would also be abstract.
  (For the specific case it doesn't, but in general it does.)
* A new `resolve_descriptors_raw` function, which does the same job as
  `resolve_descriptors` but I pass it this scalar argument
  (can be expanded, but starting small).
  * This only happens *when available*, so there are some niche paths were this cannot
    be used (`ufunc.at` and the explicit resolution function right now),
    we can deal with those by keeping the previous rules (things will just raise
    trying to convert).
  * The function also gets the actual `arrays.dtype` instances while I normally ensure that
    we pass in dtypes already cast to the correct DType class.
    (The reason is that we don't define how to cast the abstract DTypes as of now,
    and even if we did, it would not be what we need unless the dtype instance actually had
    the value information.)
* There are new loops added (for combinations!), which:
  * Use the new `resolve_descriptors_raw` (a single function dealing with everything)
  * Return the current legacy loop when that makes sense.
  * Return an always true/false loop when that makes sense.
  * To achieve this, they employ a hack/trick: `get_loop()` needs to know the value,
    but only `resolve_descriptors_raw()` does right now, so this is encoded on whether we use
    the `np.dtype("object")` singleton or a fresh instance!
    (Yes, probably ugly, but avoids channeling things to more places.)

Additionally, there is a promoter to say that Python integer comparisons can just use
`object` dtype (in theory weird if the input then wasn't a Python int,
but that is breaking promises).

---
## [RogueMaster/flipperzero-firmware-wPlugins](https://github.com/RogueMaster/flipperzero-firmware-wPlugins)@[c27986d4cf...](https://github.com/RogueMaster/flipperzero-firmware-wPlugins/commit/c27986d4cf1a22003866784ee65ea91dbc8cd6f1)
#### Thursday 2023-11-30 04:14:17 by Leeroy

Rollback Keyloq to 5 months ago! Bloody regressions making my daily life shit!

---
## [BMO-Financial-Inc/.github](https://github.com/BMO-Financial-Inc/.github)@[47ee50d0cb...](https://github.com/BMO-Financial-Inc/.github/commit/47ee50d0cbc58c5c2423b64712c0c4eb9beaba78)
#### Thursday 2023-11-30 04:36:31 by Chais Thomas Fitzwater

Create README.md

BMO-Financial-Inc/.github is a special repository: this README.md will appear on your public organization profile, visible to anyone.Chais Fitzwater stock portfolio - Google Finance November, 26. 2023 8:10 am 1160 walker ave, saint Louis. Mo 63138..I would like to propose moving support for the PulseAudio sound server into Arch Linux proper. This would also be in preparation for the eventual arrival of Gnome 3, since it will be unlikely we can effectively maintain the needed GStreamer patch any more.

To that effect I have created a plan:

---

To provide PulseAudio in [extra]...

Move the following packages from [community] to [extra]:
- libasyncns
- rtkit
- pulseaudio (split into pulseaudio and libpulse)
- alsa-plugins
- pulseaudio-alsa
    Configuration package, contains /etc/asound.conf
    depends on pulseaudio, alsa-plugins
- pavucontrol
- paprefs
- pulseaudio-mixer-applet
- ossp
    provides osspd OSS emulator

Rebuild the following packages with PulseAudio support:
- sdl (sdl-pulse in AUR)
- openal (openal-pulse in AUR)
- libgstreamer0.10-good
    split gstreamer0.10-pulse (in community)
- libao
    split libao-pulse (in community)
- libcanberra
    split libcanberra-pulse (in community)
    will be a split plugin instead of a wholly rebuilt copy
- gnome-media
    split gnome-media-pulse (in community; rebuilt with --enable-pulse)
- gnome-settings-daemon
    split gnome-settings-daemon-pulse (in community; rebuilt without gstreamer patch)

Provide the following groups:
- pulseaudio-gnome
    pulseaudio-alsa
    libcanberra-pulse
    gstreamer0.10-pulse
    gnome-media-pulse
    gnome-settings-daemon-pulse
    pulseaudio-mixer-applet
    pavucontrol
    paprefs

---

One of the problems of PulseAudio is that it pretty much becomes the default as
soon as you install it:
  - The client library will start the server if it's not running.
  - pulseaudio will install .desktop files that autostart the server together
    with Gnome or KDE.

Splitting libpulse would prevent that, but I believe we still need to test
on a per-application basis whether we can enable PulseAudio support (with a
dependency on libpulse) without breaking fallback to ALSA on systems without
pulseaudio.

Some packages (like sdl and openal) look for libpulse dynamically and will
still work even though the lib is missing, so they only need an optional
dependency.

I would be maintaining split -pulse packages where needed. A scientist explains an approaching milestone marking the arrival of quantum computers
1
Nov 20, 2023
1
Physics Quantum Physics
 Editors' notes
A scientist explains an approaching milestone marking the arrival of quantum computers
by Daniel Lidar , The Conversation

quantum computer
Credit: Pixabay/CC0 Public Domain

Quantum advantage is the milestone the field of quantum computing is fervently working toward, where a quantum computer can solve problems that are beyond the reach of the most powerful non-quantum, or classical, computers.

Quantum refers to the scale of atoms and molecules where the laws of physics as we experience them break down and a different, counterintuitive set of laws apply. Quantum computers take advantage of these strange behaviors to solve problems.

There are some types of problems that are impractical for classical computers to solve, such as cracking state-of-the-art encryption algorithms. Research in recent decades has shown that quantum computers have the potential to solve some of these problems. If a quantum computer can be built that actually does solve one of these problems, it will have demonstrated quantum advantage.

I am a physicist who studies quantum information processing and the control of quantum systems. I believe that this frontier of scientific and technological innovation not only promises groundbreaking advances in computation but also represents a broader surge in quantum technology, including significant advancements in quantum cryptography and quantum sensing.

The source of quantum computing's power
Central to quantum computing is the quantum bit, or qubit. Unlike classical bits, which can only be in states of 0 or 1, a qubit can be in any state that is some combination of 0 and 1. This state of neither just 1 or just 0 is known as a quantum superposition. With every additional qubit, the number of states that can be represented by the qubits doubles.

This property is often mistaken for the source of the power of quantum computing. Instead, it comes down to an intricate interplay of superposition, interference and entanglement.

Interference involves manipulating qubits so that their states combine constructively during computations to amplify correct solutions and destructively to suppress the wrong answers. Constructive interference is what happens when the peaks of two waves—like sound waves or ocean waves—combine to create a higher peak. Destructive interference is what happens when a wave peak and a wave trough combine and cancel each other out. Quantum algorithms, which are few and difficult to devise, set up a sequence of interference patterns that yield the correct answer to a problem.

Entanglement establishes a uniquely quantum correlation between qubits: The state of one cannot be described independently of the others, no matter how far apart the qubits are. This is what Albert Einstein famously dismissed as "spooky action at a distance." Entanglement's collective behavior, orchestrated through a quantum computer, enables computational speed-ups that are beyond the reach of classical computers.

Applications of quantum computing
Quantum computing has a range of potential uses where it can outperform classical computers. In cryptography, quantum computers pose both an opportunity and a challenge. Most famously, they have the potential to decipher current encryption algorithms, such as the widely used RSA scheme.

One consequence of this is that today's encryption protocols need to be reengineered to be resistant to future quantum attacks. This recognition has led to the burgeoning field of post-quantum cryptography. After a long process, the National Institute of Standards and Technology recently selected four quantum-resistant algorithms and has begun the process of readying them so that organizations around the world can use them in their encryption technology.


The ones and zeros – and everything in between – of quantum computing.

In addition, quantum computing can dramatically speed up quantum simulation: the ability to predict the outcome of experiments operating in the quantum realm. Famed physicist Richard Feynman envisioned this possibility more than 40 years ago. Quantum simulation offers the potential for considerable advancements in chemistry and materials science, aiding in areas such as the intricate modeling of molecular structures for drug discovery and enabling the discovery or creation of materials with novel properties.

Another use of quantum information technology is quantum sensing: detecting and measuring physical properties like electromagnetic energy, gravity, pressure and temperature with greater sensitivity and precision than non-quantum instruments. Quantum sensing has myriad applications in fields such as environmental monitoring, geological exploration, medical imaging and surveillance.

Initiatives such as the development of a quantum internet that interconnects quantum computers are crucial steps toward bridging the quantum and classical computing worlds. This network could be secured using quantum cryptographic protocols such as quantum key distribution, which enables ultra-secure communication channels that are protected against computational attacks—including those using quantum computers.

Despite a growing application suite for quantum computing, developing new algorithms that make full use of the quantum advantage—in particular in machine learning—remains a critical area of ongoing research.

Staying coherent and overcoming errors
The quantum computing field faces significant hurdles in hardware and software development. Quantum computers are highly sensitive to any unintentional interactions with their environments. This leads to the phenomenon of decoherence, where qubits rapidly degrade to the 0 or 1 states of classical bits.

Building large-scale quantum computing systems capable of delivering on the promise of quantum speed-ups requires overcoming decoherence. The key is developing effective methods of suppressing and correcting quantum errors, an area my own research is focused on.

In navigating these challenges, numerous quantum hardware and software startups have emerged alongside well-established technology industry players like Google and IBM. This industry interest, combined with significant investment from governments worldwide, underscores a collective recognition of quantum technology's transformative potential. These initiatives foster a rich ecosystem where academia and industry collaborate, accelerating progress in the field.

Quantum advantage coming into view
Quantum computing may one day be as disruptive as the arrival of generative AI. Currently, the development of quantum computing technology is at a crucial juncture. On the one hand, the field has already shown early signs of having achieved a narrowly specialized quantum advantage. Researchers at Google and later a team of researchers in China demonstrated quantum advantage for generating a list of random numbers with certain properties. My research team demonstrated a quantum speed-up for a random number guessing game.

On the other hand, there is a tangible risk of entering a "quantum winter," a period of reduced investment if practical results fail to materialize in the near term.

While the technology industry is working to deliver quantum advantage in products and services in the near term, academic research remains focused on investigating the fundamental principles underpinning this new science and technology. This ongoing basic research, fueled by enthusiastic cadres of new and bright students of the type I encounter almost every day, ensures that the field will continue to progress.


Provided by The Conversation 

This article is republished from The Conversation under a Creative Commons license. Read the original article.The Conversation

+ Explore further
Can cloud-based quantum computing really offer a quantum advantage?
41 shares
 Feedback to editors
Related
Recommended

Can cloud-based quantum computing really offer a quantum advantage?
Sep 22, 2023

Researchers provide comprehensive review of quantum teleportation
Jun 13, 2023

The best of both worlds: Combining classical and quantum systems to meet supercomputing demands
Aug 12, 2021

Can quantum computing protect AI from cyber attacks?
May 26, 2023

Two qudits fully entangled
Apr 20, 2023

IBM says it's reached milestone in quantum computing
Nov 10, 2017
Comments (1)
Sign in or create Science X account to leave the comment.

Homer10
2 hours ago
0
Computer: I'm sorry the password you typed in does not meet out complexity requirements. You need at least the following:
5243 lower case characters
32914 spaces or non printable characters
235412 upper case characters
1243 punctuation marks
32 Bitcoin ID numbers
1 Snake Eyes
and 35 Queen of hearts
Please re enter a new password?

Quoteetcryptoking1@outlook.com3@33#333O3r33p333h3e33u333s3a33n333g3e33l333s3README.md20238:10 am631381160.indexlogs

---
## [DarkoniusXNG/oaa](https://github.com/DarkoniusXNG/oaa)@[02f62cdf9a...](https://github.com/DarkoniusXNG/oaa/commit/02f62cdf9ae36672a29f88d5942e973f7bda3e50)
#### Thursday 2023-11-30 04:44:26 by Darko V

OAA balance + 7.34e (#3581)

ITEMS:
Arcane Crystal (tier 5 neutral item) bonus spell amp increased from 15% to 20%.
Arcane Crystal now also provides 20% debuff duration (like Timeless Relic).
Arcane Crystal: Fixed cast time reduction not working properly with Quick Spellcasting and Speedster modifiers.
Dispel Orb active is now activating self dispel instantly instead of after 0.2 seconds.
Disperser Manabreak mana burn on illusions increased from 8/16/24/32/40 to 8/18/28/38/48.
Disperser Manabreak mana burn on the real hero reduced from 40/60/90/130/180 to 40/50/70/100/140.
Disperser bonus damage increased from 40/50/65/85/110 to 40/50/70/100/140.
Enrage Crystal active debuff immunity now also removes Slark Pounce Leash and Invoker Deafening Blast Disarm like most other debuff immunity sources.
Enrage Crystal bonus damage reduced from 60/90/130 to 54/84/124. (same as BKB)
Enrage Crystal bonus status resistance reduced from 22/24/26% to 20/22/24%.
Greater Phase Boots active bonus attack range (for the procced attack when the wearer is a ranged hero) reduced from 150/175/200/225/250 to 150/160/170/180/190.
Linken's Sphere bonus damage increased from 10/20/35/55/80 to 10/20/40/70/110.
Reduction Orb active heal can no longer be reduced, increased or prevented.
Reduction Orb active heal per damage taken is now based on damage before reductions.
Reduction Orb active heal per damage taken reduced from 75% to 25%.
Reduction Orb active mana cost increased from 100 to 200.
Reduction Orb: Fixed Reduction Orb active heal being reduced with negative damage.
Regen Crystal active max health percent as heal reduced from 10% to 7%.
Revenant's Brooch Phantom Province magic resistance reduction duration increased from 3 to 4 seconds.
Revenant's Brooch Phantom Province magic resistance reduction rescaled from 20% to 17/18/19/20/21%
Revenant's Brooch Phantom Province max number of attacks rescaled from 6 to 5/6/7/8/9.
Shiva's Guard 4 can no longer be upgraded into Martyr's Mail.
Sonic Mask active now also provides 25/30% cast time reduction (cast speed).
Sonic Mask active now has 50 mana cost.
Spiked Mail 3 can no longer be upgraded into Stoneskin Armor 1.
Stoneskin Armor Stone Form deflected ranged attack damage is no longer lethal. (to prevent accidental denies)
Stoneskin Armor Stone Form deflected ranged attack damage is now blocked by Debuff Immunity and cannot be returned with Blade Mail, Spiked Mail etc.
Stoneskin Armor Stone Form deflected ranged attacks are now slower by 33%.
Stoneskin Armor bonus status resistance reduced from 24/26% to 22/24%.
Vampire Fang active bonus damage during the night reduced from 110/160 to 100/150.
Vampire Fang bonus attack speed reduced from 40/50 to 30/40.
Vampire Fang bonus status resistance reduced from 24/26% to 22/24%.

HEROES:
Ancient Apparition Ice Vortex dps rescaled from 20/28/36/44/60/108 to 18/24/30/36/72/108.
Anti-Mage Counterspell magic resistance rescaled from 10/20/30/40/50/60% to 15/25/35/45/50/55%.
Bane Brain Sap damage reduced from 100/200/300/400/800/1200 to 90/160/230/300/600/900.
Bane Level 15 Talent +15 Enfeeble Damage per second increased to +25.
Bane Level 25 Talent +300 Brain Sap Damage/Heal increased to +400.
Batrider Firefly cooldown reduced from 34 to 30 seconds.
Batrider Flamebreak cooldown reduced from 22/19/16/13/13/13 to 16/15/14/13/12/11 seconds.
Batrider Flamebreak dps increased at OAA levels from 60/80 to 80/120.
Batrider Flamebreak impact damage increased at OAA levels from 150/200 to 200/400.
Batrider Flaming Lasso total damage increased from 100/250/400/700/1300 to 100/300/500/900/1700.
Batrider STR gain increased from 2.2 to 2.9 per level.
Batrider Sticky Napalm damage against bosses increased from 50% to 150%.
Batrider Sticky Napalm mana cost reduced at OAA levels from 50/70 to 45/50.
Beastmaster Call of the Wild Hawk cooldown reduced at early levels from 36/34/32/30 to 33/32/31/30 seconds.
Beastmaster Call of the Wild Hawk damage increased from 60/90/120/150/300/600 to 90/120/150/180/360/720.
Bounty Hunter Shuriken Toss move speed slow increased from 20/30/40/50/60/70% to 25/35/45/55/65/75%.
Brewmaster Cinder Brew total damage increased at max level from 960 to 1280.
Brewmaster Drunken Brawler earth stance magic resistance reduced at OAA levels from 22/24% to 21/22%.
Brewmaster Drunken Brawler storm stance evasion rescaled from 10/15/20/25/30/33% to 15/20/25/30/30/30%.
Brewmaster Drunken Brawler void stance status resistance reduced at OAA levels from 25/30% to 21/22%.
Brewmaster's Fire Brewling Permanent Immolation damage radius increased from 220 to 400.
Broodmother Insatiable Hunger bonus base damage increased at max level from 110% to 120%.
Broodmother Silken Bola move speed slow increased at early levels from 10/25/40/55% to 25/35/45/55%.
Centaur Warrunner Stampede strength damage increased at max level from 5x to 6x.
Chaos Knight Phantasm mana cost increased from 75/125/175/225/275 to 100/150/200/250/300.
Chen Divine Favor damage increased from 90/160/230/300/600/1200 to 100/175/250/325/650/1300.
Chen Divine Favor physical damage shield rescaled from 100/180/240/320/640/1280 to 100/175/250/325/650/1300.
Chen Penitence cast range rescaled from 800 to 700/800/900/1000/1050/1100.
Crystal Maiden Arcane Aura bonus spell amplification rescaled from 5/6/7/8/10/12% to 4/5/6/7/9/12%.
Crystal Maiden Arcane Aura no longer provides 2/3/4/5/7/10% bonus magic resistance.
Crystal Maiden Arcane Aura now also provides 3/9/15/21/42/63 bonus intelligence.
Crystal Maiden Crystal Nova cooldown increased at early levels from 10/9.5/9/8.5 to 12/11/10/9 seconds.
Crystal Maiden Crystal Nova damage rescaled from 110/160/210/260/520/1040 to 100/175/250/325/650/1300.
Crystal Maiden Level 25 Talent +360 Crystal Nova damage reduced to +325.
Dark Willow Shadow Realm mana cost reduced at OAA levels from 200/300 to 110/120.
Dawnbreaker Celestial Hammer fire trail duration rescaled from 2.5 to 2.25/2.5/2.75/3/3.25/3.5 seconds.
Dawnbreaker Luminosity ally heal percent increased from 50/55/60/65/70/75% to 90%.
Dawnbreaker Luminosity heal penalty from creeps increased from 25% to 40%.
Dawnbreaker Solar Guardian landing damage increased from 130/190/250/500/750 to 150/225/300/525/900.
Dazzle Bad Juju cooldown reduction for items per cast reduced from 1/2/3/4/5 to 1/1.5/2/2.5/3 seconds.
Dragon Knight Elder Dragon Form cooldown increased from 70 to 80 seconds.
Dragon Knight Elder Dragon Form corrosive breath dps reduced from 25/45/65/125/125 to 25/30/35/70/70.
Dragon Knight Elder Dragon Form magic resistance reduced at max level from 40% to 30%.
Drow Ranger Level 20 Talent +25% Multishot Damage increased to +50%.
Drow Ranger Level 25 Talent +1 Multishot Waves increased to +2.
Drow Ranger Level 25 Talent +12% Marksmanship chance increased to +20%.
Drow Ranger Marskmanship proc chance reduced from 20/30/40/45/50% to 20/25/30/35/40%.
Drow Ranger Multishot cooldown reduced from 23/22/21/20/19/18 to 21/20/19/18/17/16 seconds.
Drow Ranger Multishot damage reduced at OAA levels from 200/260% to 180/200%.
Earthshaker Echo Slam cooldown reduced from 100 to 90 seconds.
Earthshaker Enchant Totem: Fixed scepter Enchant Totem having the wrong aftershock radius.
Earthshaker Fissure cooldown reduced at OAA levels from 15 to 14/13 seconds.
Faceless Void STR gain increased from 2.4 to 2.6 per level.
Faceless Void Time Lock cooldown reduced from 2 to 1.8 seconds.
Faceless Void Time Walk cast range increased at OAA levels from 825/850 to 850/900.
Grimstroke Ink Swell cooldown increased at OAA levels from 16/14 to 17/16 seconds.
Gyrocopter scepter side-gunner radius increased from 700 to 800.
Gyrocopter scepter side-gunner: Fixed Level 10 Talent improving side-gunner radius.
Huskar Inner Fire: Fixed Level 25 Talent improving the spell lifesteal by 400%.
Jakiro Dual Breath dps rescaled at OAA levels from 180/280 to 160/320.
Jakiro Level 15 Talent +325 Health changed to +30 Liquid Fire Damage.
Jakiro STR gain increased from 2.5 to 2.8 per level.
Jakiro base hp regen reduced from 5 to 0.25
Jakiro base strength increased from 25 to 26.
Legion Commander Overwhelming Odds shard bonus armor per hero increased at OAA levels from 7/8 to 8/12.
Lich Chain Frost bonus damage per jump increased at OAA levels from 35/50 to 40/55.
Lich Frost Shield cooldown reduced at early levels from 21/19/17/15 to 18/17/16/15 seconds.
Lich Sinister Gaze mana cost reduced at OAA levels from 160/240 to 90/100.
Lifestealer Feast damage reduced at max level from 2.2% to 2.1%.
Lifestealer Feast lifesteal reduced at OAA levels from 4/4.6% to 3.5/3.6%.
Lion Level 10 Talent +10% Mana Drain Slow increased to +15%.
Lion Level 20 Talent +20 Finger of Death damage per kill increased to +40.
Magnus AGI gain increased from 2 to 2.5 per level.
Magnus Empower mana cost reduced from 45/55/65/75/85/95 to 45/50/55/60/65/70.
Magnus Level 15 Talent +8 All Stats per hero hit with Reverse Polarity increased to +15.
Magnus Level 20 Talent +250 Shockwave Damage increased to +300.
Magnus Level 25 Talent +20% Empower Damage/Cleave increased to +30%.
Magnus Reverse Polarity damage increased at level 4 from 1050 to 1250.
Magnus STR gain increased from 3.1 to 3.5 per level.
Monkey King Wukong's Command scepter slow duration increased from 0.4 to 0.5 seconds.
Monkey King Wukong's Command soldier's chance to proc MK's attack increased from 25% to 40%.
Morphling Adaptive Strike (AGI) max agility multiplier increased at max level from 4.5x to 5x.
Morphling Adaptive Strike bonus agility and strength increased at OAA levels from 13/25 to 18/27.
Morphling Morph cooldown rescaled from 120/100/80/60/40 to 60 seconds at all levels.
Naga Siren Mirror Image cooldown reduced at early levels from 31/29/27/25 to 28/27/26/25 seconds.
Necrophos Death Pulse heal reduced from 55/110/165/220/440/660 to 55/80/105/130/260/520.
Necrophos Reaper's Scythe cooldown increased from 100/90/80/70/60 to 110/100/90/80/70 seconds.
Necrophos Reaper's Scythe damage per health reduced at OAA levels from 1.1/1.3 to 1.0/1.1
Nyx Assassin Vendetta bonus damage reduced at max level from 2300 to 1900.
Outworld Destroyer Sanity Eclipse base damage increased from 200/350/500/950/1400 to 200/400/600/1200/1800.
Phoenix Fire Spirits cooldown reduced from 28/26/23/20/20/20 to 23/22/21/20/19/18 seconds.
Phoenix STR gain increased from 3.3 to 3.6 per level.
Primal Beast Pulverize bonus damage per hit reduced from 30/70/110/230/350 to 20/60/100/220/340.
Primal Beast Pulverize cooldown increased from 28/26/24/22/20 to 36/34/32/30/28 seconds.
Pudge Dismember base damage per second reduced from 80/130/180/360/540 to 80/120/160/280/400.
Pudge Dismember cooldown reduced at early levels from 30/25/20 to 22/21/20 seconds.
Pudge Dismember strength damage per second increased at OAA levels from 1/1.1 to 1.2/1.5.
Pudge Flesh Heap damage block increased at level 5 from 38 to 44.
Pudge Rot scepter bonus damage rescaled from 90 to 75/80/85/90/95/100.
Pudge Rot scepter regen reduction rescaled from 20% to 5/10/15/20/25/30%.
QoP Blink shard damage reduced from 100/150/200/250/500/750 to 75/100/125/150/300/600.
QoP Level 20 Talent +220 Scream of Pain Damage reduced to +200.
QoP Scream of Pain damage increased at early levels from 75/150/225/300/600/1200 to 90/160/230/300/600/1200.
QoP Shadow Strike scepter bonus damage reduced from 75 to 60.
QoP Sonic Wave damage reduced at max level from 2600 to 2350.
Sniper Take Aim bonus attack range reduced at OAA levels from 490/580 to 450/500.
Sohei Dash: Fixed dash not working when leashed and having leash immunity (Debuff Immunity or Sonic Flight).
Sohei Dash: Fixed dash working when being affected by Tidehunter's Dead in the Water anchor.
Sohei Wholeness of Body now also removes Slark Pounce Leash and Invoker Deafening Blast Disarm like most other debuff immunity sources.
Spirit Breaker Charge of Darkness cooldown increased from 15/14/13/12/11/10 to 19/17/15/13/12/11 seconds.
Spirit Breaker Greater Bash cooldown increased from 2 to 2.3 seconds.
Sven Storm Hammer cooldown reduced at OAA levels from 12 to 11/10 seconds.
Sven Storm Hammer damage increased at max level from 960 to 1280.
Timbersaw Whirling Death stat loss percent for universal heroes increased from 5% to 7%.
Underlord Dark Rift damage increased from 250/450/650/1050/1850.
Underlord Dark Rift mana cost increased from 150/200/250/300/350 to 150/225/300/375/450.
Underlord Dark Rift radius rescaled from 375/400/425/450/475 to 430.
Underlord Dark Rift stun duration increased from 2.25/2.5/2.75/3.0/3.25 to 2.5/2.75/3.0/3.25/3.5 seconds.
Underlord Pit of Malice pit duration increased at early levels from 7/8/9/10 to 8.5/9/9.5/10 seconds.
Venomancer Noxious Plague impact damage increased from 150/300/450/750/1350 to 150/350/550/1150/1750.
Visage Familiars damage increased from 30/70/110/230/350 to 30/75/120/255/390.
Windranger Focus Fire bonus attack speed increased at OAA levels from 550/600 to 575/650.
Windranger Focus Fire cooldown reduced at early levels from 50/40/30 to 40/35/30 seconds.
Windranger STR gain increased from 2.0 to 2.6 per level.
Wraith King Reincarnation attack speed slow reduced at OAA levels from 150/225 to 75.
Wraith King Reincarnation scepter wraith form bonus attack speed reduced from 65/70/75/80/85 to 50.

---
## [DarkoniusXNG/oaa](https://github.com/DarkoniusXNG/oaa)@[d02b20945c...](https://github.com/DarkoniusXNG/oaa/commit/d02b20945cd1730d729bff675cb2a12a2ecb06c8)
#### Thursday 2023-11-30 04:44:26 by Darko V

Modifiers november 2023 (#3579)

* Chaos modifier: Modifiers that your hero didn't have before will now be prioritized when you random a modifier on respawn.
* Hyper Active modifier now provides only 5% cooldown reduction for all items.
* Hyper Active modifier now provides only 5% cooldown reduction for Dazzle Bad Juju, Earth Spirit Rolling Boulder and Faceless Void Time Walk.
* Hyper Lifesteal lifesteal and spell lifesteal against creeps reduced from 25% to 15%.
* Hyper Lifesteal: Fixed lifesteal and spell lifesteal getting amplified by healing amplification instead of lifesteal amplification and spell lifesteal amplification respectively.
* Octarine Soul cooldown reduction per point of Intelligence increased from 0.08% to 0.1%
* Octarine Soul modifier no longer stacks with Hyper Active and Pro-Active modifiers.
* Octarine Soul modifier no longer works for Dazzle Bad Juju.
* Octarine Soul modifier no longer works for items.
* Pro-Active modifier now provides only 10% cooldown reduction for Dazzle Bad Juju, Earth Spirit Rolling Boulder, Faceless Void Time Walk, Slark Shadow Dance, Terrorblade Sunder and Ursa Enrage.

---
## [danieloest/Red-Raider-Pharmarcy](https://github.com/danieloest/Red-Raider-Pharmarcy)@[fd9278625d...](https://github.com/danieloest/Red-Raider-Pharmarcy/commit/fd9278625df69950fe06aff85bfda825e5aac481)
#### Thursday 2023-11-30 04:44:53 by RandallKeur

GOT IT WORKING. F*** YEAH, now we get embedded insurance objects from patients!!!, god that was frustrating..... oh yeah, started implementing create patient, updated postman, yada yada

---
## [Quafadas/metals](https://github.com/Quafadas/metals)@[6fca4bc1b2...](https://github.com/Quafadas/metals/commit/6fca4bc1b27e11e955a366b6251a2e8ec73ff755)
#### Thursday 2023-11-30 04:52:45 by ckipp01

feat: capture and forward `diagnosticCode`

This relates to the grand plan of
https://github.com/lampepfl/dotty/issues/14904 and recently forwarding
the `diagnosticCode` has been merged in
https://github.com/lampepfl/dotty/pull/15565 and also backported so it
should show up in the 3.2.x series. While this pr isn't super exciting,
it's just making sure we capture the code and forward it, this should
unlock _much_ better ways to determine what code actions are available
for a given diagnostic. Meaning we don't have to do lovely things like
regex on the diagnostic message for Scala 3 diagnostics.

NOTE: that this does need some more changes in the build servers before
this is usable. So we can wait for those to be merged in if you'd like.

- [ ] sbt - https://github.com/sbt/sbt/pull/6998
- [ ] Bloop - https://github.com/scalacenter/bloop/pull/1750
- [ ] Mill - https://github.com/com-lihaoyi/mill/pull/1912

Now if you look at the trace file for a diagnostic you'll see the
addition of the code:

```
  "diagnostics": [
    {
      "range": {
        "start": {
          "line": 9,
          "character": 15
        },
        "end": {
          "line": 9,
          "character": 19
        }
      },
      "severity": 1,
      "code": "7",
      "source": "sbt",
      "message": "Found:    (\u001b[32m\"hi\"\u001b[0m : String)\nRequired: Int\n\nThe following import might make progress towards fixing the problem:\n\n  import sourcecode.Text.generate\n\n"
    }
  ],
```

Refs: https://github.com/lampepfl/dotty/issues/14904

---
## [naraghavan/systemd](https://github.com/naraghavan/systemd)@[1761066b13...](https://github.com/naraghavan/systemd/commit/1761066b135f1a322c446f102343ea4aa61fe3ee)
#### Thursday 2023-11-30 05:14:12 by Lennart Poettering

storagetm: add new systemd-storagetm component

This implements a "storage target mode", similar to what MacOS provides
since a long time as "Target Disk Mode":

        https://en.wikipedia.org/wiki/Target_Disk_Mode

This implementation is relatively simple:

1. a new generic target "storage-target-mode.target" is added, which
   when booted into defines the target mode.

2. a small tool and service "systemd-storagetm.service" is added which
   exposes a specific device or all devices as NVMe-TCP devices over the
   network.  NVMe-TCP appears to be hot shit right now how to expose
   block devices over the network. And it's really simple to set up via
   configs, hence our code is relatively short and neat.

The idea is that systemd-storagetm.target can be extended sooner or
later, for example to expose block devices also as USB mass storage
devices and similar, in case the system has "dual mode" USB controller
that can also work as device, not just as host. (And people could also
plug in sharing as NBD, iSCSI, whatever they want.)

How to use this? Boot into your system with a kernel cmdline of
"rd.systemd.unit=storage-target-mode.target ip=link-local", and you'll see on
screen the precise "nvme connect" command line to make the relevant
block devices available locally on some other machine. This all requires
that the target mode stuff is included in the initrd of course. And the
system will the stay in the initrd forever.

Why bother? Primarily three use-cases:

1. Debug a broken system: with very few dependencies during boot get
   access to the raw block device of a broken machine.

2. Migrate from system to another system, by dd'ing the old to the new
   directly.

3. Installing an OS remotely on some device (for example via Thunderbolt
   networking)

(And there might be more, for example the ability to boot from a
laptop's disk on another system)

Limitations:

1. There's no authentication/encryption. Hence: use this on local links
   only.

2. NVMe target mode on Linux supports r/w operation only. Ideally, we'd
   have a read-only mode, for security reasons, and default to it.

Future love:

1. We should have another mode, where we simply expose the homed LUKS
   home dirs like that.

2. Some lightweight hookup with plymouth, to display a (shortened)
   version of the info we write to the console.

To test all this, just run:

    mkosi --kernel-command-line-extra="rd.systemd.unit=storage-target-mode.target" qemu

---
## [deep-soft/rust-ripgrep](https://github.com/deep-soft/rust-ripgrep)@[082245dadb...](https://github.com/deep-soft/rust-ripgrep/commit/082245dadb3854238e62b91aa95a46018cf16ef1)
#### Thursday 2023-11-30 05:50:59 by Andrew Gallant

cli: replace clap with lexopt and supporting code

ripgrep began it's life with docopt for argument parsing. Then it moved
to Clap and stayed there for a number of years. Clap has served ripgrep
well, and it probably could continue to serve ripgrep well, but I ended
up deciding to move off of it.

Why?

The first time I had the thought of moving off of Clap was during the
2->3->4 transition. I thought the 3.x and 4.x releases were great, but
for me, it ended up moving a little too quickly. Since the release of
4.x was telegraphed around when 3.x came out, I decided to just hold off
and wait to migrate to 4.x instead of doing a 3.x migration followed
shortly by another 4.x migration. Of course, I just never ended up doing
the migration at all. I never got around to it and there just wasn't a
compelling reason for me to upgrade. While I never investigated it, I
saw an upgrade as a non-trivial amount of work in part because I didn't
encapsulate the usage of Clap enough.

The above is just what got me started thinking about it. It wasn't
enough to get me to move off of it on its own. What ended up pushing me
over the edge was a combination of factors:

* As mentioned above, I didn't want to run on the migration treadmill.
This has proven to not be much of an issue, but at the time of the
2->3->4 releases, I didn't know how long Clap 4.x would be out before a
5.x would come out.
* The release of lexopt[1] caught my eye. IMO, that crate demonstrates
exactly how something new can arrive on the scene and just thoroughly
solve a problem minimalistically. It has the docs, the reasoning, the
simple API, the tests and good judgment. It gets all the weird corner
cases right that Clap also gets right (and is part of why I was
originally attracted to Clap).
* I have an overall desire to reduce the size of my dependency tree. In
part because a smaller dependency tree tends to correlate with better
compile times, but also in part because it reduces my reliance and trust
on others. It lets me be the "master" of ripgrep's destiny by reducing
the amount of behavior that is the result of someone else's decision
(whether good or bad).
* I perceived that Clap solves a more general problem than what I
actually need solved. Despite the vast number of flags that ripgrep has,
its requirements are actually pretty simple. We just need simple
switches and flags that support one value. No multi-value flags. No
sub-commands. And probably a lot of other functionality that Clap has
that makes it so flexible for so many different use cases. (I'm being
hand wavy on the last point.)

With all that said, perhaps most importantly, the future of ripgrep
possibly demands a more flexible CLI argument parser. In today's world,
I would really like, for example, flags like `--type` and `--type-not`
to be able to accumulate their repeated values into a single sequence
while respecting the order they appear on the CLI. For example, prior
to this migration, `rg regex-automata -Tlock -ttoml` would not return
results in `Cargo.lock` in this repository because the `-Tlock` always
took priority even though `-ttoml` appeared after it. But with this
migration, `-ttoml` now correctly overrides `-Tlock`. We would like to
do similar things for `-g/--glob` and `--iglob` and potentially even
now introduce a `-G/--glob-not` flag instead of requiring users to use
`!` to negate a glob. (Which I had done originally to work-around this
problem.) And some day, I'd like to add some kind of boolean matching to
ripgrep perhaps similar to how `git grep` does it. (Although I haven't
thought too carefully on a design yet.) In order to do that, I perceive
it would be difficult to implement correctly in Clap.

I believe that this last point is possible to implement correctly in
Clap 2.x, although it is awkward to do so. I have not looked closely
enough at the Clap 4.x API to know whether it's still possible there. In
any case, these were enough reasons to move off of Clap and own more of
the argument parsing process myself.

This did require a few things:

* I had to write my own logic for how arguments are combined into one
single state object. Of course, I wanted this. This was part of the
upside. But it's still code I didn't have to write for Clap.
* I had to write my own shell completion generator.
* I had to write my own `-h/--help` output generator.
* I also had to write my own man page generator. Well, I had to do this
with Clap 2.x too, although my understanding is that Clap 4.x supports
this. With that said, without having tried it, my guess is that I
probably wouldn't have liked the output it generated because I
ultimately had to write most of the roff by hand myself to get the man
page I wanted. (This also had the benefit of dropping the build
dependency on asciidoc/asciidoctor.)

While this is definitely a fair bit of extra work, it overall only cost
me a couple days. IMO, that's a good trade off given that this code is
unlikely to change again in any substantial way. And it should also
allow for more flexible semantics going forward.

Fixes #884, Fixes #1648, Fixes #1701, Fixes #1814, Fixes #1966

[1]: https://docs.rs/lexopt/0.3.0/lexopt/index.html

---
## [Offroaders123/Smart-Text-Editor](https://github.com/Offroaders123/Smart-Text-Editor)@[a7b53c1abb...](https://github.com/Offroaders123/Smart-Text-Editor/commit/a7b53c1abb93276344f56cbe353d4ab2a49f615c)
#### Thursday 2023-11-30 06:45:54 by Offroaders123

macOS Card Controls Removal

This was a really nice feature, and I'm glad I added it! It turned out really realistic, and it worked nicely too. But I want to experiment with STE's design a bit more, maybe simplify it a bit more, bring it back to it's roots, or just modernize it a little. And, maybe, just maybe, add a light mode too (oohh noooo). I tried doing that a little ways back, but that was a rework that I never brought forward. I'll go back to that to look for inspiration for it.

But yeah, I'm not removing this because I don't like it, or it didn't work good, but because I want to try new things again, and I don't want it to hinder my design decisions later on, since I want to have new layouts and styles, and I think this time around I want to try using the same designs for all platforms.

Here's to new adventures!

---
## [SUBIKSHA302/192224244-FODS](https://github.com/SUBIKSHA302/192224244-FODS)@[d776dd9b4a...](https://github.com/SUBIKSHA302/192224244-FODS/commit/d776dd9b4a7cace4740c15347b424ad2ee0a0018)
#### Thursday 2023-11-30 07:42:32 by SUBIKSHA302

Add files via upload

import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import matplotlib.pyplot as plt
try:
    nltk.data.find('corpora/stopwords.zip')
except LookupError:
    nltk.download('stopwords')
    nltk.download('punkt')
def load_dataset(file_path):
    df = pd.read_csv(file_path)
    return df
def preprocess_text(text):
    text = text.lower()
    text = ''.join([char for char in text if char.isalnum() or char.isspace()])
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word not in stop_words]
    return ' '.join(filtered_text)
def calculate_word_frequency(text):
    words = word_tokenize(text)
    word_freq = Counter(words)
    return word_freq
def display_top_words(word_freq, top_n):
    top_words = word_freq.most_common(top_n)
    print(f"\nTop {top_n} most frequent words and their frequencies:")
    for word, freq in top_words:
        print(f"{word}: {freq}")
def plot_word_frequency(word_freq, top_n):
    top_words = dict(word_freq.most_common(top_n))
    plt.figure(figsize=(10, 6))
    plt.bar(top_words.keys(), top_words.values(), color='skyblue')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title(f'Top {top_n} Most Frequent Words')
    plt.xticks(rotation=45, ha='right')
    plt.show()
if _name_ == "_main_":
    data = {'feedback': ["Great service! Will definitely come back.",
                         "The product was faulty. Very disappointed.",
                         "Amazing experience with friendly staff.",
                         "Poor customer service. Will not recommend.",
                         "Quick delivery and good quality product."]}
    df = pd.DataFrame(data)
    df.to_csv('data.csv', index=False)
    file_path = 'data.csv'
    df = load_dataset(file_path)
    df['cleaned_feedback'] = df['feedback'].apply(preprocess_text)
    all_text = ' '.join(df['cleaned_feedback'])
    word_freq = calculate_word_frequency(all_text)
    top_n = int(input("Enter the number of top words to display and plot: "))
    display_top_words(word_freq, top_n)
    plot_word_frequency(word_freq, top_n)

---
## [nctrnm/code](https://github.com/nctrnm/code)@[d84e8b13e4...](https://github.com/nctrnm/code/commit/d84e8b13e40120a122ed70c264feb9404068e654)
#### Thursday 2023-11-30 08:21:46 by Matthew McGilvery

Add files via upload

**Delve into the Sonic Labyrinth: My Latest EP, FLUX**

Prepare to be captivated by my latest EP, FLUX, a mesmerizing fusion of captivating melodies and pulsating rhythms. Embark on a sonic odyssey as each track unveils a unique sonic tapestry, transporting you to a realm of emotions, from the electrifying energy of "Surge" to the introspective tranquility of "Serenity."

**Immerse Yourself in FLUX:**

- Plunge into the aural experience: FLUX on flux.nctrnm.com

- Witness the visual spectacle: FLUXV on fluxv.nctrnm.com

- Enhance your FLUX journey with official merchandise: FLUX Merchandise on shop.nctrnm.com

FLUX transcends the boundaries of an EP, offering an immersive exploration of my artistry. Each track is meticulously crafted to evoke a distinct emotion, leaving you breathless and yearning for more.

**This is my personal invitation to experience the sonic journey of FLUX**

Signed-off-by: Matthew McGilvery <48932877+nctrnm@users.noreply.github.com>

---
## [postare/blade-mdi](https://github.com/postare/blade-mdi)@[0092d11287...](https://github.com/postare/blade-mdi/commit/0092d11287bf139bebe5dfe5bc6eef5e5b44015f)
#### Thursday 2023-11-30 08:41:50 by Helge Sverre

Update README.md

Remove double "composer require composer require", and remove "$" prefix in the publish command, as this is very very annoying when you double-click-to-select-entire-line on a code-block and now you have a damned $ in there breaking your flow, i could elaborate on my hatred for this practice, but this is a mere PR to fix an issue quickly in the middle of the night aifhwoiehng

---
## [AnywayFarus/Skyrat-tg](https://github.com/AnywayFarus/Skyrat-tg)@[fcbbb6e0e0...](https://github.com/AnywayFarus/Skyrat-tg/commit/fcbbb6e0e0f9c0132fbc962bb03464bdcd1b20c4)
#### Thursday 2023-11-30 08:44:40 by SkyratBot

[MIRROR] Fixes body collision causing a stun, despite a successful block. [MDB IGNORE] (#25146)

* Fixes body collision causing a stun, despite a successful block. (#79824)

## About The Pull Request

Puts a block check into the ``throw_impact()`` of carbon mobs.

## Why It's Good For The Game

I'm touching on a lot of 'get around shields' stuns, and this has been a
big one for the better part of a few years and potentially not even
intentional. I would say it gained its largest popularity when it became
weaponized with fireman carrying.

Despite seemingly rolling to block, blocking a body hitting you doesn't
actually do anything at all. This reminds me a bit of energy bolas. So I
fixed it? I think, there might be a better fix, I'm just replicating
code present in xenomorph tackles. This shit sucks, please recommend a
better fix if you know it.

## Changelog
:cl:
fix: When you successfully block a body collision, it does something
rather than nothing at all.
/:cl:

* Fixes body collision causing a stun, despite a successful block.

---------

Co-authored-by: necromanceranne <40847847+necromanceranne@users.noreply.github.com>

---
## [lifning/omicron](https://github.com/lifning/omicron)@[2fc0dfd8c1...](https://github.com/lifning/omicron/commit/2fc0dfd8c11f31e66cfaf8ee80586bb2ed607216)
#### Thursday 2023-11-30 08:56:45 by Andrew J. Stone

Extract storage manager related code from sled-agent (#4332)

This is a large PR. The changes are in many ways *just* moving code
around,
and at a cursory glance may appear to be a giant waste of time. To
justify
these changes and my rationale I will first present the goals I believe
we
should strive to meet in general sled-agent development. I'll then go
into
how I believe these goals can be realized via code patterns. I'll then
discuss
the concrete changes in this PR and how they implement the discussed
patterns.
Lastly, I'll list a few open questions about the implementation in the
PR.

I want to emphasize that a lot of what I talk about below is already
done in
sled-agent, at least part way. We can pick the best patterns already in
use and
standardize on them to build a more coherent and yet decoupled
architecture for
easier testing and understanding.

# Goals

This PR is an attempt to start making sled-agent easier to maintain. In
order to
make things easier to maintain, I believe we should attempt to realize a
few key
goals:

1. Initial startup and control code should read linearly. You shouldn't
have to
jump around to follow the gist of what's going on.
2. Tasks, like functions, should live at a certain abstraction level. It
must be clear
 what state the task is managing and how it gets mutated.
3. A developer must be able to come into the codebase and know where a
given
functionality should live and be able to clearly follow existing
patterns such
that their new code doesn't break or cross abstractions that make
following the
code harder in the future.
4. Tests for individual abstractions and task driven code should be easy
to
write. You shouldn't need to spin up the whole sled-agent in order to
test an
algorithm or behavior.
 5. Hardware should be abstracted out, and much of the code shouldn't 
 deal with hardware directly.

# Patterns

## Task/Handle

In my opinion, the most important pattern to follow for async rust
software
is what I call the "task/handle" pattern. This pattern helps code
maintenance
by explicitly managing state and making task driven code easier to test.
All
tasks that provide services to other tasks should follow this pattern.
In this
pattern, all state is contained in a type owned by the task and
inaccessible
directly to other tasks. The task has a corresponding handle which must
be
`Send` and `Clone`, and can be used to make requests of the task. The
handle
interacts with the task solely via message passing. Mutexes are never
used.

A few things fall directly out of this pattern:

* Code that manipulates state inside and outside the task can be
synchronous
* We don't have to worry about mutex behavior with regards to
cancellation,
   await points, etc...
 * Testing becomes easier:
   * We can test a bunch of the code without spawning a task in many
cases. We just [directly construct the state object and call
functions](https://github.com/oxidecomputer/omicron/pull/4332/files#diff-08315639e20a9323f2740455a7813d83ca43b05dca197ebbda66c13f750d446bR634-R656),
     whether sync or async.
   * When testing sequential operations that are fire and forget,
we [know when they have been processed by the task
loop](https://github.com/oxidecomputer/omicron/pull/4332/files#diff-08315639e20a9323f2740455a7813d83ca43b05dca197ebbda66c13f750d446bR702-R709),
     because our next request will only run after those operations. 
This is a direct result of the fifo channel between handle and task.
This is not possible with state shared outside the task via a mutex.
     We must poll that mutex protected state until it either changes to
     the value we expect or we get a timeout. If we expect no change, we
     must use a side-channel.
   * We can write complex state handling algorithms, such as those in 
      maghemite or bootstore, in a deterministic, synchronous style that
allows property based testing and model checking in as straightforward
     a manner as possible.
* We can completely [fake the
task](https://github.com/oxidecomputer/omicron/pull/4332/files#diff-08315639e20a9323f2740455a7813d83ca43b05dca197ebbda66c13f750d446bR163-R223)
without changing any of the calling code except the constructor. The
real
handle can instead send messages to a fake task. Importantly, this
strategy
can also be used to abstract out hardware for unit tests and simulation.

Beyond all that though, the understanding of how state is mutated and
accessed
is clear. State is only mutated inside the task, and can only be
retrieved from
code that has a copy of the handle. There is no need for separate
`_locked`
methods, and no need to worry about order of locking for different bits
of task
state. This can make the task code itself much shorter and easier to
read as
demonstrated by the new `StorageManager` code in `sled_storage`. We can
also
maintain internal stats for the task, and all of this can be retrieved
from the
handle for reporting in `omdb`.

There is one common question/problem with this pattern. How do you
choose a
bounded channel size for handle to task messages?

This can be tricky, but in general, you want the channel to *act*
unbounded,
such that sends never fail. This makes the channels reliable, such that
we never
drop messages inside the process, and the caller doesn't have to choose
what to
do when overloaded. This simplifies things drastically for developers.
However,
you also don't want to make the channel actually unbounded, because that
can
lead to run-away memory growth and pathological behaviors, such that
requests
get slower over time until the system crashes.

After discussions with @jgallagher and reflections from @sunshowers and
@davepacheco on RFD 400, the solution is to choose a large enough bound
such that we should never hit it in practice unless we are truly
overloaded.
If we hit the bound it means that beyond that requests will start to
build
up and we will eventually topple over. So when we hit this bound, we
just
[go ahead and
panic](https://github.com/oxidecomputer/omicron/pull/4332/files#diff-08315639e20a9323f2740455a7813d83ca43b05dca197ebbda66c13f750d446bR75-R77).

Picking a channel bound is hard to do empirically, but practically, if
requests are
mostly mutating task local state, a bound of 1024 or even 8192 should be
plenty.
Tasks that must perform longer running ops can spawn helper tasks as
necessary
or include their own handles for replies rather than synchronously
waiting. Memory
for the queue can be kept small with boxing of large messages.

It should also be noted that mutexes also have queues that can build up
and
cause pathological slowness. The difference is that these queues are
implicit
and hard to track.

## Isolate subsystems via the message driven decoupling

We have a bunch of managers (`HardwareManager`, `StorageManager`,
`ServiceManager`, `InstanceManager`) that interact with each other to
provide sled-agent services. However, much of that interaction is ad-
hoc with state shared between tasks via an `Inner` struct protected
by a mutex. It's hard to isolate each of these managers and test
them independently. By ensuring their API is well defined via a
`Handle`,
we can fake out different managers as needed for independent testing.
However, we can go even farther, without the need for dependency
injection
by having different managers announce their updates via [broadcast or
watch

channels](https://github.com/oxidecomputer/omicron/pull/4332/files#diff-08315639e20a9323f2740455a7813d83ca43b05dca197ebbda66c13f750d446bR129-R133).

With this strategy, we can drive tests for a task by using the handle to
both
trigger operations, and then wait for the outflow of messages that
should occur
rather than mocking out the handle API of another task directly and
checking
the interaction via the fake. This is especially useful for lower level
services
that others depend upon such as `StorageManager`, and we should do this
when we
can, rather than having tasks talk directly to each other. This strategy
leads
directly to the last pattern I really want to mention, the `monitor`
pattern.

## High level interaction via monitors

Remember that a primary goal of these patterns is to make the sled-agent
easier
to read and discover what is happening at any given point in time. This
has to
happen with the inherent concurrency of all the separate behaviors
occurring
in the sled-agent such as monitoring for hardware and faults, or
handling user
requests from Nexus. If our low level managers announce updates via
channels
we can have high level `Monitors` that wait for those updates and then
dispatch
them to other subsystems or across clients to other sleds or services.
This
helps further decouple services for easier testing, and also allows us
to
understand all the asynchrony in the system in fewer spots. We can put
RAS code
in these monitors and use them as central points to maintain stats and
track the
overall load on the system.

# The punchline

How do the patterns above satisfy the goals? By decoupling tasks and
interacting
solely via message passing we make testing easier(goal 4). By separating
out
managers/ services into separate tasks and maintaining state locally we
satisfy
goals 2 and 5. By making the tasks clear in their responsibilities, and
their
APIs evident via their handles, we help satisfy goal 3. Goal 3 is also
satisfied
to a degree by the elimination of sharing state and the decoupling via
monitors.
Lastly, by combining all the patterns, we can spawn all our top level
tasks and
monitors in one place after initializing any global state. This allows
the code
to flow linearly.

Importantly, it's also easy to violate goal 3 by dropping some mutexes
into the
middle of a task and oversharing handles between subsystems. I believe
we can
prevent this, and also make testing and APIs clearer, by separating
subsystems
into their own rust packages and then adding monitors for them in the
sled-agent.
I took a first cut at this with the `StorageManager`, as that was the
subsystem I was
most familiar with.

# Concrete Code changes

Keeping in line with my stated goals and patterns, I abstracted the
storage
manager code into its own package called `sled-storage`. The
`StorageManager`
uses the `task/handle` pattern, and there is a monitor for it in
sled-agent
that takes notifications and updates nexus and the zone bundler. There
are also a
bunch of unit tests where none existed before. The bulk of the rest of
the code
changes fell out of this. In particular, now that we have a separate
`sled-storage`
package, all high level disk management code lives there. Construction
and
formatting of partitions still happens in `sled-hardware`, but anything
above the
zpool level occurs in `sled-storage`. This allows testing of real
storage code on
any illumos based system using file backed zpools. Importantly, the
key-management
code now lives at this abstraction level, rather than in
`sled-hardware`, which
makes more sense since encryption only operates on datasets in ZFS.

I'd like to do similar things to the other managers, and think that's a
good way
to continue cleaning up sled-agent.

The other large change in this code base is simplifying the startup of
the bootstrap agent such that all tasks that run for the lifetime of
the sled-agent process are spawned in `long_running_tasks`. There is a
struct called `LongRunningTaskHandles` that allows interaction with all
the
"managers" spawned here. This change also has the side effect of
removing the
`wait_while_handling_hardware_updates` concurrent future code, since we
have
a hardware monitor now running at the beginning of time and can never
miss
updates. This also has the effect of negating the need to start a
separate
hardware manager when the sled-agent starts up. Because we now know
which
tasks are long running, we don't have to save their tokio `JoinHandle`s
to display
ownership and thus gain clonability.

# Open Questions

* I'm not really a fan of the name `long_running_task_handles`. Is there
a better
name for these?
* Instead of calling `spawn_all_longrunning_tasks` should we just call
the
individual spawn functions directly in `bootstrap/pre_server`? Doing it
this
way would allow the `ServiceManager` to also live in the long running
handles
and remove some ordering issues. For instance, we wait for the bootdisk
inside
`spawn_all_longrunning_tasks` and we also upsert synthetic disks.
Neither
of these is really part of spawning tasks.

---
## [Aoao54/temporal](https://github.com/Aoao54/temporal)@[1be76e3583...](https://github.com/Aoao54/temporal/commit/1be76e3583ef01ba9f79503e81fed5b7c9ab389c)
#### Thursday 2023-11-30 09:05:51 by Tim Deeb-Swihart

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
## [nxsaken/bevy](https://github.com/nxsaken/bevy)@[ab300d0ed9...](https://github.com/nxsaken/bevy/commit/ab300d0ed9990972679629af3ef18fd37c0e106c)
#### Thursday 2023-11-30 09:11:59 by Connor King

Gizmo Arrows (#10550)

## Objective

- Add an arrow gizmo as suggested by #9400 

## Solution

(excuse my Protomen music)


https://github.com/bevyengine/bevy/assets/14184826/192adf24-079f-4a4b-a17b-091e892974ec

Wasn't horribly hard when i remembered i can change coordinate systems
whenever I want. Gave them four tips (as suggested by @alice-i-cecile in
discord) instead of trying to decide what direction the tips should
point.

Made the tip length default to 1/10 of the arrow's length, which looked
good enough to me. Hard-coded the angle from the body to the tips to 45
degrees.

## Still TODO

- [x] actual doc comments
- [x] doctests
- [x] `ArrowBuilder.with_tip_length()`

---

## Changelog

- Added `gizmos.arrow()` and `gizmos.arrow_2d()`
- Added arrows to `2d_gizmos` and `3d_gizmos` examples

## Migration Guide

N/A

---------

Co-authored-by: Nicola Papale <nicopap@users.noreply.github.com>

---
## [ndn-bebop1337/bulk-yt-mp3](https://github.com/ndn-bebop1337/bulk-yt-mp3)@[ad5c9596bb...](https://github.com/ndn-bebop1337/bulk-yt-mp3/commit/ad5c9596bbf4230bce855a3d444b6f8c2bae79dd)
#### Thursday 2023-11-30 09:29:20 by Replit user

Improved user interface (with extra bullshit). Added threading capability. LETS GOOOO we're fucking speedrunning the entire lifespan of a piece of fooking software! C'mon next update <8hrs away MAX, version 3.0 by TOMORROW! #FuckSleep

---
## [Bird-Lounge/Naakas-Lounge](https://github.com/Bird-Lounge/Naakas-Lounge)@[bf869a0ded...](https://github.com/Bird-Lounge/Naakas-Lounge/commit/bf869a0ded3a3ca5e00500ef5ad856bcb7f012dd)
#### Thursday 2023-11-30 09:59:07 by Bloop

[MISSED MIRROR] Fixes runtime relating to hard TGS reboots (PROBABLY WON'T FIX REBOOT CRASHES) (#25185)

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

Co-authored-by: san7890 <the@san7890.com>

---
## [unit0016/effigy-se](https://github.com/unit0016/effigy-se)@[55c13819b2...](https://github.com/unit0016/effigy-se/commit/55c13819b2937775b4de8e4858db433abab353ca)
#### Thursday 2023-11-30 11:31:41 by DaydreamIQ

Touches up Moffuchi's pizzeria  (#79899)

## About The Pull Request
I've given the icebox pizzeria ruin a few small improvements:
- Firstly, The kitchen is actually stocked with tomatoes from the get
go. Along with a few mothic themed ingredients for those signature
mothic pizzas we all know and love (And hate for being such a pain to
make)
- The discarded air alarm frames have been replaced with working ones
(I'm unsure if this was intentional or not)
- Some drinking glasses have been added to the bar
- And finally a pacman has been placed in the backroom along with some
plasma to power the place
## Why It's Good For The Game
This place gets overlooked a lot because its completely powerless, and
doesn't actually give you enough from the get go to make even a basic
pizza besides the tomato seeds a lot of people are gonna miss. This
gives the ruin just a little more life to maybe be worth trekking out
for. And having mothic themed ingredients in the **MOFFIC** Pizzeria
just makes sense even if they are a bitch to make.

Not sure if this counts as a balance change or a QOL so feel free to
yell at me if I've labelled this wrong, I have been advised that this
SHOULD be the latter at least.
## Changelog
:cl:
qol: Mothuchi's pizzeria has been improved slightly! Order yourself a
fresh mothic pizza today!
/:cl:

---
## [KDEFFALT/Sea_Kernel-Fog](https://github.com/KDEFFALT/Sea_Kernel-Fog)@[54459e6bbb...](https://github.com/KDEFFALT/Sea_Kernel-Fog/commit/54459e6bbbd0473ee22e0f6484ce624f63d4f157)
#### Thursday 2023-11-30 12:16:01 by Angelo G. Del Regno

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

---
## [iiYese/bevy](https://github.com/iiYese/bevy)@[3ee9edf280...](https://github.com/iiYese/bevy/commit/3ee9edf280c530f35a51049ec92fcfa552998614)
#### Thursday 2023-11-30 12:56:34 by Ethereumdegen

add try_insert to entity commands (#9844)

# Objective

- I spoke with some users in the ECS channel of bevy discord today and
they suggested that I implement a fallible form of .insert for
components.

- In my opinion, it would be nice to have a fallible .insert like
.try_insert (or to just make insert be fallible!) because it was causing
a lot of panics in my game. In my game, I am spawning terrain chunks and
despawning them in the Update loop. However, this was causing bevy_xpbd
to panic because it was trying to .insert some physics components on my
chunks and a race condition meant that its check to see if the entity
exists would pass but then the next execution step it would not exist
and would do an .insert and then panic. This means that there is no way
to avoid a panic with conditionals.

Luckily, bevy_xpbd does not care about inserting these components if the
entity is being deleted and so if there were a .try_insert, like this PR
provides it could use that instead in order to NOT panic.

( My interim solution for my own game has been to run the entity despawn
events in the Last schedule but really this is just a hack and I should
not be expected to manage the scheduling of despawns like this - it
should just be easy and simple. IF it just so happened that bevy_xpbd
ran .inserts in the Last schedule also, this would be an untenable soln
overall )

## Solution

- Describe the solution used to achieve the objective above.

Add a new command named TryInsert (entitycommands.try_insert) which
functions exactly like .insert except if the entity does not exist it
will not panic. Instead, it will log to info. This way, crates that are
attaching components in ways which they do not mind that the entity no
longer exists can just use try_insert instead of insert.

---

## Changelog

 

## Additional Thoughts

In my opinion, NOT panicing should really be the default and having an
.insert that does panic should be the odd edgecase but removing the
panic! from .insert seems a bit above my paygrade -- although i would
love to see it. My other thought is it would be good for .insert to
return an Option AND not panic but it seems it uses an event bus right
now so that seems to be impossible w the current architecture.

---
## [MDevereau/llvm-project](https://github.com/MDevereau/llvm-project)@[5cd24759c4...](https://github.com/MDevereau/llvm-project/commit/5cd24759c41864215e67c280234b6c745a4cd369)
#### Thursday 2023-11-30 13:15:00 by Louis Dionne

[libc++] Reduce the compilation time required by SIMD tests (#72602)

Testing all the SIMD widths exhaustively is nice in theory, however in
practice it leads to extremely slow tests. Given that
1. our testing resources are finite and actually pretty costly
2. we have thousands of other tests we also need to run
3. the value of executing these SIMD tests for absolutely all supported
SIMD widths is fairly small compared to cherry-picking a few relevant
widths

I think it makes a lot of sense to reduce the exhaustiveness of these
tests. I'm getting a ~4x speedup for the worst offender
(reference_assignment.pass.cpp) after this patch.

I'd also like to make this a reminder to anyone seeing this PR that
tests impact everyone's productivity. Slow unit tests contribute to
making the CI slower as a whole, and that has a direct impact on
everyone's ability to iterate quickly during PRs. Even though we have a
pretty robust CI setup in place, we should remember that it doesn't come
for free and should strive to keep our tests at a good bang for the buck
ratio.

---
## [alejandrojericho/app-dev](https://github.com/alejandrojericho/app-dev)@[a26a0b9f95...](https://github.com/alejandrojericho/app-dev/commit/a26a0b9f958cb79290808804adf629e08742d779)
#### Thursday 2023-11-30 14:32:51 by alejandrojericho

Update README.md

A Space Odyssey - "2001: A Space Odyssey" is a groundbreaking science fiction film directed by Stanley Kubrick. Released in 1968, it is known for its stunning visuals and philosophical themes.

Citizen Kane - Directed by Orson Welles and released in 1941, "Citizen Kane" is often regarded as one of the greatest films in the history of cinema. It revolutionized filmmaking with its innovative techniques.

La Dolce Vita - Directed by Federico Fellini and released in 1960, "La Dolce Vita" is an Italian film that explores the decadence and hedonism of Roman high society.

In the Mood for Love - A Hong Kong romantic drama film directed by Wong Kar-wai, released in 2000. It is praised for its lush cinematography and emotionally resonant storytelling.

There Will Be Blood - Directed by Paul Thomas Anderson and released in 2007, this film is a powerful drama starring Daniel Day-Lewis. It explores the ruthless world of early 20th-century oil prospecting.

Singin' in the Rain - A classic musical comedy released in 1952, directed by Stanley Donen and Gene Kelly. It celebrates the transition from silent films to "talkies."

GoodFellas - Directed by Martin Scorsese and released in 1990, this crime film is based on the true story of Henry Hill's life in the mob. It is widely regarded as one of the greatest films in the gangster genre.

North by Northwest - A classic Hitchcock thriller released in 1959, starring Cary Grant and Eva Marie Saint. It's known for its iconic scenes, including the famous crop duster sequence.

The Office - This refers to the American version of "The Office," a mockumentary sitcom that ran from 2005 to 2013. It was created by Greg Daniels and became widely popular for its unique format and humor.

---
## [Laus4Deus/f13babylon](https://github.com/Laus4Deus/f13babylon)@[9bc0add065...](https://github.com/Laus4Deus/f13babylon/commit/9bc0add065315cba3de80a2cc1feac5fe08e9fed)
#### Thursday 2023-11-30 14:47:40 by Stutternov

Locks Legion Combat Roles to Male Only (+ Other Legion Changes) (#176)

## About The Pull Request

Does the following:
- Locks all combat roles to male only - like they used to be prior to
Sunset changes.
- Locks Priestess of Mars to females only, as is in lore.
- Unlocks servant loadout on slave from being female only (real subtle
there guys)

Tl;dr - Females are relegated to slave, camp follower, auxilla,
forgemaster, or priestess. Males are able to be any role baring
priestess.

This is basically already 'rule enforced' so should just be re-added
code wise anyway.

## Why It's Good For The Game

Fits Fallout lore, the servers lore, and keeps the Legion's faction
design at least faithful to their purpose. (Hate telling people this but
- maybe........ legion aren't good people........)

## Pre-Merge Checklist
<!-- Don't bother filling these in while creating your Pull Request,
just click the checkboxes after the Pull Request is opened and you are
redirected to the page. -->
- [ ] You tested this on a local server.
- [ ] This code did not runtime during testing.
- [ ] You documented all of your changes.
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
adds: Locks roles in Legion based off gender restrictions.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Laus4Deus/f13babylon](https://github.com/Laus4Deus/f13babylon)@[830db814f3...](https://github.com/Laus4Deus/f13babylon/commit/830db814f3104bfe595db02eea0759766eb2cd10)
#### Thursday 2023-11-30 14:47:40 by GreytidePanda

Expanded Mall (#171)

## About The Pull Request
The northwest mall was an area scraped together from an older mall
building and expanded on by me well over a year ago, but it was always
unfinished as I left Sunset before I submitted the final version. You
can really tell this if you look at some of the suspiciously empty rooms
on the upper levels.

The finished version has been sitting on my harddrive for a long time so
I've copied it in and made a few changes to fit the server. I'm not sure
if the mall is staying with future map changes, but at least for now I
want to be judged on my completed work.

- References to 'Mall of Wyoming' are now 'Mall of Utah'
- A lot of rooms are now less claustrophobic and use their space better
- More loot and detail (no crazy loot - it was always intended as a
fairly beginner friendly zone)
- Now far more vertical - an underground parking lot, and accessible
roof
- Removed the 'requires_power' flag from the mall area tag - no other
ruin uses it
- Fixed the instrument shop shutter not working (I can't believe this
bug has existed for over a year)

## Why It's Good For The Game
Better locations are always good for the game!

## Pre-Merge Checklist
- [x] You tested this on a local server.
- [x] This code did not runtime during testing.
- [x] You documented all of your changes.


## Changelog
:cl:
add: The Mall of Utah now offers an even bigger shopping experience.
/:cl:

---
## [beetlejuicetr/PsychonautStation](https://github.com/beetlejuicetr/PsychonautStation)@[31afabc9af...](https://github.com/beetlejuicetr/PsychonautStation/commit/31afabc9afae2252fc22958d07f12f7148d6963d)
#### Thursday 2023-11-30 14:51:08 by Jacquerel

Adds missing default biotypes to some damage procs (#79102)

## About The Pull Request

I noticed by complete coincidence because I happened to glance at the
channel a bunch of people complaining about blobbernauts not taking any
damage when leaving the blob in manuel round end chat.
Did anyone report this bug, even after prompting? No. Not even the game
admin who was playing as the blob.

Makes you wonder how many other bugs people are perfectly willing to
spend 15 minutes posting "i fucking hate coders" about without actually
telling anyone they exist. Sucks to be them I guess.

Anyone the cause is that some of these procs didn't have a default
biotype, so they would never take the toxin damage they were being
assigned. Now they will.

## Changelog

:cl:
fix: Blobbernauts will once again take damage when not on blob tiles.
/:cl:

---
## [beetlejuicetr/PsychonautStation](https://github.com/beetlejuicetr/PsychonautStation)@[ece51a1a9d...](https://github.com/beetlejuicetr/PsychonautStation/commit/ece51a1a9d6896a54b878563d9c33002bc8f3688)
#### Thursday 2023-11-30 14:51:08 by nikothedude

[NO GBP] Fixes scream for me, and also fixes literally EVERY INSTANCE of non-random puncture wounds (#79043)

## About The Pull Request

Closes https://github.com/tgstation/tgstation/issues/79017

So turns out, I

1. Had a pair of inverted more/less than operators in a crucial area. I
DONT KNOW HOW THIS WORKED. SHIT is a FUCKING mystery.
2. Used a non-existant define which DM converted into a string because
Byond
## Why It's Good For The Game

bugsgs badagfd
## Changelog
:cl:
fix: Scream for me, the spell, now works
fix: Non-random puncture wounds can now be applied
/:cl:

---------

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [colinfrederickson/CF-Testing](https://github.com/colinfrederickson/CF-Testing)@[5074eec512...](https://github.com/colinfrederickson/CF-Testing/commit/5074eec5125f7b0384fcf3aa797aaaf7c6b5b045)
#### Thursday 2023-11-30 15:32:54 by colinfrederickson

Enhance snapshot creation process with detailed logging and progress updates

This commit introduces several enhancements to the snapshot creation process in the Flatfile integration, aimed at improving user experience and debugging:

1. **Detailed Logging**:
   - Implemented logging at the start of the snapshot creation job, providing clear visibility of the job ID and sheet ID being processed. This is particularly useful for tracking and debugging.
   - Added final status logs to clearly indicate the completion or failure of the job, enhancing the traceability of the process.

2. **Progress Updates**:
   - Introduced more granular progress updates throughout the snapshot creation process. Users are now informed at key stages, including the initiation of snapshot creation, fetching sheet details, retrieving snapshot label information, and during the actual snapshot creation.
   - Each progress update comes with a descriptive message, ensuring users are well-informed about the current stage of the process.

3. **Improved User Messaging**:
   - The completion message has been updated to include the name of the sheet for which the snapshot was created, providing a more contextually relevant message to the user. Additionally, the label is included in the message if provided by the user, further personalizing the user experience.

These enhancements are aimed at making the snapshot creation process more transparent and user-friendly, while also providing detailed logs that facilitate easier troubleshooting and monitoring.

---
## [MichaelMarcialis/kibana](https://github.com/MichaelMarcialis/kibana)@[cd909f03b1...](https://github.com/MichaelMarcialis/kibana/commit/cd909f03b1d71da93041a0b5c184243aa6506dea)
#### Thursday 2023-11-30 15:33:17 by Kyle Pollich

[Fleet] Fix inability to upgrade agents from 8.10.4 -> 8.11 (#170974)

## Summary

Closes https://github.com/elastic/kibana/issues/169825

This PR adds logic to Fleet's `/api/agents/available_versions` endpoint
that will ensure we periodically try to fetch from the live product
versions API at https://www.elastic.co/api/product_versions to make sure
we have eventual consistency in the list of available agent versions.

Currently, Kibana relies entirely on a static file generated at build
time from the above API. If the API isn't up-to-date with the latest
agent version (e.g. kibana completed its build before agent), then that
build of Kibana will never "see" the corresponding build of agent.

This API endpoint is cached for two hours to prevent overfetching from
this external API, and from constantly going out to disk to read from
the agent versions file.

## To do
- [x] Update unit tests
- [x] Consider airgapped environments

## On airgapped environments

In airgapped environments, we're going to try and fetch from the
`product_versions` API and that request is going to fail. What we've
seen happen in some environments is that these requests do not "fail
fast" and instead wait until a network timeout is reached.

I'd love to avoid that timeout case and somehow detect airgapped
environments and avoid calling this API at all. However, we don't have a
great deterministic way to know if someone is in an airgapped
environment. The best guess I think we can make is by checking whether
`xpack.fleet.registryUrl` is set to something other than
`https://epr.elastic.co`. Curious if anyone has thoughts on this.

## Screenshots


![image](https://github.com/elastic/kibana/assets/6766512/0906817c-0098-4b67-8791-d06730f450f6)


![image](https://github.com/elastic/kibana/assets/6766512/59e7c132-f568-470f-b48d-53761ddc2fde)


![image](https://github.com/elastic/kibana/assets/6766512/986372df-a90f-48c3-ae24-c3012e8f7730)

## To test

1. Set up Fleet Server + ES + Kibana
2. Spin up a Fleet Server running Agent v8.11.0
3. Enroll an agent running v8.10.4 (I used multipass)
4. Verify the agent can be upgraded from the UI

---------

Co-authored-by: Kibana Machine <42973632+kibanamachine@users.noreply.github.com>

---
## [BadAtThisGame302/cmss13](https://github.com/BadAtThisGame302/cmss13)@[f367771f57...](https://github.com/BadAtThisGame302/cmss13/commit/f367771f5799b87257d92cb79db71bcd85b62f75)
#### Thursday 2023-11-30 17:34:12 by Birdtalon

Eggsac carrier revival (#4716)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

[Forum Thread](https://forum.cm-ss13.com/t/eggsac-carrier-revival/4711)

# About the pull request

The concept of this PR is to find a middle ground between the current
eggsac carrier and the pre #4459 eggsac carrier.

This PR will make the following changes. (From this point "normal weeds"
can be substituted for "off hive weeds" Placing eggs on hive weeds is
**unchanged**.)

- Eggsac carrier can once again place eggs on normal weeds.
- Eggsac carrier can only place 4 eggs at once on normal weeds.
- If the Eggsac places more than 4 eggs on normal weeds, their oldest
placed egg will die. No hugger release.
- Eggs placed on normal weeds have a maximum lifetime of 5 MINUTES after
which they will die. No hugger release.
- Eggs placed on normal weeds have a 1 MINUTE life whilst the carrier is
further than 14 tiles away from them.
- If the carrier dies, all of their sustained eggs die.

# Explain why it's good for the game

Eggsac carrier at the moment is in a bit of a poor place and has gone
from being very strong to quite poor. Considering the limitation of
having to place only on hive weeds.
The majority of feedback I read against eggsac carrier was with the
quantity of eggs able to be placed, as well as the locations they can be
placed in, all across the map and with impunity.

This PR aims to address those concerns to make the eggsac both less
infuriating to play against while still being satisfying to play as a
frontline support or as a stealthy trapper.

Eggs can no longer be placed all over the map because of the 4 egg limit
off weeds, so the carrier has to think where they want to impact the
map. The carrier also has to stay within a reasonable distance to where
they are impacting with their eggs which localises their impact to their
immediate play area. The carrier also has to be more reactive to current
events as they cannot place an egg which then becomes useful 30 minutes
later.

Killing the carrier also has a small reward as in addition to removing a
xeno from the game, the eggs they are sustaining are cleared. If a
carrier is supporting the front and dies, the marines don't then have to
clear X number of eggs AFTER the kill.

# Testing Photographs and Procedure

1. Spawn as egg carrier.
2. Plant egg on normal weeds.
3. Move 15+ tiles away.
4. Wait 1 minute
5. OR Wait 5 minutes within 14 tiles.
6. Kill the carrier.

The 5 minute lifetime of the eggs will also clear the eggs in the case
that the carrier is admin deleted, or some other weird stuff happens
which doesn't result in a death. This will also catch carriers
de-evolving

<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
label your changes in the changelog. Please note that maintainers freely
reserve the right to remove and add tags should they deem it
appropriate. You can attempt to finagle the system all you want, but
it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Maintainers freely reserve the right to remove and add
tags should they deem it appropriate. -->

:cl:
add: Eggsac carrier can now place eggs on normal weeds to a maximum of 4
eggs.
add: Eggsac carrier eggs on normal weeds have an expiry date.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [DandelionSprout/adfilt](https://github.com/DandelionSprout/adfilt)@[e08e13557c...](https://github.com/DandelionSprout/adfilt/commit/e08e13557cc0bb9f2a8b7b625d942dcd688a19b2)
#### Thursday 2023-11-30 17:36:29 by Imre Kristoffer Eilertsen

Update AntiCorruptSportsList.txt

The phrase "Fuck this shit" is warranted by now. Professional diplomatic language be damned.

---
## [mosra/magnum-extras](https://github.com/mosra/magnum-extras)@[c1682d5acf...](https://github.com/mosra/magnum-extras/commit/c1682d5acf5064218b1acbf65b73fde2090ea0a9)
#### Thursday 2023-11-30 17:49:54 by Vladimír Vondruš

Whee: rework BaseLayer and TextLayer style assignment.

Requiring the calling code to have a compile-time-sized struct felt like
a good idea in theory. In practice it's absolutely horrendous tho, as:

 - The calling code then has to ensure matching order between a style
   enum and a style struct, which is extremely hard to maintain without
   a nasty preprocessor magic.
 - Defining a builtin style means either having to define & document a
   struct that glues a LayerStyleCommon instance together with several
   LayerStyleItem instances, which is nasty on its own, and then have to
   *somehow* populate it. Which in a (C++11) constexpr context means
   either using the implicit initializer, again losing any mapping from
   the actual enum values to the order (thus gaining *nothing* from such
   a "named tuple" definition), or having to give up on any constexpr
   use and assign to the named fields in order to ensure at least some
   ordering sanity.
 - It's extremely annoying and / or impossible to extend the style
   definition for custom widgets -- one has to *derive a struct* for
   that, and then somehow copy the original builtin data to its prefix.
 - The error message when the layer style count differs from the actual
   passed data is total garbage. Nobody is interested in how many bytes
   something occupies, they want to know *what is wrong* and the API
   isn't capable of saying or even knowing that.

So now it's instead a setStyle() API taking the LayerStyleCommon
instance and a (contiguous) list of LayerStyleItem. A downside is that
the (GL) implementation then does two GL buffer uploads, alternatively
it could put them together and upload at once (which means a nasty temp
allocation). With Vulkan (and I hope WebGPU) this won't be a problem as
there's a way to submit multiple uploads in a single command, or just
memory-mapping the buffer and doing a copy directly.

Extending a style is then a matter of creating an array that's larger
than the compile-time constant, having the custom style items start from
that constant, and copying the original data to prefix of that array.
Simple.

For the TextLayer this also merges the previous setStyle() and
setStyleFonts() APIs together, because they were always meant to be
called together anyway. It makes the whole usage a lot less janky and
unclear.

---
## [ruuda/rcl](https://github.com/ruuda/rcl)@[bb600760fb...](https://github.com/ruuda/rcl/commit/bb600760fbbe96bf7ae56eb9fd9f019f43905fa9)
#### Thursday 2023-11-30 19:08:01 by Ruud van Asseldonk

Merge support for lambda functions

One of the most pressing features that I need right now is group_by. It
can be done with comprehensions, but that is O(n²). For this, I need a
predicate to group by, so I need functions. RCL was always going to have
user-defined functions, so now is the time.

The most pleasant syntax in my opinion, is 'arg => body'. But for
multi-argument functions, '(arg1, arg2) => body', this requires
lookahead in the grammar, which I don’t know how to implement elegantly.
The current choice is a bit of a hack, and it could lead to confusing
error messages. Backtracking would be inefficient and can also lead to
confusing error messages.

The alternatives all require introducing a prefix token to disambiguate
functions from parenthesized expressions. For example, 'fn arg => body',
'fn arg: body', and '|arg| body'. But I find these visually less
pleasing. So for now, let's see how far the current syntax will go, it
can always be changed later.

I suspect RCL was previously not Turing complete because it only had
bounded loops, and I suspect that now it is, because it can now do
recursion.

The implementation is horribly inefficient. It clones the body AST, and
it stores the full construction site environment in the lambda, not only
the captured variables. But optimization can come later, let's get the
features in first.

---
## [kittysmooch/Skyrat-tg](https://github.com/kittysmooch/Skyrat-tg)@[58be66a653...](https://github.com/kittysmooch/Skyrat-tg/commit/58be66a6539c6e5b45588c8e1ed6c4b526e1d5ee)
#### Thursday 2023-11-30 19:38:32 by SkyratBot

[MIRROR] Nukie Update Followup: Returns CQC to the previous price range, Core Gear kit for newbies, hat stabilizers for everyone [MDB IGNORE] (#24679)

* Nukie Update Followup: Returns CQC to the previous price range, Core Gear kit for newbies, hat stabilizers for everyone (#79232)

## About The Pull Request

Brings the CQC kit back down to the same price range of 14 TC (it's 1
more than before weapon kits). It feels like currently that CQC is
overpriced, even with the stealth box coming along with it, and by
comparison the energy sword and shield got a huge value increase by
combining the two. They're both melee styles and also equally difficult
play styles. It isn't really necessary to make one more expensive than
the other. Also now comes with syndicate smokes. It's a whatever change,
ops get these for free on the base.

Adds a core gear kit in the weapon category. This kit comes with a
doormag, a freedom implant, stimpack and c-4 charge. All of these are
items almost every nukie buys if they want to succeed, so let's inform
newer players by putting it RIGHT on top of the list. This isn't at any
discount, this is mostly to help inform players what items help make you
successful.

Hat stabilizers are now a part of every syndicate modsuit for FREE. It
comes built in, can't be removed, and has no complexity cost. Now
everyone can wear their wacky hats as they operate.

## Why It's Good For The Game

CQC felt like it got shafted waaay too hard with the weapon case
changes. Definitely don't believe that it is punching at the same weight
as many of the other high cost weapons. So we've dropped it down a
category. 14 TC is still a large upfront cost, even if it comes bundled
with a lot of goods.

Melbert gave me the idea of a core bundle kit to help newer players and
I was really taken with that. So I added it as part of this followup.

I want people to wear their hats goddamnit, and I didn't learn my
mistake with the tool parcels. So now everyone has hat stands on their
suits. WEAR THE SOMBRERO YOU **FUCK**.

### THIS IS NOW A THREAT.

## Changelog
:cl:
balance: Operatives can once again read about the basics of CQC at a
reasonable price of 14 TC.
qol: All Syndicate MODsuits come with the potent ability to wear hats on
their helmets FOR FREE. No longer does any operative need be shamed by
their bald helmet's unhatted state when they spot the captain, in their
MODsuit, wearing a hat on their helmet. The embarrassment has resulted
in more than a few operatives prematurely detonating their implants! BUT
NO LONGER! FASHION IS YOURS!
qol: There is now a Core Gear Box, containing a few essential pieces of
gear for success as an operative. This is right at the top of the
uplink, you can't miss it! Great for those operatives just starting out,
or operatives who need all their baseline equipment NOW.
/:cl:

* Nukie Update Followup: Returns CQC to the previous price range, Core Gear kit for newbies, hat stabilizers for everyone

---------

Co-authored-by: necromanceranne <40847847+necromanceranne@users.noreply.github.com>

---
## [AcevedoB/Music-Bot-Project](https://github.com/AcevedoB/Music-Bot-Project)@[35af4c6fc3...](https://github.com/AcevedoB/Music-Bot-Project/commit/35af4c6fc39b77962eeea12713527784a45e993e)
#### Thursday 2023-11-30 19:56:06 by AcevedoB

So much pain

Adjusting the commands to include a bit more information. Turns out it FUCKING SUCKS ASS TRYING TO FIGURE OUT HOW TO ACCESS A SEPERATE JSON USING THIS STUPID ASS API but it's okay because we figured it out yay!

---
## [ilikegoodfood/Orcs-Plus](https://github.com/ilikegoodfood/Orcs-Plus)@[58dad36465...](https://github.com/ilikegoodfood/Orcs-Plus/commit/58dad36465e2a7a79c774a1dc650ba1841a6b822)
#### Thursday 2023-11-30 20:14:37 by ilikegoodfood

Chandalor Update

- Implemented Curseweaver god specific tenet for Chandalor.
- Implemented Broken Spirit curse.
- Improved conditions and utility scores for Spread Curse of Glory ritual.
- Blood Gourd item will now heal minions if the carrying agent's health is at max.

---
## [BallOfEnergy1/Hbm-s-Nuclear-Tech-GIT-OC](https://github.com/BallOfEnergy1/Hbm-s-Nuclear-Tech-GIT-OC)@[d217cfb7f3...](https://github.com/BallOfEnergy1/Hbm-s-Nuclear-Tech-GIT-OC/commit/d217cfb7f3a1af106a866dc2bbab5c4667e546ab)
#### Thursday 2023-11-30 20:19:52 by BallOfEnergy

i fucking hate github
this is to fix everything that github just broke
including removing the shit from that one PR that broke everything

---
## [MollyThaMasta/Pugh-3258-Final](https://github.com/MollyThaMasta/Pugh-3258-Final)@[533054ed32...](https://github.com/MollyThaMasta/Pugh-3258-Final/commit/533054ed324ced21066f1bfd6334a396cb32d124)
#### Thursday 2023-11-30 20:20:49 by MollyThaMasta

aita


AITA for telling my friend it’s her fault for getting married and having kids late because the world won’t wait on her now

I (39F) have a 6 person girl group since college (37-39F) and that includes Mary (38F). We’ve been close throughout the years and have been at milestone events for each other. Mary just had a baby and is completely fitting the crazy new mother stereotype.

In college, Mary has always been someone who had to make it known that she was unique/different from the rest of us which wasn’t as draining then as it has become now. For starters, all other women in our circle, got married between the ages of 22-27 and we all have multiple kids. So the 5 of us were able to experience those milestones alongside one another and got closer as we shared similar lifestyles.

Mary was very adamant on not settling until her 30s because she wanted to travel and have different experiences which we all supported. Regardless, she would continue to make comments about how she’s so lucky unlike us because we’re “tied down with husbands and babies”. I think this is where she grew resentment towards us because we were in different places in life and she was upset we couldn’t have our group be similar to how it was in college.

Then into our mid 30s it became a whole saga of she’s getting older and can’t find a husband because all the “good men” are married or divorced with kids. When she finally got married, many could not attend because it was a destination event and child-free during Covid. This caused a fight because she said how she was there for us during our weddings but we couldn’t put aside a week for her. We had all told her how we wished we could, but it simply was not financially feasible and didn’t logistically work with our kids. But she just refused to hear us out and was simply so inconsiderate about our lives and families, saying we were horrible friends.

Now, Mary just gave birth to her first child and I was very excited for her. The only issue is that she moved from our state to a very remote place that’s only accessible by a 6hr car ride. Her baby is 6mo old and none of us have been able to go up to visit her. I think she’s been having a wrong idea of what a “village” is and has essentially demanded in our groupchat that we come up for the holidays and help her out because she’s having a hard time adjusting to mom life. But this would entail we all take a week off, arrange childcare, figure out transportation, and book hotels during the holidays. It’s gotten to the point where she’s posting cryptic messages on Facebook bashing “fake friends” who won’t be there for her. As much as I wish I could, I cannot physically support her in the way she needs me to do in this stage of life. It would have been completely different if she still lived in our city and this was earlier in life when we had less commitments/priorities. So I told her this and that if she was hoping for this big village and constant support, she should have thought about that when planning out her life because we can’t all just pause our lives for her. So AITA?

---
## [thornAvery/kep-hack](https://github.com/thornAvery/kep-hack)@[d41d0e8e9a...](https://github.com/thornAvery/kep-hack/commit/d41d0e8e9aac039285a3530146f253b0f60385c9)
#### Thursday 2023-11-30 20:48:54 by Martha Schilling

minor post-playtest fixes

- Moved one of the trainers in the Celadon Uni PokeCenter to stop him from being in the way of the nurse

- Buffed one of the Scientists in the Mansion

- Moved the nurse and Weezing trader on the SS Anne slightly

- Boosted Meltan's catch rate because having it be that low is ridiculous

- Increased Luxwan's height because real swans are not that small

- Changed a Cue Ball's party to allow his dialogue to make sense

- Wild level balancing around Vermilion City

- Fixed a small Pokedex display bug

- Text fixes

---
## [mnh48-minetest/minetest_game](https://github.com/mnh48-minetest/minetest_game)@[4b95de5656...](https://github.com/mnh48-minetest/minetest_game/commit/4b95de5656ae3a7aa632ef12b6fb3dda94a56d36)
#### Thursday 2023-11-30 22:31:35 by Yaya - Nurul Azeera Hidayah @ Muhammad Nur Hidayat Yasuyoshi

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
## [BlueWildrose/Citadel-Station-13-RP](https://github.com/BlueWildrose/Citadel-Station-13-RP)@[33cae266af...](https://github.com/BlueWildrose/Citadel-Station-13-RP/commit/33cae266af864b22c509f65ffff3ad7277bbb459)
#### Thursday 2023-11-30 22:55:00 by Captain277

Subtypes Corporate Crates, Fixes Mapped Biohazard Crate, Renames Advanced Voidsuit (#6126)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

1. *Fixes Bug With Corporate Crates, Subtypes Them.*
2. *Removes Varedited Biohazard Bin and Places Normal Biohazard Bin.*
3. *Changes Advanced Voidsuit Name to Advanced Hardsuit.*

## Why It's Good For The Game

1. _I received reports of one specific corporate crate not rendering
properly when opened. As I inspected it, I realized it would be more
efficient to subtype all corporate crates, so I did that. HOWEVER, this
did not repair the initial bug. For some reason the crate was not
rendering its 'aethersecureopen' state, even though all variables and
code seemed to be working properly. No other crate exhibited this issue.
I discovered that by changing the name of the icon state from
'aethersecureopen' to 'aethersecopen', the state began to enforce and
render properly. I suspected it might be a name length issue, but tests
with other equally long icon states in the crate section disproved this
theory. This may warrant further investigation._
2. _This one avoided detection during my initial sweep through. Can't
remember who just went in and tried to varedit bins to fix biohazards,
but hopefully this is the last one they touched._
3. _This has been driving me crazy for a few days, and yesterday
especially. The Advanced Voidsuit is clearly misnamed, as it is in fact
a Hardsuit. When I tried to order these yesterday I overlooked this
cargo entry twice because I was looking for a hardsuit, not a voidsuit.
This just fixes the name._

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
add: Adds Corporate Crate Subtype, Reassigns Corporate Crates to It.
fix: Fixes incorrectly mapped biohazard bin.
tweak: Changes Name: Advanced Voidsuit to Advanced Hardsuit.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [calblueprint/impact-fund](https://github.com/calblueprint/impact-fund)@[11314efd14...](https://github.com/calblueprint/impact-fund/commit/11314efd1494004d1c856254ac78e1b96ba5df26)
#### Thursday 2023-11-30 23:00:46 by Philip Ye

[QRCodeScanner] Fixed Scan Issues and Supabase Queries 

* fixed some issues, useEffect being weird

* fuck you ESLINT

* fixed thing

* fixed some issues, useEffect being weird

* fuck you ESLINT

* fixed thing

* hello, fixed toast thing

---
## [mission23/MCBCMassacre](https://github.com/mission23/MCBCMassacre)@[371c129fa3...](https://github.com/mission23/MCBCMassacre/commit/371c129fa388189185f0f17a8853bf6cb9d29cfc)
#### Thursday 2023-11-30 23:06:06 by Kelvin Williams

GATech Warning!!! Direct from the Creator.

# Georgia Tech Warning
The CIA is trying to tie up lose ends, meaning killing anyone that may
know things or the true GATech Alumni (2013) Kelvin Eugene Williams.

## Cloaking
The CIA utilizes a cloaking technology that will render a person
practically invisible to the naked eye. It’s stolen from the military.

You should be able to find some documentation on it by searching. I
found a [this
article](https://www.nature.com/articles/s41598-017-08505-w) on photon
entanglement and cloaking that told me a lot.

It’s an electromagnetic field, I know there’s equipment on campus that
can and does detect it. Remember this is a revenge of the nerds and
you are your brother’s and sister’s keeper.

They CAN and DO use a companion technology that enables them to pass
through walls and doors.

The Creator says they are on campus tonight. (To the nerd reading
this: START RINGING THE FIREBELL! Let everyone on campus know, I bet
you have a way.)

Everyone on campus needs should not sleep alone. Pair up with another
student. Four hours of sleep is all you need. While one is sleeping,
the other is up watching and listening.

(Saving. Reload in a couple minutes for more.)

---
## [mission23/MCBCMassacre](https://github.com/mission23/MCBCMassacre)@[daa0efa5ae...](https://github.com/mission23/MCBCMassacre/commit/daa0efa5ae0b9fed2422d3e8da2b5249ecad4973)
#### Thursday 2023-11-30 23:06:06 by Kelvin Williams

annie's gonna hit again

I just realized that the other day someone told Maine to let it all
out, we had an escort here last night, measurements all around I fell
short that means she's winning over God and that means Annie is going
to strike into the church this weekend.

---
## [ReturnToZender/ReturnsBubber](https://github.com/ReturnToZender/ReturnsBubber)@[b5e095e380...](https://github.com/ReturnToZender/ReturnsBubber/commit/b5e095e380e729793628d254bb441f51ecdb046b)
#### Thursday 2023-11-30 23:22:04 by Waterpig

[MODULAR] Refactors (hopefully) all borg modular changes into one module, adds raptor borgs (#777)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Originally I was supposed to only add raptor borgs, but I am simply too
insane to let this shitcode slide.

Moves most if not all borg modular changes into one module folder
because by god these were spread out over like 8 files.
Improves modularity a bit by moving some borg related bubber edits on
skyrat into our modular files.
Adds raptor borgs

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Please make sure to actually test your PRs. If you have not tested
your PR mention it. -->

## Why It's Good For The Game

Modularity good.
Code organizing good.

https://en.wikipedia.org/wiki/Technical_debt

Also new borg sprites are cool, I guess. See icondiff bot for those
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
image: New borg sprites: Raptor
refactor: Moved most if not all bubber borg code into one modular folder
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

<!-- By opening a pull request. You have read and understood the
repository rules located on the main README.md on this project. -->

---

