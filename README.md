## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-07-07](docs/good-messages/2022/2022-07-07.md)


1,573,838 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,573,838 were push events containing 2,329,653 commit messages that amount to 172,005,876 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 36 messages:


## [ForestCranked/Shiptestengimaruin](https://github.com/ForestCranked/Shiptestengimaruin)@[f421be47a9...](https://github.com/ForestCranked/Shiptestengimaruin/commit/f421be47a95fc04e78b3d48601508222dd84ee4d)
#### Thursday 2022-07-07 00:00:06 by Recoherent

Adds five new IPC antennae (#1279)

* adds 5 new ipc antennae

feeling kinda hopeless idk

* nyaru horns thicker

this is the part where i yell at royal for replying with something dumb

* removes lights it doesn't even fucking exist

what were they thinking?????????????????????

* forgot to remove joke name

oooooooooooooooooops, the joke will have to live in our hearts

---
## [mc-oofert/tgstation](https://github.com/mc-oofert/tgstation)@[95ffcd4e19...](https://github.com/mc-oofert/tgstation/commit/95ffcd4e19304af76653ff2b33084092246e4b16)
#### Thursday 2022-07-07 00:47:40 by YakumoChen

Moves the FUCKING LIGHT FIXTURES on tiles with surgery beds (#67644)

Moves around some wall objects in surgery rooms on both Meta and Box, primarily so that there aren't light fixtures on the same tiles as surgery beds. I moved a few unrelated things for QOL.

EVERY MOTHER FUCKING TIME I DO SURGERY I ALWAYS SMASH THE FUCKING LIGHT TUBE BY ACCIDENT AND IT PISSES ME THE FUCK OFF. WHY WOULD YOU PUT A THING THERE THAT JUTS OUT OVER THE FUCKING BED AND GETS IN THE WAY OF CLICKING ON THE SPACEMAN SPRITE FUCK GOD DAMN IT.

---
## [CursedBirb/tgstation](https://github.com/CursedBirb/tgstation)@[763a10d1cc...](https://github.com/CursedBirb/tgstation/commit/763a10d1cc44c91720101d422d8709ad1aa0644d)
#### Thursday 2022-07-07 01:12:12 by distributivgesetz

Resonance cascade polishening, bugfixes and better logging (#67488)

This PR rewrites almost all messages related to cascade events. Some messages felt kinda clunky to read or could have been written better. Overall, the new messages add to the experience as a cascade being a terrifying event in a way that I felt the old ones missed, and they make the event feel overall a lot sharper.

While looking at the resonance cascade code, I noticed that there a lot of stuff about cascades in the air which was not touched on. So, as I do, this PR evolved into a polish and roundup PR for cascades. There was a lot of stuff still hanging out relating to the event, and although the big backend of it sits, there was still a bit left to be completed. Therefore this PR deserves more the title of the "Resonance cascade POLISHENING" instead of the "REFLAVAHRING". But yeah, you ever go on a massive tangent before?

---
## [Neaxic/ENS-LinkUS](https://github.com/Neaxic/ENS-LinkUS)@[a4f6ca0a54...](https://github.com/Neaxic/ENS-LinkUS/commit/a4f6ca0a5498542421c458defe7046cb31f84c70)
#### Thursday 2022-07-07 01:27:50 by Andre

file uploader, og så fucking meget lort jeg ikke mager skrive men holy shit der meget

---
## [Wrapper-Offline/informational-website](https://github.com/Wrapper-Offline/informational-website)@[a4b981f60d...](https://github.com/Wrapper-Offline/informational-website/commit/a4b981f60d46cfd9581c9e661656d396747f31cf)
#### Thursday 2022-07-07 01:45:47 by sparrkz

silent git install (note to self, do research)

also gave information onto why the hell the launcher closes after dependency install (not very user friendly)

---
## [DayangAB/terminal](https://github.com/DayangAB/terminal)@[9ccd6ecd74...](https://github.com/DayangAB/terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Thursday 2022-07-07 02:50:15 by Mike Griese

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
## [DayangAB/terminal](https://github.com/DayangAB/terminal)@[8962f88f90...](https://github.com/DayangAB/terminal/commit/8962f88f907d86fd8684b66f7f3e32a2709e3237)
#### Thursday 2022-07-07 02:50:15 by Dustin L. Howett

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
## [Dark-Matter7232/CosmicFresh-Hanoip](https://github.com/Dark-Matter7232/CosmicFresh-Hanoip)@[79116d2d8a...](https://github.com/Dark-Matter7232/CosmicFresh-Hanoip/commit/79116d2d8adf7365f67521fb3ac45fa8810a2723)
#### Thursday 2022-07-07 02:54:51 by Zi Yan

BACKPORT: mm/compaction: stop isolation if too many pages are isolated and we have pages to migrate

In isolate_migratepages_block, if we have too many isolated pages and
nr_migratepages is not zero, we should try to migrate what we have
without wasting time on isolating.

In theory it's possible that multiple parallel compactions will cause
too_many_isolated() to become true even if each has isolated less than
COMPACT_CLUSTER_MAX, and loop forever in the while loop.  Bailing
immediately prevents that.

[vbabka@suse.cz: changelog addition]

Fixes: 1da2f328fa64 (“mm,thp,compaction,cma: allow THP migration for CMA allocations”)
Suggested-by: Vlastimil Babka <vbabka@suse.cz>
Signed-off-by: Zi Yan <ziy@nvidia.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Cc: <stable@vger.kernel.org>
Cc: Mel Gorman <mgorman@techsingularity.net>
Cc: Michal Hocko <mhocko@kernel.org>
Cc: Rik van Riel <riel@surriel.com>
Cc: Yang Shi <shy828301@gmail.com>
Link: https://lkml.kernel.org/r/20201030183809.3616803-2-zi.yan@sent.com
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
[cyberknight777: backport to 4.14]
Signed-off-by: Cyber Knight <cyberknight755@gmail.com>

---
## [Y0SH1M4S73R/tgstation](https://github.com/Y0SH1M4S73R/tgstation)@[8f0df7816b...](https://github.com/Y0SH1M4S73R/tgstation/commit/8f0df7816bae3c5dedf599611cda3e6039024e14)
#### Thursday 2022-07-07 03:20:59 by Kylerace

(code bounty) The tram is now unstoppably powerful. it cannot be stopped, it cannot be slowed, it cannot be reasoned with. YOU HAVE NO IDEA HOW READY YOU ARE (#66657)

ever see the tram take 10 milliseconds per movement to move 2100 objects? now you have
https://user-images.githubusercontent.com/15794172/166198184-8bab93bd-f584-4269-9ed1-6aee746f8f3c.mp4
About The Pull Request

fixes #66887

done for the code bounty posted by @MMMiracles to optimize the tram so that it can be sped up. the tram is now twice as fast, firing every tick instead of every 2 ticks. and is now around 10x cheaper to move. also adds support for multiz trams, as in trams that span multiple z levels.

the tram on master takes around 10-15 milliseconds per movement with nothing on it other than its starting contents. why is this? because the tram is the canary in the coal mines when it comes to movement code, which is normally expensive as fuck. the tram does way more work than it needs to, and even finds new ways to slow the game down. I'll walk you through a few of the dumber things the tram currently does and how i fixed them.

    the tram, at absolute minimum, has to move 55 separate industrial_lift platforms once per movement. this means that the tram has to unregister its entered/exited signals 55 times when "the tram" as a singular object is only entering 5 new turfs and exiting 5 old turfs every movement, this means that each of the 55 platforms calculates their own destination turfs and checks their contents every movement. The biggest single optimization in this pr was that I made the tram into a single 5x11 multitile object and made it only do entering/exiting checks on the 5 new and 5 old turfs in each movement.
    way too many of the default tram contents are expensive to move for something that has to move a lot. fun fact, did you know that the walls on the tram have opacity? do you know what opacity does for movables? it makes them recalculate static lighting every time they move. did you know that the tram, this entire time, was taking JUST as much time spamming SSlighting updates as it was spending time in SStramprocess? well it is! now it doesnt do that, the walls are transparent. also, every window and every grille on the tram had the atmos_sensitive element applied to them which then added connect_loc to them, causing them to update signals every movement. that is also dumb and i got rid of that with snowflake overrides. Now we must take care to not add things that sneakily register to Moved() or the moved signal to the roundstart tram, because that is dumb, and the relative utility of simulating objects that should normally shatter due to heat and conduct heat from the atmosphere is far less than the cost of moving them, for this one object.
    all tram contents physically Entered() and Exited() their destination and old turfs every movement, even though because they are on a tram they literally do not interact with the turf, the tram does. also, any objects that use connect_loc or connect_loc behalf that are on the same point on the tram also interact with each other because of this. now all contents of the tram act as if theyre being abstract_move()'d to their destination so that (almost) nothing thats in the destination turf or the exit turf can react to the event of "something laying on the tram is moving over you". the rare things that DO need to know what is physically entering or exiting their turf regardless of whether theyre interacting with the ground can register to the abstract entered and exited signals which are now always sent.
    many of the things hooked into Moved(), whether it be overrides of Moved() itself, or handlers for the moved signal, add up to a LOT of processing time. especially for humans. now ive gotten rid of a lot of it, mostly for the tram but also for normal movement. i made footsteps (a significant portion of human movement cost) not do any work if the human themselves didnt do the movement. i optimized has_gravity() a fair amount, and then realized that since everything on the tram isnt changing momentum, i didnt actually need to check gravity for the purposes of drifting (newtonian_move() was taking a significant portion of the cost of movement at some points along the development process). so now it simply doesnt call newtonian_move() for movements that dont represent a change in momentum (by default all movements do).

also i put effort into 1. better organizing tram/lift code so that most of it is inside of a dedicated modules folder instead of scattered around 5 generic folders and 2. moved a lot of behavior from lift platforms themselves into their lift_master_datum since ideally the platforms would just handle moving themselves, while any behavior involving the entire lift such as "move to destination" and "blow up" would be handled by the lift_master_datum.

also
https://user-images.githubusercontent.com/15794172/166220129-ff2ea344-442f-4e3e-94f0-ec58ab438563.mp4
multiz tram (this just adds the capability to map it like this, no tram does this)
Actual Performance Differences

to benchmark this, i added a world.Profile(PROFILER_START) and world.Profile(PROFILER_START) to the tram moving, so that it generates a profiler output of all tram movement without any unrelated procs being recorded (except for world.Profile() overhead). this made it a lot easier to quantify what was slowing down both the tram and movement in general. and i did 3 types of tests on both master and my branch.

also i should note that i sped up the "master" tram test to move once per tick as well, simply because the normal movement speed seems unbearably slow now. so all recorded videos are done at twice the speed of the real tram on master. this doesnt affect the main thing i was trying to measure: cost for each movement.

the first test was the base tram, containing only my player mob and the movables starting on the tram roundstart. on master, this takes around 13 milliseconds or so on my computer (which is pretty close to what it takes on the servers), on this branch, it takes between 0.9-1.3 milliseconds.

ALSO in these benchmarks youll see that tram/proc/travel() will vary significantly between the master and optimized branches. this is 100% because there are 55 times more platforms moving on master compared to the master branch, and thus 55x more calls to this proc. every test was recorded with the exact same amount of distance moved

here are the master and optimized benchmark text files:
master
master base tram.txt
https://user-images.githubusercontent.com/15794172/166210149-f118683d-6f6d-4dfb-b9e4-14f17b26aad8.mp4
also this shows the increased SSlighting usage resulting from the tram on master spamming updates, which doesnt happen on the optimized branch

optimized
optimization base tram.txt
https://user-images.githubusercontent.com/15794172/166206280-cd849aaa-ed3b-4e2f-b741-b8a5726091a9.mp4

the second test is meant to benchmark the best case scaling cost of moving objects, where nothing extra is registered to movement besides the bare minimum stuff on the /atom/movable level. Each of the open tiles of the tram had 1 bluespace rped filled with parts dumped onto it, to the point that the tram in total was moving 2100 objects. the vast majority of these objects did nothing special in movement so they serve as a good base case. only slightly off due to the rped's registering to movement.

on master, this test takes over 100 milliseconds per movement
master 2000 obj's.txt
https://user-images.githubusercontent.com/15794172/166210560-f4de620d-7dc6-4dbd-8b61-4a48149af707.mp4

when optimized, about 10 milliseconds per movement
https://user-images.githubusercontent.com/15794172/166208654-bc10086b-bbfc-49fa-9987-d7558109cc1d.mp4
optimization 2000 obj's.txt

the third test is 300 humans spawned onto the tram, meant to test all the shit added on to movement cost for humans/carbons. in retrospect this test is actually way too biased in favor of my optimizations since the humans are all in only 3 tiles, so all 100 humans on a tile are reacting to the other 99 humans movements, which wouldnt be as bad if they were distributed across 20 tiles like in the second test. so dont read into this one too hard.

on master, this test takes 200 milliseconds
master 300 catgirls.txt

when optimized, this takes about 13-14 milliseconds.
optimization 300 catgirls on ram ranch.txt
Why It's Good For The Game

the tram is literally 10x cheaper to move. and the code is better organized.
currently on master the tram is as fast as running speed, meaning it has no real relative utility compared to just running the tracks (except for the added safety of not having to risk being ran over by the tram). now the tram of which we have an entire map based around can be used to its full potential.

also, has some fixes to things on the tram reacting to movement. for example on master if you are standing on a tram tile that contains a banana and the TRAM moves, you will slip if the banana was in that spot before you (not if you were there first however). this is because the banana has no concept of relative movement, you and it are in the same reference frame but the banana, which failed highschool physics, believes you to have moved onto it and thus subjected you to the humiliation of an unjust slipping. now since tram contents that dont register to abstract entered/exited cannot know about other tram contents on the same tile during a movement, this cannot happen.

also, you no longer make footstep sounds when the tram moves you over a floor
TODO

mainly opened it now so i can create a stopping point and attend to my other now staling prs, we're at a state of functionality far enough to start testmerging it anyways.

add a better way for admins to be notified of the tram overloading the server if someone purposefully stuffs it with as much shit as they can, and for admins to clear said shit.
automatically slow down the tram if SStramprocess takes over like, 10 milliseconds complete. the tram still cant really check tick and yield without introducing logic holes, so making sure it doesnt take half of the tick every tick is important
go over my code to catch dumb shit i forgot about, there always is for these kinds of refactors because im very messy
remove the area based forced_gravity optimization its not worth figuring out why it doesnt work
fix the inevitable merge conflict with master lol
create an icon for the tram_tunnel area type i made so that objects on the tram dont have to enter and exit areas twice in a cross-station traversal

    add an easy way to vv tram lethality for mobs/things being hit by it. its an easy target in another thing i already wanted to do: a reinforced concept of shared variables from any particular tram platform and the entire tram itself. admins should be able to slow down the tram by vv'ing one platform and have it apply to the entire tram for example.

Changelog

cl
balance: the tram is now twice as fast, pray it doesnt get any faster (it cant without raising world fps)
performance: the tram is now about 10 times cheaper to move for the server
add: mappers can now create trams with multiple z levels
code: industrial_lift's now have more of their behavior pertaining to "the entire lift" being handled by their lift_master_datum as opposed to belonging to a random platform on the lift.
/cl

---
## [nicerapp/nicerapp](https://github.com/nicerapp/nicerapp)@[8691712be2...](https://github.com/nicerapp/nicerapp/commit/8691712be2c703377a60468124c45ae7dde159a0)
#### Thursday 2022-07-07 04:00:50 by Rene AJM Veerman

IMPORTANT UPDATE : READ WHOLE COMMENT FOR THIS UPLOAD TO GITHUB.COM : Like in war, in the businessworld you need to pick your allies in a smart way, and stay brand-loyal and Especially Allies-Loyal, and practice the art of DIPLOMACY in your actions and words and body-language towards your AUDIENCES *AND* your Allied-companies. I am a small industrial startup man, and i've chosen (*by myself*) the allies Linux, Microsoft.com, GOOGLE.com (gmail.com is their entrypoint in terms of oAuth root-most level checks in terms of user-interfaces), tinyurl.com, Facebook.com (in effect all of Meta.com these days), is.gd (another dot-com level site for link shortening) (see my is.gd/cheetahkungfu for instance, and eh, evil people, you will call yourselves Black Panther Kung Fu Students please, or there'll be a price to pay in terms of wars that you can't handle, with all those majorities of Good Warriors (dead/alive/Divine) out there, see my https://tinyurl.com/telepathy-manual), and of course Apple.com for the quality of their hardware (girls and women LOVE that hardware, richer guys too! - so i'll be building an extension for jQuery.com that fixes jQuery.com for Apple products *myself*)

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[f6cc7f575c...](https://github.com/cockroachdb/cockroach/commit/f6cc7f575cd374982752af6909d3efa96908c3dd)
#### Thursday 2022-07-07 04:04:29 by craig[bot]

Merge #81409

81409: bazel: upgrade to rules_nodejs 5.4.2 r=rickystewart,nathanstilwell,laurenbarker a=sjbarag

Please forgive the massive second commit — there's very few valid states in this progression, as building, linting, and testing either work or they don't.  There's not much sense in intentionally leaving commits around that won't build in my opinion, as it makes bisecting extremely frustrating.  If anyone disagrees, let me know and I can keep digging for an intermediate state!

----

Upgrading to Bazel's rules_nodejs 5.x exposed a flaw in our previous Bazel integration: because rules_nodejs explicitly doesn't support yarn's "workspaces" feature [1] (in which common dependencies are hoisted to the lowest common parent directory), any NPM dependencies with different major versions between db-console and cluster-ui would
get flattened to a single version. This left one of those packages using an unsupported (and un-requested) version of a dependency. Removing the yarn workspace layout and using separate Bazel repositories for each JS project ensured each project received the correct dependencies, but revealed incompatibilities with the requested versions. Upgrade rules_nodejs to the latest released version, remove yarn workspaces from the pkg/ui/ tree, and fix all revealed compatibility issues.

Co-authored-by: Sean Barag <barag@cockroachlabs.com>

---
## [njlyf2011/reactos-dev](https://github.com/njlyf2011/reactos-dev)@[4471ee4dfa...](https://github.com/njlyf2011/reactos-dev/commit/4471ee4dfaddb2440601fd61c01542b586b7c2d0)
#### Thursday 2022-07-07 04:07:07 by George Bișoc

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
## [flolac-tw/hakyll](https://github.com/flolac-tw/hakyll)@[8980133284...](https://github.com/flolac-tw/hakyll/commit/8980133284d7d5f0d7cd71580796150c74b22f2d)
#### Thursday 2022-07-07 06:37:39 by Alexander Batischev

Docs: IRC channel moved from Freenode to Libera.Chat (#848)

There's no mention of this on the issue tracker, so here's my recap of
what led to this change.

There is some drama around Freenode. Their volunteer staff quit[1]. Then
the new-ish management started enacting strange policy changes[2] and
take over the channels[3]. On June 26th 2021 Freenode's bot tried to
take over #hakyll, but failed; however, it did succeed in #haskell and
many, many other channels.

For the preceding week, me and IRC user henk were trying to move the
channel off the Freenode, either to Libera.Chat or OFTC. Jasper, the
founder of Hakyll, was absent from IRC and didn't respond to my emails.
Me and henk are the most active IRC users on the channel. Also, I have
Collaborator access to the repo, and henk has chanop access to the IRC
channel. We believe that at this time, we're the ones who are the best
positioned to execute the move, so we're doing it.

We only considered Libera.Chat and OFTC. Libera.Chat was created a week
earlier by the same staff who quit Freenode; I personally consider them
to be a spiritual successor of Freenode. OFTC is a well-established
network with good governance documentation. Both networks are
FOSS-friendly. The choice wasn't obvious.

Libera.Chat was picked because 10 users moved there (and 1 more did
while I was typing this!), whereas only 2 joined OFTC (me and henk, and
those weren't votes for OFTC — we were just ensuring that the channel is
ours). Also, #haskell and #ghc are on Libera too, so it makes sense for
a Haskell project such as Hakyll to be present on Libera.

For posterity:

<Minoru> info #hakyll
-ChanServ(ChanServ@services.)- Information on #hakyll:
-ChanServ(ChanServ@services.)- Founder    : jaspervdj
-ChanServ(ChanServ@services.)- Registered : Mar 01 13:29:17 2011 (10y 12w 5d ago)
-ChanServ(ChanServ@services.)- Mode lock  : +ntc-slk
-ChanServ(ChanServ@services.)- *** End of Info ***

1. https://kline.sh
2. https://github.com/freenode/web-7.0/pull/513
3. https://www.devever.net/~hl/freenode_abuse

---
## [C7-Game/Prototype](https://github.com/C7-Game/Prototype)@[d4cb71a167...](https://github.com/C7-Game/Prototype/commit/d4cb71a1673b919ddf87d8afcbb2e8ad9ad25352)
#### Thursday 2022-07-07 07:05:39 by Quintillus

WIKI INFO - Build out strategic priorities a little bit.  WarPriority is a notable one as it is the first one that includes properties.

I've tried to build the priorities so there will be a common interface.  The goal being that new priorities can be added being mods, and they can still be serialized.  The interface should help for this.  If all of our StrategicPriorities were bespoke hard-coded, it might be convenient, but it would not lend itself to extensibility.

The challenge is going to be how do we merge those priorities, convenience of writing the logic, extensibility, and serialization?

This is still an evolving thought process, and I'm not totally sold on this dictionary-of-dictionaries approach, it just seemed like the most convenient way to return a weight *and* some required data about how that weight was chosen and what to do if this priority is chosen by the arbitrator.

The other half of the thought process that's not yet fully coded is that if a priority is chosen, its info should be stored in the data classes.  My general thought here is that by returning property maps, we should be able to store those, and a reference to the type of StrategicPriority, in the data classes, allowing us to reconstruct objects of the appropriate type, put in the relevant properties, and re-load from save.

The engine will also have to be able to look up the priorities based on name... maybe a key type thing?  This should also be stored in the save.  So basically, on load the engine will have the key, the weight, and properties.  It'll use the key to find the appropriate class, instantiate an instance, and stuff the properties onto that instance (and maybe the weight or maybe that's higher-level metadata that goes elsewhere).  This yields an fully inflated StrategicPriority instance that the AI part of the engine can then reference to calculate things.

Combining this with a lookup mechanism for StrategicPriorities should yield moddability.  I'm reminded of Java's "Service Provider Interface" concept, the gist of which is that if you make a class that follows an interface, and register it with the JVM in a certain way in your program, the JVM magically gains new capabilities.  An example is if I write an image processor for PCX files, and register it correctly, the general image ImageIO capabilities in Java can now magically handle PCX files, e.g. ImageIO.load("x_title.pcx") will just work, even though in stock Java it wouldn't know what to do with a PCX.  It works for other types of services too.  Our specifics will differ, but I think the goal should be similar - if you write a new StrategicPriority and follow a given interface, it'll magically be incorporated with the AI.

The remaining hard part is how is the strategic AI looped in to decision-making?  There are theoretically a thousand places this could be looped in, but if we want it to be extensible, we have to have standard interfaces.  But the StrategicPriority also has to know enough about the situation to be able to interpret what's going on.

For now I'm thinking some combination of weights and modifiers being providable by the strategic priority.  E.g. for city production, it should be able to make some things be produced more often, and that's a weight based thing.  But I'm sure there's other cases I'm not thinking of that make things more complex.  I'm also aware of what Jon or Soren mentioned somewhere about overly generic AIs sometimes not being decisive enough.  It'll be interesting...

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[6fe0683a7b...](https://github.com/tgstation/tgstation/commit/6fe0683a7bc788a497dbce8771768e427d0dffb1)
#### Thursday 2022-07-07 07:16:27 by Jolly

[READY] [KC13] Showing "The Derelict" some love: General updates, aesthetic changes and misc (#67696)

With this PR I aim to make KC13 (TheDerelict.dmm), or Russian Station (whatever you guys call it) a tad bit more flavorful with its environment as well as somethings on the mapping side (like adding area icons!).
To preface, no, I'm not remapping anything here extensively. The general layout should be relatively the same (or should be in theory).

Halfway through naming the area icons I checked the wiki page and found out it was KC not KS, so, its KS13 internally.

Readability for turf icons are cool.
Also just making the ruin more eye appealing would be better.
General cleanup and changes will give new life to this rather.. loved? Hated? Loot pinata? Ruin.
The ruin also now starts completely depowered, like Old Station (its a Derelict, it makes no sense for it to still be powered after so long). As for some mild compensation, a few more batteries were sprinkled in to offset any issues. If there is any concern of "But they'll open the vault faster!", there were always 5 batteries that people used to make the vault SMES.
Lastly, giving it some "visual story telling" is cool, as mapping fluff goes.

I also added a subtle OOC hint that the SMES in the northern most solar room needs a terminal with the following:

SMES Jumpscare
As an aside, I aim to try and keep the feel of this ruin being "dated" while at the same time having some of our newer things. With that, certain things I'll opt out of using in favor of more "generic" structures to give KC13 that true "Its old but not really" feel and look.

---
## [Zeodexic/tsorcRevamp](https://github.com/Zeodexic/tsorcRevamp)@[303373dd7e...](https://github.com/Zeodexic/tsorcRevamp/commit/303373dd7eb77ace664d3904be7c202443a59cfa)
#### Thursday 2022-07-07 07:28:06 by MarfMaster

Changes again

Added few summoning items to non-consumable list
Removed some vanilla recipes to gate them behind map progress
Changed AtmaWeapon recipe
Allowed Frost Legion enemies to spawn so using the broken snow globe doesn't fuck your world up

---
## [Spookuni/tgstation](https://github.com/Spookuni/tgstation)@[e37591540b...](https://github.com/Spookuni/tgstation/commit/e37591540b2620b7ad2a2b61734634d848e8eba2)
#### Thursday 2022-07-07 07:46:29 by san7890

[MDB Ignore] OH GOD OH FUCK OH SHIT OH LORD - SPACE AND RUINS IS BROKEN (#67324)

So, for the last few days on production, Space Ruin generation has refused to work. Why is this? It's because in #67107 (cfc233052885dd294b2e7e676caaf84a2a37592b), we repathed `/area/space`  to `/area/misc/space` (lol i should have paid attention to that) without updating everything in code to match. I couldn't seem to get `/area/misc/space` to properly work somehow (this could have also been something I was doing wrong), but I worked it back to just making everything vanilla `/area/space` and all of those unwanted behaviors should be squashed out. Let's get the game working again.

---
## [ManorSailor/etch-a-sketch](https://github.com/ManorSailor/etch-a-sketch)@[10733462df...](https://github.com/ManorSailor/etch-a-sketch/commit/10733462df161b183921a43ed5118af9712a48a4)
#### Thursday 2022-07-07 09:03:50 by ManorSailor

feat: Add clear grid option

My implementation of tools section will require a rewrite if I want to extend this app one day.
Perhaps, a separate function which can take care of deciding if the activeTool should be updated or not
Since there will be some tools like 'clear grid' which doesn't do anything apart from...

Heck. My whole codebase will need a refactor, I created this activateTool function, however, this shit cannot be called from 'click' listener
of this tools above. If we do so, our implementation breaks since activateTool has mousemove events attached to it.

Holy cow, this code has become a huge mess.

---
## [Foundation-19/Foundation-19](https://github.com/Foundation-19/Foundation-19)@[c6468997ac...](https://github.com/Foundation-19/Foundation-19/commit/c6468997acb05639ea963e86606a805e241a7474)
#### Thursday 2022-07-07 09:26:41 by CerberusHellHound

Renaming, slight rebalance, etc (#179)

* Update baystation12.dme

* 9mm/.45ACP Buff

Changes are as follow:
- Buffed 9mm dam from 8 to 25 (now it doesn't take a whole mag to take down an unarmoured man)
- Buffed .45 dam from 10 to 30
- Nerfed 9mm AP from 34 to 30
- Buffed 7,62 dam from 40 to 50 (It's supposed to be beefier than 5,56mm)

* Organ changes

Lower organ health value to make combat much deadlier.
Headshots are truly lethal now.

* Slight rebalance and renamings

List of changes :
- decreased brain health to 150 (instead of 200), it's high enough that medical assistance can be given if fast but low enough that you don't want to get shot
- increased damage values of weapons to baystation/nebula level (40 for a pistol for eg)
- increased adrenalin generation when hurt (less fading in and out, you can still use your gun when hit and pain won't be such a pain in the ass, but you're less likely to get back up once the final shot hits you)
- decreased relative size of lungs from 60% to 30% so that now, getting hit in the chest won't have as much chance of damaging your poor fucking lungs (yes 60% is the original baystation number.. it makes sense, it's a large organ, but it's a pain in the ass)
- changed some names and descriptions of certain weapons and firearms to better fit established naming convention
-made revolvers cycle the barrel instead of eject each shot (it's a revolver, not a damn rifle)
- slightly decreased firing delay for the mk9 revolver (slightly weaker than the mateba so slightly faster firing)
- decreased firing delay for the mk9 pistol (lower caliber, less recoil, easier to magdump)

---
## [AndriyKatsubo/thewasteland](https://github.com/AndriyKatsubo/thewasteland)@[b052462833...](https://github.com/AndriyKatsubo/thewasteland/commit/b052462833fe607463547d4cdd670f1e48e9922c)
#### Thursday 2022-07-07 09:51:47 by BadAtThisGame

Overheat warnings to both gatling guns (#742)

* The notorious

* Epic

* FUCK YOU

* I am going to beat you with a club

---
## [Atom-X-Devs/android_kernel_xiaomi_scarlet](https://github.com/Atom-X-Devs/android_kernel_xiaomi_scarlet)@[dd1d90b47b...](https://github.com/Atom-X-Devs/android_kernel_xiaomi_scarlet/commit/dd1d90b47b58bbcdc0f5802b8e459601e13b9125)
#### Thursday 2022-07-07 09:52:47 by Wang Han

power: Introduce OnePlus 3 fingerprintd thaw hack

Taken from Oneplus 3, this hack will make fingerprintd recover from suspend quickly.

Small fixes for newer kernels since we're coming from 3.10.108..

Change-Id: I0166e82d51a07439d15b41dbc03d7e751bfa783b
Co-authored-by: Cyber Knight <cyberknight755@gmail.com>
[cyberknight777: forwardport and adapt to 4.14]
Co-authored-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>
[Tashar02: forwardport and adapt to 4.19 and xiaomi_sdm660's fp]
Signed-off-by: Shreyansh Lodha <slodha96@gmail.com>
Signed-off-by: Pierre2324 <pdbbasketball@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>
Signed-off-by: Dhruv <dhruvgera61@gmail.com>
Signed-off-by: Cyber Knight <cyberknight755@gmail.com>
Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>

---
## [hestiacp/hestiacp](https://github.com/hestiacp/hestiacp)@[365dab5670...](https://github.com/hestiacp/hestiacp/commit/365dab5670f6d1a862858be01638072eeb2ec1db)
#### Thursday 2022-07-07 10:59:57 by divinity76

Use secure RNG to generate passwords (#2726)

* use secure rng to generate passwords

quoting MDN:
>Math.random() does not provide cryptographically secure random numbers. Do not use them for anything related to security. Use the Web Crypto API instead

My rng is kinda shitty, i know there is some fast way to cut down higher digits to get a digit in range without introducing bias, but i also know that other people have introduced bias by trying to do that on an initially secure rng and getting it wrong (iirc it's discussed here? https://www.youtube.com/watch?v=LDPMpc-ENqY - been years since i saw the talk, but i know Lavavej discussed it in one of his presentations, i think it was that one)  , but anyway this is fast enough, and secure.

* shorter name

* randomString2 / centralize js string generation

* missed 2

---
## [jktjkt/oopt-gnpy](https://github.com/jktjkt/oopt-gnpy)@[5e3e331776...](https://github.com/jktjkt/oopt-gnpy/commit/5e3e33177648cf73c24c24fc09b98feec776fbfa)
#### Thursday 2022-07-07 12:06:06 by Jan Kundrát

YANG: Equipment Library

The first step in adding YANG description for GNPy's input is the
equipment library (`tip-photonic-equipment`). It contains data about all
defined EDFA and Fiber types. This is supposed to be functionally
equivalent to the `eqpt_config.json`, but the actual JSON structure is
different.

The core idea of this model is to describe capabilities of the
simulation engine as it exists, which means that the individual
choice/case statements mirror our different "simulation input
parameters". The user is not expected to do any augmentations of the
YANG model -- just describe the amplifiers, fiber, etc, with data. This
means that the user just *uses* the YANG model, which is unlike another
proposal that was floated around back in 2019 which used YANG-level
augmentations for the equipment library.

The pre-YANG code actually split stuff from `eqpt_config.json` into
additional JSON files for "fancy bits", such as the DGT LUT. That's
something that, IMHO, does not make sense when we're willing to ship
with machine-validation of the complete input set. So instead of
deferring to another JSON file for the NF-/gain-ripple/DGT, let's move
everything in-line into the input data. This has one obvious downside in
making the amplifier data a bit too verbose. There were several options:

- Ignore the human-friendliness and push everything into the amplifier
description. This is nice and self-contained, but the data are going to
be very, very long, and the majority of the WG was worried that it would
make human editing too difficult.

- Move everything to a side-loaded JSON file. This option separates out
some numerical parameters from the equipment library, and therefore
splits the configuration into two places. One of these places would be
exempt from the YANG validation, and loaded via unspecified means.
That's a no-go.

- Put stuff into a YANG model, but use one level of indirection between
the amplifier description and the numerical data.

This took us quite some time to decide, but ultimately on 2020-09-01 we
decided that the numbers that we have been shipping are *probably*
specific to a given EDFA model they were measured on. The actual *slope*
of the DGT looks very similar between, say, the Juniper/Lumentum
measurements and the data from Orange, but the multiplication factor is
different. So the outcome was that we will probably have to ship with
some sane default, *but* any measurements done by the user will apply
only to a specific amplifier model. The YANG model reflects that, and it
uses per-type lists. They are now indexed by frequency as agreed on the
2020-09-01 coders call.

In the real world, some "common fiber types" are well-defined by ITU,
such as the SSMF. Esther tried to model this via a set of identities and
YANG `identityref`s. I think that there's no disadvantage in shipping
these data as a default content of the YANG-formatted datastore,
similarly to how the equipment library used to be structured prior to
this patch. Once again, I'm following the pattern where the user can
change any *data* without augmenting the YANG model. The only reason for
editing/augmenting the (equipment) YANG model should be changes in our
simulation *engine*, such as when adding different input parameters for
NF calculations, or adding Raman amplification, etc.

The amplifier model has been reworked a bit. I've reduced the number of
available "simulation parameters" to a reasonable minimum as suggested
by Jean-Luc (cf. issue #227):

- a polynomial NF model
- a simplified model for operators with NF_min and NF_max
- a dual-stage amplifier comprising two individual sub-amplifiers that
  are each any of the above
- a faux-Raman
- three OpenROADM-specific models

In terms of correspondence to the previous code, the "polynomial NF" is
used for current `advanced_model` (which uses yet another external JSON
file) and the `fixed_gain` model. The simplified, min-max-NF is what
Jean-Luc called "operator model"; the wording is a compromise of various
suggestions done via GitHub. The OpenROADM models are, unfortunately,
magic, especially the preamp+booster simulation. But it reflects how
it's been implemented in GNPy.

The values which are stored in the YANG-formatted JSON files have
different units than what was stored in the legacy JSON files. We are
now using the "customary units", such as ps/km, instead of s/m. This is
largely a matter of taste, but the technical reason behind this is that
YANG only defines a decimal64 data type with a limited precision, and we
were running out of fraction-digits for certain parameters where the SI
representation is "too low" (the pmd-coefficient is one example).

Other "subtle" changes have been done as well, such as clarifying that
the amplifier's band boundaries refer to the edges of the passband and
not the central frequencies, etc.

Change-Id: I449d66e952834011b3ec476023c9cc353dfca5c0

---
## [SDArtsCode/blindsighted2](https://github.com/SDArtsCode/blindsighted2)@[a4faae73b3...](https://github.com/SDArtsCode/blindsighted2/commit/a4faae73b3605da033936343a12ff9acd200d418)
#### Thursday 2022-07-07 12:50:43 by quis345

According to all known laws of aviation, there is no way a bee should be
able to fly. Its wings are too small to get its fat little body off the
ground. The bee, of course, flies anyway because bees don't care what
humans think is impossible. Yellow, black. Yellow, black. Yellow, black.
Yellow, black. Ooh, black and yellow! Let's shake it up a little. Barry!
Breakfast is ready! Ooming! Hang on a second. Hello? - Barry? - Adam? -
Oan you believe this is happening? - I can't. I'll pick you up. Looking
sharp. Use the stairs. Your father paid good money for those. Sorry. I'm
excited. Here's the graduate. We're very proud of you, son. A perfect
report card, all B's. Very proud. Ma! I got a thing going here. - You
got lint on your fuzz. - Ow! That's me! - Wave to us! We'll be in row
118,000. - Bye! Barry, I told you, stop flying in the house! - Hey,
Adam. - Hey, Barry. - Is that fuzz gel? - A little. Special day,
graduation. Never thought I'd make it. They're out of their minds. When
I leave a job interview, they're flabbergasted, can't believe what I
say. There's the sun. Maybe that's a way out. I don't remember the sun
having a big 75 on it. I predicted global warming. I could feel it
getting hotter. At first I thought it was just me. Wait! Stop! Bee!
Stand back. These are winter boots. Wait! Don't kill him! You know I'm
allergic to them! This thing could kill me! Why does his life have less
value than yours? Why does his life have any less value than mine? Is
that your statement? I'm just saying all life has value. You don't know
what he's capable of feeling. My brochure! There you go, little guy. I'm
not scared of him. It's an allergic thing. Put that on your resume
brochure. My whole face could puff up. Make it one of your special
skills. Knocking someone out is also a special skill. Right. Bye,
Vanessa. Thanks. - Vanessa, next week? Yogurt night? - Sure, Ken. You
know, whatever. - You could put c's dream! Up on a float, surrounded by
flowers, crowds cheering. A tournament. Do the roses compete in athletic
events? No. All right, I've got one. How come you don't fly everywhere?
It's exhausting. Why don't you run everywhere? It's faster. Yeah, OK, I
see, I see. All right, your turn. TiVo. You can just freeze live TV?
That's insane! You don't have that? We have Hivo, but it's a disease.
It's a horrible, horrible disease. Oh, my. Dumb bees! You must want to
sting all those jerks. We try not to sting. It's usually fatal for us.
So you have to watch your temper. Very carefully. You kick a wall, take
a walk, write an angry letter and throw it out. Work through it like any
emotion: Anger, jealousy, lust. Oh, my goodness! Are you OK? Yeah. -
What is wrong with you?! - It's a bug. He's not bothering anybody. Get
out of here, you creep! What was that? A Pic 'N' Save circular? Yeah, it
was. How did you know? It felt like about 10 pages. Seventuspenders and
colored dots... Next week... Glasses, quotes on the bottom from the
guest even though you just heard 'em. Bear Week next week! They're
scary, hairy and here live. Always leans forward, pointy shoulders,
squinty eyes, very Jewish. In tennis, you attack at the point of
weakness! It was my grandmother, Ken. She's 81. Honey, her backhand's a
joke! I'm not gonna take advantage of that? Quiet, please. Actual work
going on here. - Is that that same bee? - Yes, it is! I'm helping him
sue the human race. - Hello. - Hello, bee. This is Ken. Yeah, I remember
you. Timberland, size ten and a half. Vibram sole, I believe. Why does
he talk again? Listen, you better go 'cause we're really busy working.
But it's our yogurt night! Bye-bye. Why is yogurt night so difficult?!
You poor thing. You two have been at this for hours! Yes, and Adam here
has been a huge help. - Frosting... - How many sugars? Just one. I try
not to use the competition. So why are you help hat! This is pathetic!
I've got issues! Well, well, well, a royal flush! - You're bluffing. -
Am I? Surf's up, dude! Poo water! That bowl is gnarly. Except for those
dirty yellow rings! Kenneth! What are you doing?! You know, I don't even
like honey! I don't eat it! We need to talk! He's just a little bee! And
he happens to be the nicest bee I've met in a long time! Long time? What
are you talking about?! Are there other bugs in your life? No, but there
are other things bugging me in life. And you're one of them! Fine!
Talking bees, no yogurt night... My nerves are fried from riding on this
emotional roller coaster! Goodbye, Ken. And for your information, I
prefer sugar-free, artificial sweeteners made by man! I'm sorry about
all that. I know it's got an aftertaste! I like it! I always felt there
was some kind of barrier between Ken and me. I couldn't overcome it. Oh,
well. Are you OK for the trial? I believe Mr. Montgomery is about out
olear the gate. Royal Nectar Force onmushroom! He  - Oh, my! - I never
thoughink I should... Barry? Ba yesterday? Hold bbling like a cicadot
like a flowerve. Very close. . - I'm tall. - Yo is flowers. Oull riit's
no troubl opost belies been three dsions to thiu'retalk to him?friend.
's Bee-ish. They have a hugrnament of Roses, that's every florito a sci
from Honeyhat's a man in womn? The be keat. What right do they have to
our honey? We live on two cups a year. init? Am I sure? When I' Barry?
It's pretty big, isnWhat's therablendustfiveyburton and Honron! Yes, it
seems yoll thinplease sit down! I think it was awf! Well, hello. - Ken!
- Hello. I didn't think you wertte you do thatttwe'd all l? I've seen a
  bee documentary orreal pa're an ion't y'all date your cousins? -
  Objection! - I'm goin veour Honor, it's interestinghis court's
  valuable time? HoThey have pLadies and gent! Free the bees! F os
  ing?awaout. He'llhaveeaan't u ouldMaybe not.

---
## [Aspyse/dice-spire](https://github.com/Aspyse/dice-spire)@[c35c7b1c0d...](https://github.com/Aspyse/dice-spire/commit/c35c7b1c0d86d8ba4e5691b38f3323581d067ff4)
#### Thursday 2022-07-07 13:53:26 by Derek Royce Luy Burias

im sorry i was a lil idiot boy

i will not upload my token again

---
## [Flopster101/kernel_xiaomi_ginkgo](https://github.com/Flopster101/kernel_xiaomi_ginkgo)@[4fe8bf3cd9...](https://github.com/Flopster101/kernel_xiaomi_ginkgo/commit/4fe8bf3cd9b485de476d4e4ad929a73cf4f69018)
#### Thursday 2022-07-07 14:16:24 by Dan Pasanen

power: don't ever reboot to verity red

* We get it, shit's broken. We're flashing custom stuff, shit's bound
  to break. Don't pop this annoying screen up, we're not even using
  verity anyway.

Change-Id: Icd77b70ec1df9108a4ba9e7fd8cb9623b35b78db
Signed-off-by: celtare21 <celtare21@gmail.com>

---
## [ammarfaizi2/linux-block](https://github.com/ammarfaizi2/linux-block)@[846bb97e13...](https://github.com/ammarfaizi2/linux-block/commit/846bb97e131d7938847963cca00657c995b1fce1)
#### Thursday 2022-07-07 15:21:51 by Jason A. Donenfeld

random: credit cpu and bootloader seeds by default

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

---
## [FranzBusch/swift-protobuf](https://github.com/FranzBusch/swift-protobuf)@[ec18c12a55...](https://github.com/FranzBusch/swift-protobuf/commit/ec18c12a55a304c3d0f6b3bf90e310de9e23a312)
#### Thursday 2022-07-07 15:25:10 by FranzBusch

Add SPM plugin

# Motivation
SPM is providing new capabilities for tools to expose themselves as plugins which allows them to generate build commands. This allows us to create a plugin for `SwiftProtobuf` which invokes the `protoc` compiler and generates the Swift code. Creating such a plugin is greatly wanted since it improves the usage of the `protoc-gen-swift` plugin dramatically. Fixes https://github.com/apple/swift-protobuf/issues/1207

# Modification
This PR adds a new SPM plugin which generates build commands for generating Swift files from proto files. Since users of the plugin might have complex setups, I introduced a new `swift-protobuf-config.json` file that adopters have to put into the root of their target which wants to use the new plugin. The format of this configuration file is quite simple:

```json
{
    "invocations": [
        {
            "protoFiles": [
                "Foo.proto"
            ],
            "visibility": "internal"
        }
    ]
}

```

It allows you to configure multiple invocations to the `protoc` compiler. For each invocation you have to pass the relative path from the target source to the proto file. Additionally, you have to decide which visibility the generated symbols should have. In my opinion, this configuration files gives us the most flexibility and more complex setups to be covered as well.

# Open topics

## Hosting of the protoc binary
Hosting of the protoc binary is the last open thing to figure out before we can release a plugin for `SwiftProtobuf`. From my point of view, there are three possible routes we can take:

1. Include the `artifactbundle` inside the `SwiftProtobuf` repository
2. Include the `artifactebundle` as an artifact on the GH releases in the protobuf repo
3. Extend the the artifact bundle manifest to allow inclusion of URLs. This would require a Swift evolution pitch most likely.

However, with all three of the above we would still need to release a new version of `SwiftProtobuf` with every new release of `protoc`.

# Future work

## Proto dependencies between modules
With the current shape of the PR one can already use dependencies between proto files inside a single target. However, it might be desirable to be able to build dependency chains of Swift targets where each target includes proto files which depend on protoc files from the dependencies of the Swift target. I punted this from the initial plugin because this requires a bit more work and thinking. Firstly, how would you even spell such an import? Secondly, the current way of doing `ProtoPathModuleMapping` files is not super ideal for this approach. It might make sense to introduce a proto option to set the Swift module name inside the proto files already.

# Result
We now have a SPM plugin that can generate Swift code from proto files. To use it, it provides a configuration file format to declare different invocations to the `protoc` compiler.

---
## [LinLeng/terminal](https://github.com/LinLeng/terminal)@[1374396f10...](https://github.com/LinLeng/terminal/commit/1374396f1022dfef13f8f65bcb0cb75dc64924c1)
#### Thursday 2022-07-07 17:04:52 by Michael Niksa

Delay load call SetThreadDescription to restore WPF renderer on Win7 (#10582)

Delay load call SetThreadDescription to restore WPF renderer on Win7

## PR Checklist
* [x] Closes something @DHowett asked me to do.
* [x] I work here
* [x] I F5'd it on a version with this function and it still works


## Detailed Description of the Pull Request / Additional comments

I keep forgetting that anything in the WPF control needs to keep working on Win7. Or more specifically... I remember this fact for the DX renderer, but not for the render thread base. Oops. Turns out this particular convenience method to set thread descriptions for visibility inside the debugger (to make my life easier) only works down to 1607 (see https://docs.microsoft.com/windows/win32/api/processthreadsapi/nf-processthreadsapi-setthreaddescription). Since it's just a debugging convenience... skipping it entirely when the procedure is not found should be fine. Also I don't try to load `kernel32.dll` and just get the handle of the existing module (which per the remarks at https://docs.microsoft.com/windows/win32/api/libloaderapi/nf-libloaderapi-getmodulehandlew will not increment the module reference count) because `kernel32.dll` pretty much has to be there or we're already in hot water.

---
## [Team-Ikigami/Ascendance](https://github.com/Team-Ikigami/Ascendance)@[e137af9f29...](https://github.com/Team-Ikigami/Ascendance/commit/e137af9f29806dbbe3e63a473fbbfb79aff09cad)
#### Thursday 2022-07-07 18:08:12 by DuckEater54

God fucking dammit I absolutetly hate the 1 minute compilation for each failure. Ill try getting rid of the fullscreen

---
## [peff/git](https://github.com/peff/git)@[fac7986b68...](https://github.com/peff/git/commit/fac7986b6802acb25acbc79366737b39f3d841a1)
#### Thursday 2022-07-07 18:50:22 by Jeff King

clone: propagate empty remote HEAD even with other branches

Unless "--branch" was given, clone generally tries to match the local
HEAD to the remote one. For most repositories, this is easy: the remote
tells us which branch HEAD was pointing to, and we call our local
checkout() function on that branch.

When cloning an empty repository, it's a little more tricky: we have
special code that checks the transport's "unborn" extension, or falls back
to our local idea of what the default branch should be. In either case,
we point the new HEAD to that, and set up the branch.* config.

But that leaves one case unhandled: when the remote repository _isn't_
empty, but its HEAD is unborn. The checkout() function is smart enough
to realize we didn't fetch the remote HEAD and it bails with a warning.
But we'll have ignored any information the remote gave us via the unborn
extension. This leads to nonsense outcomes:

  - If the remote has its HEAD pointing to an unborn "foo" and contains
    another branch "bar", cloning will get branch "bar" but leave the
    local HEAD pointing at "master" (or whatever our local default is),
    which is useless. The project does not use "master" as a branch.

  - Worse, if the other branch "bar" is instead called "master" (but
    again, the remote HEAD is not pointing to it), then we end up with a
    local unborn branch "master", which is not connected to the remote
    "master" (it shares no history, and there's no branch.* config).

Instead, we should try to use the remote's HEAD, even if its unborn, to
be consistent with the other cases.

Some notes on the implementation:

 - we don't emit any specific warning here, which is unlike the
   empty-repo case (which says "you appear to have cloned an empty
   repository"). For non-bare clones, checkout() will issue a warning
   like:

     warning: remote HEAD refers to nonexistent ref, unable to checkout

   For a bare clone, it won't emit any warning at all (but will still
   set up HEAD appropriately). That's probably fine. There's no part of
   the operation we were unable to perform, so any "by the way, the
   remote HEAD wasn't there but we pointed our HEAD to it anyway"
   message would be purely informational. Though perhaps one could argue
   the same about the current "empty repository" message in a bare
   clone.

 - if the remote told us about its HEAD via the unborn extension, this
   is obviously the right thing to do. If they didn't, we'll fall back
   to our local default name. As the "unborn" extension was added in
   v2.31.0, we'd expect hosts which don't support it to become
   decreasingly common, and it may not be worth worrying too much about.
   But for the sake of completeness, here are some thoughts:

     - if the remote has a non-HEAD "master", we may still end up with a
       local "master" that isn't connected to it. This is because the
       "how to set local unborn HEAD" code is independent from the "did
       we find a remote HEAD we can checkout" code. This could be fixed,
       but I'm not sure it's worth caring too much about, since you'd
       have to really try hard to create such a situation.

     - if the remote has branches but doesn't tell us about its HEAD,
       we could pick one of those branches as our HEAD instead of
       whatever our local default is. This feels on-balance worse to me.
       While it might do the right thing in some cases (especially if
       there is only a single branch), it could certainly lead to
       surprising and unintuitive outcomes in others.

---
## [Die4Ever/deus-ex-randomizer](https://github.com/Die4Ever/deus-ex-randomizer)@[a29391e06f...](https://github.com/Die4Ever/deus-ex-randomizer/commit/a29391e06f7381cb52afa2dda450c0a656b0e4d9)
#### Thursday 2022-07-07 19:48:16 by theastropath@gmail.com

Added bingo events for killing the sick man in Battery Park who wants to
die, giving money to the junkie who lives under Maggie Chow, and for
getting the VersaLife maps from the guy in the Old China Hand

---
## [chooglen/git](https://github.com/chooglen/git)@[25baa4d22e...](https://github.com/chooglen/git/commit/25baa4d22e2b3d192da051c2b1bddd78fa001699)
#### Thursday 2022-07-07 20:50:06 by Glen Choo

setup.c: create `discovery.bare`

There is a known social engineering attack that takes advantage of the
fact that a working tree can include an entire bare repository,
including a config file. A user could run a Git command inside the bare
repository thinking that the config file of the 'outer' repository would
be used, but in reality, the bare repository's config file (which is
attacker-controlled) is used, which may result in arbitrary code
execution. See [1] for a fuller description and deeper discussion.

A simple mitigation is to forbid bare repositories unless specified via
`--git-dir` or `GIT_DIR`. In environments that don't use bare
repositories, this would be minimally disruptive.

Create a config variable, `discovery.bare`, that tells Git whether or
not to die() when it discovers a bare repository. This only affects
repository discovery, thus it has no effect if discovery was not
done, e.g. if the user passes `--git-dir=my-dir`, discovery will be
skipped and my-dir will be used as the repo regardless of the
`discovery.bare` value.

This config is an enum of:

- "always": always allow bare repositories (this is the default)
- "never": never allow bare repositories

If we want to protect users from such attacks by default, neither value
will suffice - "always" provides no protection, but "never" is
impractical for bare repository users. A more usable default would be to
allow only non-embedded bare repositories ([2] contains one such
proposal), but detecting if a repository is embedded is potentially
non-trivial, so this work is not implemented in this series.

[1]: https://lore.kernel.org/git/kl6lsfqpygsj.fsf@chooglen-macbookpro.roam.corp.google.com
[2]: https://lore.kernel.org/git/5b969c5e-e802-c447-ad25-6acc0b784582@github.com

Signed-off-by: Glen Choo <chooglen@google.com>

---
## [CoinMarketCapAustraliaNFTs/docs](https://github.com/CoinMarketCapAustraliaNFTs/docs)@[fa6c0dae26...](https://github.com/CoinMarketCapAustraliaNFTs/docs/commit/fa6c0dae26cc22f32a2f3cd4d4b28a0628754314)
#### Thursday 2022-07-07 21:52:55 by CoinMarketCap Australia NFT'S

msnmoneystocks@gmail.com

Benefits
Build
Enjoy access to JetBrains tools as it provides a broader set of IDE for different programming languages such as Python, Java, and Kotlin.

Use Bootstrap Studio to create responsive websites using the Bootstrap framework.

Polypane cares about making your site responsive, fast and accessible, including over 80 accessibility tests, 14 different emulators and two dozen tools.

Launch
GitHub Pages allows you to launch websites for you and your projects. Hosted directly from your GitHub repository. Just edit, push, and your changes are live.

Digital Ocean provides simple cloud hosting, built for developers.

Learn
Have fun learning how to code with TwilioQuest, an educational video game designed to teach a new generation of developers how to change the world with code.

Learn while building through Microsoft Azure’s Cloud Advocates Web Development for Beginners course. This 12-week, 24-lesson curriculum teaches you all about JavaScript, CSS, and HTML basics.

Level up on trending coding skills at your own pace with Educative’s interactive, text-based courses.

Offers and additional benefits status blocks and embedded text data...

Home
Privacy policy
TL;DR: Blockchair does not collect personal data or share it with third parties. We don't track you.

server {
    server_name blockchair.com;
    access_log off;
Why is this important?
One of the key advantages of cryptocurrencies is that they enable (pseudo)anonymous transactions. In most cases the user’s address and transaction details are made public and cannot be deleted, but their personal identity remains unknown if no link exists between the user and their blockchain data.

Privacy is at risk when you share any information with third parties. Cryptocurrency exchanges with KYC policies, online retailers that require delivery addresses and web wallets associated with phone numbers all require you to share information.

What’s more, most web servers maintain default logs of your IP address and User Agent (browser name and operating system), the dates and times of your browsing activity and, most importantly, the URLs you visited. Ordinarily, a cryptocurrency address page is only visited by the address owner, while the transaction page is visited by the transaction parties. Blockchain explorers can therefore easily trace the digital fingerprint that links addresses and transactions. Unfortunately, this data is also picked up by the web analytics tools (Google Analytics, Baidu Tongji, Yandex.Metrica), advertising platforms and similar third-party services.

User data can be traced in others ways too. CDN providers like Cloudflare, Incapsula and AWS Shield act as reverse proxies, which means some websites require you to request data from a CDN in order to use the site. You therefore share your information with the provider.

In addition to these data tracking services, there are several other ways how users can be identified online.

HTTP referer: a client request header that allows a server to trace the previous site you visited. Say you visit example.com followed by explorer.com/1YourBitcoinAddress then the former will receive information that you have come from the latter;
Web beacon (bug): an invisible web page element that confirms a user has visited a web page. This is used to collect user analytics;
Cookies: user activity data stored in the user’s browser. Third-party cookies can also be embedded in the site’s code (if it contains elements from other sites);
Evercookie: a JavaScript app that stores zombie cookies on a computer. These cookies are extremely difficult to remove since Evercookie recreates them whenever they are deleted;
Device / browser fingerprint: the device and browser information collected for user identification;
Browser extensions.
Why is it unsafe to share you personal data?
Most blockchain explorers and cryptocurrency companies store user information, including available balances, lists of transactions and types of cryptocurrency.

They might sell this information, publish it, share it with government agencies, or they might be hacked. If it becomes public knowledge that you have significant funds stored in cryptocurrency, you’re likely to be targeted by cyber criminals. Your personal safety may be at risk too.

Why is Blockchair the safer option?
When you connect to Blockchair your browser automatically sends us information about your computer, User Agent, IP address, and the page you want to visit. Since this data may expose your identity, we do not permanently store information about you;
We do not use cookies that can be used to identify you. We may only set our own cookies to improve your user experience and help us to fight botnets and spammers. See below for details;
Your browser won’t send HTTP referer headers when leaving Blockchair.com. This means you can move to other sites without your browsing activity being traced by those sites;
We do not use CDN-providers, including those used to distribute JavaScript libraries and styles. We do not use any third-party site elements, web analytics tools (such as Google Analytics) and hit counters. Therefore, other parties do not receive information about you.
We do not collect any user data, neither on ours nor third-party servers in our “Blockchair” Chrome Extension.
What data do we store and how do we use this data?
We only collect anonymous aggregated data that allows us to improve our website features. We count visitors, analyze popular searches, cryptocurrencies, sortings and other queries.

We also store the incoming IP addresses in masked or clear form for short periods of 1 to 2 days. This is to limit the rate of API requests.

Your device may store first-party cookies, such as those that keep the night mode on, store referer information, unique visitor and session ID.

Collected data is used to improve user experience and compile website traffic statistics. Session data is deleted on a regular basis.

We can also store and use the data you provide us through email or with other channels of communication such as Telegram or contact forms located on our website. We can use the stored data to provide you with our services, to defend our legal rights, to improve accuracy, effectiveness, security, usability of our products or we can use it in any other way you will agree to.

Overall, we won't keep your data longer than necessary.

Please, be informed, that this Privacy Policy applies on all Blockchair products and has force only in a part where it doesn't contradict to Terms of Service of any product of Blockchair Limited. This Privacy Policy provides a general legal framework for the data collection in Blockchair products, hence the respective Terms of Service for each Blockchair product can regulate this issue differently within its respective scope of applicability. In case of contradiction between provisions of any Blockchair Terms of Service and this Privacy Policy, the provisions of Blockchair Terms of Service in question should prevail.

Privacy Policy updates
We will publish any updates to our Privacy Policy at this page (https://blockchair.com/privacy) and in the GitHub repository at https://github.com/Blockchair/Blockchair.Support/blob/master/PRIVACY.md plus the link to the updated version will be available at the bottom of all our site pages.

Contacts
Please share your comments and suggestions at <danielleahy304@gmail.com>.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[cbdf67060a...](https://github.com/treckstar/yolo-octo-hipster/commit/cbdf67060a4219855d769857832111846c88a780)
#### Thursday 2022-07-07 23:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [sa111n111/crayon.py](https://github.com/sa111n111/crayon.py)@[3048036d95...](https://github.com/sa111n111/crayon.py/commit/3048036d9588aac65420a273a7bdb7c3e2d7e727)
#### Thursday 2022-07-07 23:22:23 by sa111n111

holy fucking shit markdown (actual final readme change)

---

