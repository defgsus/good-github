## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-05-28](docs/good-messages/2022/2022-05-28.md)


1,471,449 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,471,449 were push events containing 2,127,504 commit messages that amount to 121,120,407 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 31 messages:


## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[f782e45fd0...](https://github.com/cockroachdb/cockroach/commit/f782e45fd0da015396bc758e855535a951f2e21a)
#### Saturday 2022-05-28 00:15:55 by Andrei Matei

util/timeutil: don't strip mono time in timeutil.Now

Our timeutil.Now() insists on returning UTC timestamps, for better or
worse. It was doing this by calling time.Now.UTC(). The rub is that the
UTC() call strips the monotonic clock reading from the timestamp.
Despite repeatedly trying ([1]), I've failed to find any reasonable
reason for that behavior. To work around it, this patch does unsafe
trickery to get a UTC timestamp without stripping the monos.

Stripping the monos has the following downsides:
1. We lose the benefits of the monotonic clock reading.
2. On OSX, only the monotonic clock seems to have nanosecond resolution. If
we strip it, we only get microsecond resolution. Besides generally sucking,
microsecond resolution is not enough to guarantee that consecutive
timeutil.Now() calls don't return the same instant. This trips up some of
our tests, which assume that they can measure any duration of time.
3. time.Since(t) does one less system calls when t has a monotonic reading,
making it twice as fast as otherwise:
https://cs.opensource.google/go/go/+/refs/tags/go1.17.2:src/time/time.go;l=878;drc=refs%2Ftags%2Fgo1.17.2

An alternative considered was setting the process' timezone to UTC in an
init(): time.Local = time.UTC. That has downsides: it makes cockroach
more unpleasant to link as a library, and setting the process timezone
makes the timestamps not roundtrip through marshalling/unmarshalling
(see [1]).

[1] https://groups.google.com/g/golang-nuts/c/dyPTdi6oem8

---
## [Dmeto/tgstation](https://github.com/Dmeto/tgstation)@[cd294e9040...](https://github.com/Dmeto/tgstation/commit/cd294e9040505e73e46384d6166015afa43217f3)
#### Saturday 2022-05-28 00:43:54 by vincentiusvin

