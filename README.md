## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-06-02](docs/good-messages/2022/2022-06-02.md)


1,686,885 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,686,885 were push events containing 2,700,021 commit messages that amount to 197,304,609 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 38 messages:


## [hexagon-geo-surv/linux-stable](https://github.com/hexagon-geo-surv/linux-stable)@[bd7d220a61...](https://github.com/hexagon-geo-surv/linux-stable/commit/bd7d220a614aff4cf48e48c255e60ca057732eff)
#### Thursday 2022-06-02 00:18:03 by Jason A. Donenfeld

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
## [1umbrykid/Hbm-s-Nuclear-Tech-GIT](https://github.com/1umbrykid/Hbm-s-Nuclear-Tech-GIT)@[f481827aa9...](https://github.com/1umbrykid/Hbm-s-Nuclear-Tech-GIT/commit/f481827aa95a8b98ec36eaac3e2774a1ef5e6836)
#### Thursday 2022-06-02 00:27:24 by umbrykid

the shit fuck mk.10342

changes:

- ported the cc plasma gun model and you can find it in the creative tab i think

---
## [Zonespace27/Skyrat-tg](https://github.com/Zonespace27/Skyrat-tg)@[a3c0819e80...](https://github.com/Zonespace27/Skyrat-tg/commit/a3c0819e8091ab99a5ab8f53b59c4687e5b2f2cf)
#### Thursday 2022-06-02 00:34:01 by SkyratBot

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
## [Shadow-Quill/tgstation](https://github.com/Shadow-Quill/tgstation)@[92fda5014d...](https://github.com/Shadow-Quill/tgstation/commit/92fda5014dbc8ba64c19848e693c179af35da2ac)
#### Thursday 2022-06-02 00:37:21 by san7890

