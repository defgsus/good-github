## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-02-15](docs/good-messages/2022/2022-02-15.md)


1,739,204 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,739,204 were push events containing 2,793,257 commit messages that amount to 212,384,823 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 38 messages:


## [determined-ai/determined](https://github.com/determined-ai/determined)@[08888717a6...](https://github.com/determined-ai/determined/commit/08888717a6db21304115cd119ebb5d926d51c88e)
#### Tuesday 2022-02-15 00:09:43 by Bradley Laney

feat: unify task logs [DET-6062, DET-6063, DET-6064, DET-6065, DET-6066] (#3070)

This change adds persistent logs for all task types (well, all except poor old checkpoint GC). This means that logs are written to the logging back-end as configured in the master (PostgreSQL through master or Elastic) by Fluentbit and accessible through APIs in the master that translate reads to the back-end's language. To allow for this change, many other changes were required. A (probably) non-exhaustive list follows:
* Trial logs used to go to a `trial_logs` table or index. I tried to not tear the codebase asunder forever with trials and the others using different tables/queries/structs/etc everywhere. Existing tasks were marked has having `log_version == 0` and the old `trial_logs` table now serves logs those tasks (only trials). From now on, all tasks are written with `log_version == 1` and queries for their logs are routed to the `task_logs` table. The old trial logs table (now the `log_version == 0` table) is mothballed - it (mostly) shouldn't be touched again and the old logs should load from there fine forever while new features can be built on the new table. There were alternatives besides leaving trials and task logs separate forever that I shied away from; e.g., I considered a migration to update the trial logs table to schema of the task logs table, but since we access task logs by task_id, this would require rewriting the index on trial_id or adding one on task_id which is too expensive for a migration. This solution balances complexity, maintainability and migration cost.
* Because task logs went through the master, we were free to built features like readiness checks on top of them. Now that they don't, before logs leave the container a small helper script skims them, checks for the readiness logs and posts readiness to a new API. I considered alternatives here, too, like reading the logs back in on the master side, but that incurs a lot more overhead I felt this was more flexible anyway.
* The old events endpoint used to return logs, now it doesn't. This was because it (the eventManager that backed the endpoint) used to _store_ the logs, and now it doesn’t. In my opinion, the work to read the log stream and the old event stream and merge them is low value and annoying. Users should just prefer the new `/api/v1/tasks/:id/logs` endpoint for logs and rely on events to get the few task events that were relied on. Events will likely be supplanted by a task state watcher of some time so webui/cli can just watch for the readiness bit to flip.

---
## [FiendsOfTheElements/FF1Randomizer](https://github.com/FiendsOfTheElements/FF1Randomizer)@[34eea2f3d1...](https://github.com/FiendsOfTheElements/FF1Randomizer/commit/34eea2f3d105d9b5067aa55400b894c58c00e924)
#### Tuesday 2022-02-15 00:17:12 by mhn65536

Mhn65536/oops2 (#802)

* Tournament Item magic Pool
Lower Thief Agility Settings
Buff Tier1 Damage Spells

* fix

* oops

* i hate my life

Co-authored-by: x.y <x.y@z>

---
## [XertroV/aec-membership-test-simulator](https://github.com/XertroV/aec-membership-test-simulator)@[f0ad505872...](https://github.com/XertroV/aec-membership-test-simulator/commit/f0ad5058729be252b8425fbd4daaab760a31ec79)
#### Tuesday 2022-02-15 00:41:38 by Max Kaye

well, I think we can conclude that this shit's fucked.

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[079f8ac515...](https://github.com/timothymtorres/tgstation/commit/079f8ac51554bb338ac5826c9d06c8d4bc10be80)
#### Tuesday 2022-02-15 01:28:26 by LemonInTheDark

Adds moveloop bucketing, uses queues for the singulo rather then sleeps (#64418)

Adds a basic bucketing system to move loops.

This should hopefully save a lot of cpu time, and allow for more load while gaining better smoothness.

The idea is very similar to SStimer, but my implementation is much more simple, since I have to worry less about long delays and redundant buckets.
Insertion needs to be cheaper too, since I'm making a system that by design holds a lot of looping things

It comes with some minor tradeoffs, we can't have constant rechecking of loops if a move "fails", not that we really want that anyway
We also lose direct control over the timer var, but I think that's better, don't want people manipulating that directly
Not that it even really worked very well back when we did have it
Removes the sleep from singularity code

Rather then using sleep to store the state of our iteration, we instead queue the iteration in a list.
We then use a custom singulo processing subsystem to call our "digest" proc several times per full eat, with the hope of staying on top of
our queue
This rarely happens because the queue is too large, god why is a sm powered singulo 24x24 tiles.

I've also A: cached our dist checks, and B: Added dist checks to prevent attempting to pull things out of range
This might look a bit worse, but it saves a lot of work

Oh right and I made the singulo unable to eat while it still has tiles to digest. The hope is to prevent
overwork and list explosion.

Hopefully this will prevent singulo server stoppage, though I've seen some other worrying things in testing.

---
## [Legonzaur/NorthstarLauncher](https://github.com/Legonzaur/NorthstarLauncher)@[db0af63704...](https://github.com/Legonzaur/NorthstarLauncher/commit/db0af63704a6fbc57e80a9db01bbc01b79339d9f)
#### Tuesday 2022-02-15 03:57:29 by Emma Miler

Added code for chathooks

This may not seem like much to a passing observer, but this commit took me 30 hours of blood, sweat, tears, IDA debugging, server crashes, and insanity.

---
## [osamuaoki/qmk_firmware](https://github.com/osamuaoki/qmk_firmware)@[37d0acccd2...](https://github.com/osamuaoki/qmk_firmware/commit/37d0acccd2b362c70509eed8ca706cbad9f02122)
#### Tuesday 2022-02-15 05:29:08 by Osamu Aoki

Format update and note

Note: Although these 2 lines should move to // Magic section, doinso may
cause trouble.  (My development time vague memory:  Back slash and back
space became swapped.  Since others had MAGIC_TOGGLE_CONTROL_CAPSLOCK
here, I assume this is the least invasive (but ugly patch.)

Signed-off-by: Osamu Aoki <osamu@debian.org>

---
## [allie-project/libglide](https://github.com/allie-project/libglide)@[70b798996b...](https://github.com/allie-project/libglide/commit/70b798996bc1e6254770b3c9a98e8e5b7ede2a48)
#### Tuesday 2022-02-15 05:57:27 by Carson M

Add basic tests with gtest

TODO: do whatever the fuck you did with the CMake library properly

---
## [JasonSteving99/claro-lang](https://github.com/JasonSteving99/claro-lang)@[cebe6848d7...](https://github.com/JasonSteving99/claro-lang/commit/cebe6848d7cdc1ca25f74f66798efe74332282b2)
#### Tuesday 2022-02-15 07:15:22 by Jason Steving

Implement `exec(...)` in StdLib To Interpret Arbitrary Code in String.

This is obviously a generally dangerous thing, but it also leads to some really awesome fun with a language. Considering every other form of security in a programming language really just involves expecting programmers to do smart things, I'm not that sad about supporting exec from "security" concerns...just don't use it in prod code and you'll be happy lol.

The awesome thing about this is that it demonstrates the power of implementing the compiler backends themselves in the same language as the generated target source. This allows some super cool dogfooding, and the fact that this was a one night feature to implement proves the value of developing a compiler in this manner before transitioning to the more annoying thing of emitting bytecode.

---
## [repinger/exynos9611_m21_kernel](https://github.com/repinger/exynos9611_m21_kernel)@[10c2e2c286...](https://github.com/repinger/exynos9611_m21_kernel/commit/10c2e2c28644a53e32b8bb5b68aadb3859c57e40)
#### Tuesday 2022-02-15 07:15:28 by Masahiro Yamada

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
[nc: Omit rpmsg, sdw, tbsvc, and typec as they do not exist here]
Signed-off-by: Nathan Chancellor <natechancellor@gmail.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [jaimeMF/mpv](https://github.com/jaimeMF/mpv)@[c1a961ad78...](https://github.com/jaimeMF/mpv/commit/c1a961ad78b6d1da339e622c723d753a80687824)
#### Tuesday 2022-02-15 07:20:34 by wm4

draw_bmp: rewrite

draw_bmp.c is the software blender for subtitles and OSD. It's used by
encoding mode (burning subtitles), and some VOs, like vo_drm, vo_x11,
vo_xv, and possibly more.

This changes the algorithm from upsampling the video to 4:4:4 and then
blending to downsampling the OSD and then blending directly to video.
This has far-reaching consequences for its internals, and results in an
effective rewrite.

Since I wanted to avoid un-premultiplying, all blending is done with
premultiplied alpha. That's actually the sane thing to do. The old code
just didn't do it, because it's very weird in YUV fixed point.
Essentially, you'd have to compensate for the chroma centering constant
by subtracting src_alpha/255*128. This seemed so hairy (especially with
correct rounding and high bit depths involved) that I went for using
float.

I think it turned out mostly OK, although it's more complex and less
maintainable than before. reinit() is certainly a bit too long. While it
should be possible to optimize the RGB path more (for example by
blending directly instead of doing the stupid float conversion), this is
probably slower. vo_xv users probably lose in this, because it takes the
slowest path (due to subsampling requirements and using YUV).

Why this rewrite? Nobody knows. I simply forgot the reason. But you'll
have it anyway. Whether or not this would have required a full rewrite,
at least it supports target alpha now (you can for example hard sub
transparent PNGs, if you ever wanted to use mpv for this).

Remove the check in vf_sub. The new draw_bmp.c is not as reliant on
libswscale anymore (mostly uses repack.c now), and osd.c shows an
error message on missing support instead now.

Formats with chroma subsampling of 4 are not supported, because FFmpeg
doesn't provide pixfmt definitions for alpha variants. We could provide
those ourselves (relatively trivial), but why bother.

---
## [PeterlitsZo/ACMHomepage](https://github.com/PeterlitsZo/ACMHomepage)@[ace4033efa...](https://github.com/PeterlitsZo/ACMHomepage/commit/ace4033efad3202b5efa4c39a46329de3311e701)
#### Tuesday 2022-02-15 07:56:36 by Peterlits Zo

feat: Add page `News`.

Well, we have `News` component, and now we also have `News` page. Well. Well.
We will going to rename it or something else.

To go to `News` page, we let the button `Read More` in component `Carousel` be
clickable. To let the news have its own path, we add `id` for those.

To mock the new `id` attr, we also change the mock file `handler.js`. and let
it can deal with the query with variable. (By the way, to make it have better
data, we are using `faker.js`, I really hope that Marak get the money he should
have. Damn it, fuck you Github).

After that, we add its page add its `Router` in `index.jsx`. After that I find
that we need to scroll to top auto. So I add component `ScrollToTop` to deal
with it.

OK, that's all.

---
## [freedesktop/NetworkManager](https://github.com/freedesktop/NetworkManager)@[c0fb7f9366...](https://github.com/freedesktop/NetworkManager/commit/c0fb7f9366e02731c7e5a2d2b59c5c3c363e24af)
#### Tuesday 2022-02-15 08:00:37 by Thomas Haller

platform: support IPv6 mulitpath routes and fix cache inconsistency

Add support for IPv6 multipath routes, by treating them as single-hop
routes. Otherwise, we can easily end up with an inconsistent platform
cache.

Background:
-----------

Routes are hard. We have NMPlatform which is a cache of netlink objects.
That means, we have a hash table and we cache objects based on some
identity (nmp_object_id_equal()). So those objects must have some immutable,
indistinguishable properties that determine whether an object is the
same or a different one.

For routes and routing rules, this identifying property is basically a subset
of the attributes (but not all!). That makes it very hard, because tomorrow
kernel could add an attribute that becomes part of the identity, and NetworkManager
wouldn't recognize it, resulting in cache inconsistency by wrongly
thinking two different routes are one and the same. Anyway.

The other point is that we rely on netlink events to maintain the cache.
So when we receive a RTM_NEWROUTE we add the object to the cache, and
delete it upon RTM_DELROUTE. When you do `ip route replace`, kernel
might replace a (different!) route, but only send one RTM_NEWROUTE message.
We handle that by somehow finding the route that was replaced/deleted. It's
ugly. Did I say, that routes are hard?

Also, for IPv4 routes, multipath attributes are just a part of the
routes identity. That is, you add two different routes that only differ
by their multipath list, and then kernel does as you would expect.
NetworkManager does not support IPv4 multihop routes and just ignores
them.
Also, a multipath route can have next hops on different interfaces,
which goes against our current assumption, that an NMPlatformIP4Route
has an interface (or no interface, in case of blackhole routes). That
makes it hard to meaningfully support IPv4 routes. But we probably don't
have to, because we can just pretend that such routes don't exist and
our cache stays consistent (at least, until somebody calls `ip route
replace` *sigh*).

Not so for IPv6. When you add (`ip route append`) an IPv6 route that is
identical to an existing route -- except their multipath attribute -- then it
behaves as if the existing route was modified and the result is the
merged route with more next-hops. Note that in this case kernel will
only send a RTM_NEWROUTE message with the full multipath list. If we
would treat the multipath list as part of the route's identity, this
would be as if kernel deleted one routes and created a different one (the
merged one), but only sending one notification. That's a bit similar to
what happens during `ip route replace`, but it would be nightmare to
find out which route was thereby replaced.
Likewise, when you delete a route, then kernel will "subtract" the
next-hop and sent a RTM_DELROUTE notification only about the next-hop that
was deleted. To handle that, you would have to find the full multihop
route, and replace it with the remainder after the subtraction.

NetworkManager so far ignored IPv6 routes with more than one next-hop, this
means you can start with one single-hop route (that NetworkManger sees
and has in the platform cache). Then you create a similar route (only
differing by the next-hop). Kernel will merge the routes, but not notify
NetworkManager that the single-hop route is not longer a single-hop
route. This can easily cause a cache inconsistency and subtle bugs. For
IPv6 we MUST handle multihop routes.

Kernels behavior makes little sense, if you expect that routes have an
immutable identity and want to get notifications about addition/removal.
We can however make sense by it by pretending that all IPv6 routes are
single-hop! With only the twist that a single RTM_NEWROUTE notification
might notify about multiple routes at the same time. This is what the
patch does.

The Patch
---------

Now one RTM_NEWROUTE message can contain multiple IPv6 routes
(NMPObject). That would mean that nmp_object_new_from_nl() needs to
return a list of objects. But it's not implemented that way. Instead,
we still call nmp_object_new_from_nl(), and the parsing code can
indicate that there is something more, indicating the caller to call
nmp_object_new_from_nl() again in a loop to fetch more objects.

In practice, I think all RTM_DELROUTE messages for IPv6 routes are
single-hop. Still, we implement it to handle also multi-hop messages the
same way.

Note that we just parse the netlink message again from scratch. The alternative
would be to parse the first object once, and then clone the object and
only update the next-hop. That would be more efficient, but probably
harder to understand/implement.

https://bugzilla.redhat.com/show_bug.cgi?id=1837254#c20

---
## [Evolution-X/frameworks_base](https://github.com/Evolution-X/frameworks_base)@[1383bd23b5...](https://github.com/Evolution-X/frameworks_base/commit/1383bd23b5a4a5ec70304aa17521c964e63ffd15)
#### Tuesday 2022-02-15 08:55:47 by Joey Huab

core: Rework the Photos features blacklist again

* Apparently, Magic Eraser currently requires a
  specific Photos version for it to show up and
  actually work. (apkmirror.com/apk/google-inc/photos/photos-5-65-0-405472367-release/google-photos-5-65-0-405472367-10-android-apk-download)

* Basically, Magic Eraser feature will crash if Photos
  is spoofed as Pixel XL.

* If Photos is spoofed as Pixel XL and it sees the
  features to make Magic Eraser work, it will try to
  load it but it will get stuck in an endless loop.

* We want to make Magic Eraser work by default as
  long as the Unlimited Photos spoof is turned off.

* However, when PIXEL_2021_EXPERIENCE feature
  is detected by the Photos app, it will use
  the TPU tflite delegate. So we need to
  blacklist it by default from the Photos app.

* TL;DR Magic Eraser is wonky and hard to
  enable and all this mess isn't really worth
  the trouble so just stick to the older setup.

---
## [Evolution-X/frameworks_base](https://github.com/Evolution-X/frameworks_base)@[b3983abfec...](https://github.com/Evolution-X/frameworks_base/commit/b3983abfece48926438cdb3519aa417dbe5316c9)
#### Tuesday 2022-02-15 08:57:17 by Joey Huab

core: Rework the Photos features blacklist again

* Apparently, Magic Eraser currently requires a
  specific Photos version for it to show up and
  actually work. (https://apkmirror.com/apk/google-inc/photos/photos-5-65-0-405472367-release/google-photos-5-65-0-405472367-10-android-apk-download)

* Basically, Magic Eraser feature will crash if Photos
  is spoofed as Pixel XL.

* We want to make Magic Eraser work by default as
  long as the Unlimited Photos spoof is turned off.

* However, when PIXEL_2021_EXPERIENCE feature
  is detected by the Photos app, it will use
  the TPU tflite delegate. So we need to
  blacklist it by default from the Photos app.

* TL;DR Magic Eraser is wonky and hard to
  enable and all this mess isn't really worth
  the trouble so just stick to the older setup.

---
## [Evolution-X/frameworks_base](https://github.com/Evolution-X/frameworks_base)@[07fbac0c8f...](https://github.com/Evolution-X/frameworks_base/commit/07fbac0c8fc391a966a0ba72a19886948dd1adf0)
#### Tuesday 2022-02-15 08:58:07 by Joey Huab

core: Rework the Photos features blacklist again

* Apparently, Magic Eraser currently requires a
  specific Photos version for it to show up and
  actually work. (https://apkmirror.com/apk/google-inc/photos/photos-5-65-0-405472367-release/google-photos-5-65-0-405472367-10-android-apk-download)

* Basically, Magic Eraser feature will crash if
  Photos is spoofed as Pixel XL. We want to
  make Magic Eraser work by default as long as
  the Unlimited Photos spoof is turned off.

* However, when PIXEL_2021_EXPERIENCE feature
  is detected by the Photos app, it will use
  the TPU tflite delegate. So we need to
  blacklist it by default from the Photos app.

* TL;DR Magic Eraser is wonky and hard to
  enable and all this mess isn't really worth
  the trouble so just stick to the older setup.

---
## [jupyterkat/Shiptest](https://github.com/jupyterkat/Shiptest)@[5e29827ceb...](https://github.com/jupyterkat/Shiptest/commit/5e29827cebbb7cd08d4bf5b210675526f324bf6d)
#### Tuesday 2022-02-15 09:00:20 by Zephyr

Spacemandmm fixes (#799)

* do it

Signed-off-by: Matthew <matthew@tfaluc.com>

* little more detail here

Signed-off-by: Matthew <matthew@tfaluc.com>

* put it in the wrong dmi

Signed-off-by: Matthew <matthew@tfaluc.com>

* Update code/game/objects/items/tools/chisel.dm

Copy paste gp BRRR

Co-authored-by: PrefabQuasar <78622038+PrefabQuasar@users.noreply.github.com>

* resolve some issues that spacemandmm is complaining about because got fucking damn is it annoying when I am trying to code something and I get nonstop errors about stupid issues. also did you know that people though rand was exclusive on the high end? its actually not, both params are inclusive, which is stupid since this is different to almost every other god damn language

Signed-off-by: Matthew <matthew@tfaluc.com>

Co-authored-by: PrefabQuasar <78622038+PrefabQuasar@users.noreply.github.com>

---
## [HendrikPetertje/workers_test_app](https://github.com/HendrikPetertje/workers_test_app)@[60a3e3f850...](https://github.com/HendrikPetertje/workers_test_app/commit/60a3e3f850ab081da9d0ea15a9ae45e49a888737)
#### Tuesday 2022-02-15 09:32:32 by Hendrik Peter van der Meulen

Attempt 2: Advanced Sneakers ActiveJob

Like attempt 1 there isn't really a need for a bin/rip script as foreman has
significantly less patience than the worker :p. just CTRL+C as soon as you have
loaded http://localhost:3000/?name=hello-world and you should be good!

That said, I'm really liking what I'm seeing here! There are so many advantages:
- It's fast!
- Jobs are sent in to the queue and returned from the queue, it all just works.
- Queue-names are respected. There can be multiple job types per queue too, so
  that's a win!
- Time-outs, re-queueing and anything that isn't the job itself is handled by
  the rabbitMQ server (more about the job life-cycle below).
- Failing jobs are retried with "Exponential Back-off" which means that on first
  failure rabbitMQ will delay the job with 3 seconds, then 30 and then up all
  the way till it's stuck in a "try once per 24 hours" cycle at which point we
  should start to act.
- Newrelic is natively supported (getting per-worker metrics) and so is our
  current project's backup error tracker (through Airbrake) and any extra error
  tracker or Newrelic custom-event we'd like to add.
- It's all "rip the powerplug"-safe! With queues persisted to disk, ackable
  messages in our apps, etc.
- It opens a path for increased communication between our project's admin portal
  and our app infrastructure (maybe, though we should probably only build infra
  for that when we actually need it ;)).
- It has a web interface (through rabbitMQ) and options to automate different
  things on the RabbitMQ side.
- There is [excellent documentation](https://blog.rabbitmq.com/posts/2020/08/deploying-rabbitmq-to-kubernetes-whats-involved/)
  available for use with Kubernetes in situations where we don't have
  access to "Amazon MQ for RabbitMQ". The important bit we need to be aware of
  is the "Erlang Cookie" and volumes.

The disadvantages however:
- The framework depends on a pet-project by "[Veeqo](https://www.veeqo.com)".
  It's starting to become more and more popular, but its downloaded only
  22.213 times. The Rails 7.0 compatible code is only available on Github right
  now. If we are to use this project then we'll need to make sure to make
  forks of the following projects for the sake of not loosing access to them
  later on:
  - [advanced-sneakers-activejob](https://rubygems.org/gems/advanced-sneakers-activejob)
  - [bunny-publisher](https://rubygems.org/gems/bunny-publisher)
- No CRON scheduler to run tasks at specific times of the day. So we'll need to
  create a pod in our clusters that executes a persisted task using either:
  - https://github.com/jmettraux/rufus-scheduler
  - https://github.com/jjb/ruby-clock (easy integration with rails)
  - https://github.com/plashchynski/crono (over-engineered, it's more than we
    need)
- We have to depend on Bunny for increased reliability of our connection and the
  workers, but given that the adapter supports it that is not really a problem.
- We need to provision Amazon MQ rabbitMQ instances and deal with rabbit pods +
  volumes in our on-prem install.

A job Life-cycle:

- A job is created using Rails default `perform_later` logic.
- The job is posted to rabbitMQ a durable (persisted) RMQ exchange which pops
  the task on a queue. Ack-ing is enforced.
- The job is distributed to one of the connected workers channels using
  "round-robin".
- A rails worker picks the job from the queue with "manual Ack", the job is
  persisted in the queue as "unacked" by a connection and channel.
- When the worker finishes its work:
  - the worker publishes an "ack!" back to the queue
  - rabbitMQ marks the job as complete and removes it from the queue.
- When the worker fails:
  - The worker re-publishes the job to the "delayed" exchange
    with a retry-counter and the desired time-out time.
  - RabbitMQ moves the message from the jobs queue, publishes it to the
    delayed-X queue (where X is the delay time) and unassigns it from the
    connection + channel.
  - The delayed-X queue automatically pushes the job back in to the worker
    queue when the task has been in the queue for X secodns persisting its
    retry and error headers. A worker can then pick it back up.
- When the worker dies or SIGKILLs:
  - RabbitMQ will detect that the connection is gone, expire the channels,
    remove the unacked status and make the job available for the next worker.
  - A new worker (or other live-worker) will attempt to re-do the task

It's super awesome, I'm absolutely going to demo this!

---
## [RajaKunalPandit1/CodeForces_Questions](https://github.com/RajaKunalPandit1/CodeForces_Questions)@[8fb74b37c2...](https://github.com/RajaKunalPandit1/CodeForces_Questions/commit/8fb74b37c2f1bca9b998f21f214fff5ff6173a49)
#### Tuesday 2022-02-15 09:48:07 by Raja Kunal Pandit

Create 141A - Amusing Joke.cpp

Output Status: 

By Rajakunalpandit, contest: Codeforces Round #101 (Div. 2), problem: (A) Amusing Joke, Accepted

So, the New Year holidays are over. Santa Claus and his colleagues can take a rest and have guests at last. When two "New Year and Christmas Men" meet, thear assistants cut out of cardboard the letters from the guest's name and the host's name in honor of this event. Then the hung the letters above the main entrance. One night, when everyone went to bed, someone took all the letters of our characters' names. Then he may have shuffled the letters and put them in one pile in front of the door.

The next morning it was impossible to find the culprit who had made the disorder. But everybody wondered whether it is possible to restore the names of the host and his guests from the letters lying at the door? That is, we need to verify that there are no extra letters, and that nobody will need to cut more letters.

Help the "New Year and Christmas Men" and their friends to cope with this problem. You are given both inscriptions that hung over the front door the previous night, and a pile of letters that were found at the front door next morning.

Input
The input file consists of three lines: the first line contains the guest's name, the second line contains the name of the residence host and the third line contains letters in a pile that were found at the door in the morning. All lines are not empty and contain only uppercase Latin letters. The length of each line does not exceed 100.

Output
Print "YES" without the quotes, if the letters in the pile could be permuted to make the names of the "New Year and Christmas Men". Otherwise, print "NO" without the quotes.

Examples
inputCopy
SANTACLAUS
DEDMOROZ
SANTAMOROZDEDCLAUS
outputCopy
YES
inputCopy
PAPAINOEL
JOULUPUKKI
JOULNAPAOILELUPUKKI
outputCopy
NO
inputCopy
BABBONATALE
FATHERCHRISTMAS
BABCHRISTMASBONATALLEFATHER
outputCopy
NO
Note
In the first sample the letters written in the last line can be used to write the names and there won't be any extra letters left.

In the second sample letter "P" is missing from the pile and there's an extra letter "L".

In the third sample there's an extra letter "L".

---
## [kristian/neonbee](https://github.com/kristian/neonbee)@[423840cf40...](https://github.com/kristian/neonbee/commit/423840cf40db1693a520afae6bf5f994c852e37b)
#### Tuesday 2022-02-15 09:51:00 by Kristian Kraljic

feat: improve `Launcher`, `Deployable`, `EntityModelManager` and more

This change is huge... I am sorry, but here is a video of me explaining why the change got so huge [1]. Sorry? Good news tough: All changes have been made interface and thus downwards compatible to the old NeonBee version, thus no adaptions to existing functionality should become necessary. Let me go into detail what changed and which quality of life / boy scout rule improvements have been made:

- Many NeonBee methods had been introduced in a pre-Vert.x 4-era. Meaning they did not take advantage of the futurization process Vert.x went through. This change rewrites many methods and simplifies them by switching the futurized methods, instead of methods using handlers.

- Improved the NeonBee bootstrap by making it more asynchronous, by changing the structure of method calls throughout the boot process and wrapping blocking code in `AsyncHelper.executeBlocking` calls.

- Simplified implementation of the `Launcher` class. Instead of manually defining and parsing all options in the launcher to get to a `NeonBeeOption` instance, instead switching to Vert.x's annotation-based `CLIConfigurator` implementation. Annotations are now defined directly in the `NeonBeeOptions` and injected into the `NeonBeeOptions` instance by the `CLIConfigurator`. This makes it much simpler and less error prone to define options and makes it also clear: everything that is in `NeonBeeOptions` can be defined through the command-line or environment. For the latter a `EnvironmentAwareCommandLine` was introduced, that also considers the environment variables if no options are set as arguments, deprecating all "helper methods" that have been there for only this reason.

- Added a new `development_conventions.md` document, that elaborates many "hidden rules" that we came up over the years, when it comes to coding conventions, such as: naming conventions for NeonBee variables, whether to use an instance to `NeonBee` or to `Vertx`, where to place `Context` variables in method signatures and how to properly correlate log messages. Then, in this change, a couple of old methods have been cleaned up to fit this new guiding document.

- The old naming choice for the "/verticles" subfolder does no longer make sense, because not only verticles are deployed by the `DeployerVerticle`, but full "modules". Thus, introduced a new `getModulesDirectory` method to `NeonBeeOptions` and deprecated the old `getVerticlesDirectory`. Two `DeployerVerticle` will now take care to deploy the old and the new directory if necessary (present).

- Introduced a new --module-jar-paths option to NeonBee options, that allows to define paths to module JARs, that will get deployed during the bootstrap phase of NeonBee into own self-first class-loaders. Previously the only option to deploy modules was through NeonBees `DeployerVerticle`, that was watching the `verticles` sub-directory for changes. The new option grants to also deploy modules that are not physically in that folder.

- Split up `EntityModelManager` into its (previously embedded) sub-classes by introducing a package private `EntityModelLoader` class. Futurized many of its methods and improved the concept for registering "external models": Previously modules did register / unregister models to the `EntityModelManager` by using their module identifier as a unique key. The `EntityModelManager` kept a private map of these IDs (`BUFFERED_MODULE_MODELS`) mapping to a set of compiled `EntityModel` objects. Now the concept was changed by introducing a new `EntityModelDefinition` object, that can be used to influence compilation of models of the `EntityModelManager`. Whenever a `EntityModelDefinition` is added / removed from the `EntityModelManager` it will attempt to compile a new "global" set of models. This allows for inter-dependent models and sets up the `EntityModelManager` for an upcoming change to be completely remodeled in order to support versioned models going forward (see the roadmap). It also makes managing the "external models" more easy, because no longer we need to hold a map of identifiers, but only a `Set<EntityModelDefinition>` to be maintained by the `EntityModelManager`. This makes it useful not only to modules, but any object that needs to deal with model generation can now supply a `EntityModelDefinition`.

- Removed `NeonBeeModule` in favor of a new `DeployableModule`. The `Deployable` interface was thought to become a generic object. Everything that can be deployed to NeonBee should inherit `Deployable`. `NeonBeeModule` violated this pattern and implemented much the same logic. Now the whole `io.neonbee.internal.deploy` package is consistent again, by introducing a `DeployableModels` (that can deploy `EntityModelDefinition` object), `DeployableModule` (that parses JAR files and splits them up into `DeployableModels` and `DeployableVerticles`) and a generic `Deployables` class, that handles deployments of multiple `Deployable` objects. This makes the whole deployment much cleaner, as for NeonBee everything is now a `Deployable` and the logic, whether it is a module, or a verticle, or a model that is being deployed, is now completely hidden away inside of the respective `Deployable` implementation. After deployment, everything results in the same `Deployment` instance, that can be undeployed again in the same fashion.

- Quality of life improvements to `AsyncHelper` by introducing runnables, cosumers and suppliers that can throw an exception. This allowed to replace existing calls like `AsyncHelper.executeBlocking(vertx, () -> { try { ... } catch (e) { return failedFuture(e); } })` with `AsyncHelper.executeBlocking(vertx, () -> ...)`.

- Simplified `ClassPathScanner` and introduced a new `CloseableClassPathScanner` that closes the underlying `URLClassLoader` to stop leaking resources.

- Introduced a new `ThreadHelper` class, that can be used to retrieve the calling or own class, as well as the class-loader of the current thread.

- Made `NeonBeeProfile` behave the same as for `moduleJarPaths` when getting parsed, meaning that you can define multiple profiles separated by comma.

- Renamed CollectionsHelper to CollectionHelper, because it was the only helper with a plural name.

- Improve many tests (esp. Deployable ones) mainly by mocking more and spying less.

- Made `setEnvironment` and `withEnvironment` work on Windows, to be able to remove `@DisableOnOS` annotation for tests changing environment variables.

---
## [AvanaPY/DV1655_Lab1](https://github.com/AvanaPY/DV1655_Lab1)@[09a0a2487b...](https://github.com/AvanaPY/DV1655_Lab1/commit/09a0a2487bc7eaf3e00fc559b8cc16d9b45ad83c)
#### Tuesday 2022-02-15 10:01:40 by Emil Karlström

killed all shift/reduce errors, oh my god fuck you

---
## [OHJ4Y/tgstation](https://github.com/OHJ4Y/tgstation)@[7bead07444...](https://github.com/OHJ4Y/tgstation/commit/7bead0744491b9beb91689d34ac12d142aca5b31)
#### Tuesday 2022-02-15 10:32:22 by John Willard

General pAI code improvements (#63688)

Fikou said they would've made MODsuits be controllable by pAI's rather than AI's, if pAI code wasn't as bad.

But pAI code ISN'T AS BAD AS AI CODE LIKE HOLY SHIT WHAT THE FUCK MAN???

Anyways, this is just general code improvements for pAIs that I thought would be nice to have.

Documents previously undocumented vars
Moves loose vars to be where they should be
Removes single-letter variables
Makes pAI a defined job
Moves vars around to where they should be while removing unused ones.
Makes pAI abilities its own .dm file
Replaces var/silent with Stun() (like cyborgs)
Reworks pAI's doorjack to not have a ton of procs, copy paste, and a reliance on Life(), instead it just uses a do_after()
Moves screwdrivering radios from attackby to screwdriver_act

Just general code improvement for Silicon, the thing no one likes or wants to touch.

---
## [JumperBot/JB](https://github.com/JumperBot/JB)@[4846018b5c...](https://github.com/JumperBot/JB/commit/4846018b5c157f0293f45f04fea741de96e4a7b0)
#### Tuesday 2022-02-15 12:14:31 by JumperBot_

✨ Lexer Yesterday, Sorter Tomorrow (#9)

Remember the **`Lexer`**?

We're now an **`interpreted`** language.

Next would be the **`Runner`!!!**

**`Classes`** are no more...

**`Lexer's`** a dream of the past!

---
## [zx2c4/linux-rng](https://github.com/zx2c4/linux-rng)@[fafe7c03c5...](https://github.com/zx2c4/linux-rng/commit/fafe7c03c538bff9165cbbe4e62c91464ab13b25)
#### Tuesday 2022-02-15 12:20:14 by Jason A. Donenfeld

random: use linear max-period irq entropy accumulator

>>> WORK IN PROGRESS, NOT YET FOR SUBMISSION, DO NOT REVIEW <<<

The current fast_mix() function is a piece of classic mailing list
crypto, where it just sort of sprung up without a lot of real analysis
of what precisely it was accomplishing. As a permutation of only two
rounds, there are some easily searchable differential trails in it, and
as a means of preventing malicious irqs, it completely fails, since it
xors new data into the entire state every time. It can't really be
analyzed as a random permutation, because it clearly isn't, and it
can't be analyzed as an interesting linear algebraic structure either,
because it's also not that. There really is very little one can say
about it in terms of entropy accumulation. It might diffuse bits, some
of the time, maybe, we hope, I guess. But for the most part, it fails to
accomplish anything concrete.

As a reminder, the simple goal of add_interrupt_randomness() is to
simply accumulate entropy until ~64 interrupts have elapsed, and then
dump it into the main input pool, which uses a cryptographic hash.

It would be nice to have something cryptographically strong in this
context, in case a malicious irq compromises a per-cpu fast pool within
the 64 interrupts / 1 second window, and then inside of that same window
somehow can control its return address and cycle counter, even if that's
a bit far fetched. However with a very CPU-limited budget, actually
doing that remains an active research project (and perhaps there'll be
something useful for Linux to come out of it). And while the abundance
of caution would be nice, this isn't *currently* the security model, and
we don't yet have a fast enough solution to make it our security model.
Plus there's not exactly a pressing need to do that. (And for the
avoidance of doubt, the actual cluster of 64 accumulated irqs still gets
dumped into our cryptographically secure input pool.)

So, for now we are going to stick with the existing irq security model,
which assumes that each cluster of 64 irq cycle counter samples are
mostly non-malicious and not colluding with an infoleaker. With this as
our goal, we can then endeavor to simply accumulate entropy linearly,
discarding the least amount of it, and make sure that accumulation is
sound, unlike the current fast_mix().

It turns out that this security model is also the trade off that other
operating systems have taken. The NT kernel, for example, uses something
very simple to accumulate entropy in interrupts, `x = ror32(x, 5) ^ m`.
Dodis et al. analyzed this in <https://eprint.iacr.org/2021/523>, and
found that rotation by 7 would have been better than 5, but that
otherwise, simple linear constructions like this can be used as an
entropy collector for 2-monotone distributions. However, when
considering this for our four-word accumulation, versus NT's one-word,
we run into potential problems because the words don't contribute to
each other, and some may well be fixed, which means we'd need something
to schedule on top. And more importantly, our distribution is not
2-monotone like NT's, because in addition to the cycle counter, we also
include in those 4 words a register value, a return address, and an
inverted jiffies. (Whether capturing anything beyond the cycle counter
in the interrupt handler is even adding much of value is a question for
a different time.)

So since we have 4 words, and not all of them are 2-monotone, we look
for a linear accumulator with proofs for more complex distributions. It
turns out that a max-period LFSR fits this bill quite well, easily
extending to the larger state size and the fact that we're mixing in
more than just the cycle counter. A max-period linear function has the
key advantage that it only has the trivial invariant subspace (0↦0),
rather than quite a few invariant subspaces like NT's rotate-xor, which
means we benefit from the analysis of <https://eprint.iacr.org/2021/1002>,
which gives proofs that linear functions with only trivial invariant
subspaces make very good entropy accumulators for the type of complex
distributions that we have.

This commit implementations one such very fast and high diffusion
max-period linear function, implemented in a Feistel-like fashion, which
pipelines quite well. On an i7-11850H, this takes 34 cycles, versus the
original's 65 cycles. (Though, as a note for posterity: if later this is
replaced with some sort of cryptographic hash function, I'll still be
keeping 65 cycles as my target 😋.) This Magma script, <https://א.cc/V1nFTMYE>,
proves that this construction does indeed yield a linear function of
order 2^128-1 whose minimal polynomial is primitive, and is therefore
max-period, fitting exactly what we need.

I mention "high diffusion" above, because that apparently was the single
discernible design goal of the original fast_mix(), even though that
didn't wind up helping anything with it. Nonetheless, we take care to
choose an LFSR with pretty high diffusion, perhaps even higher than the
original fast_mix(), which we can quantify by computing that the minimum
weight of the linear code is 10, versus around 8 if we treat the
original fast_mix() as linear as well. In other words, we probably don't
regress at all from a perspective of diffusion, even if it's not really
the goal here anyway.

In sum, the security model of this is unchanged from before, yet its
implementation now fixes that model much more rigorously. Plus the
performance is better, which perhaps matters in irq context.

As a final note, the previous fast_mix() was contributed by an anonymous
author, which, I've been told, has made some legally-minded people a bit
uncomfortable and is also against the kernel project's "real name"
policy.

Cc: Dominik Brodowski <linux@dominikbrodowski.net>
Cc: Theodore Ts'o <tytso@mit.edu>
Cc: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Cc: Eric Biggers <ebiggers@kernel.org>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>

---
## [newstools/2022-daily-dispatch](https://github.com/newstools/2022-daily-dispatch)@[5d08abced1...](https://github.com/newstools/2022-daily-dispatch/commit/5d08abced1835e050c9386f1ad131b92709468cc)
#### Tuesday 2022-02-15 12:44:35 by Billy Einkamerer

Created Text For URL [www.dispatchlive.co.za/news/2022-02-15-we-used-to-share-lunchboxes-and-laughs-shot-thembisa-nurse-honoured-by-colleagues-and-friends/]

---
## [Anemony22/Arborealis](https://github.com/Anemony22/Arborealis)@[7560f30111...](https://github.com/Anemony22/Arborealis/commit/7560f301116d827af4abb2b54e2ff1f70d2fda6e)
#### Tuesday 2022-02-15 15:08:39 by Ben Clark

The final piece - baked model rotations!

Thank you Jayden <3

... and fuck you Minecraft that was hard >:(

Co-Authored-By: FishTreeMan <39683679+FishTreeMan@users.noreply.github.com>

---
## [storyandfortune/bob](https://github.com/storyandfortune/bob)@[d5bd4f024f...](https://github.com/storyandfortune/bob/commit/d5bd4f024fb1ee84130efeac15bb0b2228712567)
#### Tuesday 2022-02-15 16:03:15 by storyandfortune@github.com

fuck you. what i put in my repo is my business. suck my dick you nosey fucking cunts.

---
## [Warcraft-GoA-Development-Team/Warcraft-Guardians-of-Azeroth-2](https://github.com/Warcraft-GoA-Development-Team/Warcraft-Guardians-of-Azeroth-2)@[a5946f267b...](https://github.com/Warcraft-GoA-Development-Team/Warcraft-Guardians-of-Azeroth-2/commit/a5946f267be861fb53cb265317e24ec064fc5b6a)
#### Tuesday 2022-02-15 18:26:42 by Loralius

holy site modifiers; amani, pandaren, jinyu doctrines

Ula-Tek and Karazhan now grant positive opinion from rulers of different faiths. Arcane is now shunned by Amani. Pandaren and Jinyu ignore life magic.

---
## [AlphaO612/TimeBox](https://github.com/AlphaO612/TimeBox)@[69d6ce8bd0...](https://github.com/AlphaO612/TimeBox/commit/69d6ce8bd055a6c55ef92594922947cbcbd10340)
#### Tuesday 2022-02-15 18:37:12 by Alpha

ver. 1.5 (legacy)
- added only for gen.html style file(style.css)
- fixed stopping bot without reason bug(3x times)
- fixed stopping spam error's msgs bug(bot)
-------------------------------------------
p.s. Guys, bad news!
Im tired to work at this a project.
Last month i thought i'll continue work to making better and better for all people of the university, but now...
I think, i'll must stop work at TimeBox at unknown time, bc for this web-site need refactor code and DB-system, but for me(The only one member of TimeBox's dev group) is so hard and annoying already!
Yeah, bad code is was a MY mistake, but this project, when i began to make it, made very fast only for work, not for comfortable work for Devs!
I change version's type from "alpha" to "legacy", because 50% code is so old and VERY-VERY bad(sry,my bad)!
Maybe sometimes i'll be make some commits in this project, but not often and, i guess, just for fix some bugs!
I hope, u understand me!
Thank u for read! Good bye! Good luck! Cya~!

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[6b2e5a5d34...](https://github.com/mrakgr/The-Spiral-Language/commit/6b2e5a5d34f4c5bac0e942483d81013cd33aa45c)
#### Tuesday 2022-02-15 18:42:54 by Marko Grdinić

"10:20am. Got up 20m ago. Let me chill a bit more and then I will start my studies of Houdini.

10:40am. Let me start.

https://youtu.be/hd9uMUz-nQA
orient attribute houdini

Rather than finish the course by Rohan I thought about investigating how the orient attribute works first.

https://youtu.be/hd9uMUz-nQA?t=61

Hmmm, is the last field in radians?

https://youtu.be/zjMuIxRvygQ
Quaternions and 3d rotation, explained interactively

Let me study quaternions just for a bit.

11am. https://youtu.be/d4EgbgTm0Bg?t=264
Visualizing quaternions (4d numbers) with stereographic projection

I knew that 3Blue1Brown was a popular math Youtuber, but his presentation is 10/10. It is my first time experiencing it.

It is really good to start each day fresh. I would never think of trying to learn quaternions at 7pm.

They are something I really should understand since I am trying to enter the 3d art field.

11:45am. Ok, I got some insight, but this is not what I thought. I thought maybe that the 4th field would be the rotation angle, but now I am not sure. What if the quaternion is not normalized?

I guess that would also translate it.

https://youtu.be/syQnn_xuB8U
Humane Rigging 03 - 3D Bouncy Ball 04 - Axis Angle & Euler Rotation

Let me watch this.

https://www.quantamagazine.org/the-strange-numbers-that-birthed-modern-algebra-20180906/

Actually, let me read this first.

https://youtu.be/syQnn_xuB8U?t=329

I wonder how he managed to make it so that the transforms only affect the inner parts?

https://youtu.be/4mXL751ko0w
Humane Rigging 03 - 3D Bouncy Ball 05 - Quaternion Rotation

Time for this.

> Conceptually confusing.
> Simple and gotcha-free in practice.

Yeah, I need to figure them out.

12:25pm. I am playing a bit with quaternion rotations in Blender. It seems that to make a 180 rotation, I'd need to put in infinity, but it does not work for me. This is actually rather complicated. Aren't angles simpler?

12:55pm. No I was wrong, giving quaternions an axis and w of 0 rotates it 180 degrees. Sigh, I have no idea why one would not just use axis angle instead.

https://www.youtube.com/watch?v=hd9uMUz-nQA
orient attribute houdini

Now that I understand quats, let me watch the above.

1pm. In Houdini it seems that w is the last value. Ok, I see.

https://www.sidefx.com/docs/houdini/vex/functions/qconvert.html

Hmmm, does the angle/axis vector represent the rotation magnitude using its norm?

I am guessing it is the L1 norm rather than the L2.

...Though it woudln't be a problem either way. If it is the L2 norm, whem multiplying the vector by a scalar you just have to pass it through the square root first.

1:20pm. https://youtu.be/dcM2ROPx0qs?t=232
Orienting and Rotating Copies with VOPs – Houdini Attributes and VOPs ep. 9

This is interesting. I should focus in order to figure out what this is doing. Understanding how to manipulate and rotate objects is a such a fundamental skill in not just Houdini, but any 3d package.

Still, this is a 20m video and I am overdue for breakfast. Let me do the chores here.

I am quite into this.

2:30pm. Let me resume. Done with chores and breakfast. I had an idea to try out something, but I forgot what it was. My thoughts are scattered everywhere. Well, let me watch the video.

Maybe it will come to me.

https://youtu.be/dcM2ROPx0qs?t=408

Why does he keep using the Facet node to compute normals instead of the Normal node?

2:55pm. Finished the vid. Let me take a break.

https://www.youtube.com/playlist?list=PLFkMNnEYa3AP1ljfLNA4d7lqIgwKbUwHM

I'll leave this playlist for later. It is time I finish the course by Rohan.

3:10pm. Let me start.

https://www.iamag.co/free-tutorial-creating-art-in-houdini/

Here it was.

3:15pm. I am hearing thunder. Maybe I'll have to run if I hear it a few more times.

3:20pm. Holy shit, he got the ripple effect by connecting a noise texture to bump.

3:25pm. I'll have to turn off. Let me just finish the vid. 3m more.

Done with vid 8. Sigh, this looks so good. If somebody told me this is 3d I wouldn't have believed him. It looks like an actual painting.

Since I am not hearing anything, let me start the final vid.

3:40pm. https://www.iamag.co/tag/houdini/

This site has a lot of Houdini stuff, but I had to use Google to find it. Its inbuilt search is so shitty. Sometimes that is the case with sites. Search engines can be better than their own search function.

Let me take a look at that tutorial I linked to yesterday. I want to study more today.

https://www.youtube.com/playlist?list=PL2SMrYpOIl0McqZHMV7dONrmIpJTY2WpH
Houdini For The New Artist

It was this. Let me take a look.

3:55pm. https://youtu.be/LMhDBkWmGg0?list=PL2SMrYpOIl0McqZHMV7dONrmIpJTY2WpH

The first ep is a bit too basic for me, but this should be instructive.

https://youtu.be/LMhDBkWmGg0?list=PL2SMrYpOIl0McqZHMV7dONrmIpJTY2WpH&t=68

I had no idea about this project stuff. I should have used it for the pool scene.

4:10pm. Ah, I just figured out how to do the pool water for arbitrary pools, even non convex ones.

I just have to separate the original groups from the newly created hollows.

Then I take the hollow group, polyfill it, and from that derive the water.

4:15pm. Hmmm, but that would leave me in a bad spot with booleans. Suppose instead I closed the top of the pool by unioning it with a plane. That would leave a bunch of primitives on the inside of the geometry. I am not sure if I could use the PolyDoctor node, but there is no dobut a way to do it.

4:15pm. Hmmm, since the pool had a particular shape what if I clipped it at a certain point and then used the connectivity node? I should just ask. There should a really simple way of doing this.

Instead of asking in the /3/ thread, I should ask on that Houdini forum.

Now let me go back to the course.

https://youtu.be/LMhDBkWmGg0?list=PL2SMrYpOIl0McqZHMV7dONrmIpJTY2WpH&t=693

Even a beginner course like this has something new for me. I had no idea about the PolyReduce.

https://youtu.be/2gFPBhzxoDQ?list=PL2SMrYpOIl0McqZHMV7dONrmIpJTY2WpH&t=40

Ah, so this is how you add a HDRI. As a env light rather than a texture.

https://youtu.be/l1THANbGhRA?list=PL2SMrYpOIl0McqZHMV7dONrmIpJTY2WpH&t=251

I wonder if there is a builder for objects?

https://youtu.be/l1THANbGhRA?list=PL2SMrYpOIl0McqZHMV7dONrmIpJTY2WpH&t=261

Houdini has a crazy amount of complexity in its shader nodes compared to Blender.

https://youtu.be/l1THANbGhRA?list=PL2SMrYpOIl0McqZHMV7dONrmIpJTY2WpH&t=393

Principled Shader Core simplifies the principled shader.

4:50pm. I am starting to hear thunder again. Just a bit more and I'll shut down if it persists.

https://youtu.be/l1THANbGhRA?list=PL2SMrYpOIl0McqZHMV7dONrmIpJTY2WpH&t=522

Oh this is nice. You can use snapping to aim at something. This would work in Blender as well, but it never occured to me to try it.

https://youtu.be/l1THANbGhRA?list=PL2SMrYpOIl0McqZHMV7dONrmIpJTY2WpH&t=925

Adding objects like this is not something I would have thought of.

5:15pm. Ahhhhhhh...I know what I was thinking of. Remember that leaf tutorial. Instead of the sweep node, would it have been possible to use the divide node instead? Let me give it a try.

5:25pm. PolyPatch works exactly like sweep when it comes to connecting cross sections ends, except it is more principled. It even has an option to allow me to plug in the number of divisions. I think that sweep probably passes it through PolyPatch under the hood.

5:30pm. Ok, let me get back to the CGForge videos.

6pm. Done with the CGForce free stuff. Right now I am going over the TOC for the Hipflash courses to crib ideas for what I should study. Also, now that I am looking at the prices for these courses I see that they are even more expensive than what I thought. I could afford about 2-3 before it emptied my wallet.

6:05pm. Lunch time.

6:50pm. Let me resume. I think that at this point I have enough to finish the modeling stage tomorrow and move on to texturing.

That having said, I want to play with the pool. Let me see if I can get my desire to bear fruit.

7:05pm. I played around and I figured out that group expand could be used to do flood fill selection. Great!

I thought that clip would add a surface, but I was wrong it just removes mesh. This is actually better for me as I'd have to figure out how to remove the top if it did.

7:10pm. Wow, I love this. This went so much better than I was expecting. I can use this for any kind of pool.

7:15pm. I also figured out how to enter isolation mode. Right click opens up the view menu. The hotkey is Y. Good, good, good...

Now I am trying to figure out how to get thicken to work, but it is not working.

7:20pm. Well, it does not matter. I can just scale it by 0.999.

7:30pm. No, let me not do that. I saw that in one tutorial, but it is a waste of time.

7:35pm. Let me close here. Tomorrow I will attach some planar patches to those hooks and simulate them. That will give me the towels. After that I'll move to the texturing, lighting and shading. After that comes a trip back into sculpting.

https://www.youtube.com/playlist?list=PLFkMNnEYa3AP1ljfLNA4d7lqIgwKbUwHM

Oh yeah, I should keep this guy in mind and check him out. I'll do it after I am done with the scene. The same goes for the rest of the tuts on the Houdini main site."

---
## [SoCuul/d3w](https://github.com/SoCuul/d3w)@[1173d404f6...](https://github.com/SoCuul/d3w/commit/1173d404f6854836a381ab2817eb8df9019c0628)
#### Tuesday 2022-02-15 20:18:37 by Tartt

Finished Starbucks

what a fucking pain in the ass holy shit

---
## [noahshaw11/couchdb](https://github.com/noahshaw11/couchdb)@[77f34a1bbc...](https://github.com/noahshaw11/couchdb/commit/77f34a1bbc7c76aefa59777da21e2e76e79f7ec8)
#### Tuesday 2022-02-15 20:33:04 by Adam Kocoloski

Refactor Jenkins to dynamically generate stages

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

* Defaults to Erlang 23 as the embedded Erlang version in packages. We
  avoid Erlang 24 for now because Clouseau is not currently compatible.

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

This is a cherry-pick of 9b6454b with the following modifications:

- Drop the MINIMUM_ERLANG_VERSION to 20
- Drop the packaging ERLANG_VERSION to 23
- Add the weatherreport-test as a build step
- Add ARM and POWER back into the matrix using a new buildx-based
  multi-architecture container image.

---
## [mrcreepysos/pd2promod](https://github.com/mrcreepysos/pd2promod)@[328ea8c523...](https://github.com/mrcreepysos/pd2promod/commit/328ea8c5234c0987e1be8034134a03b855e73254)
#### Tuesday 2022-02-15 20:53:39 by mrcreepysos

i stg this has to be the last push for this branch

replace the copbase code with a much cleaner one, huge thank you RedFlame for this
nerf trigger happy, it allowed pistols to melt dozers waaay too quickly
nerf famas, holy shit that thing was insane

---
## [TorannD/RWoM](https://github.com/TorannD/RWoM)@[5b5e8ea252...](https://github.com/TorannD/RWoM/commit/5b5e8ea25231358a84865efd237d2470d0752132)
#### Tuesday 2022-02-15 21:29:39 by TorannD

v2.6.6.0

New:
 o Supporting magic traits:
	- Giants Blood: descendant of giants - endowed with with great strength and stamina, but slow to recover
	- Fae Blood: descendant of fae folk with a natural connection to the arcane
	- Enlightened: blessed by magic, able to harness its power without suffering the full side-effects
	- Cursed: tormented by a constant, burning rush of power that inflicts arcane weakness...

 o New class abilities for Empath and Apothecary
  - Apothecary:
	>Fire Suppression Flask (class skill)- ingredients that instantly smother fire in an area
	>Bliss (learnable scroll) - concoction that puts a pawn into a state of euphoria where pain and emotions are inconsequential, but slowly reduces skills and causes a major penalty for skill learning
	>Clarity (learnable scroll) - potion which reduces resistance to the arcane; increases mana regeneration and psychic sensitivity and the cost of mental stability

  - Empath:
   >Symbiosis (class skill) - entwines the will of an empath with another, granting great mental fortitude and awareness; the empath's presence remains with the host for the duration of this ability, leaving the body of the empath as an empty shell
   >Faded Emotions (learnable scroll) - causes the target pawn to address their emotions directly to get over whatever causes their negative mood

 o Standalone spell Magic Wardrobe - swaps apparel with an apparel set stored in a dimension pocket (apparel sets not included)
 o Fire Mage spell Heat Shield - temporary protection against heat damage and prevents pawns from catching fire
 o Ice Mage spell Alter Storm - alters rainy or snowy weather with unique conditions
 o Golemancer's can create a body tattoo using rune carving techniques that grant enchantment bonuses - if using ideology, the pawn will get a new body tattoo
 o Standalone and learnable abilities can now be configured to autocast
 o Hediffs can accept enchantments using a per stage def extension (see Clarity hediff for example)
 o Weather event: Hail storm - found mostly in cold climates, hail storms may cause injury to exposed pawns; will not puncture a roof

*new abilities will only be discovered for new classes - existing classes will not be able to retroactively learn the new abilities but will be able to gain the new skills if their class is cleared using a shard of extraction and then the same (or another) class gained

Tweaks:
 o Techno turret no longer needs to be manned; default duration is 60s and can be upgraded to last longer
 o Charge Battery spell can be used to charge golems
 o Hail storm and Healing rain weather events may occur (uncommonly) on standard maps under the right conditions
 o Apothecary gathers ingredients while caravaning based on their forage rate and gathering skill
 o Transmuting equipment made from stuff now has a minimum (10%) and maximum value (300%) relative to the value of the original stuff

Bug fixes:
 o Transpose will correctly assign drafted status and reversal hediff when used on, or by, a non-colonist pawn (t)
 o Golem drafted orders
 o Player rifts from Voidseeker role will no longer drop resources

---
## [LuanVSO/terminal](https://github.com/LuanVSO/terminal)@[b1ace967a2...](https://github.com/LuanVSO/terminal/commit/b1ace967a2f2bf17fdcb7dd4f1426b014378b83c)
#### Tuesday 2022-02-15 21:47:51 by Mike Griese

Two belling fixes (#12281)

Sorry for combining two fixes in one PR. I can separate if need be.

* [x] Closes #12276:
  - `"bellSound": null` didn't work. This one was easier, and is atomically in bcc2ca04fc14f39f37849b4bd837ad6cdb4cdaaa. Basically, we would deserialize that as an array with a single empty string in it, which we'd try to then play. I think it's more idomatic to have that deserialized as an empty array, which correctly falls back to playing the default sound.
* [x] Closes #12258: 
  - This one is the majority of the rest of the PR. If you leave the MediaPlayer open, then the media keys will _affect the Terminal_. More importantly, once the bell sounds, they'd replay the bell, which is insane. So the fix is to re-create the media player when we need it. We do this per-pane for simpler lifetime tracking. I'm not worried about the overhead of creating a mediaplayer here, since we're already throttling bells.
* Originally added in #11511
* [x] Tested manually
  - Use [`no.mp4`](https://www.youtube.com/watch?v=x2w9TyCv2gk) for this since that's like, 17s long
  - Checked that closing panes / the terminal while a bell was playing didn't crash
  - Playing a bunch of bells at once works
  - closing a pane stops the bell it's playing
  - once the bell stops, the media keys went back to working for Spotify
* [x] I work here

---
## [spinnaker/gate](https://github.com/spinnaker/gate)@[e2a108db75...](https://github.com/spinnaker/gate/commit/e2a108db759f1cdfe89c8ac6bd3fafc10c39ac8e)
#### Tuesday 2022-02-15 22:33:06 by Chris Phillips

fix(authn/oauth2): prevent oauth2 redirect loops (#1517)

During setup of spinnaker authentication with oauth2 a common hurdle is a redirect loop.

For example:

https://github.com/spinnaker/spinnaker/issues/5794
https://github.com/spinnaker/spinnaker/issues/1630

Also, many threads in Slack discuss these problems. In fact this appears to be a common
pitfall for the spring-security-oauth2-autoconfigure library in general. A light refresher
on the ouath2 flow in play here seems worthwhile. The user is redirected from `/login` in gate
to the external auth provider (google, github, etc.) and after successfully authenticating
they are redirected back to the gate `/login` endpoint but this time with a code parameter
that is to be used to request an access token.

This request can fail for a variety of reasons, and if it does, the underlying spring library
triggers a redirect to the `/error` endpoint. What causes the redirect loop for gate in particular
(and for other users of the library in a similar fashion) is that the WebSecurityConfigurerAdapter
in play is treating `/error` as an authenticated path and so instead of just returning with a 401,
it re-redirects to `/login` and the redirect loop continues.

My thought is that instead of a redirect loop, simply allowing the 401 to be returned will be a stronger
more helpful signal as to what is going on. Hopefully it will save future first-time installers headaches.

Spinnaker docs have included several troubleshooting hints and tips for how where you terminate SSL
affects configuration etc. Even after following all of these and lots of spelunking through spinnaker
github issues and combing over threads in slack, I found myself still experiencing a redirect loop even
though I had applied all the combined wisdom that was applicable to my setup.

As it turns out, I had a bad copy/paste of my client secret in my configuration. So the request
to turn the code from google into an access token from google was failing with a 401. After much
debugging and deep diving into the spring security code I found that had I turned on DEBUG in gate
for these classes in gate-local.yml:

```
logging:
  level:
    org.springframework.security.web.authentication.SimpleUrlAuthenticationFailureHandler: DEBUG
    org.springframework.security.oauth2.client.filter.OAuth2ClientAuthenticationProcessingFilter: DEBUG
```

Then I would have seen in the logs that a 401 response was returned from google and perhaps it would have
caused me to look closer at my botched client secret configuration. I think perhaps we don't want to require
that all operators of spinnaker become spring-security-oauth2 experts. So I'm proposing adding `/error` to
the list of paths in gate that aren't treated as authenticated. Thus short-circuiting the redirect loop and
bringing to light helpful troubleshooting info that was previously more or less swallowed.

---
## [VallentinDS/Foobar-Google-Challenge-2022](https://github.com/VallentinDS/Foobar-Google-Challenge-2022)@[2455516a2d...](https://github.com/VallentinDS/Foobar-Google-Challenge-2022/commit/2455516a2d58253aa0fee0ff44ebd2adab06f28c)
#### Tuesday 2022-02-15 22:35:28 by VallentinDS

Add files via upload

As a henchman on Commander Lambda's space station, you're expected to be resourceful, smart, and a quick thinker. 
It's not easy building a doomsday device and ordering the bunnies around at the same time, after all! 
In order to make sure that everyone is sufficiently quick-witted, Commander Lambda has installed new flooring outside the henchman dormitories. 
It looks like a chessboard, and every morning and evening you have to solve a new movement puzzle in order to cross the floor. 
That would be fine if you got to be the rook or the queen, but instead, you have to be the knight. 
Worse, if you take too much time solving the puzzle, you get "volunteered" as a test subject for the LAMBCHOP doomsday device!

To help yourself get to and from your bunk every day, write a function called solution(src, dest) which takes in two parameters: 
the source square, on which you start, and the destination square, which is where you need to land to solve the puzzle.  
The function should return an integer representing the smallest number of moves it will take for you to travel from the source 
square to the destination square using a chess knight's moves (that is, two squares in any direction 
immediately followed by one square perpendicular to that direction, or vice versa, in an "L" shape).  
Both the source and destination squares will be an integer between 0 and 63, inclusive, and are numbered like the example chessboard below:

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

---
## [pooneh-m/agones](https://github.com/pooneh-m/agones)@[40e6e50fb5...](https://github.com/pooneh-m/agones/commit/40e6e50fb52f559693f8b5d91a32bfcbb1bd5887)
#### Tuesday 2022-02-15 22:48:52 by Mark Mandel

Update minikube dev tooling (#1906)

Needed to update minikube to Kubernetes 1.17.x and I figured I would
also go through the minikube dev experience and update it.

This includes:

* Switch to default to the Docker driver, since everyone should have
  Docker installed.
* Removing the Windows hacks, because they were awful and I feel bad I
  even wrote them in the first place.
* Migrate tooling to use new minikube functionality
* Update minikube commands to up to date release conformity.
* Updated the documentation

Work on #1824

---
## [mrcreepysos/pd2promod](https://github.com/mrcreepysos/pd2promod)@[ebefa06a77...](https://github.com/mrcreepysos/pd2promod/commit/ebefa06a77934a3d54c04403ed1e78c6ce074fe1)
#### Tuesday 2022-02-15 23:37:56 by mrcreepysos

nerf enemy health across the board

bruh holy shit 4 shot headshot tasers with 160dmg rifles
mfw zerker was too fucking good

dozer crit mul was increased to 3.2 (normal headshot multiplier)
tasers are at 1800 health now, medics went down to 1200, shields are at 600
spoocs went down to 2400

---