Scipaper rebalancing: Nitrium and halon shell removal. Nitrous added. Emphasis on BZ. (#66738)

Similar in spirit to #65707, with some more changes.

Restructured the gaseous experiments to:

    Nitrous (practice experiment)
    BZ (mainstay experiment)
    Hyper-Nob (lategame/once-in-a-while experiment)

Added a mining partner.

Moved adv weaponry lock to normal weaponry under reactionless. Toned down t3 reactionless.

BZ locks adv engi. Medbay unbridled by toxin gasses now.

Removed Xenobio's BZ Can.
Why It's Good For The Game

My original intent with papers was expanding the difficulty range of toxins. Both to things harder than tritium (nob, nitrium, etc) and also to things easier than tritium (bz, reactionless, etc).

In that process, I feel that i strayed a bit to the harder side, this PR is an attempt to tone down the overall difficulty of some of the gaseous experiments a notch.

Nitrous now takes place of the old BZ, BZ takes place of old nitrium/halon, and noblium stays because it's difficulty is in a pretty good spot for a relatively unimportant but nice to have tech.

While we're at it, I also added more emphasis to BZ production to toxins instead of tritium. This will hopefully incentivize people to try the department out. There is a risk of this being a bit of a chore, but I believe that the relevant atmos gameplay loop is strong enough to have it be fun. You need to check on the chamber, turn on pipes, adjust the input rate, and many more that makes it significantly more fun to do.

We do this by:

    Locking advanced engineering with BZ (organs and implants lock lifted). Depending on feedback i wont mind changing this around if you want to suggest another node as long as it's of similar or very slightly less importance.

    Getting rid of xeno's BZ can. Some xeno players need it for making slimes sleep, with their roundstart supply removed there should be a significant demand for the BZ production in toxins to go online asap.

If you have been paying attention to our PRs, i have been working to make BZ production as seamless and quick as possible in toxins. My five map prs #66454 #66198 #66064 #66010 #65857 have been building up to this. You can make BZ relatively quickly with the new freezer chamber in place. Probably even faster than ordering it in cargo, which is a fine ballpark to use if you want to make changes to it.

If you want to know how to operate it, here is a wiki guide in place https://tgstation13.org/wiki/User:Vincentius_vin/Sandbox#BZ_Synthesis. We will move it to the main toxins page once the rest of the page is finished, pictures are added, 

Made adv engi tech node require bz shells as an experiment, organs no longer need it.
Adv mining no longer requires adv engi.
Removed nitrium and halon shell, implant experiment lock lifted because of the former.
Relocked sec 1 tech node to need pressure bombs, sec 2 no longer needs tritium bomb.
Made advanced pressure bombs easier to do without funny fusion gases.
Added a new mining partner that accepts smaller (even non-atmos/non-ordnance related) bombs
Added more options to purchase nodes in the paper partners. Your point gain stays the same though.
Removed roundstart BZ can from xenobio.

---
## [andresuriza/Proyecto_II-Paintplus](https://github.com/andresuriza/Proyecto_II-Paintplus)@[841678894d...](https://github.com/andresuriza/Proyecto_II-Paintplus/commit/841678894df570e7b0f281e28e56214d6807e62d)
#### Saturday 2022-05-28 01:30:33 by andresuriza

Oversocialization can lead to low self-esteem, a sense of powerlessness, defeatism, guilt, etc. One of the most important means by which our society socializes children is by making them feel ashamed of behavior or
speech that is contrary to society’s expectations. If this is overdone, or if a particular child is especially susceptible to such feelings, he ends by feeling ashamed of HIMSELF. Moreover the thought and the behavior of the oversocialized person are more restricted by society’s expectations than are those of the lightly socialized person. The majority of people engage in a significant amount of naughty behavior. They lie, they commit petty thefts, they break traffic laws, they goof off at work, they hate someone, they say spiteful things or they use some underhanded trick to get ahead of the other guy. The oversocialized person cannot do these things, or if he does do them he generates
in himself a sense of shame and self-hatred. The oversocialized person cannot even experience, without guilt, thoughts or feelings that are contrary to the accepted morality; he cannot think “unclean” thoughts. And socialization is not just a matter of morality; we are socialized to
conform to many norms of behavior that do not fall under the heading of morality. Thus the oversocialized person is kept on a psychological leash and spends his life running on rails that society has laid down for him. In many oversocialized people this results in a sense of constraint and powerlessness that can be a severe hardship. We suggest
that oversocialization is among the more serious cruelties that human being inflict on one another.

---
## [andreimatei/cockroach](https://github.com/andreimatei/cockroach)@[f6cc7f575c...](https://github.com/andreimatei/cockroach/commit/f6cc7f575cd374982752af6909d3efa96908c3dd)
#### Saturday 2022-05-28 01:49:39 by craig[bot]

Merge #81409

81409: bazel: upgrade to rules_nodejs 5.4.2 r=rickystewart,nathanstilwell,laurenbarker a=sjbarag

Please forgive the massive second commit — there's very few valid states in this progression, as building, linting, and testing either work or they don't.  There's not much sense in intentionally leaving commits around that won't build in my opinion, as it makes bisecting extremely frustrating.  If anyone disagrees, let me know and I can keep digging for an intermediate state!

----

Upgrading to Bazel's rules_nodejs 5.x exposed a flaw in our previous Bazel integration: because rules_nodejs explicitly doesn't support yarn's "workspaces" feature [1] (in which common dependencies are hoisted to the lowest common parent directory), any NPM dependencies with different major versions between db-console and cluster-ui would
get flattened to a single version. This left one of those packages using an unsupported (and un-requested) version of a dependency. Removing the yarn workspace layout and using separate Bazel repositories for each JS project ensured each project received the correct dependencies, but revealed incompatibilities with the requested versions. Upgrade rules_nodejs to the latest released version, remove yarn workspaces from the pkg/ui/ tree, and fix all revealed compatibility issues.

Co-authored-by: Sean Barag <barag@cockroachlabs.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[245ec35dae...](https://github.com/tgstation/tgstation/commit/245ec35dae59d0edc92663ccb8012b27d5e1a198)
#### Saturday 2022-05-28 02:32:25 by LemonInTheDark

Removes (in) smoke and foam reactions (#67270)

* Removes smoke and foam reactions

Turns out when you let reagents react in foam/smoke, people put bombs in
them.

This behavior was initially added to just smoke, accidentially in
(56f7ac0c0a29e8f898c4aab35947d027952b43f7) accidentialy (thalpy tried to
make both foam and smoke instant react, but instead made smoke's temporary
holder reagent instant instead. hhhhhhh)

Assuming this was intentional it was then extended to foam in
(1879e2d338c9bf5f191cef6c39944b26a41e6092)

Basically, we're idiots. Anyway lets just walk this all back to instant
reaction on smoke/foam formation. Hate you people

* Removes another source of gunpowder smoke

Temporal told me about this. Gunpowder uses an ex_act signal as a
starter, and that also counts for smoke objects.

Really don't want instant detonation smoke bombs, so let's just... not
shall we?

---
## [Gullwing-door/restoration-mod](https://github.com/Gullwing-door/restoration-mod)@[db2e4bde78...](https://github.com/Gullwing-door/restoration-mod/commit/db2e4bde7896851d7a961169331ce18f0d09d612)
#### Saturday 2022-05-28 03:13:36 by Noep

fuck

idiot moron forgets the winchester barrels affect tube length and the copypasta barrel stats won't have that shit on them

---
## [newstools/2022-daily-post-nigeria](https://github.com/newstools/2022-daily-post-nigeria)@[c3001a0a3a...](https://github.com/newstools/2022-daily-post-nigeria/commit/c3001a0a3a8f46943a75bc2827219e80f4237e43)
#### Saturday 2022-05-28 03:43:11 by Billy Einkamerer

Created Text For URL [dailypost.ng/2022/05/27/kwara-man-hacks-brother-to-death-in-bloody-fight/]

---
## [Mojave-Sun/mojave-sun-13](https://github.com/Mojave-Sun/mojave-sun-13)@[2996f41136...](https://github.com/Mojave-Sun/mojave-sun-13/commit/2996f41136fcd4dee419b4138e45ae65df9529f6)
#### Saturday 2022-05-28 04:27:14 by EdwardNashton

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
## [VoltageOS-Devices/android_kernel_xiaomi_lavender](https://github.com/VoltageOS-Devices/android_kernel_xiaomi_lavender)@[a938b43afa...](https://github.com/VoltageOS-Devices/android_kernel_xiaomi_lavender/commit/a938b43afab7eca662afd122b4677a76e246ba75)
#### Saturday 2022-05-28 05:11:32 by Maciej Żenczykowski

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
## [lyubomyr-shaydariv/git](https://github.com/lyubomyr-shaydariv/git)@[bdaf1dfae7...](https://github.com/lyubomyr-shaydariv/git/commit/bdaf1dfae71fdf120fc7253e713ccf0a06cc5558)
#### Saturday 2022-05-28 05:59:23 by Tao Klerks

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
## [crowlogic/arb4j](https://github.com/crowlogic/arb4j)@[01852b2e64...](https://github.com/crowlogic/arb4j/commit/01852b2e64b8052a8e2c6b1631b97d7af5080ca7)
#### Saturday 2022-05-28 07:16:56 by Stephen Crowley

disable the damn fucking son of a bitching shitass heap bullshit this is
why i fucking always hated C for this very reason christ on a stick.
FUCK

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[ffffe16e79...](https://github.com/treckstar/yolo-octo-hipster/commit/ffffe16e79914a1a35f6da5005700bc4c01dc9bb)
#### Saturday 2022-05-28 07:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [awesome-github-repo/Auxio](https://github.com/awesome-github-repo/Auxio)@[c6d7d8fe39...](https://github.com/awesome-github-repo/Auxio/commit/c6d7d8fe39ae0f84051482961c3d2ad5ae64137a)
#### Saturday 2022-05-28 07:41:17 by OxygenCobalt

playback: implement "safe" slider wrapper

Implement a safe slider wrapper that does not crash with invalid values
as often.

Slider is a terrible component that is not designed with Auxio's
use-case in the slightest. Instead of gracefully degrading with invalid
values, it just crashes the entire app, which is horrible for UX.

Since SeekBar is a useless buggy version-specific sh******ed mess too,
we have no choice but to wrap Slider in a safe view layout that
hopefully hacks with the input enough to not crash the app when doing
simple seeking actions.

I hate android so much.

Resolves #140.

---
## [KuzscoTech/NGCP_Embedded_SDK](https://github.com/KuzscoTech/NGCP_Embedded_SDK)@[3b4ec2a323...](https://github.com/KuzscoTech/NGCP_Embedded_SDK/commit/3b4ec2a3231960aad9de03050a294d424b6c9b79)
#### Saturday 2022-05-28 08:55:59 by George Yu

the night before demo day

- pain misery suffering
- all manual controls working with pi

---
## [skiminki/Stockfish](https://github.com/skiminki/Stockfish)@[cb9c2594fc...](https://github.com/skiminki/Stockfish/commit/cb9c2594fcedc881ae8f8bfbfdf130cf89840e4c)
#### Saturday 2022-05-28 09:31:49 by Tomasz Sobczyk

Update architecture to "SFNNv4". Update network to nn-6877cd24400e.nnue.

Architecture:

The diagram of the "SFNNv4" architecture:
https://user-images.githubusercontent.com/8037982/153455685-cbe3a038-e158-4481-844d-9d5fccf5c33a.png

The most important architectural changes are the following:

* 1024x2 [activated] neurons are pairwise, elementwise multiplied (not quite pairwise due to implementation details, see diagram), which introduces a non-linearity that exhibits similar benefits to previously tested sigmoid activation (quantmoid4), while being slightly faster.
* The following layer has therefore 2x less inputs, which we compensate by having 2 more outputs. It is possible that reducing the number of outputs might be beneficial (as we had it as low as 8 before). The layer is now 1024->16.
* The 16 outputs are split into 15 and 1. The 1-wide output is added to the network output (after some necessary scaling due to quantization differences). The 15-wide is activated and follows the usual path through a set of linear layers. The additional 1-wide output is at least neutral, but has shown a slightly positive trend in training compared to networks without it (all 16 outputs through the usual path), and allows possibly an additional stage of lazy evaluation to be introduced in the future.

Additionally, the inference code was rewritten and no longer uses a recursive implementation. This was necessitated by the splitting of the 16-wide intermediate result into two, which was impossible to do with the old implementation with ugly hacks. This is hopefully overall for the better.

First session:

The first session was training a network from scratch (random initialization). The exact trainer used was slightly different (older) from the one used in the second session, but it should not have a measurable effect. The purpose of this session is to establish a strong network base for the second session. Small deviations in strength do not harm the learnability in the second session.

The training was done using the following command:

python3 train.py \
    /home/sopel/nnue/nnue-pytorch-training/data/nodes5000pv2_UHO.binpack \
    /home/sopel/nnue/nnue-pytorch-training/data/nodes5000pv2_UHO.binpack \
    --gpus "$3," \
    --threads 4 \
    --num-workers 4 \
    --batch-size 16384 \
    --progress_bar_refresh_rate 20 \
    --random-fen-skipping 3 \
    --features=HalfKAv2_hm^ \
    --lambda=1.0 \
    --gamma=0.992 \
    --lr=8.75e-4 \
    --max_epochs=400 \
    --default_root_dir ../nnue-pytorch-training/experiment_$1/run_$2

Every 20th net was saved and its playing strength measured against some baseline at 25k nodes per move with pure NNUE evaluation (modified binary). The exact setup is not important as long as it's consistent. The purpose is to sift good candidates from bad ones.

The dataset can be found https://drive.google.com/file/d/1UQdZN_LWQ265spwTBwDKo0t1WjSJKvWY/view

Second session:

The second training session was done starting from the best network (as determined by strength testing) from the first session. It is important that it's resumed from a .pt model and NOT a .ckpt model. The conversion can be performed directly using serialize.py

The LR schedule was modified to use gamma=0.995 instead of gamma=0.992 and LR=4.375e-4 instead of LR=8.75e-4 to flatten the LR curve and allow for longer training. The training was then running for 800 epochs instead of 400 (though it's possibly mostly noise after around epoch 600).

The training was done using the following command:

The training was done using the following command:

python3 train.py \
        /data/sopel/nnue/nnue-pytorch-training/data/T60T70wIsRightFarseerT60T74T75T76.binpack \
        /data/sopel/nnue/nnue-pytorch-training/data/T60T70wIsRightFarseerT60T74T75T76.binpack \
        --gpus "$3," \
        --threads 4 \
        --num-workers 4 \
        --batch-size 16384 \
        --progress_bar_refresh_rate 20 \
        --random-fen-skipping 3 \
        --features=HalfKAv2_hm^ \
        --lambda=1.0 \
        --gamma=0.995 \
        --lr=4.375e-4 \
        --max_epochs=800 \
        --resume-from-model /data/sopel/nnue/nnue-pytorch-training/data/exp295/nn-epoch399.pt \
        --default_root_dir ../nnue-pytorch-training/experiment_$1/run_$run_id

In particular note that we now use lambda=1.0 instead of lambda=0.8 (previous nets), because tests show that WDL-skipping introduced by vondele performs better with lambda=1.0. Nets were being saved every 20th epoch. In total 16 runs were made with these settings and the best nets chosen according to playing strength at 25k nodes per move with pure NNUE evaluation - these are the 4 nets that have been put on fishtest.

The dataset can be found either at ftp://ftp.chessdb.cn/pub/sopel/data_sf/T60T70wIsRightFarseerT60T74T75T76.binpack in its entirety (download might be painfully slow because hosted in China) or can be assembled in the following way:

Get the https://github.com/official-stockfish/Stockfish/blob/5640ad48ae5881223b868362c1cbeb042947f7b4/script/interleave_binpacks.py script.
Download T60T70wIsRightFarseer.binpack https://drive.google.com/file/d/1_sQoWBl31WAxNXma2v45004CIVltytP8/view
Download farseerT74.binpack http://trainingdata.farseer.org/T74-May13-End.7z
Download farseerT75.binpack http://trainingdata.farseer.org/T75-June3rd-End.7z
Download farseerT76.binpack http://trainingdata.farseer.org/T76-Nov10th-End.7z
Run python3 interleave_binpacks.py T60T70wIsRightFarseer.binpack farseerT74.binpack farseerT75.binpack farseerT76.binpack T60T70wIsRightFarseerT60T74T75T76.binpack

Tests:

STC: https://tests.stockfishchess.org/tests/view/6203fb85d71106ed12a407b7
LLR: 2.94 (-2.94,2.94) <0.00,2.50>
Total: 16952 W: 4775 L: 4521 D: 7656
Ptnml(0-2): 133, 1818, 4318, 2076, 131

LTC: https://tests.stockfishchess.org/tests/view/62041e68d71106ed12a40e85
LLR: 2.94 (-2.94,2.94) <0.50,3.00>
Total: 14944 W: 4138 L: 3907 D: 6899
Ptnml(0-2): 21, 1499, 4202, 1728, 22

closes https://github.com/official-stockfish/Stockfish/pull/3927

Bench: 4919707

---
## [darshan-/PurpOS](https://github.com/darshan-/PurpOS)@[409940f9a5...](https://github.com/darshan-/PurpOS/commit/409940f9a57595ae66dd89b12abda243e13b6d5e)
#### Saturday 2022-05-28 12:14:07 by Darshan-Josiah Barber

I'm having a really hard time getting things going on real hardware.  Finally worked out bochs.  Which is awful, stupid, and a pain in the butt.  But it's also seemingly having the same issue as my old Compaq Presario R4000, which makes it a faster and easier way to try things that will hopefully help.  And I can have at least a little insight into what's going on.  So this is a huge mess, but it's a huge mess I don't want to lose, so committing it.

---
## [StarStation13/StarStation13](https://github.com/StarStation13/StarStation13)@[ce0aff7526...](https://github.com/StarStation13/StarStation13/commit/ce0aff7526158133acd1b53bd5d2d9d6ac9578f3)
#### Saturday 2022-05-28 13:18:44 by GoldenAlpharex

Fixed Icebox's lower two z-levels not being included in the Map Compile action (#66503)

Did you know that you could currently put a bunch of random shit in the lower levels of icebox and the map compile would be none the wiser?

I sure did.

I hate that it's done manually this way, but honestly it's not worth refactoring the whole action to make it work differently.

Ensuring that the lower levels work properly is, in fact, a good thing.

---
## [Mudasir028/ucfparking](https://github.com/Mudasir028/ucfparking)@[2e74793527...](https://github.com/Mudasir028/ucfparking/commit/2e74793527fb9b3792047fe0693f240b952de608)
#### Saturday 2022-05-28 13:41:31 by mudasir028

include of these chances:
For the "Next Data Update", we'll need to have a countdown going down for each hour and a minute (00:01, 01:01, 02:01, etc.), so it should be HH : MM : SS.

Also, I think the "X" values on the last 24h line graph are not correct. It seems like they are opposite
I want it to go from Left to Right
with Right being the newest and left being the oldest

*The final thing is we're going to have to change the times from UTC to EST. So we will have to convert it on the site's end.

So this is actually done every 6 hours. So just make it go to the 1st minute of every 6 hours (00:01:00, 06:01:00, etc.), like how the next data update is.

On the filter button, can you please add an icon for the dropdown? Like an upside down triangle to indicate it is a dropdown menu? Possibly have it change depending if the menu is opened or closed, if closed, upside down triangle, if open, upside triangle.

Yeah it auto changes depending on your system settings.

https://gyazo.com/fc4dfd84e29046fcef14897d0a2800f0
You can see how it works here

A working Google search clone made with Next.js & Tailwind CSS. - GitHub - jakeva/google-search-clone: A working Google search clone made with Next.js & Tailwind CSS.

We are also going to need a dark mode. It should auto change depending on the system's preferences, like my other site:
https://google.jakevalenzuela.com/
Source code is here (if you need to look at how I do it):
https://github.com/jakeva/google-search-clone
GitHub - jakeva/google-search-clone: A working Google search clone made with Next.js & Tailwind CSS.

For the "Next Prediction Update", feel free for now to just put it at "N/A" since I'm not too sure how often we'll do this

And here the "Available Spaces" should be "Garage X Available Spaces" so like "Garage A Available Spaces"

---
## [asd9176506911298/Android-Mod-Menu](https://github.com/asd9176506911298/Android-Mod-Menu)@[3595e6dfaa...](https://github.com/asd9176506911298/Android-Mod-Menu/commit/3595e6dfaa0cd42f96d6cb081965b56571684ebe)
#### Saturday 2022-05-28 15:08:31 by LGLTeam

Updated 2.0

DO NOT UPDATE if you are not prepared. You will need to read README again when you use this update

Changelog:
- Updated gradle and NDK target
- Can now force loading menu while waiting for the lib to be loaded
- Add saving logcat to file. It can be useful to diagnose the issues within the mod
- A rework of feature list. Now you must assign feature numbers manually. The benefit is you can easly remember the numbers and you don't need to re-order your Changes anymore when you remove/add/re-order your features. Feature numbers can be like 1,3,200,10... instead in order 0,1,2,3,4,5...
- Settings list has been moved to cpp. The numbers are assigned as negative
- Additional fixes for AIDE CMODs
- Updated README.md and README-MOBILE.md. Be sure to read it again
- Cleaned up codes again to stop the small kinderforum haters from hating us. You may notice some codes have been moved or removed
- Some minor fixes

Maybe there is more changes I forgot to list

To haters, stop using this template immediately and stop spreading hate please. There is no reason to hate. 95% of modders love this template already. To lovers, show us love by making videos of your cool mods with mod menu ❤️❤️❤️.

---
## [animeshbaranawal/Book48511](https://github.com/animeshbaranawal/Book48511)@[460b50698d...](https://github.com/animeshbaranawal/Book48511/commit/460b50698deb57c0e27b9030397b4ebd66f23696)
#### Saturday 2022-05-28 15:26:58 by Animesh Baranawal

Changes done to spellings use `se modernize-spelling`

    -> Moslem : Muslim
    -> dulness : dullness
    -> divers gambados : diverse gambados
    -> turtle-dove : turtledove
    -> fish-pond : fishpond
    -> summer-house : summerhouse
    -> love-sick : lovesick
    -> soft-heartedness : softheartedness
    -> book-case : bookcase
    -> roof-tree : rooftree
    -> thunder-cloud : thundercloud
    -> fulness : fullness
    -> sugar-cane : sugarcane
    -> battle-fields : battlefields
    -> night-time : nighttime
    -> Hindoos : Hindus (except when its in the title of a book in endnotes: View of the hindoos)
    -> eye-witness : eyewitness
    -> to-morrow : tomorrow
    -> story-book : storybook
    -> pál, pála : pal, pala
    -> iron-wood : ironwood
    -> cocoa-nut : coconut
    -> water-fowl : waterfowl
    -> wool-gathering : woolgathering
    -> by the bye : by the by
    -> fire-fly : firefly
    -> sugar-plums : sugarplums
    -> hobby-horse : hobbyhorse
    -> chess-board : chessboard
    -> to-night : tonight
    -> good-night : goodnight
    -> to-day : today
    -> counting-house : countinghouse
    -> loin-cloth: loincloth
    -> musk-rat : muskrat
    -> lamb-skin : lambskin
    -> lamp-black : lampblack
    -> new comers : newcomers
    -> shewed : showed
    -> mean time : meantime
    -> good-bye : goodbye
    -> cut-throats : cutthroats
    -> lack-lustre : lacklustre
    -> store-room : storeroom
    -> god-like : godlike
    -> short-sighted : shortsighted
    -> tom-cat : tomcat

---
## [Wallemations/heavenstation](https://github.com/Wallemations/heavenstation)@[e37591540b...](https://github.com/Wallemations/heavenstation/commit/e37591540b2620b7ad2a2b61734634d848e8eba2)
#### Saturday 2022-05-28 17:50:07 by san7890

[MDB Ignore] OH GOD OH FUCK OH SHIT OH LORD - SPACE AND RUINS IS BROKEN (#67324)

So, for the last few days on production, Space Ruin generation has refused to work. Why is this? It's because in #67107 (cfc233052885dd294b2e7e676caaf84a2a37592b), we repathed `/area/space`  to `/area/misc/space` (lol i should have paid attention to that) without updating everything in code to match. I couldn't seem to get `/area/misc/space` to properly work somehow (this could have also been something I was doing wrong), but I worked it back to just making everything vanilla `/area/space` and all of those unwanted behaviors should be squashed out. Let's get the game working again.

---
## [TomCummings07/ARWIN-Surveillance-Microphone](https://github.com/TomCummings07/ARWIN-Surveillance-Microphone)@[d5fc3a80a1...](https://github.com/TomCummings07/ARWIN-Surveillance-Microphone/commit/d5fc3a80a10cd206db9083aeb949b2811e711f98)
#### Saturday 2022-05-28 18:15:10 by Tom Cummings

Revert "'.blank' files added to ignore list."

This reverts commit d560f39aa7f4d58a929574bbf6041936dde9234a.

Note to self: if .blank files are ignored there is no fucking point in them is there. Stupid

---
## [SLASHEM-Extended/SLASHEM-Extended](https://github.com/SLASHEM-Extended/SLASHEM-Extended)@[49fb7eefcb...](https://github.com/SLASHEM-Extended/SLASHEM-Extended/commit/49fb7eefcb09bcb2462487a3773d3c68156bafe0)
#### Saturday 2022-05-28 18:20:33 by AmyBSOD

New stuff

To the person who wondered whether I was serious with the "amusing scenario for <name of that stupid tournament>":  yes. I'd not have told anyone that players who are on the blacklist would get an unplayable game, nor would I have revealed it after the tournament unless someone decided to remove my game from it permanently. But, well, as I said, that scenario was blown because my game was removed already, due to a server administator coercing bhaak into doing so.

Obviously, if I'd have secretly added that blacklist, the part where it says "you were on the blacklist" in the dumplog wouldn't have been included. The players in question are mainly ones who consider SLEX to be completely unbalanced anyway, and they believe that random player-hostile stuff happens constantly, so they would have gotten exactly what they expected, and confirmation bias would have made them go "ah, knew that variant sucked anyway, why even bother" instead of noticing that something is amiss. I'd have laughed and laughed watching both their attempts to play and the chat over in the hdf channel, but I wouldn't have said a word. And if anyone were to complain, I'd either have said "third-party complaints are not accepted" if it wasn't the blacklisted player itself filing the complaint, or "well maybe you should play better" if it was.

Now please make my pariah status official.

---
## [nmajask/Yogstation-But-Worse](https://github.com/nmajask/Yogstation-But-Worse)@[c3e823d052...](https://github.com/nmajask/Yogstation-But-Worse/commit/c3e823d052f6e07b6d1f571d0989c6305b53d5f6)
#### Saturday 2022-05-28 18:29:10 by Jamie D

Adds APC and different areas for the multiple air alarms.. why could you siphon interrogation from perma.. (#14163)

* Update Space_Station_13_areas.dm

* Fixes Brig to not be Shit

* Fixes Areastring

* other maps

* Update code/game/area/Space_Station_13_areas.dm

* Fucking hate baiomu so much

* fucking apc

---
## [nmajask/Yogstation-But-Worse](https://github.com/nmajask/Yogstation-But-Worse)@[8b77243ce9...](https://github.com/nmajask/Yogstation-But-Worse/commit/8b77243ce9da72645291d6f22f798bc32611a706)
#### Saturday 2022-05-28 18:29:10 by TheRyeGuyWhoWillNowDie

Makes bloodbrothers start with the makeshift weapons book learned. (Jamie Edition) (#14094)

* makes blood brothers a bit less shit

* oopsie

* improve???

* what

* huh??

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[e0242a1e8d...](https://github.com/mrakgr/The-Spiral-Language/commit/e0242a1e8d88b217c3436a0c87481563d4abb638)
#### Saturday 2022-05-28 18:33:12 by Marko Grdinić

"9:20am. Let me chill just a bit and then I will start.

9:50am. Let me start. Kouji's art has really gotten better in the latest doujin, it is quite impressive. It took him a while to get there. My own problem is that I am trying to skip stages and do 4/5 art with 2/5 skills.

I really need modeling practice in order to get better.

But before that, I need to establish my workflow properly. I should be able to do this once I see how Pablo does his magic. Focus me. Let me do this. I only have little bit more to go and then I am going to crush it.

10:05am. The 3d hatching brushes are interesting. They'd be useless in regular sculpting practice, but here they make sense. The way he sculpted the rocks is also next level compared to doing it in 2d.

To be honest, I want to get rid of the Houdini stuff. Even if I could do it with effort, if I started doing it in Houdini it would just end with me messing with nodes for an entire day. Like when I scattered those cylinders, I need to get a refresher how geo nodes work.

Hmmm, still if I hadn't needed to do that, geo node scattering would have been fast. I should not discard it yet.

10:10am. I am a fool for not recognizing what a remarkable gain in capability 3d is over 2d. If it was possible to work in higher dimensions than 3d, I bet the gains would be just as pronounced. Too bad humans cannot comprehend them.

10:25am. Oh, Zbrush's move brush has some option for preserving fibre mesh length.

10:30am. Interesting that he using Zmodeler to mask out polygroups.

10:40am. The thing he did with stacking fibremeshes just now is essentially what I've spent two months in Houdini for. He only made a single instance of a plant though, but maybe you don't need more than a few. Yeah, with me I do not know where ego starts and ends. I spent 70% of my art journey so far studying what I don't need.

10:45am. Focus me, stop reading the recent 1.1k votes ML thread. It is just people complaining about lack of compute. Focus on art.

10:50am. Finally done with day 3.

The next up are NPR filters and compositing. The last two days are what is really of interest to me, so let me get into it.

11:10am. https://youtu.be/u5wTPv6mzx8
Blender Addon Simply Concept

Let me just watch this. I tried googling illustration addons.

11:15am. Hmmm, I suppose it is interesting, though Zbrush would be better than that ddon. Voxelizing the model might make booleans easy, but it would make everything else hard.

Forget it. Let me take a short break and then I'll get back to day 4.

11:30am. Let me get back to it. Right now he is exaplaining what the rest of the course will cover. NPR filters come next.

11:50am. It might be a good idea to get Photoshop. It is likely to have better filters than CSP.

11:55am. 2.6gb. Let me get it off Persia just in case. I might end up never using it, but it won't hurt having it on my hard drive. It might end up like Mari or Marmoset, but that does not matter. Let me get back to the course. Right now he is putting me to sleep with composition talk.

12:10pm. Now he is explaining some weird Zbrush thing with the camera. I'd rather just stick to Blender.

One thing I've realized it that pure ref is really good at managing screenshots. I should get it later.

It am really tunning out right now. I do not want to know about the intricacies of the Zbrush camera. I want him to get on with it and get to how to do rendering and NPR filters.

12:20pm. I thought that Zbrush could be good for layouting, but I've changed my mind. The way it works is ridiculous.

12:30pm. I hate this part, I did not pay attention at all to it and actually skipped it till the end. Zbrush is crap for layouting.

You know what I want to do? I want to do a real time render and then use the lighting information as stroke density. It is like a bit what Substance Painter is doing except for 2d. I bet such an effect would be great.

I am thinking about Freestyle edges, and they won't be able to handle beveled corners. They'd be great for angular stuff, but not for charas.

2pm. I've finished breakfast a while ago and I am deep in thought.

I have some ideas, but they are leading me along certain lines. Why not try out NN style transfer? I actually completely forgot about that. I need at least one art skill to consider myself being serious at this craft, but after that it should be anything goes. Whether it be drawing or modeling, either is fine. But afterwards...

Let me finish the course, I really hope it picks up. I do not like the style he is teaching, but the thing he is doing with the matcap, that is a primitive take on style transfer. When pro artist take a real photo, cruch the midtons and make it grayscale, that is also style transfer.

2:10pm. Focus me, let me watch the course.

https://github.com/racinmat/anime-style-transfer

Hmmmm...it might be worth looking into.

https://reiinakano.com/arbitrary-image-stylization-tfjs/

Forget the course for a bit, let me try this out. Also, maybe I'll have run, I am starting to hear thunder outside.

Will it accept a huge 1k image like the one I have? Nope, it downscales them.

2:20pm. https://magenta.tensorflow.org/studio

Music plugins based on NNs? That is interesting. Damn it, the weather is really turning for the worse. And my downloads have at least 30m left.

2:25pm. Let me close here. Forget Photoshop. I'll pick it up later. I can't oppose the weather, I might as well take a break here.

6:20pm. I was in bed for longer than I thought. I had a good long think. NPR rendering is definitely what the next step after modeling is. If necessary I should take the illustration shader and adapt it for the compositing step. I should get the Mangaka plugin and see how it does.

I should be making my own NPR plugins. All I need to distribute the strokes are the normal and lighting information. Optionally depth. And optionally object ids and freestyle lines for masks. I am actually in agreement with PBR renderers on what the lighting should be. If I need to crunch it, I can always do that in the compositing stage.

I admit I was wondering where my programming skills would come into 3d, and it will be in making NPR filters. That is important enough to warrant it. Instead of going at it by hand, making a program to scatter the strokes would be a much better idea.

6:30pm. For NNs style transfer I do not even need to look at it. There is no way those useless retards in the ML community would ever give me anything useful.

https://youtu.be/X8YkWdhty7I?t=859

EBSynth might be worth checking out though.

...Let me try Deep Dream Generator. Strange that it did not show up at the top of Google search. Google's search is really going to hell lately.

6:40pm. It is really taking it a while to process the file. If this works it could have some promise.

https://deepdreamgenerator.com/user-level-compute-energy

It seems it can in fact do full resolution. This could be interesting.

https://deepdreamgenerator.com/subscription/plans

It costs at least 19$ a month.

Let me go have lunch. Also let me turn off.

7:15pm. I am back again. Ok, so NN style transfer might be viable, but I'd need to have such a net on my own computer. No way will I accept using an online service for something integral to my workflow. If Deep Dream goes away, I can't stop being an artist because of that.

https://youtu.be/7xnbGWcE7wY
Non-Photorealistic Rendering (NPR) - U-Render Tutorial

Let me watch this, I want to see what U-Render has. Today's weather really messed up everything. I am not sure I feel like watching another course video right now.

It is a pity U-Render is C4D only.

7:35pm. Nwm. I really want to stop here, but let me watch the next part of the course just for a bit. Today was really wasted.

7:40pm. No I do not feel like it. Forget it. 7:40pm is no time to be studying. I'll do it properly tomorrow. Days like this happen a few times per year. Even though I was a in bed, I have a headache from all the thinking. I want to finish this course soon so I can move on to the next part of my journey.

I've decided - what I did with that couch last year was right. To get my own style all I need to do is automate it. Let me cap the day off by getting the Mangaka plugin.

8:10pm. Got it, I'll leave installing it for tomorrow. It is only 20k in size which comes to over 600 lines. What the hell, this is pretty much nothing.

8:15pm. Right now I am looking at the source, and I can't really tell what its functionality is. When I watched the vid it felt pretty fancy, but whatever it is doing it is rather simple.

I think I'll use it as a base when I do my scattering approach to strokes. Since it is only 4$ I am not going to regret my purchase.

8:25pm. Since I've started reading the Fable thread let me close for real. Tomorrow I am going to get Zbrush for Illustrators course out of the way. After that I will make it my goal to paint the room properly. Making my own NPR compositor node should be my goal. I have no idea how I am going to do that, but I will find out."

---
## [RoxanneShewchuk/SpaceXRAacdemy](https://github.com/RoxanneShewchuk/SpaceXRAacdemy)@[4673ccd6ac...](https://github.com/RoxanneShewchuk/SpaceXRAacdemy/commit/4673ccd6ac3626844912c0ecdbf0044712f4c63a)
#### Saturday 2022-05-28 18:47:25 by RoxanneShewchuk

Update README.md

Space XR Academy welcomes contributions from everyone who shares our goals and wants to contribute in a healthy and constructive manner within our community. We do our best to recognize, appreciate and respect the diversity of our global contributors. As such, we have adopted this code of conduct and require all those who participate to agree and adhere to these Community Participation Guidelines in order to help us create a safe and positive community experience for all.

These guidelines aim to support a community where all people should feel safe to participate, introduce new ideas and inspire others, regardless of:

Background
Family status
Gender
Gender identity or expression
Marital status
Sex
Sexual orientation
Native language
Age
Ability
Race and/or ethnicity
Caste
National origin
Socioeconomic status
Religion
Geographic location
Any other dimension of diversity
Openness, collaboration and participation are core aspects of our work — from development on Space XR Academy to collaboratively designing curriculum. We gain strength from diversity and actively seek participation from those who enhance it. These guidelines exist to enable diverse individuals and groups to interact and collaborate to mutual advantage. This document outlines both expected and prohibited behavior.

When and How to Use These Guidelines
These guidelines outline our behavior expectations as members of the Space XR Academy community in all Space XR Academy activities, both offline and online. Your participation is contingent upon following these guidelines in all Space XR Academy activities, including but not limited to:

Working in Space XR Academy spaces.
Working with other Space XR Academy community participants virtually or co-located.
Representing Space XR Academy at public events.
Representing Space XR Academy in social media (official accounts, staff accounts, personal accounts, social media pages).
Participating in Space XR Academy offsites and trainings.
Participating in Space XR Academy-related forums, mailing lists, wikis, websites, chat channels, bugs, group or person-to-person meetings, and Space XR Academy-related correspondence.
While these guidelines/code of conduct are specifically aimed at Space XR Academy’s work and community, we recognize that it is possible for actions taken outside of Space XR Academy’s online or in-person spaces to have a deep impact on community health. This is an active topic in the diversity and inclusion realm. We anticipate wide-ranging discussions among our communities about appropriate boundaries.

Expected Behavior
The following behaviors are expected of all Space XR Academy community members:

Be Respectful
Value each other’s ideas, styles and viewpoints. We may not always agree, but disagreement is no excuse for poor manners. Be open to different possibilities and to being wrong. Be respectful in all interactions and communications, especially when debating the merits of different options. Be aware of your impact and how intense interactions may be affecting people. Be direct, constructive and positive. Take responsibility for your impact and your mistakes — if someone says they have been harmed through your words or actions, listen carefully, apologize sincerely, and correct the behavior going forward.

Be Direct but Professional
We are likely to have some discussions about if and when criticism is respectful and when it’s not. We must be able to speak directly when we disagree and when we think we need to improve. We cannot withhold hard truths. Doing so respectfully is hard, doing so when others don’t seem to be listening is harder, and hearing such comments when one is the recipient can be even harder still. We need to be honest and direct, as well as respectful.

Be Inclusive
Seek diverse perspectives. Diversity of views and of people on teams powers innovation, even if it is not always comfortable. Encourage all voices. Help new perspectives be heard and listen actively. If you find yourself dominating a discussion, it is especially important to step back and encourage other voices to join in. Be aware of how much time is taken up by dominant members of the group. Provide alternative ways to contribute or participate when possible.

Be inclusive of everyone in an interaction, respecting and facilitating people’s participation whether they are:

Remote (on video or phone)
Not native language speakers
Coming from a different culture
Using pronouns other than “he” or “she”
Living in a different time zone
Facing other challenges to participate
Think about how you might facilitate alternative ways to contribute or participate. If you find yourself dominating a discussion, step back. Make way for other voices and listen actively to them.

Understand Different Perspectives
Our goal should not be to “win” every disagreement or argument. A more productive goal is to be open to ideas that make our own ideas better. Strive to be an example for inclusive thinking. “Winning” is when different perspectives make our work richer and stronger.

Appreciate and Accommodate Our Similarities and Differences
Space XR Academy community members come from many cultures and backgrounds. Cultural differences can encompass everything from official religious observances to personal habits to clothing. Be respectful of people with different cultural practices, attitudes and beliefs. Work to eliminate your own biases, prejudices and discriminatory practices. Think of others’ needs from their point of view. Use preferred titles (including pronouns) and the appropriate tone of voice. Respect people’s right to privacy and confidentiality. Be open to learning from and educating others as well as educating yourself; it is unrealistic to expect members of the Space XR Academy community to know the cultural practices of every ethnic and cultural group, but everyone needs to recognize one’s native culture is only part of positive interactions.

Lead by Example
By matching your actions with your words, you become a person others want to follow. Your actions influence others to behave and respond in ways that are valuable and appropriate for our organizational outcomes. Design your community and your work for inclusion. Hold yourself and others accountable for inclusive behaviors. Make decisions based on the highest good for Mozilla’s mission.

Behavior That Will Not Be Tolerated
The following behaviors are considered to be unacceptable under these guidelines.

Violence and Threats of Violence
Violence and threats of violence are not acceptable — online or offline. This includes incitement of violence toward any individual, including encouraging a person to commit self-harm. This also includes posting or threatening to post other people’s personally identifying information (“doxxing”) online.

Personal Attacks
Conflicts will inevitably arise, but frustration should never turn into a personal attack. It is not okay to insult, demean or belittle others. Attacking someone for their opinions, beliefs and ideas is not acceptable. It is important to speak directly when we disagree and when we think we need to improve, but such discussions must be conducted respectfully and professionally, remaining focused on the issue at hand.

Derogatory Language
Hurtful or harmful language related to:

Background
Family status
Gender
Gender identity or expression
Marital status
Sex
Sexual orientation
Native language
Age
Ability
Race and/or ethnicity
Caste
National origin
Socioeconomic status
Religion
Geographic location
Other attributes
is not acceptable. This includes deliberately referring to someone by a gender that they do not identify with, and/or questioning the legitimacy of an individual’s gender identity. If you’re unsure if a word is derogatory, don’t use it. This also includes repeated subtle and/or indirect discrimination; when asked to stop, stop the behavior in question.

Disruptive Behavior
Sustained disruption of events, forums, or meetings, including talks and presentations, will not be tolerated. This includes:

‘Talking over’ or ‘heckling’ speakers.
Drinking alcohol to excess or using recreational drugs to excess, or pushing others to do so.
Making derogatory comments about those who abstain from alcohol or other substances, pushing people to drink, talking about their abstinence or preferences to others, or pressuring them to drink — physically or through jeering.
Otherwise influencing crowd actions that cause hostility in the session.
Influencing Unacceptable Behavior
We will treat influencing or leading such activities the same way we treat the activities themselves, and thus the same consequences apply.

Consequences of Unacceptable Behavior
Bad behavior from any Space XR Academy community member, including those with decision-making authority, will not be tolerated. Intentional efforts to exclude people (except as part of a consequence of the guidelines or other official action) from Space XR Academy activities are not acceptable and will be dealt with appropriately.

Reports of harassment/discrimination will be promptly and thoroughly investigated by the people responsible for the safety of the space, event or activity. Appropriate measures will be taken to address the situation.

Anyone being asked to stop unacceptable behavior is expected to comply immediately. Violation of these guidelines can result in anyone being asked to leave an event or online space, either temporarily or for the duration of the event, or being banned from participation in spaces, or future events and activities in perpetuity.

In addition, any participants who abuse the reporting process will be considered to be in violation of these guidelines and subject to the same consequences. False reporting, especially to retaliate or exclude, will not be accepted or tolerated.

Reporting
If you believe you’re experiencing unacceptable behavior that will not be tolerated as outlined above, please use https://bit.ly/3sMvEED to report.

After receiving a concise description of your situation, they will review and determine the next steps. In addition to conducting any investigation, they can provide a range of resources, from a private consultation to other community resources. They will involve other colleagues or outside specialists (such as legal counsel), as needed to appropriately address each situation.

Please also report to us if you observe a potentially dangerous situation, someone in distress, or violations of these guidelines, even if the situation is not happening to you.

If you feel you have been unfairly accused of violating these guidelines, please follow the same reporting process.

License and Attribution
This set of guidelines is distributed under a Creative Commons Attribution-ShareAlike license.

These guidelines have been adapted with modifications from Mozilla’s original Community Participation Guidelines, the Ubuntu Code of Conduct, Mozilla’s View Source Conference Code of Conduct, and the Rust Language Code of Conduct, which are based on Stumptown Syndicate’s Citizen Code of Conduct. Additional text from the LGBTQ in Technology Code of Conduct and the WisCon code of conduct. This document and all associated processes are only possible with the hard work of many, many Mozillians.

Modifications to these Guidelines
Space XR Academy may amend the guidelines from time to time and may also vary the procedures it sets out where appropriate in a particular case. Your agreement to comply with the guidelines will be deemed agreement to any changes to it.

---
## [Hurricos/openwrt](https://github.com/Hurricos/openwrt)@[b3621f6007...](https://github.com/Hurricos/openwrt/commit/b3621f6007ed652af1c22d4138b70ff3127a8b2f)
#### Saturday 2022-05-28 18:59:15 by Alexandru Gagniuc

realtek-poe: De-suckify "poe sendframe" command

Typing "0x" repeatedly in a string of numbers that's obviously
hexadecimal is painful. So don't use sscanf(), which forces the "0x"
prefix. Instead, use strtoul() in base 16. This accepts numbers with
and without the prefix.

Also, if the string we receive is crap for whatever reason, don't try
to send it to the PoE controller. Just throw it the fuck out.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[ec78086e12...](https://github.com/mrakgr/The-Spiral-Language/commit/ec78086e1209d47ca2028a4cba5722cd92ea34b1)
#### Saturday 2022-05-28 19:36:45 by Marko Grdinić

"9:10pm. I am thinking how I should tackle the problem of making my own NPR filter. To begin with, what I should do is test whether the idea is viable at all. I think the ideal way to do it would be to try it out in Substance Designer. I should be able to use the shape splatter with the original image as a density mask to distribute various kinds of strokes.

The very first challenge is to extract the normal information from the renderer, but that should be manageable. The second will be to figure out how to use the shape splatterer to make it do what I want. Assuming I could get a decent result from this, I can think about future steps. Rather than work on a Blender addon that does this, I should refine the technique in Designer first and see how far I can get with it. If it turns out to work well, I'll have an essential element of my own style.

I should be able to implement the above, but maybe it will turn out to work poorly. Who knows. The idea is quite simple though, I am not sure why I haven't seen it being used.

My understanding of painting is that it is about using values as probability density for strokes. There is also the understanding of directionality to consider, but doing them orthogonal to the normals is the solution. Note that I can't do this later thing using just pixel values, so this is why PS does not have such a filter.

The idea I have here cuts directly to the meat of the issue of what painting really is, so I will be quite disappointed if it turns out to work poorly. It is worth exploring.

If it fails, I suppose I could just become a B&W guy, and only put in special effort when it comes to doing covers. I'd like to avoid letting it come to that if it is at all possible."

---
## [Frank-horton/Stack-](https://github.com/Frank-horton/Stack-)@[8040672d24...](https://github.com/Frank-horton/Stack-/commit/8040672d24900a919b4ea31bcddc08f902c09d1f)
#### Saturday 2022-05-28 20:46:47 by Frank-horton

Merge branch 'main' of https://github.com/Frank-horton/Fuck-You

---
## [pariahstation/Pariah-Station](https://github.com/pariahstation/Pariah-Station)@[70a87f9510...](https://github.com/pariahstation/Pariah-Station/commit/70a87f95100c290699ce5b92bb099d2f56bbb336)
#### Saturday 2022-05-28 22:12:23 by Gallyus

HOLY SHIT SHUT UP (#742)

* HOLY SHIT SHUT UP

* Apply suggestions from code review

* seeba sauce

---

