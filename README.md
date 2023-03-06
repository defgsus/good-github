## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-03-05](docs/good-messages/2023/2023-03-05.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,897,100 were push events containing 2,648,844 commit messages that amount to 161,945,837 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 40 messages:


## [ORCACommander/Tannhauser-Gate-Dev](https://github.com/ORCACommander/Tannhauser-Gate-Dev)@[f5e63175ec...](https://github.com/ORCACommander/Tannhauser-Gate-Dev/commit/f5e63175eca40d65592b20a77df6025d1a3f9804)
#### Sunday 2023-03-05 00:00:52 by SkyratBot

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
## [space-wizards/space-station-14](https://github.com/space-wizards/space-station-14)@[581e8a0d12...](https://github.com/space-wizards/space-station-14/commit/581e8a0d123eca621e52716fd5816966b0569a36)
#### Sunday 2023-03-05 00:36:13 by eclips_e

Give slimes their sex back (not the ERP one) (#14380)

<!-- Please read these guidelines before opening your PR: https://docs.spacestation14.io/en/getting-started/pr-guideline -->
<!-- The text between the arrows are comments - they will not be visible on your PR. -->

## About the PR
<!-- What does it change? What other things could this impact? -->

Gives back the ability for slimes to have a definitive sex. Cosmetic/visual things such as emotes/other stuff use the person's sex and not the gender and I feel like that the removal of slime's having sexes was just to show that the species refactor could handle unsexed species.

**Media**
<!-- 
PRs which make ingame changes (adding clothing, items, new features, etc) are required to have media attached that showcase the changes.
Small fixes/refactors are exempt.
Any media may be used in SS14 progress reports, with clear credit given.

If you're unsure whether your PR will require media, ask a maintainer.

Check the box below to confirm that you have in fact seen this (put an X in the brackets, like [X]):
-->

- [x] I have added screenshots/videos to this PR showcasing its changes ingame, **or** this PR does not require an ingame showcase

**Changelog**
<!--
Here you can fill out a changelog that will automatically be added to the game when your PR is merged.

Only put changes that are visible and important to the player on the changelog.

Don't consider the entry type suffix (e.g. add) to be "part" of the sentence:
bad: - add: a new tool for engineers
good: - add: added a new tool for engineers

Putting a name after the :cl: symbol will change the name that shows in the changelog (otherwise it takes your GitHub username)
Like so: :cl: PJB
-->

:cl: eclips_e
- fix: Male and female slimes now scream and laugh properly

---
## [Unrated-Demon-List/unrated-demon-list](https://github.com/Unrated-Demon-List/unrated-demon-list)@[719c38afe1...](https://github.com/Unrated-Demon-List/unrated-demon-list/commit/719c38afe15720fbd19f9baffba91762ce510258)
#### Sunday 2023-03-05 00:50:29 by BreadDemon

List Movement march 4th, 2023

moved some levels, changelog here:
Rip It and In Abyss have swapped, with In Abyss on top.
Hyper Paradigmatic has been moved from #102 to #, Crystal Caverns has been moved from #118 to #, with Hyper Paradigmatic above Crystal Caverns and below Mystic Refractions, and Crystal Caverns above Eyre.
Sound wave destroyer has been moved from #119 to #, above Death Corridor Unner and below Ocular Miracle.
Theory of Darkness has been moved from #114 to #, above Old Sonic Wave and below CATNIVORES.
Night City has been moved from #103 to #, below Misty Downfall (Remake) and above C418. Highly subject to change, as in it should be lower so can someone play it so it can move down 🥺

---
## [PhantomEpicness/cmss13](https://github.com/PhantomEpicness/cmss13)@[fc1e2e5e26...](https://github.com/PhantomEpicness/cmss13/commit/fc1e2e5e26259773038df05c5405cb80441b8cc2)
#### Sunday 2023-03-05 00:51:20 by riot

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
## [Hostnomics/Full-Stack-Web3-32-hour-course-by-freeCodeCamp](https://github.com/Hostnomics/Full-Stack-Web3-32-hour-course-by-freeCodeCamp)@[f33fdca0f1...](https://github.com/Hostnomics/Full-Stack-Web3-32-hour-course-by-freeCodeCamp/commit/f33fdca0f141243b87ccf3626fa2a32e12cef537)
#### Sunday 2023-03-05 04:13:06 by Hostnomics

FUCK PCs FUCK THEM. MAC OR LINUX ONLY FUCK GOD DAMN PC

---
## [Rok1006/InFiniteTrain](https://github.com/Rok1006/InFiniteTrain)@[5cf54b14a4...](https://github.com/Rok1006/InFiniteTrain/commit/5cf54b14a451e9ac1fc7674fc9724d45c1f1fd11)
#### Sunday 2023-03-05 05:30:53 by ROK

freakin mini game no bug ver fuck yeah 9 hrs omg so dumb wtf

---
## [silicons/Citadel-Station-13-RP](https://github.com/silicons/Citadel-Station-13-RP)@[83d3e312f8...](https://github.com/silicons/Citadel-Station-13-RP/commit/83d3e312f83d6cf3849ac3bf1baaf2c8f62ead0f)
#### Sunday 2023-03-05 07:12:34 by Zandario

fucky wucky (#5102)

I joked about having something silly to tell players we're fixing shit,
and while looking into bee's statpanel I noticed the image for this in
their HTML files so of course I had to add it.

Ported from: BeeStation/BeeStation-Hornet/pull/1574

---
## [QKIvan/android_frameworks_base](https://github.com/QKIvan/android_frameworks_base)@[94c3f10636...](https://github.com/QKIvan/android_frameworks_base/commit/94c3f1063616614e31448f4e5712fc26346cdc42)
#### Sunday 2023-03-05 08:13:29 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6

---
## [Eric-Olalude/create-react-app](https://github.com/Eric-Olalude/create-react-app)@[9e0b925c0b...](https://github.com/Eric-Olalude/create-react-app/commit/9e0b925c0b329e63fa466d3a14497337e7bc0b89)
#### Sunday 2023-03-05 08:51:18 by Eric-Olalude

Update making-a-progressive-web-app.md

---
id: making-a-progressive-web-app
title: Making a Progressive Web App
---

The production build has all the tools necessary to generate a first-class
[Progressive Web App](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps),
but **the offline/cache-first behavior is opt-in only**.

Starting with Create React App 4, you can add a `src/service-worker.js` file to
your project to use the built-in support for
[Workbox](https://developers.google.com/web/tools/workbox/)'s
[`InjectManifest`](https://developers.google.com/web/tools/workbox/reference-docs/latest/module-workbox-webpack-plugin.InjectManifest)
plugin, which will
[compile](https://developers.google.com/web/tools/workbox/guides/using-bundlers)
your service worker and inject into it a list of URLs to
[precache](https://developers.google.com/web/tools/workbox/guides/precache-files).

If you start a new project using one of the PWA [custom
templates](https://create-react-app.dev/docs/custom-templates/), you'll get a
`src/service-worker.js` file that serves as a good starting point for an
offline-first service worker:

```sh
npx create-react-app my-app --template cra-template-pwa
```

The TypeScript equivalent is:

```sh
npx create-react-app my-app --template cra-template-pwa-typescript
```

If you know that you won't be using service workers, or if you'd prefer to use a
different approach to creating your service worker, don't create a
`src/service-worker.js` file. The `InjectManifest` plugin won't be run in that
case.

In addition to creating your local `src/service-worker.js` file, it needs to be
registered before it will be used. In order to opt-in to the offline-first
behavior, developers should look for the following in their
[`src/index.js`](https://github.com/cra-template/pwa/blob/master/packages/cra-template-pwa/template/src/index.js)
file:

```js
// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://cra.link/PWA
serviceWorkerRegistration.unregister();
```

As the comment states, switching `serviceWorker.unregister()` to
`serviceWorker.register()` will opt you in to using the service worker.

## Why Opt-in?

Offline-first Progressive Web Apps are faster and more reliable than traditional
web pages, and provide an engaging mobile experience:

- All static site assets that are a part of your `webpack` build are cached so
  that your page loads fast on subsequent visits, regardless of network
  connectivity (such as 2G or 3G). Updates are downloaded in the background.
- Your app will work regardless of network state, even if offline. This means
  your users will be able to use your app at 10,000 feet and on the subway.
- On mobile devices, your app can be added directly to the user's home screen,
  app icon and all. This eliminates the need for the app store.

However, they [can make debugging deployments more
challenging](https://github.com/facebook/create-react-app/issues/2398).

The
[`workbox-webpack-plugin`](https://developer.chrome.com/docs/workbox/modules/workbox-webpack-plugin/)
is integrated into production configuration, and it will take care of compiling
a service worker file that will automatically precache all of your
`webpack`-generated assets and keep them up to date as you deploy updates. The
service worker will use a [cache-first
strategy](https://developers.google.com/web/fundamentals/instant-and-offline/offline-cookbook/#cache-falling-back-to-network)
for handling all requests for `webpack`-generated assets, including [navigation
requests](https://developers.google.com/web/fundamentals/primers/service-workers/high-performance-loading#first_what_are_navigation_requests)
for your HTML, ensuring that your web app is consistently fast, even on a slow
or unreliable network.

Note: Resources that are not generated by `webpack`, such as static files that are
copied over from your local
[`public/` directory](https://github.com/cra-template/pwa/tree/master/packages/cra-template-pwa/template/public/)
or third-party resources, will not be precached. You can optionally set up Workbox
[routes](https://developers.google.com/web/tools/workbox/guides/route-requests)
to apply the runtime caching strategy of your choice to those resources.

## Customization

Starting with Create React App 4, you have full control over customizing the
logic in this service worker, by creating your own `src/service-worker.js` file,
or customizing the one added by the `cra-template-pwa` (or
`cra-template-pwa-typescript`) template. You can use [additional
modules](https://developers.google.com/web/tools/workbox/modules) from the
Workbox project, add in a push notification library, or remove some of the
default caching logic. The one requirement is that you keep `self.__WB_MANIFEST`
somewhere in your file, as the Workbox compilation plugin checks for this value
when generating a manifest of URLs to precache. If you would prefer not to use
precaching, you can assign `self.__WB_MANIFEST` to a variable that will be
ignored, like:

```js
// eslint-disable-next-line no-restricted-globals
const ignored = self.__WB_MANIFEST;

// Your custom service worker code goes here.
```

## Offline-First Considerations

If you do decide to opt-in to service worker registration, please take the
following into account:

1. After the initial caching is done, the [service worker lifecycle](https://developers.google.com/web/fundamentals/primers/service-workers/lifecycle)
   controls when updated content ends up being shown to users. In order to guard against
   [race conditions with lazy-loaded content](https://github.com/facebook/create-react-app/issues/3613#issuecomment-353467430),
   the default behavior is to conservatively keep the updated service worker in the "[waiting](https://developers.google.com/web/fundamentals/primers/service-workers/lifecycle#waiting)"
   state. This means that users will end up seeing older content until they close (reloading is not
   enough) their existing, open tabs. See [this blog post](https://jeffy.info/2018/10/10/sw-in-c-r-a.html)
   for more details about this behavior.

1. Users aren't always familiar with offline-first web apps. It can be useful to
   [let the user know](https://developers.google.com/web/fundamentals/instant-and-offline/offline-ux#inform_the_user_when_the_app_is_ready_for_offline_consumption)
   when the service worker has finished populating your caches (showing a "This web
   app works offline!" message) and also let them know when the service worker has
   fetched the latest updates that will be available the next time they load the
   page (showing a "New content is available once existing tabs are closed." message). Showing
   these messages is currently left as an exercise to the developer, but as a
   starting point, you can make use of the logic included in [`src/serviceWorkerRegistration.js`](https://github.com/cra-template/pwa/blob/master/packages/cra-template-pwa/template/src/serviceWorkerRegistration.js), which
   demonstrates which service worker lifecycle events to listen for to detect each
   scenario, and which as a default, only logs appropriate messages to the
   JavaScript console.

1. Service workers [require HTTPS](https://developers.google.com/web/fundamentals/getting-started/primers/service-workers#you_need_https),
   although to facilitate local testing, that policy
   [does not apply to `localhost`](https://stackoverflow.com/questions/34160509/options-for-testing-service-workers-via-http/34161385#34161385).
   If your production web server does not support HTTPS, then the service worker
   registration will fail, but the rest of your web app will remain functional.

1. The service worker is only enabled in the [production environment](deployment.md),
   e.g. the output of `npm run build`. It's recommended that you do not enable an
   offline-first service worker in a development environment, as it can lead to
   frustration when previously cached assets are used and do not include the latest
   changes you've made locally.

1. If you _need_ to test your offline-first service worker locally, build
   the application (using `npm run build`) and run a standard http server from your
   build directory. After running the build script, `create-react-app` will give
   instructions for one way to test your production build locally and the [deployment instructions](deployment.md) have
   instructions for using other methods. _Be sure to always use an
   incognito window to avoid complications with your browser cache._

1. By default, the generated service worker file will not intercept or cache any
   cross-origin traffic, like HTTP [API requests](integrating-with-an-api-backend.md),
   images, or embeds loaded from a different domain. Starting with Create
   React App 4, this can be customized just as explained above.

## Progressive Web App Metadata

The default configuration includes a web app manifest located at
[`public/manifest.json`](https://github.com/cra-template/pwa/blob/master/packages/cra-template-pwa/template/public/manifest.json), that you can customize with
details specific to your web application.

When a user adds a web app to the homescreen using Chrome or Firefox on
Android, the metadata in [`manifest.json`](https://github.com/cra-template/pwa/blob/master/packages/cra-template-pwa/template/public/manifest.json) determines what
icons, names, and branding colors to use when the web app is displayed.
[The Web App Manifest guide](https://developers.google.com/web/fundamentals/engage-and-retain/web-app-manifest/)
provides more context about what each field means, and how your customizations
will affect your users' experience.

Progressive web apps that have been added to the homescreen will load faster and
work offline when there's an active service worker. That being said, the
metadata from the web app manifest will still be used regardless of whether or
not you opt-in to service worker registration.

---
## [Jalesen/tgstation](https://github.com/Jalesen/tgstation)@[5e80257423...](https://github.com/Jalesen/tgstation/commit/5e802574231c9c6fe835c40b55f2c8aa9f1c68b4)
#### Sunday 2023-03-05 08:56:53 by Jeremiah

Refactors crew records (#72725)

## About The Pull Request
I have attempted or otherwise started this project at least 4 times. I
am sick of it being on my calendar. The code needs it. I need it.

- This makes crew records a proper datum rather than assigning
properties record.fields.
- General, medical, and security records are merged.
- Did some slight refactoring here and there for things that looked
obvious.
- Wanted states are now defined (and you can suspect someone through
sechud)
- pAI (unrelated but annoying) had some poorly named exported types that
i made more specific
- Job icons are moved back to the JS side (I wanted to get icons for
initial rank without passing trim)

<details>
<summary>previews</summary>

Editable fields & security console

![CM6d74brnC](https://user-images.githubusercontent.com/42397676/213950290-af6cfd76-eb8b-48e9-b792-925949311d9a.gif)

Medical records

![bFJErsvOaN](https://user-images.githubusercontent.com/42397676/214132534-59af1f8c-9920-4b51-8b27-297103649962.gif)

Look and feel of the more current version

![cxGruQsJpP](https://user-images.githubusercontent.com/42397676/214132611-0134eef0-e74c-4fad-9cde-328ff7c06165.gif)

</details>

## Why It's Good For The Game
TGUI'd some of the worst UIs in the game.
Creating new records is made much simpler. 
Manifest_inject is made readable.
Probably bug fixes

## Changelog

:cl:
refactor: Crew records have been refactored.
refactor: Medical records -> TGUI
refactor: Security records -> TGUI
refactor: Warrants console -> TGUI
qol: Players are now alerted when their fines are paid off.
qol: Cleaned up sec hud examination text.
qol: Adding and deleting crimes is easier.
qol: Writing crimes in the console sets players to arrest.
qol: You can now mark someone as a suspect through sec hud.
/:cl:

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [samsung-mt6768-dev/android_kernel_samsung_a31](https://github.com/samsung-mt6768-dev/android_kernel_samsung_a31)@[243ac3783e...](https://github.com/samsung-mt6768-dev/android_kernel_samsung_a31/commit/243ac3783e72954a80ef3629de187794d0816ff5)
#### Sunday 2023-03-05 08:58:21 by Peter Zijlstra

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
## [elunna/hackem](https://github.com/elunna/hackem)@[0cd940eed0...](https://github.com/elunna/hackem/commit/0cd940eed0f62c2d9a83aa66de98dd5cfab9741c)
#### Sunday 2023-03-05 09:27:37 by Erik Lunna

Funny message if you use Spirit Tempest as a hallucinating female necromancer.

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[8ab74525c1...](https://github.com/necromanceranne/tgstation/commit/8ab74525c1c3c09a7605fead3ab013d29f24d07f)
#### Sunday 2023-03-05 09:27:49 by itseasytosee

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
## [RISHOBGHOSH/Statistics](https://github.com/RISHOBGHOSH/Statistics)@[ed2aad84b1...](https://github.com/RISHOBGHOSH/Statistics/commit/ed2aad84b1aaadd01e033b417782df90c6c1201f)
#### Sunday 2023-03-05 11:22:39 by Rishob Ghosh

Add files via upload

This folder contains a comprehensive collection of important topics in statistics. Whether you are a beginner or an advanced learner, this folder is a valuable resource that can help you understand various statistical concepts and their practical applications.

The topics covered in this folder include but are not limited to:

Descriptive statistics
Inferential statistics
Probability theory
Hypothesis testing
Confidence intervals
Regression analysis
Analysis of variance (ANOVA)
Correlation analysis
Time series analysis
Nonparametric statistics
Bayesian statistics
Experimental design
Sampling methods
Data visualization
Each topic is presented in a clear and concise manner, with examples and exercises to reinforce your understanding. Additionally, this folder includes resources such as cheat sheets, formula sheets, and statistical software tutorials to assist you in your statistical analysis. With this folder, you will have a comprehensive understanding of statistics that can be applied to various fields such as business, science, engineering, and social sciences.

---
## [RISHOBGHOSH/SQL](https://github.com/RISHOBGHOSH/SQL)@[cce503053c...](https://github.com/RISHOBGHOSH/SQL/commit/cce503053cf31c88a1c55600d4229093a6ec932c)
#### Sunday 2023-03-05 11:43:08 by Rishob Ghosh

Add files via upload

Welcome to the Statistics folder! This is a comprehensive collection of important topics in statistics that can be a valuable resource for learners at all levels.

The topics covered in this folder include but are not limited to:

Descriptive statistics
Inferential statistics
Probability theory
Hypothesis testing
Confidence intervals
Regression analysis
Analysis of variance (ANOVA)
Correlation analysis
Time series analysis
Nonparametric statistics
Bayesian statistics
Experimental design
Sampling methods
Data visualization
Each topic is presented in a clear and concise manner, with examples and exercises to reinforce your understanding. This folder also includes resources such as cheat sheets, formula sheets, and statistical software tutorials to assist you in your statistical analysis.

The goal of this folder is to provide you with a comprehensive understanding of statistics that can be applied to various fields such as business, science, engineering, and social sciences. We hope you find this folder useful and welcome any feedback or suggestions for improvement.

---
## [Thelema-SS/Thelema-STG](https://github.com/Thelema-SS/Thelema-STG)@[635aee8e34...](https://github.com/Thelema-SS/Thelema-STG/commit/635aee8e346a86ee375d262342057554b973e14b)
#### Sunday 2023-03-05 11:58:16 by SkyratBot

[MIRROR] pumping your heart doesnt require to be conscious [MDB IGNORE] (#16540)

* pumping your heart doesnt require to be conscious (#63290)

Simply removes the requirement to be conscious to pump your blood with a cursed heart.
Why It's Good For The Game

Entering crit or falling asleep is basically a life sentence since you are unable to pump your blood while asleep. The player still is manually pumping it, I don't see any reason why the user has to be awake for it.
This also means medical can't revive you, as you'll instantly lose all your blood before you have enough time to wake up to start pumping again. The only IC fix would be to remove your heart entirely, something most doctors wouldn't even notice.
Changelog

cl
fix: You can manually pump your blood while asleep/in crit, rather than instantly lose all your blood and die forever.
/cl

* pumping your heart doesnt require to be conscious

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>

---
## [Thelema-SS/Thelema-STG](https://github.com/Thelema-SS/Thelema-STG)@[a9c430a5e4...](https://github.com/Thelema-SS/Thelema-STG/commit/a9c430a5e43a638d3b56f57b663104e1e6a57364)
#### Sunday 2023-03-05 11:58:43 by SkyratBot

[MIRROR] Basic Mobs Now Actually Have A Deathgasp [MDB IGNORE] (#19002)

Basic Mobs Now Actually Have A Deathgasp (#72950)

## About The Pull Request

Pretty obviously an oversight since we only checked for simple_animal
for this, but should also factor in the fact that we could now be a
basic mob.

Actually I tested it on Sybil just now and deathgasps just never worked.
We were setting death_message for... I guess when they die? It's just
fucked but it works on my local now. blurgh
## Why It's Good For The Game

Ported simple animals that are now basic mobs were able to deathgasp
this time last year. Silly that they aren't able to do that now.
## Changelog
:cl:
fix: Basic Mobs are now able to deathgasp.
/:cl:

Let me know if the new variable name for the string is cringe, I just
settled on that since it mirrored the type of check we run in
select_message_type().

Co-authored-by: san7890 <the@san7890.com>

---
## [vincenzodp/ProjectRoots](https://github.com/vincenzodp/ProjectRoots)@[43a287edee...](https://github.com/vincenzodp/ProjectRoots/commit/43a287edeeda66f3a982305b942569c5d80f9804)
#### Sunday 2023-03-05 12:01:17 by tayumaru

Spawner Functionality ++

Spawner received a vast overhaul:
- ability to spawn different types of enemies
- ability to control exact sequence of enemies
- automatically controls interval between enemy spawns for a more cinematic gaming experience

PLEASE NOTE VERY IMPORTANT:
This version includes an experimental prototype of the wave system which is disabled by default.
To enable it please find the related variable that activates it and select it (making it true) in the inspector. without this selected the gameplay may result in a very imbalanced and frustrating experience. thus the developer STRONGLY recommends activating the aforementioned variable, if you are having trouble locating it please follow the instructions enclosed within the Spawner.cs file.

---
## [mosra/corrade](https://github.com/mosra/corrade)@[9d03dde6d3...](https://github.com/mosra/corrade/commit/9d03dde6d3bc453ee58b7901f2a9aa8d0574bd1e)
#### Sunday 2023-03-05 12:55:37 by Vladimír Vondruš

Containers: don't use a bool in Triple NoInit test.

It's just too fucking painful with GCC 12 optimizations. Like, I
regularly got an XPASS for this code:

    Triple<float, int, bool> aTrivial{35.0f, 3, true};
    new(&aTrivial) Triple<float, int, bool>{Corrade::NoInit};

    CORRADE_EXPECT_FAIL_IF(!aTrivial.third(), "...");
    CORRADE_COMPARE(aTrivial.third(), true);

HOW ON EARTH can the boolean value fail on check, saying it's false, but
then in another check be true?! And of course no amount of trying to
change it to !(aTrivial.third() == true), or CORRADE_VERIFY(), etc.,
fixed it. The boolean always read as two different values on the two
lines. Amazing compilers, or UB, or I don't know what.

---
## [Therandomhoboo/Yogstation](https://github.com/Therandomhoboo/Yogstation)@[8e3e0b1450...](https://github.com/Therandomhoboo/Yogstation/commit/8e3e0b1450189ebda3b2bc760c036ba6c59c6b6a)
#### Sunday 2023-03-05 13:50:20 by LazennG

adds magmite crusher to the things you can make at the world anvil (#17530)

* FUCK YOU PLASMA CUTTER

* updated it now just waiting on BAIOMU FOR FUCKIN SPRITES

* returned old sprites i had but it's still lacking 1 handed versions

* touched up some of the sprites but STILL NEED ONEHANDED ONES FROM BAIOMU

* FINALLY

---
## [SanliFaez/OS4Physicists](https://github.com/SanliFaez/OS4Physicists)@[7920baf15e...](https://github.com/SanliFaez/OS4Physicists/commit/7920baf15eac070d47b218b36d7392c83c3a5125)
#### Sunday 2023-03-05 14:03:43 by Hendrik_Snijder

Create Readme.MD (#10)

* Create Readme.MD

Hi,

Hereby my ideas for week 8 of the course. In my opinion it is wise to start with a short lecture. After that, we can organize a 'Future (Scientific) Job Information Market'. The grades will be based on mind-maps the students will make. If time is with us, it is possible to let students do an elavator pitch. Hope you like it!

Best,

Hendrik
'

* Rename CourseDevelopment/Readme.MD to CourseDevelopment/Week8/Readme.MD

Changed Folder

* Update Readme.MD

Added e-science centre

* Update Readme.MD

- Goal of the week changed (the goal of week6 was there by accident) 
- line 61, the word traditional is avoided. 
- Footnote on PhD Advantage

* Update Readme.MD

A new option in the tutorial session is created, for the case where the visiting professionals do not have much time.

---
## [kdmukai/seedsigner](https://github.com/kdmukai/seedsigner)@[d2a657f2d4...](https://github.com/kdmukai/seedsigner/commit/d2a657f2d43c6e77e9c48cb1f859e8f4984a5f00)
#### Sunday 2023-03-05 14:34:17 by Marc G

Various edits B4 upstream submission

After a long hiatus, I have finally completed my proposed changes to the software verification section of our readme.

The verification focuses on keybase.io now storing and verifying the 3 online properties (seedsigner.com, twitter.com/seedsigner and github.com/seedsigner)

This makes the key more secure, easier to import and generally less hassle. its also revokable.  

There is more detail about how/why in the expand blocks, but It was suggested to me to keep the instructions straightforward (ie do this and now do that) , so I have reduced focus much on the why. 
However, some basic "why & how" has also been placed in new collapsible sections, at the end of each step. 

Later on, I want to add color to the collapse sections so that they show a natural boundary, but so far that markdown code is elusive to me. ;) 
Done is better than perfect....
The same for getting my external links to open in a new tab/window. sigh. Markdown is ... well....tricky. 

I can make the screenshots smaller. please comment on their size.


The Verification is done in 3 steps:
1. import the public key
2. Verify its the correct key by verying it and then comparing the Key ID to Keybase.io/seedsigner. If it matches, then its the real seedsigner project person that signed.
this is arguablly the most critical step of verifying and hence we ask the user to check for themselves that the key ID from verify is the same as on keybase.io. Hence the Key ID's are blurred in the screenshots. We dont want the user to compare the screenshots to each other. we want them to compare their result to their browser. 

3. Verify that the other files (at this stage just the .zip file) are also not altered. This does a comparision of the various files actual and expected hashes.

If all is well here, then tell the user about their success :). 
Explain the warnings, which ones are benign, and what to do if verification fails.


Lastly, "Write the software to the MicroSD' section - 
I have got draft text for this, but havent published it yet. 
The verify PR is big enough !!

Please review for my PR flow and clarity, I do still want to improve the formatting,  but wanted to get everyone's thoughts before messing with the detailed formatting and line breaks, which are especially painful!

FYI - I have done my screenshots using layers, so it easy to edit in the future. I think they

---
## [Imaginos16/tgstation](https://github.com/Imaginos16/tgstation)@[d55ce0f0bc...](https://github.com/Imaginos16/tgstation/commit/d55ce0f0bcb6c37113c9ec9f0e37facd99b69625)
#### Sunday 2023-03-05 14:35:19 by Jacquerel

Don't create abandoned airlocks with walls underneath them. (#73656)

## About The Pull Request
Fixes #71504

#70237 attempted to remove this and did in some cases, however the case
where the abandoned airlock is able to find an adjacent wall turf to
copy the type of still fails to delete the airlock.
This fixes that.

Also in my testing, the times where it _failed_ to find a nearby wall
turf to copy and spawned a default wall would leave the mapping helper
visible in the round. Oops!

## Why It's Good For The Game

Mapping helpers should always delete themselves when finished.
The airlocks with walls under them are funny once and annoying the rest
of the time. As of that older PR, this continuing to happen is regarded
as a bug.
Also apparently it might be required anyway for Wallening.

## Changelog

:cl:
fix: Maintenance tunnels should no longer sometimes contain airlocks
with walls underneath them.
/:cl:

---
## [assistcontrol/nvim](https://github.com/assistcontrol/nvim)@[a6b0d0f80f...](https://github.com/assistcontrol/nvim/commit/a6b0d0f80f04dc03c3814748ee87c6a4edf67305)
#### Sunday 2023-03-05 15:20:18 by Adam Weinberger

Switch back to mini.completion

Perhaps this experiment wasn't actually about nvim. What this actually
confirms is that @echasnovski knows exactly what he's doing. (With a
clearly significant sample size of 1.)

The main issue with nvim-cmp is that it loads exceptionally slow when
the host is under load. Binding it to InsertEnter makes mini.starter
load faster, but drags the first insert so hard that it's just not
worth it.

cmp has some nice features. Path completion and cmdline completion are
just lovely things to have, and it doesn't interfere with editing in any
way. Float pops up, float goes away; it's there if I want it.

OTOH, mini.completion contains every completion that I actually need,
loads fast, requires literally no setup, and simply works. Signatures
show up exactly when I need them, and the menu simply looks a lot better
(except for how cmp makes the keys it's matching on bold in the popup,
like `*fo*r, *fo*cus, *fo*und`).

There are two frustrating issues with mini.completion (and they're
probably local issues):

1) Inconsistent <CR> behavior
   The ctrl-y_cr key feed doesn't actually feed the <CR> for some reason,
   so I have to stop at the end of each line and check whether a newline
   actually got inserted. Sometimes I get a newline. Sometimes I just get
   a closed popup.

2) Sometimes mini.completion goes absolutely haywire.
   I hit <C-n> and it inserts some text involving pumvisible() many
   dozens of times, and each one gets its own undo point. No idea why
   this happens, but it seems to happen on lua files most often.

---
## [LilDrippyMyFnf/VS-STUPID-UPDATE](https://github.com/LilDrippyMyFnf/VS-STUPID-UPDATE)@[db65a92503...](https://github.com/LilDrippyMyFnf/VS-STUPID-UPDATE/commit/db65a9250370bb9eef725a12d8cef542770e60db)
#### Sunday 2023-03-05 15:34:07 by MyFnf

pico is gone cuz his .png file got lost

fuck you pico NO WAY!!!

---
## [DawfukFR/stellaris_kernel_oneplus_sm8250](https://github.com/DawfukFR/stellaris_kernel_oneplus_sm8250)@[d32ffbccfa...](https://github.com/DawfukFR/stellaris_kernel_oneplus_sm8250/commit/d32ffbccfab53ba0ae0fe59a24509b74ac71dfd4)
#### Sunday 2023-03-05 15:50:19 by Dan Pasanen

power: don't ever reboot to verity red

* We get it, shit's broken. We're flashing custom stuff, shit's bound
  to break. Don't pop this annoying screen up, we're not even using
  verity anyway.

Change-Id: Icd77b70ec1df9108a4ba9e7fd8cb9623b35b78db
Signed-off-by: celtare21 <celtare21@gmail.com>
Signed-off-by: sohamxda7 <sensoham135@gmail.com>
Signed-off-by: Oktapra Amtono <oktapra.amtono@gmail.com>
Signed-off-by: Anush02198 <Anush.4376@gmail.com>
Signed-off-by: Divyanshu-Modi <divyan.m05@gmail.com>
Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>

---
## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[34daca112c...](https://github.com/realforest2001/forest-cm13/commit/34daca112ce6a08b8edfee14811e9c384429ec4e)
#### Sunday 2023-03-05 16:14:17 by Segrain

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
## [selliott512/freedoom](https://github.com/selliott512/freedoom)@[3efe8a0e41...](https://github.com/selliott512/freedoom/commit/3efe8a0e4114414d764d4a1f03400a9a0f2094dd)
#### Sunday 2023-03-05 17:07:53 by mc776

levels: fix various bugs. (#871)

* levels: fix various bugs.

Thanks to Goji!, Inuk and rednakhla on Discord for pointing these out.


E1M3: Northern lift simplified to address texture alignment problems.

E1M5: Door near (-205,1336) (leading out into open ceiling area with the big strip of lights down the middle) door tracks needed to be lower unpegged.

E1M9: Lift near (-2328,120) was split into 2 sectors, causing HOMs when they went out of sync. There's nothing that relies on this split (contrast the neat lighting stuff from Map22) so the lift is just merged into one sector.

E2M2: Shellbox near (-486,192) is right on the line between two stairs, causing it to rest on the bottom step which causes ports like GZDoom to have the sprite clip *very* visibly into the upper stair. Moved it slightly so it rests on the upper of those two stairs.

E2M3: Door leading to red key and "door" leading to soulsphere: former should be lower unpegged but latter should not, but were reversed. Two exit-door-textured doorframes also given more conventional DOORTRAK and lower unpegged treatment. The teleporter representing the hatch going down into the nukage is now fully repeatable.


Map07: Infinite height in vanilla would cause the spectres in the red key courtyard to trap the player on the entrance ledge from below in a way that could not be seen or diegetically explained. Those three spectres now warp in only after you cross the ledge. (Setting them to "ambush" would do nothing since you're in LOS with them from the top of the ledge.)

Map11: Lights above red keycard weren't aligned; moved that entire sector and added a few lines to round the corner. Removed a strobe effect on the exit teleporter to compensate for a GZDoom issue where the light would go to absolute zero during the blink.

Map12: Room to the south with the 2 stimpacks, ammo boxes, 2 chaingunners and berserk would sometimes cause some of the items to be "levitated" to the highest sectors they touch. Moved them away from said higher sectors - it looks a bit sloppier but this is a backroom not a storefront lol.

Map13: The easternmost archvile platform had the archvile stuck in the seam, preventing it from lowering in vanilla. (Worked fine in GZDoom) Moved it a little further in.

Map19: The combat slugs teleport in from a W1 teleporter which could sometimes be spent while one of the pinkies is blocking the destination, permanently preventing that slug from teleporting in. These are now WRs like the other teleporting enemies.

Map22: More W1 monster teleports that should be WR. Also filled in some missing textures in the multi-sector lift connecting the cavern to the hall in the southwest, which parts are clearly not meant to be seen moving separately but can - it still looks fucked up if you manage to desync them, but it's a diegetic fucked up now.

Map24: Another W1 spawn. This one is impossible to screw up in vanilla, but there are some mods that could end up spawning something there that could block the archviles from teleporting.

Map25: More W1 problems. The spawn source room now also has a small barrier to make sure each pinkie only goes to its own teleporter unless the initial teleport fails.

Map27: Lizardbaby dropping too far meant that the bracket was falling along with it in a visibly unnatural way.

Map29: Broke up all the long linedefs on the perimeter of the map to get around the invisible hitscan barrier bug: https://doomwiki.org/wiki/Hitscan_attacks_hit_invisible_barriers_in_large_open_areas
(Ideally this entire perimeter should be redone to break up the box in favour of more natural-looking formations, but that's a bit outside the scope of a fix like this.)


Also got rid of the Plutonia-style start/end teleports on the fixed Phase 2 maps, to address #867.

* maps: more fixes.

More floaty items and other things.

E1M9
- floater mid south stim by staircase
E1M7
- floater northwest clips near the tunnels
- floaters near switch by railings, now all on the railings
- duckproofed sector 439 barrier
E2M9
- floater thing #125 medikit on top of lift, now in middle of platform
- shotgun guy (thing #309) and the spectre behind it stuck in geometry.
- lines 430 and 761 both open the same door and are in the same room right next to each other. Since 761 is actually textured and positioned as a switch, the tag and special on 430 is removed.

* levels: flag e2m7 DM stuff as multi-only.

Marked the following based on eyeballing out what items are right next to DM spawns with no obvious alternate route to them: 487, 488; 203, 397; 499, 500, 501, 502; 482, 485; 491, 492, 493; 494; 496; 28, 486; 182; 54

* levels: more misc. fixes.

E1M6 W1 lines 2318 and 2321.

E3M5 Removed all monster block lines in that gross blood room and raised the blood floor to only 4 below the normal floors, but flagged more monsters in there as ambush to make up for it. Also fixed a lot of texture alignment issues in the top skin panels and lowered the ceiling, along with adding a new sector to address texture tiling issues in the northern teleporter room.

E4M1 fixed a mysterious HOM that was going on near the northern shadow line in the northern outdoor area. Merged a lot of sectors that were identical in their properties.

E4M7 entrance to sector 985 seems to be intended that the player run off the ledge into that room, then the pinkie near the ledge ambushes the player from behind. Instead, what sometimes happens is that the pinkie is alerted somehow, then obstructs the player (vanilla infinite height) from being able to get down there. That means of getting down into that room is now walled off, and instead you step onto that lift to bring it down from above. Neat side effect: any monsters still in the ring when you enter that room will follow you down there.

E4M5 linedefs 1724 and 1725 were facing the wrong way and couldn't be hit with projectiles.

Map25 Float thing 217. Moved that entire row further south to address floating item issues.

Map28 Float thing 464.

* levels: use inner room texture in E4M7 lift.

* levels: align side textures on that lift.

Didn't realize the little squares were sticking into the floor at the *bottom* of the lift as well.

---
## [AshfordGraye/ProjectRPG](https://github.com/AshfordGraye/ProjectRPG)@[9fc7ba666e...](https://github.com/AshfordGraye/ProjectRPG/commit/9fc7ba666ea976d6e6a86edc2120ac65a11e55bb)
#### Sunday 2023-03-05 17:48:10 by Ash

A learning experience I'm sure all programmers go through...

After a machine restore and cloning the repo back from GitHub it became apparent that all local files previously present but assigned to .gitignore had been lost - including the OriginalAppBuild folder which included the original application from which this unfinished one was built. 

Well, obviously - I told it to ignore them didn't I...

The absolute kicker? I deleted the backup while cleaning up my documents folder on autopilot before restoring my machine...

A classic example of being reminded the hard way that computers do EXACTLY what you tell them to and that having backups are only good if you keep them somewhere you wont touch them by mistake.

The only upshots here are that my written work was in a totally separate location, and the actual code itself is of course exactly how I Ieft it - Praise the Omnissiah.

This commit recreates a documents folder and adds the base files for some documents I can recreate easily like the .drawio files. Added the assignment brief and some files for code snips and pseudocode writing for the assignment itself. The OriginalAppBuild is completely gone - there's no way I can reverse engineer what the code has now turned into back into what it was. Be like turning an omelette back into eggs.

---
## [Zotlan/szakdoga](https://github.com/Zotlan/szakdoga)@[25c91b077b...](https://github.com/Zotlan/szakdoga/commit/25c91b077b80c9c4e6f7540e83a8f86e5df7a77c)
#### Sunday 2023-03-05 18:12:17 by Zotlan

THE CHAT IS LIVE

IT WAS 3 LINES OF CODE.
So the chat is now live, it needs some refinement, such as accepting special characters, but FUCK YEAH, it works.
Furthermore the forum page is close to completion in terms of displaying things.
I decided to make my own modals instead of bootstrap ones. I'm halfway through with making those, one works completely, the second one is smei working, as in the form inside it does nothing yet, and the third one still uses the bootstrap one.
The site now uses session_destroy instead of unset at Kori's suggestion.
Also umm a mistake was made a while ago I maaaaaaaay have forgotten to *PROPERLY* set up the connections between the tables, they were all in restrict, now in cascade. I'll fix most issue with the chat tomorrow and I think I'll leave the rest of the forum page for the rest of the week, mostly the weekend, and I'll do the profile page next week. After that... I think I'm done after that, just beautifying and thats it, also the documentation but I don't have to commit that.

Song: Emerald Sword
Artist: Rhapsody of Fire

---
## [akgold/do4ds](https://github.com/akgold/do4ds)@[fb3ea55ad1...](https://github.com/akgold/do4ds/commit/fb3ea55ad12bc80c44c220179238a6cb6fa10f89)
#### Sunday 2023-03-05 18:18:29 by Jon Harmon

Typos and notes for Chapter 11 (#132)

* Typos and notes for Chapter 11 (does not include lab).

- I don't think the intro paragraph has been updated to match the new structure.
- I thought sure footnote 2 was going to tell me more about the "amusingly nonchalant newsgroup posting." Provide a link or something!
- People make a big deal of the difference in slashes on Windows, but (unless I'm not aware of a situation) Windows is fine with forward slash. I feel like non-Windows-users make a big deal of working around this historical artifact, and it just makes things confusing.
- The table just before the "Installing Stuff" section has some weird spaces inside words. I didn't remove them because I'm not sure why they're there. I know Quarto's visual mode was playing with that table a bit (I had to be careful not to screw it up), but the weird spacing was already there.

* Lab tweaks and notes.

- Lines 829+: This doesn't happen on Windows (tested in both gitbash and PowerShell). Are you sure this is happening on the AWS side, and not on the shell side? My do4ds-lab-key.pem has -rw-r--r--, so it looks like it's 644 just like yours. Alternatively, did you maybe set something up not-quite-default in your version of the lab?
- Line 920: I softened the "what -aG stands for" line a bit so people don't feel dumb if they didn't notice.
- Line 962: I still need to give it the pem directly. Shouldn't I have to do that? I assume it's because we haven't set up SSH config for this server yet. Since that hasn't happened, everything past here needs the key (see below).
- Line 967: You mean the root user pem key, right? Or do you mean the test-user pem key?
- Line 1042: Since we haven't set up this key permanently anywhere, evvery ssh command needs to include the key. I'm actually not sure where to put the key info in a tunnel. Edit: googling told me to do ssh -i <key> -N -L <etc as you show>, but I don't know what -N is doing there. Without the -N, it logs me in.
- I didn't do the Jupyter part of the lab because I hate working with Python; that's why I'm all-in on R. I'm sure someone else in the club will go through those steps!
- It would be helpful to have a numbered list of short steps at the end of each lab, so I can easily kill a server but then rerun those steps later. I know there are easier ways to do that, but I'm trying to get in the habit of burning it all down and going through it again, partly to get muscle memory on the basic steps.
- I removed a use or two of "just." That's generally seen as a word to avoid in education, 'cuz it makes people feel really dumb when they find that step difficult the first time they try it.
- Line 1214+: Wait, I should notice it isn't daemonized? Where did we discuss daemons? In general, this pair of paragraphs seems to take away from the very cool step we just got working. Maybe hide it in a footnote or a call out? Since we aren't resolving it, all it feels like it does is lessen the satisfaction I had with this chapter moments before the warning 🙃

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[9c28e48bea...](https://github.com/treckstar/yolo-octo-hipster/commit/9c28e48beac6938ee35db2e76c1b59be5ebd7aed)
#### Sunday 2023-03-05 18:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Danielkaas94/TheChessSpeaksForItself](https://github.com/Danielkaas94/TheChessSpeaksForItself)@[2e98565ca2...](https://github.com/Danielkaas94/TheChessSpeaksForItself/commit/2e98565ca2a42167a8a6651bf4405acb8ece283a)
#### Sunday 2023-03-05 19:08:13 by Danielkaas94

🔰🔰 BLAME FUCKING CANADA! 🔰🔰

God damn it I hate myself when I blunder so fucking badly,
because I am tired like a little baby 🥱

WHY DOES FATIGUE EXIST? 😫

---
## [Offroaders123/Smart-Text-Editor](https://github.com/Offroaders123/Smart-Text-Editor)@[8e6100931d...](https://github.com/Offroaders123/Smart-Text-Editor/commit/8e6100931dd39c57a528eacd2e88a479782e0585)
#### Sunday 2023-03-05 19:34:19 by Offroaders123

Enigmatic Glue Code

Got everything working again! Now the Editor opening sequences work correct in all situations once again, and now syncing the app's state with it's Local Storage settings now works back and forth, once again.

Finding out that there are still hidden gems of wonk sprinkled throughout the codebase, even with the "type-safety". I think it was mostly due to my `any` typing for the `STE.settings` object though, that broke some things and caused some hidden unintended consequences for me.

So currently the values returned from `STE.settings.get()` are always either `string | undefined`, and sometimes I was checking them as bare values, like `boolean`, which works fine in non-strict mode, with `==` and `!=` checks (I didn't know I was specifically relying on this for getting things to work). So, it was a big collection of things. I moved the script to run in ESM (enabling strict-mode), the `STE.settings` object wasn't type-safe enough, hiding the type checking error, and the fact that the `STE.settings` object always returns strings is not something I like XD

Ok, and for the Editor opening issues, it looks like it was because the Editor constructor code is specifically relying on how certain things are called, which I hadn't noticed when refactoring them. So, I reorganized things a bit to make it read nicer, but it turns out that it only runs correctly in the original order, because some calls rely on other things to have already happened. Now that it's working again at least, I know what that order is, and I can abstract things out so it's easier to see what each stage of the constructor is, at least.

Part of that, I can now make the `Editor` class into an extension of the `NumTextElement` component itself, allowing me to hopefully be able to remove the `STE.query()` function, as I can instead just access the Editor's components directly from the element's properties itself, instead of querying all over the document using it's identifier.

I love how much you really don't know when you first start out, some of these old design decisions are completely baffling to me how, and it's hilarous XD

Either way, I'm still very proud of how much I was able to pull out of the original codebase, with my limited experience so far too. STE is and has been very capable with lots of great features and ideas, I just hadn't learned about the best design decisions to build it yet. I'm also very happy with having things like Git, because I can see how this donkey show has progressed over the years XD (tried to think of a weird phrase to explain how goofy STE is; oops, it's a bad thing that already existings! my bad XD) It's very cool to be able to see how my opinions on building things has changed over time, and see which things have and haven't worked for me, and what I ended up going with for a given roadblock. I think messages like these are very awesome to have too, it's really neat to be able to reflect on things so close to what you're actually working on. It's tightly coupled with the actual project and you can see how things correlate together.

Listening to '40 years', 'A Mouth of God' by Marco Minnemann, and I listened to 'The Scambot Holiday Special' - Mike Keneally just before this; both awesome experimental prog albums :)

Oh yeah, and Lunatic Soul 'Through Shaded Woods' before those two :)

Gonna try to push the current state of this branch, to the main branch. Everything *should* be ready for that now, but you never know 'till you try! Currently the main branch and live site are running the 'Workspace Module' commit.

---
## [GitHubSecurityLab-CodeAnalysis/tgstation_tgstation](https://github.com/GitHubSecurityLab-CodeAnalysis/tgstation_tgstation)@[374c8340c8...](https://github.com/GitHubSecurityLab-CodeAnalysis/tgstation_tgstation/commit/374c8340c8c99586a4b4b8e978947c0b0f83a9d7)
#### Sunday 2023-03-05 20:25:11 by Jacquerel

Console Hack / Unfavourable Events won't run ghost roles which don't have time to do anything (#73343)

## About The Pull Request

Fixes #69201
The dynamic subsystem will never roll a new antagonist once the shuttle
is past the point of no return, but this check is bypassed by Console
Hacks and Unfavourable Event rolls (which are chiefly triggered from
console hacks, but also from when the Revolution wins).

I have made these procs more discerning.
Unfavourable Events will now never pick any heavy dynamic midround if
the shuttle is past the point of no return.
Console Hacking will now never spawn sleeper agents if the shuttle is
past the point of no return, and won't spawn Fugitives or Pirates if the
shuttle is called at all even if it can still be recalled

It's my feeling that given the need to get organised and move a ship to
the station there isn't really time for either of those events to
actually start properly rolling, but if you feel like that information
might be metagamed in some way by messing around with the shuttle (not
sure why or to what end, but it's technically manipulatable if you know
how the code works?) I can just give these the same restriction as
Traitor even if it means the bounty hunters risk showing up after the
shuttle has already left.

## Why It's Good For The Game

To some extent it's your own fault for clicking the popup while knowing
full well how much round time is left until the game ends, but it's
still disappointing to see a Blob or Pirates or Wizard alert appear at a
time when they can't possibly do anything interesting.
This is more true for the Pirate and Fugitive events because they
involve teamwork, placing a space ship, travel between the ship and the
station, and in the case of Fugitives its own internal five minute timer
before the other team actually arrives.

## Changelog

:cl:
fix: Hacking the Comms Console or winning a Revolution can no longer
spawn antagonists if there's not enough time left in the round for them
to antagonise anyone.
/:cl:

---
## [GitHubSecurityLab-CodeAnalysis/tgstation_tgstation](https://github.com/GitHubSecurityLab-CodeAnalysis/tgstation_tgstation)@[645054b489...](https://github.com/GitHubSecurityLab-CodeAnalysis/tgstation_tgstation/commit/645054b489212a34d80e6e1a7fa1320e35d9bfc7)
#### Sunday 2023-03-05 20:25:11 by MrMelbert

Fixes encoding on syndicate declaration of war, Fixes a way to send unencoded text to newscasters (#73366)

## About The Pull Request

Ugly


![image](https://user-images.githubusercontent.com/51863163/218280311-f282bd75-2f6e-4290-b3f4-d9d856ff36d3.png)

Nice


![image](https://user-images.githubusercontent.com/51863163/218280315-233da635-f777-4006-8778-c673b83e887e.png)

War dec: 

- TGUI inputs for syndicate declaration of war no longer double-encode
sending customized messages into the announcement
- The alert box for the war declaration no longer has multiple errors
(an extra bracket, negative seconds)
- Reduces some copy and paste in the war declaration device
- Adds a debug item that's a war declaration device but it only does the
sound and message. Please don't fake war decs admins it's a horrible
idea

Additionally

- Documented `priority_announcement`
- Ensures all uses of text and title in the priority announcement
message are encoded (Some were not!)

## Why It's Good For The Game

Encoding looks bad, unencoded text is also bad

## Changelog

:cl: Melbert
fix: Syndicate declarations of war no longer murder apostrophes and
their friends
fix: The alert box for the declaration of war no longer looks funky, and
counts forwards in time rather than backwards
fix: Fixed being able to send unencoded HTML to newscasters
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [Ladysnake/Requiem](https://github.com/Ladysnake/Requiem)@[a86ed30451...](https://github.com/Ladysnake/Requiem/commit/a86ed3045187fc9363da7ae1a3b5e5e0793249f9)
#### Sunday 2023-03-05 21:06:59 by Pyrofab

Happy new year folks!!!

Stay proud, stay safe, and do what the hell you want. And hey, find yourself some friends with which to overthrow oppressive systems while you're at it.

---
## [newstools/2023-iol-daily-news](https://github.com/newstools/2023-iol-daily-news)@[f4d495c834...](https://github.com/newstools/2023-iol-daily-news/commit/f4d495c83415102d4c32d77960f4b1d9f0946adf)
#### Sunday 2023-03-05 21:08:20 by Billy Einkamerer

Created Text For URL [www.iol.co.za/dailynews/news/dailynews/news/man-on-parole-jailed-for-life-for-raping-woman-who-owed-him-for-what-her-boyfriend-did-for-her-9a643b1d-a813-4b5a-8ee7-893743101130]

---
## [nightmarish-warlord/Shiptest](https://github.com/nightmarish-warlord/Shiptest)@[d21740b475...](https://github.com/nightmarish-warlord/Shiptest/commit/d21740b475aea65de3b250a5aea26a69677e30e8)
#### Sunday 2023-03-05 22:25:12 by tmtmtl30

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
## [BarteG44/Shiptest](https://github.com/BarteG44/Shiptest)@[31eabb62f1...](https://github.com/BarteG44/Shiptest/commit/31eabb62f1bfe944a58fa6b74d1745cf80cb83aa)
#### Sunday 2023-03-05 23:05:21 by spockye

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

