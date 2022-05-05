## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-05-04](docs/good-messages/2022/2022-05-04.md)


1,757,603 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,757,603 were push events containing 2,802,397 commit messages that amount to 201,167,341 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 33 messages:


## [newstools/2022-sahara-reporters](https://github.com/newstools/2022-sahara-reporters)@[f25f198383...](https://github.com/newstools/2022-sahara-reporters/commit/f25f198383d6fabdf2a2e2a7d0d5725088650fa5)
#### Wednesday 2022-05-04 00:02:55 by Billy Einkamerer

Created Text For URL [saharareporters.com/2022/05/03/%E2%80%98god-won%E2%80%99t-forgive-you-if-we-all-die-poverty%E2%80%99-ex-biafran-war-veterans-tell-buhari]

---
## [vdavalon01/cockroach](https://github.com/vdavalon01/cockroach)@[13a65d3682...](https://github.com/vdavalon01/cockroach/commit/13a65d3682863dc94b5057801edae7ed8f7d7d18)
#### Wednesday 2022-05-04 00:19:35 by Andrei Matei

util/tracing: fix crash in StreamClientInterceptor

Before this patch, our client-side tracing interceptor for streaming rpc
calls was exposed to gRPC bugs being currently fixed in
github.com/grpc/grpc-go/pull/5323. This had to do with calls to
clientStream.Context() panicking with an NPE under certain races with
RPCs failing. We've recently gotten two crashes seemingly because of
this. It's unclear why this hasn't shown up before, as nothing seems new
(either on our side or on the grpc side). In 22.2 we do use more
streaming RPCs than before (for example for span configs), so maybe that
does it.

This patch eliminates the problem by eliminating the
problematic call into ClientStream.Context(). The background is that
our interceptors needs to watch for ctx cancelation and consider the RPC
done at that point. But, there was no reason for that call; we can more
simply use the RPC caller's ctx for the purposes of figuring out if the
caller cancels the RPC. In fact, calling ClientStream.Context() is bad
for other reasons, beyond exposing us to the bug:
1) ClientStream.Context() pins the RPC attempt to a lower-level
connection, and inhibits gRPC's ability to sometimes transparently
retry failed calls. In fact, there's a comment on ClientStream.Context()
that tells you not to call it before using the stream through other
methods like Recv(), which imply that the RPC is already "pinned" and
transparent retries are no longer possible anyway. We were breaking
this.
2) One of the grpc-go maintainers suggested that, due to the bugs
reference above, this call could actually sometimes give us "the
wrong context", although how wrong exactly is not clear to me (i.e.
could we have gotten a ctx that doesn't inherit from the caller's ctx?
Or a ctx that's canceled independently from the caller?)

This patch also removes a paranoid catch-all finalizer in the
interceptor that assured that the RPC client span is always eventually
closed (at a random GC time), regardless of what the caller does - i.e.
even if the caller forgets about interacting with the response stream or
canceling the ctx.  This kind of paranoia is not needed. The code in
question was copied from grpc-opentracing[1], which quoted a
StackOverflow answer[2] about whether or not a client is allowed to
simply walk away from a streaming call. As a result of conversations
triggered by this patch [3], that SO answer was updated to reflect the fact
that it is not, in fact, OK for a client to do so, as it will leak gRPC
resources. The client's contract is specified in [4] (although arguably
that place is not the easiest to find by a casual gRPC user). In any
case, this patch gets rid of the finalizer. This could in theory result
in leaked spans if our own code is buggy in the way that the paranoia
prevented, but all our TestServers check that spans don't leak like that
so we are pretty protected. FWIW, a newer re-implementation of the
OpenTracing interceptor[4] doesn't have the finalizer (although it also
doesn't listen for ctx cancellation, so I think it's buggy), and neither
does the equivalent OpenTelemetry interceptor[6].

Fixes #80689

[1] https://github.com/grpc-ecosystem/grpc-opentracing/blob/8e809c8a86450a29b90dcc9efbf062d0fe6d9746/go/otgrpc/client.go#L174
[2] https://stackoverflow.com/questions/42915337/are-you-required-to-call-recv-until-you-get-io-eof-when-interacting-with-grpc-cl
[3] https://github.com/grpc/grpc-go/issues/5324
[4] https://pkg.go.dev/google.golang.org/grpc#ClientConn.NewStream
[5] https://github.com/grpc-ecosystem/go-grpc-middleware/blob/master/tracing/opentracing/client_interceptors.go#L37-L52
[6] https://github.com/open-telemetry/opentelemetry-go-contrib/blame/main/instrumentation/google.golang.org/grpc/otelgrpc/interceptor.go#L193

Release note: A rare crash indicating a nil-pointer deference in
google.golang.org/grpc/internal/transport.(*Stream).Context(...)
was fixed.

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[7c61bf65f2...](https://github.com/san7890/bruhstation/commit/7c61bf65f2b3c661bf622864bb7596e0e89d1f28)
#### Wednesday 2022-05-04 01:05:13 by vincentiusvin

Makes glass floors override platings. Fixes glass floor openspace bug. (#66301)


About The Pull Request

Fixes #63868. Actual one liner fix for this one here. If this pr dies feel free to atomize this one.
AND it turns out to not be tim's fault.

Fixes #63548. But i really shouldnt say fixed. The original implementation was causing the invincible plating bug. When tim's refactor got in it instead relies on the element state, which was broken from the get go, removing the invincible plating bug which was in a sense "intended" its all messy man I hate this code. Thats why im removing the plating thing. Let the turf handle the turf change themselves this complicates things.

Mapped in glass floors have openspace (now baseturf bottom) as their baseturfs, while built ones have plating under them. Which doesnt make sense to be honest. Why would things be visible if a plating is under the glass. They are also crowbarrable on top of this, which to be fair is my main reasoning behind the PR.

To solve this, I am instead making glass floors replace the plating instead of building over it. This is made to be generalizable for every tile in game, as long as their initial baseturf is the same and the tile wants it to happen.

do after of three seconds is completely arbitrary. If any maint want it changed let me know.
Why It's Good For The Game

First one solves a bug
Second one makes more sense
And er, icebox is currently using the glass floors in sec, they can be crowbarred very easily. This might be a good idea from a gameplay perspective.
Changelog

cl
del: Removed adding glass floors to plating
balance: Allows you to replace plating with glass floors instead. 3 second timer.
del: Removed deconstructing the glass floors. No replacement for this one, use a rcd.
fix: Fixed metastation glassfloor spawning a weird turf when crowbarred.
/cl

---
## [Mu-L/crawl](https://github.com/Mu-L/crawl)@[c08b2e8bf8...](https://github.com/Mu-L/crawl/commit/c08b2e8bf8864494d43077b7622612e4c5b192df)
#### Wednesday 2022-05-04 01:36:10 by nicolae-carpathia

Add the most nicolae demonic rune vault possible (#2260)

* Add the most nicolae demonic rune vault possible

I have reached my apotheosis: I have put a rune in a shop.

Since the demonic rune repeats if you don't pick it up, I figured it
would be the best option for a rune shop. (The abyssal rune also
reappears if you don't pick it up, but the theme is easier to fit into
Pandemonium.) If you already have the rune, the shop instead places
another kind of rarity: a figurine of a ziggurat. (The only other
really rare item I could think of was a quad damage, and I've been
explicitly told multiple times that I'm not allowed to use those
outside of Sprint. Tyranny!)

Out of 25 generated shops, the stats on the price of a demonic rune:
Minimum: 3804
Maximum: 8647
Average: 6640.76
St Dev:  1412.1
I didn't check the price stats on the zigfig because the rune is the
real draw here.

The vault also places fat stacks of cash, three other shops, and
demon-summoning monsters from other branches as visitors. Enjoy!

* Make adjustments to the pan bazaar rune vault

Make some changes based on feedback from the other devs:
1) If you already have the demonic rune, instead of selling a
   zigfig, the central shop now just sells randarts. (I had
   underestimated the importance of zigfigs.)
2) The difficulty has been turned up a bit. The area outside
   the central area places more monsters now.
3) A few of the nonruniferous shops have been tweaked.

---
## [sh4hrazad/bhoptimer](https://github.com/sh4hrazad/bhoptimer)@[75ecd0ba6e...](https://github.com/sh4hrazad/bhoptimer/commit/75ecd0ba6e54c4445901f978f2e29b682ad2b9d2)
#### Wednesday 2022-05-04 02:19:21 by rtldg

AHHHHHHHHHHHHHHHHHHH GIT YOU FUCKING FAILED THE PATCH MERGE YOU PIECE OF SHIT

