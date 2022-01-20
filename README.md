## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-01-19](docs/good-messages/2022/2022-01-19.md)


1,868,457 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,868,457 were push events containing 2,911,937 commit messages that amount to 236,419,047 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 35 messages:


## [liammcd/crawl](https://github.com/liammcd/crawl)@[070a2a64fb...](https://github.com/liammcd/crawl/commit/070a2a64fb29b2c910b5e7a89e561f090fa03f63)
#### Wednesday 2022-01-19 00:04:25 by Kate

Allow demons and holies to be feared/berserked

As part of an effort to reduce the number of effects that are restricted
to natural monsters only, to increase some of the distinctions between
undead/demonic/nonliving holinesses, and to allow some more flavourful
interactions.

Lore-wise, demons and holies are supposed to be of similar stock aside from
their god alignment, so are grouped together here. They're also established
to be like living creatures in a number of ways - they're generally
intelligent, can be poisoned, and have souls, so it feels appropriate for
them to feel emotions in some way and be able to go berserk and be feared.
(Importantly this also allows the zealot's sword to send divine allies
berserk, for any TSO worshippers who happen to find it.)

---
## [Dimensions-Softwares/project-destiny](https://github.com/Dimensions-Softwares/project-destiny)@[0e5aab0325...](https://github.com/Dimensions-Softwares/project-destiny/commit/0e5aab0325677a8570dbbc17a6d0f6c3cd9c2c22)
#### Wednesday 2022-01-19 00:09:16 by Only Void

Tried to deleted reusable workflows to see if it's the problem

God i hate my life

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[eb384bd2d7...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/eb384bd2d72a5b23dd9785cc06815049d507d3d5)
#### Wednesday 2022-01-19 00:21:10 by Useroth

Telemetry 'n shit (#10810)

