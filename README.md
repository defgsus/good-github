## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-02-27](docs/good-messages/2022/2022-02-27.md)


1,339,134 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,339,134 were push events containing 1,901,443 commit messages that amount to 112,408,009 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 25 messages:


## [kleinesfilmroellchen/serenity](https://github.com/kleinesfilmroellchen/serenity)@[3b8db9cc7d...](https://github.com/kleinesfilmroellchen/serenity/commit/3b8db9cc7d2d7d1db5b0bca6ad2f739f0992cbaf)
#### Sunday 2022-02-27 00:24:16 by kleines Filmröllchen

LibAudio+Userland: Use new audio queue in client-server communication

Previously, we were sending Buffers to the server whenever we had new
audio data for it. This meant that for every audio enqueue action, we
needed to create a new shared memory anonymous buffer, send that
buffer's file descriptor over IPC (+recfd on the other side) and then
map the buffer into the audio server's memory to be able to play it.
This was fine for sending large chunks of audio data, like when playing
existing audio files. However, in the future we want to move to
real-time audio in some applications like Piano. This means that the
size of buffers that are sent need to be very small, as just the size of
a buffer itself is part of the audio latency. If we were to try
real-time audio with the existing system, we would run into problems
really quickly. Dealing with a continuous stream of new anonymous files
like the current audio system is rather expensive, as we need Kernel
help in multiple places. Additionally, every enqueue incurs an IPC call,
which are not optimized for >1000 calls/second (which would be needed
for real-time audio with buffer sizes of ~40 samples). So a fundamental
change in how we handle audio sending in userspace is necessary.

This commit moves the audio sending system onto a shared single producer
circular queue (SSPCQ) (introduced with one of the previous commits).
This queue is intended to live in shared memory and be accessed by
multiple processes at the same time. It was specifically written to
support the audio sending case, so e.g. it only supports a single
producer (the audio client). Now, audio sending follows these general
steps:
- The audio client connects to the audio server.
- The audio client creates a SSPCQ in shared memory.
- The audio client sends the SSPCQ's file descriptor to the audio server
  with the set_buffer() IPC call.
- The audio server receives the SSPCQ and maps it.
- The audio client signals start of playback with start_playback().
- At the same time:
  - The audio client writes its audio data into the shared-memory queue.
  - The audio server reads audio data from the shared-memory queue(s).
  Both sides have additional before-queue/after-queue buffers, depending
  on the exact application.
- Pausing playback is just an IPC call, nothing happens to the buffer
  except that the server stops reading from it until playback is
  resumed.
- Muting has nothing to do with whether audio data is read or not.
- When the connection closes, the queues are unmapped on both sides.

This should already improve audio playback performance in a bunch of
places.

Implementation & commit notes:
- Audio loaders don't create LegacyBuffers anymore. LegacyBuffer is kept
  for WavLoader, see previous commit message.
- Most intra-process audio data passing is done with FixedArray<Sample>
  or Vector<Sample>.
- Improvements to most audio-enqueuing applications. (If necessary I can
  try to extract some of the aplay improvements.)
- New APIs on LibAudio/ClientConnection which allows non-realtime
  applications to enqueue audio in big chunks like before.
- Removal of status APIs from the audio server connection for
  information that can be directly obtained from the shared queue.
- Split the pause playback API into two APIs with more intuitive names.

Known issues/exposed bugs:
- Two processes running audio enqueues at the same time will pin the CPU
  at 100% due to both of them yield()ing all the time. See #12679.
- AudioServer hangs in driver after changing sample rate. (Probably
  already an issue before these changes.)
- SoundPlayer's BarsVisualization doesn't draw anything until you switch
  to another visualization and back again.

I know this is a large commit, and you can kinda tell from the commit
message. It's basically impossible to break this up without hacks, so
please forgive me. These are some of the best changes to the audio
subsystem and I hope that that makes up for this :yaktangle: commit.

:yakring:

---
## [DeStout/Godot4Alpha_FPS](https://github.com/DeStout/Godot4Alpha_FPS)@[830ce8563f...](https://github.com/DeStout/Godot4Alpha_FPS/commit/830ce8563f1e23cd433ef4e8a7dbcf74047fe893)
#### Sunday 2022-02-27 03:06:16 by DeStout

Initial commit, honestly kinda late. Add movement/aiming/shooting, slapper, pistol, and rifle, shot trails and bullethole decals, and enemy AI. Switched CSG level to Mesh. Add shooting SFX and music (thanks Banana).

---
## [ImFlynnn/android_kernel_realme_mt6785](https://github.com/ImFlynnn/android_kernel_realme_mt6785)@[33b422c549...](https://github.com/ImFlynnn/android_kernel_realme_mt6785/commit/33b422c549361a6bf7a2585ccac657bf50d5bcb9)
#### Sunday 2022-02-27 08:29:24 by Wang Han

power: Introduce OnePlus 3 fingerprintd thaw hack

Taken from Oneplus 3, this hack will make fingerprintd recover from suspend quickly.

