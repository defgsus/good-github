## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-08-02](docs/good-messages/2022/2022-08-02.md)


1,966,940 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,966,940 were push events containing 3,019,227 commit messages that amount to 249,970,320 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 32 messages:


## [Neonyxia/tgstation](https://github.com/Neonyxia/tgstation)@[8f0df7816b...](https://github.com/Neonyxia/tgstation/commit/8f0df7816bae3c5dedf599611cda3e6039024e14)
#### Tuesday 2022-08-02 00:02:35 by Kylerace

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
## [zx2c4/linux-rng](https://github.com/zx2c4/linux-rng)@[4bdcbe87f1...](https://github.com/zx2c4/linux-rng/commit/4bdcbe87f15308f4272a417870968a94cfab3694)
#### Tuesday 2022-08-02 00:05:28 by Jason A. Donenfeld

random: implement getrandom() in vDSO

Two statements:

  1) Userspace wants faster cryptographically secure random numbers of
     arbitrary size, big or small.

  2) Userspace is currently unable to safely roll its own RNG with the
     same security profile as getrandom().

Statement (1) has been debated for years, with arguments ranging from
"we need faster cryptographically secure card shuffling!" to "the only
things that actually need good randomness are keys, which are few and
far between" to "actually, TLS CBC nonces are frequent" and so on. I
don't intend to wade into that debate substantially, except to note that
recently glibc added arc4random(), whose goal is to return a
cryptographically secure uint32_t. So here we are.

Statement (2) is more interesting. The kernel is the nexus of all
entropic inputs that influence the RNG. It is in the best position, and
probably the only position, to decide anything at all about the current
state of the RNG and of its entropy. One of the things it uniquely knows
about is when reseeding is necessary.

For example, when a virtual machine is forked, restored, or duplicated,
it's imparative that the RNG doesn't generate the same outputs. For this
reason, there's a small protocol between hypervisors and the kernel that
indicates this has happened, alongside some ID, which the RNG uses to
immediately reseed, so as not to return the same numbers. Were userspace
to expand a getrandom() seed from time T1 for the next hour, and at some
point T2 < hour, the virtual machine forked, userspace would continue to
provide the same numbers to two (or more) different virtual machines,
resulting in potential cryptographic catastrophe. Something similar
happens on resuming from hibernation (or even suspend), with various
compromise scenarios there in mind.

