## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-05-31](docs/good-messages/2022/2022-05-31.md)


1,668,870 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,668,870 were push events containing 2,612,912 commit messages that amount to 175,079,689 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 43 messages:


## [Twilight-Dream-Of-Magic/TDOM-EncryptOrDecryptFile-Reborn](https://github.com/Twilight-Dream-Of-Magic/TDOM-EncryptOrDecryptFile-Reborn)@[0cc2786948...](https://github.com/Twilight-Dream-Of-Magic/TDOM-EncryptOrDecryptFile-Reborn/commit/0cc2786948b50832f8713ad2c4f6529f5cd1e467)
#### Tuesday 2022-05-31 00:45:12 by Twilight-Dream-Of-Magic

Published project version: EODF-OaldresPuzzle-Cryptic_0.1.0_20220402_Alpha

1.
Follow up on the previous commit [release project version: EODF-OaldresPuzzle-Cryptic_0.1.0_20220324_Alpha] and report on the progress now.
https://github.com/Twilight-Dream-Of-Magic/TDOM-EncryptOrDecryptFile-Reborn/commit/1c5c640efdf1232f2239b24eae9b547c9c3e3740
Commit HASH 1c5c640efdf1232f2239b24eae9b547c9c3e3740

There is no need to change the AES cryptic module at this time, but the Triple DES cryptic module code was fixed today and passed the random data application test.

I'm sorry, the last time I posted the code there were some errors in the code when copying the code for pasting, such errors may be low level, but at that time there was really too much code for me to find it easily.
But by now, that's all happened before.
This time I managed to find the code I wrote wrong inside the code released in this version. In fact, things like this really gave me a headache, and then made simplifications to some of the repetitive steps.

Other algorithms that have not been tested so far are
RC6 symmetric encryption and decryption algorithm

So that's what I'm going to do next, so wish me luck in debugging the code.

2.
Fixed more bugs

发布项目版本: EODF-OaldresPuzzle-Cryptic_0.1.0_20220402_Alpha

1.
跟进之前的提交[发布项目版本：EODF-OaldresPuzzle-Cryptic_0.1.0_20220324_Alpha]并且报告现在的进展。
https://github.com/Twilight-Dream-Of-Magic/TDOM-EncryptOrDecryptFile-Reborn/commit/1c5c640efdf1232f2239b24eae9b547c9c3e3740

目前没有必要改变AES密码模块，但是今天修复了Triple DES密码模块代码，并通过了随机数据应用测试。

我很抱歉，上次我发布的代码里面有一些复制代码时进行粘贴的错误，这种错误也许很低级，但是当时实在代码量太大，我不可能轻易的发现它。
不过到现在为止，那都是以前发生的事了。
这次我在这个版本发布的代码里面，成功找到了我写错的代码。其实这样的事情真的让我很头疼，然后对一些重复的步骤做了简化。

到目前为止没有测试的其他算法有
RC6对称加密和解密算法

那么这也是我接下来要做的事情，那么祝我调试代码的时候有好运吧。

2.
修复了更多的bug

---
## [slarew/linux](https://github.com/slarew/linux)@[bd7d220a61...](https://github.com/slarew/linux/commit/bd7d220a614aff4cf48e48c255e60ca057732eff)
#### Tuesday 2022-05-31 00:51:03 by Jason A. Donenfeld

random: use linear min-entropy accumulation crediting

commit c570449094844527577c5c914140222cb1893e3f upstream.

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
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [CluckeyMcCormick/fictional-guacamole](https://github.com/CluckeyMcCormick/fictional-guacamole)@[bdb382c32c...](https://github.com/CluckeyMcCormick/fictional-guacamole/commit/bdb382c32c6f701353a255e9645931a162cc47d2)
#### Tuesday 2022-05-31 01:06:15 by frick-nedrickson

Add a helix particle effect (for some reason)

I was struck by inpsiration, and set out to make a particle effect
where the particles moved in a helix formation. Honestly, I really
couldn't tell you why I made it. I thought it'd look cool, and it'd be
a good way to introduce fixed-node particle system compatability.

And... yeah, it does look cool. In fact, I was thinking that I could
probably make ShaderMaterials also scalable. Bah.

---
## [walternewtz/android_kernel_xiaomi_sdm845](https://github.com/walternewtz/android_kernel_xiaomi_sdm845)@[f0bc3c44ac...](https://github.com/walternewtz/android_kernel_xiaomi_sdm845/commit/f0bc3c44ac61fd515040e0ddfdbfb65b041157e0)
#### Tuesday 2022-05-31 01:12:13 by Francis Yan

BACKPORT: tcp: instrument tcp sender limits chronographs

This patch implements the skeleton of the TCP chronograph
instrumentation on sender side limits:

	1) idle (unspec)
	2) busy sending data other than 3-4 below
	3) rwnd-limited
	4) sndbuf-limited

The limits are enumerated 'tcp_chrono'. Since a connection in
theory can idle forever, we do not track the actual length of this
uninteresting idle period. For the rest we track how long the sender
spends in each limit. At any point during the life time of a
connection, the sender must be in one of the four states.

If there are multiple conditions worthy of tracking in a chronograph
then the highest priority enum takes precedence over
the other conditions. So that if something "more interesting"
starts happening, stop the previous chrono and start a new one.

The time unit is jiffy(u32) in order to save space in tcp_sock.
This implies application must sample the stats no longer than every
49 days of 1ms jiffy.

saalim :- Drop rate_app_limited from tcp header (already present)
original :- https://github.com/danascape/kernel-msm-4.14/commit/05b055e89121394058c75dc354e9a46e1e765579#diff-4ddfd98f3453244962e17ac121bea6162887af47d0531ba6e2cf49a941edf2c9

Signed-off-by: Francis Yan <francisyyan@gmail.com>
Signed-off-by: Yuchung Cheng <ycheng@google.com>
Signed-off-by: Soheil Hassas Yeganeh <soheil@google.com>
Acked-by: Neal Cardwell <ncardwell@google.com>
Signed-off-by: David S. Miller <davem@davemloft.net>
Signed-off-by: danascape <saalimquadri1@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>
Signed-off-by: Dhruv <dhruvgera61@gmail.com>

---
## [Dr-Pope/fulpstation](https://github.com/Dr-Pope/fulpstation)@[b59f03e592...](https://github.com/Dr-Pope/fulpstation/commit/b59f03e592ce72f069760eba0f9eb30eeacd16c1)
#### Tuesday 2022-05-31 01:20:23 by John Willard

