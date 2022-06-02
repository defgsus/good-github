## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-06-01](docs/good-messages/2022/2022-06-01.md)


1,376,374 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,376,374 were push events containing 2,173,857 commit messages that amount to 163,743,124 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 29 messages:


## [rebl0x3r/source-codes](https://github.com/rebl0x3r/source-codes)@[51af7d40bd...](https://github.com/rebl0x3r/source-codes/commit/51af7d40bd0e18ba3003195b5ef0c7ef005913f9)
#### Wednesday 2022-06-01 00:05:47 by mrblackx

symlinker v2 - Source Code

⛓ SYMLINKER V2 ⛓

People sell this backdoored shit for money. We cleared this fucking tool from backdoors and removed the hitstealer!

What can you do with this tool?

▪️Symlink Shells
▪️Create SMTPs*
▪️Extract Emails*
▪️Upload Mailers*
▪️Check Working Shells
▪️Find Access Hash*
▪️Find Cpanel*
▪️File Upload*
▪️Symlink & Bruteforce Cpanel*
▪️Shell Upload WP*
▪️Cpanel Checker & Uploader 
▪️Email Bounced Check
▪️SpyMailer Sender

*from shells

📧 Paste your mail here :
SymLinker V2/scripts/beast3x/youremail.txt

---
## [yuzefovich/cockroach](https://github.com/yuzefovich/cockroach)@[f782e45fd0...](https://github.com/yuzefovich/cockroach/commit/f782e45fd0da015396bc758e855535a951f2e21a)
#### Wednesday 2022-06-01 00:10:59 by Andrei Matei

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
## [crawl/crawl](https://github.com/crawl/crawl)@[1352289c90...](https://github.com/crawl/crawl/commit/1352289c90d15a53f9c472dac9343ad61d9104a7)
#### Wednesday 2022-06-01 00:38:09 by Nicholas Feinberg

New species: Meteoran

Time pressure often creates exciting gameplay and interesting
tradeoffs. Baseline Dungeon Crawl uses the Zot Clock to add a
very weak form of time pressure, but there's so much variety
between the playstyles of different species and backgrounds
that a tight clock for some would be almost impossible for
others.

So, let's try limiting that gameplay to just one species!
Meteorae have an exciting variety of bonuses - great attributes
and aptitudes across the board, passive mapping, and exploration
healing, regaining HP and MP when viewing new territory. In
exchange, they have one big downside: instead of getting 6,000
turns of Zot clock for each floor, they get 600!

The big concern here is whether this species can be made fun
without also being made wildly, boringly 'overpowered'. Lots of
levers and knobs to tweak, so let's give it a shot!

