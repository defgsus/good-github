## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-06-26](docs/good-messages/2022/2022-06-26.md)


1,540,819 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,540,819 were push events containing 2,065,223 commit messages that amount to 116,037,563 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 27 messages:


## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[9428d97a4f...](https://github.com/timothymtorres/tgstation/commit/9428d97a4fadf8a486b0c6fbe2ee345a2780e687)
#### Sunday 2022-06-26 01:14:49 by Imaginos16

[MDB IGNORE] The Tilening V2 - Damaged Tile Overlays Edition (#67761)


About The Pull Request

Hello once more! As we near summer, I continued to reminisce on several PRs done throughout last year! One of them was the controversial, but rather positive Tilening V1, as done by me and Twaticus a while back (#58932), and felt I could've done a better job with how it was presented.

And thus, thanks to @Fikou encouraging me with a very interesting find of a previous tile resprite attempt, I've successfully done it!

Ladies and Gentlemen, I present to you all, Tilening Version Two!
image

Now this isn't your run of the mill tile resprite. While I did improve the appearance of several tiles I haven't touched last time (including the showroom/freezer tiles now), I decided to do something special that most mappers shall appreciate!

Don't you hate it when of all damaged states, there's only ones for grey tiles when we have white, black, terracotta and a bunch of other materials? Don't you wish they were overlays instead?

Well golly gee do I have good news for you!
image
image

After painstakingly spending at least several hours trying to learn enough code to pull it off, I have successfully made it so most tiles display transparent versions of damage overlays over them! This means mappers can express their creativity that much better! And thanks to how the code is written, its super easy to snowflake certain tile types to make them use unique damaged states (looking at you wooden tiles), so fret not in that aspect.

Credits to:
@WJohn For actually making those damaged overlays! Wouldn't've done the PR if it wasn't for you.
@dragomagol, @RigglePrime and @LemonInTheDark for helping me out in a VC at 10 PM to 12 AM troubleshooting the code to make this improvement work!
Why It's Good For The Game

The shading is done better as compared to last time, making them feel more cubical and less like a pancake when seen from above! This PR also makes it so that we never ever have to touch damaged tiles ever again potentially, saving up some RSC regarding icons.

However, due to how damaged tiles are currently mapped in, rather than overlayed as I envision in the future, it'll require a PR by San to be merged later that should make it safe to remove these icons.
Changelog

cl PositiveEntropy, WJohnston, Dragomagol, LemonInTheDark, Riggle
imageadd: Resprites most variety of tiles into a better shaded version!
code: Damaged floors are now damaged overlays, meaning that most tiles should properly display a damaged state!
/cl

---
## [TheBoondock/tgstation](https://github.com/TheBoondock/tgstation)@[763a10d1cc...](https://github.com/TheBoondock/tgstation/commit/763a10d1cc44c91720101d422d8709ad1aa0644d)
#### Sunday 2022-06-26 01:48:45 by distributivgesetz

Resonance cascade polishening, bugfixes and better logging (#67488)

This PR rewrites almost all messages related to cascade events. Some messages felt kinda clunky to read or could have been written better. Overall, the new messages add to the experience as a cascade being a terrifying event in a way that I felt the old ones missed, and they make the event feel overall a lot sharper.

While looking at the resonance cascade code, I noticed that there a lot of stuff about cascades in the air which was not touched on. So, as I do, this PR evolved into a polish and roundup PR for cascades. There was a lot of stuff still hanging out relating to the event, and although the big backend of it sits, there was still a bit left to be completed. Therefore this PR deserves more the title of the "Resonance cascade POLISHENING" instead of the "REFLAVAHRING". But yeah, you ever go on a massive tangent before?

---
## [ynot01/Yogstation](https://github.com/ynot01/Yogstation)@[a297304eff...](https://github.com/ynot01/Yogstation/commit/a297304effcf85d7ba9828021df218ffea8f51b3)
#### Sunday 2022-06-26 02:57:48 by LazennG

makes some of the recent megafauna drops less shit (#14455)

* this is everything i think idk it's 330am

* polishes some things for now therell probably be more later

* Update miscellaneous.dm

* fuck it critical heal

* you're able to the body entirely

---
## [Reinazhard/android_kernel_xiaomi_whyred](https://github.com/Reinazhard/android_kernel_xiaomi_whyred)@[f7e04454b7...](https://github.com/Reinazhard/android_kernel_xiaomi_whyred/commit/f7e04454b739fad79227f382a9e89031edfaeea8)
#### Sunday 2022-06-26 04:49:32 by Peter Zijlstra

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
Signed-off-by: Adam W. Willis <return.of.octobot@gmail.com>

---
## [GamingMarine/gmid](https://github.com/GamingMarine/gmid)@[617c5ac024...](https://github.com/GamingMarine/gmid/commit/617c5ac0244a3d50a0f3ab30c79f088fbc17c3e8)
#### Sunday 2022-06-26 05:27:39 by GamingMarine

I just want to get this thing done already

-The GMBot now shoots its own rocket projectile, which is slower, less damaging, and overall makes them more forgiving
-Renamed all CVARs to prevent possible conflictions with other mods
-Removed scripted marines, as very few maps made use of them to make their inclusion worthwhile
-Gave the Changeling's projectiles a much less hideous light
-Nearly all the remaining Half-Life 1 sounds have been improved in quality, courtesy of Senn (aka @senn_twt)
-Added a better version of the blood drop sound effect, taken from Half-Life 2
-Fixed some offsets on the Shotgun and V-Gun Evil Marine sprites
-Added a new Tip of the Day

---
## [shruuub/bunkercoin](https://github.com/shruuub/bunkercoin)@[6ab5b59916...](https://github.com/shruuub/bunkercoin/commit/6ab5b59916453b0e4e5988c54b9294e6442a8504)
#### Sunday 2022-06-26 07:10:04 by IdotMaster1

Revert "Here we go! This is it! (Soon)"

This reverts commit b070522fa9d8031686f67b69c0b3993571c1841c.

OH MY GOD IM A FUCKING MORON

---
## [AndrewBeshay/terminal](https://github.com/AndrewBeshay/terminal)@[9ccd6ecd74...](https://github.com/AndrewBeshay/terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Sunday 2022-06-26 07:27:15 by Mike Griese

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
## [AndrewBeshay/terminal](https://github.com/AndrewBeshay/terminal)@[8962f88f90...](https://github.com/AndrewBeshay/terminal/commit/8962f88f907d86fd8684b66f7f3e32a2709e3237)
#### Sunday 2022-06-26 07:27:15 by Dustin L. Howett

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
## [ddnet/ddnet-maps](https://github.com/ddnet/ddnet-maps)@[93d842f876...](https://github.com/ddnet/ddnet-maps/commit/93d842f8767f111ab022afe615e0d4a295d69461)
#### Sunday 2022-06-26 08:56:30 by DDNet Maps

M A Strange Dream, M Cemetery, M Generic Fly, M Highlife, M Intercepter, M Just Triple Fly, M Naufrage, M Nightly Tandem, M Stronghold 2, M Stronghold, M Yun Gu 2, M Yun Gu 3, M brainduck, M brainduck2, M nullptr, M TheVoiD, M Huanghu, M Liang, M Nebula, M TakeUrLuggage, A Tied up, M Vice City, M Back in Time 3, M Shockwave, M Aftermath, M Afternoon, A Baerchen, M Canyang, M Clarity, M Coffee I, M Coffee II, A DaoYu Night, M Just HookThrough, M PreciousDream, M SomewhereDistant, M Sunny Land, M Yeyou 1, M Yeyou 2, M Yeyou 3, M Yun Gu, M Absurd 3, M Beyond Light, M Light Grey, M 1Hook, M Aufnahmetest_AE, M Euthanasia, M Run_Aim, M climate-crisis, M frustrainleave, M hotrun, M nameless_run, M run_2Rockets, M run_2rocketstwo, M run_4lollipop, M run_4mystery, M run_4popi, M run_4popo, M run_4tzoy, M run_4xerhul, M run_4xerhul2, M run_FreezyFly, M run_Jellyfish_Fields, M run_alboni, M run_alkohol, M run_antibuguse, M run_birming, M run_birthday, M run_black_white, M run_blood_thirst, M run_blue, M run_crystal, M run_dfc, M run_escape_the_darkness, M run_experience_of_incredibleness, M run_firestorm, M run_for_ghost, M run_from_ice_to_grass, M run_frosty, M run_g6, M run_galaxy, M run_glowing_ice, M run_golden_toilet, M run_granit_stone, M run_grass_hell, M run_groove, M run_hard_hell, M run_hard_hundred, M run_harder_than_hard, M run_heaven_and_hell, M run_hot_or_not, M run_ice_castle, M run_inset_into_the_heavy_jungle, M run_inset_into_the_light, M run_keksi, M run_longWAR, M run_miniatur, M run_nightmare, M run_not_short, M run_out_jungle, M run_painted, M run_pencil, M run_pink.lila, M run_radioactive, M run_redbull, M run_shadow, M run_shutter, M run_skizz_loop1200, M run_skizzpopo, M run_skizzrettex, M run_spring, M run_stoned, M run_three, M run_toxic_green, M run_world_war_zero, M run_yellow_hell, M yoshiloop, M zelda, M 2of4, M 4of4, M Anaphore, M Autumn Sky, M Bullet Master, M DayLight, M GetSpeed 3, M GetSpeed, M GetSpeed2, M Joyride 2, M Killstreak 1, M Kobra 2 Solo, A Lets Climb, M Lonely Swim 3, M Lonely Swim 4, M Lucid Dream, M Mini Zero II, M Nytro, M Race_Sanktoras, M Raid, M SpaceIsKey, M Spallok, M TOPOS, M The Space Station, M Weird Cave, M run_guy_25

---
## [GeoB99/reactos](https://github.com/GeoB99/reactos)@[61a6236b9f...](https://github.com/GeoB99/reactos/commit/61a6236b9f74082c828b10425c555c892db8ee57)
#### Sunday 2022-06-26 09:21:38 by George Bișoc

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
## [darshan-/dot](https://github.com/darshan-/dot)@[57cb210fe2...](https://github.com/darshan-/dot/commit/57cb210fe20d661ab6788773f2f5e91dea03a2de)
#### Sunday 2022-06-26 10:01:40 by Darshan-Josiah Barber

Changing binding of enter to newline-and-indent completely breaks enter key in minibuffer.  Which is batshit crazy, insane, annoying, fucked up, and hard to believe.  But okay, found a workaround to what seems like the stupidest design ever.

---
## [xavier-kong/chrome-extensions](https://github.com/xavier-kong/chrome-extensions)@[32184a7a7f...](https://github.com/xavier-kong/chrome-extensions/commit/32184a7a7fc11caf1c007066f34375abbcc65ac9)
#### Sunday 2022-06-26 11:03:43 by xavier-kong

One year, 365 days of coding. What shocked me the most was not that I learnt to code and got a software engineer job in a year, but that I was able to continue doing something without fail for a year. While I did not invent the next facebook while I was programming, I did learn to persevere. It could've been my ego reminding me of the shame of failure if I failed to commit for the day, but nevertheless, I persevered. And at the end of the day, that is what means the most to me. Life is too short for me to not aim higher and higher. See you at the top.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[80859c472a...](https://github.com/mrakgr/The-Spiral-Language/commit/80859c472a55e3e00ec5e24cd58950e7661b9740)
#### Sunday 2022-06-26 13:03:22 by Marko Grdinić

"11:45am. I am up. I blame getting up so late on my addiction to Legendary Mechanic. So far I am on chapter 580.

Let me chill a bit here and then I will start

https://boards.4chan.org/ic/thread/6123500/thoughts-on-this-nigga

I want to watch some of the vids in this thread.

https://youtu.be/8o6-2DwWWc4
●●の意見は、絶対に聞いちゃダメです。

I'll start with this one.

https://youtu.be/e7HvWvOM6jc
【気まぐれ添削48】プロが解説します！上達のポイント！

I do not feel like watching it all, let me also watch this for a bit. Then I'll post my work from yesterday on Twitter.

12:25pm. 15m of this is enough. I am not a 2d painter just yet, so I do not need to watch this right now.

https://www.youtube.com/watch?v=t1O7LpOTBfM
Jade Moon Upon a Sea of Clouds - Disc 1: Glazed Moon Over the Tides｜Genshin Impact

The Genshin Impact OST is 10/10.

12:30pm. https://www.flickr.com/creativecommons/

Before I post anything, let me just figure out what the license of the image I used was.

Hmmm, I think I used a copy righted background. I should just find something else. Yeah, that means redoing the render and the style transfer, but it no big deal.

No wait, where the hell does it say what the license is?

Yeah, I see it. The one I used is definitely fully copyrighted.

https://flic.kr/p/WycaKs

Let me go with this instead.

12:40pm. Let me redo the render.

///

I'll go with this as the finished image. It looks too much like an UFO instead of flying city, but it is fine. I only have a vague sense of what I want to do in my mind, and I can't exactly reverse the high level representation backwards through the layers to arrive at an image like a neural net could. In programming, such a high level representation coupled with some experience and skill is all that is needed to create a program, but in art being able to visualize details would be beneficial. I am guessing that to reach the apex skill as a human, one needs such an ability. Too bad, I do not have it, but I am not upset as even this good enough.

Two days ago I had a scare that my computer is failing due to all the render time crashed. Since then I've realized that they are happening due to my CPU overheating. Also, that is probably why the Luxcore room render was crashing. I also forgot to set the GPU in the preferences, so it was doing all the processing on the CPU. 3.1 was set properly which is why it was more stable. The GPU was taking the load off the CPU. What I've done is open the side case to let the air come in, and the temp went down by 6C. This was enough to stabilize it completely.

The original is pretty simple, this is how a sketchy style would look in 3d. Flats and simple shapes everywhere as well as lack of sufficient variation, unlike in 2d where the lines would be wild and unpolished. I thought of going for more elaborate models, but it does not matter. As long as it looks nice to look at, even a sketchy look is fine. At this point rather than focusing on improving the quality of my images, I should be focusing on the speed I am putting them out. This one took far too long to finish as it is.

Let me calculate it. I am going to ignore the 7 days I wasted messing with procedural generation and kitbashing to no result. My serious attempt of doing it all by my own hand is 3-4 days. A lot of this time was spent on getting a grasp on Scatter 5. I also got a grasp on some auxiliary stuff like Blender scenes, its asset browser and view layers. Had I been more skilled a work like this would definitely have been possible in a single day. But it is fine. I am low 3/5, not the apex of humanity. I've just about reached the level where I am starting to form my own style.

This time I was focusing on not repeating the mistake from my work on the room where I did too much detailing only to have the style transfer get rid of most of it. I did the right thing by focusing on the essentials.

From here on out, I will stop work on the backgrounds and get back into sculpting for a while. I need to create the chara models. I've established a good foundation last year, but my sculpting skills are still half baked. I've only done a female base model without any clothing, hair or coloring. I also haven't rigged it. Still, I am confident it won't take me too long to get a grasp on those aspects.

I guess I'll check out what Flycat has been up to. His vids really inspired me to get into sculpting. Digital sculpting is amazing, before I got into art, I never realized such an art form even existed. It is uniquely a 21st century invention. The style transfer that I am doing here is also unique to 21st century. In the future once more advanced NNs become affordable, prompt shaping will also enter the scene as a key skill. For that reason I do not want to invest myself too much into visual aesthetics. The image I am now is 3d style sketchy - and in the future I'll just tell the NN to fill in the blanks. This style will be so powerful that I might move to 2d at that time should I want to.

I like 3d though. It is a good tool when it is not burdening you to do detailing, texturing, or crashing on you. When I form my style, the hard parts of learning it will be behind me, and I will be effective at using it for any kind of illustration.

///

1:30pm. Let me get breakfast here. Also it turns out that hotspot rig is not done yet. The uploads are messed up. Thankfully I know where to look now. I'll post the images on Twitter after the break.

2:30pm. Let me resume. First order of business is to post the images on Twitter. Then I will have to look at that hotspot rig again. It just keeps hounding me. I hope that turning off GRO will be enough.

2:55pm. Let me tweet the long chain. This time I'll just send all the style transfered images. This is one of the benefits of not having to bother with /wip/ anymore. Twitter gets pretty pictures and that place gets the middle finger. Even if I just ignore the guy slinging shit at me, why would I put in special effort in posting to that place which would give me no recognition or benefit? They think too highly of themselves.

3pm. https://twitter.com/Ghostlike/status/1541043122582462466?s=20&t=zEORqaf6owSUmryUbu2n0Q

Here it is.

Let me commit here. What I have to do now is check out that hotspot again. Let me do it."

---
## [WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER)@[21dc98f470...](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/commit/21dc98f47084d3ad33cc59a55eb4c61756b25ec4)
#### Sunday 2022-06-26 14:40:05 by WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER

you'll need a few hands if you need to go through this information -- 




Changed paths:

M C16 - DEALINGS -- UNFAIR DEALINGS AND INSIDER INFORMATION.html


A LOAN 50074 - C16-93715 ANNEXED IN 153974 CARRIED OVER TO 1516523.html




-------- Forwarded Message --------
Subject: 	[BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER] c4c86c: 93715 --- nov13 and Dec18 2021 - could have saved ...
Date: 	Mon, 23 May 2022 05:02:16 -0700
From: 	1212-5858 <noreply@github.com>
To: 	MS60710444266@YAHOO.COM, BLOCK803LOT11@OUTLOOK.COM


Branch: refs/heads/93715-CS16-93715-153974

Home: https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER

Commit: c4c86cdbcc0e0fa3ea2869b7cf97d6fb393ae7dd

https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/commit/c4c86cdbcc0e0fa3ea2869b7cf97d6fb393ae7dd

Author: 1212-5858 <70865813+BSCPGROUPHOLDINGSLLC@users.noreply.github.com>

Date: 2022-05-23 (Mon, 23 May 2022)



Changed paths:

M C16 - DEALINGS -- UNFAIR DEALINGS AND INSIDER INFORMATION.html

A LOAN 50074 - C16-93715 ANNEXED IN 153974 CARRIED OVER TO 1516523.html



Log Message:

-----------

93715 --- nov13 and Dec18 2021 - could have saved about 1.5 billion dollars by switching to BBO.



ATTN: MR. MOORE & CO.

ONE STATE FARM PLAZA, BLOOMINGTON, IL, 61710



I REQUESTED AN ESTOPPEL

--- --- TO CEASE AND DESIST FROM ALL THE ACTIVITY



addr.: STATE FARM



https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=s5WAeCnxmd/hcOI4eTnbig==



addr.: THE ZUCKER FAMILY & ITS COUNSELORS [ all of them ]



https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=Jf3Un/JaVXZwF7kvbaee4w==



NOTWITHSTANDING FOOLING AROUND WITH A 40' ACT MUTUAL FUND.

IF YOU ARE LOOKING FOR AN EARLY RETIREMENT, IT DOESN'T HAVE TO BE THIS WAY.



PLUS, THE NAME HASN'T CHANGED THIS YEAR YET - AND IT DOESN'T HAVE TO....



TWENTY-FIVE MILLION US DOLLARS, UPFRONT



AND CONSIDER THE MATTER CLOSED, WITH THE IMPLIED "COVERAGE" THEREAFTER.



WITHOUT ANY LEGAL EXPOSURES, AND WITH MYSELF THERE TO ASSIST YOU PERSONALLY - UNTIL THE DISASTER YOUR ADVISORS HAVE LEFT YOU WITH IS CLEAR.



UPFRONT – THAT IS MY COST, UNLESS YOU HAVE ANOTHER PROFESSIONAL TO DEAL WITH YOUR COMPANY'S AFFAIRS LEGITIMATELY AFTER THE FACT... AND NOT THE KIND OF PROFESSIONAL THE ZUCKER WOULD HIRE TO WATCH ME IN A HOTEL ROOM AT 5AM - JUST LKE THE ATTACHED FILE.



A BETTER USE OF YOUR CREDIT LINE ANYWAYS, FOR ALL INTENSIVE PURPOSES.



TIME SENSITIVE, AS ALWAYS.



/S/ BO DINCER



MS60710444266@YAHOO.COM

BDINCER66@ICLOUD.COM

TEL.: 646-256-3609



CARRIES OVER, TRUST ME... I AM NOT A ZUCKER, AND THEY CAN NOT AFFORD ME - AT ANY PRICE.



– YOUR $25 MILLION DOLLAR CREDIT LINE IS GOING TO BE ENOUGH TO COVER MY COSTS TO REPAIR THE FIRM.

AND FOR FREE OF COURSE...

BUT ONLY AFTER WE SETTLE.



https://www.scribd.com/document/386161673/Bo-Dincer-New-York-City-Fixed-Income-Trader-Baris-Dincer-Maritime-Capital



https://en.everybodywiki.com/Maritime_Capital_Partners_LP



#GOCARDS.



THANK FOR REACHING OUT, HAVE A GOOD NIGHT - AND SORRY I WAS WORKING HK HOURS AGAIN.



>> OUT OF COURT SETTLEMENT PRICE IN US DOLLARS $25,000,000.00



WITH THE IMPLIED "COVERAGE" OF PRE-EXISTING MATTERS SETTLED



#1

THANKS DAVID FOR YOUR EMAIL AGAIN MR. MOORE.





/S/ BO DINCER.

you know what code to use, same as last

646-256-3609



#12-12.5858



##1

---
## [b3pio/AuthenticatorPro](https://github.com/b3pio/AuthenticatorPro)@[fd5737fd9b...](https://github.com/b3pio/AuthenticatorPro/commit/fd5737fd9b55b9e36f6e423d5d26bf880afe0ed6)
#### Sunday 2022-06-26 14:45:27 by Robert Harnett

56 New Icons + Complete Update of Existing Icons

# Authenticator Pro Pull Request Changelog

## TL;DR:
- Added 56 New Icons
- Updated any out of date icons (eg; Adobe).
- Remade some icons that looked low quality (eg: onshape), I admit I don't know how noticeable this is when scaled down but it allows for greater flexibility in the future if you ever decide to alter icon scaling.)
- Remade ones that were scaled incorrectly  to the 128x128 size (eg patreon).
- Note there's a fair few where they look nearly identical to existing icons, on some, the logo's have changed a tiny little bit such as a small colour change, on others they are essentially identical. At the stage where I was comparing any of the existing icons to remade icons I had done, I had basically done the hard part already and would only need to save as png, so If I remade one and it turned out to be the same I decided to still export and replace the existing icon because it looked like there was no Anti-Aliasing on the existing icons. 'onshape.png' is the clearest example of this.
- Deleted icons that are no longer needed, such as unnecessary dark mode versions, icons of services that don't exist, 'Version2' of any icons as these feel redundant, and icons of services that use a account under a different name eg: 'Yandex mail' falls under 'Yandex'.
- Updated missing_icons.txt

### Any feedback or issues please let me know, Im aware this is a large change so I don't expect it to be 100% perfect.

## Full Changelog:

### New Icons:
- Addiko Bank
- Advcash (+ Dark Mode)
- Automate.io
- Avanza
- Betfair
- BigMind
- Bitgo
- Brightbox
- Cake defi
- Call of Duty (+ Dark Mode)
- Cisco
- Clearscore (+ Dark Mode)
- Clubhouse (+ Dark Mode)
- Community America
- Crashplan
- Datto
- Degiro
- Ecobee[^Ecobee]
- Fastly
- Files.com
- Gaijin
- Google Cloud
- Hey
- Hodlenaut
- IBM
- ID.me
- idrive.com
- Intuit[^Intuit]
- Ionos
- Jovia
- Koofr
- Luno (+ Dark Mode)
- MacStadium (+ Dark Mode)
- Make
- Mercury (+ Dark Mode)
- Meta
- Morgan Stanley (+ Dark Mode) (Easily the most boring logo I've ever seen, not much I could do here)
- Nordlayer
- Nutstore
- Onehub
- Optimizely
- Oracle
- Pusher (+ Dark Mode)
- Rewind
- Runescape (+ Dark Mode)
- SEFCU
- Sony (+ Dark Mode)
- Standard Notes
- Strato
- Sync
- Trading 212
- Ubuntu One
- VMware
- VR Chat
- Whois
- Xero

### Updated Icons:
- 1and1
- 1password
- 3cx (Slightly darker grey)
- Adobe
- Airship
- Allegro
- Altaro
- Amazon
- Appveyor
- Arduino
- Asana
- Ascendex
- Atlassian
- Autodesk (+ Dark Mode)
- AWS (+ Dark Mode)
- Azure
- Basecamp
- Best Buy
- Binance
- Bitcoin
- Bitdefender
- Bitfinex
- Bitflyer
- Bitstamp (+ Dark Mode)
- Bittrex
- Blizzard
- Blockchain
- Bluehost
- Box
- Buildkite
- BunnyCDN
- Codeberg (+ Dark Mode)
- Codeship (+ Dark Mode)
- Coinjar (+ Dark Mode)
- Confluence
- Contabo
- Control D (+ Dark Mode)
- Crypto.com (+ Dark Mode)
- Dashlane (+ Dark Mode)
- Deutschebahn
- Direct Admin
- Discogs (+ Dark Mode)
- Discord
- Docker
- Dreamhost
- Dropbox
- Electronic Arts
- Envato
- Evernote
- Facebook
- Figma
- Filen (+ Dark Mode)
- Floatplane
- fmfw
- FTX
- Gemini
- Gitlab
- Gmail
- GoDaddy
- Google
- Google Drive
- Google Fi
- Google Fibre
- Google Pay
- Google Play
- Grammarly
- Hellosign
- Heroku
- Hitbtc
- Home Assistant
- Hotbit
- Humble Bundle[^Humble Bundle]
- Huobi
- Instagram
- Intigriti[^Intigriti]
- InVision
- IP Phone Forum
- Itglue
- Jagex
- Jelastic
- Jetbrains (+ Dark Mode)
- Jira
- Jottacloud
- Kaspersky
- Kraken
- Leaseweb
- Linkedin
- Linode
- Litebit
- Local Cryptos
- Local Monero
- Login.gov
- Maicoin
- Mailbox.org
- Mailchimp (+ Dark Mode)
- Mail.com
- Mailfence
- Mailgun
- Mailo
- Mapbox (+ Dark Mode)
- Mastodon
- Matomo
- Mega
- Microsoft
- Microsoft Todo
- Migros
- Mintos
- Monday.com
- Moneyforward
- Moneytree
- Moqups
- Myheritage
- Namecheap
- Name.com (+ Dark Mode)
- Netcup
- Nintendo[^Nintendo]
- Nuget
- Nulab
- NURI
- Onedrive
- Onshape
- Origin
- Outlook
- ovh
- Parsec
- Patreon
- Paykassa
- Paypal
- Paysafecard
- Plex
- Plurk
- Poloniex_Dark
- Private Internet Access
- Proxmox_dark
- Pushover
- Pypi
- Qnap
- Rackspace
- RealVNC
- Robinhood
- Roblox (+ Dark Mode)
- Roboform
- RocketbeansTV
- Salesforce
- Samsung[^Samsung]
- Scaleway
- Shortio
- Simplelogin
- Skype
- Slack
- Snapchat
- Socketlabs
- Solarwinds
- Sproutsocial
- Square
- Squarespace
- Stackpath (+ Dark Mode)
- Statuspage
- Steam (+ Dark Mode)
- Stormgain
- Surfshark
- Synology
- Team Viewer
- Telnyx
- Ting
- T-Mobile
- Tokopedia
- Tor Guard (+ Dark Mode)
- Trello
- Tresorit
- Tutanota
- Twilio
- Twitch
- Twitter
- Ultimaker
- United Domains
- Unlock Base
- Unstoppable Domains
- Updraft
- UpTimeRobot
- Visual Studio Online
- VK
- Voyager
- Vultr
- War Gaming
- Web.de
- Whale Fin
- wordfence
- Wyze (Again... Updated colour and text weight)
- ynab
- YoYo Games
- Zoho
- Zonda (+ Dark Mode)
- Zoom
- Zyxel (+ Dark)

### Deleted Icons:
Some of these have dark mode versions that are either not necessary because they are already legible in both light and dark mode or because they have an updated icon where this is now the case (I previewed them in my icon designer software with the same background colours used in the app to make sure they are clear to see).
- 34sp (Dark Mode)
- Adobe (Dark Mode)
- BasicAttentionToken is a crypto currency by Brave, it's not a service on its own and does not require a icon.
- Best Buy (Dark Mode)
- Box (Dark Mode)
- Crypton I can't find this service anywhere? Even reverse image searched the current icon and it seems it doesn't exist?
- Electronic Arts (Dark Mode)
- Google Cloud Platform (Now called 'Google Cloud')
- Google Pay (Dark Mode)
- Gildwars2 Uses Arenanet to login which already has a account.
- Hangouts (The service no longer exists)
- Integromat has rebranded into 'Make' have added a new icon for it.
- Integrity was misnamed, has simply been named 'Intigriti', icon still exists.
- Jetbrains2 (Removed the logo with the coloured line as it makes the logo really small, using just the square on its own is still within the brand guidelines.
- Patreon (Dark Mode)
- Netcup (Dark Mode)
- Oculus now exists under the 'Meta' name. I have deleted the old logo and created one for Meta.
- Office365 has rebranded as Microsoft365, I still wanted to keep a icon for office for user choice so have updated the icon and named it simply 'Office'
- Samsung[^Samsung]
- 'simpletax.co' looks 100% like a scam or very old proprietary software that almost no one uses. There's several hundred other services I would prefer we make an icon for first rather then this sketchy looking site. What caused this icon to be added? Was it a legitimate user request? I decided to remove it because I question it's legitimacy, while you could argue that's not for the job of someone submitting icons, I really hate this icon and don't want the icon selector to be clogged full of spammy random sites.
- Smashcast no longer exists.
- Starling Bank Developer (Renamed file to simply 'starlingbank')
- Statusmail (Is this an actual service, it seems to just be part of 'statuspage' which already has an icon.
- Synology (Dark Mode)
- Uplay, it's rebranded to 'Ubisoft Connect' and uses a ubisoft account which already has an icon.
- Yandex Mail (Uses a Yandex account which can be for multiple services, I have added a icon for 'Yandex'

### Updated 'missing_icons.txt':
- Removed names of added icons
- 'NordVPN Teams' has rebranded as Nord Layer, icon added.
- 'Bugzilla@Mozilla' uses the 'Mozilla' logo which already exists.
- 'Hover.com' is already added.
- TurboTax, Quickbooks, & Mint all use a shared 'Intuit' account
- removed 'Ukraine' because... well idk what it is other then a country, and I don't think an entire country has 2FA. Well I suppose it probably in a way does have two factor authentication to enter it right now but that's a differant thing entirely.
- Removed 'Samsung Smartthings' as far as im aware it uses a Samsung account.
- 'Remote Desktop Manager' & 'Online' could be any number of services, Im removing them as I don't actually know what the services are.
- 'Launchpad' uses Ubuntu One login, icon added.
- join.me uses 'LogMeIn' which already has an icon.

[^Ecobee]: Ecobee's Logo is rather thin text so this icon is based off of their app icon to improve legibility, funnily enough they seem to realise this problem themselves as they use the same solution for their favicon on their website.

[^Intigriti]: Previously misnamed as 'Integrity', not deleted, just renamed.

[^Intuit]: Their logo is just text which is hard to see so again I've based this icon off of their favicon.

[^Humble Bundle]: Both the old 'H' icon and the bag icon are within official brand guidelines and can both be used, I decided to change to the bag to reduce the use of typography in the icon set, this is a personal preference so let me know if you prefer to use the 'H'.

[^Nintendo]: Even on my Pixel 6 Pro which is both on the higher end of screen size and device PPI the current Nintendo logo is very small and hard to read, here I copied what Nintendo have done on their own website it regards to their favicon. This is again a personal preference to reduce the dependence on type heavy icons. Let me know if I should revert this change.

[^Samsung]: Samsung no longer use the rounded blue logo, so I have deleted it and made the 'samsung2' icon the primary and only Samsung logo.

---
## [WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER)@[e93a3afd9c...](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/commit/e93a3afd9ca89155bc2f5e094e636290d49402e4)
#### Sunday 2022-06-26 14:50:04 by WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER

#GOCARDS ( USC 26, ALSO WILLFULLY OBSTRUCTED under USC 18)

Section 203(f) of the Advisers Act permits the Commission to sanction any person who, at the time of the misconduct, was associated with an investment adviser, if the Commission finds that the sanction is in the public interest and the person has been convicted of any offense specified in Section 203(e)(2) within ten years of the commencement of proceedings. 15 U.S.C. § 80b3(e)(2),(f).

https://www.sec.gov/alj/aljdec/2015/id747ce.pdfconspiracy to commit securities fraud, in violation of 18 U.S.C. § 371; conspiracy to commit wire fraud, in violation of 18 U.S.C. § 1349; securities fraud, in violation of 15 U.S.C. §§ 78j(b), 78ff, and 17 CFR § 240.10b-5; wire fraud, in violation of 18 U.S.C. § 1343; and investment adviser fraud, in violation of 15 U.S.C. §§ 80b-6 and 80b-17. OIP at 2;

On June 23, 2014, Balboa was sentenced to a prison term of fortyeight months, to run concurrently on all counts, followed by three years of supervised release, and ordered to pay restitution of $390,243,873.92 and to forfeit $2,223,000.

15 U.S.C. § 80b3(e)(2)(A). Ex. C at 1-2; Exs. D, E. The superseding indictment charged Balboa with, among other things, engaging in a scheme to falsely inflate the value of illiquid securities between January 2008 and October 2008 and with committing wire fraud.

15 U.S. Code § 78r - Liability for misleading statements (a)Persons liable; persons entitled to recover; defense of good faith; suit at law or in equity; costs, etc. Any person who shall make or cause to be made any statement in any application, report, or document filed pursuant to this chapter or any rule or regulation thereunder or any undertaking contained in a registration statement as provided in subsection (d) of section 78o of this title, which statement was at the time and in the light of the circumstances under which it was made false or misleading with respect to any material fact, shall be liable to any person (not knowing that such statement was false or misleading) who, in reliance upon such statement, shall have purchased or sold a security at a price which was affected by such statement, for damages caused by such reliance, unless the person sued shall prove that he acted in good faith and had no knowledge that such statement was false or misleading. A person seeking to enforce such liability may sue at law or in equity in any court of competent jurisdiction. In any such suit the court may, in its discretion, require an undertaking for the payment of the costs of such suit, and assess reasonable costs, including reasonable attorneys’ fees, against either party litigant.

(b)Contribution Every person who becomes liable to make payment under this section may recover contribution as in cases of contract from any person who, if joined in the original suit, would have been liable to make the same payment.

(c)Period of limitations No action shall be maintained to enforce any liability created under this section unless brought within one year after the discovery of the facts constituting the cause of action and within three years after such cause of action accrued.

[SFITX] 15 U.S. Code § 78s - Registration, responsibilities, and oversight of self-regulatory organizations (5)The Commission shall consult with and consider the views of the Secretary of the Treasury prior to approving a proposed rule filed by a registered securities association that primarily concerns conduct related to transactions in government securities, except where the Commission determines that an emergency exists requiring expeditious or summary action and publishes its reasons therefor. If the Secretary of the Treasury comments in writing to the Commission on a proposed rule that has been published for comment, the Commission shall respond in writing to such written comment before approving the proposed rule. If the Secretary of the Treasury determines, and notifies the Commission, that such rule, if implemented, would, or as applied does (i) adversely affect the liquidity or efficiency of the market for government securities; or (ii) impose any burden on competition not necessary or appropriate in furtherance of the purposes of this section, the Commission shall, prior to adopting the proposed rule, find that such rule is necessary and appropriate in furtherance of the purposes of this section notwithstanding the Secretary’s determination.

https://www.sec.gov/alj/aljdec/2015/id739ce.pdf[t]he proper functioning of the securities industry and markets depends on the integrity of industry participants and their commitment to transparent disclosure. Securities industry participation by persons with a history of fraudulent conduct is antithetical to the protection of investors. . . . We have long held that a history of egregious fraudulent conduct demonstrates unfitness for future participation in the securities industry even if the disqualifying conduct is not related to the professional capacity in which the respondent was acting when he or she engaged in the misconduct underlying the proceeding. The industry relies on the fairness and integrity of all persons associated with each of the professions covered by the collateral bar to forgo opportunities to defraud and abuse other market participants.

TRANSACTIONS OF CERTAIN AFFILIATED PERSONS AND UNDERWRITERS -UNLAWFUL TRANSACTIONS SEC. 17. (a) It shall be unlawful for any affiliated person or pro- moter of or principal underwriter for a registered investment company (other than a company of the character described in section 12 (d) (3) (A) and (B)), or any affiliated person of such a person, promoter, or principal underwriter, acting as principal- (1) knowingly to sell any security or other property to such registered company or to any company controlled by such regis- tered company, unless such sale involves solely (A) securities of which the buyer is the issuer, (B) securities of which the seller is the issuer and which are part of a general offering to the holders of a class of its securities, or (C) securities deposited with the trustee of a unit investment trust or periodic payment plan by the depositor thereof;

(2) knowingly to purchase from such registered company, or from any company controlled by such registered company, any security or other property (except securities of which the seller is the issuer)

Liability of directors, etc., for willful misfeasance. SEC. 17. (h) After one year from the effective date of this title, neither the charter, certificate of incorporation, articles of association, indenture of trust, nor the by-laws of any registered investment company, nor any other instrument pursuant to which such a company is organized or administered, shall contain any provision which protects or purports to protect any director or officer of such company against any liability to the company or to its security holders to which he would otherwise be subject by reason of willful misfeasance, bad faith, gross negligence or reckless disregard of the duties involved in the conduct of his office.

|In the event that any such instrument does not at the effective date of this Act comply with the requirements of this subsection (h) and is not amended to comply therewith prior to the expiration of said one year, such company may nevertheless continue to be a registered investment company and shall not be deemed to violate this subsection if prior to said expiration date each such director or officer shall have filed with the Commission a waiver in writing of any protective provision of the instrument to the extent that it does not comply with this subsection, and each such person subsequently elected or appointed shall before assuming office file a similar waiver. |

(i) After one year from the effective date of this title no contract or agreement under which any person undertakes to act as investment adviser of, or principal underwriter for, a registered investment company shall contain any provision which protects or purports to protect such person against any liability to such company or its security holders to which he would otherwise be subject by reason of willful misfeasance, bad faith, or gross negligence, in the performance of his duties, or by reason of his reckless disregard of his obligations and duties under such contract or agreement.

Injunctions against gross abuse. SEC. 36. The Commission is authorized to bring an action in the proper district court of the United States or United States court of any Territory or other place subject to the jurisdiction of the United States, alleging that a person serving or acting in one or more of the following capacities has been guilty, after the enactment of this title and within five years of the commencement of the action, of gross misconduct or gross abuse of trust in respect of any registered investment company for which such person so serves or acts: (1) as officer, director, member of an advisory board, investment adviser, or depositor; or (2) as principal underwriter, if such registered company is an open-end company, unit investment trust, or face-amount certificate company. If the Commission's allegations of such gross misconduct or gross abuse of trust are established, the court shall enjoin such person from acting in such capacity or capacities either permanently or for such period of time as it in its discretion shall deem appropriate.

SEC. 32. (c) The Commission is authorized, by rules and regulations or order in the public interest or for the protection of investors, to require accountants and auditors to keep reports, work sheets, and other documents and papers relating to registered investment companies for such period or periods as the Commission may prescribe, and to make the same available for inspection by the Commission or any member or representative thereof.

DESTRUCTION AND FALSIFICATION OF REPORTS AND RECORDS SEC. 34.

(a) It shall be unlawful for any person, except as permitted by rule, regulation, or order of the Commission, willfully to destroy, mutilate, or alter any account, book, or other document the preservation of which has been required pursuant to section 31 (a) or 32 (c). (b) It shall be unlawful for any person to make any untrue statement of a material fact in any registration statement, application, report, account, record, or other document filed or transmitted pursuant to this title or the keeping of which is required pursuant to section 31 (a).

It shall be unlawful for any person so filing, transmitting, or keeping any such document to omit to state therein any fact necessary in order to prevent the statements made therein, in the light of the circumstances under which they were made, from being materially misleading. For the purposes of this subsection, any part of any such document which is signed or certified by an accountant or auditor in his capacity as such shall be deemed to be made, filed, transmitted, or kept by such accountant or auditor, as well as by the person filing, transmitting, or keeping the complete document.

ty FDIC

------------------------------------------------------------------------

From: BD DINCER (COLUMBIA UNIVERSITY) At: 12/18/21 19:13:39 UTC-5:00 Subject: Fwd:Fwd:Fwd:Fwd:Fwd:Fwd:STATE FARM - BLOOMINGTON » Northern Trust Company. ACRIS 6MM

|From: BD DINCER (COLUMBIA UNIVERSITY) At: 12/18/21 18:37:39 UTC-5:00 To: Susan Byrne (WESTWOOD MANAGEMENT ) , Julie Hoyer (STATE FARM MUTUAL AU ) , Greg Shull (STATE FARM MUTUAL AU ) , Jeffrey Attwood (STATE FARM MUTUAL AU ) , John Malito (STATE FARM MUTUAL AU ) , Steven Santiccioli (NORTHERN TRUST COMPA ) , Robert Stephan (STATE FARM MUTUAL AU ) , Lisa Rogers (STATE FARM MUTUAL AU ) , Elena Khoziaeva (BRIDGEWAY CAPITAL MA ) , Bill Trauner (STATE FARM MUTUAL AU ) , Heather Caldwell (STATE FARM MUTUAL AU ) , Theresa Baker (STATE FARM MUTUAL AU ) , Tammy Gipson (STATE FARM MUTUAL AU ) , Brent Reeder (NORTHERN TRUST COMPA ) , Michael Whipple (BRIDGEWAY CAPITAL MA ) , Michael Zaroogian (STATE FARM MUTUAL AU ) , Terence Lynch (GAINSCO SERVICE CORP ) , Rebekah Holt (STATE FARM MUTUAL AU ) , Katie Hubbard (STATE FARM MUTUAL AU ) , Leigh Ann Rogalski (STATE FARM MUTUAL AU ) , Chad Moser (STATE FARM MUTUAL AU ) , Tim Zelgert (STATE FARM MUTUAL AU ) , Ray Renken (STATE FARM MUTUAL AU ) , Kara Olson (STATE FARM MUTUAL AU ) , Jim Chan (BLACKROCK INSTITUTIO ) , Matt Harvey (STATE FARM MUTUAL AU ) , Steve Brucker (STATE FARM MUTUAL AU ) , John Socha (STATE FARM MUTUAL AU ) , Jennifer Hsui (BLACKROCK INSTITUTIO ) , Joe Young (STATE FARM MUTUAL AU ) , Wade Reinthaler (STATE FARM MUTUAL AU ) , Scott Reid (STATE FARM MUTUAL AU ) , Adam Hallman (STATE FARM MUTUAL AU ) , Tyler Smith (STATE FARM MUTUAL AU ) , Wei Hao (STATE FARM MUTUAL AU ) , Chris Minter (STATE FARM MUTUAL AU ) , Shelly Marsh (STATE FARM MUTUAL AU ) , Hollie Marsh (STATE FARM MUTUAL AU ) , Matthew Lockridge (WESTWOOD MANAGEMENT ) , Rich Rebholz (STATE FARM MUTUAL AU ) , Michael Mayberger (STATE FARM MUTUAL AU ) , Ashley Smock (STATE FARM MUTUAL AU ) , Brian Bengtson (STATE FARM MUTUAL AU ) , Cory Swartzlander (STATE FARM MUTUAL AU ) , Scott Lawson (WESTWOOD MANAGEMENT ) , Ayman Bari (STATE FARM MUTUAL AU ) , Adam Vales (STATE FARM MUTUAL AU ) , Robert Middleton (STATE FARM MUTUAL AU ) , Shane Jent (STATE FARM MUTUAL AU ) , Kevin Rock (STATE FARM MUTUAL AU ) , Mark Dunford (STATE FARM MUTUAL AU ) , Jean-Francois Ducrest (DUCREST, JEAN-FRANCO ) , Caroline Dirks (STATE FARM MUTUAL AU ) , Kyle Gilmore (STATE FARM MUTUAL AU ) , Diane Hsiung (GEODE CAPITAL MANAGE ) , Hunter Rose (STATE FARM MUTUAL AU ) , Cameron Kurak (STATE FARM MUTUAL AU ) , Mark Broughton (FIRST REPUBLIC BANK ) , Betsey Euliss (STATE FARM MUTUAL AU ) , Kim Bretz (STATE FARM MUTUAL AU ) , Jon Wilson (STATE FARM MUTUAL AU ) , Numan Ahmed (STATE FARM MUTUAL AU ) , Walter Ruane (STATE FARM MUTUAL AU ) , Shawna Barlow (STATE FARM MUTUAL AU ) , Philip Kroger (STATE FARM MUTUAL AU ) , Gabrielle Poole (STATE FARM MUTUAL AU ) , Ricardo Correa (STATE FARM MUTUAL AU ) , Felipe Castella (STATE FARM MUTUAL AU ) , Matt Krebsbach (STATE FARM MUTUAL AU ) , Gabriel Prado Correa (STATE FARM MUTUAL AU ) , Larnita Gates (STATE FARM MUTUAL AU ) , Ketrick Karsten (STATE FARM MUTUAL AU ) , Sophie Kim (STATE FARM MUTUAL AU ) , Vicki Trimpe (STATE FARM MUTUAL AU ) , Christin Higham (STATE FARM MUTUAL AU ) , BD DINCER (COLUMBIA UNIVERSITY ) , b.dincer@columbia.edu Cc: Kerri Saperstein (MORGAN STANLEY & CO. ) , COLIN.BROOKS@MORGAN.STANLEY.COM Subject: Fwd:Fwd:Fwd:Fwd:Fwd:STATE FARM - BLOOMINGTON » Northern Trust Company. ACRIS 6MM From: BD DINCER (COLUMBIA UNIVERSITY) At: 12/18/21 18:34:02 UTC-5:00 To: Kerri Saperstein (MORGAN STANLEY & CO. ) , colin.brooks@morgan.stanley.com Cc: james.gorman@morganstanley.com Subject: Fwd:Fwd:Fwd:Fwd:STATE FARM - BLOOMINGTON » Northern Trust Company. ACRIS 6MM From: BD DINCER (COLUMBIA UNIVERSITY) At: 12/18/21 18:27:46 UTC-5:00 To: james.gorman@morgan.stanley.com Cc: Christina Constantine (FINRA ) , Ms Hy (MORGAN STANLEY INVES ) , Ms Hyld (MORGAN STANLEY ) , Peter Melley (FINRA ) , Susan Byrne (WESTWOOD MANAGEMENT ) , Julie Hoyer (STATE FARM MUTUAL AU ) , Greg Shull (STATE FARM MUTUAL AU ) , Jeffrey Attwood (STATE FARM MUTUAL AU ) , John Malito (STATE FARM MUTUAL AU ) , Steven Santiccioli (NORTHERN TRUST COMPA ) , Robert Stephan (STATE FARM MUTUAL AU ) , Lisa Rogers (STATE FARM MUTUAL AU ) , Elena Khoziaeva (BRIDGEWAY CAPITAL MA ) , Bill Trauner (STATE FARM MUTUAL AU ) , Heather Caldwell (STATE FARM MUTUAL AU ) , Theresa Baker (STATE FARM MUTUAL AU ) , Tammy Gipson (STATE FARM MUTUAL AU ) , Brent Reeder (NORTHERN TRUST COMPA ) , Michael Whipple (BRIDGEWAY CAPITAL MA ) , Michael Zaroogian (STATE FARM MUTUAL AU ) , Terence Lynch (GAINSCO SERVICE CORP ) , Rebekah Holt (STATE FARM MUTUAL AU ) , Katie Hubbard (STATE FARM MUTUAL AU ) , Leigh Ann Rogalski (STATE FARM MUTUAL AU ) , Chad Moser (STATE FARM MUTUAL AU ) , Tim Zelgert (STATE FARM MUTUAL AU ) , Ray Renken (STATE FARM MUTUAL AU ) , Kara Olson (STATE FARM MUTUAL AU ) , Jim Chan (BLACKROCK INSTITUTIO ) , Matt Harvey (STATE FARM MUTUAL AU ) , Steve Brucker (STATE FARM MUTUAL AU ) , John Socha (STATE FARM MUTUAL AU ) , Jennifer Hsui (BLACKROCK INSTITUTIO ) , Joe Young (STATE FARM MUTUAL AU ) , Wade Reinthaler (STATE FARM MUTUAL AU ) , Scott Reid (STATE FARM MUTUAL AU ) , Adam Hallman (STATE FARM MUTUAL AU ) , Tyler Smith (STATE FARM MUTUAL AU ) , Wei Hao (STATE FARM MUTUAL AU ) , Chris Minter (STATE FARM MUTUAL AU ) , Shelly Marsh (STATE FARM MUTUAL AU ) , Hollie Marsh (STATE FARM MUTUAL AU ) , Matthew Lockridge (WESTWOOD MANAGEMENT ) , Rich Rebholz (STATE FARM MUTUAL AU ) , Michael Mayberger (STATE FARM MUTUAL AU ) , Ashley Smock (STATE FARM MUTUAL AU ) , Brian Bengtson (STATE FARM MUTUAL AU ) , Cory Swartzlander (STATE FARM MUTUAL AU ) , Scott Lawson (WESTWOOD MANAGEMENT ) , Ayman Bari (STATE FARM MUTUAL AU ) , Adam Vales (STATE FARM MUTUAL AU ) , Robert Middleton (STATE FARM MUTUAL AU ) , Shane Jent (STATE FARM MUTUAL AU ) , Kevin Rock (STATE FARM MUTUAL AU ) , Mark Dunford (STATE FARM MUTUAL AU ) , Jean-Francois Ducrest (DUCREST, JEAN-FRANCO ) , Caroline Dirks (STATE FARM MUTUAL AU ) , Kyle Gilmore (STATE FARM MUTUAL AU ) , Diane Hsiung (GEODE CAPITAL MANAGE ) , Hunter Rose (STATE FARM MUTUAL AU ) , Cameron Kurak (STATE FARM MUTUAL AU ) , Mark Broughton (FIRST REPUBLIC BANK ) , Betsey Euliss (STATE FARM MUTUAL AU ) , Kim Bretz (STATE FARM MUTUAL AU ) , Jon Wilson (STATE FARM MUTUAL AU ) , Numan Ahmed (STATE FARM MUTUAL AU ) , Walter Ruane (STATE FARM MUTUAL AU ) , Shawna Barlow (STATE FARM MUTUAL AU ) , Philip Kroger (STATE FARM MUTUAL AU ) , Gabrielle Poole (STATE FARM MUTUAL AU ) , Ricardo Correa (STATE FARM MUTUAL AU ) , Felipe Castella (STATE FARM MUTUAL AU ) , Matt Krebsbach (STATE FARM MUTUAL AU ) , Gabriel Prado Correa (STATE FARM MUTUAL AU ) , Larnita Gates (STATE FARM MUTUAL AU ) , Ketrick Karsten (STATE FARM MUTUAL AU ) , Sophie Kim (STATE FARM MUTUAL AU ) , Vicki Trimpe (STATE FARM MUTUAL AU ) , Christin Higham (STATE FARM MUTUAL AU ) , BD DINCER (COLUMBIA UNIVERSITY ) , Donald Rizer (FINRA ) , Paul Aragon (FINRA ) , b.dincer@columbia.edu, chair@sec.gov Subject: Fwd:Fwd:Fwd:STATE FARM - BLOOMINGTON » Northern Trust Company. ACRIS 6MM From: BD DINCER (COLUMBIA UNIVERSITY) At: 12/18/21 18:22:33 UTC-5:00 To: Kerri Saperstein (MORGAN STANLEY & CO. ) , james.gorman@morganstanley.com Cc: bd2561@columbia.edu Subject: Fwd:Fwd:STATE FARM - BLOOMINGTON » Northern Trust Company. ACRIS 6MM From: BD DINCER (COLUMBIA UNIVERSITY) At: 12/18/21 18:15:44 UTC-5:00 To: Ms. Hayashi (NOMURA SECURITIES CO ) , Morgan32 Stanley (MORGAN STANLEY ADVTG ) , Morgan Stanley154 (MORGAN STANLEY ADVTG ) , Morgan Stanley15 (MORGAN STANLEY ADVTG ) , Ms Hy (MORGAN STANLEY INVES ) , Ms Hyld (MORGAN STANLEY ) Cc: Kerri Saperstein (MORGAN STANLEY & CO. ) , Cmo Citibank (CITIBANK NA ) , Samriddi Abney (FEDERAL HOME LOAN BA ) , Federated Mmktops (FEDERATED INVESTMENT ) , Jesse Aguilar (FEDERAL HOME LOAN BA ) , Shafat Alam (FEDERAL RESERVE BANK ) , Steven Santiccioli (NORTHERN TRUST COMPA ) , bd2561@columbia.edu, colin.brooks@morgan.stanley.com Subject: Fwd:STATE FARM - BLOOMINGTON » Northern Trust Company. ACRIS 6MM Hey SAPS... Merry Christmas! You think this guy will figure it out??? - THE 6MM? Brent Reeder Fund Manager Northern Trust Company, The +1-312-557-0153 (o) 181 W Madison St bdr11@bloomberg.net (w) Chicago IL 60602-4510, US Focus Large Cap Stocks, Growth Investing, United States, Equities, Mid Cap Stocks, Small Cap Stocks, Global, United Kingdom, | More » Funds Managed (43 Funds/51.6B Total Assets in USD) | More » » » » » » » 590xxxx » » » » » » ??????? Investment Information Analyst State Farm Mutual Automobile Ins Co +1-309-735-2705 (o) 1 State Farm Plz +1-309-530-1865 (m) Investment Department E-8 krock5@bloomberg.net (w) Bloomington IL 61701, US You think this guy will figure it out??? - THE 6MM? Phil Supple 1 Views Today Spokesperson Career State Farm Life Insurance Co Current +1-800-782-8332 (o) 1 State Farm Plaza State Farm Life Insurance Co phil.supple.hid9@statefarm.com (w Bloomington IL 61710, US How funny was Benny ......... I like Benny also... Plus no problems after that. Right? |

From: BD DINCER (COLUMBIA UNIVERSITY) At: 12/18/21 19:13:39 UTC-5:00 Subject: Fwd:Fwd:Fwd:Fwd:Fwd:Fwd:STATE FARM - BLOOMINGTON » Northern Trust Company. ACRIS 6MM

|From: BD DINCER (COLUMBIA UNIVERSITY) At: 12/18/21 18:37:39 UTC-5:00 To: Susan Byrne (WESTWOOD MANAGEMENT ) , Julie Hoyer (STATE FARM MUTUAL AU ) , Greg Shull (STATE FARM MUTUAL AU ) , Jeffrey Attwood (STATE FARM MUTUAL AU ) , John Malito (STATE FARM MUTUAL AU ) , Steven Santiccioli (NORTHERN TRUST COMPA ) , Robert Stephan (STATE FARM MUTUAL AU ) , Lisa Rogers (STATE FARM MUTUAL AU ) , Elena Khoziaeva (BRIDGEWAY CAPITAL MA ) , Bill Trauner (STATE FARM MUTUAL AU ) , Heather Caldwell (STATE FARM MUTUAL AU ) , Theresa Baker (STATE FARM MUTUAL AU ) , Tammy Gipson (STATE FARM MUTUAL AU ) , Brent Reeder (NORTHERN TRUST COMPA ) , Michael Whipple (BRIDGEWAY CAPITAL MA ) , Michael Zaroogian (STATE FARM MUTUAL AU ) , Terence Lynch (GAINSCO SERVICE CORP ) , Rebekah Holt (STATE FARM MUTUAL AU ) , Katie Hubbard (STATE FARM MUTUAL AU ) , Leigh Ann Rogalski (STATE FARM MUTUAL AU ) , Chad Moser (STATE FARM MUTUAL AU ) , Tim Zelgert (STATE FARM MUTUAL AU ) , Ray Renken (STATE FARM MUTUAL AU ) , Kara Olson (STATE FARM MUTUAL AU ) , Jim Chan (BLACKROCK INSTITUTIO ) , Matt Harvey (STATE FARM MUTUAL AU ) , Steve Brucker (STATE FARM MUTUAL AU ) , John Socha (STATE FARM MUTUAL AU ) , Jennifer Hsui (BLACKROCK INSTITUTIO ) , Joe Young (STATE FARM MUTUAL AU ) , Wade Reinthaler (STATE FARM MUTUAL AU ) , Scott Reid (STATE FARM MUTUAL AU ) , Adam Hallman (STATE FARM MUTUAL AU ) , Tyler Smith (STATE FARM MUTUAL AU ) , Wei Hao (STATE FARM MUTUAL AU ) , Chris Minter (STATE FARM MUTUAL AU ) , Shelly Marsh (STATE FARM MUTUAL AU ) , Hollie Marsh (STATE FARM MUTUAL AU ) , Matthew Lockridge (WESTWOOD MANAGEMENT ) , Rich Rebholz (STATE FARM MUTUAL AU ) , Michael Mayberger (STATE FARM MUTUAL AU ) , Ashley Smock (STATE FARM MUTUAL AU ) , Brian Bengtson (STATE FARM MUTUAL AU ) , Cory Swartzlander (STATE FARM MUTUAL AU ) , Scott Lawson (WESTWOOD MANAGEMENT ) , Ayman Bari (STATE FARM MUTUAL AU ) , Adam Vales (STATE FARM MUTUAL AU ) , Robert Middleton (STATE FARM MUTUAL AU ) , Shane Jent (STATE FARM MUTUAL AU ) , Kevin Rock (STATE FARM MUTUAL AU ) , Mark Dunford (STATE FARM MUTUAL AU ) , Jean-Francois Ducrest (DUCREST, JEAN-FRANCO ) , Caroline Dirks (STATE FARM MUTUAL AU ) , Kyle Gilmore (STATE FARM MUTUAL AU ) , Diane Hsiung (GEODE CAPITAL MANAGE ) , Hunter Rose (STATE FARM MUTUAL AU ) , Cameron Kurak (STATE FARM MUTUAL AU ) , Mark Broughton (FIRST REPUBLIC BANK ) , Betsey Euliss (STATE FARM MUTUAL AU ) , Kim Bretz (STATE FARM MUTUAL AU ) , Jon Wilson (STATE FARM MUTUAL AU ) , Numan Ahmed (STATE FARM MUTUAL AU ) , Walter Ruane (STATE FARM MUTUAL AU ) , Shawna Barlow (STATE FARM MUTUAL AU ) , Philip Kroger (STATE FARM MUTUAL AU ) , Gabrielle Poole (STATE FARM MUTUAL AU ) , Ricardo Correa (STATE FARM MUTUAL AU ) , Felipe Castella (STATE FARM MUTUAL AU ) , Matt Krebsbach (STATE FARM MUTUAL AU ) , Gabriel Prado Correa (STATE FARM MUTUAL AU ) , Larnita Gates (STATE FARM MUTUAL AU ) , Ketrick Karsten (STATE FARM MUTUAL AU ) , Sophie Kim (STATE FARM MUTUAL AU ) , Vicki Trimpe (STATE FARM MUTUAL AU ) , Christin Higham (STATE FARM MUTUAL AU ) , BD DINCER (COLUMBIA UNIVERSITY ) , b.dincer@columbia.edu Cc: Kerri Saperstein (MORGAN STANLEY & CO. ) , COLIN.BROOKS@MORGAN.STANLEY.COM Subject: Fwd:Fwd:Fwd:Fwd:Fwd:STATE FARM - BLOOMINGTON » Northern Trust Company. ACRIS 6MM From: BD DINCER (COLUMBIA UNIVERSITY) At: 12/18/21 18:34:02 UTC-5:00 To: Kerri Saperstein (MORGAN STANLEY & CO. ) , colin.brooks@morgan.stanley.com Cc: james.gorman@morganstanley.com Subject: Fwd:Fwd:Fwd:Fwd:STATE FARM - BLOOMINGTON » Northern Trust Company. ACRIS 6MM From: BD DINCER (COLUMBIA UNIVERSITY) At: 12/18/21 18:27:46 UTC-5:00 To: james.gorman@morgan.stanley.com Cc: Christina Constantine (FINRA ) , Ms Hy (MORGAN STANLEY INVES ) , Ms Hyld (MORGAN STANLEY ) , Peter Melley (FINRA ) , Susan Byrne (WESTWOOD MANAGEMENT ) , Julie Hoyer (STATE FARM MUTUAL AU ) , Greg Shull (STATE FARM MUTUAL AU ) , Jeffrey Attwood (STATE FARM MUTUAL AU ) , John Malito (STATE FARM MUTUAL AU ) , Steven Santiccioli (NORTHERN TRUST COMPA ) , Robert Stephan (STATE FARM MUTUAL AU ) , Lisa Rogers (STATE FARM MUTUAL AU ) , Elena Khoziaeva (BRIDGEWAY CAPITAL MA ) , Bill Trauner (STATE FARM MUTUAL AU ) , Heather Caldwell (STATE FARM MUTUAL AU ) , Theresa Baker (STATE FARM MUTUAL AU ) , Tammy Gipson (STATE FARM MUTUAL AU ) , Brent Reeder (NORTHERN TRUST COMPA ) , Michael Whipple (BRIDGEWAY CAPITAL MA ) , Michael Zaroogian (STATE FARM MUTUAL AU ) , Terence Lynch (GAINSCO SERVICE CORP ) , Rebekah Holt (STATE FARM MUTUAL AU ) , Katie Hubbard (STATE FARM MUTUAL AU ) , Leigh Ann Rogalski (STATE FARM MUTUAL AU ) , Chad Moser (STATE FARM MUTUAL AU ) , Tim Zelgert (STATE FARM MUTUAL AU ) , Ray Renken (STATE FARM MUTUAL AU ) , Kara Olson (STATE FARM MUTUAL AU ) , Jim Chan (BLACKROCK INSTITUTIO ) , Matt Harvey (STATE FARM MUTUAL AU ) , Steve Brucker (STATE FARM MUTUAL AU ) , John Socha (STATE FARM MUTUAL AU ) , Jennifer Hsui (BLACKROCK INSTITUTIO ) , Joe Young (STATE FARM MUTUAL AU ) , Wade Reinthaler (STATE FARM MUTUAL AU ) , Scott Reid (STATE FARM MUTUAL AU ) , Adam Hallman (STATE FARM MUTUAL AU ) , Tyler Smith (STATE FARM MUTUAL AU ) , Wei Hao (STATE FARM MUTUAL AU ) , Chris Minter (STATE FARM MUTUAL AU ) , Shelly Marsh (STATE FARM MUTUAL AU ) , Hollie Marsh (STATE FARM MUTUAL AU ) , Matthew Lockridge (WESTWOOD MANAGEMENT ) , Rich Rebholz (STATE FARM MUTUAL AU ) , Michael Mayberger (STATE FARM MUTUAL AU ) , Ashley Smock (STATE FARM MUTUAL AU ) , Brian Bengtson (STATE FARM MUTUAL AU ) , Cory Swartzlander (STATE FARM MUTUAL AU ) , Scott Lawson (WESTWOOD MANAGEMENT ) , Ayman Bari (STATE FARM MUTUAL AU ) , Adam Vales (STATE FARM MUTUAL AU ) , Robert Middleton (STATE FARM MUTUAL AU ) , Shane Jent (STATE FARM MUTUAL AU ) , Kevin Rock (STATE FARM MUTUAL AU ) , Mark Dunford (STATE FARM MUTUAL AU ) , Jean-Francois Ducrest (DUCREST, JEAN-FRANCO ) , Caroline Dirks (STATE FARM MUTUAL AU ) , Kyle Gilmore (STATE FARM MUTUAL AU ) , Diane Hsiung (GEODE CAPITAL MANAGE ) , Hunter Rose (STATE FARM MUTUAL AU ) , Cameron Kurak (STATE FARM MUTUAL AU ) , Mark Broughton (FIRST REPUBLIC BANK ) , Betsey Euliss (STATE FARM MUTUAL AU ) , Kim Bretz (STATE FARM MUTUAL AU ) , Jon Wilson (STATE FARM MUTUAL AU ) , Numan Ahmed (STATE FARM MUTUAL AU ) , Walter Ruane (STATE FARM MUTUAL AU ) , Shawna Barlow (STATE FARM MUTUAL AU ) , Philip Kroger (STATE FARM MUTUAL AU ) , Gabrielle Poole (STATE FARM MUTUAL AU ) , Ricardo Correa (STATE FARM MUTUAL AU ) , Felipe Castella (STATE FARM MUTUAL AU ) , Matt Krebsbach (STATE FARM MUTUAL AU ) , Gabriel Prado Correa (STATE FARM MUTUAL AU ) , Larnita Gates (STATE FARM MUTUAL AU ) , Ketrick Karsten (STATE FARM MUTUAL AU ) , Sophie Kim (STATE FARM MUTUAL AU ) , Vicki Trimpe (STATE FARM MUTUAL AU ) , Christin Higham (STATE FARM MUTUAL AU ) , BD DINCER (COLUMBIA UNIVERSITY ) , Donald Rizer (FINRA ) , Paul Aragon (FINRA ) , b.dincer@columbia.edu, chair@sec.gov Subject: Fwd:Fwd:Fwd:STATE FARM - BLOOMINGTON » Northern Trust Company. ACRIS 6MM From: BD DINCER (COLUMBIA UNIVERSITY) At: 12/18/21 18:22:33 UTC-5:00 To: Kerri Saperstein (MORGAN STANLEY & CO. ) , james.gorman@morganstanley.com Cc: bd2561@columbia.edu Subject: Fwd:Fwd:STATE FARM - BLOOMINGTON » Northern Trust Company. ACRIS 6MM From: BD DINCER (COLUMBIA UNIVERSITY) At: 12/18/21 18:15:44 UTC-5:00 To: Ms. Hayashi (NOMURA SECURITIES CO ) , Morgan32 Stanley (MORGAN STANLEY ADVTG ) , Morgan Stanley154 (MORGAN STANLEY ADVTG ) , Morgan Stanley15 (MORGAN STANLEY ADVTG ) , Ms Hy (MORGAN STANLEY INVES ) , Ms Hyld (MORGAN STANLEY ) Cc: Kerri Saperstein (MORGAN STANLEY & CO. ) , Cmo Citibank (CITIBANK NA ) , Samriddi Abney (FEDERAL HOME LOAN BA ) , Federated Mmktops (FEDERATED INVESTMENT ) , Jesse Aguilar (FEDERAL HOME LOAN BA ) , Shafat Alam (FEDERAL RESERVE BANK ) , Steven Santiccioli (NORTHERN TRUST COMPA ) , bd2561@columbia.edu, colin.brooks@morgan.stanley.com Subject: Fwd:STATE FARM - BLOOMINGTON » Northern Trust Company. ACRIS 6MM Hey SAPS... Merry Christmas! You think this guy will figure it out??? - THE 6MM? Brent Reeder Fund Manager Northern Trust Company, The +1-312-557-0153 (o) 181 W Madison St bdr11@bloomberg.net (w) Chicago IL 60602-4510, US Focus Large Cap Stocks, Growth Investing, United States, Equities, Mid Cap Stocks, Small Cap Stocks, Global, United Kingdom, | More » Funds Managed (43 Funds/51.6B Total Assets in USD) | More » » » » » » » 590xxxx » » » » » » ??????? Investment Information Analyst State Farm Mutual Automobile Ins Co +1-309-735-2705 (o) 1 State Farm Plz +1-309-530-1865 (m) Investment Department E-8 krock5@bloomberg.net (w) Bloomington IL 61701, US You think this guy will figure it out??? - THE 6MM? Phil Supple 1 Views Today Spokesperson Career State Farm Life Insurance Co Current +1-800-782-8332 (o) 1 State Farm Plaza State Farm Life Insurance Co phil.supple.hid9@statefarm.com (w Bloomington IL 61710, US How funny was Benny ......... I like Benny also... Plus no problems after that. Right? From: BD DINCER (COLUMBIA UNIVERSITY) At: 12/18/21 18:03:41 UTC-5:00 To: Susan Byrne (WESTWOOD MANAGEMENT ) , Julie Hoyer (STATE FARM MUTUAL AU ) , Greg Shull (STATE FARM MUTUAL AU ) , Jeffrey Attwood (STATE FARM MUTUAL AU ) , John Malito (STATE FARM MUTUAL AU ) , Steven Santiccioli (NORTHERN TRUST COMPA ) , Robert Stephan (STATE FARM MUTUAL AU ) , Lisa Rogers (STATE FARM MUTUAL AU ) , Elena Khoziaeva (BRIDGEWAY CAPITAL MA ) , Bill Trauner (STATE FARM MUTUAL AU ) , Heather Caldwell (STATE FARM MUTUAL AU ) , Theresa Baker (STATE FARM MUTUAL AU ) , Tammy Gipson (STATE FARM MUTUAL AU ) , Brent Reeder (NORTHERN TRUST COMPA ) , Michael Whipple (BRIDGEWAY CAPITAL MA ) , Michael Zaroogian (STATE FARM MUTUAL AU ) , Terence Lynch (GAINSCO SERVICE CORP ) , Rebekah Holt (STATE FARM MUTUAL AU ) , Katie Hubbard (STATE FARM MUTUAL AU ) , Leigh Ann Rogalski (STATE FARM MUTUAL AU ) , Chad Moser (STATE FARM MUTUAL AU ) , Tim Zelgert (STATE FARM MUTUAL AU ) , Ray Renken (STATE FARM MUTUAL AU ) , Kara Olson (STATE FARM MUTUAL AU ) , Jim Chan (BLACKROCK INSTITUTIO ) , Matt Harvey (STATE FARM MUTUAL AU ) , Steve Brucker (STATE FARM MUTUAL AU ) , John Socha (STATE FARM MUTUAL AU ) , Jennifer Hsui (BLACKROCK INSTITUTIO ) , Joe Young (STATE FARM MUTUAL AU ) , Wade Reinthaler (STATE FARM MUTUAL AU ) , Scott Reid (STATE FARM MUTUAL AU ) , Adam Hallman (STATE FARM MUTUAL AU ) , Tyler Smith (STATE FARM MUTUAL AU ) , Wei Hao (STATE FARM MUTUAL AU ) , Chris Minter (STATE FARM MUTUAL AU ) , Shelly Marsh (STATE FARM MUTUAL AU ) , Hollie Marsh (STATE FARM MUTUAL AU ) , Matthew Lockridge (WESTWOOD MANAGEMENT ) , Rich Rebholz (STATE FARM MUTUAL AU ) , Michael Mayberger (STATE FARM MUTUAL AU ) , Ashley Smock (STATE FARM MUTUAL AU ) , Brian Bengtson (STATE FARM MUTUAL AU ) , Cory Swartzlander (STATE FARM MUTUAL AU ) , Scott Lawson (WESTWOOD MANAGEMENT ) , Ayman Bari (STATE FARM MUTUAL AU ) , Adam Vales (STATE FARM MUTUAL AU ) , Robert Middleton (STATE FARM MUTUAL AU ) , Shane Jent (STATE FARM MUTUAL AU ) , Kevin Rock (STATE FARM MUTUAL AU ) , Mark Dunford (STATE FARM MUTUAL AU ) , Jean-Francois Ducrest (DUCREST, JEAN-FRANCO ) , Caroline Dirks (STATE FARM MUTUAL AU ) , Kyle Gilmore (STATE FARM MUTUAL AU ) , Diane Hsiung (GEODE CAPITAL MANAGE ) , Hunter Rose (STATE FARM MUTUAL AU ) , Cameron Kurak (STATE FARM MUTUAL AU ) , Mark Broughton (FIRST REPUBLIC BANK ) , Betsey Euliss (STATE FARM MUTUAL AU ) , Kim Bretz (STATE FARM MUTUAL AU ) , Jon Wilson (STATE FARM MUTUAL AU ) , Numan Ahmed (STATE FARM MUTUAL AU ) , Walter Ruane (STATE FARM MUTUAL AU ) , Shawna Barlow (STATE FARM MUTUAL AU ) , Philip Kroger (STATE FARM MUTUAL AU ) , Gabrielle Poole (STATE FARM MUTUAL AU ) , Ricardo Correa (STATE FARM MUTUAL AU ) , Felipe Castella (STATE FARM MUTUAL AU ) , Matt Krebsbach (STATE FARM MUTUAL AU ) , Gabriel Prado Correa (STATE FARM MUTUAL AU ) , Larnita Gates (STATE FARM MUTUAL AU ) , Ketrick Karsten (STATE FARM MUTUAL AU ) , Sophie Kim (STATE FARM MUTUAL AU ) , Vicki Trimpe (STATE FARM MUTUAL AU ) , Christin Higham (STATE FARM MUTUAL AU ) , BD DINCER (COLUMBIA UNIVERSITY ) , b.dincer@columbia.edu Cc: Kerri Saperstein (MORGAN STANLEY & CO. ) , newyork@sec.gov, chair@sec.gov, colin.brooks@morgan.stanley.com Subject: Fwd:STATE FARM - BLOOMINGTON krock5@bloomberg.net (w) Bloomington IL 61701, US See also: TCRReport... Thanks! From: BD DINCER (COLUMBIA UNIVERSITY) At: 12/18/21 16:13:57 UTC-5:00 To: Greg Shull (STATE FARM MUTUAL AU ) , Bill Trauner (STATE FARM MUTUAL AU ) , Theresa Baker (STATE FARM MUTUAL AU ) , Tammy Gipson (STATE FARM MUTUAL AU ) , Leigh Ann Rogalski (STATE FARM MUTUAL AU ) , Chad Moser (STATE FARM MUTUAL AU ) , Ray Renken (STATE FARM MUTUAL AU ) , Matt Harvey (STATE FARM MUTUAL AU ) , Steve Brucker (STATE FARM MUTUAL AU ) , Wade Reinthaler (STATE FARM MUTUAL AU ) , Tyler Smith (STATE FARM MUTUAL AU ) , Rich Rebholz (STATE FARM MUTUAL AU ) , Brian Bengtson (STATE FARM MUTUAL AU ) , Kyle Gilmore (STATE FARM MUTUAL AU ) , Numan Ahmed (STATE FARM MUTUAL AU ) , Walter Ruane (STATE FARM MUTUAL AU ) , Vicki Trimpe (STATE FARM MUTUAL AU ) , Brent Reeder (NORTHERN TRUST COMPA ) , Steven Santiccioli (NORTHERN TRUST COMPA ) , sjs5@ntrs.com, rebecca.coyle@statefarm.com, nicole.bowyer@statefarm.com, phil.supple.hid9@statefarm.com, dick.luedke.h2hj@statefarm.com, brian.hodgson.nyz6@statefarm.com Cc: Christin Higham (STATE FARM MUTUAL AU ) , Sophie Kim (STATE FARM MUTUAL AU ) , Ketrick Karsten (STATE FARM MUTUAL AU ) , Larnita Gates (STATE FARM MUTUAL AU ) , Gabriel Prado Correa (STATE FARM MUTUAL AU ) , Matt Krebsbach (STATE FARM MUTUAL AU ) , Felipe Castella (STATE FARM MUTUAL AU ) , Susan Byrne (WESTWOOD MANAGEMENT ) , Julie Hoyer (STATE FARM MUTUAL AU ) , Jeffrey Attwood (STATE FARM MUTUAL AU ) , John Malito (STATE FARM MUTUAL AU ) , Robert Stephan (STATE FARM MUTUAL AU ) , Lisa Rogers (STATE FARM MUTUAL AU ) , Elena Khoziaeva (BRIDGEWAY CAPITAL MA ) , Heather Caldwell (STATE FARM MUTUAL AU ) , Michael Whipple (BRIDGEWAY CAPITAL MA ) , Michael Zaroogian (STATE FARM MUTUAL AU ) , Terence Lynch (GAINSCO SERVICE CORP ) , Rebekah Holt (STATE FARM MUTUAL AU ) , Katie Hubbard (STATE FARM MUTUAL AU ) , Tim Zelgert (STATE FARM MUTUAL AU ) , Kara Olson (STATE FARM MUTUAL AU ) , Jim Chan (BLACKROCK INSTITUTIO ) , John Socha (STATE FARM MUTUAL AU ) , Jennifer Hsui (BLACKROCK INSTITUTIO ) , Joe Young (STATE FARM MUTUAL AU ) , Scott Reid (STATE FARM MUTUAL AU ) , Adam Hallman (STATE FARM MUTUAL AU ) , Wei Hao (STATE FARM MUTUAL AU ) , Chris Minter (STATE FARM MUTUAL AU ) , Shelly Marsh (STATE FARM MUTUAL AU ) , Hollie Marsh (STATE FARM MUTUAL AU ) , Matthew Lockridge (WESTWOOD MANAGEMENT ) , Michael Mayberger (STATE FARM MUTUAL AU ) , Ashley Smock (STATE FARM MUTUAL AU ) , Cory Swartzlander (STATE FARM MUTUAL AU ) , Scott Lawson (WESTWOOD MANAGEMENT ) , Ayman Bari (STATE FARM MUTUAL AU ) , Adam Vales (STATE FARM MUTUAL AU ) , Robert Middleton (STATE FARM MUTUAL AU ) , Shane Jent (STATE FARM MUTUAL AU ) , Kevin Rock (STATE FARM MUTUAL AU ) , Mark Dunford (STATE FARM MUTUAL AU ) , Jean-Francois Ducrest (DUCREST, JEAN-FRANCO ) , Caroline Dirks (STATE FARM MUTUAL AU ) , Diane Hsiung (GEODE CAPITAL MANAGE ) , Hunter Rose (STATE FARM MUTUAL AU ) , Cameron Kurak (STATE FARM MUTUAL AU ) , Mark Broughton (FIRST REPUBLIC BANK ) , Betsey Euliss (STATE FARM MUTUAL AU ) , Kim Bretz (STATE FARM MUTUAL AU ) , Jon Wilson (STATE FARM MUTUAL AU ) , Shawna Barlow (STATE FARM MUTUAL AU ) , Philip Kroger (STATE FARM MUTUAL AU ) , Gabrielle Poole (STATE FARM MUTUAL AU ) , Ricardo Correa (STATE FARM MUTUAL AU ) , BO.DINCER@YAHOO.COM, bd2561@columbia.edu Subject: STATE FARM - BLOOMINGTON TY. Kevin Rock Investment Information Analyst State Farm Mutual Automobile Ins Co +1-309-735-2705 (o) 1 State Farm Plz +1-309-530-1865 (m) Investment Department E-8 krock5@bloomberg.net (w) Bloomington IL 61701, US Phil Supple 1 Views Today Spokesperson Career State Farm Life Insurance Co Current +1-800-782-8332 (o) 1 State Farm Plaza State Farm Life Insurance Co phil.supple.hid9@statefarm.com (w Bloomington IL 61710, US Spokesperson Nicole Tamilyn Bowyer Attorney State Farm Insurance +1-504-840-4900 (o) 853 Fincastle Turnpike +1-504-840-4941 (f) North Tazewell VA 24630 nicole.bowyer@statefarm.com (w) Focus Legal Rebecca Coyle 1 Views Today Analyst:Public Policy Career State Farm Life Insurance Co Current +1-309-766-2311 (o) 1900 M Street NW State Farm Life Insurance Co rebecca.coyle@statefarm.com (w) Washington DC 20036, US Analyst:Public Policy 2012-Present Steven Santiccioli VP:Quantitative Management Northern Trust Company, The +1-3124444419 (o) Addl Contact Info » 312-444-5777 (o) 181 W Madison St steve@bloomberg.net (w) Chicago IL 60602-4510, sjs5@ntrs.com (w) I would work harder on my marriage if there was a retirement plan. Focus Large Cap Stocks, Growth Investing, Global, Equities, Thematic Investing, United States, Developed Markets Funds Managed (7 Funds/7.7B Total Assets in USD) | More » Fund Name Tot Ast YTD Ret 3M Px Objective Status 21) Northern International Equity In 5.5B 7.8 Foreign Blend ACTV 22) Northern Global Sustainability In 1.3B 20.5 Thematic Sector ACTV 23) Green Century Equity Fund 552.1M 25.2 Thematic Sector ACTV Recent News | More » 41) Northern Funds: 497 2019/07/02 EDG 07/2019 |

<< HAPPY HOLIDAYS and Merry xmas >>

------------------------------------------------------------------------

*** 2021-2022 ANNUAL FILINGhttps://www.sec.gov/Archives/edgar/data/0000093715/000114554922006149/xslFormN-CEN_X01/primary_doc.xml

... WITHOUT BEING REGISTERED IN THE STATE OF NEW YORK TO CONDUCT ANY FORM OF INVESTMENT BANKING, THE DIRECTOR OF STATE FARM INSURANCE LLC AS THE MANAGING MEMBER OF STATE FARM MORTGAGE LLC - IS ALSO NOW HOLDING A NOTE "NOT COVERS" AS A FIDUCIARY WHICH HOLDS THE TAX LIABILITY, AND AVOIDANCE TO PROSECUTION WHEREBY THE PREMIUMS AND INSURANCE COLLECTED ON A LETTER OF CREDIT... HOWEVER "INDEMNIFIED...BY "SULLIVAN PROPERTIES LP" WHO HAS ASSURED IN WRITING THAT THEY WILL REIMBURSE "STATE FARM" IN THE EVENT OF A DEFAULT, OR LATE PAYMENT. ANNEXED IN NYSCEF 153974/2020

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=IY8iDH_PLUS_UpVanEtcRioef3A==

+++ I SENT THIS TO THE SUPREME COURT JUSTICES INDEPENDENTLY IN NOVEMBER AS WELL, BTW.

NOTICE TO STATE FARM:https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=n_PLUS_CvSQR36fqPKko6L47FFQ==

THE FAILED TO DISCLOSE TO NOT GET FINED IN TEXAS? THEY ALSO FAILED DISCLOSE IT FOR THE NEW INVESTORS OF THE TICKERS BELOW AFTER LOSING THE UPPER BOUND OF $940,000,000.00 WITH RESPECT TO BRK-B IS NOT A JOB WELL DONE, IN-DEED. TO PROTECT TAX EVASION AND THE FINES, PENALTIES AND CERTAIN PRISON TIME... WHILE COLLECTING PREMIUMS AND INTEREST FOR THE PROPERTIES WHICH ARE GOING TO NEED DENTURES ("FINANCIALLY") UPON REALIZING THEY "STATE FARM" IS LIABLE FOR 5 OTHERS UNDER 26 CFR § 1.6662

  * ACCOUNTED FOR, AND BY YOURS TRULY - WAS ANNEXED IN THE MATTER OF
    153974/2020 WHICH ANY GENERAL COUNSELOR OF LAW WOULD UNDERSTAND IN
    THEIR FIDUCIARY ROLES, NOTWITHSTANDING AN INVESTMENT PROFESSIONAL.
    P.S. #GOCARDS...

Instructions.

 1.

    Item G.1.a.i. Legal proceedings. (a) If the Registrant responded
    "YES" to Item B.11.a., provide a brief description of the
    proceedings. -- As part of the description, provide the case or
    docket number (if any), and the full names of the principal parties
    to the proceeding. (b) If the Registrant responded "YES" to Item
    B.11.b., identify the proceeding and give its date of termination.

 2.

    Item G.1.a.ii. Provision of financial support. If the Registrant
    responded "YES" to Item B.14., provide the following information
    (unless the Registrant is a Money Market Fund): (a) Description of
    nature of support. (b) Person providing support. (c) Brief
    description of relationship between the person providing support and
    the Registrant. (d) Date support provided. (e) Amount of support.
    (f) Security supported (if applicable). Disclose the full name of
    the issuer, the title of the issue (including coupon or yield, if
    applicable) and at least two identifiers, if available (e.g., CIK,
    CUSIP, ISIN, LEI). (g) Value of security supported on date support
    was initiated (if applicable). (h) Brief description of reason for
    support. (i) Term of support. (j) Brief description of any
    contractual restrictions relating to support.

 3.

    Item G.1.a.iii.

Independent public accountant's report on internal control (management investment companies other than small business investment companies only). Each management investment company shall furnish a report of its independent public accountant on the company's system of internal accounting controls. The accountant's report shall be based on the review, study and evaluation of the accounting system, internal accounting controls, and procedures for safeguarding securities made during the audit of the financial statements for the reporting period. The report should disclose any material weaknesses in: (a) the accounting system; (b) system of internal accounting control; or (c) procedures for safeguarding securities which exist as of the end of the Registrant's fiscal year. The accountant's report shall be furnished as an exhibit to the form and shall: (1) be addressed to the Registrant's shareholders and board of directors; (2) be dated; (3) be signed manually; and (4) indicate the city and state where issued. Attachments that include a report that discloses a material weakness should include an indication by the Registrant of any corrective action taken or proposed. The fact that an accountant's report is attached to this form shall not be regarded as acknowledging any review of this form by the independent public accountant. 4. Item G.1.a.iv. Change in accounting principles and practices. If the Registrant responded "YES" to Item B.21, provide an attachment that describes the change in accounting principles or practices, or the change in the method of applying any such accounting principles or practices. State the date of the change and the reasons therefor. A letter from the Registrant's independent accountants, approving or otherwise commenting on the change, shall accompany the description. 5. Item G.1.a.v. Information required to be filed pursuant to exemptive orders. File as an attachment any information required to be reported on Form N-CEN or any predecessor form to Form N-CEN (e.g., Form N-SAR) pursuant to exemptive orders issued by the Commission and relied on by the Registrant. 6. Item G.1.a.vi. Other information required to be included as an attachment pursuant to Commission rules and regulations. File as an attachment any other information required to be included as an attachment pursuant to Commission rules and regulations. Pursuant to the requirements of the Investment Company Act of 1940, the Registrant has duly caused this report to be signed on its behalf by the undersigned hereunto duly authorized.

Instructions to Item C.16 and Item C.17.

https://www.sec.gov/Archives/edgar/data/0000093715/000114554922006149/xslFormN-CEN_X01/primary_doc.xml

https://www.sec.gov/Archives/edgar/data/0000093715/000119312521278180/d222043dn8f.htm

------------------------------------------------------------------------

ATTACHED DEED AND NYC DEPT OF FINANCE TAX RECORDS FOR THE 10-YEARS PRIOR.
LOAN DOCKET 50074 - NYSCEF MATTER 153974/2020 LETTER OF CREDIT FOR $6,000,000.00 SECURED BY UNLAWFUL LEASES AND RENTS. USC 18.21, 18.225, 18.215, 18.4, 18.3, 18.229B ++ Tax records & unlawful income. [ LOAN 50074 EST++ ] FILED AND KNOWN AS REFERENCED IN THE SEQUENCE OF EXHIBITS FILED IN THE MATTER OF NYSCEF 153974/2020https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=19MVPFXy0G0QvnmRLGpYIQ==

STATE FARM (ADDRESSED IN THE STATE OF ILLINOIS) ISSUED THIS TO THE BENEFIT OF THE FOLLOWING CORPORATIONS AND UNDER THE AUSPICE OF THEIR DIRECTORS, AS FOLLOWS:

|A. SULLIVAN PROPERTIES LP. B. SULLIVAN GP LLC. C. MANHATTAN SKYLINE MANAGEMENT CORP. D. THE ZUCKER ORGANIZATION. |

NOTARIZED BY DONALD ZUCKER ON MAY 13TH, 2020 THEN FILED WITH THE NYC DEPT. OF FINANCE REGISTER.

USC 26 NOTE.

AS REFERENCED ABOVE, WAS FILED WITH THE NY FINANCE REGISTER AND IN NEW YORK SUPREME COURT CIVIL PART, PRIOR TO THE SEMI-ANNUAL REPORT WAS FILED BY STATE FARM UNDER PAUL SMITH AND TERRANCE LUDWIG [ IN HIS 40-17G FILINGS ] NEGLECTED OVER SEVERAL REPORTING PERIODS TO INCLUDE THE MATERIAL SUBSTANCE AND EXPOSURES AS IMPLIED BY THE RISKS OF THE OUTCOME OF NYSCEF MATTER 153974/2020 - WHICH NEVER WAS QUASHED OR FORGIVEN, OR WAIVED TO ANY EFFECT.

THE PROCEEDINGS WERE OBSTRUCTED BY THE CORPORATIONS, THEIR DIRECTORS, AND ATTORNEYS AS SEEN IN THOSE PROCEEDINGS WERE AWARE OF ALL CONFIRMATIONS FILED, NOTWITHSTANDING THE NOTARY SERVICES OF MISS ASHLEY HUMPHRIES WHO ALSO PARTICIPATED IN THE CASE.

ALSO ANNEXED AND FILED THEIR DISTRIBUTION OF PRIVATE VIDEOS AND PHOTOGRAPHS FROM THE INTERIOR OF MY APARTMENT - TAKEN WITHOUT MY CONSENT.

THESE VIDEOS WERE ADULTERED, PHOTO-SHOPPED, HOSTED, AND ALSO CONVERTED AND EMAILED INTO *.MOV FILES AS SEEN IN THE DOCKETS ENTERED AND ADMITTED BY THEIR COUNSELORS, WERE AWARE AND WILLFULLY CONTINUED TO OBSTRUCT JUSTICE IN ORDER TO AVOID ANY DELUGE OF INFORMATION BY STATE FARM AND TO UNLAWFULLY SECURE A LOAN FOR $6,000,000.00 WAS DISTRIBUTED BY AND BETWEEN THOSE MEMBERS BELOW (IN SALARIES, WAGES, AND FOR WHATEVER PURPOSES THEY WOULD OTHERWISE USE THOSE FUNDS) WERE PRESENTED TO THE CLERK AND JUDGE ALONG WITH MY REQUESTS FOR THEM TO CEASE AND DESIST FROM ANY FURTHERANCE AND TO STOP FILMING AND PHOTOGRAPHING THE INTERIOR OF APARTMENT - FELT THAT IT WOULD BE ENTERTAINING TO CONTINUE TO HARASS BOTH MY TIME - AS WELL AS THE STATE'S RESOURCES DURING THE HEIGHT OF THE COVID-19 PANDEMIC. THE TAX RECEIPTS WERE ALSO FILED AND DISTRIBUTED TO ALL MATERIAL PARTIES UPON DISCOVERY, AS FOLLOWS [A SHORT LIST OF 10 INDIVIDUALS, WITHOUT HAVING TO NAME ALL OF STATE FARM'S ENTITIES]:

|1. MR. DONALD ZUCKER. 2. MS. LAURIE ZUCKER. |

THE ATTORNEYS IN NYSCEF 153974/2020 - FOR CONFIRMATION CONTINUED IN THEIR AFFAIR OVER A PERIOD OF SEVERAL MONTHS, BEGINNING FIRST ON JUNE 5TH, 2020 - BEGAN FILING ARBITRARY CLAIMS WITHOUT ANY DEMAND FOR MONEY, OR A CLAIM UPON WHICH ANY MERIT FOR AWARD EXISTS, ABSENT OF THOSE WHICH I DEMANDED FROM THE COURTS AND ALSO FILED UPON MY ADVERSARIES IN THE MATTER - HAVE NOT RETURNED AN EMAIL, PHONE CALL, OR THE UNLAWFUL RENTS WHICH THEY COLLECTED - WERE USED AS AN ARTIFACT OF "CREDIBILITY" TO OBTAIN A LOAN FROM STATE FARM.

|3. MS. SHARI LASKOWITZ. 4. MR. PAUL REGAN. 5. MR. CORY WEISS. 6. MS. ASHLEY HUMPHRIES. 7. MR. JOSEPH GIAMBOI. >> LETTER OF OBSTRUCTION [ DOCKET 399 ] >> CAUSED - IN PART - A BREACH OF THE SARBANES-OXLEY AND THE OMISSIONS AS EXPRESSED BELOW. >> FAILURE TO DISCLOSE BY PRICE WATERHOUSE COOPERS IN TWO SEMI-ANNUAL REPORTS. >> BOTH FILED WITH THE SECURITIES & EXCHANGE COMMISSION UNDER CIK FILER 93715 AND 1516523. >> FAILURE TO DISCLOSE BY PRICE WATERHOUSE COOPERS IN TWO ANNUAL REPORTS.  >> BOTH FILED WITH THE SECURITIES & EXCHANGE COMMISSION UNDER CIK FILER 93715 AND 1516523. |

STATE FARM

THEIR DIRECTORS.

|8. MR. TERRENCE LUDWIG. >> FAILS TO DISCLOSE ANY MATERIAL LEGAL ACTIONS, CLAIMS. >> NOT COVERED FOR LOSSES AS A RESULT OF OMISSIONS.  >>>> CERTIFIED UNDER CERT-99 AND A BREACH UNDER 63.18 OF THE SARBANES-OXLEY (FILED WITH THE SECURITIES AND EXCHANGE COMMISSION) IN SEVERAL REPORTING PERIODS. >>>> ASSERTED THE SAME AND IN FISCAL REPORTING PERIODS 2020, 2021, AND 2022 UNDER CIK FILER 93715 AND 1516523. 9. MR. JOE MONK, JR. 10. MR. PAUL SMITH. |

LOAN 50074 EST++https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=19MVPFXy0G0QvnmRLGpYIQ==

RE: JP MORGAN CHASE RE: MORGAN STANLEY & CO (USED TWO CRD INDICATORS UNDER CIK FILER 93715 AND 1516523)

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=R9aac7D6DBJZ1wsiq0b38A==

  * Unlawful custody and deposits AT A US BANK - is unlawful, per the
    FDIC. this was also obstructed by the assisted services at the
    towers of EARL.

Does this make sense, Miss Hochul

  *

    for a C5 edifice in ZIP CODE 10012 in the following tax periods for
    the 20 units at 111 SULLIVAN STREET, NEW YORK, NY, 10012?

  *

    ALL SIX PROPERTIES CONTAIN A FULL OR PARTIAL ABSENCE OF A
    CERTIFICATE OF OCCUPANCY, OR INSPECTION AT ALL RELEVANT TIMES.

DOCKET 386https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=IY8iDH_PLUS_UpVanEtcRioef3A==

tax receipts ATTACHED. BRB. #GOCARDS. P.S. PULL29 ATTACHED COMPOUND. WAS RE-DIRECTED PROPERLY BY THE PRECINCTS LATER BY THIS OTHER OFFICER NANCY... I FORGOT WHO I SPOKE WITH. I THINK WITH WAS NANCY, DEFINITELY NANCY...

-------- Forwarded Message -------- Subject: Tax records & unlawful income USC 18.21, 18.225 Date: Fri, 24 Jun 2022 21:54:47 +0000 (UTC) From:6462563609@mms.att.netTo:bdincer66@icloud.com,kaaperstein2@bloomberg.net,josephine.vella@finra.org,ms60710444266@yahoo.com,chair@sec.gov,chicago@sec.gov,bbrief@bloomberg.net,tips@latimes.com,pronewsletter@dowjones.com,praghuram2@bloomberg.net,blawre@bloomberg.net,mediainquiries@point72.com,mshy15@morganstanley.com,jpminvestorrelations@jpmchase.com,tips@vibe.com,tips@nytimes.com,mutualfunds@statefarm.com,bofamarkets@bofa.com

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=R9aac7D6DBJZ1wsiq0b38A==^^ unlawful custody of SECURITY

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=19MVPFXy0G0QvnmRLGpYIQ==

tax receipts (#GOCARDS)

---
## [sudocanttype/youtube-playlist-shuffler](https://github.com/sudocanttype/youtube-playlist-shuffler)@[a3b3dd5e7f...](https://github.com/sudocanttype/youtube-playlist-shuffler/commit/a3b3dd5e7f8beb6b76f4b9ed072a9af8ae77f952)
#### Sunday 2022-06-26 17:16:13 by sudocanttype

Merge pull request #1 from sudocanttype/express-back-impl-FUCK-YOUTUBE

rework backend to use express rather than electron

---
## [sudocanttype/youtube-playlist-shuffler](https://github.com/sudocanttype/youtube-playlist-shuffler)@[84161ecbad...](https://github.com/sudocanttype/youtube-playlist-shuffler/commit/84161ecbada496f608c157f135b252103592b759)
#### Sunday 2022-06-26 17:17:36 by sudocanttype

Merge pull request #2 from sudocanttype/express-back-impl-FUCK-YOUTUBE

remove some boilerplate files

---
## [newstools/2022-express](https://github.com/newstools/2022-express)@[cb98289aa4...](https://github.com/newstools/2022-express/commit/cb98289aa4ad9167440f4572b24fec28078a7dab)
#### Sunday 2022-06-26 17:30:26 by Billy Einkamerer

Created Text For URL [www.express.co.uk/life-style/garden/1631223/ideal-time-of-day-to-water-houseplants-summer-morning-evening-gardening-tips-hacks]

---
## [WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER)@[f6079e6fdb...](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/commit/f6079e6fdb03b5fd0fd579f2ee926f9f2ffc9bc5)
#### Sunday 2022-06-26 17:32:39 by WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER

TAKEN FROM INSIDE OF MY CLOSET --- I CAN SEE THE HOLE OF THE CAMERA..JPG

https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/pull/5


VIOLATION OF PRIVACY.
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=fXMaXgeyzvA85ViWMmvfAQ==

or tax evasion.. whichever gets the ZUCKERS and their accomplice more time in Prison.
-- the money... a seperate matter.

https://github.com/BSCPGROUPHOLDINGSLLC/WILSONELSER-ZUCKER/issues/16


-------- Forwarded Message --------
Subject: 	--- FAXED THEIR TAX EVASION PAPERS AND INCLUDED THESE VIOLATION OF PRIVACY DOCUMENTS.
Date: 	Tue, 24 May 2022 02:09:41 -0500
From: 	B D2022 <ms60710444266@yahoo.com>
To: 	Alisa Maksimova [FRB-NY] <Alisa.Maksimova@ny.frb.org>, Solis, Anita <anita.solis@chi.frb.org>, Cynthia.H.Francis@frb.gov, dallas-reserve-mgmt@dal.frb.org <dallas-reserve-mgmt@dal.frb.org>, Mielke, Evan P <evan.p.mielke@chi.frb.org>, general.info@ny.frb.com <general.info@ny.frb.com>, general.info@ny.frb.org <general.info@ny.frb.org>, kenneth.j.fraser@frb.gov, media@chi.frb.org <media@chi.frb.org>, ny.public.information@ny.frb.org, ny.reserves@ny.frb.org <ny.reserves@ny.frb.com>, ny.reserves@ny.frb.org <ny.reserves@ny.frb.org>, nyreporting.forms@ny.frb.org <nyreporting.forms@ny.frb.org>, oighotline@frb.gov <oighotline@frb.gov>, reserves@chi.frb.org <reserves@chi.frb.org>, info@bressler.com <info@bressler.com>, JPMCinvestorrelations@jpmchase.com <JPMCinvestorrelations@jpmchase.com>, ir@expedia.com, hotel.plazanewyorktimessquare@riu.com, Hilton Hotels & Resorts <hiltonhonors@hilton.com>, jagosto@triumphhotels.com, newyork@cravath.com <newyork@cravath.com>, emil.herzog@goodnewsjail.org, Dow Jones <wsjprosupport@dowjones.com>, Jennifer.Levitz@wsj.com, Tennesse <sbarchenger@tennessean.com>
CC: 	odonned@assembly.state.ny.us <odonned@assembly.state.ny.us>, assessments@fdic.gov <assessments@fdic.gov>


Monday, March 7: Day 10
A Nashville jury awarded Andrews $55 million. Jurors found Barrett 51 percent at fault in the case, which would mean he would have to pay $51 percent of the award. The jury said Windsor Capital Group and the hotel owner, West End Hotel Partners, also were at fault
and were on the hook for the remaining 49 percent.

Friday, March 4: Day 9
Attorneys hashed out jury instructions and delivered their closing arguments. Andrews' attorneys said Barrett was a liar who the jury should not believe. Barrett testified via video deposition - after he was forced to do so by a judge - that he got Andrews' room number using an administrative phone at the hotel.

Defense attorneys want the jury to believe that story. They say Barrett was an insurance executive who traveled more than 200 nights a year and thus knew how to deceive the system to get access to Andrews.

But Andrews' attorney, Bruce Broillet, said Barrett was not believable because of documents that show he requested a room next door, and say that even if he used a staffonly phone, the hotel is still liable because it should not have given him access.
Barrett has already been deemed liable to some extent. But the jury will weigh additional questions: Is Windsor Capitol Group at fault? Was Windsor an agent of West End Hotel Partners?

(A "yes" answer to this question would mean West End Hotel Partners could have to pay damages). What portion of the fault are each Barrett and Windsor responsible for? How much should be awarded in total damages?
Thursday, March 3: Day 8

The defense rested its case about 1:30 p.m., and Andrews' lawyers did not put on what are called rebuttal (or extra) witnesses.

The defense's last witness was former NFL player Jesse Palmer, who worked on ESPN's Thursday night college football crew with Andrews in 2008 and 2009. He said he was amazed at Andrews' on-air performance at her first game back after the videos were leaked,
calling her a professional. He also said she was subject to sexual comments before the videos were leaked, and said she had additional security after the incident. Jacqueline Dement, who checked Barrett into the Nashville hotel the day he recorded the video, said she would not have seen his request to room next to Andrews. If she had seen the request, Dement said she would have followed procedure to first check with Andrews. (Andrews testified previously that never happened.)

Dement was speaking generally, however, and said she did not specifically remember checking Barrett into the hotel.
Wednesday, March 2: Day 7

Stephen Barth, a professor at the University of Houston's Conrad N. Hilton hospitality management college, testified for the defense that based on his review of the case, hotel staff did not violate procedures in place in 2008. He suggested Andrews’ lawyers were asking the jury to make assumptions about what actions hotel staff might have taken to let Barrett book the room next door to the television broadcaster. Erin Andrews' stalker a terrorist, expert says Herman Turk, a vice president for Windsor, oversaw the hotel in 2008. He said he had full confidence that the staff followed rules and procedures, and said it was very unlikely front desk staff would have seen Barrett’s request to room next to Andrews that was taken at a reservation center.

He said the local hotel excelled in a secret inspection performed by Marriott three months before Barrett checked in. Kimberly Brown, a psychologist at Vanderbilt University, said she evaluated Andrews three times, diagnosing her with mild post-traumatic stress disorder. She said she believed
Andrews’ symptoms would disappear with treatment.

Tuesday, March 1: Day 6
Andrews' lawyers closed their case after the television broadcaster's testimony. Andrews started the day on the witness stand to continue her direct testimony, but soon faced crossexamination by Marc Dedman, an attorney for the hotel operator. Dedman suggested in his
questioning that the nude videos had helped Andrews' career more than hurt it. He asked Andrews to confirm numerous commercials and other endorsements she's made since the videos.

As an early witness in the defense case, Patrick Donaher testified via his video deposition that Andrews seemed nervous when she covered her first football game after the videos
were released, but that she was still well liked and respected. Donaher was a talent coach who critiqued Andrews' on-the-job performance.

Lewis Kay, Andrews' publicist and manager, testified via video deposition and said that the stalking case did influence Andrews' decisions on what jobs to take on. He noted she was very successful and said one goal of his was to expand her audience beyond sports.


Monday, Feb. 29: Day 5 Andrews took the stand and in tearful testimony described how she got bombarded by media coverage after the videos went viral, and how she feared for her safety before her stalker was arrested. She said people bring up the videos or jeer at her each time she covers
a game. The 37-year-old said hotel staff never notified her a man was trying to stay next door. If she had known, she said, she would have called police. Andrews said she knew filing her civil lawsuit would revive media coverage, which she blamed for part of her humiliation, but said she had to stand up for herself and others. In emotional plea, Erin Andrews blames hotel Andrews' mother, Paula Andrews, sobbed during her daughter's testimony and rested her head on her husband Steve's shoulder. Paula Andrews said her daughter was driven to succeed despite her fear the videos would end her career.

"I almost think she’s trying to compensate and keep in control that aspect of her life," Paula


Barrett testified via video deposition earlier Monday. He said he filmed about 10 women through hotel peepholes, but targeted Andrews because she was popular online and he wanted to sell the videos of her for money. He said he called to confirm Andrews was staying at the hotel by making it seem it was his own reservation. In a hotel restaurant he used a house phone and asked to be transferred to her room. The hotel phone showed her room number, he said.

Thursday, Feb. 25: Day 4
The jury watched two videos of Andrews taken by her stalker: 4½ minutes of footage from the Nashville Marriott and a six-second clip shot in an Ohio hotel. One woman on the jury occasionally looked away from the videos. A tearful Andrews left the courtroom while the videos played. Bernard "Jim" Jansen, a computer scientist and professor at Penn State, was hired by Andrews' team. He said he searched the Web and determined the videos or still images of Andrews nude had been seen by more than 16.8 million people between July 2009 and January 2016.

Expert says 16.8 million saw Erin Andrews nude  Andrews’ psychotherapist, Loren Comstock, testified that repeated media coverage of what has been dubbed by some as the “peephole case” has bred anxiety in Andrews.

Comstock’s testimony was via video of her deposition taken in May 2015. She said Andrews became obsessed with checking media coverage each morning and feared she would be known for the nude video and not her work as a sports broadcaster. “She couldn’t get through the day without fear and anxiety,” Comstock said, adding that Andrews was still functioning and doing her job.



THANK YOU FOR THE PROMPT DELIVERY OF THE ACRIS REPORTS I REQUESTED YOU P.O.S.

 

- I STILL NEED TO FIND OUT IF THEY FOLLOWED ME TO LAS VEGAS AS WELL IF YOU CAN LOOK INTO THAT.


THESE ARE THE DAMAGES WHICH HAVE BEEN OBSTRUCTED, BEYOND THE CHANGE IN VALUE FOR TICKERS STFGX, STFBC, SFITX, SFBDX


1. INVESTMENT ADVISOR = HAS CEASED TO EXIST = ZERO ASSETS UNDER MANAGEMENT.

2. THE NEW ADVISOR, HOLDS THE LIABILITY OF LEGAL RECOURSE AND HAS TO FACE ME IN COURT.

3. THE CONBINED INDENDURED SERVANTS OF THE ZUCKER CANNOT AFFORD THE PENALTIES, PRISON SENTENCES, AND MONIES WHICH ARE STILL OWED TO ME IN ARREARS.


         
    " STATE FARM AUTOMOBILE INSURANCE COMPANY "
    --- NOT LICENSED IN THE STATE OF NEW YORK TO CONDUCT INVESTMENT BANKING
    --- NOT LICENSED IN THE STATE OF NEW YORK TO CONDUCT SECURITIES TRANSACTIONS.


    __________________________________________________________________________________________
    

    Item B.14. Provision of financial support.

        Did an affiliated person, promoter, or principal underwriter of the
        Registrant, or an affiliated person of such a person, provide any
        form of financial support to the Registrant during the reporting period?

  2020
    https://www.sec.gov/Archives/edgar/data/0000093715/000114554921006167/xslFormN-CEN_X01/primary_doc.xml
    
  2021
    https://www.sec.gov/Archives/edgar/data/0000093715/000114554922006149/xslFormN-CEN_X01/primary_doc.xml
    
  2021-09-30
    https://www.sec.gov/Archives/edgar/data/0001516523/000114554921074536/xslFormN-CEN_X01/primary_doc.xml
    
    Report of Independent Registered Public Accounting Firm
    https://www.sec.gov/Archives/edgar/data/0001516523/000119312521347485/d221423dncsr.htm

  2022
    https://www.sec.gov/Archives/edgar/data/0001516523/000114554921074536/xslFormN-CEN_X01/primary_doc.xml
    2020: The Northern Trust Company
            Custody records, Administrative records, and Shareholder records.
             
    https://www.sec.gov/Archives/edgar/data/0001516523/000119312522025502/d207567d4017g.htm
    [40-17G]         ADVISERS INVESTMENT TRUST       
                    BOND PERIOD: January 1, 2022 to January 1, 2023
                    Bond Number: 70436972
                   
                        Chubb Group of Insurance Companies
                        202B Hall’s Mill Road
                        Whitehouse Station, NJ 08889\
                       
                            CRYSTAL IBC LLC
                            ATTN: Matthew Flynn 32
                            OLD SLIP - 29TH FL.
                            NEW YORK, NY 10005



https://www.sec.gov/comments/s7-14-18/s71418-4531826-176079.pdf

FOR THOSE WHO ARE INVOLED..

HERE IS THE HANDBOOK FOR AIDING & ABETTING AS WELL AS OBSTRUCTION OF JUSTICE WITH RESPECT TO TAX EVASION:

    https://www.irs.gov/pub/irs-utl/tax_crimes_handbook.pdf




Notice to Regulators.
    Tax Receipts— tax evasion
https://saaze2311prdsra.blob.core.windows.net/clean/0363e59f23d6ec11a7b5000d3a1afadb/BB-117taxFiles.pd

Insider Trading Dockets
    2022-04-12 EY - PWC - MSCO NOTICE 2
https://saaze2311prdsra.blob.core.windows.net/clean/b67c1a2d29d6ec11a7b5002248307b90/04.12.2022.151652.EY.PWC.MSCO-.pdf

VIOLATION OF PRIVACY CARRIES A FEW YEARS IN FEDERAL & STATE FACILITIES, BUT DON'T WORRY ABOUT THE FINANCIAL I'M DEALING WITH THEM.
- THANKS AGAINN FOR THE WAIVER.


February 20, 2022

Your fax (ID: #30666994) to IRS CRIMINAL INVESTIGATIONS at 267-466-1115

" has been delivered successfully at 11:44 PM Eastern Daylight Time"

https://faxzero.com/status/30666994/5790f17018611119e07814be9e36110d164afaa6


--- I ALSO FAXED THEIR TAX EVASION PAPERS WITH CERTIFICATE OF OCCUPANCY
---- THAT DID NOT AND DON'T EXIST, WHICH I ALREADY DID.


March 26th, 2022.

Your fax (ID: #30852826) to JOE MONK at 8164714832 has been delivered successfully at 4:42 AM Eastern Daylight Time on March 26th, 2022.

https://faxzero.com/status/30852826/92a1a0570d178d0311eb3764f01842d3ceb65513



https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=fXMaXgeyzvA85ViWMmvfAQ==

-- THE BURDEN OF THE TORTS, NOTWITHSTANDING THE "VIOLATION OF PROVACY" HAVE ALSO CARRIED-OVER TO THE NEW "HOLDERS" OF THE LEASES AND
    RENTS, AND UNDER THE NEW FILER 1516523 - WHERE OBSTRUCTION OF JUSTICE CONTINUES.

-- PER THE TERMS OF 255 AFFIDAVIT (LETTER OF CREDIT & LOAN) BETWEEN THE PARTIES ABOVE, THE CARRIED INTEREST OF TAX EVASION DOLLARS
 OVER TIME HAS BEEN AIDED AND ABETTED BY THE COUNSELORS AND ASSOCIATES OF THE ZUCKERS.
 

- Gross valuation misstatements, and the discovery of those interests could have been disclosed earlier.
-- DEMONSTRATES HOW THE SIX PROPERTIES AND INCOME IN THE ZIPCODE 10012 WERE NOT PROPERTLY ASSSESSED AND VALUED
-- have been further OBSTRUCTED by eggeregious and BY parties who will be adjudicated with at a later time, UPON DISCOVERY


-- I TOOK THE INITIATIVE TO REPORT THIS TO ALL MATERIAL PARTIES, AND UPON NOTICE HAVE FILED WITH THE RESPECTIVE REGULATORY AGENCIES.
NOTWITHSTANDING, THE IRS "CRIMINAL INVESTIGATIONS DEPARTMENT, AND ALSO TO THE NY SUPREME COURT

VIA FAX: 212-401-9146 AND ALSO ON THE 22ND OF DECEMBER, 2021 AT 7:27PM EST

February 20, 2022

Your fax (ID: #30666994) to IRS CRIMINAL INVESTIGATIONS at 267-466-1115

" has been delivered successfully at 11:44 PM Eastern Daylight Time"

https://faxzero.com/status/30666994/5790f17018611119e07814be9e36110d164afaa6


--- I ALSO FAXED THEIR TAX EVASION PAPERS WITH CERTIFICATE OF OCCUPANCY
---- THAT DID NOT AND DON'T EXIST, WHICH I ALREADY DID.


March 26th, 2022.

Your fax (ID: #30852826) to JOE MONK at 8164714832 has been delivered successfully at 4:42 AM Eastern Daylight Time on March 26th, 2022.

https://faxzero.com/status/30852826/92a1a0570d178d0311eb3764f01842d3ceb65513




https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/blob/WILSON-ELSER-DICKER-LLP/-%20-%20153974.2020%20---%2020201005%20-%20email%20from%20iPhone%204%20-%20facetime.pdf


            no certificate of occupancy
            2022 03 02
            https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/files/8608563/2022.03.02.-.Property.Profile.Overview.-.111.sullivan.street.REAR.-.NO.CERTIFICATE.OF.OCCUPANCE.pdf
           
       
            https://user-images.githubusercontent.com/70865813/166412249-b4f53181-4497-4e23-b1f7-7482261497e2.PNG

    ############################################################################

    Item B.14. Provision of financial support.

        Did an affiliated person, promoter, or principal underwriter of the
        Registrant, or an affiliated person of such a person, provide any
        form of financial support to the Registrant during the reporting period?

    ############################################################################       

                  
Illinois Official Reports Appellate Court Andrews v. Marriott International, Inc., 2016 IL App (1st) 122731 Appellate Court Caption ERIN ANDREWS, Plaintiff-Appellant, v. MARRIOTT INTERNATIONAL, INC., a Delaware Corporation; WEST END HOTEL PARTNERS, LLC, d/b/a Nashville Marriott at Vanderbilt University, a Delaware Limited Liability Company; WINDSOR CAPITAL GROUP, INC., a Colorado Corporation; RADISSON HOTELS INTERNATIONAL, INC., a Delaware Corporation; ASREL, INC., d/b/a Radisson Hotel Milwaukee Airport, a Wisconsin Corporation; THE OHIO STATE UNIVERSITY, d/b/a The Blackwell Inn; and MICHAEL DAVID BARRETT, an Individual, Defendants (Preferred Hotel Group, Inc., d/b/a Summit Hotels and Resorts, a Delaware Corporation, Defendant-Appellee). District & No. First District, Second Division Docket No. 1-12-2731 Rule 23 order filed Rule 23 order withdrawn Opinion filed August 23, 2016 September 1, 2016 September 6, 2016 Decision Under Review Appeal from the Circuit Court of Cook County, No. 10-L-8186; the Hon. Kathy Flanagan, Judge, presiding. Judgment Affirmed. Digitally signed by Reporter of Decisions Reason: I attest to the accuracy and integrity of this document Date: 2016.11.07 10:38:25 -06'00' - 2 - Counsel on Appeal Power Rogers & Smith, P.C., of Chicago (Sean M. Houlihan, of counsel), and Greene Broillet & Wheeler, of Santa Monica, California (Bruce A. Broillet, Scott H. Carr, Alan Van Gelder, and Tobin M. Lanzetta, of counsel), for appellant. Pretzel & Stouffer, Chtrd., of Chicago (Robert Marc Chemers and Scott L. Howie, of counsel), for appellee. Panel PRESIDING JUSTICE PIERCE delivered the judgment of the court, with opinion. Justices Neville and Hyman concurred in the judgment and opinion. OPINION ¶ 1 In 2008, while plaintiff, Erin Andrews, was a guest of The Blackwell Inn (Blackwell), she was secretly recorded on video in the privacy of her hotel room by another guest, Michael David Barrett. Plaintiff filed this action sounding in negligence and invasion of privacy against defendant, Preferred Hotel Group (Preferred),1 the service provider of Blackwell’s online reservation system, for, among other things, Blackwell’s disclosure of the details of her hotel stay to Barrett. Plaintiff’s theory of liability is that Preferred was either (1) engaged in a joint venture operation of the hotel or (2) voluntarily assumed a duty to protect plaintiff’s privacy. Preferred moved to dismiss the complaint pursuant to sections 2-615 and 2-619(a)(9) of the Code of Civil Procedure (Code) (735 ILCS 5/2-615, 2-619(a)(9) (West 2010)) arguing that it did not owe a duty to plaintiff and was not engaged in a joint venture to operate Blackwell. After two years of discovery, the circuit court granted Preferred’s section 2-619(a)(9) motion to dismiss. Plaintiff appeals from the dismissal, which we affirm for the following reasons. ¶ 2 BACKGROUND ¶ 3 Relevant to plaintiff’s claims against Preferred, the following facts are taken from the complaint. On February 4, 2008, Andrews was a guest at Blackwell located in Columbus, Ohio. Blackwell is owned and operated by Ohio State University (OSU). In the days leading up to her hotel stay, Illinois resident Michael David Barrett contacted Blackwell by phone to confirm that Andrews was staying at the hotel and asked to be assigned the room next door to her. Blackwell granted Barrett’s requests. After checking into the hotel on February 4, Barrett retrofitted the peephole on Andrew’s hotel room door. In doing so, he was able to record video of her activities in the room, including changing and dressing. Eventually, he posted these videos on the Internet. 1 Plaintiff’s complaint also contained allegations against other defendants for similar events that occurred at other hotels on other dates. Those counts were all dismissed on procedural grounds. - 3 - ¶ 4 Defendant Preferred is a corporation with its principal place of business in Chicago, Illinois. It provides marketing, sales and reservation services to its network of hotels for a fee. Blackwell is a member of Preferred’s network and utilizes Preferred’s marketing and Internet reservation services. Andrews alleged that Preferred is liable for Blackwell’s staff disclosing her hotel stay and room number to Barrett and assigning him the room next door to her, without her prior consent thereby allowing him to engage in his tortious activities. ¶ 5 Plaintiff’s theory of liability is that Preferred “owned, operated, controlled, maintained, managed, supervised, handled reservations for and/or were otherwise responsible for The Blackwell Inn” and that Blackwell “was the agent and/or joint venture of Preferred *** acting within the course, scope and authority of said agency and/or venture.” Preferred “had a duty to exercise reasonable and ordinary care and action in and about the ownership, management, maintenance, supervision, control and operation of Blackwell and its reservation system, and each of their employees, agents, servants and independent contractors, all to the benefit of the guests.” Preferred was “negligent in the selection, hiring, training and supervision of each and every other defendant as an agent and/or joint venturer.” Plaintiff also alleged that Preferred and OSU were associated with the purpose of “carrying out a specific enterprise for profit.” Preferred and OSU had a community of interest and proprietary interest in Blackwell; Preferred had a right to govern the hotel’s policies and share in the hotel’s profits and losses. Based on this theory, plaintiff alleged claims against Preferred for negligent infliction of emotional distress and invasion of privacy. ¶ 6 In response to the complaint, Preferred filed a hybrid motion to dismiss under section 2-619.1 of the Code, which permits a party to combine a section 2-615 motion to dismiss with a section 2-619 motion to dismiss. 735 ILCS 5/2-619.1 (West 2010). Preferred argued that the claims must be dismissed pursuant to section 2-615 of the Code because plaintiff failed to allege sufficient facts to support the conclusory allegation that Preferred owed plaintiff a legal duty. Preferred also argued dismissal of the claims pursuant to section 2-619(a)(9) of the Code because Preferred did not owe a duty to plaintiff for the acts of Blackwell’s staff, there was no principal-agent or joint venture relationship between Preferred and Blackwell and Preferred had no knowledge that Andrews was a guest at the hotel. ¶ 7 Attached to Preferred’s motion to dismiss was a written agreement governing the relationship between Preferred and OSU. The preamble to the agreement provides that Preferred “is a service organization designed to provide marketing, sales and reservation services to member hotels.” In return for these services, Blackwell pays membership and booking fees to Preferred, it agrees to “conform strictly” with Preferred’s “Quality Assurance Program” (Standards of Excellence) and allows Preferred “to evaluate the quality of the property and related services rendered at the hotel *** from time to time *** and bear the cost of these evaluations.” The agreement explains that Preferred will invoice Blackwell every 30 days for any amounts owed and if any amounts remain unpaid after 60 days, Preferred has the right to suspend all services and charge 1.5% per month on the unpaid sums. ¶ 8 The affidavit of Xen Riggs, the associate vice president of administration and planning at OSU, was also attached to Preferred’s motion to dismiss. In this affidavit, Mr. Riggs attested that Blackwell is owned by OSU, its operations are governed by OSU’s board of trustees and it is managed by OSU’s office of administration and planning. Blackwell runs a deficit, but if it were to make a profit, any profit would solely benefit OSU. Preferred does not have any - 4 - employees at Blackwell, does not handle any phone calls to Blackwell, and does not have any involvement in the operations or management of Blackwell. ¶ 9 Also supporting Preferred’s motion was the affidavit of Ken Mastrandrea, Preferred’s executive managing director of corporate operations. Mr. Mastrandrea averred that Preferred provides online hotel reservation services to Blackwell via Preferred’s Internet booking engine (iBook). Blackwell maintains a link to iBook on its website. Preferred’s involvement with reservations made with Blackwell are limited to those made through the iBook platform. A guest inputs the reservation information into iBook, which then electronically sends the reservation request to Blackwell’s computer system, and if accepted, the guest receives electronic confirmation including the room rate and type. Preferred’s involvement with reservations at Blackwell is limited to providing the platform for the electronic transmittal of reservation confirmation to and from the hotel and its guests via the Internet. If room reservations are made other than through iBook, Preferred does not have access to any guest identity or information. Preferred never has had access to Blackwell’s guest list or any guest’s room number. Preferred has no access to any information regarding guests who booked their rooms directly through the hotel or through any other means. Because Preferred does not have access to guest identities or guest room numbers, if someone called their office requesting this information, Preferred could not give the caller any such information. ¶ 10 Mr. Mastrandrea also attested that Preferred has no ownership interest in the hotel and does not share in its profits or losses. Preferred charges Blackwell a fee for membership in the network and for its booking services. Preferred has no involvement in the operation or management of its member hotels, including Blackwell’s policies and procedures regarding safety and/or privacy. There are no “Preferred” employees at Blackwell or any of its member hotels and it does not handle phone calls placed to the member hotels. According to Preferred’s records, Andrews’s reservation was not made through Preferred’s system, and therefore, it had no knowledge that Andrews was a guest at the hotel. Barrett made a reservation through iBook on Blackwell’s website for which Preferred was paid a service fee. However, Preferred’s actions in respect to Barrett’s reservation were limited to the electronic reservation request automatically generated through the hotel’s computer system and a confirmation notice sent to Barrett over the Internet. ¶ 11 At plaintiff’s request, the circuit court permitted discovery regarding the matters raised in the motion to dismiss. This discovery was conducted over a two-year period and included the deposition of Mr. Mastrandrea. ¶ 12 At his deposition, Mastrandrea testified that Preferred’s “Standards of Excellence” are comprised of “1600 items of guest service standards that we provide to the hotel to manage their service to guests.” Member hotels are required to comply with the standards. Once a year, third-party independent inspectors perform a check to determine the level of compliance. The inspectors prepare a report that informs the hotels of their aggregate compliance score and ways to improve. A follow-up inspection is required only if a hotel falls below 70% compliance. The compliance reports are reviewed by one of Preferred’s regional managers. A Preferred executive only reviews an inspection report if the compliance score is lower than 70%. Preferred relies on the hotels to make the inspector’s suggested corrections. If corrections are not successfully made, Preferred might request an improvement plan from the hotel and follow up as needed. If a hotel still fails to remediate, then Preferred reviews the results and possibly extends the improvement plan or takes further action. Preferred has close to 800 - 5 - member hotels. In its history Preferred has terminated its relationship with only three or four hotels. All of Blackwell’s inspections have exceeded a 70% compliance rate, and therefore, no executive at Preferred has been referred to review Blackwell’s reports. There are no standards or inspection criteria that address hotel staff informing a third party about other guests staying at the hotel or granting a guest’s request to be placed in the hotel room next to another guest without prior consent. ¶ 13 After completion of discovery, plaintiff filed a written response to the motion to dismiss. Plaintiff argued that Preferred’s motion should be denied because it was a “disguised motion for summary judgment,” Preferred’s “ ‘evidence’ ” merely refutes plaintiff’s ultimate facts, which does not constitute affirmative matter, and a question of fact exists as to whether Preferred owed a duty of care to plaintiff. Plaintiff asserted that Preferred owed her a duty of care because either it was in a joint venture with OSU in the operation of Blackwell or Preferred voluntarily assumed a duty of care. Plaintiff contended that because Preferred requires its member hotels to comply with the “Standards of Excellence” that includes matters of privacy (communicating a guest’s room number in writing rather than verbally and requiring identification before issuing a duplicate key), Preferred voluntarily assumed a duty to protect the privacy of guests at its member hotels. Plaintiff also argued that Preferred exercised control over the safety measures and policies of Blackwell and these actions created a joint venture, giving rise to Preferred’s liability for the actions of Blackwell’s staff. ¶ 14 After the hearing, the circuit court granted Preferred’s motion to dismiss pursuant to section 2-619(a)(9) of the Code. The circuit court found that the parties’ discovery established that “[t]he relationship between Preferred and Blackwell was limited to services provided for electronic transmittal of requests to Blackwell in transmission of confirmation numbers back to guests.” The agreement between Preferred and OSU/Blackwell was the “limitation of the undertaking,” and the discovery established that Preferred does not have access to room numbers or other information concerning guests. Preferred is simply “a contract service provider; they charge for their services and they get paid for their services.” Although plaintiff alleged that Preferred and OSU were engaged in a joint venture, plaintiff was unable to provide the court with any evidence to dispute Preferred and OSU’s “contractual relationship.” Preferred and OSU’s written agreement for services defined their duties “which do *** not cover the conduct alleged in the complaint,” and therefore, Preferred cannot be held liable to plaintiff for the acts of Blackwell’s staff. In view of this ruling, the circuit court found Preferred’s section 2-615 motion to dismiss moot and also ordered that there was “not [sic] just reason for delay of appeal or enforcement of this order.” Thereafter, plaintiff timely filed this appeal. ¶ 15 ANALYSIS ¶ 16 First, plaintiff argues that Preferred’s motion was improperly designated as a motion to dismiss and, therefore, should have been denied outright. Plaintiff contends that the motion was a “disguised” summary judgment motion that did not involve an “affirmative matter” but merely refuted plaintiff’s well-pled allegations. In response, defendant disagrees and argues that if its arguments for dismissal were more appropriate for summary judgment rather than section 2-619 dismissal, reversal is only required where the nonmovant was prejudiced by the misdesignation. - 6 - ¶ 17 “The purpose of a section 2-619 motion to dismiss is to dispose of issues of law and easily proved issues of fact at the outset of litigation” (Van Meter v. Darien Park District, 207 Ill. 2d 359, 367 (2003)) and is “similar to a summary judgment motion because [it] ‘*** essentially amounts to a summary judgment procedure.’ ” Peterson v. Randhava, 313 Ill. App. 3d 1, 9 (2000) (quoting Malanowski v. Jabamoni, 293 Ill. App. 3d 720, 724 (1997)). These types of motions are similar because in order to rule on them we must determine “whether the existence of a genuine issue of material fact should have precluded the dismissal or, absent such an issue of fact, whether the dismissal is proper as a matter of law.” Raintree Homes, Inc. v. Village of Long Grove, 209 Ill. 2d 248, 254 (2004). Misdesignation of a motion for summary judgment as a motion to dismiss is not fatal to the movant’s right to prevail where the nonmoving party did not suffer any prejudice or unfair surprise due to the error. Peterson, 313 Ill. App. 3d at 9. ¶ 18 Here, the affirmative matter presented in Preferred’s motion is that it did not owe a duty of care to plaintiff because it did not have a principal-agent or joint venture relationship with the hotel and did not otherwise voluntarily undertake a duty of care. To support its motion, Preferred attached to its motion a copy of the written agreement between Preferred and OSU/Blackwell and the Riggs and Mastrandrea affidavits. Over the course of two years, the circuit court permitted the parties to conduct written and oral discovery on the matters raised in Preferred’s motion. Therefore, in this instance, where a defined issue was raised in Preferred’s motion and plaintiff was granted time to conduct lengthy discovery on Preferred’s assertions, we find that, whether viewed as a motion to dismiss or a motion for summary judgment, plaintiff was not prejudiced in the designation of the motion to dismiss as a motion under section 2-619(a)(9) of the Code. ¶ 19 The circuit court dismissed plaintiff’s complaint pursuant to section 2-619(a)(9) of the Code, which permits the involuntary dismissal of a claim where the claim asserted is “barred by other affirmative matter avoiding the legal effect of or defeating the claim.” 735 ILCS 5/2-619(a)(9) (West 2010). Affirmative matter is “something in the nature of a defense which negates the cause of action completely or refutes crucial conclusions of law or conclusions of material fact contained in or inferred from the complaint.” Illinois Graphics Co. v. Nickum, 159 Ill. 2d 469, 486 (1994). “Unless the affirmative matter is already apparent on the face of the complaint, the defendant must support the affirmative matter with an affidavit or with some other material that could be used to support a motion for summary judgment.” Pleasant Hill Cemetery Ass’n v. Morefield, 2013 IL App (4th) 120645, ¶ 21. Once a defendant has presented adequate affidavits or other evidence of support, “ ‘the defendant [has] satisfie[d] the initial burden of going forward on the motion’ ” and the burden then shifts to the plaintiff who is required to establish that the affirmative matter is either unfounded or involves an issue of material fact. Reynolds v. Jimmy John’s Enterprises, LLC, 2013 IL App (4th) 120139, ¶ 37 (quoting Kedzie & 103rd Currency Exchange, Inc. v. Hodge, 156 Ill. 2d 112, 116 (1993). A plaintiff may overcome this burden by presenting “affidavits or other proof.” 735 ILCS 5/2-619(c) (West 2010). However, a plaintiff cannot rely on the allegations from his own complaint to refute such evidence. Hollingshead v. A.G. Edwards & Sons, Inc., 396 Ill. App. 3d 1095, 1101-02 (2009). In addition, if a plaintiff does not come forward with a counteraffidavit refuting the evidentiary facts in the defendant’s affidavit or other evidence, those facts may be admitted and the motion may be granted on the basis that plaintiff “failed to carry the shifted burden of going forward.” Hodge, 156 Ill. 2d at 116; Pleasant Hill Cemetery Ass’n, 2013 IL App (4th) 120645, ¶ 21. - 7 - ¶ 20 The affirmative matter raised by Preferred in its motion to dismiss, and supported with affidavits and deposition testimony, is that it did not owe a duty of care to plaintiff and it was not in a joint venture with Blackwell, and therefore, it could not be held liable for Blackwell’s disclosure of details regarding plaintiff’s hotel stay to Barrett or the assignment of Barrett to the room next to plaintiff without her prior consent. ¶ 21 Plaintiff argues that Preferred can be held liable for the events that occurred at Blackwell because either (1) Preferred was a member of a joint venture with Blackwell to operate the hotel or (2) Preferred voluntarily assumed a duty of care to plaintiff. She contends that these theories of liability involve questions of fact that should have precluded dismissal of her claims. ¶ 22 Joint Venture ¶ 23 A joint venture is an association of two or more persons to carry out a single enterprise for profit. O’Brien v. Cacciatore, 227 Ill. App. 3d 836, 843 (1992). Members of a joint venture are vicariously liable for the joint venturers’ negligent acts committed during the course of the venture. Hiatt v. Western Plastics, Inc., 2014 IL App (2d) 140178, ¶ 72. Ordinarily whether a joint venture exists is a question of fact; however, where there is no evidence to support the existence of a joint venture, its existence can be decided as a matter of law. Anderson v. Boy Scouts of America, Inc., 226 Ill. App. 3d 440, 444 (1992); Oliveira-Brooks v. Re/Max International, Inc., 372 Ill. App. 3d 127, 134 (2007). “The existence of a joint venture is shown by allegations demonstrating (1) a community of interest in the purpose of the joint association, (2) a right of each member to direct and govern the policy and conduct of the other members, and (3) a right to joint control and management of the property used in the enterprise.” Romanek v. Connelly, 324 Ill. App. 3d 393, 405 (2001) (citing Behr v. Club Med, Inc., 190 Ill. App. 3d 396, 409 (1989)). A formal agreement is not essential to establish a joint venture (Hiatt, 2014 IL App (2d) 140178, ¶ 73), and its existence “may be inferred from the facts and circumstances demonstrating that the parties in fact entered into a joint venture” (O’Brien, 227 Ill. App. 3d at 843). However, the most significant element to consider in determining whether a joint venture exists is the intent of the parties. Thompson v. Hiter, 356 Ill. App. 3d 574, 582 (2005). ¶ 24 Plaintiff claims Preferred is liable for Blackwell’s actions because Preferred and OSU were engaged in a joint venture to operate Blackwell. Plaintiff argues Preferred and OSU/Blackwell’s course of conduct created a joint venture, specifically, Preferred’s control over the operations and policies of Blackwell and the sharing of reservation fees. We disagree and find that, on the record before us, Preferred and OSU were nothing more than two separate entities contracting with one another for a particular service from which each would derive their own individual profit. ¶ 25 The record before us includes a written agreement between Preferred and OSU that governs their relationship regarding limited services for Blackwell. Under the agreement, Preferred provides OSU/Blackwell with marketing, sales, and reservation services in exchange for a fee. The agreement does not mention the creation of a joint venture or enterprise, and Preferred and OSU’s rights and obligations under the agreement are different from one another. In fact, we found nothing in the agreement to infer that Preferred and OSU intended to operate Blackwell as a joint venture enterprise. Furthermore, as we discuss below, plaintiff has not provided any “affidavits or other proof” to refute Preferred’s affidavits and testimony - 8 - supporting the affirmative matter that Preferred and OSU/Blackwell did nothing to create a joint venture either through the written agreement or through their conduct. ¶ 26 Common Interest ¶ 27 As to the first element necessary to establish a joint venture, plaintiff contends that a community of interest is evidenced by Blackwell becoming a member of Preferred’s hotel network and Blackwell having access to Preferred’s iBook reservation system, which evidences a joint venture relationship. We are not persuaded. Nothing in the parties’ agreement or conduct, as developed from the discovery in the record, supports the conclusion that they shared a community of interest in association with Blackwell. Certainly, both parties expected to benefit from their contractual association, but this does not indicate the intention to create a joint venture to operate Blackwell. See Kaporovskiy v. Grecian Delight Foods, Inc., 338 Ill. App. 3d 206, 212 (2003). In fact, the agreement indicates that Preferred and Blackwell had two different interests in doing business with one another. Preferred would allow Blackwell the use of its reservation system so that Internet users could book a hotel stay, and Preferred would be paid a fee for reserving a room using its iBook service. This fee would be earned regardless of whether the reservation proved profitable to Blackwell. In return, Blackwell would sell a room and generate revenue from that and other services. There is no evidence Preferred would financially benefit beyond the fee earned through iBook. Simply put, two distinct entities doing business together does not equate to the establishment of a joint venture. See id. ¶ 28 Right to Govern Blackwell’s Policy and Joint Control Over the Enterprise ¶ 29 Next, as to the second and third joint venture elements, plaintiff suggests that Preferred’s contractual requirement that its member hotels comply with its “Standards of Excellence” equates to Preferred’s right to direct the conduct and policy of Blackwell and exert control over its operation. Contractual agreements that require one party to perform or forbid performance of a particular act does not equate to control of management for the purpose of imposing a joint venture. Kaporovskiy, 338 Ill. App. 3d at 212 (limiting one contracting party from selling competing food products did not equate to “control over property” or policy); Barton v. Evanston Hospital, 159 Ill. App. 3d 970, 974-75 (1987) (“mutuality of control” absent in a contractual relationship where doctor has discretion in patient treatment even though hospital supplied doctor with necessary equipment and personnel). ¶ 30 Here, the written agreement does not give Preferred any degree of joint control over the operation of Blackwell. Although Preferred requires that its member hotels follow the “Standards of Excellence,” the evidence before us establishes that member hotels, including Blackwell, are not required to be in complete compliance with Preferred’s standards and the hotels may interpret the standards and make adjustments or improvements at their discretion. Preferred merely provides a list of standards that it wants its member hotels to meet at a 70% or higher level, but Preferred does not actually engage in any management or control over the hotel, its operations, or its staff. According to Mr. Mastrandrea’s affidavit and deposition testimony, which has not been refuted by plaintiff through “affidavits or other proof,” Preferred does not have any employees at Blackwell, Preferred does not and never had access to Blackwell’s guest list or the assignment of hotel room numbers. Therefore, we find that Preferred and Blackwell did not have “mutuality of control” over the hotel’s property and policies necessary to establish that element of a joint venture. - 9 - ¶ 31 Although plaintiff also contends that there was a sharing in the profits and the losses of Blackwell, there is no evidence in the record to support this conclusion. Preferred’s receiving a fee for its marketing and reservation services is not akin to having a common interest and sharing profits in the operation of Blackwell. Landers-Scelfo v. Corporate Office Systems, Inc., 356 Ill. App. 3d 1060, 1066 (2005) (cooperation between two entities consisting of one handling of the payroll and human resources function of another company for a fee is insufficient as a matter of law to show a joint venture existed). There is nothing in the record to suggest that Preferred and Blackwell were anything other than two separate entities doing business with one another for their separate financial benefit. More than a mere interest in another entity’s success must be asserted to allege a joint venture. Two businesses entering into a service agreement “seeking to mutually profit from it” is not enough to turn a business relationship into a joint venture sufficient to impose vicarious liability on a contracting party. Kaporovskiy, 338 Ill. App. 3d at 212. While Preferred may have hoped for Blackwell’s continued success so that it could earn more fees through its booking and reservation services, this is not enough to support the legal conclusion that these entities were engaged in a joint venture. Finally, after two years of discovery, a further indication that no joint venture existed is the evidence that Preferred would collect booking fees even if Blackwell operated at a financial loss. ¶ 32 In the absence of any one of the required elements, a joint venture cannot be found to exist in fact or in law. Powell v. Dean Foods Co., 2013 IL App (1st) 082513-B, ¶ 76. It is plaintiff’s burden to show that she can support her claim that Preferred engaged in a joint venture to operate Blackwell. Petry v. Chicago Title & Trust Co., 51 Ill. App. 3d 1053, 1057 (1977). Beyond mere conclusory allegations, plaintiff has failed to support her legal conclusion or establish that a question of fact exists as to the existence of a joint venture. Therefore, we affirm the ruling of the circuit court that Preferred did not have a duty to plaintiff on this basis. ¶ 33 Voluntary Undertaking ¶ 34 Next, plaintiff argues that whether Preferred voluntarily assumed a duty to protect her privacy as a guest of Blackwell is a question of fact that precludes dismissal under section 2-619(a)(9) of the Code. We disagree and find that no genuine issue of material fact exists as to whether Preferred voluntarily undertook a duty to protect the privacy of Blackwell’s guests. ¶ 35 Negligence cannot be established unless the defendant owed the plaintiff a duty of care. LaFever v. Kemlite Co., 185 Ill. 2d 380, 388 (1998). Whether a duty of care exists is a question of law. Id.; Chelkova v. Southland Corp., 331 Ill. App. 3d 716, 722 (2002). Illinois courts have adopted section 324A of the Restatement (Second) of Torts (1965), which provides that one may be liable to a third person for the negligent performance of a voluntary undertaking. The relevant sections of section 324A of the Restatement provide as follows: “One who undertakes, gratuitously or for consideration, to render services to another which he should recognize as necessary for the protection of a third person or his things, is subject to liability to the third person for physical harm resulting from his failure to exercise reasonable care to protect his undertaking, if: (a) his failure to exercise reasonable care increases the risk of such harm, or (b) he has undertaken to perform a duty owed by the other to the third person, or - 10 - (c) the harm is suffered because of reliance of the other or the third person upon the undertaking.” Restatement (Second) of Torts § 324A (1965). See Bell v. Hutsell, 2011 IL 110724, ¶¶ 12-14; Pippin v. Chicago Housing Authority, 78 Ill. 2d 204 (1979). Under this theory, the scope of an assumed duty “ ‘is limited to the extent of the undertaking’ ” and must be narrowly construed. Jablonski v. Ford Motor Co., 2011 IL 110096, ¶ 123 (quoting Bell, 2011 IL 110724, ¶ 12); Siklas v. Ecker Center for Mental Health, Inc., 248 Ill. App. 3d 124, 131 (1993); Frye v. Medicare-Glaser Corp., 153 Ill. 2d 26, 32 (1992). To determine the extent of the voluntary undertaking we consider, on a case by case basis, both the specific act undertaken and a reasonable assessment of its underlying purpose. Bourgonje v. Machev, 362 Ill. App. 3d 984 (2005). ¶ 36 Plaintiff argues that Preferred’s voluntary undertaking was evidenced by several factors: (1) Preferred’s requirement that its member hotels comply with its “Standards of Excellence,” which included two standards involving guest privacy; (2) Preferred’s hiring of independent inspectors to review compliance with these standards; and (3) the appearance of Preferred’s signage in the hotel informing hotel guests that the hotel is a member in Preferred’s network. Plaintiff contends that, because Preferred has two privacy-related standards (that the hotel communicate the room rate and room number in writing at check-in and proof of identity must be shown before a duplicate key is issued), the absence of a standard relating to disclosing guest identity and room number or placing a guest next to another on request is a breach of voluntary undertaking to protect a guest’s privacy. Further, plaintiff argues that Preferred negligently failed to prevent Blackwell from disclosing the identity of Andrews, the dates of her stay, her r





     https://saaze2311prdsra.blob.core.windows.net/clean/492607eac7d7ec11a7b5000d3a1afadb/CRD149777_GORMAN4026328-6048300.pdf

    
     https://saaze2311prdsra.blob.core.windows.net/clean/f07de67079d5ec11a7b5000d3a1af965/2020-05-Jpetit-cbrooks7.png
    
     https://saaze2311prdsra.blob.core.windows.net/clean/61f910a979d5ec11a7b5000d3a1af965/2020-06-03%20Notice%20and%20Obstruction.png
    
    https://saaze2311prdsra.blob.core.windows.net/clean/2f7c8ae375d5ec11a7b5002248307b90/Screenshot_20220516-013630_Chrome.jpg
    
    
    2010-10-05        REQUEST TO QUASH
    
    https://saaze2311prdsra.blob.core.windows.net/clean/f39766e089d5ec11a7b5000d3a1afadb/email.20201005-wilsonElser-Quash.pdf
    
    
            https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/pull/35
         
    " STATE FARM LLOYDS "
    https://www.tdi.texas.gov/commissioner/disciplinary-orders/documents/20153854.pdf
    ---BROKERCHECK RANDALL HOUSTON HARBERT [MEMBER 2992788]
    
       
           
                           

       

https://saaze2311prdsra.blob.core.windows.net/clean/f07de67079d5ec11a7b5000d3a1af965/2020-05-Jpetit-cbrooks7.png

DOOR
https://saaze2311prdsra.blob.core.windows.net/clean/e4fd40a036d6ec11a7b5002248307f33/Door-221606_Gallery.jpg.PDF

2021-11-16    Morgan Stanley PLEASE FORWARD TO COMPLIANCE
https://saaze2311prdsra.blob.core.windows.net/clean/6a91074b24d6ec11a7b50022483079c1/Compliance%202021-11-16.pdf

2021-11-16 - STATE FARM AND SULLIVAN PROPS
https://saaze2311prdsra.blob.core.windows.net/clean/521e9ac936d6ec11a7b5000d3a1af965/Nov.16-StateFarm.SullivanProps.PDF

2021-11-16    DOC NOTICE
https://saaze2311prdsra.blob.core.windows.net/clean/3c87e47421d6ec11a7b5002248307f33/2021-11-16-483docNotice.png

2021-11-17 - 483 MATERIAL CORPORATE ACTION
https://saaze2311prdsra.blob.core.windows.net/clean/0010c00837d6ec11a7b5000d3a1afadb/Nov.17.483MATERIALCORPORATEACT.PDF

2021-12-18
https://saaze2311prdsra.blob.core.windows.net/clean/8de5f89e10d3ec11a7b5002248286421/CE48526B-6A0E-4B2A-89B9-93BD202498A9.jpeg

2021-12-18 93715 C.16 --- BROKERS
https://saaze2311prdsra.blob.core.windows.net/clean/db5e3c6a10d3ec11a7b5000d3a132789/8A5FDA9F-D641-4B62-9D15-3AF4205617AC.jpeg


*** Tax Receipts— tax evasion - 117 SULLIVAN STREET
https://saaze2311prdsra.blob.core.windows.net/clean/0363e59f23d6ec11a7b5000d3a1afadb/BB-117taxFiles.pdf

2020-03-10    ice data service PROVIDERS
https://saaze2311prdsra.blob.core.windows.net/clean/3217723b20d6ec11a7b5002248307f33/2020-03-10%E2%80%94ICE%20Data%20Services.PDF

2020-03-10    ice data service PROVIDERS
https://saaze2311prdsra.blob.core.windows.net/clean/3217723b20d6ec11a7b5002248307f33/2020-03-10—ICE%20Data%20Services.PDF

2022-05-09    MSCO INSIDERS
https://saaze2311prdsra.blob.core.windows.net/clean/46c8dc8e20d6ec11a7b50022483079c1/2022-05-09-InsiderTrading.PDF

2022-05-11
https://saaze2311prdsra.blob.core.windows.net/clean/d585ccd85fd3ec11a7b5000d3a1326fe/TAX%20EVASION%20%20attachments%20%252F%20Omissions.%20.pdf

DOI NOTICE
https://saaze2311prdsra.blob.core.windows.net/clean/7391818e24d6ec11a7b5000d3a1af965/DoiNotice-TaxEvasion%20and%20Continued%20OPS.PDF

05-09-2022
https://saaze2311prdsra.blob.core.windows.net/clean/46c8dc8e20d6ec11a7b50022483079c1/2022-05-09-InsiderTrading.PDF

EY - PWC - MSCO NOTICE 04-12-2022
https://saaze2311prdsra.blob.core.windows.net/clean/b67c1a2d29d6ec11a7b5002248307b90/04.12.2022.151652.EY.PWC.MSCO-.pdf
 
Docket 348
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=TxAa7cNVIHKtnJU/ni/zvg==

Docket 53
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=LMUE9g_PLUS_k6vCmKgfCSJEzuQ==
       

       
_________________________________________________________________________________________________________
    
##################################
##################################
https://saaze2311prdsra.blob.core.windows.net/clean/2bffec7889d5ec11a7b50022483079c1/AA-CEASEORDR.pdf
https://user-images.githubusercontent.com/70865813/153544431-27d6b33b-d34a-4e37-9532-aad92b15264c.png
https://saaze2311prdsra.blob.core.windows.net/clean/2bffec7889d5ec11a7b50022483079c1/AA-CEASEORDR.pdf
https://saaze2311prdsra.blob.core.windows.net/clean/397718d1fcd8ec11a7b5002248307aa9/Case%20Number_%20%20ref1.pdf


#BIN-CODES PAR-ID, IN THE DECK. QUARTERLY



DOOR DOES NOT WORK.
https://saaze2311prdsra.blob.core.windows.net/clean/e4fd40a036d6ec11a7b5002248307f33/Door-221606_Gallery.jpg.PDF
https://saaze2311prdsra.blob.core.windows.net/clean/2df8ebfad2d7ec11a7b50022483079c1/[STATE%20FARM%20VP%2043036]Advisers%20Investment%20Trust%20[$CIK%201516523]%20MONK[CRD%201357149].pdf
https://saaze2311prdsra.blob.core.windows.net/clean/25aff4b997d3ec11a7b500224828654e/[STATE%20FARM%20VP%2043036]Advisers%20Investment%20Trust%20[$CIK%201516523]%20MONK[CRD%201357149].pdf
https://saaze2311prdsra.blob.core.windows.net/clean/5380dd8997d3ec11a7b5000d3a132789/[STATE%20FARM%20VP%2043036]Advisers%20Investment%20Trust%20[$CIK%201516523]%20MONK[CRD%201357149].pdf
https://saaze2311prdsra.blob.core.windows.net/clean/e9eb965d97d3ec11a7b5000d3a1326fe/[STATE%20FARM%20VP%2043036]$%203487%20$.pdf
https://saaze2311prdsra.blob.core.windows.net/clean/25aff4b997d3ec11a7b500224828654e/[STATE%20FARM%20VP%2043036]Advisers%20Investment%20Trust%20[$CIK%201516523]%20MONK[CRD%201357149].pdf
https://saaze2311prdsra.blob.core.windows.net/clean/ff91792a95d3ec11a7b50022482864f0/[sfVP43036]%20$2876793%20-%20david.moore%20$3487%20-%20IA%208018184.pdf
https://saaze2311prdsra.blob.core.windows.net/clean/af081f4095d3ec11a7b50022482864f0/[STATE%20FARM%20VP%2043036]%20$3231040-2004555.pdf
https://saaze2311prdsra.blob.core.windows.net/clean/d88e25ae5fd3ec11a7b5002248286997/StateFarmVP%20Management%20Corp-CRD%2343036.pdf
https://saaze2311prdsra.blob.core.windows.net/clean/172de37992d3ec11a7b500224828654e/[sfVP%2043036]%204971235-%20$SMITH%20-%20SEMI.pdf
https://saaze2311prdsra.blob.core.windows.net/clean/bee2b76c92d3ec11a7b5002248286997/[SF.VP%2043036]%202876793%20-%20$david%20moore%20$3487%20-%20IA%208018184.pdf
https://saaze2311prdsra.blob.core.windows.net/clean/9194266492d3ec11a7b500224828654e/[sf%20VP%2043036-$3487]%201943922-%20$%20tipsord%20$%20STATE%20FARM%20mutual%20automobile%20insurance%20company-$3487.pdf
https://saaze2311prdsra.blob.core.windows.net/clean/172de37992d3ec11a7b500224828654e/%5BsfVP%2043036%5D%204971235-%20$SMITH%20-%20SEMI.pdf
https://saaze2311prdsra.blob.core.windows.net/clean/bee2b76c92d3ec11a7b5002248286997/[SF.VP%2043036]%202876793%20-%20$david%20moore%20$3487%20-%20IA%208018184.pdf
https://saaze2311prdsra.blob.core.windows.net/clean/9194266492d3ec11a7b500224828654e/[sf%20VP%2043036-$3487]%201943922-%20$%20tipsord%20$%20STATE%20FARM%20mutual%20automobile%20insurance%20company-$3487.pdf
https://saaze2311prdsra.blob.core.windows.net/clean/e9eb965d97d3ec11a7b5000d3a1326fe/[STATE%20FARM%20VP%2043036]$%203487%20$.pdf
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=TxAa7cNVIHKtnJU/ni/zvg==
https://a836-acris.nyc.gov/DS/DocumentSearch/DocumentImageView?doc_id=2020052000291003
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=_PLUS_TlrEGCsUUcCcvtJ8O/dfg==
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=19MVPFXy0G0QvnmRLGpYIQ==
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=19MVPFXy0G0QvnmRLGpYIQ==
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=gcMSDaFzm0ynPeXZKSHgLQ==
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=au8qh7Dn66hrVmJ9DX_PLUS_bdg==
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=gcMSDaFzm0ynPeXZKSHgLQ==
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=TxAa7cNVIHKtnJU/ni/zvg==
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=LMUE9g_PLUS_k6vCmKgfCSJEzuQ==
https://portal.311.nyc.gov/sr-details/?id=4296b0c3-c4a2-ec11-826d-0003ff86900c
https://saaze2311prdsra.blob.core.windows.net/clean/d585ccd85fd3ec11a7b5000d3a1326fe/TAX%20EVASION%20%20attachments%20%252F%20Omissions.%20.pdf
https://saaze2311prdsra.blob.core.windows.net/clean/f2d6a0fe5fd3ec11a7b5000d3a1326fe/Fwd:%20unlawful%20RENT%20and%20PAYMENTS%20in%20CUSTODY%20at%20JP%20MORGAN%20CHASE%20BANK.pdf
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=19MVPFXy0G0QvnmRLGpYIQ==
    
    
https://saaze2311prdsra.blob.core.windows.net/clean/2f7c8ae375d5ec11a7b5002248307b90/Screenshot_20220516-013630_Chrome.jpg


21 JULY 2020 - REQUEST TO DEFENDANTS TO CEASE AND DESIST [ DESC EXHIBIT ].png

0 PHOTOGRAPH OF MY APARTMENT - BEFORE THEY DECIDED TO FILM AND DOCUMENT MY EVERY MOVEMENT AND DISCUSSION.JPG

1 CAMERA IS MOUNTED ON THE SECOND STORY AND AIMED AT MY BED - PILLOWSN - AND LAPTOP.JPG

1 CAMERA IS MOUNTED ON THE SECOND STORY AND AIMED INTO MY APARTMENT.JPG

2 PHOTOGRAPH OF MY CLOSET --- TAKEN BY THEIR PORTER.JPG

3 ANOTHER PHOTOGRAPH --- TAKEN BY THEIR PORTER NOTE (BLACKOUT TINTS).JPG

4 ANOTHER PHOTOGRAPH --- TAKEN SHORTLY AFTER THEY MOUNTED THE CAMERA WHICH WAS AIMED AT MY WINDOW.JPG

5 ANOTHER PHOTOGRAPH --- TAKEN SHORTLY AFTER THEY MOUNTED THE CAMERA WHICH WAS AIMED AT MY LAPTOP.JPG

6 ANOTHER PHOTOGRAPH --- CAN THAT CAMERA ZOOM IN AND OUT AND VIEW MY LAPTOP ON AUGUST 10TH 2020.JPG

7 ANOTHER PHOTOGRAPH --- CAN THAT CAMERA FILM ME IN THE EVENINGS.JPG

8 ANOTHER PHOTOGRAPH --- CAN THAT CAMERA FILM ME IN THE DAYTIME.JPG

9 ANOTHER PHOTOGRAPH --- CAN THAT CAMERA FILM IN COLOR AND BE EDITED TO DOWNSAMPLE THE PIXELS.JPG

9 ANOTHER PHOTOGRAPH --- WAS I WEARING A SHIRT --- LOOKS LIKE NO IN THAT ONE --- WHAT ABOUT ALL THE OTHER ONES ----.JPG

9 ANOTHER PHOTOGRAPH --- WAS I WEARING A SHIRT EARLIER --- BUT HOW ANGRY IS THE POWERWASHER GUY.JPG

10 AREYNOSO@MSKYLINE.COM --- APPARENTLY HIS EMAIL ALSO DOESNT WORK ANYMORE..JPG

10 CHANN --- JGIAMBOI@MSKYLINE.COM -- LZUCKER@MSKYLINE.COM -- LEGAL@MSKYLINE.COM --- CWEISS@INGRAMLLP.COM [MOV].JPG

10 JGIAMBOI@MSKYLINE.COM --- APPARENTLY HIS EMAIL ALSO DOESNT WORK ANYMORE..JPG

10 ROSALIA CHANN --- DISTRIBUTED LINKS TO THE INTERNET -- CONVERTED INTO MOV FILES AND CIRCULATED.JPG

10 TESCHMANN@MSKYLINE.COM --- APPARENTLY HIS EMAIL ALSO DOESNT WORK ANYMORE..JPG

11 HERES A VIDEO OF ME SHANKING SOMEONE IN THE YARD.JPG

11 NOPE... NEVERMIND --- JUST ANOTHER VIDEO OF JHIM RECYLING --- LETS GO AHEAD AND VIDEOTAPE IT ANYWAYS.JPG

12 ROSALIA CHANN --- ON-DEMAND VIDEOS (NOT FOR SALE THOUGH) SAME AS THE ONE FROM THE [MOV] EARLIER IN CASE YOU MISSED THAT.JPG

12 ROSALIA CHANN --- ON-DEMAND VIDEOS (NOT FOR SALE THOUGH).JPG

13 JULY 6 2020 - CAMERA IS STILL THERE --- MAYBE ITS AN ISSUE --- SEE ALSO --- OTHER REQUESTS.JPG

14 VIDEO OF MY ENTRY WAY --- USING RODENT INSULATION THAT WENT THROUGH A HOLE IN THEIR WALL..JPG

14 VIDEO OF MY ENTRY WAY --- USING RODENT INSULATION WENT THROUGH A HOLE IN THEIR WALL -- A LITTLE DEEP FOR A CORRIDOR.JPG

15 THEY JJUST ADDRESS ME IN CARE OF [THE BUILDING ] NO NEED FOR AN APARTMENT NUMBER I GUESS - WORD GETS AROUND.JPG

16 A REQUEST FOR JUDICIARY INTERVENTION ADDRESSED IN CARE OF THE BUILDING - NO APARTMENT NUMBER --- GOOD TO GO..JPG

16 NOTE --- APARTMENT CONDITION ---- POST KEEBLER ELVES SURVEILLANCE AND HARASSSMENT OPERATIONS.JPG

21 MIWAKO G MESSERS DAILY REPORTS --- THE LEAD KEEBLER ELF IN HER 10 MINUTE PLAY-BY-PLAY ---- GOES ON AND ON.JPG

21 MIWAKO G MESSERS DAILY REPORTS NUMBER 7.JPG

21 MIWAKO G MESSERS DAILY REPORTS NUMBER 10.JPG

21 MIWAKO G MESSERS DAILY REPORTS NUMBER 12.JPG

21 MIWAKO G MESSERS DAILY REPORTS NUMBER 17 --- CAN WE GET A COUNT ON THE NUMBER OF TIMES THE DOOR WAS OPENED IM CURIOUS.JPG

21 MIWAKO G MESSERS DAILY REPORTS NUMBER 21 ----- EVERYBODY --- EMERGENCY ----- MIWA HAS FOUND A MASK DURING THE COVID PANDEMIC.JPG

21 MIWAKO G MESSERS DAILY REPORTS NUMBER 23 --- IF YOURE LOCKED OUT AND NEED THE RESTROOM ---- WAIT WAS I EVEN HOME.JPG

21 MIWAKO G MESSERS DAILY REPORTS NUMBER 27 --- HENCE --- THE HOUSE OF KEEBLER ELVES RUNNING UP AND DOWN TO COMPLETE THEIR TASKS.JPG

TAKEN FROM INSIDE OF MY CLOSET --- I CAN SEE THE HOLE OF THE CAMERA..JPG

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[5a897f987c...](https://github.com/mrakgr/The-Spiral-Language/commit/5a897f987c554fb8b3e33f730c7f6d7c1f6367bd)
#### Sunday 2022-06-26 18:24:01 by Marko Grdinić

"https://groups.google.com/a/grasehotspot.org/g/grase-hotspot/c/HI4iHL8k67k/m/q5wvvQ0OEQAJ
Upload rate near zero with Grase

///

hey there! its been a long time since i've been here.

i had the same problem and i did solve it with turning gro off on the lan interface of the hotspot.

u can do it by installing ethtool (shell: sudo apt-get install ethtool), and using it to turn of the gro on selected interface (example: ethtool -K eth1 gro off)

hope i've helped. don't know the reason, but this worked for me.

btw. i had this problem with http, for some reason https upload was working (at least better than http!)

///

I asked this question almost 6 years ago and it is still relevant.

Let me get that laptop.

3:40pm.

///

1. burn Ubuntu 14 server in DD mode
2. install LAMP and SSH server during install - optional, will be downloaded off the net automatically in case you forgot
3. sudo apt-get update & sudo apt-get upgrade - dpkg will give a weird error if it is out of date
4.
    ifconfig - remember the MAC of main card for the later steps
	sudo nano /etc/default/grub
	edit it so: GRUB_CMDLINE_LINUX="net.ifnames=0 biosdevname=0"
	sudo update-grub
	reset - this will create the rules file
	sudo nano /etc/udev/rules.d/70-persistent-net.rules
	swap router names as needed
5.
	sudo nano /etc/network/interfaces
	edit to refer to eth0 instead of p1p1 - grase needs eth0 to be the internet connection
6. wget http://packages.grasehotspot.org/pool/main/g/grase-repo/grase-repo_1.8_all.deb
7. sudo dpkg -i grase-repo_1.8_all.deb
8. sudo apt-get update
9. sudo apt-get install grase-www-portal grase-conf-freeradius
10. if uploads are slow
    ethtool -K eth1 tso off gro off gso off
    this setting doesn't need a restart
///

Here is the update hotspot tip. It turns out just turning gro off is not enough, there are also two extras. Dad managed to find those somehow, I am amazed. Sometimes he exceeds me when it comes to looking up stuff on Google.

Great. This time I am done for good with that rig. Freedom.

3:45pm. Now I need to think about what to do next.

4pm. Let me take a break so I can get in the mood.

4:05pm. Yeah, what I need to do now is cultivate a special skill that I didn't have time to before. That is drawing characters. Sculpting is only an excuse. I should give drawing them in CSP a serious try. I'll get that model and draw over them.

4:20pm. Done with the break. Let me start.

I'll admit, drawing is hard, but that is only the situtation when you can't just trace over the image. If you have a model like the ones CSP gives you how hard could it be?

4:25pm. Compared to 2d, 3d does have a lot of advantages when it comes to doing environments and composing complex scenes. The scattering capabilities of it as something trad painters can only dream of. Ray tracing rendering is hugely helpful for such things. But when it comes to drawing anime style characters, that should not be necessary.

4:30pm. Given how easy I expected drawing anime characters would be, I did not bother putting too much concern into learning it.

Still, even though will be easy, the chara illustrations will contribute 30-50% to Heaven's Key visual quality. So I can't neglect them too much.

4:40pm. One side goal which I've been neglecting is going through those 900 VN cover images. I need to refine my main styles. I'll kick out some of the drawings and add some more interesting ones from the wikiart dataset.

4:45pm. Now forget that. I need to focus on the task at hand instead of just living in my head for 45m straight. Though it is cliche, let me start off with a tutorial.

https://youtu.be/MWvKqyAqFVE
3 helpful steps for character sketches | Inma R

I need something to show me how to use the 3d models. I did that last year, but by now that knowledge has faded away. I need a refresher. That should be my first priority right now. I'll switch between doing this and sculpting as I go along. I am not in a hurry.

4:50pm. One thing I am going to have to get out of the way is getting up early at like 6am when it is cool, and moving that big wood pile inside the sheed. I did that last year, and now it is time to get busy with that again. Since I am done with the cover and the first scene.

4:55pm. Focus me, let me just watch the above. I'll dedicate at least a month to chara modeling and drawing. My env skills are quite decent now, so it is time to tackle this.

https://youtu.be/MWvKqyAqFVE?t=17

Yep, this is what I mean. Compared to doing it raw, this should be a lot easier.

https://youtu.be/MWvKqyAqFVE?t=102

Let me try immitating this step.

5:05pm. Ok, I've put the model onto the canvas, but it is pretty confusing as to how to use it after that. I am going to have to spend some time familiarizing myself. I need to make a choice, or rather, let the battle play out. I need to test both sculpting and texturing everything in 3d, in other words doing everything in 3d vs using CSP and using some of its aids to do chara design.

2d vs 3d. I need to sit which method is more fitting for me. Figuring this out will no doubt take my time. Right now, let just focus on watching CSP tutorials. I'll watch the one I am currently on and then watch some 3d specific ones.

5:20pm. https://www.youtube.com/results?search_query=clip+studio+3d

This is what I should be focusing on.

Let me watch some of these. Given how late it is I really don't feel like starting work on anything new, but that does not matter. What I should focusing is simply on playing around with CSP's 3d capabilities. Once I have a handle on that, then I can start thinking what to do with it. And not just poses, but other 3d assets as well.

https://youtu.be/22DNGGvYy-Y?t=50
2D ARTISTS should use 3D MODELS 🎓 Clip Studio Paint Tutorial

Yes, this is what I need.

https://youtu.be/22DNGGvYy-Y?t=166

I got this far before. Since I am pirating CSP, it does not seem I can use its asset store, but that does not matter. Right now I just want to do simple chara design.

5:55pm. https://youtu.be/22DNGGvYy-Y?t=343

This hand posing stuff is interesting. I am really having trouble getting used to how the camera works in this. Does it have to use the gizmos for everything?

6pm. Now I am reading Ayakahi Triangle. Ah whatever, let me take a break. I do not feel like struggling so much. I'll get it done.

6:15pm. https://youtu.be/22DNGGvYy-Y?t=596

This is so boring. That I am not into it is a problem. And it is the main problem.

If I can't get into it, I will step away from the screen, take naps, and charge up my motivation until I feel like doing it.

https://youtu.be/22DNGGvYy-Y?t=962

Hmmm, it supports characters. I wonder how that works?

6:30pm. https://youtu.be/u0GWW7BPqP4
Making reusable backgrounds with 3D models! | Vampbyte

Let me watch this. My focus is low and so is my motivation, but I need to give 2d a honest chance.

https://youtu.be/u0GWW7BPqP4?t=153

I wonder how these 3d scenes can be created for CSP. I got lucky that I picked Blender for doing my room. If I had to parent a subobject, that would be a pain in the ass in Clarisse. If you ignore the huge poly count processing advantages of Clarisse, Blender is better than it in every way possible.

6:40pm. https://youtu.be/_gXlUm_qGdM
Backgrounds with 3D in Clip Studio Paint

Let me check this out.

6:45pm. At this point, I am wondering when the food is going to arrive. I expected it would get here by now.

https://youtu.be/_gXlUm_qGdM?t=9

This is a nice city block. Really buildings can be done with just cubes of various sorts. After kitbashing failed, my desire to do any kind of complex modeling hit an all time low.

7pm. Let have lunch here. It finally arrived.

7:25pm. Done with lunch. Let me finish that video and then I will close for the day. Tomorrow what I am going to do is try the simplest thing possible. I will just use the model as a base and try tracing over it, trying to get to a proper anime character. I'll play around like that.

7:30pm. Focus me. Let me resume the video.

https://youtu.be/_gXlUm_qGdM?t=92

Why do left and right mouse buttons both zoom? I do not know how to rotate with the mouse.

7:40pm. https://youtu.be/_gXlUm_qGdM?t=228

Ah, fuck this. I can't take it anymore. None of this matters for me. Let me just figure out how to use the mouse so it rotates without having to touch the gizmo.

https://www.reddit.com/r/ClipStudio/comments/mmspc7/3d_posing_rant/

I can't find my question anywhere. Let me just ask on the relevant sub.

https://www.reddit.com/r/ClipStudio/comments/vla76o/how_to_rotate_the_3d_camera_using_the_mouse/

I'll get an answer here.

7:50pm. Oh, I did not notice I got a PM by the Scatter author. Nevermind, I might have replied 8h later than I should, but I still got to it.

7:55pm. I am going to close here. Tomorrow I am going to give drawing another shot. This was actually my plan 9 months ago. I was well aware that for most of my needs I can just trace. Me putting effort into 3d, was just me being prideful.

If I look at Royal Road or Scribble Hub, all of those stories basically have no art. There is a huge entreprenurial opportunity for potential artists to ally themselves with the writters, and yet I do not see that happening. It is really a shame, but it also an opportunity. If I do my own art, not to mention music, that will allow me to stand out and reach the top of the charts.

This is playing it smart. If I competed with other artists using art, I'd never get anywhere, but if I competed with writers using art, that would get me somewhere.

Not that I do not have confidence in my writing, the story will be unlike anything those on that site have ever seen before, but more is better. Even if I could win using just writing, that would not be enough for me to develop a path. Only art will allow me to bridge the gap with.

I thought that deep learning had jumped a shark, but diffusion models like DALLE are a crystallization of the field. Deep learning is completely unsuitable for RL, but is exactly suitable for the kind of self supervised learning powering the diffusion models. They mark the end of the first wave.

They will stand out, even in the future when we have efficient brain-like algorithms capable operating in the real world.

I am here so I should grab a piece of that pie. I'd rather compete for that than spend my precious time as a human wage slaving.

8:10pm. Before I close, I want to ask if it is possible to do the manga perspective thing in Blender. Purely out of curiosity rather than need.

https://youtu.be/22DNGGvYy-Y?t=618

I'll post this on the Blender sub. I've never had an answer to any of my questions on /3/.

https://www.reddit.com/r/blender/comments/vlatnb/is_it_possible_to_emulate_clip_studio_paints/

Maybe I should have courage and post some of my own work on this sub? What is the worst that could happen?"

---
## [Will-Bohlen/Paradise](https://github.com/Will-Bohlen/Paradise)@[6082c95eb3...](https://github.com/Will-Bohlen/Paradise/commit/6082c95eb300a9f05b5422060db79f55fe91b9b3)
#### Sunday 2022-06-26 19:01:10 by LightFire53

Relocates The Entertainment Offices and Custodial Closet on DeltaStation (#17480)

* Location, Location, Location!

* Lights and Pipes

I am so sorry for how hacky that disposal piping is

* TFW Disposals

* Oh god, what if there is a fire?!

* And a light switch...

Maybe the final commit? Taking bets on if I managed to forget something else

* If you bet on the requests console

You would be right.

* Bigger, Better, Janitor

* Bloody requests console...

---
## [HorridModz/Pixel-Gun-3D-Resources](https://github.com/HorridModz/Pixel-Gun-3D-Resources)@[2fd4a60bb5...](https://github.com/HorridModz/Pixel-Gun-3D-Resources/commit/2fd4a60bb56f6ce4a61fae4a1f154c74a032aedd)
#### Sunday 2022-06-26 19:27:33 by HorridModz

Add files via upload

Pixel Gun 3D Methods and ClassesRespository by HorridModz (User123456789#6424).
This resource is PUBLIC. You can DISTRIBUTE it to ANYONE with credit.

This respository took tens and tens of hours to make. It is the combined work of searching for every single possible string I could think of and writing down the results.
I am sorry it is so messy. It was meant to be for personal notes, but it became so big! Not everything will do what it's caption says. Most things are untested.

This repository includes:
-Labeled methods, classes, fields, and notes. Most of these are from pixel gun 3d version 16.6.1, 22.3.2, 22.4.0, or 22.4.3.
-Notes about how to find things and deobfuscate them
-Script templates

How to use this repository:
-This is not a tutorial or a mod. It is just a document of my personal notes. This is a resource for hex patching or creating mod menus. If you do not know what you are doing, do not use this.
-Search for a keyword such as "silent aim" or "unlock all"
-Choose one of the methods (or fields or whatever) to use
-Try to find this in the current game version
-Make a mod menu or gameguardian script using the offset
-Test it and see what it does. Feel free to change the caption if it does not do what it said it does. Most don't, as they are untested.

I hope you enjoy using this resource. I can make repositories like this for any game. (Of course,as long as you have an unobfuscated and unprotected version of the game. I'm not going to give you a bunch of free fire hacks xD I'm not that smart.) Tell me if you would like a respository for a certain game.

---
## [dartmouth-outing-club/fyt-bus-packet-generator](https://github.com/dartmouth-outing-club/fyt-bus-packet-generator)@[729604e4b3...](https://github.com/dartmouth-outing-club/fyt-bus-packet-generator/commit/729604e4b32e1dd9824010237a9b50821f6f2bcf)
#### Sunday 2022-06-26 20:03:53 by Alexander Petros

Convert HTML model to ES6 Classes

I caved on this one. Generally speaking I am not a proponent of using
classes because you should not write JavaScript like it's Java, and
functions offer a far more flexible and far less verbose way of
accomplishing many of the same things.

However, in this case, what I need to do is group the storage of some
data (a direction step, a direction leg) with its presentation. I guess
that I could probably create an object with a function and override the
toString prototype, but that's essentially what the ES6 syntax does and
its far less intuitive. I think that in this case not using classes
would be dogmatic and silly.

Shame I have to use the "new" keyword in maps now. Oh well.

---
## [metabase/metabase](https://github.com/metabase/metabase)@[9c4e73899e...](https://github.com/metabase/metabase/commit/9c4e73899e8914fd41e85987d4a652a9b6058d8a)
#### Sunday 2022-06-26 21:00:21 by dpsutton

Enterprise settings (#23441)

* Allow for disabling settings

Disabled settings will return their default value (else nil if no
default is set). This allows us to have enterprise override settings and
use them from regular OSS code without classloaders, extra vars,
remembering to check if the feature is enabled, etc.

Motivating examples are the appearance settings. We allow
`application-font` setting to change the font of the application. This
is an enterprise feature, but anyone can post to
`api/setting/application-font` and set a new value or startup as
`MB_APPLICATION_FONT=comic-sans java -jar metabase.jar` and have the
functionality.

Same thing for application colors in static viz. The calling code just
calls `(settings/application-colors)` and uses them but doesn't check if
the enterprise settings are enabled. To do this correctly, you have to
remember to implement the following onerous procedure:

A whole namespace for a setting
```clojure
(ns metabase-enterprise.embedding.utils
  (:require [metabase.models.setting :as setting :refer [defsetting]]
            [metabase.public-settings :as public-settings]
            [metabase.public-settings.premium-features :as premium-features]
            [metabase.util.i18n :refer [deferred-tru]]))

(defsetting notification-link-base-url
  (deferred-tru "By default \"Site Url\" is used in notification links, but can be overridden.")
  :visibility :internal
  :getter (fn []
            (when (premium-features/hide-embed-branding?)
              (or (setting/get-value-of-type :string :notification-link-base-url)
                  (public-settings/site-url)))))
```

And then in the calling code you have to do the procedure to
conditionally require it and put it behind a var that can handle it
being nil:

```clojure
;; we want to load this at the top level so the Setting the namespace defines gets loaded
(def ^:private site-url*
  (or (u/ignore-exceptions
        (classloader/require 'metabase-enterprise.embedding.utils)
        (resolve 'metabase-enterprise.embedding.utils/notification-link-base-url))
      (constantly nil)))

;; and then the usage
(defn- site-url
  "Return the Notification Link Base URL if set by enterprise env var, or Site URL."
  []
  (or (site-url*) (public-settings/site-url)))
```

Far nicer to just place the following into the regular public-settings
namespace:

```clojure
(defsetting notification-link-base-url
  (deferred-tru "By default \"Site Url\" is used in notification links, but can be overridden.")
  :visibility :internal
  :enabled?    premium-features/hide-embed-branding?)
```

Then no need for a custom namespace to hold this setting, no need to
have an extra var to point to the setting else a fallback value.

Note that this feature is not required on every enterprise feature we
have. We a namespace `metabase-enterprise.sso.integrations.sso-settings`
that has 24 settings in it, all of which are enterprise features. But
these features are used in our enterprise sso offerings and are directly
referenced from the enterprise features. No need for the extra var to
point to them and the flag checks happen in other parts.

* Mark the UI/UX customization settings as requiring whitelabeling

Mark the following settings as requiring
premium-settings/enable-whitelabeling? (aka token check)

- application-name
- loading-message (override of "doing science")
- show-metabot (override of showing our friendly metabot)
- application-colors
- application-font
- application-logo-url
- application-favicon-url

Updates the helper functions for colors to use the setting rather than
feeling entitled to use a lower level `setting/get-value-of-type`. We
need the higher level api so it takes into account if its enabled or
not.

* Move notification-link-base-url into regular settings with enabled?

* Cleanup ns

---
## [DomMcsweeney/Devil-Fuzz](https://github.com/DomMcsweeney/Devil-Fuzz)@[e2ca7b3f07...](https://github.com/DomMcsweeney/Devil-Fuzz/commit/e2ca7b3f07a45ccf11e3775d0005a4c5bf5c53ca)
#### Sunday 2022-06-26 21:33:45 by Dom Mcsweeney

Create README.md

Overdrive / Distortion / Fuzz Pedal Plugin for Windows. 
VST 3 Only 

Install it by downloading it and putting it in your plugins folder of choice.
Controls: 
Hell for Gain
Pain for Tone
Suffering for Volume

Things will change, so don't share this around yet, just enjoy it privately until I give the go ahead to announce it.

---
## [fischerling/wrapdb](https://github.com/fischerling/wrapdb)@[7e69bfce97...](https://github.com/fischerling/wrapdb/commit/7e69bfce97df6ef5d70e556ca4059e8f5f38af3f)
#### Sunday 2022-06-26 21:50:37 by Eli Schwartz

openjp2: Use wrap fallbacks instead of thirdparty

The thirdparty directory provided by upstream contains (old) versions of
projects we already have in the wrapdb. There is zero value in
permitting or encouraging this usage.

Also, the actual dependency lookups suck. e.g. the zlib logic, even when
probing for system versions, tries to find a pkg-config dependency, then
probes for 3 different library names, falls back to subproject() on a
subproject that doesn't exist in the wrap itself, with incorrect usage
of found(), and finally subdirs into the custom copy.

Half of this doesn't work, and all of it is redundant since meson
includes its own robust finder logic that does library probing correctly
in a cross-platform manner under the name... "zlib", just like the
pkg-config dependency.

Furthermore, ***upstream agrees with us***. To quote their own README:

```
This directory contains 3rd party libs (PNG, ZLIB)...

They are convinient copy of code from people outside of the OpenJPEG community.
They are solely provided for ease of build of OpenJPEG on system where those
3rd party libs are not easily accessible (typically non-UNIX).

The OpenJPEG does not recommend using those 3rd party libs over your system
installed libs. The OpenJPEG does not even guarantee that those libraries will
work for you.
```

This is so un-recommended by literally everyone everywhere, that
continuing to provide broken versions here is an intolerable thing.

What upstream wanted, really, was a build system that supported meson wraps.
Then they could have never included a thirdparty directory, but provided
subprojects/*.wrap "solely for ease of build on systems where those libs
are not easily accessible". It's a match made in heaven!

...

Also while we are at it, ditch the commented out copy of astyle, which
was built as an executable because a manually run maintainer shellscript
would execute the forked "openjpstyle" for you. It's totally unneeded by
the wrap, and even if it was considered interesting, it must go through
the standard wrap review && release process.

Move the remaining simple dependency() calls to the subdir that needs
them, which is already guarded by a project option.

Co-authored-by: Xavier Claessens <xavier.claessens@collabora.com>

---

