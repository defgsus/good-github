## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-07-17](docs/good-messages/2022/2022-07-17.md)


1,722,354 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,722,354 were push events containing 2,263,689 commit messages that amount to 119,081,399 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 27 messages:


## [AlbertoRomanRamosRodriguez/AlbertoRomanRamosRodriguez](https://github.com/AlbertoRomanRamosRodriguez/AlbertoRomanRamosRodriguez)@[95b385ceba...](https://github.com/AlbertoRomanRamosRodriguez/AlbertoRomanRamosRodriguez/commit/95b385cebab71e68c9452e63fb23e4646ee9c619)
#### Sunday 2022-07-17 01:16:36 by AlbertoRomanRamosRodriguez

Updating my contact section

I like to keep my life as private as possible. Coming from a pure FB, IG and TW life to just IG and TW and now just GitHub and LinkedIn has been kind of a reorganization of my usage of time, as I try to spend time where my mindset and skills actually improve. Not that I followed the wrong accounts but seeking my realization in other people's lives is no longer something that fulfills me.

GitHub is the *natural habitat* of programmers and engineers. I can watch what others see and *contribute* if I wanted to.

(I kinda like Microsoft haha)

---
## [RegJackson/StarbloomSS13](https://github.com/RegJackson/StarbloomSS13)@[cbd7626cb7...](https://github.com/RegJackson/StarbloomSS13/commit/cbd7626cb7b189f1aa19ae007a5dcc253757601d)
#### Sunday 2022-07-17 01:44:04 by RegJackson

Readds buckshot to the autolathe

I used the shotgun. You know why? Cause the shot gun doesn't miss, and unlike the shitty hybrid taser it stops a criminal in their tracks in two hits. Bang, bang, and they're fucking done. I use four shots just to make damn sure. Because, once again, I'm not there to coddle a buncha criminal scum sucking faggots, I'm there to 1) Survive the fucking round. 2) Guard the armory. So you can absolutely get fucked. If I get unbanned, which I won't, you can guarantee I will continue to use the shotgun to apprehend criminals. Because it's quick, clean and effective as fuck. Why in the seven hells would I fuck around with the disabler shots, which take half a clip just to bring someone down, or with the tazer bolts which are slow as balls, impossible to aim and do about next to jack shit, fuck all. The shotgun is the superior law enforcement weapon. Because it stops crime. And it stops crime by reducing the number of criminals roaming the fucking halls.

---
## [bakabun/DSharpPlus](https://github.com/bakabun/DSharpPlus)@[8380b5b2de...](https://github.com/bakabun/DSharpPlus/commit/8380b5b2deb9f2243c87e3277a34902ec08bb716)
#### Sunday 2022-07-17 01:56:09 by InFTord

