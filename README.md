## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-03-26](docs/good-messages/2022/2022-03-26.md)


1,539,732 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,539,732 were push events containing 2,215,301 commit messages that amount to 130,743,642 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 40 messages:


## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[55336d1e53...](https://github.com/timothymtorres/tgstation/commit/55336d1e5308789be1616413c8d8f87e073f7302)
#### Saturday 2022-03-26 00:55:46 by vincentiusvin

Atmos Control Console Refactor (and syndiebase atmos tidyup) (#65372)

Main Takeaways For Mappers:

Use monitored pathed atmos devices very carefully. Also dont put atmos_sensors willy nilly. They are used to hook to atmos control monitors.

We want to keep at most one device broadcasting for each of the atmos sensor, inlets, and outlets. Run the mapping verb Check Atmos Chamber Devices to be sure, though this might not catch everything.

Some of the warning are pretty harmless. For example if you have reconnected the "station atmos monitor" and you get no listener for distro/waste loop warning, it's safe to ignore.

I don't know what the maptainer policy is on making new subtypes for offstation content, but if you do please branch off the general ones instead of the specific gas ones. If you aren't making a new subtype, varedit the general ones too.

About The Pull Request:

Need Would prefer this to be merged before #65271 (In game atmos guide).
Not strictly necessary, just makes me sleep better knowing the handbook wont die alongside the rest of the UI.

Fixes #36668 (Atmos Monitoring Consoles don't update it's sensors to the new tank after reconnect())
Fixes #32122 (Mix console fucked after reconnecting it)

Also made the distro meter thing broadcast more info instead of just the pressure, because I'm sure nobody would care and it would make my life easier.

A small high-level overview in case this breaks again in the future:

A signal datum (not DCS) is sent by the atmospheric devices (injectors and vents) and will be received by the atmos computers. The data is then stored at the monitor object and then passed to the UI. This initial signal is sent by `broadcast_signal()`, called by `atmos_init()`.

New sensors/vents (if you can actually get them in game, still only adminspawn/wrenchables afaik) will also initiate the conversation if atmos_init() is called, so it works fine. This means you need to unwrench and re-wrench the devices if you adminspawn them though, ugh.

In case of a newly built computer, it needs to be the one that prompt the data to the devices, so we send a request signal. This is a bit inefficient since it doesnt work off of callbacks and assocs like DCS, but won't really matter since we're doing this rarely.

We only talk with the injectors and vents when necessary here, while sensors and meters keep beeping with every process_atmos() tick so they rarely break.


Why It's Good For The Game:

Messy code gone (debatable).


Refactored the atmos control console devices. The ones that hook to the big turf chambers.
Distro meter now broadcast the whole gasmix info instead of just pressure to the monitors.
Lavaland syndie's atmos chamber vents are now actually configurable. Moved a few things around to accomodate this.
Lavalannd syndie chambers hooked to distro and moved distro pipe to layer2
atmos monitors can detect reactions now.
Some minor code changes to how anomaly refinery and implosion compressor show the gas info. No changes expected, report if bug.
recoded checks for atmos chamber abnormalities in debug verbs.

---
## [axietheaxolotl/Skyrat-tg](https://github.com/axietheaxolotl/Skyrat-tg)@[5c1e69aa44...](https://github.com/axietheaxolotl/Skyrat-tg/commit/5c1e69aa448e6e28738b4643a54bb104ee032555)
#### Saturday 2022-03-26 01:05:31 by SkyratBot

[MIRROR] Fixes borg wallmounting [MDB IGNORE] (#12046)

* fixes wallmounts (#65408)

closes #65393 (Engineering Cyborgs can't place APC or Air alarm frames on walls anymore)
fixes the code error in #64428 (afc1e44ee2922a316feb958249f7806568953bbe)

basically what occured is that he typed out the T(turf) attackby proc to input the screwdriver as an arg rather then the wallmount, remember, you want the WALLMOUNT to hit the wall to place it, not the screwdriver, that just creates runtimes and doesnt place anything

EDIT: actually re-reading it, what it was actually doing was using the screwdriver as the user arg, and trying to smash the user into the wall, thats actually kinda funny

borgo wallmounting is a good thing, good borgos need their treats

* Fixes borg wallmounting

Co-authored-by: 小月猫 <alina.r.starkova@gmail.com>

---
## [Tiktodz/android_kernel_asus_sdm636](https://github.com/Tiktodz/android_kernel_asus_sdm636)@[97408688c8...](https://github.com/Tiktodz/android_kernel_asus_sdm636/commit/97408688c898b3a0dfad71d49af98a5d41642021)
#### Saturday 2022-03-26 01:34:06 by Dave Chiluk

sched/fair: Fix low cpu usage with high throttling by removing expiration of cpu-local slices

commit de53fd7aedb100f03e5d2231cfce0e4993282425 upstream.

It has been observed, that highly-threaded, non-cpu-bound applications
running under cpu.cfs_quota_us constraints can hit a high percentage of
periods throttled while simultaneously not consuming the allocated
amount of quota. This use case is typical of user-interactive non-cpu
bound applications, such as those running in kubernetes or mesos when
run on multiple cpu cores.

This has been root caused to cpu-local run queue being allocated per cpu
bandwidth slices, and then not fully using that slice within the period.
At which point the slice and quota expires. This expiration of unused
slice results in applications not being able to utilize the quota for
which they are allocated.

The non-expiration of per-cpu slices was recently fixed by
'commit 512ac999d275 ("sched/fair: Fix bandwidth timer clock drift
condition")'. Prior to that it appears that this had been broken since
at least 'commit 51f2176d74ac ("sched/fair: Fix unlocked reads of some
cfs_b->quota/period")' which was introduced in v3.16-rc1 in 2014. That
added the following conditional which resulted in slices never being
expired.

if (cfs_rq->runtime_expires != cfs_b->runtime_expires) {
	/* extend local deadline, drift is bounded above by 2 ticks */
	cfs_rq->runtime_expires += TICK_NSEC;

Because this was broken for nearly 5 years, and has recently been fixed
and is now being noticed by many users running kubernetes
(https://github.com/kubernetes/kubernetes/issues/67577) it is my opinion
that the mechanisms around expiring runtime should be removed
altogether.

This allows quota already allocated to per-cpu run-queues to live longer
than the period boundary. This allows threads on runqueues that do not
use much CPU to continue to use their remaining slice over a longer
period of time than cpu.cfs_period_us. However, this helps prevent the
above condition of hitting throttling while also not fully utilizing
your cpu quota.

This theoretically allows a machine to use slightly more than its
allotted quota in some periods. This overflow would be bounded by the
remaining quota left on each per-cpu runqueueu. This is typically no
more than min_cfs_rq_runtime=1ms per cpu. For CPU bound tasks this will
change nothing, as they should theoretically fully utilize all of their
quota in each period. For user-interactive tasks as described above this
provides a much better user/application experience as their cpu
utilization will more closely match the amount they requested when they
hit throttling. This means that cpu limits no longer strictly apply per
period for non-cpu bound applications, but that they are still accurate
over longer timeframes.

This greatly improves performance of high-thread-count, non-cpu bound
applications with low cfs_quota_us allocation on high-core-count
machines. In the case of an artificial testcase (10ms/100ms of quota on
80 CPU machine), this commit resulted in almost 30x performance
improvement, while still maintaining correct cpu quota restrictions.
That testcase is available at https://github.com/indeedeng/fibtest.

Fixes: 512ac999d275 ("sched/fair: Fix bandwidth timer clock drift condition")
Signed-off-by: Dave Chiluk <chiluk+linux@indeed.com>
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Reviewed-by: Phil Auld <pauld@redhat.com>
Reviewed-by: Ben Segall <bsegall@google.com>
Cc: Ingo Molnar <mingo@redhat.com>
Cc: John Hammond <jhammond@indeed.com>
Cc: Jonathan Corbet <corbet@lwn.net>
Cc: Kyle Anderson <kwa@yelp.com>
Cc: Gabriel Munos <gmunoz@netflix.com>
Cc: Peter Oskolkov <posk@posk.io>
Cc: Cong Wang <xiyou.wangcong@gmail.com>
Cc: Brendan Gregg <bgregg@netflix.com>
Link: https://lkml.kernel.org/r/1563900266-19734-2-git-send-email-chiluk+linux@indeed.com
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Signed-off-by: Ratoriku <a1063021545@gmail.com>
Signed-off-by: Peppe289 <gsperanza204@gmail.com>

---
## [Emisse/space-station-14](https://github.com/Emisse/space-station-14)@[89e6e5ead9...](https://github.com/Emisse/space-station-14/commit/89e6e5ead98f981cc6b08d6e523c15c012ea7c8a)
#### Saturday 2022-03-26 01:37:24 by Emisse

Merge branch 'space-wizards:master' into shitty-ass-branch-annoying

---
## [oxen-io/session-pysogs](https://github.com/oxen-io/session-pysogs)@[31bfd14d80...](https://github.com/oxen-io/session-pysogs/commit/31bfd14d80ec723fde3c3589408a27fc878f247f)
#### Saturday 2022-03-26 02:44:57 by Jason Rhinelander

Use SQLAlchemy for database backend

We're using it fairly minimally: essentially still writing manual
queries, but now using SQLAlchemy to handle placeholder binding which is
nicer, and portable.

The API now goes like this:

- `db.get_conn()` returns a connection from the connection pool;
  web.appdb, in particular, is a preloaded, app-context connection
  object that most code uses.

- `web.query()` does an SQLAlchemy 'text' query, which is almost like
  regular prepare+bind+execute, except that it always uses `:name` for
  placeholders and binds using `name=...` keyword arguments.  That is,
  instead of:

      db.execute("SELECT token FROM rooms WHERE id = ?", (123,))

  we now do:

      query("SELECT token FROM rooms WHERE id = :id", id=123)

  or equivalently:

      db.query(appdb, "SELECT token FROM rooms WHERE id = :id", id=123)

  (the latter version is more useful where an app context doesn't exist
  and you need to pass in some other conn, such as is now done in
  __main__).

- transactions are now controlled with a `with appdb.begin_nested():`
  context, replacing the custom nested tx handler I made for sqlite.

We *could* start using more advanced SQLAlchemy query composition, but
that seems like more of a pain rather than something useful.  (I *don't*
want to use SQLAlchemy ORM, because in my experience ORM just gets in
the way as soon as you want non-trivial database structure, which we
have here).

This will allow us to (easily) add postgresql support.  (Other database
are probably a no-go: SQLite has long looked up to postgresql for
features and syntax and so the two are very similar dialects).

---
## [kakoc/nearcore](https://github.com/kakoc/nearcore)@[6351eb5511...](https://github.com/kakoc/nearcore/commit/6351eb55116fea2f906d681ce6966b5ec2546176)
#### Saturday 2022-03-26 03:17:38 by Simonas Kazlauskas

Use non-blocking log writer (#6470)

This will utilize a separate thread to write out the spans and events
without while letting the main computation to proceed with its business.
Additionally, we are buffering the output by lines, thus reducing the
frequency of syscalls that can occur when the subscriber is writing out
parts of the message.

This should mitigate concerns of enabling debug logging as its impact on
performance should now be minimal (putting an event structure onto a
MPSC queue.) There are still costs associated with logging everything
however. Most notably formatting and construction of the
`tracing_core::ValueSet`s still occur on the caller side, so if
constructing those is expensive, the logging might remain expensive.
An example of code sketchy like that (although silly) could be:

```
debug!(message = { std::time::sleep(Duration::from_secs(1)); "hello" })
```

or for a less silly example:

```
debug!("{}", my_vector.iter().map(|...| {
  do_expensive_stuff()
}).collect::<String>())
```

These should be considered a bug (alas one that `tracing` does not have
any tooling to detect, sadly.)

I opted adding a new crate dedicated to observability utilities. From my
experience using things like prometheus will eventually result in a
variety of utilities being written, so this crate eventually would
likely expand in scope...

Fixes https://github.com/near/nearcore/issues/6072 (though I haven't made any actual measurements as to what the improvement really is)

---
## [Sedna-Games/Zero-Possession-Prototype](https://github.com/Sedna-Games/Zero-Possession-Prototype)@[5728d2d81c...](https://github.com/Sedna-Games/Zero-Possession-Prototype/commit/5728d2d81c1408e5e97f6d439c1e65cf95e6c402)
#### Saturday 2022-03-26 04:31:13 by Hamraj

[WIP] First 3 Buildings LD Set Dressing Good

- holy fuck takes time to get these done and think of cool designs for the levels and make shit interesting but its getting there bois and gals

---
## [morgoth1145/advent-of-code](https://github.com/morgoth1145/advent-of-code)@[f5e9c3d3a0...](https://github.com/morgoth1145/advent-of-code/commit/f5e9c3d3a07b0e73da901250a06212f41b31cc09)
#### Saturday 2022-03-26 04:46:45 by Patrick Hogg

2019 Day 17 Part 2

Now for the really fun part of this problem. The first part here is extracting the sequence of steps the robot needs to take to traverse the entire scaffold. Technically there is some ambiguity in the problem (the robot could turn at any given intersection) but we just need to follow the path and turn whenever a turn is forced.

The second part is the really crazy bit though. That path needs to be compressed into a <= 20 character main program and 3 <= 20 character functions. Back in 2019 I did this step by hand initially. That's 100% the right way to do it to try to leaderboard, but this time I decided to challenge myself and solve it programatically with no hand solving.

The basic idea is a backtracking search. At any given point see if an already deduced subprogram matches the next sequence of steps that remain. If so, add that to the main program and search further. If we can't find one that matches (or if the main program gets too long and we backtrack), try and find a new subprogram (assuming we have room, we max at 3!) and see if that works. And if that fails, trim the subprogram until it's empty or we find a solution.

I did of course hit some bugs in this process as it's somewhat involved.
1) Most annoyingly, I had the wrong overall sequence to start out due to having the bot face down initially. (I always invert my y!)
2) I accidentally computed the subprogram length to be len(remaining_steps) in find_solution at one point. Unluckily it didn't hit an exception but returned a garbage solution!
3) I also got tripped up by forgetting to convert my characters back to ints to pass to the subprogram, and with forgetting to put a newline after disabling the continuous camera feed!

Still, I did programmatically solve this in a respectable amount of time. This part really screams to be solved by hand if you want to be fast.

Would have missed the leaderboard by ~5.5 minutes. In fact, I was ~6.75 minutes slower than in 2019, but I did this part by hand in 2019. I'm not too mad about my showing here :)

Time: 0:50:47.789638

---
## [SamuraiAku/julia](https://github.com/SamuraiAku/julia)@[62e0729dbc...](https://github.com/SamuraiAku/julia/commit/62e0729dbc5f9d5d93d14dcd49457f02a0c6d3a7)
#### Saturday 2022-03-26 04:58:39 by Mirek Kratochvil

avoid using `@sync_add` on remotecalls (#44671)

* avoid using `@sync_add` on remotecalls

It seems like @sync_add adds the Futures to a queue (Channel) for @sync, which
in turn calls wait() for all the futures synchronously. Not only that is
slightly detrimental for network operations (latencies add up), but in case of
Distributed the call to wait() may actually cause some compilation on remote
processes, which is also wait()ed for. In result, some operations took a great
amount of "serial" processing time if executed on many workers at once.

For me, this closes #44645.

The major change can be illustrated as follows: First add some workers:

```
using Distributed
addprocs(10)
```

and then trigger something that, for example, causes package imports on the
workers:

```
using SomeTinyPackage
```

In my case (importing UnicodePlots on 10 workers), this improves the loading
time over 10 workers from ~11s to ~5.5s.

This is a far bigger issue when worker count gets high. The time of the
processing on each worker is usually around 0.3s, so triggering this problem
even on a relatively small cluster (64 workers) causes a really annoying delay,
and running `@everywhere` for the first time on reasonable clusters (I tested
with 1024 workers, see #44645) usually takes more than 5 minutes. Which sucks.

Anyway, on 64 workers this reduces the "first import" time from ~30s to ~6s,
and on 1024 workers this seems to reduce the time from over 5 minutes (I didn't
bother to measure that precisely now, sorry) to ~11s.

Related issues:
- Probably fixes #39291.
- #42156 is a kinda complementary -- it removes the most painful source of
  slowness (the 0.3s precompilation on the workers), but the fact that the
  wait()ing is serial remains a problem if the network latencies are high.

May help with #38931

Co-authored-by: Valentin Churavy <vchuravy@users.noreply.github.com>

---
## [sixthEarthAngel/sixthEarthAngel](https://github.com/sixthEarthAngel/sixthEarthAngel)@[1b5c5a88b3...](https://github.com/sixthEarthAngel/sixthEarthAngel/commit/1b5c5a88b30fc819c035146edd014f97482d5c33)
#### Saturday 2022-03-26 05:22:20 by sixthEarthAngel

Create Gods Constant Universe

This is a place where the Sweet Prince manifest to save Christopher Abbott and removes the curses in his life and restores him as the living God of E

---
## [RajaKunalPandit1/CodeForces_Questions](https://github.com/RajaKunalPandit1/CodeForces_Questions)@[6de8bd6014...](https://github.com/RajaKunalPandit1/CodeForces_Questions/commit/6de8bd6014d861356d7d01a848b5b6d68f907990)
#### Saturday 2022-03-26 05:22:34 by Raja Kunal Pandit

Create 489B - BerSU Ball.cpp

Output Status : 

By Rajakunalpandit, contest: Codeforces Round #277.5 (Div. 2), problem: (B) BerSU Ball, Accepted

The Berland State University is hosting a ballroom dance in celebration of its 100500-th anniversary! n boys and m girls are already busy rehearsing waltz, minuet, polonaise and quadrille moves.

We know that several boy&girl pairs are going to be invited to the ball. However, the partners' dancing skill in each pair must differ by at most one.

For each boy, we know his dancing skills. Similarly, for each girl we know her dancing skills. Write a code that can determine the largest possible number of pairs that can be formed from n boys and m girls.

Input
The first line contains an integer n (1 ≤ n ≤ 100) — the number of boys. The second line contains sequence a1, a2, ..., an (1 ≤ ai ≤ 100), where ai is the i-th boy's dancing skill.

Similarly, the third line contains an integer m (1 ≤ m ≤ 100) — the number of girls. The fourth line contains sequence b1, b2, ..., bm (1 ≤ bj ≤ 100), where bj is the j-th girl's dancing skill.

Output
Print a single number — the required maximum possible number of pairs.

Examples
inputCopy
4
1 4 6 2
5
5 1 5 7 9
outputCopy
3
inputCopy
4
1 2 3 4
4
10 11 12 13
outputCopy
0
inputCopy
5
1 1 1 1 1
3
1 2 3
outputCopy
2

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[a135c550ec...](https://github.com/treckstar/yolo-octo-hipster/commit/a135c550ec70dd8b1f0b12933e6b38430257f9ce)
#### Saturday 2022-03-26 06:00:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [kumaranand7/tribute](https://github.com/kumaranand7/tribute)@[3f0df51ac0...](https://github.com/kumaranand7/tribute/commit/3f0df51ac0e62088ac05d76f57ed025491293a48)
#### Saturday 2022-03-26 06:03:10 by Anand Kumar Gupta

Update README.md

This is the tribute page for our Missile Man of The India - Dr. A.P.J. Abdul Kalam . He was also known as People's President.
This shows the journey of Small boy to the President of the India and also one of the most loved man in India. We should follow his steps to become successful in life and do something for our nation.
There are many quotes given by Sir Kalam that are life-changing. I like to mention one of them :-
"It Is Very Easy To Defeat Someone, But It Is Very Hard To Win Someone"

---
## [Nagorogan/AkarisSubnauticaMods](https://github.com/Nagorogan/AkarisSubnauticaMods)@[e2f62d3dc5...](https://github.com/Nagorogan/AkarisSubnauticaMods/commit/e2f62d3dc50690bed9aeaee034bb7bd84fee2e45)
#### Saturday 2022-03-26 07:32:17 by Nagorogan

damaging laser, and primitive item picking up

made laser actually damage shit it hit

added primitive version of item collection in drone

added a metric fuckton of comments

majority are a guide to improving/finishing the item collection

probably made at least one joke in the comments, can't be expected to remember them all no matter how funny they may be

---
## [beartype/beartype](https://github.com/beartype/beartype)@[47c9fdceff...](https://github.com/beartype/beartype/commit/47c9fdceff75f2bd90162107f7a45950f1fd36cf)
#### Saturday 2022-03-26 07:50:04 by leycec

Sphinx documentation x 3.

This commit is the next in a titanic commit chain refactoring our
documentation from its current monolithic home in our top-level
`README.rst` file to its eventual modular home at [ReadTheDocs
(RTD)](https://beartype.readthedocs.io), en-route to resolving issue #8
(!) kindly submitted a literal lifetime ago by visionary computer vision
export and long-standing phenomenal Finn @felix-hilden (Felix Hildén).
Specifically, I squandered the entire evening attempting to coerce
Sphinx's `autodoc` extension into resolving cross references to
anything. I failed utterly. `autodoc` refuses to resolve cross
references to even **standard pure-Python CPython modules that are both
guaranteed to exist and be trivially importable.** In short, `autodoc`
is Hell Incarnate. I am on the precipice of abandoning all hope of
`autodoc` ever behaving as expected. In a desperate eleventh-hour
attempt to reinstate sanity, I've posted a StackOverflow question on the
topic at:

    https://stackoverflow.com/questions/71626179/sphinx-autodoc-extension-unable-to-even-find-standard-modules-guaranteed-to-ex

Since I've wasted far too many scarce unpaid volunteer evenings on
wrestling with this insanity and now harbour profound doubts that anyone
will even be able to provide relevant advice, it's likely that @beartype
will be abandoning `autodoc` entirely. Instead, I'll just document our
public API manually. That's the opposite of ideal -- but I'll take
working of a non-working ideal. Thanks for wasting weeks, `autodoc`.
(*Syrupy uructations of fructose!*)

---
## [N00byKing/VVVVVV](https://github.com/N00byKing/VVVVVV)@[e93d8989d3...](https://github.com/N00byKing/VVVVVV/commit/e93d8989d3e82e5afc52e09fd7aeae3d41644e64)
#### Saturday 2022-03-26 11:17:52 by Misa

Revert "Fix Secret Lab Time Trial trophies having wrong colors"

As reported by Dav999, Victoria and Vermilion's trophy colors are
swapped again in 2.4. He points to
37b7615b71c3a2f44e03c47894383107850812ff, the commit where I fixed the
color masks of every single surface to always be RGB or RGBA.

It sounded plausible to me, because it did have to do with colors, after
all. However, it didn't make sense to me, because I was like, I didn't
touch the trophy colors at all after I originally fixed them.

After I ruled out the RGBf() function as a confounder, I decided to see
whether intentionally reversing the color order in RGBf() to be BGR
would do anything, and to my surprise it actually swapped the colors
back around and it didn't actually look bad.

And then I realized: Swapping the trophy colors between RGB and BGR
ordering results in similar colors that still look good, but are simply
wrong, but not so wrong that they take on a color that no crewmate uses,
so it'd appear as if the crewmates were swapped, when in reality the
only thing that was swapped was actually the color order of the colors.

Trying to fix this by swapping the colors again, I actively confused
colors 33 and 35 (Vermilion and Victoria) with colors 32 and 34
(Vitellary and Viridian), so I was confused when Vermilion and Victoria
weren't swapping. Then as a debugging step, I only changed 34 to 32
without swapping 32 as well, and then finally noticed that I was
swapping Vitellary and Viridian, because there were now two Vitellarys.
And then I was reminded that Vitellary and Viridian were also wrongly
swapped since 2.0 as well.

And so then I finally realized: The original comments accompanying the
colors were correct after all. The only problem was that they were fed
into a function, RGBf(), that read the colors backwards, because the
codebase habitually changed the color order on a whim and it was really
hard to reason out which color order should be used at a given time, so
it ended up reading RGB colors as BGR, while it looked like it was
passing them through as-is.

So what happened was that in the first place, RGBf() was swapping RGB to
BGR. Then I came and swapped Vermilion and Victoria, and Vitellary and
Viridian around. Then later I fixed all the color masks, so RGBf()
stopped swapping RGB and BGR around. But then this ended up swapping the
colors of Vermilion and Victoria, and Vitellary and Viridian once again!

Therefore, swapping Vermilion and Victoria, and Vitellary and Viridian
was incorrect. Or at least, not the fix to the root cause. The root
cause would be to swap the colors in RGBf(), but this would be sort of
confusing to reason about - at least if I didn't bother to just type the
RGB values into an image editor. But that doesn't fix the real issue,
which is that the game kept swapping RGB and BGR around in every corner
of the codebase.

I further confirmed that there was no more RGB or BGR swapping by
deleting the plus-one-divide-by-three transformation in RGBf() and
seeing if the colors looked okay. Now with the colors being brighter, I
could see that passing it straight through looked fine, but
intentionally reversing it to be BGR resulted in colors that at a
distance looked okay, but were either washed out or too bright. At least
finally I could use my 8 years of playing this game for something.

So in conclusion, actually, 37b7615b71c3a2f44e03c47894383107850812ff
("Fix surface color masks") was the real fix, and
d271907f8c5d84308a3cf9323ac692199b8685a6 ("Fix Secret Lab Time Trial
trophies having wrong colors") was the real regression. It's just that
the regression came first, but it wasn't really a regression until I did
the other fix, so the fix isn't the regression, the regression is...
this is hurting my brain. Or the real regression was the friends we made
along the way, or something like that.

This is the most trivial bug ever caused by the technical debt of those
god-awful reversed color masks.

---

This reverts commit d271907f8c5d84308a3cf9323ac692199b8685a6.

Fixes #862.

---
## [Reinazhard/android_kernel_xiaomi_whyred](https://github.com/Reinazhard/android_kernel_xiaomi_whyred)@[5fe7f0ba64...](https://github.com/Reinazhard/android_kernel_xiaomi_whyred/commit/5fe7f0ba6475d8f37bdcc69d8120dea1adcb108e)
#### Saturday 2022-03-26 11:22:46 by Reinazhard

fuck you

Signed-off-by: Reinazhard <reinazhard@gmail.com>

---
## [Inolongo/BestGameEver](https://github.com/Inolongo/BestGameEver)@[f7e7e6d682...](https://github.com/Inolongo/BestGameEver/commit/f7e7e6d682e07c4ca3faceb7caea9a5df760e066)
#### Saturday 2022-03-26 11:44:06 by Inolongo

Fix enemy setting and fuck all this project it sucks i'm done with this shit

---
## [Jolly-66/Skyrat-tg](https://github.com/Jolly-66/Skyrat-tg)@[d96e7b7e27...](https://github.com/Jolly-66/Skyrat-tg/commit/d96e7b7e278dd0226a4de8d9463edda37af709f9)
#### Saturday 2022-03-26 11:51:41 by SkyratBot

[MIRROR] Makes Ants glow, puts a min on ant screaming & shoe permeability, & other ant-related things. [MDB IGNORE] (#11821)

* Makes Ants glow, puts a minimum on ant screaming and shoe permeability, and other ant-related things. (#64786)

I found out how emissives work and my first thought was "damn ants should glow that would look sick"
So now they do.

Also, having less than 5u ants in your body will make you not scream, so 0.0001u ants will no longer have that tiny chance of making someone scream for their life.

If an ant pile has a max damage value less than 1, then they won't be able to bite through your shoes. This is the same threshold as the second tier ant icon.

Makes the giant ant a hostile mob with the neutral faction, meaning they will attack anything not in the neutral faction.

* Makes Ants glow, puts a min on ant screaming & shoe permeability, & other ant-related things.

Co-authored-by: Wallem <66052067+Wallemations@users.noreply.github.com>

---
## [Tokman5/pcsx2](https://github.com/Tokman5/pcsx2)@[d6684efd26...](https://github.com/Tokman5/pcsx2/commit/d6684efd262ef1c83d37c50b48edc478952dddf9)
#### Saturday 2022-03-26 12:22:24 by RedDevilus

GameDB: GS HW Batch X

Relevant:
Bully
Colosseum - Road to Freedom
Dark Chronicle (Dark Cloud 2)
Killzone
God of War
Gun
Midnight Club 3
Mortal Kombat - Deadly Alliance
Need for Speed Carbon / Most Wanted / Undercover
Prince of Persia - Sand of Time / The Two Thrones / Warrior Within
Resident Evil 4 (BioHazard 4)
Thrillville / Off the Rails

---
## [atorik/postgres](https://github.com/atorik/postgres)@[ec62cb0aac...](https://github.com/atorik/postgres/commit/ec62cb0aac5ba31a82339606009ddbd7eb00e2ac)
#### Saturday 2022-03-26 13:06:08 by Tom Lane

Revert applying column aliases to the output of whole-row Vars.

In commit bf7ca1587, I had the bright idea that we could make the
result of a whole-row Var (that is, foo.*) track any column aliases
that had been applied to the FROM entry the Var refers to.  However,
that's not terribly logically consistent, because now the output of
the Var is no longer of the named composite type that the Var claims
to emit.  bf7ca1587 tried to handle that by changing the output
tuple values to be labeled with a blessed RECORD type, but that's
really pretty disastrous: we can wind up storing such tuples onto
disk, whereupon they're not readable by other sessions.

The only practical fix I can see is to give up on what bf7ca1587
tried to do, and say that the column names of tuples produced by
a whole-row Var are always those of the underlying named composite
type, query aliases or no.  While this introduces some inconsistencies,
it removes others, so it's not that awful in the abstract.  What *is*
kind of awful is to make such a behavioral change in a back-patched
bug fix.  But corrupt data is worse, so back-patched it will be.

(A workaround available to anyone who's unhappy about this is to
introduce an extra level of sub-SELECT, so that the whole-row Var is
referring to the sub-SELECT's output and not to a named table type.
Then the Var is of type RECORD to begin with and there's no issue.)

Per report from Miles Delahunty.  The faulty commit dates to 9.5,
so back-patch to all supported branches.

Discussion: https://postgr.es/m/2950001.1638729947@sss.pgh.pa.us

---
## [TsogtOnCrack/nestBodlog](https://github.com/TsogtOnCrack/nestBodlog)@[5033925f04...](https://github.com/TsogtOnCrack/nestBodlog/commit/5033925f04f4331087eb4f72933d682863961309)
#### Saturday 2022-03-26 13:14:56 by TsogtOnCrack

well, no succes today. I wana kill myself. I guess i need help from my teacher. damn i am a faliur, how am i supposed to become a programer, when i cant even make something as simple as this. FUCK THIS!! FUCK CODING @@@!!!!!!! AAAHHHHHH!!!

---
## [EdgeLordExe/Merchant-Station-13](https://github.com/EdgeLordExe/Merchant-Station-13)@[663688130e...](https://github.com/EdgeLordExe/Merchant-Station-13/commit/663688130e83b094351f8cdf1b1d20a6b0c80c4b)
#### Saturday 2022-03-26 13:20:08 by karmaisblackandbluepilled

I hate /tg/code so much it's actually unreal (#57)

* Hulk Recoil Removal go fuck yourself 41 damage for one wall

* medical doctors have access to genetics, again, why was this removed FUCK you

* buffs bpowder and methsplosions back up, fuck you edge

* Unnerfs chemicals for speed why why why why why

* adds silver back to synthesizers but removes the solidification reaction, for obvious reasons

* unfucks the dna sequencers because genetics is a shit minigame and making it harder to solve is for [SLUR REMOVED]

* did what the guy above told me to(?)

---
## [vincentiusvin/tgstation](https://github.com/vincentiusvin/tgstation)@[759d24ab14...](https://github.com/vincentiusvin/tgstation/commit/759d24ab14af0ab22ae9642e9190c3db91e16516)
#### Saturday 2022-03-26 13:43:35 by san7890

Four Corners, Red Rover: An Exploration in Decal Trends [MDB IGNORE] (#65290)

* Four Corners, Red Rover: An Exploration in Decaled Trends

You there! What exactly is wrong with this photograph?!

You don't need to tell me, I've boxed it out. There's four individual corners for the decalling. This is weird. You may be asking: Why don't they use the "full tile" turf decals? Let me demonstrate.

Look at the difference between the one at left and the one in the middle. The turf decal totally smothers the nice contrast lines afforded to use by the base turf, causing it to have smooth, clammy exterior. This is probably why no mapper ever uses the full turf decal, much to the chagrin of people who stare at how big the size of this repo is.

Now, what's that on the right? Why, it's the new sprite (and pathing I made) to help counter-act this issue! This perfectly lines up with the contrast lines of the base turf, allowing us to have a non-flattened visualization, while not having four fucking turf decals a turf load upon initialization. How epic!

I've also added "contrasted" variants of the "half" and "anticorner" turf decals for future use. I probably won't go through and update this in this PR, but the opportunity remains available.

I may or not map this change across all the maps. We shall see.

* neutral corners

we love vsc

* no wait

i forgot a bunch of potential edgecases so we'll have to go back. yellow should be fine but neutral, dark, blue, and green should get a second look over

* recheck

found some stuff, probably missed out on others. let us commence forth

* MISTAKE

nearly a fucko bwoingo

* final pass

it compiles and i've had enough, someone else can probably figure it out from this point onwards

* #65230 goated my timbs

now we wait for linters to fail

* YOU DIDN'T SAY THAT THE FIRST TIME

LINTERS AAFAFAFF

---
## [pariahstation/Pariah-Station](https://github.com/pariahstation/Pariah-Station)@[770ef81a1f...](https://github.com/pariahstation/Pariah-Station/commit/770ef81a1fb271572d711e7a05dbce62564ca3b0)
#### Saturday 2022-03-26 14:09:43 by John Willard

makes podpeople call parent (#65362)


About The Pull Request

kinda fucked up that it doesnt.
Also while checking this PR I noticed other species also don't, kinda screwed up world we live in...
Why It's Good For The Game

Parent's spec_life is what checks if you have nobreath, and in which case it will remove all your oxygen damage and, if in crit, give you brute damage instead. Not having this makes you basically not take damage while in crit, which I think shouldn't be the case.
Changelog

cl
fix: Podpeople now take self-respiration into account when taking damage from critical condition, like most other species.
/cl

---
## [ronak197/Spider3DFlux](https://github.com/ronak197/Spider3DFlux)@[edc38c9dc9...](https://github.com/ronak197/Spider3DFlux/commit/edc38c9dc946eafba2b73501cb7e56e3b4966777)
#### Saturday 2022-03-26 14:18:50 by Idan054

V37.04.0 - fix variations bugs - action file [GPlay & IOS Release - LIVE]
+ Share button on product page
[X] Fixed variation error 'DIZA'
[X] Fixed variation error '3DPEN'
[X] Switch back Cache on https & env

V37.03.0 - fix variations bugs - action file
- Action file is product_variant_mixin.dart - return productVariation;
[ ] Fixed variation error 'DIZA'
[ ] Fixed variation error '3DPEN'
[ ] Switch back Cache on https & env
* Check if the bug exist in lasted official version

V37.02.0 - ix variations bugs - Prints update to f
+ Bug type found

V37.01.0 - Fixed dynamic_link_service.dart
+ Fixed sendErrorMail() doesnt work (Yah lol), This fix will wotk till 30.05.22:
   אם מייל זה לא נשלח לך יותר:
   Google - החל מ-30 במאי 2022 ההגדרה הזו לא תהיה זמינה יותר - https://prnt.sc/B9wB3V-MCWdi
   https://prnt.sc/KIzQksl6210z

+ Now the share button creates shorter link that 100% work Product id Based!
Example: https://spider3dflux.page.link?amv=1&apn=com.biton.spider3dflux&ibi=com.biton.spider3dflux&imv=1.0.1&isi=1469772800&link=https://www.spider3d.co.il/?p=33897
[ ] Fixed variation error 'DIZA'
[ ] Fixed variation error '3DPEN'
[ ] Switch back Cache on https & env
* Check if the bug exist in lasted official version

V36.00.0 - Check4update I [GPlay & IOS Release - LIVE]

V35.00.0 - Fix API Bug & Update key [GPlay & IOS Release]
+ consumerKey & consumerSecret Replaced (security update)
+ var "myApiAuth" Basic auth (consumerKey & consumerSecret based) who added and Needed because "miniOrange API Authentication" Wordpress plugin.
* "myApiAuth" Basic auth generated from PostMan

V34.00.0 - Fix Urgent no pay bug. [GPlay & IOS Release]

V33.00.0 - Fix Pay but no Woo order. [GPlay & IOS Release]
+ Fixed Payment without Woo order bug! Based index.dart : lines;
278 - createOrder(), 'pending' status, // AKA ממתין לתשלום
291 - PaymentWebview() // AKA iCredit
305 - updateOrder(), 'processing' status
320 - SuccessScreen() // With order.id

V32.00.0 - 1000ILS+ Payments & Skip web success. [GPlay & IOS Release]
+ A better loading button (Fix)
+ succeedRedirect() Work (once &) ASAP instead onPageFinished:. Based payment_webview_screen.dart
+ The iCredit Web Checkout button is not auto click in 1000ILS + orders. Based click_checkoutButton bool in payment_webview_screen.dart : Line 213

V31.00.0 - COD Cash on delivery removed! [GPlay & IOS Release]
+ Shake removed
+ COD Removed, CC only.

V30.00.0 - Report with shake [GPlay & IOS Release] [Beta]

V30.00.0 - Report with shake [GPlay & IOS Release] [Beta]

V29.00.0 - Loading & Slash bug fix
+ Fix multiple slash on expiry field at payment_formV3.dart : line 149
+ Fix loading not shows on checkout based String myBillingStatus on cart_mixin.dart (Famous cartModel)

V28.02.0 - Checkout Bug fix [GPlay & IOS Release]
+ version updates only.

V28.01.0 - Bug fixes - Ux popups
[X] Ux update, when needed form (delivery or payment) empty and Green checkout button clicked - auto open needed popup.

+ When delivery method picked, if not local-pickup - auto set payment option to credit card

V28.00.0 - Bug fixes
+ Default Credit card removed (make bugs)
+ "Buyer name not exist" oc iCredit web checkout should fix.
+ Name added in "כתובת משלוח עבור" title
+ performance improvements and bug fixes (: LOL
[ ] Ux update, when needed form (delivery or payment) empty and Green checkout button clicked - auto open needed popup.

V27.01.0 - Require login - my_cart_screen.dart [IOS Release]
+ Cart button (קופה) Make sure user logged, and require login if needed. Made ios devices (who can skip login). Based my_cart_screen.dart : line 120

V27.00.0 - The Checkout V3 Makeover [GPlay Release] [IOS Release?]
+ Releasing the New checkout_screenV3.dart

app/build.gradle Changes:
+ flutterVersionCode : line 31
+ flutterVersionName : line 36

 project.pbxproj (ios) Changes:
 + MARKETING_VERSION : lines 491, 655, 704
 + CURRENT_PROJECT_VERSION : line 473

V26.01.0 - index.dart - CreditCard payment fix
+ A Great working redirect to success order page & order creates on woo
[X] The Notes button should work.
[X] Cash should appear on Local pickup only
[X] Fix embed data on the web iCredit (NEW)
[X] Status pre paid on local pickup
[ ] Make sure invoice works
[X] Make sure 1 coupon per user (ATTENTION: user can still "Hack" by create new user)

V25.00.0 -  handleCheckoutButtonV3.dart - change Status [BETA!]
[X] The Notes button should work.
[X] Cash should appear on Local pickup only
[ ] Fix embed data on the web iCredit
[X] Status pre paid on local pickup
[ ] Make sure invoice works
[X] Make sure 1 coupon per user (ATTENTION: user can still "Hack" by create new user)

V24.00.1 - handleNotesDialogV3.dart - [Commit notes update]
+ A great popup appear once click the notes button
+ The note value preview shows on the buildAddNoteButton()
+ the value saved based the global noteController on handleCheckoutButtonV3.dart (line 208)

[X] The Notes button should work.
[X] Cash should appear on Local pickup only
[ ] Fix embed data on the web iCredit
[ ] Status pre paid on local pickup
[ ] Make sure invoice works
[ ] Make sure coupon us used when so..

V23.00.0 - RadioButtonV3.dart - Cash only on local pickup
+ Cash is appear on Local pickup only
+ Checkout button make sure it.
* Check Default Changelist for full details
[ ] The Notes button should work.
[X] Cash should appear on Local pickup only
[ ] Fix embed data on the web iCredit

V22.00.0 - checkout_screenV3.dart - buildAddNoteButton()
+ A great Notes button add
+ Redesign edits.
[ ] The Notes button should work.
[ ] Cash should appear on Local pickup only
[ ] Fix embed data on the web iCredit

V21.02.0 - handleCheckoutButtonV3.dart - Loading on checkout_buttonV3.dart
+ A great loading on checkout button text Based "cartModel.user?.billing?.status" (state -> status) : line 52
& handleCheckoutButtonV3.dart : line 187, 214

V21.01.0 - handleCheckoutButtonV3.dart - Function in function test.
+ A great test of usage of 2 way move values between Functions, But Provider just way more easier..

V21.00.0 - handleCheckoutButtonV3.dart - Working success page
+ The app createOrder() in woo & great SuccessScreen shows
x - Still need to fix the actual iCredit payment.

V20.00.0 - Search page - Add to cart.
+ A great Quick add to cart on search based vertical_simple_list.dart (The search listView), dialog_add_to_cart.dart and others..
+ Minor order history page improve
+ Minor product page improve

V19.05.0 - handleCheckoutButtonV3.dart - Reset default shipping.
+ reset the selected shippingMethod on provider Based handleCheckoutButtonV3.dart : line 184

V19.04.0 - handleCheckoutButtonV3.dart - Save default payment.
+ Set Default to iCredit and remember if its changes to cash Based cart_model_woo.dart : line 176

V19.03.0 - handleCheckoutButtonV3.dart - CreateOrder [Beta]
+ Still not ready, but a better handleCheckoutButton()
+ Great performance improvements and bug fixes (: LOL

V19.02.0 - handleCheckoutButtonV3.dart - CreateOrder [Beta]
- A working only create order on WooCommerce, Not place order.

V19.01.0 - handleCheckoutButtonV3.dart - CreditCard default
+ Sets iCredit the default payment method on CartModel
CREDIT CARD default sets on cart_model_woo.dart - paymentMethod = PaymentMethod(...

V19.00.0 - handleCheckoutButtonV3.dart
+ A Great full & clean checkers before checkout + SnackBar

V18.00.0 - checkout_screenV3.dart - checkout_buttonV3.dart & dynamic prices
+ Prices on checkout_screenV3 is now dynamic (Based CartModel)
+ checkout_buttonV3.dart print values for future tests

V17.01.0 - payment_formV3.dart - Titles for the popups
+ Title added on handleDeliveryFormV3.dart

V17.00.0 - payment_formV3.dart
+ A great working payment form popup that save the details in CardModel provider

V16.03.0 - checkout_screenV3.dart - user details
+ Also Set and get User details like email & username I
+ performance improvements and bug fixes (: LOL

V16.02.0 - delivery_formV3.dart - Update button
+ Dynamic titles on checkout_screenV3.dart Instant work by added notifyListeners();

V16.01.0 - delivery_formV3.dart - Update button
+ Delivery popup update button works great and save to local.
+ Dynamic titles on checkout_screenV3.dart
# I'm God damn good.

V16.00.0 - delivery_formV3.dart - AutoComplete
+ Auto complete when edit based official CartModel (Provider)

V15.03.0 - checkout_screenV3.dart - Static
+ Just a very organize and clean delivery_formV3.dart file

V15.02.0 - checkout_screenV3.dart - Static
+ Connect delivery_screenV3.dart to cards

V15.01.0 - checkout_screenV3.dart - Static
+ checkout_screenV3 added to route_list.dart so now its called when click the Cart button
+ A list of todos in checkout_screenV3.dart
+ performance improvements and bug fixes (: LOL

V15.00.0 - checkout_screenV3.dart - Static
+ After tons of bugs on the checkout screen, its time for makeover!

V14.00.2 - Icredit Fix III
+ Ios CURRENT_PROJECT_VERSION Update (9) on project.pbxproj

V14.0.1 - Icredit Fix II
+ Icredit Fix II

V14.0.0 - Product in cart update (review_screen.dart)
+ ...getProducts() Replaced by ...createShoppingCartRows() : Line 257
So now user can change quantity & remove items from checkout page.

V13.11.0 - LoginScreen:Cart Bug Fix
+ Change the checking method if user to method based live data. (Needed for apple cuz guest mode availble but not in cart)

V13.10.1 - Coupons loading
+ loading added while searching coupon -
Based isFetching Bool

V13.10.0 - Coupons fix + summarize
+ Coupon bug fixed
- ICredit bug fixed (Token Replaced)

V13.9.10 - Login if guest & GreenButton...
+ Green Button is now not float and always show to fix bugs.
+ The Login screen shows if ur guest

V13.9.8 - Improved onboard_screen.dart
+ To fix IOS Release denied, a "Skip login" button has been added (To both OS)

V13.9.7 - [Fix] Checkout button double tap
+ Green Checkout button fixed
+ Fix Checkout button double tap by set Floating cart (bottom left on product page) - product_bottom_sheet.dart - line 278

V13.9.5 - [Fix thingi_screen.dart + Reads Reduce]
+ _check_thingiToken() ( & set_thingiToken() if needed) on every api call
+ Reduce the reads from about 450, can be reduced to ~5 (Limit is 50K)
+ Cleaner II version of set_thingiToken()

---
## [4eck-qed/Pong](https://github.com/4eck-qed/Pong)@[9b16af65fb...](https://github.com/4eck-qed/Pong/commit/9b16af65fbc2d853d2a7bd2d36c938b9ce42a194)
#### Saturday 2022-03-26 15:06:56 by Ryyo

Revert "Fuck youuuuuuuuuuuuuuuuuuuuuu"

This reverts commit 9b7753f7ce05fe2fa7a8e2d874c78c0507fa2063.

---
## [team-eoanb/EoaNB](https://github.com/team-eoanb/EoaNB)@[08b4ec5f1f...](https://github.com/team-eoanb/EoaNB/commit/08b4ec5f1fb8e7e3d72bcb597bf4728a7e366e84)
#### Saturday 2022-03-26 15:31:13 by Kenhel

Serbia updated

Fixed 2 things with the focus tree,

and for some stupid bloody reasons I can't have advisors that needs focus to become available with these code in the character files

available = {
    has_completed_focus = SER
}

so thanks a lot paradox, I had to add some other additional crap in the focus stuff it was painful moving the code, and also I can't seem to figure out how to get characters to retire after a certain date and now when I'm literally typing this was I told by Christ the code I ripped off from uk as reference was not working so welp time to rip code from prussia instead but I'll do that tmr and since I checked the error logs and there seems to be no errors I'm just gonna push this crap ok thanks

---
## [Starloader-project/Starloader-API](https://github.com/Starloader-project/Starloader-API)@[a05ba96fb9...](https://github.com/Starloader-project/Starloader-API/commit/a05ba96fb9e329c5b73cca36d93cf7872c4203b1)
#### Saturday 2022-03-26 17:31:53 by Geolykt

Move to our fork of brachyura (slbrachyura) and Starplane.

The second (or third?) generation of galimulator build tools is out.

It remains to be seen whether it will be the last generation or
whether there is a successor to it. It also remains to be seen
on how much of a good idea forking brachyura was. It is certainly
less reliable but at least have some easily extendable API and forking
it was certainly a better idea than staying with upstream.
Upstream will also probably not recieve our improvements as
they are pretty radical in many areas.

However automatic mapping of deobfuscated names will probably be the
core process of our build supply chain. Even if in the end manual
mapping may be the be-all and end-all. But given the current size
of the galimulator modding community (1 person as of right now) it
is probably just a waste of man hours for now. In the future it might
be more attractive as I might do my "Besondere Lernleistung" on
automatic updating of deobfuscation mappings however such a project
will take a lot of time. As such I might think that selling the
Starloader-project as the "Besondere Lernleistung" might be more viable,
especially because I have now worked over a year on it and at the time that
I will have to hand over the "Besondere Lernleistung" I would have
commited around 3 years and probably over 4 000 hours to the entirety
of the project. Numbers which are unthinkable for my peers. But that is
what you can do if you have no social life.

---
## [avar/git](https://github.com/avar/git)@[cd1a286aed...](https://github.com/avar/git/commit/cd1a286aed83bf7401b2bc4e96a86c2b15fe9005)
#### Saturday 2022-03-26 17:45:13 by Ævar Arnfjörð Bjarmason

object-file.c: do fsync() and close() before post-write die()

Change write_loose_object() to do an fsync() and close() before the
oideq() sanity check at the end. This change re-joins code that was
split up by the die() sanity check added in 748af44c63e (sha1_file: be
paranoid when creating loose objects, 2010-02-21).

I don't think that this change matters in itself, if we called die()
it was possible that our data wouldn't fully make it to disk, but in
any case we were writing data that we'd consider corrupted. It's
possible that a subsequent "git fsck" will be less confused now.

The real reason to make this change is that in a subsequent commit
we'll split this code in write_loose_object() into a utility function,
all its callers will want the preceding sanity checks, but not the
"oideq" check. By moving the close_loose_object() earlier it'll be
easier to reason about the introduction of the utility function.

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [GNOME/gimp](https://github.com/GNOME/gimp)@[7123b6c466...](https://github.com/GNOME/gimp/commit/7123b6c466dcf38bb274734e9d7494c9c4fd8b8e)
#### Saturday 2022-03-26 18:08:13 by Jehan

Issue #7685: g-ir-doc-tool produces broken XML.

To work around the issue, I just wrote a stupid sed script. Of course,
it means that if we encounter again the issue on some other docs, we'll
have to update it. In other words, it's neither robust nor a proper
long-term fix. Just a temporary hack.
See: https://gitlab.gnome.org/GNOME/gobject-introspection/-/issues/425

Also fixing this issue, I encountered another bug, this time in meson,
which changes backslashes in slashes on 'command' arguments, in a
completely uninvited manner! The only workaround to this is apparently
to call an external script, which is ridiculous for such a basic stuff.
But well… here is why I implement this with a script, instead of
directly calling sed in the meson 'command'.
See: https://github.com/mesonbuild/meson/issues/1564

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[8ae9a9c5ed...](https://github.com/mrakgr/The-Spiral-Language/commit/8ae9a9c5edc509a1366cccc6632045c1ead32eab)
#### Saturday 2022-03-26 18:57:06 by Marko Grdinić

"11:10am. I could have gotten out of bed 3h ago, but I felt like sleeping in. Right now I am not even lazing about, but sharpening my will. None of what is ahead of me is difficult.

I just need to determine the reason why I am doing it.

Yeah, to summarize my rant from yesterday. Art is not x/5 like most skills, but x/6. With the right programs you can get 6 whole ranks.

No matter how I look at it, it is not justifiable to switch domains like this when programming could be so much more profitable for me. Saying I do not want to get a job is not reason enough to switch to art when building up those skills would be so much harder that just getting a job.

But accumulating wealth makes no sense. For all I know humanity might not even exist in 20 years, and if it does it might be in some virtual world. I could end up falling into the trap of accumulating useless resources when I should be pursuing actual superpowers. Skills in the >5 range would qualify as that.

It is really a pity this is not the 20th century anymore, so that one can just patiently accumulate wealth like Warren Buffet.

Yeah, back at the end of high school I did not want to become a programmer exactly because of this - programming is weak. Even with 5 ranks in it, I can't do crap other than get a job. But given the nature of my goals, I had no real choice but to build them up. I can only hope that Spiral will be something I'll be able to make use of in the future. The langauge itself is firmly grafted in my mind ready to be unleashed at the right time.

11:35am. 6/6 would be pretty grand. It would be akin to having a spear while all the other monkeys don't even know how to use a club.

Why wouldn't I drop programming? Suppose I worked at Google, I could make >100k a year, but is working at Google that exceptional when another 10k people also work there?

If it is merely getting a highly paid job as a programmer, I could have just skipped high school and worked on 'refining' my resume. I doubt that having Spiral there means a thing. I could have just made some fake projects to slap them there if that is a concern. As a group, programmers have a heart attack every time it is time to learn something new. Why would I want to want to be one of them?

11:40am. I do not want to go through any of these humiliations anymore. I've cut my connections to the sordid past. I've accepted that I made a mistake not scramming to do my own thing at the age of 14 and instead I had to force myself to endure 4 extra years of boredom and humiliation.

I've been so unfailingly honest to my desires, and where I regret that is only towards having obligations and expectations of others.

Since I have no need for morality, I should give the primordial magics a real try. Since the old days, priests have always dabbed on the warriors.

I certainly have what it takes to compete with people like ONE in terms of writing. I can't say I am not envious that a person like him can just spread wageslave morality and get all the benefits that he did.

11:50am. I'll just do the opposite. I'll show the world exactly what the demonic path is about.

It is just about the time for it to rise.

11:55am. The way evolution works is a mystery, but I am guessing the particular path becomes dominant at key turning points for a species.

I should be greedy, more than anyone. 6/6 would be beyond the pinnacle for a human.

12:30pm. Let me step away from the screen again. I do not feel like doing anything right now, not even consume fiction.

Let me have breakfast first.

6/6 is the only thing worth chasing in this world. I am the only one who can do it. A regular artist would not have the programming skills for it.

I need to believe that if I keep up the pursuit that I'll find a way to make programming worth with it.

1:25pm. Done with breakfast and chores. Let me chill a bit and then I will step away from the screen to charge up my motivation. After it is time to start I'll really start and go forward without hesitation.

6:45pm. Done with lunch. I feel a bit more motivated now.

The reason I became a good programmer is because I had a problem in front of me and the desire to solve it. That desire manifested as a plan. I should put all ego behind me and start from scratch.

Art isn't any different from programming - it is about problem solving. You have a scene in mind, and you have to simplify into strokes, or simple 3d objects. That is the whole of it. You peel at the problem until it is resolved.

This is a core skill in any domain.

6:50pm. If I had been born in 1950 just what would my profession be? I probably would not have access to computers. In that case, wouldn't I aim to have my voice heard. And having it heard has power.

Consider Google the company - it sells nothing, but still manages to convert eyeballs into billions of dollars in earnings. How many people are rich because other people listen to them?

Even if I fail, if I give the utmost effort I doubt I'll do worse than the yearly salary in Croatia. And just that would be enough to get me those chips.

I have this desire not to be stuck doing random things for other people. I wouldn't mind working for others if our interests intersect, but that is the extent of it.

Also applying to jobs is humiliating. It is not so much the rejection that bothers me. It is the feeling of being some kind of bug.

6:55pm. Consider those demonic sects in xianxia where the strong rule.

If I was competing in a spot for such a place and somebody stronger than me got it instead, that is one thing. But participating in a competition where the rejects are random, where you get judged by some college girl who never wrote a line of code in her life, and where nepotism rules - is not something I desire.

I should consider views as part of my assets and focus on building those up. Later on I'll manage to convert them into cash.

7:10pm. I have to move away from the now. Programming was a means to an end - pursing the Singularity. If I wanted a job, I did not need all this training in functional programming. I could have bullshitted my way into some company and learned on the job. Being rank 3 or 5 does not matter here. Sure, at my earlier level when I was starting in 2015, I might not have been good enough to work on compilers and such, but I was certainly good enough to hack things up. I'd have gotten a shock when it was time to do programming in the large, but I'd overcome it.

Right now, there are things more important than money. I need to learn how to use my voice to impose my will on the world.

Previously I saw it as beneath me, a real man would just plow on and win with his own power, but NP Hardness is no joke. I do not want to try to tackle algorithmic inference using my gray cells anymore. It beat me in high school and it beat me last year. I do not want to spent my life making dumb experiments, wasting my time and burning away money. I want the path to provide for me properly.

I guess, I want to move from playing single player to playing multi player. It has long been time to make that transition.

7:15pm. Yeah, it is difficult, but life spent in silence is not worth living. If I am destined to win I'll win, and if not, I might as well make an uproar and leave a mark on the world.

7:30pm. It is tough. I could make guaranteed money, or steadfast the current route and spend years building up my skills. But on the other hand, just what are a few years? Nothing.

If it took me 5 years to get to rank 5, that would be nothing. It is not my own life that is in danger. It is just my impatience that is urging me.

7:35pm. Rank 6 is the goal. If I can get to rank 6 in the arts, that would be the ideal place from which to pursue the Singularity. Rank 5 in programming combined with 6 in arts should be the kind of weapon that I need.

I need to craete a connection with the machines and even if I know that I should be building the external cortex, the way I approach it - art partner vs some thing grinding away at toy games will lead to a huge difference in the end result. It is a given that ML researchers will opt for later. In that case, it should be my responsibility to take the former route. I should aim to become the only person in the world with both world class art and programming skills.

It is a chess game I'll play with my life on the line.

7:40pm. This happens to me a lot in programming. After a significant amount of time spent working I lose sight of my goals and become overwhelmed with tedium. Instead of seeing the steps that I need to take, my eyes only start seeing the huge mountain and the arduous trek towards the peak. I need to remind myself that there is no other way, but up.

To live is to develop one's own skills.

Tomorrow, I will remind myself that I seeking the sixth rank. And then I will focus on the small steps in front of me. I will finish that desk to my satisfaction and move on to the next prop. I will not hurry. It does not matter if the room takes me a week or two. What is important is that I keep pushing forward."

---
## [Unicote/kernel_xiaomi_surya](https://github.com/Unicote/kernel_xiaomi_surya)@[d51e5fee68...](https://github.com/Unicote/kernel_xiaomi_surya/commit/d51e5fee689333713a2bd87c1ab14c2fbe760e7a)
#### Saturday 2022-03-26 19:00:31 by Peter Zijlstra

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
## [ozzono/scripts](https://github.com/ozzono/scripts)@[e342ac5dac...](https://github.com/ozzono/scripts/commit/e342ac5dac179b378b6cd8e59d962ba49c9b5a53)
#### Saturday 2022-03-26 20:21:06 by Hugo Virgilio

Fortune Commit: If I could stick my pen in my heart,
I would spill it all over the stage.
Would it satisfy ya, would it slide on by ya,
Would you think the boy was strange?
Ain't he strange?
...
If I could stick a knife in my heart,
Suicide right on the stage,
Would it be enough for your teenage lust,
Would it help to ease the pain?
Ease your brain?
		-- Rolling Stones, "It's Only Rock'N Roll"

---
## [NFrid/nfrid.ru](https://github.com/NFrid/nfrid.ru)@[7047b4ce12...](https://github.com/NFrid/nfrid.ru/commit/7047b4ce1236d9e59491dbb39269ce789c5e1d39)
#### Saturday 2022-03-26 20:35:40 by Nick Friday

rename nfrid.me -> nfrid.ru (fuck you godaddy you filthy thief)

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[e58fb506ef...](https://github.com/tgstation/tgstation/commit/e58fb506effebc734a661718bed9ab2ffeb50c9e)
#### Saturday 2022-03-26 20:48:09 by LemonInTheDark

Almost halves airlock auto close delay (#65349)

We go from a delay of 15 seconds, to 8.

This has cheesed me off for a long time. Airlocks should lock, not just
stay open for a quarter of a minute.

This'll help with excited groups that stay permenantly connected at
highpop because of a slowed ssair and doors opening and closing
constantly

Also effects door chasing. I'm honestly just kinda eyeballing this, it
might be a bit much. Even if this goes through could totally be tweaked

Even if this is too low, 15 is way too damn high.

---
## [SifuF/XBMC4Gamers](https://github.com/SifuF/XBMC4Gamers)@[9ca865137c...](https://github.com/SifuF/XBMC4Gamers/commit/9ca865137c5e5898f30a18c2c7a1a648836c5540)
#### Saturday 2022-03-26 22:51:23 by John

Version 1.3 Stable

Patron Supporters:
	Richard, Giovany Rodriguez, Alf John Hammervik, Rick Girton, thePiratePimp, Michael Bergeron, Wayne Starr, Stian Tofte, Johnny Andersen, Wayne Swift
	Clayton Beeney, Andrew Ryan, Tktagmedia, Darren Titchmarsh, Jay Jay, Natetronn, Incursion64 ., Roger Serres, Darren Old, Joel Peterson, Jamie Eubank

Thank you for your support.
Would also like to thank everyone that donates its much appreciated.

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

26/10/2020
	1) New look, redone basically all dialogs and menus.
		( some aren't done yet or wont be done )
	2) Optimized and organised the texture.xpr
		( should make it easier to theme )
	3) Sorted the string.po files so now you can translate it easily as it only includes string used.
	4) New xbe file with a few fixes.
	5) Removed the DVD2Xbox profile and skin, upgrading to this version will leave it intact.
		( only effects new users )
	6) Updated screenshot.py script to save as png.
	7) Moved the option to rip games to the skin settings > scripts menu
	8) New XBE to fixed intros for good now, should be no issues at all.
		( note if no network is present there is a 5 to 6 second pause before the first window, could not resolve this. )
	9) Optimised the textures and scripts so hopefully less ram usage and faster script running.
	10) Fixed the new view options showing when highlighting the scroll bar.
	11) Added the version the the options (black button)
	12) Removed the update check on startup and added it as a button on the login screen (start button) or in the skin settings.
	13) New night mode, enable it in the skin settings menu.
		( only available for the profiles skin )
	14) Fixed a few issues with the night theme.
	15) New loading animation (busy dialog)
	16) Now if Auto login is enabled for a profile if you press the RStick in it will bring up the Options menu.
	17) Made the xbe copy filezilla server.xml on every boot from the system/backups folder.
		( this seems to fix random crashing with FTP, also fixes the corrupt filezilla server.xml issue as its copied on each boot. )
	18) Intro videos can be in two places now. System\intro or next to the default.xbe
		( intro.mp4 is still looked for in both locations, I may at some point add random video playback from the intro folder )
	19) You can now run default_p.xbe or defaultxhd.xbe from the context menu if they exist next to the default.xbe
	20) New updater look.
	21) URLDownloader updated to v1.0.18, I have moved to Google Drive for the downloads.
		( Test this out as there is a daily limit on downloads but we should never hit this )
	22) Cleaned up all the scripts.
	23) Fixed a problem in XBMC (well just disabled stopping the FTP/Time server code) that would put you in a busy loop if you had an Ethernet
		connected but not valid network, or hard crash the system if you disconnect and reconnected a Ethernet.
	24) Added a new toggle for the banner view, lets to set the icons to scale (default) or stretch.
		( under the view options > other tab )
	25) Updated all of the dialogs used to use the new focus texture and background images, plus a darken the screen so you can see them better.
	26) Updated the dialog ok.py script so it can run script and notify the user that it is.
		( used for the update check )
	27) Moved the R-Stick and L-Stick context button round so the match the pad.
	28) Y button is now Synopsis, it will check for a xbe file so it wont load on content that's not got synopsis.
		( context menu synopsis entry is disabled if the y_button_loader.py is found, no point having them on both. )
	29) New keyboard layout for the hex colour string window.
	30) Fixed custom backgrounds flashing when entering the profile.
	31) Fixed the music visualisation not showing if enabled for screensaver.
	32) Minor bug fixes
	33) Fixed the view options search function.
	34) Added new options to the view options other menu for fanart.
		( now can toggle between on, blurred, off, fog and look )
	35) New full screen fanart toggle for the fanart view
	36) Updated some views to be faster.
	37) Fixed conflict with the new artwork installer if run from the scripts menu.
	38) Updated the synopsis script.
	39) Updated the alt synopsis view to disable images if ram hits less than 2%, so not to hang the system.
		( only reaaly an issue if playing music and a track changes while moving, so most wont ever have the issue but better safe than sorry )
	40) Changed the xbe texture release limit to 4MB before it does it.
	41) View options is now a dialog, so I had to move the soft options out of this menu.
		( button to focus this option is in its place )
	42) Sort options moved out of the view options menu as they wont work if the programs menu isn't the active window.
	43) Fixed the skin settings labels menu entries focus ids.
	44) New default icons, less in your face than before.
	45) Updated the settings menu order and added a indicator to show there are more items in the list.
	46) Updated the synopsis images
	47) Updated the CD view flipped CD image for the focus item.
		( there is no point drawing the rotating CD here as it doesn't rotate due to the diffuse image not being stationary )
	48) .modules is now _modules so now FTP programs can FTP the folder over without requiring hidden files to be enabled.
	49) Imagelib usage is now set to 8MB to combat ram hitting 0MB and causing black images.
	50) Clear texture cache set to 10MB now, so when you hit 10MB it will flush the texture cache.
	51) New xbe to check what resolution is currently enabled and tell the user if its 1080i and disable it.
	52) New no_fanart image.
	53) Updated labels for the pages and items in dialogs that use them.
	54) Added support for grabbing the titleid from the inserted xbox disc in the drive.
		( can now display artwork based on the titleids )
	55) New busy/loading overlay
	56) New Search and Sort look
	57) Updated the downloader script to the latest version.
	58) Added a preview window to the dialogselect window. Only shows when in the downloader theme menu
	59) Fixed the individual game save per profile script, forgot to update the titleid in the script.
	60) When a new profile is made it will restart XBMC4Gamers and auto load into said profile.
	61) Moved to the naming format for the folder that holds the skin xml files.
		( now just xml for all )
	62) Updated and fixed all views
		( some views now use the new images that come with the v1.9.4 and onwards version of the artwork installer )
	63) Changed all the view file names to make it easier to find a view.
	64) Optimisations to the views and synopsis window to help with 64MB ram boards.
	65) Any script errors will now put a copy of the error in E:/TDATA/Rocky5 needs these logs/
		( Send me this file )
	66) Fixed the placements of the context menus.
	67) Fixed the user mode controller buttons.
	68) Added back in the scrolling latter when fast scrolling your games.
	68) Updated the synopsis window, fixed a couple things.
	69) Updated the login profile windows, logs in and out quicker.
	70) New File Manager look.
	71) New labels for the file manager.
	 ( id 103 and 104 these are used to show the current folder you're in )
	72) Redone all the views :/ optimized and fixed.
	73) New default icons for file types.
	74) Theme selection added, yes you can now theme it and add your own themes.
		( .xpr file and optional color.xml name the xml the same name as the xpr )
	75) Theme specific splash image support, images go in Skins\profile skin\extras\themes\splashes\
	76) New Video Calibration screen.
	77) Now when a profile is first run it will ask the user to calibrate the screen.
	78) Can hide the labels on most views, can toggle between both, folders only or games only.
	79) New settings thumbs
	80) Redone all view options images
	81) Redone all default folder icons, now has default and night versions.
	82) Can use fonts file for themes.
		( named the same as the xpr )
	83) Some optimisation.
	84) More info on the options dialog
	85) Fixed search button label colour
	86) Update to the skin settings, removed the updates tab and replaced it with themes.
	87) DialogSelect will show a peview window for theme selection.
	89) Redone the XBMC4Gamers logo to be cleaner looking.
	90) Themes can have there own playlists.
		( Special://skin/extras/themes/playlists/theme name.m3u )
	91) Added two new colour labels for the games list labels that can be changed.
	92 Updated the main script that does the individual saves and profile setup on first run.
		( should fix all issues now )
	93) Fixed the icons and animations on the settings profile screen of the manage profiles profile.
	94) Fixed the new xbmc4gamers script breaking if it found the UDATA Backup folder and no user profile in the current UDATA folder.
	95) Added the option to view the log files under "skin settings > debug" menu
	96) Added the option to view text based files via the "skin settings > scripts" menu.
	97) Fixed the XISO to HDD Installer script to parse multi images.
		( test.1.iso, test.2.iso, test_1(2).iso and test_2(2).iso )
	98) Some cosmetic changes to labels on dialogs.
	99) log view and text viewer script updated.
	100) Option to hide the profile pic on load if auto login is enabled.
	101) missing xbmcgui from the updater script.
	102) Fixed the dash not loading if no network was found.
	103) Few odds and ends, you can now log into your profile from the Manage profiles profile easily.
		( should fix folk not knowing what to do :/ )
	104) Fixed the ISO to HDD script.
	105) A few backend changes to help me.
	106) New login screen look.
	106) Updated the seasonal xml files.
		( more snow flakes and different types, also no more eggs for easter. )
	107) Fixed valishing labels on the login screen and changed it a tad.
		( grouplists in lists don't use there alignment attributes so had to move them out of the list. )
	108) Uninstall downloaded themes script added.
	109) Couple xml fixes.
	110) Can launch default720p.xbe if found via the content menu.
	111) Random theme on startup support.
	112) New Random theme script to go with the new xbe so theme splashes are loaded on boot when random themes are enabled on startup.
	113) New xbe that adds support for ShowPicture() in python.
	114) Updated the Apply Theme script to allow 3 uses, toggle, select and random.
	115) FIxed the uninstall theme script.
	116) New option to enable or disable the theme playlist.
		( if you don't want the theme playlsit to override your playlist keep it disabled )
	117) Fixed the settings menu.
	118) Halloween even added.
		( all events are in one file now to make it cleaner )
	119) Added Appearance to the Manage Profiles Skin settings menu and updated the Screen Calibration image.
	120) Fixed the check for extra xbes, showing all if default_p.xbe was found.
	121) Fixed the edit mode login issues.
	122) New seek bar to match the new player controls.
	**) Other stuff but its been a while since I done these changes.
		( See if you can find them LOL )

