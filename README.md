## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-11-04](docs/good-messages/2022/2022-11-04.md)


2,160,156 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,160,156 were push events containing 3,301,550 commit messages that amount to 252,895,925 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 48 messages:


## [saurookadook/sensor-and-motor-tests](https://github.com/saurookadook/sensor-and-motor-tests)@[3110d3b380...](https://github.com/saurookadook/sensor-and-motor-tests/commit/3110d3b3801a3f346a53167f5338e58eb5864733)
#### Friday 2022-11-04 00:04:42 by Andy Maskiell

I did not commit often enough here but holy fucking shit I finally got the wheels to do something

---
## [Nanu308/cmss13](https://github.com/Nanu308/cmss13)@[7cb69c2a8b...](https://github.com/Nanu308/cmss13/commit/7cb69c2a8b6f8895d5475b709183a3f30d05fbeb)
#### Friday 2022-11-04 00:06:01 by Joelampost

Creates a new tile for the predator ship (#1400)

* erm

* yer

* fuck you shaddeh

---
## [RigglePrime/tgstation](https://github.com/RigglePrime/tgstation)@[1810b85553...](https://github.com/RigglePrime/tgstation/commit/1810b855536f05891593b1379e455164f45fab3a)
#### Friday 2022-11-04 00:59:19 by tralezab

Heretics cannot be converted, and are immune to cult stun hands. Instead, the cult is rewarded for sacrificing them with the bloody bastard sword, an oversized SPIN2WIN funblade. + Soul Stealing Fantasy Affix (#69725)

About The Pull Request

Heretics can no longer be converted to a cult, as they follow their own Forgotten Gods.
Instead, Nar'Sie will reward the cult for managing to sacrifice one, with the bastard sword.
The bloody bastard sword has been cleaned up codewise and all that. Because it is a free reward instead of a (removed) progression mechanic of cult, it swings just a bit slower during the spin and doesn't have a jaunt. It's still a !fun! swinging sword of hilarity and death.
BLOODY BASTARD https://www.youtube.com/watch?v=ukznXQ3MgN0
Fantasy weapons can now roll "soul-stealing" weapons. They, on killing something, capture its soul inside the item.

    Add fail conditions that instantly end a spin2win, ala how 

    Mimes can now hold a baguette like a sword by right clicking it #69592 works

Why It's Good For The Game

Bloody bastard sword was fun, it made no sense that heretics were valid converts when they're already worshipping a DIFFERENT evil god granting them powers. Should be in a good spot as a nice little antag to antag special interaction. I fucking love antag to antag special interactions, we should have more of 'em

Fantasy affixes are always a neat thing to throw a new component into
Changelog

cl
add: Heretics can no longer be converted to cult. But sacrificing them is very valuable to Nar'Sie, and she will grant special weapons if you manage to do so.
add: Fantasy affixes can also include soul-stealing items!
/cl

---
## [ttaylorr/git](https://github.com/ttaylorr/git)@[762521e8a5...](https://github.com/ttaylorr/git/commit/762521e8a5a6948501d56d51da3f70df4f3dfdbe)
#### Friday 2022-11-04 01:04:48 by Jeff King

t5516: move plaintext-password tests from t5601 and t5516

Commit 6dcbdc0d66 (remote: create fetch.credentialsInUrl config,
2022-06-06) added tests for our handling of passwords in URLs. Since the
obvious URL to be affected is git-over-http, the tests use http. However
they don't set up a test server; they just try to access
https://localhost, assuming it will fail (because the nothing is
listening there).

This causes some possible problems:

  - There might be a web server running on localhost, and we do not
    actually want to connect to that.

  - The DNS resolver, or the local firewall, might take a substantial
    amount of time (or forever, whichever comes first) to fail to
    connect, slowing down the tests cases unnecessarily.

  - Since there's no server, our tests for "allow" and "warn" still
    expect the clone/fetch/push operations to fail, even though in the
    real world we'd expect these to succeed. We scrape stderr to see
    what happened, but it's not as robust as a more realistic test.

Let's instead move these to t5551, which is all about testing http and
where we have a real server. That eliminates any issues with contacting
a strange URL, and lets the "allow" and "warn" tests confirm that the
operation actually succeeds.

It's not quite a verbatim move for a few reasons:

  - we can drop the LIBCURL dependency; it's already part of
    lib-httpd.sh

  - we'll use HTTPD_URL_USER_PASS, etc, instead of our fake URL. To
    avoid repetition, we'll add a few extra variables.

  - the "https://username:@localhost" test uses a funny URL that
    lib-httpd.sh doesn't provide. We'll similarly construct it in a
    variable. Note that we're hard-coding the lib-httpd username here,
    but t5551 already does that everywhere.

  - for the "domain:port" test, the URL provided by lib-httpd is fine,
    since our test server will always be on an exotic port. But we'll
    confirm in the test that this is so.

  - since our message-matching is done via grep, I simplified it to use
    a regex, rather than trying to massage lib-httpd's variables.
    Arguably this makes it more readable, too, while retaining the bits
    we care about: the fatal/warning distinction, the "uses plaintext"
    message, and the fact that the password was redacted.

  - we'll use the /auth/ path for the repo, which shows that we are
    indeed making use of the auth information when needed.

  - we'll also use /smart/; most of these tests could be done via /dumb/
    in t5550, but setting up pushes there requires extra effort and
    dependencies. The smart protocol is what most everyone is using
    these days anyway.

This patch is my own, but I stole the analysis and a few bits of the
commit message from a patch by Johannes Schindelin.

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Taylor Blau <me@ttaylorr.com>

---
## [Lamella-0587/Skyrat-tg](https://github.com/Lamella-0587/Skyrat-tg)@[3dfeccbf27...](https://github.com/Lamella-0587/Skyrat-tg/commit/3dfeccbf27b8dc53c97c2e9db0f1bdc4fd000ebe)
#### Friday 2022-11-04 01:09:35 by SkyratBot

[MIRROR] Clowns will now always like bananas. [MDB IGNORE] (#17300)

* Clowns will now always like bananas. (#70919)

## About The Pull Request
Clown's liver makes them like bananas, ignoring their racial food
preferences.

## Why It's Good For The Game
I don't think clown moths should vomit from eating bananas. They are
clowns, after all.
Also clowns are healed from eating them, so it's a bit silly that they
vomit from their funny medicine.

## Changelog

:cl:
balance: Non-human clowns enjoy eating bananas now.
/:cl:

* Clowns will now always like bananas.

Co-authored-by: Striders13 <53361823+Striders13@users.noreply.github.com>

---
## [AleziaKurdis/overte](https://github.com/AleziaKurdis/overte)@[4a49631007...](https://github.com/AleziaKurdis/overte/commit/4a49631007af4a471acf179d9a7a4bca19ea6afa)
#### Friday 2022-11-04 01:13:40 by Alezia Kurdis

Added HMD notifications dismissal

Added a gestural way to dismiss the notifications in HMD.

The notifications vanishes after 10 sec. 
But if for any reason we want to accelerate the process (mostly because it hide the view or it is going to appears in photo capture)
In Desktop we can simply click on the notification to get rid of them.
But in HMD, clicking was kinda a pain (assuming the if you want to dismiss the notification is often because they are already annoying you)
have to aim and click is like pressing a button using a fishing pole, it's certainly adding more annoyance to this.
To addressed that, I introduced the "Whoosh!": An easy gesture to dismiss any 3d UI, by simply move one of you controller over you eyes height. (a bit like making flee an annoying fly.)

---
## [peff/git](https://github.com/peff/git)@[583237a251...](https://github.com/peff/git/commit/583237a25171ca5d60956b84551bbb7810299358)
#### Friday 2022-11-04 01:22:46 by Jeff King

ref-filter: fix parsing of signatures without blank lines

When ref-filter is asked to show %(content:subject), etc, we end up in
find_subpos() to parse out the three major parts: the subject, the body,
and the signature (if any).

When searching for the blank line between the subject and body, if we
don't find anything, we try to treat the whole message as the subject,
with no body. But our idea of "the whole message" needs to take into
account the signature, too. Since 9f75ce3d8f (ref-filter: handle CRLF at
end-of-line more gracefully, 2020-10-29), the code instead goes all the
way to the end of the buffer, which produces confusing output.

Here's an example. If we have a tag message like this:

  this is the subject
  -----BEGIN SSH SIGNATURE-----
  ...some stuff...
  -----END SSH SIGNATURE-----

then the current parser will put the start of the body at the end of the
whole buffer. This produces two buggy outcomes:

  - since the subject length is computed as (body - subject), showing
    %(contents:subject) will print both the subject and the signature,
    rather than just the single line

  - since the body length is computed as (sig - body), and the body now
    starts _after_ the signature, we end up with a negative length!
    Fortunately we never access out-of-bounds memory, because the
    negative length is fed to xmemdupz(), which casts it to a size_t,
    and xmalloc() bails trying to allocate an absurdly large value.

    In theory it would be possible for somebody making a malicious tag
    to wrap it around to a more reasonable value, but it would require a
    tag on the order of 2^63 bytes. And even if they did, all they get
    is an out of bounds string read. So the security implications are
    probably not interesting.

We can fix both by correctly putting the start of the body at the same
index as the start of the signature (effectively making the body empty).

Note that this is a real issue with signatures generated with gpg.format
set to "ssh", which would look like the example above. In the new tests
here I use a hard-coded tag message, for a few reasons:

  - regardless of what the ssh-signing code produces now or in the
    future, we should be testing this particular case

  - skipping the actual signature makes the tests simpler to write (and
    allows them to run on more systems)

  - t6300 has helpers for working with gpg signatures; for the purposes
    of this bug, "BEGIN PGP" is just as good a demonstration, and this
    simplifies the tests

Curiously, the same issue doesn't happen with real gpg signatures (and
there are even existing tests in t6300 with cover this). Those have a
blank line between the header and the content, like:

  this is the subject
  -----BEGIN PGP SIGNATURE-----

  ...some stuff...
  -----END PGP SIGNATURE-----

Because we search for the subject/body separator line with a strstr(),
we find the blank line in the signature, even though it's outside of
what we'd consider the body. But that puts us unto a separate code path,
which realizes that we're now in the signature and adjusts the line back
to "sigstart". So this patch is basically just making the "no line found
at all" case match that. And note that "sigstart" is always defined (if
there is no signature, it points to the end of the buffer as you'd
expect).

Reported-by: Martin Englund <martin@englund.nu>
Signed-off-by: Jeff King <peff@peff.net>

---
## [peff/git](https://github.com/peff/git)@[866c2a98d7...](https://github.com/peff/git/commit/866c2a98d7f3de879a22732db1cab06c2b39149b)
#### Friday 2022-11-04 01:23:03 by Jeff King

commit: give a hint when a commit message has been abandoned

If we launch an editor for the user to create a commit
message, they may put significant work into doing so.
Typically we try to check common mistakes that could cause
the commit to fail early, so that we die before the user
goes to the trouble.

We may still experience some errors afterwards, though; in
this case, the user is given no hint that their commit
message has been saved. Let's tell them where it is.

Signed-off-by: Jeff King <peff@peff.net>

---
## [peff/git](https://github.com/peff/git)@[1699885250...](https://github.com/peff/git/commit/1699885250c099205d51d4afdfef799171bec07c)
#### Friday 2022-11-04 01:23:23 by Jeff King

branch: gracefully handle '-d' on orphan HEAD

When deleting a branch, "git branch -d" has a safety check that ensures
the branch is merged either to its upstream, or to HEAD. To do that,
naturally we try to resolve HEAD to a commit object. If we're on an
orphan branch (i.e., HEAD points to a branch that does not yet exist),
that will fail, and we'll bail with an error:

  $ git branch -d to-delete
  fatal: Couldn't look up commit object for HEAD

This usually isn't that big of a deal. The deletion would fail anyway,
since the branch isn't merged to HEAD, and you'd need to use "-D" (or
"-f"). And doing so skips the HEAD resolution, courtesy of 67affd5173
(git-branch -D: make it work even when on a yet-to-be-born branch,
2006-11-24).

But there are still two problems:

  1. The error message isn't very helpful. We should give the usual "not
     fully merged" message, which points the user at "branch -D". That
     was a problem even back in 67affd5173.

  2. Even without a HEAD, these days it's still possible for the
     deletion to succeed. After 67affd5173, commit 99c419c915 (branch
     -d: base the "already-merged" safety on the branch it merges with,
     2009-12-29), made it OK to delete a branch if it is merged to its
     upstream.

We can fix both by removing the die() in delete_branches() completely,
leaving head_rev NULL in this case. It's tempting to stop there, as it
appears at first glance that the rest of the code does the right thing
with a NULL. But sadly, it's not quite true.

We end up feeding the NULL to repo_is_descendant_of(). In the
traditional code path there, we call repo_in_merge_bases_many(). It
feeds the NULL to repo_parse_commit(), which is smart enough to return
an error, and we immediately return "no, it's not a descendant".

But there's an alternate code path: if we have a commit graph with
generation numbers, we end up in can_all_from_reach(), which does
eventually try to set a flag on the NULL commit and segfaults.

So instead, we'll teach the local branch_merged() to treat a NULL as
"not merged". This would be a little more elegant in in_merge_bases()
itself, but that function is called in a lot of places, and it's not
clear that quietly returning "not merged" is the right thing everywhere
(I'd expect in many cases, feeding a NULL is a sign of a bug).

There are four tests here:

  a. The first one confirms that deletion succeeds with an orphaned HEAD
     when the branch is merged to its upstream. This is case (2) above.

  b. Same, but with commit graphs enabled. Even if it is merged to
     upstream, we still check head_rev so that we can say "deleting
     because it's merged to upstream, even though it's not merged to
     HEAD". Without the second hunk in branch_merged(), this test would
     segfault.

  c. The third one confirms that we correctly say "not merged to HEAD"
     when we can't resolve HEAD, and reject the deletion.

  d. Same, but with commit graphs enabled. Without the first hunk in
     branch_merged(), this one would segfault.

Reported-by: Martin von Zweigbergk <martinvonz@google.com>

---
## [mootowncow/topaz](https://github.com/mootowncow/topaz)@[ca7670d77b...](https://github.com/mootowncow/topaz/commit/ca7670d77b3edff0b10b9afd0f854a6cd8e73e43)
#### Friday 2022-11-04 01:34:28 by Shiyo

BLU balance update

Fixed a bug where “additional effects” such as Headbutts stun and Mind Blasts paralyze did not proc if they did 0 damage due to magic shield/dt/mdt/pdt/etc.

Def downs reduced to 10% max(frightful roar only)
Terror Touch reduced to 10%

Pinecone bomb same range as blm nukes
Awful eye is aoe (Conal)
New Trait!

Crit attack bonus III trait - Triumphant Roar + Diamondhide

Ranged spells can now crit regardless of “Crit varies with TP Mod” or not, and CA is not required. This is retail accurate.

 Most melee spells fSTR capped at 22 (except smite of rage?) and all ranged spells have fSTR2 capped at 44

Sandspin - 25 acc down and AOE petrify for 8s. 45s cd

Sprout Smack - +30 bonus MAcc

Wild Oats - -17 VIT and 8% attack down +30 bonus MAcc

Metallic Body - cap at 250

Queasyshroom - Ranged dmg type. also 3/tick plague +30 bonus MAcc

Feather Storm - Ranged dmg type. poison scale up to 30/tick based on lvl +30 bonus MAcc

Bludgeon - revert nerf a bit

Battle Dance - 33 Dex down and 5% crit chance down +30 bonus MAcc

Blood Drain - same range as regurgitation

Death Ray - same range and dmg as regurg. CHR WSC.

Digest - same range as regurgitation

Digest - damage type changed to ranged

Mysterious Light- same range and dmg as regurgitation. INT WSC

MP Drainkiss- same range as regurgitation

Stinking Gas - Choke equal to Cold Wave

Blitzstrahl - same range and dmg as regurgitation

Awful Eye - 10% attack down

Magnetite Cloud - 50% HP

Blood Saber - 33% HP breath. 45s cd.

Refueling - 2/tick refresh

Ice Break - double regurg dmg

Filamented Hold - slow II dMND scaling

Hecatomb Wave - 50% HP

Feather Barrier - 3m phalanx (-23)

Light of Penance - same range as regurgitation. MND WSC 30s recast

Flying Hip Press - 50% HP. Thunder dmg

Bad Breath - 100% HP

Maelstrom - double regurgitations dmg

Spiral Spin - Ranged damage type, heavy hitter ftp like death scissors or subzero

Seedspray - Ranged damage type, same dmg as frenetic rip

Spinal Cleave - piercing, 25% attack bonus, death scissors dmg

Zephyr Mantle - blink amount is Floor(Blue Magic Skill / 50)

Feather Tickle - para 2 dMND scaling and cast time

Sandspray - Blind II scaling acc and -10 macc down

Amplification - 25 HP/tick regen for 90s. 2s cast time. 60s cd.

Reactor Cool - aquaveil 3 charges 15m dura

---
## [MapleAtMorning/Games-Unite](https://github.com/MapleAtMorning/Games-Unite)@[e3ea0ba18d...](https://github.com/MapleAtMorning/Games-Unite/commit/e3ea0ba18d83e7880b3136caa1847f46e6744335)
#### Friday 2022-11-04 03:51:16 by MapleAtMorning

Optimization & Meta Editing

I honestly did a shit ton and can't remember everything I changed. Image widths were set for those who don't change, along with lazy loading and a bit more.

---
## [scalableinternetservices/OffTheRails](https://github.com/scalableinternetservices/OffTheRails)@[cf67af4e74...](https://github.com/scalableinternetservices/OffTheRails/commit/cf67af4e74c6fe0f958920c873a06b87efc210f5)
#### Friday 2022-11-04 04:18:29 by Justin Chang

Did a shitty migration change never do this pls sorry forgive me for my sins

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[e755b4c2c0...](https://github.com/san7890/bruhstation/commit/e755b4c2c0c9d4a1e45580d11867c49bca430513)
#### Friday 2022-11-04 05:43:05 by san7890

AW HELL YEAH WE'RE COOKING WITH ROCKET FUEL

MY BRAIN SHORT CIRCUITED BUT WE'RE GOOD NOW WE'RE GOOD NOW

---
## [xDroidOSS-Pixel/frameworks_base](https://github.com/xDroidOSS-Pixel/frameworks_base)@[269053d7fe...](https://github.com/xDroidOSS-Pixel/frameworks_base/commit/269053d7fe2ad8d2f4761f4262a772cc9478a7bf)
#### Friday 2022-11-04 06:55:26 by Kuba Wojciechowski

[SQUASHED] core: Blacklist pixel system feature from Google Photos

    We want to include the P21 experience flag to enable new features,
    however it seems like Google Photos uses it to decide whether to use the
    TPU tflite delegate. There doesn't seem to be any fallback so we need to
    make sure the feature is not exposed to the app so that a normal
    NNAPI/GPU delegate can be used instead.

    Test: Google Photos editor with PIXEL_2021_EXPERIENCE feature in product
    Signed-off-by: Kuba Wojciechowski <nullbytepl@gmail.com>
    Change-Id: I51a02f8347324c7a85f3136b802dce4cc4556ac5

commit 67eb31b3bb43d06fcc7f6fdb2f92eb486451cae6
Author: kondors1995 <normandija1945@gmail.com>
Date:   Thu Jun 9 17:39:25 2022 +0530

    Core: Extend Pixel experience Blacklist For Google Photos

    Turns out having these brakes Original quality backups.
    Since these indicate that the device is pixel 4 with in the turn brakes device spoofing as OG pixel

    Change-Id: I336facff7b55552f094997ade337656461a0ea1d

commit 508a99cde60b73dc3f1e843d569bca31def35988
Author: ReallySnow <reallysnow233@gmail.com>
Date:   Fri Dec 31 16:40:23 2021 +0800

    base: core: Blacklist Pixel 2017 and 2018 exclusive for Google Photos

    * In this way can use PixelPropsUtils to simulate the Pixel XL prop
      method to use the unlimited storage space of Google Photos
    * Thanks nullbytepl for the idea

    Change-Id: I92d472d319373d648365c8c63e301f1a915f8de9

commit aaf07f6ccc89c2747b97bc6dc2ee4cb7bd2c6727
Author: Akash Srivastava <akashniki@gmail.com>
Date:   Sat Aug 20 19:04:32 2022 +0700

    core: Pixel experience Blacklist For Google Photos for Android 13

    * See, in Android 13 pixel_experience_2022_midyear was added, which needs to be blacklisted aswell

    Change-Id: Id36d12afeda3cf6b39d01a0dbe7e3e9058659b8e

commit 9d6e5749a988c9051b1d47c11bb02daa7b1b36fd
Author: spezi77 <spezi7713@gmx.net>
Date:   Mon Jan 31 19:17:34 2022 +0100

    core: Rework the ph0t0s features blacklist

    * Moving the flags to an array feels more like a blacklist :P
    * Converted the flags into fully qualified package names, while at it

    Signed-off-by: spezi77 <spezi7713@gmx.net>
    Change-Id: I4b9e925fc0b8c01204564e18b9e9ee4c7d31c123

commit d7201c0cff326a6374e29aa79c6ce18828f96dc6
Author: Joey Huab <joey@evolution-x.org>
Date:   Tue Feb 15 17:32:11 2022 +0900

    core: Refactor Pixel features

    * Magic Eraser is wonky and hard to
      enable and all this mess isn't really worth
      the trouble so just stick to the older setup.

    * Default Pixel 5 spoof for Photos and only switch
      to Pixel XL when spoof is toggled.

    * We will try to bypass 2021 features and Raven
      props for non-Pixel 2021 devices as apps usage
      requires TPU.

    * Remove P21 experience system feature check

Change-Id: Iffae2ac87ce5428daaf6711414b86212814db7f2

---
## [classified/android_kernel_oneplus_sm8150](https://github.com/classified/android_kernel_oneplus_sm8150)@[7112098b69...](https://github.com/classified/android_kernel_oneplus_sm8150/commit/7112098b69d5922b7d34c1f6088dad4b0507214e)
#### Friday 2022-11-04 07:35:16 by Jason A. Donenfeld

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
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[8aac90bcbb...](https://github.com/odoo-dev/odoo/commit/8aac90bcbbaf4152d9c43e3af2a6d47f38da1095)
#### Friday 2022-11-04 07:45:20 by qsm-odoo

[FIX] website, *: allow to re-edit company team snippet images

*: website_sale

Since [1], it was not possible to edit a company team snippet image
anymore as soon as the page was saved once. Indeed that commit added
o_not_editable/contenteditable="false" on the parent column to make sure
no text can be added in that column and contenteditable="true" on the
images so that they are still editable (even though HTML-specs-wise
adding contenteditable="true" on images probably does not mean much as
images are self-closing tags, our editor understand that as the ability
to edit the image anyway). That contenteditable="true" part is however
removed when leaving edit mode... and was not restored upon entering
edit mode again.

This fixes the problems with a specific JS patch, we'll review to see if
better can be done in master.

Funny enough, that bug was actually gone in 15.0... by mistake. A recent
bug fix actually reintroduced that isolated bug at [2] (by reintroducing
the fact that images in a non-editable environment are not possible to
edit). The 3 opened tickets this commit mentions were actually reported
for 15.0 immediately after that, while the 14.0 being broken about this
since the beginning apparently did not bother anyone.

Note: as a forward-ported fix, this also takes the opportunity to clean
a bit what was done at [3]. (calling `_super`, no duplicated code,
adding comments, ...).

[1]: https://github.com/odoo/odoo/commit/656cac1bf21c7c5a56aa569008aac58436c747fb
[2]: https://github.com/odoo/odoo/commit/e113bae04a64a8bd341a80736086ab7c25079dd3
[3]: https://github.com/odoo/odoo/commit/e2f7b8fad76dc816b2f6864340d3740446117cdb

opw-3031217
opw-3032482
opw-3035289

closes odoo/odoo#104521

X-original-commit: 1636ba5ed2f8a284bef0930313a85cc3dc7cf072
Signed-off-by: Romain Derie (rde) <rde@odoo.com>
Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[08d3a86670...](https://github.com/tgstation/tgstation/commit/08d3a8667079d12ea34446ba0a4497acbc77d98f)
#### Friday 2022-11-04 08:17:12 by tralezab

The screwdriver cocktail is now the world's worst screwdriver (#70862)

## About The Pull Request

Screwdriver cocktail now secretly works as a screwdriver... just, the
worst one ever. How the fuck are you doing that?!

## Why It's Good For The Game

It's funny and I bet someone has tried this before

## Changelog

:cl:
add: Screwdriver cocktails now work as the world's worst screwdriver
/:cl:

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[cf59b0bba1...](https://github.com/tgstation/tgstation/commit/cf59b0bba1bb13b3459cbd01e441601be5a22383)
#### Friday 2022-11-04 08:26:45 by san7890

Null-checks PR Body in removeGuideComments (#71043)

This is what #71041 was supposed to be.

## About The Pull Request
Hey there,

I was looking at #71028, and I noticed that this workflow failed because
oranges left the PR body blank. I think that's silly, so let's just
include an early return so the whole thing doesn't throw.

This is the error:


![image](https://user-images.githubusercontent.com/34697715/199852746-24b2ed53-442d-4c40-b81d-902236183328.png)
via:
https://github.com/tgstation/tgstation/actions/runs/3382875608/jobs/5618241641

Here's an example PR where I fixed it (on my fork, just expand the
"Remove guide comments" step):
https://github.com/san7890/bruhstation/actions/runs/3389994395/jobs/5633658300

## Why It's Good For The Game

It hurts my heart to see checks red out in trivial situations like this.
## Changelog
Literally nothing here concerns players.

Ignore the commit history I was testing this PR the wrong way and was
effectively gaslighting myself (we're good now though)

---
## [SeigaSeiga/tgstation-local](https://github.com/SeigaSeiga/tgstation-local)@[b2be252eb6...](https://github.com/SeigaSeiga/tgstation-local/commit/b2be252eb61e91f3aac08b1e4160420e444db3e8)
#### Friday 2022-11-04 08:44:51 by san7890

UpdatePaths Readme - Reforged (#70806)

* UpdatePaths Readme - Reforged

I'm a bit tired after typing for the last hour so apologies if some of this stuff is unreadable. Basically, I just took time to add a small blurb about UpdatePaths in MAPS_AND_AWAY_MISSIONS.md, as well as write out examples on how you can properly use every single function UpdatePaths might have. I'm probably missing something? I think I got everything though. Let me know if I should be consistent somehow, but I did deliberately choose different test-cases per example because it's nearly impossible to come up one "generic" fit-all situation that illustrates every possible use of UpdatePaths (to my small mind).

Anyways, hope this helps.

* i fucked up with the TGM format

augh

---
## [Sealed101/tgstation](https://github.com/Sealed101/tgstation)@[ee1aba7a32...](https://github.com/Sealed101/tgstation/commit/ee1aba7a32d73a32694fcf904e166e7985df6676)
#### Friday 2022-11-04 09:02:48 by John Willard

pumping your heart doesnt require to be conscious (#63290)

Simply removes the requirement to be conscious to pump your blood with a cursed heart.
Why It's Good For The Game

Entering crit or falling asleep is basically a life sentence since you are unable to pump your blood while asleep. The player still is manually pumping it, I don't see any reason why the user has to be awake for it.
This also means medical can't revive you, as you'll instantly lose all your blood before you have enough time to wake up to start pumping again. The only IC fix would be to remove your heart entirely, something most doctors wouldn't even notice.
Changelog

cl
fix: You can manually pump your blood while asleep/in crit, rather than instantly lose all your blood and die forever.
/cl

---
## [Kitsunemitsu/lobotomy-corp13](https://github.com/Kitsunemitsu/lobotomy-corp13)@[f0e6476eb0...](https://github.com/Kitsunemitsu/lobotomy-corp13/commit/f0e6476eb051d781f7e4d0be7976dff0ff72fda0)
#### Friday 2022-11-04 09:07:14 by Lance

The Great Workening

Attribute Levels Displayed

No thoughts were had, thoughts injected.

Attribute Levels go brrr

Requested Change Made

WHOOPS WRONG PARENTHESIS

I swear I know how Clamps work

Holy shit how did this not get found out earlier

---
## [cgutierr-zgz/cgutierr-zgz.github.io](https://github.com/cgutierr-zgz/cgutierr-zgz.github.io)@[2c82105707...](https://github.com/cgutierr-zgz/cgutierr-zgz.github.io/commit/2c82105707b60840486adde34d4bc750c66f66b3)
#### Friday 2022-11-04 11:05:24 by Carlos Gutiérrez

Update to pipelines I hate my life please work i implore u

---
## [bazelbuild/bazel](https://github.com/bazelbuild/bazel)@[2232c5b445...](https://github.com/bazelbuild/bazel/commit/2232c5b445f5264b31b53a698f5f0e726d9be249)
#### Friday 2022-11-04 11:11:10 by Christopher Peterson Sauer

Move Boost into C++ Docs; Add Libraries Section

Hi wonderful Bazelers,

This is just a docs change.

Backstory: I'd been looking to make HTTPS requests across platforms from C++. A classic problem if there ever were one, networking being perhaps the most glaring omission in the C++ standard library. Thankfully, this is a problem Bazel can solve well, since most of the problem is the friction of using 3rd party libraries from C++. So, I spun up some build rules to make network requests easy, inspired by collaborating on the boost ones, and set off to add them to the docs.

Along the way, I noticed that the boost rules were in an odd spot: Listed at the language level alongside C++, rather than nested within C++. So I fixed that by nesting Boost inside, added Abseil, and then (hoping you'll forgive my hubris), I'd love to add the rules I just released, since I think they're a solution to a very real need. Perhaps rules for more famous, critical libraries can accumulate there over time, helping Bazel users get set up with the essential tools they need.

Thanks for your consideration!
Chris
(ex-Googler and author of [bazel-compile-commands-extractor](https://github.com/hedronvision/bazel-compile-commands-extractor), also in the docs.)

Closes #16621.

PiperOrigin-RevId: 486106928
Change-Id: I119ccff4f70e66415f8c6ac4930c975e48086bc2

---
## [Stellarthoughts/IS12-Warfare](https://github.com/Stellarthoughts/IS12-Warfare)@[538a379161...](https://github.com/Stellarthoughts/IS12-Warfare/commit/538a379161113a7a32f810b0518dc87298e234f5)
#### Friday 2022-11-04 11:15:13 by Matt

Holy shit DMLang shut the fuck up about backslashes!

---
## [newstools/2022-the-nation-ng](https://github.com/newstools/2022-the-nation-ng)@[a73226e0e5...](https://github.com/newstools/2022-the-nation-ng/commit/a73226e0e592ea8f3d0cd8b609a4e6edcd37cd96)
#### Friday 2022-11-04 12:21:09 by Billy Einkamerer

Created Text For URL [thenationonlineng.net/dont-retaliate-if-your-boyfriend-annoys-you-mike-ezuruonye/]

---
## [biglizards/hypothetical-engine](https://github.com/biglizards/hypothetical-engine)@[3cbd7ee951...](https://github.com/biglizards/hypothetical-engine/commit/3cbd7ee951ad59097e005debcbcfc5cb0ea9b372)
#### Friday 2022-11-04 13:00:47 by biglizards

Add GUI, change folder structure

+ added nanogui
+ added a callback thing in engine.cpp because i'm lazy
+++ added like a billion extra folders in ext
    (i'm pushing the headers now)
~ slightly changed everything else, but in ways i can't quite remember
  or care about
~ maybe it compiles, probably not on linux because i've only done
  .libs so far
~ oh yeah I also changed the compile script (and removed all the ugly
  absolute paths, replacing them with brittle and unsafe relative paths)
+ moved out some window code into its own file

---
## [rullzer/password-purgatory-api](https://github.com/rullzer/password-purgatory-api)@[63dd1c4214...](https://github.com/rullzer/password-purgatory-api/commit/63dd1c42147c867a1fa4a96ec3519d09a37a2369)
#### Friday 2022-11-04 13:50:07 by Arjun G

Include one season of the year

Remember the joke about PasswordSummer2022 changing to PasswordWinter2022 on rotation? Yeah, this is that.

---
## [thecsw/thecsw.github.io](https://github.com/thecsw/thecsw.github.io)@[c9cde8efdb...](https://github.com/thecsw/thecsw.github.io/commit/c9cde8efdbb44b27e3e9ba9cab376bbcc4b530ea)
#### Friday 2022-11-04 14:47:01 by Ubuntu

[ASTRIE] Added a new fortune: ** 308; 12022 H.E.

It’s raining, MY GOD I love rain. I woke up today and felt this gloomy and more melancholic vibe in the air. My bedroom is darker than usual. It’s chillier than usual. The air smells like pure bliss. Time goes slower. Tiny notes of romance are floating in the aura around. They’re so subtle that be sure to feel them through or you’ll miss out. What a weather, what a morning. What a day! Did I tell you it’s also going to rain for the rest of the day? It will! I love this. I love this. Thank you. God’s in his Heaven; all is right with the world. What day is itv well, it’s today! “Ah, my favorite,” Pooh replied.

---
## [Toqueer/docs](https://github.com/Toqueer/docs)@[489957750e...](https://github.com/Toqueer/docs/commit/489957750e86d6855b275d250eaa1faf5b4b9aae)
#### Friday 2022-11-04 15:50:57 by Toqueer

Also to work for peace and security

Also to work for peace and security

Also take care of each other

It will be even better if you have a good and lovely girlfriend

Also to act fairly

---
## [devhausleipzig/camp7-team-project](https://github.com/devhausleipzig/camp7-team-project)@[d71ad20822...](https://github.com/devhausleipzig/camp7-team-project/commit/d71ad208221995d81b09c7bf31e283e027a19b49)
#### Friday 2022-11-04 16:28:19 by Chirag Singal

Dear Franz, life has been tough, and it has been some pleasure when I worked on this project, but majorly it was a pain in the ass and also my heart, my breaks now as I type this message to tell you that I am a nincompoop

---
## [jinxynii/coyote-bayou-goobery](https://github.com/jinxynii/coyote-bayou-goobery)@[288f673652...](https://github.com/jinxynii/coyote-bayou-goobery/commit/288f6736526554c75abbcb09c92acb457be1c9b0)
#### Friday 2022-11-04 17:04:00 by Superlagg

Merge remote-tracking branch 'upstream/master' into that-stupid-fuckin-dumb-shitass-fuckin--fuck-fuckass-shitfuck-gun-thing-that-isnt-alll-that-bad-honestly

---
## [downTwo/AutoDownFilesToDrive](https://github.com/downTwo/AutoDownFilesToDrive)@[1cdc26e4ce...](https://github.com/downTwo/AutoDownFilesToDrive/commit/1cdc26e4cec9ef3ce209bf609b36a4be0040984e)
#### Friday 2022-11-04 18:02:16 by downTwo

(けもケット12) [ズンドコ精子バンク (いもたこなんきん)] Holy shit, Happy Hell! (ヘルヴァボス)

---
## [dsmith328/LC13Master](https://github.com/dsmith328/LC13Master)@[fe3e6ea6b0...](https://github.com/dsmith328/LC13Master/commit/fe3e6ea6b08b1ec21fe9e5df86682b3f2a7aaabb)
#### Friday 2022-11-04 18:06:39 by Lance

Initial Commit

Fairy Festival and Wellcheers

Second Commit

Fairy Festival Final, Bald, and Summon_Backup Fix

Third Commit

Training Rabbit, Spider Bud, Old Lady, Beauty and the Beast, Dingle Dangle

Partial Commit

Crumbling Armor

4th Commit

Crumbling Armor, Bloodbath, and We Can Change Anything

4.1 Commit

Moved to a better place.

Second Commit

White Lake

Temp WL/SG Commit

Second Commit

Silent Girl finish and Red Queen

Small SG Fix

Fixed Proc Call

Removed Commented Code

Removed Redundant Code

Second Commit

Punishing Bird attack chance increase. Tutorial Abnos can't be targetted hit by Pink Midnight. Party Everlasting doesn't move until it's summoned backup. Staining Rose unique buff. Temporary non-breaching.

Second Commit

Laetitia hugs people!

Third Commit

We Can Change Anything has grinding noises and update image statement.

Fourth Commit

Scaredy Cat searches for other Oz Abnos while Pink Midnight is occuring. Happy Teddy Bear does not breach from Pink Midnight.

Fifth Commit

Price of Silence, Queen Bee, and Knight of Despair

Sixth Commit

Melting Love revokes gift on breach

Seventh Commit

Shrimp sends his regards

Eighth Commit

Removed left over false bool

Major Commit

General Bee: Faction Checking
Queen of Hatred: Pink Midnight "friendly" breach
Queen Bee: Bee Faction Inheritance
Bottle of Tears: Breach Functionality
Fairy Festival: Fairy Faction Inheritance & Resistance Nerf
White Lake: Debug Removal
Red Queen: Following Diamonds, Diamonds don't fire unless they'd have clear LoS, Diamonds dismember on kill.
Laetitia: Fear Reduced while Breaching.
Silent Girl: Added "Party Starter" ability; Every 5 minutes while she's breached a nearby abnormality's counter will decrease by 1.
White Night: Pink Midnight Functionality, including designating WAW+ Abnormalities as Apostles.

10th Commit

Fixed Ambiguous "If"

11th Commit

General Bee: locked breaching to once per round, just in case.
Despair Knight: Made buff into status effect (placeholder Alert)
Staining Rose: Adjusted Buff

12th Commit

Despair Knight: Status Effect Refined, Icon added

13th Commit

TransferVar and RememberVar documentation and fix.
General Bee only ever breaches once per round, making her scarier if she's not been let out pre-Pink Midnight.

Silence Update

File names were changed

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[075e5cfcde...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/075e5cfcded0c8e62f40b5db66b4bfb77c3708e5)
#### Friday 2022-11-04 19:11:07 by SkyratBot

[MIRROR] Brimdemons & Lobstrosities drop (slightly) useful organs [MDB IGNORE] (#17289)

* Brimdemons & Lobstrosities drop (slightly) useful organs (#70546)

Goliaths, Legions, Watchers, and (as of recently) Bileworms all drop
something vaguely useful when they die.
Brimdemons and Lobstrosities do not. This PR aims to fix that, so that
there's at least some vague benefit to hunting them.

In this case it takes the form of organs you get when you butcher them,
similar to the regenerative core from Legions.
As they're similar to the regenerative core, I modified the regenerative
core to extend from a new common "monster core" typepath which these two
new organs also extend.
Like the regenerative core, both of these items do something when used
and something slightly different if you go to the effort of having
someone implant them into your body. They also decay over time, and you
can use stabilising serum to prevent this from happening.

https://user-images.githubusercontent.com/7483112/195967746-55a7d04d-224e-412d-aedc-3a0ec754db3d.mp4

The Rush Gland from the Lobstrosity lets you do a little impression of
their charging attack, making you run very fast for a handful of seconds
and ignoring slowdown effects. Unlike a lobstrosity you aren't actually
built to do this so if you run into a mob you will fall over, and if you
are doing this on the space station running into any dense object will
also make you fall over (it shouldn't make you _too_ much of a pain for
security to catch).
The idea here is that you use this to save time running back and forth
from the mining base.

The Brimdust Sac from the Brimdemon covers you in exploding dust. The
next three times you take Brute damage some of the dust will explode,
dealing damage equal to an unupgraded PKA shot to anything near you (but
not you).
If you do this in a space station not only is the damage proportionally
lower (still matching the PKA), but it _does_ effect you and also it
sets you on fire. You can remove the buff by showering it off.
The idea here is that you use this for minor revenge damage on enemies
whose attacks you don't manage to dodge.

https://user-images.githubusercontent.com/7483112/195967811-0b362ba9-2da0-42ac-bd55-3809473cbc74.mp4

If you implant the Rush Gland then you can use it once every 3 minutes
without consuming it, and the buff lasts very slightly longer. It will
automatically trigger itself if your health gets low, which might be
good (helps you escape a rough situation) or bad (didn't want to use it
yet).

https://user-images.githubusercontent.com/7483112/195967888-f63f7cbd-60cd-4309-8004-203afc5b2153.mp4

If you implant the Brimdust Sac then you can use it once every 3 minutes
to shake off cloud of dust which gives the buff to everyone nearby, if
you want to kit out your miner squad. The dust cloud also makes you
cough if you stand in it, and it's opaque. If you catch fire with this
organ inside you and aren't in mining atmosphere then it will explode
inside of your abdomen, which should probably be avoided, resultingly it
is very risky to use this on the space station.

* Brimdemons & Lobstrosities drop (slightly) useful organs

* update modular

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: Tom <8881105+tf-4@users.noreply.github.com>

---
## [BillyFletcher99/a-new-leaf-application](https://github.com/BillyFletcher99/a-new-leaf-application)@[38594ef9f2...](https://github.com/BillyFletcher99/a-new-leaf-application/commit/38594ef9f2c8c12d2abb6b8a3d809f55e1b31942)
#### Friday 2022-11-04 19:58:19 by Musty Braid

god's in his heaven and all's right with the world

---
## [builderdev212/RookEngine](https://github.com/builderdev212/RookEngine)@[646441ce97...](https://github.com/builderdev212/RookEngine/commit/646441ce978623baceb7a4ce390a9c1a9d4b7955)
#### Friday 2022-11-04 19:58:43 by builderdev212

Finally fixed menu bug with addition/removing.

The cursed bug has finally been fixed. Note to self. Arrays suck.

---
## [boryas/linux](https://github.com/boryas/linux)@[d21f4b7ffc...](https://github.com/boryas/linux/commit/d21f4b7ffc22c009da925046b69b15af08de9d75)
#### Friday 2022-11-04 20:04:21 by Douglas Anderson

pinctrl: qcom: Avoid glitching lines when we first mux to output

Back in the description of commit e440e30e26dd ("arm64: dts: qcom:
sc7180: Avoid glitching SPI CS at bootup on trogdor") we described a
problem that we were seeing on trogdor devices. I'll re-summarize here
but you can also re-read the original commit.

On trogdor devices, the BIOS is setting up the SPI chip select as:
- mux special function (SPI chip select)
- output enable
- output low (unused because we've muxed as special function)

In the kernel, however, we've moved away from using the chip select
line as special function. Since the kernel wants to fully control the
chip select it's far more efficient to treat the line as a GPIO rather
than sending packet-like commands to the GENI firmware every time we
want the line to toggle.

When we transition from how the BIOS had the pin configured to how the
kernel has the pin configured we end up glitching the line. That's
because we _first_ change the mux of the line and then later set its
output. This glitch is bad and can confuse the device on the other end
of the line.

The old commit e440e30e26dd ("arm64: dts: qcom: sc7180: Avoid
glitching SPI CS at bootup on trogdor") fixed the glitch, though the
solution was far from elegant. It essentially did the thing that
everyone always hates: encoding a sequential program in device tree,
even if it's a simple one. It also, unfortunately, got broken by
commit b991f8c3622c ("pinctrl: core: Handling pinmux and pinconf
separately"). After that commit we did all the muxing _first_ even
though the config (set the pin to output high) was listed first. :(

I looked at ideas for how to solve this more properly. My first
thought was to use the "init" pinctrl state. In theory the "init"
pinctrl state is supposed to be exactly for achieving glitch-free
transitions. My dream would have been for the "init" pinctrl to do
nothing at all. That would let us delay the automatic pin muxing until
the driver could set things up and call pinctrl_init_done(). In other
words, my dream was:

  /* Request the GPIO; init it 1 (because DT says GPIO_ACTIVE_LOW) */
  devm_gpiod_get_index(dev, "cs", GPIOD_OUT_LOW);
  /* Output should be right, so we can remux, yay! */
  pinctrl_init_done(dev);

Unfortunately, it didn't work out. The primary reason is that the MSM
GPIO driver implements gpio_request_enable(). As documented in
pinmux.h, that function automatically remuxes a line as a GPIO. ...and
it does this remuxing _before_ specifying the output of the pin. You
can see in gpiod_get_index() that we call gpiod_request() before
gpiod_configure_flags(). gpiod_request() isn't passed any flags so it
has no idea what the eventual output will be.

We could have debates about whether or not the automatic remuxing to
GPIO for the MSM pinctrl was a good idea or not, but at this point I
think there is a plethora of code that's relying on it and I certainly
wouldn't suggest changing it.

Alternatively, we could try to come up with a way to pass the initial
output state to gpio_request_enable() and plumb all that through. That
seems like it would be doable, but we'd have to plumb it through
several layers in the stack.

This patch implements yet another alternative. Here, we specifically
avoid glitching the first time a pin is muxed to GPIO function if the
direction of the pin is output. The idea is that we can read the state
of the pin before we set the mux and make sure that the re-mux won't
change the state.

NOTES:
- We only do this the first time since later swaps between mux states
  might want to preserve the old output value. In other words, I
  wouldn't want to break a driver that did:
     gpiod_set_value(g, 1);
     pinctrl_select_state(pinctrl, special_state);
     pinctrl_select_default_state();
     /* We should be driving 1 even if "special_state" made the pin 0 */
- It's safe to do this the first time since the driver _couldn't_ have
  explicitly set a state. In order to even be able to control the GPIO
  (at least using gpiod) we have to have requested it which would have
  counted as the first mux.
- In theory, instead of keeping track of the first time a pin was set
  as a GPIO we could enable the glitch-free behavior only when
  msm_pinmux_request_gpio() is in the callchain. That works an enables
  my "dream" implementation above where we use an "init" state to
  solve this. However, it's nice not to have to do this. By handling
  just the first transition to GPIO we can simply let the normal
  "default" remuxing happen and we can be assured that there won't be
  a glitch.

Before this change I could see the glitch reported on the EC console
when booting. It would say this when booting the kernel:
  Unexpected state 1 in CSNRE ISR

After this change there is no error reported.

Note that I haven't reproduced the original problem described in
e440e30e26dd ("arm64: dts: qcom: sc7180: Avoid glitching SPI CS at
bootup on trogdor") but I could believe it might happen in certain
timing conditions.

Fixes: b991f8c3622c ("pinctrl: core: Handling pinmux and pinconf separately")
Signed-off-by: Douglas Anderson <dianders@chromium.org>
Reviewed-by: Stephen Boyd <swboyd@chromium.org>
Link: https://lore.kernel.org/r/20221014103217.1.I656bb2c976ed626e5d37294eb252c1cf3be769dc@changeid
Signed-off-by: Linus Walleij <linus.walleij@linaro.org>

---
## [Koi-3088/ForkBot.NET](https://github.com/Koi-3088/ForkBot.NET)@[696d2d4f71...](https://github.com/Koi-3088/ForkBot.NET/commit/696d2d4f71c3f30e7e41b2496c22958ffa8ccbc5)
#### Friday 2022-11-04 20:05:33 by Koi

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
## [farwyler/helix](https://github.com/farwyler/helix)@[973c51c3e9...](https://github.com/farwyler/helix/commit/973c51c3e970aa975f2bd1869d50ce2ae6c6de34)
#### Friday 2022-11-04 20:10:53 by Michael Davis

Remove C-n and C-p from the insert mode keymap (#3340)

These are read-line-like bindings which we'd like to minimize in
insert mode in general.

In particular these two are troublesome if you have a low
`editor.idle-timeout` config and are using LSP completions: the
behavior of C-n/C-p switches from moving down/up lines to moving
down/up the completion menu, so if you hit C-n too quickly
expecting to be in the completion menu, you'll end up moving down
a line instead. Using C-p moves you back up the line but doesn't
re-trigger the completion menu. This kind of timing related change
to behavior isn't realistically that big of a deal but it can be
annoying.

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[9ccd6ecd74...](https://github.com/microsoft/terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Friday 2022-11-04 20:19:40 by Mike Griese

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
## [DennisCorabi/School-2223](https://github.com/DennisCorabi/School-2223)@[81da073b0c...](https://github.com/DennisCorabi/School-2223/commit/81da073b0c95e97c223e7a3078098688eca66021)
#### Friday 2022-11-04 20:23:29 by dennis

Java web pages w/tomcat &  postgres

I hate my life

---
## [withastro/docs](https://github.com/withastro/docs)@[6b97aae394...](https://github.com/withastro/docs/commit/6b97aae394f0cd6dff5b73809d0d1d248c62ee91)
#### Friday 2022-11-04 20:49:13 by Vinicius Victorino

Fix pronouns in Portuguese for Katie Sylor-Miller (#1955)

As you can see by her twitter account https://twitter.com/ksylor, she identifies as she/her. In Portuguese we have different names for male and female job descriptions, in this case arquitetO (male) and arquitetA (female).

Co-authored-by: Yan Thomas <61414485+Yan-Thomas@users.noreply.github.com>

---
## [maurossi/mesa](https://github.com/maurossi/mesa)@[3a9cdd780d...](https://github.com/maurossi/mesa/commit/3a9cdd780de28deeda45600fb5b8b134d91d17f2)
#### Friday 2022-11-04 21:00:50 by Alyssa Rosenzweig

panfrost/ci: Disable trace-based testing

Trace-based testing has not worked for Panfrost. It was a neat
experiment, and I'm glad we tried it, but the results have been mostly
negative for the driver. Disable the trace-based tests.

For testing that specific API features work correctly, we run the
conformance tests (dEQP), which are thorough for OpenGL ES. For big GL
features, we run Piglit, and if there are big GL features that we are
not testing adequately, we should extend Piglit for these. For
fine-grained driver correctness, we are already covered.

Where trace-based testing can fit in is as a smoke test, ensuring that
the overall rendering of complex scenes does not regress. In principle,
that's a lovely idea, but the current implementation has not worked out
for Panfrost thus far. The crux of the issue is that the trace based
tests are based on checksums, not fuzzy-compared reference images. That
requires updating checksums any time rendering changes. However, a
rendering change to a trace is NOT a regression. The behaviour of OpenGL
is specified very loosely. For a given trace, there are many different
valid checksums. That means that correct changes to core code frequently
fail CI after running through the rest of CI, only because a checksum
changed in a still correct way. That's a pain to deal with, exacerbated
by rebase pains, and provides negative value to the project. Some recent
examples of this I've hit in the past two weeks alone:

   panfrost: Enable rendering to 16-bit and 32-bit
   4b49241f7d7 ("panfrost: Use proper formats for pntc varying")
   ac2964dfbd1 ("nir: Be smarter fusing ffma")

The last example were virgl traces, but were especially bad: due to a
rebase fail, I had to update traces /twice/, wasting two full runs of
pre-merge CI across *all* hardware. This was extremely wasteful.

The value of trace-based testing is as a smoke test to check that traces
still render correctly. That is useful, but it turns out that checksums
are the wrong way to go about it. A better implementation would be
storing only a single reference image from a software rasterizer per
trace. No driver-specific references would be stored. That reference
image must never change, provided the trace never changes. CI would then
check rendered results against that image with tolerant fuzzy
comparisons. That tolerance matches with the fuzzy comparison that the
human eye would do when investigating a checksum change anyway. Yes, the
image comparison JavaScript will now report that
0 pixels changed within the tolerance, but there's nothing a human eye
can do with that information other than an error prone copypaste of new
checksums back in the yaml file and kicking it back to CI, itself a
waste of time.

Finally, in the time we've had trace-based testing alongside the
conformance tests, I cannot remember a single actual regression in one
of my commits the trace jobs have identified that the conformance tests
have not also identified. By contrast, the conformance test coverage has
prevented the merge of a number of actual regressions, with very few
flakes or xfail changes, and I am grateful we have that coverage. That
means the value added from the trace jobs is close to zero, while the
above checksum issues means that the cost is tremendous, even ignoring
the physical cost of the extra CI jobs.

If you work on trace-based testing and would like to understand how it
could adapted to be useful for Panfrost, see my recommendations above.
If you work on CI in general and would like to improve Panfrost's CI
coverage, what we need right now is not trace-based testing, it's
GLES3.1 conformance runs on MediaTek MT8192 or MT8195. That hardware is
already in the Collabora LAVA lab, but it's not being used for Mesa CI
as the required kernel patches haven't made their way to mainline yet
and nobody has cherry-picked them to the gfx-ci kernel. If you are a
Collaboran and interested in improving Panfrost CI, please ping
AngeloGioacchino for information on which specific patches need to be
backported or cherry-picked to our gfx-ci kernel. Thank you.

Signed-off-by: Alyssa Rosenzweig <alyssa@collabora.com>
Acked-by: Jason Ekstrand <jason.ekstrand@collabora.com>
Part-of: <https://gitlab.freedesktop.org/mesa/mesa/-/merge_requests/19358>

---
## [a-friendly-ghost/mishnet](https://github.com/a-friendly-ghost/mishnet)@[232fc336ad...](https://github.com/a-friendly-ghost/mishnet/commit/232fc336adff600ae308b4b67473f60527359ce1)
#### Friday 2022-11-04 21:03:02 by a-friendly-ghost

holy shit linus don't leave in unfinished just started code you fucking idiot stupid moron

---
## [mattr-/dotfiles](https://github.com/mattr-/dotfiles)@[de44043c9f...](https://github.com/mattr-/dotfiles/commit/de44043c9f1ce5ad40fa0cb978839f79110633e3)
#### Friday 2022-11-04 21:13:15 by Matt Rogers

Unfuck my cmp config

A bunch of shit changed in how to configure cmp that I didn't realize
but I'm happy to have it working again. Summary of changes:
 - rely on lspkind for icons
 - reconfigure some mappings. they needed mode specifiers apparently
 - reconfigure how sources are specified. apparently they go through the
   `cmp.config.sources` function now.
 - cmp provides a nice function to configure window borders, use it
 - re-enable lspkind, luasnip, and the various nvim-cmp plugins after I
   disabled them.

Now to unfuck LSP next. 😈

---
## [Noot-Noot-Origins/NootNootOrigins](https://github.com/Noot-Noot-Origins/NootNootOrigins)@[9984c50e03...](https://github.com/Noot-Noot-Origins/NootNootOrigins/commit/9984c50e032d89b18c326cc0745591ade778a26f)
#### Friday 2022-11-04 21:48:37 by AwareTortoise

FIXED THE GOD DAMN THING STOP CHANGING CHINESE TWINK

go fuck urself u chinese twink

---
## [derpguy125/recsbr](https://github.com/derpguy125/recsbr)@[e65cce18c2...](https://github.com/derpguy125/recsbr/commit/e65cce18c2bb59fe3d47684365e4c4dba9ea2be9)
#### Friday 2022-11-04 22:06:03 by DG

changes to the errors

because Raichu's way of showing the error was dumb

also i did a japanese ver because fuck you

---
## [HSavinien/cub3d](https://github.com/HSavinien/cub3d)@[216e0d61e5...](https://github.com/HSavinien/cub3d/commit/216e0d61e527bd9bda25def19c97935a734db73e)
#### Friday 2022-11-04 22:41:12 by Theo Mongellaz

reduced number of parameter for error function to less than five. it's fucking ugly and unreadable. thanks the norm

---