Small fixes for newer kernels since we're coming from 3.10.108..

Change-Id: I0166e82d51a07439d15b41dbc03d7e751bfa783b
Co-authored-by: Cyber Knight <cyberknight755@gmail.com>
[cyberknight777: forwardport and adapt to 4.14]
Signed-off-by: Shreyansh Lodha <slodha96@gmail.com>
Signed-off-by: Pierre2324 <pdbbasketball@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>
Signed-off-by: Dhruv <dhruvgera61@gmail.com>
Signed-off-by: Cyber Knight <cyberknight755@gmail.com>
Signed-off-by: ImFlynnn <ahmadzaid13.az@gmail.com>

---
## [Evolution-X/frameworks_base](https://github.com/Evolution-X/frameworks_base)@[f5cdac7aab...](https://github.com/Evolution-X/frameworks_base/commit/f5cdac7aab09d67afa3e123e3423d96654cedca3)
#### Sunday 2022-02-27 08:31:42 by Joey Huab

core: Refactor Pixel 2021 features availability and PixelProps spoofing

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

* Restrict Pixel 2021 features to Oriole and Raven.

* Set Pixel 5 as spoof for more Google apps that
  uses TPU when spoofed as Pixel 6.

* Default Pixel 5 spoof for Photos and only switch
  to Pixel XL when spoof is toggled.

* Pixel Buds has been reported to crash on Pixel 6 spoof
  so move it to Pixel 5.

* Keep Google Translate to Pixel 5 as it's not really as
  used as the others.

* We will try to bypass 2021 features and Raven
  props for non-Pixel 2021 devices as apps usage
  requires TPU.

---
## [crdroidandroid/android_kernel_oneplus_sm8250](https://github.com/crdroidandroid/android_kernel_oneplus_sm8250)@[0d18937dc2...](https://github.com/crdroidandroid/android_kernel_oneplus_sm8250/commit/0d18937dc27e4cb23e11b3685732a2ad97482674)
#### Sunday 2022-02-27 08:59:43 by alk3pInjection

disp: msm: Handle dim for udfps

* Apparently, los fod impl is better than udfps cuz it
  has onShow/HideFodView hook, which allows us to toggle
  dimlayer seamlessly.

  Since udfps only partially supports the former one,
  we'd better kill dim in kernel. This is kinda a hack
  but it works well, bringing perfect fod experience
  back to us.

Co-authored-by: Art_Chen <Chenxy0201@qq.com>
Signed-off-by: alk3pInjection <webmaster@raspii.tech>
Change-Id: I80bfd508dacac5db89f4fff0283529c256fb30ce

---
## [BlackSilverUfa/data](https://github.com/BlackSilverUfa/data)@[a28a738e2e...](https://github.com/BlackSilverUfa/data/commit/a28a738e2e48b233a28e076f04d44fa56cf8520b)
#### Sunday 2022-02-27 09:26:22 by Jenkins

Запись стрима 1307474557

* Daymare: 1994 Sandcastle — 2 [100%]
* Прохождения за один стрим — Little Orpheus - Episode 1 [100%]
* Первый взгляд 2022 — The Bridge Curse: Road to Salvation (демо) [100%]
* Первый взгляд 2022 — My Friendly Neighborhood (демо) [100%]
* Первый взгляд 2022 — SCP: Pandemic (демо) [100%]
* Первый взгляд 2022 — IXION (демо) [99%]

---
## [AllyMarthaJ/mcm4csharp](https://github.com/AllyMarthaJ/mcm4csharp)@[9133ee8f46...](https://github.com/AllyMarthaJ/mcm4csharp/commit/9133ee8f46df49e03532e676cc764124241f6692)
#### Sunday 2022-02-27 10:02:28 by AllyMarthaJ

Note to self, Ally sucks at coding at night. Debugging + fixes.

---
## [Aerotinge/CleanSlate](https://github.com/Aerotinge/CleanSlate)@[2c02e01a37...](https://github.com/Aerotinge/CleanSlate/commit/2c02e01a37790f62f4d5225ed4320e172d6de4fc)
#### Sunday 2022-02-27 10:15:26 by SuccinctScrivener

Events DeMTTHed

Almost all MTTH events that aren't achievement, plot, health, job, or province events have been edited to no longer use MTTH.

base_achievement_events.txt
Potentially fixed issue with flags not getting cleared in steam.026 (CleanSlate error)

base_crusade_events.txt
Some Catholic-only crusade events expanded to include Fraticelli

base_family_events.txt
Relatives who marry in event 37056 'Relative who was denied marriage ambition decides to marry in secret' now marry matrilineally if female

base_hedge_knights_events.txt
All five of the 'hedge knights visiting' events may fire now, rather than just the one where they injure themselves

base_legends_events.txt
Changing your mind about how you want to close the gates of hell no longer terminates the event chain

