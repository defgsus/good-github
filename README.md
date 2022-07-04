## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-07-03](docs/good-messages/2022/2022-07-03.md)


1,625,622 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,625,622 were push events containing 2,142,594 commit messages that amount to 130,287,909 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 25 messages:


## [zmingee/dwm](https://github.com/zmingee/dwm)@[daa26f2220...](https://github.com/zmingee/dwm/commit/daa26f2220e69031ac9ca166d1e7ce7553e0d010)
#### Sunday 2022-07-03 01:17:04 by Chris Down

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
## [mengzhisuoliu/terminal](https://github.com/mengzhisuoliu/terminal)@[9ccd6ecd74...](https://github.com/mengzhisuoliu/terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Sunday 2022-07-03 01:50:10 by Mike Griese

Manually copy trailing attributes on a resize (#12637)

## THE WHITE WHALE

This is a fairly naive fix for this bug. It's not terribly performant,
but neither is resize in the first place.

When the buffer gets resized, typically we only copy the text up to the
`MeasureRight` point, the last printable char in the row. Then we'd just
use the last char's attributes to fill the remainder of the row.

Instead, this PR changes how reflow behaves when it gets to the end of
the row. After we finish copying text, then manually walk through the
attributes at the end of the row, and copy them over. This ensures that
cells that just have a colored space in them get copied into the new
buffer as well, and we don't just blat the last character's attributes
into the rest of the row. We'll do a similar thing once we get to the
last printable char in the buffer, copying the remaining attributes.

This could DEFINITELY be more performant. I think this current
implementation walks the attrs _on every cell_, then appends the new
attrs to the new ATTR_ROW. That could be optimized by just using the
actual iterator. The copy after the last printable char bit is also
especially bad in this regard. That could likely be a blind copy - I
just wanted to get this into the world.

Finally, we now copy the final attributes to the correct buffer: the new
one.  We used to copy them to the _old_ buffer, which we were about to
destroy.

## Validation

I'll add more gifs in the morning, not enough time to finish spinning a
release Terminal build with this tonight.

Closes #32 🎉🎉🎉🎉🎉🎉🎉🎉🎉
Closes #12567

(cherry picked from commit 855e1360c0ff810decf862f1d90e15b5f49e7bbd)

---
## [travellings-link/travellings](https://github.com/travellings-link/travellings)@[bcde426301...](https://github.com/travellings-link/travellings/commit/bcde426301f7539ee9cddf9c071c87a470c75b15)
#### Sunday 2022-07-03 02:33:06 by 逊狼

🐺 R.I.P Zephyr

Dear Friends,

It is with sorrow and heartbreak that we share news about the world’s favorite wolf. Zephyr passed away today; he was 11 years old.

He was euthanized early this morning due to complications from myasthenia gravis, and was surrounded by those he held dear – his siblings, his human family, and the many wild animals with whom he shared his life.

Zephyr is a Greek word meaning “light or west wind” and much as the west wind continues to blow and howl, so too will Zephyr’s memory and passion for life.

He connected millions of people to wolves – charismatically highlighting the loving, inquisitive, and playful nature of his species – and served as the connector in his family as well. His close-knit relationship with Alawa, his litter mate, and steadfast devotion to Nikai, his younger brother, allowed the family of three to grow and adapt to an ever-changing world as a united pack.

Zephyr’s greatest talent, however, was his ability to make everyone he met feel special and valued. His piercing amber stare and propensity for melodic howls forged a bond with a global audience that will never be broken, and never should be. Much as the wind is sometimes quiet, sometimes forceful, but always present, so too is Zephyr’s love.

Thank you, Zephyr. We’ll never stop loving you.

Thank you so much for your support,

The Wolf Conservation Center Family

July 2, 2022

---
## [EtraIV/MerchantStation13](https://github.com/EtraIV/MerchantStation13)@[2a3b63c243...](https://github.com/EtraIV/MerchantStation13/commit/2a3b63c2434fec55f7dd1f232455d1594c21809f)
#### Sunday 2022-07-03 03:43:32 by BettonnCZ

Adds a new sprite for the stacker (#196)

fuck you

---
## [magnus-ISU/clientside-mods](https://github.com/magnus-ISU/clientside-mods)@[58b639c582...](https://github.com/magnus-ISU/clientside-mods/commit/58b639c5821f03d1a1dde3b0934d85f4af8a10b5)
#### Sunday 2022-07-03 04:41:09 by magnus

FIX STUPID IDIOTS ON WINDOWS LEAVING THEIR STUPID SHIT LYING AROUND AND MAKING FILES NOT MACHINE-READABLE. GNU my beloved you don't need to learn how to process these files its them not you

---
## [Ayushsunny/package-maintenance](https://github.com/Ayushsunny/package-maintenance)@[a3b5faa235...](https://github.com/Ayushsunny/package-maintenance/commit/a3b5faa235b246e875ada7381008c758a89490e1)
#### Sunday 2022-07-03 06:32:57 by Ayush Anand

Add @Ayushsunny as a member

Hello,
I'm Ayush Anand, I'm wanting to be a member so I can work with all of the interesting stuff to gain more experience. I'm available to work on any part of this org like documentation, community engagement, and package building. I'd also like to help give any input in any areas that I have experience in according to my GitHub profile.
Thank you all for your amazing work!

---
## [oleg-dubinskiy/reactos](https://github.com/oleg-dubinskiy/reactos)@[4471ee4dfa...](https://github.com/oleg-dubinskiy/reactos/commit/4471ee4dfaddb2440601fd61c01542b586b7c2d0)
#### Sunday 2022-07-03 08:39:44 by George Bișoc

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
## [fiqri19102002/android_kernel_xiaomi_mojito](https://github.com/fiqri19102002/android_kernel_xiaomi_mojito)@[313163f0eb...](https://github.com/fiqri19102002/android_kernel_xiaomi_mojito/commit/313163f0eb4b4685f21915c5027ee54272632742)
#### Sunday 2022-07-03 09:14:17 by Peter Zijlstra

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
Signed-off-by: Fiqri Ardyansyah <fiqri15072019@gmail.com>

---
## [mamh-mixed/microsoft-terminal](https://github.com/mamh-mixed/microsoft-terminal)@[8962f88f90...](https://github.com/mamh-mixed/microsoft-terminal/commit/8962f88f907d86fd8684b66f7f3e32a2709e3237)
#### Sunday 2022-07-03 09:17:37 by Dustin L. Howett

Disable the VT color quirk for pwsh and modern inbox powershell (#13352)

In #6810, we introduced a "quirk" for all known versions of PowerShell
that suppressed their requests for black background/gray foreground.
This was done to avoid an [issue in PSReadline] where it would paint
black bars all over the screen if the default background color wasn't
the same as the ANSI black color.

Years have passed since that quirk was introduced. The underlying bug
was fixed, and the fix was released broadly long ago. It's time for us
to remove the quirk... almost.

Terminal still runs on versions of Windows that ship a broken version of
PSReadline. We must maintain the quirk there -- the user can't do
anything about it, and we would make their experience worse if we
removed the quirk entirely.

PowerShell 7.0 also ships a broken version of PSReadline. It is still in
support for another 6 months, but updates have been available for some
time. We can encourage users to update.

Therefore, we only need the quirk for Windows PowerShell, and then only
for specific versions of Windows.

_Inside Windows_, we don't even need that: we're guaranteed to be built
alongside a fixed version of PowerShell!

Closes #6807

[issue in PSReadline]: https://github.com/PowerShell/PSReadLine/issues/830#issuecomment-650508857

---
## [sunofang/Foundation-19](https://github.com/sunofang/Foundation-19)@[a54b8e5040...](https://github.com/sunofang/Foundation-19/commit/a54b8e5040aab5f12f0cd7d21a46c0603b714e73)
#### Sunday 2022-07-03 09:21:20 by Bierkraan

Eta-10 sprite fix, some smaller stuff too (#144)

* balance?

* add reactor startup manual, fix sprites for lockers of all kinds

* MTF See No Evil (not being used for now), no more alien MTF

* map fix, janitor uniform

* Eta-10 helmet works!

* fixed

* SM Crystal hotfix

* Remove supermatter, for real

* No more blood sucking artifact, sprite fix for Eta-10

---
## [KiChesney/ATM-7_Minecolonies](https://github.com/KiChesney/ATM-7_Minecolonies)@[64020d8dd0...](https://github.com/KiChesney/ATM-7_Minecolonies/commit/64020d8dd093e874118b1e1426184392e7957331)
#### Sunday 2022-07-03 12:04:00 by Satisfactual

Minecolonies quest chapter

Some background about this chapter:
The design goal of this quest chapter was to tutorialize the basic progression of Minecolonies by providing useful advice or information from the wiki and my own experiences with the mod, while providing rewards which reduce the resource grind the mod is known for. The process of starting a colony is by itself very easy and straightforward - you construct a supply ship or supply camp, place it, then place your town hall schematic and your first set of colonists spawn in. However, starting a *functional* colony, and getting it to the point of self-sufficiency, is a *much* more involved process and I believe is ultimately the reason many players drop the mod before they start seeing a return on their time and resource investment. Starting a colony and spawning colonists is extremely easy, but the first step, constructing a builder's hut, requires a large amount of resources and understanding the way the request system works. Depending on the supply camp style selected and the builder's hut style selected, players can often deconstruct the majority of the camp to obtain most of the blocks the builder needs. A first time player may not know this, and even if they do, might take an hour or more to babysit the builder through the proces. By the time the builder's hut is complete, the colonists will likely be complaining about food, shelter, and safety. If the player decides to gather the resources themselves for their next few construction projects, typically housing (usually a tavern), a food source, and a gatherer such as a miner or forester, they're likely to return to dead or unhappy colonists, hours of micromanaging the builder, and low level gatherers who need a constant supply of tools and other supplies in order to break only a few blocks per minute. This problem is compounded when the player tries to construct a mine or forester first to help with the cost of construction - another hour of babysitting the builder only to have the new worker produce far less material than is needed for the next construction project. When players consider the amount of time and resources they've invested to get to this point compared to the lack of benefit they personally gain from the colony, they're likely to give up and focus on another mod with a more immediate return like blood magic or the industrial series.

With these experiences in mind, the quests are written and ordered to guide players through the mod in a similar manner to the Minecolonies "Getting Started" guide, with some other tips they would otherwise need to look up on the wiki or learn through experience. Getting housing, food, and basic gathering are prioritized over diving directly into item production, military, or research. The rewards provided are intended to minimize but not eliminate the early grind for wood and stone, as well as providing "just enough" of other items like leather and wool. Playtesting by myself and on a server has indicated that these are useful early on (though the quantities require tweaking and the item-type rewards could use another pass), but these rewards become progressively less useful as the colony develops. While it would require additional research (into structurize blueprints and block counts) and development (reward tables and itemsets), I think it would ultimately be much more rewarding to offer sets of blocks as rewards with players selecting from the structurize theme types - fortress giving dark oak and stone brick, dwarven giving more smooth stone, etc.

Quests are typically divided into two parts - the construction of a hut block/building item, which offers a token item or random building block reward, and the completion of the building, which usually offers a player choice of the same building blocks or sometimes other items. Building completion is tracked by advancements - not all buildings have an associated advancement, but it should be possible to either track the same triggers or create new advancements. The trigger used for the building completion advancements in minecolonies is minecolonies:complete_build_request, which contains conditions for hut_name (name of the building) and level (upgrade level of the building). A new building will have a level of 1, but upgrading a building to a higher level also fires the same complete_build_request event, with the new level passed in. This is how the advancements (and quests) for upgrading the builder's hut, town hall, etc. work.

In terms of what would be useful for additional quests, building completion quests for those which don't have them would be useful. At the moment, animal herder huts only have a "make the item" quest. I opted not to reward the corresponding animals for these quests, to discourage players from simply crafting all the building items and never building them in order to reap the rewards. A breeding pair of the associated animal for each hut would be a fine reward on building completion.

As far as gating, none of the mod content is actually gated beyond buildings which require university research or another building to be upgraded to a certain point. The quests are invisible until discovery purely to discourage players from doing something like building a guard tower before housing, or neglecting to upgrade their buildings. The quest to upgrade the builder's hut becomes visible as soon as they get their first additional colonist, either a child or hired visitor from the tavern, and the quest text explains that they need to upgrade the builder's hut in order to upgrade other buildings. The guard tower quest is behind the 5 population quest, and the university quest is behind the 10 population quest. Players can obviously build these things before the quest is visible, though this does leave the problem of having to craft another "building item" to progress beyond any quests unlocked after the buildings in question are already constructed. While the advancement parts should complete without issue if the advancement is done before the quest becomes visible, the item-linked quests will not.

Currently, military achivement and population count quests are devoid of text. Their rewards were also chosen without much care.
It would be nice to see either one of the later military or population quests reward some contribution towards the creation of the ATM star or some creative item.

---
## [mainman879/Magic-Token](https://github.com/mainman879/Magic-Token)@[589b2788bf...](https://github.com/mainman879/Magic-Token/commit/589b2788bf5a8719a7584c7832f1c9b8a3129504)
#### Sunday 2022-07-03 12:27:06 by ebbit1q

remove unused token relations (#160)

* search for unused relations

reverse-related is assumed to only be used for external references to
the xml
related tags should be used for internal links to make this easier and
to avoid certain errors eg the Phyrexian Insect here

the following lazy bash has been used to find these:
\#!/bin/bash
relationrx='<reverse-related([^>]*)>([^<]*)</reverse-related>'
while read -r line; do
  if [[ $line =~ $relationrx ]]; then
    name="${BASH_REMATCH[2]}"
    #args="${BASH_REMATCH[1]}"
    if ! grep -F "$name" "$HOME/.local/share/Cockatrice/Cockatrice/cards.xml" -q; then
      echo "$name"
    fi
  fi
done <tokens.xml

the following relations are affected:
Domri, Chaos Bringer (Emblem) is related internally, moved
Ajani, Adversary of Tyrants (Emblem) is related internally, moved
Chief Jim Hopper became Sophina, Spearsage Deserter, moved
Max, the Daredevil became Elmar, Ulvenwald Informant, moved
Will the Wise became Wernog, Rider's Chaplain, moved
"Big Boy Forest Crusher" was a spoiler placeholder, deleted
"Destoroyah, Perfect Lifeform" is called Everquill Phoenix, deleted
"What's Kraken" was a spoiler placeholder, deleted
Liliana, the Last Hope (Emblem) is related internally, moved
Insect Token has been renamed to Phyrexian Insect token before and had its Poison Counter relationship lost, moved
`Snake Token ` is related internally, moved
Obsessed Astronomer was probably a spoiler placeholder?, deleted
"Obosh, With The Leggies" was a spoiler placeholder, deleted
"Gigan, Cyberclaw Terror" is called Gyruda, Doom of Depths, deleted

* sort all reverse-related tags

less lazy script but still bash:
\#!/bin/bash
tag="reverse-related"
relationrx="<$tag([^>]*)>([^<]*)</$tag>"
numberrx='[0-9]+'
declare -A list # associative array
while IFS= read -r line; do
  if [[ $line =~ $relationrx ]]; then
    yes=1
    name="${BASH_REMATCH[2]}"
    args="${BASH_REMATCH[1]}"
    if [[ $args =~ $numberrx ]]; then
      args="$(printf "%03d" "${BASH_REMATCH[0]}")$args"
    fi
    list[ "$name$args"]="$line"
    keys+="
$name$args"
  elif [[ $yes ]]; then
    # LC_ALL=C determines the sort behavior!
    <<<"${keys:1}" LC_ALL=C sort --ignore-case | while read -r key; do
      echo "${list[ $key]}"
    done
    yes=""
    list=()
    keys=""
    echo "$line"
  else
    echo "$line"
  fi
done <tokens.xml | sponge tokens.xml

* remove duplicate entry

this also needed a script, because why not:
\#!/bin/bash
while IFS= read -r line; do
  if [[ $line == "$last" ]]; then
    echo "$line"
  fi
  last="$line"
done <tokens.xml

* update version

---
## [crusher083/anvio.org](https://github.com/crusher083/anvio.org)@[1d2a69daa3...](https://github.com/crusher083/anvio.org/commit/1d2a69daa391be2ff61b9cca15a527a1a6af5685)
#### Sunday 2022-07-03 13:31:38 by A. Murat Eren

going back to 3.7 due to STUPID SH*T FC*K REASONS

There is no conda package for Bowtie2 compatible with Python 3.10,
so basically we have to go all the way back to Python 3.7. This is
ridiculous and frustrating. The year made it all the way to 2022
but we are stuck in middle ages.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[ef8e1cbfb0...](https://github.com/mrakgr/The-Spiral-Language/commit/ef8e1cbfb03be039d9e9fa425c459d838b416329)
#### Sunday 2022-07-03 14:56:14 by Marko Grdinić

"7am. This is a pain. I am going to switch to working on these chores late in the day after today. My body really wants to stay in bed for longer.

But I went through all this hassle so I can get up properly today, so let me do the chores early in the morning one last time.

9:35am. I am back. Man, I am dead. I think I'll take a nap just for a bit and then browse /a/. It seems P&S S2 was announced. I never thought I'd see that happen.

9:40am. Let me take a nap just for a bit.

10:20am. I've cooled down a bit. Now let me watch some Bastard. Tenken is out as well. I am going to skip doing anything in the morning session. I'll work on the hand later

10:55am. Anime. I want to watch Bastard and I've yet to finish BRS, Virgin Road or Magireco. Right now I've just restored my state of mind a bit.

12:35pm. Done with the break. I'll leave the BRS ep for later. Right now, let me do some sculpting.

I had a proper night's rest, so I am in a better shape than yesterday.

Two days ago, I messed up with the mid of the day nap, and it wrecked my schedule. I went to bed on time, but I could not fall asleep until too late into the night. Yesterday I was too anxious to properly enjoy myself, I should have just left it all out of mind and played games or watched anime.

But even that is hard when you are dead tired. Even something as enjoyment of hobbies requires a rested mind, otherwise it feels like a burden.

Yesterday's night was good, I want to bed before 10pm and caught some zzzs right away so I am in good mental condition right now. Let me complete the hand and I will start sculpting those skelly bones.

Yesterday I was actually annoyed by not being able to grasp the proportions of the hand. I did not want to think about it, but now I do. Let me do this for a few hours maybe I will get somewhere.

1:35pm. Ok, I think I did a good enough job on the hands. Time for a break. Before I move on to the next phase I want to work more on the feet. I feel they are ridiculously large.

1:55pm. Let me resume. I should busy myself with the feet for a bit.

Focus. This is not that hard. I just need to factor into a series of individual steps.

2pm. Yeah, they were too large. I wasn't sure based on what, but the angle between the knee and the tip of the foot should be something like 67 degrees, whereas previously it was 60.

I suppose this is good enough for now.

2:15pm. Worked a bit on the proportions of the ribcage block. The sternum in partciular was too low. My focus yesterday really was not too good.

2:20pm. I am satisfied with this. This shoudl be good enough for block out 2.

Oh crap, Blender crashed as soon as I selected to display as wire. I hope I did not lose too much work.

...I did not. I must have saved just moments before, good for me.

2:25pm. Good. Now it is time for the sculpt itself. Whatever proportional errors are in the block out do not matter. Since the skeleton model is greatly modular, I should be able to easily adjust it. The only thing I haven't blocked out in the earlier phase is the skull. I'll leave that for last. Let me do a few of the bones in the foot.

Previously I've only been going through the anatomy for sculptors book roughly, but now I'll get familiar with each individual bone.

2:35pm. Hmmm, maybe I am doing the block out wrong. Instead out of cubes, it might be have been better to do it in Moi, and see how close I can get to the truth that way.

But nevermind that. This way of doing it has some benefits as well.

Focus me, stop surfing /ic/.

2:45pm. Damn it, I messed up the block out of the foot. The bone proprtions are wrong. What was I even thinking yesterday?

This kind of job I really don't feel like doing anymore. The sane response to this would be to just get a skeleton model off from somewhere. But inevitably it would cost something like 40$ at least.

Let me stop a little here.

My problem is that I just want the completed scene, but have no interest in actually modeling the entire skeleton for weeks just to get it.

2:50pm. I know I said I would complete the scene, but it not like my 7 twitter followers are paying me to do it. Let me think about applying more.

2:55pm. Yeah, it is time that I start applying here. Forget the damn skeleton. Now if only I could find at ad from before.

https://news.ycombinator.com/item?id=31843932

It was this. It was posted 10 days ago.

https://jobs.lever.co/generallyintelligent/9411e2ec-502a-403f-a39a-0d44c676b6af
Generally Intelligent Remote Job Ad

Oh wow, this is really good.

> Our research is focused primarily on self-supervised and generative video and audio models.
> All submissions are reviewed by a person, so we encourage you to include notes on why you're interested in working with us.

3pm. Ok, for now, let me go to LinkedIn and SO, and get rid of my resume. I think I might have it in another place, but nevermind that.

https://goodbyestackoverflowjobs.com/

Hmmm, SO Jobs closed?

https://meta.stackoverflow.com/questions/415293/sunsetting-jobs-developer-story

3:10pm. Art is a lot of work. I am just not motivated to pursue it unless I'd get a tangible reward. Look what I've done for the past few hours, just fiddle around. It gets tiring quick.

Let me switch gears. I'll think about my resume for a bit. I won't jump on it and apply today though.

Since I have another 2-3 hours of stacking wood after 6pm, I'll take it easy until then.

What I will do tomorrow is get some rust off my programming gears. Since it might take me a few weeks to find a job or even more, that should be enough to finish the ref counted C backend for Spiral. If I still do not have a job by then, I'll resume sculpting the skelly and studying music.

Let me check out the resume.

3:30pm. In the resume I'll push my ML skills from 3/5 to 4/5. Since I am applying to an ML company, no need to undersell myself.

///

* GVGAI F# port
- Link: https://github.com/mrakgr/GVGAI-Fsharp
- Port of the Python library of the same name.
- A DSL for making simple games of the kind suitable for training RL agents.
- Tech used: F#, FParsec, XNA.

///

I am going going to get rid of the game skill, as well as this project. Instead what I will do is put the recent CAST project on resume. I'll fork the main repo, upload my own version to it, and put it on the resume. This is something the ML places would like. I'll also put the Twitter handle, so if the ML interviewer checks it out, she can look at the pretty pictures.

Also the math skill, I'll get rid of that. Now let me fork CAST.

https://github.com/mrakgr/CAST_pytorch

Now I just have to clone it, overwrite it with my own and push it. Actually, I already have it cloned so I just need to edit the readme so it points to the authors version.

4:10pm. https://stackoverflow.com/questions/1274057/how-can-i-make-git-forget-about-a-file-that-was-tracked-but-is-now-in-gitign

This should be fine. I've made sure not to accidentally push the models, as well as gotten rid of the .pyc files.

Let me commit, then I'll figure out how to change the remote target to my own repo.

4:15pm. That was easy enough.

https://github.com/mrakgr/CAST_pytorch

Everything is right here now. Let me tweet out the link.

4:25pm. Done.

4:35pm.

///

* Optimized CAST implementation
- Link: https://github.com/mrakgr/CAST_pytorch
- While I was studying 3d art, I did some research on image style transfer to see if anything good is in this area and CAST caught my eye.
- I am not the original author of CAST, but I modified the implementation so it runs on the CPU and consumes 7x less peak memory allowing it to be run on much larger images.
- Some examples on it being applied to 3d renders can be found on my Twitter: https://twitter.com/Ghostlike/status/1536019692414017538
- Tech used: Python, PyTorch

///

I'll put this in my resume.

Now, what I need to do is put some company specific notes since the job description said they would consider it. I like doing that kind of thing anway.

I will also do the thing with small white fonts at the end, just in case they are sending the resumes through the bots. Even if the interviewer detects it, it won't count against me so there is no reason at all not to do this. In fact if it gets detected it might even be in my favor, since knowing how to trick the bots is a sign of intelligence.

Since I want to say more stuff that just leaving a single sentence saying 10 years of exp at some big company, the easiest way to get my hit rate up is to track down that joke resume, and paste some stuff from it.

I do not have access to real world resumes of seniors, so I can't paste crap from them. I can't actually see the resumes on other on LinkedIn. I think that to get that access I might need to pay some money, but I'll should be able to handle this challenge without that.

Tomorrow I'll look through my journal for that joke resume link. Nevermind that for now.

I'll also focus on writing some notes for the company.

Not right now. In a few hours I'll have another round of chores and do not want to mess with it at the moment.

4:45pm. Since the job search will take time, I'll iterate between working on the skelly and working the C backend. After not programming for so long, I want to do something other than art.

The C backend is something I really want to do as it will be necessary for AI chips. Ideally I should do it before I get my hands on them.

4:50pm. Let me close here. I think I'll watch more anime until it is time for lunch and then for a few hours do more winter prep chores. After today, I should have 2 rows left and will be able to finish 0.5 row per day. I should be done with it soon."

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[8a5e98a39a...](https://github.com/treckstar/yolo-octo-hipster/commit/8a5e98a39a645d382770ab51ad78f96c64eed397)
#### Sunday 2022-07-03 16:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Hurricos/realtek-poe](https://github.com/Hurricos/realtek-poe)@[d67ebfa829...](https://github.com/Hurricos/realtek-poe/commit/d67ebfa82985e9924e2e4d9f5c2d360516912422)
#### Sunday 2022-07-03 17:19:26 by Alexandru Gagniuc

realtek-poe: Fix memory leak in poe_reply_consume()

When thinking "embedded", it's a good idea to stay the fuck away from
malloc(). Falling out of scope is a free garbage collector. Port
config and state arrays followed this advice, but for some reason, the
command queue did not.

No worries, free() is used in poe_reply_consume(). No problemo! Crisis
averted! Did you spot the several failure modes which return before
the free() call. In these modes, a malloc()d command is taken off the
queue, and not free()d. The pointer falls out of scope and memory lost.
Quod Erat Demonstratum.

To fix this, free() the command before hitting any exit paths.

Signed-off-by: Alexandru Gagniuc <mr.nuke.me@gmail.com>

---
## [protesilaos/denote](https://github.com/protesilaos/denote)@[f35ef05cb4...](https://github.com/protesilaos/denote/commit/f35ef05cb451f265213c3aafc1e62c425b1ff043)
#### Sunday 2022-07-03 18:26:55 by Protesilaos Stavrou

REMOVE support for 'id:' hyperlink types

The original idea was to support the 'org-id' library on the premise
that it makes Denote a good Emacs citizen.  However, discussions on the
mailing list[0] and the GitHub mirror[1] have made it clear to me that
'org-id' is not consistent with Denote's emphasis on simplicity.

To support the way 'org-id' works, we will eventually have to develop
some caching mechanism, just how the org-roam package does it.  This is
because the variable 'org-id-extra-files' needs to be kept up-to-date
whenever an operation on a file is performed.  At scale, this sort of
monitoring requires specialised software.  Such a mechanism is outside
the scope of Denote---if you need a db, use org-roam which is already
great.

[0] <https://lists.sr.ht/~protesilaos/denote/%3C8735fk4y1w.fsf%40hallac.net%3E#%3C877d4un73c.fsf@protesilaos.com%3E>

[1] <https://github.com/protesilaos/denote/issues/29>

Quote of what I wrote on the GitHub mirror issue 29:

        [ggjp] This is what I was implying.  That we are, in fact,
        providing an option that is not viable long-term, but keeping
        the option for expert users who will be able to handle this.
        And we should warn about this clearly in the doc of that option.

    [protesilaos] What you write here @ggjp and what @shrysr explained
    tells me that those expert users will need to be real experts.  To
    put it concretely, I am an experienced Emacs user with no
    programming background, who has written several Emacs
    packages (including the modus-themes which are built into Emacs),
    but I have zero knowledge of using a db or of handling things with
    python and the like.  So if I opt in to 'denote-link-use-org-id' I
    will eventually run into problems that my non-existent skills will
    prevent me from solving.  At that point, I will just use org-roam
    which already handles this use-case in a competent way (and has a
    massive community to rely on in case I need further support).

    If each package needs to write its own optimisations and maintain
    its own cache, to me this shows that 'org-id' is not good enough for
    the time being: more work needs to be done in org.git to provide a
    universal solution.

    I wanted to support 'org-id' by default on the premise that Denote
    must be a good Emacs citizen which interoperates with the rest of
    the wider ecosystem.  But if 'org-id' leaves something to be
    desired, then that goal is not worth pursuing: we add complexity to
    our code, offer an option that we cannot genuinely/adequately
    support, and make usage of it contingent on reading the docs and
    having a high level of expertise.

    I think being a good Emacs citizen is a laudable principle.  In this
    case, the right thing to do is to recommend the use of org-roam
    instead of trying to accommodate 'org-id'.  As such, I have now
    changed my mind and think we should remove what we previously added.

    For some context here: the reason I never used org-roam is
    because (i) it is Org-specific whereas I write notes in different
    file types and (ii) I did not want to ever rely on a db or
    equivalent dependency.

    <https://github.com/protesilaos/denote/issues/29#issuecomment-1173036924>

---
## [fuck-boy-alam-vau-tera-papa/priya11](https://github.com/fuck-boy-alam-vau-tera-papa/priya11)@[1af49b553f...](https://github.com/fuck-boy-alam-vau-tera-papa/priya11/commit/1af49b553fb0cc5358d97dacad74c5e42d5423aa)
#### Sunday 2022-07-03 19:19:14 by Md. Alamgir Hosen

Merge pull request #1 from fuck-boy-alam-vau-tera-papa/fuck-boy-alam-vau-tera-papa-patch-1

Add files via upload

---
## [wisp-forest/ctft](https://github.com/wisp-forest/ctft)@[2a97b2c2cf...](https://github.com/wisp-forest/ctft/commit/2a97b2c2cf7ccbe3dc45b933d98defb6580d9446)
#### Sunday 2022-07-03 20:20:02 by chyzman

OMEGA REG
THE REGISTRY TO END ALL OTHER REGISTRIES
ITS SO FUCKING EFFICIENT LIKE HOLY SHIT THE CODE IS LIKE 1/10 THE SIZE IT USED TO BE

---
## [dicekillsyou161/qtile-scripts](https://github.com/dicekillsyou161/qtile-scripts)@[2c049e1a27...](https://github.com/dicekillsyou161/qtile-scripts/commit/2c049e1a271579938799af623f2d02344cf250ff)
#### Sunday 2022-07-03 20:30:22 by dicekillsyou161

Fuck, I dunno LMFAO, I guess a lot of VM theme shit copying into my main?

---
## [torvalds/linux](https://github.com/torvalds/linux)@[4a557a5d1a...](https://github.com/torvalds/linux/commit/4a557a5d1a6145ea586dc9b17a9b4e5190c9c017)
#### Sunday 2022-07-03 21:47:02 by Linus Torvalds

sparse: introduce conditional lock acquire function attribute

The kernel tends to try to avoid conditional locking semantics because
it makes it harder to think about and statically check locking rules,
but we do have a few fundamental locking primitives that take locks
conditionally - most obviously the 'trylock' functions.

That has always been a problem for 'sparse' checking for locking
imbalance, and we've had a special '__cond_lock()' macro that we've used
to let sparse know how the locking works:

    # define __cond_lock(x,c)        ((c) ? ({ __acquire(x); 1; }) : 0)

so that you can then use this to tell sparse that (for example) the
spinlock trylock macro ends up acquiring the lock when it succeeds, but
not when it fails:

    #define raw_spin_trylock(lock)  __cond_lock(lock, _raw_spin_trylock(lock))

and then sparse can follow along the locking rules when you have code like

        if (!spin_trylock(&dentry->d_lock))
                return LRU_SKIP;
	.. sparse sees that the lock is held here..
        spin_unlock(&dentry->d_lock);

and sparse ends up happy about the lock contexts.

However, this '__cond_lock()' use does result in very ugly header files,
and requires you to basically wrap the real function with that macro
that uses '__cond_lock'.  Which has made PeterZ NAK things that try to
fix sparse warnings over the years [1].

To solve this, there is now a very experimental patch to sparse that
basically does the exact same thing as '__cond_lock()' did, but using a
function attribute instead.  That seems to make PeterZ happy [2].

Note that this does not replace existing use of '__cond_lock()', but
only exposes the new proposed attribute and uses it for the previously
unannotated 'refcount_dec_and_lock()' family of functions.

For existing sparse installations, this will make no difference (a
negative output context was ignored), but if you have the experimental
sparse patch it will make sparse now understand code that uses those
functions, the same way '__cond_lock()' makes sparse understand the very
similar 'atomic_dec_and_lock()' uses that have the old '__cond_lock()'
annotations.

Note that in some cases this will silence existing context imbalance
warnings.  But in other cases it may end up exposing new sparse warnings
for code that sparse just didn't see the locking for at all before.

This is a trial, in other words.  I'd expect that if it ends up being
successful, and new sparse releases end up having this new attribute,
we'll migrate the old-style '__cond_lock()' users to use the new-style
'__cond_acquires' function attribute.

The actual experimental sparse patch was posted in [3].

Link: https://lore.kernel.org/all/20130930134434.GC12926@twins.programming.kicks-ass.net/ [1]
Link: https://lore.kernel.org/all/Yr60tWxN4P568x3W@worktop.programming.kicks-ass.net/ [2]
Link: https://lore.kernel.org/all/CAHk-=wjZfO9hGqJ2_hGQG3U_XzSh9_XaXze=HgPdvJbgrvASfA@mail.gmail.com/ [3]
Acked-by: Peter Zijlstra <peterz@infradead.org>
Cc: Alexander Aring <aahringo@redhat.com>
Cc: Luc Van Oostenryck <luc.vanoostenryck@gmail.com>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER)@[0abc0560dd...](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/commit/0abc0560dd5ff7036ef240567063862bd78e5694)
#### Sunday 2022-07-03 22:23:10 by WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER

Date: 	Sun, 3 Jul 2022 17:14:25 -0400 --- EST 1753 

\

-------- Forwarded Message --------
Subject: 	Here go reference these numbers
Date: 	Sun, 3 Jul 2022 17:14:25 -0400
From: 	BO DINCER <bondstrt007@gmail.com>
To: 	Dean Marcus Foskett <dmf2189@columbia.edu>, Samuel Meir Freilich <smf2195@columbia.edu>
CC: 	endowmentadmin@columbia.edu, Lee Bollinger <bollinger@columbia.edu>, Sara E. Ede <see2119@columbia.edu>, Steve O’Connell <sgo2107@columbia.edu>, KATHY HOCHUL <governor.hochul@exec.ny.gov>, Amber Griffiths <ag2943@columbia.edu>, Delva, Marlyn <mmt22@cumc.columbia.edu>, Marlyn Delva <mmt22@columbia.edu>, Paul Regan <LEGAL@mskyline.com>, William McKenzie <wmckenzi@nycourts.gov>, LEGALASST@mskyline.com, kevin.kilkenny@chase.com, malia.d.chatman@chase.com, Janna.Underwood@STATEFARM.COM <Janna.Underwood@statefarm.com>, Humphries, Ashley V. <ashley.humphries@wilsonelser.com>, Laskowitz, Shari <slaskowitz@ingramllp.com>, MSKYLINE <anne@thehighlandpartners.com>, Amber Griffiths <ag2943@adcu.columbia.edu>, Amy Hanrahan <amy.hanrahan@wilsonelser.com>, FTC ANTITRUST <antitrust@ftc.gov>, LZUCKER@mskyline.com, ADMINISTRATION@mskyline.com, Dean's Discipline - SCCS <conduct-admin@columbia.edu>, MANHATTAN SKYLINE, LLC. <ADMINISTRATOR@mskyline.com>


See what happens is, when your phone turns on and sends something, it goes to a tower.

So when your not in times square, its easier to figure out which towers are available, and log the numbers thatvused them .

 For example.

So put these in a spreadsheet and send them to the FBI.
-- Use codeword Ferreira, metropolitan tower loan 50074 and include the emails in the CC. 

Copy this in there so::
I don't play man, moustache or not...
-- stay the fuck away from me when im trying to knock this fortress of a zucker and their accessories and stop acting like a bitch.  also, keep your fucking mouth shut before i break the front portion of your face into chicken bones and stay the fuck out of my proximity.... all of you.
   
Thank you for your assistance gentleman.
--  that beer, was a good choice.. always welcome.

---
## [cincospenguinos/MinecraftStartup](https://github.com/cincospenguinos/MinecraftStartup)@[0b4f5744a8...](https://github.com/cincospenguinos/MinecraftStartup/commit/0b4f5744a8c5f2d32d072c47fe6ef5d63b152be4)
#### Sunday 2022-07-03 22:25:56 by Andre LaFleur

I dun goofd

* I need an extra service that duplicates the work that the spigot plugin does
  to get this configuration up and running the way I want. It is going to be
  a pain in the ass to do, but at least this way things will be isolated and
  functional and (hopefully) easy to deploy
* I do not love having things in/out of docker, but I want to be able to just
  press a button and have everything be deployed. That, and proof that I can
  put together an application in docker and get it orchestrated as desired

---
## [ss220-space/tgstation](https://github.com/ss220-space/tgstation)@[707fbfac7e...](https://github.com/ss220-space/tgstation/commit/707fbfac7e11837865d70587011aa8197b1d0c35)
#### Sunday 2022-07-03 22:32:23 by san7890

[MDB Ignore] Shifts all (sane) varedited signs to directionals  (#68004)

* [MDB Ignore] Shifts all (sane) varedited signs to directionals

Hey there,

So we have these cool new sign directionals now, but we still have all of the old pixel-shifted pre-fabrications lying around. So, I added an UpdatePaths (as well as Updated the Paths) to be a bit better at using directionals, because directionals are pretty neato.

This should update every single var_edit that used the proper 32 pixelshift (some of them used 28, and I'm unable to account for that automatically with current tooling) into a proper subtype. Mappers tend to learn by looking at well established maps, so it's always important to ensure that the well-established maps use the most recent tooling (i.e.: bring them up to the surface) and avoid needless excess lines in maps.

* The Commit With All The Maps

OH GOD OH FUCK

* Renames the UpdatePaths

---
## [Koshenko/mojave-sun-13](https://github.com/Koshenko/mojave-sun-13)@[2996f41136...](https://github.com/Koshenko/mojave-sun-13/commit/2996f41136fcd4dee419b4138e45ae65df9529f6)
#### Sunday 2022-07-03 23:23:19 by EdwardNashton

Update Time: Machinery to People (#2096)

* Update Time: Machinery to People

Added a recorders and server racks all over the city.

Slightly changed a "Cheap Motel" near Police Dept.

Slightly changed Police Dept.

Slightly updated Chemical Factory and Weather Station.

* Update time: small fixes

Changed a servers on Power Plant.

* Update Time: that god damn room in PD

I hope we're done with it.

* Update Time: small fix

Removed a potential feature with "shutter trap" in PD.

* Update Time: fixes and updating Water Treatment Station

You made me do this, Original.

* Update Time: one day the south dir comes, we'll place our stuff and go

Sometimes you get too picky

Co-authored-by: Edward Nashton <eddienigma48@gmail.com>

---

