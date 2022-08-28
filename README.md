## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-08-27](docs/good-messages/2022/2022-08-27.md)


1,583,982 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,583,982 were push events containing 2,167,251 commit messages that amount to 127,632,017 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 40 messages:


## [Libertus-Lab/react](https://github.com/Libertus-Lab/react)@[b6978bc38f...](https://github.com/Libertus-Lab/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Saturday 2022-08-27 00:14:15 by Andrew Clark

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
## [foreverLoveWisdom/command-t](https://github.com/foreverLoveWisdom/command-t)@[148e54a6c1...](https://github.com/foreverLoveWisdom/command-t/commit/148e54a6c1941beaaf940ff703dc2bff511b6def)
#### Saturday 2022-08-27 00:35:36 by Greg Hurrell

feat: continue adding to Lua port

Yeah, this is a horrible mixed-bag commit. Just showing that we can
compile multiple translation units in a single invocation (may want to
refactor the Makefile to do that a little more traditionally, to be
honest; compile each source individually, then link... but then again,
this is simple and the project is tiny so speed is not a concern).

---
## [Marcus-Arcadius/stable-diffusion-webui](https://github.com/Marcus-Arcadius/stable-diffusion-webui)@[4f8dd02ccb...](https://github.com/Marcus-Arcadius/stable-diffusion-webui/commit/4f8dd02ccb69f5e457226531a82f54fa4dfe97ea)
#### Saturday 2022-08-27 01:21:14 by Georg Zoeller

Adding .png metadata 

This may open the option to read data from images dragged into the tool later.  Activated with --save_metadata

Properties (example output from imagemagic 'identify -verbose' command:
    SD:cfg_scale: 7.5
    SD:GFPGAN: False
    SD:height: 512
    SD:normalize_prompt_weights: True
    SD:prompt: a beautiful matte painting of a cottage on a magical fantasy island, unreal engine, barometric projection, rectilinear
    SD:seed: 247624793
    SD:steps: 50
    SD:width: 512

---
## [SunnyAmirize/The-University-of-Texas-at-Austin-Data-Science-Business-Analyst-Postgrad-Diploma-Program](https://github.com/SunnyAmirize/The-University-of-Texas-at-Austin-Data-Science-Business-Analyst-Postgrad-Diploma-Program)@[1e31286296...](https://github.com/SunnyAmirize/The-University-of-Texas-at-Austin-Data-Science-Business-Analyst-Postgrad-Diploma-Program/commit/1e3128629675d8bbd8225b27d6ad1ec30334fe14)
#### Saturday 2022-08-27 01:32:01 by Sunny Amirize

Create README.md

Context
A significant number of hotel bookings are called off due to cancellations or no-shows. The typical reasons for cancellations include change of plans, scheduling conflicts, etc. This is often made easier by the option to do so free of charge or preferably at a low cost which is beneficial to hotel guests but it is a less desirable and possibly revenue-diminishing factor for hotels to deal with. Such losses are particularly high on last-minute cancellations.

The new technologies involving online booking channels have dramatically changed customers’ booking possibilities and behavior. This adds a further dimension to the challenge of how hotels handle cancellations, which are no longer limited to traditional booking and guest characteristics.

The cancellation of bookings impact a hotel on various fronts:

Loss of resources (revenue) when the hotel cannot resell the room.
Additional costs of distribution channels by increasing commissions or paying for publicity to help sell these rooms.
Lowering prices last minute, so the hotel can resell a room, resulting in reducing the profit margin.
Human resources to make arrangements for the guests.
Objective
The increasing number of cancellations calls for a Machine Learning based solution that can help in predicting which booking is likely to be canceled. INN Hotels Group has a chain of hotels in Portugal, they are facing problems with the high number of booking cancellations and have reached out to your firm for data-driven solutions. You as a data scientist have to analyze the data provided to find which factors have a high influence on booking cancellations, build a predictive model that can predict which booking is going to be canceled in advance, and help in formulating profitable policies for cancellations and refunds.

Data Description
The data contains the different attributes of customers' booking details. The detailed data dictionary is given below.

Data Dictionary

Booking_ID: unique identifier of each booking
no_of_adults: Number of adults
no_of_children: Number of Children
no_of_weekend_nights: Number of weekend nights (Saturday or Sunday) the guest stayed or booked to stay at the hotel
no_of_week_nights: Number of week nights (Monday to Friday) the guest stayed or booked to stay at the hotel
type_of_meal_plan: Type of meal plan booked by the customer:
Not Selected – No meal plan selected
Meal Plan 1 – Breakfast
Meal Plan 2 – Half board (breakfast and one other meal)
Meal Plan 3 – Full board (breakfast, lunch, and dinner)
required_car_parking_space: Does the customer require a car parking space? (0 - No, 1- Yes)
room_type_reserved: Type of room reserved by the customer. The values are ciphered (encoded) by INN Hotels.
lead_time: Number of days between the date of booking and the arrival date
arrival_year: Year of arrival date
arrival_month: Month of arrival date
arrival_date: Date of the month
market_segment_type: Market segment designation.
repeated_guest: Is the customer a repeated guest? (0 - No, 1- Yes)
no_of_previous_cancellations: Number of previous bookings that were canceled by the customer prior to the current booking
no_of_previous_bookings_not_canceled: Number of previous bookings not canceled by the customer prior to the current booking
avg_price_per_room: Average price per day of the reservation; prices of the rooms are dynamic. (in euros)
no_of_special_requests: Total number of special requests made by the customer (e.g. high floor, view from the room, etc)
booking_status: Flag indicating if the booking was canceled or not.

---
## [jonahschimpf/MagicBook](https://github.com/jonahschimpf/MagicBook)@[b0f9736f6b...](https://github.com/jonahschimpf/MagicBook/commit/b0f9736f6bffa23d2a3e5ed8dc9e51796b06930c)
#### Saturday 2022-08-27 01:53:07 by jonahschimpf

Virtualize Pi Desktop and install spchcat

# How to download Raspberry PI Desktop for VMWare Fusion

Essentially, I downloaded this link:
https://www.raspberrypi.com/software/raspberry-pi-desktop/

Which installs the Raspberry PI Desktop Image: 2022-07-01-raspios-bullseye-i386.iso

This is the disk image that *is meant to run on a Mac or PC*, if you notice the architecture is x86 32-bit (i386).

After you install the iso, I selected Debian 10.x 64-bit. 

Next, select Legacy BIOS and around 60 GBs of disk space. This is quite a bit, but ensure we won't run out of disk space in the middle of all our stuff, which is super annoying. You'll probably wan't more than 4GBs of RAM as well (or more if you can spare it).

Afterwards select graphic install, it's easier. 

Make your account and allow for the updates to happen. Which took me a loong time.

Sometime after this, select: Guided use entire disk and set up LVM. 

Make all the files in one partition.

It will say something like "Write the changes to disk?" and you want to respond with "Yes" for this.

Even more installing will happen, just wait it out. Maybe read a book or make some tea. Don't look at the clock. 

Say yes to installing the GRUB boot loaded 

Say yes to /dev/sda being the primary partition.

Wait some more. The air conditioner just turned on in my apartment. Think about how long after you move out that same sound will be heard by other people and families. I wonder if it will be too loud for them too. 

It just turned off and now I hear crickets.

The installer will periodically ask you if something is ok to do and if you want to continue. I recommend to barely even read what it asks and just click *continue*.

Experience a sense of deja-vu when the installer asks you, yet again, to choose your default language. Click something like "English" but ,this time, do it suspicouly. 

Update the software again, this is weird. It tells me it's synchronising the clock (don't look at the clock).

This failed successfully, and now I'm greeted by the Raspberry Pi Desktop. Next up is installing spchcat.

## Installing *spchcat*

*spchcat* is a non-networked speech transcriber that runs an AI model to generate speech-to-text. Run the following commands (please)

sudo dpkg --add-architecture i386
sudo dpkg --add-architecture amd64
sudo apt-get install update

Then install the .deb package for x86 (not Raspberry PI) from the Gitub repo here: https://github.com/petewarden/spchcat/

Wait a little bit more. This reminds me of a short story, I'll upload it to the repo.

Wait a bit and run

sudo dpkg -i /path/to/deb/package

If it complains about the architecture, you probably installed the wrong one.

Running spchcat should give the error:
*No such file or directory* and running ldd should give something like *not a dynamic executable*

Notice that you probably don't have a /lib/x86_64-linux-gnu directory. This is important and also not good.

So try

sudo apt-get install gcc-multilib 
sudo apt-get install libpulse-dev:amd64

And then try:
spchcat

And it should work! Feel free to shout YES and wake up your neighbors.

---
## [Citadel-Station-13/Citadel-Station-13-RP](https://github.com/Citadel-Station-13/Citadel-Station-13-RP)@[24aca0ae55...](https://github.com/Citadel-Station-13/Citadel-Station-13-RP/commit/24aca0ae55ce2204474ec23fed6d23cb46b6645e)
#### Saturday 2022-08-27 02:29:35 by LordPapalus