base_lifestyle_events.txt
Improved the selection of an appropriate love interest in event 5030 'Duelist/Poet - start'.
Fixed event 5035 'Write poems for your love interest' taking ~7 times longer to fire than it should.
Fixed the event chain to become a faqih taking ~7 times longer to complete than it should.
Fixed characters getting permanently locked out of lifestyle trait event chains when they fail a non-muslim lifestyle event chain.
Fixed event 5064 'Stay strong in the face of temptation' not firing for buddhists with the ambition to rid themselves of lustful unless they are also in the middle of a lifestyle event chain.
Fixed event 5064 'Stay strong in the face of temptation' taking 5 times as long to fire if you were in the hedonism/celibacy lifestyle event chain but also had the buddhist ambition to rid yourself of lustful.

base_lovers_events.txt & wol_lover_events.txt
Fixed events that were supposed to cause a character to break up with a particular lover not causing them to break up at all or to break up with a different lover.
Fixed a bad condition preventing event 64100 'lover comforts you after row with wife' from ever firing.

base_mongol_events.txt
Random turkic invasions now actually random

base_religious_events.txt
A number of religious events can now be performed by antipopes as well as popes
Restored option for Catholics to banish heathen advisors in response to papal pressure in event 39241, like in the Orthodox version of the event
Event 39401, 'Pope disappointed about allowing heresy', now actually waits at least 2 years to fire, as indicated by the description

base_teutonic_order_events.txt
Choosing to not donate land to the Teutonic Order at the moment no longer permanently prevents the Teutonic Order from asking for land.

base_traits_effects_events.txt
Fixed a bad condition on event 3520 'Break celibacy for your spouse' that prevented it from ever firing

hl_raiding_adventurers_events.txt
Fixed HL.100, 'Character without inheritance becomes adventurer', firing only 15% as often as in vanilla (CleanSlate error)

soi_hashshashin_order_events.txt
The Hashshashin 'kill a ruler who is at war with them' event, event 88020, can now fire for the ai, as was probably intended.

soi_muslim_honorary_titles_events.txt
Iddah period before divorce corrected from 30 days to 130 days
Fixed cooldown being added to the wrong character in event 105050 'Court Calligrapher is asked to decorate the mosque'
Lovers breaking up in the zina event chain now takes into account the Way of Life DLC
Zina event chain can no longer fire more than once at a time for a character.

soi_on_hajj.txt
promise_hajj flag now cleared from characters when asked to go on hajj by another character

soi_polygamy_events.txt
Only playable characters or their spouses will now receive most polygamy events
Most polygamy events opened up to characters of non-muslim religions with polygamy

---
## [sarcoph/Hyper-Station-13](https://github.com/sarcoph/Hyper-Station-13)@[5d96c13de2...](https://github.com/sarcoph/Hyper-Station-13/commit/5d96c13de288fd1d735a392ceffd991d7ecc17f2)
#### Sunday 2022-02-27 10:32:04 by sarcoph

holy fucking shit i am so tired of refactoring

to do list:
- ensure all useBackends use context instead of props
- ensure all uis that need it get their `{ act, data, config }` from useBackend(context)
- fix the rest of the bugs

i do not have the energy for this.

---
## [carshalash/tgstation](https://github.com/carshalash/tgstation)@[1f23d3d7ad...](https://github.com/carshalash/tgstation/commit/1f23d3d7ad87eebf74b1c9dc51867c5c21edf547)
#### Sunday 2022-02-27 11:42:02 by Jeremiah

