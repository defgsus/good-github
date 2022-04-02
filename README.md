## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-04-01](docs/good-messages/2022/2022-04-01.md)


1,863,126 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,863,126 were push events containing 2,958,004 commit messages that amount to 228,389,197 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 52 messages:


## [KDr2/pytorch](https://github.com/KDr2/pytorch)@[1b7d7d9327...](https://github.com/KDr2/pytorch/commit/1b7d7d93276eb37c009905ef87ea9c2a7c95481e)
#### Friday 2022-04-01 00:03:15 by Brian Hirsh

Reland: "free up dispatch key space (in C++)" (#74963)

Summary:
Pull Request resolved: https://github.com/pytorch/pytorch/pull/74963

This is a re-land of D35192346 (https://github.com/pytorch/pytorch/commit/9872a06d77582e91e834103db75f774ca75f7fff) and D35192317 (https://github.com/pytorch/pytorch/commit/a9216cde6cc57f94586ea71a75a35aaabee720ff), which together are a diff that changes the internal representation of `DispatchKeySet` in pytorch core to free up the number of dispatch keys that we have available. See a more detailed description of the design in the original PR: https://github.com/pytorch/pytorch/pull/69633.

The original PR broke Milan workflows, which use a pytorch mobile build, and manifested as a memory corruption bug inside of `liboacrmerged.so`.

**Background: Existing Mobile Optimization**
Pytorch mobile builds have an existing optimization (here https://github.com/pytorch/pytorch/blob/cc23725e89713138aa1c81ce5fb4a8dbcd440ccf/c10/core/DispatchKey.h#L382 and here https://github.com/pytorch/pytorch/blob/cc23725e89713138aa1c81ce5fb4a8dbcd440ccf/aten/src/ATen/core/dispatch/OperatorEntry.h#L214), which works as follows:

Every operator in pytorch has a "dispatch table" of function pointers, corresponding to all of the (up to 64) different kernels that we might dispatch to when we run an operator in pytorch (autograd, cpu, cuda, complex number support, etc).

In mobile builds, the size of that table is shrunk from 64 to 8 to save a bunch of space, because mobile doesn't end up using the functionality associated with most dispatch keys.

The dispatcher also has a notion of "fallback kernels", which are kernels that you can register to a particular dispatch key, but should be able to work for "any operator". The array of fallback kernels is defined here: https://github.com/pytorch/pytorch/blob/cc23725e89713138aa1c81ce5fb4a8dbcd440ccf/aten/src/ATen/core/dispatch/Dispatcher.h#L294.

The mobile-optimization currently does **not** extend to this array (it wouldn't be that useful anyway because there is only one array of fallback kernels globally - vs. there is a separate dispatch table of function pointers per operator). So the per-operator tables on mobile are size 8, while the fallback table is size 64.

**The Bug**
This PR actually makes it difficult to enable that optimization separately for the per-operator arrays vs. the fallback array, and incidentally shrunk the size of the fallback array from 64 to 8 for mobile (that happened on this line: https://github.com/pytorch/pytorch/pull/69633/files#diff-f735cd7aa68f15b624100cbc4bb3b5ea76ffc7c9d3bec3b0ccabaa09609e5319R294).

That isn't a problem by itself (since mobile doesn't actually use any of the fallbacks that can no longer be stored). However, pytorch core will still register all of those fallback kernels on startup in mobile builds, even if they aren't used. When we tried to register one of those fallbacks on startup, it would try to dump the kernel somewhere in memory past the bounds of the (now smaller) array inside of the `Dispatcher` object, `backendFallbackKernels_`.

**Why didn't this problem show up in OSS CI? Why didn't it break other internal mobile workflows aside from Milan?**

Ideally, this failure would show up as part of the OSS signal on GitHub, since we already have mobile OSS builds. Given that it was another memory corruption issue that only affected Milan (subset of mobile), I'm not sure what's specific about Milan's builds that caused it only to manifest there. dreiss I wonder if there's another flavor of mobile builds we could run in OSS CI that could potentially help catch this?

**The debugging experience was pretty difficult**

Debugging the Milan-specific failure was made difficult by the following:

(1) lack of CI
- the original Milan failure didn't surface on my original diff, because the Milan job(s) that failed weren't triggered to run on pytorch changes. There's probably a balance to strike here, since those jobs will only be useful if they aren't flaky, and if they can produce reliable failure logs for debugging.

(2) It's difficult to get a repro.
- my work laptop doesn't have the right specs to run the Milan development workflow (not enough disk space)
- There is an existing OnDemand workflow for Milan, but it appears to be relatively new, and after a bunch of help from MarcioPorto, we ran into issues forwarding the log output from Milan tests on the emulator back to the terminal (see the original discussion here: https://fb.workplace.com/groups/OnDemandFRL/permalink/1424937774645433/)

(3) Lack of stack-traces.
- Most Milan failures didn't include actionable stack traces. phding generously helped me debug by running my suggested patches locally, and reporting back if there were any failures. The failing test didn't include a stack trace though (just the line where the crash appeared), so I ended up making some educated guesses about what the issue was based on the area of the crash.
ghstack-source-id: 152688542

Test Plan: Confirmed with phding that the broken Milan workflow from the previous version of this diff is now passing.

Reviewed By: phding, albanD

Differential Revision: D35222806

fbshipit-source-id: 0ad115a0f768bc8ea5d4c203b2990254c7092d30
(cherry picked from commit 002b91966f11fd55ab3fa3801b636fa39a6dd12c)

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[ee0e7149e5...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/ee0e7149e57faf3f07975b7a1f17bfd0e4578954)
#### Friday 2022-04-01 00:14:44 by SkyratBot

[MIRROR] Fixes conveyor runtime [MDB IGNORE] (#12407)

* Fixes conveyor runtime (#65788)

Conveyor would runtime whenever it is right clicked with an item

Fixes #64595 (Runtime on conveyor for right clicking)

fixes a runtime with conveyor where right clicking it with any item would cause a runtime

Mothblocks rant from the issue report below, you've been warned:

Because right-clicking in BYOND is horse-shit. It pipes it all through the normal Click and only tells you it's a right-click through a flag. This means that on anything that isn't prepared, right-clicking is the same as left-clicking, which is terrible UX that only exists in SS13.

Nothing should return ..() from attackby_secondary, because the default is the legacy behavior of making right-click pass as left-click (which I want to kill ASAP, once nothing uses the stupid flags anymore).

Remove else return ..(), and make this whole thing do return SECONDARY_ATTACK_CANCEL_ATTACK_CHAIN.

* Fixes conveyor runtime

Co-authored-by: FinancialGoose <92416224+TheBoondock@users.noreply.github.com>

---
## [pariahstation/Pariah-Station](https://github.com/pariahstation/Pariah-Station)@[94ffdc8812...](https://github.com/pariahstation/Pariah-Station/commit/94ffdc8812d15c36c9044ecfbede3148a11eda13)
#### Friday 2022-04-01 00:15:29 by LemonInTheDark

Action button refactor/rework: Enhanced Dragging (#65180)

About The Pull Request

I noticed a lot of strange and un-intuitive behavior in action buttons, and got stung by the bloat bug. Damn it hug #58027
I'll do my best to explain what I've changed and why, might get a bit long.
If you want a better idea, read the commits. Most of em are pretty solid, if long.

Whelp. Here we go.
How do action buttons currently work

All action buttons are draggable, to any place on the screen. They're held in an actions list on the player's mob.
Their location in this list determines their position on the top of the screen. If one is dragged away from the top, its position in the list is "saved". This looks really bad.
If two buttons are dragged over each other, their positions swap. (inside the actions list too)
If a button is shift clicked, it is brought back to the position it started at.
If the action collapse button that you likely just mentally edit out is alt clicked, it resets the position of all action buttons on the screen.
If an action is ctrl clicked, it is "locked". This prevents any future position changes, and also enables a saving feature. With this saving feature, locked button positions persist between rounds. So your first o2 canister will always start where you saved it, etc.
Actions and buttons are a one to one link. While there is functionality to share action buttons between two players, this means showing the same object to both. So one player can move a button on another's screen. Horrendous.
This also makes code that modifies properties of the screen object itself very clunky.
Why is this bad

A: None knew pretty much any of this information. It is actually documented, just in a horribly formatted screen tip on the collapse button, you know the one we all mentally delete from the hud.
B: None of this is intuitive. Dragging buttons makes the hud look much worse, and you get no feedback that you even can drag them. Depressing
C: We use actions to make new options clear to the player. This means players can have a lot of action buttons on the hud. This gets cluttery
D: The collapse button is useless. It lets you clear your screen if someone like me fucks up and gives you 2000 actions, but outside of that it just hides all information from you. You never want to see none of your action buttons, just a filtered list of them.
E: On a technical level, they're quite messy, and not fully functionally complete. This is depressing.
What I've done

Assuming the above to be true, how do we fix them?
Well first I'm going to go over everything I changed, including links to major commits. I'll then describe the finished product, and why I made the decisions I did.

Oh and I've moved some of the more niche or technical discussion to dropdowns. Hopefully this makes finding the major functional changes easier

Adds helper procs for turning screen_loc strings into more manageable arrays. This doesn't fully support all of the screen_loc spec, but it's enough for what I'm doing. (f54865f)

Uses these helper procs to improve existing code (6273b93)

Fixes an issue with tooltip code itself. If you tried to hold down a mouse button while dragging onto a tooltip enabled object, it would silently fail. The js made assumptions about the order args came in, which broke when buttons were held down (e0e42f6)

Adds a signal linked to /client/Click(). Surprised we didn't have this before honestly (c491a4a)

Makes /client/MouseDrag() return parent. If we don't do this, any overrides of MouseDrag will never actually be called (2190b2a)
Refactors how action buttons work under the hood (53ccce2)
Basically, rather then generating one button per action, we generate one button per viewer

Starts to change button behavior, more cleanup

Changes the mouse cursor when an action button is dragged. Hopefully
this makes moving things feel less like an accident, and makes you doing
it more clear

Removes the moved and locked vars. This will be more relevant later, but
for now:

Moved exists as a sort of budget "We've been dragged" variable. We can
handle this more cleanly, and the movable type doesn't care about it

Locked is a very old variable that is also not something that the
movable type "owns". It's more an action button thing that's been moved
down.
It exists so an action can be locked in place, and in that locking, be
treated as a "saved location"
(21e20fc)

Because I've nuked move, we don't need to directly set our button's
position. We can use the default_button_position var instead. This is
quite handy.

Please ignore position_action, I will explain that later
(83e265e)

Removes the buttons locked pref

It was another obscure part of action buttons, basically do buttons
start "locked" or not. See previous discussion of locked
(b58b1bd)

Major rework starts here

Alright. Sorry for this, this is where me not commiting regularly starts
to suck. I'll do my best though.

Rather then figuring out an action button's position via a combination
of the moved and ordered vars, we use a separate location var to store
one of a few defines. This makes life later much easier.

Adds tooltip support for dragging action buttons. The way the tooltip
just froze in place when dragging really bugged me, and lead to some
nasty visual artifacts.
This is a bit messy because the drag procs are horrible, but it's
workable

Dropping a button on another button will no longer swap their positions
Behavior instead depends on the target button.

If it's a part of a group (A concept I will explain later) the dragged
button is simply inserted before it in the group's list.

If it's floating on the general hud, we instead position the dragged
button to its right. There's extra logic here to ensure buttons will
never overflow the screen, but I'll get into that later.

Alright. That's most of the refactoring. Time for the larger behavior
changes.

Adds a button palette. This is a separate dropdown that renders
underneath buttons.

image

The idea is to allow for a conceptual separation between "important"
buttons and the ones that end up cluttering the screen.

You can click on the dropdown to open it, then any later clicks that
don't involve actions in some way will autoclose it.

My goal is to come up with an alternative for the action button that
just acted as a way to hide all buttons on screen. Not convinced it saw
much use.

As a side effect of removing that, I've moved its tooltip stuff to the
palette. I've properly formatted it, so hopefully it's easier to read
then the jumble that we used to have.

(You can alt click the palette button to reset all button positions)

Oh and the palette can scroll, since as you'll see later it has a
limited size.
image

Moving on from that, I've added what amounts to action landing buttons.
These allow buttons to rejoin groups, or be positioned at the end of a
line of buttons.
image

They've got a 32x32 hitbox, and only show up when dragging. Hopefully
this makes the system more clear just by dragging an action.

Oh and I've changed how button position updating works. The old system
of calling update_action_buttons on mob every time an action button
changes position is gone, mostly because I've setup more robust
grouping. Will discuss when I get to huds

(0d1e93f)
Adds the backbone behind action button position changes (94133bd)

Moves hud defines to the global folder, safer this way (7260117)

Adds color changing to the palette button, giving some heads up for buttons being inserted into the palette automatically
image
image
Ensures a landing button is always shown, even if it needs to break the
max row rule
Makes palettes auto contract if they have no buttons inside them
Prevents palettes from being opened if they have no buttons inside them
(f9417f3)
How it looks
2022-02-26.02-30-10.mp4
Why It's Good For The Game

Players have more control over the clutter on their screen.
Buttons are available, but not in the way,
Since any player move of a button saves it, any lack of clarity in the way buttons work will be forced out by buttons not just resetting when a new game starts.
We don't overlap any existing screen elements, unless the upper button list gets really long.
The code is much less crummy (I think, may have made it worse it's hard for me to judge my own work)

If it ends up not being as usable as I'd like, I'll rip out the existing changes and just implement the qol and backend stuff. I think it's worth doing though.
Changelog

cl
add: Expanded heavily on action buttons
add: Adds an action button dropdown that sits just under the normal list in the top left. You can drag new buttons onto it to insert them. Click on it to show its contents, do what you want to do, then click again anywhere to contract it. Alt click it to reset all button positions
add: Action buttons will now remember their position between rounds. So if you really like your flashlight right next to your player for some reason, we support that now
add: When you start to drag an action button, docking ports will appear in places that it can be inserted into. (Outside of just floating somewhere on your screen of course)
del: Removed action button locking, and the associated preference. I'm reasonably sure literally none uses this, but if you do hit me up
qol: Dragging an action button will now give you an outline of its size around your cursor
fix: You can no longer cause the screen to expand by putting an action button on the edge of widescreen, and then resizing to standard.
refactor: Refactors action and button code significantly. lots of little things.
/cl

---
## [DestroyedClone/EnforcerMod](https://github.com/DestroyedClone/EnforcerMod)@[2538549196...](https://github.com/DestroyedClone/EnforcerMod/commit/253854919652e9581f25cb431113992ff0825282)
#### Friday 2022-04-01 00:24:51 by TimeSweeper

an inordinate amount of time on fucking needler

grandmastery achievement fixed real good, stun grenade achievement fixed
fucking fixed disappearing gun models god damn I just gave myself a solid week of mental turmoil tossing and turning at night wondering why i'm such a f
anyway
also mallet haha
oh yeah that. spent a very good amount of time setting up psds for recolors. nemforcer enforcer looks pretty sweet ngl

---
## [DestroyedClone/EnforcerMod](https://github.com/DestroyedClone/EnforcerMod)@[65f3fd807c...](https://github.com/DestroyedClone/EnforcerMod/commit/65f3fd807c5991f63eb4c7d407217cf758b0b5d8)
#### Friday 2022-04-01 00:24:51 by TimeSweeper

ok robit achievement networked. fuckin config mismatch holy hell
speaking of configs, moved them out of enforcermain. slowly slowly de-retarding that script
but also adding more retarding. hacked golem deflecting to stone wisps as well, wip
oh yeah golem deflecting is finally fucking networked

---
## [DestroyedClone/EnforcerMod](https://github.com/DestroyedClone/EnforcerMod)@[c8bc6835dd...](https://github.com/DestroyedClone/EnforcerMod/commit/c8bc6835dd8bf1cf2a665fa81ce87202e0f8e947)
#### Friday 2022-04-01 00:24:51 by TimeSweeper

more dumb shit i'm sure

silly limb masking but also legit limb masking
more reorganizing it looks like
vr maybe
god damn so much shit I don't even know

---
## [DestroyedClone/EnforcerMod](https://github.com/DestroyedClone/EnforcerMod)@[a3f6a92f4b...](https://github.com/DestroyedClone/EnforcerMod/commit/a3f6a92f4b6f42f51c200c162d82aab3c389e34f)
#### Friday 2022-04-01 00:24:51 by TimeSweeper

holy shit gm real?

fucking with boss hitboxes for no reason, unlockable tweaks, nothing else important I don't think

---
## [CHOMPStation2/CHOMPStation2](https://github.com/CHOMPStation2/CHOMPStation2)@[8ee5f298c3...](https://github.com/CHOMPStation2/CHOMPStation2/commit/8ee5f298c3c3c03aca8011313aa6e07dce13bd79)
#### Friday 2022-04-01 00:26:30 by Rykka

Trait List Reorganization + Fixy, 2.0

The diff looks like a lot, but:
All YW Additions have been moved to neutral_ch.dm given YW refused to follow sanity policies of putting stuff in _yw files, and we're seemingly keeping these.

All BASE VOREStation files (negative, positive, neutral).dm have been synced with upstream, and any changes are appropriately labeled with CHOMPEdits and WHY they're edited, for future coders.

Traits have been renamed to make for easier grouping.
Specifically:
Pain Intolerant -> Pain Intolerance
High Pain Intolerance -> Pain Intolerance, Major
Haemophilia (Organics Only) -> Haemophilia (2x bloodloss rate, 2 points)
Haemophilia (YW Added) -> Haemophilia, Major (This one was 3x bloodloss rate for 3 points)
Big mouth -> Mouth, Big (Yes, it reads weird, but makes it easier to see the traits in the list.)
Giant mouth -> Mouth, Giant (Yes, it reads weird, but makes it easier to see the traits in the list.)
Low/High Pressure Resistance -> Pressure Resistance, Low (or High)
Extreme Radiation Resistance -> Radiation Resistance, Major. (Standardizes names.)
High blood volume -> Blood Volume, High
Very high blood volume -> Blood Volume, Very High


Multiple traits had description notes added to explain what they MECHANICALLY do. We're a server with more action than upstream, our traits need to be mechanically clear.
Species will be receiving a pass to give their description/readme info a mechanical summary later on.

---
## [Shadow-Quill/tgstation](https://github.com/Shadow-Quill/tgstation)@[55336d1e53...](https://github.com/Shadow-Quill/tgstation/commit/55336d1e5308789be1616413c8d8f87e073f7302)
#### Friday 2022-04-01 00:28:45 by vincentiusvin

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
## [OrionTheFox/Skyrat-tg](https://github.com/OrionTheFox/Skyrat-tg)@[8607ba8b7d...](https://github.com/OrionTheFox/Skyrat-tg/commit/8607ba8b7d98c52e81f23816a9224adf70559c25)
#### Friday 2022-04-01 00:38:31 by SkyratBot

[MIRROR] Adds a very rare sussy firelock [MDB IGNORE] (#12401)

* Adds a very rare sussy firelock (#65677)

On a VERY low chance (1/25000) a normal full tile firelock can instead be generated with a more suspicious appearance based on this recent quality shitpost.

Sussy firelocks are completely identical when open (save the desc) and thus are apt not to be noticed except during exciting times. It's a fully cosmetic joke that got me to log into github, and that's an accomplishment in itself. Probability rate fully negotiable, I've added a one in a million chance before after all.

* Adds a very rare sussy firelock

* ruins all the fun

people can get banned for doing the funny sus amogus so encouraging it in code, whilst it's beautiful and funny, eh someone is going to throw a fit.

Co-authored-by: Incoming5643 <incomingnumbers@gmail.com>
Co-authored-by: KathrinBailey <53862927+KathrinBailey@users.noreply.github.com>

---
## [FIRST-Team-1699/robocats2022](https://github.com/FIRST-Team-1699/robocats2022)@[3f238171f5...](https://github.com/FIRST-Team-1699/robocats2022/commit/3f238171f5831c5bad21aeb891c11c236d3fb8d3)
#### Friday 2022-04-01 00:46:48 by Alex

Shooter things worked on, it almost worked

i hate my life

---
## [twilightwanderer/tgstation](https://github.com/twilightwanderer/tgstation)@[c8ef62c1fb...](https://github.com/twilightwanderer/tgstation/commit/c8ef62c1fb7027ea58b569f0e4bd7df5a7d58935)
#### Friday 2022-04-01 00:55:50 by LemonInTheDark

Fixes bartender drink throwing, makes smashing always spill (#65698)

Tohg's initial pr (9c0b0e5d4cc236e365ef0229400cefe98b184964) was rather poorly argued and a bit misleading, but the actual changes were honestly kinda harmless. You could already have thrown beakers to splash shit on someone, it wasn't a big issue.

However it did end up breaking bartending, because it removed the ranged
args that normally get passed into smash and SplashReagent.

I went in intending to fix that, but noticed some dumb copypasta in
broken bottle code, and decided to just start from there.

I've moved that logic to a proc on the broken bottle, and made smashing
a bottle on something splash its contents too.

I can't think of a case where you wouldn't want this, so I'ma just go
for it. Prevents future mistakes like this too.

Oh and because I'm passing ranged in properly now, splashing will not
always splash the whole amount of the bottle's reagents. Doubt that
really matters tho.

Love ya bestie

---
## [jackflack69/OpenKJ](https://github.com/jackflack69/OpenKJ)@[47d966318b...](https://github.com/jackflack69/OpenKJ/commit/47d966318b915913688a2fee73208bfbb8e2e493)
#### Friday 2022-04-01 01:39:35 by jackflack69

Create !Author deceased 02-06-2022

homas Issac Lightburn passed away in his sleep on February 6th 2022.

I knew Issac personally for several years, but really hadn't spoken to him since I moved away from Nashville in 2019.

I do know that continued development, updates, and support for OpenKJ a cross platform Karaoke player will not be continued by the original author.

Also his back-end database called Songbook @ https://okjsongbook.com/ will not be continued by the original author.

Also the iOS and Android applications created to access Songbook will not be continued by the orginal author.

The announcement of his death is verifiable from the funeral home his family used to say goodbye to Isaac. The link is below.

https://www.spannfuneralhome.com - Funeral Home

https://www.spannfuneralhome.com/obituaries/Thomas-Lightburn/#!/Obituary - T. Issac Lightburn's funeral notice.

I am sending this to the contributors listed on the github contributions page so if they were curious why Issac hadn't contacted them, this is why.

I am sorry for your loss as well. He had an amazing mind, paid attention to the little details, and created a truly great gift to the Karaoke Community.

If anyone would like to continue his little side project OpenKJ, I would love to know. It would be an amazing tribute to see OpenKJ live on even after Issacs untimely passing.

I personally have no access to any of Issacs coding, projects, or accounts. I am not looking for them either. I am not a programmer or coder, just a fan.

Thank you for your time. 

David W. -

---
## [bywok/scratch-gui](https://github.com/bywok/scratch-gui)@[5981c799a4...](https://github.com/bywok/scratch-gui/commit/5981c799a4c9cf392a11cf83e171bcc7658c2f71)
#### Friday 2022-04-01 01:45:34 by bywok

Funny fun FON - T timers set to 8:990

Go and Fuck Yourself Up The Peeeeenus

---
## [Iamgoofball/Skyrat-tg](https://github.com/Iamgoofball/Skyrat-tg)@[a74758af0e...](https://github.com/Iamgoofball/Skyrat-tg/commit/a74758af0eb885b1ab97937bc53674074cb27fde)
#### Friday 2022-04-01 01:50:12 by SkyratBot

[MIRROR] Space drifting fixes and cleanup [MDB IGNORE] (#11801)

* Space drifting fixes and cleanup (#64915)

* Fixes infi pushing off something in space

Right now you can just push "into" a dense object forever, and depending
on your move rate, just kinda glide

We can fix that by checking if we're trying to push "off" something
we're moving towards

* Makes pushing off something shift it instantly

Currently if you kick off something in space it waits the delay of the
move to start drifting. Looks dumb, let's not

* Updates backup movement to properly account for directional windows. GOD I HATE DIRECTIONAL DENSITY SHOOOOOT MEEEEEEEEEEEEEEEEEEE

* Uses range instead of orange so standing on the same tile as a directional counts properly, rather then suddenly entering a drift state. I hate it here

* Ensures all args are named, updates implementations of the proc with the new arg

* Space drifting fixes and cleanup

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [NoiceBroice/Sound-Space-Quantum-Editor](https://github.com/NoiceBroice/Sound-Space-Quantum-Editor)@[22cda7f938...](https://github.com/NoiceBroice/Sound-Space-Quantum-Editor/commit/22cda7f938992bdfcc470fe3675b27979ac5571f)
#### Friday 2022-04-01 02:25:13 by NoiceBroice

It fucking is the fucking oh my holy shit

suck my nards this is a little cleaned however
TODO:
Make it actually start at the current position
Make the window close at the end of the map (i guess this is optional tho you can still hold r)
Maybe add Settings for testing in yk the fucking settings

---
## [linoid-gaming/the-bunker-2.0](https://github.com/linoid-gaming/the-bunker-2.0)@[5466df35d9...](https://github.com/linoid-gaming/the-bunker-2.0/commit/5466df35d937e6efe33068d87e706d887fa15dfd)
#### Friday 2022-04-01 03:40:12 by Alice Lum

Yeah Boy What? We off the grid, grid, grid This for my kid, kid, kid For when my kid, kid, kids have kids Everything we did for the crib Everything we did, how we live All this smoke got a scent All that smoke kept a scent Everything I spoke, what I meant Never disguise my intent Lines outside the event Brought my life out the trench God, thank God Look what He did, did, did, did, did, did We off the grid, grid, grid, grid, grid What? We off the grid, grid, grid, grid

Yeah
Boy
What?
We off the grid, grid, grid
This for my kid, kid, kid
For when my kid, kid, kids have kids
Everything we did for the crib
Everything we did, how we live
All this smoke got a scent
All that smoke kept a scent
Everything I spoke, what I meant
Never disguise my intent
Lines outside the event
Brought my life out the trench
God, thank God
Look what He did, did, did, did, did, did
We off the grid, grid, grid, grid, grid
What?
We off the grid, grid, grid, grid

---
## [Raeschen/CHOMPStation2](https://github.com/Raeschen/CHOMPStation2)@[e502b637e9...](https://github.com/Raeschen/CHOMPStation2/commit/e502b637e9893a197cfa641cc5f03ede77a2860d)
#### Friday 2022-04-01 06:54:38 by Rykka

Trait Addition + Adjustments

Polaris Combat is ass.
Yes, bandaid trait fixes are not necessarily the solution, BUT!

All of our negatives have extreme versions, without any sort of positive counterpart, and the positives we DO have are weak.
However, a flat 50% reduction on both incoming burn/brute would be too much, therefore:

Trait changes as follows.
- Added Glass Endurance. You have 25 HP, or 50 total HP, before you die. Don't get hit, and with Baymissn't? You're a masochist.
- Brute/Burn Resists no longer exclude High/Very High Endurance.
- Major Burn/Brute Resist re-added: These provide a 40% DR (Damage Reduction), at the cost of 3 points. This is opposite to Major Weakness, which is a 50% incoming damage increase.
- Very High Endurance re-added: This increases your max HP to 150.
- Increased Pain Tolerance: Similar to Increased Pain INtolerance, you have a 40% DR on incoming pain, compared to, for Intolerance, a 50% increase on incoming pain.
- Lick Wounds added back as a 1-cost Positive trait. I wondered why I hadn't seen it - it'd been disabled for _two years_ since Jan 2020.

Now, this is very likely to be controversial as it's a VERY huge balance change. Please don't bite my head off - this came up in discussion with Serdykov in DMs, and after digging through PRs, I discovered that traits had been disabled/removed for 1-2 years.

Pending a rewrite of Polariscode combat, and/or significant tweaks to make it more palatable, this will allow for more tankiness in combat - at the cost of extreme downsides. You can't suddenly become a hulk in combat with just traits, you still have to take some heavy downsides.

For instance:
Base Points - 1
Total Traits - 8

Very High Endurance - 4
Major Burn Resist - 3
Major Brute Resist - 3
Increased Pain Tolerance - 3

Current Points -12
Current Traits Left - 4

Conductive Major - -3
Extreme Photosensitivity - -2
Haemophilia - -3
Major Loneliness - -5

Current Traits Left - 0
Current Points 1

I'd be interested in looking at making Major Brute/Burn resist 4 points to equal 40% incoming DR, but that feels odd, given the negative is 50% incoming damage total for only 3.
I'd also be open to considering making VH Endurance even more expensive to 6, since it can be taken simultaneously now, and making base High Endurance cost 4.

---
## [OpsMx/gate](https://github.com/OpsMx/gate)@[e2a108db75...](https://github.com/OpsMx/gate/commit/e2a108db759f1cdfe89c8ac6bd3fafc10c39ac8e)
#### Friday 2022-04-01 07:19:22 by Chris Phillips

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
## [renemaro/UntitledRPG](https://github.com/renemaro/UntitledRPG)@[018bc827e9...](https://github.com/renemaro/UntitledRPG/commit/018bc827e91f0a77095307e0e8f0343cf0671390)
#### Friday 2022-04-01 07:22:22 by renemaro

Some shit

A lot of small shit I can't remember...

Maybe it was:
- NPC reaction to the Player death
- The Player respawn after death
- Dead monsters respawn as cursed ahsdows from another world after the Player death.

---
## [thozza/osbuild-composer](https://github.com/thozza/osbuild-composer)@[af44202b1c...](https://github.com/thozza/osbuild-composer/commit/af44202b1c6e53a5d3a248e2c1c493445743f188)
#### Friday 2022-04-01 08:32:12 by Ondřej Budai

cloudapi: rename gpg_key field to gpgkey

Oh no, we made a mistake here: Both our json repositories and repo files in
/etc/yum.repos.d have the GPG key in a field named `gpgkey`. Unfortunately,
cloudapi uses a field named `gpg_key`. One consequence of this issue is that
our api.sh test is meant to pass GPG keys in the compose request but since
it's using a bad field name (`gpgkey`), the key is actually not used.

I've decided to fix this in cloudapi: The `gpg_key` field is now renamed to
`gpgkey`. This is a breaking change but no one is using this API anyway so
we think it's better to do this now than introducing weird backward
compatible hacks.

Signed-off-by: Ondřej Budai <ondrej@budai.cz>

---
## [Sedna-Games/Zero-Possession-Prototype](https://github.com/Sedna-Games/Zero-Possession-Prototype)@[64478f1022...](https://github.com/Sedna-Games/Zero-Possession-Prototype/commit/64478f1022ce8b50c3a832cdc3888462e3697b9d)
#### Friday 2022-04-01 08:43:33 by Hamraj

[WIP] More Buildings

- yeah still a long ass way to go but im faster at the shit now

---
## [realicraft/FightSim](https://github.com/realicraft/FightSim)@[6a78c80d09...](https://github.com/realicraft/FightSim/commit/6a78c80d09f56c10e31459e0aef7c943fc8a2328)
#### Friday 2022-04-01 08:48:24 by realicraft (pi)

Turn 67

- moved all CSS into a seperate folder
- haha, funny April Fools joke
- moved some in-line CSS into files
- new fonts
- new helper tool, designed to add a "template" system to .tbgsbb files
- mystery skill 5
- repquest can now have variable heights
- duplicated every CSS file and iconsheet, to make CGA variants
- icon for mystery skill 4
- weapon icons for mystery skill 4
- weapon icons for carving and cooking
- probably more
- woah, over 100 changes (according to code oss)

---
## [Lustmored/EasyAdminBundle](https://github.com/Lustmored/EasyAdminBundle)@[f3a4b13382...](https://github.com/Lustmored/EasyAdminBundle/commit/f3a4b13382f6d96f85b0b1d8dfe329f40a39d32c)
#### Friday 2022-04-01 09:44:26 by Javier Eguiluz

minor #5139 Disable UX-Turbo (Lustmored)

This PR was merged into the 4.x branch.

Discussion
----------

Disable UX-Turbo

In all my projects with EasyAdmin I am sharing Stimulus controllers between EasyAdmin and frontend (I need them sometimes and it's just simpler). Since enabling Turbo on some projects I need to overwrite EasyAdmin layout just to disable it.

Currently EA is very unfriendly towards Turbo - there are JavaScripts in body, DOMContentLoaded listeners and so on. Refactoring everything to be turbo-compatible would be titanic effort with little benefit (it's not really needed in CRUD dashboards in my opinion), while adding this single attribute will make life easier for probably more consumers than just myself :)

Commits
-------

735b2397 Disable UX-Turbo

---
## [Gorilla669/kernel_realme_RM6785](https://github.com/Gorilla669/kernel_realme_RM6785)@[4b1ffe1a3d...](https://github.com/Gorilla669/kernel_realme_RM6785/commit/4b1ffe1a3df7eac07a0a6146cc79d5cc76d26ba2)
#### Friday 2022-04-01 10:38:18 by Peter Zijlstra

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
Signed-off-by: Vaisakh Murali <mvaisakh@statixos.com>

---
## [ISSOtm/rgbds](https://github.com/ISSOtm/rgbds)@[730b24c896...](https://github.com/ISSOtm/rgbds/commit/730b24c8967a2469d45da056d73c9c4ab944ff60)
#### Friday 2022-04-01 10:45:23 by ISSOtm

Hack in new register syntax

Oh my god I want to die x_x

---
## [purplecofe/qb-vehiclekeys](https://github.com/purplecofe/qb-vehiclekeys)@[757fdd0859...](https://github.com/purplecofe/qb-vehiclekeys/commit/757fdd0859013e45f9d432fa894f0ecb03d8bbf5)
#### Friday 2022-04-01 11:54:33 by ItsANoBrainer

Proper Refactor

Refactored the entire resource because the key system was not working.

No longer does a server callback 10 or so times a second, on top of other bad practices.

Tested pretty much everything with my devs, but there might be some weird issues we havnt found. Please lookover as I've been going crazy with the small tedious issues I've come across doing this.

Throwing this up to get feedback, and for people to use who want it.

Features:

- Keys are saved server side, and sent to each client when they are added or removed, as well as on character selection. This allows characters to leave and come back in the same server uptime session and still have the same keys
- Keys are only pulled from the server once on character load
- Giving keys has 3 types, /givekeys with an id will attempt to give keys you have to an id, not including an id will try to give it to the closest person, and if you're in a vehicle it will give to everyone
- Can only give keys to vehicles you have keys to
- Server event to force acquire keys to a plate for a person (for lockpicking/stealing/spawning, etc.)
- Can Carjack an NPC with a gun, has different percentages to work based on weapon (config)
- Take keys from dead npc drivers
- Can lockpick a car to unlock the doors
- Can hotwire a car if you're in the driver seat of the vehicle you dont have keys to to get keys
- Keeps the engine of a vehicle off if you dont have keys to it (allows other resources to attempt to toggle car engine without needing to interface if you have keys or not)
- Vehicle blacklist system for vehicles you dont want to be lockable (always unlocked)
- Police Alerts from lockpicking/hotwiring/carjacking
- Export to check if you have keys to a vehicle
- Locking/unlocking with hotkey
- Locking/unlocking and giving keys uses a custom GetVehicleInDirection you are facing for realism/accuracy
- Fully compatible with old resource. Has an event handler for 'vehiclekeys:client:SetOwner' in which it gives keys for that plate
- Some other shit I probably forgot

TODO:
- Add LOCALE support
- Stop peds from wanting to get back into the vehicle they just got carjacked out of as they're fleeing

---
## [Ahmed88888/RTPayload22](https://github.com/Ahmed88888/RTPayload22)@[9495558871...](https://github.com/Ahmed88888/RTPayload22/commit/9495558871580d9a7b2c2922b1f0c8bd27cb9078)
#### Friday 2022-04-01 12:03:01 by Alex Swanson

Fuck ahmed and his goddamn merge conflicts he can die so can alex i wanna die like holy shit this was a miserable process

---
## [vogelpi/ibex](https://github.com/vogelpi/ibex)@[c15f3b8888...](https://github.com/vogelpi/ibex/commit/c15f3b88883781808eaa96bda205a9bdaff5eb98)
#### Friday 2022-04-01 13:01:21 by Rupert Swarbrick

[icache] Define some fake DPI functions to simplify linking

This is triggered by the fact that if the ICache parameter is false
then we don't instantiate the ibex_icache module. For verilator
simulations, the module is then discarded entirely, which means that
its two DPI functions are not defined. That's unfortunate because
we're also compiling the code in scrambled_ecc32_mem_area.cc, which
expects the functions to be defined.

The obvious solution (don't include scrambled_ecc32_mem_area.cc if you
don't have an icache) isn't easy to do, because FuseSoc doesn't
currently allow us to use parameters to configure its dependency
tree (see fusesoc issue 438 for a discussion).

The super-clever solution that I came up with before(!) was to declare
these symbols as weak in the C++ code. That way, we can do a runtime
check to make sure that no-one is silly enough to call them without an
icache, but everything will still build properly either way.

Unfortunately, that doesn't work well with xcelium simulations.
Xcelium turns out to compile all the C++ code into one .so library and
generate functions for exported DPI functions in another. These two
solibs then get loaded at runtime with dlopen(). But this doesn't work
with weak symbols: in fact, it seems you end up with the C++ version
every time. Boo!

So let's be stupider about it and define (bogus) versions of the DPI
functions in this case. Fortunately, both of them are designed to
return zero on failure so we can just return zero and needn't worry
too much.

The idea is that when this lands, we can revert the OpenTitan change
that switched the C++ code to using weak symbols and Xcelium
simulations will start working.

---
## [magatsuchi/tgstation](https://github.com/magatsuchi/tgstation)@[0d1e93ffbd...](https://github.com/magatsuchi/tgstation/commit/0d1e93ffbd5b0915b09fbc0c349410a125bac4cc)
#### Friday 2022-04-01 13:32:16 by LemonInTheDark

Reworks action buttons significantly

Alright. Sorry for this, this is where me not commiting regularly starts
to suck. I'll do my best though.

Rather then figuring out an action button's position via a combonation
of the moved and ordered vars, we use a seperate location var to store
one of a few defines. This makes life later much easier.

Adds tooltip support for dragging action buttons. The way the tooltip
just froze in place when dragging really bugged me, and lead to some
nasty visual artifacts.
This is a bit messy because the drag procs are horrible, but it's
workable

Dropping a button on another button will no longer swap their positions
Behavior instead depends on the target button.

If it's a part of a group (A concept I will explain later) the dragged
button is simply inserted before it in the group's list.

If it's floating on the general hud, we instead position the dragged
button to its right. There's extra logic here to ensure buttons will
never overflow the screen, but I'll get into that later.

Alright. That's most of the refactoring. Time for the larger behavior
changes.

Adds a button palette. This is a seperate dropdown that renders
underneath buttons.

The idea is to allow for a conceptual seperation between "important"
buttons and the ones that end up cluttering the screen.

I have some more stuff I want to do with this visually, but that can
wait for later.

You can click on the dropdown to open it, then any later clicks that
don't involve actions in some way will autoclose it. This is slightly
clunky, not sure if it's a good idea or not

My goal is to come up with an alternative for the action button that
just acted as a way to hide all buttons on screen. Not convinced it saw
much use.

As a side effect of removing that, I've moved its tooltip stuff to the
palette. I've properly formatted it, so hopefully it's easier to read
then the jumble that we used to have.

(You can alt click the palette button to reset all button positions)

Oh and the palette can scroll, since as you'll see later it has a
limited size.

Moving on from that, I've added what amounts to action landing buttons.
These allow buttons to rejoin groups, or be positioned at the end of a
line of buttons.

They've got a 32x32 hitbox, and only show up when dragging. Hopefully
this makes the system more clear just by dragging an action.

Oh and I've changed how button position updating works. The old system
of calling update_action_buttons on mob every time an action button
changes position is gone, mostly because I've setup more robust
grouping. Will discuss when I get to huds

Sprites are awful, I'm sorry

---
## [magatsuchi/tgstation](https://github.com/magatsuchi/tgstation)@[94133bda4d...](https://github.com/magatsuchi/tgstation/commit/94133bda4d28b3ccfb04200bb0fe3e354fc4db27)
#### Friday 2022-04-01 13:32:16 by LemonInTheDark

Adds the backbone behind action button position changes

Alright, so I've showed you how actions think about positioning, but how
does it actually work.

The main thing we're doing here is grouping action buttons more
expansively.

The /datum/action_group datum "owns" a set of action button screen
objects.
It manages their postion in a list, and reacts to scrolling.
Also manages the existence of landing objects, and other such things.

Subtypes of the action group include /listed, which stores the action
buttons that live in the top bar of the screen, and /palette, which
holds the buttons stored in the action palette

The palette datum also manages the position of all other palette related
things, like the dropdown button, and scroll buttons.

This dynamically reacts to the height of the list group.

Floating action buttons require much less cohesiveness. I could
probablly handle them as a datum too, but honestly since they have no
relation to each other, a list is more suitible.

In addition to all this, action groups will automatically resize if
their rows overflow the screen space. The same can be said for floating
action buttons.

As things currently stand, you can cause byond to display the "fucky"
part of the rendering space just by putting an action button to the
right in widescreen, and then switching to 15x15 space. S dumb. They'll
now relocate to prevent fuckyness.

Kind of on the same topic, floating action buttons can no longer "cut"
the border of the screen. No matter where you try and place one, it will
always remain fully visible, won't get halfway cutoff by the screen
border

---
## [KrossX/pcsx2](https://github.com/KrossX/pcsx2)@[89f10e1605...](https://github.com/KrossX/pcsx2/commit/89f10e160572063b4871bfb8d0c6ffff54f9543a)
#### Friday 2022-04-01 13:32:31 by RedDevilus

GameDB:  ':' to '-' + GS and other fixes

Windows doesn't like you to use ':' in folders this caused issues for when CK1 did savestates in folders and now it's also messing with unable to add covers in Qt so better to replace them and also to avoid other issues now and the future.
GS HW Fixes and other fixes for:
- Adventures of Cookie & Cream, The
- Brothers in Arms - Earned in Blood / Road to Hill 30
- Black
- Chaos Legion
- God Hand
- Knockout Kings 2001
- Kuon
- Outrun 2006 / 2 SP
- Project Eden
- Psi-Ops - The Mindgate
- Punisher, The
- Ratchet Deadlocked (USA) / Gladiator (Europe) / 3 Up Your Arsenal
- Silent Hills Origins / Shattered Memories / 3 / 4
- SoulCalibur II / III

Also made sure that the comments and their spacing were consistent.

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[f04b90b6e8...](https://github.com/odoo-dev/odoo/commit/f04b90b6e856bd8c1679cc728255f53fc788f8fd)
#### Friday 2022-04-01 13:56:57 by Julien Castiaux

[REF] core: HTTPocalypse (12) web ir.http & login

This commit is the 12th commit of a comprehensive refactor of our HTTP
framework. See odoo/odoo#78857 for complete historic, discussions and
rationnals.

The web module is twofold, on one side there are many controllers: /,
/web, /web/login, /web/database/selector, /web/dataset/call_kw, etc, on
the other side there is `session_info`: the method responsible to create
the web client's environ.

This module is kinda an exception as it is (with base) a server wide
module. In the case of the HTTP framework, it means that the controllers
of web are always accessible, i.e. going to / or /web/login will never
return a 404 Not Found even if the user is not connected to a database.

This is both a blessing and a curse. It is a blessing because the
controllers are always accessible it means that a new users can freely
access those routes. It is a curse because *any* user can access them,
even user who don't have a session yet thus who are not connected to a
database yet. From a developer standpoint, we have to put extra care to
correct serve users with and without a database. An example is the
/web/login route, the login/password pair is stored in a database,
without database it is impossible to validate a user login but users can
still access this route without db.

To solve this problem, there is the `ensure_db` function. This function
attempts to find a database using various sources (?db= query-string,
session db, mono db) and to save it on the user session. In case no db
is found, the user is redirected to the database selector. In a way,
this function grants a database to the user in a seamingly experience.
In a way, this function brings a welcome differentiation between
`auth='none'` with a database and `auth='none'` without a database. Such
differentiation only matters for the server wide modules as "regular"
module controllers are only accessible via the ir.http routing map, i.e.
it is not possible to declare a nodb controller outside of server wide
modules.

An important changement is the `session.authenticate` method, before it
was possible to call the method when the cursor was not yet initialized,
authenticate would open a cursor against the given database, setup a
registry and an environment and ultimately save everything on the
current request. Because the cursor is now greedily created, it is no
more possible to update the request environment when authenticating on
another database.

PR: odoo#78857
Task: 2571224

---
## [anxolin/cowswap](https://github.com/anxolin/cowswap)@[e2a9fc4d2a...](https://github.com/anxolin/cowswap/commit/e2a9fc4d2afb90a9ba9bcf6c503c90ea8cca2d3a)
#### Friday 2022-04-01 14:10:35 by David

[1057] Fix mobile swap confirmation styling (gnosis/cowswap#1063)

* move GpModal to modal mod

* add closemodallink to swap modal

* change styles to address comments

* margin fix

* Mobile responsive fixes for 1057 (gnosis/cowswap#1074)

# Summary

In response to issues/feedback reported on https://github.com/gnosis/cowswap/pull/1063
In my opinion I think the '<- Close modal and go back'
<img width="235" alt="Screen Shot 2021-07-27 at 18 09 48" src="https://user-images.githubusercontent.com/31534717/127189011-890c0cbd-4a2e-4b0b-8d53-925c718e952c.png">
can be made redundant by having a fixed header. This simplifies the approach, reduces noise and there's less interference with the content.

https://user-images.githubusercontent.com/31534717/127188882-5415fbe8-035a-4df5-a7aa-457a8217d235.mov 

https://user-images.githubusercontent.com/31534717/127188914-54a19cda-dbc9-4658-94eb-279809bb4a06.mov

# Issue spotted:
- The modal library we use, has a sort of 'janky' 'slide down to close' behavior, which interferes at times, with our fixed header approach. Here you can see how it manipulates the `transform: translateY`
<img width="1191" alt="Screen Shot 2021-07-27 at 16 55 12" src="https://user-images.githubusercontent.com/31534717/127189246-b575aaa8-3a66-40de-b3b2-4c973a332801.png">

As for a solution to this, I'd be curious if we can disable this while keeping the library. But haven't dig into that (yet).


# To Test
1. Mobile > Get to the swap confirmation modal > Scroll down > Header should remain fixed > click X to close
2. Mobile > Get to the Wallet modal > Header should remain fixed > click X to close
3. In both cases, the initial view should have sufficient top margin to separate Fixed header <-> Content.

Co-authored-by: Michel <31534717+biocom@users.noreply.github.com>

---
## [anxolin/cowswap](https://github.com/anxolin/cowswap)@[636ab85c29...](https://github.com/anxolin/cowswap/commit/636ab85c29db08620a65ab4276e54a1a589d83a6)
#### Friday 2022-04-01 14:13:22 by Anxo Rodriguez

[xDai] Xdai custom NPM (gnosis/cowswap#102)

Brings xDAI to the swap UI:
- Allows to connect
- Shows xDAI instead of ETH
- Allows to Wrap xDAI into wxDAI
- Allows to Sell xDAI (it wraps and then sells wxDAI)

![image](https://user-images.githubusercontent.com/2352112/105481766-cb989380-5ca7-11eb-84c6-e9e10da879d3.png)

![image](https://user-images.githubusercontent.com/2352112/105482349-8a54b380-5ca8-11eb-876a-2017443062c7.png)


Also includes Blockscout link:
![image](https://user-images.githubusercontent.com/2352112/105482276-71e49900-5ca8-11eb-829f-afa2757019c7.png)



## Why another xDAI PR
So here is a different approach than #94 

I was getting to some deadends with the former approaches, some criticisms 
- Some depended in a forked version of the SDK we don't control. Moreover, they are not even pushed to somewhere, they leave as a gigantic PR in Honeyswap repository that will probably never be merged. On top of this, they forked a SKD that is now sligly obsolete.
- The hacks bring a lot of typescript redefinitions to the project, and force us to change their imports, and/or do uggly hacks

## Current approach
This approach is not perfect either, it's basically a combination of:
- I forked their repo
- I PR them 2 PRS (one just adds xDAI, other adds any network). I was hopping they merge, but
- We cannot wait until Uniswap merges, so I did also a fork, and published my own package with the PR I sent to them
- In this PR I use my NPM package

Lot's of other things are happening in this PR. Sorry for making such a big PR, but I'm happy to walk through if it helps. 
I tried to at least break the commits in smaller pieces with a comment. 

## Help for the review
If it helps, let me know I can do a quick zoom session and clarify the parts. 
- My NPM package has the code from https://github.com/Uniswap/uniswap-sdk/pull/53 . Plan is to replace it once is merged.
- I tried to use our pattern of not overriding SRC, and managed in most cases, but still there was some exceptions. The exceptions where mostly because of the type, they required some objects (used as maps) to have all networks as keys. When I added xDAI they need now a value for that. I can change the type, but that would require the same change in the source file plus in every place where it's used (cause now you change the type and can return undefined)
- Most of the changes are just change on the path of the import, mostly `useContract` and `utils` because they are used a lot 
-  The most weird thing here is the updater. It was extracted from Dima's solution. He came up with a smart way to modify ETH label. Is hacky but it saves a lot of headaches (and it's contained). U'll see this in the PR in `utils/xdai/hack.ts`
- The rest, I think is easy to follow

## Not in this PR
Some labels need to be reviewed. It sometimes show ETH or WETH when is xDAI or wxDAI

Here I was wrapping xDAI:
![image](https://user-images.githubusercontent.com/2352112/105482553-d273d600-5ca8-11eb-8312-30a84f19df3e.png)

![image](https://user-images.githubusercontent.com/2352112/105482600-e3bce280-5ca8-11eb-9939-3c7320fe5eed.png)


## How to test
* Go to:
http://localhost:3000/#/swap?inputCurrency=0xb7D311E2Eb55F2f68a9440da38e7989210b9A05e&outputCurrency=0xe91D153E0b41518A2Ce8Dd3D7944Fa863463a97d&exactAmount=0.1
* Trade

---
## [Famana-Universalis-Team/FamanaUniversalis](https://github.com/Famana-Universalis-Team/FamanaUniversalis)@[1cacb8554a...](https://github.com/Famana-Universalis-Team/FamanaUniversalis/commit/1cacb8554a0c08f6d3d4f0997e8912c29b953266)
#### Friday 2022-04-01 14:33:26 by u1145

removed morale buffs from Nahallaian and Ordican ideas

fuck you github I'm not making the title shorter

---
## [dwsteele/postgres](https://github.com/dwsteele/postgres)@[ec62cb0aac...](https://github.com/dwsteele/postgres/commit/ec62cb0aac5ba31a82339606009ddbd7eb00e2ac)
#### Friday 2022-04-01 14:56:35 by Tom Lane

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
## [microsoft/terminal](https://github.com/microsoft/terminal)@[855e1360c0...](https://github.com/microsoft/terminal/commit/855e1360c0ff810decf862f1d90e15b5f49e7bbd)
#### Friday 2022-04-01 15:21:58 by Mike Griese

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

---
## [ValoTheValo/CEV-Eris](https://github.com/ValoTheValo/CEV-Eris)@[0bf8489f36...](https://github.com/ValoTheValo/CEV-Eris/commit/0bf8489f36a78217f448c0fbdb7b71f276f472d5)
#### Friday 2022-04-01 15:45:34 by Valo

Carrion to Spiderman

Spiderman, Spiderman,
Does whatever a spider can
Spins a web, any size,
Catches thieves just like flies
Look Out!
Here comes the Spiderman.
Is he strong?
Listen bud,
He's got radioactive blood.
Can he swing from a thread
Take a look overhead
Hey, there
There goes the Spiderman.
In the chill of night
At the scene of a crime
Like a streak of light
He arrives just in time.
Spiderman, Spiderman
Friendly neighborhood Spiderman
Wealth and fame
He's ingnored
Action is his reward.
To him, life is a great big bang up
Whenever there's a hang up
You'll find the Spider man.

---
## [shacharRonZohar/CaJan22-proj-Trello-frontend](https://github.com/shacharRonZohar/CaJan22-proj-Trello-frontend)@[285ec44cca...](https://github.com/shacharRonZohar/CaJan22-proj-Trello-frontend/commit/285ec44cca694671f760b9baf8bea23fbfdddd51)
#### Friday 2022-04-01 16:36:12 by RZShachar

THANK FUCKING GOD IT WORKS, IT SHOULDNT WORK, BUT IT GODAMN WORKS ON PROD ASWELL

---
## [shacharRonZohar/CaJan22-proj-Trello-backend](https://github.com/shacharRonZohar/CaJan22-proj-Trello-backend)@[8e55c1dffc...](https://github.com/shacharRonZohar/CaJan22-proj-Trello-backend/commit/8e55c1dffc015a7ed4e53ee90462174479dc5f5e)
#### Friday 2022-04-01 16:37:21 by RZShachar

Reverted the stupid activity saving to sending the whole board with the activities array, stupid thing wont work on prod otherwise, will try to make it work with the stupid sperate route if this bullshit also fucking fails

---
## [ValoTheValo/CEV-Eris](https://github.com/ValoTheValo/CEV-Eris)@[2ab1ce383d...](https://github.com/ValoTheValo/CEV-Eris/commit/2ab1ce383d24c1754ad65441011ff6a32d72a2f6)
#### Friday 2022-04-01 16:40:47 by Valo

fixing the bug (hopefully)

god shit fuck are you fucking kidding me god damn it i hope this gets merged

---
## [brantb/FFXIVQuickLauncher](https://github.com/brantb/FFXIVQuickLauncher)@[2a820bed81...](https://github.com/brantb/FFXIVQuickLauncher/commit/2a820bed814c80326c6a008653cfe7e26b7ba4a5)
#### Friday 2022-04-01 16:45:05 by Robert Baker

Add button to open integrity report

Fucking hell I hate UI code so much. I know this is a shitty way  to handle adding the button, but I tried making my own XAML window and XL never loaded it so I forced it in. 

This could probably be cleaned up or made into its own window, but it works and I never want to touch WPF again.

---
## [odoo/odoo](https://github.com/odoo/odoo)@[cbc9279eaa...](https://github.com/odoo/odoo/commit/cbc9279eaa169e65aeb2dab6dd36e3ffab4e481e)
#### Friday 2022-04-01 16:50:18 by Odoo's Mergebot

[MERGE] im_livechat: introduce chatbot scripts

PURPOSE

This commit introduces a chatbot operator that works based on a user-defined
script with various steps.

SPECS

A im_livechat.chatbot.script can be defined on a livechat rule.
When a end-user reaches a website page that matches the rule, the chat window
opens and the script of the bot starts iterating through its steps.

The chatbot code is currently directly integrated with the existing livechat
Javascript code.
It defines extra conditions and layout elements to be able to automate the
conversation and register user answers.

AVAILABLE STEPS

A script is defined with several steps that can currently be one of the
following types:

"text"

A simple text step where the bot posts a message without expecting an answer
e.g: "Hello! I'm a friendly robot!"

"question_selection"

The bot will ask a question and suggest answers, the end-user will have to
click on the answer he chooses
e.g: "How can I help you?
  -> Create a Ticket
  -> Create a Lead
  -> Speak with a human"

"question_email"

That step will ask the end user's email address (and validate it)
The result is saved on the linked im_livechat.im_livechatchatbot.mail.message

"question_phone"

Same logic as the 'question_email' for a phone number
We don't validate the input this time as it's a complicated process
(requires country, ...)

"forward_operator"

Special type of step that will add a human operator to the conversation when
reached, which stops the script and allow the visitor to discuss with a
real person.

The operator will be chosen among the available operators on the
livechat.channel.

If there is no operator available, the script continues normally which allows
to automate an "answering machine" that will redirect the user in case no
operator is available.

e.g: "I'm sorry, no operator is available right now, please contact us by email
at 'info@company.com', we will try to respond as soon as possible!".
(Or even something more complex with multiple questions / paths).

"free_input_single"

Will ask the visitor for a single line of text.
This text is not saved anywhere else than in the conversation, but it's still
useful when combined with steps that create leads / tickets since those print
the whole conversation into the description.

"free_input_multi"

Same as "free_input_single" but lets the user input multiple lines of text.
The frontend implementation is made by waiting a few seconds (currently 10) for
either the next submitted message or the next character typed into the input.

This lets visitors explain their issue / question with multiple messages.
Which is very useful since new messages are sent every time you press "Enter".

"create_lead"

Special step_type that allows creating a crm.lead when reaching it.
Usually used in addition to 'question_email' and 'question_phone' to create
interesting leads.

LINKS

Task-2030386

closes odoo/odoo#84000

Related: odoo/enterprise#24894
Signed-off-by: Thibault Delavallee (tde) <tde@openerp.com>
Co-authored-by: Patrick Hoste <pko@odoo.com>
Co-authored-by: Aurélien Warnon <awa@odoo.com>

---
## [PixelExperience-Devices/kernel_google_wahoo](https://github.com/PixelExperience-Devices/kernel_google_wahoo)@[f44f0b5d19...](https://github.com/PixelExperience-Devices/kernel_google_wahoo/commit/f44f0b5d190e4bd54cdce19232b278ab2289f960)
#### Friday 2022-04-01 17:36:28 by Maciej Żenczykowski

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
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[626b1748ed...](https://github.com/mrakgr/The-Spiral-Language/commit/626b1748ed3a449421ea275f5aac770dac42c23f)
#### Friday 2022-04-01 18:10:07 by Marko Grdinić

"4pm. The thunder did not last much, it went away as soon as I went to bed. It gave me time to think. I want to do more playing around with UVs. I need to go back to that metal piece and see whether setting the face area to 1 improves the seam placement (Edit: Yes it does). Right now it is extremely awful. After that, I want to see if setting the number of segments to even in bevel preserves the seams. It is actually a lot easier to do UVing on unbeveled surfaces.

4:10pm. How annoying. The bevels move the seams utwards rather than leave it in the middle. Well, no matter.

4:40pm. If you use select shortest path, it is possible to auto tag seams with it. I set the shortcut to something easy to reach like \ . In that case it is only slightly harder to use than unbeveled surfaces. When I set the face area to 1, the auto UV is decent on this example. It is not better than manual, but it is workable.

Ok...

4:40pm. I hate these small scans for Crow Record. Ok, let me take a break to read the second chapter and I will do some actual work.

4:50pm. Ok, enough of UVs, I am sick of them. I happy with my current grasp of them. It is not such a difficult subject.

Let me focus on texturing.

Time to fire up Substance.

https://feedback.substance3d.adobe.com/forums/261284-substance-3d-painter/suggestions/6626915-swap-foreground-and-background-color-with-shortcut

First let me resolve this problem. Why doesn't pressing X work for me?

It works with the mask layer, that switches it from black to white, but what about the paint layer? Why doesn't that work?

https://substance3d.adobe.com/documentation/spdoc/smudge-tool-143720512.html
> The simplest way to use the smudge tool is to use it directly on the content of a painting layer, as a regular paint tool.

> A smarter way to use the smudge tool is to create a painting layer and set all the channels of the layer to the "Pass through" blending mode. This will allow to smudge in a non-destructive way over all the layers located below the "smudge layer". The layers below remain intact and all the modifications applied later will be taken in account by the smudge layer.

Good advice.

Right now I am looking at the docs. I'll have to go through the docs for Clarisse as well at some point. All in due time.

For some reason the image links are broken in the docs.

5:20pm. I am looking at the shortcuts, and X is the invert grayscale tool.

There aren't too many to deal with. Ok...

https://youtu.be/H4rgnscD_3U
Passthrough Blend Mode in Substance Painter

I won't rush myself. Let me immerse myself in study. UVs I have down. Now there is just this and I'll be able to be an effective 3d artist.

I remember using the pass through in CSP, but I forgot what it is supposed to be.

6:45pm. I just realized something. Tumble and dolly based on where you grab and zoom as opposed to the object center does make sense. In this case it does make it easier to move around.

Let me stop here for lunch. I am overwhelmed by all the options right now. Even though I have the desk in front of me, I am not sure how to begin work on the intricate noise pattern.

6:55pm. When I am in Substance Painter, it feels very similar to Clip Studio Paint.

Right now, it is not that I can't do these patterns, but the problem is that there too many ways of doing them. I can't do them exactly, so I need to pick a simplified way of doing it. There are 100s of brushes to choose from, not to mention textures and materials.

It will take me a while to overcome the inertia.

7:10pm. I really don't feel like doing this anymore for the day. It is torture to have Pt open at this hour. Yesterday I might have gone till past 12am, but that was only because I obsessed about a problem that needed solving. Right now I am still fatigued from getting up too early, and do not have anything immediate I want to do. I just need to study and explore. That kind of play is best done when fresh.

7:55pm. Needed that break. At this point I am really lacking in Pt fundamentals. I need to make up my mind to gradually get into it.

8pm. I'll let it come to me, just not when I am high on stress like this. Sure it might have been better to not spend the most productive part of day messing with UVs, but an issue is finished when you feel satisfied deep down, not when you tell yourself its over. Similarly, I think the main reason why I got up this early is because I really did feel the need to readjust my schedule even if it meant a rough day.

Let me close here. Time for rest and indulgence.

I am going learn Pt and to finish the desk before long. The rest of the props should go a lot faster after that."

---
## [nikhil8617/M1_METRIC_CONVERSION_CALCULATOR](https://github.com/nikhil8617/M1_METRIC_CONVERSION_CALCULATOR)@[d402b1e0b6...](https://github.com/nikhil8617/M1_METRIC_CONVERSION_CALCULATOR/commit/d402b1e0b6152227f965548bef55140af5884d6d)
#### Friday 2022-04-01 19:00:50 by NIKHIL CHANDRA

Add files via upload

Presentation
Knowing the units of estimation that relate with a number can give you a lot more data than a digit as an independent.

Basically, the unit of estimation in science and math fills in as the supporting support point whereupon a number rests.

Unit change is an interaction that includes duplication or division by a mathematical variable.

With the worldwide progression of data that happens nowadays, everybody must get familiar with these most fundamental change factors.

Remembering all the transformation and between change cycles may not be simple for everybody.

A metric transformation number cruncher is a device that delivers some assistance by doing metric changes in couple of moments.

Research
During the French Revolution, the then existing estimation framework was so unrealistic for exchange and logical purposes.

Thus, it set up for the rise of an arrangement of estimation with judiciously related units and straightforward principles for joining them.

Accordingly, a decimal based change framework, called the Metric System, was presented and it was broadly acknowledged by researchers of those days for being a reasonable framework.

The decimal measuring standard was contrived with a point "for all individuals, forever."

Today, the authority arrangement of estimation in the greater part of the nations across the world is the decimal standard otherwise called the "Global System of Units.

However a standard framework, there are numerous units inside the decimal measuring standards and between change is dreary on the grounds that one needs to recall all the transformation factors.

Thus an apparatus that makes every one of these transformation promptly accessible will be an inviting decision.

Cost and Features
Cost
Since the framework utilizes just open source programming, it is liberated from cost..!!

Yet to be determined

Highlights
The different highlights/choices for interconversion of the framework are:

Length
Region
Volume
Mass
Speed
Characterizing the System
Framework Diagram

SWOT ANALYSIS
SWOT-Analysis

4W's and 1'H
Who:
The instrument is some assistance for small kids who might want to counter check their changes and furthermore for logical specialists and mathematicians.

What:
A metric transformation number cruncher that does metric changes in couple of moments.

When:
Whenever individuals are battling with basic transformations or when children might want to cross check their responses while rehearsing or when individuals need change brings about a jiffy to continue on further with their computations.

Where:
Can be put to utilize where basic or progressed logical and mathematic estimations it are involved to require transformations.

How:
The framework opens up to the standard rundown of metric changes that are accessible. Endless supply of one the standard framework, the rundown of between transformations i.e., the sub-framework is displayed on the screen. The client can now pick one sub unit that should be changed over into at least one other sub units that is accessible on the rundown. The outcomes for this multitude of changes are streaked in a moment.

Detail prerequisites
Undeniable Level Requirements:
ID	Description	Status
HR_01	Length	Implemented
HR_02	Area	Implemented
HR_03	Volume	Implemented
HR_04	Mass	Implemented
HR_05	Speed	Implemented
HR_06	Time	Future
HR_07	Temperature	Future
Low level Requirements:
ID	Description	HLR_ID	Status
LR_01	Meter	HR_01	Implemented
LR_02	Centimeter	HR_01	Implemented
LR_03	Foot	HR_01	Implemented
LR_04	Inch	HR_01	Implemented
LR_05	Millimeter	HR_01	Implemented
LR_06	Square Meter	HR_02	Implemented
LR_07	Square Centimeter	HR_02	Implemented
LR_08	Square Foot	HR_02	Implemented
LR_09	MSquare Inch	HR_02	Implemented
LR_10	Square Yard	HR_02	Implemented
LR_11	Cubic Meter	HR_03	Implemented
LR_12	Cubic Centimeter	HR_03	Implemented
LR_13	Litre	HR_03	Implemented
LR_14	Millilitre	HR_03	Implemented
LR_15	Gallon (imperial)	HR_03	Implemented
LR_16	Kilogram	HR_04	Implemented
LR_17	Gram	HR_04	Implemented
LR_18	Ounce	HR_04	Implemented
LR_19	Tonne (metric)	HR_04	Implemented
LR_20	Pound	HR_04	Implemented
LR_21	Meter per Second	HR_05	Implemented
LR_22	Kilometer per Hour	HR_05	Implemented
LR_23	Miles per Hour	HR_05	Implemented
LR_24	Foot per Second	HR_05	Implemented
LR_25	Knot	HR_05	Implemented
LR_26	Hour	HR_06	Future
LR_27	Minute	HR_06	Future
LR_28	Second	HR_06	Future
LR_29	Celcius	HR_07	Future
LR_30	Farenheit	HR_07	Future
LR_31	Kelvin	HR_07	Future

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[65329f4fac...](https://github.com/pytorch/pytorch/commit/65329f4fac8fb22318b7a3eb115e9da207d8d41a)
#### Friday 2022-04-01 20:15:36 by Edward Z. Yang

Disable meta device tests.

After discussion with Can Balioglu, we have concluded that
https://github.com/pytorch/pytorch/pull/53682 , while clever, is more
trouble than it is worth.  The main problem is that whenever someone
adds support for new meta tensors, they then get dozens of new test case
failures, because tests that were previously halted by lack of support
for an operator on meta tensors, now have gotten further and hit some
logic which expects to be able to, e.g., pull out a real value from a
tensor (which clearly doesn't work).  This is very annoying and time
consuming!  Most of these tests aren't written with meta device in
mind, and it's not a good use of time to try to make them more generic.

The plan on record is to switch meta testing to OpInfo, but that patch
will take some time to prepare for now I want to stem the bleeding.  I
don't think we're at high risk for regressions here because meta tensors
mostly share logic with their regular brethren.

Signed-off-by: Edward Z. Yang <ezyangfb.com>

Pull Request resolved: https://github.com/pytorch/pytorch/pull/74468

Approved by: https://github.com/mruberry

---
## [expo/expo](https://github.com/expo/expo)@[d92760eeb2...](https://github.com/expo/expo/commit/d92760eeb25ebd325b0b06a3c3f49bbfe348d4d0)
#### Friday 2022-04-01 22:13:01 by Łukasz Kosmaty

[dev-launcher][iOS] Improve handling of LAN permission crash (#16792)

# Why

Closes ENG-4203.

# How

Try to retry if the network connection was rejected due to the lack of lan permission.
My code will only retry once per app process - in my opinion, we shouldn't save that information in the shared preferences. Retrying one network call isn't that painful even if the failure wasn't connected with the lan permission. That solution was the best, in my opinion, when I was playing with different versions. 

Also, sometimes when the network call was rejected due to the lack of lan permission, retrying it doesn't help, cause the prompt didn't appear in time, but we can't detect that. However, in that case, the app won't longer crash and also the user will be delegated to the error screen. After all, it seems like pretty good UX. 

# Test Plan

- run bare-expo locally ✅

---
## [ss220-space/Skyrat-tg](https://github.com/ss220-space/Skyrat-tg)@[5b8feb6cda...](https://github.com/ss220-space/Skyrat-tg/commit/5b8feb6cda2094dc4c1919539ba1c571ccf6af9c)
#### Friday 2022-04-01 22:14:14 by SkyratBot

[MIRROR] Almost halves airlock auto close delay [MDB IGNORE] (#12314)

* Almost halves airlock auto close delay (#65349)

We go from a delay of 15 seconds, to 8.

This has cheesed me off for a long time. Airlocks should lock, not just
stay open for a quarter of a minute.

This'll help with excited groups that stay permenantly connected at
highpop because of a slowed ssair and doors opening and closing
constantly

Also effects door chasing. I'm honestly just kinda eyeballing this, it
might be a bit much. Even if this goes through could totally be tweaked

Even if this is too low, 15 is way too damn high.

* Almost halves airlock auto close delay

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [cljacoby/hacker-news](https://github.com/cljacoby/hacker-news)@[7908bbb002...](https://github.com/cljacoby/hacker-news/commit/7908bbb002b23701fa8a2b3cd582ab2758056e00)
#### Friday 2022-04-01 22:44:43 by cljacoby

Better Terminal Error Message Formatting (#27)

* Work on better error formatting (and handling)

I want to work on better error reporting at the command line. Something
nice would be akin to cargo's formatted messages. While looking into
how cargo handles errors, I also spent sometime looking at the current
error handling model.

I'm thinking that I can keep using the `fn f() -> Result<(), Box<dyn Error>>`
within the library code to propagate errors. However, there should be a
concept of crossing into the binary/application portion of the code,
where underlying error types should get mapped to a HnError variant.

This maybe achieved by either designating certain portions of the code
base as the library portion vs. the application portion. Or
alternatively, actually segment the code into separate repositories with
respective Cargo.toml types.

* Progress on improving error handling

This commit changes the trait interface for `HnCommand`. It required
that when the `cmd` function returns, the Error type should be a
concrete `HnError` instance. In other words, this means that when we
make it up to the `cmd` function in the call stack, all underlying
errors should be mapped to the concrete error type of the application.

My idea is that this error type will have augmented formatted error
printing capabilities akin to what cargo does.

Possible followup of actually moving the CLI into it's own repository.
Still have mixed feelings on this, so not sure if I will do it.

* More work on using library specific Error type

More work converting all the `Result<T, Box<dyn Error>>` into returns
using the library specific error type. This is making me how little
analysis is takes to drop `Result<T, Box<dyn Error>>` everywhere. I'm
tracing back from the CLI interface through the whole code base to where
it makes most sense to first originate errors.

Not so bad because this would have had to be done eventually. It's still
early enough too that it's not too painful.

* Use application error in error handling

I now resolve all errors to an application defined Error type when
reaching the CLI level, controlled through the trait definition of
HnCommand.

* More work on error formatting

Adding better log statements, specifically around cli commands. I want
to easily tell which subcommand's code path we went down, and if there
is a failure, where about in the code it occurred.

This commit currently sets an invalid url in the `fn thread()` method of
the HtmlClient. I am making this commit because I am about to apply
`cargo fmt`.

* Improve error reporting. Scaffold for fmt'd errors

1. Add an `ERROR` log line for each subcommand invocation if the
subcommand failed.
2. Setup the code to call a `formatted_print()` function defined on my
error type `HnError`. I will model this after how clap does pretty error
messages using the `Message` and `Colorizer` types:
- Message: https://github.com/clap-rs/clap/blob/master/src/parse/errors.rs
- Colorizer: https://github.com/clap-rs/clap/blob/master/src/output/fmt.rs

* Revisions to error handling

* Add colorized error message printing

---
## [PratyushGameDev/6-Hours](https://github.com/PratyushGameDev/6-Hours)@[15718ac65c...](https://github.com/PratyushGameDev/6-Hours/commit/15718ac65c96aa59c54218f8d1733a74eaf1d093)
#### Friday 2022-04-01 23:57:12 by Pratyush

I fixed a lot of bugs just now (read desc)

One, fixed the cursor bug where you couldn't click the buttons
Two, put in the death lose screen whenever you do die
Three, fixed the bug where the radio didn't play
Four, fixed the bug where the flashlight sfx would play when you died
Five, might have fixed the walking sfx bug (haven't playtested)

Now i have some other bugs:

make my website much better
figure out if i want to keep days
maybe if you want find a better radio ward off monster sfx
figure out objectives of other nights & days if i want to keep said days
Lower brightness of bloodOverlay so you can see monster

---

