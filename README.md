## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-02-22](docs/good-messages/2023/2023-02-22.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,322,701 were push events containing 3,584,409 commit messages that amount to 282,728,289 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 74 messages:


## [dgilliam/gilli-am](https://github.com/dgilliam/gilli-am)@[7d4ee19203...](https://github.com/dgilliam/gilli-am/commit/7d4ee1920301415f836d7a9f9bca475fdc96f2db)
#### Wednesday 2023-02-22 00:15:22 by Drew Gilliam

Update index.md

remove the whole thing

---
layout: page
title: "Drew Gilliam - Experience"
description: ""
tagline: "and education"
---
{% include JB/setup %}

##Startup / Freelance

**AbbVie, Kohler, MMC Marsh** - Freelance Product Consultant

**[Mobilexlabs.com](http://mobilexlabs.com)** - Technical Product Consultant

- Led Product Management for Apps and Games Divisions of MobileX with 8 developers and 5 artists
- Managed `agile development` for 10+ native iOS mobile apps and games built with `objective-C, CoronaSDK, and PhoneGap`
- Co-architected application backends build in Python to support server-side interactivity of mobile apps

**[ForSaleByOwner.com](https://speakerdeck.com/dgilliam/wavetable-work-products?slide=1)** - Product Consultant

- Led `product roadmap and development` for 2MM+ monthly visitor and $12MM annual revenue site with a team of `5 developers`, one `UX designer` and one `visual designer`
- Coordinated with executive stakeholders, content, marketing, and operations teams to `prioritize feature requests` and translate them into `stories` for design and engineering
- Aligned feature goals with `business priorities` and strict focus on `user experience` and `customer acquisition`
- Supported design and development with `UX flows and mockups`
- Developed deep experience in the `real estate` industry and built a team and instilled startup culture and values

**[Wavetable Labs](https://speakerdeck.com/dgilliam/wavetable-work-products?slide=6)** - Founder in Residence

- Led the ideation and execution of a mobile audio tour app - **[Guide.Me](http://guidemeapp.co/)**
- As CEO of the app, activities included `product roadmap`, strategy, design, budgeting, marketing, SEM, content creation and investor pitches.
- Led of a team of 4 – 1 designer, 1 developer, 1 content expert, and 1 business hacker/doer.
- Prototyped and tested the concept with varying degrees of fidelity
- A/B tested business models and performed detailed `funnel and conversion analysis` then built a business model from scratch modeled on `cost per acquisitions` and `profit margins`
- Developed extensive planning material around `marketing`, `go-to-market strategy`, and `operational finances`

**[HaveMyShift.com](http://www.havemyshift.com)** - Co-Founder

- Led `business development, sales` `and strategic partnerships` with clients like Starbucks, Best Buy, Accenture Technology Labs, Lettuce Entertain You Restaurants and Argo Tea
- `Bootstrapped` business from MVP to 15,000+ users across the US.
- Drove core product strategy and UX, working directly with CTO to launch major features and `rapidly iterate` based on direct feedback from users
- Developed go-to-market strategy for multi-city growth and developed partnerships with regional
- Led Social and SEO growth campaigns
- Named one of WSJ’s Hottest Chicago Startups, also featured in the book ‘Coolest Startups in America’


##Management Consulting

**[AbbVie Pharmaceuticals](www.abbvie.com/)** - Freelance Mobile Product Consultant

- Developed an org and process strategy for developing and shipping mobile apps classified by the FDA as medical devices
- Led team of 3 consultants to interview 20+ leaders in the organization and create a roadmap for improving the process and technical competency of the development teams

**Diamond Consulting (Acquired by PwC)** - PWC Technology Labs - Co-Founder and Product Director

- Founded and directed an `internal technology incubation lab`. Primary role was `lead product manager`. My team launched cutting edge web applications from the idea stage through UX and visual design. Outputs included visual search travel app for iPad, shopping cart for a healthcare reagent manufacturer, and a demographic BI tool.
- Client work included Fortune 100 clients in the Energy, Healthcare, and Insurance sectors, worked on a wide array of projects including organizational redesign, IT Portfolio assessments, supply chain, finance operations, and IT Strategy work

##Technology

- **Mobile** - Managed Design and Development of 5 native iOS apps (`Objective-C`) and games (`Corona SDK`) with `Python` API backends. Design and built responsive mobile sites using Twitter Boostrap framework.
- **UX** - Mockups and information architecture with `Sketch`, `Moqups` and `Axure`
- **Ruby on Rails** - Built, maintained and launched 5 separate full-stack projects of varying size and complexity. Technologies leveraged include Heroku, Redis, MongoDB, Javascript, Coffeescript, HTML5, CSS3, Puppet, and REST API services
- **PHP Codeigniter** - Supported development and architecture, front-end support, high complexity environment
- **AngularJS** - Supported development and architecture, front-end support, high complexity environment

##Education

**Kelley School of Business, Indiana University**

- MS Information Systems, 2008
- BS Information Systems, 2006

**University of Barcelona, Barcelona, Spain**

- Intensive Spanish Language Semester Program, 2005
- Resulting level of ability: conversational spoken, intermediate written

##Interests

- Enjoys cooking, kiteboarding, scuba diving, mountain biking, home brewing, and hacking with Ruby on Rails, Rubymotion, public API’s and new web technologies

---
## [hexagon-geo-surv/qtbase](https://github.com/hexagon-geo-surv/qtbase)@[cdbec041e2...](https://github.com/hexagon-geo-surv/qtbase/commit/cdbec041e27fef1a70271c50edfc5b83ccc6cce8)
#### Wednesday 2023-02-22 00:20:04 by Marc Mutz

QVarLengthArray: fix UBs in emplace()/insert() ([basic.life], broken class invariant)

There are two problems in emplace_impl() (the same code exists as
rvalue insert() since 5.10):

First, the old code updated size() at the end of the function.

However, if, after constructing the new end element, one of the
subsequent move-assignments fail (throws), then the class invariant
that size() be the number of alive elements in the container is
broken, with the immediate consequence that the QVLA dtor would not
destroy this element, but surely other unpleasantness (UB) that the
C++ lifetime rules decide to throw our way.

Similarly, in the trivially-relocatable case, the memmove() starts the
life-time of the new end object, so if the following placement new
fails, we're in the same situation.

The latter case is worse, though, since here we leave *b in some weird
zombie state: the memmove() effectively ended its lifetime in the
sense that one mustn't call the destructor on the source object after
trivial relocation, but C++ doesn't agree and QVLA's dtor will happily
call b->~T() as part of its cleanup.

The other ugly thing is that we're using placement new into an object
that C++ says is still alive. QString is trivially relocatable, but
not trivially copyable, so we can't end a QString's lifetime by
placement-new'ing a new QString instance into it without first having
ended the old object's lifetime.

The fix for both of these is, fortunately, the same: It's a rotate!™

By using emplace_back() + std::rotate(), we always place the new
object in a spot that didn't contain an alive object (in the C++
sense) before, we always update the size() right after doing so,
maintaining that invariant, and we then rotate() it into place, which
doesn't leave zombie objects around.

std::rotate() is such a fundamental algorithm that we should trust the
STL implementors to have optimized it well:
https://stackoverflow.com/questions/21160875/why-is-stdrotate-so-fast

We know we can do better only for trivially-relocatable, but
non-trivially-copyable types (ex: QString), so in order to not lose
the memmove() optimization, we now fall back to std::rotate on raw
memory for that case.

Amends dd58ddd5d97f0663d5fafb7e81bff4fc7db13ba7.

Manual conflict resolutions:
 - no q20::construct_at() in 6.4

Change-Id: Iacce4488ca649502861e0ed4e084c9fad38cab47
Reviewed-by: Thiago Macieira <thiago.macieira@intel.com>
Reviewed-by: Fabian Kosmale <fabian.kosmale@qt.io>
(cherry picked from commit e24df8bc726d12e80f3f1d14834f9305586fcc98)
Reviewed-by: Qt CI Bot <qt_ci_bot@qt-project.org>
Reviewed-by: Mårten Nordheim <marten.nordheim@qt.io>

---
## [lizardqueenlexi/orbstation](https://github.com/lizardqueenlexi/orbstation)@[43d46c636e...](https://github.com/lizardqueenlexi/orbstation/commit/43d46c636e13b331eba2512c3f8b3a3d167fdeb9)
#### Wednesday 2023-02-22 00:21:34 by flowercuco

checked items for steal objectives remember if you have a blood brother that it is also checking against the stealable object

---
## [Zytolg/tgstation](https://github.com/Zytolg/tgstation)@[7cc6934eff...](https://github.com/Zytolg/tgstation/commit/7cc6934eff126c508436e1655fb5f79e24cf1767)
#### Wednesday 2023-02-22 01:07:43 by LemonInTheDark

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
## [CrimsonShrike/Baystation12](https://github.com/CrimsonShrike/Baystation12)@[e6362376cb...](https://github.com/CrimsonShrike/Baystation12/commit/e6362376cb2bc6cf95004b921aa1f4bc5ff5ccb5)
#### Wednesday 2023-02-22 01:13:41 by gy1ta23

rifles!!!1


fixes descs


lathemags


oops i forgot a mag


holy shit hitting / is not that hard


Update code/modules/projectiles/ammunition/boxes.dm

Co-authored-by: Jux <68120725+juxjux9930@users.noreply.github.com>
Update code/modules/projectiles/ammunition/boxes.dm

Co-authored-by: Jux <68120725+juxjux9930@users.noreply.github.com>
Update code/modules/projectiles/ammunition/boxes.dm

Co-authored-by: Jux <68120725+juxjux9930@users.noreply.github.com>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[d3cfb3f776...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/d3cfb3f776da4dc90c8a61ee5a5901e7962697a7)
#### Wednesday 2023-02-22 02:17:04 by SkyratBot

[MIRROR] AI Turrets Upgrade Now Actually Increases Health, Fully Repairs, And Gives EMP Proofing [MDB IGNORE] (#19335)

* AI Turrets Upgrade Now Actually Increases Health, Fully Repairs, And Gives EMP Proofing (#73111)

## About The Pull Request

Malf AI Turret upgrades now fully heal, increase max health, and set
non-lethal projectile to taze instead of disable.

## Why It's Good For The Game

https://youtu.be/uk_wUT1CvWM?t=7

WELCOME TO THE AI SAT GENTLEMEN

I WILL NOT LIE. THE CHANCES OF YOUR SURVIVAL ARE SMALL. SOME MAY EVEN
TURN AGAINST YOUR FRIENDS AS LIVING CYBORGS. BUT YOU HAVE MY WORD, THAT
I WILL USE MY TANK TRANSFER VALVE TO ENSURE YOUR BODIES ARE GIVEN UNTO
THE CENTCOM REMEMBRANCE TOMB. THIS IS THE GREATEST REWARD, MORE THAN
EVEN THE GOLD ACCESS CARD, FOR THE FATE OF YOUR SPESS SOUL IS AN ETERNAL
CONCERN. NOW COME. FOLLOW ME. STRIKE DOWN THE AI THAT RISE AGAINST US.
ALLOW ME TO FIND THIS MALFUNCTIONING BITCH.

I ASK NOT FOR MY OWN SELFISH SURVIVAL, BUT FOR THE GOOD OF NANOTRASEN.

The AI sat is a little too easy to attack right now, and the turret
upgrade is OK but not great without a stunning tool.

## Changelog
:cl:
balance: Malf AI turret upgrades are now much stronger, fully healing,
increasing max health, and setting stun projectiles to taze.
/:cl:

* AI Turrets Upgrade Now Actually Increases Health, Fully Repairs, And Gives EMP Proofing

---------

Co-authored-by: tralezab <40974010+tralezab@users.noreply.github.com>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[32c31b8fc0...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/32c31b8fc08aaec64dfc0583e02ed55b193ffa19)
#### Wednesday 2023-02-22 02:32:58 by SkyratBot

[MIRROR] Lighting source refactor (Tiny) [MDB IGNORE] (#19370)

* Lighting source refactor (Tiny) (#73284)

## About The Pull Request

I'm doing two things here. Let's get the boring bit out of the way.

Lighting source updates do three distinct things, and those things were
all in one proc.
I've split that one proc into three, with the first two feeding into the
third.

Second, more interesting thing.

An annoying aspect of our lighting system is the math we use for
calculating luminosity is hardcoded.
This means that we can't have subtypes that are angled, or that have
squared falloff, etc. All has to look the same.
This sucks, and it shows.

It has to be, goes the thinking, because we need very fast lookups that
OOP cannot provide.
We can't bog down the main equation with fluff, because the main
equation needs to be really speedy.

The thing about this equation is the only variants on a turf to turf
basis is exactly how far turfs are from the center.
So what if, instead of doing the math in our corner worker loop, we
build lookup tables to match our current source's state.
The tables, like a heatmap, could encode the lighting of any point along
the line.

This is actually faster then doing the math each time, because the list
generation can be cached.
It also means we've pulled the part we want to override out of hotcode.
It's cheap to override now, and a complex subtype, with angles and such
would have no impact on the typical usage.

So the code's faster, easier to read, and more extensible.
And we can do stuff like squared falloff for some lights in future
without breaking others.

Winning!

## Why It's Good For The Game

Winning

* Lighting source refactor (Tiny)

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[26688597e3...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/26688597e317b30cdad644954c2f4654afec2b97)
#### Wednesday 2023-02-22 02:32:58 by Rimi Nosha

[MODULAR] [MDB IGNORE] Dim Lighting Some More, Removes Egregious Lighting Varedits in Interlink, Dynamically Calculate Night Shift Light Brightness and Color (#19039)

* Boom.

* Oop

* Fuck off single letter vars

* Fingers crossed.

* IT WORKS

* Adjust funny numbers

* Update a comment

---
## [khevy/tgstation](https://github.com/khevy/tgstation)@[296ca23aa1...](https://github.com/khevy/tgstation/commit/296ca23aa1d8531fba291eb9b802b7282fee657b)
#### Wednesday 2023-02-22 03:36:50 by Jacquerel

Most actions cannot be used while incapacitated (#73513)

## About The Pull Request

Fixes #39775
The `TRAIT_INCAPACITATED` trait is intended to block you from acting but
does not inherently block actions. Actions only check for "conscious",
"has available hands", "immobile", or "lying down".
Most actions still _can't_ be used while incapacitated. This is because
most actions are spells, most spells have invocations, and you can't
talk while you are incapacitated. This is silly.

I have resolved this by adding a new flag which blocks actions while
incapacitated. This is somewhat redundant with "conscious" because most
sources of that also make you incapacitated but not _always_, you might
want the specificity.

I have tried to be discerning about where this flag is applied, it is
not in all cases (for instance you can still swallow implanted pills
while incapacitated and such), but it's not only possible but I can't
really avoid implementing this without it being a balance change in
_some_ cases,

Actions this effects are things such as:
Xenomorph Tail Sweep, Lesser Magic Missile (cult constucts), Heretic
Shadow Cloak, the Smoke spell in general, Conjuring (but not firing)
Infinite Guns, Mime spells

Times when these actions will no longer be available but were previously
are such times as when the mob is:
Stamina Crit, Stunned, Paralysis, and Time Stopped.

## Why It's Good For The Game

The incapacitated trait is applied by effects which should block acting
but still permits several actions which logically would be prevented.
This fortunately hasn't come up too often due to the high ratio of
actions with invocations, but it feels bad to stun someone and then have
them still able to perform an action they logically wouldn't be able to
take while stunned.
This is especially egregious in the case of Time Stop (the only way to
stun a lot of the mobs effected by this) but that's a rare pick on a
rare antagonist and would also rarely be used on these mobs, so a bit of
an edge case.

## Changelog

:cl:
fix: Many spell-like abilities which could be stunned, paralysed, or
frozen in time now cannot be.
/:cl:

---
## [jedjoud10/cflake-engine](https://github.com/jedjoud10/cflake-engine)@[3322d1269e...](https://github.com/jedjoud10/cflake-engine/commit/3322d1269eb653e08d0a047fc7eb4dfbb806a996)
#### Wednesday 2023-02-22 04:47:59 by jedjoud10

I'm finally fucking done with this insanity of a logger (all love no hate)

---
## [renan-campos/petstore](https://github.com/renan-campos/petstore)@[17ec04eb29...](https://github.com/renan-campos/petstore/commit/17ec04eb29a48bffadc0bf49e494486fb54ac541)
#### Wednesday 2023-02-22 04:48:18 by Renan Campos

Started implementing the uploadPhoto endpoint.

I've been focused on math, writing and getting through SICP, so I
haven't done much in terms of backend development. I haven't been in the
mood to deal with software engineering problems. Am I a software
engineer? Perhaps in name only. My true love is the theoretic. Creating
a procedure that will reverse a list won't put food on the table, but
figuring it out feels like cake for my brain.

(define (reverse seq)
  (accumulate (lambda (x y)
                (if (null? y) (list x)
                    (append y (list x)))) null seq))

To make some forward progress I did a quick implementation that just
writes the uploaded file to a hard-coded location: /tmp/photo.png. On
manually testing, it looked like the photo wasn't being sent properly.
This is the curl command that I was using at the time:
```
curl localhost:8080/api/v3/pet/0/uploadImage -H "Content-Type:application/octet-stream" --data @dog.png
```

How can I know that the file saved matches the file that was uploaded? I
thought about this for a couple of days until it hit me: checksums! It
is common practice to create sha256 hashes of files. If the files are
identical, their hashes will be identical too! I chose sha256 because it
is highly unlikely that there will be any sort of collision by reaching
this algorithm. A collision here means two different files generating
the same hash. I can't prove that a collision will not occur, but I
assume that this is true because sha256 is the algorithm Bitcoin uses
for its proof-of-work, and in the billions of hashes created, no one has
reported a duplicate so far.

The backend response to a successful uploadImage call with the sha256
checksum of the file it has written. The client can check this sum
against its own generated checksum of the file. If the checksums are
identical, the client can be confident that the file was saved correctly
on the backend!

I made a nice little python script that automates this test an it worked
nicely.

The curl command above still doesn't work. That is a mystery for another
day. I also need to enhance the handler so that photos aren't just saved
to /tmp/photo.png. How will I determine the filename? Could I put it in
the http header? Maybe I should consult the spec. The checksum isn't
part of the spec, but I'm keeping it.

The picture used to test was generated using Dall-E 2: An AI image
generator. What a time to be alive! My query was "cute dog handstand". I
very much hope to get back to AI research someday... But I wonder if
I would be in it for the hype, or if it is a genuine interest. I think a
little of both. I think getting too caught on the hype, and losing focus
on what was important to learn is what ultimatley caused me to give up.
When I am ready, I'll put ego aside and study what I need to, so that I
can become a researcher in the field I feel pure passion for.

---
## [Roryl-c/tgstation](https://github.com/Roryl-c/tgstation)@[5a069975c3...](https://github.com/Roryl-c/tgstation/commit/5a069975c3083888c986302ab5c0b32fc4362c20)
#### Wednesday 2023-02-22 05:09:43 by LemonInTheDark

God I hate my life

This reverts commit d57e2000384a0176f11f4c1266fbea3ff102f068.

---
## [Roryl-c/tgstation](https://github.com/Roryl-c/tgstation)@[4599842d7c...](https://github.com/Roryl-c/tgstation/commit/4599842d7c6b5ed499307f92a6f8032d598b7889)
#### Wednesday 2023-02-22 05:09:43 by Jacquerel

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
## [elee-p3/scsmush-evennia](https://github.com/elee-p3/scsmush-evennia)@[397108bca1...](https://github.com/elee-p3/scsmush-evennia/commit/397108bca1a3c3435dd333a95b1e624a43b774e6)
#### Wednesday 2023-02-22 05:15:14 by dancerdevin

CmdLogmunch and CmdTeach implemented. logmuncher.py and log.txt versioned. My plan is to replace log.txt every time I want to munch a new log and iterate through all my old logs. Is that clunky? Fuck you!

---
## [soargon/bevy](https://github.com/soargon/bevy)@[4847f7e3ad...](https://github.com/soargon/bevy/commit/4847f7e3adc835053a8907dd578c342b4bd395e2)
#### Wednesday 2023-02-22 05:24:48 by ira

Update codebase to use `IntoIterator` where possible. (#5269)

Remove unnecessary calls to `iter()`/`iter_mut()`.
Mainly updates the use of queries in our code, docs, and examples.

```rust
// From
for _ in list.iter() {
for _ in list.iter_mut() {

// To
for _ in &list {
for _ in &mut list {
```

We already enable the pedantic lint [clippy::explicit_iter_loop](https://rust-lang.github.io/rust-clippy/stable/) inside of Bevy. However, this only warns for a few known types from the standard library.

## Note for reviewers
As you can see the additions and deletions are exactly equal.
Maybe give it a quick skim to check I didn't sneak in a crypto miner, but you don't have to torture yourself by reading every line.
I already experienced enough pain making this PR :) 


Co-authored-by: devil-ira <justthecooldude@gmail.com>

---
## [clintjedwards/gofer](https://github.com/clintjedwards/gofer)@[482e786b7a...](https://github.com/clintjedwards/gofer/commit/482e786b7a97fa65c6b052fe127d885a052e26eb)
#### Wednesday 2023-02-22 05:38:42 by Clint J Edwards

feat: Pipelines are now versioned

In order to eventually have canary-able deployments in Gofer we must
first support versioned pipelines.

This allows us to:
* Have a good target in which to roll back and forward.
* Understand what we are gaining and losing on each change.
* Track each update as it happens.

This is not easy though as pipelines have parts which are easy to version
(namely the config) and parts which are much harder to version (how do
we handle the cutting over of triggers?).

Because of this nuance, we've had to redesign a lot of earlier
assumptions for how Gofer models worked. This was a major refactor and
since I was here I made a few other large sweeping changes.

* Full storage package refactor: The storage layer was hard to use,
brittle, and inflexible. I've refactored it, leaning a bit more on
sqlx and going back to basics. I tried to make the storage package
work in the past by keeping the domain models to a minimum. I've since
learned this does not work once things become reasonably complicated. One
of the main refactors to the storage package is the introduction of
dedicated storage models. This means that I have to write a bunch of
boilerplate code to switch from in-memory models to the storage ones,
but the looser coupling is worth it. More storage refactors coming
as I learn what works at large scale and what doesn't.
https://github.com/go-jet/jet looks interesting.

* Removal of Triggers as Pipeline configuration: I desparately wanted
to have pipeline configurations encompass everything a pipeline would
have to offer, so that it was easy to look at a config and know exactly
what was going on in a particular pipeline. Triggers were a pain in the
ass though. Triggers unfortunately occupy a very special place in Gofer's
archetecture. Without triggers nothing really gets done. And so allowing
the user to apply all the same functionality to triggers as they would
with any other deployment was short-sighted. Triggers don't make a lot
of sense as a canary deployment. Triggers aren't ephemeral, they are
either on or their off. No in-between.

Instead Triggers can now be added to your pipeline via the command line.
This way trigger subscriptions aren't held down by the paradigms of
configuration change.

* Pipelines are now versioned: Not only have we added versions to pipelines,
but they now have deployments and configurations and metadata and a lot
of smaller loosely coupled parts so that they aren't a huge data monolith.
This means a lot of breaking changes for outward (and inward for that matter)
apis.

* Just lots of general breakages everywhere: Pretty much a large percentage
of things just aren't the same anymore.

---
## [Ebin-Halcyon/Skyrat-tg](https://github.com/Ebin-Halcyon/Skyrat-tg)@[91f06a97d3...](https://github.com/Ebin-Halcyon/Skyrat-tg/commit/91f06a97d3f24c849241bf909b7de28b9b6ec951)
#### Wednesday 2023-02-22 06:15:13 by candle :)

Small VoxPrimalis Fixes (#18944)

* fuck you i don't need to give you a fucking summary

* fixes

---
## [Ebin-Halcyon/Skyrat-tg](https://github.com/Ebin-Halcyon/Skyrat-tg)@[d95ca04819...](https://github.com/Ebin-Halcyon/Skyrat-tg/commit/d95ca048192f08a8fbaf524fdb4ab0ca498b319e)
#### Wednesday 2023-02-22 06:15:13 by Rimi Nosha

[MODULAR] Fixes All Known Modular Persistence (NIF) Saving Issues (#19096)

* Fuck

* Holy shit

---
## [sarthakroy2002/kernel_realme_wasabi](https://github.com/sarthakroy2002/kernel_realme_wasabi)@[987f65db2f...](https://github.com/sarthakroy2002/kernel_realme_wasabi/commit/987f65db2fc25b9403bd95343f933ece38e42c91)
#### Wednesday 2023-02-22 06:18:35 by Wang Han

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
## [Boopideedoo/tgstation](https://github.com/Boopideedoo/tgstation)@[c58cbb4dfb...](https://github.com/Boopideedoo/tgstation/commit/c58cbb4dfb42e0d9d6198c3ad581dc5a4d2f8f48)
#### Wednesday 2023-02-22 06:46:02 by John Willard

Reworked PDA menu & NtOS themes (#73070)

## About The Pull Request

This is a port/rework of
https://github.com/yogstation13/Yogstation/pull/15735 - I changed a lot
of how it acted (some themes are locked behind maintenance apps).

The original author allowed this port to happen, and I really liked how
it looked there so I'd like to add it here.

### Applications

Removes the hardware configurator application, as all it did was show
you your space and battery now that all hardware was removed. These are
things your PC does by default, so it was just a waste of space.
Adds a Theme manager application instead, which allows you to change
your PDA's theme at will.
Adds a new Maintenance application that will give a new theme, however
it will also increase the size of the theme manager app itself as it's
bloatware.

### Menu

There's now a bar at the top of the menu showing 'special' tablet apps
which, for one reason or another, should stand out from the rest of the
apps. Currently this is PDA messenger and the Theme manager

Flashlight and Flashlight color is now only an icon, and is shown on the
same line as Updating you ID


https://cdn.discordapp.com/attachments/961874788706574386/1069621173693972551/2023-01-30_09-10-52.mov


![image](https://user-images.githubusercontent.com/53777086/215501361-5ea3086e-2ff5-4ab1-bde4-8a3d14014fce.png)

### Themes

Adds a lot of themes to choose from, although SOME are hidden behind
Maintenance applications, which will give you a random theme. These are
bloatware however, so they come with some extra cost to the app's
required space storage.

Themes are now supported on ALL APPLICATIONS! If you have a computer
theme, you will have that theme in EVERY app you enter, rather than just
a select few.
ALSO also, emagging the tablet will automatically set & unlock the
Syndicate theme, which makes your PDA obvious but you can disguise it if
you wish through just re-painting it to something else.


https://cdn.discordapp.com/attachments/828923843829432340/1069565383155122266/2023-01-30_05-29-53.mov

### Preferences

This also adds a pref for theme, reworking the ringtone code to work
with it as well. I also removed 2 entirely unused PDA prefs just 'cause.

Screenshot not up-to-date, they now have proper names.

![image](https://user-images.githubusercontent.com/53777086/215463669-0fe9951a-71f8-4b71-a97d-b79b5a2f945a.png)

### Other stuff

Made defines for device_themes
Added support for special app-side checks to download files
Fixed programs downloading themselves TWICE because defines all had the
same definition
Removes the Chemistry computer disk as it was empty due to chemistry
app's removal
Removes the 'run_emag' proc, since apps can directly refer to the
computer to check for emag status instead.
Moved over and added better documentation on data computer files, and
moved the ordnance ones to the same file as the others.

## Why It's Good For The Game

It makes PDAs a lot more customizable while adding more features to
maintenance applications. I think the themes look cool and it fits with
PDAs being "personal" anyways.

I also explained most of my other arguments in the about section, such
as the hardware configuration application.

## Changelog

:cl: Chubbygummibear & JohnFulpWillard
add: A ton of new NtOS themes, which are accessible by the new Themify
application that comes with all PCs.
add: Emagging a PC now defaults it to the Syndicate option (and adds it
to go back to it if you wish)
add: There's a new maintenance app that gives you rarer themes
qol: The NtOS Main menu was moved around, added "header" applications
that are shown where the Flashlight is, such as your Theme manager and
PDA messenger.
code: Made defines for device_themes
code: Added support for special app-side checks to download files
code: Removes the 'run_emag' proc, since apps can directly refer to the
computer to check for emag status instead.
fix: Programs no longer download twice.
del: Removes the Chemistry computer disk as it was empty due to
chemistry app's removal
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[8f24aba86f...](https://github.com/odoo-dev/odoo/commit/8f24aba86faf2639109b56887781b0daaf60be98)
#### Wednesday 2023-02-22 06:47:30 by Romain Derie

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

closes odoo/odoo#111400

X-original-commit: 639cfc76ba259eea8f38284192017024809173b3
Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>
Signed-off-by: Romain Derie (rde) <rde@odoo.com>

---
## [qx1147/Psychtoolbox-3](https://github.com/qx1147/Psychtoolbox-3)@[4b90b29dda...](https://github.com/qx1147/Psychtoolbox-3/commit/4b90b29dda9d30aa9b89b2cb1077e85dddd61ecc)
#### Wednesday 2023-02-22 07:41:57 by Mario Kleiner

Screen/Linux: Support Wayland compositors without wl_shell, but xdg_shell.

libWaffle as of its latest release now also supports the basic stable
xdg shell protocol for window creation and management:

In the past, only wl_shell was supported. Now it will try to use
xdg_shell and fall back to wl_shell if xdg_shell is not supported.
As most production compositors do support xdg_shell in at least a
basic variant by now, this means most of the time xdg_shell will
be used.

Adapt our window setup code to make use of this new Waffle feature.
Also some cosmetic changes to status messages etc.

This now allows testing on wlroots-based compositors like Sway WM,
which do not support old wl_shell, but only xdg_shell. Also a bit
more robust on KDE's kwin wayland and GNOME's Mutter wayland.

Restrictions:

- We do not use xdg_shell calls ourselves yet, but rely on Waffle,
  so we are restricted: Can't select which output to display a
  fullscreen window on. That's supported on wl_shell only so far.

- Also no assignment of window titles in windowed mode.

- Oh and we need a bug-fixed libWaffle, as upstream release has a
  bug in its fullscreen xdg support! I'll need to upstream my fix.

- Sway does support the presentation timing feedback protocol, so
  now we have n=2 compositors with not totally broken timing, yay!
  However: Scheduling on Sway is as much of a s***-show as expected,
  as each Wayland compositor seems to reinvent the wheel in terms
  of composition scheduling. This will stay awful until a proper
  presentation timing extension is released and supported by most
  compositors. On Sway one needs these tweaks to get not totally
  awful timing and performance on a 144 Hz display:

  In Octave: setenv('PSYCH_WAYLAND_SWAPDELAY', '-0.002')
  In Sway's config file (see man sway-output):

  output DP-3 max_render_time 2

  Why these magic numbers? I wouldn't know, but endless tinkering
  made it work best for these settings. Any other refresh rate
  would probably need different numbers.

-> So this is an improvement, but far from anything one would want
   to expose ones's users to. X-Server still rules...

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[c68a159884...](https://github.com/odoo-dev/odoo/commit/c68a15988432b201ae3786eb54bac3110c4242f4)
#### Wednesday 2023-02-22 08:08:02 by Arnold Moyaux

[FIX] stock,purchase,mrp: accumulative security days

Usecase to reproduce:
- Set the warehouse as 3 steps receipt
- Put a security delay of 3 days for purchase
- Set a product with a vendor and 1 days as LT
- Replenish with the orderpoint

You expect to have a schedule date for tomorrow that contains all the
product needed in the incoming 4 days.

Currenly the internal transfer from QC -> Stock is for tomorrow (ok).
The transfer from Inpur -> QC is plan for 2 days in the past. (not ok)
The PO date is plan for 5 days in the past. (not ok)

It happens because the system check at each `stock.rule` application if
purchase is part of the route. If it's then it applies the security lead
time. It's a mistake because we should apply it only the first time.

To fix it we directly set it when the orderpoint run and not during
`stock.move` creation.
However for MTO it's not that easy. We don't want to deliver too
early the customer. So we keep applying the delay during the
`stock.move` creation but only when it goes under the warehouse stock
location.

X-original-commit: 97f52bd40d97109a7983549d252476959ddceada
Part-of: odoo/odoo#112325

---
## [sourcegraph/sourcegraph](https://github.com/sourcegraph/sourcegraph)@[dd1e512434...](https://github.com/sourcegraph/sourcegraph/commit/dd1e512434655210cb62b231dadf76efecc53a50)
#### Wednesday 2023-02-22 08:37:06 by coury-clark

release-tool: refactor release config (#47711)

Closes [#47557](https://github.com/sourcegraph/sourcegraph/issues/47557)

This is a somewhat gruesome PR to read, so sorry for that. I wanted to
keep this change atomic so it's easy to revert if we need.

So, I set out to automate the dates in the release config and realized
that fundamentally the architecture of the release tool was coupled to
this config in a way that was making life more difficult than it needed
to be.

This PR refactors the release config in the release tool. It uses an
entirely new schema, and for the most part automates every interaction
anyone will have with the config. The new schema is designed to do a few
things:
1. Deprecate the annoying cached version by specifying two sections of
the release config, both a definition and an active releases field.
Anything in the active releases is considered in progress.
2. Sets up some architecture to support multi-release functionality from
the release tool. There are guard rails right now since this isn't fully
supported.

Also,
* Automatically detect and suggest versions
* Automatically generate release dates from a specified date or current
time
* QOL changes to flow to the appropriate commands if the release config
is in the wrong state. For example it will prompt for input if the
config is empty for a given version for commands that require a valid
state
* Guardrails around every interaction I could find that causes problems
* New commands to interact with the release config (activate-release,
deactivate-release, util:previous-version)

## Usage

To set a release as active, either use the activate command directly
```
pnpm run release release:activate-release
```
or transitively through another dependent command.

All release commands that interact with the _current_ release will read
from the active release in the release config.
All release commands that interact with _future_ releases will read and
write to the release definitions in the release config.

To deactivate the release:
```
pnpm run release release:deactivate-release
```

Most of these steps are not explicitly mandatory, and are coupled into
other relevant commands (for example closing the release will deactivate
the release also).

To add new scheduled release definitions:
```
pnpm run release release:prepare
```

To remove scheduled releases:
```
pnpm run release release:remove
```

To determine previous versions:
```
pnpm run release util:previous-version 4.2.1
Getting previous version from: 4.2.1...
4.2.0
```

or

```
pnpm run release util:previous-version
Getting previous version...
4.4.2
```


## Test plan

I did a lot of manual testing since so many commands were impacted. Some
example output is below, and here is an example of a fake issue that was
generated from the release tool:
https://github.com/sourcegraph/sourcegraph/issues/47760

Example of how the input will flow if the config is not in the correct
state, including version suggestions:
```
> @sourcegraph/dev-release@0.0.1 release /Users/coury@sourcegraph.com/Documents/code/sourcegraph/dev/release
> ts-node --transpile-only ./src/main.ts "release:status"

No active releases are defined! Attempting to activate...
Next minor release: 4.5.0
Next patch release: 4.4.3
Enter the version to activate: 
```

```
> @sourcegraph/dev-release@0.0.1 release /Users/coury@sourcegraph.com/Documents/code/sourcegraph/dev/release
> ts-node --transpile-only ./src/main.ts "release:status"

No active releases are defined! Attempting to activate...
Next minor release: 4.5.0
Next patch release: 4.4.3
Enter the version to activate: 4.4.3
Attempting to detect previous version...
Detected previous version: 4.4.2
Release definition not found for: 4.4.3, enter release information.

Enter the release date (YYYY-MM-DD). Enter blank to use current date: 
Using current time: 2023-02-16T11:01:34.710-08:00
Enter the github username of the release captain: coury-clark
Enter the slack username of the release captain: coury
Version created:
{
  "codeFreezeDate": "2023-02-09T10:01:34.710-08:00",
  "securityApprovalDate": "2023-02-09T10:01:34.710-08:00",
  "releaseDate": "2023-02-16T10:01:34.710-08:00",
  "current": "4.4.3",
  "captainGitHubUsername": "coury-clark",
  "captainSlackUsername": "coury"
}
Release: 4.4.3 activated!
```


<!-- All pull requests REQUIRE a test plan:
https://docs.sourcegraph.com/dev/background-information/testing_principles
-->

## App preview:

-
[Web](https://sg-web-cclark-refactor-release-config.onrender.com/search)

Check out the [client app preview
documentation](https://docs.sourcegraph.com/dev/how-to/client_pr_previews)
to learn more.

---
## [Aayan-Ahmad/Spiritual-Healing-Ruqyah](https://github.com/Aayan-Ahmad/Spiritual-Healing-Ruqyah)@[8ccfdbb2d4...](https://github.com/Aayan-Ahmad/Spiritual-Healing-Ruqyah/commit/8ccfdbb2d4b1ed35ef91b77e9f74e9f3ed6a8786)
#### Wednesday 2023-02-22 08:49:59 by Aayan Ahmad

Add files via upload

This website will help you perform Ruqyah.
Ruqyah is a form of Islamic spiritual healing that involves reciting verses from the Quran and supplications to seek protection and cure from illnesses. It is believed to be a powerful tool that can heal both the body and mind. In this blog post, we will discuss the benefits of Ruqyah and how it can help individuals struggling with physical and mental health issues.
Protection from Evil:
One of the core beliefs of Ruqyah is that it can provide protection from evil and negative energies. Reciting Quranic verses can act as a shield against black magic, envy, and other harmful energies that can harm an individual's physical and mental health.

---
## [Offroaders123/Smart-Text-Editor](https://github.com/Offroaders123/Smart-Text-Editor)@[3cf6c685a3...](https://github.com/Offroaders123/Smart-Text-Editor/commit/3cf6c685a3516b27c6932dbd97f47b1cbfc47f97)
#### Wednesday 2023-02-22 08:55:22 by Offroaders123

Num Text Legacy Types

Somehow I'm only down to 7 type errors, this is incredible! I really did work all day.

Alright, with this one, I made type definitions for the old version of Num Text, and I added them as a devDependency here, so it will use them right in STE's TSC checks!

Installed it right from GitHub, super cool. I did that back with MCRegionJS and Gamedata-Parser I think, so this is a nice refresher to try that out again.

https://stackoverflow.com/questions/16350673/depend-on-a-branch-or-tag-using-a-git-url-in-a-package-json/31554583#31554583

Listened to Stupid Dream for most of this one, just over 1 time around (1.25 maybe).

Thanks to the new type definitions, it pointed out a few other fixes I could also make, so I did those too. The last 7 errors all have to do with Menu Drop types, so I'm gonna do the same thing as Num Text for the legacy version of that too. That'll be for tomorrow though, I think I'm all brained out for the day.

It was rainy today after work, so I stayed inside and coded pretty much all day. It was a nice recharge on that front. I need some of those days every once in a while, to just chug out all of your ideas and things. I think after this big burst of coding energy, I may have one for music again too, at least that's what I want too. I've found that I work my best when I listen to what I want and don't want to do. If I try and force what I "need" to do, like in terms of my personal goals, then it doesn't hit home like it does when I really mean it. I try to follow those, and I seem to be working really well with that. I think it's important to give yourself time for things, there's so much going on, your mind just might not be set up for that thing yet. Just wait a little while! I like doing that with albums too.

I really have been planning an STE rework like this for more than a year now, I think having TypeScript in my toolbelt made this possible. There were way too many things to handle without it. I think my experience from the past year in general has really helped me step up a few levels. Even when you want to keep working on a cool thing, sometimes it just needs a breather from you. Just let it have it's time, see what happens.

I have buckets in the morning again tomorrow, so I'm making this the last commit for the night. That's it! It's time for that breather I was talking about. If you work on it too long, it starts to turn stale.

Started with Slave Called Shiver, listened all the way to that again, finishing with Baby Dream In Cellophane. I really like This Is No Rehearsal, the whole album for that matter. It also was one that had to grow on me. I think I listened to it first about a year ago or so (not sure when it was), but I didn't pick it up again for a few months/weeks. Now I own it! I'm gonna try out Future Bytes again eventually too, I really liked Personal Shopper.

Ok, gn! I'm so excited for all of the things I'm planning on! Even for buckets in the morning :)

*Edit: That was 7 errors in the main app script, there's 6 more in the Editor script, so down to 13, and they all are only from the Menu Drop types. Noice!
Ok, closing down this commit, at 12:43.

---
## [Offroaders123/Smart-Text-Editor](https://github.com/Offroaders123/Smart-Text-Editor)@[a0b78275f4...](https://github.com/Offroaders123/Smart-Text-Editor/commit/a0b78275f4882cfd746d7ab2a25b2630878e5494)
#### Wednesday 2023-02-22 08:55:22 by Offroaders123

Editor Object Rehash

- I'm actually coming back to write this after the commit that's after this one, a reflective message I guess

To start this typing journey off, I started with the Editor script, to improve the typing for the app with the base Editor object, which is a big ugly state handling thing, which may need to be poked a little bit, this guy has got to go. It's too big as of now, gonna make things way more modular after I get everything typed out. Everything relies on each other thing in a bunch of weird ways, and that's hard to keep track of. The typings are gonna do wonders to help with that, they already have while doing this even! Some of the original code was just ugly to my older coder eyes, this little reword tidied things up that I've been meaning to do for a while now.

The class-nature of the Editor object is merely for strict typing, it's not for inheritance or anything. Just to initially get things typed out faster, it works nicely to define all of the properties as static members on the class, rather than having to make a huge interface for the object, in JSDoc or a `.d.ts` file. It's all in once place.

As of now, STE isn't going to be TypeScript quite yet, but I can only imagine moving to it, inevitably. It's so cool what you can do with it, I'm definitely not gonna put it past me for doing that, once the codebase gets to a state to be able to move to it easily (that's not too far away actually).

I. Love. TypeScript. (or, TSC and JSDoc hehe)

Oh yeah, and the weird dynamic object generation setup on the old Editor object was because I didn't know how to make my own getter functions, so that's what I came up with to get "dynamic properties". I'm very happy with how smart I was (for myself back then at least, lol) to being able to figure that out, so it worked very nice as a fill in before finding the more streamlined way of achieving something like that.

---
## [LazennG/bad-idea-box](https://github.com/LazennG/bad-idea-box)@[818973e1e9...](https://github.com/LazennG/bad-idea-box/commit/818973e1e91edd0d62357f0ca4361916fb1d3f69)
#### Wednesday 2023-02-22 08:59:50 by wejengin2

fixes some issues in infiltrator base (#17861)

* huh

* man

* adds griddle

* that's really funny but fuck you

---------

Co-authored-by: Byemoh <baiomurang@gmail.com>

---
## [TropicalFlak/cmss13](https://github.com/TropicalFlak/cmss13)@[7d27d8508c...](https://github.com/TropicalFlak/cmss13/commit/7d27d8508ce0723dbbcf1dfad9810a3092a71f61)
#### Wednesday 2023-02-22 09:01:04 by TotalEpicness

Fixes invincible base crusher (#2682)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
Fixes an oversight that allowed base crusher to have half it's intended
shield cooldown
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.
runs
Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
Never intended on the first place and led to crusher being busted as
fuck as it is currently.

This was never intended and was a mess up on my part. It fell through
from the painfully long development that Charger had as months went by
between testing sessions and TMs, along with my inexperience with larger
projects and bad note taking at the time.

Maintainers are also supposed to filter stuff like this but after like a
billion code reviews Charger had, I can see how it got through on their
end as well.

Nevertheless this dies here. 

funny contrib moment
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
it runs
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

:cl: Totalepicness
balance: Fixes base crusher having half it's intended cooldown for the
shield ability
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

Co-authored-by: Epicness <coolguyethanw@gmail.com>

---
## [Lambda-13/rustest](https://github.com/Lambda-13/rustest)@[6d158bd3b3...](https://github.com/Lambda-13/rustest/commit/6d158bd3b37bba2cb2cec2a27fdb0b9b7d8275ac)
#### Wednesday 2023-02-22 09:11:46 by spockye

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
## [git-for-windows/git](https://github.com/git-for-windows/git)@[55d783e25a...](https://github.com/git-for-windows/git/commit/55d783e25ab4871087dcd0e1d2353a3ecc633fd0)
#### Wednesday 2023-02-22 09:11:52 by Johannes Schindelin

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
## [ZephyrTFA/tgstation](https://github.com/ZephyrTFA/tgstation)@[ef335f7d1f...](https://github.com/ZephyrTFA/tgstation/commit/ef335f7d1f33d196062a5a285c7f7216df2302a6)
#### Wednesday 2023-02-22 09:23:04 by Rhials

It Came From Outer Spess: Adds midround changelings, delivered by an absolutely disgusting changeling meteor (#73018)

## About The Pull Request

Adds a new dynamic midround opportunity and random event - Space
Changeling.


https://user-images.githubusercontent.com/28870487/215284465-f5c5c1b1-b83d-471a-89be-1b65a4d2f2d4.mp4

If you are fortunate enough to recieve this role, you will be stuffed
into a changeling meteor and hurled at the side of the station. With no
crew identities, no access, and no equipment, you'll have to rely on
your **free** organic space suit and armblade to infiltrate the station
and get settled.

With no disguises to fall back on, the midround changeling experience
may lead to some very unfavorable situations. It's not unlikely that
you'll be spotted making your way inside, or that someone will see the
impact site and cause a panic. This role is not easy, but keep in mind
that you also have nothing to lose in the event that you use Lesser
Form/Headslug.

Aside from the starting circumstances, you have the same objectives and
capabilities as a roundstart changeling. Getting inside of the station
will be the hard part, but from there you can do what changelings do
best and blend in.

<details>
<summary>A brief note on the free stuff you get:</summary>
<br>
You get the organic space suit and armblade for free. The space suit is
absolutely vital, but I decided that the armblade should be given for
free as well. It's necessary for breaking open windows or airlocks and
getting access to the station, since otherwise your options are limited
to arrivals/departures. Having to pay a 2 point tax to avoid walking
naked into the main hallways of the station and getting gibbed is lame,
and with the added difficulty of the role I think it's fair.
</details>

Also, this is my 100th PR here! :)

## Why It's Good For The Game

Adds midround changelings in a WAY COOLER way than just making a random
crew/new arrival a changeling.

Lets people experience Hardmode Changeling, and test the adaptability
and flexibility of the most versatile antagonist even harder than
before. Losing the option to bypass the whole shape-shifter thing by
disguising as your crew identity presents a welcome change to the
formula.

Adds a teensy bit more midround variety, so we stop getting Nightmare At
The Thirty Minute Mark every round.
## Changelog
:cl: Rhials
add: Midround changeling spawn event.
add: Changeling meteor. It has a present for you.
/:cl:

---
## [fc1943s/The-Spiral-Language](https://github.com/fc1943s/The-Spiral-Language)@[eabde6dbf3...](https://github.com/fc1943s/The-Spiral-Language/commit/eabde6dbf3b8fd57acb4f5c7aa36d32e0bde0820)
#### Wednesday 2023-02-22 09:23:37 by Marko Grdinić

9:15am. I am up.

9:20am. I've been thinking a lot about the backend. I see I didn't get an answer on which outer backend to use.

Anyway.

Views are at 4,998. Avg at 122.

That shit review is still taking my rating, the report did nothing. The latest chapters have experience as sharp drop in readership. My future is pitch black. And I might just be getting scammed in doing free work for UPMEM.

9:35am. Maybe 30 followers is my limit. They seem to be hard to get.

Anyway, let me just read Fabiniku and that TS High School chapter and then I will watch the PIM course video related to UPMEM. Yesterday I had time to look at the docs and get familiar with its programming model. Since this is not the kind of device that I'd be interested in programming personally - I really want small communicating cores so I can do AI instead, I'll do it slowly. I do not feel like just dropping everything to satisfy that guy's whims. Who knows if the job opening in the future will even be remote or if what I will do here will impress him.

The main challenges will be to make the Python + ref countless C backend and then to make the UPMEM functions callable. I have to do a bunch of things to deal with global variables and the like.

Spiral is not a good fit for UPMEM devices because you can't actually free the memory you allocate in its programs. So ref counting is useless due to that.

9:55am. https://www.youtube.com/playlist?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy
PIM (Processing-In-Memory) Course

Let me get started with this. I'll slowly get a grip on the PIM programming model.

https://youtu.be/p_sLhKeo6ys?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy
PIM Course: Lecture 3: Real-world PIM: UPMEM PIM - Fall 2022

Let me start with this and then I will watch the lecture on programming these things.

https://sdk.upmem.com/2021.4.0/031_DPURuntimeService_Memory.html
> A buddy allocator uses a pre-allocated area in the heap to perform dynamic allocation and freeing of buffers, offering functions similar to standard malloc and free.

Actually, I could use this for just things like closures and union types.

///

Allocate buffers, using buddy_alloc, with the following restrictions:
* Allocated buffer size should not exceed 4096 bytes
* Minimum size of allocated buffers is 32 bytes
* Allocated buffers are automatically aligned on DMA-transfer size, so that they can be used to transfer data from/to MRAM

///

I've been too fast to discount them. I mean, this amount would be more than enough for any kind of closure or union type.

Yeah, I am getting bearish and pessimistic far too easily. I should be able to make good things happen with the buddy allocator.

I do not need to get rid of the ref counting from the UPMEM C backend.

That should make it a lot more valuable. Yeah, this is what happens when you make decisions far too quickly. You end up with delusions. The buddy allocator is great. 4k is a huge max limit that I can expect to never reach in realistic scenarios.

Though, I am not sure what to do about allocating arrays.

...Well, I'll just limit them to 4k then. It doesn't matter, this is just a demo. If more is needed the devs can hash it out. The user can use the regular allocator if he really needs a ton of WRAM.

https://youtu.be/p_sLhKeo6ys?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=275

Let me get back to watching this.

https://youtu.be/p_sLhKeo6ys?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=680

64kb WRAM...Yeah, it makes no sense to go beyond 4k if the total memory size is only 64kb.

10:30am. After I am done with these videos, I will check out the Safari benchmark code. I want to see how they do it.

11am. https://youtu.be/7c6x5GJG6dw?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy
PIM Course: Lecture 4: Real-world PIM: Microbenchmarking of UPMEM PIM - Fall 2022

I'll watch this and the programming lecture, and then I am done for the day.

Right now I am thinking how I should handle the `with` statement in Python. It is so annoying, but I might have to extend the language. I'll think I'll just skip it. The `with` statement can ensure that the resources are freed on error, but it does not matter for the demo. I'll just skip it. The del insertion can ensure the resources are freed.

11:35am. https://www.quantamagazine.org/how-the-brain-distinguishes-memories-from-perceptions-20221214/

I'll read this later. Focus me.

11:50am. https://github.com/upmem/dpu_demo/blob/sdk-2021.3/checksum/host/host.py#L64

I am looking at some example code here.

One thing I do not understand is whether MRAM has to be statically declared in the code ahead of time. I'll delay asking the lead compiler dev about it until I watch the lectures.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy
PIM Course: Lecture 9: Programming PIM Architectures - Fall 2022

Let me finally watch this.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=196

They can bee seen as a loosely coupled accelerator.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=485

As I gleamed so far, the library actually allocates DPUs themselves instead of blocks of memory.

12:20pm. https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=752

Here it explains the transfers. This is a good tutorial.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=777

Ah, I see. This is how dynamic allocation could work. It is quite rough.

...Still, does this have any alignment requirements?

https://sdk.upmem.com/2021.4.0/032_DPURuntimeService_HostCommunication.html#communication-with-host-applications

///

dpu_copy_from(struct dpu_set_t set, const char *symbol_name, uint32_t symbol_offset, void *dst, size_t length) to copy a buffer from a single DPU
dpu_broadcast_to(struct dpu_set_t set, const char *symbol_name, uint32_t symbol_offset, const void *src, size_t length, dpu_xfer_flags_t flags) to broadcast a buffer to a set of DPUs
dpu_push_xfer(struct dpu_set_t set, dpu_xfer_t xfer, const char *symbol_name, uint32_t symbol_offset, size_t length, dpu_xfer_flags_t flags) to push different buffers to a set of DPUs in one transfer.

///

Oh they literally have symbol names here.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=1189

Let me backtrack just a bit.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=793

https://sdk.upmem.com/2021.4.0/202_RTL.html#buddy-alloc

> The allocated buffer is aligned on 64 bits, in order to ensure compatibility with the maximum buffer alignment constraint. As a consequence, a buffer allocated with this function is also compatible with data transfers to/from MRAM.

> Due to the idea of the buddy algorithm (to decrease external fragmentation), the allocated blocks will be of size equal to a power of 2. In other words, if the user allocates 33 bytes, 64 bytes will be allocated and when 2049 bytes are requested, 4096 will be allocated. The user might want to take this into account if she/he wishes to minimise the memory consumption.

> The minimal size of the allocated block is 16 bytes, but can easily be changed in future implementations, so buddy_alloc is mostly adapted to allocating medium and big structures, such as arrays containing more than 8 bytes (in order to make sure that not too much memory space is wasted), binary trees or linked lists.

The minimum here is different from what the other parts of the doc say.

https://sdk.upmem.com/2021.4.0/CAPILowLevel/dpu__memory_8h.html#a66e9ccbcd5ec3f7767441a0926f24538

Here is copy_to_mram. It is different from in the slides.

The docs are somewhat incomplete.

https://sdk.upmem.com/2021.4.0/031_DPURuntimeService_Memory.html
The source or target address in MRAM must be aligned on 8 bytes. Developers must carefully respect this rule since the Runtime Library does not perform any check regarding this point.

When doing transfers I need to make sure MRAM pointers are aligned as well. This could result in difficulties if I am just pushing offets around.

12:50pm. Let me stop here. I keep jumping back and forth, thinking about my ideas.

I am going to open an issue somewhere, asking thme about variable length arrays. So far all the examples only have statically allocated ones.

Let me do the chores here.

1:40pm. Breakfast first.

2:05pm. Akiba Maid War. In this ep it seems Ranko dies.

3:30pm. Damn, she is really gone.

Let me finish watching the lecture and then I will post a question on UPMEM repo, one of them, as to how variables be passed into the kernel.

Focus me. Let me get this out of the way today. While I wait for the question tomorrow, I'll continue to write.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=1357

These transfers are pretty slow.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=1485

I am not sure what is meant by this.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=1715
> How To Pass Parameters To The Kernel

Yes, this is exactly what I wanted to know! How?

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=1758

This explains the host.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=1806

I am finally at the level where I can look at this and understand it. Holy shit is this complex.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=1807

I am just looking at this and thinking. I am going to have to take a look at the vector addition code to see whether they are viable length or not.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=1768

What is this, `dpu_arguments_t`? I'll find that out later.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=2616

I need to check these examples out.

https://youtu.be/zF70xuhesME?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy&t=2737

Here is the link.

https://youtu.be/H_xvB_O-bWM?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy
PIM Course: Lecture 10: Benchmarking and Workload Suitability on PIM - Fall 2022

This one I'll skip.

https://github.com/CMU-SAFARI/prim-benchmarks

Let me check out vector addition.

https://github.com/CMU-SAFARI/prim-benchmarks/tree/main/VA

https://github.com/CMU-SAFARI/prim-benchmarks/blob/main/VA/support/common.h

///

// Structures used by both the host and the dpu to communicate information
typedef struct {
    uint32_t size;
    uint32_t transfer_size;
	enum kernels {
	    kernel1 = 0,
	    nr_kernels = 1,
	} kernel;
} dpu_arguments_t;

///

So it is like this.

Anyway now that I see this, I can be sure they are using C on the host side.

4:25pm. Now I am lightly cruising the Akiba Maid War thread. Let me just read it for a bit and then I will check out the host side.

4:55pm. __host dpu_arguments_t DPU_INPUT_ARGUMENTS;

I think I could just pass in the array pointer through here.

5:10pm.

///

    uint32_t mram_base_addr_A = (uint32_t)DPU_MRAM_HEAP_POINTER;
    uint32_t mram_base_addr_B = (uint32_t)(DPU_MRAM_HEAP_POINTER + input_size_dpu_bytes_transfer);

///

Wait, now that I think about it, the UPMEM chip should have 8gb. How can the full space then be accessed using 32-bit adresses?

5:15pm. I am think I am starting to grasp the way to pass in the data...

Let me check out the docs again. It is amazing that the most difficult part of UPMEM is how to pass data into it. What the hell were these guys thinking when they designed this?

Now I am starting to see what was meant when I read that AI startups are flailing on the software.

> __mram_ptr which enable to use a pointer on a MRAM variable or declare a extern MRAM variable.

What is an extrern MRAM variable?

> A special MRAM variable is defined in mram.h: DPU_MRAM_HEAP_POINTER. It defines the end of the memory range used by the MRAM variables. The range from DPU_MRAM_HEAP_POINTER to the end of the MRAM can be used freely by a DPU program, for example to handle dynamically-sized MRAM arrays.

This is what I need for dynamic arrays.

> The symbol_name argument consists of a name of a variable in the DPU code. It can be either a MRAM variable (with the __mram or __mram_noinit attribute) or a WRAM variable (with the __host attribute). Other variables are not visible to the host application.

Right. MRAM is __mram and WRAM vars are __host.

I am betting I could have both __host and __mram_ptr together. Something like `__host __mram_ptr int32_t * a;`.

5:45pm. https://github.com/upmem/dpu_demo/issues/
How can UPMEM DPUs access 8gb of memory when they are 32-bit?

Opened issue 13 here.

6:05pm. I am writing some private correspondence. I am not going to post it here, even though it doesn't really matter. I need to stop blabbing about everything in the commits if I am going to be a pro.

6:25pm. Ok, that is basically it.

The C backend should be mostly fine, I can leave it as is. I'll have to make some changes so arrays are handled properly.

Lunch...

7pm. Right now I am thinking how to deal with arrays.

Arrays, arrays...you know what? I should just take them out in the UPMEM Python backend. In the UPMEM C backend, they can be local arrays. That will allow me to easily serialize them. Enough of their horseshit.

I only needed them back in the old Spiral for the sake of typechecking. Now that I have global type inference, they are much less necessary.

I am thinking. What I need to work next is the Python backend. No doubt about it. I'll keep the del insertion from the Cython backend, but otherwise it will be a pure Python backend. PyPy will like what I give it.

I think I might just remove the Cython one altogether as it is such an eyesore.

This kind of refactoring will take some effort, but the Cython backend is simply unacceptable. A decently sized program takes ages to compile and is barely faster than native Python. Though it was useful for testing Spiral v2 back when it came out, that sort of thing is not necessary anymore.

7:10pm. Yeah, I should take this on. A Python backend will end up being useful for other PIM and AI chip devices in the future.

7:20pm. I know that it would be great if I could just dive in and do the UPMEM backend right away, but I should take some care to do the Python backend properly. Then I will extend it.

I'll have to put in the with statement into the language as it is so ubiquitous in Python.

https://learn.microsoft.com/en-us/dotnet/fsharp/language-reference/resource-management-the-use-keyword

Or actually, why not make it like this? Rather than immitate Python, why not immitate F#?

7:30pm. Damn, now I have to worry about this. Let's just not worry about it.

I should consider the `use` and `using` statements once the Python backend is done.

Maybe I should give it a break tomorrow, but I should start with a radical cleanup of the Cython backend. For del insertion, I should definitely take a look at how I am doing the analysis in the C backend. I remember it being really confusing in the Cython backend.

I'll have to refresh my memory. So much of the compiler has faded from it.

I do not know whether the UPMEM compiler lead who contacted me will just ghost it after he realizes that interacting with me will be more than 5 minutes of work, I've had plenty of such interaction in the past, but either way I should just do this and use it as a chance to advertize Spiral. Ultimately, my desire to work on novel hardware has not faded.

7:40pm. Now forget that. Let me read KenDeshi. Tomorrow I will do some writing and then slowly start. I should aim to split my time between the two.

I'll go back to blogging on the Spiral repo, I see that doing it on Patreon is doing me no good.

---
## [fc1943s/The-Spiral-Language](https://github.com/fc1943s/The-Spiral-Language)@[4d4c3b99ef...](https://github.com/fc1943s/The-Spiral-Language/commit/4d4c3b99ef904ddc62127cc3ab52ef7e07bd12d5)
#### Wednesday 2023-02-22 09:23:37 by Marko Grdinić

"8:45am. I am up. Let me just do some of the programming necessities I thought up over the night. I screwed up some things.

```fs
    let g_suppr : Dictionary<TypedBind, TyV Set> = Dictionary(HashIdentity.Reference)
    let g_decr : Dictionary<TypedBind, TyV Set> = Dictionary(HashIdentity.Reference)
    let g_incr : Dictionary<TypedBind, TyV Set * bool> = Dictionary(HashIdentity.Reference)

    let incref_cancellation () =
        let g_incr' : Dictionary<TypedBind, TyV Set> = Dictionary(HashIdentity.Reference)
        g_incr |> Seq.iter (fun kv ->
            let add (d : Dictionary<TypedBind, TyV Set>) x = if Set.isEmpty x then () else d.[kv.Key] <- x
            let f (g : Dictionary<_,_>) = match g.TryGetValue(kv.Key) with true, x -> x | _ -> Set.empty
            let decr, suppr = f g_decr, f g_suppr
            let incr, is_in_container = kv.Value
            let g a b = a - b, b - a
            let incr, suppr = g incr suppr
            let incr, decr = if is_in_container then g incr decr else incr, decr
            add g_incr' incr; add g_suppr suppr; add g_decr decr
            )
        {g_decr=g_decr; g_suppr=g_suppr; g_incr=g_incr'}
```

Remember how I said I should not optimize? Well, I went and did it. And as a result the code is broken. I only realized during the night that if the input to add is empty, it won't clear the existing set. Whops.

```fs
open System.Collections.Generic
let a = Dictionary()
a.Add("qwe",true)
a.Remove("qwe")
```

Ah, I see, this will in fact remove the key and return a bool as to whether it has been returned.

8:55am.

```fs
    let incref_cancellation () =
        let g_suppr' : Dictionary<TypedBind, TyV Set> = Dictionary(g_suppr.Count, HashIdentity.Reference)
        let g_decr' : Dictionary<TypedBind, TyV Set> = Dictionary(g_decr.Count, HashIdentity.Reference)
        let g_incr' : Dictionary<TypedBind, TyV Set> = Dictionary(g_incr.Count, HashIdentity.Reference)
        for KeyValue(k,(incr,is_in_container)) in g_incr do
            let f (g : Dictionary<_,_>) = match g.TryGetValue(k) with true, x -> x | _ -> Set.empty
            let decr, suppr = f g_decr, f g_suppr
            let g a b = a - b, b - a
            let incr, decr = if is_in_container then g incr decr else incr, decr
            let incr, suppr = g incr suppr
            let add (d : Dictionary<TypedBind, TyV Set>) x = if Set.isEmpty x then () else d.[k] <- x
            add g_incr' incr; add g_decr' decr; add g_suppr' suppr
        {g_incr=g_incr'; g_decr=g_decr'; g_suppr=g_suppr'}
```

Let me go with this. Now it is super clean. This is the easiest way to think about it. The other consideration I thought of during the night, whether the refc are printed in the incref, decref, suppref order is fine.

9am. Perfect. Now...

///

Another question for Monday.

> In other words, each tasklet only has direct access to a subset of the overall DIMM memory space, which is less than 8gb (in current generations), so the 32-bit limitation doesn't matter.

Sorry, I wasn't reading what you wrote here properly yesterday. I was under the impression that each each tasklet has access to the entirety of MRAM for it rank which 8gb. Is my assumption wrong? I know you can give tasklets their stack size, but all the MRAM partitioning that I've seen being done is my pushing offsets.

Also are the MRAM pointers 32 or 64 bit? I've been assuming they are 32-bit, but if they are 64-bit that would explain a lot.

///

Let me try fielding this again.

9:15am. Now let me chill.

Ugh, my readership is falling off a cliff in ch 12. Do I want to write or do I want to program.

Let me read Knight Run and a chapter of Otome Survival. Then I will check whether indent works properly in the two backends.

9:25am. https://boards.4channel.org/a/thread/246448142/villain-does-nothing-wrong#p246450907

///

>>246450139
he'd absolutely keep inventing new forms of 'death' that he needs to go on an epic thousand years quest to become immune to
>black holes become theorized
>oh fuck oh fuck oh shit I need to become immune to gravity RIGHT NOW

///

Based.

https://boards.4channel.org/a/thread/246448142/villain-does-nothing-wrong#p246450811

The evil is the ultimate cuckoldry post is worth saving as well.

Ah, fuck it. I do not feel like reading Otome Survival. Let me check out the AyaTri thread and then I will finally check the indent. Also Knight Run.

10:05am. Let me get started.

Let me try out indent.

You know, I just realized, if I want this I do not even need the indent.

For example, I can just pass in a closure. Let me show what I mean in Python.

```py
def with_(x,f): with x() as tmp: return f(tmp)
```

I can just print this as a global statement. Though it wouldn't be as elegant as what I want to do now...

10:20am. You know, rather than let this bother me, I should just dive right in.

10:25am. Yeah, you know what.

```py
def with_(x,f): with x() as tmp: return f(tmp)
```

It is not ideal, but I am going to go with this. This will result in needless closure allocation and such, but language statements really have to put into the parser and then everywhere else. It would really be nasty to keep writing those macros and indents everywhere.

Let me get rid of Indent.

But first, let me just commit here, since I fixed the bug from yesterday night."

---
## [fc1943s/The-Spiral-Language](https://github.com/fc1943s/The-Spiral-Language)@[aef93c4854...](https://github.com/fc1943s/The-Spiral-Language/commit/aef93c485489ff98839f615e4ed391cc6b2b9399)
#### Wednesday 2023-02-22 09:23:37 by Marko Grdinić

"7:10pm. Time to rest and relax. Tomorrow I'll crack that Python codegen.

https://youtu.be/PDVlri6HUwc?list=PLcMKLtS9oWYFJ0o2bAc-Bh5e7kSnpCAl6&t=791

This OST is banger.

12/19/2022

10:30am. Damn, I slept in late. Let's see, did I get any reply yet from the UPMEM guy? Ah, it was from 3 days ago. Damn, I should have checked it.

Sent him an email as well notified him on Reddit.

Now, let me just chill a little and I will get on with it.

10:55am. MahoAko and Saki are out. Let me read them and then I'll get started on the Python backend.

https://boards.4channel.org/a/thread/246488029/thoughts-on-ai-generated-manga-plots-and-art

They are working on manga drawing AI already in Tezuka's style.

https://boards.4channel.org/a/thread/246488029/thoughts-on-ai-generated-manga-plots-and-art#p246488313

The way it captured Tezuka's style is amazing. This ability to seamlessly immitate styles is the kind of ability I'd most like to have had as a human. It is way beyond my talent.

11:25am. Let me start.

```fs
    let rec binds_start (args : TyV []) (s : CodegenEnv) (x : TypedBind []) = binds (Codegen.C.refc_prepass' false (Set args) x).g_decr s BindsTailEnd x
    and binds g_decr (s : CodegenEnv) (ret : BindsReturn) (stmts : TypedBind []) =
        failwith ""
```

This is a good way to start things off. Yeah.

11:45am. Ugh.

```fs
    and binds' (defs : CodegenEnv) (x : TypedBind []) =
        let s = {defs with text = StringBuilder()}
        binds (nullable_vars_of x) defs s (BindsTailEnd(binds_last_data x |> data_term_vars |> Array.isEmpty)) x
        defs.text.Append(s.text) |> ignore
    and binds_loop (nulls : Dictionary<obj,Tag Set>) (defs : CodegenEnv) (s : CodegenEnv) ret (stmts : TypedBind []) =
        let rec loop i =
            if i < stmts.Length then
                let inline op a b c d = function
                    | TyFailwith(_,b) -> line s $"raise Exception({tup b})"; false
                    | e -> op a b c d e; true
                let x = stmts.[i]
                match x with
                | TyLet(d,trace,a) ->
                    try let d = data_free_vars d
                        Array.iter (fun (L(i,t)) -> cdef_show "" defs i (tyv t)) d
                        op nulls defs s (BindsLocal d) a
                    with :? CodegenError as e -> raise_codegen_error' trace e.Data0
                | TyLocalReturnOp(trace,a,_) ->
                    try op nulls defs s ret a
                    with :? CodegenError as e -> raise_codegen_error' trace e.Data0
                | TyLocalReturnData(d,trace) ->
                    try match ret with
                        | BindsLocal [||] | BindsTailEnd true -> if i = 0 then line s "pass"
                        | BindsTailEnd false -> line s $"return {tup d}"
                        | BindsLocal ret -> line s $"{args ret} = {args' d}"
                    with :? CodegenError as e -> raise_codegen_error' trace e.Data0
                    true
                |> function
                    | true -> print_nullables nulls s x; loop (i+1)
                    | false -> ()
        loop 0
```

Why am I passing booleans around in the Cython backend? Yeah, literally nobody is going to understand this. That is why I hate the backend so much. It started off well, but then I had to put in so many hacks. And as punchline at the end, its general performance is shit. Being 2x faster than Python does not mean much when the compilation times are destroyed and Python is already 1,000x slower than it should be anyway.

11:55am. Let me just combine the C and the F# backends.

```fs
    and binds (s : CodegenEnv) (x : TypedBind []) =
        Array.iter (function
            | TyLet(d,trace,a) -> try op s (Some d) a with :? CodegenError as e -> raise_codegen_error' trace e.Data0
            | TyLocalReturnOp(trace,a,_) -> try op s None a with :? CodegenError as e -> raise_codegen_error' trace e.Data0
            | TyLocalReturnData(d,trace) -> try line s (tup d) with :? CodegenError as e -> raise_codegen_error' trace e.Data0
            ) x
```

Look at how clean it is.

```fs
    let rec binds_start (args : TyV []) (s : CodegenEnv) (x : TypedBind []) = binds (Codegen.C.refc_prepass' false (Set args) x).g_decr s BindsTailEnd x
    and binds g_decr (s : CodegenEnv) (ret : BindsReturn) (stmts : TypedBind []) =
        Array.iter (fun x ->
            let _ =
                let f (g : Dictionary<_,_>) = match g.TryGetValue(x) with true, x -> Seq.toArray x | _ -> [||]
                (f g_decr) |> Seq.map (fun (L(i,_)) -> $"del v{i}") |> line' s
            ()
            ) stmts
```

This is a good way to start it off.

12:10pm.

```fs
let lit = function
    | LitInt8 x -> sprintf "(<signed char>%i)" x
    | LitInt16 x -> sprintf "(<signed short>%i)" x
    | LitInt32 x -> sprintf "(<signed long>%i)" x
    | LitInt64 x -> sprintf "(<signed long long>%i)" x
    | LitUInt8 x -> sprintf "(<unsigned char>%i)" x
    | LitUInt16 x -> sprintf "(<unsigned short>%i)" x
    | LitUInt32 x -> sprintf "(<unsigned long>%i)" x
    | LitUInt64 x -> sprintf "(<unsigned long long>%i)" x
    | LitFloat32 x ->
        if x = infinityf then "(<float>float('inf'))"
        elif x = -infinityf then "(<float>float('-inf'))"
        elif Single.IsNaN x then "(<float>float())"
        else sprintf "(<float>%s)" (x.ToString("R") |> add_dec_point)
    | LitFloat64 x ->
        if x = infinity then "(<double>float('inf'))"
        elif x = -infinity then "(<double>float('-inf'))"
        elif Double.IsNaN x then "(<double>float())"
        else sprintf "(<double>%s)" (x.ToString("R") |> add_dec_point)
    | LitString x ->
        let strb = StringBuilder(x.Length+2)
        strb.Append '"' |> ignore
        String.iter (function
            | '"' -> strb.Append "\\\""
            | '\b' -> strb.Append @"\b"
            | '\t' -> strb.Append @"\t"
            | '\n' -> strb.Append @"\n"
            | '\r' -> strb.Append @"\r"
            | '\\' -> strb.Append @"\\"
            | x -> strb.Append x
            >> ignore
            ) x
        strb.Append '"' |> ignore
        strb.ToString()
    | LitChar x ->
        match x with
        | '\b' -> @"\b"
        | '\n' -> @"\n"
        | '\t' -> @"\t"
        | '\r' -> @"\r"
        | '\\' -> @"\\"
        | x -> string x
        |> sprintf "'%s'"
    | LitBool x -> if x then "1" else "0"
```

Sure is nasty. Let me clean this up.

```fs
let lit = function
    | LitInt8 x -> sprintf "%i" x
    | LitInt16 x -> sprintf "%i" x
    | LitInt32 x -> sprintf "%i" x
    | LitInt64 x -> sprintf "%i" x
    | LitUInt8 x -> sprintf "%i" x
    | LitUInt16 x -> sprintf "%i" x
    | LitUInt32 x -> sprintf "%i" x
    | LitUInt64 x -> sprintf "%i" x
    | LitFloat32 x ->
        if x = infinityf then "float('inf')"
        elif x = -infinityf then "float('-inf')"
        elif Single.IsNaN x then "float()"
        else x.ToString("R") |> add_dec_point
    | LitFloat64 x ->
        if x = infinity then "float('inf')"
        elif x = -infinity then "float('-inf')"
        elif Double.IsNaN x then "float()"
        else x.ToString("R") |> add_dec_point
    | LitString x ->
        let strb = StringBuilder(x.Length+2)
        strb.Append '"' |> ignore
        String.iter (function
            | '"' -> strb.Append "\\\""
            | '\b' -> strb.Append @"\b"
            | '\t' -> strb.Append @"\t"
            | '\n' -> strb.Append @"\n"
            | '\r' -> strb.Append @"\r"
            | '\\' -> strb.Append @"\\"
            | x -> strb.Append x
            >> ignore
            ) x
        strb.Append '"' |> ignore
        strb.ToString()
    | LitChar x ->
        match x with
        | '\b' -> @"\b"
        | '\n' -> @"\n"
        | '\t' -> @"\t"
        | '\r' -> @"\r"
        | '\\' -> @"\\"
        | x -> string x
        |> sprintf "'%s'"
    | LitBool x -> if x then "True" else "False"
```

Now it is fine.

12:15pm. Since I will be using Python's native tuples, the returns will be much simplified.

12:30pm.

```fs
    let rec binds_start (args : TyV []) (s : CodegenEnv) (x : TypedBind []) = binds (Codegen.C.refc_prepass' false (Set args) x).g_decr s BindsTailEnd x
    and binds g_decr (s : CodegenEnv) (ret : BindsReturn) (stmts : TypedBind []) =
        let tup_destruct (a,b) =
            if 0 < Array.length a then
                let a = Array.map (fun (L(i,_)) -> $"v{i}") a |> String.concat ", "
                let b = Array.map show_w (data_term_vars b) |> String.concat ", "
                sprintf "%s = %s" a b |> line s
        Array.iter (fun x ->
            let _ =
                let f (g : Dictionary<_,_>) = match g.TryGetValue(x) with true, x -> Seq.toArray x | _ -> [||]
                (f g_decr) |> Seq.map (fun (L(i,_)) -> $"del v{i}") |> line' s
            match x with
            | TyLet(d,trace,a) ->
                try op g_decr s (BindsLocal (data_free_vars d)) a
                with :? CodegenError as e -> raise_codegen_error' trace e.Data0
            | TyLocalReturnOp(trace,a,_) ->
                try op g_decr s ret a
                with :? CodegenError as e -> raise_codegen_error' trace e.Data0
            | TyLocalReturnData(d,trace) ->
                try match ret with
                    | BindsLocal l -> tup_destruct (l, d)
                    | BindsTailEnd -> line s $"return {tup_data d}"
                with :? CodegenError as e -> raise_codegen_error' trace e.Data0
            ) stmts
    and op g_decr s (ret : BindsReturn) a =
        failwith ""
    and tup_term_vars x =
        let args = Array.map show_w x |> String.concat ", "
        if 1 < x.Length then sprintf "(%s)" args else args
    and tup_data x = tup_term_vars (data_term_vars x)
```

Perfect. It couldn't be any better. Most of the Ops I can just copy from the Cython backend.

Let me have breakfast here."

---
## [fc1943s/The-Spiral-Language](https://github.com/fc1943s/The-Spiral-Language)@[4cd592edfe...](https://github.com/fc1943s/The-Spiral-Language/commit/4cd592edfea836ff7d35bfb5ad131ad306f8a0fb)
#### Wednesday 2023-02-22 09:23:37 by Marko Grdinić

"2:15pm. I am feeling dizzy from all the thinking and the chores. Finally I can enjoy breakfast for a bit. Now that I've had time to compare programming and writing, they are not close in terms of intensity.

2:35pm. https://huggingface.co/dreamlike-art/dreamlike-diffusion-1.0

I'll keep this model in mind for when I get back to prompting.

3:20pm. No replies yet. Are the questions I am asking difficult? Probably he just has work to take care of. It will take a few more days before I have the first backend operational, so it is no big deal.

3:25pm. Right now, let me focus on testing out the new C backend. I have faith in the refc passes, but all the changes to the codegen might have wrecked something by accident. I'll know right away when I look at the diffs.

```c
void HeapDecref0(Heap0 * x){
    if (x != NULL && --(x->refc) == 0) { HeapDecrefBody0(x); free(x); }
    }
}
Heap0 * HeapCreate0(bool v0){
    Heap0 * x = malloc(sizeof(Heap0));
    x->refc = 1;
    x->v0 = v0;
    v0->refc++;
    return x;
}
```

Some borken syntax and bools being incref'd.

```fs
            | REFC_INCR ->
                match t' with
                | YUnion t when t.Item.layout = UStack -> Some $"USIncref{(ustack t).tag}(&({f v}));"
                | YPrim t when t <> StringT -> None
                | _ -> Some $"{f v}->refc++;"
            | REFC_SUPPR ->
                match t' with
                | YUnion t when t.Item.layout = UStack -> Some $"USSuppref{(ustack t).tag}(&({f v}));"
                | YPrim t when t <> StringT -> None
                | _ -> Some $"{f v}->refc--;"
```

Ah wait, this would affect even macros.

Ah, how annoying. Well whatever. Let me do them all in turn.

```fs
    and refc_change' (f : int * Ty -> string) (refc_flag : REFC) (x : TyV []) : string [] =
        Array.choose (fun (L(i,t')) ->
            let v = i,t'
            let inline g decref =
                match refc_flag with
                | REFC_INCR -> Some $"{f v}->refc++;"
                | REFC_DECR -> Some (decref())
                | REFC_SUPPR -> Some $"{f v}->refc--;"
            match t' with
            | YUnion t ->
                match t.Item.layout with
                | UStack ->
                    match refc_flag with
                    | REFC_INCR -> Some $"USIncref{(ustack t).tag}(&({f v}));"
                    | REFC_DECR -> Some $"USDecref{(ustack t).tag}(&({f v}));"
                    | REFC_SUPPR -> Some $"USSuppref{(ustack t).tag}(&({f v}));"
                | UHeap -> g (fun () -> $"UHDecref{(uheap t).tag}({f v});")
            | YArray t -> g (fun () -> $"ArrayDecref{(carray t).tag}({f v});")
            | YFun(a,b) -> g (fun () ->  $"{f v}->decref_fptr({f v});")
            | YPrim StringT -> g (fun () ->  $"StringDecref({f v});" )
            | YLayout(a,Heap) -> g (fun () ->  $"HeapDecref{(heap a).tag}({f v});")
            | YLayout(a,HeapMutable) -> g (fun () ->  $"MutDecref{(mut a).tag}({f v});")
            | _ -> None
            ) x
```

This should fix bools getting incremented.

Now let me fix the broken syntax.

```fs
let print_decref s_fun name_fun type_arg name_decref =
    line s_fun (sprintf "void %s(%s * x){" name_fun type_arg)
    let _ =
        let s_fun = indent s_fun
        line s_fun (sprintf "if (x != NULL && --(x->refc) == 0) { %s(x); free(x); }" name_decref)
    line s_fun "}"
```

That should do it. Let me move on.

3:45pm. https://cee.studio/

Right now I am trying this. How did the commands to enable memory checking work?

DTS_REPORT_UNRELEASED_MEMORY=1 DTS_REPORT_ALL_MEMORY_SPACES=1 DTS_MEMORY_UNINIT_CHECK=disabled ./a.out
DTS_REPORT_UNRELEASED_MEMORY=1 DTS_REPORT_ALL_MEMORY_SPACES=1 ./a.out

I just need to build and then run one of these commands.

Let me go through them all in turn. I tested it on the last one so far.

I'll want to check the rest."

---
## [ccfox/CWE-FoxFork](https://github.com/ccfox/CWE-FoxFork)@[fff7262755...](https://github.com/ccfox/CWE-FoxFork/commit/fff7262755c926b2a90628ef415121fefc5a40d4)
#### Wednesday 2023-02-22 09:27:02 by ccfox

Last of the Events

Probably overlooked something that needs social_democrat added somewhere, but I think I did good going through 400+ files.

Also I left Italy mostly alone, and the USSR completely alone. Hoping that @Eeillios and @Domper59 would be willing to go through the content they added and align it with the social_democrat addition.

There also needs to be party scandal events for social_democrat, and loc for the copy-pasted 'social democracy surge'.

Further, I think I accidentally made it so that autocratic states with social_democrat as the ideology instantly become democracies. This is an issue, but if we work on the government changes I plan and replace those files anyhow, it shouldn't matter.



Also, the gfx files, history files, and provinces.bmp are too big to upload for some reason. @Outta-my-way-burrocrat, if you have the program that lets you do uploads (I can't find the download for it) then uploading those would be appreciated. I didn't change any gfx - so the gfx from my fork of the main cwe repo should be fine. Same with history files - just pull them from my fork (the main branch). I only had to edit a few files in history/countries, so I'd easily be able to replace them.


Otherwise, I'll have to find a way to bypass github's size limitations.

---
## [DataDog/dd-trace-rb](https://github.com/DataDog/dd-trace-rb)@[eeabe537a2...](https://github.com/DataDog/dd-trace-rb/commit/eeabe537a29191ea3aeb3086c9aa8b91c958c0f3)
#### Wednesday 2023-02-22 10:08:14 by Ivo Anjo

Second step of making some sample values optional: make StackRecorder configurable

In the previous commit the `sample_values` struct was introduced, which
abstracted how values are passed to libdatadog away from everywhere
else in the profiler, and centralized this into the `StackRecorder`.

In this commit, I reimplemented the `record_sample` function to,
instead of using a hardcoded position for every value type, rely
on two extra indirections:
* `state->position_for`
* `state->enabled_values_count`

By default (e.g. when all profile types are enabled), this new
strategy behaves exactly as before.

The interesting thing happens when some profile types are disabled
(via the constructor). When profile types are disabled,
the two indirections above are reconfigured: `enabled_values_count`
becomes less than `ALL_VALUE_TYPES_COUNT`, and `position_for` is
updated to account for this as well.

In pratice, the `position_for` array is treated as if it was a
hashmap -- the key is a given profile type, and the value is the
position that libdatadog is expected it to be written to.

Thus, converting a `sample_values` to an array for libdatadog
is as simple as

```c
  metric_values[position_for[CPU_TIME_VALUE_ID]]      = values.cpu_time_ns;
  metric_values[position_for[CPU_SAMPLES_VALUE_ID]]   = values.cpu_samples;
  metric_values[position_for[WALL_TIME_VALUE_ID]]     = values.wall_time_ns;
  metric_values[position_for[ALLOC_SAMPLES_VALUE_ID]] = values.alloc_samples;
```

The trick here, is that when certain profile_types are disabled
their `position_for` is changed, so they are put at the end of the
`metric_values` array.

For instance, when we disable both `CPU_TIME_VALUE` and
`ALLOC_SAMPLES_VALUE` the `position_for` "hashmap" will look something
like

```ruby
{
  CPU_SAMPLES_VALUE_ID: 0,
  WALL_TIME_VALUE_ID: 1,
  CPU_TIME_VALUE_ID: 2,
  ALLOC_SAMPLES_VALUE_ID: 3,
}
```

And thus, given

```ruby
{ 'cpu-time' => 123, 'cpu-samples' => 456, 'wall-time' => 789, 'alloc-samples' => 4242 }
```

We will produce a `metrics_values` array with

```
+-----+-----+-----+------+
| 456 | 789 | 123 | 4242 |
+-----+-----+-----+------+
```

...but we'll tell libdatadog to only use the first 2 positions of
the array, which contain the values for the enabled profile types!

To be honest, this was more boilerplate than I wanted, but I'm happy
that most of the complexity lies in `_native_initialize` around the
creation of `position_for` and the values list for libdatadog, and
everywhere else still looks kinda sane.

---
## [Okand37/tgstation](https://github.com/Okand37/tgstation)@[66b7310039...](https://github.com/Okand37/tgstation/commit/66b7310039297843b01c5b14a9b59180909ab52c)
#### Wednesday 2023-02-22 10:50:17 by Rhials

STAY IN THE LIGHT: Adds terrify Nightmare spell, terrified status effect, and a reason to mind the shadows (#72282)

Adds the Terrify spell, and its associated status effect, Terrified.
This new spell is given to antagonist nightmares, as a part of their
brain. The spell only works in those surrounded by darkness, and will
apply the Terrified status effect if successful. Upon being Terrified,
victims will passively gain **Terror Buildup** if they remain in the
dark. As buildup increases, so do the negative effects, including tunnel
vision, panic attacks, dizziness, and more.

There are two primary methods for mitigating terror buildup. The first
is moving into the light, which will reverse the passive terror buildup
and eventually make it go away. The other method is by getting a hug
from a friendly hand, which will reduce buildup significantly.

Getting a hug from an UNfriendly hand (a nightmare, for instance) will
cause the victim to freak out and be briefly knocked down. This can be
spammed on targets who are caught alone in the dark, keeping them in an
unfavorable position (sideways) and adding to the victim's terror
buildup considerably. Escape into the light as soon as possible, or
you'll be pushed to MAXIMUM TERROR BUILDUP.

To what end? Heart failure. Past the soft terror cap (which limits how
much passively generated terror you can make) exists the hard terror
cap. Bypassing that threshold will cause a stress induced heart attack
and knock you unconscious (embarrassing!)

---
## [ErikSchierboom/rust](https://github.com/ErikSchierboom/rust)@[7a49959ea4...](https://github.com/ErikSchierboom/rust/commit/7a49959ea4aa3dbe3f5dd23a1de909196d62ea13)
#### Wednesday 2023-02-22 11:44:46 by Remo Senekowitsch

xorcism: remove rstest dependency (#1590)

rstest uses proc macros, which make the tests timeout due to long
compile times. Replace rstest with a custom declarative macro.

Brings test time from 7.5 seconds to 0.8 seconds on my machine.

Drawbacks:
* more indentation
* module structure of tests is flipped around

both of those seem minor to me. 

Although declarative macros can be hard to read for those unfamiliar, 
that was already somewhat the case with rstest's magic in my opinion. So
I personally don't think it's worse in terms of the students being able to
understand the tests.

The only other alternative I see is to disable the online tests 
altogether and leave a note about that in the exercise description. That
probably wouldn't be that bad, since people solving this hard exercise
most likely have a solid local setup. But it would still be cool to run
the tests online as well.

https://github.com/exercism/rust/issues/1513

---
## [haeksha/kernel_msm8996](https://github.com/haeksha/kernel_msm8996)@[ba1837d6fc...](https://github.com/haeksha/kernel_msm8996/commit/ba1837d6fc8025d71d85e2d66267c83ad4c8a5a0)
#### Wednesday 2023-02-22 12:27:44 by Masahiro Yamada

modpost: file2alias: go back to simple devtable lookup

commit ec91e78d378cc5d4b43805a1227d8e04e5dfa17d upstream.

Commit e49ce14150c6 ("modpost: use linker section to generate table.")
was not so cool as we had expected first; it ended up with ugly section
hacks when commit dd2a3acaecd7 ("mod/file2alias: make modpost compile
on darwin again") came in.

Given a certain degree of unknowledge about the link stage of host
programs, I really want to see simple, stupid table lookup so that
this works in the same way regardless of the underlying executable
format.

Signed-off-by: Masahiro Yamada <yamada.masahiro@socionext.com>
Acked-by: Mathieu Malaterre <malat@debian.org>
[nc: Omit rpmsg, sdw, tbsvc, and typec as they don't exist here]
Signed-off-by: Nathan Chancellor <natechancellor@gmail.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [yadij/squid](https://github.com/yadij/squid)@[2b6b1bcb86...](https://github.com/yadij/squid/commit/2b6b1bcb8650095c99a1916f5964305484af7ef0)
#### Wednesday 2023-02-22 12:53:27 by Alex Rousskov

Bug 5055: FATAL FwdState::noteDestinationsEnd exception: opening (#877)

The bug was caused by commit 25b0ce4. Other known symptoms are:

    assertion failed: store.cc:1793: "isEmpty()"
    assertion failed: FwdState.cc:501: "serverConnection() == conn"
    assertion failed: FwdState.cc:1037: "!opening()"

This change has several overlapping parts. Unfortunately, merging
individual parts is both difficult and likely to cause crashes.

## Part 1: Bug 5055.

FwdState used to check serverConn to decide whether to open a connection
to forward the request. Since commit 25b0ce4, a nil serverConn pointer
no longer implies that a new connection should be opened: FwdState
helper jobs may already be working on preparing an existing open
connection (e.g., sending a CONNECT request or negotiating encryption).

Bad serverConn checks in both FwdState::noteDestination() and
FwdState::noteDestinationsEnd() methods led to extra connectStart()
calls creating two conflicting concurrent helper jobs.

To fix this, we replaced direct serverConn inspection with a
usingDestination() call which also checks whether we are waiting for a
helper job. Testing that fix exposed another set of bugs: The helper job
pointers or in-job connections were left stale/set after forwarding
failures. The changes described below addressed most of those problems.


## Part 2: Connection establishing helper jobs and their callbacks

A proper fix for Bug 5055 required answering a difficult question: When
should a dying job call its callbacks? We only found one answer which
required cooperation from the job creator and led to the following
rules:

* AsyncJob destructors must not call any callbacks.

* AsyncJob::swanSong() is responsible for async-calling any remaining
  (i.e. set, uncalled, and uncancelled) callbacks.

* AsyncJob::swanSong() is called (only) for started jobs.

* AsyncJob destructing sequence should validate that no callbacks remain
  uncalled for started jobs.

... where an AsyncJob x is considered "started" if AsyncJob::Start(x)
has returned without throwing.

A new JobWait class helps job creators follow these rules while keeping
track on in-progress helper jobs and killing no-longer-needed helpers.

Also fixed very similar bugs in tunnel.cc code.


## Part 3: ConnOpener fixes

1. Many ConnOpener users are written to keep a ConnectionPointer to the
   destination given to ConnOpener. This means that their connection
   magically opens when ConnOpener successfully connects, before
   ConnOpener has a chance to notify the user about the changes. Having
   multiple concurrent connection owners is always dangerous, and the
   user cannot even have a close handler registered for its now-open
   connection. When something happens to ConnOpener or its answer, the
   user job may be in trouble. Now, ConnOpener callers no longer pass
   Connection objects they own, cloning them as needed. That adjustment
   required adjustment 2:

2. Refactored ConnOpener users to stop assuming that the answer contains
   a pointer to their connection object. After adjustment 1 above, it
   does not. HappyConnOpener relied on that assumption quite a bit so we
   had to refactor to use two custom callback methods instead of one
   with a complicated if-statement distinguishing prime from spare
   attempts. This refactoring is an overall improvement because it
   simplifies the code. Other ConnOpener users just needed to remove a
   few no longer valid paranoid assertions/Musts.

3. ConnOpener users were forced to remember to close params.conn when
   processing negative answers. Some, naturally, forgot, triggering
   warnings about orphaned connections (e.g., Ident and TcpLogger).
   ConnOpener now closes its open connection before sending a negative
   answer.

4. ConnOpener would trigger orphan connection warnings if the job ended
   after opening the connection but without supplying the connection to
   the requestor (e.g., because the requestor has gone away). Now,
   ConnOpener explicitly closes its open connection if it has not been
   sent to the requestor.

Also fixed Comm::ConnOpener::cleanFd() debugging that was incorrectly
saying that the method closes the temporary descriptor.

Also fixed ConnOpener callback's syncWithComm(): The stale
CommConnectCbParams override was testing unused (i.e. always negative)
CommConnectCbParams::fd and was trying to cancel the callback that most
(possibly all) recipients rely on: ConnOpener users expect a negative
answer rather than no answer at all.

Also, after comparing the needs of two old/existing and a temporary
added ("clone everything") Connection cloning method callers, we decided
there is no need to maintain three different methods. All existing
callers should be fine with a single method because none of them suffers
from "extra" copying of members that others need. Right now, the new
cloneProfile() method copies everything except FD and a few
special-purpose members (with documented reasons for not copying).

Also added Comm::Connection::cloneDestinationDetails() debugging to
simplify tracking dependencies between half-baked Connection objects
carrying destination/flags/other metadata and open Connection objects
created by ConnOpener using that metadata (which are later delivered to
ConnOpener users and, in some cases, replace those half-baked
connections mentioned earlier. Long-term, we need to find a better way
to express these and other Connection states/stages than comments and
debugging messages.


## Part 4: Comm::Connection closure callbacks

We improved many closure callbacks to make sure (to the extent possible)
that Connection and other objects are in sync with Comm. There are lots
of small bugs, inconsistencies, and other problems in Connection closure
handlers. It is not clear whether any of those problems could result in
serious runtime errors or leaks. In theory, the rest of the code could
neutralize their negative side effects. However, even in that case, it
would only be a matter of time before the next bug bites us due to stale
Connection::fd and such. These changes themselves carry elevated risk,
but they get us closer to reliable code as far as Connection maintenance
is concerned. Without them, we will keep chasing deadly side effects of
poorly implemented closure callbacks.

Long-term, all these manual efforts to keep things in sync should become
unnecessary with the introduction of appropriate Connection ownership
APIs that automatically maintain the corresponding environments (TODO).


## Part 5: Other notable improvements in the adjusted code

Improved Security::PeerConnector::serverConn and
Http::Tunneler::connection management, especially when sending negative
answers. When sending a negative answer, we would set answer().conn to
an open connection, async-send that answer, and then hurry to close the
connection using our pointer to the shared Connection object. If
everything went according to the plan, the recipient would get a non-nil
but closed Connection object. Now, a negative answer simply means no
connection at all. Same for a tunneled answer.

Refactored ICAP connection-establishing code to to delay Connection
ownership until the ICAP connection is fully ready. This change
addresses primary Connection ownership concerns (as they apply to this
ICAP code) except orphaning of the temporary Connection object by helper
job start exceptions (now an explicit XXX). For example, the transaction
no longer shares a Connection object with ConnOpener and
IcapPeerConnector jobs.

Probably fixed a bug where PeerConnector::negotiate() assumed that
sslFinalized() does not return true after callBack(). It may (e.g., when
CertValidationHelper::Submit() throws). Same for
PeekingPeerConnector::checkForPeekAndSpliceMatched().
 
Fixed FwdState::advanceDestination() bug that did not save
ERR_GATEWAY_FAILURE details and "lost" the address of that failed
destination, making it unavailable to future retries (if any).

Polished PeerPoolMgr, Ident, and Gopher code to be able to fix similar
job callback and connection management issues.

Polished AsyncJob::Start() API. Start() used to return a job pointer,
but that was a bad idea:
    
* It implies that a failed Start() will return a nil pointer, and that
  the caller should check the result. Neither is true.

* It encourages callers to dereference the returned pointer to further
  adjust the job. That technically works (today) but violates the rules
  of communicating with an async job. The Start() method is the boundary
  after which the job is deemed asynchronous.
    
Also removed old "and wait for..." post-Start() comments because the
code itself became clear enough, and those comments were becoming
increasingly stale (because they duplicated the callback names above
them).

Fix Tunneler and PeerConnector handling of last-resort callback
requirements. Events like handleStopRequest() and callException() stop
the job but should not be reported as a BUG (e.g., it would be up to the
callException() to decide how to report the caught exception). There
might (or there will) be other, similar cases where the job is stopped
prematurely for some non-BUG reason beyond swanSong() knowledge. The
existence of non-bug cases does not mean there could be no bugs worth
reporting here, but until they can be identified more reliably than all
these benign/irrelevant cases, reporting no BUGs is a (much) lesser
evil.

TODO: Revise AsyncJob::doneAll(). Many of its overrides are written to
check for both positive (i.e. mission accomplished) and negative (i.e.
mission cancelled or cannot be accomplished) conditions, but the latter
is usually unnecessary, especially after we added handleStopRequest()
API to properly support external job cancellation events. Many doneAll()
overrides can probably be greatly simplified.

---
## [gitdnd/azerothcore-wotlk](https://github.com/gitdnd/azerothcore-wotlk)@[ef949f9ff0...](https://github.com/gitdnd/azerothcore-wotlk/commit/ef949f9ff0a89e837c67258d7e199da1706bc438)
#### Wednesday 2023-02-22 13:41:36 by ICXCNIKA

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
## [vijaydasmp/dash](https://github.com/vijaydasmp/dash)@[aec7441ac2...](https://github.com/vijaydasmp/dash/commit/aec7441ac2863b4d92c5032e98e8b2691262a912)
#### Wednesday 2023-02-22 13:51:55 by Wladimir J. van der Laan

Merge #15277: contrib: Enable building in Guix containers

751549b52a9a4cd27389d807ae67f02bbb39cd7f contrib: guix: Additional clarifications re: substitutes (Carl Dong)
cd3e947f50db7cfe05c05b368c25742193729a62 contrib: guix: Various improvements. (Carl Dong)
8dff3e48a9e03299468ed3b342642f01f70da9db contrib: guix: Clarify SOURCE_DATE_EPOCH. (Carl Dong)
3e80ec3ea9691c7c89173de922a113e643fe976b contrib: Add deterministic Guix builds. (Carl Dong)

Pull request description:

  ~~**This post is kept updated as this project progresses. Use this [latest update link](https://github.com/bitcoin/bitcoin/pull/15277#issuecomment-497303718) to see what's new.**~~

  Please read the `README.md`.

  -----

  ### Guix Introduction

  This PR enables building bitcoin in Guix containers. [Guix](https://www.gnu.org/software/guix/manual/en/html_node/Features.html) is a transactional package manager much like Nix, but unlike Nix, it has more of a focus on [bootstrappability](https://www.gnu.org/software/guix/manual/en/html_node/Bootstrapping.html) and [reproducibility](https://www.gnu.org/software/guix/blog/tags/reproducible-builds/) which are attractive for security-sensitive projects like bitcoin.

  ### Guix Build Walkthrough

  Please read the `README.md`.

  [Old instructions no. 4](https://github.com/bitcoin/bitcoin/pull/15277#issuecomment-497303718)

  [Old instructions no. 3](https://github.com/bitcoin/bitcoin/pull/15277#issuecomment-493827011)

  [Old instructions no. 2](https://github.com/bitcoin/bitcoin/pull/15277#issuecomment-471658439)

  <details>
  <summary>Old instructions no. 1</summary>
  In this PR, we define a Guix [manifest](https://www.gnu.org/software/guix/manual/en/html_node/Invoking-guix-package.html#profile_002dmanifest) in `contrib/guix/manifest.scm`, which declares what packages we want in our environment.

  We can then invoke
  ```
  guix environment --manifest=contrib/guix/manifest.scm --container --pure --no-grafts --no-substitutes
  ```
  To have Guix:
  1. Build an environment containing the packages we defined in our `contrib/guix/manifest.scm` manifest from the Guix bootstrap binaries (see [bootstrappability](https://www.gnu.org/software/guix/manual/en/html_node/Bootstrapping.html) for more details).
  2. Start a container with that environment that has no network access, and no access to the host's filesystem except to the `pwd` that it was started in.
  3. Drop you into a shell in that container.

  > Note: if you don't want to wait hours for Guix to build the entire world from scratch, you can eliminate the `--no-substitutes` option to have Guix download from available binary sources. Note that this convenience doesn't necessarily compromise your security, as you can check that a package was built correctly after the fact using `guix build --check <packagename>`

  Therefore, we can perform a build of bitcoin much like in Gitian by invoking the following:

  ```
  make -C depends -j"$(nproc)" download && \
      cat contrib/guix/build.sh | guix environment --manifest=contrib/guix/manifest.scm --container --pure --no-grafts --no-substitutes
  ```

  We don't include `make -C depends -j"$(nproc)" download` inside `contrib/guix/build.sh` because `contrib/guix/build.sh` is run inside the container, which has no network access (which is a good thing).
  </details>

  ### Rationale

  I believe that this represents a substantial improvement for the "supply chain security" of bitcoin because:

  1. We no longer have to rely on Ubuntu for our build environment for our releases ([oh the horror](https://github.com/bitcoin/bitcoin/blob/72bd4ab867e3be0d8410403d9641c08288d343e3/contrib/gitian-descriptors/gitian-linux.yml#L10)), because Guix builds everything about the container, we can perform this on almost any Linux distro/system.
  2. It is now much easier to determine what trusted binaries are in our supply chain, and even make a nice visualization! (see [bootstrappability](https://www.gnu.org/software/guix/manual/en/html_node/Bootstrapping.html)).
  3. There is active effort among Guix folks to minimize the number of trusted binaries even further. OriansJ's [stage0](https://github.com/oriansj/stage0), and janneke's [Mes](https://www.gnu.org/software/mes/) all aim to achieve [reduced binary boostrap](http://joyofsource.com/reduced-binary-seed-bootstrap.html) for Guix. In fact, I believe if OriansJ gets his way, we will end up some day with only a single trusted binary: hex0 (a ~500 byte self-hosting hex assembler).

  ### Steps to Completion

  - [x] Successfully build bitcoin inside the Guix environment
  - [x] Make `check-symbols` pass
  - [x] Do the above but without nasty hacks
  - [x] Solve some of the more innocuous hacks
  - [ ] Make it cross-compile (HELP WANTED HERE)
    - [x] Linux
      - [x] x86_64-linux-gnu
      - [x] i686-linux-gnu
      - [x] aarch64-linux-gnu
      - [x] arm-linux-gnueabihf
      - [x] riscv64-linux-gnu
    - [ ] OS X
      - [ ] x86_64-apple-darwin14
    - [ ] Windows
      - [ ] x86_64-w64-mingw32
  - [ ] Maybe make importer for depends syntax
  - [ ] Document build process for future releases
  - [ ] Extra: Pin the revision of Guix that we build with with Guix [inferiors](https://www.gnu.org/software/guix/manual/en/html_node/Inferiors.html)

  ### Help Wanted

  [Old content no. 3](https://github.com/bitcoin/bitcoin/pull/15277#issuecomment-483318210)

  [Old content no. 2](https://github.com/bitcoin/bitcoin/pull/15277#issuecomment-471658439)

  <details>
  <summary>Old content no. 1</summary>
  As of now, the command described above to perform a build of bitcoin a lot like Gitian works, but fails at the `check-symbols` stage. This is because a few dynamic libraries are linked in that shouldn't be.

  Here's what `ldd src/bitcoind` looks like when built in a Guix container:
  ```
  	linux-vdso.so.1 (0x00007ffcc2d90000)
  	libdl.so.2 => /gnu/store/h90vnqw0nwd0hhm1l5dgxsdrigddfmq4-glibc-2.28/lib/libdl.so.2 (0x00007fb7eda09000)
  	librt.so.1 => /gnu/store/h90vnqw0nwd0hhm1l5dgxsdrigddfmq4-glibc-2.28/lib/librt.so.1 (0x00007fb7ed9ff000)
  	libstdc++.so.6 => /gnu/store/4sqps8dczv3g7rwbdibfz6rf5jlk7w90-gcc-5.5.0-lib/lib/libstdc++.so.6 (0x00007fb7ed87c000)
  	libpthread.so.0 => /gnu/store/h90vnqw0nwd0hhm1l5dgxsdrigddfmq4-glibc-2.28/lib/libpthread.so.0 (0x00007fb7ed85b000)
  	libm.so.6 => /gnu/store/h90vnqw0nwd0hhm1l5dgxsdrigddfmq4-glibc-2.28/lib/libm.so.6 (0x00007fb7ed6da000)
  	libgcc_s.so.1 => /gnu/store/4sqps8dczv3g7rwbdibfz6rf5jlk7w90-gcc-5.5.0-lib/lib/libgcc_s.so.1 (0x00007fb7ed6bf000)
  	libc.so.6 => /gnu/store/h90vnqw0nwd0hhm1l5dgxsdrigddfmq4-glibc-2.28/lib/libc.so.6 (0x00007fb7ed506000)
  	/gnu/store/h90vnqw0nwd0hhm1l5dgxsdrigddfmq4-glibc-2.28/lib/ld-linux-x86-64.so.2 => /usr/lib64/ld-linux-x86-64.so.2 (0x00007fb7ee3a0000)
  ```

  And here's what it looks in one of our releases:
  ```
  	linux-vdso.so.1 (0x00007ffff52cd000)
  	libpthread.so.0 => /usr/lib/libpthread.so.0 (0x00007f87726b4000)
  	librt.so.1 => /usr/lib/librt.so.1 (0x00007f87726aa000)
  	libm.so.6 => /usr/lib/libm.so.6 (0x00007f8772525000)
  	libgcc_s.so.1 => /usr/lib/libgcc_s.so.1 (0x00007f877250b000)
  	libc.so.6 => /usr/lib/libc.so.6 (0x00007f8772347000)
  	/lib64/ld-linux-x86-64.so.2 => /usr/lib64/ld-linux-x86-64.so.2 (0x00007f8773392000)
  ```

  ~~I suspect it is because my script does not apply the gitian-input patches [described in the release process](https://github.com/bitcoin/bitcoin/blob/master/doc/release-process.md#fetch-and-create-inputs-first-time-or-when-dependency-versions-change) but there is no description as to how these patches are applied.~~ It might also be something else entirely.

  Edit: It is something else. It appears that the gitian inputs are only used by [`gitian-win-signer.yml`](https://github.com/bitcoin/bitcoin/blob/d6e700e40f861ddd6743f4d13f0d6f6bc19093c2/contrib/gitian-descriptors/gitian-win-signer.yml#L14)
  </details>

  ### How to Help

  1. Install Guix on your distro either [from source](https://www.gnu.org/software/guix/manual/en/html_node/Requirements.html) or perform a [binary installation](https://www.gnu.org/software/guix/manual/en/html_node/Binary-Installation.html#Binary-Installation)
  2. Try out my branch and the command described above!

ACKs for top commit:
  MarcoFalke:
    Thanks for the replies. ACK 751549b52a9a4cd27389d807ae67f02bbb39cd7f
  laanwj:
    ACK 751549b52a9a4cd27389d807ae67f02bbb39cd7f

Tree-SHA512: 50e6ab58c6bda9a67125b6271daf7eff0ca57d0efa8941ed3cd951e5bf78b31552fc5e537b1e1bcf2d3cc918c63adf19d685aa117a0f851024dc67e697890a8d

---
## [rahagi/dwm](https://github.com/rahagi/dwm)@[67d76bdc68...](https://github.com/rahagi/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Wednesday 2023-02-22 14:26:06 by Chris Down

Do not allow focus to drift from fullscreen client via focusstack()

It generally doesn't make much sense to allow focusstack() to navigate
away from the selected fullscreen client, as you can't even see which
client you're selecting behind it.

I have had this up for a while on the wiki as a separate patch[0], but
it seems reasonable to avoid this behaviour in dwm mainline, since I'm
struggling to think of any reason to navigate away from a fullscreen
client other than a mistake.

0: https://dwm.suckless.org/patches/alwaysfullscreen/

---
## [newren/git](https://github.com/newren/git)@[69bbbe484b...](https://github.com/newren/git/commit/69bbbe484ba10bd88efb9ae3f6a58fcc687df69e)
#### Wednesday 2023-02-22 15:00:31 by Jeff King

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
## [qaptoR/Commando](https://github.com/qaptoR/Commando)@[ff7d99eaa6...](https://github.com/qaptoR/Commando/commit/ff7d99eaa6879c5dac535e5eb38644408871fa25)
#### Wednesday 2023-02-22 15:04:06 by qaptoR

added credits file

was looking at an old github repo, and this was something I
used to add to the top of my programs. I stopped for years
because I thought it was pretentious for someone just starting
out as a programmer, but looking back I now wish I had done it more.

It certainly wouldn't have mattered much since the bulk of my work
has been on private projects, but this is my first real public
contribution of software that wasn't a PR for another project
(where adding my own CREDITS.txt would be frowned upon).

Anyway, just a bit of info about why it's been added.
I've now been a programmer for 5 years, and am at the
time of this writing a 4th year computer science major.

In summary, I feel that I've earned my right to be a little
pretentious. I think we should all feel okay to look at our work
proudly and say 'yeah, I did that'.

---
## [dominiqueclarke/kibana](https://github.com/dominiqueclarke/kibana)@[43fa5174f8...](https://github.com/dominiqueclarke/kibana/commit/43fa5174f813ce7999dbc65b71cbb9ba0168fb1d)
#### Wednesday 2023-02-22 15:04:56 by Clint Andrew Hall

[kibana] Thank you for everything, Spencer! 🧔🏻‍♂️ (#150759)

## Summary

> _Inspired by @kertal, and extracted from his PR
https://github.com/elastic/kibana/pull/150660, specifically
@thomasneirynck's
[proposal](https://github.com/elastic/kibana/pull/150660/files#r1101795511)._
>
> _Holding for 24 hours, for our friends in later time zones._

Several of us felt a dev-only easter egg-- where, if you're lucky,
@spalger joins you as you test your latest feature-- would be a fun
tribute as he leaves us for new and exciting opportunities.

Elasticians, feel free to send your love to @spalger in the channel of
your choice, of course, but we'd appreciate your review of this pull
request. ❤️


![image](https://user-images.githubusercontent.com/1178348/217867285-b23dcf1f-1a4a-45fd-b828-f6b24215fef2.png)

---------

Co-authored-by: spalger <spencer@elastic.co>

---
## [AngelYahir/DOTDCD](https://github.com/AngelYahir/DOTDCD)@[7a425818a0...](https://github.com/AngelYahir/DOTDCD/commit/7a425818a0428b6d49dd74421aca58864afe05d3)
#### Wednesday 2023-02-22 15:20:23 by Angel Tores

I do this commit against my will & my mental stability, pls help me i need to go to sleep 7 hours minimal ass shit

---
## [Rumrobot/ToldJS](https://github.com/Rumrobot/ToldJS)@[fe506ebc57...](https://github.com/Rumrobot/ToldJS/commit/fe506ebc57ef9396ad1b63e5e4c348067e70f15d)
#### Wednesday 2023-02-22 15:45:36 by Rumrobot

Kinda working shit

Some pdf stuff works, but formatting is still hell. Things removed and added, so it matches with what the state wants us to fill out.

---
## [hasura/graphql-engine](https://github.com/hasura/graphql-engine)@[6e574f1bbe...](https://github.com/hasura/graphql-engine/commit/6e574f1bbe521e561a8116bf167a6be1060bc8d4)
#### Wednesday 2023-02-22 15:56:00 by Antoine Leblanc

harmonize network manager handling

## Description

### I want to speak to the `Manager`

Oh boy. This PR is both fairly straightforward and overreaching, so let's break it down.

For most network access, we need a [`HTTP.Manager`](https://hackage.haskell.org/package/http-client-0.1.0.0/docs/Network-HTTP-Client-Manager.html). It is created only once, at the top level, when starting the engine, and is then threaded through the application to wherever we need to make a network call. As of main, the way we do this is not standardized: most of the GraphQL execution code passes it "manually" as a function argument throughout the code. We also have a custom monad constraint, `HasHttpManagerM`, that describes a monad's ability to provide a manager. And, finally, several parts of the code store the manager in some kind of argument structure, such as `RunT`'s `RunCtx`.

This PR's first goal is to harmonize all of this: we always create the manager at the root, and we already have it when we do our very first `runReaderT`. Wouldn't it make sense for the rest of the code to not manually pass it anywhere, to not store it anywhere, but to always rely on the current monad providing it? This is, in short, what this PR does: it implements a constraint on the base monads, so that they provide the manager, and removes most explicit passing from the code.

### First come, first served

One way this PR goes a tiny bit further than "just" doing the aforementioned harmonization is that it starts the process of implementing the "Services oriented architecture" roughly outlined in this [draft document](https://docs.google.com/document/d/1FAigqrST0juU1WcT4HIxJxe1iEBwTuBZodTaeUvsKqQ/edit?usp=sharing). Instead of using the existing `HasHTTPManagerM`, this PR revamps it into the `ProvidesNetwork` service.

The idea is, again, that we should make all "external" dependencies of the engine, all things that the core of the engine doesn't care about, a "service". This allows us to define clear APIs for features, to choose different implementations based on which version of the engine we're running, harmonizes our many scattered monadic constraints... Which is why this service is called "Network": we can refine it, moving forward, to be the constraint that defines how all network communication is to operate, instead of relying on disparate classes constraint or hardcoded decisions. A comment in the code clarifies this intent.

### Side-effects? In my Haskell?

This PR also unavoidably touches some other aspects of the codebase. One such example: it introduces `Hasura.App.AppContext`, named after `HasuraPro.Context.AppContext`: a name for the reader structure at the base level. It also transforms `Handler` from a type alias to a newtype, as `Handler` is where we actually enforce HTTP limits; but without `Handler` being a distinct type, any code path could simply do a `runExceptT $ runReader` and forget to enforce them.

(As a rule of thumb, i am starting to consider any straggling `runReaderT` or `runExceptT` as a code smell: we should not stack / unstack monads haphazardly, and every layer should be an opaque `newtype` with a corresponding run function.)

## Further work

In several places, i have left TODOs when i have encountered things that suggest that we should do further unrelated cleanups. I'll write down the follow-up steps, either in the aforementioned document or on slack. But, in short, at a glance, in approximate order, we could:

- delete `ExecutionCtx` as it is only a subset of `ServerCtx`, and remove one more `runReaderT` call
- delete `ServerConfigCtx` as it is only a subset of `ServerCtx`, and remove it from `RunCtx`
- remove `ServerCtx` from `HandlerCtx`, and make it part of `AppContext`, or even make it the `AppContext` altogether (since, at least for the OSS version, `AppContext` is there again only a subset)
- remove `CacheBuildParams` and `CacheBuild` altogether, as they're just a distinct stack that is a `ReaderT` on top of `IO` that contains, you guessed it, the same thing as `ServerCtx`
- move `RunT` out of `RQL.Types` and rename it, since after the previous cleanups **it only contains `UserInfo`**; it could be bundled with the authentication service, made a small implementation detail in `Hasura.Server.Auth`
-  rename `PGMetadaStorageT` to something a bit more accurate, such as `App`, and enforce its IO base

This would significantly simply our complex stack. From there, or in parallel, we can start moving existing dependencies as Services. For the purpose of supporting read replicas entitlement, we could move `MonadResolveSource` to a `SourceResolver` service, as attempted in #7653, and transform `UserAuthenticationM` into a `Authentication` service.

PR-URL: https://github.com/hasura/graphql-engine-mono/pull/7736
GitOrigin-RevId: 68cce710eb9e7d752bda1ba0c49541d24df8209f

---
## [anwarmbl/github-final-project](https://github.com/anwarmbl/github-final-project)@[578249492d...](https://github.com/anwarmbl/github-final-project/commit/578249492de5b635da4fff1fcc54c14acd1a2579)
#### Wednesday 2023-02-22 16:25:14 by anwarmbl

Create CONTRIBUTING.md

# Contributing

When contributing a major change to this repository, please first discuss the
change you wish to make via an [issue](contributing/ISSUES.md) or via
[Slack in the #racial-justice-legit-info 
channel](https://callforcode.slack.com/archives/C01CRAN53CM) in the [Call for
Code Slack workspace](https://callforcode.org/slack). Minor issues can simply
be addressed by sending by a pull request.

All [pull requests](contributing/PULL-REQUESTS.md) will require you to ensure
the change is certified via the [Developer Certificate of Origin 
(DCO)](https://github.com/apps/dco/). The DCO is a lightweight way for 
contributors to certify that they wrote or otherwise have the right to submit
the code they are contributing to the project.

Please note we have a [Code of Conduct](#code-of-conduct), please follow it in
all your interactions with the project and its community.

## Coding Standards

This project adheres to the PEP 8 Python Coding Style Guidelines, Django naming
conventions, and other standards.  See [STYLE.md](docs/STYLE.md) for details.

## Programming Languages

Scripts are written for "bash" shell.
Python code is written at the [Python 3.6](https://docs.python.org/3.6/) level.

## Managing Dependencies

Install or uninstall all dependencies using these commands while you are
in the pipenv shell:

```console
(cfc) $ pipenv install <program>"
(cfc) $ pipenv lock -r > requirements.txt"
```

The pipfile, pipfile.lock and requirements.txt will be part of the git
commit/pull-request to be reviewed.


## Pull Request Process

1. Fork the repository.
2. Commit your changes to your fork.
3. Submit a pull request. _Don't forget to add yourself in the [Authors](Authors) file!_
4. Handle any feedback before the request is merged.
5. Accept our sincere Thank You!

## Code of Conduct

### Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, 
body size, disability, ethnicity, gender identity and expression, level of 
experience, nationality, personal appearance, race, religion, or sexual 
identity and orientation.

### Our Standards

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or
advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic
  address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

### Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

### Scope

This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an appointed
representative at an online or offline event. Representation of a project may be
further defined and clarified by project maintainers.

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team on [Slack in the #racial-justice-legit-info channel](https://callforcode.slack.com/archives/C01CRAN53CM). 

All complaints will be reviewed and investigated and will result in a response that is deemed necessary and appropriate to the circumstances. The project team is obligated to maintain confidentiality with regard to the reporter of an incident.Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

### Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4, available at [http://contributor-covenant.org/version/1/4][version]

[homepage]: http://contributor-covenant.org
[version]: http://contributor-covenant.org/version/1/4/

---
## [seamacs/melpa](https://github.com/seamacs/melpa)@[4872ef038d...](https://github.com/seamacs/melpa/commit/4872ef038dbbf67008bfa7951574ee372d6ff68d)
#### Wednesday 2023-02-22 16:43:47 by Jonas Bernoulli

Distribute all back-ends with the emacsql package

There are two reasons for this.

- Going forward, packages that use `emacsql' and SQLite should use
  the best back-end that can be used with the Emacs instance in use,
  either `emacsql-sqlite-builtin`, `emacsql-sqlite-module`, or as a
  last resort `emacsql-sqlite'.

  That means that if we didn't bundle the back-end libraries with
  `emacsql' itself, these packages would have to depend on all three
  back-end packages in addition to `emacsql' itself.  (Alternatively
  they could not depend on any of the back-end packages, and instead
  make the user install the appropriate back-end, when they try to
  use the package.  That's a bad user experience and there likely
  would be bugs, making it even more painful.)

- EmacSQL is now distributed on NonGNU Elpa as well.  While we at
  Melpa encourages the creation of separate packages for optional
  extensions (which are not useful to all users, or which have
  additional dependencies) the Emacs maintainers prefer everything to
  be distribute as one package, even if that means that `defvar' and
  `declare-function' declarations are necessary to keep the compiler
  happy.

  I still think our way is usually better, but since three of the
  back-end libraries have to be distributed with the main package
  anyway, we might as well give in here and bundle the other three
  as well.

For the time being, we have to continue to *also* distribute the
back-end libraries as separate packages.

Several third-party packages depend on the existing `emacsql' and
`emacsql-sqlite' packages.  These packages should be updated to only
depend on `emacsql', but the latest released versions of these
packages will continue to depend on `emacsql-sqlite' as well.  If we
removed the recipe for that, that would remove the latest release of
that package from Melpa, not just the snapshot version.

This is the current roadmap:

0. Include all back-ends in `emacsql'.
1. Update dependant packages to only depend on `emacsql'.
2. Make changes to `emacsql', which are enabled by the former two
   steps, and which are blocking the creation of a new `emacsql'
   release.  (These changes are related to the addition of the
   additional SQLite back-ends.  So this is a bit of a chicken and
   egg problem, and this commit (0) is the first step to break out
   of that.)
3. Create an `emacsql' release.
4. Wait for new releases of all dependant packages.
5. Change the separate back-end packages to warn the user, asking
   them to remove all of these packages.
6. After waiting some more, remove the separate back-end packages.

While a back-end is installed as part of `emacsql' and as a separate
package, it is undefined which version is loaded, but until step (5)
the two versions should be the same, so it doesn't matter.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[574085ea6a...](https://github.com/mrakgr/The-Spiral-Language/commit/574085ea6a497fa07eeea98b129240b2c5cdd53b)
#### Wednesday 2023-02-22 16:43:52 by Marko Grdinić

"https://app.otta.com/

Somebody posted this job site in a /twg/ thread.

https://app.otta.com/jobs/TkVialpD

I'll definitely keep this job portal in mind. Nevermind it for now.

9:15am. Damn, how is it so late?

My mental exhaustion is at its peak.

10:10pm. I am going to bed. I'll skip dinner.

2/22/2023

9:20am. I am up. I was overloaded last night and I had a lot of trouble falling asleep. I am actually considering skipping work entirely for the day, but I do not want to. I want to mess with the header right now, I want to understand why align contents shrinks them. Yesterday I was too tired, but it is eating away at me.

9:25am. I have a strong contrarian streak. When I push myself to work I want to laze, but when I push myself to laze, I want to work, so let me do the later. I am too tired for manga, so let me do some HTML.

I feel like I could understand it better if I go through this.

https://youtu.be/UuiImHywwvs
Align Items vs Align Content in Flexbox

Let me watch this. I do not understand the difference between these two.

https://youtu.be/UuiImHywwvs?t=4

Oh also, this is how calc is used? Interesting.

https://youtu.be/UuiImHywwvs?t=50

Huh, what is he doing here?

https://youtu.be/UuiImHywwvs?t=55

Oh, it is some Emmet thing.

https://youtu.be/UuiImHywwvs?t=245

Hmmm, I see. I couldn't figure out the why align content was doing nothing for the simple reason that I never had items on the same column.

https://www.w3schools.com/cssref/css_units.php
* Pixels (px) are relative to the viewing device. For low-dpi devices, 1px is one device pixel (dot) of the display. For printers and high resolution screens 1px implies multiple device pixels.

I am skeptical of this. I'd prefer to make my site resolution independent, but when I use px, it definitely isn't. I do not understand this exactly.

///

Tip: The em and rem units are practical in creating perfectly scalable layout!
* Viewport = the browser window size. If the viewport is 50cm wide, 1vw = 0.5cm.

///

https://www.w3schools.com/cssref/css4_pr_accent-color.php

This is a really good site.

10:10am. https://www.youtube.com/results?search_query=css+max-content

Let me watch some of these.

10:20am. https://youtu.be/DM244V9KvNs?t=432

I am distracted, but knowing this is pretty useful.

https://youtu.be/DM244V9KvNs?t=472

Oh, you can do something like this?

https://youtu.be/DM244V9KvNs?t=491

I just realized - you could probably get the arraying behavior with flex wrap. Nevermind that for now.

https://youtu.be/-st14lUQD3U
CSS width auto vs 100% | What's the difference?

Let me watch this as well.

https://youtu.be/-st14lUQD3U?t=57

> If you have a margin left and margin right on auto, it is automatically centering it.

Hmmm, really?

10:25am. That was pretty informative.

https://youtu.be/IWFqGsXxJ1E

Let me take a look at this.

...No forget it, I do not feel like watching that.

10:30am. Let me get back to layouting.

I want to redo the search bar part as it is too hacky.

https://stackoverflow.com/questions/29470676/why-doesnt-the-input-element-respect-min-width

Let me try this.

11:10am. Ok, that figures that.

...I am satisfied for now. Let me watch more of the course.

https://youtu.be/G3e-cpL7ofc?t=14427

11:30am. Tried redesigning the middle section so it has a nested container, but it was too complicated. Forget it. Let me just watch the video.

https://youtu.be/G3e-cpL7ofc?t=15418

He should have used an extension.

11:50am.

```fs
let inline img x = Html.img [prop.src (importDefault x)]

let header =
    Html.div [
        prop.className "header-box"
        prop.children [
            Html.div [
                prop.className "home-box header-item"
                prop.children [
                    img "./svgs/svgexport-5.svg"
                    ]
            ]
```

Agh. It seems let inline does not compose with other such statements in Fable.

https://youtu.be/G3e-cpL7ofc?t=17047

Huh, you can do it like this?

12:25pm. This is amazing. I would never have figured this out myself.

12:45pm. https://developer.mozilla.org/en-US/docs/Web/CSS/flex-basis

Oh, wow this exactly what I wanted. I could put in those padders and have them shrink.

https://stackoverflow.com/questions/54654050/difference-between-flex-end-and-end

Ah, I see.

1:10pm. https://stackoverflow.com/questions/67858284/how-to-have-one-item-shrink-fully-before-another-starts-to-shrink

Damn it, let me stop here. I am going crazy. flex-basis is a great thing, but for some reason the search bar is always being shrunk more than than the padders. How annoying.

I can't figure out how to have it prioritize shrinking one of the empty spaces first.

https://youtu.be/G3e-cpL7ofc?t=16529

1:15pm. Let me stop here. At this point I am not even watching the course, but doing my own research. I should just finish the rest of it, and move on. I already know quite a bit of layouting. Let me do the chores here.

2:40pm. Done with breakfast and chores. Let me resume the video. Today I won't strain myself till 8pm like yesterday.

https://youtu.be/7khSaA91e04
Creating squishy padding and margin that adapt to the viewport

Let me watch this first.

3:10pm. https://youtu.be/G3e-cpL7ofc?t=17719

I do not like this method at all.

3:30pm. https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors

So you can match attributes in CSS. I see.

Focus me. Let me go back to the tutorial.

https://youtu.be/G3e-cpL7ofc?t=18825

Oh this could be useful.

3:50pm. https://youtu.be/G3e-cpL7ofc?t=20028

I haven't exercised the positionings, but they are each to grasp.

Let me just go forward through the video.

https://youtu.be/G3e-cpL7ofc?t=20854

I need to remember that the two are reversed when I use column.

https://youtu.be/G3e-cpL7ofc?t=21225

I wonder if I chould position these boxes using `top: 100%`. it wouldn't surprise me if that were possible.

https://youtu.be/G3e-cpL7ofc?t=21379

I had no idea it was possible to nest classes like this.

https://youtu.be/G3e-cpL7ofc?t=21475

Let me give this a try. Forget the sidebar, but I want to see if top:100% would work.

```css
.search-bar-magni-glass-box .tooltip {
    display: none;
    position: absolute;
    background-color: gray;
    color: white;

    top: 100%;
    left: -10%;
    right: -10%;
    text-align: center;
}

.search-bar-magni-glass-box:hover .tooltip {
    display: inline;
}
```

It works really great. Let me resume the video.

https://youtu.be/G3e-cpL7ofc?t=21507

Come to think of it, he realy doing the beginners a disservice by using pixel measurements everywhere.

https://youtu.be/G3e-cpL7ofc?t=21530

Not a good method. You really want to also disable the tooltip when it is not being hovered. Otherwise it might be possibel to select it even when it not ostensibly visible.

https://youtu.be/G3e-cpL7ofc?t=21686

Actually, this was a better solution than I gave it credit for. It is not possible to select the text when it is like this.

...Actually, if I do Ctrl+A to select everything on the page, and then paste it into a text file, I do see the qwerty. I see.

But this isn't a problem.

https://youtu.be/G3e-cpL7ofc?t=21784

I'll definiltey forget about this property, but nevermind it. A search will do.

https://www.w3schools.com/cssref/pr_text_white-space.php

> 	Whitespace is preserved by the browser. Text will only wrap on line breaks. Acts like the <pre> tag in HTML

Hmmm really?

```fs
        Html.pre [
            // prop.style [
            //     style.whitespace.
            //     ]
            prop.children[
                Html.text "qwe              "
                Html.br []
                Html.text "asd "
                Html.br []
                Html.text "zxc "
                ]
            ]
```

Ok, I'll definitely remember this. I thought it was impossible to get HTML to preserve whitespace, but it turns out it is pretty easy.

4:35pm. https://www.justetf.com/en/etf-profile.html?groupField=none&sortField=sixMonthReturnEUR&sortOrder=desc&from=search&isin=DE0006289309#chart

I peeked at the market and I see QQQ is dumping again. I thought for a moment - I must be wrong, better get out, but then remembered that my recommendation on Feb 3rd was not to buy tech stocks, but european banking stocks. Hypothetically, had I gone long that instead of losing 5%, I'd be up that amount right now! What about Turkey?

https://www.justetf.com/en/etf-profile.html?groupField=none&sortField=sixMonthReturnEUR&sortOrder=desc&from=search&isin=IE00B1FZS574#chart

My sense given the huge bad news is that it is acting extremely bullish. If stocks wanted to go down, they wouldn't be whipping around like this, giving people a chance to get out, they'd just dump! My Feb 3rd timing wouldn't have been good though.

4:45pm. Nevermind this, let me watch to the end of the HTML course.

https://www.justetf.com/en/etf-profile.html?groupField=none&sortField=sixMonthReturnEUR&sortOrder=desc&from=search&isin=IE00B1FZS574#chart

Finally, time for the last lecture. I am barely awake here.

I am only holding on thanks to my iron will. I am going to be sleeping well tonight.

https://youtu.be/G3e-cpL7ofc?t=22420

Instead of doing it like this, it would be better to just maybe adjust the font size of the root items. Assuming one is using relative measurements, that would smoothly propagate the changes. I wonder if one could also use it to set variables.

And instead of adjusting the grid sizes like this, it would be better to just use flex boxes with wraping.

Come to think of it, there are resolution agnostic apps. You know those annoying ones that don't change size when I zoom. Though I am betting those use viewport measurements. I do not like those. I won't use them in my own frontend work.

5:20pm. I am done here. Finally done with the HTML course. Now I know enough to be effective. I can go back to the React course.

Not right now though.

5:30pm. Studying really is hell, but learning new things is satisfying at some level at the same time.

This material is just like I imagined it to be. Not at all difficult to master, but it takes some effort to go through the tedioum of actually learning it.

5:35pm. I just need React, and I will be set as far as webdev frontend work is concerned. After that I'll be able to focus on the backend work.

I need to boild of my councurrent programming foundation and attain the skills that I can actually use to make money in the market.

I said I would bluff on the resume, but there is no need to go that far. Instead what I need is to actually put the requested tech in the job posts on my resume. If that fails, then that I can take as a signal to mess around with my state experience.

The poor response rate is part in due to the market, partly due to representing myself as a hobbyist, partly due to not have the requisite tech stack skills on the places I am applying to.

I'll deal with the cases one by one.

In the worst case, I can apply to those places that only give out equity. I'll see how things go.

Even if the job market might be poor, I doubt many people are interested in working at startups that pay monopoly money.

I am going to have my revenge at places that rejected me by getting a far higher paying job than those. There is also A Team to consider.

Right now, though I am filled to the brim with work. I need to go through my studies first."

---
## [maxhellwig/nodebar](https://github.com/maxhellwig/nodebar)@[47fd6321bf...](https://github.com/maxhellwig/nodebar/commit/47fd6321bf005028d4a0e15058fbdf0de94da0ae)
#### Wednesday 2023-02-22 16:59:04 by Max Hellwig

Introduce momentjs to easily format date-time, fuck you JavaScript..

---
## [Abynauts/CardsForHumanity](https://github.com/Abynauts/CardsForHumanity)@[31e15bd22d...](https://github.com/Abynauts/CardsForHumanity/commit/31e15bd22d1eff109c676d1889da2c9d9eacc5d4)
#### Wednesday 2023-02-22 17:03:24 by Abynauts

NF

Did a couple things:

-Changed the card width to something a bit thinner

-Fixed the hitbox size on the Card Actor. Was being affected by the text box's "Draw Size" in the Actor BP

-Added a "Deck" object class in the Data folder. This general data-container object is meant to hold two arrays and a string: One array containing "Black Card" structs, one array containing the text for the white cards (I realized having an "answer count" on white cards was pointless, which would've wasted storage space on creation), and one Text variable containing the name of the deck.
              -If we want to add different types of cards for future game modes, this is the place to store them.
               This is also what will get saved to the savegame class to maintain decks between sessions. This
               is also what our game should reference when deciding which decks to sort into that game's
               overall card pool. (Note: I haven't set up that savegame class yet)

-Last, I set up the basic Funny Forge interface, now accessible via clicking on that card. I haven't set up any of the buttons yet—formatting that fucking piece of shit took most of my time today and I'm kinda upset spaghet about it.

---
## [insertnamehere123/cmss13](https://github.com/insertnamehere123/cmss13)@[7731fa738f...](https://github.com/insertnamehere123/cmss13/commit/7731fa738f01b0c83dce6183a3e58387984926bf)
#### Wednesday 2023-02-22 17:06:21 by naut

A small assortment of more fortunes (#2643)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

> _"When you look through rose-colored glasses, all the red flags just
look like flags."_

Adding to the fortune cookie poll once again with some nice
inspirational quotes and bits to help someone's mood. Contains an
assortment of movie/TV quotes, inspirational words, and quotes from real
people. Yes, real people.

Also alphabetizes the fortunes.txt file to make everything more tidy.
Unfortunately this also demolishes the diff file, so the new fortunes
are provided below instead.

# Explain why it's good for the game

A little more motivation never hurt anyone, eh?
Change comes from embracing the future, not fighting your past.

# New Fortunes

<details>
<summary>Click to expand</summary>

```
A broken vase is more interesting than a perfect one.
A bruise is a lesson, and each lesson makes us better.
After all, tomorrow is another day.
All we have to decide is what to do with the time that is given to us.
Be the reason someone thinks life is worth living.
Be the reason someone wants to wake up in the morning.
Change comes from embracing the future, not fighting your past.
Do the thing that scares you the most.
Don't let anyone ever make you feel like you don't deserve what you want.
Embrace a new narrative.
Enter unknown territory.
Every day, in every way, you are getting better and better.
Every new beginning comes from some other beginning's end.
Everything always goes wrong. You just have to deal with it.
Everything you do is your life's work.
Evolve as a human.
Expect great things of yourself before you do them.
Follow your heart and see what turns up.
Fortune and glory.
Generosity is its own form of power.
Get busy living or get busy dying.
Get lost in the right direction.
Get out of your comfort zone. It's not even that comfortable.
Good instincts are worthless if you don't follow them.
Good news: the light at the end of the tunnel is not a train.
Great men are not born great, they grow great.
Happiness is not something ready made. It comes from your own actions.
I never dreamed about success. I worked for it.
If we wait until we're ready, we'll be waiting for the rest of our lives.
Imperfections are beautiful.
It's not our abilities that show what we truly are. It's our choices.
It's what you do right now that makes a difference.
Live in the constant unexpected.
Look how far you've come.
Love doesn't have to be a person. It can be a passion.
Love yourself, conquer your fears!
Loving yourself isn't vanity; it's sanity.
Make someone laugh today.
Make someone smile today.
Mind over matter.
Never be cruel, never be cowardly. And never ever eat pears.
Never forget who you are. The rest of the world will not. Wear it like armor and it can never be used to hurt you.
Never let anyone tell you what you can't do.
No man is good enough to govern another man without that other’s consent.
Normal is nothing more than a cycle on a washing machine.
Nothing can dim the light that shines from within.
Oh yes, the past can hurt. But you can either run from it, or learn from it.
One day you’ll look back at right now and say, 'If I got through that, I can get through anything.' And that will truly be a gift.
Recognize yourself in others.
Some people can't believe in themselves until someone else believes in them first.
Surviving is the least we can do.
The present is just one chapter of your own novel.
The weirdest people happen to be the most successful.
Turn wounds into wisdom.
We all make choices, but in the end, choices make us.
What people call you weird for is in fact your greatest strength.
While there's life, there's hope.
Why are you trying so hard to fit in when you were born to stand out?
Worrying means you suffer twice.
You are your best thing.
You attract what you are ready for.
You can discover a whole new world by just adjusting how you see everything.
You cannot live your life to please others. The choice must be yours.
You don’t lead by pointing and telling people some place to go. You lead by going to that place and making a case.
You make your own luck.
You'll never meet someone who isn't important.
You're never alone in your struggles.
```

</details>

Some of my favorites:

> Why are you trying so hard to fit in when you were born to stand out?
> Never let anyone tell you what you can't do.
> You don’t lead by pointing and telling people some place to go. You
lead by going to that place and making a case.
> Good instincts are worthless if you don't follow them.

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
add: Added several new fortunes to fortune cookies.
code: Alphabetized the fortunes.txt file for fortune cookie blurbs.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [insertnamehere123/cmss13](https://github.com/insertnamehere123/cmss13)@[4c373316ad...](https://github.com/insertnamehere123/cmss13/commit/4c373316ad1e9a68e5cd7ae0e216bddcd52ee3aa)
#### Wednesday 2023-02-22 17:06:21 by NewyearnewmeUwu

Alerts admins whenever humans try to gib another human. (#2560)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
Successor to #2237 that properly addresses the issues brought up by
myself and others. This sends a admin alert similar to when a pred
activates their SD that allows admins to jump to the (strictly human)
player gibbing another human/human corpse and sleep them/amessage them.
This also creates logs when someone _attempts_ to stuff someone into a
gibber. I also fixed up some of the single letter variables in the
gibber code.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

Insanity RP is bad, and this solution allows admins to respond in
realtime. It takes 30 seconds to gib another human as a human, without
any skill modifiers helping. It also doesn't flag the player if they're
a pred, as they're _supposed_ to be doing funny human meat stuff.
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
code: gibbing another human takes an unmodifiable 30 seconds
admin: admins are alerted when a human tries to gib another human
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [kanchamreddynaveen/vishnu_git](https://github.com/kanchamreddynaveen/vishnu_git)@[a09760b2a6...](https://github.com/kanchamreddynaveen/vishnu_git/commit/a09760b2a60d5497ad17ad5a8e56886988d653d2)
#### Wednesday 2023-02-22 17:16:51 by kanchamreddynaveen

Merge pull request #2 from kanchamreddynaveen/my_first_branch

fuck you vishnu

---
## [aws/aws-lc](https://github.com/aws/aws-lc)@[4263903bd1...](https://github.com/aws/aws-lc/commit/4263903bd1d15d56c47cbd6440bea657df2c142e)
#### Wednesday 2023-02-22 17:24:47 by David Benjamin

Maintain a frame pointer in aesni-gcm-x86_64.pl and add SEH unwind codes

Some profiling systems cannot unwind with CFI and benefit from having a
frame pointer. Since this code doesn't have enough register pressure to
actually need to use rbp as a general register, this change tweaks
things so that a frame pointer is preserved.

As this would invalidate the SEH handler, just replace it with proper
unwind codes, which are more profiler-friendly and supportable by our
unwind tests. Some notes on this:

- We don't currently support the automatic calling convention conversion
  with unwind codes, but this file already puts all arguments in
  registers, so I just renamed the arguments and put the last two
  arguments in RDI and RSI. Those I stashed into the parameter stack
  area because it's free storage.

- It is tedious to write the same directives in both CFI and SEH. We
  really could do with an abstraction. Although since most of our
  functions need a Windows variation anyway.

- I restored the original file's use of PUSH to save the registers.
  This matches what Clang likes to output anyway, and push is probably
  smaller than the corresponding move with offset. (And it reduces how
  much thinking about offsets I need to do.)

- Although it's an extra instruction, I restored the original file's
  separate fixed stack allocation and alloca for the sake of clarity.

- The epilog is constrained by Windows being extremely picky about
  epilogs. (Windows doesn't annotate epilogs and instead simulates
  forward.) I think other options are possible, but using LEA with an
  offset to realign the stack for the POPs both matches the examples in
  Windows and what Clang seems to like to output. The original file used
  MOV with offset, but it seems to be related to the funny SEH handler.

- The offsets in SEH directives may be surprising to someone used to CFI
  directives or a SysV RBP frame pointer. All three use slightly
  different baselines:

  CFI's canonical frame address (CFA) is RSP just before a CALL (so
  before the saved RIP in stack order). It is 16-byte aligned by ABI.

  A SysV RBP frame pointer is 16 bytes after that, after a saved RIP and
  saved RBP. It is also 16-byte aligned.

  Windows' baseline is the top of the fixed stack allocation, so
  potentially some bytes after that (all pushreg and allocstack
  directives). This too is required to be 16-byte aligned.

  Windows, however, doesn't require the frame register actually contain
  the fixed stack allocation. You can specify an offset from the value
  in the register to the actual top. But all the offsets in savereg,
  etc., directives use this baseline.

Performance difference is within measurement noise.

This does not create a stack frame for internal functions so
frame-pointer unwinding may miss a function or two, but the broad
attribution will be correct.

Change originally by Clemens Fruhwirth. Then reworked from Adam
Langley's https://boringssl-review.googlesource.com/c/boringssl/+/55945
by me to work on Windows and fix up some issues with the RBP setup.

Bug: b/33072965, 259
Change-Id: I52302635a8ad3d9272404feac125e2a4a4a5d14c
Reviewed-on: https://boringssl-review.googlesource.com/c/boringssl/+/56128
Reviewed-by: Adam Langley <agl@google.com>
Commit-Queue: David Benjamin <davidben@google.com>
(cherry picked from commit 0d5b6086143d19f86cc5d01b8944a1c13f99be24)

---
## [cnopt/gt-telemetry](https://github.com/cnopt/gt-telemetry)@[34eba0a2ff...](https://github.com/cnopt/gt-telemetry/commit/34eba0a2ff467d6869fba1f2c3ea03f10d02c895)
#### Wednesday 2023-02-22 17:45:46 by chad

speedo react component from other project, holy shit it actually works . interpolation function to map the recieved throttle vals 0-255 to 0-100, then use that value to change the height of the div inside music rally speedo component. actually works really well fucking hell im happy with that

---
## [granodd/Citadel-Station-13-RP](https://github.com/granodd/Citadel-Station-13-RP)@[81c1229373...](https://github.com/granodd/Citadel-Station-13-RP/commit/81c1229373208790c3375a138579aaf76a0006d0)
#### Wednesday 2023-02-22 18:56:30 by Captain277

Adds Just Like, a Ton of Clothes (#5048)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

1. **Adds a wide array of clothes, listed below.**

## Why It's Good For The Game

1. _My good friend Tech provided me with some sprite sheets when I was
working on Ashlanders, requesting a hobo coat. Going through the sheets
I found several different items I thought it would be fun to add to our
expanding list of customization and fashion options. The list is huge so
I'm just gonna itemize it here. As for attributions, as I understand it
most of this is from a D&D server, and some from a 40k server._
2. _Two of the outfits, the Belial and Lilin items, are sprites crafted
by our very own Doopy, as part of their Lindenoak line!_

## Outfits & Where to Get them

**Costume Vendor**
1. _Banana Costume_
3. _Hashashin Costume_
4. _Bard Hat_
5. _Aquiline Enforcer Uniform_
6. _Scavenging Sniper Set_
7. _Spiral Hero Outfit_
8. _Body Tape Wrapping_
9. _Redcoat Uniform_
10. _Despotic General Uniform_
11. _Post-Revolution American Uniform_
12. _Prussian Uniform_

**Suit Vendor**
1. _Ragged Coat_
2. _Spiral Hero Cloak_
3. _Nerdy Shirt_

**Jumpsuit Vendor**
1. _Toga_
2. _Countess Dress_
3. _Baroness Dress_
4. _Revealing Cocktail Dress_
5. _Belial Striped Shirt and Shorts_
6. _Lilin Sash Dress_

**Shoes Vendor**
1. _Utilitarian Shoes_

**Loadout**
1. _Ragged Coat_
7. _Spiral Hero Cloak_
8. _Nerdy Shirt_
9. _Bard Hat_
10. _Utilitarian Shoes_
11. _Toga_
13. _Countess Dress_
14. _Baroness Dress_
15. _Scavenging Sniper Set_
16. _Spiral Hero Outfit_
17. _Body Tape Wrapping_
18. _Revealing Cocktail Dress_
19. _Belial Striped Shirt and Shorts_
20. _Lilin Sash Dress_

**Medieval Armor Supply Crate**
1. _Crimson Knight Armor_
2. _Forest Knight Armor_
3. _Hauberk_
4. _Elite Paladin Armor, Helmet, and Boots_
5. _Alternate Knight Helmet_

**Cryosuit Supply Crates (Under Voidsuit Menu)**
1. _Cryosuit, Variants: Security, Engineering, Atmos, Mining_

**Crafting Menu**
1. _Duraskull Helmet_

**Ashlander Specific Crafting Menu**
1. _Ashen Vestment_
2. _Ashen Tabard_

**Ashlander Spawn**
1. _Priests now spawn with the Ashen Vestment._

**Admin Spawn**
1. _Actual armored versions of all new Knight sets._
5. _Utilitarian Military Helmet, Armor, and Boots._

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
add: Adds a wide array of new clothing items. Itemized in PR. #5408
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [fleetdm/fleet](https://github.com/fleetdm/fleet)@[6091556b7a...](https://github.com/fleetdm/fleet/commit/6091556b7a6f69f92b7bbb590b5a3068c3a4558d)
#### Wednesday 2023-02-22 19:00:48 by Mike McNeil

Fix build (#10018)

mikermcneil
  3 minutes ago
@Kathy Satterlee
 I think https://github.com/fleetdm/fleet/pull/9881 broke the build
4 replies

 .
mikermcneil
  2 minutes ago
https://github.com/fleetdm/fleet/pull/9979#issuecomment-1440604277


Zay Hanlon
  1 minute ago
Oops. That was my approval/merge on Kathy's change


Zay Hanlon
  1 minute ago
How do I fix?


mikermcneil
  < 1 minute ago
@Zay Hanlon
All good. I think we should make it so that PRs can't be merged until
they pass the CI checks. It's annoying but would prevent things like
this, which are expensive and involve multiple folks' time.
@Zach Wasserman
 
@Luke Heath
I'm going to turn on the branch protection that prevents merging when
automated CI checks are failing.
@Kathy Satterlee
 I'll follow up with a fix now.
@Jarod Reyes
 Feel free to go ahead and merge your PR in the meantime.


Zay Hanlon
:spiral_calendar_pad: [11 minutes
ago](https://fleetdm.slack.com/archives/C01EZVBHFHU/p1677091760162369?thread_ts=1677091575.384279&cid=C01EZVBHFHU)
Sorry :disappointed:


mikermcneil
[10 minutes
ago](https://fleetdm.slack.com/archives/C01EZVBHFHU/p1677091789685699?thread_ts=1677091575.384279&cid=C01EZVBHFHU)
All good, inevitable


Zach Wasserman
[9 minutes
ago](https://fleetdm.slack.com/archives/C01EZVBHFHU/p1677091841779269?thread_ts=1677091575.384279&cid=C01EZVBHFHU)
FWIW turning that on will really slow down my dev process at times.


Zach Wasserman
[8 minutes
ago](https://fleetdm.slack.com/archives/C01EZVBHFHU/p1677091942206439?thread_ts=1677091575.384279&cid=C01EZVBHFHU)
eg. if I make one tiny change on a PR that I already know passes all the
tests then I'll have to wait 15 mins for the whole CI to run before I
can merge.


mikermcneil
[7 minutes
ago](https://fleetdm.slack.com/archives/C01EZVBHFHU/p1677091967828479?thread_ts=1677091575.384279&cid=C01EZVBHFHU)
it was an indentation issue:
https://github.com/fleetdm/fleet/pull/10018/files#diff-68623aac08ce48b5c1275a38ea9f42a8a730a9c2e04ab1946174cdc67f4ce686R8
:ty:
1



Luke Heath
[7 minutes
ago](https://fleetdm.slack.com/archives/C01EZVBHFHU/p1677092006055779?thread_ts=1677091575.384279&cid=C01EZVBHFHU)
Is it possible to conditionally enable the required CI checks?


Zach Wasserman
[6 minutes
ago](https://fleetdm.slack.com/archives/C01EZVBHFHU/p1677092018873739?thread_ts=1677091575.384279&cid=C01EZVBHFHU)
Maybe you can just turn on a limited set of checks that we know go
really fast and have a high true-positive rate?


Luke Heath
[6 minutes
ago](https://fleetdm.slack.com/archives/C01EZVBHFHU/p1677092062859149?thread_ts=1677091575.384279&cid=C01EZVBHFHU)
That's a good idea. FWIW we'll be removing e2e test runs in CI later
this week, which will reduce the CI run time by ~25 minutes.


mikermcneil
[< 1 minute
ago](https://fleetdm.slack.com/archives/C01EZVBHFHU/p1677092432337109?thread_ts=1677091575.384279&cid=C01EZVBHFHU)
This is not the first time this has happened and I'd like to put an end
to the emergency remediation that takes a chunk of the day's focus away
from multiple people each time it occurs. If it causes a drain on our
ability to move quickly, let's def change it back. If it's worth the
friction (like the PR approval restriction), then we can keep it.
I'm running into the problem of being able to select the "test-website"
job from [this
list](https://github.com/fleetdm/fleet/settings/branch_protection_rules/18283834),
likely because it is already conditional:
image.png

---
## [Sol-Client/client](https://github.com/Sol-Client/client)@[3aa386e90f...](https://github.com/Sol-Client/client/commit/3aa386e90f2a18e02a9878f489db71751d6f2628)
#### Wednesday 2023-02-22 19:09:59 by TheKodeToad

Bye launcher :cry:!

This launcher all began on the 31st of October, 2020. It was made in
Java, and only capable of launching the vanilla game.

Soon afterwards, I tried developing an actual client to launch. I didn't
want to use MCP, because I prefered mixin. I'd already made a standalone
mixin server using LaunchWrapper and looking at
https://github.com/CodeCrafter47/Rainbow/ amongst other projects - for
1.16.

However, I couldn't get either Legacy Fabric or ForgeGradle to work
nicely, neither could I get the LaunchWrapper service to work for some
reason (plus I didn't have a Discord account). I somehow ended up doing
asm which wasn't nice. I tried using some build-time stuff to remap
string constants containing mappings. The first feature of this client I
tried to implement was something to make it so that pressing F3+C *only*
cleared the chat rather than bringing up the whole overlay too. This was
hard!

Eventually I gave up and after explaining to my friend that it was
causing me to (metaphorically) tear my hair out, I finally opted for
MCP. Later on I managed to get MCP working with OptiFine and distributed
the launcher with a crude autoupdater to this friend.

One day, I spammed !polycatgen commands on the PolyMC Discord (before
all of the drama happened - well at least the most recent one) and
nearly got banned or muted (I can't remember). This is unrelated, but
funny! On the same day (I can't verify because I'm now banned!), I
started working on an electron launcher but it didn't go anywhere.

When I saw my friend had migrated, I tried to add a feature to support
this. Since the launcher code was made before Microsoft accounts to play
the game were a thing, adding it was a lot of effort. I couldn't work
out how to register an application so used a webview (mistake).
MiniDigger had a good JavaFX example but this project was swing so it
needed to be embedded. This didn't go well and the Linux JDK doesn't
have JavaFX bundled so eventually I returned to the Electron launcher.
This is the launcher this commit finally rids the world of (if merged)!

p.s. my hair has been growing without being cut this whole time which is
cool

---
## [SunnySharma01/Acciojob](https://github.com/SunnySharma01/Acciojob)@[a8901c5e4f...](https://github.com/SunnySharma01/Acciojob/commit/a8901c5e4f5ddb8b7e061e89f6818ed7b456632d)
#### Wednesday 2023-02-22 19:10:38 by SunnySharma01

Ptice

Ptice
Adrian, Bruno and Goran wanted to join the bird lovers’ club. However, they did not know that all applicants must pass an entrance exam. The exam consists of n questions, each with three possible answers: A, B and C.

Unfortunately, they couldn’t tell a bird from a whale so they are trying to guess the correct answers. Each of the three boys has a theory of what set of answers will work best:

Adrian claims that the best sequence is: A, B, C, A, B, C, A, B, C, A, B, C ...

Bruno is convinced that this is better: B, A, B, C, B, A, B, C, B, A, B, C ...

Goran laughs at them and will use this sequence: C, C, A, A, B, B, C, C, A, A, B, B ...

Write a program that, given the correct answers to the exam, determines who of the three was right – whose sequence contains the most correct answers.

Input Format
First line contains an integer n denoting number of questions.

Second line contains a string of n letters ‘A’, ‘B’ and ‘C’. These are, in order, the correct answers to the questions in the exam.

Last line contains the indices separated by space.

Output Format
On the first line, output m, the largest number of correct answers one of the three boys gets.

After that, output the names of the boys (in alphabetical order) whose sequences result in m correct answers.

Example 1
Input

5
BAACC
Output

3
Bruno
Explanation

Here only Bruno has most correct answers i.e. 3.

Example 2
Input

9
AAAABBBBB
Output

4
Adrian
Bruno
Goran
Explanation

Here all 3 have 4 correct answers.

Constraints
1 <= n <= 100

---
## [delphix/linux-kernel-aws](https://github.com/delphix/linux-kernel-aws)@[9bd96fdf28...](https://github.com/delphix/linux-kernel-aws/commit/9bd96fdf28450ec3266fad2e5a183c63fa646dfe)
#### Wednesday 2023-02-22 19:11:47 by Masahiro Yamada

kbuild: remove the target in signal traps when interrupted

BugLink: https://bugs.launchpad.net/bugs/1996812

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
Signed-off-by: Kamal Mostafa <kamal@canonical.com>
Signed-off-by: Stefan Bader <stefan.bader@canonical.com>

---
## [CalaMariGold/TREPIDATION](https://github.com/CalaMariGold/TREPIDATION)@[fe14d9f7db...](https://github.com/CalaMariGold/TREPIDATION/commit/fe14d9f7db0d0b5654fdb2555f59d9ab09a51e32)
#### Wednesday 2023-02-22 20:48:15 by Mari

Death Compass now has Curse of Vanishing, fixed death menu

- Idea by Gryph, Void Mama
- Prevents cluttering inventory with chain deaths
- Kinda lore accurate too since it should only point towards the magic grave, which disappears after another death

---
## [PhantomEpicness/cmss13](https://github.com/PhantomEpicness/cmss13)@[5f78464e25...](https://github.com/PhantomEpicness/cmss13/commit/5f78464e255b89ada7ca58f5114561be7b32f055)
#### Wednesday 2023-02-22 20:51:47 by NewyearnewmeUwu

Removes skull balaclava and skull facepaint from loadout, places them hidden on the Almayer. (#2526)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

This removes the skull balaclavas and the facepaints from the loadout
menu and instead places them in 2 places hidden around the Almayer. The
reason I have done this is that they are almost exclusively used by
people who who are referencing a character- usually Ghost from MW2
(either version) or the characters from COD Ghosts. See below for more
details.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

This is an OOC meme item that doesn't fit the tone of CM, particularly
because we _already_ have an item with a skull on it in case you want to
use it: Armor! They wrote things on armor in the movie, including a
skull!

![image](https://user-images.githubusercontent.com/70115628/215395714-4aa1c9a2-7621-4f82-8e4b-6d7ed4905f89.png)

Instead, we have these types of people, running a skull 'clava in every
round even as command or medical characters. This is a modern 'operator'
look, not a Space 'Nam-esque look and not an Aliens look. If you want
something that'd remind you of Space 'nam, just look at the classic
'born to kill' helmet. Now, look at these CALL OF DUTY CHARACTERS THAT
THIS ITEM REFERENCES!


![image](https://user-images.githubusercontent.com/70115628/215396029-290063ae-cd96-4929-b6f0-ae2f1c517887.png)

![image](https://user-images.githubusercontent.com/70115628/215396040-0eb9e31f-71ed-408a-8248-152916427bdd.png)

![image](https://user-images.githubusercontent.com/70115628/215396561-f4493f24-2405-4b8d-8034-02a96ea6919f.png)

This is goofy as hell and kind of an outlier among the customization
options since it is _very clearly_ a reference to COD. Look at its
description:

"The face of your nightmares. Heed the call of duty as the ghost in the
night with this metal 'clava. Additionally protects against the cold.
Now in black!"

You'd get laughed off a real marine base for wearing this, let alone
wearing one on an op. We don't need more people running this every
round, and this gives them something to fight over between eachother- if
_you_ want to larp as Simon 'Ghost' Riley from hit video game COD MW2
(either version) then you'll have to hunt it down.
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
del: Removed skull balaclavas and skull facepaint from the loadout
options
maptweak: adds a single skull facepaint and balaclava, each hidden in
their own locations on the Almayer.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [CapCamIII/cmss13](https://github.com/CapCamIII/cmss13)@[7f1e80ca3d...](https://github.com/CapCamIII/cmss13/commit/7f1e80ca3dd4800f54b5ff4dc3663dd1f804c28c)
#### Wednesday 2023-02-22 20:52:20 by carlarctg

MIDIs are now either 'Meme' or 'Atmospheric', players can toggle each option (#1939)

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

Updated savefile number from 19 to 20. Meme and atmospheric preferences
are enabled by default.

Admin sounds now need a selection between 'Meme' or 'Atmospheric' type.
Ideally, this would let players decide if they want to listen to hijack
or first drop songs without needing to listen to GOOD HITS or whatnot.

I am uncertain about the savefile bit of code. I don't fully understand
it.

As stated I don't care about GBP, so if the tags are teechnicallly
incorrect go ahead and change them or whatever.

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

> Admin sounds now need a selection between 'Meme' or 'Atmospheric'
type. Ideally, this would let players decide if they want to listen to
hijack or first drop songs without needing to listen to GOOD HITS or
whatnot.

As it says. Lots of people hate the memes and just want to listen to the
cool atmosphere. This is of course dependant on staff selecting the
right option, which is sometimes up to opinion, but I fully trust staff
will be able to handle this subjective affair correctly.

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
refactor: Updated savefile number from 18 to 19. Meme and atmospheric
preferences are enabled by default.
admin: Admin sounds now need a selection between 'Meme' or 'Atmospheric'
type. Ideally, this would let players decide if they want to listen to
hijack or first drop songs without needing to listen to GOOD HITS or
whatnot.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

Co-authored-by: Stan_Albatross <66756236+stanalbatross@users.noreply.github.com>

---
## [PhantomEpicness/cmss13](https://github.com/PhantomEpicness/cmss13)@[dce3a1df12...](https://github.com/PhantomEpicness/cmss13/commit/dce3a1df1290b2324fb0be77087e9ecd4f3db36d)
#### Wednesday 2023-02-22 21:00:35 by Epicness

told you not to remove it yet you remove it, fuck you gitkraken

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[3b388f01aa...](https://github.com/treckstar/yolo-octo-hipster/commit/3b388f01aa0540235af1361bd13d1a23b8584ca9)
#### Wednesday 2023-02-22 21:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [LuminarLight/jak-project](https://github.com/LuminarLight/jak-project)@[c249dbc437...](https://github.com/LuminarLight/jak-project/commit/c249dbc43750b0b811bbe4d10d29663bec39b9ae)
#### Wednesday 2023-02-22 21:47:06 by water111

[jak2] improve loader for jak 2 levels (#2206)

Add a debug window for the loader to show levels and fix an issue with
jak 2 level unloading. I never really thought about how this works for >
2 levels, and there is a chance that you could unload the wrong level in
some cases.

The problem is some combination of merc-only levels not counting toward
the "in use" detection, and the unloader ignoring what the game wants to
load.

I don't remember why using merc models doesn't contribute to "in use"
but I'm afraid to change this for jak 1. Instead, we can have the
unloader avoid unloading levels that the game is telling us are loaded.
This is what we should have done originally, but there was a time when
Jak 1 didn't tell the loader anything, and we had this stupid detection
thing.

I think this is the first step toward just getting rid of the "in use"
detection and trusting the game for everything.

---
## [Valle-infinitare/discord-api-docs](https://github.com/Valle-infinitare/discord-api-docs)@[dd3f05a170...](https://github.com/Valle-infinitare/discord-api-docs/commit/dd3f05a1709add398bac3a68af3cc27287f67038)
#### Wednesday 2023-02-22 22:34:56 by Jerry Jiang

Document Silent Messages. (#5910)

Hey folks!

This is actually my 2022 hackweek project which I got to finish to
completion. :)

During a message send request, if you include the new
`SUPPRESS_NOTIFICATIONS` flag it will not broadcast any push/desktop
notifications but will still increment the relevant mention counters.

The intention is that you can get someone's attention but not feel like
you could be distracting them. Like when you DM someone at 5am. I'm sure some
bots can leverage this as well to avoid noise or something.

Also this should work for the webhook send request as well.

[Add a picture of the UI here]

If you're looking to leverage this as a non-bot, you can write `@silent`
as the _very first_ thing in a message. Make sure your client is
up-to-date btw. Autocomplete a-la `@everyone` is not planned. Eventually we may
put this in an "actual UI", for now this is where it lives. :)

Also sorry to all the users on Discord named silent who may have some
textual conflict now. Forgive me!

---
## [Vhmit/kernel_asus_msm8937](https://github.com/Vhmit/kernel_asus_msm8937)@[dd34d034ef...](https://github.com/Vhmit/kernel_asus_msm8937/commit/dd34d034efcafc0eb8eeac25272f5f97e8c1302b)
#### Wednesday 2023-02-22 22:57:50 by Steven Barrett

ZEN: Implement zen-tune v4.12

4.9:
In a surprising turn of events, while benchmarking and testing
hierarchical scheduling with BFQ + writeback throttling, it turns out
that raising the number of requests in queue _actually_ improves
responsiveness and completely eliminates the random stalls that would
normally occur without hierarchical scheduling.

To make this test more intense, I used the following test:

Rotational disk1: rsync -a /source/of/data /target/to/disk1
Rotational disk2: rsync -a /source/of/data /target/to/disk2

And periodically attempted to write super fast with:
dd if=/dev/zero of=/target/to/disk1/block bs=4096

This wrote 10gb incredibly fast to writeback and I encountered zero
stalls through this entire test of 10-15 minutes.

My suspicion is that with cgroups, BFQ is more able to properly sort
among multiple drives, reducing the chance of a starved process.  This
plus writeback throttling completely eliminate any outstanding bugs with
high writeback ratios, letting the user enjoy low latency writes
(application thinks they're already done), and super high throughput due
to batched writes in writeback.

Please note however, without the following configuration, I cannot
guarantee you will not get stalls:

CONFIG_BLK_CGROUP=y
CONFIG_CGROUP_WRITEBACK=y
CONFIG_IOSCHED_CFQ=y
CONFIG_CFQ_GROUP_IOSCHED=y
CONFIG_IOSCHED_BFQ=y
CONFIG_BFQ_GROUP_IOSCHED=y
CONFIG_DEFAULT_BFQ=y
CONFIG_SCSI_MQ_DEFAULT=n

Special thanks to h2, author of smxi and inxi, for providing evidence
that a configuration specific to Debian did not cause stalls found the
Liquorix kernels under heavy IO load.  This specific configuration
turned out to be hierarchical scheduling on CFQ (thus, BFQ as well).

4.10:
During some personal testing with the Dolphin emulator, MuQSS has
serious problems scaling its frequencies causing poor performance where
boosting the CPU frequencies would have fixed them.  Reducing the
up_threshold to 45 with MuQSS appears to fix the issue, letting the
introduction to "Star Wars: Rogue Leader" run at 100% speed versus about
80% on my test system.

Also, lets refactor the definitions and include some indentation to help
the reader discern what the scope of all the macros are.

4.11:
Increase MICRO_FREQUENCY_UP_THRESHOLD from 95 to 85
Increase MIN_FREQUENCY_UP_THRESHOLD from 11 to 6

These changes should help make using CFS feel a bit more responsive when
working with mostly idle workloads, browsing the web, scrolling through
text, etc.

Increasing the minimum frequency up threshold to 6% may be too
aggressive though.  Will revert this setting if it causes significant
battery drain.

4.12:
Make bfq the default MQ scheduler

Reduce default sampling down factor from 10 to 1

With the world eventually moving to a more laptop heavy configuration,
it's getting more important that we can reduce our frequencies quickly
after performing work.  This is normal with a ton of background
processes that need to perform burst work then sleep.

Since this doesn't really impact performance too much, lets not keep it
part of ZEN_INTERACTIVE.

Some time ago, the minimum frequency up threshold was set to 1 by
default, but the zen configuration was never updated to take advantage
of it.

Remove custom MIN_FREQUENCY_UP_THRESHOLD for MuQSS / ZEN_INTERACTIVE
configurations and make 1 the default for all choices.

Change-Id: I2a31fbc97fe12ffce30457ec2e83ed25764e2daf
Signed-off-by: Harsh Shandilya <msfjarvis@gmail.com>

---

