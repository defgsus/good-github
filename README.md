## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-07-24](docs/good-messages/2022/2022-07-24.md)


1,540,079 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,540,079 were push events containing 2,045,992 commit messages that amount to 108,859,297 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 35 messages:


## [yogstation13/Yogstation](https://github.com/yogstation13/Yogstation)@[b26f9f03e0...](https://github.com/yogstation13/Yogstation/commit/b26f9f03e00ded330c6bc2e0efa54aec0f8500cb)
#### Sunday 2022-07-24 01:24:39 by Vaelophis Nyx

Makes donkpocket boxes on Box station into random spawners (#14822)

* Makes donk pockets station wide into random spawners

also adds a pile of donkpocket boxes to sec's back room and gives them a microwave

* reduced quanitity of donkpockets in sec by 4 boxes

* adds randodonks to the box mining base

* another commit I fundamentally disagree with

* reduces # of donk boxes in all kitchen variants

kill me

* microwave & gun/bomb swap

* fuck you byond map code

* fixes it. again.

---
## [ParadiseSS13/Paradise](https://github.com/ParadiseSS13/Paradise)@[fd5580307e...](https://github.com/ParadiseSS13/Paradise/commit/fd5580307e1d3a2821ae8b2f26cb04cdcd139f87)
#### Sunday 2022-07-24 01:30:07 by Contrabang

Adds a blue overlay to scrying orb users. Spirit realm and scrying orb users now have a special description instead of being catatonic (#18366)

* holy shit blue ghosts

* lets fix that

* you cant see it if its not in ya hand

* Their glowing red eyes are glazed over

* farie review

* farie review pt 2

---
## [unit0016/StarbloomSS13](https://github.com/unit0016/StarbloomSS13)@[cbd7626cb7...](https://github.com/unit0016/StarbloomSS13/commit/cbd7626cb7b189f1aa19ae007a5dcc253757601d)
#### Sunday 2022-07-24 02:16:06 by RegJackson

Readds buckshot to the autolathe

I used the shotgun. You know why? Cause the shot gun doesn't miss, and unlike the shitty hybrid taser it stops a criminal in their tracks in two hits. Bang, bang, and they're fucking done. I use four shots just to make damn sure. Because, once again, I'm not there to coddle a buncha criminal scum sucking faggots, I'm there to 1) Survive the fucking round. 2) Guard the armory. So you can absolutely get fucked. If I get unbanned, which I won't, you can guarantee I will continue to use the shotgun to apprehend criminals. Because it's quick, clean and effective as fuck. Why in the seven hells would I fuck around with the disabler shots, which take half a clip just to bring someone down, or with the tazer bolts which are slow as balls, impossible to aim and do about next to jack shit, fuck all. The shotgun is the superior law enforcement weapon. Because it stops crime. And it stops crime by reducing the number of criminals roaming the fucking halls.

---
## [jeffkowalski/doomemacs](https://github.com/jeffkowalski/doomemacs)@[b07614037f...](https://github.com/jeffkowalski/doomemacs/commit/b07614037f7670682d2c193d83abdb9eed9f218e)
#### Sunday 2022-07-24 02:23:48 by TEC

fix(mu4e): support mu 1.8

Thanks to some combination of ignorance and obstinance, mu4e has thrown
compatibility to the wind and completely ignored the exitance of
define-obsolete-function-alias. Coupled with the inconsistent/partial
function renaming, this has made the mu4e 1.6⟶1.8 change particularly
annoying to deal with.

By suffering the pain of doing the mu4e author's work for them, we can
use defalias to give backwards compatibility a good shot for about 60
functions. Some mu4e~x functions are now mu4e--x, others are unchanged,
and then you've got a few odd changes like mu4e~proc -> mu4e--server and
mu4e-search-rerun. The form of message :from entries has also changed,
and a new (mu4e) entrypoint added supplanting mu4e~start.

Fix: #6511
Close: #6549
Co-authored-by: Rahguzar <aikrahguzar@gmail.com>

---
## [CCO-Project/userscripts](https://github.com/CCO-Project/userscripts)@[d7ea19fd7a...](https://github.com/CCO-Project/userscripts/commit/d7ea19fd7a089f624a6af5b5c11beff8fdf32f4f)
#### Sunday 2022-07-24 02:34:56 by LianSheng197

[v1.0] Fixed bugs, and let it draggable.
- Fixed the bug which is ui redraw loop when some buffs was expired.
- Fixed the cross-platform font display issues. (fuck you Windows)
- Some style changed.
- Special thanks to ChaosOp who provides initDrag function.

---
## [Foundation-19/Foundation-19](https://github.com/Foundation-19/Foundation-19)@[3198c7d257...](https://github.com/Foundation-19/Foundation-19/commit/3198c7d257961f97b45ae128cdc72b657a2ed36e)
#### Sunday 2022-07-24 03:23:30 by ivanmixo