Makes Hell Microwaves Not Use Power (#67413)

Hey there,

I was informed that the holodeck program Microwave Paradise would draw and suck power out of an APC. Didn't intend for that to happen, and while funny, I don't really want to arm the crew with le epic power sink with very little effort than pressing a button, or warranting this to eventually be locked to "dangerous" programs. So, let's change such that this subtype of microwaves that can not be constructed (only mapped/spawned) doesn't consume any power. I don't know why it drew off the nearest APC or how that works, but this seems to be alright.

It's not possible to deconstruct machinery spawned in at the Holodeck (which I verified while testing this PR), so do not worry about people using this to bypass the power economy for whzhzhzhz purposes.

---
## [lonfom169/Stockfish](https://github.com/lonfom169/Stockfish)@[cb9c2594fc...](https://github.com/lonfom169/Stockfish/commit/cb9c2594fcedc881ae8f8bfbfdf130cf89840e4c)
#### Thursday 2022-06-02 00:45:25 by Tomasz Sobczyk

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
## [dcunited001/zettelkasten](https://github.com/dcunited001/zettelkasten)@[e28e9c44df...](https://github.com/dcunited001/zettelkasten/commit/e28e9c44df0a40c87a73fa4f905fe9a7b7a1d530)
#### Thursday 2022-06-02 02:51:18 by David Conner

after using org-krita with emacs for first time

* all this shit happens (some my fault, some fairly suspicious)

* tried switching out hard drives to use windows on new laptop

* then can't boot from the other linux drive

* then I found out "i'm feeling lucky" is for google searches

* ... not bios updates

* then backed up all files to another disk for syncthing on a server

* then ... promptly deleted the luks key from my password file

* ... with no password history, because i'm paranoid

* ... but paranoid for no reason bc any semblance of security/privacy
  in my life is some kind of sardonic joke

* and of course it happens at the beginning of a new semester

---
## [VideoGameSmash12/WNT](https://github.com/VideoGameSmash12/WNT)@[cd8177a07c...](https://github.com/VideoGameSmash12/WNT/commit/cd8177a07c642e01da55317e2cfe664caaa646c3)
#### Thursday 2022-06-02 03:02:36 by Video

Prevents WNT from launching when Shadow Client is installed

Shadow is a client created by a group of individuals with a single goal in mind: griefing and crashing servers. Instead of adding support for the mod like I have with DeviousMod, Meteor, and (soon) Wurst, I have decided set a flag in the mod JSON to deliberately prevent the game from booting if it detects Shadow Client.

### Reason #1 - It doesn't work anyways
I had a friend test the mod and quite bluntly, Shadow breaks too much shit, including WNT. I could totally fix it on my own free time, but why should I even bother?

### Reason #2 - Conflict of interest
Members of the group have recently used exploits in Shadow Client to attack TotalFreedom to the point where they nearly crippled the server on a few occasions. Enabling a group like this to attack the server by implementing support for a client like this in a mod intended to support the administration of is a gigantic conflict of interest.

### Reason #3 - It's personal
I hold a grudge against the group and everything they do because they attacked TF with spambots and exploits. It's as simple as that.

---
## [Rebirth-of-the-Night/Rebirth-Of-The-Night](https://github.com/Rebirth-of-the-Night/Rebirth-Of-The-Night)@[ae294ac4ef...](https://github.com/Rebirth-of-the-Night/Rebirth-Of-The-Night/commit/ae294ac4efb4ff5d328c97922e42c8c0318d6e75)
#### Thursday 2022-06-02 03:41:06 by EliteMeats

demon month

-added a funny sound effect
-tweaked loading screen tips
-removed cringe moster box spawns
-reduced battleaxe attack speed
-tweaked and added sounds to some major advancements
-changed magicite message to be a bit more lore friendly
-removed blockfire mod
-added some splash text
-corrupted cincinnasite now uses death quintessence instead of spores
-gearbox recipe now uses slabs
-handcrank recipe now uses a handle
-added serpentinite to stone oredict
-fixed serpentinite bricks recipe
-removed broken balance quintessence recipe

---
## [AtilioA/AlertaDoTesouro](https://github.com/AtilioA/AlertaDoTesouro)@[e508315b0a...](https://github.com/AtilioA/AlertaDoTesouro/commit/e508315b0ad04d76eb45ddf9cc11b5a9db22c454)
#### Thursday 2022-06-02 03:53:19 by Henriquelay

style(web): Format routes

Sorry, pre-commit for eslint with multiple projects is kinda shit so it's disabled

---
## [Vaern/Hbm-s-Nuclear-Tech-GIT](https://github.com/Vaern/Hbm-s-Nuclear-Tech-GIT)@[b12b97b62e...](https://github.com/Vaern/Hbm-s-Nuclear-Tech-GIT/commit/b12b97b62e0b4368ae47a799202250fc07e472f6)
#### Thursday 2022-06-02 03:56:38 by Vaern

Added Nuke Assembler TE, no functionality yet

god fucking damnit

---
## [kannthus/Skyrat-tg](https://github.com/kannthus/Skyrat-tg)@[694a0740dc...](https://github.com/kannthus/Skyrat-tg/commit/694a0740dc96cdbf22e22884bd9d3adb3c9995c9)
#### Thursday 2022-06-02 04:59:39 by SkyratBot

[MIRROR] Parallax but better: Smooth movement cleanup [MDB IGNORE] (#13414)

* Parallax but better: Smooth movement cleanup (#66567)

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

* Parallax but better: Smooth movement cleanup

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [petre-symfony/upgrading-and-what-s-new-in-Synfony-6](https://github.com/petre-symfony/upgrading-and-what-s-new-in-Synfony-6)@[cbce6365bf...](https://github.com/petre-symfony/upgrading-and-what-s-new-in-Synfony-6/commit/cbce6365bfef87113c51db50d72ff7fd054f6044)
#### Thursday 2022-06-02 05:09:57 by petrero

12.2. Security Upgrades

  New Security System: enable_authenticator_manager
  - But the biggest change in Symfony's security system can be found in config/packages/security.yaml. It's this enable_authenticator_manager. When we upgraded the recipe, it gave us this config... but it was set to true.

  64 lines  config/packages/security.yaml
  security:
    enable_authenticator_manager: false

  This teenie, tiny, innocent-looking line allows us to switch from the old security system to the new one. And what that means, in practice, is that all of the ways you authenticate - like a custom authenticator or form_login or http_basic - will suddenly start using an entirely new system under the hood.

  For the most part, if you're using one of the built-in authentication systems, like form_login or http_basic... you probably won't notice any changes. You can activate the new system by setting this to true... and everything will work exactly like before.... even though the code behind form_login will suddenly be very different. In a lot of ways, the new security system is an internal refactoring to make the core code more readable and to give us more flexibility, when we need it.

  Guard -> Custom Authenticator Conversion
  - However, if you have any custom guard authenticators... like we do, you'll need to convert these to the new authenticator system... which is super fun anyways... so let's do it!

  Open up our custom authenticator: src/Security/LoginFormAuthenticator.php. We can already see that AbstractFormLoginAuthenticator from the old system is deprecated. Change this to AbstractLoginFormAuthenticator.

  I know, it's almost the exact same name: we just swapped "Form" and "Login" around. If your custom authenticator is not for a login form, then change your class to AbstractAuthenticator.

  Oh, and we don't need to implement PasswordAuthenticatedInterface anymore: that was something for the old system.

  Adding the New Authenticator Methods
  - The old Guard system and new authenticator system do the same thing: they figure out who's trying to log in, check the password, and decide what to do on success and failure. But the new authenticator style will feel quite a bit different. For example, you can immediately see that PhpStorm is furious because we now need to implement a new method called authenticate().

  Ok! I'll go down below supports(), go to "Code Generate" - or "cmd" + "N" on a Mac - and implement that new authenticate() method. This is the core of the new authenticator system... and we're going to talk about it in a few minutes.

  Oh, but the old and new systems do share several methods. Like, they both have a method called supports()... but the new system has a bool return type. As soon as we add that, PhpStorm is happy.

  Below, on onAuthenticationSuccess(), it looks like we need to add a return type here as well. At the end, add the Response type from HttpFoundation. Nice! And while we're working on this method, rename the $providerKey argument to $firewallName.

  You don't have to do this, that's just the new name of the argument... and it's more clear.

  Next, down on onAuthenticationFailure(), add the Response return type there as well. Oh, and for onAuthenticationSuccess(), I just remembered that this can return a nullable Response. In some systems - like API token authentication - you will not return a response.

  Finally, we still need a getLoginUrl() method, but in the new system, this accepts a Request $request argument and returns a string.

  Alright! we still need to fill in the "guts", but we at least have all the methods we need.

  Removing supports() for "form login" authenticators
  - And actually, we can remove one of these! Delete the supports() method.

  Ok, this method is still needed by custom authenticators and its job is the same as before. But, if you jump into the base class, in the new system, the supports() method is implemented for you. It checks to make sure that the current request is a POST and that the current URL is the same as the login URL. Basically, it says

  I support authenticating this request if this is a POST request to the login form.

  We wrote our logic a bit differently before, but that's exactly what we were checking.

  Ok, it's time to get to the meat of our custom authenticator: the authenticate() method. Let's do that next.

---
## [zrzxlfe/linux-stable.mirror](https://github.com/zrzxlfe/linux-stable.mirror)@[a06a4dc3a0...](https://github.com/zrzxlfe/linux-stable.mirror/commit/a06a4dc3a08201ff6a8a958f935b3cbf7744115f)
#### Thursday 2022-06-02 05:30:24 by Neil Horman

kmod: add init function to usermodehelper

About 6 months ago, I made a set of changes to how the core-dump-to-a-pipe
feature in the kernel works.  We had reports of several races, including
some reports of apps bypassing our recursion check so that a process that
was forked as part of a core_pattern setup could infinitely crash and
refork until the system crashed.

We fixed those by improving our recursion checks.  The new check basically
refuses to fork a process if its core limit is zero, which works well.

Unfortunately, I've been getting grief from maintainer of user space
programs that are inserted as the forked process of core_pattern.  They
contend that in order for their programs (such as abrt and apport) to
work, all the running processes in a system must have their core limits
set to a non-zero value, to which I say 'yes'.  I did this by design, and
think thats the right way to do things.

But I've been asked to ease this burden on user space enough times that I
thought I would take a look at it.  The first suggestion was to make the
recursion check fail on a non-zero 'special' number, like one.  That way
the core collector process could set its core size ulimit to 1, and enable
the kernel's recursion detection.  This isn't a bad idea on the surface,
but I don't like it since its opt-in, in that if a program like abrt or
apport has a bug and fails to set such a core limit, we're left with a
recursively crashing system again.

So I've come up with this.  What I've done is modify the
call_usermodehelper api such that an extra parameter is added, a function
pointer which will be called by the user helper task, after it forks, but
before it exec's the required process.  This will give the caller the
opportunity to get a call back in the processes context, allowing it to do
whatever it needs to to the process in the kernel prior to exec-ing the
user space code.  In the case of do_coredump, this callback is ues to set
the core ulimit of the helper process to 1.  This elimnates the opt-in
problem that I had above, as it allows the ulimit for core sizes to be set
to the value of 1, which is what the recursion check looks for in
do_coredump.

This patch:

Create new function call_usermodehelper_fns() and allow it to assign both
an init and cleanup function, as we'll as arbitrary data.

The init function is called from the context of the forked process and
allows for customization of the helper process prior to calling exec.  Its
return code gates the continuation of the process, or causes its exit.
Also add an arbitrary data pointer to the subprocess_info struct allowing
for data to be passed from the caller to the new process, and the
subsequent cleanup process

Also, use this patch to cleanup the cleanup function.  It currently takes
an argp and envp pointer for freeing, which is ugly.  Lets instead just
make the subprocess_info structure public, and pass that to the cleanup
and init routines

Signed-off-by: Neil Horman <nhorman@tuxdriver.com>
Reviewed-by: Oleg Nesterov <oleg@redhat.com>
Cc: Andi Kleen <andi@firstfloor.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [zrzxlfe/linux-stable.mirror](https://github.com/zrzxlfe/linux-stable.mirror)@[4c78513e45...](https://github.com/zrzxlfe/linux-stable.mirror/commit/4c78513e457f72d5554a0f6e2eabfad7b98e4f19)
#### Thursday 2022-06-02 06:03:22 by Daniel Vetter

dma-buf: mmap support

Compared to Rob Clark's RFC I've ditched the prepare/finish hooks
and corresponding ioctls on the dma_buf file. The major reason for
that is that many people seem to be under the impression that this is
also for synchronization with outstanding asynchronous processsing.
I'm pretty massively opposed to this because:

- It boils down reinventing a new rather general-purpose userspace
  synchronization interface. If we look at things like futexes, this
  is hard to get right.
- Furthermore a lot of kernel code has to interact with this
  synchronization primitive. This smells a look like the dri1 hw_lock,
  a horror show I prefer not to reinvent.
- Even more fun is that multiple different subsystems would interact
  here, so we have plenty of opportunities to create funny deadlock
  scenarios.

I think synchronization is a wholesale different problem from data
sharing and should be tackled as an orthogonal problem.

Now we could demand that prepare/finish may only ensure cache
coherency (as Rob intended), but that runs up into the next problem:
We not only need mmap support to facilitate sw-only processing nodes
in a pipeline (without jumping through hoops by importing the dma_buf
into some sw-access only importer), which allows for a nicer
ION->dma-buf upgrade path for existing Android userspace. We also need
mmap support for existing importing subsystems to support existing
userspace libraries. And a loot of these subsystems are expected to
export coherent userspace mappings.

So prepare/finish can only ever be optional and the exporter /needs/
to support coherent mappings. Given that mmap access is always
somewhat fallback-y in nature I've decided to drop this optimization,
instead of just making it optional. If we demonstrate a clear need for
this, supported by benchmark results, we can always add it in again
later as an optional extension.

Other differences compared to Rob's RFC is the above mentioned support
for mapping a dma-buf through facilities provided by the importer.
Which results in mmap support no longer being optional.

Note that this dma-buf mmap patch does _not_ support every possible
insanity an existing subsystem could pull of with mmap: Because it
does not allow to intercept pagefaults and shoot down ptes importing
subsystems can't add some magic of their own at these points (e.g. to
automatically synchronize with outstanding rendering or set up some
special resources). I've done a cursory read through a few mmap
implementions of various subsytems and I'm hopeful that we can avoid
this (and the complexity it'd bring with it).

Additonally I've extended the documentation a bit to explain the hows
and whys of this mmap extension.

In case we ever want to add support for explicitly cache maneged
userspace mmap with a prepare/finish ioctl pair, we could specify that
userspace needs to mmap a different part of the dma_buf, e.g. the
range starting at dma_buf->size up to dma_buf->size*2. This works
because the size of a dma_buf is invariant over it's lifetime. The
exporter would obviously need to fall back to coherent mappings for
both ranges if a legacy clients maps the coherent range and the
architecture cannot suppor conflicting caching policies. Also, this
would obviously be optional and userspace needs to be able to fall
back to coherent mappings.

v2:
- Spelling fixes from Rob Clark.
- Compile fix for !DMA_BUF from Rob Clark.
- Extend commit message to explain how explicitly cache managed mmap
  support could be added later.
- Extend the documentation with implementations notes for exporters
  that need to manually fake coherency.

v3:
- dma_buf pointer initialization goof-up noticed by Rebecca Schultz
  Zavin.

Cc: Rob Clark <rob.clark@linaro.org>
Cc: Rebecca Schultz Zavin <rebecca@android.com>
Acked-by: Rob Clark <rob.clark@linaro.org>
Signed-Off-by: Daniel Vetter <daniel.vetter@ffwll.ch>
Signed-off-by: Sumit Semwal <sumit.semwal@linaro.org>

---
## [zrzxlfe/linux-stable.mirror](https://github.com/zrzxlfe/linux-stable.mirror)@[75bfb9aff4...](https://github.com/zrzxlfe/linux-stable.mirror/commit/75bfb9aff45e44625260f52a5fd581b92ace3e62)
#### Thursday 2022-06-02 06:37:30 by Josef Bacik

Btrfs: cleanup error handling in build_backref_tree

When balance panics it tends to panic in the

BUG_ON(!upper->checked);

test, because it means it couldn't build the backref tree properly.  This is
annoying to users and frankly a recoverable error, nothing in this function is
actually fatal since it is just an in-memory building of the backrefs for a
given bytenr.  So go through and change all the BUG_ON()'s to ASSERT()'s, and
fix the BUG_ON(!upper->checked) thing to just return an error.

This patch also fixes the error handling so it tears down the work we've done
properly.  This code was horribly broken since we always just panic'ed instead
of actually erroring out, so it needed to be completely re-worked.  With this
patch my broken image no longer panics when I mount it.  Thanks,

Signed-off-by: Josef Bacik <jbacik@fb.com>
Signed-off-by: Chris Mason <clm@fb.com>

---
## [petre-symfony/upgrading-and-what-s-new-in-Synfony-6](https://github.com/petre-symfony/upgrading-and-what-s-new-in-Synfony-6)@[30e78d9c8c...](https://github.com/petre-symfony/upgrading-and-what-s-new-in-Synfony-6/commit/30e78d9c8c18e7fac0cf16fcffda29841d8e54ac)
#### Thursday 2022-06-02 06:50:45 by petrero

15.2. Hunting Down the Final Deprecations

  Hunting Down the Final Deprecations
  - Done! So... did we do it? Have we achieved zero deprecations and spiritual enlightenment? Go back to the homepage, refresh and... we did! Well, at least that first part... no deprecations! And if we surf around our site a bit... I'm not seeing any deprecations on any of these pages!

  Does this mean we're done? Well, we've manually tested all of the pages that we can click on. But what about POST requests... like submitting the login or registration forms? And what about API endpoints? We have one called /api/me... which doesn't work because I'm not logged in. Log back in as "abraca_admin@example.com" with password "tada" and then... yea, /api/me works.

  We can't see the web debug toolbar for this request, but I bet you already know the trick. Go to /_profiler to see the last ten requests. Here's the POST request to /login. Go down to Logs. Great! That had no deprecations. Go back and also check the API endpoint. If we look at Logs again, it also had no deprecations. We're on a roll!

  Another option, instead of checking the profiler all the time, is to go over to your terminal and tail the log file:

    tail -f var/log/dev.log
  This will constantly stream any new logs. Actually, hit ctrl + C and run that again, but grep for deprecation:

    tail -f var/log/dev.log | grep deprecation
  Perfect. Now, if any logs come through that contain the word "deprecation", we'll see them. And since deprecated code paths trigger a log in the dev environment, this is a powerful tool.

  Deprecated $this->getDoctrine() Method
  - For example, let's go register as a new user. I'll log out, then "Sign up". It asks me for my name, email, and a password. Click to "Agree" to some made-up terms and submit. Oh, my password is too short: my own validation rules coming back to haunt me! Fix that, hit "Register" again and... it works!

  But if we go back to our terminal... rut roo!

    Since symfony/framework-bundle 5.4, method AbstractController::getDoctrine() is deprecated. Inject an instance of ManagerRegistry in your controller instead.

  It's not easy to see where this is coming from in our code, but we did just register... so let's open up RegistrationController. Ah, it's complaining about this right here: the getDoctrine() method is deprecated.

  Instead of using this, we can inject the $entityManager. At the end of the argument list, autowire EntityManagerInterface $entityManager. And... then down here, delete this line because $entityManager is now being injected. Another deprecation gone!

  Logging Deprecations on Production
  Are we done now? Probably. Our project is pretty small, so checking all the pages manually isn't that big of a deal. But for bigger projects, it might be... a huge deal to check everything manually! And you really want to be sure that you didn't miss anything before you upgrade.

  One great option to make sure you didn't miss anything is to log your deprecations on production. Open config/packages/monolog.yaml and go down to when@prod. This has a number of handlers that will log all errors to php://stderr. There's also a deprecation section. With this config, Symfony will log any deprecation messages (that's what this channels: [deprecation] means) to php://stderr.

  This means that you can deploy, wait for an hour, day or week, then... just check the log! If you want to log to a file instead, change the path to something like %kernel.logs_dir%/deprecations.log.

  So that's my favorite thing to do: deploy it, and then see - in the real world - whether or not anyone is still hitting deprecated code paths.

  At this point, I'm not seeing any more deprecations on our web debug toolbar, so I think we're done! And that means we're ready for Symfony 6! Let's do the upgrade next!

---
## [petre-symfony/upgrading-and-what-s-new-in-Synfony-6](https://github.com/petre-symfony/upgrading-and-what-s-new-in-Synfony-6)@[545e2643dd...](https://github.com/petre-symfony/upgrading-and-what-s-new-in-Synfony-6/commit/545e2643ddb494957a61fdb37c6e4d42a9123bb2)
#### Thursday 2022-06-02 06:50:45 by petrero

15.1. Hunting Down the Final Deprecations

  All right team! Let's fix these last few deprecations. One of the trickiest things about these is that, sometimes, they come from third-party bundles. I don't have any examples here, but sometimes you'll get a deprecation and... if you look into it, you'll realize it's not your fault. It's coming from a library or a bundle you're using. When this happens, you need to upgrade that bundle, and hope there's a new version without any deprecations. We actually did have some examples of this way back at the beginning of the tutorial. But... we've already run composer update a few times, and have, apparently, upgraded all of our dependencies to versions without deprecations. Yay, efficiency!

  ROLE_PREVIOUS_ADMIN -> IS_IMPERSONATOR
  - Ok, let's take a look at this list. It says that, in Symfony 5.1, ROLE_PREVIOUS_ADMIN is deprecated and we should use IS_IMPERSONATOR instead. You can show the context or trace to try to get more info, like where this is coming from. It isn't always obvious... and that's one of the trickiest things about deprecations. But this one is coming from base.html.twig.

  Great! Open templates/base.html.twig and search for "previous_admin". In an earlier tutorial, we used this to check if we are currently impersonating a user with Symfony's switch_user feature. If we are, we changed the background to red to make it really obvious.

  To fix the deprecation, very simply, change this to IS_IMPERSONATOR. Copy that... because there's one other spot on this page where we need to do the same thing: IS_IMPERSONATOR. Done! One less deprecation!

  IS_AUTHENTICATED_ANONYMOUSLY -> PUBLIC_ACCESS
  - While we're talking security, open up config/packages/security.yaml and head down to access_control. I have a few entries - /logout, /admin/login - that I want to make absolutely sure are accessible by everyone, even users that are not logged in. To do, we added these rules on top and, previously used IS_AUTHENTICATED_ANONYMOUSLY. So if I go to /logout, only this access_control is matched... and since the role is IS_AUTHENTICATED_ANONYMOUSLY access is always granted.

  In Symfony 6, IS_AUTHENTICATED_ANONYMOUSLY has changed to PUBLIC_ACCESS. So use that in both places.

  If you're wondering why we didn't have a deprecation for this... well... it's a rare case where Symfony is unable to catch that deprecated path and show it to us. This doesn't happen very often, but it's a situation where a tool like SymfonyInsight can help catch this.... even when Symfony itself can't.

  The Deprecated Session Service
  - Okay, the last deprecation on the list says:

    SessionInterface aliases are deprecated, use $requestStack->getSession() instead. It's being referenced by the LoginFormAuthenticator service.

  Let's go check that out! Open src/Security/LoginFormAuthenticator.php. Ahh. I'm autowiring the SessionInterface service. In Symfony 6, that service no longer exists. There are some technical reasons for this... but long story short, the session wasn't ever, really a true service. What you're supposed to do now is get it from the Request.

  So, no big deal. Remove the SessionInterface constructor argument... and we don't need this use statement anymore either.

  Now search for "session". We're using it down in onAuthenticationSuccess(). Fortunately, this already passes us the $request object! So we can just say $request->getSession().

---
## [zrzxlfe/linux-stable.mirror](https://github.com/zrzxlfe/linux-stable.mirror)@[4d6fa57b4d...](https://github.com/zrzxlfe/linux-stable.mirror/commit/4d6fa57b4dab0d77f4d8e9d9c73d1e63f6fe8fee)
#### Thursday 2022-06-02 07:09:55 by Jason A. Donenfeld

macsec: avoid heap overflow in skb_to_sgvec

While this may appear as a humdrum one line change, it's actually quite
important. An sk_buff stores data in three places:

1. A linear chunk of allocated memory in skb->data. This is the easiest
   one to work with, but it precludes using scatterdata since the memory
   must be linear.
2. The array skb_shinfo(skb)->frags, which is of maximum length
   MAX_SKB_FRAGS. This is nice for scattergather, since these fragments
   can point to different pages.
3. skb_shinfo(skb)->frag_list, which is a pointer to another sk_buff,
   which in turn can have data in either (1) or (2).

The first two are rather easy to deal with, since they're of a fixed
maximum length, while the third one is not, since there can be
potentially limitless chains of fragments. Fortunately dealing with
frag_list is opt-in for drivers, so drivers don't actually have to deal
with this mess. For whatever reason, macsec decided it wanted pain, and
so it explicitly specified NETIF_F_FRAGLIST.

Because dealing with (1), (2), and (3) is insane, most users of sk_buff
doing any sort of crypto or paging operation calls a convenient function
called skb_to_sgvec (which happens to be recursive if (3) is in use!).
This takes a sk_buff as input, and writes into its output pointer an
array of scattergather list items. Sometimes people like to declare a
fixed size scattergather list on the stack; othertimes people like to
allocate a fixed size scattergather list on the heap. However, if you're
doing it in a fixed-size fashion, you really shouldn't be using
NETIF_F_FRAGLIST too (unless you're also ensuring the sk_buff and its
frag_list children arent't shared and then you check the number of
fragments in total required.)

Macsec specifically does this:

        size += sizeof(struct scatterlist) * (MAX_SKB_FRAGS + 1);
        tmp = kmalloc(size, GFP_ATOMIC);
        *sg = (struct scatterlist *)(tmp + sg_offset);
	...
        sg_init_table(sg, MAX_SKB_FRAGS + 1);
        skb_to_sgvec(skb, sg, 0, skb->len);

Specifying MAX_SKB_FRAGS + 1 is the right answer usually, but not if you're
using NETIF_F_FRAGLIST, in which case the call to skb_to_sgvec will
overflow the heap, and disaster ensues.

Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>
Cc: stable@vger.kernel.org
Cc: security@kernel.org
Signed-off-by: David S. Miller <davem@davemloft.net>

---
## [teskje/materialize](https://github.com/teskje/materialize)@[3bc0574297...](https://github.com/teskje/materialize/commit/3bc057429749d105bd462595fc3512554be9832f)
#### Thursday 2022-06-02 07:15:56 by Daniel Harrison

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
## [uvhw/uvhw.bitcoin.js](https://github.com/uvhw/uvhw.bitcoin.js)@[a36fe6b70b...](https://github.com/uvhw/uvhw.bitcoin.js/commit/a36fe6b70b33947dd4e6f5990725baf4cff1c4eb)
#### Thursday 2022-06-02 07:18:36 by uvhw

Update README.md

5. Network
The steps to run the network are as follows:

New transactions are broadcast to all nodes.
Each node collects new transactions into a block. 3.Each node works on finding a difficult proof-of-work for its block.
When a node finds a proof-of-work, it broadcasts the block to all nodes.
Nodes accept the block only if all transactions in it are valid and not already spent.
Nodes express their acceptance of the block by working on creating the next block in the chain, using the hash of the accepted block as the previous hash.
Nodes always consider the longest chain to be the correct one and will keep working on extending it. If two nodes broadcast different versions of the next block simultaneously, some nodes may receive one or the other first. In that case, they work on the first one they received, but save the other branch in case it becomes longer. The tie will be broken when the next proof-of-work is found and one branch becomes longer; the nodes that were working on the other branch will then switch to the longer one.

New transaction broadcasts do not necessarily need to reach all nodes. As long as they reach many nodes, they will get into a block before long. Block broadcasts are also tolerant of dropped messages. If a node does not receive a block, it will request it when it receives the next block and realizes it missed one.

6. Incentive
By convention, the first transaction in a block is a special transaction that starts a new coin owned by the creator of the block. This adds an incentive for nodes to support the network, and provides a way to initially distribute coins into circulation, since there is no central authority to issue them. The steady addition of a constant of amount of new coins is analogous to gold miners expending resources to add gold to circulation. In our case, it is CPU time and electricity that is expended.

The incentive can also be funded with transaction fees. If the output value of a transaction is less than its input value, the difference is a transaction fee that is added to the incentive value of the block containing the transaction. Once a predetermined number of coins have entered circulation, the incentive can transition entirely to transaction fees and be completely inflation free.

The incentive may help encourage nodes to stay honest. If a greedy attacker is able to assemble more CPU power than all the honest nodes, he would have to choose between using it to defraud people by stealing back his payments, or using it to generate new coins. He ought to find it more profitable to play by the rules, such rules that favour him with more new coins than everyone else combined, than to undermine the system and the validity of his own wealth.

7. Reclaiming Disk Space
Once the latest transaction in a coin is buried under enough blocks, the spent transactions before it can be discarded to save disk space. To facilitate this without breaking the block’s hash, transactions are hashed in a Merkle Tree [7][2][5], with only the root included in the block’s hash. Old blocks can then be compacted by stubbing off branches of the tree. The interior hashes do not need to be stored.

Diagram showing transactions hashed in merkle tree and then pruned

A block header with no transactions would be about 80 bytes. If we suppose blocks are generated every 10 minutes, 80 bytes * 6 * 24 * 365 = 4.2MB per year. With computer systems typically selling with 2GB of RAM as of 2008, and Moore’s Law predicting current growth of 1.2GB per year, storage should not be a problem even if the block headers must be kept in memory.

8. Simplified Payment Verification
It is possible to verify payments without running a full network node. A user only needs to keep a copy of the block headers of the longest proof-of-work chain, which he can get by querying network nodes until he’s convinced he has the longest chain, and obtain the Merkle branch linking the transaction to the block it’s timestamped in. He can’t check the transaction for himself, but by linking it to a place in the chain, he can see that a network node has accepted it, and blocks added after it further confirm the network has accepted it.

Diagram of merkle branch from longest proof-of-work chain

As such, the verification is reliable as long as honest nodes control the network, but is more vulnerable if the network is overpowered by an attacker. While network nodes can verify transactions for themselves, the simplified method can be fooled by an attacker’s fabricated transactions for as long as the attacker can continue to overpower the network. One strategy to protect against this would be to accept alerts from network nodes when they detect an invalid block, prompting the user’s software to download the full block and alerted transactions to confirm the inconsistency. Businesses that receive frequent payments will probably still want to run their own nodes for more independent security and quicker verification.

9. Combining and Splitting Value
Although it would be possible to handle coins individually, it would be unwieldy to make a separate transaction for every cent in a transfer. To allow value to be split and combined, transactions contain multiple inputs and outputs. Normally there will be either a single input from a larger previous transaction or multiple inputs combining smaller amounts, and at most two outputs: one for the payment, and one returning the change, if any, back to the sender.

Diagram with transactions containing multiple inputs and outputs

It should be noted that fan-out, where a transaction depends on several transactions, and those transactions depend on many more, is not a problem here. There is never the need to extract a complete standalone copy of a transaction’s history.

10. Privacy
The traditional banking model achieves a level of privacy by limiting access to information to the parties involved and the trusted third party. The necessity to announce all transactions publicly precludes this method, but privacy can still be maintained by breaking the flow of information in another place: by keeping public keys anonymous. The public can see that someone is sending an amount to someone else, but without information linking the transaction to anyone. This is similar to the level of information released by stock exchanges, where the time and size of individual trades, the “tape”, is made public, but without telling who the parties were.

Diagram of Traditional Privacy Model and New Privacy Model

As an additional firewall, a new key pair should be used for each transaction to keep them from being linked to a common owner. Some linking is still unavoidable with multi-input transactions, which necessarily reveal that their inputs were owned by the same owner. The risk is that if the owner of a key is revealed, linking could reveal other transactions that belonged to the same owner.

11. Calculations
We consider the scenario of an attacker trying to generate an alternate chain faster than the honest chain. Even if this is accomplished, it does not throw the system open to arbitrary changes, such as creating value out of thin air or taking money that never belonged to the attacker. Nodes are not going to accept an invalid transaction as payment, and honest nodes will never accept a block containing them. An attacker can only try to change one of his own transactions to take back money he recently spent.

The race between the honest chain and an attacker chain can be characterized as a Binomial Random Walk. The success event is the honest chain being extended by one block, increasing its lead by +1, and the failure event is the attacker’s chain being extended by one block, reducing the gap by -1.

The probability of an attacker catching up from a given deficit is analogous to a Gambler’s Ruin problem. Suppose a gambler with unlimited credit starts at a deficit and plays potentially an infinite number of trials to try to reach breakeven. We can calculate the probability he ever reaches breakeven, or that an attacker ever catches up with the honest chain, as follows[8]:

pqqz=== probability an honest node finds the next block probability the attacker finds the next block probability the attacker will ever catch up from z blocks behind

qz={1(q/p)zifp≤qifp>q}
 
q
z
=
{
1	
if
p≤q	(q
/
p
)
z
if
p>q 
}
Given our assumption that p>q, the probability drops exponentially as the number of blocks the attacker has to catch up with increases. With the odds against him, if he doesn’t make a lucky lunge forward early on, his chances become vanishingly small as he falls further behind.

We now consider how long the recipient of a new transaction needs to wait before being sufficiently certain the sender can’t change the transaction. We assume the sender is an attacker who wants to make the recipient believe he paid him for a while, then switch it to pay back to himself after some time has passed. The receiver will be alerted when that happens, but the sender hopes it will be too late.

The receiver generates a new key pair and gives the public key to the sender shortly before signing. This prevents the sender from preparing a chain of blocks ahead of time by working on it continuously until he is lucky enough to get far enough ahead, then executing the transaction at that moment. Once the transaction is sent, the dishonest sender starts working in secret on a parallel chain containing an alternate version of his transaction.

The recipient waits until the transaction has been added to a block and z blocks have been linked after it. He doesn’t know the exact amount of progress the attacker has made, but assuming the honest blocks took the average expected time per block, the attacker’s potential progress will be a Poisson distribution with expected value:

λ=zqp
 
λ
=
z
q
p
To get the probability the attacker could still catch up now, we multiply the Poisson density for each amount of progress he could have made by the probability he could catch up from that point:

∑k=0∞λke−λk!⋅{(q/p)(z−k)1ifk≤zifk>z}
 
 
 
∑
k
=
0
∞
λ
k
e
−
λ
k
!
⋅
{
(q
/
p
)
(
z
−
k
)
if
k≤z	1	
if
k>z 
}
Rearranging to avoid summing the infinite tail of the distribution…

1−∑k=0zλke−λk!(1−(q/p)(z−k))
 
 
1
−
∑
k
=
0
z
λ
k
e
−
λ
k
!
(
1
−
(
q
/
p
)
(
z
−
k
)
)
Converting to C code…

#include &lt;math.h&gt;
double AttackerSuccessProbability(double q, int z)
{
	double p = 1.0 - q;
	double lambda = z * (q / p);
	double sum = 1.0;
	int i, k;
	for (k = 0; k &lt;= z; k++)
	{
		double poisson = exp(-lambda);
		for (i = 1; i &lt;= k; i++)
			poisson *= lambda / i;
		sum -= poisson * (1 - pow(q / p, z - k));
	}
	return sum;
}
Running some results, we can see the probability drop off exponentially with z.

q=0.1
z=0    P=1.0000000
z=1    P=0.2045873
z=2    P=0.0509779
z=3    P=0.0131722
z=4    P=0.0034552  
z=5    P=0.0009137
z=6    P=0.0002428
z=7    P=0.0000647
z=8    P=0.0000173
z=9    P=0.0000046
z=10   P=0.0000012

q=0.3
z=0    P=1.0000000
z=5    P=0.1773523
z=10   P=0.0416605
z=15   P=0.0101008
z=20   P=0.0024804
z=25   P=0.0006132
z=30   P=0.0001522
z=35   P=0.0000379
z=40   P=0.0000095
z=45   P=0.0000024
z=50   P=0.0000006
Solving for P less than 0.1%…

P &lt; 0.001
q=0.10   z=5
q=0.15   z=8
q=0.20   z=11
q=0.25   z=15
q=0.30   z=24
q=0.35   z=41
q=0.40   z=89
q=0.45   z=340
12. Conclusion
We have proposed a system for electronic transactions without relying on trust. We started with the usual framework of coins made from digital signatures, which provides strong control of ownership, but is incomplete without a way to prevent double-spending. To solve this, we proposed a peer-to-peer network using proof-of-work to record a public history of transactions that quickly becomes computationally impractical for an attacker to change if honest nodes control a majority of CPU power. The network is robust in its unstructured simplicity. Nodes work all at once with little coordination. They do not need to be identified, since messages are not routed to any particular place and only need to be delivered on a best effort basis. Nodes can leave and rejoin the network at will, accepting the proof-of-work chain as proof of what happened while they were gone. They vote with their CPU power, expressing their acceptance of valid blocks by working on extending them and rejecting invalid blocks by refusing to work on them. Any needed rules and incentives can be enforced with this consensus mechanism.

References
[1] W. Dai, “b-money,” http://www.weidai.com/bmoney.txt, 1998.

[2] H. Massias, X.S. Avila, and J.-J. Quisquater, “Design of a secure timestamping service with minimal trust requirements,” In 20th Symposium on Information Theory in the Benelux, May 1999.

[3] S. Haber, W.S. Stornetta, “How to time-stamp a digital document,” In Journal of Cryptology, vol 3, no 2, pages 99-111, 1991.

[4] D. Bayer, S. Haber, W.S. Stornetta, “Improving the efficiency and reliability of digital time-stamping,” In Sequences II: Methods in Communication, Security and Computer Science, pages 329-334, 1993.

[5] S. Haber, W.S. Stornetta, “Secure names for bit-strings,” In Proceedings of the 4th ACM Conference on Computer and Communications Security, pages 28-35, April 1997.

[6] A. Back, “Hashcash – a denial of service counter-measure,” http://www.hashcash.org/papers/hashcash.pdf, 2002.

[7] R.C. Merkle, “Protocols for public key cryptosystems,” In Proc. 1980 Symposium on Security and Privacy, IEEE Computer Society, pages 122-133, April 1980.

[8] W. Feller, “An introduction to probability theory and its applications,” 1957.

---
## [abaicus/gutenberg](https://github.com/abaicus/gutenberg)@[3ea2d42b0a...](https://github.com/abaicus/gutenberg/commit/3ea2d42b0a6a206663735a47f9796bd42eda2186)
#### Thursday 2022-06-02 08:39:23 by Dennis Snell

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
## [Suzaku94x/Naruto_Ninpou](https://github.com/Suzaku94x/Naruto_Ninpou)@[80cd503e06...](https://github.com/Suzaku94x/Naruto_Ninpou/commit/80cd503e06b6da03cbec977535c84e603ab9b6ee)
#### Thursday 2022-06-02 09:12:44 by MetalfOxXer

changes

- Reduced Roshi lava mode slow to 10%
- Fixed Hidan R not reflecting damage properly
- Fixed some descriptions
- Fixed Dark Totsuka life steal not working
- Fixed Fuu Yamanaka semi
- Rock Lee W doesn't push creeps anymore / Fixed sfx effect not moving with him
- Itachi additional heal on his D removed
- Return damage from Juubi Skin from Book of Gelel reduced by 50%
- Kid Gaara Q damage type changed from Magic to Normal
- Tenten's R is now slightly slower again
- Improved Torune's T animation slightly maybe
- Rikudou Naruto W from 50x HP and 25x Mana to 75x HP and 50x Mana

---
## [ADDCreative/opencart](https://github.com/ADDCreative/opencart)@[89c304ae61...](https://github.com/ADDCreative/opencart/commit/89c304ae61fb683b2ca8ff7dcf5ceabfc4f5a0eb)
#### Thursday 2022-06-02 09:30:53 by Anton

OC4 return created module_id

IMHO every single model function, creating a row in DB, must return this row id after executed.

I can check `$module_id = $this->db->getLastId();` in my code on clean opencart installation.
But what if this model function calls any `after` events which also insert rows into DB?

This is not a developer friendly software architecture when you need to create hacks, hooks, workarounds and other voodoo magic to get a single value for page redirect.

BUG:
By the way on creating, for example a banner module, on save you are not redirected to created module page. 
So every click on Save button just creates a duplicate of a module.

---
## [avar/git](https://github.com/avar/git)@[0f04cc772a...](https://github.com/avar/git/commit/0f04cc772ab2cb9b14c62de51afd4954b5474b73)
#### Thursday 2022-06-02 10:08:06 by Ævar Arnfjörð Bjarmason

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
## [vitessio/vitess](https://github.com/vitessio/vitess)@[dbfb9a49f7...](https://github.com/vitessio/vitess/commit/dbfb9a49f7c3b067221d0aae0d3c0285e6baf098)
#### Thursday 2022-06-02 10:19:58 by Andrew Mason

[vtadmin] Add infrastructure for generating authz tests for vtadmin (#10397)

* Add infrastructure for generating authz tests for vtadmin

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

* add missing license headers

Signed-off-by: Andrew Mason <andrew@planetscale.com>

* Add make target and CI check

Signed-off-by: Andrew Mason <andrew@planetscale.com>

---
## [SpaceXpanse/rod-core-wallet](https://github.com/SpaceXpanse/rod-core-wallet)@[619f8a27ad...](https://github.com/SpaceXpanse/rod-core-wallet/commit/619f8a27ad0f6a44f0ad1a1e55a0aaaef7a91312)
#### Thursday 2022-06-02 10:35:19 by MarcoFalke

Merge bitcoin/bitcoin#24304: [kernel 0/n] Introduce `bitcoin-chainstate`

2c03cec2ff8cdbfd5da92bfb507d218e5c6435b0 ci: Build bitcoin-chainstate (Carl Dong)
095aa6ca37bf0bd5c5e221bab779978a99b2a34c build: Add example bitcoin-chainstate executable (Carl Dong)

Pull request description:

  Part of: #24303

  This PR introduces an example/demo `bitcoin-chainstate` executable using said library which can print out information about a datadir and take in new blocks on stdin.

  Please read the commit messages for more details.

  -----

  #### You may ask: WTF?! Why is `index/*.cpp`, etc. being linked in?

  This PR is meant only to capture the state of dependencies in our consensus engine as of right now. There are many things to decouple from consensus, which will be done in subsequent PRs. Listing the files out right now in `bitcoin_chainstate_SOURCES` is purely to give us a clear picture of the task at hand, it is **not** to say that these dependencies _belongs_ there in any way.

  ### TODO

  1. Clean up `bitcoin-chainstate.cpp`
     It is quite ugly, with a lot of comments I've left for myself, I should clean it up to the best of my abilities (the ugliness of our init/shutdown might be the upper bound on cleanliness here...)

ACKs for top commit:
  ajtowns:
    ACK 2c03cec2ff8cdbfd5da92bfb507d218e5c6435b0
  ryanofsky:
    Code review ACK 2c03cec2ff8cdbfd5da92bfb507d218e5c6435b0. Just rebase, comments, formatting change since last review
  MarcoFalke:
    re-ACK 2c03cec2ff8cdbfd5da92bfb507d218e5c6435b0 🏔

Tree-SHA512: 86e7fb5718caa577df8abc8288c754f4a590650d974df9d2f6476c87ed25c70f923c4db651c6963f33498fc7a3a31f6692b9a75cbc996bf4888c5dac2f34a13b

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[7d7e3ce6b2...](https://github.com/mrakgr/The-Spiral-Language/commit/7d7e3ce6b27ede4c59f2727212a9274f4e0d3804)
#### Thursday 2022-06-02 10:43:36 by Marko Grdinić

"9am. Let me chill a bit and I will start.

9:25am. Enough of the Rance thread. I'll leave Clyce and Her Majesty's Swarm for later. It is time to do some sculpting. Ah, let me post the reviews up first.

https://www.reddit.com/r/ProgrammingLanguages/comments/v2sevf/comment/iavya3n/?utm_source=share&utm_medium=web2x&context=3

Here it is. Let me post it in the Twitter thread.

9:40am. Let me get started now.

10:20am. I've seen enough. Let me remesh it and I will use the snake hook brush to get the job done.

10:25am. Damn it, these brushes are so hard to work with. They have huge lag.

Hmmm, how do you switch to another object without having to go through object mode? I think it was D or Shift+D but it is not working for me right now. Remember when I did huge line by accident while working on the base mesh? It is possible to do it.

https://www.reddit.com/r/blenderhelp/comments/mfs7ao/how_do_i_switch_objects_in_sculpt_mode/

https://blender.stackexchange.com/questions/183121/how-to-switch-object-in-sculpt-mode

Let me try Alt + Q. Yep that is it. Nice. Let me remesh the pillow.

10:55am. i might have gone overboard on the bed creases.

Ok, that is done. It looks good, so that is all that matters. For the blankets, I'll just make use of the clothing sims. First let me make the mattress a colider.

Huh, does the collision modifier now work for both rigid body, and soft body and cloth sims? Nice.

I thought it was awkward how rigid body and soft body sims had separate ones.

11:25am. Had to take a break for a bit. Let me try out the clothing sim. Admittedly, I hate doing these, but I should get used to it.

11:30am. Doing sims is so annoying. Let me load another file. I can't tell what is going on at all due to the huge lag.

11:40am. Let me do the chores here.

12pm. Let me resume. I've opened a separate file and tried the cloth sim there. It seems to work fine. I only get trouble once I try messing with remesh modifiers. Let me go back to the original file. Let me replicate what I just did here. Then I will try bending the blanket.

12:15pm. I've forgotten just how much cloth sims suck. They suck really, really bad. Sculpting the folds by hand is totally a viable approach. I complained a bit about the cloth brush, but that is nothing compared to how much the cloth sim sucks.

Let me try sculpting the blanket.

12:15pm. I won't use the 0.005 voxel resolution. It is causing the cloth brush sim to take too long. Instead let go for something like 0.02. It does not look as good, but I'll have to make do. Trying to do it in Zbrush is also an option.

12:20pm. The Enable Collision option in the cloth brush is so slow as to be useless. I'll have to disable it.

12:25pm. Let me do more chores.

12:35pm. I am back. I am really struggling how to do this blanket. I need to take a proper sculpting approach to it. Let me mask out the affected pieces, and cut them. Then I will drag them into place. Trying to use the cloth brush with drag or snake hook is not working for me. I should focus only blocking out the blankets and only use the brushes to give the appearance of the folds being there. With cloth sims I will be here all day at this rate. They are so hard to use. The same goes for the cloth brush.

12:40pm. As annoying as it would be to draw the folds, maybe for a person good at it, it would be easier. I keep seeing that guy in /ic/ posting that drawing is easier and I can't help but feel there is a dash of truth to it. Though I think that style transfer would work better with ray traced 3d scenes, it is not like it would not work with drawings.

Also it is not like I could not draw in 3d, I just need to account for the line work from the start.

And it is not fair to compare drawing to cloth sims. I should compare drawing to reg sculpting. I should try that approach. Forget chara modeling. Just do these blankets.

Let me first have breakfast and then I am going to home in on the problem."

---
## [mayhemheroes/git](https://github.com/mayhemheroes/git)@[bdaf1dfae7...](https://github.com/mayhemheroes/git/commit/bdaf1dfae71fdf120fc7253e713ccf0a06cc5558)
#### Thursday 2022-06-02 10:54:03 by Tao Klerks

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
## [makingglitches/GooglePhotoDownload](https://github.com/makingglitches/GooglePhotoDownload)@[eddca81163...](https://github.com/makingglitches/GooglePhotoDownload/commit/eddca811639691c962bd0258e8e4964d20601bf2)
#### Thursday 2022-06-02 11:56:24 by John Sohn

Is it that you fucking people have a problem with anyone enjoying some level of personal success or enjoyment ? Pretty sure I asked this before.
Just curious.
Stop stealing and deleting an innocent enough man's code.
So far as I can tell you're just enabling these monsters to keep raping kids and breeding replacements for them since the people age but the clones don't.
Stop it.
Jesus I just want to finish my fucking programs, I'm a goddamn old man.
Law enforcement is dirty, the feds are dirty, everyones a fucking monster and life was not supposed to result in this kind of horrific unreality. simply put. a species that destroys its young does not survive. if it werent for the preexisting structure of industry and know how that these creatures inhabit like pygmies in roman ruins, or some kind of scifi race using machines of the ancients they don't know how to fix these fucked up THINGS would probably be extinct by now the way everything is going.

---
## [jeroenlooijtu/progressTracker](https://github.com/jeroenlooijtu/progressTracker)@[bb2a43674e...](https://github.com/jeroenlooijtu/progressTracker/commit/bb2a43674ef2d102a150258342a122e6d191b2fc)
#### Thursday 2022-06-02 12:11:04 by Jeroen Looij

search by id works by the cors is still fucked beyond believe omg i want to beat the shit out of express why does one work now and the other doesnt this is giving me fucking aids

---
## [erikem/Test3DProject](https://github.com/erikem/Test3DProject)@[7110d887c7...](https://github.com/erikem/Test3DProject/commit/7110d887c749dba23659b0b31cb6f2a602755153)
#### Thursday 2022-06-02 15:03:59 by erikem

Fixed stupid generation bug that was caused by abbyssmally stupid defaulting coordinates to -1 in 
public int CountBlocks(float cellCheckValue, string cellCheckCondition, int fromRow, int toRow, int fromColumn, int toColumn)

it was something like
public int CountBlocks(float cellCheckValue, string cellCheckCondition, int fromRow=0, int toRow=-1, int fromColumn=0, int toColumn=-1)

And these -1 were handled inside method and converted into the array size (so if array was 10x10 than -1 was converted to 10). The problem was that sometimes code was sendign actual -1 there and it all broke down.

A note to self: NEVER DO SUCH HACKS AGAIN!!!!!!!11!!!!!!111

---
## [Tiktodz/android_kernel_asus_sdm636](https://github.com/Tiktodz/android_kernel_asus_sdm636)@[726c861fa9...](https://github.com/Tiktodz/android_kernel_asus_sdm636/commit/726c861fa9970e81da9f7885833097c6b77ce0c9)
#### Thursday 2022-06-02 16:16:08 by Dave Chiluk

sched/fair: Fix low cpu usage with high throttling by removing expiration of cpu-local slices

commit de53fd7aedb100f03e5d2231cfce0e4993282425 upstream.

It has been observed, that highly-threaded, non-cpu-bound applications
running under cpu.cfs_quota_us constraints can hit a high percentage of
periods throttled while simultaneously not consuming the allocated
amount of quota. This use case is typical of user-interactive non-cpu
bound applications, such as those running in kubernetes or mesos when
run on multiple cpu cores.

This has been root caused to cpu-local run queue being allocated per cpu
bandwidth slices, and then not fully using that slice within the period.
At which point the slice and quota expires. This expiration of unused
slice results in applications not being able to utilize the quota for
which they are allocated.

The non-expiration of per-cpu slices was recently fixed by
'commit 512ac999d275 ("sched/fair: Fix bandwidth timer clock drift
condition")'. Prior to that it appears that this had been broken since
at least 'commit 51f2176d74ac ("sched/fair: Fix unlocked reads of some
cfs_b->quota/period")' which was introduced in v3.16-rc1 in 2014. That
added the following conditional which resulted in slices never being
expired.

if (cfs_rq->runtime_expires != cfs_b->runtime_expires) {
	/* extend local deadline, drift is bounded above by 2 ticks */
	cfs_rq->runtime_expires += TICK_NSEC;

Because this was broken for nearly 5 years, and has recently been fixed
and is now being noticed by many users running kubernetes
(https://github.com/kubernetes/kubernetes/issues/67577) it is my opinion
that the mechanisms around expiring runtime should be removed
altogether.

This allows quota already allocated to per-cpu run-queues to live longer
than the period boundary. This allows threads on runqueues that do not
use much CPU to continue to use their remaining slice over a longer
period of time than cpu.cfs_period_us. However, this helps prevent the
above condition of hitting throttling while also not fully utilizing
your cpu quota.

This theoretically allows a machine to use slightly more than its
allotted quota in some periods. This overflow would be bounded by the
remaining quota left on each per-cpu runqueueu. This is typically no
more than min_cfs_rq_runtime=1ms per cpu. For CPU bound tasks this will
change nothing, as they should theoretically fully utilize all of their
quota in each period. For user-interactive tasks as described above this
provides a much better user/application experience as their cpu
utilization will more closely match the amount they requested when they
hit throttling. This means that cpu limits no longer strictly apply per
period for non-cpu bound applications, but that they are still accurate
over longer timeframes.

This greatly improves performance of high-thread-count, non-cpu bound
applications with low cfs_quota_us allocation on high-core-count
machines. In the case of an artificial testcase (10ms/100ms of quota on
80 CPU machine), this commit resulted in almost 30x performance
improvement, while still maintaining correct cpu quota restrictions.
That testcase is available at https://github.com/indeedeng/fibtest.

Fixes: 512ac999d275 ("sched/fair: Fix bandwidth timer clock drift condition")
Signed-off-by: Dave Chiluk <chiluk+linux@indeed.com>
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Reviewed-by: Phil Auld <pauld@redhat.com>
Reviewed-by: Ben Segall <bsegall@google.com>
Cc: Ingo Molnar <mingo@redhat.com>
Cc: John Hammond <jhammond@indeed.com>
Cc: Jonathan Corbet <corbet@lwn.net>
Cc: Kyle Anderson <kwa@yelp.com>
Cc: Gabriel Munos <gmunoz@netflix.com>
Cc: Peter Oskolkov <posk@posk.io>
Cc: Cong Wang <xiyou.wangcong@gmail.com>
Cc: Brendan Gregg <bgregg@netflix.com>
Link: https://lkml.kernel.org/r/1563900266-19734-2-git-send-email-chiluk+linux@indeed.com
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Signed-off-by: Ratoriku <a1063021545@gmail.com>
Signed-off-by: Peppe289 <gsperanza204@gmail.com>
Signed-off-by: Tiktodz <ewprjkt@proton.me>
Change-Id: I2af9ef3f1397939deb05b2bd263d90f9200b888e

---
## [sunamo/sunamo](https://github.com/sunamo/sunamo)@[170c5e6c9b...](https://github.com/sunamo/sunamo/commit/170c5e6c9b8bec125dc8bee3ef08ac25aab1946f)
#### Thursday 2022-06-02 16:59:42 by Radek Jancik

13604;The message that President Obama delivered in his speech at Notre Dame was: morality is immoral. Pro-life is the extremist position, not a moral position. Yet we should compromise and work to reduce abortions. Where's the compromise between life and death - and why work to reduce the number of them occurring if there's nothing wrong with them?;Rush Limbaugh;death

---
## [tailwindlabs/headlessui](https://github.com/tailwindlabs/headlessui)@[aeac5d03bd...](https://github.com/tailwindlabs/headlessui/commit/aeac5d03bde41bf4659acb3031781eccb37ca5d0)
#### Thursday 2022-06-02 17:06:21 by Robin Malfait

simplify `outside click` behaviour

Here is a little story. We used to use the `click` event listener on the
window to try and detect whether we clicked outside of the main area we
are working in.

This all worked fine, until we got a bug report that it didn't work
properly on Mobile, especially iOS. After a bit of debugging we switched
this behaviour to use `pointerdown` instead of the `click` event
listener. Worked great! Maybe...

The reason the `click` didn't work was because of another bug fix. In
React if you render a `<form><Dialog></form>` and your `Dialog` contains
a button without a type, (or an input where you press enter) then the
form would submit... even though we portalled the `Dialog` to a
different location, but it bubbled the event up via the SyntethicEvent
System. To fix this, we've added a "simple" `onClick(e) { e.stopPropagation() }`
to make sure that click events didn't leak out.

Alright no worries, but, now that we switched to `pointerdown` we got
another bug report that it didn't work on older iOS devices. Fine, let's
add a `mousedown` next to the `pointerdown` event. Now this works all
great! Maybe...

This doesn't work quite as we expected because it could happen that both
events fire and then the `onClose` of the Dialog component would fire
twice. In fact, there is an open issue about this: #1490 at the time of
writing this commit message.
We tried to only call the close function once by checking if those
events happen within the same "tick", which is not always the case...

Alright, let's ignore that issue for a second, there is another issue
that popped up... If you have a Dialog that is scrollable (because it is
greater than the current viewport) then a wild scrollbar appears (what a
weird Pokémon). The moment you try to click the scrollbar or drag it the
Dialog closes. What in the world...?

Well... turns out that `pointerdown` gets fired if you happen to "click"
(or touch) on the scrollbar. A click event does not get fired. No
worries we can fix this! Maybe...

(Narrator: ... nope ...)

One thing we can try is to measure the scrollbar width, and if you
happen to click near the edge then we ignore this click. You can think
of it like `let safeArea = viewportWidth - scrollBarWidth`. Everything
works great now! Maybe...

Well, let me tell you about macOS and "floating" scrollbars... you can't
measure those... AAAAAAAARGHHHH

Alright, scratch that, let's add an invisible 20px gap all around the
viewport without measuring as a safe area. Nobody will click in the 20px
gap, right, right?! Everything works great now! Maybe...

Mobile devices, yep, Dialogs are used there as well and usually there is
not a lot of room around those Dialogs so you almost always hit the
"safe area". Should we now try and detect the device people are
using...?

/me takes a deep breath...

Inhales... Exhales...

Alright, time to start thinking again... The outside click with a
"simple" click worked on Menu and Listbox not on the Dialog so this
should be enough right?

WAIT A MINUTE

Remember this piece of code from earlier:

```js
onClick(event) {
  event.stopPropagation()
}
```

The click event never ever reaches the `window` so we can't detect the
click outside...

Let's move that code to the `Dialog.Panel` instead of on the `Dialog`
itself, this will make sure that we stop the click event from leaking
if you happen to nest a Dialog in a form and have a submitable
button/input in the `Dialog.Panel`. But if you click outside of the
`Dialog.Panel` the "click" event will bubble to the `window` so that we
can detect a click and check whether it was outside or not.

Time to start cleaning:
  - ☑️ Remove all the scrollbar measuring code...
    - Closing works on mobile now, no more safe area hack
  - ☑️ Remove the pointerdown & mousedown event
    - Outside click doesn't fire twice anymore
  - ☑️ Use a "simple" click event listener
    - We can click the scrollbar and the browser ignores it for us

All issues have been fixed! (Until the next one of course...)

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[0c4d9bfe0a...](https://github.com/mrakgr/The-Spiral-Language/commit/0c4d9bfe0a6b65ff618a3bf38e9715273c632fd4)
#### Thursday 2022-06-02 17:59:59 by Marko Grdinić

"https://mangadex.org/chapter/bb6fb096-3d84-4790-8ff9-401c44ff875b/14

Clice has some hard surface modeling porn.

1:20pm. Done with breakfast. let me just chill a bit and then I will get started.

1:50pm. Let me get started. I am going to figure out how to deal with the blanket using regular sculpting.

Damn it, how do you deal with face sets in Blender?

https://youtu.be/2wiDu9yU0M8
How to use Sculpt Face Sets?

I made good use of these in Zbrush.

Oh, you can hide the rest of the mesh by simply pressing H while hovering over the face set.

2:10pm. Progress is coming very hard to me over this. In real life I just fold the blanket, but trying to have it come out right using the move brush if proving be very hard. I might have to give up on doing the folds directly.

https://youtu.be/gNx4v0WVVHo
How to sculpt cloth in 3D?

2:15pm. I've decided, it is too difficult for me to do a mesh that folds in on itself. It was actually my original plan to do it fakely, but as expected I cannot do it. This way does have some disadvantages.I won't be capable of making the middle part completely natural, but that is fine. For most camera angles it won't be noticeable.

https://youtu.be/gNx4v0WVVHo?t=564

Oh yeah, remember how the mono fill pen had the option to not cross over the ref lines. It might be the case that those ref lines might not need to be enclosed areas. This tutorial is really good. I haven't been thinking about tension points at all.

What I could do is put the tension points using vectors and then use the mono fill pen option as light and dark area boundaries. That would be a much easier workflow than trying to make masks work for something like folds.

https://youtu.be/gNx4v0WVVHo?t=575

Still, it would be easier to sculpt lifelike folds than to draw them.

2:40pm. https://youtu.be/CNKWPlrIEww
FOLDED BLANKET Loft

Let me watch this. I really do need a tutorial for how to do a folded blanket.

https://youtu.be/CNKWPlrIEww?t=74

He is going to make the initial shape using NURBs. Really?

2:50pm. Ok, for this blanket it is regular enough that this approach would work. But do I have no choice but to do it like this. Instead of trying this let me use masks do dig into the walls.

2:55pm. Nope, nope, nope.

Let me repeat the process once more. I'll try extracting the folded area using a mask. What I tried just now is using the masks on the crevice area and moved it using the move tool, but I pierced the mesh on the other side. It is not a good technique. A good technique gives you the result you want without much hassle. What I am trying to do here would be pretty easy using drawing, but with sculpting I am simply doing it wrong.

Think of that fold like extracting a plate. That will put me on the correct path.

3:50pm. I do not know why. For some reason it is not smoothing the normals in places correctly. It works in sculpt mode, but not in object mode. Weird.

Ah, I see. I just had to turn off the autosmooth normals. Now it works just fine.

3:55pm. This looks good now. I think I understand the workflow for sculpting blankets.

But I do want to connect the other end to the first one.

4:20pm. This is insanely difficult! It took me how much time...3-4 hours?!

What I did now is not a viable workflow. Let me take a break here.

I think it might be worth mixing in cloth sims into the workflow. True, it might be so slow as to be unusable right now, but that is because I am using >10k faces on the blanket. What if I used 1k faces just to have it land in the right spot, remeshed it and then came in with the cloth brush. The blanket itself did not come out too well.

Right now even I could do it, I feel completely helpless as if I do not have any control over the process.

Sculpting folds on clothing would not be a problem. What the problem with these blankets is is that they fold on each other. I really need a cloth sim to have that land in the right place.

Ok, let me try it. Let me open a separate file just for that kind of experiment. The quad remesher is actually useful here, the regular one...well, I suppose I could do a flod fill with dyntopo. That could also work. But the quad topology is better so why not use it?

4:40pm. This works well. The plan is starting to come together for me.

Let me take a short break here.

5pm. Let me resume. One trouble that I had is that the solidify modifier and extrusion in the normal direction did not work as planned for me. Let me try that again. Did I have insufficient curvature? Or was the gap too narrow? Blender's solidify usually works well. Also how do I bake the cloth sim?

Oh, I just apply the modifier. Yeah, now that it has mostly even quads, the solidify mod works quite well. This folded towel would be such a pain in the ass to do using sculpting. In fact, I do not think it would be possible.

5:15pm. Damn it, I want a break, this was so exhausting. I wanted to deal with the cloth today, but I am only 20% done. With the techniques I have in mind I should be done with this quickly.

GGGGGGGGGGGGGGGGGGGGhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh...Let me give a try!

5:20pm. Merged all the objects on the right bed into one and remeshed it with 1k quad target. In the end it does have 4k faces, but that is in the allowable range.

6:45pm. I'll leave the curtains for tomorrow. I realized today that even 1000 quads for a blanket is too much during the cloth sim. I should have gone with less. Also, the elastic hook cloth brush works better with a strength higher than 1. What is my standing currently?

~* Crease on the beds and the pillows~
~* Put in the blankets and the clothing~
* Do the curtains
* Put in the glass door panes and (optionally) frost it a bit via the roughness setting
* Put in the flats for every object in the room

The curtains won't be too hard. Glass panes I already have, I just need to fiddle with the shader for them a bit. I think I understand how to do folded blankets now. Maybe I should learn how to draw after all? But drawing is a hard sell when it comes to perspective. Different tools have different stregnths.

3d is not actually weak when it comes to doing clothing, it is just that my inexperience with it here made me spend a lot of time needlessly. I'll do it a lot better next time.

Let me gather the tips:

* For folded blankets, use a cloth sim to put it into place and do the higher freq details using the cloth brush.
* Quad remesh the colliders and the blankets to a small quad size before running the sim. Try to go under 1k quads next time so the self collision distance can be set higher.
* Remesh without adaptive quad sizes. Having vertices be too close will cause the cloth sim to go haywire.
* The snake hook cloth brush is great, but has low power even at 1. Try it with brush strength above 1 next time.

Had I followed this advice from the start of the day, I'd have long been done with both the blankets and the curtains.

I'll post the above tips in the /wip/ thread.

7:35pm. Let me close here. I've already started reading manga.

I've decided. The next time I try drawing, I'll stick to using figure tools. That is curves. The very first thing I studied when I started on the art path was the Adobe Illustrator and it struck me that using curves is a good. Since then I've learned a bit of sketching and refinement, but as important as that is, I also need precision. I really like that Yumeko trace video. Drawing lines using curves could be made to work. I keep reading that pen and paper is a lot more precise than a pen tablet and it makes sense to me. At least the one I am using is quite small. It might not be a bad idea to revisit some of that old stuff. Maybe I'll try it once I am done with the current scene.

Having the scene in 3d sort of ruined trying to do it in 2d for me. I'd just be doing that work twice, especially with NN style transfer. But if I was starting work on a new scene it might make more sense.

Before I close, let me try the monofil pen idea.

7:50pm. Hmm, not what I hoped for. It is only useful for larger brushes. Even if you start the stroke on one side, if you skip by accident it will paint on the other side. But it is not like it would be hard to just go in with the eraser and fix that issue. The feature works for erasers as well. Yeah, indeed, I've been having a lot of trouble with figuring out how to cell shade one side dark and the other light, and this tool would be quite useful for that purpose. It should be on by default for all my tools.

Whatever direct precision digital lacks compared to paper, it can make up for it in other ways. Ultimately, people will judge my art itself and not my technique. It does not matter if I use vector curves for my line art if it looks good. There is no set way art should be done. All I need to figure out is the most effective method and then make use of it."

---
## [daviiid99/Pokemon-Pi](https://github.com/daviiid99/Pokemon-Pi)@[ba55af3232...](https://github.com/daviiid99/Pokemon-Pi/commit/ba55af32328a5f4697a595dc85197dfede9683eb)
#### Thursday 2022-06-02 18:45:25 by daviiid99

Multiple improvements
What's new
- New wild encounter opening animation
- Map background light changed with the real world (Morning, evening and night)
- New battle fight menu and cursor
- Other improvements

---
## [rainersigwald/msbuild](https://github.com/rainersigwald/msbuild)@[a572dc6b79...](https://github.com/rainersigwald/msbuild/commit/a572dc6b796aec7d028e53aa24a82a059e47edfa)
#### Thursday 2022-06-02 22:03:46 by Forgind

Fix low priority issues (#7413)

Thanks @svetkereMS for bringing this up, driving, and testing.

This fixes two interconnected issues.
First, if a process starts at normal priority then changes to low priority, it stays at normal priority. That's good for Visual Studio, which should stay at normal priority, but we relied on passing priority from a parent process to children, which is no longer valid. This ensures that we set the priority of a process early enough that we get the desired priority in worker nodes as well.

Second, if we were already connected to normal priority worker nodes, we could keep using them. This "shuts down" (disconnects—they may keep running if nodeReuse is true) worker nodes when the priority changes between build submissions.

One non-issue (therefore not fixed) is connecting to task hosts that are low priority. Tasks host nodes currently do not store their priority or node reuse. Node reuse makes sense because it's automatically off always for task hosts, at least currently. Not storing low priority sounds problematic, but it's actually fine because we make a task host—the right priority for this build, since we just made it—and connect to it. If we make a new build with different priority, we disconnect from all nodes, including task hosts. Since nodeReuse is always false, the task host dies, and we cannot reconnect to it even though if it didn't immediately die, we could, erroneously.

On the other hand, we went a little further and didn't even specify that task hosts should take the priority assigned to them as a command line argument. That has been changed.

svetkereMS had a chance to test some of this. He raised a couple potential issues:

conhost.exe launches as normal priority. Maybe some custom task dlls or other (Mef?) extensions will do something between MSBuild start time and when its priority is adjusted.
Some vulnerability if MSBuild init code improperly accounts for timing
For (1), how is conhost.exe related to MSBuild? It sounds like a command prompt thing. I don't know what Mef is.
For (2), what vulnerability? Too many processes starting and connecting to task hosts with different priorities simultaneously? I could imagine that being a problem but don't think it's worth worrying about unless someone complains.

He also mentioned a potential optimization if the main node stays at normal priority. Rather than making a new set of nodes, the main node could change the priority of all its nodes to the desired priority. Then it can skip the handshake, and if it's still at normal priority, it may be able to both raise and lower the priority of its children. Since there would never be more than 2x the "right" number of nodes anyway, and I don't think people will be switching rapidly back and forth, I think maybe we should file that as an issue in the backlog and get to it if we have time but not worry about it right now.

Edit:
I changed "shuts down...worker nodes when the priority changes" to just changing their priority. This does not work on linux or mac. However, Visual Studio does not run on linux or mac, and VS is the only currently known customer that runs in normal priority but may change between using worker nodes at normal priority or low priority. This approach is substantially more efficient than starting new nodes for every switch, disconnecting and reconnecting, or even maintaining two separate pools for different builds.

---
## [00mn00/FRLG-Plus_Custom](https://github.com/00mn00/FRLG-Plus_Custom)@[57d9354aed...](https://github.com/00mn00/FRLG-Plus_Custom/commit/57d9354aedb94f7654cc4a86173e7872a01d5cc3)
#### Thursday 2022-06-02 23:22:01 by 00mn00

Key System Setting Changes

Introduced a LEVEL CAP system based on the code from Infused Emerald by AsparagusEduardo. The options are STRICT, HARSH, and RELAXED. If the CAP is reached, the EXP. gain is stopped. This includes RARE CANDY use, and POKéMON DAY-CARE CENTER growth.

Introduced a NO ITEM HEALS system to disable healing item use from the field, from battle, and from both as an alternative to disabling the POKéCENTER. Items in the MEDICINE POCKET no longer have the “USE” text choice when selected. The POKé FLUTE is disabled in battle, but still functions for waking up SNORLAX. The BERRY POUCH no longer has the “USE” or “GIVE” text choice, however EV changing BERRIES still function as usual.

Added another EXP. MODIFIER option, as I have a busy life and a 4x option suits me better at times. 0x, 1/2x, 1x, and 2x still remain.

A “SHINY CLAUSE ON” and “SHINY CLAUSE OFF” option is now in NUZLOCKE MODE. This was a real pain in the ass to deal with. If switched on, and a shiny POKéMON is the first encounter on a route, the following non-shiny POKéMON will still be classed as the “first” encounter (with the “1” sprite to reflect this). The subsequent non-shiny encounters will be fainted as usual. If a shiny POKéMON is encountered after the first non-shiny encounter, it will still be valid and not immediately fainted. Switching the clause off is NUZLOCKE MODE without the SHINY CLAUSE. Switching it to DISABLED is the base game without NUZLOCKE MODE.

A fair amount of help system text and formatting overhaul, to reflect the new changes and fit the new information into the pitiful amount of space allowed by the system.

I'm sure my code is absolute dogshit to look at, so sorry for harming your eyes. This is still being tested, updated, and generally messed with. Use at your own risk?

Credit to me, for a lot of this. And of course to Deokishisu, for the original KEY SYSTEM SETTINGS menu and rom hack in general.

---