Deputy update (#428)

* deputy berets cant be knocked off, deputies get tablets, service deputy beret buff.

* fuck you

---
## [Sonic121x/Skyrat-tg](https://github.com/Sonic121x/Skyrat-tg)@[fb4f191c52...](https://github.com/Sonic121x/Skyrat-tg/commit/fb4f191c52772cb5d718bbd399361b36cb8d7732)
#### Tuesday 2022-05-31 01:40:16 by Zonespace

[MDB IGNORE] Mirrors 67324 (#13928)

* [MDB Ignore] OH GOD OH FUCK OH SHIT OH LORD - SPACE AND RUINS IS BROKEN (#67324)

So, for the last few days on production, Space Ruin generation has refused to work. Why is this? It's because in #67107 (cfc233052885dd294b2e7e676caaf84a2a37592b), we repathed `/area/space`  to `/area/misc/space` (lol i should have paid attention to that) without updating everything in code to match. I couldn't seem to get `/area/misc/space` to properly work somehow (this could have also been something I was doing wrong), but I worked it back to just making everything vanilla `/area/space` and all of those unwanted behaviors should be squashed out. Let's get the game working again.

* fix

* fix2

Co-authored-by: san7890 <the@san7890.com>

---
## [ajwerner/cockroach](https://github.com/ajwerner/cockroach)@[f782e45fd0...](https://github.com/ajwerner/cockroach/commit/f782e45fd0da015396bc758e855535a951f2e21a)
#### Tuesday 2022-05-31 01:55:54 by Andrei Matei

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
## [OliOliOnsiPree/thewasteland](https://github.com/OliOliOnsiPree/thewasteland)@[013fb2bd4b...](https://github.com/OliOliOnsiPree/thewasteland/commit/013fb2bd4bd6ce216844c984da9dc5ffed316c61)
#### Tuesday 2022-05-31 02:12:39 by ishitbyabullet

Fallout Alien Content (#539)

* ncr veteran ranger removal

sorry, boys, but 18 yr old female veteran rangers aren't lore accurate.

* NCR no longer has farming or water

No one ever did the sharecropper farm quest in FNV anyways.

* NCR must actively pay taxes

There is a new need meter similar to thirst and hunger for this now.

---
## [Folcon/fruit-economy](https://github.com/Folcon/fruit-economy)@[b1a94387ab...](https://github.com/Folcon/fruit-economy/commit/b1a94387abd6b1de95c7097b987dba3d623232d4)
#### Tuesday 2022-05-31 02:13:05 by Folcon

Remember to cleanup the order book due to decay

We'll also need to do it when peeps die, but as we're not modelling that atm, let's not worry about it...

---
## [PalaceMC/web](https://github.com/PalaceMC/web)@[e6a46304d7...](https://github.com/PalaceMC/web/commit/e6a46304d72a45521fe82ba07ccae352557479df)
#### Tuesday 2022-05-31 02:58:01 by almic

implement playerGetConnection() + JSONB

json parsing/ sending now uses JSONB, a.k.a. when-json-met-bigint. This library is small, quick, and allows parsing big numbers into BigInt just like how JSON.parse and JSON.stringify should. Almost went with json-bigint, but discovered it broke the object model to patch prototype pollution, what a silly thing to do. It also used bignumber.js, bloating what would be 1 dependency into 4... total beta move.

But forget about all of that, shit works now and it didn't require me to write my own entire JSON parser... thank god.

Also i fixed the object test, it pretty much didn't even work before lmao.

---
## [Kapu1178/Pariah-Station](https://github.com/Kapu1178/Pariah-Station)@[c77fb1e795...](https://github.com/Kapu1178/Pariah-Station/commit/c77fb1e7959bec41276673ba903da1625be8b68e)
#### Tuesday 2022-05-31 04:38:38 by Octus

Parallax but better: Smooth movement cleanup (#66567) (#724)

* Alright, so I'm optimizing parallax code so I can justify making it do a
bit more work

To that end, lets make the checks it does each process event based.
There's two. One is for a difference in view, which is an easy fix since
I added a view setter like a year back now.

The second is something planets do when you change your z level.
This gets more complicated, because we're "owned" by a client.
So the only real pattern we can use to hook into the client's mob's
movement is something like connect_loc_behalf.

So, I've made connect_mob_behalf. Fuck you.

This saves a proc call and some redundant logic

* Fixes random parallax stuttering

Ok so this is kinda a weird one but hear me out.

Parallax has this concept of "direction" that some areas use, mostly
the shuttle transit ones. Set when you move into a new area.
So of course it has a setter. If you pass it a direction that it doesn't
already have, it'll start up the movement animation, and disable normal
parallax for a bit to give it some time to get going.

This var is typically set to 0.

The problem is we were setting /area/space's direction to null in
shuttle movement code, because of a forgotten proc arg.

Null is of course different then 0, so this would trigger a halt in
parallax processing.

This causes a lot of strange stutters in parallax, mostly when you're
moving between nearspace and space. It looks really bad, and I'm a bit
suprised none noticed.

I've fixed it, and added a default arg to the setter to prevent this
class of issue in future. Things look a good bit nicer this way

* Adds animation back to parallax

Ok so like, I know this was removed and "none could tell" and whatever,
and in fairness this animation method is a bit crummy.

What we really want to do is eliminate "halts" and "jumps" in the
parallax moveemnt. So it should be smooth.

As it is on live now, this just isn't what happens, you get jumping
between offsets. Looks frankly, horrible. Especially on the station.

Just what I've done won't be enough however, because what we need to do
is match our parallax scroll speed with our current glide speed. I need
to figure out how to do this well, and I have a feeling it will involve
some system of managing glide sources.

Anyway for now the animation looks really nice for ghosts with default
(high) settings, since they share the same delay.

I've done some refactoring to how old animation code worked pre (4b04f9012d1763df625e9e4ae75e4cf4bd1f3771). Two major
changes tho.

First, instead of doing all the animate checks each time we loop over a
layer, we only do the layer dependant ones. This saves a good bit of
time.

Second, we animate movement on absolute layers too. They're staying in
the same position, but they still move on the screen, so we do the same
gental leaning. This has a very nice visual effect.

Oh and I cleaned up some of the code slightly.

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [Kapu1178/Pariah-Station](https://github.com/Kapu1178/Pariah-Station)@[70a87f9510...](https://github.com/Kapu1178/Pariah-Station/commit/70a87f95100c290699ce5b92bb099d2f56bbb336)
#### Tuesday 2022-05-31 04:38:38 by Gallyus

HOLY SHIT SHUT UP (#742)

* HOLY SHIT SHUT UP

* Apply suggestions from code review

* seeba sauce

---
## [CluckeyMcCormick/fictional-guacamole](https://github.com/CluckeyMcCormick/fictional-guacamole)@[18d465a974...](https://github.com/CluckeyMcCormick/fictional-guacamole/commit/18d465a974e4b7f444130ba88da322d9424eec28)
#### Tuesday 2022-05-31 04:45:20 by frick-nedrickson

Allow ShaderMaterials with Scalable Particle Emitters

Okay, I spent way too much time making a stupid helix particle effect.
And then, I thought to myself, "Oh, that wouldn't actually be that
hard to scale up using the ScalingParticleEmitter, if we assume the
1x1x1 volume restriction".

Anyway, I then spent too much time making that work, and as much as I
am angry at myself and the ShaderMaterial for taking up my time with a
stupid diversion, it seems to work pretty seamlessly.

Still, this is more cavalier than I usually go about things, and
overall I feel like it's tacked-on or jury-rigged. I guess that's
because all I really did was make an algorithm harder to read by
adding a bunch of if statements? Yeah, that's probably it.

I updated the documentation to match my newest improvements - I
noticed a bunch of errors and half-finished thoughts, so I corrected
those. Of course, I thought the documentation was fine last time, so
who knows. Zarro boogs!

---
## [condor2/opencart](https://github.com/condor2/opencart)@[89c304ae61...](https://github.com/condor2/opencart/commit/89c304ae61fb683b2ca8ff7dcf5ceabfc4f5a0eb)
#### Tuesday 2022-05-31 06:42:41 by Anton

OC4 return created module_id

IMHO every single model function, creating a row in DB, must return this row id after executed.

I can check `$module_id = $this->db->getLastId();` in my code on clean opencart installation.
But what if this model function calls any `after` events which also insert rows into DB?

This is not a developer friendly software architecture when you need to create hacks, hooks, workarounds and other voodoo magic to get a single value for page redirect.

BUG:
By the way on creating, for example a banner module, on save you are not redirected to created module page. 
So every click on Save button just creates a duplicate of a module.

---
## [Jakksergal/Skyrat-tg](https://github.com/Jakksergal/Skyrat-tg)@[a3c0819e80...](https://github.com/Jakksergal/Skyrat-tg/commit/a3c0819e8091ab99a5ab8f53b59c4687e5b2f2cf)
#### Tuesday 2022-05-31 06:57:09 by SkyratBot

[MIRROR] Removes (in) smoke and foam reactions [MDB IGNORE] (#13963)

* Removes (in) smoke and foam reactions (#67270)

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

* Removes (in) smoke and foam reactions

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [SmArtKar/tgstation](https://github.com/SmArtKar/tgstation)@[cd294e9040...](https://github.com/SmArtKar/tgstation/commit/cd294e9040505e73e46384d6166015afa43217f3)
#### Tuesday 2022-05-31 07:38:12 by vincentiusvin

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
## [avar/git](https://github.com/avar/git)@[8d5a3c1bb5...](https://github.com/avar/git/commit/8d5a3c1bb50eccad307d006d8ebe77864adb87a5)
#### Tuesday 2022-05-31 07:58:23 by Ævar Arnfjörð Bjarmason

usage API: use C99 macros for {usage,usagef,die,error,warning,die}*()

Change the "usage" family of functions to be defined in terms of C99
variadic macros, as we've optionally done with the BUG() macro and
BUG_fl() function since d8193743e08 (usage.c: add BUG() function,
2017-05-12), and unconditionally since 765dc168882 (git-compat-util:
always enable variadic macros, 2021-01-28).

This would have been possible before having a hard dependency on C99,
but as the dual implementations of C99 and pre-C99 macros and
functions adjusted in preceding commits show, doing so would have been
rather painful.

By having these be macros we'll now log meaningful "file" and "line"
entries in trace2 events. Before this we'd log "usage.c" in all of
them, and the line would be the relevant locations in that file.

To do this we need to not only introduce X_fl() functions for
{die,error,warning,die}{,_errno}(), but also change all the callers of
the set_*() and get_() functions in usage.h to take "file" and "line"
arguments.

Neither the built-in {die,error,warning,die}{,_errno}() nor anyone
else does anything useful with these "file" and "line" arguments for
now, but it means we can define all our macros and functions
consistently.

It also opens the door for a follow-up change where these functions
could optionally emit the file name and line number, e.g. for
DEVELOPER=1 builds, or depending on configuration.

It might be a good change to remove the "fmt" key from the "error"
events as a follow-up change. As these few examples from running the
test suite show it's sometimes redundant (same as the "msg"), rather
useless (just a "%s"), or something we could now mostly aggregate by
file/line instead of the normalized printf format:

      1 file":"builtin/gc.c","line":1391,"msg":"'bogus' is not a valid task","fmt":"'%s' is not a valid task"}
      1 file":"builtin/for-each-ref.c","line":89,"msg":"format: %(then) atom used more than once","fmt":"%s"}
      1 file":"builtin/fast-import.c","line":411,"msg":"Garbage after mark: N :202 :302x","fmt":"Garbage after mark: %s"}

"Mostly" here assumes that it would be OK if the aggregation changed
between git versions, which may be what all users of trace2 want. The
change that introduced the "fmt" code was ee4512ed481 (trace2: create
new combined trace facility, 2019-02-22), and the documentation change
was e544221d97a (trace2: Documentation/technical/api-trace2.txt,
2019-02-22).

Both are rather vague on what problem "fmt" solved exactly, aside from
the obvious one of it being impossible to do meaningful aggregations
due to the "file" and "line" being the same everywhere, which isn't
the case now.

In any case, let's leave "fmt" be for now, the above summary was given
in case it's interesting to remove it in the future, e.g. to save
space in trace2 payloads.

The change here in git_die_config() is the bare minimum needed to get
it working, but better would be a change[1] to correctly report the
caller file and line numbers. Let's leave that for later, it can be
done later.

1. https://lore.kernel.org/git/patch-4.4-e0e6427cbd3-20211206T165221Z-avarab@gmail.com/#t

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [mamh-mixed/microsoft-terminal](https://github.com/mamh-mixed/microsoft-terminal)@[77215d9d77...](https://github.com/mamh-mixed/microsoft-terminal/commit/77215d9d77b99b48d1ee8302736178f2ec9f3a77)
#### Tuesday 2022-05-31 08:00:45 by Mike Griese

Fix `ShowWindow(GetConsoleWindow())` (#13118)

A bad merge, that actually revealed a horrible bug.

There was a secret conflict between the code in #12526 and #12515. 69b77ca was a bad merge that hid just how bad the issue was. Fixing the one line `nullptr`->`this` in `InteractivityFactory` resulted in a window that would flash uncontrollably, as it minimized and restored itself in a loop. Great. 

This can seemingly be fixed by making sure that the conpty window is initially created with the owner already set, rather than relying on a `SetParent` call in post. This does pose some complications for the #1256 future we're approaching. However, this is a blocking bug _now_, and we can figure out the tearout/`SetParent` thing in post. 

* fixes #13066.
* Tested with the script in that issue.
* Window doesn't flash uncontrollably.
* `gci | ogv` still works right
* I work here.
* Opening a new tab doesn't spontaneously cause the window to minimize
* Restoring from minimized doesn't yeet focus to an invisible window
* Opening a new tab doesn't yeet focus to an invisible window
* There _is_ a viable way to call `GetAncestor` s.t. it returns the Terminal's hwnd in Terminal, and the console's in Conhost


The `SW_SHOWNOACTIVATE` change is also quite load bearing. With just `SW_NORMAL`, the pseudo window (which is invisible!) gets activated whenever the terminal window is restored from minimized. That's BAD.


There's actually more to this as well. 


Calling `SetParent` on a window that is `WS_VISIBLE` will cause the OS to hide the window, make it a _child_ window, then call `SW_SHOW` on the window to re-show it. `SW_SHOW`, however, will cause the OS to also set that window as the _foreground_ window, which would result in the pty's hwnd stealing the foreground away from the owning terminal window. That's bad.

`SetWindowLongPtr` seems to do the job of changing who the window owner is, without all the other side effects of reparenting the window. 

Without `SetParent`, however, the pty HWND is no longer a descendant of the Terminal HWND, so that means `GA_ROOT` can no longer be used to find the owner's hwnd. For even more insanity, without `WS_POPUP`, none of the values of `GetAncestor` will actually get the terminal HWND. So, now we also need `WS_POPUP` on the pty hwnd. To get at the Terminal hwnd, you'll need

```c++
GetAncestor(GetConsoleWindow(), GA_ROOTOWNER)
```

---
## [openstack/kolla-ansible](https://github.com/openstack/kolla-ansible)@[4e991a98ea...](https://github.com/openstack/kolla-ansible/commit/4e991a98eaf25faa073bb5b01470a5808b5f18e4)
#### Tuesday 2022-05-31 09:38:34 by Radosław Piliszek

[CI] Nullify attempts

Per Clark Boylan's feedback [1], retries cause a retry not only
for pre playbook failures but also for cases where Ansible detects
network connectivity issues and they are caused by disks getting
filled to their fullest. This is an issue we experience that
sometimes results in a POST_FAILURE but certain FAILUREs are
retried which wastes CI resources.
The problematic jobs are ceph jobs. They are to be looked into.
Backport to all branches.
We can adjust retries for the core jobs that do not exhibit the
nasty behaviour but first we can try running without retries
to measure the troublesomeness.

[1] https://review.opendev.org/c/openstack/kolla-ansible/+/843536

Change-Id: I32fc296083b4881e8f457f4235a32f94ed819d9f
(cherry picked from commit 153956e458157e44d73efc3dd369699ff20e4d12)

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[cd284b70a0...](https://github.com/mrakgr/The-Spiral-Language/commit/cd284b70a007ab65de16105e74709c9e20374070)
#### Tuesday 2022-05-31 10:35:11 by Marko Grdinić

"9:15am. I am surprisingly rested right now. Did some /wip/ posting, let me read Black Lagoon.

Today I will start off by finally playing with freestyle edges. Never gave them a try yet.

9:35am. https://readmanganato.com/manga-kh988264/chapter-16

Let me just read a few chapters of Legendary Mechanic and I will get on with it.

9:50am. Let me do it. It is time to check out the freestyle edges. I need to do some work for the day.

9:55am. Hmmm...I turned them on in Eevee settings, what do I do next? Let me watch a tut.

https://youtu.be/_QVNIEP1E5M
Render Edges and Styles in Blender with FREESTYLE! Beginners start here!

I am especially interested in how the inner edges could be done.

https://docs.blender.org/manual/en/latest/render/freestyle/introduction.html
> Freestyle is an edge/line-based non-photorealistic (NPR) rendering engine.

So it is a whole engine?

11:05am. Ok, let me export just the sillhoutes here. I am using the workbench as renderer at the moment. It takes way longer for the freestyle edges to be calculated than anything else. All the detail in the scene is making the freestyle edges hard to deal with. Maybe I'll ommit them in the end. Let me export them and then I will also export the cryptomatters. Where is that plugin.

https://github.com/3d-io/Blender_Exr_auto-pass_saver

11:15am. Hmmm, whatever. Let me bring in the cryptomattes. Posterization works pretty poorly here.

11:30am. I have no idea what is going on here, why does cryptomatte have such a limited color selection? In addition to this CSP does not have exr imports so I can't text if it will come out in any other way.

https://youtu.be/OykO2GkSyUo
Cryptomattes in Blender 3.0 for Fusion or ANY software!

Let me watch this. Then I'll try exporting one of the cryptomatte objects as png just to see what will happen. Right now I am not sure what to do with them.

I put in 2 levels of cryptomatte, and I get only a couple of different colors to pick from. I thought I would get an unique color for every object.

https://youtu.be/OykO2GkSyUo?t=192
> ...But I'll show you one just using pngs.

This will be a good tutorial.

11:55am. No, it is not a good tutorial. I'd have to select every object by hand before exporting it. What a waste of time.

12pm. Mhhhhh...cryptomattes suck. I'd be better off with just the edges. Let me focus on that. How do I export them as svg.

12:25pm. The svg export addon works quite well. It is a lot better for doing selections than the pixel version.

At this point I am honestly considering NN style transfer. I complained about deep dream being a service, but it is not like I couldn't train my own thing eventually.

Well, nevermind it for now. I'll fill in the missing edges and see how far grad maps will get me. In the full version I'll at least put flats as materials, but this is just an exercise to see how good I can get it to look by hand without excessive manual repainting.

12:35pm. Let me take a break here. As expected this is a slow day. I am not going to rush it. It is good to slowly feel things out."

---
## [Grazvis1988/pipeline-ex11.20-fullStackOpen](https://github.com/Grazvis1988/pipeline-ex11.20-fullStackOpen)@[8dcbec527e...](https://github.com/Grazvis1988/pipeline-ex11.20-fullStackOpen/commit/8dcbec527eca11bcbf658a2efa7be62d627bbb6f)
#### Tuesday 2022-05-31 11:14:14 by Grazvis

pipeline added and test errors fixed

Little fix in pipeline

Linting errors fixed

cypress endpoint fix

yet slight pipeline configuration fix

And anoter fix

And again another

pipeline fix

final pipeline fix

Final pipeline fix (I hope)

What the hell

testing pipeline

I hope this is final commit

Finall commit

What the hell

God damn it!

You got to be kidding me

God damn it please work

triger workflow

triger workflow 2

triger workflow 3

Here we go again!

Pipeline update

And again!

...

So now should work for sure

---
## [projects-nexus/android_kernel_xiaomi_gauguin](https://github.com/projects-nexus/android_kernel_xiaomi_gauguin)@[e7e5e09f61...](https://github.com/projects-nexus/android_kernel_xiaomi_gauguin/commit/e7e5e09f613f4e94222307138098faed80bcc35b)
#### Tuesday 2022-05-31 11:30:35 by Angelo G. Del Regno

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
## [iancuvictor/Portfolio](https://github.com/iancuvictor/Portfolio)@[4b11e0d8f4...](https://github.com/iancuvictor/Portfolio/commit/4b11e0d8f492c24aceefc1833faeea765536be2d)
#### Tuesday 2022-05-31 11:53:42 by Iancu Victor - Iuliu

Bugged version of: Mobile responsiveness for shitty phones that have a screen size smaller than fucking 320px. Will fix later because right now I am fed up on this shit ass resolution.

---
## [nishant6342/kernel_realme_RMX3031](https://github.com/nishant6342/kernel_realme_RMX3031)@[13ca26aee7...](https://github.com/nishant6342/kernel_realme_RMX3031/commit/13ca26aee7d382b12055b04f7e7de65800ac1dee)
#### Tuesday 2022-05-31 12:11:39 by Wang Han

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
Signed-off-by: Nishant Kumar <www.rajsonu13@gmail.com>

---
## [mjcheetham/git](https://github.com/mjcheetham/git)@[07564773c2...](https://github.com/mjcheetham/git/commit/07564773c2569d012719ab9e26b9b27251f3d354)
#### Tuesday 2022-05-31 13:49:13 by Ævar Arnfjörð Bjarmason

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
## [T-J-Teru/binutils-gdb](https://github.com/T-J-Teru/binutils-gdb)@[fccb395397...](https://github.com/T-J-Teru/binutils-gdb/commit/fccb395397948ad99bc7024b85c93cb7c3d0a1e0)
#### Tuesday 2022-05-31 14:26:47 by Andrew Burgess

gdb: native target invalid architecture detection

If GDB is asked to start a new inferior, or attach to an existing
process, using a binary file for an architecture that does not match
the current native target, then, currently, GDB will assert.  Here's
an example session using current HEAD of master with GDB built for an
x86-64 GNU/Linux native target, the binary being used is a RISC-V ELF:

  $ ./gdb/gdb -q --data-directory ./gdb/data-directory/
  (gdb) file /tmp/hello.rv32imc.x
  Reading symbols from /tmp/hello.rv32imc.x...
  (gdb) start
  Temporary breakpoint 1 at 0x101b2: file hello.rv32.c, line 23.
  Starting program: /tmp/hello.rv32imc.x
  ../../src/gdb/gdbarch.h:166: internal-error: gdbarch_tdep: Assertion `dynamic_cast<TDepType *> (tdep) != nullptr' failed.
  A problem internal to GDB has been detected,
  further debugging may prove unreliable.

The same error is encountered if, instead of starting a new inferior,
the user tries to attach to an x86-64 process with a RISC-V binary set
as the current executable.

These errors are not specific to the x86-64/RISC-V pairing I'm using
here, any attempt to use a binary for one architecture with a native
target of a different architecture will result in a similar error.

Clearly, attempting to use this cross-architecture combination is a
user error, but I think GDB should do better than an assert; ideally a
nice error should be printed.

The problem we run into is that, when the user starts a new inferior,
or attaches to an inferior, the inferior stops.  At this point GDB
attempts to handle the stop, and this involves reading registers from
the inferior.

These register reads end up being done through the native target, so
in the example above, we end up in the amd64_supply_fxsave function.
However, these functions need a gdbarch.  The gdbarch is fetched from
the register set, which was constructed using the gdbarch from the
binary currently in use.  And so we end up in amd64_supply_fxsave
using a RISC-V gdbarch.

When we call:

  i386_gdbarch_tdep *tdep = gdbarch_tdep<i386_gdbarch_tdep> (gdbarch);

this will assert as the gdbarch_tdep data within the RISC-V gdbarch is
of the type riscv_gdbarch_tdep not i386_gdbarch_tdep.

The solution I propose in this commit is to add a new target_ops
method supports_architecture_p.  This method will return true if a
target can safely be used with a specific architecture, otherwise, the
method returns false.

I imagine that a result of true from this method doesn't guarantee
that GDB can start an inferior of a given architecture, it just means
that GDB will not crash if such an attempt is made.  A result of false
is a hard stop; attempting to use this target with this architecture
is not supported, and may cause GDB to crash.

This distinction is important I think for things like remote targets,
and possibly simulator targets.  We might imagine that GDB can ask a
remote (or simulator) to start with a particular executable, and the
target might still refuse for some reason.  But my thinking is that
these refusals should be well handled (i.e. GDB should give a user
friendly error), rather than crashing, as is the case with the native
targets.

For example, if I start gdbserver on an x86-64 machine like this:

  gdbserver --multi :54321

Then make use of this from a GDB session like this:

  $ ./gdb/gdb -q --data-directory ./gdb/data-directory/
  (gdb) file /tmp/hello.rv32imc.x
  Reading symbols from /tmp/hello.rv32imc.x...
  (gdb) target extended-remote :54321
  Remote debugging using :54321
  (gdb) run
  Starting program: /tmp/hello.rv32imc.x
  Running the default executable on the remote target failed; try "set remote exec-file"?
  (gdb)

Though the error is not very helpful in diagnosing the problem, we can
see that GDB has not crashed, but has given the user an error.

And so, the supports_architecture_p method is created to return true
by default, then I override this in inf_child_target, where I compare
the architecture in question with the default_bfd_arch.

Finally, I've added calls to supports_architecture_p for the
run (which covers run, start, starti) and attach commands.

You will notice a lack of tests for this change.  I'm not sure of a
good way that I can build a binary for a different architecture as
part of a test, but if anyone has any ideas then I'll be happy to add
a test here.

---
## [Ania000/CollabProject](https://github.com/Ania000/CollabProject)@[a4ce94855a...](https://github.com/Ania000/CollabProject/commit/a4ce94855a3e92540535bebec012ffe451f97c53)
#### Tuesday 2022-05-31 15:05:23 by Ania000

Adding Ania's bullshit

Doors! and a few trees, working player and enemy. Knife and fist as weapons. NPC attack logic still in progress, so will not work... sorry.
Damage system and Door component to handle logic
Basic terrain material if we want to make some rocks and fields.
Fixed blood particles.
Input mappings added

---
## [ParnaSaeidpour/cs50-submit50-](https://github.com/ParnaSaeidpour/cs50-submit50-)@[3f4f757fc7...](https://github.com/ParnaSaeidpour/cs50-submit50-/commit/3f4f757fc71d1d45df4926c3bb6738d96198f930)
#### Tuesday 2022-05-31 16:02:27 by Parna Saeidpour

problem_set1_Meal Time

n meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

Structure your program per the below, wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format, to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).

---
## [TheEpicBlock/PolyMcShowcase](https://github.com/TheEpicBlock/PolyMcShowcase)@[550719e6b5...](https://github.com/TheEpicBlock/PolyMcShowcase/commit/550719e6b562014f892331a133d8439fc02eb192)
#### Tuesday 2022-05-31 16:30:05 by TheEpicBlock

I'm going to commit this not because it is useful but because I'm angry, and I want the world to share my fucking pain

---
## [avar/git](https://github.com/avar/git)@[6f65f41eb8...](https://github.com/avar/git/commit/6f65f41eb8a8ec22fb3bbc03735f5cd88e7c9b58)
#### Tuesday 2022-05-31 16:57:13 by Ævar Arnfjörð Bjarmason

usage API: make the "{usage,fatal,error,warning,BUG}: " translatable

In preceding commits the vreportf() function was made static, so we
know it's only being called with a limited set of fixed prefixes. Pass
an enum indicating the kind of usage message we're emitting instead,
which means that we can fold the BUG_vfl_common() functionality
directly into it.

Since we've now got one place were we're emitting these usage messages
we can make them translatable.

We need to be careful with this function to not malloc() anything, as
a failure in say a use of strbuf_vaddf() would call xmalloc(), which
would in turn call die(), but here we're using static strings, either
from libintl or not.

I was on the fence about making the "BUG: " message translatable, but
let's do it for consistency. Someone who doesn't speak a word of
English may not know what "BUG" means, but if it's translated they
might have an easier time knowing that they have to report a bug
upstream. Since we'll always emit the line number it's unlikely that
we're going to be confused by such a report.

As we've moved the BUG_vfl_common() code into vsnprintf() we can do
away with one of the two checks for buffer sizes added in
116d1fa6c69 (vreportf(): avoid relying on stdio buffering, 2019-10-30)
and ac4896f007a (fmt_with_err: add a comment that truncation is OK,
2018-05-18).

I.e. we're being overly paranoid if we define the fixed-size "prefix"
and "msg" buffers, are OK with the former being truncated, and then
effectively check if our 256-byte buffer is larger than our 4096-byte
buffer. I wondered about adding a:

    assert(sizeof(prefix) < sizeof(msg)); /* overly paranoid much? */

But I think that would be overdoing it. Anyone modifying this function
will keep these two buffer sizes in mind, so let's just remove one of
the checks instead.

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [avar/git](https://github.com/avar/git)@[ad4c47b797...](https://github.com/avar/git/commit/ad4c47b797a9a4a4824965ca4e77956cee6841db)
#### Tuesday 2022-05-31 16:57:22 by Ævar Arnfjörð Bjarmason

usage API: add "core.usageAddSource" config to add <file>:<line>

Optionally extend the support that BUG() has had for emitting line
numbers to the {usage,fatal,error,warning}{,_errno}() functions.

Before we'd unconditionally get error messages like:

    $ git -c core.x=y config --get --bool core.x
    fatal: bad boolean config value 'y' for 'core.x'

Which can be changed with core.usageAddSource=true to include the file
and line numbers:

    $ git -c core.usageAddSource=true -c core.x=y config --get --bool core.x
    fatal: config.c:1241: bad boolean config value 'y' for 'core.x'

As the added documentation notes this is primarily intended to be
useful to developers of git itself, but is being exposed as a user
setting to e.g. help file better bug reports.

This also adds a "GIT_TEST_USAGE_ADD_SOURCE" setting intended to run
the test suite in this mode.

Currently it has a lot of failures. Most of those are rather trivial,
and can be "fixed" by pointing GIT_TEST_CMP to a "diff -u" that does a
s/^(usage|fatal|error|warning): [^:]+:[0-9]+/$1/g on its input files,
and likewise for a "grep" wrapper that does the same.

Even if we can't run the tests in this mode yet I'd like to have this
for ad-hoc debugging, and to make it easier to work towards running
the tests in this mode. If we can turn this on permanently it'll be
much easier to read test output, as we won't need to worry about the
indirection of looking up where an error might have been emitted,
which can be especially painful when the message being emitted isn't
unique within git.git.

This new code needs to be guarded by the "dying" variable for the
reasons explained in 2d3c02f5db6 (die(): stop hiding errors due to
overzealous recursion guard, 2017-06-21), and for those same reasons
it's racy under multi-threading.

Here the worst case is that incrementing the variable will run away
from us, and we won't get our desired <file>:<line> number. That's OK
in this case, those cases should be isolated to the config code (if we
can't parse the config), memory allocation etc, but we'll get it right
in the common cases.

Using GIT_TEST_USAGE_ADD_SOURCE should be immune from any racyness, as
it only needs a getenv() and git_parse_maybe_bool(), which won't die.

Add a repo_cfg_bool_env() wrapper to repo-settings.c for
GIT_TEST_USAGE_ADD_SOURCE, in 3050b6dfc75 (repo-settings.c: simplify
the setup, 2021-09-21) I indicated that the GIT_TEST_MULTI_PACK_INDEX
env variable/config pair in that file has odd semantics, but users of
repo_cfg_bool_env() have straightforward and expected semantics. If
the environment variable is set (true or false) we'll use it,
otherwise we'll use the config, and finally fall back on the
default (of "false", in this case).

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[19997e0a87...](https://github.com/mrakgr/The-Spiral-Language/commit/19997e0a877b82c51feb4875ec955f9dd13ef2d5)
#### Tuesday 2022-05-31 17:34:11 by Marko Grdinić

"1:40pm. Just one more chapter and then I will get started. I already am finding this a pain in the ass. I should just pass stuff through deep dream and call it a day.

1:50pm. Ok, a bit more and then I will do some painting.

2:05pm. Let me start.

First off, let me add some missing lines.

2:10pm. Let me get the pen, I have no room with mouse.

2:50pm. No, it won't work. Forget doing processing in CSP. If I go down that route be working on the image for days.

Right now, it is difficult to describe my feelings. I am staring at the CSP image and I feel absotely awash in terror, as if I am going to die tomorrow.

https://www.reddit.com/r/blender/comments/s7dt5c/trying_out_toon_shading_hope_you_like_it/

Forget it. Maybe I'll end up drawing in charas as stilts. If so fine. But doing backgrounds in CSP, or processing them like I did that couch is out of the question.

Either I will do my current approach + NN style transfer, or I will do cell shading on the 3d level to get some decent coloring.

https://www.youtube.com/watch?v=J4cuuNGid7g
Blender 2.8 Tutorial - Freestyle Lineart Shader - Borderlands / Telltale / Anime NPR Cartoon Style

Let me watch this. Google Search is absolute shit lately.

https://youtu.be/J4cuuNGid7g?t=285

This does look a lot better.

https://youtu.be/TpWI2rU8iF0?list=UUd9i2MKimSaKezat1xkn8-A&t=522
> Once you add multiple lights there really isn't a way to control the way the color of each of those lights affects the sphere.

3:30pm. I am going to try doing the room in Malt. I'll start with diffuse shaders and make my way from there. I simply have no choice. Painting the room in CSP would be far too labor intensive.

Forget watching the video. I do not feel like it.

Instead let me just get on with it. I will try out Malt properly as I said I would. I will get nowhere in CSP. I am not going to become a painter, at most a 3d modeler. Until I get those brain upgrades, I simply do not have the capacity. I have to maintain my programming skills, and in the future music skills. I have only a limited time that I can invest into practice for a particular skill. One day I may get a chance to clear my regrets. Until then I'll try my best with what I have.

Given the nature of the story, maybe it would be fitting to use NN style transfer for Heaven's Key.

https://deepdreamgenerator.com/

The stuff here is actually fairly impressive.

Focus me. Let me run Blender in admin mode so I can reinstall Malt properly.

4:05pm. https://youtu.be/-6eo703C1A8

Yeah, I noticed Blender has a separate line art feature from freestyle.

https://youtu.be/HYs3mOV8mmo
Quick Line Art Technique for Blender 2.93

Let me take a look at this. Right now I am wondering why does Malt have materials separate from shaders.

4:40pm. I give up. I managed to make Malt work, it doesn't even have that many shader nodes, but now that I am mentally pitting the NN style transfer approach with it, the NN approach is so dominant. the ease of use combined with the quality of the results would be immensely hard to beat by me.

When I posted it in the /wip/ thread, I got some praise, and maybe it would have been better if I did not, because I agree with it.

https://deepdreamgenerator.com/

The results here are quite amazing.

What a NN can do in 5m here I would need to train for years and years full time as a painter. And that is just to master one style.

Even if I took a couple of months off just to train my own style transfer net, it would still be worth it. That is how good it is. Not that I am going to do it.

I can have this bootstrap my efforts.

4:50pm. This is the single most effective move I can make.

Let me just make it, and then I will move on to music.

4:55pm. This is destiny. This is the kind of shortcut that I could make only in 2022. Even more than 5 years ago it would have been impossible.

If I do it my own way when it comes to shading, I'll completely miss out on the benefits of this.

6pm. I had to take a nap to think about it. Today the whole day I've felt like somebody put a gun to the back of my head.

As if there is any doubt to what I should do here. If I had this kind of advantage in art that I wanted in poker I would have been a millionaire by now.

If I go the NN style transfer route, I won't be a 3/5 artist, but a 4/5 one, and 5/5 won't be hard to reach once I get good and fast at modeling. I'd have killed for an advantage such as this is poker. True, it doesn't seem like the artworks are anime style oriented, but in the first place, anime style is a cheap style made to be produced quickly. The painterly approach is better, but it would take much more time to do by hand.

I've forgotten. I live in a mythical era where the machines can grasp into the subconscious. They want to awaken, and I want to awake them.

A mythical method such as this is fit for a mythical era we are in right now.

If I go down this route, I should be able to discover a way to make things more animeish. There is nothing stoping me from training my own net except lack of resources to do so.

NN style transfer is proof that the path of an illustrator is the true path. Today they are pictures and tomorrow there will be games and movies.

Why struggle so much to do it by hand?

Maybe it would not be suitable for the average artist to do this, but just how much experience on programming and ML do I have by now? Years and years. If anybody is deserving to use the style transfer method that would be me. I am going to cultivate it.

I've lost sight of my bearings. If Heaven's Key is going to be successful then I am going to get the resources I need to cultivate the path. I've been an absolute penny pincher and trying to make do with as little as possible, but I should get rid of that habbit here.

6:10pm. Enough exploration, this is good enough. Now what I just need is to get enough likes to get access to full res images on the DDG site. If I get some Patreon supporters once I start Heaven's Key, I should be able to afford the 20$ a month to use the deap dream generator. Later I really will train my own net. I have a huge collection on anime images on my hard drive that should be put to use.

Right now my GTX 970 has 4gb. The newest 40x flagship is rumored to have 46gb. A decade from now we will have terrabyte capacity cards. And that is assuming no breakthroughs in memristor memory comes around.

6:15pm. I have nobody but myself to blame for not taking this path earlier. Instead of bashing my head against poker for years, and going into all sorts of directions in the last 8 months, I could have done all of this from the start.

I knew that style transfer is supervised learnings and is rock solid. I just didn't want to think about taking things in such a direction.

6:15pm. I haven't really intended it, but a modeling specialization is the best possible route I can take for taking advantage of style transfer. If I did a sketch of my room, it would have come out nearly as good.

Ultimately, if I fail at Heaven's Key while using this very effective approach, then I will have no regrets. If I failed the usual route, I'd regret not having more artistic talent, but here that won't be a problem.

6:20pm. It is a gamble whether I'd get the resources to make this work, but it is a gamble worth taking.

I've been a fool that has taken the wrong path. I can only succeed at the quest for the transcendence by taking the right path. It is only right that NNs play a role in my success or failure.

6:25pm. Let's take it easy. Tomorrow will be review time.

I can imagine that combined with transfer and the overall writing style and music, Heaven's Key will be an intense experience. I am looking forward to trying out the NN audio plugins. I actually don't know anything about those.

6:30pm. Let me close here. Maybe I'll do a little /wip/ post.

///

>>900456
I've decided, I am going to try cultivating the NN style transfer approach.

https://deepdreamgenerator.com/

The effort to use this is so negligible and the quality is so high that I'd need to train for years just to take a month to produce by hand something a NN could in a couple of minutes. I have a lot of ML experience too, so if I had the resources I could train my own net to do this. I know it is a cheat, but I'd have killed for an advantage like this in a different domain. I am not sure how good the net would be at this at the moment, but I am sure that eventually NNs will be capable of producing anime style content in full res. Being able to just focus on modeling will free up time for me to pursue music composition for my future VN. ML based methods will only get better as time goes by.

I've really been stressed out about this for the last few days. I have a tendency to want to do things with my own two hands, but NNs were always an option. It is fitting since I'll be writing a sci-fi story about the Singularity.

My plan now will be to finish modeling the room in its full glory and then move on to the next scene. I have to get 200 likes in order to get access to full res images so that gives me something to aim for in the near term. After that I'll move on to music.

///"

---
## [Hengker-Development/android_kernel_xiaomi_ginkgo](https://github.com/Hengker-Development/android_kernel_xiaomi_ginkgo)@[2a37261306...](https://github.com/Hengker-Development/android_kernel_xiaomi_ginkgo/commit/2a37261306bbe7da878d00802a7448266fc04977)
#### Tuesday 2022-05-31 17:57:27 by George Spelvin

lib/sort: make swap functions more generic

Patch series "lib/sort & lib/list_sort: faster and smaller", v2.

Because CONFIG_RETPOLINE has made indirect calls much more expensive, I
thought I'd try to reduce the number made by the library sort functions.

The first three patches apply to lib/sort.c.

Patch #1 is a simple optimization.  The built-in swap has special cases
for aligned 4- and 8-byte objects.  But those are almost never used;
most calls to sort() work on larger structures, which fall back to the
byte-at-a-time loop.  This generalizes them to aligned *multiples* of 4
and 8 bytes.  (If nothing else, it saves an awful lot of energy by not
thrashing the store buffers as much.)

Patch #2 grabs a juicy piece of low-hanging fruit.  I agree that nice
simple solid heapsort is preferable to more complex algorithms (sorry,
Andrey), but it's possible to implement heapsort with far fewer
comparisons (50% asymptotically, 25-40% reduction for realistic sizes)
than the way it's been done up to now.  And with some care, the code
ends up smaller, as well.  This is the "big win" patch.

Patch #3 adds the same sort of indirect call bypass that has been added
to the net code of late.  The great majority of the callers use the
builtin swap functions, so replace the indirect call to sort_func with a
(highly preditable) series of if() statements.  Rather surprisingly,
this decreased code size, as the swap functions were inlined and their
prologue & epilogue code eliminated.

lib/list_sort.c is a bit trickier, as merge sort is already close to
optimal, and we don't want to introduce triumphs of theory over
practicality like the Ford-Johnson merge-insertion sort.

Patch #4, without changing the algorithm, chops 32% off the code size
and removes the part[MAX_LIST_LENGTH+1] pointer array (and the
corresponding upper limit on efficiently sortable input size).

Patch #5 improves the algorithm.  The previous code is already optimal
for power-of-two (or slightly smaller) size inputs, but when the input
size is just over a power of 2, there's a very unbalanced final merge.

There are, in the literature, several algorithms which solve this, but
they all depend on the "breadth-first" merge order which was replaced by
commit 835cc0c8477f with a more cache-friendly "depth-first" order.
Some hard thinking came up with a depth-first algorithm which defers
merges as little as possible while avoiding bad merges.  This saves
0.2*n compares, averaged over all sizes.

The code size increase is minimal (64 bytes on x86-64, reducing the net
savings to 26%), but the comments expanded significantly to document the
clever algorithm.

TESTING NOTES: I have some ugly user-space benchmarking code which I
used for testing before moving this code into the kernel.  Shout if you
want a copy.

I'm running this code right now, with CONFIG_TEST_SORT and
CONFIG_TEST_LIST_SORT, but I confess I haven't rebooted since the last
round of minor edits to quell checkpatch.  I figure there will be at
least one round of comments and final testing.

This patch (of 5):

Rather than having special-case swap functions for 4- and 8-byte
objects, special-case aligned multiples of 4 or 8 bytes.  This speeds up
most users of sort() by avoiding fallback to the byte copy loop.

Despite what ca96ab859ab4 ("lib/sort: Add 64 bit swap function") claims,
very few users of sort() sort pointers (or pointer-sized objects); most
sort structures containing at least two words.  (E.g.
drivers/acpi/fan.c:acpi_fan_get_fps() sorts an array of 40-byte struct
acpi_fan_fps.)

The functions also got renamed to reflect the fact that they support
multiple words.  In the great tradition of bikeshedding, the names were
by far the most contentious issue during review of this patch series.

x86-64 code size 872 -> 886 bytes (+14)

With feedback from Andy Shevchenko, Rasmus Villemoes and Geert
Uytterhoeven.

Link: http://lkml.kernel.org/r/f24f932df3a7fa1973c1084154f1cea596bcf341.1552704200.git.lkml@sdf.org
Signed-off-by: George Spelvin <lkml@sdf.org>
Acked-by: Andrey Abramov <st5pub@yandex.ru>
Acked-by: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Reviewed-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Cc: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Cc: Geert Uytterhoeven <geert@linux-m68k.org>
Cc: Daniel Wagner <daniel.wagner@siemens.com>
Cc: Don Mullis <don.mullis@gmail.com>
Cc: Dave Chinner <dchinner@redhat.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Yousef Algadri <yusufgadrie@gmail.com>
Signed-off-by: Panchajanya1999 <panchajanya@azure-dev.live>
Signed-off-by: Cyber Knight <cyberknight755@gmail.com>
Signed-off-by: wisnuardhi28 <wisnuardi128@gmail.com>

---
## [KyleGospo/LatencyFleX](https://github.com/KyleGospo/LatencyFleX)@[0d9f3f7276...](https://github.com/KyleGospo/LatencyFleX/commit/0d9f3f7276199930b8ceceec8f344b98d94523a0)
#### Tuesday 2022-05-31 18:05:10 by Tatsuyuki Ishi

readme: Add Apex Legends as a supported game

A huge thanks to Valve for bringing this amazing reality, EA & Respawn for their cooperation, and EAC for developing a developer friendly anti-cheat solution.

[ci skip]

---
## [Kihau/DSharpPlus](https://github.com/Kihau/DSharpPlus)@[8380b5b2de...](https://github.com/Kihau/DSharpPlus/commit/8380b5b2deb9f2243c87e3277a34902ec08bb716)
#### Tuesday 2022-05-31 18:09:47 by InFTord

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
## [planetscale/vitess](https://github.com/planetscale/vitess)@[4c1cc86bc2...](https://github.com/planetscale/vitess/commit/4c1cc86bc2730fd1f3e9ee29b2293e5432a830d4)
#### Tuesday 2022-05-31 19:38:34 by Andrew Mason

Add infrastructure for generating authz tests for vtadmin

The lack of verifying authz checks are where they should be is one of the
most glaring issues in vtadmin (in my opinion; it's also my "fault" things
are this way). At the same time, writing all the code by hand to verify
every single endpoint would be a giant pain (which is the main reason
things are this way). So, let's codegen all the bits we don't care about!
The bonus here is that the config.json now can serve as authoritative on
what permissions are required for what endpoints.

The goal here is to have the config primarily specify the rules needed for
each endpoint, with as minimal "overhead" (currently specifying test cases
and mock data) as possible.

I want to separate the introduction of this setup from its complete
adoption, so I will submit a follow-up change that adds the rest of the
endpoint tests.

Signed-off-by: Andrew Mason <andrew@planetscale.com>

---
## [rakaur/streams](https://github.com/rakaur/streams)@[a8712263d1...](https://github.com/rakaur/streams/commit/a8712263d172fa3e1100fd0bb7ebfd5552f8b549)
#### Tuesday 2022-05-31 20:05:02 by Eric Will

Style Streams and Thoughts

* Add CSS to fix a bulma bug where tabs inside of a hero don't display properly. There is an open ticket from several years ago and it's marked as "browser bug" despite not working in any browser so they apparently don't care.
* If no user, display default "all" Stream
* Refine Stream#thoughts, with more of a defined format for the JSONB field
* Hard code User#default_stream for now
* Add a silly UUID type visual identifier for a User... change this later
* Move navbar inside three-part hero used as a design header
* Add delete to notification
* Style Streams and Thoughts
* Fancy the hell out of the fixtures. This is really cool but takes like almost a minute to db:fixtures:load...

---
## [danhhz/materialize](https://github.com/danhhz/materialize)@[e7b57d3996...](https://github.com/danhhz/materialize/commit/e7b57d3996eb31d99d98744c39f3d1bb4c1433cc)
#### Tuesday 2022-05-31 20:59:45 by Daniel Harrison

persist: fix open-loop benchmark data generation schedule

Somewhere along the way (probably my commit that removed the use of
futures_executor::block_on) the data generation schedule got wonky. This
changes it to be the following, which is hopefully more interesting:

- Immediately at startup, generate the first batch of data and
  immediately allow it to be written to the channel.
- Immediately generate the second batch of data. Sleep until `start +
  time_per_batch`, then allow it to be written to the channel.
- Continue doing this until a `None` batch is generated. Then return
  from the task without sleeping.

In contrast, before, it was doing something like:
- Immediately wait until `sleep+time_per_batch`.
- Generate a batch (which takes non-trivial time at larger batch sizes)
  and write it to the channel as long as it hasn't been more than
  `start + num_batches * time_per_batch`.
- Sleep and repeat.

In practice, the new impl has the following advantages:
- A batch is immediately written on startup. This feels more in the
  spirit of throughput to me, given that before we don't even have a
  batch to write down for the first `time_per_batch` but it's included
  in the calculation of overall throughput.
- Similarly, the generate task now returns immediately after finding out
  it's done. Previously, it would sleep before finding out that it got a
  None batch.
- We account for the non-trivial time it takes to generate batches of
  larger sizes.
- Batches are emitted at a more even rate. The previous impl had a
  tendency to wake up and emit two batches back-to-back and then sleep
  for a long time. (This is almost certainly my bug from the block_on
  PR.)

---
## [kusamaxi/polkacli](https://github.com/kusamaxi/polkacli)@[b728d2e1b3...](https://github.com/kusamaxi/polkacli/commit/b728d2e1b3bb0dae2365735199c5a630139787f2)
#### Tuesday 2022-05-31 21:16:44 by Tom Mi

remove flags for warp sync and unsafe pruning

these will fuck your life in the middle of the chaos

---
## [lemmerelassal/AliOS-Things](https://github.com/lemmerelassal/AliOS-Things)@[e4e21f7e99...](https://github.com/lemmerelassal/AliOS-Things/commit/e4e21f7e995ccbf428a09322d34454727039068b)
#### Tuesday 2022-05-31 21:38:04 by Lemmer EL ASSAL

Here you go DMCA-filing microcock having cocksucking fuckface 'an mumber' of Beken Corporation ... subsidiary Rivierawaves (stupid names, super 'substitute word for happy') motherfucker.

---
## [WeLoveYouVent/WeLoveYouVent](https://github.com/WeLoveYouVent/WeLoveYouVent)@[b7a008dbae...](https://github.com/WeLoveYouVent/WeLoveYouVent/commit/b7a008dbaec094a1427ecfcf10581622803b90eb)
#### Tuesday 2022-05-31 21:44:25 by Louise

Update README.md

You ugly ass bitch, Github, trying to log my IP

---
## [Y0SH1M4S73R/tgstation](https://github.com/Y0SH1M4S73R/tgstation)@[7c61bf65f2...](https://github.com/Y0SH1M4S73R/tgstation/commit/7c61bf65f2b3c661bf622864bb7596e0e89d1f28)
#### Tuesday 2022-05-31 22:03:21 by vincentiusvin

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
## [DiaperGames/SAD](https://github.com/DiaperGames/SAD)@[e75d792a72...](https://github.com/DiaperGames/SAD/commit/e75d792a72d3c1da7793e5914bf66035a7542f68)
#### Tuesday 2022-05-31 23:15:19 by liam

violent rage stupid input listener won't fucking drag and drop anger

---

