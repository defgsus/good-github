## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-02-08](docs/good-messages/2022/2022-02-08.md)


1,750,245 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,750,245 were push events containing 2,799,647 commit messages that amount to 226,982,541 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 42 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[906fb0682b...](https://github.com/tgstation/tgstation/commit/906fb0682bab6a0975b45036001c54f021f58ae7)
#### Tuesday 2022-02-08 00:01:46 by necromanceranne

Ballistic to Energy: Autorifles for Thermal Pistols; Adds .38 Crate to Cargo (#64280)

About The Pull Request
The design doc behind this PR, which is only mildy been deviated from on some of the end particulars. Cobby-Approved! Maintainer Discussed!
https://hackmd.io/@6DbtsAKCTtW_9MByKFjZqg/r1xYKCNOt

Cargo Changes
Cargo has had all WT-550's removed and replaced with Thermal Pistols.
Cargo can now order Thermal Pistols, a kind of energy/ballistic hybrid weapon shooting chunks of altered nanites into people. We couldn't use them in people, so maybe we'll use them as bullets! Magma/Ice bullets, to be exact.
You can, after paying a whopping 4K on a goodie pack (you have to pay from your own personal account) buy a .38 revolver. This is mostly to help some poor detective who lost their revolve in what I'm sure will be an inevitable scramble for ballistics. If even the 4K pricetag isn't enough, at least it requires detective access to open the pack...I hope.
Some of the crates that contained autorifle related items have been changed/removed.

unknown (2)

securarevolver 4 0

Science Changes
Ballistic Weaponry node no longer exists, and has been replaced with Exotic Ammo as both the pre-requisite to other nodes, as well as being able to be researched as soon as the Weaponry node is unlocked and not Advanced Weaponry.

Thermal Pistols
-Fairly average bullet statistics; 10 AP but shooting into Energy armor. 20 damage (Brute for cryo, Burn for inferno). Decent wounding potential, but individually much lower ammo counts than lasers.
-Bought in twinned pairs in a two gun holster (just for normal sized energy guns). They're normal sized.
-Each gun has 8 shots (thereabouts). 16 between two.
-Cryo pistols do a knockdown and extra damage against extremely hot targets. Inferno pistols do an explosion cantered on the target against extremely cold targets.
-The guns are EMP-proof.

Why It's Good For The Game
The current gameplay loop of crew combatants is them relying on backup and retreating as necessary to reload their weapons during fights. The ability to repeatedly harry opponents in the field reloads is something that should be moved away from for crew equipment, as it emphasizes lone wolf tactics and one-man army problems, with boxes full of spare ammo usually allowing any single combatant to outlast multiple foes. In addition, ballistics often are not subject to the same (interesting) limitations of energy weapons, so they're typically a no-brainer choice. We shouldn't have such an easy choice be readily available like that.

The thermal pistols present a more challenging weapon to use as a solo combatant but become far more versatile and potent when paired with a decent buddy and basic level co-ordination. They're not a straightforward choice for every situation, but instead are a weapon employed given the right circumstances for them to shine.

In addition to the gameplay issues that ballistics pose, we're in a goddamn spacegame. Unless the ballistics are noticeably weird (they're not), we should expect that our more advanced research station has some pretty odd guns of the energy variety.

Changelog
🆑 Necromanceranne, quin
add: Adds the Inferno and Cryo Pistols. A hybrid energy/ballistic weapon, to cargo. It can be purchased in either a goodies pack or a normal crate order.
add: Thermal Pistols do more damage and a special based on temperature of the target hit.
add: Inferno pistols cause an explosion when they hit a severely cold target.
add: Cryo pistols cause a knockdown and extra damage if they hit a severely hot target.
add: There is a special nanite pistol, which is admin spawned. Don't tell anyone about the forbidden ballistic energy gun.
add: You can order a .38 revolver as a goodie pack. It is expensive.
del: Removes WT-550's from cargo and related content from the techweb/protolathes.
balance: Exotic Ammo is now much earlier in the tech web to take the place of Ballistic Weaponry.
/🆑

---
## [mijiturka/stupid-movie-oracle](https://github.com/mijiturka/stupid-movie-oracle)@[53f5f63885...](https://github.com/mijiturka/stupid-movie-oracle/commit/53f5f63885a02cc658f954db503014e319f96f64)
#### Tuesday 2022-02-08 00:10:57 by Rumyana

Build and configure pyenv with ansible

I kinda hate ansible already

As I wait and wait for it I am filling the time by
reading a blogpost in favour of how useful it is,
because you can use it to install Docker.

I am not joking: https://nickjanetakis.com/blog/docker-and-ansible-solve-2-different-problems-and-they-can-be-used-together

---
## [TychoMagneticAnomaly-1/mpv](https://github.com/TychoMagneticAnomaly-1/mpv)@[649556b2b6...](https://github.com/TychoMagneticAnomaly-1/mpv/commit/649556b2b65207c0d40751fae941223978b04932)
#### Tuesday 2022-02-08 00:20:37 by Dudemanguy

github/workflows: use lua 5.1 on macos

LuaJIT is still actively developed, but upstream is allergic to making
new releases for whatever reason. The last tagged release was in May of
2017, so we probably shouldn't expect a new release anytime soon. Now
for mpv, this doesn't really matter except in the case of macOS where
2.0.5 is actually a bit broken (and of course the CI uses luajit). More
specifically, the 2.0.5 pc is broken and has a "-pagezero_size 10000"
flag which causes libmpv to fail (only executables are allowed to use
this). This magically works on waf. It's possible that it just happens
to ignore the link arguments. However on the meson build, this is broken
and led to a really ugly hack using a partial dependency so both mpv and
libmpv succeed. Fortunately, the 2.1 luajit branch fixes this.
Unfortunately, there's no actual release.

Instead, just use Lua 5.1. Note that lua 5.1 is technically deprecated
in homebrew, but the chances of this going away is pretty slim since
everyone knows that new lua versions are not backwards compatible.
Anyways, using 5.1 works fine and lets us get rid of a terrible hack in
the meson build. People really shouldn't be using 2.0 LuaJIT anyway.

---
## [TychoMagneticAnomaly-1/mpv](https://github.com/TychoMagneticAnomaly-1/mpv)@[f9bf6a601c...](https://github.com/TychoMagneticAnomaly-1/mpv/commit/f9bf6a601c563015706bed7bdb2b4984119db360)
#### Tuesday 2022-02-08 00:20:37 by Dudemanguy

meson: remove horrifying macos luajit hack

See the previous commit for the full explanation. Basically, luajit 2.0
has a bad pc file on macos that causes libmpv to fail during build. The
workaround was, if the os was darwin and luajit was found, to save a
full luajit dep and a partial luajit dep with the link args removed. The
partial dep was used for compiling libmpv, and the full dep was used for
the actual mpv executable. This worked and was needed for the CI to pass
but it sucked. Since the previous commit now makes the CI grab lua 5.1,
we don't need all this crap anymore. Just delete it and treat the
dependency normally.

This does effectively mean that building libmpv with luajit 2.0 on macOS
will no longer work with the meson build. However libraries not being
built correctly is not a mpv-specific issue. The waf build will succeed
for some reason, but it has known issues and it would be better if it
just failed honestly. An upstream developer said years ago that that
macOS users should use the 2.1 branch (and there's no release of
course). In any case, no macOS user should be building mpv with luajit
2.0, so we shouldn't be going out of our way to support this.

https://github.com/mpv-player/mpv/issues/7512
https://github.com/LuaJIT/LuaJIT/issues/521#issuecomment-562999247

---
## [TychoMagneticAnomaly-1/mpv](https://github.com/TychoMagneticAnomaly-1/mpv)@[34e0a212cd...](https://github.com/TychoMagneticAnomaly-1/mpv/commit/34e0a212cd2e0a073a3580952549a62ede38c2d6)
#### Tuesday 2022-02-08 00:20:37 by Dudemanguy

wayland: partially fix drag and drop handling

Drag and drop in wayland is weird and it seems everyone does this
slightly differently (fun). In the past, there was a crash that
occured (fixed by 700f4ef5fad353800fa866b059663bc1dd58d3b7) which
involved using the wl_data_offer_finish in an incorrect way that
triggered a protocol error (always fatal). The fix involved moving the
function call to data_device_handle_drop which seemingly works, but it
has an unfortunate side effect. It appears like GTK applications (or at
least firefox) close the pipe after this function is called which makes
it impossible for mpv to read data from the fd (well you could force it
open again in theory but let's not do that). Who knows if that was the
case when that commit was made (probably not because I'd think I would
have noticed; could just be a dummy though), but obviously having broken
dnd for a major application isn't so fun (this works with QT and
chromium anyway).

Ideally one would just simply check the pipe in data_device_handle_drop,
but this doesn't work because it doesn't seem the compositor actually
sends mpv the data by then. There's not actually a defined event when
you're supposed to be able to read data from this pipe, so we wait for
the usual event checking loop later for this. In that case,
wl_data_offer_finish needs to go back into check_dnd_fd, but we have to
be careful when calling it otherwise we'd just commit protocol errors
like before. We check to make sure we even have a valid wl->dnd_offer
before trying to indicate that it is finished and additionally make sure
there is a valid dnd_action (after checking the fd, it's always set back
to -1).

This doesn't fix everything though. Specifically, sway with
focus_follows_mouse (the default) and GTK as the data source still
doesn't work. The reason is that when you do a drag and drop in sway
with that option on, a new wl_data_device.data_offer event is sent out
instantly after the drop event. This happens before any data is sent
across the fd and before mpv even has a chance to check it. What GTK
does, when getting this new data_offer event, is close the pipe
(POLLHUP). This means mpv can't read it when we reach the event loop and
thus no data is ever read and broken drag and drop. From the client
side, this isn't really fixable since the wayland protocol doesn't have
a clear indication of when clients are supposed to read from the fd and
both the compositor and data source are doing things totally out of our
control. So we'll consider this weird case, "not our bug" at least. The
rest should work.

---
## [SPLURT-Station/S.P.L.U.R.T-Station-13](https://github.com/SPLURT-Station/S.P.L.U.R.T-Station-13)@[a44973ea6a...](https://github.com/SPLURT-Station/S.P.L.U.R.T-Station-13/commit/a44973ea6a448f1b75da30e91347cd9ee7a8f8b8)
#### Tuesday 2022-02-08 00:21:17 by PurpleFenn

Add RTC

This was originally meant to be a joke but I kinda liked the idea so
fuck it. Enjoy, nerds.

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[b48cda6afa...](https://github.com/san7890/bruhstation/commit/b48cda6afa047be95390dc1360e8d899ec6394b0)
#### Tuesday 2022-02-08 00:22:15 by LemonInTheDark

Fixes harddels in pinned module code, cleans up a musty pattern that I want to die (#64674)

* Please stop typecasting target, noooooooooooooooooo

* Fixes harddels in pinned module code

The logic for pinned modules was intentionally hanging references to the
mob that pinned the action button. I have depression.

The pinned_to list also was never fully cleared, but that would have
just exasperated the issue. I've converted its use of mobs to refs, and
its use of the module var into something better managed

(Friendly reminder that actions will persist in your nightmares forever
unless they are manually qdel'd, this code wasn't doing that.

Also cleaned up how the pinned_to list is managed, hopefully it's a bit
more action centered now

---
## [sailfishos-mirror/rust](https://github.com/sailfishos-mirror/rust)@[734368a200...](https://github.com/sailfishos-mirror/rust/commit/734368a200904ef9c21db86c595dc04263c87be0)
#### Tuesday 2022-02-08 00:45:24 by bors

Auto merge of #87869 - thomcc:skinny-io-error, r=yaahc

Make io::Error use 64 bits on targets with 64 bit pointers.

I've wanted this for a long time, but didn't see a good way to do it without having extra allocation. When looking at it yesterday, it was more clear what to do for some reason.

This approach avoids any additional allocations, and reduces the size by half (8 bytes, down from 16). AFAICT it doesn't come additional runtime cost, and the compiler seems to do a better job with code using it.

Additionally, this `io::Error` has a niche (still), so `io::Result<()>` is *also* 64 bits (8 bytes, down from 16), and `io::Result<usize>` (used for lots of io trait functions) is 2x64 bits (16 bytes, down from 24 — this means on x86_64 it can use the nice rax/rdx 2-reg struct return). More generally, it shaves a whole 64 bit integer register off of the size of basically any `io::Result<()>`.

(For clarity: Improving `io::Result` (rather than io::Error) was most of the motivation for this)

On 32 bit (or other non-64bit) targets we still use something equivalent the old repr — I don't think think there's improving it, since one of the fields it stores is a `i32`, so we can't get below that, and it's already about as close as we can get to it.

---

### Isn't Pointer Tagging Dodgy?

The details of the layout, and why its implemented the way it is, are explained in the header comment of library/std/src/io/error/repr_bitpacked.rs. There's probably more details than there need to be, but I didn't trim it down that much, since there's a lot of stuff I did deliberately, that might have not seemed that way.

There's actually only one variant holding a pointer which gets tagged. This one is the (holder for the) user-provided error.

I believe the scheme used to tag it is not UB, and that it preserves pointer provenance (even though often pointer tagging does not) because the tagging operation is just `core::ptr::add`, and untagging is `core::ptr::sub`. The result of both operations lands inside the original allocation, so it would follow the safety contract of `core::ptr::{add,sub}`.

The other pointer this had to encode is not tagged — or rather, the tagged repr is equivalent to untagged (it's tagged with 0b00, and has >=4b alignment, so we can reuse the bottom bits). And the other variants we encode are just integers, which (which can be untagged using bitwise operations without worry — they're integers).

CC `@RalfJung` for the stuff in repr_bitpacked.rs, as my comments are informed by a lot of the UCG work, but it's possible I missed something or got it wrong (even if the implementation is okay, there are parts of the header comment that says things like "We can't do $x" which could be false).

---

### Why So Many Changes?

The repr change was mostly internal, but changed one widely used API: I had to switch how `io::Error::new_const` works.

This required switching `io::Error::new_const` to take the full message data (including the kind) as a `&'static`, rather than just the string. This would have been really tedious, but I made a macro that made it much simpler, but it was a wide change since `io::Error::new_const` is used everywhere.

This included changing files for a lot of targets I don't have easy access to (SGX? Haiku? Windows? Who has heard of these things), so I expect there to be spottiness in CI initially, unless luck is on my side.

Anyway this large only tangentially-related change is all in the first commit (although that commit also pulls the previous repr out into its own file), whereas the packing stuff is all in commit 2.

---

P.S. I haven't looked at all of this since writing it, and will do a pass over it again later, sorry for any obvious typos or w/e. I also definitely repeat myself in comments and such.

(It probably could use more tests too. I did some basic testing, and made it so we `debug_assert!` in cases the decode isn't what we encoded, but I don't know the degree which I can assume libstd's testing of IO would exercise this. That is: it wouldn't be surprising to me if libstds IO testing were minimal, especially around error cases, although I have no idea).

---
## [Pika-Software/gpm](https://github.com/Pika-Software/gpm)@[5c2a06a77f...](https://github.com/Pika-Software/gpm/commit/5c2a06a77fa2156a3fab76d9f96e8f261295ce52)
#### Tuesday 2022-02-08 00:52:50 by PrikolMen:-b

Fuck the rubat and his whole family, 2 fucking hours I fucked to understand the fact that this fag blocked reading the files received from the server in the name of his schizophrenia and sick security obsession

---
## [SollyW/Skewer](https://github.com/SollyW/Skewer)@[b8868ed707...](https://github.com/SollyW/Skewer/commit/b8868ed707ad80f754338b4ca48a308c60beae36)
#### Tuesday 2022-02-08 00:56:07 by Jack Papel

Skewers are now functional! + Major refactors

Condiment tags are still kinda fucky wucky

Practically everything is brand new, as if it were from scratch.

Lots of changes. To be honest I've been working on this so long, and I'm tired, and I don't remember everything. But I'll list some:
Dev command
CondimentItem
Idk everything just feels better, less loosey-goosey. Like proper I guess.
Hopefully it's easier for you folks to work with.

Alright,
Night.

---
## [bm16ton/i2c-star-blackpill-gpio](https://github.com/bm16ton/i2c-star-blackpill-gpio)@[10867e1a40...](https://github.com/bm16ton/i2c-star-blackpill-gpio/commit/10867e1a403f5752c1f8ed2aed6bae60e003be37)
#### Tuesday 2022-02-08 01:04:00 by bm16ton

pwm now works but is horrible hack...whats worse then hack? anyway period and duty cycle are ignored until enabled once enabled only duty cycle work/updates the pwm and its fucking ugly

---
## [ViktorKoL/tgstation](https://github.com/ViktorKoL/tgstation)@[413fd90502...](https://github.com/ViktorKoL/tgstation/commit/413fd9050271829e2899b88a676995ae2517111c)
#### Tuesday 2022-02-08 01:09:21 by GoldenAlpharex

Dullahan Partial Refactor: They Work Again Edition (#63696)

So, a few months ago I was like "hmm there's something weird going on with party pods...", which got me looking into important_recursive_hearers or something like that. I spoke about it in the coding channel and Kyler actually fixed it before I did. But I also caught a similar glitch with Dullahans, so I decided to investigate...

Two months later...

I present to you a partial unfuckening of the Dullahans, in that I made them fully functional once again:

They only hear speech through their head (not sounds, sadly, someone else would have to tell me how to do that because I otherwise really wouldn't know how to do it in a sane way), they speak through their head, runechat-included.
When you spawn a Dullahan, you're set to look through the Dullahan's eyes (so from their head), and that doesn't reset when you log off and back in, or admin-ghost and come back in your body.
When you're looking through your head, your view will no longer be reset to your body upon entering a locker, which is nice to avoid not being blind while looking through your body.
Dullahan heads no longer look completely lifeless and without organs. They have eyes that don't look dead and that even match the player's intended eye color.
Dullahan can now properly examine things from their head, which was intended and 100% not functional.
Dullahan heads now speak with the proper name of their owner, instead of having a random name attached to it at round-start.
Dullahan heads are also now properly named too.
Dullahans can now properly whisper, sing and do all these funny things that they were unable to do before.
Dullahan whispers will now properly respect the range of the whisper.
Dullahans can now succumb in hardcrit by whispering, as intended. This potentially fixes other species that worked similarly not being able to succumb, like abductors, although I didn't test if they normally could, I just know they absolutely will be able to now.
When switching from Dullahans to a different species, your old head will no longer stay behind.
I also added a proc for species to do some code when we get a ckey login in our mob, which could potentially be useful for other stuff in the future, but it was necessary here as the view is reliant on the client, which we want to ensure doesn't get weird view glitches like having their head's vision overlay while actually being centered on their body.

I also made it so say() now takes a range argument, which is 7 by default, just so things that aren't humans can also whisper and do all those kinds of things. Going with that, there's probably a few more things that will be able to be done better thanks to this, although I haven't tested every edge case with this, but I doubt it will make much of a difference in the future.

---
## [benjaminRomano/rules_kotlin](https://github.com/benjaminRomano/rules_kotlin)@[15dd1de6dd...](https://github.com/benjaminRomano/rules_kotlin/commit/15dd1de6dd1431c5d2f7d2d7f1179a951d63a328)
#### Tuesday 2022-02-08 01:30:23 by Christian Edward Gruber

Expose kotlinc's -Xfriend-paths to all jvm/android kt rules under the attribute 'assocates=' (#465)

Associates lets a library associate it self to other libraries, making them part of the same module. This is constrained such that while multiple libraries may be associated, they must all shard the same module, and so cannot associate to anything that is part of a different module. These module relationships are in the bazel build graph, not the contents of the jars as such.

This module membership is transitive (within the above-mentioned constraint), though strict-deps would stop that. Also, only kotlin targets can be associated.

Per discussions across several media, the name "associates" was chosen over "friends" (despite the kotlinc flag being -Xfriend-paths) as that is the terminology used in the gradle kotlin plugin, which is kotlin's primary delivery vehicle, and to avoid confusion with the C++ friends concepts. The pre-existing "friends" attribute is preserved for backward compatibility with a warning. Future PR will add a flag to turn off that support, and then we'll delete it.

kt_jvm_import does not include this facility, but these can just set their module_name in common to participate.

Android should work, but because kt_android_* is a macro not a rule, the implicit target //my/android/library:mytarget_kt should be friended, since it has a KtJvmInfo. The //my/android/library will macro-resolve into an android_library. Until the android rules get the right kind of love, such that we can make a rule that has KtJvmInfo AND android-whatever providers, this simply is a known limitation we'll have to live with.

Also, the prior implementation shoved the full transitive closure (all jars, kotlin or no) of the friend= into the -Xfriends-paths flag, which is awful. This PR does break that, in case people were relying on that by some oddity. The fix is to just add the targets directly.

Fixes #211

---
## [MooglyGuy/mame](https://github.com/MooglyGuy/mame)@[a49e215466...](https://github.com/MooglyGuy/mame/commit/a49e2154666b0ee7423e2d859c21b7592a4c61b8)
#### Tuesday 2022-02-08 02:14:09 by Firehawke

Apple II updates for January 2022 (#9189)

* New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

Earth Science: Interplanetary Travel (cleanly cracked) [4am, Firehawke]
Isaac Newton and F.I.G. Newton (cleanly cracked) [4am, Firehawke]
Return to Reading: The Call of the Wild (cleanly cracked) [4am, Firehawke]
The German Hangman (cleanly cracked) [4am, Firehawke]
Legionnaire (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

Bridge Tutor with Precision and Scientific Bidding (cleanly cracked) [4am, san inc, Firehawke]
The French Hangman (cleanly cracked) [4am, Firehawke]
The Russian Hangman (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_orig.xml)
----------------------------------------------------------

Mickey's Space Adventure [4am, Firehawke]
The Environment Life Dynamic [4am, Firehawke]

* New working software list additions (apple2_flop_orig.xml)
----------------------------------------------------------

Stellar Power [4am, Firehawke]

New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

Ken Uston's Professional Blackjack (Version 1.12) (cleanly cracked) [4am, Firehawke]
Dinosaur's Lunch (cleanly cracked) [4am, Firehawke]
Race Car Keys (cleanly cracked) [4am, Firehawke]
Functional Harmony: Basic Chords (cleanly cracked) [4am, Firehawke]
Functional Harmony: Diatonic Seventh Chords (cleanly cracked) [4am, Firehawke]
Functional Harmony: Borrowed and Altered Chords (cleanly cracked) [4am, Firehawke]
Building Reading Skills: The Letter-Sound Farm (cleanly cracked) [4am, Firehawke]
Follow Me (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

The German Hangman (Revision 2) (cleanly cracked) [4am, Firehawke]
The Russian Hangman (Revision 2) (cleanly cracked) [4am, Firehawke]
The Spanish Hangman (Revision 2) (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

Exploring Library Land (cleanly cracked) [4am, Firehawke]
Library Treasure Hunt (cleanly cracked) [4am, Firehawke]
Expedition U.S.A.! (cleanly cracked) [4am, Firehawke]
Codes and Cyphers (cleanly cracked) [4am, san inc, Firehawke]
Ripley's Believe It Or Not: Beginning Library Research Skills (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_orig.xml)
----------------------------------------------------------

Glutton [4am, Firehawke]

---
## [Lianvee/Shiptest](https://github.com/Lianvee/Shiptest)@[031c0866ed...](https://github.com/Lianvee/Shiptest/commit/031c0866ed35af71a3ac4782fe4d6aa9e6464f53)
#### Tuesday 2022-02-08 02:45:42 by SweetBlueSylveon

Nanotrasen Deserter Vault Ruin (#732)

* Nanotrasen Deserter Vault Ruin

A ruin based around a Nanotrasen ultra secure vault. It should spawn on the ice planet. This commit adds everything.

* Map Changes

-Replaces Glockroach family with Jack and Jill, Slaughter and Laughter demons.
-Replaces Sniper Rifle with Particle Acceleration Rifle.
-Replaces Sniper Rifle ammo with a single upgraded weapon power cell.
-Adds a sentience potion and cns rebooter implant to vault safe since there were only mats in it otherwise.

* Minor commit

Removes a cybernetic that should have been removed before the last commit.

* Update code/game/area/areas/ruins/icemoon.dm

I'm dumb and didn't realize I did this. Also didn't realize linters was the code checker, so I didn't realize to check the code. I know now! Thanks for the help.

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

* Adds the knight gear design disk.

Adds the "magical disk of smithing" to the safe.

* Unmodularizes your Modularization

Moves the datum to an unmodularized folder.

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

---
## [Nerev4r/Skyrat-tg](https://github.com/Nerev4r/Skyrat-tg)@[eb384bd2d7...](https://github.com/Nerev4r/Skyrat-tg/commit/eb384bd2d72a5b23dd9785cc06815049d507d3d5)
#### Tuesday 2022-02-08 02:46:13 by Useroth

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
## [R2Northstar/NorthstarLauncher](https://github.com/R2Northstar/NorthstarLauncher)@[2bc20f0eef...](https://github.com/R2Northstar/NorthstarLauncher/commit/2bc20f0eefd20fbd9f48d188221fec90c8c4b438)
#### Tuesday 2022-02-08 03:12:11 by Emma Miler

Added code for chathooks

This may not seem like much to a passing observer, but this commit took me 30 hours of blood, sweat, tears, IDA debugging, server crashes, and insanity.

---
## [PixelPlusUI-Devices/alioth_kernel_xiaomi_sm8250](https://github.com/PixelPlusUI-Devices/alioth_kernel_xiaomi_sm8250)@[fbbff41261...](https://github.com/PixelPlusUI-Devices/alioth_kernel_xiaomi_sm8250/commit/fbbff412610f09dd8a436ccc5c82b28420d88772)
#### Tuesday 2022-02-08 04:30:22 by George Spelvin

lib/list_sort: optimize number of calls to comparison function

CONFIG_RETPOLINE has severely degraded indirect function call
performance, so it's worth putting some effort into reducing the number
of times cmp() is called.

This patch avoids badly unbalanced merges on unlucky input sizes.  It
slightly increases the code size, but saves an average of 0.2*n calls to
cmp().

x86-64 code size 739 -> 803 bytes (+64)

Unfortunately, there's not a lot of low-hanging fruit in a merge sort;
it already performs only n*log2(n) - K*n + O(1) compares.  The leading
coefficient is already at the theoretical limit (log2(n!) corresponds to
K=1.4427), so we're fighting over the linear term, and the best
mergesort can do is K=1.2645, achieved when n is a power of 2.

The differences between mergesort variants appear when n is *not* a
power of 2; K is a function of the fractional part of log2(n).  Top-down
mergesort does best of all, achieving a minimum K=1.2408, and an average
(over all sizes) K=1.248.  However, that requires knowing the number of
entries to be sorted ahead of time, and making a full pass over the
input to count it conflicts with a second performance goal, which is
cache blocking.

Obviously, we have to read the entire list into L1 cache at some point,
and performance is best if it fits.  But if it doesn't fit, each full
pass over the input causes a cache miss per element, which is
undesirable.

While textbooks explain bottom-up mergesort as a succession of merging
passes, practical implementations do merging in depth-first order: as
soon as two lists of the same size are available, they are merged.  This
allows as many merge passes as possible to fit into L1; only the final
few merges force cache misses.

This cache-friendly depth-first merge order depends on us merging the
beginning of the input as much as possible before we've even seen the
end of the input (and thus know its size).

The simple eager merge pattern causes bad performance when n is just
over a power of 2.  If n=1028, the final merge is between 1024- and
4-element lists, which is wasteful of comparisons.  (This is actually
worse on average than n=1025, because a 1204:1 merge will, on average,
end after 512 compares, while 1024:4 will walk 4/5 of the list.)

Because of this, bottom-up mergesort achieves K < 0.5 for such sizes,
and has an average (over all sizes) K of around 1.  (My experiments show
K=1.01, while theory predicts K=0.965.)

There are "worst-case optimal" variants of bottom-up mergesort which
avoid this bad performance, but the algorithms given in the literature,
such as queue-mergesort and boustrodephonic mergesort, depend on the
breadth-first multi-pass structure that we are trying to avoid.

This implementation is as eager as possible while ensuring that all
merge passes are at worst 1:2 unbalanced.  This achieves the same
average K=1.207 as queue-mergesort, which is 0.2*n better then
bottom-up, and only 0.04*n behind top-down mergesort.

Specifically, defers merging two lists of size 2^k until it is known
that there are 2^k additional inputs following.  This ensures that the
final uneven merges triggered by reaching the end of the input will be
at worst 2:1.  This will avoid cache misses as long as 3*2^k elements
fit into the cache.

(I confess to being more than a little bit proud of how clean this code
turned out.  It took a lot of thinking, but the resultant inner loop is
very simple and efficient.)

Refs:
  Bottom-up Mergesort: A Detailed Analysis
  Wolfgang Panny, Helmut Prodinger
  Algorithmica 14(4):340--354, October 1995
  https://doi.org/10.1007/BF01294131
  https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.6.5260

  The cost distribution of queue-mergesort, optimal mergesorts, and
  power-of-two rules
  Wei-Mei Chen, Hsien-Kuei Hwang, Gen-Huey Chen
  Journal of Algorithms 30(2); Pages 423--448, February 1999
  https://doi.org/10.1006/jagm.1998.0986
  https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.4.5380

  Queue-Mergesort
  Mordecai J. Golin, Robert Sedgewick
  Information Processing Letters, 48(5):253--259, 10 December 1993
  https://doi.org/10.1016/0020-0190(93)90088-q
  https://sci-hub.tw/10.1016/0020-0190(93)90088-Q

Feedback from Rasmus Villemoes <linux@rasmusvillemoes.dk>.

Link: http://lkml.kernel.org/r/fd560853cc4dca0d0f02184ffa888b4c1be89abc.1552704200.git.lkml@sdf.org
Signed-off-by: George Spelvin <lkml@sdf.org>
Acked-by: Andrey Abramov <st5pub@yandex.ru>
Acked-by: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Reviewed-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Cc: Daniel Wagner <daniel.wagner@siemens.com>
Cc: Dave Chinner <dchinner@redhat.com>
Cc: Don Mullis <don.mullis@gmail.com>
Cc: Geert Uytterhoeven <geert@linux-m68k.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [tluxe13/Skyrat-tg](https://github.com/tluxe13/Skyrat-tg)@[1dfcffccd1...](https://github.com/tluxe13/Skyrat-tg/commit/1dfcffccd1d453fc0d3f928f5dfa1d3115f977f9)
#### Tuesday 2022-02-08 04:59:45 by Zenitheevee

Tarkon Update 1.5: Meet the Ensign  (#11089)

* THE LORE, GUYS, THE LORE

* P-T 1.5: Meet The Ensign

* Dont remember, live is fucky and i need to test shit

* So many active turfs now fixed...

* Medical Malpractice: Swapped patients thumbs with their big toes.

* THE SOOOUUUULLLLLLLNGNGHHGHGHHH

* ok maybe i want this back.

* some other stuff and future-proof testing

---
## [trpo2022/hw-IVTFROLLER](https://github.com/trpo2022/hw-IVTFROLLER)@[5c780d2e66...](https://github.com/trpo2022/hw-IVTFROLLER/commit/5c780d2e6651dd025c598b788a9e2bb9aeb65097)
#### Tuesday 2022-02-08 05:22:09 by Pavel Borinskiy

Testing file created ( another one time becasue that mfker named Ruslan cannot agreed with his stupid comp lmao omg sorry

---
## [Koi-3088/ForkBot.NET](https://github.com/Koi-3088/ForkBot.NET)@[f8eac54e21...](https://github.com/Koi-3088/ForkBot.NET/commit/f8eac54e2173a9841d8d249e860ef5116125a0e2)
#### Tuesday 2022-02-08 05:32:13 by Koi

Mr. Mime is a thing, unfortunately.
Mild clean, some more Cherish set handling attempts.
Exclude set MetDate from mystery gifts.
Fix daycare enum parsing.
Check for no result in case $qc was used or some other weird thing happens.
Remove FixOT and TradeCord as routine types (FlexTrade handles both).
Try to apply trainer info for Mystery gifts.
Re-add fixed met date if not GO origin.
Update DenBot distribution data, minor fixes.
Fix Yamask-Galar in daycare, some more oopsies.
-Add DenBot - a seed lookup and day skipper bot for raids.
-Change AutoRoll's behavior to make use of some of DenBot's functionality.
Minor clean.
Revise TradeCord "traded" check, remove potential user path straggler entries because paranoia, some minor fixes.
TradeCord fixes (shocker, I know).
Extract Json serializer.
Minor clean and fixes.
Minor fixes.
Fix Milcery when an Alcremie variant is a parent.
Update to latest Core and ALM dependencies.
Handle non-shiny events in a better way.
Work around a race condition?
Simplify and de-bugify trade completion check.
Fix indexing, improve chance for Melmetal-Gmax because it's nigh impossible to get.
Rework TradeCord internals, add new functionality:
-Migrate user data from ".txt" files to a serialized Json (migration for a large amount of users will take a few minutes, be patient).
-Make TradeCord configurable, add its own settings category.
-Add some template events with an optional end timer (YYYY/MM/DD 8PM as an example, though any local time format should work).
-Add barebones Pokedex (counter, flavor text).
-Can check dex completion by typing `$dex`, check missing entries by typing `$dex missing`.
-Completing the Pokedex will slightly improve shiny rate.
-Can now mass release cherish event Pokemon and shinies ($massrelease shiny/cherish).
-Various tweaks, improvements, and bugfixes.

Slightly change FixOT's behavior:
-If a shown Pokemon is illegal and an event, attempt to find a match within the MGDB first.
-Try to force users to trade away the shown Pokemon, log attempt to change shown Pokemon.
Add consideration for easter eggs being enabled in settings, fix Suicune
Change species rng for TradeCord, some bugfixes (I really need to rewrite this mess)
Add check if we're using ListUtil for Giveaway instead of TradeCord.
Amend commit since I'm squashing and force-pushing while bringing the fork in line with the main branch
Add Giveaway module to Discord bot (#22)

Thanks, rigrassm.
Co-authored-by: Koi-3088 <61223145+Koi-3088@users.noreply.github.com>
Specify USB port instead of adding the first result (can be found via Device Manager).
Re-add boolean check because we don't want to fix everything
FixOT will attempt to regenerate illegal Pokémon.
Apply trash bytes for reasons.
Minor TradeCord fixes and adjustments.
Minor clean for C#9
Use "GetValidPreEvolutions()" instead of "GetPreEvolutions()".
Index forms correctly.
Fix the fixed and re-introduced empty daycare index error.
*an* Ultra Ball.
Add EvoTree breeding for TradeCord.
Remove unnecessary value declarations for pinging on encounter match.
Mildly beautify EncounterBot mark output.
Integrate Anubis' system update prevention into Soft Reset and Regigigas Encounter Modes.
Rename "Regi" Encounter Mode to "Soft Reset".
Speed up "A" clicks for Regigigas and Soft Reset modes.
Add Mark logging output for EncounterBot.
Fix oops (re-order logic, remove unnecessary lines).
Add optional species and form specification for $massrelease
Use an obscure string splitter because people like symbols in their names.
Fix things that broke after rebasing to the latest main repo commit.
Use a less unfortunate field name and value splitter...again.
Fix Marowak-Alola always generating as an NPC trade.
Add filters for "$list <species>" to narrow down results.
Fix Cherish Pichu and Octillery
Stop making dumb mistakes, me (implying the rest of it isn't a dumb mistake).
Can't breed antiques.
Use a less unfortunate embed name and value splitter
Add Melmetal-Gmax to TradeCord.
Add ability to search by caught ball.
Have MassRelease ignore events.
Add specific regional form breeding.
Revise egg rate and egg shiny chance.
Have trade evolutions hold an Everstone.
Add an extra right click when navigating to settings for AutoRoll.
Add reworked encounter/egg/fossil logs.
Minor clean.
Minor clean.
Get rid of EncounterBot, FossilBot, EggFetch text logs until I properly rework them.
Break on an empty page due to aggressive rounding
Add multi-page lists for Tradecord.
More random bugfixes.
Fix some bugs before major clean
Add Language parameter for TradeCord.
Change trainer info input format for TradeCord.
Move focus on Showdown set instead of randomizing a pkm file.
Allow user to enter whatever they want for $list, handle edge cases like Kommo-o
Add "$list all" to show non-duplicate caught species.
Automatically remove from favorites if trading or gifting (small QOL thing).
Change how favorites are removed from user file.
Revert base egg shiny chance nerf.
Fix daycare
Add favorites command to TradeCord.
Slightly nerf eggs.
Fix TradeCord list for shinies
Add TradeCord (my dumbest and messiest project so far, Archit pls don't hate the mess).
Add Showdown output for Star/Square shinies and OTGender.
Add optional link code input for FixOT.
Change how OTName, TID, SID is displayed.
Add Regigigas SR bot.
Add SoJ Camp SR bot.
Ribbons now work with EggTrade (remove ribbons if egg).
Remove EggRoll.
Add another filter for FixOT
Fix.. FixOT
Update offsets for EncounterBot catching.
Slightly change StrongSpawn to work with Regi SR and make it its own mode.
Make SpinTrade only available for USB-Botbase
Update valid eggs for CT
winforms: resize icon.ico to fix crash at startup on unix using mono
Rework Spin, read initial in-game coordinates in order to correct drift
Add TID, SID, Language output for Showdown
Remove obsolete OT and Language parsing
Very minor clean until I have time for a proper one.
Detach controller when stopping USB bot.
Actually set LastUsedBall for EncounterBot (missed when bringing in line with main repo)
Move extra RaidBot timings following the official commit
Remove PKHeX Discord invite from Readme.md

Maybe fewer people will pester devs now about my unofficial fork?
Update for latest main repo EncounterBot commits.
Update README.md
Add back best commit: Red's SpinTrade.
Add egg trades, foreign Dittos and OT for Twitch.
If ItemMule is enabled, also display the item a user is receiving.
Add periodic time sync toggle for all methods of hosting (except for non-soft locked AutoRoll) to (hopefully) prevent den rollover during extended hosts.

Add routine to exit a lobby for SoftLock if no players are ready in time (to preserve soft lock).

Add a routine to recover from disbanded lobbies (when someone disconnects unexpectedly) for SoftLock.

Add a routine to restart game if all else fails and we're stuck in a raid.

Add a routine for adding and deleting friends if we're soft locked and raids go empty.

Slightly reorganize settings, extract methods, minor clean.
Don't use such a generic file name for stream assets.
Check USB port index for running bots. Should fix adding additional USB bots when no config is saved.
Add fixed met date for FixOT.
How do I boolean
Change airplane mode logic, tweak timings and routine for soft lock lobby exit
Rework EggRoll cooldown (static list in favor of a txt file).
Start clean up and refactor
Add setting to increase delay after pressing "Home" after a date skip.
Use USB port index for blocking and sprite pngs if connection type is USB
Add option for airplane host (usb-botbase required)
Add option to softlock on selected species for AutoRoll
Add automatic compatibility for all console languages when date skipping (have to set ConsoleLanguage under ScreenDetection)
Attempt to fix multiple USB device add and connect...again
Minor clean
Fix oops?
Handle add/remove of bots
Distinguish between multiple USB devices, tweak BotRemoteControl for USB, other various fixes
Add SpA modifier for foreign Dittos
Add alpha USB-Botbase support
Fix DateTime parsing for European format for EggRoll
Set fixed EggMetDate and MetDate for EggRoll
More FixOT filters
Remove Beheeyem. Oops.
Split EggRoll into its own routine and trade type, only output "Receiving: Mysterious Egg" if routine is EggRoll, other minor tweaks and fixes
Make FixOT its own queue with roles and counts
Add a couple more OTs to $fix
Parsing for EggRaffle auto-clear and $clearcooldown
Adjust timings and split Watt collecting clicks for AutoRoll
Fix oops with file attachments for Ditto
Further improvements for OT, memes for invalid pokemon (disable EasterEggs)
Add spaces, digits for OT
Randomize memes, cut down bloat
Fix miscellaneous bots after Anubis' recent QOL additions
-Ignore events for OT because headache.
-Add overlooked "$convert <generation>" input for OT.
-Move $clearcooldown to SudoModule
-Clear timer automatically if NoTrainerFound
-More reliable Dittos
-Foreign Dittos for $convert
-Command to clear cooldown for EggRaffle in case trade gets disconnected
-Fix "Trade finished" line to keep result secret
-EggRaffle as a toggle, option to specify channels
-Seed Check output to both DMs and Channel (apparently some want it)
-Randomly generated egg raffle via a "$roll" command with a configurable cooldown
-FixAdOT reworked, has its own command "$fix" and no longer overrides $clone
-Ball: <value> output for Showdown sets
-Fix oversight
-Option to output Seed Check results to Discord channel with a User mention
-Showdown set output for OT name and eggs
-Basic "OT: <name>" option without Showdown set output
-Initial $convert support for EggTrade
-Egg moves for EggTrade test attempt
-Minor update
-EggTrade (by nicknaming a Pokémon "Egg" using $trade)
-Failsafe for memes if enabled but field left blank or incomplete
-Niche breedable Ditto trade mode.
Add minimize button
EggFetch text logs
StrongSpawn mode for EncounterBot
Re-add EncounterBot Master Ball catching
More parsing for FixAdOTs
Park Ball as held item instead of string
Actually remove the offset instead of saying I did
Initial DLC commit
Faster code entry
Removed catching for EncounterBot (need a new offset)
CloneBot mode to fix Nickname and OT if adverts detected

---
## [cyberitsolutions/bootstrap2020](https://github.com/cyberitsolutions/bootstrap2020)@[4e5cc0c72e...](https://github.com/cyberitsolutions/bootstrap2020/commit/4e5cc0c72ec11ee6fe4e279fbb5c39b5f00a2f1e)
#### Tuesday 2022-02-08 05:41:07 by Trent W. Buck

13:49 <twb> On my regular Debian 11 system, "logger test" appears in "journalctl -fn0".  On my hardened system, it doesn't.  This is the case regardless of whether root or a GUI user runs "logger test".
13:49 <twb> Where should I be looking to isolate this fault?
13:49 <twb> Hrm, it seems /dev/log is not a symlink on the hardened system
13:49 <twb> That seems very likely to be a problem...
13:53 <twb> journald doesn't appear upset in any way, and /run/systemd/journal/dev-log exists, bit /dev/log is not symlinked to it
13:53 <twb> If I make that symlink, it works right away
13:55 <Edu4rdSHL> When hardened is not hardened :p
13:55 <Edu4rdSHL> I mean, it should be even more aggresive in logging events
13:57 <twb> systemd-journald-dev-log.socket  should be it
13:57 <twb> Which is running
13:58 <twb> So my thinking is that symlink was made and then delted OR someting else wrote over the top
13:59 <damjan> or your user sessions getting a different /dev ?
13:59 <twb> OK the problem is rsyslogd somehow
13:59 <damjan> you're running rsyslogd too?
13:59 <twb> Even though rsyslogd is only running to act as a RELP client
14:00 <twb> Because journald is shit and doesn't implement anything except HTTP pull
14:00 <twb> module(load="imuxsock") looks wrong
14:01 <twb> It should be automatically detecting journald and using "read from journald" mode
14:01 <twb> bootstrap:>$t/etc/rsyslog.conf printf %s\\n 'module(load="imuxsock")' 'module(load="omrelp")' 'action(type="omrelp" target="logserv" port="2514" template="RSYSLOG_SyslogProtocol23Format")'
14:01 <twb> ^ that's the old code
14:02 <twb> The new code is basically the same except it's generated at boot time.
14:03 <twb> https://github.com/cyberitsolutions/bootstrap2020/blob/main/debian-11-main/get-config-from-dnssd.service
14:10 <twb> Which also explains why I hadn't noticed before because logger--/dev/log-->rsyslogd--relp-->logserv  is still working, so log events still appear on the central logserv
14:11 <twb> rsyslogd is supposed to detect systemd is pid1 and switch to "read from journald, not /dev/log" mode, and I think that is somehow failing due to a race condition
14:12 <twb> IIRC journald reads from /run/systemd/journal/dev-log (which /dev/log symlinks to) and then it also writes out to something like /run/systemd/journal/downstream-logd-output
14:13 <twb> journald and rsyslogd disagree on which reader to read from: https://www.rsyslog.com/doc/v8-stable/configuration/modules/imjournal.html  vs.  https://www.rsyslog.com/doc/v8-stable/configuration/modules/imuxsock.html
14:13 <twb> i.e. journald says "you should use imjournald because it has more features", rsyslogd says "you should not use imjournald because journald is buggy as fuck"
14:14 <twb> Specifically we want this part of the docs: https://www.rsyslog.com/doc/v8-stable/configuration/modules/imuxsock.html#coexistence-with-systemd
14:15 <twb> "if rsyslog is running under systemd AND /run/systemd/journal/syslog exists, (AND the user has not explicitly set SysSock.Use="off") then the default listener socket name is overwritten with /run/systemd/journal/syslog."
14:16 <twb> So I'm thinking I can start by hard-coding it to explicitly be /run/systemd/journal/syslog which will at least give better error reporting when the race condition happens...
14:20 <twb> https://cyber.com.au/~twb/tmp/why-is-rsyslog-bypassing-journald-on-dev-log.svg
14:21 <twb> There's definitely not an obvious race condition there -- all of journald DEFINITELY started before rsyslog, and bootstrap2020-get-config-from-dnssd DEFINITELY READY=1'd before rsyslogd started
14:21 <damjan> not sure why you use rsyslog. there are milions of journald exporters out there, supporting all sorts of endpoints
14:21 <damjan> I mean, it obviously wants to fight journald
14:22 <twb> damjan: aptitude search '?depends(librelp)' ==> one hit
14:22 <twb> damjan: this has worked perfectly for about 12 years
14:22 <twb> ah sorry it worked perfectly for 12 years, of which 6 journald was also involved
14:22 <damjan> _sigh_ "it has worked perfectly X years"
15:31 <twb> It's definitely a problem I've caused SOMEHOW, because it's only happening when "resolvectl query -t SRV _relp._tcp.$(hostname --domain)" finds a record.
15:32 <twb> Er, resolvectl service _relp._tcp "$(hostname --domain)"
15:38 <twb> ohhhhh wait did I "systemd analyze-security rsyslog"?
15:39 <twb> ...nope
15:39 <twb> (I thought for a second maybe I had blocked e.g. AF_NETLINK and that caused rsyslog to misdetect "is systemd running?")
15:40 <twb> But "→ Overall exposure level for rsyslog.service: 9.6 UNSAFE 😨" --- so it's not that
16:11 <twb> Hard-coding rsyslog.conf also doesn't cause the problem.  It's only when I try to configure rsyslog.conf at boot time, after the network is up, before rsyslog sarts.
17:57 <twb> In other news, I'm still trying to understand why rsyslogd mis-configures itself to hijack /dev/log even though journald has /run/systemd/journal/stdout there waiting for it
⋮
17:57 <grawity> but if setting eth0's interface MTU to 1500 seems to fix the issue, that might be good enough
17:58 <grawity> (normally dislike lowering MTU, but 1500 is setting it back to the "standard internet MTU" anyway)
17:58 <grawity> twb: wait, /stdout isn't for that at all
17:58 <twb> http://ix.io/3OVa  is what rsyslogd is printing
17:58 <twb> grawity: sorry I meant .../syslog
17:59 <grawity> and /syslog is supposed to be created by rsyslogd, journald waits for it
17:59 <grawity> I'm not sure I agree with rsyslogd's claims about imjournal being broken though
17:59 <twb> grawity: according to rsyslog's source, it wait for journald to create it
17:59 <lioh> Just to confirm. Setting the MTU on the router to 1500 which is announced via RA works.
17:59 <twb> Which was confusing -- what you say makes more sense
17:59 <grawity> twb: well, syslog.socket is what normally creates it, and the syslogd inherits it
18:00 <grawity> but the end result is still that syslogd listens and journald connects
18:00 <twb> Is it possible that I've managed to "systemctl enable rsyslog" and so BOTH .service and .socket are starting, and the wrong one starts first?
18:00 <twb> You can see in that pastebin that it *definitely* knows to READY=1 -- "done signaling to systemd that we are ready!"
18:01 <twb> But /dev/log happens before that
18:01 <grawity> dunno, maybe it needs [Service] Sockets=syslog.socket, or whatever
18:01 [grawity using syslog-ng here]
18:02 <twb> the reason I suspect that is I'm doing a "systemctl preset" or so
18:02 <twb> Which can cause weirdness.  e.g. on Debian 9 it tries to stat both ssh.socket AND ssh.service
18:03 <grawity> lioh: does your machine's eth0 also default to high MTU for the interface itself? I thought even jumbo-frame-capable interfaces generally default to pretending they're 1500-only
18:06 <twb> grawity: damn that fixed my problem
18:06 <twb> "disable rsyslog.service" in etc/systemd/system-preset/50-bootstrap2020-main.preset
18:06 <twb> Hrm but now rsyslog isn't running at all
18:07 <twb> And "systemctl start syslog.socket" says "systemd[1]: syslog.socket: Socket service syslog.service not loaded, refusing."
18:07 <lioh> grawity, no the interface uses 1500
18:08 <twb> Oh, because "enable" both creates multi-user.target.wants/rsyslog.service *and* syslog.service -> rsyslog.service.  Urgh
18:09 <twb> If I change rsyslog.service so Install.Alias=syslog.service is present, and Install.WantedBy=multi-user.target is absent, my problem is fixed.  I think.
18:25 <twb> grawity: OK I give up, I'm going to use imjournal
18:25 <twb> I've been staring at this for like 4 hours now without solving it

---
## [cyberitsolutions/bootstrap2020](https://github.com/cyberitsolutions/bootstrap2020)@[71db732209...](https://github.com/cyberitsolutions/bootstrap2020/commit/71db73220917bc9e030188172ec1cc62f6dd7a36)
#### Tuesday 2022-02-08 05:41:07 by Trent W. Buck

rsyslog: read /*/log/journal/*.journal (not /run/systemd/journal/syslog)

If systemd-journald provided a RELP push instead of HTTP pull,
we would not need any of this bullshit.

The rsyslog docs say basically:

  1. journald was created by Lennart in secret with no consultation
     from existing logging experts (even personal friends like Gerhard),
     and is a bit dumb.

  2. imjournal can break when .journal files are corrupt (due to journald bugs).
     When this happens, rsyslogd will logspam downstream log servers.
     Therefore do not use imjournal unless you really have to.

  3. imuxsock defaults to /dev/log and will delete anything already
     there, put a ryslog listener there, and remove it when rsyslog
     exists.

     BUT if rsyslog detects that systemd is around,
     it will instead use /run/systemd/journal/syslog.
     This is why journald is hard-coded to WRITE to.

     This can also break due to journald bugs, but
     when this happens, the result is lost messages, not log spam.
     Therefore use this one.

We have used imuxsock just fine with a hard-coded rsyslog.conf for a decade.

We recently switched to using a systemd unit that configures
rsyslog.conf dynamically for the local network, based on SRV records.
When we did that, rsyslog broke and started listening on /dev/log
instead of / as well as /run/systemd/journal/syslog.

The problem GOES AWAY if we turn off all get-config-from-dnssd* files.
i.e. SOMEHOW we caused this.

I tried for about 6 hours to isolate and fix this problem, by
juggling the systemd unit hooks.  In the end I gave up.

I am using imjournal instead now which I think works better???
I'm slightly scared of #1 though.

https://www.rsyslog.com/doc/v8-stable/configuration/modules/imuxsock.html#coexistence-with-systemd
https://www.rsyslog.com/doc/v8-stable/configuration/modules/imjournal.html

---
## [classified/android_kernel_oneplus_sm8150](https://github.com/classified/android_kernel_oneplus_sm8150)@[c43d7ae3c6...](https://github.com/classified/android_kernel_oneplus_sm8150/commit/c43d7ae3c6b686876b152043fe007cbd103de74c)
#### Tuesday 2022-02-08 06:26:43 by alk3pInjection

drm: Handle dim for udfps

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
## [VincentRPS/discord.io](https://github.com/VincentRPS/discord.io)@[b031ecdd1b...](https://github.com/VincentRPS/discord.io/commit/b031ecdd1b431f9541f12ab3a01228627548adb0)
#### Tuesday 2022-02-08 06:41:51 by Vincent

chore: deprecate

if anyone would want to make a command handler you can easily do it but i have not that much experience in how it would be done especially adding options the way i want, if you want you can make a PR and if i like it i will accept it but i myself feel like i shouldn't be making this.

---
## [wking/openshift-api](https://github.com/wking/openshift-api)@[2988f6b7a8...](https://github.com/wking/openshift-api/commit/2988f6b7a8c6106c8eb473ad409705b2a1b096d2)
#### Tuesday 2022-02-08 07:51:34 by W. Trevor King

config/v1/types_cluster_version: Add capabilties properties

Roughly as described in [enhancement].  After discussion with Ben and
David, we've made the following changes:

# spec

## capabilities

The [enhancement] didn't have an opinion on whether or not this should
be a pointer.  I've gone with pointer, because I'm fine allowing folks
to leave this unset.  The docs for this pointer property point out
that there's no distinction between nil (Go, or for JSON, null) and an
empty object (&ClusterVersionCapabilitiesSpec{} in Go, {} in JSON), so
we don't have to rehash all the ClusterVersionCapabilitiesSpec
children defaults here, where they'd likely go stale as folks update
defaults within ClusterVersionCapabilitiesSpec or add new child
properties.

### baselineCapabilitySet

David prefered this name to the [enhancement]'s inclusionDefault, and
Ben and I are fine with that name.

David also prefered None to Exclude and vCurrent to Include, with
additional values like v4.11 for "give me the 4.11 stuff, but not new
4.12 stuff, until I have time to look that over after I update to
4.12".  That seems overly complicated to me, and also like we coulld
add v4.11 later if folks felt None and vCurrent weren't convenient
enough, but David wanted v4.11 out of the gate.  We can always see how
it plays out in production, and we can stop adding new v4.y forms if
they aren't popular enough to be worth maintaining.  There's an enum
type to make it easy to validate, and hard to typo, these values.

There's also a map, so consumers like the cluster-version operator who
vendor the API repository can get the API-maintainer-intended
capability membership for each set, now that those semantics are more
complicated than all or nothing.

There were a few ways we could have taken the property default here:

a. Explicit +kubebuilder:default:=... .  No option for folks to sit on
   the fence, or to adjust existing clusters later without the admin's
   explicit buy-in.  But no ambiguity about what happens if the user
   has no opinion.

b. omitempty, and docs for "we'll pick a sane default if you don't
   care", that don't commit to a specific default.  Great for when we
   decide to change our default preference, because we don't need to
   hunt down buy-in from admins that have deferred to us.  Not great
   for folks who are mildly curious about our current choice, but who
   still trust us to evolve the default (I think this set is nearly
   empty).

c. omitempty, and docs for "the current default is A, but who knows
   tomorrow".  Effectively (b), but also gives folks some information
   that's not actionable which can go stale as soon as they close
   their eyes.

(a) makes sense if we are confident we will never want to change our
default, and that seems plausible in this case.  (b) makes sense when
we think we might change our default, and I'm fine with that in this
case too.  I don't really understand the use case for (c), but as
David points out, even if we do change the default, we don't expect to
change it often, so maybe my personal take is off and there are a
bunch of folks who are mildly curious about our current choice, but
who still trust us to evolve the default.  Anyhow, David's the
approver, so we're going with (c).

### additionalEnabledCapabilities

David prefered this name to the [enhancement]'s inclusionDefault, and
Ben and I are fine with that name.

In the [enhancement], Ben had intended to distribute the ability to
create new capabilities to all manifest-providing repositories, simply
by declaring the capability.openshift.io/name annotation.  David was
worried about validation, and also possibly about insufficiently
scoped names between separate teams, so this pull request declares a
central enum where API maintainers can review and approve new
capability names, and work them into the appropriate entries in the
set maps.  The installer and cluster-version operator will have to
bump their vendored API version after each addition to pick up the new
changes, but new capability additions shouldn't be too frequent to
make that particularly painful.

### exclude

The [enhancement] also provided a way to drop specific capabilities
from the selected set (inclusionDefault or baselineCapabilitySet).
Ben still feels like that will be popular, but David is skeptical, and
because we can always add a property in this space later without
breaking backwards compatibility, we're leaving it off for now.

# status

## capabilities

The [enhancement] didn't have an opinion on whether or not this should
be a pointer.  I've gone with non-pointer, because we will always
declare at least some capabilities (e.g. knownCapabilities), so users
will be able to discover additional capabilities which they might want
to enable in their cluster.

### enabledCapabilities

David prefered this name to the [enhancement]'s include, and Ben's ok
with that name.  I'm not wild about 'Capabilities' in:

  status:
    capabilities:
      enabledCapabilities: ...

but David was committed, citing the example of:

  FeatureGateSelection.FeatureSet

Although FeatureGateSelection is consumed with less context:

  type FeatureGateSpec struct {
	FeatureGateSelection `json:",inline"`
  }

I'd pushed back against the stuttering in [stutterPrecedent], but
without success, and :shrug:, doesn't matter all that much if folks
have to type a few redundant characters to use this property.

### knownCapabilities

The [enhancement] had floated 'exclude'.  There are a few capability
sets in play for the status listings:

* A is the set of all caps.
* I is the set of included caps.
* E is the set of excluded caps.
* Each cap must be either included or excluded, so I and E are disjoint, and the union of I and E is A.

So you can take any two of those three sets and construct the one
you're missing:

* A = I ∪ E
* E = A - I
* I = A - E

If we have to pick two to include in status, picking I and E gives us
all the data we need, and saves a few bytes by excluding the largest,
which is A.  But David preferred picking I (as enabledCapabilities)
and A (as knownCapabilities) [knownCapabilities], so that's what we're
doing in this commit.

### inclusionDefault

The [enhancement] also provided a way to echo the spec set in an
inclusionDefault status property.  I've left that out of the status
structure, because I'm using explicit, exhaustive list for
enabledCapabilities and knownCapabilities there.  The exhaustive lists
will provide a convenient set (via A - I set subtraction) of "things
you don't have right now, but which you could choose to install right
now", so admins don't have to guess about their options there.  With
the exhaustive lists, reflecting the default setting didn't seem to
add much useful information.  And we can always add that property to
the status structure later if we do decide it would be useful.

## conditions

I have not created a constant with the status.conditions[] type that
will be used to declare "we are installing a capability you have not
asked for, because we don't support uninstalling capabilities, and
that one was tainted in via your cluster's history".  We can come back
and declare that constant later if we want, although that's somewhat
complicated by the fact that we use ClusterOperatorStatusCondition,
and the new condition type would not be something that makes sense for
ClusterOperator.

[enhancement]: https://github.com/openshift/enhancements/blob/88cb7438f3ac0a8121e3cef87cb144097ece8cda/enhancements/installer/component-selection.md
[knownCapabilities]: https://github.com/openshift/api/pull/1106#discussion_r799819632
[validation]: https://book.kubebuilder.io/reference/generating-crd.html#validation
[statusPropertyNames]: https://github.com/openshift/api/pull/1106#discussion_r799819632
[stutterPrecedent]: https://github.com/openshift/api/pull/1106#discussion_r799879689

---
## [fuzzard/xbmc](https://github.com/fuzzard/xbmc)@[ee5e0a485b...](https://github.com/fuzzard/xbmc/commit/ee5e0a485ba8b2321f50f493a7a10a063f8f54f7)
#### Tuesday 2022-02-08 08:20:07 by fritsch

AESinkAudioTrack: Pause-Burst - a little revisit

Pause-Bursts in RAW format are a red hering in general as they rely on
a non-existing API within Android. The implementation opens the audio
device but directly pauses it, hoping that internally the system does
the needful to keep the sink alive.

Sadly this happens intransparent for kodi, as the reported buffer of the
device stays zero. VideoPlayer calls AddPause multiple times in the
beginning to sync audio and video properly, while expecting that pause
bursts on audio side will fill up the sink (prepare it) and on the same time
causing a certain stable or better said: known delay when real data is
added later on.

The implementation asks android to pause, but blocks video player for the
amount of millis that it wants to add, stating: buffer is already filled.

As we sleep the non-existing data in, we need to "hack" the way back, remember
buffer is empty and not filled when first AddPacket is coming. We fake
this situation further until the real audio data has reached the same level
then we continue normally. Especially the way out is the hack as AE
exactly knows that out of a sudden 10 ms of data cannot be added in 0 ms if
the buffer is actually full. Though AE nicely gives us some time to get
our stuff in line.

But hack stays hack. If someone of google reads this:
Please add a method where you expose your IEC Packer so that we can create
and enqueue pause_bursts like normal audio. That way these hacks here would
not be needed at all.

---
## [pri0818/android_kernel_realme_sm7125](https://github.com/pri0818/android_kernel_realme_sm7125)@[d57c2b072a...](https://github.com/pri0818/android_kernel_realme_sm7125/commit/d57c2b072a53ca2d6d9e9ea82f0baf49910e8664)
#### Tuesday 2022-02-08 10:18:21 by Wang Han

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

---
## [ammarfaizi2/linux-block](https://github.com/ammarfaizi2/linux-block)@[dd0602d8df...](https://github.com/ammarfaizi2/linux-block/commit/dd0602d8dfd6c2dc2a1c659d206b590436d3f342)
#### Tuesday 2022-02-08 11:01:57 by Jason A. Donenfeld

random: use linear min-entropy accumulation crediting

30e37ec516ae ("random: account for entropy loss due to overwrites")
assumed that adding new entropy to the LFSR pool probabilistically
cancelled out old entropy there, so entropy was credited asymptotically,
approximating Shannon entropy of independent sources (rather than a
stronger min-entropy notion) using 1/8th fractional bits and replacing
a constant 2-2/√𝑒 term (~0.786938) with 3/4 (0.75) to slightly
underestimate it. This wasn't superb, but it was perhaps better than
nothing, so that's what was done. Which entropy specifically was being
cancelled out and how much precisely each time is hard to tell, though
as I showed with the attack code in my previous commit, a motivated
adversary with sufficient information can actually cancel out
everything.

Since we're no longer using an LFSR for entropy accumulation, this
probabilistic cancellation is no longer relevant. Rather, we're now
using a computational hash function as the accumulator and we've
switched to working in the random oracle model, from which we can now
revisit the question of min-entropy accumulation, which is done in
detail in <https://eprint.iacr.org/2019/198>.

Consider a long input bit string that is built by concatenating various
smaller independent input bit strings. Each one of these inputs has a
designated min-entropy, which is what we're passing to
credit_entropy_bits(h). When we pass the concatenation of these to a
random oracle, it means that an adversary trying to receive back the
same reply as us would need to become certain about each part of the
concatenated bit string we passed in, which means becoming certain about
all of those h values. That means we can estimate the accumulation by
simply adding up the h values in calls to credit_entropy_bits(h);
there's no probabilistic cancellation at play like there was said to be
for the LFSR. Incidentally, this is also what other entropy accumulators
based on computational hash functions do as well.

So this commit replaces credit_entropy_bits(h) with essentially `total =
min(POOL_BITS, total + h)`, done with a cmpxchg loop as before.

What if we're wrong and the above is nonsense? It's not, but let's
assume we don't want the actual _behavior_ of the code to change much.
Currently that behavior is not extracting from the input pool until it
has 128 bits of entropy in it. With the old algorithm, we'd hit that
magic 128 number after roughly 256 calls to credit_entropy_bits(1). So,
we can retain more or less the old behavior by waiting to extract from
the input pool until it hits 256 bits of entropy using the new code. For
people concerned about this change, it means that there's not that much
practical behavioral change. And for folks actually trying to model
the behavior rigorously, it means that we have an even higher margin
against attacks.

Cc: Theodore Ts'o <tytso@mit.edu>
Cc: Dominik Brodowski <linux@dominikbrodowski.net>
Cc: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Reviewed-by: Eric Biggers <ebiggers@google.com>
Reviewed-by: Jean-Philippe Aumasson <jeanphilippe.aumasson@gmail.com>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>

---
## [repinger/exynos9611_m21_kernel](https://github.com/repinger/exynos9611_m21_kernel)@[95ff383209...](https://github.com/repinger/exynos9611_m21_kernel/commit/95ff3832095d32f5d54f32b1bf02ac7ba45201aa)
#### Tuesday 2022-02-08 11:03:53 by Masahiro Yamada

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
## [coldud13/Skyrat-tg](https://github.com/coldud13/Skyrat-tg)@[1f70226654...](https://github.com/coldud13/Skyrat-tg/commit/1f70226654438f75811a2d59ad9c52bf88c048fc)
#### Tuesday 2022-02-08 11:58:05 by SkyratBot

[MIRROR] Removes the fucking 20 second stunlock rng from tourettes because it's fucking stupid and I just had the most agonizing thirty fucking minutes of my goddamn life, holy shit [MDB IGNORE] (#11027)

* Removes the fucking 20 second stunlock rng from tourettes because it's fucking stupid and I just had the most agonizing thirty fucking minutes of my goddamn life, holy shit (#64416)

Removes the 20 second stunlock from tourettes

* Removes the fucking 20 second stunlock rng from tourettes because it's fucking stupid and I just had the most agonizing thirty fucking minutes of my goddamn life, holy shit

Co-authored-by: Iamgoofball <iamgoofball@gmail.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[4fecc5852a...](https://github.com/mrakgr/The-Spiral-Language/commit/4fecc5852af3bcd4abbfe7f1dea78db4ff9475ee)
#### Tuesday 2022-02-08 12:16:15 by Marko Grdinić

"10am. Almost ready to start. I went to bed at 12am, and have gotten up 30m ago. The disease's effect is definitely waning. Let me read the Yakuza Princess chapter and I will start work on varying the vines.

10:10am. Let me start.

Hmmm, I've been wondering this for a while. What is photogrammetry? I see this being ref'd in the docs everywhere.

> Photogrammetry is the art and science of extracting 3D information from photographs. The process involves taking overlapping photographs of an object, structure, or space, and converting them into 2D or 3D digital models.

10:15am. I ma thinking. Let me just ask.

10:20am.

///

The stalk for this flower is made from a curve. I want to add variation to it, and I am trying to figure out how to interpolate between this and a straight curve.

One way of doing it would be to pick the middle point of the curve and scale it so the curve gets straighter.

But if I do that it might be good to also rescale the curve so it has the original length. How could I do that?

///

Hmmm, there is also something called attribute interpolate. And I need to keep in mind that position is an attribute.

Actually, I won't ask. I figure it out on my own already. Let me just put my plan into action.

11:25am. Damn it, this is so annoying. How do I make one HDA inherit params from another.

12:35pm. I've figured out how to straighten and interpolate long ago using blend shapes. I've also figured out that it is just possible to drag the node into the parameters. Houdini is great here.

But right now I am really wracking my brain as to how I could vary the individual flowers.

12:45pm. Decided to actually ask. Copy stamping? But how would that work when it is not even in the same scope.

1pm. https://www.youtube.com/watch?v=-tTzZZuoRco
[VEX for Algorithmic Design] E16 _ Geometry Functions

I am stuck mentally on this issue. As a programmer I understand that the type of the HDA is wrong. I have `geo * geo * geo`, but what it should be is `geo * (point -> geo)`. Maybe I could hack it if I could pass VEX scripts via channel functions.

1:15pm. Focus me. I am way too lost in thought. In the worst case, I could just inline by hand.

I am just wasting time here. Let me have breakfast."

---
## [alphagov/govuk-helm-charts](https://github.com/alphagov/govuk-helm-charts)@[cfa1a475b5...](https://github.com/alphagov/govuk-helm-charts/commit/cfa1a475b52a672d976bb56c0ff1e5fa1d13a045)
#### Tuesday 2022-02-08 12:24:54 by Chris Banks

Have chart-releaser skip duplicate chart versions.

With `CR_SKIP_EXISTING=true`, chart-releaser will skip uploading a chart
tarball where one already exists with the same filename (i.e. same chart
name and chart version). This means the chart-releaser GitHub Action
will no longer fail when we make changes to a chart without updating the
version number.

This is essentially a quick bodge to avoid having to automate
incrementing the chart version on merge-to-main for now.

We really don't want to have to update chart versions for charts which
we're only deploying via ArgoCD (which doesn't care about version
numbers). Having to change the version number on every change causes
merge conflicts and has proved a frequent source of annoyance even in
the absense of merge conflicts, even for experienced users. This was a
recurring theme in the feedback from the 2021-11 user testing.

There's no technical reason why we need to bother with version numbers
for the charts which we're installing with ArgoCD, since Argo just
evaluates the chart using `helm template` and compares the output; it
doesn't care about chart version numbers. We still need to care about
version numbers for charts which we're deploying using the Helm
Terraform provider, though.

Unfortunately the chart-releaser GH Action doesn't support filtering on
paths; it just releases every charts that's changed under `charts_dir`
and it uses the Git history rather than the chart version to tell
whether a chart has changed.

We could configure separate chart-releaser actions for the
Terraform-deployed charts, but that sounds like a maintenance pain.

Eventually we might want to have all of our charts published in the
chart repo, at which point we could automate bumping the version number.
We'd have to forego Helm's conventional use of semver and just increment
(say) the minor version number. Doesn't seem worth it for now though.

---
## [tannerhelland/PhotoDemon](https://github.com/tannerhelland/PhotoDemon)@[1bd3a1ee78...](https://github.com/tannerhelland/PhotoDemon/commit/1bd3a1ee7848e4ac89590e9ae45281955db96880)
#### Tuesday 2022-02-08 14:43:33 by Tanner

MULTIPLE SELECTIONS ARE ACTUALLY GONNA WORK!

This commit is just a placeholder, and only "add" combine mode is implemented, but for the first time in PhotoDemon history, the program is capable of functional multiple selection support.

This is a placeholder commit because there are a billion details still to work out, including a lot of critical feature work, but the core fundamentals are all in place and they work without crashing the app.  I honestly had my doubts that I would ever make it this far... but hey, hope springs eternal!

This commit may not look like it contains much code, but there are approximately two thousand rounds of work that were written then deleted as I tried to to graft multiple selection behavior onto PD's ancient selection engine.  A lot of attempts didn't go well so I had to back up and start over, but I finally think I've arrived at a solution that won't require a total rewrite of the app.  (In a perfect world, that would be lovely and probably produce a much tidier selection engine core, but I don't have infinite time so I have to be practical about how I implement new features.)

A lot of debug messaging is strewn throughout this commit, but don't worry - I'll deal with these as I work through the known bugs associated with those program areas.

Next up is getting border rendering working correctly when multiple selections are active (only masks are calculated right now), then I need to get "subtract" and "intersect" modes working.  Then there are a ton of UI issues left to solve.... but the worst of this project is finally in the past, I think.

---
## [ThePeeps191/learnmonkey.github.io](https://github.com/ThePeeps191/learnmonkey.github.io)@[14792cae65...](https://github.com/ThePeeps191/learnmonkey.github.io/commit/14792cae65065ff0ad95392297565db6b84863d6)
#### Tuesday 2022-02-08 15:54:31 by Danny Wang (ThePeeps191)

Merge pull request #26 from ThePeeps191/main

fuck you @calgary34

---
## [ghc/ghc](https://github.com/ghc/ghc)@[31088dd32a...](https://github.com/ghc/ghc/commit/31088dd32a4dbbed649dff0700610eb7ed7a9fca)
#### Tuesday 2022-02-08 16:32:26 by David Feuer

Add test supplied in T20996 which uses data family result kind polymorphism

David (@treeowl) writes:

> Following @kcsongor, I've used ridiculous data family result kind
> polymorphism in `linear-generics`, and am currently working on getting
> it into `staged-gg`. If it should be removed, I'd appreciate a heads up,
> and I imagine Csongor would too.
>
> What do I need by ridiculous polymorphic result kinds? Currently, data
> families are allowed to have result kinds that end in `Type` (or maybe
> `TYPE r`? I'm not sure), but not in concrete data kinds. However, they
> *are* allowed to have polymorphic result kinds. This leads to things I
> think most of us find at least quite *weird*. For example, I can write
>
> ```haskell
> data family Silly :: k
> data SBool :: Bool -> Type where
>   SFalse :: SBool False
>   STrue :: SBool True
>   SSSilly :: SBool Silly
> type KnownBool b where
>   kb :: SBool b
> instance KnownBool False where kb = SFalse
> instance KnownBool True where kb = STrue
> instance KnownBool Silly where kb = Silly
> ```
>
> Basically, every kind now has potentially infinitely many "legit" inhabitants.
>
> As horrible as that is, it's rather useful for GHC's current native
> generics system. It's possible to use these absurdly polymorphic result
> kinds to probe the structure of generic representations in a relatively
> pleasant manner. It's a sort of "formal type application" reminiscent of
> the notion of a formal power series (see the test case below). I suspect
> a system more like `kind-generics` wouldn't need this extra probing
> power, but nothing like that is natively available as yet.
>
> If the ridiculous result kind polymorphism is banished, we'll still be
> able to do what we need as long as we have stuck type families. It's
> just rather less ergonomical: a stuck type family has to be used with a
> concrete marker type argument.

Closes #20996

Co-authored-by: Matthew Pickering <matthewtpickering@gmail.com>

---
## [LucasLyn/pokeemerald](https://github.com/LucasLyn/pokeemerald)@[295e1d2c2e...](https://github.com/LucasLyn/pokeemerald/commit/295e1d2c2ef61f051a6ef8597cf859c3c9d1a260)
#### Tuesday 2022-02-08 17:05:51 by Revo

Fix the source of pain and suffering for the last 2 years.

Why wasn't this fixed yet. This is dumb. This is really dumb. This is fuckin' stupid.

---
## [stalker780/opencart](https://github.com/stalker780/opencart)@[89c304ae61...](https://github.com/stalker780/opencart/commit/89c304ae61fb683b2ca8ff7dcf5ceabfc4f5a0eb)
#### Tuesday 2022-02-08 18:21:13 by Anton

OC4 return created module_id

IMHO every single model function, creating a row in DB, must return this row id after executed.

I can check `$module_id = $this->db->getLastId();` in my code on clean opencart installation.
But what if this model function calls any `after` events which also insert rows into DB?

This is not a developer friendly software architecture when you need to create hacks, hooks, workarounds and other voodoo magic to get a single value for page redirect.

BUG:
By the way on creating, for example a banner module, on save you are not redirected to created module page. 
So every click on Save button just creates a duplicate of a module.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[d082688732...](https://github.com/mrakgr/The-Spiral-Language/commit/d0826887329e1337835a437e0c31e663589a52c6)
#### Tuesday 2022-02-08 19:07:32 by Marko Grdinić

"3pm. Ah, whatever. This is so weird. Why does Primitive Property SOP does not works as I'd expect it to? Its pivot point transform seems to be bonkers.

Let me play around with it more. Let me close the pool file.

3:10pm. I am so confused. Let me ask about this. I know how to get the first point of the curve, but seriously, how transform a primitive around it.

3:20pm. Decided to ask.

https://www.youtube.com/watch?v=SY6NyECDwpk
[Houdini Snippet] Save Node as Python Code

Let me watch this since it got linked to me.

3:45pm. https://www.tokeru.com/cgwiki/index.php?title=HoudiniVex#Rotate_prims_around_an_edge.2C_alternate_version

```vex
int points[] = primpoints(0,@primnum); // list of points in prim

// get @P of first and second point
vector p0 = point(0,'P',points[0]);
vector p1 = point(0,'P',points[1]);

vector axis = p0-p1;

float angle = ch('angle');
matrix3 rotm = ident();
rotate(rotm, angle, axis);

// get midpoint of edge
vector pivot = (p0+p1)/2;

// move point to origin, rotate, move back

@P -= pivot;
@P *= rotm;
@P += pivot;
```

Of course since this is a matrix multiply, it should be able to scale as well.

3:55pm.

```vex
vector p0 = point(0,'P',primpoint(0,@primnum,0));

@P -= p0;
@P *= chf("factor");
@P += p0;
```

After some thinking I pared it down to this.

Ok, this clinches it. I really should get a bit familiar with Vex.

4pm. Still, isn't there a way to do this using just nodes?

4:05pm. I am completely distracted.

4:10pm. I need to set these issues aside. Forget about trying to learn Vex now. If I need it I'll make time for this later. Let me go back to the pool scene.

4:25pm. I'll push the question of what happens if the point is a part of more than one primitive to the back of my mind.

What should I do now...

Yeah, let me make those flowers.

4:45pm. What does create black boxed asset mean?

> Black Box. You can now create “black box” assets that can be freely distributed and used without a license, but cannot be inspected or modified. Select an instance of an asset and choose Assets > Create black-boxed asset.

Ok.

4:50pm. Ogh, this is so fucking annoying. Can this thing be any more slower?

4:55pm. I need to do this properly. The subnets were really annoying so I tried creating an HDA, but now I have different problems. And now Houdini even crashed.

5:40pm. FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF

I really, really hate Houdini right now. Fuck!!!

Sigh...

I had the bright idea of putting the nodes in a loop, and making the branches that way for variety. What is instead happening is that I am having trouble converting the iteration count into a string so that I can make the damn name. I hate this so much it is ridiculous.

I've wasted the whole day going around in circles.

Well, that is about the par for this.

I've been in an exploratory mood and that does not end well.

5:45pm. I need to get a proper handle on assets. Right now I am afraid of using the liberaly because they will result in all sort of HDD garbage. And if they have merged objects, I get all sorts of complaints from them.

I really hate how this was designed in Houdini as well as it being a first order language.

Ok, let me pause here. I need to figure out how to deal with those merged objects. Let me start a new file.

5:50pm. https://youtu.be/tWjIWEgoOf8?list=PLXNFA1EysfYnnm2-UZmxrd-MWC7LTWEVl
Houdini Digital Assets | 3. Create Parameters

He talked about those extra files here. I need to figure out how to convert things to internal references. Unless I do that, every time I edit the asset, I am going to get errors pestering me.

I am a fool. Just why did I not make up my mind to do it from the start. Also how to delete HDAs?

> Choose File ▸ Import ▸ Houdini digital asset. Choose Windows ▸ Asset Manager. Right-click the library name and choose Uninstall.

In the asset manager as expected.

There is also an option to check for external references in Type Properties. I can switch it off to stop it from pestering me.

But suppose I want to convert things to internal refs, how would I do it?

https://youtu.be/gtO-YGMLyfM
Tutorial 8. All about Houdini Digital Assets

Let me watch this.

6:45pm. Back from lunch.

I didn't watch the above. Instead I just decided to put my foot down and made the rule that internal HDA will be prefixed with `I`. That will allow me to make use of them in mass.

```
1e5 + ch("../foreach_begin1_metadata1/iteration/")
```

Now how did I fuck this up? I got a warning in a really weird place that this reference is not right, and it turns out it is not. The seed is the same everywhere.

Let me start a new file.

Ah, crap, these are detail attributes. Shit.

6:55pm.

```
detail("../foreach_count1","iteration",0)
```

This is still not giving me what I want. I hate Houdini. It is being so annoying right now.

```
detail("../block_begin2", "iteration", 0)
```

7:05pm. I have no idea why doing it by count is never showing me anything, but forget that.

7:15pm. I 'got' it to work, but this wasn't as I'd planned. It seems that just a single one of these flowers takes 40mb of memory. I put in 100 and watch the computer slow to a crawl.

7:20pm. This is strange. Why is the leaf weight doing nothing?

7:25pm. What a buggy piece of shit. There is a weird Houdini bug where the first argument is always leaf of 1.

7:55pm. Ok, through judicious use of packing, I managed to bring down the memory use from 4gb for 100 flowers to 67mb for 300 flowers. Now it can actually fit into memory. I've underestimated greatly of how much computation all this would take. Houdini was really useful in showing me the memory use in the info window. Otherwise I would be having a lot of trouble right now.

What I need to do now is put in some variation in stack sizes.

Do I have any better functions that `fit01`? Well, actually that one is pretty good. But I though that maybe something Gaussian would fit the bill better.

8pm. Let me close here as I am tired. Tomorrow, I am going to finish adding the needed variation to the flowers. Stalks, bulb size, I'll randomize all of that. That should allow me to move on to the next stage.

Today I got stuck fighting weird issues, including self inflicted ones. Tomorrow I will make definitely progress on the scene."

---
## [gaelicWizard/bash-it](https://github.com/gaelicWizard/bash-it)@[b84983331a...](https://github.com/gaelicWizard/bash-it/commit/b84983331aa89bfb525cc4cdd65a90b280b8b9b2)
#### Tuesday 2022-02-08 20:55:37 by John D Pell

lib/search: code style cleanup

Couldn't even `shellcheck` until I did a first pass...too much noise! ♥

lib/search: `shellcheck`

SC2076
SC2091
SC2004
SC2086
SC2207

lib/search: fix `_bash-it-flash-term()`

1. `$text_black` isn't a parameter provided by _Bash It_. Typo?
2. `$bold_yellow` is meant for prompt strings and putputs `\[`; ditto `$bold_red`.
3. The color was never returned to normal after.

lib/search: fix usage statement `_bash-it-search()`

SC2154

lib/search: `shfmt`

My apologies to future `git blame` hunters ♥

lib/search: code cleanup

Improve `_bash-it-erase-term()`, `_bash-it-flash-term()`, `_bash-it-rewind()`, `_bash-it-search-result()`, and `_bash-it-search-component()`. Minor tweaks to `_bash-it-is-partial-match()`, and `_bash-it-search()`.

pathmunge tests

main: Glob for *.bash properly when path contains spaces

- `shfmt`, `shellcheck`
- Clean up legacy/compatibility code to simpler control flow
- Move theme stuff down to where themes are handled
- Don't use `**` as _Bash It_ has never before set `globstar`; this eliminates varying behavior by environment; this alsö fixes users having any not-enabled themes under their custom dir.
- Lose weird Mac-specific alternate shell startup file (Bash loads startup files on Mac the same as it does on any other *nix system.)
- Place `composure.sh` init all in one place

main: adopt `_bash-it-log-prefix-by-path()`

lib/reloader: adopt `_bash-it-log-prefix-by-path()`

lib/appearance: `shellcheck` && `shfmt`

reloader: `shellcheck` && `shfmt`

Rewrite globbing per `shellcheck`'s SC2013 recommendations, and standardize whitespace.

lib/preview: `shfmt` && `shellcheck`

Fix theme file path globbing when $BASH_IT contains any spaces.

My apologies to future `git blame` hunters ♥

uninstall: `shellcheck` && `shfmt`

lint: add lib to clean_files.txt

lib/theme: `shfmt` && `shellcheck`

My apologies to future `git blame` hunters ♥

lib/colors: `shellcheck` && `shfmt`

Alsö, clean up `__color_rgb` to just use a regular if block.

lib/p4helpers: `shfmt`

My apologies to future `git blame` hunters ♥

lib/githelpers: `shfmt` && `shellcheck`

My apologies to future `git blame` hunters ♥

lib/theme: don't redefine battery_char()

Combine the two definitions for `battery_char()` so the second one doesn't just overwrite the first one. Do one or the other, not both.

Don't evaluate if `battery_percentage()` is available at load time, evaluate it at run time.

lib/command_duration: `shfmt` && `shellcheck`

My apologies to future `git blame` hunters ♥

lib/theme: `shellcheck` SC2154

These variables are referenced by themes already linted.

lib/theme.githelpers: unbound varbl

lib/theme: don't use `date` for `$THEME_CLOCK_FORMAT`

main: simplify flow of lib loader loop

Eliminate the separate loop for `vendor/init.d` since it's just as easy to glob it in the `lib` loop.

lib: delete `appearance.bash`

This adds *three* lines to `bash_it.sh`, and two to `plugin/base`. Just not worth an extra file requiring special handling.

main: load custom theme

Allow for simpler directory strucutre when loading theme from `$CUSTOM_THEME_DIR`/`$BASH_IT_CUSTOM`

make aliases load very late

...and update all the tests...

preexec: add helper functions to loader

Define the helper functions for `bash-preexec.sh` immediately after importing it, rather than in `lib/theme`.
- `__check_precmd_conflict()` and `save_append_prompt_command()` are generally useful and not theme-specific.
- Add matching `__check_preexec_conflict()` like `__check_precmd_conflict()`, and alsö `safe_append_preexec()`.

preexec: work around upstream

Alsö, move `set +T` in here.

test/theme: make fewer assumptions

Literally copying a line from the source to be tested is perhaps not the best way to test that code. 😉

That said, we do want to verify that the function was actually loaded.

TODO: actually test the function.

install: use `.bashrc` and notify user

The logic to guess whether to use `.bash_profile` or `.bashrc` was buggy and wrong. Just use `.bashrc` and either automatically fill in a `.bash_profile`, or notify the user that they need to edit their `.bash_profile`.

completions/sqlmap: use `_command_exists`

Addresses bash-it/bash-it#1632

completion/fabric: no need for `_command_exists`

If we're already inside the completion handler for `fab`...then it's a bit silly to check if `fab` is installed.

plugins/go: simplify _bash-it-gopath-pathmunge()

plugin/history: no need to set a trap
Instead of globbally clearing `$HISTTIMEFORMAT` and setting a return trap to re-enable it, just make it local to the function.

Also, set the defaults in a way that is happy with read-only parameters.

aliases/general: minor fixes

- Don't define some aliases if the target isn't installed, use _command_exists to check instead of `type` and `which`.
- Use `$EDITOR` for the editor for aliases about editing, excep the `sudo` ones because maybe you want those specifically?
- Fix `ls` aliases to match their common definitions (-A instead of -a: don't show '.' and '..' when displaying hidden files).

themes/base: use `type -P` instead of `which`

Avoid external binary `which`. Use built-in `type -P` instead. Uppercase `-P` forces a path search to avoid hashed matches and functions/aliases and whatnot.

completion/grunt: shellcheck

completion/subversion: load system completion

Load the completion script from the subversion package installed on the system, instead of bundling a copy. This addresses Bash-it/bash-it#1818.

NOTE: If `completions/system` is enabled, then it will load this same file anyway automatically.

plugins/battery: lint

plugins/xterm: not just Xterm

plugins/thefuck: lint

plugins/todo: lint

plugin/base: use `_bash-it-component-item-is-enabled()`

completion/git: use `_completion_exists()`

plugins/alias: remove old `SC2154` flag

This is no logner needed because the `local` keyword was moved higher up in the function.

---
## [Atom-X-Devs/android_kernel_xiaomi_scarlet](https://github.com/Atom-X-Devs/android_kernel_xiaomi_scarlet)@[d05b73befe...](https://github.com/Atom-X-Devs/android_kernel_xiaomi_scarlet/commit/d05b73befe212b07fe6bd5513a1464ad0bd5517f)
#### Tuesday 2022-02-08 22:41:26 by Angelo G. Del Regno

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
5      	      20220479
2      	      20940223
1      	      21231290

Remember again that we're loading from a UFS card and that
we are loading ~1.1MB more out of a 20MB file.
If you're smart enough you surely know already about RAM and CPU
overhead of very high compression levels.

If you still disagree with what I just did, read this commit description
another 20 times, or more, until you understand it. :)))

Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>

---
## [gitster/git](https://github.com/gitster/git)@[07564773c2...](https://github.com/gitster/git/commit/07564773c2569d012719ab9e26b9b27251f3d354)
#### Tuesday 2022-02-08 23:30:22 by Ævar Arnfjörð Bjarmason

compat: auto-detect if zlib has uncompress2()

We have a copy of uncompress2() implementation in compat/ so that we
can build with an older version of zlib that lack the function, and
the build procedure selects if it is used via the NO_UNCOMPRESS2
$(MAKE) variable.  This is yet another "annoying" knob the porters
need to tweak on platforms that are not common enough to have the
default set in the config.mak.uname file.

Attempt to instead ask the system header <zlib.h> to decide if we
need the compatibility implementation.  This is a deviation from the
way we have been handling the "compatiblity" features so far, and if
it can be done cleanly enough, it could work as a model for features
that need compatibility definition we discover in the future.  With
that goal in mind, avoid expedient but ugly hacks, like shoving the
code that is conditionally compiled into an unrelated .c file, which
may not work in future cases---instead, take an approach that uses a
file that is independently compiled and stands on its own.

Compile and link compat/zlib-uncompress2.c file unconditionally, but
conditionally hide the implementation behind #if/#endif when zlib
version is 1.2.9 or newer, and unconditionally archive the resulting
object file in the libgit.a to be picked up by the linker.

There are a few things to note in the shape of the code base after
this change:

 - We no longer use NO_UNCOMPRESS2 knob; if the system header
   <zlib.h> claims a version that is more cent than the library
   actually is, this would break, but it is easy to add it back when
   we find such a system.

 - The object file compat/zlib-uncompress2.o is always compiled and
   archived in libgit.a, just like a few other compat/ object files
   already are.

 - The inclusion of <zlib.h> is done in <git-compat-util.h>; we used
   to do so from <cache.h> which includes <git-compat-util.h> as the
   first thing it does, so from the *.c codes, there is no practical
   change.

 - Until objects in libgit.a that is already used gains a reference
   to the function, the reftable code will be the only one that
   wants it, so libgit.a on the linker command line needs to appear
   once more at the end to satisify the mutual dependency.

 - Beat found a trick used by OpenSSL to avoid making the
   conditionally-compiled object truly empty (apparently because
   they had to deal with compilers that do not want to see an
   effectively empty input file).  Our compat/zlib-uncompress2.c
   file borrows the same trick for portabilty.

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Helped-by: Beat Bolli <dev+git@drbeat.li>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---