Should fix shuttles leaving without sections(#64764)

Should(tm)

This was a suggestion by @Mothblocks and it seemed easy to implement

Fixes #64546 (Icebox evac will sometimes leave without sections)
Fixes #64653 (You might have fixed the kilo whiteship by making it move, but you didn't fix all of it)

Uh people won't just randomly get yeeted into space with half of a shuttle.
Kinda funny for people watching but not if you die of pressure loss or get stuck on the station
Runtime man bad

(Sleeping in here in general is like admitting that we're ok with missing a few atoms, which is what this runtime is. S just missing is better then overtime. Supposedly --Lemon)

---
## [DexterHuang/CyberCodeOnline](https://github.com/DexterHuang/CyberCodeOnline)@[f9fd302bd7...](https://github.com/DexterHuang/CyberCodeOnline/commit/f9fd302bd7f43a7a693c1ae306071bea3ef64344)
#### Sunday 2022-02-27 12:48:56 by Lance0-32

Update tips.txt

haha guys exp memories guys (they stopped existing)

also deixtoria thank your for the new facts about enemy XP NOW PLS STOP TALKING ABOUT IT BECAUSE I MADE THIS TIP AND IT'S CAUSING EMOTIONAL DAMAGE WHICH WAS VERY EFFECTIVE. (they didn't actually talk about it that much I'm overdramatizing lmao)

and some things that somehow slipped by people, myself included. WAIT I SHOULD'VE JUST DONE THE "some changes joke" ;-;

guess I'll do it for the additions, which are:
some changes

---
## [Project-Awaken-Twelve/android_packages_apps_Launcher3](https://github.com/Project-Awaken-Twelve/android_packages_apps_Launcher3)@[ae0ecb3a23...](https://github.com/Project-Awaken-Twelve/android_packages_apps_Launcher3/commit/ae0ecb3a234c884e74d85adea9c26f5335176147)
#### Sunday 2022-02-27 12:58:27 by Alex Cruz

Launcher3: Restart with change only on exit

This change allow the user to change everything they have to inside the
homescreen activity and only restart on exit. Previously this was a pain
in the fucking ass because you had to go in and set each option one by one
with a restart inbetween. At least now is not that big of a pain.

- Restart on destroy (hitting the back button, actionbar arrow)
- Restart when a chance is made and the home button is pressed

** Thanks "Jack" for code to detect home button
https://stackoverflow.com/a/27956263

- Cleaned up restart code

eyosen adapted to 10

Change-Id: I4962916ae0bd59d08247b59de585a97a2b9da3a1

---
## [rphsoftware/OneLoader](https://github.com/rphsoftware/OneLoader)@[d2177d768a...](https://github.com/rphsoftware/OneLoader/commit/d2177d768ad4dd7c0e5ac169d8d5b93dea6846c2)
#### Sunday 2022-02-27 13:24:27 by Rph

Fixes to zip handling.
Thanks to @NUMBER1LIFEJAMGUYFAN for finding this bug.

Fuck you @NUMBER1LIFEJAMGUYFAN for finding this bug.

---
## [mvaisakh/oneplus7](https://github.com/mvaisakh/oneplus7)@[75a1e2d6b0...](https://github.com/mvaisakh/oneplus7/commit/75a1e2d6b0cfe2462d1032163ec14f76236c2bcc)
#### Sunday 2022-02-27 16:19:52 by Peter Zijlstra

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
## [taydev/compendium](https://github.com/taydev/compendium)@[2931d8f7a9...](https://github.com/taydev/compendium/commit/2931d8f7a9b7eec3e83d5528e8f89bca4ae7fff2)
#### Sunday 2022-02-27 17:28:31 by Tay B

what's that one saying? "work smarter, not harder"?

- Migrated Core to Kotlin. (+ deleted Java stuff from Core, replacing it with Kotlin equivalents)
  - I don't know how to write Kotlin, but we're learning on the job :)
  - Also, thank you @binaryoverload for the suggestion <3
    - My boilerplating pains have been greatly reduced.
- Project-wide reformat, as per usual. Force of habit. A habit I really need to break.
  - Also, there's this button called "Rearrange Entries". I might have clicked it.
    - Me clicking it might have been a massive problem. Having to rearrange pom files manually is painful.
    - "Why not just ctrl-z and reverse it?" I didn't know how badly it screwed things up. :')
- Slightly modified .gitignore to make VSCode happy.
- Added all of the Spell boilerplate.
  - Also known as "a lot of boilerplate".
  - Honestly, I'm contemplating using Spring for the API just to save myself from having to rewrite all of that boilerplate.
- Added tests!
  - TDD seems cool, but not the direction I wanna go with this at the moment since it's mostly just creating boilerplate from JSON dumps. Maybe another time.

Also, I'm debating on not using MongoDB. FaunaDB looks cool. Might use that and learn something new.

---
## [WarswordConquestTeam/Warsword-Conquest](https://github.com/WarswordConquestTeam/Warsword-Conquest)@[7c3475b1b6...](https://github.com/WarswordConquestTeam/Warsword-Conquest/commit/7c3475b1b671aaeface79650d20d054bb4d06e57)
#### Sunday 2022-02-27 18:31:08 by Marshal

Sourthlands Edition 2021

same as the ModDB version but with a little extra stuff.

Changelog:

Wight blade effect no longer works on hero characters
Fixed half health after battle bug
Included fix for endless spawn bug for champion mode
Fixed siege teleportation bug
Bearmen of Urslo buffed
TLD archer aim fix added
Empire halberdiers have proficiency increase, small power strike increase, thrust damage increase to all empire halberds
Wolf kin and wolf brother have proficency increase
Knights of the white wolf given helmets
Massive agility increase for flagellants and given unbreakable
Power strike buff for Helhuntens
Marauder champions and berserkers get proficiency boost
Big proficiency boost for pit kings
Dark Elf executioners given killing blow
Ranged line in VC tree are now all archers
One handed wight blade killing blow reduced to 1 in 8 chance
Agility increase to Counts champion
Slight increase to some bastard weapon speed.
Curing the plague via potion will now give stats back
Gloves added to high tier dwarf infantry
Multiple small stat increases to high level chaos troops
Proficiency boost to marauders
Proficiency boost to daemon princes
Armour increase to saurus.
Proficiency increase to saurus and agility increase to high level saurus.
Javelins added to skink riders
Slight increase to Bretonnian armour
Bastard swords and picks removed from men at arms weapon options.
Slight buff to high level dark elf strength
Reduction in samurai power draw
Undeath staff does not count as shield now for Ryze and Sulekhim
Bug where factions reseige a location they have just taken should be fixed.
Activities menu now available in castles for upgrades and garrison option.
Guildmaster can now buy your cattle direct so long as the herd is close by.
Swing speed of dwarven 2 handed axes increased.
All 3 magic skills increased max to 15
Bironas timewarp radius drastically increased.
Enchanted blades of aiban now increases accuracy of firearms too.
Increased chance of final transmutation being successful
Sir Aristide now has the 'blessing of the lady' regeneration ability.
Death frenzy now buffs damage as it should(instead of speed)
Pestilent breath now triggers more hits
Riding a horse now decreases dodge chance by 30%
Iron skin now offers damage protection instead of ignore pain.
Runes should now work properly in dungeons
Curse of the genie affect doubled
Chaos dwarf arenas fixed
New music for battles, dungeons, undead pirates and dwarven lands by Jalrick
Magic missiles now do bonus damage against shields.
Cult masters and humanitarians will now take villagers from prisoners as well as party.
If you have ignore pain the nurgle lore attribute will go straight to advanced ignore pain.
Skinks now have dodge