[ci-skip] Fix docs typos in DiscordRestClient (#1317)

* Update DiscordRestClient.cs

* insanity

edited all of this with github site editor
madness
editing 2k lines of code is kinda pain with github site editor

* im idiot

* fixing...

* uh oh

* i love fixing docs

* fixing inconsistent ID stuff..

---
## [aosp-sweet/android_kernel_xiaomi_sweet](https://github.com/aosp-sweet/android_kernel_xiaomi_sweet)@[5e6b904933...](https://github.com/aosp-sweet/android_kernel_xiaomi_sweet/commit/5e6b9049333d321ad816d1386d3545358237d24e)
#### Sunday 2022-07-17 02:51:58 by Wang Han

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
## [PixelExperience-Devices/kernel_xiaomi_lavender](https://github.com/PixelExperience-Devices/kernel_xiaomi_lavender)@[4be14dc4ed...](https://github.com/PixelExperience-Devices/kernel_xiaomi_lavender/commit/4be14dc4ed79ed83de3aaa6c963c1c2ffc66dd63)
#### Sunday 2022-07-17 03:12:38 by Maciej Żenczykowski

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
Signed-off-by: ImPrashantt <prashant33968@gmail.com>
Signed-off-by: Aaradhay Vijay <inferno964.github@gmail.com>

---
## [sorosune/ImpulseGJ22](https://github.com/sorosune/ImpulseGJ22)@[ede86dc9c9...](https://github.com/sorosune/ImpulseGJ22/commit/ede86dc9c90c9b7d114f78892254086dec2eed26)
#### Sunday 2022-07-17 03:32:57 by Lane Knauff

smiles with pain in eyes

I plugged the level saver back in I am so sorry for whos time this fuckes up

---
## [A-freedom/beamCalculator](https://github.com/A-freedom/beamCalculator)@[770592ae08...](https://github.com/A-freedom/beamCalculator/commit/770592ae08ebf8ad5eb4850b67483ce86ddc6f87)
#### Sunday 2022-07-17 04:34:07 by A-freedom

I can't get the deflection to work if the supports are in the center of the beam by using the integration method ,there is no problem with the code the code run exactly like I want to run , but I believe that the problem is in my 'MATH' ,since it seems like I will not be able to solve it in the moment ,so I will try the singularity function method

I did disable calculating deflection because I couldn't to make it work so I will star redoing my logic for the start in hope that will make a change .

sofat I have been able to get the defliction function work with some cases but still there are some bugs need to be fix like the one with  Exam:Mid_Term 2022

note:: now all function start from there local zero I find that this methond working just find and there is no need to change it. And If needed it will be way easier to just convert the output than refracting the source code. So from now and then the locals zeros will be the official method

and after two days of doing nothing I fixed the bug, I found the bug which was a laze shit I did with the 'd' variable when I was refactoring the code in calculateDeflection line 233

Now we can calculate reactions from supports

---
## [boy2mantwicethefam/vgstation13](https://github.com/boy2mantwicethefam/vgstation13)@[b879dddba0...](https://github.com/boy2mantwicethefam/vgstation13/commit/b879dddba0f6a2afcf72a77f4696f3e9c031ecb5)
#### Sunday 2022-07-17 04:34:50 by rob

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
## [Kelprunner/coyote-bayou](https://github.com/Kelprunner/coyote-bayou)@[f5237fe227...](https://github.com/Kelprunner/coyote-bayou/commit/f5237fe227ece164896e815b14c3faf4ea3ae56a)
#### Sunday 2022-07-17 04:36:56 by Kelprunner

Update wastebots.dm

Changes gutsy HP to be a little less fuck you

---
## [ODRI-the-human/Vampire-Pooers](https://github.com/ODRI-the-human/Vampire-Pooers)@[27a8f218bd...](https://github.com/ODRI-the-human/Vampire-Pooers/commit/27a8f218bdec724b76b152990cacf312ddb16ff2)
#### Sunday 2022-07-17 06:06:19 by ODRI-the-human

V1.1

- Changed progression to wave-based. Each wave, 3 lots of enemies are spawned, and after each wave, you choose an item. The time gap between enemy spawns decreases over time and the number of enemies spawned per 'lot' increases over time. In later versions, the HP enemies have might increase over time, but I'll definitely make it so the enemies themselves get more dangerous over time.

- x2 damage item now stacks additively because it was a bit too ridiculous.
- Reworked damage calculation (was done based on the scale of the bullets before, which just got confusing)

- Added item: Wet Womedy Wapants (creates a pool of slowing creep every few seconds. Cooldown decreases with stacks)
- Added item: Holy Mantis (reduces the first damage you take each wave. Number of times damage can be reduced and damage reduction increases with stacks)
Added item: Converter (At the start of each round, 2% (+2% per stack) of the %HP you're missing gets converted to a damage multiplier.
Added item: Easier times (chance to block damage upon getting hit. Chance increases with stacks.)
Added item: Stopwatch (slows all enemies, reduces their shot speed and fire rate. Effect increases with stacks.)
Added item: Bouncy shots (Your bullets can bounce of enemies +1 (+1 per stack) times.)
Added item: 4-Direction Marty (every few shots (number decreases with stacks) shoot 4 bullets around you.)
Added item: Piercing (shots pierce 1 (+1 per stack) enemies.)
Added item: Creep (Leave damaging creep as you move. Size of creep increases with stacks.)

---
## [austingae/coup-d-etat](https://github.com/austingae/coup-d-etat)@[dc6e10b396...](https://github.com/austingae/coup-d-etat/commit/dc6e10b396dca63937581df13cfaa03a1bce2b13)
#### Sunday 2022-07-17 06:16:20 by Austin Gae

OHHHHHgit add .! worked on this one problem for 2 and a half hours BUT I FINALLY SOLVED IT. HOLY CRAP, THAT WAS FRUSTRATING. BUT, WHEN I FINALLY GOT IT TO WORK, DAMNN, BEST FEELING IN THE ENTIRE WORLD. What I was trying to do was if the bar with the label 1960 was clicked, then below the bar graph, all the coups that occurred in the year 1960 would appear. So I was trying to solve it but my nested .map() didn't work (I had a map within a map). What I later realized was that my syntaxes were wrong when doing nested .map(). So my logic was correct on how to solve this problem but my syntaxes were wrong. So, with the help of https://stackoverflow.com/questions/51615559/react-map-over-nested-array-of-objects, I was able to adapt the answer to fit my situation. ALSO, I need to organize my code cus it is so messy. the code works, but too messy.

---
## [magatsuchi/Skyrat-tg](https://github.com/magatsuchi/Skyrat-tg)@[b74df4cbdd...](https://github.com/magatsuchi/Skyrat-tg/commit/b74df4cbdd0c2618a4d8477a74a233fc883b7c19)
#### Sunday 2022-07-17 06:26:06 by SkyratBot

[MIRROR] Revisiting The Goliath: Or, that time I dripped out the SBC Starfury just because [MDB IGNORE] (#14813)

* Revisiting The Goliath: Or, that time I dripped out the SBC Starfury just because (#68126)

Drips the SHIT out of the SBC Starfury while not completely overhauling it. Touches everything NOT in engineering or southward (because I love how scuffed that part is and refuse to touch it on principle) - Also converts one map varedit into a real boy subtype, and moves tiny fans to their own file.

Mandatory disclosure on the gameplay changes:
Fighters 1 and 3 are now NOT in the hangar, and are now attached to the formerly unused gunnery rooms.
Cryo now works. Yeah. I know.
You can actually open the anesthetic closet now.
Everyone now shares three spawners. This doesn't reduce the amount of people who can play when this rolls, as I've adjusted var/uses in accordance: it just reduces clutter.
A few of the horizontal double airlocks have been compacted into glass_large airlocks.
The bar windows now actually have grilles like they were meant to.
Four turbines have shown up. They aren't functional*, they just look like gunnery and conveniently fit in the spots. I'm sure this is space OSHA compliant.
The map is ever so slightly smaller, vertically. This should distance us from an edge case where somehow all space levels are too cluttered for this to spawn properly, for the time being.

*Technically there's nothing stopping you from using them besides the amount of time it'd take for the operatives to kick your ass

This map was originally designed wayyy back before we even had the computer sprites we have now, (#27760 if you want to see SOUL) and it shows. While it will never have it's SM again, we can at least make the thing much nicer to look at.

* Revisiting The Goliath: Or, that time I dripped out the SBC Starfury just because

Co-authored-by: BluBerry016 <50649185+unit0016@users.noreply.github.com>

---
## [move-me-to-ipfs-shipyard/Thorin](https://github.com/move-me-to-ipfs-shipyard/Thorin)@[8749faaa57...](https://github.com/move-me-to-ipfs-shipyard/Thorin/commit/8749faaa57fc4d1cddb5e02b3856f5f7f2941c8e)
#### Sunday 2022-07-17 06:37:03 by Thorin

our 6th food for Asterix's magic potion is grapefruit - so desperately needed for vitamin-C and bitterness
:Kevin-Heart i could swear you said you were born in Hawaii - you said this is a cliff my mother held me over, i even remember you singing a song
:Dwayne-The-Rock-Johnson yeah, how did the song go?
:Kevin kuulaa matanaaa

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[22d57da140...](https://github.com/tgstation/tgstation/commit/22d57da14091d9bf7d8e1dcb7a5104b3f89eeec5)
#### Sunday 2022-07-17 08:55:17 by LemonInTheDark

Readds Alien Vore (#68312)

* Readds Alien Vore

Aliens can now eat people again. Behavior was removed by #43991 (b6c41e3b328078b72bd0f88fd46719aa99c55be2)
because nasku thought it was weird, and the code was really bad.

I think it's funny, and I've made the code not trashtier.

Basically, an alien can agressive grab any living mob. If they stay next
to the mob, facing them for 13 seconds, they will "eat" the mob,
IE:insert them into a list on their custom stomach.

The xeno can then hit an action button to spit out the mob, alongside
some acid.

If the mob is alive enough to pull out a weapon inside the xeno/has one
on it, they can attack the xeno from inside, dealing damage to the
creature and its stomach. If the stomach drops below a threshold, the
mob gibs the xeno and escapes.

I've done my best to steer things away from horny and into gross, though
I'm aware you fucks do your best to blur that line.

Anyway something something balance change something something lets xenos
abduct people more easily, I'm mostly doing this cause I think it has
soul.

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [Offroaders123/Funky-Pages](https://github.com/Offroaders123/Funky-Pages)@[fe88c2f53c...](https://github.com/Offroaders123/Funky-Pages/commit/fe88c2f53c8c9c21390b62fd1646c84ed33f2a11)
#### Sunday 2022-07-17 09:59:30 by Offroaders123

First Commit

A new Swift project!

I recently made the leap and got myself a new iPad mini 6th gen, and I've been using it to get back into investigating Swift again!
I first dabbled in Swift in 2020 and 2021 a bit, but I was feeling a bit overwhelmed with a new language and a feature-packed IDE (bloated, if I may dare XD), Xcode. I heard about Swift Playgrounds a short while ago, and it really gained my interest a bit. I like the idea that I didn't have to be at my desktop to work on Swift.

And some more info and things I wanted to make sure to note:

My first and foremost need for my new iPad is with GarageBand and music making, but this little surprise of Swift Playgrounds is definitely leading me down a new possible programming rabbit hole, and I am very interested in that!
Now that I have more tools at my disposal like Git and my Terminal knowledge, this seems more like something I can tackle now. The little bit I have looked into about TypeScript, JSX, and more object-oriented programming (and my JS fundamentals too, duh!) have definitely helped me start to wrap my head around how this all works a bit better, and how it is similar/dissimilar to the Web, which is a base for a lot of my programming knowledge (A note about that: Not that it gives me some authorization or something like that, but that all of those kinds of things really show where the dots are on the picture, and how I need to connect them, if that makes sense. It's like parts from each of those have taught me some of the fundamentals for Swift in other areas, where the things in JS I have learned may not have overlapped with).

There were a ton of articles that I used to start working on this: (I started this about two days ago (Got my iPad on the 14th :D), and I am just commiting everything now, now that something is actually working hehe. This is pretty much my first working-ish thing in Swift that I figured out myself, by connecting the dots with online articles and docs, like I've done with JS for a long time now. Finally finding nice Swift resources!)
https://www.learnui.design/blog/ios-design-guidelines-templates.html
https://www.hackingwithswift.com/articles/216/complete-guide-to-navigationview-in-swiftui
https://nemecek.be/blog/155/how-to-let-user-select-file-from-files
https://www.hackingwithswift.com/books/ios-swiftui/using-coordinators-to-manage-swiftui-view-controllers
https://developer.apple.com/documentation/uikit/uiviewcontroller
https://developer.apple.com/documentation/uikit/uidocumentpickerviewcontroller
https://capps.tech/blog/read-files-with-documentpicker-in-swiftui
https://developer.apple.com/documentation/uikit/view_controllers/providing_access_to_directories
https://www.youtube.com/watch?v=V-6o_Th4cPo

These also helped me set up my dev setup for this Git repo on my Mac:
https://stackoverflow.com/questions/35853139/can-git-and-icloud-drive-be-effectively-used-together
https://stackoverflow.com/questions/7130850/how-can-i-move-all-git-content-one-level-up-in-the-folder-hierarchy (Not used for this, but DEFINITELY great to note for myself later, as I have definitely done this the wrong way a few times before)
https://stackoverflow.com/questions/505467/can-i-store-the-git-folder-outside-the-files-i-want-tracked
https://stackoverflow.com/questions/51150343/changing-the-git-file-name-when-having-the-working-directory-in-a-separate-fold

A little breakdown about that real quick too:
So I edit my app with Swift Playgrounds on my iPad, which is then saved to iCloud Drive with every edit it seems to look like. I downloaded the Swift Playgrounds app on my Mac, which allows me to see the Playgrounds folder in iCloud Drive on my machine (it might have been accessible without the app, not sure, but either way).
I was going to create the git directory within the `.swiftpm` bundle which saves to iCloud Drive, but I was concerned about read and write times as there are a lot more files when dealing with the source control too. I don't really need the Git part of things in the cloud, so I looked to find a way to separate the working directory from the Git folder. Those last links above led the way, and now I have it working!
In my `~/Coding Projects/Funky-Pages/` folder, I have a top-level `.git` folder (essentially `Funky-Pages/` is the `.git` folder itself), and then it will look for the working directory files over in `~/Library/Mobile Documents/iCloud~com~apple~Playgrounds/Documents/Funky-Pages.swiftpm/`, which is what is synced back and forth to my iPad when I edit there.
So, with all of that set up, I can just edit over in Swift Playgrounds on my iPad, then wait for the modifications to come over to my Mac, and then use Git like normal through the CLI or GitHub Desktop like I would otherwise for my other local projects.
And yet another cool thing, since the app is written in SwiftUI, the same exact code can run as a Mac app in the Swift Playgrounds on my Mac! Super neat.

Quick note: The source files made myself are all the ones that aren't `Package.swift` or in `.swiftpm/`, those are automatically generated by Swift Playgrounds.

If you read that, you are a champ.

Now, what's next? A Swift NBT library? Probably. I gotta learn some more things first though!
Brandooon

P.S.
These are really relieving to write. While it may just be docs for my little code snippets, I like that I can come back and read about the things I have found and learned. I won't forget as many things per se, and I think it's cool that this might help someone looking for some information similar to this. Open source really is cool, and I love that it's so open! It's crazy how much information is out there, the fact that I can learn how to make something brand new, and that I have the possiblility to share my findings, which may also help someone else on the same path that I am trying to take.

---
## [Denperidge/monica](https://github.com/Denperidge/monica)@[087aa82e27...](https://github.com/Denperidge/monica/commit/087aa82e27d2b3f9882f7d48f5ae7bb995101f0e)
#### Sunday 2022-07-17 10:06:18 by Cat (she/they)

README change: referral to Asperger & Alzheimer's

This isn't code breaking! But I saw some phrasing that could perhaps be improved upon, to be more accommodating to as much people as possible.
This is probably not important to a lot of people nor general knowledge, so some context behind the rephrasing:
- "Suffer from" is a phrasing that got co-opted by people who see autism as a bad thing, something that has to be cured
- Asperger's syndrome, a.k.a. "high functioning autism" is only one subset of the spectrum. It makes sense that people with AS would be the most likely to reach out and give feedback, it'd be nice to also acknowledge the other subsets, along with "social disorders like" to include stuff that is akin to, but not exactly, ASD
- "Affected by Alzheimer's" also includes people who have someone with Alzheimer's in their life, who then also get use out of this app to make notes about their relative/friend/etc!

Hopefully these changes make sense, feel free to ask any questions, and thank you for reading!

---
## [aospa-sdm660/android_kernel_asus_sdm660](https://github.com/aospa-sdm660/android_kernel_asus_sdm660)@[32a6e1c1e8...](https://github.com/aospa-sdm660/android_kernel_asus_sdm660/commit/32a6e1c1e85832012983a1d656a0e439c1c0775c)
#### Sunday 2022-07-17 10:08:00 by Jason A. Donenfeld

random: credit cpu and bootloader seeds by default

[ Upstream commit 846bb97e131d7938847963cca00657c995b1fce1 ]

This commit changes the default Kconfig values of RANDOM_TRUST_CPU and
RANDOM_TRUST_BOOTLOADER to be Y by default. It does not change any
existing configs or change any kernel behavior. The reason for this is
several fold.

As background, I recently had an email thread with the kernel
maintainers of Fedora/RHEL, Debian, Ubuntu, Gentoo, Arch, NixOS, Alpine,
SUSE, and Void as recipients. I noted that some distros trust RDRAND,
some trust EFI, and some trust both, and I asked why or why not. There
wasn't really much of a "debate" but rather an interesting discussion of
what the historical reasons have been for this, and it came up that some
distros just missed the introduction of the bootloader Kconfig knob,
while another didn't want to enable it until there was a boot time
switch to turn it off for more concerned users (which has since been
added). The result of the rather uneventful discussion is that every
major Linux distro enables these two options by default.

While I didn't have really too strong of an opinion going into this
thread -- and I mostly wanted to learn what the distros' thinking was
one way or another -- ultimately I think their choice was a decent
enough one for a default option (which can be disabled at boot time).
I'll try to summarize the pros and cons:

Pros:

- The RNG machinery gets initialized super quickly, and there's no
  messing around with subsequent blocking behavior.

- The bootloader mechanism is used by kexec in order for the prior
  kernel to initialize the RNG of the next kernel, which increases
  the entropy available to early boot daemons of the next kernel.

- Previous objections related to backdoors centered around
  Dual_EC_DRBG-like kleptographic systems, in which observing some
  amount of the output stream enables an adversary holding the right key
  to determine the entire output stream.

  This used to be a partially justified concern, because RDRAND output
  was mixed into the output stream in varying ways, some of which may
  have lacked pre-image resistance (e.g. XOR or an LFSR).

  But this is no longer the case. Now, all usage of RDRAND and
  bootloader seeds go through a cryptographic hash function. This means
  that the CPU would have to compute a hash pre-image, which is not
  considered to be feasible (otherwise the hash function would be
  terribly broken).

- More generally, if the CPU is backdoored, the RNG is probably not the
  realistic vector of choice for an attacker.

- These CPU or bootloader seeds are far from being the only source of
  entropy. Rather, there is generally a pretty huge amount of entropy,
  not all of which is credited, especially on CPUs that support
  instructions like RDRAND. In other words, assuming RDRAND outputs all
  zeros, an attacker would *still* have to accurately model every single
  other entropy source also in use.

- The RNG now reseeds itself quite rapidly during boot, starting at 2
  seconds, then 4, then 8, then 16, and so forth, so that other sources
  of entropy get used without much delay.

- Paranoid users can set random.trust_{cpu,bootloader}=no in the kernel
  command line, and paranoid system builders can set the Kconfig options
  to N, so there's no reduction or restriction of optionality.

- It's a practical default.

- All the distros have it set this way. Microsoft and Apple trust it
  too. Bandwagon.

Cons:

- RDRAND *could* still be backdoored with something like a fixed key or
  limited space serial number seed or another indexable scheme like
  that. (However, it's hard to imagine threat models where the CPU is
  backdoored like this, yet people are still okay making *any*
  computations with it or connecting it to networks, etc.)

- RDRAND *could* be defective, rather than backdoored, and produce
  garbage that is in one way or another insufficient for crypto.

- Suggesting a *reduction* in paranoia, as this commit effectively does,
  may cause some to question my personal integrity as a "security
  person".

- Bootloader seeds and RDRAND are generally very difficult if not all
  together impossible to audit.

Keep in mind that this doesn't actually change any behavior. This
is just a change in the default Kconfig value. The distros already are
shipping kernels that set things this way.

Ard made an additional argument in [1]:

    We're at the mercy of firmware and micro-architecture anyway, given
    that we are also relying on it to ensure that every instruction in
    the kernel's executable image has been faithfully copied to memory,
    and that the CPU implements those instructions as documented. So I
    don't think firmware or ISA bugs related to RNGs deserve special
    treatment - if they are broken, we should quirk around them like we
    usually do. So enabling these by default is a step in the right
    direction IMHO.

In [2], Phil pointed out that having this disabled masked a bug that CI
otherwise would have caught:

    A clean 5.15.45 boots cleanly, whereas a downstream kernel shows the
    static key warning (but it does go on to boot). The significant
    difference is that our defconfigs set CONFIG_RANDOM_TRUST_BOOTLOADER=y
    defining that on top of multi_v7_defconfig demonstrates the issue on
    a clean 5.15.45. Conversely, not setting that option in a
    downstream kernel build avoids the warning

[1] https://lore.kernel.org/lkml/CAMj1kXGi+ieviFjXv9zQBSaGyyzeGW_VpMpTLJK8PJb2QHEQ-w@mail.gmail.com/
[2] https://lore.kernel.org/lkml/c47c42e3-1d56-5859-a6ad-976a1a3381c6@raspberrypi.com/

Cc: Theodore Ts'o <tytso@mit.edu>
Reviewed-by: Ard Biesheuvel <ardb@kernel.org>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [devil-ira/bevy](https://github.com/devil-ira/bevy)@[4847f7e3ad...](https://github.com/devil-ira/bevy/commit/4847f7e3adc835053a8907dd578c342b4bd395e2)
#### Sunday 2022-07-17 10:08:25 by ira

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
## [pistolPeterson/ISTW-GMTK-Game-Jam-Unity](https://github.com/pistolPeterson/ISTW-GMTK-Game-Jam-Unity)@[eb4b64bcda...](https://github.com/pistolPeterson/ISTW-GMTK-Game-Jam-Unity/commit/eb4b64bcda66fd5e29a5ec6893da1373c8bb80b6)
#### Sunday 2022-07-17 10:18:39 by Luis Ahumada

Menu Created

Started very late in the night. Is barely functional, and is using an asset from the unity store, which is probably my worst investment of all year, that doesn't do much.
Needs work on settings, but at least works as a main menu.
It's 6:15am, am running on two hours of sleep, [redacted] thoughts and an Oreo, and I'm ready to fight god, OR BECOME HIM

---
## [internalsystemerror/laminas-form](https://github.com/internalsystemerror/laminas-form)@[d854a56108...](https://github.com/internalsystemerror/laminas-form/commit/d854a5610889ff42d36076a46bb2422f37caa29b)
#### Sunday 2022-07-17 11:30:45 by Michał Bundyra

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
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[dd9c4fcb87...](https://github.com/mrakgr/The-Spiral-Language/commit/dd9c4fcb87e47087a6c9bf33ad6385f46da02b1a)
#### Sunday 2022-07-17 13:42:53 by Marko Grdinić

"```fs
| UnionTag, [DUnion(_,l) | DV(L(_,YUnion l)) as x] ->
```

Whops, this is a minor error, but the left side should never be triggered.

```fs
            | UnionTag, [DV(L(_,YUnion l)) as x] ->
                match l.Item.layout with
                | UHeap -> "->tag"
                | UStack -> ".tag"
                |> sprintf "%s%s" (tup_data x)
```

I didn't bother thinking how unions worked when I did this part. Since it does not change the functionality of the codegen, I won't bother publishing another update right now.

*

```fs
        | EOp(_,UnionTag,[a]) ->
            let eval k (h : Union) = h.Item.tags.[k] |> LitInt32 |> DLit
            match term s a with
            | DNominal(DV(L(_,YUnion h)) & a, _) ->
                match cse_tryfind s (TyOp(Unbox,[a])) with
                | Some (DPair(DSymbol k, _)) -> eval k h
                | Some _ -> raise_type_error s "Compiler error: Expected a symbol/value pair."
                | None -> push_op_no_rewrite s UnionTag a (YPrim Int32T)
            | DNominal(DUnion(DPair(DSymbol k,_),h), _) -> eval k h
            | a -> raise_type_error s <| sprintf "Expected an union.\nGot: %s" (show_data a)
```

Yeah, it only ever pushes a DV into the codegen stage. There is no problem. In fact...

```fs
            | UnionTag, [DV(L(i,YUnion l)) as x] ->
                match l.Item.layout with
                | UHeap -> "->tag"
                | UStack -> ".tag"
                |> sprintf "v%i%s" i
```

Let me do it like this. Now this should be perfect.

11:10am. Music, starto!

I should check out Cakewalk studio, but I remember reading about Magenta which uses NNs. So let me start with the later.

https://magenta.tensorflow.org/studio/

https://magenta.tensorflow.org/get-started

Oh, it has some style transfer stuff for images as well.

https://magenta.tensorflow.org/talks
> If you're interested in finding out more about our work, but don't want to go through all the blog posts, here are some conference talks about Magenta, both from team members and community collaborators!

I guess I'll watch one of these. Nothing since 2019 however. But that is fine, it is not like I'd be able to run the newer models anyway.

https://youtu.be/pM9u9xcM_cs?t=256

This is nice.

11:30am. It is going to be hard. Let me watch this and I'll in fact go back to the skeleton. If I start doing music right now, I'd just spend the whole day installing Ableton Live or whatever, but with Blender I could get something concrete done. Sculpting would not be a bad hobby for times like these.

12pm. It was a boring video I did not watch it all the way through.

1:30pm. https://spectrum.ieee.org/nuclear-submarine

Done with breakfast. LycoReco is really good. I am going to try opening Blender and seeing if I feel like doing sculpting. If I don't I'll just play BG2.

Before 2014, I did try writing, but never had the motivation to go beyond a few pages. Unless I have a big plan I generally don't feel like doing things.

1:35pm. The shark drone in that article looks pretty cool.

1:50pm. Let me give Blender a try again.

1:55pm. Let me try one of the easy bones. I am not that particularly interested in it. But maybe I will get into it.

2pm. The hops mirror mod is getting in the way. How do I get rid of it?

https://youtu.be/Sb0odwAjFok
NEW mirror option in HARDOPS for Blender

Now I am watching tutorials by Ryuu again.

Ugh, I could just clear from one and then copy the mods to all.

2:05pm. Nevermind. I'll isolate the individual piece I am working on. Let me go into isolation mode and then sculpt. Let's not waste time watching videos. I want to have fun with this.

2:10pm. Art is too much of a chore if I think too much about it. I won't treat is as programming and instead focus on just making a single piece. Forget those shitty block outs. I should started from the bones so as to not bore myself.

Ah, wait, I forgot what I was working on and was using the wrong bone as reference. Let undo a bit.

2:15pm. I think that unlike programming, art is not something you can really plow through. I thought back to where I went wrong for the last 9 months and I think the fun is what I was missing from it. I think somebody who just doodled 2d without caring so much about optimizing his workflow would have been superior to me.

I just didn't want to take the risk of doing that, but there are no shortcuts to skill. Well, apart from putting DALLE directly in your brain, but that is some ways away.

It is interesting to realize - when human level AIs come around, every one of them will have the ability to brain dump their imagination on canvas like DALLE.

2:35pm. Damn it, I sure have the doodling down. I look at the reference, forget it, and do my own thing instead.

I feel like I should be looking at the mental image of the model I am trying to make, but I am not doing that at all, instead I seem to be focused on my own moves.

This actually how I program, but I am not sure if that is how I should be doing art.

Also the reference is confusing me. I can't get a clear grasp of what the form of the bone I am trying to do should be. Forget the book, can I see a 3d scan or a move of the skeleton anatomy somewhere.

https://youtu.be/f8zQel-jAUY
Skeletal anatomy introduction

https://youtu.be/f8zQel-jAUY?t=45
> I am not going to tell you that bones are actually a living much more flexible tissue than we see here. This stiff brittle bone is what we see after death.

I see.

> We've got 206 bones in the body.

A lot of stuff to sculpt. As an artist, I'd need to be familiar with all of them.

https://youtu.be/f8zQel-jAUY?t=243

What the hell. How was I not aware that this bone existed? Was I blind?

No, I honestly don't see it in the sculptors book.

Let me ask on /3/.

2:50pm. Have to do some chores.

https://youtu.be/f8zQel-jAUY?t=681

This video is a lot clearer than the book when it comes to serving as a reference. Hopefully he will cover the feet.

3:25pm. https://youtu.be/f8zQel-jAUY?t=1196

Yeah, I am bored. Let me try giving the metatarsal bone a try again using this as a reference. If that fails, I'll move to clearing the De'Arnise's Keep of trolls.

https://youtu.be/f8zQel-jAUY?t=1182

This is a good shot.

3:30pm. https://youtu.be/f8zQel-jAUY?t=997

No, I can't stand this anymore. Without a great project that I want to do, I just do not have the motivation to plow through the hardship. Right now I'd rather just buy a skeleton from some store, even if I had to pay 50-100$ to do it.

3:30pm. I really should be programming AWS instead of trying to do sculpting. Hopefully I'll be able to start that tomorrow.

I did the C backend optimization so I did not waste the whole day, but I really hope I can start exercising my cloud computing skills tomorrow. I do not want to spend my precious time doing nothing or playing games."

---
## [suzzzuya/c_homework](https://github.com/suzzzuya/c_homework)@[b24c19c959...](https://github.com/suzzzuya/c_homework/commit/b24c19c9599808a0f61fa1693a1b25a60298ee0c)
#### Sunday 2022-07-17 15:15:48 by Dmitriy

You must take care of your pet. Watch his life-neccesary bars and don't let it die. Remember the game is working in real time, while the programm is running!

---
## [move-me-to-ipfs-shipyard/Fennec](https://github.com/move-me-to-ipfs-shipyard/Fennec)@[9e458859f5...](https://github.com/move-me-to-ipfs-shipyard/Fennec/commit/9e458859f534b31d549b1973e2343e4e7bbe06e4)
#### Sunday 2022-07-17 16:15:12 by Fennec

our final element is not Leeloo- it is water - as honest as B12, and we can savour and cronometer - we are that guy
:Jon-Stewart no, you come across to people as a big bear of a deep-shit - people look at you and say - oh my God, i'm better than this guy - that fat fuck - they told him to stood with a monkey and hold a baby - and now look at him go
:Zach-Galifiankis thanks, man

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[3b66f94bc5...](https://github.com/treckstar/yolo-octo-hipster/commit/3b66f94bc53dc45f02521981cd2874c7f9154b78)
#### Sunday 2022-07-17 17:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [repnop/rust](https://github.com/repnop/rust)@[b269213b35...](https://github.com/repnop/rust/commit/b269213b35f102a22b5a9645de48814fa255f7a2)
#### Sunday 2022-07-17 22:13:24 by Matthias Krüger

Rollup merge of #91387 - graydon:E0038-clarification, r=wesleywiser

Clarify and tidy up explanation of E0038

I ran into E0038 (specifically the `Self:Sized` constraint on object-safety) the other day and it seemed to me that the explanations I found floating around the internet were a bit .. wrong. Like they didn't make sense. And then I went and checked the official explanation here and it didn't make sense either.

As far as I can tell (reading through the history of the RFCs), two totally different aspects of object-safety have got tangled up in much of the writing on the subject:
  - Object-safety related to "not even theoretically possible" issues. This includes things like "methods that take or return Self by value", which obviously will never work for an unsized type in a world with fixed-size stack frames (and it'd be an opaque type anyways, which, ugh). This sort of thing was originally decided method-by-method, with non-object-safe methods stripped from objects; but in [RFC 0255](https://rust-lang.github.io/rfcs/0255-object-safety.html) this sort of per-impossible-method reasoning was made into a per-trait safety property (with the escape hatch left in where users could mark methods `where Self:Sized` to have them stripped before the trait's object safety is considered).
  - Object-safety related to "totally possible but ergonomically a little awkward" issues. Specifically in a trait with `Trait:Sized`, there's no a priori reason why this constraint makes the trait impossible to make into an object -- imagine it had nothing but harmless `&self`-taking methods. No problem! Who cares if the Trait requires its implementing types to be sized? As far as I can tell reading the history here, in both RFC 0255 and then later in [RFC 0546](https://rust-lang.github.io/rfcs/0546-Self-not-sized-by-default.html) it seems that the motivation for making `Trait:Sized` be non-object-safe has _nothing to do_ with the impossibility of making objects out of such types, and everything to do with enabling "[a trait object SomeTrait to implement the trait SomeTrait](https://rust-lang.github.io/rfcs/0546-Self-not-sized-by-default.html#motivation)". That is, since `dyn Trait` is unsized, if `Trait:Sized` then you can never have the automatic (and reasonable) ergonomic implicit `impl Trait for dyn Trait`. And the authors of that RFC really wanted that automatic implicit implementation of `Trait` for `dyn Trait`. So they just defined `Trait:Sized` as non-object safe -- no `dyn Trait` can ever exist that the compiler can't synthesize such an impl for. Well enough!

However, I noticed in my reading-and-reconstruction that lots of documentation on the internet, including forum and Q&A site answers and (most worrying) the compiler explanation all kinda grasp at something like the first ("not theoretically possible") explanation, and fail to mention the second ("just an ergonomic constraint") explanation. So I figured I'd clean up the docs to clarify, maybe confuse the next person less (unless of course I'm misreading the history here and misunderstanding motives -- please let me know if so!)

While here I also did some cleanups:

  - Rewrote the preamble, trying to help the user get a little better oriented (I found the existing preamble a bit scattered).
  - Modernized notation (using `dyn Trait`)
  - Changed the section headings to all be written with the same logical sense: to all be written as "conditions that violate object safety" rather than a mix of that and the negated form "conditions that must not happen in order to ensure object safety".

I think there's a fair bit more to clean up in this doc -- the later sections get a bit rambly and I suspect there should be a completely separated-out section covering the `where Self:Sized` escape hatch for instructing the compiler to "do the old thing" and strip methods off traits when turning them into objects (it's a bit buried as a digression in the individual sub-error sections). But I did what I had time for now.

---
## [RobertZhudetti/BitWire](https://github.com/RobertZhudetti/BitWire)@[3a7a36e079...](https://github.com/RobertZhudetti/BitWire/commit/3a7a36e079df71f52d64db699c90cf96d721e1d4)
#### Sunday 2022-07-17 22:30:27 by Robert M. Zhudetti

Fixed stupid mistake that screwed up pin settings in weird ways.

(Don't write low level pin manipulation fuctions while half asleep
boys and girls ;) )

---
## [ARF-SS13/coyote-bayou](https://github.com/ARF-SS13/coyote-bayou)@[118a3d6fc0...](https://github.com/ARF-SS13/coyote-bayou/commit/118a3d6fc09a1d6a680fe76f070087342bbb8c80)
#### Sunday 2022-07-17 22:56:20 by Tk420634

Heavens Night Upper Floor

Now with sleepyshops, or fucktents.   Your call.

---