---
## [amit-matreja/Malignant-Comments-Classifier](https://github.com/amit-matreja/Malignant-Comments-Classifier)@[2f36a5bb30...](https://github.com/amit-matreja/Malignant-Comments-Classifier/commit/2f36a5bb30e6a9f0c1b6ca164b2da34fbd2c1499)
#### Saturday 2022-03-26 23:36:07 by Amit Matreja

Add files via upload

MALIGNANT COMMENTS CLASSIFICATION

The proliferation of social media enables people to express their opinions widely online. However, at the same time, this has resulted in the emergence of conflict and hate, making online environments uninviting for users. Although researchers have found that hate is a problem across multiple platforms, there is a lack of models for online hate detection.
Online hate, described as abusive language, aggression, cyberbullying, hatefulness and many others has been identified as a major threat on online social media platforms. Social media platforms are the most prominent grounds for such toxic behaviour.   
There has been a remarkable increase in the cases of cyberbullying and trolls on various social media platforms. Many celebrities and influences are facing backlashes from people and have to come across hateful and offensive comments. This can take a toll on anyone and affect them mentally leading to depression, mental illness, self-hatred and suicidal thoughts.    
Internet comments are bastions of hatred and vitriol. While online anonymity has provided a new outlet for aggression and hate speech, machine learning can be used to fight it. The problem we sought to solve was the tagging of internet comments that are aggressive towards other users. This means that insults to third parties such as celebrities will be tagged as unoffensive, but “u are an idiot” is clearly offensive.
Our goal is to build a prototype of online hate and abuse comment classifier which can used to classify hate and offensive comments so that it can be controlled and restricted from spreading hatred and cyberbullying.

