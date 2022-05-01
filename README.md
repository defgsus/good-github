## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-04-30](docs/good-messages/2022/2022-04-30.md)


1,440,064 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,440,064 were push events containing 2,156,300 commit messages that amount to 119,701,350 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 30 messages:


## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[579bb9a238...](https://github.com/treckstar/yolo-octo-hipster/commit/579bb9a2389bed2fec390a24bf64ba7cddaef47b)
#### Saturday 2022-04-30 00:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Cutiekittypet/Tannhauser-Gate](https://github.com/Cutiekittypet/Tannhauser-Gate)@[c5f0ea76e0...](https://github.com/Cutiekittypet/Tannhauser-Gate/commit/c5f0ea76e0fa1d1236fe04a2edaf6d9c047fc7c8)
#### Saturday 2022-04-30 00:25:59 by SkyratBot

[MIRROR] Vim mecha changes [MDB IGNORE] (#12981)

* Vim mecha changes (#66153)

This PR changes the following:

    fixes a bug with Vim overlays, making it always appear as if there was a pilot inside, even after leaving it
    adds a balloon alert when a mob fails to enter the mech due to its size
    adds a crafting recipe for Vim in the "robots" category
    allows using Vim as a circuit shell
    allows small mobs to use the mech as well

My reasoning behind the changes:

    fixing the overlay bug - bugfixes good, bugs bad
    balloon alert - it should help reduce confusion among players who can't figure why on earth they cannot enter the mech
    crafting recipe - I think a crafting recipe will make it a lot more accessible to players, especially because there is no way to learn about its existence in-game
    circuit shell - non-standard circuit shells can be pretty fun and people seemed to enjoy the ability to use circuits inside their piano synths or cameras, so I figured we could expand on this, while giving players more ways to interact with sentient pets
    maximum mob size increase - Vim has never really been built too often, most likely because even if people got their hands on a sentient pet, it wouldn't probably fit in the tiny mecha anyway. Currently pretty much only butterflies, rats and cockroaches can use Vim and they pretty much never become sentient.

* Vim mecha changes

Co-authored-by: B4CKU <50628162+B4CKU@users.noreply.github.com>

---
## [Offroaders123/Menu-Drop-Component](https://github.com/Offroaders123/Menu-Drop-Component)@[6dc66baa36...](https://github.com/Offroaders123/Menu-Drop-Component/commit/6dc66baa36834bf18c220e9616051aed0f30680d)
#### Saturday 2022-04-30 00:38:12 by Offroaders123

The Componentization!

Alright! Unfortunately, this is my second time around to writing this changelog. I was about more than halfway through writing it when my dad turned off the power to fix one of the lights in our house. I had to take a little break, it really bugged that I lost about 15 minutes of writing out of nowhere. Aah, ok. Let's try it again XD

I've been working on this update for a while now, pretty much since the last one I released just a few days ago. I essentially rewrote Menu Drop's logic to better handle changes in it's element structure, and made it more user-accessible by removing the Shadow DOM (user in this case being whoever implements Menu Drop, not the site user). Here's some more about that, next!

Changes:
- Now that the Shadow DOM has been taken out, the entire component's structure is directly part of the Light DOM! This allows the user to style the different sub-components using global CSS, like you might for a standard `<select>` menu. You won't have to use `::part()` selectors anymore.
- *Part* of the last change (p-unintended (this intended though, lol)), now each of the sub-components within Menu Drop now use their own dedicated custom elements, rather than using existing built-in ones, like `ul` and `li`! This both helps prevent global style collisions with other page styles (one of my reasons for wanting to use Shadow DOM originally), and this makes things much easier for moving component behavior out of the main Menu Drop element, and on to the child elements instead. One example of this, is that rather than calling `MenuDropElement.getOptions(aListWithOptions)` to get a list's items, you now call the method (now a getter) on the list itself, `MenuListElement.items`.
- Also related to that last note, menu options are now called menu items, once again, like the classic Menu Drop days. I think I changed to calling them options around when I added the select menu behavior, and now I think I like the original implementation I had before, which equates to the standard `ul` and `li` elements, with the equivalents of `menu-list` and `menu-item` for Menu Drop.
- Thanks to the more modular nature of the component's structure, the element will now better handle customization by the user as they need. For example, say you wanted to add a new item to a new list in an existing sub menu. Now you can just use `document.createElement()` like you would for anything else in the DOM, and the Web Component classes for Menu Drop's sub-components will handle setting everything up for you! No need to add `tabindex` or `part` attributes to a new menu item anymore, now they show up there as soon as the element is initialized!
- There are still a few features I have to re-implement before this new setup is synonymous with the existing stable release of Menu Drop, like the select menu behavior, support for anchor tags inside of list items, and mobile support. The buttons and everything work on mobile, but I want to get everything working nicely for desktop first before I start to add specific changes to mobile.
- And another change/feature addition is that I want to make the default styles for Menu Drop more-default like, as if it was a standard built-in HTML element from the spec. It's more boring for sure, but I'd like it to have an un-opinionated look in terms of styles, like that it would make you want to add your own look to it. Especially now that it is part of the Light DOM, now it will be much easier to add your own look, however you want it to be!
- Also also also related to the last note, these new default styles are responsive to dark color schemes! I found out about these on web.dev, and in the W3C Working Draft pages. It's called System Colors, and they respond to whatever the currently set color scheme is. This is great because it means that Menu Drop will look light in light mode, and dark in dark mode, no need to add any `@media` queries or color scheme properties yourself! This was something I've been hoping to have without any extra style tricks, for a while now, and I love how simple the styles are to get it to work. For more info about System Colors, check out these two articles which helped me get exactly what I've wanted!
https://web.dev/color-scheme/#the-user-agent-stylesheet
https://drafts.csswg.org/css-color/#css-system-colors

Alright, alright. Sorry if that was insanely long (it was, probably). I like to try and write everything about my updates now, as it really helps to document the journey along the way, and to be able to look back and see if I missed anything (undoubtedly, yes). This is a much more modern setup for Menu Drop, and I think it is more semantically nice to work with, something that wasn't quite the case before.

Oh yeah! One more thing I will also do with time, is to add Aria roles and attributes to the custom sub-components, as right now they don't have them, and the previous `ul` `li` ones did. I haven't tried those out yet before, so I will read more about them before implementing them here.

Okay! That should be good now :)

See ya soon!
Brandon

---
## [GForceTF/tgstation](https://github.com/GForceTF/tgstation)@[a137c15a79...](https://github.com/GForceTF/tgstation/commit/a137c15a790bc8242a1ccd70bb6570d0278833c0)
#### Saturday 2022-04-30 01:11:12 by Vladin Heir

Kills research scanner toggle, moves functionality to examine_more. Improves research scanner code and fixes a modsuit bug. (#66415)

* FINALLY. I'VE KILLED IT. I CAN LIVE MY LIFE NOW.

I hate the fucking Toggle Research Scanner action button so god damn much. Why the fuck would I ever not want this to be on? Why do you think I'm wearing the fucking goggles? That stupid button is so annoying to use. Even if I'm NOT using the research scanner aspect of the goggles, that little shit floats there, taking up space on my screen, taunting me.

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[a0fa5ba3ce...](https://github.com/Paxilmaniac/Skyrat-tg/commit/a0fa5ba3ce25d019dafa88e1d606e079f7649cc6)
#### Saturday 2022-04-30 01:45:23 by SkyratBot

[MIRROR] Updates Maps And Away Missions MD [MDB IGNORE] (#13095)

* Updates Maps And Away Missions MD (#66455)

* Updates Maps And Away Missions MD

Hey there,

This was outdated for a bit, so I decided to pretty it up and make a few things a bit more explicit.

I alphabetized the maps since we don't really prioritize one-over-the-other (except Meta now being the default map instead of the non-existent Box).

I also alphabetized Removed Station Maps, and removed the "outdated" (they are all outdated, or will definitely all be outdated by the time a reader reads this).

I elaborated a bit more on how station maps are loaded these days (correct me if I am wrong).

Standardized how we show code paths.

Gave explicit instructions on never using Dream Maker to map, and linking two programs that we tell anyone who wanders in on the Discord to use anyways (please do inform me if we should not do this- but Dream Maker just fucking sucks shit).

I also fixed up some language around the Away Missions part, and added a newer section for the Map Depot since I do not believe it is discussed elsewhere on the main repository (as well as a short warning on anyone who things they can get Phobos or something running out-of-the-box).

Alright, cool.

* Updates Maps And Away Missions MD

Co-authored-by: san7890 <34697715+san7890@users.noreply.github.com>

---
## [Justin4587/holbertonschool-interview](https://github.com/Justin4587/holbertonschool-interview)@[2114b573c2...](https://github.com/Justin4587/holbertonschool-interview/commit/2114b573c215f7e75a6a4c4aa390940e212254ea)
#### Saturday 2022-04-30 01:55:05 by Justin Thurman

I really hate losing points over stupid shit. I'm gussing my compiler was a different version or something

---
## [liquidprjkt/liquid_kernel_xiaomi_lavender](https://github.com/liquidprjkt/liquid_kernel_xiaomi_lavender)@[fcb70167f6...](https://github.com/liquidprjkt/liquid_kernel_xiaomi_lavender/commit/fcb70167f606ec17f23e10451d8ecd34620d7356)
#### Saturday 2022-04-30 02:02:50 by Maciej Żenczykowski

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
Signed-off-by: liquidprjkt <xprjkts@gmail.com>

---
## [PhoenixBureau/PythonOberon](https://github.com/PhoenixBureau/PythonOberon)@[43a475feb4...](https://github.com/PhoenixBureau/PythonOberon/commit/43a475feb4a4955808bc07b9842f2f0a762b8a36)
#### Saturday 2022-04-30 02:11:38 by Simon Forman

I guess you don't need that first noop?

I must have put it there for a reason?  Oh yeah!  The Joy interpreter I
was working on used the Zeroth word as the root of all stacks (or
something like that, it's been over a year) so it had to point to
itself, or something.  Anyway, that's enough information, however dimly
recalled, to put my concern about that no-op to rest.  Whew!

---
## [hamishdev/AlarmRadio](https://github.com/hamishdev/AlarmRadio)@[b3149e678c...](https://github.com/hamishdev/AlarmRadio/commit/b3149e678c18053f17932610a6e39d6ca80121ea)
#### Saturday 2022-04-30 02:18:14 by hamishdev

26/04/2022

-lul fixed it

Twitch being muted was actually a much bigger problem than I thought, but also my implementation was really bad (I had a webview of a custom hosted webpage that embeded the twitch player in it) and the twitch player obeys all the rules of a default browser (like chrome or etc) and those browsers have very strict rules about loading a video and playing it with sound without user interaction.

But like I said it was the wrong way to go about it anyway, because a webview of the link (youtube or twitch) doesn't involve a 3rd party browser (just the android WebView browser), and therefore I can custom set the flag which allows videos in a twitch or Youtube webpage to play automatically (mediaPlaybackRequiresUserGesture). There was a little fenangling to ensure the webview didn't by default use the native twitch or youtube mobile apps...? (I don't actually know what these are, they're not the downloaded apps, theyre like if you view a webpage from mobile, because what I want is just like the desktop site ((I think)))

Either way, links are playing on lockedscreen on alarm going off now. (Everything looks shit because of a 3-day proof that it could work worrying about nothing else)

---
## [Fargowilta/FargowiltasSouls](https://github.com/Fargowilta/FargowiltasSouls)@[bda389a9ff...](https://github.com/Fargowilta/FargowiltasSouls/commit/bda389a9ff5b153f2ef438ee4bc3463699b77313)
#### Saturday 2022-04-30 02:26:50 by terrynmuse

deerclops emode
 x1.25 life
 attacks inflict hypothermia, frostburn, and marked for death (he hits like a wet noodle its ok)
 spike attacks are bigger
 debris moves faster
 can actually despawn
 literally just removed random ghost hands because i hate them
deerclops has a 66% p2
 can teleport behind you
 spike attacks are gigantic
 less startup on double wall
 spike double wall persists a bit longer
deerclops has a 33% p3
 faster
 roar comes with a stomp on you
 double wall spike persists for VERY long (can stunlock)
deerclops has maso changes
 all ice persists longer
 adds the ghost hands back
 everything is dumbfuck faster

---
## [new-meta-incorporated/pokemon-showdown](https://github.com/new-meta-incorporated/pokemon-showdown)@[2358ac4adb...](https://github.com/new-meta-incorporated/pokemon-showdown/commit/2358ac4adbe199eb8bcf6d89878435eb42c3aea9)
#### Saturday 2022-04-30 02:29:26 by Matteo

scarcaneshitpart2

Yeah, so, I'm an idiot, and merging the old version would've fucked shit up. We'll have to do the rotom-glow/mow and scarcane learnsets again.

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[bcc9c5365f...](https://github.com/san7890/bruhstation/commit/bcc9c5365f71f28ba2900c58a8541776ea836252)
#### Saturday 2022-04-30 04:19:27 by san7890

Menage A Trois - Putting IceBoxStation In One DMM

Hey there,

I got it to work. I thought something would horribly break. However, nothing did. Not a peep out of runtimes, and cave generator appears to have worked flawlessly. I'm astounded, maybe I just did everything right, or maybe there's a deep demon lurking underneath the surface. Irregardless, it works:tm:.

There is a new annoying thing where you must click up twice in StrongDMM to get up to the "Station" level of IceBox, but such is the price we pay for being able to visualize everything in one window.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[7c61bf65f2...](https://github.com/tgstation/tgstation/commit/7c61bf65f2b3c661bf622864bb7596e0e89d1f28)
#### Saturday 2022-04-30 05:48:50 by vincentiusvin

Makes glass floors override platings. Fixes glass floor openspace bug. (#66301)


About The Pull Request

Fixes #63868. Actual one liner fix for this one here. If this pr dies feel free to atomize this one.
AND it turns out to not be tim's fault.

Fixes #63548. But i really shouldnt say fixed. The original implementation was causing the invincible plating bug. When tim's refactor got in it instead relies on the element state, which was broken from the get go, removing the invincible plating bug which was in a sense "intended" its all messy man I hate this code. Thats why im removing the plating thing. Let the turf handle the turf change themselves this complicates things.

Mapped in glass floors have openspace (now baseturf bottom) as their baseturfs, while built ones have plating under them. Which doesnt make sense to be honest. Why would things be visible if a plating is under the glass. They are also crowbarrable on top of this, which to be fair is my main reasoning behind the PR.

To solve this, I am instead making glass floors replace the plating instead of building over it. This is made to be generalizable for every tile in game, as long as their initial baseturf is the same and the tile wants it to happen.

do after of three seconds is completely arbitrary. If any maint want it changed let me know.
Why It's Good For The Game

First one solves a bug
Second one makes more sense
And er, icebox is currently using the glass floors in sec, they can be crowbarred very easily. This might be a good idea from a gameplay perspective.
Changelog

cl
del: Removed adding glass floors to plating
balance: Allows you to replace plating with glass floors instead. 3 second timer.
del: Removed deconstructing the glass floors. No replacement for this one, use a rcd.
fix: Fixed metastation glassfloor spawning a weird turf when crowbarred.
/cl

---
## [PKRoma/git](https://github.com/PKRoma/git)@[bdaf1dfae7...](https://github.com/PKRoma/git/commit/bdaf1dfae71fdf120fc7253e713ccf0a06cc5558)
#### Saturday 2022-04-30 06:20:07 by Tao Klerks

branch: new autosetupmerge option 'simple' for matching branches

With the default push.default option, "simple", beginners are
protected from accidentally pushing to the "wrong" branch in
centralized workflows: if the remote tracking branch they would push
to does not have the same name as the local branch, and they try to do
a "default push", they get an error and explanation with options.

There is a particular centralized workflow where this often happens:
a user branches to a new local topic branch from an existing
remote branch, eg with "checkout -b feature1 origin/master". With
the default branch.autosetupmerge configuration (value "true"), git
will automatically add origin/master as the upstream tracking branch.

When the user pushes with a default "git push", with the intention of
pushing their (new) topic branch to the remote, they get an error, and
(amongst other things) a suggestion to run "git push origin HEAD".

If they follow this suggestion the push succeeds, but on subsequent
default pushes they continue to get an error - so eventually they
figure out to add "-u" to change the tracking branch, or they spelunk
the push.default config doc as proposed and set it to "current", or
some GUI tooling does one or the other of these things for them.

When one of their coworkers later works on the same topic branch,
they don't get any of that "weirdness". They just "git checkout
feature1" and everything works exactly as they expect, with the shared
remote branch set up as remote tracking branch, and push and pull
working out of the box.

The "stable state" for this way of working is that local branches have
the same-name remote tracking branch (origin/feature1 in this
example), and multiple people can work on that remote feature branch
at the same time, trusting "git pull" to merge or rebase as required
for them to be able to push their interim changes to that same feature
branch on that same remote.

(merging from the upstream "master" branch, and merging back to it,
are separate more involved processes in this flow).

There is a problem in this flow/way of working, however, which is that
the first user, when they first branched from origin/master, ended up
with the "wrong" remote tracking branch (different from the stable
state). For a while, before they pushed (and maybe longer, if they
don't use -u/--set-upstream), their "git pull" wasn't getting other
users' changes to the feature branch - it was getting any changes from
the remote "master" branch instead (a completely different class of
changes!)

An experienced git user might say "well yeah, that's what it means to
have the remote tracking branch set to origin/master!" - but the
original user above didn't *ask* to have the remote master branch
added as remote tracking branch - that just happened automatically
when they branched their feature branch. They didn't necessarily even
notice or understand the meaning of the "set up to track 'origin/master'"
message when they created the branch - especially if they are using a
GUI.

Looking at how to fix this, you might think "OK, so disable auto setup
of remote tracking - set branch.autosetupmerge to false" - but that
will inconvenience the *second* user in this story - the one who just
wanted to start working on the topic branch. The first and second
users swap roles at different points in time of course - they should
both have a sane configuration that does the right thing in both
situations.

Make this "branches have the same name locally as on the remote"
workflow less painful / more obvious by introducing a new
branch.autosetupmerge option called "simple", to match the same-name
"push.default" option that makes similar assumptions.

This new option automatically sets up tracking in a *subset* of the
current default situations: when the original ref is a remote tracking
branch *and* has the same branch name on the remote (as the new local
branch name).

Update the error displayed when the 'push.default=simple' configuration
rejects a mismatching-upstream-name default push, to offer this new
branch.autosetupmerge option that will prevent this class of error.

With this new configuration, in the example situation above, the first
user does *not* get origin/master set up as the tracking branch for
the new local branch. If they "git pull" in their new local-only
branch, they get an error explaining there is no upstream branch -
which makes sense and is helpful. If they "git push", they get an
error explaining how to push *and* suggesting they specify
--set-upstream - which is exactly the right thing to do for them.

This new option is likely not appropriate for users intentionally
implementing a "triangular workflow" with a shared upstream tracking
branch, that they "git pull" in and a "private" feature branch that
they push/force-push to just for remote safe-keeping until they are
ready to push up to the shared branch explicitly/separately. Such
users are likely to prefer keeping the current default
merge.autosetupmerge=true behavior, and change their push.default to
"current".

Also extend the existing branch tests with three new cases testing
this option - the obvious matching-name and non-matching-name cases,
and also a non-matching-ref-type case. The matching-name case needs to
temporarily create an independent repo to fetch from, as the general
strategy of using the local repo as the remote in these tests
precludes locally branching with the same name as in the "remote".

Signed-off-by: Tao Klerks <tao@klerks.biz>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [jhonmethew/jhon-](https://github.com/jhonmethew/jhon-)@[82d8a72eb8...](https://github.com/jhonmethew/jhon-/commit/82d8a72eb8a299232211584b915f2f674fc74551)
#### Saturday 2022-04-30 07:23:03 by jhonmethew

bookmywear

Bookmywear Is well established online Platform for women Attire. We means Bookmywear has expertise and experience of more than a decade to design and manufacture the latest designer Women apparel. We have very friendly Website so people cannot confuse and easily come to know all require details related to products and payment and shipping. We are the only store mainly focus on latest design for all types of Lehenga choli, Lehenga, Gown, Party Wear Gown, Saree, Banarasi saree, Kurti, Salwar Suit, Salwar Kameez and all Women Attire.

We, Bookmywear is one stop solution for all kind of clothing for women and Girls. We are customer friendly hence our Terms and condition and Privacy policy has taken Customer’s Satisfaction and experience into the consideration. We have secure mode of online payments. We also Provide Cash on Delivery option so, customer don’t face any issue related to payment. Customer satisfaction is our goal so, we Provide the best quality products to our customer at reasonable Price. We have very transparent Policy and terms condition for Shipping, Return and Exchange So, Our customer come to know very clear and specific details so they are not entertained. We follow the Latest and Unique Trends for women Attire like Bollywood Lehenga or Lehenga choli, Bollywood Saree, Festive Lehenga and festive gown. So, our customer come to know regarding latest trend and go with trend to be fashionable and stylish to walk with the time.

	Our motive is to provide latest trend and latest design quality Apparel for women at best price. We have vast variety of different and unique collection for women attire. People loves us as we have Huge collection of clothing for women and girls. Not only this but we all also protect customer privacy So, Customer feel secure and safe while purchasing from our site “BOOKMYWEAR.COM”.  People also love to purchase from us as we have all trendy design and style cloths available in different Color and Size as per customer requirements. We also provide Customize Stitching to our customer as per customer requirement so customer don’t need to go anywhere else.

---
## [Capitanloco6/Divergences-HPM](https://github.com/Capitanloco6/Divergences-HPM)@[a149573ae0...](https://github.com/Capitanloco6/Divergences-HPM/commit/a149573ae03d17b6287156cd19ecd9c1aa509f93)
#### Saturday 2022-04-30 07:32:09 by Capitanloco6

Armenia and Kar-Kiya patch

-	Added possibility for Armenia to break free If the Shaki fail their early wars. The Player can attempt to lead an uprising against the Shaki and play the newly added Armenian content which contains:
o	Flavour-events for the process of civilising
o	Armenian expansion and gaining cores in the Caucasus and Anatolia over the course of the game
o	An event chain regarding the state of the Armenian Cilicians
o	A decision to restore the Empire of Tigranes the Great for absolute Monarchies and fascist dictatorships and a less reactionary equivalent for socialist governments
o	Decisions to accept Assyrians, Georgians and Syriacs
o	Flavour events such as the reintegration of the Armenian diaspora
-	Added an event chain to the Kar-Kiya leading up to the constitutional revolution. The choices taken during the events unlock one of the three possible country paths for the Kar-Kiya
o	Constitutionalist – Nationalist. Encourage unification rebels in other Iranian countries, liberate the Caspian Iranians in Azerbaijan and reform the administration and economy of your realm, among other decisions.
o	Zaydi – Theocratic. Content regarding the persecution of the other Shi’a sects within your realm, expansion towards the holy shrines in Khorasan and the protection of the Zaydi minority in Yemen.
o	Royalist. Take advantage of the Russian patrons that helped keep the monarchy in power – at the risk of the Russians making unacceptable demands back. Possiblity of getting a new tech school and conflict if Russia decides to expand into the southern Caspian shore as the first step towards India.
-	Reduced the maluses Italy receives upon integrating Venice, Sardinia and Corsica
-	Reduced the militancy maluses the Sublime Porte receives when the Janissaries win the Civil War, preventing the depopulation of Bulgaria
-	Proclaiming the Kingdom of Hanover now gives Rhenish as an accepted culture
-	Taking the Baltic expansion path as Russia no longer leaves a few random provinces uncored
-	Mostar is now properly considered a port province, no longer making Illyria a landlocked nation
-	Fixed naval base in Christanborg, preventing bugged ship building
-	Fixed positions in Kiel
-	Fixed the Scramble for Africa full annexation CB not working as intended
-	The decision to integrate the Cape Coloured can no longer be taken as a Vryland-formed South Africa
-	The decision to integrate Greeks as a Venice who failed in the Council of Athens now properly works for both regular Republic and Merchant Republic governments
-	Various miscellaneous localisation fixes
-	Fixed improper promotion of serfs to farmers in mineral RGO provinces
-	Neu Kurland and Tobago now start as states, making Neu Kurland runs more viable
-	Eendrachtsland now has Burgundian rather than Bosnian ship names
-	Tarfaya, Aaiun and Dakhla no longer start as colonial provinces
-	Dissolving Gran Colombia as an Arcadian/Amerigan Great Power now properly releases Lusitania and Cuba

---
## [tannerhelland/PhotoDemon](https://github.com/tannerhelland/PhotoDemon)@[9dea56340e...](https://github.com/tannerhelland/PhotoDemon/commit/9dea56340e82e33d43d27621b6dd9d8498979d98)
#### Saturday 2022-04-30 13:05:48 by Tanner

First draft of `Edit > Content-Aware Fill` tool

Holy shit, friends - this actually works.  I'm honestly a little (okay a LOT) astonished to see the functional content-aware fill behavior in action, because part of me thought this was never going to work in a reasonably good way.

But it works, and it works *well*.  Like, this will be a tool that people actually use!

There's a ton of clean-up and refinement left to do (and I still need to build a UI) but that's easy-peasy compared to just getting the damn algorithm working in the first place.

---
## [limoniumstatice/bulu_kernel_sm8250](https://github.com/limoniumstatice/bulu_kernel_sm8250)@[38b0bd0f25...](https://github.com/limoniumstatice/bulu_kernel_sm8250/commit/38b0bd0f251010073efb3fc37a708ae9079bb332)
#### Saturday 2022-04-30 13:08:54 by Linus Torvalds

gpiolib: acpi: use correct format characters

[ Upstream commit 213d266ebfb1621aab79cfe63388facc520a1381 ]

When compiling with -Wformat, clang emits the following warning:

  gpiolib-acpi.c:393:4: warning: format specifies type 'unsigned char' but the argument has type 'int' [-Wformat]
                        pin);
                        ^~~

So warning that '%hhX' is paired with an 'int' is all just completely
mindless and wrong. Sadly, I can see a different bogus warning reason
why people would want to use '%02hhX'.

Again, the *sane* thing from a human perspective is to use '%02X. But
if the compiler doesn't do any range analysis at all, it could decide
that "Oh, that print format could need up to 8 bytes of space in the
result". Using '%02hhX' would cut that down to two.

And since we use

        char ev_name[5];

and currently use "_%c%02hhX" as the format string, even a compiler
that doesn't notice that "pin <= 255" test that guards this all will
go "OK, that's at most 4 bytes and the final NUL termination, so it's
fine".

While a compiler - like gcc - that only sees that the original source
of the 'pin' value is a 'unsigned short' array, and then doesn't take
the "pin <= 255" into account, will warn like this:

  gpiolib-acpi.c: In function 'acpi_gpiochip_request_interrupt':
  gpiolib-acpi.c:206:24: warning: '%02X' directive writing between 2 and 4 bytes into a region of size 3 [-Wformat-overflow=]
       sprintf(ev_name, "_%c%02X",
                            ^~~~
  gpiolib-acpi.c:206:20: note: directive argument in the range [0, 65535]

because gcc isn't being very good at that argument range analysis either.

In other words, the original use of 'hhx' was bogus to begin with, and
due to *another* compiler warning being bad, and we had that bad code
being written back in 2016 to work around _that_ compiler warning
(commit e40a3ae1f794: "gpio: acpi: work around false-positive
-Wstring-overflow warning").

Sadly, two different bad compiler warnings together does not make for
one good one.

It just makes for even more pain.

End result: I think the simplest and cleanest option is simply the
proposed change which undoes that '%hhX' change for gcc, and replaces
it with just using a slightly bigger stack allocation. It's not like
a 5-byte allocation is in any way likely to have saved any actual stack,
since all the other variables in that function are 'int' or bigger.

False-positive compiler warnings really do make people write worse
code, and that's a problem. But on a scale of bad code, I feel that
extending the buffer trivially is better than adding a pointless cast
that literally makes no sense.

At least in this case the end result isn't unreadable or buggy. We've
had several cases of bad compiler warnings that caused changes that
were actually horrendously wrong.

Fixes: e40a3ae1f794 ("gpio: acpi: work around false-positive -Wstring-overflow warning")
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [Patriot-06/android_kernel_realme_x3](https://github.com/Patriot-06/android_kernel_realme_x3)@[94f9c59c9e...](https://github.com/Patriot-06/android_kernel_realme_x3/commit/94f9c59c9ea368c0f80c2c01eaa62d4ef6f636d5)
#### Saturday 2022-04-30 14:31:03 by George Spelvin

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
## [NokioPyro/stuff-for-gb](https://github.com/NokioPyro/stuff-for-gb)@[efd5b9fec0...](https://github.com/NokioPyro/stuff-for-gb/commit/efd5b9fec0b72e7e9f794bf4d722dc48d4eccd1d)
#### Saturday 2022-04-30 14:53:22 by NokioPyro

Add files via upload

Fuck you adobe flash JESUS CHRIST I GOT JUMPSCARED I WAS WATCHING SPOOKY MONTH WHEN WRITING THIASJKHDSAHLKDHJKL

---
## [cmss13-devs/cmss13-design-docs](https://github.com/cmss13-devs/cmss13-design-docs)@[2dc78c4391...](https://github.com/cmss13-devs/cmss13-design-docs/commit/2dc78c4391e2fe20ab9b6cef1e1cd0b4a196c5ea)
#### Saturday 2022-04-30 15:00:30 by Bigboyyo

I'm so sick of things preventing me from getting this merged holy fuck

---
## [AkjDragonMaster/Java](https://github.com/AkjDragonMaster/Java)@[73e729a949...](https://github.com/AkjDragonMaster/Java/commit/73e729a94987bdf76fca5c344062764b29a11a37)
#### Saturday 2022-04-30 16:30:45 by AkjDragonMaster

anime

Wake up to reality! Nothing ever goes as planned in this accursed world. The longer you live, the more you realize that the only things that truly exist in this reality are merely pain. suffering and futility. Listen, everywhere you look in this world, wherever there is light, there will always be shadows to be found as well. As long as there is a concept of victors, the vanquished will also exist. The selfish intent of wanting to preserve peace, initiates war. and hatred is born in order to protect love. There are nexuses causal relationships that cannot be separated

---
## [SadAugust/AutoTrimps_Testing](https://github.com/SadAugust/AutoTrimps_Testing)@[f7b39ffdb5...](https://github.com/SadAugust/AutoTrimps_Testing/commit/f7b39ffdb51d3a4ae1748556e0767ccd67539602)
#### Saturday 2022-04-30 17:55:37 by SadAugust

Fixing bugs and adding universe selection feature

Heyy, I made a few modification to graphs for my AT fork and figured I might as well share since it fixes a few bugs that I've at least been annoyed by quite a bit. If you want to test it out first to make sure it's all working you can test it on https://SadAugust.github.io/AutoTrimps_Local. Changed I've made are listed below, I've only done minimal testing but haven't found any issues with it.

Removed minified version of code to make it readable

Added option to select Universe which will visibility of U1 and U2 graphs depending on the selection. Reduces a ton of unnecessary settings from cluttering the list and figured I'd make it easier to expand for if we do get more universes.

Remembers graph selection when reloading the page instead of defaulting to helium/radon per hour

Hides portals from other universes showing so if U2 graphs are being looked at you won't see U1 portals in the sidebar, should fix bugs like void maps being unreadable when there's a significant difference in portals between the 2 universes.

Fixed it not drawing graphs properly when reopening Graphs after the initial load as it was a nuisance having to go to another graph and back to get it to display anything.

---
## [LukeSandsor/GitFit-App](https://github.com/LukeSandsor/GitFit-App)@[581b91acff...](https://github.com/LukeSandsor/GitFit-App/commit/581b91acff84fb97f45824bbf79384b501b06dde)
#### Saturday 2022-04-30 20:13:35 by Lucas Reyna

after painfully implementing contexts into the CalendarPage.js, I am happy to announce that the calendar will now load info on a specific day. The code looks kinda like garbage, but it works for now. I just hope that there won't be many slow downs when incorporating the backend. We'll have to see about caching, maybe.

---
## [doctea/usb_midi_clocker](https://github.com/doctea/usb_midi_clocker)@[e5ae6ddad1...](https://github.com/doctea/usb_midi_clocker/commit/e5ae6ddad1e381b7955c008edcc83332611cfa09)
#### Saturday 2022-04-30 20:27:17 by doctea

first commit of teensy branch.  kinda works -- detects USB devices and assigns correct callbacks on boot, but fucks up when devices are disconnected/reconnected, and has same 'MIDI clock for second device is unstable as hell' problem that saw mentioned on forums :/

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[4d0bfb71de...](https://github.com/mrakgr/The-Spiral-Language/commit/4d0bfb71de2c2c5ba06fcaae5783ced28e600255)
#### Saturday 2022-04-30 20:55:29 by Marko Grdinić

"9:15am. Change of plans, I am doing the monitor right now. I've had a stressful night thinking about poles.

According to topology guides, poles are what cause pinching in the corners. And ngon and tries lead to that as well.

9:35am. Huh I was wrong. I thought that as long as I had all quads, there would be no pinching, but that is not the case. I made the top of a cylinder into quads and I am getting distortions even if its to a small degree. I expected it would be perfect, but that is not the case.

In fact, if I connect the middle into all triangles, the results is a lot better.

10:10am. I've been messing with the cylinder all this time. Let me go for some tuts.

https://youtu.be/NGmbHYySoLQ
Request - Avoid Pinching

10:15am. Hmmmm...

https://youtu.be/3rlMzsBWtPY
Advanced Subsurf Modeling - Techniques to Avoid Pinching

Let me watch this as well. Then instead of fiddling around with the cylinder, I'll do some work on the monitor.

https://youtu.be/3rlMzsBWtPY?t=169

> So what we are going to do is shrinkwrap this mesh on top of out guide mesh right here.

This is a good idea.

https://youtu.be/3rlMzsBWtPY?t=187

This fixed it rather well.

https://youtu.be/1PE-NUBWPrw
Blender 2 80 - Hole On Curved Surface. SubD Modeling.

Let me also watch this.

https://youtu.be/1PE-NUBWPrw?t=156

Ctrl + Shift is find shortest with fill region turned on. You learn something new every day.

10:40am. Why did I watch that? Forget it. Let me finally deal with the monitor. If needed, I'll retopo it by hand.

10:45am. The quad remesher is shit. Let me do it by hand.

Retopo sucks.

12:15pm. I am being a retard, this isn't working for me. Extruding edges and placing them where they should go looks a lot easier when the Youtuber girl did it.

Retopo is a specialized skill all on its own. I am not sure I care too much about it. So, what I am going to do is try assigning materials to loops.

12:50pm. The quad remesher is kind of shitty. It keeps doing a good result where I don't need it to. I'll have to try it out in Zbrush. Let me export the screen as obj.

12:55pm. What a shitty job Zbrush did importing the ngons.

1pm. When I triangulate it, it imports it properly. The Zremesher is better than the quad remesher.

But how do I import the material settings from the old thing?

In fact, it might be better if I ignored them and simply painted them. The edges in those materials are a bit crooked, but here I should be able to draw them straight thanks to possessing the shift key. I have to do this if I want to retopo because the edges are quite crooked.

Let me take a break here and I will do that. To think that Zbrush would be better for retopology than Blender.

1:30pm. I am done with breakfast at a record pace. Damn it, why can't I paint on the stupid thing. It is not reacting to my inputs. I turned on the paint mode. What did I forget to do? Let me take a refresher.

https://youtu.be/9ONLg_gC1tE
042 ZBrush Polypaint Basics

This might be an old tutorial, but nevermind. I did manage to make painting work a few days ago, but it slipped my mind how to do it. Nothing is appearing when I try to draw on the object.

https://youtu.be/9ONLg_gC1tE?t=163

It was nothing special. I think I was simply painting with the white color while expecting it to be black.

2:05pm. I am so incompetent. This is exactly how good you would expect a guy would be after just watching tutorials.

2:55pm. Aghhh, what the fuck am I doing?!

I am doing it pixel by pixel trying to iron out the edge. I've gone completely crazy.

Think me, think.

Don't I have a better way of doing this.

More than once, the though to increase the polycount to 1m from 10k right now and then paint the borders occured to me.

3:35pm. I give up! I can't make the Zremesher work for this. That thing has zero nuance, and I am finding it so hard to move around Zbrush. It is ridiculous.

5:40pm. Had to take a break for a bit.

At any rate, I am done with my first retopo attempt. I went back to Blender and did it by hand. I am really pissed at how poorly it went. Not the final product, but the way I worked at it. At best this is a passing grade.

I should be able to do something like this in 30m instead of it taking the whole day. Let me try it again.

This time I'll try putting a subdiv before a shrinkwrap and try to do it in smaller steps.

6:10pm. This seems a bit promising actually. I had the idea of importing the object in Moi and doing retopoint it that way. That kind of thing would work very well. With NURBs I could get it exactly where I want, but right now I am messing with projections.

6:25pm. https://youtu.be/QDM3UiNm7GM
ONE BY ONE: The Shrinkwrap Modifier in Blender 2.93 for retopology or surface based geometry.

Let me watch a tutorial. I am having trouble catching the edges properly.

https://youtu.be/QDM3UiNm7GM?t=335

This is pretty educational.

https://youtu.be/QDM3UiNm7GM?t=489

This is an interesting way of working.

I myself have always been gluing it to the surface, but maybe this way would be easier.

Also, since stretching the subdiv model is giving me trouble, why now split it apart. I can always grid fill it.

7pm. Had to leave for lunch. Let me resume.

Nix on working away from the surface. The closer I have the model to the reference, the better it will be for me.

7:25pn. Doing it like this defeats the purpose of using subdiv it is too imprecise. I am just moving things around trying to get it to fit around that hole. Screw that. Let me try loading it in Moi.

Moi can't even open it. I've waited long enough. Let me try opening it in Rhino.

7:35pm. Rhino opens it, but I do not know it well enough to try attempting retopology in it.

So far it has all been failure. Just like witH Hops, let me look into some of the retopo addons in Blender. It suddenly important to me. Extruding edges and connecting them is not really the way I should be working.

https://youtu.be/X8kQiccJetw
Learn RetopoFlow3 - Ultimate Retopo Tutorial

Let me watch this. Retopoflow is the most popular retopo addon in Blender.

///

Exoside Quad Remesher v1.1, v1.2

Quad Remesher — an auto-retopologizer from the developer of ZBrush ZRemesher — is available for Blender

///

Hmmm, the guy who made the Zbrush addon made the Blender one.

I see.

https://youtu.be/X8kQiccJetw?t=148

Having something like this would be useful yes.

https://youtu.be/X8kQiccJetw?t=445

This is way better than how I am doing it now.

https://youtu.be/X8kQiccJetw?t=828

I can't find this on Persia, but it will still be worth watching to get ideas. I think the topology brush of Zbrush should be what I need. The way I am working now is absolutely assinine. Towards the end, I did a merge it turns out I missed all kind of duplicate verts. Instead of doing that, drawing curves and having the polys be where they interset really makes sense.

I had to keep reapplying the shrinkwrap mod as well constantly.

https://youtu.be/X8kQiccJetw?t=895

Nevermind this, let me move to the Zbrush tutorials.

https://youtu.be/iF6dpIB3-us
Why am i doing Retopo in Zbrush and how?

https://youtu.be/iF6dpIB3-us?t=774

I need to make my technique better. I've tried doing it in batches, but that probably just ended up making thing more complicated for me.

https://youtu.be/iF6dpIB3-us?t=774

Let me pause here I want to try the polybuild tool again.

8:25pm. Yeah, the tool is awkward to use. I want the topo brush, so why am I wasting time on these videos. Let me skim that guy and then I'll take a look at the rest.

https://youtu.be/2UdUNa7c4ek?t=89
Quick and easy retopology of head in Zbrush (with bonus UV mapping)

This is on Zremesher guides.

8:40pm. Not very impressive.

https://youtu.be/kiKaWl4rcyc
008 ZSphere Retopology

Let me take a look at this.

https://youtu.be/kiKaWl4rcyc?t=238

I thought it would be something more fancy.

8:50pm. https://youtu.be/0MTfcpLma5Q
Zbrush - Topology Brush

https://youtu.be/0MTfcpLma5Q?t=161

I quite like this.

https://youtu.be/0MTfcpLma5Q?t=222

In this situation, houw would one connect that middle empty quad.

...No don't think of it as an empty quad. Think of it as a bunch of empty space. Once you look at it from that angle, the way becomes clear.

9:20pm. Let me try the brush myself.

Blender is good if you want to put the vertices line by line, but like hell am I going to put down 1000 faces by hand.

10pm. This sucks so bad. Let me try Moi again. I'll just do a crappy remesh and use that as a reference.

https://blendermarket.com/products/retopoflow

86$ is too much. No way am I buying this.

Hmm, it loaded it. I wonder what the problem was. Let me try 10k instead 1k. I'll remesh it again.

10:30pm. https://github.com/CGCookie/retopoflow

As it turns out Retopoflow can be found on Github. Forget Moi. I am really amazed at how good the subdiv import is, but wanting to retopo in Moi is stupid. Arrimus gave plenty of example of CAD software giving poor topology.

https://www.aeblender.com/2021/02/blender-addon-retopoflow-v3-1-0-rc2-crack-download/

Here is the cracked version.

https://www.reddit.com/r/blenderhelp/comments/eljxj8/short_guide_on_getting_retopoflow_30_to_work_from/

Here is a guide how to install it from Github.

https://github.com/CGCookie/retopoflow/releases

The one I got is outdated, so let me get the latest instead.

10:40pm. It installed very cleanly, I just had to download the zip from the releases page. I'll close here instead of trying it out. I am dead tired at this point in the day.

Tomorrow, I'll figure it out.

You can see how it builds. Me bashing my head against the wall gave me the motivation to improve my workflow in retoplogy. Rinse and repeat, and I'll get skilled eventually."

---
## [UnderMybrella/usa](https://github.com/UnderMybrella/usa)@[26b6161782...](https://github.com/UnderMybrella/usa/commit/26b61617829e98e83cc938ccf54a8beaea019055)
#### Saturday 2022-04-30 21:23:45 by MarkiSpider

Update 60 files @ Sat, 30 Apr 2022 21:23:42 GMT
This site update changes michaeljackson.html, the-asshats.html, thekilleidoscope.html, everyone.html, karen6815.html, Jupiterandfriends.html, the-baboonies.html, moriarty.html, zeusandfriends.html, thefounders.html, sexygoldarms.html, usa-home.html, byebyebye.html, woahhh.html, shatteredbysomeone.html, ohyouwouldlikethatwouldntyou.html, thecaptain.html, gettingjiggywithit.html, terrorblycute.html, karen6804.html, ijustmadeyoulookunderthere.html, Imsorrymissjackson.html, aretheyalium.html, karen-archive.html, the-d_.html, lolgotyou.html, thedude.html, dont-push.html, thebannerborn.html, theoracle.html, nebuchadnezzar.html, karen6816.html, cachow.html, oopsalbangers.html, illinois.html, karen6809.html, kriskringle.html, redacted.html, thejackson5.html, dickpicks.html, idkbro.html, capitalism.html, LixianTV.html, fuckem.html, corn-dm.html, karen6803.html, search.html, Rad_R.html, 2702-invincible2syndicate.html, agentloginportal.html, MichaelJackson.html, thealienalliance.html, terfwar.html, girlofthe21stcentury.html, thebutterflysoldiers.html, NerdFiction.html, iinhumanresources.html, case-directory.html, nyfu.png, bannerad03.jpg

---
## [Toshiro90/rathena](https://github.com/Toshiro90/rathena)@[d617d9f083...](https://github.com/Toshiro90/rathena/commit/d617d9f08381442b14cb69da6ef5251a12817cd3)
#### Saturday 2022-04-30 21:40:24 by Aleos

Updates SC_CHANGEUNDEAD behavior (#6867)

* Fixes #6834.
* Versus Players
- Animation will be properly displayed for Blessing/Increase Agility when the target has Change Undead active (buffs are not applied even though animation is displayed).
- Target can no longer be killed through the single damage applied by Blessing/Increase Agility and Change Undead.
- If the target has Curse and Stone active, only Curse is removed by Blessing first (buffs are not applied).
- Shadow or Undead armor have no impact on Blessing or Increase Agility at all.
* Versus Monsters
- Blessing is applied normally to the target as long as it's not an Undead element or Demon race.
- Blessing does not cancel out Curse or Stone.
Thanks to @Playtester!

---
## [Tastyfish/Skyrat-tg](https://github.com/Tastyfish/Skyrat-tg)@[cd2bd18cf8...](https://github.com/Tastyfish/Skyrat-tg/commit/cd2bd18cf8193c7cfc2f0014ef449baa8792aad4)
#### Saturday 2022-04-30 22:27:38 by SkyratBot

[MIRROR] Creates Linters for (bad) Commented Out Lines in Maps [MDB IGNORE] (#12543)

* Creates Linters for (bad) Commented Out Lines in Maps (#65888)

* Creates CI Linters for Commented Out Lines in Maps

Creates Linters for (bad) Commented Out Lines in Maps

Hey there,

This PR is made because what happened in #65837 was fucking horrible awful shit that I'm still dealing with a few days after I fixed it. This _should hopefully_ add a new linter for commented out lines of code in a .DMM file, and HOPEFULLY doesn't flag the commented line that prevents unwanted TGM > DMM conversion.

As a proof to see if it works, I'll be adding a comment to Line 2 of IcemoonUnderground_Above.dmm. Hopefully, on the first CI check, it'll fail. I'll remove that line so it doesn't make its way into production (it will suck).

* Creates Linters for (bad) Commented Out Lines in Maps

Co-authored-by: san7890 <34697715+san7890@users.noreply.github.com>

---
## [sigstksz/sigstksz.github.io](https://github.com/sigstksz/sigstksz.github.io)@[3e43f74932...](https://github.com/sigstksz/sigstksz.github.io/commit/3e43f749325f20951874fb8b1b73c9ff8b19bb8d)
#### Saturday 2022-04-30 22:49:04 by sigstksz

change sans serif to monospace, fuck you sans, monospace all the things

---

