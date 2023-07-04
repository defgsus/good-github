## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-07-03](docs/good-messages/2023/2023-07-03.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,067,068 were push events containing 3,343,734 commit messages that amount to 273,301,379 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 57 messages:


## [UFifty50/AnEngine](https://github.com/UFifty50/AnEngine)@[db413fb930...](https://github.com/UFifty50/AnEngine/commit/db413fb930f3af56f095e71aba88a5d1e51102e8)
#### Monday 2023-07-03 00:07:43 by UFifty50sh

quite a lot, added ShaderUniform struct FUCK YOU C++ COMPILER

---
## [effigy-se/effigy-se](https://github.com/effigy-se/effigy-se)@[fd11ae6c90...](https://github.com/effigy-se/effigy-se/commit/fd11ae6c90bc7539616dcdc50f90cfba0ce1a6fe)
#### Monday 2023-07-03 00:17:10 by ChungusGamer666

SPECIES NUKING 2023: Head flags 3 & Knuckles: Fixes some growing pains with head flags  (#76440)

## About The Pull Request

Fixes https://github.com/tgstation/tgstation/issues/76422
This was caused by me somehow not using the wrapper there and not
noticing it

Also fixes hair gradients and facial hair gradients. I am pretty sure
they were uhh, being hidden behind the actual hair/facial hair. Oops.

Also also fixes spawning yourself as a human as admin and getting random
hair colors. That was just a failure to update the icon after updating
everything, I think?

Additionally, to totally babyproof all of this, ensures that head_flags
involved stuff gets applied AFTER species by creating a new preference
priority, and uses two separate wrappers to apply gradient style and
color.

Here's this absolute hellspawn to prove that everything works.

![image](https://github.com/tgstation/tgstation/assets/82850673/7ed29a68-cb60-4b28-996c-3be0e7331be8)

![image](https://github.com/tgstation/tgstation/assets/82850673/e57128be-0d7c-46ad-90dd-ee25981d0fea)

![image](https://github.com/tgstation/tgstation/assets/82850673/5c3619a8-fe6f-42b3-9fdc-12277d568e8d)

![image](https://github.com/tgstation/tgstation/assets/82850673/fdd13000-2220-47ad-8e02-44bc75a4a907)

Sorry for being so damn good at breaking this codebase.

## Why It's Good For The Game

Bugs are bad they make you mad

## Changelog

:cl:
fix: Hair and facial hair gradients work again now
fix: Facial hair colors apply properly again
fix: Admin spawned characters will get hair color preferences applied
properly
/:cl:
# Conflicts:
#	code/modules/mob/living/carbon/human/human_helpers.dm

---
## [Youtubeboy139/Skyrat-tg](https://github.com/Youtubeboy139/Skyrat-tg)@[79febdf95d...](https://github.com/Youtubeboy139/Skyrat-tg/commit/79febdf95dbcdb81d6a8027dc21deba19f8e659e)
#### Monday 2023-07-03 00:34:42 by SkyratBot

[MIRROR] New planetary exclusive random event/unfavorable situation, Chasmic Earthquake [MDB IGNORE] (#21778)

* New planetary exclusive random event/unfavorable situation, Chasmic Earthquake (#75864)

## About The Pull Request

https://github.com/tgstation/tgstation/assets/28870487/2451bc69-db1e-420d-9a18-2f899ca65427

This introduces a new unfavorable situation (non-antagonist random
events that dynamic triggers under certain circumstances), restricted to
planetary maps (Icebox). An earthquake occurs, felt by everyone on the
map, forming a fault that tears the a hole somewhere on the station.

The fault zone is indicated by shaking tiles, which gives a chance
(about 30 seconds) for you to move your machinery/property/crewmembers
out of the way. If you're on those tiles when the fault forms, get ready
to take a nasty fall.

Anything caught in the fault zone as it collapses inward will be
destroyed, violently, _before_ being dropped down into the z-level
below.

![image](https://github.com/tgstation/tgstation/assets/28870487/56916c9f-c8da-4ffb-9d8b-7e940e92bbc2)

These can also happen as a random event, however their rarity is on-par
with that of a meteor storm.

This also adds a helper for finding a midpoint turf between two provided
turfs, thanks to ZephyrTFA.

This idea basically possessed me over the course of a few days, and I
found myself unable to work on anything else until I had it complete.
I'm glad its done.
## Why It's Good For The Game

Gives Icebox its own big "environmental disaster" event. I'm hoping it
isn't received as being too destructive, but mind that this is meant to
be an equal to the dreaded meteor storm.

Also makes it so that unfavorable events aren't a coinflip between a
portal storm/rod on planetary maps.
## Changelog
:cl: Rhials
add: Chasmic Earthquake random event, exclusive to Icebox. Tears a huge
chasm in the hull of the station. Watch out for shaking tiles!
sound: Adds sounds for distant rumbling, metal creaking, and rubble
shaking.
imageadd: Achievement icon for getting sucked up in an earthquake chasm.
/:cl:

* New planetary exclusive random event/unfavorable situation, Chasmic Earthquake

---------

Co-authored-by: Rhials <Datguy33456@gmail.com>

---
## [yarnpkg/berry](https://github.com/yarnpkg/berry)@[21fcc792bf...](https://github.com/yarnpkg/berry/commit/21fcc792bf83825aa051c51c96cdc683ee85d20b)
#### Monday 2023-07-03 00:36:49 by Maël Nison

Sets the default compression to 0 (#5526)

**What's the problem this PR addresses?**

Cache compression doesn't seem the best option nowadays:

- It adds significant time to installs
- It adds a non-negligible runtime overhead (partially related, #1817)
- It prevents Git from diffing archives when they're modified

Its main advantage is for some amazingly large packages, where storing
them inside a Git repository would be impossible (GitHub has a 600MB
file limit). But since we changed the cache default to
`enableGlobalCache: true`, this isn't relevant by default, so the cache
compression should be set to zero.

One potential issue is how it may give the impression that Yarn became
worse for global cache users. We don't believe it's the case (Git can
delta uncompressed archives in some measure, making it less expensive to
upgrade from one package version to another), but to the average eye it
may not look as such.

**How did you fix it?**

This diff sets the new default compression setting to 0.

To avoid breaking projects' (or at least not making the migration more
difficult), I added a rule to automatically set `compressionLevel` (and
`enableGlobalCache`) to their 3.x default values when running `yarn
install` in a 3.x project. When users are ready they can remove these
settings and re-run the install.

I kept the current compression level on our repository to avoid changing
all archives again. I think we'll have to think of purging the
repository in some form to migrate it to `compressionLevel: 0`.

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
## [UFifty50/AnEngine](https://github.com/UFifty50/AnEngine)@[fc4ce0e356...](https://github.com/UFifty50/AnEngine/commit/fc4ce0e356b62868da094e4df25f32fb778d23a2)
#### Monday 2023-07-03 00:40:40 by UFifty50sh

removed some MSVC extension specific code, added movement to the SandBox
Still fuck you C++ typing rules, I beat you with some polymorphism fuckery

---
## [MemedHams/Shiptest](https://github.com/MemedHams/Shiptest)@[9aa3fb2901...](https://github.com/MemedHams/Shiptest/commit/9aa3fb29012991ce7a9d755e640a1af65f3fe319)
#### Monday 2023-07-03 00:59:34 by thgvr

Fixes a good chunk of Vox sprites. Removes environmental regulator (#2092)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Oh god the pain. Oh god. The unbearable pain. Why.

Adds a ton of unused vox sprites from Drawsstuff.
Cleans up the files for sprites we don't actually have
Ensures they are pathed correctly, with flags set correctly.
I spent five hours on this in one sitting after being upset at shitty
vox mechanics/sprite support again. They're cool and unique and it was
sad.
Removes the Environmental Regulator.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
1. Vox sprites were incomplete. This completes them a little bit more.
2. The environmental regulator isn't fun. This will remove the regulator
and vox needing to use it. It was buggy, poorly made, and just not fun
even when it worked correctly. Vox aren't nearly strong enough to be
constantly crippled.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: A metric ton of Vox sprites
del: Vox no longer need environmental regulators
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [MemedHams/Shiptest](https://github.com/MemedHams/Shiptest)@[c84e40255d...](https://github.com/MemedHams/Shiptest/commit/c84e40255d466e37983e5cb03c110e7dd8ab90c8)
#### Monday 2023-07-03 00:59:34 by Imaginos16

Ports pinging in Adminsay from /tg/station (#2111)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Does what it says on the tin, porting a behavior that allows you to ping
a person in admin say by just doing @(ckey) from /tg/station in PR
[#61712](https://github.com/tgstation/tgstation/pull/61712)


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/fc756e0f-668f-4641-9bcd-689d6548d343)

Oh and this PR I guess fixes a hilarious issue where **someone** wrote
'tgstation.dme' instead of 'shiptest.dme' where they shouldn't have.
Whoops!

Most cool of all, which was completely unintentional by me, ports Datum
linking (partially), as well as Ticket linking, respectively added in
PRs [#65154](https://github.com/tgstation/tgstation/pull/65154) and
[#65634](https://github.com/tgstation/tgstation/pull/65634)


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/d6f980ee-c490-4f8d-a76c-81447aeb7658)



<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
I swear to fucking christ if I have to log into the game one more
goddamn time as an admin only to have 2 people being DJs, another one
spriting, and another one doing jack shit while not paying attention at
the server when I am trying to solve a crucial ticket, I'll develop an
aneurysm.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: Ryll-Ryll/Shaps
admin: Adds pinging to adminsay!
admin: Adds the ability to link datums!
admin: Adds linking tickets to asay! Simply put a # followed by a ticket
number for it to be linked in the chat!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [splashcat-ink/splashcat](https://github.com/splashcat-ink/splashcat)@[f1bd3fc3c3...](https://github.com/splashcat-ink/splashcat/commit/f1bd3fc3c37f5f6470a8bca288d2eaad4449d7ad)
#### Monday 2023-07-03 01:05:34 by kitt

oops, someone is stupid!!!!!!!!!!!!!!!!!!

fuck this life.

---
## [terr0rist/DiscordShit](https://github.com/terr0rist/DiscordShit)@[c9775837ae...](https://github.com/terr0rist/DiscordShit/commit/c9775837ae63a65cb243d31a9b4cad7d9df31765)
#### Monday 2023-07-03 01:37:01 by Astral

nvm delete cuz the code DOESNT FUCKING WORK WHY CANT ONE THING I DO GO RIGHT I HATE MY LIFE

---
## [knative-automation/client-pkg](https://github.com/knative-automation/client-pkg)@[44453375bd...](https://github.com/knative-automation/client-pkg/commit/44453375bd5527e2d08a397e960f7adac9582c78)
#### Monday 2023-07-03 01:49:47 by Knative Automation

upgrade to latest dependencies

bumping knative.dev/serving 2c1bb07...4c3b36c:%0A  > 4c3b36c Update net-gateway-api nightly (# 14136)%0A  > 9a75a93 Update net-istio nightly (# 14132)%0A  > ca618b7 Update net-certmanager nightly (# 14131)%0A  > ea3e9c3 Update net-contour nightly (# 14130)%0A  > 2e7d6e4 Update community files (# 14128)%0A  > 63fa389 Allow to set QP resources per service (# 14038)%0A  > 9310e4d Update net-kourier nightly (# 14125)%0A  > 0462ce6 Update net-istio nightly (# 14126)%0A  > 2813b9a Update net-gateway-api nightly (# 14119)%0A  > eaf666e Update net-istio nightly (# 14116)%0A  > 53169cd Update net-istio nightly (# 14112)%0A  > e865aa7 Update net-contour nightly (# 14109)%0A  > 921daf8 Update net-certmanager nightly (# 14111)%0A  > bb581cc Update net-kourier nightly (# 14110)%0A  > fbfffc0 upgrade to latest dependencies (# 14108)%0A  > bcf9274 upgrade to latest dependencies (# 14101)%0A  > f085b30 fix: requests are sent to all pods even if cc=1 and the parity of activatorCount and podTracker is different (# 14022)%0A  > 9772417 Update net-kourier nightly (# 14107)%0A  > f6d0c7b Update net-contour nightly (# 14106)%0A  > 560e0ea Update net-certmanager nightly (# 14105)%0A  > 51f4f1e Update net-istio nightly (# 14104)%0A  > 18519b1 Update net-contour nightly (# 14079)%0A  > 38c155e Add chainguard-dev/actions for creating kind cluster (# 14018)%0A  > 74c57d8 Update net-istio nightly (# 14098)%0A  > 5a9c574 Update net-kourier nightly (# 14096)%0A  > 3a6c2b6 upgrade to latest dependencies (# 14095)%0A  > 5a90438 Update net-istio nightly (# 14091)%0A  > dc0692a Update net-istio nightly (# 14088)%0A  > 0fbd780 Update net-certmanager nightly (# 14087)%0A  > 6f63c98 Update net-kourier nightly (# 14086)%0A  > e74f5f4 Update net-gateway-api nightly (# 14085)%0A  > 1587070 Update net-kourier nightly (# 14081)%0A  > 2e00e9f Update net-certmanager nightly (# 14080)%0A  > a3c7864 Update net-istio nightly (# 14078)%0A  > 384b889 Update net-gateway-api nightly (# 14077)%0A  > 7d0f963 Change storage version of DomainMapping to v1beta1 (# 14058)%0A  > e8b6f05 Update net-gateway-api nightly (# 14068)%0A  > 41e4212 Get certificate reconciler from `networking` instead of `control-protocol` (# 14072)%0A  > e71b933 Update net-certmanager nightly (# 14070)%0A  > 8f516b6 Update net-kourier nightly (# 14069)%0A  > a2bb4aa upgrade to latest dependencies (# 14071)%0A  > c95f17b Update community files (# 14067)%0A  > bf48e64 Remove deprecated internalEncryption dependency (# 14064)%0A  > 6b87d67 Update net-istio nightly (# 14065)%0A  > fbecf34 refactor throttler_test.go (# 14055)%0A  > 349b2d6 Change minimum TLS version to 1.3 for internal encryption (between activator and queue-proxy) (# 13887)%0A  > d07bf78 Update net-contour nightly (# 14049)%0A  > aa023e8 Update net-istio nightly (# 14048)%0A  > 8fc4bb9 Update net-gateway-api nightly (# 14047)%0A  > 135be30 Update net-certmanager nightly (# 14046)%0A  > 8da71b5 Update net-kourier nightly (# 14042)%0A  > 13a4e46 poll until timeout - don't error out if the deployment can't be found (# 14027)%0A  > 31c2b7e upgrade to latest dependencies (# 14043)%0A  > 6a6e417 Update net-istio nightly (# 14041)%0A  > 807fc2c Update net-certmanager nightly (# 14040)%0A  > 3c23945 drop safe to evict annotations (# 14035)%0A  > fca5c14 Update net-gateway-api nightly (# 14033)%0A  > c12c917 Update net-contour nightly (# 14034)%0A  > 2da856d Update net-kourier nightly (# 14032)%0A  > d7c8779 Update net-certmanager nightly (# 14031)%0A  > aaf01dc Update net-istio nightly (# 14030)%0A  > bdaa436 RandomChoice 2 policy wasn't random when the number of targets is 2 (with equal weight) (# 14028)%0A  > c91f8c4 Fix metrics reporting period (# 14019)%0A  > 9f60969 Update net-kourier nightly (# 14004)%0A  > 6020cec Update net-istio nightly (# 14025)%0A  > 88cae7f Update net-gateway-api nightly (# 14016)%0A  > a143bf8 Update net-contour nightly (# 14015)%0A  > c2be582 Update net-certmanager nightly (# 14014)%0A  > 3450f0a upgrade to latest dependencies (# 14013)%0A  > 35cfd8f [Automated] Update net-gateway-api nightly (# 14003)%0A  > 08a9708 Update net-istio nightly (# 14009)%0A  > 5074b4c Update net-contour nightly (# 14010)%0A  > e8cb343 upgrade to latest dependencies (# 13999)%0A  > 1261074 Update net-certmanager nightly (# 14002)%0A  > f987ca6 Bump kind to 0.19 (# 14008)%0A  > fbb7fa1 Update community files (# 13998)%0A  > bff1d80 Remove 1.24 kind version (# 14007)%0A  > a657321 Update net-kourier nightly (# 13993)%0A  > d75b0f0 Update net-contour nightly (# 13990)%0A  > 6d26f54 upgrade to latest dependencies (# 13991)%0A  > df5001f Update net-certmanager nightly (# 13992)%0A  > 2594084 upgrade to latest dependencies (# 13989)%0A  > 7c303fa Update cluster-version to 1.25 (# 13988)%0A  > 9e751a2 Update net-certmanager nightly (# 13974)%0A  > 7b35cfb upgrade to latest dependencies (# 13987)%0A  > 99800ed Set default domain to cluster's domain (# 13964)%0A  > c90fabf Metric annotations work with global class config (# 13978)%0A  > da31cd1 Update net-kourier nightly (# 13975)%0A  > f457924 Update net-contour nightly (# 13976)%0A  > 14ad4d1 upgrade to latest dependencies (# 13973)%0A  > 00ddfd9 Update net-kourier nightly (# 13972)%0A  > fc63583 Update net-kourier nightly (# 13966)%0A  > 219285e Update net-kourier nightly (# 13959)%0A  > 2fa05bd Min TLS for tag to digest defaults to 1.2 again and is configurable (# 13962)%0A  > 43df348 Update net-contour nightly (# 13958)%0A  > 50a9f22 Update net-certmanager nightly (# 13961)%0A  > 4e379cb Update net-gateway-api nightly (# 13957)%0A  > 3d53294 Update net-istio nightly (# 13960)%0A  > ea2a6c8 :lipstick: Install ko using setup-ko, from ko-build (# 13951)%0A  > e5070cd upgrade to latest dependencies (# 13950)%0A  > 9778f2d Update net-istio nightly (# 13949)%0A  > f27ba4e Update net-certmanager nightly (# 13944)%0A  > 2840301 Update net-kourier nightly (# 13945)%0A  > 117a642 Update net-gateway-api nightly (# 13943)%0A  > 84a2230 Update net-contour nightly (# 13942)%0A  > 7aa5edb upgrade to latest dependencies (# 13941)%0A  > 01707d8 upgrade to latest dependencies (# 13940)%0A  > b7d5e8d Update net-istio nightly (# 13939)%0A  > 5e056a0 Update net-certmanager nightly (# 13926)%0A  > 35efd12 Update net-contour nightly (# 13929)%0A  > f476717 Update net-istio nightly (# 13935)%0A  > bd8e37c Update net-gateway-api nightly (# 13925)%0A  > 37a7010 Update net-kourier nightly (# 13934)%0A  > f47802d Update community files (# 13933)%0A  > 990d701 Update net-kourier nightly (# 13928)%0A  > ff9f03d Update net-istio nightly (# 13927)%0A  > 690c525 upgrade to latest dependencies (# 13924)%0A  > 1dd07a7 Update community files (# 13923)%0A  > 66141b8 Update net-istio nightly (# 13920)%0Abumping k8s.io/code-generator 6523e22...eec869e:%0A  > eec869e Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > 824419b Bump runc go module v1.1.4 -> v1.1.6%0A  > ba94e65 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 6276bf2 Update golang.org/x/net to v0.7.0%0A  > 73b9c40 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 882af80 Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 6063700 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > b615940 Update golang.org/x/net 1e63c2f%0A  > 11d5c4c update k8s.io/utils to fix util tracing panic%0A  > 081720d Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > d44fa8c dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > 300cdcf Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > e0ef4aa Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > 557ce1f Merge pull request # 113126 from alexzielenski/remove-unwanted-replace%0A  > f86120d remove errant replace%0A  > d6a8b70 Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > f77ba6d dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > 3bbe215 Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > e80bbc4 Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > d403dc0 update kube-openapi%0A  > 790e4bc update fsnotify to v1.6.0%0A  > 27bd7d9 Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 4731e5c Bump golang.org/x/text to v0.3.8%0A  > a8a213c Merge pull request # 112875 from pohly/update-yaml%0A  > 5f5bab9 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 983d5d0 Merge pull request # 112819 from thockin/no-make-generators%0A  > c35177b Format calls to codegens%0A  > 83929d0 Codegens: Do not auto-set boilerplate path%0A  > 1d82d12 Merge pull request # 112705 from stevekuznetsov/skuznets/fix-comment%0A  > c3414a0 clients: clarify a misleading comment%0A  > 998e449 Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > e4543b2 Update to latest k8s.io/utils to pick up changes%0A  > 8e999f2 Merge pull request # 112613 from dims/update-github.com/go-openapi/jsonreference-to-drop-github.com/PuerkitoBio/purell%0A  > 524127d update github.com/go-openapi/jsonreference to drop github.com/PuerkitoBio/purell%0A  > 4ca0baf Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > b54a056 Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 350c30a updated etcd to v3.5.5 and newer otel libraries as well%0A  > 5f3f945 e2e: bump ginkgo to v2.2.0%0A  > 2e5cca7 Merge pull request # 112200 from pohly/client-go-shared-informer-factory-shutdown%0A  > c3fdc3c Merge pull request # 112349 from pohly/klog-update%0A  > e4b7976 client-go: support waiting for SharedInformerFactory shutdown%0A  > 135f69b build: update to klog v2.80.1%0A  > f60067d Merge pull request # 112341 from enj/enj/i/second_time_is_the_charm%0A  > 7c81c99 Merge pull request # 111768 from weilaaa/feature_add_symmetric_difference_in_sets_string%0A  > 8468f16 Remove in-tree credential plugins (again)%0A  > 9b98ed3 add symmetric difference in sets%0A  > 34125ff Merge pull request # 112199 from pohly/klog-update%0A  > a055687 dependencies: update to klog v2.80.0%0A  > 16cba21 Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > e051ad0 dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > 3a31bb1 Merge pull request # 111934 from deads2k/apply-gen%0A  > 4d73156 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 1382941 make applyconfiguration-gen skip generation for types that have generated clients and lack objectmeta%0A  > 03a75ea Bump prometheus/client_golang to v1.13.0%0A  > 17196da update the apply generator to use the same package the the client generator expects%0A  > a4e23d1 Merge pull request # 111566 from inosato/remove-ioutil-from-code-generator%0A  > a6a370c make applyconfiguration-gen handle pointers to slices%0A  > 087714e Merge pull request # 109884 from qzoscar/patch-1%0A  > fc00858 Remove ioutil from code-generator%0A  > ed79ca3 make applyconfiguration-gen work for resources without objectmeta%0A  > fea40fb Merge pull request # 111918 from liggitt/in-tree-auth%0A  > 3612509 fix a broken link%0A  > 78677a3 update the applyconfiguration-gen flag external-applyconfigurations to work%0A  > ad6af70 Revert "Remove gcp and azure auth plugins"%0A  > 7ba56cb applyconfiguration-gen handling of types that have a non-embedded use of TypeMeta%0A  > 97fa351 Merge pull request # 111696 from liggitt/go119mod%0A  > d71f529 add metav1.OwnerReference to the default external configurations to ease generation%0A  > 2b9093f Update go.mod to go1.19%0Abumping golang.org/x/net 8e2b117...dfa2b5d:%0A  > dfa2b5d go.mod: update golang.org/x dependencies%0A  > 8c4ef2f hmtl: add security section to package comment%0A  > 1d46ed8 html: have Render escape comments less often%0A  > 569fe81 html: add "Microsoft Outlook comment" tests%0Abumping github.com/matttproud/golang_protobuf_extensions c182aff...c182aff:%0Abumping golang.org/x/mod b3066c3...b710602:%0A  > b710602 sumdb/dirhash: correct documentation of hash%0A  > a42224d all: replace io/ioutil with io and os package%0A  > 77d797e sumdb/dirhash: fix a panic when argument is not a directory%0A  > 7c05a44 sumdb/note: remove dependency on golang.org/x/crypto/ed25519%0Abumping github.com/prometheus/client_golang 64435fc...254e546:%0A  > 254e546 Merge pull request # 1162 from kakkoyun/cut-1.14.0%0A  > 07d3a81 Merge pull request # 1161 from prometheus/release-1.13%0A  > c8a3d32 Cut v1.14.0%0A  > 870469e Test and support 1.19 (# 1160)%0A  > 53e51c4 Merge pull request # 1157 from prometheus/cut-1.13.1%0A  > b785d0c Fix go_collector_latest_test Fail on go1.19 (# 1136)%0A  > 79ca0eb Added tip from Björn + Grammarly.%0A  > 4d54769 Fix float64 comparison test failure on archs using FMA (# 1133)%0A  > 078f11f Cut 1.13.1 release (+ documenting release process).%0A  > 5f202ee Merge pull request # 1150 from prometheus/sparsehistogram%0A  > ddd7f0e Fix race condition with Exemplar in Counter (# 1146)%0A  > 0859bb8 Merge pull request # 1152 from jessicalins/update-to-custom-reg%0A  > fffb76c Merge branch 'main' into sparsehistogram%0A  > 1f93f64 Fix `CumulativeCount` value of `+Inf` bucket created from exemplar (# 1148)%0A  > 10b0550 Fix race condition with Exemplar in Counter (# 1146)%0A  > a340ca4 Run make format%0A  > e92a8c7 Avoid the term 'sparse' where possible%0A  > 8cc2b6c Fix double-counting bug in promhttp.InstrumentRoundTripperCounter (# 1118)%0A  > dcea97e Fix `CumulativeCount` value of `+Inf` bucket created from exemplar (# 1148)%0A  > 6056615 Update random example to use custom registry%0A  > d31f13b Add SparseBucketsZeroThresholdZero and groom doc comments%0A  > 9801a4e Examples: Replace deprecated WithGoCollections with WithGoCollectorRuntimeMetrics (# 1130)%0A  > 0b7f488 Update simple example to use custom registry%0A  > 58a8ca4 examples: Adjust doc comment for native histograms%0A  > 7c46c15 Clarify documentation around what constructors do (# 1125)%0A  > 9b5c5b8 Update basic example to use custom registry%0A  > 4e71e6f Update prometheus/client_model dependency%0A  > 83d56b1 Extend prometheus.Registry to implement Collector (# 1103)%0A  > 111fae1 Merge branch 'main' into sparsehistogram%0A  > 4c41dfb Clarify exemplar(Add|Observe) by renaming to (add|observe)WithExemplar (# 1122)%0A  > 25bc188 Merge pull request # 1144 from prometheus/beorn7/histogram2%0A  > f73e3cc Fix double-counting bug in promhttp.InstrumentRoundTripperCounter (# 1118)%0A  > 95cf173 Merge branch 'main' into sparsehistogram%0A  > 6942f9e sparse buckets: Fix handling of +Inf/-Inf/NaN observations%0A  > c7aa2a5 Merge pull request # 1113 from prometheus/release-1.13%0A  > ec86ef1 Merge pull request # 1092 from prometheus/beorn7/histogram%0A  > 1e61b8e Update common Prometheus files (# 1111)%0A  > 6141a07 Merge branch 'main' into sparsehistogram%0A  > 8cbcd40 histograms: Move to new exposition protobuf format%0A  > 5a321c7 Merge branch 'foo-commit' into sparsehistogram%0A  > e93e384 Merge branch 'beorn7/release' into sparsehistogram%0A  > e203144 Merge branch 'release-1.12' of github.com:prometheus/client_golang into release-1.12%0A  > 525d042 Merge branch 'main' into sparsehistogram%0A  > a516626 Merge branch 'release-1.12' into beorn7/release%0A  > a27b6d7 Fix conflicts%0A  > 6ba7871 Merge branch 'main' into sparsehistogram%0A  > eb59a7b Histogram: Fix bug with negative schemas (# 1054)%0A  > b237230 Merge branch 'main' into sparsehistogram%0A  > 294cca4 Merge branch 'main' into sparsehistogram%0A  > 70253f4 Fix typo in doc comment%0A  > 5b19c55 Merge branch 'master' into sparsehistogram%0A  > dfbcc28 Merge pull request # 901 from prometheus/beorn7/histogram%0A  > 84fcaff Merge branch 'master' into sparsehistogram%0A  > 263be8d Refactoring of sparse histograms%0A  > 9ef5f90 Allow a zero threshold of zero%0A  > 2409960 Implement strategy to limit the sparse bucket count%0A  > aa6f67a Add TODO about bucket search optimization%0A  > 43f31c2 Merge pull request # 886 from prometheus/beorn7/histogram%0A  > 5aa8534 Merge branch 'master' into sparsehistogram%0A  > 5142344 Pin client_model to the most recent sparsehistogram commit%0A  > 97eb041 Tidy go.sum%0A  > 6c4e0ef Add tests for sparse histogram%0A  > 553ed73 Fix lint warning%0A  > 31318b7 Switch to base-2 buckets%0A  > b7a540a Fix test%0A  > a9df0ba Update prometheus/client_model%0A  > ce36ee3 Merge branch 'master' into beorn7/histogram%0A  > d698336 Merge branch 'master' into beorn7/histogram%0A  > 08104a0 Minor doc comment fixes%0A  > a9d0066 Add note about pow-of-10 precision issue%0A  > d1f5366 Fix span offset%0A  > abe540f Encode sparse histograms in protobuf%0A  > c98db4e Demo sparse histograms%0Abumping k8s.io/apiextensions-apiserver 2c55649...52c998e:%0A  > 52c998e Update dependencies to v0.26.5 tag%0A  > 186ff9b Merge pull request # 117274 from jkh52/release-1.26-knp-0.0.37%0A  > b7b18f5 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > ee5015a Bump konnectivity-client to 0.0.37%0A  > 9ce75f3 Bump runc go module v1.1.4 -> v1.1.6%0A  > e9d194a Merge pull request # 115599 from jkh52/release-1.26-knp-0.0.36%0A  > d7df0be Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 9152c67 Bump konnectivity-client to v0.0.36%0A  > 89cec57 Update golang.org/x/net to v0.7.0%0A  > f72cc5c Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 28eb995 Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 33db789 Merge pull request # 114861 from jpbetz/release-1.26%0A  > a06e03d Merge pull request # 114927 from jkh52/release-1.26-knp-metrics%0A  > 0859963 Cherry pick 114857 to release-1.26%0A  > 5183885 Bump konnectivity-client to v0.0.35%0A  > 6e13726 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > c338f3e Update golang.org/x/net 1e63c2f%0A  > 9768bad sync: update go.mod%0A  > f9c2bba fix aggregated discovery version sorting%0A  > d2c9e18 Merge pull request # 113171 from Jefftree/aggregated-discovery-generic%0A  > 470c040 Merge pull request # 113577 from pacoxu/prometheus-client%0A  > 915a888 add crds to aggregated discovery%0A  > 92430b6 Merge pull request # 113314 from cici37/celIntegration%0A  > ac326ca upgrade prometheus-client to v1.14.0%0A  > 5a6bf16 Merge pull request # 113688 from dashpole/update_utils%0A  > 67b0610 Integrate cel admission with API.%0A  > 84fed82 upgrade github.com/prometheus/client_golang to v1.13.1%0A  > 077b441 update k8s.io/utils to fix util tracing panic%0A  > 5bbf20d Adding new api version of admissionregistration.k8s.io v1alpha1 for CEL in Admission Control%0A  > 3b533ba Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > 975bbeb dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > ae2b4c3 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > c4deae9 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > bc4263f Merge pull request # 113172 from dashpole/endpoint_handler_tracing%0A  > f6c164e migrate apiserver utiltrace usage to component-base/tracing%0A  > 53e3726 Merge pull request # 113015 from ritazh/crencryption%0A  > c8d8a9f Enable encryption for custom resources%0A  > 6405068 Merge pull request # 113325 from panslava/fix-time-since-defer%0A  > 508e399 Fix time.Since() in defer. Wrap in anonymous function%0A  > 5f8e59e Merge pull request # 112691 from aimuz/apiextensions-apiserver-change-to-cmp%0A  > c996139 Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > f83e03c apiextensions-apiserver: change k8s.io/apimachinery/pkg/util/diff to github.com/google/go-cmp/cmp%0A  > b68fc51 dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > 49c41b4 Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > 3aaa2a0 Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > d9f6ebd update kube-openapi%0A  > 82e3ba4 Merge pull request # 112789 from enj/enj/r/kms_load_once_v2%0A  > 7423813 update fsnotify to v1.6.0%0A  > 8bf3487 Merge pull request # 113011 from jpmcb/cobra-1.6.0%0A  > d34393e Load encryption config once%0A  > 6ba582f Bumps cobra from 1.5.0 to 1.6.0%0A  > 8e0697b Merge pull request # 113022 from logicalhan/webhook-metrics%0A  > 90c63e0 Merge pull request # 112926 from jiahuif-forks/refactor/cel-out-of-apiextensions%0A  > 548c480 unparameterize 'webhook' from conversion metrics since it's the only one%0A  > 77badb8 Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 609e270 use DefaultMaxRequestSizeBytes for maxRequestSizeBytes.%0A  > 04f26fa Bump golang.org/x/text to v0.3.8%0A  > dd981e1 move CEL package to apiserver package.%0A  > 1644998 Move celopenapi/model to staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/cel/ (# 109959)%0A  > 08d44e8 Merge pull request # 112875 from pohly/update-yaml%0A  > 1300140 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 5fb82bd Merge pull request # 112819 from thockin/no-make-generators%0A  > f5f5279 Codegens: Do not auto-set boilerplate path%0A  > f22ee73 Merge pull request # 112738 from liggitt/proto-tag%0A  > ba7f1b7 Merge pull request # 112689 from cheftako/master%0A  > 7ac7774 github.com/matttproud/golang_protobuf_extensions v1.0.2%0A  > e678457 Merge pull request # 112748 from wojtek-t/lock_ssa_gate%0A  > 0aca5a6 Bump konnectivity-client to v0.0.33%0A  > 9be4b4a Lock ServerSideApply feature to true%0A  > 7b53cb7 Merge pull request # 111980 from aramase/kms%0A  > f40a683 Merge pull request # 112705 from stevekuznetsov/skuznets/fix-comment%0A  > 4cd9125 Add staging directory for kms%0A  > d4e654a clients: clarify a misleading comment%0A  > 8b851d9 Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 362a89c Merge pull request # 112615 from mengjiao-liu/update_CRD_link%0A  > add0c80 Update to latest k8s.io/utils to pick up changes%0A  > 374216b Merge pull request # 112613 from dims/update-github.com/go-openapi/jsonreference-to-drop-github.com/PuerkitoBio/purell%0A  > a7ee7f9 Update `PreserveUnknownFields` field document link%0A  > 488bf20 update github.com/go-openapi/jsonreference to drop github.com/PuerkitoBio/purell%0A  > 47c15ca Merge pull request # 112588 from pacoxu/fsnotify-v1.5.4%0A  > d5b6243 Merge pull request # 112584 from dims/brneto-master%0A  > 8c6aa82 update fsnotify/fsnotify to v1.5.4%0A  > f8e18e9 run pin-dependency.sh and then hack/update-vendor.sh%0A  > c540c8c Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 70b0d96 Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 39cab0b updated etcd to v3.5.5 and newer otel libraries as well%0A  > 5faccda Merge pull request # 111866 from pacoxu/validate%0A  > 1c3fe9d e2e: bump ginkgo to v2.2.0%0A  > 917d446 Merge pull request # 112458 from dims/switch-to-release-tag-for-antlr-v1.4.10%0A  > 8b3fe74 add test case for array checking with dup values%0A  > 045fc90 Merge pull request # 112433 from ncdc/reduce-SchemaHas-allocs%0A  > 73cc883 Switch to release tag for antlr : v1.4.10%0A  > 22bcc66 added ratcheting validation for embedded resource and x-kubernetes-list-type validation%0A  > 269d73d Reduce allocations in HasSchemas%0A  > 7342cc6 Merge pull request # 112200 from pohly/client-go-shared-informer-factory-shutdown%0A  > aabbdff Merge pull request # 112349 from pohly/klog-update%0A  > fdf28bc client-go: support waiting for SharedInformerFactory shutdown%0A  > 6b7d12b build: update to klog v2.80.1%0A  > 559b4fa Merge pull request # 111768 from weilaaa/feature_add_symmetric_difference_in_sets_string%0A  > bf7d058 add symmetric difference in sets%0A  > 04ff81e Merge pull request # 112199 from pohly/klog-update%0A  > 87a4c3f dependencies: update to klog v2.80.0%0A  > 8f15690 Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > f637e1c dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > b6adc1c Merge pull request # 111964 from DangerOnTheRanger/cel-estimate-fix-update%0A  > ea2d438 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 6b4dc0b Add unit tests.%0A  > 767e67b Bump prometheus/client_golang to v1.13.0%0A  > 782b982 Run pin-dependency.sh and update-vendor.sh.%0A  > 305963e Merge pull request # 111909 from tosi3k/bump-prom-client%0A  > fa2959a Merge pull request # 111830 from t1anz0ng/typo%0A  > 5a6ffec Bump prometheus/client_golang to v1.12.2%0A  > e0abc3b fix(typo): remove extra " from autoscaling doc string%0A  > 2184a8d Merge pull request # 111696 from liggitt/go119mod%0A  > f750907 Update go.mod to go1.19%0Abumping github.com/fsnotify/fsnotify 0f4b979...5f8c606:%0A  > 5f8c606 Update ChangeLog%0A  > 8878587 Tweak the docs a bit%0A  > 89b4cf1 Add test for re-adding a renamed file (# 508)%0A  > 85acde2 Update x/sys%0A  > 69c24b0 Update x/sys%0A  > fb07f82 Add test to see what happens if you watch a symlink (# 498)%0A  > 666da9c Clarify doc comment on WatchList() (# 499)%0A  > 123e4e3 Add note about README version%0A  > 61a05ce Update documentation and examples (# 496)%0A  > e180a87 Move some inotify-tests to run on all backends; test that state is cleaned up after Remove (# 494)%0A  > fdf41a3 Move some files around%0A  > 844d71f Port minor test changes from fen-v2 branch; make LICENSE text not ugly%0A  > 5b87f50 windows: simplify a bit (# 493)%0A  > 2bfaa00 all: add Watcher.{sendEvent,sendError} (# 492)%0A  > 8ab3b84 kqueue: don't set up watchers on unreadable files (# 479)%0A  > a4bcdf8 Update changelog%0A  > 4b43fad kqueue: remove timeout from unix.Kevent() (# 480)%0A  > a24f78c windows: test symlinks (# 491)%0A  > f45391f windows: run TestWatchRename/rename_overwriting_existing_file (# 490)%0A  > ee33a65 Use "os.Rename()" in tests instead of "mv"%0A  > 9dd0568 cmd/fsnotify: fix time.Format() string%0A  > 5dcbfba windows: replace syscall with golang.org/x/sys/windows%0A  > 1f8edaf windows: replace "e" with "err" for error variables%0A  > 99715ba windows: increase buffer size from 4K to 64K (# 485)%0A  > a5c5815 ci: update to use Go 1.19, kick off fewer builds, update x/sys (# 484)%0A  > f2d35c3 Remove CLA section in contributing%0A  > 4604469 Need Linux 5.9 for a useful fanotify we can use%0A  > a566bb1 Update CONTRIBUTING.md%0A  > 01dfc6f Remove PULL_REQUEST_TEMPLATE%0A  > a58e868 Run tests in illumos (# 481)%0A  > 666c6a0 Update ChangeLog%0A  > 928895c [bugfix] close handle when remWatch open in getIno (# 288)%0A  > f174f95 windows: update watch paths when renaming directories with sub-watches (# 370)%0A  > 87dc1fa Rewrite tests (# 478)%0A  > 57e6a49 Add {Event,Op}.Has() (# 477)%0A  > 39823aa Document that /proc and /sys won't work%0A  > 60fbf57 Clarify FAQ on goroutines%0A  > ca0e2f4 macos: retry if open() returns EINTR (# 475)%0A  > ff39bb4 Fix lint (# 476)%0A  > 421f529 debian 6 test: deal with multiple packages (# 474)%0A  > a3256ef Remove AUTHORS file%0A  > 0e78fa6 Update README: split out FAQ to "Platform-specific notes"%0A  > 1a7b6ef inotify: don't ignore events for files that don't exist (# 470)%0A  > f0aceb2 Tweak comment regarding relative paths (# 466)%0A  > d9c9fa5 Add cmd/fsnotify (# 463)%0A  > cc15908 kqueue: better error if watching a file fails (# 471)%0A  > c4e64e4 Replace Use of Kthread-blocking Epoll with Poller Read, Remove Per-Event LStats on Linux # 433 (# 434)%0A  > 4b8b298 Test some more things in CI (# 469)%0A  > 548b8fb Add missing changelog for 1.4.{8,9} (# 468)%0A  > 7fe2936 inotify: fix race in Close() (# 465)%0A  > 35b6378 Clarify README on network drives (# 467)%0A  > e56409e Update link to CONTRIBUTING in the README (# 464)%0A  > 4678dfd Update documentation for linux systems (max_user_watches) (# 287)%0A  > 808f582 bump up GitHub Actions (# 461)%0A  > 4193dfd Do not suppress Chmod on non-existent file (# 260)%0A  > 6ae56b7 kqueue: Make watcher.Close() O(n) instead of O(n^2) (# 233)%0A  > adf5320 strings.Builder instead of bytes.Buffer (# 285)%0A  > 217e78e Explicit mutext (un)locking (# 462)%0A  > 1a4f949 Use common error when removing an unwatched file (# 460)%0A  > 5acfdc1 windows: protect access to isClosed with mutex (# 454)%0A  > c56cafd Test Go 1.18%0A  > 37badf6 This project is archived (# 459)%0Abumping golang.org/x/sys 90c8f94...c7a1bf9:%0A  > c7a1bf9 unix: define PerfBitWriteBackward%0A  > 1470852 unix: add SetsockoptTCPMD5Sig on linux%0A  > a6bfb89 unix: use unsafe.Slice in anyToSockaddr%0A  > c10701f windows: use unsafe.Slice in (*RawSockaddrAny).Sockaddr on windows%0A  > 6f25076 unix: define extended TCPInfo on Linux%0A  > 10499f4 unix: add ioctlPtr with unsafe.Pointer arg on other unices (cont)%0A  > 92c4c39 unix: add Dup3 on FreeBSD%0A  > 748af6e unix: pass PROT_MPROTECT(PROT_READ|PROT_WRITE) to initial Mmap on netbsd%0A  > 972870e unix/linux: update to Linux kernel 6.2, glibc 2.37 and Go 1.20.1%0A  > cc0b67d unix: use C.ioctl in generated ioctlPtr%0A  > a3b23cc unix: use SYS_PTRACE in generated ptracePtr%0A  > 71a906e unix/linux: add TUN flags and virtio_net_hdr constants%0A  > 2977c77 unix: add ptracePtr that accepts pointer arg as unsafe.Pointer%0A  > 6877dcc execabs: don't override Go 1.19 error with our error%0A  > b13f40e unix: add ioctlPtr with unsafe.Pointer arg on other unices%0A  > 3b9b58b unix: Faccess: check CAP_DAC_OVERRIDE on Linux%0A  > 2da1413 cpu: get hwcap/auxv from the Go 1.21+ runtime%0A  > 4fee21c windows: Add WSALookupService syscall wrappers%0A  > c79a742 unix: fix a use-after-free bug in PtraceIO on freebsd%0Abumping knative.dev/networking e5d04e8...b9dd5c2:%0A  > b9dd5c2 upgrade to latest dependencies (# 816)%0A  > 68947c5 upgrade to latest dependencies (# 815)%0A  > 14a2bd4 Move `pkg/certificates` from `control-protocol` to `networking` (# 802)%0A  > 2daa483 Update community files (# 813)%0A  > 0dbe4f9 upgrade to latest dependencies (# 812)%0A  > 2a2f7d2 upgrade to latest dependencies (# 810)%0A  > fcbedad Update community files (# 809)%0A  > a44b093 upgrade to latest dependencies (# 808)%0A  > 7c2f7ac upgrade to latest dependencies (# 807)%0A  > 33636d9 Backward compatibility for InternalEncryption (# 806)%0A  > 77975a1 Add the new certificate names for dataplane and controlplane (# 804)%0A  > c3cca43 upgrade to latest dependencies (# 803)%0A  > 3f4627e Add internal trust flag to config (# 778)%0A  > 02055c8 Update community files (# 801)%0A  > 68725bd upgrade to latest dependencies (# 798)%0A  > 1594abb Update community files (# 797)%0Abumping k8s.io/apimachinery 4fbe8e4...b207ce5:%0A  > b207ce5 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > 917de35 Bump runc go module v1.1.4 -> v1.1.6%0A  > 53ecdf0 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 05339fa Update golang.org/x/net to v0.7.0%0A  > eabbfd5 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 48b8d1f Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 373a5f7 Merge pull request # 114521 from 3point2/automated-cherry-pick-of-# 113283-upstream-release-1.26%0A  > b5e5df6 Fix SPDY proxy authentication with special chars%0A  > 553a2d6 Improve error message when proxy connection fails%0A  > 5d4cdd2 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > 6cbc4a3 Update golang.org/x/net 1e63c2f%0A  > 6561235 Merge pull request # 113699 from liggitt/manjusaka/fix-107415%0A  > dad8cd8 Update workload selector validation%0A  > fe82462 Add extra value validation for matchExpression field in LabelSelector%0A  > 067949d update k8s.io/utils to fix util tracing panic%0A  > 0ceff90 Merge pull request # 112223 from astraw99/fix-ownerRef-validate%0A  > 9e85d3a Merge pull request # 112649 from howardjohn/set/optimize-everything-nothing%0A  > b0dd9ec Fix ownerRef controller validate err%0A  > b03a432 Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > 88a1448 Rename and comment on why sharing is safe%0A  > 4e6bcdb dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > 3adc870 Optimize `Everything` and `Nothing` label selectors%0A  > 0524d6c Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > 5a0277f Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > 6809593 Merge pull request # 112377 from weilaaa/refactor_sets_use_generic%0A  > 70a38aa Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > f2d9aed refactor sets use generic%0A  > d097f82 dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > 7b5633b Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > b839e82 Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > b7d8973 update kube-openapi%0A  > 1dc6ace update fsnotify to v1.6.0%0A  > 78d003c Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 04898ff Bump golang.org/x/text to v0.3.8%0A  > 79993b2 Merge pull request # 112875 from pohly/update-yaml%0A  > 7379c15 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 66e26ac Merge pull request # 112707 from enj/enj/i/https_links%0A  > 882b67d Use https links for k8s KEPs, issues, PRs, etc%0A  > 7fb78ee Merge pull request # 112472 from ialidzhikov/nit/error-msg%0A  > 826a74e Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 22fe889 Improve the error returned from the `LabelSelectorAsSelector` func%0A  > e2f9797 Update to latest k8s.io/utils to pick up changes%0A  > f8159af Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 612703e Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 9901884 updated etcd to v3.5.5 and newer otel libraries as well%0A  > 6439059 Merge pull request # 112526 from liggitt/redirect%0A  > 0564b5e e2e: bump ginkgo to v2.2.0%0A  > 2e3bf73 Limit redirect proxy handling to redirected responses%0A  > 6d854d7 Merge pull request # 112349 from pohly/klog-update%0A  > e1e1b7c build: update to klog v2.80.1%0A  > ed93eed Merge pull request # 111768 from weilaaa/feature_add_symmetric_difference_in_sets_string%0A  > 36163c5 Merge pull request # 112193 from jindijamie/master%0A  > b7b9ba4 add symmetric difference in sets%0A  > 31bc292 Merge pull request # 112199 from pohly/klog-update%0A  > 1c318b6 Add an option for aggregator%0A  > 0d0d03e Merge pull request # 111936 from haoruan/bugfix-111928-microtime-marshal-precision%0A  > 145c075 dependencies: update to klog v2.80.0%0A  > 2d64dac Merge pull request # 112089 from zeze1004/fix-typo%0A  > 2187a78 Marshal MicroTime to json and proto at the same precision%0A  > 53c4d51 Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > 30e9977 Fix typo "sturct" to "struct"%0A  > 5e4f25a dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > 349dcdf Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 16a7f7a Bump prometheus/client_golang to v1.13.0%0A  > 2b9fe2c Merge pull request # 111808 from alvaroaleman/meta-wrapping%0A  > bb48261 Apimachinery meta errors: Support errors.Is and error wrapping%0Abumping golang.org/x/term d974fe8...0edf009:%0A  > 0edf009 go.mod: update golang.org/x dependencies%0Abumping knative.dev/pkg dfad48e...6eb4b40:%0A  > 6eb4b40 Update community files (# 2760)%0A  > eb63a40 Support to set qps and burst via env variable (# 2755)%0A  > 74c4be5 Generate kresource duck type codegen (# 2754)%0A  > 4dbc312 fix boilerplate (# 2753)%0A  > 15605c7 Defaulting Controller options for all kind of webhooks (# 2738)%0A  > 94b81fc Update community files (# 2752)%0A  > 5671699 drop the dynamic type (# 2750)%0A  > 9bda38b Fix some webhook testing tech debt (# 2751)%0A  > ec20442 Update community files (# 2747)%0A  > 05bfcf6 bump k8s dependencies and update min version to v1.25 (# 2745)%0A  > 52ff2ac drop dynamic client wrappers (# 2744)%0A  > a170a07 Eventing TLS: validate that Destination.CACerts is a PEM encoded cert (# 2743)%0A  > dfb4bf0 Drop dynamic wrapper injection code generation (# 2742)%0A  > db8a353 Add SinkCACerts to SourceStatus (# 2733)%0A  > 9049667 Update community files (# 2735)%0A  > aacec7f Update community files (# 2734)%0A  > 300df43 Eventing TLS: Added AddressableFromDestination method on the resolver (# 2717)%0Abumping golang.org/x/text 71a9c9a...9db913a:%0A  > 9db913a go.mod: update to newer x/tools%0A  > 30dadde all: correct comment typos%0Abumping golang.org/x/tools b3b5c13...d0863f0:%0A  > d0863f0 go.mod: update golang.org/x dependencies%0A  > 545ca87 gopls/internal/regtest/marker: require go/packages%0A  > 1ace7db go,gopls: remove license from package doc comments%0A  > ebad375 gopls/internal/lsp/protocol: prevent license rendering in godoc%0A  > 10a39ef gopls/internal/lsp/regtest: address additional comments on marker.go%0A  > 69920f2 gopls/internal/regtest/marker: add missing tests for hover%0A  > 24a13c6 gopls/internal/regtest: fill out features of the new marker tests%0A  > 2b149ce gopls/internal/regtest: add a regtest-based version of the marker tests%0A  > edddc5f go/packages: don't discard errors loading export data%0A  > a762c82 go/ssa: add MultiConvert instruction%0A  > f124b50 cmd/stringer: streamline test subprocesses%0A  > 6b6857a gopls: fix typos in comments and doc%0A  > 8111118 go/analysis/internal/facts: fix cycle in importMap.%0A  > dd1c468 gopls/internal/lsp/source: simplify extracting object hover doc%0A  > 66f8f71 gopls/internal/lsp/source: use syntax alone in FormatVarType%0A  > 30f191f internal/imports: update stdlib index for Go 1.20%0A  > 4e98188 internal/imports: use go/packages instead of cmd/api to compute symbols%0A  > 4e8ff89 internal/imports: update stdlib index for 1.20%0A  > 6bd0d00 gopls/internal/lsp: go to definition from linkname directive%0A  > 0cfddb3 gopls/internal/lsp: enable clear builtin completion test%0A  > 41adf8d gopls/internal/lsp/tests: remove StripSubscripts%0A  > 86fdadc gopls/internal/lsp/safetoken: delete safetoken.Range%0A  > c276ee5 internal/robustio: fix signature of getFileID on plan9%0A  > e170d45 gopls/internal/lsp: add clear builtin%0A  > 2ea4b81 go/ast/inspector: skip ranges that do not contain a node type%0A  > 407bbed go/analysis: improve error message on duplicate fixes%0A  > bd5dfbb all: fix some comments%0A  > 072fca5 gopls/protocol: use the current definition of the lsp%0A  > aa633e7 tools/gopls: provide markdown for completion and signature help%0A  > 684a1c0 go/analysis/internal/analysisflags: use os.Executable for program path%0A  > bd5e595 gopls/internal/lsp/cache: add missing mutex%0A  > 2683128 gopls/internal/lsp: differentiate govulncheck/vulncheck imports diags%0A  > d1e92d6 gopls/internal/lsp/mod: reorder vulncheck quick fixes%0A  > 87d00e6 gopls/internal/lsp: separate some requests from source.Identifier%0A  > ae242ec gopls: fix windows file corruption%0A  > 6f65213 gopls/internal/lsp/protocol: Mapper.NodeMappedRange%0A  > e260368 gopls/semantic: report type parameters in the type of a receiver%0A  > b62cbb6 internal/lockedfile: fix build constraints on solaris%0A  > 1aa7e72 gopls/internal/lsp/source: avoid qualifiedObjectsAtProtocolPos%0A  > 5ed33df gopls/internal/lsp/source: rename: prep for incrementality%0A  > e0659d1 gopls/internal/lsp/source: simplify legacy 'references' func%0A  > 1edcfe7 gopls/internal/regtest/diagnostics: require cgo for TestGoListErrors%0A  > f052158 gopls/internal/lsp/protocol: move TestBytesOffset%0A  > d093a13 gopls/internal/lsp/protocol: LocationTextDocumentPositionParams%0A  > bcb677e gopls/internal/regtest: make RegexpSearch return a Location%0A  > 60782e9 gopls/internal/lsp/source: eliminate a couple uses of posToMappedRange%0A  > 031e6e6 gopls/internal/lsp/source: eliminate ResolveImportPath%0A  > f2cd9ef gopls/internal/lsp/source: reduce usage of TypecheckWorkspace%0A  > f10e7d5 gopls/internal/lsp/cache: remove package dependence on packages.Config%0A  > 8270757 gopls/internal/lsp/source: switch call hierarchy to references v2%0A  > 37c69d8 gopls/internal/lsp/source: references: support exported methods%0A  > f3c36a2 gopls/internal/lsp/cmd/test: delete marker-based tests of gopls cmd%0A  > c224aae gopls/internal/lsp/cmd/test: new integration test for gopls command%0A  > deeb64b gopls/internal/lsp/source/xrefs: allow Lookup of a set%0A  > f269f53 gopls/internal/lsp: remove Server.processModifications%0A  > fcd57eb gopls: allow 'any' and 'comparable' in completion results%0A  > aae3642 gopls/internal/lsp/source: referencesV2: support unexported methods%0A  > b5d65e0 tools/gopls: register semantic tokens statically%0A  > 51abc5b gopls/internal/lsp/source: stub: don't panic when encountering 'error'%0A  > ce28f40 gopls/internal/regtest: add a test demonstrating confusion following an%0A  > c4c6aa6 internal/lsp/cache: don't panic in Snapshot on a shutdown view%0A  > 1faecd3 tools/internal/diff: fix off-by-one error in computing diffs%0A  > a7f033a gopls/internal/lsp: consolidate the FileHandle API%0A  > 271e621 internal/lockedfile/internal/filelock: fix aix build tag%0A  > ff9bea5 gopls/internal/lsp/cmd/test: signpost future cleanups%0A  > 7d4ba2f gopls/release: remove unused functionality from release script%0A  > 46b6958 gopls/internal/lsp/source: delete source_test%0A  > bcc7794 go/analysis/passes/directive: add directive analyzer%0A  > 33d416e gopls/internal/lsp: add missing comments on 3x tests.Test impls%0A  > afea272 gopls/internal/lsp/source: make implementations2 work on embedded fields%0A  > bb7c440 gopls/internal/lsp/filecache: use file locking, not rename%0A  > 561a9be gopls/internal/lsp/filecache: actually delete files%0A  > 9682b0d gopls/internal/lsp/source: delete IsInterface%0A  > 7a7b699 go/analysis/passes/loopclosure: avoid panic in new parallel subtest check when t.Run has single argument%0A  > 3e6f71b gopls/internal/regtest: use AfterChange in more places%0A  > 9ff31a5 x/tools/go/analysis/passes/printf: revert URL in error message%0A  > 2fa6ca1 gopls/internal/lsp/source/impls: a new "implementations" index%0A  > 957bec5 gopls/protocol: new versions of generated LSP files%0A  > f0e2d5c internal/gcimporter: discard position info for unneeded lines%0A  > 5bedd86 cmd/digraph: use ReadString rather than bufio.Scanner%0A  > f6ea009 gopls/internal/lsp: remove the experimentalWatchedFileDelay setting%0A  > f46e418 gopls/internal/lsp/source: include ITVs in global references%0A  > f3e53e5 internal/jsonrpc2_v2: fix typos%0A  > d958e85 internal/gcimporter: use two-level file index%0A  > 8aba49b internal/gcimporter: preserve column and line in shallow iexport%0A  > d7fc4e7 gopls: new LSP stub generator%0A  > 5c176b1 internal/robustio: skip os.Link test on android%0A  > d34a055 go/ssa: sanity check the types of phi nodes%0A  > 6f095b4 go/callgraph/vta: add flows for receiver function types%0A  > 8e94967 cmd/fiximports: do not assume go list -json unmarshals into build.Package%0A  > e035d0c go/ssa: fix phi node type in slice to array conversion%0A  > 03eac81 go/expect: remove testdata go.mod to go.fake.mod%0A  > 1e819a3 gopls/internal/regtest: follow-ups to review comments from earlier CLs%0A  > 9ba8bb1 gopls/internal/regtest: clean up workspace symbol helpers%0A  > 91b6070 gopls/internal/regtest: eliminate DiagnosticAtRegexp%0A  > bd48b9a gopls/internal/regtest: eliminate DiagnosticsAtRegexpWithMessage%0A  > 5d65394 gopls/internal/regtest: eliminate DiagnosticAt%0A  > 27dfeb2 gopls/internal/regtest: replace NoDiagnostics with NoMatchingDiagnostics%0A  > 87092c8 gopls/internal/lsp/fake: use protocol types for the fake editor%0A  > 672a036 gopls/internal/regtest: simplify OnceMet expressions with an env helper%0A  > ab7b5b2 gopls/internal/regtest: eliminate GoSumDiagnostic%0A  > 331a1c6 gopls/internal/regtest: add a simpler API for diagnostic expectations%0A  > c9b82f2 gopls/internal/regtest: eliminate EmptyDiagnostics%0A  > e81af27 gopls: update golang.org/x/vuln@6ad3e3d%0A  > d19e3d1 internal/regtest/bench: fix BenchmarkRename and add more benchmark tests for gopls%0A  > 2be1a9a gopls/internal/regtest: rename EmptyOrNoDiagnostics to NoDiagnostics%0A  > 7ec05ac gopls/internal/regtest: eliminate NoDiagnostics%0A  > e956495 gopls/internal/regtest: eliminate DiagnosticsFor%0A  > 8087911 gopls: remove the experimentalWorkspaceModule mode%0A  > 5b300bd gopls/internal/lsp/cache: clean up view workspace information%0A  > 97d5de5 gopls/internal/cache: don't mark initialized after cancellation%0A  > 58691bc gopls/internal/lsp/glob: add an LSP compliant glob implementation%0A  > a3c22fc cmd/cover: delete package%0A  > 98dcb0e cmd/cover: remove replace directive%0A  > 7765567 gopls/internal/lsp/source: minor clarifications%0A  > a7f7db3 cmd/cover: carve out deprecated command into its own module%0A  > f9a10c0 Revert "cmd/cover: carve out deprecated command into its own module"%0A  > e345d46 internal/gcimporter: fix export of invalid methods%0A  > 4305a22 gopls/internal/lsp/cache: don't cache files if mtime is too recent%0A  > 227ee72 internal/regtest/misc: fail eagerly in TestRenameFileFromEditor%0A  > 43158af cmd/cover: carve out deprecated command into its own module%0A  > b798934 gopls/internal/lsp/protocol: cleanups and docs for Mapper%0A  > a24944e gopls/internal/lsp/protocol: rename s/ColumnMapper/Mapper/%0A  > 55935f4 gopls/internal/span: simplify Span%0A  > 40a1c97 gopls/internal/lsp/lsppos: delete Mapper%0A  > 6a3bc37 gopls/internal/lsp/protocol: reimplement ColumnMapper line logic%0A  > 6e9a35d go/callgraph/cha: refactor callee construction%0A  > fef5b76 go/callgraph: fix slicing in callgraph_test.go%0A  > 2be9d05 gopls/internal/lsp/source/xrefs: a new reference index%0A  > 0362cea gopls/internal/lsp/lsppos: delete TokenMapper%0A  > 67baca6 go/callgraph/vta: optimize scc computation%0A  > 2eb6138 gopls/internal/lsp/filecache: use TempDir if UserCacheDir fails us%0A  > 36bd3db gopls/internal/lsp/protocol: move MappedRange%0A  > 16b3bf8 gopls/internal/lsp/cache: assume Go 1.16+%0A  > 3856a5d internal/robustio: add Plan9 support to FileID%0A  > 09cbc42 gopls/internal/lsp/fake: fix EOF bug in applyEdits%0A  > 4ded35d gopls/internal/lsp/cache: use distinct types for mod and work parse keys%0A  > 107f43f gopls/completion: avoid duplicating text in test func completions%0A  > e225fd4 gopls/internal/lsp/mod: fix nil panic in go.mod hover%0A  > 057ed3c gopls/internal/lsp/filecache: use os.Chtimes%0A  > 1fe76af gopls/internal/lsp/source: MappedRange cleanup%0A  > 02bea03 gopls/internal/lsp/protocol: simplify ColumnMapper%0A  > a4455fe go/callgraph: adds benchmarks comparing algorithms%0A  > 7db99dd go.mod: update golang.org/x dependencies%0A  > 1e0dff2 gopls/internal/regtest: avoid race in TestSwitchFromGOPATHToModuleMode%0A  > 0441b43 gopls/internal/lsp/cache: use specific mutexes for module data%0A  > 33071fb internal/robustio: move robustio%0A  > b01e7a4 gopls/internal/regtest/watch: don't run TestSwitchFromGOPATHToModuleMode%0A  > e417ea3 gopls: remove dead analysis code%0A  > 1a08d01 gopls/internal/lsp: update replace directives in go.mod for package renaming%0A  > eac36cb gopls/internal/regtest: port experimental workspace tests to go.work%0A  > 224a61b gopls/internal/lsp/source: delete Snapshot.WriteEnv method%0A  > 81e741e gopls/internal/lsp/safetoken: funnel more calls through this package%0A  > 8367fb2 gopls/internal/regtest: await go.work changes in TestAddAndRemoveGoWork%0A  > 3b16059 gopls/internal/regtest: make BufferText strict%0A  > 0e1d013 gopls/internal/lsp/cache: recreate Views when their root changes%0A  > 2f31dd4 go/ssa,go/analysis/passes/nilness: refine when type param constants are nil%0A  > ae4ff82 gopls/internal/lsp/source: delete GetTypedFile%0A  > fe6b300 gopls/internal/lsp/source: eliminate Snapshot.Package{,s}ForFile%0A  > 26fc609 gopls/internal/lsp/cache: eliminate snapshot.containingPackages%0A  > 85e6ad7 gopls/internal/lsp/safetoken: fix bug in Offset at EOF%0A  > ef1ec5d gopls/internal/lsp/safetoken: fix error message%0A  > 44395ff gopls/internal/lsp/source: avoid unnecessary transitive rdeps%0A  > 6546d82 Revert "gopls/internal/regtest: harmless CL used for benchmark test"%0A  > 3be0647 gopls/symbols: call source.Document symbols only for Go files%0A  > d462c83 gopls/internal/lsp: Replace input text when completing a definition%0A  > 7efffe1 gopls/internal/regtest: harmless CL used for benchmark test%0A  > 1627e95 gopls/internal/lsp: more comment tweaks post-//line support%0A  > 21f6100 internal/lsp/debug: fix broken template%0A  > 6ad27d0 gopls/internal/robustio: FileID, a portable file identifier%0A  > 6df6eee internal/diff/lcs: optimize inner loop%0A  > 57b1265 go/gcexportdata: drop support for go1.6 export data%0A  > 099260e gopls/internal/lsp: followups to dropping line directives%0A  > 61e2d3f gopls/internal/lsp/cache: a new analysis driver%0A  > eb70795 gopls: ignore //line directives%0A  > b4dfc36 go/ssa: deref core type in emitLoad%0A  > 1270fd7 gopls/internal/lsp: announce selectionRangeProvider capability%0A  > 9bc5dce gopls/internal/lsp/cache: simplify DiagnosePackage%0A  > df35cd8 x/tools: drop support for Go toolchains older than go1.16%0A  > db9d10f go/gcexportdata: preallocate buffer to read into when size is known%0A  > 0d2045b gopls/internal/lsp: document analysis-related functions%0A  > b2b9dc3 gopls/internal/lsp/cache: reduce type-checking in renameImports%0A  > 3cb82d5 go/ssa/interp: fix conversion of slice to named array%0A  > 5899b6a gopls: upgrade dependencies following release%0A  > 763a030 gopls/internal/lsp/cache: delete Snapshot.KnownPackages%0A  > cc0e696 gopls/internal/hooks: panic if diff consistency check fails%0A  > 9ec8553 gopls/internal/lsp/source: emit interface stub methods at top level%0A  > 444c8f6 gopls/internal/lsp/cache: only invalidate parsed files if they changed%0A  > 601ca6c gopls/internal/lsp/source: use correct token.File%0A  > 95c9dce internal/lsp/mod: fix run_govulncheck codelens name%0A  > d72a64a gopls/internal/lsp: add selection range request%0A  > 18f76ec gopls/internal/lsp: split ActivePackages%0A  > 84299a0 gopls/internal/lsp/cache: simplify ad-hoc package warning logic%0A  > a3eef25 gopls/internal/lsp/cache: record parse keys when they're created%0A  > 3da7f1e gopls/hover: remove header tags from hover markdown%0A  > a310bcb gopls/internal/lsp/source: eliminate getStubFile%0A  > 3cba5a8 internal/gcimporter: port CL 424876 from std importer%0A  > b0fdb78 gopls/internal/lsp/mod: add Reset vulncheck result codelens%0A  > 88ceb24 gopls/internal/lsp: perform analysis unconditionally%0A  > 3f74d91 gopls/internal/lsp/cache: invalidate govulncheck results older than 1hr%0A  > 6b8674f gopls/internal/lsp/source: avoid typechecking in findRune%0A  > d7dfffd gopls/internal/lsp: eliminate more unnecessary typechecking%0A  > f3fb218 gopls/internal/lsp/fake: use robustio.RemoveAll in (*Workdir).RemoveFile%0A  > 96ff41d gopls/internal/vulncheck: add TODO for the vulncheck diagnostics%0A  > 0f6c6f1 gopls: delete obsolete govulncheck code and stop gopls vulncheck -summary%0A  > c5343a6 gopls/internal/lsp/regtest: fix TestRunGovulncheckError2%0A  > cb701f7 gopls/internal/lsp: avoid type-checking when computing hyperlinks%0A  > d0f184d gopls/internal/lsp/source: avoid unnecessary calls to GetTypedFile%0A  > 1e5efed gopls/internal/lsp/fake: simply use polling to simulate file watching%0A  > 838a165 gopls/internal/lsp/fake: eliminate the unnecessary fake.FileEvent%0A  > 09fb680 gopls/internal/lsp/fake: eliminate the unnecessary ChangeFilesOnDisk API%0A  > 09ae2d5 gopls/internal/lsp/source: KnownPackagePaths: avoid loading%0A  > 1dcc423 gopls/internal/lsp/cache: split metadata and loading in PackagesForFile%0A  > 6b50501 gopls/release: fix the release script when go.work is not used%0A  > aee3994 gopls/internal/lsp/fake: in (*Workdir).RenameFile, fall back to read + write%0A  > fe60148 go.mod: update golang.org/x dependencies%0A  > c9ea9a7 gopls/internal/regtest: add a test for the case when the renaming package's path contains "internal" as a segment%0A  > bf5db81 gopls/internal/lsp/cache: improve ad-hoc warning for nested modules%0A  > aa9f4b2 go/analysis: document that facts are gob encoded in one gulp%0A  > bdcd082 internal/gcimporter: skip tests earlier when 'go build' is not available%0A  > 2ad6325 gopls/internal/lsp/cache: expand ImportPath!=PackagePath comment%0A  > 52c7b88 gopls/internal/robustio: only define ERROR_SHARING_VIOLATION on Windows%0A  > 4f69bf3 gopls/internal/lsp/cache: narrow reloadOrphanedFiles to open files%0A  > 6002d6e gopls/internal/regtest/misc: test Implementations + vendor%0A  > f540ee6 internal/gcimporter: load cached export data for packages individually%0A  > d444fa3 gopls/internal/lsp/cache: simplify canonical URI cache%0A  > 25fdb81 gopls/internal/regtest/misc: skip vendor test on go1.13%0A  > e0b516b gopls/internal/lsp/cache: invalidate metadata after vendor change%0A  > 31d5843 gopls/internal/lsp/cache: fix re-entrant session locking%0A  > 8c78b30 gopls/internal/vulncheck: always use pkg.go.dev/vuln for urls%0A  > 47a8246 gopls/internal/regtest/misc: skip TestRunGovulncheckError2%0A  > d54e12b gopls/internal/lsp: avoid I/O in URI comparison operations%0A  > 0379b73 internal/gcimporter: fix TestImportStdLib%0A  > e79e423 gopls/internal/vulncheck: handle package errors%0A  > c5ce806 gopls/internal/lsp/mod: disable the diagnostics on stdlib vulns%0A  > 78c1861 gopls/internal/vulncheck: clarify the log message%0A  > 1a0053c gopls: move reset go.mod diagnostic codelens to module statement%0A  > 9b8d87b gopls/internal/regtest: fix TestRunGovulncheckStd%0A  > 81b6bef gopls/internal/lsp: add run vulncheck fix for stdlib vulns%0A  > fe83ddb gopls/internal/lsp: move options off of the cache%0A  > 88ee30b gopls/internal/lsp/source: enable run_govulncheck codelens in exp mode%0A  > 0a6aa90 gopls/internal/lsp/command: rename run_vulncheck_exp to run_govulncheck%0A  > bedad5a gopls/internal/lsp/mod: add hover for stdlib vulnerabilities%0A  > 7a1b570 gopls/internal/vulncheck: check vulnerabilities in standard library%0A  > 9a54670 gopls/internal/lsp/mod: add "Run govulncheck" codeaction%0A  > f1b76ae gopls/internal/lsp: add an option to overwrite previous diagnostics%0A  > e8a70a5 gopls/internal/lsp: remove access to mutable session state from the view%0A  > ff22fab gopls/internal/lsp/cache: eliminate obsolete invalidation step%0A  > 3881046 gopls: add a go:generate rule for doc generation%0A  > 4c3cb1e internal/gocommand: add GoVersionString%0A  > e29d1ed gopls: add diagnostic for standard library%0A  > f718365 gopls/internal/lsp: include all vulns info to fetch_vulncheck_result%0A  > 9519368 gopls/internal/lsp/mod: add the vulncheck diagnostics mode%0A  > 7d9f451 gopls/internal/govulncheck: add in-memory cache for vulndb%0A  > 1ccccf8 go/ssa: deprecate coreType and _NormalTerms%0A  > 4b7d1b3 gopls: add diagnostics for both vulns used and not used%0A  > 50ccef5 internal/regtest/bench: add benchmark tests for gopls%0A  > d39685a gopls/internal/lsp/source: Package clarifications%0A  > 7cfde84 gopls/internal/vulncheck: add import info based vuln scanning%0A  > 2b56641 internal/gcimporter: adjust the number of expected packages in TestStdlib%0A  > 50df761 gopls: skip vulnerabilities that are probably fixed in hover%0A  > 7cda55e gopls/internal/lsp/cache: wire in mod vulnerability analysis%0A  > 5c35617 gopls: add quick fixes for all vulnerabilities%0A  > fb7be64 gopls/internal/lsp/command: return the vulncheck progress token%0A  > 060c049 go/packages: fix doc typo%0A  > 6eafd96 gopls: fix formatting for vulncheck results in hover%0A  > b797704 go/analysis/passes/loopclosure: recursively check last statements in statements like if, switch, and for%0A  > 3b9d20c internal/gcimporter: in TestStdlib, only check x/tools packages if we expect to have their source%0A  > 2ad3c33 go/packages: change workaround for issue 28749 to not require NeedFiles%0A  > 57f56ab gopls/internal/lsp/source: avoid panic(nil)%0A  > 41c70c9 internal/lsp/source: avoid using go/types.Implements with Typ[Invalid]%0A  > db5eae2 analysis: correct go/analysis/passes/findcall path in docs%0A  > b978661 cmd/godoc: streamline test subprocesses%0A  > 932ec22 internal/testenv: add a Command function that replaces exec.Command%0A  > 19fb30d gopls/internal/lsp/cache: fix data race in Symbols%0A  > 4ce4f93 gopls/internal/lsp: add gopls.fetch_vulncheck_result%0A  > 8ba9a37 gopls/internal/lsp/mod: highlight when there is no fix for vuln%0A  > 128f61d gopls/internal/lsp/mod: add related info%0A  > fc03993 internal/lsp/mod: adjust vulncheck diagnostics suppression logic%0A  > c099dff gopls/internal/vulncheck: log progress%0A  > 36a5c6a go/ssa: build generic function bodies%0A  > 85bf7a8 gopls/internal/lsp/source: eliminate Metadata interface%0A  > 2592a85 gopls/internal/lsp: simplify KnownPackages%0A  > c7ed4b3 gopls/internal/lsp/cache: clean up tracking of GO111MODULE%0A  > 23056f6 internal/lsp/cache: clean up getOrLoadIDsForURI%0A  > 5a4eba5 internal/lsp/cache: remove support for invalid metadata%0A  > 32a17c0 gopls/internal/lsp/mod: fix unaffecting vuln diagnostics msgs%0A  > dea100b internal/testenv: skip tests that need export data for std if 'go tool compile' does not exist%0A  > ba373ee playground/socket: eliminate an arbitrary timeout in TestLimiter%0A  > 3d085f3 gopls/internal/lsp/lsprpc: eliminate arbitrary timeout in TestEnvForwarding%0A  > 434d569 gopls/internal/lsp/regtest: improve documentation%0A  > ce26db4 go/analysis: add Pass.TypeErrors field%0A  > b0ad6b2 gopls/internal/regtest/misc: fix use of the AfterChange API%0A  > 89856a4 gopls/semantic: semantic tokens for type parameters%0A  > 6e8da3f internal/pkgbits: port small optimization from compiler to tools%0A  > 06fb723 internal/gcimporter: port memory reuse optimizations from Go tree%0A  > fc702c5 internal/gcimporter: fix performance regression for unified IR%0A  > 1cb4c17 gopls/internal/regtest: make AfterChange do the awaiting%0A  > 0c71b56 gopls/internal/lsp: fix diagnostic suppression when folders change%0A  > e3b3c01 go/pointer: break TestInput into subtests and update skips%0A  > 13648cd gopls/internal/lsp/cache: use Package.FileSet where possible%0A  > 8f32411 cmd/stringer: replace ioutil with os%0A  > 3c3713e gopls/internal/lsp/cache: use typed strings (PackagePath et al) throughout%0A  > 004d118 gopls/internal/lsp/mod: simplify ModVulnerabilityDiagnostics%0A  > 4a8413c gopls/internal/lsp/mod: deleted unused function pkgVersion%0A  > bc08991 gopls: sync golang.org/x/vuln@3af8368ee4fe%0A  > d66e9b4 internal/typesinternal: update go/types error codes for 1.20%0A  > 6f99366 gopls/internal/lsp/cache: don't pass snapshot.fset to go/packages%0A  > d56532a cmd/compilebench: make it work without installed .a's%0A  > 502c634 go.mod: update golang.org/x dependencies%0A  > bd04e32 internal/jsonrpc2_v2: eliminate a potential Accept/Dial race in TestIdleTimeout%0A  > d41a43b internal/jsonrpc2_v2: fix a potential deadlock when (*Conn).Close is invoked during Bind%0A  > 3057465 gopls/doc: Add plugin for Lapce to gopls documentation%0A  > ba92ae1 internal/persistent: avoid incorrect map validation due to multiple keys%0A  > 9474ca3 gopls/doc: clarify `go work use`%0A  > 003fde1 internal/gcimporter: use nondeprecated go/packages mode bits%0A  > 5050657 gopls/fake: add semantic token modifiers to fake editor%0A  > 88a3548 gopls/coverage: repair coverage.go%0A  > 8e0240a internal/regtest/workspace: permanently skip TestDeleteModule_Interdependent%0A  > fe725d9 gopls/internal/regtest: simplify awaiting diagnostics from a change%0A  > 3c8152e internal/gcimporter: optimize dependency lookup%0A  > 39c2fd8 internal/lsp/cache: simplify importsState modfile hashing logic%0A  > ec044b1 gopls: update dependencies following the v0.10.0 release%0A  > 2b29c66 internal/gcimporter: API for shallow export data%0A  > affa603 internal/gcimporter: moved from go/internal/gcimporter%0A  > a77a1fb gopls/internal/lsp/mod: fix vulncheck hover message%0A  > 4ada35e gopls/internal/lsp: handle modVulncheckSource in diagnosticSource.String%0A  > e5f03c1 gopls/doc: clean up README and add a release policy%0A  > d5e9e35 go/analysis/passes/loopclosure: enable analysis of parallel subtests%0A  > 039b24b internal/jsonrpc2_v2: initiate shutdown when the Writer breaks%0A  > 32e1cb7 gopls/internal/lsp: clarify control around diagnostics%0A  > feeb0ba gopls/internal/lsp/cmd: fix deadlock when opening a file%0A  > 6e9dc86 gopls/internal/lsp/source/completion: fix panic in completion on *error%0A  > 73fcd88 Revert "internal/jsonrpc2_v2: initiate shutdown when the Writer breaks"%0A  > 70a130e gopls/api-diff: simplify the api-diff implementation%0A  > 3e8da47 internal/jsonrpc2_v2: initiate shutdown when the Writer breaks%0A  > 3566f69 gopls/internal/lsp/source: minor space optimizations%0A  > 7cdb0e7 internal/jsonrpc2_v2: rename Serve to NewServer and eliminate its error return%0A  > 28e9e50 internal/jsonrpc2_v2: eliminate error return from Bind%0A  > eabc3a0 internal/jsonrpc2_v2: eliminate isClosingErr%0A  > 4885f7c internal/jsonrpc2_v2: eliminate a temporary connection leak in (*Server).run%0A  > 739f55d internal/jsonrpc2_v2: rework Connection concurrency%0A  > e172e97 go/types/typeutil: break recursion through anonymous interfaces%0A  > f1c8f7f internal/lsp/source: optimize filter regular expression%0A  > e074ef8 gopls/internal: don't show a warning if the Go version is undetected%0A  > 7fba77c gopls/internal/lsp/source: remove deprecated settings from EnableAllExperiments%0A  > 42cb7be gopls/internal/lsp: improve the Go version deprecation message%0A  > 2af106e gopls/internal/hooks: fixes to diff disaster logic%0A  > e4bb343 go/internal/gcimporter: update to anticipate missing targets and .as%0A  > 875c31f go/internal/gcimporter: add test of export/import on std%0A  > 541f4c5 cmd/bundle: quote command-line arguments in output%0A  > de675d5 tools/gopls: argument in function bodies marked as parameter by semantic tokens%0A  > 3e1371f gopls/internal: start on LSP stub generator in Go.%0A  > 121f889 gopls/internal/lsp/mod: merge vuln diagnostics to one, and add a hover%0A  > d6511e5 internal/facts: share go/analysis/internal/facts with gopls%0A  > 2e0ca3a go/internal/gcimporter: fix bug in struct iexport%0A  > 1928cea go/ssa: emit field and index lvals on demand%0A  > 8166dca go/analysis/passes/asmdecl: define register-ABI result registers for RISCV64%0A  > 2dcdbd4 go/internal/gcimporter: port CL 431495 to tools, add tests%0A  > d476af7 go/ssa: add slice to array conversion%0A  > d212f7d gopls/internal/regtest/workspace: fix bugs in test%0A  > 051f03f gopls/internal/lsp/cache: remove unnecessary params%0A  > 21f6127 gopls/internal/lsp/cache: add PkgPath->PackageID index to Metadata%0A  > 06041c9 gopls/doc: update manual documentation of the newDiff setting%0A  > f112c43 go.mod: update golang.org/x dependencies%0A  > 207f456 go/internal/gcimporter: bump version number in skew check%0A  > 65196ca gopls/README.md: fix wording around supported Go versions%0A  > 6128030 gopls/internal: support renaming packages with int. test variants%0A  > 649df2e go.mod: mark as requiring -compat 1.16%0A  > 91311ab gopls/internal/lsp/cache: better import path hygiene%0A  > 9eda97b go/analysis: enable a test that applies after go list behavior change%0A  > b50d7ba gopls: minor cleanup of standalone package support%0A  > 502b93c gopls/internal/lsp: tolerate missing end position in RelatedInformation%0A  > d67c3ad internal/imports: repair warnings from default analyzers%0A  > bc2e3ae internal/jsonrpc2_v2: add Func convenience wrappers for the Binder and Preempter interfaces%0A  > a9b653b cmd/compilebench: use -a instead of -i to ensure dependencies are built%0A  > 4818d9e Revert "gopls/internal/lsp/cache: disable strict analysis while we fix panics"%0A  > b2efd4d internal/jsonrpc2_v2: eliminate most arbitrary timeouts in tests%0A  > 371ef16 internal/jsonrpc2_v2: rework concurrency in idleListener%0A  > 5935531 internal/jsonrpc2_v2: remove “Box” suffix from channel field names%0A  > fd32990 internal/jsonrpc2_v2: error out in-flight client calls when the reader breaks%0A  > 0e222f5 internal/jsonrpc2_v2: close the underlying connection if Wait is called instead of Close%0A  > bc4e384 gopls/internal/lsp/cache: fix crash in analysis%0A  > b93a56f refactor/satisfy: fix visiting functions in the unsafe package%0A  > 9b5e55b gopls/internal/lsp/cache: disable strict analysis while we fix panics%0A  > 9ffaf69 gopls/internal/lsp/cache: minor analysis cleanups%0A  > ffb862b gopls/internal/lsp/cache: remove stray print statement%0A  > f87c1ed internal/fastwalk: improve Darwin performance by ~3x%0A  > b253314 gopls/internal/lsp/cache: add support for loading standalone main files%0A  > 3beecff gopls/internal/span: some cleanups%0A  > d375238 gopls: dedup upgrade code actions for vulncheck%0A  > b20ae4b README: format install command%0A  > 19a5504 gopls/internal/lsp: use the golang.org/x/vuln/exp/govulncheck%0A  > ab79327 cmd/ssadump: disable run mode with runtime package%0A  > 29429f5 gopls/internal/lsp/source: sort protocol edits%0A  > 49b340b go/analysis: update tests for different go list error behavior%0A  > cd0288f internal/lsp/cache: invalidate analysis results on packages.Load%0A  > 906c733 gopls/internal/lsp/source: find references in test packages%0A  > 2a41b25 internal/robustio: fix log.Fatal calls that should be log.Fatalf%0A  > 150b5f8 internal/imports: read entire API dir in mkstdlib.go%0A  > 19cfa79 internal/lsp/source: switch the default diff algorithm to "checked"%0A  > fa6bd3b gopls: include informational vulnerability diagnostics%0A  > 89b4335 gopls/internal/lsp: merge notifications about deprecated settings%0A  > f90d8ad all: fix a few function names o…

---
## [yarnpkg/berry](https://github.com/yarnpkg/berry)@[a0064712f7...](https://github.com/yarnpkg/berry/commit/a0064712f7b0ae38c21fb204bea9831c2b269bd7)
#### Monday 2023-07-03 01:53:06 by Maël Nison

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
## [yarnpkg/berry](https://github.com/yarnpkg/berry)@[ec7f37a8ca...](https://github.com/yarnpkg/berry/commit/ec7f37a8ca118a6f73f848e993272db957f286d6)
#### Monday 2023-07-03 01:53:06 by Maël Nison

Modernizes installs' output (#5509)

**What's the problem this PR addresses?**

I wasn't entirely happy with the Yarn output:

- When running `yarn add`, we have no way to know what packages are
actually added to the lockfile. The cache messages sometimes help, but
with zero-installs now being opt-in, in many cases the packages would
already be in the cache and thus wouldn't be displayed at all.

- The "can't be found in the cache and will be fetched from the remote
registry" messages were incredibly slow to print - the same install
would take 28s install for Gatsby on a local iTerm 2 without those logs,
vs almost 2 minutes with. They also weren't very useful: we were only
showing the last 5 of them, and with zero-installs being opt-in in many
cases they wouldn't be shown at all.

- The `node-gyp` warnings were for the most part unactionable (at best
the user would pin a fixed version in their `packageExtensions` field,
which I suspect no one ever did).

- The `deprecated` warnings were for the most part unactionable, and
only printed in very specific cases (the first time they were added to
the project).

- The "missing / invalid peer dependency" warnings were actionable, but
in practice no one really look at them except when something breaks -
and even then, it becomes unreadable when there are too many of them.

- The skipped build warnings were printed every single time you ran
`yarn install`. It's nice to know the first time, then it quickly
becomes redundant.

Fixes #4165

**How did you fix it?**

I went a little overboard and did everything in the same PR ... at first
I thought I wouldn't have to change unrelated parts, but then I finished
implementing the skipped build warnings duplicate removal and oh no 🙈

- Only peer dependency warnings caused by workspaces are now reporter.
They have also been moved inside the post-resolution validation step.
The resolution step is now expected to only do one of two things: either
report an error when the resolution fails, or report the packages which
got added / removed from the lockfile.

- The `node-gyp` warnings have been removed.

- The `deprecated` warnings have been removed from the install. The
`yarn npm audit` command now reports deprecated packages, although this
can be disabled using `--no-deprecations` (or any of the audit filtering
settings).

- The "can't be found in the cache" messages have been removed. Instead,
the fetch step will report the number of cache hits / cache misses once
it's finished (same behaviour as `preferAggregateCacheInfo`). The size
delta will also be reported.

- Packages whose build was skipped are now stored within
`Project#skippedBuilds`, which is stored within the install state file.
Warnings are only emitted if the install was skipped for the first time.
To see the messages again, users can run `yarn rebuild`.

- Added the Yarn version on installs. A bit because of branding when
screenshot are taken, but mostly so we easily know what version are
people using when they share screenshots to us. In a follow-up PR I'd
like to try to retrieve the latest version from the website, to let them
know once one is available.

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
## [yarnpkg/berry](https://github.com/yarnpkg/berry)@[3626ea2ae3...](https://github.com/yarnpkg/berry/commit/3626ea2ae3e48ee26771b15b92292a28afe3d49d)
#### Monday 2023-07-03 01:53:06 by Maël Nison

Adds support for running native binaries without JS intermediaries (#5508)

**What's the problem this PR addresses?**

Yarn currently cannot run native binaries without going through a JS
jumper script. Other package managers don't have this restriction, and
it makes the `yarn run` overhead worse on some scripts for little
reasons - or doesn't work at all when packages don't use jumper scripts.

**How did you fix it?**

Two mechanisms are used:

- First we check for the binary extension
- Then we check its magic number

If one of the two match a predetermined list, the binary is spawned
without going through Node. This ensures that this logic is called only
when the binary is truly a native binary, and will not affect the
behaviour of other existing scripts.

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
## [Toastgoats/tgstation](https://github.com/Toastgoats/tgstation)@[ed57b8127f...](https://github.com/Toastgoats/tgstation/commit/ed57b8127f1b28507272170c60c7db16f6e02a87)
#### Monday 2023-07-03 02:05:18 by Jacquerel

Rat RP expansion (#76455)

## About The Pull Request

This fixes a vile and long-standing bug where putting a mouse inside
your hat would not allow the mouse to control your movements, as it
would pop out of the hat whenever it tried to move.
Additionally as a feature this allows a mouse sitting on your head to
convey complicated instructions such as "scream" or "do a flip", via
emoting. Through drift compatibility, the rat's living mech will also
perform this action.

I could have made this into a component but there's no fucking way any
other item is going to have this behaviour, so I didn't.

## Why It's Good For The Game

This feature was already in the game but broken and I want it not to be
broken.
The mouse should be able to control your entire life.

## Changelog

:cl:
fix: Placing a mouse inside your chef hat will once more allow it to
pilot you around.
add: A player-controlled mouse inside your chef hat can compel you to
perform complex actions, such as flipping and spinning. You will obey
because the mouse knows better than you do.
/:cl:

---
## [JD-The-65th/cyberbreak](https://github.com/JD-The-65th/cyberbreak)@[38d044a7bf...](https://github.com/JD-The-65th/cyberbreak/commit/38d044a7bf049f47bcbb0888332e3ebca30eb3df)
#### Monday 2023-07-03 02:08:51 by JD Williams

Simplify Collision shape HOLY SHIT THAT WAS STUPID
Add Holo shader to Joint

---
## [knative-automation/kn-plugin-source-kamelet](https://github.com/knative-automation/kn-plugin-source-kamelet)@[39007148ee...](https://github.com/knative-automation/kn-plugin-source-kamelet/commit/39007148ee477c7632b5166b0cdc370d85265965)
#### Monday 2023-07-03 02:36:09 by Knative Automation

upgrade to latest dependencies

bumping github.com/fsnotify/fsnotify 0f4b979...5f8c606:%0A  > 5f8c606 Update ChangeLog%0A  > 8878587 Tweak the docs a bit%0A  > 89b4cf1 Add test for re-adding a renamed file (# 508)%0A  > 85acde2 Update x/sys%0A  > 69c24b0 Update x/sys%0A  > fb07f82 Add test to see what happens if you watch a symlink (# 498)%0A  > 666da9c Clarify doc comment on WatchList() (# 499)%0A  > 123e4e3 Add note about README version%0A  > 61a05ce Update documentation and examples (# 496)%0A  > e180a87 Move some inotify-tests to run on all backends; test that state is cleaned up after Remove (# 494)%0A  > fdf41a3 Move some files around%0A  > 844d71f Port minor test changes from fen-v2 branch; make LICENSE text not ugly%0A  > 5b87f50 windows: simplify a bit (# 493)%0A  > 2bfaa00 all: add Watcher.{sendEvent,sendError} (# 492)%0A  > 8ab3b84 kqueue: don't set up watchers on unreadable files (# 479)%0A  > a4bcdf8 Update changelog%0A  > 4b43fad kqueue: remove timeout from unix.Kevent() (# 480)%0A  > a24f78c windows: test symlinks (# 491)%0A  > f45391f windows: run TestWatchRename/rename_overwriting_existing_file (# 490)%0A  > ee33a65 Use "os.Rename()" in tests instead of "mv"%0A  > 9dd0568 cmd/fsnotify: fix time.Format() string%0A  > 5dcbfba windows: replace syscall with golang.org/x/sys/windows%0A  > 1f8edaf windows: replace "e" with "err" for error variables%0A  > 99715ba windows: increase buffer size from 4K to 64K (# 485)%0A  > a5c5815 ci: update to use Go 1.19, kick off fewer builds, update x/sys (# 484)%0A  > f2d35c3 Remove CLA section in contributing%0A  > 4604469 Need Linux 5.9 for a useful fanotify we can use%0A  > a566bb1 Update CONTRIBUTING.md%0A  > 01dfc6f Remove PULL_REQUEST_TEMPLATE%0A  > a58e868 Run tests in illumos (# 481)%0A  > 666c6a0 Update ChangeLog%0A  > 928895c [bugfix] close handle when remWatch open in getIno (# 288)%0A  > f174f95 windows: update watch paths when renaming directories with sub-watches (# 370)%0A  > 87dc1fa Rewrite tests (# 478)%0A  > 57e6a49 Add {Event,Op}.Has() (# 477)%0A  > 39823aa Document that /proc and /sys won't work%0A  > 60fbf57 Clarify FAQ on goroutines%0A  > ca0e2f4 macos: retry if open() returns EINTR (# 475)%0A  > ff39bb4 Fix lint (# 476)%0A  > 421f529 debian 6 test: deal with multiple packages (# 474)%0A  > a3256ef Remove AUTHORS file%0A  > 0e78fa6 Update README: split out FAQ to "Platform-specific notes"%0A  > 1a7b6ef inotify: don't ignore events for files that don't exist (# 470)%0A  > f0aceb2 Tweak comment regarding relative paths (# 466)%0A  > d9c9fa5 Add cmd/fsnotify (# 463)%0A  > cc15908 kqueue: better error if watching a file fails (# 471)%0A  > c4e64e4 Replace Use of Kthread-blocking Epoll with Poller Read, Remove Per-Event LStats on Linux # 433 (# 434)%0A  > 4b8b298 Test some more things in CI (# 469)%0A  > 548b8fb Add missing changelog for 1.4.{8,9} (# 468)%0A  > 7fe2936 inotify: fix race in Close() (# 465)%0A  > 35b6378 Clarify README on network drives (# 467)%0A  > e56409e Update link to CONTRIBUTING in the README (# 464)%0A  > 4678dfd Update documentation for linux systems (max_user_watches) (# 287)%0A  > 808f582 bump up GitHub Actions (# 461)%0A  > 4193dfd Do not suppress Chmod on non-existent file (# 260)%0A  > 6ae56b7 kqueue: Make watcher.Close() O(n) instead of O(n^2) (# 233)%0A  > adf5320 strings.Builder instead of bytes.Buffer (# 285)%0A  > 217e78e Explicit mutext (un)locking (# 462)%0A  > 1a4f949 Use common error when removing an unwatched file (# 460)%0A  > 5acfdc1 windows: protect access to isClosed with mutex (# 454)%0A  > c56cafd Test Go 1.18%0A  > 37badf6 This project is archived (# 459)%0Abumping k8s.io/api 88912e3...6b24792:%0A  > 6b24792 Update dependencies to v0.26.5 tag%0A  > 37e98ba Merge pull request # 117814 from kerthcet/automated-cherry-pick-of-# 117802-upstream-release-1.26%0A  > 7ff025f Update podFailurePolicy comments from alpha-level to beta%0A  > c9f384e Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > c00f1ad Bump runc go module v1.1.4 -> v1.1.6%0A  > 4c28c5a Merge pull request # 117323 from dddddai/automated-cherry-pick-of-# 117182-upstream-release-1.26%0A  > 9483bbc use case-insensitive header keys for http probes%0A  > 0545f3a Merge pull request # 116081 from pohly/automated-cherry-pick-of-# 115928-origin-release-1.26%0A  > e92d7e9 api: generated files%0A  > 16f23da api: drop Resources.Claims from PVC and PVC template%0A  > 5fd8a44 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 1b65b64 Update golang.org/x/net to v0.7.0%0A  > 2e857c1 Merge pull request # 115400 from pohly/automated-cherry-pick-of-# 115354-origin-release-1.26%0A  > 1c6bd70 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 50d0b42 dynamic resource allocation: avoid apiserver complaint about list content%0A  > 045c7fe Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 07a9cbc Merge pull request # 114617 from JoelSpeed/automated-cherry-pick-of-# 114585-upstream-release-1.26%0A  > 52655b9 Resource claims should be a map type%0A  > 07ac8fe Merge remote-tracking branch 'origin/master' into release-1.26%0A  > 566ee01 Update golang.org/x/net 1e63c2f%0A  > b966dc9 sync: update go.mod%0A  > 053624e Merge pull request # 111023 from pohly/dynamic-resource-allocation%0A  > 3590eda Merge pull request # 113375 from atiratree/PodHealthyPolicy-api%0A  > 8356158 api: update testdata%0A  > 5cb3202 Merge pull request # 113186 from ttakahashi21/KEP-3294%0A  > 5a4f9a5 generated%0A  > 78799a8 api: generated files%0A  > dfd6ea2 Generate code%0A  > 993c43c api: add UnhealthyPodEvictionPolicy for PDBs%0A  > ef72ea9 api: dynamic resource allocation API%0A  > d8ab3fb Add API and validation for CrossNamespaceVolumeDataSource%0A  > af772fc api: add resource claims to core API%0A  > 7beaa08 Merge pull request # 112744 from pwschuurman/statefulset-slice-impl%0A  > d7d25c8 Merge pull request # 113360 from mimowo/handling-pod-failures-beta-enable%0A  > f46cd33 Undo unintentional documentation comment change%0A  > f967e44 Merge pull request # 113485 from MikeSpreitzer/apf-borrowing%0A  > 11620b8 Enable the feature into beta%0A  > 6ae95de Fix typo in function emptyInvariants()%0A  > 34f4a52 apiserver: update API testdata at HEAD for flowcontrol%0A  > 3928298 Rebasing feature branch%0A  > e91ffd8 apiserver: add generated files for borrowing in flowcontrol%0A  > d961983 Update doc comments and change name of feature gate%0A  > fcd0d56 apiserver: add fields for borrowing in apf flowcontrol%0A  > adddac7 Small updates and comment fixes%0A  > 98c1aa6 Merge pull request # 113314 from cici37/celIntegration%0A  > 0d02273 Update generated protobuf files%0A  > 3f61c95 Merge pull request # 113688 from dashpole/update_utils%0A  > 8a0a045 API - make update%0A  > a5e7c66 Adding implementation of KEP-3335, StatefulSetSlice%0A  > 72a29bf Merge pull request # 113500 from kerthcet/feat/graduate-nodeInclusionPoplicy-to-beta%0A  > 2a2f510 update k8s.io/utils to fix util tracing panic%0A  > 891a1f8 Adding new api version of admissionregistration.k8s.io v1alpha1 for CEL in Admission Control%0A  > ee30dcf Merge pull request # 113047 from everpeace/improve-supplemental-groups-description%0A  > 2482389 Feat: graduate NodeInclusionPolicy to beta%0A  > a489930 Rename copy to v1alpha1%0A  > 9a33ad3 Merge pull request # 112360 from mimowo/handling-pod-failures-beta-kubelet%0A  > c4b2250 Improve the description of PodSecurityContext.SupplementalGroups (including cri-api)%0A  > 358a069 Copy over admissionregistration v1 to v1alpha1%0A  > 6c616e1 Merge pull request # 113510 from alculquicondor/finalizers-stable%0A  > 5210e2f Add pod disruption conditions for kubelet initiated failures%0A  > 2025045 Merge pull request # 113351 from andrewsykim/endpointslice-terminating-ga%0A  > aa2b4eb Graduate JobTrackingWithFinalizers to stable%0A  > 4bad656 Merge pull request # 113274 from Huang-Wei/kep-3521-A%0A  > aa9d0a7 k8s.io/api/discovery: remove API docs referencing EndpointSliceTerminatingCondition feature gate%0A  > 91f2496 Merge pull request # 113496 from avoltz/anvoltz/ga-itr%0A  > 686871f Automated codegen%0A  > c865c5c Promote ServiceInternalTrafficPolicy to GA%0A  > bd25e4f APIs, Validation and condition enforcements%0A  > 5448eb3 Merge pull request # 106242 from thockin/revive-copy-lb-status-type-to-ingress%0A  > edbfe77 Copy LoadBalancerStatus from core to networking%0A  > 6892570 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > c5dc3f4 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > 4e8dc44 Merge pull request # 111978 from Jefftree/aggregated-discovery-types%0A  > 72580e4 Add discovery types%0A  > 0184bd8 Merge pull request # 112643 from SergeyKanzhelev/removeDynamicKubeletConfig%0A  > 0f81104 Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > f8118a1 remove DynamicKubeletConfig feature gate from the code%0A  > 370c8f0 Bump golang.org/x/text to v0.3.8%0A  > 3638040 Merge pull request # 112875 from pohly/update-yaml%0A  > 7ecab5c dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 669318b Merge pull request # 112832 from tkashem/apf-prelifecycle-gen%0A  > 2cfef31 apiserver: prerelease-lifecycle-gen for flowcontrol%0A  > 3cedfad Merge pull request # 112306 from tkashem/v1beta3%0A  > 3814236 Merge pull request # 112707 from enj/enj/i/https_links%0A  > 418dd97 add testdata for flowcontrol v1beta3%0A  > ba008c5 Use https links for k8s KEPs, issues, PRs, etc%0A  > c96c62f rename assuredConcurrencyShares for flowcontrol v1beta3%0A  > be233f8 Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 51a3f54 add patch annotations to flowcontrol v1beta3%0A  > ca5be1f Update to latest k8s.io/utils to pick up changes%0A  > 7e203ee apiserver: generate for apf v1beta3%0A  > 79091da Merge pull request # 112577 from andrewsykim/feature-gate-cleanup%0A  > 19d0ef4 apiserver: enable v1beta3 for apf%0A  > 052d63f Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 1f28922 remove +featureGate=LoadBalancerClass tag in service.spec.loadBalancerClass%0A  > f50a5b7 apiserver: apf rename copy to v1beta3%0A  > 9df3db1 updated etcd to v3.5.5 and newer otel libraries as well%0A  > bed6431 apiserver: copy apf v1beta2 to v1beta3%0A  > c98ebf1 Merge pull request # 112487 from liggitt/flowcontrol-test%0A  > 5c9e17a Add compatibility fixtures for v1beta2 flowcontrol%0A  > 9842651 Merge pull request # 111333 from flant/selfsubjectattributesreviews%0A  > 43df43b Add auth API to get self subject attributes%0A  > 30ff991 Merge pull request # 112349 from pohly/klog-update%0A  > e6114e9 build: update to klog v2.80.1%0A  > 929c3f0 Merge pull request # 112301 from aojea/ipv6_rfc3849%0A  > a687cab use IPv6 Address Prefix Reserved for Documentation for api docs%0A  > 6dd661f Merge pull request # 112199 from pohly/klog-update%0A  > 8a7d12c dependencies: update to klog v2.80.0%0A  > a6ff7c9 Merge pull request # 112146 from kerthcet/feat/move-schedulerError-to-api%0A  > ab89e44 Move constant schedulerError in scheduler to v1 package%0A  > d104994 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 15b6dd2 Bump prometheus/client_golang to v1.13.0%0A  > 3be0a3c Merge pull request # 111974 from liggitt/1-25-compatibility%0A  > 49e055e Merge pull request # 111830 from t1anz0ng/typo%0A  > fcc83cd Drop 1.23 compatibility data%0A  > 64f80bd Merge pull request # 111611 from kardashov/ref-spec-docs-typo-fix%0A  > ea5df3a fix(typo): remove extra " from autoscaling doc string%0A  > 4cde1ad Add 1.25 compatibility data%0A  > 2e7b661 Merge pull request # 111657 from aojea/hc_nodeport%0A  > d07af88 Generate specs after fixing typo in documentation%0A  > 649256a Fix typo in field description.%0Abumping golang.org/x/term d974fe8...0edf009:%0A  > 0edf009 go.mod: update golang.org/x dependencies%0Abumping knative.dev/hack f591fea...fc42790:%0A  > fc42790 Update community files (# 296)%0A  > d7586a2 Update e2e kntest link (# 295)%0A  > a861c8e Update community files (# 294)%0A  > 5b7907f Update actions (# 289)%0A  > c133d5d Install Istio for tests (# 291)%0A  > 5812c57 Update community files (# 292)%0A  > 7d81248 Update community files (# 286)%0A  > 6e4569c Update community files (# 285)%0Abumping golang.org/x/net 8e2b117...dfa2b5d:%0A  > dfa2b5d go.mod: update golang.org/x dependencies%0A  > 8c4ef2f hmtl: add security section to package comment%0A  > 1d46ed8 html: have Render escape comments less often%0A  > 569fe81 html: add "Microsoft Outlook comment" tests%0Abumping k8s.io/apiextensions-apiserver 2c55649...52c998e:%0A  > 52c998e Update dependencies to v0.26.5 tag%0A  > 186ff9b Merge pull request # 117274 from jkh52/release-1.26-knp-0.0.37%0A  > b7b18f5 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > ee5015a Bump konnectivity-client to 0.0.37%0A  > 9ce75f3 Bump runc go module v1.1.4 -> v1.1.6%0A  > e9d194a Merge pull request # 115599 from jkh52/release-1.26-knp-0.0.36%0A  > d7df0be Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 9152c67 Bump konnectivity-client to v0.0.36%0A  > 89cec57 Update golang.org/x/net to v0.7.0%0A  > f72cc5c Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 28eb995 Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 33db789 Merge pull request # 114861 from jpbetz/release-1.26%0A  > a06e03d Merge pull request # 114927 from jkh52/release-1.26-knp-metrics%0A  > 0859963 Cherry pick 114857 to release-1.26%0A  > 5183885 Bump konnectivity-client to v0.0.35%0A  > 6e13726 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > c338f3e Update golang.org/x/net 1e63c2f%0A  > 9768bad sync: update go.mod%0A  > f9c2bba fix aggregated discovery version sorting%0A  > d2c9e18 Merge pull request # 113171 from Jefftree/aggregated-discovery-generic%0A  > 470c040 Merge pull request # 113577 from pacoxu/prometheus-client%0A  > 915a888 add crds to aggregated discovery%0A  > 92430b6 Merge pull request # 113314 from cici37/celIntegration%0A  > ac326ca upgrade prometheus-client to v1.14.0%0A  > 5a6bf16 Merge pull request # 113688 from dashpole/update_utils%0A  > 67b0610 Integrate cel admission with API.%0A  > 84fed82 upgrade github.com/prometheus/client_golang to v1.13.1%0A  > 077b441 update k8s.io/utils to fix util tracing panic%0A  > 5bbf20d Adding new api version of admissionregistration.k8s.io v1alpha1 for CEL in Admission Control%0A  > 3b533ba Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > 975bbeb dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > ae2b4c3 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > c4deae9 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > bc4263f Merge pull request # 113172 from dashpole/endpoint_handler_tracing%0A  > f6c164e migrate apiserver utiltrace usage to component-base/tracing%0A  > 53e3726 Merge pull request # 113015 from ritazh/crencryption%0A  > c8d8a9f Enable encryption for custom resources%0A  > 6405068 Merge pull request # 113325 from panslava/fix-time-since-defer%0A  > 508e399 Fix time.Since() in defer. Wrap in anonymous function%0A  > 5f8e59e Merge pull request # 112691 from aimuz/apiextensions-apiserver-change-to-cmp%0A  > c996139 Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > f83e03c apiextensions-apiserver: change k8s.io/apimachinery/pkg/util/diff to github.com/google/go-cmp/cmp%0A  > b68fc51 dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > 49c41b4 Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > 3aaa2a0 Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > d9f6ebd update kube-openapi%0A  > 82e3ba4 Merge pull request # 112789 from enj/enj/r/kms_load_once_v2%0A  > 7423813 update fsnotify to v1.6.0%0A  > 8bf3487 Merge pull request # 113011 from jpmcb/cobra-1.6.0%0A  > d34393e Load encryption config once%0A  > 6ba582f Bumps cobra from 1.5.0 to 1.6.0%0A  > 8e0697b Merge pull request # 113022 from logicalhan/webhook-metrics%0A  > 90c63e0 Merge pull request # 112926 from jiahuif-forks/refactor/cel-out-of-apiextensions%0A  > 548c480 unparameterize 'webhook' from conversion metrics since it's the only one%0A  > 77badb8 Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 609e270 use DefaultMaxRequestSizeBytes for maxRequestSizeBytes.%0A  > 04f26fa Bump golang.org/x/text to v0.3.8%0A  > dd981e1 move CEL package to apiserver package.%0A  > 1644998 Move celopenapi/model to staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/cel/ (# 109959)%0A  > 08d44e8 Merge pull request # 112875 from pohly/update-yaml%0A  > 1300140 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 5fb82bd Merge pull request # 112819 from thockin/no-make-generators%0A  > f5f5279 Codegens: Do not auto-set boilerplate path%0A  > f22ee73 Merge pull request # 112738 from liggitt/proto-tag%0A  > ba7f1b7 Merge pull request # 112689 from cheftako/master%0A  > 7ac7774 github.com/matttproud/golang_protobuf_extensions v1.0.2%0A  > e678457 Merge pull request # 112748 from wojtek-t/lock_ssa_gate%0A  > 0aca5a6 Bump konnectivity-client to v0.0.33%0A  > 9be4b4a Lock ServerSideApply feature to true%0A  > 7b53cb7 Merge pull request # 111980 from aramase/kms%0A  > f40a683 Merge pull request # 112705 from stevekuznetsov/skuznets/fix-comment%0A  > 4cd9125 Add staging directory for kms%0A  > d4e654a clients: clarify a misleading comment%0A  > 8b851d9 Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 362a89c Merge pull request # 112615 from mengjiao-liu/update_CRD_link%0A  > add0c80 Update to latest k8s.io/utils to pick up changes%0A  > 374216b Merge pull request # 112613 from dims/update-github.com/go-openapi/jsonreference-to-drop-github.com/PuerkitoBio/purell%0A  > a7ee7f9 Update `PreserveUnknownFields` field document link%0A  > 488bf20 update github.com/go-openapi/jsonreference to drop github.com/PuerkitoBio/purell%0A  > 47c15ca Merge pull request # 112588 from pacoxu/fsnotify-v1.5.4%0A  > d5b6243 Merge pull request # 112584 from dims/brneto-master%0A  > 8c6aa82 update fsnotify/fsnotify to v1.5.4%0A  > f8e18e9 run pin-dependency.sh and then hack/update-vendor.sh%0A  > c540c8c Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 70b0d96 Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 39cab0b updated etcd to v3.5.5 and newer otel libraries as well%0A  > 5faccda Merge pull request # 111866 from pacoxu/validate%0A  > 1c3fe9d e2e: bump ginkgo to v2.2.0%0A  > 917d446 Merge pull request # 112458 from dims/switch-to-release-tag-for-antlr-v1.4.10%0A  > 8b3fe74 add test case for array checking with dup values%0A  > 045fc90 Merge pull request # 112433 from ncdc/reduce-SchemaHas-allocs%0A  > 73cc883 Switch to release tag for antlr : v1.4.10%0A  > 22bcc66 added ratcheting validation for embedded resource and x-kubernetes-list-type validation%0A  > 269d73d Reduce allocations in HasSchemas%0A  > 7342cc6 Merge pull request # 112200 from pohly/client-go-shared-informer-factory-shutdown%0A  > aabbdff Merge pull request # 112349 from pohly/klog-update%0A  > fdf28bc client-go: support waiting for SharedInformerFactory shutdown%0A  > 6b7d12b build: update to klog v2.80.1%0A  > 559b4fa Merge pull request # 111768 from weilaaa/feature_add_symmetric_difference_in_sets_string%0A  > bf7d058 add symmetric difference in sets%0A  > 04ff81e Merge pull request # 112199 from pohly/klog-update%0A  > 87a4c3f dependencies: update to klog v2.80.0%0A  > 8f15690 Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > f637e1c dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > b6adc1c Merge pull request # 111964 from DangerOnTheRanger/cel-estimate-fix-update%0A  > ea2d438 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 6b4dc0b Add unit tests.%0A  > 767e67b Bump prometheus/client_golang to v1.13.0%0A  > 782b982 Run pin-dependency.sh and update-vendor.sh.%0A  > 305963e Merge pull request # 111909 from tosi3k/bump-prom-client%0A  > fa2959a Merge pull request # 111830 from t1anz0ng/typo%0A  > 5a6ffec Bump prometheus/client_golang to v1.12.2%0A  > e0abc3b fix(typo): remove extra " from autoscaling doc string%0A  > 2184a8d Merge pull request # 111696 from liggitt/go119mod%0A  > f750907 Update go.mod to go1.19%0Abumping knative.dev/client-pkg 4f052f9...f377f06:%0A  > f377f06 Update community files (# 106)%0A  > b93ceb0 Update community files (# 105)%0A  > 83c91f4 Update community files (# 103)%0A  > e5c405e Update community files (# 102)%0A  > eee9b55 Update community files (# 100)%0Abumping k8s.io/client-go 7226b15...6e9dabb:%0A  > 6e9dabb Update dependencies to v0.26.5 tag%0A  > 038b381 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > cd83e43 Bump runc go module v1.1.4 -> v1.1.6%0A  > dbfbc03 Merge pull request # 117686 from ardaguclu/automated-cherry-pick-of-# 117495-upstream-release-1.26%0A  > d72dec4 Use absolute path instead requestURI in openapiv3 discovery%0A  > a5144d4 Merge pull request # 117638 from seans3/automated-cherry-pick-of-# 117571-origin-release-1.26%0A  > d6f8d04 Refactors discovery content-type and helper functions%0A  > 2dd0093 Merge pull request # 115899 from odinuge/automated-cherry-pick-of-# 115620-upstream-release-1.26%0A  > f3ae5cb Merge pull request # 116666 from seans3/automated-cherry-pick-of-# 116603-origin-release-1.26%0A  > fffc68d Change where transformers are called.%0A  > 5ebee18 Aggregated discovery resilient to nil GVK%0A  > 8190aa4 client-go/cache: update Replace comment to be more clear%0A  > 87720b3 Merge pull request # 116437 from seans3/automated-cherry-pick-of-# 116145-# 115865-origin-release-1.26%0A  > b667227 client-go/cache: rewrite Replace to check queue first%0A  > fc13749 Removes old discovery hack ignoring 403 and 404%0A  > 30215cd client-go/cache: merge ReplaceMakesDeletionsForObjectsInQueue tests%0A  > f39ba12 Plumb stale GroupVersions through aggregated discovery%0A  > ba35969 client-go/cache: fix missing delete event on replace without knownObjects%0A  > f538edf Merge pull request # 116352 from seans3/automated-cherry-pick-of-# 115978-origin-release-1.26%0A  > 97cf9cb client-go/cache: fix missing delete event on replace%0A  > 5dbbc58 Tolerate empty discovery response in memcache client%0A  > 62133a9 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 8ce239f Update golang.org/x/net to v0.7.0%0A  > e6bc0bc Merge pull request # 115566 from enj/automated-cherry-pick-of-# 115315-upstream-release-1.26%0A  > 9112e19 Merge pull request # 115400 from pohly/automated-cherry-pick-of-# 115354-origin-release-1.26%0A  > 0519b53 kubelet/client: collapse transport wiring onto standard approach%0A  > 2e34348 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 7be38cd dynamic resource allocation: avoid apiserver complaint about list content%0A  > 4968c4a Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 0c34939 Merge pull request # 114617 from JoelSpeed/automated-cherry-pick-of-# 114585-upstream-release-1.26%0A  > 04b098b Resource claims should be a map type%0A  > b3fff46 Merge pull request # 114415 from hoskeri/automated-cherry-pick-of-# 114404-upstream-release-1.26%0A  > 236db3c Merge pull request # 113988 from liggitt/automated-cherry-pick-of-# 113933-upstream-release-1.26%0A  > a2ef324 Check the correct error in d.downloadAPIs%0A  > 95a14c3 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > ebb499f Limit request retrying to []byte request bodies%0A  > 1a7cd1d Update golang.org/x/net 1e63c2f%0A  > 53f2fea sync: update go.mod%0A  > 968ba8d Merge pull request # 113797 from seans3/force-no-aggregated%0A  > c8ffed3 Merge pull request # 111023 from pohly/dynamic-resource-allocation%0A  > 3ac73ea Adds bool to force non-aggregated discovery%0A  > 61cd728 Merge pull request # 113826 from jsafrane/add-openstack%0A  > 522eaa1 api: generated files%0A  > cfd682c Merge pull request # 113375 from atiratree/PodHealthyPolicy-api%0A  > f2b10f3 Remove OpenStack cloud provider%0A  > acc9fa7 Merge pull request # 113186 from ttakahashi21/KEP-3294%0A  > f1c80d7 generated%0A  > a3d3eb0 Revert "Remove references to openstack and cinder"%0A  > c7bdab2 Generate code%0A  > 0a1f6a8 Merge pull request # 112744 from pwschuurman/statefulset-slice-impl%0A  > 1c7a870 Merge pull request # 113485 from MikeSpreitzer/apf-borrowing%0A  > eed2516 Adding implementation of KEP-3335, StatefulSetSlice%0A  > 7280270 Merge pull request # 113599 from seans3/discovery-client-update%0A  > d4a3675 apiserver: add generated files for borrowing in flowcontrol%0A  > 7694435 Update redacting functionality to redact all sensitive info in config when printing with view (# 109189)%0A  > 25d5761 Aggregated discovery client%0A  > 4b1a9fd Merge pull request # 113314 from cici37/celIntegration%0A  > ea9ec91 Merge pull request # 112905 from alexzielenski/kubectl-apply-csa-migration%0A  > 3a430a4 API - make update%0A  > 3daf180 Merge pull request # 113688 from dashpole/update_utils%0A  > 898b7a3 add FindFieldsOwners util function%0A  > dbe034b update k8s.io/utils to fix util tracing panic%0A  > 4f63b62 add UpgradeManagedFieldsPatch%0A  > 7ed3193 Merge pull request # 111545 from jlsong01/rewrite_signature_of_StartEventWatcher%0A  > c8c6cb5 add OWNERS to csaupgrade%0A  > cbe28cf Merge pull request # 113274 from Huang-Wei/kep-3521-A%0A  > 3467961 rewrite signature of function StartEventWatcher%0A  > a45874a remove kubectl annotation logic from upgrade patch%0A  > 2248bf3 Automated codegen%0A  > d576a35 Merge pull request # 113387 from wojtek-t/refactor_client_indexing%0A  > 4fbef5b Merge pull request # 106242 from thockin/revive-copy-lb-status-type-to-ingress%0A  > 5e7ba1f Minor cleanup of thread safe store%0A  > bc6266d Merge pull request # 103177 from arkbriar/support_cancelable_exec_stream%0A  > 3f162fe Copy LoadBalancerStatus from core to networking%0A  > b69a16c Refactor store index into its structure%0A  > 19b2e89 Merge pull request # 113523 from seans3/content-type-response%0A  > 0563dec Propagate the panic with a channel%0A  > 8ff4970 Get response content-type%0A  > 2362c7b use subtests and defer in TestSPDYExecutorStream%0A  > 0d57396 Merge pull request # 113304 from mimowo/handling-pod-failures-beta-ssa%0A  > 5e0a531 Support cancelable SPDY executor stream%0A  > a232cf0 Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > a191e58 SSA to add pod failure conditions - ready for review%0A  > 984bdbf dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > f87d047 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > d236783 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > ef8a2e5 Merge pull request # 113089 from zackzhangkai/fix-doc%0A  > 197e479 Merge pull request # 108959 from astraw99/fix-duplicate-list%0A  > 0945beb fix typo%0A  > 42a0e1c Merge pull request # 113062 from alexzielenski/client-go-json-output%0A  > f549acf Fix duplicate code block of ListAll function%0A  > b6d3c8d Merge pull request # 107278 from harsimranmaan/allow_pagination_in_dynamic_fake_lister%0A  > 624929c address feedback%0A  > 9cc33a4 Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > 0c269b7 remove selflink as per review feedback%0A  > 12cafe2 refactor to use Schema(contentType)%0A  > 9b51067 dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > fbd8e9a fix failing test assertions%0A  > 8b6ceae add more options for fetching openapiv3 in clients%0A  > fa9ed7f Merge pull request # 112860 from nckturner/remove-log-line%0A  > 1f10368 Preserve metadata for fake dynamic client unstructured lists%0A  > 6b24912 Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > 5870c62 Remove log line from expiration cache%0A  > aea20dd Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > e3bb48f update kube-openapi%0A  > 1af3711 update fsnotify to v1.6.0%0A  > e6d958c Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 5e469ba Bump golang.org/x/text to v0.3.8%0A  > f515a4c Merge pull request # 112774 from stevekuznetsov/skuznets/dynamic-client-similar%0A  > b28f6c9 Merge pull request # 112875 from pohly/update-yaml%0A  > 34e8a5d client-go: factor the dynamic client similarly to others%0A  > c9afc73 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > f24bd69 Merge pull request # 112306 from tkashem/v1beta3%0A  > ebc7cd4 Merge pull request # 112707 from enj/enj/i/https_links%0A  > 9b97b72 rename assuredConcurrencyShares for flowcontrol v1beta3%0A  > 2f43d37 Merge pull request # 112705 from stevekuznetsov/skuznets/fix-comment%0A  > 1665808 Use https links for k8s KEPs, issues, PRs, etc%0A  > 9bac803 apiserver: generate for apf v1beta3%0A  > 3697342 Merge pull request # 112680 from enj/enj/i/tls_cache_key_comparable%0A  > 956c1ce clients: clarify a misleading comment%0A  > c81636c Merge pull request # 112665 from NoicFank/fix-typo%0A  > cc2441c transport/cache: statically assert that tlsCacheKey is comparable%0A  > be20b2b Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 59765b8 fix typo error%0A  > 04dbcd8 Update to latest k8s.io/utils to pick up changes%0A  > 2fd4aac Merge pull request # 112613 from dims/update-github.com/go-openapi/jsonreference-to-drop-github.com/PuerkitoBio/purell%0A  > 47ad72a update github.com/go-openapi/jsonreference to drop github.com/PuerkitoBio/purell%0A  > f7c9c63 Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > b6e72dc Merge pull request # 112226 from aojea/client_go_transport%0A  > 6b5ecad updated etcd to v3.5.5 and newer otel libraries as well%0A  > acfaa39 Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 1bd914a client-go: test transport generation is goroutine safe%0A  > 037b5fd Merge pull request # 112514 from markmc/patch-1%0A  > ec6c80a e2e: bump ginkgo to v2.2.0%0A  > 3f66212 client-go: remove reference to TPR in examples%0A  > 86ffa32 Merge pull request # 112475 from vatsalparekh/fix-TestRESTClientLimiter%0A  > ece6462 Merge pull request # 112476 from enj/enj/i/list_pager_flake%0A  > bf2b395 Fix Infelicities in TestRESTClientLimiter%0A  > 58155b7 Merge pull request # 112450 from enj/enj/i/exec_tls_cache_holder_cleanup%0A  > 6703098 Check for context cancellation on each buffered chunk%0A  > eecd3e5 Merge pull request # 112091 from xyz-li/master%0A  > 5dab9a0 client-go/transport: drop Dial and GetCert fields in favor of Holders%0A  > f6b8521 Merge pull request # 111333 from flant/selfsubjectattributesreviews%0A  > cc3cc93 kubectl: fix memory leaks in port forwarding client%0A  > b2b55e6 Add auth API to get self subject attributes%0A  > 18c3338 Merge pull request # 112200 from pohly/client-go-shared-informer-factory-shutdown%0A  > 9dae691 Merge pull request # 112309 from shyamjvs/disable-compression%0A  > ec4fedd client-go: support waiting for SharedInformerFactory shutdown%0A  > ab826d2 Merge pull request # 112349 from pohly/klog-update%0A  > 49ac40b Autogen code%0A  > ab0bfda build: update to klog v2.80.1%0A  > b8a8d94 Add DisableCompression option to KubeConfig%0A  > f32861c Merge pull request # 112341 from enj/enj/i/second_time_is_the_charm%0A  > 7d208ba Remove in-tree credential plugins (again)%0A  > e003fa9 Merge pull request # 112017 from enj/enj/i/exec_tls_cache%0A  > 2698e82 Merge pull request # 111967 from alexzielenski/csa-to-ssa%0A  > 6a008ec exec auth: support TLS config caching%0A  > 27c67e7 Merge pull request # 111122 from alexzielenski/informer%0A  > 00d892f correct spacing%0A  > d28c736 Merge pull request # 112022 from JackZxj/release-lock%0A  > a300ae0 return when test is done%0A  > 2efbeaf add boilerplate%0A  > b8b6206 Merge pull request # 112199 from pohly/klog-update%0A  > d04c2ce update lock getter of leaderelection%0A  > 93e5e0e hold listener lock while waiting for goroutines to finish%0A  > dac0826 remove inaccurate comment%0A  > 5a2c3e9 dependencies: update to klog v2.80.0%0A  > e11a988 simplify control flow%0A  > 7634f2e make upgrade modify input instead of deep copying%0A  > 7ccf7b0 Merge pull request # 112134 from apelisse/client-go-valid-segment%0A  > ac7f657 fix spelling%0A  > 9aa7c11 remove fieldsv1 from upgrade body%0A  > d83ec9e Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > a4b84d8 Validate segments with client-go/dynamic%0A  > 0f4a6cf reset listenersStarted%0A  > 703d15e Update staging/src/k8s.io/client-go/util/csaupgrade/upgrade.go%0A  > cac10a8 dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > 449817f add multithreaded test to shared informer%0A  > 675ca93 refactor if statement%0A  > 46d4284 Merge pull request # 111241 from Abirdcfly/fixtestorsource%0A  > de0b767 remove duplicate test%0A  > cfaca90 address comments%0A  > bdae576 Merge pull request # 112068 from aojea/aojea_client_go%0A  > 9b300de make TestListPager_EachListItem rework%0A  > 0565962 address review comments%0A  > 089614c remove last applied configuration information%0A  > fd22687 add aojea as client-go reviewer%0A  > 5a25eb0 switch listeners to use a map, adapt tests%0A  > efe3789 add more test cases%0A  > 35ead05 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 90c6a46 active remove/add tests for event handlers%0A  > 46dc22f clean up test%0A  > 5291ca2 Bump prometheus/client_golang to v1.13.0%0A  > de4dd3a tests for invalid registration removals%0A  > ced85a8 update godoc%0A  > e6538dd Merge pull request # 112024 from cndoit18/remove-redundant-judgment%0A  > 33eff64 apply desired changes for handler registration%0A  > 049ba69 expose FieldsToSet and SetToFields%0A  > bcd2e6c style: remove redundant judgment%0A  > d73e40f rename handle to registration%0A  > aa892ab remove  unused code%0A  > d5e5863 Merge pull request # 111752 from aanm/revert-final-url-template%0A  > b3a61c6 remove informational informer methods again%0A  > 90ef078 dont expose internal methods in implementatoin%0A  > 5feaced Merge pull request # 67782 from dims/yank-in-tree-openstack-cloud-provider%0A  > e9d4627 client-go/rest: check if url is nil to prevent nil pointer dereference%0A  > ecdc8bf support removal of event handlers from SharedIndexInformers%0A  > c364b63 add function to upgrade managedfields CSA to SSA%0A  > 0fdc4f3 Merge pull request # 111684 from 0xff-dev/master1%0A  > 98e81a7 Remove references to openstack and cinder%0A  > c501ee0 Revert "client-go: remove no longer used finalURLTemplate"%0A  > 4faffa8 Merge pull request # 111564 from inosato/remove-ioutil-from-cli-client-go%0A  > c94a539 use constant NamespaceDefault instead of variable namespace%0A  > 2e40408 Merge pull request # 111918 from liggitt/in-tree-auth%0A  > 27de641 Remove ioutil from client-go%0Abumping golang.org/x/text 71a9c9a...9db913a:%0A  > 9db913a go.mod: update to newer x/tools%0A  > 30dadde all: correct comment typos%0Abumping knative.dev/serving 2c1bb07...4c3b36c:%0A  > 4c3b36c Update net-gateway-api nightly (# 14136)%0A  > 9a75a93 Update net-istio nightly (# 14132)%0A  > ca618b7 Update net-certmanager nightly (# 14131)%0A  > ea3e9c3 Update net-contour nightly (# 14130)%0A  > 2e7d6e4 Update community files (# 14128)%0A  > 63fa389 Allow to set QP resources per service (# 14038)%0A  > 9310e4d Update net-kourier nightly (# 14125)%0A  > 0462ce6 Update net-istio nightly (# 14126)%0A  > 2813b9a Update net-gateway-api nightly (# 14119)%0A  > eaf666e Update net-istio nightly (# 14116)%0A  > 53169cd Update net-istio nightly (# 14112)%0A  > e865aa7 Update net-contour nightly (# 14109)%0A  > 921daf8 Update net-certmanager nightly (# 14111)%0A  > bb581cc Update net-kourier nightly (# 14110)%0A  > fbfffc0 upgrade to latest dependencies (# 14108)%0A  > bcf9274 upgrade to latest dependencies (# 14101)%0A  > f085b30 fix: requests are sent to all pods even if cc=1 and the parity of activatorCount and podTracker is different (# 14022)%0A  > 9772417 Update net-kourier nightly (# 14107)%0A  > f6d0c7b Update net-contour nightly (# 14106)%0A  > 560e0ea Update net-certmanager nightly (# 14105)%0A  > 51f4f1e Update net-istio nightly (# 14104)%0A  > 18519b1 Update net-contour nightly (# 14079)%0A  > 38c155e Add chainguard-dev/actions for creating kind cluster (# 14018)%0A  > 74c57d8 Update net-istio nightly (# 14098)%0A  > 5a9c574 Update net-kourier nightly (# 14096)%0A  > 3a6c2b6 upgrade to latest dependencies (# 14095)%0A  > 5a90438 Update net-istio nightly (# 14091)%0A  > dc0692a Update net-istio nightly (# 14088)%0A  > 0fbd780 Update net-certmanager nightly (# 14087)%0A  > 6f63c98 Update net-kourier nightly (# 14086)%0A  > e74f5f4 Update net-gateway-api nightly (# 14085)%0A  > 1587070 Update net-kourier nightly (# 14081)%0A  > 2e00e9f Update net-certmanager nightly (# 14080)%0A  > a3c7864 Update net-istio nightly (# 14078)%0A  > 384b889 Update net-gateway-api nightly (# 14077)%0A  > 7d0f963 Change storage version of DomainMapping to v1beta1 (# 14058)%0A  > e8b6f05 Update net-gateway-api nightly (# 14068)%0A  > 41e4212 Get certificate reconciler from `networking` instead of `control-protocol` (# 14072)%0A  > e71b933 Update net-certmanager nightly (# 14070)%0A  > 8f516b6 Update net-kourier nightly (# 14069)%0A  > a2bb4aa upgrade to latest dependencies (# 14071)%0A  > c95f17b Update community files (# 14067)%0A  > bf48e64 Remove deprecated internalEncryption dependency (# 14064)%0A  > 6b87d67 Update net-istio nightly (# 14065)%0A  > fbecf34 refactor throttler_test.go (# 14055)%0A  > 349b2d6 Change minimum TLS version to 1.3 for internal encryption (between activator and queue-proxy) (# 13887)%0A  > d07bf78 Update net-contour nightly (# 14049)%0A  > aa023e8 Update net-istio nightly (# 14048)%0A  > 8fc4bb9 Update net-gateway-api nightly (# 14047)%0A  > 135be30 Update net-certmanager nightly (# 14046)%0A  > 8da71b5 Update net-kourier nightly (# 14042)%0A  > 13a4e46 poll until timeout - don't error out if the deployment can't be found (# 14027)%0A  > 31c2b7e upgrade to latest dependencies (# 14043)%0A  > 6a6e417 Update net-istio nightly (# 14041)%0A  > 807fc2c Update net-certmanager nightly (# 14040)%0A  > 3c23945 drop safe to evict annotations (# 14035)%0A  > fca5c14 Update net-gateway-api nightly (# 14033)%0A  > c12c917 Update net-contour nightly (# 14034)%0A  > 2da856d Update net-kourier nightly (# 14032)%0A  > d7c8779 Update net-certmanager nightly (# 14031)%0A  > aaf01dc Update net-istio nightly (# 14030)%0A  > bdaa436 RandomChoice 2 policy wasn't random when the number of targets is 2 (with equal weight) (# 14028)%0A  > c91f8c4 Fix metrics reporting period (# 14019)%0A  > 9f60969 Update net-kourier nightly (# 14004)%0A  > 6020cec Update net-istio nightly (# 14025)%0A  > 88cae7f Update net-gateway-api nightly (# 14016)%0A  > a143bf8 Update net-contour nightly (# 14015)%0A  > c2be582 Update net-certmanager nightly (# 14014)%0A  > 3450f0a upgrade to latest dependencies (# 14013)%0A  > 35cfd8f [Automated] Update net-gateway-api nightly (# 14003)%0A  > 08a9708 Update net-istio nightly (# 14009)%0A  > 5074b4c Update net-contour nightly (# 14010)%0A  > e8cb343 upgrade to latest dependencies (# 13999)%0A  > 1261074 Update net-certmanager nightly (# 14002)%0A  > f987ca6 Bump kind to 0.19 (# 14008)%0A  > fbb7fa1 Update community files (# 13998)%0A  > bff1d80 Remove 1.24 kind version (# 14007)%0A  > a657321 Update net-kourier nightly (# 13993)%0A  > d75b0f0 Update net-contour nightly (# 13990)%0A  > 6d26f54 upgrade to latest dependencies (# 13991)%0A  > df5001f Update net-certmanager nightly (# 13992)%0A  > 2594084 upgrade to latest dependencies (# 13989)%0A  > 7c303fa Update cluster-version to 1.25 (# 13988)%0A  > 9e751a2 Update net-certmanager nightly (# 13974)%0A  > 7b35cfb upgrade to latest dependencies (# 13987)%0A  > 99800ed Set default domain to cluster's domain (# 13964)%0A  > c90fabf Metric annotations work with global class config (# 13978)%0A  > da31cd1 Update net-kourier nightly (# 13975)%0A  > f457924 Update net-contour nightly (# 13976)%0A  > 14ad4d1 upgrade to latest dependencies (# 13973)%0A  > 00ddfd9 Update net-kourier nightly (# 13972)%0A  > fc63583 Update net-kourier nightly (# 13966)%0A  > 219285e Update net-kourier nightly (# 13959)%0A  > 2fa05bd Min TLS for tag to digest defaults to 1.2 again and is configurable (# 13962)%0A  > 43df348 Update net-contour nightly (# 13958)%0A  > 50a9f22 Update net-certmanager nightly (# 13961)%0A  > 4e379cb Update net-gateway-api nightly (# 13957)%0A  > 3d53294 Update net-istio nightly (# 13960)%0A  > ea2a6c8 :lipstick: Install ko using setup-ko, from ko-build (# 13951)%0A  > e5070cd upgrade to latest dependencies (# 13950)%0A  > 9778f2d Update net-istio nightly (# 13949)%0A  > f27ba4e Update net-certmanager nightly (# 13944)%0A  > 2840301 Update net-kourier nightly (# 13945)%0A  > 117a642 Update net-gateway-api nightly (# 13943)%0A  > 84a2230 Update net-contour nightly (# 13942)%0A  > 7aa5edb upgrade to latest dependencies (# 13941)%0A  > 01707d8 upgrade to latest dependencies (# 13940)%0A  > b7d5e8d Update net-istio nightly (# 13939)%0A  > 5e056a0 Update net-certmanager nightly (# 13926)%0A  > 35efd12 Update net-contour nightly (# 13929)%0A  > f476717 Update net-istio nightly (# 13935)%0A  > bd8e37c Update net-gateway-api nightly (# 13925)%0A  > 37a7010 Update net-kourier nightly (# 13934)%0A  > f47802d Update community files (# 13933)%0A  > 990d701 Update net-kourier nightly (# 13928)%0A  > ff9f03d Update net-istio nightly (# 13927)%0A  > 690c525 upgrade to latest dependencies (# 13924)%0A  > 1dd07a7 Update community files (# 13923)%0A  > 66141b8 Update net-istio nightly (# 13920)%0Abumping github.com/prometheus/client_golang 64435fc...254e546:%0A  > 254e546 Merge pull request # 1162 from kakkoyun/cut-1.14.0%0A  > 07d3a81 Merge pull request # 1161 from prometheus/release-1.13%0A  > c8a3d32 Cut v1.14.0%0A  > 870469e Test and support 1.19 (# 1160)%0A  > 53e51c4 Merge pull request # 1157 from prometheus/cut-1.13.1%0A  > b785d0c Fix go_collector_latest_test Fail on go1.19 (# 1136)%0A  > 79ca0eb Added tip from Björn + Grammarly.%0A  > 4d54769 Fix float64 comparison test failure on archs using FMA (# 1133)%0A  > 078f11f Cut 1.13.1 release (+ documenting release process).%0A  > 5f202ee Merge pull request # 1150 from prometheus/sparsehistogram%0A  > ddd7f0e Fix race condition with Exemplar in Counter (# 1146)%0A  > 0859bb8 Merge pull request # 1152 from jessicalins/update-to-custom-reg%0A  > fffb76c Merge branch 'main' into sparsehistogram%0A  > 1f93f64 Fix `CumulativeCount` value of `+Inf` bucket created from exemplar (# 1148)%0A  > 10b0550 Fix race condition with Exemplar in Counter (# 1146)%0A  > a340ca4 Run make format%0A  > e92a8c7 Avoid the term 'sparse' where possible%0A  > 8cc2b6c Fix double-counting bug in promhttp.InstrumentRoundTripperCounter (# 1118)%0A  > dcea97e Fix `CumulativeCount` value of `+Inf` bucket created from exemplar (# 1148)%0A  > 6056615 Update random example to use custom registry%0A  > d31f13b Add SparseBucketsZeroThresholdZero and groom doc comments%0A  > 9801a4e Examples: Replace deprecated WithGoCollections with WithGoCollectorRuntimeMetrics (# 1130)%0A  > 0b7f488 Update simple example to use custom registry%0A  > 58a8ca4 examples: Adjust doc comment for native histograms%0A  > 7c46c15 Clarify documentation around what constructors do (# 1125)%0A  > 9b5c5b8 Update basic example to use custom registry%0A  > 4e71e6f Update prometheus/client_model dependency%0A  > 83d56b1 Extend prometheus.Registry to implement Collector (# 1103)%0A  > 111fae1 Merge branch 'main' into sparsehistogram%0A  > 4c41dfb Clarify exemplar(Add|Observe) by renaming to (add|observe)WithExemplar (# 1122)%0A  > 25bc188 Merge pull request # 1144 from prometheus/beorn7/histogram2%0A  > f73e3cc Fix double-counting bug in promhttp.InstrumentRoundTripperCounter (# 1118)%0A  > 95cf173 Merge branch 'main' into sparsehistogram%0A  > 6942f9e sparse buckets: Fix handling of +Inf/-Inf/NaN observations%0A  > c7aa2a5 Merge pull request # 1113 from prometheus/release-1.13%0A  > ec86ef1 Merge pull request # 1092 from prometheus/beorn7/histogram%0A  > 1e61b8e Update common Prometheus files (# 1111)%0A  > 6141a07 Merge branch 'main' into sparsehistogram%0A  > 8cbcd40 histograms: Move to new exposition protobuf format%0A  > 5a321c7 Merge branch 'foo-commit' into sparsehistogram%0A  > e93e384 Merge branch 'beorn7/release' into sparsehistogram%0A  > e203144 Merge branch 'release-1.12' of github.com:prometheus/client_golang into release-1.12%0A  > 525d042 Merge branch 'main' into sparsehistogram%0A  > a516626 Merge branch 'release-1.12' into beorn7/release%0A  > a27b6d7 Fix conflicts%0A  > 6ba7871 Merge branch 'main' into sparsehistogram%0A  > eb59a7b Histogram: Fix bug with negative schemas (# 1054)%0A  > b237230 Merge branch 'main' into sparsehistogram%0A  > 294cca4 Merge branch 'main' into sparsehistogram%0A  > 70253f4 Fix typo in doc comment%0A  > 5b19c55 Merge branch 'master' into sparsehistogram%0A  > dfbcc28 Merge pull request # 901 from prometheus/beorn7/histogram%0A  > 84fcaff Merge branch 'master' into sparsehistogram%0A  > 263be8d Refactoring of sparse histograms%0A  > 9ef5f90 Allow a zero threshold of zero%0A  > 2409960 Implement strategy to limit the sparse bucket count%0A  > aa6f67a Add TODO about bucket search optimization%0A  > 43f31c2 Merge pull request # 886 from prometheus/beorn7/histogram%0A  > 5aa8534 Merge branch 'master' into sparsehistogram%0A  > 5142344 Pin client_model to the most recent sparsehistogram commit%0A  > 97eb041 Tidy go.sum%0A  > 6c4e0ef Add tests for sparse histogram%0A  > 553ed73 Fix lint warning%0A  > 31318b7 Switch to base-2 buckets%0A  > b7a540a Fix test%0A  > a9df0ba Update prometheus/client_model%0A  > ce36ee3 Merge branch 'master' into beorn7/histogram%0A  > d698336 Merge branch 'master' into beorn7/histogram%0A  > 08104a0 Minor doc comment fixes%0A  > a9d0066 Add note about pow-of-10 precision issue%0A  > d1f5366 Fix span offset%0A  > abe540f Encode sparse histograms in protobuf%0A  > c98db4e Demo sparse histograms%0Abumping knative.dev/pkg dfad48e...6eb4b40:%0A  > 6eb4b40 Update community files (# 2760)%0A  > eb63a40 Support to set qps and burst via env variable (# 2755)%0A  > 74c4be5 Generate kresource duck type codegen (# 2754)%0A  > 4dbc312 fix boilerplate (# 2753)%0A  > 15605c7 Defaulting Controller options for all kind of webhooks (# 2738)%0A  > 94b81fc Update community files (# 2752)%0A  > 5671699 drop the dynamic type (# 2750)%0A  > 9bda38b Fix some webhook testing tech debt (# 2751)%0A  > ec20442 Update community files (# 2747)%0A  > 05bfcf6 bump k8s dependencies and update min version to v1.25 (# 2745)%0A  > 52ff2ac drop dynamic client wrappers (# 2744)%0A  > a170a07 Eventing TLS: validate that Destination.CACerts is a PEM encoded cert (# 2743)%0A  > dfb4bf0 Drop dynamic wrapper injection code generation (# 2742)%0A  > db8a353 Add SinkCACerts to SourceStatus (# 2733)%0A  > 9049667 Update community files (# 2735)%0A  > aacec7f Update community files (# 2734)%0A  > 300df43 Eventing TLS: Added AddressableFromDestination method on the resolver (# 2717)%0Abumping k8s.io/apimachinery 4fbe8e4...b207ce5:%0A  > b207ce5 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > 917de35 Bump runc go module v1.1.4 -> v1.1.6%0A  > 53ecdf0 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 05339fa Update golang.org/x/net to v0.7.0%0A  > eabbfd5 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 48b8d1f Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 373a5f7 Merge pull request # 114521 from 3point2/automated-cherry-pick-of-# 113283-upstream-release-1.26%0A  > b5e5df6 Fix SPDY proxy authentication with special chars%0A  > 553a2d6 Improve error message when proxy connection fails%0A  > 5d4cdd2 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > 6cbc4a3 Update golang.org/x/net 1e63c2f%0A  > 6561235 Merge pull request # 113699 from liggitt/manjusaka/fix-107415%0A  > dad8cd8 Update workload selector validation%0A  > fe82462 Add extra value validation for matchExpression field in LabelSelector%0A  > 067949d update k8s.io/utils to fix util tracing panic%0A  > 0ceff90 Merge pull request # 112223 from astraw99/fix-ownerRef-validate%0A  > 9e85d3a Merge pull request # 112649 from howardjohn/set/optimize-everything-nothing%0A  > b0dd9ec Fix ownerRef controller validate err%0A  > b03a432 Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > 88a1448 Rename and comment on why sharing is safe%0A  > 4e6bcdb dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > 3adc870 Optimize `Everything` and `Nothing` label selectors%0A  > 0524d6c Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > 5a0277f Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > 6809593 Merge pull request # 112377 from weilaaa/refactor_sets_use_generic%0A  > 70a38aa Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > f2d9aed refactor sets use generic%0A  > d097f82 dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > 7b5633b Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > b839e82 Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > b7d8973 update kube-openapi%0A  > 1dc6ace update fsnotify to v1.6.0%0A  > 78d003c Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 04898ff Bump golang.org/x/text to v0.3.8%0A  > 79993b2 Merge pull request # 112875 from pohly/update-yaml%0A  > 7379c15 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 66e26ac Merge pull request # 112707 from enj/enj/i/https_links%0A  > 882b67d Use https links for k8s KEPs, issues, PRs, etc%0A  > 7fb78ee Merge pull request # 112472 from ialidzhikov/nit/error-msg%0A  > 826a74e Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 22fe889 Improve the error returned from the `LabelSelectorAsSelector` func%0A  > e2f9797 Update to latest k8s.io/utils to pick up changes%0A  > f8159af Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 612703e Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 9901884 updated etcd to v3.5.5 and newer otel libraries as well%0A  > 6439059 Merge pull request # 112526 from liggitt/redirect%0A  > 0564b5e e2e: bump ginkgo to v2.2.0%0A  > 2e3bf73 Limit redirect proxy handling to redirected responses%0A  > 6d854d7 Merge pull request # 112349 from pohly/klog-update%0A  > e1e1b7c build: update to klog v2.80.1%0A  > ed93eed Merge pull request # 111768 from weilaaa/feature_add_symmetric_difference_in_sets_string%0A  > 36163c5 Merge pull request # 112193 from jindijamie/master%0A  > b7b9ba4 add symmetric difference in sets%0A  > 31bc292 Merge pull request # 112199 from pohly/klog-update%0A  > 1c318b6 Add an option for aggregator%0A  > 0d0d03e Merge pull request # 111936 from haoruan/bugfix-111928-microtime-marshal-precision%0A  > 145c075 dependencies: update to klog v2.80.0%0A  > 2d64dac Merge pull request # 112089 from zeze1004/fix-typo%0A  > 2187a78 Marshal MicroTime to json and proto at the same precision%0A  > 53c4d51 Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > 30e9977 Fix typo "sturct" to "struct"%0A  > 5e4f25a dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > 349dcdf Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 16a7f7a Bump prometheus/client_golang to v1.13.0%0A  > 2b9fe2c Merge pull request # 111808 from alvaroaleman/meta-wrapping%0A  > bb48261 Apimachinery meta errors: Support errors.Is and error wrapping%0Abumping knative.dev/eventing 034bec9...f5b1b12:%0A  > f5b1b12 Send namespace header in MT components (# 7048)%0A  > 4b5fde8 [main] Update community files (# 7043)%0A  > 8f74094 Add handler to auto create Event Types (# 7034)%0A  > 901ef61 Remove check for empty Namespace on resolver (# 7040)%0A  > 95cdbaa We should not limit the EventType creation from the Sources Duck to just brokers (# 7032)%0A  > 7429761 Adjust the Namespace reference to the one from the parent (# 7035)%0A  > cb2a891 update the redeployment script (# 7038)%0A  > ab01938 [main] Upgrade to latest dependencies (# 7025)%0A  > c9dcaf3 Added basic gc loop to kncloudevents clients map (# 6997)%0A  > d6cf96d EventType works with channel (# 7023)%0A  > 365d0b0 Run TLS e2e tests only when Istio is not enabled (# 7029)%0A  > 825a237 Update IMC CRD addressstatus to include `.name` and `.CACerts` fields (# 7026)%0A  > 3190df7 Tracking/reconcile KResource references (# 7014)%0A  > 0f68861 Rename more to Resource, instead of broker (# 7022)%0A  > bccb7d4 Better reflecting the lifecycle of event type … (# 7019)%0A  > 49d4acd Skip ping source TLS rekt test, since extremely flaky (# 7016)%0A  > 8719e18 [main] Upgrade to latest dependencies (# 7012)%0A  > e5ae717 Use HTTP POST when terminating istio proxy (# 7015)%0A  > fea730f Only check if the reference does exist (# 7010)%0A  > 631f4ec Add TLS support for mt-broker-filter (# 6940)%0A  > 45f0a19 Allow wathola components to run with Istio  (# 7011)%0A  > 65f4b1c [main] Format Go code (# 7008)%0A  > 3267b1a test SinkBinding with eventshub TLS receiver as sink (# 6979)%0A  > aad53f4 Updated eventingtls test certs to support IP addresses (# 7006)%0A  > 57d78e0 [main] Update community files (# 7004)%0A  > dfb2243 Support TLS in Trigger and Channel reconciler (# 6988)%0A  > df08b49 Eventing TLS: verify APIServerSource and PingSource sinkURI is https (# 6987)%0A  > d21c1aa [main] Upgrade to latest dependencies (# 6989)%0A  > 70113e8 Deprecate broker field and use KReference for the broker instead (# 6870)%0A  > 4e4647f test update to newest version (# 6990)%0A  > 870ac6b Update MessageDispatcher and FanoutMessageHandler to support sending events to TLS endpoints (# 6983)%0A  > 6dd5d58 Test PingSource with eventshub TLS receiver as sink (# 6965)%0A  > 55f4f28 [main] Upgrade to latest dependencies (# 6982)%0A  > 2a5a9a5 Add more items in the development getting started documentation (# 6978)%0A  > 59118a0 imc-dispatcher starts a TLS server, accepts host based routing on http receiver and path based routing on https receiver (# 6954)%0A  > ee49ada Rework kncloudevents library to support multiple clients (# 6975)%0A  > ee88094 Make ServerManager independent from kncloudevents package (# 6980)%0A  > 6a11c5f [main] Upgrade to latest dependencies (# 6969)%0A  > 8a9a532 Updated DEVELOPMENT.md to provide better instructions on setting up kubernetes (# 6977)%0A  > 390a0c8 Eventing TLS: Test ContainerSource with eventshub TLS receiver as sink (# 6957)%0A  > 5e245ac Fix flaky PingSource TLS unit test (# 6970)%0A  > f9f27c9 Use random names in Channel tests (# 6967)%0A  > d4609a5 Do not parse flags in InitializeEventingFlags (# 6966)%0A  > ef68a0a [main] Update community files (# 6968)%0A  > 4adc287 Add transport-encryption prerequisite for Addressable tests (# 6964)%0A  > deb0ef4 Add field for subscribers & replys CA certs to `SubscriberSpec` and `SubscriptionStatusPhysicalSubscription` (# 6959)%0A  > b81082c Eventing TLS: Test ApiServerSource with eventshub TLS receiver as sink (# 6956)%0A  > cdff269 Adding source duck type to v1b2 (# 6962)%0A  > b47b4ec [main] Upgrade to latest dependencies (# 6958)%0A  > 3315c20 Provide Channels CACerts in Brokers status annotation (# 6952)%0A  > 4b9fdef [main] Upgrade to latest dependencies (# 6955)%0A  > da31970 Improve cert-manager resources for Eventing TLS certs provisioning (# 6953)%0A  > fc5befb Provide subscribers CACerts in triggers status (# 6951)%0A  > 1efab19 Using v1b2 in the reconciler (# 6949)%0A  > c44671c Updating rekt test resources for EventType v1b2 (# 6946)%0A  > e31eb1f Adding testingv1b2 for eventtype (# 6944)%0A  > a9908ef Support TLS in PingSource (# 6929)%0A  > df559c0 Fix typo in flags.IsDisbledTransportEncryption name (# 6941)%0A  > 7073cc9 [main] Upgrade to latest dependencies (# 6939)%0A  > c6bc9bb Eventing TLS: Support K_CA_CERTS env variable injection for SinkBinding subjects (# 6931)%0A  > 24fbfe5 Eventing TLS: support exposing https address in Broker controller (# 6930)%0A  > d18cb42 Add information about retryable error in servermanager (# 6921)%0A  > f92a05b Added Support for K_CA_CERTS in the heartbeats (# 6920)%0A  > b8b43d0 Remove CA certs empty and non nil check, use URL scheme only (# 6928)%0A  > 3c8cc05 Return error directly if one receiver of servermanager fails (# 6919)%0A  > 92ab7f8 [main] Upgrade to latest dependencies (# 6927)%0A  > 5c6fe57 two more for reducing to debug, instead of info (# 6922)%0A  > 6cf9397 less verbose logs on scheduler component  (# 6912)%0A  > 69918f2 Adds ServerManager. Supports http/https message receivers (# 6908)%0A  > d58e259 Install ko using setup-ko in kind e2e tests (# 6910)%0A  > 9cdea5d Eventing TLS: Added Support for setting K_CA_CERTS in the ApiServerSource controller for the adapter (# 6897)%0A  > add8436 Eventing TLS: support exposing https address in InMemoryChannel controller (# 6881)%0A  > 59cfb6d [main] Upgrade to latest dependencies (# 6906)%0A  > 03f2a3d Remove unused test helper (# 6907)%0A  > 7a90c46 Remove eventing-natss from downstream tests (# 6905)%0A  > ba2550b [main] Upgrade to latest dependencies (# 6904)%0A  > 999eead More EventType v1beta2 work (# 6903)%0A  > 66e8257 Remove sanitize HTTP body for `knativeerrordata` extension (# 6902)%0A  > cd50d27 [main] Format Go code (# 6898)%0A  > 0f0a82c [main] Update community files (# 6901)%0A  > 7f4deb5 EventType v1b2 API addition (# 6893)%0A  > 1f917d0 Refactor PingSource adapter client creation (# 6880)%0A  > e2f1c77 [main] Update community files (# 6896)%0A  > 6a5c7ee Eventing TLS: migrate all resolver.URIResolver usages over to AddressableFromDestinationV1 (# 6883)%0A  > 0a12a6c Adds path based routing to message_receiver pkg (# 6873)%0Abumping knative.dev/networking e5d04e8...b9dd5c2:%0A  > b9dd5c2 upgrade to latest dependencies (# 816)%0A  > 68947c5 upgrade to latest dependencies (# 815)%0A  > 14a2bd4 Move `pkg/certificates` from `control-protocol` to `networking` (# 802)%0A  > 2daa483 Update community files (# 813)%0A  > 0dbe4f9 upgrade to latest dependencies (# 812)%0A  > 2a2f7d2 upgrade to latest dependencies (# 810)%0A  > fcbedad Update community files (# 809)%0A  > a44b093 upgrade to latest dependencies (# 808)%0A  > 7c2f7ac upgrade to latest dependencies (# 807)%0A  > 33636d9 Backward compatibility for InternalEncryption (# 806)%0A  > 77975a1 Add the new certificate names for dataplane and controlplane (# 804)%0A  > c3cca43 upgrade to latest dependencies (# 803)%0A  > 3f4627e Add internal trust flag to config (# 778)%0A  > 02055c8 Update community files (# 801)%0A  > 68725bd upgrade to latest dependencies (# 798)%0A  > 1594abb Update community files (# 797)%0Abumping github.com/matttproud/golang_protobuf_extensions c182aff...c182aff:%0Abumping github.com/prometheus/client_model 7bc5445...63fb982:%0A  > 63fb982 Merge pull request # 63 from prometheus/sparsehistogram%0A  > 5c16fa2 Merge pull request # 57 from prometheus/repo_sync%0A  > fdb567d Add note about native histograms to README%0A  > 6b8c742 Update common Prometheus files%0A  > 942d53c Update common Prometheus files%0A  > 7f720d2 Add note about experimental state of native histograms%0A  > f60d1ac Update common Prometheus files%0A  > 1f8dcad Merge pull request # 59 from prometheus/beorn7/histogram%0A  > 6dc836e Merge pull request # 53 from prometheus/repo_sync%0A  > 421ad2b Merge pull request # 58 from prometheus/beorn7/histogram%0A  > a7ff713 Flatten the buckets of native histograms%0A  > 0e1ed89 Merge pull request # 52 from prometheus/repo_sync%0A  > a227486 Update common Prometheus files%0A  > 408689d Merge branch 'master' into sparsehistogram%0A  > 0da3265 Explain Span layout better%0A  > 14ab895 Merge pull request # 51 from prometheus/repo_sync%0A  > bc75c6a Update common Prometheus files%0A  > 61b6c1a Merge pull request # 47 from prometheus/beorn7/histogram%0A  > 8171e83 Add float histograms and gauge histograms to proto spec%0A  > a863571 Merge pull request # 49 from prometheus/repo_sync%0A  > 2fc368c Update common Prometheus files%0A  > 8831f0d Merge branch 'master' into sparsehistogram%0A  > bbaf1cc Switch to base 2 and powers of 2 for resolution%0A  > 675c4e5 Merge pull request # 48 from prometheus/repo_sync%0A  > a3e6551 Update common Prometheus files%0A  > 24db95a Merge remote-tracking branch 'origin/master' into beorn7/histogram%0A  > 147c58e Move .proto file and add caching of protoc and protoc-gen-go during build (# 46)%0A  > 56ab8d9 Update common Prometheus files%0A  > 4b803f3 Experimental encoding for sparse buckets in histogram%0A  > 0255a22 Merge pull request # 43 from roidelapluie/security-dot-md%0A  > 1f48c5c Rename metrics.proto to io_prometheus_client_metrics.proto (# 45)%0A  > 60555c9 Merge pull request # 41 from prometheus/repo_sync%0A  > 1bb3080 Add SECURITY.md%0A  > 1106810 Update common Prometheus files%0Abumping golang.org/x/sys 90c8f94...c7a1bf9:%0A  > c7a1bf9 unix: define PerfBitWriteBackward%0A  > 1470852 unix: add SetsockoptTCPMD5Sig on linux%0A  > a6bfb89 unix: use unsafe.Slice in anyToSockaddr%0A  > c10701f windows: use unsafe.Slice in (*RawSockaddrAny).Sockaddr on windows%0A  > 6f25076 unix: define extended TCPInfo on Linux%0A  > 10499f4 unix: add ioctlPtr with unsafe.Pointer arg on other unices (cont)%0A  > 92c4c39 unix: add Dup3 on FreeBSD%0A  > 748af6e unix: pass PROT_MPROTECT(PROT_READ|PROT_WRITE) to initial Mmap on netbsd%0A  > 972870e unix/linux: update to Linux kernel 6.2, glibc 2.37 and Go 1.20.1%0A  > cc0b67d unix: use C.ioctl in generated ioctlPtr%0A  > a3b23cc unix: use SYS_PTRACE in generated ptracePtr%0A  > 71a906e unix/linux: add TUN flags and virtio_net_hdr constants%0A  > 2977c77 unix: add ptracePtr that accepts pointer arg as unsafe.Pointer%0A  > 6877dcc execabs: don't override Go 1.19 error with our error%0A  > b13f40e unix: add ioctlPtr with unsafe.Pointer arg on other unices%0A  > 3b9b58b unix: Faccess: check CAP_DAC_OVERRIDE on Linux%0A  > 2da1413 cpu: get hwcap/auxv from the Go 1.21+ runtime%0A  > 4fee21c windows: Add WSALookupService syscall wrappers%0A  > c79a742 unix: fix a use-after-free bug in PtraceIO on freebsd

Signed-off-by: Knative Automation <automation@knative.team>

---
## [TheNeoGamer42/Skyrat-tg](https://github.com/TheNeoGamer42/Skyrat-tg)@[54011a20b9...](https://github.com/TheNeoGamer42/Skyrat-tg/commit/54011a20b903317639fdefb82fa11ad1c03eb710)
#### Monday 2023-07-03 02:46:19 by SkyratBot

[MIRROR] Replaces the syndicate corpse Legions can drop with one without a MODSuit [MDB IGNORE] (#21517)

* Replaces the syndicate corpse Legions can drop with one without a MODSuit (#75700)

## About The Pull Request
This is part of a pass I'm working on doing where I go through and
remove instances of antag gear outside of their normal context. This is
mostly going to involve replacing space/Lavaland ruin gear with
something close to the same power level but not distinctly something
only antags should be able to get. I want to keep ruins rewarding but I
don't want explicit antag gear to be something you can obtain without
needing an uplink.

The first part of this is me removing the MODSuit from the syndicate
operative corpse. The new one drops a turtleneck, a syndicate gas mask,
and gripper gloves.

## Why It's Good For The Game
It's my opinion that antag gear should probably stay in antag hands
unless you manage to kill one or steal an uplink. The main impetus for
this was a discussion I had a while back about how blood red hardsuits
used to _just_ be an antag thing. I kind of miss that general feeling of
paranoia that came from seeing someone wearing it, as opposed to seeing
it these days and just thinking "Yeah, it's probably someone who got it
from space".

In this specific instance, Syndicate MODSuits are pretty strong anyway
and, regardless of the low odds of getting one, I really don't think it
should be available as loot off a fairly easy-to-kill mob.

## Changelog
:cl:
balance: Syndicate corpses dropped from killing a Legion no longer come
with a MODSuit.
/:cl:

* Replaces the syndicate corpse Legions can drop with one without a MODSuit

---------

Co-authored-by: TheVekter <TheVekter@users.noreply.github.com>

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[18819cc7fb...](https://github.com/shiptest-ss13/Shiptest/commit/18819cc7fb78eb4eaf11691e4a07b1294b76358a)
#### Monday 2023-07-03 03:09:14 by zevo

Minor changes to the Syndicate Battle Sphere ruin (#2045)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Various fixes for provinggrounds.dmm, mainly the server room and SMES.
Server room is no longer filled with black box recorders, but salvagable
servers. There is now one singular black box recorder in the center
where a black box on a table was. The SMES now should actually charge
the ruin. Tossed a medkit in one of the halls for players to use while
clearing the ruin. Replaced about half of the syndicate researcher mobs
with syndicate operatives who will actually fight the players. Rotated
an airlock missed in the map updates for anywalls.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
boy, i sure love functional ruins! also players should not have 25 of a
very rare potential quest item. The ruin can stay as it is otherwise,
because it provides a fun challenge for superbly well armed players (or
a rugged explorer with nothing but a lazer gun and a dream) with a
fitting reward at the end of a mounted LMG.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
fix: Syndicate Battle Dome (provinggrounds.dmm) should now have a
functional SMES and airlocks/blast doors.
fix: Syndicate Battle Dome (provinggrounds.dmm) no longer has ~20 black
box recorders and now only has one.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [MarkSuckerberg/Shiptest](https://github.com/MarkSuckerberg/Shiptest)@[d21740b475...](https://github.com/MarkSuckerberg/Shiptest/commit/d21740b475aea65de3b250a5aea26a69677e30e8)
#### Monday 2023-07-03 03:19:40 by tmtmtl30

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
## [tommyettinger/libgdx](https://github.com/tommyettinger/libgdx)@[e1d1fdc5fb...](https://github.com/tommyettinger/libgdx/commit/e1d1fdc5fb5b8409dc74f638c633ead405e535f3)
#### Monday 2023-07-03 03:48:01 by Tommy Ettinger

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
## [Joseph11024/PkmEmpire-ForkBot.NET](https://github.com/Joseph11024/PkmEmpire-ForkBot.NET)@[6eaa4d5ecd...](https://github.com/Joseph11024/PkmEmpire-ForkBot.NET/commit/6eaa4d5ecd44bafc60156e6cfbb39807f4fa388b)
#### Monday 2023-07-03 05:11:59 by Koi

Mr. Mime is a thing, unfortunately.
Mild clean, some more Cherish set handling attempts.
Exclude set MetDate from mystery gifts.
Fix daycare enum parsing.
Check for no result in case $qc was used or some other weird thing happens.
Remove FixOT and TradeCord as routine types (FlexTrade handles both).
Try to apply trainer info for Mystery gifts.
Re-add fixed met date if not GO origin.
Update DenBot distribution data, minor fixes.
Fix Yamask-Galar in daycare, some more oopsies.
-Add DenBot - a seed lookup and day skipper bot for raids.
-Change AutoRoll's behavior to make use of some of DenBot's functionality.
Minor clean.
Revise TradeCord "traded" check, remove potential user path straggler entries because paranoia, some minor fixes.
TradeCord fixes (shocker, I know).
Extract Json serializer.
Minor clean and fixes.
Minor fixes.
Fix Milcery when an Alcremie variant is a parent.
Update to latest Core and ALM dependencies.
Handle non-shiny events in a better way.
Work around a race condition?
Simplify and de-bugify trade completion check.
Fix indexing, improve chance for Melmetal-Gmax because it's nigh impossible to get.
Rework TradeCord internals, add new functionality:
-Migrate user data from ".txt" files to a serialized Json (migration for a large amount of users will take a few minutes, be patient).
-Make TradeCord configurable, add its own settings category.
-Add some template events with an optional end timer (YYYY/MM/DD 8PM as an example, though any local time format should work).
-Add barebones Pokedex (counter, flavor text).
-Can check dex completion by typing `$dex`, check missing entries by typing `$dex missing`.
-Completing the Pokedex will slightly improve shiny rate.
-Can now mass release cherish event Pokemon and shinies ($massrelease shiny/cherish).
-Various tweaks, improvements, and bugfixes.

Slightly change FixOT's behavior:
-If a shown Pokemon is illegal and an event, attempt to find a match within the MGDB first.
-Try to force users to trade away the shown Pokemon, log attempt to change shown Pokemon.
Add consideration for easter eggs being enabled in settings, fix Suicune
Change species rng for TradeCord, some bugfixes (I really need to rewrite this mess)
Add check if we're using ListUtil for Giveaway instead of TradeCord.
Amend commit since I'm squashing and force-pushing while bringing the fork in line with the main branch
Add Giveaway module to Discord bot (#22)

Thanks, rigrassm.
Co-authored-by: Koi-3088 <61223145+Koi-3088@users.noreply.github.com>
Specify USB port instead of adding the first result (can be found via Device Manager).
Re-add boolean check because we don't want to fix everything
FixOT will attempt to regenerate illegal Pokémon.
Apply trash bytes for reasons.
Minor TradeCord fixes and adjustments.
Minor clean for C#9
Use "GetValidPreEvolutions()" instead of "GetPreEvolutions()".
Index forms correctly.
Fix the fixed and re-introduced empty daycare index error.
*an* Ultra Ball.
Add EvoTree breeding for TradeCord.
Remove unnecessary value declarations for pinging on encounter match.
Mildly beautify EncounterBot mark output.
Integrate Anubis' system update prevention into Soft Reset and Regigigas Encounter Modes.
Rename "Regi" Encounter Mode to "Soft Reset".
Speed up "A" clicks for Regigigas and Soft Reset modes.
Add Mark logging output for EncounterBot.
Fix oops (re-order logic, remove unnecessary lines).
Add optional species and form specification for $massrelease
Use an obscure string splitter because people like symbols in their names.
Fix things that broke after rebasing to the latest main repo commit.
Use a less unfortunate field name and value splitter...again.
Fix Marowak-Alola always generating as an NPC trade.
Add filters for "$list <species>" to narrow down results.
Fix Cherish Pichu and Octillery
Stop making dumb mistakes, me (implying the rest of it isn't a dumb mistake).
Can't breed antiques.
Use a less unfortunate embed name and value splitter
Add Melmetal-Gmax to TradeCord.
Add ability to search by caught ball.
Have MassRelease ignore events.
Add specific regional form breeding.
Revise egg rate and egg shiny chance.
Have trade evolutions hold an Everstone.
Add an extra right click when navigating to settings for AutoRoll.
Add reworked encounter/egg/fossil logs.
Minor clean.
Minor clean.
Get rid of EncounterBot, FossilBot, EggFetch text logs until I properly rework them.
Break on an empty page due to aggressive rounding
Add multi-page lists for Tradecord.
More random bugfixes.
Fix some bugs before major clean
Add Language parameter for TradeCord.
Change trainer info input format for TradeCord.
Move focus on Showdown set instead of randomizing a pkm file.
Allow user to enter whatever they want for $list, handle edge cases like Kommo-o
Add "$list all" to show non-duplicate caught species.
Automatically remove from favorites if trading or gifting (small QOL thing).
Change how favorites are removed from user file.
Revert base egg shiny chance nerf.
Fix daycare
Add favorites command to TradeCord.
Slightly nerf eggs.
Fix TradeCord list for shinies
Add TradeCord (my dumbest and messiest project so far, Archit pls don't hate the mess).
Add Showdown output for Star/Square shinies and OTGender.
Add optional link code input for FixOT.
Change how OTName, TID, SID is displayed.
Add Regigigas SR bot.
Add SoJ Camp SR bot.
Ribbons now work with EggTrade (remove ribbons if egg).
Remove EggRoll.
Add another filter for FixOT
Fix.. FixOT
Update offsets for EncounterBot catching.
Slightly change StrongSpawn to work with Regi SR and make it its own mode.
Make SpinTrade only available for USB-Botbase
Update valid eggs for CT
winforms: resize icon.ico to fix crash at startup on unix using mono
Rework Spin, read initial in-game coordinates in order to correct drift
Add TID, SID, Language output for Showdown
Remove obsolete OT and Language parsing
Very minor clean until I have time for a proper one.
Detach controller when stopping USB bot.
Actually set LastUsedBall for EncounterBot (missed when bringing in line with main repo)
Move extra RaidBot timings following the official commit
Remove PKHeX Discord invite from Readme.md

Maybe fewer people will pester devs now about my unofficial fork?
Update for latest main repo EncounterBot commits.
Update README.md
Add back best commit: Red's SpinTrade.
Add egg trades, foreign Dittos and OT for Twitch.
If ItemMule is enabled, also display the item a user is receiving.
Add periodic time sync toggle for all methods of hosting (except for non-soft locked AutoRoll) to (hopefully) prevent den rollover during extended hosts.

Add routine to exit a lobby for SoftLock if no players are ready in time (to preserve soft lock).

Add a routine to recover from disbanded lobbies (when someone disconnects unexpectedly) for SoftLock.

Add a routine to restart game if all else fails and we're stuck in a raid.

Add a routine for adding and deleting friends if we're soft locked and raids go empty.

Slightly reorganize settings, extract methods, minor clean.
Don't use such a generic file name for stream assets.
Check USB port index for running bots. Should fix adding additional USB bots when no config is saved.
Add fixed met date for FixOT.
How do I boolean
Change airplane mode logic, tweak timings and routine for soft lock lobby exit
Rework EggRoll cooldown (static list in favor of a txt file).
Start clean up and refactor
Add setting to increase delay after pressing "Home" after a date skip.
Use USB port index for blocking and sprite pngs if connection type is USB
Add option for airplane host (usb-botbase required)
Add option to softlock on selected species for AutoRoll
Add automatic compatibility for all console languages when date skipping (have to set ConsoleLanguage under ScreenDetection)
Attempt to fix multiple USB device add and connect...again
Minor clean
Fix oops?
Handle add/remove of bots
Distinguish between multiple USB devices, tweak BotRemoteControl for USB, other various fixes
Add SpA modifier for foreign Dittos
Add alpha USB-Botbase support
Fix DateTime parsing for European format for EggRoll
Set fixed EggMetDate and MetDate for EggRoll
More FixOT filters
Remove Beheeyem. Oops.
Split EggRoll into its own routine and trade type, only output "Receiving: Mysterious Egg" if routine is EggRoll, other minor tweaks and fixes
Make FixOT its own queue with roles and counts
Add a couple more OTs to $fix
Parsing for EggRaffle auto-clear and $clearcooldown
Adjust timings and split Watt collecting clicks for AutoRoll
Fix oops with file attachments for Ditto
Further improvements for OT, memes for invalid pokemon (disable EasterEggs)
Add spaces, digits for OT
Randomize memes, cut down bloat
Fix miscellaneous bots after Anubis' recent QOL additions
-Ignore events for OT because headache.
-Add overlooked "$convert <generation>" input for OT.
-Move $clearcooldown to SudoModule
-Clear timer automatically if NoTrainerFound
-More reliable Dittos
-Foreign Dittos for $convert
-Command to clear cooldown for EggRaffle in case trade gets disconnected
-Fix "Trade finished" line to keep result secret
-EggRaffle as a toggle, option to specify channels
-Seed Check output to both DMs and Channel (apparently some want it)
-Randomly generated egg raffle via a "$roll" command with a configurable cooldown
-FixAdOT reworked, has its own command "$fix" and no longer overrides $clone
-Ball: <value> output for Showdown sets
-Fix oversight
-Option to output Seed Check results to Discord channel with a User mention
-Showdown set output for OT name and eggs
-Basic "OT: <name>" option without Showdown set output
-Initial $convert support for EggTrade
-Egg moves for EggTrade test attempt
-Minor update
-EggTrade (by nicknaming a Pokémon "Egg" using $trade)
-Failsafe for memes if enabled but field left blank or incomplete
-Niche breedable Ditto trade mode.
Add minimize button
EggFetch text logs
StrongSpawn mode for EncounterBot
Re-add EncounterBot Master Ball catching
More parsing for FixAdOTs
Park Ball as held item instead of string
Actually remove the offset instead of saying I did
Initial DLC commit
Faster code entry
Removed catching for EncounterBot (need a new offset)
CloneBot mode to fix Nickname and OT if adverts detected

---
## [driver1998/git](https://github.com/driver1998/git)@[11e5c1a6c9...](https://github.com/driver1998/git/commit/11e5c1a6c925ccf4e80032eddd9844cdb570ed6a)
#### Monday 2023-07-03 05:16:37 by Johannes Schindelin

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
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[a8e16030f8...](https://github.com/san7890/bruhstation/commit/a8e16030f83911aef695ba9f28d565c41c99c3e6)
#### Monday 2023-07-03 05:43:34 by LemonInTheDark

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
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[5c032cc098...](https://github.com/san7890/bruhstation/commit/5c032cc098f9a1d62f9f9dee133ae7c3e4489dca)
#### Monday 2023-07-03 05:43:34 by LemonInTheDark

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
## [rust-lang/miri](https://github.com/rust-lang/miri)@[f72364e727...](https://github.com/rust-lang/miri/commit/f72364e727b27ba9df484166e49fa4f328944e78)
#### Monday 2023-07-03 06:37:08 by bors

Auto merge of #113108 - compiler-errors:normalize-opaques-with-late-bound-vars-again, r=jackh726

Normalize opaques with late-bound vars again

We have a hack in the compiler where if an opaque has escaping late-bound vars, we skip revealing it even though we *could* reveal it from a technical perspective. First of all, this is weird, since we really should be revealing all opaques in `Reveal::All` mode. Second of all, it causes subtle bugs (linked below).

I attempted to fix this in #100980, which was unfortunately reverted due to perf regressions on codebases that used really deeply nested futures in some interesting ways. The worst of which was #103423, which caused the project to hang on build. Another one was #104842, which was just a slow-down, but not a hang. I took some time afterwards to investigate how to rework `normalize_erasing_regions` to take advantage of better caching, but that effort kinda fizzled out (#104133).

However, recently, I was made aware of more bugs whose root cause is not revealing opaques during codegen. That made me want to fix this again -- in the process, interestingly, I took the the minimized example from https://github.com/rust-lang/rust/issues/103423#issuecomment-1292947043, and it doesn't seem to hang any more...

Thinking about this harder, there have been some changes to the way we lower and typecheck async futures that may have reduced the pathologically large number of outlives obligations (see description of #103423) that we were encountering when normalizing opaques with bound vars the last time around:
* #104321 (lower `async { .. }` directly as a generator that implements `Future`, removing the `from_generator` shim)
* #104833 (removing an `identity_future` fn that was wrapping desugared future generators)

... so given that I can see:
* No significant regression on rust perf bot (https://github.com/rust-lang/rust/pull/107620#issuecomment-1600070317)
* No timeouts in crater run I did (https://github.com/rust-lang/rust/pull/107620#issuecomment-1605428952, rechecked failing crates in https://github.com/rust-lang/rust/pull/107620#issuecomment-1605973434)

... and given that this PR:
* Fixes #104601
* Fixes #107557
* Fixes #109464
* Allows us to remove a `DefiningAnchor::Bubble` from codegen (75a8f681837c70051e0200a14f58ae07dbe58e66)

I'm inclined to give this another shot at landing this. Best case, it just works -- worst case, we get more examples to study how we need to improve the compiler to make this work.

r? types

---
## [hoshotakamoto/banzukesurfing](https://github.com/hoshotakamoto/banzukesurfing)@[05063a9363...](https://github.com/hoshotakamoto/banzukesurfing/commit/05063a936341a3c3de35d2e53dbe8bd2827b5f6d)
#### Monday 2023-07-03 06:47:05 by hoshotakamoto

Unit Test Setup: jest (#3)

https://chat.openai.com/share/eb107b81-4e26-48fc-a4fb-d2c1e315bae1

I have these files (below) but I can't run the unit test. Set up the
files I need to run the unit test.

```
index.html
<!DOCTYPE html>
<html>
<head>
    <title>Banzuke Surfing Game</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <!-- Link to the external CSS file -->
    <!-- Uncomment this if you have styles to include -->
    <!-- <link rel="stylesheet" href="styles.css"> -->
</head>
<body>
    <h1>Welcome to Banzuke Surfing Game!</h1>
    <p>Select your Rikishi and start playing!</p>
    <select id="rikishi">
        <option value="1">Rikishi 1</option>
        <option value="2">Rikishi 2</option>
        <!-- more options here -->
    </select>
    <button onclick="startPlaying()">Start Playing</button>
    <!-- Link to the external JavaScript file -->
    <script src="game.js"></script>
</body>
</html>

game.js
function startPlaying() {
    var rikishi = $('#rikishi').val();
    // This is where you'd connect to your game logic
    // For example:
    // sendRikishiToServer(rikishi);
    alert("You selected: " + rikishi);
}

game.test.js
const { startPlaying } = require('./game');

test('check if startPlaying is defined', () => {
  expect(startPlaying).toBeDefined();
});
```

ChatGPT
To run unit tests, you can use a testing library like Jest, a JavaScript
Testing Framework. It allows you to create, run and structure tests.

Here are the steps to set up Jest:

Firstly, initialize a Node.js project by creating a package.json. You
can do this by running the command npm init -y in your project root
directory. This will automatically create a package.json file with
default values.

Then, you need to install Jest. You can install it using the npm package
manager with the following command: npm install --save-dev jest.

Your package.json should then look like this:

```json
{
  "name": "banzuke-surfing-game",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "jest"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "jest": "^27.0.6"
  }
}
```

Next, update your game.js file to make it module-friendly (so that it
can be imported in other js files). You can do this by modifying it as
shown below:

```javascript
function startPlaying() {
    var rikishi = $('#rikishi').val();
    alert("You selected: " + rikishi);
}

// Add this line to make this function accessible in other js files
module.exports = { startPlaying };
```

Your game.test.js file seems fine, it will import the startPlaying
function and checks if it's defined.

Finally, run the test by using the following command: npm run test.

However, since you're using jQuery in the code, you might face issues
with the Jest environment because it doesn't have access to the DOM. In
that case, you would need to use something like jsdom (a JavaScript
based headless browser that can create a realistic testing environment)
and mock the jQuery syntax.

Here is a simple example of how you could test your startPlaying
function:

```javascript
global.$ = jest.fn(() => ({
    val: jest.fn(() => '1')
}));

const { startPlaying } = require('./game');

test('check if startPlaying is defined and returns expected value', () => {
    const result = startPlaying();
    expect(result).toBe("You selected: 1");
});
```

This code creates a mock for jQuery and then calls startPlaying. It then
checks if the function is working as expected and returns the correct
result.

Remember to install jest and jsdom in your project using npm:

```shell
npm install --save-dev jest jsdom
```

Please note that running a front-end unit test without a browser context
can be tricky, and the given mock example is a simplification of the
reality. In a more complex scenario, you would probably use tools such
as Jest with additional libraries (like Enzyme or Testing Library) that
help handle React components, virtual DOM and many other things to
provide a more complete testing environment.


```
npm test

> banzukesurfing@1.0.0 test
> jest

 FAIL  ./game.test.js
  ✕ check if startPlaying is defined and returns expected value

  ● check if startPlaying is defined and returns expected value

    ReferenceError: alert is not defined

      4 |     // For example:
      5 |     // sendRikishiToServer(rikishi);
    > 6 |     alert("You selected: " + rikishi);
        |     ^
      7 | }
      8 |
      9 | module.exports = { startPlaying };

      at alert (game.js:6:5)
      at Object.startPlaying (game.test.js:8:20)

Test Suites: 1 failed, 1 total
Tests:       1 failed, 1 total
Snapshots:   0 total
Time:        0.189 s
Ran all test suites.

```
ChatGPT
The error "ReferenceError: alert is not defined" happens because the
alert function is part of the window object in a browser environment.
When running Jest, it uses a Node.js environment, which does not have a
window object or any of its methods (like alert).

In a test environment, it's best to avoid using these kinds of functions
that rely on the browser. But if you absolutely need to use something
like alert, you can mock it out for testing. However, a better approach
might be to refactor your code to not rely on such methods.

Let's refactor your code to return the string message instead of
alerting it, which will allow us to test the result.

Here's your updated game.js:

```javascript
function startPlaying() {
    var rikishi = $('#rikishi').val();
    var message = "You selected: " + rikishi;
    return message;
}

module.exports = { startPlaying };
```

And the test file game.test.js would look like this:

```javascript
global.$ = jest.fn(() => ({
    val: jest.fn(() => '1')
}));

const { startPlaying } = require('./game');

test('check if startPlaying is defined and returns expected value', () => {
    const result = startPlaying();
    expect(result).toBe("You selected: 1");
});
```

Now when you run npm run test, Jest will call the function startPlaying
and compare the return value with the expected string "You selected: 1".

Please note that such kind of changes where we change our original code
to accommodate testing are not always the best solution. In real
projects, you would want to structure your code in a way that makes it
easy to test and avoid functions that are difficult to test like alert.

---
## [KevinTao24/langchain](https://github.com/KevinTao24/langchain)@[75fb9d2fdc...](https://github.com/KevinTao24/langchain/commit/75fb9d2fdcc201e80ad9c065a02c6cc9ccf6d716)
#### Monday 2023-07-03 07:14:54 by Stefano Lottini

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
## [jinuthomas/openpower-vpd-parser](https://github.com/jinuthomas/openpower-vpd-parser)@[34001376f9...](https://github.com/jinuthomas/openpower-vpd-parser/commit/34001376f96124d579d6d5daabba13c68b72d4b3)
#### Monday 2023-07-03 07:29:32 by jinuthomas

Catching File Exceptions in openpower-vpd-parser

In this commit, I have added code to handle file exceptions
more effectively. By implementing proper exception handling,
we can improve the robustness and reliability of the file
operations within our codebase.

Here are the key changes made in this commit:

 - Introduced a try-catch block around the file operations sections.
 - Within the try block, added code to perform the necessary file
   operations.
 - Implemented catch blocks to handle specific file exceptions.
 - In each catch block, included appropriate error handling logic,
   such as logging the error message or displaying a user-friendly
   error message.
 - Ensured that the catch blocks gracefully handle the exceptions
   and prevent the program from crashing or behaving unexpectedly.

By adding this exception handling code, we can anticipate and handle
potential file-related errors gracefully, providing a smoother
experience for users and preventing any unexpected crashes or data
loss. This would also aid in debugging issues.

Signed-off-by: jinuthomas <jinu.joy.thomas@in.ibm.com>

---
## [The-New-Platinum-Team/PlatinumQuest-Dev](https://github.com/The-New-Platinum-Team/PlatinumQuest-Dev)@[eece70a07a...](https://github.com/The-New-Platinum-Team/PlatinumQuest-Dev/commit/eece70a07a5ae9623eb94ecfccf8abf997180a3f)
#### Monday 2023-07-03 07:50:51 by TheGreatAutismo

Updated "Side Entrance" (Custom Co-op Level)

Added set music, a preview, and a jank ass camera path (do NOT look at that shit in the level editor! you will DIE! (mostly just the numbers being out of order both in the list of objects and the actual camera path itself))

---
## [aspiers/melpa](https://github.com/aspiers/melpa)@[570bde6b4b...](https://github.com/aspiers/melpa/commit/570bde6b4b89eb74eaf47dda64004cd575f9d953)
#### Monday 2023-07-03 08:45:34 by Jonas Bernoulli

Cosmetic changes to numerous recipes

This commit only touches recipes whose `:files' property contains an
`:exclude' element, because I had to look at all those recipes for an
only marginally related reason.

To an extend these changes only reflect my own personal preference, so
I will explain the types of changes I have made.  This should serve as
a starting point for a future discussion in case we want to encourage
a certain style or even enforce it.

- Lines should be intended as `indent-for-tab-command' would, except
  in special-cases such as in the recipe of `use-package', which is
  also a macro with special indentation rules; we override those
  because the `use-package' in use-package's recipe is not that macro,
  it is just a symbol appearing as the first element of a data list.

- I prefer it if there is a newline between the package symbol (the
  car) and the plist that follows, but usually only add it to existing
  recipes when lines would otherwise get to long.  I also do not
  change this if I am not making any other changes that affect more
  than one line.

- Either the complete list should be on a single line or each line
  should contain only one key/value pair.  The first pair may share a
  line with the package symbol (see previous point).  If the recipe
  needs more than one line, then two key/value pairs should never
  appear on one line.  Newline characters are cheap enough these days.

- `:fetcher' should come before `:url' or `:repo', not least because
  the former dictates which of the latter two is required/valid.  You
  can also think of the fetcher as the type or class of the recipe,
  which IMO should come first, like in code: (git-fetcher :url val).

- The most common keywords should be specified in this order:
  `:fetcher', `:url'/`:repo', `:files'.  Other keywords should go
  either before or after `:files' (but preferable not on both sides
  of that for any given recipe).

- A common value of `:files' is: (:defaults (:exclude "...")).
  This could be split across multiple lines, but writing everything
  on one line makes it easier to read it as 'use the defaults, except
  exclude "..."':

    :files (:defaults (:exclude "..."))

- If the value of `:files' is too long for one line, then place
  newlines "semantically", instead of trying to "save space".  For
  example any element that is a list should appear on its own line.
  Two sibling lists should never appear on the same line.  String
  siblings should also not appear on one line in many cases, though
  it might makes sense (but isn't my preference) to group them by
  "type" as in:

    (:defaults
     "foo/*.el" "bar/*.el"
     "docs/foo/*.texi" "docs/bar/*.texi"
     (:exclude "..."))

- While there may be multiple (:exclude ...) elements, I've merged
  them into one.  Mostly for future proofing.

- The position of `:exclude' elements in `:files' value is significant
  in theory.  However in most cases it already appears at the very end
  and I have moved it there in cases where the order is not
  significant.  Mostly for future proofing.

---
## [jinuthomas/openpower-vpd-parser](https://github.com/jinuthomas/openpower-vpd-parser)@[5fcdebb647...](https://github.com/jinuthomas/openpower-vpd-parser/commit/5fcdebb64736726294d80ea47704a780d4fe4b71)
#### Monday 2023-07-03 09:37:07 by jinuthomas

Catching File Exceptions in openpower-vpd-parser

In this commit, I have added code to handle file exceptions
more effectively. By implementing proper exception handling,
we can improve the robustness and reliability of the file
operations within our codebase.

Here are the key changes made in this commit:

  - Introduced a try-catch block around the file operation sections.
  - Within the try block, added code to perform the necessary file
    operations.
  - Implemented catch blocks to handle specific file exceptions.
  - In each catch block, included appropriate error handling logic,
    such as logging the error message or displaying a user-friendly
    error message.
  - Ensured that the catch blocks gracefully handle the exceptions
    and prevent the program from crashing or behaving unexpectedly.

By adding this exception handling code, we can anticipate and handle
potential file-related errors gracefully, providing a smoother
experience for users and preventing any unexpected crashes or data
loss. This would also aid in debugging issues.

Signed-off-by: jinuthomas <jinu.joy.thomas@in.ibm.com>

---
## [Helg2/tgstation](https://github.com/Helg2/tgstation)@[8c2c72b0ed...](https://github.com/Helg2/tgstation/commit/8c2c72b0ed7a1fad112fc4da8a8b7de7faa5e114)
#### Monday 2023-07-03 10:45:16 by LemonInTheDark

Duiffel Spotfix (#76442)

## About The Pull Request

Gives duffelbags their proper slot count
They inherited this from backpacks, but I sorta just forgot about that

[Creates "levels" of locked objects, uses that to make locked duffels
work](https://github.com/tgstation/tgstation/pull/76442/commits/c613c00f62fa3ff03bb33737d24da9acbf2050e3)

[c613c00](https://github.com/tgstation/tgstation/pull/76442/commits/c613c00f62fa3ff03bb33737d24da9acbf2050e3)

Turns locked into something that holds defines, this makes life a lot
easier.
Requires a lot of boilerplate because of how many uses of these procs
there are and all the passthrough and shit.

Adds a few outfit subtypes to avoid this class of failure in future.

Renames the args in a few but not all touched procs, one thing at a time

Closes #76407
Closes #76430 Had the lock check in the wrong place
Closes #76441 GOD I HATE TK SO MUCH

Wrote half the pr without glasses so if it's weird gimme some grace
yeah?

## Changelog
:cl:
fix: Fixes some fuck with duffelbags, them not holding enough + issues
with spawning gear in them (job shit and all)
/:cl:

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[221e82c364...](https://github.com/necromanceranne/tgstation/commit/221e82c3640c75d99dc2616bf666bd897b4a5be8)
#### Monday 2023-07-03 11:15:02 by ChungusGamer666

[NO GBP] Fixes my fuckups with species livers (#76331)

## About The Pull Request

Fixes https://github.com/tgstation/tgstation/issues/76329
I DID A REAL STUPID MISTAKE WHILE CODING
https://github.com/tgstation/tgstation/pull/76184 I AM SORRY
The signal was sending the fucking human instead of seconds_per_tick

## Why It's Good For The Game

Fixes a BUNCH of liver behavior including plasmamen livers not healing
wounds

## Changelog

:cl:
fix: Plasma will now heal plasmamen properly
/:cl:

---
## [cilium/linux](https://github.com/cilium/linux)@[e72ce0570d...](https://github.com/cilium/linux/commit/e72ce0570da3050baf7b6fea551352ad96470b35)
#### Monday 2023-07-03 12:49:58 by Daniel Borkmann

bpf: Add fd-based tcx multi-prog infra with link support

This work refactors and adds a lightweight extension ("tcx") to the tc BPF
ingress and egress data path side for allowing BPF program management based
on fds via bpf() syscall through the newly added generic multi-prog API.
The main goal behind this work which we also presented at LPC [0] last year
and a recent update at LSF/MM/BPF this year [3] is to support long-awaited
BPF link functionality for tc BPF programs, which allows for a model of safe
ownership and program detachment.

Given the rise in tc BPF users in cloud native environments, this becomes
necessary to avoid hard to debug incidents either through stale leftover
programs or 3rd party applications accidentally stepping on each others toes.
As a recap, a BPF link represents the attachment of a BPF program to a BPF
hook point. The BPF link holds a single reference to keep BPF program alive.
Moreover, hook points do not reference a BPF link, only the application's
fd or pinning does. A BPF link holds meta-data specific to attachment and
implements operations for link creation, (atomic) BPF program update,
detachment and introspection. The motivation for BPF links for tc BPF programs
is multi-fold, for example:

  - From Meta: "It's especially important for applications that are deployed
    fleet-wide and that don't "control" hosts they are deployed to. If such
    application crashes and no one notices and does anything about that, BPF
    program will keep running draining resources or even just, say, dropping
    packets. We at FB had outages due to such permanent BPF attachment
    semantics. With fd-based BPF link we are getting a framework, which allows
    safe, auto-detachable behavior by default, unless application explicitly
    opts in by pinning the BPF link." [1]

  - From Cilium-side the tc BPF programs we attach to host-facing veth devices
    and phys devices build the core datapath for Kubernetes Pods, and they
    implement forwarding, load-balancing, policy, EDT-management, etc, within
    BPF. Currently there is no concept of 'safe' ownership, e.g. we've recently
    experienced hard-to-debug issues in a user's staging environment where
    another Kubernetes application using tc BPF attached to the same prio/handle
    of cls_bpf, accidentally wiping all Cilium-based BPF programs from underneath
    it. The goal is to establish a clear/safe ownership model via links which
    cannot accidentally be overridden. [0,2]

BPF links for tc can co-exist with non-link attachments, and the semantics are
in line also with XDP links: BPF links cannot replace other BPF links, BPF
links cannot replace non-BPF links, non-BPF links cannot replace BPF links and
lastly only non-BPF links can replace non-BPF links. In case of Cilium, this
would solve mentioned issue of safe ownership model as 3rd party applications
would not be able to accidentally wipe Cilium programs, even if they are not
BPF link aware.

Earlier attempts [4] have tried to integrate BPF links into core tc machinery
to solve cls_bpf, which has been intrusive to the generic tc kernel API with
extensions only specific to cls_bpf and suboptimal/complex since cls_bpf could
be wiped from the qdisc also. Locking a tc BPF program in place this way, is
getting into layering hacks given the two object models are vastly different.

We instead implemented the tcx (tc 'express') layer which is an fd-based tc BPF
attach API, so that the BPF link implementation blends in naturally similar to
other link types which are fd-based and without the need for changing core tc
internal APIs. BPF programs for tc can then be successively migrated from classic
cls_bpf to the new tc BPF link without needing to change the program's source
code, just the BPF loader mechanics for attaching is sufficient.

For the current tc framework, there is no change in behavior with this change
and neither does this change touch on tc core kernel APIs. The gist of this
patch is that the ingress and egress hook have a lightweight, qdisc-less
extension for BPF to attach its tc BPF programs, in other words, a minimal
entry point for tc BPF. The name tcx has been suggested from discussion of
earlier revisions of this work as a good fit, and to more easily differ between
the classic cls_bpf attachment and the fd-based one.

For the ingress and egress tcx points, the device holds a cache-friendly array
with program pointers which is separated from control plane (slow-path) data.
Earlier versions of this work used priority to determine ordering and expression
of dependencies similar as with classic tc, but it was challenged that for
something more future-proof a better user experience is required. Hence this
resulted in the design and development of the generic attach/detach/query API
for multi-progs. See prior patch with its discussion on the API design. tcx is
the first user and later we plan to integrate also others, for example, one
candidate is multi-prog support for XDP which would benefit and have the same
'look and feel' from API perspective.

The goal with tcx is to have maximum compatibility to existing tc BPF programs,
so they don't need to be rewritten specifically. Compatibility to call into
classic tcf_classify() is also provided in order to allow successive migration
or both to cleanly co-exist where needed given its all one logical tc layer.
tcx supports the simplified return codes TCX_NEXT which is non-terminating (go
to next program) and terminating ones with TCX_PASS, TCX_DROP, TCX_REDIRECT.
The fd-based API is behind a static key, so that when unused the code is also
not entered. The struct tcx_entry's program array is currently static, but
could be made dynamic if necessary at a point in future. The a/b pair swap
design has been chosen so that for detachment there are no allocations which
otherwise could fail. The work has been tested with tc-testing selftest suite
which all passes, as well as the tc BPF tests from the BPF CI, and also with
Cilium's L4LB.

Kudos also to Nikolay Aleksandrov and Martin Lau for in-depth early reviews
of this work.

  [0] https://lpc.events/event/16/contributions/1353/
  [1] https://lore.kernel.org/bpf/CAEf4BzbokCJN33Nw_kg82sO=xppXnKWEncGTWCTB9vGCmLB6pw@mail.gmail.com/
  [2] https://colocatedeventseu2023.sched.com/event/1Jo6O/tales-from-an-ebpf-programs-murder-mystery-hemanth-malla-guillaume-fournier-datadog
  [3] http://vger.kernel.org/bpfconf2023_material/tcx_meta_netdev_borkmann.pdf
  [4] https://lore.kernel.org/bpf/20210604063116.234316-1-memxor@gmail.com/

Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>

---
## [cilium/linux](https://github.com/cilium/linux)@[e7da136e17...](https://github.com/cilium/linux/commit/e7da136e17f1e1149e460cade3a053d03ea37e2a)
#### Monday 2023-07-03 12:49:58 by Daniel Borkmann

bpf: Add generic attach/detach/query API for multi-progs

This adds a generic layer called bpf_mprog which can be reused by different
attachment layers to enable multi-program attachment and dependency resolution.
In-kernel users of the bpf_mprog don't need to care about the dependency
resolution internals, they can just consume it with few API calls.

The initial idea of having a generic API sparked out of discussion [0] from an
earlier revision of this work where tc's priority was reused and exposed via
BPF uapi as a way to coordinate dependencies among tc BPF programs, similar
as-is for classic tc BPF. The feedback was that priority provides a bad user
experience and is hard to use [1], e.g.:

  I cannot help but feel that priority logic copy-paste from old tc, netfilter
  and friends is done because "that's how things were done in the past". [...]
  Priority gets exposed everywhere in uapi all the way to bpftool when it's
  right there for users to understand. And that's the main problem with it.

  The user don't want to and don't need to be aware of it, but uapi forces them
  to pick the priority. [...] Your cover letter [0] example proves that in
  real life different service pick the same priority. They simply don't know
  any better. Priority is an unnecessary magic that apps _have_ to pick, so
  they just copy-paste and everyone ends up using the same.

The course of the discussion showed more and more the need for a generic,
reusable API where the "same look and feel" can be applied for various other
program types beyond just tc BPF, for example XDP today does not have multi-
program support in kernel, but also there was interest around this API for
improving management of cgroup program types. Such common multi-program
management concept is useful for BPF management daemons or user space BPF
applications coordinating about their attachments.

Both from Cilium and Meta side [2], we've collected the following requirements
for a generic attach/detach/query API for multi-progs which has been implemented
as part of this work:

  - Support prog-based attach/detach and link API
  - Dependency directives (can also be combined):
    - BPF_F_{BEFORE,AFTER} with relative_{fd,id} which can be {prog,link,none}
      - BPF_F_ID flag as {fd,id} toggle
      - BPF_F_LINK flag as {prog,link} toggle
      - If relative_{fd,id} is none, then BPF_F_BEFORE will just prepend, and
        BPF_F_AFTER will just append for attaching
      - Enforced only at attach time
    - BPF_F_{FIRST,LAST}
      - Enforced throughout the bpf_mprog state's lifetime
      - Admin override possible (e.g. link detach, prog-based BPF_F_REPLACE)
    - If no flags are set, then it's default append behavior for attaching
  - Internal revision counter and optionally being able to pass expected_revision
  - User space daemon can query current state with revision, and pass it along
    for attachment to assert current state before doing updates
  - Query also gets extension for link_ids array and link_attach_flags:
    - prog_ids are always filled with program IDs
    - link_ids are filled with link IDs when link was used, otherwise 0
    - {prog,link}_attach_flags for holding {prog,link}-specific flags
  - Must be easy to integrate/reuse for in-kernel users

The uapi-side changes needed for supporting bpf_mprog are rather minimal,
consisting of the additions of the attachment flags, revision counter, and
expanding existing union with relative_{fd,id} member.

The bpf_mprog framework consists of an bpf_mprog_entry object which holds
an array of bpf_mprog_fp (fast-path structure) and bpf_mprog_cp (control-path
structure). Both have been separated, so that fast-path gets efficient packing
of bpf_prog pointers for maximum cache efficieny. Also, array has been chosen
instead of linked list or other structures to remove unnecessary indirections
for a fast point-to-entry in tc for BPF. The bpf_mprog_entry comes as a pair
via bpf_mprog_bundle so that in case of updates the peer bpf_mprog_entry
is populated and then just swapped which avoids additional allocations that
could otherwise fail, for example, in detach case. bpf_mprog_{fp,cp} arrays are
currently static, but they could be converted to dynamic allocation if necessary
at a point in future. Locking is deferred to the in-kernel user of bpf_mprog,
for example, in case of tcx which uses this API in the next patch, it piggy-
backs on rtnl. The nitty-gritty details are in the bpf_mprog_{replace,head_tail,
add,del} implementation and an extensive test suite for checking all aspects
of this API for prog-based attach/detach and link API as BPF selftests in
this series.

Kudos also to Andrii Nakryiko for API discussions wrt Meta's BPF management.

  [0] https://lore.kernel.org/bpf/20221004231143.19190-1-daniel@iogearbox.net/
  [1] https://lore.kernel.org/bpf/CAADnVQ+gEY3FjCR=+DmjDR4gp5bOYZUFJQXj4agKFHT9CQPZBw@mail.gmail.com
  [2] http://vger.kernel.org/bpfconf2023_material/tcx_meta_netdev_borkmann.pdf

Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>

---
## [knative-automation/client-pkg](https://github.com/knative-automation/client-pkg)@[4b4ee791db...](https://github.com/knative-automation/client-pkg/commit/4b4ee791dbeeb5def968a63d6231b893d9652c83)
#### Monday 2023-07-03 13:31:54 by Knative Automation

upgrade to latest dependencies

bumping k8s.io/apimachinery 4fbe8e4...b207ce5:%0A  > b207ce5 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > 917de35 Bump runc go module v1.1.4 -> v1.1.6%0A  > 53ecdf0 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 05339fa Update golang.org/x/net to v0.7.0%0A  > eabbfd5 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 48b8d1f Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 373a5f7 Merge pull request # 114521 from 3point2/automated-cherry-pick-of-# 113283-upstream-release-1.26%0A  > b5e5df6 Fix SPDY proxy authentication with special chars%0A  > 553a2d6 Improve error message when proxy connection fails%0A  > 5d4cdd2 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > 6cbc4a3 Update golang.org/x/net 1e63c2f%0A  > 6561235 Merge pull request # 113699 from liggitt/manjusaka/fix-107415%0A  > dad8cd8 Update workload selector validation%0A  > fe82462 Add extra value validation for matchExpression field in LabelSelector%0A  > 067949d update k8s.io/utils to fix util tracing panic%0A  > 0ceff90 Merge pull request # 112223 from astraw99/fix-ownerRef-validate%0A  > 9e85d3a Merge pull request # 112649 from howardjohn/set/optimize-everything-nothing%0A  > b0dd9ec Fix ownerRef controller validate err%0A  > b03a432 Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > 88a1448 Rename and comment on why sharing is safe%0A  > 4e6bcdb dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > 3adc870 Optimize `Everything` and `Nothing` label selectors%0A  > 0524d6c Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > 5a0277f Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > 6809593 Merge pull request # 112377 from weilaaa/refactor_sets_use_generic%0A  > 70a38aa Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > f2d9aed refactor sets use generic%0A  > d097f82 dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > 7b5633b Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > b839e82 Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > b7d8973 update kube-openapi%0A  > 1dc6ace update fsnotify to v1.6.0%0A  > 78d003c Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 04898ff Bump golang.org/x/text to v0.3.8%0A  > 79993b2 Merge pull request # 112875 from pohly/update-yaml%0A  > 7379c15 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 66e26ac Merge pull request # 112707 from enj/enj/i/https_links%0A  > 882b67d Use https links for k8s KEPs, issues, PRs, etc%0A  > 7fb78ee Merge pull request # 112472 from ialidzhikov/nit/error-msg%0A  > 826a74e Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 22fe889 Improve the error returned from the `LabelSelectorAsSelector` func%0A  > e2f9797 Update to latest k8s.io/utils to pick up changes%0A  > f8159af Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 612703e Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 9901884 updated etcd to v3.5.5 and newer otel libraries as well%0A  > 6439059 Merge pull request # 112526 from liggitt/redirect%0A  > 0564b5e e2e: bump ginkgo to v2.2.0%0A  > 2e3bf73 Limit redirect proxy handling to redirected responses%0A  > 6d854d7 Merge pull request # 112349 from pohly/klog-update%0A  > e1e1b7c build: update to klog v2.80.1%0A  > ed93eed Merge pull request # 111768 from weilaaa/feature_add_symmetric_difference_in_sets_string%0A  > 36163c5 Merge pull request # 112193 from jindijamie/master%0A  > b7b9ba4 add symmetric difference in sets%0A  > 31bc292 Merge pull request # 112199 from pohly/klog-update%0A  > 1c318b6 Add an option for aggregator%0A  > 0d0d03e Merge pull request # 111936 from haoruan/bugfix-111928-microtime-marshal-precision%0A  > 145c075 dependencies: update to klog v2.80.0%0A  > 2d64dac Merge pull request # 112089 from zeze1004/fix-typo%0A  > 2187a78 Marshal MicroTime to json and proto at the same precision%0A  > 53c4d51 Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > 30e9977 Fix typo "sturct" to "struct"%0A  > 5e4f25a dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > 349dcdf Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 16a7f7a Bump prometheus/client_golang to v1.13.0%0A  > 2b9fe2c Merge pull request # 111808 from alvaroaleman/meta-wrapping%0A  > bb48261 Apimachinery meta errors: Support errors.Is and error wrapping%0Abumping k8s.io/code-generator 6523e22...eec869e:%0A  > eec869e Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > 824419b Bump runc go module v1.1.4 -> v1.1.6%0A  > ba94e65 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 6276bf2 Update golang.org/x/net to v0.7.0%0A  > 73b9c40 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 882af80 Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 6063700 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > b615940 Update golang.org/x/net 1e63c2f%0A  > 11d5c4c update k8s.io/utils to fix util tracing panic%0A  > 081720d Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > d44fa8c dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > 300cdcf Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > e0ef4aa Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > 557ce1f Merge pull request # 113126 from alexzielenski/remove-unwanted-replace%0A  > f86120d remove errant replace%0A  > d6a8b70 Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > f77ba6d dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > 3bbe215 Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > e80bbc4 Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > d403dc0 update kube-openapi%0A  > 790e4bc update fsnotify to v1.6.0%0A  > 27bd7d9 Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 4731e5c Bump golang.org/x/text to v0.3.8%0A  > a8a213c Merge pull request # 112875 from pohly/update-yaml%0A  > 5f5bab9 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 983d5d0 Merge pull request # 112819 from thockin/no-make-generators%0A  > c35177b Format calls to codegens%0A  > 83929d0 Codegens: Do not auto-set boilerplate path%0A  > 1d82d12 Merge pull request # 112705 from stevekuznetsov/skuznets/fix-comment%0A  > c3414a0 clients: clarify a misleading comment%0A  > 998e449 Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > e4543b2 Update to latest k8s.io/utils to pick up changes%0A  > 8e999f2 Merge pull request # 112613 from dims/update-github.com/go-openapi/jsonreference-to-drop-github.com/PuerkitoBio/purell%0A  > 524127d update github.com/go-openapi/jsonreference to drop github.com/PuerkitoBio/purell%0A  > 4ca0baf Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > b54a056 Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 350c30a updated etcd to v3.5.5 and newer otel libraries as well%0A  > 5f3f945 e2e: bump ginkgo to v2.2.0%0A  > 2e5cca7 Merge pull request # 112200 from pohly/client-go-shared-informer-factory-shutdown%0A  > c3fdc3c Merge pull request # 112349 from pohly/klog-update%0A  > e4b7976 client-go: support waiting for SharedInformerFactory shutdown%0A  > 135f69b build: update to klog v2.80.1%0A  > f60067d Merge pull request # 112341 from enj/enj/i/second_time_is_the_charm%0A  > 7c81c99 Merge pull request # 111768 from weilaaa/feature_add_symmetric_difference_in_sets_string%0A  > 8468f16 Remove in-tree credential plugins (again)%0A  > 9b98ed3 add symmetric difference in sets%0A  > 34125ff Merge pull request # 112199 from pohly/klog-update%0A  > a055687 dependencies: update to klog v2.80.0%0A  > 16cba21 Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > e051ad0 dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > 3a31bb1 Merge pull request # 111934 from deads2k/apply-gen%0A  > 4d73156 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 1382941 make applyconfiguration-gen skip generation for types that have generated clients and lack objectmeta%0A  > 03a75ea Bump prometheus/client_golang to v1.13.0%0A  > 17196da update the apply generator to use the same package the the client generator expects%0A  > a4e23d1 Merge pull request # 111566 from inosato/remove-ioutil-from-code-generator%0A  > a6a370c make applyconfiguration-gen handle pointers to slices%0A  > 087714e Merge pull request # 109884 from qzoscar/patch-1%0A  > fc00858 Remove ioutil from code-generator%0A  > ed79ca3 make applyconfiguration-gen work for resources without objectmeta%0A  > fea40fb Merge pull request # 111918 from liggitt/in-tree-auth%0A  > 3612509 fix a broken link%0A  > 78677a3 update the applyconfiguration-gen flag external-applyconfigurations to work%0A  > ad6af70 Revert "Remove gcp and azure auth plugins"%0A  > 7ba56cb applyconfiguration-gen handling of types that have a non-embedded use of TypeMeta%0A  > 97fa351 Merge pull request # 111696 from liggitt/go119mod%0A  > d71f529 add metav1.OwnerReference to the default external configurations to ease generation%0A  > 2b9093f Update go.mod to go1.19%0Abumping github.com/fsnotify/fsnotify 0f4b979...5f8c606:%0A  > 5f8c606 Update ChangeLog%0A  > 8878587 Tweak the docs a bit%0A  > 89b4cf1 Add test for re-adding a renamed file (# 508)%0A  > 85acde2 Update x/sys%0A  > 69c24b0 Update x/sys%0A  > fb07f82 Add test to see what happens if you watch a symlink (# 498)%0A  > 666da9c Clarify doc comment on WatchList() (# 499)%0A  > 123e4e3 Add note about README version%0A  > 61a05ce Update documentation and examples (# 496)%0A  > e180a87 Move some inotify-tests to run on all backends; test that state is cleaned up after Remove (# 494)%0A  > fdf41a3 Move some files around%0A  > 844d71f Port minor test changes from fen-v2 branch; make LICENSE text not ugly%0A  > 5b87f50 windows: simplify a bit (# 493)%0A  > 2bfaa00 all: add Watcher.{sendEvent,sendError} (# 492)%0A  > 8ab3b84 kqueue: don't set up watchers on unreadable files (# 479)%0A  > a4bcdf8 Update changelog%0A  > 4b43fad kqueue: remove timeout from unix.Kevent() (# 480)%0A  > a24f78c windows: test symlinks (# 491)%0A  > f45391f windows: run TestWatchRename/rename_overwriting_existing_file (# 490)%0A  > ee33a65 Use "os.Rename()" in tests instead of "mv"%0A  > 9dd0568 cmd/fsnotify: fix time.Format() string%0A  > 5dcbfba windows: replace syscall with golang.org/x/sys/windows%0A  > 1f8edaf windows: replace "e" with "err" for error variables%0A  > 99715ba windows: increase buffer size from 4K to 64K (# 485)%0A  > a5c5815 ci: update to use Go 1.19, kick off fewer builds, update x/sys (# 484)%0A  > f2d35c3 Remove CLA section in contributing%0A  > 4604469 Need Linux 5.9 for a useful fanotify we can use%0A  > a566bb1 Update CONTRIBUTING.md%0A  > 01dfc6f Remove PULL_REQUEST_TEMPLATE%0A  > a58e868 Run tests in illumos (# 481)%0A  > 666c6a0 Update ChangeLog%0A  > 928895c [bugfix] close handle when remWatch open in getIno (# 288)%0A  > f174f95 windows: update watch paths when renaming directories with sub-watches (# 370)%0A  > 87dc1fa Rewrite tests (# 478)%0A  > 57e6a49 Add {Event,Op}.Has() (# 477)%0A  > 39823aa Document that /proc and /sys won't work%0A  > 60fbf57 Clarify FAQ on goroutines%0A  > ca0e2f4 macos: retry if open() returns EINTR (# 475)%0A  > ff39bb4 Fix lint (# 476)%0A  > 421f529 debian 6 test: deal with multiple packages (# 474)%0A  > a3256ef Remove AUTHORS file%0A  > 0e78fa6 Update README: split out FAQ to "Platform-specific notes"%0A  > 1a7b6ef inotify: don't ignore events for files that don't exist (# 470)%0A  > f0aceb2 Tweak comment regarding relative paths (# 466)%0A  > d9c9fa5 Add cmd/fsnotify (# 463)%0A  > cc15908 kqueue: better error if watching a file fails (# 471)%0A  > c4e64e4 Replace Use of Kthread-blocking Epoll with Poller Read, Remove Per-Event LStats on Linux # 433 (# 434)%0A  > 4b8b298 Test some more things in CI (# 469)%0A  > 548b8fb Add missing changelog for 1.4.{8,9} (# 468)%0A  > 7fe2936 inotify: fix race in Close() (# 465)%0A  > 35b6378 Clarify README on network drives (# 467)%0A  > e56409e Update link to CONTRIBUTING in the README (# 464)%0A  > 4678dfd Update documentation for linux systems (max_user_watches) (# 287)%0A  > 808f582 bump up GitHub Actions (# 461)%0A  > 4193dfd Do not suppress Chmod on non-existent file (# 260)%0A  > 6ae56b7 kqueue: Make watcher.Close() O(n) instead of O(n^2) (# 233)%0A  > adf5320 strings.Builder instead of bytes.Buffer (# 285)%0A  > 217e78e Explicit mutext (un)locking (# 462)%0A  > 1a4f949 Use common error when removing an unwatched file (# 460)%0A  > 5acfdc1 windows: protect access to isClosed with mutex (# 454)%0A  > c56cafd Test Go 1.18%0A  > 37badf6 This project is archived (# 459)%0Abumping knative.dev/serving 2c1bb07...32ec382:%0A  > 32ec382 Drop unused ytt patch for Ingress ServiceType (# 14143)%0A  > 4c3b36c Update net-gateway-api nightly (# 14136)%0A  > 9a75a93 Update net-istio nightly (# 14132)%0A  > ca618b7 Update net-certmanager nightly (# 14131)%0A  > ea3e9c3 Update net-contour nightly (# 14130)%0A  > 2e7d6e4 Update community files (# 14128)%0A  > 63fa389 Allow to set QP resources per service (# 14038)%0A  > 9310e4d Update net-kourier nightly (# 14125)%0A  > 0462ce6 Update net-istio nightly (# 14126)%0A  > 2813b9a Update net-gateway-api nightly (# 14119)%0A  > eaf666e Update net-istio nightly (# 14116)%0A  > 53169cd Update net-istio nightly (# 14112)%0A  > e865aa7 Update net-contour nightly (# 14109)%0A  > 921daf8 Update net-certmanager nightly (# 14111)%0A  > bb581cc Update net-kourier nightly (# 14110)%0A  > fbfffc0 upgrade to latest dependencies (# 14108)%0A  > bcf9274 upgrade to latest dependencies (# 14101)%0A  > f085b30 fix: requests are sent to all pods even if cc=1 and the parity of activatorCount and podTracker is different (# 14022)%0A  > 9772417 Update net-kourier nightly (# 14107)%0A  > f6d0c7b Update net-contour nightly (# 14106)%0A  > 560e0ea Update net-certmanager nightly (# 14105)%0A  > 51f4f1e Update net-istio nightly (# 14104)%0A  > 18519b1 Update net-contour nightly (# 14079)%0A  > 38c155e Add chainguard-dev/actions for creating kind cluster (# 14018)%0A  > 74c57d8 Update net-istio nightly (# 14098)%0A  > 5a9c574 Update net-kourier nightly (# 14096)%0A  > 3a6c2b6 upgrade to latest dependencies (# 14095)%0A  > 5a90438 Update net-istio nightly (# 14091)%0A  > dc0692a Update net-istio nightly (# 14088)%0A  > 0fbd780 Update net-certmanager nightly (# 14087)%0A  > 6f63c98 Update net-kourier nightly (# 14086)%0A  > e74f5f4 Update net-gateway-api nightly (# 14085)%0A  > 1587070 Update net-kourier nightly (# 14081)%0A  > 2e00e9f Update net-certmanager nightly (# 14080)%0A  > a3c7864 Update net-istio nightly (# 14078)%0A  > 384b889 Update net-gateway-api nightly (# 14077)%0A  > 7d0f963 Change storage version of DomainMapping to v1beta1 (# 14058)%0A  > e8b6f05 Update net-gateway-api nightly (# 14068)%0A  > 41e4212 Get certificate reconciler from `networking` instead of `control-protocol` (# 14072)%0A  > e71b933 Update net-certmanager nightly (# 14070)%0A  > 8f516b6 Update net-kourier nightly (# 14069)%0A  > a2bb4aa upgrade to latest dependencies (# 14071)%0A  > c95f17b Update community files (# 14067)%0A  > bf48e64 Remove deprecated internalEncryption dependency (# 14064)%0A  > 6b87d67 Update net-istio nightly (# 14065)%0A  > fbecf34 refactor throttler_test.go (# 14055)%0A  > 349b2d6 Change minimum TLS version to 1.3 for internal encryption (between activator and queue-proxy) (# 13887)%0A  > d07bf78 Update net-contour nightly (# 14049)%0A  > aa023e8 Update net-istio nightly (# 14048)%0A  > 8fc4bb9 Update net-gateway-api nightly (# 14047)%0A  > 135be30 Update net-certmanager nightly (# 14046)%0A  > 8da71b5 Update net-kourier nightly (# 14042)%0A  > 13a4e46 poll until timeout - don't error out if the deployment can't be found (# 14027)%0A  > 31c2b7e upgrade to latest dependencies (# 14043)%0A  > 6a6e417 Update net-istio nightly (# 14041)%0A  > 807fc2c Update net-certmanager nightly (# 14040)%0A  > 3c23945 drop safe to evict annotations (# 14035)%0A  > fca5c14 Update net-gateway-api nightly (# 14033)%0A  > c12c917 Update net-contour nightly (# 14034)%0A  > 2da856d Update net-kourier nightly (# 14032)%0A  > d7c8779 Update net-certmanager nightly (# 14031)%0A  > aaf01dc Update net-istio nightly (# 14030)%0A  > bdaa436 RandomChoice 2 policy wasn't random when the number of targets is 2 (with equal weight) (# 14028)%0A  > c91f8c4 Fix metrics reporting period (# 14019)%0A  > 9f60969 Update net-kourier nightly (# 14004)%0A  > 6020cec Update net-istio nightly (# 14025)%0A  > 88cae7f Update net-gateway-api nightly (# 14016)%0A  > a143bf8 Update net-contour nightly (# 14015)%0A  > c2be582 Update net-certmanager nightly (# 14014)%0A  > 3450f0a upgrade to latest dependencies (# 14013)%0A  > 35cfd8f [Automated] Update net-gateway-api nightly (# 14003)%0A  > 08a9708 Update net-istio nightly (# 14009)%0A  > 5074b4c Update net-contour nightly (# 14010)%0A  > e8cb343 upgrade to latest dependencies (# 13999)%0A  > 1261074 Update net-certmanager nightly (# 14002)%0A  > f987ca6 Bump kind to 0.19 (# 14008)%0A  > fbb7fa1 Update community files (# 13998)%0A  > bff1d80 Remove 1.24 kind version (# 14007)%0A  > a657321 Update net-kourier nightly (# 13993)%0A  > d75b0f0 Update net-contour nightly (# 13990)%0A  > 6d26f54 upgrade to latest dependencies (# 13991)%0A  > df5001f Update net-certmanager nightly (# 13992)%0A  > 2594084 upgrade to latest dependencies (# 13989)%0A  > 7c303fa Update cluster-version to 1.25 (# 13988)%0A  > 9e751a2 Update net-certmanager nightly (# 13974)%0A  > 7b35cfb upgrade to latest dependencies (# 13987)%0A  > 99800ed Set default domain to cluster's domain (# 13964)%0A  > c90fabf Metric annotations work with global class config (# 13978)%0A  > da31cd1 Update net-kourier nightly (# 13975)%0A  > f457924 Update net-contour nightly (# 13976)%0A  > 14ad4d1 upgrade to latest dependencies (# 13973)%0A  > 00ddfd9 Update net-kourier nightly (# 13972)%0A  > fc63583 Update net-kourier nightly (# 13966)%0A  > 219285e Update net-kourier nightly (# 13959)%0A  > 2fa05bd Min TLS for tag to digest defaults to 1.2 again and is configurable (# 13962)%0A  > 43df348 Update net-contour nightly (# 13958)%0A  > 50a9f22 Update net-certmanager nightly (# 13961)%0A  > 4e379cb Update net-gateway-api nightly (# 13957)%0A  > 3d53294 Update net-istio nightly (# 13960)%0A  > ea2a6c8 :lipstick: Install ko using setup-ko, from ko-build (# 13951)%0A  > e5070cd upgrade to latest dependencies (# 13950)%0A  > 9778f2d Update net-istio nightly (# 13949)%0A  > f27ba4e Update net-certmanager nightly (# 13944)%0A  > 2840301 Update net-kourier nightly (# 13945)%0A  > 117a642 Update net-gateway-api nightly (# 13943)%0A  > 84a2230 Update net-contour nightly (# 13942)%0A  > 7aa5edb upgrade to latest dependencies (# 13941)%0A  > 01707d8 upgrade to latest dependencies (# 13940)%0A  > b7d5e8d Update net-istio nightly (# 13939)%0A  > 5e056a0 Update net-certmanager nightly (# 13926)%0A  > 35efd12 Update net-contour nightly (# 13929)%0A  > f476717 Update net-istio nightly (# 13935)%0A  > bd8e37c Update net-gateway-api nightly (# 13925)%0A  > 37a7010 Update net-kourier nightly (# 13934)%0A  > f47802d Update community files (# 13933)%0A  > 990d701 Update net-kourier nightly (# 13928)%0A  > ff9f03d Update net-istio nightly (# 13927)%0A  > 690c525 upgrade to latest dependencies (# 13924)%0A  > 1dd07a7 Update community files (# 13923)%0A  > 66141b8 Update net-istio nightly (# 13920)%0Abumping golang.org/x/text 71a9c9a...9db913a:%0A  > 9db913a go.mod: update to newer x/tools%0A  > 30dadde all: correct comment typos%0Abumping github.com/matttproud/golang_protobuf_extensions c182aff...c182aff:%0Abumping golang.org/x/net 8e2b117...dfa2b5d:%0A  > dfa2b5d go.mod: update golang.org/x dependencies%0A  > 8c4ef2f hmtl: add security section to package comment%0A  > 1d46ed8 html: have Render escape comments less often%0A  > 569fe81 html: add "Microsoft Outlook comment" tests%0Abumping golang.org/x/mod b3066c3...b710602:%0A  > b710602 sumdb/dirhash: correct documentation of hash%0A  > a42224d all: replace io/ioutil with io and os package%0A  > 77d797e sumdb/dirhash: fix a panic when argument is not a directory%0A  > 7c05a44 sumdb/note: remove dependency on golang.org/x/crypto/ed25519%0Abumping golang.org/x/sys 90c8f94...c7a1bf9:%0A  > c7a1bf9 unix: define PerfBitWriteBackward%0A  > 1470852 unix: add SetsockoptTCPMD5Sig on linux%0A  > a6bfb89 unix: use unsafe.Slice in anyToSockaddr%0A  > c10701f windows: use unsafe.Slice in (*RawSockaddrAny).Sockaddr on windows%0A  > 6f25076 unix: define extended TCPInfo on Linux%0A  > 10499f4 unix: add ioctlPtr with unsafe.Pointer arg on other unices (cont)%0A  > 92c4c39 unix: add Dup3 on FreeBSD%0A  > 748af6e unix: pass PROT_MPROTECT(PROT_READ|PROT_WRITE) to initial Mmap on netbsd%0A  > 972870e unix/linux: update to Linux kernel 6.2, glibc 2.37 and Go 1.20.1%0A  > cc0b67d unix: use C.ioctl in generated ioctlPtr%0A  > a3b23cc unix: use SYS_PTRACE in generated ptracePtr%0A  > 71a906e unix/linux: add TUN flags and virtio_net_hdr constants%0A  > 2977c77 unix: add ptracePtr that accepts pointer arg as unsafe.Pointer%0A  > 6877dcc execabs: don't override Go 1.19 error with our error%0A  > b13f40e unix: add ioctlPtr with unsafe.Pointer arg on other unices%0A  > 3b9b58b unix: Faccess: check CAP_DAC_OVERRIDE on Linux%0A  > 2da1413 cpu: get hwcap/auxv from the Go 1.21+ runtime%0A  > 4fee21c windows: Add WSALookupService syscall wrappers%0A  > c79a742 unix: fix a use-after-free bug in PtraceIO on freebsd%0Abumping k8s.io/client-go 7226b15...6e9dabb:%0A  > 6e9dabb Update dependencies to v0.26.5 tag%0A  > 038b381 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > cd83e43 Bump runc go module v1.1.4 -> v1.1.6%0A  > dbfbc03 Merge pull request # 117686 from ardaguclu/automated-cherry-pick-of-# 117495-upstream-release-1.26%0A  > d72dec4 Use absolute path instead requestURI in openapiv3 discovery%0A  > a5144d4 Merge pull request # 117638 from seans3/automated-cherry-pick-of-# 117571-origin-release-1.26%0A  > d6f8d04 Refactors discovery content-type and helper functions%0A  > 2dd0093 Merge pull request # 115899 from odinuge/automated-cherry-pick-of-# 115620-upstream-release-1.26%0A  > f3ae5cb Merge pull request # 116666 from seans3/automated-cherry-pick-of-# 116603-origin-release-1.26%0A  > fffc68d Change where transformers are called.%0A  > 5ebee18 Aggregated discovery resilient to nil GVK%0A  > 8190aa4 client-go/cache: update Replace comment to be more clear%0A  > 87720b3 Merge pull request # 116437 from seans3/automated-cherry-pick-of-# 116145-# 115865-origin-release-1.26%0A  > b667227 client-go/cache: rewrite Replace to check queue first%0A  > fc13749 Removes old discovery hack ignoring 403 and 404%0A  > 30215cd client-go/cache: merge ReplaceMakesDeletionsForObjectsInQueue tests%0A  > f39ba12 Plumb stale GroupVersions through aggregated discovery%0A  > ba35969 client-go/cache: fix missing delete event on replace without knownObjects%0A  > f538edf Merge pull request # 116352 from seans3/automated-cherry-pick-of-# 115978-origin-release-1.26%0A  > 97cf9cb client-go/cache: fix missing delete event on replace%0A  > 5dbbc58 Tolerate empty discovery response in memcache client%0A  > 62133a9 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 8ce239f Update golang.org/x/net to v0.7.0%0A  > e6bc0bc Merge pull request # 115566 from enj/automated-cherry-pick-of-# 115315-upstream-release-1.26%0A  > 9112e19 Merge pull request # 115400 from pohly/automated-cherry-pick-of-# 115354-origin-release-1.26%0A  > 0519b53 kubelet/client: collapse transport wiring onto standard approach%0A  > 2e34348 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 7be38cd dynamic resource allocation: avoid apiserver complaint about list content%0A  > 4968c4a Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 0c34939 Merge pull request # 114617 from JoelSpeed/automated-cherry-pick-of-# 114585-upstream-release-1.26%0A  > 04b098b Resource claims should be a map type%0A  > b3fff46 Merge pull request # 114415 from hoskeri/automated-cherry-pick-of-# 114404-upstream-release-1.26%0A  > 236db3c Merge pull request # 113988 from liggitt/automated-cherry-pick-of-# 113933-upstream-release-1.26%0A  > a2ef324 Check the correct error in d.downloadAPIs%0A  > 95a14c3 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > ebb499f Limit request retrying to []byte request bodies%0A  > 1a7cd1d Update golang.org/x/net 1e63c2f%0A  > 53f2fea sync: update go.mod%0A  > 968ba8d Merge pull request # 113797 from seans3/force-no-aggregated%0A  > c8ffed3 Merge pull request # 111023 from pohly/dynamic-resource-allocation%0A  > 3ac73ea Adds bool to force non-aggregated discovery%0A  > 61cd728 Merge pull request # 113826 from jsafrane/add-openstack%0A  > 522eaa1 api: generated files%0A  > cfd682c Merge pull request # 113375 from atiratree/PodHealthyPolicy-api%0A  > f2b10f3 Remove OpenStack cloud provider%0A  > acc9fa7 Merge pull request # 113186 from ttakahashi21/KEP-3294%0A  > f1c80d7 generated%0A  > a3d3eb0 Revert "Remove references to openstack and cinder"%0A  > c7bdab2 Generate code%0A  > 0a1f6a8 Merge pull request # 112744 from pwschuurman/statefulset-slice-impl%0A  > 1c7a870 Merge pull request # 113485 from MikeSpreitzer/apf-borrowing%0A  > eed2516 Adding implementation of KEP-3335, StatefulSetSlice%0A  > 7280270 Merge pull request # 113599 from seans3/discovery-client-update%0A  > d4a3675 apiserver: add generated files for borrowing in flowcontrol%0A  > 7694435 Update redacting functionality to redact all sensitive info in config when printing with view (# 109189)%0A  > 25d5761 Aggregated discovery client%0A  > 4b1a9fd Merge pull request # 113314 from cici37/celIntegration%0A  > ea9ec91 Merge pull request # 112905 from alexzielenski/kubectl-apply-csa-migration%0A  > 3a430a4 API - make update%0A  > 3daf180 Merge pull request # 113688 from dashpole/update_utils%0A  > 898b7a3 add FindFieldsOwners util function%0A  > dbe034b update k8s.io/utils to fix util tracing panic%0A  > 4f63b62 add UpgradeManagedFieldsPatch%0A  > 7ed3193 Merge pull request # 111545 from jlsong01/rewrite_signature_of_StartEventWatcher%0A  > c8c6cb5 add OWNERS to csaupgrade%0A  > cbe28cf Merge pull request # 113274 from Huang-Wei/kep-3521-A%0A  > 3467961 rewrite signature of function StartEventWatcher%0A  > a45874a remove kubectl annotation logic from upgrade patch%0A  > 2248bf3 Automated codegen%0A  > d576a35 Merge pull request # 113387 from wojtek-t/refactor_client_indexing%0A  > 4fbef5b Merge pull request # 106242 from thockin/revive-copy-lb-status-type-to-ingress%0A  > 5e7ba1f Minor cleanup of thread safe store%0A  > bc6266d Merge pull request # 103177 from arkbriar/support_cancelable_exec_stream%0A  > 3f162fe Copy LoadBalancerStatus from core to networking%0A  > b69a16c Refactor store index into its structure%0A  > 19b2e89 Merge pull request # 113523 from seans3/content-type-response%0A  > 0563dec Propagate the panic with a channel%0A  > 8ff4970 Get response content-type%0A  > 2362c7b use subtests and defer in TestSPDYExecutorStream%0A  > 0d57396 Merge pull request # 113304 from mimowo/handling-pod-failures-beta-ssa%0A  > 5e0a531 Support cancelable SPDY executor stream%0A  > a232cf0 Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > a191e58 SSA to add pod failure conditions - ready for review%0A  > 984bdbf dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > f87d047 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > d236783 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > ef8a2e5 Merge pull request # 113089 from zackzhangkai/fix-doc%0A  > 197e479 Merge pull request # 108959 from astraw99/fix-duplicate-list%0A  > 0945beb fix typo%0A  > 42a0e1c Merge pull request # 113062 from alexzielenski/client-go-json-output%0A  > f549acf Fix duplicate code block of ListAll function%0A  > b6d3c8d Merge pull request # 107278 from harsimranmaan/allow_pagination_in_dynamic_fake_lister%0A  > 624929c address feedback%0A  > 9cc33a4 Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > 0c269b7 remove selflink as per review feedback%0A  > 12cafe2 refactor to use Schema(contentType)%0A  > 9b51067 dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > fbd8e9a fix failing test assertions%0A  > 8b6ceae add more options for fetching openapiv3 in clients%0A  > fa9ed7f Merge pull request # 112860 from nckturner/remove-log-line%0A  > 1f10368 Preserve metadata for fake dynamic client unstructured lists%0A  > 6b24912 Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > 5870c62 Remove log line from expiration cache%0A  > aea20dd Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > e3bb48f update kube-openapi%0A  > 1af3711 update fsnotify to v1.6.0%0A  > e6d958c Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 5e469ba Bump golang.org/x/text to v0.3.8%0A  > f515a4c Merge pull request # 112774 from stevekuznetsov/skuznets/dynamic-client-similar%0A  > b28f6c9 Merge pull request # 112875 from pohly/update-yaml%0A  > 34e8a5d client-go: factor the dynamic client similarly to others%0A  > c9afc73 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > f24bd69 Merge pull request # 112306 from tkashem/v1beta3%0A  > ebc7cd4 Merge pull request # 112707 from enj/enj/i/https_links%0A  > 9b97b72 rename assuredConcurrencyShares for flowcontrol v1beta3%0A  > 2f43d37 Merge pull request # 112705 from stevekuznetsov/skuznets/fix-comment%0A  > 1665808 Use https links for k8s KEPs, issues, PRs, etc%0A  > 9bac803 apiserver: generate for apf v1beta3%0A  > 3697342 Merge pull request # 112680 from enj/enj/i/tls_cache_key_comparable%0A  > 956c1ce clients: clarify a misleading comment%0A  > c81636c Merge pull request # 112665 from NoicFank/fix-typo%0A  > cc2441c transport/cache: statically assert that tlsCacheKey is comparable%0A  > be20b2b Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 59765b8 fix typo error%0A  > 04dbcd8 Update to latest k8s.io/utils to pick up changes%0A  > 2fd4aac Merge pull request # 112613 from dims/update-github.com/go-openapi/jsonreference-to-drop-github.com/PuerkitoBio/purell%0A  > 47ad72a update github.com/go-openapi/jsonreference to drop github.com/PuerkitoBio/purell%0A  > f7c9c63 Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > b6e72dc Merge pull request # 112226 from aojea/client_go_transport%0A  > 6b5ecad updated etcd to v3.5.5 and newer otel libraries as well%0A  > acfaa39 Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 1bd914a client-go: test transport generation is goroutine safe%0A  > 037b5fd Merge pull request # 112514 from markmc/patch-1%0A  > ec6c80a e2e: bump ginkgo to v2.2.0%0A  > 3f66212 client-go: remove reference to TPR in examples%0A  > 86ffa32 Merge pull request # 112475 from vatsalparekh/fix-TestRESTClientLimiter%0A  > ece6462 Merge pull request # 112476 from enj/enj/i/list_pager_flake%0A  > bf2b395 Fix Infelicities in TestRESTClientLimiter%0A  > 58155b7 Merge pull request # 112450 from enj/enj/i/exec_tls_cache_holder_cleanup%0A  > 6703098 Check for context cancellation on each buffered chunk%0A  > eecd3e5 Merge pull request # 112091 from xyz-li/master%0A  > 5dab9a0 client-go/transport: drop Dial and GetCert fields in favor of Holders%0A  > f6b8521 Merge pull request # 111333 from flant/selfsubjectattributesreviews%0A  > cc3cc93 kubectl: fix memory leaks in port forwarding client%0A  > b2b55e6 Add auth API to get self subject attributes%0A  > 18c3338 Merge pull request # 112200 from pohly/client-go-shared-informer-factory-shutdown%0A  > 9dae691 Merge pull request # 112309 from shyamjvs/disable-compression%0A  > ec4fedd client-go: support waiting for SharedInformerFactory shutdown%0A  > ab826d2 Merge pull request # 112349 from pohly/klog-update%0A  > 49ac40b Autogen code%0A  > ab0bfda build: update to klog v2.80.1%0A  > b8a8d94 Add DisableCompression option to KubeConfig%0A  > f32861c Merge pull request # 112341 from enj/enj/i/second_time_is_the_charm%0A  > 7d208ba Remove in-tree credential plugins (again)%0A  > e003fa9 Merge pull request # 112017 from enj/enj/i/exec_tls_cache%0A  > 2698e82 Merge pull request # 111967 from alexzielenski/csa-to-ssa%0A  > 6a008ec exec auth: support TLS config caching%0A  > 27c67e7 Merge pull request # 111122 from alexzielenski/informer%0A  > 00d892f correct spacing%0A  > d28c736 Merge pull request # 112022 from JackZxj/release-lock%0A  > a300ae0 return when test is done%0A  > 2efbeaf add boilerplate%0A  > b8b6206 Merge pull request # 112199 from pohly/klog-update%0A  > d04c2ce update lock getter of leaderelection%0A  > 93e5e0e hold listener lock while waiting for goroutines to finish%0A  > dac0826 remove inaccurate comment%0A  > 5a2c3e9 dependencies: update to klog v2.80.0%0A  > e11a988 simplify control flow%0A  > 7634f2e make upgrade modify input instead of deep copying%0A  > 7ccf7b0 Merge pull request # 112134 from apelisse/client-go-valid-segment%0A  > ac7f657 fix spelling%0A  > 9aa7c11 remove fieldsv1 from upgrade body%0A  > d83ec9e Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > a4b84d8 Validate segments with client-go/dynamic%0A  > 0f4a6cf reset listenersStarted%0A  > 703d15e Update staging/src/k8s.io/client-go/util/csaupgrade/upgrade.go%0A  > cac10a8 dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > 449817f add multithreaded test to shared informer%0A  > 675ca93 refactor if statement%0A  > 46d4284 Merge pull request # 111241 from Abirdcfly/fixtestorsource%0A  > de0b767 remove duplicate test%0A  > cfaca90 address comments%0A  > bdae576 Merge pull request # 112068 from aojea/aojea_client_go%0A  > 9b300de make TestListPager_EachListItem rework%0A  > 0565962 address review comments%0A  > 089614c remove last applied configuration information%0A  > fd22687 add aojea as client-go reviewer%0A  > 5a25eb0 switch listeners to use a map, adapt tests%0A  > efe3789 add more test cases%0A  > 35ead05 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 90c6a46 active remove/add tests for event handlers%0A  > 46dc22f clean up test%0A  > 5291ca2 Bump prometheus/client_golang to v1.13.0%0A  > de4dd3a tests for invalid registration removals%0A  > ced85a8 update godoc%0A  > e6538dd Merge pull request # 112024 from cndoit18/remove-redundant-judgment%0A  > 33eff64 apply desired changes for handler registration%0A  > 049ba69 expose FieldsToSet and SetToFields%0A  > bcd2e6c style: remove redundant judgment%0A  > d73e40f rename handle to registration%0A  > aa892ab remove  unused code%0A  > d5e5863 Merge pull request # 111752 from aanm/revert-final-url-template%0A  > b3a61c6 remove informational informer methods again%0A  > 90ef078 dont expose internal methods in implementatoin%0A  > 5feaced Merge pull request # 67782 from dims/yank-in-tree-openstack-cloud-provider%0A  > e9d4627 client-go/rest: check if url is nil to prevent nil pointer dereference%0A  > ecdc8bf support removal of event handlers from SharedIndexInformers%0A  > c364b63 add function to upgrade managedfields CSA to SSA%0A  > 0fdc4f3 Merge pull request # 111684 from 0xff-dev/master1%0A  > 98e81a7 Remove references to openstack and cinder%0A  > c501ee0 Revert "client-go: remove no longer used finalURLTemplate"%0A  > 4faffa8 Merge pull request # 111564 from inosato/remove-ioutil-from-cli-client-go%0A  > c94a539 use constant NamespaceDefault instead of variable namespace%0A  > 2e40408 Merge pull request # 111918 from liggitt/in-tree-auth%0A  > 27de641 Remove ioutil from client-go%0Abumping knative.dev/eventing 034bec9...f5b1b12:%0A  > f5b1b12 Send namespace header in MT components (# 7048)%0A  > 4b5fde8 [main] Update community files (# 7043)%0A  > 8f74094 Add handler to auto create Event Types (# 7034)%0A  > 901ef61 Remove check for empty Namespace on resolver (# 7040)%0A  > 95cdbaa We should not limit the EventType creation from the Sources Duck to just brokers (# 7032)%0A  > 7429761 Adjust the Namespace reference to the one from the parent (# 7035)%0A  > cb2a891 update the redeployment script (# 7038)%0A  > ab01938 [main] Upgrade to latest dependencies (# 7025)%0A  > c9dcaf3 Added basic gc loop to kncloudevents clients map (# 6997)%0A  > d6cf96d EventType works with channel (# 7023)%0A  > 365d0b0 Run TLS e2e tests only when Istio is not enabled (# 7029)%0A  > 825a237 Update IMC CRD addressstatus to include `.name` and `.CACerts` fields (# 7026)%0A  > 3190df7 Tracking/reconcile KResource references (# 7014)%0A  > 0f68861 Rename more to Resource, instead of broker (# 7022)%0A  > bccb7d4 Better reflecting the lifecycle of event type … (# 7019)%0A  > 49d4acd Skip ping source TLS rekt test, since extremely flaky (# 7016)%0A  > 8719e18 [main] Upgrade to latest dependencies (# 7012)%0A  > e5ae717 Use HTTP POST when terminating istio proxy (# 7015)%0A  > fea730f Only check if the reference does exist (# 7010)%0A  > 631f4ec Add TLS support for mt-broker-filter (# 6940)%0A  > 45f0a19 Allow wathola components to run with Istio  (# 7011)%0A  > 65f4b1c [main] Format Go code (# 7008)%0A  > 3267b1a test SinkBinding with eventshub TLS receiver as sink (# 6979)%0A  > aad53f4 Updated eventingtls test certs to support IP addresses (# 7006)%0A  > 57d78e0 [main] Update community files (# 7004)%0A  > dfb2243 Support TLS in Trigger and Channel reconciler (# 6988)%0A  > df08b49 Eventing TLS: verify APIServerSource and PingSource sinkURI is https (# 6987)%0A  > d21c1aa [main] Upgrade to latest dependencies (# 6989)%0A  > 70113e8 Deprecate broker field and use KReference for the broker instead (# 6870)%0A  > 4e4647f test update to newest version (# 6990)%0A  > 870ac6b Update MessageDispatcher and FanoutMessageHandler to support sending events to TLS endpoints (# 6983)%0A  > 6dd5d58 Test PingSource with eventshub TLS receiver as sink (# 6965)%0A  > 55f4f28 [main] Upgrade to latest dependencies (# 6982)%0A  > 2a5a9a5 Add more items in the development getting started documentation (# 6978)%0A  > 59118a0 imc-dispatcher starts a TLS server, accepts host based routing on http receiver and path based routing on https receiver (# 6954)%0A  > ee49ada Rework kncloudevents library to support multiple clients (# 6975)%0A  > ee88094 Make ServerManager independent from kncloudevents package (# 6980)%0A  > 6a11c5f [main] Upgrade to latest dependencies (# 6969)%0A  > 8a9a532 Updated DEVELOPMENT.md to provide better instructions on setting up kubernetes (# 6977)%0A  > 390a0c8 Eventing TLS: Test ContainerSource with eventshub TLS receiver as sink (# 6957)%0A  > 5e245ac Fix flaky PingSource TLS unit test (# 6970)%0A  > f9f27c9 Use random names in Channel tests (# 6967)%0A  > d4609a5 Do not parse flags in InitializeEventingFlags (# 6966)%0A  > ef68a0a [main] Update community files (# 6968)%0A  > 4adc287 Add transport-encryption prerequisite for Addressable tests (# 6964)%0A  > deb0ef4 Add field for subscribers & replys CA certs to `SubscriberSpec` and `SubscriptionStatusPhysicalSubscription` (# 6959)%0A  > b81082c Eventing TLS: Test ApiServerSource with eventshub TLS receiver as sink (# 6956)%0A  > cdff269 Adding source duck type to v1b2 (# 6962)%0A  > b47b4ec [main] Upgrade to latest dependencies (# 6958)%0A  > 3315c20 Provide Channels CACerts in Brokers status annotation (# 6952)%0A  > 4b9fdef [main] Upgrade to latest dependencies (# 6955)%0A  > da31970 Improve cert-manager resources for Eventing TLS certs provisioning (# 6953)%0A  > fc5befb Provide subscribers CACerts in triggers status (# 6951)%0A  > 1efab19 Using v1b2 in the reconciler (# 6949)%0A  > c44671c Updating rekt test resources for EventType v1b2 (# 6946)%0A  > e31eb1f Adding testingv1b2 for eventtype (# 6944)%0A  > a9908ef Support TLS in PingSource (# 6929)%0A  > df559c0 Fix typo in flags.IsDisbledTransportEncryption name (# 6941)%0A  > 7073cc9 [main] Upgrade to latest dependencies (# 6939)%0A  > c6bc9bb Eventing TLS: Support K_CA_CERTS env variable injection for SinkBinding subjects (# 6931)%0A  > 24fbfe5 Eventing TLS: support exposing https address in Broker controller (# 6930)%0A  > d18cb42 Add information about retryable error in servermanager (# 6921)%0A  > f92a05b Added Support for K_CA_CERTS in the heartbeats (# 6920)%0A  > b8b43d0 Remove CA certs empty and non nil check, use URL scheme only (# 6928)%0A  > 3c8cc05 Return error directly if one receiver of servermanager fails (# 6919)%0A  > 92ab7f8 [main] Upgrade to latest dependencies (# 6927)%0A  > 5c6fe57 two more for reducing to debug, instead of info (# 6922)%0A  > 6cf9397 less verbose logs on scheduler component  (# 6912)%0A  > 69918f2 Adds ServerManager. Supports http/https message receivers (# 6908)%0A  > d58e259 Install ko using setup-ko in kind e2e tests (# 6910)%0A  > 9cdea5d Eventing TLS: Added Support for setting K_CA_CERTS in the ApiServerSource controller for the adapter (# 6897)%0A  > add8436 Eventing TLS: support exposing https address in InMemoryChannel controller (# 6881)%0A  > 59cfb6d [main] Upgrade to latest dependencies (# 6906)%0A  > 03f2a3d Remove unused test helper (# 6907)%0A  > 7a90c46 Remove eventing-natss from downstream tests (# 6905)%0A  > ba2550b [main] Upgrade to latest dependencies (# 6904)%0A  > 999eead More EventType v1beta2 work (# 6903)%0A  > 66e8257 Remove sanitize HTTP body for `knativeerrordata` extension (# 6902)%0A  > cd50d27 [main] Format Go code (# 6898)%0A  > 0f0a82c [main] Update community files (# 6901)%0A  > 7f4deb5 EventType v1b2 API addition (# 6893)%0A  > 1f917d0 Refactor PingSource adapter client creation (# 6880)%0A  > e2f1c77 [main] Update community files (# 6896)%0A  > 6a5c7ee Eventing TLS: migrate all resolver.URIResolver usages over to AddressableFromDestinationV1 (# 6883)%0A  > 0a12a6c Adds path based routing to message_receiver pkg (# 6873)%0Abumping k8s.io/api 88912e3...6b24792:%0A  > 6b24792 Update dependencies to v0.26.5 tag%0A  > 37e98ba Merge pull request # 117814 from kerthcet/automated-cherry-pick-of-# 117802-upstream-release-1.26%0A  > 7ff025f Update podFailurePolicy comments from alpha-level to beta%0A  > c9f384e Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > c00f1ad Bump runc go module v1.1.4 -> v1.1.6%0A  > 4c28c5a Merge pull request # 117323 from dddddai/automated-cherry-pick-of-# 117182-upstream-release-1.26%0A  > 9483bbc use case-insensitive header keys for http probes%0A  > 0545f3a Merge pull request # 116081 from pohly/automated-cherry-pick-of-# 115928-origin-release-1.26%0A  > e92d7e9 api: generated files%0A  > 16f23da api: drop Resources.Claims from PVC and PVC template%0A  > 5fd8a44 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 1b65b64 Update golang.org/x/net to v0.7.0%0A  > 2e857c1 Merge pull request # 115400 from pohly/automated-cherry-pick-of-# 115354-origin-release-1.26%0A  > 1c6bd70 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 50d0b42 dynamic resource allocation: avoid apiserver complaint about list content%0A  > 045c7fe Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 07a9cbc Merge pull request # 114617 from JoelSpeed/automated-cherry-pick-of-# 114585-upstream-release-1.26%0A  > 52655b9 Resource claims should be a map type%0A  > 07ac8fe Merge remote-tracking branch 'origin/master' into release-1.26%0A  > 566ee01 Update golang.org/x/net 1e63c2f%0A  > b966dc9 sync: update go.mod%0A  > 053624e Merge pull request # 111023 from pohly/dynamic-resource-allocation%0A  > 3590eda Merge pull request # 113375 from atiratree/PodHealthyPolicy-api%0A  > 8356158 api: update testdata%0A  > 5cb3202 Merge pull request # 113186 from ttakahashi21/KEP-3294%0A  > 5a4f9a5 generated%0A  > 78799a8 api: generated files%0A  > dfd6ea2 Generate code%0A  > 993c43c api: add UnhealthyPodEvictionPolicy for PDBs%0A  > ef72ea9 api: dynamic resource allocation API%0A  > d8ab3fb Add API and validation for CrossNamespaceVolumeDataSource%0A  > af772fc api: add resource claims to core API%0A  > 7beaa08 Merge pull request # 112744 from pwschuurman/statefulset-slice-impl%0A  > d7d25c8 Merge pull request # 113360 from mimowo/handling-pod-failures-beta-enable%0A  > f46cd33 Undo unintentional documentation comment change%0A  > f967e44 Merge pull request # 113485 from MikeSpreitzer/apf-borrowing%0A  > 11620b8 Enable the feature into beta%0A  > 6ae95de Fix typo in function emptyInvariants()%0A  > 34f4a52 apiserver: update API testdata at HEAD for flowcontrol%0A  > 3928298 Rebasing feature branch%0A  > e91ffd8 apiserver: add generated files for borrowing in flowcontrol%0A  > d961983 Update doc comments and change name of feature gate%0A  > fcd0d56 apiserver: add fields for borrowing in apf flowcontrol%0A  > adddac7 Small updates and comment fixes%0A  > 98c1aa6 Merge pull request # 113314 from cici37/celIntegration%0A  > 0d02273 Update generated protobuf files%0A  > 3f61c95 Merge pull request # 113688 from dashpole/update_utils%0A  > 8a0a045 API - make update%0A  > a5e7c66 Adding implementation of KEP-3335, StatefulSetSlice%0A  > 72a29bf Merge pull request # 113500 from kerthcet/feat/graduate-nodeInclusionPoplicy-to-beta%0A  > 2a2f510 update k8s.io/utils to fix util tracing panic%0A  > 891a1f8 Adding new api version of admissionregistration.k8s.io v1alpha1 for CEL in Admission Control%0A  > ee30dcf Merge pull request # 113047 from everpeace/improve-supplemental-groups-description%0A  > 2482389 Feat: graduate NodeInclusionPolicy to beta%0A  > a489930 Rename copy to v1alpha1%0A  > 9a33ad3 Merge pull request # 112360 from mimowo/handling-pod-failures-beta-kubelet%0A  > c4b2250 Improve the description of PodSecurityContext.SupplementalGroups (including cri-api)%0A  > 358a069 Copy over admissionregistration v1 to v1alpha1%0A  > 6c616e1 Merge pull request # 113510 from alculquicondor/finalizers-stable%0A  > 5210e2f Add pod disruption conditions for kubelet initiated failures%0A  > 2025045 Merge pull request # 113351 from andrewsykim/endpointslice-terminating-ga%0A  > aa2b4eb Graduate JobTrackingWithFinalizers to stable%0A  > 4bad656 Merge pull request # 113274 from Huang-Wei/kep-3521-A%0A  > aa9d0a7 k8s.io/api/discovery: remove API docs referencing EndpointSliceTerminatingCondition feature gate%0A  > 91f2496 Merge pull request # 113496 from avoltz/anvoltz/ga-itr%0A  > 686871f Automated codegen%0A  > c865c5c Promote ServiceInternalTrafficPolicy to GA%0A  > bd25e4f APIs, Validation and condition enforcements%0A  > 5448eb3 Merge pull request # 106242 from thockin/revive-copy-lb-status-type-to-ingress%0A  > edbfe77 Copy LoadBalancerStatus from core to networking%0A  > 6892570 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > c5dc3f4 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > 4e8dc44 Merge pull request # 111978 from Jefftree/aggregated-discovery-types%0A  > 72580e4 Add discovery types%0A  > 0184bd8 Merge pull request # 112643 from SergeyKanzhelev/removeDynamicKubeletConfig%0A  > 0f81104 Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > f8118a1 remove DynamicKubeletConfig feature gate from the code%0A  > 370c8f0 Bump golang.org/x/text to v0.3.8%0A  > 3638040 Merge pull request # 112875 from pohly/update-yaml%0A  > 7ecab5c dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 669318b Merge pull request # 112832 from tkashem/apf-prelifecycle-gen%0A  > 2cfef31 apiserver: prerelease-lifecycle-gen for flowcontrol%0A  > 3cedfad Merge pull request # 112306 from tkashem/v1beta3%0A  > 3814236 Merge pull request # 112707 from enj/enj/i/https_links%0A  > 418dd97 add testdata for flowcontrol v1beta3%0A  > ba008c5 Use https links for k8s KEPs, issues, PRs, etc%0A  > c96c62f rename assuredConcurrencyShares for flowcontrol v1beta3%0A  > be233f8 Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 51a3f54 add patch annotations to flowcontrol v1beta3%0A  > ca5be1f Update to latest k8s.io/utils to pick up changes%0A  > 7e203ee apiserver: generate for apf v1beta3%0A  > 79091da Merge pull request # 112577 from andrewsykim/feature-gate-cleanup%0A  > 19d0ef4 apiserver: enable v1beta3 for apf%0A  > 052d63f Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 1f28922 remove +featureGate=LoadBalancerClass tag in service.spec.loadBalancerClass%0A  > f50a5b7 apiserver: apf rename copy to v1beta3%0A  > 9df3db1 updated etcd to v3.5.5 and newer otel libraries as well%0A  > bed6431 apiserver: copy apf v1beta2 to v1beta3%0A  > c98ebf1 Merge pull request # 112487 from liggitt/flowcontrol-test%0A  > 5c9e17a Add compatibility fixtures for v1beta2 flowcontrol%0A  > 9842651 Merge pull request # 111333 from flant/selfsubjectattributesreviews%0A  > 43df43b Add auth API to get self subject attributes%0A  > 30ff991 Merge pull request # 112349 from pohly/klog-update%0A  > e6114e9 build: update to klog v2.80.1%0A  > 929c3f0 Merge pull request # 112301 from aojea/ipv6_rfc3849%0A  > a687cab use IPv6 Address Prefix Reserved for Documentation for api docs%0A  > 6dd661f Merge pull request # 112199 from pohly/klog-update%0A  > 8a7d12c dependencies: update to klog v2.80.0%0A  > a6ff7c9 Merge pull request # 112146 from kerthcet/feat/move-schedulerError-to-api%0A  > ab89e44 Move constant schedulerError in scheduler to v1 package%0A  > d104994 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 15b6dd2 Bump prometheus/client_golang to v1.13.0%0A  > 3be0a3c Merge pull request # 111974 from liggitt/1-25-compatibility%0A  > 49e055e Merge pull request # 111830 from t1anz0ng/typo%0A  > fcc83cd Drop 1.23 compatibility data%0A  > 64f80bd Merge pull request # 111611 from kardashov/ref-spec-docs-typo-fix%0A  > ea5df3a fix(typo): remove extra " from autoscaling doc string%0A  > 4cde1ad Add 1.25 compatibility data%0A  > 2e7b661 Merge pull request # 111657 from aojea/hc_nodeport%0A  > d07af88 Generate specs after fixing typo in documentation%0A  > 649256a Fix typo in field description.%0Abumping github.com/prometheus/client_golang 64435fc...254e546:%0A  > 254e546 Merge pull request # 1162 from kakkoyun/cut-1.14.0%0A  > 07d3a81 Merge pull request # 1161 from prometheus/release-1.13%0A  > c8a3d32 Cut v1.14.0%0A  > 870469e Test and support 1.19 (# 1160)%0A  > 53e51c4 Merge pull request # 1157 from prometheus/cut-1.13.1%0A  > b785d0c Fix go_collector_latest_test Fail on go1.19 (# 1136)%0A  > 79ca0eb Added tip from Björn + Grammarly.%0A  > 4d54769 Fix float64 comparison test failure on archs using FMA (# 1133)%0A  > 078f11f Cut 1.13.1 release (+ documenting release process).%0A  > 5f202ee Merge pull request # 1150 from prometheus/sparsehistogram%0A  > ddd7f0e Fix race condition with Exemplar in Counter (# 1146)%0A  > 0859bb8 Merge pull request # 1152 from jessicalins/update-to-custom-reg%0A  > fffb76c Merge branch 'main' into sparsehistogram%0A  > 1f93f64 Fix `CumulativeCount` value of `+Inf` bucket created from exemplar (# 1148)%0A  > 10b0550 Fix race condition with Exemplar in Counter (# 1146)%0A  > a340ca4 Run make format%0A  > e92a8c7 Avoid the term 'sparse' where possible%0A  > 8cc2b6c Fix double-counting bug in promhttp.InstrumentRoundTripperCounter (# 1118)%0A  > dcea97e Fix `CumulativeCount` value of `+Inf` bucket created from exemplar (# 1148)%0A  > 6056615 Update random example to use custom registry%0A  > d31f13b Add SparseBucketsZeroThresholdZero and groom doc comments%0A  > 9801a4e Examples: Replace deprecated WithGoCollections with WithGoCollectorRuntimeMetrics (# 1130)%0A  > 0b7f488 Update simple example to use custom registry%0A  > 58a8ca4 examples: Adjust doc comment for native histograms%0A  > 7c46c15 Clarify documentation around what constructors do (# 1125)%0A  > 9b5c5b8 Update basic example to use custom registry%0A  > 4e71e6f Update prometheus/client_model dependency%0A  > 83d56b1 Extend prometheus.Registry to implement Collector (# 1103)%0A  > 111fae1 Merge branch 'main' into sparsehistogram%0A  > 4c41dfb Clarify exemplar(Add|Observe) by renaming to (add|observe)WithExemplar (# 1122)%0A  > 25bc188 Merge pull request # 1144 from prometheus/beorn7/histogram2%0A  > f73e3cc Fix double-counting bug in promhttp.InstrumentRoundTripperCounter (# 1118)%0A  > 95cf173 Merge branch 'main' into sparsehistogram%0A  > 6942f9e sparse buckets: Fix handling of +Inf/-Inf/NaN observations%0A  > c7aa2a5 Merge pull request # 1113 from prometheus/release-1.13%0A  > ec86ef1 Merge pull request # 1092 from prometheus/beorn7/histogram%0A  > 1e61b8e Update common Prometheus files (# 1111)%0A  > 6141a07 Merge branch 'main' into sparsehistogram%0A  > 8cbcd40 histograms: Move to new exposition protobuf format%0A  > 5a321c7 Merge branch 'foo-commit' into sparsehistogram%0A  > e93e384 Merge branch 'beorn7/release' into sparsehistogram%0A  > e203144 Merge branch 'release-1.12' of github.com:prometheus/client_golang into release-1.12%0A  > 525d042 Merge branch 'main' into sparsehistogram%0A  > a516626 Merge branch 'release-1.12' into beorn7/release%0A  > a27b6d7 Fix conflicts%0A  > 6ba7871 Merge branch 'main' into sparsehistogram%0A  > eb59a7b Histogram: Fix bug with negative schemas (# 1054)%0A  > b237230 Merge branch 'main' into sparsehistogram%0A  > 294cca4 Merge branch 'main' into sparsehistogram%0A  > 70253f4 Fix typo in doc comment%0A  > 5b19c55 Merge branch 'master' into sparsehistogram%0A  > dfbcc28 Merge pull request # 901 from prometheus/beorn7/histogram%0A  > 84fcaff Merge branch 'master' into sparsehistogram%0A  > 263be8d Refactoring of sparse histograms%0A  > 9ef5f90 Allow a zero threshold of zero%0A  > 2409960 Implement strategy to limit the sparse bucket count%0A  > aa6f67a Add TODO about bucket search optimization%0A  > 43f31c2 Merge pull request # 886 from prometheus/beorn7/histogram%0A  > 5aa8534 Merge branch 'master' into sparsehistogram%0A  > 5142344 Pin client_model to the most recent sparsehistogram commit%0A  > 97eb041 Tidy go.sum%0A  > 6c4e0ef Add tests for sparse histogram%0A  > 553ed73 Fix lint warning%0A  > 31318b7 Switch to base-2 buckets%0A  > b7a540a Fix test%0A  > a9df0ba Update prometheus/client_model%0A  > ce36ee3 Merge branch 'master' into beorn7/histogram%0A  > d698336 Merge branch 'master' into beorn7/histogram%0A  > 08104a0 Minor doc comment fixes%0A  > a9d0066 Add note about pow-of-10 precision issue%0A  > d1f5366 Fix span offset%0A  > abe540f Encode sparse histograms in protobuf%0A  > c98db4e Demo sparse histograms%0Abumping github.com/prometheus/client_model 7bc5445...63fb982:%0A  > 63fb982 Merge pull request # 63 from prometheus/sparsehistogram%0A  > 5c16fa2 Merge pull request # 57 from prometheus/repo_sync%0A  > fdb567d Add note about native histograms to README%0A  > 6b8c742 Update common Prometheus files%0A  > 942d53c Update common Prometheus files%0A  > 7f720d2 Add note about experimental state of native histograms%0A  > f60d1ac Update common Prometheus files%0A  > 1f8dcad Merge pull request # 59 from prometheus/beorn7/histogram%0A  > 6dc836e Merge pull request # 53 from prometheus/repo_sync%0A  > 421ad2b Merge pull request # 58 from prometheus/beorn7/histogram%0A  > a7ff713 Flatten the buckets of native histograms%0A  > 0e1ed89 Merge pull request # 52 from prometheus/repo_sync%0A  > a227486 Update common Prometheus files%0A  > 408689d Merge branch 'master' into sparsehistogram%0A  > 0da3265 Explain Span layout better%0A  > 14ab895 Merge pull request # 51 from prometheus/repo_sync%0A  > bc75c6a Update common Prometheus files%0A  > 61b6c1a Merge pull request # 47 from prometheus/beorn7/histogram%0A  > 8171e83 Add float histograms and gauge histograms to proto spec%0A  > a863571 Merge pull request # 49 from prometheus/repo_sync%0A  > 2fc368c Update common Prometheus files%0A  > 8831f0d Merge branch 'master' into sparsehistogram%0A  > bbaf1cc Switch to base 2 and powers of 2 for resolution%0A  > 675c4e5 Merge pull request # 48 from prometheus/repo_sync%0A  > a3e6551 Update common Prometheus files%0A  > 24db95a Merge remote-tracking branch 'origin/master' into beorn7/histogram%0A  > 147c58e Move .proto file and add caching of protoc and protoc-gen-go during build (# 46)%0A  > 56ab8d9 Update common Prometheus files%0A  > 4b803f3 Experimental encoding for sparse buckets in histogram%0A  > 0255a22 Merge pull request # 43 from roidelapluie/security-dot-md%0A  > 1f48c5c Rename metrics.proto to io_prometheus_client_metrics.proto (# 45)%0A  > 60555c9 Merge pull request # 41 from prometheus/repo_sync%0A  > 1bb3080 Add SECURITY.md%0A  > 1106810 Update common Prometheus files%0Abumping knative.dev/pkg dfad48e...6eb4b40:%0A  > 6eb4b40 Update community files (# 2760)%0A  > eb63a40 Support to set qps and burst via env variable (# 2755)%0A  > 74c4be5 Generate kresource duck type codegen (# 2754)%0A  > 4dbc312 fix boilerplate (# 2753)%0A  > 15605c7 Defaulting Controller options for all kind of webhooks (# 2738)%0A  > 94b81fc Update community files (# 2752)%0A  > 5671699 drop the dynamic type (# 2750)%0A  > 9bda38b Fix some webhook testing tech debt (# 2751)%0A  > ec20442 Update community files (# 2747)%0A  > 05bfcf6 bump k8s dependencies and update min version to v1.25 (# 2745)%0A  > 52ff2ac drop dynamic client wrappers (# 2744)%0A  > a170a07 Eventing TLS: validate that Destination.CACerts is a PEM encoded cert (# 2743)%0A  > dfb4bf0 Drop dynamic wrapper injection code generation (# 2742)%0A  > db8a353 Add SinkCACerts to SourceStatus (# 2733)%0A  > 9049667 Update community files (# 2735)%0A  > aacec7f Update community files (# 2734)%0A  > 300df43 Eventing TLS: Added AddressableFromDestination method on the resolver (# 2717)%0Abumping golang.org/x/tools b3b5c13...d0863f0:%0A  > d0863f0 go.mod: update golang.org/x dependencies%0A  > 545ca87 gopls/internal/regtest/marker: require go/packages%0A  > 1ace7db go,gopls: remove license from package doc comments%0A  > ebad375 gopls/internal/lsp/protocol: prevent license rendering in godoc%0A  > 10a39ef gopls/internal/lsp/regtest: address additional comments on marker.go%0A  > 69920f2 gopls/internal/regtest/marker: add missing tests for hover%0A  > 24a13c6 gopls/internal/regtest: fill out features of the new marker tests%0A  > 2b149ce gopls/internal/regtest: add a regtest-based version of the marker tests%0A  > edddc5f go/packages: don't discard errors loading export data%0A  > a762c82 go/ssa: add MultiConvert instruction%0A  > f124b50 cmd/stringer: streamline test subprocesses%0A  > 6b6857a gopls: fix typos in comments and doc%0A  > 8111118 go/analysis/internal/facts: fix cycle in importMap.%0A  > dd1c468 gopls/internal/lsp/source: simplify extracting object hover doc%0A  > 66f8f71 gopls/internal/lsp/source: use syntax alone in FormatVarType%0A  > 30f191f internal/imports: update stdlib index for Go 1.20%0A  > 4e98188 internal/imports: use go/packages instead of cmd/api to compute symbols%0A  > 4e8ff89 internal/imports: update stdlib index for 1.20%0A  > 6bd0d00 gopls/internal/lsp: go to definition from linkname directive%0A  > 0cfddb3 gopls/internal/lsp: enable clear builtin completion test%0A  > 41adf8d gopls/internal/lsp/tests: remove StripSubscripts%0A  > 86fdadc gopls/internal/lsp/safetoken: delete safetoken.Range%0A  > c276ee5 internal/robustio: fix signature of getFileID on plan9%0A  > e170d45 gopls/internal/lsp: add clear builtin%0A  > 2ea4b81 go/ast/inspector: skip ranges that do not contain a node type%0A  > 407bbed go/analysis: improve error message on duplicate fixes%0A  > bd5dfbb all: fix some comments%0A  > 072fca5 gopls/protocol: use the current definition of the lsp%0A  > aa633e7 tools/gopls: provide markdown for completion and signature help%0A  > 684a1c0 go/analysis/internal/analysisflags: use os.Executable for program path%0A  > bd5e595 gopls/internal/lsp/cache: add missing mutex%0A  > 2683128 gopls/internal/lsp: differentiate govulncheck/vulncheck imports diags%0A  > d1e92d6 gopls/internal/lsp/mod: reorder vulncheck quick fixes%0A  > 87d00e6 gopls/internal/lsp: separate some requests from source.Identifier%0A  > ae242ec gopls: fix windows file corruption%0A  > 6f65213 gopls/internal/lsp/protocol: Mapper.NodeMappedRange%0A  > e260368 gopls/semantic: report type parameters in the type of a receiver%0A  > b62cbb6 internal/lockedfile: fix build constraints on solaris%0A  > 1aa7e72 gopls/internal/lsp/source: avoid qualifiedObjectsAtProtocolPos%0A  > 5ed33df gopls/internal/lsp/source: rename: prep for incrementality%0A  > e0659d1 gopls/internal/lsp/source: simplify legacy 'references' func%0A  > 1edcfe7 gopls/internal/regtest/diagnostics: require cgo for TestGoListErrors%0A  > f052158 gopls/internal/lsp/protocol: move TestBytesOffset%0A  > d093a13 gopls/internal/lsp/protocol: LocationTextDocumentPositionParams%0A  > bcb677e gopls/internal/regtest: make RegexpSearch return a Location%0A  > 60782e9 gopls/internal/lsp/source: eliminate a couple uses of posToMappedRange%0A  > 031e6e6 gopls/internal/lsp/source: eliminate ResolveImportPath%0A  > f2cd9ef gopls/internal/lsp/source: reduce usage of TypecheckWorkspace%0A  > f10e7d5 gopls/internal/lsp/cache: remove package dependence on packages.Config%0A  > 8270757 gopls/internal/lsp/source: switch call hierarchy to references v2%0A  > 37c69d8 gopls/internal/lsp/source: references: support exported methods%0A  > f3c36a2 gopls/internal/lsp/cmd/test: delete marker-based tests of gopls cmd%0A  > c224aae gopls/internal/lsp/cmd/test: new integration test for gopls command%0A  > deeb64b gopls/internal/lsp/source/xrefs: allow Lookup of a set%0A  > f269f53 gopls/internal/lsp: remove Server.processModifications%0A  > fcd57eb gopls: allow 'any' and 'comparable' in completion results%0A  > aae3642 gopls/internal/lsp/source: referencesV2: support unexported methods%0A  > b5d65e0 tools/gopls: register semantic tokens statically%0A  > 51abc5b gopls/internal/lsp/source: stub: don't panic when encountering 'error'%0A  > ce28f40 gopls/internal/regtest: add a test demonstrating confusion following an%0A  > c4c6aa6 internal/lsp/cache: don't panic in Snapshot on a shutdown view%0A  > 1faecd3 tools/internal/diff: fix off-by-one error in computing diffs%0A  > a7f033a gopls/internal/lsp: consolidate the FileHandle API%0A  > 271e621 internal/lockedfile/internal/filelock: fix aix build tag%0A  > ff9bea5 gopls/internal/lsp/cmd/test: signpost future cleanups%0A  > 7d4ba2f gopls/release: remove unused functionality from release script%0A  > 46b6958 gopls/internal/lsp/source: delete source_test%0A  > bcc7794 go/analysis/passes/directive: add directive analyzer%0A  > 33d416e gopls/internal/lsp: add missing comments on 3x tests.Test impls%0A  > afea272 gopls/internal/lsp/source: make implementations2 work on embedded fields%0A  > bb7c440 gopls/internal/lsp/filecache: use file locking, not rename%0A  > 561a9be gopls/internal/lsp/filecache: actually delete files%0A  > 9682b0d gopls/internal/lsp/source: delete IsInterface%0A  > 7a7b699 go/analysis/passes/loopclosure: avoid panic in new parallel subtest check when t.Run has single argument%0A  > 3e6f71b gopls/internal/regtest: use AfterChange in more places%0A  > 9ff31a5 x/tools/go/analysis/passes/printf: revert URL in error message%0A  > 2fa6ca1 gopls/internal/lsp/source/impls: a new "implementations" index%0A  > 957bec5 gopls/protocol: new versions of generated LSP files%0A  > f0e2d5c internal/gcimporter: discard position info for unneeded lines%0A  > 5bedd86 cmd/digraph: use ReadString rather than bufio.Scanner%0A  > f6ea009 gopls/internal/lsp: remove the experimentalWatchedFileDelay setting%0A  > f46e418 gopls/internal/lsp/source: include ITVs in global references%0A  > f3e53e5 internal/jsonrpc2_v2: fix typos%0A  > d958e85 internal/gcimporter: use two-level file index%0A  > 8aba49b internal/gcimporter: preserve column and line in shallow iexport%0A  > d7fc4e7 gopls: new LSP stub generator%0A  > 5c176b1 internal/robustio: skip os.Link test on android%0A  > d34a055 go/ssa: sanity check the types of phi nodes%0A  > 6f095b4 go/callgraph/vta: add flows for receiver function types%0A  > 8e94967 cmd/fiximports: do not assume go list -json unmarshals into build.Package%0A  > e035d0c go/ssa: fix phi node type in slice to array conversion%0A  > 03eac81 go/expect: remove testdata go.mod to go.fake.mod%0A  > 1e819a3 gopls/internal/regtest: follow-ups to review comments from earlier CLs%0A  > 9ba8bb1 gopls/internal/regtest: clean up workspace symbol helpers%0A  > 91b6070 gopls/internal/regtest: eliminate DiagnosticAtRegexp%0A  > bd48b9a gopls/internal/regtest: eliminate DiagnosticsAtRegexpWithMessage%0A  > 5d65394 gopls/internal/regtest: eliminate DiagnosticAt%0A  > 27dfeb2 gopls/internal/regtest: replace NoDiagnostics with NoMatchingDiagnostics%0A  > 87092c8 gopls/internal/lsp/fake: use protocol types for the fake editor%0A  > 672a036 gopls/internal/regtest: simplify OnceMet expressions with an env helper%0A  > ab7b5b2 gopls/internal/regtest: eliminate GoSumDiagnostic%0A  > 331a1c6 gopls/internal/regtest: add a simpler API for diagnostic expectations%0A  > c9b82f2 gopls/internal/regtest: eliminate EmptyDiagnostics%0A  > e81af27 gopls: update golang.org/x/vuln@6ad3e3d%0A  > d19e3d1 in…

---
## [dfinity/motoko](https://github.com/dfinity/motoko)@[b0f5aee3c7...](https://github.com/dfinity/motoko/commit/b0f5aee3c71c66f01aaad12cabe39928b043b829)
#### Monday 2023-07-03 13:32:38 by Claudio Russo

feat: allow canister imports of service constructors, silently ignoring the service arguments. (#4041)

Allow canister imports of service constructors, silently ignoring the service arguments. 

A hack that fixes #3990 (for some definition of fix) and duplicate #2319.

Really, dfx should be feeding the idl of the instantiated service, not service constructor, to dependent canisters, but until it's fixed to do so (and it hasn't been forever now), this is a reasonable and simple workaround, avoiding the error-prone and kludgy workaround of rewriting candid files described, for instance, here:

https://dfinityorg.notion.site/ckBTC-example-Encode-Hackathon-0aaf6292e3404dabb49df5d1b5abc797#08a7469beaf14d6ba35e8827e363e160

and also used here:

https://github.com/letmejustputthishere/ckbtc-payments

via npm scripting hacks (!).

Also see here for the pain this caused:

https://forum.dfinity.org/t/confusing-type-error-when-crossing-canisters-expression-of-type-mytype-cannot-produce-expected-type-mytype-1/20636

UPDATE: I turned the previous error into a warning to nag us to fix dfx.


UPDATE: Potentially obviated by https://github.com/dfinity/sdk/pull/3138, which teaches dfx to strip the service argument.

UPDATE: @chenyan-dfinity thinks we should still merge for other scenarios (old dfx, new compiler, I guess).

---
## [consul/consul](https://github.com/consul/consul)@[970a64e276...](https://github.com/consul/consul/commit/970a64e2762c8dd8c9e265acb9195f069ea7bb0a)
#### Monday 2023-07-03 14:16:15 by Javi Martín

Enable mousewheel when focusing on the map

Zooming with the mousewheel is useful when you want to use it, but
annoying when you don't want to.

Here we're taking an intermediary approach: by default, the mousewheel
isn't active, but it will be active after focusing on the map, so it can
be used both to scroll and to zoom.

This behavior presents usability issues, though, since we aren't making
users aware of the way the mousewheel works, and even if they were
aware, it could be confusing anyway. However, I currently think it's
better than always enabling or always disabling the mousewheel (might
change my mind, though).

Note that the "focus" event is only used on the map, so if we click on a
marker or navigate to a marker with the keyboard without focusing on the
map first, the mousewheel isn't enabled. The same would happen if we
used the "click" event.

We might use the Leaflet.GestureHandling plugin in the future to deal
with this issue and the scroll on touch screens.

---
## [knative-automation/kn-plugin-source-kamelet](https://github.com/knative-automation/kn-plugin-source-kamelet)@[608bf864c8...](https://github.com/knative-automation/kn-plugin-source-kamelet/commit/608bf864c87297b3530bdae704b7e0a7fd81619f)
#### Monday 2023-07-03 14:16:20 by Knative Automation

upgrade to latest dependencies

bumping k8s.io/apiextensions-apiserver 2c55649...52c998e:%0A  > 52c998e Update dependencies to v0.26.5 tag%0A  > 186ff9b Merge pull request # 117274 from jkh52/release-1.26-knp-0.0.37%0A  > b7b18f5 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > ee5015a Bump konnectivity-client to 0.0.37%0A  > 9ce75f3 Bump runc go module v1.1.4 -> v1.1.6%0A  > e9d194a Merge pull request # 115599 from jkh52/release-1.26-knp-0.0.36%0A  > d7df0be Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 9152c67 Bump konnectivity-client to v0.0.36%0A  > 89cec57 Update golang.org/x/net to v0.7.0%0A  > f72cc5c Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 28eb995 Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 33db789 Merge pull request # 114861 from jpbetz/release-1.26%0A  > a06e03d Merge pull request # 114927 from jkh52/release-1.26-knp-metrics%0A  > 0859963 Cherry pick 114857 to release-1.26%0A  > 5183885 Bump konnectivity-client to v0.0.35%0A  > 6e13726 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > c338f3e Update golang.org/x/net 1e63c2f%0A  > 9768bad sync: update go.mod%0A  > f9c2bba fix aggregated discovery version sorting%0A  > d2c9e18 Merge pull request # 113171 from Jefftree/aggregated-discovery-generic%0A  > 470c040 Merge pull request # 113577 from pacoxu/prometheus-client%0A  > 915a888 add crds to aggregated discovery%0A  > 92430b6 Merge pull request # 113314 from cici37/celIntegration%0A  > ac326ca upgrade prometheus-client to v1.14.0%0A  > 5a6bf16 Merge pull request # 113688 from dashpole/update_utils%0A  > 67b0610 Integrate cel admission with API.%0A  > 84fed82 upgrade github.com/prometheus/client_golang to v1.13.1%0A  > 077b441 update k8s.io/utils to fix util tracing panic%0A  > 5bbf20d Adding new api version of admissionregistration.k8s.io v1alpha1 for CEL in Admission Control%0A  > 3b533ba Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > 975bbeb dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > ae2b4c3 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > c4deae9 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > bc4263f Merge pull request # 113172 from dashpole/endpoint_handler_tracing%0A  > f6c164e migrate apiserver utiltrace usage to component-base/tracing%0A  > 53e3726 Merge pull request # 113015 from ritazh/crencryption%0A  > c8d8a9f Enable encryption for custom resources%0A  > 6405068 Merge pull request # 113325 from panslava/fix-time-since-defer%0A  > 508e399 Fix time.Since() in defer. Wrap in anonymous function%0A  > 5f8e59e Merge pull request # 112691 from aimuz/apiextensions-apiserver-change-to-cmp%0A  > c996139 Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > f83e03c apiextensions-apiserver: change k8s.io/apimachinery/pkg/util/diff to github.com/google/go-cmp/cmp%0A  > b68fc51 dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > 49c41b4 Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > 3aaa2a0 Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > d9f6ebd update kube-openapi%0A  > 82e3ba4 Merge pull request # 112789 from enj/enj/r/kms_load_once_v2%0A  > 7423813 update fsnotify to v1.6.0%0A  > 8bf3487 Merge pull request # 113011 from jpmcb/cobra-1.6.0%0A  > d34393e Load encryption config once%0A  > 6ba582f Bumps cobra from 1.5.0 to 1.6.0%0A  > 8e0697b Merge pull request # 113022 from logicalhan/webhook-metrics%0A  > 90c63e0 Merge pull request # 112926 from jiahuif-forks/refactor/cel-out-of-apiextensions%0A  > 548c480 unparameterize 'webhook' from conversion metrics since it's the only one%0A  > 77badb8 Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 609e270 use DefaultMaxRequestSizeBytes for maxRequestSizeBytes.%0A  > 04f26fa Bump golang.org/x/text to v0.3.8%0A  > dd981e1 move CEL package to apiserver package.%0A  > 1644998 Move celopenapi/model to staging/src/k8s.io/apiextensions-apiserver/pkg/apiserver/schema/cel/ (# 109959)%0A  > 08d44e8 Merge pull request # 112875 from pohly/update-yaml%0A  > 1300140 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 5fb82bd Merge pull request # 112819 from thockin/no-make-generators%0A  > f5f5279 Codegens: Do not auto-set boilerplate path%0A  > f22ee73 Merge pull request # 112738 from liggitt/proto-tag%0A  > ba7f1b7 Merge pull request # 112689 from cheftako/master%0A  > 7ac7774 github.com/matttproud/golang_protobuf_extensions v1.0.2%0A  > e678457 Merge pull request # 112748 from wojtek-t/lock_ssa_gate%0A  > 0aca5a6 Bump konnectivity-client to v0.0.33%0A  > 9be4b4a Lock ServerSideApply feature to true%0A  > 7b53cb7 Merge pull request # 111980 from aramase/kms%0A  > f40a683 Merge pull request # 112705 from stevekuznetsov/skuznets/fix-comment%0A  > 4cd9125 Add staging directory for kms%0A  > d4e654a clients: clarify a misleading comment%0A  > 8b851d9 Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 362a89c Merge pull request # 112615 from mengjiao-liu/update_CRD_link%0A  > add0c80 Update to latest k8s.io/utils to pick up changes%0A  > 374216b Merge pull request # 112613 from dims/update-github.com/go-openapi/jsonreference-to-drop-github.com/PuerkitoBio/purell%0A  > a7ee7f9 Update `PreserveUnknownFields` field document link%0A  > 488bf20 update github.com/go-openapi/jsonreference to drop github.com/PuerkitoBio/purell%0A  > 47c15ca Merge pull request # 112588 from pacoxu/fsnotify-v1.5.4%0A  > d5b6243 Merge pull request # 112584 from dims/brneto-master%0A  > 8c6aa82 update fsnotify/fsnotify to v1.5.4%0A  > f8e18e9 run pin-dependency.sh and then hack/update-vendor.sh%0A  > c540c8c Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 70b0d96 Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 39cab0b updated etcd to v3.5.5 and newer otel libraries as well%0A  > 5faccda Merge pull request # 111866 from pacoxu/validate%0A  > 1c3fe9d e2e: bump ginkgo to v2.2.0%0A  > 917d446 Merge pull request # 112458 from dims/switch-to-release-tag-for-antlr-v1.4.10%0A  > 8b3fe74 add test case for array checking with dup values%0A  > 045fc90 Merge pull request # 112433 from ncdc/reduce-SchemaHas-allocs%0A  > 73cc883 Switch to release tag for antlr : v1.4.10%0A  > 22bcc66 added ratcheting validation for embedded resource and x-kubernetes-list-type validation%0A  > 269d73d Reduce allocations in HasSchemas%0A  > 7342cc6 Merge pull request # 112200 from pohly/client-go-shared-informer-factory-shutdown%0A  > aabbdff Merge pull request # 112349 from pohly/klog-update%0A  > fdf28bc client-go: support waiting for SharedInformerFactory shutdown%0A  > 6b7d12b build: update to klog v2.80.1%0A  > 559b4fa Merge pull request # 111768 from weilaaa/feature_add_symmetric_difference_in_sets_string%0A  > bf7d058 add symmetric difference in sets%0A  > 04ff81e Merge pull request # 112199 from pohly/klog-update%0A  > 87a4c3f dependencies: update to klog v2.80.0%0A  > 8f15690 Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > f637e1c dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > b6adc1c Merge pull request # 111964 from DangerOnTheRanger/cel-estimate-fix-update%0A  > ea2d438 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 6b4dc0b Add unit tests.%0A  > 767e67b Bump prometheus/client_golang to v1.13.0%0A  > 782b982 Run pin-dependency.sh and update-vendor.sh.%0A  > 305963e Merge pull request # 111909 from tosi3k/bump-prom-client%0A  > fa2959a Merge pull request # 111830 from t1anz0ng/typo%0A  > 5a6ffec Bump prometheus/client_golang to v1.12.2%0A  > e0abc3b fix(typo): remove extra " from autoscaling doc string%0A  > 2184a8d Merge pull request # 111696 from liggitt/go119mod%0A  > f750907 Update go.mod to go1.19%0Abumping k8s.io/client-go 7226b15...6e9dabb:%0A  > 6e9dabb Update dependencies to v0.26.5 tag%0A  > 038b381 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > cd83e43 Bump runc go module v1.1.4 -> v1.1.6%0A  > dbfbc03 Merge pull request # 117686 from ardaguclu/automated-cherry-pick-of-# 117495-upstream-release-1.26%0A  > d72dec4 Use absolute path instead requestURI in openapiv3 discovery%0A  > a5144d4 Merge pull request # 117638 from seans3/automated-cherry-pick-of-# 117571-origin-release-1.26%0A  > d6f8d04 Refactors discovery content-type and helper functions%0A  > 2dd0093 Merge pull request # 115899 from odinuge/automated-cherry-pick-of-# 115620-upstream-release-1.26%0A  > f3ae5cb Merge pull request # 116666 from seans3/automated-cherry-pick-of-# 116603-origin-release-1.26%0A  > fffc68d Change where transformers are called.%0A  > 5ebee18 Aggregated discovery resilient to nil GVK%0A  > 8190aa4 client-go/cache: update Replace comment to be more clear%0A  > 87720b3 Merge pull request # 116437 from seans3/automated-cherry-pick-of-# 116145-# 115865-origin-release-1.26%0A  > b667227 client-go/cache: rewrite Replace to check queue first%0A  > fc13749 Removes old discovery hack ignoring 403 and 404%0A  > 30215cd client-go/cache: merge ReplaceMakesDeletionsForObjectsInQueue tests%0A  > f39ba12 Plumb stale GroupVersions through aggregated discovery%0A  > ba35969 client-go/cache: fix missing delete event on replace without knownObjects%0A  > f538edf Merge pull request # 116352 from seans3/automated-cherry-pick-of-# 115978-origin-release-1.26%0A  > 97cf9cb client-go/cache: fix missing delete event on replace%0A  > 5dbbc58 Tolerate empty discovery response in memcache client%0A  > 62133a9 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 8ce239f Update golang.org/x/net to v0.7.0%0A  > e6bc0bc Merge pull request # 115566 from enj/automated-cherry-pick-of-# 115315-upstream-release-1.26%0A  > 9112e19 Merge pull request # 115400 from pohly/automated-cherry-pick-of-# 115354-origin-release-1.26%0A  > 0519b53 kubelet/client: collapse transport wiring onto standard approach%0A  > 2e34348 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 7be38cd dynamic resource allocation: avoid apiserver complaint about list content%0A  > 4968c4a Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 0c34939 Merge pull request # 114617 from JoelSpeed/automated-cherry-pick-of-# 114585-upstream-release-1.26%0A  > 04b098b Resource claims should be a map type%0A  > b3fff46 Merge pull request # 114415 from hoskeri/automated-cherry-pick-of-# 114404-upstream-release-1.26%0A  > 236db3c Merge pull request # 113988 from liggitt/automated-cherry-pick-of-# 113933-upstream-release-1.26%0A  > a2ef324 Check the correct error in d.downloadAPIs%0A  > 95a14c3 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > ebb499f Limit request retrying to []byte request bodies%0A  > 1a7cd1d Update golang.org/x/net 1e63c2f%0A  > 53f2fea sync: update go.mod%0A  > 968ba8d Merge pull request # 113797 from seans3/force-no-aggregated%0A  > c8ffed3 Merge pull request # 111023 from pohly/dynamic-resource-allocation%0A  > 3ac73ea Adds bool to force non-aggregated discovery%0A  > 61cd728 Merge pull request # 113826 from jsafrane/add-openstack%0A  > 522eaa1 api: generated files%0A  > cfd682c Merge pull request # 113375 from atiratree/PodHealthyPolicy-api%0A  > f2b10f3 Remove OpenStack cloud provider%0A  > acc9fa7 Merge pull request # 113186 from ttakahashi21/KEP-3294%0A  > f1c80d7 generated%0A  > a3d3eb0 Revert "Remove references to openstack and cinder"%0A  > c7bdab2 Generate code%0A  > 0a1f6a8 Merge pull request # 112744 from pwschuurman/statefulset-slice-impl%0A  > 1c7a870 Merge pull request # 113485 from MikeSpreitzer/apf-borrowing%0A  > eed2516 Adding implementation of KEP-3335, StatefulSetSlice%0A  > 7280270 Merge pull request # 113599 from seans3/discovery-client-update%0A  > d4a3675 apiserver: add generated files for borrowing in flowcontrol%0A  > 7694435 Update redacting functionality to redact all sensitive info in config when printing with view (# 109189)%0A  > 25d5761 Aggregated discovery client%0A  > 4b1a9fd Merge pull request # 113314 from cici37/celIntegration%0A  > ea9ec91 Merge pull request # 112905 from alexzielenski/kubectl-apply-csa-migration%0A  > 3a430a4 API - make update%0A  > 3daf180 Merge pull request # 113688 from dashpole/update_utils%0A  > 898b7a3 add FindFieldsOwners util function%0A  > dbe034b update k8s.io/utils to fix util tracing panic%0A  > 4f63b62 add UpgradeManagedFieldsPatch%0A  > 7ed3193 Merge pull request # 111545 from jlsong01/rewrite_signature_of_StartEventWatcher%0A  > c8c6cb5 add OWNERS to csaupgrade%0A  > cbe28cf Merge pull request # 113274 from Huang-Wei/kep-3521-A%0A  > 3467961 rewrite signature of function StartEventWatcher%0A  > a45874a remove kubectl annotation logic from upgrade patch%0A  > 2248bf3 Automated codegen%0A  > d576a35 Merge pull request # 113387 from wojtek-t/refactor_client_indexing%0A  > 4fbef5b Merge pull request # 106242 from thockin/revive-copy-lb-status-type-to-ingress%0A  > 5e7ba1f Minor cleanup of thread safe store%0A  > bc6266d Merge pull request # 103177 from arkbriar/support_cancelable_exec_stream%0A  > 3f162fe Copy LoadBalancerStatus from core to networking%0A  > b69a16c Refactor store index into its structure%0A  > 19b2e89 Merge pull request # 113523 from seans3/content-type-response%0A  > 0563dec Propagate the panic with a channel%0A  > 8ff4970 Get response content-type%0A  > 2362c7b use subtests and defer in TestSPDYExecutorStream%0A  > 0d57396 Merge pull request # 113304 from mimowo/handling-pod-failures-beta-ssa%0A  > 5e0a531 Support cancelable SPDY executor stream%0A  > a232cf0 Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > a191e58 SSA to add pod failure conditions - ready for review%0A  > 984bdbf dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > f87d047 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > d236783 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > ef8a2e5 Merge pull request # 113089 from zackzhangkai/fix-doc%0A  > 197e479 Merge pull request # 108959 from astraw99/fix-duplicate-list%0A  > 0945beb fix typo%0A  > 42a0e1c Merge pull request # 113062 from alexzielenski/client-go-json-output%0A  > f549acf Fix duplicate code block of ListAll function%0A  > b6d3c8d Merge pull request # 107278 from harsimranmaan/allow_pagination_in_dynamic_fake_lister%0A  > 624929c address feedback%0A  > 9cc33a4 Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > 0c269b7 remove selflink as per review feedback%0A  > 12cafe2 refactor to use Schema(contentType)%0A  > 9b51067 dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > fbd8e9a fix failing test assertions%0A  > 8b6ceae add more options for fetching openapiv3 in clients%0A  > fa9ed7f Merge pull request # 112860 from nckturner/remove-log-line%0A  > 1f10368 Preserve metadata for fake dynamic client unstructured lists%0A  > 6b24912 Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > 5870c62 Remove log line from expiration cache%0A  > aea20dd Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > e3bb48f update kube-openapi%0A  > 1af3711 update fsnotify to v1.6.0%0A  > e6d958c Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 5e469ba Bump golang.org/x/text to v0.3.8%0A  > f515a4c Merge pull request # 112774 from stevekuznetsov/skuznets/dynamic-client-similar%0A  > b28f6c9 Merge pull request # 112875 from pohly/update-yaml%0A  > 34e8a5d client-go: factor the dynamic client similarly to others%0A  > c9afc73 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > f24bd69 Merge pull request # 112306 from tkashem/v1beta3%0A  > ebc7cd4 Merge pull request # 112707 from enj/enj/i/https_links%0A  > 9b97b72 rename assuredConcurrencyShares for flowcontrol v1beta3%0A  > 2f43d37 Merge pull request # 112705 from stevekuznetsov/skuznets/fix-comment%0A  > 1665808 Use https links for k8s KEPs, issues, PRs, etc%0A  > 9bac803 apiserver: generate for apf v1beta3%0A  > 3697342 Merge pull request # 112680 from enj/enj/i/tls_cache_key_comparable%0A  > 956c1ce clients: clarify a misleading comment%0A  > c81636c Merge pull request # 112665 from NoicFank/fix-typo%0A  > cc2441c transport/cache: statically assert that tlsCacheKey is comparable%0A  > be20b2b Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 59765b8 fix typo error%0A  > 04dbcd8 Update to latest k8s.io/utils to pick up changes%0A  > 2fd4aac Merge pull request # 112613 from dims/update-github.com/go-openapi/jsonreference-to-drop-github.com/PuerkitoBio/purell%0A  > 47ad72a update github.com/go-openapi/jsonreference to drop github.com/PuerkitoBio/purell%0A  > f7c9c63 Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > b6e72dc Merge pull request # 112226 from aojea/client_go_transport%0A  > 6b5ecad updated etcd to v3.5.5 and newer otel libraries as well%0A  > acfaa39 Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 1bd914a client-go: test transport generation is goroutine safe%0A  > 037b5fd Merge pull request # 112514 from markmc/patch-1%0A  > ec6c80a e2e: bump ginkgo to v2.2.0%0A  > 3f66212 client-go: remove reference to TPR in examples%0A  > 86ffa32 Merge pull request # 112475 from vatsalparekh/fix-TestRESTClientLimiter%0A  > ece6462 Merge pull request # 112476 from enj/enj/i/list_pager_flake%0A  > bf2b395 Fix Infelicities in TestRESTClientLimiter%0A  > 58155b7 Merge pull request # 112450 from enj/enj/i/exec_tls_cache_holder_cleanup%0A  > 6703098 Check for context cancellation on each buffered chunk%0A  > eecd3e5 Merge pull request # 112091 from xyz-li/master%0A  > 5dab9a0 client-go/transport: drop Dial and GetCert fields in favor of Holders%0A  > f6b8521 Merge pull request # 111333 from flant/selfsubjectattributesreviews%0A  > cc3cc93 kubectl: fix memory leaks in port forwarding client%0A  > b2b55e6 Add auth API to get self subject attributes%0A  > 18c3338 Merge pull request # 112200 from pohly/client-go-shared-informer-factory-shutdown%0A  > 9dae691 Merge pull request # 112309 from shyamjvs/disable-compression%0A  > ec4fedd client-go: support waiting for SharedInformerFactory shutdown%0A  > ab826d2 Merge pull request # 112349 from pohly/klog-update%0A  > 49ac40b Autogen code%0A  > ab0bfda build: update to klog v2.80.1%0A  > b8a8d94 Add DisableCompression option to KubeConfig%0A  > f32861c Merge pull request # 112341 from enj/enj/i/second_time_is_the_charm%0A  > 7d208ba Remove in-tree credential plugins (again)%0A  > e003fa9 Merge pull request # 112017 from enj/enj/i/exec_tls_cache%0A  > 2698e82 Merge pull request # 111967 from alexzielenski/csa-to-ssa%0A  > 6a008ec exec auth: support TLS config caching%0A  > 27c67e7 Merge pull request # 111122 from alexzielenski/informer%0A  > 00d892f correct spacing%0A  > d28c736 Merge pull request # 112022 from JackZxj/release-lock%0A  > a300ae0 return when test is done%0A  > 2efbeaf add boilerplate%0A  > b8b6206 Merge pull request # 112199 from pohly/klog-update%0A  > d04c2ce update lock getter of leaderelection%0A  > 93e5e0e hold listener lock while waiting for goroutines to finish%0A  > dac0826 remove inaccurate comment%0A  > 5a2c3e9 dependencies: update to klog v2.80.0%0A  > e11a988 simplify control flow%0A  > 7634f2e make upgrade modify input instead of deep copying%0A  > 7ccf7b0 Merge pull request # 112134 from apelisse/client-go-valid-segment%0A  > ac7f657 fix spelling%0A  > 9aa7c11 remove fieldsv1 from upgrade body%0A  > d83ec9e Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > a4b84d8 Validate segments with client-go/dynamic%0A  > 0f4a6cf reset listenersStarted%0A  > 703d15e Update staging/src/k8s.io/client-go/util/csaupgrade/upgrade.go%0A  > cac10a8 dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > 449817f add multithreaded test to shared informer%0A  > 675ca93 refactor if statement%0A  > 46d4284 Merge pull request # 111241 from Abirdcfly/fixtestorsource%0A  > de0b767 remove duplicate test%0A  > cfaca90 address comments%0A  > bdae576 Merge pull request # 112068 from aojea/aojea_client_go%0A  > 9b300de make TestListPager_EachListItem rework%0A  > 0565962 address review comments%0A  > 089614c remove last applied configuration information%0A  > fd22687 add aojea as client-go reviewer%0A  > 5a25eb0 switch listeners to use a map, adapt tests%0A  > efe3789 add more test cases%0A  > 35ead05 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 90c6a46 active remove/add tests for event handlers%0A  > 46dc22f clean up test%0A  > 5291ca2 Bump prometheus/client_golang to v1.13.0%0A  > de4dd3a tests for invalid registration removals%0A  > ced85a8 update godoc%0A  > e6538dd Merge pull request # 112024 from cndoit18/remove-redundant-judgment%0A  > 33eff64 apply desired changes for handler registration%0A  > 049ba69 expose FieldsToSet and SetToFields%0A  > bcd2e6c style: remove redundant judgment%0A  > d73e40f rename handle to registration%0A  > aa892ab remove  unused code%0A  > d5e5863 Merge pull request # 111752 from aanm/revert-final-url-template%0A  > b3a61c6 remove informational informer methods again%0A  > 90ef078 dont expose internal methods in implementatoin%0A  > 5feaced Merge pull request # 67782 from dims/yank-in-tree-openstack-cloud-provider%0A  > e9d4627 client-go/rest: check if url is nil to prevent nil pointer dereference%0A  > ecdc8bf support removal of event handlers from SharedIndexInformers%0A  > c364b63 add function to upgrade managedfields CSA to SSA%0A  > 0fdc4f3 Merge pull request # 111684 from 0xff-dev/master1%0A  > 98e81a7 Remove references to openstack and cinder%0A  > c501ee0 Revert "client-go: remove no longer used finalURLTemplate"%0A  > 4faffa8 Merge pull request # 111564 from inosato/remove-ioutil-from-cli-client-go%0A  > c94a539 use constant NamespaceDefault instead of variable namespace%0A  > 2e40408 Merge pull request # 111918 from liggitt/in-tree-auth%0A  > 27de641 Remove ioutil from client-go%0Abumping golang.org/x/sys 90c8f94...c7a1bf9:%0A  > c7a1bf9 unix: define PerfBitWriteBackward%0A  > 1470852 unix: add SetsockoptTCPMD5Sig on linux%0A  > a6bfb89 unix: use unsafe.Slice in anyToSockaddr%0A  > c10701f windows: use unsafe.Slice in (*RawSockaddrAny).Sockaddr on windows%0A  > 6f25076 unix: define extended TCPInfo on Linux%0A  > 10499f4 unix: add ioctlPtr with unsafe.Pointer arg on other unices (cont)%0A  > 92c4c39 unix: add Dup3 on FreeBSD%0A  > 748af6e unix: pass PROT_MPROTECT(PROT_READ|PROT_WRITE) to initial Mmap on netbsd%0A  > 972870e unix/linux: update to Linux kernel 6.2, glibc 2.37 and Go 1.20.1%0A  > cc0b67d unix: use C.ioctl in generated ioctlPtr%0A  > a3b23cc unix: use SYS_PTRACE in generated ptracePtr%0A  > 71a906e unix/linux: add TUN flags and virtio_net_hdr constants%0A  > 2977c77 unix: add ptracePtr that accepts pointer arg as unsafe.Pointer%0A  > 6877dcc execabs: don't override Go 1.19 error with our error%0A  > b13f40e unix: add ioctlPtr with unsafe.Pointer arg on other unices%0A  > 3b9b58b unix: Faccess: check CAP_DAC_OVERRIDE on Linux%0A  > 2da1413 cpu: get hwcap/auxv from the Go 1.21+ runtime%0A  > 4fee21c windows: Add WSALookupService syscall wrappers%0A  > c79a742 unix: fix a use-after-free bug in PtraceIO on freebsd%0Abumping golang.org/x/net 8e2b117...dfa2b5d:%0A  > dfa2b5d go.mod: update golang.org/x dependencies%0A  > 8c4ef2f hmtl: add security section to package comment%0A  > 1d46ed8 html: have Render escape comments less often%0A  > 569fe81 html: add "Microsoft Outlook comment" tests%0Abumping knative.dev/networking e5d04e8...b9dd5c2:%0A  > b9dd5c2 upgrade to latest dependencies (# 816)%0A  > 68947c5 upgrade to latest dependencies (# 815)%0A  > 14a2bd4 Move `pkg/certificates` from `control-protocol` to `networking` (# 802)%0A  > 2daa483 Update community files (# 813)%0A  > 0dbe4f9 upgrade to latest dependencies (# 812)%0A  > 2a2f7d2 upgrade to latest dependencies (# 810)%0A  > fcbedad Update community files (# 809)%0A  > a44b093 upgrade to latest dependencies (# 808)%0A  > 7c2f7ac upgrade to latest dependencies (# 807)%0A  > 33636d9 Backward compatibility for InternalEncryption (# 806)%0A  > 77975a1 Add the new certificate names for dataplane and controlplane (# 804)%0A  > c3cca43 upgrade to latest dependencies (# 803)%0A  > 3f4627e Add internal trust flag to config (# 778)%0A  > 02055c8 Update community files (# 801)%0A  > 68725bd upgrade to latest dependencies (# 798)%0A  > 1594abb Update community files (# 797)%0Abumping github.com/fsnotify/fsnotify 0f4b979...5f8c606:%0A  > 5f8c606 Update ChangeLog%0A  > 8878587 Tweak the docs a bit%0A  > 89b4cf1 Add test for re-adding a renamed file (# 508)%0A  > 85acde2 Update x/sys%0A  > 69c24b0 Update x/sys%0A  > fb07f82 Add test to see what happens if you watch a symlink (# 498)%0A  > 666da9c Clarify doc comment on WatchList() (# 499)%0A  > 123e4e3 Add note about README version%0A  > 61a05ce Update documentation and examples (# 496)%0A  > e180a87 Move some inotify-tests to run on all backends; test that state is cleaned up after Remove (# 494)%0A  > fdf41a3 Move some files around%0A  > 844d71f Port minor test changes from fen-v2 branch; make LICENSE text not ugly%0A  > 5b87f50 windows: simplify a bit (# 493)%0A  > 2bfaa00 all: add Watcher.{sendEvent,sendError} (# 492)%0A  > 8ab3b84 kqueue: don't set up watchers on unreadable files (# 479)%0A  > a4bcdf8 Update changelog%0A  > 4b43fad kqueue: remove timeout from unix.Kevent() (# 480)%0A  > a24f78c windows: test symlinks (# 491)%0A  > f45391f windows: run TestWatchRename/rename_overwriting_existing_file (# 490)%0A  > ee33a65 Use "os.Rename()" in tests instead of "mv"%0A  > 9dd0568 cmd/fsnotify: fix time.Format() string%0A  > 5dcbfba windows: replace syscall with golang.org/x/sys/windows%0A  > 1f8edaf windows: replace "e" with "err" for error variables%0A  > 99715ba windows: increase buffer size from 4K to 64K (# 485)%0A  > a5c5815 ci: update to use Go 1.19, kick off fewer builds, update x/sys (# 484)%0A  > f2d35c3 Remove CLA section in contributing%0A  > 4604469 Need Linux 5.9 for a useful fanotify we can use%0A  > a566bb1 Update CONTRIBUTING.md%0A  > 01dfc6f Remove PULL_REQUEST_TEMPLATE%0A  > a58e868 Run tests in illumos (# 481)%0A  > 666c6a0 Update ChangeLog%0A  > 928895c [bugfix] close handle when remWatch open in getIno (# 288)%0A  > f174f95 windows: update watch paths when renaming directories with sub-watches (# 370)%0A  > 87dc1fa Rewrite tests (# 478)%0A  > 57e6a49 Add {Event,Op}.Has() (# 477)%0A  > 39823aa Document that /proc and /sys won't work%0A  > 60fbf57 Clarify FAQ on goroutines%0A  > ca0e2f4 macos: retry if open() returns EINTR (# 475)%0A  > ff39bb4 Fix lint (# 476)%0A  > 421f529 debian 6 test: deal with multiple packages (# 474)%0A  > a3256ef Remove AUTHORS file%0A  > 0e78fa6 Update README: split out FAQ to "Platform-specific notes"%0A  > 1a7b6ef inotify: don't ignore events for files that don't exist (# 470)%0A  > f0aceb2 Tweak comment regarding relative paths (# 466)%0A  > d9c9fa5 Add cmd/fsnotify (# 463)%0A  > cc15908 kqueue: better error if watching a file fails (# 471)%0A  > c4e64e4 Replace Use of Kthread-blocking Epoll with Poller Read, Remove Per-Event LStats on Linux # 433 (# 434)%0A  > 4b8b298 Test some more things in CI (# 469)%0A  > 548b8fb Add missing changelog for 1.4.{8,9} (# 468)%0A  > 7fe2936 inotify: fix race in Close() (# 465)%0A  > 35b6378 Clarify README on network drives (# 467)%0A  > e56409e Update link to CONTRIBUTING in the README (# 464)%0A  > 4678dfd Update documentation for linux systems (max_user_watches) (# 287)%0A  > 808f582 bump up GitHub Actions (# 461)%0A  > 4193dfd Do not suppress Chmod on non-existent file (# 260)%0A  > 6ae56b7 kqueue: Make watcher.Close() O(n) instead of O(n^2) (# 233)%0A  > adf5320 strings.Builder instead of bytes.Buffer (# 285)%0A  > 217e78e Explicit mutext (un)locking (# 462)%0A  > 1a4f949 Use common error when removing an unwatched file (# 460)%0A  > 5acfdc1 windows: protect access to isClosed with mutex (# 454)%0A  > c56cafd Test Go 1.18%0A  > 37badf6 This project is archived (# 459)%0Abumping golang.org/x/term d974fe8...0edf009:%0A  > 0edf009 go.mod: update golang.org/x dependencies%0Abumping knative.dev/hack f591fea...fc42790:%0A  > fc42790 Update community files (# 296)%0A  > d7586a2 Update e2e kntest link (# 295)%0A  > a861c8e Update community files (# 294)%0A  > 5b7907f Update actions (# 289)%0A  > c133d5d Install Istio for tests (# 291)%0A  > 5812c57 Update community files (# 292)%0A  > 7d81248 Update community files (# 286)%0A  > 6e4569c Update community files (# 285)%0Abumping github.com/matttproud/golang_protobuf_extensions c182aff...c182aff:%0Abumping golang.org/x/text 71a9c9a...9db913a:%0A  > 9db913a go.mod: update to newer x/tools%0A  > 30dadde all: correct comment typos%0Abumping k8s.io/api 88912e3...6b24792:%0A  > 6b24792 Update dependencies to v0.26.5 tag%0A  > 37e98ba Merge pull request # 117814 from kerthcet/automated-cherry-pick-of-# 117802-upstream-release-1.26%0A  > 7ff025f Update podFailurePolicy comments from alpha-level to beta%0A  > c9f384e Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > c00f1ad Bump runc go module v1.1.4 -> v1.1.6%0A  > 4c28c5a Merge pull request # 117323 from dddddai/automated-cherry-pick-of-# 117182-upstream-release-1.26%0A  > 9483bbc use case-insensitive header keys for http probes%0A  > 0545f3a Merge pull request # 116081 from pohly/automated-cherry-pick-of-# 115928-origin-release-1.26%0A  > e92d7e9 api: generated files%0A  > 16f23da api: drop Resources.Claims from PVC and PVC template%0A  > 5fd8a44 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 1b65b64 Update golang.org/x/net to v0.7.0%0A  > 2e857c1 Merge pull request # 115400 from pohly/automated-cherry-pick-of-# 115354-origin-release-1.26%0A  > 1c6bd70 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 50d0b42 dynamic resource allocation: avoid apiserver complaint about list content%0A  > 045c7fe Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 07a9cbc Merge pull request # 114617 from JoelSpeed/automated-cherry-pick-of-# 114585-upstream-release-1.26%0A  > 52655b9 Resource claims should be a map type%0A  > 07ac8fe Merge remote-tracking branch 'origin/master' into release-1.26%0A  > 566ee01 Update golang.org/x/net 1e63c2f%0A  > b966dc9 sync: update go.mod%0A  > 053624e Merge pull request # 111023 from pohly/dynamic-resource-allocation%0A  > 3590eda Merge pull request # 113375 from atiratree/PodHealthyPolicy-api%0A  > 8356158 api: update testdata%0A  > 5cb3202 Merge pull request # 113186 from ttakahashi21/KEP-3294%0A  > 5a4f9a5 generated%0A  > 78799a8 api: generated files%0A  > dfd6ea2 Generate code%0A  > 993c43c api: add UnhealthyPodEvictionPolicy for PDBs%0A  > ef72ea9 api: dynamic resource allocation API%0A  > d8ab3fb Add API and validation for CrossNamespaceVolumeDataSource%0A  > af772fc api: add resource claims to core API%0A  > 7beaa08 Merge pull request # 112744 from pwschuurman/statefulset-slice-impl%0A  > d7d25c8 Merge pull request # 113360 from mimowo/handling-pod-failures-beta-enable%0A  > f46cd33 Undo unintentional documentation comment change%0A  > f967e44 Merge pull request # 113485 from MikeSpreitzer/apf-borrowing%0A  > 11620b8 Enable the feature into beta%0A  > 6ae95de Fix typo in function emptyInvariants()%0A  > 34f4a52 apiserver: update API testdata at HEAD for flowcontrol%0A  > 3928298 Rebasing feature branch%0A  > e91ffd8 apiserver: add generated files for borrowing in flowcontrol%0A  > d961983 Update doc comments and change name of feature gate%0A  > fcd0d56 apiserver: add fields for borrowing in apf flowcontrol%0A  > adddac7 Small updates and comment fixes%0A  > 98c1aa6 Merge pull request # 113314 from cici37/celIntegration%0A  > 0d02273 Update generated protobuf files%0A  > 3f61c95 Merge pull request # 113688 from dashpole/update_utils%0A  > 8a0a045 API - make update%0A  > a5e7c66 Adding implementation of KEP-3335, StatefulSetSlice%0A  > 72a29bf Merge pull request # 113500 from kerthcet/feat/graduate-nodeInclusionPoplicy-to-beta%0A  > 2a2f510 update k8s.io/utils to fix util tracing panic%0A  > 891a1f8 Adding new api version of admissionregistration.k8s.io v1alpha1 for CEL in Admission Control%0A  > ee30dcf Merge pull request # 113047 from everpeace/improve-supplemental-groups-description%0A  > 2482389 Feat: graduate NodeInclusionPolicy to beta%0A  > a489930 Rename copy to v1alpha1%0A  > 9a33ad3 Merge pull request # 112360 from mimowo/handling-pod-failures-beta-kubelet%0A  > c4b2250 Improve the description of PodSecurityContext.SupplementalGroups (including cri-api)%0A  > 358a069 Copy over admissionregistration v1 to v1alpha1%0A  > 6c616e1 Merge pull request # 113510 from alculquicondor/finalizers-stable%0A  > 5210e2f Add pod disruption conditions for kubelet initiated failures%0A  > 2025045 Merge pull request # 113351 from andrewsykim/endpointslice-terminating-ga%0A  > aa2b4eb Graduate JobTrackingWithFinalizers to stable%0A  > 4bad656 Merge pull request # 113274 from Huang-Wei/kep-3521-A%0A  > aa9d0a7 k8s.io/api/discovery: remove API docs referencing EndpointSliceTerminatingCondition feature gate%0A  > 91f2496 Merge pull request # 113496 from avoltz/anvoltz/ga-itr%0A  > 686871f Automated codegen%0A  > c865c5c Promote ServiceInternalTrafficPolicy to GA%0A  > bd25e4f APIs, Validation and condition enforcements%0A  > 5448eb3 Merge pull request # 106242 from thockin/revive-copy-lb-status-type-to-ingress%0A  > edbfe77 Copy LoadBalancerStatus from core to networking%0A  > 6892570 Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > c5dc3f4 Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > 4e8dc44 Merge pull request # 111978 from Jefftree/aggregated-discovery-types%0A  > 72580e4 Add discovery types%0A  > 0184bd8 Merge pull request # 112643 from SergeyKanzhelev/removeDynamicKubeletConfig%0A  > 0f81104 Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > f8118a1 remove DynamicKubeletConfig feature gate from the code%0A  > 370c8f0 Bump golang.org/x/text to v0.3.8%0A  > 3638040 Merge pull request # 112875 from pohly/update-yaml%0A  > 7ecab5c dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 669318b Merge pull request # 112832 from tkashem/apf-prelifecycle-gen%0A  > 2cfef31 apiserver: prerelease-lifecycle-gen for flowcontrol%0A  > 3cedfad Merge pull request # 112306 from tkashem/v1beta3%0A  > 3814236 Merge pull request # 112707 from enj/enj/i/https_links%0A  > 418dd97 add testdata for flowcontrol v1beta3%0A  > ba008c5 Use https links for k8s KEPs, issues, PRs, etc%0A  > c96c62f rename assuredConcurrencyShares for flowcontrol v1beta3%0A  > be233f8 Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 51a3f54 add patch annotations to flowcontrol v1beta3%0A  > ca5be1f Update to latest k8s.io/utils to pick up changes%0A  > 7e203ee apiserver: generate for apf v1beta3%0A  > 79091da Merge pull request # 112577 from andrewsykim/feature-gate-cleanup%0A  > 19d0ef4 apiserver: enable v1beta3 for apf%0A  > 052d63f Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 1f28922 remove +featureGate=LoadBalancerClass tag in service.spec.loadBalancerClass%0A  > f50a5b7 apiserver: apf rename copy to v1beta3%0A  > 9df3db1 updated etcd to v3.5.5 and newer otel libraries as well%0A  > bed6431 apiserver: copy apf v1beta2 to v1beta3%0A  > c98ebf1 Merge pull request # 112487 from liggitt/flowcontrol-test%0A  > 5c9e17a Add compatibility fixtures for v1beta2 flowcontrol%0A  > 9842651 Merge pull request # 111333 from flant/selfsubjectattributesreviews%0A  > 43df43b Add auth API to get self subject attributes%0A  > 30ff991 Merge pull request # 112349 from pohly/klog-update%0A  > e6114e9 build: update to klog v2.80.1%0A  > 929c3f0 Merge pull request # 112301 from aojea/ipv6_rfc3849%0A  > a687cab use IPv6 Address Prefix Reserved for Documentation for api docs%0A  > 6dd661f Merge pull request # 112199 from pohly/klog-update%0A  > 8a7d12c dependencies: update to klog v2.80.0%0A  > a6ff7c9 Merge pull request # 112146 from kerthcet/feat/move-schedulerError-to-api%0A  > ab89e44 Move constant schedulerError in scheduler to v1 package%0A  > d104994 Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 15b6dd2 Bump prometheus/client_golang to v1.13.0%0A  > 3be0a3c Merge pull request # 111974 from liggitt/1-25-compatibility%0A  > 49e055e Merge pull request # 111830 from t1anz0ng/typo%0A  > fcc83cd Drop 1.23 compatibility data%0A  > 64f80bd Merge pull request # 111611 from kardashov/ref-spec-docs-typo-fix%0A  > ea5df3a fix(typo): remove extra " from autoscaling doc string%0A  > 4cde1ad Add 1.25 compatibility data%0A  > 2e7b661 Merge pull request # 111657 from aojea/hc_nodeport%0A  > d07af88 Generate specs after fixing typo in documentation%0A  > 649256a Fix typo in field description.%0Abumping knative.dev/serving 2c1bb07...32ec382:%0A  > 32ec382 Drop unused ytt patch for Ingress ServiceType (# 14143)%0A  > 4c3b36c Update net-gateway-api nightly (# 14136)%0A  > 9a75a93 Update net-istio nightly (# 14132)%0A  > ca618b7 Update net-certmanager nightly (# 14131)%0A  > ea3e9c3 Update net-contour nightly (# 14130)%0A  > 2e7d6e4 Update community files (# 14128)%0A  > 63fa389 Allow to set QP resources per service (# 14038)%0A  > 9310e4d Update net-kourier nightly (# 14125)%0A  > 0462ce6 Update net-istio nightly (# 14126)%0A  > 2813b9a Update net-gateway-api nightly (# 14119)%0A  > eaf666e Update net-istio nightly (# 14116)%0A  > 53169cd Update net-istio nightly (# 14112)%0A  > e865aa7 Update net-contour nightly (# 14109)%0A  > 921daf8 Update net-certmanager nightly (# 14111)%0A  > bb581cc Update net-kourier nightly (# 14110)%0A  > fbfffc0 upgrade to latest dependencies (# 14108)%0A  > bcf9274 upgrade to latest dependencies (# 14101)%0A  > f085b30 fix: requests are sent to all pods even if cc=1 and the parity of activatorCount and podTracker is different (# 14022)%0A  > 9772417 Update net-kourier nightly (# 14107)%0A  > f6d0c7b Update net-contour nightly (# 14106)%0A  > 560e0ea Update net-certmanager nightly (# 14105)%0A  > 51f4f1e Update net-istio nightly (# 14104)%0A  > 18519b1 Update net-contour nightly (# 14079)%0A  > 38c155e Add chainguard-dev/actions for creating kind cluster (# 14018)%0A  > 74c57d8 Update net-istio nightly (# 14098)%0A  > 5a9c574 Update net-kourier nightly (# 14096)%0A  > 3a6c2b6 upgrade to latest dependencies (# 14095)%0A  > 5a90438 Update net-istio nightly (# 14091)%0A  > dc0692a Update net-istio nightly (# 14088)%0A  > 0fbd780 Update net-certmanager nightly (# 14087)%0A  > 6f63c98 Update net-kourier nightly (# 14086)%0A  > e74f5f4 Update net-gateway-api nightly (# 14085)%0A  > 1587070 Update net-kourier nightly (# 14081)%0A  > 2e00e9f Update net-certmanager nightly (# 14080)%0A  > a3c7864 Update net-istio nightly (# 14078)%0A  > 384b889 Update net-gateway-api nightly (# 14077)%0A  > 7d0f963 Change storage version of DomainMapping to v1beta1 (# 14058)%0A  > e8b6f05 Update net-gateway-api nightly (# 14068)%0A  > 41e4212 Get certificate reconciler from `networking` instead of `control-protocol` (# 14072)%0A  > e71b933 Update net-certmanager nightly (# 14070)%0A  > 8f516b6 Update net-kourier nightly (# 14069)%0A  > a2bb4aa upgrade to latest dependencies (# 14071)%0A  > c95f17b Update community files (# 14067)%0A  > bf48e64 Remove deprecated internalEncryption dependency (# 14064)%0A  > 6b87d67 Update net-istio nightly (# 14065)%0A  > fbecf34 refactor throttler_test.go (# 14055)%0A  > 349b2d6 Change minimum TLS version to 1.3 for internal encryption (between activator and queue-proxy) (# 13887)%0A  > d07bf78 Update net-contour nightly (# 14049)%0A  > aa023e8 Update net-istio nightly (# 14048)%0A  > 8fc4bb9 Update net-gateway-api nightly (# 14047)%0A  > 135be30 Update net-certmanager nightly (# 14046)%0A  > 8da71b5 Update net-kourier nightly (# 14042)%0A  > 13a4e46 poll until timeout - don't error out if the deployment can't be found (# 14027)%0A  > 31c2b7e upgrade to latest dependencies (# 14043)%0A  > 6a6e417 Update net-istio nightly (# 14041)%0A  > 807fc2c Update net-certmanager nightly (# 14040)%0A  > 3c23945 drop safe to evict annotations (# 14035)%0A  > fca5c14 Update net-gateway-api nightly (# 14033)%0A  > c12c917 Update net-contour nightly (# 14034)%0A  > 2da856d Update net-kourier nightly (# 14032)%0A  > d7c8779 Update net-certmanager nightly (# 14031)%0A  > aaf01dc Update net-istio nightly (# 14030)%0A  > bdaa436 RandomChoice 2 policy wasn't random when the number of targets is 2 (with equal weight) (# 14028)%0A  > c91f8c4 Fix metrics reporting period (# 14019)%0A  > 9f60969 Update net-kourier nightly (# 14004)%0A  > 6020cec Update net-istio nightly (# 14025)%0A  > 88cae7f Update net-gateway-api nightly (# 14016)%0A  > a143bf8 Update net-contour nightly (# 14015)%0A  > c2be582 Update net-certmanager nightly (# 14014)%0A  > 3450f0a upgrade to latest dependencies (# 14013)%0A  > 35cfd8f [Automated] Update net-gateway-api nightly (# 14003)%0A  > 08a9708 Update net-istio nightly (# 14009)%0A  > 5074b4c Update net-contour nightly (# 14010)%0A  > e8cb343 upgrade to latest dependencies (# 13999)%0A  > 1261074 Update net-certmanager nightly (# 14002)%0A  > f987ca6 Bump kind to 0.19 (# 14008)%0A  > fbb7fa1 Update community files (# 13998)%0A  > bff1d80 Remove 1.24 kind version (# 14007)%0A  > a657321 Update net-kourier nightly (# 13993)%0A  > d75b0f0 Update net-contour nightly (# 13990)%0A  > 6d26f54 upgrade to latest dependencies (# 13991)%0A  > df5001f Update net-certmanager nightly (# 13992)%0A  > 2594084 upgrade to latest dependencies (# 13989)%0A  > 7c303fa Update cluster-version to 1.25 (# 13988)%0A  > 9e751a2 Update net-certmanager nightly (# 13974)%0A  > 7b35cfb upgrade to latest dependencies (# 13987)%0A  > 99800ed Set default domain to cluster's domain (# 13964)%0A  > c90fabf Metric annotations work with global class config (# 13978)%0A  > da31cd1 Update net-kourier nightly (# 13975)%0A  > f457924 Update net-contour nightly (# 13976)%0A  > 14ad4d1 upgrade to latest dependencies (# 13973)%0A  > 00ddfd9 Update net-kourier nightly (# 13972)%0A  > fc63583 Update net-kourier nightly (# 13966)%0A  > 219285e Update net-kourier nightly (# 13959)%0A  > 2fa05bd Min TLS for tag to digest defaults to 1.2 again and is configurable (# 13962)%0A  > 43df348 Update net-contour nightly (# 13958)%0A  > 50a9f22 Update net-certmanager nightly (# 13961)%0A  > 4e379cb Update net-gateway-api nightly (# 13957)%0A  > 3d53294 Update net-istio nightly (# 13960)%0A  > ea2a6c8 :lipstick: Install ko using setup-ko, from ko-build (# 13951)%0A  > e5070cd upgrade to latest dependencies (# 13950)%0A  > 9778f2d Update net-istio nightly (# 13949)%0A  > f27ba4e Update net-certmanager nightly (# 13944)%0A  > 2840301 Update net-kourier nightly (# 13945)%0A  > 117a642 Update net-gateway-api nightly (# 13943)%0A  > 84a2230 Update net-contour nightly (# 13942)%0A  > 7aa5edb upgrade to latest dependencies (# 13941)%0A  > 01707d8 upgrade to latest dependencies (# 13940)%0A  > b7d5e8d Update net-istio nightly (# 13939)%0A  > 5e056a0 Update net-certmanager nightly (# 13926)%0A  > 35efd12 Update net-contour nightly (# 13929)%0A  > f476717 Update net-istio nightly (# 13935)%0A  > bd8e37c Update net-gateway-api nightly (# 13925)%0A  > 37a7010 Update net-kourier nightly (# 13934)%0A  > f47802d Update community files (# 13933)%0A  > 990d701 Update net-kourier nightly (# 13928)%0A  > ff9f03d Update net-istio nightly (# 13927)%0A  > 690c525 upgrade to latest dependencies (# 13924)%0A  > 1dd07a7 Update community files (# 13923)%0A  > 66141b8 Update net-istio nightly (# 13920)%0Abumping knative.dev/eventing 034bec9...f5b1b12:%0A  > f5b1b12 Send namespace header in MT components (# 7048)%0A  > 4b5fde8 [main] Update community files (# 7043)%0A  > 8f74094 Add handler to auto create Event Types (# 7034)%0A  > 901ef61 Remove check for empty Namespace on resolver (# 7040)%0A  > 95cdbaa We should not limit the EventType creation from the Sources Duck to just brokers (# 7032)%0A  > 7429761 Adjust the Namespace reference to the one from the parent (# 7035)%0A  > cb2a891 update the redeployment script (# 7038)%0A  > ab01938 [main] Upgrade to latest dependencies (# 7025)%0A  > c9dcaf3 Added basic gc loop to kncloudevents clients map (# 6997)%0A  > d6cf96d EventType works with channel (# 7023)%0A  > 365d0b0 Run TLS e2e tests only when Istio is not enabled (# 7029)%0A  > 825a237 Update IMC CRD addressstatus to include `.name` and `.CACerts` fields (# 7026)%0A  > 3190df7 Tracking/reconcile KResource references (# 7014)%0A  > 0f68861 Rename more to Resource, instead of broker (# 7022)%0A  > bccb7d4 Better reflecting the lifecycle of event type … (# 7019)%0A  > 49d4acd Skip ping source TLS rekt test, since extremely flaky (# 7016)%0A  > 8719e18 [main] Upgrade to latest dependencies (# 7012)%0A  > e5ae717 Use HTTP POST when terminating istio proxy (# 7015)%0A  > fea730f Only check if the reference does exist (# 7010)%0A  > 631f4ec Add TLS support for mt-broker-filter (# 6940)%0A  > 45f0a19 Allow wathola components to run with Istio  (# 7011)%0A  > 65f4b1c [main] Format Go code (# 7008)%0A  > 3267b1a test SinkBinding with eventshub TLS receiver as sink (# 6979)%0A  > aad53f4 Updated eventingtls test certs to support IP addresses (# 7006)%0A  > 57d78e0 [main] Update community files (# 7004)%0A  > dfb2243 Support TLS in Trigger and Channel reconciler (# 6988)%0A  > df08b49 Eventing TLS: verify APIServerSource and PingSource sinkURI is https (# 6987)%0A  > d21c1aa [main] Upgrade to latest dependencies (# 6989)%0A  > 70113e8 Deprecate broker field and use KReference for the broker instead (# 6870)%0A  > 4e4647f test update to newest version (# 6990)%0A  > 870ac6b Update MessageDispatcher and FanoutMessageHandler to support sending events to TLS endpoints (# 6983)%0A  > 6dd5d58 Test PingSource with eventshub TLS receiver as sink (# 6965)%0A  > 55f4f28 [main] Upgrade to latest dependencies (# 6982)%0A  > 2a5a9a5 Add more items in the development getting started documentation (# 6978)%0A  > 59118a0 imc-dispatcher starts a TLS server, accepts host based routing on http receiver and path based routing on https receiver (# 6954)%0A  > ee49ada Rework kncloudevents library to support multiple clients (# 6975)%0A  > ee88094 Make ServerManager independent from kncloudevents package (# 6980)%0A  > 6a11c5f [main] Upgrade to latest dependencies (# 6969)%0A  > 8a9a532 Updated DEVELOPMENT.md to provide better instructions on setting up kubernetes (# 6977)%0A  > 390a0c8 Eventing TLS: Test ContainerSource with eventshub TLS receiver as sink (# 6957)%0A  > 5e245ac Fix flaky PingSource TLS unit test (# 6970)%0A  > f9f27c9 Use random names in Channel tests (# 6967)%0A  > d4609a5 Do not parse flags in InitializeEventingFlags (# 6966)%0A  > ef68a0a [main] Update community files (# 6968)%0A  > 4adc287 Add transport-encryption prerequisite for Addressable tests (# 6964)%0A  > deb0ef4 Add field for subscribers & replys CA certs to `SubscriberSpec` and `SubscriptionStatusPhysicalSubscription` (# 6959)%0A  > b81082c Eventing TLS: Test ApiServerSource with eventshub TLS receiver as sink (# 6956)%0A  > cdff269 Adding source duck type to v1b2 (# 6962)%0A  > b47b4ec [main] Upgrade to latest dependencies (# 6958)%0A  > 3315c20 Provide Channels CACerts in Brokers status annotation (# 6952)%0A  > 4b9fdef [main] Upgrade to latest dependencies (# 6955)%0A  > da31970 Improve cert-manager resources for Eventing TLS certs provisioning (# 6953)%0A  > fc5befb Provide subscribers CACerts in triggers status (# 6951)%0A  > 1efab19 Using v1b2 in the reconciler (# 6949)%0A  > c44671c Updating rekt test resources for EventType v1b2 (# 6946)%0A  > e31eb1f Adding testingv1b2 for eventtype (# 6944)%0A  > a9908ef Support TLS in PingSource (# 6929)%0A  > df559c0 Fix typo in flags.IsDisbledTransportEncryption name (# 6941)%0A  > 7073cc9 [main] Upgrade to latest dependencies (# 6939)%0A  > c6bc9bb Eventing TLS: Support K_CA_CERTS env variable injection for SinkBinding subjects (# 6931)%0A  > 24fbfe5 Eventing TLS: support exposing https address in Broker controller (# 6930)%0A  > d18cb42 Add information about retryable error in servermanager (# 6921)%0A  > f92a05b Added Support for K_CA_CERTS in the heartbeats (# 6920)%0A  > b8b43d0 Remove CA certs empty and non nil check, use URL scheme only (# 6928)%0A  > 3c8cc05 Return error directly if one receiver of servermanager fails (# 6919)%0A  > 92ab7f8 [main] Upgrade to latest dependencies (# 6927)%0A  > 5c6fe57 two more for reducing to debug, instead of info (# 6922)%0A  > 6cf9397 less verbose logs on scheduler component  (# 6912)%0A  > 69918f2 Adds ServerManager. Supports http/https message receivers (# 6908)%0A  > d58e259 Install ko using setup-ko in kind e2e tests (# 6910)%0A  > 9cdea5d Eventing TLS: Added Support for setting K_CA_CERTS in the ApiServerSource controller for the adapter (# 6897)%0A  > add8436 Eventing TLS: support exposing https address in InMemoryChannel controller (# 6881)%0A  > 59cfb6d [main] Upgrade to latest dependencies (# 6906)%0A  > 03f2a3d Remove unused test helper (# 6907)%0A  > 7a90c46 Remove eventing-natss from downstream tests (# 6905)%0A  > ba2550b [main] Upgrade to latest dependencies (# 6904)%0A  > 999eead More EventType v1beta2 work (# 6903)%0A  > 66e8257 Remove sanitize HTTP body for `knativeerrordata` extension (# 6902)%0A  > cd50d27 [main] Format Go code (# 6898)%0A  > 0f0a82c [main] Update community files (# 6901)%0A  > 7f4deb5 EventType v1b2 API addition (# 6893)%0A  > 1f917d0 Refactor PingSource adapter client creation (# 6880)%0A  > e2f1c77 [main] Update community files (# 6896)%0A  > 6a5c7ee Eventing TLS: migrate all resolver.URIResolver usages over to AddressableFromDestinationV1 (# 6883)%0A  > 0a12a6c Adds path based routing to message_receiver pkg (# 6873)%0Abumping github.com/prometheus/client_golang 64435fc...254e546:%0A  > 254e546 Merge pull request # 1162 from kakkoyun/cut-1.14.0%0A  > 07d3a81 Merge pull request # 1161 from prometheus/release-1.13%0A  > c8a3d32 Cut v1.14.0%0A  > 870469e Test and support 1.19 (# 1160)%0A  > 53e51c4 Merge pull request # 1157 from prometheus/cut-1.13.1%0A  > b785d0c Fix go_collector_latest_test Fail on go1.19 (# 1136)%0A  > 79ca0eb Added tip from Björn + Grammarly.%0A  > 4d54769 Fix float64 comparison test failure on archs using FMA (# 1133)%0A  > 078f11f Cut 1.13.1 release (+ documenting release process).%0A  > 5f202ee Merge pull request # 1150 from prometheus/sparsehistogram%0A  > ddd7f0e Fix race condition with Exemplar in Counter (# 1146)%0A  > 0859bb8 Merge pull request # 1152 from jessicalins/update-to-custom-reg%0A  > fffb76c Merge branch 'main' into sparsehistogram%0A  > 1f93f64 Fix `CumulativeCount` value of `+Inf` bucket created from exemplar (# 1148)%0A  > 10b0550 Fix race condition with Exemplar in Counter (# 1146)%0A  > a340ca4 Run make format%0A  > e92a8c7 Avoid the term 'sparse' where possible%0A  > 8cc2b6c Fix double-counting bug in promhttp.InstrumentRoundTripperCounter (# 1118)%0A  > dcea97e Fix `CumulativeCount` value of `+Inf` bucket created from exemplar (# 1148)%0A  > 6056615 Update random example to use custom registry%0A  > d31f13b Add SparseBucketsZeroThresholdZero and groom doc comments%0A  > 9801a4e Examples: Replace deprecated WithGoCollections with WithGoCollectorRuntimeMetrics (# 1130)%0A  > 0b7f488 Update simple example to use custom registry%0A  > 58a8ca4 examples: Adjust doc comment for native histograms%0A  > 7c46c15 Clarify documentation around what constructors do (# 1125)%0A  > 9b5c5b8 Update basic example to use custom registry%0A  > 4e71e6f Update prometheus/client_model dependency%0A  > 83d56b1 Extend prometheus.Registry to implement Collector (# 1103)%0A  > 111fae1 Merge branch 'main' into sparsehistogram%0A  > 4c41dfb Clarify exemplar(Add|Observe) by renaming to (add|observe)WithExemplar (# 1122)%0A  > 25bc188 Merge pull request # 1144 from prometheus/beorn7/histogram2%0A  > f73e3cc Fix double-counting bug in promhttp.InstrumentRoundTripperCounter (# 1118)%0A  > 95cf173 Merge branch 'main' into sparsehistogram%0A  > 6942f9e sparse buckets: Fix handling of +Inf/-Inf/NaN observations%0A  > c7aa2a5 Merge pull request # 1113 from prometheus/release-1.13%0A  > ec86ef1 Merge pull request # 1092 from prometheus/beorn7/histogram%0A  > 1e61b8e Update common Prometheus files (# 1111)%0A  > 6141a07 Merge branch 'main' into sparsehistogram%0A  > 8cbcd40 histograms: Move to new exposition protobuf format%0A  > 5a321c7 Merge branch 'foo-commit' into sparsehistogram%0A  > e93e384 Merge branch 'beorn7/release' into sparsehistogram%0A  > e203144 Merge branch 'release-1.12' of github.com:prometheus/client_golang into release-1.12%0A  > 525d042 Merge branch 'main' into sparsehistogram%0A  > a516626 Merge branch 'release-1.12' into beorn7/release%0A  > a27b6d7 Fix conflicts%0A  > 6ba7871 Merge branch 'main' into sparsehistogram%0A  > eb59a7b Histogram: Fix bug with negative schemas (# 1054)%0A  > b237230 Merge branch 'main' into sparsehistogram%0A  > 294cca4 Merge branch 'main' into sparsehistogram%0A  > 70253f4 Fix typo in doc comment%0A  > 5b19c55 Merge branch 'master' into sparsehistogram%0A  > dfbcc28 Merge pull request # 901 from prometheus/beorn7/histogram%0A  > 84fcaff Merge branch 'master' into sparsehistogram%0A  > 263be8d Refactoring of sparse histograms%0A  > 9ef5f90 Allow a zero threshold of zero%0A  > 2409960 Implement strategy to limit the sparse bucket count%0A  > aa6f67a Add TODO about bucket search optimization%0A  > 43f31c2 Merge pull request # 886 from prometheus/beorn7/histogram%0A  > 5aa8534 Merge branch 'master' into sparsehistogram%0A  > 5142344 Pin client_model to the most recent sparsehistogram commit%0A  > 97eb041 Tidy go.sum%0A  > 6c4e0ef Add tests for sparse histogram%0A  > 553ed73 Fix lint warning%0A  > 31318b7 Switch to base-2 buckets%0A  > b7a540a Fix test%0A  > a9df0ba Update prometheus/client_model%0A  > ce36ee3 Merge branch 'master' into beorn7/histogram%0A  > d698336 Merge branch 'master' into beorn7/histogram%0A  > 08104a0 Minor doc comment fixes%0A  > a9d0066 Add note about pow-of-10 precision issue%0A  > d1f5366 Fix span offset%0A  > abe540f Encode sparse histograms in protobuf%0A  > c98db4e Demo sparse histograms%0Abumping knative.dev/pkg dfad48e...6eb4b40:%0A  > 6eb4b40 Update community files (# 2760)%0A  > eb63a40 Support to set qps and burst via env variable (# 2755)%0A  > 74c4be5 Generate kresource duck type codegen (# 2754)%0A  > 4dbc312 fix boilerplate (# 2753)%0A  > 15605c7 Defaulting Controller options for all kind of webhooks (# 2738)%0A  > 94b81fc Update community files (# 2752)%0A  > 5671699 drop the dynamic type (# 2750)%0A  > 9bda38b Fix some webhook testing tech debt (# 2751)%0A  > ec20442 Update community files (# 2747)%0A  > 05bfcf6 bump k8s dependencies and update min version to v1.25 (# 2745)%0A  > 52ff2ac drop dynamic client wrappers (# 2744)%0A  > a170a07 Eventing TLS: validate that Destination.CACerts is a PEM encoded cert (# 2743)%0A  > dfb4bf0 Drop dynamic wrapper injection code generation (# 2742)%0A  > db8a353 Add SinkCACerts to SourceStatus (# 2733)%0A  > 9049667 Update community files (# 2735)%0A  > aacec7f Update community files (# 2734)%0A  > 300df43 Eventing TLS: Added AddressableFromDestination method on the resolver (# 2717)%0Abumping knative.dev/client-pkg 4f052f9...f377f06:%0A  > f377f06 Update community files (# 106)%0A  > b93ceb0 Update community files (# 105)%0A  > 83c91f4 Update community files (# 103)%0A  > e5c405e Update community files (# 102)%0A  > eee9b55 Update community files (# 100)%0Abumping k8s.io/apimachinery 4fbe8e4...b207ce5:%0A  > b207ce5 Merge pull request # 117691 from dims/re-do-of-117242-on-release-1.26%0A  > 917de35 Bump runc go module v1.1.4 -> v1.1.6%0A  > 53ecdf0 Merge pull request # 115787 from liggitt/net-0.7.0-1.26%0A  > 05339fa Update golang.org/x/net to v0.7.0%0A  > eabbfd5 Merge pull request # 115642 from nckturner/pin-golang.org/x/net-to-v0.4.0-in-1.26%0A  > 48b8d1f Pin golang.org/x/net to v0.4.0 in 1.26%0A  > 373a5f7 Merge pull request # 114521 from 3point2/automated-cherry-pick-of-# 113283-upstream-release-1.26%0A  > b5e5df6 Fix SPDY proxy authentication with special chars%0A  > 553a2d6 Improve error message when proxy connection fails%0A  > 5d4cdd2 Merge remote-tracking branch 'origin/master' into release-1.26%0A  > 6cbc4a3 Update golang.org/x/net 1e63c2f%0A  > 6561235 Merge pull request # 113699 from liggitt/manjusaka/fix-107415%0A  > dad8cd8 Update workload selector validation%0A  > fe82462 Add extra value validation for matchExpression field in LabelSelector%0A  > 067949d update k8s.io/utils to fix util tracing panic%0A  > 0ceff90 Merge pull request # 112223 from astraw99/fix-ownerRef-validate%0A  > 9e85d3a Merge pull request # 112649 from howardjohn/set/optimize-everything-nothing%0A  > b0dd9ec Fix ownerRef controller validate err%0A  > b03a432 Merge pull request # 113367 from pohly/dep-ginkgo-gomega%0A  > 88a1448 Rename and comment on why sharing is safe%0A  > 4e6bcdb dependencies: update to gomega v1.23.0 and ginkgo v2.4.0 and dependencies%0A  > 3adc870 Optimize `Everything` and `Nothing` label selectors%0A  > 0524d6c Merge pull request # 112693 from aimuz/fix-GO-2022-0969%0A  > 5a0277f Fixed (CVE-2022-27664) Bump golang.org/x/net to v0.1.1-0.20221027164007-c63010009c80%0A  > 6809593 Merge pull request # 112377 from weilaaa/refactor_sets_use_generic%0A  > 70a38aa Merge pull request # 113106 from pohly/dep-ginkgo-gomega%0A  > f2d9aed refactor sets use generic%0A  > d097f82 dependencies: update to gomega v1.22.1 and ginkgo v2.3.1%0A  > 7b5633b Merge pull request # 112988 from alexzielenski/update-kube-openapi%0A  > b839e82 Merge pull request # 113037 from pacoxu/fsnotify-v1.6.0%0A  > b7d8973 update kube-openapi%0A  > 1dc6ace update fsnotify to v1.6.0%0A  > 78d003c Merge pull request # 112989 from ameukam/bump-golang.org/x/text-to-v0.3.8%0A  > 04898ff Bump golang.org/x/text to v0.3.8%0A  > 79993b2 Merge pull request # 112875 from pohly/update-yaml%0A  > 7379c15 dependencies: update to sigs.k8s.io/yaml v1.3.0%0A  > 66e26ac Merge pull request # 112707 from enj/enj/i/https_links%0A  > 882b67d Use https links for k8s KEPs, issues, PRs, etc%0A  > 7fb78ee Merge pull request # 112472 from ialidzhikov/nit/error-msg%0A  > 826a74e Merge pull request # 112673 from dims/update-to-latest-k8s.io/utils-sep-22%0A  > 22fe889 Improve the error returned from the `LabelSelectorAsSelector` func%0A  > e2f9797 Update to latest k8s.io/utils to pick up changes%0A  > f8159af Merge pull request # 112545 from dims/update-etcd-3.5.5-and-all-otel-related-to-latest%0A  > 612703e Merge pull request # 112352 from pohly/e2e-ginkgo-progress%0A  > 9901884 updated etcd to v3.5.5 and newer otel libraries as well%0A  > 6439059 Merge pull request # 112526 from liggitt/redirect%0A  > 0564b5e e2e: bump ginkgo to v2.2.0%0A  > 2e3bf73 Limit redirect proxy handling to redirected responses%0A  > 6d854d7 Merge pull request # 112349 from pohly/klog-update%0A  > e1e1b7c build: update to klog v2.80.1%0A  > ed93eed Merge pull request # 111768 from weilaaa/feature_add_symmetric_difference_in_sets_string%0A  > 36163c5 Merge pull request # 112193 from jindijamie/master%0A  > b7b9ba4 add symmetric difference in sets%0A  > 31bc292 Merge pull request # 112199 from pohly/klog-update%0A  > 1c318b6 Add an option for aggregator%0A  > 0d0d03e Merge pull request # 111936 from haoruan/bugfix-111928-microtime-marshal-precision%0A  > 145c075 dependencies: update to klog v2.80.0%0A  > 2d64dac Merge pull request # 112089 from zeze1004/fix-typo%0A  > 2187a78 Marshal MicroTime to json and proto at the same precision%0A  > 53c4d51 Merge pull request # 112129 from pohly/e2e-ginkgo-report-after-each%0A  > 30e9977 Fix typo "sturct" to "struct"%0A  > 5e4f25a dependencies: update to ginkgo v2.1.6 and gomega v1.20.1%0A  > 349dcdf Merge pull request # 112052 from tosi3k/bump-client-golang%0A  > 16a7f7a Bump prometheus/client_golang to v1.13.0%0A  > 2b9fe2c Merge pull request # 111808 from alvaroaleman/meta-wrapping%0A  > bb48261 Apimachinery meta errors: Support errors.Is and error wrapping%0Abumping github.com/prometheus/client_model 7bc5445...63fb982:%0A  > 63fb982 Merge pull request # 63 from prometheus/sparsehistogram%0A  > 5c16fa2 Merge pull request # 57 from prometheus/repo_sync%0A  > fdb567d Add note about native histograms to README%0A  > 6b8c742 Update common Prometheus files%0A  > 942d53c Update common Prometheus files%0A  > 7f720d2 Add note about experimental state of native histograms%0A  > f60d1ac Update common Prometheus files%0A  > 1f8dcad Merge pull request # 59 from prometheus/beorn7/histogram%0A  > 6dc836e Merge pull request # 53 from prometheus/repo_sync%0A  > 421ad2b Merge pull request # 58 from prometheus/beorn7/histogram%0A  > a7ff713 Flatten the buckets of native histograms%0A  > 0e1ed89 Merge pull request # 52 from prometheus/repo_sync%0A  > a227486 Update common Prometheus files%0A  > 408689d Merge branch 'master' into sparsehistogram%0A  > 0da3265 Explain Span layout better%0A  > 14ab895 Merge pull request # 51 from prometheus/repo_sync%0A  > bc75c6a Update common Prometheus files%0A  > 61b6c1a Merge pull request # 47 from prometheus/beorn7/histogram%0A  > 8171e83 Add float histograms and gauge histograms to proto spec%0A  > a863571 Merge pull request # 49 from prometheus/repo_sync%0A  > 2fc368c Update common Prometheus files%0A  > 8831f0d Merge branch 'master' into sparsehistogram%0A  > bbaf1cc Switch to base 2 and powers of 2 for resolution%0A  > 675c4e5 Merge pull request # 48 from prometheus/repo_sync%0A  > a3e6551 Update common Prometheus files%0A  > 24db95a Merge remote-tracking branch 'origin/master' into beorn7/histogram%0A  > 147c58e Move .proto file and add caching of protoc and protoc-gen-go during build (# 46)%0A  > 56ab8d9 Update common Prometheus files%0A  > 4b803f3 Experimental encoding for sparse buckets in histogram%0A  > 0255a22 Merge pull request # 43 from roidelapluie/security-dot-md%0A  > 1f48c5c Rename metrics.proto to io_prometheus_client_metrics.proto (# 45)%0A  > 60555c9 Merge pull request # 41 from prometheus/repo_sync%0A  > 1bb3080 Add SECURITY.md%0A  > 1106810 Update common Prometheus files

Signed-off-by: Knative Automation <automation@knative.team>

---
## [DerTimonius/next.js](https://github.com/DerTimonius/next.js)@[6238f8a5c0...](https://github.com/DerTimonius/next.js/commit/6238f8a5c0ffabb7dfb35872c52c942ed7f148da)
#### Monday 2023-07-03 14:18:21 by Jimmy Lai

performance: don't compile on hover on dev (#51830)

An annoying issue that slows down compilation times in dev for Next is
that we might trigger compilation of a page via hover on app.

We do this because we want the same experience in production and dev and
the prefetching is important for instantaneous loading states.

The alternative in this PR is that we don't prefetch at all anymore in
dev but instead, when we handle navigation, we can force a prefetch
navigation.

The slight compromise with this approach is that you can't test
prefetching anymore in dev.


<!-- Thanks for opening a PR! Your contribution is much appreciated.
To make sure your PR is handled as smoothly as possible we request that
you follow the checklist sections below.
Choose the right checklist for the change(s) that you're making:

## For Contributors

### Improving Documentation

- Run `pnpm prettier-fix` to fix formatting issues before opening the
PR.
- Read the Docs Contribution Guide to ensure your contribution follows
the docs guidelines:
https://nextjs.org/docs/community/contribution-guide

### Adding or Updating Examples

- The "examples guidelines" are followed from our contributing doc
https://github.com/vercel/next.js/blob/canary/contributing/examples/adding-examples.md
- Make sure the linting passes by running `pnpm build && pnpm lint`. See
https://github.com/vercel/next.js/blob/canary/contributing/repository/linting.md

### Fixing a bug

- Related issues linked using `fixes #number`
- Tests added. See:
https://github.com/vercel/next.js/blob/canary/contributing/core/testing.md#writing-tests-for-nextjs
- Errors have a helpful link attached, see
https://github.com/vercel/next.js/blob/canary/contributing.md

### Adding a feature

- Implements an existing feature request or RFC. Make sure the feature
request has been accepted for implementation before opening a PR. (A
discussion must be opened, see
https://github.com/vercel/next.js/discussions/new?category=ideas)
- Related issues/discussions are linked using `fixes #number`
- e2e tests added
(https://github.com/vercel/next.js/blob/canary/contributing/core/testing.md#writing-tests-for-nextjs
- Documentation added
- Telemetry added. In case of a feature if it's used or not.
- Errors have a helpful link attached, see
https://github.com/vercel/next.js/blob/canary/contributing.md


## For Maintainers

- Minimal description (aim for explaining to someone not on the team to
understand the PR)
- When linking to a Slack thread, you might want to share details of the
conclusion
- Link both the Linear (Fixes NEXT-xxx) and the GitHub issues
- Add review comments if necessary to explain to the reviewer the logic
behind a change

### What?

### Why?

### How?

Closes NEXT-
Fixes #

-->

link NEXT-1317

---
## [LanceMcCarthy/terminal](https://github.com/LanceMcCarthy/terminal)@[9ccd6ecd74...](https://github.com/LanceMcCarthy/terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Monday 2023-07-03 14:39:43 by Mike Griese

Manually copy trailing attributes on a resize (#12637)

## THE WHITE WHALE

This is a fairly naive fix for this bug. It's not terribly performant,
but neither is resize in the first place.

When the buffer gets resized, typically we only copy the text up to the
`MeasureRight` point, the last printable char in the row. Then we'd just
use the last char's attributes to fill the remainder of the row.

Instead, this PR changes how reflow behaves when it gets to the end of
the row. After we finish copying text, then manually walk through the
attributes at the end of the row, and copy them over. This ensures that
cells that just have a colored space in them get copied into the new
buffer as well, and we don't just blat the last character's attributes
into the rest of the row. We'll do a similar thing once we get to the
last printable char in the buffer, copying the remaining attributes.

This could DEFINITELY be more performant. I think this current
implementation walks the attrs _on every cell_, then appends the new
attrs to the new ATTR_ROW. That could be optimized by just using the
actual iterator. The copy after the last printable char bit is also
especially bad in this regard. That could likely be a blind copy - I
just wanted to get this into the world.

Finally, we now copy the final attributes to the correct buffer: the new
one.  We used to copy them to the _old_ buffer, which we were about to
destroy.

## Validation

I'll add more gifs in the morning, not enough time to finish spinning a
release Terminal build with this tonight.

Closes #32 🎉🎉🎉🎉🎉🎉🎉🎉🎉
Closes #12567

(cherry picked from commit 855e1360c0ff810decf862f1d90e15b5f49e7bbd)

---
## [JeromeFitz/websites](https://github.com/JeromeFitz/websites)@[e927742292...](https://github.com/JeromeFitz/websites/commit/e927742292832b99f43b1e24311943626b415cbb)
#### Monday 2023-07-03 15:37:48 by Jerome Fitzgerald

🧨 (revamp) NICE-43 Next RSC, Notion API, & Tailwind [b] [!] (#1621)

# ⚠️ Please Note

This is a bit bigger than I would want, but this is a complete refactor to better utilize a `Notion CMS` within a `Next 13 App` structure taking advantage of `RSC`. And then for good measure started the migration _back_ to `Tailwind` (but now I think `Stitches|Vanilla Extract` are oaky with Next 13).

✨ NICE-43 revamp Next RSC, Notion API, & Tailwind

BREAKING CHANGE: New Notion Implementation through Next 13 RSC (App)

# Complete Refactor for Next RSC

- [x] Redis KV Cache
  - Good for quicker Vercel builds / and reducing Notion random limits
  - Next will still limit due to deduplicated requests
    - Sidenote: Need to get better at _not_ prop-drilling and just calling function again
- [x] Image Component
  - [x] Next Refactor
  - [x] Notion Refactor
- [x] Tailwind
  - [x] Move away from Stitches
  - [x] Temporary move to `@jeromefitz/ds` localized version
  - [x] Radix UI Refactor
  - [x] Use internal Component Library for now
- [x] Notion Refactor

  - [x] Image: Hosted by Notion Expiration Refresh
  - [x] Rely less on custom queries and manipulation, more on out of the box Notion API, React, and Next
    - [x] Move from `nodes` to more straight-forward components
    - [x] Refactor logic for
      - [x] `Column|ColumnList`
      - [x] `ListBulleted|ListItem|ListNumbered`
      - [x] `TextAnnotations`
    - [x] **New**: `Embed|Video`
      - [x] `Embed.Twitter` <= Twitter is self-imploding, so good timing.
      - [x] `Embed.YouTube` <= YouTube is ... no comment.

- [x] Next
  - [ ] `preload` => hold on this for now not working as expected
  - [x] `generateMetadata` => move away from `next-seo` (rip)
    - [ ] Need to re-incorporate `@vercel/og` -- or not temporarily.
  - [x] `generateStaticParams` => hack if `isDev` to stop running all the time :?
  - [x] `not-found` => Instead of customizing every route, use `notFound()`
  - [x] `robots.ts|sitemap.ts` => move away from `next-sitemap` (rip)
- [x] Package Upgrades
  - [x] Basically everything except `plaiceholder|semantic-release|syncpack`
- [x] Other refactors
  - [x] EmojiWrapper
  - [x] Config Packages
    - [x] `./packages/*` – this all needs to be ported to [`@jeromefitz/packages`](https://github.com/JeromeFitz/packages)
      - Was borderline impossible to do these in-tandem (need to get better at `pnpm linking`)
- [x] Fathom advises against custom domains now :/

## Layout

Not to be lost in the backend type stuff but this is a complete rehaul of presentation.

The eventual goal of this `Notion + Next` implementation is you can take the data in any way and display it as you would like. For now though still tightly coupled with a lot of decisions until I can abstract away further. Which -- at teh rate I am going may never happen.

## Notion

Do not "normalize" data from Notion, embrace it.

- This is the CMS why are we going through all the trouble to hack it
- Create new Block Components to match and mimic needs

### Formulas

The "big change" here is utilizing Notion Formulas in the CMS.

#### Slug

Before we had `Slug` now we populated `Slug.Preview` where we are able to have Notion mimic Routes better Server Side than figuring it all out on the fly in `next`.

**Note:** For `Events` we need to manually write the `Slug` for now. The potential clash of having multiple Headline Acts means we could have a url like:

- `../jerome-and,alex-o-jerome`

Which I think _could_ work because we could loop through but also _very_ confusing as a URL to share, haha.

To recap:

- `Slug.Preview` for example will create the matching Next Segment Route
  - Before: `jerome-and` (shows); After: `/shows/jerome-and`
  - Before: `jerome-and` (events); After: `/events/2023/06/16/jerome-and`
  - Before: `homepage` (pages); After: `/`

##### Date

Same here, instead of getting the data from Notion then running through `date-fns`, Notion uses `moment` (I think). So we can do more preparation which makes for a more straight-forward:

```bash
- Date: July 15, 2023 9:00PM
- Date.DayOfMonth: 15
- Date.DayOfMonthOrdinal: 15th
- Date.DayOfWeek: Saturday
- Date.DayOfWeekAbbr: Sat
- Date.DaysUntilEvent: 15
- Date.HoursUntilEvent: 360
- Date.ISO: 2023-07-15T21:00:00-04:00
- Date.Month: 07
- Date.MonthName: July
- Date.MonthNameAbbr: Jul
- Date.Time: 09:00 PM
- Date.Timezone: EDT
- Date.WeekNumber: 28
- Date.Year: 2023
```

## Next

### App

The gains of doing `[[...catchAll]]` for everything at **root** was not worth it. 😅

Especially if we _want_ to be able to change layout, RSC data points and more based on the Segment (Notion Database Type).

So there is some duplication of code throughout but will look into better ways of lifting the "same" stuff.

### Events

Ability to see a range of events depending on Date (say for a week, or a weekend):

- `events/yyyy/mm/dd/to/yyyy/mm/dd`
- `events/2023/06/29/to/2023/07/02`

Props to Katie T. as we came up with this idea in a brainstorm session.

- `events/[from]/to/[to]`
- `events/2023/06/15/to/2023/06/18` (THU-SUN)
- `events/2023/06/29/to/2023/05/01` (Across Months)
- `events/2023/12/28/to/2025/01/07` (Across Years)

Probably need to do something for malformed dates, but I reckon `404` will do that.

Up next would be ideas for `Landing Pages`.

### In-House

`next-seo` and `next-sitemap` will eventually be absorded, or their functionality at least, within `next` itself. This gets the ball rolling on that. They were awesome, and thank you.

Depending on your use case those will still be very valid for use!

## Packages

This just covers the `sites/jeromefitzgerald.com` for now

**Upgrade:**
```bash
@mantine/hooks@6.0.15
@notionhq/client@2.2.6
@radix-ui/...@latest
@upstash/redis@1.22.0
@vercel/og@0.5.8
framer-motion@10.12.18
next@13.4.8-canary.14
react-swipeable@7.0.1
swr@2.2.0

@types/ramda@0.29.3
@types/react@18.2.14
@types/react-dom@18.2.6
@types/uuid@9.0.2
tailwind-merge@1.13.2
```

**Add:**

```bash
emoji-regex@10.2.1
node-emoji@2.1.0
react-headroom@3.2.1 # use framer-motion instead
react-tweet@2.0.2 # 3.x has no release notes

@types/react-headroom@3.2.0
```

**Remove:**

```bash
next-seo
next-sitemap
next-unused
```

---
## [nicolas-grekas/symfony](https://github.com/nicolas-grekas/symfony)@[af44385d9e...](https://github.com/nicolas-grekas/symfony/commit/af44385d9e6eba77b4bf4610231ce9569bdcc9b5)
#### Monday 2023-07-03 15:55:51 by Robin Chalas

feature #50754 [HttpKernel] when configuring the container add services_{env} with php extension  (helyakin)

This PR was merged into the 6.4 branch.

Discussion
----------

[HttpKernel] when configuring the container add services_{env} with php extension

| Q             | A
| ------------- | ---
| Branch?       | 6.4
| Bug fix?      | no
| New feature?  | yes
| Deprecations? | no
| Tickets       | none
| License       | MIT

Hello the community

This is my first PR attempt.

So after reading this [documentation](https://symfony.com/doc/current/service_container.html#remove-services) and unsuccessfully trying to load my `service_test.php`, I've noticed that the `configureContainer(..)` function in the `MicroKernelTrait` file was not configured to automatically load this file.

So either we should fix the documentation, either we should fix the configuration.

Since this the [framework-bundle](https://github.com/symfony/framework-bundle) is backed by [Alximy](https://alximy.io) I figured it would be cool 😎 to try and fix 🐛 the configuration.

Anyway share me your thoughts about what should be done !

And I wanted to say that php service configuration is 🔥 so shoutout to the one who did this (I think it's you `@nicolas`-grekas with this [PR](https://github.com/symfony/symfony/pull/23834) right ? 💪🏻)

Also big thanks to `@jeremyFreeAgent` for debugging this with me and `@HeahDude` for showing me the php service configuration PR.

Commits
-------

4aac1d9fee :bug: (kernel) when configuring the container add services with php ext

---
## [meemofcourse/Shiptest](https://github.com/meemofcourse/Shiptest)@[8744738e59...](https://github.com/meemofcourse/Shiptest/commit/8744738e5955c02834d67db6f14201c28c9ac61c)
#### Monday 2023-07-03 16:44:18 by Arturlang

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
## [ahjragaas/binutils-gdb](https://github.com/ahjragaas/binutils-gdb)@[8bcead6966...](https://github.com/ahjragaas/binutils-gdb/commit/8bcead69665af3a9f9867cd34c3a1daf22120027)
#### Monday 2023-07-03 17:10:09 by Andrew Burgess

gdb/testsuite: add test for core file with a 0 pid

This patch contains a test for this commit:

  commit c820c52a914cc9d7c63cb41ad396f4ddffff2196
  Date:   Fri Aug 6 19:45:58 2010 +0000

              * thread.c (add_thread_silent): Use null_ptid instead of
              minus_one_ptid while getting rid of stale inferior_ptid.

This is another test that has been carried in the Fedora GDB tree for
some time, and I thought that it would be worth merging to master.  I
don't believe there is any test like this currently in the testsuite.

The original issue was reported in this thread:

  https://inbox.sourceware.org/gdb-patches/AANLkTi=zuEDw6qiZ1jRatkdwHO99xF2Qu+WZ7i0EQjef@mail.gmail.com/

The problem was that when GDB was used to open a vmcore (core file)
image generated by the Linux kernel GDB would (sometimes) crash with
an assertion failure:

  thread.c:884: internal-error: switch_to_thread: Assertion `inf != NULL' failed.

To understand what's going on we need some background; a vmcore file
represents each processor core in the same way that a standard
application core file represents threads.  Thus, we might say, a
vmcore file represents cores as threads.

When writing a vmcore file, the kernel will store the pid of the
process currently running on that core as the thread's lwpid.

However, if a core is idle, with no process currently running on it,
then the lwpid for that thread is stored as 0 in the vmcore file.  If
multiple cores are idle then multiple threads will have a lwpid of 0.

Back in 2010, the original issue reported tried to change the kernel's
behaviour in this thread:

  https://lkml.org/lkml/2010/8/3/75

This change was rejected by the kernel team, the current
behaviour (lwpid of 0) was considered correct.  I've checked the
source of a recent kernel.  The code mentioned in the lkml.org posting
has moved, it's now in the function crash_save_cpu in the file
kernel/kexec_core.c, but the general behaviour is unchanged, an idle
core will have an lwpid of 0, so I think GDB still needs to be able to
handle this case.

When GDB loads a vmcore file (which is handled just like any other
core file) the sections are processed in core_open to generate the
threads for the core file.  The processing is done by calling
add_to_thread_list, a function which looks for sections named .reg/NN
where NN is the lwpid of the thread, GDB then builds a ptid_t for the
new thread and calls add_thread.

Remember, in our case the lwpid is 0.  Now for the first thread this
is fine, if a little weird, 0 isn't usually a valid lwpid, but that's
OK, GDB creates a thread with lwpid of 0 and carries on.

When we find the next thread (core) with lwpid of 0, we attempt to
create another thread with an lwpid of 0.  This of course clashes with
the previously created thread, they have the same ptid_t, so GDB tries
to delete the first thread.

And it was within this thread delete code that we triggered a bug
which would then cause GDB to assert -- when deleting we tried to
switch to a thread with minus_one_ptid, this resulted in a call to
find_inferior_pid (passing in minus_one_ptid's pid, which is -1), the
find_inferior_pid call fails and returns NULL, which then triggered an
assert in switch_to_thread.

The actual details of the why the assert triggered are really not
important.  What's important (I think) is that a vmcore file might
have this interesting lwpid of 0 characteristic, which isn't something
we see in "normal" application core files, and it is this that I think
we should be testing.

Now, you might be thinking: isn't deleting the first thread the wrong
thing to do?  If the vmcore file has two threads that represent two
cores, and both have an lwpid of 0 (indicating both cores are idle),
then surely GDB should still represent this as two threads?  You're
not wrong.  This was mentioned by Pedro in the original GDB mailing
list thread here:

  https://inbox.sourceware.org/gdb-patches/201008061057.03037.pedro@codesourcery.com/

This is indeed a problem, and this problem is still present in GDB
today.  I plan to try and address this in a later commit, however,
this first commit is about getting a test in place to confirm that GDB
at a minimum doesn't crash when loading such a vmcore file.

And so, finally, what's in this commit?

This commit contains a new test.  The test doesn't actually contain a
vmcore file.  Instead I've created a standard application core file
that contains two threads, and then manually edited the core file to
set the lwpid of each thread to 0.

To further reduce the size of the core file (as it will be stored in
git), I've zeroed all of the LOAD-able segments in the core file.
This test really doesn't care about that part of the core file, we
only really care about loading the register's, this is enough to
confirm that the GDB doesn't crash.

Obviously as the core file is pre-generated, this test is architecture
specific.  There are already a few tests in gdb.arch/ that include
pre-generate core files.  Just as those existing tests do, I've
compressed the core file with bzip2, which reduces it to just 750
bytes.  I have structured the test so that if/when this patch is
merged I can add some additional core files for other architectures,
however, these are not included in this commit.

The test simply expands the core file, and then loads it into GDB.
One interesting thing to note is that GDB reports the core file
loading like this:

  (gdb) core-file ./gdb/testsuite/outputs/gdb.arch/core-file-pid0/core-file-pid0.x86-64.core
  [New process 1]
  [New process 1]
  Failed to read a valid object file image from memory.
  Core was generated by `./segv-mt'.
  Program terminated with signal SIGSEGV, Segmentation fault.
  The current thread has terminated
  (gdb)

There's two interesting things here: first, the repeated "New process
1" message.  This is caused because linux_core_pid_to_str reports
anything with an lwpid of 0 as a process, rather than an LWP.  And
second, the "The current thread has terminated" message.  This is
because the first thread in the core file is the current thread, but
when GDB loads the second thread (which also has lwpid 0) this causes
the first thread to be deleted, as a result GDB thinks that the
current (first) thread has terminated.

As I said previously, both of these problems are a result of the lwpid
0 aliasing, which is not being fixed in this commit -- this commit is
just confirming that GDB doesn't crash when loading this core file.

Reviewed-By: Kevin Buettner <kevinb@redhat.com>

---
## [IIWOLFII/PSolving-with-AaDS](https://github.com/IIWOLFII/PSolving-with-AaDS)@[3cbca2edb5...](https://github.com/IIWOLFII/PSolving-with-AaDS/commit/3cbca2edb5ba2e67f3812f486b9436eb66c5f733)
#### Monday 2023-07-03 17:22:11 by IIWOLFII

chapter 4 maze done, wish i could understand teh shitcode from the book that would be cool i think,
fuck DP

---
## [cohnt/drake](https://github.com/cohnt/drake)@[f90899e13f...](https://github.com/cohnt/drake/commit/f90899e13fd6b703ac5c7da3d1b7c0584a793769)
#### Monday 2023-07-03 17:30:54 by Jeremy Nimmer

[geometry] Add Meshcat::GetRealtimeRate (#19700)

Tidy up recent Meshcat changes:
- Add missing pydrake bindings.
- Strongly prefer testing the public API (eschew test-friendship hacks).
  We want to guard against regressions in the end-user experience;
  using private API goes against that goal.
- Fix indentation, typos, and eschew abbreviation.

---
## [Moltovz/Shiptest](https://github.com/Moltovz/Shiptest)@[0cff53fc09...](https://github.com/Moltovz/Shiptest/commit/0cff53fc09c34d989d2bc34b1699bd856af2cb92)
#### Monday 2023-07-03 17:50:49 by meemofcourse

Reworks the Twinkleshine-Class (#1825)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request


![2023 05 13-23 20
45](https://github.com/shiptest-ss13/Shiptest/assets/75212565/de6f3a47-7be8-4800-ae73-9fc386e4bf01)

![twinklerework5](https://github.com/shiptest-ss13/Shiptest/assets/75212565/f1808576-70e3-4b56-b977-5b5e7d665fdd)





The Twinkleshine is a CyberSun-made Syndicate display of force, staffed
by every branch of the Syndicate. Despite the silly name, the presence
of one in a sector implies it to be of importance to the Syndicate, and
enemies within sight can only pray that the Twinkleshine crew are
incompetent enough to shoot themselves with their own weaponry (or blow
themselves up with the supermatter on-board).

It is staffed by:

- 1 Captain
- 1 Lieutenant (previously the Operative - serves as a warden/hos)
- 2 Medics
- 2 Engineers (previously the Mechanics)
- 5 Operatives (previously the Troopers)
- 1 Bartender
- 1 Miner
- 2 Deck Assistants

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Few days ago, an admin spawned a Twinkleshine, and I got to captain it.
The Twinkleshine is old. It sucks. This, hopefully, fixes that.

Originally, this was going to be minor fixes, but ended up becoming an
attempt at reworking the ship to a more modern state - the hull has been
redone and is mostly symmetrical, the old spacepod was replaced with a
Dark Gygax, the supermatter shouldn't be activated upon spawning the
ship, there's more turf decals and a bigger lot-of-things, added a
bartender and a miner, people can actually tell who they are and what
they do, and there is now a box moth. Rejoice.

Also, this is the first time I've ever mapped a ship. What better way to
begin with a giant battleship?

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
tweak: Reworks the Twinkleshine
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: meemofcourse <75212565+meemofcourse@users.noreply.github.com>

---
## [Moonshanks/cmss13](https://github.com/Moonshanks/cmss13)@[0f386c8188...](https://github.com/Moonshanks/cmss13/commit/0f386c8188849b2a761ef773ed83d7f2a95d40e7)
#### Monday 2023-07-03 17:54:03 by fira

Stops Squad Leaders and ComTechs from blowing up the Almayer (#3602)

# About the pull request

Okay that's a clickbait....

When people put C4 and Breaching Charges in their bag and what not the
log gets triggered.

This spams niche log with false warnings of /!\ DANGEROUS GRIEFING
TERRORISTS /!\

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
Uh

# Changelog
:cl:
fix: Handling C4 and Breaching Charges should not zealously trigger
antigrief protection anymore
/:cl:

---------

Co-authored-by: harryob <me@harryob.live>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[f2ec16c1e6...](https://github.com/tgstation/tgstation/commit/f2ec16c1e6485bdf2035837fb3d42de24900e8b4)
#### Monday 2023-07-03 18:55:07 by Vekter

Plasma objects no longer violently explode when ignited (#76492)

## About The Pull Request
This is one of those "can I get away with making a change I want" PRs.

I actually didn't know this had been changed before as it's not exactly
something I mess with often, but I really think it sucks. Plasma stuff
is supposed to ignite and cause fires, not explode (unless in a TTV). I
noticed this when I was poking around and found out that apparently
Disco Inferno just explodes now instead of setting on fire which also
sucks.

I figure there's a few fixes for this problem:

1) Nerf how hard plasma stuff explodes. This is an option, but I kind of
dislike that it does it at all more than anything. The biggest issue is
that just the regular statues explode with 20 LIGHT, which is pretty
fucking massive and basically just delimbs everyone around. I'd have to
nerf it HARD for it to get anywhere near what I think is acceptable.
2) Make a snowflake version of the statue that just ignites on hit with
a torch. I also don't like this because it'll make people think the
regular statues don't explode.
3) This option, which I think is cleaner and just makes sense compared
to the others.

I don't know if @vincentiusvin still codes, but as far as I can tell
this was their doing, so it's only fair they get to speak up.

Fixes #71894

## Why It's Good For The Game
I don't like it, I think it goes against what we're used to for plasma
stuff (that it starts fires, not makes explosions) and it makes one of
my favorite shuttles boring and stupid. That being said, I'm honestly
not going to fight for this too hard if a lot of people like it, but I
am - as always - open to alternatives.

## Changelog
:cl: Vekter
del: Plasma objects (statues, toilets, etc.) no longer explode when
ignited. They just release plasma like everything else plasma. (This
doesn't impact injecting plasma into cells or dipping cigars in plasma,
those still explode.)
/:cl:

---
## [awatefkh3/hw4](https://github.com/awatefkh3/hw4)@[901ea1f520...](https://github.com/awatefkh3/hw4/commit/901ea1f52034a5801a5ac8132343346f5dcafc74)
#### Monday 2023-07-03 19:35:53 by awatefkh1

fuck you dvir twito!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[05cba97a2f...](https://github.com/TaleStation/TaleStation/commit/05cba97a2f8e9328f5fc70b24062109f43a01c82)
#### Monday 2023-07-03 19:52:18 by TaleStationBot

[MIRROR] [MDB IGNORE] Plasma objects no longer violently explode when ignited (#6595)

Original PR: https://github.com/tgstation/tgstation/pull/76492
-----
## About The Pull Request
This is one of those "can I get away with making a change I want" PRs.

I actually didn't know this had been changed before as it's not exactly
something I mess with often, but I really think it sucks. Plasma stuff
is supposed to ignite and cause fires, not explode (unless in a TTV). I
noticed this when I was poking around and found out that apparently
Disco Inferno just explodes now instead of setting on fire which also
sucks.

I figure there's a few fixes for this problem:

1) Nerf how hard plasma stuff explodes. This is an option, but I kind of
dislike that it does it at all more than anything. The biggest issue is
that just the regular statues explode with 20 LIGHT, which is pretty
fucking massive and basically just delimbs everyone around. I'd have to
nerf it HARD for it to get anywhere near what I think is acceptable.
2) Make a snowflake version of the statue that just ignites on hit with
a torch. I also don't like this because it'll make people think the
regular statues don't explode.
3) This option, which I think is cleaner and just makes sense compared
to the others.

I don't know if vincentiusvin still codes, but as far as I can tell this
was their doing, so it's only fair they get to speak up.

Fixes #71894

## Why It's Good For The Game
I don't like it, I think it goes against what we're used to for plasma
stuff (that it starts fires, not makes explosions) and it makes one of
my favorite shuttles boring and stupid. That being said, I'm honestly
not going to fight for this too hard if a lot of people like it, but I
am - as always - open to alternatives.

## Changelog
:cl: Vekter
del: Plasma objects (statues, toilets, etc.) no longer explode when
ignited. They just release plasma like everything else plasma. (This
doesn't impact injecting plasma into cells or dipping cigars in plasma,
those still explode.)
/:cl:

---------

Co-authored-by: Vekter <TheVekter@users.noreply.github.com>

---
## [MemedHams/mojave-sun-13](https://github.com/MemedHams/mojave-sun-13)@[b2f0f35f3a...](https://github.com/MemedHams/mojave-sun-13/commit/b2f0f35f3afe1905cfefcf9e682de51cff2d4499)
#### Monday 2023-07-03 19:57:18 by EdwardNashton

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[2afbefa52e...](https://github.com/treckstar/yolo-octo-hipster/commit/2afbefa52ea9f7c91f07724f189dbb9bf9f24ae9)
#### Monday 2023-07-03 20:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[9701b40ca0...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/9701b40ca03e164bd8bd4238fafb6cf778c52efe)
#### Monday 2023-07-03 21:33:08 by SkyratBot

[MIRROR] Plasma objects no longer violently explode when ignited [MDB IGNORE] (#22216)

* Plasma objects no longer violently explode when ignited (#76492)

## About The Pull Request
This is one of those "can I get away with making a change I want" PRs.

I actually didn't know this had been changed before as it's not exactly
something I mess with often, but I really think it sucks. Plasma stuff
is supposed to ignite and cause fires, not explode (unless in a TTV). I
noticed this when I was poking around and found out that apparently
Disco Inferno just explodes now instead of setting on fire which also
sucks.

I figure there's a few fixes for this problem:

1) Nerf how hard plasma stuff explodes. This is an option, but I kind of
dislike that it does it at all more than anything. The biggest issue is
that just the regular statues explode with 20 LIGHT, which is pretty
fucking massive and basically just delimbs everyone around. I'd have to
nerf it HARD for it to get anywhere near what I think is acceptable.
2) Make a snowflake version of the statue that just ignites on hit with
a torch. I also don't like this because it'll make people think the
regular statues don't explode.
3) This option, which I think is cleaner and just makes sense compared
to the others.

I don't know if @ vincentiusvin still codes, but as far as I can tell
this was their doing, so it's only fair they get to speak up.

Fixes #71894

## Why It's Good For The Game
I don't like it, I think it goes against what we're used to for plasma
stuff (that it starts fires, not makes explosions) and it makes one of
my favorite shuttles boring and stupid. That being said, I'm honestly
not going to fight for this too hard if a lot of people like it, but I
am - as always - open to alternatives.

## Changelog
:cl: Vekter
del: Plasma objects (statues, toilets, etc.) no longer explode when
ignited. They just release plasma like everything else plasma. (This
doesn't impact injecting plasma into cells or dipping cigars in plasma,
those still explode.)
/:cl:

* Plasma objects no longer violently explode when ignited

---------

Co-authored-by: Vekter <TheVekter@users.noreply.github.com>

---
## [examknow/solanum](https://github.com/examknow/solanum)@[06c5309534...](https://github.com/examknow/solanum/commit/06c53095343c2756208f6398bb7e00fb2cbe46dd)
#### Monday 2023-07-03 22:51:41 by Ed Kellett

m_sasl: Remove implicit abort on registration

This doesn't make sense in a world where post-registration SASL is
allowed, and should fix one case of an annoying login desync that's seen
in the real world.

Specifically, when a client sends its final AUTHENTICATE and Atheme
receives it, it sends an SVSLOGIN for that client. If the client sends
us its CAP END *before* we see the SVSLOGIN, the implicit abort will try
to abort the SASL session that's already succeeded.

Atheme interprets this as an instruction to forget about the successful
SASL session; you'll connect unidentified. But it's already sent
SVSLOGIN, which will log the client in ircd-side, causing ircd and
services views to differ until the user authenticates again manually.

I think allowing a SASL session to be aborted when it has already
succeeded is an Atheme bug, and it can still be triggered without this
change. But our behaviour here seems silly anyway.

---
## [rstrojan/AutoBattlerPrototype](https://github.com/rstrojan/AutoBattlerPrototype)@[33dd97e68b...](https://github.com/rstrojan/AutoBattlerPrototype/commit/33dd97e68b61f6fe02a34060a085b8fe76464be8)
#### Monday 2023-07-03 23:14:42 by rstrojan

Inventory enhancement shared pointers (#8)

* Starting implementation of GameState object (#7)

* Add files via upload

* Started implementing the Game State object.

- GameState time. I started by moving the prepLoop inventories and GameObjects into the GameState object. I relearned a couple of things while doing. One I don't think I've dealt with since my first coding classes at Everett Community College, the other is something I've been kinda dreading.
- The first thing: Relearning about Constructor Initializer Lists. In my GS_Campaign class I need to have some Inventories. However, the constructor for those inventories need to be called in order to create them properly. So I couldn't simply declare it as "Inventory equipmentInv;" and start using it. It needs to call the Inventory(string name) constuructor. That simple declaration on the header file doesn't cut it. Previously, I had this done as part of the declaration in the header file.  it was "Inventory equipmentInv = Inventory("Equipment")". This would call the constructor properly. However, this is apparently not best practice. You don't want to do constructor calls as part of your declerations in your class header files. According to ChatGPT, the benefits are:
	- Improved performance: Initializing member variables in the constructor initialization list can be more efficient than initializing them in the constructor body, especially for complex objects.
	- Consistent initialization: Initialization lists ensure that member variables are always initialized to a valid state, even if an exception is thrown during construction.
	- Cleaner code: Initialization lists can make the code easier to read and understand, especially for classes with many member variables.
- I don't exactly know what it is more effecient, but I am sold none-the-less. Similar to doing the std:: namespace thing. It may feel weird at first, but I should get use to it and just make it part of how I opperate.
- Now, I will only put the declaration of the member variable in the header page Inventory equipmentInv. And then in the constructor, you would do this:
	GS_Campaign::GS_Campaign() :
	equipmentInv("Equipment")
	{};
- The other issue that came up (the thing I've been kinda dreading or at least was hoping to avoid) would be memory management involved in maintaining gameObjects. In order for my gameState to be able to create objects in its constructor and then also access those later, I need them to not be destroyed in the constructor. To do this, I have to use the "new" keyword, which allocates memory on the heap. However, that will also mean that I'm on the hook for deleting them. Now, I'm already planning on passing that object around mostly by pointer. In fact, Inventory is set up hold pointers. The easiest way to do this will be to use shared pointers. AKA smart pointers. These will maintain the object so long as the object has an existing reference pointing to it. If all of the pointers are destroyed, then the object will also be destroyed. Which is what I want. The question is going to be, how are these shared pointers going to be created?

* Converted Inventory.inv from ptrs to shared_ptrs.

- OK, today I'm going to try and change my Inventory class over from a list of regular pointers, to a list of shared_pointers or smart pointers as they are called. I had initially avoided these when I started, as I didn't quite understand why they were different. However, they have a major benefit over regular pointers, in that, when an object is created with a shared pointer, the shared pointer will keep track of how many other pointers are pointing to it. When there are no more pointers pointing to the object, the object will be destroyed. This is great, because for the GameState class to maintain objects, it needs to use the 'new' keyword and add them to the heap. The only way to get those objects off the heap is to destroy them. I could try to create some grand scheme for how this will work, but I don't actually need to, I can just let the shared pointers do that. Currently, the Inventory class keeps track of all it's objects as regular pointers, which means that I would have to handle destroying them. However, if I move them to shared pointers, then the objects will destroy themselves. So that's what we are gonna do.
- To do this, I'm going to need a new library that I have not used called <memory>.
- That was actually really easy! All I had to do was change the function declarations and definitions and the declaration of the objects themselves. I also streamlined the declaration of the objects in GS_Campaign so that I'm not declaring the obj first, then passing it. Now I declare it directly in the argument, which means I don't have an extra pointer inside of GS_Campaign.
- I would get into the techical details, but there really isn't that much difference between this and regular pointers. I just had to ask chatGPT a couple of syntax questions and now it's working.

---