---
## [Timberpoes/tgstation-nxt](https://github.com/Timberpoes/tgstation-nxt)@[0e904f7032...](https://github.com/Timberpoes/tgstation-nxt/commit/0e904f70328a460af310014891eaadb5968ec31a)
#### Saturday 2022-03-26 23:37:58 by LemonInTheDark

[MDB IGNORE] Moves non floor turfs off /floor. You can put lattices on lavaland edition (#65504)


About The Pull Request

Alternative to #65354

Ok so like, there was a lot of not floor types on /floor. They didn't actually want any of their parent type's functionality, except maybe reacting to breaking (which was easy to move down) and some other minor stuff.
Part of what we don't want them to have is "plateable" logic.
I should not be able to put floor tiles on the snow and be fine. It's dumb.

Instead, I've moved all non floor types down to a new type, called /misc.

It holds very little logic. Mostly allowing pipes and wires and preventing blob stuff.
It also supports lattice based construction, which is one of the major changes here. I think it makes more sense, and it fixes an assumption in shuttle code that assumed you couldn't place "a new tile" by just hitting some snow with a floor tile.
Oh and lattices don't smooth with asteroid tiles anymore, this looks nicer I think.

Moving on to commits, and minor changes

Changes clf3 to try and burn any turfs it's exposed to, instead of just floors
Moves break_tile down to the turf definition, alongside burn_tile
If you're in basic buildmode and click on anything that's not handled in a targeted way, you just build plating
FUNCTION CHANGE: you can't use cult pylons to convert misc tiles over anymore
Generalizes building floors on top of something into two helper procs on /turf/open, reducing copypasta
Adds a new turf flag, IS_SOLID, that describes if a turf is tangible or not.
Uses this alongside a carpet and open check to replace plating and floor checks in carpet code. This does mean that non iron tiles can be carpeted, but I think that's fine

Moves the /floor update_icon -> update_visuals call to /open
This change is horrificly old, dating back to 8e112f6 but that commit describes nothing about why it was done. Choosing to believe it was a newfriend mistake. Uncomfortable nuking it though, because of just how old it is. Moving down instead

Create a buildable "misc" type off open, moves /dirt onto it
Basically, we want a type we can use to make something support
construction, since that can be a messy bit of logic. Also enough
structure to set things up sanely.

I'm planning on moving most misc turfs onto it, if only because
constructing on a dirt tile with rods should be possible, and the same
applies to most things

Murders captain planet, disentangles /turf/open/floor/grass/snow/basalt

Adds a diggable component that applies the behavior of "digging"
something out from a turf.

Uses it to free the above pain typepath into something a bit more
sensible

The typepaths that aren't actually used by floor tiles are moved onto
/misc

The others are given names that better describe them, and kept in
fancy_floor

Oh and snowshoes don't work on basalt anymore, sorry

Snowed over platings now actually have broken/burned icon states, fixing black holes to nowhere

Misc turfs no longer smooth as floors, so lattices will ignore them

Placing a lattice will no longer scrape the tile it's on

Ok this is a really old one.
I believe this logic is a holdover from kor's baseturf pr
(97990c9)
It used to be that turfs didn't have a concept of "beneath" and instead
just decided what should be under them by induction. This logic of "if
it's being latticed scapeaway to space" made sense then, but has since
been somewhat distorted

We do want to scape away on lattice spawn sometimes, mostly when we're
being destroyed, but not always. We especially don't want to scape away
if someone is just placing a rod, that's dumb.

Adds a path updating script for this change

I've done my best to find all the errors this repathing will pull out, but I may have missed some. I'm sorry.
Why It's Good For The Game

Very old code made better, more consistent turfs for lavaland and icebox, better visuals, minor fix to snowed plating, demon banishment in lattice placement, fixes the icebox mining shuttle not being repairable
Changelog

cl
add: Rather then being tileable with just floor tiles, lavaland turfs, asteroid and snow (among other things) now support lattice -> floor tile construction
fix: Because of the above, you can now properly fix the icebox mining shuttle
refactor: Non floor turfs are no longer typed as floor. This may break things, please yell at me if it does
/cl

---
## [nikp123/xava](https://github.com/nikp123/xava)@[14da8ea606...](https://github.com/nikp123/xava/commit/14da8ea6062d2c40f0d14c71920db0ab122ebb90)
#### Saturday 2022-03-26 23:41:14 by Nikola Pavlica

[bugfix] x11: remove stupid crtc monitor check

it may cause further bugs but the entirety of X11 is just fucking UB
and i absolutely hate it

C stands for Cease

---