Fixes MTF heli runtime (#547)

* Fixes mtf heli

* Fuck you die

* Whoops funny haha

* Cheeky juke fix

---
## [blazerpaul15/kernel_xiaomi_mt6785](https://github.com/blazerpaul15/kernel_xiaomi_mt6785)@[161208cdfe...](https://github.com/blazerpaul15/kernel_xiaomi_mt6785/commit/161208cdfed54ebf9917aac4791df6d9717e2dda)
#### Sunday 2022-07-24 04:53:04 by Peter Zijlstra

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
## [Gullwing-door/restoration-mod](https://github.com/Gullwing-door/restoration-mod)@[56cf8bc234...](https://github.com/Gullwing-door/restoration-mod/commit/56cf8bc234375b7a09481f2fd262fb55670b3898)
#### Sunday 2022-07-24 04:53:48 by Noep

Fixed Gold AK bolt

- YO LIL DONNIE, I JUST SHIT AND PISSED MYSELF AFTER I FOUND OUT THE FUCKING GOLD AK BOLT I WAS HAVING SO MUCH TROUBLE WITH WAS POINTING TO AN INVALID TEXTURE IN ITS MATERIAL CONFIG
-- For real tho, kill me

---
## [darkmusic/bevy](https://github.com/darkmusic/bevy)@[4847f7e3ad...](https://github.com/darkmusic/bevy/commit/4847f7e3adc835053a8907dd578c342b4bd395e2)
#### Sunday 2022-07-24 05:40:14 by ira

Update codebase to use `IntoIterator` where possible. (#5269)

Remove unnecessary calls to `iter()`/`iter_mut()`.
Mainly updates the use of queries in our code, docs, and examples.

```rust
// From
for _ in list.iter() {
for _ in list.iter_mut() {

// To
for _ in &list {
for _ in &mut list {
```

We already enable the pedantic lint [clippy::explicit_iter_loop](https://rust-lang.github.io/rust-clippy/stable/) inside of Bevy. However, this only warns for a few known types from the standard library.

## Note for reviewers
As you can see the additions and deletions are exactly equal.
Maybe give it a quick skim to check I didn't sneak in a crypto miner, but you don't have to torture yourself by reading every line.
I already experienced enough pain making this PR :) 


Co-authored-by: devil-ira <justthecooldude@gmail.com>

---
## [Marrone321/coyote-bayou](https://github.com/Marrone321/coyote-bayou)@[eab43e488d...](https://github.com/Marrone321/coyote-bayou/commit/eab43e488d564b0f079d7b0694afac1adb05c907)
#### Sunday 2022-07-24 05:48:32 by Marrone

Loadout Update

General Description: This PR updates several loadouts for followers, wastelanders, far-landers, and the Redwater faction.

FOLLOWERS CHANGES

STARTING TEXT
- Starting text, including Description, Enforces and Forbids, have been edited to reflect the standard the server wants to see and has also omitted references to NCR and the Legion.
- For Admin and Guard there is slightly different text to match their job descriptions.

LOADOUTS

- Removed CHEMWIZ trait which somehow fixed them not having CHEMWHIZ
- Professors now have Loadouts, two robust options which provide new machine boards to the Followers when they join as part of their loadout. The two loadouts are Environmental Scientist who has hydroponic boards, and Medical Specialist who has a blood bank.

- Specialists have some tweaks to make Medical Researcher more robust by adding a Bluespace syringe and an advanced health analyzer to their loadout.

- Randomly it seems the Volunteer loadout which has tools and construction stuff, had a chemist PDA. This has been removed and now the weakest loadout, the Student, has a PDA.

- Followers Guard had a tweak, the long range loadout has a scope, and the shotgun for the short range loadout has been changed to a police shotgun which is more inline with the aesthetic, and starts with bean bag rounds - though its total capacity is 6 as opposed to the previous 4.

These changes are intended to bring more value and encourage more players to participate in these roles. If you have any suggestions for additions, changes or subtractions let me know in the comments.

WASTELANDER CHANGES

LOADOUTS

Several additions and tweaks have been done to the Wastelander loadouts in order to properly reflect a myriad of playstyles.

- Small changes include, changing a welding helmet to welding goggles, adding extra magazines where there was only 1, tweaking the settler loadout to be more settler-y by giving them glass instead of wood, giving them a more melee focused build that resemble tools, and adding seeds to their loadout.  The Wasteland Medic has been tuned down with salts and surgery bag removed, and the Vaultie has lost their headset radio.

- 10 new Wastelander loadouts have been added, the Gambler which has a lot of interesting RP items, the Vaquero which allows players to explore another aesthetic in-line with the South West, the Hobo loadout for those who want a challenge, the Hombre loadout to replace the desert ranger one so it is more in-line with our current lore and to get away from New Vegas, Ex-Military for those who want to LARP as a soldier or mercenary, a brand new Brotherhood of Steel waster loadout that does not have grenades and is more balanced with other waster loadouts, Eidelon loadout for those who wish to be sneaky and slightly Russian if they so wish, the Aviator loadout to allow players some options to have that air pilot aesthetic, the Trapper loadout for that CLASSIC CLASSIC Fallout experience, and finally the Trouper loadout for all of the bottoms out there.

FAR-LANDER CHANGES

- I have created a whole new set of traits and it took a lot of work, having to do multiple things seven times over and over to make a book that allows you to pick from a list a traitbook which makes it so you can craft one of the seven different former tribes armor and garments. Rejoice!

- The loadouts for Far-Landers have been reduced from 21-3 to 5. To those who wish for aesthetic or loadout options which have been omitted from this decision, let me know and I can tweak some things or add another class since I removed a lot, but they must be more generalized so that specific tribes arent tied to actual loadout options.

REDWATER CHANGES

- Redwater Slave, my favourite job, no longer has explosive collars; they are now shock collars. Aww man, I wanted to be round ended.

- A whole new job was added called Redwater Resident. They will be in charge of supervising and protecting Redwater, and act as inhabitants of the town; they may travel outside of the town to gather materials but otherwise should be staying in the area and around town. They are equipped in quite a robust manner, so anyone who dares to battle the town better be geared to the teeth.

- The Overboss keeps spawning in Nash naked. I fixed this. They now have clothes, and also spawn in Redwater.

---
## [faceyneck/marley_bella](https://github.com/faceyneck/marley_bella)@[2aac0f6202...](https://github.com/faceyneck/marley_bella/commit/2aac0f6202b9a02bc21ea1236be3812558c4e79c)
#### Sunday 2022-07-24 06:14:36 by RJ

Github is a pain in the fucking ass

Uploaded files that are in a branch, to the main branch! 
FUCK YOU GITHUB, YOU ARE CONFUSING AND ANNOYING AS FUCK.
FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK 
FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK FUCK

---
## [lemonhandgrenade/hp-datapack](https://github.com/lemonhandgrenade/hp-datapack)@[ce97c191e9...](https://github.com/lemonhandgrenade/hp-datapack/commit/ce97c191e92768806a6c10eefe8e1be46bb36783)
#### Sunday 2022-07-24 07:43:15 by lemonhandgrenade

Pain update

What this adds:

Werewolves:
When a player is hit by a werewolf they have a 1/10 chance to get lycanthropy sickness
If a player does use a mixture of powdered silver and dittany in time they will become a werewolf
Werewolves change on the full moon and the player is no longer able to control the character
However if the player drinks Wolfsbane potion before the full moon they will be able to control themselves while in werewolf form

Clothes:
Invisibility Cloak
Cloak of Invisibility
House robes

Misc:
Instant Darkness Powder
Hand of Glory
Player Hair
Frog Cards
Frog Boxes/Chocolate Frog
Dungbomb
Trunks
Quaffle

Potions:
Draught of Living Death
Essence of Dittany
Mixture of Powdered Silver and Dittany
Polyjuice
Wolfsbane

Frog Cards:
Added 135 officially known frog cards that have rank and number

Spells:
Updated Levitation charm
Changed Langlock particle
Updated Locking spells to be more accurate
Updated Wand lighting charms to fix weird duplication error
Fix spelling mistake of Quietening charm
Added Items to Levitation charms effects
Fixes:
Added animagus to player info
Changed the frogs to 1.19
Removed a lot of unneeded newlines
Changed potion making system to id set
Changed right click to better cauldrons
Fixed Mortar & Pestle giving multiple players items
Sorted equipment into folders
Fixed bug with duplicating/transfiguring items caused 713-720 to spawn
Fix problem in remove_armor function allowing players to duplicate armor

---
## [cr4yth/freeram](https://github.com/cr4yth/freeram)@[90b7e66605...](https://github.com/cr4yth/freeram/commit/90b7e666054773c9bfd84c43168f6eea692a86c2)
#### Sunday 2022-07-24 08:14:24 by Shanu Flash #noυ

run command

"The method exec(String, String[]) from the type Runtime is deprecated since version 18" fuck you java

---
## [amir73il/linux](https://github.com/amir73il/linux)@[ab93bbf114...](https://github.com/amir73il/linux/commit/ab93bbf114902c35b4aacbeda0fa60ffd5c89143)
#### Sunday 2022-07-24 08:17:08 by Dave Chinner

xfs: logging the on disk inode LSN can make it go backwards

commit 32baa63d82ee3f5ab3bd51bae6bf7d1c15aed8c7 upstream.

When we log an inode, we format the "log inode" core and set an LSN
in that inode core. We do that via xfs_inode_item_format_core(),
which calls:

	xfs_inode_to_log_dinode(ip, dic, ip->i_itemp->ili_item.li_lsn);

to format the log inode. It writes the LSN from the inode item into
the log inode, and if recovery decides the inode item needs to be
replayed, it recovers the log inode LSN field and writes it into the
on disk inode LSN field.

Now this might seem like a reasonable thing to do, but it is wrong
on multiple levels. Firstly, if the item is not yet in the AIL,
item->li_lsn is zero. i.e. the first time the inode it is logged and
formatted, the LSN we write into the log inode will be zero. If we
only log it once, recovery will run and can write this zero LSN into
the inode.

This means that the next time the inode is logged and log recovery
runs, it will *always* replay changes to the inode regardless of
whether the inode is newer on disk than the version in the log and
that violates the entire purpose of recording the LSN in the inode
at writeback time (i.e. to stop it going backwards in time on disk
during recovery).

Secondly, if we commit the CIL to the journal so the inode item
moves to the AIL, and then relog the inode, the LSN that gets
stamped into the log inode will be the LSN of the inode's current
location in the AIL, not it's age on disk. And it's not the LSN that
will be associated with the current change. That means when log
recovery replays this inode item, the LSN that ends up on disk is
the LSN for the previous changes in the log, not the current
changes being replayed. IOWs, after recovery the LSN on disk is not
in sync with the LSN of the modifications that were replayed into
the inode. This, again, violates the recovery ordering semantics
that on-disk writeback LSNs provide.

Hence the inode LSN in the log dinode is -always- invalid.

Thirdly, recovery actually has the LSN of the log transaction it is
replaying right at hand - it uses it to determine if it should
replay the inode by comparing it to the on-disk inode's LSN. But it
doesn't use that LSN to stamp the LSN into the inode which will be
written back when the transaction is fully replayed. It uses the one
in the log dinode, which we know is always going to be incorrect.

Looking back at the change history, the inode logging was broken by
commit 93f958f9c41f ("xfs: cull unnecessary icdinode fields") way
back in 2016 by a stupid idiot who thought he knew how this code
worked. i.e. me. That commit replaced an in memory di_lsn field that
was updated only at inode writeback time from the inode item.li_lsn
value - and hence always contained the same LSN that appeared in the
on-disk inode - with a read of the inode item LSN at inode format
time. CLearly these are not the same thing.

Before 93f958f9c41f, the log recovery behaviour was irrelevant,
because the LSN in the log inode always matched the on-disk LSN at
the time the inode was logged, hence recovery of the transaction
would never make the on-disk LSN in the inode go backwards or get
out of sync.

A symptom of the problem is this, caught from a failure of
generic/482. Before log recovery, the inode has been allocated but
never used:

xfs_db> inode 393388
xfs_db> p
core.magic = 0x494e
core.mode = 0
....
v3.crc = 0x99126961 (correct)
v3.change_count = 0
v3.lsn = 0
v3.flags2 = 0
v3.cowextsize = 0
v3.crtime.sec = Thu Jan  1 10:00:00 1970
v3.crtime.nsec = 0

After log recovery:

xfs_db> p
core.magic = 0x494e
core.mode = 020444
....
v3.crc = 0x23e68f23 (correct)
v3.change_count = 2
v3.lsn = 0
v3.flags2 = 0
v3.cowextsize = 0
v3.crtime.sec = Thu Jul 22 17:03:03 2021
v3.crtime.nsec = 751000000
...

You can see that the LSN of the on-disk inode is 0, even though it
clearly has been written to disk. I point out this inode, because
the generic/482 failure occurred because several adjacent inodes in
this specific inode cluster were not replayed correctly and still
appeared to be zero on disk when all the other metadata (inobt,
finobt, directories, etc) indicated they should be allocated and
written back.

The fix for this is two-fold. The first is that we need to either
revert the LSN changes in 93f958f9c41f or stop logging the inode LSN
altogether. If we do the former, log recovery does not need to
change but we add 8 bytes of memory per inode to store what is
largely a write-only inode field. If we do the latter, log recovery
needs to stamp the on-disk inode in the same manner that inode
writeback does.

I prefer the latter, because we shouldn't really be trying to log
and replay changes to the on disk LSN as the on-disk value is the
canonical source of the on-disk version of the inode. It also
matches the way we recover buffer items - we create a buf_log_item
that carries the current recovery transaction LSN that gets stamped
into the buffer by the write verifier when it gets written back
when the transaction is fully recovered.

However, this might break log recovery on older kernels even more,
so I'm going to simply ignore the logged value in recovery and stamp
the on-disk inode with the LSN of the transaction being recovered
that will trigger writeback on transaction recovery completion. This
will ensure that the on-disk inode LSN always reflects the LSN of
the last change that was written to disk, regardless of whether it
comes from log recovery or runtime writeback.

Fixes: 93f958f9c41f ("xfs: cull unnecessary icdinode fields")
Signed-off-by: Dave Chinner <dchinner@redhat.com>
Reviewed-by: Darrick J. Wong <djwong@kernel.org>
Signed-off-by: Darrick J. Wong <djwong@kernel.org>
Signed-off-by: Amir Goldstein <amir73il@gmail.com>

---
## [PowerfulBacon/BeeStation-Hornet-Bacons-Fork](https://github.com/PowerfulBacon/BeeStation-Hornet-Bacons-Fork)@[3249b4560b...](https://github.com/PowerfulBacon/BeeStation-Hornet-Bacons-Fork/commit/3249b4560b568fe762f2a695a6427bab7c56c649)
#### Sunday 2022-07-24 09:15:07 by DrDuckedGoose

Lasso Fix (#7345)

* Merge https://github.com/BeeStation/BeeStation-Hornet into annoying-thing Merge conflicts :)

* Initial - 23 7 22

- Doesn't allow dead mobs to be ridden
- Space walk is now specific to the mob

* Actually Fix It - 23 7 22

* Fuck - 23 7 22

- Fix being able to tame human
- Fix being able to tame the dead

* Update carp_lasso.dm

* You boys fucked buckle code - 23 7 22

* Update carp_lasso.dm

* Update riding.dm

* fix icon - 24 7 22

* Review Changes - 24 7 22

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[b83f58a4a6...](https://github.com/mrakgr/The-Spiral-Language/commit/b83f58a4a6fd522b87d372b89b39f4b3176b0415)
#### Sunday 2022-07-24 10:47:03 by Marko Grdinić

"9:10am. I slept like a rock tonight despite getting up 2 times. Despite it, I fell into deep sleep every time.

Any mail? Nope. Tomorrow I have that Kalepa interview at 10:30am. I set the alarm at 10am just in case I oversleep. So I am ready perfectly.

Today my goal will be to finish this tedious Blazor course. Tomorrow the cards might finally arrive by mail and I'll be able to open the AWS account and start learning it.

10:10am. Let me get started. I'll leave the last chapter of Otome Survival for later.

I'll see whether I can finish the course early and take a break for the rest of the day.

https://youtu.be/QKr1HPq6YlI?t=14479

It seem the next assignment is only at the 5:20h mark. Right now I am at 4h. Let me just watch the thing then.

I need to backtrack a little, I forgot how he set up the DBContext. It was the same as in the ASP.NET course. I really should look into Entity Framework in more depth, but it does not matter right now.

10:15am. https://youtu.be/QKr1HPq6YlI?t=14625

What is this Design package for? That wasn't used in the ASP.NET course.

https://youtu.be/QKr1HPq6YlI?t=15549

I am confused at why this has return types.

https://youtu.be/QKr1HPq6YlI?t=16190

Why is he converting to and fro?

https://youtu.be/QKr1HPq6YlI?t=16370

Returning a new `CategoryDTO` object if it can't find it in the database feels like spew.

https://youtu.be/QKr1HPq6YlI?t=16428

This occured to me as well, but I thought the mapper might know on its own to create the DateTime at the current time even if it seemed unlikely.

11:15am. https://www.ycombinator.com/companies/ivy/jobs

Found this on HN, but the pay is really poor. Forget it. I'd rather go into webdev than accept low pay working on a ML library.

Spiral, ML, I am over it. I just need to master the cloud and get the resources to make proper use of it.

11:25am. https://youtu.be/QKr1HPq6YlI?t=16688

He is talking about the lifetimes of the services. I wonder how they are created?

https://youtu.be/QKr1HPq6YlI?t=17383

This is strange. Why does it have to be capital?

https://youtu.be/QKr1HPq6YlI?t=17457

I should mention - with hot reaload, Blazor is actually better for UIs than any of the desktop UI frameworks that I've seen.

11:50am. https://youtu.be/QKr1HPq6YlI?t=17766

I see. Only 25m more until the next assignment. I'll watch up to that point and then take a break.

12pm. https://youtu.be/QKr1HPq6YlI?t=18148

Focus me, let me watch another 20m of this. Lurking the /twg/ thread can come later.

https://youtu.be/QKr1HPq6YlI?t=18308
> I want to think about what could be the issue here?

Is the loading delay due to it having to access the database?

https://youtu.be/QKr1HPq6YlI?t=18349

Ah, I see. Would the solution be to make it async?

https://youtu.be/QKr1HPq6YlI?t=18711

Does not hesitate to copy paste.

https://youtu.be/QKr1HPq6YlI?t=18905

I am not sure that this is how I'd design it. I can think of better ways. Using whether `id == 0` to differentiate between create and update? Spew.

The guy is certainly knowledgeable about Blazor, but his general skills could be better.

https://youtu.be/QKr1HPq6YlI?t=19041

Does `.modal` show a page as a popup?

12:30pm. https://youtu.be/QKr1HPq6YlI?t=19195

I am starting to tune out. Just 10m more and I can take a break. Let me just plow through this.

https://youtu.be/QKr1HPq6YlI?t=19236

This JS confuses me. I am going to have to look into what it is supposed to be doing.

12:40pm. https://youtu.be/QKr1HPq6YlI?t=19501

Let me pause here. This seems like a simple assignment, except I haven't been following step by step and will have to build it up to the point where I can do the assignment. All of that using only the finished ref will be more challenging by far than the assignment itself. It should make for a decent bit of learning. Once I am done with this, I'll have completed my first CRUD app.

12:45pm. The most difficult part for me would be replicating the styling. I'll have to look at the finish code for most of it, but nevermind that. It is not relevant to the functionality.

Let me have breakfast here."

---
## [yogstation13/Yogstation](https://github.com/yogstation13/Yogstation)@[5bbc6a2401...](https://github.com/yogstation13/Yogstation/commit/5bbc6a2401361e71f4c6fb0ad173900153603787)
#### Sunday 2022-07-24 11:06:10 by Marmio64

Sinful demon changes + re-enable (#14345)

* first wave of demon changes

many changes
1: gluttonous demons hunger 3x as fast as normal people
2: all demons no longer enter softcrit (still can enter hardcrit), are geneless, dont suffocate in crit, and have stable hearts.
3: true demon form deals 20 damage instead of 24 (wrath is 24 instead of 28). Health is lowered to 160 and health regen per hit is now 8 instead of 10. To compensate, they are ever so slightly faster, but are still slower than everyone but podpeople. Demons also lose 2 hp every life tick (a life tick is generally 2 seconds, so 2 hp every 2 seconds), so as to try to deter you from staying in demon form the entire round.
4: objectives are made a bit less murderbone-ey.
5: sinful demon spawns slightly less often

* re enables event

* fixes

* removes chance for envy to get an identity theft objective

* word change

* sinful demon is rarer still

honestly, they arent very interesting if they happen too much, so i'd like them to mildly rare

Co-authored-by: Jamie D <993128+JamieD1@users.noreply.github.com>

---
## [ZIPING-LIU-CORPORATION/icecream-man](https://github.com/ZIPING-LIU-CORPORATION/icecream-man)@[1ba97648f2...](https://github.com/ZIPING-LIU-CORPORATION/icecream-man/commit/1ba97648f2cd609f67a2464dcc821d84b1592913)
#### Sunday 2022-07-24 11:25:06 by zipingl

feat: update ticket with msg transcript released - add cross origin allow to pdf file, https required fo content, and that's mainly because Amazon Legal thought the rules of law determine one's guilt as if the human condition is govnernmed by a set of laws man wrote for himself, no amazon legel, it's always the idiots like you Adam Selipsky who are so behind in the human brain developent index that you think you can determine my guilt and wrong from these laws, and by laws of your watever corporation, like moving chess pieces on a 8 U.S. Inch ruled by 8 U.S. Inch ruled chess board, with your attorney pawns. And when told that's not okay. What do you do? Your executive powers and your years of wisdom tell you to have the ERC ask for my first name AND NOT FUCKING PAY ME, SINCE APRIL 2022, YOU STILL HAVE NOT PAID ME, HOW ARE YOU THIS BAD AT LEGAL PROCEDURES?

---
## [EdwardNashton/mojave-sun-13](https://github.com/EdwardNashton/mojave-sun-13)@[a7a0e33192...](https://github.com/EdwardNashton/mojave-sun-13/commit/a7a0e33192ad3fcac5ad64d441f24af6ec852054)
#### Sunday 2022-07-24 11:56:42 by Hekzder

Mob overhaul for DT (#2117)

* Basic mobs

Title

* Start of simple robots

Title

* THE GREAT MOB SOUNDENING

TITLE

* Handies + ranged attack buffs

FASTER!!

* Protectrons, robobrains

* Death sounds and fixes some dumb shit

Title

* NEW ROACHES OMG!!!

WOW!

* Robo sounds

Title

* Mob projectile tweaks

I THINK WE'RE GOOD

* bitty

---
## [Aryan-Rajoria/free-programming-books](https://github.com/Aryan-Rajoria/free-programming-books)@[97016edd67...](https://github.com/Aryan-Rajoria/free-programming-books/commit/97016edd6791285128758dd91904b343d1f3b0fd)
#### Sunday 2022-07-24 12:22:41 by David Ordás

Add CodingFantasy's CSS coding interactive games (#5490)

* Add "Knights of the Flexbox table" game

Welcome to the Knights of the Flexbox table. A game where you can help Sir Frederic Flexbox and his friends to uncover the treasures hidden in the Tailwind CSS dungeons.
You can navigate the knight through the dungeon by changing his position within the dungeon using Flexbox and Tailwind CSS.

* Add "Flex Box Adventure" game

Once upon a time, there was a King Arthur. He ruled his kingdom fair and square. But Arthur had one problem. He was a very naive person. So one sunny day, three alchemist brothers offered Arthur to exchange all his Gold Coins for coins made of a more valuable new metal that they had invented - Bit Coins.

Arthur believed them and gave them all his gold. The brothers took the gold and promised to give the bit coins back to Arthur in seven days.

Seven days passed. The brothers have not turned up. Arthur realized he had been scammed. He is angry and intends to take revenge on them. Let's help him do it with our weapon – CSS Flex Box!

We made this game for You
1. You often stumble and try to figure out which combination of Flex Box properties makes the browser do what you want it to do.

2. You want to create complex web layouts without constantly looking at the web page after every Cmd/Ctrl+S press in the code editor.

3. You have tried to learn Flex Box with video tutorials and articles but still don't fully understand how some parts of it work.

4*. Or, if you are a master of CSS Flex Box, we have something interesting and for you too (read further).

Have you found yourself there? Then you definitely want to learn or improve your Flex Box skills. So we have good news for you, really good news...

Learn Flex Box by Playing Game
No more boring videos, tutorials and courses. Learn Flex Box in a completely new, fun, effective and revolutionary way. By playing Flex Box coding game!

* Add "Grid Attack" coding game

In an ancient Elvish prophecy, it was said that one day a man would be born with an incredible power that predicts the future – "Marketi Predictori." And another will come to take this power. But the years went by and nothing happened. Until one day, a little elf was born. He was named Luke.

From an early age, he surprised his parents and his sister Rey by guessing the price of apples at the farmer's market before they even reached it. Every year his power rose and his predictions became more and more accurate. But there was one thing Luke could not predict. The coming of the demon Valcorian. It was the one from the prophecy that was to come and take Luke's power. One day Valcorian and his army attacked the town where Luke had lived and kidnapped him to make a ritual of stealing his power.

Go on a dangerous quest with Luke's sister Rey and find her brother. Defeat Valcorian and all his demons using a secret weapon – CSS Grid.

We made this game for You?
1. You often stumble and try to figure out which combination of Grid properties makes the browser do what you want it to do.

2. You are scared by the number of properties a CSS Grid has, and you feel uncomfortable when you need to create a grid layout.

3. You want to create complex web layouts using Grid, but without constantly looking at the web page after every "Cmd/Ctrl+S" press in the code editor.

4. You have tried to learn CSS Grid with video tutorials and articles but still don't fully understand how some parts of it work.

5. You use a Flex Box where Grid is required because you don't feel confident in using it.

Have you found yourself there? Then you definitely want to learn or improve your Grid skills. So we have good news for you, really good news...

Learn Grid by Playing CSS Game
No more boring videos, courses and articles. Learn Grid in a revolutionary new, fun, and effective way. By playing a Grid coding game!

---
## [eun0115/android_kernel_samsung_universal7904](https://github.com/eun0115/android_kernel_samsung_universal7904)@[5673ece30d...](https://github.com/eun0115/android_kernel_samsung_universal7904/commit/5673ece30d2d333de4aed699e899cd5e96e0ac74)
#### Sunday 2022-07-24 13:00:49 by Masahiro Yamada

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
## [JihadZoabi/Aleph](https://github.com/JihadZoabi/Aleph)@[7b23eae9e9...](https://github.com/JihadZoabi/Aleph/commit/7b23eae9e905c0c7d2246c5a5ec5528b15613eab)
#### Sunday 2022-07-24 13:37:45 by Eyal Z

How much would it cost to rent out an entire Apple store for a wedding?

My fiancé (25F) and I (47M) are lovers of all things Apple. We have only Mac laptops and desktops, only watches we own are Apple watches and have only used iPhones since 2007. We are wanting to get married in an Apple store somewhere near us, closest being Chicago.

Does anyone know how much it would cost to rent out an entire Apple store for the entire weekend? We would have the rehearsal, rehearsal dinner and then wedding ceremony and wedding reception. We are thinking a full 3 course meal served by the geniuses themselves.

Any information would be great. Thank you.

---
## [Aevann1/rDrama](https://github.com/Aevann1/rDrama)@[856f155b41...](https://github.com/Aevann1/rDrama/commit/856f155b4138c40efeb31b1cbf628abee8115958)
#### Sunday 2022-07-24 15:03:21 by DrTransmisia

Errorcodejihad (#323)

* formatmaxxing brained formatting

* formatmaxxing brained formatting: EPISODE 2

* Start implementing a .json interface for all logged users reddit-like

PROs:
- easier to debugmaxx applications
- good faith actors can scrap the site more easly :gigachadglow:
CONs:
- bad faith actors can scrap the site more easly :gigachadglow:
- jannitors lose a little of their power of allowlisting applications (they do it for free though)

anyways. I make this commit a separate commit so that Snakes can esclude it from the PR if he doesn't like it (cringe)

* /<username>/comments route now returns appropriate [citation needed] HTTP codes when called in JSON mode so that stupid JSON clients can crashmaxx

* More error codes (sorry I don't know how to squash)

* json endpoint. see other commit. I don't know how to squash

---
## [newstools/2022-iol-the-mercury](https://github.com/newstools/2022-iol-the-mercury)@[3c395c394d...](https://github.com/newstools/2022-iol-the-mercury/commit/3c395c394def11e307592b97b7f74db473f9bf5b)
#### Sunday 2022-07-24 16:54:31 by Billy Einkamerer

Created Text For URL [www.iol.co.za/mercury/dailynews/news/kwazulu-natal/woman-allegedly-orchestrates-kidnapping-murder-of-her-ex-boyfriends-current-girlfriend-91265bda-f862-4523-9e8b-d16648b5b4be]

---
## [mattsta/mutil](https://github.com/mattsta/mutil)@[926a0bb8ae...](https://github.com/mattsta/mutil/commit/926a0bb8ae6ec33571085564e685dddf86406e8e)
#### Sunday 2022-07-24 17:10:16 by Matt Stancliff

Fix websocket serving under adversarial API users

Are you sending a weird state value? We'll fix it for you. Are you
providing a callback handler with too few parameters? We'll just call it
with fewer parameters.

(the state management hack is very ugly and should be fixed upstream
elsewhere, but we can't actually figure out why the state's embedded
state state isn't showing up properly anymore... so this is a big hack
for now until we can fix the wrappers elsewhere)

Also fixes the actual websocket serving to not just outright exit when
it receives 2 MB of data at once because the default buffers are
configured too small and provides no meaningful feeedback why it
self-disconnects under typical usage scenarios. thanks everybody.

---
## [PixelExperience-Devices/kernel_motorola_exynos9610](https://github.com/PixelExperience-Devices/kernel_motorola_exynos9610)@[ba75cca4b2...](https://github.com/PixelExperience-Devices/kernel_motorola_exynos9610/commit/ba75cca4b2b33194761ff0939d221e434e65d8b7)
#### Sunday 2022-07-24 18:06:26 by Maciej Żenczykowski

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
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Cc: Dongseok Yi <dseok.yi@samsung.com>
Cc: Willem de Bruijn <willemb@google.com>
Link: https://lore.kernel.org/bpf/CANP3RGfjLikQ6dg=YpBU0OeHvyv7JOki7CyOUS9modaXAi-9vQ@mail.gmail.com
Link: https://lore.kernel.org/bpf/20210617000953.2787453-2-zenczykowski@gmail.com

(cherry picked from commit 364745fbe981a4370f50274475da4675661104df https://git.kernel.org/pub/scm/linux/kernel/git/bpf/bpf-next.git/commit/?id=364745fbe981a4370f50274475da4675661104df )
Test: builds, TreeHugger
Bug: 188690383
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Change-Id: I0ef3174cbd3caaa42d5779334a9c0bfdc9ab81f5

---
## [2001-kushalbasak/Alopath](https://github.com/2001-kushalbasak/Alopath)@[9db7da35cf...](https://github.com/2001-kushalbasak/Alopath/commit/9db7da35cf29690d97e89e905cd61f56d73fe7b1)
#### Sunday 2022-07-24 18:41:38 by Kushal

update functionality added successfully.... 25-07-2022 four unplaced unemployeed peacemakers under one roof full of dreams sorrows desires ..no worries my boys a day will come soon in our lives when all our dreams wil come true when we can feel rather see what life looks like we will have lots of fun that day.... peace out babbby..

---
## [beistroff/Links-forms](https://github.com/beistroff/Links-forms)@[87cfccaa24...](https://github.com/beistroff/Links-forms/commit/87cfccaa24d1f4d2011cbd841a0219aeb8e6000f)
#### Sunday 2022-07-24 18:59:10 by beistroff

Add files via upload

Some of details: 
1. links.html - the first task 
2. forms.html - the second task (1 srceen)
3. divide-form.html - the second task (2 screen)
4. loginform-rozetka.html - 3 screen (3 screen)
5. second-rozetkaform.html - 4 screen (4 screen)

So, when I started to create form which seems to be from rozetka page, i gave some additional experience and my work is not brilliant. 
I used not the same close button which in right top corner on the screen, cause it's svg type, also some of icons.
Overall, it's cool but i made a big mistake with custom checkbox (in order to click on checkbox, u need to click nearly to the checkbox, not on the exact box).
And idk how to fix it, I sure that i made some of mistake, but i tried hard to find and fix it. I just burnt out and make a decision to do it later. 
Hope You will enjoy it!

---
## [parautenbach/Home-Automation](https://github.com/parautenbach/Home-Automation)@[21c16dee0f...](https://github.com/parautenbach/Home-Automation/commit/21c16dee0fb5e413fbd6a02a1153fd461a0aaa19)
#### Sunday 2022-07-24 19:04:04 by Pieter Rautenbach

Tomorrow.io fuck you – really, fuck you

Most unreliable weather service ever and no support. Can't even get logged in. Just stuck in a loop.

---
## [WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/FEDERAL-USE-AND-DISTRIBUTION-ONLY](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/FEDERAL-USE-AND-DISTRIBUTION-ONLY)@[3f32a09c30...](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/FEDERAL-USE-AND-DISTRIBUTION-ONLY/commit/3f32a09c3045e9dfd34d5d89b4ed5d3b1b43d9b9)
#### Sunday 2022-07-24 20:24:08 by WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER

Subject: 	Fwd: LERNER HALL, BUTLER LIBRARY, HOW ABOUT EVERY BUILDING SURROUNDING THE LOW LIBRARY.

I don't know, ask the parents of COLUMBIA UNIVERSITY IN THE CITY OF NEW YORK
ABOUT:  how they feel about it, just make sure it is on the front page of the ADMISSIONS, or APPLICATION -- PRIOR to their VIOLATION OF PRIVACY
as exhibited in NYSCEF 153974/2020 --- > peeping tomcats. 


> ALL BELONG IN PRISON.
> LET me know how many students can SAFELY enroll at this point in time, without having their PRIVACY violated, notwithstanding their CIVIL RIGHTS, et. al.


-------- Forwarded Message --------
Subject: 	Fwd: LERNER HALL, BUTLER LIBRARY, HOW ABOUT EVERY BUILDING SURROUNDING THE LOW LIBRARY.
Date: 	Sun, 24 Jul 2022 16:17:34 -0500
From: 	B D2022 <ms60710444266@yahoo.com>
To: 	72pctdvo@nypd.org <72pctdvo@nypd.org>, 72pctyco@nypd.org <72pctyco@nypd.org>, 90pctdvo@nypd.org <90pctdvo@nypd.org>, bdincer66@icloud.com <bdincer66@icloud.com>
CC: 	MARTY.ROWLAND@PARKS.NYC.GOV <MARTY.ROWLAND@PARKS.NYC.GOV>, ogis@nara.gov <ogis@nara.gov>



you cannot keep that institution OPEN while they peek into other students dorms, condos, and apartments without consent.

>> It is illegal, no matter how much money you have - without consent, NOT PERMITTED BY LAW and IN ANY JURISDICTION WITHOUT EXPLICIT CONSENT.


-------- Forwarded Message --------
Subject: 	LERNER HALL, BUTLER LIBRARY, HOW ABOUT EVERY BUILDING SURROUNDING THE LOW LIBRARY.
Date: 	Sun, 24 Jul 2022 16:15:28 -0500
From: 	B D2022 <ms60710444266@yahoo.com>
To: 	Doc Webmaster <webmaster@doc.gov>, tmprosecutordocs@uspto.gov <tmprosecutordocs@uspto.gov>, SARAH 00068govtIdx BARNHART <SarahB@doc.ks.gov>, MICHAEL 00064govtIdx OSVER <mosver@doc.gov>, Karol.Sabodocha@nypd.org <Karol.Sabodocha@nypd.org>, HREmployeeServices@doc.nyc.gov <HREmployeeServices@doc.nyc.gov>, doc@dc.gov, doc-del@libraries.cul.columbia.edu, Constituentservices@doc.nyc.gov <Constituentservices@doc.nyc.gov>, CHERYL 00068govtIdx CADUE <CherylCa@doc.ks.gov>, bdocs2019@gmail.com, support@nicic.gov <support@nicic.gov>, NYM-PREAComplianceMgr-S@bop.gov <NYM-PREAComplianceMgr-S@bop.gov>, Bop Info <info@bop.gov>, CNK-CCM@bop.gov <CNK-CCM@bop.gov>, BRO-ExecAssistant-S@bop.gov <BRO-ExecAssistant-S@bop.gov>, BOP-RSD-PREACOORDINATOR@bop.gov <BOP-RSD-PREACOORDINATOR@bop.gov>, BOP-IPP-PublicAffairs@bop.gov <BOP-IPP-PublicAffairs@bop.gov>, acjic@alacop.gov, ANNETTE 00000govtIdx FORD <ANNETTE.R.FORD@USDOJ.GOV>, CAROL 00000govtIdx BURGER <CAROL.S.BURGER@USDOJ.GOV>, dojfax@bops.gov, Randyc.wilson@usdoj.gov <Randyc.wilson@usdoj.gov>, tina.jeffery@usdoj.gov <tina.jeffery@usdoj.gov>, Victimassistance.fraud@usdoj.gov <Victimassistance.fraud@usdoj.gov>, 4audit@bloomberg.net <4audit@bloomberg.net>, CRC FTC REPORTS <CRCMESSAGES@ftc.gov>, crcomplaints@treasury.gov <crcomplaints@treasury.gov>, TheBronxBBJccl@gmail.com, QueensBBJccl@gmail.com, BrooklynBBJccl@gmail.com
CC: 	1pctyco@nypd.org <1pctyco@nypd.org>, Ashley V. Humphries <ashley.humphries@wilsonelser.com>, inbox@livekelly.com <inbox@livekelly.com>


you cannot keep that institution OPEN while they peek into other students dorms, condos, and apartments without consent.

>> It is illegal, no matter how much money you have - without consent, NOT PERMITTED BY LAW and IN ANY JURISDICTION WITHOUT EXPLICIT CONSENT.


-------- Forwarded Message --------
Subject: 	Fwd: Fwd: 612 West 115th Street (Watson Hall, 8th floor)
Date: 	Sun, 24 Jul 2022 16:08:18 -0500
From: 	B D2022 <ms60710444266@yahoo.com>
To: 	royalty.statements@sonymusic.com <royalty.statements@sonymusic.com>, realtime@sonymusic.com <realtime@sonymusic.com>, privacy@sonymusic.com <privacy@sonymusic.com>, secretariat@impforum.org <secretariat@impforum.org>, dgosset@impalamusic.org <dgosset@impalamusic.org>, info@immf.com <info@immf.com>, press@ifpi.org <press@ifpi.org>, secretariat@icmp-ciem.org <secretariat@icmp-ciem.org>, office@fim-musicians.org <office@fim-musicians.org>, tom.cording@sonymusic.com <tom.cording@sonymusic.com>, angela.barkan@sonymusic.com <angela.barkan@sonymusic.com>, karyan.diaz@sonymusic.com <karyan.diaz@sonymusic.com>, allen.brown@sonymusic.com <allen.brown@sonymusic.com>, publicity@rcarecords.com <publicity@rcarecords.com>, columbia.publicity@sonymusic.com <columbia.publicity@sonymusic.com>, FrontDesk@LoungeStudiosNYC.com <FrontDesk@LoungeStudiosNYC.com>, head office <headoffice@icmpmusic.com>, Martin.Rowland@parks.nyc.gov <Martin.Rowland@parks.nyc.gov>, pietro.villani@icmpmusic.com <pietro.villani@icmpmusic.com>, info@sagaftra.org <info@sagaftra.org>, sean.combs@icmpmusic.com
CC: 	1pctdvo@nypd.org <1pctdvo@nypd.org>

YOU'RE GOING TO ALLOW THEM TO CONTINUE TO TREAT THEIR STUDENTS LIKE THAT?
- AS A PRIVATE INSTITUTION?

YOU CAN'T ALLOW THAT EITHER... IT DOESN'T MATTER HOW MUCH MONEY THEY HAVE.
>> THOSE CAMERAS --- ARE ALL MONITORED AND EVEN IN MY APARTMENT
- AS PROVIDED EARLIER, NEED TO RECORD MY CONVERSATIONS FOR SOMETHING YOU REALLY DON'T WANT TO KNOW ASHLEY.

> WHICH IS WHY, I BEG YOU TO PLEASE TAKE MY ADVICE, IN GOOD CANDOR - NOT LEGAL ADVICE, THAT'S LIFE.



THAT LINK - IS NOT WHAT I EXPECTED EITHER---

https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/files/8085790/LEGAL.OPINIONS.OGC.2022.02.16.pdf

-------- Forwarded Message --------
Subject: 	Fwd: 612 West 115th Street (Watson Hall, 8th floor)
Date: 	Sun, 24 Jul 2022 16:05:51 -0500
From: 	B D2022 <ms60710444266@yahoo.com>
To: 	REDACTED



THESE PEOPLE ARE TRULY DISTURBED, PEEPING TOMCATS.

THANK YOU FOR YOUR HELP
-------- Forwarded Message --------
Subject: 	Re: 612 West 115th Street (Watson Hall, 8th floor)
Date: 	Sun, 24 Jul 2022 16:03:14 -0500
From: 	B D2022 <ms60710444266@yahoo.com>
To: 	pblaer@cs.columbia.ed, pbr@columbia.edu


TOLD YOU TOMMY... IT'S THAT BAD.

1. https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=ANDSuLFWlbjttGxgjUXGAw==

    COLURFUL, HOWEVER WITHOUT CONSENT WAS VIDEOTAPED WHILE ALL THOSE MEMBERS, AS REPORTED...
    -     IN THE LEWISOHN HALL, AND ON THEIR PERSONAL DEVICES DISTRIBUTED AND HOSTED THOSE VIDEOS WITHOUT MY CONSENT.
    -    AN INTEDETERMINATE NUMBER OF VIDEOS.
    -    WATCHED ME BUTT NAKED, DRESSED, AND WITHOUT CONSENT.. DESPITE HAVING FILED A CEASE AND DESIST ORDER IN A NEW YORK SUPREME COURT OF LAW, IN JUNE OF 2020.
    -    CASE:    NYSCEF 153974/2020

2. https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=fXMaXgeyzvA85ViWMmvfAQ==
3. https://lnkd.in/gMRuiQsn

those are the links in the description I provided.
>> i left them out of this part in to TO area....
LETS see who I reported and IF/WHAT they tell you about THEIR INVOLVEMENTS

.... they are in FACT: PEEPING TOMS, WALKING FELONS WITHOUT A CHARGE, ARRAIGNMENT DATE, AND

HINT: I have no idea what backyard those servers may hold those videos either - PEEPING TOMCATS, ARE ABOVE YOU BEYOND WHERE THE EYE CAN SEE.








On 7/24/2022 3:52 PM, B D2022 wrote:
> 70 Morningside: STUDENT MAIL CENTER, "hsbc also in the description"
>
> > i just filed with using maxient - a columbia system.
> https://cm.maxient.com/reportingform.php?ColumbiaUniv&layout_id=5
>
> Medical Center: By Appointment
> Hours of operation are: Monday-Friday, 9 am - 5 pm with the exception of University holidays
>
> SEE ALSO: ARGUMENTS ABOUT MY OPINION ON WHETHER OR NOT I WANT "GOD" IN MY LIFE.
> >> THEY ALSO HAD AN ISSUE FOR THAT, AND ISSED A CONDUCT LETTER TO AID, ABET AND FURTHER OBSTRUCT THE RELEASE OF MATERIAL INFORMATION AND DURING A FEDERAL BANK AND SECURITIES INVESTIGATION.
>
>
> ATTACHED
>
> >>    SCCS BOWE HEARING LETTER NOV 19 - 2021 -AGREED.pdf

---
## [WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/RELATIVES](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/RELATIVES)@[df0ed6c212...](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/RELATIVES/commit/df0ed6c212ba9cadb8ea4e803f0be6f142f21f4d)
#### Sunday 2022-07-24 21:03:27 by WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER

all FELONIES <locked> I need to call 1 person to CONFIRM 1 thing.

DO YOU REALLY WANT GOD IN YOUR LIFE, MR MAXIENT? <locked>

SHORT LIST OF FEDERAL CHARGES APPLICABLE AND FILED IN NYSCEF 153974-2020.TXT
18.214 -Offer for procurement of Federal Reserve bank loan and discount of commercial paper.TXT
18.220 - Illegal remunerations for referrals to recovery homes - CLINICAL TREATMENT KICKBACKS.TXT
18.218 - VOIDING TRANSACTIONS.TXT
USC 18.373(B)[ VOICEMAIL ] MOTIVATED COMMANDING OR TO POSTPONE - OR SUBSTITUTE ANOTHER VICTIM.TXT
USC 18.1962 AND USC 18.1963 VIOLATED WITH NYSCEF LINKS.TXT
USC 18.1962 VIOLATED.TXT
18.152 -- CONCEALMENT OF ASSETS UNDER THE SCOPE OF AVOIDANCE TO A TECHNICAL BANKRUPTCY ( A GREY AREA ).TXT
SHORT LIST OF MEMBERS AT SULLIVAN PROPERTIES LP.txt
18.208 - ACTS AFFECTING A PERSONAL FINANCIAL INTEREST.TXT
18.208 - ACTS AFFECTING A PERSONAL FINANCIAL INTEREST (2).TXT
18.115- THREATENING INJURY TO IMPEDE - INTIMIFFATE OR INTERFERE WITH AN OFFICIAL.TXT
18.115 - INFLUENCING - IMPEDING - OR RETALIATING AGAIN A FEDERAL OFFICIAL BY THREAT OR INJURY.TXT
January 1 2020 to January 1 2023 - [40-17G] NOT COVERED TWO INDENTURES.txt
TaxEfiled@law.nyc.gov -- TAXEFILED.TXT
Block 2679- Lot 43- 840-46 Lorimer Street - KCCO-EFILE.txt
Filing User Shari Laskowitz - 2129079600 NYSCEF 153974-2020.txt
Your fax to Nancy T. Sunshine. could not be delivered-VIOLATIONOFPRIVACY LINKS IN NYSCEF 153974.TXT
29 JUNE 2020 courtyard - RICKI.ROER-AT-WILSONELSER.TXT
civil.rights.division - FEBRUARY 20 - 2022.TXT
rosalia-chann---VIDEO.ON-DEMAND.DOMAIN.REGISTER.TXT
05 JUNE 2020 - ITEM 53 - ITEM 55.txt
JAN 30-2022 - EMAIL TO WILSONELSER AS ATTORNEYS ON RECORD NYSCEF 153974-2020.txt
JUNE 28 2022-malia.d.chatman.TXT
STATE FARM - BLOOMINGTON-Northern Trust Company-ACRIS-6MM.txt
Hon. Nancy T. SunshineNYSCEF 400842-2020 - THE ZUCKER ENTERPRISES LLC receipt.TXT
2022-01-30-WILSONELSER-THE-CONARTISTS.txt
04.2020-Defendants attest and document to circulating communications WITHOUT MY CONSENT.TXT
ATTORNEYS IN NYSCEF 153974 AND THEY BAR NUMBERS.txt
ATTORNEYS IN NYSCEF 153974 AND THEY BAR NUMBERS (2).TXT
INVESTORS OF STFGX - SFITX - SFBDX - STFBX receipts.txt
VIOLATION OF PRIVACY AND BREACH OF DUTIES.txt
150 EAST 42ND STREET INDIVIDUALS LISTED .txt
DOCUMENT CCF_000031 EXECUTED ON AUGUST 8TH 2020 IN GOOD FAITH.txt
[USC 18.225] docket 403 - FILED 2020 MAY 15 - CRFN 2020000155422 - 6MM LOAN BY STATE FARM.TXT
RFC822 - MSG READ RECEIPTS = [ BSCPGROUPHOLDINGSLLC-WILSONELSER-ZUCKER] #50074.txt
USC 18.2 - Principals - THOSE WHO COMMIT AN OFFENSE AGAINST THE UNITED STATES - NOTWITHSTANDING ACCESSORIES.TXT
USC 18.1963 - forfeit to the United States all property described - INCLUDING REAL PROPERTY.TXT
USC 18.1962 - PINCOME DERIVED FROM COLLECTIONS OF UNLAWFUL DEBT.TXT
USC 18.373 - SOLICITATION TO CORROBORATE AND INDUCE UNDER CIRCUMSTANCES STRONGLY CORROBORATIVE OF THAT INTENT.TXT
THIS PAGE IS BEING MONITORED BY SEVERAL DEPARTMENTS AS PART OF A FEDERAL INVESTIGATION.txt
BANGING ON A RADIATOR.txt
ATTACHED VIDEO OF MYSELF HAMMERING INSIDE OF MY APARTMENT.txt
ATTACHED VIDEO OF MYSELF DRILLING INSIDE OF MY APARTMENT.txt
DISTRIBUTED VIDEOS OF MYSELF IN MY APARTMENT -- THE INTERIOR.txt
VIDEOTAPED ME - INSIDE OF MY APARTMENT -.txt
VIDEO.MOV FILES - DISTRIBUTED WITHOUT CONSENT.TXT

---
## [OpenImageIO/oiio](https://github.com/OpenImageIO/oiio)@[afc2bd1649...](https://github.com/OpenImageIO/oiio/commit/afc2bd1649a921c56192bbf8c3b326b137237c31)
#### Sunday 2022-07-24 21:37:36 by Larry Gritz

parallel.h refactoring and add support for TBB (#3473)

Hide nearly all of the implementation of the parallel_for family of
methods rather than expose them as inline. This gives us more freedom
to change the implementation in the future without breaking ABI.

Deprecate the parallel methods that take task functions whose first
parameter is the thread ID. The only reason they existed is because
our cobbled together thread_pool used that in its inner workings.  But
there are good reasons why we should not expose that:

  * We never used it anyway.

  * It was not very useful, since sometimes it was a real thread ID, but
    other times it was -1 in cases where the calling thread executed the
    task directly.

  * It is inconsistent with other thread pool implementations that we may
    wish to try in the future.

So better just to not expose those thread IDs at all. Mark those
versions of the parallel loops as deprecated and schedule them for
removal in OIIO 3.0.

If TBB is detected at build time, support will be built in that allows
either the old OIIO built-in pool, or TBB, depending on the setting of
a new global OIIO attribute, "use_tbb" (default 0), if set to nonzero
will use the TBB thread pool.

In my experiments, the TBB thread pool seems slightly better -- I
think because there is less overhead, and maybe the clever
work-stealing it does elps to load balance. It's not used by default,
set the attribute if you want to use it (assuming the build
included. After we've had a chance to test more thoroughly, we may
change to use TBB by default. I'm interested to hear people's thoughts
on the matter.

One case where you almost certainly will want to use the TBB thread
pool is if you're using libOpenImageIO from within an application that
uses TBB for its own threding -- that way you're using one pool for
everything, rather than have two separate thread pools that don't know
about each other (and probably twice as many threads as you have
cores)..

---
## [chadvandy/nagash](https://github.com/chadvandy/nagash)@[7060e9e6fe...](https://github.com/chadvandy/nagash/commit/7060e9e6fe7dbf0bb3ed94e819a36abacab250d8)
#### Sunday 2022-07-24 21:40:06 by Scott (JvJ)

Economy changes and some bug fixes

- removed tomb guard/halberds from subhorde T3 war beast chain
- small growth tweaks across the board for hordes
- settlements +15 base growth, should help to compensate from the lack of province growth from T2/T3 settlements
- settlement major main chain income increased 10/15/20/25 % increase per tier (mostly effects special settlements because growth) T1 income remains the same
- settlement minor main chain income +25
- settlement income chain now 150/250/400
- horde BP/Mort/Sub horde Industry chain added a base 50 to all tiers
- syphon outpost chain effect now province wide, removed LD debuff, enemy forces start winded (hopefully will push less reliance on the income chain)
- corruption outpost chain now gives a small but spooky garrison
- arkhan staff no longer gives PO bonuses
- husk dark conduit skill now correctly gives +2 horde growth
- husk innate now gives additional growth
- fixed dodgy building chain slot unlock (left over from a previous attempt at being clever)
- removed loc references to dodgy building chain slot unlocks
- added references to spirit hosts and fell spectres for the ancient terrors red line skill loc.
- wight king/vampire/gunnery wight mounts now correctly applied
- fixed capacity issue with wight kings and tomb princes
- fixed krell anc typo

---
## [Zomis/Games](https://github.com/Zomis/Games)@[399147981c...](https://github.com/Zomis/Games/commit/399147981c9c9e80caa303bf981e9b4f28c1f25a)
#### Sunday 2022-07-24 22:05:07 by Simon Forsberg

Add generic copy/fork method, with a shit-ton of debugging (See #291)

Deliberately making this commit bigger than it has to be to better show my thought process. Hopefully someone at some point will take a look at it and either learn something about it, or laugh about it.

The extra debugging will be removed soon again, enjoy it while it lasts. Luckily, Git history lasts forever.

---
## [emersonford/clap](https://github.com/emersonford/clap)@[d43f1dbf6f...](https://github.com/emersonford/clap/commit/d43f1dbf6f1f7865dccfece0e1605a12efb76670)
#### Sunday 2022-07-24 23:11:00 by Ed Page

docs: Move everything to docs.rs

A couple of things happened when preparing to release 3.0
- We needed derive documentation
  - I had liked how serde handled theres
  - I had bad experiences finding things in structopt's documentation
- The examples were broken and we needed tests
- The examples seemed to follow a pattern of having tutorial content and
  cookbook content
- We had been getting bug reports from people looking at master and
  thinking they were looking at what is currently released
- We had gotten feedback to keep down the number of places that
  documentation was located

From this, we went with a mix of docs.rs and github
- We kept the number of content locations at 2 rather than 3 by not
  having an external site like serde
- We rewrote the examples into explicit tutorials and cookbooks to align
  with the 4 styles of documentation
- We could test our examples by running `console` code blocks with
  trycmd
- Documentation was versioned and the README pointed to the last release

This had downsides
- The tutorials didn't have the code inlined
- Users still had a hard time finding and navigating between the
  different forms of documentation
- In practice, we were less likely to cross-link between the different
  types of documentation

Moving to docs.rs would offer a lot of benefits, even if it is only
designed for Rust-reference documentation and isn't good for Rust derive
reference documentation, tutorials, cookbooks, etc.  The big problem was
keeping the examples tested to keep maintenance costs down.  Maybe its
just me but its easy to overlook
- You can pull documentation from a file using `#[doc = "path"]`
- Repeated doc attributes get concatenated rather than first or last
  writer winning

Remember these when specifically thinking about Rust documentation made
me realize that we could get everything into docs.rs.

When doing this
- Tutorial code got brought in as was one of the aims
- We needed to split the lib documentation and the README to have all of
  the linking work.  This allowed us to specialize them according to
  their rule (user vs contributor)
- We needed to avoid users getting caught up in making a decision
  between Derive and Builder APIs so we put the focus on the derive API
  with links to the FAQ to help users decide when to use one or the
  other.
- Improved cross-referencing between different parts of the
  documentation
- Limited inline comments were added to example code
  - Introductory example code intentionally does not have teaching
    comments in it as its meant to give a flavor or sense of things and
    not meant to teach on its own.

This is a first attempt.  There will be a lot of room for further
improvement.  Current know downsides:
- Content source is more split up for the tutorials

This hopefully addresses #3189

---

