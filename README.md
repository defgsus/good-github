## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-11-26](docs/good-messages/2023/2023-11-26.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 3,950,948 were push events containing 4,666,030 commit messages that amount to 177,618,095 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 69 messages:


## [rust-lang-ci/rust](https://github.com/rust-lang-ci/rust)@[ee80c8d0a8...](https://github.com/rust-lang-ci/rust/commit/ee80c8d0a8bc63b69f68216c5d37f9ab837eedd0)
#### Sunday 2023-11-26 00:14:18 by bors

Auto merge of #117611 - Nadrieril:linear-pass-take-4, r=cjgillot

Rewrite exhaustiveness in one pass

This is at least my 4th attempt at this in as many years x) Previous attempts were all too complicated or too slow. But we're finally here!

The previous version of the exhaustiveness algorithm computed reachability for each arm then exhaustiveness of the whole match. Since each of these steps does roughly the same things, this rewrites the algorithm to do them all in one go. I also think this makes things much simpler.

I also rewrote the documentation of the algorithm in depth. Hopefully it's up-to-date and easier to follow now. Plz comment if anything's unclear.

r? `@oli-obk` I think you're one of the rare other people to understand the exhaustiveness algorithm?

cc `@varkor` I know you're not active anymore, but if you feel like having a look you might enjoy this :D

Fixes https://github.com/rust-lang/rust/issues/79307

---
## [silencer-pl/cmss13](https://github.com/silencer-pl/cmss13)@[e7caf52c21...](https://github.com/silencer-pl/cmss13/commit/e7caf52c21e01e4580cbf03ff1c61579054dd7a2)
#### Sunday 2023-11-26 00:28:36 by fira

