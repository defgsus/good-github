## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-06-15](docs/good-messages/2022/2022-06-15.md)


1,727,223 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,727,223 were push events containing 2,729,881 commit messages that amount to 194,370,398 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 21 messages:


## [Khalvat-M/kernel_samsung_msm8974](https://github.com/Khalvat-M/kernel_samsung_msm8974)@[cceb3c1fb4...](https://github.com/Khalvat-M/kernel_samsung_msm8974/commit/cceb3c1fb42139e9059af43302e21f4335a5dc33)
#### Wednesday 2022-06-15 00:44:18 by KOSAKI Motohiro

mqueue: don't use kmalloc with KMALLOC_MAX_SIZE

KMALLOC_MAX_SIZE is not a good threshold.  It is extremely high and
problematic.  Unfortunately, some silly drivers depend on this and we
can't change it.  But any new code needn't use such extreme ugly high
order allocations.  It brings us awful fragmentation issues and system
slowdown.

Signed-off-by: KOSAKI Motohiro <mkosaki@jp.fujitsu.com>
Acked-by: Doug Ledford <dledford@redhat.com>
Acked-by: Joe Korty <joe.korty@ccur.com>
Cc: Amerigo Wang <amwang@redhat.com>
Cc: Serge E. Hallyn <serue@us.ibm.com>
Cc: Jiri Slaby <jslaby@suse.cz>
Cc: Joe Korty <joe.korty@ccur.com>
Cc: Manfred Spraul <manfred@colorfullife.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [bob-b-b/tgstation](https://github.com/bob-b-b/tgstation)@[20e4add487...](https://github.com/bob-b-b/tgstation/commit/20e4add48712b59e9bcadd187beee54c02f98e38)
#### Wednesday 2022-06-15 00:59:01 by Tim

Change healing by sleeping to be affected by sanity, darkness (or blindfold), and earmuffs. (#65713)


About The Pull Request

Depending on the mob's sanity level, it can have a positive or negative boost to healing effects while sleeping. Sleeping in darkness, wearing a blindfold, and using earmuffs also counts as a healing bonus. Beauty sleep is very important for 2D spessmen.
Why It's Good For The Game

This is a small gameplay change that rewards players for keeping their sanity at good levels. Also depression has also been linked with impeding wound healing in real life. The placebo effect on peoples minds is strenuously documented and I think it would be cool to see it in the game.
Changelog

cl
expansion: Healing by sleeping is now affected by sanity, sleeping in darkness (or using a blindfold), and using earmuffs. The healing from sleeping in a bed was slightly decreased.
/cl

---
## [tannerhelland/PhotoDemon](https://github.com/tannerhelland/PhotoDemon)@[9f19bd5ff4...](https://github.com/tannerhelland/PhotoDemon/commit/9f19bd5ff4700f5d5be5fc5a1d610133c7d075ca)
#### Wednesday 2022-06-15 01:20:41 by Tanner

File > Export > Color lookup: this is actually gonna work!

I honestly didn't know if this homebrew LUT creation strategy would work, but it does!  Yay!

Here's the gist:

3D LUTs are used in a number of industries - video editing, game development, photography, etc.  LUT files exist in a bunch of different formats, and they're basically just giant tables that map colors from one domain to another.  Such tables are extremely helpful for taking complex color transforms with a ton of steps and reducing them into a single table that applies *all* those changes at once - e.g. in a game pipeline you might bump up brightness, reduce yellow tones, increase contrast, improve clarity at high and low ranges of the green spectrum, give everything a slightly violet tint, then tone-map that into a final screen-ready gamut. - but doing all those steps separately takes forever, so instead at development time you use Photoshop (or dedicated color-grading software) to create a LUT that performs all of those steps on every color in the spectrum (or a reasonably representative subset of colors), stores the final mapping of each color in a giant list, and then at run-time you can just apply that LUT to each frame to apply your huge list of edits in a single uniform pass.  Whether you're doing 100 adjustments or 1 doesn't matter - a LUT merges all those changes into a single mapping table that does it for you.

LUTs are also used extensively for color-grading photos and film, because once you develop a signature "look" you can simply merge the full pipeline of edits into a single LUT, and with one click you get that "look" on any arbitrary photo, video, whatever.  LUTs are one of the few photo editing things that works across almost any software and/or platform because at the end of the day, LUTs are pretty much just text files with encoded RGB tables inside.  So even if your software doesn't support e.g. a Curves tool, you can let users load a LUT created in software that *does* support curve adjustments and then apply it, because software doesn't care how a LUT was created - it just uses the embedded tables to convert all colors to new values.

So applying LUTs is the easy part.  PhotoDemon supports a number of LUT formats and lets you apply them to images the same way any other photo editor does.  But creating LUTs is a different story, and there was no way to *create* new LUTs inside PD... until this commit.

Photoshop limits LUT creation to adjustment layers specifically - you have to set up 1+ adjustment layers on an image, and then you can export the resulting merged adjustment-layer-transform into a new LUT file.  This is cool, obviously, and relatively easy to support because the possible range of edits is small.  But PhotoDemon doesn't provide adjustment layers (yet) and even Photoshop only supports a subset of its full Adjustment tool library as adjustment layers.  Wouldn't it be better if you could just edit a photo using ANY AND EVERY TOOL in the app, and then the app would magically reverse-engineer a LUT for you, encompassing all the changes you'd made?

That's what I've attempted to do in PhotoDemon, and by god, it works.  Mostly.  It's a little slow right now due to huge numbers of classes used in the necessary data structs (so the code is fast, but class teardown is like 60 seconds for the hundreds of thousands of classes that get created), so I'll need to rewrite some data structures either using lightweight classes or by converting them to array-driven methods.  But that's easy stuff compared to the work that's already been done!

Now for the caveats.

LUTs encode 1:1 mapping between colors, so they cannot encode area-driven effects (like blur, distort filters, etc).  This means they are best at encoding edits from Adjustment menu tools, but you don't really need to care about that - if you use any Effects, PhotoDemon can still auto-create LUTs for you!  But if the same color gets mapped to multiple output colors (due to a blur effect or similar), the quality of the LUT will suffer.

For the next caveat, I need to describe PD's LUT creator works.  Basically, the algorithm starts by comparing the final, edited image state to its original, unmodified state.  A huge tree of all represented colors is constructed, and the algorithm analyzes how each color has changed.  From that list of changes, it constructs a full-gamut LUT, directly using relevant color changes where it can and interpolating changes from similar colors for any parts of the color spectrum that the current image doesn't include.  This encodes most "normal" adjustment patterns very well, but can produce weird results if your source image has a very limited palette (e.g. it's grayscale, or mostly a single color tone, etc).

So for best results, if you intend to export a LUT you'll want to perform your adjustments/effects/etc on a photo with reasonably good color diversity - lots of dark and bright tones of as many different colors as possible.  This gives the LUT creator more information to work with, and the resulting LUT file will be more applicable to any type of image.

Next up is resolving the damn VB6 class teardown perf issue, then looking at an improved interpolation strategy that provides more accurate coverage of massive state changes (like "invert all colors").  I also want to write a new Render effect for generating color test patterns, which would help immensely for improving gamut coverage.

I need this tool available so that I can finally create a default set of LUTs to ship with PhotoDemon.  I want to provide similar LUTs to Photoshop's default set, but they copyright their LUTs (which seems silly - can you really copyright a list of numbers?  idk).  So I can't just ship Photoshop's files outright - but I can certainly make my own set of edits that produce a similar result to theirs, then create my own LUT files and ship *those*.  So that's what I'm gonna do.

Anyway, I legitimately didn't know if this strategy would work, so I'm pretty stoked to have a workable path forward for this feature.

---
## [cheekybrdy/goonstation](https://github.com/cheekybrdy/goonstation)@[87a7ec3ee8...](https://github.com/cheekybrdy/goonstation/commit/87a7ec3ee8fbcadcce5bd453b5399ce1c20ec526)
#### Wednesday 2022-06-15 02:09:09 by cheekybrdy

Fixes done

Spread out crew area☒ (thought split maint equaling main hallways meant that antags would be disadvantaged especially vamps so I tried to make SE and SW wings lower traffic. Was this antag issue a misdiagnosis?
Squishy Silicon rooms☑
More Space needs to be used? ☑

MOVE THE SYNDICATE OUTPOST (/) ☑
use the big medbay lobby properly ☑

split ghosties?☒

Major issues
-I'm not going to complain about the many pipes going through walls since most maps do that in places (except for the disposal pipe in west medbay that one's just nasty), but several areas are set up wrong (particularly around sec but not exclusively). Pipes can cross over one another fine but you can't put multiple in the same direction on the same tile, the system isn't advanced enough to handle that.☑
-Although I appreciate criming toys, the syndie destruction, purge and rewind systems in maint are well into overkill for maint goodies.☑
-The mail network as is won't function as most things end up in the mail room. The pipes need to loop back at some point. (see cog1 for a simple setup, and cog2 for one that has several loops and a central router)☑
-/area/station/chapel is an abstract type for some reason, but you can just make the whole chapel the sanctuary subtype☑
-The listening post is kinda fucked in general: it's not meant to be on station, the wall between the foyer and the cairngorm teleporter is simulated, and I'm pretty sure the buddies in there are just hostile to everybody. Also the strelka isn't appropriate.☑
-The 3 N2O cans in the patho sector are, but it might be fine if you replace them with a static N2O tank (probably enough to feed all the rooms too). The N2O pressure tank in engineering seems odd too, but I personally approve. :P☒ (static in patho changed)
-Quartermasters don't have engineering access, so they can't open one of the doors to get in their office. When they get there, they're missing a bunch of manufacturers and a way to easily get crates out front.☒ (the out the front bit, rest makes since
-Your engine is hotwired by default. To map SMESes properly, you need to lead the raw engine output into /obj/machinery/power/terminals that feed into the SMESes. Then you can have a wire from under the SMES to the station grid. If you need an example cog1 is probably easiest, because the raw engine wire is brown and easier to follow because of that. When you fix this, also look at the spare SMES in security.☑
-Speaking of that room with the SMES, dedicated execution chambers really aren't a good vibe.☒
-I'm not sure if the mining teleporter functions on space maps. The mineral magnet is also rectangular and I think it needs to be square to function.☒ (magnet changes done).
-Jazz lounge looking straight onto a major hallway limits its capacity for crime.☐
-The inputs to the huge toxins burn chambers and the mixer need pumps/valves.☑
-All of medbay has just one nanomed to supply them.☑
-6 tasers and 4 eguns in the armoury is fairly spicy. Might get antags to pay attention to the dang place though. :P (Probably ask others for second opinions on that one, I'm not a sec/combat balance person)☒
-I appreciate this is probably because the map is a draft, but there's so few windows into places.☑ (WIP)
Minor issues/concerns
-Red crosses in medbay are (to my knowledge) discouraged, so the one in medbay's floor should maybe be changed.☑
-If the free-standing bit of medbay is meant to be another pathology lab, it's missing an autoclave☑
-I don't remember patho that well but 8 centrifuges seems way superfluous☑
-Armory auth computer isn't an appropriate match for the ☑ (placeholder for what likley will be blue retextured armoury auth)
-Also I don't think it can do any harm, but why the nuclear centrifuge in there?☑
-I appreciate you've got the cleanerbot in robotics, but usually there's a drain near the operating tables too☑
-The robotics database is unused and I think doesn't do anything☑
-You don't need to add Faith to the chaplain's locker, they spawn with it.☒
-The long couch (whose comical length I love) doesn't have proper ends☑
-Some of the chapel pews are missing the top bit☑
-Library doesn't need the torpedo guide if the map doesn't have torpedos☑ (intended as a late manta reference)
-Space tile under the NAS-T in the listening post foyer, and another under a conveyor in the ghostdrone factory☑
-A few misplaced firedoors around the bridge☑
-The bridge windows need electrification☑
-I think data terminals need a wire with a node at the center to work, and if I'm correct in that the mainframe isn't☑
-Missing turret control for the computer core☑
-Missing corner in that nasty disposal pipe in west medbay☑
-Missing wire for the APC to that main engineering/atmospherics room☑
-What are those carousel units in engineering going to power?☑
-Missing wall in the telesci pad room☑
-Missing mug rack in the medbay break room (critical, I know), same with sec.☑
-The shower room in the medbay/bar cluster is only accessible via maint?☒ (less accessibility for crimeing)
-EVA missing tank dispenser and RCD crate, luminol grenade is kinda weird to see there?☑
-Missing bit of pipe under a chute in botany☑
-Sauna pipe junction is probably non-functional, but there's dedicated junctions instead. (I think you have to search for manifold)☑
-Missing wire corner near in sauna/barber maint☑
-I haven't heard of the prototype Nano-fabricator (the blue tinted one), but it seems like it has no recipes.☐
-Prototype RCD in tool storage is, I think, a deathtrap from an azone.☑
-A few of the main station sections are done in plating instead of floortiles☑
-Medbay hand trader is missing the supply marker☑
-Missing cap's spare☑
-Misplaced bedsheet in bridge wall.☑
-Bar doesn't have a reagent heater, bartender is kinda just missing the stuff normally in their office too.☑
-Robotics is missing the borg parts crate I think☑
-Chemistry is missing a bunch of glasswear and stuff, also there's no source of welding fuel in all of sci.☑
-Clock 188 in the HoS room?☒ ( want to make office work a breakin)

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[9428d97a4f...](https://github.com/tgstation/tgstation/commit/9428d97a4fadf8a486b0c6fbe2ee345a2780e687)
#### Wednesday 2022-06-15 03:54:05 by Imaginos16

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
## [cheekybrdy/goonstation](https://github.com/cheekybrdy/goonstation)@[e55afc8f2f...](https://github.com/cheekybrdy/goonstation/commit/e55afc8f2f35d6fbf5ab375d2fb6c7d061b3de20)
#### Wednesday 2022-06-15 04:22:37 by cheekybrdy

Suggestions Implemented

Major issues
-I'm not going to complain about the many pipes going through walls since most maps do that in places (except for the disposal pipe in west medbay that one's just nasty), but several areas are set up wrong (particularly around sec but not exclusively). Pipes can cross over one another fine but you can't put multiple in the same direction on the same tile, the system isn't advanced enough to handle that.☑
-Although I appreciate criming toys, the syndie destruction, purge and rewind systems in maint are well into overkill for maint goodies.☑
-The mail network as is won't function as most things end up in the mail room. The pipes need to loop back at some point. (see cog1 for a simple setup, and cog2 for one that has several loops and a central router)☑
-/area/station/chapel is an abstract type for some reason, but you can just make the whole chapel the sanctuary subtype☑
-The listening post is kinda fucked in general: it's not meant to be on station, the wall between the foyer and the cairngorm teleporter is simulated, and I'm pretty sure the buddies in there are just hostile to everybody. Also the strelka isn't appropriate.☑
-The 3 N2O cans in the patho sector are, but it might be fine if you replace them with a static N2O tank (probably enough to feed all the rooms too). The N2O pressure tank in engineering seems odd too, but I personally approve. :P☒ (static in patho changed)
-Quartermasters don't have engineering access, so they can't open one of the doors to get in their office. When they get there, they're missing a bunch of manufacturers and a way to easily get crates out front.☒ (the out the front bit, rest makes since
-Your engine is hotwired by default. To map SMESes properly, you need to lead the raw engine output into /obj/machinery/power/terminals that feed into the SMESes. Then you can have a wire from under the SMES to the station grid. If you need an example cog1 is probably easiest, because the raw engine wire is brown and easier to follow because of that. When you fix this, also look at the spare SMES in security.☑
-Speaking of that room with the SMES, dedicated execution chambers really aren't a good vibe.☒
-I'm not sure if the mining teleporter functions on space maps. The mineral magnet is also rectangular and I think it needs to be square to function.☒ (magnet changes done).
-Jazz lounge looking straight onto a major hallway limits its capacity for crime.☑
-The inputs to the huge toxins burn chambers and the mixer need pumps/valves.☑
-All of medbay has just one nanomed to supply them.☑
-6 tasers and 4 eguns in the armoury is fairly spicy. Might get antags to pay attention to the dang place though. :P (Probably ask others for second opinions on that one, I'm not a sec/combat balance person)☒ (idk input needed)
-I appreciate this is probably because the map is a draft, but there's so few windows into places.☑ (WIP)
Minor issues/concerns
-Red crosses in medbay are (to my knowledge) discouraged, so the one in medbay's floor should maybe be changed.☑
-If the free-standing bit of medbay is meant to be another pathology lab, it's missing an autoclave☑
-I don't remember patho that well but 8 centrifuges seems way superfluous☑
-Armory auth computer isn't an appropriate match for the ☑ (placeholder for what likley will be blue retextured armoury auth)
-Also I don't think it can do any harm, but why the nuclear centrifuge in there?☑
-I appreciate you've got the cleanerbot in robotics, but usually there's a drain near the operating tables too☑
-The robotics database is unused and I think doesn't do anything☑
-You don't need to add Faith to the chaplain's locker, they spawn with it.☒
-The long couch (whose comical length I love) doesn't have proper ends☑
-Some of the chapel pews are missing the top bit☑
-Library doesn't need the torpedo guide if the map doesn't have torpedos☑ (intended as a late manta reference)
-Space tile under the NAS-T in the listening post foyer, and another under a conveyor in the ghostdrone factory☑
-A few misplaced firedoors around the bridge☑
-The bridge windows need electrification☑
-I think data terminals need a wire with a node at the center to work, and if I'm correct in that the mainframe isn't☑
-Missing turret control for the computer core☑
-Missing corner in that nasty disposal pipe in west medbay☑
-Missing wire for the APC to that main engineering/atmospherics room☑
-What are those carousel units in engineering going to power?☑
-Missing wall in the telesci pad room☑
-Missing mug rack in the medbay break room (critical, I know), same with sec.☑
-The shower room in the medbay/bar cluster is only accessible via maint?☒ (less accessibility for crimeing)
-EVA missing tank dispenser and RCD crate, luminol grenade is kinda weird to see there?☑
-Missing bit of pipe under a chute in botany☑
-Sauna pipe junction is probably non-functional, but there's dedicated junctions instead. (I think you have to search for manifold)☑
-Missing wire corner near in sauna/barber maint☑
-I haven't heard of the prototype Nano-fabricator (the blue tinted one), but it seems like it has no recipes.☑
-Prototype RCD in tool storage is, I think, a deathtrap from an azone.☑
-A few of the main station sections are done in plating instead of floortiles☑
-Medbay hand trader is missing the supply marker☑
-Missing cap's spare☑
-Misplaced bedsheet in bridge wall.☑
-Bar doesn't have a reagent heater, bartender is kinda just missing the stuff normally in their office too.☑
-Robotics is missing the borg parts crate I think☑
-Chemistry is missing a bunch of glasswear and stuff, also there's no source of welding fuel in all of sci.☑
-Clock 188 in the HoS room?☒ (Want people to have incentive to break into HoS private quarters).

---
## [Kry9toN/kernel_xiaomi_sm6250](https://github.com/Kry9toN/kernel_xiaomi_sm6250)@[b6bb10940d...](https://github.com/Kry9toN/kernel_xiaomi_sm6250/commit/b6bb10940ddc7132a19eaa83bf6265ac498be788)
#### Wednesday 2022-06-15 07:18:06 by Maciej Żenczykowski

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
## [furcan/next.js](https://github.com/furcan/next.js)@[91146b23a2...](https://github.com/furcan/next.js/commit/91146b23a21e33d54332a469f30afe6e6156cd65)
#### Wednesday 2022-06-15 07:26:01 by Glenn Gijsberts

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
## [newstools/2022-express](https://github.com/newstools/2022-express)@[ba013f2df2...](https://github.com/newstools/2022-express/commit/ba013f2df29fbf8bfa8f4e0b622299e2ff11afb3)
#### Wednesday 2022-06-15 12:12:31 by Billy Einkamerer

Created Text For URL [www.express.co.uk/life-style/life/1625764/heatwave-hacks-hot-weather-summer-how-to-cool-down-house-night-sleep-hot-water-bottle]

---
## [RocketChat/Rocket.Chat](https://github.com/RocketChat/Rocket.Chat)@[5a37518e42...](https://github.com/RocketChat/Rocket.Chat/commit/5a37518e42dec114e0ed1a71b5d103b4a62e9b58)
#### Wednesday 2022-06-15 12:12:42 by Ben Wiederhake

[FIX] Client-generated sort parameters in channel directory  (#25768)

## Proposed changes (including videos or screenshots)
- In the web-client, sorting the channel directory by "Last Message" raises the error "Invalid sort parameter provided".

I don't think a screenshot is necessary, but if you'd like one anyway, here it is:

![Bildschirmfoto_2022-06-06_12-54-34](https://user-images.githubusercontent.com/2690845/172147996-e9942daf-6819-4eee-afa4-b1c6bce7a650.png)


## Issue(s)
Closes #25695

## Steps to test or reproduce

- Open the web client, i.e. navigate your browser to `https://rocketchat.$DOMAIN/home`
- Click the "Directory" button in the top left, (or just navigate directly to `https://rocketchat.$DOMAIN/directory/channels`)
- In the table header, click on "Last message" once
- In the table header, click on "Last message" again

Expected behavior: Clicking "Last message" turns on and then toggles sorting by the date of the last message, either first ascending and then descending, or the other way around.

Actual behavior: The first click sorts the messages in ascending order (good!), the second click shows a red warning box "FIXME", the table content disappears, and is replaced by throbbing grey placeholders.

### "Good" request (ascending order):

`https://rocketchat.domain.org/api/v1/directory?query=%7B%22type%22%3A%22channels%22%2C%22text%22%3A%22%22%2C%22workspace%22%3A%22local%22%7D&sort=%7B%22lastMessage%22%3A1%7D&count=25`

More easily readable GET parameters:

```
query | {"type":"channels","text":"","workspace":"local"}
sort | {"lastMessage":1}
count | 25
```

Response:
```
{"result":[{"_id":"AAAAAAAAAAAAAAAAA","name":"foobar","fname":"foobar","t":"c","usersCount":10,"ts":"2019-01-01T00:00:00.000Z","default":false,"lastMessage":{"_id":"AAAAAAAAAAAAAAAAA","rid":"AAAAAAAAAAAAAAAAA","msg":"Hello, World!","ts":"2019-01-01T00:00:00.000Z","u":{"_id":"AAAAAAAAAAAAAAAAA","username":"normaluser","name":"normaluser"},"unread":true,"_updatedAt":"2019-01-01T00:00:00.000Z","urls":[],"mentions":[],"channels":[]},"description":"Obviously, this JSON response is heavily censored."}],"count":25,"offset":0,"total":52,"success":true}
```

(Obviously, this JSON response is heavily censored, but you get the gist: It was successful.)

### "Bad" request (descending order):

`https://rocketchat.domain.org/api/v1/directory?query=%7B%22type%22%3A%22channels%22%2C%22text%22%3A%22%22%2C%22workspace%22%3A%22local%22%7D&sort=%7B%22lastMessage%22%3A0%7D&count=25`

More easily readable GET parameters:

```
query | {"type":"channels","text":"","workspace":"local"}
sort | {"lastMessage":0}
count | 25
```

Response:
```
{"success":false,"error":"Invalid sort parameter provided: \"{\"lastMessage\":0}\" [error-invalid-sort]","errorType":"error-invalid-sort","details":{"helperMethod":"parseJsonQuery"}}
```

## Further comments

Version on the server where I noticed this: `https://rocketchat.$DOMAIN/api/info` returns `{"version":"4.8","success":true}`. According to the "Releases" page, this version appeared 5 days ago, so I believe this is up to date.

### The journey to here

For some reason, the descending order uses the wrong magic number "0", and the server can't interpret that. However, this *used* to work, so I'm not very sure about this.

The error message appears in the source code of the entire organization exactly once: https://github.com/RocketChat/Rocket.Chat/blob/31ae30f30ad71d9e5a1b0cad494b3471a7dd8807/apps/meteor/app/api/server/helpers/parseJsonQuery.ts#L42
So I'll guess that this is the line of code that generated this particular message.

A few lines above we see that the server only knows 1 and -1 as magic numbers for the sorting:
https://github.com/RocketChat/Rocket.Chat/blob/31ae30f30ad71d9e5a1b0cad494b3471a7dd8807/apps/meteor/app/api/server/helpers/parseJsonQuery.ts#L35
This matches the observed bug: The browser sends 1 (which works) and 0 (which doesn't work).

Generally, it seems that the web client actually uses the strings "asc" and "desc" internally, which are hard to mix up. So I assume that it's the conversion of that is broken somehow.

Exactly this seems to be the case here:
https://github.com/RocketChat/Rocket.Chat/blob/31ae30f30ad71d9e5a1b0cad494b3471a7dd8807/apps/meteor/client/views/directory/hooks.js#L11

The code around it produces exactly the kind of query seen in the network log, and can also produce the buggy parameter `sort: 0`. This either fixes bug #25695, or a different bug of the same kind.

I am not sure how to add tests for this, can someone do this for me or show me where to start? I'm actually just an end-user and "accidentally" found the fix for the bug while writing the bug report ^^'

EDIT: Rebased for convenience, and to re-check CI.

---
## [canalplus/rx-player](https://github.com/canalplus/rx-player)@[6bb50f25a7...](https://github.com/canalplus/rx-player/commit/6bb50f25a701627592ad3238b896c27390a01a54)
#### Wednesday 2022-06-15 12:51:38 by Paul Berberian

Update most dependencies but Jest

This commit update almost all dependencies but jest.

This is because Jest 28 seems to break while running code, presumably
due to `import`/`export` declarations in imported RxJS files (but I do
not think RxJS is at fault here) that lead to an `unexpected token` when
running through Jest.

You could think that the fault is linked to node not understanding
`import`/`export` (linked to CommonJS/ES6 import shenanigans) but it is
even trickier than that as Jest already performed some JavaScript
transformation at that point, which made the import/export inside an
IIFE - and I'm not sure that this is supported anywhere.

After taking ~a day (much more time than I should) trying to play around
to remove that issue, I gave up and avoided updating Jest to its v28.

In the future, I guess we should either:

  - understand what we're supposed to do here to make it work with Jest
    28 (Jest documentation was poor - even without considering the
    sometimes incomprehensible google-translated french one I get each
    time by default on their docusaurus-based documentation)

    Opened GitHub issues were 100% for angular-based applications - as it
    seems the RxJS+TypeScript cocktail is very majoritarily those. Those
    have their own "fix" through another magical angular dependency.

    Moreover, it does not help that Jest's philosophy seems to be trying to be
    extremely simple for users at the cost of some complex behaviors (as an
    example, it looks like it auto-picks a `babel.config.js` file if it
    sees one at the root of the project. If like us you have multiple build
    files at the root depending on the building context, it is not a good
    idea to silently pick random files like that by default).

    I couldn't understand under an acceptable time where the issue was - and
    at which step it happened.
    I just browsed dozens of doc pages, GitHub and StackOverflow issues
    which just proposed to add yet other automagic dependencies (looked like a
    parody of what JavaScript haters talk about!) - which all seemed to have
    no effect whatsoever.

    I also asked for help from other teams at Canal+, but those in the
    same situation (TypeScript and RxJS) also seem to have random issue
    preventing them from doing the switch.

  - Remove RxJS from the code. It's presumably not its fault yet we
    already started doing that, so maybe we'll just raise the jest
    version once RxJS is definitely removed from the RxPlayer.

  - Wait for some kind of Jest fix or new way of handling those?

  - Remove Jest and go with another testing framework.

    I almost did that due to being fed-up with Jest, but it might no be
    as easy as it seems, mostly the module-mocking part as I'm unsure of
    how other framework handle that now and if it is as convenient as
    Jest's way.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[f27d9796ea...](https://github.com/treckstar/yolo-octo-hipster/commit/f27d9796eaeb345e46d2e2301a9feff69a434b6f)
#### Wednesday 2022-06-15 13:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [LuoYi-SG/My-code](https://github.com/LuoYi-SG/My-code)@[6ac7ff612d...](https://github.com/LuoYi-SG/My-code/commit/6ac7ff612d916b60dc36ff80886f6a13f611e97b)
#### Wednesday 2022-06-15 13:43:22 by Luo Yi

Mad Libs generator

This tells a tale about a person and his/her friend going for an adventure. You just enter words by following the instructions given, and it will give you a story based on my storyline. It is kind of random but it is funny although it might not make sense. Enjoy :)

---
## [the-dwasint-foundation/MonkeStation](https://github.com/the-dwasint-foundation/MonkeStation)@[ada837ddc0...](https://github.com/the-dwasint-foundation/MonkeStation/commit/ada837ddc0840bb3a6dd1631d8c752a71853366c)
#### Wednesday 2022-06-15 13:58:12 by BluBerry016

Exploration PP - Reworks Outpost Nuke Announcement (#450)

* Fuck you, die

* Update nuke_ruin.dm

---
## [uclouvain/osis-portal](https://github.com/uclouvain/osis-portal)@[797852bc38...](https://github.com/uclouvain/osis-portal/commit/797852bc3880c027afb3be7cb9cc445602d072e9)
#### Wednesday 2022-06-15 15:03:11 by mathieuzen

OSIS-6757 in every life we have some trouble, but when you worry you make it double

=> don't worry be happy

---
## [giantswarm/azure-admission-controller](https://github.com/giantswarm/azure-admission-controller)@[84f1ccf1d9...](https://github.com/giantswarm/azure-admission-controller/commit/84f1ccf1d91516d6c95d4eb07e0214aa569f0c6c)
#### Wednesday 2022-06-15 15:35:40 by Christian Bianchi

Resiliency (#405)

* Improve resiliency and speed

* fuck you nancy

* fix VPA manifest

---
## [Addust/tgstation](https://github.com/Addust/tgstation)@[a3c8013b45...](https://github.com/Addust/tgstation/commit/a3c8013b45c92fdb8efec7ba827d7b00191e2d55)
#### Wednesday 2022-06-15 17:03:55 by GoldenAlpharex

Refactors how legs are displayed so they no longer appear above one-another when looking EAST or WEST (#66607)

So, for over 5 years, left legs have been displaying over right legs. Never noticed it? Don't blame you.
Here's a nice picture provided by #20603 (Bodypart sprites render with incorrect layering), that clearly displays the issue that was happening:

It still happened to this day.
Notice how the two directions don't look the same? That's because the left leg is always displaying above the right one.

Obviously, that's no good, and I was like "oh, that's a rendering issue, so there's nothing I can do about it, it's an issue with BYOND".

Until it struck me.

"What if we used a mask that would cut out the parts of the right leg, from the left leg, so that it doesn't actually look as if it's above it?"

Here I am, after about 25 hours of work, 15 of which of very painful debugging due to BYOND's icon documentation sucking ass.

So, how does it work?

Basically, we create a mask of a left leg (that'll be explained later down the line), more specifically, a cutout of JUST the WEST dir of the left leg, with every other dir being just white squares. We then cache that mask in a static list on the right leg, so we don't generate it every single time, as that can be expensive. All that happens in update_body_parts(), where I've made it so legs are handled separately, to avoid having to generate limb icons twice in a row, due to it being expensive. In that, when we generate_limb_icon() a right leg, we apply the proper left leg mask if necessary.

Now, why masking the right leg, if the issue was the left leg?
Because, see, when you actually amputated someone, and gave them a leg again, it would end up being that new leg that would be displayed below the other leg. So I fixed that, by making it so that bodyparts would be sorted correctly, before the end of update_body_parts(). Which means that right legs ended up displaying above left legs, which meant that I had to change everything I had written to work on right legs rather than left legs.

I spent so much time looking up BYOND documentation for MapColors() and filters and all icon and image vars and procs, I decided to make a helper proc called generate_icon_alpha_mask(), because honestly it would've saved me at least half a day of pure code debugging if I had it before working on this refactor.

I tried to put as much documentation down as I could, because this shit messes with your brain if you spend too long looking at it. icon and image are two truly awful classes to work with, and I don't look forward to messing with them more in the future.

Anyway. It's nice, because it requires no other effort from anyone, no matter what the shape of the leg is actually like. It's all handled dynamically, and only one per type of leg, meaning that it's not actually too expensive either, which is very nice. Especially since it's very downstreams-friendly from being done this way.


It fixes #20603 (Bodypart sprites render with incorrect layering), an issue that has been around for over half a decade, as well as probably many more issues that I just didn't bother sifting through.

Plus, it just looks so much better.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[61d0c14dc8...](https://github.com/mrakgr/The-Spiral-Language/commit/61d0c14dc898689424f1035db7da15122c126e1c)
#### Wednesday 2022-06-15 17:23:09 by Marko Grdinić

"5:05pm. It has been a long time since I've experienced this kind of suffering. Let me watch the Cityscene and the kitbashing videos. There I am going to watch some chara modeling videos. I've decided - I am going to throw away my skill at that. If posisble I should use existing addons and modify them lightly. Sculpting personally should not be my first choice, just like modeling shouldn't.

Houdini mislead me. It is not like the Labs node has no value, but it put me in a completely wrong mindset. If I want to make a good looking city, importing the flat OSM data and starting from there is not the way to go. The real start would be to get a photograph of the place I want to model. Then kitbash it. That is how I'd image anime background illustrators would do it.

It is a child's technique, but it is devastatingly effective.

Having the right mindset sounds easy, but it is actually very hard. I knew that I was embarassing myself during the last few days, but I could not help it.

I am going to do it. I am going to master kitbashing, and then I am going to master whatever the equivalent of that if for character models.

5:10pm. Houdini's building generator node is good, but it is not like arraying a bunch of windows would be hard even in Blender. I'd have to put in a bit extra effort to do all 4 corners, but it would be fine.

Remember that wine scene. I took so much effort to make the flowers unique, but if I had gone small to big, it would have been a lot easier and I would not have noticed much a difference. I made the choice to push my limit and 2 months went by as a result.

I do not really need Houdini. Nobody is going to admire my skills. What they will is admire the end results of my work.

Now focus me. Cityscene videos.

https://youtu.be/FdDLlm4c5YQ
SceneCity 1.9 Blender Addon Review

https://youtu.be/FdDLlm4c5YQ?t=60

Oh wow, this more fancy than I thought it would be.

https://youtu.be/FdDLlm4c5YQ?t=93

This really does look nice. Those particles are vegetation.

https://youtu.be/FdDLlm4c5YQ?t=102

This is worth getting excited about.

https://youtu.be/FdDLlm4c5YQ?t=157
> Dynamic skies which is a free sky addon.

5:20pm. I need to focus a bit on this. Just what is he doing to change the vegetation?

https://youtu.be/FdDLlm4c5YQ?t=145

Scatter addon. What is he doing with that addon?

He changed the material it seems.

https://youtu.be/FdDLlm4c5YQ?t=210

This is a lot more advanced than I thought it would be. Yeah, it is worth getting excited for this. It is not just about cities.

He mentions he will have other tutorials on Scenecity

https://youtu.be/kJ1MQCBHuW8
Citybuilder 3D Blender Addon

I can't find anything more recent by him on SceneCity, but he did mention this addon.

Hmmm, what is this Metahuman thing? I'll check it out at some point, let me watch the above video first.

It seems Citybuilder 3D is like an asset pack. I'll keep it in mind. Right about this time, I should get familiar with Blender asset system. I have no idea how it happened, but in my past Blender projects I ended up with them being strewn about everywhere. I am going to have to put some thought into organizing them.

https://youtu.be/serjEGO1mlw
Create Your Own City Within 2Min || Scene-city |Blender Tutorial

Let me watch this next. ...It was a bit shitty.

https://www.youtube.com/user/PiiichanPictures/videos

I think this guy is the author of Scenecity.

https://youtu.be/1IgaoXaaMy4
blender 2.82-Addon Scene City Tutorial 01

Let me just watch this. I can't find anything longer than 5m other than this.

The video seems to be in either Chinese or Korean, I can't tell. But it has subtitles.

5:55pm. I can't follow this. Half the time the subtitled aren't even tracking the video.

5:55pm. https://youtu.be/VORsNaExhn8
🔴Blender - Lets make a Floating City

I am not sure I want to watch this, but I'll keep it in mind.

https://scenecitydoc.cgchan.com/

Houdini is worth giving up for this. Nevermind the docs being sparse. I'll figure it out as I play along.

6pm. https://youtu.be/rulrjt25ZQk
Blender: Everything About KitBashing (In 5 Minutes!)

Royal Skies. I probably watched this video last year. Let me do it again.

https://youtu.be/rulrjt25ZQk?t=40
> For 8$ you could buy this. 8$ is how much you'd make working at McDonalds for an hour. And I promise you it would take you a lot longer to make all this from scratch.

I should check out Artstation at some point.

https://youtu.be/rulrjt25ZQk?t=54

Oh, wow, this one is something I want for after the Earth gets blasted.

https://cgpersia.com/2019/11/kitbash3d-aftermath-165039.html

Here it is on Persia. It is close to 8gb. If I am going to be downloading these things, it will be time to start thinking about getting a RapidGator or AlphaFile account. They are all 15$ a month. This would be way cheapter than paying the full price for the kit.

https://youtu.be/rulrjt25ZQk?t=94
> This is an excellent way to make breathtaking scenes even if your modeling sucks total ass.

https://youtu.be/rulrjt25ZQk?t=152

This juggles my memory a bit. This guy is good. He seems bombastic, but gives good advice. I didn't think I'd gain much from watching this video, but I have. Let me finish it.

https://www.youtube.com/playlist?list=PL3QJ5EUZG_SHErrGfSrIkOtLCAC8yQ_xH
Kitbash 3d - Industry Pro Series

There are a bunch of short vids here.

https://youtu.be/IOFBk9Clh0g?list=PL3QJ5EUZG_SHErrGfSrIkOtLCAC8yQ_xH&t=78

This is a good end-of-the world kind of shot.

https://youtu.be/RYS-pLfRGwM?list=PL3QJ5EUZG_SHErrGfSrIkOtLCAC8yQ_xH&t=87
> For our industry what is exciting when I think of the future is that tools are coming that I can't even imagine that are gonna be so much fun to use.

https://youtu.be/fKC11ESSQWg?list=PL3QJ5EUZG_SHErrGfSrIkOtLCAC8yQ_xH&t=78

This guy is pretty good.

6:35pm. https://youtu.be/g89X33yfWww?list=PL3QJ5EUZG_SHErrGfSrIkOtLCAC8yQ_xH&t=101

I wonder what program he is using here.

6:40pm. https://youtu.be/89FEqJh8rV8
How to kitbash like a pro in Blender!

I'll leave this for tomorrow. I've been tired the whole day today and I am much more stressed than I should be.

My sleep was worse than I thought.

6:45pm. It does not matter. I am going to grasp this. Kitbashing like this is how I should have started out, but I am the type of person to study the low level way first. Now it is time for me to master the high level. It did give me some time to think about how exactly I want to deal with the city lighting. I want it to match what I've done in the cover somewhat. It won't make sense unless there is a golden glow everywhere. I thought of ways of doing it.

Tomorrow, I am going to completely go into the Kitbashing midset. Also I'll take a look at the Scatter adddon. Yes, I spent 2 months in Houdini just for that, but who cares about it. Maybe scattering is better in Blender and I just overlooked it. There is more to Blender than geo nodes. I have only myself to blame for considering addons last.

6:50pm. https://youtu.be/UnLwnyY06Mw
Scatter 5 for Blender IS HERE! What's New?

Let me watch this now and then I will close.

https://youtu.be/UnLwnyY06Mw?t=150

This seems to have a fair bit of functionality.

As I suspected, this would be easier to use than geo nodes.

https://cgpersia.com/2022/01/blendermarket-scatter-5-0-182241.html

Let me get this. It has 5 parts of 250mb. So it has some size.

7pm. Sigh, part 1 is missing on Gator. it only informed me of that after I'd completed the capcha. Let me try part 4 in Gator.

Oghhhh...

Well, it is not a vital addon for me by any means. AlfaFile and NitroFlare will do the job eventually.

https://youtu.be/UnLwnyY06Mw?t=368

These scatter capabilities attracted me to Clarisse, but Clarisse is a annoying to use as it crashes constantly.

https://youtu.be/UnLwnyY06Mw?t=392
> There is quite possibly the best documentation that I've seen for a Blender addon.

https://youtu.be/UnLwnyY06Mw?t=420

This is cool.

https://youtu.be/UnLwnyY06Mw?t=486

Yeah, rather than spending time on Clarisse, it might have been better to study this instead. This is the consequence of my choices.

https://youtu.be/gQwf2xZxowQ
A Powerful Combination | Scatter 5 and Graswald | Blender Intermediate Tutorial

What is Graswald?

https://www.graswald3d.com/?ref=jaredtimme

Vegetation asset library.

7:20pm. Ok, at some point I am going to pay 15$ a month for a RapidGator account and go on a downloading spree.I I'll grab everything that is not nailed down at that time. Not just yet.

Let me close here. Tomorrow I am going to play around with SceneCity as well as download the rest of the Scatter addon.

Hopefully I'll get some good sleep tonight."

---
## [nirzaf/Algorithm_A_Day](https://github.com/nirzaf/Algorithm_A_Day)@[2aae3cb0b5...](https://github.com/nirzaf/Algorithm_A_Day/commit/2aae3cb0b53b63bbcb5f6b13fe9874bb66ae1e96)
#### Wednesday 2022-06-15 17:56:49 by nirzaf

am a Senior Full-Stack Engineer. Mainly developing backend web API and integrating with UI frameworks such as
WPF & Angular. .NET is my favourite backend development platform in terms of developing business logic & database
integrations. Currently, I take part in developing Microservices based on event-driven programming using Azure
Service Bus and RabbitMQ,
My strongest skills are
 C# is my favourite .NET language. Since it is evolving faster, I like to stick with it (12+ years)
 Microsoft SQL server has been my primary database solution for most of the projects (8+ years)
 ASP.NET/Core is my ultimate tech stack in all projects when it comes to API development (6+ Years)
 Angular is my go-to UI framework for SPA and enterprise-level Web UI (3+ years)
 Database Designing in Entity Framework (5+ Years)
 Continuous Development and Continuous Integration using Azure DevOps, Gitlab CI-CD pipelines, GitHub
Actions
 Handling Version Controlling Systems using GitHub, Gitlab, Bit Bucket (6+ Years)
 Project Management tools such as Azure Boards, Jira, Monday.com, ClickUps (3+ years)
 Azure Durable Functions, Azure Service Bus, Logic Apps (2+ Years)
 Currently Learning (Mass Transit, Rabbit MQ, Docker, Kubernetes, SAGA)
I am looking for Full-Stack (.NET, Angular) or Backend(.NET) Engineer role; prefer a small-sized team where I can
collaborate closer. A good culture is one in which team members collaborate, share knowledge, communicate, and
support one another. When people feel supported and know that someone has their back, they can do amazing
things.
I have contributed to some open-source projects to improve the application by creating issues when I found bugs. I
share my knowledge through my blogging site with my community. I am conducting workshops and training sessions
for university students to train them on current industrial technical demands and guide them and supervise new
interns of the company.
My professional experience & constant passion for learning has provided me with the innovative and technical skills
necessary for a medium to a large organization with multifaceted technical solutions across a wide range of software
platforms. I was instrumental in structuring several internal systems comprising order entry/management tools,
conversion/revenue reporting, and production workflow tracking in my current position. Successfully collaborated
on solutions with our product management, quality assurance, and marketing teams to offer the best user experience
to build higher customer lifetime value.
Please explore my portfolio collection on my website and blog links. My long journey has been accumulated lots of
projects which cannot be listed all here, so please check out the complete list of my projects on GitHub and GitLab
https://nirzaf.github.io
https://www.dotnetevangelist.net
I am glad that you spent a moment of your precious time to know a bit further about me. Suppose you think I would
be a good fit for your requirements. In that case, I am happy to provide further insight into my knowledge of technical
abilities, personal attributes, and track record of success in building revenue-generating technologies compatible
across multiple platforms.
It would be a pleasure to learn more about your requirements and working culture. I believe in better working culture
will bring out the best in me. Thank you for considering my candidacy for this position. I hope to hear from you soon
to schedule a discussion to work together toward a common goal.
Warm Regards,
FM Fazrin,

---
## [wael444/dwm](https://github.com/wael444/dwm)@[ebbae5b04e...](https://github.com/wael444/dwm/commit/ebbae5b04e96b831abc152eea03eb37d8c5529e9)
#### Wednesday 2022-06-15 20:40:33 by wael

god fucking damn it config.def.h & README why are you here

---
## [raidenlunari/raidenlunari.github.io](https://github.com/raidenlunari/raidenlunari.github.io)@[70b0301e2c...](https://github.com/raidenlunari/raidenlunari.github.io/commit/70b0301e2c6659f2f7f96ce4771984e93ddbdbcd)
#### Wednesday 2022-06-15 22:14:54 by raidenlunari

again trying to fix this factory thing i hate my life

---

