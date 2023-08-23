## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-08-22](docs/good-messages/2023/2023-08-22.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,271,795 were push events containing 3,458,368 commit messages that amount to 273,794,843 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 71 messages:


## [kernelci/linux](https://github.com/kernelci/linux)@[4542057e18...](https://github.com/kernelci/linux/commit/4542057e18caebe5ebaee28f0438878098674504)
#### Tuesday 2023-08-22 00:01:22 by Linus Torvalds

mm: avoid 'might_sleep()' in get_mmap_lock_carefully()

This might_sleep() goes back a long time: it was originally introduced
way back when by commit 010060741ad3 ("x86: add might_sleep() to
do_page_fault()"), and made it into the generic VM code when the x86
fault path got re-organized and generalized in commit c2508ec5a58d ("mm:
introduce new 'lock_mm_and_find_vma()' page fault helper").

However, it turns out that the placement of that might_sleep() has
always been rather questionable simply because it's not only a debug
statement to warn about sleeping in contexts that shouldn't sleep (which
was the original reason for adding it), but it also implies a voluntary
scheduling point.

That, in turn, is less than desirable for two reasons:

 (a) it ends up being done after we successfully got the mmap_lock, so
     just as we got the lock we will now eagerly schedule away and
     increase lock contention

and

 (b) this is all very possibly part of the "oops, things went horribly
     wrong" path and we just haven't figured that out yet

After all, the whole _reason_ for having that get_mmap_lock_carefully()
rather than just doing the obvious mmap_read_lock() is because this code
wants to deal somewhat gracefully with potential kernel wild pointer
bugs.

So then a voluntary scheduling point here is simply not a good idea.

We could certainly turn the 'might_sleep()' into a '__might_sleep()' and
make it be just the debug check that it was originally intended to be.

But even that seems questionable in the wild kernel pointer case - which
again is part of the whole point of this code.  The problem wouldn't be
about the _sleeping_ part of the page fault, but about a bad kernel
access.  The fact that that bad kernel access might happen in a section
that you shouldn't sleep in is secondary.

So it really ends up being the case that this is simply entirely the
wrong place to do this debug check and related scheduling point at all.

So let's just remove the check entirely.  It's been around for over a
decade, it has served its purpose.

The re-schedule will happen at return to user space anyway for the
normal case, and the warning - if we even need it - might be better off
done as a special case for "page fault from kernel mode" once we've
dealt with any potential kernel oopses where the oops is the relevant
thing, not some artificial "scheduling while atomic" test.

Reported-by: Mateusz Guzik <mjguzik@gmail.com>
Link: https://lore.kernel.org/lkml/20230820104303.2083444-1-mjguzik@gmail.com/
Cc: Matthew Wilcox <willy@infradead.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[cd8a55f9d5...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/cd8a55f9d54bd82fca9605e88169c96d79558f5d)
#### Tuesday 2023-08-22 00:38:38 by Rhials

Adds a handful of Ninja Hacking MODule interactions of varying usefulness (#77707)

## About The Pull Request

Adds a few new interactions with the Ninja's ~~right click multipurpose
trolling tool~~ Hacking MOD Module. These new effects are not tied to
objectives and are geared towards expanding the ninja's access,
disabling equipment, and giving them more ways to punk the crew.

### **Useful additions**
Ninjas can now hack open **windoors** and **elevator control panels**.
Both trigger emag_act() when hacked, opening in the case of the windoor,
and disabling the access restrictions _(and also maybe the safeties)_ in
the case of the elevator controls.

**Buttons** can also be emagged by the hacking modules, which removes
their access restrictions.

Hacking a **camera** will now EMP it, disabling it for about 90 seconds.
This can especially useful when trying to complete objectives, and works
better than smashing the cameras with your sword or lugging around
tools.

**Firelocks** can be right-click opened now too, thanks to the hacking
MODule.

**Energy guns** of all variety, useless to a ninja since they can't use
ranged weapons, can now be drained and used to charge your suit. This
takes a brief do_after to complete, so pulling it off mid-combat may be
as risky as it is stylish.

### **Being a nuisance**

**Vendors** can be hacked, expending some charge to trigger the "throw"
wire, making it launch inventory at anyone who passes by.

You can now hack **simplebots**, expending some charge from your suit to
overload and detonate them. It's faster than tipping, and far more
tragic. Sentient simplebots should take care when a ninja is around.

### **Sabotage opportunities**

The **recycler** can now be hacked. This takes 30 seconds and notifies
the AI, just like the communications console hack. Completing the hack
will emag it. That's it.

Hacking the **tram control console** will trigger an extended Tram
Malfunction event, and can be repeated after the event is done. This can
only be done to the "main" tram of the map, which I forsee will be an
absolute nightmare to complete on highpop tramstation.

Neither of these, presently, contribute towards any objectives. They can
be useful for diverting attention, but I see them more as ways for an
overachieving ninja to flex or continue the chaos after their objectives
are complete.

### **OH ALSO**

Hacking open doors costs energy. This really shouldn't be an issue just
remember to recharge sometimes.

The charge drains and do_after lengths for all of these were chosen on
vibes. In all honesty I think the drainage values don't _really_ matter,
due to how easy recharging is, but I had a hard time settling on how
long some of these hack do_afters should take (even if I know they
probably won't matter either).

## Why It's Good For The Game

Being able to hack open airlocks but not windoors always irked me. I
figured that they would be openable like any other door, and that losing
their status as a "-1 dash charge gate" wouldn't be a big enough balance
change to spark arguments. The same philosophy extends to buttons and
elevator controls.

Sapping power from eguns expands on the list of sources energy can be
siphoned from. You can also use it to disarm opponents (like the badass
ninja you are), take emergency charge from a recently-gored officer's
disabler, or dunk on security by draining their entire armory.

Hacking simplebots, vendors, and by extension elevator lifts (since that
also disables the safeties!) give opportunities for minor sabotage. Not
meant to be super disruptive, just a bit silly and annoying for the
crew.

The recycler/tram hacking in particular are meant to be bonus goals,
only sought out by the ballsiest (or more likely boredest) of ninjas.

I see all of these additions as expanding upon the current abilities of
the ninja (not really making them much more powerful, just expanding
their flexibility), or providing more interactions to have fun (and
antagonize the crew) with when not mainlining their objectives.
## Changelog
:cl: Rhials
add: Ninjas can now temporarily disable cameras with the Ninja MOD
right-click hacking ability.
add: Ninjas can emag windoors, elevator controls, and buttons with their
hacking ability.
add: Ninjas can drain the power from energy weaponry, adding the charge
to their MODsuit.
add: Ninjas can now hack simplebots, overloading and detonating them
after a brief delay.
add: Ninjas can now hack vendors, causing them to eject their inventory
at people.
add: Ninjas can now hack the recycler, which notifies the AI and emags
it once complete.
add: Ninjas can now trigger an extended tram malfunction by hacking the
tram control console.
add: Ninjas can now hack open firelocks (temporarily) with right-click.
balance: Hacking open doors with the Ninja Hacking MODule will subtract
a paltry amount of energy from your suit.
/:cl:

---
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[02cc4b223f...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/02cc4b223f1d84cd0cb35e8e1451c9f1f990a732)
#### Tuesday 2023-08-22 00:40:15 by Jacquerel

Mining mob tweaks (#77763)

## About The Pull Request

~~I wanted to do this after #77700 (wow cool numbers) but nobody has
merged it yet despite how simple it is so i'll just hope they don't
conflict.~~ Thanks san

I'm fucking about with mining mobs with the intention of making them
more interesting but not necessarily towards making mining _harder_, but
some of these changes unquestionably have done so.

These changes are mostly in response to feedback about Watchers who are
definitely significantly more threatening than previously, although some
of this is user error.

- Watchers are annoying when traversing lavaland because they use their
ability on you instantly upon acquiring a target, if you are trying to
escape other fauna this quickly becomes deadly.
- A lot of players don't really realise what the overwatch ability is
actually doing and so just complain about getting machine gunned.
- If you _do_ react properly to the ability it still makes fighting them
take a lot longer than it used to.
- The "look away" icon is hard to see in the dark sometimes

To ammeliorate these factors I have:

- Reduced watcher health by ~20%
- Display an alerted graphic over the head of the watcher every time you
trigger the overwatch.
- Multiple watchers now won't overwatch you at the same time (this made
the "penalty" volley essentially become instant death)
- The "look away" icon is rendered above the lighting plane so you can
always see it
- Added a new component which tracks how long a mob has had a specific
target.
- - Watchers will now only Overwatch you if they've seen you for at
least 5 seconds (usually they'll try and shoot at you twice before
this).
- - Goliaths will only tentacle you if they've seen you for at least 3
seconds.

If overwatch is still problematic after this I guess I can just nerf it
to not track movement at all and only respond to attacks.

## Why It's Good For The Game

I don't want to discourage miners from "actually mining" by having them
get sniped just for walking around and the added time-to-kill on these
guys could make clearing tendrils more tedious too.

## Changelog

:cl:
balance: Watchers have less health
balance: You can't be overwatched by several watchers at a time
balance: Watchers won't overwatch you instantly upon seeing you
balance: Goliaths won't launch tentacles at you instantly upon seeing
you
/:cl:

---
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[19d6b928f8...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/19d6b928f8563c4aa1fdc76a32f3878d0b01cd2d)
#### Tuesday 2023-08-22 00:41:29 by LukasBeedellCodestuff

Compact shotgun re-added (#77759)

## About The Pull Request

This pr seeks to re-add the compact shotgun (slightly buffed with 1 more
ammo) and buff up its larger brother the combat shotgun (with 2 more
ammo.)

## Why It's Good For The Game
With the recent laser buffs, there is a real possibility for the compact
shotgun to return as a unique weapon to make the HOS slightly more
powerful. I am aware that it was a warden's weapon previously but the
HoS doesn't really have many fun toys to play with. The warden already
has crav maga (100x cooler than the laser) so giving this beast to the
HOS could help make it a more attractive and powerful head to play.
(Given 1 extra shot to keep up with the crazy lasers nowadays.)

In regards to the slight combat shotgun buff. The gun itself is ass,
it's barely ever used and the riot shotgun is superior because you can
actually put it in your armour slot. The hope is that this buff will
make people actually use it because it carries a lot of shots now so the
viability may increase.


## Changelog
:cl:
add: Added compact shotgun to the hos locker
add: Added compact shotgun as a traitor objective 
balance: gives the compact shotgun 1 extra shot
/:cl:

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[66152a862d...](https://github.com/git-for-windows/git/commit/66152a862d282113e883c869f6d3f4c26a0f68bf)
#### Tuesday 2023-08-22 00:46:16 by Johannes Schindelin

windows: ignore empty `PATH` elements

When looking up an executable via the `_which` function, Git GUI
imitates the `execlp()` strategy where the environment variable `PATH`
is interpreted as a list of paths in which to search.

For historical reasons, stemming from the olden times when it was
uncommon to download a lot of files from the internet into the current
directory, empty elements in this list are treated as if the current
directory had been specified.

Nowadays, of course, this treatment is highly dangerous as the current
directory often contains files that have just been downloaded and not
yet been inspected by the user. Unix/Linux users are essentially
expected to be very, very careful to simply not add empty `PATH`
elements, i.e. not to make use of that feature.

On Windows, however, it is quite common for `PATH` to contain empty
elements by mistake, e.g. as an unintended left-over entry when an
application was installed from the Windows Store and then uninstalled
manually.

While it would probably make most sense to safe-guard not only Windows
users, it seems to be common practice to ignore these empty `PATH`
elements _only_ on Windows, but not on other platforms.

Sadly, this practice is followed inconsistently between different
software projects, where projects with few, if any, Windows-based
contributors tend to be less consistent or even "blissful" about it.
Here is a non-exhaustive list:

Cygwin:

	It specifically "eats" empty paths when converting path lists to
	POSIX: https://github.com/cygwin/cygwin/commit/753702223c7d

	I.e. it follows the common practice.

PowerShell:

	It specifically ignores empty paths when searching the `PATH`.
	The reason for this is apparently so self-evident that it is not
	even mentioned here:
	https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables#path-information

	I.e. it follows the common practice.

CMD:

	Oh my, CMD. Let's just forget about it, nobody in their right
	(security) mind takes CMD as inspiration. It is so unsafe by
	default that we even planned on dropping `Git CMD` from Git for
	Windows altogether, and only walked back on that plan when we
	found a super ugly hack, just to keep Git's users secure by
	default:

		https://github.com/git-for-windows/MINGW-packages/commit/82172388bb51

	So CMD chooses to hide behind the battle cry "Works as
	Designed!" that all too often leaves users vulnerable. CMD is
	probably the most prominent project whose lead you want to avoid
	following in matters of security.

Win32 API (`CreateProcess()`)

	Just like CMD, `CreateProcess()` adheres to the original design
	of the path lookup in the name of backward compatibility (see
	https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw
	for details):

		If the file name does not contain a directory path, the
		system searches for the executable file in the following
		sequence:

		    1. The directory from which the application loaded.

		    2. The current directory for the parent process.

		    [...]

	I.e. the Win32 API itself chooses backwards compatibility over
	users' safety.

Git LFS:

	There have been not one, not two, but three security advisories
	about Git LFS executing executables from the current directory by
	mistake. As part of one of them, a change was introduced to stop
	treating empty `PATH` elements as equivalent to `.`:
	https://github.com/git-lfs/git-lfs/commit/7cd7bb0a1f0d

	I.e. it follows the common practice.

Go:

	Go does not follow the common practice, and you can think about
	that what you want:
	https://github.com/golang/go/blob/go1.19.3/src/os/exec/lp_windows.go#L114-L135
	https://github.com/golang/go/blob/go1.19.3/src/path/filepath/path_windows.go#L108-L137

Git Credential Manager:

	It tries to imitate Git LFS, but unfortunately misses the empty
	`PATH` element handling. As of time of writing, this is in the
	process of being fixed:
	https://github.com/GitCredentialManager/git-credential-manager/pull/968

So now that we have established that it is a common practice to ignore
empty `PATH` elements on Windows, let's assess this commit's change
using Schneier's Five-Step Process
(https://www.schneier.com/crypto-gram/archives/2002/0415.html#1):

Step 1: What problem does it solve?

	It prevents an entire class of Remote Code Execution exploits via
	Git GUI's `Clone` functionality.

Step 2: How well does it solve that problem?

	Very well. It prevents the attack vector of luring an unsuspecting
	victim into cloning an executable into the worktree root directory
	that Git GUI immediately executes.

Step 3: What other security problems does it cause?

	Maybe non-security problems: If a project (ab-)uses the unsafe
	`PATH` lookup. That would not only be unsafe, though, but
	fragile in the first place because it would break when running
	in a subdirectory. Therefore I would consider this a scenario
	not worth keeping working.

Step 4: What are the costs of this measure?

	Almost nil, except for the time writing up this commit message
	;-)

Step 5: Given the answers to steps two through four, is the security
	measure worth the costs?

	Yes. Keeping Git's users Secure By Default is worth it. It's a
	tiny price to pay compared to the damages even a single
	successful exploit can cost.

So let's follow that common practice in Git GUI, too.

Signed-off-by: Johannes Schindelin <johannes.schindelin@gmx.de>

---
## [ArcaneMusic/TG-Station-Arcane-Remix](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix)@[dc6ddd821b...](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix/commit/dc6ddd821b1d9fe4783cf5d05c4ed2aa96f98e89)
#### Tuesday 2023-08-22 00:56:40 by Cheshify

North Star Science Rework And More (#77439)

## About The Pull Request
I fixed a few miscellaneous issues and also redid science (mainly
genetics, cytology, and xenobiology)
This is genetics, it's basically the same but moneky have bananas and I
rotated it so they'll be visible from the front desk.

![geneticsnew](https://github.com/tgstation/tgstation/assets/73589390/7c10d75b-2a7a-47b2-a6ca-a30354d713c3)

Holy fuck it's Cytology as a proper area. It now has main hall access
and a public access petting zoo. Now you can show off all your new
creatures (it also has some items cytologists generally want)

![cytonew](https://github.com/tgstation/tgstation/assets/73589390/7d9256c9-b39a-4502-b599-9226a2ca5cd8)

Upstairs is Xenobio, which is now much larger and soulless. Instead of a
normal holding cell there's a prefilled room of oxygen and BZ (the
holding room, why is BZ invisible?)

![xenonew](https://github.com/tgstation/tgstation/assets/73589390/5dc28dba-a051-4858-a9fc-16d51e987c33)

I also gave Ordnance 5 TTVs, same as other maps.
Also the coroner no longer has an unreachable box of bodybags
Also sec now has 2 secways + 2 keys for their usage
## Why It's Good For The Game
I'm forcing xenobiologists to be closer to a hall so they might actually
interact with people, and giving cytologists a reason to do anything
ever because they have a petting zoo to show their creatures off in. Oh
yeah also cytology gets equipment they should just have (a botany tray,
tools to butcher with, a shitty old laser gun to kill experiments gone
wrong)
Genetics is just better because people from the hall can see the
Geneticists working so they can bug them for stuff.

A few of the fixes are very tiny, like moving a few areas by the service
hall and adding a single pipe to the AI SAT
## Changelog
:cl:
qol: North Star's Cytology and Xenobiology are now significantly more
usable.
add: North Star's Genetics has been tweaked.
fix: The North Star's AI SAT has a working vent and it's service hall
has a working lightswitch
/:cl:

---
## [janleigh/cc-102](https://github.com/janleigh/cc-102)@[cab6808f51...](https://github.com/janleigh/cc-102/commit/cab6808f51ae5b5a9f6b34bb45944d8703a285ad)
#### Tuesday 2023-08-22 00:57:17 by Jan Leigh Muñoz

chore: use scanf() instead of console args cause fuck you codeblocks

---
## [ArcaneMusic/TG-Station-Arcane-Remix](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix)@[297f7f88e8...](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix/commit/297f7f88e866d4a17b27cb15c0b8ee606742bbf6)
#### Tuesday 2023-08-22 01:01:57 by Sealed101

Fixes things about goliaths: wallhacks/range hacks(no, really) and tentacles not spawning in mineral turfs; also fixes `find_potential_targets` wallhacks (#77393)

## About The Pull Request

Goliath's sand digging behaviour could potentially target a turf that's
actually unreachable by the goliath, e.g.
```
G#
#T
```
where G - goliath # - wall T - target turf. fixed that, but i think
there could be something easier here, maybe instead grabbing turfs in
goliath's `view()`? unsure

The component goliaths use to telegraph their attacks
(`basic_mob_attack_telegraph`) casts a `do_after()` to perform the
attack, but it was not actually checking for the target staying in melee
range, as it was using the source goliath as both `user` and `target`,
so it didn't actually care at all for the target. Implemented an
`extra_checks` to `Adjacent()` since that's the closest we get for melee
range shenanigans I suppose
This still allows the source basicmob to attack the target if the target
moves around the source basicmob.

`!`Goliaths were also able to summon tentacles on a target that moved
into cover and still stayed in the `find_potential_targets` target
range. Which meant more wallhacks. This was a thing for the base
`find_potential_targets`, meaning that every basic mob using it was a
dirty haxxor (or very vengeful). Fixed that by making
`find_potential_targets` also check for `can_see()` before proceeding
further down `find_potential_targets/perform()`. `!` The only exception
to this check currently are bileworms.

`!`Goliath tentacles were not spawning in mineral turfs as their
`Initialize()` checked for closed turfs before handling mineral turf
mining. Fixed that as well.

## Why It's Good For The Game

![Dr__Hax_by_Didgeridoo_Dealer](https://github.com/tgstation/tgstation/assets/75863639/fbcbfc1b-f489-435e-bb01-677f55398787)

## Changelog

:cl:
fix: fixed goliaths digging sand that they can't actually reach (behind
windows or inbetween closed turfs)
fix: fixed goliaths melee attacking their target despite the target
running away from goliath melee range
fix: fixed goliath tentacles not spawning in mineral turfs
fix: fixed goliaths summoning tentacles on targets that moved behind
cover but stayed in their targeting range. this applies for most basic
mobs, really, so if any basic mob was targeting you despite you hauling
ass behind cover, they shouldn't anymore
/:cl:

---
## [Hatterhat/Skyrat-tg](https://github.com/Hatterhat/Skyrat-tg)@[a0a9a43562...](https://github.com/Hatterhat/Skyrat-tg/commit/a0a9a435625f5b89b78394550b5b7b570a3729b4)
#### Tuesday 2023-08-22 01:41:47 by SkyratBot

[MIRROR] Refactors Regal Rats into Basic Mobs (more titles edition) [MDB IGNORE] (#23188)

* Refactors Regal Rats into Basic Mobs (more titles edition) (#77681)

## About The Pull Request

I literally can't focus on anything nowadays, so I just did this to
break a never-ending chain of distress. Anyways, regal rats! These
fellas are mostly player controlled, but did have _some_ AI capabilities
(mainly tied to their actions), so that was incorporated too. Everything
should work as-expected (as well as look a shitload cleaner).

Instead of doing weird and awful conditional signals being sent out, I
made the `COMSIG_REGAL_RAT_INTERACT` (not the actual name) have a return
value so we can always rely on that working whenever we have that signal
registered on something we attack. I also cleaned up pretty much every
proc related to regal rats, gave them AIs to reflect their kingly nature
(and action capabilities (as well as move the action to
`mob_cooldown`)).

Since I thought they needed it, Regal Rats now get a special moniker!
This is stuff like "the Big Cheese" and what-not, like actual regents in
history. That's nice.
## Why It's Good For The Game

Two more off the list. Much better code to read. Way smarter rats with
spawning their army as part of a retaliatory assault (war). More sovl
with better regal rat names. The list goes on.
## Changelog
:cl:
refactor: Regal Rats have been refactored into basic mobs. They should
be a bit smarter and retain their docility (until attacked, in which
case you should prepare to get rekt by summoned rats), and properly flee
when they can instead of just sit there as you beat them to death. The
framework for them interacting with stuff (i.e. opening doors while
slobbering on food) is a bit more unified too, now. They also have
cooler names too!
/:cl:

FYI: Beyond a few code touchups, I haven't touched the actions at all. I
do not believe myself to be enthusiastic about fixing anything involving
the actions code as of this moment so that this PR is more overbloated
unless it's unbelievably stupid or easy to fix.

* Refactors Regal Rats into Basic Mobs (more titles edition)

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [dwasint/Monkestation2.0](https://github.com/dwasint/Monkestation2.0)@[afb791ca88...](https://github.com/dwasint/Monkestation2.0/commit/afb791ca88904597f332a8efdd7a151e532f3237)
#### Tuesday 2023-08-22 02:07:12 by Jacquerel

Goliath basic mob (#76754)

Converts Goliaths to the basic mob framework and gives them some new
moves because I can't leave things well enough alone.
I am planning on touching all the lavaland fauna and then maybe even the
icebox ones if I haven't got bored. The Golaith is the first because it
is iconic.

https://www.youtube.com/watch?v=JNcKvMwT4-Q
Here's me getting killed by one as a demonstration. Despite my poor
performance I would contend that they aren't a _lot_ more dangerous, but
they are a little more dangerous.

The chief difference here is that they have two new attacks which they
will only use in response to being attacked.
If fired at from range, they will target the attacker with a line of
tentacles (it doesn't track you, so is easily sidestepped).
If attacked in melee, they will surround _themselves_ with tentacles, on
a longer cooldown.

Something else you may notice in this video: I discovered that basic
mobs are actually _too smart_ to be Lavaland fauna.
Typically (unlike their old form) a mob on our new AI system is smart
enough to attack someone _the moment they come into range_ rather than
only checking on predictable ticks, which would make using the Crusher
an essentially unviable prospect.
To counteract this, Goliaths now have a delayed attack component which
gives you a visual warning and short duration to get out of range before
they swing at you. I will probably put this on all mining fauna that get
reworked, it wouldn't be a terrible thing to put on other mobs to be
honest.

Other changes: The goliath stun is now a status effect with _buckles_
you to the tentacle as if grabbed, as well as its previous effects.
While this seems purely worse, any nearby helpers can now help-click on
you to instantly remove the debuff.
Experiencing the effect of a Lobstrosity Rush Gland makes you immune to
being grabbed by tentacles and an implanted one will automatically
trigger and free you if you are hit, and the explosive effect of
Brimdust also causes the tentacle to retract (although you'd need to
take damage for this to happen). Using the tools of the land, you can
make these creatures less threatening.

The ability for a Goliath to chain-apply the ability has now also been
reduced, it won't refresh its duration if you are hit when already
buckled.

When not occupied hounding miners, Goliaths will intermittently dig up
the asteroid sand and eat any worms that this produces.
I also made some new sprites for riding a Goliath because they've been
broken since the Lavaland mob update and also kind of were ugly before
then anyway:

![image](https://github.com/tgstation/tgstation/assets/7483112/90580403-d82f-4c29-b3e1-6c462e01edda)

Other code changes:
- I made an element which only lets an attached object move every x
seconds. This is because Goliaths are far too slow to use the speed
system (the glide just looks bugged as hell) but one thing I am invested
in when converting these is to make sure that they share the same
behaviour when player or AI controlled. This is disabled while you're
riding them because it was interminably slow.
- The Goliath tentacle trail uses a supertype object now shared with the
Meteor Heart which did something kind of similar.

It begins the process of moving one of our larger subsets of NPCs onto
the newer framework for NPC behaviour.
It adds a little bit more life to an iconic but slightly uninteresting
foe which mostly just walked at you slowly.
This PR contains a few components I expect to apply more widely to other
mobs in the future.

:cl:
refactor: Goliaths now use the Basic Mob framework, please report any
unusual behaviour.
add: Goliaths learned a couple of new attacks which they will use in
self-defence.
balance: Help-clicking a miner grabbed by Goliath tentacles will
immediately free them, as will the effect of several items you can
scavenge from around Lavaland.
image: New sprites for the Goliath saddle.
/:cl:

---
## [dwasint/Monkestation2.0](https://github.com/dwasint/Monkestation2.0)@[65136f78e0...](https://github.com/dwasint/Monkestation2.0/commit/65136f78e0621b0ba2777707c05163bfa092d227)
#### Tuesday 2023-08-22 02:07:12 by LemonInTheDark

Optimizes timer insertion by 80% (W QDEL_IN micro) (#76214)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

[Reduces timer insertion cost by
80%](https://github.com/tgstation/tgstation/commit/c9e5b285ed74e60108fddd3f6b45d6d3995c92a8)

Timer name generation involved a LOT of string shit, some in ways where
the string only existed for a moment.
This costs a good bit of time, and can be reduced with only minimal
impacts on the end product, so let's do that. Includes a compile flag to
flip it back if we ever have trouble in future.

This is about 0.1s off init, since we do a lot of timer stuff then too

[Removes STOPPABLE flag from QDEL_IN, moves it to a bespoke
macro](https://github.com/tgstation/tgstation/commit/e7a5d7f2a78fcf0dce4742ced258c9505411b202)

Its a waste most of the time, tho I would LOVE to analyze at compile
time to work out if we care

I like it when we don't spend all of our cpu time just setting the name
var on timers. that's good and not bad.
This saves time fucking everywhere. 15% off explosions, 0.1 seconds off
init, bunch of time off foam. it's just good.

Cherry picked out of #76104 since that was too cluttered (sannnnnn)

<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [j12bates/Innullifiability](https://github.com/j12bates/Innullifiability)@[206e895a7d...](https://github.com/j12bates/Innullifiability/commit/206e895a7daa6b425f87a60aa42a3990f7c084d4)
#### Tuesday 2023-08-22 02:33:02 by Jacob Bates

Exhaustive Test - Optimized Length-3

Now the recursive function bases out at length-3 sets, and a separate
function takes it from there. The function does a simple equality check,
and then tries out operations to see if it can make two values into the
remaining one. At first, I thought I had to do this in a for-loop to get
all the different possible arrangements, but as it turns out, I don't
have to, as anything can be rearranged by inverse operations to just the
original possibilities. How cool is that? I wonder if I could use that
principle to optimize the recursive logic. But anyways, this new
function is vastly simpler and will return a result much faster than
going back through the recursive function's logic.

Then I made another simplification: the user-mode function now also
ensures there are no zeros, so the other logic doesn't have to deal with
that. It'd be redundant to check if there are equal values every time
but then also check for zeros, as they can only come from equal values.

The N = 6, M <= 40 case now only takes 0.79s to run, and the weeding
phase of that has been reduced to 0.120s. As for the N = 7, M <= 81 case
(which, as I should have clarified earlier, was also just the weeding
phase), it went down to 25s. Also, it turns out disk I/O isn't included
in user time, meaning my measurements from before are also good. Holy
mackerel, this is so much faster than before!

---
## [SathiaPang/BelteiConstruction](https://github.com/SathiaPang/BelteiConstruction)@[9790901e26...](https://github.com/SathiaPang/BelteiConstruction/commit/9790901e2694801b0a123ca706f9dd29f93f63da)
#### Tuesday 2023-08-22 02:49:23 by SathiaPang

Merge pull request #1 from SoeunKimsong/main

fuck you satia

---
## [Fennec82/ChaosStation--Coyote-Bayou](https://github.com/Fennec82/ChaosStation--Coyote-Bayou)@[aac465cc2a...](https://github.com/Fennec82/ChaosStation--Coyote-Bayou/commit/aac465cc2a5026b18fcab3cd7b7eefde77d2d8a3)
#### Tuesday 2023-08-22 02:52:13 by Tk420634

Don't worry about it

hate telemetry warnings, yeah they're great and all but fuck the fuck off

---
## [livelyupward/foreway-golf](https://github.com/livelyupward/foreway-golf)@[bc66607c60...](https://github.com/livelyupward/foreway-golf/commit/bc66607c602b78d521daa7c679a13744981e28ea)
#### Tuesday 2023-08-22 02:59:11 by Dave Grammas

Removed rounded border design. Dealing with rounding all corners was a pain in the ass and it's better with sharp edges in my opinion.

---
## [c3nn/notwikipedia](https://github.com/c3nn/notwikipedia)@[700484d45a...](https://github.com/c3nn/notwikipedia/commit/700484d45aab18b2222e59f334cfc76daeb01829)
#### Tuesday 2023-08-22 03:09:56 by Conmann

added one slash to fix the whole issue

i hate my life

---
## [newstools/2023-information-nigeria](https://github.com/newstools/2023-information-nigeria)@[d8531621d6...](https://github.com/newstools/2023-information-nigeria/commit/d8531621d63cae1f29e933a8beeec6d9b8b27b3c)
#### Tuesday 2023-08-22 03:15:29 by Billy Einkamerer

Created Text For URL [www.informationng.com/2023/08/lve-been-in-over-40-robberies-evil-spirit-makes-me-steal-16-year-old-suspect-confesses.html]

---
## [BeagleGaming1/cmss13](https://github.com/BeagleGaming1/cmss13)@[f3fc60ed65...](https://github.com/BeagleGaming1/cmss13/commit/f3fc60ed655d27bb3f012d0e0d834c64990b173d)
#### Tuesday 2023-08-22 03:38:52 by morrowwolf

Attachment nerfs and removals (#4122)

# About the pull request

This PR:

Removes the barrel charger from vendors

Removes all benefits other than wield delay mod from the angled grip

Adds wield delay to the extended barrel

# Explain why it's good for the game

Barrel charger is a straight damage increase and rather silly to work
around given how burst works bypassing real fire rate concerns. If you
know, you know. Horrible idea, I am amazed it's been around this long.

Angled grip had zero downside. Now it still has zero downside but isn't
also a ton of accuracy buffs on top of the god-tier lower wield delay.

Extended barrel had zero downside. Now it has a downside.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

:cl: Morrow
balance: Removed the barrel charger from vendors
balance: Removed all benefits other than wield delay mod from the angled
grip
balance: Added wield delay to extended barrel
/:cl:

---
## [dwasint/Monkestation2.0](https://github.com/dwasint/Monkestation2.0)@[cc1ab48bd8...](https://github.com/dwasint/Monkestation2.0/commit/cc1ab48bd83b958d59d3366e199160e5027de00b)
#### Tuesday 2023-08-22 03:53:59 by san7890

Refactors Regal Rats into Basic Mobs (more titles edition) (#77681)

I literally can't focus on anything nowadays, so I just did this to
break a never-ending chain of distress. Anyways, regal rats! These
fellas are mostly player controlled, but did have _some_ AI capabilities
(mainly tied to their actions), so that was incorporated too. Everything
should work as-expected (as well as look a shitload cleaner).

Instead of doing weird and awful conditional signals being sent out, I
made the `COMSIG_REGAL_RAT_INTERACT` (not the actual name) have a return
value so we can always rely on that working whenever we have that signal
registered on something we attack. I also cleaned up pretty much every
proc related to regal rats, gave them AIs to reflect their kingly nature
(and action capabilities (as well as move the action to
`mob_cooldown`)).

Since I thought they needed it, Regal Rats now get a special moniker!
This is stuff like "the Big Cheese" and what-not, like actual regents in
history. That's nice.

Two more off the list. Much better code to read. Way smarter rats with
spawning their army as part of a retaliatory assault (war). More sovl
with better regal rat names. The list goes on.
:cl:
refactor: Regal Rats have been refactored into basic mobs. They should
be a bit smarter and retain their docility (until attacked, in which
case you should prepare to get rekt by summoned rats), and properly flee
when they can instead of just sit there as you beat them to death. The
framework for them interacting with stuff (i.e. opening doors while
slobbering on food) is a bit more unified too, now. They also have
cooler names too!
/:cl:

FYI: Beyond a few code touchups, I haven't touched the actions at all. I
do not believe myself to be enthusiastic about fixing anything involving
the actions code as of this moment so that this PR is more overbloated
unless it's unbelievably stupid or easy to fix.

---
## [dwasint/Monkestation2.0](https://github.com/dwasint/Monkestation2.0)@[b0f53fcff6...](https://github.com/dwasint/Monkestation2.0/commit/b0f53fcff6a053be43225ed3edbc92c89b60f226)
#### Tuesday 2023-08-22 03:53:59 by Sealed101

Dog wit the butter (feat. a bunch of dog-related code improvements) (#77039)

Adds a `dog_fashion` for the stick of butter.(screenshot is outdated as
Lisa won't have butter no more)
![butter
dawgs](https://github.com/tgstation/tgstation/assets/75863639/a22e702c-98a8-4283-abd9-28d4a9fb3bd0)

Also cleans up dog.dm because it was SHIT and FUCK and MY FUCKING GOD
TWO INITIALIZE()s TWO TIMES IN A SINGLE FILE WHAT IN THE GODDAMN

Most noticeably, Lisa properly won't wear any hats, and puppies properly
can't wear head/back items (by just removing those item slots from the
strip/equip menu. if some admeme wants to fumble around they may still
equip shit there. but otherwise for a normal player those slots are
inaccessible).
Basic mobs now also send signals when they run
`appear_dead`/`appear_alive` procs, which corgis hook into to update
their dead fashion overlays.
The side-effect of getting that to work is that dogs (and any basic mob
that uses `play_dead` ai behavior) are so good at feigning death, that
they fool medical HUDs and other related things. They're just that good.
There's a bunch of other things involved and I was mostly just being
angry at the state of the file so I'll check back when I gather all
things changed.

![strippy](https://github.com/tgstation/tgstation/assets/75863639/ec4d17a2-d4df-401c-bd1f-7c4ee1b95671)

https://github.com/tgstation/tgstation/assets/75863639/b34589cb-94d6-4b80-bf0f-1814c08da100

:cl:
add: dog with a butter on 'em
add: dead dog with da butter on 'em (dogs feigning death are so good at
it, they appear dead to medical HUDs and other things)
add: Nars-Ian now can revive from the dead if he consumes a pet
fix: fixes dog fashion items with no speech modifiers set making dressed
up corgis unable to perform their speech or emote behaviors
fix: fixes old Ian losing his mobility ride when shaved with a razor
fix: fixes pets not dropping their collar when gibbed
fix: butter don't go on Lisa and corgi puppies (Lisa won't wear hats and
corgi puppies can't wear hats and back slot items)
/:cl:

---
## [dwasint/Monkestation2.0](https://github.com/dwasint/Monkestation2.0)@[01e034a63a...](https://github.com/dwasint/Monkestation2.0/commit/01e034a63afe86bc21b439d1474318f31b7ddf95)
#### Tuesday 2023-08-22 03:53:59 by Ben10Omintrix

convert the eyeball a basic monster (#77411)

I have created a basic eyeball monster with new abilities and behaviors.
The eyeball has a unique power that allows it to glare at humans and
make them slow for a short period. However, this ability only works if
the human can see the eyeball monster. If a person is blind or unable to
see the eyeball, the ability won't affect them. Also, if someone turns
their back to the eyeball, it cannot use the ability on them. But be
cautious because the eyeball will try to position itself in front of the
person's face to use its power.

The eyeball is hostile towards all humans except for the blind ones and
those with significant eye damage. It has a compassionate side too, as
it loves to help people with eye damage by providing small healing to
their eyes.

Furthermore, the eyeball has a fondness for eating carrots, which not
only satisfies its appetite but also grants it a small health boost. To
add to its appearance, I've given it a new, larger, and scarier sprite.
However, I am open to changing it back to the old sprite if the player
prefers it that way.

Additionally, the eyeball displays emotions, and if you hit it, it will
cry tears as a sign of pain or sadness.
![eyeballs
pictures](https://github.com/tgstation/tgstation/assets/138636438/8933ea63-d339-474b-8c6e-90a222b74945)

the eyeball now have more depth and character to his behavier.

:cl:
refactor: the eyeball is a basic monster, please report any bugs
sprites: the eyeball now is bigger and scarier and now he will cry when
u hit him
/:cl:

---
## [dwasint/Monkestation2.0](https://github.com/dwasint/Monkestation2.0)@[c5e59b8965...](https://github.com/dwasint/Monkestation2.0/commit/c5e59b8965bbf6753288b90652aa76ed5c98a104)
#### Tuesday 2023-08-22 03:53:59 by san7890

Refactors Slaughter/Laughter Demons into Basic Mobs (#77206)

On the tin, the former "imp" is now refactored into basic mob code. Very
simple since these are only meant to be controlled by players, and all
of their stuff was on Signal Handlers and Cooldown Actions anyways. Just
lessens the amount of stupidity.

Did you know that we were trying to make demons spawn in a `pop`'d cat
named "Laughter"? Embedded in the list? I've literally never seen this
cat, so I'm under heavy suspicion that the code we were using was broken
for the longest time (or may have never worked), and we now instead just
do it a much more sane way of having a cat spawn on our demise.

Cleaner code! Less simple mob jank to deal with. Trims down the list of
simple animals to refactor. No more duplicated code that we were already
doing on parent! It's so good man literally everything was seamless with
a bit of retooling and tinkering. The typepath is also no longer `imp`,
it's actually `demon`, which I'm happy with because there's no other
demons to have it be confused with anymore.

We were also doing copypasta on both the demon spawner bottle and the
demon spawning event so I also just unified that into the mob. I also
reorganized the sprites to be a bit clearer and match their new
nomenclature

:cl:
refactor: Slaughter and Laughter Demons have been refactored, please
place an issue report for any unexpected things/hitches.
fix: Laughter Demons should now actually drop a kitten.
/:cl:

---
## [dwasint/Monkestation2.0](https://github.com/dwasint/Monkestation2.0)@[f3bf27b467...](https://github.com/dwasint/Monkestation2.0/commit/f3bf27b46721e1e60a456585e99f8168dc889486)
#### Tuesday 2023-08-22 03:53:59 by Jacquerel

Basic Watchers & Basilisks (#77630)

This one is a double feature because Watchers and Basilisks share the
same typepath. You might see a couple more of those.
As is tradition I decided to fuck with them rather than just port them.
Here's what's up.

**Basilisks**

![image](https://github.com/tgstation/tgstation/assets/7483112/9e4b0115-65dd-4df7-b62a-21c7be8549bf)

![image](https://github.com/tgstation/tgstation/assets/7483112/59162e68-7d73-4659-9531-5078ff751228)

- Have a new soulless sprite which looks less like a living blue hedge.
- Walk at you and shoot you while you are not in range (just like
before).
- Become supercharged if they become "heated" by lava, lasers, or
temperature weapons. This was a feature they also previously had but
they would never encounter lava, so now it also works if you use the
wrong gun on them.
- Lose their supercharge if you cool them down.
- Otherwise pretty normal mobs.

**Watchers**

https://www.youtube.com/watch?v=kOq_Bf78k5A
Here's a traditional video of me intentionally getting hit by mechanics
(trust me its definitely on purpose)

- They glow emmissively a little bit so you can see them from further
away.
- Their eyes light up about 0.5 seconds before they are able to shoot at
you.
- No longer melee attack, instead try to stay out of melee.
- Will occasionally put you into "Overwatch", meaning they will shoot
you rapidly if you move or act while they're staring at you for a brief
time period (after which you become immune for 12 seconds, and during
which other watchers will play fair and stop shooting at you).
- If they start taking damage they will also start using their "Gaze"
attack, look away or suffer some kind of negative effect!
- - Normal watcher gaze flashes and confuses you.
- - Magmawing watcher gaze obviously burns (and briefly stuns) you.
- - Icewing watcher gaze freezes you and throws you backwards.
- Magnetically attract and eat diamonds. They also used to do this, but
just if they happened to coincidentally walk past some.

**Other accompanying changes**

All basic mobs will now adopt the "stop gliding" trait if they get
slowed down too much.
I moved behaviour for "fire a projectile from this atom" into a helper
proc because I was using it in three places and I will probably use it
in more places. There are probably other places in the existing code
which could be using this.
I think I made the basic mob melee attack forecast default a little more
forgiving, they were fucking me up too much and I am the playtester.

Another one off the list.
New tricks for old dogs.
Framework for making mobs with ranged attacks "fairer" (you can see when
they are ready to shoot you).
More (hopefully) versatile AI behaviours which we will reuse later (I
hope I'm not duplicating one someone already made).
If our players "enjoy" them enough we can give more mobs "don't look at
me" mechanics.
Removes some soul sprites.

:cl:
refactor: Basilisks and Watchers now use the basic mob framework. Please
bug report any unusual behaviour.
sprite: Basilisks have new sprites.
add: Basilisks will go into a frenzy if heated by energy weapons or
temperature beams as well as by lava.
add: Watcher eyes will be illuminated briefly when they are ready to
fire at you.
add: Watchers can now briefly put you into "Overwatch" and penalise you
for moving while they can see you.
add: Wounded watchers will occasionally punish players who look at them.
balance: Unusual watcher variants are more likely to appear.
/:cl:

---
## [dwasint/Monkestation2.0](https://github.com/dwasint/Monkestation2.0)@[f1998f5aaa...](https://github.com/dwasint/Monkestation2.0/commit/f1998f5aaa7aed6b6118f7d79bf9fa29e4cb6624)
#### Tuesday 2023-08-22 03:53:59 by san7890

Refactors Morphs into Basic Mobs (there is now a swag action for morphification) (#77503)

I was bored, so did this. Probably one of the neatest refactors I've
done, sorry if there's some oddities because I was experimenting with
some other stuff in this so just tell me to clean them up whenever I
can.

Anyways, morphs are basic mobs now. We are able to easily refactor the
whole "eat items and corpses" stuff in the basic mob framework, but the
whole "morph into objects and people" turned out to be a bit trickier.
That was easily rectified with a datum mob cooldown action and
copy-pasting the old code into that code, as well as doing some nice
stuff with traits and signals to ensure the one-way communication from
the action to the mob.

Old Morph AI didn't seem to be existant whatsoever, they inappropriately
leveraged some old procs and I have no idea how to make it work with new
AI. They DEFINITELY don't spawn outside of admin interference/ the event
anymore, and will always be controlled by a player, so this shouldn't be
too bad of an issue. I gave them something to seem alive just in case
though, but I think adding legitimate prop-hunt AI would be such a
laborious task that I am unwilling to do it in this PR.

If admins want to add the ability for Ian to assume the form of the HoP,
they can do that now! The datum action cooldown is quite nice for simple
and basic mobs... but it is currently not compatible with carbons. That
is not within scope for this PR, but I am dwelling on ways to extend it
to carbon but they all sound really awfully bad.

Also morphs are smarter, and we tick another simple animal in need of
refactoring off the list.
:cl:
refactor: Morphs are now basic mobs with a nice new ability to help you
change forms rather than the old shift-click method, much more
intuitive.
admin: With the morph rework comes a new ability you can add to mobs,
"Assume Form". Feel free to add that to any simple or basic mob for le
funnies as Runtime turns into a pen or something.
/:cl:

~~Does anyone know if there's a (sane) way to alias a cooldown action as
a keypress? I can't think of a good way to retain the old shift-click
functionality, because that does feel _kinda_ nice, but I think it can
be lived without.~~ I added it. Kinda fugly but whatever.

---
## [newstools/2023-cbs-news](https://github.com/newstools/2023-cbs-news)@[b8095d6a30...](https://github.com/newstools/2023-cbs-news/commit/b8095d6a30734691d1e8d7c0405147ad3408b04d)
#### Tuesday 2023-08-22 04:38:15 by Billy Einkamerer

Created Text For URL [www.cbsnews.com/news/mackenzie-shirilla-sentenced-ohio-crash-15-years-to-life-in-deaths-of-boyfriend-friend/]

---
## [FlufflesTheDog/tgstation](https://github.com/FlufflesTheDog/tgstation)@[2d34c7433a...](https://github.com/FlufflesTheDog/tgstation/commit/2d34c7433a0c5315e6a46f7e32e2c9a6c90280b3)
#### Tuesday 2023-08-22 05:24:35 by Andrew

New Mech UI and equipment refactor (#77221)

![bWJlVIDO53](https://github.com/tgstation/tgstation/assets/3625094/d75030b5-59e9-43f6-96b4-1b7564caceef)

## About The Pull Request

Made a new UI and refactored some mech code in the process.

Fixes #66048
Fixes #77051
Fixes #65958 ??? if it was broken
Fixes #73051 - see details below
Fixes other undocumented things, see changelog.

## Why It's Good For The Game

The UI was too bulky and Mechs were too complex for no reason. 
Now they follow some general rules shared between other SS13 machinery,
and there is less magic happening under the hood.

## Detailed Changes

### New Mech UI, Air Tank and Radio as separate modules

Previous UI for comparison:

<img alt="9SScrXAOjy"
src="https://github.com/tgstation/tgstation/assets/3625094/904e3d07-e7d7-4d3a-a062-93e0e35b4b66">

Previously mechs came with radio pre-installed and air canisters
magically pre-filled with air even when you build one in fab.
Radio and Air Tanks are now both utility modules that are optional to
install. Gas RCS thrusters still require Air Tank module to operate.

This made the Mechs more barebones when built, giving you only the basic
functionality.

<img alt="5SDMlXTJxv"
src="https://github.com/tgstation/tgstation/assets/3625094/b9364230-49ac-416b-aa70-e851fbf2050e">

To compensate this change, all mechs got two extra utility module slots.

All other modules got new UI. And ore box now shows the list of ores
inside.

<img alt="SRX5FjvsHA"
src="https://github.com/tgstation/tgstation/assets/3625094/cbe2e98d-1cd4-4667-8dae-2f9227b4b265">

### Mounted Radio

Works as a normal radio, but with subspace transmission. Available from
the basic mech research node and can be printed in fab.

### Cabin Sealing

To compensate for the lack of air tank by default, mechs with enclosed
cabin (e.g. all except Ripley) got an ability to toggle cabin exposure
to the outside air. Exiting the mech makes cabin air automatically
exposed.

When you seal the cabin, it traps some of the outside air inside the
cabin and you can breathe with this air to perform a short space trips.
But the oxygen will run out quickly and CO2 will build up.

Sealing the cabin in space will make the cabin filled with vacuum, and
it will stay there until you return to air environment and unseal the
cabin, letting the breathable air to enter. There are temperature and
pressure sensors that turn yellow/red when the corresponding warning
thresholds are reached.

You could also use personal internals in combination with cabin sealing
for long space travels, so Air Tank is completely optional now and
mostly needed when you need RCS thruster.

### RCS thrusters

They are now available earlier in tech tree and consume reasonable
amount of air (5 times more than human jetpacks), and they don't work
without Mounted Air Tank, unless it's an Ion thruster variant.

### Mounted Air Tank

Available from the basic mech research node and can be printed in fab.
Built model comes empty, and syndicate mechs come with one full of
oxygen.

<img alt="GrFDrH5Hwe"
src="https://github.com/tgstation/tgstation/assets/3625094/b677b705-bda0-4c8c-96c7-d32bf7bf9f28">

Can be switched to pressurize or not pressurize the cabin. Releases gas
only when the cabin is sealed shut. Starts releasing automatically, but
can be toggled to not release if you want to use it just as a portable
canister.

Cabin pressure can now be configured in the module UI instead of
Maintenance UI.

Can be attached to a pipe network when the mech is parked above a
connection port.

Comes with a pump that works similarly to the portable pump. It lets you
vent the air tank contents outside, or suck air from the room to fill
the air tank. Intended to provide an ability to fill the air tank
without the need to bother with pipes.

Also has gas sensors that display gas mix data of the tank and the cabin
(when sealed).

### Stock part changes

All mechs now require a servo motor and they reduce mech movement power
consumption instead of scanning module.

Scanning modules are optional for mech operation (still required to
build) and the lack of one disables the following UI elements:

- Display of mech integrity (you can still see the alerts or examine the
mech to get rough idea)
- Display of mech status on internal damage (and you can't repair what
you can't diagnose)

The rating of scanning module doesn't have any effect as of now.

Cargo mech comes without it roundstart.

<img alt="2vDtt99oqb"
src="https://github.com/tgstation/tgstation/assets/3625094/147144ca-824e-4501-acf5-6ee104f309e7">

Capacitors now also reduce light power usage and raise the overclocking
temperature thresholds (see below).

### Maintenance

Maintenance UI removed, and its logic migrated to other places.

Access modification now managed inside the mech, and anyone who can
control the mech, can adjust the access in the same way as they can set
DNA key.

To open the maintenance panel you just need a screwdriver. It is instant
when the mech is empty and it has a 5 second delay when there is an
occupant to avoid in-combat hacking and part removal. It will alert the
occupant that someone is trying to tinker with their mech.


![image](https://github.com/tgstation/tgstation/assets/3625094/1abfca3c-8ba9-44b0-913c-c209564b91fd)

Once the panel is open, you can see the part ratings:


![image](https://github.com/tgstation/tgstation/assets/3625094/404f95bb-9f74-4e5b-a975-5ab6f74bdfa9)

With open panel you can hack the mech wires (roboticists can now see
them):

<img alt="mj205G2qDa"
src="https://github.com/tgstation/tgstation/assets/3625094/44cea0d1-44b4-4b50-b1d3-a97c0056bab3">

There are wires for:
- Enabling/Disabling ID and DNA locks
- Toggling mech lights
- Toggling mech circuits malfunction (battery drain, sparks) 
- Toggling mech equipment malfunction (to repair after EMP or cause
EMP-like effect, disarming mech)
- 3 dud wires that do nothing

The hacker may be shocked if the mech power cell allows.

When the panel is open and the user has access to the mech, they can
remove parts with a crowbar:

<img alt="jR40gyTWtJ"
src="https://github.com/tgstation/tgstation/assets/3625094/b573f5b9-b8ea-412e-b3e0-c872e01e0c23">

Hitting the mech with an ID from outside now toggles the ID Lock on/off
if the ID has sufficient access.

### Power consumption and overclocking

Rebalanced mech power consumption. T4 parts were not working in
Syndicate Mechs, as their effect was not calculated until you manipulate
parts manually. Constructed mechs with t1 parts even had their energy
drain reduced with upgrade to t1.

Now all mechs apply their base step power usage correctly don't ignore
the stock parts.

Servo tier now reduces base power consumption by 0% at t1, 50% at t2,
33% at t3 and 25% at t4
Capacitor tier now reduces base power consumption of mele attacks,
phasing and light by the same amounts.

Gygax leg actuators overload replaced with mech overclocking. Any mech
can be overclocked by hacking wires, but only Gygax has a button for
toggling it from the Cabin.

Now there is an overclock coefficient. 1.5 for Gygax and other mechs, 2
for Dark Gygax.

When overclocked, mechs moves N times faster, but consumes N times more
power.


![image](https://github.com/tgstation/tgstation/assets/3625094/01e285fd-6fd6-4558-8277-2ed3abf474d8)

While overclocked, mech heats up every second, regardless of movement,
and starts receiving internal and integrity damage after a certain
temperature threshold. The chance is 0% at the threshold, and 100% at
thresholds * 2. The roll happens every tick. Capacitor upgrades this
threshold, letting you overclock safely for longer periods.


![image](https://github.com/tgstation/tgstation/assets/3625094/80d90cea-0d20-4054-9369-a47deb6f52f2)

When you stop overclock, the temperature goes back down.

### Other changes and fixes

Concealed weapon bay now doesn't show up when you examine the mech, so
it's actually concealed now.

New radio module can properly change its frequency, as it didn't work
for previous radio.

Launcher type weapons were ignoring cooldowns and power usage, so you
could spam explosive banana peals, while they should have a 2 second
cooldown:
<img alt="q5GjUsHwGr"
src="https://github.com/tgstation/tgstation/assets/3625094/d102725d-e9e1-4588-9d6c-b9e38b7a6535">

Now this is fixed and all launcher type weapons properly use power and
have their cooldowns working.
And now they have the kickback effect working (when it pushes you in the
opposite direction in zero gravity on throw).

Thermoregulator now heats/cools considering heat capacity instead of
adding/reducing flat 10 degrees. So you can heat up cabin air quicker if
the pressure is low.

There were some other sloppy mistakes in mech code, like some functions
returning too early, blocking other functionality unintentionally. Fixed
these and made some other minor changes and improvements.

## Changelog

:cl:
refactor: Refactored Mech UI
refactor: Refactored mech radio into a utility module, adding extra slot
to all mechs
refactor: Refactored mech air tank into a utility module with an air
pump, adding extra slot to all mechs
refactor: Refactored mech cabin air - there is now a button to seal or
unseal cabin to make it airtight or exchanging gases with the
environment
refactor: Removed mech maintenance UI Access is set in mech UI, and
parts are ejected with a crowbar
add: Mech now has wires and can be hacked
qol: Roboticists now can see MOD suit and mech wires
add: Mechs now require servo motor stock part and it affects movement
power usage instead of scanning module
add: Scanning module absence doesnt block mech movement and hides some
UI data instead. Big Bess starts without one.
qol: Hitting mech with ID card now toggles ID lock on/off if the card
has required access
fix: Fixed concealed weapon bay not being concealed on mech examine
fix: Fixed mech radio not changing frequency
fix: Fixed mech launcher type weapons ignoring specified cooldown
fix: Fixed mech launcher type weapons not using specified power amount
fix: Fixed mech temperature regulator ignoring gas heat capacity
fix: Fixed mech stopping processing other things while not heating
internal air
fix: Fixed mech being able to leave transit tube in transit
fix: Fixed mech internal damage flags working incorrectly
fix: Fixed Gygax leg overloading being useless
fix: Fixed mechs ignoring their stock parts on creation. Syndicate mechs
now stronger against lasers and consume less energy on move. Upgrading
from tier 1 to tier 2 doesn't make mech consume MORE energy than before
the upgrade.
balance: Rebalanced mech energy drain with part upgrades. Base energy
drain reduced by 50%, 33%, 25% with upgrades and applies to movement
(Servo rating), phasing, punching, light (Capacitor rating).
balance: Hydraulic clamp now can force open airlocks
balance: Made mech RCS pack consume reasonable amount of gas
code: Fixed some other minor bugs and made some minor changes in the
mech code
/:cl:

---------

Co-authored-by: SyncIt21 <110812394+SyncIt21@users.noreply.github.com>
Co-authored-by: Sealed101 <cool.bullseye@yandex.ru>
Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [GuillaumePrata/tgstation](https://github.com/GuillaumePrata/tgstation)@[c8266cf0a2...](https://github.com/GuillaumePrata/tgstation/commit/c8266cf0a2effaf8b931ba870c124608305b7d68)
#### Tuesday 2023-08-22 05:31:13 by necromanceranne

Settler Quirk: Tame the Outdoors! Have trouble with tall shelves... (#77654)

## About The Pull Request

Adds the Settler quirk. This gives you bonuses to taming animals and
fishing, as well as making you gain hunger slower than others.

However, you are quite a bit slower than most people, and have trouble
with vaulting objects. You do, however, suffer significantly less from
equipment slowdown. (to the point that it is almost zero)

Settler riders are faster on their mounts than others if they're at
least sane. They start to slow down if they're less sane.

You are also shorter than most people. 

<details>
  <summary>Typical Settler encounters the typical Spacer</summary>
  

![Dr_Xr1nU0AAMsSE](https://github.com/tgstation/tgstation/assets/40847847/86ed4947-de5f-4bdf-a8ae-521dc7c30662)
  
</details>

## Why It's Good For The Game

I wanted to add a lightweight quirk that was kind of the 'opposite' of
Spacer, but a little more focused on interacting with elements of the
game world that would enjoy some attention. So, I thought 'what about an
outdoorsman quirk?'

So, I based it around being from people who lived out on the rim, under
unideal circumstances (and probably heavier gravity than Earth), and
taming the land. The slower movespeed encourages finding an animal to
tame that you can ride, and the bonuses to taming should help make that
a bit easier. The other additions just made sense for someone living it
a bit rough in the wilderness.

Having a bunch of settlers taming cows and riding around on them all
shift just kind of sounds hilarious to me.

## Changelog
:cl:
add: Settler quirk! Conqueror the great outdoors....in space. Just make
sure nobody asks you to get anything from the top shelf.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [Steveice10/yuzu](https://github.com/Steveice10/yuzu)@[8e703e08df...](https://github.com/Steveice10/yuzu/commit/8e703e08dfcf735a08df2ceff6a05221b7cc981f)
#### Tuesday 2023-08-22 06:22:15 by comex

Implement SSL service

This implements some missing network APIs including a large chunk of the SSL
service, enough for Mario Maker (with an appropriate mod applied) to connect to
the fan server [Open Course World](https://opencourse.world/).

Connecting to first-party servers is out of scope of this PR and is a
minefield I'd rather not step into.

 ## TLS

TLS is implemented with multiple backends depending on the system's 'native'
TLS library.  Currently there are two backends: Schannel for Windows, and
OpenSSL for Linux.  (In reality Linux is a bit of a free-for-all where there's
no one 'native' library, but OpenSSL is the closest it gets.)  On macOS the
'native' library is SecureTransport but that isn't implemented in this PR.
(Instead, all non-Windows OSes will use OpenSSL unless disabled with
`-DENABLE_OPENSSL=OFF`.)

Why have multiple backends instead of just using a single library, especially
given that Yuzu already embeds mbedtls for cryptographic algorithms?  Well, I
tried implementing this on mbedtls first, but the problem is TLS policies -
mainly trusted certificate policies, and to a lesser extent trusted algorithms,
SSL versions, etc.

...In practice, the chance that someone is going to conduct a man-in-the-middle
attack on a third-party game server is pretty low, but I'm a security nerd so I
like to do the right security things.

My base assumption is that we want to use the host system's TLS policies.  An
alternative would be to more closely emulate the Switch's TLS implementation
(which is based on NSS).  But for one thing, I don't feel like reverse
engineering it.  And I'd argue that for third-party servers such as Open Course
World, it's theoretically preferable to use the system's policies rather than
the Switch's, for two reasons

1. Someday the Switch will stop being updated, and the trusted cert list,
   algorithms, etc. will start to go stale, but users will still want to
   connect to third-party servers, and there's no reason they shouldn't have
   up-to-date security when doing so.  At that point, homebrew users on actual
   hardware may patch the TLS implementation, but for emulators it's simpler to
   just use the host's stack.

2. Also, it's good to respect any custom certificate policies the user may have
   added systemwide.  For example, they may have added custom trusted CAs in
   order to use TLS debugging tools or pass through corporate MitM middleboxes.
   Or they may have removed some CAs that are normally trusted out of paranoia.

Note that this policy wouldn't work as-is for connecting to first-party
servers, because some of them serve certificates based on Nintendo's own CA
rather than a publicly trusted one.  However, this could probably be solved
easily by using appropriate APIs to adding Nintendo's CA as an alternate
trusted cert for Yuzu's connections.  That is not implemented in this PR
because, again, first-party servers are out of scope.

(If anything I'd rather have an option to _block_ connections to Nintendo
servers, but that's not implemented here.)

To use the host's TLS policies, there are three theoretical options:

a) Import the host's trusted certificate list into a cross-platform TLS
   library (presumably mbedtls).

b) Use the native TLS library to verify certificates but use a cross-platform
   TLS library for everything else.

c) Use the native TLS library for everything.

Two problems with option a).  First, importing the trusted certificate list at
minimum requires a bunch of platform-specific code, which mbedtls does not have
built in.  Interestingly, OpenSSL recently gained the ability to import the
Windows certificate trust store... but that leads to the second problem, which
is that a list of trusted certificates is [not expressive
enough](https://bugs.archlinux.org/task/41909) to express a modern certificate
trust policy.  For example, Windows has the concept of [explicitly distrusted
certificates](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn265983(v=ws.11)),
and macOS requires Certificate Transparency validation for some certificates
with complex rules for when it's required.

Option b) (using native library just to verify certs) is probably feasible, but
it would miss aspects of TLS policy other than trusted certs (like allowed
algorithms), and in any case it might well require writing more code, not less,
compared to using the native library for everything.

So I ended up at option c), using the native library for everything.

What I'd *really* prefer would be to use a third-party library that does option
c) for me.  Rust has a good library for this,
[native-tls](https://docs.rs/native-tls/latest/native_tls/).  I did search, but
I couldn't find a good option in the C or C++ ecosystem, at least not any that
wasn't part of some much larger framework.  I was surprised - isn't this a
pretty common use case?  Well, many applications only need TLS for HTTPS, and they can
use libcurl, which has a TLS abstraction layer internally but doesn't expose
it.  Other applications only support a single TLS library, or use one of the
aforementioned larger frameworks, or are platform-specific to begin with, or of
course are written in a non-C/C++ language, most of which have some canonical
choice for TLS.  But there are also many applications that have a set of TLS
backends just like this; it's just that nobody has gone ahead and abstracted
the pattern into a library, at least not a widespread one.

Amusingly, there is one TLS abstraction layer that Yuzu already bundles: the
one in ffmpeg.  But it is missing some features that would be needed to use it
here (like reusing an existing socket rather than managing the socket itself).
Though, that does mean that the wiki's build instructions for Linux (and macOS
for some reason?) already recommend installing OpenSSL, so no need to update
those.

 ## Other APIs implemented

- Sockets:
    - GetSockOpt(`SO_ERROR`)
    - SetSockOpt(`SO_NOSIGPIPE`) (stub, I have no idea what this does on Switch)
    - `DuplicateSocket` (because the SSL sysmodule calls it internally)
    - More `PollEvents` values

- NSD:
    - `Resolve` and `ResolveEx` (stub, good enough for Open Course World and
      probably most third-party servers, but not first-party)

- SFDNSRES:
    - `GetHostByNameRequest` and `GetHostByNameRequestWithOptions`
    - `ResolverSetOptionRequest` (stub)

 ## Fixes

- Parts of the socket code were previously allocating a `sockaddr` object on
  the stack when calling functions that take a `sockaddr*` (e.g. `accept`).
  This might seem like the right thing to do to avoid illegal aliasing, but in
  fact `sockaddr` is not guaranteed to be large enough to hold any particular
  type of address, only the header.  This worked in practice because in
  practice `sockaddr` is the same size as `sockaddr_in`, but it's not how the
  API is meant to be used.  I changed this to allocate an `sockaddr_in` on the
  stack and `reinterpret_cast` it.  I could try to do something cleverer with
  `aligned_storage`, but casting is the idiomatic way to use these particular
  APIs, so it's really the system's responsibility to avoid any aliasing
  issues.

- I rewrote most of the `GetAddrInfoRequest[WithOptions]` implementation.  The
  old implementation invoked the host's getaddrinfo directly from sfdnsres.cpp,
  and directly passed through the host's socket type, protocol, etc. values
  rather than looking up the corresponding constants on the Switch.  To be
  fair, these constants don't tend to actually vary across systems, but
  still... I added a wrapper for `getaddrinfo` in
  `internal_network/network.cpp` similar to the ones for other socket APIs, and
  changed the `GetAddrInfoRequest` implementation to use it.  While I was at
  it, I rewrote the serialization to use the same approach I used to implement
  `GetHostByNameRequest`, because it reduces the number of size calculations.
  While doing so I removed `AF_INET6` support because the Switch doesn't
  support IPv6; it might be nice to support IPv6 anyway, but that would have to
  apply to all of the socket APIs.

  I also corrected the IPC wrappers for `GetAddrInfoRequest` and
  `GetAddrInfoRequestWithOptions` based on reverse engineering and hardware
  testing.  Every call to `GetAddrInfoRequestWithOptions` returns *four*
  different error codes (IPC status, getaddrinfo error code, netdb error code,
  and errno), and `GetAddrInfoRequest` returns three of those but in a
  different order, and it doesn't really matter but the existing implementation
  was a bit off, as I discovered while testing `GetHostByNameRequest`.

  - The new serialization code is based on two simple helper functions:

    ```cpp
    template <typename T> static void Append(std::vector<u8>& vec, T t);
    void AppendNulTerminated(std::vector<u8>& vec, std::string_view str);
    ```

    I was thinking there must be existing functions somewhere that assist with
    serialization/deserialization of binary data, but all I could find was the
    helper methods in `IOFile` and `HLERequestContext`, not anything that could
    be used with a generic byte buffer.  If I'm not missing something, then
    maybe I should move the above functions to a new header in `common`...
    right now they're just sitting in `sfdnsres.cpp` where they're used.

- Not a fix, but `SocketBase::Recv`/`Send` is changed to use `std::span<u8>`
  rather than `std::vector<u8>&` to avoid needing to copy the data to/from a
  vector when those methods are called from the TLS implementation.

---
## [Mu365/Mu365](https://github.com/Mu365/Mu365)@[ce1146a028...](https://github.com/Mu365/Mu365/commit/ce1146a0280a24376ec4a11d8b0da0bb437ed0d6)
#### Tuesday 2023-08-22 07:21:23 by Mu365

Create README.md

# Coronavirus (COVID-19) Information Repository

![Coronavirus](https://github.com/yourusername/coronavirus-repo/raw/main/images/coronavirus_banner.jpg)

Welcome to the Coronavirus (COVID-19) Information Repository. This repository is designed to provide accurate and up-to-date information about the coronavirus pandemic, including its causes, symptoms, preventive measures, and relevant resources. 

## Table of Contents

- [Introduction](#introduction)
- [Understanding COVID-19](#understanding-covid-19)
  - [What is COVID-19?](#what-is-covid-19)
  - [Symptoms](#symptoms)
  - [Transmission](#transmission)
- [Preventive Measures](#preventive-measures)
  - [Personal Hygiene](#personal-hygiene)
  - [Social Distancing](#social-distancing)
  - [Face Masks](#face-masks)
- [Resources](#resources)
  - [Official Health Organizations](#official-health-organizations)
  - [Reliable Information Sources](#reliable-information-sources)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Coronavirus (COVID-19) pandemic is a global health crisis that emerged in late 2019. This repository aims to provide information to help individuals understand the virus, its symptoms, transmission methods, and effective preventive measures.

## Understanding COVID-19

### What is COVID-19?

COVID-19 is a respiratory illness caused by the novel coronavirus SARS-CoV-2. It was first identified in Wuhan, China, and has since spread worldwide. The symptoms range from mild to severe and can include fever, cough, shortness of breath, fatigue, and more.

### Symptoms

Common symptoms of COVID-19 include:

- Fever
- Cough
- Shortness of breath or difficulty breathing
- Fatigue
- Muscle or body aches
- Loss of taste or smell
- Sore throat
- Headache
- Chills
- Congestion or runny nose
- Nausea or vomiting
- Diarrhea

### Transmission

COVID-19 primarily spreads through respiratory droplets produced when an infected person coughs, sneezes, talks, or breathes. It can also spread by touching a surface or object that has the virus on it and then touching the mouth, nose, or eyes.

## Preventive Measures

To reduce the spread of COVID-19, it's important to follow preventive measures.

### Personal Hygiene

- Wash hands frequently with soap and water for at least 20 seconds.
- Use hand sanitizer with at least 60% alcohol if soap is not available.
- Avoid touching your face, especially your eyes, nose, and mouth.

### Social Distancing

- Maintain a distance of at least 6 feet from others.
- Avoid large gatherings and crowded places.
- Stay home if you're feeling unwell or have been in contact with a confirmed case.

### Face Masks

- Wear a mask in public settings, especially when social distancing is not possible.
- Masks help prevent the spread of respiratory droplets that may contain the virus.

## Resources

### Official Health Organizations

- [World Health Organization (WHO)](https://www.who.int/)
- [Centers for Disease Control and Prevention (CDC)](https://www.cdc.gov/)

### Reliable Information Sources

- [COVID-19 Mythbusters - WHO](https://www.who.int/emergencies/disease-outbreak-news/item/2020-DON264)
- [COVID-19 Dashboard - Johns Hopkins University](https://coronavirus.jhu.edu/map.html)
- [COVID-19 Health Information - Mayo Clinic](https://www.mayoclinic.org/coronavirus-covid-19)

## Contributing

Contributions to this repository are welcome. If you have accurate and relevant information to add or update, feel free to create a pull request. For major changes, please open an issue to discuss before proceeding.

## License

This repository and its contents are licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/). You are free to share and adapt the material for any purpose, even commercially. Please provide appropriate attribution to the original authors.

---

**Note:** This repository is for informational purposes only and does not replace professional medical advice. Always consult with healthcare professionals for medical guidance and treatment.

---
## [jyotiram7402/Search--Application-using-RedirectView-Using_Spring_MVC](https://github.com/jyotiram7402/Search--Application-using-RedirectView-Using_Spring_MVC)@[c21cf104fc...](https://github.com/jyotiram7402/Search--Application-using-RedirectView-Using_Spring_MVC/commit/c21cf104fc7a59c44a1401d1fc7d627e106db465)
#### Tuesday 2023-08-22 07:57:41 by Jyotiram Kamble

Add files via upload

"Search Application using RedirectView with Spring"

Welcome to our Search Application built using the powerful Spring framework! This application showcases the seamless integration of Spring's RedirectView to create an efficient and user-friendly search experience.

🔍 **Key Features:**
- **Search Functionality:** Easily search through our database with a robust search functionality powered by Spring.
- **RedirectView Integration:** We leverage Spring's RedirectView to enhance user experience by efficiently redirecting search queries.
- **Clean and Structured Code:** Our codebase follows best practices, ensuring maintainability and scalability.

🚀 **Getting Started:**
1. **Clone the Repository:** Begin by cloning this repository to your local machine.
2. **Configure Dependencies:** Make sure you have the required dependencies configured in your Spring project.
3. **Database Setup:** Set up your database and configure the data source properties in the Spring configuration.
4. **Build and Run:** Compile and run the application using your preferred IDE or the command line.
5. **Access the App:** Open your browser and access the application. Use the search bar to experience the RedirectView in action!

📁 **Project Structure:**
- `src/main/java`: Contains the Java source code files.
  - `springmvcsearch`: Main application package.
    - `controller`: Houses the controllers for handling search functionality and redirection.
    - `service`: Implements the business logic and search algorithms.
    - `model`: Defines the data models used in the application.
- `src/main/resources`: Contains configuration files and resources.
  - `application.properties`: Configure database properties and Spring settings.
  - `templates`: Contains HTML templates for rendering the search UI.

📝 **Usage:**
1. Enter your search query in the search bar.
2. Click the search button or press Enter.
3. Our application will use RedirectView to process your query efficiently and display the relevant search results.

🌟 **Contributing:**
We welcome contributions from the open-source community! If you'd like to add features, fix bugs, or improve documentation, feel free to submit pull requests.

📞 **Contact Us:**
Have questions or feedback? Reach out to our team at jyotiramkamble7402@gmail.com

Thank you for exploring our Search Application built with RedirectView and Spring. Happy searching! 🎉

---
## [toolan365/semantic-kernel](https://github.com/toolan365/semantic-kernel)@[2733a5574f...](https://github.com/toolan365/semantic-kernel/commit/2733a5574f72980413e339f100dbe4272644888c)
#### Tuesday 2023-08-22 08:08:22 by Mark Karle

Python: Import OpenAPI documents into the semantic kernel (#2297)

### Motivation and Context

<!-- Thank you for your contribution to the semantic-kernel repo!
Please help reviewers and future users, providing the following
information:
  1. Why is this change required?
  2. What problem does it solve?
  3. What scenario does it contribute to?
  4. If it fixes an open issue, please link to the issue here.
-->

This allows us to import OpenAPI documents, including ChatGPT plugins,
into the Semantic Kernel.

### Description

<!-- Describe your changes, the overall approach, the underlying design.
These notes will help understanding how your code works. Thanks! -->
- The interface reads the operationIds of the openapi spec into a skill:
```python
from semantic_kernel.connectors.openapi import register_openapi_skill
skill = register_openapi_skill(kernel=kernel, skill_name="test", openapi_document="url/or/path/to/openapi.yamlorjson")
skill['operationId'].invoke_async()
```
- Parse an OpenAPI document
- For each operation in the document, create a function that will
execute the operation
- Add all those operations to a skill in the kernel
- Modified `import_skill` to accept a dictionary of functions instead of
just class so that we can import dynamically created functions
- Created unit tests

TESTING:
I've been testing this with the following ChatGPT plugins:
- [Semantic Kernel Starter's Python Flask
plugin](https://github.com/microsoft/semantic-kernel-starters/tree/main/sk-python-flask)
- [ChatGPT's example retrieval
plugin](https://github.com/openai/chatgpt-retrieval-plugin/blob/main/docs/providers/azuresearch/setup.md)
- This one was annoying to setup. I didn't get the plugin functioning,
but I was able to send the right API requests
- Also, their openapi file was invalid. The "servers" attribute is
misindented
- [Google ChatGPT
plugin](https://github.com/Sogody/google-chatgpt-plugin)
- [Chat TODO plugin](https://github.com/lencx/chat-todo-plugin)
- This openapi file is also invalid. I checked with an online validator.
I had to remove"required" from the referenced request objects'
properties:
https://github.com/lencx/chat-todo-plugin/blob/main/openapi.yaml#L85

Then I used this python file to test the examples:

```python
import asyncio
import logging

import semantic_kernel as sk
from semantic_kernel import ContextVariables, Kernel
from semantic_kernel.connectors.ai.open_ai import AzureTextCompletion
from semantic_kernel.connectors.openapi.sk_openapi import register_openapi_skill

# Example usage
chatgpt_retrieval_plugin = {
    "openapi": # location of the plugin's openapi.yaml file,
    "payload": {
        "queries": [
            {
                "query": "string",
                "filter": {
                    "document_id": "string",
                    "source": "email",
                    "source_id": "string",
                    "author": "string",
                    "start_date": "string",
                    "end_date": "string",
                },
                "top_k": 3,
            }
        ]
    },
    "operation_id": "query_query_post",
}

sk_python_flask = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "path_params": {"skill_name": "FunSkill", "function_name": "Joke"},
    "payload": {"input": "dinosaurs"},
    "operation_id": "executeFunction",
}
google_chatgpt_plugin = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "query_params": {"q": "dinosaurs"},
    "operation_id": "searchGet",
}

todo_plugin_add = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "path_params": {"username": "markkarle"},
    "payload": {"todo": "finish this"},
    "operation_id": "addTodo",
}

todo_plugin_get = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "path_params": {"username": "markkarle"},
    "operation_id": "getTodos",
}

todo_plugin_delete = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "path_params": {"username": "markkarle"},
    "payload": {"todo_idx": 0},
    "operation_id": "deleteTodo",
}


plugin = todo_plugin_get # set this to the plugin you want to try

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

kernel = Kernel(log=logger)
deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()
kernel.add_text_completion_service(
    "dv", AzureTextCompletion(deployment, endpoint, api_key)
)

skill = register_openapi_skill(
    kernel=kernel, skill_name="test", openapi_document=plugin["openapi"]
)
context_variables = ContextVariables(variables=plugin)
result = asyncio.run(
    skill[plugin["operation_id"]].invoke_async(variables=context_variables)
)
print(result)
```

### Contribution Checklist

<!-- Before submitting this PR, please make sure: -->

- [ ] The code builds clean without any errors or warnings
- [ ] The PR follows the [SK Contribution
Guidelines](https://github.com/microsoft/semantic-kernel/blob/main/CONTRIBUTING.md)
and the [pre-submission formatting
script](https://github.com/microsoft/semantic-kernel/blob/main/CONTRIBUTING.md#development-scripts)
raises no violations
- [ ] All unit tests pass, and I have added new tests where possible
- [ ] I didn't break anyone :smile:

---------

Co-authored-by: Abby Harrison <abharris@microsoft.com>

---
## [vizabi/shared-components](https://github.com/vizabi/shared-components)@[8ca4528b14...](https://github.com/vizabi/shared-components/commit/8ca4528b148d6adf75b38025ff1b66d39a63d4e4)
#### Tuesday 2023-08-22 09:01:14 by angie

Slice section: dirty midnight refactoring to support setting label DS...

This allows labels to request names for every entity, such as Male, Female. If we don't update the datasource of label enc, the new dimensions may be missing from the old data source and it will not be able to resolve their names and return just 0 and 1 for genders

---
## [vdaular-dev/linksfordevs](https://github.com/vdaular-dev/linksfordevs)@[783629a9c3...](https://github.com/vdaular-dev/linksfordevs/commit/783629a9c3346e676802aaa3a8e9f7edeb8f8ec8)
#### Tuesday 2023-08-22 09:28:15 by Ben Dornis

Updating: 8/21/2023 9:00:00 PM

 1. Added: Backing Up Personal Files with rclone
    (https://vineeth.io/posts/2023/rclone-backups/)
 2. Added: Reliable communication allows for simpler interfaces - Max's Notes
    (https://notes.max.engineer/reliable-communication-allows-for-simpler-interfaces)
 3. Added: Metaphors for thinking about LLMs
    (https://vivekhaldar.com/articles/metaphors-for-thinking-about-llms/)
 4. Added: The Future of Data Engineering in the Warehouse
    (https://chrisreuter.me/2023-08-21-future-of-data-engineering/)
 5. Added: A Process for Building LLM Classifiers
    (https://blog.kasperjunge.com/a-process-for-building-llm-classifiers)
 6. Added: Listen to non-users!
    (https://kodare.net/2023/08/21/listen-to-non-users.html)
 7. Added: JSON Sort CLI and Pre-Commit Hook
    (https://www.paraesthesia.com/archive/2023/08/21/json-sort-cli-pre-commit/)
 8. Added: The Broad Set of Computer Science Problems Faced at Cloud Database Companies
    (https://davidgomes.com/the-broad-set-of-computer-science-problems-faced-at-cloud-database-companies/)
 9. Added: Don't Fire Your Illustrator
    (https://sambleckley.com/writing/dont-fire-your-illustrator.html)
10. Added: The Problem with Friendly C – Embedded in Academia
    (https://blog.regehr.org/archives/1287)
11. Added: Storing passkeys in password managers is okay, actually
    (https://cendyne.dev/posts/2023-08-21-passkeys-in-password-managers-is-okay.html)
12. Added: Brenton Cleeland - Website Best Practices
    (https://brntn.me/blog/website-best-practices/)
13. Added: DIY Deliberate Practice  — Lynette Bye Coaching
    (https://lynettebye.com/blog/2023/7/27/diy-deliberate-practice)
14. Added: We don't need to "degrow" the economy
    (https://www.elysian.press/p/we-dont-need-degrowth-for-the-environment)
15. Added: Declarative package management with a Brewfile
    (https://matthiasportzel.com/brewfile/)
16. Added: Why LFI is a tough sell
    (https://surfingcomplexity.blog/2023/08/20/why-lfi-is-a-tough-sell/)
17. Added: Algolia + NextJS for Ecommerce
    (https://www.avikaminetzky.dev/posts/algolia-ecommerce-nextjs)
18. Added: E-ink is so Retropunk
    (https://rmkit.dev/eink-is-so-retropunk/)
19. Added: What’s a Website
    (https://joe-ferrara.github.io/2023/08/20/whats-a-website.html)
20. Added: Concise explanations accelerate progress
    (https://stephanango.com/concise)
21. Added: The Ugly Truth About Sleep
    (https://www.okdoomer.io/the-ugly-truth-about-sleep/)
22. Added: Enjoying the Internet again with the Fediverse and IndieWeb
    (https://blog.kovah.de/en/2023/enjoying-internet-again-with-fediverse-indieweb/)

Generation took: 00:08:36.5061520
 Maintenance update - cleaning up homepage and feed

---
## [argilla-io/argilla](https://github.com/argilla-io/argilla)@[028416a56e...](https://github.com/argilla-io/argilla/commit/028416a56e1eb05defe9dffcd03de5d1744bdcf2)
#### Tuesday 2023-08-22 10:04:40 by Natalia Elvira

Docs/feedback setfit tutorial (#3530)

<!-- Thanks for your contribution! As part of our Community Growers
initiative 🌱, we're donating Justdiggit bunds in your name to reforest
sub-Saharan Africa. To claim your Community Growers certificate, please
contact David Berenstein in our Slack community or fill in this form
https://tally.so/r/n9XrxK once your PR has been merged. -->

# Description

Adds a new tutorial on how to use SetFit to get zero-shot suggestions
for `Label` and `MultiLabel` questions in Feedback datasets.

Closes #3528 

**Type of change**

(Remember to title the PR according to the type of change)

- [x] Documentation update

**How Has This Been Tested**

(Please describe the tests that you ran to verify your changes.)

- [x] `sphinx-autobuild` (read [Developer
Documentation](https://docs.argilla.io/en/latest/community/developer_docs.html#building-the-documentation)
for more details)

**Checklist**

- [ ] I added relevant documentation
- [x] I followed the style guidelines of this project
- [x] I did a self-review of my code
- [x] I made corresponding changes to the documentation
- [x] My changes generate no new warnings
- [ ] I filled out [the contributor form](https://tally.so/r/n9XrxK)
(see text above)
- [ ] I have added relevant notes to the `CHANGELOG.md` file (See
https://keepachangelog.com/)

---
## [mietek/mame](https://github.com/mietek/mame)@[e97630981c...](https://github.com/mietek/mame/commit/e97630981c406ba446e2d7fb1bf8ecf8d3a6b93b)
#### Tuesday 2023-08-22 10:06:16 by A-Noid33

Added software list for cracked Macintosh floppy images. (#11454)

New working software list items (mac_flop_orig.xml)
-------------------------------
Alter Ego (male version 1.0) (san inc crack) [4am, san inc, A-Noid]
Alter Ego (version 1.1 female) (san inc crack) [4am, san inc, A-Noid]
Alternate Reality: The City (version 3.0) (san inc crack) [4am, san inc, A-Noid]
Animation Toolkit I: The Players (version 1.0) (4am crack) [4am, A-Noid]
Balance of Power (version 1.03) (san inc crack) [4am, san inc, A-Noid]
Borrowed Time (san inc crack) [4am, san inc, A-Noid]
Championship Star League Baseball (san inc crack) [4am, san inc, A-Noid]
Cutthroats (release 23 / 840809-C) (4am crack) [4am, A-Noid]
CX Base 500 (French, version 1.1) (san inc crack) [4am, san inc, A-Noid]
Deadline (release 27 / 831005-C) (4am crack) [4am, A-Noid]
Defender of the Crown (san inc crack) [4am, san inc, A-Noid]
Deluxe Music Construction Set (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Déjà Vu (version 2.3) (4am crack) [4am, A-Noid]
Déjà Vu: A Nightmare Comes True!! (san inc crack) [4am, san inc, A-Noid]
Déjà Vu II: Lost in Las Vegas!! (san inc crack) [4am, san inc, A-Noid]
Dollars and Sense (version 1.3) (4am crack) [4am, A-Noid]
Downhill Racer (san inc crack) [4am, san inc, A-Noid]
Dragonworld (4am crack) [4am, A-Noid]
ExperLisp (version 1.0) (4am crack) [4am, A-Noid]
Forbidden Castle (san inc crack) [4am, san inc, A-Noid]
Fusillade (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Geometry (version 1.1) (4am crack) [4am, A-Noid]
Habadex (version 1.1) (4am crack) [4am, A-Noid]
Hacker II (san inc crack) [4am, san inc, A-Noid]
Harrier Strike Mission (san inc crack) [4am, san inc, A-Noid]
Indiana Jones and the Revenge of the Ancients (san inc crack) [4am, san inc, A-Noid]
Infidel (release 22 / 840522-C) (4am crack) [4am, A-Noid]
Jam Session (version 1.0) (4am crack) [4am, A-Noid]
Legends of the Lost Realm I: The Gathering of Heroes (version 2.0) (4am crack) [4am, A-Noid]
Lode Runner (version 1.0) (4am crack) [4am, A-Noid]
Mac Pro Football (version 1.0) (san inc crack) [4am, san inc, A-Noid]
MacBackup (version 2.6) (4am crack) [4am, A-Noid]
MacCheckers and Reversi (4am crack) [4am, A-Noid]
MacCopy (version 1.1) (4am crack) [4am, A-Noid]
MacGammon! (version 1.0) (4am crack) [4am, A-Noid]
MacGolf (version 2.0) (4am crack) [4am, A-Noid]
MacWars (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 1.10) (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 2.00h) (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 3.4a) (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 4.0) (san inc crack) [4am, san inc, A-Noid]
Math Blaster (version 1.0) (4am crack) [4am, A-Noid]
Maze Survival (san inc crack) [4am, san inc, A-Noid]
Microsoft Excel (version 1.00) (san inc crack) [4am, san inc, A-Noid]
Microsoft File (version 1.04) (san inc crack) [4am, san inc, A-Noid]
Mindshadow (san inc crack) [4am, san inc, A-Noid]
Moriarty's Revenge (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Moriarty's Revenge (version 1.03) (4am crack) [4am, A-Noid]
Mouse Stampede (version 1.00) (4am crack) [4am, A-Noid]
Murder by the Dozen (Thunder Mountain) (4am crack) [4am, A-Noid]
My Office (version 2.7) (4am crack) [4am, A-Noid]
One on One (san inc crack) [4am, san inc, A-Noid]
Orb Quest: Part I: The Search for Seven Wards (version 1.04) (san inc crack) [4am, san inc, A-Noid]
Patton Strikes Back (version 1.00) (san inc crack) [4am, san inc, A-Noid]
Patton vs. Rommel (version 1.05) (san inc crack) [4am, san inc, A-Noid]
Pensate (version 1.1) (4am crack) [4am, A-Noid]
PFS File and Report (version A.00) (4am crack) [4am, A-Noid]
Physics (version 1.0) (4am crack) [4am, A-Noid]
Physics (version 1.2) (4am crack) [4am, A-Noid]
Pinball Construction Set (version 2.5) (san inc crack) [4am, san inc, A-Noid]
Pipe Dream (version 1.2) (4am crack) [4am, A-Noid]
Professional Composer (version 2.3Mfx) (san inc crack) [4am, san inc, A-Noid]
Q-Sheet (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Rambo: First Blood Part II (san inc crack) [4am, san inc, A-Noid]
Reader Rabbit (version 2.0) (4am crack) [4am, A-Noid]
Rogue (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Seastalker (release 15 / 840522-C) (4am crack) [4am, A-Noid]
Seven Cities of Gold (san inc crack) [4am, san inc, A-Noid]
Shadowgate (san inc crack) [4am, san inc, A-Noid]
Shanghai (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Shufflepuck Cafe (version 1.0) (4am crack) [4am, A-Noid]
Sierra Championship Boxing (4am crack) [4am, A-Noid]
SimCity (version 1.1) (4am crack) [4am, A-Noid]
SimCity (version 1.2, black & white) (4am crack) [4am, A-Noid]
SimEarth (version 1.0) (4am crack) [4am, A-Noid]
Skyfox (san inc crack) [4am, san inc, A-Noid]
Smash Hit Racquetball (version 1.01) (san inc crack) [4am, san inc, A-Noid]
SmoothTalker (version 1.0) (4am crack) [4am, A-Noid]
Speed Reader II (version 1.1) (4am crack) [4am, A-Noid]
Speller Bee (version 1.1) (4am crack) [4am, A-Noid]
Star Trek: The Kobayashi Alternative (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Stratego (version 1.0) (4am crack) [4am, A-Noid]
Suspect (release 14 / 841005-C) (4am crack) [4am, A-Noid]
Tass Times in Tonetown (san inc crack) [4am, san inc, A-Noid]
Temple of Apshai Trilogy (version 1985-09-30) (san inc crack) [4am, san inc, A-Noid]
Temple of Apshai Trilogy (version 1985-10-08) (san inc crack) [4am, san inc, A-Noid]
The Chessmaster 2000 (version 1.02) (4am crack) [4am, A-Noid]
The Crimson Crown (san inc crack) [4am, san inc, A-Noid]
The Duel: Test Drive II (san inc crack) [4am, san inc, A-Noid]
The Hitchhiker's Guide to the Galaxy (release 47 / 840914-C) (4am crack) [4am, A-Noid]
The King of Chicago (san inc crack) [4am, san inc, A-Noid]
The Lüscher Profile (san inc crack) [4am, san inc, A-Noid]
The Mind Prober (version 1.0) (san inc crack) [4am, san inc, A-Noid]
The Mist (san inc crack) [4am, san inc, A-Noid]
The Quest (4am crack) [4am, A-Noid]
The Slide Show Magician (version 1.2) (4am crack) [4am, A-Noid]
The Surgeon (version 1.5) (san inc crack) [4am, san inc, A-Noid]
The Toy Shop (version 1.1) (san inc crack) [4am, san inc, A-Noid]
The Witness (release 22 / 840924-C) (4am crack) [4am, A-Noid]
ThinkTank 128 (version 1.000) (4am crack) [4am, A-Noid]
Uninvited (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Uninvited (version 2.1D1) (san inc crack) [4am, san inc, A-Noid]
Where in Europe is Carmen Sandiego? (version 1.0) (4am crack) [4am, A-Noid]
Winter Games (version 1985-10-24) (san inc crack) [4am, san inc, A-Noid]
Winter Games (version 1985-10-31) (san inc crack) [4am, san inc, A-Noid]
Wishbringer (release 68 / 850501-D) (4am crack) [4am, A-Noid]
Wizardry: Proving Grounds of the Mad Overlord (version 1.10) (san inc crack) [4am, san inc, A-Noid]
Zork II (release 48 / 840904-C) (4am crack) [4am, A-Noid]
Zork III (release 17 / 840727-C) (4am crack) [4am, A-Noid]

---
## [vmware-tanzu/kubeapps](https://github.com/vmware-tanzu/kubeapps)@[4e5ac7a243...](https://github.com/vmware-tanzu/kubeapps/commit/4e5ac7a24310d30a0ab539560373cab1106277cd)
#### Tuesday 2023-08-22 10:20:16 by Antonio Gámez, PhD

Use finalizers to spin up AppRepo clean-up jobs (#6647)

### Description of the change

Even if the sync jobs were added a security context (by means of each
AppRepo CRD), this information was not available for Cleanup jobs. This
is mainly due to the fact that those jobs are spun up once a NotFound
error is thrown when fetching an AppRepo.
However, Kubernetes does have a native approach for dealing with these
scenarios: finalizers.

In https://github.com/vmware-tanzu/kubeapps/pull/6605 we proposed a
simplistic workaround based on adding more params to the controller...
but as suggested in
https://github.com/vmware-tanzu/kubeapps/pull/6605#issuecomment-1678268807,
moving to finalizers is a better long-term solution.


### Benefits

Cleanup jobs are now handled within an existing AppRepo context...
meaning we have all the syncJobTemplate available to be used (ie,
securityPolicies and so on).

### Possible drawbacks

When dealing with finalizers in the past I often found it really
annoying when they get stuck and prevent the resource to get deleted. I
wonder if we should add some info in the FAQ on how to manually remove
the finalizers.

Additionally, and this might be something important: for the AppRepo
controller to be able to `update` AppRepos in other namespaces !=
kubeapps.... (to add the finalizer) it now needs extra RBAC. Before we
were just granting `...-appprepos-read`.. but now we would need to grant
`...-write` as well...and I'm not sure we really want to do so.
WDYT, @absoludity ?
Another idea is using an admission policy... but not sure again if we
want to deal with that...

~(I haven't modified the RBAC yet in this PR)~ Changes have been
performed finally

### Applicable issues

- fixes #6545

### Additional information

This PR is based on top of
https://github.com/vmware-tanzu/kubeapps/pull/6646, but the main change
to review is
https://github.com/vmware-tanzu/kubeapps/commit/6e7091015f9a6c3a289224d05dab5f60736489a0
The rest is just moving code into separate files, mostly.

Also, I have been taking a look at `kubebuilder` to create a new
controller, based on the `sigs.k8s.io/controller-runtime` rather than on
the workqueues we currently have. While it is pretty easy to start with
([see quickstart](https://book.kubebuilder.io/quick-start)), I think it
is adding too much complexity (using kustomize, adding rbac proxies,
prometheus metrics, etc...
I also quickly tried the k8s codegen scripts, but ran into some issues
with my setup... but perhaps it's the best option.

IMO, at some point we should start thinking about moving towards a new
state-of-the-art k8s controller boilerplate.

---------

Signed-off-by: Antonio Gamez Diaz <agamez@vmware.com>

---
## [zaid-rana/Ecommerce-Website](https://github.com/zaid-rana/Ecommerce-Website)@[be01b4dcdb...](https://github.com/zaid-rana/Ecommerce-Website/commit/be01b4dcdbcc9c3296610f9d2449366e9d936a0a)
#### Tuesday 2023-08-22 10:33:47 by zaid-rana

Add files via upload

"Fleets" - Your Ultimate Footwear Destination

Welcome to "Fleets," your go-to destination for all things footwear! Our meticulously crafted e-commerce website is designed to cater to every shoe enthusiast's desires and needs. With an extensive collection of shoes that range from trendy sneakers to elegant formal wear, Fleets is your one-stop shop for all your footwear cravings.

**Discover Our Vast Selection**

At Fleets, we understand that shoes aren't just an accessory; they're an expression of your personality and style. That's why we offer an extensive range of footwear options. Whether you're searching for the perfect pair of running shoes to conquer your fitness goals, stylish heels to elevate your evening attire, or comfortable everyday sneakers, our curated selection has you covered.

**Quality Meets Style**

We are committed to offering the best quality footwear to our customers. Every shoe in our inventory is handpicked for its durability, comfort, and, of course, style. Our partnerships with renowned brands and artisan shoemakers ensure that you get nothing but the finest shoes available on the market.

**User-Friendly Shopping Experience**

Shopping at Fleets is a breeze. Our user-friendly website is designed with you in mind. You can easily browse our collection, filter products by size, color, or style, and read detailed product descriptions and reviews to make informed decisions. We also offer secure payment options to ensure a hassle-free shopping experience.

**Stay on Trend**

Fashion evolves, and so does Fleets. Our team of fashion experts keeps a keen eye on the latest footwear trends, ensuring that our collection is always up to date. You can trust us to provide you with the most fashionable and stylish footwear options that are in vogue.

**Exceptional Customer Service**

At Fleets, we value our customers above all else. Our dedicated customer support team is here to assist you with any questions or concerns you may have. We strive to provide exceptional service and ensure that your shopping experience with us is nothing short of fantastic.

**Stay Connected**

Don't miss out on our exciting promotions, discounts, and exclusive offers. Subscribe to our newsletter and follow us on social media to stay updated on the latest arrivals and special deals.

Join us at Fleets and step into a world of footwear that combines quality, style, and convenience. Whether you're shopping for yourself or searching for the perfect gift, Fleets has something for everyone. Elevate your shoe game today with Fleets - Where Fashion Meets Feet!

---
## [EldarFara/BetweenEmpires](https://github.com/EldarFara/BetweenEmpires)@[0ddc954d3d...](https://github.com/EldarFara/BetweenEmpires/commit/0ddc954d3df16d9b455928c3785bc99d39b935ac)
#### Tuesday 2023-08-22 10:34:58 by LeutnantZaki

Changes

xml export code

Export to XML

bulgaria and zimbabwe

kys

Revert "Game initialization"

This reverts commit 124879fbb393507fcd759c1a4eeb02a8ca19790d.

Game initialization

whoops

This doesnt work lol

country parameters per starting date

province201 core fix

Faction parameters at start date example

removed dupes

ye

flag and color tweak

1936 parameters and stuff

yes

1919 start date

malo aires

some stuff AAAAA

anhalt core1 fix and other stuff

funni gambia + funni sierra leone oversight error

few stuffs (i'm stuff)

1910 start date params

1877 start date params

1877 #2

1877 #1

few things

literally 1861

two kirovs

1936 #2

1936 #1

guangxi provinces

core1 params fix for zimbabwe and south africa

warlord states

sum fix + ukrayni

eic only eic, raj will be part of faction_britain

1877-1919 except rus civil war

some 1877 and 1910 stuff (uncompiled)

+

EU starts #2

Fixed bugs

EU starts

dixie

start 1861

Population bug fix

core1 params done

I’ll be back Svinoti (no)

few additions before i sleep

yes why not (cores)

New population initialization system

dutch east indies additions

few tweaks

few tweaks

kerguelen

terrain types done ez

s. ameriKKKan taiga to tundra

s. ameriKKKa dome

north s. ameriKKKa

ameriKKKa central

qilai

new terrain types and cores

arab, mongolia, northern china, korea, afghanistan and pakistan

i love nihari at 12 am

khamenei's mountains

ameriKKKa terrain types

provice321-province400 terrain types

europe + russia terrain types

armenia core on west armenia (parts of east turk)

rip balts

another fix for balts

фиксик

prussia

need new factions based on the cores

Divided scripts into smaller ones

formable countries pt. 1

yes

suomen

fix for paraguay

transportation cost  calculation

japanis cores

pls add nations flag and color

more cores

baltics gov type fix

"few" cores

georgia flag tweakin

ukraine, crimea and kazakh

stan countries

eternal conflict countries

nord flags

ameriKKKa

ameriKKKan flags be trollin

Iran and Transjordan cores

petrodollar monarchies

flags and tweaks

wooow more cores

canada fix and few flags

yeee

bruuh

cores and trold amount of flags lolololol

trold cores

few ethiopian stuff

trold

rookie mistake

islands n retard

flags and stuff

zanzibar + bing chilling warlord + the rock

it exceeds 300 lool

bing chilling

more cores

leopold the second's wet dream

cores done

flags

Copium incoming

fixed some

few stuff

nipah what? nipah virus

vlach

turk

core changes

saparmurat

province700 core fix

ulus mongol

few core stuff

---
## [sjp38/linux](https://github.com/sjp38/linux)@[8b9c1cc041...](https://github.com/sjp38/linux/commit/8b9c1cc0418a43196477083e7082568e7a4c9418)
#### Tuesday 2023-08-22 10:53:04 by David Hildenbrand

smaps: use vm_normal_page_pmd() instead of follow_trans_huge_pmd()

We shouldn't be using a GUP-internal helper if it can be avoided.

Similar to smaps_pte_entry() that uses vm_normal_page(), let's use
vm_normal_page_pmd() that similarly refuses to return the huge zeropage.

In contrast to follow_trans_huge_pmd(), vm_normal_page_pmd():

(1) Will always return the head page, not a tail page of a THP.

 If we'd ever call smaps_account with a tail page while setting "compound
 = true", we could be in trouble, because smaps_account() would look at
 the memmap of unrelated pages.

 If we're unlucky, that memmap does not exist at all. Before we removed
 PG_doublemap, we could have triggered something similar as in
 commit 24d7275ce279 ("fs/proc: task_mmu.c: don't read mapcount for
 migration entry").

 This can theoretically happen ever since commit ff9f47f6f00c ("mm: proc:
 smaps_rollup: do not stall write attempts on mmap_lock"):

  (a) We're in show_smaps_rollup() and processed a VMA
  (b) We release the mmap lock in show_smaps_rollup() because it is
      contended
  (c) We merged that VMA with another VMA
  (d) We collapsed a THP in that merged VMA at that position

 If the end address of the original VMA falls into the middle of a THP
 area, we would call smap_gather_stats() with a start address that falls
 into a PMD-mapped THP. It's probably very rare to trigger when not
 really forced.

(2) Will succeed on a is_pci_p2pdma_page(), like vm_normal_page()

 Treat such PMDs here just like smaps_pte_entry() would treat such PTEs.
 If such pages would be anonymous, we most certainly would want to
 account them.

(3) Will skip over pmd_devmap(), like vm_normal_page() for pte_devmap()

 As noted in vm_normal_page(), that is only for handling legacy ZONE_DEVICE
 pages. So just like smaps_pte_entry(), we'll now also ignore such PMD
 entries.

 Especially, follow_pmd_mask() never ends up calling
 follow_trans_huge_pmd() on pmd_devmap(). Instead it calls
 follow_devmap_pmd() -- which will fail if neither FOLL_GET nor FOLL_PIN
 is set.

 So skipping pmd_devmap() pages seems to be the right thing to do.

(4) Will properly handle VM_MIXEDMAP/VM_PFNMAP, like vm_normal_page()

 We won't be returning a memmap that should be ignored by core-mm, or
 worse, a memmap that does not even exist. Note that while
 walk_page_range() will skip VM_PFNMAP mappings, walk_page_vma() won't.

 Most probably this case doesn't currently really happen on the PMD level,
 otherwise we'd already be able to trigger kernel crashes when reading
 smaps / smaps_rollup.

So most probably only (1) is relevant in practice as of now, but could only
cause trouble in extreme corner cases.

Let's move follow_trans_huge_pmd() to mm/internal.h to discourage future
reuse in wrong context.

Link: https://lkml.kernel.org/r/20230803143208.383663-3-david@redhat.com
Fixes: ff9f47f6f00c ("mm: proc: smaps_rollup: do not stall write attempts on mmap_lock")
Signed-off-by: David Hildenbrand <david@redhat.com>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hugh Dickins <hughd@google.com>
Cc: Jason Gunthorpe <jgg@ziepe.ca>
Cc: John Hubbard <jhubbard@nvidia.com>
Cc: Linus Torvalds <torvalds@linux-foundation.org>
Cc: liubo <liubo254@huawei.com>
Cc: Matthew Wilcox (Oracle) <willy@infradead.org>
Cc: Mel Gorman <mgorman@suse.de>
Cc: Paolo Bonzini <pbonzini@redhat.com>
Cc: Peter Xu <peterx@redhat.com>
Cc: Shuah Khan <shuah@kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---
## [Kubisopplay/tgstation](https://github.com/Kubisopplay/tgstation)@[ebbc45b161...](https://github.com/Kubisopplay/tgstation/commit/ebbc45b1616c08d2dc0b6e6ce48258f68eefd46a)
#### Tuesday 2023-08-22 12:17:14 by distributivgesetz

Improved PDA Direct Messenger (#75820)

## About The Pull Request

Fixes #76708, Closes #76729 (sorry Zephyr)

This PR expands the Direct Messenger UI, adding a chat screen for each
available messenger that you can find, and moving message sending over
to TGUI.

This chat screen includes a message log that displays messages sent by
you as well as messages received from the recipient. This gets rid of
the previous chat log, which just had all messages thrown together that
you received or have sent, in one big list.

Furthermore, all messaging is now done inside the UI. This kills all
TGUI popups you would ever need to send messages forever (except for
quick replies). Use the input bar on the bottom, press Enter or the Send
button, and it sends your message. Spam mode is now done in the UI too,
via a text field you can find in the contacts list.

Additionally, because I have a habit of blowing things massively out of
scope, I've also completely refactored how messages and chat logs are
stored in the PDA messenger. I plan on using this in a PR that merges
the chat client with the messenger, sometime in the future. Sorry this
took so long.

Stuff left to do before I open this PR for review:
- [x] Add "recent messages"
- [x] Add "unread messages"
- [x] Add message drafts
- [x] Make photo sending not shit
- [x] Implement the edge cases for automated and rigged messages
- [x] Make sure shit isn't fucked
- [x] Profit

<details>
  <summary>Screenshots</summary>
  

![dreamseeker_HIrEfrap5X](https://github.com/tgstation/tgstation/assets/47710522/97c713b7-dda3-44d3-a8f5-d0ec11c92668)

![qIOWhVld4l](https://github.com/tgstation/tgstation/assets/47710522/3ab4e2c1-a38f-4b20-8e9f-509ea14c0434)

![dreamseeker_LIqwi05i4O](https://github.com/tgstation/tgstation/assets/47710522/c051c791-b595-4166-a4d3-82cb7568411f)

![BIYxNVjGL7](https://github.com/tgstation/tgstation/assets/47710522/b9c97eab-52b5-449f-b00f-a0d8aa5f865c)

![dreamseeker_IWdoSsUinC](https://github.com/tgstation/tgstation/assets/47710522/2a4cd76a-2bdc-4283-b642-09e92476fef5)

![L9DxzFHDEF](https://github.com/tgstation/tgstation/assets/47710522/6a5b0e29-d535-4c7e-a88e-e9b71198719b)

![rAuDgqBLNE](https://github.com/tgstation/tgstation/assets/47710522/128a0291-91da-4f9e-9bc5-a65cf411ea6d)

![dreamseeker_voui6S8MUf](https://github.com/tgstation/tgstation/assets/47710522/6e3ba044-b8df-492d-b58d-6c73ab07233d)

![image](https://github.com/tgstation/tgstation/assets/47710522/522c1d85-b9cf-4e0e-9588-9d3993eea03f)

</details>

## Why It's Good For The Game

The UI has largely stayed the same since modular tablets were added a
year ago. Even better, direct messaging has been the same since PDAs
were first added *more than a decade ago*. Imagine that.

Now we finally actually (!) make use of those brand new features that we
got from the TGUI switch in this regard.
## Changelog
:cl: distributivgesetz
add: Updated Direct Messenger to v6.5.3. Now including brand new
individual chat rooms, proper image attachments and a revolutionary
message input field!
add: Added a "Reset Imprint" option to the PDA painter.
refactor: Refactored PDA imprinting code just a bit.
fix: PDAs should now properly respond to rigged messages.
/:cl:

---------

Co-authored-by: Jeremiah <42397676+jlsnow301@users.noreply.github.com>

---
## [Kubisopplay/tgstation](https://github.com/Kubisopplay/tgstation)@[27d46f1717...](https://github.com/Kubisopplay/tgstation/commit/27d46f17173034b805d6ef064d4db31c7e34b26d)
#### Tuesday 2023-08-22 12:17:14 by OrionTheFox

Science Resprite! (With Sovl!) (#77314)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
What a crusty department. These outfits are...
Something.

![image](https://github.com/tgstation/tgstation/assets/76465278/63fe13cf-bcbf-42c2-a22c-c868ae49a72c)

How old are these now? I'm pretty sure they're unchanged since when I
started playing years ago on other servers.... besides the RD Turtleneck
and Roboticist suit of course. But they still did have some touch-ups to
be made...

Regardless, I think this department deserves a little love!
I've tried to stay true as I could to their current designs; this isn't
a re-**_design_**, just a re-sprite. I used the base jumpsuit design
from Medbay for most of these since it's the most modern suit that fit
with the colored-spots style.

![image](https://github.com/tgstation/tgstation/assets/76465278/ef7ff5b0-f0e3-481a-9ed4-ba830e3ee0c3)

All of them have been touched up, and the RD's "alt" is now a subtype of
the buttondown so it can easily inherit any sprite updates in the
future.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
These deserved some touch-ups and modernization, and while I'm not keen
on entirely reworking them I figured I could at the least give them the
update the Science Team deserves.

(The buttondown has an outdated obj sprite in this image! It's since
been made smaller and more folded)
Also labcoats for comparison

![dreamseeker_Ds8gZLKoGE](https://github.com/tgstation/tgstation/assets/76465278/4da60512-b813-4260-b3fe-5c71b60cec81)

![dreamseeker_C9DpFWWOS7](https://github.com/tgstation/tgstation/assets/76465278/1de55f4c-2eaa-480b-811f-aaa5832eeceb)

![dreamseeker_02d3d7b6aj](https://github.com/tgstation/tgstation/assets/76465278/b1f40d03-c9b8-4f6b-bc54-516b11a7bfb3)

![dreamseeker_DwJGDwbUf1](https://github.com/tgstation/tgstation/assets/76465278/20f97a5e-42ab-4fe0-8eae-4ac6ed24ead4)


<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. You can read up on GBP
and it's effects on PRs in the tgstation guides for contributors. Please
note that maintainers freely reserve the right to remove and add tags
should they deem it appropriate. You can attempt to finagle the system
all you want, but it's best to shoot for clear communication right off
the bat. -->

:cl:
image: resprited the entirety of RnD! Genetics, Robotics, the RD, and
the Science Team themselves will enjoy the fresh new looks but same
great taste! No, wait, great STYLE! Don't eat these, they're covered in
chemicals.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Kubisopplay/tgstation](https://github.com/Kubisopplay/tgstation)@[a288abcaf2...](https://github.com/Kubisopplay/tgstation/commit/a288abcaf2a6b6c44edade8265a66b9ba3f0e67b)
#### Tuesday 2023-08-22 12:17:14 by san7890

Fixes runtime relating to hard TGS reboots (PROBABLY WON'T FIX REBOOT CRASHES) (#77309)

## About The Pull Request

Servers are crashing on every round restart and I have absolutely no
idea where to start, but I noticed this so I figure I'll throw up a PR
to fix it.

This is the runtime (only found in dd.log, sorry non-admin/maintainer
gamers
https://[tgstation13.org/raw-logs/sybil/data/logs/2023/08/01/round-211577/dd.log](https://tgstation13.org/raw-logs/sybil/data/logs/2023/08/01/round-211577/dd.log)
)

```txt
[00:07:07] Runtime in code/modules/logging/log_holder.dm,166: Attempted to call shutdown_logging twice!
  proc name: shutdown logging (/datum/log_holder/proc/shutdown_logging)
  src: /datum/log_holder (/datum/log_holder)
  call stack:
  /datum/log_holder (/datum/log_holder): shutdown logging()
  shutdown logging()
  world: Reboot(0, 0)
  Ticker (/datum/controller/subsystem/ticker): Reboot("Round ended.", "proper completion", 600)
```

This is the full log:


![image](https://github.com/tgstation/tgstation/assets/34697715/af938235-3076-41d5-98b2-02907dedb6d5)

This is the code:


![image](https://github.com/tgstation/tgstation/assets/34697715/371b11cb-3bc9-4a99-a17c-73968ded308d)

For some reason, even though we invoke `TGSEndProcess`, we still
continue on in this `if()` chain. I don't know why we keep executing DM
code after TGS is supposed to be shut down (which may be why no one has
ever included a `return` here, but let's be safe instead of sorry.

If you really want to investigate why TGS is running DM code after we
end the process, I am amenable to including a stack trace or crash of
this phenomenon instead.
## Why It's Good For The Game

Since we aren't invoking `LOG_CLOSE_ALL` to rust-g twice (which seems to
be really unwanted per the code I read), hopefully thing no crash?
Rust-g had two breaking changes (one with logs, and one with SQL), so
I'm presuming that this might be related to the log one (which is why we
didn't see this sorta thing happen pre-#77307)... Worst case scenario
less runtimes in the funny runtime log.

I hope this wasn't loadbearing either... Likely requires testmerging
since TGS and I don't get along on my machine.
## Changelog
:cl:
server: Added a preventative measure to prevent calling both
TGSHardRestart and TGSReboot, as well as potentially invoking sensitive
procs that are only meant to be called once.
/:cl:

TL;DR- I do not definitively know why servers are crashing but I noticed
this runtime so I'll put out this open flame while I have the time to do
so.

---
## [Aquizit/Yogstation](https://github.com/Aquizit/Yogstation)@[9db2f06363...](https://github.com/Aquizit/Yogstation/commit/9db2f06363bc325a0e8eadfdf7266e55def4d7c1)
#### Tuesday 2023-08-22 13:07:42 by Scrambledeggs

Fuck you *Ungreens your Peacekeepers* (#20053)

* Sprites Part 1: I hate transparency

* Sprites Part 2: Electric Booogaloo

* lack of transparency fixed

* More sprite fixes

* Tacmask and sprites

* Tacprod inactive and nocell sprites

* Tacprod Animation Part 1: Bugs galore

* Tacprod Animation Part 2: Tacmask revengance

* white beret

---
## [PixelTheKermit/space-station-14](https://github.com/PixelTheKermit/space-station-14)@[31607a0be0...](https://github.com/PixelTheKermit/space-station-14/commit/31607a0be0e2ef24f4d53c7611172ec6d40a3a2b)
#### Tuesday 2023-08-22 14:14:38 by Emisse

hardsuit/firesuit cleanup (#18308)

* real

* hjoly fuck you guy sare annoying

* fix cargo arbitrage idk why tf it changed from editing armor values but fuck my life i guess

* why god

* Update suits.yml

* Update cargo_emergency.yml

---
## [pippinbarr/v-r-5](https://github.com/pippinbarr/v-r-5)@[b9b5de295e...](https://github.com/pippinbarr/v-r-5/commit/b9b5de295eabd74e44d18e019f5dd49bb3f31a3b)
#### Tuesday 2023-08-22 14:37:17 by Pippin Barr

Resized the island and added a test structure

- Made the island smaller and flatter to avoid it feeling overwhelmingly large (now 1km square)
- Fought with ProBuilder enough to create a kind of "shipping container" shape you can go into, plus some stairs leading into it
- Shades of the whole v r $4.99 thing where uneven terrain means thinking about "accessibility" for the character controller capsule -- down the line might want to terraform in some places to make things sit in interesting ways?
- Made a "concrete" texture to try to match the resolution of the world as the standard Unity diffuse texture looked pretty weird. Made it nonmetallic and nonsmooth and it doesn't look too too awful - suspect its "grain" can be even more subtle than it is right now, same goes for normals which I tried to mess with as well to flatten them out a bit too.
- Exported as WebGL so it's viewable
- Feels like the rubber is gonna hit the road soon in terms of... well, when I make these structures what do the shadows *actually look like* and are they worth looking at?
- Really need to build up my competency with ProBuilder - may even need to just slam some tutorials - if I'm going to be able to fluidly build out the "shadow boxes" and other display ideas
- Tried to find some water but reprioritized to the shadows -- but still need water and would like a similar low res look to it I guess? The build is still coming in around 36MB which is... promising?

---
## [Rex9001/Rex_Tg](https://github.com/Rex9001/Rex_Tg)@[3645fa7d89...](https://github.com/Rex9001/Rex_Tg/commit/3645fa7d8956bed2d3ebff86b072f8b9544d383d)
#### Tuesday 2023-08-22 14:39:41 by distributivgesetz

Replaces slime clone damage with a "Covered in Slime" status effect (#77569)

## About The Pull Request

This PR replaces clone damage dealt by slimes with a new status effect,
"Covered in Slime".

The status effect is applied when you wrestle a slime off. The status
effect has a chance of not applying if your biohazard protection on your
head and chest is good enough.

It deals brute damage over time and gets removed when you stand under
the shower for about 10 seconds or when you are about to enter softcrit.

As a direct consequence of adding this feature I added showers to the
North Star and Birdshot Xenobiology Labs. I'm sorry, I'm sure you wanted
to make a statement with this, but we kind of require them in there now.

## Why It's Good For The Game

One source of clone damage eliminated whilst hopefully keeping a
"unique" interaction when dealing with slimes. No other source of clone
damage has been touched.

Clone damage is a damage type that shouldn't exist anymore, it's a relic
left from the era of cloning and it's so specific of a damage type that
it rarely gets used as a result. It really should be a type of
affliction (wound etc) instead of its own damage counter.

However, some things in the game still depend on clone damage being
around, so those needs to be addressed first.
We start off with slimes in this PR.

This status effect either lets you either continue with your work if you
react fast enough or it forces you to medbay, giving a victim more
control over the situation, as opposed to just being dealt a rare damage
type that always forces you to go to medbay if you want it healed.

## Changelog

:cl: distributivgesetz
add: Replaced slime clone damage with a "Covered in Slime" status effect
that deals brute damage over time and can be washed off by standing
under a shower.
add: Northstar and Birdshot Xenobiology have been outfitted with a new
shower.
code: Replaced the magic strings in slime code with macros. Also
included some warnings to anyone daring to touch the macros.
/:cl:

---
## [nickmccurdy/react](https://github.com/nickmccurdy/react)@[ac1a16c67e...](https://github.com/nickmccurdy/react/commit/ac1a16c67e268fcb2c52e91717cbc918c7c24446)
#### Tuesday 2023-08-22 14:55:48 by Sebastian Markbåge

Add Postpone API (#27238)

This adds an experimental `unstable_postpone(reason)` API.

Currently we don't have a way to model effectively an Infinite Promise.
I.e. something that suspends but never resolves. The reason this is
useful is because you might have something else that unblocks it later.
E.g. by updating in place later, or by client rendering.

On the client this works to model as an Infinite Promise (in fact,
that's what this implementation does). However, in Fizz and Flight that
doesn't work because the stream needs to end at some point. We don't
have any way of knowing that we're suspended on infinite promises. It's
not enough to tag the promises because you could await those and thus
creating new promises. The only way we really have to signal this
through a series of indirections like async functions, is by throwing.
It's not 100% safe because these values can be caught but it's the best
we can do.

Effectively `postpone(reason)` behaves like a built-in [Catch
Boundary](https://github.com/facebook/react/pull/26854). It's like
`raise(Postpone, reason)` except it's built-in so it needs to be able to
be encoded and caught by Suspense boundaries.

In Flight and Fizz these behave pretty much the same as errors. Flight
just forwards it to retrigger on the client. In Fizz they just trigger
client rendering which itself might just postpone again or fill in the
value. The difference is how they get logged.

In Flight and Fizz they log to `onPostpone(reason)` instead of
`onError(error)`. This log is meant to help find deopts on the server
like finding places where you fall back to client rendering. The reason
that you pass in is for that purpose to help the reason for any deopts.

I do track the stack trace in DEV but I don't currently expose it to
`onPostpone`. This seems like a limitation. It might be better to expose
the Postpone object which is an Error object but that's more of an
implementation detail. I could also pass it as a second argument.

On the client after hydration they don't get passed to
`onRecoverableError`. There's no global `onPostpone` API to capture
postponed things on the client just like there's no `onError`. At that
point it's just assumed to be intentional. It doesn't have any `digest`
or reason passed to the client since it's not logged.

There are some hacky solutions that currently just tries to reuse as
much of the existing code as possible but should be more properly
implemented.
- Fiber is currently just converting it to a fake Promise object so that
it behaves like an infinite Promise.
- Fizz is encoding the magic digest string `"POSTPONE"` in the HTML so
we know to ignore it but it should probably just be something neater
that doesn't share namespace with digests.

Next I plan on using this in the `/static` entry points for additional
features.

Why "postpone"? It's basically a synonym to "defer" but we plan on using
"defer" for other purposes and it's overloaded anyway.

---
## [TheVekter/tgstation](https://github.com/TheVekter/tgstation)@[6c34d93be7...](https://github.com/TheVekter/tgstation/commit/6c34d93be715012943626d0f812e99f730a536ef)
#### Tuesday 2023-08-22 15:20:45 by necromanceranne

Nukies Update 7: Hats (Also massive uplink standardization, weapon kits and ammo changes) (#77330)

## About The Pull Request

Massively overhauls and standardizes the nuclear operative uplink. 

### Weapon Kits

Essentially, all the main weapons of the uplink have been changed to
instead come as 'weapon kits', which are essentially cases containing a
weapon loadout to enable operatives to easily start operating on only
just one item purchase, without the fuss of worrying whether or not
operatives are getting spare ammo, or getting relevant equipment for
success. Consider this a pseudo-loadout, though without necessarily
restricting the purchasing of more weapon kits.

All kits come in three categories: Low Cost (8 TC), Medium Cost (14 TC)
and High Cost (18 TC). This is also matched by categorized ammo costs;
Basic Ammo (2 TC), Hollow Point and Armour Penetrating (4 TC),
Incendiary (3 TC) and Special (or anything that does not easily fit
these categories and does something real extra) (5 TC). Weapons that
lacked these ammos have gained these ammo types to fill the gaps.

<details>
There is may one exception to this in disruptor ammo, which is priced as
basic ammo if only because it isn't _quite_ good enough to justify
pricing at 5 tc and I can see an op wanting to use it as a basic ammo
type instead of normal .50 BMG against, say, a silicon/mech heavy
opposition. Since it cannot kill organics on its own, I'll consider this
mostly basic-adjacent
</details>
The kits have also been labelled based on potential difficulty. This
reflects possible difficulties in using the item, how conducive it is to
success for how much game knowledge needed to actually use it, and how
likely an op is to succeed using it. I don't expect ops to win using
nothing but a rocket launcher, but I think ops should get a fair shake
at trying, yeah?

The kits are as below:
#### **Low-Cost**
_Bulldog (Moderate):_ Shotgun and three magazines of standard ammo.
_Ansem (Easy/Spare):_ Pistol and three spare magazines of standard ammo.
#### **Medium Cost**
_C-20r (Easy):_ SMG and three spare magazines of standard ammo.
_Energy Sword and Shield (Very Hard):_ Energy sword and shield. (Also a
special hat)
_Revolver (Moderate):_ Revolver and three speedloaders of standard ammo.
_Rocket Launcher (Hard):_ Rocket launcher with three spare rockets.
#### **High Cost**
_L6 SAW (Moderate):_ LMG, and that's it. No spare ammo.
_M-90gl (Hard):_ Rifle, two spare magazines of standard ammo and a box
of rubber grenades.
_Sniper (Hard):_ Sniper rifle, two spare magazine of standard ammo, and
one magazine of disruptor ammo. Also suit and tie.
_CQC (Very Hard):_ Comes with a stealth implant and a bandana.
_Double-Energy Sword (Very Hard):_ Double-energy sword, syndicate soap,
antislip module, meth injector and a prisoner jumpsuit.
_**NEW** Grenadier's Kit (Hard):_ Grenadier's belt and grenade launcher
(the one that launchers chem grenades). (I replaced the shit acid
grenade with another flashbang in the belt)

Surplus SMG (Flukie difficulty) has been unchanged. It just now comes
with two rations.

Includes two new revolver ammo types: Phasic, which goes through walls
and armor, but has significantly less damage as a result (I've equalized
the revolver damage and the rifle version's damage to 30 for both). And
Heartseeker, which has homing bullets. Both are Special ammo, and are
priced at 5 TC a speedloader.

### Other Gear

The other items in the uplink have also been consolidated and
standardized in various ways.

#### Grenades

Most now cost 15 TC for three grenades of any given type (including the
full fungal tuberculous). This is pretty much identical to the previous
price, just more consistent overall and front-loaded in cost.

#### Reinforcements

All the various reinforcements now cost 35 TC and all refundable,
equalizing cost to the average across the reinforcements. This is
primarily because I feel like all these options should be weighed
equally, and not one of these options are necessarily worse or better
than the other in their current balance. They're largely inaccessible
for normal ops regardless, and typically come out when there is a
discount or war ops. I took the average value and went with it. Not much
more to say.

#### Mechs

They're just cheaper. These things still suck and they need help.
They've always needed help. A slightly less excessive value for the
mechs may help see people willing to spend the TC on them. I doubt it. I
seriously suggest not buying these still. I keep them in primarily
because they are big stompy mechs and are kind of iconic 'war ops' gear.

#### Bundles

Since I've implemented weapon kits, gun bundles are rather redundant. So
the bulldog weapon and ammo bundle, the c20-r weapon and ammo bundle and
technically the sniper bundle were removed. The sniper bundle is now the
weapon kit, obviously.

Nothing else here really. Except for one....

#### Implants

Not much changed here. I standardized the implant prices to 8 TC a pop.
This is in accordance with traitor implants, which ops also get. So
everything in this category bar a few exceptions (like macro/microbombs)
are around 8 TC. Makes sense to me, really.

Importantly, I made the Implant bundle 25 TC, and I unrandomized the
contents. Who in the right fucking mind would spend 40 TC just to get
five reviver implants is beyond me. But instead, you get one of each of
the cybernetic implants except thermal eyes (you can just buy thermals
and get the benefit of both vision types; x-ray and thermal vision, if
you want to use smokescreens a lot).

#### Base Keys

They're all now 15 TC, except the fridge which is 5 TC. It's weird
they're valued differently when they are taken mostly to do gimmicks
like xenobio and toxins in a hurry before hitting the station. So we've
standardized it.

## Hat Crate

**YES, GOOD SIR, YOU TOO CAN ORDER A HAT CRATE FROM THE SYNDICATE STORE
FOR ONLY 5 TC!**

**NO NEED FOR A KEY, JUST BUY IT AND PULL IT OPEN WITH YOUR STANDARD
ISSUE CROWBAR!**

**ENJOY YOUR NEW CRATE! ENJOY YOUR NEW HAT!**

**PUT IT ON USING THE FREE HAT STABILIZERS WE INCLUDED WITH THE HATS!**

~~**NO REFUNDS IF YOU GET BLOOD ON YOUR HAT!**~~

<details>
There is a 1% chance to instagib people with direct hits from a rocket.
This does the crit effect.
</details>

## Why It's Good For The Game

The uplink needed more spring cleaning and standardization.

With this, I've partially implemented my older idea for ammo consistency
and initial allowance for nukies. Ammo is kind of over-priced and often
where a good chunk of TC goes towards without really pushing nukies
towards meaningful success. And it is often what is tripping up new
players who didn't think to get any. Now, when they get a gun, they get
ammo in their case. On top of this, the weapon kit category is both at
the top of the uplink AND has a little label to say 'Recommend', so that
these new players will hopefully know they should be looking there
first.

In addition, it is the gateway towards a concept that is currently being
worked on. Nuclear operatives having some degree of predefined loadouts
for players to select if they aren't sure what they want, or don't know
what to get. Nukies is very confusing for many players. So giving them a
fighting chance with some premade setups can help ease them into the
role without needing too much player knowledge in how to apply the
items. This is only one step towards that, so that players can identify
what gear they need to help succeed based on their skill.

I wanted to implement a difficulty warning so that players can choose
gear loadouts that are actually conducive to their skill and knowledge.
I based it on how much players would need to know to engage in combat
with it, and how much fiddling is required to get something to work
properly (overly involved reloading is a consideration, for example, as
well as precise button presses). In addition, how much of a force
multiplier some weapons can be for their ease of use.

Most people recognize the c20-r as the most new player friendly weapon,
as an example. So it would be good to steer players towards taking that
gun because of how easy it is to use, understand and succeed with it.

And most importantly of all; Having standards within the uplink is
important. Most of the values in the uplink are just completely random.
Nobody has a good grasp of what is too much or too little. Even just a
hint of consistency, and people will stick to it (see implants for what
I mean). And there is still some work to be done even there. A good
start is weapons. Price for power can be meaningful when decided whether
we want some weapons to come out more often than others. Players do
enjoy making informed decisions and choices, and having affordability be
a draw to some otherwise less powerful weapons (looking at you, Bulldog)
can actually be a worthwhile and meaningful difference.

~~I thought it would tick off the gun nerds to change the calibers on
the guns.~~

~~I also thought adding hats would be funny given the release of TF2's
most recent update.~~

## Changelog
:cl:
balance: Standardizes some of the nuclear operative entries to have more
consistent pricing within their respective categories.
add: Adds some new categories so that players have an easier time
navigating the nuclear operative uplink.
balance: Many items have had prices reduced or adjusted to make them
more desirable or more consistent within their category.
add: Weapon kits have replaced almost all the individual weapons in the
uplink. You now buy these instead of the individual weapon. These often
come with spare ammo or relevant gear for success.
add: Most ammo types have been standardized in price.
refactor; Removes a lot of redundant item entry code and tidies up the
actual code part of the nuclear uplink so that it is much easier to find
things within it.
add: Added 40 new cosmetic items to the Syndicate Store. Buy them now
from the Hat Crate, only 5 TC!
code: Updated the nuclear operative uplink files.
/:cl:

---
## [TheVekter/tgstation](https://github.com/TheVekter/tgstation)@[95ec0e6545...](https://github.com/TheVekter/tgstation/commit/95ec0e65458ece9c5c80952e75d5d32c4fbb794b)
#### Tuesday 2023-08-22 15:20:45 by necromanceranne

Dissection experiments are handled by autopsy surgery. Removes redundant dissection surgery. You can repeat an autopsy on someone who has come back to life. (#77386)

## About The Pull Request

TRAIT_DISSECTED has had the surgical speed boost moved over to
TRAIT_SURGICALLY_ANALYZED.

TRAIT_DISSECTED now tracks if we can do an autopsy on the same body
again, and blocks further autopsies if it is on the mob. A mob that
comes back to life loses TRAIT_DISSECTED. This allows for mobs to be
autopsied once again.

Since it is completely redundant now (and was the whole time TBH),
dissections have been removed in favour of just having the experiment
track autopsies.

Fixes https://github.com/tgstation/tgstation/issues/76775

## Why It's Good For The Game

Today I showed up to a round where someone autopsied all the bodies in
the morgue, not realizing they were using the wrong surgery. Since I
couldn't _redo_ the surgery, this rendered all these bodies useless.
This was not out of maliciousness, they just didn't know better. There
are two autopsies in the surgery list, but only one is valid for the
experiment and doing the wrong one blocks _both surgeries_. Dissection
is completely useless outside of experiments. This same issue also
prevents additional autopsies on the same person, even if they had come
back to life and died again after you had done the initial autopsy.
Surely you would want to do more than one autopsy, right? That's two
separate deaths!

This resolves that by giving you a method of redoing any screwups on the
same corpse if necessary. It only matters if the experiment is available
anyway, so there isn't much reason to punish players unduly just because
they weren't aware science hadn't hit a button on their side (especially
since it isn't communicated to the coroner in any way to begin with). It
also removes a completely useless surgery and ties in the experiment to
what the coroner is already going to be doing. They can dissect their
corpses to their hearts content without worrying about retribution from
science for doing so.

In addition, someone repeatedly dying can continue to have autopsies
done on them over the course of the round. The surgery bonus only
applies once, so the only reason to do autopsies after the first is to
discover what might have killed someone. No reason this should block
further surgeries, just block surgeries when the person remains a
corpse.

## Changelog
:cl:
fix: You can do autopsies on people who were revived and died again
after they had already been dissected.
qol: Autopsies have become the surgery needed to complete the dissection
experiments. As a result, the dissection surgery has been removed as it
is now redundant.
qol: A coroner knows whether someone has been autopsied and recently
dissected (and thus hasn't been revived) by examining them.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[2d4d23dbf1...](https://github.com/san7890/bruhstation/commit/2d4d23dbf1e2cc23ed2046534011561e443060f7)
#### Tuesday 2023-08-22 16:26:12 by Timberpoes

Replaces the poster and graffiti objectives with assault and early steal & destroy ones. (#77029)

## About The Pull Request

With the blessings of @Watermelon914 I am removing the two objectives
for placing posters and spraying graffiti.

These old objectives are not dead. Their items have moved to the
Badassery section of the uplink.

A box of 3 demotivational posters can be bought for 1TC with 0 rep.
The spraycan can be bought for 1TC with 0 rep.

In their place comes one new objective and one extended objective.

The new objective is Assault a Crewmember. This objective requires you
to attack the specified target 2-5 times (random on objective
generation). It tallies from any attack that filters through the
`/datum/element/relay_attackers` element and has an "attacker"
associated with it.

Although it asks you not to kill the other player, it doesn't fail if
you kill them.

I have expanded the low-risk theft objectives with items like a mime
mask, lawyer badge and a fake moustache (commonly on cooks).

Finally, I've added a very low level set of steal-and-destroy objectives
aimed at some items that will require a bit of basic breaking and
entering, and the destruction of which may hurt crew morale.

```
/datum/objective_item/steal/traitor/donut_box
/datum/objective_item/steal/traitor/rpd
/datum/objective_item/steal/traitor/space_law
/datum/objective_item/steal/traitor/granted_stamp
/datum/objective_item/steal/traitor/denied_stamp
/datum/objective_item/steal/traitor/lizard_plush
/datum/objective_item/steal/traitor/moth_plush
/datum/objective_item/steal/traitor/insuls
```

This PR also fixes clown shoes missing a proc override to allow them to
actually register as a theft objective.


![image](https://github.com/tgstation/tgstation/assets/24975989/775d46cf-f40a-43e5-9bf1-3aa4a31d436e)

![image](https://github.com/tgstation/tgstation/assets/24975989/66c77815-1f2b-4dfb-99c6-b8f2e0061654)

![image](https://github.com/tgstation/tgstation/assets/24975989/85d3878a-c598-4ec0-9bb1-920380a004c6)
## Why It's Good For The Game

Basically my discussion with Watermelon focused on the idea that the
graffiti and poster objectives weren't really crimes. They baited
antagonists into very passive play early-game.

These new replacements encourage a more antagonistic playstyle. Starting
fights plus B&E are two bread-and-butter play paradigms for antaggery.

Giving a few early game theft + destroy options with a mix of impactful
items (like insuls and RPDs) versus more symbolic or emotive items
(plushies, donut boxes, Cargonia stamps) gets antagonists out and about
in the station, warming themselves up.

And having an objective to assault players (even if you don't kill them)
allows cheeky antags with a penchant for shittery to start fights with
players and start genuinely impacting the shift, involving sec and
drawing players into their antaggery.

Both of these natually ease players into the more substantive theft and
murder objectives.

The existing spray and posters are actually thematically super cool.
Traitors now have even more access to them since they can be bought for
1TC per spraycan/3-pack of posters. This lets antags with TC to spare
run gimmicks around them and adds extra fun to the Badassery section.
## Changelog
:cl:
del: Traitor objectives to place posters and graffiti the station have
been removed.
add: The items associated with the poster and graffiti objectives can
now be purchased from the Badassery section of the uplink. The posters
come in a box of 3 for 1TC, and the spraycans are 1TC each.
add: Adds a new Assault traitor objective, requiring you to the attack
the target a few times without needing to kill them. Earn TC and
reputation by starting barroom fights and bait players into escalation
battles for fun and profit.
add: Expands low-risk steal objectives to include the Chef's fake
moustache, Lawyer's badge, and Mime's mask.
add: Adds brand new shift start Steal & Destroy objectives for early
breaking and entering. Smash your way into a sec checkpoint to grab a
Space Law book, engineering to grab some insulated gloves or the psych
office to kidnap their moth plush.
fix: Fixes an issue where the steal clown shoes objective would never be
valid.
/:cl:

---
## [adump1v/platform_frameworks_base](https://github.com/adump1v/platform_frameworks_base)@[66461cd22c...](https://github.com/adump1v/platform_frameworks_base/commit/66461cd22caaf1aa02583884ba9d68c9b20977b9)
#### Tuesday 2023-08-22 17:08:42 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6
Signed-off-by: Sageofd6path <mail2anirban95@gmail.com>

---
## [PixelExperience-Devices/kernel_xiaomi_sm7325](https://github.com/PixelExperience-Devices/kernel_xiaomi_sm7325)@[870e7d7108...](https://github.com/PixelExperience-Devices/kernel_xiaomi_sm7325/commit/870e7d7108432f0c6fad2dec6ef6060d4ee49169)
#### Tuesday 2023-08-22 17:22:50 by Darrick J. Wong

xfs: change the order in which child and parent defer ops are finished

commit 27dada070d59c28a441f1907d2cec891b17dcb26 upstream.

The defer ops code has been finishing items in the wrong order -- if a
top level defer op creates items A and B, and finishing item A creates
more defer ops A1 and A2, we'll put the new items on the end of the
chain and process them in the order A B A1 A2.  This is kind of weird,
since it's convenient for programmers to be able to think of A and B as
an ordered sequence where all the sub-tasks for A must finish before we
move on to B, e.g. A A1 A2 D.

Right now, our log intent items are not so complex that this matters,
but this will become important for the atomic extent swapping patchset.
In order to maintain correct reference counting of extents, we have to
unmap and remap extents in that order, and we want to complete that work
before moving on to the next range that the user wants to swap.  This
patch fixes defer ops to satsify that requirement.

The primary symptom of the incorrect order was noticed in an early
performance analysis of the atomic extent swap code.  An astonishingly
large number of deferred work items accumulated when userspace requested
an atomic update of two very fragmented files.  The cause of this was
traced to the same ordering bug in the inner loop of
xfs_defer_finish_noroll.

If the ->finish_item method of a deferred operation queues new deferred
operations, those new deferred ops are appended to the tail of the
pending work list.  To illustrate, say that a caller creates a
transaction t0 with four deferred operations D0-D3.  The first thing
defer ops does is roll the transaction to t1, leaving us with:

t1: D0(t0), D1(t0), D2(t0), D3(t0)

Let's say that finishing each of D0-D3 will create two new deferred ops.
After finish D0 and roll, we'll have the following chain:

t2: D1(t0), D2(t0), D3(t0), d4(t1), d5(t1)

d4 and d5 were logged to t1.  Notice that while we're about to start
work on D1, we haven't actually completed all the work implied by D0
being finished.  So far we've been careful (or lucky) to structure the
dfops callers such that D1 doesn't depend on d4 or d5 being finished,
but this is a potential logic bomb.

There's a second problem lurking.  Let's see what happens as we finish
D1-D3:

t3: D2(t0), D3(t0), d4(t1), d5(t1), d6(t2), d7(t2)
t4: D3(t0), d4(t1), d5(t1), d6(t2), d7(t2), d8(t3), d9(t3)
t5: d4(t1), d5(t1), d6(t2), d7(t2), d8(t3), d9(t3), d10(t4), d11(t4)

Let's say that d4-d11 are simple work items that don't queue any other
operations, which means that we can complete each d4 and roll to t6:

t6: d5(t1), d6(t2), d7(t2), d8(t3), d9(t3), d10(t4), d11(t4)
t7: d6(t2), d7(t2), d8(t3), d9(t3), d10(t4), d11(t4)
...
t11: d10(t4), d11(t4)
t12: d11(t4)
<done>

When we try to roll to transaction #12, we're holding defer op d11,
which we logged way back in t4.  This means that the tail of the log is
pinned at t4.  If the log is very small or there are a lot of other
threads updating metadata, this means that we might have wrapped the log
and cannot get roll to t11 because there isn't enough space left before
we'd run into t4.

Let's shift back to the original failure.  I mentioned before that I
discovered this flaw while developing the atomic file update code.  In
that scenario, we have a defer op (D0) that finds a range of file blocks
to remap, creates a handful of new defer ops to do that, and then asks
to be continued with however much work remains.

So, D0 is the original swapext deferred op.  The first thing defer ops
does is rolls to t1:

t1: D0(t0)

We try to finish D0, logging d1 and d2 in the process, but can't get all
the work done.  We log a done item and a new intent item for the work
that D0 still has to do, and roll to t2:

t2: D0'(t1), d1(t1), d2(t1)

We roll and try to finish D0', but still can't get all the work done, so
we log a done item and a new intent item for it, requeue D0 a second
time, and roll to t3:

t3: D0''(t2), d1(t1), d2(t1), d3(t2), d4(t2)

If it takes 48 more rolls to complete D0, then we'll finally dispense
with D0 in t50:

t50: D<fifty primes>(t49), d1(t1), ..., d102(t50)

We then try to roll again to get a chain like this:

t51: d1(t1), d2(t1), ..., d101(t50), d102(t50)
...
t152: d102(t50)
<done>

Notice that in rolling to transaction #51, we're holding on to a log
intent item for d1 that was logged in transaction #1.  This means that
the tail of the log is pinned at t1.  If the log is very small or there
are a lot of other threads updating metadata, this means that we might
have wrapped the log and cannot roll to t51 because there isn't enough
space left before we'd run into t1.  This is of course problem #2 again.

But notice the third problem with this scenario: we have 102 defer ops
tied to this transaction!  Each of these items are backed by pinned
kernel memory, which means that we risk OOM if the chains get too long.

Yikes.  Problem #1 is a subtle logic bomb that could hit someone in the
future; problem #2 applies (rarely) to the current upstream, and problem

This is not how incremental deferred operations were supposed to work.
The dfops design of logging in the same transaction an intent-done item
and a new intent item for the work remaining was to make it so that we
only have to juggle enough deferred work items to finish that one small
piece of work.  Deferred log item recovery will find that first
unfinished work item and restart it, no matter how many other intent
items might follow it in the log.  Therefore, it's ok to put the new
intents at the start of the dfops chain.

For the first example, the chains look like this:

t2: d4(t1), d5(t1), D1(t0), D2(t0), D3(t0)
t3: d5(t1), D1(t0), D2(t0), D3(t0)
...
t9: d9(t7), D3(t0)
t10: D3(t0)
t11: d10(t10), d11(t10)
t12: d11(t10)

For the second example, the chains look like this:

t1: D0(t0)
t2: d1(t1), d2(t1), D0'(t1)
t3: d2(t1), D0'(t1)
t4: D0'(t1)
t5: d1(t4), d2(t4), D0''(t4)
...
t148: D0<50 primes>(t147)
t149: d101(t148), d102(t148)
t150: d102(t148)
<done>

This actually sucks more for pinning the log tail (we try to roll to t10
while holding an intent item that was logged in t1) but we've solved
problem #1.  We've also reduced the maximum chain length from:

    sum(all the new items) + nr_original_items

to:

    max(new items that each original item creates) + nr_original_items

This solves problem #3 by sharply reducing the number of defer ops that
can be attached to a transaction at any given time.  The change makes
the problem of log tail pinning worse, but is improvement we need to
solve problem #2.  Actually solving #2, however, is left to the next
patch.

Note that a subsequent analysis of some hard-to-trigger reflink and COW
livelocks on extremely fragmented filesystems (or systems running a lot
of IO threads) showed the same symptoms -- uncomfortably large numbers
of incore deferred work items and occasional stalls in the transaction
grant code while waiting for log reservations.  I think this patch and
the next one will also solve these problems.

As originally written, the code used list_splice_tail_init instead of
list_splice_init, so change that, and leave a short comment explaining
our actions.

Signed-off-by: Darrick J. Wong <darrick.wong@oracle.com>
Reviewed-by: Dave Chinner <dchinner@redhat.com>
Reviewed-by: Brian Foster <bfoster@redhat.com>
Signed-off-by: Chandan Babu R <chandan.babu@oracle.com>
Acked-by: Darrick J. Wong <djwong@kernel.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [yousuf-safin/Mosque_Donation](https://github.com/yousuf-safin/Mosque_Donation)@[c6b1948a1e...](https://github.com/yousuf-safin/Mosque_Donation/commit/c6b1948a1ec84d292a425edc12c70835a6f071f8)
#### Tuesday 2023-08-22 17:24:42 by Yousuf Ali Shafin

Add files via upload

Welcome to the Mosque Donation System GitHub Repository!

**Project Description:**

The Mosque Donation System is a comprehensive platform designed to facilitate seamless donation management for mosques and their congregants. Developed using Java Swing for the frontend and powered by MSSQL for database management, this project offers both an admin panel and a user panel to ensure efficient administration and user engagement.

**Features:**

1. **Dual Panel Functionality:** The system provides distinct panels for both administrators and users. Administrators can oversee and manage various aspects of the donation system, while users can conveniently make donations and track their contribution history.

2. **User Registration and Login:** Both administrators and users can register and log in to the system securely. This ensures personalized experiences and streamlined interactions.

3. **Mosque Selection:** Users can choose from a list of participating mosques and select the specific donation area they wish to contribute to. This feature empowers users to direct their donations according to their preferences.

4. **Comprehensive Admin Controls:** The admin panel offers the ability to update, delete, and manage mosque and user information. This ensures the system remains up-to-date and adaptable to changing circumstances.

5. **Real-time Donation Tracking:** The system dynamically tracks and displays the total donations received for each mosque sector. This functionality aids administrators in monitoring donation trends and allocating resources effectively.

6. **Detailed User Contribution History:** Users can view their donation history, including dates, mosque sectors, and amounts. This transparency fosters trust and encourages continued engagement.

**Getting Started:**

To run the Mosque Donation System on your system, follow these steps:

1. Clone the repository or download the project files.
2. Import the provided SQL file into your MSSQL Server instance to create the necessary database schema and tables.
3. Open the project in your preferred Java IDE and configure the database connection.
4. Build and run the project.

**Contributing:**

We invite contributions to enhance the Mosque Donation System. Whether you have ideas for new features, bug fixes, or improvements, please submit your pull requests. Make sure your code is well-documented and adheres to coding standards.

**License:**

The Mosque Donation System is released under the [GNU License].

Thank you for your interest in the Mosque Donation System. By offering a user-friendly and efficient platform for mosque donations, we hope to encourage greater community participation and support for these important institutions.

---
## [goober3/hi-github-portside](https://github.com/goober3/hi-github-portside)@[b033e1ed6a...](https://github.com/goober3/hi-github-portside/commit/b033e1ed6a1e7f87edc73a75a96bcf6536e39aba)
#### Tuesday 2023-08-22 18:02:28 by Sun-Soaked

Update_Appearance Port (#2170)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
[(original pr)](https://github.com/tgstation/tgstation/pull/55468)
After nine years in development we hope it was worth the wait

I ported this specifically for the signals I'll need for world icons.
However, it had a lot of other useful stuff, so I ended up just grabbing
(almost) the entire pr.
I tried to grab as few of the superfluous code rewrites as possible to
make reviewing a bit easier, but I couldn't help grab stuff like the APC
icon code rewrite(the original code was a war crime).

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

- ports the wrapper proc `update_appearance` for icons, descs, and
names, adds `update_desc` and `update_name` subprocs to handle those.
Things. without just stuffing them into update_icons like some kind of
psychopath

- ports a bunch of signal hooks useful for changing names, descriptions,
and icons. I needed these for world_icons which is where this wild ride
all started

- ports some `base_icon_state` implementation. Stuff like spear code
makes slightly less duplicates(and more sense) now which is nice.
We could definitely implement it more I think but that's a future me
problem

- 500 files of immersive vsc-mass-editing action to implement
`update_appearance()`(sorry in advance, but not as sorry as I was when
manually copy-pasting the custom ones for like 3 straight days)

-"consig" and "comisg" have been taken out behind the codebase and shot.
Not 'technically' a bug it just made my head hurt

-My first pr with 0 player facing changes (confetti)
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: TemporalOroboros, Memed Hams
code: ports update_appearance, update_name, and update_desc from tg, as
well as associated signals
code: a bit of base_icon_state implementation. Can you believe it's been
sitting in our code almost unused for like 3 years
code: cleans up some code formatting, mainly around custom icons and
overlays
code: fixes the typos in COMSIG_STORAGE_EXITED and
COMSIG_STORAGE_ENTERED
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Lufferly/tgstation](https://github.com/Lufferly/tgstation)@[820c22a5f5...](https://github.com/Lufferly/tgstation/commit/820c22a5f5381364c595d21b6c047e269f7f0497)
#### Tuesday 2023-08-22 18:26:19 by DaydreamIQ

Buffs Heretic ash ascension (#77618)

## About The Pull Request

Post-Ascension the Nightwatchers Rebirth (Or Fiery Rebirth) has its
cooldown lowered from 60 seconds to 10
Additionally adds bomb immunity to the list of resistances that
ascension provides

## Why It's Good For The Game

Ash ascension kind of sucks when compared to its big brothers flesh,
rust and blade. You do get a couple of cool spells but their impact is
negated by how shitty fire damage is and while you get a ton of
resistances, you don't get stun immunity and have absolutely zero
sustainability in long-term engagements.

Blade has its lifesteal, rust has its leeching walk and flesh has a big
worm that eats arms. And while the laziest solution would be to give ash
stun immunity like those three I think it'd be more fitting if it could
capitalize on one of its more powerful spells. Keeping in the fight by
siphoning health from all those people you lit on fire with your cascade
instead of watching in pain as they completely negate any threat you
have with a fire extinguisher and temp adapt.

---
## [Lufferly/tgstation](https://github.com/Lufferly/tgstation)@[63f7eb1a6a...](https://github.com/Lufferly/tgstation/commit/63f7eb1a6a01c0c48dcc075f57b58a662d27fc17)
#### Tuesday 2023-08-22 18:26:19 by san7890

Fixes Ticked File Enforcement and Missing Unit Test (and makes said Unit Test Compile) (and genericizes the C&D list to the base unit test datum) (#77632)

Closes #77631

## About The Pull Request

Hey there,

Ticked File Enforcement simply wasn't catching files that were missed.
That's a bit stupid, so I decided to look into what the issue might be,
and whoopsie daisies I did double periods back in #76592
(020ac2405308eab83f314282499dfe777aba5874).

![image](https://github.com/tgstation/tgstation/assets/34697715/6023afe8-313d-4550-9a60-58a8bc211b4f)

I also added some debug info and some more checks to prevent such a
break from happening again on runtime of this script. I thought it was a
weird string concatenation issue (and not the simple break I thought it
was), so I rewrote how it adds `glob`s. I think it's cleaner so I'll
keep it anyhow

This PR also corrects the oversight of the missing unit test (introduced
in #77218 (69827604c46952dd4393db8617cd494ade17bea2)) by reticking it in
the `_unit_tests.dm` file, and also makes it compile because it didn't
do that.

I also then had to do some more work to get the unit test to work.
* Genericizes the Create-and-Destroy "ignore" list to be a static list
on `/datum/unit_test` to allow it to be shared between these types of
tests that we need to test.
* Adds that list to C&D and the broken unit test regarding fantasy
bonuses
* Fixes some actually broken that the unit test was made to catch (beam
rifles, butterdogs and other slippery items, random ingredient boxes).
* Adds cases for things that the unit test and overall framework really
shouldn't be altering anyways (mythril), and was likely causing
inappropriate stack traces on master

## Why It's Good For The Game

Unit Tests WORK. Tools WORK.


![image](https://github.com/tgstation/tgstation/assets/34697715/9a59c0db-7a33-4546-918b-c73372a5b867)


## Changelog

:cl:
fix: Beam rifles will no longer inappropriately retain any bonuses they
may gain from wizardry.
fix: Inappropriate stack traces over bonuses being applied to components
that gain bonuses innately (like Mythril stacks) should cease.
/:cl:

---
## [MCBCMF/MCBCMassacre](https://github.com/MCBCMF/MCBCMassacre)@[24e0471805...](https://github.com/MCBCMF/MCBCMassacre/commit/24e0471805ae290da166dd2ce010af6027f3c4f0)
#### Tuesday 2023-08-22 18:35:32 by Kelvin Williams

Update README.md - Emergency 

#Emergency- Save a Life!


effective: 8-22-23 14:33 EDT until: removed 

We need your assistance in reaching law enforcement in Kentucky. There is a Stingray in operation here in Riverdale I cannot trust I’m talking to the law enforcement in Kentucky.

Please call Lexington KY Police (I cannot trust my Google results to provide you a number) and KY State Police in Frankfort ONLY—they will advise you to call Richmond or LexPD but let them know I am requesting the call and only them.

The address is Mount Calvary Baptist Church. 4742 Todds Rd, Lexington, KY. Lives may be in peril, they can enter!

I need them to send a FEW officers, I need dispatch to check on them every other minute until they’ve said it’s clear.

This is the CIA backed up by the FBI, they can only trust a true Kentuckian. But we may be “brother against brother” again.

I am in Atlanta. I am the pastor of the church. There is no service going on. Regardless of what they see, if they see a hearse they need to call for backup immediately.

See new wiki at https://SotC.wiki or go to https://GitHub.Com/Mission23

Kelvin / Micah

---
## [H-A-M-G-E-R/deltarune_repainted](https://github.com/H-A-M-G-E-R/deltarune_repainted)@[1800bed13e...](https://github.com/H-A-M-G-E-R/deltarune_repainted/commit/1800bed13e153f03e0adc1d77976976062c62d15)
#### Tuesday 2023-08-22 18:57:20 by Fatfuck22

somewhere in nevada

<<I just wanted to tell you a few things. They are pretty important. Everyone thinks it, but they aren't man enough to say it. Krinkels, you movies SUCK!!!!!! Yeah, I said it. It's true! You sucked in the NG styled art collab. You suck all the time. I'm surprised you even had a wife. You are so damn gay. Gay motherfucker! Madness is boring and shouldn't be allowed on newgrounds. Madness Interactive was the worst game every, yeah, who would want to play as a character from a crappy, pointless, and lame series? NOT ME! Everyone thinks that madness is SHIT, they're not lying. You sucked in the rectangle and oval collaboration movie. You act so full of yourself, when you have no reason. Bitch. Madness 9 was the worst movie ever, I saw spam wayyyyyy better than that. Seriously. YOU SUCK! I want you to burn! Madness is dead. BURN IN HELL! Madness is lame! Krinkels.net is for homosexuals, who would want to see a picture of you. I bet your mom made that site for you. You are a fucking homo. Fuck you bitch. I wish everyone could tell you how they really feel about madness combat. We know that they can't........But I can!!! FUCK YOU! Newgrounds doesn't need your damn madness. I can sleep at night knowing that this pm could ruin you life and/or reputation. I can sleep soundly knowing that. You suck. You stupid Fuck! FUCK YOU! Madness 9? What the hell were you thinking? We didn't want madness combat 1. We didn't want breadman, the death of breadman, or the return of breadman! Why? BECAUSE IT WAS SHIT!!!!!!!!!!!!!!!!!!! Krinkels you suck! I didn't write this to mess with you, I wrote this to tell you what everyone is thinking. What the hell kind of name is "KRINKELS"? Even officialdude is better than that.>>
- an angry guy on newground

---
## [Sravani0514/clock_with_sound](https://github.com/Sravani0514/clock_with_sound)@[f68baa641b...](https://github.com/Sravani0514/clock_with_sound/commit/f68baa641b94a830e909ed8c09c75da836d2e1a6)
#### Tuesday 2023-08-22 19:23:12 by Sravani0514

Update README.md



Welcome to the Analog Clock with Changing Background Images project! This project was created as a fun and educational exercise in web development, aiming to combine the visual appeal of an analog clock with the excitement of dynamic background imagery.

 Background

The concept behind this project was to create an analog clock that goes beyond the ordinary by incorporating visually striking background images. Traditional analog clocks serve the purpose of telling time, but we wanted to take it a step further by offering an engaging user experience that evolves with each visit.

 How It Works

When you open the project in your web browser, you'll be greeted by an elegant analog clock featuring hour, minute, and second hands. These hands are designed to move in real-time, accurately reflecting the current time. The clock is positioned against a backdrop of stunning background images that change randomly with each page load.

 Features at a Glance

- **Accurate Time Display:** The clock hands move smoothly and accurately to show the current time.
- **Dynamic Backgrounds:** A collection of captivating background images provides a fresh look every time you open the page.
- **Responsive Design:** The project is designed to look great on various devices, from desktops to smartphones.

 Customization

Feel free to customize this project to suit your preferences or integrate it into other projects. You can adjust the clock's styling, choose different background images, or even enhance the clock with additional features.

 Contributing

Contributions to this project are welcome! If you have suggestions for improvements, bug fixes, or new features, please feel free to submit a pull request.




Enjoy exploring the Analog Clock with Changing Background Images project!

---
## [Alexciao/bubblepopper](https://github.com/Alexciao/bubblepopper)@[059978f884...](https://github.com/Alexciao/bubblepopper/commit/059978f8848ce8cbece8a72a16ff3bfb768ca694)
#### Tuesday 2023-08-22 19:45:35 by Alexciao

Fix the most stupid bug ever

I hate my life i literally spent 5 hours trying to fix this and it was one fricking letter

---
## [facebook/pyre-check](https://github.com/facebook/pyre-check)@[30dbfd9b72...](https://github.com/facebook/pyre-check/commit/30dbfd9b724cf11b1e33c6f9b553eefce32b47ac)
#### Tuesday 2023-08-22 19:49:06 by Vincent Lee

Easy List.length = 0 -> List.is_empty optimizations

Summary:
I was talking with a personal friend learning OCaml yesterday and noticed that List has these neat compare_lengths and compare_length_with functions.

In our codebases, we do List.length on two lists a lot and compare the result, or we do it once and compare the result to a constant integer. Not only is this linear time, it also always traverses the entire list, when we could have bailed early (say we were checking that the length is greater than 2, e.g., a list of length 1000 still gets traversed all the way through).

 ---

All of that to say, that's not what this diff does , this diff just does the easy replacements of List.length <> 0 or similar to call Core.List.is_empty, which is essentially a pointer compare with the empty list and is faster in all cases than calling length then comparing to 0.

I think a follow up (that I won't do, but if anyone is interested) is to make utility functions List.shorter_than/longer_than/equal_lengths that wrap Caml.List.compare_lengths and Caml.List.compare_length_with in a nicer looking API, because they're pretty ugly to use directly, then migrate all `List.length x < int` and `List.length a < List.length b` calls or similar to it, if the length is only used in the comparison and is not subsequently used in the conditional branches.

On callsites where large lists are often passed, or lists of very disparate sizes are passed, it could be a potentially-significant perf win.

Reviewed By: alexkassil

Differential Revision: D48542763

fbshipit-source-id: b846bc32523b7b1b938cc033eb001d656970fa0f

---
## [Mission23/Mission23](https://github.com/Mission23/Mission23)@[1a37dff8ac...](https://github.com/Mission23/Mission23/commit/1a37dff8acf8a2e054d29cacb5841e4ad52ce2d5)
#### Tuesday 2023-08-22 19:51:07 by Micah

Update README.md

Just came to make a link… and left this wall of text behind:

# Mission23

This is the primary repository for #Mission23. It is the repository that holds the soon-to-be (after the shaking stops) most popular wiki in the universe, confirmed so says the creator of it (me), but confirmed by our boss (He is nice to y'all but, He can be really mean though to us), my creator, your creator, the creator of that shaking, the creator of the universe (He doesn't call it that though, He doesnt know how to do anything small scale, the Creator. 

did you see what i did there with the big C? always do that when you talk about Him. and that too with the H, He likes it for the disambiguation (need to check the largest Wiki in the universe real quick to see if i used and smelled that right. im out. brb. always.

y'all ready for GitHub to be a household name!?!?? 

Seriously, thanks @GitHub for helping us get the word out in a way they could not hide it any longer. You dont want to know what I know about that NSL, your network security team has been augemented by Above The Clouds Security, He knows how to handle the bestest NSA staffer. 

Thanke to the git nerds and IRC users everywhere that just clone when asked!
Even biggger thanks to those who pull often. Anr more to git nerds who prayed I'd use it better--He told me to put that shit in cement (the commit descriptions). and lastly, cause my phone or junk is being lasered fron the apartment above. screeb flashed and junk hurted for a second. its that serious! "commit often Kelvin!" (said Donovan) .., the biggest thanks to nerd heroes out there who pulled or refreshed often enough, then paused long enough to call authorities when i couldnt. they got there today! 

As soon as my boss gets a checkbook, I'm gonna buy one of those fancy accounts at GitHub--we do have some copyleft software, algos, and some formulas to that will slow death and stop aging (it is a disease) around here to share. 3 users even. only two will probably ever login. not TomTom  though, he don't do flat phones or flat files either. The third (really the first) who knows... just the Creator, He does come over here. You never know when or where. I always know its Him becauee he's awkward a.f., last time I seen him though didnt realize it was Him untik he "passed" me a cigarette--I'll spare the details. I just thought, "who the hell passes a cigarette like that?" Then I realized... I wonder how He looked as a black woman in church? It is Kentucky, was (s)He one of those northerner types or a good southern lady??? He hardly talks to anyone in person, He would, but you wouldnt like it. Ill explain why in the wiki soon. 

On that note... See that Wiki over there? [Use it.](https://github.com/Mission23/Mission23/wiki)
-m

---
## [AyaShibbi/CODSOFT](https://github.com/AyaShibbi/CODSOFT)@[d25fe9a701...](https://github.com/AyaShibbi/CODSOFT/commit/d25fe9a7011dc128b38111744a4ed28327db2e5f)
#### Tuesday 2023-08-22 19:53:36 by AyaShibbi

Add files via upload

ATM Interface: 

Experience the convenience of the ATM Interface built in Java, a comprehensive project designed to replicate the functionalities of an Automated Teller Machine. Developed with user-friendliness in mind, this simulator encapsulates the essential features of an ATM, offering a seamless banking experience.

Features:
- Class-Based Architecture: The project encompasses classes representing the ATM machine, user interface, and bank account. Each component is thoughtfully designed for clear separation of concerns.
- Interactive User Interface: Crafted to emulate a real ATM experience, the user interface offers options for withdrawing, depositing, and checking the balance. Users can interact with the ATM seamlessly.
- Functional Methods: The project implements essential methods for each user option: withdraw(amount), deposit(amount), and checkBalance(). These methods ensure smooth transactions.
- Bank Account Class: A dedicated class represents the user's bank account, efficiently storing and managing account balances.
- Seamless Integration: The ATM class interacts with the user's bank account class, facilitating the seamless management and modification of account balances.
- Input Validation: To ensure data integrity, user inputs are meticulously validated to guarantee they fall within acceptable limits. This prevents unauthorized actions and enhances security.
- User-Centric Messages: Users receive informative messages based on their chosen options and the outcome of their transactions. Clear feedback enhances the user experience.


Usage:
1. Practical Banking: Offers a platform to practice and familiarize with banking operations safely.
2. Functional Learning: Ideal for hands-on learning in coding, UI design, and software integration.
3. Safe Exploration: Users can experiment with various transactions without affecting actual accounts.
4. Code Development: Developers can enhance skills in software architecture and implementation.
5. User-Centered Interaction: Provides positive and educational interaction, increasing confidence in real-life ATM usage.

Experience virtual banking with the ATM Interface. Whether you're a developer refining skills or an individual keen on understanding ATM operations, this project offers an immersive, educational, and practical experience. Elevate your software design and banking understanding today.

---
## [anderssonw/krakeroygutta](https://github.com/anderssonw/krakeroygutta)@[a0ba21189e...](https://github.com/anderssonw/krakeroygutta/commit/a0ba21189e75ef89585991a728bd60883d21aff5)
#### Tuesday 2023-08-22 20:09:33 by anderssonw

holy shit fantasy picking works

Signed-off-by: anderssonw <wandersson.98@gmail.com>

---
## [digvijai7/Machine_Learning](https://github.com/digvijai7/Machine_Learning)@[c6330f5e12...](https://github.com/digvijai7/Machine_Learning/commit/c6330f5e12115f11f66ef9595931733ee3d71c79)
#### Tuesday 2023-08-22 20:47:19 by Digvijay Singh Parmar

Add files via upload

## Problem Statement:
🎉🎉 Attention all student data whizzes! We are beyond excited to kick off the "Data Science Student Championship 2023". This year's challenge? A real head-turner: Predicting the 'total_fare' for taxi rides! 🚖

 

As a student, you've undoubtedly hailed a ride when you're late for class or heading out for a late-night study session. Ever wondered how the total cost of your ride is determined? Well, it's time to switch gears from passenger to predictor. In this thrilling hackathon, you'll put your data science skills to the ultimate test by predicting the total fare of a ride-hailing trip. 🎯

 

This championship is designed not just to put your skills under the microscope, but to refine them, strengthen them, and prepare you for real-world problem-solving scenarios. And that's not all! You'll be delving into a fundamental issue in the world of transportation economics.

 
## Meta Data:
* ⏱️ 'trip_duration': How long did the journey last?[in Seconds]
* 🛣️ 'distance_traveled': How far did the taxi travel?[in Km]
* 🧑‍🤝‍🧑 'num_of_passengers': How many passengers were in the taxi?
* 💵 'fare': What's the base fare for the journey?[In INR]
* 💲 'tip': How much did the driver receive in tips?[In INR]
* 🎀 'miscellaneous_fees': Were there any additional charges during the trip?e.g. tolls, convenience fees, GST etc.[In INR]
* 💰 'total_fare': The grand total for the ride (this is your prediction target!).[In INR]
* ⚡ 'surge_applied': Was there a surge pricing applied? Yes or no?

---
## [Pixie-Pie/ProceedPersonalTraining](https://github.com/Pixie-Pie/ProceedPersonalTraining)@[1a1150a68c...](https://github.com/Pixie-Pie/ProceedPersonalTraining/commit/1a1150a68c5fcc804a084ef7bfc1ae0ca9dcc235)
#### Tuesday 2023-08-22 20:48:18 by Ali

Update README.md

Proceed Personal Training offers coaching and nutrition services tailored to both individual and group setting, with a specialization in online coaching. The website serves as comprehensive resource for prospective clients, offering insights into the services, teams, pricing, and clients results. Potential clients can gain inspiration and insight offered by the work of Proceed Personal Training by exploring the transformations achieved by our previous clients.

 

UX

The website features a clean and straightforward layout, designed to facilitate easy access to all the essential information for our clients. Visitors can readily discover details about our team, services, pricing, contact information, gallery, and testimonials from previous clients.

 

User Stories

As a new user of the website, I aim to understand the purpose and offerings of this platform.

As a new user of the website, I'm interested in accessing the pricing information.

As a new user of the website, my goal is to locate the contact details for reaching out.

As a new user of the website, I'd like to explore the before-and-after section showcasing transformations.

As a new user of the website, I'm curious to know about the individuals working at Proceed Personal Training.

As a new user of the website, I intend to find the means to get in touch with the team.

As a new user of the website, I'm looking to connect on various social media platforms to receive updates.

SCOPE

Features:

User-Friendly Navigation: Intuitive and effortless navigation throughout the website.

Services and Pricing: Comprehensive list of offered services along with corresponding pricing details.

Employee Directory: A dedicated section showcasing the team members and the services they offer.

Client Progress Gallery: Visual representation of client transformations and progress.

Testimonials: Collection of testimonials and feedback from past clients.

Contact Form: An interactive form allowing clients to get in touch directly.

Contact Information: Clear and accessible contact details for easy communication.

Social Media Integration: Inclusion of social media links in the website footer, enabling users to follow the salon on various platforms for updates.

Structure

Header: Logo on the left-hand corner with the navigation bar on the right-hand corner

Footer: Contact information, social media link

Home Page

Homepage image: The image can be found at the top of the home page, positioned just below the header. It conveys a positive impression to potential clients, portraying a group of content individuals. The photo's link is: https://www.pexels.com/photo/three-women-kneeling-on-floor-866023/

About us and welcome message under the homepage image:

At Proceed Personal Training, our expertise lies in the realms of fitness and nutrition. Our focus revolves around aiding clients in realizing their fitness aspirations, whether it's shedding or gaining weight, sculpting their body composition, building muscle mass, achieving a lean physique, or enhancing stamina. We craft personalized fitness and nutrition plans that are meticulously tailored to align with your unique requirements and lifestyle.

Exercise and a balanced diet stand as key pillars in weight management, but it's essential to acknowledge the additional vital factors influencing your journey. If you want to learn more about other vital factors, we encourage you to reach out to us through the provided form below or by visiting our "Contact Us" section, which offers various avenues to connect with our team.

Your success is our ultimate motivation, and we're ready to be your enthusiastic and dedicated supporters every step of the way.

Form – name, email, contact number, message, send button.

Privacy notice under the form: Proceed Personal Training is committed to protecting and respecting your privacy, we will only use your personal information to answer your query and provide the products and services you requested from us.

Gallery: The "Gallery" button offers a swift glimpse into a selection of client images. A single click on this button will seamlessly transition you to the complete gallery for a more immersive experience.

---
## [digvijai7/Machine_Learning](https://github.com/digvijai7/Machine_Learning)@[c98155ae55...](https://github.com/digvijai7/Machine_Learning/commit/c98155ae552a458112a5f89c0ea7b5eb70530175)
#### Tuesday 2023-08-22 20:56:07 by Digvijay Singh Parmar

Add files via upload

## Problem Statement
A key challenge for the insurance industry is to charge each customer an appropriate premium for the risk they represent. The ability to predict a correct claim amount has a significant impact on insurer's management decisions and financial statements. Predicting the cost of claims in an insurance company is a real-life problem that needs to be solved in a more accurate and automated way. Several factors determine the cost of claims based on health factors like BMI, age, smoker, health conditions and others. Insurance companies apply numerous techniques for analyzing and predicting health insurance costs

## Data Definition

**age** : Age of the policyholder (Numeric)

**sex:** Gender of policyholder (Categoric)

**weight:** Weight of the policyholder (Numeric)

**bmi**: Body mass index, providing an understanding of body, weights that are relatively high or low relative to height, objective index of body weight (kg / m ^ 2) using the ratio of height to weight (Numeric)

**no_of_dependents:** Number of dependent persons on the policyholder (Numeric)

**smoker:** Indicates policyholder is a smoker or a non-smoker (non-smoker=0;smoker=1) (Categoric)

**claim:** The amount claimed by the policyholder (Numeric)

**bloodpressure:** Bloodpressure reading of policyholder (Numeric)

**diabetes:** Indicates policyholder suffers from diabetes or not (non-diabetic=0; diabetic=1) (Categoric)

**regular_ex:** A policyholder regularly excercises or not (no-excercise=0; excercise=1) (Categoric)

**job_title:** Job profile of the policyholder (Categoric)

**city:** The city in which the policyholder resides (Categoric)

**hereditary_diseases:**  A policyholder suffering from a hereditary diseases or not (Categoric)

---
## [Mission23/Mission23](https://github.com/Mission23/Mission23)@[7761971b68...](https://github.com/Mission23/Mission23/commit/7761971b68a3eaab197e29ca38d8933a0140aad3)
#### Tuesday 2023-08-22 21:21:53 by Micah

If ever the CIA left a blueprint in the clear it was this.

I was just trying to get her last name.  Then I stared at the woman first met in my sister's house as the housekeeper, she was a personal assistant to my aunt Mary after they killed my Uncle Clennon.  They definitely surprised my family in Sandy Hook, TN.  Surprise Annie, or should I call you "Hurricane Annie," are you surprised?  We cannot and will not be killed by you, your armies, etc...  Wait till I tell the world about Legacy.  Maybe I'll give guided tours here to make money since you kill everyone by surprise.  Did my boss surprise you?  He's had ENOUGH of you, and your ilks shit?  I'll wait on your next suitcase delivery man to show up.  Tell my minders I need cigarettes, IM GOING TO BE TYPING FOR A WHILE TONIGHT

He is an asshole about getting the word out.  HE SURPRISED ME THIS MORNING THOUGH, when you had the NSA attack NameCheap's servers for following the law and standard praxtices and their own policies and didn't kill our domain.  I warned you and the FBI, if it says SotC, you may as well consider that His signature and leave it the fuck alone.

bye.. Micah

ps...  No need for lawyers, Sector 7 doesn't have trials.

---
## [dmatos2012/nushell](https://github.com/dmatos2012/nushell)@[ad49c17eba...](https://github.com/dmatos2012/nushell/commit/ad49c17ebacd04585fb4355e079ec87d7fc63d8d)
#### Tuesday 2023-08-22 21:25:54 by Kiryl Mialeshka

fix(nu-parser): do not update plugin.nu file on nu startup (#10007)

<!--
if this PR closes one or more issues, you can automatically link the PR
with
them by using one of the [*linking
keywords*](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword),
e.g.
- this PR should close #xxxx
- fixes #xxxx

you can also mention related issues, PRs or discussions!
-->

# Description

I've been investigating the [issue
mentioned](https://github.com/nushell/nushell/pull/9976#issuecomment-1673290467)
in my prev pr and I've found that plugin.nu file that is used to cache
plugins signatures gets overwritten on every nushell startup and that
may actually mess up with the file content if 2 or more instances of
nushell will run simultaneously.

To reproduce:
1. register at least 2 plugins in your local nushell
2. remember how many entries you have in plugin.nu with `open
$nu.plugin-path | find nu_plugin`
3. run 
    - either `cargo test` inside nushell repo
- or run smth like this `1..100 | par-each {|it| $"(random integer
1..100)ms" | into duration | sleep $in; nu -c "$nu.plugin-path"}` to
simulate parallel access. This approach is not so reliable to reproduce
as running test but still a good point that it may effect users actually
4. validate that your `plugin.nu` file was stripped

<!--
Thank you for improving Nushell. Please, check our [contributing
guide](../CONTRIBUTING.md) and talk to the core team before making major
changes.

Description of your pull request goes here. **Provide examples and/or
screenshots** if your changes affect the user experience.
-->

# Solution

In this pr I've refactored the code of handling the `register` command
to minimize code duplications and make sure that overwrite of
`plugin.nu` file is happen only when user calls the command and not on
nu startup

Another option would be to use temp `plugin.nu` when running tests, but
as the issue actually can affect users I've decided to prevent
unnecessary writing at all. Although having isolated `plugin.nu` still
worth of doing

# User-Facing Changes
<!-- List of all changes that impact the user experience here. This
helps us keep track of breaking changes. -->
It changes the behaviour actually as the call `register <plugin>
<signature>` now doesn't updates `plugin.nu` and just reads signatures
to the memory. But as I understand that kind of call with explicit
signature is meant to use only by nushell itself in the `plugin.nu` file
only. I've asked about it in
[discord](https://discordapp.com/channels/601130461678272522/615962413203718156/1140013448915325018)

<!--
Don't forget to add tests that cover your changes.

Make sure you've run and fixed any issues with these commands:

- `cargo fmt --all -- --check` to check standard code formatting (`cargo
fmt --all` applies these changes)
- `cargo clippy --workspace -- -D warnings -D clippy::unwrap_used -A
clippy::needless_collect -A clippy::result_large_err` to check that
you're using the standard code style
- `cargo test --workspace` to check that all tests pass
- `cargo run -- -c "use std testing; testing run-tests --path
crates/nu-std"` to run the tests for the standard library

> **Note**
> from `nushell` you can also use the `toolkit` as follows
> ```bash
> use toolkit.nu # or use an `env_change` hook to activate it
automatically
> toolkit check pr
> ```
-->

# After Submitting
<!-- If your PR had any user-facing changes, update [the
documentation](https://github.com/nushell/nushell.github.io) after the
PR is merged, if necessary. This will help us keep the docs up to date.
-->

Actually, I think the way plugins are stored might be reworked to
prevent or mitigate possible issues further:
- problem with writing to file may still arise if we try to register in
parallel as several instances will write to the same file so the lock
for the file might be required
- using additional parameters to command like `register` to implement
some internal logic could be misleading to the users
- `register` call actually affects global state of nushell that sounds a
little bit inconsistent with immutability and isolation of other parts
of the nu. See issues
[1](https://github.com/nushell/nushell/issues/8581),
[2](https://github.com/nushell/nushell/issues/8960)

---
## [FalloutFalcon/Shiptest](https://github.com/FalloutFalcon/Shiptest)@[f07cb3bd3b...](https://github.com/FalloutFalcon/Shiptest/commit/f07cb3bd3b52bfbdb7994aaf4ae68dcf90d57d2f)
#### Tuesday 2023-08-22 22:28:58 by Bjarl

Overmap 4.7: Gas Giants, More Storms, 8 hours of work (#1997)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Adds some content based on sprites I saw sitting around in the overmap
file, mainly carp storms and dust storms.
Carp storms throw space carp at you. Dust storms throw dust.

Also adds gas giants, a place to harvest gasses if you're low, and don't
want to stop at a planet. They *should* be persistent. Your average gas
giant mix is very cold, very high pressure, and absolutely not something
you want to breathe. Plasma giants are cold and allow harvesting of
plasma.

Electrical storms have been rebalanced to not Explode Your Ship. Minor
and Moderate ones will now only shock and damage objects and mobs, major
ones will still explode you, so remain careful.



![image](https://github.com/shiptest-ss13/Shiptest/assets/94164348/84257435-32de-45a5-8a8d-d9aa30021f90)
Example overmap with some carp migrations.


https://github.com/shiptest-ss13/Shiptest/assets/94164348/5c30fa9a-c7e4-453a-99a6-5c3564946b26
flying through a minor electrical storm


https://github.com/shiptest-ss13/Shiptest/assets/94164348/db7fcdf0-3f7a-4830-821e-a4a7106632ba
gas giant


https://github.com/shiptest-ss13/Shiptest/assets/94164348/0a5f0575-b7d9-4e3f-9e13-942a8fdf8617

![image](https://github.com/shiptest-ss13/Shiptest/assets/94164348/6bb5ddc2-373a-4dd9-9a63-0f6f0bdd26a9)

plasma giant

https://github.com/shiptest-ss13/Shiptest/assets/94164348/9268c293-39f3-4306-889e-f8c19067cec1

A particularly dusty solar system

![image](https://github.com/shiptest-ss13/Shiptest/assets/94164348/5b27e2a8-1cc1-47bb-95b8-e9d5c3ba8e71)


I might try and fix ion storms but I don't see what might be breaking
them.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
More content for the overmap / balancing out some old systems
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Planets now can (and will) play a sound when you land on them
add: Gas / Plasma giants, cold, dockable worlds with absolutely no
livable surfaces. As a matter of fact it's all chasm. All highly
pressurized, gas rich, chasm.
add: Dust storms and carp storms now grace the sector. 
add: physical storms (dust, carp, asteroid), will now only trigger if
you go through them too fast. Take it easy and you might get through
unscathed.
add: planets will now have a name on the overmap
add: overmap hazards now have a description
tweak: Space carp can now survive in hyperspace, their natural habitat
balance: minor and moderate electrical storms will no longer Explode you
balance: asteroid storm lists have been trimmed of Extremely Deadly ones
fix: restores planet naming behavior, I believe this was unintentionally
removed at some point
fix: Ion storms work again. Fuck you whoever touched them last.
soundadd: planet_landing_1 and planet_landing_2, (tech_notification and
sos_morse_code from CM respectively. I don't know how to attribute
properly please tell me how if you have issue with this attribution
because I did not make these sounds they're from Colonial Marines)
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: Bjarl <94164348+Bjarl@users.noreply.github.com>

---
## [dieamond13/tgstation-dieamond](https://github.com/dieamond13/tgstation-dieamond)@[52c8da7ea4...](https://github.com/dieamond13/tgstation-dieamond/commit/52c8da7ea49ef566c9a997a4b7cfc5d3d2a59178)
#### Tuesday 2023-08-22 23:19:15 by Jacquerel

PAI Holochassis are now leashed to an area around their card (#76763)

## About The Pull Request

This change restricts PAI holograms to an area around their assigned PAI
card. If you leave this area, you are teleported back to the card's
location (but not automatically put back into the card).

https://www.youtube.com/watch?v=L2ThEVa4nx8

This setting can be configured from the PAI menu, it's set pretty short
in the video because otherwise it wouldn't teleport when I threw the
card and I like doing that.

![image](https://github.com/tgstation/tgstation/assets/7483112/faf0fa0b-e9d6-4990-8d8c-f30def2892f1)

To accomodate this I set up a component to deal with a reasonably common
problem I have had, "what if I want to track the movement of something
in a box in a bag in someone's inventory". Please tell me if the
solution I came up with is stupid and we already have a better one that
I forgot about.

Also now you can put pAIs inside bots again, by popular request.

## Why It's Good For The Game

Personal AIs are intended to be personal assistants to their owner.
rather than fully independent entities which can pick up their own card
and leave as soon as they spawn.
As "aimless wanderer" players can now possess station bots, pAIs can be
limited to an area around the bearer of their card.

Because the holoform now doesn't contain the card, this also means that
a PAI cannot run off and then be impossible to retrieve. You are always
in control of where it can go.

Also it's funny to throw the card and watch the chicken get teleported
to it.

## Changelog

:cl:
add: Personal AI holograms are now limited to an area around their PAI
card. The size of this are can be configured via the PAI card.
add: pAI cards can now be placed inside bots in order to grant them
control of the bot.
/:cl:

---

