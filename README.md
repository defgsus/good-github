## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-03-09](docs/good-messages/2022/2022-03-09.md)


1,759,409 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,759,409 were push events containing 2,828,142 commit messages that amount to 205,771,949 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 48 messages:


## [uwstout-cs458-s22/advisor001](https://github.com/uwstout-cs458-s22/advisor001)@[bf6d5b5863...](https://github.com/uwstout-cs458-s22/advisor001/commit/bf6d5b586382c9138462004021ce71b34a564c9f)
#### Wednesday 2022-03-09 00:07:22 by Phosgenite

Current Attempt for api connection

pain.

Ruin has come to our family. You remember our venerable house, opulent and imperial, gazing proudly from its stoic perch above the moor? I lived all my years in that ancient, rumor shadowed manor, fattened by decadence and luxury - and yet I began to tire of conventional extravagance. Singular, unsettling tales suggested the mansion itself was a gateway to some fabulous and unnameable power. With relic and ritual I bent every effort towards the excavation and recovery of those long buried secrets, exhausting what remained of our family fortune on swarthy workmen and sturdy shovels.

At last in the salt soaked crags beneath the lowest foundations we unearthed that damnable portal of antediluvian evil. Our every step unsettled the ancient earth but we were in a realm of death and madness. In the end I alone fled laughing and wailing through those blackened arcades of antiquity until consciousness failed me.

You remember our venerable house, opulent and imperial. It is a festering abomination! I beg you. Return home; claim your birthright, and deliver our family from the ravenous, clutching shadows of the API functionality connection.

---
## [CitiesSkylinesMods/TMPE](https://github.com/CitiesSkylinesMods/TMPE)@[8ad7a2983d...](https://github.com/CitiesSkylinesMods/TMPE/commit/8ad7a2983d9e313858480015773933ca4c60a309)
#### Wednesday 2022-03-09 00:19:44 by aubergine10

gah, my brain while my friends are being bombed = mush

Note: FUCK ALL STATE FUNDED TERORIST GROUPS

---
## [vpsfreecz/linux](https://github.com/vpsfreecz/linux)@[0f323e87c8...](https://github.com/vpsfreecz/linux/commit/0f323e87c8ccacfaeaceaac38819a13413958fee)
#### Wednesday 2022-03-09 00:35:35 by Daniel Borkmann

mm: Consider __GFP_NOWARN flag for oversized kvmalloc() calls

commit 0708a0afe291bdfe1386d74d5ec1f0c27e8b9168 upstream.

syzkaller was recently triggering an oversized kvmalloc() warning via
xdp_umem_create().

