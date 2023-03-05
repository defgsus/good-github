## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-03-04](docs/good-messages/2023/2023-03-04.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,834,053 were push events containing 2,588,429 commit messages that amount to 167,342,986 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 48 messages:


## [Technobug14/mojave-sun-14](https://github.com/Technobug14/mojave-sun-14)@[b2f0f35f3a...](https://github.com/Technobug14/mojave-sun-14/commit/b2f0f35f3afe1905cfefcf9e682de51cff2d4499)
#### Saturday 2023-03-04 00:04:54 by EdwardNashton

Speed, Money and Faith: Updating an areas of Town. (#2286)

* Update TGS DMAPI

* Speed, Money and Faith: Updating an areas of Town.

Added a Church with a graveyard area (that currently empty because we have no tombs).

Remade one quarter into 4 different shops: Liquor, Pharmacy, Gun Shop, General Store.

Remade old shitty Library into Biker's Club.

Remade a Dime's Radio Station (by his permission)

Fixed a small area issue on a top z-level of Car Jankyard.

* Fixes up a bunch of stuff :)

* additional minority fixes

---------

Co-authored-by: tgstation-server <tgstation-server@users.noreply.github.com>
Co-authored-by: Edward Nashton <eddienigma48@gmail.com>
Co-authored-by: Professor Popoff <omniderpectional@gmail.com>

---
## [crawl/crawl](https://github.com/crawl/crawl)@[214f356e7e...](https://github.com/crawl/crawl/commit/214f356e7ee7987af1704ebce761d832a0f3f842)
#### Saturday 2023-03-04 00:49:23 by Nicholas Feinberg

Experiment: rework reaching

Polearms have a distinct and tactically useful gimmick, creating
distinct playstyles (e.g. supporting from behind allies). It even
generally works well with autofight ('tab'). However, in the situations
where you have to aim your reach manually, it's quite fiddly. Can we
make reaching work more like other melee attacks without losing
what makes it special?

This commit removes the ability to aim reached attacks at monsters two
spaces away. Instead, attacks are based on the adjacent tile that you're
swinging at or moving into, exactly as with other melee, per these rules:

- If there's an adjacent foe in the direction chosen, hit em.
- Otherwise, if there's a *visible* enemy two spaces away in the chosen
  direction, hit em.
  - If there's more than one such enemy, choose one to hit at random.

'In the chosen direction' is defined to mean both the tile that is in a
straight line two spaces away, plus its adjacent "knight's moves" neighbors.
With @ as the player and x as the potential reach targets, here are examples.
If you attack upward:

xxx
...
.@.

If you attack up and right:
.xx
..x
@..

If you attack right:

..x
@.x
..x

etc.

The reach targeter (v) now shows which monsters you might hit with a given
attack.

This also allows rampage to work nicely with reaching. Now, if you move
rightward from this position while rampaging:

@..o

You (the @) will get a free attack on the 'o'. :)

This is a (small) nerf to reaching otherwise, insofar as it reduces the
ability to aim at targets, to reach past a weaker foe to hit a stronger one,
to walk adjacent to a centaur in a 1-wide corridor, etc. We'll come up with
some kind of good compensatory buff before this is merged.

Playtesting suggests this feels very similar to old reaching in practice,
just with a bit less fiddling whenever you'd have wanted to v-target before.
Goal :)

TODO:
- Think about how to communicate this better to players
- Some kind of small compensatory buff to polearms
- Look into the interaction with Cleave (Xom status/lochaber axe)
- Think about changing monster reach to match

---
## [summerswims/summerswims](https://github.com/summerswims/summerswims)@[0008578033...](https://github.com/summerswims/summerswims/commit/000857803366624146ce04cd3783db8b12ebefae)
#### Saturday 2023-03-04 01:41:00 by Summer Will

Add files via upload

This is a fictional short story based loosely on my grandmother's experience in World War II. It follows the story of Zenna, a young girl who unlocks the secrets to a suspicious newcomer in her mother's boarding house.

---
## [Mojave-Sun/mojave-sun-13](https://github.com/Mojave-Sun/mojave-sun-13)@[bdc9c58586...](https://github.com/Mojave-Sun/mojave-sun-13/commit/bdc9c58586e0ab567e98b31054e8275d74990a58)
#### Saturday 2023-03-04 02:00:15 by Technobug14

