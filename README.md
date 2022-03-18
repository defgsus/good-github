## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-03-17](docs/good-messages/2022/2022-03-17.md)


1,752,180 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,752,180 were push events containing 2,788,416 commit messages that amount to 190,498,802 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 29 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[0e904f7032...](https://github.com/tgstation/tgstation/commit/0e904f70328a460af310014891eaadb5968ec31a)
#### Thursday 2022-03-17 00:02:29 by LemonInTheDark

[MDB IGNORE] Moves non floor turfs off /floor. You can put lattices on lavaland edition (#65504)


About The Pull Request

Alternative to #65354

Ok so like, there was a lot of not floor types on /floor. They didn't actually want any of their parent type's functionality, except maybe reacting to breaking (which was easy to move down) and some other minor stuff.
Part of what we don't want them to have is "plateable" logic.
I should not be able to put floor tiles on the snow and be fine. It's dumb.

Instead, I've moved all non floor types down to a new type, called /misc.

It holds very little logic. Mostly allowing pipes and wires and preventing blob stuff.
It also supports lattice based construction, which is one of the major changes here. I think it makes more sense, and it fixes an assumption in shuttle code that assumed you couldn't place "a new tile" by just hitting some snow with a floor tile.
Oh and lattices don't smooth with asteroid tiles anymore, this looks nicer I think.

Moving on to commits, and minor changes

Changes clf3 to try and burn any turfs it's exposed to, instead of just floors
Moves break_tile down to the turf definition, alongside burn_tile
If you're in basic buildmode and click on anything that's not handled in a targeted way, you just build plating
FUNCTION CHANGE: you can't use cult pylons to convert misc tiles over anymore
Generalizes building floors on top of something into two helper procs on /turf/open, reducing copypasta
Adds a new turf flag, IS_SOLID, that describes if a turf is tangible or not.
Uses this alongside a carpet and open check to replace plating and floor checks in carpet code. This does mean that non iron tiles can be carpeted, but I think that's fine

Moves the /floor update_icon -> update_visuals call to /open
This change is horrificly old, dating back to 8e112f6 but that commit describes nothing about why it was done. Choosing to believe it was a newfriend mistake. Uncomfortable nuking it though, because of just how old it is. Moving down instead

Create a buildable "misc" type off open, moves /dirt onto it
Basically, we want a type we can use to make something support
construction, since that can be a messy bit of logic. Also enough
structure to set things up sanely.

I'm planning on moving most misc turfs onto it, if only because
constructing on a dirt tile with rods should be possible, and the same
applies to most things

Murders captain planet, disentangles /turf/open/floor/grass/snow/basalt

Adds a diggable component that applies the behavior of "digging"
something out from a turf.

Uses it to free the above pain typepath into something a bit more
sensible

The typepaths that aren't actually used by floor tiles are moved onto
/misc

The others are given names that better describe them, and kept in
fancy_floor

Oh and snowshoes don't work on basalt anymore, sorry

Snowed over platings now actually have broken/burned icon states, fixing black holes to nowhere

Misc turfs no longer smooth as floors, so lattices will ignore them

Placing a lattice will no longer scrape the tile it's on

Ok this is a really old one.
I believe this logic is a holdover from kor's baseturf pr
(97990c9)
It used to be that turfs didn't have a concept of "beneath" and instead
just decided what should be under them by induction. This logic of "if
it's being latticed scapeaway to space" made sense then, but has since
been somewhat distorted

We do want to scape away on lattice spawn sometimes, mostly when we're
being destroyed, but not always. We especially don't want to scape away
if someone is just placing a rod, that's dumb.

Adds a path updating script for this change

I've done my best to find all the errors this repathing will pull out, but I may have missed some. I'm sorry.
Why It's Good For The Game

Very old code made better, more consistent turfs for lavaland and icebox, better visuals, minor fix to snowed plating, demon banishment in lattice placement, fixes the icebox mining shuttle not being repairable
Changelog

cl
add: Rather then being tileable with just floor tiles, lavaland turfs, asteroid and snow (among other things) now support lattice -> floor tile construction
fix: Because of the above, you can now properly fix the icebox mining shuttle
refactor: Non floor turfs are no longer typed as floor. This may break things, please yell at me if it does
/cl

---
## [Shadow-Quill/tgstation](https://github.com/Shadow-Quill/tgstation)@[770ef81a1f...](https://github.com/Shadow-Quill/tgstation/commit/770ef81a1fb271572d711e7a05dbce62564ca3b0)
#### Thursday 2022-03-17 00:23:33 by John Willard

makes podpeople call parent (#65362)


About The Pull Request

kinda fucked up that it doesnt.
Also while checking this PR I noticed other species also don't, kinda screwed up world we live in...
Why It's Good For The Game

Parent's spec_life is what checks if you have nobreath, and in which case it will remove all your oxygen damage and, if in crit, give you brute damage instead. Not having this makes you basically not take damage while in crit, which I think shouldn't be the case.
Changelog

cl
fix: Podpeople now take self-respiration into account when taking damage from critical condition, like most other species.
/cl

---
## [GForceTF/tgstation](https://github.com/GForceTF/tgstation)@[884c1eeb62...](https://github.com/GForceTF/tgstation/commit/884c1eeb62e1c970b2b6edc425f36c924b9f48ee)
#### Thursday 2022-03-17 00:39:48 by 小月猫

fixes wallmounts (#65408)

closes #65393 (Engineering Cyborgs can't place APC or Air alarm frames on walls anymore)
fixes the code error in #64428 (afc1e44ee2922a316feb958249f7806568953bbe)

basically what occured is that he typed out the T(turf) attackby proc to input the screwdriver as an arg rather then the wallmount, remember, you want the WALLMOUNT to hit the wall to place it, not the screwdriver, that just creates runtimes and doesnt place anything

EDIT: actually re-reading it, what it was actually doing was using the screwdriver as the user arg, and trying to smash the user into the wall, thats actually kinda funny

borgo wallmounting is a good thing, good borgos need their treats

---
## [jhnstn/gutenberg](https://github.com/jhnstn/gutenberg)@[3ea2d42b0a...](https://github.com/jhnstn/gutenberg/commit/3ea2d42b0a6a206663735a47f9796bd42eda2186)
#### Thursday 2022-03-17 00:54:32 by Dennis Snell

Blocks: Remember raw source block for invalid blocks. (#38923)

Part of #38922

When the editor is unable to validate a block it should preserve the
broken content in the post and show an accurate representation of that
underlying markup in the absence of being able to interact with it.

Currently when showing a preview of an invalid block in the editor we
attempt to re-generate the save output for a block given the attributes
we originally parsed. This is a flawed approach, however, because by
the nature of being invalid we know that there is a problem with those
attributes as they are.

In this patch we're introducing the `__unstableBlockSource` attribute on 
a block which only exists for invalid blocks at the time of this patch. That 
`__unstableBlockSource` carries the original un-processed data for a block
node and can be used to reconstruct the original markup without using
garbage data and without inadvertently changing it through the series
of autofixes, deprecations, and the like that happen during normal block loading.

The noticable change is in `block-list/block` where we will be showing
that reconstruction rather than the re-generated block content. Previously
it was the case that the preview might represent a corrupted version of the
block or show the block as if emptied of all its content. Now, however,
the preview sould accurately reflect the HTML in the source post even
when it's invalid or unrecognized according to the editor.

Further work should take advantage of the `__unstableBlockSource`
property to provide a more consistent and trusting experience for
working with unrecognized content.

---
## [SuffolkLITLab/ALKiln](https://github.com/SuffolkLITLab/ALKiln)@[fe728649d3...](https://github.com/SuffolkLITLab/ALKiln/commit/fe728649d3b5a7be2d6cbf4eff90857d63a2986b)
#### Thursday 2022-03-17 01:30:00 by plocket

Update our package's dependencies for v4 (#503)

I'm thinking this is just going to be for v4. Not bothering with this for v3 unless we absolutely have to since none of the vulnerabilities are severe. My current rationale is that the more work we do to maintain 3, the less work we can do getting v4 ready for release. Ready to hear opinions.

- Close #164, update cucumber to v7
- Prepare for v8 of cucumber because I won't remember it later
- Close #394, update puppeteer
- Update our version of node (and that of our action that we'll run for other people's libs). [Addresses #393 so we can use the suffolk npm org package.]
- Use `npm audit` to fix the remaining vulnerabilities (now 0)
- [Remove package.json as discussed in #489 to align our tests' behaviors with those of our users.]

* Update action.yml node to v17

* Update from cucumber v6 to v7. See details.

See https://github.com/cucumber/cucumber-js/blob/main/docs/migration.md#migrating-to-cucumber-js-7xx

Only use cucumber setDefaultTimeout globally and use a shim that replicates the fix in v8 that lets you do custom timeouts more easily so we can still give enough time for steps that may need more time.

Use all caps for statuses.

Test screenshot step.

Btw, the cucumber test output visually looks a bit different now - when a scenario passes, all the steps pass too.

Sorry about the little comment changes, etc. Tried to remove a lot of those incidental unrelated changes.

* Update puppeteer to latest (13). See details below.

- page.waitFor -> page.waitForTimeout and page.waitForSelector (Got deprication notice. See https://github.com/puppeteer/puppeteer/issues/6214.)
- remove removeEventListener (we'd need to change it to removeListener anyway - v4.0.0 and see https://github.com/puppeteer/puppeteer/blob/main/docs/api.md#eventemitterremovelistenerevent-handler). For now we'll count on page close taking care of it, just in case removing it would prevent multiple-file-downloads.

* Update GitHub worflow node version, tweak changelog item order

* Fix npm audit vulnerabilities and update action.yml cucumber

* Pin the colors lib in action.yml

* Remove package-lock.json #489, use kiln v4 for users, CHANGELOG

* Fix custom timeout, remove duplicate report entry, as per review

---
## [Lamella-0587/Skyrat-tg](https://github.com/Lamella-0587/Skyrat-tg)@[8b1ec33143...](https://github.com/Lamella-0587/Skyrat-tg/commit/8b1ec331432234f358b26ee1627c10358ccae6a7)
#### Thursday 2022-03-17 01:49:51 by LeonY24

P90 (#12125)

* P90 SMG

le new gun for new away mission we're planning to make

* Update p90.dm

* includes p90.dm

my fucking retard ass hadnt shit included bruh

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[66a9307a05...](https://github.com/treckstar/yolo-octo-hipster/commit/66a9307a05cf0562099af40c767e737f5272a5a4)
#### Thursday 2022-03-17 03:45:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Tripp1986/Tripp1986](https://github.com/Tripp1986/Tripp1986)@[19c1ef6b27...](https://github.com/Tripp1986/Tripp1986/commit/19c1ef6b27fe26809b18ee15070a23c4738a16a8)
#### Thursday 2022-03-17 04:37:11 by Tripp1986

Rosa Bonheur's 200th Birthday   Cash App refund number  1-800-969-1940 FOR QUESTIONS OR ASSISTANCE, PLEASE CONTACT CUSTOMER SERVICE AT 1-800-969-1940 OR IN THE CASH APP.Aug 19, 2021 https://cash.app › legal › en-us › car... This Cash App Prepaid Card Program Agreement outlines the ... Feedback About featured snippets People also ask How do I force a refund on Cash App? How do I talk to a Cash App representative? Does Cash App actually refund? Will Cash App refund money if scammed? Feedback https://cash.app › contact Contact Cash App Support To speak to a Cash App Support representative, please request contact through Cash App, cash.app/help or at 1- 800-969-1940. https://cash.app › help How Can We Help You? - Cash App Get help using the Cash App and learn how to send and receive money without a problem using our support. People also search for https://donotpay.com › learn › cash-... How to Request a Cash App Refund - DoNotPay Dial +1 (845) 477-5160; Be patient while a Cash App representative answers; File a complaint on the unresponsive recipient. Once again, please note ... https://donotpay.com › learn › can-... How Can You Chargeback on Cash App? [Money Saving Hacks] Cash App Chargeback and Refund Policy ... Cash App has a phone number you can dial for support, and it is 855-351-2274. While you won't be able to talk to a ... Google Play Cash App Cash App 4.4 (1.1M) Cash App is the easiest way to send, spend, and invest your money. It's the SAFE, FAST, and FREE mobile banking* app. *Cash App is a financial services ... Install https://cash-app.pissedconsumer.com › ... Cash App Customer Service Phone Number (855) 351-2274, Email Jan 22, 2022 — (855) 351-2274. Call customer service. Customer Service: (800) 969-1940. Cash App Emails ... https://www.bbb.org › news-releases BBB Warning: Consumers Report Fake Cash App Customer Support Jul 23, 2020 — As of right now, Cash App does not actually offer customer service via the telephone, only via email or through the app. If a consumer does call ... https://www.elliott.org › cash-app-c... Cash App Customer Service Contacts - Elliott Advocacy Cash App is a mobile phone app that was developed by Square, Inc. The mobile app allows users to transfer money to one another. 1455 Market Street Suite 600 https://gethuman.com › contact › Sq... Contact Square Cash | Fastest, No Wait Time - GetHuman The best phone number and way to avoid the wait on hold, available live chat ... I received an email saying I was refunded money back to my cash app, ... Related searches Pay friends app Pay friends app Pay friends app Hillsborough, North Carolina - From your IP address Update location tripp131616@gmail.com - Switch account Dark theme: off Settings HelpFeedback PrivacyTerms About this resultBETA Source Cash App is a mobile payment service developed by Block, Inc. that allows users to transfer money to one another using a mobile phone app. The service is only available in the US and the UK. In September 2021, the service reported 70 million annual transacting users and has generated $1.8 billion in gross profit.Wikipedia · https://cash.app/contact · Your connection to this site is secure More about this page Your search & this result · These search terms appear in the result: cash and app · The website cash.app matches one or more of your search terms · Other websites with your search terms link to this result · The result is in English · This result seems relevant for searches from the United States Learn more search tips This is a search result, not an ad. Only ads are paid, and they'll always be labeled with "Sponsored" or "Ad."   Send feedback on this info Privacy settingsHow Search works

Rosa Bonheur's 200th Birthday


Cash App refund number

1-800-969-1940
FOR QUESTIONS OR ASSISTANCE, PLEASE CONTACT CUSTOMER SERVICE AT 1-800-969-1940 OR IN THE CASH APP.Aug 19, 2021
https://cash.app › legal › en-us › car...
This Cash App Prepaid Card Program Agreement outlines the ...
Feedback
About featured snippets
People also ask
How do I force a refund on Cash App?
How do I talk to a Cash App representative?
Does Cash App actually refund?
Will Cash App refund money if scammed?
Feedback
https://cash.app › contact
Contact Cash App Support
To speak to a Cash App Support representative, please request contact through Cash App, cash.app/help or at 1- 800-969-1940.
https://cash.app › help
How Can We Help You? - Cash App
Get help using the Cash App and learn how to send and receive money without a problem using our support.
People also search for
https://donotpay.com › learn › cash-...
How to Request a Cash App Refund - DoNotPay
Dial +1 (845) 477-5160; Be patient while a Cash App representative answers; File a complaint on the unresponsive recipient. Once again, please note ...
https://donotpay.com › learn › can-...
How Can You Chargeback on Cash App? [Money Saving Hacks]
Cash App Chargeback and Refund Policy ... Cash App has a phone number you can dial for support, and it is 855-351-2274. While you won't be able to talk to a ...
Google Play
Cash App
Cash App
4.4
(1.1M)
Cash App is the easiest way to send, spend, and invest your money. It's the SAFE, FAST, and FREE mobile banking* app. *Cash App is a financial services ...
Install
https://cash-app.pissedconsumer.com › ...
Cash App Customer Service Phone Number (855) 351-2274, Email
Jan 22, 2022 — (855) 351-2274. Call customer service. Customer Service: (800) 969-1940. Cash App Emails ...
https://www.bbb.org › news-releases
BBB Warning: Consumers Report Fake Cash App Customer Support
Jul 23, 2020 — As of right now, Cash App does not actually offer customer service via the telephone, only via email or through the app. If a consumer does call ...
https://www.elliott.org › cash-app-c...
Cash App Customer Service Contacts - Elliott Advocacy
Cash App is a mobile phone app that was developed by Square, Inc. The mobile app allows users to transfer money to one another. 1455 Market Street Suite 600
https://gethuman.com › contact › Sq...
Contact Square Cash | Fastest, No Wait Time - GetHuman
The best phone number and way to avoid the wait on hold, available live chat ... I received an email saying I was refunded money back to my cash app, ...
Related searches
Pay friends app
Pay friends app
Pay friends app
Hillsborough, North Carolina - From your IP address
Update location
tripp131616@gmail.com - Switch account
Dark theme: off
Settings
HelpFeedback
PrivacyTerms
About this resultBETA
Source
Cash App is a mobile payment service developed by Block, Inc. that allows users to transfer money to one another using a mobile phone app. The service is only available in the US and the UK. In September 2021, the service reported 70 million annual transacting users and has generated $1.8 billion in gross profit.Wikipedia
·
https://cash.app/contact
·
Your connection to this site is secure
More about this page
Your search & this result
·
These search terms appear in the result: cash and app
·
The website cash.app matches one or more of your search terms
·
Other websites with your search terms link to this result
·
The result is in English
·
This result seems relevant for searches from the United States
Learn more search tips
This is a search result, not an ad. Only ads are paid, and they'll always be labeled with "Sponsored" or "Ad."


Send feedback on this info
Privacy settingsHow Search works

---
## [projects-nexus/android_kernel_xiaomi_lavender-LTO](https://github.com/projects-nexus/android_kernel_xiaomi_lavender-LTO)@[ca6cafd669...](https://github.com/projects-nexus/android_kernel_xiaomi_lavender-LTO/commit/ca6cafd66977399d9c960c1f4361af50ebd52a40)
#### Thursday 2022-03-17 05:32:07 by Maciej Żenczykowski

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

---
## [chaldeaprjkt/kernel_xiaomi_vayu](https://github.com/chaldeaprjkt/kernel_xiaomi_vayu)@[18f03961b3...](https://github.com/chaldeaprjkt/kernel_xiaomi_vayu/commit/18f03961b3b28226ea69e75ebb973f77f7969e4f)
#### Thursday 2022-03-17 07:16:05 by Peter Zijlstra

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
## [Nowaaru/suwariyomi](https://github.com/Nowaaru/suwariyomi)@[1e64d32eb2...](https://github.com/Nowaaru/suwariyomi/commit/1e64d32eb26c28c6215b3cfa1f4c9f48ee04a69b)
#### Thursday 2022-03-17 07:52:31 by Nowaaru

give modal dark theme color which will inevitably bite me in the ass because i styled it using sx which isnt very compatible with the theming system i have in mind so life is genuinely just extremely awful i hate everything

---
## [varglbargl/varglbRPG](https://github.com/varglbargl/varglbRPG)@[833f748f9f...](https://github.com/varglbargl/varglbRPG/commit/833f748f9f43659feb696bbd950e4dffcd28511d)
#### Thursday 2022-03-17 08:35:45 by Vanessa

fixed some bugs with some shit

gonna have to make that start screen into a whole ass scene tomorrow, which might suck but might not

---
## [Mu-L/git](https://github.com/Mu-L/git)@[96bfb2d8ce...](https://github.com/Mu-L/git/commit/96bfb2d8ce221d31b3da08a49a455e316dbef7fb)
#### Thursday 2022-03-17 10:03:08 by Jeff King

run-command: unify signal and regular logic for wait_or_whine()

Since 507d7804c0 (pager: don't use unsafe functions in signal handlers,
2015-09-04), we have a separate code path in wait_or_whine() for the
case that we're in a signal handler. But that code path misses some of
the cases handled by the main logic.

This was improved in be8fc53e36 (pager: properly log pager exit code
when signalled, 2021-02-02), but that covered only case: actually
returning the correct error code. But there are some other cases:

  - if waitpid() returns failure, we wouldn't notice and would look at
    uninitialized garbage in the status variable; it's not clear if it's
    possible to trigger this or not

  - if the process exited by signal, then we would still report "-1"
    rather than the correct signal code

This latter case even had a test added in be8fc53e36, but it doesn't
work reliably. It sets the pager command to:

  >pager-used; test-tool sigchain

The latter command will die by signal, but because there are multiple
commands, there will be a shell in between. And it's the shell whose
waitpid() call will see the signal death, and it will then exit with
code 143, which is what Git will see.

To make matters even more confusing, some shells (such as bash) will
realize that there's nothing for the shell to do after test-tool
finishes, and will turn it into an exec. So the test was only checking
what it thought when /bin/sh points to a shell like bash (we're relying
on the shell used internally by Git to spawn sub-commands here, so even
running the test under bash would not be enough).

This patch adjusts the tests to explicitly call "exec" in the pager
command, which produces a consistent outcome regardless of shell. Note
that without the code change in this patch it _should_ fail reliably,
but doesn't. That test, like its siblings, tries to trigger SIGPIPE in
the git-log process writing to the pager, but only do so racily. That
will be fixed in a follow-on patch.

For the code change here, we have two options:

  - we can teach the in_signal code to handle WIFSIGNALED()

  - we can stop returning early when in_signal is set, and instead
    annotate individual calls that we need to skip in this case

The former is a simpler patch, but means we're essentially duplicating
all of the logic. So instead I went with the latter. The result is a
bigger patch, and we do run the risk of new code being added but
forgetting to handle in_signal. But in the long run it seems more
maintainable.

I've skipped any non-trivial calls for the in_signal case, like calling
error(). We'll also skip the call to clear_child_for_cleanup(), as we
were before. This is arguably the wrong thing to do, since we wouldn't
want to try to clean it up again. But:

  - we can't call it as-is, because it calls free(), which we must avoid
    in a signal handler (we'd have to pass in_signal so it can skip the
    free() call)

  - we'll only go through the list of children to clean once, since our
    cleanup_children_on_signal() handler pops itself after running (and
    then re-raises, so eventually we'd just exit). So this cleanup only
    matters if a process is on the cleanup list _and_ it has a separate
    handler to clean itself up. Which is questionable in the first place
    (and AFAIK we do not do).

  - double-cleanup isn't actually that bad anyway. waitpid() will just
    return an error, which we won't even report because of in_signal.

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [silont-project/kernel_xiaomi_surya](https://github.com/silont-project/kernel_xiaomi_surya)@[8b7945b830...](https://github.com/silont-project/kernel_xiaomi_surya/commit/8b7945b830ff59a44d951250a51b7d493a0f86a7)
#### Thursday 2022-03-17 12:33:27 by Yaroslav Furman

power: supply: force disable frame pointers and optimize for size

Holy fucking shit this is so retarded, it doesn't boot with frame pointers.

Signed-off-by: Yaroslav Furman <yaro330@gmail.com>

This is possibly breaking the DS28E16 verification driver
Signed-off-by: Forenche <prahul2003@gmail.com>
Signed-off-by: azrim <mirzaspc@gmail.com>

---
## [Divine-Journey-2/main](https://github.com/Divine-Journey-2/main)@[197b4428c4...](https://github.com/Divine-Journey-2/main/commit/197b4428c49c6e5c2842ab88e56797e27c163a77)
#### Thursday 2022-03-17 12:50:28 by Atricos

Update 2.13.0

Mod updates:

- AE2 Unofficial Extended Life v51d -> v51e (This fixes autocrafting not recognizing simulated returned items properly (like empty Buckets).)
- Replaced ReAuth 3.6.0 with OAuth 1.06.3. (This fixes not being able to relog with Microsoft accounts.)
- Added the Better P2P Mod. (This lets you see and find connected P2P tunnels in-world.) Also added a quest for it in Chapter 6.

Additions:

- Different tier EnderIO Conduits can now connect to each other.
- Pulsating Iron is now craftable in the Arc Furnace.
- Pereskia Bulbs can now also be used to make Plant Oil in the Squeezer.
- Added Hooves to the Mob Loot Fabricator Bewitchment output.

Fixes:

- Reverted the change from 2.11.0 that added Skyroot Planks to the plankWood OreDict. Now Skyroot Buckets are craftable again.
- The Mob Loot Fabricator Blood Magic recipe no longer incorrectly shows that it outputs LP.
- Fixed an issue where an empty Shulker Box that has been placed down and picked back up couldn't be upgraded into Iron Shulker Box.

Miscellaneous:

- Updated the Blood Altar link in the Chapter 17 Large Bloodstone Tile quest.
- Renamed the Chapter 3 Grove Stone quest and the Chapter 15 Cracked and Clean Runic Plate quests to avoid confusion.

---
## [wegtam/elasticsearch](https://github.com/wegtam/elasticsearch)@[37ea6a8255...](https://github.com/wegtam/elasticsearch/commit/37ea6a8255623d41be7df11440610ffa958ce50e)
#### Thursday 2022-03-17 13:46:18 by Nik Everett

TSDB: Support GET and DELETE and doc versioning (#82633)

This adds support for GET and DELETE and the ids query and
Elasticsearch's standard document versioning to TSDB. So you can do
things like:
```
POST /tsdb_idx/_doc?filter_path=_id
{
  "@timestamp": "2021-12-29T19:25:05Z", "uid": "adsfadf", "v": 1.2
}
```

That'll return `{"_id" : "BsYQJjqS3TnsUlF3aDKnB34BAAA"}` which you can turn
around and fetch with
```
GET /tsdb_idx/_doc/BsYQJjqS3TnsUlF3aDKnB34BAAA
```
just like any other document in any other index. You can delete it too!
Or fetch it.

The ID comes from the dimensions and the `@timestamp`. So you can
overwrite the document:
```
POST /tsdb_idx/_bulk
{"index": {}}
{"@timestamp": "2021-12-29T19:25:05Z", "uid": "adsfadf", "v": 1.2}
```

Or you can write only if it doesn't already exist:
```
POST /tsdb_idx/_bulk
{"create": {}}
{"@timestamp": "2021-12-29T19:25:05Z", "uid": "adsfadf", "v": 1.2}
```

This works by generating an id from the dimensions and the `@timestamp`
when parsing the document. The id looks like:
* 4 bytes of hash from the routing calculated from routing_path fields
* 8 bytes of hash from the dimensions
* 8 bytes of timestamp
All that's base 64 encoded so that `Uid` can chew on it fairly
efficiently.

When it comes time to fetch or delete documents we base 64 decode the id
and grab the routing from the first four bytes. We use that hash to pick
the shard. Then we use the entire ID to perform the fetch or delete.

We don't implement update actions because we haven't written the
infrastructure to make sure the dimensions don't change. It's possible
to do, but feels like more than we need now.

There *ton* of compromises with this. The long term sad thing is that it
locks us into *indexing* the id of the sample. It'll index fairly
efficiently because the each time series will have the same first eight
bytes. It's also possible we'd share many of the first few bytes in the
timestamp as well. In our tsdb rally track this costs 8.75 bytes per
document. It's substantial, but not overwhelming.

In the short term there are lots of problems that I'd like to save for a
follow up change:
1. ~~We still generate the automatic `_id` for the document but we don't use
   it. We should stop generating it.~~ Included in this PR based on review comments.
2. We generated the time series `_id` on each shard and when replaying
   the translog. It'd be the good kind of paranoid to generate it once
   on the primary and then keep it forever.
3. We have to encode the `_id` as a string to pass it around
   Elasticsearch internally. And Elasticsearch assumes that when an id
   is loaded we always store as bytes encoded the `Uid` - which *does*
   have nice encoding for base 64 bytes. But this whole thing requires
   us to make the bytes, base 64 encode them, and then hand them back to
   `Uid` to base 64 decode them into bytes. It's a bit hacky. And, it's
   a small thing, but if the first byte of the routing hash encodes to
   254 or 255 we `Uid` spends an extra byte to encode it. One that'll
   always be a common prefix for tsdb indices, but still, it hurts my
   heart. It's just hard to fix.
4. We store the `_id` in Lucene stored fields for tsdb indices. Now
   that we're building it from the dimensions and the `@timestamp` we
   really don't *need* to store it. We could recalculate it when fetching
   documents. In the tsdb rall ytrick this'd save us 6 bytes per document
   at the cost of marginally slower fetches. Which is *fine*.
5. There are several error messages that try to use `_id` right now
   during parsing but the `_id` isn't available until after the parsing
   is complete. And, if parsing fails, it may not be possible to know
   the id at all. All of these error messages will have to change,
   at least in tsdb mode.
6. ~~If you specify an `_id` on the request right now we just overwrite
   it. We should send you an error.~~ Included in this PR after review comments.
7. We have to entirely disable the append-only optimization that allows
   Elasticsearch to skip looking up the ids in lucene. This *halves*
   indexing speed. It's substantial. We have to claw that optimization
   back *somehow*. Something like sliding bloom filters or relying on
   the increasing timestamps.
8. We parse the source from json when building the routing hash when
   parsing fields. We should just build it from to parsed field values.
   It looks like that'd improve indexing speed by about 20%.
9. Right now we write the `@timestamp` little endian. This is likely bad
   the prefix encoded inverted index. It'll prefer big endian. Might shrink it.
10. Improve error message on version conflict to include tsid and timestamp.
11. Improve error message when modifying dimensions or timestamp in update_by_query
12. Make it possible to modify dimension or timestamp in reindex.
13. Test TSDB's `_id` in `RecoverySourceHandlerTests.java` and `EngineTests.java`.

I've had to make some changes as part of this that don't feel super
expected. The biggest one is changing `Engine.Result` to include the
`id`. When the `id` comes from the dimensions it is calculated by the
document parsing infrastructure which is happens in
`IndexShard#pepareIndex`. Which returns an `Engine.IndexResult`. To make
everything clean I made it so `id` is available on all `Engine.Result`s
and I made all of the "outer results classes" read from
`Engine.Results#id`. I'm not excited by it. But it works and it's what
we're going with.

I've opted to create two subclasses of `IdFieldMapper`, one for standard
indices and one for tsdb indices. This feels like the right way to
introduce the distinction, especially if we don't want tsdb to cary
around it's old fielddata support. Honestly if we *need* to aggregate on
`_id` in tsdb mode we have doc values for the `tsdb` and the
`@timestamp` - we could build doc values for `_id` on the fly. But I'm
not expecting folks will need to do this. Also! I'd like to stop storing
tsdb'd `_id` field (see number 4 above) and the new subclass feels like
a good place to put that too.

---
## [Danzo7/doctorIO](https://github.com/Danzo7/doctorIO)@[95f7726689...](https://github.com/Danzo7/doctorIO/commit/95f772668951073f546cb001f2d37b0eec161921)
#### Thursday 2022-03-17 14:50:51 by Danzo7

💥:  Drop all the support for snowpack

Although it was a very long journey of headaches to setup snowpack, and  even going further to create custom plugins for it, And after finally succeeding in all tasks that I suppose to do, I come to realize that even though it's a very beautiful concept and its work just fine at a very decent point, It's still unpredictable and it can break at any time, every update from the team was introducing new bugs and old bugs where rarely fixed I even try to contribute myself but there was a huge changes going on at the time that always break my work, well Nothing is wasted and it was a great experience but, unfortunately I decide to move to webpack , I start setting webpack up and I was succeeded to make them both work parallel in the same project. But snowpack become a legacy code for me and time has come to drop all packages related to it and remove the config file as it's no longer useful for the project, especially after the dev team move to another path and give-up on the project. Vite the supposedly snowpack alternative was a horrible experience for me as its filled with so much code and functionalities that has a very few uses cases, so from now we are sticking with webpack till the end of this project.

✨ I gain so much knowledge in the last year and I'm exiting to learn more as everyday something new appears✨ .

---
## [lynnnnzx/kernel_xiaomi_ysl](https://github.com/lynnnnzx/kernel_xiaomi_ysl)@[d072136e07...](https://github.com/lynnnnzx/kernel_xiaomi_ysl/commit/d072136e0719a5c829e1baa78811030c0942e1c0)
#### Thursday 2022-03-17 16:25:23 by Angelo G. Del Regno

Merge: Performance improvements.

This patchset brings some performance improvements and the addition of the LZO-RLE
algorithm to the kernel, also usable in zram (yup, tested, works but LZ4 is still ok for us).

The main performance improvement is for SWAP space: the locking has changed and
the swap cache is now split in 64MB trunks.
This gives us a reduction of the median page fault latency of 375%, from 15uS to 4uS,
and an improvement of 192% on the swap throughput (this includes "virtual" swap
devices, like zRAM!). The real world user experience improvement of this on a mobile
device is seen after a day or two of usage, where it usually starts losing just a little
performance due to the large amount of apps kept open in background: now I cannot
notice any more performance loss and the user experience is now basically the same as
if the phone was in its first 2 hours of boot life.

Other performance improvements include, in short:

    UDP v4/v6: 10% more performance on single RX queue
    Userspace applications will be faster when checking running time of threads
    2-5% improvements on heavy multipliers (yeah, not a lot, but was totally free...)
    Improvements on rare conditions during sparsetruncate of about 0.3% to a
    way more rare around 20% improvement (that's never gonna happen, but there
    is no performance drop anywhere).

Tested on SoMC Tama Akatsuki RoW

This was taken from
Repo:
https://github.com/sonyxperiadev/kernel
PR: 2039 ([2.3.2.r1.4] Performance improvements)

---
## [ar-sht/whichrewardscard](https://github.com/ar-sht/whichrewardscard)@[d6fc64733d...](https://github.com/ar-sht/whichrewardscard/commit/d6fc64733d18c35c7fe5583168a0430b06167227)
#### Thursday 2022-03-17 16:53:40 by Ari Shtein

It's working!!
  - Problems & solutions
    - Wasn't displaying results
      - Lots of little typos leading to Reference Errors - fixed typos
      - Was showing same card multiple times due to flaw in logic - improved logic's clarity
      - 'cards' list was drawing from wrong source leading to Key Errors - converted to draw from source it would be referenced against (probably inefficient and stupid, honestly I'm just glad it's finally working, I'll fix it later maybe probably not)
      - 'cards' list was sorting weirdly due to negatives and NaNs - added check to prevent the bullshit from getting in
    - Showed 'undefined' as a suggestion because I wanted results for different cards, and didn't account for the top two scores to be unique to just one card - added a check at the end of an iteration to reiterate process if necessary
  - Future plans
    - Might add database/memory/account stuff later
    - No support for next month or so, working on a different thing for a school assignment, also trying to do more Odin Project

---
## [mahak/scylla](https://github.com/mahak/scylla)@[674d3a5a84...](https://github.com/mahak/scylla/commit/674d3a5a8465c365cb0e608f4c921e3c12b758c6)
#### Thursday 2022-03-17 17:30:24 by Nadav Har'El

compound_compat.hh: add missing methods of iterator

While debugging legacy_compound_view, I noticed that it cannot be used
as a C++20 std::ranges::input_range because it is missing some trivial
methods. So let's fix this, and make the life of future developers a
little bit easier.

The two trivial methods we need to implement:

1. A postfix increment operator. We already had a prefix increment
   operator, but the C++20 concept weakly_iterable also needs postfix.

2. By mistake (this will be corrected in https://wg21.link/P2325R3),
   weakly_iterable also required the default_initialized concept, so
   our iterator type also needs a default constructor.
   We'll never actually use this silly constructor, and when this C++20
   standard mistake is corrected, we can remove this constructor.

After this patch, a legacy_compound_view is accepted for the C++20
ranges::input_range concept.

Signed-off-by: Nadav Har'El <nyh@scylladb.com>

---
## [ThePyProgrammer/masterMind](https://github.com/ThePyProgrammer/masterMind)@[4704a399d5...](https://github.com/ThePyProgrammer/masterMind/commit/4704a399d5ef39c2966f5ed4430e326f97b27711)
#### Thursday 2022-03-17 17:55:23 by ThePyProgrammer

PLEASE WORK FOR GOD'S SAKE YOU STUPID PIECE OF CRAP CODE I'VE WRITTEN FROM SCRATCH THREE TIME ALREADY!

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[8224f05927...](https://github.com/mrakgr/The-Spiral-Language/commit/8224f0592787aa0a1be9b4d9b37e7a9db147996c)
#### Thursday 2022-03-17 19:23:33 by Marko Grdinić

"10am. I am up. I had a really good night's sleep, completely different than yesterday. It seems there is a cycle of stress coming on and then short circuiting.

I realize - I was the strongest when I was just playing around and exploring. When I went out in pursuit of goals, my vision narrowed. Goals are important, but they are something to be played with, not something to control me. It is fine if I live accumulating skills.

The manipulation tree skills should naturaly send resources my way, and my programming skills when I have the resources to take advantage of them will serve as the catalyst for unlocking the door to true AI.

All that idiocy when I tried pushing things wasn't me. I do not need a plan more elaborate than just buying those AI chips in a store. They'll come one way or another.

10:10am. Let me read Tower of God and then I am going to get started.

10:30am. Let me start. Stop the Girls Frontline OST and start the course video.

No, actually, let me make the terrain. I'll start up Houdini.

10:35am. Agh, there is the mask expand. The guy doing the course knows nothing.

10:45am. In heightfield layer, the base offset and base scale don't do anything. I probably need to upgrade Houdini to fix these bugs, but V-Ray is hindering me. I'll get rid of it soon. This is one advantage of using USD - I do not have to worry about Houdini version incompatibilities with 3rd party renderers.

11:10am. Got an orangutan skull off sketchfab.

11:25am. Placed it, but at this point I am wondering if it is necessary to turn it into a volume as that make things ungoldy slow.

11:30am. It is really taking a while to convert the heightfield into something sensible.

11:30am. It took 2m and I got a result where there are tears where the height is 0. Lame.

I've decide to ramp up the voxel size drastically and decrease the detail by 16x. I can't work like this.

Let me watch the course. It has been smooth up to the point where I've started doing conversions.

I've converted the skull to a VDB, but I am not sure whether I should be doing that at all.

11:40am. Got an out of memory error when I tried opening the video while the skull was being unioned. Everything crashed.

Nevermind this. Let me just watch the course. If I could understand why its intent is with the skull I might be able to come up with some good solutions.

It seems the audio is broken. Let me reset.

11:50am. Now he is opening a new material linker tab despite it being open on the right side. This guy is somewhat inexperienced with both Houdini and Clarisse. But maybe I'll learn something from him. At this point, I am thinking that maybe there will be no point to him using Nuke after all.

Let me watch the course in its entirety since I bothered getting it. Let me just watch part 5 and I will stop for breakfast.

12pm. I was wondering what AO was for, but it seems it is for game engines. Yeah, I know what ambient occlussion is, but I was wondering why explicit maps for it were necessary and never saw a difference when using them. Now I have my answer.

He is showing textures from textures.com, but the free limit there is really low. Instead what I am going to do is use the V-Ray asset library that I got with it. That thing has plenty of stuff. Also the textures I got with Blender I should organize and back up in the asset library.

12:05pm. As an aside, if I am going to have the orangutan skull as a separate object, it was a mistake to put it in the same place as the heightfield. Right now is the ideal time to start importing things into Solaris. But I'll defer that until I come to an understanding of what he is trying to do with it.

Also, I just realized I forgot to add the noise at the top of the cliffs. This is because I was doing it from memory. The way I did the cliffs is to noise the whole layer, offset and scale it and then use the mask to combine it with the base. This is much better than the method he used which was to mask out the noise being added. Because it was centered he had to use max and chain multiple nodes to get something good, this is just pure spew.

* Add clipped top noise.

Let me leave this note.

I should do that before the errosion. Also there were some terraces that he hand painted that I did not do, but those do not matter.

12:10pm. Oh, I did not know it is possible to drag and drop textures directly into the slots. That is cool.

12:15pm. Why are both normal and displacement maps necessary? I've been wondering about this as well.

12:25pm. This was a pretty basic texturing tutorial. I had no idea that it is possible to increase the tesselation of the sphere without modifying its rows and cols.

Let me stop here. It is time for breakfast. It is very light, so I doubt I'll have trouble finishing the course today.

2:15pm. Done with breakfast and chores. Let me finish the chapter of Otome Survival and I will start.

2:20pm. Let me start.

Life should be lived according to a sense of freedom. My power should come from manifesting my designs. Today it shall be 3d, tomorrow it will be something else.

The traveling the path to omnipotence is a journey. I won't bother sprinting or being anxious about other people overtaking me. I should just do it at my own pace. What is the point of setting goals if you can't reach them, nor the world even caring if you reach them?

I've learned from roguelikes that you should always fight like a coward. I didn't want to accept that I should live like a coward because that would mean having to break my few relationships, but they were broken in the end, so the lesson is that I should have done it earlier. Delusions cannot be maintained forever. That weak heart of mine should perish. I feel pain, but one day I will overcome my obsessions.

2:25pm. Doing art should be like playing a game. I've tried far too hard to grasp things out of my reach, but in the end what has that gotten me. The trading skills I cannot use. The programming skills are something that I'd rather not rely on for making money. I'd rather be a charlatan and a fraud than continue living in such a disadvantageous position.

Just what is the point of being alone if the skills I have won't support such a lifestyle. If I had to live like this wouldn't it be better to cultivate in a way appropriate for it?

One trend that is working in my favor is that as time goes on, art gets increasingly more technical in nature. This is quite similar to warfare.

Nobody takes people drawing oils on paper seriously, anymore that peasants with guns could go against a modern military.

2:30pm. Right now it is stressful, but a few years of skill development and I will just as good at art as I am at programming. At that point I will be free from financial burdens.

I have this NEET existence, so I might as well use it to its fullest effect.

Just what is there beyond trading, programming and art? Becoming a doctor? Yeah, I don't think so. After this I should be reasonably complete in terms of skill development as a human. So let me do it. The last run. Heaven's Key is waiting to be done.

Let me resume the course.

> One thing that is going to pay of when rendering in any engine is to render .tx files instead of .tif files.

He recommends converting them.

I had no idea you could just drag files into an exe in the Findows Explorer.

2:35pm. This is interesting. Is it really necessary to convert textures like this? Does it make things faster? Why is this the first time I am hearing about this?

If it is that important should the program do it on its own when leading them to RAM?

Now he is showing me how to replace hardcoded paths with variables. Clarisse has a Path Manager to automate this.

https://forums.chaos.com/forum/v-ray-for-3ds-max-forums/v-ray-for-3ds-max-general/73881-tx-texture-vs-jpg-tif-why-is-tx-slower-to-render

According to this .tx is actually less efficient.

///

TX isn't about making your image render faster, it's about being able to have more texture information than you could possible hold in your Ram as it dynamically loads in and out when required.

Unfortunately the process of loading the texture in and out will be slower than just having it in memory. but you can have 500GB of textures as tx and still rendering, try that with normal exr are 32gb of Ram.

///

I see...

https://forum.isotropix.com/viewtopic.php?f=5&t=5372

It seems Clarisse has an inbuilt converter.

https://vimeo.com/319342502
Clarisse Survival Kit: Conversion to .TX

Let me watch this.

2:55pm. Let me go gack to it. I got distracted with the .tx thing. I won't worry about this for the time being.

3:25pm. I've been trying to figure out how to smooth border for half an hour, but only then it occured to me that erode would get rid of those artefacts. How foolish of me. If it wasn't for times I get stuck like this, I'd be pretty fast. Well, I'll learn.

Let me go back to the video. Right now he is showing me how in My Downloads area on Isotropix site, there is a 2.5 Gb download of Clarisse examples. The equivalent of V-Ray's asset library.

I'll consider tracking that down later, for now let me just get on with it. I might now even need a commercial license to download this. It just another reason to open an account.

3:40pm. Ah, I see. I was wonder why groups when combiners exist, but groups can take in patterns rather than just objects.

3:50pm. He keep using combiners where instances would suffice for some reason.

I honestly doubt he will be adding more objects to them.

3:55pm. Done with 06. These tutorials so far have been very light. This is not hard stuff by any means. Let me move on to 07.

Focus me, let me do this. I'll deal with this course and move on to doing my own thing.

4:15pm. If he had left the height map as it were, he could have just exported it as an displacement map. In fact, I am a bit confused at what he is importing. I thought he had converted it to voluem. Let pause here, and I'll pay more attention to what he is doing at the start.

...Yeah, it is an obj, without the base for some reaosn. Had he not gone through some much effort to put the skull into the same geometry, he could have made things a lot easier on himself.

4:20pm. When I think of height fields, I really should be thinking of how to export them as an image. The terrain tutorial on the Houdini site did show me how to texture them, so it is a better reference for how to do this than the Gnomon workshop one. What Gnomon workshop will give me is some Clarisse experience.

I need to focus. What I am doing here is the most important of all.

So far: Oct,Nov,Dec,Jan,Feb...I am only my sixth month of art study already. That is 6.5 months gone by and I still haven't mastered the fundamentals.

Had I started with Clarisse from the start, I could have become an effective artist already. So my path was the opposite of what it should have been. Originally I did not put much stock into environments, but now that I can see their full potential, I want to grasp this. Because being good at them is something no other VN would do, and it would improve the quality greatly if I did.

It also meshes extremely well with the kind of stories Simulacrum arcs are with the world getting wrecked all the time.

4:30pm. I went through the art path in the wrong direction. This happened to me many times in programming. I could have just mastered Clarisse, never even touched Houdini and Blender and I could have become a very effective artist. But the opposite is not the case. With Blender and Houdini, all I can do is trivial one off stuff. A single building rather than a city.

I might not even do any modeling in the future and just end up putting lego blocks together. And I'd be a genius if I can put myself into such a position.

4:35pm. Now focus me. I'll try to watch the tutorial in its entirety today. One single day is worth being spent on this. After that I'll get to work on finishing the pool scene. It won't be impressive, but doing it properly will allow me to cover all the ground, art wise. After I finish it I will be mid 2/5 and all I will need is to properly refine my existing workflow to break into the pro level.

Rather than reordering the channels, he really should have exported the files as single channel ones. That would have made things easier than packing them into color channels.

4:45pm. Let me start skimming this stuff, it is not that interesting watching him do this. My focus is starting to waver.

4:55pm. Let me move on to 08. Let me just get this out of the way. I want to start work on my own stuff. I can always return to this course in the future.

5:10pm. Ah, come to think of it, if he has a mesh, then rather than exporting image files, he could have just had the attributes as point properties in Clarisse. That would have made things a lot easier.

Actually turning things into a mesh isn't a bad decision if you consider ease of use. This might be a stronger factor than trying to save hard drive space. With displacement you have to mess around with bounds and tesselation, none of which are factors if you just bring in the whole mesh as it is.

Right now I am looking at the skull at is looks very nice. This is because he tranfsered the various attributes to it, so it gets the benefits of texturing just from that. It is smart and better than doing it separately.

Had I been doing it, I'd want to go over the skull in Blender to plug the holes of the eyes and nose.

I could probably do that in Houdini as well by eplitting and then extruding down the y axis.

There is no need to worry about this thing.

Let me go back to the tutorial.

5:25pm. Focus me, let me move on to 09. I am not really paying attention at this point.

5:30pm. 09 is him just messing with volumes. I already know all this, let me move on to the next. 10 is on AOV and Exporting. After that comes the Nuke stuff. I'll pay attention to what he is doing there. I've never studied Nuke before, the closest I've come to compositing is while studying texturing in the past month in the COP context.

5:45pm. Finally on the last two. Time to check out what he is doing in Nuke. I probably won't bother with this as it would be easier to just render it all out at once.

Watching him change the night from day by just adjusting the gamma make me think that it might be worth doing that for my own image.

6pm. This kind of course is a bit of a waste of Clarisse's abilities. If it is a scene like this texturing it in Houdini would have been completely doable assuming the renderers weren't complete shit like they are now. I mean, all he did was use the masks and slapped some textures on them.

It not like the tutorial where there was a million stars and dozens of thousands of high poly trees.

Compositing in Nuke makes a lot more sense when you aren't working on an animation and the complexity is so high that it would take a week to re-render the scene.

Clarisse in particular is so fast that you can do all you need in the viewport. Let me investigate a bit why my saved rendered image was different from I could see in the Image View.

6:15pm. Why is Google coaxing me to donate to Ukraine as soon as I enter Mail? Let me activate my Isotropix account so I can post a question in the forum. I think that most likely Clarisse is doing some color correction in the viewport, but I do not know what it is.

Oh, this is really nice. Here is the 2.44gb example project and free assets. There is also the 5.5 Early Access. I'll stick with 5.0 for now, I do not want to risk wiping my licenses.

> A new Angie renderer is introduced. Much faster than the classic Clarisse renderer, it comes with both CPU and GPU rendering backends (GPU rendering is only available on NVidia GPUs, starting with Pascal models).

Pascal is a generation later than Maxwel, I think. I won't be able to use Angie with the GPU until I upgrade my rig.

6:30pm. I made that question. Sigh. Do I feel like starting now. Let me first check out that intersect. I am a bit curious about it now. Then...

7:35pm. Done with lunch. Let me chill a bit more. I am not going to do any shading work today, but I think I will try exporting the Houdini scene and assigning some groups. To be honest, I do feel like just closing it here right now. I am not motivated to do anything more for the day.

7:45pm. Let me leave Otome Survival for later. I am getting into it, but let me deal with the scene.

7:50pm. Is Solaris shitting itself while importing the obj context? It appears so.

Forget this. Let me try importing it without the vines and the pool water. I'll have to start paring things down. If it comes down to it, I'll just export all the assets separately and merge them back together in Clarisse.

It worked. Let me try exporting it.

It works just fine. Let me also import the vines as a separate object.

I had to force close Houdini again. It seems that the vines are so demanding it literally can't import them into stage from the obj context. I guess I'll have to bring them into Clarisse as cloud points and instance them as such.

8:10pm. Let me close here. My curiosity has been satisfied. USD importing works just fine.

What I am going to do tomorrow is separate out the objects in the stage context and name them properly. That will allow me to work on them in Clarisse.

In SOP import I can dive into objects, right? ...Of course. It would be stranger if I could not.

Yeah, that is good. I'll separate out all the relevant parts of the scene and work on them that way.

One good aspect of being able to do my work in Clarisse is that I will be able to ditch the low poly versions of the assets. I only did them because the burden on Houdini would have been too much, but to Clarisse this kind of burden would be nothing.

8:20pm. The whole Houdini is a mess and after I finish the extraction I probably won't want to touch the scene again because of that. Clarisse offers me a much better workflow. Blender and Houdini will just be my geometry workhorses from here on out."

---
## [der-lyse/newsboat](https://github.com/der-lyse/newsboat)@[dbbaa664f1...](https://github.com/der-lyse/newsboat/commit/dbbaa664f105be14058462ca98ad634586d816da)
#### Thursday 2022-03-17 20:36:31 by Lysander Trischler

Remove trailing whitespace

Trailing whitespace is not harmful, but unnecessary and ugly in my
opinion. I configured my editor to highlight it, so I see it all the
time, which is a bit annoying. Let's get rid of it.

Actually regenerating the filter produces some slightly different code
with my installed version of cococpp (Coco/R Jan 02, 2012), so I just
kept the old code and removed the trailing spaces and tabulators.

---
## [avar/git](https://github.com/avar/git)@[c9ca821ae7...](https://github.com/avar/git/commit/c9ca821ae74a0e22008082cff530accbf329e8a0)
#### Thursday 2022-03-17 21:21:26 by Ævar Arnfjörð Bjarmason

object-file.c: do fsync() and close() before post-write die()

Change write_loose_object() to do an fsync() and close() before the
oideq() sanity check at the end. This change re-joins code that was
split up by the die() sanity check added in 748af44c63e (sha1_file: be
paranoid when creating loose objects, 2010-02-21).

I don't think that this change matters in itself, if we called die()
it was possible that our data wouldn't fully make it to disk, but in
any case we were writing data that we'd consider corrupted. It's
possible that a subsequent "git fsck" will be less confused now.

The real reason to make this change is that in a subsequent commit
we'll split this code in write_loose_object() into a utility function,
all its callers will want the preceding sanity checks, but not the
"oideq" check. By moving the close_loose_object() earlier it'll be
easier to reason about the introduction of the utility function.

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [kleinesfilmroellchen/serenity](https://github.com/kleinesfilmroellchen/serenity)@[62a97e1272...](https://github.com/kleinesfilmroellchen/serenity/commit/62a97e1272d5759db629a8014ec47403041ab346)
#### Thursday 2022-03-17 22:04:23 by kleines Filmröllchen

LibAudio+Userland: Use new audio queue in client-server communication

Previously, we were sending Buffers to the server whenever we had new
audio data for it. This meant that for every audio enqueue action, we
needed to create a new shared memory anonymous buffer, send that
buffer's file descriptor over IPC (+recfd on the other side) and then
map the buffer into the audio server's memory to be able to play it.
This was fine for sending large chunks of audio data, like when playing
existing audio files. However, in the future we want to move to
real-time audio in some applications like Piano. This means that the
size of buffers that are sent need to be very small, as just the size of
a buffer itself is part of the audio latency. If we were to try
real-time audio with the existing system, we would run into problems
really quickly. Dealing with a continuous stream of new anonymous files
like the current audio system is rather expensive, as we need Kernel
help in multiple places. Additionally, every enqueue incurs an IPC call,
which are not optimized for >1000 calls/second (which would be needed
for real-time audio with buffer sizes of ~40 samples). So a fundamental
change in how we handle audio sending in userspace is necessary.

This commit moves the audio sending system onto a shared single producer
circular queue (SSPCQ) (introduced with one of the previous commits).
This queue is intended to live in shared memory and be accessed by
multiple processes at the same time. It was specifically written to
support the audio sending case, so e.g. it only supports a single
producer (the audio client). Now, audio sending follows these general
steps:
- The audio client connects to the audio server.
- The audio client creates a SSPCQ in shared memory.
- The audio client sends the SSPCQ's file descriptor to the audio server
  with the set_buffer() IPC call.
- The audio server receives the SSPCQ and maps it.
- The audio client signals start of playback with start_playback().
- At the same time:
  - The audio client writes its audio data into the shared-memory queue.
  - The audio server reads audio data from the shared-memory queue(s).
  Both sides have additional before-queue/after-queue buffers, depending
  on the exact application.
- Pausing playback is just an IPC call, nothing happens to the buffer
  except that the server stops reading from it until playback is
  resumed.
- Muting has nothing to do with whether audio data is read or not.
- When the connection closes, the queues are unmapped on both sides.

This should already improve audio playback performance in a bunch of
places.

Implementation & commit notes:
- Audio loaders don't create LegacyBuffers anymore. LegacyBuffer is kept
  for WavLoader, see previous commit message.
- Most intra-process audio data passing is done with FixedArray<Sample>
  or Vector<Sample>.
- Improvements to most audio-enqueuing applications. (If necessary I can
  try to extract some of the aplay improvements.)
- New APIs on LibAudio/ClientConnection which allows non-realtime
  applications to enqueue audio in big chunks like before.
- Removal of status APIs from the audio server connection for
  information that can be directly obtained from the shared queue.
- Split the pause playback API into two APIs with more intuitive names.

I know this is a large commit, and you can kinda tell from the commit
message. It's basically impossible to break this up without hacks, so
please forgive me. These are some of the best changes to the audio
subsystem and I hope that that makes up for this :yaktangle: commit.

:yakring:

---
## [postgres/postgres](https://github.com/postgres/postgres)@[ec62cb0aac...](https://github.com/postgres/postgres/commit/ec62cb0aac5ba31a82339606009ddbd7eb00e2ac)
#### Thursday 2022-03-17 22:18:49 by Tom Lane

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
## [dpanjali/dpanjali](https://github.com/dpanjali/dpanjali)@[9007ff1b7b...](https://github.com/dpanjali/dpanjali/commit/9007ff1b7b56451db7d5829950bf908edd641849)
#### Thursday 2022-03-17 22:31:09 by dpanjali

index.md

👋 Hi, I’m @dpanjali! I am student at the University of Auckland, majoring in Statistics. This is a new learning journey for me so please bear with me as I might be a bit inexpereicend. Hope you enjoy!

**This is _meme_ I made for the first time!**



![my_meme](https://user-images.githubusercontent.com/100880633/158904053-e3c63695-a20b-4303-beea-b649db4ef89d.png)


**These are the codes I used to make this meme:**

![Screen Shot 2022-03-18 at 11 26 31 AM](https://user-images.githubusercontent.com/100880633/158904488-7ce76655-c709-4655-8865-e3405f33519a.png)


A really short and unhelpful summary of my inspiration for the meme is:
- As a statistician I struggle with this everyday!! So decided to make a meme on it :)

---
## [Ewwmewgewd/tgstation](https://github.com/Ewwmewgewd/tgstation)@[906fb0682b...](https://github.com/Ewwmewgewd/tgstation/commit/906fb0682bab6a0975b45036001c54f021f58ae7)
#### Thursday 2022-03-17 22:51:19 by necromanceranne

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
## [bobgeorgethe3rd/freesewing](https://github.com/bobgeorgethe3rd/freesewing)@[67da7dd595...](https://github.com/bobgeorgethe3rd/freesewing/commit/67da7dd5950f3e3ed39a190c23f3cd8b095cd93f)
#### Thursday 2022-03-17 23:07:12 by Joost De Cock

feat(lab): First stab at custom layout

This adds a React component to handle custom layouts.
This React component is a long way from perfect, but it's a start.

There are two reasons that (at least in my opinion) implementing this is non-trivial:

1) React re-render vs DOM updates

   For performance reasons, we can't re-render with React when the user drags a
   pattern part (or rotates it). It would kill performance.
   So, we don't re-render with React upon dragging/rotating, but instead manipulate
   the DOM directly.

   So far so good, but of course we don't want a pattern that's only correctly laid
   out in the DOM. We want to updat the pattern gist so that the new layout is stored.
   For this, we re-render with React on the end of the drag (or rotate).

   Handling this balance between DOM updates and React re-renders is a first contributing
   factor to why this component is non-trivial

2) SVG vs DOM coordinates

   When we drag or rotate with the mouse, all the events are giving us coordinates of
   where the mouse is in the DOM.

   The layout uses coordinates from the embedded SVG which are completely different.
   So we need to make this translation and that adds complexity.

3) Part-level transforms

   It's not just that the DOM coordinates and SVG coordinate system is different, each
   part also has it's own transforms applied and because of this behaves as if they have
   their own coordinate system.

   In other words, a point (0,0) in the part is not the top-left corner of the page.
   In the best-case scenario, it's the top-left corner of the part. But even this is
   often not the case as parts will have transforms applied to them.

4) Flip along X or Y axis

   Parts can be flipped along the X or Y axis to facilitate a custom layout.
   This is handled in a transform, so the part's coordinate's don't actually change. They
   are flipped late into the rendering process (by the browser displaying the SVG).

   Handling this adds yet more mental overhead

5) Bounding box

   While moving and rotating parts around is one thing. Recalculating the bounding box
   (think auto-cropping the pattern) gets kinda complicated because of the reasons
   outlined above.

   We are currently handling a lot in the frontend code. It might be more elegant to move
   some of this to core. For example, core expects the custom layout to set the widht and height
   rather than figuring it out on its own as it does for auto-generated layouts.

 Known issues

 - Rotating gets a little weird sometimes as the part rotates around it's center in the
   SVG coordinate system, but the mouse uses it's own coordinates as the center point that's
   used to calculate the angle of the rotation

 - Moving parts into the negative space (minus X or Y coordinated) does not extend the bounding box.

 - Rotation gets weird when a part is mirrored

 - The bounding box update when a part is rotated is not entirely accurate

I've sort of left it at this because I'm starting to wonder if we should perhaps re-think
how custom layouts are supported in the core. And I would like to discuss this with the core team.

---