The triggered warning was added back in 7661809d493b ("mm: don't allow
oversized kvmalloc() calls"). The rationale for the warning for huge
kvmalloc sizes was as a reaction to a security bug where the size was
more than UINT_MAX but not everything was prepared to handle unsigned
long sizes.

Anyway, the AF_XDP related call trace from this syzkaller report was:

  kvmalloc include/linux/mm.h:806 [inline]
  kvmalloc_array include/linux/mm.h:824 [inline]
  kvcalloc include/linux/mm.h:829 [inline]
  xdp_umem_pin_pages net/xdp/xdp_umem.c:102 [inline]
  xdp_umem_reg net/xdp/xdp_umem.c:219 [inline]
  xdp_umem_create+0x6a5/0xf00 net/xdp/xdp_umem.c:252
  xsk_setsockopt+0x604/0x790 net/xdp/xsk.c:1068
  __sys_setsockopt+0x1fd/0x4e0 net/socket.c:2176
  __do_sys_setsockopt net/socket.c:2187 [inline]
  __se_sys_setsockopt net/socket.c:2184 [inline]
  __x64_sys_setsockopt+0xb5/0x150 net/socket.c:2184
  do_syscall_x64 arch/x86/entry/common.c:50 [inline]
  do_syscall_64+0x35/0xb0 arch/x86/entry/common.c:80
  entry_SYSCALL_64_after_hwframe+0x44/0xae

Björn mentioned that requests for >2GB allocation can still be valid:

  The structure that is being allocated is the page-pinning accounting.
  AF_XDP has an internal limit of U32_MAX pages, which is *a lot*, but
  still fewer than what memcg allows (PAGE_COUNTER_MAX is a LONG_MAX/
  PAGE_SIZE on 64 bit systems). [...]

  I could just change from U32_MAX to INT_MAX, but as I stated earlier
  that has a hacky feeling to it. [...] From my perspective, the code
  isn't broken, with the memcg limits in consideration. [...]

Linus says:

  [...] Pretty much every time this has come up, the kernel warning has
  shown that yes, the code was broken and there really wasn't a reason
  for doing allocations that big.

  Of course, some people would be perfectly fine with the allocation
  failing, they just don't want the warning. I didn't want __GFP_NOWARN
  to shut it up originally because I wanted people to see all those
  cases, but these days I think we can just say "yeah, people can shut
  it up explicitly by saying 'go ahead and fail this allocation, don't
  warn about it'".

  So enough time has passed that by now I'd certainly be ok with [it].

Thus allow call-sites to silence such userspace triggered splats if the
allocation requests have __GFP_NOWARN. For xdp_umem_pin_pages()'s call
to kvcalloc() this is already the case, so nothing else needed there.

Fixes: 7661809d493b ("mm: don't allow oversized kvmalloc() calls")
Reported-by: syzbot+11421fbbff99b989670e@syzkaller.appspotmail.com
Suggested-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Tested-by: syzbot+11421fbbff99b989670e@syzkaller.appspotmail.com
Cc: Björn Töpel <bjorn@kernel.org>
Cc: Magnus Karlsson <magnus.karlsson@intel.com>
Cc: Willy Tarreau <w@1wt.eu>
Cc: Andrew Morton <akpm@linux-foundation.org>
Cc: Alexei Starovoitov <ast@kernel.org>
Cc: Andrii Nakryiko <andrii@kernel.org>
Cc: Jakub Kicinski <kuba@kernel.org>
Cc: David S. Miller <davem@davemloft.net>
Link: https://lore.kernel.org/bpf/CAJ+HfNhyfsT5cS_U9EC213ducHs9k9zNxX9+abqC0kTrPbQ0gg@mail.gmail.com
Link: https://lore.kernel.org/bpf/20211201202905.b9892171e3f5b9a60f9da251@linux-foundation.org
Reviewed-by: Leon Romanovsky <leonro@nvidia.com>
Ackd-by: Michal Hocko <mhocko@suse.com>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [TeodorD420/tgstation](https://github.com/TeodorD420/tgstation)@[3bd5a2d8df...](https://github.com/TeodorD420/tgstation/commit/3bd5a2d8df49213708540f1c0ffe0873b5d2e233)
#### Wednesday 2022-03-09 01:06:36 by Wallem

Makes Ants glow, puts a minimum on ant screaming and shoe permeability, and other ant-related things. (#64786)

I found out how emissives work and my first thought was "damn ants should glow that would look sick"
So now they do.

Also, having less than 5u ants in your body will make you not scream, so 0.0001u ants will no longer have that tiny chance of making someone scream for their life.

If an ant pile has a max damage value less than 1, then they won't be able to bite through your shoes. This is the same threshold as the second tier ant icon.

Makes the giant ant a hostile mob with the neutral faction, meaning they will attack anything not in the neutral faction.

---
## [Trilbyspaceclone/sojourn-station](https://github.com/Trilbyspaceclone/sojourn-station)@[83c7559f7c...](https://github.com/Trilbyspaceclone/sojourn-station/commit/83c7559f7c9d151b330239652f0b66ba3463584a)
#### Wednesday 2022-03-09 02:13:03 by WilliamNelson37

Fratellis and Co

Finishes the Fratellis

Removed Low level code that allowed staff to vore people (why the fuck)

Removed Low level code that allowed staff to regurgitate vored people (god's light has diminished)

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[f1d38cedcf...](https://github.com/LemonInTheDark/tgstation/commit/f1d38cedcfb82d0c2fad1b5dad429de8df5ee873)
#### Wednesday 2022-03-09 04:19:03 by LemonInTheDark

Almost halves airlock auto close delay

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
## [AysheDaArtist/sojourn-station](https://github.com/AysheDaArtist/sojourn-station)@[66a6e3d75b...](https://github.com/AysheDaArtist/sojourn-station/commit/66a6e3d75b1fd8cd72b3b22441443186c71832da)
#### Wednesday 2022-03-09 04:33:37 by Bones

More Genes then JC Pennies!

bottomless belly given to doggos. Increases max capacity for nutrition to 4 times the amount. good for long journeys if you can fill up. -10%
cat eyes on panthers and cats. Gives increased dark vision. Flashes will wreck your ass. -20%
cold resistance renamed into Thick Fur. Thick fur given to bears and corgis of all kind (protect Ian)  Now gives 10% brute resist along with cold resistance. Gives 10% burn weakness and takes up skin mutation slot - 20% instability.
honk given to geese. Literally just makes you honk like a dork
Echolocation given to bats.  allows you to see without eyes. -40% (If people abuse this with organ insertions I will make it turn your vision fucking black)
screaming given to possoms. Like moo and honk but for those who must scream!
toxin resistance given to snakes and bats. Gives a 10% reduction in toxin damage taken. 20% instability
Balances cowhide to cause 20% instability (Agreed amount with Hex)
Creates MUT_TYPE_EYES to keep from gaining all the eye genes.
Barotrauma gene added to space sharks/great whites. costs 20% instability. Gives pressure resistance.

---
## [payday-restoration/restoration-mod](https://github.com/payday-restoration/restoration-mod)@[81df0d577e...](https://github.com/payday-restoration/restoration-mod/commit/81df0d577ea6810aef7aba782067ba46f861135d)
#### Wednesday 2022-03-09 05:14:03 by Reeeno

_sc zeals (crashes)

i dont fucking care i hate working on them someone else fix this shit

---
## [repinger/exynos9611_m21_kernel](https://github.com/repinger/exynos9611_m21_kernel)@[f2ae024774...](https://github.com/repinger/exynos9611_m21_kernel/commit/f2ae0247743c9a7633cef873edbed1338262c83d)
#### Wednesday 2022-03-09 05:53:48 by Dave Chiluk

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

---
## [mrsafalpiya/spl](https://github.com/mrsafalpiya/spl)@[a42236b320...](https://github.com/mrsafalpiya/spl/commit/a42236b32097a4f08f153dd47cb2ffa001ebc04a)
#### Wednesday 2022-03-09 05:54:02 by Safal Piya

spl_flags.h: Fixed long-non-equal argument bug and added non_defined_flags

Previously the long-non-equal argument was searching for secondary flags
(which was always true) and thus looping through and adding the argument
to non_defined_flags.

The solution in my opinion is kinda ugly :( But still I don't wanna
create code redundancy i.e. create two similar codes (only editing the
secondary flag checking part) for ARG_SHORT_NON_EQUAL and
ARG_LONG_NON_EQUAL.

Also, the non_defined_flags is added along with non_defined_flags_c

---
## [mamh-mixed/microsoft-terminal](https://github.com/mamh-mixed/microsoft-terminal)@[b1ace967a2...](https://github.com/mamh-mixed/microsoft-terminal/commit/b1ace967a2f2bf17fdcb7dd4f1426b014378b83c)
#### Wednesday 2022-03-09 06:26:33 by Mike Griese

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
## [double-a-stories/life-of-the-party](https://github.com/double-a-stories/life-of-the-party)@[a0338e74e1...](https://github.com/double-a-stories/life-of-the-party/commit/a0338e74e1a050692d68d45dbbcf445ebca863a4)
#### Wednesday 2022-03-09 06:34:00 by double-a-stories

Changed most instances of "God" to other stuff

-Most characters reflexively use "oh my gosh" instead.
-Nikki/Nox are polytheists, and say "gods"
-Ana uses "G-d" instead. She's Jewish.
-Hollis's commands still use "oh god oh fuck"
-The "pantheon of animal gods" are no longer forgotten.

---
## [MisterTea/mame](https://github.com/MisterTea/mame)@[137649ccec...](https://github.com/MisterTea/mame/commit/137649ccec8159929e68212470b41eeed136b252)
#### Wednesday 2022-03-09 06:35:48 by Firehawke

New working software list additions (apple2gs_flop_clcracked.xml) (#8712)

* New working software list additions (apple2gs_flop_clcracked.xml)
-----------------------------------------------------------------

Aesop's Fables (cleanly cracked) [Brian Troha]
All About America (cleanly cracked) [Brian Troha]
Ancient Land of Ys (cleanly cracked) [Brian Troha]
Arkanoid (Version 12-Jan-89) (cleanly cracked) [Brian Troha]
Arkanoid II: Revenge of Doh (Version 29-Aug-89) (cleanly cracked) [Brian Troha]
Arkanoid II: Revenge of Doh (Version 18-Jul-89) (cleanly cracked) [Brian Troha]
Battle Chess (cleanly cracked) [Brian Troha]
Block Out (Version 1.0) (cleanly cracked) [Brian Troha]
Bubble Ghost (cleanly cracked) [Brian Troha]
Bubble Ghost - Hard Drive compatible (cleanly cracked) [Brian Troha]
Calendar Crafter (Version 1.2) (cleanly cracked) [Brian Troha]
California Games (cleanly cracked) [Brian Troha]
Captain Blood (cleanly cracked) [Brian Troha]
Cavern Cobra (cleanly cracked) [Brian Troha]
Club Backgammon (Version 2.0) (cleanly cracked) [Brian Troha]
Club Backgammon (Version 1.0) (cleanly cracked) [Brian Troha]
Cribbage King / Gin King (Version 1.01) (cleanly cracked) [Brian Troha]
Defender of the Crown (cleanly cracked) [Brian Troha]
Déjà Vu (cleanly cracked) [Brian Troha]
Déjà Vu II: Lost in Las Vegas (cleanly cracked) [Brian Troha]
Designer Prints (Version 1.0) (cleanly cracked) [Brian Troha]
Designer Puzzles (Version 1.0) (cleanly cracked) [Brian Troha]
Destroyer (cleanly cracked) [Brian Troha]
Downhill Challenge (cleanly cracked) [Brian Troha]
Fantavision (Version 2.1) (cleanly cracked) [Brian Troha]
Fantavision (Version 1.0) (cleanly cracked) [Brian Troha]
Fast Break (cleanly cracked) [Brian Troha]
Final Assault (cleanly cracked) [Brian Troha]
Gauntlet (cleanly cracked) [Brian Troha]
Geometry (Version 1.0) (cleanly cracked) [Brian Troha]
Gnarly Golf (cleanly cracked) [Brian Troha]
Grand Prix Circuit (cleanly cracked) [Brian Troha]
Great Western Shootout (cleanly cracked) [Brian Troha]
Hacker II: The Doomsday Papers (cleanly cracked) [Brian Troha]
Hardball! (cleanly cracked) [Brian Troha]
Hostage: Rescue Mission (cleanly cracked) [Brian Troha]
Impossible Mission II (cleanly cracked) [Brian Troha]
Jack Nicklaus' Greatest 18 Holes of Major Championship Golf (cleanly cracked) [Brian Troha]
Jigsaw (Version 1.4 - 022988) (cleanly cracked) [Brian Troha]
King's Quest - Quest for the Crown (cleanly cracked) [Brian Troha]
King's Quest II - Romancing The Throne (cleanly cracked) [Brian Troha]
King's Quest III - To Hier is Human (cleanly cracked) [Brian Troha]
LaserForce (cleanly cracked) [Brian Troha]
Leisure Suit Larry in the Land of the Lounge Lizards (cleanly cracked) [Brian Troha]
Magical Myths (cleanly cracked) [Brian Troha]
Mancala (Version 1.0) (cleanly cracked) [Brian Troha]
Marble Madness (cleanly cracked) [Brian Troha]
Math Blaster Plus! (Version 1.1) (cleanly cracked) [Brian Troha]
Math Blaster Plus! (Version 1.0) (cleanly cracked) [Brian Troha]
Math Wizard (cleanly cracked) [Brian Troha]
Mavis Beacon Teaches Typing (Version 1.8 21-Dec-88) (cleanly cracked) [Brian Troha]
Mavis Beacon Teaches Typing (Version 1.2 16-Nov-87) (cleanly cracked) [Brian Troha]
Mean 18 (cleanly cracked) [Brian Troha]
Mercury (Version 1.0) (cleanly cracked) [Brian Troha]
Music Construction Set (Version 1.0) (cleanly cracked) [Brian Troha]
Neuromancer (cleanly cracked) [Brian Troha]
Paperboy (cleanly cracked) [Brian Troha]
Pipe Dream (cleanly cracked) [Brian Troha]
Qix (Version 1.4? 16-Jan-90) (cleanly cracked) [Brian Troha]
Read and Rhyme (cleanly cracked) [Brian Troha]
Read-a-Rama (cleanly cracked) [Brian Troha]
Reader Rabbit (Version 2.3) (cleanly cracked) [Brian Troha]
Reader Rabbit (Version 2.2) (cleanly cracked) [Brian Troha]
Reading and Me (Version 1.0) (cleanly cracked) [Brian Troha]
Sea Strike (Version 1.0) (cleanly cracked) [Brian Troha]
Serve and Volley (cleanly cracked) [Brian Troha]
Shanghai (Version 15-Sep-87) (cleanly cracked) [Brian Troha]
Shanghai (Version 20-Jan-87) (cleanly cracked) [Brian Troha]
ShowOff (Version 1.1) (cleanly cracked) [Brian Troha]
Silent Service (Version 925.01) (cleanly cracked) [Brian Troha]
Silpheed - Super Dogfighter (cleanly cracked) [Brian Troha]
Skate or Die (Version 1.1 07-Oct-88) (cleanly cracked) [Brian Troha]
Skate or Die (Version 1.0 12-Aug-88) (cleanly cracked) [Brian Troha]
Space Quest - The Sarien Encounter (cleanly cracked) [Brian Troha]
Space Quest II - Vohual's Revenge (cleanly cracked) [Brian Troha]
Spirit of Excalibur (cleanly cracked) [Brian Troha]
Storybook Weaver (Version 1.0) (cleanly cracked) [Brian Troha]
Storybook Weaver - World of Adventure (Version 1.0) (cleanly cracked) [Brian Troha]
Storybook Weaver - World of Make-Believe (Version 1.0) (cleanly cracked) [Brian Troha]
Street Sports Soccer (cleanly cracked) [Brian Troha]
Superstar Ice Hockey (cleanly cracked) [Brian Troha]
Tales From The Arabian Nights (cleanly cracked) [Brian Troha]
Task Force (cleanly cracked) [Brian Troha]
Tetris (cleanly cracked) [Brian Troha]
The Adventures of Sinbad (cleanly cracked) [Brian Troha]
The Duel: Test Drive II (cleanly cracked) [Brian Troha]
The Fidelity Chessmaster 2100 (Version 1.1 17-Nov-88) (cleanly cracked) [Brian Troha]
The Fidelity Chessmaster 2100 (Version 1.01 28-Sep-88) (cleanly cracked) [Brian Troha]
The Graphics Studio (cleanly cracked) [Brian Troha]
The Immortal (cleanly cracked) [Brian Troha]
The King of Chicago (cleanly cracked) [Brian Troha]
The Last Ninja (cleanly cracked) [Brian Troha]
The Logic Master (Version 1.5) (cleanly cracked) [Brian Troha]
The Print Shop (Version 1.0) (cleanly cracked) [Brian Troha]
The Third Courier (cleanly cracked) [Brian Troha]
The Tower of Myraglen (Version 1.0) (cleanly cracked) [Brian Troha]
The Wonders of the Animal Kingdom (cleanly cracked) [Brian Troha]
The Word Master (cleanly cracked) [Brian Troha]
Thexder (Version 2.7) (cleanly cracked) [Brian Troha]
Topdraw (Version 1.00A) (cleanly cracked) [Brian Troha]
TrianGo (Version 1.0) (cleanly cracked) [Brian Troha]
Uninvited (cleanly cracked) [Brian Troha]
Vegas Craps (Version 1.0) (cleanly cracked) [Brian Troha]
Vegas Gambler (Version 1.1 25-Jul-88) (cleanly cracked) [Brian Troha]
Vegas Gambler (Version 1.0 07-Jun-88) (cleanly cracked) [Brian Troha]
War in Middle Earth (cleanly cracked) [Brian Troha]
Where in the U.S.A. is Carmen Sandiego? (cleanly cracked) [Brian Troha]
Where in the World is Carmen Sandiego? (cleanly cracked) [Brian Troha]
Winter Games (cleanly cracked) [Brian Troha]
World Games (cleanly cracked) [Brian Troha]
World Tour Golf (cleanly cracked) [Brian Troha]
Writer's Choice Elite (cleanly cracked) [Brian Troha]
Xenocide (Version 25-Sep-89) (unprotected) [Brian Troha]
Xenocide (Version 11-Aug-89) (cleanly cracked) [Brian Troha]
Zany Golf (cleanly cracked) [Brian Troha]

---
## [double-a-stories/life-of-the-party](https://github.com/double-a-stories/life-of-the-party)@[df58753d98...](https://github.com/double-a-stories/life-of-the-party/commit/df58753d98eb8a48b62077ea7d51daeacb628e45)
#### Wednesday 2022-03-09 06:56:21 by double-a-stories

Changed religious references (e.g. "God")...

-Most characters reflexively use "oh my gosh" instead.
-Nikki/Nox are polytheists, and say "gods"
-Ana says "woof" and "oh my fuck" instead.
-Hollis's commands still use "oh god oh fuck"
-The "pantheon of animal gods" are no longer forgotten.

---
## [entn-at/flashlight](https://github.com/entn-at/flashlight)@[14888c51d1...](https://github.com/entn-at/flashlight/commit/14888c51d174519278712dd0bc8d4bb29f074b4f)
#### Wednesday 2022-03-09 07:16:21 by Jacob Kahn

Move flashlight to C++14 (#267)

Summary:
Pull Request resolved: https://github.com/facebookresearch/flashlight/pull/267

Upgrade to C++ 14.

We've been talking about this for some time; I think it's time to make the transition.

To be honest, moving to C++17 may not be a bad step in the near future, but making incremental changes will make this transition easier.

For now, this change only removes backports for `make_unique` and various `type_traits`, and leaves other things as they are for now.

### General Thoughts
- Staying >= 4 years behind the standard (2020 - 2014), to me, is extremely reasonable
- ArrayFire already requires C++14 to build from source
- gcc >= 5 has solid support for C++14 already, and that's our compiler recommendation as is since we use some "advanced" C++11 features.
- PyTorch has a C++14 minimum for its C++ API to build from source, so this is consistent with other competing frameworks frameworks

### What's new in C++14?
A light summary here — there are a wealth of new features that make life better:
- `std::make_unique<T>` (enough said)
- Removal of a bunch of awful type trait backports
  - `std::remove_const_t` and friends
  - `decay_t`!
- `auto` as a return type for functions
- `auto` lambda params!
```
auto fun = [](auto v) { return v + 1; };
```
- Move capture rather than reference in a persistent pointer!
```
auto _myFoo = std::make_unique<Foo>();
auto fun = [myFoo = std::move(_myFoo)]() { ... }
```
- Compile time literals for a bunch of stuff (datetime, string)
```
using namespace std::chrono_literals;
auto week = 168h;
```

Reviewed By: tlikhomanenko

Differential Revision: D25037733

fbshipit-source-id: 9d88d39922e544e6a5bde2ce5f5bafb9f319acca

---
## [psarna/scylla](https://github.com/psarna/scylla)@[674d3a5a84...](https://github.com/psarna/scylla/commit/674d3a5a8465c365cb0e608f4c921e3c12b758c6)
#### Wednesday 2022-03-09 07:58:27 by Nadav Har'El

compound_compat.hh: add missing methods of iterator

While debugging legacy_compound_view, I noticed that it cannot be used
as a C++20 std::ranges::input_range because it is missing some trivial
methods. So let's fix this, and make the life of future developers a
little bit easier.

The two trivial methods we need to implement:

1. A postfix increment operator. We already had a prefix increment
   operator, but the C++20 concept weakly_iterable also needs postfix.

2. By mistake (this will be corrected in https://wg21.link/P2325R3),
   weakly_iterable also required the default_initialized concept, so
   our iterator type also needs a default constructor.
   We'll never actually use this silly constructor, and when this C++20
   standard mistake is corrected, we can remove this constructor.

After this patch, a legacy_compound_view is accepted for the C++20
ranges::input_range concept.

Signed-off-by: Nadav Har'El <nyh@scylladb.com>

---
## [downthecrop/2009scape-mirror](https://github.com/downthecrop/2009scape-mirror)@[7968367e14...](https://github.com/downthecrop/2009scape-mirror/commit/7968367e147fc3567f1785f80bdf90923519c0c1)
#### Wednesday 2022-03-09 08:20:09 by skelsoft

The Fremmenik Trials quest has been completed, now accesible in-game

Barrows prayer drain timer standardized to 18 seconds

Giant Mole's Burrow mechanic corrected in functionality. Burrow: When the mole's health is between 5-50%, there is a 25% chance for any incoming attack to cause it to burrow away into another location. There is also a chance that the dirt she digs while burrowing to escape can extinguish the player's light source (shown with dirt splatters on the player's screen), though covered light sources will be unaffected by this.

Mole Lair's unique music track now correctly plays across the entirety of the Mole Lair region

Giant Mole droptable corrected. Egregious RSPS noted secondary drops removed. G. Mole can now correctly drop random Hard Clues, and the 100 Iron Ore (noted) drop has been added.

Hostile Random Events return! Tree Spirit, River Troll, Rock Golem, Shade, and Zombie Hostile Random Events rejoin the Evil Chicken in their AFK-anihilation onslaught! Beware!

Mounted Glories now have full right-click Teleport options

You can now build an Obelisk inside your POH at 41 Construction, as the centrepiece spot inside a standard Garden room

Can now trade in Long and Curved bones to Barlak in the Dorgeshuun Mine (temporary location for now) for Construction EXP (after completion of The Lost Tribe)

Ridiculous amounts of funky fresh new NPC dialogues by Q in the following areas: LLetya, Isafdar, Ardougne, Witchaven, Ape Atoll, Miscellania, Dorgeshuun, Zanaris and many many many more!

Potion decanting note bug should now be fixed and not eat up all your notes when attempting to decant

Weapon Poison addition and removal fixes

All currently functional Summoning familiars with invisible skills boosts are now correctly added to the game! Pyrelord, Forge Regent, Arctic Bear, Lava Titan, Magpie, Spirit Graahk, Spirit Larupia, Spirit Kyatt, Void Ravager and Wolpertinger now boost skills alongside their other helpful abilities.

The Mining Guild can now be entered under 60 Mining via the use of skill boosts

The Lady of the Lake will now finally enhance Excalibur for you if you have the prerequisite Seers Hard Diary and Merlin's Crystal completed, and the headband and sword equipped when talking to her.

Can now fish slimy eels

Restored the removed/regressed/whatever Bot Dialogues!

All Ancient Warriors' Equipment (Vesta, Zuriel etc) is now correctly tradeable and droppable in its un-degraded form

Some hat clipping fixes

Fixed blanket Wilderness aggression forcing even non-aggressive monsters to be aggressive

Fremennik helmets (eg: archers, warriors, etc) now locked behind Fremennik Trials Quest

Added the following SFX:
giant mole combat sfx
water elemental combat sfx
fire elemental combat sfx
earth elemental combat sfx
air elemental combat sfx
baby blue dragon combat sfx
baby red dragon combat sfx + examine
baby black dragon combat sfx
black demon combat sfx
dark beast combat sfx
dust devil combat sfx
gargoyle combat sfx
fire giant combat sfx
moss giant combat sfx
hill giant combat sfx
nechryael combat sfx
turoth combat sfx
kurask combat sfx
wallasalki combat sfx
yak combat sfx
abyssal demon combat sfx
bloodveld combat sfx
cave crawler combat sfx
Digging with spade SFX added
abyssal leech combat sfx
abyssal walker combat sfx
void brawler combat sfx (pest control)
chaos elemental standard combat sfx (NOT spells)
cockatrice combat sfx
crawling hand combat sfx
crocodile combat sfx
void defiler combat sfx (pest control)
lesser demon champion combat sfx
elf warrior combat sfx
ghoul combat sfx
ghoul champion combat sfx
jelly combat sfx
pyrefiend combat sfx
void ravager combat sfx (pest control)
rock lobster combat sfx
rockslug combat sfx
void shifter combat sfx (pest control)
void spinner combat sfx (pest control)
void splatter combat sfx (pest control)
void torcher combat sfx (pest control)
starlight combat sfx (GWD: Saradomin Melee Minion)
growler combat sfx (GWD: Saradomin Mage Minion)
Picking herb/harvesting crop SFX added
Planting a seed with seed dibber SFX added
Digging up patch with a Spade SFX added
Raking a patch SFX added
Watering a farming patch with a Watering can SFX added
Using a Plant Cure on a diseased patch SFX added
Pouring Compost/Supercompost on a farming patch SFX added
Filling Compost Bin SFX added
Opening and closing the Compost Bin SFX added
Filling buckets with Compost from the Compost Bin SFX added
Chaos Elemental's three unique spells (Discord, Madness, and Confusion) now have correct impact sfx when hitting the player

Standard Seed Bird's Nest loot pool corrections

Ring Bird's Nest loot pool corrected

Wyson Bird's Nest loot pool corrected

Wyson Bird's Nest loot quantities corrected

Fixed tick delay on Fletching bows and crossbows

Chaos Elemental Drop Table Overhaul

Chaos Elemental's Main drop table has been overhauled to correct items, amounts, and (close-enough) weights

Chaos Elemental's Minor drop table added, using Item ID 799 as an item container

Chaos Elemental now correctly rolls 1 minor drop and 1 major drop from its minor/major loot tables when it is killed.

Restrict Dwarven Multicannon use inside Fremennik Slayer Cave

---
## [ThatRedKite/thatkitebot](https://github.com/ThatRedKite/thatkitebot)@[0fa6685c66...](https://github.com/ThatRedKite/thatkitebot/commit/0fa6685c66f08908ca179d526a8156bc771a8b88)
#### Wednesday 2022-03-09 08:24:42 by Jack Woo

Added UWUify command  (#43)

* Added 8ball command

* damn i am an idiot

* i should probably check this next time

* Added uwuify command (im sorry mom)

---
## [laminas/.github](https://github.com/laminas/.github)@[0c61a71747...](https://github.com/laminas/.github/commit/0c61a7174702b0a0b881b6a09aa06fe1710b5c88)
#### Wednesday 2022-03-09 08:32:58 by Michał Bundyra

Message against the war, in Russian and English

🇷🇺 Русским гражданам

Мы, участники Laminas, родились и живем в разных странах. У многих из нас есть друзья, родственники и коллеги как в России, так и в Украине. Некоторые из нас родились в России. Некоторые из нас живут в России. У некоторых бабушки и дедушки сражались с фашистами во Второй мировой войне. Здесь никто не поддерживает фашизм.

У одного из нас есть украинская родственница, которая спаслась из дома вместе с сыном. Поезд задержался из-за бомбежки на дороге впереди. У нас есть друзья, которые прячутся в бомбоубежищах. Мы с тревогой ждем весточки от них после воздушных налетов, которые беспорядочно наносят удары и попадают по больницам, школам, детским садам и домам. Мы не берем это из каких-либо СМИ. Мы наблюдаем это напрямую.

Вы доверяете нам достаточно, чтоб использовать наши программы, и мы просим вас довериться нам вновь. Мы нуждаемся в помощи. Выходите и протестуйте против этой бесполезной войны. Остановите кровопролитие. Скажите "Нет войне!"

🇺🇸 To Citizens of Russia

We at Laminas come from all over the world. Many of us have friends, family and colleagues in both Russia and Ukraine. Some of us were born in Russia. Some of us currently live in Russia. Some have grandparents who fought Nazis in World War II. Nobody here supports fascism.

One team member has a Ukrainian relative who fled her home with her son. The train was delayed due to bombing on the road ahead. We have friends who are hiding in bomb shelters. We anxiously follow up on them after the air raids, which indiscriminately fire at hospitals, schools, kindergartens and houses. Were not taking this from any media. These are our actual experiences.

You trust us enough to use our software. We ask that you trust us to say the truth on this. We need your help. Go out and protest this unnecessary war. Stop the bloodshed. Say "stop the war!"

Signed-off-by: Michał Bundyra <contact@webimpress.com>

---
## [henricaodopao1/kernel-to-flash-to-use-to-report-unexistent-bugs-to-feed-to-sleep-to-talk-to](https://github.com/henricaodopao1/kernel-to-flash-to-use-to-report-unexistent-bugs-to-feed-to-sleep-to-talk-to)@[5d3e5eb541...](https://github.com/henricaodopao1/kernel-to-flash-to-use-to-report-unexistent-bugs-to-feed-to-sleep-to-talk-to/commit/5d3e5eb541caa47382e2284ee37f96e8264e10f8)
#### Wednesday 2022-03-09 10:28:39 by Maciej Żenczykowski

FROMGIT: bpf: Do not change gso_size during bpf_skb_change_proto()

This is technically a backwards incompatible change in behaviour, but I'm
going to argue that it is very unlikely to break things, and likely to fix
*far* more then it breaks.

In no particular order, various reasons follow:

(a) I've long had a bug assigned to myself to debug a super rare kernel crash
on Android Pixel phones which can (per stacktrace) be traced back to BPF clat
IPv6 to IPv4 protocol conversion causing some sort of ugly failure much later
on during transmit deep in the GSO engine, AFAICT precisely because of this
change to gso_size, though I've never been able to manually reproduce it. I
believe it may be related to the particular network offload support of attached
USB ethernet dongle being used for tethering off of an IPv6-only cellular
connection. The reason might be we end up with more segments than max permitted,
or with a GSO packet with only one segment... (either way we break some
assumption and hit a BUG_ON)

(b) There is no check that the gso_size is > 20 when reducing it by 20, so we
might end up with a negative (or underflowing) gso_size or a gso_size of 0.
This can't possibly be good. Indeed this is probably somehow exploitable (or
at least can result in a kernel crash) by delivering crafted packets and perhaps
triggering an infinite loop or a divide by zero... As a reminder: gso_size (MSS)
is related to MTU, but not directly derived from it: gso_size/MSS may be
significantly smaller then one would get by deriving from local MTU. And on
some NICs (which do loose MTU checking on receive, it may even potentially be
larger, for example my work pc with 1500 MTU can receive 1520 byte frames [and
sometimes does due to bugs in a vendor plat46 implementation]). Indeed even just
going from 21 to 1 is potentially problematic because it increases the number
of segments by a factor of 21 (think DoS, or some other crash due to too many
segments).

(c) It's always safe to not increase the gso_size, because it doesn't result in
the max packet size increasing.  So the skb_increase_gso_size() call was always
unnecessary for correctness (and outright undesirable, see later). As such the
only part which is potentially dangerous (ie. could cause backwards compatibility
issues) is the removal of the skb_decrease_gso_size() call.

(d) If the packets are ultimately destined to the local device, then there is
absolutely no benefit to playing around with gso_size. It only matters if the
packets will egress the device. ie. we're either forwarding, or transmitting
from the device.

(e) This logic only triggers for packets which are GSO. It does not trigger for
skbs which are not GSO. It will not convert a non-GSO MTU sized packet into a
GSO packet (and you don't even know what the MTU is, so you can't even fix it).
As such your transmit path must *already* be able to handle an MTU 20 bytes
larger then your receive path (for IPv4 to IPv6 translation) - and indeed 28
bytes larger due to IPv4 fragments. Thus removing the skb_decrease_gso_size()
call doesn't actually increase the size of the packets your transmit side must
be able to handle. ie. to handle non-GSO max-MTU packets, the IPv4/IPv6 device/
route MTUs must already be set correctly. Since for example with an IPv4 egress
MTU of 1500, IPv4 to IPv6 translation will already build 1520 byte IPv6 frames,
so you need a 1520 byte device MTU. This means if your IPv6 device's egress
MTU is 1280, your IPv4 route must be 1260 (and actually 1252, because of the
need to handle fragments). This is to handle normal non-GSO packets. Thus the
reduction is simply not needed for GSO packets, because when they're correctly
built, they will already be the right size.

(f) TSO/GSO should be able to exactly undo GRO: the number of packets (TCP
segments) should not be modified, so that TCP's MSS counting works correctly
(this matters for congestion control). If protocol conversion changes the
gso_size, then the number of TCP segments may increase or decrease. Packet loss
after protocol conversion can result in partial loss of MSS segments that the
sender sent. How's the sending TCP stack going to react to receiving ACKs/SACKs
in the middle of the segments it sent?

(g) skb_{decrease,increase}_gso_size() are already no-ops for GSO_BY_FRAGS
case (besides triggering WARN_ON_ONCE). This means you already cannot guarantee
that gso_size (and thus resulting packet MTU) is changed. ie. you must assume
it won't be changed.

(h) changing gso_size is outright buggy for UDP GSO packets, where framing
matters (I believe that's also the case for SCTP, but it's already excluded
by [g]).  So the only remaining case is TCP, which also doesn't want it
(see [f]).

(i) see also the reasoning on the previous attempt at fixing this
(commit fa7b83bf3b156c767f3e4a25bbf3817b08f3ff8e) which shows that the current
behaviour causes TCP packet loss:

  In the forwarding path GRO -> BPF 6 to 4 -> GSO for TCP traffic, the
  coalesced packet payload can be > MSS, but < MSS + 20.

  bpf_skb_proto_6_to_4() will upgrade the MSS and it can be > the payload
  length. After then tcp_gso_segment checks for the payload length if it
  is <= MSS. The condition is causing the packet to be dropped.

  tcp_gso_segment():
    [...]
    mss = skb_shinfo(skb)->gso_size;
    if (unlikely(skb->len <= mss)) goto out;
    [...]

Thus changing the gso_size is simply a very bad idea. Increasing is unnecessary
and buggy, and decreasing can go negative.

Fixes: 6578171a7ff0 ("bpf: add bpf_skb_change_proto helper")
Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Cc: Dongseok Yi <dseok.yi@samsung.com>
Cc: Willem de Bruijn <willemb@google.com>
Link: https://lore.kernel.org/bpf/CANP3RGfjLikQ6dg=YpBU0OeHvyv7JOki7CyOUS9modaXAi-9vQ@mail.gmail.com
Link: https://lore.kernel.org/bpf/20210617000953.2787453-2-zenczykowski@gmail.com

(cherry picked from commit 364745fbe981a4370f50274475da4675661104df https://git.kernel.org/pub/scm/linux/kernel/git/bpf/bpf-next.git/commit/?id=364745fbe981a4370f50274475da4675661104df )
Test: builds, TreeHugger
Bug: 158835517
Bug: 188690383
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Change-Id: I0ef3174cbd3caaa42d5779334a9c0bfdc9ab81f5

---
## [scr1pti3/Gaelog](https://github.com/scr1pti3/Gaelog)@[3dd006f4e6...](https://github.com/scr1pti3/Gaelog/commit/3dd006f4e6e1a3539b3da5a26043160e9a33ce7c)
#### Wednesday 2022-03-09 10:48:06 by Raznan

Okay, so I just had to fking deal with debugging a plugin which is not a
very fun way to waste my ever so scarce free time. THEN! God itself had
to butt fk me with this blasphemous behavioural shit with this
fjhwebfhujebfghkr fvj code! please wai....

I tried adding a forward/skip function for the cursor, in which it would
forward the cursor and render the data on screen immediately for the
next node, but noooooooooooooooooooooooooooo. It just had to that the
Engine decides it would emit my signal forward twice from who knows where,
forwarding all my rendered data until the fking stone age. I tried to debug it all day,
but i cant find a single damn reason for that signal to be called twice!
when i am just calling it once.... And I can the fuckk not stand using Godot's
command line debugger any further. It is a torturous, and bad for the soul.

In what universe does a command line debugger not have the feature to
list my current file so i can see where the fuck i am currently
at!!!#12iewnfjdwfdf I AM DEAD.

---
## [gotenksIN/device_xiaomi_alioth](https://github.com/gotenksIN/device_xiaomi_alioth)@[e255e30a3b...](https://github.com/gotenksIN/device_xiaomi_alioth/commit/e255e30a3bf0e40636e35a5770f9582cc610a1e7)
#### Wednesday 2022-03-09 10:55:14 by Omkar Chandorkar

fuck you xiaomi

Signed-off-by: Omkar Chandorkar <gotenksIN@aosip.dev>

---
## [ksant0s/android_kernel_samsung_universal8895](https://github.com/ksant0s/android_kernel_samsung_universal8895)@[5f4af1623b...](https://github.com/ksant0s/android_kernel_samsung_universal8895/commit/5f4af1623b26b5a996f91a12843a749509b0159b)
#### Wednesday 2022-03-09 11:16:14 by Masahiro Yamada

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
[nc: Omit rpmsg, sdw, fslmc, tbsvc, and typec as they don't exist here
     Add of to avoid backporting two larger patches]
Signed-off-by: Nathan Chancellor <natechancellor@gmail.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [mkingopng/feedback_prize_pytorch](https://github.com/mkingopng/feedback_prize_pytorch)@[3cd8c642de...](https://github.com/mkingopng/feedback_prize_pytorch/commit/3cd8c642de16ca2b00ba085d347477cca7f1e525)
#### Wednesday 2022-03-09 11:44:49 by Michael Kingston

this is weird. The code works in notebook. Doesn't work when transplanted to .py file. I've tried splitting it into functions and execution. I've now got it all in one file. It keeps generating errors around the tez module. This thing has been giving me the shits since i started using it.

I think I'm going to have to default to using jupyter. Don't have time to fuck around with this.

---
## [ProbablyCarl/BoH-Bay-1](https://github.com/ProbablyCarl/BoH-Bay-1)@[fe6e9e9f05...](https://github.com/ProbablyCarl/BoH-Bay-1/commit/fe6e9e9f05778ededd5f354206899b74c12ffc44)
#### Wednesday 2022-03-09 11:50:32 by ShadeAware

Makeshift Weaponry expansion (#1400)

* early work, still doesn't compile, kill me

* changing some notes

* Big updato

* fhghfgdgfd

* fuck

* fuck you

* piece of shit

* Revert "piece of shit"

This reverts commit 207cb44e914315e6cbfcd45c9a801f19c945432a.

* WORK

* ereersgRRG

---
## [SuffolkLITLab/ALKiln](https://github.com/SuffolkLITLab/ALKiln)@[fe728649d3...](https://github.com/SuffolkLITLab/ALKiln/commit/fe728649d3b5a7be2d6cbf4eff90857d63a2986b)
#### Wednesday 2022-03-09 12:28:53 by plocket

Update our package's dependencies for v4 (#503)

I'm thinking this is just going to be for v4. Not bothering with this for v3 unless we absolutely have to since none of the vulnerabilities are severe. My current rationale is that the more work we do to maintain 3, the less work we can do getting v4 ready for release. Ready to hear opinions.

- Close #164, update cucumber to v7
- Prepare for v8 of cucumber because I won't remember it later
- Close #394, update puppeteer
- Update our version of node (and that of our action that we'll run for other people's libs). [Addresses #393 so we can use the suffolk npm org package.]
- Use `npm audit` to fix the remaining vulnerabilities (now 0)
- [Remove package.json as discussed in #489 to align our tests' behaviors with those of our users.]

* Update action.yml node to v17

* Update from cucumber v6 to v7. See details.

See https://github.com/cucumber/cucumber-js/blob/main/docs/migration.md#migrating-to-cucumber-js-7xx

Only use cucumber setDefaultTimeout globally and use a shim that replicates the fix in v8 that lets you do custom timeouts more easily so we can still give enough time for steps that may need more time.

Use all caps for statuses.

Test screenshot step.

Btw, the cucumber test output visually looks a bit different now - when a scenario passes, all the steps pass too.

Sorry about the little comment changes, etc. Tried to remove a lot of those incidental unrelated changes.

* Update puppeteer to latest (13). See details below.

- page.waitFor -> page.waitForTimeout and page.waitForSelector (Got deprication notice. See https://github.com/puppeteer/puppeteer/issues/6214.)
- remove removeEventListener (we'd need to change it to removeListener anyway - v4.0.0 and see https://github.com/puppeteer/puppeteer/blob/main/docs/api.md#eventemitterremovelistenerevent-handler). For now we'll count on page close taking care of it, just in case removing it would prevent multiple-file-downloads.

* Update GitHub worflow node version, tweak changelog item order

* Fix npm audit vulnerabilities and update action.yml cucumber

* Pin the colors lib in action.yml

* Remove package-lock.json #489, use kiln v4 for users, CHANGELOG

* Fix custom timeout, remove duplicate report entry, as per review

---
## [imag00/fondo](https://github.com/imag00/fondo)@[3f32789b4a...](https://github.com/imag00/fondo/commit/3f32789b4a0668b302019e473d7d8a1907bac8dd)
#### Wednesday 2022-03-09 12:32:06 by Ismael Magro

Somebody once told me the world is gonna roll me I ain't the sharpest tool in the shed She was looking kind of dumb with her finger and her thumb In the shape of an "L" on her forehead Well the years start coming and they don't stop coming Fed to the rules and I hit the ground running Didn't make sense not to live for fun Your brain gets smart but your head gets dumb So much to do, so much to see So what's wrong with taking the back streets? You'll never know if you don't go You'll never shine if you don't glow Hey now, you're an all-star, get your game on, go play Hey now, you're a rock star, get the show on, get paid And all that glitters is gold Only shooting stars break the mold It's a cool place and they say it gets colder You're bundled up now, wait 'til you get older But the meteor men beg to differ Judging by the hole in the satellite picture The ice we skate is getting pretty thin The water's getting warm so you might as well swim My world's on fire, how about yours? That's the way I like it and I'll never get bored Hey now, you're an all-star, get your game on, go play Hey now, you're a rock star, get the show on, get paid All that glitters is gold Only shooting stars break the mold Hey now, you're an all-star, get your game on, go play Hey now, you're a rock star, get the show, on get paid And all that glitters is gold Only shooting stars Somebody once asked could I spare some change for gas? I need to get myself away from this place I said, "Yup" what a concept I could use a little fuel myself And we could all use a little change Well, the years start coming and they don't stop coming Fed to the rules and I hit the ground running Didn't make sense not to live for fun Your brain gets smart but your head gets dumb So much to do, so much to see So what's wrong with taking the back streets? You'll never know if you don't go (go!) You'll never shine if you don't glow Hey now, you're an all-star, get your game on, go play Hey now, you're a rock star, get the show on, get paid And all that glitters is gold Only shooting stars break the mold And all that glitters is gold Only shooting stars break the mold

---
## [intona/ethernet-debugger](https://github.com/intona/ethernet-debugger)@[546029dcfb...](https://github.com/intona/ethernet-debugger/commit/546029dcfb3ef40669a8859575a2d6bc268d75a6)
#### Wednesday 2022-03-09 12:40:50 by Vincent Lang

usb_io: fix exit handling and exit freezes

This was quite puzzling, and I even suspected libusb bugs. libusb
seemingly didn't run all transfer completion callbacks when cancelling
transfers. But in the end, it was my own stupidity, and the cause and
solution are astonishingly simple: if ctx->interrupt is set to 1, then
libusb_handle_events_completed() will always exit immediately. I just
assumed it would handle all outstanding events, and then just not wait.
But it basically returns immediately. Since ctx->interrupt was never
unset, no events got handled, and no further transfer callbacks
happened. The workaround hack with the timeouts was even more idiotic
than it seemed, and it "helped" only because killing the event handler
was delayed for a bit, making it less likely that there were still
pending transfers.

Fix this by using the fact that libusb_interrupt_event_handler() does
guarantee that libusb_handle_events() returns at least once. (This was
unclear to me until I read more of the libusb source code. It could have
been that the function had certain races, for example when called before
entering the event handler, and might have required using certain
locks.) This greatly simplifies the logic, and we don't need to mess
with stupid locks and other stuff.

usb_cancel_all() was redundant, because usb_ep_remove() must be called
for all EPs before exiting, which cancels all transfers.

Move the code for waiting for all transfers to finish from usb_thread()
to usb_thread_destroy(), because I think it's easier to understand and
to debug. It's not technically necessary.

And now it's time to complain about libusb. At least the Linux backend
is single-threaded and uses a poll() mainloop. (nose uses a separate
thread for libusb mainly because it would be too tricky to integrate our
own mainloop with libusb's on win32.) Yet libusb has tons of different
mutexes and condition variables and stuff to interact with them - what
for? If your library is single-threaded, it's better to have a simple
API and let the user worry about synchronization. Interacting with the
threaded stuff is not simple. libusb_interrupt_event_handler(), the most
useful function, was under-documented. Extremely tricky to use
mechanisms like libusb_handle_events_completed() get too much focus. The
idea of multiple thread to handle events (not concurrently) seems rather
dumb. Requiring the API user to wait for transfer completion after
cancellation is the main reason for all the complexity in usb_io.c, and
with which all API users have to fight with. (Or they ignore it and you
get unreliable libusb programs.) Completion callbacks are a really bad
choice, because they require the user to implement synchronization (a
backend could still choose to call them from random threads), and it
creates API reentrancy issues. There seem to be implementation bugs too:
event_handler_active (struct libusb_context) is read/written under
different two independent mutexes. OK that's all.

---
## [Archmagnificent/ScienceAndSorcery](https://github.com/Archmagnificent/ScienceAndSorcery)@[d7d2ba0463...](https://github.com/Archmagnificent/ScienceAndSorcery/commit/d7d2ba04636c19b8366cf3e1b6a89b99cf157960)
#### Wednesday 2022-03-09 12:56:39 by DwarfLordDurin

Movement groundwork

also bullshit engine number change and some other shit? brother i do not know

---
## [DroneBetter/ChessPieceVision](https://github.com/DroneBetter/ChessPieceVision)@[9c5caa9566...](https://github.com/DroneBetter/ChessPieceVision/commit/9c5caa95669fc631a72f41a15593052687297610)
#### Wednesday 2022-03-09 13:01:52 by Drone_Better

Add GUI for playing with God

I haven't added Cburnett pieces so currently kings are squares and knights are circles, but moves are highlighted based on whether they're optimal continuations (to win or draw in the fewest moves or lose in the most), sometimes (when you're being checkmated) moving your king away from a knight is green but capturing it is red, because you can't be checkmated either way and drawing can be achieved in fewer moves (assuming cooperation from the opponent (not attempting to maximise the proportion of continuations that lead to winning or accounting for the opponent doing that or anything (drawing optimality isn't important because you draw either way and God doesn't blunder))).
Also, regardless of whether or not you use the GUI mode, it now resets the state to a new random one upon stale/checkmate instead of returning an error if it's God's turn or awaiting an input then returning an error if it's yours. It may be confusing due to God moving and the state resetting instantly and due to eightfold symmetry still making it appear to flip (will be fixed in subsequent commit (sorry)).

---
## [S0M3-DUD3/CyberCodeOnline](https://github.com/S0M3-DUD3/CyberCodeOnline)@[6d5cb134f2...](https://github.com/S0M3-DUD3/CyberCodeOnline/commit/6d5cb134f217d2cfa2a14edfd3a81d4748a74fdc)
#### Wednesday 2022-03-09 13:08:23 by S0M3_DUD3

Updated german commen used curse words

Translations
		"Arschfresse" - Analface
		"Arschlecker" - Anallicker
		"Arschficker" - Analfucker
		"Pimmel" - other word for dick
		"Schwanzlutscher" - dicksucker
		"Kanacke" - curse word for imigrants
		"Fettsack" - "Fat guy"
		"Schlampe" - "Bitch"
		"Mutterficker" - "Motherfucker"
		"Assi" - curse word for jobless
		"Aushilfsnazi" - nazi thing

---
## [9Fork/next.js](https://github.com/9Fork/next.js)@[91146b23a2...](https://github.com/9Fork/next.js/commit/91146b23a21e33d54332a469f30afe6e6156cd65)
#### Wednesday 2022-03-09 13:38:03 by Glenn Gijsberts

Make adjustment to cache config of with-apollo example (#32733)

## Description
This year we implemented the new Apollo config using this example. We recently moved to `getServerSideProps` as well, however, this was giving us some cache problems. The issue was that the cache was older than the actual data that was coming from the server side query. 

Because the `merge` of the cache in `apolloClient.js` is merging the existingCache in the initialState it will overwrite the "fresh" initialState with properties that already exists. This means that if you have something in your cache from previous client render, for example `user` with the value `null`, and you go to a new page and do a new query on the server which returns a value for the `user` field, it will still return `null` because of that `merge` function.

Since this was weird in our opinion, we've changed this in our own environment by always overwriting the existing cache with the new initialState, so that the initialState that is coming from a fresh server side query is overwriting. We thought it was a good idea to reflect this also in this example, because we couldn't think of a reason why the existing cache should overwrite fresh queries.

I've added a reproduction that shows what this is exactly about. I hope my description makes sense, let me know what you think!

## Reproduction of old scenario
Created a reproduction branch here: https://github.com/glenngijsberts/with-apollo-example. Using a different API than in the example, because of https://github.com/vercel/next.js/issues/32731.

1. checkout the example
2. yarn
3. yarn dev
4. visit http://localhost:3000/client-only
5. Hit "Update name". This will run a mutation that will update the cache automatically. Because I use a mocked API, the actual value on the API won't be updated, but this is actually the perfect scenario for the problem because in reality data can already change in the meantime when you're doing a new request.
6. Go to the SSR page
7. This will display two values: one is coming from the server side request (which is the latest data, because no cache is used in `getServerSideProps`) and the other is using the cache, which is outdated at that point, yet it's still returned because the old way of merging the cache was picking the existing cache over the initialState that was coming from the fresh server side query.

## Documentation / Examples

- [x] Make sure the linting passes by running `yarn lint`

---
## [vgstation-coders/vgstation13](https://github.com/vgstation-coders/vgstation13)@[b879dddba0...](https://github.com/vgstation-coders/vgstation13/commit/b879dddba0f6a2afcf72a77f4696f3e9c031ecb5)
#### Wednesday 2022-03-09 14:36:51 by rob

adds sound effects to surgery steps (#31850)

* the everything

* nmb

* ok

* dfdffdfsds

* ssssssssssssssssssssskurfusr

* fuck yoiu damian fuck you!!!!!

* DAMIANNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN

* D

---
## [engine-flutter-autoroll/flutter](https://github.com/engine-flutter-autoroll/flutter)@[99977cea1c...](https://github.com/engine-flutter-autoroll/flutter/commit/99977cea1c4ab14dbd46866df8711d5a91af16f9)
#### Wednesday 2022-03-09 15:03:24 by Pierre-Louis

[Fonts] Update icons (#95007)

* update icons

All existing codepoints are stable, with 2 exceptions `wifi_tethering_error_rounded_sharp` and `wifi_tethering_error_rounded_outlined`.

Add 1028 new icons. Codepoints:
airline_seat_individual_suite_baseline, airline_seat_legroom_reduced_baseline, airline_seat_legroom_normal_baseline, airline_seat_recline_normal_baseline, airline_seat_legroom_extra_baseline, airline_seat_recline_extra_baseline, airline_seat_flat_angled_baseline, align_horizontal_center_baseline, account_balance_wallet_baseline, align_horizontal_right_baseline, arrow_drop_down_circle_baseline, airplanemode_inactive_baseline, align_horizontal_left_baseline, align_vertical_bottom_baseline, align_vertical_center_baseline, admin_panel_settings_baseline, assignment_turned_in_baseline, assistant_navigation_baseline, add_photo_alternate_baseline, airplanemode_active_baseline, assignment_returned_baseline, assistant_direction_baseline, auto_awesome_mosaic_baseline, auto_awesome_motion_baseline, access_time_filled_baseline, accessible_forward_baseline, add_circle_outline_baseline, add_to_home_screen_baseline, align_vertical_top_baseline, arrow_back_ios_new_baseline, arrow_circle_right_baseline, arrow_circle_right_outlined, accessibility_new_baseline, add_shopping_cart_baseline, airline_seat_flat_baseline, arrow_circle_down_baseline, arrow_circle_left_baseline, arrow_circle_left_outlined, arrow_circle_right_rounded, arrow_forward_ios_baseline, assignment_return_baseline, add_location_alt_baseline, airplanemode_off_baseline, app_registration_baseline, app_settings_alt_baseline, arrow_circle_left_rounded, assured_workload_baseline, assured_workload_outlined, account_balance_baseline, airplane_ticket_baseline, airplanemode_on_baseline, airport_shuttle_baseline, alternate_email_baseline, arrow_circle_right_sharp, arrow_circle_up_baseline, arrow_drop_down_baseline, arrow_right_alt_baseline, assignment_late_baseline, assistant_photo_baseline, assured_workload_rounded, auto_fix_normal_baseline, account_circle_baseline, arrow_back_ios_baseline, arrow_circle_left_sharp, arrow_downward_baseline, assignment_ind_baseline, autofps_select_baseline, access_alarms_baseline, accessibility_baseline, add_moderator_baseline, add_to_photos_baseline, airline_stops_baseline, airline_stops_outlined, all_inclusive_baseline, arrow_drop_up_baseline, arrow_forward_baseline, assured_workload_sharp, auto_fix_high_baseline, access_alarm_baseline, account_tree_baseline, add_business_baseline, add_location_baseline, add_reaction_baseline, add_to_drive_baseline, add_to_queue_baseline, airline_stops_rounded, announcement_baseline, app_blocking_baseline, app_shortcut_baseline, app_shortcut_outlined, architecture_baseline, arrow_upward_baseline, aspect_ratio_baseline, attach_email_baseline, attach_money_baseline, auto_awesome_baseline, auto_fix_off_baseline, auto_stories_baseline, access_time_baseline, account_box_baseline, add_a_photo_baseline, add_comment_baseline, add_ic_call_baseline, adf_scanner_baseline, adf_scanner_outlined, agriculture_baseline, amp_stories_baseline, app_shortcut_rounded, apps_outage_baseline, apps_outage_outlined, arrow_right_baseline, attach_file_baseline, attractions_baseline, attribution_baseline, auto_delete_baseline, accessible_baseline, add_circle_baseline, adf_scanner_rounded, airline_stops_sharp, apps_outage_rounded, area_chart_baseline, area_chart_outlined, arrow_back_baseline, arrow_left_baseline, assessment_baseline, assignment_baseline, attachment_baseline, audio_file_baseline, audio_file_outlined, audiotrack_baseline, auto_graph_baseline, add_alarm_baseline, add_alert_baseline, add_chart_baseline, ads_click_baseline, ads_click_outlined, alarm_add_baseline, alarm_off_baseline, all_inbox_baseline, alt_route_baseline, analytics_baseline, animation_baseline, apartment_baseline, app_shortcut_sharp, area_chart_rounded, art_track_baseline, assistant_baseline, audio_file_rounded, autorenew_baseline, ad_units_baseline, add_call_baseline, add_card_baseline, add_card_outlined, add_link_baseline, add_road_baseline, add_task_baseline, addchart_baseline, adf_scanner_sharp, ads_click_rounded, airlines_baseline, airlines_outlined, alarm_on_baseline, approval_baseline, apps_outage_sharp, av_timer_baseline, ac_unit_baseline, add_box_baseline, add_card_rounded, airlines_rounded, airplay_baseline, all_out_baseline, android_baseline, archive_baseline, area_chart_sharp, article_baseline, audio_file_sharp, adjust_baseline, ads_click_sharp, anchor_baseline, add_card_sharp, adobe_baseline, adobe_outlined, airlines_sharp, alarm_baseline, album_baseline, apple_baseline, apple_outlined, adobe_rounded, apple_rounded, apps_baseline, abc_baseline, abc_outlined, adb_baseline, add_baseline, air_baseline, aod_baseline, api_baseline, atm_baseline, abc_rounded, adobe_sharp, apple_sharp, abc_sharp, baby_changing_station_baseline, battery_charging_full_baseline, browser_not_supported_baseline, bluetooth_connected_baseline, bluetooth_searching_baseline, bluetooth_disabled_baseline, branding_watermark_baseline, border_horizontal_baseline, brightness_medium_baseline, batch_prediction_baseline, bookmark_outline_baseline, breakfast_dining_baseline, battery_unknown_baseline, bluetooth_audio_baseline, bluetooth_drive_baseline, bookmark_border_baseline, bookmark_remove_baseline, border_vertical_baseline, brightness_auto_baseline, brightness_high_baseline, browser_updated_baseline, browser_updated_outlined, business_center_baseline, bedroom_parent_baseline, bookmark_added_baseline, brightness_low_baseline, browse_gallery_baseline, browse_gallery_outlined, browser_updated_rounded, bakery_dining_baseline, battery_alert_baseline, battery_saver_baseline, bedroom_child_baseline, block_flipped_baseline, blur_circular_baseline, border_bottom_baseline, browse_gallery_rounded, brunch_dining_baseline, backup_table_baseline, battery_full_baseline, beach_access_baseline, bedroom_baby_baseline, bike_scooter_baseline, bookmark_add_baseline, border_clear_baseline, border_color_baseline, border_inner_baseline, border_outer_baseline, border_right_baseline, border_style_baseline, brightness_5_baseline, brightness_4_baseline, brightness_1_baseline, brightness_7_baseline, brightness_6_baseline, brightness_3_baseline, brightness_2_baseline, broken_image_baseline, browser_updated_sharp, bubble_chart_baseline, build_circle_baseline, battery_std_baseline, bedtime_off_baseline, bedtime_off_outlined, blur_linear_baseline, book_online_baseline, border_left_baseline, browse_gallery_sharp, bedtime_off_rounded, border_all_baseline, border_top_baseline, bug_report_baseline, burst_mode_baseline, back_hand_baseline, back_hand_outlined, backspace_baseline, bar_chart_baseline, bloodtype_baseline, bluetooth_baseline, bookmarks_baseline, bus_alert_baseline, back_hand_rounded, backpack_baseline, bathroom_baseline, bedtime_off_sharp, beenhere_baseline, blur_off_baseline, bookmark_baseline, bungalow_baseline, business_baseline, balance_baseline, balance_outlined, balcony_baseline, bathtub_baseline, bedtime_baseline, biotech_baseline, blender_baseline, blur_on_baseline, back_hand_sharp, backup_baseline, balance_rounded, ballot_baseline, badge_baseline, bento_baseline, block_baseline, brush_baseline, build_baseline, balance_sharp, bolt_baseline, book_baseline, bed_baseline, boy_baseline, boy_outlined, boy_rounded, boy_sharp, check_box_outline_blank_baseline, closed_caption_disabled_baseline, connect_without_contact_baseline, control_point_duplicate_baseline, call_missed_outgoing_baseline, cancel_schedule_send_baseline, check_circle_outline_baseline, circle_notifications_baseline, collections_bookmark_baseline, content_paste_search_baseline, content_paste_search_outlined, calendar_view_month_baseline, cancel_presentation_baseline, center_focus_strong_baseline, chat_bubble_outline_baseline, compass_calibration_baseline, confirmation_number_baseline, connecting_airports_baseline, connecting_airports_outlined, content_paste_search_rounded, calendar_view_week_baseline, cast_for_education_baseline, chrome_reader_mode_baseline, closed_caption_off_baseline, connecting_airports_rounded, calendar_view_day_baseline, candlestick_chart_baseline, candlestick_chart_outlined, center_focus_weak_baseline, cleaning_services_baseline, comments_disabled_baseline, comments_disabled_outlined, content_paste_off_baseline, content_paste_search_sharp, create_new_folder_baseline, currency_exchange_baseline, currency_exchange_outlined, candlestick_chart_rounded, catching_pokemon_baseline, charging_station_baseline, close_fullscreen_baseline, comments_disabled_rounded, confirmation_num_baseline, connecting_airports_sharp, content_paste_go_baseline, content_paste_go_outlined, currency_bitcoin_baseline, currency_bitcoin_outlined, currency_exchange_rounded, card_membership_baseline, contact_support_baseline, content_paste_go_rounded, credit_card_off_baseline, currency_bitcoin_rounded, calendar_month_baseline, calendar_month_outlined, calendar_today_baseline, call_to_action_baseline, camera_enhance_baseline, camera_outdoor_baseline, candlestick_chart_sharp, cast_connected_baseline, change_history_baseline, child_friendly_baseline, closed_caption_baseline, cloud_download_baseline, cloudy_snowing_baseline, comments_disabled_sharp, compare_arrows_baseline, control_camera_baseline, corporate_fare_baseline, crop_landscape_baseline, currency_exchange_sharp, currency_franc_baseline, currency_franc_outlined, currency_pound_baseline, currency_pound_outlined, currency_ruble_baseline, currency_ruble_outlined, currency_rupee_baseline, currency_rupee_outlined, calendar_month_rounded, call_received_baseline, camera_indoor_baseline, card_giftcard_baseline, change_circle_baseline, checklist_rtl_baseline, chevron_right_baseline, contact_phone_baseline, content_paste_baseline, content_paste_go_sharp, control_point_baseline, crop_original_baseline, crop_portrait_baseline, currency_bitcoin_sharp, currency_franc_rounded, currency_lira_baseline, currency_lira_outlined, currency_pound_rounded, currency_ruble_rounded, currency_rupee_rounded, currency_yuan_baseline, currency_yuan_outlined, camera_front_baseline, cameraswitch_baseline, check_circle_baseline, chevron_left_baseline, cloud_circle_baseline, cloud_upload_baseline, coffee_maker_baseline, comment_bank_baseline, connected_tv_baseline, construction_baseline, contact_mail_baseline, contact_page_baseline, content_copy_baseline, credit_score_baseline, cruelty_free_baseline, cruelty_free_outlined, currency_lira_rounded, currency_yen_baseline, currency_yen_outlined, currency_yuan_rounded, calendar_month_sharp, call_missed_baseline, camera_rear_baseline, camera_roll_baseline, card_travel_baseline, celebration_baseline, chat_bubble_baseline, clean_hands_baseline, cloud_queue_baseline, collections_baseline, contactless_baseline, content_cut_baseline, coronavirus_baseline, countertops_baseline, credit_card_baseline, crop_rotate_baseline, crop_square_baseline, cruelty_free_rounded, currency_franc_sharp, currency_pound_sharp, currency_ruble_sharp, currency_rupee_sharp, currency_yen_rounded, call_merge_baseline, call_split_baseline, camera_alt_baseline, car_rental_baseline, car_repair_baseline, cell_tower_baseline, cell_tower_outlined, child_care_baseline, cloud_done_baseline, cloud_sync_baseline, cloud_sync_outlined, co_present_baseline, co_present_outlined, color_lens_baseline, currency_lira_sharp, currency_yuan_sharp, calculate_baseline, call_made_baseline, carpenter_baseline, cell_tower_rounded, cell_wifi_baseline, chair_alt_baseline, check_box_baseline, checklist_baseline, checkroom_baseline, clear_all_baseline, cloud_off_baseline, cloud_sync_rounded, co_present_rounded, copyright_baseline, crop_16_9_baseline, crop_free_baseline, cruelty_free_sharp, currency_yen_sharp, call_end_baseline, campaign_baseline, category_baseline, code_off_baseline, colorize_baseline, compress_baseline, computer_baseline, contacts_baseline, contrast_baseline, contrast_outlined, copy_all_baseline, crop_din_baseline, crop_5_4_baseline, crop_7_5_baseline, crop_3_2_baseline, cell_tower_sharp, cloud_sync_sharp, co_present_sharp, comment_baseline, commute_baseline, compare_baseline, compost_baseline, compost_outlined, contrast_rounded, cottage_baseline, cached_baseline, camera_baseline, cancel_baseline, casino_baseline, castle_baseline, castle_outlined, chalet_baseline, church_baseline, church_outlined, circle_baseline, coffee_baseline, commit_baseline, commit_outlined, compost_rounded, cookie_baseline, cookie_outlined, create_baseline, cabin_baseline, cable_baseline, cases_baseline, castle_rounded, chair_baseline, check_baseline, church_rounded, class_baseline, clear_baseline, close_baseline, cloud_baseline, commit_rounded, contrast_sharp, cookie_rounded, cake_baseline, call_baseline, cast_baseline, chat_baseline, code_baseline, compost_sharp, copy_baseline, crib_baseline, crop_baseline, castle_sharp, church_sharp, co2_baseline, co2_outlined, commit_sharp, cookie_sharp, css_baseline, css_outlined, cut_baseline, co2_rounded, css_rounded, co2_sharp, css_sharp, do_not_disturb_on_total_silence_baseline, directions_railway_filled_baseline, directions_transit_filled_baseline, drive_file_rename_outline_baseline, directions_subway_filled_baseline, desktop_access_disabled_baseline, drive_file_move_outline_baseline, directions_boat_filled_baseline, directions_bus_filled_baseline, directions_car_filled_baseline, download_for_offline_baseline, dashboard_customize_baseline, developer_board_off_baseline, disabled_by_default_baseline, domain_verification_baseline, drive_file_move_rtl_baseline, drive_file_move_rtl_outlined, drive_folder_upload_baseline, directions_railway_baseline, directions_transit_baseline, do_not_disturb_alt_baseline, do_not_disturb_off_baseline, drive_file_move_rtl_rounded, data_thresholding_baseline, data_thresholding_outlined, device_thermostat_baseline, directions_subway_baseline, do_not_disturb_on_baseline, data_exploration_baseline, data_exploration_outlined, data_thresholding_rounded, directions_ferry_baseline, directions_train_baseline, disabled_visible_baseline, disabled_visible_outlined, display_settings_baseline, display_settings_outlined, dnd_forwardslash_baseline, document_scanner_baseline, drive_file_move_rtl_sharp, data_exploration_rounded, delivery_dining_baseline, departure_board_baseline, design_services_baseline, desktop_windows_baseline, developer_board_baseline, directions_bike_baseline, directions_boat_baseline, directions_walk_baseline, disabled_visible_rounded, display_settings_rounded, domain_disabled_baseline, downhill_skiing_baseline, drive_file_move_baseline, data_saver_off_baseline, data_thresholding_sharp, delete_forever_baseline, delete_outline_baseline, density_medium_baseline, density_medium_outlined, developer_mode_baseline, device_unknown_baseline, directions_bus_baseline, directions_car_baseline, directions_off_baseline, directions_run_baseline, do_disturb_alt_baseline, do_disturb_off_baseline, do_not_disturb_baseline, drag_indicator_baseline, data_exploration_sharp, data_saver_on_baseline, density_large_baseline, density_large_outlined, density_medium_rounded, density_small_baseline, density_small_outlined, devices_other_baseline, dinner_dining_baseline, disabled_visible_sharp, display_settings_sharp, do_disturb_on_baseline, download_done_baseline, delete_sweep_baseline, density_large_rounded, density_small_rounded, do_not_touch_baseline, done_outline_baseline, door_sliding_baseline, double_arrow_baseline, dry_cleaning_baseline, dynamic_feed_baseline, dynamic_form_baseline, data_object_baseline, data_object_outlined, density_medium_sharp, description_baseline, desktop_mac_baseline, do_not_step_baseline, donut_large_baseline, donut_small_baseline, downloading_baseline, drag_handle_baseline, data_array_baseline, data_array_outlined, data_object_rounded, data_usage_baseline, date_range_baseline, density_large_sharp, density_small_sharp, device_hub_baseline, dialer_sip_baseline, difference_baseline, difference_outlined, directions_baseline, dirty_lens_baseline, do_disturb_baseline, domain_add_baseline, domain_add_outlined, door_front_baseline, dangerous_baseline, dark_mode_baseline, dashboard_baseline, data_array_rounded, difference_rounded, disc_full_baseline, domain_add_rounded, door_back_baseline, drive_eta_baseline, data_object_sharp, deselect_baseline, deselect_outlined, discount_baseline, discount_outlined, done_all_baseline, doorbell_baseline, download_baseline, data_array_sharp, deselect_rounded, details_baseline, devices_baseline, dialpad_baseline, diamond_baseline, diamond_outlined, difference_sharp, discord_baseline, discord_outlined, discount_rounded, domain_add_sharp, deblur_baseline, deblur_outlined, dehaze_baseline, delete_baseline, diamond_rounded, dining_baseline, discord_rounded, domain_baseline, drafts_baseline, deblur_rounded, deselect_sharp, discount_sharp, deck_baseline, diamond_sharp, discord_sharp, dock_baseline, done_baseline, draw_baseline, draw_outlined, deblur_sharp, dns_baseline, draw_rounded, dry_baseline, duo_baseline, dvr_baseline, draw_sharp, 4g_plus_mobiledata_baseline, 4g_mobiledata_baseline, 4k_plus_baseline, 4mp_baseline, 4k_baseline, 5k_plus_baseline, 5mp_baseline, 5g_baseline, 5k_baseline, 8k_plus_baseline, 8mp_baseline, 8k_baseline, 1x_mobiledata_baseline, 1k_plus_baseline, 18mp_baseline, 15mp_baseline, 14mp_baseline, 19mp_baseline, 11mp_baseline, 17mp_baseline, 16mp_baseline, 13mp_baseline, 12mp_baseline, 10mp_baseline, 123_baseline, 123_outlined, 10k_baseline, 123_rounded, 1k_baseline, 123_sharp, enhance_photo_translate_baseline, emoji_transportation_baseline, electrical_services_baseline, emoji_food_beverage_baseline, enhanced_encryption_baseline, edit_notifications_baseline, expand_circle_down_baseline, expand_circle_down_outlined, edit_location_alt_baseline, electric_rickshaw_baseline, escalator_warning_baseline, expand_circle_down_rounded, electric_scooter_baseline, exposure_minus_1_baseline, exposure_minus_2_baseline, earbuds_battery_baseline, edgesensor_high_baseline, edit_attributes_baseline, event_available_baseline, expand_circle_down_sharp, exposure_plus_1_baseline, exposure_plus_2_baseline, edgesensor_low_baseline, electric_moped_baseline, emoji_emotions_baseline, exposure_neg_1_baseline, exposure_neg_2_baseline, edit_calendar_baseline, edit_calendar_outlined, edit_location_baseline, elderly_woman_baseline, elderly_woman_outlined, electric_bike_baseline, emoji_objects_baseline, emoji_symbols_baseline, error_outline_baseline, exposure_zero_baseline, extension_off_baseline, e_mobiledata_baseline, edit_calendar_rounded, elderly_woman_rounded, electric_car_baseline, emoji_events_baseline, emoji_nature_baseline, emoji_people_baseline, event_repeat_baseline, event_repeat_outlined, emoji_flags_baseline, engineering_baseline, euro_symbol_baseline, event_repeat_rounded, exit_to_app_baseline, expand_less_baseline, expand_more_baseline, explore_off_baseline, edit_calendar_sharp, elderly_woman_sharp, ev_station_baseline, event_busy_baseline, event_note_baseline, event_seat_baseline, edit_note_baseline, edit_note_outlined, edit_road_baseline, emergency_baseline, emergency_outlined, equalizer_baseline, escalator_baseline, event_repeat_sharp, extension_baseline, edit_note_rounded, edit_off_baseline, elevator_baseline, emergency_rounded, explicit_baseline, exposure_baseline, earbuds_baseline, egg_alt_baseline, egg_alt_outlined, elderly_baseline, explore_baseline, edit_note_sharp, egg_alt_rounded, emergency_sharp, expand_baseline, eject_baseline, email_baseline, error_baseline, event_baseline, east_baseline, edit_baseline, egg_alt_sharp, euro_baseline, eco_baseline, egg_baseline, egg_outlined, egg_rounded, egg_sharp, 2k_plus_baseline, 24mp_baseline, 21mp_baseline, 23mp_baseline, 22mp_baseline, 20mp_baseline, 2mp_baseline, 2k_baseline, 3g_mobiledata_baseline, 30fps_select_baseline, 3d_rotation_baseline, 3k_plus_baseline, 30fps_baseline, 360_baseline, 3mp_baseline, 3k_baseline, 3p_baseline, 60fps_select_baseline, 6_ft_apart_baseline, 6k_plus_baseline, 60fps_baseline, 6mp_baseline, 6k_baseline, 7k_plus_baseline, 7mp_baseline, 7k_baseline, 9k_plus_baseline, 9mp_baseline, 9k_baseline, format_textdirection_l_to_r_baseline, format_textdirection_r_to_l_baseline, format_list_numbered_rtl_baseline, face_retouching_natural_baseline, format_indent_decrease_baseline, format_indent_increase_baseline, format_align_justify_baseline, format_list_bulleted_baseline, format_list_numbered_baseline, format_strikethrough_baseline, face_retouching_off_baseline, fiber_manual_record_baseline, filter_center_focus_baseline, flip_camera_android_baseline, format_align_center_baseline, format_line_spacing_baseline, featured_play_list_baseline, fiber_smart_record_baseline, file_download_done_baseline, format_align_right_baseline, format_color_reset_baseline, file_download_off_baseline, filter_tilt_shift_baseline, fire_extinguisher_baseline, font_download_off_baseline, format_align_left_baseline, format_color_fill_baseline, format_color_text_baseline, format_underlined_baseline, free_cancellation_baseline, free_cancellation_outlined, favorite_outline_baseline, follow_the_signs_baseline, format_underline_baseline, forward_to_inbox_baseline, free_cancellation_rounded, family_restroom_baseline, favorite_border_baseline, filter_list_alt_baseline, filter_list_off_baseline, filter_list_off_outlined, flip_camera_ios_baseline, format_overline_baseline, format_overline_outlined, fullscreen_exit_baseline, featured_video_baseline, filter_alt_off_baseline, filter_alt_off_outlined, filter_b_and_w_baseline, filter_list_off_rounded, filter_vintage_baseline, fitness_center_baseline, flashlight_off_baseline, flight_takeoff_baseline, folder_special_baseline, format_overline_rounded, free_breakfast_baseline, free_cancellation_sharp, file_download_baseline, filter_alt_off_rounded, filter_9_plus_baseline, filter_frames_baseline, flashlight_on_baseline, flip_to_front_baseline, folder_delete_baseline, folder_delete_outlined, folder_shared_baseline, font_download_baseline, format_italic_baseline, format_shapes_baseline, fast_forward_baseline, file_present_baseline, filter_drama_baseline, filter_list_off_sharp, find_in_page_baseline, find_replace_baseline, fire_hydrant_baseline, flight_class_baseline, flight_class_outlined, flip_to_back_baseline, flutter_dash_baseline, folder_delete_rounded, format_clear_baseline, format_overline_sharp, format_paint_baseline, format_quote_baseline, fast_rewind_baseline, file_upload_baseline, filter_alt_off_sharp, filter_list_baseline, filter_none_baseline, fingerprint_baseline, flag_circle_baseline, flag_circle_outlined, flight_class_rounded, flight_land_baseline, flourescent_baseline, folder_copy_baseline, folder_copy_outlined, folder_open_baseline, format_bold_baseline, format_size_baseline, fact_check_baseline, filter_alt_baseline, filter_hdr_baseline, first_page_baseline, fit_screen_baseline, flag_circle_rounded, flash_auto_baseline, folder_copy_rounded, folder_delete_sharp, folder_off_baseline, folder_off_outlined, folder_zip_baseline, folder_zip_outlined, fork_right_baseline, fork_right_outlined, forward_10_baseline, forward_30_baseline, foundation_baseline, front_hand_baseline, front_hand_outlined, fullscreen_baseline, fiber_dvr_baseline, fiber_new_baseline, fiber_pin_baseline, file_copy_baseline, file_open_baseline, file_open_outlined, fireplace_baseline, flash_off_baseline, flight_class_sharp, folder_off_rounded, folder_zip_rounded, food_bank_baseline, fork_left_baseline, fork_left_outlined, fork_right_rounded, forward_5_baseline, front_hand_rounded, functions_baseline, facebook_baseline, fastfood_baseline, favorite_baseline, feedback_baseline, festival_baseline, file_open_rounded, filter_8_baseline, filter_5_baseline, filter_4_baseline, filter_9_baseline, filter_1_baseline, filter_7_baseline, filter_6_baseline, filter_3_baseline, filter_2_baseline, flag_circle_sharp, flash_on_baseline, flatware_baseline, fmd_good_baseline, folder_copy_sharp, fork_left_rounded, factory_baseline, factory_outlined, fmd_bad_baseline, folder_off_sharp, folder_zip_sharp, fork_right_sharp, forward_baseline, front_hand_sharp, factory_rounded, female_baseline, file_open_sharp, filter_baseline, fitbit_baseline, fitbit_outlined, flight_baseline, folder_baseline, forest_baseline, forest_outlined, fork_left_sharp, fence_baseline, fitbit_rounded, flaky_baseline, flare_baseline, foggy_baseline, forest_rounded, forum_baseline, face_baseline, factory_sharp, feed_baseline, flag_baseline, flip_baseline, fort_baseline, fort_outlined, fax_baseline, fax_outlined, fitbit_sharp, forest_sharp, fort_rounded, fax_rounded, fort_sharp, fax_sharp, generating_tokens_baseline, generating_tokens_outlined, generating_tokens_rounded, grid_goldenratio_baseline, generating_tokens_sharp, gps_not_fixed_baseline, g_mobiledata_baseline, group_remove_baseline, group_remove_outlined, g_translate_baseline, golf_course_baseline, group_remove_rounded, graphic_eq_baseline, group_work_baseline, gpp_maybe_baseline, gps_fixed_baseline, grid_view_baseline, group_add_baseline, group_off_baseline, group_off_outlined, group_remove_sharp, gpp_good_baseline, gradient_baseline, grid_4x4_baseline, grid_3x3_baseline, grid_off_baseline, group_off_rounded, gamepad_baseline, gesture_baseline, get_app_baseline, gif_box_baseline, gif_box_outlined, gpp_bad_baseline, gps_off_baseline, grading_baseline, grid_on_baseline, garage_baseline, gif_box_rounded, group_off_sharp, groups_baseline, games_baseline, gavel_baseline, grade_baseline, grain_baseline, grass_baseline, group_baseline, gif_box_sharp, girl_baseline, girl_outlined, gite_baseline, gif_baseline, girl_rounded, girl_sharp, horizontal_distribute_baseline, hdr_enhanced_select_baseline, home_repair_service_baseline, headphones_battery_baseline, history_toggle_off_baseline, hourglass_disabled_baseline, h_plus_mobiledata_baseline, health_and_safety_baseline, hearing_disabled_baseline, highlight_remove_baseline, horizontal_split_baseline, hourglass_bottom_baseline, hdr_auto_select_baseline, holiday_village_baseline, horizontal_rule_baseline, hourglass_empty_baseline, hdr_off_select_baseline, hourglass_full_baseline, hdr_on_select_baseline, highlight_alt_baseline, highlight_off_baseline, hourglass_top_baseline, h_mobiledata_baseline, heart_broken_baseline, heart_broken_outlined, help_outline_baseline, high_quality_baseline, house_siding_baseline, headset_mic_baseline, headset_off_baseline, heart_broken_rounded, help_center_baseline, hide_source_baseline, history_edu_baseline, home_filled_baseline, hotel_class_baseline, hotel_class_outlined, how_to_vote_baseline, hdr_strong_baseline, headphones_baseline, hide_image_baseline, hotel_class_rounded, how_to_reg_baseline, handshake_baseline, handshake_outlined, heart_broken_sharp, highlight_baseline, home_mini_baseline, home_work_baseline, houseboat_baseline, handshake_rounded, handyman_baseline, hardware_baseline, hdr_auto_baseline, hdr_plus_baseline, hdr_weak_baseline, home_max_baseline, hotel_class_sharp, hdr_off_baseline, headset_baseline, healing_baseline, hearing_baseline, hexagon_baseline, hexagon_outlined, history_baseline, hls_off_baseline, hls_off_outlined, hot_tub_baseline, handshake_sharp, hdr_on_baseline, height_baseline, hexagon_rounded, hiking_baseline, hls_off_rounded, hotel_baseline, house_baseline, https_baseline, hail_baseline, help_baseline, hevc_baseline, hexagon_sharp, hive_baseline, hive_outlined, hls_off_sharp, home_baseline, html_baseline, html_outlined, http_baseline, hvac_baseline, hive_rounded, hls_baseline, hls_outlined, html_rounded, hub_baseline, hub_outlined, hd_baseline, hls_rounded, hub_rounded, hive_sharp, html_sharp, hls_sharp, hub_sharp, keyboard_double_arrow_right_baseline, keyboard_double_arrow_right_outlined, keyboard_double_arrow_down_baseline, keyboard_double_arrow_down_outlined, keyboard_double_arrow_left_baseline, keyboard_double_arrow_left_outlined, keyboard_double_arrow_right_rounded, keyboard_double_arrow_down_rounded, keyboard_double_arrow_left_rounded, keyboard_double_arrow_right_sharp, keyboard_double_arrow_up_baseline, keyboard_double_arrow_up_outlined, keyboard_double_arrow_down_sharp, keyboard_double_arrow_left_sharp, keyboard_double_arrow_up_rounded, keyboard_double_arrow_up_sharp, keyboard_arrow_right_baseline, keyboard_command_key_baseline, keyboard_command_key_outlined, keyboard_control_key_baseline, keyboard_control_key_outlined, keyboard_arrow_down_baseline, keyboard_arrow_left_baseline, keyboard_command_key_rounded, keyboard_control_key_rounded, keyboard_option_key_baseline, keyboard_option_key_outlined, keyboard_backspace_baseline, keyboard_option_key_rounded, keyboard_arrow_up_baseline, keyboard_capslock_baseline, keyboard_command_key_sharp, keyboard_control_key_sharp, keyboard_control_baseline, keyboard_option_key_sharp, keyboard_return_baseline, keyboard_voice_baseline, keyboard_hide_baseline, kebab_dining_baseline, kebab_dining_outlined, keyboard_alt_baseline, keyboard_tab_baseline, kebab_dining_rounded, kitesurfing_baseline, kebab_dining_sharp, kayaking_baseline, keyboard_baseline, king_bed_baseline, key_off_baseline, key_off_outlined, kitchen_baseline, key_off_rounded, key_off_sharp, key_baseline, key_outlined, key_rounded, key_sharp, label_important_outline_baseline, local_convenience_store_baseline, local_fire_department_baseline, local_laundry_service_baseline, local_grocery_store_baseline, lte_plus_mobiledata_baseline, leave_bags_at_home_baseline, location_searching_baseline, laptop_chromebook_baseline, library_add_check_baseline, lightbulb_outline_baseline, local_gas_station_baseline, local_post_office_baseline, location_disabled_baseline, local_attraction_baseline, local_print_shop_baseline, local_restaurant_baseline, location_history_baseline, label_important_baseline, local_printshop_baseline, laptop_windows_baseline, local_activity_baseline, local_car_wash_baseline, local_hospital_baseline, local_pharmacy_baseline, local_shipping_baseline, lte_mobiledata_baseline, label_outline_baseline, legend_toggle_baseline, library_books_baseline, library_music_baseline, linked_camera_baseline, local_airport_baseline, local_florist_baseline, local_library_baseline, local_parking_baseline, location_city_baseline, layers_clear_baseline, linear_scale_baseline, local_dining_baseline, local_movies_baseline, local_police_baseline, location_off_baseline, location_pin_baseline, lock_outline_baseline, low_priority_baseline, lunch_dining_baseline, leaderboard_baseline, leak_remove_baseline, library_add_baseline, line_weight_baseline, local_drink_baseline, local_hotel_baseline, local_offer_baseline, local_phone_baseline, local_pizza_baseline, location_on_baseline, laptop_mac_baseline, light_mode_baseline, line_style_baseline, local_cafe_baseline, local_mall_baseline, local_play_baseline, local_taxi_baseline, lock_clock_baseline, lock_reset_baseline, lock_reset_outlined, label_off_baseline, landscape_baseline, last_page_baseline, lens_blur_baseline, lightbulb_baseline, line_axis_baseline, line_axis_outlined, live_help_baseline, local_atm_baseline, local_bar_baseline, local_see_baseline, lock_open_baseline, lock_reset_rounded, looks_one_baseline, looks_two_baseline, language_baseline, leak_add_baseline, line_axis_rounded, link_off_baseline, list_alt_baseline, logo_dev_baseline, logo_dev_outlined, live_tv_baseline, lock_reset_sharp, logo_dev_rounded, looks_5_baseline, looks_4_baseline, looks_6_baseline, looks_3_baseline, loyalty_baseline, luggage_baseline, laptop_baseline, launch_baseline, layers_baseline, line_axis_sharp, liquor_baseline, living_baseline, logout_baseline, label_baseline, light_baseline, login_baseline, logo_dev_sharp, looks_baseline, loupe_baseline, lens_baseline, link_baseline, list_baseline, lock_baseline, loop_baseline, lan_baseline, lan_outlined, lan_rounded, lan_sharp, integration_instructions_baseline, indeterminate_check_box_baseline, insert_chart_outlined_baseline, image_not_supported_baseline, image_aspect_ratio_baseline, imagesearch_roller_baseline, important_devices_baseline, incomplete_circle_baseline, incomplete_circle_outlined, insert_drive_file_baseline, insert_invitation_baseline, insert_page_break_baseline, insert_page_break_outlined, invert_colors_off_baseline, incomplete_circle_rounded, insert_page_break_rounded, interpreter_mode_baseline, interpreter_mode_outlined, invert_colors_on_baseline, import_contacts_baseline, insert_emoticon_baseline, install_desktop_baseline, install_desktop_outlined, interpreter_mode_rounded, incomplete_circle_sharp, insert_comment_baseline, insert_page_break_sharp, install_desktop_rounded, install_mobile_baseline, install_mobile_outlined, import_export_baseline, install_mobile_rounded, interpreter_mode_sharp, invert_colors_baseline, image_search_baseline, info_outline_baseline, insert_chart_baseline, insert_photo_baseline, install_desktop_sharp, ice_skating_baseline, insert_link_baseline, install_mobile_sharp, inventory_2_baseline, interests_baseline, interests_outlined, inventory_baseline, ios_share_baseline, icecream_baseline, insights_baseline, interests_rounded, interests_sharp, image_baseline, inbox_baseline, input_baseline, info_baseline, iron_baseline, iso_baseline, javascript_baseline, javascript_outlined, join_inner_baseline, join_inner_outlined, join_right_baseline, join_right_outlined, javascript_rounded, join_full_baseline, join_full_outlined, join_inner_rounded, join_left_baseline, join_left_outlined, join_right_rounded, join_full_rounded, join_left_rounded, javascript_sharp, join_inner_sharp, join_right_sharp, join_full_sharp, join_left_sharp, online_prediction_baseline, open_in_browser_baseline, open_in_new_off_baseline, ondemand_video_baseline, offline_share_baseline, outdoor_grill_baseline, outgoing_mail_baseline, outlined_flag_baseline, offline_bolt_baseline, open_in_full_baseline, other_houses_baseline, offline_pin_baseline, open_in_new_baseline, open_with_baseline, outbound_baseline, opacity_baseline, outbond_baseline, outbox_baseline, outlet_baseline, output_baseline, output_outlined, output_rounded, output_sharp, no_encryption_gmailerrorred_baseline, notification_important_baseline, notifications_active_baseline, notifications_paused_baseline, not_listed_location_baseline, notifications_none_baseline, notifications_off_baseline, near_me_disabled_baseline, nightlight_round_baseline, notification_add_baseline, notifications_on_baseline, navigate_before_baseline, no_meals_ouline_baseline, no_meeting_room_baseline, network_locked_baseline, no_photography_baseline, nordic_walking_baseline, not_accessible_baseline, not_interested_baseline, nature_people_baseline, navigate_next_baseline, network_check_baseline, night_shelter_baseline, no_encryption_baseline, notifications_baseline, now_wallpaper_baseline, nearby_error_baseline, network_cell_baseline, network_ping_baseline, network_ping_outlined, network_wifi_baseline, new_releases_baseline, network_ping_rounded, nights_stay_baseline, no_accounts_baseline, no_backpack_baseline, no_stroller_baseline, no_transfer_baseline, not_started_baseline, now_widgets_baseline, navigation_baseline, nearby_off_baseline, nightlight_baseline, no_luggage_baseline, north_east_baseline, north_west_baseline, network_ping_sharp, new_label_baseline, newspaper_baseline, newspaper_outlined, next_plan_baseline, next_week_baseline, nightlife_baseline, no_drinks_baseline, newspaper_rounded, no_flash_baseline, no_meals_baseline, note_add_baseline, note_alt_baseline, near_me_baseline, no_cell_baseline, no_food_baseline, numbers_baseline, numbers_outlined, nature_baseline, newspaper_sharp, no_sim_baseline, numbers_rounded, north_baseline, notes_baseline, note_baseline, numbers_sharp, nat_baseline, nfc_baseline, miscellaneous_services_baseline, mark_unread_chat_alt_baseline, mark_unread_chat_alt_outlined, motion_photos_paused_baseline, mark_unread_chat_alt_rounded, media_bluetooth_off_baseline, mobile_screen_share_baseline, motion_photos_pause_baseline, markunread_mailbox_baseline, media_bluetooth_on_baseline, motion_photos_auto_baseline, mark_email_unread_baseline, mark_unread_chat_alt_sharp, medication_liquid_baseline, medication_liquid_outlined, messenger_outline_baseline, missed_video_call_baseline, mode_edit_outline_baseline, monochrome_photos_baseline, motion_photos_off_baseline, mark_chat_unread_baseline, medical_services_baseline, medication_liquid_rounded, mic_external_off_baseline, motion_photos_on_baseline, multitrack_audio_baseline, my_library_books_baseline, my_library_music_baseline, manage_accounts_baseline, mark_email_read_baseline, mic_external_on_baseline, mobile_friendly_baseline, monetization_on_baseline, money_off_csred_baseline, multiline_chart_baseline, maps_home_work_baseline, mark_as_unread_baseline, mark_chat_read_baseline, medication_liquid_sharp, mobiledata_off_baseline, mode_of_travel_baseline, mode_of_travel_outlined, model_training_baseline, monitor_weight_baseline, movie_creation_baseline, my_library_add_baseline, manage_search_baseline, military_tech_baseline, mode_of_travel_rounded, monitor_heart_baseline, monitor_heart_outlined, move_to_inbox_baseline, multiple_stop_baseline, mail_outline_baseline, meeting_room_baseline, mode_comment_baseline, mode_standby_baseline, monitor_heart_rounded, movie_filter_baseline, mode_of_travel_sharp, music_video_baseline, my_location_baseline, markunread_baseline, medication_baseline, merge_type_baseline, mobile_off_baseline, mode_night_baseline, monitor_heart_sharp, more_horiz_baseline, motorcycle_baseline, music_note_baseline, mediation_baseline, menu_book_baseline, menu_open_baseline, messenger_baseline, microwave_baseline, mode_edit_baseline, money_off_baseline, more_time_baseline, more_vert_baseline, move_down_baseline, move_down_outlined, music_off_baseline, maps_ugc_baseline, maximize_baseline, mic_none_baseline, minimize_baseline, mood_bad_baseline, move_down_rounded, message_baseline, mic_off_baseline, monitor_baseline, move_up_baseline, move_up_outlined, margin_baseline, memory_baseline, mosque_baseline, mosque_outlined, move_down_sharp, move_up_rounded, moving_baseline, museum_baseline, masks_baseline, merge_baseline, merge_outlined, money_baseline, moped_baseline, mosque_rounded, mouse_baseline, movie_baseline, mail_baseline, male_baseline, menu_baseline, merge_rounded, mode_baseline, mood_baseline, more_baseline, move_up_sharp, man_baseline, man_outlined, map_baseline, mic_baseline, mms_baseline, mosque_sharp, man_rounded, merge_sharp, mp_baseline, man_sharp, panorama_photosphere_select_baseline, panorama_horizontal_select_baseline, panorama_wide_angle_select_baseline, production_quantity_limits_baseline, playlist_add_check_circle_baseline, playlist_add_check_circle_outlined, panorama_vertical_select_baseline, photo_size_select_actual_baseline, playlist_add_check_circle_rounded, perm_device_information_baseline, phone_bluetooth_speaker_baseline, photo_size_select_large_baseline, photo_size_select_small_baseline, precision_manufacturing_baseline, picture_in_picture_alt_baseline, playlist_add_check_circle_sharp, published_with_changes_baseline, perm_contact_calendar_baseline, panorama_photosphere_baseline, pause_circle_outline_baseline, private_connectivity_baseline, private_connectivity_outlined, panorama_horizontal_baseline, panorama_wide_angle_baseline, pause_circle_filled_baseline, person_add_disabled_baseline, person_remove_alt_1_baseline, pest_control_rodent_baseline, play_circle_outline_baseline, playlist_add_circle_baseline, playlist_add_circle_outlined, private_connectivity_rounded, pause_presentation_baseline, photo_camera_front_baseline, picture_in_picture_baseline, play_circle_filled_baseline, playlist_add_check_baseline, playlist_add_circle_rounded, power_settings_new_baseline, panorama_fish_eye_baseline, panorama_vertical_baseline, perm_data_setting_baseline, person_pin_circle_baseline, photo_camera_back_baseline, pie_chart_outline_baseline, pivot_table_chart_baseline, portable_wifi_off_baseline, private_connectivity_sharp, panorama_fisheye_baseline, perm_contact_cal_baseline, perm_device_info_baseline, person_add_alt_1_baseline, play_circle_fill_baseline, playlist_add_circle_sharp, pending_actions_baseline, perm_camera_mic_baseline, personal_injury_baseline, phone_forwarded_baseline, phonelink_erase_baseline, phonelink_setup_baseline, playlist_remove_baseline, playlist_remove_outlined, people_outline_baseline, perm_phone_msg_baseline, perm_scan_wifi_baseline, person_add_alt_baseline, person_outline_baseline, personal_video_baseline, phone_callback_baseline, phone_disabled_baseline, phonelink_lock_baseline, phonelink_ring_baseline, picture_as_pdf_baseline, playlist_remove_rounded, pregnant_woman_baseline, present_to_all_baseline, print_disabled_baseline, perm_identity_baseline, person_remove_baseline, person_search_baseline, phone_android_baseline, phone_enabled_baseline, phone_in_talk_baseline, phonelink_off_baseline, photo_library_baseline, play_disabled_baseline, play_for_work_baseline, playlist_play_baseline, point_of_sale_baseline, priority_high_baseline, pan_tool_alt_baseline, pan_tool_alt_outlined, pause_circle_baseline, pest_control_baseline, phone_iphone_baseline, phone_locked_baseline, phone_missed_baseline, phone_paused_baseline, photo_camera_baseline, photo_filter_baseline, playlist_add_baseline, playlist_remove_sharp, price_change_baseline, pan_tool_alt_rounded, paragliding_baseline, photo_album_baseline, play_circle_baseline, play_lesson_baseline, power_input_baseline, price_check_baseline, privacy_tip_baseline, punch_clock_baseline, punch_clock_outlined, party_mode_baseline, pedal_bike_baseline, people_alt_baseline, perm_media_baseline, person_add_baseline, person_off_baseline, person_pin_baseline, pin_invoke_baseline, pin_invoke_outlined, plagiarism_baseline, play_arrow_baseline, psychology_baseline, public_off_baseline, punch_clock_rounded, pan_tool_alt_sharp, phonelink_baseline, piano_off_baseline, pie_chart_baseline, pin_invoke_rounded, power_off_baseline, pageview_baseline, pan_tool_baseline, panorama_baseline, password_baseline, payments_baseline, pentagon_baseline, pentagon_outlined, phishing_baseline, phishing_outlined, pin_drop_baseline, plumbing_baseline, plus_one_baseline, podcasts_baseline, polyline_baseline, polyline_outlined, portrait_baseline, post_add_baseline, punch_clock_sharp, push_pin_baseline, padding_baseline, palette_baseline, pattern_baseline, payment_baseline, pending_baseline, pentagon_rounded, percent_baseline, percent_outlined, phishing_rounded, pin_end_baseline, pin_end_outlined, pin_invoke_sharp, polyline_rounded, polymer_baseline, preview_baseline, publish_baseline, paypal_baseline, paypal_outlined, people_baseline, percent_rounded, person_baseline, pin_end_rounded, policy_baseline, public_baseline, pages_baseline, paste_baseline, pause_baseline, paypal_rounded, pentagon_sharp, phishing_sharp, phone_baseline, photo_baseline, piano_baseline, pinch_baseline, pinch_outlined, place_baseline, polyline_sharp, power_baseline, print_baseline, paid_baseline, park_baseline, percent_sharp, pets_baseline, pin_end_sharp, pinch_rounded, poll_baseline, pool_baseline, paypal_sharp, php_baseline, php_outlined, pin_baseline, pix_baseline, pix_outlined, php_rounded, pinch_sharp, pix_rounded, php_sharp, pix_sharp, quick_contacts_dialer_baseline, quick_contacts_mail_baseline, qr_code_scanner_baseline, question_answer_baseline, queue_play_next_baseline, query_builder_baseline, question_mark_baseline, question_mark_outlined, question_mark_rounded, query_stats_baseline, queue_music_baseline, question_mark_sharp, quickreply_baseline, qr_code_2_baseline, qr_code_baseline, queue_baseline, quora_baseline, quora_outlined, quiz_baseline, quora_rounded, quora_sharp, signal_wifi_statusbar_connected_no_internet_4_baseline, signal_cellular_connected_no_internet_4_bar_baseline, signal_cellular_connected_no_internet_0_bar_baseline, signal_wifi_connected_no_internet_4_baseline, sentiment_very_dissatisfied_baseline, signal_wifi_statusbar_4_bar_baseline, signal_wifi_statusbar_null_baseline, sentiment_very_satisfied_baseline, settings_input_component_baseline, settings_input_composite_baseline, settings_system_daydream_baseline, subdirectory_arrow_right_baseline, security_update_warning_baseline, sentiment_satisfied_alt_baseline, settings_backup_restore_baseline, subdirectory_arrow_left_baseline, sentiment_dissatisfied_baseline, settings_accessibility_baseline, settings_input_antenna_baseline, shopping_cart_checkout_baseline, shopping_cart_checkout_outlined, signal_cellular_no_sim_baseline, signal_cellular_nodata_baseline, signal_wifi_4_bar_lock_baseline, stay_current_landscape_baseline, stay_primary_landscape_baseline, screen_lock_landscape_baseline, screen_search_desktop_baseline, settings_applications_baseline, settings_input_svideo_baseline, shopping_cart_checkout_rounded, signal_cellular_4_bar_baseline, signal_cellular_0_bar_baseline, star_border_purple500_baseline, stay_current_portrait_baseline, stay_primary_portrait_baseline, screen_lock_portrait_baseline, screen_lock_rotation_baseline, security_update_good_baseline, signal_cellular_null_baseline, store_mall_directory_baseline, send_time_extension_baseline, send_time_extension_outlined, sentiment_satisfied_baseline, settings_brightness_baseline, settings_input_hdmi_baseline, shopping_cart_checkout_sharp, signal_cellular_alt_baseline, signal_cellular_off_baseline, sports_martial_arts_baseline, sports_martial_arts_outlined, send_time_extension_rounded, settings_bluetooth_baseline, share_arrival_time_baseline, sports_martial_arts_rounded, sports_motorsports_baseline, stacked_line_chart_baseline, sentiment_neutral_baseline, settings_ethernet_baseline, settings_overscan_baseline, signal_wifi_4_bar_baseline, signal_wifi_0_bar_baseline, sim_card_download_baseline, slow_motion_video_baseline, speaker_notes_off_baseline, sports_basketball_baseline, sports_gymnastics_baseline, sports_gymnastics_outlined, sports_volleyball_baseline, stacked_bar_chart_baseline, stop_screen_share_baseline, self_improvement_baseline, send_and_archive_baseline, send_time_extension_sharp, settings_display_baseline, settings_suggest_baseline, sports_gymnastics_rounded, sports_martial_arts_sharp, screen_rotation_baseline, security_update_baseline, settings_remote_baseline, shopping_basket_baseline, signal_wifi_bad_baseline, signal_wifi_off_baseline, social_distance_baseline, space_dashboard_baseline, sports_baseball_baseline, sports_football_baseline, sports_handball_baseline, strikethrough_s_baseline, safety_divider_baseline, send_to_mobile_baseline, settings_phone_baseline, settings_power_baseline, settings_voice_baseline, share_location_baseline, sim_card_alert_baseline, snippet_folder_baseline, sports_cricket_baseline, sports_esports_baseline, sports_gymnastics_sharp, sports_kabaddi_baseline, star_purple500_baseline, satellite_alt_baseline, satellite_alt_outlined, schedule_send_baseline, sd_card_alert_baseline, sensor_window_baseline, settings_cell_baseline, shopping_cart_baseline, shutter_speed_baseline, skateboarding_baseline, skip_previous_baseline, smart_display_baseline, smoking_rooms_baseline, sort_by_alpha_baseline, south_america_baseline, south_america_outlined, speaker_group_baseline, speaker_notes_baseline, speaker_phone_baseline, sports_hockey_baseline, sports_soccer_baseline, sports_tennis_baseline, sticky_note_2_baseline, satellite_alt_rounded, saved_search_baseline, scatter_plot_baseline, screen_share_baseline, scuba_diving_baseline, scuba_diving_outlined, shopping_bag_baseline, smart_button_baseline, smart_screen_baseline, snowboarding_baseline, soup_kitchen_baseline, soup_kitchen_outlined, south_america_rounded, sports_rugby_baseline, sports_score_baseline, star_outline_baseline, scuba_diving_rounded, sensor_door_baseline, sensors_off_baseline, shield_moon_baseline, shield_moon_outlined, snowshoeing_baseline, soup_kitchen_rounded, splitscreen_baseline, sports_golf_baseline, square_foot_baseline, star_border_baseline, stop_circle_baseline, satellite_alt_sharp, scoreboard_baseline, scoreboard_outlined, screenshot_baseline, sd_storage_baseline, search_off_baseline, select_all_baseline, shield_moon_rounded, short_text_baseline, show_chart_baseline, shuffle_on_baseline, single_bed_baseline, smartphone_baseline, smoke_free_baseline, sms_failed_baseline, snowmobile_baseline, south_america_sharp, south_east_baseline, south_west_baseline, spellcheck_baseline, sports_bar_baseline, sports_mma_baseline, ssid_chart_baseline, ssid_chart_outlined, storefront_baseline, straighten_baseline, streetview_baseline, sanitizer_baseline, satellite_baseline, scoreboard_rounded, scuba_diving_sharp, skip_next_baseline, slideshow_baseline, smart_toy_baseline, soup_kitchen_sharp, space_bar_baseline, ssid_chart_rounded, star_half_baseline, star_rate_baseline, save_alt_baseline, schedule_baseline, security_baseline, set_meal_baseline, settings_baseline, shield_moon_sharp, shop_two_baseline, shortcut_baseline, signpost_baseline, signpost_outlined, sim_card_baseline, sledding_baseline, snapchat_baseline, snapchat_outlined, straight_baseline, straight_outlined, stroller_baseline, sailing_baseline, save_as_baseline, save_as_outlined, savings_baseline, scanner_baseline, science_baseline, scoreboard_sharp, sd_card_baseline, segment_baseline, sensors_baseline, shopify_baseline, shopify_outlined, shuffle_baseline, signpost_rounded, snapchat_rounded, snowing_baseline, speaker_baseline, ssid_chart_sharp, stadium_baseline, stadium_outlined, storage_baseline, straight_rounded, subject_baseline, save_as_rounded, schema_baseline, school_baseline, search_baseline, shield_baseline, shop_2_baseline, shopify_rounded, shower_baseline, snooze_baseline, source_baseline, sports_baseline, square_baseline, square_outlined, stadium_rounded, stairs_baseline, stream_baseline, scale_baseline, scale_outlined, score_baseline, share_baseline, signpost_sharp, snapchat_sharp, south_baseline, speed_baseline, spoke_baseline, spoke_outlined, square_rounded, stars_baseline, start_baseline, start_outlined, store_baseline, storm_baseline, straight_sharp, style_baseline, save_as_sharp, save_baseline, scale_rounded, sell_baseline, send_baseline, shop_baseline, shopify_sharp, sick_baseline, soap_baseline, sort_baseline, spoke_rounded, stadium_sharp, star_baseline, start_rounded, stop_baseline, sip_baseline, sms_baseline, spa_baseline, square_sharp, scale_sharp, sd_baseline, spoke_sharp, start_sharp, radio_button_unchecked_baseline, remove_circle_outline_baseline, rotate_90_degrees_ccw_baseline, radio_button_checked_baseline, remove_shopping_cart_baseline, replay_circle_filled_baseline, report_gmailerrorred_baseline, rotate_90_degrees_cw_baseline, rotate_90_degrees_cw_outlined, rotate_90_degrees_cw_rounded, running_with_errors_baseline, restore_from_trash_baseline, real_estate_agent_baseline, record_voice_over_baseline, remove_from_queue_baseline, rotate_90_degrees_cw_sharp, radio_button_off_baseline, remove_moderator_baseline, room_preferences_baseline, roundabout_right_baseline, roundabout_right_outlined, radio_button_on_baseline, reduce_capacity_baseline, restaurant_menu_baseline, roundabout_left_baseline, roundabout_left_outlined, roundabout_right_rounded, remove_red_eye_baseline, report_problem_baseline, roller_skating_baseline, roller_skating_outlined, roundabout_left_rounded, rounded_corner_baseline, railway_alert_baseline, recent_actors_baseline, remove_circle_baseline, repeat_one_on_baseline, request_quote_baseline, rocket_launch_baseline, rocket_launch_outlined, roller_skating_rounded, roundabout_right_sharp, r_mobiledata_baseline, ramen_dining_baseline, receipt_long_baseline, request_page_baseline, restore_page_baseline, rocket_launch_rounded, room_service_baseline, rotate_right_baseline, roundabout_left_sharp, rate_review_baseline, remember_me_baseline, remove_done_baseline, restart_alt_baseline, ring_volume_baseline, roller_skating_sharp, rotate_left_baseline, rule_folder_baseline, ramp_right_baseline, ramp_right_outlined, repeat_one_baseline, report_off_baseline, restaurant_baseline, rocket_launch_sharp, run_circle_baseline, ramp_left_baseline, ramp_left_outlined, ramp_right_rounded, read_more_baseline, recommend_baseline, rectangle_baseline, rectangle_outlined, recycling_baseline, recycling_outlined, repeat_on_baseline, replay_10_baseline, replay_30_baseline, reply_all_baseline, rice_bowl_baseline, rv_hookup_baseline, ramp_left_rounded, rectangle_rounded, recycling_rounded, replay_5_baseline, reset_tv_baseline, rss_feed_baseline, ramp_right_sharp, raw_off_baseline, receipt_baseline, refresh_baseline, reorder_baseline, restore_baseline, reviews_baseline, roofing_baseline, ramp_left_sharp, raw_on_baseline, rectangle_sharp, recycling_sharp, reddit_baseline, reddit_outlined, redeem_baseline, remove_baseline, repeat_baseline, replay_baseline, report_baseline, rocket_baseline, rocket_outlined, router_baseline, rowing_baseline, radar_baseline, radio_baseline, reddit_rounded, reply_baseline, rocket_rounded, route_baseline, route_outlined, redo_baseline, room_baseline, route_rounded, rsvp_baseline, rule_baseline, reddit_sharp, rocket_sharp, rtt_baseline, route_sharp, update_disabled_baseline, u_turn_right_baseline, u_turn_right_outlined, u_turn_left_baseline, u_turn_left_outlined, u_turn_right_rounded, unfold_less_baseline, unfold_more_baseline, unpublished_baseline, unsubscribe_baseline, upload_file_baseline, u_turn_left_rounded, u_turn_right_sharp, unarchive_baseline, u_turn_left_sharp, umbrella_baseline, upcoming_baseline, upgrade_baseline, usb_off_baseline, update_baseline, upload_baseline, undo_baseline, usb_baseline, transfer_within_a_station_baseline, text_rotation_angledown_baseline, text_rotation_angleup_baseline, text_rotate_vertical_baseline, text_rotation_down_baseline, text_rotation_none_baseline, thumb_down_off_alt_baseline, transit_enterexit_baseline, turn_slight_right_baseline, turn_slight_right_outlined, table_restaurant_baseline, table_restaurant_outlined, thumb_up_off_alt_baseline, tips_and_updates_baseline, tips_and_updates_outlined, trending_neutral_baseline, turn_sharp_right_baseline, turn_sharp_right_outlined, turn_slight_left_baseline, turn_slight_left_outlined, turn_slight_right_rounded, table_restaurant_rounded, temple_buddhist_baseline, temple_buddhist_outlined, thermostat_auto_baseline, timer_10_select_baseline, tips_and_updates_rounded, turn_sharp_left_baseline, turn_sharp_left_outlined, turn_sharp_right_rounded, turn_slight_left_rounded, tab_unselected_baseline, tablet_android_baseline, takeout_dining_baseline, temple_buddhist_rounded, text_rotate_up_baseline, theater_comedy_baseline, thumb_down_alt_baseline, thumbs_up_down_baseline, timer_3_select_baseline, travel_explore_baseline, turn_sharp_left_rounded, turn_slight_right_sharp, table_restaurant_sharp, text_decrease_baseline, text_decrease_outlined, text_increase_baseline, text_increase_outlined, time_to_leave_baseline, tips_and_updates_sharp, track_changes_baseline, trending_down_baseline, trending_flat_baseline, turn_sharp_right_sharp, turn_slight_left_sharp, turned_in_not_baseline, tap_and_play_baseline, temple_buddhist_sharp, temple_hindu_baseline, temple_hindu_outlined, text_decrease_rounded, text_increase_rounded, text_snippet_baseline, thumb_up_alt_baseline, turn_sharp_left_sharp, table_chart_baseline, temple_hindu_rounded, text_fields_baseline, text_format_baseline, tire_repair_baseline, tire_repair_outlined, transgender_baseline, trending_up_baseline, trip_origin_baseline, two_wheeler_baseline, table_rows_baseline, table_view_baseline, tablet_mac_baseline, taxi_alert_baseline, text_decrease_sharp, text_increase_sharp, thermostat_baseline, thumb_down_baseline, tire_repair_rounded, toggle_off_baseline, turn_right_baseline, turn_right_outlined, table_bar_baseline, table_bar_outlined, tag_faces_baseline, temple_hindu_sharp, timelapse_baseline, timer_off_baseline, toggle_on_baseline, touch_app_baseline, transform_baseline, translate_baseline, turn_left_baseline, turn_left_outlined, turn_right_rounded, turned_in_baseline, table_bar_rounded, task_alt_baseline, telegram_baseline, telegram_outlined, terminal_baseline, terminal_outlined, theaters_baseline, thumb_up_baseline, timeline_baseline, timer_10_baseline, tire_repair_sharp, tonality_baseline, tungsten_baseline, turn_left_rounded, telegram_rounded, terminal_rounded, terrain_baseline, textsms_baseline, texture_baseline, timer_3_baseline, traffic_baseline, turn_right_sharp, table_bar_sharp, tablet_baseline, tiktok_baseline, tiktok_outlined, turn_left_sharp, tv_off_baseline, tapas_baseline, telegram_sharp, terminal_sharp, tiktok_rounded, timer_baseline, title_baseline, today_baseline, token_baseline, token_outlined, topic_baseline, train_baseline, task_baseline, token_rounded, toll_baseline, tour_baseline, toys_baseline, tram_baseline, tune_baseline, tab_baseline, tag_baseline, tiktok_sharp, toc_baseline, try_baseline, tty_baseline, token_sharp, tv_baseline, system_security_update_warning_baseline, system_security_update_good_baseline, switch_access_shortcut_add_baseline, switch_access_shortcut_add_outlined, switch_access_shortcut_add_rounded, switch_access_shortcut_add_sharp, supervised_user_circle_baseline, swap_horizontal_circle_baseline, switch_access_shortcut_baseline, switch_access_shortcut_outlined, system_security_update_baseline, switch_access_shortcut_rounded, swap_vertical_circle_baseline, switch_access_shortcut_sharp, supervisor_account_baseline, system_update_alt_baseline, swap_vert_circle_baseline, system_update_tv_baseline, swipe_right_alt_baseline, swipe_right_alt_outlined, surround_sound_baseline, swipe_down_alt_baseline, swipe_down_alt_outlined, swipe_left_alt_baseline, swipe_left_alt_outlined, swipe_right_alt_rounded, swipe_vertical_baseline, swipe_vertical_outlined, switch_account_baseline, subscriptions_baseline, subtitles_off_baseline, sunny_snowing_baseline, support_agent_baseline, swipe_down_alt_rounded, swipe_left_alt_rounded, swipe_vertical_rounded, switch_camera_baseline, sync_disabled_baseline, system_update_baseline, swipe_right_alt_sharp, swipe_up_alt_baseline, swipe_up_alt_outlined, switch_right_baseline, switch_video_baseline, sync_problem_baseline, superscript_baseline, swipe_down_alt_sharp, swipe_left_alt_sharp, swipe_right_baseline, swipe_right_outlined, swipe_up_alt_rounded, swipe_vertical_sharp, switch_left_baseline, swap_calls_baseline, swap_horiz_baseline, swipe_down_baseline, swipe_down_outlined, swipe_left_baseline, swipe_left_outlined, swipe_right_rounded, subscript_baseline, subtitles_baseline, summarize_baseline, swap_vert_baseline, swipe_down_rounded, swipe_left_rounded, swipe_up_alt_sharp, synagogue_baseline, synagogue_outlined, sync_lock_baseline, sync_lock_outlined, swipe_right_sharp, swipe_up_baseline, swipe_up_outlined, synagogue_rounded, sync_alt_baseline, sync_lock_rounded, support_baseline, surfing_baseline, swipe_down_sharp, swipe_left_sharp, swipe_up_rounded, subway_baseline, synagogue_sharp, sync_lock_sharp, sunny_baseline, swipe_baseline, swipe_up_sharp, sync_baseline, youtube_searched_for_baseline, yard_baseline, wifi_tethering_error_rounded_baseline, wifi_protected_setup_baseline, wifi_tethering_error_baseline, wifi_tethering_error_outlined, wifi_tethering_off_baseline, workspaces_outline_baseline, wallet_membership_baseline, wheelchair_pickup_baseline, wifi_tethering_error_sharp, workspace_premium_baseline, workspace_premium_outlined, workspaces_filled_baseline, workspace_premium_rounded, wallet_giftcard_baseline, waterfall_chart_baseline, wb_incandescent_baseline, wifi_calling_3_baseline, wifi_tethering_baseline, workspace_premium_sharp, wrong_location_baseline, wallet_travel_baseline, warning_amber_baseline, wb_iridescent_baseline, wb_twighlight_baseline, web_asset_off_baseline, where_to_vote_baseline, wifi_password_baseline, wifi_password_outlined, water_damage_baseline, wifi_calling_baseline, wifi_channel_baseline, wifi_channel_outlined, wifi_password_rounded, woo_commerce_baseline, woo_commerce_outlined, work_outline_baseline, watch_later_baseline, waving_hand_baseline, waving_hand_outlined, wb_twilight_baseline, web_stories_baseline, wifi_channel_rounded, woo_commerce_rounded, water_drop_baseline, water_drop_outlined, waving_hand_rounded, wifi_password_sharp, workspaces_baseline, wallpaper_baseline, warehouse_baseline, warehouse_outlined, watch_off_baseline, watch_off_outlined, water_drop_rounded, wb_cloudy_baseline, web_asset_baseline, wifi_channel_sharp, wifi_find_baseline, wifi_find_outlined, wifi_lock_baseline, woo_commerce_sharp, wordpress_baseline, wordpress_outlined, wrap_text_baseline, warehouse_rounded, watch_off_rounded, waving_hand_sharp, wb_shade_baseline, wb_sunny_baseline, whatsapp_baseline, whatsapp_outlined, whatshot_baseline, wifi_find_rounded, wifi_off_baseline, wine_bar_baseline, wordpress_rounded, work_off_baseline, warning_baseline, water_drop_sharp, wb_auto_baseline, webhook_baseline, webhook_outlined, weekend_baseline, whatsapp_rounded, widgets_baseline, wysiwyg_baseline, warehouse_sharp, watch_off_sharp, webhook_rounded, wechat_baseline, wechat_outlined, wifi_find_sharp, window_baseline, wordpress_sharp, watch_baseline, water_baseline, waves_baseline, wechat_rounded, whatsapp_sharp, woman_baseline, woman_outlined, wash_baseline, webhook_sharp, west_baseline, wifi_baseline, woman_rounded, work_baseline, web_baseline, wechat_sharp, wc_baseline, woman_sharp, vertical_align_bottom_baseline, vertical_align_center_baseline, vertical_distribute_baseline, videogame_asset_off_baseline, vertical_align_top_baseline, video_camera_front_baseline, volunteer_activism_baseline, video_camera_back_baseline, video_collection_baseline, view_comfortable_baseline, view_compact_alt_baseline, view_compact_alt_outlined, videogame_asset_baseline, view_compact_alt_rounded, volume_down_alt_baseline, vertical_split_baseline, video_settings_baseline, view_comfy_alt_baseline, view_comfy_alt_outlined, visibility_off_baseline, voice_over_off_baseline, verified_user_baseline, video_library_baseline, view_carousel_baseline, view_comfy_alt_rounded, view_compact_alt_sharp, view_headline_baseline, view_timeline_baseline, view_timeline_outlined, vaping_rooms_baseline, vaping_rooms_outlined, video_stable_baseline, videocam_off_baseline, view_compact_baseline, view_sidebar_baseline, view_timeline_rounded, vaping_rooms_rounded, video_label_baseline, view_agenda_baseline, view_column_baseline, view_comfy_alt_sharp, view_kanban_baseline, view_kanban_outlined, view_module_baseline, view_stream_baseline, volume_down_baseline, volume_mute_baseline, vpn_key_off_baseline, vpn_key_off_outlined, video_call_baseline, video_file_baseline, video_file_outlined, view_array_baseline, view_comfy_baseline, view_in_ar_baseline, view_kanban_rounded, view_quilt_baseline, view_timeline_sharp, visibility_baseline, voice_chat_baseline, volume_off_baseline, vpn_key_off_rounded, vape_free_baseline, vape_free_outlined, vaping_rooms_sharp, vibration_baseline, video_file_rounded, view_cozy_baseline, view_cozy_outlined, view_list_baseline, view_week_baseline, voicemail_baseline, volume_up_baseline, vaccines_baseline, vaccines_outlined, vape_free_rounded, verified_baseline, videocam_baseline, view_cozy_rounded, view_day_baseline, view_kanban_sharp, vignette_baseline, vpn_key_off_sharp, vpn_lock_baseline, vaccines_rounded, video_file_sharp, vpn_key_baseline, vape_free_sharp, view_cozy_sharp, vrpano_baseline, vaccines_sharp, villa_baseline, zoom_out_map_baseline, zoom_in_map_baseline, zoom_in_map_outlined, zoom_in_map_rounded, zoom_in_map_sharp, zoom_out_baseline, zoom_in_baseline}
❌ new codepoints file does not contain all 7315 existing codepoints. Missing: {baby_changing_station, battery_charging_full, browser_not_supported, bluetooth_connected, bluetooth_searching, bluetooth_disabled, branding_watermark, border_horizontal, brightness_medium, batch_prediction, bookmark_outline, breakfast_dining, battery_unknown, bluetooth_audio, bluetooth_drive, bookmark_border, bookmark_remove, border_vertical, brightness_auto, brightness_high, business_center, bedroom_parent, bookmark_added, brightness_low, bakery_dining, battery_alert, battery_saver, bedroom_child, block_flipped, blur_circular, border_bottom, brunch_dining, backup_table, battery_full, beach_access, bedroom_baby, bike_scooter, bookmark_add, border_clear, border_color, border_inner, border_outer, border_right, border_style, brightness_5, brightness_4, brightness_1, brightness_7, brightness_6, brightness_3, brightness_2, broken_image, bubble_chart, build_circle, battery_std, blur_linear, book_online, border_left, border_all, border_top, bug_report, burst_mode, backspace, bar_chart, bloodtype, bluetooth, bookmarks, bus_alert, backpack, bathroom, beenhere, blur_off, bookmark, bungalow, business, balcony, bathtub, bedtime, biotech, blender, blur_on, backup, ballot, badge, bento, block, brush, build, bolt, book, bed, airline_seat_individual_suite, airline_seat_legroom_reduced, airline_seat_legroom_normal, airline_seat_recline_normal, airline_seat_legroom_extra, airline_seat_recline_extra, airline_seat_flat_angled, align_horizontal_center, account_balance_wallet, align_horizontal_right, arrow_drop_down_circle, airplanemode_inactive, align_horizontal_left, align_vertical_bottom, align_vertical_center, admin_panel_settings, assignment_turned_in, assistant_navigation, add_photo_alterna…

---
## [UniverseLambda/42-inception](https://github.com/UniverseLambda/42-inception)@[3e435789ac...](https://github.com/UniverseLambda/42-inception/commit/3e435789acb00ac4e464eddcd98407917efb177f)
#### Wednesday 2022-03-09 15:37:02 by clsaad

clement: more unit test, IComm interface and more

introducing IComm interface, which aims to add abstraction for the client-server communication process (perfect for tests)
add Interface header to ease the creation of interface with 42's restrictions
add more (and more complex) unit tests
User now has a pointer to Server
every class (should) now respect the canonical form
remove privatisation of copy constructor/assign operator
improve unit test error reporting mechanism
fix Channel::setMode always returning false
fix Message not copying mChannel (FUCK YOU <3)

---
## [facebook/pyre-check](https://github.com/facebook/pyre-check)@[e721ace08b...](https://github.com/facebook/pyre-check/commit/e721ace08b810e219eabd3cc14d1373d832e0cb6)
#### Wednesday 2022-03-09 16:08:54 by Steven Troxler

Productionize incremental API (#596)

Summary:
Switch the API from using `uwsgi` over a socket to `gunicorn` over port 5000.

With this change, I am able to get it working in incremental mode with one pyre server per worker thread.

### Context for the changes

**Why the switch from `uwsgi` to `gunicorn`?**

They have different worker startup models: `uwsgi` does module initialization upfront and then forks, whereas gunicorn just starts multiple workers.

This is a problem for me because it is much easier to ensure each worker has an associated incremental server if we can force this initialization to happen at startup. There is a uwsgi decorator that should help with this, but I struggled to make it work properly, and the internet broadly suggests that gunicorn is a better choice anyway for simple webapps - uwsgi is more powerful but also quite a bit harder to fully understand because it is more complex.

**Why use port 5000 rather than a socket?**

A lot of guides use sockets, which in theory is simpler and more efficient. But if anything doesn't work, it puts us in a pickle because it's not straightforward to send HTTP requests to a socket, which means we can't easily determine whether a problem is with the server itself or the nginx config.

Running on port 5000 makes it easy to query the gunicorn server directly to determine that it is working, at which point any problems have to be with nginx.

It makes no difference from a security point of view given that port 5000 is closed (so you have to be ssh'ed in to hit it), and the overhead isn't a real concern.

For future reference I think it is possible to curl a socket, it's just quite a bit harder to remember the incantation, and the first few webpages I looked at gave me commands that didn't work. But here's a discussion of how to do it using the extra `--unix-socket`; the unintuitive thing is that the socket and the rest of the URL don't live in the same argument to the curl command
https://superuser.com/questions/834307/can-curl-send-requests-to-sockets

 ---

Pull Request resolved: https://github.com/facebook/pyre-check/pull/596

Test Plan:
The commands needed to spin up a playground server are unchanged, we're still using nginx plus a systemd service.

I rebooted the server running this code and saw that we now reliably finish typecheck requests in around a second.

Reviewed By: grievejia

Differential Revision: D34687333

Pulled By: stroxler

fbshipit-source-id: 28c918ded24a08e8ef71bc005c49d63aeb28bc13

---
## [jobfaironline/jobfair-frontend](https://github.com/jobfaironline/jobfair-frontend)@[fcbbc81afd...](https://github.com/jobfaironline/jobfair-frontend/commit/fcbbc81afd64c712ba44a81a28b0f2b37ec26ca5)
#### Wednesday 2022-03-09 17:00:54 by Tien T. Truong

Cap 197 This is trash (#64)

* add third person control

* fix third person control

* add outline

* refactor

* fucking shit this is so much pain please kill me

---
## [bluca/systemd-stable](https://github.com/bluca/systemd-stable)@[367041af81...](https://github.com/bluca/systemd-stable/commit/367041af816d48d4852140f98fd0ba78ed83f9e4)
#### Wednesday 2022-03-09 17:50:37 by Lennart Poettering

pid1: set SYSTEMD_NSS_DYNAMIC_BYPASS=1 env var for dbus-daemon

There's currently a deadlock between PID 1 and dbus-daemon: in some
cases dbus-daemon will do NSS lookups (which are blocking) at the same
time PID 1 synchronously blocks on some call to dbus-daemon. Let's break
that by setting SYSTEMD_NSS_DYNAMIC_BYPASS=1 env var for dbus-daemon,
which will disable synchronously blocking varlink calls from nss-systemd
to PID 1.

In the long run we should fix this differently: remove all synchronous
calls to dbus-daemon from PID 1. This is not trivial however: so far we
had the rule that synchronous calls from PID 1 to the dbus broker are OK
as long as they only go to interfaces implemented by the broke itself
rather than services reachable through it. Given that the relationship
between PID 1 and dbus is kinda special anyway, this was considered
acceptable for the sake of simplicity, since we quite often need
metadata about bus peers from the broker, and the asynchronous logic
would substantially complicate even the simplest method handlers.

This mostly reworks the existing code that sets SYSTEMD_NSS_BYPASS_BUS=
(which is a similar hack to deal with deadlocks between nss-systemd and
dbus-daemon itself) to set SYSTEMD_NSS_DYNAMIC_BYPASS=1 instead. No code
was checking SYSTEMD_NSS_BYPASS_BUS= anymore anyway, and it used to
solve a similar problem, hence it's an obvious piece of code to rework
like this.

Issue originally tracked down by Lukas Märdian. This patch is inspired
and closely based on his patch:

       https://github.com/systemd/systemd/pull/22038

Fixes: #15316
Co-authored-by: Lukas Märdian <slyon@ubuntu.com>
(cherry picked from commit de90700f36f2126528f7ce92df0b5b5d5e277558)

---
## [absent-cc/backend](https://github.com/absent-cc/backend)@[775749b27c...](https://github.com/absent-cc/backend/commit/775749b27c2ee6616ea424d438b6560660362508)
#### Wednesday 2022-03-09 18:37:23 by Roshan Karim

fixed kevins retarded ass shit that he should have done himself but didn't because he couldn't read the code TWO LINES below it to figure out how things were done correctly my fucking god

---
## [Nesjob/The-Jackbox-Party-Pack-8-German](https://github.com/Nesjob/The-Jackbox-Party-Pack-8-German)@[49bdfb6bd9...](https://github.com/Nesjob/The-Jackbox-Party-Pack-8-German/commit/49bdfb6bd96cea0a8e76c1fab0cc47eec69aa87a)
#### Wednesday 2022-03-09 18:47:18 by Maxi

8 Fragen

Bezüglich der VfB-Frage: Leider ist der Begriff VfB allein nicht sehr aussagekräftig, da es VfB's wie Sand am Meer gibt. Verstehe aber die Frustration. Ja, ich wollte die Fragen mal im Spiel sehen. Faszinierendes Gefühl XD.
1. Welches sind echte Krawattenknoten? (ID 83447).
2. Welche dieser Athleten haben fünf oder mehr olympische Goldmedaillen gewonnen? Ich habe ein paar deutsche Namen hinzugefügt, auch wenn die vermutlich auch keine Sau kennt (ID 83080).
3. Welches sind echte Arten von Quallen? Bah, ekelhafte Viecher (ID 82907).
4. Welche dieser Personen, Gruppen oder Gegenstände wurden Stand 2021 vom US-amerikanischen Time Magazine zur "Person of the Year" ausgezeichnet? Sie ist jetzt nicht mehr familienfreundlich, da ich entdeckt habe, dass Hitler und Stalin auf dieser Liste sind XD (ID 82899).
5. Welche dieser Speisen wurden in der ersten Klasse der Titanic serviert, nur Stunden bevor sie am 14. April 1912 sank? Ich hatte echt Probleme, diese Speisen zu übersetzen (ID 82891).
6. Welche dieser Tiere sind Beuteltiere? Endlich mal niedliche Tiere (ID 82742).
7. Wobei handelt es sich um Positionen im Fußball? (ID 82716).
8. Welches sind Teile eines Kreises? Schon wieder so ein übelster Dad-Joke. Kreisverwaltung lol (ID 82689).

---
## [rbleattler/IISLogManager](https://github.com/rbleattler/IISLogManager)@[5a47540495...](https://github.com/rbleattler/IISLogManager/commit/5a475404954c3a3a0bde449642bd7ee03b43057a)
#### Wednesday 2022-03-09 19:02:14 by Robert Bleattler

fix nuspec to follow old stupid nuget rules. I hate you nuget. die in a fire

---
## [Bradenbertrand/WordleLeaderboards](https://github.com/Bradenbertrand/WordleLeaderboards)@[7d72802679...](https://github.com/Bradenbertrand/WordleLeaderboards/commit/7d72802679f537457a40fe743ee03afdce1b1752)
#### Wednesday 2022-03-09 20:00:41 by Bradenbertrand

Update getSolution.js

more frustrating attempts at figuring this out before I leave for work in 30 min (sorry to employers looking at this ik its not a journal but fuck it mcnugget)

---
## [Tiktodz/kernel_asus_sdm660](https://github.com/Tiktodz/kernel_asus_sdm660)@[16efa746f8...](https://github.com/Tiktodz/kernel_asus_sdm660/commit/16efa746f8cb4cb2c391d8bf62866f346ac5a120)
#### Wednesday 2022-03-09 20:13:10 by Angelo G. Del Regno

Makefile.lib: Lower kernel gzip compression to fastest

You're reading this - so you're trying to understand "JUST WHY OMG".
That's already a good step.

First of all, this is a downstream kernel - always keep that in mind!
Now, this kernel is targeting new *very powerful* Qualcomm platforms
like SM8250 and the Sony Edo platform - which has a very fast UFS card.

Keep in mind that the bootloader sets the CPU at a frequency that is
slightly faster than the "in the middle" ones, which is anyway not
veeeery fast - but that's good, really. I agree.

So.. check this out:   for Image.gz-dtb.....
COMP_LEVEL    SIZE
9             20116171
5	      20220479
2	      20940223
1	      21231290

Remember again that we're loading from a UFS card and that
we are loading ~1.1MB more out of a 20MB file.
If you're smart enough you surely know already about RAM and CPU
overhead of very high compression levels.

If you still disagree with what I just did, read this commit description
another 20 times, or more, until you understand it. :)))

Signed-off-by: RyuujiX <saputradenny712@gmail.com>
Signed-off-by: Tiktodz <kuplemarkeple@gmail.com>

---
## [azhou-determined/determined](https://github.com/azhou-determined/determined)@[08888717a6...](https://github.com/azhou-determined/determined/commit/08888717a6db21304115cd119ebb5d926d51c88e)
#### Wednesday 2022-03-09 20:19:41 by Bradley Laney

feat: unify task logs [DET-6062, DET-6063, DET-6064, DET-6065, DET-6066] (#3070)

This change adds persistent logs for all task types (well, all except poor old checkpoint GC). This means that logs are written to the logging back-end as configured in the master (PostgreSQL through master or Elastic) by Fluentbit and accessible through APIs in the master that translate reads to the back-end's language. To allow for this change, many other changes were required. A (probably) non-exhaustive list follows:
* Trial logs used to go to a `trial_logs` table or index. I tried to not tear the codebase asunder forever with trials and the others using different tables/queries/structs/etc everywhere. Existing tasks were marked has having `log_version == 0` and the old `trial_logs` table now serves logs those tasks (only trials). From now on, all tasks are written with `log_version == 1` and queries for their logs are routed to the `task_logs` table. The old trial logs table (now the `log_version == 0` table) is mothballed - it (mostly) shouldn't be touched again and the old logs should load from there fine forever while new features can be built on the new table. There were alternatives besides leaving trials and task logs separate forever that I shied away from; e.g., I considered a migration to update the trial logs table to schema of the task logs table, but since we access task logs by task_id, this would require rewriting the index on trial_id or adding one on task_id which is too expensive for a migration. This solution balances complexity, maintainability and migration cost.
* Because task logs went through the master, we were free to built features like readiness checks on top of them. Now that they don't, before logs leave the container a small helper script skims them, checks for the readiness logs and posts readiness to a new API. I considered alternatives here, too, like reading the logs back in on the master side, but that incurs a lot more overhead I felt this was more flexible anyway.
* The old events endpoint used to return logs, now it doesn't. This was because it (the eventManager that backed the endpoint) used to _store_ the logs, and now it doesn’t. In my opinion, the work to read the log stream and the old event stream and merge them is low value and annoying. Users should just prefer the new `/api/v1/tasks/:id/logs` endpoint for logs and rely on events to get the few task events that were relied on. Events will likely be supplanted by a task state watcher of some time so webui/cli can just watch for the readiness bit to flip.

---
## [lawrieliv/stats220](https://github.com/lawrieliv/stats220)@[1335244698...](https://github.com/lawrieliv/stats220/commit/1335244698e2d6ce6d6d689af1bb6cab164b993a)
#### Wednesday 2022-03-09 20:59:38 by lawrieliv

Create index.md

Most people go through the five stages of grief whether in life or forms of entertainment.  I can say that the little errors that appeared during the creation of my meme made my experience the five stages of grief

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[e7e6a6339c...](https://github.com/mrakgr/The-Spiral-Language/commit/e7e6a6339c7befd5dda5e0af696c39bc4e5dacb4)
#### Wednesday 2022-03-09 21:33:13 by Marko Grdinić

"8:55am. Woke up early due to a nightmare, and to make matters worse while stretching I accidentally pulled a mucle on my left leg. On the plus side, it is not as bad the last time this happened. This demontrates the perils of multitasking.

https://mangadex.org/chapter/709f1499-b957-4d5b-b396-78b495a31d1a/5

Wow, this is completely different that the translation by WildFang. Now I am wondering what is wrong in the latest one. Ok, I'll make it a rule not to read stuff by the WF guy again.

Let me chill Freiren and Yakuza Princess are out as well. Let me do this part and then I will start. I've been tirelessly collecting knowledge for the past week and now will be the time to put it to use.

10am. Let me start. It is time to get things done. Time to get competent at art for real. Lately, while watching anime I've been paying attention to the backgrounds and thinking - how could I do that? I haven't seen a case that I could not do yet. I need to put this power to good use.

10:05am. Now as the first thing. I really need to decide how to assign materials. Right now it is really awkward for me how I can't change the existing assignments. But more than that, I need to move them after pack. V-Ray considers materials on the object level.

10:10am. https://www.reddit.com/r/Houdini/comments/ovfkr8/help_with_assigning_materials/

No, forget Solaris. Let me just remove all the materials, and their node. Then I'll do them from scratch.

Oh, if you delete them, they still remain assigned. That is good to know. That will make swapping them a lot easier.

Still, I wish I could use something like a material library. Solaris is not a bad idea. If I wanted to make a night scene and a day scene without modifying geometry it would be a good way to parameterize all of that. I'll ignore those considerations for now.

10:40am. I've just realized that `uvwgen` is an int. What the hell? How is that possible? I mean it clearly has translation, rotation and offset. There is not enough room for all of that in the UV.

https://docs.chaos.com/display/VRAYHOUDINI/V-Ray+Bercon+Distortion

Let me read the docs for this. The process of painting 3d is essentially manipulating noise functions. When I first saw this in Blender it felt like a huge hack, but now I think it is divine. Most likely, the brain itself works by doing something like this. It is certainly not chaining matrix multiplies together like ANNs.

10:50am. I had no idea you can have such complex brick patterns. Mastering procedural textures is really a major part of being good at shading. This is something I will be practicing quite a bit.

https://docs.chaos.com/display/VMAX/VRayUVWRandomizer#expand-UIPathMaterialEditorwindowMaterialMapBrowserMaps

I should pay attention to help for other versions of V-Ray.

https://docs.chaos.com/display/VMAX/VRayCurvature

Why doesn't the Houdini version have this?

11:30am. The ramp for the bercon grad is behaving extremely strangely.

The bypass through the gradient ramp does not work. V-Ray for Houdini is full of bugs. if it wasn't for the bugs it would be quite decent. For this reason I am really tempted to try out Redshift.

12pm. I am not doing anything great right now. I am just trying to get a handle on how the gradient textures work.

I found this very thing confusing in Blender as well.

12:05pm. I broke something and the shader is not working. What the hell?

How ridiculous. It was not looking at the material assignment due to what it was focused on. But if the object was turned off in the object mode it would get ignored. So I naturally assumed that the output node would take priority.

Another bug in V-Ray.

12:30pm. Ah, ah crap. I am so dumb. I've been scratching my head all this time as to why the hell is the gradient 3d box texture starting at 0.5,0.5,0.5, but that makes sense if you think what those represent in UV space. In UV space 0.5 is the center!

Still, how is the centroid calculated? The object's pivot is is object level translation. Then 0.5 just get added to that.

1:45pm. Let me stop here.

3:30pm. Done with breakfast and chores. Let me resume.

Wow, are object spaces confusing. The way to make translation for example sane, I'd need to divide by scale and negate it.

Now, let me figure out how rotation works.

3:35pm. Also during the break, I managed to reason out how to make UVs explicit. What I need is UV To Texture. That turns them into color. And then I can reassemble them using Expilicit UV.

That would give me more flexibility when it comes to manipulating UVs. Now...

3:50pm. Yeah, it goes translation scale rotation (Rx Ry Rz). Damn what a pain in the ass. I can't believe it took me this long just to get a grasp on procedural textures. At least in Houdini I can add some extra params and automate things.

The fact that radial and box textures start at 0 makes them really annoying to rotate.

4pm. Why does gradient nose in the gradient ramp not work?

4:55pm. Let me take a break here. I've been fiddling with that leaf for 4h now. Seeing how little progress I make artistically each day is making me self conscious.

No, the gradient textures are difficult to deal with. I should try to avoid them if possible. Or rather, if I want to texture directly, I should do that in a dedicated fashion.

I should try doing it Blender first and see where that takes me after that.

5:45pm. I am playing around with textures in Blender. I've finally figured out exactly what generated coordiates are. They are right there in texture space. While the object is based directly off the pivot point.

Ok, that is one thing. Let me go back to Houdini. Is making auto UVs and then setting them up in the COP network a possibility?

It does not seem like it.

Let me watch a tut.

https://youtu.be/xqpVoQ4f-gM
How to use COP nodes for texturing in Houdini.

https://youtu.be/xqpVoQ4f-gM?t=96

I think I saw COP2 having a bunch of patterns, but I can't find any. I do not have the pattern used in this video.

6:10pm. This was short and sweet.

https://youtu.be/8QIASDCh0Qw?t=12

What he has here looks so good.

6:15pm. Let me have lunch.

He has a bunch of textures. In theory I could do a lot with gradient texture composition, but it is just too unwieldy to work like that.

Imagine trying to do image editing by modifying hex values. It could work only in theory and not practice. Just why are these gradient textures even inside?

6:55pm. Let me resume.

https://youtu.be/8QIASDCh0Qw?t=462

Why are his nodes like this?

At any rate, let me pause. I am not sure I should be studying this.

https://youtu.be/yVjCdRxdm-I
Compositing In Nuke - Explainer Video

Let me watch an explainer.

7:10pm. No, this kind of work is too much for me. I do not need it. Instead...

Yeah, I need to learn texture painting at this point. I really feel like stopping for the day here though.

I am going to have to watch some tutorials on how to do it in Blender.

Nevermind that for now.

7:20pm. I am thinking

1d/2d procedural textures are out. They are too hard to deal with under the present setup. Today I got far too obsessed with figuring out gradient textures.

https://www.youtube.com/results?search_query=procedural+texturing

The 5h Rebelway masterclass has a bunch on procedural texturing at the 2:10h mark.

7:30pm. I didn't mean to start this search.

The idea I had 10m ago was - instead of doing texture painting in some program, or having to do UV unwrapping - instead of shit like that, why don't I simply paint masks?

Instead of busting my head over how to place those texture gradient I could have just selected a few points on the leaf, assigned an attribute of 1 on them, imported that in the shader and colored it. That would have been a piece of cake.

I was already introduced to this idea in the heightfield tutorial, but it was completely blasted from my mind. I just had to try digging a hole with gradient textures.

It is true that this approach will require extra geometry, but given what I want to do - illustrations and static scenes, I can definitely afford this expense. I am not making a real-time game here.

There is actually quite a lot on Youtube about proc texturing. Quite more than I expected.

Let me watch this 3m video.

https://youtu.be/Wx9vmYwQeBg
The Future of Texturing is Procedural

https://youtu.be/Wx9vmYwQeBg?t=45

Wow, this is complex.

https://youtu.be/Wx9vmYwQeBg?t=69

Substance Player is free.

https://youtu.be/Wx9vmYwQeBg?t=93

This is really cool. I bet Houdini and Blender will have plugins for this too.

I've actually been watching an ad this whole time. Andrew Price knows his business.

https://youtu.be/NjbLYFXrfFU
Why most CG metal looks fake

Let me watch this.

https://www.youtube.com/watch?v=kz-_z3wREbY
Free Masterclass: Procedural Asset Development for Environments in Houdini

This is 5h and procedural texturing is 2/3rds of it. Let me skip the 2:10h mark and I'll watch it for a bit. Actually let me watch the intro as well first.

https://youtu.be/kz-_z3wREbY?t=8263

This will be a good tutorial I can sense it. He talks about doing it in Mantra, but suggests image compositing as a better alternative. What I've been doing today is not that much different from doing the shading all in Mantra. I should definitely get familiar with COPs.

https://youtu.be/kz-_z3wREbY?t=9191

This has potential, but in practice how would one deal with UV seams?

https://youtu.be/kz-_z3wREbY?t=10063

Let me stop this here for today. I think that this course is worth watching in full. As well as the other Blender vids on top of the Youtube search. My failure today really sparked the interest in me to learn this. Though I am not really sure how much good COPs will do me - maybe I'll end up using just masks + 3d textures only. But I can't make a good decision unless I dedicate myself to learning this. I need to push on.

https://youtu.be/t1TWbcaajvM
Houdini: Baking Point Attributes To Textures

This really caught my eye. ...Let me watch this and then I will close.

https://youtu.be/t1TWbcaajvM?t=50

Houdini can load Adobe Illutrator files? It seems so.

https://youtu.be/t1TWbcaajvM?t=229

2d volume?

https://youtu.be/t1TWbcaajvM?t=476
> The underlying algorithm of Vorley noise is very similar to what we're doing here.

9:25pm. How did that trick of scattering extra points on the voronoi fracture points work.

https://youtu.be/WTg_pVZoac0?t=2003

It was Point Replicate.

9:30pm. I am thinking about painting masks, and I am changing my mind. It would work in a crutch, but it has a lot of disdvantages as well. It is not really a substitute for texture painting. I'll have to go with it as it will be easy to make use of, but it should not be my only tool.

9:35pm. It could be made to work better if the points would not get interpolated linearly, but based on distance. I'll leave this consideration for later.

9:40pm.

https://youtu.be/QZiVXcrsvPM
11 Procedural Shading Tips in Under 10 Minutes

Let me watch this as well.

https://youtu.be/QZiVXcrsvPM?t=163

These are good tips.

https://youtu.be/QZiVXcrsvPM?t=265

This is quite amazing. This is a very good video.

https://youtu.be/QZiVXcrsvPM?t=351

I would not have thought of the stuff in this video myself. This is remarkable.

https://youtu.be/QZiVXcrsvPM?t=428

He could have put in `tau` instead of `2*pi`.

10pm. https://youtu.be/9ngbOV0YKbk
Advanced Procedural Texturing

Ah, let me watch this as well.

10:10pm. No I am dead. I have no more energy for this. I've thought about it and trying to do procedural texturing as shown by Creative Shrimp would be too tedious. You really need something like Blender's smoothness to make it work. For me, getting value out of V-Ray will not be through connecting vast networks of nodes, but by making use what is already there.

Maybe I should accept triplanar projections into my heart and go with those plus the Chop nets. Getting too much into fiddling with V-Ray noise textures might end being to my detriment.

10:25pm. But just getting that example of how chop nets can be used to generate textures, and how to load them gives me a lot of capability.

With regards to attribute masks, I could get good things if I use thresholding. V-Ray does not have such a node, but I can just use remap for such a purpose."

---
## [Knuxfan24/Marathon](https://github.com/Knuxfan24/Marathon)@[590c74be3b...](https://github.com/Knuxfan24/Marathon/commit/590c74be3bda6d7fbb499d098300b77eef0b4760)
#### Wednesday 2022-03-09 22:32:35 by Knux

Stupid hacky shit for static meshes

I hate this but I don't know how else to do it because Assimp is shit.

---
## [tongjin0521/eecs464-p1-green](https://github.com/tongjin0521/eecs464-p1-green)@[e4b2ab8062...](https://github.com/tongjin0521/eecs464-p1-green/commit/e4b2ab806202e2a8e038b4db45c3577d4ba3b68e)
#### Wednesday 2022-03-09 23:33:46 by George Paul

updated myRobotRealIX.py to include plot update capabilities (see merge request where I said idk what i merged bc im a fucking idiot sorry)

---