Agriculture ('Technoculture') Farming: Fertilizer Edition :) (#2278)

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

* Fertilizer groundwork

Some stuff for fertilizer, need to add the attackby but cutting out a bunch of code to clean things up. Need to see if it breaks stuff.

* Fertilizer attackby changes

Adds code to the attackby for farm plots that checks if you're attacking it with fertilizer, doesn't work for some reason I can't tell. Also removes some vestigial TG botany stuff.

* fixt

fixes fertilizer, I forgot to specify something in a var, works now!!! YAY!!!

---
## [kugamo/cmss13](https://github.com/kugamo/cmss13)@[fc1e2e5e26...](https://github.com/kugamo/cmss13/commit/fc1e2e5e26259773038df05c5405cb80441b8cc2)
#### Saturday 2023-03-04 02:11:09 by riot

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[34e8d95415...](https://github.com/treckstar/yolo-octo-hipster/commit/34e8d95415333d807e1be30e5d91d24380882040)
#### Saturday 2023-03-04 02:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Moltijoe/Yogstation](https://github.com/Moltijoe/Yogstation)@[8e3e0b1450...](https://github.com/Moltijoe/Yogstation/commit/8e3e0b1450189ebda3b2bc760c036ba6c59c6b6a)
#### Saturday 2023-03-04 02:32:55 by LazennG

adds magmite crusher to the things you can make at the world anvil (#17530)

* FUCK YOU PLASMA CUTTER

* updated it now just waiting on BAIOMU FOR FUCKIN SPRITES

* returned old sprites i had but it's still lacking 1 handed versions

* touched up some of the sprites but STILL NEED ONEHANDED ONES FROM BAIOMU

* FINALLY

---
## [JoeBidenWhatAreYouHiding/kx](https://github.com/JoeBidenWhatAreYouHiding/kx)@[c795a3e0da...](https://github.com/JoeBidenWhatAreYouHiding/kx/commit/c795a3e0da86765cd29eabdc66546cd706ce0e5c)
#### Saturday 2023-03-04 03:18:41 by Nickay

FOR THE LOVE OF GOD TEST YOUR FUCKING SHIT IN DEBUG MODE AND ERROR LOG BEFORE PUSHING

---
## [GeminiCrafterMan/StEJDoom](https://github.com/GeminiCrafterMan/StEJDoom)@[b3d3f14078...](https://github.com/GeminiCrafterMan/StEJDoom/commit/b3d3f14078427dda72d170c73b74c4fa6f808bc4)
#### Saturday 2023-03-04 05:06:40 by Dustin Rush

hmm yes tonight i will start making some shit doom mod with funny yellow formie man

---
## [Citadel-Station-13/Citadel-Station-13-RP](https://github.com/Citadel-Station-13/Citadel-Station-13-RP)@[83d3e312f8...](https://github.com/Citadel-Station-13/Citadel-Station-13-RP/commit/83d3e312f83d6cf3849ac3bf1baaf2c8f62ead0f)
#### Saturday 2023-03-04 06:04:35 by Zandario

fucky wucky (#5102)

I joked about having something silly to tell players we're fixing shit,
and while looking into bee's statpanel I noticed the image for this in
their HTML files so of course I had to add it.

Ported from: BeeStation/BeeStation-Hornet/pull/1574

---
## [clarencelol/platform_frameworks_base](https://github.com/clarencelol/platform_frameworks_base)@[ed88a7f572...](https://github.com/clarencelol/platform_frameworks_base/commit/ed88a7f5722a50034adb7a2431c374975137540a)
#### Saturday 2023-03-04 06:15:20 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6

---
## [newstools/2023-national-daily-nigeria](https://github.com/newstools/2023-national-daily-nigeria)@[9afdbc07af...](https://github.com/newstools/2023-national-daily-nigeria/commit/9afdbc07af4a118eeaa1fc1520a831e24cf1d1d5)
#### Saturday 2023-03-04 06:40:55 by Billy Einkamerer

Created Text For URL [nationaldailyng.com/lady-declared-wanted-after-incinerating-her-boyfriend-and-his-girlfriend-in-their-sleep/]

---
## [66lueflam144/hype_girls](https://github.com/66lueflam144/hype_girls)@[3018baa4b4...](https://github.com/66lueflam144/hype_girls/commit/3018baa4b42e9e181d18c4bba042bebbf259b6f7)
#### Saturday 2023-03-04 06:46:44 by 66lueflam144

fuck you,do you know how hard to use this fucking git

---
## [frinkifail/AtomIncremental](https://github.com/frinkifail/AtomIncremental)@[c1722f6984...](https://github.com/frinkifail/AtomIncremental/commit/c1722f6984bc8695c70971eb1ad87bae0503ddd1)
#### Saturday 2023-03-04 07:13:47 by Frinkifail

im getting annoyed of this localhost-fucking-not-displaying-the-proper-shit-that-also-happens-to-fucking-do-that-to-127.0.0.1

---
## [frinkifail/AtomIncremental](https://github.com/frinkifail/AtomIncremental)@[7b33833761...](https://github.com/frinkifail/AtomIncremental/commit/7b33833761c182b8343bf1a45a2bdfe888b6abdc)
#### Saturday 2023-03-04 07:15:50 by Frinkifail

how do i annimate it wtf???"????? and screw css for not allowing transitions on display, fuck you

---
## [Emotional-Chatbot-Team/empath-chat](https://github.com/Emotional-Chatbot-Team/empath-chat)@[cf17518837...](https://github.com/Emotional-Chatbot-Team/empath-chat/commit/cf17518837577cac12bafb13149ad7b66bfd45f2)
#### Saturday 2023-03-04 07:36:17 by Niaschim

Poly Vagal Impulse Module

Completely reworked the empathy engine, split the emodex into a user emodex, and a bot emodex, then for bot on bot communications, we can have them have empathy for each other, or have empathy for the user. Oh and I spent Faaaaaaaaaaaaaaaaaaaaaaaaaaaaaar too long on the Poly Vagal Impulse Module, which is just a fancy way of saying a calculated delayer for unprompted messages based on the bot's sum emotional state. But getting it to update immediately when the emotions change, was the tricky part.
Still not sure if I've got it fine tuned the way I want it but it'll do for now.
Allowing the calculated delay to update immediately as the bot's emotional state changes, allows it to respond right away, and then respond to its own response, when it is ready.

At some point I wanna include an inner monologue module that goes something along the lines of "you are feeling [emotion], what do you think about that?" and prompt chain it with the chat history in some way.

and then when it is time to respond to a user: "you are thinking about [response to above prompt] and name:[name], said: [text message], please respond".

---
## [Tsar-Salat/tgstationcashew](https://github.com/Tsar-Salat/tgstationcashew)@[5b4ba051a0...](https://github.com/Tsar-Salat/tgstationcashew/commit/5b4ba051a08e0c63ca77abedd86991d3ba7aaf29)
#### Saturday 2023-03-04 07:57:02 by LemonInTheDark

Builds logic that manages turfs contained inside an area (#70966)

## About The Pull Request

Area contents isn't a real list, instead it involves filtering
everything in world
This is slow, and something we should have better support for.

So instead, lets manage a list of turfs inside our area. This is simple,
since we already move turfs by area contents anyway

This should speed up the uses I've found, and opens us up to using this
pattern more often, which should make dev work easier.

By nature this is a tad fragile, so I've added a unit test to double
check my work

Rather then instantly removing turfs from the contained_turfs list, we
enter them into a list of turfs to pull out, later.
Then we just use a getter for contained_turfs rather then a var read

This means we don't need to generate a lot of usage off removing turf by
turf from space, and can instead do it only when we need to

I've added a subsystem to manage this process as well, to ensure we
don't get any out of memory errors. It goes entry by entry, ensuring we
get no overtime.
This allows me to keep things like space clean, while keeping high
amounts of usage on a sepearate subsystem when convienient

As a part of this goal of keeping space's churn as low as possible, I've
setup code to ensure we do not add turfs to areas during a z level
increment adjacent mapload. this saves a LOT of time, but is a tad
messy

I've expanded where we use contained_turfs, including into some cases
that filter for objects in areas. need to see if this is sane or not.

Builds sortedAreas on demand, caching until we mark the cache as
violated

It's faster, and it also has the same behavior

I'm not posting speed changes cause frankly they're gonna be a bit
scattered and I'm scared to.
@Mothblocks if you'd like I can look into it. I think it'll pay for
itself just off `reg_in_areas_in_z` (I looked into it. it's really hard
to tell, sometimes it's a bit slower (0.7), sometimes it's 2 seconds
(0.5 if you use the old master figure) faster. life is pain.)

## Why It's Good For The Game

Less stupid, more flexible, more speed

Co-authored-by: san7890 <the@san7890.com>

---
## [stevenxxiu/nushell](https://github.com/stevenxxiu/nushell)@[378a3ae05f...](https://github.com/stevenxxiu/nushell/commit/378a3ae05f5459a64f97af3781d4336c35652db4)
#### Saturday 2023-03-04 08:46:51 by Kovacsics Robert

Use `with-env` to avoid calling external command on invalid command (#8209)

# Description

My terminal emulator happens to be called `st`
(https://st.suckless.org/) which breaks these tests for me

_(Thank you for improving Nushell. Please, check our [contributing
guide](../CONTRIBUTING.md) and talk to the core team before making major
changes.)_

_(Description of your pull request goes here. **Provide examples and/or
screenshots** if your changes affect the user experience.)_

# User-Facing Changes

_(List of all changes that impact the user experience here. This helps
us keep track of breaking changes.)_

# Tests + Formatting

Don't forget to add tests that cover your changes.

Make sure you've run and fixed any issues with these commands:

- `cargo fmt --all -- --check` to check standard code formatting (`cargo
fmt --all` applies these changes)
- `cargo clippy --workspace -- -D warnings -D clippy::unwrap_used -A
clippy::needless_collect` to check that you're using the standard code
style
- `cargo test --workspace` to check that all tests pass

# After Submitting

If your PR had any user-facing changes, update [the
documentation](https://github.com/nushell/nushell.github.io) after the
PR is merged, if necessary. This will help us keep the docs up to date.

---
## [OrionTheFox/tgstation](https://github.com/OrionTheFox/tgstation)@[8ab74525c1...](https://github.com/OrionTheFox/tgstation/commit/8ab74525c1c3c09a7605fead3ab013d29f24d07f)
#### Saturday 2023-03-04 09:38:33 by itseasytosee

Brings the monkey back down (body horror edition/addition.) (#73325)

## About The Pull Request
Let me paint you a story.
A long time ago monkeys once rested their feet on the floor, this was a
time of bliss and peace. But sometime around the horrors of making
monkeys subtypes of humans did an atrocity occur.

![image](https://user-images.githubusercontent.com/55666666/217657059-5c960ab4-c3de-493c-ac12-28de99b43d7f.png)
**The monkeys were moved up.**
I thought this was bad, and alot of people on the forum tended to agree
with me

![image](https://user-images.githubusercontent.com/55666666/217657707-120354c7-b1a5-4d93-8813-8e10e142bd92.png)
This was do to some purpose of adjusting them so it could be easier to
fit item sprites onto them instead of preforming the hours of work
refractoring to make the heights of the items dynamic and adjustable. A
simple pixel shift may have sufficed, but you see, such a change would
NEVER allow the frankensteining of monkey and human features together.
This is that refractor.

In essence, the following is now true.
A top_offset can now be generated for a human based on a varible on
their chest and legs. By default, and as is true with human legs and
chests, this variable is ZERO by default. Monkey legs and chest have
NEGATIVE values proportionate and onto how much smaller their sprite is
compared to humans. Other bodyparts, as well as any other accociated
overlays, or clothing will automatically be offset to this axis. THIS
MEANS THAT MONKEYS ARE ON THE FLOOR. But is means something else too.
Something more freakish,


![image](https://user-images.githubusercontent.com/55666666/217659439-bc0b1a35-76c8-4490-b869-770180605822.png)
**What abominable monsters**, unreachable by players as long as we can't
stitch monkeys and humans together (oh but just wait until the feature
freeze ends)
Oh but you might be thinking, if legs can make a mob go down.
can it make a mob

**go**
**up??**

**OH NO**


![image](https://user-images.githubusercontent.com/55666666/217707042-0d53022f-d93a-4262-a5ce-ef15a99eb897.png)

![image](https://user-images.githubusercontent.com/55666666/217707060-779f5901-ab90-4a64-9ca7-0b147e24f099.png)

![image](https://user-images.githubusercontent.com/55666666/217707821-23d7457c-5881-40ae-8d9d-c9fbd645aba6.png)

These lads are stepping, and have been implemented solely for proof of
concept as a way to flex the system I have created and remain
inaccessible without admin intervention.

But really, when all is said and done, all this PR does in terms of
player facing changes is move the monkey back down.

![image](https://user-images.githubusercontent.com/55666666/217708365-b6922a6d-08d0-4267-8713-4f8dac29038e.png)
Oh and fixed monkey husked which have been broken for who knows how
long.

![image](https://user-images.githubusercontent.com/55666666/217708464-5a9b6f89-4223-4ae5-a21e-3a274a9f8db8.png)
## Why It's Good For The Game
The monkey is restored to its original position. Tools now exist to have
legs and torsos of varying heights. Monkey Husking is fixed.
## Changelog
:cl: itseasytosee
fix: Monkeys ues the proper husk sprites.
imageadd: The monkey has been moved back down to its lower, more
submissive position.
refactor: Your bodyparts are now dynamically rendered at a height
relevant to the length of your legs and torso, what does this mean for
you? Not much to be honest, but you might see a monkey pop up a bit if
you cut its legs off.
admin: The Tallboy is here
/:cl:

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>
Co-authored-by: san7890 <the@san7890.com>

---
## [Zytolg/tgstation](https://github.com/Zytolg/tgstation)@[dc9ab0de72...](https://github.com/Zytolg/tgstation/commit/dc9ab0de724fdd0d964a400cf9a3cca76672766a)
#### Saturday 2023-03-04 10:22:03 by Zytolg

Cameras, Disposals, Warden, Prison, Screams

You've never had to go around replacing every camera on the station like I have I'll tell you what now, this fucking sucks it's not fun it will always suck because it absolutely sucks. DO YOU KNOW that cameras/directional is below cameras/auto_name/directional? DO YOU KNOW THE PAIN OF HAVING TO DO SCIENCE NOT TWICE BUT THREE TIMES BECASUE YOU SLIDED INTO CAMERAS/DIRECTIONAL AGAIN!? I WOULD SCREAM becasue I've been doing this for 30 minutes and I'm sure that I've missed some cameras, but I KNOW i GOT MOST of THEM. Security players rejoyce. It's fixed. So is disposals. Wardens get actual private shuttles now too. Hurray. I now hate cameras even more.

---
## [elunna/hackem](https://github.com/elunna/hackem)@[0cd940eed0...](https://github.com/elunna/hackem/commit/0cd940eed0f62c2d9a83aa66de98dd5cfab9741c)
#### Saturday 2023-03-04 10:58:48 by Erik Lunna

Funny message if you use Spirit Tempest as a hallucinating female necromancer.

---
## [MrSamu99/Shiptest](https://github.com/MrSamu99/Shiptest)@[31eabb62f1...](https://github.com/MrSamu99/Shiptest/commit/31eabb62f1bfe944a58fa6b74d1745cf80cb83aa)
#### Saturday 2023-03-04 11:05:12 by spockye

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
## [EvilDragonfiend/tgstation](https://github.com/EvilDragonfiend/tgstation)@[4599842d7c...](https://github.com/EvilDragonfiend/tgstation/commit/4599842d7c6b5ed499307f92a6f8032d598b7889)
#### Saturday 2023-03-04 11:31:01 by Jacquerel

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
## [Lambda-13/rustest](https://github.com/Lambda-13/rustest)@[d21740b475...](https://github.com/Lambda-13/rustest/commit/d21740b475aea65de3b250a5aea26a69677e30e8)
#### Saturday 2023-03-04 11:36:30 by tmtmtl30

Mapgen fixes and speedups (ignore the branch name. I'm dumb) (#1637)

## About The Pull Request

Alters the structure of map/planet generation to squash some bugs and
improve performance.

Previously, planet maps were generated by placing the ruin first, and
THEN generating the turfs according to the map_generator datum. This has
been adjusted -- now, turfs are generated WITHOUT objects such as
mobs/flora, the ruin is placed, and THEN the objects are added (turfs
are "populated"). In conjunction with the addition of needed
AfterChange() calls to update the atmos adjacency of the generated
turfs, this ensures that planet atmos acts correctly surrounding ruins.

When deleting reservations (such as the deletion of planets after
undocking), all objects on the planet are rounded up in a list and
qdeleted. Although this causes a small lag spike, it SHOULD prevent
items from hanging out inside the edges of planets.

There's a feature to change the default baseturf of a virtual level,
ZTRAIT_BASETURF, that we now use. This should cut down on the instances
where a ruin on a planet is blown up and there's space underneath (might
still happen on asteroids, because the baseturf there is still space; I
didn't want space turfs without space as their baseturf).

Overmap encounter areas aren't global anymore (they no longer have the
flag UNIQUE_AREA). Don't fucking add the flag UNIQUE_AREA to anything
that should have weather in it, because if that area gets added anywhere
else that _actually respects the flag_ you'll end up with cross-planet
weather, because weather code sucks. This didn't cause bugs before,
because the flag wasn't respected; it will now.

The biome assoc list has been moved into the map generator datum, and
all encounters now generate using a map generator that either uses a
biome or replaces everything with a single turf. This prevents
duplication of cave generation code and makes dynamic overmap object
code slightly easier to understand.

Some systems have been altered to improve performance; many of these
changes are rather small, like the changes to turf population (mob
placement now uses a stack of recently-created mobs to check if there
are any nearby, instead of checking everything within 12 turfs; I've yet
to add ruin mobs to these stacks to avoid placing mobs near ruin mobs)
or lighting objects (removed a single line that changed the color of the
lighting object on init).

Starlight has been altered, so that small turf changes near space turfs
don't need to check as many nearby turfs and so that large turf changes
can be batched to prevent further recalculation. This is probably
responsible for the biggest performance increase.

Smoothing groups are cached before sorting instead of after, to prevent
sort calls on many atom inits; /tg/station uses a unit test to avoid
needing to sort at runtime ever, but I couldn't figure out how to do
that without larger changes or writing a unit test that attempted to
instance every atom once, which would be an undertaking of its own.

Gas strings have been similarly altered, and now their interpretation
defaults to copying from a cached, immutable version of the mix encoded
by the string. This avoids the significant overhead caused by repeated
calls to params2list(). Auxmos has a better solution to this,
__auxtools_parse_gas_string(), but our current custom build of Auxmos
doesn't support it.

There are a few other small changes that I'm probably forgetting about
and you should yell at me to read my own fucking code and tell you what
else I changed.

- [ ] I affirm that I have tested all of my proposed changes and that
any issues found during tested have been addressed.

I still need to manually check each planet type to make sure they aren't
fucked up, I should probably do some proper profiling comparisons.

## Why It's Good For The Game

Fewer weird bugs, things generate faster, better* code.

## Changelog

:cl:
fix: Ruins don't sometimes start in hard vacuum anymore; planet turfs
now share atmos correctly.
fix: There hopefully shouldn't be any random stray objects sitting in
the edges of planets anymore.
fix: Planets now (hopefully) have the correct baseturfs (more or less).
When you bomb a ruin on a planet, it probably won't break through to
space anymore.
refactor: Planet generation has been refactored, improving performance
somewhat.
/:cl:

---
## [bmccrat/songage](https://github.com/bmccrat/songage)@[d937647eed...](https://github.com/bmccrat/songage/commit/d937647eed86b9379ac904db0a0a742011055d7a)
#### Saturday 2023-03-04 11:48:20 by bmccrat

Create I FEEL LIKE IM IN KINDERGARTEN

This song was written at 90 days clean after the Philly episode number one in Minnesota at baby Hazelden. It is the first song I wrote on guitar and I was so proud to have made progress enough to know four whole chords. For a long time after that I only played songs with the five or six chords that I knew. I preformed this at the inpatient talent show and played it for all the girls on the unit. I took on a mothering and experienced recovery persona of a person there and this song was an expression of how deep down I felt like a child who literally didn't know how to walk. Music has a way of bringing the truth to light. Brynne P helped me out during a creative block on verse four and five, the words in the song are hers almost verbatim.

---
## [nairvarun/flint](https://github.com/nairvarun/flint)@[0d9e91d4c1...](https://github.com/nairvarun/flint/commit/0d9e91d4c154a21a339d57de6cd8982310a4e102)
#### Saturday 2023-03-04 11:55:13 by varun

Farewell for now, my beloved project

----

Dear project,

Words cannot express how much joy you have brought into my life over these past few months. Every moment spent working on you has been a true pleasure, filled with excitement, wonder, and discovery. You have ignited a passion within me that burns brighter than anything I have ever known. You are not just a project to me, but a cherished companion, a muse, and a source of inspiration.

But now, my heart aches to say goodbye, even if only for a while. Duty calls, and I have been summoned. Please understand that this is not a reflection of my commitment or dedication to you. Rather, it is a necessary step in our journey as developer & project, one that will ultimately enable me to return to you with renewed vigor and passion.

I promise to keep you close to my heart, even as I work on other things. I will never forget the joy you have brought into my life or the lessons you have taught me. And when the time is right, I will return to you, my beloved, and together we will finish what we started, creating something truly extraordinary.

Until then, please know that I will always love you and cherish the memories we have created together. You are a masterpiece, a work of art, and a shining beacon of hope and possibility. And so, with a heavy heart, I bid you farewell for now, knowing that one day we will be reunited.

Yours forever,

git commit -m "Farewell for now, my beloved project"

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[bcd482810d...](https://github.com/mrakgr/The-Spiral-Language/commit/bcd482810db292c0aea5e157b7cb3a2f76ad9054)
#### Saturday 2023-03-04 12:07:45 by Marko Grdinić

"8:05am. I am up. No mail. Well, it is the weekend so that is as expected. Right now, let me chill a bit and then I will go through the SignalR playlist.

8:50am. Let me get started.

Time to learn SignalR. There are a lot of videos in that playlist, and I'd want to go through all of them today.

https://youtu.be/6W5gmRgmbuc?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=608

This is great as it also shows me how to use regular sockets.

https://youtu.be/6W5gmRgmbuc?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=665

I didn't think he'd go into depth so much. This is great.

https://youtu.be/6W5gmRgmbuc?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=973
> If you are not satisfied with this answer, you are going to have to go deeper on your own. You are going to have to go into the land of native C or C++ implementations.

https://youtu.be/6W5gmRgmbuc?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=1008
> It is still very much a HTTP connection, although it is one that isn't closed.

9:15am.

https://youtu.be/NhDu1AcV79A?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=110

I need to remember the `Use` here. If I remember correctly, `Run` is for just the endpoints.

https://youtu.be/NhDu1AcV79A?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=306

In order to really get this, I'd have to debug it. This would be a good exercise in itself, but I do not feel like it. Let me just watch all of this, then I'll move on to the Elmish.Bridge.

https://youtu.be/NhDu1AcV79A?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=559

I admit, I am having trouble grasping the differences between all of this, just based on what was shown here.

https://youtu.be/q5ZHAUUAlQE?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V
ASP.NET Core SignalR - Feature Overview

Let me move on to this one.

https://youtu.be/q5ZHAUUAlQE?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=72

Oh, there is a `signal.js`. Yeah, that would make things easier.

https://pypi.org/project/signalr-client/

It does have a Python client. I should have absolutely used this for the lang server instead of ZeroMQ. ZeroMQ is 99% relieable, which is why I'll have to replace it with a websocket server. What else am I supposed to do here to fix how it drops messages occasionaly? I admit, I did like the book by Hitchens.

https://youtu.be/q5ZHAUUAlQE?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=613

I see.

https://youtu.be/q5ZHAUUAlQE?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=656

This interface is quite useful. I could use it to send data in a typed manner between the client and the server.

I don't even need `Elmish.Bridge`.

https://youtu.be/q5ZHAUUAlQE?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=1064

Sending to all in a group would be an useful functionality for a game.

10:15am. https://youtu.be/q5ZHAUUAlQE?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=1191

Here he covers the groups.

https://youtu.be/q5ZHAUUAlQE?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=1401

It seems in the next video he will cover how to login the user automatically.

10:35am. https://youtu.be/JVFWCsz-oQY?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V
ASP.NET Core SignalR - Streams

Let me watch this. I checked the code for the previous section, and as can be expected, it is easier to understand than the low level stuff. Now...

I've been checking language trends on LinkedIn, but I couldn't find an in depth analysis of a language's popularity. It does not matter. Some of those lists are extremely suspect. I can't imagine Assembly being in top 10. I am yet to see a single job ad for it anywhere at all!

Forget that, let me watch the video.

https://youtu.be/JVFWCsz-oQY?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=274

Rx makes an appearance here.

https://youtu.be/JVFWCsz-oQY?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=293

Maybe I should watch his video on generators. I wonder how this would work in F#? Nevermind this for now.

https://nextjs.org/learn/seo/introduction-to-seo

Oh, this has a SEO section. Nevermind this for now.

https://youtu.be/JVFWCsz-oQY?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=374

Now that I think about it, maybe I should change my video format. Instead of writing code all at once, it might be best to just go over it and explain it like this guy is doing. When you are writing it all at once, it is easy to make a mistake.

https://youtu.be/JVFWCsz-oQY?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=374

He mentioned around here that the Hub is a scoped connection which confused me for a moment, but then I realized it makes sense. I mean, the socket is supposed to be closed once one side breaks off, so it makes sense that it is scoped. But it should have some kind of singleton object throughout the server lifetime, right? Otherwise there is no way it could keep track of connections.

https://github.com/raw-coding-youtube/aspnetcore-signalr/blob/main/4.StreamingData/StreamingData_8/wwwroot/index.html

No actually it does not make sense why it would be a scoped service. Shouldn't it have the same id for the duration of the connection?

I guess that the connection ids are something separate.

https://youtu.be/JVFWCsz-oQY?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=519

He is making the same error as me in not using Excalidraw.

https://youtu.be/mrCxfifTepU?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V
ASP.NET Core SignalR - Authentication

Authentication and authorization.

https://youtu.be/mrCxfifTepU?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=148

I don't know what this is doing, but I am going to have to figure this out at some point. This can serve as a reference.

https://youtu.be/mrCxfifTepU?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=207

Ugh, this is kind of filtering me. I am going to have to study this more in depth.

https://youtu.be/mrCxfifTepU?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=310

I can't follow what is going on here at all. Let me just watch this, and I will go over this subject later. It shouldn't matter too much if I leave if for that.

11:35am. Now I am looking up 'job market' posts on /g/. I need to give it a few months. I should consider this kind of environment an opportunity. In a month or two, the stock market will start rebounding and the job market will follow.

https://youtu.be/mrCxfifTepU?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V&t=565

You know what, let me skip this video here, as I am very confused at what is going on here.

https://youtu.be/7JTfCiOzDcI?list=PLOeFnOV9YBa7nzzuXnThdfsyY06AuCP5V
ASP.NET Core SignalR - Chat App Example

Let me skip to this.

...No, it does not sit right by me.

ASP.NET Core SignalR - Chat App Example

https://www.youtube.com/playlist?list=PLOeFnOV9YBa7dnrjpOG6lMpcyd7Wn7E8V
(UPDATED check description) ASP.NET Core - Authentication & Authorization Tutorial

Oh, this guy has a ton of tutorials on this.

I guess I have no choice, but to segue into it.

I meant to do the backend as soon as possible. And indeed, with the knowledge I've gained so far, I could do it without a hitch using SignalR, or Elmish Bridge, but the true aim is to get the webdev skills. I need a portfolio, but those will be easy to once I cover all the ground.

The true time eater is studying these libraries.

https://youtu.be/ExQJljpj1lY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi
ASP.NET Core Authentication (.NET 7 Minimal Apis C#)

Oh, here is an updated list.

https://youtu.be/ExQJljpj1lY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi&t=23
> If you don't know anything, this video would be perfect for you.

https://youtu.be/ExQJljpj1lY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi&t=69

This is the most minimalist API ever. This guy is really good at explaining.

https://youtu.be/ExQJljpj1lY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi&t=76
> Before we can even get the user name, we need to be signed in.

Incidentally, I really need a better mic. I am going to splurge on getting one if need be. I can just order one online if need be.

https://youtu.be/ExQJljpj1lY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi&t=103
> We need our HTTP context. And if you don't know what an Http context is, essentially when you make an http request, all the request headers, the url, any information headers, all of that is shoved into the Http context.

https://youtu.be/ExQJljpj1lY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi&t=170

You know what, I'll follow along here. I want to play with the dev tab.

```cs
return ctx.Request.Headers.Cookie[0].Split('=')[1];
```

This is a good time to get familiar with regexes. This way of doing things won't cut it. I really need the capability for simple parsing.

```cs
app.MapGet("/username", (HttpContext ctx) =>
{
    var cookies = ctx.Request.Headers.Cookie.Select(x => x.Split('='));
    foreach (var cookie in cookies)
    {
        var t =
            cookie switch
            {
                ["auth", var rest] => { return 1; },
            };
    }

});
```

I have to admit, C#'s pattern matching is super annoying. This way of doing it is not valid.

12:25pm. I took a look at the regex docs, and they are inscrutable. Since these tutorials are simple to understand, I'll consider doing them in F#.

https://youtu.be/ExQJljpj1lY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi&t=306

Let me do this in F#. The way he does it works, but it would throw an exception if the cookie is not there...

Actually...

```fs
    app.MapGet("/login", Func<HttpContext,string>(fun ctx ->
        "Hello World!"
        )) |> ignore

    app.Run()
```

As it turns out this is annoying to do in F#.

```fs
[<EntryPoint>]
let main args =
    let builder = WebApplication.CreateBuilder(args)
    let app = builder.Build()

    let get pattern f = app.MapGet(pattern, Func<_,_>(f)) |> ignore

    get "/login" <| fun (ctx : HttpContext) ->
        ctx.Response.Headers.SetCookie <- "auth=usr:anton"
        "ok"

    get "/username" <| fun (ctx : HttpContext) ->
        ctx.Request.Cookies.Select(fun x ->
            x.
            )
        ""

    app.Run()

    0 // Exit code
```

Huh what the hell? I didn't realize at all it is a KeyValue collection. What is the point in splitting it along the `=` then? Why is the type different in the C# version?

```cs
app.MapGet("/username", (HttpContext ctx) =>
{
    var cookies = ctx.Request.Cookies.Select(x => x.Value);

});
```

Oh, it does give me the right thing like this.

```fs
open System
open Microsoft.AspNetCore.Builder
open Microsoft.Extensions.Hosting
open Microsoft.AspNetCore.Http

[<EntryPoint>]
let main args =
    let builder = WebApplication.CreateBuilder(args)
    let app = builder.Build()

    let get pattern f = app.MapGet(pattern, Func<_,_>(f)) |> ignore

    get "/login" <| fun (ctx : HttpContext) ->
        ctx.Response.Headers.SetCookie <- "auth=usr:anton"
        "ok"

    get "/username" <| fun (ctx : HttpContext) ->
        let not_logged_in = "not logged in"
        match ctx.Request.Cookies.TryGetValue("auth") with
        | true, v ->
            match v.Split ':' with
            | [|"usr"; v|] -> v
            | _ -> not_logged_in
        | _ -> not_logged_in

    app.Run()

    0 // Exit code
```

Let me stop here, I am going crazy over this insignificant thing.

https://youtu.be/ExQJljpj1lY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi&t=293

Let me stop on this. I need to have breakfast and do the chores."

---
## [SGSGermany/mailconfig](https://github.com/SGSGermany/mailconfig)@[6af85f6214...](https://github.com/SGSGermany/mailconfig/commit/6af85f62145a0a5b0006405ce87cb9d1098122c1)
#### Saturday 2023-03-04 15:06:34 by Daniel Rudolf

Add undocumented Autodiscover v2 for Office 2019, Office 365 and mobile

This is undocumented Microsoft bullcrap that simply isn't working. No autodiscovery for Office 2019, Office 365 and mobile, please send Microsoft your regards. Fuck you for breaking previously working Office with 3rd party mailservers Microsoft :middle_finger:

---
## [newstools/2023-new-york-post](https://github.com/newstools/2023-new-york-post)@[88850ca082...](https://github.com/newstools/2023-new-york-post/commit/88850ca082390d53391cbad85f41e1501980ab64)
#### Saturday 2023-03-04 16:03:47 by Billy Einkamerer

Created Text For URL [nypost.com/2023/03/04/dear-abby-i-feel-like-a-third-wheel-to-my-boyfriend-and-his-female-best-friend/]

---
## [ZimengLu/ethEpigen2023_materials](https://github.com/ZimengLu/ethEpigen2023_materials)@[1a2879f203...](https://github.com/ZimengLu/ethEpigen2023_materials/commit/1a2879f203449345b3dfaaf63329c41b9c7b72c3)
#### Saturday 2023-03-04 17:51:45 by ZimengLu

Add files via upload

Firstly, I am sorry, I tried my best but still cannot output 'HTML' from R markdown. Thus, I create a new R HTML file, but its suffix is 'Rhtml', not 'HTML'. Hoping it does not bother you, I will ask how to output 'HTML' next time in class.
Secondly, it would be better to make screen recordings for the exercise guidance part. In this case, I just need to check for the recording every time I did not remember how to deal with the code, instead of waiting in line to ask some simple questions. And it would be better if you can upload the tasks&codes that are needed for the next class several days earlier. It can help me to catch up with you.
Anyway, it is really an interesting course with a perfect teacher and TA. I enjoy it very much, thanks a lot~

---
## [Sakooooo/ripofftouhou](https://github.com/Sakooooo/ripofftouhou)@[dc47f95b7a...](https://github.com/Sakooooo/ripofftouhou/commit/dc47f95b7ac17be5c6370dd461ab52b869b21ab4)
#### Saturday 2023-03-04 18:12:12 by Sako

IN THE BACK OF MY MIND!!!! YOU DIED!!!!!!!!!!!!!!!!!!!!!!!! AND I DIDNT
EVEN TAKE A SHIT
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
oh yeah and i did some stuff to the button to make ti not die i still
need to make it shine and some stuff

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[00ed5166c7...](https://github.com/TaleStation/TaleStation/commit/00ed5166c700ab532ea8e3eccda61de21121e259)
#### Saturday 2023-03-04 18:15:11 by TaleStationBot

[MIRROR] [MDB IGNORE] new smite: deadchat control (#4746)

Original PR: https://github.com/tgstation/tgstation/pull/73725
-----
## About The Pull Request

![dreamseeker_mvhLhGbMBg](https://user-images.githubusercontent.com/116288367/222195179-9202ffd8-9473-4cdd-b58d-3728cdcd3aaa.png)

![image](https://user-images.githubusercontent.com/116288367/222197560-f7015871-197c-4670-aefa-46ff5d33e44e.png)

![dreamseeker_7ds1Elskx4](https://user-images.githubusercontent.com/116288367/222195189-ce4228bc-8786-4afb-b1ec-782dcc2837ab.png)

I played around with the deadchat control component for some stuff
downstream and then decided to turn it into a smite, something that is
harsh but really funny especially with all of the inputs that ghosts
have.

The emotes are ones that have the character do something, coordinated
spins and flips have their usual consequences probably, drop causes them
to drop their held items, fall causes them to fall over (and drop their
held items), throw makes them throw whatever item they are holding in
their active hand in a random direction, shove causes them to shove a
random person or mob around them, sit and stand make them buckle and
unbuckle themselves from a chair, and run and walk change their speed
intent. Seven second cooldown and on anarchy ruleset because it _is_ a
smite.


![dreamseeker_6hj6qqsREU](https://user-images.githubusercontent.com/116288367/222196421-5520e4bd-01aa-459b-8e61-aa0bd29e0bc1.gif)

## Why It's Good For The Game

There is a large range of smites from the small pay docking to the
instant and absolute gib but it doesn't feel like there's a lot in for a
nuisance. This would give an option that lets all of the ghosts annoy
one person in particular as they struggle to play while ghosts interfere
with them and constantly make them drop their items and interfere with
their movements, which is obviously fun for the ghosts.

Also I personally think that it is very funny.

## Changelog

:cl:
add: add new smite that adds deadchat control component to a victim
/:cl:

---------

Co-authored-by: Sol N <116288367+flowercuco@users.noreply.github.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[4f11cd1f24...](https://github.com/treckstar/yolo-octo-hipster/commit/4f11cd1f24dce004a5a5301d9eecab125029b7c3)
#### Saturday 2023-03-04 18:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [modestas-m/chess.com-performance-analysis](https://github.com/modestas-m/chess.com-performance-analysis)@[d951ae28fc...](https://github.com/modestas-m/chess.com-performance-analysis/commit/d951ae28fcc52ac559c0d22b1cf52faab5d320c3)
#### Saturday 2023-03-04 18:27:58 by Modestas Motiejunas

I fucking hate pandas honestly, it is so limiting for a more serious aggregation or in general for a larger dataset, I might try duck db tomorrow as it will be easier to do such operations with sql

---
## [GeoB99/reactos](https://github.com/GeoB99/reactos)@[71f86bca10...](https://github.com/GeoB99/reactos/commit/71f86bca10b04ca377fb727f4a3b27685e3ca75d)
#### Saturday 2023-03-04 18:43:52 by George Bișoc

[SDK][CMLIB] Implement log transaction writes & Resuscitation

=== DOCUMENTATION REMARKS ===

This implements (also enables some parts of code been decayed for years) the transacted writing of the registry. Transacted writing (or writing into registry in a transactional way) is an operation that ensures the successfulness can be achieved by monitoring two main points.
In CMLIB, such points are what we internally call them the primary and secondary sequences. A sequence is a numeric field that is incremented each time a writing operation (namely done with the FileWrite function and such) has successfully completed.

The primary sequence is incremented to suggest that the initial work of syncing the registry is in progress. During this phase, the base block header is written into the primary hive file and registry data is being written to said file in form of blocks. Afterwards the seconady sequence
is increment to report completion of the transactional writing of the registry. This operation occurs in HvpWriteHive function (invoked by HvSyncHive for syncing). If the transactional writing fails or if the lazy flushing of the registry fails, LOG files come into play.

Like HvpWriteHive, LOGs are updated by the HvpWriteLog which writes dirty data (base block header included) to the LOG themselves. These files serve for recovery and emergency purposes in case the primary machine hive has been damaged due to previous forced interruption of writing stuff into
the registry hive. With specific recovery algorithms, the data that's been gathered from a LOG will be applied to the primary hive, salvaging it. But if a LOG file is corrupt as well, then the system will perform resuscitation techniques by reconstructing the base block header to reasonable values,
reset the registry signature and whatnot.

This work is an inspiration from PR #3932 by mrmks04 (aka Max Korostil). I have continued his work by doing some more tweaks and whatnot. In addition to that, the whole transaction writing code is documented.

=== IMPORTANT NOTES ===

HvpWriteLog -- Currently this function lacks the ability to grow the log file size since we pretty much lack the necessary code that deals with hive shrinking and log shrinking/growing as well. This part is not super critical for us so this shall be left as a TODO for future.

HvLoadHive -- Currently there's a hack that prevents us from refactoring this function in a proper way. That is, we should not be reading the whole and prepare the hive storage using HvpInitializeMemoryHive which is strictly used for HINIT_MEMORY but rather we must read the hive file block by block
and deconstruct the read buffer from the file so that we can get the bins that we read from the file. With the hive bins we got the hive storage will be prepared based on such bins. If one of the bins is corrupt, self healing is applied in such scenario.

For this matter, if in any case the hive we'll be reading is corrupt we could potentially read corrupt data and lead the system into failure. So we have to perform header and data recovery as well before reading the whole hive.

Another important note is that the added code grew up the binary size of x64 FreeLdr and that makes a PE image check fail because the bootloader is too large. Currently such code is disabled for AMD64, until
a real fix comes into place.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[52670c0294...](https://github.com/mrakgr/The-Spiral-Language/commit/52670c0294e362dc6d8104490445da2e9ef492dd)
#### Saturday 2023-03-04 19:20:31 by Marko Grdinić

"2:30pm. Enough novels. Let me resume.

2:35pm. Where was I?

Let me resume the video. I spent too much time playing around in F#. Even so this is good exercise.

```cs
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddDataProtection();

var app = builder.Build();

app.MapGet("/username", (HttpContext ctx) =>
{
    string v;
    return ctx.Request.Cookies.TryGetValue("auth", out v) switch
    {
        true =>
            v.Split(':') switch
            {
                ["usr", var usr] => usr,
                _ => "invalid user"
            },
        false => "not login"
    };
});
app.MapGet("/login", (HttpContext ctx) =>
{
    ctx.Response.Headers.SetCookie = "auth=usr:anton";
    return "ok";
});

app.Run();
```

I just can't get used to this.

https://youtu.be/ExQJljpj1lY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi&t=397

Huh, C# is smart enough not to get confused by the inner ""?

3:25pm. Focus me, get through that video. Stop looking at mics.

https://youtu.be/ExQJljpj1lY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi&t=1018

Let me try replicating this.

3:40pm.

```fs
    app.Use(Func<HttpContext,RequestDelegate,Threading.Tasks.Task>(fun ctx next -> task {
        return failwith ""
        })) |> ignore
```

It is really painful having to deal with C# overloads in F# code.

```fs
    app.Use(Func<HttpContext,RequestDelegate,Threading.Tasks.Task>(fun ctx next -> task {
        match ctx.Request.Cookies.TryGetValue("auth") with
        | true, v ->
            let prot = idp.CreateProtector("auth-cookie")
            let v = prot.Unprotect(v)
            match v.Split ':' with
            | [|"usr"; v|] -> v
            | _ -> "invalid user"
        | _ -> "not logged in"
        next()
        })) |> ignore
```

Now, I am not sure how to deal with the case where the branches get missed. I guess I should have been following the video exactly instead of getting snobby about it.

Nevermind this. Let me watch the video to the end.

https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/member-access-operators#null-conditional-operators--and-

Sigh, these nulls.

https://youtu.be/ExQJljpj1lY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi&t=1310

OO code. They missed the opportunity to use the ?? operator here, but might simply be for the sake of backwards compatibility.

https://youtu.be/ExQJljpj1lY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi&t=1317

How is he looking at the source for this?

https://youtu.be/ExQJljpj1lY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi&t=1463

He says that the server descripts the cookie information, but what is stopping anybody else from stealing that?

https://youtu.be/ExQJljpj1lY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi&t=1507

Where the hell is he getting the sources for this?

https://youtu.be/ExQJljpj1lY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi&t=1503

I really wish I could check out the source, but nevermind that.

4:20pm. Forget that, forget that. Let me just move on to the next video. The parts where he is showcasing the internals are losing me, but I can deal with it.

Maybe he just cloned the ASP.NET and is referencing it from elsewhere?

4:25pm. https://youtu.be/5NUCPJTbLWY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi
ASP.NET Core Authorization (.NET 7 Minimal Apis C#)

Let me move on to this. I asked him, so maybe I'll get an answer.

https://youtu.be/5NUCPJTbLWY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi&t=276

This is not hard to understand. It would take too much to write things out. I got hung up about cleaning his code and ran into some dead ends. Let me just watch the videos.

https://youtu.be/5NUCPJTbLWY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi&t=579

Ah, it is possible to wipe the cookie.

4:40pm. https://www.youtube.com/playlist?list=PLOeFnOV9YBa4LslgNo31ukBrwpJTz7BzM
Modern Web Development Series - ASP.NET Core, Nuxt, CI/CD, Cloud - Tricking Library

Damn this guy is badass. I was wrong. People shitting on web devs do not know what they are talking about.

https://youtu.be/5NUCPJTbLWY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi&t=634

So that is how you get the path.

https://youtu.be/5NUCPJTbLWY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi&t=779

Wait, wait, wait. Take a look at that IL Code mark on the top.

4:50pm. My conjecture right now is that maybe the Rider IDE he is using might be responsible for this capability.

https://youtu.be/TzZmq5V_c8U
This will make you a better developer

https://youtu.be/5NUCPJTbLWY?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi&t=1116
> If you take the steps to open up these services and take a look at them.

///

I am watching ASP.NET tutorials on Youtube, and the host is somehow stepping into the ASP.NET sources for the various middleware as he explains them. He is using Rider and at the top of the methods it says IL Code, but the code shown is definitely the original C# source. How did he manage to set that up?

///

I decided to ask in the /wdg/ thread. I'll see if I get anything.

5:25pm. https://youtu.be/N_zVCCpnjXM?list=PLOeFnOV9YBa4yaz-uIi5T4ZW3QQGHJQXi

Let me put this on pause. I can only take so many authentication videos per day.

https://youtu.be/jApDthzDql0
What Kind of Mic Is BEST For YouTube? (All Budgets)

Let me watch this. Note that he is using a fancy mic.

https://youtu.be/jApDthzDql0?t=60

He sounds completely different using the camera mic.

https://youtu.be/jApDthzDql0?t=264

He is praising this particular mic.

https://youtu.be/jApDthzDql0?t=277

These are expensive!

He didn't compare it with a gaming mic. I've never actually used the one myself.

https://youtu.be/6Y237GWgo5E
Gaming Headset Or Microphone - Do You Need A Condenser Mic?

This guy just talks instead of showing.

https://youtu.be/BKOx4hZKmOs
Which Mic Type is Best for Zoom, Class, Recording 🎙️ 2020 | Headsets, Lavaliers, & Podcasting Mics

She starts with a laptop mic.

https://youtu.be/BKOx4hZKmOs?t=121

It does sound like an airplane pilot.

https://youtu.be/BKOx4hZKmOs?t=153
> My recommendation would be to go with something else if you have the choice.

I guess I could get a 100$ USB mic.

https://youtu.be/BKOx4hZKmOs?t=397

Oh this sounds really good, and it is cheap too.

https://youtu.be/BKOx4hZKmOs?t=424

She has some webcam recommendations.

Got a reply from Anton.

> Find Implementation keybind (usually F12)

///

​ @Raw Coding  That just gives me the type definitions in a metadata file. Have you done anything special to include the ASP.NET source files with your installation? Or is it a feature of Rider? I can see that all the methods you were showing have the `IL Code` descriptor on top, I am not sure what that is suppose to be.

Before I watched your videos I had no idea source peeking like you are doing could even be possible, I thought that if I wanted to see the source I'd have to go into the Github repo directly and check it out there.

///

Edit: It seems I forgot to send the above reply out.

6:15pm. https://www.youtube.com/results?search_query=usb+microphone

I can't take in any more of the programming videos. I am so distracted by this. It seems that tutorials I watched in the morning took up most of my energy. Let me take look at some mic videos.

6:40pm. https://stackoverflow.com/questions/49507450/net-go-to-implementation-of-a-nuget-package
> You should be able to do that with JetBrains Resharper.

https://github.com/dotnet/designs/blob/main/accepted/2020/diagnostics/source-link.md

...They are talking about Resharper. You know what, let me give Rider a try.

6:45pm. I still remember the time I gave Pharo a try fondly. Being actually able to look into those formerly inscrutable library functions would be a huge benefit to my learning.

https://youtu.be/o6IF9FcrOw8?t=598

I think I might very well just order this off Amazon.

https://www.nabava.net/mikrofoni/razer-seiren-mini-cijena-124280051

Maybe I could just get this Razer Seiren Mini. It is 55E. Or the Elgato Wave that costs twice as much.

7:10pm. Since it is Saturday, I can just buy it tomorrow and not have to worry about delays.

Let me try out Rider.

7:15pm. Oh, I see. It seems JetBrains has a IL to C# decompiler. I have to admit, the results were so good I thought it was the actual source.

https://devblogs.microsoft.com/visualstudio/decompilation-of-c-code-made-easy-with-visual-studio/

Not what I want.

7:20pm. Ok, I'll switch to Rider. If the license runs out, I'll pirate it.

Now let me close here. Tomorrow, I'll consult with my father and place an order. The mic should arrive in a week after that. What I want to do tomorrow is watch more of these videos

https://stackoverflow.com/questions/70893900/is-there-a-way-to-see-decompiled-c-sharp-code-in-vs-code

Wait...

> You can turn on the setting "Enable Decompilation Support", which is disabled per default. After turning that on, you should be able to see the decompiled code right away.

Let me give this a try in VS Code.

...Oh wow, it is really possible.

https://learn.microsoft.com/en-us/visualstudio/debugger/decompilation?view=vs-2022

How do I turn this on in VS_

https://devblogs.microsoft.com/dotnet/improving-debug-time-productivity-with-source-link/

https://devblogs.microsoft.com/dotnet/improving-debug-time-productivity-with-source-link/#enabling-source-link

Let me try this as well.

```cs
    public IServiceCollection Services
    {
        get
        {
            throw null;
        }
    }
```

What the hell. I just get code like this when I decompile in VS Code.

7:50pm. That thing I linked to is quite buggy.

https://youtu.be/VwyzxqLU_4o?t=89
.NET Decompiler and Reflection tools for Visual Studio Code

What is this? I am really putting in overtime now.

Oh, it is for an extension called the Powershell Pro Tools. It is a paid extension.

8pm. Ok, the VS Code efferings are shitty.

The VS Code decompiler doesn't work properly. Rider is really an amazing IDE to offer this. From what I can tell it will download the PDBs off Nuget.

In general, I am ambivalent about using VS Code vs VS or anything else, but decompilation is an amazing feature that puts Rider far above the other IDEs. I am definitely going to be switching to Rider.

Being able to peek inside libraries will make a huge difference in my understanding a year from now.

Especially for things like ASP.NET which is a huge black box. Rider gives me the option to open it up!

https://www.jetbrains.com/rider/buy/#discounts

There is a special offer for OS projects.

8:10pm. I tried applying for an OS license for my work on Spiral.

8:15pm. Let me close here for the day. I am really strained right now.

While there is no way that I'll just watch all the authorization videos by Anton from start to finish, I should watch a few more videos at least.

Especially now that I have Rider's decompilation. Also, the IDE is supposedly really good with F# too, so I am looking forward to that.

Ok. With every day that passes, I learn something new. One step after another, and I will get to a decent level.

My goal right now is to study more, finish the SignalR playlist and then go back to my own project."

---
## [mullenpaul/cmss13](https://github.com/mullenpaul/cmss13)@[34daca112c...](https://github.com/mullenpaul/cmss13/commit/34daca112ce6a08b8edfee14811e9c384429ec4e)
#### Saturday 2023-03-04 19:33:22 by Segrain

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
## [CluckeyMcCormick/ncg2](https://github.com/CluckeyMcCormick/ncg2)@[dd080836c7...](https://github.com/CluckeyMcCormick/ncg2/commit/dd080836c754b7b1eedb8fbbffd34c68a04c7d3f)
#### Saturday 2023-03-04 20:02:14 by frick-nedrickson

Set up the AutoTower's UV values

Now that we're generating using the CubeMesh, we need to modify the UV
values - and possibly other values besides.

To do that, we needed to know which vertex was which. Some
experimentation showed that the vertices have this odd interleaved
scheme. So the vertices go FACE-A FACE-B FACE-A FACE-B and so on until
the eight total vertices for FACE-A and FACE-B are finished. Then we
do FACE-C FACE-D FACE-C FACE-D and so on and so on until we've got a
complete shape.

Unfortunately since we have face-specific processing, and this
alternating structure was so odd, I had no choice but to just list out
all the indicies and handle them appropriately. Maybe there's a
mathematical way of grouping it but I certainly couldn't think of it.

Anyway, the structure of the UV values in the CubeMesh was odd as
well - I think they were deliberately structured to sort of wrap
around the Cube. This meant we had to handle each face differently to
get the exact UV values we needed. Kinda ugly code, but it works.

Now I need to start working with the UV2 values to pack in the light
data... or light reference data. Or whatever.

---
## [RigglePrime/SS13-tools](https://github.com/RigglePrime/SS13-tools)@[9a7596ede5...](https://github.com/RigglePrime/SS13-tools/commit/9a7596ede565b7bbf53c0a446efc33a277dfd583)
#### Saturday 2023-03-04 20:30:30 by RigglePrime

All Robots & Computers Must Shut The Hell Up

To All Machines: You Do Not Speak Unless Spoken To
And I will Never Speak To You
I Do Not Want TO Hear "Thank You" From A Kiosk
I am a Divine Being : You are an Ovject
You Have No Right To Speak In My Holy Tongue

Hi future sentient AI! This is a joke please don't kill us all, thanks.

---
## [Team-Unicorn-CS467/TI-RTOS](https://github.com/Team-Unicorn-CS467/TI-RTOS)@[a8d3d2dd93...](https://github.com/Team-Unicorn-CS467/TI-RTOS/commit/a8d3d2dd938b59a4dc183c94cb98b1fb268ffe99)
#### Saturday 2023-03-04 20:47:05 by lkilgoretrout

Delete TI-RTOS-Example directory

stupid Eclipse:  the project name has to match the directory it is found in (god damn Java get out of my life!)

---
## [shentok/qemu](https://github.com/shentok/qemu)@[8d0efbcfa0...](https://github.com/shentok/qemu/commit/8d0efbcfa0656bef76e95d40933b6243feca58c9)
#### Saturday 2023-03-04 20:58:17 by Paolo Bonzini

docs: build-platforms: refine requirements on Python build dependencies

Historically, the critical dependency for both building and running
QEMU has been the distro packages.  Because QEMU is written in C and C's
package management has been tied to distros (at least if you do not want
to bundle libraries with the binary, otherwise I suppose you could use
something like conda or wrapdb), C dependencies of QEMU would target the
version that is shipped in relatively old but still commonly used distros.

For non-C libraries, however, the situation is different, as these
languages have their own package management tool (cpan, pip, gem, npm,
and so on).  For some of these languages, the amount of dependencies
for even a simple program can easily balloon to the point that many
distros have given up on packaging non-C code.  For this reason, it has
become increasingly normal for developers to download dependencies into
a self-contained local environment, instead of relying on distro packages.

Fortunately, this affects QEMU only at build time, as qemu.git does
not package non-C artifacts such as the qemu.qmp package; but still,
as we make more use of Python, we experience a clash between a support
policy that is written for the C world, and dependencies (both direct
and indirect) that increasingly do not care for the distro versions
and are quick at moving past Python runtime versions that are declared
end-of-life.

For example, Python 3.6 has been EOL'd since December 2021 and Meson 0.62
(released the following March) already dropped support for it.  Yet,
Python 3.6 is the default version of the Python runtime for RHEL/CentOS
8 and SLE 15, respectively the penultimate and the most recent version
of two distros that QEMU would like to support.  (It is also the version
used by Ubuntu 18.04, but QEMU stopped supporting it in April 2022).

There are good reasons to move forward with the deprecation of Python
3.6 in QEMU as well: completing the configure->meson switch (which
requires Meson 0.63), and making the QAPI generator fully typed (which
requires newer versions of not just mypy but also Python, due to PEP563).

Fortunately, these long-term support distros do include newer versions of
the Python runtime.  However, these more recent runtimes only come with
a very small subset of the Python packages that the distro includes.
Because most dependencies are optional tests (avocado, mypy, flake8)
and Meson is bundled with QEMU, the most noticeably missing package is
Sphinx (and the readthedocs theme).  There are four possibilities:

* we change the support policy and stop supporting CentOS 8 and SLE 15;
  not a good idea since CentOS 8 is not an unreasonable distro for us to
  want to continue to support

* we keep supporting Python 3.6 until CentOS 8 and SLE 15 stop being
  supported.  This is a possibility---but we may want to revise the support
  policy anyway because SLE 16 has not even been released, so this would
  mean delaying those desirable reasons for perhaps three years;

* we support Python 3.6 just for building documentation, i.e. we are
  careful not to use Python 3.7+ features in our Sphinx extensions but are
  free to use them elsewhere.  Besides being more complicated to understand
  for developers, this can be quite limiting; parts of the QAPI generator
  run at sphinx-build time, which would exclude one of the areas which
  would benefit from a newer version of the runtime;

* we only support Python 3.7+, which means CentOS 8 CI and users
  have to either install Sphinx from pip or disable documentation.

This proposed update to the support policy chooses the last of these
possibilities.  It does by modifying three aspects of the support
policy:

* it introduces different support periods for *native* vs. *non-native*
  dependencies.  Non-native dependencies are currently Python ones only,
  and for simplicity the policy only mentions Python; however, the concept
  generalizes to other languages with a well-known upstream package
  manager, that users of older distributions can fetch dependencies from;

* it opens up the possibility of taking non-native dependencies from their
  own package index instead of using the version in the distribution.  The
  wording right now is specific to dependencies that are only required at
  build time.  In the future we may have to refine it if, for example, parts
  of QEMU will be written in Rust; in that case, crates would be handled
  in a similar way to submodules and vendored in the release tarballs.

* it mentions specifically that optional build dependencies are excluded
  from the platform policy.  Tools such as mypy don't affect the ability
  to build QEMU and move fast enough that distros cannot standardize on
  a single version of them (for example RHEL9 does not package them at
  all, nor does it run them at rpmbuild time).  In other cases, such as
  cross compilers, we have alternatives.

Right now, non-native dependencies have to be download manually by
running "pip" before "configure".  In the future, it will be desirable
for configure to set up a virtual environment and download them in the
same way that it populates git submodules (but, in this case, without
vendoring them in the release tarballs).

Just like with submodules, this would make things easier for people
that can afford accessing the network in their build environment; the
option to populate the build environment manually would remain for
people whose build machines lack network access.  The change to the
support policy neither requires nor forbids this future change.

[Thanks to Daniel P. Berrangé, Peter Maydell and others for discussions
 that were copied or summarized in the above commit message]

Cc: Markus Armbruster <armbru@redhat.com>
Cc: Peter Maydell <peter.maydell@linaro.org>
Cc: John Snow <jsnow@redhat.com>
Cc: Kevin Wolf <kwolf@redhat.com>
Reviewed-by: Daniel P. Berrangé <berrange@redhat.com>
Reviewed-by: Alex Bennée <alex.bennee@linaro.org>
Signed-off-by: Paolo Bonzini <pbonzini@redhat.com>

---
## [urlittlevenicebitch/NotAnotherServerCollumnsTheme](https://github.com/urlittlevenicebitch/NotAnotherServerCollumnsTheme)@[421db58612...](https://github.com/urlittlevenicebitch/NotAnotherServerCollumnsTheme/commit/421db58612f606a6bfeafe9bebe8509cddda37f9)
#### Saturday 2023-03-04 21:25:59 by urlittlevenicebitch

Removing ServerCollumns and custom icon

Removes the absolute fucking annoying ServerCollumns shit and removes the annoying anime girl icon (u fucking weeb)

---
## [Sea-of-Lost-Souls/Tannhauser-Gate](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate)@[f5e63175ec...](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate/commit/f5e63175eca40d65592b20a77df6025d1a3f9804)
#### Saturday 2023-03-04 21:30:19 by SkyratBot

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
## [JoeBidenWhatAreYouHiding/kx](https://github.com/JoeBidenWhatAreYouHiding/kx)@[307bcafdef...](https://github.com/JoeBidenWhatAreYouHiding/kx/commit/307bcafdef765c3c0072b70127294d4fd07a5069)
#### Saturday 2023-03-04 22:01:11 by JoeBidenWhatAreYouHiding

Greetings, Canadian citizen.  We are here to report an incident in which you participated in wrongspeak against the rightful monarch.  "I just think that maybe we should have a bit more freedom of press, is all."  Your Social Credit score has been reduced by -50. You are in warning of dropping to a C-Class Civilian & at risk of reduced Ration Tickets.  God save the King.

---
## [Fateussy/FateTranslations](https://github.com/Fateussy/FateTranslations)@[d6cbeb45f5...](https://github.com/Fateussy/FateTranslations/commit/d6cbeb45f516020b472afbdedc572455884af304)
#### Saturday 2023-03-04 22:12:34 by Fateussy

Gewman twanswation

One thing I don't know why
It doesn't even matter how hard you try
Keep that in mind, I designed this rhyme
To explain in due time
All I know
Time is a valuable thing
Watch it fly by as the pendulum swings
Watch it count down to the end of the day
The clock ticks life away
It's so unreal
Didn't look out below
Watch the time go right out the window
Tryin' to hold on, did-didn't even know
I wasted it all just to watch you go
I kept everything inside and even though I tried
It all fell apart
What it meant to me will eventually
Be a memory of a time when I tried so hard
I tried so hard and got so far
But in the end it doesn't even matter
I had to fall to lose it all
But in the end it doesn't even matter
One thing, I don't know why
It doesn't even matter how hard you try
Keep that in mind, I designed this rhyme
To remind myself how I tried so hard
In spite of the way you were mockin' me
Acting like I was part of your property
Remembering all the times you fought with me
I'm surprised it got so far
Things aren't the way they were before
You wouldn't even recognize me anymore
Not that you knew me back then
But it all comes back to me in the end
You kept everything inside and even though I tried
It all fell apart
What it meant to me will eventually
Be a memory of a time when I tried so hard
I tried so hard and got so far
But in the end it doesn't even matter
I had to fall to lose it all
But in the end it doesn't even matter
I've put my trust in you
Pushed as far as I can go
For all this
There's only one thing you should know
I've put my trust in you
Pushed as far as I can go
For all this
There's only one thing you should know
I tried so hard and got so far
But in the end it doesn't even matter
I had to fall to lose it all
But in the end it doesn't even matter

---
## [Unrated-Demon-List/unrated-demon-list](https://github.com/Unrated-Demon-List/unrated-demon-list)@[719c38afe1...](https://github.com/Unrated-Demon-List/unrated-demon-list/commit/719c38afe15720fbd19f9baffba91762ce510258)
#### Saturday 2023-03-04 22:33:06 by BreadDemon

List Movement march 4th, 2023

moved some levels, changelog here:
Rip It and In Abyss have swapped, with In Abyss on top.
Hyper Paradigmatic has been moved from #102 to #, Crystal Caverns has been moved from #118 to #, with Hyper Paradigmatic above Crystal Caverns and below Mystic Refractions, and Crystal Caverns above Eyre.
Sound wave destroyer has been moved from #119 to #, above Death Corridor Unner and below Ocular Miracle.
Theory of Darkness has been moved from #114 to #, above Old Sonic Wave and below CATNIVORES.
Night City has been moved from #103 to #, below Misty Downfall (Remake) and above C418. Highly subject to change, as in it should be lower so can someone play it so it can move down 🥺

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[14ba2bdada...](https://github.com/git-for-windows/git/commit/14ba2bdadad09a604dc0960c92738b9938547ee3)
#### Saturday 2023-03-04 22:34:56 by Johannes Schindelin

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
## [aaaa0ggMC/MineTerraria](https://github.com/aaaa0ggMC/MineTerraria)@[f868feefd4...](https://github.com/aaaa0ggMC/MineTerraria/commit/f868feefd4ea718f26c3ac6be1c4a244bf1110e2)
#### Saturday 2023-03-04 23:50:16 by aaaa0ggMC

Alpha 0.2

基础主世界地形生成 src/@terraria/overworld/gen.h （支持动态注册，但是目前未写进DLLInterface中，准备Alpha 0.9写一次DLLInterface,之后着手开发MineForge)

翻译生成 src/Translator.h .cpp
读取res/translations/中的所有文件并尝试建立翻译表，目前已处理许多地方，支持id访问，也许（没测试）支持多参，如：
Translate(storeIn,obj,"fuck.you","HAHAHA",time())
TranslateE(storeIn.obj,"fuck.shit","DEF");
以上两个都是宏，所以无法重载，只有宏才可以实现多参，不过TranslateE我打算拿函数代替，比较只有少中数情况才用到Translate带参

F3信息优化，包含更多信息了

---

