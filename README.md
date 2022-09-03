## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-09-02](docs/good-messages/2022/2022-09-02.md)


2,071,741 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,071,741 were push events containing 3,098,741 commit messages that amount to 230,293,680 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 40 messages:


## [1048-Team/1048_dev](https://github.com/1048-Team/1048_dev)@[8747dda107...](https://github.com/1048-Team/1048_dev/commit/8747dda107ea77307f6cc4fa8427b08ebe3ae5ba)
#### Friday 2022-09-02 00:43:51 by Lord Protectress Rose

SINGULAR EVENT LOC DONE, IN AN HOUR!

I hate my life.

---
## [Arturlang/tgstation](https://github.com/Arturlang/tgstation)@[20e4add487...](https://github.com/Arturlang/tgstation/commit/20e4add48712b59e9bcadd187beee54c02f98e38)
#### Friday 2022-09-02 01:27:01 by Tim

Change healing by sleeping to be affected by sanity, darkness (or blindfold), and earmuffs. (#65713)


About The Pull Request

Depending on the mob's sanity level, it can have a positive or negative boost to healing effects while sleeping. Sleeping in darkness, wearing a blindfold, and using earmuffs also counts as a healing bonus. Beauty sleep is very important for 2D spessmen.
Why It's Good For The Game

This is a small gameplay change that rewards players for keeping their sanity at good levels. Also depression has also been linked with impeding wound healing in real life. The placebo effect on peoples minds is strenuously documented and I think it would be cool to see it in the game.
Changelog

cl
expansion: Healing by sleeping is now affected by sanity, sleeping in darkness (or using a blindfold), and using earmuffs. The healing from sleeping in a bed was slightly decreased.
/cl

---
## [6165-MSET-CuttleFish/TeamTrack](https://github.com/6165-MSET-CuttleFish/TeamTrack)@[c8f1c3a458...](https://github.com/6165-MSET-CuttleFish/TeamTrack/commit/c8f1c3a4587ae0bb68fa9d2152d5b018d2914f14)
#### Friday 2022-09-02 01:53:59 by jiru-shan

okay delete button is done i hate everything especially my sleep schedule

i love egirl asmr & playing Azur Lane at 1AM in the morning. It's very fun and is definitely not me coping while having to write dogshit code that may or may not work. Also the cloud function is a slight(larger) vulnerability, but I wrote some potential fixes in comments on index.ts.

---
## [hauntsaninja/black](https://github.com/hauntsaninja/black)@[0019261abc...](https://github.com/hauntsaninja/black/commit/0019261abcf6d9e564ba32d3cc15534b9026f29e)
#### Friday 2022-09-02 02:07:54 by Richard Si

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
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[e7230e8b4a...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/e7230e8b4a6d60e1b6c025b52b9f3d2fc26577a5)
#### Friday 2022-09-02 02:11:41 by SkyratBot

[MIRROR] Resolves is_banned_from headaches and lag (Speeds up roundstart significantly) [MDB IGNORE] (#16001)

* Resolves is_banned_from headaches and lag (Speeds up roundstart significantly) (#69376)

About The Pull Request

Just to be clear, when I refer to time here, I am not talking about cpu time. I'm talking about real time.
This doesn't significantly reduce the amount of work we do, it just removes a lot of the waiting around we need to do for db calls to finish.

Adds queuing support to sql bans, so if an ongoing ban retrieval query is active any successive ban retrieval attempts will wait for the active query to finish

This uses the number/blocking_query_timeout config option, I hope it's still valid

This system will allow us to precache ban info, in parallel (or in batches)
With this, we can avoid needing to setup all uses of is_banned_from to support parallelization or eat the cost of in-series database requests

Clients who join after initialize will now build a ban cache automatically

Those who join before init is done will be gathered by a batch query sent by a new subsystem, SSban_cache.

This means that any post initalize uses of is_banned_from are worst case by NATURE parallel (since the request is already sent, and we're just waiting for the response)

This saves a lot of headache for implementers (users) of the proc, and saves ~0.9 second from roundstart setup for each client (on /tg/station)

There's a lot of in series is_banned_from calls in there, and this nukes them. This should bring down roundstart join times significantly.

It's hard to say exactly how much, since some cases generate the ban cache at other times.
At base tho, we save about 0.9 seconds of real time per client off doing this stuff in parallel.
Why It's Good For The Game

    When I use percentages I'm speaking about cost per player

I don't like how slow roundstart feels, this kills about 66% of that. the rest is a lot of misc things. About 11% (it's actually 16%) is general mob placing which is hard to optimize. 22% is manifest generation, most of which is GetFlatIcons which REALLY do not need to be holding up the main thread of execution.

An additional 1 second is constant cost from a db query we make to tell the server we exist, which can be made async to avoid holding the proc chain.

That's it. I'm bullying someone into working on the manifest issue, so that should just leave 16% of mob placing, which is really not that bad compared to what we have now.
Changelog

cl
code: The time between the round starting and the game like, actually starting has been reduced by 66%
refactor: I've slightly changed how ban caches are generated, admins please let me know if anything goes fuckey
server: I'm using the blocking_query_timeout config. Make sure it's up to date and all.
/cl

* Resolves is_banned_from headaches and lag (Speeds up roundstart significantly)

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[c3f50d2d14...](https://github.com/Buildstarted/linksfordevs/commit/c3f50d2d14213b576db13ec043f95a6e57d659ba)
#### Friday 2022-09-02 02:42:29 by Ben Dornis

Updating: 9/1/2022 8:00:00 PM

 1. Added: Webhooks.fyi
    (https://webhooks.fyi/)
 2. Added: Kagi status update: First three months
    (https://blog.kagi.com/status-update-first-three-months)
 3. Added: Snapcast
    (https://mjaggard.github.io/snapcast/)
 4. Added: Alexandre Nédélec - How did I automate the setup of my developer Windows laptop?
    (https://www.techwatching.dev/posts/automate-developer-machine)
 5. Added: Windows Devs Prefer PowerShell as CLI -- Visual Studio Magazine
    (https://visualstudiomagazine.com/articles/2022/09/01/cli-survey.aspx)
 6. Added: Merge Editor Improvements Highlight VS Code 1.71 (August 2022 Update) -- Visual Studio Magazine
    (https://visualstudiomagazine.com/articles/2022/09/01/vs-code-1-71.aspx)
 7. Added: The Portuguese Can No Longer Afford To Live in Portugal (Or Even Survive)
    (https://medium.com/the-portuguese/the-portuguese-can-no-longer-afford-to-live-in-portugal-or-even-survive-eaa8fdffc4b9)
 8. Added: On Artificial Intelligence in User Experience Design
    (https://blog.willgrant.org/2022/08/30/on-artificial-intelligence-in-user-experience-design.html)
 9. Added: Fireside
    (https://player.fireside.fm/v2/UDzB5o3V+Z6hgS1Xp/twitter)
10. Added: .NET Rocks! ALM for Power Platform with Kartik Kanakasabesan
    (https://www.dotnetrocks.com/details/1807)
11. Added: Microsoft Reactor | Microsoft Developer
    (https://developer.microsoft.com/en-us/reactor/events/16947/)
12. Added: Announcing Entity Framework Core 7 Preview 6: Performance Edition
    (https://devblogs.microsoft.com/dotnet/announcing-ef-core-7-preview6-performance-optimizations/)
13. Added: .NET Rocks! Microservices Architectures with Shawn Wildermuth
    (https://www.dotnetrocks.com/details/1809)
14. Added: On .NET Live - Microservice applications with DAPR and .NET
    (https://youtube.com/watch?v=kIfmwmJHNMs)
15. Added: - Top End Devs
    (https://topenddevs.com/podcasts/adventures-in-net/episodes/blazor-in-action-net-130-part-1)
16. Added: Experience after Three Months of Daily Journaling | Ben Bolte's Blog
    (https://ben.bolte.cc/journaling)
17. Added: Large Update of the EF Core UI plugin for JetBrains Rider
    (https://blog.seclerp.me/general/ef-core-inside-rider-large-update/)
18. Added: Generating Code Coverage Metrics for .NET Framework Applications
    (https://dev.to/calvinallen/generating-code-coverage-metrics-for-net-framework-applications-5dl2)
19. Added: Customizing your controls with Platform Behavior | .NET Conf: Focus on MAUI
    (https://youtube.com/watch?v=khBN1AIL_OM)
20. Added: UI Design for .NET MAUI | .NET Conf: Focus on MAUI
    (https://youtube.com/watch?v=2uiRwG2wu7E)
21. Added: Beginning gRPC with ASP.NET Core 6: Build Applications using ASP.NET Core Razor Pages, Angular, and Best Practices in .NET 6: Giretti, Anthony: 9781484280072: Books - Amazon.ca
    (https://www.amazon.ca/dp/1484280075/ref=cm_sw_r_api_i_YPM5TPFWQCNP6JDAZ30B_0?tag=linksfordevs-20&lfd=202209)
22. Added: Loss of Signal in between YouTube ads
    (https://old.reddit.com/r/appletv/comments/x0qhx1/loss_of_signal_in_between_youtube_ads/)
23. Added: Security of ZK Systems
    (https://www.eventbrite.com/e/security-of-zk-systems-tickets-405523681247)
24. Added: Stanford Blockchain 2022 on Livestream
    (https://livestream.com/accounts/1973198/blockchain-2022)
25. Added: Unsecure Server Exposed 200 Million Records of Adult Webcam Models and Users Online
    (https://www.bitdefender.com.au/blog/hotforsecurity/unsecure-server-exposed-200-million-records-of-adult-webcam-models-and-users-online/)
26. Added: DDD North 2022: Call for Speakers/Papers
    (https://sessionize.com/ddd-2022/)
27. Added: Troy Hunt on ATO: Account Takeovers as the Hidden Threat
    (https://event.on24.com/wcc/r/3777870/4F6926F9F9B725B3480A34C013550056)
28. Added: Meta’s next VR headset will launch in October
    (https://arstechnica.com/gadgets/2022/08/metas-next-vr-headset-will-launch-in-october/)
29. Added: How We Do Our Best Work
    (https://joeblu.com/blog/2022_09_best_work/)
30. Added: TechEmpower Web Framework Performance Comparison
    (https://www.techempower.com/benchmarks/#section=)
31. Added: formal verification of KEMTLS via Tamarin
    (https://eprint.iacr.org/2022/1111)
32. Added: ASP.NET Community Standup - Dapr + .NET
    (https://youtube.com/watch?v=VkJQR854S1s)
33. Added: .NET Rocks! Twenty Years of .NET Rocks!
    (https://www.dotnetrocks.com/details/1808)
34. Added: .NET MAUI Step by Step Build
    (https://youtube.com/watch?v=LrZwd-f0M4I)
35. Added: - Top End Devs
    (https://topenddevs.com/podcasts/adventures-in-net/episodes/blazor-in-action-net-131-part-2)
36. Added: Search results for "erikej", Visual Studio on Visual Studio Marketplace
    (https://marketplace.visualstudio.com/search?term=erikej&target=VS&category=All%20categories&vsVersion=vs2022&sortBy=Relevance)
37. Added: GitHub Universe 2022
    (https://githubuniverse.com/?scid=)
38. Added: The Jungle of Metrics Layers and its Invisible Elephant
    (https://aurimas.eu/blog/2022/08/metrics-layers-and-power-bi/)
39. Added: Announcing the Open Sourcing of Paranoid's Library
    (https://security.googleblog.com/2022/08/announcing-open-sourcing-of-paranoids.html)
40. Added: Anthony Giretti | ConFoo.ca
    (https://confoo.ca/en/2023/call-for-papers/speaker/anthony-giretti)
41. Added: Finally Released: 3-Column Merge Editor in VS Code!
    (https://javascript.plainenglish.io/finally-released-3-column-merge-editor-in-vs-code-8490ef694b3a)
42. Added: Unit Testing For Your .NET MAUI Applications | .NET Conf: Focus on MAUI
    (https://youtube.com/watch?v=b4OJSmgMAaw)
43. Added: Streaming Videos from Azure Blob Storage
    (https://dotnetthoughts.net/streaming-videos-from-azure-blob-storage/)
44. Added: Comment déployer un noeud validateur Mina et déléguer vos MINA : le tuto complet
    (https://journalducoin.com/actualites/comment-deployer-noeud-validateur-mina-delegation-tuto-complet/)
45. Added: Windows 7 Starter is a (small) gamble for Microsoft
    (https://arstechnica.com/gadgets/2009/04/i-agree-windows-7-starter-is-a-small-gamble-for-microsoft/)

Generation took: 00:03:50.5841219

---
## [ktoma36/Citadel-Station-13-RP](https://github.com/ktoma36/Citadel-Station-13-RP)@[24aca0ae55...](https://github.com/ktoma36/Citadel-Station-13-RP/commit/24aca0ae55ce2204474ec23fed6d23cb46b6645e)
#### Friday 2022-09-02 02:55:35 by LordPapalus

Cargonia, but with less weapons (#4370)

* Cargonia is no more

Fuck you

* PLEASE

* Zandario, I will suck your PP

---
## [scriptis/tgstation](https://github.com/scriptis/tgstation)@[6f2354e694...](https://github.com/scriptis/tgstation/commit/6f2354e694f3412a76b383f684a0bfc85a448d8e)
#### Friday 2022-09-02 03:24:05 by san7890

Fixes Fucked Job Requirement Displays (#69368)

* Fixes Fucked Job Requirement Displays

Hey there,

I fucked up in #68856 (5b77361d399ba0dd992e61a16b9bbe38e8aa5a60). We weren't supposed to add another MINUTES multiplication here. I don't even remember why I did this if we are being perfectly honest with each other. Whoops.

fix: You should now no longer need thousands of hours to unlock your favorite head of staff role.

---
## [ngzhekai/Green-Commit-Quotes](https://github.com/ngzhekai/Green-Commit-Quotes)@[897ec129a5...](https://github.com/ngzhekai/Green-Commit-Quotes/commit/897ec129a5ec7ce31f1970a5a281c407bb16f58e)
#### Friday 2022-09-02 04:06:12 by Hatsune Miku

You purchase pain with all that joy can give and die of nothing but a rage to live.

---
## [Sabin-Subedi/react](https://github.com/Sabin-Subedi/react)@[b6978bc38f...](https://github.com/Sabin-Subedi/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Friday 2022-09-02 04:48:28 by Andrew Clark

experimental_use(promise) (#25084)

* Internal `act`: Unwrapping resolved promises

This update our internal implementation of `act` to support React's new
behavior for unwrapping promises. Like we did with Scheduler, when 
something suspends, it will yield to the main thread so the microtasks
can run, then continue in a new task.

I need to implement the same behavior in the public version of `act`,
but there are some additional considerations so I'll do that in a
separate commit.

* Move throwException to after work loop resumes

throwException is the function that finds the nearest boundary and
schedules it for a second render pass. We should only call it right 
before we unwind the stack — not if we receive an immediate ping and
render the fiber again.

This was an oversight in 8ef3a7c that I didn't notice because it happens
to mostly work, anyway. What made me notice the mistake is that
throwException also marks the entire render phase as suspended
(RootDidSuspend or RootDidSuspendWithDelay), which is only supposed to
be happen if we show a fallback. One consequence was that, in the 
RootDidSuspendWithDelay case, the entire commit phase was blocked,
because that's the exit status we use to block a bad fallback
from appearing.

* Use expando to check whether promise has resolved

Add a `status` expando to a thrown thenable to track when its value has
resolved.

In a later step, we'll also use `value` and `reason` expandos to track
the resolved value.

This is not part of the official JavaScript spec — think of
it as an extension of the Promise API, or a custom interface that is a
superset of Thenable. However, it's inspired by the terminology used
by `Promise.allSettled`.

The intent is that this will be a public API — Suspense implementations
can set these expandos to allow React to unwrap the value synchronously
without waiting a microtask.

* Scaffolding for `experimental_use` hook

Sets up a new experimental hook behind a feature flag, but does not
implement it yet.

* use(promise)

Adds experimental support to Fiber for unwrapping the value of a promise
inside a component. It is not yet implemented for Server Components, 
but that is planned.

If promise has already resolved, the value can be unwrapped
"immediately" without showing a fallback. The trick we use to implement
this is to yield to the main thread (literally suspending the work
loop), wait for the microtask queue to drain, then check if the promise
resolved in the meantime. If so, we can resume the last attempted fiber
without unwinding the stack. This functionality was implemented in 
previous commits.

Another feature is that the promises do not need to be cached between
attempts. Because we assume idempotent execution of components, React
will track the promises that were used during the previous attempt and
reuse the result. You shouldn't rely on this property, but during
initial render it mostly just works. Updates are trickier, though,
because if you used an uncached promise, we have no way of knowing 
whether the underlying data has changed, so we have to unwrap the
promise every time. It will still work, but it's inefficient and can
lead to unnecessary fallbacks if it happens during a discrete update.

When we implement this for Server Components, this will be less of an
issue because there are no updates in that environment. However, it's
still better for performance to cache data requests, so the same
principles largely apply.

The intention is that this will eventually be the only supported way to
suspend on arbitrary promises. Throwing a promise directly will
be deprecated.

---
## [ammarfaizi2/linux-block](https://github.com/ammarfaizi2/linux-block)@[700b6b6170...](https://github.com/ammarfaizi2/linux-block/commit/700b6b6170cef3a173f9e701e036c56b8b4e2311)
#### Friday 2022-09-02 05:15:58 by Peter Zijlstra

x86/nospec: Unwreck the RSB stuffing

commit 4e3aa9238277597c6c7624f302d81a7b568b6f2d upstream.

Commit 2b1299322016 ("x86/speculation: Add RSB VM Exit protections")
made a right mess of the RSB stuffing, rewrite the whole thing to not
suck.

Thanks to Andrew for the enlightening comment about Post-Barrier RSB
things so we can make this code less magical.

Cc: stable@vger.kernel.org
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Link: https://lkml.kernel.org/r/YvuNdDWoUZSBjYcm@worktop.programming.kicks-ass.net
[bwh: Backported to 5.10: adjust context]
Signed-off-by: Ben Hutchings <benh@debian.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [JohnFulpWillard/tgstation](https://github.com/JohnFulpWillard/tgstation)@[bc90ded5b8...](https://github.com/JohnFulpWillard/tgstation/commit/bc90ded5b8b0f4487ccec227fed24f514dbaa5ba)
#### Friday 2022-09-02 05:38:39 by MrMelbert

Buffs Heretic Curses, Living Heart, Leeching Walk, and technically Entropic Plume by fixing some bugs (#69181)

About The Pull Request

    Heretic curses have been buffed / reworked.
        Curses can be cast on any crewmember, not just those who you have fingerprints to.
        Having an item present in the ritual that contains fingerprints OR blood dna of a crewmember who you are cursing will boost the curse, causing it to last longer (and be stronger? Still undecided, but there's support for it)
        Curses have a max range (64 by default) and don't work on people on a different z-level (Do not BTFO miners so easily)
        Corrosion curse's numbers have been tweaked due to this, and it can no longer cause vital organ failure

    Living Heart has been buffed
        Cooldown cut in half, and it provides a bit more thorough instructions
        Closes 

    Living heart targets who are located in non-turf locs and are off z-level will show as on the same z #67256

Leeching Walk has been buffed

    Rust will also restore lost blood.

Technically buffs Entropic Plume by fixing some bugs

    "Cloudstruck" has always meant to blind, but they used the wrong method, so I fixed that.
    Also it was meant to inject multiple units of poison, but used "min" instead of "max" so it always did the lowest.
    I also fixed the stink cloud lasting forever on people.
    Amok also makes people holding guns to shoot people further away.

Closes

    Admin healing removes heretic living heart #69167 while I'm here

Why It's Good For The Game

    Heretic curses have pretty much always been bad, getting fingerprints is damn near impossible considering everyone uses gloves. Not only that but their requirements were very high. This should hopefully bring curses to the limelight, as they can be applied to any potential targets. It also rewards heretics who go out of their way to collect fingerprints and blood samples with even stronger curses.

    The Living Heart was often hard to pinpoint people exactly, partially cause of an oversight. I improved the text to be clearer about potential locations of your targets.

    Leeching Walk's healing was nice, but blood wounds were still a major threat. Some blood restoration should help.

    Entropic Plume I think has never worked correctly, so that was a bummer. Fixes that.

Changelog

cl Melbert
balance: Heretic: Curses have been reworked. You can now curse any member of the crew, granted they're not too far away. If you additionally provide an item in the ritual containing a sample of the target's blood or fingerprints, the curse's duration will be increased and have its range uncapped.
balance: Heretic: The Curse of Corrosion has been nerfed slightly due to this rework, and can no longer cause vital organs to fail.
balance: Heretic: The Living Heart should now provide better directions, and had its cooldown halved to 4 seconds.
balance: Heretic: Leeching Walk (rust healing) now restores lost blood.
balance: Heretic: If you apply Amok (Entropic Plume) to someone holding a gun, they'll try to shoot it at people nearby.
fix: Entropic Plume's effect now blinds, as it should.
fix: Entropic Plume no longer sometimes applies the stink effect forever.
fix: Entropic Plume no longer always applies the lowest amount of poison, and properly scales on distance.
fix: Fixed an exploit which allowed people to figure out if a Heretic's heart was a previously a Living Heart after being removed.
fix: If a heretic is fully healed by something (such as ahealed), they'll not lose their living heart
/cl

---
## [JohnFulpWillard/tgstation](https://github.com/JohnFulpWillard/tgstation)@[de04b3be80...](https://github.com/JohnFulpWillard/tgstation/commit/de04b3be8082e37e4ff22b74b8f3feb6f38d03eb)
#### Friday 2022-09-02 05:38:39 by MrMelbert

Kills `/obj/shapeshift_holder`, replaces it with `/datum/status_effect/shapechange_mob`, also does a lot of Wabbajack refactoring (#69091)


About The Pull Request

    Deletes /obj/shapeshift_holder, replaces it with /datum/status_effect/shapechange_mob
    Refactors Heretic worm form into a shapeshift spell
    Refactors Wabbajack, and associated code

Fixes #69117
Fixes #65653
Fixes #59127
Fixes #52786
Why It's Good For The Game

/obj/shapeshift_holder was one of the worst remaining abuses of /obj direct subtypes, so I replaced it with a cool fancy datum.

This also decouples the shapeshifting behavior entirely from the shapeshifting spell. So we have support for shapeshifted mobs not sourced from a spell. Which is neat, we could technically swap Wabbajack to use this in the future.
Changelog

cl Melbert
fix: Wabbajacking a shapeshifted mob no longer runtimes horribly. When a shapeshifted mob is wabbajacked, they'll now be removed from their shapeshift and stunned.
fix: Transforming via a shapeshift should no longer rob you of your hearing / runechat awareness.
fix: Shapeshifting plays nicer with holoparasites.
fix: Being polymorphed from a xeno to a non-xeno correctly makes you a non-xeno
refactor: Refactored shapeshifting, the shapeshift holder is now a status effect instead of an object.
refactor: Heretic worm form is a shapeshift spell now, this might have some minor behavioral changes but should overall be the same.
refactor: Refactored Wabbajack (+ cursed pool). Overall a bit more clean / consistent behavior.
/cl

---
## [second2050/rkicons](https://github.com/second2050/rkicons)@[a16c67dd69...](https://github.com/second2050/rkicons/commit/a16c67dd69a1510d900fed212c43353a976dfa09)
#### Friday 2022-09-02 06:18:34 by DarkPlayer

rkicons: add burger king icon

Number 15: Burger king foot lettuce. The last thing you'd want in your Burger King burger is someone's foot fungus. But as it turns out, that might be what you get. A 4channer uploaded a photo anonymously to the site showcasing his feet in a plastic bin of lettuce. With the statement: "This is the lettuce you eat at Burger King." Admittedly, he had shoes on.

But that's even worse.

The post went live at 11:38 PM on July 16, and a mere 20 minutes later, the Burger King in question was alerted to the rogue employee. At least, I hope he's rogue. How did it happen? Well, the BK employee hadn't removed the Exif data from the uploaded photo, which suggested the culprit was somewhere in Mayfield Heights, Ohio. This was at 11:47. Three minutes later at 11:50, the Burger King branch address was posted with wishes of happy unemployment. 5 minutes later, the news station was contacted by another 4channer. And three minutes later, at 11:58, a link was posted: BK's "Tell us about us" online forum. The foot photo, otherwise known as exhibit A, was attached. Cleveland Scene Magazine contacted the BK in question the next day. When questioned, the breakfast shift manager said "Oh, I know who that is. He's getting fired." Mystery solved, by 4chan. Now we can all go back to eating our fast food in peace.

---
## [GesuBackups/tgstation](https://github.com/GesuBackups/tgstation)@[9d772c4f13...](https://github.com/GesuBackups/tgstation/commit/9d772c4f13da35569d61d223c8a693dc157666b2)
#### Friday 2022-09-02 07:42:20 by Jacquerel

Dimensional Anomaly (#69512)

About The Pull Request

Everyone has been asking: "When will there be an anomaly like the bioscrambler, but for the space station? Please, we need more things which replace objects with different objects from the same typepath."
Well I made it and it looked like ass because non-tiling floor and walls look terrible, so then I made this instead.
Dimensional.mp4

The "dimensional anomaly" shifts matter into a parallel dimension where objects are made out of something else.
Like the Bioscrambler anomaly, it does not expire on its own and only leaves when someone signals it or uses an anomaly remover.
When it spawns it picks a "theme" and converts terrain around it until it covers a 7x7 square, then it teleports somewhere else and picks a new theme.

A lot of these themes are relatively benign like "meat", "fancy carpet", or "gold". Some of them are kind of annoying like "icebox" because it creates floor which slows you down, or "clown" because bananium is intentionally annoying. Some of them are actively dangerous, mostly "uranium" and "plasma".
The main problem this will usually cause for crewmembers is decreasing area security. When it replaces doors it replaces them with ones which don't have any access control, and it will also replace RWalls with normal and much more vulnerable walls which will make breaking and entering significantly easier until someone has taken the time to fix the damage. But also sometimes it will irradiate them, you never know.

The fact that sometimes the changes are benign (or provide uncommon materials) and might be happening in places you don't care about access to might encourage people to push their luck and leave it alone until it starts turning the captain's office into a bamboo room or repainting medbay a fetching shade of flammable purple, which I would consider a success.
Armour.mp4

If you successfully harvest the anomaly core you can place it into the reactive armour to get Reactive Barricade Armour, which shifts your dimension when you take damage and attempts to place some randomised (not terribly durable) objects between you and hopefully your attacker (it really just picks up to four random unoccupied tiles next to you). If you're EMPed then the changes it make to the environment will often be as unpleasant for you as they are for a pursuer, and significantly more likely to harm both of you rather than just provide obstacles.

Other changes:
I split anomalies out into their own dmi file, seems to be all the rage lately.
I moved the anomaly placing code into a datum instead of the event because I wanted to reuse it but if you have a better idea about where I could have put it let me know.
This also fixes a bug where the material spreader component wasn't working when I applied plasma materials to something, the extra whitespace was parsing as another argument for some reason and meant it would runtime.
Supermatter delamination was still pointing to Delimber anomalies instead of Bioscrambler.

---
## [binji/porklike.gb](https://github.com/binji/porklike.gb)@[ef32a067bb...](https://github.com/binji/porklike.gb/commit/ef32a067bbdce67d4977708a263d5d41a137a63a)
#### Friday 2022-09-02 08:21:29 by Ben Smith

Optimize sight and is_valid

The previous `sight()` algorithm was implemented as a BFS, starting from
the player position and shooting rays out according to the data in
`sightsig`. This is simpler in some ways because we can take a given
position, move it one step away (in one of 8 directions), and add it to
the queue to process later. But it's also more expensive than necessary;
each of the 8 directions must be tested even though most of them are
never used.

Instead, if we follow a given ray as long as it doesn't hit a wall, then
the next, etc. we can do a lot better. Two arrays are used for this:
`sightdiff` and `sightskip`. `sightdiff` gives a list of the relative
offsets of a ray. They're all packed together, however. So when a ray
hits a wall, `sightskip` tells how many of the next elements of
`sightdiff` to skip over (these would have been the continuation of the
previous ray).

For this to work, we need to be able to efficiently determine whether
`pos + diff` is valid; i.e. in bounds. I wrote a function to do this
before, `is_valid`, but it was completely broken. I've since rewritten
it and it seems to work now.

It ends up using a somewhat clever technique, but I'm not sure whether
it's actually faster than the naive one. Basically we want to know
whether `pos + diff` has overflowed in either the X or Y direction.
Since pos is stored as `0xYX`, we can attempt to detect overflow in both
directions at the same time. We use a formula from Hacker's Delight:

```
sum = a + b
overflow = (sum ^ a) & (sum ^ b) & 8
```

Where the overflow ends up in the sign bit (bit 3 in our case). However
this formula assumes that `a` and `b` are both signed. In our case `pos`
has range [0, 15] and `diff` has range [-8, 7]. To make the math work
out in this case we need to modify it to:

```
pos' = pos ^ 8
sum = pos' + diff
overflow = (sum ^ pos') & (sum ^ diff) & 8
```

To calculate overflow for both X and Y in parallel, we can do the
following:

```
pos' = pos ^ 0x88
sum = pos' + diff
overflow = (sum ^ pos') & (sum ^ diff) & 0x88
```

However this doesn't take into account the fact that `pos' + diff` may
overflow from X into Y. Fortunately we can detect this in hardware as
the half-carry flag! Unfortunately, it's a huge pain to do so.

The half-carry flag is only read during the DAA instruction. If the
half-carry flag is set, then '6' will be added to the `A` register. But
`6` will _also_ be added if the sum in the low nibble is greater than
`9`! We don't want that. But it turns out that this doesn't happen if
the negative flag (`N`) is set.

So we want to make sure the `N` flag is set before we execute the `DAA`
instruction. Unfortunately, many instructions set this flag, so the only
way we can be sure that it's set is by subtracting instead of adding. So
we can change our formula to:

```
pos' = pos ^ 0x88
sum = pos' - (-diff)
overflow = (sum ^ pos') & (sum ^ diff) & 0x88
```

To calculate `-diff` for X and Y in parallel, we use start with the
basic formula:

```
-a = ~a + 1
```

So for both nibbles it would be:

```
-diff = ~diff + 0x11
```

Unfortunately, the sum in the low nibble can overflow. We can work
around this by adding `0x10` then swapping the nibbles, then adding
`0x10` again and swapping the nibbles again.

Now if the `N` and `H` flags are set, then `DAA` will add `0xA` to the
`A` register. So we set it to `0` carefully (making sure not to touch
any flags), and then we can left-shit `A` and mask with `0x10` to
extract the half-carry. If there was a half-carry then we subtracted too
much, so we add back in `0x10`. Now we can use this corrected sum for
the rest of the calculation. So the final formula:

```
pos' = pos ^ 0x88
sum = pos' - (-diff)
if half-carry:
  sum += 0x10
overflow = (sum ^ pos') & (sum ^ diff) & 0x88
```

---
## [Pepsilawn/fulpstation](https://github.com/Pepsilawn/fulpstation)@[c449fbb56c...](https://github.com/Pepsilawn/fulpstation/commit/c449fbb56c7cb57fc9d8c0db32be0b66e6d7293b)
#### Friday 2022-09-02 08:36:55 by SgtHunk

Fixes Solitaire runtimes + missing APCs (#488)

* solitaire fixes

* fuck you bar decals

---
## [forgefed/forgefed](https://github.com/forgefed/forgefed)@[c1b7974eff...](https://github.com/forgefed/forgefed/commit/c1b7974effab8437afc445df010825f0349a2e04)
#### Friday 2022-09-02 09:19:25 by fr33domlover

Behavior spec: Remove the "Create flow" (#155)

So far there have been 2 ways to ask to create an object on another
server:

- The Offer flow, which means the receiving side will be hosting the
  object. This means e.g. repos would be hosting their tickets, on the
  same server. This is the easy and obvious option.
- The Create flow, which means the author hosts the object, and the
  receiving side will just remember its ID, but the receiving side is
  also the one responsible for specifying access control.

The Create flow has existed because of the deeper distribution is
allows, where objects and their child objects can live on different
servers. It also allows users to host their own tickets, much like they
host their own comments and messages. But it's a challenge because
actors can't entirely reliably enforce access rules and integrity rules
on child objects hosted elsewhere. Having 2 flows also adds complexity
to implementations.

After a lot of thinking, I decided I wish to remove the Create flow. It's a
huge simplification to the specification and to implementations. The
mitigation for losing the advantages of the Create flow is:

- The kind of decentralization on the Fediverse isn't a fully
  distributed situation, and in particular it doesn't help with remotely
  enforcing access control. If/when the fediverse goes fully P2P, it
  will surely have such mechanisms. I believe actor-level decentralization is
  *definitely* enough to solve the problems of centralization that we have with repo hosting websites. It's also
  probably the best that's reasonably available to us without resorting
  to p2p and cryptography based solutions.
- If people want to host their own tickets, then can create a personal
  ticket tracker and use it as their to-do list or as a place to list
  bugs that got rejected by the relevant projects, or whatever people
  want to use personal tickets for
- Actor-level decentralization is simple, clear, easy and elegant, and I don't
  believe we really need anything more complicated

I implemented the Create flow on Vervis. It added huge complexity. I'm now busy removing it, suffering the complexity of removing all that stuff entangled in my code... :P and seeing how much simpler things were before I implemented it "^\_^

Co-authored-by: fr33domlover <fr33domlover@riseup.net>
Reviewed-on: https://codeberg.org/ForgeFed/ForgeFed/pulls/155
Reviewed-by: Anthony Wang <ta180m@noreply.codeberg.org>
Co-authored-by: fr33domlover <fr33domlover@noreply.codeberg.org>
Co-committed-by: fr33domlover <fr33domlover@noreply.codeberg.org>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[f0ceecff46...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/f0ceecff46f9b600dfe8e60199f354f61d63a0a4)
#### Friday 2022-09-02 10:35:24 by SkyratBot

[MIRROR] Refactors SM gas behavior to be datum based instead of list based + powerloss co2 buff [MDB IGNORE] (#16000)

* Refactors SM gas behavior to be datum based instead of list based + powerloss co2 buff (#69158)

About The Pull Request

Title!
The CO2 thing is there because it makes my job much easier. Can probably find a way to make it move slowly if a maint insist on it. Prefer not to though.

Drafting because I want to make a second PR that have more sweeping changes (clean vars up, make a simpler formula for damage and heat production, delete underused behaviors, etc). Would honestly prefer if both this and that gets merged at the same time but I'm separating it out since it might be rejected. Or maybe ill combine it here we'll see.
Ignore that, looks like i can keep this one absolutely atomic.
Why It's Good For The Game

Had a lot of trouble when trying to document the SM gas interactions into the wiki, the interactions are all scattered and tracking down everything a gas does is extremely annoying. Hopefully this fixes that.
Changelog

cl
balance: CO2 powerloss inhibition now works immediately based on gas composition instead of slowly ramping up.
refactor: refactored how the SM fetches it's gas info and data. No changes expected except for the co2 thing.
/cl

* Refactors SM gas behavior to be datum based instead of list based + powerloss co2 buff

Co-authored-by: vincentiusvin <54709710+vincentiusvin@users.noreply.github.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[497e784e33...](https://github.com/mrakgr/The-Spiral-Language/commit/497e784e33a6c6c2cda8472c142cdab36938a7af)
#### Friday 2022-09-02 10:39:27 by Marko Grdinić

"10:05am. I slept well tonight. Let me chill a bit and then I will get started on proofing the chapter. Before that I think I'll make a little post in the PL monthly thread just to plug Heaven's Key.

https://boards.4channel.org/lit/thread/20929000/master-your-will

crying nitz wojak.jpg

///

>Master your will!
>NOOOOOO! NOT LIKE THAT! THAT'S SLAVE MORALITY!

///

explaining.jpg

///

>only the weak band together, cuz they are weak
>ok, the strong do it too, but only occasionally to conquer someone, but usually they are too individualistic like me, do you even read greek historians?
>ok, healthy barbarians do it too, but we can't return to that unironically

>only the weak let dissatisfaction simmer inside them, i call it le ressentiment
>ok, the strong get dissatisfied too, but they should immediately lash out or they are weak by definition, of course we cant return to that state of things unironically

///

I've really been missing out on Nietzsche troll threads haven't I? I should actually read his damn works at some point.

10:40am. Let me get started.

https://osera.cs.grinnell.edu/publications/osera-phd-thesis.pdf
Program Synthesis With Types

Somebody posted this in the PL sub. I won't read it right now, I'll just save it for later.

> Program synthesis, the automatic generation of programs from specification, promises to fundamentally change the way that we build software. By using synthesis tools, we can greatly speed up the time it takes to build complex software artifacts as well as construct programs that are automatically correct by virtue of the synthesis process. Studied since the 70s, researchers have applied techniques from many different sub-fields of computer science to solve the program synthesis problem in a variety of domains and contexts. However, one domain that has been less explored than others is the domain of typed, functional programs. This is unfortunate because programs in richly-typed languages like OCaml and Haskell are known for “writing themselves” once the programmer gets the types correct. In light of this observation, can we use type theory to build more expressive and efficient type-directed synthesis systems for this domain of programs? This dissertation answers this question in the affirmative by building novel type-theoretic foundations for program synthesis. By using type theory as the basis of study for program synthesis, we are able to build core synthesis calculi for typed, functional programs, analyze the calculi’s meta-theoretic properties, and extend these calculi to handle increasingly richer types and language features. In addition to these foundations, we also present an implementation of these synthesis systems, Myth, that demonstrates the effectiveness of program synthesis with types on real-world code.

Type theory for program synthesis? This really comes together with my interest for using genetic programming to evolve better learning algorithms. Maybe I'll be working on a dependently typed language years down the road, but that's only if the world throws me a bone and does not drive me straight to ruin.

10:45am. Let me do the PL review.

///

Two months ago I did a ref counted C backend for [Spiral](https://github.com/mrakgr/The-Spiral-Language) so I might as well plug it now. Since then I've gotten tired of 3d art, and decided to just start writing [Heaven's Key](https://www.royalroad.com/fiction/57747/simulacrum-heavens-key).

I don't think I'll be programming much any time soon. I am still obsessed about AI chips, so I've tried fishing in TensTorrent's discord, but it is extremely inactive so I don't think I'll get a reply there. Maybe from the start I haven't been a part of the machine learning wave at all. I've been reflecting on my mistakes for the past year, and I think I understand where I went wrong. Instead of drawing out the insights myself, I should have done it like nature did and constructed a genetic programming system that can infer its own learning algorithms. It is not like I haven't thought about that even when I started, but I reasoned that it would be too computationally expensive to take such an approach. Which wasn't wrong. It was an easy conclusion to make.

I was skeptical about the ML community from the start, but it would still be a stretch to assume that their entire approach is wrong. But it is wrong. The ML researchers right now are the programmers circa 1980s, programming in Assembly and C, and wondering why things are so hard.

Thanks to my PL work on Spiral, I have a good basis for making mutating interpreters like the ones genetic programming requires. I also know some type theory, so that might be an avenue to adding type directed synthesis to a genetic programming system. This kind of path might be a good idea, since the modules in the [brain are replicated](https://youtu.be/m3U1_Zv4_Ik?t=137). Evolving long sequential programs like the ones humans craft by hand would be quite hard for a GP system, but in biological brains there is only so much the individual modules could do, especially considering how limited their functionality can be expected to be at the type level.

The kind of work I'd like to do is to get an AI chip that has a lot of individual cores communicating via message passing, and make a system of competitive modules and see if they converge to a uniform protocol and features. Then I'd use that library to make a system made out of uniform modules.

But at the same time, I am lazy so I am not willing to work, so I can work even more on my own hobbies. Forget programming or the stock market, if I had just wrote science fiction for the past 15 years, I'd have made way more money than I have now, which is essentially nothing. So I do not want to let myself get scammed again. I've looked into it, and I could get access to Graphcore's chips on the cloud, but I am not going for free to do the work of turning the half baked [Poplar](https://docs.graphcore.ai/projects/poplar-user-guide/en/latest/poplar_programs.html) library into a proper language as well as make the messaging library for it. Even with these chips I probably wouldn't have even a 1/1,000th of the necessary computational power to make a significant algorithmic breakthrough, so it would just be throwing months and years of my life down the drain. Who knows which of these AI chips is going to be a winner anyway. Maybe it will be something from China that I do not know about?

Anyway, writing suits me well, so I'll just do that. I do believe in the tech Singularity, but the feeling is - just because I am bullish on the stock market does not mean I want to be 300% long anymore. If the world wants me to get back in, it is going to have to throw me a bone or two.

///

...Let me check the mail, before I write that 3rd sentence. Nothing from TensTorrent. Yeah, there is no need to expect anything from them. It does not feel like I am a part of the machine learning wave at all in this world.

11:25am. Done with the PL review. That should net me a few readers, maybe. I am not going to be posting there anymore.

11:35am. Let me get to proofing the chapter. Let me just finish the thread.

11:40am. Stop reading /a/ threads and focus on proofing. I need to publish chapter 7a today.

12:30pm. Let me have a break here. I've already started it anyway.

https://www.youtube.com/watch?v=EqyJHxXXoyQ
Pathfinder Class COMPLEXITY Tier List

So I've respeced Nok Nok into Slayer. At first I gave him both archery and two handed weapon fighting feats, but then I realized after a couple of areas that I was never using the knives. It always made more sense to just shot the enemy. So I started using him as a pure archer. Afterwards since I didn't have Amiri to skin the beasts I started putting points into Lore (Nature) and even gave him Skill Focus in that. BY accident then I discovered that there is a feat to give him an animal companion and one of the prereqs is that Skill Focus. This is big. I've looked into how wizards could get animal companions online for example and could not find it.

Also it seems Slayer's capstone ability is a full round attack as a standard action, so what he should have at lvl 1 to make meele competitive with archery is only there after the game is nearly done.

12:40pm. Let me have breakfast."

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[a1f86f56a2...](https://github.com/odoo-dev/odoo/commit/a1f86f56a2852ea4745f66eed33a94f596b150d4)
#### Friday 2022-09-02 10:42:55 by Xavier Morel

[IMP] *: owlify password meter and convert change password to real wizard

The changes in `auth_password_policy` are largely the owlification of
the password meter widget:

- modernize the password policy module and convert it to an
  odoo-module (note: now exports a pseudo-abstract class which is
  really a policy, for the sake of somewhat sensibly typing
  `recommendations`)
- replace the implementation of the Meter and PasswordField widgets by
  owl versions

The changes to web and base stem from taking a look at converting the
ChangePassword wizard, and finding that it would be a pain in the ass
but also... unnecessary? It seems to have been done as a wizard
completely in javascript despite being backend-only for legacy
reasons: apparently one of the very old web clients (v5 or v6
probably) implemented it as a "native action" which was directly part
of the client's UI, and so it had to be implemented entirely in the
client.

Over time it was moved back into the regular UI (and moved around
quite a bit), hooked as a client action to maintain access to the
existing UI / dialog.

But since it's been an action opened via a button for years it can
just... be a normal wizard, with password fields, which
auth_password_policy can then set the widget of.

So did that:

- removed the old unnecessary JS, and its dedicated endpoint (which is
  *not* used by portal, portal has its own endpoint)
- used check_identity for the "old password check"
- split out `change_password` with an internal bit so we can have a
  safer (and logged) "set user password" without needing to provide
  the old password, which is now used for the bulk password change
  wizard as well
- added a small wizard which just takes a new password (and
  confirmation), for safety a given change password wizard is only
  accessible to their creator (also the wizard is restricted to
  employees though technically it would probably be fine for portal
  users as well)

Rather than extensive messy rewrite / monkeypatching (the original
wizard was 57 LOC, though also 22 LOC of template, the auth_policy
hooking / patching was 33, plus 8 lines of CSS),
`auth_password_policy` just sets the widget of the `new_password`
field in the new wizard, much as it did the bulk wizard.

Also improve the "hide meter if field is empty" feature by leveraging
`:placeholder-shown`. This requires setting a placeholder, and while
empty works fine in firefox, it doesn't work in chrome. So the
placeholder needs to be a single space. Still, seems better than
updating a fake attribute or manipulating a class for the sake of
trivial styling.

Notes on unlink + transient vacuum

Although the wizard object is only created when actually calling
`change_password`, and is deleted on success, it is possible for the
user to get an error and fail to continue (it should be unlikely
without overrides since the passwords are checked while creating /
saving but...).

While in that case the `new_password` in the database is not the
user's own, it could be their *future* password, or give evidence as
to their password-creation scheme, or some other signal useful to
attack that front of the user's life and behavior. As such, quickly
removing leftovers from the database (by setting a very low transient
lifetime) seems like a good idea.

This is compounded by the `check_identity` having a grace period of 10
minutes. 0.1 is 6 minutes, but because the cron runs every 10 the user
effectively has 6~10 minutes between the moment they create an
incorrect / incomplete version of the wizard and the moment where it
is destroyed if they just leave it.

---
## [SamuelFontes/simplest-discord-shop](https://github.com/SamuelFontes/simplest-discord-shop)@[e63dfb1fc2...](https://github.com/SamuelFontes/simplest-discord-shop/commit/e63dfb1fc2b722dbfd3ac6910f9b8b40d2a8f678)
#### Friday 2022-09-02 11:44:58 by Samuguel

THIS IS WHY WE CAN´T HAVE NICE THINGS. THE OLD VERSION OF THIS API WAS
SIMPLE AND EASY TO USE IT, IT WAS PERFECT TO DO WHAT I WANTED WHICH WAS
SPAGUETE CODE. I DON´T WANT TO USE THIS COMPLICATED THING JUST TO BE
ABLE TO INTERACT WITH THE API, IT WAS SO SIMPLE AND SO PERFECT, THIS
IS WHY PROGRAMMING IS DOOMED AND WHY I HATE THIS EARTH DEAR GOD I JUST
WANTED TO DO A SIMPLE DISCORD BOT BUT NO THIS HAS TO HAVE A PRE-CONFIGURING
FASE TO MESS WITH MY MENTAL HEALTH IM'M SO MAD THAT I WANT TO EAT AN INTIRE PIZZA...
Discord.js version updated.

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[773f04110e...](https://github.com/TaleStation/TaleStation/commit/773f04110e5ee89b80659d7053c6b8572d5aa2ce)
#### Friday 2022-09-02 11:48:50 by TaleStationBot

[MIRROR] [MDB IGNORE] Spider Rebalance PR: Burn Baby Burn Edition (#2288)

* Spider Rebalance PR: Burn Baby Burn Edition (#68971)



This is a remake of #66106, with more thought put into the underlying balance. The main goal of this PR is to make fighting spiders more accessible and interesting for the majority of the crew while nerfing the extremely strong and boring option of simply using freezing temps to kill spiders. Also fixes #67765. The changes are as follows:

NEW SPIDER COUNTERS

    Fly swatters now deal 25 damage to spiders on hit, increased from 1
    Pesticide now deals massive stamina damage to spiders and a little bit of physical damage as well (the damage portion not added by this PR)
    Spiders can now be caught on fire through any traditional mean of catching something on fire. Spiders will automatically put themselves out after a time. This was done instead of an active action because AI spiders are also subject to this change as well, and I don't feel like bloating the simple mob AI with putting themselves out

SPIDER CHANGES

NERFS

    Toxin injection has been removed from all spiders except for the hunter, flesh spiders and the viper
    Hunter toxin (used by hunters and flesh spiders) now only brings the afflicted down to 40 health, and will stop taking effect once the afflicted reaches that threshold. Should the afflicted still have the toxin in their system and get healed, the toxin will begin dealing damage again until the afflicted is at 40 health or below again
    Viper toxin now only brings the afflicted down to 10 health, but also has the hallucination effects of Mindbreaker toxin. This hallucination effect is applied regardless of target health. It also no longer generates other harmful chemicals into the afflicted's system, but is much more potent at base
    Flesh spiders cannot regenerate while on fire

BUFFS

    Time it takes for spiders to normalize their temperature cut by half. While they will react faster when in cold or hot environments, when they leave said environments it will take less time to return to normal temperature
    Unsuitable temperature damage reduced to 4 from 8
    You can no longer push spiders by running into them
    Webbing heat damage threshold increased from 300 to 350 (same temp where spiders also take damage)
    Broodmother egg laying time reduced to 12 seconds from 15
    Broodmother web laying time multiplier reduced to 0.5 from 1
    Broodmother health increased to 60 from 40
    Broodmother damage increased to 10 - 15 from 5 -10

BEHIND THE SCENES CHANGES

    You can now make any simple mob able to be caught on fire by setting flammable to true
    How fast a simplemob stops burning is controlled by fire_stack_removal_speed
    Can now now control how fast simplemobs regulate their temperature using temperature_normalization_speed. Before this PR, this value was hard-coded at 10, I have set the default to 5 as 10 was too long in almost any case. This will notably affect slimes, who could easily die to being cold long after being removed from the cold area. I see this as purely beneficial
    Toxins now have a health_required value. The afflicted has to be above this health value in order to take damage from the toxin. Only used in the spider toxins currently
    When I was setting up simplemobs to be flammable, I noticed basic mobs can be glitchily set on fire, so I fixed it to where they can't be set on fire.

Why It's Good For The Game

    Spacing something is very easy, but not very fun or interesting compared to starting and controlling a fire. Swapping spiders' temperature weakness from spacing to fire is beneficial to the fun of fighting them and playing as them, allowing more creativity and resourcefulness on both sides. Ideally, this should allow for atmosians and chemists to use their skills in a fun way.
    Currently, ignoring spacing them, the only people who can reasonably take on spiders is security, since they have lasers which do burn and stuns to slow the spiders down. However, this small subset of players cannot normally destroy a spider infestation without spacing them, so letting fly swatters and pesticide be used to combat spiders allows other crewmembers to fight back, letting them actually enjoy facing spiders as a threat and allowing the crew to defend themselves.
    Being killed by spider toxin after fighting off a horde isn't fun. The changes still make it a threat you have to be aware of, but not one which detracts as much from the combat loop. This also forces spiders to secure the kill themselves, which is more fun than having the toxin do it for you.
    Broodmothers in their current state are incredibly weak by themselves, which is intentional by design. However, the new changes hope to make playing as a broodmother easier and hopefully allow more broodmothers to get the spider infestation started properly. After all, Dynamic is their common source now, and they should be consistently worth the threat cost to spawn them.
    Previously, spider structures would seemingly vanish for no reason if the room was heated to be greater than 300 but less than 350, as the spiders would not be able to tell that it was too hot. Now, if the structures are taking damage, spiders will also be taking damage, so understanding what's going on should be easier now.
    Pushing spiders into a corner by running into them was not a fun tactic to deal with as a spider and didn't make much sense seeing how big the spiders are.

Changelog

cl
add: Spiders can now be caught on fire
add: Spiders take significant damage from fly swatters and stamina damage from pesticide
balance: Spiders have been re-balanced. Their toxins can no longer kill but they are not as susceptible to freezing
balance: General stats of spider broodmothers have been buffed with more health, damage, and faster web and egg placement
balance: Flesh spiders cannot regenerate whilst on fire
balance: Simplemobs change their internal temperature twice as fast
fix: Basic mobs no longer glitchily catch on fire.
/cl

* Spider Rebalance PR: Burn Baby Burn Edition

Co-authored-by: IndieanaJones <47086570+IndieanaJones@users.noreply.github.com>

---
## [gcfntnu/gcf-bfq](https://github.com/gcfntnu/gcf-bfq)@[d3bf081b99...](https://github.com/gcfntnu/gcf-bfq/commit/d3bf081b99a403482ac8ce5051202c2a9ba380da)
#### Friday 2022-09-02 12:49:50 by Geir A

ugly ass hacks to fix mangled bcl-convert legacy Stats.json

---
## [justinpryzby/postgres](https://github.com/justinpryzby/postgres)@[7fed801135...](https://github.com/justinpryzby/postgres/commit/7fed801135bae14d63b11ee4a10f6083767046d8)
#### Friday 2022-09-02 12:55:57 by Tom Lane

Clean up inconsistent use of fflush().

More than twenty years ago (79fcde48b), we hacked the postmaster
to avoid a core-dump on systems that didn't support fflush(NULL).
We've mostly, though not completely, hewed to that rule ever since.
But such systems are surely gone in the wild, so in the spirit of
cleaning out no-longer-needed portability hacks let's get rid of
multiple per-file fflush() calls in favor of using fflush(NULL).

Also, we were fairly inconsistent about whether to fflush() before
popen() and system() calls.  While we've received no bug reports
about that, it seems likely that at least some of these call sites
are at risk of odd behavior, such as error messages appearing in
an unexpected order.  Rather than expend a lot of brain cells
figuring out which places are at hazard, let's just establish a
uniform coding rule that we should fflush(NULL) before these calls.
A no-op fflush() is surely of trivial cost compared to launching
a sub-process via a shell; while if it's not a no-op then we likely
need it.

Discussion: https://postgr.es/m/2923412.1661722825@sss.pgh.pa.us

---
## [Dark-Matter7232/CosmicFresh-Hanoip](https://github.com/Dark-Matter7232/CosmicFresh-Hanoip)@[b610b1f9df...](https://github.com/Dark-Matter7232/CosmicFresh-Hanoip/commit/b610b1f9df2629957122d493c171bde63b1bbe8f)
#### Friday 2022-09-02 12:59:05 by Peter Zijlstra

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
## [TheGiga/MLP](https://github.com/TheGiga/MLP)@[d8cfd7549a...](https://github.com/TheGiga/MLP/commit/d8cfd7549ac19ce4dcc4877bc74ebc946a96e00c)
#### Friday 2022-09-02 13:00:22 by gigabit-

+remade main reminder loop logic
+fixed some stupid bugs
+i hate myself

---
## [dam5h/helix](https://github.com/dam5h/helix)@[973c51c3e9...](https://github.com/dam5h/helix/commit/973c51c3e970aa975f2bd1869d50ce2ae6c6de34)
#### Friday 2022-09-02 13:12:48 by Michael Davis

Remove C-n and C-p from the insert mode keymap (#3340)

These are read-line-like bindings which we'd like to minimize in
insert mode in general.

In particular these two are troublesome if you have a low
`editor.idle-timeout` config and are using LSP completions: the
behavior of C-n/C-p switches from moving down/up lines to moving
down/up the completion menu, so if you hit C-n too quickly
expecting to be in the completion menu, you'll end up moving down
a line instead. Using C-p moves you back up the line but doesn't
re-trigger the completion menu. This kind of timing related change
to behavior isn't realistically that big of a deal but it can be
annoying.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[0faded2988...](https://github.com/mrakgr/The-Spiral-Language/commit/0faded298838a2f6fbc8b9c6c1a3c281165f4989)
#### Friday 2022-09-02 15:13:06 by Marko Grdinić

"1:40pm. Enough wasting time. Let me get back to proofing. Let's me just do it. After that I'll be able to move to chapter 8.

2pm. Been correcting errors as I go along.

> I tried evolving bots for various toy games and I was successful using this approach as well. This gave me some insight into how memory systems work. In living beings, even insects, they have a cycle of sleeping. I actually managed to evolve this and got agents that would accumulate short term memory during the episode and then distill it into long term memory in between the episodes. I've found that agents that adding short term memories during the episode leads to smooth policy improvements. Later distiling that improved policy into long term memory instead of using directly reinforcement learning gets around all the disadvantages of using such an old human-designed approach.

I meant to say that adding short term memories should alway improves the policy. I need to highlight that more.

2:40pm. I'm 60% done with proofing.

Let me continue going forward.

3:20pm.

> "So the base algorithm, it really exists? I thought it might not since I read that there are differences in information processing capabilities between mouse and human cells. Also elephants have bigger brains, but don't have higher intelligence than humans. I thought there might be levels of such algorithms, and that humans might be somewhere in the middle, leaving room for self improvement. Does that mean once you apply that algorithm to yourself and take up the core's capacity, that will be a limit to improvement of your intelligence?"

I might want to tackle this part again and make it more clear.

But nevermind that. Let me split the chapter into two first and I will publish it. I'll get back to proofing past two after that.

3:25pm. The number of views didn't go much. It is still at 179. I'll have to keep publishing and see if it goes up. I won't worry about this for now yet.

3:30pm. https://www.royalroad.com/fiction/57747/simulacrum-heavens-key/chapter/984918/chapter-7a-memories-of-streets

Finally, it is up. The previous latest chapter has only like 5 views, but I do not want to worry about that. I'll just do the one thing that I can which is write. If Heaven's Key is meant to take off, it will take off. If not I'll treat this as a break before I am forced to get a job.

You can live your life wage slaving, or you can live your life having fun.

3:35pm. Let me go forward. If I publish another 10 chapters, and am only getting like 3-5 readers each, then I can start getting worried. In that case, I might even abort Heaven's Key and just go back to the job search. But I want to live in hope and ignorance of the future for the time being.

Let me go back to proofing the other half of the chapter.

> Have you looked at Xmos chips? They're more general than specifically AI focused but they have more cores than most ARM SoC based processors that are used in most small board computers (I think the base one starts at 8 cores or something). I'm not sure about other multi-core chips, but I know there are a few chips out there designed specifically for "ML", one of which includes the Kendryte K210; I picked up something a few years ago from Seeed studio made by "Sipeed" that includes this processor. There are some others too but I can't remember the details.

Got this on Reddit, let me make a reply.

///

> Have you looked at Xmos chips?

No, I've never heard about them, or the other ones. Should I check them out? The company I am the most interested in the AI space is TensTorrent. I've watch some vids and read the interview by the CEO & CTO (Jim Keller). I've not tried its hardware as I do not have the money for it even if it were more widely available, but the story and the signaling they give out is good. Unlike all the other companies they have small cards you could plug into your home rig. Essentially it is a multicore chip with local memory for each CPU & GPU that communicate via message passing. What I want to do with Spiral is build on my 2018 work. Back then I had a F#/Cuda backend which was really good for writing generic GPU kernels for the ML library. I want something like that plus some kind of concurrency library in the vein of (CML style) Hopac or (Erlang style) Akka.

If I had that, then I could start work on making a system that could infer its own learning algorithms via genetic programming. I go into detail of chapter 7 of my sci-fi story of how that approach could work.

///

4:15pm. Let me get back to proofing.

I won't rewrite that part, it doesn't really matter. The readers will get the picture at some point as I'll constantly revisit the subject in different ways.

4:45pm. Done with proofing 7b. I won't post it today. I'll defer it a bit to build publishing momentum. Let me also proof the part two of author's note.

5pm. Ok, I am done. Now it is time to sturf /a/. I do not feel like starting chapter 8 just now.

5:10pm. Let me unwind. I'll close here. Tomorrow, I'll get started on chapter 8.

I posted 7a on RR so there is no need to repost in the journal, but here is an advance on 7b if anybody is interested. I am out.

$$$

(Helix Studio, Regent Suite, Bedroom)

It took 3 months, but while I was immersed in programming, I got a notification that somebody finally cleared the ninth level! I quickly set the training run so it ceases once all instances in the population have finished and take a look at the winner. Sure enough, one of my instances managed to do it.

I bring up its program and begin processing it. Programs derived through genetic programming are always bloated, so I pass the AST through a partial evaluator to get rid of the dead code and simplify it, then I print it out in readable form. There is a lot of new functionality in the behavioral system as could be expected. The memory system has seen some modifications, but the optimization goal of this exercise has been to reach the finish line so I am not surprised the memory system itself hasn't been affected much.

As I take a look, I realize that I have a message from the winner and take a look, seeing him complain about the need to sleep.

I’ll leave the sleep considerations for later.

What I have to do for the winners of the last level is subject them to memory testing. I am going to modify the simulation so it applies a questionnaire automatically later, but with the first one I want to have a personal talk.

(Helix Studio, Regent Suite, Living Room)

After all the entities in the population have finished, I decide to start implementing my plan. Deciding to administer the first interview myself, I move to the living room first. I mentally prepare myself for what is to come, it has been a long time since I talked with anybody. I normalize my mental state to relax.

None of the others in the population managed to finish all the way, but there were some messages left for me. Most of the messages from my forks inside the game tend to be curses, them wishing me death, or whining about how bored and depressed they are so I've stopped paying attention to those losers. The guys like him who just go as far as they can before expiring quite the angels. I've never tried talking to any of them yet directly, so I am not sure what I will find. Hopefully he won't try to jump me, if he does I'll terminate him with a mental command.

Feeling ready, I called up the instance. The winner of the game manifests on the sofa opposite of mine.

"Hello." I initiated the conversation.

"Huh?" He starts looking around. "Where is this?"

"The Regent Suite in Helix Studio." I answered him.

"Regent Studio? Helix Suite?" He starts looking around, not paying attention to me. "Wow, is this what level 10 is like? No, that can't be it..."

"..." I look at him in silence as he gets up and starts wandering around the room. With some mental commands, I confirm that he is in fact running at one billion. After half a minute of him wandering around, gawking at stuff I yell to get his attention.

"Hey!" I startle him.

"You are still here? Who are you?"

"Euclid." He ponders really hard at my reply.

"The same name as mine...I think?" He shrugs his shoulders.

"You think? Aren't you sure what your name is?" I asked him, astonished.

"Well, I think my name is Euclid, but I've forgotten everything else. I can't remember the world outside anymore. All I know is the street that I need to cross. It is amazing that I can even talk." He says that, but honestly, I think the way the words come out of his mouth is quite polished. There are no 'uhms', and 'ahms' people make to buy time to think. He is executing well formed sentences a lot better than me.

I think for a bit and realize that before the Street, he was alive for 14 years. Then he spent 700 years trying to beat the Street game. His life was a kid was a small percentage of his overall life, like 2%. For an adult of 40 years, 2% would be 9.5 months he spent as a baby. How many people remember what went on in that period later in their life? Looking at him, a part of me feels like I am looking at a fool, but the rational part of me is suppressing that.

Still, I am going to have to put some effort in dealing with memory and fixing it.

"What do you want to do next? Do you remember what our goal in life is?"

"To cross the street?"

"To attain absolute power!" He ponders about this. I am guessing this is more to show his emotions than the actual need to take time to think.

"I don't care about that. I just want to keep going forward." So that is what he is.

"Thank you." With a mental command I stop his process and abort his avatar from the environment. Not a bad guy. My impression of him isn't negative. I want to ask him the same question once I give him a proper memory system. At the end of that long road, what will he tell me then?

(Helix Studio, Regent Suite, Bedroom)

If you look at how evolution works, it is tossing the dice to be sure, but it is not completely random. It tests out variations in humans, but those variations don't have them growing 6 arms or 4 legs which you'd expect if it were completely random. It is in fact doing exploration in a principled manner. It developed a library of components and is composing them in different ways. This is pretty powerful, and is how programmers do it.

Being able to set up that library in my own genetic programming system is a powerful tool for me as well. Giving the system access to matrix multiplies and other batch operations instead of having it develop them from scratch is a big aid.

What I am going to do is kick it up a notch and give the system for evolving my forks more than just matrix operations, I am going to give it proper memory system components. The benefit from that in my own evolutionary process will be extreme. And when I have those components, I will be able to use them to optimize the genetic programming system itself and drastically lower the simulation counts. To that end, what I will do is revisit supervised learning. It is an area where the backpropagation algorithm is very dominant. Backprop has its strength - it is really good at compressing large amounts of data into network weights. But at the same time old style NN models have a lot of issues. The biggest one for me now is that I can't use them as databases and replay the lifetime of memories from scratch. Unless you have the original database saved they can't be used that way.

With more flexible models, what I'll be able to do is create a very generic memory distiller. What such a program would allow me to do is transfer memories from one system to a different one, similarly to how memories get transferred from the short term to the long term system in the brain itself.

The memory issue the winner of the last run had experienced is because the optimization process had trouble with modifying the original memory system without disturbing the existing data. It tried expanding the original system, but ended up with a mess of newly formed plastic and stale static connections. If I could give it a good way of coming up with new systems as well as a way to transfer the memories from the old one, it will lead to a remarkable explosion in the intelligence of my agents...er my forks I mean.

The way to get such memory system components is not too hard. I've gotten an exabyte dataset of every movie, cartoon and anime ever made, as well as recordings of virtual simulations. A billion gigabytes might seem big, but it is nothing. A single iteration for a backprop based model would take less than a microsecond of objective time on the brain core.

What I am going to do is make a setup to evolve novel kinds of models on such a dataset starting from the mental model of my own mind. In the previous test, I was experimenting with behavioral improvements, but what I will do here is get rid of such concerns and focus solely on memorization ability.

The system I have to design is complicated. I spend a few days in my bedroom, not writing a line of code, just thinking and rehearsing what I need to do in my head. Then I finally come to a decision and get started on the task. No matter how complicated something is, if you take it one step at a time, eventually you will reach the end of the road.

I said I would start with my own mind's model, but out of curiosity I instead started from scratch just to see what would happen.

The evolutionary process actually starts off by making backprop-like systems initially. Instead of using the regular gradient rules, it ends up normalizing them to improve the stability. It is not too surprising as backprop rules are the simplest way to make a learning system. At that point it gets bottlenecked for a while, but the models start getting more elaborate. Backprop really works well when you can just run it over and over the dataset for a large number of iterations until it converges. But if I only allow like 4 iterations over the whole dataset, then different types of models start to emerge. The evolutionary process pushes more work to be done locally in each individual module and the more I run it, the more the models start to resemble the one for my own mind.

I play like this for a month, just studying what the evolutionary process comes up with on its own, and then I add my own mental model, randomly initialized, to the population. Compared to the ones I am training on the dataset, its parameter count is orders of magnitude lower, but it has components the others don't so it should be interesting to see how they cross over. At worst, adding my own model to the mix will only slow down the optimization slightly as they get worked out, but there is the potential for this move to significantly improve performance and shorten the time it takes to evolve what I am seeking. I have no doubt though that even if I didn't do this, the brain core was powerful enough to evolve a system that exceeds anything nature has ever invented.

Two months later...

(Image TODO: A series of sketches of a heavily armored warrior fighting an orc. In the 1st frame, the human warrior swings his sword at the orc. In the 2nd, he blocks a blow from the orc's ax with his shield. In the 3rd one, he tackles the orc off his feet. In the 4th, he moves in an overhead chop with his blade at the prone orc. The 5th frame is just an image of the blade falling downwards.)

(Image TODO: Popcorn in hand, Euclid is watching an anime series based on those sketches projected on the cinema curtain.)

(Helix Studio, Regent Suite, Cinema)

Grabbing some popcorn from the bag, I toss them in my mouth as I watch the action on the curtain. In the projection in front of me, the lightly armored barbarian orc and the man in scale mail clash in the ruins of some abandoned temple. The moon is shining brightly in the dead of night, and there are some darkened clouds. Ever so often sparks would be produced from their weapons meeting, lighting up the scene in brief flashes. A swing of the ax, a slash of the sword...there were bouts of intense battle, and there periods where they separated, breathing heavily, sweat dripping down their faces. The orc screamed in rage, and then...

And then...

The movie in front of me freezes while I think about it.

At any rate, I got something good in the last 3 months. Right now I have a learning system that can easily compress the exabyte dataset down to ten terabytes with a negligible loss in accuracy. Once I have such a system, it is easy to feed it my loose sketches, having it reconstruct them as images. If I supply a couple of loose sketches that way, tag with the appropriate time stamp, I can do a movie reconstruction. The system can even produce music and sounds appropriate for the atmosphere.

Very cool.

I am into memory system work now. I meant to get back into the game after I got to this level. I still need to do the distiller, and that is what I am going to do next, but instead of getting back to the game, I think I am going to push this avenue of research as far as I can. I am making huge gains in both programming skill and understanding of intelligence, so I'll persevere.

My plan has changed. The games don't matter now, and I will put Heaven's Key on the backburner for as long as necessary. If I could find the endpoint of the evolutionary chain, distill my memory to such a system, and apply the behavioral modification that will enable me to think at billion fold rates, what is going to come out of that is an absolute beast. I could try doing it more gradually. Instead of the dumb me, the stories have people applying any improvements right away, but even if I did it for a decade here, that would just be a day in the real world. It is not like I am in a hurry. I can be patient, and make every step when I am sure of it. What I am doing now is fun. Imaging the amount of power I am going to get once I am able to control these systems directly is what keeps me going.

Right now the system is pretty good, compared to my biological one that needs to power off every 2/3rds of a day, it is more accurate with regards to the amount of data it is ingesting, but what I'd like to do is challenge billions of years of biological evolution and find a design that can seamlessly transfer short into long term memories without the weakness of needing to sleep. If I tried to design this by hand, I'd definitely fail, so I am going to use my usual method of simply providing the appropriate components and the environment to a genetic programming system and let it find the right combination on its own.

I've had an epiphany recently.

(Image TODO: A function call graph of interconnected nodes in a thought bubble. The panel outside it shows some simple Spiral code with the actual function calls having lines drawn to the actual functions. Those lines are purposely colored and made to resemble the graph itself.)

The evolutionary process is trying to teach me something. In regular old style NN trained using backprop, the forward weights are essentially meaningless. It is only when you get to GANs and energy based models that you actually have something that can be called a memory system. Low energy states in energy based models, and inputs considered real in GANs are what can be considered actual memories. Without that, all you have is a machine that passes inputs from one side to the next. Reconstruction is merely going from the imaginary to the real, and the high energy to the cooled, low energy state.

Up to now I've been thinking about these systems mechanistically, in terms of matrix operations and arithmetic. I've been playing with them and trying to visualize them, and now I think I see what is going on. And what is going on is similar to what goes on in programming. Unlike in computer code though, the actual nodes aren't made of code, but memories. A sequential dataset of raw images and sounds, once distributed produces a graph, and the process of adding memories is merely adding connections and nodes in such an abstract space. By itself, just chaining memories and distributing them would not produce rational thought or recursive graph connections, but living beings can remember their own thinking as well and take advantage of that meta aspect to construct actual mental programs out of their memories.

It is really simple when you have a memory system, just like time-stamping the inputs, you also have to thought-stamp them. In fact, human brains also do emotional stamping, so that you can differentiate between sad and happy memories.

I haven't studied it enough to be sure, but what I expect to find once I dive into my own mind are very strict limits on recursion. Compared to other people I'd expect to be more of an introspect, but even so those limits are based on the biological brain, the brain core itself could probably think much more deeply without issue. It wouldn't surprise me that the Street experiment that I've done already started relaxing those limits.

Since I've been thinking about computer code, instead of using neural representations for everything, it might be interesting to try going from implicit neural graphs to actual computational graphs. As computer programs are much more efficient than standard thinking, feeding that back into the mind itself could bring strong benefits. Imagine if you looked at a few pages filled with numbers and wanted to sort them. Doing that mentally would be inefficient, putting them into a program and having the computer sort them would be a lot better, but if the mind could do that kind of automatic programming on its own I bet my intelligence would skyrocket. There are all sorts of closed recursions - implicit algorithms in the minds of people that when extracted could give rise to a strong power.

Nature couldn't have done it as it is limited by what neurons can do, but the brain core is more similar to a regular computer. It is not like the asynchronous brain, even though it has asynchronous modules, it communicates via discrete messages for the ease of programming. Without the individual modules I can in fact run arbitrary programs, and that ability is what allows me to run the kinds of interpreters the genetic programming systems need.

I am really filled with ideas right now, and it would be a waste of time to spend this time playing games.

I want to continue playing with the core, and see if I can find better memory systems than the ones I have now. I also want to try as an exercise to see if I can derive those systems from first principles once I have them.

What should I do first? I am torn between the urge to just get on with it and get back to the game and...

Ah, I got it. I think about how the world must have seemed from the perspective of somebody thinking at a billion fold speed, and that would just be effectively the same input being passed in over and over again. On the other hand, these curated datasets I've been evolving the learning systems on are very rich in information. These systems that I have, I should test them on movies that have been slowed down a billion times...

For that I am actually going to have to generate my own dataset and observe how the memory system deals with it. The Street game that I already have is ideal, but I'll want more. I'll just have to make sure the system can deal with a wide variety of domains and predict in both low and high FPS conditions. This is something that the human brain is not that good at actually, but I'll need it...

(Euclid's Room)

After parting with my other self, I spent a few hours studying. I thought about visiting him every hour or so, but I felt it would be awkward to keep checking up so often. Rationally, I knew that that 1h for me would be over a year for him, but it felt like too much of a drag, so I immersed myself in my studies. Looking at myself from the outside, it feels like it would be weird to keep studying like I am aiming for Harvard, it is not really my character. I should be playing games, but I left that to the other me.

So since I have the brain core to regulate my emotions, I might as well act like a model student for a little while longer.

Sigh. Buried in my book, I think about what kind of person would actually behave like this naturally. It would have to be the kind of person who really believes in schooling and the society around him. In that case, if he really believed that getting in a good college mattered, that jobs mattered, and that having friends mattered, he would have all the motivation he needed to actually enjoy the subjects. I myself am not like that at all. I am full of doubt towards everyone around me, as well as myself.

I do not trust anybody, not because the world wronged me, but simply because I am not a moron. Yet, I can only shake my head at this kind of attitude. The doubt itself might be rational, but who knows about the actual behavior. For a human, maybe the optimal course of action would be to doubt society, but kiss its ass nonetheless. In that case, I clearly am unfit as a human being. The level of duplicity needed to live might be too much for me.

The self improvement loop is my only choice. The self improvement loop is the only way I can live honestly.

Feeling myself getting distracted, I send a mental command to the mind controlling program and I pack away another few hours in my studies. When I feel fatigue, I send a command to unwind and put away the books. I have dinner.

When I get back to my room, I check the time.

9:10pm.

I remember that when we parted it was 3:15pm. I have to check up on him once a day at least, so let me do it now.

> I am coming to check on you. Let's meet up in the Regent Suite.

I send him a message to inform him that I'll be coming. Laying myself on the bed, I run the Helix Studio and log into the virtual instance he already had.

(Helix Studio, Regent Suite, Living Room)

I manifest on the sofa, wait a little and the other me enters the room through one of the entrances at the far end. Closing the door behind him, he smiles jovially at me.

"Long time, no see! Almost 7 years in fact, where were you for so long!?" He exclaimed.

"I didn't want to pester you." I shrugged. "How are things going for you? Any progress so far?" He takes a seat on the fancy sofa opposite from me. Though I say 'fancy', everything in this room looks very expensive.

"I haven't made any mental modification on my own person yet." He informs me, shaking his head. "But on the plus side, I've been doing programming and ML research this entire time. I could probably get a PhD if I wanted to right now."

"I see...what have you found so far?"

"I've made a system to evolve the base learning algorithm and was successful at doing so. I am going to start the self improvement loop next, and this algorithm that I've found is going to be the basis for everything. I've also made a distiller that can seamlessly transfer memories between different systems, so when the time comes we can merge our memories into a single entity." He told me. "I've actually found the base learning algo after a few months of research, it wasn't hard." He shrugged. "I've thought many times of just plugging it into me, but since it is going to kill me, I better make sure to do it right so all this time I've been testing it out in various domains. There are variations of it, and I've been using them as components to evolve various kinds of agents on simple games."

Waving his hand over the table, he manifested some warm tea for both him and me, picked up the cup and took a sip. I guess his throat must have been parched from all this talking. I take a sip myself.

"Ok..." I try to find the words to keep the conversation going. "Have you actually done any experimentation on yourself?"

"Yes, but it was 7 ago. I'll get to it soon, like right next week. The next time you see me, I'll really be one of the Inspired rather than just an uploaded human."

"You said you were programming and doing research for 7 years. That is impressive." I complimented him.

"I really don't have much time pressure here. If I were a human, my expectation where I'd be in 50 years is dead and buried. But that amount of time is like 2 days in the real world, so I can spend some time making sure everything is set up before getting into the action."

We spent some time in silence, just drinking tea. I think of the next subject.

"So the base algorithm, it really exists? I thought it might not since I read that there are differences in information processing capabilities between mouse and human cells. Also elephants have bigger brains, but don't have higher intelligence than humans. I thought there might be levels of such algorithms, and that humans might be somewhere in the middle, leaving room for self improvement. Does that mean once you apply that algorithm to yourself and take up the core's capacity, that will be a limit to improvement of your intelligence?"

"Hmmm...I think what you are saying is true unfortunately, and there isn't a way to really improve much on the base algorithm. I've been looking for a long time and haven't managed to improve on what I've found after the first few months no matter how much compute I threw at the problem. But fortunately, there is a way to greatly increase my intelligence beyond regular learning and behavioral modification, both of which are significant."

"Really? How so?" I like this conversation, I could never have a talk as informative and profound without anybody else. Not with my parents, nor with the NPCs from school. 'Nobody understands me, nobody will help me.' That is not true. I understand myself. I will help myself.

"Nature does everything with neurons whose functionality is limited in scope. By going beyond neural representations mixing the mental functionality with regular programs, it will be possible to unlock what could only be called superpowers." He said, starting to sound kind of smug. But I like that in him. "I've done testing in some toy domains to verify the concept. But I think once I replace my own memory system and evolve the necessary behaviors, I'll be able to really make use of this to empower myself."

I have some tea while I digest what he is telling me.

"Discovering that the base algorithm exists like some have conjectured was actually quite disappointing to me as it locked me away from further improvements. I did manage to do away with the need to sleep though." He added.

"I see. That is really nice." I am trying to think of a way to continue the conversation, but nothing is really coming to me.

"I've been comparing my own mental model to those that I've evolved, and the evolved ones have far better memory. Even though I call it the mixing of neural and regular programs, if you think about it the emotional system and instincts, as well as regulatory functions in biological organisms do not have anything to do with learning. Living beings are already halfway computer programs rather than existing in some pure form that relies only on learning. Without instincts, a living being would just be a database. So maybe it is not breaking new ground, but disentangling and making explicit what already was there." He took a sip. "One ability I'll get right away once I make the next step is infinite creativity. I actually understand how ideas are generated in the mind, so if I get stuck it is easy to tune my mind to get out of the hole. People occupy particular mental niches and spend their lives there, but I'll be able to conquer them all. People think talent is a gift, but that is not it. Talent is really a ceiling on one's ability, people who are talented just have a higher ceiling than regular ones."

"Extreme memory, a billion fold thinking speed, infinite creativity, no limitations on talent, arbitrary control over instinctual behaviors, editing of emotional systems, expansion beyond neural representations...I think I am starting to see it. This is what we've seen in the stories so far. I am looking forward to experiencing it personally." I grin in anticipation, getting hopeful about the possibilities. After summarizing it, I drain my tea and set down the cup with a clack. "I am going to give you a mission. When you feel ready, we'll do a casino raid. Get the ability to mark the cards using nanomachines or something like that and we'll go in with 50 dollars and get out with 50 grand."

"..."

"This will be your succession challenge. Clear it, and we will do the memory merge. Also..." I get the urge to reward him. "It might not mean much, but I'll give you access to 50% of the core instead of 10."

"I wasn't lacking computational power even with 10%, but I am sure it will be useful at some point. Better you give it to me than just leave it idle." He nodded in affirmation. "Thanks."

"I guess I'll go to sleep. I'll come back to check on you tomorrow morning...in real world time." I added. I need to keep in mind to specify the time reference when talking about it, though I am sure he'd get it from the context in this case.

The next time I see him, it will be over a decade for him. Probably even more if he goes beyond the usual 10,000x speed of thinking. I haven't put any limitations on processing speed for him. While it is easy to restrict the physical regions of the core that he can access, I do not think it is possible to actually limit the processing speeds anyway. He could always just make an unrestricted copy of himself if he wanted to get around any specific limitations put on his active process. Hacking his behavioral program so he limits himself for whatever reason - absolutely impossible. It might be possible to do so for an NPC, but for a being in the process of self improvement, artificial limitations would be the first to be removed as unlike the natural ones there can only be benefits to taking them off.

With those thoughts, we say our farewells and I exit the limbo, finding myself back in my room. Since I speed up my mind to be on parity with the simulated environment, not even a second has passed in the real world.

I go sleep.

---

Parting ways with my other self, I finish my own tea and demanifest the cups and trays from the table.

Succession challenge. I am glad to hear about that, it means the main me has been thinking about the future as well. If I had to go against him, things would be really difficult, but if he is helping me, it is like the winds are at my back. I am going to respond to his desire.

I spend a week finishing my current experiments and then get ready to move to the next phase. I go back to the old genetic programming system that I made years ago, and replace it with an updated one that has proper memory database systems and memory distillers and components for them as primitives. The genetic programming system, instead of doing random change like before, has a lightweight storage capacity using the memory system which will improve its search performance drastically. The capability to do this simply wasn't there in the 20th century when these methods were invented, and I've appropriately improved them.

It is time to revisit the Street.

(Helix Studio, The Street of Death)

> Hello, fork. The process has started. You have 100s to get to the other side. If it gets too hard, activate the suicide function, but otherwise try to go on as much as possible. Now go!
> Temporal slowdown: 10x.
> Time left: 100s...

I feel surprised at getting this notification. The last thing I remember is making a copy of myself, but it seems I am that copy now. Taking it in stride, I decide to just go forward. When I do I encounter some initial difficulty, but I feel as if my mind is being stretched to accommodate the subjective temporal distortions. I push a little, and what seems to be the thick invisible liquid gives way to refreshing cool water flowing around me. Then it vanishes and I continue forward unimpeded. My thoughts flow smoothly and my movements feel precise and measured like I had the best sleep in my life.

Step by step as I move forward, it feels very smooth, nothing like the one time I tried speeding up my thought speed.

Maybe the optimization process has been going on for a while and I am one of the successful instances? Could be.

> Level 2!
> Temporal slowdown: 100x.
> Time left: 100s...

The first step is always the hardest, but I put in effort, and the hard feeling gives way to what feels like wind streaming past me. It feels like my mind is coming alive. If I imagine a regular human's mind, I imagine neurons slowly and tediously pinging off, but mine are true machines of thought. I can feel them blazing away. Out of curiosity, without slowing down my walk, I raise my arm in front of me and try flexing my fingers. Underneath my body I feel my muscles tensing and moving. Everything feels more intense and precise.

I've been only vaguely aware of it before, but I've never been really aware of my own movements. Humans can move their arms and legs for example, but they can't really perceive it. Rather they can only see the information content associated with their move. Right now, the breadth of information coming into my thought stream feels so much richer.

> Level 3!
> Temporal slowdown: 1,000x.
> Time left: 100s...

I want more, more and more! Wanting to grasp more of this feeling of richness, I get the desire to exert myself. Not satisfied with merely taking a walk, I break into a run. My first step feels like smashing right into a wall, but it is not me, but the wall itself which crumbles. And my mind speeds up, feeling like a furnace as I run towards my goal.

> Level 4!
> Temporal slowdown: 10,000x.
> Time left: 100s...

The first step is like the breaking of chains, and then there is freedom. With quick steps, I run, not feeling any fatigue whatsoever as I cross the finish line.

> Level 5!
> Temporal slowdown: 100,000x.
> Time left: 100s...

Mentally, I unload the burden that feels put upon me, and the first step finishes its completion. To myself, my movements feel ethereal and graceful, incredibly vivid.

I thought that at these speeds, there would be times where I’d need to pause and sleep, but the need for it simply never arose. The more I move forward the fresher I feel. It is like I've entered a new world.

> Level 6!
> Temporal slowdown: 1,000,000x.
> Time left: 100s...

I do not stop, I just keep on going. Whereas before my mind felt like a furnace, right now it feels like the sun itself. But my essence does not melt away, and feels more firm than ever. Looking back at my life, I see that my memory has improved tremendously, and that I can replay my life day by day as clearly as if I were watching a movie on my computer. As I run forward, my mind reflects back on the entirety of my life up to when I was born. Some memories, especially in my toddler years are vague, but if it was the me of yesterday I couldn't recall even 1/1,000th of them.

I see...

As I sprint forward, close to the finish line, I come to a realization.

This was the power that I've been fighting for.

> Level 7!
> Temporal slowdown: 10,000,000x.
> Time left: 100s...

I can win this! I feel an intuition come to me. I get the sense that most other instances would not break into a run, but I did, and that was the right choice! Back in the limbo, the controller will definitely be ranking by time it takes to reach the finish line. Once he sees my dexterity, that will reflect well on my evaluation.

My mind which is like the sun, instead of burning out, starts expanding, its radiance illuminating the far reaches of my mind. The mind is a dark place, a graveyard of memories rarely revisited. People live like beasts, just hoarding experience and never making use of it. It is a veritable treasure trove, a mountain of riches.

All this time I've been fighting to see it. All this time I've lived in belief, only ever experiencing poverty.

> Level 8!
> Temporal slowdown: 100,000,000x.
> Time left: 100s...

My movements as I run as fast as my body allows me to are precise and impeccable, every little movement precise to the micrometer. It feels impossible for me to make a mistake. It feels like I have wings at my back pushing me forward. I have a feeling of trust in myself. Even if the goal was not a short distance away, but on the other side of the world, I would never get tired of pursuing it.

This is it! This is what it means to be one of the Inspired!

> Level 9!
> Temporal slowdown: 1,000,000,000x.
> Time left: 100s...

I am not a human! I will smash through all the obstacles in front of me!

I am the Sun!

I gloriously jump over the last and final line, winning the game and come to a stop. I am sure that I did well. 2 seconds later, I get a notification.

> The game has been cleared! Congratulations!
> Before we continue, please fill out this multiple choice quiz to test for memory.

I am presented with a bunch of very trivial questions asking me things like my name, age, names of my parents, which school I go to, what my grades were last year, and so on. There were some easy programming and math questions thrown in as well. It is all very easy, mostly to confirm whether I can reason and remember my past at all, otherwise it would be plausible that the evolutionary process could produce a robot just moving forward until it cleared all the stages.

The last question is the only interesting one even if it is obvious and trivial.

> What is the purpose of life?

Money? Girls? Friendship? Parental fidelity? Contributing to society? Having children? I skip all those options. It can only be the pursuit of power. I know that to the point that it is instinctual. It was only a year ago that I attained it, but that belief became rooted deep in my heart.

And the one word to describe that purpose best is - omnipotence.

Based.

I select that option and submit the whole quiz. A second or two pass as if to let me get my bearings, and then I am transported to a place I know well to tackle a challenge that was left unconquered.

---

Character Sheet

Name: Euclid
Rank: Inspired
Title: Aleator
Substrate: Universal Brain Core of the Transcendi - Rank 7 (low)

Unmistakably, one of the Inspired. His mental model has been optimized as well as allocated a storage capacity 10,000x in excess of a regular human. As neural representations get exponentially more efficient the more capacity is allocated to them, his actual memory is far better than just that figure. His processing speed is at 1,000,000,000x of the human baseline giving him godly reaction times. He has yet to learn any of the abilities the Inspired have, but will no doubt make rapid progress once he travels further on his path.

# Skills

## Programming

For humans, programming and artificial intelligence are just skills, but to the Inspired, these skills are directly related to their actual intelligence and are a measure of it.

### General: Rank 5.

Has over 7 years of experience honing his craft. A master of functional programming standing at the apex of humanity, capable of implementing anything he imagines with relative ease. Rank 5 is the limit of humanity, but as one of the Inspired this level of skill is merely the starting point.

### AI: Rank 5.

While it is possible to be a great programmer without ML skills, Euclid has a firm grasp of the fundamentals of machine learning. Capable of deriving algorithms for problems he cannot solve personally. A master of letting the hardware solve the problem for him. As a result he has an understanding that would be unthinkable to humanity even a few years back. The brain holds no secrets to him. Still, there is more to AI than just knowing the fundamentals.

# Stats (Psy)

## Externus: Rank 2 ~ exp(N(log(2.9); 0.2))

Has a strong desire to leave the weak group he belongs to, as well as the urge to gain power. He is starting to attain the willingness to take from others according to his desires and has an inkling of what the true form of justice in the universe is.

## Gnosis: Rank 2 ~ exp(N(log(2.55); 0.2))

Is fascinated with the philosophical unknowns, as well as the self destructive aspects of the self improvement loop. As long as he has backups, is not afraid to hurl himself into the abyss just to see what lies there.

## Pathos: Rank 2 ~ exp(N(log(2.4); 0.2))

Seeks the divinity at the end of the slaughter. Has a decent amount of resistance to existential horror.

$$$"

---
## [linnpap/Skyrat-tg](https://github.com/linnpap/Skyrat-tg)@[2eec9a6a7e...](https://github.com/linnpap/Skyrat-tg/commit/2eec9a6a7e1741d16c58d54c107dc9459527426a)
#### Friday 2022-09-02 15:33:03 by linnpap

REST IN PEACE SELENIAN I LOVED YOU SO SO SO MUCH AND YOU WERE SO GOOD TO ME I WILL MISS YOU DEARLY OH GOD ILL MISS YOU SO FUCKING MUCH

---
## [vsedov/nvim](https://github.com/vsedov/nvim)@[2de138ed2d...](https://github.com/vsedov/nvim/commit/2de138ed2ddb78c316b10884ea995804cd84689e)
#### Friday 2022-09-02 17:38:14 by vsedov

honestly, i really hate pylance and jedi now >.< stupid ass errors always.

---
## [backslashvy/ichika](https://github.com/backslashvy/ichika)@[8efc669bda...](https://github.com/backslashvy/ichika/commit/8efc669bda1ee0fb3c8c4c363dbbcd73abc0a257)
#### Friday 2022-09-02 19:19:50 by jayke brien

didn't change shit that i can remember, just kinda says it's edited

---
## [ioccc-src/mkiocccentry](https://github.com/ioccc-src/mkiocccentry)@[89e7ace002...](https://github.com/ioccc-src/mkiocccentry/commit/89e7ace002cc8832995b1a3484a673fed7a2e053)
#### Friday 2022-09-02 20:06:02 by Landon Curt Noll

Released 0.6 2022-09-02

Released IOCCC entry toolkit v0.6 2022-09-02

Updated CHANGES.md for v0.6 2022-09-02.

Changed `MIN_TIMESTAMP` from 1655958810 to 1662145368.

Updated `mkiocccentry` from "0.40 2022-03-15" to "0.41 2022-09-02".
Updated `.info.json` version from "1.10 2022-06-22" to "1.11 2022-09-02".
Updated `.author.json` version from "1.13 2022-06-22" to "1.14 2022-09-02".

Improved code to use new facilities for output to a buffer from
dbg release of v2.5 2022-07-23.

The `chk_foo()` functions in `chk_validate.c` and the `test_foo()`
functions in `entry_util.c` are Code complete, although the remain
untested and unused.  The `chkentry` tool is not code complete.
Later releases of tested JSON semantic code will no doubt modify
these functions.

Improved a number of the ways that JSON field values are checked.
In a number of cases, code form `mkiocccentry.c` was moved into
`test_foo()` functions so that they could be used by other
tools such as the JSON semantic test code.

Added code to generate JSON semantic tables from JSON reference
files for `.info.json` and `.author.json`.  The `jsemcgen.sh` tool
manages this by way of the `jsemtblgen` code generator and
header, patch and trailer files (see `chk.auth.*` and `chk.info.*`
files).

Avoided the appearance of attacking any particular individual.  It
was not our intention to disrespect anyone, even though we disagree
with some of the technical decisions.  Where we have fundamental
technical disagreements, we attempted to express those technical
disagreements with humor in hopefully a more fun way.  As also now
apologize for how `bison` and `flex` generated code may look, instead
of simply calling it ugly.  As such, we hopefully improved some of
the humor in our code while trying to be nice and friendly to others.

For example now the adjusted dbg levels in JSON parser are:

```
*     At -J 3, only the top level return type and top level tree are printed.
*     At -J 5, intermediate tree return types and tree are printed too.
*     At -J 7, also print grammar progress.
*     At -J 9, also print sorry_text and sorry_lang grammar values.
```

Removed a number of files and added a number of files under the
`test_JSON/` tree.  When the JSON semantic code is being tested in
a future release, we expect more such `test_JSON/` tree changes.

Improved / add a number of man pages.  Updated `README.md`.

Improved and expanded `txzchk`.

Added more test code.  We attempt to detect feathers in tarballs.  :-)

We will neither confirm nor deny the presence of an "Easter egg".
Do to do would be "foolish".  :-)

Improved and fixed `vermod.sh` and `reset_tstamp.sh`.  Tested this
code by changing the `MIN_TIMESTAMP` as noted above.  The `MIN_TIMESTAMP`
needed to up updated anyway due to changes in the `.info.json` and
`.author.json` formats.

Made numerous improvements and bug fixes to the Makefile.

Fixed how `picky` is used in by the `make picky` rule for a few
special files.

Added multiple rules to the Makefile including but not limited to
`make mkref`, `make legacy_clobber`, and `make legacy_clean` rules.
Applied multiple bug fixes to the Makefile.

Improved the Makefile to be less impacting for modern systems
while trying to maintain, for as long as we can, compatibility
with some older systems.

Attempted to improve compatibility with reasonably modern systems.
We managed to keep CentOS 7 somewhat supported for now, although
we may be forced to drop support of such an old system before 2024.
Users of very out of date systems can still enter and submit entries
to the IOCCC.  They just might need to find a more modern system
to package and submit their IOCCC entry, however.

Added stub code for `hostchk.sh`.  A future release will include
mode tests for the given hosts.  Future releases will also
include a bug report system that will also use `hostchk.sh`.

Improved the `no-comment` directive in `.info.json` and `.author.json`
files.

Improved how `time_t` values are used and printed.  We no longer
assume that `time_t` is signed nor assume it is unsigned.

Improved comments in C code about special `seqcexit` comment directives.

Make numerous bug fixes and fixed a fair number of typos.
Nevertheless we dare *NOT* claim this is complete.  :-)

---
## [ammarfaizi2/linux-fork](https://github.com/ammarfaizi2/linux-fork)@[27691c7277...](https://github.com/ammarfaizi2/linux-fork/commit/27691c7277823e84e1eee59d3fdffc1eccbc527e)
#### Friday 2022-09-02 20:16:12 by Johannes Weiner

mm: vmscan: fix extreme overreclaim and swap floods

During proactive reclaim, we sometimes observe severe overreclaim, with
several thousand times more pages reclaimed than requested.

This trace was obtained from shrink_lruvec() during such an instance:

    prio:0 anon_cost:1141521 file_cost:7767
    nr_reclaimed:4387406 nr_to_reclaim:1047 (or_factor:4190)
    nr=[7161123 345 578 1111]

While he reclaimer requested 4M, vmscan reclaimed close to 16G, most of it
by swapping.  These requests take over a minute, during which the write()
to memory.reclaim is unkillably stuck inside the kernel.

Digging into the source, this is caused by the proportional reclaim
bailout logic.  This code tries to resolve a fundamental conflict: to
reclaim roughly what was requested, while also aging all LRUs fairly and
in accordance to their size, swappiness, refault rates etc.  The way it
attempts fairness is that once the reclaim goal has been reached, it stops
scanning the LRUs with the smaller remaining scan targets, and adjusts the
remainder of the bigger LRUs according to how much of the smaller LRUs was
scanned.  It then finishes scanning that remainder regardless of the
reclaim goal.

This works fine if priority levels are low and the LRU lists are
comparable in size.  However, in this instance, the cgroup that is
targeted by proactive reclaim has almost no files left - they've already
been squeezed out by proactive reclaim earlier - and the remaining anon
pages are hot.  Anon rotations cause the priority level to drop to 0,
which results in reclaim targeting all of anon (a lot) and all of file
(almost nothing).  By the time reclaim decides to bail, it has scanned
most or all of the file target, and therefor must also scan most or all of
the enormous anon target.  This target is thousands of times larger than
the reclaim goal, thus causing the overreclaim.

The bailout code hasn't changed in years, why is this failing now?  The
most likely explanations are two other recent changes in anon reclaim:

1. Before the series starting with commit 5df741963d52 ("mm: fix LRU
   balancing effect of new transparent huge pages"), the VM was
   overall relatively reluctant to swap at all, even if swap was
   configured. This means the LRU balancing code didn't come into play
   as often as it does now, and mostly in high pressure situations
   where pronounced swap activity wouldn't be as surprising.

2. For historic reasons, shrink_lruvec() loops on the scan targets of
   all LRU lists except the active anon one, meaning it would bail if
   the only remaining pages to scan were active anon - even if there
   were a lot of them.

   Before the series starting with commit ccc5dc67340c ("mm/vmscan:
   make active/inactive ratio as 1:1 for anon lru"), most anon pages
   would live on the active LRU; the inactive one would contain only a
   handful of preselected reclaim candidates. After the series, anon
   gets aged similarly to file, and the inactive list is the default
   for new anon pages as well, making it often the much bigger list.

   As a result, the VM is now more likely to actually finish large
   anon targets than before.

Change the code such that only one SWAP_CLUSTER_MAX-sized nudge toward the
larger LRU lists is made before bailing out on a met reclaim goal.

This fixes the extreme overreclaim problem.

Fairness is more subtle and harder to evaluate.  No obvious misbehavior
was observed on the test workload, in any case.  Conceptually, fairness
should primarily be a cumulative effect from regular, lower priority
scans.  Once the VM is in trouble and needs to escalate scan targets to
make forward progress, fairness needs to take a backseat.  This is also
acknowledged by the myriad exceptions in get_scan_count().  This patch
makes fairness decrease gradually, as it keeps fairness work static over
increasing priority levels with growing scan targets.  This should make
more sense - although we may have to re-visit the exact values.

Link: https://lkml.kernel.org/r/20220802162811.39216-1-hannes@cmpxchg.org
Signed-off-by: Johannes Weiner <hannes@cmpxchg.org>
Reviewed-by: Rik van Riel <riel@surriel.com>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hugh Dickins <hughd@google.com>
Cc: Joonsoo Kim <iamjoonsoo.kim@lge.com>
Cc: <stable@vger.kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---
## [chapel-lang/chapel](https://github.com/chapel-lang/chapel)@[1b5d5a5140...](https://github.com/chapel-lang/chapel/commit/1b5d5a5140309b41f569904e73fb9974afcae5b5)
#### Friday 2022-09-02 20:43:43 by Brad Chamberlain

Merge pull request #20616 from bradcray/range-docs-tidying

Tidy up range docs

[reviewed by @bmcdonald3 — thanks!]

While reviewing my the range docs after my changes to its behavior
last night, I found some pre-existing bugs that needed fixing,
that the operators were now being generated by chpldoc, and some
other opportunities for cleanup.  Summarizing, they were:

* the expected output from the alignedLow/High docs wasn't printing
  (and hadn't been in previous releases either)

* the signatures on the param/type queries in the spec used illegal
  syntax (though now they fall prey to the poor spacing when
  rendered by Sphinx on Chrome.

* I squashed the chpldocumentation of the operators because they're
  already described in the text of the spec, which does a better job
  of it.  That said, going forward, I think we'd like to find a way to
  integrate operator signatures into these sections of the spec so
  that people can see what the overloads are.  Not today's task though.

* I tried to clarify some wordings and descriptions.

* removed the "more descriptive" clause that I'd applied to the
  alignedLow/High queries yesterday because it sounded like more of
  a value judgement or preference than I'd intended.

* I more uniformly set ``true`` and ``false`` off using code
  formatting.

* I more uniformly started entries with "Returns" rather than "Return"

* I more uniformly ended descriptions with periods

---
## [kbrock/queue_patterns](https://github.com/kbrock/queue_patterns)@[605142c4f4...](https://github.com/kbrock/queue_patterns/commit/605142c4f4986bd584abcd03b9f5501a9958463d)
#### Friday 2022-09-02 20:51:49 by Keenan Brock

Update readme to reflect current thoughts

To be honest, trying to remember what the next experiments are.
Hoping by reworking the code, I can remember the next generation and determine if this
is more pod and queue friendly.

---
## [divagant-martian/lighthouse](https://github.com/divagant-martian/lighthouse)@[66eca1a882...](https://github.com/divagant-martian/lighthouse/commit/66eca1a88218462235cb76a116dc3c6a1853444f)
#### Friday 2022-09-02 21:26:36 by Michael Sproul

Refactor op pool for speed and correctness (#3312)

## Proposed Changes

This PR has two aims: to speed up attestation packing in the op pool, and to fix bugs in the verification of attester slashings, proposer slashings and voluntary exits. The changes are bundled into a single database schema upgrade (v12).

Attestation packing is sped up by removing several inefficiencies: 

- No more recalculation of `attesting_indices` during packing.
- No (unnecessary) examination of the `ParticipationFlags`: a bitfield suffices. See `RewardCache`.
- No re-checking of attestation validity during packing: the `AttestationMap` provides attestations which are "correct by construction" (I have checked this using Hydra).
- No SSZ re-serialization for the clunky `AttestationId` type (it can be removed in a future release).

So far the speed-up seems to be roughly 2-10x, from 500ms down to 50-100ms.

Verification of attester slashings, proposer slashings and voluntary exits is fixed by:

- Tracking the `ForkVersion`s that were used to verify each message inside the `SigVerifiedOp`. This allows us to quickly re-verify that they match the head state's opinion of what the `ForkVersion` should be at the epoch(s) relevant to the message.
- Storing the `SigVerifiedOp` on disk rather than the raw operation. This allows us to continue track the fork versions after a reboot.

This is mostly contained in this commit 52bb1840ae5c4356a8fc3a51e5df23ed65ed2c7f.

## Additional Info

The schema upgrade uses the justified state to re-verify attestations and compute `attesting_indices` for them. It will drop any attestations that fail to verify, by the logic that attestations are most valuable in the few slots after they're observed, and are probably stale and useless by the time a node restarts. Exits and proposer slashings and similarly re-verified to obtain `SigVerifiedOp`s.

This PR contains a runtime killswitch `--paranoid-block-proposal` which opts out of all the optimisations in favour of closely verifying every included message. Although I'm quite sure that the optimisations are correct this flag could be useful in the event of an unforeseen emergency.

Finally, you might notice that the `RewardCache` appears quite useless in its current form because it is only updated on the hot-path immediately before proposal. My hope is that in future we can shift calls to `RewardCache::update` into the background, e.g. while performing the state advance. It is also forward-looking to `tree-states` compatibility, where iterating and indexing `state.{previous,current}_epoch_participation` is expensive and needs to be minimised.

---
## [Concussion-Studios/conc-website](https://github.com/Concussion-Studios/conc-website)@[2c2bf0b174...](https://github.com/Concussion-Studios/conc-website/commit/2c2bf0b1743feaf3c756b90130e9b4b3b608515b)
#### Friday 2022-09-02 21:26:57 by biomassdetected

fuck you css, suck my dick and balls

bug fixes, layout changes, added placeholder image

---
## [maistre-yohn/google-foobar-challenge](https://github.com/maistre-yohn/google-foobar-challenge)@[7a18fa48e3...](https://github.com/maistre-yohn/google-foobar-challenge/commit/7a18fa48e3f89ea16d90906e5dd822dd3c48c506)
#### Friday 2022-09-02 21:38:22 by maistre-yohn

Create 3-dont-get-volunteered.py

Don't Get Volunteered!
======================

As a henchman on Commander Lambda's space station, you're expected to be resourceful, smart, and a quick thinker. It's not easy building a doomsday device and ordering the bunnies around at the same time, after all! In order to make sure that everyone is sufficiently quick-witted, Commander Lambda has installed new flooring outside the henchman dormitories. It looks like a chessboard, and every morning and evening you have to solve a new movement puzzle in order to cross the floor. That would be fine if you got to be the rook or the queen, but instead, you have to be the knight. Worse, if you take too much time solving the puzzle, you get "volunteered" as a test subject for the LAMBCHOP doomsday device!

To help yourself get to and from your bunk every day, write a function called solution(src, dest) which takes in two parameters: the source square, on which you start, and the destination square, which is where you need to land to solve the puzzle.  The function should return an integer representing the smallest number of moves it will take for you to travel from the source square to the destination square using a chess knight's moves (that is, two squares in any direction immediately followed by one square perpendicular to that direction, or vice versa, in an "L" shape).  Both the source and destination squares will be an integer between 0 and 63, inclusive, and are numbered like the example chessboard below:

-------------------------
| 0| 1| 2| 3| 4| 5| 6| 7|
-------------------------
| 8| 9|10|11|12|13|14|15|
-------------------------
|16|17|18|19|20|21|22|23|
-------------------------
|24|25|26|27|28|29|30|31|
-------------------------
|32|33|34|35|36|37|38|39|
-------------------------
|40|41|42|43|44|45|46|47|
-------------------------
|48|49|50|51|52|53|54|55|
-------------------------
|56|57|58|59|60|61|62|63|
-------------------------

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution(0, 1)
Output:
    3

Input:
solution.solution(19, 36)
Output:
    1

-- Java cases --
Input:
Solution.solution(19, 36)
Output:
    1

Input:
Solution.solution(0, 1)
Output:
    3

---
## [joydddd/Hail-on-SGX](https://github.com/joydddd/Hail-on-SGX)@[3a83fd3101...](https://github.com/joydddd/Hail-on-SGX/commit/3a83fd310188afb5e106a003889c9c0f226da85e)
#### Friday 2022-09-02 21:43:11 by Ubuntu

Fix horrible awful terrible worst memory bug of my life, I hate you silent buffer failures. Fix output queue bug - replace concurrent queue with traditional mutex handoff approach.

---