New UI

Horned ones are now faster than cold ones.
Magic resistance cost increased.
Dwarves have one handed axes and hammers lengthened
Music track added for last dungeon room
New music for battles and dwarven lands
New weapons for orc boar riders
Fixed issue where runic weapons would not work for dwarf companions
Fixed runic blunderbus
Cost of ships increased
Desert lore fixed and new aoe added.
Mounts rebalanced.
Fixed curse of the horned one spell in plague
Ice guard added to Kislev as retinue troop
Money lost in random events has been capped
Good and economy rebalance for some of the factions

Kislev weaponsmith fixed
Bears made to the right scale
Bolts added to tomb kings
Araby horsemasters given their bows in battle.
Tweaks to VC shield quality among troops and shields added to weaponsmith.
Slight increase to orc archer power draw
Summoned weapons now remain until unequipped
Fire particles should now disappear from flamed weapons when unequipped.
Fixed boon of tzeentch cancellation script
It is now 'z' to brace a spear
Celestial mages now ignore lightning storm event
Fixed an issue where poisoned globes would still poison those who should be immune
Invocation of Nehek increased in mana cost and cooldown time.
Fixed Kislev character creation stats
Split poisonous into venomous and poisonous.
Curing potion will now make you immune to venom and poison for a period of time after drinking (based on constitution)
Due to skink conflict (and that they wear no metal) plague of rust and arcane unforging will not work on goblins and skinks
Ice magic lore attribute now regenerates in battle in snowy terrain as well as the map.
Made changes which should help solve resiege civil war bug

New vampire faces by Kraggrim
Dungeon room fix by Kraggrim
Blunderbus and shotgun range reduced
Mighty blow, damage runes and special weapon effects and some magic effects will now work against mounts
Life, vampire and Qhash lore attributes will only work if an appropriate troop was affected
Qhasyh lore attribute will now stack with any ward save you have up to maximum of 2+
Fixed issue where burning head thinks it failed when it hits
New potion ui (where you place them in inventory now no longer matters)
Magic and potions should now work on the streets scene of sieges
Amber, Jade, desert, vampire, qhaysh, gold, grey, light and orc schools have staffs added
Fixed an issue where you could not remove dungeon companions if you have more than one disabled
Magic users in dungeons restricted
More loot in end chest with main item. Increased difficulty means more items.

Bank associate added so players can access treasury anywhere and also set up one before becoming a lord/king
Many companions stats changed
High persuasion will now reduce the rtr, renown, relation and reputation requirements for lords of your race/faction joining your kingdom

