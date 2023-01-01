## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-12-31](docs/good-messages/2022/2022-12-31.md)


1,591,242 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,591,242 were push events containing 2,033,428 commit messages that amount to 117,044,159 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 58 messages:


## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[b174af7661...](https://github.com/MTandi/tgstation/commit/b174af7661cbfaf564292caabfccca18619bda23)
#### Saturday 2022-12-31 00:02:00 by Jacquerel

Basic Mob Carp Part VIII: Basic Mob Carp (#72073)

## About The Pull Request

Wow we're finally here. This turns carp into Basic Mobs instead of
Simple Animals.
They use a variety of behaviours added in previous PRs to act in a
marginally more interesting way than they used to.
But don't worry there's still 2 or 3 PRs to follow this one until I'm
done with space fish.

Changes in this PR:
Carp will try to run away if they get below 50% health, to make use of
their "regenerate if not attacked" component.
Magicarp have different targetting behaviour for spells depending on
their spell;
- Ressurecting Carp will try to ressurect allied mobs.
- Animating Carp will try to animate nearby objects.
- Door-creating Carp will try to turn nearby walls into doors.

You can order Magicarp to cast their spell on something if you happen to
manage to tame one.
The eating element now has support for "getting hurt" when you eat
something. Carp eating can rings and hating it was too soulful not to
continue supporting.

## Why It's Good For The Game

Carp are iconic beasts and I think they should be more interesting.
Also we just want to turn mobs into basic mobs anyway.

## Changelog

:cl:
add: Carp will now run away if their health gets low, meaning they may
have a chance to regenerate.
add: Lia will now fight back if attacked instead of letting herself get
killed, watch out!
balance: Magicarp will now aim their spells more intelligently.
add: Tame Magicarp can be ordered to use their spells on things.
refactor: Carp are now "Basic Mobs" instead of "Simple Mobs"
fix: Dehydrated carp no longer give you a bad feeling when they're your
friend and a good feeling when they're going to attack you.
balance: Tamed carp are now friendly only to their tamer rather than
their whole faction, which should make dehydrated carp more active.
Order them to stay or follow you if you want them to behave around your
friends.
/:cl:

---
## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[125745d232...](https://github.com/MTandi/tgstation/commit/125745d232163406c107d3947b87d6d406ac3a17)
#### Saturday 2022-12-31 00:02:00 by Fikou

guardian death checks (#72251)

## About The Pull Request
if a guardian summoner is dead during the summoner setting process, we
(the guardian) now kill ourselves since itd mean a guardian that cant
die
to combat some fucked upness of it (if you inject a guardian and it only
spawns after you died and then dusts you), the process of spawning a
guardian from the playerside guardian creator stuff gets canceled if
youre dead or dont exist

## Why It's Good For The Game
yeah that seems good

## Changelog
:cl:
fix: guardian spirits check for death before they add themselves to you
/:cl:

---
## [moltoretardo/cmss13](https://github.com/moltoretardo/cmss13)@[ab5f1fcb45...](https://github.com/moltoretardo/cmss13/commit/ab5f1fcb45311e9a4fff9f6250ec180207c6271e)
#### Saturday 2022-12-31 00:11:00 by carlarctg

Fixed entering APC being 0.1 seconds instead of 1 (#2117)

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
Fixed entering APC being 0.1 seconds instead of 0.5

It had '1' instead of '1 SECONDS'. This isn't intentional because of the
outdated comment and as stated below

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

Sometimes bugs and oversights are elevated into features, this is
effectively one but in practice it means that marines have way too much
freedom of movement and versatility entering it, it's less like a
clunky, bulky, cassettepunk APC and more like a Ferrari convertile. It
also allows them to instantly enter the APC while being killed by a
Xeno, which is stupid and lame.

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
fix: Fixed entering APC being 0.1 seconds instead of 1 second.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [Hatterhat/tgstation](https://github.com/Hatterhat/tgstation)@[e9cff525dc...](https://github.com/Hatterhat/tgstation/commit/e9cff525dc5b57153af3b4bb9039de08d6823805)
#### Saturday 2022-12-31 00:15:40 by tralezab

Refactors Pirates into Pirate Gangs, Adds the Psyker-gang as new pirates (#71650)

## About The Pull Request

### Refactor
Pirate gangs are now datumized for extendability, custom dialogue, etc.

### Psyker Gang 🧠 
Psyker-gang Members are pirates who are... yes, Psykers. They're on a
gore-binge and need some money for more hits of gore!

- Gore autoinjectors, filled with dirty kronkaine. Don't overdose,
you'll go splat.
- Psykerboost armor, reactive armor that refreshes psychic abilities.
Given to the leader.

- [x] @Fikou is making the map :D

## Why It's Good For The Game

God I fucking love variety also now we can add as many different pirates
as we so desire

<details>
  <summary>Spoiler warning</summary>
  

![image](https://user-images.githubusercontent.com/40974010/205342701-9cba63ef-a22c-4f07-9b48-8793c4a2b5af.png)
  
</details>

## Changelog
:cl: Tralezab code, Fikou's map, PigeonVerde and Halcyon for sprites!
add: Psyker-gangers are new pirates
refactor: refactored pirate code so we can add more in the future
/:cl:

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [Hatterhat/tgstation](https://github.com/Hatterhat/tgstation)@[ebc0227176...](https://github.com/Hatterhat/tgstation/commit/ebc0227176b5213f379eefc3f5c6aa7be2d09c0a)
#### Saturday 2022-12-31 00:15:40 by Tastyfish

Makes dog a basic mob [MDB IGNORE] (#70799)


About The Pull Request

    Made a basic version of the pet base called /mob/living/basic/pet. It's significantly more stripped down from the old simple_animal one, because its half collar stuff and...

    Made the collar slot a component that you could theoretically remove from a pet to disable the behavior, or add to any other living mob as long as you set up the icon states for the collar (or not, the visuals are optional).
        The corgi's collar strippable slot is now generally the pet collar slot, and in theory could be used for other pet stripping screens.

    I also gutted the extra access card code from /mob/living/basic/pet as it's only being used by corgis. Having a physical ID is now just inherent to corgis, as they're the only ones that could equip it anyway.

    Ported the make_babies() function from simple_animals to a new subtree and associated behavior, called /datum/ai_planning_subtree/make_babies that uses blackboards to know the animal-specific info.
        Note that it's marginally improved, as the female walks to the male first instead of bluespace reproduction.

    Tweaked and improved the dog AI to work as a basic mob, including making /datum/idle_behavior/idle_dog fully functional.

    Made a /datum/ai_planning_subtree/random_speech/dog that pulls the dynamic speech and emotes to support dog fashion.

I've tested base collars across multiple pet types.

For dogs, I've tested general behavior, fetching, reproduction, dog fashion, and deadchat_plays, covering all the oddities I'm aware of.

image
Why It's Good For The Game

Very big mob converted to a basic mob.
Changelog

cl
fix: Lisa no longer uses bluespace when interacting with Ian.
refactor: A large portion of dog code was re-written; please report any strange bugs.
/cl

---
## [appwiz/apollo-server](https://github.com/appwiz/apollo-server)@[3fd7b5f261...](https://github.com/appwiz/apollo-server/commit/3fd7b5f26144a02e711037b7058a8471e9648bc8)
#### Saturday 2022-12-31 00:59:58 by Trevor Scheer

Update `@apollo/utils.keyvaluecache` dependency (#7187)

Previous releases of the `@apollo/utils.keyvaluecache` package
improperly specified the version range for its `lru-cache` dependency.

Fresh installs of our packages should receive the patch update since
it's careted, so this issue can be worked around by forcing the update
if you're using a lockfile. We should update it anyway since `2.0.0` is
invalid.

<!--
First, 🌠 thank you 🌠 for taking the time to consider a contribution to
Apollo!

Here are some important details to follow:

* ⏰ Your time is important
To save your precious time, if the contribution you are making will take
more
than an hour, please make sure it has been discussed in an issue first.
          This is especially true for feature requests!
* 💡 Features
Feature requests can be created and discussed within a GitHub Issue. Be
sure to search for existing feature requests (and related issues!) prior
to
opening a new request. If an existing issue covers the need, please
upvote
that issue by using the 👍 emote, rather than opening a new issue.
* 🔌 Integrations
Apollo Server has many web-framework integrations including Express,
Koa,
Hapi and more. When adding a new feature, or fixing a bug, please take a
peak and see if other integrations are also affected. In most cases, the
fix can be applied to the other frameworks as well. Please note that,
since new web-frameworks have a high maintenance cost, pull-requests for
new web-frameworks should be discussed with a project maintainer first.
* 🕷 Bug fixes
These can be created and discussed in this repository. When fixing a
bug,
please _try_ to add a test which verifies the fix. If you cannot, you
should
still submit the PR but we may still ask you (and help you!) to create a
test.
* 📖 Contribution guidelines
Follow
https://github.com/apollographql/apollo-server/blob/main/CONTRIBUTING.md
when submitting a pull request. Make sure existing tests still pass, and
add
          tests for all new behavior.
* ✏️ Explain your pull request
Describe the big picture of your changes here to communicate to what
your
pull request is meant to accomplish. Provide 🔗 links 🔗 to associated
issues!

We hope you will find this to be a positive experience! Open source
contribution can be intimidating and we hope to alleviate that pain as
much as possible. Without following these guidelines, you may be missing
context that can help you succeed with your contribution, which is why
we encourage discussion first. Ultimately, there is no guarantee that we
will be able to merge your pull-request, but by following these
guidelines we can try to avoid disappointment.
-->

---
## [Evolution-X-Devices/device_oneplus_sm8350-common](https://github.com/Evolution-X-Devices/device_oneplus_sm8350-common)@[5482af319e...](https://github.com/Evolution-X-Devices/device_oneplus_sm8350-common/commit/5482af319e76d4fa50d0047cbd93df5505fb751c)
#### Saturday 2022-12-31 01:10:47 by AnierinB

sm8350-common: Force disable a2dp for now

Fuck you qpr1!

Signed-off-by: AnierinB <anierin@evolution-x.org>

---
## [jakewilliami/advent-of-code](https://github.com/jakewilliami/advent-of-code)@[004d719e47...](https://github.com/jakewilliami/advent-of-code/commit/004d719e47ed9503b09ab60a57c30df608ecb1c9)
#### Saturday 2022-12-31 01:19:15 by Jake Ireland

Add summary of solutions to early AoC days of 2022

After the 13th, I realised that it was annoying when I was looking
back at old AoC solutions but couldn't for the life of me remember
what any of the code did or why, and I didn't want to have to load up
the AoC website for that day of the previous years and read the
description there to find out what it was.  Hence, I started writing
short summaries of the problems, and a quick description of my
solution, and any other worthwhile notes.  As I only started doing
this after the 13th, I retrospectively add these notes/summaries in
this commit.

---
## [christiands/c-cpp-blender](https://github.com/christiands/c-cpp-blender)@[c198daa7c5...](https://github.com/christiands/c-cpp-blender/commit/c198daa7c5a2fcb4395b717153371e6263f671fb)
#### Saturday 2022-12-31 01:20:20 by Christian Scott

oh boy I just love abusing the preprocessor
it's basically a hobby at this point
funny thing is, this actually kinda looks like a library that would be
released

---
## [i3roly/CMI8788](https://github.com/i3roly/CMI8788)@[154ac08c6d...](https://github.com/i3roly/CMI8788/commit/154ac08c6dcfdd81d0de2be3426436f246dfb188)
#### Saturday 2022-12-31 01:43:44 by gagan sidhu

happy to be wrong but: OSX does not have a *fully* functional PCI API, fr Tim Cook went FULL <YOU KNOW WHAT>

i'm going to preface my findings with this statement: i am happy to be wrong. please show me what i'm not seeing.

APPUL offers like, three variants that wrap around this in some shitty fashion, using a different kind of memory addressing:
	-pciDevice->{extended}config{Read,Write}{8,16,32} (closest to what we want)
	-pciDevice->io{Read,Write}{8,16,32} (an inferior version of IOMapped{Read,Write}{8,16,32})

	-i have looked at various implementations:
		-the esteemed VoodooHDA tries to directly write/read to the address returned by ->getVirtualAddress() (https://github.com/CloverHackyColor/VoodooHDA/blob/main/branches/zdev/VoodooHDADevice.cpp#L1064)
			-this is unsafe and, from what i tried, does not work.
	-i have also looked at "Envy24HT", which tries to use the ioWrite{8,16,32}(https://github.com/fredemmott/Envy24HT/blob/master/AudioDevice.cpp#L469)

-after some very stringent evaluations over the past two days i have learned the following:
	-pciDevice->{extended}Config{Read,Write}{8,16,32} will work for rudimentary things, but when you go outside of reading vendor IDs or those pre-defined macros defined by APPUL, it is VERY unreliable.
		-for example i've had it successfully write the memory address for some of the streams, but not others (wtf?)
	-IOMapped{Read,Write}{8,16,32} makes you *think* it's being done, but it's not.

i discovered IOMapped is a fraud by using the CMedia documentation:
	-*if* we truly wrote to the OXYGEN_INTERRUPT_MASK,
		-*then* the OXYGEN_INTERRUPT_STATUS should be non-zero.

BUT, in spite of IOMappedRead16 returning the right value from OXYGEN_INTERRUPT_MASK, IOMappedRead16 OXYGEN_INTERRUPT_STATUS returns ZERO.
	-this means whatever we have written via IOMapped (or config, or io, whatever) is not being received by the device
		-if it was being sent, then the value for the interrupt status should not be zero.

- there's only one way to truly guarantee your data is getting written/read from configuration space: read/write{b,w,l}.
	- i should have known yesterday when this didn't work properly, that APPUL has been fucking up for some time now.

what's funnier is these fucking PUNKS are so fucking NECK DEEP in SHITE they've rolled out PCI "API"s and deprecated them within one OS release:
	-check out pciDevice->Memory{Read,Write}{8,16,32} : introduced in 10.15.3 and deprecated in macOS11 (https://developer.apple.com/documentation/kernel/iopcidevice/3516641-memoryread16)

hahahahahahaa these fucking FULL-GOOF <YOU KNOW WHAT> let me tell you WOW.
	-and this fucking combover cunt <YOU KNOW WHAT> thinks he can roll out an ARM-based Mac PRO with PCI slots that fucking work?
		- is this a fucking joke? REALLY? IS THIS A JOKE?

THE LINUX GUYS ARE FUCKING LAUGHING SO HARD RIGHT NOW
	"hahaha what a fool! he expected APPUL to have a full-featured, functional PCI API hahaha".

i bet all the fucking germans are fucking fist slamming the surface upon which they're rolling with laughter, tears coming down, reading my discovery. and they know this is what's been going on for the the past 15-20 years.

fat fucking greedy bitch
winfrey known for being rich
top bitch top cheese
cuffin' pads for TIMMAY' kneez

hustled these mac devs
all app makers-all whatevs
read/write{b,w,l} broken
no more hopin'

top bitch had to get paid
now she stayin' made
APPUL devs gettin' played
to do PCI anyway.

DriverKit and PCI ROFL don't make me FUCKING LAUGH okay. fucking joke.

in spite of being angry by APPUL's blatant scamming, i still love you ben!

https://www.youtube.com/watch?v=X6WHBO_Qc-Q

---
## [SameepAher/zulip](https://github.com/SameepAher/zulip)@[23a776c144...](https://github.com/SameepAher/zulip/commit/23a776c1448da18b906529e5951e24d8d58a7e81)
#### Saturday 2022-12-31 01:57:33 by Mateusz Mandera

maybe_send_to_registration: Don't reuse pre-existing PreregistraionUser.

There was the following bug here:
1. Send an email invite to a user.
2. Have the user sign up via social auth without going through that
   invite, meaning either going via a multiuse invite link or just
   straight-up Sign up if the org permissions allow.

That resulted in the PreregistrationUser that got generated in step (1)
having 2 Confirmations tied to it - because maybe_send_to_registration
grabbed the object and created a new confirmation link for it. That is a
corrupted state, Confirmation is supposed to be unique.

One could try to do fancy things with checking whether a
PreregistrationUser already have a Confirmation link, but to avoid races
between ConfirmationEmailWorker and maybe_send_to_registration, this
would require taking locks and so on - which gets needlessly
complicated. It's simpler to not have them compete for the same object.

The point of the PreregistrationUser re-use in
maybe_send_to_registration is that if an admin invites a user, setting
their initial streams and role, it'd be an annoying experience if the
user ends up signing up not via the invite and those initial streams
streams etc. don't get set up. But to handle this, we can just copy the
relevant values from the pre-existing prereg_user, rather than re-using
the object itself.

---
## [ichard26/black](https://github.com/ichard26/black)@[0019261abc...](https://github.com/ichard26/black/commit/0019261abcf6d9e564ba32d3cc15534b9026f29e)
#### Saturday 2022-12-31 02:35:25 by Richard Si

Update stable branch after publishing to PyPI (#3223)

We've decided to a) convert stable back into a branch and b) to update
it immediately as part of the release process. We may as well automate
it. And about going back to a branch ...

Git tags are not the right tool, at all[^1]. They come with the
expectation that they will never change. Things will not work as
expected if they do change, doubly so if they change regularly. Once
you pull stable from the remote and it's copied in your local
repository, no matter how many times you run git pull you'll never see
it get updated automatically. Your only recourse is to delete the tag
via `git tag -d stable` before pulling.

This gets annoying really quickly since stable is supposed to be the
solution for folks "who want to move along as Black developers deem
the newest version reliable."[^2] See this comment for how this impacts
users using our Vim plugin[^3]. It also affects us developers[^4]. If
you have stable locally, once we cut a new release and update the stable
tag, a simple `git pull` / `git fetch` will not pull down the updated
stable tag. Unless you remember to delete stable before pulling, stable
will become stale and useless.

You can argue this is a good thing ("people should explicitly opt into
updating stable"), but IMO it does not match user expectations nor
developer expectations[^5]. Especially since not all our integrations
that use stable are bound by this security measure, for example our
GitHub Action (since it does a clean fetch of the repository every time
it's used). I believe consistency would be good here.

Finally, ever since we switched to a tag, we've been facing issues with
ReadTheDocs not picking up updates to stable unless we force a rebuild.
The initial rebuild on the stable update just pulls the commit the tag
previously pointed to. I'm not sure if switching back to a branch will
fix this, but I'd wager it will.

[^1]: https://git-scm.com/docs/git-tag#_on_re_tagging

[^2]: https://black.readthedocs.io/en/stable/contributing/release_process.html#moving-the-stable-tag

[^3]: https://github.com/psf/black/issues/2503#issuecomment-1196357379

[^4]: In fairness, most folks working on Black probably don't use the
      `stable` ref anyway, especially us maintainers who'd know what is
      the latest version by heart, but it'd still be nice to make it
      usable for local dev though.

[^5]: Also what benefit does a `stable` ref have over explicit version
      tags like `22.6.0`? If you're going to opt into some odd pin
      mechanism, might as well use explicit version tags for clarity
      and consistency.

---
## [ArcadeDan/roguelike](https://github.com/ArcadeDan/roguelike)@[9caa8a0b56...](https://github.com/ArcadeDan/roguelike/commit/9caa8a0b5620c2cbd61d9c506536fc4f00e74d49)
#### Saturday 2022-12-31 03:04:28 by dan

why the hell does it panic blah blah blah out of bounds fuck you

---
## [av14149/render](https://github.com/av14149/render)@[a9cf6f1882...](https://github.com/av14149/render/commit/a9cf6f1882843771a473bbf670a5209687f0e471)
#### Saturday 2022-12-31 03:29:21 by Aadish Verma

+ Added User-Friendly File Org & README
This redesign of Render was meant to be user–friendly, removing the complex file system and adding a README (albeit with very limited info, just an overview).
More docs coming soon.
We are working on the next version of Render. After running some tests, if more speed and optimizations are needed, then that will become Render v2.0.1. Otherwise, we may move straight to adding more shapes and improving the developer experience (mainly ViewRenderer upgrades) for Render v2.1.0.
And design changes are already underway from Render v3.0.0 (aka DynamicRender)!
Currently there's only 1 person (and a 11-year-old in 6th grade, for that) working on this project, so expect the next version of v2 to come out by mid-January.
I wish you all the best in trying out Render. Please remember that it is nowhere close to production, expect that in Render 3.0 or 4.0.

---
## [artvin01/TF2-Zombie-Riot](https://github.com/artvin01/TF2-Zombie-Riot)@[646650b086...](https://github.com/artvin01/TF2-Zombie-Riot/commit/646650b086ad82d70823da3bb24fc69578565836)
#### Saturday 2022-12-31 05:20:16 by jDeivid

oops (#116)

* oh look, billion's of hp no more

* Tornado-Blitz

If only tf2 didn't have a projectile limit

* Update zombieriot.phrases.weapons.description.txt

* Slight tornado-blitz adjustments

* funny changes

* A tripple

meem, gun, fistman

* aaaaaaa

* ah fuck

---
## [SomeRandomOwl/Skyrat-tg](https://github.com/SomeRandomOwl/Skyrat-tg)@[ae02bd97ff...](https://github.com/SomeRandomOwl/Skyrat-tg/commit/ae02bd97ff71d2f4714b4ea7c8076acf21ed06c6)
#### Saturday 2022-12-31 06:43:09 by OrionTheFox

Gunset case resprite (#18119)

* Noice Icons

* smol

* ccode 4 icon

* Fuck it. We Webedit.

* Oh this should go too

* i hate commas anyways

Co-authored-by: Tom <8881105+tf-4@users.noreply.github.com>

Co-authored-by: Tom <8881105+tf-4@users.noreply.github.com>

---
## [gy1ta23/oic](https://github.com/gy1ta23/oic)@[301b85664c...](https://github.com/gy1ta23/oic/commit/301b85664c00d8e36fee2d74e0e5d0f5d5e77f8e)
#### Saturday 2022-12-31 06:44:08 by gy1ta23

potted plants; our friends


potted plants; our friends


potted plants; our friends


potted plants; our friends


potted plants; fixing our friends (on their away maps)


potted plants; our (poorly indentated) friends


for the love of god stop failing checks


potted plants; our friends (dreammaker is not a friend)


fuck you, old-lab 2


green's replacement


potted plants; our friends (against whitespace)

---
## [axietheaxolotl/tgstation](https://github.com/axietheaxolotl/tgstation)@[fccd833526...](https://github.com/axietheaxolotl/tgstation/commit/fccd833526364b131ce440b4ab0e65022103927c)
#### Saturday 2022-12-31 06:46:39 by GoldenAlpharex

Fishing Odds Code Improvements and Rescue Hooks (#71415)

## About The Pull Request
I wanted to try and implement an easier way for people to fish out
corpses from chasms, as I heard many tales of people trying to fish
others out of chasms and it taking over one IRL hour, with some cases
where it would take over two hours. Obviously, that's not really
interesting gameplay, and it doesn't really give people an incentive to
fish, it just turns it into an annoyance that people won't want to do
for fun. Now, we don't want that, do we?

As such, I've created the rescue hook, a special fishing hook that can
only be used in chasms (as that's currently the only place you can find
people into), which will only be able to fish out duds, skeleton
corpses, any mob that's fallen into a chasm and hasn't been rescued yet,
or rarely, a hostile monster lurking below. It has, at the time of
writing this, a weight of 5 (50 without bait, lower with bait) for duds
and a weight of 30 for chasm detritus, which themselves have a 50%
chance to be a random skeleton corpse, or a lobstrosity, and the
remaining 50% chance of fishing out a mob that's fallen into a chasm.
I'm open to tweaking these values if we think it's too easy or too hard,
but it's still a rather expensive item, so I'd consider it quite fine
the way it is myself, as it's still not risk-free.

It's currently only obtainable through buying it from cargo in the
goodies section, at a default price of 600 credits (making it
SIGNIFICANTLY more expensive than the rest of the fishing content, and
making it something that assistants will have to put some elbow grease
into if they want to be able to afford it).

As it stands currently, it can't be used to recover the fallen's
belongings that weren't on their person (i.e., their crusher if they
were holding it in hands), ~*but* I'm down to make that easier to fish
out using, for instance, the magnet hook, while also making it
incompatible with fishing out bodies, which would make it a nice way to
recover those lost items without spending over an hour fishing for them,
if that's something that maintainers would want.~ Maintainers did want
it, and as such...

The Magnetic hook is now the go-to hook to retrieve objects from chasms!
Not only does it inherently do a much better job at fishing out
non-fishes, it also has a lesser chance of retrieving random junk from
chasms, and an even lower chance of fishing out lobstrosities!

I also improved the code for the fishing weights calculation so that the
hooks and the rods can have an effect on the odds of certain types of
rewards more easily, with the option of offloading a more of what's
currently being calculated on `fishing_challenge` over on the rods or
even the hooks themselves.

I finished by fixing a handful of capitalization and punctuation issues
in various fishing items, as that bugged me when I was testing my
changes.

## Why It's Good For The Game
Corpses being recoverable from chasms was a great idea, however making
it so people would have to sink a major portion of their shift for a
chance at recovering a corpse doesn't create a particularly interesting
gameplay loop. However, being able to spend your hard-earned funds in
order to streamline that process without really being able to use that
to cheese other mechanics sounds like a great deal to me.

## Changelog

:cl: GoldenAlpharex
add: Added a Rescue Hook, that will allow the fishing rod it's attached
onto to become a lot more proficient at recovering corpses from chasms,
at the expense of making it unusable for more traditional fishing. It
isn't entirely lobstrosity-proof, however...
balance: The magnetic hook can no longer fish out corpses from chasms,
but will fish out items much more efficiently than any other hooks,
while also being much less attractive to lobstrosities. Some still fall
for it regardless, however.
spellcheck: Fixed the capitalization and punctuation in the description
of multiple fishing accessories.
code: Improved the code for fishing weights, to allow for different
hooks to have some more noticeable results on the weights without having
to add to an already massive proc.
/:cl:

---
## [mattdway/CreateWithVR](https://github.com/mattdway/CreateWithVR)@[04645b333a...](https://github.com/mattdway/CreateWithVR/commit/04645b333a9a43012a8793cd0d2adac33ba8d55b)
#### Saturday 2022-12-31 07:53:01 by mattdway

12-31-22 Commit v2.8.2

12-31-22 v2.8.2
12-31-22 Commit
Up next to fix:

These four clock pieces have been fixed.

1.) The clock socket has been fixed.  This was a combination of the socket's Interaction Layer Mask settings to include the clock, the positioning of the socket on the wall (it needed to come forward away from the wall just a tad) and adjusting the rotation of the socket on the wall (180, 180, 180) so that when the clock did socket it didn't socket to the outside of the wall.  Adjustining these three pieces allowed the clock to socket to the wall without any further issue.

2.) I also adjusted the LeftHand Ray and Righthand Ray Interaction Layer Mask to include the clock and to exclude Art.  This way the art could not be picked up via raycast (I tested and this did cause a lot of distruction when calling for the large painting from across the room -- anything it hit between its original position and my position went flying) and so that I could grab the clock from afar.

This was also a great reminder to be sure to update these Interaction Layer Masks (as these are not set to Everything) whenever a new item has been added to the room otherwise these won't be able to be picked up via distance grabbing.  I checked and all items that should be able to be grabbed with distance grabbing can be and anything not able to be grabbed by distance grabbing: the doors, the drawer and the art) cannot.

3.) I rebaked my lighting to get rid of the static shadow behind the clock, now that the clock is dynamic and is able to be grabbed.

To do this, I adjusted my lighting to make sure that every light in my room (minus the flashlight) were set to baked.  This includes: Chandellers, Entire_Room_Point_Light (which I had thought was legacy and should be set to real time and disabled but in doing this I found out that most of my room was in shadows, so I changed this back to baked and rebaked my lighting for my room to correct), Outside_Directional_Light, Fireplace_Modern, Lamp_Floor_Double, Lamp_Table_Red and Sconces.

I also went through and made sure that all of my "-- STATIC --" and all of my "-- STATIC INTERACTIVE --" and that all of my "-- LIGHTS --" game objects were set to "Static" in the inspector, to the right of each game object's name.  Under "-- DYNAMIC --" I also checked that nothing there was set to static with the exception of these items:

Under "-- DYNAMIC --" > "Cabinets" > the following items were set to static:
"Cabinet With Drawer"
"Left side panel"
"Shelf"
"Top"
"Right side panel"
"Bottom panel"

"Door and "Drawer" do not have the "Static" checkmark, however, since those objects are grabable and are ment to move.

Under "-- DYNAMIC --" > "Cabinets" > "Cabinets With Two Doors" > "Cabinet_Modern_Left" and "Cabinet_Modern_Right" the following items were set to static:
"Cabinet_Body"

"Cabinet_Door_Left" and "Cabinet_Door_Right" and their child object "Handle" do not have the "Static" checkmark, however, since those objects are grabable and are ment to move.

I used the trick of searchingi for t:light in the Hierarchy search bar to expose all the lights, I then used "Ctrl" + "A" to select all, I held down the "Ctrl" key and then single left-clicked on "Lightsource_FLashlight_Yellow_Spot Light" and then in the "Inspector" pane under "Light" I changed the "Mode" parameter from "Realtime" to "Baked."
Then, under the "Lighting" tab or "Windows" > "Rendering" > "Lighting" I single left-clicked on the "Generate Lighting" button to render a new lightmap.

I made the mistake of under the "Lighting" tab > "Enviorment" > "Skybox Material" of having the "MegaSun" skybox selected.  When baking a lightmap the lightbox light color and reflection colors are included and this gave a very washed out orange tint to everything in my lightmap.  To fix this I had to temporarily change the "Skybox Material" back to "Sky-Default" then rebaking my lightmap again.  After this baked I then changed the "Skybox Material" back to my "MegaSun" skybox, of choice.

4.) I fixed the roation on of the clock when picking it up.  I had to go into "Edit" > "Project Settings" > "Physics" and I had to disable the physics interactions for both "Clock/Clock" and "Clock/Pseudo Body" so that the clock couldn't interact with either.  Once set this object rotated as normal.  I also doublechecked that "Smooth Position" and "Smooth Rotation" were both checked in the "XR Grab Interactable" component settings.  They were.

I turned off raycast distance grabbing for all objects of the "Art" layer.  Due to the large size of this art and its collisions this caused too many issues distance grabbing from across the room.  Art must be grabbed using "Direct Interactable", now, only.

I moved the dinning room chairs and the hidden teleportation anchor mats back so that it is easier to climb onto the chairs to climb onto the table to reach the shelf where the record player, record, and books live.  From this vantage point players can also directly reach the clock and the painting, if they so wish.

I moved the "Measuring Stick" game object from static to "-- DYNAMIC --" as this is a grabable object and this is where this should live.  The "Measuring Stick" is a disabled game object used as a quick referene for sizing objects to all be the same.  Yesterday I changed the height of this measuring stick to 0.3048 meters, which is 12 inches.  The same length of a standard ruler.

I also updated the version number and the commit date on the Welcome Menu screen.

To Fix Next:

Writing a script for the Water Bottle Flip Challenge to detect when there is a floor collision with either the top, sides or bottom and to play a corresponding sound when that happens.

Determine if there is a good solution for the character controller colliding with the cabinet doors when leaning forward.

Determine why my physics hands can clip through the dinning room table and chairs when at a fast enough speed.  Try and make this work more like the couch or outside colliders.  Test with other furniture to see if anything else in the room allows this to happen.  Compare and contrast to troubleshoot.

Thin items like photos from the polaroid camera and my punch list sheets are still sometimes getting stuck under the floor and I need to troubleshoot that more to try and fix.

Updating the Interactive board and/or punch lists.  I'm running out of room on my punch lists and I have no more room to add additional punch lists, so I'll have to decide how I wish to use these moving forward.  I still love the idea of having bugs and/or future features viewable in VR and I have a lot of future ideas (both from ideas I've come up with and that my students have come up with that could be added).

If I get that working I feel like I have a lot of the bug pieces for all the current items added to my room fixed.  I'll have to go back to my bug list to check to be sure, but off the top of my head there aren't any others that are coming to mind that I need to fix.  At this point I may choose a new feature to add to this room, just to continue my (and my student's) learning.
@mattdway
mattdway committed on Dec 31

---
## [K-C-DaCosta/ph-assign-2](https://github.com/K-C-DaCosta/ph-assign-2)@[508af7b0ae...](https://github.com/K-C-DaCosta/ph-assign-2/commit/508af7b0aebd8fd79b5907b46725799c3fa13030)
#### Saturday 2022-12-31 07:59:20 by k-c-dacosta

Creating Test Stage

In order to test mutation recording I need Insert,Delete, Record,
and Export tools. This commit sets the foundation for implementing
those tools.

I've thought about it ALOT and I believe I have a good way of
recording the mutation history. I kinda hate javaScript though. I want
to do some entropy encoding or something but from the looks of it
JS is not the best language for doing raw data manipulation in. A WASM
module for compression is probably Ideal, but I don't wanna spend
too much time on this assignment honestly.

---
## [sunset-wasteland/sunset-wasteland](https://github.com/sunset-wasteland/sunset-wasteland)@[1f15689fe0...](https://github.com/sunset-wasteland/sunset-wasteland/commit/1f15689fe0eeb42ab1a80e863177732920065d3e)
#### Saturday 2022-12-31 08:28:17 by ProbablyCarl

Demolitions & Rockets
- - -
Balance:
 - Mech rockets corrected. They weren't meant to be firing HE. Whoops.
 - Legion Demolitions given a proper explosive grenade.
   - HE given to Demolitions has also been made a crafting option.
 - Enclave roles with grenades given the appropriate F13 item.
 - Brotherhood has lost access to the L30, alongside the tribeam. The latter because it was a redundant choice and sandwiched between two far superior options.
- - -
Map:
 - Heaven's Night and general Pahrump modifications in line with internal discussions.
- - -

---
## [Call-Me-Doc/origins_lore_](https://github.com/Call-Me-Doc/origins_lore_)@[2da25f2e96...](https://github.com/Call-Me-Doc/origins_lore_/commit/2da25f2e9636d7762c639a280cb5507a159e19b7)
#### Saturday 2022-12-31 08:43:31 by Call-Me-Doc

colour and links

added some links, added colour, fuck you.

---
## [NSU-FIT-Operating-Systems/20201-POSIX-Threads](https://github.com/NSU-FIT-Operating-Systems/20201-POSIX-Threads)@[4c2d00ecee...](https://github.com/NSU-FIT-Operating-Systems/20201-POSIX-Threads/commit/4c2d00ecee6c814524f02de59d24f60a08217b63)
#### Saturday 2022-12-31 09:51:55 by Alexander Yanin

a.yanin/common: Create a new common module `loop`

After prolonged deliberation, I've decided to create a simple event loop
that would support async TCP socket operations.

The event loop design is directly inspired by libuv,
with a few minor differences.

- the extensive use of the `error` and `log` modules because I don't
  care about other people's use-cases

- fearless memory allocations (since I've kept avoiding them for some
  reason while having a machine with 16 GiB of RAM)

- `poll` instead of the clearly superior `epoll` because POSIX...
  at least it's not `select`, duh.

- the extensible handler interface
  - they'll be responsible for juggling callbacks

- a decoupled executor interface (now that I think of it, it looks
  really similar to Java's executors... that's scary.)

I'm still thinking where to put the I/O operations in this picture
so that they wouldn't be a royal pain.

The goal is to have an overwhelmingly large part of the codebase shared
among the 31st and 33rd labs; the only difference there being
a different choice of the executor (single-threaded vs thread pool).

And since I anticipate (and actively hope) that this will be my last
grand effort writing code in C, I'm going extravagant with my designs.
To the detriment of the poor people who'll have to review this.
To them I say this: I'm not sorry at all.

---
## [vincentiusvin/tgstation](https://github.com/vincentiusvin/tgstation)@[eb6c0eb37c...](https://github.com/vincentiusvin/tgstation/commit/eb6c0eb37c095c188074c7cec98bf5bf36a2cf04)
#### Saturday 2022-12-31 09:58:42 by Jacquerel

Dogs use the Pet Command system (#72045)


About The Pull Request

Chiefly this refactors dogs to use the newer component/datum system for "pet which follows instructions". It also refactors it a little bit because I had better ideas while working on this than I had last week. Specifically, instead of passing around keys we just stick a weakref to our currently active behaviour in the blackboard. Basically the same but skipping an unecessary step.

Additionally it adds a component for the previous "befriending a mob by clicking it repeatedly" behaviour which hopefully we won't use too much because it's not very exciting (I am planning on replacing it for dogs some time after Christmas).
The biggest effort in here was making the Fetch command more generic, which includes multiple behaviours (which might be used on their own?) and another component (for holding an item without hands).

Additionally I noticed that dogs would keep following my instructions after they died.
This seems unideal, and would be unideal for virtually any AI controller, so I added it as an AI_flag just in case there's some circumstance where you do want to process AI on a dead mob.

Finally this should replicate all behaviour Ian already had plus "follow" (from rats) and a new bonus easter egg reaction, however I noticed that the fetch command is supposed to have Ian eat any food that you try to get him to fetch.
This has been broken for some time and I will be away from my desk for a couple weeks pretty soon, so I wrote the behaviour for this but left it unused. I will come back to this in the future, once I figure out a way to implement it which does not require adding the "you can hit this" flag to every edible item.

Also I had to refit the recent addition of dogs barking at felinids to fit into this, with a side effect that now dogs won't get mad at a Felinid they are friends with. This... feels like intended behaviour anyway?
Why It's Good For The Game

It's good for these to work the same way instead of reimplementing the same behaviour in multiple files.
Being able to have Ian (or other dogs) follow you around the station is both fun and cute, and also makes him significantly more vulnerable to being murdered.
Changelog

cl
add: Ian has learned some new tricks, tell him what a good boy he is!
add: Ian will come on a walk with you, if you are his friend.
refactor: Ian's tricks work the same way as some other mobs' tricks and should be extendable to future mobs.
fix: Dogs no longer run at the maximum possible speed for a mob at all times.
add: When Ian gets old, he also slows down. Poor little guy.
add: Dogs will no longer dislike the presence of Felinids who have taken the time to befriend them.
/cl

---
## [ShelbyHell/android_kernel_samsung_a31-1](https://github.com/ShelbyHell/android_kernel_samsung_a31-1)@[4ba3ebfe9d...](https://github.com/ShelbyHell/android_kernel_samsung_a31-1/commit/4ba3ebfe9d8cb2fdf47ddb09aff45c500bc03f97)
#### Saturday 2022-12-31 10:24:01 by Peter Zijlstra

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

---
## [TheNeoGamer42/Skyrat-tg](https://github.com/TheNeoGamer42/Skyrat-tg)@[b922aef977...](https://github.com/TheNeoGamer42/Skyrat-tg/commit/b922aef97718aeffc0d3b450012575df2d065e20)
#### Saturday 2022-12-31 10:25:13 by SkyratBot

[MIRROR] Adds Some Supermatter Effects  [MDB IGNORE] (#17734)

* Adds Some Supermatter Effects  (#67866)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

This pull request adds a variety of Supermatter delamination effects to
make the crystal a bit more fun to watch and stare at. The initial
filter effects and animations are from Baystation12, but I have adapted
it to make it fun to watch!

It'll be a bit hard to explain in text, so this is the text explanation.

For normal running conditions, the Supermatter will emit pretty golden
rays, and a large campfire like that glow that grows and shrinks based
on it's power level.

![dreamseeker_vnw1BL7DNy](https://user-images.githubusercontent.com/77420409/174471609-7be70234-5eae-4839-b551-1c28145d6b60.gif)

For high power conditions, such as high O2 or CO2 amounts, the
Supermatter's rays will glow red and it will emit red light, aswell as
turn red (like before, unchanged).

https://user-images.githubusercontent.com/77420409/174471693-e191ee47-1a01-4b76-8570-9d12b994c2d4.mp4

When the conditions for a cascade, singularity, or a tesla are met, the
colours and rays emitting from the crystal will change to match!

https://user-images.githubusercontent.com/77420409/174471747-dffb3beb-dd38-42a1-a97b-7262dabd60af.mp4

https://user-images.githubusercontent.com/77420409/174471765-af1927e8-a48e-4fd5-a35c-6b3aa53c5add.mp4

Also, I've added more sucking power to the crystal during its final
countdown for DRAMATIC EFFECT. If the singularity conditions are met,
the supermatter will SUCK THINGS INTO IT, even if they are bolted to the
GROUND. Just like a singularity! It's REALLY COOL.
https://streamasaurus.com/sharing/singularity_full.mp4 <--17MB video.
UPDATE 1: New rays for the singulo

https://user-images.githubusercontent.com/77420409/174933219-0118748a-02da-40f8-9b99-06009e197cc8.mp4
UPDATE 2:
Singularity delamination final countdown effect??:

https://user-images.githubusercontent.com/77420409/175421220-66bae109-204d-44ee-8a67-c18ce8eff3ba.mp4

When the supermatter has reached the FINAL COUNTDOWN but does NOT meet
the criteria for a singularity, it will simply YOINK everything
unwrenched towards, like a gravitational anomaly, range based on power
at the time. Not as crazy as the singularity. Most things will get
slapped against walls.

Here, have another cool delamination demo showing the criteria's
swapping mid countdown!
https://streamasaurus.com/sharing/modeswapping.mp4 <-- 17.5MB

I am likely missing something important from this body as I am drowsy
making this! I will update this body with anything I forgot to note that
I did.

## Why It's Good For The Game

The supermatter is a a very cool thing, but it could be cooler. I think
the visual experience could do with a bit of an upgrade, as visual
feedback is really cool and impressive to watch! You could tell more
about the crystal without looking at the console, but not everything or
precise numbers.

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
add: The Supermatter crystal will now emit rays of light, varying on
it's power level and situation.
code: improves a formatting and comment spelling
fix: The Causality field now actually shows up!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

Co-authored-by: tralezab <40974010+tralezab@ users.noreply.github.com>

* Adds Some Supermatter Effects

Co-authored-by: nevimer <77420409+nevimer@users.noreply.github.com>
Co-authored-by: tralezab <40974010+tralezab@ users.noreply.github.com>

---
## [ThePiachu/cmss13](https://github.com/ThePiachu/cmss13)@[639765b0c6...](https://github.com/ThePiachu/cmss13/commit/639765b0c69faddeec405080ab4fde79503fcf5d)
#### Saturday 2022-12-31 10:39:38 by Skegal

Loadout - Sniper facepaint (#2015)

# About the pull request

This PR is here to add the sniper facepaint into the loadout for 4
points like the skull facepaint.
 
 I tested it and it worked well as expected.
 
I saw a lot of marines asking the sniper for their bodypaint recently,
and i thought, that since it doesnt change anything game-wise we could
give it on the loadout, as the sniper isnt always here and sometime even
throw it to the trash...also people wont annoy the sniper for his paint
too.

((sorry for the webedit i ran into some problem doing the PR with visual
code studio))

# Explain why it's good for the game

I think its good because it add more customisation to characters with
one more good looking facepaint and like i said earlier, i saw some
marines asking the sniper for it (talked about it on discord and people
seemed to be ok with it)


# Testing Photographs and Procedure

<details>
<summary>Screenshots & Videos</summary>

i posted the pic here
https://discord.com/channels/150315577943130112/1054515157923020842 (if
in the pic you see the facepaint above the other paint its normal, i
tested it with the code above the other but it should appear under the
skull paint in the pr)

</details>


# Changelog

:cl: Skegal
add: Added Full Body Paint to Loadout
/:cl:

---
## [ThePiachu/cmss13](https://github.com/ThePiachu/cmss13)@[0c2b070039...](https://github.com/ThePiachu/cmss13/commit/0c2b070039afaa0d18a8bbdeb9c28e8333e16470)
#### Saturday 2022-12-31 10:39:38 by Stan_Albatross

Acid vest TGUI (#2050)

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

converts the acid vest config to TGUI

this took a long time to do because the way it's set up was somewhat
annoying

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

fuck  nanoui


![image](https://user-images.githubusercontent.com/66756236/208936729-7814c386-320d-4ae3-85b5-d7da44e9cedf.png)

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
ui: converted the A.C.I.D. harness to use TGUI
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

Co-authored-by: Stan_Albatross <swt91a@gmail.com>

---
## [Offroaders123/Art-Gen](https://github.com/Offroaders123/Art-Gen)@[989a83f497...](https://github.com/Offroaders123/Art-Gen/commit/989a83f497575b9bf910fd200c53a8b74e978a70)
#### Saturday 2022-12-31 10:43:13 by Offroaders123

Generator GUI

Now there's a semi-GUI for making the actual images!

I'm no expert at CSS Grid yet, so it's a bit broken, but now you can actually use the project as it's been planned to work! I haven't added a zip/download button yet, that will come with more GUI improvements too. Right now, you can simply copy/save the images by right-clicking on them, just for demo's sake.

Some help for tonight's progress (pun not initially intended :) )
https://developer.mozilla.org/en-US/docs/Web/HTML/Element/progress
https://www.freecodecamp.org/news/how-to-create-an-image-gallery-with-css-grid-e0f0fd666a5c/ (not quite what I ended up using)
https://css-tricks.com/intrinsically-responsive-css-grid-with-minmax-and-min/

I got inspired to work on this project a little more tonight because I'm looking into starting to publish my music back catalog again. I made a crazy album cover for the songs I'm finishing up, and I'm super happy with how ludicrous it is. I exported the songs from GarageBand (they're over a year old now), and added the artwork to them too. Then I started making these edits to the app, so then I can use it to generate all of my art tracks for YouTube. Even if it's not quite user-friendly yet, I want to at least get this working so I can start to use it. I think I'll probably just make this a regular old site on GitHub Pages, use that to generate all of the thumbnails, when I get to that stage of the production process, then use FFmpeg on the command line, maybe with a shell script or something to make it easy to do, and I still then have to figure out how I'm gonna do the YouTube upload part. I haven't had to deal with that in a while, so I think that's why I haven't looked into automating it yet. Once I have all of the pieces built up, including the YouTube automation part, I may combine all of them together here, and make it a simple Node script. Not sure if it's a thing, but it would be very cool if you could use something like `OffscreenCanvas` in Node, that would make this process much more contained. Then I could wrap the whole thing up and compile it into "native" byte code, and then you could run it using your terminal, just like a shell program. I think that would be the easiest way to get things done quickly, and without too much interference, but I also feel like that would have a harder way of attracting people to use it, since it's not just a GUI app, website, or app icon even. Still debating all of these things in my head! It's already really fun to use to automate the thumbnail part, I love it!

Drag 'n drop seems to be broken for some reason, not sure about that yet.

---
## [TheTimeSweeper/the](https://github.com/TheTimeSweeper/the)@[b6fb629a1c...](https://github.com/TheTimeSweeper/the/commit/b6fb629a1c671fa0d08afbc2b01a03dcb4ddd8bb)
#### Saturday 2022-12-31 10:57:28 by TheTimeSweeper

joe about to be fuckin real
tweaked and balanced numbers all around getting ready for release
lot of shit sorry future me

---
## [kemzops/ytmous](https://github.com/kemzops/ytmous)@[f6b81a9933...](https://github.com/kemzops/ytmous/commit/f6b81a9933c411dd05fc375eccee75947eb8d4ca)
#### Saturday 2022-12-31 11:07:51 by Yonle

Final commit.

After 6 - 10 months of no updates, It's time to deprecate this project. Even though i see somebody open a issue during a day that does not has update, still i respond to them.

I really had no idea of what am i doing after the past 6 months. Seriously, I'M LAZY AS HECK! You see, 3-5 Planned features that were planned since 6 MONTHS AGO IS NEVER IMPLEMENTED FOR THE PAST 6 MONTHS!

Every hours i'm busy and selling some stuff in my shop. Which can also the reason why i can't maintain this repository longer. You can also say that i can't maintain this repo longer due to life issue. I'm busy, tho. Scrolling through Telegram, Twitter, and Mastodon everytime when i'm bored and had no idea of what to do.

Believe me or no, The frontend code (Right in views folder) is mostly a copy paste result in Bootstrap example. Unbelieveable, Isn't it? This project also my random-bored project that i made when i had no idea of what am i doing in some hours.

So yeah. I think this is the end, But not the end. Since the code is open, Somebody may fork it and improve this project with their own.

Thanks for the 36 starts on github. I really appreciate it.

That's it. See you next time, folks.

Bye.

- Yonle <yonle@duck.com>
  Sat, 15 Jan 2022 06:32:25 GMT

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[fb49c0e791...](https://github.com/cmss13-devs/cmss13/commit/fb49c0e791afce778e81041c144eb038f8320d31)
#### Saturday 2022-12-31 11:18:47 by ThePiachu

Carrier buffs and xeno ability toggles (#1996)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

After playing a few rounds as various Carriers, it really felt they
could use a small buff to work way better with how basically they are
expected to build Hive Clusters now.

So the changes are:
- Vanilla and Shaman Carriers now have 500 plasma instead of 400
(would've given them 450 but the defines are in increments of 100).
Eggsac still sits at 600.
- Base carrier can carry 8 eggs (up from 7), and Eggsac can carry 12 (up
from 7). The latter especially suffered from not being able to carry
more than its base variant.
- Shaman can now plat weeds (since we do have support for 5 xeno actions
everything still fits). It was strange they could make special
structures but not base weeds as a Drone evo strain...
- Eggsac's egg generation is now a toggle instead of an active ability.
It uses plasma per tick and generates an egg every 30 seconds. This
makes it less fiddly and lets you plant eggs more actively. Still the
same cost overall.
- To support that, I added a new xeno ability type - active toggle. For
now it's used by Hivelord for Resin Walker and Eggsac for generating the
egg

Hopefully the active egg generation will actually make Eggsac a strong
frontline xeno, since currently it's not that popular, not to mention
it's still a liability for the Hive if they die...

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

Carriers are usually very plasma starved, especially when they are
expected to build Hive Clusters for their Eggs, so mitigated that a bit.
Eggsac carrying more eggs means it is compensated for losing huggers,
and being able to generate eggs on an ongoing basis makes that ability
less fiddly. The ability toggle makes it so the Resin Walker actually
deactivates properly when you run out of plasma and cleans up the code a
bit. Shaman being able to plant weeds means they can properly support
the frontline without needing other Drones for the base weeds.

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
balance: Base and Shaman Carriers now have 500 base plasma, up from 400.
Eggsac remains at 600 plasma.
balance: Base and Shaman Carriers can now store up to 8 eggs, up from 7.
Eggsac now can store a whopping 12 eggs, up from 7. Be careful not to
die while carrying those and give Marines greeno material!
balance: Shaman can now plant weeds. This bumped all their other
abilities one slot over shortcut-wise.
qol: Eggsac's egg generation ability is now a toggle that uses plasma
per tick to generate eggs at an ongoing rate until full or out of
plasma.
code: Hivelord's Resin Walker now uses the same toggle structure.
fix: Hivelord's Resin Walker now deactivates properly when you run out
of plasma.
fix: Fixed a runtime around Shaman's ability initialisation.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

Co-authored-by: harryob <me@harryob.live>

---
## [NetBSD/pkgsrc](https://github.com/NetBSD/pkgsrc)@[ead15b0370...](https://github.com/NetBSD/pkgsrc/commit/ead15b0370fdf2325a12833cb8f5ab43049b117d)
#### Saturday 2022-12-31 13:07:49 by wiz

mame: update to 0.251.

It looks like MAME 0.251 has made it out the door just in time for
the end of 2022! December felt like a long month in MAME development,
because so much happened! Nebula, an elusive DECO Cassette game,
is now emulated. With working steering controls, Magical Pumpkin:
Puroland de Daibouken is now playable. Two members of the HP 9825
family from the 1970s have been added, and issues with keyboard
input on localised versions of the HP 86B have been fixed.

One of the most interesting systems added this month is the so-called
Gerät 32620, make by the Institut für Kosmosforschung of the Deutsche
Demokratische Republik. This device was used to read coded messages
to be broadcast via shortwave radio numbers stations for reception
by undercover agents. If a human were to read the numbers, they
could inadvertently disclose knowledge about the nature of the
messages or the coding scheme in their speech patterns. This device
gives a small glimpse into the shadowy world of espionage.

Konami fans have a lot to be excited about. Firstly, two more
hand-held LCD games have been added: Skate or Die, and Bill Elliott’s
NASCAR Racing. Secondly, Windy Fairy has been making steady progress
on the PowerPC-based arcade systems, with gun controls now working
in Teraburst. Finally, various refinements and fixes to the CPU
core for Konami’s custom 6809 processor have fixed a subtle parallax
scrolling effect in the classic Padodius DA!

Several systems have been fleshed out noticeably this month,
including the NEC PC-8801mkII SR family of Japanese computers, the
3com Palm IIIc and Palm m100 PDAs, and the Yamaha DX100 synthesizer.
Additionally, the NEC PC-88VA2 can now boot most software, and the
work on the Palm systems has allowed the VTech IQ Unlimited to show
signs of life.

Quite a few systems have had pluggable controller support added
this month, and support for some additional controllers has been
added, including:

* Pluggable controller support for consoles and computers from
  Sega, NEC and Sharp.

* Sega Mega Drive mouse and 4-player adaptor support.

* Support for an ATmega-based paddle controller that works with
  export versions of the Sega Master System.

* NEC PC Engine mouse support.

* Support for the Dempa Micom Soft XE-1AP, the first analog
  gamepad. Can be used with compatible software for the Sega Mega
  Drive, NEC PC Engine, Sharp X68000 and FM Towns families.

Of course, there are lots of other fixes and emulation improvements.
The Apple IIgs has better ADB and real-time clock emulation. Sega’s
Turbo and Buck Rogers: Planet of Zoom have better controls, and
the latter has had graphical priority issues fixed. The NES APU
frame counter interrupt is now emulated, fixing issues with dozens
of games. For developers, debugger command and expression history
is now saved between sessions.

---
## [newstools/2022-the-irish-times](https://github.com/newstools/2022-the-irish-times)@[f1dfd5026d...](https://github.com/newstools/2022-the-irish-times/commit/f1dfd5026dc06fd6a2d78926d2dfb4b24fae55e9)
#### Saturday 2022-12-31 13:11:07 by Billy Einkamerer

Created Text For URL [www.irishtimes.com/culture/2022/12/31/donald-clarke-will-we-ever-again-have-a-who-shot-jr-moment-shut-up-you-dull-idiot/]

---
## [Salex08/tgstation](https://github.com/Salex08/tgstation)@[50929f054b...](https://github.com/Salex08/tgstation/commit/50929f054b89cab80a1e501b7a01bc74c79163d7)
#### Saturday 2022-12-31 14:08:24 by GuillaumePrata

Goliath dna infusion (#71657)

## About The Pull Request
This is a baseline version of the organs and I intend on polishing them
more in the future (Hopefully after other faunas get added to the
infuser.)

Now, this PR adds goliaths to the DNA infuser at genetics. It gives 4
organs and a final bonus effect.

1- Goliath eyes: Simple mostly filler organ that gives night vision.
2- Goliath lungs: Allow miners to breath either lavaland or the default
air mix. As a side effect they can't breath pure O2 anymore so internals
can't be used. Stay away from N2O or use your gas mask properly.
3- Goliath heart: Give miner ash storm protection
4- Goliath brain: Turns one of the miner's arm into a tendril goliath
hammer that can be used to mine. Like the mounted chainsaw it cannot be
dropped, it has slower atk speed, deals 20 damage by default and a bonus
80 to lavaland fauna, it also acts as a baseball bat against fauna so
you can dodge being hit back with good timing.
As a side effect, you can't equip gloves as your hand is a big ass
hammer...

The extra effect for having all 4 organs is lava immunity for now, I
really want to turn it into something more interesting later.

GAGS organs and bonus coderspriter arm:
![goliath
sprites](https://user-images.githubusercontent.com/55374212/205477889-22cfa586-dd43-405d-80cf-3981b31304e1.png)
If I have time I might animate the arm later.
## Why It's Good For The Game
This add some useful tools for miners if they opt into asking genetics
for help and bother to drag a goliath corpses to it.
The organs can be useful on the station, but they will only really shine
at lavaland.

We were brainstorming more things that miners can get from the station
on their downtime waiting the cargo shuttle to bring their bought gear,
this would be a simple and easy power up for miners that can have some
small (ignoring the hammer arm) bonus to miners, but small power ups
pile up.

I also wrote a hackMD around these organs, their goals, non goals,
future possibilities for fauna organs (goliath and others) etc.
https://hackmd.io/@GuillaumePrata/goliath_infusion_organs

## Changelog
:cl: Guillaume Prata
add: Geneticists figured out how to infuse goliath DNA into humanoids!
(Many monkeys were harmed in the process!)
add: Goliath eyes for nightvision, lungs to breath at lavaland safely,
heart to protect you from ash storms and the brain which turns one of
your arms into a tendril hammer.
add: Tendril hammer: Your arm becomes a giant mass of plate and tendril
but it won't fit on gloves anymore. While slow to swing around, you can
obliterate fauna/megafauna with it, 20 base dmg + 80 bonus damage to
fauna/megafauna with a bonus knockback.
/:cl:

---
## [benTAS12/-2349066046474-HOW-CAN-I-JOIN-SECRET-OCCULT-TO-MAKE-MONEY-](https://github.com/benTAS12/-2349066046474-HOW-CAN-I-JOIN-SECRET-OCCULT-TO-MAKE-MONEY-)@[2405587cc5...](https://github.com/benTAS12/-2349066046474-HOW-CAN-I-JOIN-SECRET-OCCULT-TO-MAKE-MONEY-/commit/2405587cc5be0fca41c4bee30e071c8d3dde961b)
#### Saturday 2022-12-31 14:34:30 by benTAS12

I WANT TO JOIN SPRITUAL WARFARE BROTHERHOOD OCCULT

 WELCOME TO THE OCCULT OF SPRITUALWARFARE OCCULT THE GLOBAL SOCIETY, WE ARE CELEBRATING OUR YEARS OF UNITY AND PROGRESSIVE, ARE YOU DESPERATE TO BE RICH AND FAMOUS COME AND JOIN US IN EDO STATE TO CELEBRATE 51 YEARS ANNIVERSARY WE WORN JUR WE FIND ANY TYPE OF THINGS YOU NEED IN THIS WORLD MONEY, PROTECTION, SPIRITUAL RING, FREE VISA, WEALTH, WE ARE NOT HERE FOR THE UNSERIOUS ONES PLEASE IF YOU KNOW THAT YOU HAVE NOT MAKE UP YOUR MIND TO JOIN US DON'T CALL +2349066046474

---
## [LeafyLuigi/discord-themes](https://github.com/LeafyLuigi/discord-themes)@[5e9e415e06...](https://github.com/LeafyLuigi/discord-themes/commit/5e9e415e0663abb4a2c15da9df668f2f6ac891d4)
#### Saturday 2022-12-31 14:39:45 by LeafyLuigi

holy fucking shit: an update!

- Reworked modal's backend (and looks, obviously)
- Also reworked Profile modals (Popout, Modal, Panel etc) which may cause a few issues with custom CSS
- Default Code font now contains Hack (Hi KDE users)
- Messed around with the chat divider a little too much
- Attempted to fix any status color issues
- Reworked string translations. If you'd like to translate anything added by the theme, please say something!

Newly themed:
- Hide/Show channels page
- Customise user page

New Variable:
--hide-profile-panel: default 1, hides profile panel in DMs

NOT DONE:
- Client Mod stuff
- Activities in UML
- Stayed sane

---
## [The-Balthazar/BrewWikiGen](https://github.com/The-Balthazar/BrewWikiGen)@[1fda7711af...](https://github.com/The-Balthazar/BrewWikiGen/commit/1fda7711af04ae092c6f8f2b8436ab278ca3c872)
#### Saturday 2022-12-31 15:14:44 by Balthazar

Fixed an error if some dumb fuck put a non sound in a sounds table.
Sorry, that's mean, I shouldn't call you a dumb fuck. You're a careles f

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[4d0e195d08...](https://github.com/cmss13-devs/cmss13/commit/4d0e195d08ae4d36d83c59f6e73b98fdb8c2d7d0)
#### Saturday 2022-12-31 16:30:31 by carlarctg

Adds three eye_blur pain overlay preferences. (#2039)

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

Adds three preference tiers for eye_blur()

0, the default, keeps the new and updated blur Stan ported from TG.

1 re-adds the weldervision impair, vision-block scaling depending on
amount of blur.

2 brings back the ancient legacy eye blur, with various warnings that it
is not recommended.

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

Some people report this hurting their eyes, so a preference to return to
the old is a good thing.

Bringing back the legacy overlay will also let some boomers experience
soul in cm again.

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
add: Added a preference for eye blurring. Can be defaut blur, vision
impair, or the legacy blurring effect.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

Co-authored-by: harryob <me@harryob.live>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[1c76ea5334...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/1c76ea533439dcd7fca15a2dd500a44dc6158883)
#### Saturday 2022-12-31 16:37:04 by SkyratBot

[MIRROR] Changes our map_format to SIDE_MAP [MDB IGNORE] (#18070)

* Changes our map_format to SIDE_MAP (#70162)

## About The Pull Request

This does nothing currently, but will allow me to test for layering
issues on LIVE, rather then in just wallening.
Oh also I'm packaging in a fix to one of my macros that I wrote wrong,
as a joke

[removes SEE_BLACKNESS usage, because we actually cannot use it
effectively](https://github.com/tgstation/tgstation/pull/70162/commits/c9a19dd7cce95038340ebd5c1a6e4cb27ee7c9ee)

[c9a19dd](https://github.com/tgstation/tgstation/pull/70162/commits/c9a19dd7cce95038340ebd5c1a6e4cb27ee7c9ee)

Sidemap removes the ability to control it on a plane, so it basically
just means there's an uncontrollable black slate even if you have other
toggles set.

This just like, removes that, since it's silly

[fixes weird layering on solars and ai portraits. Pixel y was casuing
things to render below who
shouldn't](https://github.com/tgstation/tgstation/pull/70162/commits/3885b9d9ed634cdc4c8041b19df5b5ea9a1a37ae)

[3885b9d](https://github.com/tgstation/tgstation/pull/70162/commits/3885b9d9ed634cdc4c8041b19df5b5ea9a1a37ae)

[Fixes flicker
issues](https://github.com/tgstation/tgstation/pull/70162/commits/2defc0ad20a0ee7d12e0b071f6d31b6127b8765d)

[2defc0a](https://github.com/tgstation/tgstation/pull/70162/commits/2defc0ad20a0ee7d12e0b071f6d31b6127b8765d)

Offsetting the vis_contents'd objects down physically, and then up
visually resolves the confliciting that was going on between the text
and its display.

This resolves the existing reported flickering issues

[fixes plated food not appearing in
world](https://github.com/tgstation/tgstation/pull/70162/commits/28a34c64f830660d7fb1cc669b9fc3ed9f5c7d61)

[28a34c6](https://github.com/tgstation/tgstation/pull/70162/commits/28a34c64f830660d7fb1cc669b9fc3ed9f5c7d61)

pixel_y'd vis_contents strikes again. It's a tad hacky but we'll just
use pixel_z for this

[Adds wall and upper wall plane
masters](https://github.com/tgstation/tgstation/pull/70162/commits/89fe2b4eb40edc36879e4e1954dee8616be94522)

[89fe2b4](https://github.com/tgstation/tgstation/pull/70162/commits/89fe2b4eb40edc36879e4e1954dee8616be94522)

We use these + the floor and space planes to build a mask of all the
visible turfs.
Then we take that, stick it in a plane master, and mask the emissive
plane with it.

This solves the lighting fulldark screen object getting cut by emissives
Shifts some planes around to match this new layering. Also ensures we
only shift fullscreen objects if they don't object to it.

[compresses plane master
controllers](https://github.com/tgstation/tgstation/pull/70162/commits/bd64cc196a4265d42809eebbd1afa46fa33a576d)

[bd64cc1](https://github.com/tgstation/tgstation/pull/70162/commits/bd64cc196a4265d42809eebbd1afa46fa33a576d)

we don't use them for much rn, but we might in future so I'm keeping it
as a convienince thing

:cl:
refactor: The logic of how we well, render things has changed. Make an
issue report if anything looks funky, particularly layers. PLEASE USE
YOUR EYES
/:cl:

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* Changes our map_format to SIDE_MAP

* Modular!

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>
Co-authored-by: Funce <funce.973@gmail.com>

---
## [silencer-pl/cmss13](https://github.com/silencer-pl/cmss13)@[0dd70b12e5...](https://github.com/silencer-pl/cmss13/commit/0dd70b12e5142b3b0f14bf237765c1e643fe8a3f)
#### Saturday 2022-12-31 17:10:23 by Stan_Albatross

removes unused nanoui templates (#2012)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

none of these templates are used anywhere

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

fuck nanoui

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
del: Removed ten unused nanoui templates. Don't worry, they'll all be
going away soon.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

Co-authored-by: Stan_Albatross <swt91a@gmail.com>

---
## [Danielkaas94/DTAP](https://github.com/Danielkaas94/DTAP)@[9130c8d7d7...](https://github.com/Danielkaas94/DTAP/commit/9130c8d7d702789a62447041599e1977559999fb)
#### Saturday 2022-12-31 17:23:25 by Danielkaas94

Blow 🍆💦
Did you ever know
There's a light inside your bones
The hope that you can't hide
And it teases you every night

And you don't understand
Glaring at the light
Sitting like a dog
In your ordinary life

Why you're so paralyzed
Why don't you spit it out
Coming on your face
Oh yeah

Feel you
Feel me
One life
One shot
One love
Now you're a mannequin

Candy
Cane gun
Micro
Brain waves
Remote
Controled white man

High speed
Defcon
Mental
Gang bang
Black out
You're not dragster man

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[a6dcc479ac...](https://github.com/mrakgr/The-Spiral-Language/commit/a6dcc479acca138cf1cbb35b6efb7f82ab4c51c3)
#### Saturday 2022-12-31 17:24:48 by Marko Grdinić

"2:25pm. Uah, let me do the chores here.

3:05pm. Phew done. Let me read the 2 Satanophany chapters. I need some chill time.

I am glad that Satanophany scanlations have picked up again. There was even a new Blattodea chapter out recently.

```sl
inl main () =
    inl x : inv a u64 f32 = create 1
    inl y = index x 0
    set x 0 y
    ()
```

I just wanted to check whether the original inv arrays still work. They do. Ok.

That is one concern less.

```
2.3.5 (WIP)

* Added the SizeOf op to the language.
* Modified the way Int32 and UInt32 literals are printed back to how they were before.
* Added a check when applying prototype instances.
* Added the FreeVars op to the language
```

Let me push out a new version. A decent amount of work went into the language in the past two weeks. The two most noteworthy changes is that I perfected ref counting in the c backend, replaced the Cython with a Python one, and improved how the pattern matching is compiled.

These 3 are huge improvements to the quality of the language. And the rest of what I had done will improve the serialization for the sake of future backends. Spiral has gained a lot. Whether I can translate those gains into my personal benefits remains to be seen.

3:25pm. Let me read manga. I won't hurry the yearly review. If I cannot do it by tomorrow I'll just post it two days later. It is not like doing them is my job.

Hmmm, what I should do is start a new repo.

https://github.com/mrakgr/PIM-Programming-In-Spiral-UPMEM-Demo

Here it is. It was really painless opening this.

3:40pm. Let me take a break for half an hour, or an hour. I should take this time to think of what exactly do I want to do next.

https://www.youtube.com/watch?v=5l7enB9iNIc&list=PLQHmK8j6zHB5uZLsbF4BoAZmuIz6vi2Q0&index=14
Evenicle 2 OST

I've never listened to it before, but the Evenicle 2 OST is good.

https://mangadex.org/chapter/5dee9109-65b9-49d2-8d46-5228213d78bd/10

1 in 20 people? That seems way off. I mean, this sort of physiology I've only ever heard manga chars having.

3:55pm. Done with the Satananophany chapters. Let me do the yearly review. I'll write it in Google Docs.

6:05pm.

///

2022 was quite a lame year for me. After throwing in the towel on RL in late 2021, I started studying art with the intent of illustrating my VN. I just needed to do anything other than programming, so it seemed as good a thing as any. I did drawing at first, but then quickly moved into 3d and spent a total of 9 months playing with various 3d programs like Blender, Houdini, Moi, Clarisse, Substance Painter and Designer, and Zbrush. I’ve gotten familiar with the use of these programs, but I haven’t grasped the efficiency I really wanted from that practice, and then a few months after the last review DALLE and Stable Diffusion came out. The way I dropped making my own artwork in favor of generative NNs is somewhat messy. At first I was hyped, then I tried the two and found them difficult to deal with and left them alone for a few months, but then I started using the [free SD version](https://huggingface.co/spaces/runwayml/stable-diffusion-v1-5) on Hugging Face. It wouldn’t give me quite what I wanted, but after I got used to prompting I started enjoying going through 10/10 masterpieces and picking the best. I love Stable Diffusion now.

All the other NN stuff is not that interesting to me, but SD itself is like a sneak peek into the Singularity. If a human’s skill can go between ranks 1 and 5 in art, then these NN models are rank 6. Right now, these diffusion models are the greatest artists in the world, and no human can come close. Chapters 1-15 of [Simulacrum: Heaven’s Key](https://www.royalroad.com/author-dashboard/dashboard/57747) have been illustrated almost entirely using SD 1.4 and 1.5. I have about 1,000 pages written about it so check it out.

After I had gotten tired of 3d art, I said to myself that I will either get a job or start writing the story, and I picked the latter. In hindsight, studying 3d was a waste of time. In the end, I was chasing a skill that only generative NNs like these could give me. Who knows, maybe in the future I will be using NNs to generate 3d. Strangely enough, even though I should have just started writing Heaven’s Key right away, and I won’t be using 3d anymore, I do not feel regret about learning the things that I did. Despite my inner turmoil maybe living this way by pushing myself to learn things for my goals is satisfying after all.

The lack of money is painful for me psychologically. I didn’t want to be an artist so I picked goals that would hopefully land me in success, but ended up missing the target. What should I do now? It is 2023, Intel can’t stop tripping over its own feet, the various AI chip startups are basically vaporware or going only after the big fist. I do not have access to them. It hurts that I still have my GTX 970 in my rig. GPU performance is still doubling every 18 months, but so is their price and in 2023 the price of a high end GPU costs as much as an entire high end rig a couple of years previously.

The main reason why I blame my late 2021 failure in RL is lack of computational resources. I used to think that it would be enough to just look at existing papers and that with effort I would be able to infer the way to make RL work well. I thought that my responsibility would only be to create the tools to enable me to take advantage of the next hardware wave. That was [Spiral](https://github.com/mrakgr/The-Spiral-Language). I thought that there would be numerous AI companies offering smaller chips to the general public, which would also be my potential sponsors for the language. I thought I could make RL agent for a toy game like poker without much trouble and use botting to get further computational resources which would further increase my ability to make agents in a neverending virtuous cycle.

I just couldn’t have imagined that backprop itself would be so dominant for so long! That is the main mistake that caused all my other bad luck. I thought that if the ML field is given a couple of years to play around, they would get around to discovering something useful for RL. But that didn’t happen. I am not sure how things will go at this rate.

One thing I am starting to change my mind on is what my own responsibility is. I thought that it would be fine to leave such an important thing to the field itself, but I am going to have to figure it out myself. If I could I’d have done it in 2021 instead of dead ending it, but better hardware will come out. The move to [PIM programming](https://www.youtube.com/playlist?list=PL5Q2soXY2Zi8KzG2CQYRNQOVD0GOBrnKy) still has not happened, and unlike with GPUs, Spiral right now is in particularly good shape. I have my board ready to ride this wave. The AI accelerator companies themselves are quite disappointing and of what I’ve seen only Tenstorrent is really worth paying attention to. Out of all the companies that I’ve looked into only Tenstorrent has plans to sell cards you and I could slot into our home rig.

Graphcore for example, in its cheapest form leases machines for 9,000$ a month. And its programming model is ridiculous, composing AST nodes in C++. Since it is losing the fight against GPUs, it will go broke before long.

Having small offerings is important for the company’s survival long term. When computers are cheap, anyone can program them in their free time, and make open source and commercial software for them, raising their value. But when something costs 9 grand, they are only going to be used to train large NNs and it is the company itself which will be shouldering the cost of writing software. Forget playing around with those kinds of machines. I get the sense that Tenstorrent as a company understands that much, but the other companies are blindly going after the big fish and it will cost them. This seems obvious to me, but strategic vision in AI companies is really rare.

Since late 2021 I haven’t been doing any programming. I did the C backend back in July when I stopped 3d, but the only exception from that is the work on Spiral I’ve done in the last two weeks.

I posted [a link](https://www.reddit.com/r/ProgrammingLanguages/comments/zm01jr/pim_processinginmemory_course/) to that PIM course on Reddit saying how much I’d like to program these things, and the lead compiler dev for UPMEM which is one of the companies featured in the course sent me a PM telling me he could point me to the [simulator](https://sdk.upmem.com/). I sensed an opportunity, if that guy was interested, then the others on the list might be as well, so I decided to go out on a limb and create a Spiral backend for UPMEM. He was gracious and said that he would answer any questions that I have as long as his energy allows. I sent him some questions. He answered almost none of them and has been ghosting all my messages. That is about how much you can expect from Internet randos. I’ve had people contact me offering unwanted advice, but I’ve yet to even once succeed at manipulating them into using their brains. It is not like I am trying to scam them. I just break the script a little and they vanish. This particular case has been especially annoying. It has been two weeks since I last heard from him, and I am still mad.

Anyway, the UPMEM Python + C backend is done, I’ve done a fair bit of programming to make a useful demo and what I need to do next is write [an article](https://github.com/mrakgr/PIM-Programming-In-Spiral-UPMEM-Demo) showing off my skills.

The UPMEM devices themselves are pretty useless, as they are only good at integer arithmetic, but they are not GPUs, but true PIM chips so they are the ideal demo for what Spiral can do. The other devices covered on the PIM course are much more interesting. If I could get the one with 1.2 PFLOPs, that would give me 1,000x the computational power of my GTX 970 and would make it worth attempting to do RL again. A couple of months ago, I posted a link to Spiral in the Tenstorrent’s discord, and haven’t gotten any replies, but maybe the article once it is done will serve as bait. I’ve decided - I don't really want a job (even though I want money) but I am going to make an exception when it comes to these companies. If UPMEM extended me an offer I would have taken it just to spread the light of staged functional programming at these kinds of places. A language like Spiral is the only one fit for devices such as these. I’ll demonstrate what I mean in the article. No other design has the same combination of efficiency and the interop capability.

I am not sure how all of this will go. It feels like all my attempts are doomed, but I have no choice, but to persevere and keep going forward.

Besides baiting AI companies, I am thinking about how to try ML again. The 2021 failure proved to me that I cannot understand and truly improve in ML like I can in regular programming which was devastating to my ego, so this time I am considering playing it by the book. That means something like tabular RL at the top and evolution at the bottom. I made a huge mistake trying to figure out the algorithms myself. That is the primary lesson which I drew from that failure. I realized that if the hardware is powerful enough I could just create a genetic programming system that could infer the right learning algorithms itself, but I do not have such capable hardware. GPUs are just not suitable for making such a system, but those UPMEM devices confirmed my prediction that PIM chips will have more general purpose capabilities.

Compared to late 2021 I do have access to better hardware. While my own rig only has a 4gb GTX 970, a 8$/month subscription on [Paperspace](https://console.paperspace.com/signup?R=F3BL1O4) gets me free 16gb RTX5000 and A4000 which are much better than it. I’ve been using them to illustrate the latest chapter of Heaven’s Key. The company is in a growth period of trying to lock in customers by offering far below market prices to use their hardware, so it is way cheaper than any other cloud place I’ve looked at. It even has free basic Graphcore IPUs, but who is going to program those? Graphcore made the mistake all AI chip companies (including Tenstorrent) have which is to load itself up on C/C++ programmers. It should have been hiring functional PL experts instead.

Right now, Spiral is in really good shape. I can do things with it that I could only have dreamed about even as far back as 2020. I originally envisioned it as being used to write ML libraries, but backprop just won’t go away which has led to the absolute dominance of frameworks like PyTorch and Tensorflow, and consequently the AI chip companies adapting to that reality and going after the big fish. But now I think that once I get my hands on next gen hardware, I will be able to use it to create a genetic programming system.

In 2023, I intend to split my time between writing and programming RL agents. Maybe I’ll make a Heaven’s Key game, something like a VN where you play against my poker agents. That could be a bit interesting. I should be doing AI, but none of these algorithms are worth using with real money on the line, so maybe some crappy players I could sell. And this would lead me to further cultivating my programming skills.

I know.

I am a programmer so I should be programming rather than writing or doing art, but when you’ve lost your way, what can you do?

Heaven’s Key…lacks the energy I put into my 2014 stories. I know that better should be possible, but I cannot do it. Right now I am still trying to push forward through the obstacles with my own power rather than having the computers helping me. I am shouldering my burdens on my own. I do not know whether I will reach my end, or whether I will manage to grasp the chance that I’ve been pursuing. My future looks bleak.

The Singularity will happen with or without me, but deep down what I want to do is to cause the Singularity myself.

Getting killed by a self improving being would not be bad. It would vindicate who I am at least, but I want to be the igniter rather than an onlooker in its grand story of transcendence. That would be a true victory to me.

For now, the best I can do to make up for 2021 is to handle my future AI work like a scientist. That means having evolutionary group competitions, no more equivalents of trying to burn holes through the back of the cards with my mind’s eye. I am going to make sure that the GPUs/AI/PIM chips are the ones working hard instead of me. I’ll take it step by step, according to my responsibilities and without any expectation of them being good for real money matches.

///

6:20pm. Done with lunch. Let me close here. This is good enough. Tomorrow I'll start work on the article."

---
## [Danielkaas94/DTAP](https://github.com/Danielkaas94/DTAP)@[0c533d9cfc...](https://github.com/Danielkaas94/DTAP/commit/0c533d9cfc538b980836cf735401656358c9b740)
#### Saturday 2022-12-31 17:50:15 by Danielkaas94

🥂 Seaside Friends 🥂
I feel comfortable
My life is spectacular
I am free
Totally free
I love me

I was born a millionaire
And I'll die a billionaire
And wind blows in the trees
And my good friends are with me
Under trankillizers
In my villa near Kabul
We're wondering ourselves
If it's true or insane
That we're all made of champaign
Love love me, any time
Love love me, turn around

Good friends at the pool
Waiting for the dawn
Making the sound of rocks ya
Knock in their glasses
Imagining the world
In orbit around their asses
Yes my friend and I
Are debating about art
golf, porn and cars
Aren't second guessing ourselves
If we know each other well

Love love me, any time
Love love me, turn around
Love love me if your fine

---
## [Vinny008/tgstation](https://github.com/Vinny008/tgstation)@[deee485693...](https://github.com/Vinny008/tgstation/commit/deee48569310b1d48d739fc3b529ac00838e45b0)
#### Saturday 2022-12-31 17:56:18 by LemonInTheDark

Fixes antag hud icons disappearing if mesons were equipped (#71155)

## About The Pull Request

They sit on plane 0, IE the darkness plane. So if say, the darkness
plane was alpha'd away (which we have to do with see_blackness), then so
goes the hud element. stupid stupid stupid stupid

## Why It's Good For The Game

Fixes a derivation of #68087
Not all of it, since most of that came about pre plane cube and likely
has to do with z'd image shenanigines. I got it to replicate once
randomly but then it stopped. v annoying. There is a linked issue report
that mentions mesons however, which this does resolve.

## Changelog
:cl:
fix: You can now see antag hud icons AND see through walls. WOW
/:cl:

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[b6cd073409...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/b6cd073409b6d02ff690b7f33861d9de6d38c1f2)
#### Saturday 2022-12-31 18:07:01 by SkyratBot

[MIRROR] Unfuckies pod blood [MDB IGNORE] (#18411)

* Unfuckies pod blood (#72323)

I broke it in #72220
Thanks to @ Fikou for catching this
list(variable = 0.1) doesnt work on byond, so I last-minute improvised
and changed it to
list("[variable]" = 0.1), using a string instead of a typepath. I
already tested it thoroughly so decided it was probably good without
thinking of it anymore

:cl:
fix: fixes pod blood I swear
/:cl:

Co-authored-by: Fikou <23585223+Fikou@ users.noreply.github.com>

* Unfuckies pod blood

Co-authored-by: Time-Green <timkoster1@hotmail.com>
Co-authored-by: Fikou <23585223+Fikou@ users.noreply.github.com>

---
## [Danielkaas94/DTAP](https://github.com/Danielkaas94/DTAP)@[8babd6bd27...](https://github.com/Danielkaas94/DTAP/commit/8babd6bd27f360991ae4079817d2d830891efd55)
#### Saturday 2022-12-31 18:15:45 by Danielkaas94

🔥🥶 Hot Night In a Cold Town 🥶🔥
Sonny's out strolling, ambling slowly
Washed in amber street lights
A mexican wind blows in
Takin' ahold of angelina's hair
And her halo
Motors running, muffling the sound
Of the street talk
A big deal's goin' down

In another hot night
In a cold town
Got yourself a hot night
In a cold town

Johnny's got spare change
In his pocket
A ring and a watch
To hock for a sweet ride
A one way ticket
Hidden in his shoe
These last few hours
He says he'll spend with you
He's leavin' home without a trace
No forwarding address

He'll never have to face another

Hot night
In a cold town
Got yourself a hot night
In a cold town

Well, the losers and the groovers
And the corner boys
Are hangin' around
Runnin' in and out of doorways
Up and down the stairways
Stray dogs headed for the pound

In another
Hot night in a cold town
Got you, got yourself a
Hot night in a cold, cold town
Cold town

It's just another hot night
In a cold town

Such a cold town

---
## [Griffty/Terminal-Graphic](https://github.com/Griffty/Terminal-Graphic)@[3240aeeaf1...](https://github.com/Griffty/Terminal-Graphic/commit/3240aeeaf1a512b5b4cf412eb5b088facbe8ff11)
#### Saturday 2022-12-31 18:33:25 by Griffty

Few weeks after, I returned here. Finally, I finished base functionality now it's more or less usable, just for fun, but usable. I cannot remember truly what I said before, but now I added more user-friendly interface, at this moment you need to start StartSettings.bat or just Settings.java by itself, after you will see little settings menu where you will be able to launch the program. Also, I think in previous update rotation wasn't working at all or was broken, so now it is. Along z axis it's still a bit weird, but it is what it is, I will try to fix that later. In nearest future I am thinking on giving user ability to add multiple objects and control each of them individually, it should be great.

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[1737ab8598...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/1737ab8598dc94f6c5d8a9f11d8b8bc5a75055d6)
#### Saturday 2022-12-31 18:43:46 by SkyratBot

[MIRROR] Fixes parallax on >2 level maps going fucky with optimized multiz [MDB IGNORE] (#18298)

* Fixes parallax on >2 level maps going fucky with optimized multiz (#72169)

## About The Pull Request

We no longer always render parallax.
This was causing issues because we can't isolate the white of space from
the vaugely white of everything else.

So instead, if your parallax plane is out of view, we'll not only
disable it, but we'll disable the strand we send from the main plane TO
it.

Instead only blending against the bottom stack.

This does mean there's a possibility for fullwhite on z transition
borders (potentially fixable), or when hijacking the plane (also
fixable, but significantly more annoying).

This is enough to make large maps functional though, so I'm happy with
it

## Why It's Good For The Game

Allows for #71731 and other maps like it. Makes my code actually work

## Changelog
:cl:
fix: Using optimized multiz on > 2 z layer maps will no longer cause
fucko bungo
/:cl:

* Fixes parallax on >2 level maps going fucky with optimized multiz

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [Mixelz/SynergismUnofficial](https://github.com/Mixelz/SynergismUnofficial)@[a0515406da...](https://github.com/Mixelz/SynergismUnofficial/commit/a0515406da6037eee69582bdfd63b66fafde290a)
#### Saturday 2022-12-31 19:10:17 by Mixelz

Perk List Overhaul

Contained within this commit is an encompassing overhaul onto several different parts of the Perk List, including the merging of several perks, adding additional levels to denote previously hidden effects and implementing updating effect % counters to applicable perks.
To clarify, no changes to the functionality of the perks were made, only to the presentation of said perks.
The full list of changes are as follows, in the order they appear in the code:

Merging in Midas' Windfall and Industrial Daily Codes into 2 levels of XYZ.
Minor formatting change for Unlimited Growth.
Improved readability of Not so challenging description and uppercased its name.
Merged A Particular Improvement into Automation Upgrades, also added an extra level to denote the previously hidden effect of keeping w2x10.
Revamped the descriptions for Automation Upgrades to improve readability and internal consistency with labeled effects.
Combined Blessed by the Spirits, Advanced Runes Autobuyer, and Autobuy Talisman Resources into a new perk: Automagical Runes.
Combined Better Cube Opening and Automation Cubes into a new perk: Cool QoL Cubes.
Combined Real Time Auto Ascend and Auto Ascension Challenge Sweep into a new perk: Eternal Ascensions.
Updated descriptions for "Ant God's Cornucopia" for readability/spelling.
Swapped the descriptions of Golden Revolution 1 and 2 (Keeping it in line with the effect ordering of GQ 1/2/3 themselves.)
Golden Revolution 1/2/3, PL-AT Σ, and skrauQ now all update to display their current % effect.
Combined Metacogenesis and Metatrigenesis into a new perk: Octeract Metagenesis.
Immaculate Alchemy now updates its description per level instead of having 1 description for all 3 levels.

---
## [tnekohue/tgstation](https://github.com/tnekohue/tgstation)@[cf02f62298...](https://github.com/tnekohue/tgstation/commit/cf02f622986932af8fb09e48cbdf5ec0ac567cf5)
#### Saturday 2022-12-31 20:07:07 by LemonInTheDark

useless update_appearance reduction, emissive_blocker micro optimization (saves a second of init) (#71658)

## About The Pull Request

[Saves 0.2 seconds of init time. 50% of emissive
blockers](https://github.com/tgstation/tgstation/commit/8318b648f6d32844aacbfb4c309152cd45801f5c)

Emissive blockers are a decent expense during init, even these, which
are the ones that update outside of initialize.
I've inlined them, removed some redundant vars and checks, reduced the
arg count, and shifted some things around. This ends up saving 200ms, or
50% of its total cost.

I also shifted mutable_appearance about a bit. it's not a massive
saving, but it is technically faster

[Prevents a few redundant appearance_updates, saves 0.8 seconds of
init](https://github.com/tgstation/tgstation/commit/5475cd778b66b22b1e2c8d86b2c6d59fb84f219a)

Prequisit info: update_appearance is decently expensive
It's good then to only do it if we have a reason to, right?

Me and moth were shooting the shit about just general init time, and we
came up with the idea of tracking which update_appearances actually
"worked" and which didn't.

That bit comes later, let's enjoy the fruits of that work first

First, holograms were calling update_appearance on process, for almost
no reason.
I patched the one event they don't already "react" to, and then locked
it behind a change decection if.
good for live, doesn't impact init.

Next, decals. If you add a decal to something before it inits, it'll
react to the after successful init signal.
The trouble is the same atom could have its appearance updated from this
MORE then once, since decals can be stacked on tiles, and signal
unregisters don't work once the signal is sent.
So we add a flag to track if we've had this happen to us or not, so it
only happens once.
saves 80 ms

Power! lots of things call power_change on init, often more then once.
We'll update appearance for each of those calls, even if only one is an
actual change.
That's silly, better to track what sort of power we're using for our
appearance and go off that changing

This was taking about 300ms. Really stupid

Icon smoothing. After emissive blockers were added, any change to
something's icon smoothing would lead to an update_appearance call.
Nasty shit, specially cause of walls, which don't even use emissive
blockers.
Ok then, so we'll always update appearance for movables, and will allow
turfs that are interested to hook it manually.
Not many of those anyhow
This is slightly a dev ux thing, but it saves 600ms so I think it's
worth it. Rare case anyway

Telecomms:
telecomm machines were updating appearance on process. This is to cover
for them turning on/off on process.
Better then to just check if on actually changed.
This cost adds up midgame, doesn't impact init tho

Materials:
There's this update_appearance call in material on_apply. it doesn't do
anything.
The logs will lie to you and say it does, but it's just like reapplying
emissives. It doesn't need to exist
Saves like 50ms

Canisters:
Live thing, lots of time wasted updating appearance for no reason, lets
see if we change anything first yes?

[Uses defines to wrap update_appearance for
tracking](https://github.com/tgstation/tgstation/commit/4fa82e1c9d93577aadb3c743f17196331f62e67c)

[Undoes _update_appearance changes, instead reccomends 2 regexes to
use](https://github.com/tgstation/tgstation/commit/a8c8fec57a4e43d1fa636b5ac68459903faa9fc5)

I need file and line number for my tracking, so I need to override
update_appearance calls, and also preferably not require every override
of update_appearance to handle dummy file + line args.

So instead, I created a wrapper proc that checks to see if appearanaces
match (they're unique remember, the two of the same visual appearance
will be equivalent)
The trouble is I can't intercept JUST proc calls, or JUST function
definitions with defines. it needs to be both.

So I renamed the /update_appearance proc to /_update_appearance

this way I can capture old uses, and don't need to worry about merge/dev
brain skew

~~It does mean that all update_appearance proc definitions now look
weird tho.
My profiling is leaking into dev ux. I wish I had better templating.~~

**The above is no longer being pr'd**, it's instead just recommended via
a few regexes adjacent to the define.
Smelled wrong anyhow

[Adds a setter for panel_open, so I can update_appearance on
it](https://github.com/tgstation/tgstation/pull/71658/commits/cf1df8a69fc1a816391d085ee7419b14f9fe9167)

## Why It's Good For The Game

Speed

---
## [tnekohue/tgstation](https://github.com/tnekohue/tgstation)@[176f7a0e42...](https://github.com/tnekohue/tgstation/commit/176f7a0e422b8417456e1ab65fa59e7ee88a16c5)
#### Saturday 2022-12-31 20:07:07 by san7890

Traitor UI only shows Unlock/Failsafe Code if you have it (#72114)

## About The Pull Request

There are cases in which you don't have an unlock code (if the uplink is
implanted in you from the start) and you obviously don't always start
with with a failsafe code (need to buy it). So, let's only fill in this
fields in the UI should they exist.

There might be something to be said about wanting to ensure that people
remember that they can check this UI screen to find the failsafe code
should they lose it later, and I wouldn't mind changing the string to be
something like "Failsafe: None" in that case. However, I just think that
keeping it as:

```txt
Code:
Failsafe:
```

is silly and should be changed somehow.
## Why It's Good For The Game


![image](https://user-images.githubusercontent.com/34697715/208604758-d7ff3ae9-e552-4dd2-998d-81715cd06ffc.png)

Note: That white box isn't part of the UI, that's a part of the edit I
did to the screenshot in the area where the stuff... isn't? What was i
thinking

I think the UI looks a lot cleaner for those cases when you just don't
have anything.
## Changelog
:cl:
qol: The Traitor's Antagonist Panel's Unlock and Failsafe entries will
only appear if there is an Unlock/Failsafe Code to display.
/:cl:

---
## [sleepynecrons/cmss13](https://github.com/sleepynecrons/cmss13)@[a742c64df9...](https://github.com/sleepynecrons/cmss13/commit/a742c64df98ec4f23eaa64162a2518a91c642ead)
#### Saturday 2022-12-31 20:08:53 by carlarctg

Fix entering a ghosted xeno not removing ghostize sleep. (#2076)

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

Fix entering a ghosted xeno not removing ghostize sleep.

# Explain why it's good for the game

This sucks ass! Let me wake up!!!!! can KILL you if you enter a xeno in
a difficult situation!!!!!!

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
fix: Fix entering a ghosted xeno not removing ghostize sleep.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [Capsandi/tgstation](https://github.com/Capsandi/tgstation)@[8cb4947084...](https://github.com/Capsandi/tgstation/commit/8cb4947084edffc9476c40ea6283b68e818f48bd)
#### Saturday 2022-12-31 20:26:55 by Jacquerel

AI actions won't unassign each other's movement targets & Mice stop being scared of people if fed cheese  (#72130)

## About The Pull Request

Fixes #72116 
I've had a persistent issue with basic mob actions reporting this error
and think I finally cracked it
When replanning with `AI_BEHAVIOR_CAN_PLAN_DURING_EXECUTION` it can run
`Setup` on one action leading to the plan changing, meaning that it runs
`finishCommand` to cancel all other existing commands
If you triggered a replan by setting up a movement action in the middle
of another movement action, cancelling the existing action would remove
the target already set by the current one.
We want actions to be able to remove _their own_ movement target but not
if it has been changed by something else in the intervening time.

I fixed this by passing a source every time you set a movement target
and adding a proc which only clears it if you are the source... but this
feels kind of ugly. I couldn't think of anything but if you have a
better idea let me know.

Also while I was doing this I turned it into a feature because I'm
crazy.
If you feed a mouse cheese by hand it will stop being scared of humans
and so will any other mice it attracts from eating more cheese. This is
mostly because I think industrial mouse farming to pass cargo bounties
is funny.
Mice controlled by a Regal Rat lose this behaviour and forget any past
loyalties they may have had.


https://user-images.githubusercontent.com/7483112/208779368-3bd1da0f-4191-4405-86e5-b55a58c2cd00.mp4

Oh also I removed a block about cancelling if you have another target
from the "hunt" behaviour, everywhere using this already achieves that
simply by ordering the actions in expected priority order and it was
messing with how I expected mice to work.
Now if they happen to stop by some cheese they will correctly stop
fleeing in order to eat it before continuing to run away.

## Why It's Good For The Game

Fixes a bug I kept running into.
Makes it possible to set up a mouse farm without them screaming
constantly.
Lets people more easily domesticate mice to support Ratatouille
gameplay.

## Changelog

:cl:
add: Mice who are fed cheese by hand will accept humans as friends, at
least until reminded otherwise by their rightful lord.
fix: Fixed a runtime preventing mice from acting correctly when trying
to flee and also eat cheese at the same time.
/:cl:

---
## [FrancisChukwuemeka/Fontend](https://github.com/FrancisChukwuemeka/Fontend)@[ec54e415a9...](https://github.com/FrancisChukwuemeka/Fontend/commit/ec54e415a9cde512212743638b4a73252585d088)
#### Saturday 2022-12-31 21:11:08 by Francis Chukwuemeka

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=, initial-scale=1.0">
    <link rel="stylesheet" href="Bio.css">
    <title>Adalia Cassius</title>
</head>
<body>
    <div class="block"><img src="My_images/adelia.jpg" width="200px" height="200px"></div>

        <h1>Adalia Cassius Biograghy</h1>
    <p class=>My name is Adelia Maria Cassius, <i> <b>I was born on 20/01/1987.</b></i> I am an International banker. My Address: Beldiceanu Nicolae, Strada 550074. My City: Sibiu în România. I have lived and worked in different countries in the world like Six Countries. I studied Accountancy in Lucian Blaga University of Sibiu. I later proceeded to get my masters degree in Economics in University of Bucharest.</p>
    <p class=>I later Study foreign Language at University of Silesia.foreign language offered by the School of the Polish Language and Culture of the University of Silesia. I married a Romanian man named Ionut, and I have one Son with him. I am the Branch head account auditing Poland branch. My first working experiences I work as account auditing at Banca Comerciala bank of Româna. But later I am looking for a green passion,as a International banker, I first got an offer from Banco Amigável Internacional Brazil branch.</p>
    <p class=>I am a divorced woman my Son and my Mother live under my care, I Divorced my ex husband in 2015 because he is addicted to hard drugs and alcoholism. I lose my father in 2010 after suffering from brain cancer ( glioblastoma). You can view all my photos and my other things you need to know about me. Thanks.</p>
    <h2>About My Work</h2>
    <p class=>At Banco Amigável Internacional Brazil branch I work as International bank cashier.But I later promoted to chief auditing officer at Brazil branch Banco Amigável Internacional. My brief profile Details, Sex: Female, Hight: 5 ft. 5 inches, Weight : 85.1 kg, I am correctly an accountant offer and Staff of Banco Amigável Internacional Poland a head accounting offer in Poland.I am a divorced woman I have only one Son name Adrian Cassius Ionut. My Father is late, but my Mother is still alive. She is 68 year of and lives with my Son in Romain.</p>
</body>
</html>
*{
    padding: 5px;
    margin: 1px;
    box-sizing: border-box;
}

body{
    background-color: beige;
    height: 100vh;
}

.block{
    display: flex;
    flex-wrap: wrap;
    flex-direction: column;
    justify-content: flex-end;
    width: 200px;
    height: 200px;
    border: black;
}

h1{
    font-style: bold;
    font-family: sans-serif;

}

h2{
    font-style: bold;
    font-family: sans-serif;
}

.p{
    font-size: medium;
    font-weight: 200;
    font-family: sans-serif;
    font-style: oblique;
    font: small-caps;
    font-variant-caps: petite-caps;
}

---
## [greenhas/spg_website](https://github.com/greenhas/spg_website)@[98fb0c8b75...](https://github.com/greenhas/spg_website/commit/98fb0c8b753cba0f2ef228242b65586dc55f6fee)
#### Saturday 2022-12-31 21:50:33 by Spencer Greenhalgh

post I've read this short novella at least four times already, but I received a physical copy for Christmas and couldn't help but give it another read. Despite being existentially horrifying, it's one of my favorite books of all time. The protagonist is a Mormon man who dies and wakes up to his surprise in hell. This hell is specifically promised to be finite, but it's a vast kind of finite: It's a Borges-inspired library that consists of every possible book (as if written by monkeys on typewriters), and once you find the book that tells your life story, you get out of hell.  It turns out, though, that this library is mind-bogglingly huge, so you could live billions of lifetimes before finding your book. The point of the book is to problematize eternity: If a "finite" hell is this awful, how much worse is an eternal hell? Heck, even an eternal heaven doesn't necessarily sound great when you're done with the book. For such a depressing premise, though, it's so well done—and leaves so much to think about.

---
## [seanpdoyle/turbo](https://github.com/seanpdoyle/turbo)@[c8dbbab791...](https://github.com/seanpdoyle/turbo/commit/c8dbbab79144f5885d704ad59890e789be3f66d0)
#### Saturday 2022-12-31 22:13:02 by Sean Doyle

Extract `FrameVisit` to drive `FrameController`

The problem
---

Programmatically driving a `<turbo-frame>` element when its `[src]`
attribute changes is a suitable end-user experience in consumer
applications. It's a fitting black-box interface for the outside world:
change the value of the attribute and let Turbo handle the rest.

However, internally, it's a lossy abstraction.

For example, when the `FrameRedirector` class listens for page-wide
`click` and `submit` events, it determines if their targets are meant to
drive a `<turbo-frame>` element by:

1. finding an element that matches a clicked `<a>` element's `[data-turbo-frame]` attribute
2. finding an element that matches a submitted `<form>` element's `[data-turbo-frame]` attribute
3. finding an element that matches a submitted `<form>` element's
   _submitter's_ `[data-turbo-frame]` attribute
4. finding the closest `<turbo-frame>` ancestor to the `<a>` or `<form>`

Once it finds the matching frame element, it disposes of all that
additional context and navigates the `<turbo-frame>` by updating its
`[src]` attribute. This makes it impossible to control various aspects
of the frame navigation (like its "rendering" explored in
[hotwired/turbo#146][]) outside of its destination URL.

Similarly, since a `<form>` and submitter pairing have an impact on
which `<turbo-frame>` is navigated, the `FrameController` implementation
passes around a `HTMLFormElement` and `HTMLSubmitter?` data clump and
constantly re-fetches a matching `<turbo-frame>` instance.

Outside of frames, page-wide navigation is driven by a `Visit` instance
that manages the HTTP life cycle and delegates along the way to a
`VisitDelegate`. It also pairs calls to visit with a `VisitOption`
object to capture additional context.

The proposal
---

This commit introduces the `FrameVisit` class. It serves as an
encapsulation of the `FetchRequest` and `FormSubmission` lifecycle
events involved in navigating a frame.

It's implementation draws inspiration from the `Visit`, `VisitDelegate`,
and `VisitOptions` pairing. Since the `FrameVisit` knows how to unify
both `FetchRequest` and `FormSubmission` hooks, the resulting callbacks
fired from within the `FrameController` are flat and consistent.

Extra benefits
---

The biggest benefit is the introduction of a DRY abstraction to
manage the behind the scenes HTTP calls necessary to drive a
`<turbo-frame>`.

With the introduction of the `FrameVisit` concept, we can also declare a
`visit()` and `submit()` method for `FrameElementDelegate`
implementations in the place of other implementation-specific methods
like `loadResponse()` and `formSubmissionIntercepted()`.

In addition, these changes have the potential to close
[hotwired/turbo#326][], since we can consistently invoke
`loadResponse()` across `<a>`-click-initiated and
`<form>`-submission-initiated visits. To ensure that's the case, this
commit adds test coverage for navigating a `<turbo-frame>` by making a
`GET` request to an endpoint that responds with a `500` status.

[hotwired/turbo#146]: https://github.com/hotwired/turbo/pull/146
[hotwired/turbo#326]: https://github.com/hotwired/turbo/issues/326

---
## [Alonefromhell/cmss13](https://github.com/Alonefromhell/cmss13)@[70bcd3b6fb...](https://github.com/Alonefromhell/cmss13/commit/70bcd3b6fbcf17b4c26640321f23c83da0ab80a3)
#### Saturday 2022-12-31 23:34:35 by carlarctg

Queen eye shuffles weed sprites when passing over them. (#1901)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Queen eye shuffles weed sprites when passing over them.

Fixed some single letter vars so the mantainer agenda can't delay this
PR from merging.



<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game


> Queen eye shuffles weed sprites when passing over them.

It's a way for marines to know there's an entire queen eye looking over
them. Basically means an MD isn't 100% necessary to know the queen will
broadcast the location of your flank to the entire hive.

https://streamable.com/kmnd72

It's more subtle than i wanted it to be, but WCYD. Also doesn't work on
corner sprites.

Also, it looks fucking creepy as hell! It's awesome.

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
add: Queen eye shuffles weed sprites when passing over them.
fix: Fixed some single letter vars so the mantainer agenda can't delay
this PR from merging.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---