There's a more general reason why userspace rolling its own RNG from a
getrandom() seed is fraught. There's a lot of attention paid to this
particular Linuxism we have of the RNG being initialized and thus
non-blocking or uninitialized and thus blocking until it is initialized.
These are our Two Big States that many hold to be the holy
differentiating factor between safe and not safe, between
cryptographically secure and garbage. The fact is, however, that the
distinction between these two states is a hand-wavy wishy-washy inexact
approximation. Outside of a few exceptional cases (e.g. a HW RNG is
available), we actually don't really ever know with any rigor at all
when the RNG is safe and ready (nor when it's compromised). We do the
best we can to "estimate" it, but entropy estimation is fundamentally
impossible in the general case. So really, we're just doing guess work,
and hoping it's good and conservative enough. Let's then assume that
there's always some potential error involved in this differentiator.

In fact, under the surface, the RNG is engineered around a different
principal, and that is trying to *use* new entropic inputs regularly and
at the right specific moments in time. For example, close to boot time,
the RNG reseeds itself more often than later. At certain events, like VM
fork, the RNG reseeds itself immediately. The various heuristics for
when the RNG will use new entropy and how often is really a core aspect
of what the RNG has some potential to do decently enough (and something
that will probably continue to improve in the future from random.c's
present set of algorithms). So in your mind, put away the metal
attachment to the Two Big States, which represent an approximation with
a potential margin of error. Instead keep in mind that the RNG's primary
operating heuristic is how often and exactly when it's going to reseed.

So, if userspace takes a seed from getrandom() at point T1, and uses it
for the next hour (or N megabytes or some other meaningless metric),
during that time, potential errors in the Two Big States approximation
are amplified. During that time potential reseeds are being lost,
forgotten, not reflected in the output stream. That's not good.

The simplest statement you could make is that userspace RNGs that expand
a getrandom() seed at some point T1 are nearly always *worse*, in some
way, than just calling getrandom() every time a random number is
desired.

For those reasons, after some discussion on libc-alpha, glibc's
arc4random() now just calls getrandom() on each invocation. That's
trivially safe, and gives us latitude to then make the safe thing faster
without becoming unsafe at our leasure. Card shuffling isn't
particularly fast, however.

How do we rectify this? By putting a safe implementation of getrandom()
in the vDSO, which has access to whatever information a
particular iteration of random.c is using to make its decisions. I use
that careful language of "particular iteration of random.c", because the
set of things that a vDSO getrandom() implementation might need for making
decisions as good as the kernel's will likely change over time. This
isn't just a matter of exporting certain *data* to userspace. We're not
going to commit to a "data API" where the various heuristics used are
exposed, locking in how the kernel works for decades to come, and then
leave it to various userspaces to roll something on top and shoot
themselves in the foot and have all sorts of complexity disasters.
Rather, vDSO getrandom() is supposed to be the *same exact algorithm*
that runs in the kernel, except it's been hoisted into userspace as
much as possible. And so vDSO getrandom() and kernel getrandom() will
always mirror each other hermetically.

API-wise, vDSO getrandom has a pair of functions:

  ssize_t getrandom(void *state, void *buffer, size_t len, unsigned int flags);
  void *getrandom_alloc([inout] size_t *num, [out] size_t *size_per_each);

In the first function, the return value and the latter 3 arguments are
the same as ordinary getrandom(), while the first argument is a pointer
to some state allocated with getrandom_alloc(). getrandom_alloc() takes
the desired number of states, and returns an array of states, the number
actually allocated, and the size in bytes of each one, enabling a libc
to use one per thread. We very intentionally do *not* leave state
allocation up to the caller. There are too many weird things that can go
wrong, and it's important that vDSO does not provide too generic of a
mechanism. It's not going to store its state in just any old memory
address. It'll do it only in ones it allocates.

Right now this means it's a mlock'd page with WIPEONFORK set. In the
future maybe there will be other interesting page flags or
anti-heartbleed measures, or other platform-specific kernel-specific
things that can be set. Again, it's important that the vDSO has a say in
how this works rather than agreeing to operate on any old address;
memory isn't neutral.

The interesting meat of the implementation is in lib/vdso/getrandom.c,
as generic C code, and it aims to mainly follow random.c's buffered fast
key erasure logic. Before the RNG is initialized, it falls back to the
syscall. Right now it uses a simple generation counter to make its
decisions on reseeding; this covers many cases, but not all, so this RFC
still has a little bit of improvement work to do. But it should give you
the general idea.

The actual place that has the most work to do is in all of the other
files. Most of the vDSO shared page infrastructure is centered around
gettimeofday, and so the main structs are all in arrays for different
timestamp types, and attached to time namespaces, and so forth. I've
done the best I could to add onto this in an unintrusive way, but you'll
notice almost immediately from glancing at the code that it still needs
some untangling work. This also only works on x86 at the moment. I could
certainly use a hand with this part.

So far in my test results, performance is pretty stellar (around 15x for
uint32_t generation), and it seems to be working. But this is very, very
young, immature code, suitable for an RFC and no more, so expect
dragons.

Cc: linux-crypto@vger.kernel.org
Cc: x86@kernel.org
Cc: Nadia Heninger <nadiah@cs.ucsd.edu>
Cc: Thomas Ristenpart <ristenpart@cornell.edu>
Cc: Theodore Ts'o <tytso@mit.edu>
Cc: Vincenzo Frascino <vincenzo.frascino@arm.com>
Cc: Adhemerval Zanella Netto <adhemerval.zanella@linaro.org>
Cc: Florian Weimer <fweimer@redhat.com>
Cc: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>

---
## [tuxedocomputers/linux](https://github.com/tuxedocomputers/linux)@[99ce4b0505...](https://github.com/tuxedocomputers/linux/commit/99ce4b05058fb42a64a58edb033e5d3a417e1ffc)
#### Tuesday 2022-08-02 00:59:05 by Peter Zijlstra

objtool: Fix symbol creation

commit ead165fa1042247b033afad7be4be9b815d04ade upstream.

Nathan reported objtool failing with the following messages:

  warning: objtool: no non-local symbols !?
  warning: objtool: gelf_update_symshndx: invalid section index

The problem is due to commit 4abff6d48dbc ("objtool: Fix code relocs
vs weak symbols") failing to consider the case where an object would
have no non-local symbols.

The problem that commit tries to address is adding a STB_LOCAL symbol
to the symbol table in light of the ELF spec's requirement that:

  In each symbol table, all symbols with STB_LOCAL binding preced the
  weak and global symbols.  As ``Sections'' above describes, a symbol
  table section's sh_info section header member holds the symbol table
  index for the first non-local symbol.

The approach taken is to find this first non-local symbol, move that
to the end and then re-use the freed spot to insert a new local symbol
and increment sh_info.

Except it never considered the case of object files without global
symbols and got a whole bunch of details wrong -- so many in fact that
it is a wonder it ever worked :/

Specifically:

 - It failed to re-hash the symbol on the new index, so a subsequent
   find_symbol_by_index() would not find it at the new location and a
   query for the old location would now return a non-deterministic
   choice between the old and new symbol.

 - It failed to appreciate that the GElf wrappers are not a valid disk
   format (it works because GElf is basically Elf64 and we only
   support x86_64 atm.)

 - It failed to fully appreciate how horrible the libelf API really is
   and got the gelf_update_symshndx() call pretty much completely
   wrong; with the direct consequence that if inserting a second
   STB_LOCAL symbol would require moving the same STB_GLOBAL symbol
   again it would completely come unstuck.

Write a new elf_update_symbol() function that wraps all the magic
required to update or create a new symbol at a given index.

Specifically, gelf_update_sym*() require an @ndx argument that is
relative to the @data argument; this means you have to manually
iterate the section data descriptor list and update @ndx.

Fixes: 4abff6d48dbc ("objtool: Fix code relocs vs weak symbols")
Reported-by: Nathan Chancellor <nathan@kernel.org>
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Signed-off-by: Borislav Petkov <bp@suse.de>
Acked-by: Josh Poimboeuf <jpoimboe@kernel.org>
Tested-by: Nathan Chancellor <nathan@kernel.org>
Cc: <stable@vger.kernel.org>
Link: https://lkml.kernel.org/r/YoPCTEYjoPqE4ZxB@hirez.programming.kicks-ass.net
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
CVE-2022-29900
CVE-2022-29901
Signed-off-by: Thadeu Lima de Souza Cascardo <cascardo@canonical.com>

---
## [Chris-plus-alphanumericgibberish/dNAO](https://github.com/Chris-plus-alphanumericgibberish/dNAO)@[63dcc92dd4...](https://github.com/Chris-plus-alphanumericgibberish/dNAO/commit/63dcc92dd4abb3fe82e54bb259cab9b8bf84f0dc)
#### Tuesday 2022-08-02 01:44:40 by chris

"Light" Chaos 1 improvements

Add doom knights instead of named "black knight" player mons.
-Starting equip pending <_<'
-Doom knights cast spells on 25% of moves
--Inflict blindness
--Vulnerability
--Flare
--Drain life (ought to be death touch, but...)
-rarely spawn in Tiamat's area.

Add special intrinsics to the crystals
-Each crystal grants knowledge of a spell
--Air: Lightning bolt
--Fire: Fireball
--Water: Cone of cold
--Earth: Digging
--Black: Hast self, extra healing, reduced spell failure
-Each crystal grants skills (+1 cur and max (capped at expert or grand master))
--Air: Axe, healing, attack, dagger
--Fire: Long sword, bow, wand, matter
--Water: Hammer, spear, broad, cleric, music
--Earth: Attack, healing, cleric, dagger
--Black: Two-handed sword

The fiends buff Chaos if not killed before confronting Chaos
-Lich
--Weaken stats replaced with death touch
--Ice storm replaced with spacewarp
--Earthquake replaced with a second casting of flare
-Kary
--Chaos gets +3 speed
--Chaos spawns with weapons (this bonus is not lost if Kary is later killed!)
--Claw attacks (3rd and 4th) become marilith hands
--Fire pillar replaced with stun
-Kraken
--Passive attacks (from Chaos's extra faces. Unholy bite, study gaze, bad luck or curse items, blinding spit.
---Kraken also gets passive tentacle attacks (up to 8x, stay out of melee!)
--Geyser replaced with ice storm
-Tiamat
-- -6 AC and +4 DR
--Most ranged weapons are blown back at attacker
---Ditto for Tiamat herself
--Poison gas replaced with plague


Set fiend HP to fixed values (they varried wildly before)
-Lich: 500
-Kary: 700
-Kraken: 900
-Tiamat: 1100
-Chaos: 2000
--Chaos's healing spell is very significant now (999), so PCs without good DPR will no longer be able to gradually whittle Chaos down, and should therefore retreat.
---Because of the spell rotation, he will cast this no more frequently than once per seven turns

Chaos and Kary don't gate in help. All fiends are marked "Lord" or "Prince" as applicable.
-Other demon lord summoning also shouldn't pull Chaos and Kary

Switched all fiends to extramission
-Kraken's derpy movement may be because he can't see you.
-Kraken and krakens get scent.

Quest monster gen checks G_GONE instead of just G_GENOD

---
## [Chubbygummibear/Yogstation-TG](https://github.com/Chubbygummibear/Yogstation-TG)@[b26f9f03e0...](https://github.com/Chubbygummibear/Yogstation-TG/commit/b26f9f03e00ded330c6bc2e0efa54aec0f8500cb)
#### Tuesday 2022-08-02 03:12:25 by Vaelophis Nyx

Makes donkpocket boxes on Box station into random spawners (#14822)

* Makes donk pockets station wide into random spawners

also adds a pile of donkpocket boxes to sec's back room and gives them a microwave

* reduced quanitity of donkpockets in sec by 4 boxes

* adds randodonks to the box mining base

* another commit I fundamentally disagree with

* reduces # of donk boxes in all kitchen variants

kill me

* microwave & gun/bomb swap

* fuck you byond map code

* fixes it. again.

---
## [zjykymt/libmodbus](https://github.com/zjykymt/libmodbus)@[6f915d4215...](https://github.com/zjykymt/libmodbus/commit/6f915d4215c06be3c719761423d9b5e8aa3cb820)
#### Tuesday 2022-08-02 03:18:04 by Stéphane Raimbault

Fix my so stupid fix for VD-1301 vulnerability

I can't believe I committed that copy/paste mistake.
Sorry Maor Vermucht and Or Peles, excepted naming your original
patch was OK.

Thank you Karl Palsson for your review.

---
## [BSCPGROUPHOLDINGSLLC/AIDED-LIKE-BERNIE](https://github.com/BSCPGROUPHOLDINGSLLC/AIDED-LIKE-BERNIE)@[c047c74193...](https://github.com/BSCPGROUPHOLDINGSLLC/AIDED-LIKE-BERNIE/commit/c047c741930c25183de3639359269990df8d25ea)
#### Tuesday 2022-08-02 04:14:13 by 1212-5858

[DONATED 100% OF ALL PROCEEDS TO: Jacob A. Riis Neighborhood Settlement COMMUNITY](https://iapps.courts.state.ny.us/nyscef/ConfirmationNotice?docId=gcMSDaFzm0ynPeXZKSHgLQ==)

[DONATED 100% OF ALL PROCEEDS TO: Jacob A. Riis Neighborhood Settlement COMMUNITY](https://iapps.courts.state.ny.us/nyscef/ConfirmationNotice?docId=gcMSDaFzm0ynPeXZKSHgLQ==)

BYLAWS / GUIDELINES

https://www.ecfr.gov/

ALL PROCEEDS DONATED TO:
Jacob A. Riis Neighborhood Settlement
10-25 41st Ave, Queens, NY 11101
(718) 784-7447


HERE ARE THE ITEMS, AND ALL THE WASTE OF TIME THESE CATS DELETE THEIR INFORMATIONWHILE I BOOST IT TO GET MORE AWARDS FOR ABOVE.

(1) USER INPUT (2) CPU PROCESSING TIME (3) CPU STORAGE TIME (4) CPU OUTPUT TIME.

https://iapps.courts.state.ny.us/nyscef/ConfirmationNotice?docId=gcMSDaFzm0ynPeXZKSHgLQ==


thank you for understanding, the banker also instructed that I place them in a spreadsheet.

https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/FEDERAL-USE-AND-DISTRIBUTION-ONLY/blob/main/README.md

https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/pull/46

ASCII (American Standard Code for Information Interchange)
    peer-to-peer network
-----------    slaskowitz@ingramllp.com <slaskowitz@ingramllp.com>,
			+13478801899

-----------    ADMINISTRATION@mskyline.com <ADMINISTRATION@mskyline.com>,
-----------    LZUCKER@mskyline.com <lzucker@mskyline.com>,
-----------    ASHLEY.HUMPHRIES@wilsonelser.com <ASHLEY.HUMPHRIES@wilsonelser.com>,
			+19084337463
peer-to-peer network
        -----------    LEGAL@mskyline.com <LEGAL@mskyline.com>,
    +19178433456.
    1320 EST: Voicemail from Mr. PAUL regan [USC 18, §241]
LCD, or liquid crystal display
Cathode Ray Tube
all up like the farmers, but at 116th/ not in disneyland.
-----------    Stephen O'Connell <sgo2107@columbia.edu>
____ FOR INSPECTION ( I WOULD CONCERNED IF I WAS UNDER INVESTIGATION OF THOSE CHARGES)
Desktop Computers
Enterprise "cloud" Workstations
Portable Laptop Computers
Tablet computers (ex: iPad)
Handheld computers (ex: Personal Digital Assistant, or PDA)
Smartphones (ex: a samsung galaxy 10e and/or Smartphone)


	(CRT) Monitors
-------- Forwarded Message --------
Subject: 	[WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER] 2c44b9: slaskowitz@ingramllp.com <slaskowitz@ingramllp.com...
Date: 	Tue, 28 Jun 2022 00:53:27 -0700
From: 	WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER <noreply@github.com>
To: 	ms60710444266@yahoo.com, financialeducation@info.consumerfinance.gov


Author: WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER <108204659+WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER@users.noreply.github.com>

Date: 2022-06-28 (Tue, 28 Jun 2022)

Changed paths: A wilsonelser-Jan 30-2022

Log Message:

-----------

slaskowitz@ingramllp.com <slaskowitz@ingramllp.com>, lzucker@mskyline.com <lzucker@mskyline.com>, Stephen O'Connell <sgo2107@columbia.edu>

BELOW, FOR CONVENIENCE.

slaskowitz@ingramllp.com <slaskowitz@ingramllp.com>, lzucker@mskyline.com <lzucker@mskyline.com>, Stephen O'Connell <sgo2107@columbia.edu>
Yep.
/S/ BO DINCER

----- Forwarded Message -----
From: "MILTON MCKENZIE" <ms60710444266@yahoo.com>
To: "B D2022" <ms60710444266@yahoo.com>, "60710 BD. 153974" <bdincer66@icloud.com>, "ashley.humphries@wilsonelser.com" <ashley.humphries@wilsonelser.com>, "kidsprivacy@viacomcbs.com" <kidsprivacy@viacomcbs.com>, "ricki.roer@wilsonelser.com" <ricki.roer@wilsonelser.com>, "BD" <bondstrt@protonmail.com>, "60710 BD. 153974" <bo.dincer@yahoo.com>, "American Bar Association" <abanews@americanbar.org>, "stephen.barrett@wilsonelser.com" <stephen.barrett@wilsonelser.com>, "william.behr@wilsonelser.com" <william.behr@wilsonelser.com>, "nibal.pena@nypd.org" <nibal.pena@nypd.org>, "christina.ortiz@nypd.org" <christina.ortiz@nypd.org>, "brittany.postiglione@nypd.org" <brittany.postiglione@nypd.org>, "wmckenzie@nycourts.gov" <wmckenzie@nycourts.gov>, "john.lamneck@nypd.org" <john.lamneck@nypd.org>

Cc: "lauren.zink@wilsonelser.com" <lauren.zink@wilsonelser.com>, "erin.zecca@wilsonelser.com" <erin.zecca@wilsonelser.com>, "ellyn.wilder@wilsonelser.com" <ellyn.wilder@wilsonelser.com>, "patricia.wik@wilsonelser.com" <patricia.wik@wilsonelser.com>, "angel.vitiello@wilsonelser.com" <angel.vitiello@wilsonelser.com>, "aviva.stein@wilsonelser.com" <aviva.stein@wilsonelser.com>, "suzanne.swanson@wilsonelser.com" <suzanne.swanson@wilsonelser.com>, "grace.song@wilsonelser.com" <grace.song@wilsonelser.com>, "urvashi.sinha@wilsonelser.com" <urvashi.sinha@wilsonelser.com>, "jennifer.provost@wilsonelser.com" <jennifer.provost@wilsonelser.com>, "kathleen.mullins@wilsonelser.com" <kathleen.mullins@wilsonelser.com>, "carole.nimaroff@wilsonelser.com" <carole.nimaroff@wilsonelser.com>, "meghan.rigney@wilsonelser.com" <meghan.rigney@wilsonelser.com>, "ricki.roer@wilsonelser.com" <ricki.roer@wilsonelser.com>, "angelique.sabia-candero@wilsonelser.com" <angelique.sabia-candero@wilsonelser.com>, "jennifer.sciales@wilsonelser.com" <jennifer.sciales@wilsonelser.com>, "elizabeth.scoditti@wilsonelser.com" <elizabeth.scoditti@wilsonelser.com>, "lois.ottombrino@wilsonelser.com" <lois.ottombrino@wilsonelser.com>, "judy.selmeci@wilsonelser.com" <judy.selmeci@wilsonelser.com>, "stacey.seltzer@wilsonelser.com" <stacey.seltzer@wilsonelser.com>, "lori.semlies@wilsonelser.com" <lori.semlies@wilsonelser.com>, "corrine.shea@wilsonelser.com" <corrine.shea@wilsonelser.com>, "andrea.shiffman@wilsonelser.com" <andrea.shiffman@wilsonelser.com>, "yana.siegel@wilsonelser.com" <yana.siegel@wilsonelser.com>, "debra.tama@wilsonelser.com" <debra.tama@wilsonelser.com>, "craig.brinker@wilsonelser.com" <craig.brinker@wilsonelser.com>, "craig.hunter@wilsonelser.com" <craig.hunter@wilsonelser.com>, "curt.schlom@wilsonelser.com" <curt.schlom@wilsonelser.com>, "daniel.flores@wilsonelser.com" <daniel.flores@wilsonelser.com>, "roger.gottilla@wilsonelser.com" <roger.gottilla@wilsonelser.com>, "sean.wagner@wilsonelser.com" <sean.wagner@wilsonelser.com>, "thomas.manisero@wilsonelser.com" <thomas.manisero@wilsonelser.com>, "brittany.postiglione@nypd.org" <brittany.postiglione@nypd.org>, "William McKenzie" <wmckenzi@nycourts.gov>

Sent: Sun, Jan 30, 2022 at 11:20 AM

Subject: *** Assigned Judge: Shlomo S. Hagler --- TY FOR GETTING THIS TO THE RIGHT PRECINCT IMMEDIATE. >> 153974/2020

ATTORNEYS ON THE RECORD FOR THE MATTER REPRESENTING THE ANNEXED ENTITIES, NOTWITHSTANDING ITS:



Members, Providers, Affiliates, Agents, Officers, Directors, Volunteers, Employees, Contractors, and Principals are being drafted in a NY SUPREME COURT as a conglomerate of: THE ZUCKERS, THE YUZERS, THE ELSERS, AND THEIR ACCESSORIES...





101 WEST 55th STREET, NEW YORK, NY, 10019

PAUL R. REGAN, ESQ. [NYS BAR # 2623577]

JOSEPH J. GIAMBOI, ESQ. [NYS BAR # 2104396]

DANIEL F. SULLIVAN, ESQ. [NYS BAR # 2383347]

WHERE DO THE ZUCKERS WORK FROM, THEY ALSO TRIED TO PEACOCK THE PROSECUTION OF THE NYPD...

150 EAST 42ND STREET, 19TH FLOOR, NEW YORK, NY, 10017

SHARI S. LASKOWITZ, ESQ. [NYS BAR # 3043015]

CORY L. WEISS, ESQ. [NYS BAR # 2327187]

"...LOCATION..."

>>> RICKI E. ROER, ESQ. [NYS BAR # 1838549] <<<
notarized by the ELSERS ///
see also docket 33. 153972-2020; Ashley v. Humphries


received a confirm from your paralegal Miss Roer...
Tel.: 281-330-8004.



WITHOUT MY CONSENT...


>>> in the matter of 153974/2020, 

>>> I BCCED the proper NYPD Precincts here as well for you, who demonstrably are capable of using their emails as well.


Inline image

PART 1.01 WRITTEN DOCUMENTATION, ENTERED IS AN INVASION OF MY PRIVACY BY DEFENDANTS IN THE CAPTION AS REFERENCED HEREUNDER.

ARTIFACT NUMBER [1] NYSCEF DOCKET 32: THE AFFIDAVIT OF MIWAKO G. MESSER.

(i) ANNEXED here is [X01], EXHIBIT 1 and in the AFFIDAVIT of MIWAKO G. MESSER aided and abetted the invasion of my privacy, demonstrably in her daily recount of my personal life and as part a part of her daily tasks and affairs attested further under penalty of perjury:

1) Observed from the corridor myself positioned and in her 22ND item of record, on the 27TH of April - myself as:

“…banging against the radiator…”

ARTIFACT NUMBER [2] ANNEXED here is [X02], EXHIBIT 2, and in, consideration of the ARTIFACT NUMBER [1], as ANNEXED IN THIS MATTER as items X01 and X02:


viii. ITEM 21

3 April 2020. Defendants attest and document to a “…chronicle…” in light of the 1/8” hole that was drilled and reported on the 28TH of March, as a basis of cause for the six hundred dollars in damages paid to replace a light fixture and paint a wall;

2 April 2020. Attest and document to myself using a hammer.

2 April 2020. Attest and document to myself building a bed.

2 April 2020. Attest and document myself hanging two chandeliers from the ceiling.



ix. ITEM 22

---
## [BSCPGROUPHOLDINGSLLC/AIDED-LIKE-BERNIE](https://github.com/BSCPGROUPHOLDINGSLLC/AIDED-LIKE-BERNIE)@[7276772501...](https://github.com/BSCPGROUPHOLDINGSLLC/AIDED-LIKE-BERNIE/commit/7276772501c1aaddff216dc88ee499065ee321e0)
#### Tuesday 2022-08-02 04:36:41 by 1212-5858

$$$(https://iapps.courts.state.ny.us/nyscef/ConfirmationNotice?docId=lpS_PLUS_/xcRixuvW1/mkKheUg==)

<https://iapps.courts.state.ny.us/nyscef/ConfirmationNotice?docId=lpS_PLUS_/xcRixuvW1/mkKheUg==>

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=0oALanv/mNr_PLUS_zXOysW5zeg==

HOPEFULLY, Miss Hochul takes care of whatever converstaions she had to and the rent was I am owed in arrears, I forgot the order number, 2395 * 13 months. You know --- I’m not wasting another moment dealing with that nonsense, for REASONABLE CAUSE, so hopefully this is sufficient for notice.

you know more than you need to at this point ,
     
<https://iapps.courts.state.ny.us/nyscef/ConfirmationNotice?docId=lpS_PLUS_/xcRixuvW1/mkKheUg==>
[ethical concerns in procedural decisions](https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=R9aac7D6DBJZ1wsiq0b38A==)


-------- Forwarded Message --------
Subject: 	Fwd: Fwd: 251295/2021 thru 251334/ [31 CERTIFICATE OF OCCUPANCY]
Date: 	Fri, 1 Jul 2022 02:30:32 -0500
From: 	B D2022 <ms60710444266@yahoo.com>
To: 	Ricki Roer <ricki.roer@wilsonelser.com>, Ashley V. Humphries <ashley.humphries@wilsonelser.com>
CC: 	DOFTaxpayerAdvocate@finance.nyc.gov, TaxEfiled@law.nyc.gov, FILER 400842/2020 <isaac@shermantax.com>, 1pctdvo@nypd.org <1pctdvo@nypd.org>, 72pctdvo@nypd.org <72pctdvo@nypd.org>, 72pctyco@nypd.org <72pctyco@nypd.org>, info@mta.gov, usdoj@public.govdelivery.com <usdoj@public.govdelivery.com>, irs@service.govdelivery.com <irs@service.govdelivery.com>, usttb@public.govdelivery.com <usttb@public.govdelivery.com>, financialeducation@info.consumerfinance.gov <financialeducation@info.consumerfinance.gov>, DHSOIG@public.govdelivery.com <DHSOIG@public.govdelivery.com>, vaoig@messages.va.gov <vaoig@messages.va.gov>, pbgc@subscriptions.pbgc.gov <pbgc@subscriptions.pbgc.gov>, USPSOIG@public.govdelivery.com <USPSOIG@public.govdelivery.com>, cdfifund@service.govdelivery.com <cdfifund@service.govdelivery.com>, subscribe@subscribe.ftc.gov <subscribe@subscribe.ftc.gov>, vatax@public.govdelivery.com <vatax@public.govdelivery.com>, tigta@service.govdelivery.com <tigta@service.govdelivery.com>, news@updates.sba.gov <news@updates.sba.gov>, news@updates.oig.dot.gov <news@updates.oig.dot.gov>, Office of the Special Inspector General for the Troubled Asset Relief Program (SIGTARP) <sigtarp@service.govdelivery.com>, HUDOIG@info.hudoig.gov <HUDOIG@info.hudoig.gov>, FrontDesk@LoungeStudiosNYC.com <FrontDesk@LoungeStudiosNYC.com>, Council of the Inspectors General on Integrity and Efficiency <CIGIE@public.govdelivery.com>, CBPMEDIARELATIONS@cbp.dhs.gov, AZCBPPublicAffairs@cbp.dhs.gov <AZCBPPublicAffairs@cbp.dhs.gov>, Constituentservices@doc.nyc.gov <Constituentservices@doc.nyc.gov>, OFCCP-Public@dol.gov, foia@eeoc.gov <foia@eeoc.gov>, NYCTLservicing@tcmfund.com <NYCTLservicing@tcmfund.com>, matthew.schimmel@cigie.gov <matthew.schimmel@cigie.gov>, laura.nichols@cigie.gov <laura.nichols@cigie.gov>, subscriptions@subscriptions.treas.gov <subscriptions@subscriptions.treas.gov>, Columbia EMOT Alert <00000121e5ec70a4-dmarc-request@lists.columbia.edu>, Hon. Nancy T. Sunshine <kcco-efile@nycourts.gov>, CUIT Communications <cuit-communications@columbia.edu>, CommissionerCrenshaw@sec.gov, CommissionerLee@sec.gov, usmint-support@usmcatalog.com <usmint-support@usmcatalog.com>, ofac_feedback@treasury.gov <ofac_feedback@treasury.gov>, NYSCEF Resource Center <efile@nycourts.gov>, ServiceECF@law.nyc.gov <ServiceECF@law.nyc.gov>, JPINN@LAW.NYC.GOV <JPINN@LAW.NYC.GOV>, nschaier@law.nyc.gov


    HERE YOU CAN EXPLAIN THIS TO THE POLICE AS WELL.

I DON;'T KNOW ANYBODY ELSER WHO WOULD CAUSE THIS MUCH DAMAGE.

you can learn a lot in a day, did you tell the investors of STFGX why the price dropped like that after I notified their Promoting Brokers?





	

Category Code: 	31      CERTIFICATE OF OCCUPANCY - NONE/ILLEGAL/CONTRARY TO CO

	CERTIFICATE OF OCCUPANCY : ILLEGAL/NONE


Assigned To: 	MANHATTAN CONSTRUCTION ENFORCEMENT 	Priority:  C    
311 Reference Number:  311-10416012    
Received: 	  05/24/2022    	  	Block:  503 	Lot:  8 	  	Community Board:  102
Owner: 	  SULLIVAN PROPERTIESLP 	 

Last Inspection:   	05/25/2022 - - BY BADGE # 1795
Disposition:   	05/25/2022 - XX - ADMINISTRATIVE CLOSURE
Comments:   	COMPLAINT STATEMENT IS NOT FOR OCCUPANCY CONTRARY TO OR ILLEGAL OCCUPANCY ,

SEE ALSO COMMENTS: 31      CERTIFICATE OF OCCUPANCY - NONE/ILLEGAL/CONTRARY TO CO


*Thursday, February 03, 2022 11:19 PM*

'lois.ottombrino@wilsonelser.com' 'ashley.humphries@wilsonelser.com' 'RICKI.ROER@WILSONELSER.COM'
*'WMCKENZIE@NYCOURTS.GOV' *   'nyscef@nycourts.gov'

> insurance <

Case: 400842/2020 *** block 2679, lot 43.





On 6/29/2022 8:45 AM, Bo Dincer wrote:
As stated,

>>Claim Value: $600,000.00
      Block 2679, Lot 43.
      840-46 Lorimer Street
      Zucker Enterprises LLC.

While dealing with their business in Brooklyn, New York.
— Kept me pre-occupied without cause to take care of their other business without my opinion or any reveal as to what they really do for a living.

For example:

>> Hon. Nancy T. Sunshine, Kings County Clerk
         and Clerk of the Supreme Court

<https://iapps.courts.state.ny.us/nyscef/ConfirmationNotice?docId=HD6/wXvlOxflJUlQyXqedQ==>

     case number:  400842/2020
     Filed:  09/23/2020
     *** KINGS COUNTY ***

Zucker Enterprises LLC
           - v. -
THE TAX COMMISSION OF THE CITY OF NEW YORK, AND
THE COMMISSIONER OF FINANCE OF THE CITY OF NEW YORK

Complaint at:  111 REAR SULLIVAN STREET 	BIN: 1077252 	   	Borough: MANHATTAN 	   	ZIP: 10012




-------- Forwarded Message --------
Subject: 	Fwd: 251295/2021 thru 251334/2021
Date: 	Wed, 29 Jun 2022 15:57:16 -0500
From: 	B D2022 <ms60710444266@yahoo.com>
To: 	TaxEfiled@law.nyc.gov, governor.hochul@exec.ny.gov, gschuller@pssb-law.com
CC: 	Yana Siegel <yana.siegel@wilsonelser.com>, WILLIAM BEHR <william.behr@wilsonelser.com>, Urvashi Sinha <urvashi.sinha@wilsonelser.com>, Thomas R. Manisero <thomas.manisero@wilsonelser.com>, Suzanne S. Swanson <suzanne.swanson@wilsonelser.com>, Stephen J. Barrett <stephen.barrett@wilsonelser.com>, Stacey L. Seltzer <stacey.seltzer@wilsonelser.com>, Sean Wagner <sean.wagner@wilsonelser.com>, Roger R. Gottilla <roger.gottilla@wilsonelser.com>, Ricki Roer <ricki.roer@wilsonelser.com>, Ricki Roer <ricki.roer@wilsonanddicker.com>, ricki.raared@wilsonsdickers.com <ricki.raared@wilsonsdickers.com>, patricia.wik@wilsonelser.com, meghan.rigney@wilsonelser.com, Lori Semlies <lori.semlies@wilsonelser.com>, Lois K. Ottombrino <lois.ottombrino@wilsonelser.com>, Lauren M. Zink <lauren.zink@wilsonelser.com>, Kathleen A. Mullins <kathleen.mullins@wilsonelser.com>, judy.selmeci@wilsonelser.com, Jennifer L. Sciales <jennifer.sciales@wilsonelser.com>, Jennifer M. Provost <jennifer.provost@wilsonelser.com>, info@wilsonelser.com, Hannah.King@WILSONELSER.COM, grace.song@wilsonelser.com, erin.zecca@wilsonelser.com, ellyn.wilder@wilsonelser.com, elizabeth.scoditti@wilsonelser.com, Debra Tama <debra.tama@wilsonelser.com>, Daniel F. Flores <daniel.flores@wilsonelser.com>, curt.schlom@wilsonelser.com, craig.hunter@wilsonelser.com, craig.brinker@wilsonelser.com, Corrine Shea <corrine.shea@wilsonelser.com>, carole.nimaroff@wilsonelser.com, aviva.stein@wilsonelser.com, Ashley V. Humphries <ashley.humphries@wilsonelser.com>, Angelique Sabia-Candero <angelique.sabia-candero@wilsonelser.com>, angel.vitiello@wilsonelser.com, Andrea Shiffman <andrea.shiffman@wilsonelser.com>, Amy Hanrahan <amy.hanrahan@wilsonelser.com>, alex.kress@wilsonelser.com, Alan Rubin <alan.rubin@wilsonelser.com>


Have been avoided and obstructed by all parties who represent the plaintiff in NYSCEF 152974/2020

- SO I WILL JUST CROSS YOU IN ANOTHER VENUE AT ANOTHER TIME IF YOU FEEL THAT IS NOT FAIR?
Hon. Milton A. Tingling, 
New York County Clerk and Clerk of the Supreme Court

---
## [BSCPGROUPHOLDINGSLLC/AIDED-LIKE-BERNIE](https://github.com/BSCPGROUPHOLDINGSLLC/AIDED-LIKE-BERNIE)@[6ffa8b244b...](https://github.com/BSCPGROUPHOLDINGSLLC/AIDED-LIKE-BERNIE/commit/6ffa8b244b4dd7f25c0f9322df75f16b17a4bcba)
#### Tuesday 2022-08-02 04:44:48 by 1212-5858

https://youtu.be/pzhD2MyeIbY?t=1940

https://youtu.be/pzhD2MyeIbY?t=1940

 xmas, interborough rapid transit, 50074 EST ++ KEYWORD RECEIPT or H
 
 https://github.com/BSCPGROUPHOLDINGSLLC/AIDED-LIKE-BERNIE/tree/main
 

https://www.fbi.gov/video-repository/newss-chasing-the-dragon-the-life-of-an-opiate-addict/file_view <https://www.fbi.gov/video-repository/newss-chasing-the-dragon-the-life-of-an-opiate-addict/file_view>

https://youtu.be/pzhD2MyeIbY?t=1940

https://youtu.be/pzhD2MyeIbY?t=1181

https://youtu.be/pzhD2MyeIbY?t=1176


THANK YOU, AND GOD BLESS.

https://github.com/BSCPGROUPHOLDINGSLLC/AIDED-LIKE-BERNIE/tree/main

https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=0oALanv/mNr_PLUS_zXOysW5zeg==

---
## [davejfish/book-shop](https://github.com/davejfish/book-shop)@[4d7ac30feb...](https://github.com/davejfish/book-shop/commit/4d7ac30feb9bc66ad9ab0899b04685007ab94071)
#### Tuesday 2022-08-02 05:41:51 by Dave Fisher

this shit is so broken and I can not even slightly figure out why it is so god damn broken

---
## [YanceyChiew/terminal](https://github.com/YanceyChiew/terminal)@[9ccd6ecd74...](https://github.com/YanceyChiew/terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Tuesday 2022-08-02 06:34:04 by Mike Griese

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
## [TheVanderlin/40K-Eipharius](https://github.com/TheVanderlin/40K-Eipharius)@[fd5321ae5b...](https://github.com/TheVanderlin/40K-Eipharius/commit/fd5321ae5b06dcdc5eba522440abbe05a6c4b297)
#### Tuesday 2022-08-02 06:36:41 by Vanderlin

orks_species

Orks now regenerate health at 0.5 instead of 0.08 since we did nerf the crap out of waaagh previously, not sure why Orks had a regen that is basically equiv to not healing at all but were given the Waaagh heal that literally shoves their eyeballs back into place...

Waagh also no longer heals brute/burn, it only recovers organ damage and blood loss. This means Orks will need to rely on their regen ability more often and their pain immunity in combat, otherwise waaagh is only useful for recovering blood loss or organ damage after a fight.

Ork stats were debuff'd PRIMARILY in the Endurance category of a whopping +18 endurance. If you were trying to figure out why the Orks seem to be unkillable, it's because of the endurance stats they were given. The instant heal waaagh probably didn't help either.

They also have pain and embed immunity, I swear if I see another Ork pickup an IFAK just to use the morphine ampoule I'm gonna lose my mind. NO MORE.

---
## [lyndsayrandall/blog_robinwieruch_content](https://github.com/lyndsayrandall/blog_robinwieruch_content)@[7e53db9c45...](https://github.com/lyndsayrandall/blog_robinwieruch_content/commit/7e53db9c455baae6fb2a30e38172d142ef92b2c8)
#### Tuesday 2022-08-02 06:48:07 by Peter Hauke

Improve and Correct the English language

The & should not really be used as a shortcut for 'and' -- a lot of people do this, but it is ugly and not really correct. I almost never use the & sign, unless it is part of the code.

'via' is obviously a Latin word, and generally, good written English tries to avoid the use of Latin if it is not necessary. Some English language learners will not know what 'via' means.

I would probably normally write 'from the command line', but 'on the command line' is not wrong. However, I used 'on' because you use it later.

'kinda', as well as 'gonna', 'wanna' is not correct at all. This is how many people speak, but it should really be avoided in writing. 

I added "With the 'useCustom' hook" -- I think that is correct.

I did not replace 'caveat'. Again this is Latin. I would have to change the whole phrase, so I left it as it was.

People use 'pretty' instead of 'almost', 'really', etc. But it is generally wrong. 'pretty' means that something is nice or beautiful. I avoid using it in that way.

Why write four words when one will do? I changed 'Last but not least' to 'Finally', they really mean the same.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[b26fd5cf6d...](https://github.com/mrakgr/The-Spiral-Language/commit/b26fd5cf6db4510d2b154a384cb1549826827c22)
#### Tuesday 2022-08-02 07:51:18 by Marko Grdinić

"8:10am. It is time to give this a try. Any mail? Not anything worth mentioning.

Before I go in, let me do the pitch.

///

Hello, I am Marko Grdinić. Out of the 6.5 years that I've been working on my own projects as a hobby programmer, 3 years of full time work went into creating the language called Spiral. I started work on it in 2017 specifically with the intention of using it on future AI chips. I had a lot of difficulty creating a GPU-based ML library in F#, so I wanted a language that would be easy to use, highly efficient - enough to compile GPU kernels on it, as well being capable of seamless language interop. I haven't been interested in GPUs for a while now, and I really want the chance to prove that my vision was true and that the tool is suitable for something like Tenstorrent's chips.

https://github.com/mrakgr/The-Spiral-Language

It is a functional language similar to F#, except with some extensions that greatly increase the domain of what it can do compared to regular languages. If any in this community are interested in the simulation capabilities of Tenstorrent's chips rather than just using their functionalities from PyTorch, you'll find the language very useful. For writing kernel code directly, it will be much easier to use than C++. You can check out the language on the VS Code marketplace. Recently I've done a ref counted C backend for it.

My proposal is to implement a Tenstorrent chip backend so the language can be used with Tenstorrent chips. My request is that I either be given access to the cloud and free credits for it, or that you mail me one of the Tenstorrent cards to my address in Croatia for free. Once I have that I'll implement the backend, and do some programs as demos to show how it can be used.

How does that sound to all of you here?

///

This is good. Now where is the Discord link?

https://docs.tenstorrent.com/tenstorrent/learn-more/support

8:40am. It is asking me for my mobile now. Good thing I got that dealt with and actually have one now. It would have been a pain to have to go through dad's just to get the registration code. I had to do that several times in the past.

8:45am. Ok, I am in. Let me post the above. I might just get banned for self promoting, but so be it.

8:50am. The channel is quite slow. But this way I can guarantee it will be seen and thought about by the relevant engineers at Tenstorrent.

8:55am. Well, I'll check it every hour or so. I slept well during the night today. Yesterday I was obsessed about what to do today so I did not have much to think about what to write.

I've been reflecting on my mistake.

In order for me to make money via programming, I need to get over my inhibition of doing favors to random people.

Solo dev and pro dev two different paths. Even if I wanted those 100-200k remote jobs, they are absolutely impossible for me until I've made the determination to step on the pro path. In order to do that, I'd need to either do freelancing or get a junior position for 3-6 months. I do not feel like going down that route. With the exception of satisfying my obsession towards AI chips in this thread here, I am not interested in stepping on the pro path.

9:15am. Let me close the tab. I'll check out the Discord later in the day. It is very slow, let me just leave it out of mind for now.

Doing this was the first good move that I did since last year apart from doing the C backend. The companies are too difficult approach. I wish I had thought of looking whether they had a Discord server earlier. But hasn't been more than 7 months since they opened it, and people only started joining 5 months ago. So I did not waste too much time.

Right now, Tenstorrent is my best bet for making Spiral useful on these devices. Other companies do not have the vision to see the benefits of serving the little people. While big customers will make them the big money, it is the individual programmers who will write the libraries that will make their devices really valuable to use. So it is good to spread cheap version of their AI chip so that people with small budgets can play with them.

Companies like Graphcore and Groq will have a strategic problem years down the road when Tenstorrent will have OS libraries made for it by the community while they are stuck paying programmers to do the same. This is what I meant by Tenstorrent having the strongest vision compared to Graphcore and Groq in the `A Question for the Machine` pdf. Incidentally, this is also why you wouldn't want to be in inference-only business. The more general purpose the device is, the better the results will be in the long run for the company.

To be honest, I expected more from the 20s. There are many startups in the field, but only a few are interesting. I thought I might be able to have multiple sponsors for Spiral easily once the wave hits, but I'll be lucky if I manage even 1 at this rate.

9:40am. Let me step away from the screen. I've spend quite a lot of time in the last few days in bed, and it seems today won't be an exception.

I'll assume that my offer won't get accepted and start focusing my will to step on the pro novelist path.

2014 when I wrote the first Simulacrum arcs was special. I didn't really care about my audience too much, I just wanted to write the story as a way of declaring victory. To say I understand what the Singularity is about. But this time, at least I will make sure to post it on a site like Royal Road where most people can see it. I'll open a Patreon with advance chapters. An important part of my writing journey is to really gauge interest in this kind of story.

This kind of story is the only thing I want to write. I woudn't be able to write anything else actually. Maybe that has a parallel with my programming.

You'd think that a pro writter would be able to write any kind of story, but I want only one kind. So maybe I am not suitable to be a pro writter either.

But it is fine if I am no good as a pro. My programming is good and my writing will be good. What else can I ask for?"

---
## [Kneba/kernel_asus_sdm660](https://github.com/Kneba/kernel_asus_sdm660)@[b627a233c4...](https://github.com/Kneba/kernel_asus_sdm660/commit/b627a233c454cd49e1b2233e1918b9a58efb2117)
#### Tuesday 2022-08-02 08:17:27 by Dan Pasanen

power: don't ever reboot to verity red

* We get it, shit's broken. We're flashing custom stuff, shit's bound
  to break. Don't pop this annoying screen up, we're not even using
  verity anyway.

Change-Id: Icd77b70ec1df9108a4ba9e7fd8cb9623b35b78db
Signed-off-by: Kneba <abenkenary3@gmail.com>

---
## [JihadZoabi/Aleph](https://github.com/JihadZoabi/Aleph)@[fae1fb1d2e...](https://github.com/JihadZoabi/Aleph/commit/fae1fb1d2eab7fcbde555f4577c7ab2489620a4a)
#### Tuesday 2022-08-02 09:13:05 by Eyal Z

The great Charlemagne, my father,
liberated me from the Saracens,
and from heaven he gave me life
of Meritxell, the great Mother.

I was born a princess and heiress
between two nations, neutral;
I am the only remaining daughter
of the Charlemagne empire.

Faithful and free for eleven centuries,
Faithful and free I want to be.
May the laws be my tutors
𝄆 and my Princes defenders! 𝄇

---
## [pri0818/dragonsoul_kernel_realme_sm7125](https://github.com/pri0818/dragonsoul_kernel_realme_sm7125)@[896373745d...](https://github.com/pri0818/dragonsoul_kernel_realme_sm7125/commit/896373745ddd07c88e5e9e06bc29de7e8e015ed3)
#### Tuesday 2022-08-02 11:18:41 by Peter Zijlstra

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
Signed-off-by: pri0818 <priyanshusinghal0818@gmail.com>

---
## [wikimedia/puppet](https://github.com/wikimedia/puppet)@[f67b662212...](https://github.com/wikimedia/puppet/commit/f67b6622126dfcd57a98b505443acf737157cf13)
#### Tuesday 2022-08-02 12:19:54 by jbond

P:adduser: apply adduser before any packages are installed

We are still suffering race conditions where software can be installed
before we have correctly configured the system with the right apt
sources and the correct adduser config, As such create a dependency

This performs the desired action however we also need to be aware that
we don't also trigger puppetdb slowness[1] again.  I think this should be
fine as its a one to many relationship as opposed to a many to many
relationship (which is what we had in the previous issue) however we
should monitor puppetdb if/after this CR is merged

Its worth noting i did try this CR using stages (see previous PS's)
but that got me into some dependency cycle hell but happy to consider
that over this.  I think both options have there down sides, however i
feel we need something in place to ensure we get a more reproducible
build

Is also worth mentioning i have tested this change with beaker and after
its applied we still achieve a clean build from scratch.

[1]https://phabricator.wikimedia.org/T263578#7322135

Hosts: sretest1002.eqiad.wmnet
Bug: T235067
Bug: T263578
Change-Id: I23be80efc59cf08d6b5243f445397345374b51b7

---
## [Marrone321/coyote-bayou](https://github.com/Marrone321/coyote-bayou)@[f83ef520c6...](https://github.com/Marrone321/coyote-bayou/commit/f83ef520c6e2e1df4b172101c86e0eb950ebbfc7)
#### Tuesday 2022-08-02 13:50:12 by Marrone

Redwater/Nash Loadout Updates + Minor Tweaks

MINOR TWEAKS

/obj/item/clothing/suit/armor/light/leather/rig
- Added 4 small pockets
- Fixed the description

/obj/item/clothing/suit/armor/medium/duster
- The bullet armor wasnt good, so I changed it to be better for PVP combat.

/obj/item/clothing/shoes/galoshes

Removed slowdown

/obj/item/clothing/head/f13/flatranger
- Changed name and description, one of many NCR items that need to be reworked

OASIS LOADOUT CHANGES

MAYOR

no longer has shit guns that make no sense between loadouts and other jobs. It is a command position, and as such they have access to higher tier side arm weapons.

Frontier Leader = from Snub to Peacekeeper
First Citizen = From AEP7 to Auto Beretta
High Roller = From Type 17 (???????????????) to MK23
Mayor for Life keeps their custom M1911, its a really good gun

SECRETARY

- Removed trait selection book. Sorry, it just doesnt make sense and need the handspace for loadout icon and suitcase. Good news is now Secretaries have access to loadout choices.

SHERIFF

The Law Man
- Changed uniform to formal police uniform
- Removed peacekeeper, replaced with a holstered 45 APC revolver
- Gave military plated boots
- Gave scope

The Chief
- Gave them the Chief under instead of police formal
- They now have a 45 APC revolver holstered with ammo
- They now have combat boots with actual armor values, why they gave jackboots previously idk
- AEP9 has been replaced with a city killer shotgun.

- Unused loadout commented out

https://i.imgur.com/HDMg6WG.png

DEPUTY

- I didnt really wanna touch this too much beause I will ultimately nerf it. I'm looking at you Nash SWAT loadout, mk12 and a fully automatic assault rifle. But yeah I'll have to get to this another time.

- Removed the extra bulletproof vest, they dont need 2

PROSPECTOR AND FARMER

- Commented out entirely and integrated with better loadouts into the Citizen role.

TOWN DOCTOR

Town Doctors now have actual loadouts that are robust and bring value to the hospital. Check them out in this pic below:

https://i.imgur.com/7Ie0VR3.png

They have been given more ways to defend themselves, but limited ammo so they dont uhh you know become combat town doctor.

CITIZENS

All loadouts have been updated and given a LOT more value. Unfortunately I do not have an updated picture to show everything cohesively, you'll have to see through code what I did.

They have been entirely reworked so that they have balance and provide value to the town and players experience no matter your playstyle.

- I also added a bunch of randomizers for what they start out with in terms of uniform and hat.

BANKER

- They had unbalanced weapons between loadouts and lacked flavor, so I didnt want to do too much. I upgraded the guns and added a flavor item to each.

Classy = 45 revolver holster and a golden lighter
Loanshark = Golden violin, they get to keep their Uzi
Investor = Gold ignot and lever action shotgun

LOADOUT CHANGES FOR REDWATER

- Outlaws have been removed from Redwater not on the map but in the join selection screen (I dont want any map merge errors, it can be done on another PR)

- Outlaws description changed from
"You are an undesirable figure of some kind- the choice of why is up to you. You've decided to become a part of the town of Redwater for one reason or another, or at least feel you can semi-safely call it home. Be you a member of the Redwater Gangs that run the slave trade through the town or a weary exile looking for a way back home you've shacked up in the shanties, and your morals are your own.  Beware, life is cheap in Redwater."

to

"You are an Outlaw - the choice of why is up to you. You are responsible for making the wasteland unsafe and today is another day to antagonize it. You may be varied in your approaches, but you must have motives that are realistic for your job."

- Changed their radio to a normal one, not a redwater one for now

- Made it so 50% chance to get a neck item like a cape or poncho

- Updated random helmets you can get so that there is a higher variaton

- Updated all Outlaw loadouts names so they are more consistent and not so Redwater based

- Added pocketprotector to Quack Doctor loadout

- Changed NCR deserter to Outlaw Ranger and changed their clothes/armor

- Gave vault renegade a pipboy

- Changed Sulphur Tribe Outcast to 'Tribal Outcast' and gave them a Tribal Traditions skillgranter book

REDWATER WATCHERS

New-ish job that replaces the CURRENT Redwater Residents mean to be the people who maintain the town, whether that means guarding it, making sure slaves are productive, keeping up with the hospital, etc

- Fixed desc to make it fit
- Gave them randomizing uniform/suit/shoes/neck/hats that are redwater flavored

- Shrunk down the loadout names to keep them simple

- Fixed up some loadout stuff for Maintainer, gave them a lever action shotgun bumped their titanium up to 15 and gave them actual blackpowder instead of a scrawny bottle.

REDWATER RESIDENT

NEWWWWW JOB

	description = "You are a Redwater Resident - the choice of why is up to you. You are a squatter who has taken it upon themselves to call Redwater home and be a part of their ecosystem without responsibility. You are not a slave as you have built a good reputation for yourself, however you are not immune from consequences."

		/datum/outfit/loadout/tribal_drifter,
		/datum/outfit/loadout/fish_wrangler,
		/datum/outfit/loadout/tapster,
		/datum/outfit/loadout/hospitalier,
		/datum/outfit/loadout/shepherd,
		/datum/outfit/loadout/fieldhand,
		/datum/outfit/loadout/mole,
		/datum/outfit/loadout/seductress,
		/datum/outfit/loadout/pilferer,
		/datum/outfit/loadout/trafficker

Had a lot of fun putting this together, this job gets a full suite of attention which should encourage players to give it a spin, despite it being at a lower power level than Nash citizen. The chance for better helmet armor is present, pretty much if you wanted to be a squatter over in Redwater, take a break from the other redwater roles and have a low stress round, want to help do the farm without being a slave, etc, this job has a lot of options for players to explore.

Unfortunately do not have an updated picture of the loadouts, you'll have to look in the code.

REDWATER SLAVE

- Very subtle, 10 percent probability to get a hairband or servant hat. Seemed like the right thing to do.

- Fixed coding typo

JOBS.DM

Commented out farmer and prospector, moved Outlaw out of Redwater slot, and added Redwater Watchers

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[fe98f70153...](https://github.com/mrakgr/The-Spiral-Language/commit/fe98f701539de28dab603f60de7d245608ec4dd9)
#### Tuesday 2022-08-02 14:04:44 by Marko Grdinić

"2:40pm. I am back. I actually forgot to have breakfast while I was in bed so I am having it now. Let me finish it and then I will note my thoughts.

2:45pm. Let me read Youjo Senki and Sengoku Komachi. This is what my morning would usually be like, but it is the middle of the day.

Anyway it is all or nothing here. If I log into the channel now and see my post has been removed, not much I can do about that. I'll spend the next few years writing. If they are asking questions about the language, I am gold. I'll be able to proceed on my path as a programmer.

I can't really commit to writing until I resolve this issue pressing down on me. Let me do my reading and then I will take a look.

3:15pm. Whatever, let me check the channel. At this rate I'll just get nervous. I wasn't nervous before, but once you get the urge and suppress it, it turns to nervousness. There is no need to make a big deal out of this. Let's see what cards will I get dealt.

Nothing yet. The post is still there, but no replies have come to it. It seems the place is really slower than I thought. Nobody looked at my post yet.

Anyway...this is pretty anti-climactic. I'll let that bait hang there. I've time to think about what my moves should be at Tenstorrent and my future proposals for it, so there is no need to dwell upon it too much.

Actually, some ideas have come to me even now. I thinking what I could say to the CEO as potential business opportunities. Pretty much everything that involves optimization is a target. I'd suggest to him that once the hardware + software foundation is there, that he hire software people to explore those possibilities and make products that can be sold. There is no need to rely purely on hardware.

They are aiming to revolutionize computing, so there is no need to focus too much on the narrow game of deep learning.

3:30pm. Remember how those two posts hung on Reddit for months with no replies until I got rid of them recently?

I think their Discord channel is a much better place seek attention that that out of the way Reddit channel that was started by somebody unrelated to the company, so it is unlikely that I will go without a reply for too long. But for whatever reason, I can't wait forever here. Am I going to lie in bed all day waiting for the fish to come? No. I am going to have to start writing.

3:35pm. Yeah, this is perfect. In fact, they did open the channel last year in September, I got the months wrong by about 4. So yes, because I was not paying attention I lost a big opportunity to showcase Spiral much earlier. But I can correct it like this. It is important to give it a try. Maybe they'll go for it, and if that is the case it would have been a tragedy to miss the chance.

3:50pm. Let me chill a bit, maybe take a bath and I will close it early for the day. I am going to start focusing on the writing grove. Write the pages and cultivate readership. I need to put this piece of bait out of mind. If I do not get a reply by tomorrow, it is going to be questionable when it is going to arive if at all. I am only assuming that those people are paying attention to their Discord, but it is pretty bereft of activity. Most of the messages are hellos from when the people first joined.

They are US based so a day or two should be enough for them to see it and think about it. If I do not get an answer by tomorrow, the chances will be a lot higher that it will get neglected. If two days pass, I can assume the interest is cool. In that case I'll go to the Discord channel and just leave my email there instead of checking it daily. Or maybe I will just tell them to open an issue on the Spiral repo. Instead of actually leaving the email I'll just note that it is on my Github profile.

4pm. Now...it is chilling time. I need to finish sorting out my emotions and focus determinately on writing. I've gone through the Tenstorrent scenarios in my head, so I need to leave that behind. I can't depend on anything. I just have to do what I want.

4:05pm. Let me close here. Tomorrow I am going to get some writing done. Until I have access to the Tenstorrent chips I'll pretend it does not exist."

---
## [eIfo1/php-roblox-clone](https://github.com/eIfo1/php-roblox-clone)@[7e9fb1b2c8...](https://github.com/eIfo1/php-roblox-clone/commit/7e9fb1b2c82481a209f941901752f7984e4b7f97)
#### Tuesday 2022-08-02 14:14:58 by Hank Hill

Fixed absolute garbage online check function

This shit was so fucking retarded It went from like 15 lines to 4 lines. It's a display of how shitty my php skills were. To add flame to this fire, I had covid-19 when I wrote this shit. LOL

---
## [Kneba/kernel_asus_sdm660](https://github.com/Kneba/kernel_asus_sdm660)@[facefc5bb4...](https://github.com/Kneba/kernel_asus_sdm660/commit/facefc5bb45dc44a0fafab9aa78b0062a4189019)
#### Tuesday 2022-08-02 15:26:55 by Dave Chiluk

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
Signed-off-by: Kneba <abenkenary3@gmail.com>

---
## [lucaskroni/Frontend](https://github.com/lucaskroni/Frontend)@[ad1fb08df9...](https://github.com/lucaskroni/Frontend/commit/ad1fb08df9a2ad26e375bab6e02b9fe729580d51)
#### Tuesday 2022-08-02 17:28:47 by lkronlac

Yooo today you actually did a lot that was really good not having your phone with you so eh yeah thing is that you did the following:

- Solved Convert or actually XML-Problem
- Solved Saving Problem (There might be flaws though please test)

Yoo but man you got this on god no finishing till your done and also no going to bed till your done also write the fine lady rahel and brush your beepin teeth oooonn god and on jesus and the other brothers there

Yoo though have a nice day and you nearly down so you can finish this but the end dont slow down more like the other way around yeah

Have a nice day you a beast you is one

---
## [jlambert360/HomieBuild](https://github.com/jlambert360/HomieBuild)@[3f61caadbd...](https://github.com/jlambert360/HomieBuild/commit/3f61caadbd4c6872c649d0065bb9d3b831b74c53)
#### Tuesday 2022-08-02 19:06:51 by ItsCamusBitch

Because i need to make an SD and im lazy and fuck you Dom im doing my due diligence

---
## [QuickWrite/MiniMinigames](https://github.com/QuickWrite/MiniMinigames)@[8641e88259...](https://github.com/QuickWrite/MiniMinigames/commit/8641e88259a3044f1a5d31f414436b1cf23cc883)
#### Tuesday 2022-08-02 19:10:53 by Hasenzahn1

QolI 11, 12, 13

QolI 11:
convert all text messages to config

QolI 12:
Sort Ships

QolI 13:
Set Player Gamemode to Adventure and allow him to fly

- I hate my life............

---
## [jack1142/Red-DiscordBot](https://github.com/jack1142/Red-DiscordBot)@[49c1074a5c...](https://github.com/jack1142/Red-DiscordBot/commit/49c1074a5c46aa994bdf998325a983979fd513a4)
#### Tuesday 2022-08-02 19:40:17 by Toby Harradine

Refactor CogManager and extension loading

This kicked off with me realising our use of `Loader.load_module()`
as a hacky way to import modules from random locations is deprecated.
Looking closer, I realised there were a couple of smelly things here
which could be cleaned up. Here's what's changed:
- Paths in CogManager are now inserted into `redbot.cogs.__path__`.
  This means to import any cog, including an external cog, the import
  path would be `redbot.cogs.cog_to_import`. It makes the rest of the
  logic really straightforward. The only side effect is,
  to differentiate core cogs from external cogs, we now need to look at
  a module's `__file__` rather than its `__module__` or `__package__`.
- Importing cog modules is now done with `importlib.import_module`.
  This is a high-level function which allows us to delegate all of the
  nitty gritty import logic to Python itself, and it should be much
  more reliable. We're also no longer dealing with `ModuleSpec`
  objects, we just go straight from cog name to module.
- We're now using `importlib.reload` to reload modules like a good
  boy. This is done from the bottom-up, twice, to make sure all
  internal imports in the package are updated.
- Packages are no longer deleted from `sys.modules` in
  `Red.unload_extension()`. This was really smelly and, in my opinion,
  unnecessary. It would have resulted in a miniscule memory saving
  at best, although I'm pretty sure even after doing this the module
  would still remain in memory, as Python keeps a reference to imported
  modules in C code as well.
- `Red.load_extension` can take either a module, or a straight name.
  This means loading a package is as simple as
  `Red.load_extension(package_name)`, no more needing to know what
  method of `CogManager` to use.
- Some internal documentation was added in a module docstring of
  `redbot.core.cog_manager`.

Co-authored-by: Jakub Kuczys <6032823+jack1142@users.noreply.github.com>

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[f74fe936ba...](https://github.com/cockroachdb/cockroach/commit/f74fe936baf053e26d8974f343fd3adaccc89bf5)
#### Tuesday 2022-08-02 20:41:10 by craig[bot]

Merge #83120 #84617 #84781 #84867 #85326 #85466 #85483

83120: server: include system and meta ranges in hot ranges report  r=koorosh a=koorosh

 `status.HotRangesV2` endpoint iterates over ranges that have the highest
 QPS, and it might include meta- or system ranges that don't have
 table descriptors. Before, it didn't include such ranges that 
 didn't provide users full information on what ranges are hot even
 if it's a system range.

 The current patch includes system and meta ranges in the Hot Ranges list
 with limited information (that doesn't include table-specific data).

Release note: None

Resolves #83117

84617: apiv2: accept cookie auth when header is non-empty r=knz,kpatron-cockroachlabs,xinhaoz a=dhartunian

In order to make use of HTTP endpoints under `/api/v2` in the DB Console
it is necessary to support cookie-based authentication for ergonomic
Javascript use.

Previously, header-based auth was not possible to use in the DB Console
because the login endpoint we use returns the session in a Cookie.
Moving this cookie into a header would require us to read into a
less-secure storage method (local storage, redux, etc.) instead of
keeping it secure in the browser's cookie storage.

We implement a suggestion to rely on Cookie auth by requiring the
presence of the auth header with a magic value of `"cookie"` that tells the
server to look for the session in the session cookie. This forces the caller
to modify the request via JS, which protects us from CSRF since
cross-origin requests can only be "simple". See the issue for further
discussion.

Resolves https://github.com/cockroachdb/cockroach/issues/84311

Release note (security update): The HTTP endpoints under the `/api/v2` prefix
will now accept cookie-based authentication similar to other HTTP endpoints
used by the DB Console. The encoded session *must* be in a cookie named
`"session"`, and the `"X-Cockroach-API-Session"` header is required to be set
to `"cookie"` for the session to be read from the cookie header. A cookie
provided without the custom header present will be ignored.

84781: sql: implement locality-aware DistSQL planning in multi-tenant setup r=yuzefovich a=yuzefovich

**sql: clean up PartitionSpans a bit**

This commit cleans up `PartitionSpans` implementations a bit:
- it pulls out some of the code shared between `partitionSpansSystem`
and `partitionSpansTenant` into `PartitionSpans` to avoid the
duplication
- it refactors the way we handle spans with no end keys (such spans are
converted into GetRequests later on). This required a minor fix to the
fake span resolver used in `fakedist` config
- it converts a panic about "no spans" into an assertion error.

Release note: None

**sql: move some functions around**

This commit moves a few functions around in order to get better grouping
of related functions. This is a pure mechanical change.

Release note: None

**sql: implement locality-aware DistSQL planning in multi-tenant setup**

This commit implements the region-aware DistSQL physical planning in
the multi-tenant setup. Previously, we would use a round-robin strategy
of assigning single-range spans to all available SQL instances and now
we'll make a much better decision.

The algorithm is as follows:
1. find all available SQL pods and determine their locality (via the
`sqlinstance.Provider`)
2. iterate over all spans and break them down into single-range spans
using the range cache that the gateway SQL instance maintains
3. for each single-range span, find the KV leaseholder and determine its
locality (via the `kvtenantccl.Connector`), then pick a random SQL
instance in the same locality
4. if there is no SQL instance in that locality, then assign the
single-range span to the gateway SQL instance.

At the moment, the only locality "tier" that we look at is the "region",
but in the future we can easily extend it (say, to also include the
"availability zone").

The choice of randomly picking the SQL instance in the same locality in
the step 3 is done so that we distribute the load evenly among multiple
pods.

The step 2 was already being performed for the system tenant, so this
commit extracts out some helpers to reuse the code as much as possible.
Additionally, it fixes an omission in the physical planning in
multi-tenancy when the query has a LIMIT (`getInstanceIDForScan`).

If in step 1 we couldn't determine the region of any available SQL pod,
then we fallback to the old naive locality-ignorant strategy of
assigning pods in round-robin fashion.

Fixes: #80678.

Release note: None (I don't think that any of these changes are
user-visible since the serverless doesn't yet support the multi-region
clusters.)

84867: ci: add scripts to build patched versions of Go runtime r=irfansharif,rail a=rickystewart

The script simply uses our existing cross toolchains and applies a patch
to the Go sources for the fine-grained CPU attribution work. We make a
custom `go` executable for all supported platforms except FreeBSD, for
which we have no cross-compilers, and M1/M2 Macs, for which we don't
have a code-signing pipeline set up yet.

Also update `build/README.MD` to capture the new process of building
dependencies.

Part of https://github.com/cockroachdb/cockroach/issues/82625.

Release note: None

85326: ui: update cluster ui to v22.2.0-prerelease-5 r=maryliag a=maryliag

Update cluster-ui version to latest published version

Release note: None

85466: sql: do not log DistSQL diagrams on the main query path r=yuzefovich a=yuzefovich

We recently merged a change to add the DistSQL diagrams to the trace
(when the tracing is enabled). This was prompted by the desire to
provide more visibility into "transparent" execution flows that are
kicked off by the main query (e.g. apply joins run a new flow on each
iteration and we didn't have any visibility into the physical plan for
that). However, this introduced non-trivial performance overhead on the
main query path when the tracing is enabled. This commit goes around the
issue by skipping the diagram generation on the main query path - this
way we still get the additional visibility on the "non-main" query paths
whereas the main query path doesn't incur any overhead. We already have
tools to get the diagrams on the main path when we need it (namely, the
stmt bundles or explicit `EXPLAIN (DISTSQL)`).

Release note: None

85483: doctor: if `docker volume create` fails, dump the error output r=rail a=rickystewart

This can fail e.g. if the Docker daemon is not running.

Release note: None

Co-authored-by: Andrii Vorobiov <and.vorobiov@gmail.com>
Co-authored-by: David Hartunian <davidh@cockroachlabs.com>
Co-authored-by: Yahor Yuzefovich <yahor@cockroachlabs.com>
Co-authored-by: Ricky Stewart <ricky@cockroachlabs.com>
Co-authored-by: Marylia Gutierrez <marylia@cockroachlabs.com>

---
## [Spookysword/rey](https://github.com/Spookysword/rey)@[05dbb98f10...](https://github.com/Spookysword/rey/commit/05dbb98f10bd5e3f254f7ff82f48a8852bb8713f)
#### Tuesday 2022-08-02 20:47:57 by Spookysword

Somebody once told me the world is gonna roll me
I ain't the sharpest tool in the shed
She was looking kind of dumb with her finger and her thumb
In the shape of an "L" on her forehead

[Pre-Chorus]
Well, the years start comin' and they don't stop comin'
Fed to the rules and I hit the ground runnin'
Didn't make sense not to live for fun
Your brain gets smart but your head gets dumb
So much to do, so much to see
So what's wrong with taking the backstreets?
You'll never know if you don't go (W-w-wacko)
You'll never shine if you don't glow
[Chorus]
Hey now, you're an all star
Get your game on, go play
Hey now, you're a rock star
Get the show on, get paid
(And all that glitters is gold)
Only shootin' stars break the mold

[Verse 2]
It's a cool place, and they say it gets colder
You're bundled up now, wait 'til you get older
But the meteor men beg to differ
Judging by the hole in the satellite picture
The ice we skate is getting pretty thin
The water's getting warm so you might as well swim
My world's on fire, how 'bout yours?
That's the way I like it and I'll never get bored

[Chorus]
Hey now, you're an all star
Get your game on, go play
Hey now, you're a rock star
Get the show on, get paid
(All that glitters is gold)
Only shootin' stars break the mold
[Interlude]
Go for the moon [?] (W-w-wacko, w-w-wacko)
Go for the moon [?] (W-w-wacko, w-w-wacko)
Go for the moon [?]
Go for the moon [?]

[Chorus]
Hey now, you're an all star
Get your game on, go play
Hey now, you're a rock star
Get the show on, get paid
(And all that glitters is gold)
Only shooting stars…

[Verse 3]
Somebody once asked, "Could I spare some change for gas?
I need to get myself away from this place"
I said, "Yep, what a concept
I could use a little fuel myself and we could all use a little change"

[Pre-Chorus]
Well, the years start comin' and they don't stop comin'
Fed to the rules and I hit the ground runnin'
Didn't make sense not to live for fun
Your brain gets smart but your head gets dumb
So much to do, so much to see
So what's wrong with taking the backstreets?
You'll never know if you don't go (Go!)
You'll never shine if you don't glow
[Chorus]
Hey now, you're an all star
Get your game on, go play
Hey now, you're a rock star
Get the show on, get paid
(And all that glitters is gold)
Only shootin' stars break the mold

[Outro]
(And all that glitters is gold)
Only shooting stars break the mold

---
## [LegendaryGuard/darkplaces](https://github.com/LegendaryGuard/darkplaces)@[91342dd0a8...](https://github.com/LegendaryGuard/darkplaces/commit/91342dd0a88d002a188418a4b0dd21957e0737b6)
#### Tuesday 2022-08-02 21:26:27 by Cloudwalk

 README: Remove Discord invite link. The Discord server is now deprecated

I'm unable to sustain the DarkPlaces engine community on Discord. They have
falsely disabled my main account and now my second account, this time
without an email explaining the reason. I have a 3rd account that is still
active. They have not responded to my emails asking for them to review
the ban of my main account and they have the gall to nuke my second
account as well.

They are flooded with support tickets likely because it is incredibly easier
to hijack a Discord account than any other account due to the simple fact
that Discord does NOT require email verification to change passwords. God
only knows what other horrors lie beneath that Eldritch abomination of
duct-taped JavaScript.

I was not banned from Discord as I was able to create the third account using
the same IP address. They ban IPs if you're banned from Discord. I can no
longer, in good conscience, give this shit, incompetent, bullshit company
a single neuron of mindshare going forward. Other arrangements for a community
hangout are to be determined but are not available at this time. The IRC,
obviously, remains available.

Until they get their shit together (if they do), FUCK Discord and FUCK
everything they stand for.

Signed-off-by: Cloudwalk <cloudwalk@icculus.org>

---
## [chromium/chromium](https://github.com/chromium/chromium)@[61672858ee...](https://github.com/chromium/chromium/commit/61672858eefbc277b4a70c6b965df53f03abca26)
#### Tuesday 2022-08-02 21:42:57 by Taylor Bergquist

Fix pinned tabs stuck at the wrong index when dragged in from the left.

Once upon a time, the math for determining insertion index when attaching to a new tabstrip was totally separate from the math for determining the index when dragging within the tabstrip. I changed that in https://chromium-review.googlesource.com/c/chromium/src/+/2575428 so attaching to a new tabstrip just inserts in a valid spot and then uses the rearranging math.

However, I apparently missed this one special case that prevented an ugly behavior of the old system, which prevented the rearranging code from fixing the mistakes made by the insertion code if fixing those mistakes would look weird - namely if it would involve swapping a tab to the right in response to the mouse moving left, or vice versa. That code was acting up in this new context and causing the linked bug.

TL;DR shit is now less complicated and we can delete the complicated bandaid code. Yay!

Bug: 1220878
Change-Id: I1e713b453be555136ff764a7a33d49c2b93da2ff
Reviewed-on: https://chromium-review.googlesource.com/c/chromium/src/+/3803381
Reviewed-by: Peter Boström <pbos@chromium.org>
Commit-Queue: Taylor Bergquist <tbergquist@chromium.org>
Cr-Commit-Position: refs/heads/main@{#1030755}

---
## [Gandalf2k15/tgstation](https://github.com/Gandalf2k15/tgstation)@[6fe0683a7b...](https://github.com/Gandalf2k15/tgstation/commit/6fe0683a7bc788a497dbce8771768e427d0dffb1)
#### Tuesday 2022-08-02 22:34:20 by Jolly

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
## [newstools/2022-vanguard-nigeria](https://github.com/newstools/2022-vanguard-nigeria)@[0c9ed44922...](https://github.com/newstools/2022-vanguard-nigeria/commit/0c9ed44922b397c1df53b7343d20ce37b02278d7)
#### Tuesday 2022-08-02 22:44:10 by Billy Einkamerer

Created Text For URL [www.vanguardngr.com/2022/08/why-i-shot-my-prstitute-girlfriend-%e2%80%95-jealous-boyfriend-confesses/]

---