Extra notes:
- Meteorae are humanoid beings. (In the night sky, they look
  like dots because they're very far up.) Hat tip to Neil Gaiman's
  Stardust.
- This commit has a silly 'flavour' gimmick where Meteorae's LOS
  radius decreases by 2 when they have less than 50 turns left
  of Zot clock, and again when they have less than 10. Darkness
  is closing in...
- Meteorae glow in the dark. Permanent backlit status (not halo!):
  +enemy to hit, -stealth, disables invis. Suppressed in forms.
  Seems funny.

Credit to hellmonk for the initial version of this species and
pushing to make 'em happen. :)

---
## [peterbro1/RCCS_Impl](https://github.com/peterbro1/RCCS_Impl)@[819cd86344...](https://github.com/peterbro1/RCCS_Impl/commit/819cd863441de1eba0e85462962348b9b4face5a)
#### Wednesday 2022-06-01 01:16:42 by GMX

Added *reversibility*, except it's super broken. I have an early morning tomorrow so I can't work anymore tonight.

I may need to completely rethink the reversibility design. Java passes reference instead of cloning objects on assignment, which is annoying. I will look for ways around this.

Signed-off-by: GMX <pbrowning7@gmail.com>

---
## [jupyterkat/tgstation](https://github.com/jupyterkat/tgstation)@[92fda5014d...](https://github.com/jupyterkat/tgstation/commit/92fda5014dbc8ba64c19848e693c179af35da2ac)
#### Wednesday 2022-06-01 01:34:29 by san7890

Makes Hell Microwaves Not Use Power (#67413)

Hey there,

I was informed that the holodeck program Microwave Paradise would draw and suck power out of an APC. Didn't intend for that to happen, and while funny, I don't really want to arm the crew with le epic power sink with very little effort than pressing a button, or warranting this to eventually be locked to "dangerous" programs. So, let's change such that this subtype of microwaves that can not be constructed (only mapped/spawned) doesn't consume any power. I don't know why it drew off the nearest APC or how that works, but this seems to be alright.

It's not possible to deconstruct machinery spawned in at the Holodeck (which I verified while testing this PR), so do not worry about people using this to bypass the power economy for whzhzhzhz purposes.

---
## [bamablood94/qb-core](https://github.com/bamablood94/qb-core)@[9d83a952c2...](https://github.com/bamablood94/qb-core/commit/9d83a952c29fdfd3fb3ca77a45329556a32368f5)
#### Wednesday 2022-06-01 01:59:16 by uShifty

feat: Implement QBCore.Shared.VehicleHashs 

Describe Pull request
Indexs the vehicles jenkins joaat(Hash) value as the key of the table as the key so we dont have to do some shitty ass loop through the vehicles comparing joaat values. I have no clue why this secondary table was removed in the first place if I had to guess people were lazy but this should help the lazys by automatically filling the table.

Questions (please complete the following information):
Have you personally loaded this code into an updated qbcore project and checked all it's functionality? [yes/no] (Be honest) 
Yes

Does your code fit the style guidelines? [yes/no] 
Yes

Does your PR fit the contribution guidelines? [yes/no]
Yes

---
## [00mn00/FRLG-Plus_Custom](https://github.com/00mn00/FRLG-Plus_Custom)@[6a2bb2914a...](https://github.com/00mn00/FRLG-Plus_Custom/commit/6a2bb2914aeb9660fedda5c7194a1ba504ed49b6)
#### Wednesday 2022-06-01 02:49:56 by 00mn00

Key System Setting Changes (EXP, Level Cap, Battle Heals, Shiny Clause, etc)

Introduced a level cap system based on the code from Infused Emerald by AsparagusEduardo. The options are Strict(normal), Harsh(hard), and Relaxed(easy). Once the cap is reached, the gainz stop, including Rare Candy use, and Pokémon Day Care Center growth.

Added an option to disable healing during battle, as an alternative to disabling the Pokémon Center. Items in the Medicine Bag and the Berry Pouch no longer have the USE text choice when selected, this also includes the Poké Flute Key Item.

Added an additional experience gain mod option. I have a busy life at times and a 4x option suits me better. 0x, 1/2x, 1x, and 2x still remain.

A "Shiny Clause" is now in effect for Nuzlocke mode. This was a real pain in the ass to deal with. If a shiny Pokémon is the first encounter on a route, the following non-shiny Pokémon will still be classed as the "first" encounter (with the #1 sprite to reflect this), and the subsequent non-shiny encounters will be fainted as usual. If a shiny Pokémon is encountered after the first non-shiny encounter, it will still be valid and not immediately fainted. This also applies to Traded Pokémon, Gift Pokémon, and Pokémon Day Care Center eggs.

A fair amount of help system text and formatting overhaul, to reflect the new changes and fit the information into the pitiful amount of space allowed.

This is still being tested, updated, and generally messed with. Use at your own risk?

---
## [jupyterkat/Pariah-Station](https://github.com/jupyterkat/Pariah-Station)@[fb13b0e4ff...](https://github.com/jupyterkat/Pariah-Station/commit/fb13b0e4ff4a8957f2837adf7ba06ae2eb388bf8)
#### Wednesday 2022-06-01 03:33:00 by PariahBot

[MIRROR] Vim mecha changes (#541)

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
Co-authored-by: Debian <debian@packer-output-01d6f1be-59bf-4994-80ec-c61b12fe30e1>

---
## [Iatots/tgstation](https://github.com/Iatots/tgstation)@[cd294e9040...](https://github.com/Iatots/tgstation/commit/cd294e9040505e73e46384d6166015afa43217f3)
#### Wednesday 2022-06-01 03:41:14 by vincentiusvin

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
## [Iatots/tgstation](https://github.com/Iatots/tgstation)@[245ec35dae...](https://github.com/Iatots/tgstation/commit/245ec35dae59d0edc92663ccb8012b27d5e1a198)
#### Wednesday 2022-06-01 03:41:14 by LemonInTheDark

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
## [CB-Mdk/SimpleCRUD](https://github.com/CB-Mdk/SimpleCRUD)@[6bec9b6c9c...](https://github.com/CB-Mdk/SimpleCRUD/commit/6bec9b6c9c0087d5a05630539436c2659f9f8649)
#### Wednesday 2022-06-01 04:37:28 by CB-Mdk

Added a simple button, and FUCK YOU ORACLE, where is the "mysql for visual studio 2022" FFS

---
## [chagel/dwm](https://github.com/chagel/dwm)@[67d76bdc68...](https://github.com/chagel/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Wednesday 2022-06-01 04:41:23 by Chris Down

Do not allow focus to drift from fullscreen client via focusstack()

It generally doesn't make much sense to allow focusstack() to navigate
away from the selected fullscreen client, as you can't even see which
client you're selecting behind it.

I have had this up for a while on the wiki as a separate patch[0], but
it seems reasonable to avoid this behaviour in dwm mainline, since I'm
struggling to think of any reason to navigate away from a fullscreen
client other than a mistake.

0: https://dwm.suckless.org/patches/alwaysfullscreen/

---
## [looSeeCan/BethanysPieShopHRM](https://github.com/looSeeCan/BethanysPieShopHRM)@[40004fbfee...](https://github.com/looSeeCan/BethanysPieShopHRM/commit/40004fbfee293b2a31fbea6b99e0e0664cd361f2)
#### Wednesday 2022-06-01 04:56:34 by Lucycan LY

GoodNight

switched over to vs code. I want pluralsight to record my progress and vs code is the only way to do that. Visual studio does not have that option. Although Visual Studio is a much better option, atleast for C# ii is. but i need the exp points on pluralsight.... also got stuck on some shit with the debugger and the terminal.

---
## [darshan-/PurpOS](https://github.com/darshan-/PurpOS)@[1954a42236...](https://github.com/darshan-/PurpOS/commit/1954a42236c89840b8d9689a808245b7fa371016)
#### Wednesday 2022-06-01 05:20:23 by Darshan-Josiah Barber

Notes.  Plus I figured out yet another bochs setting whose default is God awful, and figuring it out makes bochs actually move toward usable.  (Why are the defaults so amazingly bad???  It defautls to 5 Hz refresh rate...  I thought it was just the slowest thing in the world, but it turns out it's capable of 30 Hz without sweating; you just have to ask it nicely to not use an utterly ridiculously slow rate...)

---
## [avar/git](https://github.com/avar/git)@[bdaf1dfae7...](https://github.com/avar/git/commit/bdaf1dfae71fdf120fc7253e713ccf0a06cc5558)
#### Wednesday 2022-06-01 07:37:11 by Tao Klerks

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
## [rohittembhurne2194/ICTSBMALL_ULB](https://github.com/rohittembhurne2194/ICTSBMALL_ULB)@[e229cd854a...](https://github.com/rohittembhurne2194/ICTSBMALL_ULB/commit/e229cd854a96e9272ff41547427035968ce18a19)
#### Wednesday 2022-06-01 07:53:58 by umeshl@appynitty.com

Chanegs done By Millionaire persone and its me Umesh aka PeaceMinded i will definitely successful in this year god blessed me thanku for giving me this beautiful life and sorry for my any mistake

---
## [ammarfaizi2/linux-fork](https://github.com/ammarfaizi2/linux-fork)@[bd7d220a61...](https://github.com/ammarfaizi2/linux-fork/commit/bd7d220a614aff4cf48e48c255e60ca057732eff)
#### Wednesday 2022-06-01 10:36:22 by Jason A. Donenfeld

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
## [lyz-code/blue-book](https://github.com/lyz-code/blue-book)@[e96ef2185f...](https://github.com/lyz-code/blue-book/commit/e96ef2185f9bffad83adaec602a56783c4114514)
#### Wednesday 2022-06-01 11:04:57 by Lyz

feat(python_snippets#Define a property of a class): Define a property of a class

If you're using Python 3.9 or above you can directly use the decorators:

```python
class G:
    @classmethod
    @property
    def __doc__(cls):
        return f'A doc for {cls.__name__!r}'
```

If you're not, the solutions are not that good.

perf(git#Change's Controversy): Master to main branch change's controversy

The change is not free of controversy, for example in the [PDM
project](https://github.com/pdm-project/pdm/pull/1064) some people are not sure
that it's needed for many reasons. Let's see each of them:

* *The reason people are implementing the change is because other people are
    doing it*: After a quick search I found that the first one to do the change
    was [the software freedom conservancy with the Git
    project](https://sfconservancy.org/news/2020/jun/23/gitbranchname/). You can
    also see [Python](https://github.com/python/cpython/issues/78786),
    [Django](https://github.com/django/django/pull/2692),
    [Redis](https://github.com/redis/redis/issues/3185),
    [Drupal](https://www.drupal.org/node/2275877),
    [CouchDB](https://issues.apache.org/jira/browse/COUCHDB-2248) and
    [Github](https://www.theserverside.com/feature/Why-GitHub-renamed-its-master-branch-to-main)'s
    statements.

   As we're not part of the deciding organisms of the collectives
    doing the changes, all we can use are their statements and discussions to
    guess what are the reasons behind their support of the change. Despite that
    some of them do use the argument that other communities do support the
    change to emphasize the need of the change, all of them mention that the
    main reason is that the term is offensive to some people.

* *I don't see an issue using the term master*: If you relate to this statement
    it can be because you're not part of the communities that suffer the
    oppression tied to the term, and that makes you blind to the issue. It's
    a lesson I learned on my own skin throughout the years. There are thousand
    of situations, gestures, double meaning words and sentences that went
    unnoticed by me until I started discussing it with the people that are
    suffering them (women, racialized people, LGTBQI+, ...). Throughout my
    experience I've seen that the more privileged you are, the blinder you
    become. You can read more on privileged blindness
    [here](https://iveybusinessjournal.com/fighting-privilege-blindness/),
    [here](https://dojustice.crcna.org/article/becoming-aware-my-privilege) or
    [here](https://www.mindful.org/the-research-on-white-privilege-blindness/)
    (I've skimmed through the articles, and are the first articles I've found,
    there are probably better references).

    I'm not saying that privileged people are not aware of the issues or that
    they can even raise them. We can do so and more we read, discuss and train
    ourselves, the better we'll detect them. All I'm saying is that a non
    privileged person will always detect more because they suffer them daily.

    I understand that for you there is no issue using the word *master*, there
    wasn't an issue for me either until I saw these projects doing the change,
    again I was blinded to the issue as I'm not suffering it. That's because
    change is not meant for us, as we're not triggered by it. The change is
    targeted to the people that do perceive that `master` is an offensive term.
    What we can do is empathize with them and follow this tiny tiny tiny
    gesture. It's the least we can do.

    Think of a term that triggers you, such as *heil hitler*, imagine that those
    words were being used to define the main branch of your code, and that
    everyday you sit in front of your computer you see them. You'll probably be
    reminded of the historic events, concepts, feelings that are tied to that
    term each time you see it, and being them quite negative it can slowly mine
    you. Therefore it's legit that you wouldn't want to be exposed to that
    negative effects.

* *I don't see who will benefit from this change*: Probably the people that
    belongs to communities that are and have been under constant oppression for
    a very long time, in this case, specially the racialized ones which have
    suffered slavery.

    Sadly you will probably won't see many the affected people speak in these
    discussions, first because there are not that many, sadly the IT world is
    dominated by middle aged, economically comfortable, white, cis, hetero,
    males. Small changes like this are meant to foster diversity in the
    community by allowing them being more comfortable. Secondly because when
    they see these debates they move on as they are so fed up on teaching
    privileged people of their privileges. They not only have to suffer the
    oppression, we also put the burden on their shoulders to teach us.

As and ending thought, if you see yourself being specially troubled by the
change, having a discomfort feeling and strong reactions. In my experience these
signs are characteristic of privileged people that feel that their privileges
are being threatened, I've felt them myself countless times. When I feel it,
+I usually do two things, fight them as strong as I can, or embrace them, analyze
them, and go to the root of them. Depending on how much energy I have I go with
the easy or the hard one. I'm not saying that it's you're case, but it could
be.

---
## [newstools/2022-new-york-post](https://github.com/newstools/2022-new-york-post)@[d17cbdd9d4...](https://github.com/newstools/2022-new-york-post/commit/d17cbdd9d481a60fc42b92ed1c4800aa40601dc7)
#### Wednesday 2022-06-01 11:24:21 by Billy Einkamerer

Created Text For URL [nypost.com/2022/05/31/heres-what-gave-away-that-my-boyfriend-was-cheating-on-me/]

---
## [shrinivaasanka/asfer-github-code](https://github.com/shrinivaasanka/asfer-github-code)@[e2dda210d6...](https://github.com/shrinivaasanka/asfer-github-code/commit/e2dda210d6c0e23746bdf513eef4901d6d1db03f)
#### Wednesday 2022-06-01 11:42:14 by Krishna iResearch - NeuronRain - K.Srinivasan

---------------------------------------------------------------------------------------------------------------------------------------------
1255. (THEORY and FEATURE) Astronomical Dataset Analytics - Planetarium Ephemeris Search - 1 June 2022 - related to 731,1206,1236 and all sections on Astronomical Dataset Mining, Archaeoastronomical Dating, Sequence Mining, String analytics, Sequence Alignment, Visual Planetarium Search, Archaeology, Reciprocal Recommender Systems based Matrimony analytics in Bipartite Social Networks, Climate and Extreme Weather Event Analytics
---------------------------------------------------------------------------------------------------------------------------------------------
1255.1 MaitreyaEncHoro_RuleSearch.py python Swiss-JPL ephemeris search maitreya8t text client wrapper has been updated for searching sky for a zodiac configuration which simulates visual timeline search for celestial bodies in planetarium software.
1255.2 Astronomical data are rife in ancient scriptures and most archaeological artefacts as religion and astronomy are often intertwined. Scientific corroboration of mythology and historicity of epics requires an exhaustive search of astronomical references in scriptures either through Planetarium software or traditional alternatives.
1255.3 Problem lies in computational cost of this exhaustive search to pinpoint historic timeline of events described in an epic which could have occurred few millenia ago and lack of ephemeris data for that period (possibly hindered by tropical-sidereal conflicts,ayanamsa conundrum among others). Exhaustive search could be optimized to some extent by exploiting orbital periodicity-conjunctions of planets and extrapolating future - e.g Eight planets were conjunct 0 degree of Aries during Kali era birth, Eight planets were conjunct in 1962 in Aquarius.
1255.4 Visual equivalent of earlier textual search script could be far more intensive and might need preprocessing but does not depend on cuspal boundaries :
	1255.4.1 Plot visual zodiac (Degrees of Planets,Meteors,Constellations) from astronomical data mentioned in a treatise
	1255.4.2 Do a matching image search of previous plot and Visual Planetarium Sky Maps dating back thousands of years - number of sky images to search and match could be in millions.
1255.5 MaitreyaEncHoro_RuleSearch.py has been so far restricted to search of class association rules (which are subsets of 360 degree zodiac), mined from past extreme weather event datasets by GSP Sequence Mining and Sequence Alignment, to predict future climate and seismic events. It has been enhanced in this commit to search a celestial configuration from text file CelestialConfiguration.txt (full 360 degree zodiac - which could be birth data of a mythological personality or event described in scriptures) in the ephemeris within a minimum-maximum range of days-months-years through maitreya8t text client.
1255.6 MaitreyaEncHoro_RuleSearch.py has been upgraded to Python 3.7 by 2to3 + autopep8 upgrade tools. Two boolean flags ClassAssociationRuleSearch and PlanetariumSearch have been introduced to separate CAR (class association rule) search and Planetarium search (read from either MinedClassAssociationRules.txt or CelestialConfiguration.txt) and invoke either substring_find() or a new function match_chart_and_rule().
1255.7 New function match_chart_and_rule() has been implemented as a container iterable alternative of string-based substring_find() to check equality of chart data dictionary from maitreya8t and dictionary computed from CelestialConfiguration.txt and return boolean -1 (Dissimilar) or 1 (Similar). Both dictionaries have 12 key-value pairs mapping zodiac divisions to planets housed therein.
1255.8 Maitreya8t and any planetarium software are limited by availability of ephemeris data which seems to be restricted to 3000 BC and older dates are not supported. Maitreya8t provides facilities for astrological matrimonial match by following commandline options:
	 --file2=<str>             	Open second file for partner chart
	 --partner-vedic           	Show Vedic partner analysis
  	 --partner-composite       	Show partner composite chart
which is culture-oriented orthodox match making complementing reciprocal recommender systems followed in bipartite (Bride-Groom) matrimonial portal software.
1255.9 An example Celestial configuration for 1 June 2022 is searched by MaitreyaEncHoro_RuleSearch.py (PlanetariumSearch=True) and match is identified as per testlogs/MaitreyaEncHoro_RuleSearch.PlanetariumSearch.log.1June2022

References:
----------
1255.10 Date of Ramayana - https://www.vifindia.org/transcriptions-paper/2012/07/03/scientific-dating-of-ancient-events-from-7000-bc-to-2000-bc - 5114 BC to 5075 BC derived by Planetarium software based on astronomical data in Ramayana - Sea level was 3 metres below present level 7000 years BCE.
1255.11 Aihole inscription of Kali era and Mahabharata war - 3101 BC - https://www.myindiamyglory.com/2018/10/27/what-aihole-inscription-of-meguti-temple-tell-about-mahabharata-war-date/
1255.12 Milankovitch cycles - https://climate.nasa.gov/news/2948/milankovitch-orbital-cycles-and-their-role-in-earths-climate/ - 100000(eccentricity),41000(oblique tilt),26000(precession) year cycles causing climate change
1255.13 Date of Mahabharata War - 3067 BC - [Prof.Srinivasa Raghavan-1891] - https://archive.org/details/dateofmahabharat00srinuoft - War time placed in Kali and not Dvapara yuga
1255.14 Vartak's dating of Mahabharata war - 5561 BC - https://archive.org/details/ArticleOnScientificDatingOfMahabharataWar_PVVartakSpeakingTree/mode/2up
1255.15 Valmiki Ramayana - Yudhha Kanda - Sarga 4 - Verse 5 - "Uttaraphalguni conjoins Hasta" - implies unusual occultation of one constellation by the other - https://www.valmikiramayan.net/utf8/yuddha/sarga4/yuddha_4_frame.htm - उत्तरा फल्गुनी हि अद्य श्वस् तु हस्तेन योक्ष्यते || ६-४-५ अभिप्रयाम सुग्रीव सर्व अनीक समावृताः |
1255.16 Valmiki Ramayana - Bala Kanda - Sarga 18 - Verses 8,9,10,11 - "Chaitra Navami,When Five planets were exalted,Moon-Jupiter were conjunct,Cancer ascending" - https://www.valmikiramayan.net/utf8/baala/sarga18/bala_18_frame.htm - ततश्च द्वादशे मासे चैत्रे नावमिके तिथौ || १-१८-८ नक्षत्रेऽदितिदैवत्ये स्वोच्चसंस्थेषु पंचसु | ग्रहेषु कर्कटे लग्ने वाक्पताविंदुना सह
1255.17 Quintuple Planetary Groupings from 3101 BC to 2735 AD - https://articles.adsabs.harvard.edu//full/1994JBAA..104..293D/0000295.000.html- Grouping on 18 February 3101 BC is axiomatically the Kali era beginning.

---
## [astropy/pyvo](https://github.com/astropy/pyvo)@[a1a831d286...](https://github.com/astropy/pyvo/commit/a1a831d28619ecb553399f819de68a2511288a23)
#### Wednesday 2022-06-01 16:37:16 by Markus Demleitner

Switching Interface, Capability and friends to new xsi:type handling.

Since this is a rather ugly hack, a few words of background:

It turns out that astropy.utils.xml completely discards all namespace
information.  That you can parse Registry/capability documents with it
in the first place is just because we only have local elements with
elementFormDefault=unqualified.  Ah well.

Given that, we can either do XML processing ourselves, properly managing
namespaces (which wouldn't be a terrible amount of work).  Or we ignore
namespaces and namespace prefixes, too.  Since I can't think of anywhere
that would be trouble in the current VO, this commit opts for the second
option.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[ff5ed3bda7...](https://github.com/treckstar/yolo-octo-hipster/commit/ff5ed3bda7a1129569e6ff20c02ab981c4b60936)
#### Wednesday 2022-06-01 17:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [umanwizard/materialize-1](https://github.com/umanwizard/materialize-1)@[3bc0574297...](https://github.com/umanwizard/materialize-1/commit/3bc057429749d105bd462595fc3512554be9832f)
#### Wednesday 2022-06-01 17:50:34 by Daniel Harrison

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
## [iwamatsu/linux-watchdog](https://github.com/iwamatsu/linux-watchdog)@[213d266ebf...](https://github.com/iwamatsu/linux-watchdog/commit/213d266ebfb1621aab79cfe63388facc520a1381)
#### Wednesday 2022-06-01 18:04:13 by Linus Torvalds

gpiolib: acpi: use correct format characters

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

---
## [CocaColaTastesGood/thewasteland](https://github.com/CocaColaTastesGood/thewasteland)@[013fb2bd4b...](https://github.com/CocaColaTastesGood/thewasteland/commit/013fb2bd4bd6ce216844c984da9dc5ffed316c61)
#### Wednesday 2022-06-01 20:47:46 by ishitbyabullet

Fallout Alien Content (#539)

* ncr veteran ranger removal

sorry, boys, but 18 yr old female veteran rangers aren't lore accurate.

* NCR no longer has farming or water

No one ever did the sharecropper farm quest in FNV anyways.

* NCR must actively pay taxes

There is a new need meter similar to thirst and hunger for this now.

---
## [InterShare/MobileApp](https://github.com/InterShare/MobileApp)@[0762512d27...](https://github.com/InterShare/MobileApp/commit/0762512d27d77fc52eb06674ca06116e1666974d)
#### Wednesday 2022-06-01 21:01:28 by Julian Baumann

Fuck you medium article. Why the hell is "—" so indistinguishable to "-"

---
## [transcom/mymove](https://github.com/transcom/mymove)@[8af1f5a031...](https://github.com/transcom/mymove/commit/8af1f5a03143dce4ab3c6aa01b8772cd2f41adb9)
#### Wednesday 2022-06-01 21:04:05 by Marty Boren

Very rough skeleton of move code search

after many moons of struggle, I've finally got something that
kinda works.
There's an endpoint for searching for moves.
and an office page with a search box that hits that endpoint
and drops the results in a table.

i was really struggling to get the react part of this to work without
setting off an infinite loop, so now that I've finally gotten there
i want to commit even though this is still full of debug cruft.

lots of exciting things left to do, such as:
- the moves that are returned by the endpoint are missing most of the
  stuff they should have.
- We also can't search for DoD ID
- interface for passing search info between things is inconsistent

---
## [Gay-Snake-Squad/Teds-Larger-Lootpools](https://github.com/Gay-Snake-Squad/Teds-Larger-Lootpools)@[054a02952f...](https://github.com/Gay-Snake-Squad/Teds-Larger-Lootpools/commit/054a02952fdba67849b630897b40b98f1e49daf8)
#### Wednesday 2022-06-01 23:13:38 by ted

push even though it can't even launch

fuck you i know it doesn't work i'll fix it later i am tired already

---
## [kanemaki/duckstation](https://github.com/kanemaki/duckstation)@[f9212363d3...](https://github.com/kanemaki/duckstation/commit/f9212363d3370efcdb97d4f7de010b5f17bd5c5e)
#### Wednesday 2022-06-01 23:14:35 by IlDucci

Spanish translation overhaul + Addition of es-ES alternative

In its current state, the Spanish translations for Duckstation are a mess of different dialects, multiple translations for the same terms, mistranslations or excessively literal translations, and typos.

It's a shame, because you could feel that the initial translations were done with care, but were muddled with future revisions.

This commit tries to solve all of these and also change the initial decision of the first translator to have an "universal" "neutral" Spanish, as time has proven it's not possible without a dedicated translator who actually wants to have one Spanish language for all Spanish-speakers across the globe.

I'm not going to be that one, so the next option would be to duplicate the Spanish translations into two: one for the Spanish-speaking American people (called "Latin American Spanish", "español de Hispanoamérica", code es-419") and one for the European Spanish speakers (called "Spanish (Spain)", "español de España", code es-ES).

This distinction is used in multiple software applications that managed to have translators for different languages, and should also funnel any future Latin American Spanish and European Spanish translators to the corresponding file.

I have tried to follow as many existing terms and constructions as possible, restoring and/or rewording any phrasal constructions that were disunified by the multiple translators.

Since I have a limited experience with Latin American Spanish, this commit should be sent as a draft for additional revisions. I'm open to stick to having a single Spanish language, but it has to be done RIGHT.

This is an overview of changes across the board:
 - Added missing translations for QT and Android builds.
 - Unified translations between those.
 - Updated the QT file with the latest string values.
 - Massive removal of Title Uppercasing inherited from English in menu strings (the rules set by the Royal Academy of the Spanish Language, or RAE, limit the areas where Title Uppercasing is considered correct in Spanish. Menu names and window header texts are not within those areas).
 - Unified the treatment of users in the Latin American version to formal "ustedeo". This treatment could be modified with additional input.
 - Removed any gendering assumptions from any string directed towards the user (Are you sure...?, changed ¿Está/s seguro...? with ¿Seguro que...?)
 - Naturalization rewrites.
 - Typo corrections.
 - Gender corrections over definitive terms.
 - Adding missing NBSPs after required mathemathical characters or units.
 - Mass replacement of double/single quotes with angled quotes (the ones approved for Spanish).
 - Quoted non-Spanish, non-proper noun English words as dictated by RAE.
 - Removal of unwanted hyphens to join words (Auto-detectar with Detección automática, post-procesamiento with posprocesamiento). In Spanish, hyphens tend to separate, rather than join.
 - Revision of the compound forms, unified depending on Latin American Spanish or European Spanish.
 - Lowercased the first word of a text between parenthesis (Spanish rules dictate that they should be considered a continuation of the phrase, and thus, they should start with lowercase unless it's a proper noun or a word that must be uppercased) and corrected the positions between periods and parentheses.
 - Unified the accentuation rules for the adverb solo/sólo and the demostrative pronouns (este/ese/aquel) by removing all accents in European Spanish (following the RAE's 2010 suggestions) or keeping/adding them for Latin American Spanish (the 2010 rule ended up being a suggestion because while Spain has mostly deprecated those accents, it appears that the Latin American countries have not). To discuss?
 - Tweaked the key shortcuts for the QT menu to minimize duplicates.
 - Terms unified (this list doesn't represent the entirety of the changes):
    - Failed to (Fallo al/Error al): Fallo al
    - Hardcore Mode (Modo Hardcore/Modo Difícil): «hardcore» mode (Foreign non-proper nouns should be quoted, RetroAchievements does not have an official Spanish translation, so the term should be kept in English)
    - Enable/Disable (habilitado/deshabilitado/activado/desactivado/activo/inactivo): habilitado/deshabilitado
    - host (host/anfitrión/sistema): sistema, TO BE DETERMINED AND UNIFIED
    - Signed (numbers; firmados): (números) con signo
    - scan (verb and noun; escanear): buscar/búsqueda
    - Clear (something, like bindings or codes; despejar, limpiar): borrar/quitar
    - requirement (of a system, requisito/requerimento): requisito
    - input (of a controller, control): entrada
    - Threaded X (hilo de X): X multihilo
    - Frame Pacing (frame pacing): duración de fotogramas
    - XX-bit (XX-bit): XX bits (proper form)
    - Widescreen (screens, widescreen hacks; pantalla ancha, pantalla panorámica): pantalla panorámica
    - Antialiasing (anti-aliasing): Antialiasing (considered a proper noun by NVidia, doesn't need that hyphen)
    - hash: «hash» (could be discussed as "sumas de verificación", like on Dolphin)
    - Focus Loss (perder el foco): ir/entrar en segundo plano
    - toggle (verb for hotkeys, activar): alternar (as the key alternates between enabling and disabling the function, while "activate" might sound like it's just the enable part)
    - Rewind (function; retrocediendo, retrocedimiento): rebobinado (to discuss on LATAM Spanish)
    - shader (shader/sombreado): sombreador
    - resume (resumir): reanudar, continuar (resumir is a false friend)
    - Check (verb; chequear/revisar/comprobar): chequear (LATAM Spanish), comprobar (European Spanish)
    - Add (something; añadir/agregar): agregar (LATAM Spanish, to discuss) or añadir (European Spanish)
    - Enter/Input (ingrese, inserte): ingresar (LATAM Spanish) or introducir (European Spanish)
    - mouse (device; mouse/ratón): mouse (LATAM Spanish), ratón (European Spanish)
    - Auto-Detect (Auto-detectar): Detección automática
    - Controller (control): mando (for European Spanish only)
    - run (a game, the emulator; correr): ejecutar, funcionar (for European Spanish only)

---