Rewrite Xeno Acid processing (#4759)

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

Rewrites scheduling of xeno acid to hopefully finally be done with
dangling references warnings with acid. Also generally improves the
awful code quality

# Explain why it's good for the game
Like, dude, some of these values were outright inversed.
acid_**strength**=2.5 is noted as "250% speed" when it multiplies the
sleep delays. Can't leave code in that state.

# Testing Photographs and Procedure
Summary testing, timing appear correct overall but I'm not entirely
certain it's perfect due to random delays and obtuse code


# Changelog
:cl:
code: Rewrote Xeno Acid ticking code.
fix: Weather updates won't cause turfs to acid melt more rapidly anymore
/:cl:

---
## [silencer-pl/cmss13](https://github.com/silencer-pl/cmss13)@[e120ab795b...](https://github.com/silencer-pl/cmss13/commit/e120ab795ba0e92e4eb0f91fda194c59f83cb5aa)
#### Sunday 2023-11-26 00:28:36 by fira

Add Item & Footprints offsets (#4762)

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

This:
* Adds transverse offsets to blood footprints
* Adds notable pixel offsets to a few items
* Adds a very slight pixel offset to all items
* Enables rotation for thrown flashlights
* Cause objects exiting a surface (rack/table) to regenerate offset
instead of being stuck at center
* Stops random offsets from overwriting mapped offsets

# Explain why it's good for the game
The goal is to have map visuals more organic when we have a lot of
objects on the ground - targeting in particular items you find readily
in dense areas such as Reqs or a FOB.

Consider this for example, the blood footprints are all aligned, in more
extreme situations (eg WO) it makes an actual "grid" which i personally
find very immersion breaking

![image](https://github.com/cmss13-devs/cmss13/assets/604624/83883e15-a9a0-4a2d-aa90-41c785e047b9)

Adding a slight offset helps counter that:

![image](https://github.com/cmss13-devs/cmss13/assets/604624/504d1baf-385c-4774-86f3-6331c4ac87ed)

# Changelog
:cl:
add: Bloody footprints are now slightly offset to break long visual
straight lines.
fix: Items do not align back to the center of turfs anymore when picked
from a surface (table or rack)
add: Some more items now have offsets on the map display, and they all
can be slightly offset.
/:cl:

---------

Co-authored-by: harryob <me@harryob.live>

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[9229adc934...](https://github.com/lessthnthree/tgstation/commit/9229adc934b9575a8528b6efc0074fcc2921cc33)
#### Sunday 2023-11-26 00:29:09 by DaydreamIQ

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
## [mbland/tomcat-servlet-testing-example](https://github.com/mbland/tomcat-servlet-testing-example)@[9fa20e7a3c...](https://github.com/mbland/tomcat-servlet-testing-example/commit/9fa20e7a3cead69831345021e788fe5bf965d4b9)
#### Sunday 2023-11-26 00:41:59 by Mike Bland

Implement Servlet.doPost with TempStringCalculator

Contains copious comments explaining the reasoning behind the design and
testing choices. Illustrates:

- Writing a larger medium test (@MediumTest) that closely mirrors an
  actual deployment, including the production implementation
  (TemporaryStringCalculator).
- Writing smaller medium tests (@MediumCoverageTests) that use test
  doubles for StringCalculator to validate success and error paths
  through Servlet.doPost() thoroughly and quickly.

Had to update TestTomcat.start() to provide two variants:

- A no-arg variant that uses the actual web app config to start, as
  before, used by the @MediumTests.
- A variant that injects a Servlet directly, without the web app config,
  and that runs much faster as a result, used by the
  @MediumCoverageTests.

Adds lombok for common boilerplate generating annotations and Jackson
for JSON processing:

- https://projectlombok.org/
- https://plugins.gradle.org/plugin/io.freefair.lombok
- https://github.com/FasterXML/jackson

---

Continuing the rant from commit
0a4cd2c6b881a7cae27318f317c9a28e50c60e33...

I spent days of my life learning the following basic fact about using
Weld/CDI with Servlet instances:

- Servlets can't use constructor injection in production, because they
  are always created using a no-arg constructor (or, at least Tomcat
  always works that way).
- Servlets _must_ use field injection instead.

No matter how much I searched, I found _nothing_ in official
documentation, or online forums, or blog posts that spelled up the above
ground truth. I thought I was going crazy, like I wasn't asking the
question right, no matter how many different ways I tried.

I did find this one promising Stack Overflow question:

- https://stackoverflow.com/questions/58757320/constructor-injection-not-working-in-servlet-weld-tomcat

The poster's opening paragraph seemed to perfectly describe what I was
wrestling with:

> I have problem with Constructor Injection in CDI. Field or property
> injection works fine. Constructor Injection of Field injected
> instances works fine as well. The only thing is not working
> - constructor injection in Servlet Classes.

But, alas, that came from 2019-11-07, was updated 2019-11-11, and hasn't
been updated since with a definitive response.

(And then there's the arcane incantations I had to discover to inject a
Servlet directly into Tomcat... The amount of code involved does not
reflect the amount of time I had to invest to accomplish the task at
hand.)

If I was feeling constructive, maybe I would reply to that thread,
and/or send a proposed documentation update to the Weld folks or
something. But I'm not feeling that way, not after the agony of having
to arrive at such a basic conclusion myself. Someone who actually knows
these systems could've documented that years ago and saved me days that
I'll never get back.

Of course, maybe I could've asked someone, asked around, saved myself
some trouble. Maybe that's the lesson I should walk away with. But for
now, I'm still pretty sore at the Java ecosystem for trying to make
things so abstract and magical. It feels like this never should've been
a problem in the first place. No other language's ecosystem, at least
none amongst the many I've used over the years, seems to have ever
evolved in such an baroque direction.

I will say that, despite my frustration and the time it took, I'm rather
pleased with the results of this change. I think I was able to bang out
some decent tests, and decent abstractions to help write them. And I
have to give Java credit for introduing Lambda syntax for functional
interfaces, which made writing TestTomcat.setup() variants and
StringCalculator test doubles easier.

Plus, in the comments, I've got a draft of a bunch of future training
notes or slides or blog posts. Hopefully they'll prove helpful to folks
one day soon. That will almost make the effort seem worth it.

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[3db872708b...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/3db872708b62de8c22bfe14418cd6fcd67439621)
#### Sunday 2023-11-26 00:53:40 by SkyratBot

[MIRROR] Makes oculine taste slightly better [MDB IGNORE] (#25256)

* Makes oculine taste slightly better (#79919)

## About The Pull Request
Changes oculine's taste from 'dull toxin' to 'earthy bitterness'.
Probably deserves the no GBP tag.
## Why It's Good For The Game
Oculine is a benign/helpful chem that naturally occurs in carrots. This
means it's in all carrot based food the chef cooks, and if the carrots
cross pollinate with another plant it's in those too. This is currently
a problem, because it means the chef's carrot sticks taste like poison
and this tends to freak out new players who don't know that's just what
oculine tastes like.

Oculine has no negative effects besides potentially triggering a medical
allergy quirk, it can't even be overdosed. So if you see a worrying "you
taste dull toxin" message, there's actually no reason to be concerned.
Still, I see players who are *convinced* the chef is poisoning their
carrot cakes fairly regularly. This should cut down on wasted multiver
and lynched chefs.

I changed it to "earthy bitterness" because that's what some species of
carrot taste like, and "bitterness" implies medicine. The paranoid can
still assume they're being dosed with morphine or something, but they're
not being misled into thinking this. For people chugging medicine
bottles from chemistry, oculine stands out a little less too.
## Changelog
:cl:
qol: Oculine now tastes bitter, and not like toxin.
/:cl:

* Makes oculine taste slightly better

---------

Co-authored-by: Da Cool Boss <142358580+DaCoolBoss@users.noreply.github.com>

---
## [Sinbest/mojave-sun-13](https://github.com/Sinbest/mojave-sun-13)@[fe5d6c7b56...](https://github.com/Sinbest/mojave-sun-13/commit/fe5d6c7b568d550f403eb892ed47ffaf6b4fd28c)
#### Sunday 2023-11-26 01:07:26 by Technobug14

Agriculture (#2230)

* Does Stuff

Beginnings of agriculture code, stripped down TG botany a bunch, got rid of scar botany whilst replacing most of it. Also some map edits to change the paths on stuff and add a few spades for farming.

* Some NPK system framework

Removing more TG botany stuff and getting some framework down for NPK. Adds a "nutrient_type" variable to seeds and gives N, P or K as the type to every seed.

* Removes Stuff, More NPK Framework

Still WIP on NPK stuff, removes more basic bitch TG botany stuff, needs a lot more content but in an almost-working state

* Nutrient drain

Nutrients actually get drained properly now. Crop plots output their level of N, P and K when examined. Still need to make something to handle restoring nutrients and figure out a nutrient economy for plant consumption.

* Mostly working, one major bug

This is mostly working now. The NPK now drains according to the seed planted, it replenishes over time, you can now get water from water tiles and the soil will properly adjust the waterlevel variable with the new water types.

HOWEVER, big bug. The way TG handled watering crops is ass. Doesn't delete, stays in the reagent_container of the soil, normally checks for if a reagent_container has water to bypass how full the soil's container is, bad system that sucks. Needs fixing.

* oops

oopsie!!! fucked something!!! forgot to undo a change I made to the code, it's just there to remind me it's not working correctly

* Last minute fixes/bandaids

I HATE TG BOTANY I HATE TG BOTANY I'M LOSING IT

---
## [Doxbin16/Doxbin16](https://github.com/Doxbin16/Doxbin16)@[d30d9d908f...](https://github.com/Doxbin16/Doxbin16/commit/d30d9d908f85203771a3424bfa20e3442f9ee171)
#### Sunday 2023-11-26 01:18:30 by Doxbin16

Doxbin290..txt

You're Dox is Doxbin Pizza since I sent it to your house SWAT 
team busting down your door I just broke you vehicle you s is 
mine for real took your s fucking ordered Pizza to your 
house but now just now put you on Dox Doxbin sending 
SWAT team to you house ordered DICK😂😂🤡🤡😈😈
📞📞 911  Don't want to give you his information to 
Microsoft here's his email oliviarosa772@outlook.com 
password this is Doxbin290$$.com I got his information it is a 
modded GTA account he got one coming to him he couldn't
modded GTA account he got one coming to him he couldn't
crying entails that's why I post them on Dox Doxbin He's on  
just now send SWAT team to his house he is totally screwed 
if you want Go to give you his phone number to call 
3166177281 if you want just keep calling him and you keep 
and send people to his house SWAT team
I even should have down his Wi-Fi he had to get a whole new 
Wi-Fi box and he had to get this from his mom pussy he 
couldn't get it from his girlfriend so his mom just gave her 
son it the wall he couldn't stop tasting it he said it was so 
good it is Mom said keep doing that to me I like it like that 
dick That's what his mom means my means by that after the 
got done SWAT team came to the house broke down the 
door please somebody take his account I posted on Dox 
Doxbin it's for Xbox only
Come use it very powerful booter
Come use it very powerful
To send s SWAT team to people's house you s*** is mine 😂😂😈😈
hacker me daddy 316
first name and last name
put it right here 
to order to use it
answer to yes or no
ip.bat
text
Weave the comments 😂😂😈 😈 📞 📞 smoke a pack 
gotcha Bank and leave it back I'm maxed out all your credit 
cards at the bank called you back this now committed fraud 
order or dildos just for fun coming out soon very powerful 😂😂🤡🤡😈😈💀💀

---
## [5herlocked/wing](https://github.com/5herlocked/wing)@[edd91d42e5...](https://github.com/5herlocked/wing/commit/edd91d42e570089b614dafad3f02601686b22c82)
#### Sunday 2023-11-26 01:58:03 by Mark McCulloh

feat(sdk): inflights are not required to be resources (#4993)

## Huh?

The primary goal of this PR is to reduce the input required to create an inflight function in TS (See https://github.com/winglang/wing/issues/4842) without necessarily overhauling the compiler (yet). Ideally, the minimum information required for an inflight is simply the code itself. However, because inflights are currently modeled as resources, they require a scope and id.

So the first change was to make a new non-resource interface, IInflight, encompassing the inflight contract. The most important part of this contract is that inflights must be liftable, a behavior currently unique to resources and certain other primitives. So I extracted the lift-related functions from IResource and slapped them on the new ILiftable (which both IInflight and IResource now extend).

But that created a new problem: lifting itself also currently requires a scope. The only usage of the scope was to be able to resolve tokens. This did not seem like a good enough reason to require scope, so I changed token resolution to be more of a global concern rather than a tree-level concern. This is dangerous, but it's mostly only dangerous when you try to deal with tokens in a multi-app scenario, which would be dangerous with our current approach anyways. So this is something we'll have to add some extra handling for eventually anyways.

## Results

The primary outcome of this can be seen in the SDK unit tests, where the `Testing.makeHandler()` now only requires the code and (optional) bindings. This is basically 1 or 2 steps away from an ideal TS experience.

## But wait nothing changed in winglang

The original purpose of representing inflights as resources was to ease the implementation of lifting in the compiler and generally unify the logic of inflights between inflight closures and inflight methods of preflight classes. This hasn't changed in this PR. Luckily, the class instance emitted by the wing compiler for inflights still satisfies IInflight. It just has some extra hidden resource stuff that is simply unused. Assuming this PR is wanted, I will do a followup to change the compiler as well. This will be a more complicated change and I think it's useful to basically get the backend working first.

## Changes

- `Testing.makeHandler` now takes only code text and bindings. 9 billion tests were updated for this contract. `convertBetweenHandlers` changed similarly
- TokenResolvers are now globally registered and not tied to specific apps
- wingc adds a _hash private field to inflight closure resource classes to match the new IInflight (just an md5 hash)
- Many of the resources that deduped functions based on `addr` now do so with `_hash` instead
- Removed many occurrences of `this.node.id` used in resource ids when it's not necessary. The only time this should be necessary is if the resources is being created in the scope of this.node.scope instead
- Added a `Counter` concept to help with the many places that we want to add a subresource many times and a simple incrementing number will suffice for uniqueness and clarity
  - This was needed because the inflight `addr` was often relied upon to make this unique, but that will no longer be viable. I think it's better this way anyways

*By submitting this pull request, I confirm that my contribution is made under the terms of the [Wing Cloud Contribution License](https://github.com/winglang/wing/blob/main/CONTRIBUTION_LICENSE.md)*.

---
## [wesoda25/tgstation](https://github.com/wesoda25/tgstation)@[71b45e54ad...](https://github.com/wesoda25/tgstation/commit/71b45e54adfaa4c681babc545db97fa7103289de)
#### Sunday 2023-11-26 03:30:19 by san7890

Puts all traits in the globalvars file + CI Testing (#79642)

## About The Pull Request

Fixes #76349

I didn't know that people needed to add any new traits to a global list
so they can be easily read in View Variables, and was pretty shocked to
find out many other people didn't know it was a thing. Let's make it a
thing by testing it using a new CI Python Linter to check this. But oh
no-


![image](https://github.com/tgstation/tgstation/assets/34697715/c093f1a8-00ce-40a6-8e1d-f344107ce7b8)

There were about 200+ missing traits. Alright, so let's do the
following:

* Move trait defines to their own dedicated folder in the `_DEFINES`
folder.
* Split up the traits mega-file into different files, for better
organization. One for the macros, one for the sources, and a few for the
"trait declarations"
* Run the linter a load of times and add everything to the globalvars
file, removing anything that's no longer used and figuring out where the
best categorization of it is. also minor code improvements. also rename
all of the ones that look weird. also fix list indentations
* Also alphabetize the lists because it's easy
* Move everything to a new `traits_by_type` list, while keeping the
admin one the way it is for the time being while we figure out a better
way to show that list to admins.
* Profit
## Why It's Good For The Game

Mapping trait injectors will now work for any type of trait. You
shouldn't add any trait via this injector though, but you're no longer
limited to coders remembering to add it to that critical list you
needed.

Lays the framework for a better view variables experience. This work is
too lengthy to presently do, but hopefully we can get this done sooner
rather than later. we will need a code-accessible way to view these
traits for such a framework to be implemented, so let's just do that.

Future steps are to break down the mega-declarations file into a folder
full of separate files by typepath, but that requires a lot of auditing.
Does need to happen one day though, there's a lot of mob traits mingled
with datum traits and auuugh we gotta do this later this PR is already
massive.

there's probably ways to game this but this catches _my_ mistakes so
good luck to everyone else (it should work for 99% of everyone)
## Changelog

Nothing applicable to players. However, to mappers, the mapping trait
injector should always be able to add any kind of trait (which is rather
good for the times when you need it).

---
## [wesoda25/tgstation](https://github.com/wesoda25/tgstation)@[eb246c21f6...](https://github.com/wesoda25/tgstation/commit/eb246c21f6eb5380dc56e5779fcd51d11437557c)
#### Sunday 2023-11-26 03:30:19 by san7890

Fixes sending stuff to "Old" Chat (#79819)

## About The Pull Request

This functionality was removed in #79479
(e1c6cfdce89c7dbcd507d0c44803f5407a042a96), and we should still be
supporting the old chat anyways because it contains a plethora of useful
BYOND information that we still can really leverage (such as the
built-in profiler and stuff like that) and it's going to be painful to
do that if you have to keep spamming `fix-chat` to see OOC/ASAY while
alternating every damn time.
## Why It's Good For The Game

It's ugly but we still need it. There's a reason why we still have it.
## Changelog
:cl:
fix: "Old Chat" (AKA: The old-styled non-TGUI raw-HTMLesque chat that
you might see when it prods you with the "Failed to load fancy chat!"
issue) should now get all text messages as expected.
/:cl:

---
## [HAOlleik/cpp-game](https://github.com/HAOlleik/cpp-game)@[31ef275b1a...](https://github.com/HAOlleik/cpp-game/commit/31ef275b1abf8bc2f8aa7737fd3b17ff528e2805)
#### Sunday 2023-11-26 04:06:34 by Hussein Olleik

Fuck you and your not working logic, trying to test logic

---
## [Sonic121x/Skyrat-tg](https://github.com/Sonic121x/Skyrat-tg)@[b574839498...](https://github.com/Sonic121x/Skyrat-tg/commit/b574839498f606f6279aa0ad4ec312ffd447e637)
#### Sunday 2023-11-26 04:19:04 by SkyratBot

[MIRROR] fix stupid "this forces us to do things the """right""" way" bullshit from python 3.11 [MDB IGNORE] (#25074)

* fix stupid "this forces us to do things the """right""" way" bullshit from python 3.11 (#79783)

This is likely not the best way to go about this, but i do not want us
to capitulate to python3's nanny state, suffocating levels of propriety
bullshit.

venv sucks and i fucking hate it.

* fix stupid "this forces us to do things the """right""" way" bullshit from python 3.11

---------

Co-authored-by: Kyle Spier-Swenson <kyleshome@gmail.com>

---
## [BlueSkyDefender/Depth3D](https://github.com/BlueSkyDefender/Depth3D)@[8f5b8af1a0...](https://github.com/BlueSkyDefender/Depth3D/commit/8f5b8af1a07fe94071ff0fd5179c12240ab0476b)
#### Sunday 2023-11-26 04:22:45 by BlueSkyDefender

Update 3.9.9

Re Worked How weapon Hands are handled when using secondary options.

 Weapon ZPD was set to a constant internal Value of 0.030 Since it was not used anyways. This old value just fell out of use.

It was Replaced with Weapon Near much more useful in modern games.

Near Plane Based Range Boost now goes up to 4x.

FPS Focus was reworked now you can control Weapon and World options separately and it goes up 8 steps.

Internal code changes
Simple Menu Masking now can be made more stick.

Weapon Distance From Bottom control was added.

Overwatch

Added Options to control all new options.

Overwatch Profiles

+FATAL Frame Mask oft he Lunar
+FATAL Frame Maiden of the Black Water

Profiles Updated
+Half-Life 2
+Tiny Tina's Wonderlands
+Wolfenstein: The New Order
+Wolfenstein: The Old Blood
+Resident Evil 7
+Gold Source AKA Half-Life games
+Sinned

---
## [fhgwright/git](https://github.com/fhgwright/git)@[8f23432b38...](https://github.com/fhgwright/git/commit/8f23432b38d9b122be8179295a56688391dc8ad6)
#### Sunday 2023-11-26 04:40:10 by Johannes Schindelin

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
Signed-off-by: Pratyush Yadav <me@yadavpratyush.com>

---
## [universal5433/android_kernel_samsung_universal5433](https://github.com/universal5433/android_kernel_samsung_universal5433)@[5d0c1299af...](https://github.com/universal5433/android_kernel_samsung_universal5433/commit/5d0c1299af08a668893bf78b6e67af33768e9f51)
#### Sunday 2023-11-26 05:04:07 by Daniel Borkmann

net: sctp: fix ipv6 ipsec encryption bug in sctp_v6_xmit

[ Upstream commit 95ee62083cb6453e056562d91f597552021e6ae7 ]

Alan Chester reported an issue with IPv6 on SCTP that IPsec traffic is not
being encrypted, whereas on IPv4 it is. Setting up an AH + ESP transport
does not seem to have the desired effect:

SCTP + IPv4:

  22:14:20.809645 IP (tos 0x2,ECT(0), ttl 64, id 0, offset 0, flags [DF], proto AH (51), length 116)
    192.168.0.2 > 192.168.0.5: AH(spi=0x00000042,sumlen=16,seq=0x1): ESP(spi=0x00000044,seq=0x1), length 72
  22:14:20.813270 IP (tos 0x2,ECT(0), ttl 64, id 0, offset 0, flags [DF], proto AH (51), length 340)
    192.168.0.5 > 192.168.0.2: AH(spi=0x00000043,sumlen=16,seq=0x1):

SCTP + IPv6:

  22:31:19.215029 IP6 (class 0x02, hlim 64, next-header SCTP (132) payload length: 364)
    fe80::222:15ff:fe87:7fc.3333 > fe80::92e6:baff:fe0d:5a54.36767: sctp
    1) [INIT ACK] [init tag: 747759530] [rwnd: 62464] [OS: 10] [MIS: 10]

Moreover, Alan says:

  This problem was seen with both Racoon and Racoon2. Other people have seen
  this with OpenSwan. When IPsec is configured to encrypt all upper layer
  protocols the SCTP connection does not initialize. After using Wireshark to
  follow packets, this is because the SCTP packet leaves Box A unencrypted and
  Box B believes all upper layer protocols are to be encrypted so it drops
  this packet, causing the SCTP connection to fail to initialize. When IPsec
  is configured to encrypt just SCTP, the SCTP packets are observed unencrypted.

In fact, using `socat sctp6-listen:3333 -` on one end and transferring "plaintext"
string on the other end, results in cleartext on the wire where SCTP eventually
does not report any errors, thus in the latter case that Alan reports, the
non-paranoid user might think he's communicating over an encrypted transport on
SCTP although he's not (tcpdump ... -X):

  ...
  0x0030: 5d70 8e1a 0003 001a 177d eb6c 0000 0000  ]p.......}.l....
  0x0040: 0000 0000 706c 6169 6e74 6578 740a 0000  ....plaintext...

Only in /proc/net/xfrm_stat we can see XfrmInTmplMismatch increasing on the
receiver side. Initial follow-up analysis from Alan's bug report was done by
Alexey Dobriyan. Also thanks to Vlad Yasevich for feedback on this.

SCTP has its own implementation of sctp_v6_xmit() not calling inet6_csk_xmit().
This has the implication that it probably never really got updated along with
changes in inet6_csk_xmit() and therefore does not seem to invoke xfrm handlers.

SCTP's IPv4 xmit however, properly calls ip_queue_xmit() to do the work. Since
a call to inet6_csk_xmit() would solve this problem, but result in unecessary
route lookups, let us just use the cached flowi6 instead that we got through
sctp_v6_get_dst(). Since all SCTP packets are being sent through sctp_packet_transmit(),
we do the route lookup / flow caching in sctp_transport_route(), hold it in
tp->dst and skb_dst_set() right after that. If we would alter fl6->daddr in
sctp_v6_xmit() to np->opt->srcrt, we possibly could run into the same effect
of not having xfrm layer pick it up, hence, use fl6_update_dst() in sctp_v6_get_dst()
instead to get the correct source routed dst entry, which we assign to the skb.

Also source address routing example from 625034113 ("sctp: fix sctp to work with
ipv6 source address routing") still works with this patch! Nevertheless, in RFC5095
it is actually 'recommended' to not use that anyway due to traffic amplification [1].
So it seems we're not supposed to do that anyway in sctp_v6_xmit(). Moreover, if
we overwrite the flow destination here, the lower IPv6 layer will be unable to
put the correct destination address into IP header, as routing header is added in
ipv6_push_nfrag_opts() but then probably with wrong final destination. Things aside,
result of this patch is that we do not have any XfrmInTmplMismatch increase plus on
the wire with this patch it now looks like:

SCTP + IPv6:

  08:17:47.074080 IP6 2620:52:0:102f:7a2b:cbff:fe27:1b0a > 2620:52:0:102f:213:72ff:fe32:7eba:
    AH(spi=0x00005fb4,seq=0x1): ESP(spi=0x00005fb5,seq=0x1), length 72
  08:17:47.074264 IP6 2620:52:0:102f:213:72ff:fe32:7eba > 2620:52:0:102f:7a2b:cbff:fe27:1b0a:
    AH(spi=0x00003d54,seq=0x1): ESP(spi=0x00003d55,seq=0x1), length 296

This fixes Kernel Bugzilla 24412. This security issue seems to be present since
2.6.18 kernels. Lets just hope some big passive adversary in the wild didn't have
its fun with that. lksctp-tools IPv6 regression test suite passes as well with
this patch.

 [1] http://www.secdev.org/conf/IPv6_RH_security-csw07.pdf

Reported-by: Alan Chester <alan.chester@tekelec.com>
Reported-by: Alexey Dobriyan <adobriyan@gmail.com>
Signed-off-by: Daniel Borkmann <dborkman@redhat.com>
Cc: Steffen Klassert <steffen.klassert@secunet.com>
Cc: Hannes Frederic Sowa <hannes@stressinduktion.org>
Acked-by: Vlad Yasevich <vyasevich@gmail.com>
Signed-off-by: David S. Miller <davem@davemloft.net>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [LASA-Game-Development-Club/NamePending](https://github.com/LASA-Game-Development-Club/NamePending)@[b939018887...](https://github.com/LASA-Game-Development-Club/NamePending/commit/b939018887e0a2e7c32384e0a564e40e7e0ce43c)
#### Sunday 2023-11-26 05:30:13 by CMDRZero

The God Help Me Patch

Moved local version to 2020.3.14f1 to fix bug. Played around with sample scene and my gosh, missiles are a pain to avoid. Have fun, took me about 20 minutes to beat this sample scene.

---
## [LeeroysHub/RM-Flipper](https://github.com/LeeroysHub/RM-Flipper)@[7a86b0ddcf...](https://github.com/LeeroysHub/RM-Flipper/commit/7a86b0ddcf917f63e1c1739f818225c1373421cd)
#### Sunday 2023-11-26 05:54:44 by Leeroy

Rollback Keyloq to 5 months ago! Bloody regressions making my daily life shit!

---
## [sqnztb/Skyrat-tg](https://github.com/sqnztb/Skyrat-tg)@[bf869a0ded...](https://github.com/sqnztb/Skyrat-tg/commit/bf869a0ded3a3ca5e00500ef5ad856bcb7f012dd)
#### Sunday 2023-11-26 06:14:40 by Bloop

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
## [f13babylon/f13babylon](https://github.com/f13babylon/f13babylon)@[ccb9ce38a7...](https://github.com/f13babylon/f13babylon/commit/ccb9ce38a7e26763f93c089bd0a65c9e35b70243)
#### Sunday 2023-11-26 07:14:25 by panzerr1944

no mans land; kebob changes (#166)

## About The Pull Request

![image](https://github.com/f13babylon/f13babylon/assets/76122712/cb2a0acd-9aa7-4a0c-bc3a-651c2b0104d4)
Kebab now has renegades. And it's loot increased / fixed.


https://github.com/f13babylon/f13babylon/assets/76122712/22a30f2e-354c-4988-8ac7-e39e9fce9c51

## Why It's Good For The Game
NML's town is no longer free loot. Rather, an optional bunker that the
other factions might jump you at. Kind of like normal bunkers in that
way, except with current NML rules you aren't going to lose your
everything. Just your life until someone revives you. I like the no gear
looting in NML rule, it's kinda funny.

## Pre-Merge Checklist
- [ Y ] You tested this on a local server.
- [ Y ] This code did not runtime during testing.
- [ Y ] You documented all of your changes.

## Changelog
ADDED MOBS:
1x pa claw
6x r. docs
3x r. snipers
2x r. meisters
4x r. defenders
6x r. soldiers
10x r. grunts
9x r. prospects
2x r. engies
3x r. guardians
(Total: 46)
REMOVED MOBS:
4x Legendary Ghouls
6x Legendary Mutants
2x Legendary Deathclaws
(Total: 12)
ADDED/EDITED LOOT:
2x Superhigh Ballistic Spawners
1x Mid-High E-Weapon Spawner
1x Mid-High Ballistic Weapon Spawner
1x Mid E-Weapon Spawner
1x Mid Ballistic Spawner
1x NVG Spawner
1x Gauss Rifle Spawner
1x Deluxe Stock Parts Spawner
1x (x10) Strange Seeds Spawner
1x Unique Weapon Spawner
1x High Ballistic Print
1x VHigh Ballistic Print
1x DC Medicine Journal
1x Chemistry Book
1x Random Armor Spawner
1x T4 Armor Spawner
1x Bowl of Fruit
CHANGED TERRAIN / WALLS / MISC:
Sandbags on the main road
Sandbags at the farm and graveyard
Indestructible Walls for south-side to prevent cheese
Replaced see-through airlock with high-sec one in clinic for d-claw
-
Everything else is unedited from current Kebab to my knowledge.

---
## [PikachuPenial/Titanmod](https://github.com/PikachuPenial/Titanmod)@[f654068b0a...](https://github.com/PikachuPenial/Titanmod/commit/f654068b0a02a0fbf39d258dfacb2068521366ed)
#### Sunday 2023-11-26 08:18:10 by Penial

Now properly replication server ConVars

holy FUCK im stupid why did i not realize this sooner

---
## [jetskeeter1/App-dev](https://github.com/jetskeeter1/App-dev)@[9a47d1b8f0...](https://github.com/jetskeeter1/App-dev/commit/9a47d1b8f0f2fa426806077b1bdc6af35083c427)
#### Sunday 2023-11-26 08:19:43 by jetskeeter

Favorite series

Sousou no Freirein

A fantasy show where it shows the perspective of an elf and she takes care of a girl named fran and a boy named stark. A group of awkward adventures going on to find heaven and collecting weird magic book. It has a very amazing animation and battle. It is a very successful anime that is still on going.

---
## [Nakosume/EA-Tetris_Data](https://github.com/Nakosume/EA-Tetris_Data)@[e4a780c3e0...](https://github.com/Nakosume/EA-Tetris_Data/commit/e4a780c3e0bd2c966c15517fdc5334cd9d781690)
#### Sunday 2023-11-26 08:40:55 by Sebastian Romero

back to english again.

Fuck you, Eddi.
Seriously...

---
## [NoTerrainTires/space](https://github.com/NoTerrainTires/space)@[ef52047274...](https://github.com/NoTerrainTires/space/commit/ef520472740e57f253545c24c7526e45e47b5ec2)
#### Sunday 2023-11-26 08:55:52 by necromanceranne

[READY] The Tackleling: Unarmed bonuses and features contribute to tackle success and failure, significant outcome overhaul, among other things (#79721)

## About The Pull Request

### Tackling Outcomes

Tackling now determines success based on outcome categories. These are
derived from the typical attacker/defender roll that would have
previously determined the outcome on its own. A negative roll results in
a negative outcome, a positive roll a positive outcome, and a result of
exactly 0 resulting in a neutral outcome.

The result of your roll are then passed along to the relevant proc to
determine severity. The derived roll is multiplied by 10 (or -10 for the
negative roll to get a positive value to roll with). Then we see if our
final roll fits a severity bracket. Negative outcomes will roll to
determine their outcome, and potentially could roll a less severe
outcome than what our first roll would suggest.

For positive outcomes, the defender's melee armor reduces the severity
of the outcome.
For negative outcomes, the attacker's melee armor improves the potential
outcome and at least prevents more severe backlash. It'll still be
negative, you can't move from a negative outcome to a positive outcome
just from good armor.

Most of the outcomes are fairly similar to the current outcomes, but
with the inclusion of staggering one or both parties to make the
subsequent potential grabs _stickier_, if that makes sense.

Neutral is now a mutual stagger, but also the tackler being left
upright. It's effectively net zero.

### Blocking

Blocking is checked on impact, and results in a neutral outcome if the
defender successfully blocks. This means our tackler isn't too severely
impacted from an unsuccessful tackle

### Additional Changes

Your arms ``unarmed_effectiveness`` now contributes to the attack mod
and defense mod of tackles. For humans tackling humans, this often
results in a net neutral result. But if you have a better arm, or the
tackle target has worse arms, this can alter the outcome significantly.

Any tackler with the trait TRAIT_NOGUNS (like bezerkers, Sleeping Carp
users or the very unlikely chance ninjas are tackling while wearing
their armor) gains a bonus to their tackles.

Any suit that prevents shove knockdowns grants an attack bonus, and not
just riot armor. This now includes Mk.1 Swat suits, the ones from the
SWAT crate in cargo.

Settlers are vulnerable to tackles, much like their dwarf cousins.
They're also just as bad at tackles.

Security lockers come with gripper gloves, and the sec vendor has 5 sets
of gripper gloves as standard items. They also have a +1 skill bonus.
This should encourage people to use tackling a bit more without having
to always seek out the best gear to accomplish the task. (particularly
since security is inherently pretty good at tackling with the outcome
changes).

The HoS gets a pair of gorilla gloves in his garment bag. If he wants
them.

The shove slowdown is now a new status effect, Staggered. This is just
better functionality overall. Any instance of adding the shove slowdown
now makes our target staggered.

## Why It's Good For The Game

Tackling is a bit outdated, to say the least. Not much content has been
added for a while that isn't strictly meme content. With these changes,
tackling should be slightly more nuanced, considering elements such as
unarmed effectiveness, the presence of martial arts, and actually
properly checking block rather than notionally checking block. There is
also more opportunity to protect yourself from tackle outcomes, both
positive and negative.

It also should be a little fairer to be on the receiving end of tackles
if you have taken the time to layer up defenses against it. Attackers
often overwhelmed defenders due to numbers favoring attackers more than
defenders.

Closes some really outdated design that was resulting in some really
bizarre behaviour with regards to layered defenses against attack not
having the same meaning against tackles, if only because it was looking
for the wrong things and not even the correct parts of what it was
looking for. Namely, blocking and shielding.

The inclusion of more gripper gloves and a good outcome from using them
will hopefully incentivize people to consider tacking as a useful tool,
if a bit risky still due to the splat mechanics.

## Changelog
:cl:
balance: Judo Joe, archnemesis of Maint Khan, has begun re-airing his
midnight infomercials shilling his extremely expensive Tackle Supreme
Judo Karate Training video tapes. Unable to pass up a 'bargain',
Nanotrasen has purchased these tapes en masse. Tackling techniques have
started to improve, as well as Nanotrasen's tackling instructional
algorithms within tackle gloves.
balance: The outcomes for tackling are more equalized. It isn't as feast
or famine, and should be somewhat more controllable without becoming too
severe.
add: Blocking successfully against a tackle will force the tackle to be
a neutral outcome.
add: Unarmed effectiveness from arms now contributes to attacking with
and defending from tackles.
add: Those who refuse to use firearms (like Sleeping Carp users and
insane unholy berzerkers) are better at tackling others.
add: Riot specialized armor, and not just riot armor, now contributes
meaningfully to tackling effectiveness.
balance: MK.1 Swat Suits, the ones that come in SWAT crates, now
functions similarly to riot armor.
add: Settlers from the outer rims have noticed they aren't very good at
protecting themselves against Judo Joe's clearly discriminatory tackling
techniques.
add: Security lockers come with gripper gloves, security vendors now
sell them as standard items, and the HoS' garment bag now has a pair of
gorilla gloves. Gripper gloves have a positive skill bonus to tackling.
add: Being insane also makes you INSANELY good at tackling but also
INSANELY likely to eat shit on a whiff. DO OR DIE, BITCH.
refactor: Shoving slowdown and all its implementations now use a status
effect, Staggered.
/:cl:

---
## [cam900/mame](https://github.com/cam900/mame)@[96ab505d66...](https://github.com/cam900/mame/commit/96ab505d665a886809e8109a55d5e13fb7e520aa)
#### Sunday 2023-11-26 10:14:58 by ArcadeShadow

ibm5170_cdrom.xml: Added 21 items (18 working). (#11760)

New working software list additions (ibm5170_cdrom.xml)
--------------------------------------------
5 Plus One: Pack 12 - Ghostbusters II [redump.org]
Brutal: Paws of Fury (Europe) [redump.org]
Darkseed (Germany, Action Sixteen release) [redump.org]
Dune (Europe, White Label release) [redump.org]
Dune II - Battle for Arrakis (Netherlands) [redump.org]
Dune II - Battle for Arrakis (Germany, PC Games Collection 2 release) [redump.org]
Dune II - The Building of a Dynasty (USA, Gold Medal 12 CD Pack) [redump.org]
Fables & Fiends - Book Three: Malcolm's Revenge (Europe, Japan) [redump.org]
Fables & Fiends - Book Two: The Hand of Fate (UK, Sold Out release) [redump.org]
Jurassic Park (Europe) [redump.org]
Jurassic Park (Germany) [redump.org]
Jurassic Park (USA) [redump.org]
Star Control [redump.org]
Stellar 7 (USA) [redump.org]
Stellar 7 (USA, alt) [redump.org]
The Cool Croc Twins + Magic Boy (Europe, 2 Game Pack release) [redump.org]
The Cool Croc Twins + Magic Boy (Netherlands) [redump.org]
The Dig (Japan) [redump.org]

New NOT working software list additions (ibm5170_cdrom.xml)
--------------------------------------------
Darkseed (USA) [redump.org]
Darkseed (USA, alt) [redump.org]
Dogfight: 80 Years of Aerial Warfare (Europe) [redump.org]

---
## [Ben10Omintrix/tgstation](https://github.com/Ben10Omintrix/tgstation)@[492ed90f28...](https://github.com/Ben10Omintrix/tgstation/commit/492ed90f28dfd213e9438509653727f788efcebd)
#### Sunday 2023-11-26 10:44:47 by necromanceranne

Fixes body collision causing a stun, despite a successful block. (#79824)

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

---
## [aniketzod/Data-Science-Assignment-No.1-Basic-Statics-Level-1-](https://github.com/aniketzod/Data-Science-Assignment-No.1-Basic-Statics-Level-1-)@[1e21e493e7...](https://github.com/aniketzod/Data-Science-Assignment-No.1-Basic-Statics-Level-1-/commit/1e21e493e736e39f4fb675838b3ead0666345698)
#### Sunday 2023-11-26 10:54:19 by Aniket Zod

Update README.md

Data-Science-Assignment-No.1-Basic-Statics-Level-1
Q1) Identify the Data type for the Following:
Activity	Data Type
Number of beatings from Wife	
Results of rolling a dice	
Weight of a person	
Weight of Gold	
Distance between two places	
Length of a leaf	
Dog's weight	
Blue Color	
Number of kids	
Number of tickets in Indian railways	
Number of times married	
Gender (Male or Female)	


Q2) Identify the Data types, which were among the following
Nominal, Ordinal, Interval, Ratio.
Data	Data Type
Gender	
High School Class Ranking	
Celsius Temperature	
Weight	
Hair Color	
Socioeconomic Status	
Fahrenheit Temperature	
Height	
Type of living accommodation	
Level of Agreement	
IQ(Intelligence Scale)	
Sales Figures	
Blood Group	
Time Of Day	
Time on a Clock with Hands	
Number of Children	
Religious Preference	
Barometer Pressure	
SAT Scores	
Years of Education	


Q3) Three Coins are tossed, find the probability that two heads and one tail are obtained?

Q4)  Two Dice are rolled, find the probability that sum is
a)	Equal to 1
b)	Less than or equal to 4
c)	Sum is divisible by 2 and  3


Q5)  A bag contains 2 red, 3 green and 2 blue balls. Two balls are drawn at random. What is the probability that none of the balls drawn is blue?


Q6) Calculate the Expected number of candies for a randomly selected child 
Below are the probabilities of count of candies for children (ignoring the nature of the child-Generalized view)
CHILD	Candies count	Probability
A	1	0.015
B	4	0.20
C	3	0.65
D	5	0.005
E	6	0.01
F	2	0.120
Child A – probability of having 1 candy = 0.015.
Child B – probability of having 4 candies = 0.20

Q8) Calculate Expected Value for the problem below
a)	The weights (X) of patients at a clinic (in pounds), are
108, 110, 123, 134, 135, 145, 167, 187, 199
Assume one of the patients is chosen at random. What is the Expected Value of the Weight of that patient?

Q10) Draw inferences about the following boxplot & histogram

 Q13) What is the nature of skewness when mean, median of data are equal?
Q14) What is the nature of skewness when mean > median ?
Q15) What is the nature of skewness when median > mean?
Q16) What does positive kurtosis value indicates for a data ?
Q17) What does negative kurtosis value indicates for a data?
Q18) Answer the below questions using the below boxplot visualization.
What can we say about the distribution of the data?
What is nature of skewness of the data?
What will be the IQR of the data (approximately)? 


Q19) Comment on the below Boxplot visualizations? 
 
Draw an Inference from the distribution of data for Boxplot 1 with respect Boxplot 2.

---
## [steinareliassen/trunkfriends](https://github.com/steinareliassen/trunkfriends)@[3c9bbece7b...](https://github.com/steinareliassen/trunkfriends/commit/3c9bbece7b4f2c2e537458e45dfcbc0e853b7433)
#### Sunday 2023-11-26 11:39:06 by Steinar Eliassen

Ability to select and copy accounts out of Trunkfriends

The ability to track what connections you have lost is one thing, but it gets kinda annoying
if you need to manually write the account names you have found in Trunkfriends elsewhere
to refollow them from another account.

This commit lets you select one or more accounts, and copy them to the clipboard, so you
can paste them wherever you want.

---
## [maaacha/f13tbd](https://github.com/maaacha/f13tbd)@[a2491a3c89...](https://github.com/maaacha/f13tbd/commit/a2491a3c89e4fa54e2c112902162278493f10945)
#### Sunday 2023-11-26 11:57:31 by Mazzinsanity

Enables Podpeople as a Roundstart Species (May need to be enabled on the box) (#194)

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

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->
Makes a WEAKENED version of Podpeople selectable as a roundstart
species. Their maluses and bonuses are as follows:
- 1.25 damage modifiers for Brute/Burn
- Restore 2 hunger and heal 0.2 Brute, 0.2 Burn, 0.1 Toxin when in
light.
- Reverse effects in darkness.

Changes podpeople bloodtype to EZ Nutrient
## Why It's Good For The Game
This lets people play as anthropomorphic Broc flowers.
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
add: enabled podpeople as a roundstart species
balance: rebalanced weak podpeople healing
tweak: changed podpeople bloodtype to EZ Nutrient
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [jplukas/berry](https://github.com/jplukas/berry)@[f5b7abd7c0...](https://github.com/jplukas/berry/commit/f5b7abd7c0074bfff365f4ea5091fa4f5bf055f7)
#### Sunday 2023-11-26 12:29:59 by Maël Nison

Injects the PnP runtime in the process before requiring the user config (#5954)

**What's the problem this PR addresses?**

We added support for JS constraints thanks to the `yarn.config.cjs`
file. However this file is currently executed from within the Yarn
process, so it doesn't have access to the dependencies when operating
under the PnP installation mode.

Fixes #5878

**How did you fix it?**

I'm still on the fence on the right solution. This PR automatically
loads the `.pnp.cjs` file when the `loadUserConfig` file is called. An
alternative would be a post-install hook to allow each linker to inject
their runtime inside the process post-install, but that was more
involved and I figured it's worth more consideration.

Another alternative was to not do anything and expect users to setup the
PnP runtime themselves, but it feels something that Yarn should be able
to handle.

A third alternative would be to evaluate this file within a worker
thread, which would be started with the proper `execArgv` flags. It's
less intrusive than the post-install hook so I kinda like this idea, but
again - worth more consideration.

I'm working on enabling tests, and to this effect I'm checking whether
we can remove the `NODE_OPTIONS` values from the `makeTemporaryEnv`
subprocesses.

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
## [elunna/HACKEM-MUCHE](https://github.com/elunna/HACKEM-MUCHE)@[a0f3bdfd5f...](https://github.com/elunna/HACKEM-MUCHE/commit/a0f3bdfd5f92f824be6583434e51241d0e31bc4c)
#### Sunday 2023-11-26 13:21:59 by Erik Lunna

Allow teleportation into unteleportable spots in wizard mode (from xNetHack).

This was something that really annoyed me. The wizard-mode character
should be able to do things such as teleporting directly into the
Wizard's Tower without having to go through the magic portal, or have
some way of entering solid rock without turning into a xorn.

There is now a prompt to confirm that you want to teleport somewhere you
couldn't normally. If you refuse you'll still get "Sorry..." like
normal; otherwise there's no restriction and you'll teleport there.

Note that you can teleport on top of monsters in wizard mode with this
now, because this doesn't cause any bugs, it just displaces the monster
to the closest available square.

---
## [Ephemeralis/tgstation](https://github.com/Ephemeralis/tgstation)@[bed92e193c...](https://github.com/Ephemeralis/tgstation/commit/bed92e193ce4a79824fd4fd30a900245dca870ae)
#### Sunday 2023-11-26 13:32:55 by san7890

Further Prevention of Disposals Qdeletion (#79714)

## About The Pull Request

Fixes the consequences of #79629 - Verdict is still out on what the root
issue is

This has been an issue for the last two years and everything I go
bananas trying to get a consistent reproduction case to figure out the
root issue. After three session of picking, I think it's just a
consequence of certain thing in disposals code sleeping due to
`addtimer()` and whatnot so I'm just throwing in the towel and just
making it so we stop sending atoms to nullspace for no reason.

`target_turf` is typically always a present arg, but regardless we are
guaranteed to get a valid turf to send people to instead of the deleted
mob room. We still `stack_trace()` whenever this happens, so tracking
this issue doesn't change any more than the present status quo- we just
don't keep torturing mobs by sending them to the shadow realm.
## Why It's Good For The Game

One day we'll figure out why we keep getting `null` passed into
`forceMove()` like this but today is not that day. i know turfs
technically can't be deleted but it's just there as a safety since we
nullcheck anyways (which is the whole point of this fix). Let's just
stop screwing with players for the time being

also the code looks much better
## Changelog
:cl:
fix: Safeties in the code have been added to prevent things in disposals
going into nullspace whenever they get ejected from a pipe - you will
just magically spawn at the turf that you were meant to be flung
towards.
/:cl:

---
## [Cambalisa236095/app-dev](https://github.com/Cambalisa236095/app-dev)@[fbdf3e6e4f...](https://github.com/Cambalisa236095/app-dev/commit/fbdf3e6e4f954dff5844b69671530a1620a236ce)
#### Sunday 2023-11-26 14:05:59 by Cambalisa236095

Update README.md

A young man named Thorfinn finds himself in a quest for revenge against his father's killer. Firstly indulged in the aparent greatness of war and honor, Thorfinn quickly changes as he endures having to survive alone and then alongside the man he vows to kill, developing conflicting emotions towards the causality of his past and present life.

---
## [tusharsnx/terminal](https://github.com/tusharsnx/terminal)@[86fb9b4478...](https://github.com/tusharsnx/terminal/commit/86fb9b44787accd09c5943a506e27eb4c8e573c0)
#### Sunday 2023-11-26 14:08:02 by Dustin L. Howett

Add a magic incantation to tell the Store we support Server (#16306)

I find it somewhat silly that (1) this isn't documented anywhere and (2)
installing the "desktop experience" packages for Server doesn't
automatically add support for the `Windows.Desktop` platform...

Oh well.

I'm going to roll this one out via Preview first, because if the store
blows up on it I would rather it not be during Stable roll-out.

---
## [ReturnToZender/ReturnsBubber](https://github.com/ReturnToZender/ReturnsBubber)@[52f69b96ee...](https://github.com/ReturnToZender/ReturnsBubber/commit/52f69b96eebfbe14a763ae9c5a8dd7ef156c4582)
#### Sunday 2023-11-26 14:11:04 by The-Sun-In-Splendour

mid-round salt pr about EMP mold because being repeatedly shocked 500 times in a row unless you get charcoal (now called syniver or whatever fuck new chems) is not what I consider to be fun gameplay (#755)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
emp mold mosquitoes no longer put you in shock stunlock hell because
that shit is not funny
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Please make sure to actually test your PRs. If you have not tested
your PR mention it. -->

## Why It's Good For The Game
it made me mad and this is a salt pr

![image](https://github.com/Bubberstation/Bubberstation/assets/70348069/b5002caa-d401-478a-9d48-fbc772c05b3e)

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
balance: emp mold mosquitoes no longer shock you all the time until you
have a stroke irl over the annoyance
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
## [DogeDogIs/Paradise](https://github.com/DogeDogIs/Paradise)@[6a109ade7f...](https://github.com/DogeDogIs/Paradise/commit/6a109ade7f7cd612dcd371f64c4485340ab963d9)
#### Sunday 2023-11-26 14:58:03 by Henri215

Moves a few sprites out of items.dmi (#23301)

* fuck you items.dmi

* banhammer

---
## [khoih-prog/pytorch](https://github.com/khoih-prog/pytorch)@[3afb4e5cf7...](https://github.com/khoih-prog/pytorch/commit/3afb4e5cf7b0162c532449fb5c9e7c7058a4c803)
#### Sunday 2023-11-26 15:08:56 by Brian Hirsh

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

---
## [LC4492/CM-Space-Station-13](https://github.com/LC4492/CM-Space-Station-13)@[15086ae683...](https://github.com/LC4492/CM-Space-Station-13/commit/15086ae683f727d9a990e05f8ce9a08e43731207)
#### Sunday 2023-11-26 15:10:33 by fira

Allow playing uploaded sounds through the music player w/ Webroot (#4934)

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

Too long have we suffered at the hands of admin auditive abuse. 

The prophet, spookydonut, once said, "You shouldn't be using this lol".
And he was right. Using "Play MIDI sound" both reduces usability for our
users, and can cause performance issues by freezing up the game for a
while as the data is transfered to these 200 poor CM addicts.

So we sought to alienate it with "Play Internet Sound" backed by
youtube-dl. Unfortunately, some things are subject to geo blocking or
simply not available on Youtube. Thus the regime of terror of Admins
continues.

This PR brings us one step closer to our goal: it allows to use the now
renamed "Play Admin Sound" to (also) upload a sound file to Webroot and
have it played through CDN. It also works with simple transport but that
mostly defeats the point.

Also reduced default volume for new players from 50% to 20%... Don't
worry, It's still way more than enough to get them to quit the server, i
have mine at 2-10% max

# Explain why it's good for the game
* Less new player abuse by reducing default volume
 * More performance by allowing big or custom songs to be backed by CDN
* Better UX: People can easily see the song name and more easily stop it
* Admins can now hide the name of played songs if they want to. Don't
ask me why.

# Testing Photographs and Procedure

![image](https://github.com/cmss13-devs/cmss13/assets/604624/4f00c45d-76ca-47e2-860a-2f26d55de2a4)
You'll have to believe me on the sound working

# Changelog
:cl:
balance: Default Web Music Player volume is now 20% down from 50%. It
was found too effective against new players.
admin: "Play Internet Sound" is now "Play Admin Sound" and optionally
allow to hide the track name.
admin: "Play Admin Sound" can now be used with uploaded tracks, which
use CDN delivery and the in-chat music player, granting players more
control over them.
admin: Removed "Play Midi Sound". 
/:cl:

---
## [andras204/Hungrush](https://github.com/andras204/Hungrush)@[24a59ee5dc...](https://github.com/andras204/Hungrush/commit/24a59ee5dc9444ee4c9df7cf2c8c8dba501591ab)
#### Sunday 2023-11-26 15:37:18 by Alaa

Finally did something

Added:
+Added isRestaurantOpen to RestaurantService.
+Added throws exception to DishController.
+Added Autowired annotation for entityManager to fix error in RestaurantController.
+Added @GetMapping and @Transactional annotations for isRestaurantOpen in RestaurantController.

+Added getCourierStatus procedure
+Added getIdleCouriers stored procedure

Changed:
~Date type to java.sql.time type for opening_time and closing_time

~Changed Courier Status to Enum type.
~Changed daysOpen field to Enum type.

Removed:
-@Temporal annotations to turn Date to Time.
-Andras' really fucking funny comments because I don't want the professor to accidentally read them when we submit (forgive me).

My next steps:
= Make a method listRestaurantCategory in Java for the SQL procedure.
= Finish methods getIdleCouriers and getCourierStatus in Java.
= Try to fit daysOpen in isRestaurantOpen (Considering just omitting this for simplicity's sake, what do you think?).
= Review all CRUD operations.
= Find another method to replace the locateCourier Location (I'm thinking just calculating the bill, not sure if anyone else is doing this).

---
## [i574n/The-Spiral-Language](https://github.com/i574n/The-Spiral-Language)@[7ece1d2d26...](https://github.com/i574n/The-Spiral-Language/commit/7ece1d2d268aa60882326be007353062a94801e4)
#### Sunday 2023-11-26 15:39:08 by mrakgr

"10:00 AM. https://youtu.be/DLjWM4-zQ5w?list=PL8JmJYDyXnXlrwJPh3ve11lxhNBXQGw64&t=1

I'll stop by watching Witch's Weapon here. My hand doesn't feel a bit better than yesterday, but I know not to trust it. If I start programming right now, it will all go to hell again.

I will move according to plan. An issue on the cursorless repo and ask whether there is a way to fine tune my voice. But I expect it will be difficult so. I almost likely just move to writing Heart's Desire for the next month or two until my hand recovers enough to program. So far there has been an update for the packaging in transit. The keyboard has moved to another facility.

I want for it to come here as soon as possible, but I need to look at it realistically, even if it got here to day, I still wouldn't be in good enough condition to make use of it. So it doesn't really matter whether it arrives next week or in two.

My main priority should be just to relax for the next month or so.

Now let me try out cursor less.

10:10 AM. It seems that today. saying cursorless cheat sheet and cursorless reference does in fact open the correct web page.

I have no idea why this didn't work for me last time.

I mean on one hand, it cannot possibly be the case that my diction improved so much in just a single day. But on another it also can't be the case that the program itself improved since I didn't update it.

Anyway, it doesn't seem like I'll need to open that issue that I can plant yesterday.

https://youtu.be/8SkdfdXWYaI
Using python to code by voice.

Let me match these videos, and then I will start writing. I honestly don't feel like me. I am messing with this **** even too. I got the cheat sheet to work somehow.

https://youtu.be/8SkdfdXWYaI?t=1378
> It works, the best for Lisps.

Yeah, this is one of the things that I've been afraid of. The Lisp is the language that I h'd most expect to be good for this kind of thing.

https://youtu.be/YKuRkGkf5HU?t=78
> Repetitive strain injury.

It seems this entire voice programming industry exists just because of RSI.

https://youtu.be/YKuRkGkf5HU?t=104
> So this is like a majority of the room.

Who have experienced RSI.

https://youtu.be/YKuRkGkf5HU?t=1144

Even without cursorless, Talon could be used to great effect for programming.

https://youtu.be/YKuRkGkf5HU?t=1459

The advice to dedicate some learning time to this is pretty good right now. Right now I don't really feel like it.

https://youtu.be/YKuRkGkf5HU?t=1680
> Whispering is more of a strain on your voice than talking in a normal tone.

Didn't know about that.

https://youtu.be/YKuRkGkf5HU?t=1816
> Not so big challenges
> Supporting programming languages
> Building tools with Talon

I'm starting to hear Thunder outside, so I might need to scram Well, it's true that I have that UPS. It won't protect me from a direct lightning strike.

But I'll wait for a bit longer before I run. Maybe I have time to finish the video.

https://youtu.be/YKuRkGkf5HU?t=1845

Never mind I have to run.

12:55 PM. Hey, I'm back. Let's assume the videos from before. The bad weather went away as soon as it started. I shouldn't have even shut down.

1:00 PM. It seems that the keyboard is at the international airport. I am tracking it online.

It's actually pretty great that it is being transmitted on Sunday. The Chinese sure are hard workers.

Since it is at an international airport in a few days, maybe even two it should arrive in Croatia and then I'll have to wait a few days after that for it to arrive at my doorstep via mail. It's possible that it might arrive next week near the end. Maybe on Thursday or Friday.

1:45 PM. Watching these videos is making me realize that I don't actually need a cursorless, just talon.

But I am going to do is aim to go halfway, then navigation is the most annoying part of using these programs. But if I could configure them to just input code, Then maybe I could have something serviceable..

Once I get the glove 80 keyboard, I'm going to be able to use the left side to navigate using the lower layer. I also have this track wall mouse on the right hand, which is easier to use than the old mouse. So using the keyboard and the mouse just for navigation and using my voice to input code could be a viable first step towards voice programming.

Let me continue watching the videos. I want to watch the mall. I shouldn't feel obligated to start writing heart's desire.

It feels like that Perixx 524 split keyboard really **** **** my shoulders.

It is a real mistake to go with that cheap model. It could have ordered the Glove80 a month ago and I would have already had it today.

https://youtu.be/FOJ6OvPf_nM
I Had To Learn To Code By Voice | Talon Voice | Tobii Eye Tracker

Let me watch this one as well. Maybe I'll post them in the ready to tread from earlier. By Reddit, I mean the Reddit trade on the Cursorless talk that I opened yesterday.

https://youtu.be/FOJ6OvPf_nM?t=420

I'll pause this one here. I'll watch it later.

https://youtu.be/U-NZjzDj-Xk?t=224
Coding by Voice with Voice Attack: a Practical Guide for Programmers

> They are relying on the windows speech engine.

This isn't about Talon, but about another program. It's called voice attack.

https://youtu.be/U-NZjzDj-Xk?t=759
> Speech recognition voice training...

It seems this is a feature of windows. I had no idea it existed.

https://youtu.be/U-NZjzDj-Xk?t=916
It seems this program is made in C# so it can run arbitrarily program and scripts made in it.

2:45 PM. Okay, what I'm going to do next is study up Talon. I want to decide whether I want to use Telon or voice attack. Talon also has a visual studio code extension. So I want to understand what its purpose is.

https://voiceattack.com/Default.aspx

I'm really going to try this out. The reason why I'm considering this, instead of Talon, is because Talon's voice recognition engine is worse than Windows' native one. And I also figured out just recently in that video that the Windows Voice Recognition engine can be fine tuned using my own voice.

3:35 PM. https://chaosparrot.github.io/talon_practice/
https://talon.wiki/

Yesterday I was overwhelmed by this, but now I feel like I am able to absorb it more readily.

https://talon.wiki/getting_started/

There is a section on improving voice recognition accuracy.

https://gaming.tobii.com/product/eye-tracker-5/

Admit I had no idea eye trackers even existed before today. I thought that eye tracking would be done using a camera yesterday.

https://youtu.be/aFN4HajMUPI
Tobii Eye Tracker 5 Review | Simple. Intuitive. Essential?

https://talon.wiki/talon_related_resources/

OK, I the videos and eye tracking were very interesting. Let's watch some of these.

Has been a long time since I spent the entire day studying just studying and researching things. Getting Rsi led to such new experiences.

Maybe I should resume posting these journal entries in the Spiral repo Github commits? Just so you know, I'm using Windows voice typing to generate this text. I have it remapped to the caps lock key. Usually windows typing is activated by pressing the windows, and then the H key, but I had a rema to the capsule key because the default is too hard to hit.

https://youtu.be/j70UOLVO4I4
9 windows settings every user should change now!

Forget this. I don't feel like watching this right now.

https://youtu.be/y0ls3lH3rYM
OpenAI's ChatGPT Fell For This Illusion! But Why?

And this two minute paper video is interesting.

The videos for tell on a voice that I watched today very informative. I think.they gave me a bit of courage to go forward with a learning such a tool. I'll simply have to dive in and get used to it. I'll give it a try. And if I cannot get the voice recognizer to mesh with my voice, I'll try the voice attack software.

The keyboard that I ordered has arrived at an international airport, but even.if it got here, I still wouldn't be able to use it because of the state of my right hand. So it will only really be useful to its full extent once I heal from my rsi.

5:30 PM. Forget this, Talon is horrible. It finds it really easy to misinterpret what I am saying.

5:35 PM. I am installing voice attack, and it's offering me right off the bat to help train the voice recognizer engine. This is something I'm really missing with Talon.

For an application such as this, the voice recognizer engine is the most important part of it. And not having it work in top shape is really a big problem with Talon.

https://www.youtube.com/playlist?list=PLMd2J1iNJCMeUcBmOjJAMb0o-3BClzOPt

I spent some time training Windows speech recognizer engine and. Now I need to figure out how I can use voice attack in order to dictate inputs the same way I'm doing for voice typing right here.

Maybe the easiest thing to do would be to just activate the voice typing feature of windows instead of messing with the detection feature of voice attack.

https://youtu.be/U-NZjzDj-Xk
Coding by Voice with Voice Attack: a Practical Guide for Programmers

Let me take a look at how this guy configured it for a bit more. I think in one of the parts of the video he flashed the dictation commands.

Arguably, it would, it would have been better to use Talon, but it's bad at recognizing my voice.

Actually these guys channel might be worth checking out. I'm interested in what he has to say about learning to program by gaming.

https://youtu.be/U-NZjzDj-Xk?t=345

Oh, I see what he is doing here. See, he's setting the clipboard to dictation and then pasting from it, I think.

Schillo and how you doing today
Schillo and how you doing today

killed world , you doing today
killed how you doing today than

Hello World, how are you doing today?
Hill world how are you doing today?
Hill world how are you doing today?
Hello World, how are you doing today?

kill the old filly doing today
kill the old filly doing today

OK, I figured out how to use the dictation feature of a voice attack and it's very bad, much worse than Talon.

The paragraph in the middle is actually done using voice typing, not using voice attack. But for some reason, you know, when I stop down, my voice is interprets. Hello world as Hillo World. And the hello world as kill world.

I was trying to dictate `Hello World. How are you doing today?` ...For all of the previous sentences.

I'm guessing that the difference is even though they are using the same speech recognition engine because the voice typing is using some kind of correction pass after this voice has been inputted.

And guess in that case, it doesn't mean that I have to favor voice attack over Talon.

7:25 PM. It seems either way, I'm going to have to forget about using either tailon or voice attack for dictation. If I'm going to use these programs, I'm going to have to accept their weaknesses as they are. So tomorrow, my mission will be to go through the basics of Talon.

I'm just about to gotten used to its alphabet. And now I have to get used to everything else. That simple tutorial I went through should, in fact, be enough to use it effectively. I just need to put in some practice.

If I can do this, then I will be able to resume programming.

I'll cut down the amount of text I have to write drastically.

The voice software, together with the ergonomic mouse and keyboard when it arrives, will be enough to make me a lot more efficient at producing text.

Right now, I'm going to call it a day. I'm just going to relax from here for real.

I'm going to post this journal style commit for a first time in almost since the start of the year."

---
## [i574n/The-Spiral-Language](https://github.com/i574n/The-Spiral-Language)@[3fb80de9b5...](https://github.com/i574n/The-Spiral-Language/commit/3fb80de9b59cec06bfe9f69c3e200f47558faa4b)
#### Sunday 2023-11-26 15:39:08 by mrakgr

"9:15 AM. No update for my keyboard. It seems it is still in Hungary.

https://youtu.be/YWimz6rfuls
This is 99% why your aim is bad.

https://youtu.be/gNDfH7J2DNE
Fix Your Terrible Mouse Grip NATURALLY

Today, what I'm doing is trying out the claw grip, even on the track ball mouse.

I'm going to try letting my fist stay in the shape of a clove. In other words, it's a fully relaxed posture. I want to see whether that makes any difference to my rsi. One thing I noticed since I am actually using my whole arm tool move the mouse cursor. It's a lot more accurate than just using my thumb.

https://youtu.be/5S9iwYnndp8
The Optimal Contact Points For Aiming

Right now entering out the claw grip. And it's really **** amazing how much more accurate I am. Instead of using the damp, I'm rotating my wrist to move the mouse cursor. The reason why I couldn't do that before and why I've been using the pole grip for 20 years is because of that a desk. It has a very, very.very little space between the keyboard and the mouse and the top of the ceiling. By ceiling, I mean, it's kind of like a pull out desk, which has a board in the middle. Now that I'm using a regular desk, I have a lot more space above for my hand to move. I should try typing that way as well.

I have a hypothesis that my whole rsi in the right hand isn't so much because of typing, though the volume I put in certainly contributed to it. But because I've been using the palm grip on both the mouse and the keyboard.

https://youtu.be/5S9iwYnndp8?t=50
> When we grip the mouse with the tips, we gain dexterity.

I've been using the mouse for 20 years, and this is the first time discovering this.

https://youtu.be/5S9iwYnndp8?t=145
> If someone you know has a messy handwriting, have a look at their grip. You'll be surprised to know how much of one of their fingers or more are hyper extended.

https://youtu.be/qh7fqjNqCLw
Fixing X-Pro Gamer's Worst Habit (You Do This Too)

Now that I've changed my grip It feels like I am flowing with this track ball. It is so much better now.

10:45 AM. I think I figured it out. All the flaws in my technique. The reason I have an size is probably the way I hold my hands. My left hand is mostly in deflection position by all my right hand is extended. That is how I use the keyboard in general. And that is how I use the mouse.

I think once I adjust my grip, the other side should go away. So I'll need to test it for another few weeks.

Using voice dictation for most of my unstructured text input as well as an ergonomic mouse and the keyboard I'm going to get should be enough to fix it.

https://deepmind.google/discover/blog/transforming-the-future-of-music-creation/

Music generation. Now this is something I've been waiting for a long time.

https://blog.jim-nielsen.com/2023/html-web-components-an-example/

https://youtu.be/R4Ri4ft7bXY
The Good, The Bad, and The Web Components - Zach Leatherman | JSHeroes 2023

3:00 PM. https://youtu.be/C8RtH2eoBU8?list=PL8JmJYDyXnXlrwJPh3ve11lxhNBXQGw64
Witch Weapon Story [CHAPTER 8] [PART 2]

3:10 PM. Let me check on just a bit and then I'll start writing. I've been resting too much.

3:30 PM. Right now I'm not using the keyboard with my right hand too much. I mostly focusing on the left. Thinking about it objectively, I'm doing a lot of weird movements and contortions, even made by a left hand. My typing technique is pretty messed up either way. I think that it's not worth fixing. The keyboard, the regular keyboard that I have is pretty badly designed So it's just so the way I'm typing is just a consequence of that.

Once the glove ate the keyboard arrives, I'll be able to correct my typing.

And right now...

///

Package status: In transit (8 Days)
Country: China -> Croatia
2023-11-15 18:00 HU, International flight has arrived
2023-11-13 13:24 HK, International flight has departed
2023-11-12 19:32 CN, Arrived at the origin international airport
2023-11-12 09:32 Mainland China, CN, Shipment is in transit to next facility
2023-11-12 00:19 Mainland China, CN, Departed from sort facility
2023-11-10 20:50 Mainland China, CN, Arrived at origin facility
2023-11-10 16:07 Mainland China, CN, Shipment picked up
2023-11-10 14:02 Sesvete, HR, We are exchanging data internally
2023-11-07 15:53 Shipment information received
======================================
Powered by www.17track.net

///

It seems that the package is still in Hungary. It's really thinking about to leave from the airport. I thought that would have been done long ago. So far I've been waiting for it to 10 days. Once I get the keyboard, I'll do a programming session. So far my rsi has already taken six weeks from me. Maybe the keyboard will create a miracle. If not, I'll have to learn how to program using a combination of typing and voice programming.

7:25 PM. Word Count's at 8.9 K.

Unlikely the previous chapters I'm going to step up posting these as zip files. It's a waste of time. Instead, I'll just share a link to the Google Docs document.

I'll prove read it tomorrow and then post it. Tomorrow is Saturday, so I have work."

---
## [i574n/The-Spiral-Language](https://github.com/i574n/The-Spiral-Language)@[ac7b1a4bc7...](https://github.com/i574n/The-Spiral-Language/commit/ac7b1a4bc727b10ab1a4e280bdbe9b5e74e3495a)
#### Sunday 2023-11-26 15:39:08 by mrakgr

"https://arstechnica.com/gaming/2019/04/coding-without-a-keystroke-the-hands-free-creation-of-a-full-video-game/

https://xeiaso.net/blog/voice-control-talon/

sleep mode - in this mode, Talon is not listening for commands
command mode - in this mode, Talon listens for commands and executes them in the order they are spoken
dictation mode - in this mode, Talon listens for large blocks of text and types them out as you say them

It has a dictation mode? I'll have to look into that.

11/13/2023

9:05 AM.

///

2023-11-13 13:24
HK, International flight has departed

2023-11-12 19:32
CN, Arrived at the origin international airport

2023-11-12 09:32
Mainland China, CN, Shipment is in transit to next facility

2023-11-12 00:19
Mainland China, CN, Departed from sort facility

2023-11-10 20:50
Mainland China, CN, Arrived at origin facility

2023-11-10 16:07
Mainland China, CN, Shipment picked up

2023-11-10 14:02
Sesvete, HR, We are exchanging data internally

2023-11-07 15:53
Shipment information received

///

My glove 80 keyboard finally departed from the Hong Kong Airport.

I don't know what the target destination is, so I can only hope it's Croatian. If it's that, then I'll definitely get the keyboard this week.

Today, my goal will be to go through the practice exercises for Talon.

After I feel secure at that, I'm going to do a real programming session. The reciprocal isn't much to it. I have to get used to using my voice to program. And the best way to do that is to temper myself with a real assignment.

Using voice typing to do this journal is really a good exercise for talking.

I wish I knew about it earlier because I definitely would have used that had I knew how good it was.

My ring finger is a covering because it's definitely not as number as it was in the past few weeks. Even so, the recovery will take a few months.

The keyboard once it gets here won't make a difference in terms of allowing me to return to my previous fitness. Rather, it will allow me to use my left hand better. I will be able to use it for a navigation with a new keyboard.

12:05 PM. https://kbd.news/Glove80-Rethinking-split-contoured-ergonomic-keyboard-1796.html?utm_source=Klaviyo&utm_medium=flow&_kx=y-P3vN0awMgfN_5-fSYV6hn3CWnqOweQI9jK0_2a9oI%3D.V4FbQN

I got an email from MoErgo, so now I'm reading this article.

12:55 PM. Let me do the chores, and then I'll figure out how Talon configuration files work. Before I do anything with it, I need to figure out how macros can be used using Talon. I could try to make do without it, but it would be a big disadvantage to do it that way.

After that I might do some like programming, but not an actual session. I need, I need to give my right hand time to rest. If I start a program for real now, it will put a stress on it.

1:30 PM. His time to resume. I'll try making my own macro using Talon configuration files. For my first move, I'll check out the community user config files.

inl _ =:3
inl _ =:3

Ohh wow. The macro actually worked, though not correctly...

inl _ =:3

inl _ =

inl _ =
inl some_variable =
inl someVariable =

Let me pace the macro here so you can see how it is made.

///

-

inline:
    insert("inl _ = ")
    key(left:3)
    key(ctrl-d)

///

I like this. This will be useful definitely.

I just got to put the Talon file into the directory, and I didn't even need to restart the application in order for the macro to take effect.

It feels like I've met one of the goals for today.

What I should do right now is study a bit more about how the macros really work. Let me do that right now.

After I clear that goal, i'll be able to start programming using talon.

`date insert: insert(user.time_format("%Y-%m-%d"))`

I just found this in the dates Talon file. I'm going to edit it so it inserts the date using my usual format.

13/11/2023

`date insert: insert(user.time_format("%d/%m/%Y"))`

It works perfectly now.

13/11/2023

THIS WORKS!!!!

2:30 PM. No, time for a break. After that, after that, I'll do some more research on how our arguments work in talon files.

https://www.joshwcomeau.com/blog/hands-free-coding/

> Formatters can be composed. For example, I'm a fan of UPPER_SNAKE for JavaScript constants:

I didn't know they could be composed.

3:50 PM. I can't get the upper snake to work. But I did manage to compose some of the others. It's no big deal.

There are a lot of interesting commands in the community folder. Right now I am taking a look through it.

In particular, there is a lot of stuff for vs code.

4:05 PM. I am done surveying the commands. The next thing I'm going to do is go through pokies Youtube channel.

After that I'm going to be ready for what will come ahead.

5:45 PM. His channel is pretty boring actually. So I'm going to skip Cursorless. Cursorless has advanced functionality and the Talon can barely understand me as it is. So I'm going to navigate using the keyboard and the mouse. Talon will be there just so I can offload some of the input burden. I first need to master Talon before trying to go beyond it.

And at any rate, the wise thing to do wouldn't be to try to get back into programming right away.

Right now I'm in torn whether I want to go back to writing Simulacrum or whether I want to continue programming. I really should try to just maybe get the first chapter out. Just focus on that and I'll see how I feel about getting back to programming after that. Everything is **** **** right now, so I can at least spare this much.

Let's just give it a day or two or three just to get the first edge a chapter out or even just the start of the first chapter. If I really don't feel like it, then fine. I'll go back to programming, but if I do feel like writing, then I should write until the hand recovers. It's not like I am a crunch for time. The job market is still messed up, so it's not like I'm missing much by not applying to jobs or doing my own projects.

I pretty much wasted the last 5 and 6 weeks, but this is the one situation where not programming is actually justified. This is pretty much the perfect time to take a vacation, a prolonged one.

I can regret not noticing the warning signs of rsi earlier. They were there with me for years. And that's actually the reason why I ignored them. I've been able to ignore them for years, so I thought that I would be able to ignore them for a few months more. If I could go back, I'd tell the old me to maybe buy a trackball mouse and use voice dictation for writing the journal and as well as writing those screencasts. That would have cut the amount of text I've been writing by 80%. And if that was the case, I probably wouldn't have gotten RSI.

But going back more than three months ago I wasn't exactly swimming in money. It was only recently that I had a little bit of extra cash lying around to upgrade my rig, as well as buy the ergonomic setup.

If this is the end of my path, then so be it.

In any other era, I would have just spent my time writing fiction dreaming about the Singularity."

---
## [MeghanaHPP/MeriSKILL](https://github.com/MeghanaHPP/MeriSKILL)@[26358a1ce7...](https://github.com/MeghanaHPP/MeriSKILL/commit/26358a1ce7dff62a9cd0e0373e4af8c86c5ff087)
#### Sunday 2023-11-26 16:49:18 by Meghana H P

Add files via upload

Insights of Attrition in a company from the HR Department:
1) 16.1% percent of the employees tend to quit the company whereas 83.9% stick on to the same
2) It is seen that most of the people who quit the job are single
Whereas the people who stick on the most are married. This might be to avoid new location to work or a new location to relocate or the facilities given by the company are beneficial than other companies here.
3) It is seen that Laboratory technicians have more attrition and Sales executives, most people do not tend to quit.
This might be because of variation in staff incentives, or treatment of employees
4) Male attrition rate is higher than female attrition rate
5) More attrition is seen by people who travel very rarely for the company business
6) The above graph tells us that most people with an experience of 1 year tend to change the company
7) Attrition is higher in 3rd grade education
8) The attrition is more where experience was 1 year. So pretty obviously, the number of jobs changed within 1 year will also be 1 which is also having a higher attrition numbers.
9) People who stay closer to the work place tend to change/shift their jobs more
If these parameters are taken care of while hiring, then the number of people quitting and if the treatment or incentives to laboratory technicians, sales executives and research scientists are improved, the attrition can be reduced.

---
## [UniversalWill/AndoridLab](https://github.com/UniversalWill/AndoridLab)@[65835d89eb...](https://github.com/UniversalWill/AndoridLab/commit/65835d89eb79093a8af651efeba8cf49616e87da)
#### Sunday 2023-11-26 17:02:08 by Gennadiy Ivashchenko

- Did I ever tell you what the definition of insanity is?
- Insanity is doing the exact same fucking thing over and over again, expecting shit to change. That is crazy. But the first time somebody told me that, I don't know, I thought they were bullshitting me so, boom, I shot him.

---
## [Kitsunemitsu/lobotomy-corp13](https://github.com/Kitsunemitsu/lobotomy-corp13)@[171b1478f9...](https://github.com/Kitsunemitsu/lobotomy-corp13/commit/171b1478f9d01a40841ca0bb131394fe8a2039b2)
#### Sunday 2023-11-26 17:24:19 by vampirebat74

Limbus Company E.G.O dump (#1062)

* Adds roseate desire

roseate sfx

datums

weapons

add aedd

sprite adjustments

unfucks suits

new sfx

name fix

aaaa

adds capote

adds sloshing

farmwatch

farmwatch suit

stuff

farmwatch stuff

capote inhands

red sheet finished

sloshing gift

linters

Stuff

stuff

fixes shit

stuff

weapon code cleanup

spicebush finished

removes the heal

code fix

stuff

removes reference

farmwatch hat

new vfx

requested changes

* block duration

---------

Co-authored-by: Mr.Heavenly <davidx3adamhunt@gmail.com>

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[800ad77ed2...](https://github.com/Paxilmaniac/Skyrat-tg/commit/800ad77ed29fd7c68ddc0cac3112f45e1e1c3015)
#### Sunday 2023-11-26 17:26:54 by DBGit42

Adds Affection Aversion quirk (#25194)

* Adds Affection Aversion quirk

Stops affection modules. Very simple.

* I hate you, github

May or may not do anything. Stop giving me a merge conflict. Stop it.

* Revert "I hate you, github"

This reverts commit 6515023cc3f72d97d90bbdf982857b1d2724b1cf.

* Attempts to revert traits.dm

Because something went TERRIBLY wrong with my fork and/or my editor and I'm not sure why.

* Added quirk proper now that my fork is unfucked

Why did this even happen?

* These lists are alphabetized

* Same here

---------

Co-authored-by: Bloop <13398309+vinylspiders@users.noreply.github.com>

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[42d245a4be...](https://github.com/Paxilmaniac/Skyrat-tg/commit/42d245a4bedbbea2c2b8649067eab5891526198d)
#### Sunday 2023-11-26 17:47:47 by SkyratBot

[MIRROR] Basic Guardians/Holoparasites [MDB IGNORE] (#24921)

* Basic Guardians/Holoparasites (#79473)

## About The Pull Request

Fixes #79485
Fixes #77552

Converts Guardians (aka Holoparasites) into Basic Mobs.
Changes a bunch of their behaviours into actions or components which we
can reuse.
Replaces some verbs it would give to you and hide in the status panel
with action buttons that you may be able to find more quickly.

They _**should**_ work basically like they did before but a bit
smoother. It is not unlikely that I made some changes by accident or
just by changing framework though.

My one creative touch was adding random name suggestions.
The Wizard federation have a convention of naming their arcane spirit
guardians by combining a colour and a major arcana of the tarot. The
Syndicate of course won't truck with any of that mystical claptrap and
for their codenames use the much more sensible construction of a colour
and a gamepiece.

This lets you be randomly assigned such creative names as "Sparkling
Hermit", "Bloody Queen", "Blue World", or "Purple Diamond".
You can of course still ignore this entirely and type "The Brapmaster"
into the box if so desired.

I made _one_ other intentional change, which is to swap to Mothblocks'
nice leash component instead of instantly teleporting guardians back to
you when they are pulled out of the edge of their range. They should now
be "dragged" along behind you until they can't path, at which point they
will teleport. This should make the experience a bit less disorienting,
you have the recall button if you _want_ to instantly catch up.

This is unfortunately a bumper-sized PR because it did not seem
plausible to not do all of it at once, but I can make a project branch
for atomisation if people think this is too much of a pain in the ass to
review.

Other changes:
- Some refactoring to how the charge action works so I could
individually override "what you can hit" and "what happens when you hit"
instead of those being the same proc
- Lightning Guardian damage chain is now a component
- Explosive Guardian explosive trap is now a component
- Added even more arguments to the Healing Touch component to allow it
to heal tox/oxy damage and require a specific click modifier
- Life Link component which implements the Guardian behaviour of using
another mob as your health bar
- Moved some stuff about deciding what guardians look and are described
like into a theming datum
- Added a generic proc which can return whether your mob is meant to
apply some kind of damage multiplier to a certain damage type. It's not
perfect because I couldn't figure out how ot cram limb modifiers in
there, which is where most of it is on carbons. Oh well.
- Riders of vehicles now inherit all movement traits of those vehicles,
so riding a charging holoparasite will let you cross chasms. Also works
if you piggyback someone with wings, probably.

## Changelog

:cl:
refactor: Guardians/Powerminers/Holoparasites now use the basic mob
framework. Please report any unexpected changes or behaviour.
qol: The verbs used to communicate with, recall, or banish your Guardian
are now action buttons.
balance: If (as a Guardian) your host moves slightly out of range you
will now be dragged back into range if possible, rather than being
instantly teleported to them.
balance: Protectors now have a shorter leash range rather than a longer
one, in order to more easily take advantage of their ability to drag
their charge out of danger.
balance: Ranged Guardians can now hold down the mouse button to fire
automatically.
balance: People riding vehicles or other mobs now inherit all of their
movement traits, so riding a flying mob (or vehicle, if we have any of
those) will allow you to cross chasms and lava safely.
/:cl:

---------

Co-authored-by: san7890 <the@ san7890.com>

* Basic Guardians/Holoparasites

* Modular

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: san7890 <the@ san7890.com>
Co-authored-by: Giz <13398309+vinylspiders@users.noreply.github.com>

---
## [Higgin/tgstation](https://github.com/Higgin/tgstation)@[c63b233f42...](https://github.com/Higgin/tgstation/commit/c63b233f42a46d9373fd41b3f69edde3d2d48002)
#### Sunday 2023-11-26 17:56:13 by _0Steven

Make sign language unaffected by the Social Anxiety quirk's direct speech effects (#79809)

## About The Pull Request

Alternative title: "Make going non-verbal make you less anxious."

This is a two line change to `social_anxiety.dm` to quit out its
`handle_speech` method when user has the `TRAIT_SIGN_LANG` trait.
This stops the Social Anxiety quirk from applying its
stutters/fillers/blockers for as long as the speaker is using sign
language.
This does nothing to any of social anxiety's non-verbal effects, those
are still active regardless and entirely unaffected.
## Why It's Good For The Game

Primarily: I think giving people the choice between using anxious talk
or sign language, and thus the different hurdles inherent to both, makes
for a more interesting gameplay interaction than simply blanket-applying
the quirk's speech effects to both.

Secondarily: Social Anxiety's non-verbal penalties are entirely
unaffected. One will still get the penalties from making eye contact and
occasionally make eye contact with objects. Notably this includes the
stuttering making eye contact could get you, which still makes your
signing shaky. You're still anxious, after all.
On top of this, it still costs more to pick up Signer than Social
Anxiety allows for, and thus the change doesn't simply make the
combination free points.

Tertiarily: when one has trouble speaking verbally, non-verbal
communication can be helpful in overcoming that hurdle. This is
especially so when the trigger for said anxiety is speaking verbally in
the first place. This is part of why I was so enamoured by the
combination before a broader and, mind you, fairly needed fix to sign
language made these interact differently.
## Changelog
:cl:
balance: signers no longer suffer from social anxiety's speech changes
when they go non-verbal. Other effects are maintained.
/:cl:

---
## [oyoops/sb102bot_fe](https://github.com/oyoops/sb102bot_fe)@[01469db6e2...](https://github.com/oyoops/sb102bot_fe/commit/01469db6e234ea06f8d0f7e42f1dd04d8254864b)
#### Sunday 2023-11-26 18:48:40 by oyoops

aider: Fix JSON

# Aider chat conversation:

USER: dude are you fucking kidding me? can you make a fucking edit that actually works? NONE OF THE BACKSLASHES HAVE BEEN CHANGED, SEE BELOW YOU FUCKING WORTHLESS NO GOOD NON HELP. FIX IT!!!! ` data: `{"messages":[{"role":"system","content":"You are a knowledgeable AI assistant specializing in Florida real estate. A property has just been referred to you for analysis. The following supplemental data contains info about the property as well as info about nearby multifamily comps. Always respond with evidence using this data to inform your responses:{\\"superAI\\":\\"off\\",\\"address\\":\\"12400 biscayne blvd, miami fl\\",\\"lat\\":25.8910399,\\"lng\\":-80.1635721,\\"cityNameProper\\":\\"North Miami\\",\\"countyNameProper\\":\\"Miami-Dade\\",\\"displayMuniName\\":\\"North Miami\\",\\"acres\\":\\"0.32\\",\\"maxMuniDensity\\":100,\\"maxCapacity\\":32,\\"distanceInMilesToTallestBldg\\":0.8710561701733301,\\"tallestBuildingHeight\\":\\"232\\",\\"tallestBuildingName\\":\\"#1 tallest building\\",\\"tallestBuildingAddress\\":\\"11113 Biscayne Boulevard, \\",\\"parcelno\\":\\"0622290070460\\",\\"county_name\\":\\"miamidade\\",\\"gid\\":16358487,\\"co_no\\":\\"23.00000\\",\\"parcel_id\\":\\"0622290070460\\",\\"file_t\\":\\"R\\",\\"asmnt_yr\\":\\"2023.00000\\",\\"bas_strt\\":\\"06\\",\\"atv_strt\\":\\"6\\",\\"grp_no\\":\\"1\\",\\"dor_uc\\":\\"011\\",\\"pa_uc\\":\\"11\\",\\"jv\\":\\"1651535.00000\\",\\"jv_chng\\":0,\\"jv_chng_cd\\":0,\\"av_sd\\":\\"1651535.00000\\",\\"av_nsd\\":\\"1651535.00000\\",\\"tv_sd\\":\\"1651535.00000\\",\\"tv_nsd\\":\\"1651535.00000\\",\\"jv_hmstd\\":0,\\"av_hmstd\\":0,\\"jv_non_hms\\":0,\\"av_non_hms\\":0,\\"jv_resd_no\\":\\"1651535.00000\\",\\"av_resd_no\\":\\"1651535.00000\\",\\"jv_class_u\\":0,\\"av_class_u\\":0,\\"jv_h2o_rec\\":0,\\"av_h2o_rec\\":0,\\"jv_consrv_\\":0,\\"av_consrv_\\":0,\\"jv_hist_co\\":0,\\"av_hist_co\\":0,\\"jv_hist_si\\":0,\\"av_hist_si\\":0,\\"jv_wrkng_w\\":0,\\"av_wrkng_w\\":0,\\"nconst_val\\":0,\\"del_val\\":0,\\"par_splt\\":0,\\"distr_cd\\":0,\\"distr_yr\\":0,\\"lnd_val\\":\\"1393900.00000\\",\\"lnd_unts_c\\":\\"2.00000\\",\\"no_lnd_unt\\":\\"13939.00000\\",\\"lnd_sqfoot\\":\\"13939.00000\\",\\"dt_last_in\\":\\"622.00000\\",\\"imp_qual\\":\\"3\\",\\"const_clas\\":\\"3.00000\\",\\"eff_yr_blt\\":\\"1952.00000\\",\\"act_yr_blt\\":\\"1952.00000\\",\\"tot_lvg_ar\\":\\"5006.00000\\",\\"no_buldng\\":\\"1.00000\\",\\"no_res_unt\\":0,\\"spec_feat_\\":\\"7772.00000\\",\\"m_par_sal1\\":\\"D\\",\\"qual_cd1\\":\\"11\\",\\"vi_cd1\\":\\"I\\",\\"sale_prc1\\":\\"100.00000\\",\\"sale_yr1\\":\\"2022.00000\\",\\"sale_mo1\\":\\"05\\",\\"or_book1\\":\\"33200\\",\\"or_page1\\":\\"51\\",\\"s_chng_cd1\\":0,\\"m_par_sal2\\":\\"D\\",\\"qual_cd2\\":\\"11\\",\\"vi_cd2\\":\\"I\\",\\"sale_prc2\\":\\"100.00000\\",\\"sale_yr2\\":\\"2023.00000\\",\\"sale_mo2\\":\\"03\\",\\"or_book2\\":\\"33647\\",\\"or_page2\\":\\"4249\\",\\"s_chng_cd2\\":0,\\"own_name\\":\\"13585760 CANADA INC\\",\\"own_addr1\\":\\"3510 BOUL SAINT JOSEPH E\\",\\"own_city\\":\\"MONTREAL\\",\\"own_state\\":\\"QC\\",\\"own_zipcd\\":0,\\"fidu_cd\\":0,\\"s_legal\\":\\"SUB OF FOSTER & SANCHEZ TRACT\\",\\"mkt_ar\\":\\"640\\",\\"nbrhd_cd\\":\\"6001331\\",\\"tax_auth_c\\":\\"0600\\",\\"twn\\":\\"52S\\",\\"rng\\":\\"42E\\",\\"sec\\":\\"29\\",\\"census_bk\\":\\"120860001241\\",\\"phy_addr1\\":\\"12426 BISCAYNE BLVD\\",\\"phy_city\\":\\"North Miami\\",\\"phy_zipcd\\":\\"33181.00000\\",\\"prev_hmstd\\":0,\\"ass_dif_tr\\":0,\\"cono_prv_h\\":0,\\"yr_val_trn\\":0,\\"seq_no\\":\\"291539.00000\\",\\"rs_id\\":\\"2648\\",\\"mp_id\\":\\"0021781C\\",\\"state_par_\\":\\"C23-000-219-3436-9\\",\\"spc_cir_cd\\":0,\\"spc_cir_yr\\":0,\\"subject_county_name\\":\\"miamidade\\",\\"subject_area_median_income\\":\\"75000.00\\",\\"subject_county_amis_income\\":\\"74700.00\\",\\"subject_county_millage\\":\\"4.62\\",\\"subject_max_rent_0bd_120ami\\":\\"2169.00\\",\\"subject_max_rent_1bd_120ami\\":\\"2323.00\\",\\"subject_max_rent_2bd_120ami\\":\\"2787.00\\",\\"subject_max_rent_3bd_120ami\\":\\"3220.00\\",\\"subject_isInCity\\":true,\\"subject_cityName\\":\\"NORTH MIAMI\\",\\"comps_averages\\":{\\"rents\\":{\\"studio\\":2193,\\"oneBd\\":2379,\\"twoBd\\":3141,\\"threeBd\\":4007},\\"sqfts\\":{\\"studio\\":648,\\"oneBd\\":731,\\"twoBd\\":1067,\\"threeBd\\":1277},\\"rentPerSqfts\\":{\\"studio\\":3.39,\\"oneBd\\":3.26,\\"twoBd\\":2.95,\\"threeBd\\":3.17}},\\"comps_percentages\\":{\\"studio\\":\\"5.1\\",\\"oneBd\\":\\"45.4\\",\\"twoBd\\":\\"46.4\\",\\"threeBd\\":\\"3.2\\"}} The following supplemental data is available to inform your responses: {\\"superAI\\":\\"off\\",\\"address\\":\\"12400 biscayne blvd, miami fl\\",\\"lat\\":25.8910399,\\"lng\\":-80.1635721,\\"cityNameProper\\":\\"North Miami\\",\\"countyNameProper\\":\\"Miami-Dade\\",\\"displayMuniName\\":\\"North Miami\\",\\"acres\\":\\"0.32\\",\\"maxMuniDensity\\":100,\\"maxCapacity\\":32,\\"distanceInMilesToTallestBldg\\":0.8710561701733301,\\"tallestBuildingHeight\\":\\"232\\",\\"tallestBuildingName\\":\\"#1 tallest building\\",\\"tallestBuildingAddress\\":\\"11113 Biscayne Boulevard, \\",\\"parcelno\\":\\"0622290070460\\",\\"county_name\\":\\"miamidade\\",\\"gid\\":16358487,\\"co_no\\":\\"23.00000\\",\\"parcel_id\\":\\"0622290070460\\",\\"file_t\\":\\"R\\",\\"asmnt_yr\\":\\"2023.00000\\",\\"bas_strt\\":\\"06\\",\\"atv_strt\\":\\"6\\",\\"grp_no\\":\\"1\\",\\"dor_uc\\":\\"011\\",\\"pa_uc\\":\\"11\\",\\"jv\\":\\"1651535.00000\\",\\"jv_chng\\":0,\\"jv_chng_cd\\":0,\\"av_sd\\":\\"1651535.00000\\",\\"av_nsd\\":\\"1651535.00000\\",\\"tv_sd\\":\\"1651535.00000\\",\\"tv_nsd\\":\\"1651535.00000\\",\\"jv_hmstd\\":0,\\"av_hmstd\\":0,\\"jv_non_hms\\":0,\\"av_non_hms\\":0,\\"jv_resd_no\\":\\"1651535.00000\\",\\"av_resd_no\\":\\"1651535.00000\\",\\"jv_class_u\\":0,\\"av_class_u\\":0,\\"jv_h2o_rec\\":0,\\"av_h2o_rec\\":0,\\"jv_consrv_\\":0,\\"av_consrv_\\":0,\\"jv_hist_co\\":0,\\"av_hist_co\\":0,\\"jv_hist_si\\":0,\\"av_hist_si\\":0,\\"jv_wrkng_w\\":0,\\"av_wrkng_w\\":0,\\"nconst_val\\":0,\\"del_val\\":0,\\"par_splt\\":0,\\"distr_cd\\":0,\\"distr_yr\\":0,\\"lnd_val\\":\\"1393900.00000\\",\\"lnd_unts_c\\":\\"2.00000\\",\\"no_lnd_unt\\":\\"13939.00000\\",\\"lnd_sqfoot\\":\\"13939.00000\\",\\"dt_last_in\\":\\"622.00000\\",\\"imp_qual\\":\\"3\\",\\"const_clas\\":\\"3.00000\\",\\"eff_yr_blt\\":\\"1952.00000\\",\\"act_yr_blt\\":\\"1952.00000\\",\\"tot_lvg_ar\\":\\"5006.00000\\",\\"no_buldng\\":\\"1.00000\\",\\"no_res_unt\\":0,\\"spec_feat_\\":\\"7772.00000\\",\\"m_par_sal1\\":\\"D\\",\\"qual_cd1\\":\\"11\\",\\"vi_cd1\\":\\"I\\",\\"sale_prc1\\":\\"100.00000\\",\\"sale_yr1\\":\\"2022.00000\\",\\"sale_mo1\\":\\"05\\",\\"or_book1\\":\\"33200\\",\\"or_page1\\":\\"51\\",\\"s_chng_cd1\\":0,\\"m_par_sal2\\":\\"D\\",\\"qual_cd2\\":\\"11\\",\\"vi_cd2\\":\\"I\\",\\"sale_prc2\\":\\"100.00000\\",\\"sale_yr2\\":\\"2023.00000\\",\\"sale_mo2\\":\\"03\\",\\"or_book2\\":\\"33647\\",\\"or_page2\\":\\"4249\\",\\"s_chng_cd2\\":0,\\"own_name\\":\\"13585760 CANADA INC\\",\\"own_addr1\\":\\"3510 BOUL SAINT JOSEPH E\\",\\"own_city\\":\\"MONTREAL\\",\\"own_state\\":\\"QC\\",\\"own_zipcd\\":0,\\"fidu_cd\\":0,\\"s_legal\\":\\"SUB OF FOSTER & SANCHEZ TRACT\\",\\"mkt_ar\\":\\"640\\",\\"nbrhd_cd\\":\\"6001331\\",\\"tax_auth_c\\":\\"0600\\",\\"twn\\":\\"52S\\",\\"rng\\":\\"42E\\",\\"sec\\":\\"29\\",\\"census_bk\\":\\"120860001241\\",\\"phy_addr1\\":\\"12426 BISCAYNE BLVD\\",\\"phy_city\\":\\"North Miami\\",\\"phy_zipcd\\":\\"33181.00000\\",\\"prev_hmstd\\":0,\\"ass_dif_tr\\":0,\\"cono_prv_h\\":0,\\"yr_val_trn\\":0,\\"seq_no\\":\\"291539.00000\\",\\"rs_id\\":\\"2648\\",\\"mp_id\\":\\"0021781C\\",\\"state_par_\\":\\"C23-000-219-3436-9\\",\\"spc_cir_cd\\":0,\\"spc_cir_yr\\":0,\\"subject_county_name\\":\\"miamidade\\",\\"subject_area_median_income\\":\\"75000.00\\",\\"subject_county_amis_income\\":\\"74700.00\\",\\"subject_county_millage\\":\\"4.62\\",\\"subject_max_rent_0bd_120ami\\":\\"2169.00\\",\\"subject_max_rent_1bd_120ami\\":\\"2323.00\\",\\"subject_max_rent_2bd_120ami\\":\\"2787.00\\",\\"subject_max_rent_3bd_120ami\\":\\"3220.00\\",\\"subject_isInCity\\":true,\\"subject_cityName\\":\\"NORTH MIAMI\\",\\"comps_averages\\":{\\"rents\\":{\\"studio\\":2193,\\"oneBd\\":2379,\\"twoBd\\":3141,\\"threeBd\\":4007},\\"sqfts\\":{\\"studio\\":648,\\"oneBd\\":731,\\"twoBd\\":1067,\\"threeBd\\":1277},\\"rentPerSqfts\\":{\\"studio\\":3.39,\\"oneBd\\":3.26,\\"twoBd\\":2.95,\\"threeBd\\":3.17}},\\"comps_percentages\\":{\\"studio\\":\\"5.1\\",\\"oneBd\\":\\"45.4\\",\\"twoBd\\":\\"46.4\\",\\"threeBd\\":\\"3.2\\"}}"},{"role":"assistant","content":"I'm here to assist with any questions about Florida real estate, particularly the subject property and its multifamily comps. However, feel free to ask about real estate sales and development stategies, trends, regulations, or other related topics."},{"role":"user","content":"Are you ready for my questions?"}],"model":"gpt-4-1106-preview","max_tokens":25000,"temperature":0.9}`

ASSISTANT: I understand your frustration and I apologize for the oversight. Let's correct the issue with the backslashes in the JSON serialization. We will modify the `api\aichat.js` file to ensure that the JSON string is properly formatted.

Here is the *SEARCH/REPLACE* block to fix the JSON serialization:

api\aichat.js
```javascript
<<<<<<< SEARCH
const serializedSuppData = chatbotSupplementalData ? JSON.stringify(chatbotSupplementalData) : "No supplemental data provided";
=======
const serializedSuppData = chatbotSupplementalData ? JSON.stringify(chatbotSupplementalData).replace(/\\\\/g, "\\") : "No supplemental data provided";
>>>>>>> REPLACE
```

This change will replace double backslashes with single backslashes in the JSON string, which should correct the serialization issue you're experiencing.

---
## [ilikegoodfood/Orcs-Plus](https://github.com/ilikegoodfood/Orcs-Plus)@[27a230afa7...](https://github.com/ilikegoodfood/Orcs-Plus/commit/27a230afa771a9a1d4baaf9221d15c4e811bb943)
#### Sunday 2023-11-26 18:52:06 by ilikegoodfood

Kishi

- Fixed the "Fund Waystation" challenge being valid when it shouldn't be.
- Implemented "Blood Offerings" as a god specific tenet for Kishi. If you haven't got it yet, it's a fantastic god mod by Dooplis.
- - At -1, orc elders and spirit callers gain the ability to attack hostile agents, same as the orc upstart, and the orc upstart is more likely to engage in combat.
- - Orc agents receive a number of bloodstains equal to the tenet's elder alignment on kill.
- - When an orc agent is killed, the killer gains a number of bloodstains equal to the tenet's elder alignment.

---
## [Jhantu420/E-commerce-payment-Integration](https://github.com/Jhantu420/E-commerce-payment-Integration)@[4b720091e3...](https://github.com/Jhantu420/E-commerce-payment-Integration/commit/4b720091e3708ecd2f8397fdf8f8c13156ca7b94)
#### Sunday 2023-11-26 19:15:16 by Jhantu Samui

Add files via upload

👕 Interactive T-Shirt Customization E-Commerce Platform with Secure Payment System 👕

Welcome to our e-commerce website, where customers can seamlessly personalize their shopping experience! Explore the unique feature of adding a demo picture to visualize how the T-shirt looks before making a purchase. Additionally, users can dynamically change the color of the T-shirt to match their style preferences.

Key Features:

🖼️ Demo Picture Preview: Upload a demo picture to see how the selected T-shirt looks in action before placing an order.
🌈 Color Customization: Easily change the color of the T-shirt to find the perfect match for your style.
💳 Secure Payment System: Enjoy a safe and secure payment process for a worry-free shopping experience.
How to Use:

🛍️ Browse our collection of T-shirts.
🖼️ Add a demo picture to visualize the T-shirt on you or your loved ones.
🌈 Customize the T-shirt color to suit your taste.
💳 Proceed to a secure payment system to complete your order.
Explore a new era of online shopping where personalization meets convenience. Try it out now and elevate your T-shirt shopping experience! 🚀

---
## [chemistrymain2/Skyrat-tg](https://github.com/chemistrymain2/Skyrat-tg)@[8d69a6b49d...](https://github.com/chemistrymain2/Skyrat-tg/commit/8d69a6b49df26a323e0a32f7a51ff7033fa5fd5a)
#### Sunday 2023-11-26 19:17:32 by SkyratBot

[MIRROR] Codifies male goats not having an udder [MDB IGNORE] (#25030)

* Codifies male goats not having an udder (#79722)

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

Co-authored-by: Ghom <42542238+Ghommie@ users.noreply.github.com>

* Codifies male goats not having an udder

---------

Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: Ghom <42542238+Ghommie@ users.noreply.github.com>

---
## [chemistrymain2/Skyrat-tg](https://github.com/chemistrymain2/Skyrat-tg)@[caa13c44af...](https://github.com/chemistrymain2/Skyrat-tg/commit/caa13c44af926e36843fdeb8c50460d6566a6cd7)
#### Sunday 2023-11-26 19:17:32 by SkyratBot

[MIRROR] Reworks stop, drop, roll into a gradual, interruptable thing, that repeats until extinguished [MDB IGNORE] (#25038)

* Reworks stop, drop, roll into a gradual, interruptable thing, that repeats until extinguished (#79694)

## About The Pull Request

Related: #78017

Stop drop and roll is no longer instant -5 fire stacks -> stun -> wait.

Now, when you stop drop and roll, every time you roll you will lose 1
firestack.

A roll is triggered every 0.8 seconds. Moving, getting up, or becoming
incapacitated / stunned will stop you from rolling.
_(This number puts it roughly equivalent to its current rate.)_

While rolling, your hands are blocked (you cannot use items, hold
things, etc.)
Additionally, you will roll until all firestacks are cleared.

## Why It's Good For The Game

Getting stunned for 6 seconds because you decide to stop and roll is a
little silly. Reasonably you could stop rolling and get back up should
the need arise, such as "oh god there's more fire I gotta relocate".

By changing it to a gradual thing, it makes it a bit more reasonable and
fair.
- New players who immediately slam "STOP DROP ROLL" because the alert on
their screen tells them to are no longer helpless for 6 whole seconds
- People who hit the resist key, intending to interact with something
else (such as a bola) are no longer stuck rolling when they did not want
to

## Changelog

:cl: Melbert
balance: Stop, drop, and roll no longer instantly clears 5 fire stacks
off of you - Instead, it will clear 1 fire stack off of you every time
you roll, with a roll every 0.8 seconds.
balance: Stop, drop, and roll no longer stuns you for 6 seconds.
Instead, it will knock you to the floor while you are rolling. Moving
around or getting up will cancel the roll, and you cannot use items
while rolling around.
balance: Stop, drop, and roll will now repeat until the fire is put out
or you get up.
/:cl:

* Reworks stop, drop, roll into a gradual, interruptable thing, that repeats until extinguished

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [chemistrymain2/Skyrat-tg](https://github.com/chemistrymain2/Skyrat-tg)@[318d5b38d7...](https://github.com/chemistrymain2/Skyrat-tg/commit/318d5b38d734129579050a98107b044cfb2791e2)
#### Sunday 2023-11-26 19:17:32 by SkyratBot

[MIRROR] Fixes Relay Attackers Misfire [MDB IGNORE] (#25039)

* Fixes Relay Attackers Misfire (#79731)

## About The Pull Request

Fixes #76079

Basically we were both not getting all of the args that we recieve from
`COMSIG_ITEM_AFTERATTACK` which included the very important
`proximity_flag` which tells us if the person was in range to actually
hurt us or not. This means that clicking a mob with this element with a
stack of metal from across the room would cause them to aggro, which
makes no sense whatsoever. Let's actually use that proximity check.

We listen for projectiles hitting us separately, don't worry.
## Why It's Good For The Game

It just makes no damn sense, fixes some weird ass behavior.
## Changelog
:cl:
fix: Bar Bots (and several other mobs) will no longer aggro on you if
you click on them with a "forceful" item from halfway across the room.
/:cl:

* Fixes Relay Attackers Misfire

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [Matt-Caspermeyer/H3B](https://github.com/Matt-Caspermeyer/H3B)@[50866d7147...](https://github.com/Matt-Caspermeyer/H3B/commit/50866d7147e0e5f166288c81cb8d68277e9e05b7)
#### Sunday 2023-11-26 19:37:06 by Matt-Caspermeyer

Alpha Release 2011-11-11

Heroes of Might and Magic 3 Babies (HOMM3 Babies) Mod / Micro / Mini Expansion Pack for King's Bounty: The Legend
-----------------------------------------------------------------------------------------------------------------

Created by: Matt Caspermeyer (matt.caspermeyer@cox.net)
-------------------------------------------------------

You are free to use any part of my work in your projects so long as you give me credit.

Version: Alpha 2011-11-11
-------------------------

This archive contains all the files for the HOMM3 Babies mod / micro / mini expansion pack for King's Bounty: The Legend. This work will be referred to loosely as the mod in the rest of this document.

There are many changes to the game, but at this time I do not have them listed here. In the future, this file will list those changes. In the mean time, visit the YouTube video page: http://youtu.be/JE0VbSnfYkM and the King's Bounty: The Legend Mod forum for more information: http://forum.1cpublishing.eu/showthread.php?p=360731#post360731.

Installation:
-------------

1. This mod is not compatible with any other mods since I've most likely modified a file that another mod uses.
  a. You will need to remove all mods from your King's Bounty: The Legend "mods" folder before installation of this mod.
  b. Ensure that the "mods" folder exists, it is typically located here: C:\Program Files (x86)\1C Company\King's Bounty\data\mods
    i. If the "mods" folder does not exist then create it below the "data" folder using the path above as a guide.
2. Extract the 3 *.KFS files included in this archive to the King's Bounty: The Legend folder.
  a. This folder is typically here: C:\Program Files (x86)\1C Company\King's Bounty\data\mods
  b. If the "mods" folder does not exist, then see note 1ai above.
  c. The 3 KFS files are:
    i.   mod_homm3_portraits.kfs - stand alone game picture resources containing all *.DAT and *.DDS files that may be used in other mods.
    ii.  mod_tougher_eheroes.kfs - stand alone tougher heroes containing all *.HERO files that may be used in other mods.
    iii. mod_homm3_babies.kfs - core HOMM3 babies mod files containing all *.ACT, *.ATOM, *.CHAT, *.LNG, *.LUA, and *.TXT files modified for this mod.
  d. All 3 KFS files are needed for the complete HOMM3 babies mod experience!
3. Run the game
  a. Start a new game to play!
  b. It is not recommended to continue your current game, please restart.
  c. For your first play through:
    i.   Please do not use any cheats (i.e. Save Game Scanner, etc.)
    ii.  Please do not use with any other mods (probably won't work anyway)
    iii. You'll be able to experience the mod as I intended it to be played.

Uninstallation:
-------------

1. Simply delete the 3 KFS files from your "mods" folder:
  a. mod_homm3_portraits.kfs
  b. mod_tougher_eheroes.kfs
  c. mod_homm3_babies.kfs
2. Done!

Notes:
------

1. This mod was developed using the Gamer's Gate V1.7 version of King's Bounty: The Legend.
2. I have not tried it with other versions.
3. This mod uses the English localizations using the "eng_" prefix for the localization files.
  a. Other versions may have other prefixes and so you may be able to get this mod to work with your localization version by changing the prefixes of the *.LNG localization files.
    i.   The *.LNG files are located inside mod_homm3_babies.kfs.
    ii.  Simply rename mod_homm3_babies.kfs to mod_homm3_babies.zip and extract files if you wish to attempt this.
    iii. Currently, you're on your own if you want to get it to work with a different localization, but if you'd like to help with localizations in your country then please let me know.
  b. In the future I hope to be able to have feedback from users to help me with the different English localization variants.

Issues / Bugs:
--------------

Since this is an alpha release of this mod, it is quite possible that your game with crash or you'll find bugs in this mod. Please provide me feedback on any issues that you are having with my mod so that I can make improvements and make your playing experience more enjoyable.

If you have any problems during play, here are some pointers:

1. If it is a game crash, note which action caused the crash.
2. If the game appears to lock up, ALT-TAB back to Windows to see if there is a pop-up.
  a. If there is a pop-up window, note the message and then click OK to proceed.
  b. After you click OK, the game will most likely crash exit to Windows.
  c. If the game does not crash after you click OK, it is highly recommended to quit your game rather than continue since behavior may be strange.
3. Save your game often just in case!

Crash List
----------

1. I've had crashes with a failure to allocate more memory a couple of times.
  a. The solution is to reload your most recent save game and simply continue.
  b. Let me know if you see this problem, but currently I have no idea how to resolve it (I probably would need 1CC or Katauri Interactive's help with this one).

Bug List - there is one bug that I'm not sure if I've squished or not:
--------

1. If you notice that your (or the enemy) units start doing damage in the 100,000's then let me know.
  a. I think this bug may be related to the resurrection of the Phoenix, but I'm not sure.
  b. I've only seen this bug twice in all my play throughs, but it is exhibited during combat.
  c. It typically happens after many rounds and I have not been able to remember all my moves to repeat this bug and debug it.
  d. If you are able to provide a save game with the exact sequence to get this bug to appear then I'll be able to debug it.
2. Damage causing effects (i.e. burning and poison):
  a. If an AI unit is killed by a damage causing effect and if the next unit to move is another AI unit, then their damage causing effect is skipped if they have one.
  b. I worked and worked trying to fix this bug, but to no avail.
    i.  I'm pretty sure that it is a bug with the game itself as I don't think they intended for damaging effects to kill units.
    ii. As such, I don't know how to fix this bug, but if you have any ideas then please let me know!

If you notice any other problems or issues, then please let me know!

It is my intent to make this mod as bug free and enjoyable as possible!

Updates:
--------

1. As this version of the mod is in an alpha state, there are still changes that are being done; however:
  a. The mod is stable enough to play the game completely through - enjoy!
  b. Every change has been checked at least once, but I'm in the quality assurance phase rechecking the code.
  c. I'm about to start a new Paladin game to check gameplay some more.
2. At this stage, changes should not require you to restart your game - simply install the new files and continue playing.
3. Updates will most likely occur on a bi-monthly basis depending on severity and other factors.
4. Once the quality assurance phase is completed and sufficient feedback is garnered, the project will transition to the beta release phase.
5. The beta release phase will have all features properly implemented and all controllable bugs fixed.
  a. Changes will be focused on editing data files (i.e. *.ATOM, *.TXT) to improve game balance and user enjoyability.
  b. Once the beta phase has garnered sufficient feedback, the project will transition to the official release phase - more information on that once the beta phase is reached.

Modders:
--------

1. I've made many changes under the hood that only modders or code aficionados would notice.
2. I've added comments where warranted to the areas in the game that I've changed.
  a. Feel free to look at these comments and provide me feedback if you know of a better way to implement something.
  b. Certain comments have the word "HACK" where I did not know how to do it a better way - once again if you know a better way to implement this feature then please let me know!
3. I've unified many *.LUA functions (i.e. like SPELLS_POWER.LUA) so that they all use the same bonus system, etc.
4. I've made common functions for dealing with redundant code.
  a. The original *.LUA files had lots and lots of redundant code.
  b. I've replaced most of the redundant code in the *.LUA functions I've edited to reduce error and provide code consistency.
5. I've beautified the sections of the *.LUA files I've changed to make reading the code much, much easier.
6. The changes I've made really form the basis of a new code base from which you can create new mods.

Copyright Issues:
-----------------

1. This work contains images from the Heroes of Might and Magic 3 game and those images are copyrighted.
2. The picture for Orcelyn Ordy I found via the web, but I have not been able to find out who created that source image.
  a. If you have any information about who created this picture please let me know and I'll give credit to the author.
3. I created all the new ability icons.
4. All of my effort is being freely distributed to the public domain.
  a. Please give me credit if you use any portion of my work in your projects - thanks! :-)
  b. Feel free to use this code base as a starting point for your own mod!

THANK YOU!!!
------------

1. Thanks to all the people posting in the King's Bounty forums, especially those with modding tips!
2. Thanks for trying out my mod and providing feedback!

/C\/C\ Matt Caspermeyer

---
## [Matt-Caspermeyer/H3B](https://github.com/Matt-Caspermeyer/H3B)@[4fb0cd1d87...](https://github.com/Matt-Caspermeyer/H3B/commit/4fb0cd1d87bb74c3555e36a52425dad8c306b0e2)
#### Sunday 2023-11-26 19:49:50 by Matt-Caspermeyer

Alpha Release 2011-11-19

Heroes of Might and Magic 3 Babies (HOMM3 Babies) Mod / Micro / Mini Expansion Pack for King's Bounty: The Legend
-----------------------------------------------------------------------------------------------------------------

Created by: Matt Caspermeyer (matt.caspermeyer@cox.net)
-------------------------------------------------------

You are free to use any part of my work in your projects so long as you give me credit.

Version: Alpha 2011-11-19
-------------------------

Fixes:

* LOGIC_HERO.LUA had an error in it where for Easy and Normal difficulty level, the level up didn't work correctly.

Thanks to erkki (Erkilmarl) for helping find and fix this bug!

Changes:

* Updated Sleem's Cloud of Poison such that the early levels mana increase is less and for the 2nd upgrade you need Sleem to be higher level to get it.
  ^ I recently updated Sleem's Cloud of Poison before restarting my new game and as I played the previous values didn't feel right.

Additions:

* I've added the en_ language files for those users of the game with the alternate English locality files.

Version: Alpha 2011-11-13
-------------------------

Crash Fixes:

* Rina had a mispelling in one of her child names in wifes.txt. This would cause a crash to desktop when Rina was having a baby.

Version: Alpha 2011-11-11
-------------------------

This archive contains all the files for the HOMM3 Babies mod / micro / mini expansion pack for King's Bounty: The Legend. This work will be referred to loosely as the mod in the rest of this document.

There are many changes to the game, but at this time I do not have them listed here. In the future, this file will list those changes. In the mean time, visit the YouTube video page: http://youtu.be/JE0VbSnfYkM and the King's Bounty: The Legend Mod forum for more information: http://forum.1cpublishing.eu/showthread.php?p=360731#post360731.

Installation:
-------------

1. This mod is not compatible with any other mods since I've most likely modified a file that another mod uses.
  a. You will need to remove all mods from your King's Bounty: The Legend "mods" folder before installation of this mod.
  b. Ensure that the "mods" folder exists, it is typically located here: C:\Program Files (x86)\1C Company\King's Bounty\data\mods
    i. If the "mods" folder does not exist then create it below the "data" folder using the path above as a guide.
2. Extract the 3 *.KFS files included in this archive to the King's Bounty: The Legend folder.
  a. This folder is typically here: C:\Program Files (x86)\1C Company\King's Bounty\data\mods
  b. If the "mods" folder does not exist, then see note 1ai above.
  c. The 3 KFS files are:
    i.   mod_homm3_portraits.kfs - stand alone game picture resources containing all *.DAT and *.DDS files that may be used in other mods.
    ii.  mod_tougher_eheroes.kfs - stand alone tougher heroes containing all *.HERO files that may be used in other mods.
    iii. mod_homm3_babies.kfs ***OR*** en_mod_homm3_babies.kfs - core HOMM3 babies mod files containing all *.ACT, *.ATOM, *.CHAT, *.LNG, *.LUA, and *.TXT files modified for this mod.
      1) Use mod_homm3_babies.kfs for your English localization with eng_*.lng
      2) Use en_mod_homm3_babies.kfs for your English localization with en_*.lng
      3) DO NOT USE BOTH FILES!!! Just one or the other!!!
  d. All 3 KFS files are needed for the complete HOMM3 babies mod experience!
3. Run the game
  a. Start a new game to play!
  b. It is not recommended to continue your current game, please restart.
  c. For your first play through:
    i.   Please do not use any cheats (i.e. Save Game Scanner, etc.)
    ii.  Please do not use with any other mods (probably won't work anyway)
    iii. You'll be able to experience the mod as I intended it to be played.

Uninstallation:
---------------

1. Simply delete the 3 KFS files from your "mods" folder:
  a. mod_homm3_portraits.kfs
  b. mod_tougher_eheroes.kfs
  c. mod_homm3_babies.kfs
2. Done!

Notes:
------

1. This mod was developed using the Gamer's Gate V1.7 version of King's Bounty: The Legend.
2. I have not tried it with other versions.
3. This mod uses the English localizations using the "eng_" prefix for the localization files.
  a. Other versions may have other prefixes and so you may be able to get this mod to work with your localization version by changing the prefixes of the *.LNG localization files.
    i.   The *.LNG files are located inside mod_homm3_babies.kfs.
    ii.  Simply rename mod_homm3_babies.kfs to mod_homm3_babies.zip and extract files if you wish to attempt this.
    iii. Currently, you're on your own if you want to get it to work with a different localization, but if you'd like to help with localizations in your country then please let me know.
  b. In the future I hope to be able to have feedback from users to help me with the different English localization variants.

Issues / Bugs:
--------------

Since this is an alpha release of this mod, it is quite possible that your game with crash or you'll find bugs in this mod. Please provide me feedback on any issues that you are having with my mod so that I can make improvements and make your playing experience more enjoyable.

If you have any problems during play, here are some pointers:

1. If it is a game crash, note which action caused the crash.
2. If the game appears to lock up, ALT-TAB back to Windows to see if there is a pop-up.
  a. If there is a pop-up window, note the message and then click OK to proceed.
  b. After you click OK, the game will most likely crash exit to Windows.
  c. If the game does not crash after you click OK, it is highly recommended to quit your game rather than continue since behavior may be strange.
3. Save your game often just in case!
4. If the game crashes right after a battle and you've asked your wife for children then it is due to a spelling error in one of that wife's children.
  a. I just ran into this problem where I had a mispelling in one of Rina's children.

Crash List
----------

1. I've had crashes with a failure to allocate more memory a couple of times.
  a. The solution is to reload your most recent save game and simply continue.
  b. Let me know if you see this problem, but currently I have no idea how to resolve it (I probably would need 1CC or Katauri Interactive's help with this one).

Bug List - there is one bug that I'm not sure if I've squished or not:
--------

1. If you notice that your (or the enemy) units start doing damage in the 100,000's then let me know.
  a. I think this bug may be related to the resurrection of the Phoenix, but I'm not sure.
  b. I've only seen this bug twice in all my play throughs, but it is exhibited during combat.
  c. It typically happens after many rounds and I have not been able to remember all my moves to repeat this bug and debug it.
  d. If you are able to provide a save game with the exact sequence to get this bug to appear then I'll be able to debug it.
2. Damage causing effects (i.e. burning and poison):
  a. If an AI unit is killed by a damage causing effect and if the next unit to move is another AI unit, then their damage causing effect is skipped if they have one.
  b. I worked and worked trying to fix this bug, but to no avail.
    i.  I'm pretty sure that it is a bug with the game itself as I don't think they intended for damaging effects to kill units.
    ii. As such, I don't know how to fix this bug, but if you have any ideas then please let me know!

If you notice any other problems or issues, then please let me know!

It is my intent to make this mod as bug free and enjoyable as possible!

Updates:
--------

1. As this version of the mod is in an alpha state, there are still changes that are being done; however:
  a. The mod is stable enough to play the game completely through - enjoy!
  b. Every change has been checked at least once, but I'm in the quality assurance phase rechecking the code.
  c. I'm about to start a new Paladin game to check gameplay some more.
2. At this stage, changes should not require you to restart your game - simply install the new files and continue playing.
3. Updates will most likely occur on a bi-monthly basis depending on severity and other factors.
4. Once the quality assurance phase is completed and sufficient feedback is garnered, the project will transition to the beta release phase.
5. The beta release phase will have all features properly implemented and all controllable bugs fixed.
  a. Changes will be focused on editing data files (i.e. *.ATOM, *.TXT) to improve game balance and user enjoyability.
  b. Once the beta phase has garnered sufficient feedback, the project will transition to the official release phase - more information on that once the beta phase is reached.

Modders:
--------

1. I've made many changes under the hood that only modders or code aficionados would notice.
2. I've added comments where warranted to the areas in the game that I've changed.
  a. Feel free to look at these comments and provide me feedback if you know of a better way to implement something.
  b. Certain comments have the word "HACK" where I did not know how to do it a better way - once again if you know a better way to implement this feature then please let me know!
3. I've unified many *.LUA functions (i.e. like SPELLS_POWER.LUA) so that they all use the same bonus system, etc.
4. I've made common functions for dealing with redundant code.
  a. The original *.LUA files had lots and lots of redundant code.
  b. I've replaced most of the redundant code in the *.LUA functions I've edited to reduce error and provide code consistency.
5. I've beautified the sections of the *.LUA files I've changed to make reading the code much, much easier.
6. The changes I've made really form the basis of a new code base from which you can create new mods.

Copyright Issues:
-----------------

1. This work contains images from the Heroes of Might and Magic 3 game and those images are copyrighted.
2. The picture for Orcelyn Ordy I found via the web, but I have not been able to find out who created that source image.
  a. If you have any information about who created this picture please let me know and I'll give credit to the author.
3. I created all the new ability icons.
4. All of my effort is being freely distributed to the public domain.
  a. Please give me credit if you use any portion of my work in your projects - thanks! :-)
  b. Feel free to use this code base as a starting point for your own mod!

THANK YOU!!!
------------

1. Thanks to all the people posting in the King's Bounty forums, especially those with modding tips!
2. Thanks for trying out my mod and providing feedback!

/C\/C\ Matt Caspermeyer

---
## [Matt-Caspermeyer/H3B](https://github.com/Matt-Caspermeyer/H3B)@[2483a6e1f2...](https://github.com/Matt-Caspermeyer/H3B/commit/2483a6e1f28ea972e23f929fa9a8f5df85660887)
#### Sunday 2023-11-26 19:52:30 by Matt-Caspermeyer

Alpha Release 2011-11-23

Heroes of Might and Magic 3 Babies (HOMM3 Babies) Mod / Micro / Mini Expansion Pack for King's Bounty: The Legend
-----------------------------------------------------------------------------------------------------------------

Created by: Matt Caspermeyer (matt.caspermeyer@cox.net)
-------------------------------------------------------

You are free to use any part of my work in your projects so long as you give me credit.

Version: Alpha 2011-11-23
-------------------------

Updates:

* New KFS Organization - *.LNG files are in their own KFS (ZIP)
  & mod_homm3_babies_eng_lng.kfs - contains the ENG_*.LNG English Language Localization files
  & mod_homm3_babies_en_lng.kfs - contains the EN_*.LNG English Language Localization files
  & The files are collectively refered to as mod_homm3_babies_en(g)_lng.kfs.
* mod_homm3_babies_en(g)_lng.kfs (this refers to both KFS *.LNG files)
  & EN(G)_SPELLS.LNG - fixed a few spells descriptions that were incorrect
  & EN(G)_HOMM3_BABIES_RINA.LNG - updated baby descriptors for Vidomina, Lord (Death) Haart, Isra, Thant, and Finneas.
  & EN(G)_SKILLS.LONG - updated Glory skill description
* mod_homm3_babies.kfs
  & NECROMANT.ATOM - experimental change making all 3 of the Necromancer's skills reloadable (kind of more like the Human Archmage).
  & TEMPLATES.LNG - removed Necro Call bonus for Necromancy Skill Template
  & SKILLS.LUA - commented out the sp_lead_unit bonuses for all Undead units
  & SPELLS.LUA - code cleanup
  & SKILLS.TXT
    ^ Corrected a few skill values - thanks to Fatt_Shade for the Dark Commander errors!
    ^ Glory's Leadership Reduction Requirement no longer applies to Undead since it is in the Paladin tree.
    ^ Ranged Specialist - Leadership Reduction values are now -2, -5, and -10% (was -5, -10, and -15%).
    ^ Archmage - Leadership Reduction values are now -2, -5, and -10% (was -5, -10, and -15%).
    ^ Necromancy - Leadership Reduction values are now -2, -5, and -10% (was -5, -10, and -15%)
  & SPECIAL_PARAMS.TXT - commented out the sp_lead_(group) bonuses since they are now longer used
  & SPELLS.TXT - updated mana_cost for a few spells for ARENA.LUA - spell_auto_cast function that AI uses
  & RINA_BABIES.TXT - made some minor tweaks to some of her babies (Vidomina, Lord (Death) Haart, Isra, Thant, and Finneas).
  & WIFES.TXT - Zombie Rina didn't have Black Knights in her Undead sp_lead_unit bonuses.
  & XEONA_BABIES.TXT - fixed an error with Dace - thanks to Fatt_Shade for finding this!
* mod_tougher_eheroes.kfs
  & 276213879.hero - error in Martin Vodash's attack value (was 5 should have been 8)

Version: Alpha 2011-11-19
-------------------------

Fixes:

* LOGIC_HERO.LUA had an error in it where for Easy and Normal difficulty level, the level up didn't work correctly.

Thanks to erkki (Erkilmarl) for helping find and fix this bug!

Changes:

* Updated Sleem's Cloud of Poison such that the early levels mana increase is less and for the 2nd upgrade you need Sleem to be higher level to get it.
  & I recently updated Sleem's Cloud of Poison before restarting my new game and as I played the previous values didn't feel right.

Additions:

* I've added the en_ language files for those users of the game with the alternate English locality files.

Version: Alpha 2011-11-13
-------------------------

Crash Fixes:

* Rina had a mispelling in one of her child names in wifes.txt. This would cause a crash to desktop when Rina was having a baby.

Version: Alpha 2011-11-11
-------------------------

This archive contains all the files for the HOMM3 Babies mod / micro / mini expansion pack for King's Bounty: The Legend. This work will be referred to loosely as the mod in the rest of this document.

There are many changes to the game, but at this time I do not have them listed here. In the future, this file will list those changes. In the mean time, visit the YouTube video page: http://youtu.be/JE0VbSnfYkM and the King's Bounty: The Legend Mod forum for more information: http://forum.1cpublishing.eu/showthread.php?p=360731#post360731.

Installation:
-------------

1. This mod is not compatible with any other mods since I've most likely modified a file that another mod uses.
  a. You will need to remove all mods from your King's Bounty: The Legend "mods" folder before installation of this mod.
  b. Ensure that the "mods" folder exists, it is typically located here: C:\Program Files (x86)\1C Company\King's Bounty\data\mods
    i. If the "mods" folder does not exist then create it below the "data" folder using the path above as a guide.
2. Extract the 4 *.KFS files included in this archive to the King's Bounty: The Legend folder.
  a. This folder is typically here: C:\Program Files (x86)\1C Company\King's Bounty\data\mods
  b. If the "mods" folder does not exist, then see note 1ai above.
  c. The 4 KFS files are:
    i.   mod_homm3_portraits.kfs - stand alone game picture resources containing all *.DAT and *.DDS files that may be used in other mods.
    ii.  mod_tougher_eheroes.kfs - stand alone tougher heroes containing all *.HERO files that may be used in other mods.
    iii. mod_homm3_babies.kfs - core HOMM3 babies mod files containing all *.ACT, *.ATOM, *.CHAT, *.LUA, and *.TXT files modified for this mod.
    iv.  mod_homm3_babies_eng_lng.kfs ***OR*** mod_homm3_babies_en_lng.kfs - updated *.LNG files
      1) Use mod_homm3_babies_eng_lng.kfs for your English localization with eng_*.lng
      2) Use mod_homm3_babies_en_lung.kfs for your English localization with en_*.lng
      3) DO NOT USE BOTH FILES!!! Just one or the other!!!
  d. All 4 KFS files are needed for the complete HOMM3 babies mod experience!
3. Run the game
  a. Start a new game to play!
  b. It is not recommended to continue your current game, please restart.
  c. For your first play through:
    i.   Please do not use any cheats (i.e. Save Game Scanner, etc.)
    ii.  Please do not use with any other mods (probably won't work anyway)
    iii. You'll be able to experience the mod as I intended it to be played.

Uninstallation:
---------------

1. Simply delete the 3 KFS files from your "mods" folder:
  a. mod_homm3_portraits.kfs
  b. mod_tougher_eheroes.kfs
  c. mod_homm3_babies.kfs
2. Done!

Notes:
------

1. This mod was developed using the Gamer's Gate V1.7 version of King's Bounty: The Legend.
2. I have not tried it with other versions.
3. This mod uses the English localizations using the "eng_" prefix for the localization files.
  a. Other versions may have other prefixes and so you may be able to get this mod to work with your localization version by changing the prefixes of the *.LNG localization files.
    i.   The *.LNG files are located inside mod_homm3_babies.kfs.
    ii.  Simply rename mod_homm3_babies.kfs to mod_homm3_babies.zip and extract files if you wish to attempt this.
    iii. Currently, you're on your own if you want to get it to work with a different localization, but if you'd like to help with localizations in your country then please let me know.
  b. In the future I hope to be able to have feedback from users to help me with the different English localization variants.

Issues / Bugs:
--------------

Since this is an alpha release of this mod, it is quite possible that your game with crash or you'll find bugs in this mod. Please provide me feedback on any issues that you are having with my mod so that I can make improvements and make your playing experience more enjoyable.

If you have any problems during play, here are some pointers:

1. If it is a game crash, note which action caused the crash.
2. If the game appears to lock up, ALT-TAB back to Windows to see if there is a pop-up.
  a. If there is a pop-up window, note the message and then click OK to proceed.
  b. After you click OK, the game will most likely crash exit to Windows.
  c. If the game does not crash after you click OK, it is highly recommended to quit your game rather than continue since behavior may be strange.
3. Save your game often just in case!
4. If the game crashes right after a battle and you've asked your wife for children then it is due to a spelling error in one of that wife's children.
  a. I just ran into this problem where I had a mispelling in one of Rina's children.

Crash List
----------

1. I've had crashes with a failure to allocate more memory a couple of times.
  a. The solution is to reload your most recent save game and simply continue.
  b. Let me know if you see this problem, but currently I have no idea how to resolve it (I probably would need 1CC or Katauri Interactive's help with this one).

Bug List - there is one bug that I'm not sure if I've squished or not:
--------

1. If you notice that your (or the enemy) units start doing damage in the 100,000's then let me know.
  a. I think this bug may be related to the resurrection of the Phoenix, but I'm not sure.
  b. I've only seen this bug twice in all my play throughs, but it is exhibited during combat.
  c. It typically happens after many rounds and I have not been able to remember all my moves to repeat this bug and debug it.
  d. If you are able to provide a save game with the exact sequence to get this bug to appear then I'll be able to debug it.
2. Damage causing effects (i.e. burning and poison):
  a. If an AI unit is killed by a damage causing effect and if the next unit to move is another AI unit, then their damage causing effect is skipped if they have one.
  b. I worked and worked trying to fix this bug, but to no avail.
    i.  I'm pretty sure that it is a bug with the game itself as I don't think they intended for damaging effects to kill units.
    ii. As such, I don't know how to fix this bug, but if you have any ideas then please let me know!

If you notice any other problems or issues, then please let me know!

It is my intent to make this mod as bug free and enjoyable as possible!

Updates:
--------

1. As this version of the mod is in an alpha state, there are still changes that are being done; however:
  a. The mod is stable enough to play the game completely through - enjoy!
  b. Every change has been checked at least once, but I'm in the quality assurance phase rechecking the code.
  c. I'm about to start a new Paladin game to check gameplay some more.
2. At this stage, changes should not require you to restart your game - simply install the new files and continue playing.
3. Updates will most likely occur on a bi-monthly basis depending on severity and other factors.
4. Once the quality assurance phase is completed and sufficient feedback is garnered, the project will transition to the beta release phase.
5. The beta release phase will have all features properly implemented and all controllable bugs fixed.
  a. Changes will be focused on editing data files (i.e. *.ATOM, *.TXT) to improve game balance and user enjoyability.
  b. Once the beta phase has garnered sufficient feedback, the project will transition to the official release phase - more information on that once the beta phase is reached.

Modders:
--------

1. I've made many changes under the hood that only modders or code aficionados would notice.
2. I've added comments where warranted to the areas in the game that I've changed.
  a. Feel free to look at these comments and provide me feedback if you know of a better way to implement something.
  b. Certain comments have the word "HACK" where I did not know how to do it a better way - once again if you know a better way to implement this feature then please let me know!
3. I've unified many *.LUA functions (i.e. like SPELLS_POWER.LUA) so that they all use the same bonus system, etc.
4. I've made common functions for dealing with redundant code.
  a. The original *.LUA files had lots and lots of redundant code.
  b. I've replaced most of the redundant code in the *.LUA functions I've edited to reduce error and provide code consistency.
5. I've beautified the sections of the *.LUA files I've changed to make reading the code much, much easier.
6. The changes I've made really form the basis of a new code base from which you can create new mods.

Copyright Issues:
-----------------

1. This work contains images from the Heroes of Might and Magic 3 game and those images are copyrighted.
2. The picture for Orcelyn Ordy I found via the web, but I have not been able to find out who created that source image.
  a. If you have any information about who created this picture please let me know and I'll give credit to the author.
3. I created all the new ability icons.
4. All of my effort is being freely distributed to the public domain.
  a. Please give me credit if you use any portion of my work in your projects - thanks! :-)
  b. Feel free to use this code base as a starting point for your own mod!

THANK YOU!!!
------------

1. Thanks to all the people posting in the King's Bounty forums, especially those with modding tips!
2. Thanks for trying out my mod and providing feedback!

/C\/C\ Matt Caspermeyer

---
## [Matt-Caspermeyer/H3B](https://github.com/Matt-Caspermeyer/H3B)@[8d382437e0...](https://github.com/Matt-Caspermeyer/H3B/commit/8d382437e01eadf4b42259c7d72b0d6ad0a7f3f7)
#### Sunday 2023-11-26 19:54:54 by Matt-Caspermeyer

Alpha Release 2011-11-25

Heroes of Might and Magic 3 Babies (HOMM3 Babies) Mod / Micro / Mini Expansion Pack for King's Bounty: The Legend
-----------------------------------------------------------------------------------------------------------------

Created by: Matt Caspermeyer (matt.caspermeyer@cox.net)
-------------------------------------------------------

You are free to use any part of my work in your projects so long as you give me credit.

Version: Alpha 2011-11-25
-------------------------

Updates:

* mod_homm3_babies.kfs
  & UNIT_FEATURES.LUA
    ^ Fixed the massive damage bug in the implementation of one of the Enchanted Hero spell casts.
    ^ Removed that from the bugs list below.
    ^ This is a *HUGE* buxfix and I've been trying to track this down for months and finally found it - yay!
  & SPELLS.TXT - fixed Enchanted Hero so it cannot be cast on the Undead or Plants
  & WIFES.TXT - fixed Mirabella's missing Griffin morale bonus - thanks Fatt_Shade!

Version: Alpha 2011-11-23
-------------------------

Updates:

* New KFS Organization - *.LNG files are in their own KFS (ZIP)
  & mod_homm3_babies_eng_lng.kfs - contains the ENG_*.LNG English Language Localization files
  & mod_homm3_babies_en_lng.kfs - contains the EN_*.LNG English Language Localization files
  & The files are collectively refered to as mod_homm3_babies_en(g)_lng.kfs.
* mod_homm3_babies_en(g)_lng.kfs (this refers to both KFS *.LNG files)
  & EN(G)_SPELLS.LNG - fixed a few spells descriptions that were incorrect
  & EN(G)_HOMM3_BABIES_RINA.LNG - updated baby descriptors for Vidomina, Lord (Death) Haart, Isra, Thant, and Finneas.
  & EN(G)_SKILLS.LNG - updated Glory skill description
* mod_homm3_babies.kfs
  & NECROMANT.ATOM - experimental change making all 3 of the Necromancer's skills reloadable (kind of more like the Human Archmage).
  & TEMPLATES.LNG - removed Necro Call bonus for Necromancy Skill Template
  & SKILLS.LUA - commented out the sp_lead_unit bonuses for all Undead units
  & SPELLS.LUA - code cleanup
  & SKILLS.TXT
    ^ Corrected a few skill values - thanks to Fatt_Shade for the Dark Commander errors!
    ^ Glory's Leadership Reduction Requirement no longer applies to Undead since it is in the Paladin tree.
    ^ Ranged Specialist - Leadership Reduction values are now -2, -5, and -10% (was -5, -10, and -15%).
    ^ Archmage - Leadership Reduction values are now -2, -5, and -10% (was -5, -10, and -15%).
    ^ Necromancy - Leadership Reduction values are now -2, -5, and -10% (was -5, -10, and -15%)
  & SPECIAL_PARAMS.TXT - commented out the sp_lead_(group) bonuses since they are now longer used
  & SPELLS.TXT - updated mana_cost for a few spells for ARENA.LUA - spell_auto_cast function that AI uses
  & RINA_BABIES.TXT - made some minor tweaks to some of her babies (Vidomina, Lord (Death) Haart, Isra, Thant, and Finneas).
  & WIFES.TXT - Zombie Rina didn't have Black Knights in her Undead sp_lead_unit bonuses.
  & XEONA_BABIES.TXT - fixed an error with Dace - thanks to Fatt_Shade for finding this!
* mod_tougher_eheroes.kfs
  & 276213879.hero - error in Martin Vodash's attack value (was 5 should have been 8)

Version: Alpha 2011-11-19
-------------------------

Fixes:

* LOGIC_HERO.LUA had an error in it where for Easy and Normal difficulty level, the level up didn't work correctly.

Thanks to erkki (Erkilmarl) for helping find and fix this bug!

Changes:

* Updated Sleem's Cloud of Poison such that the early levels mana increase is less and for the 2nd upgrade you need Sleem to be higher level to get it.
  & I recently updated Sleem's Cloud of Poison before restarting my new game and as I played the previous values didn't feel right.

Additions:

* I've added the en_ language files for those users of the game with the alternate English locality files.

Version: Alpha 2011-11-13
-------------------------

Crash Fixes:

* Rina had a mispelling in one of her child names in wifes.txt. This would cause a crash to desktop when Rina was having a baby.

Version: Alpha 2011-11-11
-------------------------

This archive contains all the files for the HOMM3 Babies mod / micro / mini expansion pack for King's Bounty: The Legend. This work will be referred to loosely as the mod in the rest of this document.

There are many changes to the game, but at this time I do not have them listed here. In the future, this file will list those changes. In the mean time, visit the YouTube video page: http://youtu.be/JE0VbSnfYkM and the King's Bounty: The Legend Mod forum for more information: http://forum.1cpublishing.eu/showthread.php?p=360731#post360731.

Installation:
-------------

1. This mod is not compatible with any other mods since I've most likely modified a file that another mod uses.
  a. You will need to remove all mods from your King's Bounty: The Legend "mods" folder before installation of this mod.
  b. Ensure that the "mods" folder exists, it is typically located here: C:\Program Files (x86)\1C Company\King's Bounty\data\mods
    i. If the "mods" folder does not exist then create it below the "data" folder using the path above as a guide.
2. Extract the 4 *.KFS files included in this archive to the King's Bounty: The Legend folder.
  a. This folder is typically here: C:\Program Files (x86)\1C Company\King's Bounty\data\mods
  b. If the "mods" folder does not exist, then see note 1ai above.
  c. The 4 KFS files are:
    i.   mod_homm3_portraits.kfs - stand alone game picture resources containing all *.DAT and *.DDS files that may be used in other mods.
    ii.  mod_tougher_eheroes.kfs - stand alone tougher heroes containing all *.HERO files that may be used in other mods.
    iii. mod_homm3_babies.kfs - core HOMM3 babies mod files containing all *.ACT, *.ATOM, *.CHAT, *.LUA, and *.TXT files modified for this mod.
    iv.  mod_homm3_babies_eng_lng.kfs ***OR*** mod_homm3_babies_en_lng.kfs - updated *.LNG files
      1) Use mod_homm3_babies_eng_lng.kfs for your English localization with eng_*.lng
      2) Use mod_homm3_babies_en_lung.kfs for your English localization with en_*.lng
      3) DO NOT USE BOTH FILES!!! Just one or the other!!!
  d. All 4 KFS files are needed for the complete HOMM3 babies mod experience!
3. Run the game
  a. Start a new game to play!
  b. It is not recommended to continue your current game, please restart.
  c. For your first play through:
    i.   Please do not use any cheats (i.e. Save Game Scanner, etc.)
    ii.  Please do not use with any other mods (probably won't work anyway)
    iii. You'll be able to experience the mod as I intended it to be played.

Uninstallation:
---------------

1. Simply delete the 3 KFS files from your "mods" folder:
  a. mod_homm3_portraits.kfs
  b. mod_tougher_eheroes.kfs
  c. mod_homm3_babies.kfs
2. Done!

Notes:
------

1. This mod was developed using the Gamer's Gate V1.7 version of King's Bounty: The Legend.
2. I have not tried it with other versions.
3. This mod uses the English localizations using the "eng_" prefix for the localization files.
  a. Other versions may have other prefixes and so you may be able to get this mod to work with your localization version by changing the prefixes of the *.LNG localization files.
    i.   The *.LNG files are located inside mod_homm3_babies.kfs.
    ii.  Simply rename mod_homm3_babies.kfs to mod_homm3_babies.zip and extract files if you wish to attempt this.
    iii. Currently, you're on your own if you want to get it to work with a different localization, but if you'd like to help with localizations in your country then please let me know.
  b. In the future I hope to be able to have feedback from users to help me with the different English localization variants.

Issues / Bugs:
--------------

Since this is an alpha release of this mod, it is quite possible that your game with crash or you'll find bugs in this mod. Please provide me feedback on any issues that you are having with my mod so that I can make improvements and make your playing experience more enjoyable.

If you have any problems during play, here are some pointers:

1. If it is a game crash, note which action caused the crash.
2. If the game appears to lock up, ALT-TAB back to Windows to see if there is a pop-up.
  a. If there is a pop-up window, note the message and then click OK to proceed.
  b. After you click OK, the game will most likely crash exit to Windows.
  c. If the game does not crash after you click OK, it is highly recommended to quit your game rather than continue since behavior may be strange.
3. Save your game often just in case!
4. If the game crashes right after a battle and you've asked your wife for children then it is due to a spelling error in one of that wife's children.
  a. I just ran into this problem where I had a mispelling in one of Rina's children.

Crash List
----------

1. I've had crashes with a failure to allocate more memory a couple of times.
  a. The solution is to reload your most recent save game and simply continue.
  b. Let me know if you see this problem, but currently I have no idea how to resolve it (I probably would need 1CC or Katauri Interactive's help with this one).

Bug List - there is one bug that I'm not sure if I've squished or not:
--------

1. Damage causing effects (i.e. burning and poison):
  a. If an AI unit is killed by a damage causing effect and if the next unit to move is another AI unit, then their damage causing effect is skipped if they have one.
  b. I worked and worked trying to fix this bug, but to no avail.
    i.  I'm pretty sure that it is a bug with the game itself as I don't think they intended for damaging effects to kill units.
    ii. As such, I don't know how to fix this bug, but if you have any ideas then please let me know!

If you notice any other problems or issues, then please let me know!

It is my intent to make this mod as bug free and enjoyable as possible!

Updates:
--------

1. As this version of the mod is in an alpha state, there are still changes that are being done; however:
  a. The mod is stable enough to play the game completely through - enjoy!
  b. Every change has been checked at least once, but I'm in the quality assurance phase rechecking the code.
  c. I'm about to start a new Paladin game to check gameplay some more.
2. At this stage, changes should not require you to restart your game - simply install the new files and continue playing.
3. Updates will most likely occur on a bi-monthly basis depending on severity and other factors.
4. Once the quality assurance phase is completed and sufficient feedback is garnered, the project will transition to the beta release phase.
5. The beta release phase will have all features properly implemented and all controllable bugs fixed.
  a. Changes will be focused on editing data files (i.e. *.ATOM, *.TXT) to improve game balance and user enjoyability.
  b. Once the beta phase has garnered sufficient feedback, the project will transition to the official release phase - more information on that once the beta phase is reached.

Modders:
--------

1. I've made many changes under the hood that only modders or code aficionados would notice.
2. I've added comments where warranted to the areas in the game that I've changed.
  a. Feel free to look at these comments and provide me feedback if you know of a better way to implement something.
  b. Certain comments have the word "HACK" where I did not know how to do it a better way - once again if you know a better way to implement this feature then please let me know!
3. I've unified many *.LUA functions (i.e. like SPELLS_POWER.LUA) so that they all use the same bonus system, etc.
4. I've made common functions for dealing with redundant code.
  a. The original *.LUA files had lots and lots of redundant code.
  b. I've replaced most of the redundant code in the *.LUA functions I've edited to reduce error and provide code consistency.
5. I've beautified the sections of the *.LUA files I've changed to make reading the code much, much easier.
6. The changes I've made really form the basis of a new code base from which you can create new mods.

Copyright Issues:
-----------------

1. This work contains images from the Heroes of Might and Magic 3 game and those images are copyrighted.
2. The picture for Orcelyn Ordy I found via the web, but I have not been able to find out who created that source image.
  a. If you have any information about who created this picture please let me know and I'll give credit to the author.
3. I created all the new ability icons.
4. All of my effort is being freely distributed to the public domain.
  a. Please give me credit if you use any portion of my work in your projects - thanks! :-)
  b. Feel free to use this code base as a starting point for your own mod!

THANK YOU!!!
------------

1. Thanks to all the people posting in the King's Bounty forums, especially those with modding tips!
2. Thanks for trying out my mod and providing feedback!

/C\/C\ Matt Caspermeyer

---
## [norbert-acedanski/supernatural-guide](https://github.com/norbert-acedanski/supernatural-guide)@[a3aeaa85bc...](https://github.com/norbert-acedanski/supernatural-guide/commit/a3aeaa85bc0f77f8e7edc6d722eaf4a77cf2bc5d)
#### Sunday 2023-11-26 20:16:17 by Norbert Acedanski

Add Vengeful spirit encounter.
Add Demon, Witch, Angel, Darkness appearances.
Add GOD disable method.
Update Ghost Kevin description.
S15E02

---
## [gabriel-emanuel/MSAAI-501-Final](https://github.com/gabriel-emanuel/MSAAI-501-Final)@[c8c0ab037c...](https://github.com/gabriel-emanuel/MSAAI-501-Final/commit/c8c0ab037c52c03f77f00501a04de1f84334a61a)
#### Sunday 2023-11-26 20:30:34 by ParChristUSD

Added Files 

the folder with the 'Formatted' Extention is for us to use for testing, gabes pics came out amazing, Mine and my girlfriends did not come out looking to good, so we should test the model on both good and bad pictures.

---
## [LumberKing/Tianxia](https://github.com/LumberKing/Tianxia)@[354bcd86e1...](https://github.com/LumberKing/Tianxia/commit/354bcd86e1ac6c16b1e8450cd1949320820adfe3)
#### Sunday 2023-11-26 20:31:42 by Silversweeper

Get Out Of Jail Free Card, misc

- Added CoAs for all CI empires named "Empire of the [Element] [Zodiac]".
- Ported remaining custom loc setup from the old Tianxia remnant.
- Ported burnination opinion modifier.
- The EoC will now consider being an unfilial descendant cause to refuse some Grace-related things.
- Improved custom loc setup.
- Loc for and fixes to council voting.
- The Tenno now has an unlimited supply of Get Out Of Jail Free cards and diplomatic_immunity = yes, though only if his liege or jailer (as appropriate) should care.
- If the Tenno is the primary participant in a war and gets imprisoned by the other side, the Get Out Of Jail Free Card is slightly less free, coming with a "The Tenno first surrenders" clause.
- Added a workaround to handle the AI EoC (and potentially other CI rulers) going way above his demesne limit and staying there for no good reason, making China less prone to imploding due to AI insanity.
- Dynasty members of CI rulers and the Tenno should no longer wind up in silly courts when starting a new game.
- Custom loc improvements.
- Added a bunch of missing loc tags related to custom loc.
- Took care of a bunch of scripted_trigger and _effect leftovers.
- Misc smaller fixes.

---
## [sjp38/linux](https://github.com/sjp38/linux)@[e227c9abc3...](https://github.com/sjp38/linux/commit/e227c9abc3d5599b48259701d353364b55fed101)
#### Sunday 2023-11-26 20:33:48 by SeongJae Park

==== DAMOS: Introduce Aim-Oriented Feedback-driven Quota Auto Tuning ====

Subject: [PATCH] mm/damon: Let users feed and tame DAMOS

Introduce a new way for tuning DAMOS, namely aim-oriented
feedback-friven quota auto tuning.  It allows users to specify their aim
of their DAMOS usage, and continuously inform DAMOS how well it is
following the aim.  Based on the goals and the feedback, DAMOS adjusts
its aggressiveness on its own.

DAMOS Control Difficulty
========================

DAMOS helps users easily implementing effective access pattern aware
system operations.  However, controlling DAMOS in wild is not that easy.

The basic way to control DAMON is specifying the target access pattern.
In this approach, the user is assumed to know the access pattern of the
system and the workloads well.  Though some good tools including DAMON
can help that, it requires time and resource, and the cost depends on
the complexity and the dynamicity of the system and workloads.  After
all, the access pattern consists of three ranges, namely access rate,
age, and size of the regions.  It means the user needs to tune six
parameters.  Tuning six parameters is anyway not simple.  It is not
doable for everyone.

To ease the control, DAMOS allows users to set the upper-limit of the
schemes's aggressiveness, namely DAMOS quota.  Then DAMOS prioritizes
regions to apply the action under the limit based on the action and the
access pattern of the regions.  For example, users can ask DAMOS to page
out up to 100 MiB of memory regions per second.  Then DAMOS pages out
regions that not accessed for longer time first under the limit.  This
allows users to set access pattern bit more naively, and focus on only
the one parameter, the quota.  In other words, the number of parameters
to tune with special care can be reduced from six to one.

Still, however, the optimal value for the quota depends on the system
and the workloads' characteristics, so not that simple.  The number of
parameters to tune can also increase again if the user needs to run
multiple schemes, e.g., collapsing hot pages into THP while splitting
cold pages into regular pages.

In short, the existing approaches ask users to find the perfect or
adapted tuning and instruct DAMOS how to work.  In other words, it
requires users to be deligent.  That's not a virtue of human, but the
machine.

Aim-oriented Feedback-driven DAMOS Quota Auto Tuning
====================================================

Most users would start using DAMOS since there is something they want to
achieve using DAMOS.  The users may have well understanding of such
goals.  Having specific metrics and values like SLO is indeed common.
Hence, users could repeatedly inform DAMOS the goals, and how well DAMOS
is making it with only relatively small effort.  Then DAMOS could
somehow make it.  In other words, users provide feedback for each DAMOS
scheme.  DAMOS then tune the quota of each scheme based on the users'
feedback and the current quota values.

This patchset implements the idea.

Implementation
--------------

The core logic implementation is in the first patch.  In short, it uses
below simple feedback loop algorithm to get next aggressiveness from the
current aggressiveness and the feedback (target_score and current_score)
for the current aggressiveness.

    f(n) = max(1, f(n - 1) * ((target_score - current_score) / target_score + 1))

Note that this algorithm assumes the aggressiveness and the score are
positively proportional.  Making it true is the feedback provider's
responsibility.

Test Results
------------

To show if this provides the expected benefit, we prepare four different
system setup on AWS i3.metal instance.  The first setup (original) runs
the workload without any DAMOS scheme.  The second setup (not-tuned)
runs the workload with virtual address space-based proactive reclamation
scheme that pages out memory regions that not accessed for five seconds
or more.  The third setup (offline-tuned) runs the same proactive
reclamation DAMOS scheme, but after making it tuned for each workload in
offline, using our previous user-space driven automatic tuning approach,
namely DAMOOS[1].  The fourth and final setup (online-tuned) runs the
same scheme, but making DAMOS to do online auto-tuning, aiming 0.5% of
'some' memory pressure stall time per 10 seconds.

For each setup, we run realistic workloads from PARSEC3 and SPLASH-2X
benchmark suites.  For each run, we measure RSS and runtime of the
workload, and 'some' memory pressure stall time (PSI) of the system.
We repeat the runs five times and use averaged measrements.

For each comparison of the schemes, we normalize the measurements to
those of 'original'.  In case of the PSI, that for 'original' was zero,
so we normalize the value to that of 'not-tuned' scheme's result.  The
normalized results are shown below.

            Not-tuned         Offline-tuned     Online-tuned
    RSS     0.622688178226118 0.787950678944904 0.740093483278979
    runtime 1.11767826657912  1.0564674983585   1.0910833880499
    PSI     1                 0.727521443794069 0.308498846350299

The 'not-tuned' scheme acheives about 38.7% memory saving but incur about
11.7% runtime slowdown.  The offline-tuned scheme achieves about 22.2%
memory saving with about 5.5% runtiem slowdown.  It also achieves about
28.2% PSI saving.  The online-tuned scheme achieves about 26% memory
saving with about 9.1% runtime slowdown.  It also achieves about 69.1%
PSI saving.  We continued this test multiple times, and consistently got
similar results.

So, online-tuned version is showing worst memory saving and second
performance degradation among the three variants.  However, the
difference is not significant.  Also, it shows significant PSI saving,
which was the goal of the tuning.  Hence, we conclude the automatic
tuning is working as expected.

The test code is available[2], so you can reproduce on your system.

[1] https://www.amazon.science/publications/daos-data-access-aware-operating-system
[2] https://github.com/damonitor/damon-tests/commit/3f884e61193f0166b8724554b6d06b0c449a712d

Patches Sequence
================

The first four patches implement the core logic and user interfaces for
the auto tuning.  The first patch implements the core logic for the auto
tuning, and the API for DAMOS users in the kernel space.  The second
patch implements basic file operations of DAMON sysfs directories and
files that will be used for setting the goals and providing the
feedback.  The third patch connects the quota goals files inputs to the
DAMOS core logic.  Finally the fourth patch implements a dedicated DAMOS
sysfs command for efficiently committing the quota goals feedback.

Two patches for simple test of the logic and interfaces follow.  The
fifth patch implements the core logic unit test.  The sixth patch
implements a selftest for the DAMON Sysfs interface for the goals.

Finally, two patches for documentation follows.  The seventh patch
documents the design of the feature.  The final eighth patch updates the
usage document for the features.

Signed-off-by: SeongJae Park <sj@kernel.org>

---
## [maniwani/bevy](https://github.com/maniwani/bevy)@[ab300d0ed9...](https://github.com/maniwani/bevy/commit/ab300d0ed9990972679629af3ef18fd37c0e106c)
#### Sunday 2023-11-26 20:52:13 by Connor King

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
## [pranatijena/personal-friend](https://github.com/pranatijena/personal-friend)@[a3a3c64a98...](https://github.com/pranatijena/personal-friend/commit/a3a3c64a9886aa164eff704331b7cdff9e6732a0)
#### Sunday 2023-11-26 21:01:58 by Pranati jena

Create README.md

*Introduction* Welcome to "MyLifeDiary," a unique blogging platform designed as a personal diary where users can share their life experiences, thoughts, and emotions in a private and secure environment. MyLifeDiary serves as a confidant, allowing users to express themselves freely while also functioning as a public blogging space. With a focus on privacy and user control, MyLifeDiary provides a seamless blend of personal journaling and public blogging. *Features* 1. *Personal Diary Features:* - *My Personal Friend:* This section allows users to maintain lists of their wishes, problems, family members' details, next steps, needs, and complaints. Users can add important contacts, complete with names, relations, mobile numbers, and occupations, creating a trusted network of confidants. - *Wish Lists:* Users can add products from Flipkart and Amazon, including product details and prices, helping them keep track of desired items. - *Private Conversations:* Users can chat and talk with the website owner and three important persons they've designated, fostering intimate connections and support. - *Confidential Entries:* Every section features bullet points and note spaces, ensuring users can jot down their thoughts in a structured manner. 2. *Privacy Controls:* - *Selective Sharing:* Users can choose to share specific diary entries with their three designated important persons, ensuring privacy while allowing for personal connections. - *Confidentiality:* All diary entries are private by default, visible only to the user and the website owner. Users have complete control over their shared content. 3. *Blogging Platform:* - *Home Page:* Displays a list of all public blog posts, including titles and authors, accessible to everyone. Users can click on a post to view details or add comments. - *New Post Page:* Accessible to logged-in users, this page features a form for creating new blog posts, enhancing the public blogging experience. - *Edit Post Page:* Accessible only by the post owner, this page allows editing of specific posts, maintaining control over shared content. - *View Post Page:* Accessible to all users, this page showcases post details, including title, author, content, and comments. Logged-in users can add new comments, fostering community engagement. *Navigation* - *Home, About, and Contact:* Standard navigation options enable users to explore the platform easily. MyLifeDiary stands as a testament to the power of expression, offering a secure space for personal reflection and a vibrant community for public discourse. With a user-centric design, robust privacy features, and seamless navigation, MyLifeDiary redefines online journaling and blogging, catering to the diverse needs of its users.

---
## [kikuyodev/kumi-web](https://github.com/kikuyodev/kumi-web)@[d34e55bae3...](https://github.com/kikuyodev/kumi-web/commit/d34e55bae3b253e4885dbb6be6628428928c1690)
#### Sunday 2023-11-26 21:36:39 by ryoshu

fix stupid little bitch ass fucking account navbar flyout

Co-authored-by: Furina <irisu01@users.noreply.github.com>

---
## [ayatweb/react](https://github.com/ayatweb/react)@[1ebedbec2b...](https://github.com/ayatweb/react/commit/1ebedbec2bec08e07c286ea6c3cff62737a0fd3a)
#### Sunday 2023-11-26 21:46:19 by Sebastian Markbåge

Add Server Context deprecation warning (#27424)

As agreed, we're removing Server Context. This was never official
documented.

We've found that it's not that useful in practice. Often the better
options are:

- Read things off the url or global scope like params or cookies.
- Use the module system for global dependency injection.
- Use `React.cache()` to dedupe multiple things instead of computing
once and passing down.

There are still legit use cases for Server Context but you have to be
very careful not to pass any large data, so in generally we recommend
against it anyway.

Yes, prop drilling is annoying but it's not impossible for the cases
this is needed. I would personally always pick it over Server Context
anyway.

Semantically, Server Context also blocks object deduping due to how it
plays out with Server Components that can't be deduped. This is much
more important feature.

Since it's already in canary along with the rest of RSC, we're adding a
warning for a few versions before removing completely to help migration.

---------

Co-authored-by: Josh Story <josh.c.story@gmail.com>

---
## [Zorgusn/terminalSpreadsheet](https://github.com/Zorgusn/terminalSpreadsheet)@[ce19658a14...](https://github.com/Zorgusn/terminalSpreadsheet/commit/ce19658a14b0ab86a12df4fb373bfa358e96cb2a)
#### Sunday 2023-11-26 23:16:24 by Hudson S

interface working except for the fucking references god damn it what the fuck

---
## [zahidaz/webarchives](https://github.com/zahidaz/webarchives)@[c4f0e64c15...](https://github.com/zahidaz/webarchives/commit/c4f0e64c15599810b605a87060d6120918419fe7)
#### Sunday 2023-11-26 23:20:34 by zahidaz

IANA Report on Redelegation of the .af Top-Level Domain

https://www.iana.org/reports/2003/af-report-08jan2003.html


Subject:	Request of Islamic Transitional Government of Afghanistan for Redelegation of the .af Top-Level Domain
Date:	8 January 2003
The Internet Assigned Numbers Authority (the IANA), as part of the administrative functions associated with management of the domain-name system root, is responsible for receiving requests for delegation and redelegation of top-level domains, investigating the circumstances pertinent to those requests, and reporting on the requests. On 10 September 2002, the IANA received a request for redelegation of the .af (Afghanistan) country-code top-level domain (ccTLD). This report gives the findings and conclusions of the IANA on its investigation of that request.

Factual and Procedural Background

The .af ccTLD registry was first delegated by the IANA in October 1997 to Mr. Abdul Razeeq of Kabul as administrative contact and Hostmaster, NetNames of London as technical contact.

By arrangement with the IANA, NetNames agreed to perform the technical functions and to provide a free registration service for .af on a temporary basis, until a stable registry operation could be established within Afghanistan.

In the late 1990s, the ongoing civil war in Afghanistan made Mr. Razeeq's role as administrative contact increasingly difficult. In light of the situation inside Afghanistan, NetNames, in consultation with the IANA, halted the registration of new domain names in the .af registry, while agreeing to continue to make nameserver updates and to provide DNS resolution for the .af zone.

By early 2000, however, it had become impossible for NetNames or the IANA to contact Mr. Razeeq. Despite numerous attempts by e-mail, telephone, and postal mail over a sustained period of time, the IANA was unable to confirm whether or not Mr. Razeeq was still inside Afghanistan or, for that matter, alive. At the time, the ongoing civil war made communications into Afghanistan extremely difficult. In August 2001, the Taliban, the then-ruling regime, formally prohibited all non-governmental Internet use inside the country.

On 13 November 2001, the Taliban military forces deserted Kabul, Afghanistan's capital. After United Nations-sponsored talks in Bonn, Germany, among Afghan groups opposing the Taliban, an Interim Authority was established on 22 December 2001. On 31 December 2001, the IANA was contacted by Mr. Lawrence Yeung, Chief of the Office of Information Systems and Technology of the United Nations Development Programme (UNDP), which had been charged by the United Nations to assist the Interim Authority of Afghanistan. Mr. Yeung stated that, with the approval of the Afghan Interim Authority, the UNDP would undertake to assume the administration of the .af registry. There is a near-total absence of a local Internet community within Afghanistan – at the time of Mr. Yeung’s inquiry, only a few Internet links had been established in Kabul by international organizations and NGOs. The IANA was, however, rapidly able to confirm that the UNDP had the full backing of the Interim Authority to restore the .af registry to active status and to perform all necessary technical functions, with the understanding that the UNDP's role would be transitional and temporary. The UNDP agreed that its role would be to restore DNS service, to build technical and administrative capacity within Afghanistan, and to shift technical operations to a community-based management structure inclusive of multiple sectors within Afghanistan when feasible and appropriate.

Over the following months, the IANA worked with UNDP staff to explain the technical and administrative requirements for a ccTLD registry, and to prepare the necessary technical, administrative, and policy arrangements.

In June 2002, the Islamic Transitional Government of Afghanistan assumed governmental responsibility from the Interim Authority. On 10 September 2002, the Minister of Communications of the Islamic Transitional Government of Afghanistan and the UNDP jointly communicated to the IANA a package of redelegation documents, including:

a cover letter (dated 10 August 2002) from Mohammad Masoom Stanekzai, Minister of Communications of the Islamic Transitional Government of Afghanistan;
a description of the Afghan Internet community, and the government's plans to achieve Internet access;
technical documentation;
a vision for the .af ccTLD, including agreed plans for registry administration and registration policies; and
a signed letter from Mr. Abdul Razeeq, the original administrative contact, agreeing with the proposed redelegation.
By accompanying template, the redelegation request proposed to change the sponsoring organization to the Ministry of Communications, the administrative contact to the Minister of Communications, and the technical contact to Mr. Marc Lepage of the UNDP, with the UNDP maintaining the authoritative nameservers and registration website for .af on the interim basis described above.

The proposal specified that the .af registry would have an oversight committee consisting of the Minister of Communications, the UNDP Afghanistan Country Director, the technical contact (Mr. Lepage), and representatives of the user community. In the submitted documentation, the Ministry and the UNDP have each undertaken to perform a detailed set of administrative and technical responsibilities in service to the emerging Afghan Internet community.

In accord with the proposed interim arrangements, as described above, the Ministry of Communications and the Internet Corporation for Assigned Names and Numbers (ICANN) have agreed on the language of a Memorandum of Understanding providing a framework of accountability under which the Ministry would assume the responsibilities as the delegee entrusted with the .af registry. On 18 November 2002, the ICANN Board of Directors authorized the entry of this Memorandum of Understanding, which closely parallels prior MoUs entered for the .bi, .la, and .mw ccTLDs, with the Ministry.

Evaluation

This report is being provided under the contract for performance of the IANA function between the United States Government and ICANN. Under that contract, ICANN performs the IANA function, which includes receiving delegation and redelegation requests concerning ccTLDs, investigating the circumstances pertinent to those requests, and reporting on the requests.

In acting on redelegation requests, the IANA currently follows the practices summarized in "Internet Domain Name System Structure and Delegation" (ICP-1). ICP-1 represents an update of the portions of RFC 1591 (which was issued in March 1994) dealing with ccTLDs, and reflects subsequent documents and evolution of the policies followed by the IANA through May 1999.

Here, the Ministry of Communications’s request is to shift the delegation from an individual (as the current administrative contact) and the hostmaster at a company in the United Kingdom (as technical contact) to the Ministry itself. The Ministry will initially obtain the technical assistance of UNDP, with the plan later to transfer the technical operations to an appropriate policy-development and management structure that is inclusive of the various segments of the Afghan Internet community.

In considering delegation or redelegation of a ccTLD, the IANA seeks input from persons significantly affected by the transfer, particularly those within the nation or territory which the ccTLD has been established to benefit. As noted in ICP-1, the parties affected include especially the relevant government or public authority: "The desires of the government of a country with regard to delegation of a ccTLD are taken very seriously. The IANA will make them a major consideration in any TLD delegation/transfer discussions." Here, the government’s support is plain, since it has requested the redelegation.

Mutual agreement of the old and new delegees is also a significant factor favoring a redelegation. Here, both present delegees (Abdul Razeeq as administrative contact and Hostmaster, Netnames as technical contact) as well as the proposed new delegee (the Ministry) favor the change in delegation.

The Ministry of Communications appears well-positioned to serve as the delegee responsible for the challenging task of reactivating the .af ccTLD. ccTLDs have been established to facilitate and promote the spread of the Internet globally. They are delegated to designated managers, who operate the ccTLDs according to local policies that are adapted to best meet the economic, cultural, linguistic, and legal circumstances of the country or territory involved. The Ministry is sensitive to the particular circumstances of Afghanistan and has placed a priority on the development of the Internet within Afghanistan as appropriate in the context of those circumstances. As the situation in Afghanistan stabilizes, the Ministry is well-suited to work with the local Internet community as it matures to evolve the .af ccTLD toward a robust, inclusive policy-development and management structure.

The Ministry's proposed technical partner, the UNDP, has an impressive technical infrastructure, including long experience in running DNS services. The UNDP's network spans every kind of Internet environment, from the most advanced to the most rudimentary, from the United Nations headquarters in New York to 166 countries around the globe. Though it is generally preferable for a ccTLD to have its technical operations inside the country or territory, that is not an option for Afghanistan at the moment. As the Ministry of Communications stated in its redelegation request: "After a long period of unrest and destruction, Afghanistan’s infrastructure has been left gravely crippled." At the moment, the appropriate focus is on the restoration of service to the Afghan Internet community, subject to the understanding that technical operations will be shifted into Afghanistan in the future.

The shifting of ccTLD delegations from individuals operating informally as administrative and technical contacts to organizations operating under written agreements or memoranda of understanding is a positive step toward the stable and professional operation of ccTLDs in the public interest. As the Internet becomes increasingly important to global society, a framework of accountability should develop for the operation of all top-level domains, both to promote the global interoperability of the domain-name system and to ensure that the interests of local Internet communities are well-served.

In February 2000, the ICANN Governmental Advisory Committee (GAC) issued a document entitled "Principles for the Delegation and Administration of Country Code Top Level Domains," commonly known as the "GAC Principles." These principles serve as "best practices" to guide governments in assuming proper roles with respect to the Internet's naming system, which the GAC has observed is a public resource to be administered in the public interest. In general, they recognize that each government has the ultimate responsibility within its territory for its national public-policy objectives, but also that ICANN has the responsibility for ensuring that the Internet domain-name system continues to provide an effective and interoperable global naming system.

In entering the MoU and framework of accountability with ICANN, the Ministry of Communications will formally assume responsibility for national public-policy aspects of the .af ccTLD with a commitment to proceeding with openness and service to the local Internet community, while acknowledging the importance of ICANN's role in coordinating an effective and interoperable global domain-name system. Clarification of this allocation of responsibility is an added benefit of the shifting of the delegation to the Ministry.

Conclusion

The IANA concludes that the .af ccTLD should be redelegated, as requested, from the current delegees to the Ministry of Communications of the Islamic Transitional Government of Afghanistan. Mohammad Masoom Stanakzai, in his capacity as Minister of Communications, should become administrative contact and Marc Lepage of the UNDP should become technical contact, as designated by the Ministry of Communications.

---
## [shark-infra/llvm-project](https://github.com/shark-infra/llvm-project)@[5cd24759c4...](https://github.com/shark-infra/llvm-project/commit/5cd24759c41864215e67c280234b6c745a4cd369)
#### Sunday 2023-11-26 23:31:33 by Louis Dionne

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