Your riding skill now needs to be 2 levels above your mounts riding difficulty to qualify for guaranteed casting.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[5706234e2a...](https://github.com/mrakgr/The-Spiral-Language/commit/5706234e2ad576399ca59fa9faf3d96bb7a99479)
#### Sunday 2022-02-27 19:13:08 by Marko Grdinić

"11:10am. I went to bed a bit earlier, but had trouble falling asleep which cancelled it out. This is the usual for me.

Let me chill a bit and then I will start with the heightfields.

11:40am. Let me restart. I had my bit of fun. Let me finish the first biome video.

11:50am. Ah, in the distort example, it does not move because distort acts in a multiplicative manner. That is the only answer.

12:35pm. Done with 03.

> Heightfields are limited to 2D axis, but I will show you a trick in which you can get overhang details! We do some post-processing and keep the details to the lava bits, but you can at least keep this trick in the bag and know that you can get interesting results from tuning the noise types and settings!

This is what the description says for 06. You can get overhand with height fields? That seems quite interesting.

The next lesson is on textures this should be of interest to me for my own scene. I should not ignore COPs.

The more I learn, the more capable I will be down the road. Playing around is necessary, but only when I support it through learning from others. That is when my effectiveness will be maximized. So what if I am not working on my own project right now. Later I will do so much that it will last me for an eternity.

12:45pm. It is surprising that COPs do not have their own ramp in there somewhere.

I bet I'd find one if I looked.

1:05pm. Let me stop 04 at 19m. It is time for breakfast. This tutorial series is good. It gives me a lot of possibility for creating terrains in the future.

Today my goal will be to go through at least half the playlist. The videos seem to be 30m long on average, so it should be doable.

3pm. Letm me resume. It seems that the break took just as long as usual. For the next 5h it is only lectures for me. I'll get them out of the way today.

3:10pm. I do not like the indirect approaches like this. If I had to get the light I'd rather just do that directly using mask from feature.

...Though who knows if it would work on height fields. Maybe height fields have something specifically for that. It would not surprise me if they did.

3:20pm. The way he is doing the texturing in the COP is something that I could not even imagine doing.

3:40pm. Done with 04. What he did would be really hard to immitate. Artists always go overboard with fiddling around. But I got the gist of it.

This lecture was 50m long. Thankfully the next one is only 12m. Let me watch it.

My focus is low, but should go up once I start doing my own things.

4pm. Instead of moving on to 06, let me move onto the rendering part for the dusty biome - 11.

That should be instructive. Let me see how he does his thing.

4:10pm. So he is using displacement. I've checked and it is possible to straight up convert the heightfield to a polygon and other volumes.

4:20pm. 14m in. I am nearly done with the shading part. But I think he is doing the process wrong. He did a shitload of work during texturing, but only now he is doing the actual lookdev which is a mistake. If it was possible, it would have been a lot better to constantly look at the final render to see how good it would be. Just what is fiddling with 2d textures for 50m without looking at the final render going to do?

4:25pm. Let me take a break so I can read Ayakashi.

4:50pm. Let me resume. Time for the Fiery Biome. These lectures are both under 20m.

5:10pm. Now come the textures for the Fiery Biome. 10m unlike for the previous one which was 50m.

But at least, the one thing I gained from that is that I started thinking about image compositing more seriously. I wouldn't do it the same as him, I'd try a more straightforward way, but if I had no watched this video even trying it at all would have been the furthest thing from my mind.

5:30pm. Let me study the rendering parts for the fiery biome. That will leave the icy for last.

5:50pm. Oh, wow, the fiery biome looks great. I'd never have guessed it based on the intermediate steps. Lookdev is messed up in Houdini.

But for the sake of texturing you can really do a lot with masks. Masks are the most important part.

Let me watch it again, I want to pay attention to what he did for roughness.

5:55pm. Let me take a short break.

6pm. Masks, not color are the secret ingredient to texturing. Once you have the masks you can use color ramps to get the color. I knew this for a while now.

Let me rewatch the last part of the CHOP2 work for the fiery biome. I want to see how he gets the roughness again. Also I have no idea why he using that grid pattern, but it does not matter.

6:10pm. Ok. Let me watch the Icy Biome stuff.

6:20pm. 5:45m in. Adding this much terracing is crazy. He lost all the original detail, just what is he thinking? If he wanted to do this he should have started from this step.

6:55pm. I really isn't a good idea to try to replicate his texturing workflow directly. A proper workflow would always be looking at the final output and making gradual changes.

Uah, I am tired of this. When is lunch?

7:05pm. I'll fit in the time to watch the last two vids after I am done eating here.

7:45pm. Done with lunch. Let me watch the tree video.

7:50pm. Nevermind, I have no will for this. What I've learned should be more than enough. Tomorrow, I am going to use the density VDB to put those floating tiles where I want them. Then I am going to check out the USD imports and exports. After that I'll start on the shading parts. It is about time to wrap up the work on the scene so I can get back to sculpting.

Months ago, I wanted to do simple backgrounds for a VN, but my ambition has grown significantly since then. And so have my abilities.

https://docs.blender.org/manual/en/latest/render/shader_nodes/input/texture_coordinate.html

I think I can imagine what each of these options does. I actually couldn't figure it out based on the descriptions last time I was on this page, months ago, but now I only don't know what the Reflection mode does, and maybe Camera. The rest I can imagine. I'd have to test my theory though, but it should be right.

8:05pm.

* Check out how USD imports/exports work.
* Get started with work on shading.

Let me order the priorities like this. Figuring out the imports and exports will not take me longer than 10m anyway.

Now let me have some fun.

At this point I think I have a very broad overview of Houdini and I've learned a lot about how to manipulate geometry in it. I still do not know a lot about it, and this includes geometry as well, but I know just enough to start getting confident. Going forward, I should be quite effective at it.

8:10pm. What I have to do is prove that. And I have the full intention of doing that."

---
## [TARKZiM/android_kernel_htc_msm8952](https://github.com/TARKZiM/android_kernel_htc_msm8952)@[ac2825b5a3...](https://github.com/TARKZiM/android_kernel_htc_msm8952/commit/ac2825b5a3568f4d4a369840ea17cc731d38873e)
#### Sunday 2022-02-27 19:39:29 by Masahiro Yamada

modpost: file2alias: go back to simple devtable lookup

[ Upstream commit ec91e78d378cc5d4b43805a1227d8e04e5dfa17d ]

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
Signed-off-by: Sasha Levin <sashal@kernel.org>
Change-Id: If4290e58a2c34a7f69e2aa8e9ec0b07f15792d21

---
## [Leo2323232/MARDEK-Leos-Mod](https://github.com/Leo2323232/MARDEK-Leos-Mod)@[7619b007d8...](https://github.com/Leo2323232/MARDEK-Leos-Mod/commit/7619b007d8d05e5e32d911f83324571cf9fa0da6)
#### Sunday 2022-02-27 20:21:02 by Leo2323232

karnos prelim changes

mp 999 to 100
atl 70 to 60
str 80 to 90
starts with regen and double shields
removed all mana costs with stated exceptions
added cleave 0.9xatk hits all targets, no split
shock used as regular melee skill, can crit
enhancement changed to +10str, +5 vitality, +3 spirit, +5 agility, +3 def, +3 mdef, +3 atk
invigoration from 150 to 300 power
shatter claw 200 power to 2xatk
bisect 120% hp damage to 150%, accuracy 90 to 100
basic melee skills 1.2xatk to 1x
uses thunderstorm when air

both p and m counters changed to 15% smite evil, 17% dark claw, 19% blood claw, 21% shock, 23% bisect, 25% cleave,100% elemental shift

---
## [xKoZa/ConnGa](https://github.com/xKoZa/ConnGa)@[2c99d9201f...](https://github.com/xKoZa/ConnGa/commit/2c99d9201f0a2f7737bd57918617f6e42bdbe796)
#### Sunday 2022-02-27 20:28:18 by xKoZa

Finished friend list

I think this time I'm dying
I'm not melodramatic
I'm just pragmatic beyond any
Reasoning for thinking I've got ###### rabies or something
I think this time I'm dying
I think this time I'm dying
I think I've lost my mind
Blurring the fact and the fiction
Whilst simultaneously fixing
Myself up with a girl named Panadol
Bite the tablet, elixir
Disintegrate, mouth's a mixer
I think I've lost my mind
I think I've lost my mind

---
## [chrmhoffmann/android_kernel_google_wahoo](https://github.com/chrmhoffmann/android_kernel_google_wahoo)@[a57c475309...](https://github.com/chrmhoffmann/android_kernel_google_wahoo/commit/a57c4753090f1c08c321f6b373d44835aed5e793)
#### Sunday 2022-02-27 21:04:28 by Maciej Żenczykowski

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
## [RojjaCebolla/crawl](https://github.com/RojjaCebolla/crawl)@[a852ce8369...](https://github.com/RojjaCebolla/crawl/commit/a852ce8369264a3a4759b99df0bbba7645a78c97)
#### Sunday 2022-02-27 22:06:52 by Nicholas Feinberg

Play with ranged weapon stats more

Following some thinking about ranged weapons, here's a new set of
ammoless stats. Philosophy:

- Slings are high-skill 1-handers. Hunting slings are vaguely like
  war axes, and fustibaluses are no longer ultra-rare but are now
  more like broad axes.
- Bows are high-skill 2-handers.
- Crossbows are lower-skill - it takes fairly little to get the hand
  crossbow or the arbalest to mindelay. The triple crossbow is still
  high-skill, but it's quite rare, so doesn't define the 'feel' of
  the class, much as you can't rely on finding a triple sword as a
  lbl user or an exec axe as an axe user. (Unless a gifting god gets
  involved.)

If we're going to keep all these item classes, it would be great to
have some more obvious and pronounced gimmicks. I suspect we'll end
up merging or removing some of these at some point, but that's a
larger project than I'm ready for right now.

TODO: make fustibali spawn at a higher rate - right now they're about
1/5th as common as I'd like.

---
## [awesomeusername69420/meth_tools](https://github.com/awesomeusername69420/meth_tools)@[d544be9b79...](https://github.com/awesomeusername69420/meth_tools/commit/d544be9b798b3cc61d1e3a9cb14eb0f32fc6de68)
#### Sunday 2022-02-27 22:27:11 by awesomeusername69420

Update 3d_penetration_crosshair.lua

using CalcView to get EyePos and EyeAngles because meth breaks EyePos fuck you wolfie fuck you fuck you fuck you fuckyou fuckyoufuckyou

---
## [AkiraNoSushi/kernel_cherry_sdm439](https://github.com/AkiraNoSushi/kernel_cherry_sdm439)@[837dbc0d67...](https://github.com/AkiraNoSushi/kernel_cherry_sdm439/commit/837dbc0d673f53d22049d96320da66ccaa06025b)
#### Sunday 2022-02-27 23:40:14 by Angelo G. Del Regno

Merge: Performance improvements.

This patchset brings some performance improvements and the addition of the LZO-RLE
algorithm to the kernel, also usable in zram (yup, tested, works but LZ4 is still ok for us).

The main performance improvement is for SWAP space: the locking has changed and
the swap cache is now split in 64MB trunks.
This gives us a reduction of the median page fault latency of 375%, from 15uS to 4uS,
and an improvement of 192% on the swap throughput (this includes "virtual" swap
devices, like zRAM!). The real world user experience improvement of this on a mobile
device is seen after a day or two of usage, where it usually starts losing just a little
performance due to the large amount of apps kept open in background: now I cannot
notice any more performance loss and the user experience is now basically the same as
if the phone was in its first 2 hours of boot life.

Other performance improvements include, in short:

    UDP v4/v6: 10% more performance on single RX queue
    Userspace applications will be faster when checking running time of threads
    2-5% improvements on heavy multipliers (yeah, not a lot, but was totally free...)
    Improvements on rare conditions during sparsetruncate of about 0.3% to a
    way more rare around 20% improvement (that's never gonna happen, but there
    is no performance drop anywhere).

Tested on SoMC Tama Akatsuki RoW

This was taken from
Repo:
https://github.com/sonyxperiadev/kernel
PR: 2039 ([2.3.2.r1.4] Performance improvements)

Signed-off-by: sweetyicecare <gabrielseedev@outlook.com>
Signed-off-by: Jprimero15 <jprimero155@gmail.com>
Signed-off-by: Joel Gómez <nahuelgomez329@gmail.com>

Conflicts:
	mm/swapfile.c
	mm/swap.c

---
## [TaoK/git](https://github.com/TaoK/git)@[0b5d478951...](https://github.com/TaoK/git/commit/0b5d47895120539d6a72a91398f33a0e33df7cd5)
#### Sunday 2022-02-27 23:52:06 by Tao Klerks

merge: new autosetupmerge option 'simple' for matching branches

With the default push.default option, "simple", beginners are
protected from accidentally pushing to the "wrong" branch in
centralized workflows: if the remote tracking branch they would push
to does not have the same name as the local branch, and they try to do
a "default push", they get an error and explanation with options.

There is a particular centralized workflow where this often happens:
a user branches to a new local feature branch from an existing
upstream branch, eg with "checkout -b feature1 origin/master". With
the default branch.autosetupmerge configuration (value "true"), git
will automatically add origin/master as the remote tracking branch.

When the user pushes with "git push", they get an error, and (amongst
other things) a suggestion to run "git push origin HEAD". Eventually
they figure out to add "-u" to change the tracking branch, or they set
push.default to "current", or some tooling does one or the other of
these things for them.

When one of their coworkers works on the same branch, they don't get
any of that weirdness. They just "git checkout feature1" and
everything works exactly as they expect, with the shared remote branch
set up as remote tracking branch, and push and pull working out of the
box.

The "stable state" for this way of working is that local branches have
the same-name remote tracking branch (origin/feature1 in this
example), and multiple people can work on that remote feature branch
at the same time, trusting "git pull" to merge or rebase as required
for them to be able to push their interim changes to that same feature
branch on that same remote.

(merging from the upstream "master" branch, and merging back to it,
are separate more involved processes in this flow).

There is a problem in this flow/way of working, however, which is that
the first user, when they first branched from origin/master, ended up
with the "wrong" remote tracking branch (different from the stable
state). For a while, before they pushed (and maybe longer, if they
don't use -u/--set-upstream), their "git pull" wasn't getting other
users' changes to the feature branch - it was getting any changes from
the remote "master" branch instead (a completely different class of
changes!)

Any experienced git user will presumably say "well yeah, that's what
it means to have the remote tracking branch set to origin/master!" -
but that user didn't *ask* to have the remote master branch added as
remote tracking branch - that just happened automatically when they
branched their feature branch. They didn't necessarily even notice or
understand the meaning of the "set up to track 'origin/master'"
message when they created the branch - especially if they are using a
GUI.

Looking at how to fix this, you might think "OK, so disable auto setup
of remote tracking - set branch.autosetupmerge to false" - but that
will inconvenience the *second* user in this story - the one who just
wanted to start working on the feature branch. The first and second
users swap roles at different points in time of course - they should
both have a sane configuration that does the right thing in both
situations.

Make these flows painless by introducing a new branch.autosetupmerge
option called "simple", to match the same-name "push.default" option
that makes similar assumptions.

This new option automatically sets up tracking in a *subset* of the
current default situations: when the original ref is a remote tracking
branch *and* has the same branch name on the remote (as the new local
branch name).

With this new configuration, in the example situation above, the first
user does *not* get origin/master set up as the tracking branch for
the new local branch. If they "git pull" in their new local-only
branch, they get an error explaining there is no upstream branch -
which makes sense and is helpful. If they "git push", they get an
error explaining how to push *and* suggesting they specify
--set-upstream - which is exactly the right thing to do for them.

This new option is likely not appropriate for users intentionally
implementing a "triangular workflow" with a shared upstream tracking
branch, that they "git pull" in and a "private" feature branch that
they push/force-push to just for remote safe-keeping until they are
ready to push up to the shared branch explicitly/separately. Such
users are likely to prefer keeping the current default
merge.autosetupmerge=true behavior, and change their push.default to
"current".

Signed-off-by: Tao Klerks <tao@klerks.biz>

---

