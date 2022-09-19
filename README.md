## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-09-18](docs/good-messages/2022/2022-09-18.md)


1,928,920 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,928,920 were push events containing 2,522,241 commit messages that amount to 126,508,508 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 31 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[f923f61011...](https://github.com/tgstation/tgstation/commit/f923f6101103e4ff1aeefd57d0531a3bc437a77a)
#### Sunday 2022-09-18 00:28:09 by MMMiracles

Tramstation: Modular Maintenance Insanity (#69000)

About The Pull Request
Every single part of maintenance has been segmented into modules with multiple variants with different themes. As it stands, there are currently 80 modular parts that come together to form the entire maintenance layout for both levels. Part 1 of a 2 part PR set, requires #69486 to have full effect.

Why It's Good For The Game
Maintenance as it stands is a bit barren, not much reason to explore it with boring same-same rooms despite current randomized modules. With these issues in mind, I completely scrapped maintenance as it was and rebuilt it in mind with full modular segments with proper documentation on what each piece is and where it is located. These changes were also designed to make maintenance more friendly for our dark-dwelling antags and xenos alike, as each major module now has an air vent and scrubber.

Fixes #68320

Main Event:

Every single part of maintenance was turned into module chunks. Sections of the map that originally had maintenance was traced out with checkered flooring so mappers can still see the general layout of the tunnels when making larger edits.
Every module has been documented with proper nodes with descriptions of where each module is located on the map.
Each main module has a regular variant and an abandoned variant. Abandoned variants have blocked access routes and look more like unfinished carved out tunnels than regular maintenance.
Each module has 2 attachment points barring 2. Each attachment has 3 potential layouts that are chosen each round. A storage room with construction supplies one round might be a carved out room with minerals the next.
QoL/General Fixes:

Maintenance should have much more xeno/antag spawns to give various mid-round antags better chances at starting.
Camera network has been given a once-over with duplicate/floating cameras fixed.
The helpful bots in the lower tunnel should now actually do full rotations instead of whatever the hell they were doing before.
I still need to do some testing with disposals and final touch ups to make sure there aren't any weird overlaps, but as of right now the actual mapping quality is ready for review.

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[4c8cfb57aa...](https://github.com/pytorch/pytorch/commit/4c8cfb57aa3ac58112efb693635198b07edf008f)
#### Sunday 2022-09-18 01:08:49 by Edward Z. Yang

Convert SymInt tracing to mode based tracing (#83380)

We're on our way to deleting ProxyTensor entirely (see https://github.com/pytorch/pytorch/pull/83330 ), but before we can do that, we have to delete ProxySymInt first. Here's the plan.

Changes in torch.fx.experimental.symbolic_shapes

* The general idea is to do mode based tracing. This means we need a mode that can interpose on all SymInt operations. There are a few ways to do this, but I've done it the easy way: (1) I have a separate mode for SymInt operations specifically called SymDispatchMode, and (2) this mode operates on PySymInt (and not the basic SymInt which is user visible). I elided Int from the name because if we add SymFloats I want to use the same mode to handle those as well, and I used Dispatch rather than Function because this is the "inner" dispatch operating PySymInt and not SymInt (this is not a perfect analogy, but SymFunctionMode definitely seemed wrong as you still must go through the C++ binding.) The mode is entirely implemented in Python for ease of implementation. We could have implemented this more symmetrically to TorchFunctionMode in C++, but I leave that as later work; this API is unlikely to get used by others (unlike TorchFunctionMode). One downside to not doing the mode in C++ is that we still have to do the hop via a preexisting PySymInt to wrap; this is currently not a big deal as conversion to SymInts only really happens when there is already another SymInt floating around. SymDispatchMode is pared down from TorchDispatchMode; there is no ancestor tracking since I don't expect people to be mixing up SymDispatchModes.
*  I made some improvements for tracing. When I invoke the SymDispatchMode handler, I would like constants to show up as constants, so they can be directly inlined into the FX graph (rather than going through a wrapping process first, and then the wrapped SymInt being used in the operation). To do this, I directly track if a PySymInt is a constant at construction time. Only wrapped PySymInts are constants.
* For convenience, PySymInts now support all magic methods that regular SymInts do. This is so that redispatch inside the SymDispatchMode can be written the idiomatic way `func(*args, **kwargs)` where func is an operator. The original names are retained for direct C++ calls.

Changes in torch.fx.experimental.proxy_tensor

* OK, so we got a new SymDispatchMode, so we define a ProxySymDispatchMode and activate it when we start tracing. This mode is currently unconditionally activated although technically we only need to activate it when doing symbolic tracing (it doesn't matter either way as there are no SymInts if you are not doing symbolic tracing).
* We delete ProxySymInt. To do this, we must now record the proxy for the SymInt some other way. Based on discussion with Chillee, it is more intuitive to him if the proxies are still recorded on the SymInt in some way. So we store them in the `__dict__` of the PySymInt, indexed by Tracer. An improvement is to make this a weak map, so that we remove all of these entries when the tracer dies. In an original version of this PR, I keyed on the mode itself, but tracer is better as it is accessible from both modes (and as you will see, we will need to fetch the map from both the ProxySymDispatchMode as well as the ProxyTorchDispatchMode.) The implementation of SymDispatchMode now simply retrieves the proxies, performs the underlying operation as well as the FX graph recording, and then records the output proxy to the PySymInt. Note that FX tracing does not work with proxies and SymInts, so we manually call `call_function` to ensure that the correct operations get recorded to the graph. This means conventional FX retracing with proxies only will not work with these graphs, but there wasn't really any reason to do this (as opposed to `make_fx` retracing) anyway. Constants are detected and converted directly into Python integers.
* SymInts can show up as arguments to tensor operations, so they must be accounted for in ProxyTorchDispatchMode as well. This is done by searching for SymInt arguments and converting them into proxies before the proxy call. This can be done more efficiently in a single `tree_map` but I'm lazy. The helper `unwrap_symint_proxy` conveniently implements the unwrapping in one place given a tracer; unfortunately it cannot be shared with SymDispatchMode as SymDispatchMode gets PySymInts, but ProxyTensorMode gets SymInts. Similarly, tensors that are returned from tensor operations can have SymInts in their shapes, which need fresh proxies allocated. To avoid leaking internal details of SymInt shape computation to the tensor operation graph, these SymInts are always given proxies derived from `x.size(dim)` call on their return tensor. We also need to do this for strides and numel but have not done so yet. Furthermore, we must avoid tracing internal SymInt calls while we run meta operations on the true operation; this is achieved by also disabling SymInt tracing on the inside of tensor tracing. This is analogous to how tensor tracing is disabled inside the implementation of tracing mode, but unfortunately we are unable to use the same mechanism (this would have been easier if the two modes could be combined somehow, and I am amenable to suggestions to try harder to achieve this.)
* Because there are no more ProxySymInts, we no longer need to do anything to unwrap SymInt. Furthermore, we do not need to reallocate ProxySymInts on class creation.
* If a bare SymInt without a Proxy is encountered, it is assumed that this must be a constant. `create_arg` handles this case. Non-constant free SymInts result in an assert error.
* The initial input handling in `dispatch_trace` involves traversing all of the input tensors, traversing over their shapes, and assigning proxies for the SymInts in shapes in the same way we handle proxies for the output tensors.

The preexisting testing is inadequate but will be better after I rebase past https://github.com/pytorch/pytorch/pull/82209

Signed-off-by: Edward Z. Yang <ezyang@fb.com>
Pull Request resolved: https://github.com/pytorch/pytorch/pull/83380
Approved by: https://github.com/samdow

---
## [dwasint/MonkeStation](https://github.com/dwasint/MonkeStation)@[31c9d411a7...](https://github.com/dwasint/MonkeStation/commit/31c9d411a7b9e4f6ad66b930d535e24e5555bd06)
#### Sunday 2022-09-18 01:48:23 by nednaZ

Dynamic Adjustments Part 2 (#627)

* Dynamic Changes II

Changes the intercept message to be more flavorful.

Clamps the threat level to between 75% player pop and 200% player pop.

Logs increases to Dynamic threat budget.

Slightly reduces the weight of latejoin traitors. (From 7 to 4)

Increases the Weight (2 to 4), decreases the Cost (40 to 20) and decreases Minimum Players (35 to 30) of Revolution Latejoins.

Restores Heretics to Latejoin and Roundstart.

Heretics now have a lower number of sacrifice objectives. (From 2-6 to 1-3)

Heretics now have a chance to get a Steal objective.

Dynamic Abductors may no longer get spawned  in solo by mistake.

Midround Traitor chance reduced. (From 7 to 5)
Midround Traitor cap reduced. (From player_count / 10 to player_count / 15)

Midround Wizard weight increased (From 1 to 3)
Midround Wizards are now a HIGH_IMPACT_RULESET and will not repeat.

Midround Nuclear Operative Weight reduced. (From 5 to 4)

Blob Weight (4 to 3) and Cost (10 to 25) changed.

Xenomorph Cost increased (10 to 25)

Nightmare Cost increased (10 to 15)

Abductor Cost increased (10 to 15)

Space Pirates added to Dynamic.

Space Pirates have been given an update, with ship names and support for multiple types of pirates existing.

Revenant added to Dynamic.

Obsessed added to Dynamic.

Space Dragon early start changed to 40 minutes (From 50 minutes)

Roundstart Traitor cost increased (7 to 8)

Blood Brother Weight (4 to 2), Cost(15 to 13) and Scaling Cost(15 to 13) adjusted.

Changeling Weight(3 to 4) and Cost(15 to 17) adjusted.

Roundstart Wizard Weight(2 to 5) and Cost(40 to 30) adjusted.

Blood and Clock Cult Weight and Cost(30 to 25) adjusted.

Nuclear Operatives Weight(3 to 4) and Cost(50 to 25) adjusted.

* lone op

why didn't this commit

* Reverts max_traitors change

The maximum number of traitors is now player_count / 10 rather than 15

* Revolution Tweaks

Reduces the weight of latejoin revs from 4 to 2.

Increases the minimum number of required enemies from 2-0 to 5.

Changes the required enemies to be only security and the captain, AI and Cyborg are not counted.

The shuttle is no longer automatically called upon a Revolution victory.

There will be an announcement made after either 30% of the station is converted into revolutionaries OR if two heads of staff are killed.

* Pirate Fixes

Pirates now function as intended in Dynamic.

Pirates have a 25 player minimum to be called as antagonists.

Pirates have a minimum of 2 enemies before they can be called.

* Faster than opening VSC.

---
## [leandroppf/otservbr-global-laundtaund](https://github.com/leandroppf/otservbr-global-laundtaund)@[fbd70d116c...](https://github.com/leandroppf/otservbr-global-laundtaund/commit/fbd70d116c260a94902c2e0164ceca94023f2f28)
#### Sunday 2022-09-18 01:55:07 by rigis1

Fixes and add blood brothers quest till mission 4 (#753)

Fix:
• electric sparks
• baking
• filling fluids container
• the hunt for the sea serpent quest

Add:
• questlog entry for blood brothers quest, the hunt for the sea serpent quest and grave danger quest
• storages for blood brothers quest, the hunt for the sea serpent quest and grave danger quest
• keywords for blood brothers quest, the hunt for the sea serpent quest and grave danger quest
• condition to harlow travel to vengoth
• holy water to henricus shop
• food for blood brothers quest
• spawn npc ortheus and jack springer, monster gaffir
• npc jack springer 
• ugly monster loot
• events to gaffir and ugly monster
• ice cracking
• basic events for bosses Sir Nictros and Sir Baeloc
• basic spawn boss for levers
• access to falcon bastion

---
## [walternewtz/android_kernel_xiaomi_sdm845](https://github.com/walternewtz/android_kernel_xiaomi_sdm845)@[90ff21e3ff...](https://github.com/walternewtz/android_kernel_xiaomi_sdm845/commit/90ff21e3ffceb2daca7b63105caa3f9ae93cffff)
#### Sunday 2022-09-18 02:04:43 by tanish2k09

Introducing KLapse - A kernel level livedisplay module v4.0:

Author: @tanish2k09 (email: tanish2k09.dev@gmail.com)

What is it?
Kernel-based Lapse ("K-Lapse") is a linear RGB scaling module that 'shifts' RGB based on time (of the day/selected by user), or (since v2.0) brightness. This concept is inspired from
LineageOS (formerly known as 'CyanogenMod') ROM's feature "livedisplay" which also changes the display settings (RGB, hue, temperature, etc) based on time.

Why did you decide to make this? (Tell me a story).
I (personally) am a big fan of the livedisplay feature found on LineageOS ROM. I used it every single day, since Android Lollipop. Starting from Android Nougat, a native night mode
solution was added to AOSP and it felt like livedisplay was still way superior, thanks to its various options (you could say it spoiled me, sure). I also maintained a kernel (Venom
kernel) for the device I was using at that time. It was all good until the OEM dropped support for the device at Android M, and XDA being XDA, was already working on N ROMs. The issue
was, these ROMs weren't LineageOS or based on it, so livedisplay was... gone. I decided I'll try to bring that feature to every other ROM. How would I do that? Of course! The kernel! It
worked on every single ROM, it was the key! I started to work on it ASAP and here it is, up on GitHub, licensed under GPL (check klapse.c), open to everyone :)

How does it work?
Think of it like a fancy night mode, but not really. Klapse is dependent on an RGB interface (like Gamma on MTK and KCAL on SD chipsets). It fetches time from the kernel, converts it to
local time, and selects and RGB set based on the time. The result is really smooth shifting of RGB over time.

How does it really work (dev)?
Klapse mode 1 (time-based scaling) uses a method void klapse_pulse(void) that should ideally be called every minute. This can be done by injecting a pulse call inside another method that
is called repeatedly naturally, like cpufreq or atomic or frame commits. It can be anything, whatever you like, even a kthread, as long as it is called repeatedly naturally. To execute
every 60 seconds, use jiffies or ktime, or any similar method. The pulse function fetches the current time and makes calculations based on the current hour and the values of the tunables
listed down below.

Klapse mode 2 (brightness-based scaling) uses a method void set_rgb_slider(<type> bl_lvl) where is the data type of the brightness level used in your kernel source. (OnePlus 6 uses u32
data type for bl_lvl) set_rgb_slider needs to be called/injected inside a function that sets brightness for your device. (OnePlus 6 uses dsi_panel.c for that, check out the diff for that
file in /op6)

What all stuff can it do?

1, Emulate night mode with the proper RGB settings
2, Smoothly scale from one set of RGB to another set of RGB in integral intervals over time.
3, Reduce perceived brightness using brightness_factor by reducing the amount of color on screen. Allows lower apparent brightness than system permits.
4, Scale RGB based on brightness of display (low brightness usually implies a dark environment, where yellowness is probably useful).
5, Automate the perceived brightness independent of whether klapse is enabled, using its own set of start and stop hours.
6, Be more efficient,faster by residing inside the kernel instead of having to use the HWC HAL like android's night mode.
7, (On older devices) Reduce stuttering or frame lags caused by native night mode.
8, An easier solution against overlay-based apps that run as service in userspace/Android and sometimes block apps asking for permissions.
9, Give you a Livedisplay alternative if it doesn't work in your ROM.
10, Impress your crush so you can get a date (Hey, don't forget to credit me if it works).

Alright, so this is a replacement for night mode?
NO! Not at all. One can say this is merely an alternative for LineageOS' Livedisplay, but inside a kernel. Night mode is a sub-function of both Livedisplay and KLapse. Most comparisons
here were made with night mode because that's what an average user uses, and will relate to the most. There is absolutely no reason for your Android kernel to not have KLapse. Go ahead
and add it or ask your kernel maintainer to. It's super-easy!

What can it NOT do (yet)?

1, Calculate scaling to the level of minutes, like "Start from 5:37pm till 7:19am". --TODO
2, Make coffee for you.
3, Fly you to the moon. Without a heavy suit.
4, Get you a monthly subscription of free food, cereal included.

All these following tunables are found in their respective files in /sys/klapse/

1. enable_klapse : A switch to enable or disable klapse. Values : 0 = off, 1 = on (since v2.0, 2 = brightness-dependent mode)
2. klapse_start_hour : The hour at which klapse should start scaling the RGB values from daytime to target (see next points). Values : 0-23
3. klapse_stop_hour : The hour by which klapse should scale back the RGB values from target to daytime (see next points). Values : 0-23
4. daytime_rgb : The RGB set that must be used for all the time outside of start and stop hour range.
5. target_rgb : The RGB set that must be scaled towards for all the time inside of start and stop hour range.
6. klapse_scaling_rate : Controls how soon the RGB reaches from daytime to target inside of start and stop hour range. Once target is reached, it remains constant till 30 minutes before
   stop hour, where target RGB scales back to daytime RGB.
7. brightness_factor : From the name itself, this value has the ability to bend perception and make your display appear as if it is at a lesser brightness level than it actually is at.
   It works by reducing the RGB values by the same factor. Values : 2-10, (10 means accurate brightness, 5 means 50% of current brightness, you get it)
8. brightness_factor_auto : A switch that allows you to automatically set the brightness factor in a set time range. Value : 0 = off, 1 = on
9. brightness_factor_auto_start_hour : The hour at which brightness_factor should be applied. Works only if #8 is 1. Values : 0-23
10. brightness_factor_auto_stop_hour : The hour at which brightness_factor should be reverted to 10. Works only if #8 is 1. Values : 0-23
11. backlight_range : The brightness range within which klapse should scale from daytime to target_rgb. Works only if #1 is 2. Values : MIN_BRIGHTNESS-MAX_BRIGHTNESS

Signed-off-by: Eliminater74 <eliminater74@gmail.com>
Signed-off-by: energyspear17 <energyspear17@gmail.com>
Signed-off-by: Michael <loukerismichalis@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>

---
## [Jackraxxus/tgstation](https://github.com/Jackraxxus/tgstation)@[ad01ab5ed0...](https://github.com/Jackraxxus/tgstation/commit/ad01ab5ed0a5f80278076b1e0e6ac33fe73b0e32)
#### Sunday 2022-09-18 02:31:00 by LemonInTheDark

Fixes asset caching (#69852)

The asset was being loaded, seeing that fully_generated is false, so it
attempts to rebuild. The rebuilding clears the existing file cache, and
fucks us.

Life is pain.

---
## [ShreyJ1729/SnapFit](https://github.com/ShreyJ1729/SnapFit)@[846a907571...](https://github.com/ShreyJ1729/SnapFit/commit/846a9075716b3704ab79f4e0a88a258b4d434a42)
#### Sunday 2022-09-18 04:06:39 by Shrey Joshi

fuck this shit ive been up too long and i fucking hate coding

---
## [sakura-knoll/abyss-lab](https://github.com/sakura-knoll/abyss-lab)@[b12080127f...](https://github.com/sakura-knoll/abyss-lab/commit/b12080127fe20b19f7c66ce0af1fd0807f865396)
#### Sunday 2022-09-18 05:14:08 by Sem104

Update scene-4-00.xml (#230)

* Update scene-4-00.xml

* Fix syntax error

* Update scene-4-00.xml

* Update scene-4-00.xml

There's a backspace still missing between the last "pain" and "endless recovery, endless pain"

Tried to fix in last branch too but didn't work, this time should (I hope) cuz there was a [\s] that shouldn't have been there cuz the two things were already separated by mono-mono

Didn't affect the VN but maybe was the cause the backspace isn't showing...

If you know how, feel free to modify, I'm hoping this is the last time I see this scene

* Backspace error (yet again)

The backspace still doesn't appear, let's see if this is the right way or else I'm out of ideas and we'll just leave it at that... T_T

* Update scene-4-00.xml

Think I got how to trigger that backspace (the 2 sentences were separated by mono-mono but the second one wasn't a "pageend" one so it should be fine to just unify the paragraphs only leaving aside the last one with the end of the page

Also centered the other line you see modified because it was too high before and there was too much space below.

Hope it's finally done now

* Finally we're done

YESSSSSSSSSSSSSSSSSSSSSSSSS, THE LAST CHANGE WORKED

We were only missing the spacebar/mouse click input "[ \ s ]" cuz I didn't think about it yesterday but hell fucken yeah chapter 0 is finally done

Co-authored-by: Sakura Knoll <s4kura.knoll@gmail.com>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[a4bfe65cb1...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/a4bfe65cb1caece1e3e6a4635fa17d39f1aa3478)
#### Sunday 2022-09-18 05:45:53 by SkyratBot

[MIRROR] Dimensional Anomaly [MDB IGNORE] (#15974)

* Dimensional Anomaly (#69512)

About The Pull Request

Everyone has been asking: "When will there be an anomaly like the bioscrambler, but for the space station? Please, we need more things which replace objects with different objects from the same typepath."
Well I made it and it looked like ass because non-tiling floor and walls look terrible, so then I made this instead.
Dimensional.mp4

The "dimensional anomaly" shifts matter into a parallel dimension where objects are made out of something else.
Like the Bioscrambler anomaly, it does not expire on its own and only leaves when someone signals it or uses an anomaly remover.
When it spawns it picks a "theme" and converts terrain around it until it covers a 7x7 square, then it teleports somewhere else and picks a new theme.

A lot of these themes are relatively benign like "meat", "fancy carpet", or "gold". Some of them are kind of annoying like "icebox" because it creates floor which slows you down, or "clown" because bananium is intentionally annoying. Some of them are actively dangerous, mostly "uranium" and "plasma".
The main problem this will usually cause for crewmembers is decreasing area security. When it replaces doors it replaces them with ones which don't have any access control, and it will also replace RWalls with normal and much more vulnerable walls which will make breaking and entering significantly easier until someone has taken the time to fix the damage. But also sometimes it will irradiate them, you never know.

The fact that sometimes the changes are benign (or provide uncommon materials) and might be happening in places you don't care about access to might encourage people to push their luck and leave it alone until it starts turning the captain's office into a bamboo room or repainting medbay a fetching shade of flammable purple, which I would consider a success.
Armour.mp4

If you successfully harvest the anomaly core you can place it into the reactive armour to get Reactive Barricade Armour, which shifts your dimension when you take damage and attempts to place some randomised (not terribly durable) objects between you and hopefully your attacker (it really just picks up to four random unoccupied tiles next to you). If you're EMPed then the changes it make to the environment will often be as unpleasant for you as they are for a pursuer, and significantly more likely to harm both of you rather than just provide obstacles.

Other changes:
I split anomalies out into their own dmi file, seems to be all the rage lately.
I moved the anomaly placing code into a datum instead of the event because I wanted to reuse it but if you have a better idea about where I could have put it let me know.
This also fixes a bug where the material spreader component wasn't working when I applied plasma materials to something, the extra whitespace was parsing as another argument for some reason and meant it would runtime.
Supermatter delamination was still pointing to Delimber anomalies instead of Bioscrambler.

* Dimensional Anomaly

* Fixes the upstream merge skew

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>
Co-authored-by: GoldenAlpharex <jerego1234@hotmail.com>

---
## [Tiktodz/android_kernel_asus_sdm636](https://github.com/Tiktodz/android_kernel_asus_sdm636)@[3918e02a7b...](https://github.com/Tiktodz/android_kernel_asus_sdm636/commit/3918e02a7b63206b7c79126c761892efb7d58469)
#### Sunday 2022-09-18 07:08:42 by Angelo G. Del Regno

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

Signed-off-by: Kneba <abenkenary3@gmail.com>
Signed-off-by: Tiktodz <kuplemarkeple@gmail.com>

---
## [nicolajlinde/indiegems](https://github.com/nicolajlinde/indiegems)@[e099f89dcd...](https://github.com/nicolajlinde/indiegems/commit/e099f89dcdb962dc6f96b8536753c4747ccefc9e)
#### Sunday 2022-09-18 08:26:56 by Nicolaj Linde

Swicthing to my Mac to save power because of that goddamn idiot Putin. Fuck him.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[cd1dc25eb2...](https://github.com/treckstar/yolo-octo-hipster/commit/cd1dc25eb241953a4bb07ae23768a823a1ef03e3)
#### Sunday 2022-09-18 11:22:02 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [ProjectVelvet/android_kernel_sm6250](https://github.com/ProjectVelvet/android_kernel_sm6250)@[71bdd7f9c3...](https://github.com/ProjectVelvet/android_kernel_sm6250/commit/71bdd7f9c356cfd0d1af138999a2286c65c82f22)
#### Sunday 2022-09-18 12:19:32 by Maciej Żenczykowski

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
Signed-off-by: Excalibur-99 <txexcalibur99@gmail.com>

---
## [Caldony/lobotomy-corp13](https://github.com/Caldony/lobotomy-corp13)@[f490a226b2...](https://github.com/Caldony/lobotomy-corp13/commit/f490a226b241795abefbddeb84938af4e183b2a8)
#### Sunday 2022-09-18 13:46:01 by Gelatelly

sassy shepherd

makes shepherd lie like the bitch he is

I HATE RUNTIMES I HATE RUNTIMES I HATERUNTIMES

use the shittiest method in existence to bypass runtimes, unfortunately I couldn't use initial() without adding some issues so fuck me I guess

updates the people and abno list

imagine using signalers

why is there a huge gap there

leftovercode that doesn't do anything

linter fix?

this is the worst fix I hate linters so much

I'm making everything worse by trying to fix it

send help

adds abno spawn signaller

I love adding signallers for meme PR

changes how the lists are used/rename a few things

SLightCamelCaseChange

clears the people_list on destroy()

this isn't much but it should avoid some problems

moves the abno spawn signal to lobotomy_corp.dm

---
## [Caldony/lobotomy-corp13](https://github.com/Caldony/lobotomy-corp13)@[f0e6476eb0...](https://github.com/Caldony/lobotomy-corp13/commit/f0e6476eb051d781f7e4d0be7976dff0ff72fda0)
#### Sunday 2022-09-18 13:46:01 by Lance

The Great Workening

Attribute Levels Displayed

No thoughts were had, thoughts injected.

Attribute Levels go brrr

Requested Change Made

WHOOPS WRONG PARENTHESIS

I swear I know how Clamps work

Holy shit how did this not get found out earlier

---
## [eldoriarpg/BloodNight](https://github.com/eldoriarpg/BloodNight)@[481469737b...](https://github.com/eldoriarpg/BloodNight/commit/481469737ba019f30d7165e1924636db3d3e1e43)
#### Sunday 2022-09-18 14:10:30 by MinerCoffee

Knight Zombie Boss (#115)

* I have added a new boss called KnightZombie. It has special properties to block the player's attack and can push them two blocks higher. I have also added custom drops to this mob. It includes Iron nuggets, experience bottles, and rotten flesh. They all have a chance to get to a random drops.

* Update BloodNight-core/src/main/java/de/eldoria/bloodnight/specialmobs/mobs/zombie/KnightZombie.java

Co-authored-by: Lilly Tempest <46890129+RainbowDashLabs@users.noreply.github.com>

* Update BloodNight-core/src/main/java/de/eldoria/bloodnight/specialmobs/mobs/zombie/KnightZombie.java

Co-authored-by: Lilly Tempest <46890129+RainbowDashLabs@users.noreply.github.com>

* Optimized and changed events.

* Moved actions around to fit the corresponding events.

* Fixed player velocity to get launched. The player.getVelocity does not work how I want to. I changed it to setVelocity as it functions how it should. Fixed timings for the events. Everything works as expected.

Co-authored-by: Lilly Tempest <46890129+RainbowDashLabs@users.noreply.github.com>

---
## [mosra/magnum-integration](https://github.com/mosra/magnum-integration)@[8fdf1479bf...](https://github.com/mosra/magnum-integration/commit/8fdf1479bf01109d4171ba43496eea9578c120b0)
#### Sunday 2022-09-18 15:13:02 by Vladimír Vondruš

package/archlinux: don't build DartIntegration in the dev PKGBUILD.

I'm tired of this thing. The libdart package is in AUR and depends on
a fractal consisitng of about 90 packages, including OSG, blas, TBB and
lapack, many of which take 30+ GB RAM to build and include tests and all
other crap. And then, once I suffer through all that, it will crash
right after start because *the damn thing* sends unaligned allocations
to Eigen AVX code, blowing up.

No. Enough suffering. Not worth my time. The only place where this thing
is built is on a single CI job, and even that is painful. DART has to
fix its dependency tree, it's not my job to do that for them.

---
## [rjbs/Synergy](https://github.com/rjbs/Synergy)@[abf374a916...](https://github.com/rjbs/Synergy/commit/abf374a916afc7a7a6e9a783e15377f6d5386c19)
#### Sunday 2022-09-18 15:39:01 by Ricardo Signes

WIP: a new rototron engine

This is not perfect, or probably even 10 years perfect, but I think it's
a big improvement, and should be pretty easy to finish delivering.

The old rototron worked like this:

    every week has a Weeks Since Epoch number, WSE

    every rotor has a list of workers

    for each rotor:
      candidate-list = all workers for rotor, deterministically sorted

      for each day in the week being scheduled:
        CANDIDATE: until scheduled or worker list exhausted:
          candidate = delete candidate-list[ WSE % candidate-list.size ]

          if candidate is unavailable or on leave
            next CANDIDATE

GOOD:  Because the WSE number is stable within a week, the first choice
for any day in the week is the same, as is the second.  That means a
week will favor being one person.  If that person is not available for 2
days, the same person is likely to be fallback.

BAD:  Not too much prevents week 1's first choice from being week 2's
second choice, meaning the odds of getting two weeks in a row, when
somebody is out for a week, are poorly defined.  (Insert link to number
theory about coprimality here.)

BAD:  Rotors are entirely unaware of each other, so nothing much
prevents someone being assigned three rotations in a week.

The new rototron (not fully implemented yet) works like this:

    every week has a Weeks Since Epoch number, WSE

    every rotor has a map of workers to fixed preference¹

    every rotor-worker has a level of rotor-fatigue²

    ROTOR: for each rotor:
      for every worker in worker map:
        if worker has any other rotor assignment in this date range:
          mark worker as one level less preferable

      for every level of preferability:
        select set of workers available on the most days³

        for each worker in this set:
          select set of workers with the lowest rotor-fatigue

          candidate = set[ WSE % set.size ]

          schedule candidate for all available dates in range

          redo ROTOR with unscheduled days

1: Preference is a number.  The lower the preference number, the more
   likely someone is to be scheduled.  Thing of preference:1 as being
   "first string".  For most rotors, the usual plumbers will all have
   preference 1, and I (rjbs) might have preference 3.  For escalation,
   a full-time escalation handler would have preference 1, and most
   everyone else preference 2.

2: I bet we'll want to adjust how rotor fatigue works, but right now
   your level of rotor fatigue is the number of days you were on
   rotation in the last 90 days.  This builds up every time you're on
   duty, and fades off over time.

3: If everybody is available all week, the set is everybody.  If two
   people are out one day, it's everybody but those two.  If everybody
   is out exactly one day, it's everybody again.

Rotor fatigue probably has two problems.  First, if a rotation is done
by one person for 90d and then a second person is added to rotation with
the same preference, they'd be on rotation 45d before getting a break.
be on rotation for 45d straight.  Second, it's per-rotor, which may or
may not be noticeable over time.  Still, it should be easy to adjust its
behavior over time, and this was easy to implement.

The next likely steps are:

1.  Replace the availability checker callback with something acting kind
    of or exactly like the AvailabilityChecker class in Rototron1.

2.  Treat the rototron's own schedule (persisted in SQLite or something)
    as canonical, with the JMAP duty roster calendar treated as a
    published copy.

---
## [fartdev/Coffee](https://github.com/fartdev/Coffee)@[2b68c0f038...](https://github.com/fartdev/Coffee/commit/2b68c0f038353dbbc086fee19ab9146877eade91)
#### Sunday 2022-09-18 16:19:35 by 0x3C50

been a while
- remove viafabric's new warning for girlboss, guardian or nochatreports being installed
- add girlboss into the client directly
fuck you kenny you know what you did

---
## [marnixah/Schwi](https://github.com/marnixah/Schwi)@[eb58a4927a...](https://github.com/marnixah/Schwi/commit/eb58a4927a244537bcea3f8c21a6c670ed3099bb)
#### Sunday 2022-09-18 16:21:42 by marnixah

fix(homeassistant): :ambulance: I fucking hate python's dependency tracking "solution" it's so ass and only leads to problems

---
## [system-zero/system-zero](https://github.com/system-zero/system-zero)@[f2b3a0867e...](https://github.com/system-zero/system-zero/commit/f2b3a0867ea68e6190ed99ceb2a0da3aea6bb699)
#### Sunday 2022-09-18 16:25:10 by why not not

But before we go, this is the very old good code from par:

https://bitbucket.org/amc-nicemice/par/src/master

This is an almost untouchable copy all of the original par code actual algorithm,
merged into a single unit and the functionality exposed as a library.

We use an instance and pass this to the functions as their first argument,
and we exposed this without hiding anything from the user (for flexibity).

However (for now) only the functions that expose functionality, changed their
signature and use this instance.

This is to keep as much of the original code with the exact way it was written,
so nothing has really been changed or removed (except the duplicated headers).

However the main function has been removed, but it is possible to use the (perhaps
known) exact same syntax par's command line interface, passed as an array of strings
to the exposed function (so to mimic and implemented the original standard behavior).

Usage:

  par_t *this = par_new ()
  par_parse_argv (this, array of strings)
  int par_main (this, string type input)

and

  var q = {
    just     : ifwewanttojust  # by default yes
    width    : ourwidth        # by default 78
    tabwidth : tabidth         # by default 8
  }

  var p = Par.new (; q)

  var argv = ["P=*-`_s#"]
  Par.parse_argv (p, argv)

  var s = some_string
  var r = Par.process (p, s; tostdout)  # without the tostdout qualifier this returns a string

also to see the corresponded options above issue from our shell:

  Par --help

and as an example, you may try:

  Par --just --arg=P=*-`_s#  README.md
    # you may need to escape some of the P option chars on another shell

  see par.doc for documantation and for their many many details!

As an inner deep expression which i would like to share , i feel that i've
been very lucky:

  - to read this very old code
  - to see it compiled by modern compilers in C11 without a single warning
    and turning on agrressive warnings
  - for the so many detailed comments
  - to read the documantation and laugh with the author about his apologies
    i'm totally sure that he should be very fine kind of a human being
  - and ... is very fast

so I feel to owe a way too much appreciation for this gift, many many thanks.

---
## [ethDreamer/lighthouse](https://github.com/ethDreamer/lighthouse)@[66eca1a882...](https://github.com/ethDreamer/lighthouse/commit/66eca1a88218462235cb76a116dc3c6a1853444f)
#### Sunday 2022-09-18 17:30:31 by Michael Sproul

Refactor op pool for speed and correctness (#3312)

## Proposed Changes

This PR has two aims: to speed up attestation packing in the op pool, and to fix bugs in the verification of attester slashings, proposer slashings and voluntary exits. The changes are bundled into a single database schema upgrade (v12).

Attestation packing is sped up by removing several inefficiencies: 

- No more recalculation of `attesting_indices` during packing.
- No (unnecessary) examination of the `ParticipationFlags`: a bitfield suffices. See `RewardCache`.
- No re-checking of attestation validity during packing: the `AttestationMap` provides attestations which are "correct by construction" (I have checked this using Hydra).
- No SSZ re-serialization for the clunky `AttestationId` type (it can be removed in a future release).

So far the speed-up seems to be roughly 2-10x, from 500ms down to 50-100ms.

Verification of attester slashings, proposer slashings and voluntary exits is fixed by:

- Tracking the `ForkVersion`s that were used to verify each message inside the `SigVerifiedOp`. This allows us to quickly re-verify that they match the head state's opinion of what the `ForkVersion` should be at the epoch(s) relevant to the message.
- Storing the `SigVerifiedOp` on disk rather than the raw operation. This allows us to continue track the fork versions after a reboot.

This is mostly contained in this commit 52bb1840ae5c4356a8fc3a51e5df23ed65ed2c7f.

## Additional Info

The schema upgrade uses the justified state to re-verify attestations and compute `attesting_indices` for them. It will drop any attestations that fail to verify, by the logic that attestations are most valuable in the few slots after they're observed, and are probably stale and useless by the time a node restarts. Exits and proposer slashings and similarly re-verified to obtain `SigVerifiedOp`s.

This PR contains a runtime killswitch `--paranoid-block-proposal` which opts out of all the optimisations in favour of closely verifying every included message. Although I'm quite sure that the optimisations are correct this flag could be useful in the event of an unforeseen emergency.

Finally, you might notice that the `RewardCache` appears quite useless in its current form because it is only updated on the hot-path immediately before proposal. My hope is that in future we can shift calls to `RewardCache::update` into the background, e.g. while performing the state advance. It is also forward-looking to `tree-states` compatibility, where iterating and indexing `state.{previous,current}_epoch_participation` is expensive and needs to be minimised.

---
## [SurlyMae/surlymae.github.io](https://github.com/SurlyMae/surlymae.github.io)@[a77c996586...](https://github.com/SurlyMae/surlymae.github.io/commit/a77c9965866ea39e6a5ec5aeee6273ef4bb898cf)
#### Sunday 2022-09-18 17:33:25 by firstName lastName

Merge pull request #3 from SurlyMae/mobile-first

stupid git troubleshooting hate you sometimes git

---
## [sjp38/linux](https://github.com/sjp38/linux)@[69337fce08...](https://github.com/sjp38/linux/commit/69337fce08d23d3435a14d8ffbf0fe51975abec3)
#### Sunday 2022-09-18 17:38:53 by Johannes Weiner

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
## [donategifts/ts-backend](https://github.com/donategifts/ts-backend)@[5c1228dc25...](https://github.com/donategifts/ts-backend/commit/5c1228dc253cb7870a330e8e9b7c1021bdf2f0fe)
#### Sunday 2022-09-18 19:07:12 by Patric

Card magic (#19)

* Lots of address related shit

* fucking card stuff

* fucking card stuff

Co-authored-by: gnorbsl <ph@mycraftnote.de>

---
## [SebassTehFish/SeptemberJam2022](https://github.com/SebassTehFish/SeptemberJam2022)@[f4529075a4...](https://github.com/SebassTehFish/SeptemberJam2022/commit/f4529075a49f626b43f4664a392a352025925e4e)
#### Sunday 2022-09-18 19:27:39 by Orionicles

FUCKFUCKFUCK

ldtk is my literal nightmare. I am going to strangle Cammin. God fucking damn this shit hits harder than my mom

---
## [ToppleTheNun/WoWAnalyzer](https://github.com/ToppleTheNun/WoWAnalyzer)@[90c1dd8db4...](https://github.com/ToppleTheNun/WoWAnalyzer/commit/90c1dd8db4b04d465daf45332ec73a28130651d1)
#### Sunday 2022-09-18 20:11:47 by Richard Harrah

second pass on demon hunter

clean out changelog entries referencing
abilities that are removed in DF

add sigils to HDH abilities list

clean out entries in SPELLS/demonhunter that are
present in TALENTS/demonhunter

add support for Charred Warblades

add getTalentRank function for Combatant

correct locations of multiple analyzers in the
statistics tab

add support for Misery in Defeat class talent

add support for Retaliation talent

add Buffs module for Vengeance to make frailty
support easier, given that it can now be applied by
three different abilities.

add support for Painbringer talent

add Blur and Darkness to Vengeance

add support for Tactical Retreat talent

add support for Initiative talent

update support for Cycle of Hatred talent

correct Know Your Enemy scaling

regenerate DH talents

---
## [Aidan-Lalonde-Novales/ics4u-unit1-02-typescript](https://github.com/Aidan-Lalonde-Novales/ics4u-unit1-02-typescript)@[d33f14d625...](https://github.com/Aidan-Lalonde-Novales/ics4u-unit1-02-typescript/commit/d33f14d6257946fc8f52a48669cb16992b531e60)
#### Sunday 2022-09-18 21:24:53 by Aidan-Lalonde-Novales

I HATE MY LIFEgit add -Agit add -Agit add -Agit add -Agit add -Agit add -Agit add -Agit add -Agit add -A

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[f73fc2ea10...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/f73fc2ea10c3193a56595e9d02d9aab186d99076)
#### Sunday 2022-09-18 22:12:18 by Halcyon

Redoes bluesec clothing sprites to have a nicer, more consistent color palette, along with correcting alot of glaring mistakes. (#16068)

* Everything

All the bluesec shit redone, given a consistent palette and better colors.

* Forgot the obj sprites, fuck

* formal oversuit

* Hey shitass, watch me kill these sprites

* More obj icons

* Bulltproof items.

Returns helmet to stock TG, cause the current one is ugly ass piss.

* obj

* secmed

* updates secmed a bit more

* helmet

---
## [ARF-SS13/coyote-bayou](https://github.com/ARF-SS13/coyote-bayou)@[2062e298a0...](https://github.com/ARF-SS13/coyote-bayou/commit/2062e298a06759209a0f3832362b4d750c10a9be)
#### Sunday 2022-09-18 22:19:39 by Tk420634

Slows Knife Raiders, and their buddies attacks a bit.

Haha, fucked that up didn't I?  We do a little shitting.  Also lowered some damages on rapid_meleeing mobs

---
## [Mojave-Sun/mojave-sun-13](https://github.com/Mojave-Sun/mojave-sun-13)@[736422fac8...](https://github.com/Mojave-Sun/mojave-sun-13/commit/736422fac8d84c8e054853fd2b205cc993250c21)
#### Sunday 2022-09-18 23:52:22 by Technobug14

Field Transfusions & Fixes Sprites/Runtime (#2152)

* Working field transfusions

As far as I can tell, no runtimes or bugs. Should be good to go. Could maybe do with some polish? But otherwise it works great.

* Fixes energy weapon bugs

Fixes a runtime related to emptying cells from energy weapons, and fixes an overlay bug and inventory icon bug on the cells themselves.

* Bug fixes

read above, fixes a few bugs/errors

* Broken as hell

Supposed to add new IV bag sprites and overlays that would change as the bag gets emptier. Multiple bugs both with transfusion and the icon/overlay. Right now, the icon currently disappears once the object is on the ground and I can't tell why. Secondly, the overlay has the visual bugs and could probably do with a more thorough system to apply it? The bugs on transfusion are mostly due to a lack of sanity checks, where it will continue to be attached to someone from many tiles away when thrown/dropped, etc.

* Shit

HATE HATE HATE this sucks and it is buggy as hell

* Fix icon/overlay updates

* Mostly working

Still some broken stuff, you can attach IV bags if you're not next to someone and do it from inside containers, also fixes the world states for the police and military 10mm pistol

* Finishing touches

Couple of bug fixes, fixes 10mm police/military world sprite, etc etc. Should be good to go.

Co-authored-by: Koshenko <koshenko@pm.me>
Co-authored-by: Koshenko <53068134+Koshenko@users.noreply.github.com>

---