* Refactors dbcore and limits the maximum amount of concurrent async queries to a variable amount (#59676)

Refactors dbcore to work off a subsystem if executed async and limits the maximum amount of concurrent async queries to 25.

This has been tested locally on a mysql docker image and there were no crashes (as long as you didn't run it with debug extools) + data was getting recorded fine.
Why It's Good For The Game

May or may not resolve terry crashes, however, each query creates a new thread which takes up 2mb, preventing the game from using that 2mb. This can lead to ooms if they stack up, e.g. due to poor connectivity. This solves that issue.

maintainer note: this did not actually resolve the crashes, but has value anyway. Crashes were sidestepped fixed by finding out Large Address Awareness works

cl
refactor: Refactors dbcore.dm to possibly resolve the crashes that happen on Terry.
/cl

* Fixes an oversight in database code and cleans up telemetry (#64177)

As it is right now, we never actually clear the temporary list processing_queries
So if the subsystem is for some reason unable to complete a run, we will just whip right back around to it again
If it's been long enough, this could even cause horrific log spam. There was just now a manuel round with roughly 30k undeleted query errors. not good.

But what was actually not deleting you may ask?
Well

When you create a db request, a 5 minute timer starts. after those 5 minutes are up, the request is qdeleted by the db subsystem
This is to prevent the creation of unused requests, and to handle requests that are never cleaned up

Telemetry code was creating all of its db requests inside a for loop that could check tick, and then later
attempting to call them in series

Since requests by default sleep, this almost always lead to undeleted queries, which harddel'd given long enough periods

I've fixed this by moving the data gathering away from the query creation
Why is it good for the game

I was working on atmos code, happy, safe in my delusion, when suddenly I got a ping from tattle freaking out over 200 undeleted queries a second
This resolves that issue, so I can once again live in peace
Changelog

cl
admin: Telemetry code will spam you with undeleted query logs much less often now!
server: Improved how the db subsystem handles undeleted queries, should never have an incident like that again
/cl

* Fixes an error in telemetry queries (#64205)

* Hardsynced time_track.dm with upstream

Co-authored-by: Watermelon914 <37270891+Watermelon914@users.noreply.github.com>
Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [tjstansell/terraform-provider-cloudflare](https://github.com/tjstansell/terraform-provider-cloudflare)@[7dc1827e5f...](https://github.com/tjstansell/terraform-provider-cloudflare/commit/7dc1827e5f785898adcf04cb796c0710072c64ff)
#### Wednesday 2022-01-19 00:49:04 by Jacob Bednarz

resource/cloudflare_ruleset: improve dashboard collisions

One of the earliest niggles with customers coming from the dashboard to
Terraform was the collision caused by a Ruleset phase being created in
the UI but the Terraform provider also needing to create the same
phase. This was problematic for a few reasons:

- The first was that when you deleted Ruleset rules in the UI, it didn't
  remove the phase. This was intentional but hidden behind the UI and
  only accessible via the API.
- Secondly, when customers wanted to use Terraform, there was an
  assumption they would be starting from scratch and many were not.
- Finally, in the event of a collision, we didn't know which Ruleset the
  customer wanted to use so we error'd out with a link to manually
  resolve which isn't a great solution but made the issue more
  prominent.

I had a chance to rethink through this issue and managed to find a way
that we improve all three points above and remove majority of the pain
points. With the proposed changes, the only time a customer needs to
manually resolve the Ruleset rules is if there are existing rules in the
UI which requires them to be deleted or migrated.

Achieving this requires the assumption that if the Ruleset has no rules,
it is ok to modify. Unfortunately, it's not that simple in practice. If
the phase already exists, we cannot just update it as the `name`
attribute is not writable after creation. Along with this, the `ref` and
`version` values will be automatically incremented causing a permadiff
in Terraform as the customer hasn't actually modified these values but
the backing service (and API) has. To work around this, if we find a
phase with no rules, we recreate it with the provided values which is
essentially the same the same thing as the "happy path" for a new
Terraform resource would be anyway.

---
## [aartisinghh/Sensights](https://github.com/aartisinghh/Sensights)@[06254a1dd8...](https://github.com/aartisinghh/Sensights/commit/06254a1dd8cca705b1cea4bbd11739a33dd9a17f)
#### Wednesday 2022-01-19 01:45:36 by graedenlau

Rename holy shit it works.ipynb to nice as hell.ipynb

---
## [Kubius/goonstation](https://github.com/Kubius/goonstation)@[213b1fb1c9...](https://github.com/Kubius/goonstation/commit/213b1fb1c936cb95eace5cc4faac16cddc174eac)
#### Wednesday 2022-01-19 02:51:51 by Nexusuxen

AI Skins (#7129)

* wip
skins added
support for different skins added
- battmode & apcmode overlays
- readjust stun/bsod icon states to use overlays
setSkin proc also includes input validation to ensure only valid icons
medal+reward "Now you're thinking with portals!" dwaine skin
FUCK NPC AI WHY DO THE MARTIANS AGGRO ON SPAWN ARGHGHH

* mostly final changes
adds clown skin
further refactors to ai core frame layering
ai core sprites are now separate from the screen
blank screen now used for when the ai is depowered
(cant remember all the details, its been a while)

* tweaks
some desc adjusts
undid weird indentation(s)
removed unnecessary/outdated comments
1 -> TRUE
adds clown ai kit to geoff honkington's stock
(honk)

---
## [Leo2323232/MARDEK-Leos-Mod](https://github.com/Leo2323232/MARDEK-Leos-Mod)@[1de7941760...](https://github.com/Leo2323232/MARDEK-Leos-Mod/commit/1de79417600f481cc8e9445243ae5e8bbd760e19)
#### Wednesday 2022-01-19 03:18:47 by Leo2323232

Water Guardian Changes

-blind 10 to 40, poison 10 to 25, paralysis 10 to 40, sleep 10 to 30, confuse 0 to 25, numb, silence and curse 90 to 80
-basic spells 60 to 40 power and have 25% chance to cause poison, paralysis and silence, tsunami 50 to 30 power, silence chance 90 to 50, but hits everyone, renamed mass silence, emela uses magic bolt as null, claws have 30% crit chance and 100 accuracy, inversion mp cost 30 to 10, mega barrier mp 50 to 10, will counter by buffing its own spirit by 1
-increase hp 30 to 40k
-starts with regen

---
## [NXPmicro/zephyr](https://github.com/NXPmicro/zephyr)@[6809593739...](https://github.com/NXPmicro/zephyr/commit/680959373982584eb4fca09cdea464dfe59d262d)
#### Wednesday 2022-01-19 03:49:41 by Andy Ross

soc/intel_adsp: Linkage rework

Lots of changes to the linkage, none major:

+ Remove all the manually-defined ELF program headers.  This was a big
  pain to maintain, and I finally figured out why we were doing this:
  it turns out to have been a workaround for the flags issue below.

+ Suppress the "empty loadable section" warnings at module generation.
  This turns out to be an objcopy issue, when you drop all the
  sections from an ELF program header.

+ Set section flags for NOLOAD sections manually.  Rimage is very
  strict about flags (even to the point of trying to suck in its own
  metadata section as program text).  This turns out to be really
  fragile, as the linker automatically sets flags on the output
  section based on the symbols placed in it.  Rather than needing to
  have one program header per section, or playing games in the
  assembly for section definition to make this all match, just set the
  flags expressly on the sections we know about on the objcopy command
  line.

+ Similarly drop the special memory regions with explicit faked
  "physical" addresses that were being used for non-loadable sections
  (e.g. .fw_metadata, .static_log_entries).  Just link them all after
  the rest of the image like other platforms do.

+ Clean up multiple levels of macro indirection for the manifest base
  address, which is ultimately coming from kconfig.  Now the magic
  numbers don't seem so magic.

+ Remove legacy symbol exports for "cacheattr" that we don't use
  anymore.

Signed-off-by: Andy Ross <andrew.j.ross@intel.com>

---
## [Atom-X-Devs/android_kernel_xiaomi_scarlet](https://github.com/Atom-X-Devs/android_kernel_xiaomi_scarlet)@[b91c377639...](https://github.com/Atom-X-Devs/android_kernel_xiaomi_scarlet/commit/b91c3776394447a22c7360345a04be3677e6dd66)
#### Wednesday 2022-01-19 07:25:50 by Peter Zijlstra

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
Signed-off-by: Ratoriku <a1063021545@gmail.com>
Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>

---
## [paranormalshrimp/Nightmare-Client](https://github.com/paranormalshrimp/Nightmare-Client)@[68d01ca0de...](https://github.com/paranormalshrimp/Nightmare-Client/commit/68d01ca0de16d0deb5e8ce7a8a1cb5768f9abaf4)
#### Wednesday 2022-01-19 07:31:17 by paranormalshrimp

Add files via upload

Hello! This is Nightmare Hack Client for Minecraft version 1.8.
This client is not fully developed yet and I plan on adding more things in the future.
You can find all past versions of my client in the Legacy Versions section.
Check back every 2 months or so to see if I got my lazy ass around to an update.
Works well on BlocksMC (NoFall sometimes kicks but everything else is fine)
There's no click GUI or tabgui YET so things are only accessible through keybinds
R - Sprint
P - FullBright
N - NoFall
L - JumpFly
K - Fly
B - KillAura
Thats all for now, I hope you enjoy!
(idk how one would go about obfuscation so it open source I'm 99% sure)

---
## [Almeerakitchen2021/Kitchen](https://github.com/Almeerakitchen2021/Kitchen)@[40e8cd9fae...](https://github.com/Almeerakitchen2021/Kitchen/commit/40e8cd9fae8e16fc493123d12be9d0799eff6820)
#### Wednesday 2022-01-19 08:01:39 by Almeerakitchen2021

Create 30 Best Kitchen Cabinet 

The kitchen is a popular space in most homes, and it's no wonder why. It's the place where families get together to cook great food for dinner or breakfast, and it's the heart of home life. But over time, kitchens have evolved; they are no longer just utilitarian spaces with basic appliances and traditional cabinets.

---
## [SowryaSharma/swiftLearning](https://github.com/SowryaSharma/swiftLearning)@[5ed16ac131...](https://github.com/SowryaSharma/swiftLearning/commit/5ed16ac131b4331f3003424dc083bcde15e4f2c4)
#### Wednesday 2022-01-19 08:07:02 by SowryaSharma

Create Bill Division.swift

Two friends Anna and Brian, are deciding how to split the bill at a dinner. Each will only pay for the items they consume. Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.

For example, assume the bill has the following prices: . Anna declines to eat item  which costs . If Brian calculates the bill correctly, Anna will pay . If he includes the cost of , he will calculate . In the second case, he should refund  to Anna.

Function Description

Complete the bonAppetit function in the editor below. It should print Bon Appetit if the bill is fairly split. Otherwise, it should print the integer amount of money that Brian owes Anna.

bonAppetit has the following parameter(s):

bill: an array of integers representing the cost of each item ordered
k: an integer representing the zero-based index of the item Anna doesn't eat
b: the amount of money that Anna contributed to the bill
Input Format

The first line contains two space-separated integers  and , the number of items ordered and the -based index of the item that Anna did not eat.
The second line contains  space-separated integers  where .
The third line contains an integer, , the amount of money that Brian charged Anna for her share of the bill.

Constraints

The amount of money due Anna will always be an integer
Output Format

If Brian did not overcharge Anna, print Bon Appetit on a new line; otherwise, print the difference (i.e., ) that Brian must refund to Anna. This will always be an integer.

Sample Input 0

4 1
3 10 2 9
12
Sample Output 0

5
Explanation 0
Anna didn't eat item , but she shared the rest of the items with Brian. The total cost of the shared items is  and, split in half, the cost per person is . Brian charged her  for her portion of the bill. We print the amount Anna was overcharged, , on a new line.

Sample Input 1

4 1
3 10 2 9
7
Sample Output 1

Bon Appetit
Explanation 1
Anna didn't eat item , but she shared the rest of the items with Brian. The total cost of the shared items is  and, split in half, the cost per person is . Because , we print Bon Appetit on a new line.

---
## [bolt/docs](https://github.com/bolt/docs)@[fd2da32eb9...](https://github.com/bolt/docs/commit/fd2da32eb95f83fc78d1c082d636aede506b4e80)
#### Wednesday 2022-01-19 10:17:13 by Michael Born

Improve / correct new `showimage` example in Bol5 upgrade docs

Yeah, my example from yesterday was not that accurate. `<img src="{{ showimage(record.image) }}">` doesn't actually render an image, since it breakst the HTML. :man_facepalming:

---
## [centrefornetzero/domestic-heating-abm](https://github.com/centrefornetzero/domestic-heating-abm)@[02a2c98fb8...](https://github.com/centrefornetzero/domestic-heating-abm/commit/02a2c98fb8284819d1cb2d4706b86372d0bfb1e5)
#### Wednesday 2022-01-19 11:00:12 by Tom Phillips

Type hints and mypy checks for `abm` module (#60)

* Don't allow dynamic attributes

This functionality isn't used anywhere in the model. It limits the
effectiveness of type checking because any attribute would have be of
the type `Any` (see ["dynamic attributes" in the mypy cheat sheet]
[0]). Better to add an explicit argument in any subclasses.

[0]:
(https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html#when-you-re-puzzled-or-when-things-are-complicated

* Type hint changes for stricter mypy checking

I almost got this to pass with `--strict` mode. Instead in
`pyproject.toml` I've specified every flag in `--strict` except for
`--disallow-any-generics`.

I'm not certain but I think our design is not type safe. The problem is
with the optional `model` argument to `Agent.make_decisions`, which is
of the argument type `Optional[AgentBasedModel]`. In subclasses of
`Agent` we want to specify a subclass of `AgentBasedModel`, but it's
[unsafe to override a method with a more specific argument type][0].

To make it type safe I think we'd have to make some more substantial
changes. I don't think there's sufficient benefit to justify the
effort.

[0]:
https://mypy.readthedocs.io/en/stable/common_issues.html#incompatible-overrides

---
## [newstools/2022-the-daily-sun](https://github.com/newstools/2022-the-daily-sun)@[940b5443cb...](https://github.com/newstools/2022-the-daily-sun/commit/940b5443cbd3162b28a75c070c2c2752e8308fe4)
#### Wednesday 2022-01-19 12:02:27 by Billy Einkamerer

Created Text For URL [www.dailysun.co.za/News/umona-and-evil-spirits-blocked-my-dreams-20220119]

---
## [JayMonari/ts-personal](https://github.com/JayMonari/ts-personal)@[a4885ddb5c...](https://github.com/JayMonari/ts-personal/commit/a4885ddb5cd7a5443b971a98161f2531f6f3c9a0)
#### Wednesday 2022-01-19 13:04:00 by Jay Monari

Honest to god, fuck deno, fuck node, fuck ts, this is some of the dumbest shit. I can spend in hour on petty squabbles of idiots.

---
## [rupert648/BibTeX-Management-System](https://github.com/rupert648/BibTeX-Management-System)@[4d479ac9fe...](https://github.com/rupert648/BibTeX-Management-System/commit/4d479ac9fe6059b71d2f80af325b6b6f848448f5)
#### Wednesday 2022-01-19 14:38:38 by Rupert

after much blood sweat and tears have finally got typescript react electron to open a fucking file browser

---
## [nkruzan/ArduConfigurator](https://github.com/nkruzan/ArduConfigurator)@[7e0a444f79...](https://github.com/nkruzan/ArduConfigurator/commit/7e0a444f79fa612bf2150be5c27bfb7f6666bc06)
#### Wednesday 2022-01-19 15:41:05 by Buzz

wip smartlinks test - can we get server-side node from mavagent to work?


more wip - 

tmp copied mav_v2.js direct from mavagent, as its known to work with smartlinks.js , also from mavagent.  todo delete the mav_v2 and use the one in js/mavsp/ foldrr
notes abut using -sdk version for developers


make new backend folder for Node-loaded local code.


allow jspack and 'long' module to both be used by the backend, if we want. 

yes, this is a differernet to the one in js/mavsp/local_modules/ which are currently tweaked for frontend use. sorry about the dupe, we should fix that at some point.
add mavlink parser as a proper local-node-module to the backend

.. with just tiny tweaks.
describe NW flavour on console at startup.

its easy to get the wrong one.
more dev notes


lightly hacked mavagent.js and its modules bing used as a pre-startup.js for ArduConfigurator.

// TERRIBLE HACK using mavagent.js almost in its entirety as a pre-startup.js for arduconfigurator.  
// surprisingly, it seems to kinda mostly work apart from the CLI interface.    we won't leave this here, but its interesting.
 - having this loaded its connecting to a SITL instance on tcp:localhost:5760 if u have one, and forwarding the packets to udp:localhost:14550, such as missionplanner etc.   its not yet routing any of this mavlink stream into the GUI, but its not crashing. 
remove most of  mavagent from pre-startup.js leaving mostly just smartlinks.js  AND get backend UDP routing through to frontend

frontend GUI is a bit borked when UDP right now, but its getting the data.
hex_parser changes are untested so hext parsing might be broken.?

prevents *really* early udp/tcp throwing error before window is opend.

---
## [plumbwicked/Wicked-Menu-for-GTA5](https://github.com/plumbwicked/Wicked-Menu-for-GTA5)@[66a1a34948...](https://github.com/plumbwicked/Wicked-Menu-for-GTA5/commit/66a1a34948b89554b2e4e78918fd40264da2da3d)
#### Wednesday 2022-01-19 17:50:17 by plumbwicked

v1.5

v1,5

Cleaned up GUI , Color Coded all Cheats
Green = Main Folders
Blue = Chapters
Orange = Cheats
Lime = PopOut Menus

Added :
MenuCodeBase.
Disclaimer.
Weapon Damage/Range set to Default on "All Cheats Off".
Auto Start Section -
Compact/FullViewMode / My Notication set to single/main monitor windows borderless mode,
Now AutoStarts with Menu .
LSC Cheat [Save any spawned car to your Garage to keep !]
Mini Garage[ Add Benny Wheels to Any Car !]
Teleports to LSC , Last Vehicle and Owned Vehicle added to Vehicle Options.
Roulette hack .
Player Invisibility.
Single Player Options [Oxygen,Special Ability and Money]
Encrypted Value Editor.

Removed: [ But Still Accessable from "All Menus" ]
GNulls' mini garage .
GNulls Old Mini Garage [To many Vehicle spawn menus that do the same thing ?]
Item Dropper [ Broken]
Old Item Dropper [ Also Broken ? ]

Moved:
Rid Joiner to "Session Options ".
Fly/Superjump/invisibility etc to "Fun Stuff".

Some other shit I forgot :\

---
## [Nebby1999/EnforcerMod](https://github.com/Nebby1999/EnforcerMod)@[2538549196...](https://github.com/Nebby1999/EnforcerMod/commit/253854919652e9581f25cb431113992ff0825282)
#### Wednesday 2022-01-19 17:53:47 by TimeSweeper

an inordinate amount of time on fucking needler

grandmastery achievement fixed real good, stun grenade achievement fixed
fucking fixed disappearing gun models god damn I just gave myself a solid week of mental turmoil tossing and turning at night wondering why i'm such a f
anyway
also mallet haha
oh yeah that. spent a very good amount of time setting up psds for recolors. nemforcer enforcer looks pretty sweet ngl

---
## [Nebby1999/EnforcerMod](https://github.com/Nebby1999/EnforcerMod)@[c8bc6835dd...](https://github.com/Nebby1999/EnforcerMod/commit/c8bc6835dd8bf1cf2a665fa81ce87202e0f8e947)
#### Wednesday 2022-01-19 17:53:47 by TimeSweeper

more dumb shit i'm sure

silly limb masking but also legit limb masking
more reorganizing it looks like
vr maybe
god damn so much shit I don't even know

---
## [Nebby1999/EnforcerMod](https://github.com/Nebby1999/EnforcerMod)@[a3f6a92f4b...](https://github.com/Nebby1999/EnforcerMod/commit/a3f6a92f4b6f42f51c200c162d82aab3c389e34f)
#### Wednesday 2022-01-19 17:53:47 by TimeSweeper

holy shit gm real?

fucking with boss hitboxes for no reason, unlockable tweaks, nothing else important I don't think

---
## [vincentiusvin/tgstation](https://github.com/vincentiusvin/tgstation)@[b2ba847c22...](https://github.com/vincentiusvin/tgstation/commit/b2ba847c223dcbdc49c85a46156d5dbc28dbe5bd)
#### Wednesday 2022-01-19 18:24:51 by LemonInTheDark

Reduces the move delay buffer to 1 tick (#63332)

We've got this delay buffer behavior
Idea is basically, if we're just holding down the key, just keep adding to the old delay
This way, fractional move delays make sense

Was added in this commit 491bdac

When it was added, movement was triggered by verbs sent by the client
So we needed a big grace window to account for networking delay

Don't need that anymore cause we use keyLoop, so let's just cut it all the way down

Why?
Because right now if you somehow manage to input a move afer move_delay is up
but before the window runs out, you will be elidgable for a new move before you visually reach the tile

Got a dm from mothblocks about this last night, something about flash stepping? IDK I don't play here
Seems silly though, let's sweep this up

Oh and mothblocks owes me a pizza, please add this to the commit history so it can be certified as a part of the blockchain

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[59efe8716e...](https://github.com/mrakgr/The-Spiral-Language/commit/59efe8716e9f28776183ea1950883e74ebef3d6b)
#### Wednesday 2022-01-19 18:36:15 by Marko Grdinić

"10:40am. I was very restless tonight. I was so heated I had to remove all, but a single blanket in order to fall asleep. It took me a while before I got to that point.

My sleep might have been poor, but my will is high. Let me chill a bit and then I will start the Houdini tutorials. I really need to finish these basic ones before I can more on to the rest.

11:15am. Let me start instead of wasting so much time.

Time for the tutorials.

11:20am. https://youtu.be/NjtlYXRgqWc?list=PLhyeWJ40aDkUDHDOhZQ2UkCfNiQj7hS5W&t=137

Come to think of it, I never explicitly studied any animation tutorials. Ram's could count, but I never followed along, so this will be a first for me.

11:40am. I am starting to get used to the Houdini UI. The way it is designed is very good. If you press escape in the viewport, it is in move mode. But if you press enter, it goes into the transform node and you have those handles like in Blender. But it is not just that, it is actually sensitive to the node I have selected. Right now I am in the extrude node, and the transform handle allows me to extrude it.

https://youtu.be/NjtlYXRgqWc?list=PLhyeWJ40aDkUDHDOhZQ2UkCfNiQj7hS5W&t=671

Speaking as a programmer, this is a really good way of working.

12:10pm. https://youtu.be/NjtlYXRgqWc?list=PLhyeWJ40aDkUDHDOhZQ2UkCfNiQj7hS5W&t=954

I do like this. Houdini has it made. For Blender to have all of this, it would take an unimaginable amount of work.

https://youtu.be/NjtlYXRgqWc?list=PLhyeWJ40aDkUDHDOhZQ2UkCfNiQj7hS5W&t=1062

This kind of packing node would be impossible with Blender.

1:10pm. https://youtu.be/IcbzGNqnFkA?list=PLhyeWJ40aDkUDHDOhZQ2UkCfNiQj7hS5W&t=627

Let me stop here for the morning. I am overdue for breakfast.

1:40pm. Let me finish the ep of Kaiji Kaihatsu and then I'll go do the chores.

2:55pm. It is time to resume.

3pm. Let me do it. Time to do those shaders. Once I finish this series I can do more advanced tutorials.

3:20pm. This is strange. I noticed that in render view the background and platform shaders were not taking effect. I tried fiddling with them, and suddenly that happened.

https://youtu.be/IcbzGNqnFkA?list=PLhyeWJ40aDkUDHDOhZQ2UkCfNiQj7hS5W&t=855

I wonder how shadow intensity works. I thought shadows were only related to the amount of light in a scene. Strange.

3:35pm. https://www.quantamagazine.org/neural-noise-shows-the-uncertainty-of-our-memories-20220118/

Let me read this.

https://youtu.be/NHmAcO6Dob4?list=PLhyeWJ40aDkUDHDOhZQ2UkCfNiQj7hS5W
Houdini Isnt Scary Project - Part 3: Rigid Body Dynamics

After that it is rigid body dynamics for me.

3:40pm. Let me start.

https://youtu.be/NHmAcO6Dob4?list=PLhyeWJ40aDkUDHDOhZQ2UkCfNiQj7hS5W&t=264

To get it to start in the right place, I had to turn on use object transform. I wonder why it works for him despite that?

4:50pm. Time for part 4. Had to take a little break. Let me finish this.

5pm. Let me stop here for a bit, I have to do an extra bit of chores.

5:15pm. Let me resume.

5:25pm. And I am trying to do it on my own and weird things are happening. Is it possible that Houdini has caching bugs?

How do I clear it? Let me just watch the video. I do not know how to stop the platform from turning into water particles.

5:40pm. I've cleared up some of my confusion, but what is the point of that timeshift node? I had to have done something wrong since, it just results in an object that does nothing. Let me watch the video.

6:05pm. This is so annoying! I should have followed it step by step exactly instead of trying to explore on my own. I keep getting cache errors.

6:35pm. I am back from lunch.

Let me resume the tutorial.

7pm. Ugh, I have no idea what timeshift was supposed to be doing. And I really don't want to mess with IO nodes even though I should have. one thing I am dissapointed about is that he did not cover how to tranfer the velocity from the ball to the fluid.

7:05pm. Mhhh, damn it. I need to investigate the disk caching. I actually skipped the IO parts.

I also need to go back and figure out what that timeshift is doing.

7:10pm. I do not feel like it right now. As strange as it is, I couldn't finish the lecture series today despite how basic it is. I am going to do it tomorrow in its proper time and move on to making that soccer ball.

One step at a time. Let me have some rest here.

Despite not being able to do it, I was actually rather focused throughout. I think I internalized most of it. The problem is that there is so much of it. I can really see why Houdini is considered to have the hardest learning curve out of all the 3d programs out there. It is not just a 3d package like Blender, but a fully fledged programming environment. And on top of that it is massive, much more so than Blender. It feels like a program where if I could claim to understand 10% of it, I could call myself an expert.

I need to keep going forward with this. Maybe it seems like a waste, but assuming I could get an AI chip, maybe I could make it a side business to write physics simulation solvers for 3d programs. That woudl be a lot more realistic as a first step than trying to infer out intelligence algorithms via genetic programming. It would be excellent practice too as the intelligence algorithms will be some kind of phyisical system simulation anyway.

7:30pm> Let me close here, instead of stading here in a daze. I'll get this done tomorrow. At some point I will maange to establish my workflow. I need keep going forward until then. I could have already established it, but I will be able to reach a higher level of skill in the end if I add Houdini to my toolset. It will be worth it. I do not care about getting rich anymore.

I feel that artists doing it for the sake of art is a weird cope, but wanting to do ML for the sake either money or causing the Singularity did not make me any more successful. So I'll do this for the money, but I am not expecting anything great, not like with trading or ML. Just a little bit to start things off will be enough. Surely, I can at least get to the point where I am making 100$ a month. So far Spiral is making me 5$ a month, so I suppose that is something. I need to get more patrons. If I can get sponsors, I can actually start cultivating AI again. If not, then that is where the quest will end for me."

---
## [bellomia/MOTTlab](https://github.com/bellomia/MOTTlab)@[eb9960dd54...](https://github.com/bellomia/MOTTlab/commit/eb9960dd542264c1b82bbd1bf2cb5c63f021f8f6)
#### Wednesday 2022-01-19 19:07:31 by Gabriele Bellomia

Optimize `I_L vs U` calculation: fix of math.fconv()

Here we end the story of the mysterious convolution bug.

- Having established that the log plots of the two convolutions are strikingly distinct after the midpoint of the arrays, we go for a careful inspection of that region, that we recall being substantially zero in the bird-eye views found in docs/fast_conv/App.gif
  > we plot just those behaded arrays, with an extremely zoomed y-axis and we see that A. the built-in conv gives a TRUE ZERO (🥺blackmagic!) while B. our fast implementation stays to a totally respectable machine zero. (And we knew it, the norm(conv-fconv) was ridicously small!)

Soooo... are the numerically vanishing negative numbers affecting so much the DMFT self-consistency?! THEY ARE. ✨😶‍🌫️✨

- Let's look downstream in the DMFT_loop: first of all the final result of the nested convolutions (the imag of the 2nd order bubble) is fed to the Kramers-Kronig transform, coded through the hilbert() function embedded in the Signal Processing Toolbox. Will it be so sensible to some vanishing negative numbers?
  > Actually not, the resulting self-energies (docs/fast_conv/sloc_bad.gif) are qualitatively correct, and undistinguishable to the post-fix /sloc_good.gif plots. The error is propagating for sure, but not exploding yet! 🧐

- Then let's continue going downstream and we arrive at the SELF-CONSISTENCY relationship: the Hilbert transform of the Bethe lattice DOS, through the 1/(z-Sigma) Cauchy kernel. This is coded in +phys.BetheHilbert() in the most naive way, directly from the definition of the transform and the analytical expression of the DOS. (maybe at some point we should rewrite it exploiting once more the hilbert() matlab function?)
  > HERE YOU HAVE: docs/fast_conv/gloc_bad.gif is EXTREMELY BAD and totally different from the post-fix /gloc_good.gif file! 😏

So yeah, am I telling you that such a totally negligible 1e-10 difference in the computed convolutions accounts for THIS MESS?! Yes, I am. 😌

The proof is the easiest: add a freaking abs() at the last line of the fconv algorithm (line 60) and... you have it: the magic happens and we retrieve the good old convergence properties and the nicest I_L vs U span (docs/fast_conv/luttinger_good.svg). And with respect to the reference commit 6c38c0d0f6d9f9ecde5a2b81dfabddd76481a7da we go down from ~990s to ~140s, a brillant overall 7x speedup!

We'll provide more insights on the actual speedup of the conv() vs fconv() self-times, but for now we can say that Issue #1 is closed! 💥

Over and out. 🙃

---
## [mc-skyprison/SkyPrisonClaims](https://github.com/mc-skyprison/SkyPrisonClaims)@[a9c2c6e9de...](https://github.com/mc-skyprison/SkyPrisonClaims/commit/a9c2c6e9deb8aee2a0a58e6c9d4b745a7ff4a830)
#### Wednesday 2022-01-19 19:11:29 by DrakePork

Fucking hell I havnt pushed this one in a while whoops.

+ Added fly flag
+ Added EffectFlag
+ Moved some code regarding regions over from SkyPrisonCore
+ Implemented claim transfer
+ Did so admins in a claim can change flags
+ added blocks as a substitute to /claim claimblocks, so /claim blocks is now a thing
+ Same with /claim buyclaimblocks, you can now use /claim buyblocks.
+ /claim nearby has been added too instead of /claim nearbyclaims.
+ Did so /claim returns the help message
+ commented /claimadmin migrate since its not needed anymore
+ Completely removed /claim setflag. Claim flags can now only be set through the GUI.
+ Added a few more donor flags like weather lock
+ Started work on allowing players to allow specific players to enter their claim without being member when entry is denied.
+ Updated so much shit
+ Completely redid the entire getClaimInfo to make it so much better to look and more informative.

---
## [clamor-s/u-boot](https://github.com/clamor-s/u-boot)@[8ee134ff80...](https://github.com/clamor-s/u-boot/commit/8ee134ff80affb2f1123ca40c8277883d86383de)
#### Wednesday 2022-01-19 19:30:50 by Marcel Ziswiler

tegra: lcd: video: integrate display driver for t30

On popular request make the display driver from T20 work on T30 as
well. Turned out to be quite straight forward. However a few notes
about some things encountered during porting: Of course the T30 device
tree was completely missing host1x as well as PWM support but it turns
out this can simply be copied from T20. The only trouble compiling the
Tegra video driver for T30 had to do with some hard-coded PWM pin
muxing for T20 which is quite ugly anyway. On T30 this gets handled by
a board specific complete pin muxing table. The older Chromium U-Boot
2011.06 which to my knowledge was the only prior attempt at enabling a
display driver for T30 for whatever reason got some clocking stuff
mixed up. Turns out at least for a single display controller T20 and
T30 can be clocked quite similar. Enjoy.

Signed-off-by: Svyatoslav Ryhel <clamor95@gmail.com>

---
## [chromium/chromium](https://github.com/chromium/chromium)@[e7a4c46875...](https://github.com/chromium/chromium/commit/e7a4c46875b2fc01914d0e1d629383f043acaa55)
#### Wednesday 2022-01-19 19:37:55 by Adam Langley

webauthn: remember whether to jump to Windows native UI.

Currently Chrome will immediately trigger the Windows native UI for
WebAuthn unless either:
   1. accounts.google.com is doing caBLEv1 or server-link.
   2. There are paired caBLEv2 phones.

If you're in an enterprise setting where very regular security key
operations are needed then probably neither of those apply. However,
when we enable QR support there'll always be the option to add a phone.
Rather than always showing the Chrome UI first this change does a couple
of things:

   1. Make the option for the native API top of the mechanism selection
      list. Thus you can trigger it by just hitting enter.
   2. Remember whether the last successful registration or assertion
      used the native API or not. If so, do directly to the native API
      next time and only show the Chrome UI if that UI is cancelled.

This isn't perfect, but there are limits to what we can do with
operations split between Chrome and Windows. It means that users who use
physical security keys a lot, and users who use phones a lot, get a good
experience. People who switch between them end up worse off as a
tradeoff. The estimate is that the number of such people is relatively
small.

BUG=1002262

Change-Id: I28d74b42a5c950622cc56b98e4c13c3450071b25
Reviewed-on: https://chromium-review.googlesource.com/c/chromium/src/+/3363266
Reviewed-by: Ken Buchanan <kenrb@chromium.org>
Reviewed-by: Avi Drissman <avi@chromium.org>
Commit-Queue: Adam Langley <agl@chromium.org>
Cr-Commit-Position: refs/heads/main@{#961065}

---
## [maxspells/fulpstation](https://github.com/maxspells/fulpstation)@[c797bf79ea...](https://github.com/maxspells/fulpstation/commit/c797bf79ea71c9fd26f598306753a9abc55427d8)
#### Wednesday 2022-01-19 19:55:43 by Pepsilawn

Fixes broken ass area on Helios tation (#440)

* Fixes Helios

* fuck you turbine

* MACHINERY/wish_granter

---
## [edx/edx-analytics-data-api](https://github.com/edx/edx-analytics-data-api)@[1c2fbe8249...](https://github.com/edx/edx-analytics-data-api/commit/1c2fbe82497c93f1b01773e3b11a9dd15dd1efd8)
#### Wednesday 2022-01-19 20:50:48 by Andy Shultz

fix: move most sorting from MySQL to python

in theory it makes sense to sort in the DB. In practice it means we
sort whether we need to or not and we add invisible work to queries
because the sort is not at the point of querying

in practical effect our DB is often taking this sort out to a
materialized table on disk, which is super slow, and then we'll have
it all in memory in django anyway

so drop ordering from the object models, add it to the views where
needed to support groupbys

location is left alone because it is not causing trouble today and its
sorting and grouping is slightly wonky and could use a complete
rebuild

MST-1305

---
## [Toby-Osborne/DynamicsAXAutomated](https://github.com/Toby-Osborne/DynamicsAXAutomated)@[f43760d17b...](https://github.com/Toby-Osborne/DynamicsAXAutomated/commit/f43760d17ba4bd0d5a43f202af17a9ae1bf56e81)
#### Wednesday 2022-01-19 21:24:16 by Toby Osborne

I can't fUCKING USE GIT ON THIS COMPUTER FUCK why

fuck you ports of auckland IT desk why did you block github

---
## [ahhuang007/wallstreetbets](https://github.com/ahhuang007/wallstreetbets)@[11ca521fbc...](https://github.com/ahhuang007/wallstreetbets/commit/11ca521fbc285a0692eb4b693d4b45fca75c4b20)
#### Wednesday 2022-01-19 22:34:30 by ahhuang007

created validation environment/script, tested our two models

Created a validation environment that uses new data not included in training, both models kinda shit the bed a bit. I think I need to re-evalauate my reward function, since my models clearly aren't understanding what to do to increase reward. Also, this might be a fluke but my models seem to do well at the beginning of the episode, which could be because they have much more experience at that part of the episode - maybe I should initialize episodes on a random point in my data to train on all my data

---
## [81Denton/tgstation](https://github.com/81Denton/tgstation)@[4610f700eb...](https://github.com/81Denton/tgstation/commit/4610f700eb74a3a41555e69c4904ad897caf2d99)
#### Wednesday 2022-01-19 23:25:04 by LemonInTheDark

Fixes up multiz atmos connection, cleans some things up in general (#63270)

About The Pull Request

ALLLRIGHT so
Multiz atmos was letting gas flow down into things that should be well, not flowable into
Like say doors, or windows.

This is weird.

Let's get into some context on why yeah?

First, how do things work currently?

atoms have a can_atmos_pass var defined on them. This points to a define that describes how they interact with
flow.
ATMOS_PASS_NO means well, if we're asked, block any attempts at flow. This is what walls use.
ATMOS_PASS_YES means the inverse
ATMOS_PASS_DENSITY means check our current density
ATMOS_PASS_PROC means call can_atmos_pass, we need some more details about this attempt

These are effectively optimizations.

That var, can_atmos_pass is accessed by CANATMOSPASS() the macro
It's used for 3 things.

1: Can this turf share at all?
2: Can this turf share with another turf
3: Does this atom block a share to another turf

All of this logic is bundled together to weed out the weak.

Anyway, so when we added multiz atmos, we effectively made a second version of this system, but for vertical
checks.

Issue here, we don't actually need to.
The only time we care if a check is vertical or not is if we're talking to another turf, it's not like you'll
have an object that only wants to block vertical atmos.
And even if you did, that's what ATMOS_PASS_PROC is for.

As it stands we need to either ignore any object behavior, or just duplicate can_atmos_pass but again.
Silly.

So I've merged the two, and added an arg to mark if this is a verical attempt.
This'll fix things that really should block up/down but don't, like windows and doors and such.

Past that, I've cleaned can_atmos_pass up a bit so it's easier for people to understand in future.
Oh and I removed the second CANATMOSPASS from immediate_calculate_adjacent_turfs.
It isn't a huge optimization, and it's just not functional.

It ties into zAirOut and zAirIn, both of which expect to be called with a valid direction.
So if say, you open a door that's currently blocking space from leaking in from above, you end up with the door
just not asking the space above if it wants to share, since the door can't zAirOut with itself.

Let's just wipe it out.

This makes the other code much cleaner too, heals the soul.

Anyway yadeyada old as ass bug, peace is restored to the kingdom, none noticed this somehow you'd think people
would notice window plasma, etc etc.
Why It's Good For The Game

MUH SIMULATION
Also fuck window gas
Changelog

cl
fix: Fixed gas flowing into windows from above, I am.... so tired
fix: Fixes gas sometimes not moving up from below after a structure change, see above
/cl

---
## [Hinaichigo/vgstation13-1](https://github.com/Hinaichigo/vgstation13-1)@[622f3fac2b...](https://github.com/Hinaichigo/vgstation13-1/commit/622f3fac2b24476f23d8c9ebfae2dba5e371a3cc)
#### Wednesday 2022-01-19 23:28:24 by ShiftyRail

The Thing Before Christmas (#31715)

I thought this was a good way to spice up the winter season.
While I know Ling was removed for a reason, I want you to consider that it got removed years ago. It is fair to say that the playerbase and the game changed so much since then than a "tabula rasa" might be justified.

Besides, ling had deathsting removed and its obnoxious chemical stings axxed too. (#23014)
From a QoL standpoint, the stings have been converted to spells and should be as easy to use as the vampire ones.

As a final note, it's painstaingly true that ling is the least worked over of all our antags and is in dire need of some love and new content. However, this content can only come if people experience ling first-hand and get motivated to fix it.

Worse come to worse, we remove it again lole

Merry Christmas everyone.

:cl:
- rscadd: Santa Claus is coming to town. More specifically, he's coming to Antartica. Wait, he was already here all this time? And why does he look so familiar... OH GOD HELP

---
## [raehik/gtvm-hs](https://github.com/raehik/gtvm-hs)@[4366703727...](https://github.com/raehik/gtvm-hs/commit/436670372769ea22c44c66d95f5754bd174faae7)
#### Wednesday 2022-01-19 23:41:39 by Ben Orchard

huge refactor, tons of cool ideas

Flowchart handling is rewritten to use a fun wrapper I wrote over the
refined refinement types library, plus a binary parsing/serializing
layer using the former. The result is a newtype-heavy solution that puts
the binary schema into the types, along with some magic that tries to
restrict you from making errors while you're transforming your data.

It was very interesting to write. I both like and dislike newtype-heavy
code. I think the best approach is to provide lots of combinators, then
an optional convenience interface over them via a typeclass. My case
feels different, because the whole pattern is based around having
fancy newtypes that you define a number of different instances over to
enable parsing and serializing between weak and strong views. The
newtypes *are* the combinators, connecting various typeclasses.

I don't like the algebra I had to perform to extract, rewrap newtypes
inside traverses and fmaps. But, that sort of work is pretty much
automated with a good IDE, and once written they felt like nice
combinators. Also, the heavy static typing limits what you can do for
unusual formats like ELF, which encodes which endianness to use early in
the header. That's just a limitation of the pattern, you can't handle
that sort of dynamicism in the type level.

All in all, a cool investigation that I should spin out into a
standalone library.

---