---
## [XiaoGeMa/spacemacs](https://github.com/XiaoGeMa/spacemacs)@[c595640a34...](https://github.com/XiaoGeMa/spacemacs/commit/c595640a344b90965bd080420f7845af65526736)
#### Wednesday 2022-05-04 02:51:03 by Daniel Nicolai

In navigation layer, Bind J/K to scroll up/down in Info-mode

Spacemacs lacks a keybinding alternative to the most natural way of scrolling
Info pages (i.e. SPC) in vanilla emacs.
Anyway, this commit adds J/K to scroll most naturally through info pages.
Currently, in Info-mode, a keybinding for J is not defined while K is bound to
evil-lookup.

Issue #2828 already adresses the inconsistent experience, and in my opinion this
can and should be improved as navigating Info pages is a very crucial part of
using Emacs.

Personally I have bound J/K to scroll page up/down in buffers/pdf/djvu/doc-view,
which I inherited from using the zathura pdf reader, and I think this is a better
default than the default vim alternatives.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[535d6ea775...](https://github.com/treckstar/yolo-octo-hipster/commit/535d6ea775f45e2bac47f2a9ca67e99e3f2f54e5)
#### Wednesday 2022-05-04 03:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [AmokDash/landing-page](https://github.com/AmokDash/landing-page)@[b94bf04125...](https://github.com/AmokDash/landing-page/commit/b94bf0412559e70917419049ee9bdea5ca9f96f2)
#### Wednesday 2022-05-04 03:31:49 by AmokDash

Add flex properties to the boxes

Still having issues to display pictures separately aka space between
them. God damn headache

Add some hight to quote menu as it was annoyingly close

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[27946f516d...](https://github.com/tgstation/tgstation/commit/27946f516dd77faa071576499bb700c6fa22fbab)
#### Wednesday 2022-05-04 05:33:39 by san7890

Update Comments and Adjusts Incorrect Variables for Map Defines and Map Config (#66540)

Hey there,

These comments were really showing their age, and they gave the false impression that nothing had changed (there was a fucking City of Cogs mention in this comment!). I rewrote a bit of that, and included a blurb about using the in-game verb for Z-Levels so people don't get the wrong impressions of this quick-reference comment (they always do).

I also snooped around map_config.dm and I found some irregularities and rewrote the comments there to be a bit more readable (in my opinion). Do tell me if I'm a cringe bastard for writing what I did.

Also, we were using the Box whiteship/emergency shuttle if we were missing the MetaStation JSON. Whoops, let's make sure that's fixed.

People won't have to wander in #coding-general/#mapping-general asking "WHAT Z-LEVEL IS X ON???". It's now here for quick reference, as well as a long-winded section on why you shouldn't trust said quick reference.

---
## [FreshROMs/android_kernel_samsung_exynos9610_mint](https://github.com/FreshROMs/android_kernel_samsung_exynos9610_mint)@[1fee34fb08...](https://github.com/FreshROMs/android_kernel_samsung_exynos9610_mint/commit/1fee34fb08a6717feeb13c76a697b22bd45bb2d1)
#### Wednesday 2022-05-04 06:03:52 by Peter Zijlstra

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
Signed-off-by: John Vincent <git@tenseventyseven.cf>

---
## [AmokDash/landing-page](https://github.com/AmokDash/landing-page)@[82f00e15b7...](https://github.com/AmokDash/landing-page/commit/82f00e15b772a33544e34aa95dbb36eeed28e9b9)
#### Wednesday 2022-05-04 06:26:45 by AmokDash

Push style on box section and remove my patience

Gods...the flexbox stuff is kicking me...I spent on thing portion of the
webiste more time that I wanted.

First, h2 was under flexbox, but it was a f headache. It was messy, so
displayed as block and aligned at the center.

Second, the images part...well, it was hard to make them perfect
but it looks great, + add
transition for those sick styling.

Then, some hover over image.

And flexbox...I lost all my nerves on that thing and still code looks
like a code monkey got himself free from the cage! If remove box section
flexbox property - everything going to be messed up! Than, going to box
classes itself - ok, I got it for some magical reason it did not want to
do it easy way and I have to be a shaman with a drum, jumping around
this section like a madlad. Whoever will be reading that - know that I
spent entire evening to just make it right.

There were different options to style them as they are sitting now, but
all of them were bad and ugly. Sure, code looks like a mess, but hey -
if it's working, it's not stupid.

Holly Jesus, what an experience.

Though, I learned a lot and read about different options and even tried
them.

---
## [99rgosse/gitea](https://github.com/99rgosse/gitea)@[3725fa28cc...](https://github.com/99rgosse/gitea/commit/3725fa28ccc01ab08060f591f894ea6443a348e8)
#### Wednesday 2022-05-04 06:40:46 by Gusted

Improve UI on mobile (#19546)

Start making the mobile experience not painful and be actually usable. This contains a few smaller changes to enhance this experience.

- Submit buttons on the review forms aren't columns anymore and are now allowed to be displayed on one row.
- The label/milestone & New Issue buttons were given each own row even tough, there's enough place to do it one the same row. This commit fixes that.
- The issues+Pull tab on repo's has a third item besides the label/milestone & New Issue buttons, the search bar. On desktop there's enough place to do this on one row, for mobile it isn't, currently it was using for each item a new row. This commits fixes that by only giving the searchbar a new row and have the other two buttons on the same row.
- The notification table will now be show a scrollbar instead of overflow.
- The repo buttons(Watch, Star, Fork) on mobile were showing quite big and the SVG wasn't even displayed on the same line, if the count of those numbers were too high it would even overflow. This commit removes the SVG, as there isn't any place to show them on the same row and allows them to have a new row if the counts of those buttons are high.
- The admin page can show you a lot of interesting information, on mobile the System Status + Configuration weren't properly displayed as the margin's were too high. This commit fixes that by reducing the margin to a number that makes sense on mobile.
- Fixes to not overflow the tables but instead force them to be scrollable.
- When viewing a issue or pull request, the comments aren't full-width but instead 80% and aligned to right, on mobile this is a annoyance as there isn't much width to begin with. This commits fixes that by forcing full-width and removing the avatars on the left side and instead including them inline in the comment header.

---
## [pawan-deepsource/msbuild](https://github.com/pawan-deepsource/msbuild)@[a572dc6b79...](https://github.com/pawan-deepsource/msbuild/commit/a572dc6b796aec7d028e53aa24a82a059e47edfa)
#### Wednesday 2022-05-04 07:41:52 by Forgind

Fix low priority issues (#7413)

Thanks @svetkereMS for bringing this up, driving, and testing.

This fixes two interconnected issues.
First, if a process starts at normal priority then changes to low priority, it stays at normal priority. That's good for Visual Studio, which should stay at normal priority, but we relied on passing priority from a parent process to children, which is no longer valid. This ensures that we set the priority of a process early enough that we get the desired priority in worker nodes as well.

Second, if we were already connected to normal priority worker nodes, we could keep using them. This "shuts down" (disconnects—they may keep running if nodeReuse is true) worker nodes when the priority changes between build submissions.

One non-issue (therefore not fixed) is connecting to task hosts that are low priority. Tasks host nodes currently do not store their priority or node reuse. Node reuse makes sense because it's automatically off always for task hosts, at least currently. Not storing low priority sounds problematic, but it's actually fine because we make a task host—the right priority for this build, since we just made it—and connect to it. If we make a new build with different priority, we disconnect from all nodes, including task hosts. Since nodeReuse is always false, the task host dies, and we cannot reconnect to it even though if it didn't immediately die, we could, erroneously.

On the other hand, we went a little further and didn't even specify that task hosts should take the priority assigned to them as a command line argument. That has been changed.

svetkereMS had a chance to test some of this. He raised a couple potential issues:

conhost.exe launches as normal priority. Maybe some custom task dlls or other (Mef?) extensions will do something between MSBuild start time and when its priority is adjusted.
Some vulnerability if MSBuild init code improperly accounts for timing
For (1), how is conhost.exe related to MSBuild? It sounds like a command prompt thing. I don't know what Mef is.
For (2), what vulnerability? Too many processes starting and connecting to task hosts with different priorities simultaneously? I could imagine that being a problem but don't think it's worth worrying about unless someone complains.

He also mentioned a potential optimization if the main node stays at normal priority. Rather than making a new set of nodes, the main node could change the priority of all its nodes to the desired priority. Then it can skip the handshake, and if it's still at normal priority, it may be able to both raise and lower the priority of its children. Since there would never be more than 2x the "right" number of nodes anyway, and I don't think people will be switching rapidly back and forth, I think maybe we should file that as an issue in the backlog and get to it if we have time but not worry about it right now.

Edit:
I changed "shuts down...worker nodes when the priority changes" to just changing their priority. This does not work on linux or mac. However, Visual Studio does not run on linux or mac, and VS is the only currently known customer that runs in normal priority but may change between using worker nodes at normal priority or low priority. This approach is substantially more efficient than starting new nodes for every switch, disconnecting and reconnecting, or even maintaining two separate pools for different builds.

---
## [RayAnor/Skyrat-tg](https://github.com/RayAnor/Skyrat-tg)@[a0fa5ba3ce...](https://github.com/RayAnor/Skyrat-tg/commit/a0fa5ba3ce25d019dafa88e1d606e079f7649cc6)
#### Wednesday 2022-05-04 07:42:03 by SkyratBot

[MIRROR] Updates Maps And Away Missions MD [MDB IGNORE] (#13095)

* Updates Maps And Away Missions MD (#66455)

* Updates Maps And Away Missions MD

Hey there,

This was outdated for a bit, so I decided to pretty it up and make a few things a bit more explicit.

I alphabetized the maps since we don't really prioritize one-over-the-other (except Meta now being the default map instead of the non-existent Box).

I also alphabetized Removed Station Maps, and removed the "outdated" (they are all outdated, or will definitely all be outdated by the time a reader reads this).

I elaborated a bit more on how station maps are loaded these days (correct me if I am wrong).

Standardized how we show code paths.

Gave explicit instructions on never using Dream Maker to map, and linking two programs that we tell anyone who wanders in on the Discord to use anyways (please do inform me if we should not do this- but Dream Maker just fucking sucks shit).

I also fixed up some language around the Away Missions part, and added a newer section for the Map Depot since I do not believe it is discussed elsewhere on the main repository (as well as a short warning on anyone who things they can get Phobos or something running out-of-the-box).

Alright, cool.

* Updates Maps And Away Missions MD

Co-authored-by: san7890 <34697715+san7890@users.noreply.github.com>

---
## [RoundtableHold/roundtablehold.github.io](https://github.com/RoundtableHold/roundtablehold.github.io)@[07161f103d...](https://github.com/RoundtableHold/roundtablehold.github.io/commit/07161f103d851b6b863d25c50950515adf1a007b)
#### Wednesday 2022-05-04 07:50:02 by Olivia

Landmarks Overhaul pt 1

- The Evergaols and Legacy Dungeons pages are completely gone. I removed the yaml and html files. Their progress will be lost.
- The Caves page has been completely redone to become a Landmarks page. The page has been renamed to Landmarks & Locations and the yaml is renamed to landmarks.yaml. The id is still caves so that progress from Caves, Catacombs, and Tunnels is preserved on this new page.
- Content from the two deleted pages has been moved to the Landmarks page. Their ids now follow new conventions to not clash with the existing Caves ids: "e1" - "e10" for evergaols, and "ld1" - "ld14" for legacy dungeons.
- The Location column and description for all preexisting items on the Landmarks page have been removed. It will be made obsolete by map links to every location, though these are not yet implemented.
- Every location in the game that generates a landmark on the in-game map now has an entry on the Landmarks page, dramatically extending the page. For the most part, these new entries don't have notes or other info that'd be good to add yet, but they do all have their correct icons, unless I made any mistakes. Landmarks follow the id convention "l1" - "l130". I think I got all of them, but there's 130 and no list in the game to compare against, so I welcome double and triple checkers.
- The Landmarks page is sorted by location as the Caves page was, with all other integrated items sorted into their places.
- Within region sections, I sorted the locations into consistent orders as best I could, but they will likely need reordering. My order within a region is Caves, Catacombs, Tunnels, Hero's Graves, Evergaols, Minor Erdtrees, Divine Towers, Puzzle Towers, Ruins, Shacks, Churches, Unique, and Legacy Dungeons. I enforced this order with commenting in every section.
- The original Caves page was missing two: Sellia Hideaway and Auriza Side Tomb. These have been added.
- I changed Fort Haight from a legacy dungeon to a simple landmark. Calling it a legacy dungeon seemed a pretty extreme stretch, especially when all other (sometimes bigger) Forts weren't.
- In other tweaks, I renamed rememberances.yaml to be spelled correctly, remembrances.yaml. The page title was spelled correctly, so the html name didn't change and any links should be preserved.
- I moved Incantations below Sorceries in the list of pages, just because it seemed silly that we have Incantations on top when Sorceries are always listed first in-game.
- Next up is linking the locations of all these new Landmarks.

---
## [ScriptBox99/WindowsTerminal](https://github.com/ScriptBox99/WindowsTerminal)@[446f280757...](https://github.com/ScriptBox99/WindowsTerminal/commit/446f2807573ffda411f548a519835d15cacdcd9b)
#### Wednesday 2022-05-04 07:50:48 by Mike Griese

Try to silently fall back to a local monarch (#12825)

This is a crazy idea Dustin and I had.

> we can't repro this at will. But we kinda have an idea of where the deref is. We don't know if the small patch (throw, and try again) will fix it. We're sure that the "just fall back to an isolated monarch" will work. I'd almost rather take a build testing the small patch first, to see if that works

> This might seem crazy
> in 1.12, isolated monarch. In 1.13, "small patch". In 1.14, we can wait and see

I can write more details in the morning. It's 5pm here so if we want this today, here it is.

@dhowett double check my velocity flag logic here. Should be always true for Release, and off for Dev, Preview. 

* [x] closes #12774

---
## [ProjectKasumi/android_vendor_kasumi](https://github.com/ProjectKasumi/android_vendor_kasumi)@[68a09d15cb...](https://github.com/ProjectKasumi/android_vendor_kasumi/commit/68a09d15cbd97fa5340a606318d2d2e09be2b38b)
#### Wednesday 2022-05-04 07:59:04 by Beru Shinsetsu

Launch 1.2 Stable

Eh, this one was a quick update with some little feature additions.

Let's see what do we have here this time.

1- We're now on Discord and left Telegram into oblivion. Settings
   will now show Discord invite code instead of Telegram chat tag
   to avoid confusion.
2- We have done some little change on TARGET_BOOT_ANIMATION_RES
   definition and made a much better implementation for it,
   considering devices coming from Lineage and other ROMs using
   Lineage implementation for boot animation. I tested it and it
   works.
3- Upon request, offline charging animation seen in Google Pixel
   devices and Pixel Experience has been added. Botan Yuukan, Ocean
   maintainer, said she tested it and that it works.
4- Merged in April 2022 ASB and this is the first ASB that we didn't
   change SafetyNet spoofing fingerprints for. Finally no more failing
   SafetyNet after ASB upstreams! Yay!

For those asking for Android 12(L), I'm going to start working on it
as soon as possible. I'm still working at halogenOS 12.1, and I'm
really stuck at some point. If someone wants to see what's going on
and help me in our Discord server, either sync the sources and try to
build it or ping me there so I can sync, retry and send you the
screenshot of the errors. "ROM derp"ers, I know it's ROM derp, it's
my own derp and I'm trying to fix it. Please stay away from saying
it.

Another news is Sakura's death. Yes, sadly, Project Sakura is now
dead, and I now have a much more important position considering
how Sakura and Kasumi had similar types of designs on common parts
like Settings. Their commits were helping me, and several of my
commits were helping them. Sad to see them go...

Now, CI jobs for v1 will run again and release OTAs. Let's see how
it goes!

Signed-off-by: Beru Shinsetsu <windowz414@1337.lgbt>

---
## [AnmolS1/SpamStudy](https://github.com/AnmolS1/SpamStudy)@[7f4fd6b22b...](https://github.com/AnmolS1/SpamStudy/commit/7f4fd6b22b6e8872fabcffd280e4a08ee48788dc)
#### Wednesday 2022-05-04 08:01:51 by Anmol Saxena

more done

finished tidying the data, it's practically ready to upload to the cloud. i'll make changes based on whatever dr. munyaka wants tomorrow. final step is uploading the data to the ibm database. honestly this was incredible. i haven't slept since sunday night (it's wednesday morning now), and i've hardly eaten. it's just been pushing and pushing to get this done before monday next week, and it looks like i just might be able to do this And get all my other work done. props to me lol.

---
## [lostnet/couchdb](https://github.com/lostnet/couchdb)@[9b6454b81c...](https://github.com/lostnet/couchdb/commit/9b6454b81ca1a599da1f538548dc67654b6ce8d7)
#### Wednesday 2022-05-04 08:29:00 by Adam Kocoloski

Refactor Jenkins build to dynamically generate test stages (#3903)

This is one of those situations where you go in to make a small change,
see an opportunity for some refactoring, and get sucked into a rabbit
hole that leaves you wondering if you have any idea how computers
actually work. My initial goal was simply to update the Erlang version
used in our binary packages to a modern supported release. Along the
way I decided I wanted to figure out how to eliminate all the copypasta
we generate for making any change to this file, and after a few days of
hacking here we are. This rewrite has the following features:

* Updates to use Debian 11 (current stable) as the base image for
  building releases and packaging repos.

* Defaults to Erlang 24.2 as the embedded Erlang version in packages.

* Dynamically generates the parallel build stages used to test and
  package CouchDB on various OSes. This is accomplished through a bit
  of scripted pipeline code that relies on two new methods defined at
  the beginning of the Jenkinsfile, one for "native" builds on macOS
  and FreeBSD and one for container-based builds. See comments in the
  Jenkinsfile for additional details.

* Expands commands like `make check` into a series of steps to improve
  visibility. The Jenkins UI will now show the time spent in each step
  of the build process, and if a step (e.g. `make eunit`) fails it will
  only expand the logs for that step by default instead of showing the
  logs for the entire build stage. The downside is that if we do make
  changes to the series of targets underneath `check` we need to
  remember to update the Jenkinsfile as well.

* Starts per-stage timer _after_ agent is acquired. Previously builds could
  fail with a 15m timeout when all they did was sit in the build queue.

---
## [paulgessinger/acts](https://github.com/paulgessinger/acts)@[6e1fd31474...](https://github.com/paulgessinger/acts/commit/6e1fd314745ae31eaddd8db8f0454b88a9aa60fa)
#### Wednesday 2022-05-04 13:14:21 by Stephen Nicholas Swatman

feat: Implement a new orthogonal range search seed finder (#904)

As I said in #901, I have been playing around with seed finding a little bit lately. Last weekend, I mentioned an idea for a new (?) kind of seed finding algorithm based on range search datastructures, and this is the very, very first semi-working implementation of it, just before the weekend.

The idea behind this algorithm is relatively simple. In traditional seedfinding, we check a whole lot of candidate spacepoints to see whether they meet some condition. If you look at this differently, each spacepoint defines a volume in the z-r-φ space, which contains any spacepoints it can form a doublet with. What if we reversed this logic? What if we defined this volume first, and then just extract the spacepoints inside of that space? That way, we can vastly reduce the number of spacepoints we need to look at.

How do we do this quickly? With [_k_-d trees](https://en.wikipedia.org/wiki/K-d_tree). These data structures are cheap to build, and they give us very fast orthogonal range searches. In other words, we can very quickly look up which of our spacepoints lie within an axis-aligned orthognal n-dimensional hyperrectangle. In this case, which spacepoints lie within a z-r-φ box.

So, the core idea of this seedfinder is to define as many of our seedfinding constraints in orthogonal fashion. That way, we can make our candidate hyperrectangle smaller and smaller. The tighter the constraints we can place, the better. Then, we look up the relevant spacepoints, and we can avoid looking at any others. That also means this solution requires no binning whatsoever.

## Constraint conversion

Currently there are quite a few constraints in the code. Here is my status update on how well it is going to convert each of them. In some cases, we can define a weaker version of the constraints in orthogonal fashion. This is still very powerful, and it doesn't actually lose us any efficiency (because we can always check the tighter constraint in a non-orthogonal way later, not a problem)!

### Unary constraints

Currently, I am not aware of any unary constraints in the Acts seed finding code. That is to say, logic to determine whether a point is allowed to be a lower spacepoint. However, I have the following thoughts about introducing some:

* I believe the binning code does some kind of magic to determine whether a spacepoint can be a lower spacepoint. Since my solution doesn't use any binning, I don't have access to this just yet. However, if we can incorporate this logic it could be very powerful.
* Maximum single-point η: we currently have some checks in place to see if the pseudorapidity of particles is not too high. We could realistically use this maximum pseudorapidity, combined with the collision region range to constrain the bottom spacepoints.

### Binary constraints

These are the existing binary constraints on spacepoint duplets:

Constraint | Description | Orthogonalization
-|-|-
Minimum ∆r | Ensure that the second spacepoint is within a certain difference in radius | Full
Maximum cot θ | Ensure that the pseudorapidity of the duplet is not too high | Unsuccessful
z-origin range | Ensure that the duplet would have originated from the collision point | Weakened 
Maximum ∆φ<sup>1</sup> | Ensure that the duplet does not bend too much in the x-y plane | Full

<sup>1</sup> This check does not exist explicitly in the existing seed finder, but is implicit in the binning process.

### Ternary constraints

There are a lot of ternary constraints (to check whether a triplet is valid):

Constraint | Description | Orthogonalization
-|-|-
Scattering angle | ??? | Unsuccessful
Helix diameter | Ensure the helix diameter is within some range | In progress
Impact parameters | Ensure the impact parameters are close to the collision point | In progress
Monotonic z<sup>1</sup> | Ensure that z increases or decreases monotonically between points | Full

<sup>1</sup> This check does not exist in the existing seed finder, check #901.

There are also constraints defined in the experiment-specific cuts, and the seed filter, and in other places. If we could convert some of those to orthogonal constraints the implementation would become much more powerful. However, I don't really understand what is happening in those files just yet. Need more reading.

## Current performance

The current performance of this seedfinder is... Complicated. On my machine, it runs a 4000 π<sup>+</sup> event in about 5 seconds, three times slower than the existing seedfinder. Its efficiency is much higher though, and the fake rate is much lower. So that's something. However, that is in part because I am creating far more seed candidates, so take this with a big grain of salt.

## Potential gain

There are two ways that I can think of to use this kind of algorithm. The first is an inside-to-outside algorithm, where we pick a lower spacepoint first, check the space it defines for a middle spacepoint, and then check the space the two of them define for a third spacepoint. This algorithm has time complexity 𝒪(_n_<sup>3</sup>), and it has space complexity 𝒪(_n_). Due to the constants, I still believe this implementation can outperform the 𝒪(_n_<sup>2</sup>) existing algorithm, however.

The second way would be to construct a set of duplets using this logic, and then to fit those together like we do with traditional seedfinding. This has 𝒪(_n_<sup>2</sup>) time complexity like the existing code, but also space complexity 𝒪(_n_<sup>2</sup>).

## Things that are completed

* The implementation of the _k_-d tree seems to work very well, and it is quite fast.
* Basic seedfinding using this strategy is functional.

## Things that don't work yet

* My maximum ∆φ constraint does not cross the 2π boundary yet.
* I used the existing seedfinding algorithm as a stepping stone, which I have completely destroyed in the process. Obviously I do not intend on keeping it that way, and the existing algorithm will be restored to its full glory.
* Lots more.

## Things that can be improved

* Add more constraints, and tighten existing ones.
* Lots of things, pretty much everything. But I really want to go home for the weekend, so I will write this part next week.

---
## [citizenfx/fivem](https://github.com/citizenfx/fivem)@[6051b8790c...](https://github.com/citizenfx/fivem/commit/6051b8790c185b2435da75c2f41f59ec3be4578f)
#### Wednesday 2022-05-04 13:53:03 by blattersturm

Revert "tweak(client/core): nvidia, fuck you."

The gift that keeps on giving: NVIDIA drivers. Some users seem to crash
in new places with `disable.txt` present and used.

Seriously?!

This reverts commit 02df4a52b1dba9b56a89b10bf59be7c9ff79c0d9.

---
## [Vito-Research/podman](https://github.com/Vito-Research/podman)@[e74717f348...](https://github.com/Vito-Research/podman/commit/e74717f348c2768b87cad7dd6997c42dc85fc50a)
#### Wednesday 2022-05-04 16:41:19 by Ed Santiago

Treadmill script: revamp

Major revamp: instead of stacking a vendor commit on top of
the treadmill changes, do it the other way around: vendor,
then apply treadmill diffs.

Reason: the build-all-new-commits test. Sigh. It fails in the
common case where our treadmill changes include a new struct
element in cmd/podman/images/build.go

Why this is good: well, superficially, it's more intuitive.

Why this is horrible: omg the rebasing games are a nightmare.
When the vendor commit is on top (HEAD), it's ultra-trivial
to drop it, rebase the treadmill changes on main, then add
a new vendor-buildah commit on top. As you can see from the
diffs in this PR, treadmill-as-HEAD introduces all sorts
of complex dance steps in which things can go catastrophically
wrong and you can lose all your treadmill patches. I try very
hard to prevent this, and to offer hints if there's a problem,
and heck in the worst case it's still git so it's still possible
to find lost commits... but it's still much riskier than the
old way.

Alternative I considered: using sed magic to disable the
build-all-new-commits test. So tempting... but that would
also disable the bloat check.

Signed-off-by: Ed Santiago <santiago@redhat.com>

---
## [LoganDark/luajit-argon2](https://github.com/LoganDark/luajit-argon2)@[cbe3aa8a58...](https://github.com/LoganDark/luajit-argon2/commit/cbe3aa8a5849a9c37b9033159b3751b45e7094fb)
#### Wednesday 2022-05-04 18:23:34 by LoganDark

Correct the worst most obvious typo ever

Let's be honest, this package will never see another release, and this
typo will never actually be corrected because I don't want to publish a
patch release just for the stupid abstract.

I hate my life.

---
## [cminyard/linux-ipmi](https://github.com/cminyard/linux-ipmi)@[213d266ebf...](https://github.com/cminyard/linux-ipmi/commit/213d266ebfb1621aab79cfe63388facc520a1381)
#### Wednesday 2022-05-04 18:38:21 by Linus Torvalds

gpiolib: acpi: use correct format characters

When compiling with -Wformat, clang emits the following warning:

  gpiolib-acpi.c:393:4: warning: format specifies type 'unsigned char' but the argument has type 'int' [-Wformat]
                        pin);
                        ^~~

So warning that '%hhX' is paired with an 'int' is all just completely
mindless and wrong. Sadly, I can see a different bogus warning reason
why people would want to use '%02hhX'.

Again, the *sane* thing from a human perspective is to use '%02X. But
if the compiler doesn't do any range analysis at all, it could decide
that "Oh, that print format could need up to 8 bytes of space in the
result". Using '%02hhX' would cut that down to two.

And since we use

        char ev_name[5];

and currently use "_%c%02hhX" as the format string, even a compiler
that doesn't notice that "pin <= 255" test that guards this all will
go "OK, that's at most 4 bytes and the final NUL termination, so it's
fine".

While a compiler - like gcc - that only sees that the original source
of the 'pin' value is a 'unsigned short' array, and then doesn't take
the "pin <= 255" into account, will warn like this:

  gpiolib-acpi.c: In function 'acpi_gpiochip_request_interrupt':
  gpiolib-acpi.c:206:24: warning: '%02X' directive writing between 2 and 4 bytes into a region of size 3 [-Wformat-overflow=]
       sprintf(ev_name, "_%c%02X",
                            ^~~~
  gpiolib-acpi.c:206:20: note: directive argument in the range [0, 65535]

because gcc isn't being very good at that argument range analysis either.

In other words, the original use of 'hhx' was bogus to begin with, and
due to *another* compiler warning being bad, and we had that bad code
being written back in 2016 to work around _that_ compiler warning
(commit e40a3ae1f794: "gpio: acpi: work around false-positive
-Wstring-overflow warning").

Sadly, two different bad compiler warnings together does not make for
one good one.

It just makes for even more pain.

End result: I think the simplest and cleanest option is simply the
proposed change which undoes that '%hhX' change for gcc, and replaces
it with just using a slightly bigger stack allocation. It's not like
a 5-byte allocation is in any way likely to have saved any actual stack,
since all the other variables in that function are 'int' or bigger.

False-positive compiler warnings really do make people write worse
code, and that's a problem. But on a scale of bad code, I feel that
extending the buffer trivially is better than adding a pointless cast
that literally makes no sense.

At least in this case the end result isn't unreadable or buggy. We've
had several cases of bad compiler warnings that caused changes that
were actually horrendously wrong.

Fixes: e40a3ae1f794 ("gpio: acpi: work around false-positive -Wstring-overflow warning")
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>

---
## [postgres/postgres](https://github.com/postgres/postgres)@[c40ba5f318...](https://github.com/postgres/postgres/commit/c40ba5f318f96a6a5a29729b987ead11c5dc65c1)
#### Wednesday 2022-05-04 18:45:15 by Tom Lane

Fix rowcount estimate for SubqueryScan that's under a Gather.

SubqueryScan was always getting labeled with a rowcount estimate
appropriate for non-parallel cases.  However, nodes that are
underneath a Gather should be treated as processing only one
worker's share of the rows, whether the particular node is explicitly
parallel-aware or not.  Most non-scan-level node types get this
right automatically because they base their rowcount estimate on
that of their input sub-Path(s).  But SubqueryScan didn't do that,
instead using the whole-relation rowcount estimate as if it were
a non-parallel-aware scan node.  If there is a parallel-aware node
below the SubqueryScan, this is wrong, and it results in inflating
the cost estimates for nodes above the SubqueryScan, which can cause
us to not choose a parallel plan, or choose a silly one --- as indeed
is visible in the one regression test whose results change with this
patch.  (Although that plan tree appears to contain no SubqueryScans,
there were some in it before setrefs.c deleted them.)

To fix, use path->subpath->rows not baserel->tuples as the number
of input tuples we'll process.  This requires estimating the quals'
selectivity afresh, which is slightly annoying; but it shouldn't
really add much cost thanks to the caching done in RestrictInfo.

This is pretty clearly a bug fix, but I'll refrain from back-patching
as people might not appreciate plan choices changing in stable branches.
The fact that it took us this long to identify the bug suggests that
it's not a major problem.

Per report from bucoo, though this is not his proposed patch.

Discussion: https://postgr.es/m/202204121457159307248@sohu.com

---
## [EasyCorp/EasyAdminBundle](https://github.com/EasyCorp/EasyAdminBundle)@[919545baeb...](https://github.com/EasyCorp/EasyAdminBundle/commit/919545baebcf0b7ae1f8a35210afc4bd92769161)
#### Wednesday 2022-05-04 18:46:28 by Javier Eguiluz

feature #5066 Allow `Translatable` objects in addition to `string` in translated context (Lustmored)

This PR was squashed before being merged into the 4.x branch.

Discussion
----------

Allow `Translatable` objects in addition to `string` in translated context

This PR is pretty massive, yet almost all of it's code changes are just enablers for features that are already in Symfony Forms (5.4+) and Symfony Translation (also 5.4+). It allows passing `Translatable` objects as labels and other parts.

### Background

Currently my main problem with EasyAdmin is translation extraction. I maintain pretty large project where translation extraction is build into workflow very tightly and using manual extraction is unmaintainable. Fortunately most translations in admin context have no parameters, so I can workaround that by doing:
```
yield TextField::new('name', (string) t('Client name'));
```
But that's just a dirty hack and works only when label needs no parameters to translate properly. This is why I would benefit greatly if EasyAdmin would simply allow those objects internally and I think other users would welcome it too :smiley:

I have tested those changes on real life projects and they worked like a charm :smile:

### Complexity (?)

As stated before most of the changes are just enablers. By just changing some signatures and adding very simple logic whenever EasyAdmin translates content I was able to pass `Translatable` objects to templates and Symfony Forms, where they handle it without any additional work.

### Backwards compatibility

Functional backwards compatibility is kept. By that I mean - if project uses strings in those contexts (or leaves them empty for Easy Admin to fill with default values), no incompatibility arises. Setters accept strings as before and getters will return those strings. Also - everything will be translated, as before.

Unfortunately the same cannot be said about class signatures. Summary of signature changes are as follows:

Final classes with signature changes:

- Config\Action (new, setLabel); only docblocks and deprecation logic
- Config\Menu\*MenuItem (constructors)
- Config\MenuItem (linkTo*, section, subMenu)
- Dto\ActionDto (getLabel, setLabel and private field)
- Dto\CrudDto (getEntityLabelInSingular, setEntityLabelInSingular,getEntityLabelInPlural, setEntityLabelInPlural, setCustomPageTitle, getHelpMessage, setHelpMessage)
- Dto\FieldDto (getLabel, setLabel, getHelp, setHelp)
- Dto\FilterDto (getLabel, setLabel); only docblocks
- Dto\MenuItemDto (getLabel, setLabel)
- Field\*Field (new); only docblocks
- Field\FormField (addPanel, addTab)

Non-final classes with signature changes:

- Config\Crud (setHelp)
- Field\FieldTrait (setLabel, setHelp); setLabel only in docblock

I wouldn't consider signature changes in setters in final classes as BI, but getters are - end user code might expect getter to return `?string`, while this PR changes it to `TranslatableInterface|string|null`. Again - in simple use case, where user is not using `Translatable` objects this assumption will still hold. But libraries, bundles and other code does not have such guarantee.

Also one non-final class and commonly used trait have signature changes in parameter types that will raise errors when inherited.

I don't see any way we can achieve the same without breaking BC, therefore I think this change can only target `5.0`. But I'd love to hear from the others :)

### TODO

- [x] get feedback
- [x] write tests for functional changes (probably just translating part, there is no point in testing getters and setters IMO)
- [x] Add UPGRADE/CHANGELOG entry documenting changes

Commits
-------

7596f24f Allow `Translatable` objects in addition to `string` in translated context

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[183902336f...](https://github.com/mrakgr/The-Spiral-Language/commit/183902336fbbfa9352c9d25c763476d3cc54cd61)
#### Wednesday 2022-05-04 18:51:28 by Marko Grdinić

"9:30am. Let me get started since I've already started obsessing about it. I just can't find the ideal style that has precision of NURBs, and the flexibility of sculpting. Right now what is giving me trouble is how to do cut outs.

9:40am. https://youtu.be/1PE-NUBWPrw
Blender 2 80 - Hole On Curved Surface. SubD Modeling.

Remember that hole Arrimus did on the cable. I am trying to do it now and am getting confused as to how I could do it. I keep getting a mess.

https://youtu.be/HfTdQNECvtU?t=16

Yeah, what is the best way to do these side holes. I know Arrimus just planared them, but what I tried that, that gave me duplicated edges. Let me change things a bit. I am being retarded. After that I'll watch the vid.

https://youtu.be/HfTdQNECvtU?t=189

Yeah, this is what I did. Arrimus said he did a bevel, but he most likely did an inset instead.

I am having a certain iadea how to deal with corners. Maybe if...

Let me first watch the video.

https://youtu.be/HfTdQNECvtU?t=206

I am surprised he it outright deleting the faces. I thought he would just scale to the bottom and merge verts.

https://youtu.be/HfTdQNECvtU?t=226

Oh, I completely forgot about the f2 addon.

But this trick would only work for cubes.

https://youtu.be/HfTdQNECvtU?t=307

Oh, it completely slipped my mind that it is possible to place loops like this. to straighten out the corners.

10:15pm. Interesting vid. He says that booleans aren't hard surface modeling, but sketching.

https://youtu.be/8ihNsjiFhQI?list=PLoSyNsQF2hFBk6_lEES7IYlEdEt3ihB-f&t=12

Let me watch this.

https://www.youtube.com/playlist?list=PLoSyNsQF2hFBk6_lEES7IYlEdEt3ihB-f
Subdivision surface modelling in Blender 3

This is a series worth going through. Subdiv modeling is the kind of subject that seems simple, but is not.

https://youtu.be/8ihNsjiFhQI?list=PLoSyNsQF2hFBk6_lEES7IYlEdEt3ihB-f&t=16

The topology is excellent. How did he do the cut on the side?

https://youtu.be/8ihNsjiFhQI?list=PLoSyNsQF2hFBk6_lEES7IYlEdEt3ihB-f&t=267

> The process of fixing it by moving points will get you nowhere to usable geometry.

Yeah, I know that what Blender bros are shilling is wrong and they'd be better off using Moi for that kind of style.

https://youtu.be/8ihNsjiFhQI?list=PLoSyNsQF2hFBk6_lEES7IYlEdEt3ihB-f&t=305

Had no idea about Shift + Alt + S.

10:30am. https://youtu.be/8ihNsjiFhQI?list=PLoSyNsQF2hFBk6_lEES7IYlEdEt3ihB-f&t=530

Change of plans. These techniques are all something I should know, but don't. Let me dedicate time to studying thme.

https://youtu.be/8ihNsjiFhQI?list=PLoSyNsQF2hFBk6_lEES7IYlEdEt3ihB-f&t=618

I am confused at what the flatten is doing.

https://youtu.be/8ihNsjiFhQI?list=PLoSyNsQF2hFBk6_lEES7IYlEdEt3ihB-f&t=904

This guy is way better than me. I am 7 months in, and it seems only now am I learning the modeling basics. Just what have I been doing?

10:40am. I just realized something. Extrusion has dissolve orthogonal edges which can be used to extrude inwards at the corners.

10:50am. https://youtu.be/PmFhBo0eVcM?list=PLoSyNsQF2hFBk6_lEES7IYlEdEt3ihB-f

Let me go at it from the start.

https://youtu.be/PmFhBo0eVcM?list=PLoSyNsQF2hFBk6_lEES7IYlEdEt3ihB-f&t=126

Yeah, I should have had orbit around selection turned on.

10:55am. When he did that shrinkwrap projection in order to extrude the shape, I realized than that it was the correct answer for how to match the shape that I desired. Maybe it did work on the boolean'd model, but it would have worked if I applied the subdiv mod on a copy and did some sculpting on it. It would have been so much easier than what I'd been doing.

Actually, did he apply the shrinkwrap. I am a bit confused? Did he use the shrinkwrap just to move the original verts?

https://youtu.be/8ihNsjiFhQI?list=PLoSyNsQF2hFBk6_lEES7IYlEdEt3ihB-f&t=725

He got rid of the modifier and then applied the shrinkwrap project. It has a setting for subdivs that I did not understand, but really should have.

Let me go back to the first video here.

11:05am. I should have done this long ago. Every time I start up Blender I delete the came, the light and join the timeline at the bottom. Also turning on selectability to good. These are all good tips, and I am surprised I hadn't done this earlier. Did Covid permanently impair my inteligence or something?

11:50am. Had to take a break. I think rather than there being 4 styles of modling, I should just separate them into 2: sketching and modeling.

Before I resume the video, let me get a grip on shrinkwrap mod.

I can't figure out a good test for it, but I am guessing the shrinkwrap subdiv level applies subdiv, projects, and then unsubdivides.

Hmmm, you can get back to the original cube, but it will be severely shrunken.

https://youtu.be/1C9z1CwZWEQ
Shrinkwrap for PERFECT shading in Blender

This one is by Josh. There is a chance of giving me what I want.

12:15pm. I can't find it. But I think that it subdiving, projecting and unsubdiving is a good bet. I doubt it is using the same unsubdiv scheme as decimate. Surpringly doing it manually on nested cubes gives a perfect result anyway. By that I mean, create two duplicate cubes that overlap, scale one so it is inside, subdiv it, project, apply the project, remove the subdiv and you get a perfect match with the other cube.

https://youtu.be/PmFhBo0eVcM?list=PLoSyNsQF2hFBk6_lEES7IYlEdEt3ihB-f&t=434

Oh, there is a make planar faces in clean up.

https://youtu.be/LVeQkKh5z1w?list=PLoSyNsQF2hFBk6_lEES7IYlEdEt3ihB-f&t=639

Instead of doing that, he could have added the Weld modifier.

https://youtu.be/aRSVYFrRWeU?t=263

What a pain in the ass. No way will I remember this. Why didn't To Sphere do a perfect job.

https://youtu.be/pWOh9cWwYqU?t=184

I wouldn't have thought of deleting the face and doing a grid fill.

https://youtu.be/pWOh9cWwYqU?t=254

Another new use for inset. I would have done a loop cut and beveled it. But this way is better.

1pm. https://youtu.be/BmxF8gBSKmQ?t=5

Yeah, I really am foolish. Doing this with insets and loop cuts is very natural, but I've been doing my subdiv modeling in overthing other than that.

https://youtu.be/BmxF8gBSKmQ?t=106

Hmm, I had no idea about this aspect of bevel.

1:20pm. https://youtu.be/PeK6-6Ob8ZU
Blender Chessboard - #8 Subdivison Surface Modelling in Blender 3.0.

Let me stop here. Time for breakfast. I really should know these techniques if I want to get to 3/5 as a 3d artist.

Had I done the monitor differenly it could been a lot easier.

2:25pm. Done with breakfast. Let me resume.

https://youtu.be/PeK6-6Ob8ZU
Blender Chessboard - #8 Subdivison Surface Modelling in Blender 3.0.

Let me watch this.

2:45pm. Instead of watching this I am getting lost in thought. I never realized before now that inset can be used to do localized controling edges instead of loop cuts. This is something that should have been wholy obvious to me, but for some reason it was not. How foolish of me.

2:50pm. Let me get back to the video. Right now I am needlessly lost in thought. These techniques with the inset are much better than the knifing I was doing on the monitor yesterday.

https://youtu.be/PeK6-6Ob8ZU?t=362

Is there an easy way to fix these poles I wonder?

https://youtu.be/PeK6-6Ob8ZU?t=619

Yeah, I wouldn't have thought of doing it like this. It would be inefficient to do it like this, but you can always get rid of these needless boundary loops later. He is just putting them here so they don't get in the way of further loop cuts. Why not just use insets though?

One reason I can think of is that this way the topology would be better.

https://youtu.be/PeK6-6Ob8ZU?t=758

No I do not buy that all those middle loops are necessary. And even if they were, he could have just used creases instead to confine the corner changes.

https://youtu.be/PeK6-6Ob8ZU?t=765

Still now that I am into it, I find this way of modeling quite beatiful. It resonates with me.

https://youtu.be/PSqHeCq7Kio?t=327

I've never tried Cast, I thought it was just for spheres, but I see it can take a target object. Maybe I could use this instead of shrinkwrap. This is something to think about.

https://docs.blender.org/manual/en/latest/modeling/modifiers/deform/cast.html

No, it is just for a few predefined shapes.

https://youtu.be/PSqHeCq7Kio?t=525

Instead of doing this, he should just put the sphere into a vertex group and cast it again. That should get him a perfect sphere...though I am not sure if the problem is how the shading affects the current object or how it affect the subdiv model down the stream. If it is the later, then my advice is good.

https://youtu.be/vi0jiL7LsDA?t=659

So this is how you can set up the lattice easily by hand.

4:35pm. Ah, yesterday, I should have used the vertex groups to protect one of the sides since I could not make it symmetric. That would have worked well for me.

https://youtu.be/IS2LPVNp6SE?t=262

This way of doing it is interesting. So this is how you can do a boolean while preserving the toplogy. I see where this is going.

https://youtu.be/IS2LPVNp6SE?t=283

I am getting lost in thought, I need to focus. I didn't think he would use a shrinkwrap. I thought he would make the loops and start removing faces where they intersect.

4:45pm. https://youtu.be/IS2LPVNp6SE?t=433

This went beyond my expectation. This is a fundamentally different way of working from what I've been studying.

He mentioned that the only other way to get around the issues of booleans is to make the mesh really desnse, and indeed, this is what I would go for. That stuff Josh showed me on how to fix various issues are super hacky, and he should just be honest and say that the method is broken.

4:45pm. You know, given how the lattice works, I am surprised Moi does not have it. Maybe it could be made to work for Nurbs modeling?

https://youtu.be/IS2LPVNp6SE?t=651

What is he doing here?

Ohhhhh! Remember that Zbrush thing where the loop cuts went in the direction of the normal? I thought that was cool. It turns out smoothness is how the same thing could work in Blender. Meaning I can do that fuse even without MESHmachine assuming I am doing proper modeling instead of sketching.

https://youtu.be/IS2LPVNp6SE?t=687
> And we'll find because it a proper subdivision surface model, UV unwrapping and texturing will be simple. Transparency and subsurface scattering will all work correctly.

5pm. https://youtu.be/K5VJYlUV23I
Blender - Insetting and softbodies - #16 Subdivision Surface Modelling in Blender 3

Time for this.

https://youtu.be/K5VJYlUV23I?t=963

Remember those towels I simulated in Houdini? I should have done this instead.

https://youtu.be/K5VJYlUV23I?t=1015

GPU subdivision. I forgot to enable this. It only works when the subdiv mod is last, but that is fine.

Oh, right. Instead of using the lattice, had I been using a proper workflow, I could have applied the subdiv mod once and moved from there.

Tsk. But even though I've learned a bit about topology, it seems yesterday I still haven't learned enough on how to be effective with subdiv.

5:50pm. Focus me, finish the video, not browse /a/.

6:05pm. https://youtu.be/PQThJA_LCPM?t=1030

An interesting trick. So proportional editing + individual origins projects the influence from each origin.

https://youtu.be/PQThJA_LCPM?t=1269

So you can fix the 5 spoked poles like this.

6:15pm. https://youtu.be/PQThJA_LCPM?t=1641

This would end up being a lot of verts on the bottom. I think he could have just done a grid fill as it were without the inner scale. Or better, do that last extrude, but don't do a grid fill. Instead crease the ngon.

https://youtu.be/7Cuj30VikvU
Blender - Boolean Sphere Hard Surface - #18 Subdivision Surface Modelling in Blender 3

6:25pm. Focus me, let me watch this vid as well.

https://youtu.be/7Cuj30VikvU?t=186

This is not how Josh did it, he recommends that the density of two sides match.

https://youtu.be/7Cuj30VikvU?t=555

Yeah, this is close to how I imagined he would do the cylinder. I do not like this technique much, it feels like a pain in the ass.

https://youtu.be/7Cuj30VikvU?t=830

Here he shows how to use the Laplacian Smooth modifier. I'd have never figured this out on my own.

https://youtu.be/ySL4KG2dunQ
Blender Rigid Body Text - #19 Subdivision Surface Modelling in Blender 3

This is the most recent video on his playlist.

Let me watch it and I'll close for the day.

https://youtu.be/5CwjjN7Oibg
King of Sub-D Modeling | Design Highlight #6

Let me watch this. That tutorial by Ian is just how to do a rigid body sim. I studied that before, and it is not too interesting to me at the moment.

https://youtu.be/5CwjjN7Oibg?t=463

He calls him the kind of subd modeling and I believe it.

8pm. Done with lunch. I am not going to do anything more here for the day.

I need some time to digest these new techniques. But now that I've had some time to think, I don't think I like the using subdiv for large scale stuff. The stuff with the use of insets was remarkable, and I finally figured out how to use loop cuts to their full potential, but as a method of getting things done quickly, this leaves a lot to be desired.

I I had to pick a method, I'll probably go with booleans and automated retopo. This is what I will go with.

The disadvantaged of automated retopo start to go away the higher you ramp up the quad size and this is what I going to go with.

If I am going to use subdiv, I am definitely going to be making use of ngons.

8:20pm. I just tried it, and it seems subdiv results in planar faces even when used on a non-planar ngon. Remarkable. If anything that kind of mesh stability is an even stronger reason to use it.

Although it is hacky, it will make things a lot easier, and in no way it will make what I learned today less effective. What he taught me today was proper ways of making extrusions amonths other. These tricks are quite local.

8:25pm. Yeah, it is not like I don't like this. I am filled with admiration for the beauty of subdiv models, but at some point I'll have to stop messing around and pick how I want to do things.

I think that thanks to what I've learned in the last few days, that I consider myself at least having basic proficiency in subdiv modeling. This is good enough for now.

I need to texture that monitor and move on to the rig. I certianly won't be repeating the Moi stuff by hand in subdiv. Instead I'll just import it in Rhino and have its NURBS compatible quad remesher have a go at it. When I start work on Heaven's Key in earnest I'll use sculpting to design my charas, but I won't waste too much time getting the topology right. I can always get a good result by ramping up the face count. The GPU is there for a reason. If it can allow me to save time, I should take advantage of that.

Dealing with topology is fascinating and every 3d artist should have basic proficiency in subdiv modeling, but there is no need to get obsessed with it in the age of quad remeshers.

It is good enough if I understanding it enough to get the shape I want without suffering pinching and shading issues. The best way to understand what is happening is to observe it in wireframe mode.

Though Ian McGlasham stressed quad topology, subdiv supports tris and ngons for a reason.

8:40pm. Everything. Rather than sculpting or NURBS or subdiv, I will take all these techniques and merge them into a single workflow. I am going to step on it tomorrow. I'll finish the monitor and get started on the rig. I can't let this tiny thing hold me back for longer.

8:45pm. It is fun focusing and learning new skills, but I want to get to the point where I am making money from it. This is the only disadvantage of this kind of lifestyle. But I will grasp it at some point. That point will be where I know enough not to be swayed by Youtube modeling vids."

---
## [SabreML/Skyrat-tg](https://github.com/SabreML/Skyrat-tg)@[c5f0ea76e0...](https://github.com/SabreML/Skyrat-tg/commit/c5f0ea76e0fa1d1236fe04a2edaf6d9c047fc7c8)
#### Wednesday 2022-05-04 19:29:40 by SkyratBot

[MIRROR] Vim mecha changes [MDB IGNORE] (#12981)

* Vim mecha changes (#66153)

This PR changes the following:

    fixes a bug with Vim overlays, making it always appear as if there was a pilot inside, even after leaving it
    adds a balloon alert when a mob fails to enter the mech due to its size
    adds a crafting recipe for Vim in the "robots" category
    allows using Vim as a circuit shell
    allows small mobs to use the mech as well

My reasoning behind the changes:

    fixing the overlay bug - bugfixes good, bugs bad
    balloon alert - it should help reduce confusion among players who can't figure why on earth they cannot enter the mech
    crafting recipe - I think a crafting recipe will make it a lot more accessible to players, especially because there is no way to learn about its existence in-game
    circuit shell - non-standard circuit shells can be pretty fun and people seemed to enjoy the ability to use circuits inside their piano synths or cameras, so I figured we could expand on this, while giving players more ways to interact with sentient pets
    maximum mob size increase - Vim has never really been built too often, most likely because even if people got their hands on a sentient pet, it wouldn't probably fit in the tiny mecha anyway. Currently pretty much only butterflies, rats and cockroaches can use Vim and they pretty much never become sentient.

* Vim mecha changes

Co-authored-by: B4CKU <50628162+B4CKU@users.noreply.github.com>

---
## [a12n/dwm](https://github.com/a12n/dwm)@[67d76bdc68...](https://github.com/a12n/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Wednesday 2022-05-04 19:52:05 by Chris Down

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
## [Metelak/Ritual](https://github.com/Metelak/Ritual)@[13c129b775...](https://github.com/Metelak/Ritual/commit/13c129b775d44941683588ec73c36bdc73bb0704)
#### Wednesday 2022-05-04 20:43:42 by crosenfrisk

Added comments to styling sheet for clarity. Some of the chakra-ui names are weird, so having them in sections helps devs know what they are. Footer still appears a little funny on Dashboard view in my opinion, but otherwise Header img and title have a nice margin, and the nav buttons also have a small margin on the right side. I increased the padding of the body section, so there is more space between the header and the body elements. We will see what that looks like with Megan's styling adds for Dashboard page.

---
## [itsprashanthan/OctoPrint-hueCommands](https://github.com/itsprashanthan/OctoPrint-hueCommands)@[cb455b5db6...](https://github.com/itsprashanthan/OctoPrint-hueCommands/commit/cb455b5db648795498f86e8674e0248b9d13ddb7)
#### Wednesday 2022-05-04 21:17:27 by itsprashanthan

Update __init__.py

Hi there,

I was using your plugin (which I love btw!) and noticed the hue doesn't change with the H and U commands. I also noticed the transition time was changing. I know very little about code and programming (I actually made this account on git just for this) but I think the error was that the variable transition time was being changed on line 139 and 140 as opposed to hue? I have proposed the change (sorry if I did it wrong). I would love if you could make the change and release it as it is crucial for me to do what I want to do with my octoprint setup! Thank you!

Prash

---
## [Lindakk/stroke-risk-analysis](https://github.com/Lindakk/stroke-risk-analysis)@[5b0d827667...](https://github.com/Lindakk/stroke-risk-analysis/commit/5b0d827667ceecb3c3049b1f6841761066da06e5)
#### Wednesday 2022-05-04 21:27:39 by Linda Deckerli

Update README.md

This project seeks to create a model using the dataset (‘healthcare-dataset-stroke-data’) so as to predict if a person is more likely to have a stroke based on features in the dataset such as gender, age, blood pressure, blood sugar, and marriage status, etc. I plan to use multiple machine learning models I have learned from this course as well as two other models I found online. I am aiming to find the best model to perform the classifications of the likely to have a stroke (stroke=1) and likely not to have a stroke (stroke =0).
This project has three sections. Section 1 focuses on cleaning and preparing the data (dropping null values, converting categorical values to numeric values) and analyzing the correlations between the features and the lable class. Section 2 focuses on using KNN, Logistic, and Random forest models to classify the stroke lable, and compute the associated performance matrices. Section 3 focuses on oversampling the data first and then applying different machine learning models so as to compare the results.
Section 1:
First I checked the dataset’s basic info and its null values. I dropped the ‘id’ column since it is not a valid feature to perform classification. Then, I filled the null values in the ‘bmi’ column using the mean value of ‘bmi’. Then I converted all categorical values to numeric values such as Female=1, Male=0, Yes=1, No=0 in 'ever_married' column, etc. Finally, I checked the correlations between all the features and the ‘stroke’ lable.
	 

Based on the above graph, ‘age’ has the highest correlation with ‘stroke’ compared to other features. This means that older people have higher chance of having a stroke. ‘hypertension’,’avg_glucose_level’ and ‘heart_disease’ also have relatively high correlations with ‘stroke’.  


 

I also checked the relations between avg_glucose_level and age based on the ‘stroke’ lable. Based on the above graph, we can see that older people are more likely to have higher avg_glucose_level (above 100), and are more likely  to have a stroke. 

Section 2:
The datapoints for the ‘stroke’ column is very imbalanced (see the graph below). For this section, I wanted to try KNN, Logistic and Random Forest models without oversampling the data. 
 
KNN classification:
I tried k_values=1-10. Based on the accuracy rate, k=10 gives the best accuracy rate. 
 
When  K=10, compute the MAE, RMSE, confusion matrix and TP,FP,TN,FN,accuracy, TPR and TNR values.
MAE: 0.050489236790606656
RMSE: 0.2246981014397021
 
 

Logistic model:
MAE: 0.050489236790606656
RMSE: 0.2246981014397021
 
 
Random Forest:
MAE: 0.05244618395303327
RMSE: 0.22901131839503758
 
 


From the above figures, we can see that the performance matrices such as accuracy rates, MAE and RMSE for each model are all fairly high. However, from the confusion matrix graphs and the TN /TNR table, we can tell the TNR, which represents the rate of successfully identifying stroke=1, is extremely low (basically 0). Therefore, none of the models performed well in terms of predicting the likelihood of having a stroke. This made me realize that the extremely imbalanced class distribution causes some performance matrices such as accuracy rate to be poor measures for evaluating the classification models. 

Section 3: 
In order to solve the above issue, I used SMOTE Class to perform over-sampling. The values in the ‘stroke’ column after oversampling are plotted as follows:
 
I created a function run_model, and re-ran KNN(K=10), Logistic, and Random Forest models. The results are:
KNN(K=10):
 
 

Logistic regression:
 
 

Random Forest Tree:
 

 


I also tried to use StratifiedKfold to make 10 folds and perform SMOTE and Random Forest with each fold. The best TNR I got is below:
 
The best TNR is 0.36 which is still not optimal. 

I did another attempt with SVC model to see if I can get a better result with TNR:
SVC model with class_weight='balanced':

 
 


In conclusion, the main purpose of this project was to predict the likelihood of a person having a stroke. Considering all the machine learning models I tried, I think the logistic model provided a relatively better result than the other models, because the TNR rate for the logistic model was 79%, which was much higher than the other models. I also think that perhaps this dataset did not include the most appropriate features for the ‘stroke’ classification. I am looking forward to doing more research on this and to finding out if other features (such as alcohol consumption, family history, etc.) would contribute to a better classification result.

---
## [OpenAngelArena/oaa](https://github.com/OpenAngelArena/oaa)@[841368b6b0...](https://github.com/OpenAngelArena/oaa/commit/841368b6b064c700c6194d8e46d798e0d4494ed1)
#### Wednesday 2022-05-04 22:39:31 by Darko V

Modifiers changes (May 2022) (#3351)

* Cycled Out modifiers: Hyper Lifesteal, Blood Magic, Healer and Brute.
* Randomize button will no longer randomize the 'None' option.
* Buffed Timeless Relic modifier from 25% to 30%.
* Telescope modifier now also provides 400 bonus vision (day/night).
* Fixed Telescope modifier cast range bonus not stacking with other cast range bonuses.
* Fixed Creed of Omniscience and Telescope neutral items cast range bonuses not stacking with Octarine Core or Far Sight cast range bonuses.
* Random Draft number of banned heroes increased from 70 to 75.
1) Added Aghanim, Nimble and Sorcerer modifiers.
2) Updated tooltip for Wisdom modifier.
3) Bonus AoE/Radius modifier now ignores:
- Arc Warden Flux search radius
- Drow Ranger agility range penalty
- Monkey King Wukong's Command
- Phantom Assassin Blur
- Spectre Desolate
4) Bonus AoE/Radius now improves Sohei's Dash width.
5) Diarrhetic auto-poop-ward check-for-wards-radius increased from 200 to 300. This means auto-pooped wards will be farther from each other.
6) Explosive Death modifier will now proc on Tempest Doubles and heroes that are reincarnating.
7) Attack Range Switch modifier bonus attack range reduced from 600 to 500.
8) Attack Range Switch modifier bonus projectile speed increased from 900 to 1100.
9) Added Max Power modifier
10) Fixed tooltip for modifiers saying undefined when 'Random' option is selected.

---