Cargonia, but with less weapons (#4370)

* Cargonia is no more

Fuck you

* PLEASE

* Zandario, I will suck your PP

---
## [itseasytosee/tgstation](https://github.com/itseasytosee/tgstation)@[5dc17bd865...](https://github.com/itseasytosee/tgstation/commit/5dc17bd86556c01cc0f81f54a6ce270169c00088)
#### Saturday 2022-08-27 02:54:38 by san7890

Security's Scaling Departmental Accesses - More Pop, More Problems (#68534)

lternative to #68527
About The Pull Request

Hey there,

This is an alternative PR that I concocted based on talking with Goof on that PR. Basically, we already have a nicely complicated system to track and balance the number of security officers we have in a shift based on some config coefficient setting, by which we can set the amount of lockers that spawn in on the start of a round, as well as determine truly how many security officers we have.

image

So, I've decided to leverage this in another way. Basically, based on the number of security officers in a shift, their specific departmental officers will also get more (elevated) accesses. They already start with a certain amount of access, but they can get more if it is a low-pop shift with the mechanic introduced in this PR. For example, an Engineering Security Officer can access Atmospherics and Engineering departments by default, but they can't access Telecommunications unless there is a lower population of players AT SHIFT START. Same for a Medical Security Officer accessing Medbay, but not Plumbing.

Update: I have made it such that there are three system that server operators can set:

They can use the Scaling System that operates in the same method outlined in the rest of the PR.
They can disable giving departmental security officers "elevated access" (such as access beyond the "front doors") to these officers.
Finally, they can also just always ensure that departmental security officers get the maximal accesses possible.

The default setting is the "Scaling System" outlined in this PR, which is already dependent on the general Security Officer Scaling Co-Efficient.
Why It's Good For The Game

I think it's better to involve some more nuanced config scaling that we already have present in the game. The major theme that we want to avoid is that departmental security officers having maximal accesses when there is an already large number of persons on the security force will result in "miserable" shifts for the common person working within a department (security metaprotections). However, some server operators (as well as server cultures) tend to have very wide ranges in how many security officers they have on a shift-by-shift basis. One day, you could have 0-2 security officers, the next, you could have 4-6. It's all variable on who's playing (as always). There is also a significant variation between server to server in regards to how many security officer slots you tend to have on spawn, but this is already manageable by the security officer co-efficient in config.

I believe this PR is an acceptable proposal within the bounds of #68527 (comment) , although it may bend certain aspects of it, I definitely do see where some people may be coming from. I believe I've adjusted the accesses to a "sane"/justifiable amount, but I'll come back to think on everything.

"Red-tiding" may or may not be a problem, but there's always just going to be something inherently silly with a security officer being able to walk into plumbing to start plumbing. I hoped that this would be seen as a positive as opposed to a negative, but I can see how it could negatively impact player experience. HOWEVER, interplayer experience should not be handled by the codebase in all aspects, which is why I've also passed in the associated config variables, so that server operators (who should handle the interplayer experience with their level of discretion and nuance) can.
What accesses are where?

The general philosophy as I thought through designing this would be that the security officer should at the very least have general "front-door" access into a department, and maybe something benign. If we had even more per-door accesses, this could definitely be a bit more granular (one example I can think of would only atmospherics technicians having access to the "Pump Room", while Security Officers would not. However, this is for a later date). So, you have the "default" access you always get, and a potential to get "elevated" access as a Departmental Security Officer.

The balances are as such:

The Cargo Security Officer will have access to the Cargo Bay, Mining Section, and the Shipping Room. The first two are rather general areas, with the Shipping Room being a rather good help for rescuing (or "rescuing") flushed crewmembers when the cargo techies can't get to it/no AI. The Auxiliary Base is not essential to the security officer's functions, and the mining station helps restrict access further on stations like IceBox. This would also grant them extra access to the Lavaland base, so let's snip that out.

The Engineering Security Officer should have access to only general Engineering and Atmospherics. Construction pertains to certain rooms in maintenance I believe, and Engine-Equipment should be the one that grants access to APCs (lol). I don't think a security officer should have the latter one to be honest, but I think we'll be stretching the scope of this PR. Telecommunications is a bit weird, it's a critical station function, but I think you also shouldn't be able to nick one goon's ID and have access, so let's give it to them only when it's "needed".

The Medical Security Officer should have access to only the general Medbay Area and the Morgue, in case someone starts trotting on the doctor's turf, or if there's someone doing unsavory things to the bodies while the doctors are away. They will not have access to the specialized (dangerous) areas unless the ratio of secoffs to the population is low enough should it necessitate it (Plumbing Room, Pharmacy, Virology). I also added Surgery to the scaling access, but I'm iffy on that one. I don't particularly see why they should have it as a base access, but I also do see there being some need in dire straits (in relation to helping people, not tiding).

The Science Security Officer definitely got a huge cut. They now only have general access to R&D and normal scientist areas like the lathe room, circuits lab (presumably)since these are generally trafficked areas, but I definitely clamped down on additional access they might get in a "normally balanced" situation (no ordnance+storage, no xenobio, no genetics, no to robotics, etc.) They don't have a particular use in these areas and can even be a bit obstructive to flow in normal circumstances, but if abnormal circumstances arise and there's not a lot of security hands-on-deck, then their access is expanded.

Honestly, balancing this both makes sense and is conversely rather odd. I'm just running off what we already hold to be true and expected (or at least as of the last two months), and we can go from there.
Changelog

cl
balance: Nanotrasen realized that the more access they had on their cards was costing them a pretty penny, so they trimmed back the number of accesses a certain departmental Security Guard might have. However, any given guard will get back a greater amount of accesses depending on how many security guards there are in relation to the population.
config: Hey server operators, listen! We've changed up how Departmental Security Officers get their accesses, so be sure to review the DEPSEC_ACCESS_LEVEL config number to see what you want to work best for your server.
/cl

Also, every single line of code found in 4533f07 that is now presently in this PR is deliberate

---
## [csomervil/Sand-Kingdom](https://github.com/csomervil/Sand-Kingdom)@[83fdefcdd7...](https://github.com/csomervil/Sand-Kingdom/commit/83fdefcdd7e57b92fb97aae6ef06b6792c887a1d)
#### Saturday 2022-08-27 03:26:31 by csomervil

Added leather

I added leather and different leather types for each of the scorpions. They should all be recipes for apparel. The armor quality goes as follows: zealot = shifter = pikeman < support < king. I also added a custom weapon for the pikemen instead of using the Neolithic pike weapon (still needs art). HOWEVER, I did find (and implement) fundamentals for abilities I want to create. Currently I am taking from the vanilla core files the ability to summon tornados and fire projectiles from melee weapons. I had no idea doing this was so easy and I how to make custom animations/different abilities. Currently the projectiles fired from the spears have a wind sound already used in the game (it is kind of weird). I have not addressed any of the problems in my last TODO, but I do now have more realistic goals (I think/hope). I did take a look at Nudism and to be honest I do not that think that the game allows for it like it says it does (or at least doesn't display). I have been trying to solve Nudism for a while, but I am uncertain as to weather I need Rimworld Ideology (as I think stated in the files) or maybe some other knock off/cheesy method.

TODO (similar to last time):
Fix Nudism, balance (raid points), models (for weapons too), custom poisons (king's), and I think that is it (maybe more units maybe one with new projectiles).
Add faction icons <- BIG FOR DISPLAY ERROR, be wary of aeo. DO TESTING. 
Add new projectiles (please be easy).

---
## [RonyAgentSpp/website3](https://github.com/RonyAgentSpp/website3)@[d53911b41a...](https://github.com/RonyAgentSpp/website3/commit/d53911b41a0a6008b6244b4ed5d210fd48fac8cd)
#### Saturday 2022-08-27 03:44:06 by RONALDO LIMA/RONY INSIDE CODE

Website 3 Portifolio

Agradecimentos especiais em todos que acreditam e podem me ajudar com feed-back, dicas e sugestões.
Have a nice night, may God Bless you!

---
## [ammarfaizi2/linux-fork](https://github.com/ammarfaizi2/linux-fork)@[17ba9d9409...](https://github.com/ammarfaizi2/linux-fork/commit/17ba9d94093bd007a63a59175a6be908f3418bea)
#### Saturday 2022-08-27 05:16:06 by Johannes Weiner

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
## [haze/zig](https://github.com/haze/zig)@[a31b449b55...](https://github.com/haze/zig/commit/a31b449b55c32eba1cb61a48753a6fc98696c98f)
#### Saturday 2022-08-27 06:42:37 by Andrew Kelley

make LLVM and Clang emit DWARF 4 instead of 5

This reverts 6d679eb2bcbe76e389c02e0bb4d4c4feb2847783 and additionally
changes the command line parameters passed to Clang to match.

Clang 14 defaults to DWARFv5 which is an interesting choice. v5 has been
out for 5 years and yet Valgrind does not support it, and apparently
neither does either GDB or LLD, I haven't determined which, but I wasn't
able to use GDB to debug my LLVM-emitted dwarf 5 zig code that was linked
with LLD.

A couple years ago when I was working on the self-hosted ELF linker, I
emitted DWARFv5 but then downgraded to v4 when I realized that third
party tools were stuck in the past. Years later, they still are.

Hopefully, Clang 14's bold move will inspire third party tools to get
their shit together, however, in the meantime, everything's broken, so
we're passing `-gdwarf-4` to clang and instructing LLVM to emit DWARFv4.

Note that Zig's std.debug code *does* support DWARFv5 already as of a
previous commit that I made today.

---
## [TrashDoxx/TG](https://github.com/TrashDoxx/TG)@[6f2354e694...](https://github.com/TrashDoxx/TG/commit/6f2354e694f3412a76b383f684a0bfc85a448d8e)
#### Saturday 2022-08-27 06:59:05 by san7890

Fixes Fucked Job Requirement Displays (#69368)

* Fixes Fucked Job Requirement Displays

Hey there,

I fucked up in #68856 (5b77361d399ba0dd992e61a16b9bbe38e8aa5a60). We weren't supposed to add another MINUTES multiplication here. I don't even remember why I did this if we are being perfectly honest with each other. Whoops.

fix: You should now no longer need thousands of hours to unlock your favorite head of staff role.

---
## [ggevay/materialize](https://github.com/ggevay/materialize)@[305082a6a9...](https://github.com/ggevay/materialize/commit/305082a6a99ee063839975c86bd1e821a2af0e23)
#### Saturday 2022-08-27 09:53:36 by Daniel Harrison

persist: commit state updates to durable storage incrementally

Before, there was pressure to keep the size of state down, because it
was rewritten entirely on each command application. In particular, this
created a tension in compaction tuning between being aggressive about
fewer batches (smaller state) and compacting small batches lazily
(smaller write amplification).

Writing state updates as incremental diffs means that size of a
Consensus writes for each command is independent of the total size of
state. We should be able leverage this to make the entire
`WriteHandle::compare_and_append_batch` latency constant w.r.t. the size
of state and thus independent of compaction. This lets us tune
compaction entirely for where we want to be in its more intrinsic
tradeoff between read, write, and space amplification.

(NB: This commit doesn't quite get us to constant latencies, there's
some elbow grease left. I've proven concretely that it can get down to
`O(log(num state batches))`, but that included some hacks that didn't
make this PR. This would be lovely followup work once we get a chance.)

As persist metadata changes over time, we make its versions (each
identified by a [SeqNo]) durable in two ways:
- `rollups`: Periodic copies of the entirety of [State], written to
  [Blob].
- `diffs`: Incremental [StateDiff]s, written to [Consensus]. The
following invariants are maintained at all times:
- A shard is initialized iff there is at least one version of it in
  Consensus.
- The first version of state is written to `SeqNo(1)`. Each successive
  state version is assigned its predecessor's SeqNo +1.
- `current`: The latest version of state. By definition, the largest
  SeqNo present in Consensus.
- As state changes over time, we keep a range of consecutive versions
  available. These are periodically `truncated` to prune old versions
  that are no longer necessary.
- `earliest`: The first version of state that it is possible to
  reconstruct.
  - Invariant: `earliest <= current.seqno_since()` (we don't garbage
    collect versions still being used by some reader).
  - Invariant: `earliest` is always the smallest Seqno present in
    Consensus.
    - This doesn't have to be true, but we select to enforce it.
    - Because the data stored at that smallest Seqno is an incremental
      diff, to make this invariant work, there needs to be a rollup at
      either `earliest-1` or `earliest`. We choose `earliest` because it
      seems to make the code easier to reason about in practice.
    - A consequence of the above is when we garbage collect old versions
      of state, we're only free to truncate ones that are `<` the latest
      rollup that is `<= current.seqno_since`.
- `live diffs`: The set of SeqNos present in Consensus at any given
  time.
- `live states`: The range of state versions that it is possible to
  reconstruct: `[earliest,current]`.
  - Because of earliest and current invariants above, the range of `live
    diffs` and `live states` are the same.
- The set of known rollups are tracked in the shard state itself.
  - For efficiency of common operations, the most recent rollup's Blob
    key is always denormalized in each StateDiff written to Consensus.
    (As described above, there is always a rollup at earliest, so we're
    guaranteed that there is always at least one live rollup.)
  - Invariant: The rollups in `current` exist in Blob.
    - A consequence is that, if a rollup in a state you believe is
      `current` doesn't exist, it's a guarantee that `current` has
      changed (or it's a bug).
  - Any rollup at a version `< earliest-1` is useless (we've lost the
    incremental diffs between it and the live states). GC is tasked with
    deleting these rollups from Blob before truncating diffs from
    Consensus. Thus, any rollup at a seqno < earliest can be considered
    "leaked" and deleted by the leaked blob detector.
  - Note that this means, while `current`'s rollups exist, it will be
    common for other live states to reference rollups that no longer
    exist.

---
## [rust-adventure/first-rust-cli](https://github.com/rust-adventure/first-rust-cli)@[c9219275ef...](https://github.com/rust-adventure/first-rust-cli/commit/c9219275ef915950d327ebf28ffad7550ab1d3f7)
#### Saturday 2022-08-27 10:48:15 by Christopher Biscardi

Borrowing

\## Intro

In this lesson we're going to learn how to share references to the data in our variables instead of copying the data.

```rust
❯ cargo run post rust,bevy "Doing shader stuff in Bevy" doing-shader-stuff-in-bevy.md
   Compiling first v0.1.0 (/rust-adventure/first-cli)
    Finished dev [unoptimized + debuginfo] target(s) in 0.18s
     Running `target/debug/first post rust,bevy 'Doing shader stuff in Bevy' doing-shader-stuff-in-bevy.md`
[src/main.rs:5] &args = [
    "target/debug/first",
    "post",
    "rust,bevy",
    "Doing shader stuff in Bevy",
    "doing-shader-stuff-in-bevy.md",
]
[src/main.rs:12] layout = "post"
[src/main.rs:12] tags = "rust,bevy"
[src/main.rs:12] heading = "Doing shader stuff in Bevy"
[src/main.rs:12] filename = "doing-shader-stuff-in-bevy.md"
```

\## The Code

We're going to end up with this code.

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    dbg!(&args);

    let layout = &args[1];
    let tags = &args[2];
    let heading = &args[3];
    let filename = &args[4];

    dbg!(layout, tags, heading, filename);
}
```

\## Borrowing

In the case of our CLI, cloning works just fine: the extra copies of data don't matter from a performance perspective.

<aside>
⚠️ Sidenote: If you're planning to do performance work *always* profile your application, *then* test your changes, then profile again. Don't rely on guesses.

</aside>

Instead I want to introduce the concept of borrowing as a way to convey information about your program *and* have the Rust compiler enforce that information.

You can imagine that the implementation of `dbg!`, for example, isn't going to need to mutate the value we give it. It's going to print the data to the console, not append characters to the string.

Similarly, our argument variables don't need to own their data. They can use read-only access to the data we already have stored in `args`.

\## Shared References

Using shared references, we can explicitly state that the places we're using the data are only going to read the data and not mutate it.

This means that we can have as many shared references to the original `Vec` as we want since every usage can read the data without worrying about what the rest of our program is doing.

Everywhere we used `.clone()`, we can replace that usage with `&` before the value.

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    dbg!(&args);

    let layout = &args[1];
    let tags = &args[2];
    let heading = &args[3];
    let filename = &args[4];

    dbg!(layout, tags, heading, filename);
}
```

`&` is how we create shared references to the original data instead of creating copies of it.

`dbg!` gets a shared reference to the entire `Vec` of `String`s.

`layout`, `tags`, `heading`, and `filename` all get shared references to a specific `String` at an index in the `Vec`.

\## When to clone and when to borrow?

In general, you should clone data when you want copies of it and borrow data when you want to share access to some data.

In practice knowing when you need to clone and when it makes sense to borrow is something that will take writing code in different situations.

If you run into trouble, you can often get away with using .clone to get you out of a jam if you're feeling overwhelmed by the compiler feedback.

---
## [rust-adventure/first-rust-cli](https://github.com/rust-adventure/first-rust-cli)@[2695fa6b30...](https://github.com/rust-adventure/first-rust-cli/commit/2695fa6b300cb4d685a9761e1c3a4b0df4b0c8b3)
#### Saturday 2022-08-27 10:48:15 by Christopher Biscardi

when in doubt, clone it

\## Intro

In this lesson we're going to learn how to access the individual arguments that we collected in the last lesson. When we run the program, we'll be able to print out each argument individually.

```rust
❯ cargo run post rust,bevy "Doing shader stuff in Bevy" doing-shader-stuff-in-bevy.md
    Finished dev [unoptimized + debuginfo] target(s) in 0.00s
     Running `target/debug/first post rust,bevy 'Doing shader stuff in Bevy' doing-shader-stuff-in-bevy.md`
[src/main.rs:13] layout = "post"
[src/main.rs:13] tags = "rust,bevy"
[src/main.rs:13] heading = "Doing shader stuff in Bevy"
[src/main.rs:13] filename = "doing-shader-stuff-in-bevy.md"
```

\## The Code

We're going to end up with this code and on the way we'll work our way through Ownership.

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    let layout = args[1].clone();
    let tags = args[2].clone();
    let heading = args[3].clone();
    let filename = args[4].clone();

    dbg!(layout, tags, heading, filename);
}
```

\## Arguments

When we run our program we can pass any number of arguments to it.

```rust
❯ cargo run 1 2 3 4
   Compiling first v0.1.0 (/rust-adventure/first-cli)
    Finished dev [unoptimized + debuginfo] target(s) in 0.18s
     Running `target/debug/first 1 2 3 4`
[src/main.rs:5] args = [
    "target/debug/first",
    "1",
    "2",
    "3",
    "4",
]
```

Each of the arguments we pass in comes in order after the name of the program we're running.

We can associate the position of each argument with a meaning. To do that we have to decide what kind of file we're scaffolding.

For the workshop we'll build out a markdown file scaffolding tool, like we were writing a blog post.

First we need to decide what each position will mean.

The first argument will be the post layout, for example a “post” or an image “gallery”.

The second will be a list of tags, like “rust,bevy”.

The third will be the heading of our blog post.

and the fourth will be the file we write the template out to.

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    dbg!(args);

    let layout = args[1];
    let tags = args[2];
    let heading = args[3];
    let filename = args[4];

    dbg!(layout, tags, heading, filename);
}
```

We'll also add a `dbg!` macro to print out each variable to the console.

We've set up the arguments to be accessed by index, much like would be familiar in another programming language, but if we run the program it won't compile.

```rust
❯ cargo run 1 2 3 4
   Compiling first v0.1.0 (/rust-adventure/first-cli)
error[E0382]: borrow of moved value: `args`
 --> src/main.rs:7:18
  |
4 |     let args: Vec<String> = env::args().collect();
  |         ---- move occurs because `args` has type `Vec<String>`, which does not implement the `Copy` trait
5 |     dbg!(args);
  |     ---------- value moved here
6 |
7 |     let layout = args[1];
  |                  ^^^^ value borrowed here after move
```

This is where we first encounter Ownership and Borrowing, one of the defining features of the Rust language.

Every value in Rust has an owner and there can be only one owner at a time. Rust enforces this rule for us, which means we have one less piece of context to “just remember” when we write our programs.

In our case, the variable `args` owns the Vec of Strings that contains our arguments.

When we pass the `args` variable to `dbg!`, we're giving up ownership of the value to the `dbg!` macro. Rust calls this moving, or a `move`.

That gives us enough information to read the error message, or at least half of it.

The value in `args` is moved when we call `dbg!`. Moving a value means we no longer have access to it after that point, but we try to access it again later when we index into it with `args[1]`.

\## Cloning

We have two solutions to this problem

1. we can create more copies of the arguments value to pass around
2. we can share the access to the original arguments value

In our case, both of these solutions work and both are about the same amount of code.

First we'll creating more copies. This is often the method that matches what happens in other programming languages.

The method we use to create more copies is called `clone`.

```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    dbg!(args.clone());

    let layout = args[1].clone();
    let tags = args[2].clone();
    let heading = args[3].clone();
    let filename = args[4].clone();

    dbg!(layout, tags, heading, filename);
}
```

First we'll create a copy of the whole `Vec`, including the Strings to pass to `dbg!`.

Then we'll clone each of the individual values in the `Vec` as well when we access them by index.

Now we can compile and run our program.

```rust
❯ cargo run 1 2 3 4
   Compiling first v0.1.0 (/rust-adventure/first-cli)
    Finished dev [unoptimized + debuginfo] target(s) in 0.20s
     Running `target/debug/first 1 2 3 4`
[src/main.rs:5] args.clone() = [
    "target/debug/first",
    "1",
    "2",
    "3",
    "4",
]
[src/main.rs:12] layout = "1"
[src/main.rs:12] tags = "2"
[src/main.rs:12] heading = "3"
[src/main.rs:12] filename = "4"
```

When you're just starting out, cloning is the easiest way around what you'll think of as “ownership and borrowing issues” and even after you gain more expertise in Rust, cloning will still be an important tool in your toolbox.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[95a67f0bbc...](https://github.com/mrakgr/The-Spiral-Language/commit/95a67f0bbc247bb9b46d99293745035089415f89)
#### Saturday 2022-08-27 11:02:55 by Marko Grdinić

"9:40am. https://comikey.com/read/thank-you-isekai-manga/eglWVo/chapter-19/

Let me finish reading this and I will get started. I got up 20m ago.

10:05am. There is really nothing good on /lit/.

Let me start writing.

10:15am. I've been thinking what I should write in my author's note.

10:20am. Instead of thinking about that I should focus on the story itself. Sigh, I am just so wounded right now. I am a shell of a my former self.

But let me highlight something. Currently, in the dashboards I see my total views are at 159 and my average views are at 26.

I am not sure by how much, but it was less yesterday. So even if I am still at 2 followers, I think as long as the view counts go up, and I get regular readers, I'll be able to convert those into follows and patrons.

10:25am. 300 pages by the end of the next month! More total views!

As long as I keep writing the total views will go up. It is a form of currency itself.

I should just think of those 160 view as 160$ and keep going. The total views can only go up.

10:30am. Enough rambling, let me see if I can go over what I wrote yesterday and make it less crazy. Then I will do the legendary street crossing scene.

$$$

(Helix Studio, Regent Suite, Bedroom)

"Ahhhhh!" With a scream, I eject myself from the game, and into the safe space.

"Hah, hah, hah!" I breathe heavily. After I catch my bearings, I slurp my saliva down my throat and wipe the droll with my sleeve.

I can't believe it, right now I am still trembling all over! Real death, unexpected death is traumatic!

"Hah, hah, hah..."  It takes me a while to calm down. Right now I am in my bedroom in the cruise, lying on the king sized bed. After a while my shivers susbside and I start to gather my thoughts.

I admit this caught me by surprise, I didn't think that somebody would pull a gun on me. I have a week of experience in the game by now, so I know that what he did should be impossible. While it is easy to create manifestations in the city itself, in the dueling realms, I've tried it, and found it impossible to create even the simplest things. Whatever system is reading my thoughts and manifesting my projections does not work when the chips are down. Otherwise why would anybody play poker to begin with? Call, fold, raise? Just shot the other guy. Bang!

What the white haired guy did was quite amazing. Right now, I have no way of countering it. If I could make my own gun, I could try getting the jump on him, or maybe if I could make a shield, I could protect myself. But that is not possible.

What he did in the street would not be too hard, I'd have to study the structure of a gun for a while and practice manifesting it. This would be easy in this virtual space. You can't actually hurt anybody in this city directly. If I tried attacking anybody on the street, with a gun, fist or anything else, that would initiate a resolution match. Mickey told me about it.

I am not sure what I should do right now.

I get off the bed and stretch my body. Now that I've gotten over the shakes, I realize that I need a bath and a meal, in that order.

I know where the bathroom is already, so I make my way there. Opulence, luxury, I really envy the rich people who can experience this in real life. Everything in the bathroom looks like it costs at least 100k dollars. At home I just take showers, but here I do that and then a nice long break in the tub. It is a new experience for me, so I try experimenting with all the shampos and bathing soaps that I've never seen before.

Refreshed and relaxed, I go into the kitchen and get some food. In the mega-fridge there are all sorts of meals and drinks. I go for some pasta and salsa. When I pick up the item I get a window asking me:

> Do you want to the system to warm up the meal for you? Yes/No.

I mentally confirm it, and the meal transforms into a freshly cooked one. I take out some cutlery from one of the drawers, put the meals and it on a tray, and have a meal alone in the living room. The world is bright and sunny outside, and my only company is the murmur of waves.

Afterwards, I note the living room has a bar so I get drunk and spend a few hours lounging on the sofa. I waste some time watching anime on TV. Wonderful.

A part of me wishes I could stay there forever.

...

I remember the gunshot, and it spoils my mood.

[Pathos check DC 2 Failed - Sampled 1.52]

But I do not feel like doing anything about that guy. Why would I want to leap right back into the fray? I leave Heaven's Key aside from my mind, and just have some fun on the cruise. I think about my experiences in the game itself and a wave of lethargy assaults me. I spend a week there just grinding chips, but in the end what has that gotten me?

I could have gotten a million chips and it still would not have given me any benefits in real life. Just what was the point of all that effort? There isn't as far as I can see. It taught me a little bit of live poker, but what am I going to use that for? Nothing really. I am certainly not good enough to start grinding for real money online.

I put in a week of effort into it, and so like that I spend a week relaxing on the cruise.

It was a long time for me, but only a minute passes in the real world.

(Helix Studio, Regent Suite, Brow of the ship)

The cruise is huge, and I had time to adventure and explore it. Nobody is here, but me. I had the time so I checked the rooms one by one when I had free time from gaming. They were all neatly aranged, and they all belonged to me. At the end of the week, I started to feel pangs of loneliness.

[Externus check DC 2 Succeeded - Sampled 4.1]

But it was not because there aren't any people here. Neither do I miss my parents. Loneliness is caused by only one thing - lack of power.

Power, huh? As I wander through the ship without direction, I come to the brow. I go up to the railing and sit myself below it, dangling my feet over the ledge. I gaze at the waters below.

The thought that comes to mind, is hardship. It is so difficult. I think about my life since I uploaded myself, and contrast that with some of the recent gaming sessions.

I was playing an RPG. In there controlling the characters is so easy. They can go into battle after difficult battle without complaint, with seemingly endless capacity for work. It is not that they are robots, it is that they have somebody controling and guiding their actions from beyond.

I think about it. How would being a character in a computer RPG or a tabletop game be?

I'd have my own thoughts and feelings. I wouldn't realize that I am being guided by some force entity beyond. Whatever system that entity would be using would not feel tacked on. It would feel like...

I think about it. And the world to describe it perfectly comes to me - natural.

I realize the truth at that point. People think they have free will, but ultimately they are just acting based on their instincts. Ultimately, somebody designed their emotional system and they will act according to it, for better or for worse. There is no guarantee that their feelings will guide them to the correct solution, anymore that a bad player can win the game on the first game without dying.

I look at my hands and realize that this is all my determination amounts to. I wanted superpowers. I knew that it would be hard to get them. I started playing Simulacrum as per plan and made good progress thanks to my cheating. Then somebody put his boot up my ass, and I am so distraught that I stopped playing it for an entire week.

If somebody was playing me, and I was an RPG character, he would never let that happen. He would just reload and get me back into the fray.

The reason this is happening is because the responsibility for the task I set out to do is too great. I ran into difficulty, and my great plan collapsed, drowned in a wave of emotion. A melancholic feel comes over me as I look at the waves below. I am somehow reminded of that time I hurled myself from the rim of the city.

I remember falling and recall the feeling. I recall that how once I threw myself, just before I hit I wanted myself to stop falling. It was a swirl of emotions without end in sight.

Suppose back then I used the mind control app to normalize my mental state, I would be calm throughout. But if I extrapolated such an attitude to my whole life, I'd live a very dull if calm life. The ability to accept anything and be happy about anything is a dangerous thing. If I can accept anything, why not become a normie and treat the well traveled path? Because I know that their path does not lead to power.

The main problem is that I broke under pressure. It is not like studying a textbook. I simply do not have the ability to do surgery on myself in the middle of a fight. It is normal to get heated in battle. Use the core to get rid of fear, and you get comfortable with getting hit. A graceful loser is still a loser. I do not need pride, but I need victory.

Victory should come over everything. Does it really matter how it is accomplished? I need to win the game, but does it really matter that I be the character in the game?

In a moment of clarity, I remember the character sheet of the character in the game I was playing. And I see the game being played from perspective of tens and hundreds of thousands of other players. And I realize that every single one of them of them is looking at themselves from the perspective of the character. But the characters are nothing. They are meant to be broken and tossed away. The true power lies in being a player. It is hard to realize this, because they themselves are players.

It would be weird to dream about being a player of a game, when you are already doing that.

But that is what I must dream about. I must aim to be a player.

In life, everyone wants to be a characters with high base stats. People live their life, and when they lose they blame themselves. If life was truly a game, the one to take responsibility for victory and defeat should be the one controlling them from beyond - the player. By that reasoning, since humans are controlled by nature, the one who should take credit for that is nature itself. But nature is a brainless and non-adaptive. It doesn't care about the goals of the characters. It doesn't care about its own responsibility as a player. It can't take responsibility, so it has to fall on the character itself.

Being controlled by nature is unjust.

With such a player, if I go into the game, of course I am going to get an anal expansion as soon as I inevitably run into somebody better. It is my responsibility to see that the justice is done.

I get up and clench my fist decisively.

I will go beyond and become my own player. This more than just winning a game. It is about playing it properly.

(Heaven's Key, Regent Suite, Bedroom)

I have no confidence of being able to beat the white haired guy. But that doesn't matter, I am not going to be fighting him as a character inside the game, but as a player.

But before that, instead of having to bear the computational burden of the Simulacrum game, if I did some simpler simulations, I could get a lot more training done in the same amount of time that if I played the game directly. I've read that the notion of training on simulated games is the most powerful idea in machine learning, but to make it work it is best to follow a curriculum. Little kids learn arithmetic before they move on to algebra. I must learn to walk before I can run, in this case literally.

I'll ignore the challenge waiting for me in Heaven's Key, and conquer the very first challenge that all Inspired must do which is adapt to using the full computational power of the core.

Right now, I can only run my own simulation at the same rate as the outerlying environment. Even small increases of computational speed gives me great difficulty in moving. Let me not waste anymore time tackling this, I am going to deal with this first.

$$$

12:40pm. Done with lunch. I am not really blocked even though I haven't writen much. I am not even distracted. It is just that the topic of the self improvement loop is sensitive to me, and revisiting it after over half a decade of programming and ML. I can't help, but feel both deep sadness and longing as I think about it.

1pm. Let me take a nap. I do not feel like writing right now."

---
## [petre-symfony/symfony-6-fundamentals-services-config-and-environments](https://github.com/petre-symfony/symfony-6-fundamentals-services-config-and-environments)@[78f2d6a678...](https://github.com/petre-symfony/symfony-6-fundamentals-services-config-and-environments/commit/78f2d6a678ab95184ddaf21bf7a00a8a69d0972a)
#### Saturday 2022-08-27 11:35:52 by petrero

9 Environments

  Our application is like a machine: it's a set of services and PHP classes that do work... and ultimately render some pages. But we can make our machine work differently by feeding it different configuration.

  For example, in SongController, we're using the  service to log some information:

 30 lines  src/Controller/SongController.php
  class SongController extends AbstractController
  {
    #[Route('/api/songs/{id<\d+>}', methods: ['GET'], name: 'api_songs_get_one')]
    public function getSong(int $id, LoggerInterface $logger): Response
    {
    }
  }
  If we feed the logger some configuration that says "log everything", it will log everything, including low level debug messages. But if we change the config to say "only log errors", then this will only log errors. In other words, the same machine can behave differently based on our configuration. And sometimes, like with logging, we might need that configuration to be different while we're developing locally versus on production.

  To handle this, Symfony has an important concept called "environments". I don't mean environments like local vs staging vs beta vs production. A Symfony environment is a set of configuration.

  For example, you can run your code in the dev environment with a set of config that's designed for development. Or you can run your app in the prod environment with a set of config that's optimized for production. Let me show you!

  The APP_ENV Variable
  - In the root of our project, we have a .env file:

 20 lines  .env
  # In all environments, the following files are loaded if they exist,
  # the latter taking precedence over the former:
  #
  #  * .env                contains default values for the environment variables needed by the app
  #  * .env.local          uncommitted file with local overrides
  #  * .env.       committed environment-specific defaults
  #  * .env..local uncommitted environment-specific overrides
  #
  # Real environment variables win over .env files.
  #
  # DO NOT DEFINE PRODUCTION SECRETS IN THIS FILE NOR IN ANY OTHER COMMITTED FILES.
  #
  # Run "composer dump-env prod" to compile .env files for production use (requires symfony/flex >=1.2).
  # https://symfony.com/doc/current/best_practices.html#use-environment-variables-for-infrastructure-configuration
  ###> symfony/framework-bundle ###
  APP_ENV=dev
  APP_SECRET=4777a99cd6c61ce84969bd1338737c38
  ###
  We're going to talk more about this file later. But see this APP_ENV=dev? This tells Symfony that the current environment is dev, which is perfect for local development. When we deploy to production, we'll change this to prod. More on that in a few minutes.

  But... what difference does that make? What happens in our app when we change this from dev to prod? To answer, let me close some folders... and open public/index.php:

  10 lines  public/index.php
  <?php
  use App\Kernel;
  require_once dirname(__DIR__).'/vendor/autoload_runtime.php';
  return function (array $context) {
    return new Kernel($context['APP_ENV'], (bool) $context['APP_DEBUG']);
  };
  Remember: this is our front controller. It's the first file that's executed on every request. We don't really care much about this file, but its job is important: it boots up Symfony.

  What's interesting is that it reads the APP_ENV value and passes it as the first argument to this Kernel class. And... this Kernel class is actually in our code! It lives at src/Kernel.php.

  Cool. So what I want to know now is: What does the first argument to Kernel control?

  If we open the class we find... absolutely nothing. It's empty. That's because the majority of the logic lives in this trait. Hold "cmd" or "control" and click MicroKernelTrait to open that up.

  The config/packages/{ENV} Directory
  The job of the Kernel is to load all of the services and routes in our app. If you scroll down, it has a method called configureContainer(). Ooh! We know what the container is now! And check out what it does! It takes this $container object and imports $configDir.'/{packages}/*.{php,yaml}'. This line says:

    Yo container! I want to load all of the files from the config/packages/ directory.

  It loads all of those files, and then it passes the configuration from each to whatever bundle is defined as the root key. But what's really interesting for environments is this next line: import $configDir.'/{packages}/'.$this->environment.'/*.{php,yaml}'. If you dug a little, you'd learn that $this->environment is equal to the first argument that's passed to Kernel!

  In other words, in the dev environment, this will be dev. So, in addition to the main config files, this will also load anything in the config/packages/dev/ directory. Yup, we can add extra config there that overrides the main configuration in the dev environment. For example, we could add logging config that tells the logger to log everything!

  Below this, we also load a file called services.yaml and, if we have it, services_dev.yaml. We'll talk more about services.yaml real soon.

  The when@{ENV} Config
  - So, if you want to add environment-specific configuration, you can put it in the correct environment directory. But there's one other way. It's a pretty new feature and we saw it at the bottom of twig.yaml. It's the when@ syntax:

  7 lines  config/packages/twig.yaml
  when@test:
    twig:
        strict_variables: true
  In Symfony, by default, there are three environments: dev, prod, and then if you run automated tests, there's an environment called test. Inside of twig.yaml, by saying, when@test, it means that this configuration will only be loaded if the environment is equal to test.

  The best example of this might be in monolog.yaml. monolog is the bundle that controls the logger service. It does have some configuration that's used in all environments. But, below this, it has when@dev. We won't talk too much about the specific monolog configuration, but this controls how log messages are handled. In the dev environment, this says that it should log everything and it should log to a file, using this fancy %kernel.logs_dir% syntax that we'll learn about soon.

  Anyways, this points to a var/logs/dev.log file and the level: debug part means that it will log every single message to dev.log... regardless of how important or unimportant that message is.

  Below this, for the prod environment, it's quite different. The most important line is action_level: error. That says:

  Hi Ms Logger! This app probably logs a ton of messages, but I only want you to actually save messages that are an error importance level or higher.

  That makes sense! In production, we don't want our log files filling up with tons and tons of debug messages. With this, we only log error messages.

  The big point is this: by using these tricks, we can configure our services differently based on the environment.

  Environment-Specific Routing
  - And, we can even do the same thing with routes! Sometimes you have entire routes that you only want to load in a certain environment. Back in MicroKernelTrait, if you go down, there's a method called configureRoutes(). This is what's responsible for loading all of our routes... and it's very similar to the other code. It loads $configDir.'/{routes}/*.{php,yaml}' as well as this dev environment directory, if you have one. We don't.

  You can also use the when@dev trick. This file is responsible for registering the routes used by the web debug toolbar. We don't want the web debug toolbar in production... so these routes are only imported in the dev environment.

  9 lines  config/routes/web_profiler.yaml
  when@dev:
    web_profiler_wdt:
        resource: '@WebProfilerBundle/Resources/config/routing/wdt.xml'
        prefix: /_wdt
    web_profiler_profiler:
        resource: '@WebProfilerBundle/Resources/config/routing/profiler.xml'
        prefix: /_profiler
  Heck, certain bundles are only enabled in some environments! If you open config/bundles.php, we have the name of the bundle... and then on the right, the environments in which that bundle should be enabled. This all means all environments.... and most are enabled in all environments.

  The WebProfilerBundle however - the bundle that gives us the web debug toolbar and profiler - is only loaded in the dev and test environments. Yup, the entire bundle - and the services it provides - are never loaded in the prod environment.

  So, now that we understand the basics of environments, let's see if we can switch our application to the prod environment. And then, as a challenge, we'll configure our cache service differently in dev. That's next.

---
## [petre-symfony/symfony-6-fundamentals-services-config-and-environments](https://github.com/petre-symfony/symfony-6-fundamentals-services-config-and-environments)@[28e3623b92...](https://github.com/petre-symfony/symfony-6-fundamentals-services-config-and-environments/commit/28e3623b923ddd5d3487c02a3e67f601f16adce7)
#### Saturday 2022-08-27 11:35:52 by petrero

11.1 Creating a Service

  We know that bundles give us services and services do work. Ok. But what if we need to write our own custom code that does work? Should we... put that into our own service class? Absolutely! And it's a great way to organize your code.

  We are already doing some work in our app. In the browse() action we make an HTTP request and cache the result. Putting this logic in our controller is fine. But by moving it into its own service class, it'll make the purpose of the code more clear, allow us to reuse it from multiple places... and even enable us to unit test that code if we want to.

  Creating the Service Class
  - That sounds amazing, so let's do it! How do we create a service? In the src/ directory, create a new PHP class wherever you want. It seriously doesn't matter what directories or subdirectories you create in src/: do whatever feels good for you.

  For this example, I'll create a Service/ directory - though again, you could call that PizzaParty or Repository - and inside of that, a new PHP class. Let's call it... how about MixRepository. "Repository" is a pretty common name for a service that returns data. Notice that when I create this, PhpStorm automatically adds the correct namespace. It doesn't matter how we organize our classes inside of src/... as long as our namespace matches the directory

  One important thing about service classes: they have nothing to do with Symfony. Our controller class is a Symfony concept. But MixRepository is a class we're creating to organize our own code. That means... there are no rules! We don't need to extend a base class or implement an interface. We can make this class look and feel however we want. The power!

  With that in mind, let's create a new public function called, how about, findAll() that will return an array of all of the mixes in our system. Back in VinylController, copy all of the logic that fetches the mixes and paste that here

  PhpStorm will ask if we want to add a use statement for the CacheItemInterface. We totally do! Then, instead of creating a $mixes variable, just return

  There are some undefined variables in this class... and those will be a problem. But ignore them for a minute: I first want to see if we can use our shiny new MixRepository.

  Is our Service already in the Container?
  - Head into VinylController. Let's think: we somehow need to tell Symfony's service container about our new service so that we can then autowire it in the same way we're autowiring core services like HtttpClientInterface and CacheInterface.

  Whelp, I have a surprise! Spin over to your terminal and run:

    php bin/console debug:autowiring --all
  Scroll up to the top and... amaze! MixRepository is already a service in the container! Let me explain two things here. First, the --all flag is not that important. It basically tells this command to show you the core services like $httpClient and $cache, plus our own services like MixRepository.

  Second, the container... somehow already saw our repository class and recognized it as a service. We'll learn how that happened in a few minutes... but for now, it's enough to know that our new MixRepository is already inside the container and its service id is the full class name. That means we can autowire it!

---
## [petre-symfony/symfony-6-fundamentals-services-config-and-environments](https://github.com/petre-symfony/symfony-6-fundamentals-services-config-and-environments)@[f7ce9dc1d4...](https://github.com/petre-symfony/symfony-6-fundamentals-services-config-and-environments/commit/f7ce9dc1d4df672c026fb03c75bde80d8a981acb)
#### Saturday 2022-08-27 11:35:52 by petrero

13.1 Parameters - php bin/console debug:container --parameters

  We know there's this container concept that holds all of our services... and we can see the full list of services by running:

    php bin/console debug:container

  Listing Parameters
  - Well, it turns out that the container holds one other thing: grudges. Seriously, don't expect to pull a prank on the service container and get away with it.

  Ok, what it really holds, in addition to services, is parameters. These are simple configuration values, and we can see them by running a similar command:

    php bin/console debug:container --parameters
  These are basically variables that you can read and reference in your code. We don't need to worry about most of these, actually. They're set by internal things and used by internal things. But there are a few that start with kernel that are pretty interesting, like kernel.project_dir, which points to the directory of our project. Yep! If you ever need a way to refer to the directory of your app, this parameter can help.

  Fetching Parameters from a Controller
  - So... how do we use these parameters? There are two ways. First, it's not super common, but you can fetch a parameter in your controller. For example, in VinylController, let's dd($this->getParameter()) - which is a shortcut method from AbstractController - and then kernel.project_dir. We even get some nice auto-completion thanks to the Symfony PhpStorm plugin!
  And when we try it... yep! There it is!

  Referencing Parameters with %parameter%
  - Now... delete that. This works, but most of the time, the way you'll use parameters is by referencing them in your configuration files. And we've seen this before! Open up config/packages/twig.yaml:

  7 lines  config/packages/twig.yaml
  twig:
    default_path: '%kernel.project_dir%/templates'

  Remember that default_path? That's referencing the kernel.project_dir parameter. When you're in any of these .yaml configuration files and you want to reference a parameter, you can use this special syntax: %, the name of the parameter, then another %

---
## [petre-symfony/symfony-6-fundamentals-services-config-and-environments](https://github.com/petre-symfony/symfony-6-fundamentals-services-config-and-environments)@[be4c7ead64...](https://github.com/petre-symfony/symfony-6-fundamentals-services-config-and-environments/commit/be4c7ead647123949cfe792c13cf28119ede49ac)
#### Saturday 2022-08-27 11:35:52 by petrero

14.1 Manual Service Config in services.yaml

  At your terminal, run:

    bin/console debug:container --parameters
  One of the kernel parameters is called kernel.debug. In addition to environments, Symfony has this concept of "debug mode". It's true for the dev environment and false for prod. And, occasionally, it comes in handy!

  Here's our new challenge (mostly to see if we can do it). Inside of MixRepository, I want to figure out if we're in debug mode. If debug mode is true, we will cache for 5 seconds. If it's false, I want to cache for 60 seconds

  Dependency Injection!
  - Let's back up for a minute. Suppose you're working inside of a service like MixRepository. Suddenly you realize that you need some other service like the logger. What do you do to get the logger? The answer: you do the dependency injection dance. You add a private LoggerInterface $logger argument and property... then you use it down in your code. You'll do this tons of times in Symfony.

  Let me undo that... because we don't actually need the logger right now. But what we do need is similar. Right now we're inside of a service and we've suddenly realized that we need some configuration (the kernel.debug flag) to do our work. What do we do to get that config? The same thing! Add that as an argument to our constructor. Say private bool $isDebug, and down here, use it: if $this->isDebug, cache for 5 seconds, else cache for 60 seconds.

  Non-Autowireable Arguments
  - But... there's a slight complication... and I bet you already know what it is. When we refresh the page... yikes! We get a Cannot resolve argument error. If you skip a bit, it says:

    Cannot autowire service App\Service\MixRepository: argument $isDebug of method __construct() is type-hinted bool, you should configure its value explicitly.

  That makes sense. Autowiring only works for services. You can't have a bool  argument and expect Symfony to somehow realize that we want the kernel.debug parameter. I might be a wizard, but I don't have a spell for that. I can make a whole slice of pie disappear, though. With magic. Definitely.

---
## [Axlefublr/Main](https://github.com/Axlefublr/Main)@[b511aa63ae...](https://github.com/Axlefublr/Main/commit/b511aa63aea7e05c1212a7ebc3bcb29287638e46)
#### Saturday 2022-08-27 12:18:29 by Axlefublr

Single line and expression only functions in App.ahk switched to arrow functions. Single function function abstractions now use bind, since global variables are recognized by the extension. My new-found formatter will be taking over my formatting preferences from now on (can't figure out how to change its behavior). While I can do some magic with the extension's regex, I've had my share of fun with that and now I'm moving towards comfortability > feature(ability). I could implement object coloring, change the colors for built in methods, functions, properties, etc; Different highlighting for links, but that's something I have to maintain. Yes, I used to have functions that did all of that for me automatically, but were still something to take care of, from time to time, or at the very least I thought about them. Now I have the priviledge of using good software without the need to really change it, so I'll just make do with what I have, rather than going back to 'maintain hell'. I'm not being paid for that shit after all!. While highlighting properties over the object they're on looks goofy, it gets the job done of contrasting the start of the object and the end of it, also doing the job of separating functions with methods

---
## [petre-symfony/symfony-6-fundamentals-services-config-and-environments](https://github.com/petre-symfony/symfony-6-fundamentals-services-config-and-environments)@[da66e9fb42...](https://github.com/petre-symfony/symfony-6-fundamentals-services-config-and-environments/commit/da66e9fb4210332e1cbf2020b92e8155c74aab15)
#### Saturday 2022-08-27 12:33:09 by petrero

15.2 All About services.yaml

   This would work just fine. But thanks to the _defaults section, those aren't needed! The _defaults says:

    Unless it's been overridden on a specific service, set autowire and autoconfigure to true for all services in this file.

  And what does autowire do? Simple! It tells Symfony's container:

    Hey! Please try to guess my constructor arguments by looking at their type-hints.

  This feature is pretty awesome... which is why it's automatically turned on for all of our services. The other option - autoconfigure - is more subtle and we'll talk about it later.

  Service Auto-Registration
  - All right, by the time we get to the _defaults line, we've established some default configuration... but we haven't actually registered any services yet. That's the job of the next section... and it's the key to everything:

  29 lines  config/services.yaml
  services:
    # makes classes in src/ available to be used as services
    # this creates a service per class whose id is the fully-qualified class name
    App\:
        resource: '../src/'
        exclude:
            - '../src/DependencyInjection/'
            - '../src/Entity/'
            - '../src/Kernel.php'
  This special syntax says

    Please look inside the src/ directory and automatically register all PHP classes as a service... except for these three things.

  This is why, immediately after we created the MixRepository class, it was already in the container! And thanks to the _defaults section, any services registered by this will automatically have autowire: true and autoconfigure: true. That's some serious team work! This mechanism is called "Service Auto-Registration".

  But remember, every service in the container needs to have a unique ID. If you look back at debug:container, most of the service IDs are snake case. Let me zoom out a bit so it's easier to see. Better! So, for example, the Twig service has the snake case twig ID. But if you scroll up to the top of this list, our MixRepository ID is... the full class name.

  Yep! When you use Service Auto-Registration, it uses the class name as both the class and the service ID. This is done for simplicity... but also for autowiring. When we try to autowire MixRepository into our controller or anywhere else, to figure out which service to pass us, Symfony will look for a service whose ID exactly matches App\Service\MixRepository. So Service Auto-Registration not only registers our classes as services, it does it in a way that makes them autowireable. That's awesome!

  Auto-Registration of Non-Services?
  - Anyway, after this section here, every class in src/ is now registered as a service in the container. Except, well... we don't want every class in src/ to be a service.

  There are really two types of classes in your app: "Service classes" that do work, and "model classes" - sometimes called "DTOs" - whose job is mostly to hold data - like a Product class with name and price properties. We want the container to handle instantiating our services. But for model classes, we will create them whenever we need them - like with $product = new Product(). So, these will not be services in the container.

 In the next tutorial, we'll create Doctrine entity classes, which are model classes for the database. These will live in the src/Entity/ directory... and since they're not meant to be services, that directory is excluded. So we register everything in the src/ directory as a service, except for these three things.

  But.. fun fact! This exclude key is not that important. Heck, you could delete it and everything would still work! If you accidentally register something as a service that isn't meant to be a service, no worries! Since you'll never try to autowire and use that class like a service, Symfony will realize it's not being used and remove it from the container. Dang, that is smart!

---
## [learn-more/reactos](https://github.com/learn-more/reactos)@[4471ee4dfa...](https://github.com/learn-more/reactos/commit/4471ee4dfaddb2440601fd61c01542b586b7c2d0)
#### Saturday 2022-08-27 12:46:22 by George Bișoc

[NTOS:SE] Properly handle dynamic counters in token

On current master, ReactOS faces these problems:

- ObCreateObject charges both paged and non paged pool a size of TOKEN structure, not the actual dynamic contents of WHAT IS inside a token. For paged pool charge the size is that of the dynamic area (primary group + default DACL if any). This is basically what DynamicCharged is for.
For the non paged pool charge, the actual charge is that of TOKEN structure upon creation. On duplication and filtering however, the paged pool charge size is that of the inherited dynamic charged space from an existing token whereas the non paged pool size is that of the calculated token body
length for the new duplicated/filtered token. On current master, we're literally cheating the kernel by charging the wrong amount of quota not taking into account the dynamic contents which they come from UM.

- Both DynamicCharged and DynamicAvailable are not fully handled (DynamicAvailable is pretty much poorly handled with some cases still to be taking into account). DynamicCharged is barely handled, like at all.

- As a result of these two points above, NtSetInformationToken doesn't check when the caller wants to set up a new default token DACL or primary group if the newly DACL or the said group exceeds the dynamic charged boundary. So what happens is that I'm going to act like a smug bastard fat politician and whack
the primary group and DACL of an token however I want to, because why in the hell not? In reality no, the kernel has to punish whoever attempts to do that, although we currently don't.

- The dynamic area (aka DynamicPart) only picks up the default DACL but not the primary group as well. Generally the dynamic part is composed of primary group and default DACL, if provided.

In addition to that, we aren't returning the dynamic charged and available area in token statistics. SepComputeAvailableDynamicSpace helper is here to accommodate that. Apparently Windows is calculating the dynamic available area rather than just querying the DynamicAvailable field directly from the token.
My theory regarding this is like the following: on Windows both TokenDefaultDacl and TokenPrimaryGroup classes are barely used by the system components during startup (LSASS provides both a DACL and primary group when calling NtCreateToken anyway). In fact DynamicAvailable is 0 during token creation, duplication and filtering when inspecting a token with WinDBG. So
if an application wants to query token statistics that application will face a dynamic available space of 0.

---
## [FurryMrNuts/sillycathax](https://github.com/FurryMrNuts/sillycathax)@[3bd117f451...](https://github.com/FurryMrNuts/sillycathax/commit/3bd117f45142d4696df7e0bf8fbafd0b9cb5cef8)
#### Saturday 2022-08-27 13:36:45 by FurryMrNuts

sillycathax loadstring

fuck you aflac im releasing this to the public

---
## [wrye-bash/wrye-bash](https://github.com/wrye-bash/wrye-bash)@[510e59c0f5...](https://github.com/wrye-bash/wrye-bash/commit/510e59c0f5d9f1c547bc36c44c5718cf337e4e90)
#### Saturday 2022-08-27 13:50:31 by Infernio

Rework the Mods tab's context menu RRR

You now what really doesn't help the first time user experience?
Throwing a giant context menu in their face. Sometimes people report
they can't find the Rebuild Patch option even though it's right there -
almost certainly because in order to find it, their eyes have to scan
through up to *twenty-eight* menu items.

This commit brings a similar refactoring to what we did to the
Installers tab to the Mods tab as well. There are now only twelve
top-level items, exposing the most commonly used features (e.g. Rebuild
Patch, Move to, Jump to Installer, etc.) at the top level and placing
the less commonly used features in sub-menus (Info and Plugin, in this
case - plus an Advanced menu for the weird shit:tm:).

Note 'Export Patch Configuration' getting dropped entirely - you can
already do that via Rebuild Patch... > Export, plus it was confusing
that you could export like this but not *import* that way. And on top of
all that, it would have lead to unintuitive UI with the new context
menu, since I would have either had to move it to Plugin.. or kept such
a rarely used command at top level.

Didn't update the docs for this because they also haven't been updated
for the latest Installers changes yet and I want to do all that in one
go with updated images and all.

Closes # 643 <--- RRR

---
## [anchit-choudhry/spark](https://github.com/anchit-choudhry/spark)@[c4c623a3a8...](https://github.com/anchit-choudhry/spark/commit/c4c623a3a890267b2f9f8d472c8be30fc5db53e1)
#### Saturday 2022-08-27 14:37:08 by Hyukjin Kwon

[SPARK-39869][SQL][TESTS] Fix flaky hive - slow tests because of out-of-memory

### What changes were proposed in this pull request?

This PR adds some manual `System.gc`. I know enough that this doesn't guarantee the garbage collection and sounds somewhat funny but it works in my experience so far, and I did such hack in some places before.

### Why are the changes needed?

To deflake the tests.

### Does this PR introduce _any_ user-facing change?

No, dev and test-only.

### How was this patch tested?

CI in this PR should test it out.

Closes #37291 from HyukjinKwon/SPARK-39869.

Authored-by: Hyukjin Kwon <gurwls223@apache.org>
Signed-off-by: Hyukjin Kwon <gurwls223@apache.org>

---
## [newstools/2022-iol-weekend-argus](https://github.com/newstools/2022-iol-weekend-argus)@[87e884e9bf...](https://github.com/newstools/2022-iol-weekend-argus/commit/87e884e9bf829af7ebdc1016287dcaab9d44b96d)
#### Saturday 2022-08-27 16:42:08 by Billy Einkamerer

Created Text For URL [www.iol.co.za/weekend-argus/weekend-argus/news/where-there-is-hope-there-is-life-two-year-mystery-of-missing-school-girl-f14eb090-9bc0-47f0-a6cb-dccf4d445422]

---
## [Smattr/mattutils](https://github.com/Smattr/mattutils)@[c2160bd59e...](https://github.com/Smattr/mattutils/commit/c2160bd59e222a5e67d4162d2e85a309287fe531)
#### Saturday 2022-08-27 17:02:07 by Matthew Fernandez

vim: disable Python ftplugin overriding tabstop settings

Honestly, WTF? If I set my own tabstop settings, I’m pretty sure I want them
applied, not some other bullshit.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[8b23190e84...](https://github.com/mrakgr/The-Spiral-Language/commit/8b23190e84aed941466a1dbde1e90a08f08b4357)
#### Saturday 2022-08-27 17:13:09 by Marko Grdinić

"6:30pm. Oh shit, I was in bed for a lot longer than I thought. I couldn't help it. I am very sad today. As I think about the self improvement loop it just bring my own failures to bear. While doing 3d art I was able to avoid it for a while, but that damn failure essentially ruined me.

It is going to take me effort to overcome.

I have 3 goals.

1) Write Simulacrum.
2) The second one I will save for the author's note.
3) Try out the evolutionary approach. Put my effort where my mouth is and try it out on a small scale.

I can't really just not program for the next few years. Taking on a project to redeem myself is something I should challenge myself with.

Taking a meta approach to ML is something that will help me overcome my defeat.

It will help me move from putting my hope on the ML community or the hardware guys, to my own programming. Why not make that basic bitch poker agent using evo methods?

It is true that the true power of evolution lies in evolving learning algorithms, but I won't be able to try that path until the hardware gets good enough. But nonetheless, I know that this is what I will be doing.

If somebody gives me the brain core, and the human intelligence algorithms, how would I go to a level higher than that?

Of course, by using the power of evolution. With the brain core, that approach would be limitlessly more powerful. It would work.

It wouldn't work on my current rig. But there is something to be said for getting some practice early on. It would at least prove that I am not a complete fuck up.

6:35pm. Also I think I figured out what the purpose of sleep is.

The strength of evolutionary algorithms, is that I could continually build and add parameters, and optimize them piecemeal. At the end of that I could have a large program, that has been gradually built up. What I could do then, is that and distil them into a NN.

Deep RL is super shitty, but distiling a policy would just be supervised learning and work well.

After that I could use that NN as just another component in the program and start building it up again using evo methods. This would avoid all the instability of RL and give me guaranteed improvements.

I think that the brain does something similar - during the day it accumulates memories and during sleep it distils them. Why not optimize directly?

Because actual RL is very unstable, but supervised learning is the opposite.

Tabular RL is a red herring, I won't find a use for it.

Evolutionary algorithms are really good at one thing - optimizing parameters regardless of their placement. I could even take that original network, copy it, stick extra layers in it, and optimize those piece by piece and afterwards distil it into the original.

There is a point to this - by adding memories instead of mutating them, you can guarantee never losing the original progress.

6:45pm. Sigh, I won't regret learning 3d, but the last year sucked. The parts that really stick out for me are the job applications. I've never been so humiliated in my life. It feels like in the last year I went against everyhing I stand for.

The me that I idolize should have firm beliefs and confidence in his skills, right now I have neither.

I will take on the project on brushing up on evolutionary methods using poker. But it won't be like last time. Since this will be small scale, my goals will be humbler. It will just be preparation for the future.

To begin with, nature probably started off with simple behavioral programs and then added memory as it went along. I doubt that bacteria needed to sleep. I should follow in its example and do it step by step.

7pm. I've falled into a trap set by people like Hinton. For some reason I've internalized that doing things by hand is cheating, when I should have well known that there is a way path from handwritten rules to general behavior.

After I do my small scale tests, I won't have good enough to make money in real world tables, but at least I will be able to call myself a proper scientist. Evolutionary methods are the automation of science.

7:05pm. Let me commit here. Tomorrow I am going to see if I can get some writing done. If I can't I'll spend the day in bed again until I muster up the will.

7:10pm. I don't think I can really be myself without programming. Even if it is for small wins, I should aim for them. I should save my grandest thoughts for my writing, and my humblest thoughts for my programming."

---
## [ORCACommander/Tannhauser-Gate-Dev](https://github.com/ORCACommander/Tannhauser-Gate-Dev)@[f0cef47678...](https://github.com/ORCACommander/Tannhauser-Gate-Dev/commit/f0cef47678384716080d4cc2adfa8be85b9ddc69)
#### Saturday 2022-08-27 17:38:41 by SkyratBot

[MIRROR] Adds the Mothroach [MDB IGNORE] (#15399)

* Adds the Mothroach (#68763)

About The Pull Request

Yup. That's pretty much it. This PR adds the Mothroach to the game, described as "An ancient ancestor of the moth that surprisingly looks like the crossbreed of a moth and a cockroach."

Do you love the Mothroach? Then you can cuddle with it and pat it, as well as place it on your head for extra cuteness.
What if you hate it, though? You can always kill and butcher Mothroaches in order to mass produce moth plushes for your own profit... How fun!

Either way, you win!

The Mothroach can be picked up and has a special on-head sprite (which looks really cute). It is able to vent-crawl and you may get one by randomly summoning a friendly mob through the gold slime extracts, or by ordering one through the Cargo Requests. After butchered, you may use its hide, a heart, and some cloth to craft a moth plushie, the most devilish of Devil's designs.

Full Preview of all the Sprites (NEW): https://www.youtube.com/watch?v=pdg8FTNEYjI
Preview of some of the Sprites (OLD): https://www.youtube.com/watch?v=9A-8hGCiW0s
In-hand, on-head, and grounded Mothroach sprite credits go to ValuedEmployee.
I did the Mothroach hide sprite though!
Why It's Good For The Game

The Mothroach is incredibly cute and a neat, fresh, new piece of content. Although it could use some future repurposing, right now it's simply a cute exotic pet with a few interactions.

These cute sprites are just too good to go to waste...

I keep seeing people complain about the lack of new content. Well, here's something niche that won't break the whole balance of the game and that will be cute. I seriously cannot see a motive not to add this to the game. Just because it isn't a powergaming tool or something that is seen every shift, that doesn't mean that it won't have a positive influence on the game. As I have stated, right now the Mothroaches are underperforming in terms of interactions and ways of getting them, but adding them is the first step to later improve them.
Changelog

cl
add: The Mothroach, your new local exotic pet
add: Mothroach Hide and Mothroach Meat
add: New crafting recipe for the Moth Plush: 1 Mothroach Hide; 1 heart; 3 cloth
fix: Fixes dead mobs on-head not having sprites
/cl

* Adds the Mothroach

Co-authored-by: Justice <42555530+Justice12354@users.noreply.github.com>

---
## [ginkgo-stuff/android_frameworks_base](https://github.com/ginkgo-stuff/android_frameworks_base)@[e7533e5ae0...](https://github.com/ginkgo-stuff/android_frameworks_base/commit/e7533e5ae0a1366dc3a69cce7aa1d6ece890ffb7)
#### Saturday 2022-08-27 17:52:59 by Joey Huab

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

---
## [petre-symfony/symfony-6-fundamentals-services-config-and-environments](https://github.com/petre-symfony/symfony-6-fundamentals-services-config-and-environments)@[d72b47fdad...](https://github.com/petre-symfony/symfony-6-fundamentals-services-config-and-environments/commit/d72b47fdad4c0e3fa9e3b206484360a411c37491)
#### Saturday 2022-08-27 18:03:00 by petrero

17.1 Named Autowiring & Scoped HTTP Clients

  In MixRepository, it would be cool if we didn't need to specify the host name when we make the HTTP request. Like, it'd be great if that were preconfigured and we only needed to include the path. Also, pretty soon, we're going to configure an access token that will be used when we make requests to the GitHub API. We could pass that access token manually here in our service, but how cool would it be if the HttpClient service came preconfigured to always include the access token?

  So, does Symfony have a way for us to, sort of, "preconfigure" the HttpClient service? It does! It's called "scoped clients": a feature of HttpClient where you can create multiple HttpClient services, each preconfigured differently.

  Creating a Scoped Client
  - Here's how it works. Open up config/packages/framework.yaml. To create a scoped client, under the framework key, add http_client followed by scoped_clients. Now, give your scoped client a name, like githubContentClient... since we're using a part of their API that returns the content of files. Also add base_uri, go copy the host name over here... and paste

  Remember: the purpose of these config files is to change the services in the container. The end result of this new code is that a second HttpClient service will be added to the container. We'll see that in a minute. And, by the way, there's no way that you could just guess that you need http_client and scoped_clients keys to make this work. Configuration is the kind of thing where you really need to rely on the documentation.

  Anyways, now that we've preconfigured this client, we should be able to go into MixRepository and make a request directly to the path

  But if we head over and refresh... ah...

    Invalid URL: scheme is missing [...]. Did you forget to add "http(s)://"?

  I didn't think we forgot... since we configured it via the base_uri option... but apparently that didn't work. And you may have guessed why. Find your terminal and run:

    php bin/console debug:autowiring client
  There are now two HttpClient services in the container: The normal, non-configured one and the one that we just configured. Apparently, in MixRepository, Symfony is still passing us the unconfigured HttpClient service.

  How can I be sure? Well, think back to how autowiring works. Symfony looks at the type-hint of our argument, which is Symfony\Contracts\HttpClient\HttpClientInterface, and then looks in the container to find a service whose ID is an exact match. It's that simple

---
## [Joe-Degs/emulator](https://github.com/Joe-Degs/emulator)@[8beef32c9e...](https://github.com/Joe-Degs/emulator/commit/8beef32c9e6a042204b6df0a8c0001f9b772225c)
#### Saturday 2022-08-27 20:01:44 by Joseph Attah

fixed bugs and cleaned up code

its been a long week but everything is working now.. hurray!
I have cleaned up the code significantly, cleared up all magic
numbers in the code. The problem keeping me up were some omission
errors in the logic for decoding instructions, but that is behind
me now. I still think there might be some sign extension bugs in it
but I don't know if I can find and fix those until they start biting
me in the ass.
It executes well too for now.. until i find
the next bug that keeps me up at night. I am not going to be working
on this too much now, i have to concentrate on my final thesis and
graduate successfully. tough couple of weeks ahead of me i'll tell
you that.

---
## [petre-symfony/symfony-6-fundamentals-services-config-and-environments](https://github.com/petre-symfony/symfony-6-fundamentals-services-config-and-environments)@[92bc58ab23...](https://github.com/petre-symfony/symfony-6-fundamentals-services-config-and-environments/commit/92bc58ab23b9dadef15f055adca249e91ab6d502)
#### Saturday 2022-08-27 21:05:29 by petrero

9 Environments
  Our application is like a machine: it's a set of services and PHP classes that do work... and ultimately render some pages. But we can make our machine work differently by feeding it different configuration.

  For example, in SongController, we're using the  service to log some information:

 30 lines  src/Controller/SongController.php
  class SongController extends AbstractController
  {
    #[Route('/api/songs/{id<\d+>}', methods: ['GET'], name: 'api_songs_get_one')]
    public function getSong(int $id, LoggerInterface $logger): Response
    {
    }
  }
  If we feed the logger some configuration that says "log everything", it will log everything, including low level debug messages. But if we change the config to say "only log errors", then this will only log errors. In other words, the same machine can behave differently based on our configuration. And sometimes, like with logging, we might need that configuration to be different while we're developing locally versus on production.

  To handle this, Symfony has an important concept called "environments". I don't mean environments like local vs staging vs beta vs production. A Symfony environment is a set of configuration.

  For example, you can run your code in the dev environment with a set of config that's designed for development. Or you can run your app in the prod environment with a set of config that's optimized for production. Let me show you!

  The APP_ENV Variable
  - In the root of our project, we have a .env file:

 20 lines  .env
  # In all environments, the following files are loaded if they exist,
  # the latter taking precedence over the former:
  #
  #  * .env                contains default values for the environment variables needed by the app
  #  * .env.local          uncommitted file with local overrides
  #  * .env.       committed environment-specific defaults
  #  * .env..local uncommitted environment-specific overrides
  #
  # Real environment variables win over .env files.
  #
  # DO NOT DEFINE PRODUCTION SECRETS IN THIS FILE NOR IN ANY OTHER COMMITTED FILES.
  #
  # Run "composer dump-env prod" to compile .env files for production use (requires symfony/flex >=1.2).
  # https://symfony.com/doc/current/best_practices.html#use-environment-variables-for-infrastructure-configuration
  ###> symfony/framework-bundle ###
  APP_ENV=dev
  APP_SECRET=4777a99cd6c61ce84969bd1338737c38
  ###
  We're going to talk more about this file later. But see this APP_ENV=dev? This tells Symfony that the current environment is dev, which is perfect for local development. When we deploy to production, we'll change this to prod. More on that in a few minutes.

  But... what difference does that make? What happens in our app when we change this from dev to prod? To answer, let me close some folders... and open public/index.php:

  10 lines  public/index.php
  <?php
  use App\Kernel;
  require_once dirname(__DIR__).'/vendor/autoload_runtime.php';
  return function (array $context) {
    return new Kernel($context['APP_ENV'], (bool) $context['APP_DEBUG']);
  };
  Remember: this is our front controller. It's the first file that's executed on every request. We don't really care much about this file, but its job is important: it boots up Symfony.

  What's interesting is that it reads the APP_ENV value and passes it as the first argument to this Kernel class. And... this Kernel class is actually in our code! It lives at src/Kernel.php.

  Cool. So what I want to know now is: What does the first argument to Kernel control?

  If we open the class we find... absolutely nothing. It's empty. That's because the majority of the logic lives in this trait. Hold "cmd" or "control" and click MicroKernelTrait to open that up.

  The config/packages/{ENV} Directory
  - The job of the Kernel is to load all of the services and routes in our app. If you scroll down, it has a method called configureContainer(). Ooh! We know what the container is now! And check out what it does! It takes this $container object and imports $configDir.'/{packages}/*.{php,yaml}'. This line says:

    Yo container! I want to load all of the files from the config/packages/ directory.

  It loads all of those files, and then it passes the configuration from each to whatever bundle is defined as the root key. But what's really interesting for environments is this next line: import $configDir.'/{packages}/'.$this->environment.'/*.{php,yaml}'. If you dug a little, you'd learn that $this->environment is equal to the first argument that's passed to Kernel!

  In other words, in the dev environment, this will be dev. So, in addition to the main config files, this will also load anything in the config/packages/dev/ directory. Yup, we can add extra config there that overrides the main configuration in the dev environment. For example, we could add logging config that tells the logger to log everything!

  Below this, we also load a file called services.yaml and, if we have it, services_dev.yaml. We'll talk more about services.yaml real soon.

  The when@{ENV} Config
  - So, if you want to add environment-specific configuration, you can put it in the correct environment directory. But there's one other way. It's a pretty new feature and we saw it at the bottom of twig.yaml. It's the when@ syntax:

  7 lines  config/packages/twig.yaml
  when@test:
    twig:
        strict_variables: true
  In Symfony, by default, there are three environments: dev, prod, and then if you run automated tests, there's an environment called test. Inside of twig.yaml, by saying, when@test, it means that this configuration will only be loaded if the environment is equal to test.

  The best example of this might be in monolog.yaml. monolog is the bundle that controls the logger service. It does have some configuration that's used in all environments. But, below this, it has when@dev. We won't talk too much about the specific monolog configuration, but this controls how log messages are handled. In the dev environment, this says that it should log everything and it should log to a file, using this fancy %kernel.logs_dir% syntax that we'll learn about soon.

  Anyways, this points to a var/logs/dev.log file and the level: debug part means that it will log every single message to dev.log... regardless of how important or unimportant that message is.

  Below this, for the prod environment, it's quite different. The most important line is action_level: error. That says:

  Hi Ms Logger! This app probably logs a ton of messages, but I only want you to actually save messages that are an error importance level or higher.

  That makes sense! In production, we don't want our log files filling up with tons and tons of debug messages. With this, we only log error messages.

  The big point is this: by using these tricks, we can configure our services differently based on the environment.

  Environment-Specific Routing
  - And, we can even do the same thing with routes! Sometimes you have entire routes that you only want to load in a certain environment. Back in MicroKernelTrait, if you go down, there's a method called configureRoutes(). This is what's responsible for loading all of our routes... and it's very similar to the other code. It loads $configDir.'/{routes}/*.{php,yaml}' as well as this dev environment directory, if you have one. We don't.

  You can also use the when@dev trick. This file is responsible for registering the routes used by the web debug toolbar. We don't want the web debug toolbar in production... so these routes are only imported in the dev environment.

  9 lines  config/routes/web_profiler.yaml
  when@dev:
    web_profiler_wdt:
        resource: '@WebProfilerBundle/Resources/config/routing/wdt.xml'
        prefix: /_wdt
    web_profiler_profiler:
        resource: '@WebProfilerBundle/Resources/config/routing/profiler.xml'
        prefix: /_profiler
  Heck, certain bundles are only enabled in some environments! If you open config/bundles.php, we have the name of the bundle... and then on the right, the environments in which that bundle should be enabled. This all means all environments.... and most are enabled in all environments.

  The WebProfilerBundle however - the bundle that gives us the web debug toolbar and profiler - is only loaded in the dev and test environments. Yup, the entire bundle - and the services it provides - are never loaded in the prod environment.

  So, now that we understand the basics of environments, let's see if we can switch our application to the prod environment. And then, as a challenge, we'll configure our cache service differently in dev. That's next.

---
## [petre-symfony/symfony-6-fundamentals-services-config-and-environments](https://github.com/petre-symfony/symfony-6-fundamentals-services-config-and-environments)@[c7b4137117...](https://github.com/petre-symfony/symfony-6-fundamentals-services-config-and-environments/commit/c7b41371173e42d230cee0690550fa5844aebba7)
#### Saturday 2022-08-27 21:05:29 by petrero

8 debug:container & How Autowiring Works - php bin/console debug:container

  Before we talk about environments, I need to come clean about something: I have not been showing you all of the services in Symfony. Not even close.

  Head over your terminal and run our favorite command:

    php bin/console debug:autowiring
  We know that all of these services are floating around in Symfony, waiting for us to ask for them. And we know that bundles give us services. The Twig service down here comes from TwigBundle.

  And since each service is an object, something somewhere must be responsible for instantiating these objects. The question is: "Who?" And the answer is... the service container!

  Hello Service Container
  - It turns out that all of the services aren't really... "floating around": they all live inside something called the "container". And there are way more services in the container than debug:autowiring has been telling us about. Ooh... secrets! This time, run:

    php bin/console debug:container
  And... whoa! This prints out a huge list. It's so big, it's hard to see everything. Let me make my font smaller. Much better!

  This is the full list of all of the services in our app... or in the "container". The container is basically a giant "array" where each service has a unique name that points to its service object. For example, down here... there we go... we can see that there's a service whose unique name - or "id" is twig.

  Knowing that the id of the Twig service is twig is not usually important, but it is useful to understand that each service has a unique id... and that you can see all of them inside the debug:container command.

  The Container Creates Objects
  - And really, the container might be better-described as a big array of instructions on how to instantiate services, if and when something asks for them. For instance, the container knows exactly how to instantiate this Twig service. It knows that its class is Twig\Environment. And even though you can't see it on this list, it knows the exact arguments to pass to its constructor. The moment someone needs the Twig service, the container instantiates it and returns it.

  Yup, when we autowire a service, we're basically saying:

    Hey container, can you please give me the HTTP Client service?

  If nothing in our code has asked for that service yet during this request, the container will create it. But if something has already asked for it, then the container will simply return the one it already created. This means that if we ask for the HTTP Client service in ten different places, the container will only create and return the same one instance. Pretty cool!

  How Autowiring Works
  - Anyway, debug:container shows us all of the services that the container knows how to instantiate. But debug:autowiring only shows us a fraction of those services. Why?

  Well, it turns out that not all services are autowireable. Many of the items in this list are low-level services that just exist to help other services do their job. You'll probably never need to use these low-level services directly... and you actually cannot fetch them via autowiring.

  But, let's back up a minute. Now that we know a bit more, we can now learn exactly how Symfony's autowiring system works. It's beautifully simple.

  As we've seen, the container is really an array where every service has an id that points to that service object. When Symfony sees this HttpClientInterface type - this is the full type that it sees, thanks to our use statement - in order to figure out which service in the container it needs to pass us, it simply looks for a service whose ID matches this string exactly. Let me show you!

  Scroll towards the top of this list to find... a service whose ID is Symfony\Contracts\HttpClient\HttpClientInterface! The vast majority of the services in the container use the "snake case" naming strategy. But if a service is intended for us to use in our code, Symfony will add an additional service inside that matches its class or interface name.

  Thanks to that, when we type-hint HttpClientInterface, Symfony looks in the container for a service whose id is Symfony\Contracts\HttpClient\HttpClientInterface, it finds it and passes it to us.

  Service Aliases
  - But look over on the right side: it says that this is an alias for a different service ID. An "alias" is like a symbolic link. It means that when someone asks for the HttpClientInterface service, Symfony will actually pass us this other service.

  We can use the same logic down here for the CacheInterface type. If we check the list, here's the service whose id matches that type. But, in reality, it's just an alias for a service called cache.app. So when we autowire CacheInterface, the cache.app service is what's actually being passed to us.

  If you're feeling unsure, here are the three big takeaways. One: there are a ton of service objects floating around and they all live inside something called the "container". Each service has a unique id.

  Two, only a small percentage of these are useful to us... and those are set up so that we can autowire them. Autowiring works by looking in the container for a service whose id exactly matches the type. When we run debug:autowiring, it's basically just showing us the services from this list whose id is a class or interface name. Those are the "autowireable services".

  The third and final takeaway is that services also have an alias system... which just means that when we ask for the CacheInterface service, what it will really give us is the service whose id is cache.app.

  If you're wondering how we could ever use a non-autowireable service in our code, that's a great question! It's somewhat rare, but we will learn how to do that later.

  Next, let's talk about using different configuration locally versus production. Let's talk about environments.

---
## [petre-symfony/symfony-6-fundamentals-services-config-and-environments](https://github.com/petre-symfony/symfony-6-fundamentals-services-config-and-environments)@[ba40038510...](https://github.com/petre-symfony/symfony-6-fundamentals-services-config-and-environments/commit/ba4003851031846d9a8fcacdf353ea31df70a7bc)
#### Saturday 2022-08-27 21:05:29 by petrero

6.1 Bundle Config (to Control Bundle Services) - bin/console debug:config twig

  We're now using the HttpClientInterface and CacheInterface services. Yay! But we aren't actually responsible for instantiating these service objects. Nope, they're created by something else (we'll talk about that in a few minutes), and then just passed to us.

  That's great because all of these services - the "tools" of our app - come ready to use, out-of-the-box. But... if something else is responsible for instantiating these service objects, how can we control them?

  Introducing: bundle configuration!

  Bundle Configuration
  - Go check out the config/packages/ directory. This has a number of different YAML files, all of which are loaded automatically by Symfony when it first boots up. These files all have exactly one purpose: to configure the services that each bundle gives us.

  Open up twig.yaml:

  7 lines  config/packages/twig.yaml
  twig:
    default_path: '%kernel.project_dir%/templates'
  when@test:
    twig:
        strict_variables: true
  For now, ignore this when@test: we're going to talk about that in a few minutes. This file has a root key called twig. And so, the entire purpose of this file is to control the services provide by the "Twig" bundle. And, it's not the filename - twig.yaml - that's important. I could rename this to pineapple_pizza.yaml and it would work exactly the same and be delicious. I don't care what you think.

  When Symfony loads this file, it sees this root key - twig - and says:

  Oh, okay. I'm going to pass whatever configuration is below to TwigBundle.

  And remember! Bundles give us services. Thanks to this config, when TwigBundle is preparing its services, Symfony passes it this configuration and TwigBundle uses it to decide how its services should be instantiated... like what class names to use for each service... or what first second or third constructor arguments to pass.

  For example, if we changed the default_path to something like %kernel.project_dir%/views, the result is that the Twig service that renders templates would now be pre-configured to look in that directory.

  The point is: the config in these files give us the power to control the services that each bundle provides.

  Let's check out another one: framework.yaml:

  25 lines  config/packages/framework.yaml
  # see https://symfony.com/doc/current/reference/configuration/framework.html
  framework:
    secret: '%env(APP_SECRET)%'
    #csrf_protection: true
    http_method_override: false
    # Enables session support. Note that the session will ONLY be started if you read or write from it.
    # Remove or comment this section to explicitly disable session support.
    session:
        handler_id: null
        cookie_secure: auto
        cookie_samesite: lax
        storage_factory_id: session.storage.factory.native
    #esi: true
    #fragments: true
    php_errors:
        log: true
  when@test:
    framework:
        test: true
        session:
            storage_factory_id: session.storage.factory.mock_file
  Because the root key is framework, all of this config is passed to FrameworkBundle... which uses it to configure the services it provides.

  And, as I mentioned, the filename doesn't matter... though the name often matches the root key... just for sanity reasons: like framework and framework.yaml. But that's not always the case. Open up cache.yaml:

  20 lines  config/packages/cache.yaml
  framework:
    cache:
        # Unique name of your app: used to compute stable namespaces for cache keys.
        #prefix_seed: your_vendor_name/app_name
        # The app cache stores to the filesystem by default.
        # The data in this cache should persist between deploys.
        # Other options include:
        # Redis
        #app: cache.adapter.redis
        #default_redis_provider: redis://localhost
        # APCu (not recommended with heavy random-write workloads as memory fragmentation can cause perf issues)
        #app: cache.adapter.apcu
        # Namespaced pools use the above app backend by default
        #pools:
            #my.dedicated.cache: null
  Woh! This is... just more config for FrameworkBundle! It lives in its own file... just because it's nice to have a separate file to control the cache.

  Debugging the Available Bundle Config
  At this point, you might be asking yourself:

  Ok, cool... but what config keys are we allowed to put here? Where can I find which options are available?

  Great question! Because... you can't just "invent" whatever keys you want: that would throw an error. First, yes, you can, of course, read the documentation. But there's another way: and it's one of my favorite things about Symfony's config system.

  If you want to know what configuration you can pass to "Twig" bundle, there are two bin/console commands to help you. The first is:

  php bin/console debug:config twig

  This will print out all of the current configuration under the twig key, including any default values that the bundle is adding. You can see our default_path set to the templates/ directory, which comes from our config file. This %kernel.project_dir% is just a fancy way to point to the root of our project. More on that later.

  Try this: change the value to views, re-run that command and... yup! We see "views" in the output. Let me go ahead and change that back.

  So debug:config shows us all of the actual, current config for a specific bundle, like twig... which is especially handy since it also shows you defaults added by the bundle. It's a great way to see what you can configure. For example, apparently we can add a global variable to Twig via this globals key!

---
## [petre-symfony/symfony-6-fundamentals-services-config-and-environments](https://github.com/petre-symfony/symfony-6-fundamentals-services-config-and-environments)@[9e03e34696...](https://github.com/petre-symfony/symfony-6-fundamentals-services-config-and-environments/commit/9e03e346960fee4d391698a7859957bf307fd2a9)
#### Saturday 2022-08-27 21:05:29 by petrero

7.1 Configuring the Cache Service - php bin/console config:dump framework cache

  So... I want to know how I can configure the cache service... like to store the cache somewhere else. In the real world, we can just search for "How do I configure Symfony's cache service". But... we can also figure this out on our own, by using the commands we just learned.

  We already noticed there's a cache.yaml file

  It looks like FrameworkBundle is responsible for creating the cache service... and it has a sub cache key where we can pass some values to control it. All of this is commented-out at the moment.

  To get more information about FrameworkBundle, run:

    php bin/console config:dump framework
  FrameworkBundle is the main bundle inside of Symfony. So you can see that this dumps... wow... a ton. FrameworkBundle provides a lot of services... so there's a lot of config.

  Debugging the Cache Config
  - To... zoom in a bit, re-run the command again, passing framework and then cache to filter for that sub-key:

    php bin/console config:dump framework cache
  And... cool! This may not always be super understandable, but it's a great starting point. This definitely just helped us answer the question:

    Why does the cache system store stuff in the var/cache directory?

  Because... there's a directory key that defaults to %kernel.cache_dir%... which is a fancy way of pointing at the /var/cache/dev directory. And then we see /pools/app, which is the actual directory that holds our cache.

  Using dump() and the Profiler
  So here's the goal: instead of caching things to the filesystem, I want to change the cache system to store somewhere else. Before we do that, go into VinylController and, so we can see the result of the change we're about to make, dump($cache). We've been using dd() so far, which stands for "dump and die". But in this case I want dump()... but let the page load.

  Refresh now. Wait, where is my dump? This is a... feature! When you use dump(), you won't actually see it on the page: it hides down here on the web debug toolbar. If you look there, the cache is some sort of TraceableAdapter. But inside of that, there's an object called FilesystemAdapter. That's proof that the cache system is saving to the filesystem.

---
## [newstools/2022-sabc-news-online](https://github.com/newstools/2022-sabc-news-online)@[e44553b09a...](https://github.com/newstools/2022-sabc-news-online/commit/e44553b09aea003ff225538f6c41cf42007dce54)
#### Saturday 2022-08-27 22:03:35 by Billy Einkamerer

Created Text For URL [www.sabcnews.com/sabcnews/ec-police-arrests-a-29-year-old-female-for-her-boyfriends-murder/]

---
## [Atom-X-Devs/android_kernel_xiaomi_scarlet](https://github.com/Atom-X-Devs/android_kernel_xiaomi_scarlet)@[e009133bd3...](https://github.com/Atom-X-Devs/android_kernel_xiaomi_scarlet/commit/e009133bd35807adc9687ac7bc8c576ddedd1335)
#### Saturday 2022-08-27 22:25:44 by Peter Zijlstra

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
Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>

---
## [matthewgismondi76/matthewgismondi76.github.io](https://github.com/matthewgismondi76/matthewgismondi76.github.io)@[fd87b56863...](https://github.com/matthewgismondi76/matthewgismondi76.github.io/commit/fd87b5686304f5b448aa0317b2998bbcee7dbed4)
#### Saturday 2022-08-27 23:33:49 by Matthew Gismondi

Create holy

+I started to write this explanation about how being holy was not about being pure or perfect or anything at all except who you are, but then as soon as I started I was interrupted by a million people who were so excited to jump on the chance to call me out for being a hypocrite. I mean, someone on Grindr even suddenly was wanting to bring me GHB and couldn't stop telling me he was going to come over so I could suck his big fat d***. So I can see that I need to put this on hold and make a very clear statement about who I am and what my intentions are and also who I am not and who I have no desire to be because it's pretty sad when the people who judge Christians for being intolerant and close-minded turn out to be even worse themselves. It's the kind of thing that makes me want to give up on everyone and everything, and I already feel like that about my faith most of the time as it is. But it is because of things like that that turn my stomach and ultimately I do get angry at God which I know is unfair. But it is still frustrating when it feels like His help is completely hindered as if these people are stronger than He is which is what it feels like when you are screaming for help and nothing comes because of whatever reason. And this was supposed to be His chance to take His turn and show off after everyone else was done with their turn, but I guess they couldn't do that without ... without what? Why couldn't they do that? Because then I would know what they had been doing? What did everyone think was going to happen? That you could just go all out torturing and ignoring all the rules because it was a contest against God which meant you were playing outside of the rules? You can do anything you want to. Everyone has free will. But that doesn't mean you are free from justice and getting caught. I had been granted permission long ago to do the only illegal things that I do which are not even illegal in other countries. And it's not illegal by God's law either aside from following the laws of the land. That is why it was significant that I got permission, even though someone else claimed it as theirs because he had more power and influence than I did. A lot of people have done that and the more they did the more impossible it became to prove I was the one who earned it by my reputation and by doing things because I had confidence in the fact that it would hold up if anyone looked into it. And so far it has even against the odds and even with everyone poised at every moment to jump in and catch me. That doesn't mean that I still am strong enough to follow through with what I wrote a long time ago about taking something all the way to the supreme court though. That was not a public declaration of intent, but it was conveyed that way to a lot of people who have felt that I let them down. I wrote that before I was broken completely by my experience in North Carolina, and I have tried to make that clear many times since then. I am not the same person anymore, so when you came looking for the outspoken Jesus freak who had the dog that could understand what I said and the ability to focus on God and allow Him to turn ashes into gold when it was His will and not the will of someone who wanted to be rich (which is why parking yourself around me and starving me until I am forced to make that happen is never going to work and is about as f***ed up as all the other things people have done to me just because God drew near to me for no other reason than I was genuine. You wouldn't know that today most likely though since I spend most of my time screaming at Him for leaving me and throwing things and breaking them and keeping my mouth shut every opportunity I get to talk about Him. But that is because I feel like people are fishing for those things and it feels like just one more example of conditional love. Everyone requires something in return in order to be there for you and when you can't give it to them you're lucky if you are allowed to have any sort of peace at all. Angels are messengers from God. They can be Heavenly Hosts like Gabriel or Michael, they can be Watchers here on Earth, or they can even be human beings that He chooses to convey a message to other humans since angels of the spiritual nature are not meant to cross over that division except in extremely important circumstances. Like the advent of the Messiah and the apocalyptic events of the end of the world. Those are kind of extreme circumstances where you do not want to risk the fallibility of human nature that makes all other communication a little less perfect. That is not a flaw in design. It is a blessing to be able to get help from above at all. Why it keeps getting turned into some kind of cosmic vending machine free to plunder I do not know, but years ago God did give me a very clear message that came with a boot falling onto the floor in my hotel room as if to kick me for not delivering it then when I was supposed to. That was my fault, and that was over a year ago. But it was the clearest message I have ever received from Him and it was this: QUIT ROBBING ME. And that is a quote from Him. From Yahweh directly to everyone who has been cutting me off, demanding I justify to you what you took, and ignoring me when I told you I needed something. It is directly to those of you who roll your eyes and say, "Matt... do you really need to get some d***? Come on. Are you telling me that you REALLY need meth and GHB?" I don't know what you all have and what you have been sitting on or rerouting to your own pockets, so I don't know the answer to that. The message is to you all not to me. So if you are asking me that and you have been noticing strange things show up that you can't explain that you assumed to be from some Satanic cult that figured out they could follow me around and claim everything so they wouldn't have to pay for it themselves, then you know better than I do. And I don't know who all has been involved, but I suspect it was not all just about racism and gender. I have wondered how many times you put glyphosphate in what I was given or what other chemicals you enjoyed watching me smoke that never killed me. I'm not sure who made the magnetic stuff and how much of what you gave me actually did cure cancer or how much of that was just garbage knowing that you could take the credit for what healing God did. But what I am saying is that instead of seeing this as a chance to destroy me and giggle about it because you were annoyed by the things I screamed about you or about the things I wrote somewhere in a terminal and never even saved or because of voices you heard that were not even mine at all, I think this was supposed to be something along the lines of Goodwill and Union, and yet there are still too many people directly involved who would rather put me in my place and keep pocketing the good stuff because they are the only connection between you and me and they know that they can get away with it because how are you going to ever find out? You rely on them to give you all the information about me. They control my phone. They control my drugs. They control my life. The hand that rocks the cradle rules the world. And I am the one that was called Ba which often implied baby. Because that is what I am compared to everyone else. It is God that does anything significant, and I am happy to give Him the credit for that because it frees me from being culpable for anything that happened. If your camp got burned down then was it me that cursed you or did you attack me when I had asked God for the Shield of Faith? And my faith believed that if someone cursed me I could reflect it back to them. I have no interest in magic or spells because I don't want to be responsible for the consequences, and an argument could be made for manslaughter in situations that involve someone doing that to another person. Why there is no law against occult magic is beyond me because it is real and it is dangerous. And the terrifying thing to me is that the last time I was at a bookstore, the special deals section up front was covered with books about witchcraft and magic and spells aimed at children as if it were just a hobby and a cool thing to play with. What the F is wrong with anyone who would advertise Satan to children? I mean someone go find the people at Barnes & Noble and pick them up by the neck and shake them until they have some sense returned to their corporate board room selves. You made me use "selves" which isn't even a word. That is how upset that makes me. Because I found one tiny little book about God on the back side that was half buried. And yet when I want to get high and make someone feel good and feel good myself in a mutually beneficial and agreed upon situation I suddenly am attacked as if I am some kind of evil monster trying to shove my Jesus down everyone's throat while having sex privately behind closed doors? That is the best part. That people accuse me the way that they do and try to destroy me using private conversations in a gay hookup app. How are you going to argue anything when you were there too? Because I have posted screenshots of my conversations publicly before without revealing anyone's identity. And I have even sent printouts of them to the FBI to show them what was going on. They apparently were involved in it somehow is all I can figure though because all that happened was that the scrutiny was tightened. So eventually it leaves me with a feeling that everyone had some kind of stake in it including the Feds, and that is why the Eddie pie-hands theory became the dominant one. It wasn't necessarily all those different entities as much as something that has its hands in all the pies. Or has its fingers in all the cakes? Not only does that make it impossible to detect, but it makes it impossible to fight because they just all retreat back into their agency or board room and let them take the blame. And then we are back to guerilla warfare. Eventually we might even get back to cinnamon rabbit babies and Schroedinger's Cat, but I am not taking responsibility for Terms and Conditions. That was enforced by someone else, and I still will say even in this state of perpetual poverty and neck squeezing deprivation that I would not ever want anything that came from that because it was underhanded and stupid. I said it then and I'm saying it again. And I'll also say again that it was not being high that caused it. If it did then it was also being high that convicted me and made me remove it as soon as I posted it. I will never back down from that because it is important to me that I fight back against the ones who think that they can come at me with lies and tricks and make everyone else that I don't even know about think that I am being picky or unreasonable while they give me the same thing I repeatedly tell them I don't want while telling me to shut up under their breath. To say that being high was the reason why everything went  bad exonerates them and makes it harder for me to seek the help that I need because no matter what was going on at the time, the fact remains that there were complications from a medication that I was taking during a time of sobriety, and during that time of sobriety was when I noticed the problems that I still suffer from. And the people who keep coming at me telling me to shut up and making my life a living hell unless I admit that I was high during any time that there were problems is a clear indication of who they represent. That's all I am saying.

---

